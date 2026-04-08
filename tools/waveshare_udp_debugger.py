#!/usr/bin/env python3
from __future__ import annotations

import json
import queue
import socket
import threading
import time
import tkinter as tk
import zlib
from dataclasses import dataclass
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from typing import Any, Dict, Optional


def _compact_json(payload: Dict[str, Any]) -> bytes:
    return json.dumps(payload, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def encode_with_crc(payload: Dict[str, Any]) -> bytes:
    message = dict(payload)
    message.pop("crc", None)
    raw = _compact_json(message)
    message["crc"] = f"{(zlib.crc32(raw) & 0xFFFFFFFF):08x}"
    return _compact_json(message)


def try_decode_with_crc(data: bytes) -> Optional[Dict[str, Any]]:
    try:
        message = json.loads(data.decode("utf-8", errors="strict"))
    except Exception:
        return None
    if not isinstance(message, dict):
        return None
    crc_text = message.get("crc")
    if not crc_text:
        return message

    unsigned = dict(message)
    unsigned.pop("crc", None)
    raw = _compact_json(unsigned)
    calc = f"{(zlib.crc32(raw) & 0xFFFFFFFF):08x}"
    message["crc_valid"] = str(crc_text).lower() == calc
    return message


@dataclass(frozen=True)
class MotionStep:
    name: str
    pan: Optional[int]
    tilt: Optional[int]


class WaveshareUdpDebugger(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Waveshare UDP Bus Debugger")
        self.geometry("1200x820")
        self.minsize(960, 660)

        self._sock: Optional[socket.socket] = None
        self._lock = threading.Lock()
        self._ui_queue: queue.Queue[tuple[str, str]] = queue.Queue()
        self._seq = 0
        self._sequence_token = 0

        self._build_ui()
        self.after(50, self._drain_ui_queue)

    def _build_ui(self) -> None:
        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)

        top = ttk.Frame(self, padding=10)
        top.grid(row=0, column=0, sticky="ew")
        for column in range(10):
            top.columnconfigure(column, weight=1 if column in (1, 3, 5, 7) else 0)

        ttk.Label(top, text="Host").grid(row=0, column=0, sticky="w")
        self.host_var = tk.StringVar(value="192.168.4.1")
        ttk.Entry(top, textvariable=self.host_var, width=14).grid(row=0, column=1, sticky="ew", padx=(6, 12))

        ttk.Label(top, text="Port").grid(row=0, column=2, sticky="w")
        self.port_var = tk.StringVar(value="9000")
        ttk.Entry(top, textvariable=self.port_var, width=8).grid(row=0, column=3, sticky="ew", padx=(6, 12))

        ttk.Label(top, text="Local Port").grid(row=0, column=4, sticky="w")
        self.local_port_var = tk.StringVar(value="0")
        ttk.Entry(top, textvariable=self.local_port_var, width=8).grid(row=0, column=5, sticky="ew", padx=(6, 12))

        ttk.Label(top, text="Listen ms").grid(row=0, column=6, sticky="w")
        self.listen_ms_var = tk.StringVar(value="900")
        ttk.Entry(top, textvariable=self.listen_ms_var, width=8).grid(row=0, column=7, sticky="ew", padx=(6, 12))

        self.connect_btn = ttk.Button(top, text="Open Socket", command=self._toggle_socket)
        self.connect_btn.grid(row=0, column=8, sticky="ew", padx=(0, 8))

        self.status_var = tk.StringVar(value="Socket closed")
        ttk.Label(top, textvariable=self.status_var).grid(row=0, column=9, sticky="e")

        controls = ttk.LabelFrame(self, text="Bridge Actions", padding=10)
        controls.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 10))
        for column in range(10):
            controls.columnconfigure(column, weight=1)

        ttk.Button(controls, text="Hello", command=self._send_hello).grid(row=0, column=0, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Heartbeat", command=self._send_heartbeat).grid(row=0, column=1, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Bus Ping", command=self._send_bus_ping).grid(row=0, column=2, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Sound Test", command=self._send_sound).grid(row=0, column=3, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Center", command=lambda: self._send_move(90, 35)).grid(row=0, column=4, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Pan Left", command=lambda: self._send_move(20, None)).grid(row=0, column=5, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Pan Right", command=lambda: self._send_move(160, None)).grid(row=0, column=6, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Tilt Low", command=lambda: self._send_move(None, 10)).grid(row=0, column=7, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Tilt High", command=lambda: self._send_move(None, 55)).grid(row=0, column=8, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Stop Sequence", command=self._stop_sequence).grid(row=0, column=9, sticky="ew", padx=4, pady=4)

        ttk.Label(controls, text="Pan").grid(row=1, column=0, sticky="e")
        self.pan_var = tk.StringVar(value="90")
        ttk.Entry(controls, textvariable=self.pan_var, width=8).grid(row=1, column=1, sticky="ew", padx=4, pady=4)

        ttk.Label(controls, text="Tilt").grid(row=1, column=2, sticky="e")
        self.tilt_var = tk.StringVar(value="35")
        ttk.Entry(controls, textvariable=self.tilt_var, width=8).grid(row=1, column=3, sticky="ew", padx=4, pady=4)

        ttk.Label(controls, text="Move ms").grid(row=1, column=4, sticky="e")
        self.move_time_var = tk.StringVar(value="160")
        ttk.Entry(controls, textvariable=self.move_time_var, width=8).grid(row=1, column=5, sticky="ew", padx=4, pady=4)

        ttk.Label(controls, text="Dwell ms").grid(row=1, column=6, sticky="e")
        self.dwell_ms_var = tk.StringVar(value="700")
        ttk.Entry(controls, textvariable=self.dwell_ms_var, width=8).grid(row=1, column=7, sticky="ew", padx=4, pady=4)

        ttk.Label(controls, text="Repeats").grid(row=1, column=8, sticky="e")
        self.repeat_var = tk.StringVar(value="1")
        ttk.Entry(controls, textvariable=self.repeat_var, width=8).grid(row=1, column=9, sticky="ew", padx=4, pady=4)

        ttk.Button(controls, text="Send Move", command=self._send_custom_move).grid(row=2, column=0, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Send Pan Only", command=self._send_custom_pan_only).grid(row=2, column=1, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Send Tilt Only", command=self._send_custom_tilt_only).grid(row=2, column=2, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Pan Sweep", command=self._start_pan_sweep).grid(row=2, column=3, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Tilt Sweep", command=self._start_tilt_sweep).grid(row=2, column=4, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Motion Sweep", command=self._start_motion_sweep).grid(row=2, column=5, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Move + Ping", command=self._move_with_bus_ping).grid(row=2, column=6, sticky="ew", padx=4, pady=4)
        ttk.Button(controls, text="Clear Log", command=self._clear_log).grid(row=2, column=7, sticky="ew", padx=4, pady=4)

        self.result_var = tk.StringVar(value="Ready")
        ttk.Label(controls, textvariable=self.result_var).grid(row=2, column=8, columnspan=2, sticky="ew", padx=4, pady=4)

        info = ttk.LabelFrame(self, text="What To Run", padding=10)
        info.grid(row=2, column=0, sticky="ew", padx=10, pady=(0, 10))
        info.columnconfigure(0, weight=1)
        self.info_var = tk.StringVar(
            value=(
                "Use Send Pan Only or Send Tilt Only to isolate one servo at a time. Motion Sweep runs bus_ping "
                "first, then center, left, right, center, tilt low, tilt high, center, and shows the current "
                "firmware's flat state reply fields like motion_queued, ping_queued, last_pan_cmd, last_tilt_cmd, and uart_rx."
            )
        )
        ttk.Label(info, textvariable=self.info_var, justify="left", wraplength=1120).grid(row=0, column=0, sticky="w")

        log_frame = ttk.LabelFrame(self, text="Raw TX / RX Log", padding=10)
        log_frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=(0, 10))
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)

        self.log = ScrolledText(log_frame, wrap="word", font=("Consolas", 10))
        self.log.grid(row=0, column=0, sticky="nsew")

    def _log(self, text: str) -> None:
        self.log.insert("end", text + "\n")
        self.log.see("end")

    def _clear_log(self) -> None:
        self.log.delete("1.0", "end")

    def _enqueue(self, action: str, payload: str) -> None:
        self._ui_queue.put((action, payload))

    def _drain_ui_queue(self) -> None:
        while True:
            try:
                action, payload = self._ui_queue.get_nowait()
            except queue.Empty:
                break
            if action == "log":
                self._log(payload)
            elif action == "status":
                self.status_var.set(payload)
            elif action == "result":
                self.result_var.set(payload)
            elif action == "info":
                self.info_var.set(payload)
        self.after(50, self._drain_ui_queue)

    def _toggle_socket(self) -> None:
        if self._sock is not None:
            self._close_socket()
        else:
            self._open_socket()

    def _open_socket(self) -> None:
        try:
            local_port = self._int_value(self.local_port_var, 0, 0, 65535)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind(("0.0.0.0", local_port))
            sock.setblocking(False)
            self._sock = sock
            bound_port = sock.getsockname()[1]
            self.connect_btn.configure(text="Close Socket")
            self.status_var.set(f"Socket open on UDP {bound_port}")
            self._log(f"OPEN udp://0.0.0.0:{bound_port}")
        except Exception as exc:
            self._sock = None
            self.status_var.set("Socket open failed")
            self._log(f"ERROR open: {exc}")

    def _close_socket(self) -> None:
        try:
            if self._sock is not None:
                self._sock.close()
        except Exception:
            pass
        self._sock = None
        self.connect_btn.configure(text="Open Socket")
        self.status_var.set("Socket closed")
        self._log("CLOSE")

    def _next_seq(self) -> int:
        self._seq += 1
        if self._seq <= 0:
            self._seq = 1
        return self._seq

    def _next_sequence_token(self) -> int:
        self._sequence_token += 1
        return self._sequence_token

    def _target(self) -> tuple[str, int]:
        host = self.host_var.get().strip() or "192.168.4.1"
        port = self._int_value(self.port_var, 9000, 1, 65535)
        return host, port

    def _listen_ms(self) -> int:
        return self._int_value(self.listen_ms_var, 900, 50, 15000)

    def _dwell_ms(self) -> int:
        return self._int_value(self.dwell_ms_var, 700, 0, 10000)

    def _repeat_count(self) -> int:
        return self._int_value(self.repeat_var, 1, 1, 20)

    def _int_value(self, variable: tk.StringVar, default: int, minimum: int, maximum: int) -> int:
        try:
            value = int(variable.get().strip() or str(default))
        except ValueError:
            value = default
            variable.set(str(default))
        value = max(minimum, min(maximum, value))
        variable.set(str(value))
        return value

    def _build_move_payload(self, pan: Optional[int], tilt: Optional[int]) -> Dict[str, Any]:
        payload: Dict[str, Any] = {
            "move_time_ms": self._int_value(self.move_time_var, 160, 40, 5000),
            "safety": 1,
            "mode": 0,
        }
        if pan is not None:
            payload["pan_cmd"] = pan
        if tilt is not None:
            payload["tilt_cmd"] = tilt
        return payload

    def _drain_socket(self, sock: socket.socket) -> None:
        while True:
            try:
                sock.recvfrom(4096)
            except BlockingIOError:
                break

    def _exchange_packet(
        self,
        label: str,
        packet_type: str,
        payload: Optional[Dict[str, Any]] = None,
        listen_ms: Optional[int] = None,
    ) -> list[Dict[str, Any]]:
        with self._lock:
            if self._sock is None:
                raise RuntimeError("socket is not open")

            host, port = self._target()
            seq = self._next_seq()
            self._drain_socket(self._sock)

            message: Dict[str, Any] = {
                "v": 1,
                "t": packet_type,
                "seq": seq,
                "ts": int(time.time() * 1000),
            }
            if payload is not None:
                message["p"] = payload

            encoded = encode_with_crc(message)
            self._sock.sendto(encoded, (host, port))
            self._enqueue("log", f"TX {label}: {encoded.decode('utf-8', errors='replace')}")

            timeout_ms = listen_ms if listen_ms is not None else self._listen_ms()
            deadline = time.time() + (timeout_ms / 1000.0)
            replies: list[Dict[str, Any]] = []
            while time.time() < deadline:
                try:
                    data, addr = self._sock.recvfrom(4096)
                except BlockingIOError:
                    time.sleep(0.01)
                    continue

                text = data.decode("utf-8", errors="replace")
                self._enqueue("log", f"RX {label} {addr[0]}:{addr[1]}: {text}")
                decoded = try_decode_with_crc(data)
                if decoded is not None:
                    decoded["_from"] = f"{addr[0]}:{addr[1]}"
                    replies.append(decoded)
            return replies

    def _state_reply(self, replies: list[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        for message in reversed(replies):
            if message.get("t") == "state":
                return message
        return replies[-1] if replies else None

    def _state_fields(self, message: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        if not isinstance(message, dict):
            return {}
        payload = message.get("p")
        if isinstance(payload, dict):
            return payload
        return message

    def _extract_bus_diag(self, replies: list[Dict[str, Any]]) -> str:
        for message in reversed(replies):
            payload = self._state_fields(message)
            if not payload:
                continue
            bus = payload.get("bus")
            if isinstance(bus, dict):
                pan_ok = bool(bus.get("pan_sub_ok") or bus.get("pan_xor_ok"))
                tilt_ok = bool(bus.get("tilt_sub_ok") or bus.get("tilt_xor_ok"))
                return f"pan_ping={'OK' if pan_ok else 'FAIL'} tilt_ping={'OK' if tilt_ok else 'FAIL'}"
            if "ping_queued" in payload or "motion_queued" in payload:
                return (
                    f"parse_ok={payload.get('parse_ok', '-')} "
                    f"ping_queued={payload.get('ping_queued', '-')} "
                    f"motion_queued={payload.get('motion_queued', '-')} "
                    f"uart_rx={payload.get('uart_rx', '-')}"
                )
        return ""

    def _bus_ping_ok(self, replies: list[Dict[str, Any]]) -> bool:
        for message in reversed(replies):
            payload = self._state_fields(message)
            if not payload:
                continue
            bus = payload.get("bus")
            if isinstance(bus, dict):
                return bool(
                    bus.get("pan_sub_ok")
                    or bus.get("pan_xor_ok")
                    or bus.get("tilt_sub_ok")
                    or bus.get("tilt_xor_ok")
                )
            if payload.get("ping_queued") is True and payload.get("parse_ok") is True:
                return True
        return False

    def _summarize_result(self, label: str, replies: list[Dict[str, Any]]) -> str:
        if not replies:
            return f"{label}: no reply"

        ack_count = sum(1 for message in replies if message.get("t") == "ack")
        ack_ok = sum(1 for message in replies if message.get("t") == "ack" and bool(message.get("ok")))
        state_count = sum(1 for message in replies if message.get("t") == "state")
        cap_count = sum(1 for message in replies if message.get("t") == "cap")
        state = self._state_reply(replies)
        state_payload = self._state_fields(state)
        pan_value = state_payload.get("pan", state_payload.get("last_pan_cmd", "-"))
        tilt_value = state_payload.get("tilt", state_payload.get("last_tilt_cmd", "-"))
        motion_value = state_payload.get("motion_queued", "-")
        uart_value = state_payload.get("uart_rx", "-")
        pan_text = f" pan={pan_value}" if state_payload else ""
        tilt_text = f" tilt={tilt_value}" if state_payload else ""
        motion_text = f" motion={motion_value}" if state_payload else ""
        uart_text = f" uart_rx={uart_value}" if state_payload else ""
        bus_diag = self._extract_bus_diag(replies)
        suffix = f" | {bus_diag}" if bus_diag else ""
        return f"{label}: ack_ok={ack_ok}/{ack_count} state={state_count} cap={cap_count}{pan_text}{tilt_text}{motion_text}{uart_text}{suffix}"

    def _format_summary(self, message: Optional[Dict[str, Any]]) -> str:
        if not message:
            return "-"

        payload = self._state_fields(message)
        lines = [
            f"type={message.get('t', '-')}",
            f"from={message.get('_from', '-')}",
            f"crc_valid={message.get('crc_valid', '-')}",
            f"ack_ok={message.get('ok', '-')}",
        ]
        if payload:
            lines.append(f"pan={payload.get('pan', '-')}")
            lines.append(f"tilt={payload.get('tilt', '-')}")
            lines.append(f"fire={payload.get('fire', '-')}")
            lines.append(f"safety={payload.get('safety', '-')}")
            lines.append(f"mode={payload.get('mode', '-')}")
            lines.append(f"acc={payload.get('acc', '-')}")
            lines.append(f"spare={payload.get('spare', '-')}")
            lines.append(f"control_source_mode={payload.get('control_source_mode', '-')}")
            lines.append(f"control_source_active={payload.get('control_source_active', '-')}")
            lines.append(f"rc_link_active={payload.get('rc_link_active', '-')}")
            lines.append(f"parse_ok={payload.get('parse_ok', '-')}")
            lines.append(f"motion_queued={payload.get('motion_queued', '-')}")
            lines.append(f"ping_queued={payload.get('ping_queued', '-')}")
            lines.append(f"last_pan_cmd={payload.get('last_pan_cmd', '-')}")
            lines.append(f"last_tilt_cmd={payload.get('last_tilt_cmd', '-')}")
            lines.append(f"uart_rx={payload.get('uart_rx', '-')}")
            lines.append(f"uart_markers={payload.get('uart_markers', '-')}")
            lines.append(f"uart_windows={payload.get('uart_windows', '-')}")
            lines.append(f"uart_state={payload.get('uart_state', '-')}")
            bus = payload.get("bus")
            if isinstance(bus, dict):
                lines.append(
                    "bus_ping="
                    f"pan(sub={bus.get('pan_sub_ok', '-')},xor={bus.get('pan_xor_ok', '-')}) "
                    f"tilt(sub={bus.get('tilt_sub_ok', '-')},xor={bus.get('tilt_xor_ok', '-')})"
                )
        return "\n".join(lines)

    def _send_packet(self, label: str, packet_type: str, payload: Optional[Dict[str, Any]] = None) -> None:
        def run() -> None:
            try:
                replies = self._exchange_packet(label, packet_type, payload)
                self._enqueue("result", self._summarize_result(label, replies))
                self._enqueue("info", self._format_summary(self._state_reply(replies)))
            except Exception as exc:
                self._enqueue("log", f"ERROR {label}: {exc}")
                self._enqueue("result", f"{label}: failed")

        threading.Thread(target=run, daemon=True).start()

    def _send_hello(self) -> None:
        self._send_packet("hello", "hello", {"role": "waveshare-debugger", "want": ["ack", "state", "cap"]})

    def _send_heartbeat(self) -> None:
        self._send_packet("heartbeat", "hb", {})

    def _send_bus_ping(self) -> None:
        self._send_packet("bus_ping", "cmd", {"action": "bus_ping"})

    def _send_sound(self) -> None:
        self._send_packet(
            "sound",
            "cmd",
            {"action": "sound", "freq_hz": 1400, "duration_ms": 220, "volume_pct": 100},
        )

    def _send_custom_move(self) -> None:
        pan = self._int_value(self.pan_var, 90, 0, 220)
        tilt = self._int_value(self.tilt_var, 35, 0, 70)
        self._send_move(pan, tilt)

    def _send_custom_pan_only(self) -> None:
        pan = self._int_value(self.pan_var, 90, 0, 220)
        self._send_move(pan, None)

    def _send_custom_tilt_only(self) -> None:
        tilt = self._int_value(self.tilt_var, 35, 0, 70)
        self._send_move(None, tilt)

    def _send_move(self, pan: Optional[int], tilt: Optional[int]) -> None:
        self._send_packet("move", "cmd", self._build_move_payload(pan, tilt))

    def _stop_sequence(self) -> None:
        self._next_sequence_token()
        self._enqueue("result", "sequence: stop requested")
        self._enqueue("log", "INFO sequence stop requested")

    def _run_sequence(self, label: str, steps: list[MotionStep], include_bus_ping: bool) -> None:
        token = self._next_sequence_token()
        dwell_ms = self._dwell_ms()
        repeats = self._repeat_count()

        def run() -> None:
            try:
                if include_bus_ping:
                    ping_replies = self._exchange_packet("motion preflight", "cmd", {"action": "bus_ping"}, listen_ms=max(1200, self._listen_ms()))
                    ping_result = self._summarize_result("motion preflight", ping_replies)
                    self._enqueue("log", f"INFO {ping_result}")
                    self._enqueue("info", self._format_summary(self._state_reply(ping_replies)))
                    if not self._bus_ping_ok(ping_replies):
                        self._enqueue("result", "motion sweep: bus_ping failed, move packets may still send")
                    else:
                        self._enqueue("result", "motion sweep: bus_ping OK, starting step sequence")

                total_steps = len(steps) * repeats
                completed = 0
                last_replies: list[Dict[str, Any]] = []

                for repeat_index in range(repeats):
                    for step in steps:
                        if token != self._sequence_token:
                            self._enqueue("result", f"{label}: cancelled at step {completed}/{total_steps}")
                            return

                        completed += 1
                        step_label = f"{label} {completed}/{total_steps} {step.name}"
                        last_replies = self._exchange_packet(step_label, "cmd", self._build_move_payload(step.pan, step.tilt))
                        self._enqueue("result", self._summarize_result(step_label, last_replies))
                        self._enqueue("info", self._format_summary(self._state_reply(last_replies)))

                        if dwell_ms > 0 and completed < total_steps:
                            time.sleep(dwell_ms / 1000.0)

                self._enqueue("result", f"{label}: completed {total_steps} steps")
                self._enqueue("info", self._format_summary(self._state_reply(last_replies)))
            except Exception as exc:
                self._enqueue("log", f"ERROR {label}: {exc}")
                self._enqueue("result", f"{label}: failed")

        threading.Thread(target=run, daemon=True).start()

    def _start_pan_sweep(self) -> None:
        tilt = self._int_value(self.tilt_var, 35, 0, 70)
        steps = [
            MotionStep("left", 20, tilt),
            MotionStep("center", 90, tilt),
            MotionStep("right", 160, tilt),
            MotionStep("center", 90, tilt),
        ]
        self._run_sequence("pan sweep", steps, include_bus_ping=False)

    def _start_tilt_sweep(self) -> None:
        pan = self._int_value(self.pan_var, 90, 0, 220)
        steps = [
            MotionStep("low", pan, 10),
            MotionStep("center", pan, 35),
            MotionStep("high", pan, 55),
            MotionStep("center", pan, 35),
        ]
        self._run_sequence("tilt sweep", steps, include_bus_ping=False)

    def _start_motion_sweep(self) -> None:
        steps = [
            MotionStep("center", 90, 35),
            MotionStep("pan_left", 20, 35),
            MotionStep("pan_right", 160, 35),
            MotionStep("center", 90, 35),
            MotionStep("tilt_low", 90, 10),
            MotionStep("tilt_high", 90, 55),
            MotionStep("center", 90, 35),
        ]
        self._run_sequence("motion sweep", steps, include_bus_ping=True)

    def _move_with_bus_ping(self) -> None:
        pan = self._int_value(self.pan_var, 90, 0, 220)
        tilt = self._int_value(self.tilt_var, 35, 0, 70)
        steps = [MotionStep("requested_move", pan, tilt)]
        self._run_sequence("move + ping", steps, include_bus_ping=True)


def main() -> int:
    app = WaveshareUdpDebugger()
    return app.mainloop() or 0


if __name__ == "__main__":
    raise SystemExit(main())
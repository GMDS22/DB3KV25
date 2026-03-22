"""
Smart Sentry v2 — Standalone Communication

Handles direct serial (USB COM) and UDP (WiFi) communication with the ESP32
and optional Debug Board, independent of the main application's serial pipeline.

Connection Modes:
    0  ESP32 USB only         → full ASCII protocol on one COM port
    1  ESP32 USB + Debug Board USB  → bus servo pan/tilt on Debug Board COM,
                                      IO tokens on ESP32 COM  (2 USB cables)
    2  ESP32 WiFi + Debug Board USB → bus servo pan/tilt on Debug Board COM,
                                      IO tokens over UDP       (1 USB cable)
    3  ESP32 WiFi + Debug Board on ESP32 UART2 → full ASCII protocol over UDP
                                                 (no runtime USB)

ESP32 ASCII protocol: ``P{pan}T{tilt}F{fire}L{led}R{laser}G{acc3}S{safety}M{mode}\\n``
Bus servo protocol:    Yahboom-style register write (0xFF 0xFF ID LEN INST REG …)
"""

from __future__ import annotations

import json
import os
import socket
import threading
import time
import zlib
from typing import Any, Callable, Dict, Optional

import serial as _serial
import serial.tools.list_ports as _list_ports

from .sentry_v2_config import (
    SENTRY_PAN_MAX,
    SENTRY_PAN_MIN,
    SENTRY_TILT_MAX,
    SENTRY_TILT_MIN,
)


class SentryV2Comm:
    """Self-contained ESP32 + Debug Board communication for Smart Sentry v2."""

    PAN_OUTPUT_MIN = SENTRY_PAN_MIN
    PAN_OUTPUT_MAX = SENTRY_PAN_MAX
    TILT_OUTPUT_MIN = SENTRY_TILT_MIN
    TILT_OUTPUT_MAX = SENTRY_TILT_MAX

    # --- Connection mode constants ---
    MODE_ESP32_USB = 0           # Single USB — full ASCII to ESP32
    MODE_DUAL_USB = 1            # Debug Board USB (pan/tilt) + ESP32 USB (IO)
    MODE_WIFI_DEBUG_USB = 2      # Debug Board USB (pan/tilt) + ESP32 WiFi (IO)
    MODE_WIFI_FULL = 3           # Everything over WiFi (debug board on ESP32)

    MODE_LABELS = [
        "ESP32 USB",
        "ESP32 USB + Debug Board USB",
        "ESP32 WiFi + Debug Board USB",
        "ESP32 WiFi + Debug Board on ESP32 UART",
    ]

    def __init__(self) -> None:
        # Primary ESP32 serial (modes 0, 1)
        self._ser: Optional[_serial.Serial] = None
        # Debug board serial (modes 1, 2)
        self._bus_ser: Optional[_serial.Serial] = None
        # UDP socket (modes 2, 3)
        self._sock: Optional[socket.socket] = None
        self._udp_target: Optional[tuple] = None

        self._mode: int = self.MODE_ESP32_USB
        self._lock = threading.Lock()

        # Accessory state (tracked locally)
        self.led_on: bool = False
        self.laser_on: bool = False
        self.safety_armed: bool = False   # False=LOCKED (S1), True=ARMED (S0)
        self.trigger_mode_bb: bool = False  # False=Water M0, True=BB M1

        # Direction inversion
        self.invert_pan: bool = False
        self.invert_tilt: bool = False

        # Bus servo config
        self.pan_servo_id: int = 1
        self.tilt_servo_id: int = 2
        self.bus_servo_time_ms: int = 20
        self._bus_checksum_mode: str = "auto"  # "auto", "sub", or "xor"
        self._bus_servo_ping_ok: bool = False

        # Diagnostics
        self._last_cmd: str = ""
        self._last_error: str = ""
        self._udp_seq: int = 0
        
        # PIR event callback (called when sensor data is received)
        self._on_pir_event: Optional[Callable[[int, float], None]] = None

    # ------------------------------------------------------------------ #
    #  Port scanning
    # ------------------------------------------------------------------ #

    @staticmethod
    def list_serial_ports() -> list:
        """Return list of (port, description) tuples for available COM ports."""
        return [(p.device, p.description) for p in _list_ports.comports()]

    # ------------------------------------------------------------------ #
    #  Connection management
    # ------------------------------------------------------------------ #

    def connect(
        self,
        mode: int,
        *,
        esp32_port: str = "",
        esp32_baud: int = 115200,
        debug_port: str = "",
        debug_baud: int = 115200,
        udp_host: str = "192.168.4.1",
        udp_port: int = 9000,
    ) -> bool:
        """Open connections for the specified mode. Returns True on success.

        Sets ``_connect_details`` with per-link status for the UI.
        """
        self.disconnect()
        self._mode = int(mode)
        self._connect_details = {}          # per-link status dict
        self._last_error = ""
        try:
            if self._mode == self.MODE_ESP32_USB:
                ok = self._open_serial(esp32_port, esp32_baud, primary=True)
                self._connect_details["ESP32 USB"] = (ok, esp32_port if ok else self._last_error)
                return ok

            elif self._mode == self.MODE_DUAL_USB:
                ok_bus = self._open_serial(debug_port, debug_baud, primary=False)
                bus_err = self._last_error
                if ok_bus:
                    checksum_mode = self._probe_bus_servo_checksum(self._bus_ser)
                    if checksum_mode is not None:
                        self._connect_details["Debug Board"] = (True, f"{debug_port} ({checksum_mode} checksum)")
                    else:
                        self._connect_details["Debug Board"] = (True, f"{debug_port} (auto checksum fallback)")
                else:
                    self._connect_details["Debug Board"] = (False, bus_err)

                ok_esp = self._open_serial(esp32_port, esp32_baud, primary=True)
                esp_err = self._last_error
                self._connect_details["ESP32 USB"] = (ok_esp, esp32_port if ok_esp else esp_err)

                if not ok_bus and not ok_esp:
                    self._last_error = f"Both failed — Debug: {bus_err} | ESP32: {esp_err}"
                elif not ok_bus:
                    self._last_error = f"Debug board failed: {bus_err}"
                elif not ok_esp:
                    self._last_error = f"ESP32 failed: {esp_err}"
                return ok_bus and ok_esp

            elif self._mode == self.MODE_WIFI_DEBUG_USB:
                ok_bus = self._open_serial(debug_port, debug_baud, primary=False)
                bus_err = self._last_error
                if ok_bus:
                    checksum_mode = self._probe_bus_servo_checksum(self._bus_ser)
                    if checksum_mode is not None:
                        self._connect_details["Debug Board"] = (True, f"{debug_port} ({checksum_mode} checksum)")
                    else:
                        self._connect_details["Debug Board"] = (True, f"{debug_port} (auto checksum fallback)")
                else:
                    self._connect_details["Debug Board"] = (False, bus_err)

                ok_udp = self._open_udp(udp_host, udp_port)
                udp_err = self._last_error
                self._connect_details["ESP32 WiFi"] = (ok_udp, f"{udp_host}:{udp_port}" if ok_udp else udp_err)

                if not ok_bus and not ok_udp:
                    self._last_error = f"Both failed — Debug: {bus_err} | WiFi: {udp_err}"
                elif not ok_bus:
                    self._last_error = f"Debug board failed: {bus_err}"
                elif not ok_udp:
                    self._last_error = f"WiFi failed: {udp_err}"
                return ok_bus and ok_udp

            elif self._mode == self.MODE_WIFI_FULL:
                ok = self._open_udp(udp_host, udp_port)
                self._connect_details["ESP32 WiFi"] = (ok, f"{udp_host}:{udp_port}" if ok else self._last_error)
                return ok

            else:
                self._last_error = f"Unknown mode: {self._mode}"
                return False
        except Exception as e:
            self._last_error = str(e)
            return False

    def _open_serial(self, port: str, baud: int, *, primary: bool) -> bool:
        def _normalize_serial_port_name(raw_port: str) -> str:
            try:
                port_text = str(raw_port or "").strip()
            except Exception:
                return ""
            if not port_text:
                return ""

            port_upper = port_text.upper()
            if port_upper.startswith("\\\\.\\COM"):
                return "\\\\.\\COM" + port_text[8:].strip()

            token = port_text.split()[0].strip().rstrip(":")
            token_upper = token.upper()
            if token_upper.startswith("COM") and len(token) > 3:
                suffix = token[3:].strip()
                if suffix.isdigit():
                    return f"COM{int(suffix)}"
            if token.isdigit():
                return f"COM{int(token)}"
            return port_text

        try:
            normalized_port = _normalize_serial_port_name(port)
            if not normalized_port:
                self._last_error = "No COM port specified"
                return False

            try_ports = [normalized_port]
            if (
                os.name == "nt"
                and normalized_port.upper().startswith("COM")
                and not normalized_port.startswith("\\\\.\\")
            ):
                try:
                    if int(normalized_port[3:]) >= 10:
                        try_ports.append("\\\\.\\" + normalized_port)
                except Exception:
                    pass

            last_error = ""
            ser = None
            for candidate in try_ports:
                try:
                    ser = _serial.Serial(candidate, baud, timeout=0.1, write_timeout=1)
                    break
                except Exception as e:
                    last_error = str(e)
                    ser = None

            if ser is None:
                self._last_error = last_error or f"could not open port '{normalized_port}'"
                return False

            if primary:
                self._ser = ser
            else:
                self._bus_ser = ser
            return True
        except Exception as e:
            self._last_error = str(e)
            return False

    def _open_udp(self, host: str, port: int) -> bool:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setblocking(False)
            self._sock = sock
            self._udp_target = (host, int(port))
            return True
        except Exception as e:
            self._last_error = str(e)
            return False

    @staticmethod
    def _compact_json(obj: Dict[str, Any]) -> bytes:
        return json.dumps(obj, separators=(",", ":"), ensure_ascii=True).encode("utf-8")

    def _build_udp_packet(self, payload: Dict[str, Any]) -> bytes:
        with self._lock:
            self._udp_seq = (self._udp_seq + 1) & 0x7FFFFFFF
            if self._udp_seq == 0:
                self._udp_seq = 1
            seq = self._udp_seq
        msg = {
            "v": 1,
            "t": "cmd",
            "seq": seq,
            "ts": int(time.time() * 1000),
            "p": payload,
        }
        raw = self._compact_json(msg)
        msg["crc"] = f"{(zlib.crc32(raw) & 0xFFFFFFFF):08x}"
        return self._compact_json(msg)

    def _send_udp_payload(self, payload: Dict[str, Any], *, label: str) -> bool:
        with self._lock:
            sock = self._sock
            udp_target = self._udp_target
        try:
            if sock is None or udp_target is None:
                return False
            data = self._build_udp_packet(payload)
            sock.sendto(data, udp_target)
            self._last_cmd = label
            return True
        except Exception as e:
            self._last_error = str(e)
            return False

    def _safe_close_serial(self, ser: Optional[_serial.Serial]) -> None:
        if ser is None:
            return
        try:
            cancel_read = getattr(ser, "cancel_read", None)
            if callable(cancel_read):
                cancel_read()
        except Exception:
            pass
        try:
            cancel_write = getattr(ser, "cancel_write", None)
            if callable(cancel_write):
                cancel_write()
        except Exception:
            pass
        try:
            ser.close()
        except Exception:
            pass

    def disconnect(self) -> None:
        """Close all open connections."""
        with self._lock:
            ser = self._ser
            bus_ser = self._bus_ser
            sock = self._sock
            self._ser = None
            self._bus_ser = None
            self._sock = None
            self._udp_target = None

        self._safe_close_serial(ser)
        self._safe_close_serial(bus_ser)
        if sock is not None:
            try:
                sock.close()
            except Exception:
                pass

    def is_connected(self) -> bool:
        m = self._mode
        if m == self.MODE_ESP32_USB:
            return self._ser is not None and self._ser.is_open
        elif m == self.MODE_DUAL_USB:
            return (
                self._ser is not None and self._ser.is_open
                and self._bus_ser is not None and self._bus_ser.is_open
            )
        elif m == self.MODE_WIFI_DEBUG_USB:
            return (
                self._bus_ser is not None and self._bus_ser.is_open
                and self._sock is not None and self._udp_target is not None
            )
        elif m == self.MODE_WIFI_FULL:
            return self._sock is not None and self._udp_target is not None
        return False

    def connection_info(self) -> str:
        if not self.is_connected():
            return "Disconnected"
        m = self._mode
        if m == self.MODE_ESP32_USB:
            return f"ESP32 USB: {self._ser.port} @ {self._ser.baudrate}"
        elif m == self.MODE_DUAL_USB:
            return f"ESP32: {self._ser.port} | Debug: {self._bus_ser.port}"
        elif m == self.MODE_WIFI_DEBUG_USB:
            return f"WiFi: {self._udp_target[0]}:{self._udp_target[1]} | Debug: {self._bus_ser.port}"
        elif m == self.MODE_WIFI_FULL:
            return f"WiFi: {self._udp_target[0]}:{self._udp_target[1]} (full)"
        return "Unknown"

    # ------------------------------------------------------------------ #
    #  High-level command API
    # ------------------------------------------------------------------ #

    def _normalize_output_angles(self, pan: float, tilt: float) -> tuple[float, float]:
        """Convert logical Smart Sentry aim angles to hardware output angles."""
        pan_out = max(self.PAN_OUTPUT_MIN, min(self.PAN_OUTPUT_MAX, float(pan)))
        tilt_out = max(self.TILT_OUTPUT_MIN, min(self.TILT_OUTPUT_MAX, float(tilt)))
        if self.invert_pan:
            pan_out = self.PAN_OUTPUT_MAX - pan_out
        if self.invert_tilt:
            tilt_out = self.TILT_OUTPUT_MAX - tilt_out
        return (
            max(self.PAN_OUTPUT_MIN, min(self.PAN_OUTPUT_MAX, pan_out)),
            max(self.TILT_OUTPUT_MIN, min(self.TILT_OUTPUT_MAX, tilt_out)),
        )

    # ------------------------------------------------------------------ #
    # PIR sensor event interface  
    # ------------------------------------------------------------------ #

    def set_on_pir_event(self, callback: Optional[Callable[[int, float], None]]) -> None:
        """
        Register a callback to be called when PIR sensor data is received.
        Callback signature: on_pir_event(sensor_id: int, timestamp: float)
        """
        self._on_pir_event = callback

    def inject_pir_event(self, sensor_id: int) -> None:
        """
        Manually inject a PIR sensor event (useful for testing).
        In production, this would be called when parsing telemetry from ESP32.
        """
        if self._on_pir_event is not None:
            self._on_pir_event(sensor_id, time.time())

    def send_command(
        self,
        pan: float,
        tilt: float,
        fire: int = 0,
        move_time_ms: Optional[int] = None,
    ) -> bool:
        """Build and send a full protocol command. Returns True if sent."""
        pan_out, tilt_out = self._normalize_output_angles(pan, tilt)
        m = self._mode
        if m == self.MODE_ESP32_USB:
            return self._send_ascii(pan_out, tilt_out, fire, via_serial=True)
        elif m == self.MODE_DUAL_USB:
            ok_bus = self._send_bus_servo(pan_out, tilt_out, move_time_ms=move_time_ms)
            ok_io = self._send_io_serial(fire)
            return ok_bus and ok_io
        elif m == self.MODE_WIFI_DEBUG_USB:
            ok_bus = self._send_bus_servo(pan_out, tilt_out, move_time_ms=move_time_ms)
            ok_io = self._send_io_udp(fire)
            return ok_bus and ok_io
        elif m == self.MODE_WIFI_FULL:
            return self._send_wifi_full(pan_out, tilt_out, fire, move_time_ms=move_time_ms)
        return False

    def send_movement(
        self,
        pan: float,
        tilt: float,
        *,
        move_time_ms: Optional[int] = None,
    ) -> bool:
        """Send pan/tilt movement without coupling bus-servo motion to IO delivery.

        In Debug Board modes, motion should continue even when ESP32 IO state is unchanged.
        """
        pan_out, tilt_out = self._normalize_output_angles(pan, tilt)
        m = self._mode
        if m == self.MODE_ESP32_USB:
            return self._send_ascii(pan_out, tilt_out, fire=0, via_serial=True)
        if m == self.MODE_DUAL_USB:
            return self._send_bus_servo(pan_out, tilt_out, move_time_ms=move_time_ms)
        if m == self.MODE_WIFI_DEBUG_USB:
            return self._send_bus_servo(pan_out, tilt_out, move_time_ms=move_time_ms)
        if m == self.MODE_WIFI_FULL:
            return self._send_wifi_full(pan_out, tilt_out, fire=0, move_time_ms=move_time_ms)
        return False

    def send_fire_burst(
        self, pan: float, tilt: float,
        burst_count: int = 1, interval_ms: int = 50,
    ) -> None:
        """Send a fire burst (blocking)."""
        delay = max(10, interval_ms) / 1000.0
        for i in range(burst_count):
            self.send_command(pan, tilt, fire=1)
            time.sleep(delay)
            self.send_command(pan, tilt, fire=0)
            if i < burst_count - 1:
                time.sleep(delay)

    def set_led(self, on: bool, pan: float, tilt: float) -> bool:
        self.led_on = on
        return self.send_command(pan, tilt)

    def set_laser(self, on: bool, pan: float, tilt: float) -> bool:
        self.laser_on = on
        return self.send_command(pan, tilt)

    def set_safety(self, armed: bool, pan: float, tilt: float) -> bool:
        self.safety_armed = armed
        return self.send_command(pan, tilt)

    # ------------------------------------------------------------------ #
    #  ASCII protocol  (modes 0, 3)
    # ------------------------------------------------------------------ #

    def _build_ascii(self, pan: float, tilt: float, fire: int = 0) -> str:
        p = int(max(self.PAN_OUTPUT_MIN, min(self.PAN_OUTPUT_MAX, round(pan))))
        t = int(max(self.TILT_OUTPUT_MIN, min(self.TILT_OUTPUT_MAX, round(tilt))))
        print(f"DEBUG: SERIALIZED: P{p} T{t} (from pan={pan:.3f}, tilt={tilt:.3f})")
        f = int(bool(fire))
        led = 1 if self.led_on else 0
        laser = 1 if self.laser_on else 0
        safety = 0 if self.safety_armed else 1
        mode = 1 if self.trigger_mode_bb else 0
        return f"P{p}T{t}F{f}L{led}R{laser}G0S{safety}M{mode}\n"

    def _send_ascii(self, pan: float, tilt: float, fire: int, *, via_serial: bool) -> bool:
        cmd = self._build_ascii(pan, tilt, fire)
        print(f"DEBUG: USB SEND: {cmd.rstrip()}")
        with self._lock:
            ser = self._ser
            sock = self._sock
            udp_target = self._udp_target
        try:
            if via_serial:
                if ser and ser.is_open:
                    ser.write(cmd.encode("utf-8"))
                    self._last_cmd = cmd.rstrip()
                    return True
            else:
                if sock and udp_target:
                    sock.sendto(cmd.encode("utf-8"), udp_target)
                    self._last_cmd = cmd.rstrip()
                    return True
            return False
        except Exception as e:
            self._last_error = str(e)
            return False

    def _send_wifi_full(
        self,
        pan: float,
        tilt: float,
        fire: int,
        *,
        move_time_ms: Optional[int] = None,
    ) -> bool:
        payload: Dict[str, Any] = {
            "pan_cmd": int(max(self.PAN_OUTPUT_MIN, min(self.PAN_OUTPUT_MAX, round(pan)))),
            "tilt_cmd": int(max(self.TILT_OUTPUT_MIN, min(self.TILT_OUTPUT_MAX, round(tilt)))),
            "fire": int(bool(fire)),
            "safety": 0 if self.safety_armed else 1,
            "mode": 1 if self.trigger_mode_bb else 0,
            "led": 1 if self.led_on else 0,
            "laser": 1 if self.laser_on else 0,
        }
        if move_time_ms is not None:
            payload["move_time_ms"] = int(max(0, min(5000, int(move_time_ms))))
        label = (
            f"UDP P{payload['pan_cmd']}T{payload['tilt_cmd']}F{payload['fire']}"
            f"L{payload['led']}R{payload['laser']}S{payload['safety']}M{payload['mode']}"
        )
        return self._send_udp_payload(payload, label=label)

    # ------------------------------------------------------------------ #
    #  Bus servo protocol  (modes 1, 2)
    # ------------------------------------------------------------------ #

    def _deg_to_ticks(self, deg: float) -> int:
        """Map 0..270 degrees to 0..4095 ticks."""
        d = max(0.0, min(270.0, float(deg)))
        return int(round((d / 270.0) * 4095.0))

    def _bus_checksum(self, payload: bytes) -> int:
        s = sum(payload) & 0xFF
        if self._bus_checksum_mode == "xor":
            return (0xFF ^ s) & 0xFF
        return (0xFF - s) & 0xFF

    def _build_ping_packet(self, servo_id: int) -> bytes:
        sid = int(servo_id) & 0xFF
        payload = bytes([sid, 0x02, 0x01])
        chk = self._bus_checksum(payload)
        return b"\xFF\xFF" + payload + bytes([chk])

    def _bus_servo_reply_matches_servo(self, rx: bytes, servo_id: int) -> bool:
        try:
            data = bytes(rx or b"")
            return len(data) >= 3 and data[0] == 0xFF and data[2] == (int(servo_id) & 0xFF)
        except Exception:
            return False

    def _try_ping(self, active_ser: Optional[_serial.Serial], servo_id: int, *, timeout_s: float = 0.12) -> bytes:
        try:
            if active_ser is None or not active_ser.is_open:
                return b""
            try:
                active_ser.reset_input_buffer()
            except Exception:
                pass
            active_ser.write(self._build_ping_packet(servo_id))
            try:
                active_ser.flush()
            except Exception:
                pass

            end = time.time() + float(timeout_s)
            buf = bytearray()
            while time.time() < end and len(buf) < 64:
                try:
                    chunk = active_ser.read(64)
                except Exception:
                    chunk = b""
                if chunk:
                    buf.extend(chunk)
                    if len(buf) >= 4:
                        break
                else:
                    time.sleep(0.01)
            return bytes(buf)
        except Exception:
            return b""

    def _probe_bus_servo_checksum(self, active_ser: Optional[_serial.Serial]) -> Optional[str]:
        if active_ser is None or not active_ser.is_open:
            self._bus_servo_ping_ok = False
            self._bus_checksum_mode = "auto"
            return None

        original_mode = str(self._bus_checksum_mode or "auto")
        try:
            for mode in ("sub", "xor"):
                self._bus_checksum_mode = mode
                for servo_id in (self.pan_servo_id, self.tilt_servo_id):
                    rx = self._try_ping(active_ser, servo_id)
                    if self._bus_servo_reply_matches_servo(rx, servo_id):
                        self._bus_servo_ping_ok = True
                        return mode
            self._bus_servo_ping_ok = False
            self._bus_checksum_mode = "auto"
            return None
        finally:
            if self._bus_checksum_mode not in ("sub", "xor"):
                self._bus_checksum_mode = original_mode if original_mode in ("auto", "sub", "xor") else "auto"

    def _build_servo_packet(self, servo_id: int, pos_ticks: int, time_ms: int) -> bytes:
        """Build a write-position packet (register 0x2A)."""
        sid = servo_id & 0xFF
        pos = max(0, min(4095, pos_ticks))
        t = max(0, min(30000, time_ms))
        payload = bytes([
            sid, 0x07, 0x03, 0x2A,
            (pos >> 8) & 0xFF, pos & 0xFF,
            (t >> 8) & 0xFF, t & 0xFF,
        ])
        chk = self._bus_checksum(payload)
        return b"\xFF\xFF" + payload + bytes([chk])

    def _send_bus_servo(
        self,
        pan: float,
        tilt: float,
        move_time_ms: Optional[int] = None,
    ) -> bool:
        """Send pan/tilt to debug board via bus servo binary packets."""
        with self._lock:
            bus_ser = self._bus_ser
            pan_servo_id = self.pan_servo_id
            tilt_servo_id = self.tilt_servo_id
            checksum_mode = str(self._bus_checksum_mode or "auto").lower()
            default_move_time = self.bus_servo_time_ms
        try:
            if bus_ser is None or not bus_ser.is_open:
                return False
            move_time = int(default_move_time if move_time_ms is None else move_time_ms)
            move_time = max(0, min(1000, move_time))
            pan_ticks = self._deg_to_ticks(pan)
            tilt_ticks = self._deg_to_ticks(tilt)

            def _write_pair(candidate_mode: str) -> None:
                original_mode = self._bus_checksum_mode
                self._bus_checksum_mode = candidate_mode
                try:
                    pan_pkt = self._build_servo_packet(pan_servo_id, pan_ticks, move_time)
                    tilt_pkt = self._build_servo_packet(tilt_servo_id, tilt_ticks, move_time)
                finally:
                    self._bus_checksum_mode = original_mode
                bus_ser.write(pan_pkt)
                bus_ser.write(tilt_pkt)
                try:
                    bus_ser.flush()
                except Exception:
                    pass

            if checksum_mode == "auto":
                for candidate_mode in ("sub", "xor"):
                    _write_pair(candidate_mode)
                    time.sleep(0.002)
            else:
                _write_pair(checksum_mode)

            self._last_cmd = f"BUS P{pan:.0f} T{tilt:.0f} @{move_time}ms [{checksum_mode}]"
            return True
        except Exception as e:
            self._last_error = str(e)
            return False

    # ------------------------------------------------------------------ #
    #  IO token sending  (modes 1, 2)
    # ------------------------------------------------------------------ #

    def _build_io_tokens(self, fire: int = 0) -> dict:
        return {
            "fire": int(bool(fire)),
            "safety": 0 if self.safety_armed else 1,
            "mode": 1 if self.trigger_mode_bb else 0,
            "led": 1 if self.led_on else 0,
            "laser": 1 if self.laser_on else 0,
        }

    def _send_io_serial(self, fire: int = 0) -> bool:
        """Send IO tokens to ESP32 via USB serial (mode 1)."""
        with self._lock:
            ser = self._ser
        try:
            if ser is None or not ser.is_open:
                return False
            io = self._build_io_tokens(fire)
            ser.write(f"S{io['safety']}\n".encode("utf-8"))
            ser.write(f"M{io['mode']}\n".encode("utf-8"))
            ser.write(
                f"F{io['fire']}L{io['led']}R{io['laser']}G0\n".encode("utf-8")
            )
            self._last_cmd += f" | IO F{io['fire']}L{io['led']}R{io['laser']}"
            return True
        except Exception as e:
            self._last_error = str(e)
            return False

    def _send_io_udp(self, fire: int = 0) -> bool:
        """Send IO tokens to ESP32 via WiFi UDP (mode 2)."""
        io = self._build_io_tokens(fire)
        ok = self._send_udp_payload(
            io,
            label=f"UDP IO F{io['fire']}L{io['led']}R{io['laser']}S{io['safety']}M{io['mode']}",
        )
        if ok:
            self._last_cmd += f" | UDP IO F{io['fire']}L{io['led']}R{io['laser']}"
        return ok


"""ESP32 UDP link and command protocol helper.

This module provides a lightweight UDP link with:
- explicit message format (JSON + CRC32)
- ack/timeout retry handling
- heartbeat and link health tracking
- non-blocking background IO
"""

from __future__ import annotations

import json
import queue
import socket
import threading
import time
import zlib
from dataclasses import dataclass
from typing import Any, Callable, Dict, Optional


@dataclass
class LinkStatus:
    connected: bool
    last_rx_s: float
    last_tx_s: float
    last_ack_s: float
    rtt_ms: float
    last_error: Optional[str]
    pending: int


class Esp32Link:
    """UDP link manager for PC <-> ESP32 control."""

    def __init__(
        self,
        *,
        ack_timeout_s: float = 0.15,
        max_retries: int = 3,
        heartbeat_interval_s: float = 0.25,
        link_timeout_s: float = 1.0,
    ) -> None:
        self._ack_timeout_s = float(ack_timeout_s)
        self._max_retries = int(max_retries)
        self._heartbeat_interval_s = float(heartbeat_interval_s)
        self._link_timeout_s = float(link_timeout_s)

        self._sock: Optional[socket.socket] = None
        self._thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()
        self._send_queue: "queue.Queue[dict]" = queue.Queue()
        self._event_queue: "queue.Queue[dict]" = queue.Queue()

        self._target_addr: Optional[tuple[str, int]] = None
        self._seq = 1
        self._pending: Dict[int, dict] = {}
        self._last_state: Dict[str, Any] = {}
        self._caps: Dict[str, Any] = {}

        self._last_rx_s = 0.0
        self._last_tx_s = 0.0
        self._last_ack_s = 0.0
        self._last_error: Optional[str] = None
        self._rtt_ms = 0.0
        self._connected = False
        self._last_hb_s = 0.0

    # -----------------------------
    # Public API
    # -----------------------------
    def connect(self, host: str, port: int, *, local_port: int = 0) -> None:
        self.disconnect()
        self._stop_event.clear()
        self._target_addr = (str(host), int(port))
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.setblocking(False)
        self._sock.bind(("0.0.0.0", int(local_port)))
        self._thread = threading.Thread(target=self._io_loop, daemon=True, name="Esp32Link")
        self._thread.start()
        self._queue_event({"type": "link", "status": "connecting"})
        self._send_hello()

    def disconnect(self) -> None:
        self._stop_event.set()
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=0.25)
        self._thread = None
        if self._sock is not None:
            try:
                self._sock.close()
            except Exception:
                pass
        self._sock = None
        self._pending.clear()
        self._connected = False
        self._queue_event({"type": "link", "status": "disconnected"})

    def send_command(self, payload: Dict[str, Any]) -> int:
        seq = self._next_seq()
        msg = {"v": 1, "t": "cmd", "seq": seq, "ts": self._now_ms(), "p": payload}
        self._enqueue(msg, expect_ack=True)
        return seq

    def send_action(self, action: str, payload: Optional[Dict[str, Any]] = None) -> int:
        data = {"action": str(action)}
        if payload:
            data.update(payload)
        return self.send_command(data)

    def get_status(self) -> LinkStatus:
        return LinkStatus(
            connected=bool(self._connected),
            last_rx_s=float(self._last_rx_s),
            last_tx_s=float(self._last_tx_s),
            last_ack_s=float(self._last_ack_s),
            rtt_ms=float(self._rtt_ms),
            last_error=self._last_error,
            pending=len(self._pending),
        )

    def get_state(self) -> Dict[str, Any]:
        return dict(self._last_state)

    def get_caps(self) -> Dict[str, Any]:
        return dict(self._caps)

    def drain_events(self, *, max_items: int = 50) -> list[dict]:
        items = []
        for _ in range(max_items):
            try:
                items.append(self._event_queue.get_nowait())
            except queue.Empty:
                break
        return items

    # -----------------------------
    # Internal helpers
    # -----------------------------
    def _next_seq(self) -> int:
        self._seq = (self._seq + 1) & 0x7FFFFFFF
        if self._seq == 0:
            self._seq = 1
        return self._seq

    @staticmethod
    def _now_ms() -> int:
        return int(time.time() * 1000.0)

    def _queue_event(self, evt: dict) -> None:
        try:
            self._event_queue.put_nowait(evt)
        except Exception:
            pass

    def _enqueue(self, msg: dict, *, expect_ack: bool) -> None:
        if expect_ack:
            self._pending[int(msg["seq"])] = {
                "msg": msg,
                "sent": 0.0,
                "tries": 0,
                "expect_ack": True,
            }
        self._send_queue.put(msg)

    def _send_hello(self) -> None:
        msg = {
            "v": 1,
            "t": "hello",
            "seq": self._next_seq(),
            "ts": self._now_ms(),
            "p": {"role": "pc", "want": ["state", "caps", "ack"]},
        }
        self._enqueue(msg, expect_ack=True)

    def _send_heartbeat(self) -> None:
        msg = {
            "v": 1,
            "t": "hb",
            "seq": self._next_seq(),
            "ts": self._now_ms(),
            "p": {},
        }
        self._enqueue(msg, expect_ack=False)

    def _io_loop(self) -> None:
        while not self._stop_event.is_set():
            self._recv_once()
            self._send_once()
            self._retry_pending()
            self._update_link_state()
            time.sleep(0.005)

    def _recv_once(self) -> None:
        if not self._sock:
            return
        try:
            while True:
                data, _addr = self._sock.recvfrom(4096)
                self._last_rx_s = time.time()
                msg = self._decode_message(data)
                if not msg:
                    continue
                mtype = msg.get("t")
                if mtype == "ack":
                    self._handle_ack(msg)
                elif mtype == "state":
                    self._last_state = msg.get("p", {}) or {}
                    self._connected = True
                    self._queue_event({"type": "state", "data": self._last_state})
                elif mtype == "cap":
                    self._caps = msg.get("p", {}) or {}
                    self._connected = True
                    self._queue_event({"type": "caps", "data": self._caps})
                else:
                    self._queue_event({"type": "msg", "data": msg})
        except BlockingIOError:
            return
        except Exception as exc:
            self._last_error = f"RX error: {exc}"
            self._queue_event({"type": "error", "error": self._last_error})

    def _send_once(self) -> None:
        if not self._sock or not self._target_addr:
            return
        try:
            msg = self._send_queue.get_nowait()
        except queue.Empty:
            return
        payload = self._encode_message(msg)
        try:
            self._sock.sendto(payload, self._target_addr)
            self._last_tx_s = time.time()
            if int(msg.get("seq", 0)) in self._pending:
                self._pending[int(msg["seq"])]["sent"] = self._last_tx_s
                self._pending[int(msg["seq"])]["tries"] += 1
        except Exception as exc:
            self._last_error = f"TX error: {exc}"
            self._queue_event({"type": "error", "error": self._last_error})

    def _retry_pending(self) -> None:
        if not self._sock or not self._target_addr:
            return
        now = time.time()
        for seq, rec in list(self._pending.items()):
            sent = float(rec.get("sent", 0.0) or 0.0)
            tries = int(rec.get("tries", 0) or 0)
            if sent <= 0:
                continue
            if (now - sent) < self._ack_timeout_s:
                continue
            if tries >= self._max_retries:
                self._pending.pop(seq, None)
                self._queue_event({"type": "warn", "msg": f"ACK timeout seq={seq}"})
                continue
            self._send_queue.put(rec["msg"])

    def _update_link_state(self) -> None:
        now = time.time()
        if self._target_addr and (now - self._last_hb_s) >= self._heartbeat_interval_s:
            self._last_hb_s = now
            self._send_heartbeat()

        if self._connected and self._last_rx_s > 0:
            if (now - self._last_rx_s) > self._link_timeout_s:
                self._connected = False
                self._queue_event({"type": "link", "status": "lost"})

    def _handle_ack(self, msg: dict) -> None:
        seq = int(msg.get("seq", 0) or 0)
        if seq in self._pending:
            rec = self._pending.pop(seq, None)
            if rec and rec.get("sent"):
                self._rtt_ms = max(0.0, (time.time() - float(rec["sent"])) * 1000.0)
            self._last_ack_s = time.time()
        if "state" in msg:
            self._last_state = msg.get("state", {}) or {}
            self._queue_event({"type": "state", "data": self._last_state})
        if msg.get("ok") is False:
            self._queue_event({"type": "warn", "msg": msg.get("err", "ESP32 NACK")})

    def _encode_message(self, msg: dict) -> bytes:
        payload = dict(msg)
        payload.pop("crc", None)
        raw = json.dumps(payload, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
        crc = zlib.crc32(raw) & 0xFFFFFFFF
        payload["crc"] = f"{crc:08x}"
        return json.dumps(payload, separators=(",", ":"), ensure_ascii=True).encode("utf-8")

    def _decode_message(self, data: bytes) -> Optional[dict]:
        try:
            msg = json.loads(data.decode("utf-8"))
        except Exception:
            return None
        if not isinstance(msg, dict):
            return None
        crc = msg.get("crc")
        if not crc:
            return None
        payload = dict(msg)
        payload.pop("crc", None)
        raw = json.dumps(payload, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
        calc = f"{(zlib.crc32(raw) & 0xFFFFFFFF):08x}"
        if str(crc).lower() != calc:
            return None
        return msg

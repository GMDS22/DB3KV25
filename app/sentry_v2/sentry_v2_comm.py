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
    3  ESP32 WiFi + Debug Board on ESP32 → full ASCII protocol over UDP
                                           (no USB — fully wireless)

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
from typing import Optional

import serial as _serial
import serial.tools.list_ports as _list_ports


class SentryV2Comm:
    """Self-contained ESP32 + Debug Board communication for Smart Sentry v2."""

    PAN_OUTPUT_MIN = 0.0
    PAN_OUTPUT_MAX = 220.0
    TILT_OUTPUT_MIN = 0.0
    TILT_OUTPUT_MAX = 130.0

    # --- Connection mode constants ---
    MODE_ESP32_USB = 0           # Single USB — full ASCII to ESP32
    MODE_DUAL_USB = 1            # Debug Board USB (pan/tilt) + ESP32 USB (IO)
    MODE_WIFI_DEBUG_USB = 2      # Debug Board USB (pan/tilt) + ESP32 WiFi (IO)
    MODE_WIFI_FULL = 3           # Everything over WiFi (debug board on ESP32)

    MODE_LABELS = [
        "ESP32 USB",
        "ESP32 USB + Debug Board USB",
        "ESP32 WiFi + Debug Board USB",
        "ESP32 WiFi (wireless, no USB)",
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
        self._bus_checksum_mode: str = "sub"  # "sub" or "xor"

        # Diagnostics
        self._last_cmd: str = ""
        self._last_error: str = ""
        self._udp_seq: int = 0

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
                self._connect_details["Debug Board"] = (ok_bus, debug_port if ok_bus else bus_err)

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
                self._connect_details["Debug Board"] = (ok_bus, debug_port if ok_bus else bus_err)

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

    def disconnect(self) -> None:
        """Close all open connections."""
        with self._lock:
            for s in (self._ser, self._bus_ser):
                if s is not None:
                    try:
                        s.close()
                    except Exception:
                        pass
            self._ser = None
            self._bus_ser = None
            if self._sock is not None:
                try:
                    self._sock.close()
                except Exception:
                    pass
                self._sock = None
                self._udp_target = None

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
            return self._send_ascii(pan_out, tilt_out, fire, via_serial=False)
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
        p = int(max(0, min(220, round(pan))))
        t = int(max(0, min(130, round(tilt))))
        f = int(bool(fire))
        led = 1 if self.led_on else 0
        laser = 1 if self.laser_on else 0
        safety = 0 if self.safety_armed else 1
        mode = 1 if self.trigger_mode_bb else 0
        return f"P{p}T{t}F{f}L{led}R{laser}G0S{safety}M{mode}\n"

    def _send_ascii(self, pan: float, tilt: float, fire: int, *, via_serial: bool) -> bool:
        cmd = self._build_ascii(pan, tilt, fire)
        with self._lock:
            try:
                if via_serial:
                    if self._ser and self._ser.is_open:
                        self._ser.write(cmd.encode("utf-8"))
                        self._last_cmd = cmd.rstrip()
                        return True
                else:
                    if self._sock and self._udp_target:
                        self._sock.sendto(cmd.encode("utf-8"), self._udp_target)
                        self._last_cmd = cmd.rstrip()
                        return True
                return False
            except Exception as e:
                self._last_error = str(e)
                return False

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
            try:
                if self._bus_ser is None or not self._bus_ser.is_open:
                    return False
                move_time = int(self.bus_servo_time_ms if move_time_ms is None else move_time_ms)
                move_time = max(0, min(1000, move_time))
                pan_pkt = self._build_servo_packet(
                    self.pan_servo_id,
                    self._deg_to_ticks(pan),
                    move_time,
                )
                tilt_pkt = self._build_servo_packet(
                    self.tilt_servo_id,
                    self._deg_to_ticks(tilt),
                    move_time,
                )
                self._bus_ser.write(pan_pkt)
                self._bus_ser.write(tilt_pkt)
                self._last_cmd = f"BUS P{pan:.0f} T{tilt:.0f} @{move_time}ms"
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
            try:
                if self._ser is None or not self._ser.is_open:
                    return False
                io = self._build_io_tokens(fire)
                self._ser.write(f"S{io['safety']}\n".encode("utf-8"))
                self._ser.write(f"M{io['mode']}\n".encode("utf-8"))
                self._ser.write(
                    f"F{io['fire']}L{io['led']}R{io['laser']}G0\n".encode("utf-8")
                )
                self._last_cmd += f" | IO F{io['fire']}L{io['led']}R{io['laser']}"
                return True
            except Exception as e:
                self._last_error = str(e)
                return False

    def _send_io_udp(self, fire: int = 0) -> bool:
        """Send IO tokens to ESP32 via WiFi UDP (mode 2)."""
        with self._lock:
            try:
                if self._sock is None or self._udp_target is None:
                    return False
                io = self._build_io_tokens(fire)
                self._udp_seq += 1
                msg = {
                    "v": 1, "t": "cmd",
                    "seq": self._udp_seq,
                    "ts": int(time.time() * 1000),
                    "p": io,
                }
                raw = json.dumps(msg, separators=(",", ":")).encode("utf-8")
                crc = zlib.crc32(raw) & 0xFFFFFFFF
                msg["crc"] = f"{crc:08x}"
                data = json.dumps(msg, separators=(",", ":")).encode("utf-8")
                self._sock.sendto(data, self._udp_target)
                self._last_cmd += f" | UDP IO F{io['fire']}L{io['led']}R{io['laser']}"
                return True
            except Exception as e:
                self._last_error = str(e)
                return False


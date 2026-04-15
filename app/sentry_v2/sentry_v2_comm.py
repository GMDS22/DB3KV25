"""
SMART SENTRY V3 — Standalone Communication

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

ESP32 ASCII protocol: ``P{pan}T{tilt}F{fire}L{led}R{laser}G{acc}A{spare}S{safety}M{mode}\n``
Bus servo protocol:    Yahboom-style register write (0xFF 0xFF ID LEN INST REG …)
"""

from __future__ import annotations

import json
import os
import re
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
    """Self-contained ESP32 + Debug Board communication for SMART SENTRY V3."""

    PAN_OUTPUT_MIN = SENTRY_PAN_MIN
    PAN_OUTPUT_MAX = SENTRY_PAN_MAX
    TILT_OUTPUT_MIN = SENTRY_TILT_MIN
    TILT_OUTPUT_MAX = SENTRY_TILT_MAX

    # --- Connection mode constants ---
    MODE_ESP32_USB = 0           # Single USB — full ASCII to ESP32
    MODE_DUAL_USB = 1            # Debug Board USB (pan/tilt) + ESP32 USB (IO)
    MODE_WIFI_DEBUG_USB = 2      # Debug Board USB (pan/tilt) + ESP32 WiFi (IO)
    MODE_WIFI_FULL = 3           # Everything over WiFi (debug board on ESP32)
    MODE_DUAL_ESP32_WIFI = 4     # Dual ESP32 WiFi (servos + IO separate)

    MODE_LABELS = [
        "ESP32 USB",
        "ESP32 USB + Debug Board USB",
        "ESP32 WiFi + Debug Board USB",
        "ESP32 WiFi + Debug Board on ESP32 UART",
        "Dual ESP32 WiFi",
    ]

    @staticmethod
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

    def __init__(self) -> None:
        # Primary ESP32 serial (modes 0, 1)
        self._ser: Optional[_serial.Serial] = None
        # Debug board serial (modes 1, 2)
        self._bus_ser: Optional[_serial.Serial] = None
        # Primary UDP socket (modes 2, 3, 4) - IO/accessories
        self._sock: Optional[socket.socket] = None
        self._udp_target: Optional[tuple] = None
        # Secondary UDP socket (mode 4) - servos
        self._servo_sock: Optional[socket.socket] = None
        self._servo_udp_target: Optional[tuple] = None

        self._mode: int = self.MODE_ESP32_USB
        self._lock = threading.Lock()
        self._bus_io_lock = threading.Lock()

        # Accessory state (tracked locally)
        self.led_pwm: int = 0
        self.laser_on: bool = False
        self.acc_on: bool = False          # GPIO 25 accessory relay
        self.spare_on: bool = False        # GPIO 26 spare relay
        self.safety_armed: bool = False   # False=LOCKED (S1), True=ARMED (S0)
        self.trigger_mode_bb: bool = False  # False=Water M0, True=BB M1
        self.trigger_servo_rest_deg: int = 0
        self.trigger_servo_fire_deg: int = 45
        self.trigger_servo_speed_dps: int = 360
        self.rest_pan: float = 90.0
        self.rest_tilt: float = 55.0
        self.pir_event_blink_enabled: bool = False

        # Direction inversion
        self.invert_pan: bool = False
        self.invert_tilt: bool = False

        # Bus servo config
        self.pan_servo_id: int = 1
        self.tilt_servo_id: int = 2
        self.bus_servo_time_ms: int = 20
        self._bus_checksum_mode: str = "sub"  # "auto", "sub", or "xor"
        self._bus_servo_ping_ok: bool = False

        # Diagnostics
        self._last_cmd: str = ""
        self._last_error: str = ""
        self._udp_seq: int = 0
        self._receiver_stop = threading.Event()
        self._receiver_thread: Optional[threading.Thread] = None
        self._serial_rx_buffer: str = ""
        
        # PIR event callback (called when sensor data is received)
        self._on_pir_event: Optional[Callable[[int, float], None]] = None
        self._on_transport_log: Optional[Callable[[str], None]] = None
        self._last_udp_state_trace: str = ""
        self._last_udp_state_trace_s: float = 0.0

        # Bus-servo feedback telemetry (modes 1, 2)
        self._servo_feedback: Dict[str, Any] = {
            "active": False,
            "source": "inactive",
            "pan_deg": None,
            "tilt_deg": None,
            "pan_ticks": None,
            "tilt_ticks": None,
            "pan_load_raw": None,
            "tilt_load_raw": None,
            "pan_voltage_raw": None,
            "tilt_voltage_raw": None,
            "pan_voltage_v": None,
            "tilt_voltage_v": None,
            "last_update": 0.0,
            "diag_last_update": 0.0,
            "last_error": "",
        }
        self._feedback_poll_interval_s: float = 0.75
        self._feedback_waiting_poll_interval_s: float = 1.1
        self._feedback_post_move_delay_s: float = 0.35
        self._feedback_diag_poll_interval_s: float = 2.5
        self._feedback_next_poll_time: float = 0.0
        self._feedback_diag_next_poll_time: float = 0.0
        self._feedback_last_motion_time: float = 0.0
        self._feedback_waiting_miss_count: int = 0
        self._feedback_pause_until_s: float = 0.0
        self._last_bus_pan_ticks: Optional[int] = None
        self._last_bus_tilt_ticks: Optional[int] = None

        self._io_runtime: Dict[str, Any] = {
            "active": False,
            "source": "inactive",
            "safety": None,
            "mode": None,
            "switch_in": None,
            "hw_arm_enabled": None,
            "control_source_mode": "",
            "control_source_active": "",
            "rc_link_active": None,
            "rc_override_active": None,
            "rc_failsafe_active": None,
            "rc_frame_age_ms": None,
            "rc_channels": {},
            "current_fault": None,
            "pir_enabled": None,
            "pan_mA": None,
            "pan_mA_valid": None,
            "tilt_mA": None,
            "tilt_mA_valid": None,
            "total_mA": None,
            "total_mA_valid": None,
            "last_update": 0.0,
            "last_error": "",
        }
        self._bridge_caps: Dict[str, Any] = {
            "active": False,
            "source": "inactive",
            "role": "",
            "rc_input_supported": None,
            "rc_input_planned": "",
            "rc_mode_supported": None,
            "rc_mode_default": "",
            "rc_receiver_model": "",
            "rc_source_switch_channel": None,
            "switch_supported": None,
            "switch_role": "",
            "switch_active_low": None,
            "switch_pullup_enabled": None,
            "sound_supported": None,
            "speaker_supported": None,
            "current_pan_supported": None,
            "current_tilt_supported": None,
            "current_total_supported": None,
            "led_relay_assigned": None,
            "laser_relay_assigned": None,
            "trigger_servo_assigned": None,
            "buzzer_volume_assigned": None,
            "speaker_volume_assigned": None,
            "header_reference_locked": None,
            "pins": {},
            "raw": {},
            "last_update": 0.0,
            "last_error": "",
        }

    def _report_runtime_warning(self, context: str, exc: Exception) -> None:
        self._last_error = f"{context}: {exc}"
        print(f"[SENTRY_V2_COMM] {self._last_error}", flush=True)

    def _emit_transport_log(self, message: str) -> None:
        callback = self._on_transport_log
        if callback is None:
            return
        try:
            text = str(message or "").strip()
            if not text:
                return
            callback(text)
        except Exception as exc:
            self._report_runtime_warning("Transport log callback failed", exc)

    @staticmethod
    def _payload_flag(value: Any) -> Optional[bool]:
        if value is None:
            return None
        if isinstance(value, bool):
            return bool(value)
        try:
            return bool(int(value))
        except Exception:
            text = str(value or "").strip().lower()
            if text in {"true", "on", "yes", "armed", "active"}:
                return True
            if text in {"false", "off", "no", "locked", "inactive"}:
                return False
        return None

    def _summarize_runtime_payload_for_log(self, payload: Dict[str, Any]) -> str:
        if not isinstance(payload, dict):
            return ""
        parts = []
        safety_raw = payload.get("safety")
        try:
            safety = int(safety_raw) if safety_raw is not None else None
        except Exception:
            safety = None
        if safety is not None:
            parts.append(f"safety={'ARMED' if safety == 0 else 'LOCKED'}")

        mode_raw = payload.get("mode")
        try:
            mode = int(mode_raw) if mode_raw is not None else None
        except Exception:
            mode = None
        if mode is not None:
            parts.append(f"mode={'PROJECTILE' if mode == 1 else 'WATER'}")

        pir_enabled = self._payload_flag(payload.get("pir_enabled"))
        if pir_enabled is not None:
            parts.append(f"pir={'ON' if pir_enabled else 'OFF'}")

        current_fault = self._payload_flag(payload.get("current_fault"))
        if current_fault is not None:
            parts.append(f"fault={'TRIP' if current_fault else 'CLEAR'}")

        control_source = str(payload.get("control_source_active") or payload.get("control_source_mode") or "").strip()
        if control_source:
            parts.append(f"ctrl={control_source}")
        return " ".join(parts)

    def _summarize_caps_payload_for_log(self, payload: Dict[str, Any]) -> str:
        if not isinstance(payload, dict):
            return ""
        parts = []
        fw = str(payload.get("fw") or "").strip()
        role = str(payload.get("role") or "").strip()
        pir_support = self._payload_flag(payload.get("pir_support"))
        pir_count = payload.get("pir_count")
        if fw:
            parts.append(f"fw={fw}")
        if role:
            parts.append(f"role={role}")
        if pir_support is not None:
            if pir_support and pir_count is not None:
                parts.append(f"pir={int(pir_count)}")
            else:
                parts.append(f"pir={'ON' if pir_support else 'OFF'}")
        return " ".join(parts)

    def _emit_udp_state_trace(self, payload: Dict[str, Any], *, timestamp_ms: Any = None) -> None:
        summary = self._summarize_runtime_payload_for_log(payload)
        if not summary:
            return
        update_time = self._runtime_update_time_from_timestamp(timestamp_ms)
        if summary == self._last_udp_state_trace and (update_time - self._last_udp_state_trace_s) < 2.0:
            return
        self._last_udp_state_trace = summary
        self._last_udp_state_trace_s = update_time
        self._emit_transport_log(f"ESP32 UDP STATE {summary}")

    def _reset_servo_feedback_state(self, *, active: bool, source: str, last_error: str = "") -> None:
        with self._lock:
            self._servo_feedback = {
                "active": bool(active),
                "source": str(source or "inactive"),
                "pan_deg": None,
                "tilt_deg": None,
                "pan_ticks": None,
                "tilt_ticks": None,
                "pan_load_raw": None,
                "tilt_load_raw": None,
                "pan_voltage_raw": None,
                "tilt_voltage_raw": None,
                "pan_voltage_v": None,
                "tilt_voltage_v": None,
                "last_update": 0.0,
                "diag_last_update": 0.0,
                "last_error": str(last_error or ""),
            }
            self._feedback_next_poll_time = 0.0
            self._feedback_diag_next_poll_time = 0.0
            self._feedback_last_motion_time = 0.0
            self._feedback_waiting_miss_count = 0
            self._feedback_pause_until_s = 0.0

    def _reset_bus_motion_cache(self) -> None:
        with self._lock:
            self._last_bus_pan_ticks = None
            self._last_bus_tilt_ticks = None

    def get_servo_feedback_snapshot(self) -> Dict[str, Any]:
        with self._lock:
            snapshot = dict(self._servo_feedback)
        last_update = float(snapshot.get("last_update") or 0.0)
        snapshot["age_s"] = max(0.0, time.time() - last_update) if last_update > 0.0 else None
        diag_last_update = float(snapshot.get("diag_last_update") or 0.0)
        snapshot["diag_age_s"] = max(0.0, time.time() - diag_last_update) if diag_last_update > 0.0 else None
        return snapshot

    def _reset_io_runtime_state(self, *, active: bool, source: str, last_error: str = "") -> None:
        with self._lock:
            self._io_runtime = {
                "active": bool(active),
                "source": str(source or "inactive"),
                "safety": None,
                "mode": None,
                "switch_in": None,
                "hw_arm_enabled": None,
                "control_source_mode": "",
                "control_source_active": "",
                "rc_link_active": None,
                "rc_override_active": None,
                "rc_failsafe_active": None,
                "rc_frame_age_ms": None,
                "rc_channels": {},
                "current_fault": None,
                "pir_enabled": None,
                "pan_mA": None,
                "pan_mA_valid": None,
                "tilt_mA": None,
                "tilt_mA_valid": None,
                "total_mA": None,
                "total_mA_valid": None,
                "last_update": 0.0,
                "last_error": str(last_error or ""),
            }

    def _reset_bridge_caps_state(self, *, active: bool, source: str, last_error: str = "") -> None:
        with self._lock:
            self._bridge_caps = {
                "active": bool(active),
                "source": str(source or "inactive"),
                "role": "",
                "rc_input_supported": None,
                "rc_input_planned": "",
                "rc_mode_supported": None,
                "rc_mode_default": "",
                "rc_receiver_model": "",
                "rc_source_switch_channel": None,
                "switch_supported": None,
                "switch_role": "",
                "switch_active_low": None,
                "switch_pullup_enabled": None,
                "sound_supported": None,
                "speaker_supported": None,
                "current_pan_supported": None,
                "current_tilt_supported": None,
                "current_total_supported": None,
                "led_relay_assigned": None,
                "laser_relay_assigned": None,
                "trigger_servo_assigned": None,
                "buzzer_volume_assigned": None,
                "speaker_volume_assigned": None,
                "header_reference_locked": None,
                "pins": {},
                "raw": {},
                "last_update": 0.0,
                "last_error": str(last_error or ""),
            }

    def get_io_runtime_snapshot(self) -> Dict[str, Any]:
        with self._lock:
            snapshot = dict(self._io_runtime)
            rc_channels = snapshot.get("rc_channels") or {}
            snapshot["rc_channels"] = dict(rc_channels) if isinstance(rc_channels, dict) else {}
        last_update = float(snapshot.get("last_update") or 0.0)
        snapshot["age_s"] = max(0.0, time.time() - last_update) if last_update > 0.0 else None
        return snapshot

    def get_bridge_caps_snapshot(self) -> Dict[str, Any]:
        with self._lock:
            snapshot = dict(self._bridge_caps)
            pins = snapshot.get("pins") or {}
            raw = snapshot.get("raw") or {}
            snapshot["pins"] = dict(pins) if isinstance(pins, dict) else {}
            snapshot["raw"] = dict(raw) if isinstance(raw, dict) else {}
        last_update = float(snapshot.get("last_update") or 0.0)
        snapshot["age_s"] = max(0.0, time.time() - last_update) if last_update > 0.0 else None
        return snapshot

    @staticmethod
    def _runtime_update_time_from_timestamp(timestamp_ms: Any = None) -> float:
        """Convert remote timestamps to a local freshness clock.

        Bridge packets currently use ESP32 millis-since-boot in `ts`, while the app
        freshness checks compare `last_update` against `time.time()`. Treat only
        epoch-like millisecond timestamps as absolute wall clock values; otherwise
        use local receipt time so fresh bridge replies are not marked stale.
        """
        now = time.time()
        if timestamp_ms is None:
            return now
        try:
            ts_s = float(timestamp_ms) / 1000.0
        except Exception:
            return now
        if ts_s >= 946684800.0:
            return ts_s
        return now

    def _apply_io_runtime_state(self, payload: Dict[str, Any], *, source: str, timestamp_ms: Any = None) -> None:
        if not isinstance(payload, dict):
            return
        update_time = self._runtime_update_time_from_timestamp(timestamp_ms)

        def _maybe_int(value: Any) -> Optional[int]:
            try:
                return int(value)
            except Exception:
                return None

        def _maybe_bool(value: Any) -> Optional[bool]:
            if value is None:
                return None
            if isinstance(value, bool):
                return value
            if isinstance(value, (int, float)):
                return bool(value)
            text = str(value).strip().lower()
            if text in {"1", "true", "yes", "on", "enabled", "valid"}:
                return True
            if text in {"0", "false", "no", "off", "disabled", "invalid"}:
                return False
            return None

        with self._lock:
            runtime = self._io_runtime
            runtime["active"] = True
            runtime["source"] = str(source or "esp32")
            safety = _maybe_int(payload.get("safety"))
            if safety is not None:
                runtime["safety"] = safety
            mode = _maybe_int(payload.get("mode"))
            if mode is not None:
                runtime["mode"] = mode
            switch_in = _maybe_int(payload.get("switch_in"))
            if switch_in is not None:
                runtime["switch_in"] = switch_in
            hw_arm_enabled = _maybe_int(payload.get("hw_arm_enabled"))
            if hw_arm_enabled is not None:
                runtime["hw_arm_enabled"] = hw_arm_enabled
            if "control_source_mode" in payload:
                runtime["control_source_mode"] = str(payload.get("control_source_mode") or "")
            if "control_source_active" in payload:
                runtime["control_source_active"] = str(payload.get("control_source_active") or "")
            for key in ("rc_link_active", "rc_override_active", "rc_failsafe_active"):
                if key in payload:
                    value = payload.get(key)
                    runtime[key] = None if value is None else bool(value)
            rc_frame_age_ms = _maybe_int(payload.get("rc_frame_age_ms"))
            if rc_frame_age_ms is not None:
                runtime["rc_frame_age_ms"] = rc_frame_age_ms
            rc_payload = payload.get("rc")
            if isinstance(rc_payload, dict):
                rc_channels: Dict[str, int] = {}
                for channel_index in range(1, 7):
                    key = f"ch{channel_index}_us"
                    parsed = _maybe_int(rc_payload.get(key))
                    if parsed is not None:
                        rc_channels[key] = parsed
                if rc_channels:
                    runtime["rc_channels"] = rc_channels
                link_active = rc_payload.get("link_active")
                if link_active is not None:
                    runtime["rc_link_active"] = bool(link_active)
                override_active = rc_payload.get("override_active")
                if override_active is not None:
                    runtime["rc_override_active"] = bool(override_active)
                failsafe_active = rc_payload.get("failsafe_active")
                if failsafe_active is not None:
                    runtime["rc_failsafe_active"] = bool(failsafe_active)
                frame_age = _maybe_int(rc_payload.get("frame_age_ms"))
                if frame_age is not None:
                    runtime["rc_frame_age_ms"] = frame_age
            current_fault = payload.get("current_fault")
            if current_fault is not None:
                runtime["current_fault"] = bool(current_fault)
            pir_enabled = _maybe_int(payload.get("pir_enabled"))
            if pir_enabled is not None:
                runtime["pir_enabled"] = pir_enabled
            for key in ("pan_mA", "tilt_mA", "total_mA"):
                parsed = _maybe_int(payload.get(key))
                if parsed is not None:
                    runtime[key] = parsed
            for key in ("pan_mA_valid", "tilt_mA_valid", "total_mA_valid"):
                if key in payload:
                    runtime[key] = _maybe_bool(payload.get(key))
            runtime["last_update"] = update_time
            runtime["last_error"] = ""

    def _apply_bridge_caps(self, payload: Dict[str, Any], *, source: str, timestamp_ms: Any = None) -> None:
        if not isinstance(payload, dict):
            return
        update_time = self._runtime_update_time_from_timestamp(timestamp_ms)

        with self._lock:
            caps = self._bridge_caps
            caps["active"] = True
            caps["source"] = str(source or "esp32-cap")
            caps["role"] = str(payload.get("role") or caps.get("role") or "")
            if "rc_input_supported" in payload:
                value = payload.get("rc_input_supported")
                caps["rc_input_supported"] = None if value is None else bool(value)
            if "rc_input_planned" in payload:
                caps["rc_input_planned"] = str(payload.get("rc_input_planned") or "")
            if "rc_mode_supported" in payload:
                value = payload.get("rc_mode_supported")
                caps["rc_mode_supported"] = None if value is None else bool(value)
            if "rc_mode_default" in payload:
                caps["rc_mode_default"] = str(payload.get("rc_mode_default") or "")
            if "rc_receiver_model" in payload:
                caps["rc_receiver_model"] = str(payload.get("rc_receiver_model") or "")
            if "rc_source_switch_channel" in payload:
                try:
                    caps["rc_source_switch_channel"] = int(payload.get("rc_source_switch_channel"))
                except Exception:
                    caps["rc_source_switch_channel"] = None
            for key in (
                "switch_supported",
                "switch_active_low",
                "switch_pullup_enabled",
                "sound_supported",
                "speaker_supported",
                "current_pan_supported",
                "current_tilt_supported",
                "current_total_supported",
                "led_relay_assigned",
                "laser_relay_assigned",
                "trigger_servo_assigned",
                "buzzer_volume_assigned",
                "speaker_volume_assigned",
                "header_reference_locked",
            ):
                if key in payload:
                    value = payload.get(key)
                    caps[key] = None if value is None else bool(value)
            if "switch_role" in payload:
                caps["switch_role"] = str(payload.get("switch_role") or "")
            pins = payload.get("pins")
            if isinstance(pins, dict):
                caps["pins"] = dict(pins)
            caps["raw"] = dict(payload)
            caps["last_update"] = update_time
            caps["last_error"] = ""

    def _has_fresh_servo_feedback_locked(self, now: Optional[float] = None, *, max_age_s: float = 1.5) -> bool:
        feedback = self._servo_feedback
        if str(feedback.get("source") or "") != "debug-board":
            return False
        last_update = float(feedback.get("last_update") or 0.0)
        if last_update <= 0.0:
            return False
        current_time = time.time() if now is None else float(now)
        return (current_time - last_update) <= float(max_age_s)

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
        servo_udp_host: str = "192.168.4.2",
        servo_udp_port: int = 9001,
    ) -> bool:
        """Open connections for the specified mode. Returns True on success.

        Sets ``_connect_details`` with per-link status for the UI.
        """
        self.disconnect()
        self._mode = int(mode)
        self._connect_details = {}          # per-link status dict
        self._last_error = ""
        self._reset_servo_feedback_state(
            active=self._mode in (self.MODE_DUAL_USB, self.MODE_WIFI_DEBUG_USB),
            source="waiting" if self._mode in (self.MODE_DUAL_USB, self.MODE_WIFI_DEBUG_USB) else "inactive",
        )
        self._reset_io_runtime_state(
            active=self._mode in (self.MODE_WIFI_DEBUG_USB, self.MODE_WIFI_FULL, self.MODE_DUAL_ESP32_WIFI),
            source="waiting" if self._mode in (self.MODE_WIFI_DEBUG_USB, self.MODE_WIFI_FULL, self.MODE_DUAL_ESP32_WIFI) else "inactive",
        )
        self._reset_bridge_caps_state(
            active=self._mode in (self.MODE_WIFI_DEBUG_USB, self.MODE_WIFI_FULL, self.MODE_DUAL_ESP32_WIFI),
            source="waiting" if self._mode in (self.MODE_WIFI_DEBUG_USB, self.MODE_WIFI_FULL, self.MODE_DUAL_ESP32_WIFI) else "inactive",
        )
        try:
            if self._mode == self.MODE_ESP32_USB:
                ok = self._open_serial(esp32_port, esp32_baud, primary=True)
                self._connect_details["ESP32 USB"] = (ok, esp32_port if ok else self._last_error)
                if ok:
                    self._start_receiver()
                return ok

            elif self._mode == self.MODE_DUAL_USB:
                ok_bus = self._open_serial(debug_port, debug_baud, primary=False)
                bus_err = self._last_error
                if ok_bus:
                    checksum_mode = self._probe_bus_servo_checksum(self._bus_ser)
                    if checksum_mode is not None:
                        self._connect_details["Debug Board"] = (True, f"{debug_port} ({checksum_mode} checksum)")
                    else:
                        # USB port opened and the board is connected, but the quick
                        # servo ping probe is not authoritative for all board/servo
                        # combinations.  Keep the connection green and mark the probe
                        # as inconclusive rather than implying the servos are broken.
                        self._connect_details["Debug Board"] = (True, f"{debug_port} (servo probe inconclusive)")
                else:
                    self._connect_details["Debug Board"] = (False, bus_err)

                norm_debug_port = self._normalize_serial_port_name(debug_port)
                norm_esp_port = self._normalize_serial_port_name(esp32_port)
                esp_disabled = (not norm_esp_port) or (
                    norm_debug_port
                    and norm_esp_port
                    and norm_debug_port.upper() == norm_esp_port.upper()
                )

                if esp_disabled:
                    ok_esp = False
                    esp_err = "ESP32 link skipped (blank or same as Debug Board COM port)"
                    self._connect_details["ESP32 USB"] = (False, esp_err)
                else:
                    ok_esp = self._open_serial(esp32_port, esp32_baud, primary=True)
                    esp_err = self._last_error
                    self._connect_details["ESP32 USB"] = (ok_esp, esp32_port if ok_esp else esp_err)

                if not ok_bus and not ok_esp and not esp_disabled:
                    self._last_error = f"Both failed — Debug: {bus_err} | ESP32: {esp_err}"
                elif not ok_bus:
                    self._last_error = f"Debug board failed: {bus_err}"
                elif not ok_esp and not esp_disabled:
                    self._last_error = f"ESP32 failed: {esp_err}"
                if ok_esp:
                    self._start_receiver()
                return ok_bus and (ok_esp or esp_disabled)

            elif self._mode == self.MODE_WIFI_DEBUG_USB:
                ok_bus = self._open_serial(debug_port, debug_baud, primary=False)
                bus_err = self._last_error
                if ok_bus:
                    checksum_mode = self._probe_bus_servo_checksum(self._bus_ser)
                    if checksum_mode is not None:
                        self._connect_details["Debug Board"] = (True, f"{debug_port} ({checksum_mode} checksum)")
                    else:
                        # USB port opened and the board is connected, but the quick
                        # servo ping probe is not authoritative for all board/servo
                        # combinations.  Keep the connection green and mark the probe
                        # as inconclusive rather than implying the servos are broken.
                        self._connect_details["Debug Board"] = (True, f"{debug_port} (servo probe inconclusive)")
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
                    self._last_error = f"WiFi failed (Debug Board still connected): {udp_err}"
                if ok_udp:
                    self._start_receiver()
                # In WiFi+Debug mode, Debug Board is the critical movement link.
                # Allow degraded operation when WiFi is down so manual movement
                # and tracking-to-servo can still run.
                return ok_bus

            elif self._mode == self.MODE_WIFI_FULL:
                ok = self._open_udp(udp_host, udp_port)
                self._connect_details["ESP32 WiFi"] = (ok, f"{udp_host}:{udp_port}" if ok else self._last_error)
                if ok:
                    self._start_receiver()
                return ok

            elif self._mode == self.MODE_DUAL_ESP32_WIFI:
                # Primary ESP32 (IO/accessories)
                ok_primary = self._open_udp(udp_host, udp_port)
                primary_err = self._last_error
                self._connect_details["Primary ESP32 WiFi"] = (ok_primary, f"{udp_host}:{udp_port}" if ok_primary else primary_err)

                # Secondary ESP32 (servos)
                ok_servo = self._open_udp_secondary(servo_udp_host, servo_udp_port)
                servo_err = self._last_error
                self._connect_details["Servo ESP32 WiFi"] = (ok_servo, f"{servo_udp_host}:{servo_udp_port}" if ok_servo else servo_err)

                if not ok_primary and not ok_servo:
                    self._last_error = f"Both failed — Primary: {primary_err} | Servo: {servo_err}"
                elif not ok_primary:
                    self._last_error = f"Primary ESP32 failed: {primary_err}"
                elif not ok_servo:
                    self._last_error = f"Servo ESP32 failed: {servo_err}"
                if ok_primary:
                    self._start_receiver()
                return ok_primary and ok_servo

            else:
                self._last_error = f"Unknown mode: {self._mode}"
                return False
        except Exception as e:
            self._last_error = str(e)
            return False

    def _open_serial(self, port: str, baud: int, *, primary: bool) -> bool:
        try:
            normalized_port = self._normalize_serial_port_name(port)
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
                    err_text = str(e).lower()
                    if "access is denied" in err_text or "permissionerror" in err_text:
                        last_error = f"{normalized_port} is already in use by another process ({e})"
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
            # Reachability probe: on a non-blocking UDP socket, sendto raises
            # OSError (WSAENETUNREACH/ENETUNREACH) immediately if there is no
            # route to the host's network — e.g. the ESP32 WiFi AP is off and
            # the PC has no 192.168.4.x interface.  If a route exists (even if
            # the ESP32 is busy/not yet listening) the send succeeds silently,
            # which is the expected UDP fire-and-forget behaviour.
            try:
                sock.sendto(b"ping", (host, int(port)))
            except OSError as _probe_err:
                try:
                    sock.close()
                except Exception:
                    pass
                self._last_error = f"WiFi host unreachable ({host}:{port}): {_probe_err}"
                return False
            self._sock = sock
            self._udp_target = (host, int(port))
            return True
        except Exception as e:
            self._last_error = str(e)
            return False

    def _open_udp_secondary(self, host: str, port: int) -> bool:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setblocking(False)
            self._servo_sock = sock
            self._servo_udp_target = (host, int(port))
            return True
        except Exception as e:
            self._last_error = str(e)
            return False

    def refresh_primary_udp_link(self, host: str, port: int) -> bool:
        """Reopen the primary UDP transport without disturbing serial links."""
        with self._lock:
            old_sock = self._sock
            self._sock = None
            self._udp_target = None
        if old_sock is not None:
            try:
                old_sock.close()
            except Exception:
                pass
        self._reset_io_runtime_state(active=True, source="waiting")
        ok = self._open_udp(host, port)
        if ok:
            self._start_receiver()
            self._send_udp_message("hello", None, label="UDP hello")
        return ok

    @staticmethod
    def _compact_json(obj: Dict[str, Any]) -> bytes:
        return json.dumps(obj, separators=(",", ":"), ensure_ascii=True).encode("utf-8")

    def _build_udp_message(self, message_type: str, payload: Optional[Dict[str, Any]] = None) -> bytes:
        with self._lock:
            self._udp_seq = (self._udp_seq + 1) & 0x7FFFFFFF
            if self._udp_seq == 0:
                self._udp_seq = 1
            seq = self._udp_seq
        msg = {
            "v": 1,
            "t": str(message_type or "cmd"),
            "seq": seq,
            "ts": int(time.time() * 1000),
        }
        if payload is not None:
            msg["p"] = payload
        raw = self._compact_json(msg)
        msg["crc"] = f"{(zlib.crc32(raw) & 0xFFFFFFFF):08x}"
        return self._compact_json(msg)

    def _build_udp_packet(self, payload: Dict[str, Any]) -> bytes:
        return self._build_udp_message("cmd", payload)

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
            self._reset_io_runtime_state(active=True, source="waiting", last_error=self._last_error)
            return False

    def _send_udp_message(self, message_type: str, payload: Optional[Dict[str, Any]] = None, *, label: str) -> bool:
        with self._lock:
            sock = self._sock
            udp_target = self._udp_target
        try:
            if sock is None or udp_target is None:
                return False
            data = self._build_udp_message(message_type, payload)
            sock.sendto(data, udp_target)
            self._last_cmd = label
            return True
        except Exception as e:
            self._last_error = str(e)
            self._reset_io_runtime_state(active=True, source="waiting", last_error=self._last_error)
            self._reset_bridge_caps_state(active=True, source="waiting", last_error=self._last_error)
            return False

    def _send_udp_payload_secondary(self, payload: Dict[str, Any], *, label: str) -> bool:
        with self._lock:
            sock = self._servo_sock
            udp_target = self._servo_udp_target
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
        try:
            if self.is_connected():
                self.send_pir_enabled(False)
        except Exception:
            pass
        self._stop_receiver()
        with self._lock:
            ser = self._ser
            bus_ser = self._bus_ser
            sock = self._sock
            servo_sock = self._servo_sock
            self._ser = None
            self._bus_ser = None
            self._sock = None
            self._servo_sock = None
            self._udp_target = None
            self._servo_udp_target = None

        self._safe_close_serial(ser)
        self._safe_close_serial(bus_ser)
        if sock is not None:
            try:
                sock.close()
            except Exception:
                pass
        if servo_sock is not None:
            try:
                servo_sock.close()
            except Exception:
                pass
        self._reset_bus_motion_cache()
        self._reset_servo_feedback_state(active=False, source="disconnected")
        self._reset_io_runtime_state(active=False, source="disconnected")
        self._reset_bridge_caps_state(active=False, source="disconnected")

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
            return self._bus_ser is not None and self._bus_ser.is_open
        elif m == self.MODE_WIFI_FULL:
            return self._sock is not None and self._udp_target is not None
        elif m == self.MODE_DUAL_ESP32_WIFI:
            return (
                self._sock is not None and self._udp_target is not None
                and self._servo_sock is not None and self._servo_udp_target is not None
            )
        return False

    def can_send_sound(self) -> bool:
        m = self._mode
        if m in (self.MODE_ESP32_USB, self.MODE_DUAL_USB):
            return self._ser is not None and self._ser.is_open
        if m in (self.MODE_WIFI_DEBUG_USB, self.MODE_WIFI_FULL, self.MODE_DUAL_ESP32_WIFI):
            with self._lock:
                return self._sock is not None and self._udp_target is not None
        return False

    def is_sound_link_verified(self, max_age_s: float = 3.0) -> bool:
        m = self._mode
        if m in (self.MODE_ESP32_USB, self.MODE_DUAL_USB):
            return self._ser is not None and self._ser.is_open
        if m in (self.MODE_WIFI_DEBUG_USB, self.MODE_WIFI_FULL, self.MODE_DUAL_ESP32_WIFI):
            return self.has_live_io_link(max_age_s=max_age_s)
        return False

    def has_live_io_link(self, max_age_s: float = 3.0) -> bool:
        with self._lock:
            sock = self._sock
            udp_target = self._udp_target
            runtime = dict(self._io_runtime)
        if sock is None or udp_target is None:
            return False
        source = str(runtime.get("source") or "")
        if source not in ("esp32-state", "esp32-ack"):
            return False
        last_update = float(runtime.get("last_update") or 0.0)
        if last_update <= 0.0:
            return False
        return (time.time() - last_update) <= float(max_age_s)

    def sound_transport_info(self) -> str:
        m = self._mode
        if m in (self.MODE_WIFI_DEBUG_USB, self.MODE_WIFI_FULL, self.MODE_DUAL_ESP32_WIFI):
            with self._lock:
                sock = self._sock
                udp_target = self._udp_target
                runtime = dict(self._io_runtime)
            if sock is None or udp_target is None:
                return "Sound link unavailable: ESP32 WiFi/UDP not connected"
            if self.has_live_io_link():
                return f"Sound link ready: ESP32 WiFi {udp_target[0]}:{udp_target[1]}"
            source = str(runtime.get("source") or "")
            if source == "waiting":
                return f"Sound link standby: ESP32 WiFi {udp_target[0]}:{udp_target[1]} awaiting runtime reply"
            last_update = float(runtime.get("last_update") or 0.0)
            if last_update > 0.0:
                age_s = max(0.0, time.time() - last_update)
                return f"Sound link standby: ESP32 WiFi {udp_target[0]}:{udp_target[1]} runtime stale ({age_s:.1f}s)"
            return f"Sound link standby: ESP32 WiFi {udp_target[0]}:{udp_target[1]} send path ready"
        if self.can_send_sound():
            if m in (self.MODE_ESP32_USB, self.MODE_DUAL_USB):
                return "Sound link ready: ESP32 serial"
            if self._udp_target is not None:
                return f"Sound link ready: ESP32 WiFi {self._udp_target[0]}:{self._udp_target[1]}"
            return "Sound link ready"
        if m == self.MODE_WIFI_DEBUG_USB:
            return "Sound link unavailable: ESP32 WiFi/UDP not connected"
        if m == self.MODE_DUAL_ESP32_WIFI:
            return "Sound link unavailable: primary ESP32 WiFi not connected"
        return "Sound link unavailable"

    def _bridge_optional_feature_supported(self, feature_name: str) -> bool:
        m = self._mode
        if m not in (self.MODE_WIFI_DEBUG_USB, self.MODE_WIFI_FULL, self.MODE_DUAL_ESP32_WIFI):
            return True
        with self._lock:
            caps = dict(self._bridge_caps)
        if not bool(caps.get("active")):
            return True
        value = caps.get(feature_name)
        return value is not False

    def _bridge_optional_feature_noop(self, feature_name: str, label: str) -> bool:
        self._last_cmd = f"{label} ignored: bridge reports {feature_name}=false"
        self._last_error = ""
        return True

    def connection_info(self) -> str:
        if not self.is_connected():
            return "Disconnected"
        m = self._mode
        if m == self.MODE_ESP32_USB:
            return f"ESP32 USB: {self._ser.port} @ {self._ser.baudrate}"
        elif m == self.MODE_DUAL_USB:
            return f"ESP32: {self._ser.port} | Debug: {self._bus_ser.port}"
        elif m == self.MODE_WIFI_DEBUG_USB:
            if self._udp_target is not None:
                return f"WiFi: {self._udp_target[0]}:{self._udp_target[1]} | Debug: {self._bus_ser.port}"
            return f"Debug: {self._bus_ser.port} | WiFi: unavailable"
        elif m == self.MODE_WIFI_FULL:
            return f"WiFi: {self._udp_target[0]}:{self._udp_target[1]} (full)"
        elif m == self.MODE_DUAL_ESP32_WIFI:
            return f"Primary: {self._udp_target[0]}:{self._udp_target[1]} | Servo: {self._servo_udp_target[0]}:{self._servo_udp_target[1]}"
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

    def _normalize_feedback_angles(self, pan: float, tilt: float) -> tuple[float, float]:
        """Convert hardware servo readback angles back to Smart Sentry logical angles."""
        pan_logical = max(self.PAN_OUTPUT_MIN, min(self.PAN_OUTPUT_MAX, float(pan)))
        tilt_logical = max(self.TILT_OUTPUT_MIN, min(self.TILT_OUTPUT_MAX, float(tilt)))
        if self.invert_pan:
            pan_logical = self.PAN_OUTPUT_MAX - pan_logical
        if self.invert_tilt:
            tilt_logical = self.TILT_OUTPUT_MAX - tilt_logical
        return (
            max(self.PAN_OUTPUT_MIN, min(self.PAN_OUTPUT_MAX, pan_logical)),
            max(self.TILT_OUTPUT_MIN, min(self.TILT_OUTPUT_MAX, tilt_logical)),
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

    def set_on_transport_log(self, callback: Optional[Callable[[str], None]]) -> None:
        """Register a callback for raw transport/log activity from the ESP32 link."""
        self._on_transport_log = callback

    def inject_pir_event(self, sensor_id: int) -> None:
        """
        Manually inject a PIR sensor event (useful for testing).
        In production, this would be called when parsing telemetry from ESP32.
        """
        if self._on_pir_event is not None:
            self._on_pir_event(sensor_id, time.time())

    def send_pir_enabled(self, enabled: bool) -> bool:
        value = 1 if bool(enabled) else 0
        m = self._mode
        if m in (self.MODE_ESP32_USB, self.MODE_DUAL_USB):
            with self._lock:
                ser = self._ser
            try:
                if ser is None or not ser.is_open:
                    return False
                cmd = f"P{value}\n"
                ser.write(cmd.encode("utf-8"))
                self._last_cmd = cmd.rstrip()
                return True
            except Exception as e:
                self._last_error = str(e)
                return False
        if m in (self.MODE_WIFI_DEBUG_USB, self.MODE_WIFI_FULL, self.MODE_DUAL_ESP32_WIFI):
            return self._send_udp_payload({"pir_enabled": value}, label=f"UDP PIR P{value}")
        return False

    def send_sound(self, freq_hz: int, duration_ms: int, volume_pct: int = 100) -> bool:
        freq = int(max(120, min(6000, int(freq_hz))))
        duration = int(max(10, min(2000, int(duration_ms))))
        volume = int(max(0, min(100, int(volume_pct))))
        m = self._mode
        if m in (self.MODE_ESP32_USB, self.MODE_DUAL_USB):
            with self._lock:
                ser = self._ser
            try:
                if ser is None or not ser.is_open:
                    self._last_error = "ESP32 serial sound transport unavailable"
                    return False
                cmd = f"SOUND:{freq}:{duration}\n"
                ser.write(cmd.encode("utf-8"))
                self._last_cmd = cmd.rstrip()
                self._last_error = ""
                return True
            except Exception as e:
                self._last_error = str(e)
                return False
        if m in (self.MODE_WIFI_DEBUG_USB, self.MODE_WIFI_FULL, self.MODE_DUAL_ESP32_WIFI):
            if not self.can_send_sound():
                self._last_error = self.sound_transport_info()
                return False
            ok = self._send_udp_payload(
                {
                    "action": "sound",
                    "freq_hz": freq,
                    "duration_ms": duration,
                    "volume_pct": volume,
                },
                label=f"UDP SOUND {freq}Hz {duration}ms @{volume}%",
            )
            if ok:
                self._last_error = ""
            return ok
        self._last_error = "Sound transport unavailable for current connection mode"
        return False

    def send_sweep(self) -> bool:
        m = self._mode
        if m in (self.MODE_WIFI_DEBUG_USB, self.MODE_WIFI_FULL, self.MODE_DUAL_ESP32_WIFI):
            ok = self._send_udp_payload({"action": "sweep"}, label="UDP SWEEP")
            if ok:
                self._last_error = ""
            return ok
        self._last_error = "Sweep action requires ESP32 WiFi/UDP transport"
        return False

    def send_command(
        self,
        pan: float,
        tilt: float,
        fire: int = 0,
        move_time_ms: Optional[int] = None,
        allow_rest_tilt: bool = False,
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
            return self._send_wifi_full(pan_out, tilt_out, fire, move_time_ms=move_time_ms, allow_rest_tilt=allow_rest_tilt)
        elif m == self.MODE_DUAL_ESP32_WIFI:
            # Send servo commands to secondary ESP32
            ok_servo = self._send_servo_udp(pan_out, tilt_out, move_time_ms=move_time_ms)
            # Send IO commands to primary ESP32
            ok_io = self._send_io_udp(fire)
            return ok_servo and ok_io
        return False

    def _start_receiver(self) -> None:
        if self._receiver_thread is not None and self._receiver_thread.is_alive():
            return
        self._receiver_stop.clear()
        self._serial_rx_buffer = ""
        self._receiver_thread = threading.Thread(
            target=self._receiver_loop,
            name="sentry-v2-comm-rx",
            daemon=True,
        )
        self._receiver_thread.start()
        if self._sock is not None and self._udp_target is not None:
            self._send_udp_message("hello", None, label="UDP hello")

    def _stop_receiver(self) -> None:
        self._receiver_stop.set()
        thread = self._receiver_thread
        self._receiver_thread = None
        if thread is not None and thread.is_alive():
            thread.join(timeout=0.35)

    def _receiver_loop(self) -> None:
        while not self._receiver_stop.is_set():
            try:
                self._poll_serial_events()
                self._poll_udp_events()
                self._poll_bus_servo_feedback()
            except Exception:
                pass
            time.sleep(0.02)

    def _poll_bus_servo_feedback(self) -> None:
        # CHANGE WARNING: Debug Board readback shares the same COM port as bus-servo
        # writes; keep polling serialized and conservative so read attempts cannot
        # starve pan/tilt motion during active tracking.
        if self._mode not in (self.MODE_DUAL_USB, self.MODE_WIFI_DEBUG_USB):
            return
        now = time.time()
        if now < self._feedback_pause_until_s:
            return
        if now < self._feedback_next_poll_time:
            return
        if now - self._feedback_last_motion_time < self._feedback_post_move_delay_s:
            return

        with self._lock:
            bus_ser = self._bus_ser
            pan_servo_id = int(self.pan_servo_id)
            tilt_servo_id = int(self.tilt_servo_id)
        if bus_ser is None or not bus_ser.is_open:
            return

        pan_ticks = self._read_bus_servo_register(pan_servo_id, 0x38, 2)
        tilt_ticks = self._read_bus_servo_register(tilt_servo_id, 0x38, 2)

        if pan_ticks is None or tilt_ticks is None:
            with self._lock:
                self._feedback_waiting_miss_count += 1
                self._servo_feedback["active"] = True
                self._servo_feedback["source"] = "waiting"
                if not self._servo_feedback.get("last_update"):
                    self._servo_feedback["last_error"] = "Waiting for first servo feedback reply"
                pause_s = 0.0
                if self._feedback_waiting_miss_count >= 12:
                    pause_s = 20.0
                    self._servo_feedback["last_error"] = "Waiting for first servo feedback reply (polling paused)"
                elif self._feedback_waiting_miss_count >= 4:
                    pause_s = 5.0
                    self._servo_feedback["last_error"] = "Waiting for first servo feedback reply (polling throttled)"
                if pause_s > 0.0:
                    self._feedback_pause_until_s = now + pause_s
            self._feedback_next_poll_time = now + self._feedback_waiting_poll_interval_s
            return

        pan_deg, tilt_deg = self._normalize_feedback_angles(
            self._ticks_to_deg(pan_ticks),
            self._ticks_to_deg(tilt_ticks),
        )
        with self._lock:
            self._feedback_waiting_miss_count = 0
            self._feedback_pause_until_s = 0.0
            self._servo_feedback.update(
                {
                    "active": True,
                    "source": "debug-board",
                    "pan_deg": pan_deg,
                    "tilt_deg": tilt_deg,
                    "pan_ticks": pan_ticks,
                    "tilt_ticks": tilt_ticks,
                    "last_update": now,
                    "last_error": "",
                }
            )
            self._feedback_next_poll_time = now + self._feedback_poll_interval_s
        self._poll_bus_servo_diagnostics(now, pan_servo_id, tilt_servo_id)

    def _poll_bus_servo_diagnostics(self, now: float, pan_servo_id: int, tilt_servo_id: int) -> None:
        if now < self._feedback_diag_next_poll_time:
            return
        pan_load_raw = self._read_bus_servo_register(pan_servo_id, 0x3C, 2, timeout_s=0.05)
        tilt_load_raw = self._read_bus_servo_register(tilt_servo_id, 0x3C, 2, timeout_s=0.05)
        pan_voltage_raw = self._read_bus_servo_register(pan_servo_id, 0x3E, 1, timeout_s=0.05)
        tilt_voltage_raw = self._read_bus_servo_register(tilt_servo_id, 0x3E, 1, timeout_s=0.05)

        def _decode_signed_16(value: Optional[int]) -> Optional[int]:
            if value is None:
                return None
            raw = int(value) & 0xFFFF
            return raw - 0x10000 if raw >= 0x8000 else raw

        def _decode_voltage(raw_value: Optional[int]) -> Optional[float]:
            if raw_value is None:
                return None
            return float(int(raw_value)) / 10.0

        with self._lock:
            self._servo_feedback.update(
                {
                    "pan_load_raw": _decode_signed_16(pan_load_raw),
                    "tilt_load_raw": _decode_signed_16(tilt_load_raw),
                    "pan_voltage_raw": None if pan_voltage_raw is None else int(pan_voltage_raw),
                    "tilt_voltage_raw": None if tilt_voltage_raw is None else int(tilt_voltage_raw),
                    "pan_voltage_v": _decode_voltage(pan_voltage_raw),
                    "tilt_voltage_v": _decode_voltage(tilt_voltage_raw),
                    "diag_last_update": now,
                }
            )
            self._feedback_diag_next_poll_time = now + self._feedback_diag_poll_interval_s

    def _poll_serial_events(self) -> None:
        with self._lock:
            ser = self._ser
        if ser is None or not ser.is_open:
            return
        try:
            waiting = int(getattr(ser, "in_waiting", 0) or 0)
        except Exception:
            waiting = 0
        if waiting <= 0:
            return
        try:
            chunk = ser.read(waiting)
        except Exception:
            return
        if not chunk:
            return
        self._serial_rx_buffer += chunk.decode("utf-8", errors="ignore")
        while "\n" in self._serial_rx_buffer:
            line, self._serial_rx_buffer = self._serial_rx_buffer.split("\n", 1)
            self._handle_serial_line(line.strip())

    def _poll_udp_events(self) -> None:
        with self._lock:
            sock = self._sock
        if sock is None:
            return
        while not self._receiver_stop.is_set():
            try:
                packet, _addr = sock.recvfrom(4096)
            except BlockingIOError:
                return
            except Exception:
                return
            if not packet:
                return
            self._handle_udp_packet(packet)

    def _handle_serial_line(self, line: str) -> None:
        if not line:
            return
        self._emit_transport_log(f"ESP32 USB RX {line}")
        match = re.search(r"PIR_EVENT\s+sensor_id=(\d+)\s+timestamp=(\d+)", line, re.IGNORECASE)
        if not match:
            match = re.search(r"\[PIR\]\s*Sensor\s+(\d+)\s+triggered\b.*?\bt=(\d+)", line, re.IGNORECASE)
        if not match:
            return
        sensor_id = int(match.group(1))
        timestamp_ms = int(match.group(2))
        self._dispatch_pir_event(sensor_id, timestamp_ms / 1000.0)

    def _handle_udp_packet(self, packet: bytes) -> None:
        try:
            message = json.loads(packet.decode("utf-8", errors="ignore"))
        except Exception:
            return
        if not isinstance(message, dict):
            return
        message_type = str(message.get("t") or "").strip().lower()
        if message_type == "state":
            payload = message.get("p") or {}
            if isinstance(payload, dict):
                self._apply_io_runtime_state(payload, source="esp32-state", timestamp_ms=message.get("ts"))
                self._emit_udp_state_trace(payload, timestamp_ms=message.get("ts"))
            return
        if message_type == "ack":
            payload = message.get("p") or message.get("state") or {}
            if isinstance(payload, dict):
                self._apply_io_runtime_state(payload, source="esp32-ack", timestamp_ms=message.get("ts"))
                summary = self._summarize_runtime_payload_for_log(payload)
                self._emit_transport_log(f"ESP32 UDP ACK {summary}" if summary else "ESP32 UDP ACK")
            return
        if message_type == "cap":
            payload = message.get("p") or {}
            if isinstance(payload, dict):
                self._apply_bridge_caps(payload, source="esp32-cap", timestamp_ms=message.get("ts"))
                summary = self._summarize_caps_payload_for_log(payload)
                self._emit_transport_log(f"ESP32 UDP CAPS {summary}" if summary else "ESP32 UDP CAPS")
            return
        if message_type != "pir_event":
            return
        payload = message.get("p") or {}
        if not isinstance(payload, dict):
            return
        try:
            sensor_id = int(payload.get("sensor_id"))
        except Exception:
            return
        raw_ts = payload.get("timestamp_ms", message.get("ts", 0))
        try:
            timestamp = float(raw_ts) / 1000.0
        except Exception:
            timestamp = time.time()
        try:
            trace_ts = int(float(raw_ts))
        except Exception:
            trace_ts = 0
        self._emit_transport_log(f"ESP32 UDP RX PIR S{sensor_id + 1} ts={trace_ts}")
        self._dispatch_pir_event(sensor_id, timestamp)

    def _dispatch_pir_event(self, sensor_id: int, timestamp: float) -> None:
        callback = self._on_pir_event
        if callback is None:
            return
        try:
            callback(int(sensor_id), float(timestamp))
        except Exception as exc:
            self._report_runtime_warning("PIR event callback failed", exc)

    def send_movement(
        self,
        pan: float,
        tilt: float,
        *,
        move_time_ms: Optional[int] = None,
        allow_rest_tilt: bool = False,
    ) -> bool:
        """Send pan/tilt movement without coupling bus-servo motion to IO delivery.

        In Debug Board modes, motion should continue even when ESP32 IO state is unchanged.
        """
        pan_out, tilt_out = self._normalize_output_angles(pan, tilt)
        m = self._mode
        if m == self.MODE_ESP32_USB:
            ok = self._send_ascii(pan_out, tilt_out, fire=0, via_serial=True)
            if ok:
                self._last_error = ""
            return ok
        if m == self.MODE_DUAL_USB:
            ok_bus = self._send_bus_servo(pan_out, tilt_out, move_time_ms=move_time_ms)
            if ok_bus:
                self._last_error = ""
                self._send_io_serial(0)
            return ok_bus
        if m == self.MODE_WIFI_DEBUG_USB:
            ok_bus = self._send_bus_servo(pan_out, tilt_out, move_time_ms=move_time_ms)
            if ok_bus:
                self._last_error = ""
                # Keep mode-2 movement aligned with the earlier working path by
                # refreshing the IO-side safety/mode state when WiFi is present,
                # while still allowing pan/tilt movement to succeed if WiFi drops.
                self._send_io_udp(0)
            return ok_bus
        if m == self.MODE_WIFI_FULL:
            ok = self._send_wifi_full(pan_out, tilt_out, fire=0, move_time_ms=move_time_ms, allow_rest_tilt=allow_rest_tilt)
            if ok:
                self._last_error = ""
            return ok
        if m == self.MODE_DUAL_ESP32_WIFI:
            ok = self._send_servo_udp(pan_out, tilt_out, move_time_ms=move_time_ms)
            if ok:
                self._last_error = ""
            return ok
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
        """Backward-compat shim: maps bool on/off to PWM 255/0."""
        return self.set_led_pwm(255 if on else 0, pan, tilt)

    def set_led_pwm(self, pwm: int, pan: float, tilt: float) -> bool:
        """Set LED brightness via 8-bit PWM value (0-255)."""
        if not self._bridge_optional_feature_supported("led_relay_assigned"):
            self.led_pwm = 0
            return self._bridge_optional_feature_noop("led_relay_assigned", "LED")
        self.led_pwm = int(max(0, min(255, pwm)))
        return self.send_command(pan, tilt)

    def set_laser(self, on: bool, pan: float, tilt: float) -> bool:
        if not self._bridge_optional_feature_supported("laser_relay_assigned"):
            self.laser_on = False
            return self._bridge_optional_feature_noop("laser_relay_assigned", "Laser")
        self.laser_on = on
        return self.send_command(pan, tilt)

    def set_acc(self, on: bool, pan: float, tilt: float) -> bool:
        """Control GPIO 25 accessory relay (G token)."""
        self.acc_on = on
        return self.send_command(pan, tilt)

    def set_spare(self, on: bool, pan: float, tilt: float) -> bool:
        """Control GPIO 26 spare relay (A token)."""
        self.spare_on = on
        return self.send_command(pan, tilt)

    def set_safety(self, armed: bool, pan: float, tilt: float) -> bool:
        self.safety_armed = armed
        return self.send_command(pan, tilt)

    def send_trigger_runtime_config(self) -> bool:
        m = self._mode
        if m in (self.MODE_ESP32_USB, self.MODE_DUAL_USB):
            return self._send_trigger_runtime_config_serial()
        if not self._bridge_optional_feature_supported("trigger_servo_assigned"):
            return self._bridge_optional_feature_noop("trigger_servo_assigned", "Trigger runtime config")
        payload: Dict[str, Any] = {
            "action": "config",
            "trigger": {
                "mode": 1 if self.trigger_mode_bb else 0,
                "servo_rest_deg": int(max(0, min(180, int(self.trigger_servo_rest_deg)))),
                "servo_fire_deg": int(max(0, min(180, int(self.trigger_servo_fire_deg)))),
                "servo_speed_dps": int(max(10, min(5000, int(self.trigger_servo_speed_dps)))),
            },
            "rest": {
                "pan": float(max(self.PAN_OUTPUT_MIN, min(self.PAN_OUTPUT_MAX, float(self.rest_pan)))),
                "tilt": float(max(self.TILT_OUTPUT_MIN, min(self.TILT_OUTPUT_MAX, float(self.rest_tilt)))),
            },
            "pir": {
                "event_blink": 1 if self.pir_event_blink_enabled else 0,
            },
        }
        ok = self._send_udp_payload(payload, label="UDP CFG trigger-servo/pir-led")
        if ok:
            self._last_error = ""
        return ok

    def set_control_source_mode(self, mode: str) -> bool:
        requested_mode = str(mode or "app").strip().lower()
        if requested_mode not in ("app", "rc", "auto"):
            self._last_error = f"Unsupported control source mode: {mode}"
            return False
        m = self._mode
        if m not in (self.MODE_WIFI_DEBUG_USB, self.MODE_WIFI_FULL, self.MODE_DUAL_ESP32_WIFI):
            self._last_error = "Control source mode requires ESP32 WiFi bridge mode"
            return False
        ok = self._send_udp_payload(
            {
                "action": "rc_mode",
                "mode": requested_mode,
                "control_source_mode": requested_mode,
            },
            label=f"UDP RC MODE {requested_mode}",
        )
        if ok:
            self._last_error = ""
        return ok

    def _send_trigger_runtime_config_serial(self) -> bool:
        with self._lock:
            ser = self._ser
        try:
            if ser is None or not ser.is_open:
                return False
            rest_deg = int(max(0, min(180, int(self.trigger_servo_rest_deg))))
            fire_deg = int(max(rest_deg, min(180, int(self.trigger_servo_fire_deg))))
            speed_dps = int(max(10, min(5000, int(self.trigger_servo_speed_dps))))
            pir_blink = 1 if self.pir_event_blink_enabled else 0
            ser.write(f"U{rest_deg}\n".encode("utf-8"))
            ser.write(f"V{fire_deg}\n".encode("utf-8"))
            ser.write(f"H{speed_dps}\n".encode("utf-8"))
            ser.write(f"B{pir_blink}\n".encode("utf-8"))
            self._last_cmd = f"SER CFG U{rest_deg} V{fire_deg} H{speed_dps} B{pir_blink}"
            self._last_error = ""
            return True
        except Exception as e:
            self._last_error = str(e)
            return False

    # ------------------------------------------------------------------ #
    #  ASCII protocol  (modes 0, 3)
    # ------------------------------------------------------------------ #

    def _build_ascii(self, pan: float, tilt: float, fire: int = 0) -> str:
        p = int(max(self.PAN_OUTPUT_MIN, min(self.PAN_OUTPUT_MAX, round(pan))))
        t = int(max(self.TILT_OUTPUT_MIN, min(self.TILT_OUTPUT_MAX, round(tilt))))
        f = int(bool(fire))
        led = int(max(0, min(255, self.led_pwm)))
        laser = 1 if self.laser_on else 0
        acc = 1 if self.acc_on else 0
        spare = 1 if self.spare_on else 0
        safety = 0 if self.safety_armed else 1
        mode = 1 if self.trigger_mode_bb else 0
        return f"P{p}T{t}F{f}L{led}R{laser}G{acc}A{spare}S{safety}M{mode}\n"

    def _send_ascii(self, pan: float, tilt: float, fire: int, *, via_serial: bool) -> bool:
        cmd = self._build_ascii(pan, tilt, fire)
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
        allow_rest_tilt: bool = False,
    ) -> bool:
        payload: Dict[str, Any] = {
            "pan_cmd": int(max(self.PAN_OUTPUT_MIN, min(self.PAN_OUTPUT_MAX, round(pan)))),
            "tilt_cmd": int(max(self.TILT_OUTPUT_MIN, min(self.TILT_OUTPUT_MAX, round(tilt)))),
            "fire": int(bool(fire)),
            "safety": 0 if self.safety_armed else 1,
            "mode": 1 if self.trigger_mode_bb else 0,
            "led": int(max(0, min(255, self.led_pwm))),
            "laser": 1 if self.laser_on else 0,
            "acc": 1 if self.acc_on else 0,
            "spare": 1 if self.spare_on else 0,
        }
        if allow_rest_tilt:
            payload["allow_rest_tilt"] = 1
        if move_time_ms is not None:
            payload["move_time_ms"] = int(max(0, min(5000, int(move_time_ms))))
        label = (
            f"UDP P{payload['pan_cmd']}T{payload['tilt_cmd']}F{payload['fire']}"
            f"L{payload['led']}R{payload['laser']}G{payload['acc']}A{payload['spare']}"
            f"S{payload['safety']}M{payload['mode']}"
        )
        return self._send_udp_payload(payload, label=label)

    def _send_servo_udp(self, pan: float, tilt: float, move_time_ms: Optional[int] = None) -> bool:
        """Send servo position command to secondary ESP32 over UDP."""
        payload = {
            "pan_cmd": round(pan, 2),
            "tilt_cmd": round(tilt, 2),
        }
        if move_time_ms is not None:
            payload["move_time_ms"] = int(move_time_ms)
        return self._send_udp_payload_secondary(payload, label=f"UDP Servo P{pan:.1f} T{tilt:.1f}")

    # ------------------------------------------------------------------ #
    #  Bus servo protocol  (modes 1, 2)
    # ------------------------------------------------------------------ #

    def _deg_to_ticks(self, deg: float) -> int:
        """Map 0..270 degrees to 0..4095 ticks."""
        d = max(0.0, min(270.0, float(deg)))
        return int(round((d / 270.0) * 4095.0))

    def _ticks_to_deg(self, ticks: int) -> float:
        raw = max(0, min(4095, int(ticks)))
        return (float(raw) / 4095.0) * 270.0

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

    def _build_read_packet(self, servo_id: int, register_addr: int, read_len: int) -> bytes:
        sid = int(servo_id) & 0xFF
        addr = int(register_addr) & 0xFF
        size = max(1, min(8, int(read_len)))
        payload = bytes([sid, 0x04, 0x02, addr, size])
        chk = self._bus_checksum(payload)
        return b"\xFF\xFF" + payload + bytes([chk])

    def _extract_bus_reply_payload(self, response: bytes, servo_id: int) -> Optional[bytes]:
        data = bytes(response or b"")
        start = -1
        header_len = 0
        for candidate in (b"\xFF\xFF", b"\xFF\xF5"):
            idx = data.find(candidate)
            if idx >= 0:
                start = idx
                header_len = len(candidate)
                break
        if start < 0 or len(data) < start + header_len + 4:
            return None
        packet = data[start:]
        packet = packet[header_len - 2:]
        if len(packet) < 6 or packet[2] != (int(servo_id) & 0xFF):
            return None
        declared_len = int(packet[3])
        total_len = declared_len + 4
        if declared_len < 2 or len(packet) < total_len:
            return None
        packet = packet[:total_len]
        checksum = self._bus_checksum(packet[2:-1])
        if checksum != packet[-1]:
            return None
        if packet[4] != 0x00:
            return None
        return bytes(packet[5:-1])

    def _read_bus_servo_register(
        self,
        servo_id: int,
        register_addr: int,
        read_len: int,
        *,
        timeout_s: float = 0.06,
    ) -> Optional[int]:
        with self._lock:
            bus_ser = self._bus_ser
        if bus_ser is None or not bus_ser.is_open:
            return None
        try:
            with self._bus_io_lock:
                try:
                    bus_ser.reset_input_buffer()
                except Exception:
                    pass
                bus_ser.write(self._build_read_packet(servo_id, register_addr, read_len))
                try:
                    bus_ser.flush()
                except Exception:
                    pass

                end = time.time() + float(timeout_s)
                buf = bytearray()
                while time.time() < end and len(buf) < 64:
                    try:
                        chunk = bus_ser.read(64)
                    except Exception:
                        chunk = b""
                    if chunk:
                        buf.extend(chunk)
                        payload = self._extract_bus_reply_payload(bytes(buf), servo_id)
                        if payload is not None and len(payload) >= int(read_len):
                            value = 0
                            for byte in payload[: int(read_len)]:
                                value = (value << 8) | int(byte)
                            return value
                    else:
                        time.sleep(0.005)
        except Exception as exc:
            with self._lock:
                self._servo_feedback["last_error"] = str(exc)
        return None

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
            with self._bus_io_lock:
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
            
            # Accept both direct-servo replies (FF FF ...) and the observed
            # debug-board forwarded reply header (FF F5 ...).
            if len(buf) >= 4 and buf[0] == 0xFF and buf[1] in (0xFF, 0xF5):
                return bytes(buf)
            else:
                # Not a valid servo response - return empty to indicate no servo detected
                return b""
        except Exception:
            return b""

    def _probe_bus_servo_checksum(self, active_ser: Optional[_serial.Serial]) -> Optional[str]:
        if active_ser is None or not active_ser.is_open:
            self._bus_servo_ping_ok = False
            self._bus_checksum_mode = "sub"
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
            self._bus_checksum_mode = original_mode if original_mode in ("sub", "xor") else "sub"
            return None
        finally:
            if self._bus_checksum_mode not in ("sub", "xor"):
                self._bus_checksum_mode = original_mode if original_mode in ("sub", "xor") else "sub"

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
        # CHANGE WARNING: This write path shares the Debug Board serial link with
        # background feedback polling. Keep actual packet writes inside the bus IO
        # lock and push the next feedback poll out so engagement bursts do not
        # deadlock into repeated write timeouts on marginal hardware.
        """Send pan/tilt to debug board via bus servo binary packets."""
        now = time.time()
        with self._lock:
            bus_ser = self._bus_ser
            pan_servo_id = self.pan_servo_id
            tilt_servo_id = self.tilt_servo_id
            checksum_mode = str(self._bus_checksum_mode or "auto").lower()
            default_move_time = self.bus_servo_time_ms
            last_pan_ticks = self._last_bus_pan_ticks
            last_tilt_ticks = self._last_bus_tilt_ticks
            allow_axis_dedup = self._has_fresh_servo_feedback_locked(now)
        try:
            if bus_ser is None or not bus_ser.is_open:
                return False
            move_time = int(default_move_time if move_time_ms is None else move_time_ms)
            move_time = max(0, min(1000, move_time))
            pan_ticks = self._deg_to_ticks(pan)
            tilt_ticks = self._deg_to_ticks(tilt)
            send_pan = True
            send_tilt = True
            if allow_axis_dedup:
                send_pan = last_pan_ticks is None or pan_ticks != int(last_pan_ticks)
                send_tilt = last_tilt_ticks is None or tilt_ticks != int(last_tilt_ticks)

            if not send_pan and not send_tilt:
                self._last_cmd = f"BUS hold P{pan:.0f} T{tilt:.0f} @{move_time}ms [{checksum_mode}]"
                return True

            def _write_pair(candidate_mode: str) -> None:
                original_mode = self._bus_checksum_mode
                self._bus_checksum_mode = candidate_mode
                try:
                    pan_pkt = self._build_servo_packet(pan_servo_id, pan_ticks, move_time) if send_pan else None
                    tilt_pkt = self._build_servo_packet(tilt_servo_id, tilt_ticks, move_time) if send_tilt else None
                finally:
                    self._bus_checksum_mode = original_mode
                with self._bus_io_lock:
                    if pan_pkt is not None:
                        bus_ser.write(pan_pkt)
                    if tilt_pkt is not None:
                        bus_ser.write(tilt_pkt)
                    try:
                        bus_ser.flush()
                    except Exception:
                        pass
                with self._lock:
                    if pan_pkt is not None:
                        self._last_bus_pan_ticks = pan_ticks
                    if tilt_pkt is not None:
                        self._last_bus_tilt_ticks = tilt_ticks

            if checksum_mode == "auto":
                for candidate_mode in ("sub", "xor"):
                    _write_pair(candidate_mode)
                    time.sleep(0.002)
            else:
                _write_pair(checksum_mode)

            self._feedback_last_motion_time = now
            self._feedback_next_poll_time = max(
                self._feedback_next_poll_time,
                now + self._feedback_post_move_delay_s,
            )
            sent_axes = []
            if send_pan:
                sent_axes.append(f"P{pan:.0f}")
            if send_tilt:
                sent_axes.append(f"T{tilt:.0f}")
            self._last_cmd = f"BUS {' '.join(sent_axes)} @{move_time}ms [{checksum_mode}]"
            return True
        except Exception as e:
            self._reset_bus_motion_cache()
            self._feedback_last_motion_time = now
            self._feedback_next_poll_time = max(
                self._feedback_next_poll_time,
                now + self._feedback_waiting_poll_interval_s,
            )
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
            "led": int(max(0, min(255, self.led_pwm))),
            "laser": 1 if self.laser_on else 0,
            "acc": 1 if self.acc_on else 0,
            "spare": 1 if self.spare_on else 0,
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
            label=f"UDP IO F{io['fire']}L{io['led']}R{io['laser']}S{io['safety']}M{io['mode']}A{io['acc']}P{io['spare']}",
        )
        if ok:
            self._last_cmd += f" | UDP IO F{io['fire']}L{io['led']}R{io['laser']}A{io['acc']}P{io['spare']}"
        return ok


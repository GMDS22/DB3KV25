#!/usr/bin/env python3
"""Focused regression checks for connection availability diagnostics."""

import sys
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).parent))

from app.sentry_v2.sentry_v2_comm import SentryV2Comm
from app.sentry_v2.sentry_v2_tab import SentryV2TabWidget


class _FakeConnectionTab:
    def __init__(self) -> None:
        self._comm = SimpleNamespace(SERIAL_IO_LABEL=SentryV2Comm.SERIAL_IO_LABEL)
        self.config = SimpleNamespace(connection=SimpleNamespace(esp32_port="COM7", debug_port="COM8"))

    def _list_serial_ports_normalized(self):
        return [("COM3", "USB-SERIAL CH340"), ("COM4", "CP210 USB to UART")]

    def _resolve_serial_port(self, target: str, preferred_port: str = "") -> str:
        return ""

    def _wifi_credentials_candidates_for_mode(self, mode: int):
        return [("SMART-SENTRY-V2.3", "db3000pass")]

    def _windows_wifi_current_ssid(self) -> str:
        return "OfficeWiFi"

    def _windows_wifi_network_available(self, ssid: str) -> bool:
        return ssid == "SMART-SENTRY-V2.3"

    def _normalize_ssid(self, ssid: str) -> str:
        return SentryV2TabWidget._normalize_ssid(self, ssid)

    def _ssid_matches_expected(self, candidate_ssid: str, expected_ssids):
        return SentryV2TabWidget._ssid_matches_expected(self, candidate_ssid, expected_ssids)

    def _connection_detail_map(self, details):
        return SentryV2TabWidget._connection_detail_map(self, details)

    def _summarize_visible_com_ports(self, ports, limit: int = 6) -> str:
        return SentryV2TabWidget._summarize_visible_com_ports(self, ports, limit=limit)

    def _connection_serial_port_note(self, target: str, label: str, configured_port: str, detail_value: str, *, visible_ports=None) -> str:
        return SentryV2TabWidget._connection_serial_port_note(
            self,
            target,
            label,
            configured_port,
            detail_value,
            visible_ports=visible_ports,
        )

    def _connection_wifi_link_note(self, mode: int) -> str:
        return SentryV2TabWidget._connection_wifi_link_note(self, mode)


class _FakeButton:
    def __init__(self) -> None:
        self.enabled = True
        self.text = ""

    def setEnabled(self, value: bool) -> None:
        self.enabled = bool(value)

    def setText(self, value: str) -> None:
        self.text = str(value)


class _FakeCheckBox:
    def __init__(self, checked: bool = False) -> None:
        self._checked = bool(checked)

    def isChecked(self) -> bool:
        return self._checked

    def setChecked(self, value: bool) -> None:
        self._checked = bool(value)


class _FakeComm:
    SERIAL_IO_LABEL = SentryV2Comm.SERIAL_IO_LABEL

    def __init__(self, *, connected: bool, mode2_wifi_ready: bool = False) -> None:
        self._connected = bool(connected)
        self._sock = object() if mode2_wifi_ready else None
        self._udp_target = ("192.168.4.1", 9000) if mode2_wifi_ready else None
        self.trigger_mode_bb = False

    def is_connected(self) -> bool:
        return self._connected


class _VoiceConnectResultTab(_FakeConnectionTab):
    def __init__(self, *, mode: int, connected: bool, enabled: bool = False, deferred_enable: bool = False, mode2_wifi_ready: bool = False) -> None:
        super().__init__()
        self._comm = _FakeComm(connected=connected, mode2_wifi_ready=mode2_wifi_ready)
        self.config = SimpleNamespace(
            connection=SimpleNamespace(connection_type=mode, esp32_port="COM7", debug_port="COM8"),
            engagement=SimpleNamespace(auto_trigger_enabled=False),
            pir_guard=SimpleNamespace(pir_enabled=False),
        )
        self._btn_connect = _FakeButton()
        self._chk_enable = _FakeCheckBox(enabled)
        self._connection_busy = True
        self._connection_task_label = "connecting Smart Sentry boards"
        self._connection_cancel_requested = False
        self._connection_attempt_context = {
            "mode": mode,
            "preferred_esp32_port": "COM7",
            "preferred_debug_port": "COM8",
            "resolved_esp32_port": "COM7",
            "resolved_debug_port": "",
            "visible_ports": [("COM3", "USB-SERIAL CH340"), ("COM4", "CP210 USB to UART")],
            "udp_host": "192.168.4.1",
            "udp_port": 9000,
        }
        self._voice_protocol_connect_via_voice_active = True
        self._deferred_enable_sentry_after_connect = bool(deferred_enable)
        self._deferred_enable_sentry_reason = "voice connect and enable request"
        self._startup_autoconnect_active = False
        self._startup_autoconnect_retry = 0
        self._closing = False
        self._safety_armed = False
        self.status_updates = []
        self.logs = []
        self.task_updates = []
        self.spoken = []
        self.voice_windows = []
        self.prompt_delays = []
        self.queue_runtime_trigger_calls = 0
        self.auto_yolo_delays = []
        self.startup_rest_calls = 0
        self.home_sync_calls = 0
        self.enable_clear_calls = 0

    def _format_connection_details(self, details, fallback: str) -> str:
        return SentryV2TabWidget._format_connection_details(self, details, fallback)

    def _extract_connection_detail_endpoint(self, detail_value: str) -> str:
        return SentryV2TabWidget._extract_connection_detail_endpoint(self, detail_value)

    def _voice_normalize_connection_phrase(self, text: str) -> str:
        return SentryV2TabWidget._voice_normalize_connection_phrase(self, text)

    def _connection_success_notes(self, mode: int, details, *, current_enabled: bool):
        return SentryV2TabWidget._connection_success_notes(self, mode, details, current_enabled=current_enabled)

    def _connection_diagnostic_notes(self, mode: int, details, *, include_mode2_wifi_warning: bool = False):
        return SentryV2TabWidget._connection_diagnostic_notes(
            self,
            mode,
            details,
            include_mode2_wifi_warning=include_mode2_wifi_warning,
        )

    def _set_connection_status(self, text: str, state: str) -> None:
        self.status_updates.append((str(text), str(state)))

    def _log(self, message: str) -> None:
        self.logs.append(str(message))

    def _sync_home_screen_visibility(self) -> None:
        self.home_sync_calls += 1

    def _queue_runtime_trigger_config_if_connected(self) -> None:
        self.queue_runtime_trigger_calls += 1

    def _schedule_auto_yolo_load(self, delay_ms: int) -> None:
        self.auto_yolo_delays.append(int(delay_ms))

    def _schedule_startup_rest_move(self) -> None:
        self.startup_rest_calls += 1

    def _set_operator_task_status(self, label: str, state: str, detail: str = "") -> None:
        self.task_updates.append((str(label), str(state), str(detail)))

    def _clear_enable_sentry_after_connect(self) -> None:
        self.enable_clear_calls += 1
        self._deferred_enable_sentry_after_connect = False
        self._deferred_enable_sentry_reason = ""

    def _start_voice_interaction_window(self, *, reason: str, hold_s: float) -> None:
        self.voice_windows.append((str(reason), float(hold_s)))

    def _estimate_human_phrase_duration_s(self, phrase: str) -> float:
        return 0.5

    def _speak_human_phrase(self, phrase: str, *, interrupt: bool = True) -> bool:
        self.spoken.append((str(phrase), bool(interrupt)))
        return True

    def _schedule_voice_next_action_prompt(self, *, delay_s: float) -> None:
        self.prompt_delays.append(float(delay_s))


def test_mode2_failure_reports_missing_debug_board_and_visible_wifi() -> None:
    tab = _FakeConnectionTab()

    notes = SentryV2TabWidget._connection_diagnostic_notes(
        tab,
        SentryV2Comm.MODE_WIFI_DEBUG_USB,
        {
            "Debug Board": (False, "No COM port specified"),
            "ESP32 WiFi": (False, "WiFi host unreachable"),
        },
    )

    assert any("Debug Board was not found on any COM port" in note for note in notes)
    assert any("ESP32 WiFi SMART-SENTRY-V2.3 is available" in note and "OfficeWiFi" in note for note in notes)


def test_mode2_degraded_success_still_reports_visible_wifi_gap() -> None:
    tab = _FakeConnectionTab()

    notes = SentryV2TabWidget._connection_diagnostic_notes(
        tab,
        SentryV2Comm.MODE_WIFI_DEBUG_USB,
        {
            "Debug Board": (True, "COM4"),
            "ESP32 WiFi": (False, "WiFi host unreachable"),
        },
        include_mode2_wifi_warning=True,
    )

    assert notes == [
        "ESP32 WiFi SMART-SENTRY-V2.3 is available, but Windows is currently connected to OfficeWiFi instead."
    ]


def test_open_serial_reports_missing_port_inventory() -> None:
    comm = SentryV2Comm()
    original = SentryV2Comm.list_serial_ports
    try:
        SentryV2Comm.list_serial_ports = staticmethod(lambda: [("COM3", "USB-SERIAL CH340"), ("COM4", "Debug Board")])

        assert comm._open_serial("COM8", 115200, primary=False) is False
        assert "COM8 was not found in any available COM port" in comm._last_error
        assert "COM3" in comm._last_error
        assert "COM4" in comm._last_error
    finally:
        SentryV2Comm.list_serial_ports = original


def test_voice_connect_failure_reports_missing_debug_board_inventory() -> None:
    tab = _VoiceConnectResultTab(mode=SentryV2Comm.MODE_WIFI_DEBUG_USB, connected=False)

    details = {
        "Debug Board": (False, "No COM port specified"),
        "ESP32 WiFi": (False, "WiFi host unreachable"),
    }

    SentryV2TabWidget._on_connection_operation_finished(
        tab,
        "connect",
        False,
        "Debug board failed",
        details,
        "Disconnected",
    )

    assert tab.spoken
    spoken_text = tab.spoken[-1][0]
    assert "Debug Board was not found on any COM port" in spoken_text
    assert "C O M 3" in spoken_text
    assert "C O M 4" in spoken_text
    assert any(state == "failed" for _label, state, _detail in tab.task_updates)


def test_voice_connect_success_reports_actual_debug_board_port() -> None:
    tab = _VoiceConnectResultTab(
        mode=SentryV2Comm.MODE_WIFI_DEBUG_USB,
        connected=True,
        enabled=False,
        deferred_enable=True,
        mode2_wifi_ready=False,
    )
    tab._connection_attempt_context["resolved_debug_port"] = "COM4"

    details = {
        "Debug Board": (True, "COM4 (servo probe inconclusive)"),
        "ESP32 WiFi": (False, "WiFi host unreachable"),
    }

    SentryV2TabWidget._on_connection_operation_finished(
        tab,
        "connect",
        True,
        "",
        details,
        "Debug: COM4 | WiFi: unavailable",
    )

    assert tab.spoken
    spoken_text = tab.spoken[-1][0]
    assert "connected the Debug Board on C O M 4 instead of C O M 8" in spoken_text
    assert "OfficeWiFi" in spoken_text
    assert "Smart Sentry is enabled." in spoken_text
    assert tab._chk_enable.isChecked() is True


def main() -> None:
    test_mode2_failure_reports_missing_debug_board_and_visible_wifi()
    test_mode2_degraded_success_still_reports_visible_wifi_gap()
    test_open_serial_reports_missing_port_inventory()
    test_voice_connect_failure_reports_missing_debug_board_inventory()
    test_voice_connect_success_reports_actual_debug_board_port()
    print("connection diagnostic checks passed")


if __name__ == "__main__":
    main()
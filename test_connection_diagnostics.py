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

    def _voice_spell_com_port(self, text: str) -> str:
        return SentryV2TabWidget._voice_spell_com_port(text)


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

    def _voice_spell_com_port(self, text: str) -> str:
        return SentryV2TabWidget._voice_spell_com_port(text)

    def _voice_connection_failure_response(self, err: str, details) -> str:
        return SentryV2TabWidget._voice_connection_failure_response(self, err, details)

    def _set_connection_status(self, text: str, state: str) -> None:
        self.status_updates.append((str(text), str(state)))

    def _log(self, message: str) -> None:
        self.logs.append(str(message))

    def _update_runtime_diagnostics(self, *, reason: str, force: bool = False) -> None:
        self.logs.append(f"diag:{reason}:{int(bool(force))}")

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


class _CameraFailureTab:
    def __init__(self, *, voice_window_active: bool = True) -> None:
        self._closing = False
        self._camera_open_in_progress = True
        self._startup_retry_count = 3
        self._btn_cam = _FakeButton()
        self._voice_window_active = bool(voice_window_active)
        self.camera_status = []
        self.logs = []
        self.spoken = []

    def _has_local_source(self) -> bool:
        return False

    def _set_camera_status(self, text: str, level: str) -> None:
        self.camera_status.append((str(text), str(level)))

    def _log(self, message: str) -> None:
        self.logs.append(str(message))

    def _voice_interaction_window_active(self) -> bool:
        return self._voice_window_active

    def _speak_after_operator_quiet(self, phrase: str, *, interrupt: bool = False, minimum_quiet_s: float = 0.0) -> bool:
        self.spoken.append((str(phrase), bool(interrupt), float(minimum_quiet_s)))
        return True

    def _voice_spell_com_port(self, text: str) -> str:
        return SentryV2TabWidget._voice_spell_com_port(text)


def test_voice_connection_failure_response_reports_missing_ports_and_wifi() -> None:
    tab = _FakeConnectionTab()
    tab._connection_attempt_context = {
        "preferred_esp32_port": "COM7",
        "preferred_debug_port": "COM8",
        "visible_ports": [("COM3", "USB-SERIAL CH340"), ("COM4", "CP210 USB to UART")],
        "udp_host": "192.168.4.1",
        "udp_port": 9000,
    }

    phrase = SentryV2TabWidget._voice_connection_failure_response(
        tab,
        "Debug board failed",
        {
            "Debug Board": (False, "No COM port specified"),
            "ESP32 WiFi": (False, "WiFi host unreachable"),
        },
    )

    assert "Debug Board was not found on any C O M port" in phrase
    assert "C O M 8" in phrase
    assert "C O M 3" in phrase
    assert "C O M 4" in phrase
    assert "ESP32 WiFi is unavailable at 192.168.4.1:9000" in phrase


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
    assert "Debug Board was not found on any C O M port" in spoken_text
    assert "C O M 3" in spoken_text
    assert "C O M 4" in spoken_text
    assert "ESP32 WiFi is unavailable at 192.168.4.1:9000" in spoken_text
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
    assert "Smart Sentry boards are connected on the C O M link" in spoken_text
    assert "Smart Sentry is enabled." in spoken_text
    assert tab._chk_enable.isChecked() is True


def test_camera_open_failure_reports_unavailable_index_and_voice_feedback() -> None:
    tab = _CameraFailureTab(voice_window_active=True)

    SentryV2TabWidget._on_camera_open_failed(tab, "0")

    assert tab.camera_status
    assert tab.camera_status[-1][0] == "Camera index 0 is unavailable or already in use"
    assert tab.camera_status[-1][1] == "error"
    assert tab.spoken
    assert "Camera source 0 is not available right now." in tab.spoken[-1][0]


def test_camera_open_failure_reports_unavailable_stream() -> None:
    tab = _CameraFailureTab(voice_window_active=False)

    SentryV2TabWidget._on_camera_open_failed(tab, "rtsp://192.168.4.10/live")

    assert tab.camera_status
    assert tab.camera_status[-1][0] == "Camera stream is unavailable: rtsp://192.168.4.10/live"
    assert tab.camera_status[-1][1] == "error"
    assert not tab.spoken


def main() -> None:
    test_voice_connection_failure_response_reports_missing_ports_and_wifi()
    test_open_serial_reports_missing_port_inventory()
    test_voice_connect_failure_reports_missing_debug_board_inventory()
    test_voice_connect_success_reports_actual_debug_board_port()
    test_camera_open_failure_reports_unavailable_index_and_voice_feedback()
    test_camera_open_failure_reports_unavailable_stream()
    print("connection diagnostic checks passed")


if __name__ == "__main__":
    main()
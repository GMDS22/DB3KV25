#!/usr/bin/env python3
"""Focused regression checks for voice conversation recovery paths."""

import sys
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).parent))

import app.sentry_v2.sentry_v2_tab as sentry_v2_tab_mod
from app.sentry_v2.sentry_v2_tab import SentryV2TabWidget


class _TimerCapture:
    def __enter__(self):
        self.calls = []
        self._original = sentry_v2_tab_mod.QTimer.singleShot

        def _capture(delay_ms, callback):
            self.calls.append((int(delay_ms), callback, getattr(callback, "__name__", repr(callback))))

        sentry_v2_tab_mod.QTimer.singleShot = _capture
        return self.calls

    def __exit__(self, exc_type, exc, tb):
        sentry_v2_tab_mod.QTimer.singleShot = self._original


class _FakeButton:
    def __init__(self) -> None:
        self.enabled = True
        self.text = ""

    def setEnabled(self, value: bool) -> None:
        self.enabled = bool(value)

    def setText(self, value: str) -> None:
        self.text = str(value)


class _VoiceRecoveryTab:
    def __init__(self) -> None:
        self.config = SimpleNamespace(sound=SimpleNamespace(human_voice_enabled=True))
        self._voice_protocol_pending_response_token = 0
        self._voice_protocol_pending_connect_confirmation = False
        self._voice_protocol_pending_command_clarification = ""
        self._voice_protocol_pending_command_heard_text = ""
        self._voice_protocol_awaiting_next_action = False
        self._voice_protocol_hold_paused = False
        self._voice_interaction_active_until_s = 5.0
        self._assistant_busy = False
        self._scenario = "idle"
        self.spoken = []
        self.logs = []
        self.task_updates = []
        self.voice_windows = []
        self.followups = []
        self.prompt_delays = []
        self.ai_states = []

    def _arm_voice_pending_response_timeout(self, *, kind: str, heard_text: str, timeout_s: float) -> None:
        return SentryV2TabWidget._arm_voice_pending_response_timeout(self, kind=kind, heard_text=heard_text, timeout_s=timeout_s)

    def _on_voice_protocol_next_action_timeout(self) -> None:
        return SentryV2TabWidget._on_voice_protocol_next_action_timeout(self)

    def _reopen_voice_followup_after_response(self, **kwargs):
        return SentryV2TabWidget._reopen_voice_followup_after_response(self, **kwargs)

    def _clear_voice_connect_confirmation(self) -> None:
        self._voice_protocol_pending_connect_confirmation = False

    def _clear_voice_command_clarification(self) -> None:
        self._voice_protocol_pending_command_clarification = ""
        self._voice_protocol_pending_command_heard_text = ""

    def _set_operator_task_status(self, label: str, state: str, detail: str = "") -> None:
        self.task_updates.append((str(label), str(state), str(detail)))

    def _set_voice_protocol_scenario(self, scenario: str) -> None:
        self._scenario = str(scenario)

    def _start_voice_interaction_window(self, *, reason: str, hold_s: float = 10.0) -> None:
        self.voice_windows.append((str(reason), float(hold_s)))

    def _voice_operator_silence_delay_s(self, *, minimum_quiet_s: float = 0.0, now=None) -> float:
        return max(0.2, float(minimum_quiet_s or 0.0))

    def _speak_after_operator_quiet(self, text: str, *, interrupt: bool = False, assistant_output: bool = False, minimum_quiet_s: float = 0.0, _response_delay_applied: bool = False) -> bool:
        self.spoken.append((str(text), bool(interrupt), float(minimum_quiet_s)))
        return True

    def _estimate_human_phrase_duration_s(self, phrase: str) -> float:
        return 0.6

    def _prime_voice_listener_followup_window(self, *, reason: str, hold_s: float, delay_s: float = 0.0) -> None:
        self.followups.append((str(reason), float(hold_s), float(delay_s)))

    def _schedule_voice_next_action_prompt(self, *, delay_s: float) -> None:
        self.prompt_delays.append(float(delay_s))

    def _log(self, message: str) -> None:
        self.logs.append(str(message))

    def _human_voice_busy(self) -> bool:
        return False

    def _human_voice_supported(self) -> bool:
        return True

    def _voice_auto_resume_tracking_enabled(self) -> bool:
        return False

    def _on_ai_state_update(self, state: str) -> None:
        self.ai_states.append(str(state))


class _BusyVoiceConnectionTab(_VoiceRecoveryTab):
    def __init__(self, *, connection_task_label: str, enable_requested: bool = False, connected: bool = False) -> None:
        super().__init__()
        self._connection_busy = True
        self._connection_task_label = str(connection_task_label)
        self._deferred_enable_sentry_after_connect = bool(enable_requested)
        self._voice_protocol_connect_via_voice_active = False
        self._voice_protocol_disconnect_via_voice_active = False
        self._comm = SimpleNamespace(is_connected=lambda: bool(connected))
        self._chk_enable = SimpleNamespace(isChecked=lambda: False)
        self.enable_clear_calls = 0

    def _execute_voice_connect_request(self) -> str:
        return SentryV2TabWidget._execute_voice_connect_request(self)

    def _execute_voice_disconnect_request(self) -> str:
        return SentryV2TabWidget._execute_voice_disconnect_request(self)

    def _host_controls_hardware(self) -> bool:
        return False

    def _clear_enable_sentry_after_connect(self) -> None:
        self.enable_clear_calls += 1
        self._deferred_enable_sentry_after_connect = False


class _DisconnectCompletionTab:
    def __init__(self) -> None:
        self._connection_busy = True
        self._connection_task_label = "disconnecting Smart Sentry boards"
        self._closing = False
        self._btn_connect = _FakeButton()
        self._voice_protocol_connect_via_voice_active = False
        self._voice_protocol_disconnect_via_voice_active = True
        self._connection_cancel_requested = False
        self._startup_autoconnect_active = False
        self._startup_autoconnect_retry = 0
        self.spoken = []
        self.logs = []
        self.task_updates = []
        self.prompt_delays = []
        self.voice_windows = []
        self.status_updates = []

    def _set_connection_status(self, text: str, state: str) -> None:
        self.status_updates.append((str(text), str(state)))

    def _log(self, message: str) -> None:
        self.logs.append(str(message))

    def _sync_home_screen_visibility(self) -> None:
        return None

    def _clear_enable_sentry_after_connect(self) -> None:
        return None

    def _set_operator_task_status(self, label: str, state: str, detail: str = "") -> None:
        self.task_updates.append((str(label), str(state), str(detail)))

    def _start_voice_interaction_window(self, *, reason: str, hold_s: float = 10.0) -> None:
        self.voice_windows.append((str(reason), float(hold_s)))

    def _speak_human_phrase(self, phrase: str, *, interrupt: bool = True) -> bool:
        self.spoken.append((str(phrase), bool(interrupt)))
        return True

    def _estimate_human_phrase_duration_s(self, phrase: str) -> float:
        return 0.6

    def _schedule_voice_next_action_prompt(self, *, delay_s: float) -> None:
        self.prompt_delays.append(float(delay_s))


def test_connect_confirmation_timeout_reopens_followup_window() -> None:
    tab = _VoiceRecoveryTab()
    tab._voice_protocol_pending_connect_confirmation = True

    with _TimerCapture() as timer_calls:
        tab._arm_voice_pending_response_timeout(
            kind="connect_confirmation",
            heard_text="connect Smart Sentry boards",
            timeout_s=12.0,
        )

    assert timer_calls
    _delay_ms, callback, _name = timer_calls[0]
    callback()

    assert tab.spoken
    assert "No confirmation received. I did not connect the Smart Sentry boards." in tab.spoken[-1][0]
    assert tab.voice_windows[-1][0] == "connect_confirmation-timeout"
    assert tab.followups[-1][0] == "connect_confirmation-timeout"
    assert tab.prompt_delays
    assert tab._voice_protocol_pending_connect_confirmation is False


def test_next_action_timeout_announces_guarding_continues() -> None:
    tab = _VoiceRecoveryTab()
    tab._voice_protocol_awaiting_next_action = True

    tab._on_voice_protocol_next_action_timeout()

    assert tab.spoken
    assert "Guarding continues." in tab.spoken[-1][0]
    assert tab._voice_protocol_awaiting_next_action is False
    assert tab._scenario == "idle"


def test_connect_request_while_disconnecting_gives_actionable_retry_message() -> None:
    tab = _BusyVoiceConnectionTab(connection_task_label="disconnecting Smart Sentry boards", enable_requested=True)

    result = tab._execute_voice_connect_request()

    assert result == "acknowledged"
    assert tab.spoken
    assert "Tell me to connect Smart Sentry again when that finishes." in tab.spoken[-1][0]
    assert tab.prompt_delays
    assert tab.enable_clear_calls == 1


def test_disconnect_request_while_connecting_does_not_promise_impossible_disconnect() -> None:
    tab = _BusyVoiceConnectionTab(connection_task_label="connecting Smart Sentry boards")

    result = tab._execute_voice_disconnect_request()

    assert result == "acknowledged"
    assert tab.spoken
    assert "Tell me to disconnect after it finishes" in tab.spoken[-1][0]
    assert tab.prompt_delays
    assert tab._voice_protocol_disconnect_via_voice_active is False


def test_disconnect_completion_reports_ready_for_next_command() -> None:
    tab = _DisconnectCompletionTab()

    SentryV2TabWidget._on_connection_operation_finished(
        tab,
        "disconnect",
        True,
        "",
        {},
        "Disconnected",
    )

    assert tab.spoken
    assert "Smart Sentry boards are disconnected." in tab.spoken[-1][0]
    assert "Ask another question or give another command when ready." in tab.spoken[-1][0]
    assert tab.prompt_delays
    assert tab.voice_windows[-1][0] == "disconnect-complete"


def main() -> None:
    test_connect_confirmation_timeout_reopens_followup_window()
    test_next_action_timeout_announces_guarding_continues()
    test_connect_request_while_disconnecting_gives_actionable_retry_message()
    test_disconnect_request_while_connecting_does_not_promise_impossible_disconnect()
    test_disconnect_completion_reports_ready_for_next_command()
    print("voice protocol recovery checks passed")


if __name__ == "__main__":
    main()
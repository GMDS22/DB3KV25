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

    def _update_runtime_diagnostics(self, *, reason: str = "", force: bool = False) -> None:
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


class _VoiceRecoveryStatusTab:
    def __init__(self) -> None:
        self._voice_heard_status_text = "idle"
        self._voice_runtime_recovery_attempts = 0
        self._voice_runtime_recovery_max_attempts = 4
        self._voice_runtime_recovery_token = 0
        self._voice_last_command_confidence = -1.0
        self._voice_heard_partial_text = ""
        self._voice_last_partial_before_final_text = ""
        self._voice_heard_final_text = ""
        self._voice_transcript_history = []
        self._voice_transcript_history_limit = 20
        self._voice_runtime_diag_log = []
        self._voice_runtime_diag_log_limit = 60
        self._closing = False
        self.logs = []
        self.runtime_diag_updates = []
        self.scheduled_recovery = []
        self.cleared_recovery = []

    def _append_voice_runtime_diag_log(self, message: str) -> None:
        text = str(message or "")
        self._voice_runtime_diag_log.append(text)

    def _append_voice_transcript_entry(self, **kwargs) -> None:
        self._voice_transcript_history.append(kwargs)

    def _update_runtime_diagnostics(self, *, reason: str = "", force: bool = False) -> None:
        self.runtime_diag_updates.append((str(reason), bool(force)))

    def _schedule_voice_runtime_recovery(self, *, reason: str, delay_s: float) -> None:
        self.scheduled_recovery.append((str(reason), float(delay_s)))

    def _reset_voice_runtime_recovery(self, *, reason: str) -> None:
        self.cleared_recovery.append(str(reason))

    def _log(self, message: str) -> None:
        self.logs.append(str(message))

    def _on_voice_transcript_event(self, payload: object) -> None:
        return SentryV2TabWidget._on_voice_transcript_event(self, payload)


class _DeferredEnablePauseResetTab:
    def __init__(self) -> None:
        self._deferred_enable_sentry_after_connect = False
        self._deferred_enable_sentry_reason = ""
        self._voice_protocol_hold_paused = True
        self._voice_interaction_engine_paused = True

    def _arm_enable_sentry_after_connect(self, reason: str = "") -> None:
        return SentryV2TabWidget._arm_enable_sentry_after_connect(self, reason=reason)


class _VoiceVerificationTab:
    def __init__(self) -> None:
        self.config = SimpleNamespace(
            sound=SimpleNamespace(
                voice_operator_allow_pin_fallback=False,
                voice_operator_pin_max_attempts=3,
                voice_operator_pin_lockout_s=45.0,
            )
        )
        self._voice_operator_pending_command = ""
        self._voice_operator_pending_reason = "control-command"
        self._voice_operator_pending_started_s = 0.0
        self._voice_operator_verification_lockout_until_s = 0.0
        self._voice_operator_verification_attempts = 0
        self._voice_operator_verification_until_s = 0.0
        self.spoken = []
        self.intake_windows = []
        self.verified_started = 0
        self.finalized = 0

    def _voice_operator_try_consume_verification_input(self, command: str) -> bool:
        return SentryV2TabWidget._voice_operator_try_consume_verification_input(self, command)

    def _voice_operator_reset_pending_verification(self) -> None:
        return SentryV2TabWidget._voice_operator_reset_pending_verification(self)

    def _voice_operator_verification_lockout_active(self) -> bool:
        return False

    def _voice_operator_pin_configured(self) -> bool:
        return False

    def _voice_control_request_requires_operator(self, text: str) -> bool:
        normalized = str(text or "").strip().lower()
        return any(token in normalized for token in ("close", "restart", "shutdown", "stop app"))

    def _voice_operator_start_verified_session(self) -> None:
        self.verified_started += 1
        self._voice_operator_verification_until_s = 9999999999.0

    def _voice_operator_finalize_verified_pending_command(self) -> None:
        self.finalized += 1
        self._voice_operator_pending_command = ""

    def _extract_voice_operator_pin_candidate(self, command: str) -> str:
        return ""

    def _verify_voice_operator_pin(self, pin_code: str) -> bool:
        return False

    def _speak_after_operator_quiet(self, text: str, *, interrupt: bool = False, assistant_output: bool = False, minimum_quiet_s: float = 0.0, _response_delay_applied: bool = False) -> bool:
        self.spoken.append(str(text))
        return True

    def _open_voice_conversation_intake(self, *, source: str, hold_s: float, intake_phrase: str) -> None:
        self.intake_windows.append((str(source), float(hold_s), str(intake_phrase)))


class _WindowCloseProbe:
    def __init__(self) -> None:
        self.closed = 0

    def close(self) -> None:
        self.closed += 1


class _ClosePathTab:
    def __init__(self) -> None:
        self.window_probe = _WindowCloseProbe()
        self.self_closed = 0

    def _request_full_application_close(self) -> None:
        return SentryV2TabWidget._request_full_application_close(self)

    def window(self):
        return self.window_probe

    def isWindow(self) -> bool:
        return False

    def close(self) -> None:
        self.self_closed += 1


class _FakeCombo:
    def __init__(self, labels):
        self._labels = [str(label) for label in labels]

    def count(self):
        return len(self._labels)

    def itemText(self, index):
        return self._labels[index]


class _VoiceProfileResolveTab:
    def __init__(self) -> None:
        self._combo_master_profile = _FakeCombo(
            [
                "Smart Sentry Speed 1",
                "Smart Sentry Speed 2",
                "Smart Sentry Speed 3",
                "Smart Sentry Speed 4",
            ]
        )

    def _normalize_explicit_voice_command(self, command: str) -> str:
        return SentryV2TabWidget._normalize_explicit_voice_command(self, command)

    def _normalize_voice_profile_lookup_text(self, text: str) -> str:
        return SentryV2TabWidget._normalize_voice_profile_lookup_text(self, text)

    def _extract_voice_master_profile_request(self, command: str) -> str:
        return SentryV2TabWidget._extract_voice_master_profile_request(self, command)

    def _resolve_voice_master_profile_index(self, requested_name: str) -> int:
        return SentryV2TabWidget._resolve_voice_master_profile_index(self, requested_name)

    def _assistant_cue_name(self) -> str:
        return "elion"


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


def test_voice_status_mic_error_schedules_recovery() -> None:
    tab = _VoiceRecoveryStatusTab()

    tab._on_voice_transcript_event({"kind": "status", "text": "mic_error", "source": "watchdog"})

    assert tab.scheduled_recovery
    reason, delay_s = tab.scheduled_recovery[-1]
    assert reason == "mic_error"
    assert delay_s >= 1.5
    assert not tab.cleared_recovery


def test_voice_status_listening_clears_recovery_attempts() -> None:
    tab = _VoiceRecoveryStatusTab()
    tab._voice_runtime_recovery_attempts = 2

    tab._on_voice_transcript_event({"kind": "status", "text": "listening", "source": "vosk"})

    assert tab.cleared_recovery
    assert tab.cleared_recovery[-1] == "listening"


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


def test_arm_enable_after_connect_clears_hold_pause() -> None:
    tab = _DeferredEnablePauseResetTab()

    tab._arm_enable_sentry_after_connect(reason="voice command: run the smart sentry")

    assert tab._deferred_enable_sentry_after_connect is True
    assert tab._deferred_enable_sentry_reason == "voice command: run the smart sentry"
    assert tab._voice_protocol_hold_paused is False
    assert tab._voice_interaction_engine_paused is False


def test_verification_face_repeat_accepts_same_command_without_pin() -> None:
    tab = _VoiceVerificationTab()
    import app.sentry_v2.sentry_v2_tab as sentry_v2_tab_mod

    tab._voice_operator_pending_command = "close app"
    tab._voice_operator_pending_started_s = float(sentry_v2_tab_mod.time.time())

    consumed = tab._voice_operator_try_consume_verification_input("close app")

    assert consumed is True
    assert tab.verified_started == 1
    assert tab.finalized == 1
    assert tab._voice_operator_pending_command == ""


def test_verification_pending_expires_and_stops_swallowing_commands() -> None:
    tab = _VoiceVerificationTab()
    tab._voice_operator_pending_command = "restart smart sentry app"
    tab._voice_operator_pending_started_s = 1.0

    # Force staleness by making current time effectively far ahead.
    import app.sentry_v2.sentry_v2_tab as sentry_v2_tab_mod

    original_time = sentry_v2_tab_mod.time.time
    sentry_v2_tab_mod.time.time = lambda: 100.0
    try:
        consumed = tab._voice_operator_try_consume_verification_input("restart smart sentry app")
    finally:
        sentry_v2_tab_mod.time.time = original_time

    assert consumed is False
    assert tab._voice_operator_pending_command == ""


def test_request_full_application_close_targets_parent_window() -> None:
    tab = _ClosePathTab()

    tab._request_full_application_close()

    assert tab.window_probe.closed == 1
    assert tab.self_closed == 0


def test_profile_request_resolution_handles_change_profile_phrase() -> None:
    tab = _VoiceProfileResolveTab()

    requested = tab._extract_voice_master_profile_request("elion change the profile to smart sentry speed four")
    resolved_index = tab._resolve_voice_master_profile_index(requested)

    assert requested == "smart sentry speed four"
    assert resolved_index == 3


def main() -> None:
    test_connect_confirmation_timeout_reopens_followup_window()
    test_next_action_timeout_announces_guarding_continues()
    test_connect_request_while_disconnecting_gives_actionable_retry_message()
    test_disconnect_request_while_connecting_does_not_promise_impossible_disconnect()
    test_disconnect_completion_reports_ready_for_next_command()
    test_arm_enable_after_connect_clears_hold_pause()
    test_verification_face_repeat_accepts_same_command_without_pin()
    test_verification_pending_expires_and_stops_swallowing_commands()
    test_request_full_application_close_targets_parent_window()
    test_profile_request_resolution_handles_change_profile_phrase()
    print("voice protocol recovery checks passed")


if __name__ == "__main__":
    main()
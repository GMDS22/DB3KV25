#!/usr/bin/env python3
"""Focused regression checks for low-latency voice confirmation scheduling."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import app.sentry_v2.sentry_v2_tab as sentry_v2_tab_mod
from app.sentry_v2.sentry_v2_tab import SentryV2TabWidget


class _TimerCapture:
    def __enter__(self):
        self.calls: list[int] = []
        self._original = sentry_v2_tab_mod.QTimer.singleShot

        def _capture(delay_ms, callback):
            self.calls.append(int(delay_ms))

        sentry_v2_tab_mod.QTimer.singleShot = _capture
        return self.calls

    def __exit__(self, exc_type, exc, tb):
        sentry_v2_tab_mod.QTimer.singleShot = self._original


class _FakeConfirmTab:
    def __init__(self) -> None:
        self.spoken: list[str] = []
        self.actions: list[str] = []
        self.logs: list[str] = []

    def _voice_shutdown_blocked(self):
        return False

    def _prepare_human_speech_text(self, text: str, assistant_output: bool = False):
        return " ".join(str(text or "").split()).strip()

    def _spoken_sentence(self, text: str, assistant_output: bool = False):
        return self._prepare_human_speech_text(text, assistant_output=assistant_output)

    def _voice_operator_silence_delay_s(self, *, now=None, minimum_quiet_s: float = 0.0):
        return 0.0

    def _voice_response_delay_s(self):
        return 0.0

    def _estimate_human_phrase_duration_s(self, text: str):
        return 1.1

    def _voice_confirmation_action_lead_s(self, text: str):
        return SentryV2TabWidget._voice_confirmation_action_lead_s(self, text)

    def _speak_after_operator_quiet(
        self,
        text: str,
        *,
        interrupt: bool = False,
        assistant_output: bool = False,
        minimum_quiet_s: float = 0.0,
        _response_delay_applied: bool = False,
    ):
        self.spoken.append(str(text or ""))
        return True

    def _log(self, message: str):
        self.logs.append(str(message))


class _FakeClarifyTab:
    def _voice_command_starts_with_phrase(self, command: str, phrases):
        normalized = " ".join(str(command or "").split()).strip().lower()
        for phrase in phrases:
            token = " ".join(str(phrase or "").split()).strip().lower()
            if token and (normalized == token or normalized.startswith(f"{token} ")):
                return True
        return False

    def _voice_command_contains_phrase(self, command: str, phrases):
        normalized = " ".join(str(command or "").split()).strip().lower()
        for phrase in phrases:
            token = " ".join(str(phrase or "").split()).strip().lower()
            if token and token in normalized:
                return True
        return False

    def _voice_command_requests_connect_and_enable(self, command: str):
        return SentryV2TabWidget._voice_command_requests_connect_and_enable(self, command)

    def _voice_command_should_bypass_clarification(self, command: str):
        return SentryV2TabWidget._voice_command_should_bypass_clarification(self, command)

    def _voice_command_is_cue_only(self, command: str):
        return False

    def _voice_command_confidence(self):
        return 0.55

    def _voice_command_confidence_threshold(self):
        return 0.78

    def _voice_command_looks_actionable(self, command: str):
        return True

    def _voice_command_is_ambiguous(self, command: str):
        return False

    def _voice_command_ambiguous_threshold(self):
        return 0.92


def test_confirmation_action_uses_short_lead_in() -> None:
    tab = _FakeConfirmTab()

    with _TimerCapture() as timer_calls:
        result = SentryV2TabWidget._run_voice_action_after_confirmation(
            tab,
            "Connecting Smart Sentry boards now.",
            lambda: tab.actions.append("ran"),
            action_label="connect",
        )

    assert result is True
    assert tab.spoken == ["Connecting Smart Sentry boards now."]
    assert tab.actions == []
    assert timer_calls
    assert min(timer_calls) <= 320


def test_run_action_immediately_still_speaks_before_scheduling_action() -> None:
    tab = _FakeConfirmTab()

    with _TimerCapture() as timer_calls:
        result = SentryV2TabWidget._run_voice_action_after_confirmation(
            tab,
            "Disconnecting Smart Sentry boards now.",
            lambda: tab.actions.append("ran"),
            action_label="disconnect",
            run_action_immediately=True,
        )

    assert result is True
    assert tab.spoken == ["Disconnecting Smart Sentry boards now."]
    assert tab.actions == []
    assert timer_calls
    assert min(timer_calls) <= 140


def test_connect_and_enable_command_skips_low_confidence_clarification() -> None:
    tab = _FakeClarifyTab()

    assert (
        SentryV2TabWidget._voice_command_should_request_clarification(
            tab,
            "connect boards and enable smart sentry",
        )
        is False
    )


def main() -> None:
    test_confirmation_action_uses_short_lead_in()
    test_run_action_immediately_still_speaks_before_scheduling_action()
    test_connect_and_enable_command_skips_low_confidence_clarification()
    print("voice confirmation timing checks passed")


if __name__ == "__main__":
    main()
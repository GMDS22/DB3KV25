#!/usr/bin/env python3
"""Regression checks for voice-driven app close/restart commands."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from app.sentry_v2.sentry_v2_tab import SentryV2TabWidget


class _LifecycleVoiceTab:
    def __init__(self) -> None:
        self._shutdown_in_progress = False
        self._cleanup_started = False
        self.actions = []
        self.spoken = []

    def _consume_voice_connect_confirmation(self, _cmd: str):
        return None

    def _run_voice_action_after_confirmation(
        self,
        phrase: str,
        callback,
        *,
        interrupt: bool,
        action_label: str,
        wait_for_speech_completion: bool,
    ) -> None:
        self.actions.append(
            {
                "phrase": str(phrase),
                "callback": callback,
                "interrupt": bool(interrupt),
                "action_label": str(action_label),
                "wait_for_speech_completion": bool(wait_for_speech_completion),
            }
        )

    def _speak_after_operator_quiet(self, text: str, *, interrupt: bool = False) -> bool:
        self.spoken.append((str(text), bool(interrupt)))
        return True

    def _voice_pick_phrase(self, _key: str, variants):
        options = [str(item) for item in list(variants or []) if str(item or "").strip()]
        return options[0] if options else ""

    def _voice_command_requests_connect_and_enable(self, _command: str) -> bool:
        return False

    def _normalize_explicit_voice_command(self, command: str) -> str:
        return " ".join(str(command or "").strip().lower().split())

    def _voice_command_starts_with_phrase(self, command: str, phrases) -> bool:
        return SentryV2TabWidget._voice_command_starts_with_phrase(self, command, phrases)

    def begin_graceful_shutdown(self, on_complete=None) -> None:
        self.actions.append({"shutdown_called": True, "on_complete": on_complete})

    def close(self) -> None:
        self.actions.append({"close_called": True})

    def _restart_application(self) -> None:
        self.actions.append({"restart_called": True})


def test_close_the_smart_sentry_app_phrase_routes_to_close_action() -> None:
    tab = _LifecycleVoiceTab()

    result = SentryV2TabWidget._handle_voice_protocol_command(tab, "close the smart sentry app")

    assert result == "acknowledged"
    assert tab.actions
    assert tab.actions[-1]["action_label"] == "close-app"


def test_restart_the_smart_sentry_app_phrase_routes_to_restart_action() -> None:
    tab = _LifecycleVoiceTab()

    result = SentryV2TabWidget._handle_voice_protocol_command(tab, "restart the smart sentry app")

    assert result == "acknowledged"
    assert tab.actions
    assert tab.actions[-1]["action_label"] == "restart-app"


def test_app_lifecycle_commands_bypass_low_confidence_clarification() -> None:
    tab = _LifecycleVoiceTab()

    assert SentryV2TabWidget._voice_command_should_bypass_clarification(tab, "close the smart sentry app")
    assert SentryV2TabWidget._voice_command_should_bypass_clarification(tab, "restart the smart sentry app")


def main() -> None:
    test_close_the_smart_sentry_app_phrase_routes_to_close_action()
    test_restart_the_smart_sentry_app_phrase_routes_to_restart_action()
    test_app_lifecycle_commands_bypass_low_confidence_clarification()
    print("voice app lifecycle command checks passed")


if __name__ == "__main__":
    main()

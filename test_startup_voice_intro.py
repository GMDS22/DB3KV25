#!/usr/bin/env python3
"""Focused regression checks for startup voice intro behavior."""

import sys
import time
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).parent))

import app.sentry_v2.sentry_v2_tab as sentry_v2_tab_mod
from app.sentry_v2.sentry_v2_tab import SentryV2TabWidget


class _TimerCapture:
    def __enter__(self):
        self.calls: list[tuple[int, str]] = []
        self._original = sentry_v2_tab_mod.QTimer.singleShot

        def _capture(delay_ms, callback):
            self.calls.append((int(delay_ms), getattr(callback, "__name__", repr(callback))))

        sentry_v2_tab_mod.QTimer.singleShot = _capture
        return self.calls

    def __exit__(self, exc_type, exc, tb):
        sentry_v2_tab_mod.QTimer.singleShot = self._original


class _FakeStartupTab:
    def __init__(self, *, direct_ok: bool = True, fallback_ok: bool = True, human_voice_supported: bool = True, has_local_source: bool = True):
        self.config = SimpleNamespace(
            sound=SimpleNamespace(human_voice_enabled=True),
            quick_startup_enabled=True,
        )
        self._assistant_busy = False
        self._startup_voice_intro_announced = False
        self._startup_voice_intro_pending = True
        self._startup_voice_intro_scheduled_at_s = time.time()
        self._human_voice_supported_value = bool(human_voice_supported)
        self._has_local_source_value = bool(has_local_source)
        self._direct_ok = bool(direct_ok)
        self._fallback_ok = bool(fallback_ok)
        self.logs: list[str] = []
        self.spoken: list[tuple[str, str, bool]] = []
        self.yolo_delay = 0

    def _announce_startup_voice_intro(self):
        return SentryV2TabWidget._announce_startup_voice_intro(self)

    def _schedule_startup_tasks(self):
        return SentryV2TabWidget._schedule_startup_tasks(self)

    def _refresh_operator_listening_state(self):
        return None

    def _voice_shutdown_blocked(self):
        return False

    def isVisible(self):
        return True

    def _has_local_source(self):
        return self._has_local_source_value

    def _human_voice_supported(self):
        return self._human_voice_supported_value

    def _refresh_ai_provider_status(self):
        self.logs.append("provider-refreshed")

    def _speak_human_phrase(self, phrase: str, *, interrupt: bool = True):
        self.spoken.append(("direct", phrase, bool(interrupt)))
        return self._direct_ok

    def _speak_after_operator_quiet(self, phrase: str, *, interrupt: bool = False, assistant_output: bool = False, minimum_quiet_s: float = 0.0, _response_delay_applied: bool = False):
        self.spoken.append(("fallback", phrase, bool(interrupt)))
        return self._fallback_ok

    def _log(self, message: str):
        self.logs.append(str(message))

    def _schedule_auto_yolo_load(self, delay_ms: int):
        self.yolo_delay = int(delay_ms)

    def _auto_open_camera_on_startup(self):
        raise AssertionError("timer callback should not execute during startup intro tests")

    def _schedule_startup_rest_move(self):
        raise AssertionError("timer callback should not execute during startup intro tests")

    def _stop_human_speech(self):
        self.logs.append("speech-stopped")

    def _human_voice_busy(self):
        return False

    def _on_ai_state_update(self, state: str):
        self.logs.append(f"ai-state:{state}")

    def _suspend_system_reporting_speech(self, *, reason: str = ""):
        if reason:
            self.logs.append(f"system-reporting-suspended:{reason}")


def test_startup_intro_does_not_wait_for_camera_source_ready() -> None:
    tab = _FakeStartupTab(direct_ok=True, fallback_ok=True, has_local_source=False)

    with _TimerCapture() as timer_calls:
        tab._announce_startup_voice_intro()

    assert tab._startup_voice_intro_announced is True
    assert tab._startup_voice_intro_pending is False
    assert any(mode == "fallback" for mode, _phrase, _interrupt in tab.spoken)
    assert not any(delay_ms == 250 and callback_name == "_announce_startup_voice_intro" for delay_ms, callback_name in timer_calls)


def test_startup_intro_speaks_after_camera_source_is_ready() -> None:
    tab = _FakeStartupTab(direct_ok=True, fallback_ok=True, has_local_source=True)

    with _TimerCapture() as timer_calls:
        tab._announce_startup_voice_intro()

    assert tab._startup_voice_intro_announced is True
    assert tab._startup_voice_intro_pending is False
    assert any(mode == "fallback" for mode, _phrase, _interrupt in tab.spoken)
    assert not any(delay_ms == 400 for delay_ms, _name in timer_calls)


def test_startup_intro_retries_when_speech_backend_is_not_ready() -> None:
    tab = _FakeStartupTab(direct_ok=False, fallback_ok=False, has_local_source=True)

    with _TimerCapture() as timer_calls:
        tab._announce_startup_voice_intro()

    assert tab._startup_voice_intro_announced is True
    assert tab._startup_voice_intro_pending is False
    assert not any(delay_ms == 500 for delay_ms, _name in timer_calls)


def test_operator_listening_state_does_not_cancel_pending_startup_intro() -> None:
    tab = _FakeStartupTab(direct_ok=True, fallback_ok=False)

    tab._refresh_operator_listening_state()

    assert tab._startup_voice_intro_pending is True
    assert not any("startup greeting suppressed" in message for message in tab.logs)


def test_schedule_startup_tasks_arms_intro_and_schedules_announce() -> None:
    tab = _FakeStartupTab(direct_ok=True, fallback_ok=False)

    with _TimerCapture() as timer_calls:
        tab._schedule_startup_tasks()

    assert tab._startup_voice_intro_pending is True
    assert any(delay_ms == 1500 and callback_name == "_announce_startup_voice_intro" for delay_ms, callback_name in timer_calls)
    assert any(delay_ms == 800 and callback_name == "_auto_open_camera_on_startup" for delay_ms, callback_name in timer_calls)
    assert tab.yolo_delay == 2500


def main() -> None:
    test_startup_intro_does_not_wait_for_camera_source_ready()
    test_startup_intro_speaks_after_camera_source_is_ready()
    test_startup_intro_retries_when_speech_backend_is_not_ready()
    test_operator_listening_state_does_not_cancel_pending_startup_intro()
    test_schedule_startup_tasks_arms_intro_and_schedules_announce()
    print("startup voice intro checks passed")


if __name__ == "__main__":
    main()
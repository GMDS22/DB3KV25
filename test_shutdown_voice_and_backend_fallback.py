#!/usr/bin/env python3
"""Focused regression checks for shutdown speech and runtime voice fallback behavior."""

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


class _RuntimeStub:
    def __init__(self, *, active_backend: str, neural_tts_ready: bool, speak_result: bool):
        self._active_speech_backend = active_backend
        self.neural_tts_ready = bool(neural_tts_ready)
        self._speak_result = bool(speak_result)
        self.dynamic_calls = []

    def register_output_echo_suppression(self, text: str):
        return None

    def speak_dynamic(self, text: str) -> bool:
        self.dynamic_calls.append(text)
        return self._speak_result


class _ShutdownSpeechTab:
    def __init__(self):
        self._shutdown_in_progress = True
        self._shutdown_voice_sequence_active = False
        self._cleanup_started = False
        self._closing = False
        self.spoken = []
        self.voice_blocked_during_speak = None

    def _voice_shutdown_blocked(self):
        return SentryV2TabWidget._voice_shutdown_blocked(self)

    def _speak_shutdown_closing_sequence(self, on_finished):
        return SentryV2TabWidget._speak_shutdown_closing_sequence(self, on_finished)

    def _stop_human_speech(self):
        return None

    def _speak_human_phrase(self, phrase: str, *, interrupt: bool = True):
        self.voice_blocked_during_speak = self._voice_shutdown_blocked()
        self.spoken.append((phrase, bool(interrupt)))
        return True

    def _estimate_human_phrase_duration_s(self, phrase: str) -> float:
        return 0.4


class _SpeechFallbackTab:
    def __init__(self, runtime: _RuntimeStub):
        self.config = SimpleNamespace(sound=SimpleNamespace(human_voice_enabled=True))
        self._voice_runtime = runtime
        self._speech_available = True
        self._speech_engine = object()
        self._speech_state_label = "ready"
        self._kokoro_busy_until_s = 0.0
        self.local_qt_utterances = []
        self.logs = []

    def _voice_shutdown_blocked(self):
        return False

    def _prepare_human_speech_text(self, text: str, assistant_output: bool = False):
        return str(text or "").strip()

    def _apply_live_human_voice_volume(self):
        return None

    def _human_voice_supported(self):
        return True

    def _selected_human_voice_backend(self, voice_name: str = "") -> str:
        return "kokoro"

    def _allow_local_qt_speech_fallback(self, *, selected_backend: str):
        return SentryV2TabWidget._allow_local_qt_speech_fallback(self, selected_backend=selected_backend)

    def _sync_human_speech_engine(self):
        return None

    def _issue_human_speech(self, cleaned: str):
        self.local_qt_utterances.append(cleaned)
        return True

    def _set_human_voice_runtime_state(self, label: str):
        self._speech_state_label = str(label)

    def _report_runtime_warning(self, title: str, exc: Exception):
        raise AssertionError(f"unexpected runtime warning: {title}: {exc}")

    def _log(self, message: str):
        self.logs.append(str(message))

    def _kokoro_speed_value(self) -> float:
        return 1.0

    def _human_voice_busy(self) -> bool:
        return False


class _VoiceSelectionTab:
    def __init__(self):
        self.config = SimpleNamespace(
            sound=SimpleNamespace(
                human_voice_name="",
                kokoro_voice_name="",
                kokoro_voice_profile="female_us",
                kokoro_voice_female_us="bf_isabella",
                kokoro_voice_male_us="am_michael",
                kokoro_voice_female_uk="bf_emma",
                kokoro_voice_male_uk="bm_george",
            )
        )
        self._speech_available = True
        self._speech_engine = object()
        self._speech_voice_names = ["Microsoft Zira Desktop"]

    def _available_local_qt_voice_names(self):
        return ["Microsoft Zira Desktop"]

    def _available_kokoro_voice_names(self):
        return ["bf_isabella", "am_michael", "bf_emma", "bm_george"]

    def _available_neural_voice_names(self):
        return []

    def _is_local_qt_voice_name(self, voice_name: str) -> bool:
        return str(voice_name or "").strip().lower() == "microsoft zira desktop"

    def _is_kokoro_voice_name(self, voice_name: str) -> bool:
        return str(voice_name or "").strip().lower() in {"bf_isabella", "am_michael", "bf_emma", "bm_george"}

    def _is_neural_voice_name(self, voice_name: str) -> bool:
        return False

    def _preferred_local_qt_voice_name(self) -> str:
        return SentryV2TabWidget._preferred_local_qt_voice_name(self)

    def _prefer_local_qt_human_voice(self, voice_name: str = "") -> bool:
        return SentryV2TabWidget._prefer_local_qt_human_voice(self, voice_name)

    def _human_voice_name(self) -> str:
        return SentryV2TabWidget._human_voice_name(self)

    def _selected_human_voice_backend(self, voice_name: str = "") -> str:
        return SentryV2TabWidget._selected_human_voice_backend(self, voice_name)


def test_shutdown_sequence_can_speak_while_shutdown_is_in_progress() -> None:
    tab = _ShutdownSpeechTab()

    with _TimerCapture() as timer_calls:
        tab._speak_shutdown_closing_sequence(lambda: tab.spoken.append(("finished", False)))

    assert tab.spoken
    assert tab.voice_blocked_during_speak is False
    assert tab._shutdown_voice_sequence_active is True
    assert timer_calls
    _delay_ms, callback, _name = timer_calls[0]
    callback()
    assert tab._shutdown_voice_sequence_active is False


def test_runtime_backend_failure_does_not_fall_back_to_local_qt_when_backend_is_active() -> None:
    runtime = _RuntimeStub(active_backend="kokoro", neural_tts_ready=True, speak_result=False)
    tab = _SpeechFallbackTab(runtime)

    spoken = SentryV2TabWidget._speak_human_phrase(tab, "Smart Sentry response", interrupt=False)

    assert spoken is False
    assert runtime.dynamic_calls == ["Smart Sentry response"]
    assert tab.local_qt_utterances == []
    assert any("fallback suppressed" in message.lower() for message in tab.logs)


def test_runtime_unavailable_allows_local_qt_fallback() -> None:
    runtime = _RuntimeStub(active_backend="unavailable", neural_tts_ready=False, speak_result=False)
    tab = _SpeechFallbackTab(runtime)

    spoken = SentryV2TabWidget._speak_human_phrase(tab, "Smart Sentry response", interrupt=False)

    assert spoken is True
    assert tab.local_qt_utterances == ["Smart Sentry response"]
    assert any("fallback used" in message.lower() for message in tab.logs)


def test_blank_voice_name_keeps_kokoro_profile_instead_of_defaulting_to_local_qt() -> None:
    tab = _VoiceSelectionTab()

    selected_name = tab._human_voice_name()
    selected_backend = tab._selected_human_voice_backend()

    assert selected_name == "bf_isabella"
    assert selected_backend == "kokoro"


def main() -> None:
    test_shutdown_sequence_can_speak_while_shutdown_is_in_progress()
    test_runtime_backend_failure_does_not_fall_back_to_local_qt_when_backend_is_active()
    test_runtime_unavailable_allows_local_qt_fallback()
    test_blank_voice_name_keeps_kokoro_profile_instead_of_defaulting_to_local_qt()
    print("shutdown speech and backend fallback checks passed")


if __name__ == "__main__":
    main()
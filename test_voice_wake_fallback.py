#!/usr/bin/env python3
"""Focused regression checks for stale-partial wake fallback behavior."""

import audioop
import math
import os
import struct
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from app.sentry_v2.voice_runtime import VoskCommandListener


def _make_listener(*, device_name: str = ""):
    commands: list[str] = []
    transcripts: list[dict[str, object]] = []
    listener = VoskCommandListener(
        model_path="dummy",
        wake_word="elion",
        command_cooldown_s=0.0,
        on_command=commands.append,
        on_transcript=transcripts.append,
        on_log=lambda _msg: None,
        device_name=device_name,
    )
    return listener, commands, transcripts


def test_partial_wake_detection_handles_on_lion_drift() -> None:
    listener, _commands, _transcripts = _make_listener()

    assert listener._partial_contains_wake("on lion") is True
    assert listener._partial_contains_wake("lion") is True


def test_partial_wake_detection_rejects_long_embedded_elliot_noise() -> None:
    listener, _commands, _transcripts = _make_listener()

    assert listener._partial_contains_wake("logging enabled the pir the elliot i current") is False
    assert listener._partial_contains_wake("status of e lion") is False


def test_stale_partial_does_not_dispatch_false_wake_from_embedded_elliot_noise() -> None:
    listener, commands, transcripts = _make_listener()
    listener._last_partial_text = "logging enabled the pir the elliot i current"
    listener._last_partial_updated_s = time.time() - 1.3
    listener._suppress_wake_only_until_s = 0.0

    listener._flush_stale_partial_if_due(now=time.time())

    assert commands == []
    assert not any(str(payload.get("text") or "") == "elion" for payload in transcripts)


def test_stale_partial_dispatches_wake_only_final() -> None:
    listener, commands, transcripts = _make_listener()
    listener._last_partial_text = "on lion"
    listener._last_partial_updated_s = time.time() - 1.3
    listener._suppress_wake_only_until_s = 0.0

    listener._flush_stale_partial_if_due(now=time.time())

    assert commands == ["elion"]
    assert any(
        str(payload.get("kind") or "") == "final" and str(payload.get("text") or "") == "elion"
        for payload in transcripts
    )


def test_stale_partial_dispatches_followup_command() -> None:
    listener, commands, transcripts = _make_listener()
    listener._last_partial_text = "elion who are you"
    listener._last_partial_updated_s = time.time() - 1.3
    listener._suppress_wake_only_until_s = 0.0

    listener._flush_stale_partial_if_due(now=time.time())

    assert commands == ["who are you"]
    assert any(
        str(payload.get("kind") or "") == "final" and str(payload.get("text") or "") == "who are you"
        for payload in transcripts
    )


def test_wake_only_final_dispatches_after_partial_ack_suppression() -> None:
    listener, _commands, _transcripts = _make_listener()
    listener._emit_partial_wake_ack("alion")

    command = listener._normalize_command_text("alion")

    assert command == "elion"


def test_wake_followup_strips_greeting_noise_after_partial_ack() -> None:
    listener, _commands, transcripts = _make_listener()
    listener._emit_partial_wake_ack("hi hello elliot introduce yourself")

    command = listener._normalize_command_text("hi hello elliot introduce yourself")

    assert command == "introduce yourself"
    assert any(
        str(payload.get("kind") or "") == "final"
        and str(payload.get("text") or "") == "introduce yourself"
        for payload in transcripts
    )


def test_wake_followup_buffer_clears_after_immediate_dispatch() -> None:
    listener, _commands, _transcripts = _make_listener()

    command = listener._normalize_command_text("elion who are you")

    assert command == "who are you"
    assert listener._listen_window_buffer == []


def test_vosk_phrase_grammar_is_opt_in() -> None:
    listener, _commands, _transcripts = _make_listener()
    original = os.environ.get("SMART_SENTRY_VOSK_CONSTRAINED_GRAMMAR")
    try:
        os.environ.pop("SMART_SENTRY_VOSK_CONSTRAINED_GRAMMAR", None)
        assert listener._use_constrained_vosk_phrase_grammar() is False

        os.environ["SMART_SENTRY_VOSK_CONSTRAINED_GRAMMAR"] = "1"
        assert listener._use_constrained_vosk_phrase_grammar() is True

        os.environ["SMART_SENTRY_VOSK_CONSTRAINED_GRAMMAR"] = "0"
        pinned_listener, _commands, _transcripts = _make_listener(device_name="Microphone (Logi USB Headset)")
        assert pinned_listener._use_constrained_vosk_phrase_grammar() is False
    finally:
        if original is None:
            os.environ.pop("SMART_SENTRY_VOSK_CONSTRAINED_GRAMMAR", None)
        else:
            os.environ["SMART_SENTRY_VOSK_CONSTRAINED_GRAMMAR"] = original


def test_vosk_phrase_grammar_defaults_on_for_pinned_windows_mic() -> None:
    original = os.environ.get("SMART_SENTRY_VOSK_CONSTRAINED_GRAMMAR")
    try:
        os.environ.pop("SMART_SENTRY_VOSK_CONSTRAINED_GRAMMAR", None)
        listener, _commands, _transcripts = _make_listener(device_name="Microphone (Logi USB Headset)")

        assert listener._use_constrained_vosk_phrase_grammar() is (os.name == "nt")
    finally:
        if original is None:
            os.environ.pop("SMART_SENTRY_VOSK_CONSTRAINED_GRAMMAR", None)
        else:
            os.environ["SMART_SENTRY_VOSK_CONSTRAINED_GRAMMAR"] = original


def test_camera_view_object_query_is_allowed_intent() -> None:
    listener, _commands, _transcripts = _make_listener()

    assert listener._is_allowed_command_or_intent("what objects can you see in the current camera view") is True
    assert listener._is_allowed_command_or_intent("describe to me what you currently see") is True


def test_quiet_speech_is_boosted_past_recognizer_gate() -> None:
    listener, _commands, _transcripts = _make_listener()
    sample_count = 4000

    def _chunk_for_target_rms(target_rms: int) -> bytes:
        amplitude = max(1, int(target_rms * (2 ** 0.5)))
        frames = []
        for index in range(sample_count):
            value = int(
                max(-32768, min(32767, amplitude * math.sin(2 * math.pi * 220 * (index / 16000.0))))
            )
            frames.append(struct.pack("<h", value))
        return b"".join(frames)

    for target_rms in (20, 30):
        chunk = _chunk_for_target_rms(target_rms)
        raw_rms = int(audioop.rms(chunk, 2))
        _boosted, boosted_rms, _peak, gain = listener._boost_audio_chunk(chunk)

        assert raw_rms < 35
        assert gain > 1.0
        assert boosted_rms >= int(getattr(listener, "_noise_rms_threshold", 95) or 95)


def test_recognizer_gate_is_softer_than_full_noise_threshold() -> None:
    listener, _commands, _transcripts = _make_listener()
    listener._adaptive_noise_threshold = False
    listener._noise_rms_threshold = 95

    assert listener._recognizer_gate_rms() == 68
    assert listener._should_process_recognizer_audio(80) is True
    assert listener._should_process_recognizer_audio(40) is False


def test_quieter_chunks_can_retrain_recognizer_gate() -> None:
    listener, _commands, _transcripts = _make_listener()
    listener._noise_rms_threshold = 95

    for _ in range(50):
        listener._should_process_recognizer_audio(70)

    assert listener._noise_rms_threshold == 84


def test_core_intent_recovery_handles_who_are_you_drift() -> None:
    listener, _commands, _transcripts = _make_listener()

    assert listener._canonicalize_command_text("we re yo an") == "who are you"
    assert listener._normalize_command_text("elion we re yo an") == "who are you"


def test_run_smart_sentry_drift_canonicalizes_to_connect_and_enable() -> None:
    listener, _commands, _transcripts = _make_listener()

    assert (
        listener._canonicalize_command_text("the smart say say the command run the smarts and three")
        == "connect boards and enable smart sentry"
    )
    assert listener._normalize_command_text("elion run the smarts and drink") == "connect boards and enable smart sentry"
    assert listener._normalize_command_text("elion run the smart sent tree") == "connect boards and enable smart sentry"
    assert listener._normalize_command_text("elion run the smart sent three") == "connect boards and enable smart sentry"


def test_single_word_command_passes_fast_final_gate() -> None:
    listener, _commands, _transcripts = _make_listener()
    listener._active_speech_started_s = time.time()

    assert listener._passes_final_transcript_gate("connect", now=time.time()) is True


def test_voice_state_transitions_emit_status_transcripts() -> None:
    listener, _commands, transcripts = _make_listener()

    listener._set_voice_state("LISTENING", reason="test-listening")
    listener._set_voice_state("PROCESSING", reason="test-processing")

    statuses = [
        str(payload.get("text") or "")
        for payload in transcripts
        if str(payload.get("kind") or "") == "status"
    ]

    assert statuses[:2] == ["listening", "processing"]


def test_phrase_variants_are_allowed_by_runtime_and_tab_gate() -> None:
    listener, _commands, _transcripts = _make_listener()
    from app.sentry_v2.sentry_v2_tab import SentryV2TabWidget

    tab = SentryV2TabWidget.__new__(SentryV2TabWidget)
    phrases = (
        "can you tell us who you are",
        "what all can you do for us",
        "what games can we play",
        "do you remember us",
        "do you still remember me",
        "give us a freeze dance challenge",
        "my kids are here and they want to meet you can you introduce yourself",
        "could you say something funny please",
        "hello there elion",
    )

    assert all(listener._is_allowed_command_or_intent(phrase) for phrase in phrases)
    assert all(tab._voice_prompt_has_supported_ai_intent(phrase) for phrase in phrases)


def main() -> None:
    test_partial_wake_detection_handles_on_lion_drift()
    test_partial_wake_detection_rejects_long_embedded_elliot_noise()
    test_stale_partial_does_not_dispatch_false_wake_from_embedded_elliot_noise()
    test_stale_partial_dispatches_wake_only_final()
    test_stale_partial_dispatches_followup_command()
    test_wake_only_final_dispatches_after_partial_ack_suppression()
    test_wake_followup_strips_greeting_noise_after_partial_ack()
    test_wake_followup_buffer_clears_after_immediate_dispatch()
    test_vosk_phrase_grammar_is_opt_in()
    test_vosk_phrase_grammar_defaults_on_for_pinned_windows_mic()
    test_camera_view_object_query_is_allowed_intent()
    test_quiet_speech_is_boosted_past_recognizer_gate()
    test_recognizer_gate_is_softer_than_full_noise_threshold()
    test_quieter_chunks_can_retrain_recognizer_gate()
    test_core_intent_recovery_handles_who_are_you_drift()
    test_run_smart_sentry_drift_canonicalizes_to_connect_and_enable()
    test_single_word_command_passes_fast_final_gate()
    test_voice_state_transitions_emit_status_transcripts()
    test_phrase_variants_are_allowed_by_runtime_and_tab_gate()
    print("voice wake fallback checks passed")


if __name__ == "__main__":
    main()
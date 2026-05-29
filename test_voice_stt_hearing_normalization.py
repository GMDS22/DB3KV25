#!/usr/bin/env python3
"""Focused regression checks for STT hearing normalization."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from app.sentry_v2.voice_runtime import VoskCommandListener


def _make_listener():
    commands: list[str] = []
    transcripts: list[dict[str, object]] = []
    listener = VoskCommandListener(
        model_path="dummy",
        wake_word="elion",
        command_cooldown_s=0.0,
        on_command=commands.append,
        on_transcript=transcripts.append,
        on_log=lambda _msg: None,
        device_name="",
    )
    return listener, commands, transcripts


def test_token_level_drift_recovers_connect_enable_command() -> None:
    listener, _commands, _transcripts = _make_listener()

    assert (
        listener._normalize_command_text("elion conect the boreds and inable smard sentra")
        == "connect boards and enable smart sentry"
    )


def test_token_level_drift_recovers_camera_status_and_diagnostics() -> None:
    listener, _commands, _transcripts = _make_listener()

    assert listener._normalize_command_text("elion open the kamra") == "open camera"
    assert listener._normalize_command_text("elion check statis") == "check status"
    assert listener._normalize_command_text("elion run diganostics") == "run diagnostics"


def test_token_level_drift_recovers_guarding_and_tracking_commands() -> None:
    listener, _commands, _transcripts = _make_listener()

    assert listener._normalize_command_text("elion resume gaurding mode") == "resume guarding mode"
    assert listener._normalize_command_text("elion start traking") == "start tracking"


def test_windows_phrase_drift_recovers_run_smart_sentry_command() -> None:
    listener, _commands, _transcripts = _make_listener()

    assert listener._normalize_command_text("wonder smart sentry to rob", confidence=0.16) == (
        "connect boards and enable smart sentry"
    )
    assert listener._normalize_command_text(
        "as the thought of that stuff like that and wonder smart sentry to rob",
        confidence=0.16,
    ) == "connect boards and enable smart sentry"


def test_phrase_alias_corrections_fix_recognition_token_drift() -> None:
    listener, _commands, _transcripts = _make_listener()

    assert listener._apply_phrase_alias_corrections("enable face rekognition") == "enable face recognition"
    assert listener._apply_phrase_alias_corrections("switch prophile") == "switch profile"


def main() -> None:
    test_token_level_drift_recovers_connect_enable_command()
    test_token_level_drift_recovers_camera_status_and_diagnostics()
    test_token_level_drift_recovers_guarding_and_tracking_commands()
    test_windows_phrase_drift_recovers_run_smart_sentry_command()
    test_phrase_alias_corrections_fix_recognition_token_drift()
    print("voice STT hearing normalization checks passed")


if __name__ == "__main__":
    main()
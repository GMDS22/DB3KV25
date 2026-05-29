#!/usr/bin/env python3
"""Focused regression checks for shared voice toggle command handling."""

import sys
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).parent))

from app.sentry_v2.sentry_v2_tab import SentryV2TabWidget
from app.sentry_v2.voice_runtime import VoskCommandListener


def _make_listener():
    return VoskCommandListener(
        model_path="dummy",
        wake_word="elion",
        command_cooldown_s=0.0,
        on_command=lambda _cmd: None,
        on_transcript=lambda _payload: None,
        on_log=lambda _msg: None,
    )


def _make_tab() -> SentryV2TabWidget:
    tab = SentryV2TabWidget.__new__(SentryV2TabWidget)
    tab._voice_phrase_last_by_key = {}
    tab._prepare_human_speech_text = lambda text, assistant_output=False: " ".join(str(text or "").split()).strip()
    return tab


def test_extended_pir_toggle_variants_normalize_to_disable_command() -> None:
    listener = _make_listener()

    phrases = (
        "turn the pir sensors off",
        "switch the pir guard off",
        "make the pir detectors disabled",
        "i want the pir sensor off",
    )

    for phrase in phrases:
        assert listener._normalize_command_text(phrase) == "disable pir sensors"


def test_wake_prefixed_pir_activate_normalizes_to_enable_command() -> None:
    listener = _make_listener()

    assert listener._normalize_command_text("elion activate the pir sensors") == "enable pir sensors"


def test_wake_prefixed_pir_status_for_query_normalizes_to_status_command() -> None:
    listener = _make_listener()

    assert listener._normalize_command_text("elion whats the status for the pir sensors") == "status pir sensors"


def test_pir_toggle_executor_uses_plural_voice_reply() -> None:
    tab = _make_tab()
    state = {"checked": True}
    tab._chk_pir_enabled = SimpleNamespace(
        isChecked=lambda: state["checked"],
        setChecked=lambda value: state.__setitem__("checked", bool(value)),
    )

    result = tab._execute_voice_toggle_command("disable pir sensors")

    assert result is not None
    spoken = str(result[1] or "").lower()
    assert "pir sensors are" in spoken
    assert "not active" in spoken


def test_pir_status_executor_reports_active_state_words() -> None:
    tab = _make_tab()
    state = {"checked": True}
    tab._chk_pir_enabled = SimpleNamespace(
        isChecked=lambda: state["checked"],
        setChecked=lambda value: state.__setitem__("checked", bool(value)),
    )

    result = tab._execute_voice_toggle_command("status pir sensors")

    assert result is not None
    spoken = str(result[1] or "").lower()
    assert "pir sensors are currently active" in spoken


def test_pir_toggle_executor_reports_already_active_state() -> None:
    tab = _make_tab()
    state = {"checked": True}
    tab._chk_pir_enabled = SimpleNamespace(
        isChecked=lambda: state["checked"],
        setChecked=lambda value: state.__setitem__("checked", bool(value)),
    )

    result = tab._execute_voice_toggle_command("enable pir sensors")

    assert result is not None
    spoken = str(result[1] or "").lower()
    assert "pir sensors are already active" in spoken


def main() -> None:
    test_extended_pir_toggle_variants_normalize_to_disable_command()
    test_wake_prefixed_pir_activate_normalizes_to_enable_command()
    test_wake_prefixed_pir_status_for_query_normalizes_to_status_command()
    test_pir_toggle_executor_uses_plural_voice_reply()
    test_pir_status_executor_reports_active_state_words()
    test_pir_toggle_executor_reports_already_active_state()
    print("voice toggle command checks passed")


if __name__ == "__main__":
    main()
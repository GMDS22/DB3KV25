#!/usr/bin/env python3
"""Focused regression checks for live transcript visibility in the conversation UI."""

import sys
import time
import types
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from app.sentry_v2.sentry_v2_tab import SentryV2TabWidget
from app.sentry_v2.voice_runtime import VoskCommandListener


class _FakeTranscriptOutput:
    def __init__(self) -> None:
        self.text = ""

    def setPlainText(self, text: str) -> None:
        self.text = str(text or "")


class _FakeReasoningPanel:
    def __init__(self) -> None:
        self.updates: list[dict[str, object]] = []

    def update_reasoning(self, payload: dict[str, object]) -> None:
        self.updates.append(dict(payload))


class _FakeTranscriptTab:
    def __init__(self) -> None:
        self._txt_voice_heard = _FakeTranscriptOutput()
        self._ai_reasoning_panel = _FakeReasoningPanel()
        self._last_voice_signature: dict[str, object] = {}
        self._voice_heard_status_text = "idle"
        self._voice_heard_partial_text = ""
        self._voice_heard_final_text = ""
        self._voice_last_final_transcript_s = 0.0
        self._voice_last_partial_transcript_s = 0.0
        self._voice_last_command_confidence = -1.0
        self._voice_last_partial_before_final_text = ""
        self.ai_states: list[str] = []
        self.events: list[tuple[tuple[object, ...], dict[str, object]]] = []
        self.logs: list[str] = []

        self._voice_signature_snapshot = types.MethodType(SentryV2TabWidget._voice_signature_snapshot, self)
        self._refresh_voice_hearing_panel = types.MethodType(SentryV2TabWidget._refresh_voice_hearing_panel, self)
        self._voice_transcript_reasoning_note = types.MethodType(SentryV2TabWidget._voice_transcript_reasoning_note, self)
        self._mirror_voice_transcript_to_reasoning_panel = types.MethodType(
            SentryV2TabWidget._mirror_voice_transcript_to_reasoning_panel,
            self,
        )

    def _human_voice_busy(self) -> bool:
        return False

    def _stop_human_speech(self) -> None:
        return

    def _voice_operator_currently_speaking(self, *, now=None) -> bool:
        return False

    def _refresh_operator_listening_state(self) -> None:
        return

    def _note_operator_voice_activity(self, *, now=None) -> None:
        return

    def _clear_voice_next_action_prompt(self) -> None:
        return

    def _on_ai_state_update(self, state: str) -> None:
        self.ai_states.append(str(state or ""))

    def _start_voice_interaction_window(self, **_kwargs) -> None:
        return

    def _prime_voice_listener_followup_window(self, **_kwargs) -> None:
        return

    def _log(self, message: str) -> None:
        self.logs.append(str(message or ""))

    def _record_runtime_conversation_event(self, *args, **kwargs) -> None:
        self.events.append((args, dict(kwargs)))


class _FakeFaceProfile:
    def __init__(self, profile_id: str, name: str) -> None:
        self.profile_id = profile_id
        self.name = name


class _FakeFaceLibrary:
    def __init__(self, profiles=None) -> None:
        self.profiles = list(profiles or [])

    def find_by_name(self, name: str):
        target = str(name or "").strip().lower()
        for profile in self.profiles:
            if str(getattr(profile, "name", "") or "").strip().lower() == target:
                return profile
        return None


class _FakeAuthorizationTab:
    def __init__(self) -> None:
        self._authorized_voice_frequency_hz = 0.0
        self._authorized_voice_identity_label = ""
        self.logs: list[str] = []
        self.spoken: list[str] = []
        self._identity_label = ""
        self._identity_profile_id = ""
        self._signature = {}
        self._face_library = _FakeFaceLibrary()
        self.config = types.SimpleNamespace(
            face_recognition=types.SimpleNamespace(
                operator_profile_id="",
                operator_profile_name="",
            )
        )

    def _voice_control_request_requires_operator(self, text: str) -> bool:
        return True

    def _voice_signature_snapshot(self):
        return dict(self._signature)

    def _current_voice_identity_label(self) -> str:
        return str(self._identity_label or "")

    def _current_voice_identity_profile_id(self) -> str:
        return str(self._identity_profile_id or "")

    def _normalize_voice_face_name(self, name: str) -> str:
        return SentryV2TabWidget._normalize_voice_face_name(name)

    def _spoken_face_profile_name(self, name: str) -> str:
        return SentryV2TabWidget._spoken_face_profile_name(name)

    def _configured_operator_face_profile(self):
        return SentryV2TabWidget._configured_operator_face_profile(self)

    def _configured_operator_face_identity(self):
        return SentryV2TabWidget._configured_operator_face_identity(self)

    def _speak_after_operator_quiet(self, text: str, *, interrupt: bool = False):
        self.spoken.append(str(text or ""))
        return True

    def _log(self, message: str) -> None:
        self.logs.append(str(message or ""))


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
    )
    return listener, commands, transcripts


def test_voice_transcript_updates_main_conversation_surface() -> None:
    tab = _FakeTranscriptTab()
    partial_payload = {
        "kind": "partial",
        "text": "hello elion",
        "timestamp": time.time(),
        "source": "windows",
    }

    SentryV2TabWidget._on_voice_transcript_received(tab, partial_payload)

    assert "Partial: hello elion" in tab._txt_voice_heard.text
    assert tab._ai_reasoning_panel.updates[-1] == {
        "section": "info",
        "content": "Hearing (windows): hello elion",
        "replace": True,
    }

    final_payload = {
        "kind": "final",
        "text": "who are you",
        "timestamp": time.time(),
        "source": "windows",
        "confidence": 0.82,
    }

    SentryV2TabWidget._on_voice_transcript_received(tab, final_payload)

    assert "Final: who are you" in tab._txt_voice_heard.text
    assert tab._ai_reasoning_panel.updates[-1] == {
        "section": "info",
        "content": "Heard final (windows), conf 0.82: who are you",
        "replace": True,
    }


def test_windows_partial_publish_caches_live_partial_text() -> None:
    listener, _commands, transcripts = _make_listener()

    listener._publish_partial_transcript("elion who are you", source="windows")

    assert listener._last_partial_text == "elion who are you"
    assert listener._last_partial_updated_s > 0.0
    assert any(
        str(payload.get("kind") or "") == "partial"
        and str(payload.get("text") or "") == "elion who are you"
        and str(payload.get("source") or "") == "windows"
        for payload in transcripts
    )


def test_voice_operator_authorization_seeds_from_recognized_face_identity() -> None:
    tab = _FakeAuthorizationTab()
    tab._identity_label = "gary"
    tab._signature = {"frequency_hz": 182.0}

    allowed = SentryV2TabWidget._authorize_voice_control_request(tab, "change theme")

    assert allowed is True
    assert tab._authorized_voice_identity_label == "gary"
    assert tab._authorized_voice_frequency_hz == 182.0


def test_voice_operator_authorization_allows_when_no_face_identity_is_available() -> None:
    tab = _FakeAuthorizationTab()
    tab._authorized_voice_identity_label = "gary"
    tab._authorized_voice_frequency_hz = 182.0
    tab._signature = {"frequency_hz": 260.0}

    allowed = SentryV2TabWidget._authorize_voice_control_request(tab, "change theme")

    assert allowed is True
    assert tab.spoken == []
    assert any("operator face not currently recognized" in message for message in tab.logs)


def test_configured_operator_profile_allows_matching_recognized_face_identity() -> None:
    tab = _FakeAuthorizationTab()
    tab._face_library = _FakeFaceLibrary([_FakeFaceProfile("gary-1", "Gary")])
    tab.config.face_recognition.operator_profile_id = "gary-1"
    tab.config.face_recognition.operator_profile_name = "Gary"
    tab._identity_profile_id = "gary-1"
    tab._identity_label = "gary"
    tab._signature = {"frequency_hz": 182.0}

    allowed = SentryV2TabWidget._authorize_voice_control_request(tab, "change theme")

    assert allowed is True
    assert tab.spoken == []
    assert tab._authorized_voice_identity_label == "gary"


def test_configured_operator_profile_allows_when_no_face_is_recognized() -> None:
    tab = _FakeAuthorizationTab()
    tab._face_library = _FakeFaceLibrary([_FakeFaceProfile("gary-1", "Gary")])
    tab.config.face_recognition.operator_profile_id = "gary-1"
    tab.config.face_recognition.operator_profile_name = "Gary"
    tab._signature = {"frequency_hz": 260.0}

    allowed = SentryV2TabWidget._authorize_voice_control_request(tab, "change theme")

    assert allowed is True
    assert tab.spoken == []
    assert any("configured operator face is not currently recognized" in message for message in tab.logs)


def test_voice_operator_authorization_rejects_conflicting_recognized_face_identity() -> None:
    tab = _FakeAuthorizationTab()
    tab._authorized_voice_identity_label = "gary"
    tab._authorized_voice_frequency_hz = 182.0
    tab._identity_label = "alex"
    tab._signature = {"frequency_hz": 260.0}

    allowed = SentryV2TabWidget._authorize_voice_control_request(tab, "change theme")

    assert allowed is False
    assert tab.spoken == [
        "I heard the request, but voice setting changes are currently locked to Gary while I recognize Alex in view."
    ]


def test_configured_operator_profile_rejects_conflicting_recognized_face_identity() -> None:
    tab = _FakeAuthorizationTab()
    tab._face_library = _FakeFaceLibrary([
        _FakeFaceProfile("gary-1", "Gary"),
        _FakeFaceProfile("alex-1", "Alex"),
    ])
    tab.config.face_recognition.operator_profile_id = "gary-1"
    tab.config.face_recognition.operator_profile_name = "Gary"
    tab._identity_profile_id = "alex-1"
    tab._identity_label = "alex"
    tab._signature = {"frequency_hz": 260.0}

    allowed = SentryV2TabWidget._authorize_voice_control_request(tab, "change theme")

    assert allowed is False
    assert tab.spoken == [
        "I heard the request, but voice setting changes are currently locked to Gary while I recognize Alex in view."
    ]


def main() -> None:
    test_voice_transcript_updates_main_conversation_surface()
    test_windows_partial_publish_caches_live_partial_text()
    test_voice_operator_authorization_seeds_from_recognized_face_identity()
    test_voice_operator_authorization_allows_when_no_face_identity_is_available()
    test_configured_operator_profile_allows_matching_recognized_face_identity()
    test_configured_operator_profile_allows_when_no_face_is_recognized()
    test_voice_operator_authorization_rejects_conflicting_recognized_face_identity()
    test_configured_operator_profile_rejects_conflicting_recognized_face_identity()
    print("voice transcript visibility checks passed")


if __name__ == "__main__":
    main()
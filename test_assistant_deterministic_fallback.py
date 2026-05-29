#!/usr/bin/env python3
"""Focused regression checks for deterministic assistant fallback speech."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from app.sentry_v2.assistant.models import AssistantAction, AssistantFinding
from app.sentry_v2.assistant.service import LocalAssistantService


def _build_service() -> LocalAssistantService:
    return LocalAssistantService(personality="sentinel")


def test_action_fallback_uses_deterministic_guidance_language() -> None:
    service = _build_service()

    reply = service._fallback_chat_text(
        "connect the boards",
        {},
        [],
        [],
        [AssistantAction("connect_link", "Connect Smart Sentry boards", {}, False)],
    )

    assert "could not reach the local model" not in reply.lower()
    assert "deterministic runtime guidance" in reply.lower()
    assert "connect smart sentry boards" in reply.lower()


def test_face_fallback_uses_summary_instead_of_model_error() -> None:
    service = _build_service()
    snapshot = {
        "config": {"face_recognition": {"enabled": True}},
        "camera_status": {"capture_open": False},
        "face_runtime": {},
        "recent_log_lines": [],
    }

    reply = service._fallback_chat_text("check the face recognition status", snapshot, [], [], [])

    assert "could not reach the local model" not in reply.lower()
    assert reply.startswith("Deterministic face-runtime summary.")
    assert "root cause:" in reply.lower()
    assert "suggested fix:" in reply.lower()


def test_generic_fallback_stays_actionable() -> None:
    service = _build_service()

    reply = service._fallback_chat_text("diagnose subsystem delta nine", {}, [], [], [])

    assert "could not reach the local model" not in reply.lower()
    assert "status report" in reply.lower()
    assert "another command" in reply.lower()


def test_finding_fallback_uses_deterministic_guidance_language() -> None:
    service = _build_service()

    reply = service._fallback_chat_text(
        "analyze the runtime",
        {},
        [AssistantFinding("warning", "Link", "The debug board is disconnected.")],
        [],
        [],
    )

    assert "could not reach the local model" not in reply.lower()
    assert reply.startswith("Using deterministic runtime guidance")
    assert "debug board is disconnected" in reply.lower()


def main() -> None:
    test_action_fallback_uses_deterministic_guidance_language()
    test_face_fallback_uses_summary_instead_of_model_error()
    test_generic_fallback_stays_actionable()
    test_finding_fallback_uses_deterministic_guidance_language()
    print("assistant deterministic fallback checks passed")


if __name__ == "__main__":
    main()
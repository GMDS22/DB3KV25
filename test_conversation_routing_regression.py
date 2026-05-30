#!/usr/bin/env python3
"""Regression checks for conversation vs explicit command routing."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from app.sentry_v2.assistant.service import LocalAssistantService


def _build_service() -> LocalAssistantService:
    return LocalAssistantService(personality="sentinel")


def test_help_understand_prompt_routes_to_conversation() -> None:
    service = _build_service()

    result = service._should_use_general_conversation(
        "Can you help me understand the detection system?",
        [],
    )

    assert result is True


def test_frustration_prompt_routes_to_conversation() -> None:
    service = _build_service()

    result = service._should_use_general_conversation(
        "I am feeling frustrated with the setup",
        [],
    )

    assert result is True


def test_can_you_connect_stays_explicit_command() -> None:
    service = _build_service()

    result = service._should_use_general_conversation(
        "Can you connect to boards",
        [],
    )

    assert result is False


def main() -> None:
    test_help_understand_prompt_routes_to_conversation()
    test_frustration_prompt_routes_to_conversation()
    test_can_you_connect_stays_explicit_command()
    print("conversation routing regression checks passed")


if __name__ == "__main__":
    main()

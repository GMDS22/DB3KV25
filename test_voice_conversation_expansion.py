#!/usr/bin/env python3
"""Focused regression checks for expanded deterministic voice conversation replies."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from app.sentry_v2.assistant.service import LocalAssistantService


def _build_service(*, personality: str = "playful") -> LocalAssistantService:
    return LocalAssistantService(personality=personality)


def test_family_intro_uses_known_names() -> None:
    service = _build_service()
    reply = service.fast_voice_conversation_reply(
        "my kids are here and they want to meet you can you introduce yourself",
        conversation_context={"friendly_recognized_names": ["Mia", "Noah"]},
    )

    assert reply is not None
    assert "Mia" in reply
    assert "Noah" in reply
    assert "Elion" in reply


def test_precision_coach_reply_is_available() -> None:
    service = _build_service()
    reply = service.fast_voice_conversation_reply("how can i improve the aiming precision")

    assert reply is not None
    assert any(token in reply.lower() for token in ("precision", "tracking", "center lock", "steadier"))


def test_identity_variant_prompt_is_available() -> None:
    service = _build_service()
    reply = service.fast_voice_conversation_reply("can you tell us who you are")

    assert reply is not None
    assert "Elion" in reply


def test_capability_variant_prompt_is_available() -> None:
    service = _build_service()
    reply = service.fast_voice_conversation_reply("what all can you do for us")

    assert reply is not None
    assert any(token in reply.lower() for token in ("smart sentry", "diagnostic", "command", "help"))


def test_playful_coach_reply_is_available() -> None:
    service = _build_service()
    reply = service.fast_voice_conversation_reply("how can i make it more playful")

    assert reply is not None
    assert "playful" in reply.lower() or "fun" in reply.lower()


def test_playful_variant_prompt_is_available() -> None:
    service = _build_service()
    reply = service.fast_voice_conversation_reply("could you make it more fun for the kids")

    assert reply is not None
    assert "playful" in reply.lower() or "fun" in reply.lower()


def test_family_discovery_prompt_is_available() -> None:
    service = _build_service()
    reply = service.fast_voice_conversation_reply("what can we ask you")

    assert reply is not None
    assert "joke" in reply.lower() or "introduce" in reply.lower()


def test_splash_mission_prompt_is_available() -> None:
    service = _build_service()
    reply = service.fast_voice_conversation_reply("give us a splash mission")

    assert reply is not None
    assert any(token in reply.lower() for token in ("mission", "challenge", "round"))


def test_social_memory_recall_uses_prior_names() -> None:
    service = _build_service()
    service.fast_voice_conversation_reply(
        "my kids are here and they want to meet you can you introduce yourself",
        conversation_context={"friendly_recognized_names": ["Mia", "Noah"]},
    )
    reply = service.fast_voice_conversation_reply("do you remember us")

    assert reply is not None
    assert "Mia" in reply
    assert "Noah" in reply


def test_social_memory_variant_recall_uses_prior_names() -> None:
    service = _build_service()
    service.fast_voice_conversation_reply(
        "my kids are here and they want to meet you can you introduce yourself",
        conversation_context={"friendly_recognized_names": ["Mia", "Noah"]},
    )
    reply = service.fast_voice_conversation_reply("do you still remember me")

    assert reply is not None
    assert "Mia" in reply
    assert "Noah" in reply


def test_followup_challenge_prompt_is_available() -> None:
    service = _build_service()
    first_reply = service.fast_voice_conversation_reply("give us a splash mission")
    followup_reply = service.fast_voice_conversation_reply("give us another challenge")

    assert first_reply is not None
    assert followup_reply is not None
    assert any(token in followup_reply.lower() for token in ("mission", "challenge", "round", "game"))
    assert followup_reply != first_reply


def test_followup_game_variant_prompt_is_available() -> None:
    service = _build_service()
    service.fast_voice_conversation_reply("give us a splash mission")
    followup_reply = service.fast_voice_conversation_reply("give us one more game")

    assert followup_reply is not None
    assert any(token in followup_reply.lower() for token in ("mission", "challenge", "round", "game"))


def test_freeze_challenge_prompt_is_available() -> None:
    service = _build_service()
    reply = service.fast_voice_conversation_reply("give us a freeze dance challenge")

    assert reply is not None
    assert any(token in reply.lower() for token in ("freeze", "statue", "hold"))


def test_joke_variant_prompt_is_available() -> None:
    service = _build_service()
    reply = service.fast_voice_conversation_reply("could you say something funny please")

    assert reply is not None
    profile_jokes = {str(item).strip() for item in (service._assistant_personality_profile().get("jokes") or []) if str(item).strip()}
    assert reply in profile_jokes


def test_greeting_variant_prompt_is_available() -> None:
    service = _build_service()
    reply = service.fast_voice_conversation_reply("hello there elion")

    assert reply is not None
    assert len(reply.strip()) > 0


def main() -> None:
    test_family_intro_uses_known_names()
    test_precision_coach_reply_is_available()
    test_identity_variant_prompt_is_available()
    test_capability_variant_prompt_is_available()
    test_playful_coach_reply_is_available()
    test_playful_variant_prompt_is_available()
    test_family_discovery_prompt_is_available()
    test_splash_mission_prompt_is_available()
    test_social_memory_recall_uses_prior_names()
    test_social_memory_variant_recall_uses_prior_names()
    test_followup_challenge_prompt_is_available()
    test_followup_game_variant_prompt_is_available()
    test_freeze_challenge_prompt_is_available()
    test_joke_variant_prompt_is_available()
    test_greeting_variant_prompt_is_available()
    print("voice conversation expansion checks passed")


if __name__ == "__main__":
    main()
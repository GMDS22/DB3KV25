#!/usr/bin/env python3
"""Focused regression checks for the person identity auto-fire veto."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from app.sentry_v2.engagement_planner import EngagementOrder
from app.sentry_v2.sentry_v2_config import SentryV2Config
from app.sentry_v2.sentry_v2_engine import SentryV2Engine
from app.sentry_v2.target_filter import DetectedObject
from app.sentry_v2.threat_scorer import TrackedTarget


def _make_person_target(
    *,
    track_id: int = 1,
    identity_label: str = "",
    friendly: bool = False,
    confidence: float = 0.98,
    persistence: float = 4.0,
) -> TrackedTarget:
    profile_id = f"profile-{track_id}" if identity_label else ""
    det = DetectedObject(
        track_id=track_id,
        class_name="person",
        confidence=confidence,
        bbox=(120, 80, 90, 180),
        center_x=165.0,
        center_y=170.0,
        frame_width=640,
        frame_height=480,
        identity_label=identity_label,
        identity_confidence=0.93 if identity_label else 0.0,
        identity_profile_id=profile_id,
        friendly_identity=friendly,
    )
    return TrackedTarget(
        det=det,
        threat_score=0.92,
        persistence=persistence,
        history_samples=8,
    )


def test_unknown_person_fire_allowed_by_default() -> None:
    # fire_on_unknown_persons defaults to True — unknown persons should not
    # block auto-fire when the operator has not configured a face library.
    config = SentryV2Config()
    config.face_recognition.enabled = True
    # default: fire_on_unknown_persons = True

    engine = SentryV2Engine(config)
    target = _make_person_target()

    assert engine._target_meets_fire_requirements(target, now=1.0) is True
    assert engine.get_engagement_stats()["fire_veto_reason"] == ""


def test_unknown_person_blocked_when_fire_on_unknown_false() -> None:
    # When fire_on_unknown_persons=False, unknown persons must be vetoed.
    config = SentryV2Config()
    config.face_recognition.enabled = True
    config.face_recognition.fire_on_unknown_persons = False

    engine = SentryV2Engine(config)
    target = _make_person_target()

    assert engine._target_meets_fire_requirements(target, now=1.0) is False
    assert "unknown person" in engine.get_engagement_stats()["fire_veto_reason"]


def test_friendly_person_identity_is_blocked_from_fire() -> None:
    config = SentryV2Config()
    config.face_recognition.enabled = True

    engine = SentryV2Engine(config)
    target = _make_person_target(identity_label="operator", friendly=True)

    assert engine._target_meets_fire_requirements(target, now=1.0) is False
    assert "friendly identity operator" in engine.get_engagement_stats()["fire_veto_reason"]


def test_explicit_hostile_identity_allows_fire() -> None:
    # A non-friendly recognized identity (current or recently cached) must
    # ALLOW fire — the original code inverted this logic and vetoed it.
    config = SentryV2Config()
    config.face_recognition.enabled = True

    engine = SentryV2Engine(config)
    engine.start()

    recognized_target = _make_person_target(track_id=7, identity_label="intruder", friendly=False)
    assert engine._target_meets_fire_requirements(recognized_target, now=10.0) is True

    engine.update([recognized_target.det], 10.0)

    # Same track without current identity label — engine resolves from cache.
    # Non-friendly cached identity should ALLOW fire (not veto).
    cached_target = _make_person_target(track_id=7)
    assert engine._target_meets_fire_requirements(cached_target, now=10.5) is True
    assert engine.get_engagement_stats()["fire_veto_reason"] == ""


def test_face_recognition_disabled_allows_fire_by_default() -> None:
    # When the operator disables face recognition, fire_on_unknown_persons
    # defaults True — all person targets should be fire-authorized.
    config = SentryV2Config()
    config.face_recognition.enabled = False

    engine = SentryV2Engine(config)
    target = _make_person_target(identity_label="intruder", friendly=False)

    assert engine._target_meets_fire_requirements(target, now=1.0) is True
    assert engine.get_engagement_stats()["fire_veto_reason"] == ""


def test_face_recognition_disabled_blocks_when_fire_on_unknown_false() -> None:
    # When face recognition is disabled AND fire_on_unknown_persons=False,
    # person auto-fire must be vetoed.
    config = SentryV2Config()
    config.face_recognition.enabled = False
    config.face_recognition.fire_on_unknown_persons = False

    engine = SentryV2Engine(config)
    target = _make_person_target(identity_label="intruder", friendly=False)

    assert engine._target_meets_fire_requirements(target, now=1.0) is False
    assert "face recognition disabled" in engine.get_engagement_stats()["fire_veto_reason"]


def test_begin_fire_backstop_blocks_friendly_person_target() -> None:
    config = SentryV2Config()
    config.face_recognition.enabled = True
    config.engagement.auto_trigger_enabled = True

    engine = SentryV2Engine(config)
    fire_events = []
    engine.on_fire(lambda burst: fire_events.append(burst))

    target = _make_person_target(identity_label="operator", friendly=True)
    order = EngagementOrder(target=target, pan=engine.current_pan, tilt=engine.current_tilt, rank=0)

    engine._begin_fire(order, 1.0)

    assert fire_events == []
    assert engine._engage_phase == "aim"
    assert "friendly identity operator" in engine.get_engagement_stats()["fire_veto_reason"]


def main() -> None:
    test_unknown_person_fire_allowed_by_default()
    test_unknown_person_blocked_when_fire_on_unknown_false()
    test_friendly_person_identity_is_blocked_from_fire()
    test_explicit_hostile_identity_allows_fire()
    test_face_recognition_disabled_allows_fire_by_default()
    test_face_recognition_disabled_blocks_when_fire_on_unknown_false()
    test_begin_fire_backstop_blocks_friendly_person_target()
    print("person identity fire-gate checks passed")


if __name__ == "__main__":
    main()
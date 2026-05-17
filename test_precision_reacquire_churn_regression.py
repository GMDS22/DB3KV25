#!/usr/bin/env python3
"""Focused regression checks for tracker-ID churn during active precision reacquire."""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from app.sentry_v2.engagement_planner import EngagementOrder
from app.sentry_v2.sentry_v2_config import SentryV2Config
from app.sentry_v2.sentry_v2_engine import SentryV2Engine
from app.sentry_v2.target_filter import DetectedObject, FilterDecision
from app.sentry_v2.threat_scorer import TrackedTarget


def _make_target(
    *,
    track_id: int,
    confidence: float = 0.96,
    center_x: float = 320.0,
    center_y: float = 210.0,
) -> TrackedTarget:
    det = DetectedObject(
        track_id=track_id,
        class_name="person",
        confidence=confidence,
        bbox=(280, 120, 84, 180),
        center_x=center_x,
        center_y=center_y,
        frame_width=640,
        frame_height=480,
    )
    return TrackedTarget(
        det=det,
        threat_score=0.88,
        persistence=0.35,
        history_samples=5,
        heading_x=0.02,
        heading_y=0.0,
        heading_stability=0.92,
    )


def test_tracker_churn_grace_holds_confirm_pending_frame() -> None:
    config = SentryV2Config()
    engine = SentryV2Engine(config)
    now = time.time()

    original = _make_target(track_id=7)
    churned = _make_target(track_id=19, center_x=326.0, center_y=214.0)
    order = EngagementOrder(target=churned, pan=engine.current_pan, tilt=engine.current_tilt, rank=0)

    engine._remember_active_target(original.det, target=original, timestamp=now - 0.05)
    engine._remember_active_target(churned.det, target=churned, timestamp=now)
    engine._arm_active_reacquire_confirm_pending(old_track_id=7, new_track_id=19, now=now)
    engine.last_targets = []
    engine.last_detections = [churned.det]
    engine.last_filter_diagnostics = [
        FilterDecision(
            track_id=19,
            class_name="person",
            source="yolo",
            confidence=float(churned.det.confidence),
            area_ratio=float(churned.det.area_ratio),
            passed=False,
            reason="semantic_confirm",
            detail="confirm pending",
            confirm_hits=1,
            confirm_required=2,
        )
    ]
    engine._find_reacquire_target = lambda _order: None  # type: ignore[method-assign]

    held_target = engine._find_active_target(order)

    assert held_target is order.target
    assert engine.get_engagement_stats()["reacquire_note"] == "reacquire confirm pending 19"


def test_tracker_churn_grace_does_not_hold_without_pending_state() -> None:
    config = SentryV2Config()
    engine = SentryV2Engine(config)

    target = _make_target(track_id=11)
    order = EngagementOrder(target=target, pan=engine.current_pan, tilt=engine.current_tilt, rank=0)

    engine._remember_active_target(target.det, target=target, timestamp=1.0)
    engine.last_targets = []
    engine.last_detections = [target.det]
    engine.last_filter_diagnostics = [
        FilterDecision(
            track_id=11,
            class_name="person",
            source="yolo",
            confidence=float(target.det.confidence),
            area_ratio=float(target.det.area_ratio),
            passed=False,
            reason="semantic_confirm",
            detail="confirm pending",
            confirm_hits=1,
            confirm_required=2,
        )
    ]
    engine._find_reacquire_target = lambda _order: None  # type: ignore[method-assign]

    assert engine._find_active_target(order) is None


def main() -> None:
    test_tracker_churn_grace_holds_confirm_pending_frame()
    test_tracker_churn_grace_does_not_hold_without_pending_state()
    print("precision reacquire churn regression checks passed")


if __name__ == "__main__":
    main()
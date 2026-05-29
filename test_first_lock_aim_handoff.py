#!/usr/bin/env python3
"""Focused regression checks for coarse-acquire to precision handoff behavior."""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from app.sentry_v2.engagement_planner import EngagementOrder
from app.sentry_v2.sentry_v2_config import SentryV2Config
from app.sentry_v2.sentry_v2_engine import SentryV2Engine
from app.sentry_v2.target_filter import DetectedObject
from app.sentry_v2.threat_scorer import TrackedTarget


def _make_target(*, track_id: int, center_x: float, center_y: float) -> TrackedTarget:
    det = DetectedObject(
        track_id=track_id,
        class_name="person",
        confidence=0.95,
        bbox=(420, 120, 84, 180),
        center_x=center_x,
        center_y=center_y,
        frame_width=640,
        frame_height=480,
    )
    return TrackedTarget(
        det=det,
        threat_score=0.91,
        persistence=0.40,
        history_samples=6,
        heading_x=0.01,
        heading_y=0.0,
        heading_stability=0.94,
    )


def test_large_residual_error_stays_in_coarse_acquire() -> None:
    config = SentryV2Config()
    engine = SentryV2Engine(config)
    now = time.time()

    far_target = _make_target(track_id=17, center_x=580.0, center_y=240.0)
    raw_err_pan, raw_err_tilt = engine._compute_target_angle_error(far_target.det)
    order = EngagementOrder(
        target=far_target,
        pan=engine.current_pan + raw_err_pan,
        tilt=engine.current_tilt + raw_err_tilt,
        rank=0,
    )

    engine._queue = [order]
    engine._queue_index = 0
    engine.last_targets = [far_target]

    engine._start_order_engagement(order, now)
    first_command_pan = float(engine.current_pan)

    # Enough time passes for the first coarse move to settle, but the target is
    # still far off-center and should require another coarse acquire step.
    engine.last_targets = [far_target]
    engine._update_engaging(now + 0.20)

    assert engine._engage_phase == "aim"
    assert float(engine.current_pan) > first_command_pan


def test_small_residual_error_can_enter_precision() -> None:
    config = SentryV2Config()
    engine = SentryV2Engine(config)
    now = time.time()

    near_target = _make_target(track_id=23, center_x=336.0, center_y=240.0)
    raw_err_pan, raw_err_tilt = engine._compute_target_angle_error(near_target.det)
    order = EngagementOrder(
        target=near_target,
        pan=engine.current_pan + raw_err_pan,
        tilt=engine.current_tilt + raw_err_tilt,
        rank=0,
    )

    engine._queue = [order]
    engine._queue_index = 0
    engine.last_targets = [near_target]

    engine._start_order_engagement(order, now)
    engine.last_targets = [near_target]
    engine._update_engaging(now + 0.20)

    assert engine._engage_phase == "precision"


def main() -> None:
    test_large_residual_error_stays_in_coarse_acquire()
    test_small_residual_error_can_enter_precision()
    print("first-lock coarse handoff regression checks passed")


if __name__ == "__main__":
    main()
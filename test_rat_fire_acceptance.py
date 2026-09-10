"""Controlled acceptance checks for the strict rat auto-fire contract."""

from pathlib import Path

from app.sentry_v2.sentry_v2_config import SentryV2Config, TargetFilterConfig
from app.sentry_v2.sentry_v2_engine import SentryV2Engine
from app.sentry_v2.target_filter import DetectedObject, TargetFilter
from app.sentry_v2.threat_scorer import TrackedTarget


def _detection(class_name: str, *, track_id: int = 1, confidence: float = 0.92) -> DetectedObject:
    return DetectedObject(
        track_id=track_id,
        class_name=class_name,
        confidence=confidence,
        bbox=(300, 200, 80, 40),
        center_x=340.0,
        center_y=220.0,
        frame_width=640,
        frame_height=480,
    )


def test_clutter_scene_has_zero_approved_rat_targets():
    config = TargetFilterConfig(
        allowed_classes=["rat"],
        min_confidence=0.80,
        min_size_ratio=0.0025,
        shape_filter_enabled=True,
        shape_profile_name="rat",
        semantic_min_confirm_frames=3,
        semantic_min_confirm_confidence=0.72,
    )
    target_filter = TargetFilter(config)
    clutter = [_detection(name, track_id=index) for index, name in enumerate(("bottle", "chair", "box", "backpack"), 1)]

    for frame in range(3):
        qualified = target_filter.filter(clutter, timestamp=float(frame))
        assert qualified == []


def test_confirmed_moving_rat_passes_final_authorization():
    config = SentryV2Config()
    config.target_filter.allowed_classes = ["rat"]
    config.target_filter.min_confidence = 0.80
    config.target_filter.min_size_ratio = 0.0025
    config.target_filter.shape_filter_enabled = True
    config.target_filter.shape_profile_name = "rat"
    config.target_filter.semantic_min_confirm_frames = 3
    config.target_filter.semantic_min_confirm_confidence = 0.72
    config.engagement.motion_policy_mode = "require_recent_motion"
    engine = SentryV2Engine(config)
    detection = _detection("rat")

    for frame in range(3):
        qualified, decisions = engine._filter.filter_with_diagnostics([detection], timestamp=100.0 + (frame * 0.1))
    engine.last_detections = [detection]
    engine.last_filter_diagnostics = decisions
    engine._motion_policy_state[1] = {
        "state": "ENGAGEABLE",
        "motion_allowed": True,
        "recent_motion_distance_px": 24.0,
        "motion_confidence": 0.70,
        "average_velocity_px_s": 18.0,
    }

    assert qualified == [detection]
    target = TrackedTarget(det=detection, persistence=0.5, threat_score=0.9)
    assert engine._target_meets_fire_requirements(target, now=3.0) is True
    assert engine._last_fire_gate_trace["approved"] is True
    assert all(stage["pass"] for stage in engine._last_fire_gate_trace["stages"])


def test_stationary_rat_remains_rejected_despite_velocity_only_signal():
    config = SentryV2Config()
    config.target_filter.allowed_classes = ["rat"]
    config.target_filter.min_confidence = 0.80
    config.target_filter.min_size_ratio = 0.0025
    config.target_filter.shape_filter_enabled = True
    config.target_filter.shape_profile_name = "rat"
    config.engagement.motion_policy_mode = "require_recent_motion"
    engine = SentryV2Engine(config)
    detection = _detection("rat")
    engine.last_detections = [detection]
    engine.last_filter_diagnostics = [
        type("Decision", (), {"track_id": 1, "passed": True, "confirm_hits": 3, "confirm_required": 3, "reason": "qualified"})()
    ]
    engine._motion_policy_state[1] = {
        "state": "ENGAGEABLE",
        "motion_allowed": True,
        "recent_motion_distance_px": 4.0,
        "motion_confidence": 0.70,
        "average_velocity_px_s": 40.0,
    }

    target = TrackedTarget(det=detection, persistence=0.5, threat_score=0.9)
    assert engine._target_meets_fire_requirements(target, now=1.0) is False
    assert "displacement" in engine.get_engagement_stats()["fire_veto_reason"]


def test_effective_runtime_model_and_rat_profile_are_logged_inputs():
    settings_path = Path(__file__).parent / "app" / "config" / "smart_sentry_settings.json"
    config = SentryV2Config.load(str(settings_path))

    assert config.detection_mode.yolo_model_name == "ratdogcat_last.pt"
    assert config.detection_mode.yolo_confidence >= 0.85
    assert config.detection_mode.yolo_min_area >= 2000
    assert config.target_filter.shape_profile_name == "rat"
    assert config.target_filter.min_confidence >= 0.80

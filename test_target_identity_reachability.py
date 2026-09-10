"""Focused checks for semantic animal confirmation and servo reachability."""

from app.sentry_v2.engagement_planner import EngagementPlanner
from app.sentry_v2.sentry_v2_config import EngagementConfig, GuardConfig, SentryV2Config, TargetFilterConfig
from app.sentry_v2.sentry_v2_engine import SentryV2Engine
from app.sentry_v2.target_filter import DetectedObject, TargetFilter
from app.sentry_v2.threat_scorer import TrackedTarget


def _animal_detection(*, confidence: float = 0.9, track_id: int = 1) -> DetectedObject:
    return DetectedObject(
        track_id=track_id,
        class_name="rat",
        confidence=confidence,
        bbox=(300, 200, 80, 80),
        center_x=340.0,
        center_y=240.0,
        frame_width=640,
        frame_height=480,
    )


def test_animal_identity_requires_three_consistent_frames():
    config = TargetFilterConfig(
        allowed_classes=["cat", "dog", "rat"],
        min_confidence=0.5,
        min_size_ratio=0.001,
        shape_filter_enabled=False,
        semantic_min_confirm_frames=1,
    )
    target_filter = TargetFilter(config)
    detection = _animal_detection()

    qualified_first = target_filter.filter([detection], timestamp=1.0)
    qualified_second = target_filter.filter([detection], timestamp=1.1)
    qualified_third = target_filter.filter([detection], timestamp=1.2)

    assert qualified_first == []
    assert qualified_second == []
    assert qualified_third == [detection]


def test_animal_identity_rejects_full_frame_box():
    config = TargetFilterConfig(
        allowed_classes=["cat", "dog", "rat"],
        min_confidence=0.5,
        min_size_ratio=0.0001,
        max_size_ratio=0.0,
        shape_filter_enabled=False,
    )
    target_filter = TargetFilter(config)
    detection = DetectedObject(
        track_id=2,
        class_name="rat",
        confidence=0.95,
        bbox=(0, 0, 1083, 720),
        center_x=541.5,
        center_y=360.0,
        frame_width=1280,
        frame_height=720,
    )

    qualified, decisions = target_filter.filter_with_diagnostics([detection], timestamp=1.0)

    assert qualified == []
    assert decisions[0].reason == "semantic_box_too_large"


def _target(norm_cx: float) -> TrackedTarget:
    detection = _animal_detection()
    detection.center_x = norm_cx * detection.frame_width
    return TrackedTarget(det=detection, threat_score=0.9, persistence=1.0)


def test_planner_skips_target_beyond_pan_limit():
    guard = GuardConfig(camera_hfov=120.0, camera_vfov=60.0, pan_min=0.0, pan_max=180.0)
    planner = EngagementPlanner(EngagementConfig(min_threat_score=0.2, max_queue_length=2), guard)

    orders = planner.plan([_target(1.0)], current_pan=170.0, current_tilt=55.0)

    assert orders == []


def test_planner_keeps_target_inside_servo_envelope():
    guard = GuardConfig(camera_hfov=120.0, camera_vfov=60.0, pan_min=0.0, pan_max=180.0)
    planner = EngagementPlanner(EngagementConfig(min_threat_score=0.2, max_queue_length=2), guard)

    orders = planner.plan([_target(0.5)], current_pan=90.0, current_tilt=55.0)

    assert len(orders) == 1


def test_stationary_animal_is_not_engageable_under_allow_stationary_profile():
    config = SentryV2Config()
    config.engagement.motion_policy_mode = "allow_stationary"
    config.engagement.motion_allow_stationary_engagement = True
    engine = SentryV2Engine(config)

    engageable, snapshots = engine._apply_motion_policy_to_targets([_target(0.5)], 1.0)

    assert engageable == []
    assert snapshots[0]["profile_mode"] == "require_recent_motion"


def test_stationary_animal_cannot_pass_backup_fire_gate():
    config = SentryV2Config()
    config.engagement.motion_policy_mode = "require_recent_motion"
    engine = SentryV2Engine(config)
    engine._motion_policy_state[1] = {
        "motion_allowed": False,
        "suppression_reason": "recent motion timeout",
    }

    assert engine._target_meets_fire_requirements(_target(0.5), now=1.0) is False
    assert "motion" in engine.get_engagement_stats()["fire_veto_reason"]


def test_old_stationary_target_rejected_even_with_micro_motion():
    """
    Regression test: Track 356 false-positive (storage room labeled as 'rat' with 0.74-0.85 confidence,
    128 seconds old) passed all gates because micro-jitter (4px) and weak motion_confidence (0.46)
    reset the motion-policy state to ENGAGEABLE. 
    
    This test verifies that targets 5+ seconds old with insufficient meaningful motion
    are rejected from fire authorization, preventing false-positive fires on old stationary
    misclassifications.
    """
    config = SentryV2Config()
    config.engagement.motion_policy_mode = "require_recent_motion"
    config.engagement.fire_trigger_min_confidence = 0.34
    config.engagement.fire_trigger_min_persistence = 0.08
    engine = SentryV2Engine(config)
    
    # Create a 128-second-old target (Track 356 scenario)
    old_target = _target(0.5)
    old_target.age = 128.0  # Very old detection
    
    # Motion policy state shows it's ENGAGEABLE (motion_allowed=True) due to micro-motion reset
    # but recent_motion_distance_px is only 4 pixels (insufficient for legitimate animal motion)
    engine._motion_policy_state[1] = {
        "state": "ENGAGEABLE",
        "motion_allowed": True,
        "recent_motion_distance_px": 4.0,  # Only 4px motion (noise/jitter, not real animal)
        "average_velocity_px_s": 39.3,
        "motion_confidence": 0.46,
        "suppression_reason": "",
    }
    
    # Should REJECT the fire despite motion_allowed=True, because track is old with no meaningful motion
    assert engine._target_meets_fire_requirements(old_target, now=129.0) is False
    assert "too old" in engine.get_engagement_stats()["fire_veto_reason"]
    assert "insufficient motion" in engine.get_engagement_stats()["fire_veto_reason"]


def test_detect_faces_preview_only_lists_unknown_faces_for_enrollment():
    """Only unrecognized faces should appear in the enrollment sidebar, while known faces stay
    as video overlays only."""
    import numpy as np
    from types import SimpleNamespace

    from app.sentry_v2.face_identity import FaceMatchResult
    from app.sentry_v2.sentry_v2_tab import SentryV2Tab

    class DummyTab:
        def __init__(self):
            self.config = SimpleNamespace(face_recognition=SimpleNamespace(min_face_size_px=56, recognition_threshold=0.82))
            self._face_runtime = SimpleNamespace(
                detect_faces=lambda frame, **kwargs: [(0, 0, 50, 50)],
                extract_embeddings_from_bboxes=lambda frame, bboxes: [np.ones(128, dtype=np.float32)],
                match_known_faces=lambda frame, **kwargs: [
                    FaceMatchResult(
                        bbox=(0, 0, 50, 50),
                        profile_id="known-1",
                        name="Alice",
                        confidence=0.94,
                        friendly=True,
                        announce_name=True,
                        cute_gesture=True,
                    )
                ],
                detect_unknown_faces=lambda frame, **kwargs: [],
            )
            self._face_registration_candidates = []
            self._face_candidate_layout = None
            self._force_next_display_refresh = False
            self._log = lambda *args, **kwargs: None
            self._set_face_import_status = lambda *args, **kwargs: None
            self._rebuild_face_registration_candidates_ui = lambda: None
            self._face_runtime_status = None

    tab = DummyTab()
    SentryV2Tab._detect_faces_from_frame(tab, np.zeros((100, 100, 3), dtype=np.uint8), source_label="test")

    assert tab._face_registration_candidates == []

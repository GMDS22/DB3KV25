import os
import sys

import cv2
import numpy as np


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from app.sentry_v2.engagement_planner import EngagementPlanner
from app.sentry_v2.sentry_v2_config import SentryV2Config
from app.sentry_v2.sentry_v2_detector import SentryV2Detector
from app.sentry_v2.threat_scorer import TrackedTarget
from app.sentry_v2.target_filter import DetectedObject, TargetFilter


def make_frame(rect=None, color=(0, 0, 255)):
    frame = np.zeros((240, 320, 3), dtype=np.uint8)
    if rect is not None:
        x, y, w, h = rect
        frame[y:y + h, x:x + w] = color
    return frame


def assert_true(condition, message):
    if not condition:
        raise AssertionError(message)
    print(f"[VERIFY] PASS: {message}")


def verify_motion_required():
    detector = SentryV2Detector()
    detector.color_preset = "any"
    detector.set_yolo_classes("")
    blank = make_frame()
    moved = make_frame((40, 50, 40, 40))

    result_1 = detector.detect(blank, 10)
    result_2 = detector.detect(moved, 10)
    result_3 = detector.detect(moved, 10)

    assert_true(result_1 == [], "motion-locked mode ignores the first static frame")
    assert_true(len(result_2) >= 1, "motion-locked mode detects a moving object")
    assert_true(result_3 == [], "motion-locked mode stops showing the object when motion stops")


def verify_color_filter():
    detector = SentryV2Detector()
    detector.color_preset = "red"
    detector.color_fusion_overlap = 10
    detector.set_yolo_classes("")
    blank = make_frame()
    red_move = make_frame((60, 50, 45, 45), (0, 0, 255))
    blue_move = make_frame((60, 50, 45, 45), (255, 0, 0))

    detector.detect(blank, 10)
    red_result = detector.detect(red_move, 10)

    detector.reset()
    detector.color_preset = "red"
    detector.color_fusion_overlap = 10
    detector.set_yolo_classes("")
    detector.detect(blank, 10)
    blue_result = detector.detect(blue_move, 10)

    assert_true(len(red_result) >= 1, "red color filter keeps a red moving object")
    assert_true(blue_result == [], "red color filter rejects a blue moving object")


def verify_color_preset_discrimination():
    detector = SentryV2Detector()
    detector.color_min_area = 50
    detector.color_max_area = 100000

    gray = np.full((240, 320, 3), 160, dtype=np.uint8)
    cyan_patch = gray.copy()
    cyan_patch[60:120, 90:150] = (255, 255, 0)

    detector.color_preset = "blue"
    blue_result = detector.detect(cyan_patch, 6)

    detector.color_preset = "cyan"
    cyan_result = detector.detect(cyan_patch, 6)

    purple_patch = gray.copy()
    purple_patch[60:120, 90:150] = (220, 30, 120)
    detector.color_preset = "blue"
    blue_on_purple = detector.detect(purple_patch, 6)

    greenish_cyan_patch = gray.copy()
    greenish_cyan_patch[60:120, 90:150] = (169, 220, 30)
    detector.color_preset = "green"
    green_on_cyanish = detector.detect(greenish_cyan_patch, 6)

    assert_true(blue_result == [], "blue preset rejects a cyan-only patch")
    assert_true(len(cyan_result) >= 1, "cyan preset keeps a cyan patch")
    assert_true(blue_on_purple == [], "blue preset rejects a purple-leaning patch")
    assert_true(green_on_cyanish == [], "green preset rejects a cyan-leaning patch")


def verify_black_background_rejection():
    detector = SentryV2Detector()
    detector.color_preset = "black"
    detector.color_min_area = 50
    detector.color_max_area = 100000

    blank = np.zeros((240, 320, 3), dtype=np.uint8)
    gray = np.full((240, 320, 3), 160, dtype=np.uint8)
    black_patch = gray.copy()
    black_patch[60:120, 90:150] = (0, 0, 0)

    blank_result = detector.detect(blank, 6)
    patch_result = detector.detect(black_patch, 6)

    assert_true(blank_result == [], "black preset ignores a full-frame dark background")
    assert_true(len(patch_result) >= 1, "black preset still detects a bounded black target")


def verify_real_world_color_shades():
    detector = SentryV2Detector()
    detector.color_min_area = 50
    detector.color_max_area = 100000

    background = np.full((240, 320, 3), 128, dtype=np.uint8)

    def hsv_patch(h: int, s: int, v: int) -> np.ndarray:
        patch = np.uint8([[[h, s, v]]])
        return cv2.cvtColor(patch, cv2.COLOR_HSV2BGR)[0, 0]

    checks = [
        ("red", (0, 95, 110), "red preset keeps a dim red shade"),
        ("orange", (18, 95, 120), "orange preset keeps a muted orange shade"),
        ("yellow", (30, 105, 130), "yellow preset keeps a softer yellow shade"),
        ("green", (60, 95, 110), "green preset keeps a dim green shade"),
        ("blue", (112, 95, 115), "blue preset keeps a dim blue shade"),
        ("purple", (145, 95, 115), "purple preset keeps a dim purple shade"),
        ("cyan", (90, 95, 120), "cyan preset keeps a dim cyan shade"),
        ("white", (30, 45, 190), "white preset keeps an off-white shade"),
        ("black", (30, 80, 60), "black preset keeps a dark low-saturation shade"),
    ]

    for preset, hsv, message in checks:
        bgr = tuple(int(v) for v in hsv_patch(*hsv))
        frame = background.copy()
        frame[60:140, 90:170] = bgr
        detector.color_preset = preset
        result = detector.detect(frame, 6)
        assert_true(len(result) >= 1, message)


def verify_adaptive_shade_tolerance():
    detector = SentryV2Detector()
    detector.color_min_area = 50
    detector.color_max_area = 100000

    background = np.full((240, 320, 3), 128, dtype=np.uint8)
    adaptive_cases = [
        ("red", (0, 70, 92), "red preset auto-corrects a darker shaded red"),
        ("green", (60, 68, 92), "green preset auto-corrects a darker shaded green"),
        ("blue", (112, 68, 92), "blue preset auto-corrects a darker shaded blue"),
        ("purple", (145, 60, 85), "purple preset auto-corrects a darker shaded purple"),
        ("cyan", (90, 60, 95), "cyan preset auto-corrects a darker shaded cyan"),
    ]

    for preset, hsv, message in adaptive_cases:
        patch = np.uint8([[[hsv[0], hsv[1], hsv[2]]]])
        bgr = tuple(int(v) for v in cv2.cvtColor(patch, cv2.COLOR_HSV2BGR)[0, 0])
        frame = background.copy()
        frame[60:140, 90:170] = bgr
        detector.color_preset = preset
        result = detector.detect(frame, 6)
        assert_true(len(result) >= 1, message)


def verify_class_refinement():
    detector = SentryV2Detector()
    detector.color_preset = "any"
    detector._yolo_loaded = True
    detector._yolo_model = object()
    detector.set_yolo_classes("person")
    detector._detect_yolo = lambda frame: [(40, 50, 40, 40, 0.9, 0)]

    blank = make_frame()
    moved = make_frame((40, 50, 40, 40))
    detector.detect(blank, 10)
    result = detector.detect(moved, 10)

    assert_true(len(result) == 1 and int(result[0][5]) == 0, "class refinement preserves only overlapping moving class targets")


def verify_motion_fallback_survives_filtering():
    cfg = SentryV2Config()
    cfg.target_filter.allowed_classes = ["person"]
    cfg.target_filter.min_size_ratio = 0.01
    filt = TargetFilter(cfg.target_filter)

    moving_fallback = DetectedObject(
        track_id=1,
        class_name="moving_object",
        confidence=0.75,
        bbox=(50, 60, 18, 18),
        center_x=59.0,
        center_y=69.0,
        source="motion_locked",
        frame_width=320,
        frame_height=240,
    )

    filtered = filt.filter([moving_fallback])
    assert_true(len(filtered) == 1, "motion-locked fallback boxes survive class and size filtering")


def verify_single_target_planning():
    cfg = SentryV2Config()
    cfg.engagement.single_target_only = True
    cfg.engagement.max_queue_length = 5
    planner = EngagementPlanner(cfg.engagement, cfg.guard)

    targets = []
    for idx, cx in enumerate((120, 180), start=1):
        det = DetectedObject(
            track_id=idx,
            class_name="moving_object",
            confidence=0.8,
            bbox=(cx, 80, 30, 30),
            center_x=float(cx + 15),
            center_y=95.0,
            source="motion_locked",
            frame_width=320,
            frame_height=240,
        )
        targets.append(TrackedTarget(det=det, threat_score=0.8 - (idx * 0.1)))

    queue = planner.plan(targets, 90.0, 50.0)
    assert_true(len(queue) == 1, "planner keeps only one target in single-target mode")


def main() -> int:
    verify_motion_required()
    verify_color_filter()
    verify_color_preset_discrimination()
    verify_black_background_rejection()
    verify_real_world_color_shades()
    verify_adaptive_shade_tolerance()
    verify_class_refinement()
    verify_motion_fallback_survives_filtering()
    verify_single_target_planning()
    print("[VERIFY] ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
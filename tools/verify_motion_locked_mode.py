import os
import sys

import numpy as np


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from app.sentry_v2.engagement_planner import EngagementPlanner
from app.sentry_v2.sentry_v2_config import SentryV2Config
from app.sentry_v2.sentry_v2_detector import SentryV2Detector
from app.sentry_v2.threat_scorer import TrackedTarget
from app.sentry_v2.target_filter import DetectedObject


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
    verify_class_refinement()
    verify_single_target_planning()
    print("[VERIFY] ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
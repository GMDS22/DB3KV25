import os
import sys

import numpy as np


os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")
os.environ.setdefault("CUDA_VISIBLE_DEVICES", "")


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_DIR = os.path.join(REPO_ROOT, "app")
if APP_DIR not in sys.path:
    sys.path.insert(0, APP_DIR)


from PyQt5.QtWidgets import QApplication

from MAIN_FILE_SINGLE_CAM import TrackingApp


def make_frame(rects=None, color=(0, 0, 255)):
    frame = np.zeros((240, 320, 3), dtype=np.uint8)
    for rect in rects or []:
        x, y, w, h = rect
        frame[y:y + h, x:x + w] = color
    return frame


def assert_true(condition, message):
    if not condition:
        raise AssertionError(message)
    print(f"[APP-VERIFY] PASS: {message}", flush=True)


def main() -> int:
    os.chdir(APP_DIR)
    app = QApplication(sys.argv)
    window = TrackingApp()

    sentry = getattr(window, "sentry_v2_tab", None)
    assert_true(sentry is not None, "Smart Sentry v2 tab exists in the app")

    cfg = sentry.config
    assert_true(cfg.detection_mode.detection_mode == 10, "app loads motion-locked filtered mode by default")
    assert_true(cfg.detection_mode.color_preset == "any", "app loads neutral color preset by default")
    assert_true(cfg.target_filter.allowed_classes == [], "app loads no class restriction by default")
    assert_true(cfg.engagement.single_target_only is True, "app loads single-target-only engagement")
    assert_true(cfg.engagement.max_queue_length == 1, "app loads queue length capped at one")
    assert_true(cfg.show_threat_scores is False, "app loads overlay score clutter disabled")
    assert_true(cfg.show_engagement_zone is False, "app loads engagement zone overlay disabled")

    sentry.set_enabled(True)
    app.processEvents()

    blank = make_frame()
    moving = make_frame([(40, 50, 40, 40)])
    stopped = make_frame([(40, 50, 40, 40)])
    two_movers = make_frame([(30, 40, 40, 40), (190, 60, 45, 45)])

    sentry.process_frame(blank, None, use_internal_detector=True)
    app.processEvents()
    assert_true(len(sentry.engine.last_targets) == 0, "shared-feed path ignores the initial static frame")

    sentry.process_frame(moving, None, use_internal_detector=True)
    app.processEvents()
    assert_true(len(sentry.engine.last_targets) >= 1, "shared-feed path detects a moving object")
    primary = sentry.overlay._get_primary_target(sentry.engine)
    assert_true(primary is not None, "overlay resolves a single primary target when motion is present")

    sentry.process_frame(stopped, None, use_internal_detector=True)
    app.processEvents()
    assert_true(len(sentry.engine.last_targets) == 0, "shared-feed path drops the target once motion stops")

    sentry._detector.reset()
    sentry._tracker.reset()
    sentry.engine.stop()
    sentry.engine.start()
    app.processEvents()

    sentry.process_frame(blank, None, use_internal_detector=True)
    sentry.process_frame(two_movers, None, use_internal_detector=True)
    app.processEvents()
    queue_length = len(sentry.engine.last_queue)
    assert_true(queue_length <= 1, "engagement queue stays limited to one target in the live app path")

    sentry.set_enabled(False)
    app.processEvents()
    try:
        window.close()
    finally:
        app.quit()
    print("[APP-VERIFY] ALL CHECKS PASSED", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
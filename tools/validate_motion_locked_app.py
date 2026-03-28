import os
import sys

import numpy as np


os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")
os.environ.setdefault("CUDA_VISIBLE_DEVICES", "")


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_DIR = os.path.join(REPO_ROOT, "app")
if APP_DIR not in sys.path:
    sys.path.insert(0, APP_DIR)


def _preload_torch_runtime() -> None:
    try:
        import torch  # noqa: F401
    except Exception as exc:
        print(f"[BOOT] Torch preload failed: {exc}", flush=True)


_preload_torch_runtime()


from PyQt5.QtWidgets import QApplication

from sentry_v2.sentry_v2_config import SentryV2Config
from run_sentry_v2 import SentryV2StandaloneWindow


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
    os.chdir(REPO_ROOT)
    app = QApplication(sys.argv)
    window = SentryV2StandaloneWindow()

    sentry = getattr(window, "sentry_v2_tab", None)
    assert_true(sentry is not None, "Smart Sentry v2 tab exists in the standalone window")
    assert_true(sentry._get_main_window() is None, "standalone launcher registers no host main window")

    cfg = sentry.config
    fallback_cfg = SentryV2Config.from_dict({})
    assert_true(fallback_cfg.connection.camera_source == "0", "blank config falls back to standalone camera source 0")
    assert_true(fallback_cfg.engagement.single_target_only is True, "blank config keeps single-target-only engagement enabled")
    assert_true(fallback_cfg.show_threat_scores is False, "blank config keeps overlay score clutter disabled")
    assert_true(fallback_cfg.show_engagement_zone is False, "blank config keeps engagement zone overlay disabled")
    assert_true(cfg.engagement.single_target_only is True, "standalone runtime keeps single-target-only engagement enabled")
    assert_true(cfg.engagement.max_queue_length == 1, "standalone runtime keeps queue length capped at one")

    sentry._combo_detection_mode.blockSignals(True)
    sentry._combo_detection_mode.setCurrentIndex(10)
    sentry._combo_detection_mode.blockSignals(False)
    sentry._on_detection_mode_changed(10)
    sentry.config.detection_mode.color_preset = "any"
    sentry._detector.color_preset = "any"
    sentry._detector.reset()
    sentry._tracker.reset()

    sentry.set_enabled(True)
    app.processEvents()
    if getattr(sentry, "_cam_timer", None) is not None:
        sentry._cam_timer.stop()
    if getattr(sentry, "_cap", None) is not None:
        try:
            sentry._cap.release()
        except Exception:
            pass
        sentry._cap = None
    sentry._detector.reset()
    sentry._detector._motion_suppressed_until = 0.0
    sentry.engine.stop()
    sentry.engine.start()
    app.processEvents()

    blank = make_frame()
    moving = make_frame([(40, 50, 40, 40)])
    stopped = make_frame([(40, 50, 40, 40)])
    two_movers = make_frame([(30, 40, 40, 40), (190, 60, 45, 45)])

    sentry.process_frame(blank, None, use_internal_detector=True)
    app.processEvents()
    assert_true(len(sentry.engine.last_targets) == 0, "standalone path ignores the initial static frame")

    sentry.process_frame(moving, None, use_internal_detector=True)
    app.processEvents()
    assert_true(len(sentry.engine.last_targets) >= 1, "standalone path detects a moving object")
    primary = sentry.overlay._get_primary_target(sentry.engine)
    assert_true(primary is not None, "overlay resolves a single primary target when motion is present")

    sentry.process_frame(stopped, None, use_internal_detector=True)
    app.processEvents()
    assert_true(len(sentry.engine.last_targets) == 0, "standalone path drops the target once motion stops")

    sentry._detector.reset()
    sentry._tracker.reset()
    sentry.engine.stop()
    sentry.engine.start()
    app.processEvents()

    sentry.process_frame(blank, None, use_internal_detector=True)
    sentry.process_frame(two_movers, None, use_internal_detector=True)
    app.processEvents()
    queue_length = len(sentry.engine.last_queue)
    assert_true(queue_length <= 1, "engagement queue stays limited to one target in the standalone app path")

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
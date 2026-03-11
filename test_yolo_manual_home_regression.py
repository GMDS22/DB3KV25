#!/usr/bin/env python
"""
Regression test: YOLO modes must respect manual movement + Go Home ownership.

Covers detection modes with YOLO involvement:
  - 2: YOLO
  - 4: Hybrid FrameDiff + YOLO
  - 5: Hybrid BackSub + YOLO
  - 9: Hybrid Color + YOLO

What this validates:
  1) While operator hold is active, YOLO detections must NOT auto-enable tracking.
  2) After hold expires, YOLO detections may auto-enable tracking.
  3) Manual move sets operator hold and blocks YOLO overwrite of target pan/tilt.
  4) Go Home completes and preserves coherent tracking/aiming state restoration.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import numpy as np
from PyQt5.QtWidgets import QApplication

BASE_DIR = Path(__file__).resolve().parent
APP_DIR = BASE_DIR / "app"
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from MAIN_FILE_SINGLE_CAM import TrackingApp  # noqa: E402


class TestFailure(Exception):
    pass


class _YoloStub:
    def __init__(self) -> None:
        self.model_loaded = True
        self.model_name = "stub.pt"

    def detect(self, frame, conf=0.5):
        return [(120, 90, 80, 80)]

    def set_target_classes(self, _classes):
        return None

    def load_model(self, _name):
        self.model_loaded = True
        return True

    def find_models(self):
        return ["stub.pt"]


def _pump(app: QApplication, ms: int = 30) -> None:
    end = time.time() + (ms / 1000.0)
    while time.time() < end:
        app.processEvents()


def _set_mode(app_obj: TrackingApp, mode_index: int) -> None:
    app_obj.detection_mode_combo.setCurrentIndex(mode_index)
    try:
        app_obj.on_detection_mode_change(mode_index)
    except Exception:
        pass


def _assert(cond: bool, msg: str) -> None:
    if not cond:
        raise TestFailure(msg)


def run() -> int:
    qapp = QApplication([])
    w = TrackingApp()

    try:
        try:
            if getattr(w, "timer", None) is not None:
                w.timer.stop()
        except Exception:
            pass

        # No hardware side effects in test
        w.send_serial_command = lambda *a, **k: None

        # Stable frame source with deliberate motion between frame1/frame2.
        black = np.zeros((480, 640, 3), dtype=np.uint8)
        white = np.full((480, 640, 3), 255, dtype=np.uint8)
        frames = [black, white]
        state = {"i": 0}

        def cap_read():
            arr = frames[state["i"] % 2].copy()
            state["i"] += 1
            return True, arr

        w._cap_read = cap_read

        # Force YOLO path availability (deterministic stub avoids DLL/runtime variance)
        w.auto_tracking_enabled = True
        w._user_initiated_stop = False
        w.speed_threaded_yolo = False
        w.yolo_detector = _YoloStub()
        try:
            if getattr(w, "yolo_model_combo", None) is not None:
                if w.yolo_model_combo.findText("stub.pt") < 0:
                    w.yolo_model_combo.addItem("stub.pt")
                w.yolo_model_combo.setCurrentText("stub.pt")
        except Exception:
            pass

        # Make mode-4 gate easier to satisfy
        try:
            if getattr(w, "motion_gate_threshold_input", None) is not None:
                w.motion_gate_threshold_input.setValue(0.0)
        except Exception:
            pass

        # Keep mode-5 from waiting long warmup
        w.backsub_warmup = 0

        yolo_modes = [2, 4, 5, 9]

        print("=== YOLO Mode Ownership Regression ===")
        for mode in yolo_modes:
            _set_mode(w, mode)

            # 1) During operator hold, detection must not auto-enable tracking
            w.tracking_active = False
            w.aiming_active = False
            w._operator_control_until = time.time() + 8.0
            for _ in range(2):
                w.update_frame()
                _pump(qapp, 10)

            _assert(
                not bool(w.tracking_active),
                f"Mode {mode}: tracking auto-enabled during operator hold",
            )

            # 2) After hold expires, detection may auto-enable tracking
            w._operator_control_until = time.time() - 0.1
            resumed = False
            for _ in range(10):
                w.update_frame()
                _pump(qapp, 15)
                if bool(w.tracking_active) and bool(w.aiming_active):
                    resumed = True
                    break
            _assert(resumed, f"Mode {mode}: tracking did not resume after hold expired")
            print(f"PASS mode {mode}: hold blocks, then resume works")

        # 3) Manual movement must set hold and prevent overwrite while active
        _set_mode(w, 2)
        w.tracking_active = True
        w.aiming_active = True
        pan_before = float(w.target_pan)
        w.move_manual(pan=10, tilt=0)
        _assert(float(w._operator_control_until) > time.time(), "Manual move did not set operator hold")
        pan_after_manual = float(w.target_pan)
        _assert(pan_after_manual != pan_before, "Manual move did not update target pan")

        # Let detections run while hold active; pan should remain manual-owned
        for _ in range(4):
            w.update_frame()
            _pump(qapp, 15)
        pan_after_updates = float(w.target_pan)
        _assert(
            abs(pan_after_updates - pan_after_manual) < 0.75,
            f"Manual target overwritten during hold (manual={pan_after_manual:.2f}, after={pan_after_updates:.2f})",
        )
        print("PASS manual ownership: pan remains stable during operator hold")

        # 4) Go Home must complete and keep coherent state restoration
        w._go_home_prev_tracking = True
        w._go_home_prev_aiming = True
        w._user_initiated_stop = False
        w.go_home()

        done = False
        t0 = time.time()
        while time.time() - t0 < 4.5:
            _pump(qapp, 20)
            if not bool(getattr(w, "_in_go_home", False)):
                done = True
                break

        _assert(done, "Go Home did not complete")
        _assert(bool(w.tracking_active), "Tracking not active after Go Home completion")
        _assert(bool(w.aiming_active), "Aiming not active after Go Home completion")
        _assert(float(getattr(w, "_operator_control_until", 0.0)) > time.time(), "Operator hold not refreshed by Go Home")
        print("PASS go_home ownership: completed + coherent restore")

        print("\nREGRESSION_PASS: YOLO manual/home ownership is stable across modes")
        return 0

    except TestFailure as e:
        print(f"REGRESSION_FAIL: {e}")
        return 1
    except Exception as e:
        print(f"REGRESSION_ERROR: {e}")
        return 2
    finally:
        try:
            w.close()
        except Exception:
            pass
        try:
            qapp.quit()
        except Exception:
            pass


if __name__ == "__main__":
    raise SystemExit(run())

"""
Smart Sentry v2 — Standalone Detector

Self-contained detection pipeline supporting all 11 detection modes,
independent of the main application's detection code.

Modes:
    0  Frame Difference
    1  Background Subtraction (MOG2)
    2  YOLO Object Detection
    3  Hybrid: Frame Diff + BackSub
    4  Hybrid: Frame Diff + YOLO
    5  Hybrid: BackSub + YOLO
    6  Color Detection
    7  Hybrid: Color + Frame Diff
    8  Hybrid: Color + BackSub
    9  Hybrid: Color + YOLO
   10  Filtered Target Mode (YOLO with class filter)
"""

from __future__ import annotations

import os
import time
from typing import Dict, List, Optional, Tuple, Any

import cv2
import numpy as np


CLASS_ID_MOTION = -1
CLASS_ID_FOREGROUND = -2
CLASS_ID_COLOR = -3
CLASS_ID_MOVING_OBJECT = -4


# ---------------------------------------------------------------------------
#  Color presets (HSV ranges)
# ---------------------------------------------------------------------------
COLOR_PRESETS: Dict[str, Dict[str, Any]] = {
    "any": {"ranges": []},
    "red": {
        "ranges": [
            {"lower": (0, 100, 100), "upper": (10, 255, 255)},
            {"lower": (160, 100, 100), "upper": (179, 255, 255)},
        ],
    },
    "orange": {"ranges": [{"lower": (10, 100, 100), "upper": (25, 255, 255)}]},
    "yellow": {"ranges": [{"lower": (25, 100, 100), "upper": (35, 255, 255)}]},
    "green": {"ranges": [{"lower": (35, 100, 100), "upper": (85, 255, 255)}]},
    "blue": {"ranges": [{"lower": (85, 100, 100), "upper": (130, 255, 255)}]},
    "purple": {"ranges": [{"lower": (130, 100, 100), "upper": (160, 255, 255)}]},
    "cyan": {"ranges": [{"lower": (80, 100, 100), "upper": (100, 255, 255)}]},
    "white": {"ranges": [{"lower": (0, 0, 200), "upper": (179, 40, 255)}]},
    "black": {"ranges": [{"lower": (0, 0, 0), "upper": (179, 255, 40)}]},
}


class SentryV2Detector:
    """Self-contained multi-mode detector for Smart Sentry v2."""

    def __init__(self) -> None:
        # Frame-diff state
        self._prev_frame: Optional[np.ndarray] = None

        # Background subtractor (lazy init)
        self._back_sub: Optional[cv2.BackgroundSubtractorMOG2] = None
        self._backsub_warmup: int = 0
        self._BACKSUB_WARMUP_FRAMES: int = 30

        # YOLO (lazy init)
        self._yolo_model = None
        self._yolo_loaded: bool = False
        self._yolo_model_path: str = ""
        self._yolo_target_classes: List[str] = ["person"]

        # Detection parameters
        self.blur_kernel: int = 5
        self.threshold: int = 40
        self.dilate_iters: int = 2
        self.min_contour: float = 300.0
        self.max_contour: float = 1_400_000.0
        self.yolo_confidence: float = 0.5
        self.yolo_min_area: float = 0.0

        # Color detection
        self.color_preset: str = "any"
        self.color_blur: int = 5
        self.color_morph_iters: int = 2
        self.color_min_area: float = 300.0
        self.color_max_area: float = 500_000.0
        self.custom_hsv_lower: Tuple[int, int, int] = (0, 100, 100)
        self.custom_hsv_upper: Tuple[int, int, int] = (179, 255, 255)

        # Motion gate threshold (for hybrids that gate on motion first)
        self.motion_gate_threshold: float = 1.0
        self.color_fusion_overlap: int = 15
        self._motion_suppressed_until: float = 0.0

    # ------------------------------------------------------------------ #
    #  YOLO management
    # ------------------------------------------------------------------ #

    def load_yolo(self, model_path: str) -> bool:
        """Load a YOLO model from *model_path*. Returns True on success."""
        if self._yolo_loaded and self._yolo_model_path == model_path:
            return True
        try:
            # Environment prep for Windows
            if os.name == "nt":
                os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")
                os.environ.setdefault("OMP_NUM_THREADS", "1")
            from ultralytics import YOLO  # lazy import
            self._yolo_model = YOLO(model_path)
            self._yolo_model_path = model_path
            self._yolo_loaded = True
            return True
        except Exception as e:
            print(f"[SENTRY_V2_DET] YOLO load failed: {e}")
            self._yolo_loaded = False
            return False

    def set_yolo_classes(self, classes: str) -> None:
        """Set target classes from comma-separated string."""
        self._yolo_target_classes = [
            c.strip().lower() for c in classes.split(",") if c.strip()
        ]

    # ------------------------------------------------------------------ #
    #  Main entry point
    # ------------------------------------------------------------------ #

    def detect(
        self, frame: np.ndarray, mode: int,
    ) -> List[Tuple[int, int, int, int, float, int]]:
        """Run detection on *frame* using the specified *mode*.

        Returns list of ``(x, y, w, h, score, class_id)`` tuples.
        """
        if frame is None:
            return []
        if mode == 0:
            return self._detect_frame_diff(frame)
        elif mode == 1:
            return self._detect_backsub(frame)
        elif mode == 2:
            return self._detect_yolo(frame)
        elif mode == 3:
            return self._detect_hybrid_diff_backsub(frame)
        elif mode == 4:
            return self._detect_hybrid_diff_yolo(frame)
        elif mode == 5:
            return self._detect_hybrid_backsub_yolo(frame)
        elif mode == 6:
            return self._detect_color(frame)
        elif mode == 7:
            return self._detect_hybrid_color_diff(frame)
        elif mode == 8:
            return self._detect_hybrid_color_backsub(frame)
        elif mode == 9:
            return self._detect_hybrid_color_yolo(frame)
        elif mode == 10:
            return self._detect_motion_locked_filtered(frame)
        return []

    def suppress_motion(self, seconds: float) -> None:
        self._motion_suppressed_until = max(
            self._motion_suppressed_until,
            time.time() + max(0.0, seconds),
        )

    def _motion_detection_suppressed(self) -> bool:
        return time.time() < self._motion_suppressed_until

    # ------------------------------------------------------------------ #
    #  Frame Difference  (mode 0)
    # ------------------------------------------------------------------ #

    def _detect_frame_diff(self, frame: np.ndarray) -> list:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if self._motion_detection_suppressed():
            self._prev_frame = gray.copy()
            return []
        if self._prev_frame is None:
            self._prev_frame = gray
            return []
        diff = cv2.absdiff(self._prev_frame, gray)
        self._prev_frame = gray.copy()

        k = self.blur_kernel | 1  # force odd
        blur = cv2.GaussianBlur(diff, (k, k), 0)
        _, thresh = cv2.threshold(blur, self.threshold, 255, cv2.THRESH_BINARY)

        kernel = np.ones((3, 3), np.uint8)
        opened = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
        dilated = cv2.dilate(opened, kernel, iterations=self.dilate_iters)

        contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return self._contours_to_boxes(contours, score=0.62, class_id=CLASS_ID_MOTION)

    # ------------------------------------------------------------------ #
    #  Background Subtraction  (mode 1)
    # ------------------------------------------------------------------ #

    def _detect_backsub(self, frame: np.ndarray) -> list:
        if self._back_sub is None:
            self._back_sub = cv2.createBackgroundSubtractorMOG2()
            self._backsub_warmup = 0

        mask = self._back_sub.apply(frame)
        if self._motion_detection_suppressed():
            return []
        self._backsub_warmup += 1
        if self._backsub_warmup < self._BACKSUB_WARMUP_FRAMES:
            return []

        kernel = np.ones((3, 3), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return self._contours_to_boxes(contours, score=0.7, class_id=CLASS_ID_FOREGROUND)

    # ------------------------------------------------------------------ #
    #  YOLO  (modes 2, 10)
    # ------------------------------------------------------------------ #

    def _detect_yolo(self, frame: np.ndarray) -> list:
        if not self._yolo_loaded or self._yolo_model is None:
            return []
        results = self._yolo_model(frame, stream=True, verbose=False)
        model_names = getattr(self._yolo_model, "names", {})
        target_set = set(self._yolo_target_classes) if self._yolo_target_classes else set()
        available = set()
        if isinstance(model_names, dict):
            available = {str(v).strip().lower() for v in model_names.values()}
        use_filter = bool(target_set) and bool(target_set & available)

        boxes: list = []
        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                cls_name = model_names.get(cls_id, "unknown")
                if isinstance(cls_name, str):
                    cls_name = cls_name.lower()
                conf = float(box.conf[0])
                if conf < self.yolo_confidence:
                    continue
                if use_filter and cls_name not in target_set:
                    continue
                x1, y1, x2, y2 = box.xyxy[0]
                w = int(x2 - x1)
                h = int(y2 - y1)
                area = w * h
                if area < self.yolo_min_area:
                    continue
                boxes.append((int(x1), int(y1), w, h, conf, cls_id))
        return boxes

    # ------------------------------------------------------------------ #
    #  Color Detection  (mode 6)
    # ------------------------------------------------------------------ #

    def _detect_color(self, frame: np.ndarray) -> list:
        if self.color_preset in ("", "any"):
            return []
        k = self.color_blur | 1
        blurred = cv2.GaussianBlur(frame, (k, k), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        combined_mask = np.zeros(hsv.shape[:2], dtype=np.uint8)

        if self.color_preset == "custom":
            lower = np.array(self.custom_hsv_lower, dtype=np.uint8)
            upper = np.array(self.custom_hsv_upper, dtype=np.uint8)
            combined_mask = cv2.inRange(hsv, lower, upper)
        elif self.color_preset in COLOR_PRESETS:
            preset = COLOR_PRESETS[self.color_preset]
            for r in preset["ranges"]:
                lower = np.array(r["lower"], dtype=np.uint8)
                upper = np.array(r["upper"], dtype=np.uint8)
                m = cv2.inRange(hsv, lower, upper)
                combined_mask = cv2.bitwise_or(combined_mask, m)

        kernel = np.ones((3, 3), np.uint8)
        cleaned = cv2.morphologyEx(combined_mask, cv2.MORPH_OPEN, kernel, iterations=1)
        cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_CLOSE, kernel, iterations=self.color_morph_iters)

        contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return self._contours_to_boxes(contours,
                                       min_area=self.color_min_area,
                                       max_area=self.color_max_area,
                                       score=0.85,
                                       class_id=CLASS_ID_COLOR)

    # ------------------------------------------------------------------ #
    #  Hybrid modes
    # ------------------------------------------------------------------ #

    def _has_motion_diff(self, frame: np.ndarray) -> bool:
        """Quick frame-diff motion gate — returns True if motion exceeds threshold."""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if self._prev_frame is None:
            self._prev_frame = gray
            return False
        diff = cv2.absdiff(self._prev_frame, gray)
        self._prev_frame = gray.copy()
        score = float(np.sum(diff)) / diff.size
        return score > (self.motion_gate_threshold / 100.0)

    def _detect_hybrid_diff_backsub(self, frame: np.ndarray) -> list:
        diff_boxes = self._detect_frame_diff(frame)
        backsub_boxes = self._detect_backsub(frame)
        return self._merge_boxes(diff_boxes, backsub_boxes)

    def _detect_hybrid_diff_yolo(self, frame: np.ndarray) -> list:
        diff_boxes = self._detect_frame_diff(frame)
        if not diff_boxes:
            return []
        return self._detect_yolo(frame) or diff_boxes

    def _detect_hybrid_backsub_yolo(self, frame: np.ndarray) -> list:
        backsub_boxes = self._detect_backsub(frame)
        if not backsub_boxes:
            return []
        return self._detect_yolo(frame) or backsub_boxes

    def _detect_hybrid_color_diff(self, frame: np.ndarray) -> list:
        color_boxes = self._detect_color(frame)
        diff_boxes = self._detect_frame_diff(frame)
        return self._merge_boxes(color_boxes, diff_boxes)

    def _detect_hybrid_color_backsub(self, frame: np.ndarray) -> list:
        color_boxes = self._detect_color(frame)
        backsub_boxes = self._detect_backsub(frame)
        return self._merge_boxes(color_boxes, backsub_boxes)

    def _detect_hybrid_color_yolo(self, frame: np.ndarray) -> list:
        color_boxes = self._detect_color(frame)
        if not color_boxes:
            return []
        return self._detect_yolo(frame) or color_boxes

    def _detect_motion_locked_filtered(self, frame: np.ndarray) -> list:
        motion_boxes = self._merge_boxes(
            self._detect_frame_diff(frame),
            self._detect_backsub(frame),
        )
        if not motion_boxes:
            return []

        require_color = self.color_preset not in ("", "any")
        color_boxes = self._detect_color(frame) if require_color else []

        if not self._yolo_loaded or self._yolo_model is None:
            return []
        yolo_boxes = self._detect_yolo(frame)
        if not yolo_boxes:
            return []

        filtered: list = []
        for motion_box in motion_boxes:
            mx, my, mw, mh, motion_score, _ = motion_box
            motion_rect = (mx, my, mw, mh)

            if require_color:
                color_match = False
                for color_box in color_boxes:
                    overlap = self._bbox_overlap_ratio(motion_rect, color_box[:4])
                    if overlap >= max(0.05, self.color_fusion_overlap / 100.0):
                        color_match = True
                        break
                if not color_match:
                    continue

            best_cls = None
            best_overlap = 0.0
            for yolo_box in yolo_boxes:
                overlap = self._bbox_overlap_ratio(motion_rect, yolo_box[:4])
                if overlap >= 0.15 and overlap > best_overlap:
                    best_overlap = overlap
                    best_cls = yolo_box
            if best_cls is None:
                continue

            yx, yy, yw, yh = (int(best_cls[0]), int(best_cls[1]), int(best_cls[2]), int(best_cls[3]))
            score = max(float(motion_score), float(best_cls[4]))
            class_id = int(best_cls[5]) if len(best_cls) >= 6 else CLASS_ID_MOVING_OBJECT

            # Motion gates whether the target is eligible; YOLO supplies the
            # box used for aiming because it is materially more stable.
            filtered.append((yx, yy, yw, yh, score, class_id))

        return filtered

    # ------------------------------------------------------------------ #
    #  Helpers
    # ------------------------------------------------------------------ #

    def _contours_to_boxes(
        self, contours, *, min_area: float = -1, max_area: float = -1,
        score: float = 1.0, class_id: int = 0,
    ) -> list:
        mn = min_area if min_area >= 0 else self.min_contour
        mx = max_area if max_area >= 0 else self.max_contour
        boxes = []
        for c in contours:
            a = cv2.contourArea(c)
            if mn < a < mx:
                x, y, w, h = cv2.boundingRect(c)
                boxes.append((x, y, w, h, score, class_id))
        return boxes

    @staticmethod
    def _merge_boxes(a: list, b: list) -> list:
        """Merge two box lists, dropping near-duplicates."""
        if not a:
            return b
        if not b:
            return a
        merged = list(a)
        for bx in b:
            dup = False
            for ax in a:
                if abs(bx[0] - ax[0]) < 20 and abs(bx[1] - ax[1]) < 20:
                    dup = True
                    break
            if not dup:
                merged.append(bx)
        return merged

    @staticmethod
    def _bbox_overlap_ratio(a: tuple, b: tuple) -> float:
        ax, ay, aw, ah = a
        bx, by, bw, bh = b
        ax2, ay2 = ax + aw, ay + ah
        bx2, by2 = bx + bw, by + bh

        ix1 = max(ax, bx)
        iy1 = max(ay, by)
        ix2 = min(ax2, bx2)
        iy2 = min(ay2, by2)
        iw = max(0, ix2 - ix1)
        ih = max(0, iy2 - iy1)
        inter = iw * ih
        if inter <= 0:
            return 0.0
        area_a = max(1, aw * ah)
        return inter / area_a

    def reset(self) -> None:
        """Reset stateful detectors (call when mode changes or on enable)."""
        self._prev_frame = None
        self._back_sub = None
        self._backsub_warmup = 0

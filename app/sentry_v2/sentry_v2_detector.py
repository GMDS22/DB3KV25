"""
SMART SENTRY V3 — Standalone Detector

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
            {"lower": (0, 80, 80), "upper": (10, 255, 255)},
            {"lower": (165, 80, 80), "upper": (179, 255, 255)},
        ],
    },
    "orange": {"ranges": [{"lower": (10, 80, 90), "upper": (25, 255, 255)}]},
    "yellow": {"ranges": [{"lower": (20, 85, 100), "upper": (36, 255, 255)}]},
    "green": {"ranges": [{"lower": (35, 75, 80), "upper": (80, 255, 255)}]},
    "blue": {"ranges": [{"lower": (100, 80, 80), "upper": (126, 255, 255)}]},
    "purple": {"ranges": [{"lower": (130, 80, 80), "upper": (160, 255, 255)}]},
    "cyan": {"ranges": [{"lower": (81, 80, 80), "upper": (99, 255, 255)}]},
    "white": {"ranges": [{"lower": (0, 0, 185), "upper": (179, 55, 255)}]},
    "black": {"ranges": [{"lower": (0, 0, 0), "upper": (179, 140, 70)}]},
        "grey": {"ranges": [{"lower": (0, 0, 45), "upper": (179, 45, 190)}]},
}

COLOR_TOLERANCE_BY_PRESET: Dict[str, Dict[str, int]] = {
    "red": {"s": 28, "v": 28},
    "orange": {"s": 18, "v": 20},
    "yellow": {"s": 16, "v": 18},
    "green": {"s": 16, "v": 16},
    "blue": {"s": 24, "v": 24},
    "purple": {"s": 28, "v": 28},
    "cyan": {"s": 26, "v": 24},
    "white": {"s": 18, "v": 18},
    "black": {"s": 10, "v": 10},
}


class SentryV2Detector:
    """Self-contained multi-mode detector for SMART SENTRY V3."""

    def __init__(self) -> None:
        # Frame-diff state
        self._prev_frame: Optional[np.ndarray] = None
        # Resize acceleration is intentionally limited to pure motion-only modes.
        # Hybrid modes keep full-resolution gating to avoid small-target regressions.
        self._motion_resize_max_dim: int = 960
        self._morph_kernel = np.ones((3, 3), np.uint8)

        # Background subtractor (lazy init)
        self._back_sub: Optional[cv2.BackgroundSubtractorMOG2] = None
        self._backsub_warmup: int = 0
        self._BACKSUB_WARMUP_FRAMES: int = 30
        self._BACKSUB_HISTORY: int = 120
        self._BACKSUB_VAR_THRESHOLD: float = 36.0

        # YOLO (lazy init)
        self._yolo_model = None
        self._yolo_loaded: bool = False
        self._yolo_model_path: str = ""
        self._last_error: str = ""
        self._yolo_target_classes: List[str] = ["person"]
        self._yolo_infer_max_dim: int = 1280

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
        self.color_fusion_strategy: str = "AND"
        self.custom_hsv_lower: Tuple[int, int, int] = (0, 100, 100)
        self.custom_hsv_upper: Tuple[int, int, int] = (179, 255, 255)

        # Motion gate threshold (for hybrids that gate on motion first)
        self.motion_gate_threshold: float = 1.0
        self.color_fusion_overlap: int = 15
        self._motion_suppressed_until: float = 0.0
        self._last_color_gate_status: Dict[str, Any] = {}

    # ------------------------------------------------------------------ #
    #  YOLO management
    # ------------------------------------------------------------------ #

    def load_yolo(self, model_path: str) -> bool:
        """Load a YOLO model from *model_path*. Returns True on success."""
        model_path = os.path.abspath(model_path)
        if self._yolo_loaded and self._yolo_model_path == model_path:
            self._last_error = ""
            return True
        try:
            if not os.path.isfile(model_path):
                raise FileNotFoundError(model_path)
            # Environment prep for Windows
            if os.name == "nt":
                os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")
                os.environ.setdefault("OMP_NUM_THREADS", "1")
            from ultralytics import YOLO  # lazy import
            self._yolo_model = YOLO(model_path)
            self._yolo_model_path = model_path
            self._yolo_loaded = True
            self._last_error = ""
            return True
        except Exception as e:
            self._last_error = str(e)
            print(f"[SENTRY_V2_DET] YOLO load failed: {e}")
            self._yolo_loaded = False
            self._yolo_model_path = ""
            return False

    def set_yolo_classes(self, classes: str) -> None:
        """Set target classes from comma-separated string."""
        self._yolo_target_classes = [
            c.strip().lower() for c in classes.split(",") if c.strip()
        ]

    def _prepare_yolo_frame(self, frame: np.ndarray) -> tuple[np.ndarray, float]:
        h, w = frame.shape[:2]
        max_dim = max(h, w)
        if max_dim <= int(self._yolo_infer_max_dim):
            return frame, 1.0
        scale = float(self._yolo_infer_max_dim) / float(max_dim)
        resized = cv2.resize(frame, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
        return resized, scale

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
        if mode not in (6, 7, 8, 9, 10):
            self._last_color_gate_status = {}
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
            result = self._detect_color(frame)
            self._set_color_gate_status(
                mode=6,
                color_boxes=len(result),
                gate_boxes=len(result),
                final_boxes=len(result),
            )
            return result
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

    def get_last_color_gate_status(self) -> Dict[str, Any]:
        return dict(self._last_color_gate_status)

    def _motion_detection_suppressed(self) -> bool:
        return time.time() < self._motion_suppressed_until

    def _prepare_motion_frame(
        self,
        frame: np.ndarray,
        *,
        allow_resize: bool = True,
    ) -> tuple[np.ndarray, float]:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        h, w = gray.shape[:2]
        max_dim = max(h, w)
        if not allow_resize or max_dim <= self._motion_resize_max_dim:
            return gray, 1.0
        scale = float(self._motion_resize_max_dim) / float(max_dim)
        resized = cv2.resize(gray, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
        return resized, scale

    def _prepare_backsub_frame(
        self,
        frame: np.ndarray,
        *,
        allow_resize: bool = True,
    ) -> tuple[np.ndarray, float]:
        h, w = frame.shape[:2]
        max_dim = max(h, w)
        if not allow_resize or max_dim <= self._motion_resize_max_dim:
            return frame, 1.0
        scale = float(self._motion_resize_max_dim) / float(max_dim)
        resized = cv2.resize(frame, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
        return resized, scale

    # ------------------------------------------------------------------ #
    #  Frame Difference  (mode 0)
    # ------------------------------------------------------------------ #

    def _detect_frame_diff(self, frame: np.ndarray, *, allow_resize: bool = True) -> list:
        gray, scale = self._prepare_motion_frame(frame, allow_resize=allow_resize)
        if self._motion_detection_suppressed():
            self._prev_frame = gray.copy()
            return []
        if self._prev_frame is not None and self._prev_frame.shape != gray.shape:
            self._prev_frame = gray.copy()
            return []
        if self._prev_frame is None:
            self._prev_frame = gray.copy()
            return []
        diff = cv2.absdiff(self._prev_frame, gray)
        self._prev_frame = gray.copy()

        k = self.blur_kernel | 1  # force odd
        blur = cv2.GaussianBlur(diff, (k, k), 0)
        _, thresh = cv2.threshold(blur, self.threshold, 255, cv2.THRESH_BINARY)

        opened = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, self._morph_kernel, iterations=1)
        dilated = cv2.dilate(opened, self._morph_kernel, iterations=self.dilate_iters)

        contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return self._contours_to_boxes(
            contours,
            score=0.62,
            class_id=CLASS_ID_MOTION,
            frame_shape=frame.shape,
            scale=scale,
        )

    # ------------------------------------------------------------------ #
    #  Background Subtraction  (mode 1)
    # ------------------------------------------------------------------ #

    def _detect_backsub(self, frame: np.ndarray, *, allow_resize: bool = True) -> list:
        if self._back_sub is None:
            self._back_sub = cv2.createBackgroundSubtractorMOG2(
                history=self._BACKSUB_HISTORY,
                varThreshold=self._BACKSUB_VAR_THRESHOLD,
                detectShadows=False,
            )
            self._backsub_warmup = 0

        processing_frame, scale = self._prepare_backsub_frame(frame, allow_resize=allow_resize)
        filtered = cv2.GaussianBlur(processing_frame, (5, 5), 0)
        mask = self._back_sub.apply(filtered)
        if self._motion_detection_suppressed():
            return []
        self._backsub_warmup += 1
        if self._backsub_warmup < self._BACKSUB_WARMUP_FRAMES:
            return []

        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, self._morph_kernel, iterations=1)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, self._morph_kernel, iterations=max(1, self.dilate_iters))
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return self._contours_to_boxes(
            contours,
            score=0.7,
            class_id=CLASS_ID_FOREGROUND,
            frame_shape=frame.shape,
            scale=scale,
        )

    # ------------------------------------------------------------------ #
    #  YOLO  (modes 2, 10)
    # ------------------------------------------------------------------ #

    def _detect_yolo(self, frame: np.ndarray) -> list:
        if not self._yolo_loaded or self._yolo_model is None:
            return []
        infer_frame, infer_scale = self._prepare_yolo_frame(frame)
        results = self._yolo_model(infer_frame, stream=False, verbose=False)
        model_names = getattr(self._yolo_model, "names", {})
        target_set = set(self._yolo_target_classes) if self._yolo_target_classes else set()
        available = set()
        if isinstance(model_names, dict):
            available = {str(v).strip().lower() for v in model_names.values()}
        use_filter = bool(target_set) and bool(target_set & available)
        scale_back = 1.0 / float(infer_scale) if infer_scale > 0.0 else 1.0

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
                if infer_scale != 1.0:
                    x1 = float(x1) * scale_back
                    y1 = float(y1) * scale_back
                    x2 = float(x2) * scale_back
                    y2 = float(y2) * scale_back
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

    def _color_range_with_tolerance(
        self,
        lower: Tuple[int, int, int],
        upper: Tuple[int, int, int],
        *,
        tolerant: bool,
    ) -> Tuple[Tuple[int, int, int], Tuple[int, int, int]]:
        if not tolerant:
            return lower, upper

        lo_h, lo_s, lo_v = lower
        hi_h, hi_s, hi_v = upper
        preset = str(self.color_preset or "").strip().lower()
        tol = COLOR_TOLERANCE_BY_PRESET.get(preset, {"s": 18, "v": 18})
        s_tol = int(tol.get("s", 18))
        v_tol = int(tol.get("v", 18))

        if preset == "white":
            lo_v = max(0, lo_v - v_tol)
            hi_s = min(255, hi_s + s_tol)
        elif preset == "black":
            hi_v = min(255, hi_v + v_tol)
            hi_s = min(255, hi_s + s_tol)
        else:
            lo_s = max(0, lo_s - s_tol)
            lo_v = max(0, lo_v - v_tol)

        return (lo_h, lo_s, lo_v), (hi_h, hi_s, hi_v)

    def _build_color_mask(self, hsv: np.ndarray, *, tolerant: bool) -> np.ndarray:
        combined_mask = np.zeros(hsv.shape[:2], dtype=np.uint8)

        if self.color_preset in ("", "any"):
            lower = np.array((0, 55, 35), dtype=np.uint8)
            upper = np.array((179, 255, 255), dtype=np.uint8)
            return cv2.inRange(hsv, lower, upper)
        if self.color_preset == "custom":
            lower = np.array(self.custom_hsv_lower, dtype=np.uint8)
            upper = np.array(self.custom_hsv_upper, dtype=np.uint8)
            return cv2.inRange(hsv, lower, upper)
        if self.color_preset in COLOR_PRESETS:
            preset = COLOR_PRESETS[self.color_preset]
            for range_cfg in preset["ranges"]:
                lower, upper = self._color_range_with_tolerance(
                    tuple(range_cfg["lower"]),
                    tuple(range_cfg["upper"]),
                    tolerant=tolerant,
                )
                m = cv2.inRange(
                    hsv,
                    np.array(lower, dtype=np.uint8),
                    np.array(upper, dtype=np.uint8),
                )
                combined_mask = cv2.bitwise_or(combined_mask, m)
        return combined_mask

    def _extract_color_boxes(
        self,
        cleaned: np.ndarray,
        *,
        frame_shape: Tuple[int, int, int],
        fill_ratio_min: float,
    ) -> list:
        contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        frame_area = float(max(1, frame_shape[0] * frame_shape[1]))
        boxes: list = []
        for c in contours:
            area = float(cv2.contourArea(c))
            if not (self.color_min_area < area < self.color_max_area):
                continue
            x, y, w, h = cv2.boundingRect(c)
            if w <= 1 or h <= 1:
                continue
            if self.color_preset == "black":
                touches = sum(
                    (
                        x <= 1,
                        y <= 1,
                        (x + w) >= (frame_shape[1] - 1),
                        (y + h) >= (frame_shape[0] - 1),
                    )
                )
                if area >= (frame_area * 0.55):
                    continue
                if touches >= 2 and area >= (frame_area * 0.15):
                    continue
            roi = cleaned[y:y + h, x:x + w]
            if roi.size <= 0:
                continue
            filled = float(cv2.countNonZero(roi)) / float(w * h)
            if filled < fill_ratio_min:
                continue
            boxes.append((int(x), int(y), int(w), int(h), 0.85, CLASS_ID_COLOR))
        return boxes

    def _detect_color(self, frame: np.ndarray) -> list:
        k = self.color_blur | 1
        blurred = cv2.GaussianBlur(frame, (k, k), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        kernel = np.ones((3, 3), np.uint8)
        combined_mask = self._build_color_mask(hsv, tolerant=False)
        cleaned = cv2.morphologyEx(combined_mask, cv2.MORPH_OPEN, kernel, iterations=1)
        cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_CLOSE, kernel, iterations=self.color_morph_iters)

        # Reduce false positives by ensuring enough of each contour box is
        # actually filled by selected-color mask pixels.
        fill_ratio_min = 0.12 if self.color_preset in ("", "any") else 0.22
        boxes = self._extract_color_boxes(
            cleaned,
            frame_shape=frame.shape,
            fill_ratio_min=fill_ratio_min,
        )
        if boxes or self.color_preset in ("", "any", "custom"):
            return boxes

        tolerant_mask = self._build_color_mask(hsv, tolerant=True)
        tolerant_cleaned = cv2.morphologyEx(tolerant_mask, cv2.MORPH_OPEN, kernel, iterations=1)
        tolerant_cleaned = cv2.morphologyEx(
            tolerant_cleaned,
            cv2.MORPH_CLOSE,
            kernel,
            iterations=self.color_morph_iters,
        )
        return self._extract_color_boxes(
            tolerant_cleaned,
            frame_shape=frame.shape,
            fill_ratio_min=max(0.16, fill_ratio_min - 0.04),
        )

    # ------------------------------------------------------------------ #
    #  Hybrid modes
    # ------------------------------------------------------------------ #

    def _has_motion_diff(self, frame: np.ndarray, *, update_prev: bool = True) -> bool:
        """Quick frame-diff motion gate — returns True if motion exceeds threshold."""
        gray, _ = self._prepare_motion_frame(frame, allow_resize=False)
        if self._prev_frame is not None and self._prev_frame.shape != gray.shape:
            if update_prev:
                self._prev_frame = gray.copy()
            return False
        if self._prev_frame is None:
            if update_prev:
                self._prev_frame = gray.copy()
            return False
        diff = cv2.absdiff(self._prev_frame, gray)
        if update_prev:
            self._prev_frame = gray.copy()
        score = float(np.sum(diff)) / diff.size
        return score > (self.motion_gate_threshold / 100.0)

    def _detect_hybrid_diff_backsub(self, frame: np.ndarray) -> list:
        backsub_boxes = self._detect_backsub(frame, allow_resize=False)
        diff_boxes = self._detect_frame_diff(frame, allow_resize=False)
        return self._gate_primary_boxes(backsub_boxes, diff_boxes, min_overlap=0.10)

    def _detect_hybrid_diff_yolo(self, frame: np.ndarray) -> list:
        if not self._has_motion_diff(frame, update_prev=False):
            return []
        diff_boxes = self._detect_frame_diff(frame, allow_resize=False)
        if not diff_boxes:
            return []
        yolo_boxes = self._detect_yolo(frame)
        return self._gate_primary_boxes(yolo_boxes, diff_boxes, min_overlap=0.12)

    def _detect_hybrid_backsub_yolo(self, frame: np.ndarray) -> list:
        backsub_boxes = self._detect_backsub(frame, allow_resize=False)
        if not backsub_boxes:
            return []
        if not self._has_motion_diff(frame):
            return []
        yolo_boxes = self._detect_yolo(frame)
        return self._gate_primary_boxes(yolo_boxes, backsub_boxes, min_overlap=0.12)

    def _detect_hybrid_color_diff(self, frame: np.ndarray) -> list:
        color_boxes = self._detect_color(frame)
        diff_boxes = self._detect_frame_diff(frame, allow_resize=False)
        if self.color_preset not in ("", "any"):
            # In specific-color mode, motion must overlap the selected color.
            result = self._gate_primary_boxes(
                diff_boxes,
                color_boxes,
                min_overlap=max(0.08, self.color_fusion_overlap / 100.0),
            )
            self._set_color_gate_status(
                mode=7,
                color_boxes=len(color_boxes),
                gate_boxes=len(diff_boxes),
                final_boxes=len(result),
            )
            return result
        result = self._fuse_boxes_by_strategy(
            color_boxes,
            diff_boxes,
            min_overlap=max(0.08, self.color_fusion_overlap / 100.0),
        )
        self._set_color_gate_status(
            mode=7,
            color_boxes=len(color_boxes),
            gate_boxes=len(diff_boxes),
            final_boxes=len(result),
        )
        return result

    def _detect_hybrid_color_backsub(self, frame: np.ndarray) -> list:
        color_boxes = self._detect_color(frame)
        backsub_boxes = self._detect_backsub(frame, allow_resize=False)
        if self.color_preset not in ("", "any"):
            # In specific-color mode, foreground motion must overlap selected color.
            result = self._gate_primary_boxes(
                backsub_boxes,
                color_boxes,
                min_overlap=max(0.08, self.color_fusion_overlap / 100.0),
            )
            self._set_color_gate_status(
                mode=8,
                color_boxes=len(color_boxes),
                gate_boxes=len(backsub_boxes),
                final_boxes=len(result),
            )
            return result
        result = self._fuse_boxes_by_strategy(
            color_boxes,
            backsub_boxes,
            min_overlap=max(0.08, self.color_fusion_overlap / 100.0),
        )
        self._set_color_gate_status(
            mode=8,
            color_boxes=len(color_boxes),
            gate_boxes=len(backsub_boxes),
            final_boxes=len(result),
        )
        return result

    def _detect_hybrid_color_yolo(self, frame: np.ndarray) -> list:
        color_boxes = self._detect_color(frame)
        if not color_boxes:
            self._set_color_gate_status(mode=9, color_boxes=0, gate_boxes=0, final_boxes=0)
            return []
        yolo_boxes = self._detect_yolo(frame)
        if not yolo_boxes:
            # Keep color tracking functional when YOLO is unavailable.
            self._set_color_gate_status(
                mode=9,
                color_boxes=len(color_boxes),
                gate_boxes=0,
                final_boxes=len(color_boxes),
            )
            return color_boxes
        min_overlap = max(0.08, self.color_fusion_overlap / 100.0)
        if self.color_preset not in ("", "any"):
            # In specific-color mode, always require YOLO overlap with selected color.
            result = self._gate_primary_boxes(yolo_boxes, color_boxes, min_overlap=min_overlap)
            self._set_color_gate_status(
                mode=9,
                color_boxes=len(color_boxes),
                gate_boxes=len(yolo_boxes),
                final_boxes=len(result),
            )
            return result
        strategy = (self.color_fusion_strategy or "AND").strip().upper()
        if strategy == "OR":
            result = self._merge_boxes(yolo_boxes, color_boxes)
            self._set_color_gate_status(
                mode=9,
                color_boxes=len(color_boxes),
                gate_boxes=len(yolo_boxes),
                final_boxes=len(result),
            )
            return result
        result = self._gate_primary_boxes(yolo_boxes, color_boxes, min_overlap=min_overlap)
        self._set_color_gate_status(
            mode=9,
            color_boxes=len(color_boxes),
            gate_boxes=len(yolo_boxes),
            final_boxes=len(result),
        )
        return result

    def _detect_motion_locked_filtered(self, frame: np.ndarray) -> list:
        motion_boxes = self._merge_boxes(
            self._detect_frame_diff(frame, allow_resize=False),
            self._detect_backsub(frame, allow_resize=False),
        )
        if not motion_boxes:
            return []

        require_color = self.color_preset not in ("", "any")
        color_boxes = self._detect_color(frame) if require_color else []

        yolo_boxes = self._detect_yolo(frame) if (self._yolo_loaded and self._yolo_model is not None) else []

        filtered: list = []
        for motion_box in motion_boxes:
            mx, my, mw, mh, motion_score, _ = motion_box
            motion_rect = (mx, my, mw, mh)

            if require_color:
                color_match = False
                for color_box in color_boxes:
                    if self._boxes_overlap(
                        motion_rect,
                        color_box[:4],
                        min_overlap=max(0.05, self.color_fusion_overlap / 100.0),
                    ):
                        color_match = True
                        break
                if not color_match:
                    continue

            best_cls = None
            best_overlap = 0.0
            for yolo_box in yolo_boxes:
                overlap = max(
                    self._bbox_overlap_ratio(motion_rect, yolo_box[:4]),
                    self._bbox_overlap_ratio(yolo_box[:4], motion_rect),
                )
                if overlap >= 0.15 and overlap > best_overlap:
                    best_overlap = overlap
                    best_cls = yolo_box
            if best_cls is None:
                # Fallback to motion/color box if YOLO is unavailable for this frame.
                filtered.append((mx, my, mw, mh, float(motion_score), CLASS_ID_MOVING_OBJECT))
                continue

            yx, yy, yw, yh = (int(best_cls[0]), int(best_cls[1]), int(best_cls[2]), int(best_cls[3]))
            score = max(float(motion_score), float(best_cls[4]))
            class_id = int(best_cls[5]) if len(best_cls) >= 6 else CLASS_ID_MOVING_OBJECT

            # Motion gates whether the target is eligible; YOLO supplies the
            # box used for aiming because it is materially more stable.
            filtered.append((yx, yy, yw, yh, score, class_id))
        self._set_color_gate_status(
            mode=10,
            color_boxes=len(color_boxes),
            gate_boxes=len(motion_boxes),
            final_boxes=len(filtered),
        )
        return filtered

    def _set_color_gate_status(
        self,
        *,
        mode: int,
        color_boxes: int,
        gate_boxes: int,
        final_boxes: int,
    ) -> None:
        self._last_color_gate_status = {
            "mode": int(mode),
            "preset": str(self.color_preset or "any"),
            "strategy": str(self.color_fusion_strategy or "AND"),
            "color_boxes": int(color_boxes),
            "gate_boxes": int(gate_boxes),
            "final_boxes": int(final_boxes),
            "timestamp": time.time(),
        }

    # ------------------------------------------------------------------ #
    #  Helpers
    # ------------------------------------------------------------------ #

    def _contours_to_boxes(
        self, contours, *, min_area: float = -1, max_area: float = -1,
        score: float = 1.0, class_id: int = 0,
        frame_shape: Optional[Tuple[int, int, int]] = None,
        scale: float = 1.0,
    ) -> list:
        mn = min_area if min_area >= 0 else self.min_contour
        mx = max_area if max_area >= 0 else self.max_contour
        boxes = []
        frame_h = int(frame_shape[0]) if frame_shape is not None else 0
        frame_w = int(frame_shape[1]) if frame_shape is not None else 0
        frame_area = float(max(1, frame_h * frame_w)) if frame_h and frame_w else 0.0
        scale_value = float(scale) if scale and scale > 0.0 else 1.0
        area_scale = scale_value * scale_value
        for c in contours:
            a = float(cv2.contourArea(c))
            if area_scale != 1.0:
                a /= area_scale
            if mn < a < mx:
                x, y, w, h = cv2.boundingRect(c)
                if scale_value != 1.0:
                    x = int(round(x / scale_value))
                    y = int(round(y / scale_value))
                    w = int(round(w / scale_value))
                    h = int(round(h / scale_value))
                if w <= 2 or h <= 2:
                    continue
                bbox_area = float(max(1, w * h))
                fill_ratio = a / bbox_area
                if fill_ratio < 0.12:
                    continue
                if frame_area > 0.0:
                    touches = sum(
                        (
                            x <= 1,
                            y <= 1,
                            (x + w) >= (frame_w - 1),
                            (y + h) >= (frame_h - 1),
                        )
                    )
                    if touches >= 2 and bbox_area >= (frame_area * 0.12):
                        continue
                boxes.append((x, y, w, h, score, class_id))
        return boxes

    def _gate_primary_boxes(
        self,
        primary_boxes: list,
        gate_boxes: list,
        *,
        min_overlap: float,
    ) -> list:
        if not primary_boxes or not gate_boxes:
            return []

        gated = []
        for primary_box in primary_boxes:
            if any(self._boxes_overlap(primary_box[:4], gate_box[:4], min_overlap=min_overlap) for gate_box in gate_boxes):
                gated.append(primary_box)
        return gated

    def _fuse_boxes_by_strategy(
        self,
        primary_boxes: list,
        gate_boxes: list,
        *,
        min_overlap: float,
    ) -> list:
        strategy = (self.color_fusion_strategy or "AND").strip().upper()
        if strategy == "OR":
            if not primary_boxes and not gate_boxes:
                return []
            if not primary_boxes:
                return list(gate_boxes)
            if not gate_boxes:
                return list(primary_boxes)
            return self._merge_boxes(primary_boxes, gate_boxes)
        return self._gate_primary_boxes(primary_boxes, gate_boxes, min_overlap=min_overlap)

    def _boxes_overlap(
        self,
        a: tuple,
        b: tuple,
        *,
        min_overlap: float,
    ) -> bool:
        return (
            self._bbox_overlap_ratio(a, b) >= min_overlap
            or self._bbox_overlap_ratio(b, a) >= min_overlap
        )

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
        self._last_color_gate_status = {}

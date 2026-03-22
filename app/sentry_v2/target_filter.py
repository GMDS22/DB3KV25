"""
Smart Sentry v2 — Target Filter

Decides which YOLO detections qualify as engageable targets based on
user-defined criteria (class, confidence, size, zone).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from .sentry_v2_config import TargetFilterConfig


NON_SEMANTIC_CLASSES = {"motion", "foreground", "color", "moving_object"}


@dataclass
class DetectedObject:
    """A single YOLO detection normalised for sentry processing."""
    track_id: int                       # Unique ID (from tracker or index)
    class_name: str                     # YOLO class label
    confidence: float                   # 0-1
    bbox: Tuple[int, int, int, int]     # (x, y, w, h) in pixels
    center_x: float                     # Pixel center x
    center_y: float                     # Pixel center y
    source: str = "yolo"
    frame_width: int = 640
    frame_height: int = 480

    # Derived
    @property
    def area_ratio(self) -> float:
        """Bounding box area as fraction of frame area."""
        _, _, w, h = self.bbox
        return (w * h) / max(1, self.frame_width * self.frame_height)

    @property
    def norm_cx(self) -> float:
        return self.center_x / max(1, self.frame_width)

    @property
    def norm_cy(self) -> float:
        return self.center_y / max(1, self.frame_height)


class TargetFilter:
    """
    Filters raw detections against user-set criteria.

    Usage:
        filt = TargetFilter(config)
        qualified = filt.filter(detections)
    """

    def __init__(self, config: TargetFilterConfig):
        self.cfg = config

    def update_config(self, config: TargetFilterConfig) -> None:
        self.cfg = config

    # ------------------------------------------------------------------ #
    def filter(self, detections: List[DetectedObject]) -> List[DetectedObject]:
        """Return only detections that pass all criteria."""
        return [d for d in detections if self._passes(d)]

    # ------------------------------------------------------------------ #
    def _passes(self, det: DetectedObject) -> bool:
        is_non_semantic = det.class_name in NON_SEMANTIC_CLASSES

        # 1. Class whitelist
        if (
            not is_non_semantic
            and self.cfg.allowed_classes
            and det.class_name not in self.cfg.allowed_classes
        ):
            return False

        # 2. Confidence
        if det.confidence < self.cfg.min_confidence:
            return False

        # 3. Size
        if not is_non_semantic:
            area = det.area_ratio
            if area < self.cfg.min_size_ratio:
                return False
            if self.cfg.max_size_ratio > 0 and area > self.cfg.max_size_ratio:
                return False

        # 4. Engagement zone
        z = self.cfg.engagement_zone
        if not (z[0] <= det.norm_cx <= z[2] and z[1] <= det.norm_cy <= z[3]):
            return False

        return True

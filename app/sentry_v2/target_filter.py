"""
SMART SENTRY V3 — Target Filter

Decides which YOLO detections qualify as engageable targets based on
user-defined criteria (class, confidence, size, zone).
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from .sentry_v2_config import TargetFilterConfig


NON_SEMANTIC_CLASSES = {"motion", "foreground", "color", "moving_object"}

SHAPE_PROFILE_ALIASES = {
    "birds": "bird",
}

SHAPE_FILTER_PROFILES = {
    "rat": {"min_aspect_ratio": 0.85, "max_aspect_ratio": 4.6},
    "car": {"min_aspect_ratio": 1.15, "max_aspect_ratio": 4.8},
    "cat": {"min_aspect_ratio": 0.65, "max_aspect_ratio": 3.2},
    "dog": {"min_aspect_ratio": 0.65, "max_aspect_ratio": 3.6},
    "person": {"min_aspect_ratio": 0.20, "max_aspect_ratio": 1.05},
    "bird": {"min_aspect_ratio": 0.45, "max_aspect_ratio": 2.8},
}


@dataclass
class _SemanticConfirmState:
    class_name: str
    hits: int = 0
    last_seen: float = 0.0


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
    identity_label: str = ""
    identity_confidence: float = 0.0
    identity_profile_id: str = ""
    friendly_identity: bool = False

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
        self._semantic_confirm: dict[int, _SemanticConfirmState] = {}

    def update_config(self, config: TargetFilterConfig) -> None:
        self.cfg = config

    def reset(self) -> None:
        self._semantic_confirm.clear()

    # ------------------------------------------------------------------ #
    def filter(self, detections: List[DetectedObject], timestamp: Optional[float] = None) -> List[DetectedObject]:
        """Return only detections that pass all criteria."""
        now = timestamp or time.time()
        qualified = [d for d in detections if self._passes(d, now)]
        self._prune_confirmation_state(now)
        return qualified

    # ------------------------------------------------------------------ #
    def _passes(self, det: DetectedObject, now: float) -> bool:
        if not self._passes_base(det):
            return False
        return self._passes_semantic_confirmation(det, now)

    def _passes_base(self, det: DetectedObject) -> bool:
        is_prompted = str(getattr(det, "source", "")) == "prompted"
        is_non_semantic = det.class_name in NON_SEMANTIC_CLASSES

        # 1. Class whitelist
        if (
            not is_prompted
            and self.cfg.allowed_classes
            and det.class_name not in self.cfg.allowed_classes
        ):
            return False

        # 2. Confidence
        if det.confidence < self.cfg.min_confidence:
            return False

        # 3. Size
        if not is_prompted:
            area = det.area_ratio
            if area < self.cfg.min_size_ratio:
                return False
            if self.cfg.max_size_ratio > 0 and area > self.cfg.max_size_ratio:
                return False
            if not is_non_semantic and not self._passes_shape_profile(det):
                return False

        # 4. Engagement zone
        z = self.cfg.engagement_zone
        if not (z[0] <= det.norm_cx <= z[2] and z[1] <= det.norm_cy <= z[3]):
            return False

        return True

    def _passes_shape_profile(self, det: DetectedObject) -> bool:
        if not bool(getattr(self.cfg, "shape_filter_enabled", False)):
            return True

        profile_name = str(getattr(self.cfg, "shape_profile_name", "") or "").strip().lower()
        if not profile_name:
            profile_name = str(det.class_name or "").strip().lower()
        profile_name = SHAPE_PROFILE_ALIASES.get(profile_name, profile_name)
        profile = SHAPE_FILTER_PROFILES.get(profile_name)
        if not profile:
            return True

        width = max(1.0, float(det.bbox[2]))
        height = max(1.0, float(det.bbox[3]))
        aspect_ratio = width / height
        min_aspect_ratio = float(profile.get("min_aspect_ratio", 0.0) or 0.0)
        max_aspect_ratio = float(profile.get("max_aspect_ratio", 0.0) or 0.0)
        if min_aspect_ratio > 0.0 and aspect_ratio < min_aspect_ratio:
            return False
        if max_aspect_ratio > 0.0 and aspect_ratio > max_aspect_ratio:
            return False
        return True

    def _passes_semantic_confirmation(self, det: DetectedObject, now: float) -> bool:
        if det.class_name in NON_SEMANTIC_CLASSES or str(getattr(det, "source", "")) == "prompted":
            return True

        required_frames = max(1, int(getattr(self.cfg, "semantic_min_confirm_frames", 1) or 1))
        if required_frames <= 1:
            return True

        confirm_conf = max(
            float(self.cfg.min_confidence),
            float(getattr(self.cfg, "semantic_min_confirm_confidence", 0.0) or 0.0),
        )
        confirm_ttl = max(0.1, float(getattr(self.cfg, "semantic_confirm_ttl_s", 0.8) or 0.8))
        state = self._semantic_confirm.get(int(det.track_id))
        counted = float(det.confidence) >= confirm_conf

        if state is None or state.class_name != det.class_name or (now - state.last_seen) > confirm_ttl:
            hits = 1 if counted else 0
        else:
            hits = (state.hits + 1) if counted else 0

        self._semantic_confirm[int(det.track_id)] = _SemanticConfirmState(
            class_name=str(det.class_name),
            hits=hits,
            last_seen=now,
        )
        return hits >= required_frames

    def _prune_confirmation_state(self, now: float) -> None:
        confirm_ttl = max(0.1, float(getattr(self.cfg, "semantic_confirm_ttl_s", 0.8) or 0.8))
        stale_track_ids = [
            track_id
            for track_id, state in self._semantic_confirm.items()
            if (now - state.last_seen) > confirm_ttl
        ]
        for track_id in stale_track_ids:
            self._semantic_confirm.pop(track_id, None)

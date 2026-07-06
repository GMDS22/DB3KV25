"""
SMART SENTRY V3 — Target Filter

Decides which YOLO detections qualify as engageable targets based on
user-defined criteria (class, confidence, size, zone).
"""

from __future__ import annotations

import math
import time
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from .sentry_v2_config import TargetFilterConfig


NON_SEMANTIC_CLASSES = {"motion", "foreground", "color", "moving_object"}

# Normalized-coordinate distance threshold for detecting same-class re-ID jumps.
# If a track_id's detection center moves more than this between frames, the
# confirmation counter is reset to prevent an old object's hit count being
# inherited by a newly assigned track ID.
_REID_CENTER_JUMP_THRESHOLD = 0.3

SHAPE_PROFILE_ALIASES = {
    "birds": "bird",
}

SHAPE_FILTER_PROFILES = {
    "rat": {"min_aspect_ratio": 1.15, "max_aspect_ratio": 3.2},
    "car": {"min_aspect_ratio": 1.15, "max_aspect_ratio": 4.8},
    "cat": {"min_aspect_ratio": 0.65, "max_aspect_ratio": 3.2},
    "dog": {"min_aspect_ratio": 0.65, "max_aspect_ratio": 3.6},
    "person": {"min_aspect_ratio": 0.20, "max_aspect_ratio": 1.05},
    "bird": {"min_aspect_ratio": 0.45, "max_aspect_ratio": 2.8},
    "cat_dog_rat": {"min_aspect_ratio": 0.60, "max_aspect_ratio": 3.8},
}


@dataclass
class _SemanticConfirmState:
    class_name: str
    hits: int = 0
    last_seen: float = 0.0
    # Normalized center of the detection when this state was last updated.
    # Used to detect same-class track-ID reuse (re-identification jumps).
    last_cx: float = -1.0
    last_cy: float = -1.0


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


@dataclass
class FilterDecision:
    """Per-detection filter outcome for runtime diagnostics."""
    track_id: int
    class_name: str
    source: str
    confidence: float
    area_ratio: float
    passed: bool
    reason: str
    detail: str = ""
    confirm_hits: int = 0
    confirm_required: int = 1


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
        self.last_decisions: List[FilterDecision] = []

    def update_config(self, config: TargetFilterConfig) -> None:
        self.cfg = config

    def reset(self) -> None:
        self._semantic_confirm.clear()
        self.last_decisions = []

    # ------------------------------------------------------------------ #
    def filter(self, detections: List[DetectedObject], timestamp: Optional[float] = None) -> List[DetectedObject]:
        """Return only detections that pass all criteria."""
        qualified, _ = self.filter_with_diagnostics(detections, timestamp)
        return qualified

    def filter_with_diagnostics(
        self,
        detections: List[DetectedObject],
        timestamp: Optional[float] = None,
    ) -> Tuple[List[DetectedObject], List[FilterDecision]]:
        """Return qualified detections plus per-detection filter decisions."""
        now = timestamp or time.time()
        qualified: List[DetectedObject] = []
        decisions: List[FilterDecision] = []
        for det in detections:
            passed, reason, detail, confirm_hits, confirm_required = self._evaluate(det, now)
            if passed:
                qualified.append(det)
            decisions.append(FilterDecision(
                track_id=int(det.track_id),
                class_name=str(det.class_name),
                source=str(getattr(det, "source", "") or ""),
                confidence=float(det.confidence),
                area_ratio=float(det.area_ratio),
                passed=bool(passed),
                reason=str(reason),
                detail=str(detail),
                confirm_hits=int(confirm_hits),
                confirm_required=max(1, int(confirm_required)),
            ))
        self._prune_confirmation_state(now)
        self.last_decisions = decisions
        return qualified, decisions

    # ------------------------------------------------------------------ #
    def _passes(self, det: DetectedObject, now: float) -> bool:
        passed, _, _, _, _ = self._evaluate(det, now)
        return passed

    def _evaluate(self, det: DetectedObject, now: float) -> Tuple[bool, str, str, int, int]:
        passed, reason, detail = self._passes_base(det)
        if not passed:
            return False, reason, detail, 0, 1
        return self._passes_semantic_confirmation(det, now)

    def _passes_base(self, det: DetectedObject) -> Tuple[bool, str, str]:
        is_prompted = str(getattr(det, "source", "")) == "prompted"
        is_non_semantic = det.class_name in NON_SEMANTIC_CLASSES

        # 1. Class whitelist
        if (
            not is_prompted
            and self.cfg.allowed_classes
            and det.class_name not in self.cfg.allowed_classes
        ):
            return False, "class_rejected", f"allowed={','.join(self.cfg.allowed_classes)}"

        # 2. Confidence
        if det.confidence < self.cfg.min_confidence:
            return False, "low_confidence", f"{det.confidence:.2f}<{self.cfg.min_confidence:.2f}"

        # 3. Size
        if not is_prompted:
            area = det.area_ratio
            if area < self.cfg.min_size_ratio:
                return False, "size_too_small", f"{area:.4f}<{self.cfg.min_size_ratio:.4f}"
            if self.cfg.max_size_ratio > 0 and area > self.cfg.max_size_ratio:
                return False, "size_too_large", f"{area:.4f}>{self.cfg.max_size_ratio:.4f}"
            shape_ok, shape_detail = self._passes_shape_profile(det)
            if not is_non_semantic and not shape_ok:
                return False, "shape_rejected", shape_detail

        # 4. Engagement zone
        z = self.cfg.engagement_zone
        if not (z[0] <= det.norm_cx <= z[2] and z[1] <= det.norm_cy <= z[3]):
            return False, "outside_zone", f"center=({det.norm_cx:.3f},{det.norm_cy:.3f}) zone={z}"

        return True, "passed_base", ""

    def _passes_shape_profile(self, det: DetectedObject) -> Tuple[bool, str]:
        if not bool(getattr(self.cfg, "shape_filter_enabled", False)):
            return True, ""

        profile_name = str(getattr(self.cfg, "shape_profile_name", "") or "").strip().lower()
        if not profile_name:
            profile_name = str(det.class_name or "").strip().lower()
        profile_name = SHAPE_PROFILE_ALIASES.get(profile_name, profile_name)
        profile = SHAPE_FILTER_PROFILES.get(profile_name)
        if not profile:
            return True, ""

        width = max(1.0, float(det.bbox[2]))
        height = max(1.0, float(det.bbox[3]))
        aspect_ratio = width / height
        min_aspect_ratio = float(profile.get("min_aspect_ratio", 0.0) or 0.0)
        max_aspect_ratio = float(profile.get("max_aspect_ratio", 0.0) or 0.0)
        if min_aspect_ratio > 0.0 and aspect_ratio < min_aspect_ratio:
            return False, f"aspect={aspect_ratio:.2f}<{min_aspect_ratio:.2f} profile={profile_name}"
        if max_aspect_ratio > 0.0 and aspect_ratio > max_aspect_ratio:
            return False, f"aspect={aspect_ratio:.2f}>{max_aspect_ratio:.2f} profile={profile_name}"
        return True, ""

    def _passes_semantic_confirmation(self, det: DetectedObject, now: float) -> Tuple[bool, str, str, int, int]:
        if det.class_name in NON_SEMANTIC_CLASSES or str(getattr(det, "source", "")) == "prompted":
            return True, "qualified", "non_semantic_or_prompted", 1, 1

        required_frames = max(1, int(getattr(self.cfg, "semantic_min_confirm_frames", 1) or 1))
        if required_frames <= 1:
            return True, "qualified", "semantic_confirm_disabled", 1, 1

        confirm_conf = max(
            float(self.cfg.min_confidence),
            float(getattr(self.cfg, "semantic_min_confirm_confidence", 0.0) or 0.0),
        )
        confirm_ttl = max(0.1, float(getattr(self.cfg, "semantic_confirm_ttl_s", 0.8) or 0.8))
        state = self._semantic_confirm.get(int(det.track_id))
        counted = float(det.confidence) >= confirm_conf

        # Detect same-class track-ID reuse: if the detection center has jumped
        # beyond the re-ID threshold the previous hit count must not carry over.
        center_jumped = False
        if state is not None and state.last_cx >= 0.0 and state.last_cy >= 0.0:
            ddx = det.norm_cx - state.last_cx
            ddy = det.norm_cy - state.last_cy
            if math.sqrt(ddx * ddx + ddy * ddy) > _REID_CENTER_JUMP_THRESHOLD:
                center_jumped = True

        if state is None or state.class_name != det.class_name or (now - state.last_seen) > confirm_ttl or center_jumped:
            hits = 1 if counted else 0
        else:
            hits = (state.hits + 1) if counted else 0

        self._semantic_confirm[int(det.track_id)] = _SemanticConfirmState(
            class_name=str(det.class_name),
            hits=hits,
            last_seen=now,
            last_cx=det.norm_cx,
            last_cy=det.norm_cy,
        )
        if hits >= required_frames:
            return True, "qualified", f"confirm={hits}/{required_frames}", hits, required_frames
        if counted:
            detail = f"confirm={hits}/{required_frames} conf={det.confidence:.2f}"
        else:
            detail = f"confirm={hits}/{required_frames} conf={det.confidence:.2f}<{confirm_conf:.2f}"
        return False, "semantic_confirm_pending", detail, hits, required_frames

    def _prune_confirmation_state(self, now: float) -> None:
        confirm_ttl = max(0.1, float(getattr(self.cfg, "semantic_confirm_ttl_s", 0.8) or 0.8))
        stale_track_ids = [
            track_id
            for track_id, state in self._semantic_confirm.items()
            if (now - state.last_seen) > confirm_ttl
        ]
        for track_id in stale_track_ids:
            self._semantic_confirm.pop(track_id, None)

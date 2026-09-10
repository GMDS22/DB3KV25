"""
SMART SENTRY V3 — Engagement Planner

Given a list of scored targets, decides:
  1. Which targets to engage (above threshold)
  2. In what order (minimum servo slew / nearest-neighbor)
  3. How to convert pixel positions to pan/tilt angles

Also implements multi-target sequencing logic.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List, Optional, Tuple

from .sentry_v2_config import EngagementConfig, GuardConfig, NoFireMaskConfig
from .threat_scorer import TrackedTarget


@dataclass
class EngagementOrder:
    """A single commanded engagement."""
    target: TrackedTarget
    pan: float   # degrees
    tilt: float  # degrees
    rank: int    # 0 = first-to-engage


class EngagementPlanner:
    """
    Plans multi-target engagement sequences.

    Usage:
        planner = EngagementPlanner(eng_cfg, guard_cfg)
        orders = planner.plan(scored_targets, current_pan, current_tilt)
    """

    def __init__(
        self,
        eng_cfg: EngagementConfig,
        guard_cfg: GuardConfig,
        no_fire_masks: Optional[List[NoFireMaskConfig]] = None,
    ):
        self.eng = eng_cfg
        self.guard = guard_cfg
        self.no_fire_masks = list(no_fire_masks or [])

    def update_config(
        self,
        eng_cfg: EngagementConfig,
        guard_cfg: GuardConfig,
        no_fire_masks: Optional[List[NoFireMaskConfig]] = None,
    ) -> None:
        self.eng = eng_cfg
        self.guard = guard_cfg
        self.no_fire_masks = list(no_fire_masks or [])

    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #

    def plan(
        self,
        targets: List[TrackedTarget],
        current_pan: float,
        current_tilt: float,
    ) -> List[EngagementOrder]:
        """
        Return ordered list of engagements.

        Targets below ``min_threat_score`` are skipped.
        If ``optimize_slew_order`` is True, uses a nearest-neighbour heuristic
        starting from the current turret position to minimise total servo travel.
        Otherwise, engages in straight threat-score descending order.
        """
        qualified = [
            t for t in targets if t.threat_score >= self.eng.min_threat_score
        ][: self.eng.max_queue_length]

        if self.eng.single_target_only and qualified:
            qualified = qualified[:1]

        if not qualified:
            return []

        # Convert each target to pan/tilt
        orders: List[EngagementOrder] = []
        for t in qualified:
            if not self.target_is_reachable(t, current_pan, current_tilt):
                continue
            pan, tilt = self._pixel_to_pantilt(t, current_pan, current_tilt)
            orders.append(EngagementOrder(target=t, pan=pan, tilt=tilt, rank=0))

        if (not self.eng.single_target_only) and self.eng.optimize_slew_order and len(orders) > 1:
            orders = self._nearest_neighbour_order(orders, current_pan, current_tilt)
        else:
            # Keep threat-score order
            for i, o in enumerate(orders):
                o.rank = i

        return orders

    def target_is_reachable(
        self,
        target: TrackedTarget,
        current_pan: float,
        current_tilt: float,
    ) -> bool:
        pan_err, tilt_err = self.pixel_error_to_angle_error(
            target.det.norm_cx,
            target.det.norm_cy,
        )
        requested_pan = float(current_pan) + float(pan_err)
        requested_tilt = float(current_tilt) + float(tilt_err)
        return (
            float(self.guard.pan_min) <= requested_pan <= float(self.guard.pan_max)
            and float(self.guard.tilt_min) <= requested_tilt <= float(self.guard.tilt_max)
        )

    # ------------------------------------------------------------------ #
    # Pixel → Pan / Tilt conversion
    # ------------------------------------------------------------------ #

    def pixel_error_to_angle_error(self, norm_cx: float, norm_cy: float) -> Tuple[float, float]:
        """Convert a normalized detection center into pan/tilt angular error."""
        g = self.guard
        dx = float(norm_cx) - 0.5
        dy = float(norm_cy) - 0.5
        pan_err = dx * g.camera_hfov + g.pan_center_bias_deg
        tilt_err = -(dy * g.camera_vfov) + g.tilt_center_bias_deg
        return pan_err, tilt_err

    def aim_from_normalized_center(
        self,
        norm_cx: float,
        norm_cy: float,
        current_pan: float,
        current_tilt: float,
    ) -> Tuple[float, float]:
        """Convert a normalized detection center to absolute turret angles."""
        g = self.guard
        pan_err, tilt_err = self.pixel_error_to_angle_error(norm_cx, norm_cy)
        pan = current_pan + pan_err
        tilt = current_tilt + tilt_err
        pan = max(g.pan_min, min(g.pan_max, pan))
        tilt = max(g.tilt_min, min(g.tilt_max, tilt))
        return pan, tilt

    def _pixel_to_pantilt(
        self, target: TrackedTarget, current_pan: float, current_tilt: float,
    ) -> Tuple[float, float]:
        """
        Convert a normalised detection center to absolute pan/tilt degrees.

        Uses the turret's *current* position as reference (not the guard
        home position), since the camera shows what the turret is pointing
        at right now.  A target at frame-center (0.5, 0.5) means the
        turret is already aimed correctly → output == current position.
        """
        return self.aim_from_normalized_center(
            target.det.norm_cx,
            target.det.norm_cy,
            current_pan,
            current_tilt,
        )

    # ------------------------------------------------------------------ #
    # Minimum-slew ordering (nearest-neighbour TSP heuristic)
    # ------------------------------------------------------------------ #

    @staticmethod
    def _nearest_neighbour_order(
        orders: List[EngagementOrder],
        start_pan: float,
        start_tilt: float,
    ) -> List[EngagementOrder]:
        """
        Re-order engagements to minimise total servo slew.

        Uses greedy nearest-neighbour starting from (start_pan, start_tilt).
        This isn't globally optimal but is O(n²) and good enough for ≤10 targets.
        """
        remaining = list(orders)
        result: List[EngagementOrder] = []
        cur_pan, cur_tilt = start_pan, start_tilt

        while remaining:
            best_idx = 0
            best_dist = float("inf")
            for i, o in enumerate(remaining):
                d = math.hypot(o.pan - cur_pan, o.tilt - cur_tilt)
                if d < best_dist:
                    best_dist = d
                    best_idx = i
            chosen = remaining.pop(best_idx)
            chosen.rank = len(result)
            result.append(chosen)
            cur_pan, cur_tilt = chosen.pan, chosen.tilt

        return result

    # ------------------------------------------------------------------ #
    # Utility
    # ------------------------------------------------------------------ #

    def get_return_position(self) -> Tuple[float, float]:
        """Return the guard (rest) position."""
        return self.guard.guard_pan, self.guard.guard_tilt

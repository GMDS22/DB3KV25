"""
Smart Sentry v2 — Engagement Planner

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

from .sentry_v2_config import EngagementConfig, GuardConfig
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

    def __init__(self, eng_cfg: EngagementConfig, guard_cfg: GuardConfig):
        self.eng = eng_cfg
        self.guard = guard_cfg

    def update_config(self, eng_cfg: EngagementConfig, guard_cfg: GuardConfig) -> None:
        self.eng = eng_cfg
        self.guard = guard_cfg

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

        if not qualified:
            return []

        # Convert each target to pan/tilt
        orders: List[EngagementOrder] = []
        for t in qualified:
            pan, tilt = self._pixel_to_pantilt(t)
            orders.append(EngagementOrder(target=t, pan=pan, tilt=tilt, rank=0))

        if self.eng.optimize_slew_order and len(orders) > 1:
            orders = self._nearest_neighbour_order(orders, current_pan, current_tilt)
        else:
            # Keep threat-score order
            for i, o in enumerate(orders):
                o.rank = i

        return orders

    # ------------------------------------------------------------------ #
    # Pixel → Pan / Tilt conversion
    # ------------------------------------------------------------------ #

    def _pixel_to_pantilt(self, target: TrackedTarget) -> Tuple[float, float]:
        """
        Convert a normalised detection center to absolute pan/tilt degrees.

        Assumes:
          - guard_pan / guard_tilt = turret position when camera center = (0.5, 0.5)
          - camera_hfov / camera_vfov = angular coverage
        """
        g = self.guard
        # Offset from frame center in normalised coords (-0.5 .. +0.5)
        dx = target.det.norm_cx - 0.5
        dy = target.det.norm_cy - 0.5

        # Convert to degrees
        pan = g.guard_pan + dx * g.camera_hfov
        tilt = g.guard_tilt + dy * g.camera_vfov

        # Clamp to safe servo range
        pan = max(5.0, min(185.0, pan))
        tilt = max(10.0, min(130.0, tilt))
        return pan, tilt

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

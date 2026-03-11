"""
Smart Sentry v2 — Overlay (HUD Rendering)

Draws threat scores, engagement zones, guard crosshair, engagement
queue, and state indicator on the video frame.
"""

from __future__ import annotations

import math
import cv2
import numpy as np
from typing import List, Optional, Tuple

from .sentry_v2_config import SentryV2Config
from .sentry_v2_engine import SentryV2Engine, SentryV2State
from .threat_scorer import TrackedTarget
from .engagement_planner import EngagementOrder


# Colour palette (BGR)
_COL_GREEN = (0, 255, 0)
_COL_RED = (0, 0, 255)
_COL_YELLOW = (0, 255, 255)
_COL_CYAN = (255, 255, 0)
_COL_MAGENTA = (255, 0, 255)
_COL_WHITE = (255, 255, 255)
_COL_ORANGE = (0, 165, 255)
_COL_GRAY = (128, 128, 128)


class SentryV2Overlay:
    """Renders the Smart Sentry HUD on a BGR frame."""

    def __init__(self, config: SentryV2Config):
        self.cfg = config

    def update_config(self, config: SentryV2Config) -> None:
        self.cfg = config

    # ------------------------------------------------------------------ #
    # Main draw call
    # ------------------------------------------------------------------ #

    def draw(self, frame: np.ndarray, engine: SentryV2Engine) -> np.ndarray:
        """Draw all overlays onto *frame* (mutates in place, also returns it)."""
        if not self.cfg.show_overlay:
            return frame

        h, w = frame.shape[:2]

        # Engagement zone rectangle
        if self.cfg.show_engagement_zone:
            self._draw_engagement_zone(frame, w, h)

        # Guard crosshair
        if self.cfg.show_guard_crosshair:
            self._draw_guard_crosshair(frame, w, h)

        # All scored targets with threat bars
        if self.cfg.show_threat_scores:
            self._draw_targets(frame, engine.last_targets, w, h)

        # Engagement queue lines
        self._draw_queue(frame, engine, w, h)

        # Active engagement reticle
        if engine.active_order is not None:
            self._draw_active_reticle(frame, engine.active_order, w, h)

        # State badge (top-left)
        self._draw_state_badge(frame, engine)

        # Stats line (bottom-left)
        self._draw_stats(frame, engine, h)

        return frame

    # ------------------------------------------------------------------ #
    # Primitives
    # ------------------------------------------------------------------ #

    def _draw_engagement_zone(self, frame: np.ndarray, w: int, h: int) -> None:
        z = self.cfg.target_filter.engagement_zone
        x1, y1 = int(z[0] * w), int(z[1] * h)
        x2, y2 = int(z[2] * w), int(z[3] * h)
        cv2.rectangle(frame, (x1, y1), (x2, y2), _COL_CYAN, 1)
        cv2.putText(frame, "ZONE", (x1 + 4, y1 + 14),
                     cv2.FONT_HERSHEY_SIMPLEX, 0.4, _COL_CYAN, 1)

    def _draw_guard_crosshair(self, frame: np.ndarray, w: int, h: int) -> None:
        cx, cy = w // 2, h // 2
        size = 20
        cv2.line(frame, (cx - size, cy), (cx + size, cy), _COL_GREEN, 1)
        cv2.line(frame, (cx, cy - size), (cx, cy + size), _COL_GREEN, 1)
        cv2.circle(frame, (cx, cy), size, _COL_GREEN, 1)

    def _draw_targets(
        self, frame: np.ndarray, targets: List[TrackedTarget], w: int, h: int
    ) -> None:
        for t in targets:
            bx, by, bw, bh = t.det.bbox
            # Colour by threat score
            if t.threat_score >= 0.6:
                col = _COL_RED
            elif t.threat_score >= 0.3:
                col = _COL_ORANGE
            else:
                col = _COL_YELLOW

            # Bounding box
            cv2.rectangle(frame, (bx, by), (bx + bw, by + bh), col, 2)

            # Label: class + score
            label = f"{t.det.class_name} {t.threat_score:.0%}"
            cv2.putText(
                frame, label, (bx, by - 6),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, col, 1,
            )

            # Threat bar (right side of bbox)
            bar_x = bx + bw + 4
            bar_h = max(1, int(bh * t.threat_score))
            bar_top = by + bh - bar_h
            cv2.rectangle(frame, (bar_x, bar_top), (bar_x + 6, by + bh), col, -1)
            cv2.rectangle(frame, (bar_x, by), (bar_x + 6, by + bh), _COL_GRAY, 1)

            # Speed arrow
            if t.speed > 0.02:
                cx = int(t.det.center_x)
                cy = int(t.det.center_y)
                ex = int(cx + t.heading_x * 60)
                ey = int(cy + t.heading_y * 60)
                cv2.arrowedLine(frame, (cx, cy), (ex, ey), _COL_MAGENTA, 1, tipLength=0.3)

    def _draw_queue(
        self, frame: np.ndarray, engine: SentryV2Engine, w: int, h: int
    ) -> None:
        """Draw numbered lines connecting engagement queue in order."""
        queue = engine.last_queue
        if len(queue) < 2:
            return
        for i in range(len(queue) - 1):
            a = queue[i].target.det
            b = queue[i + 1].target.det
            pt1 = (int(a.center_x), int(a.center_y))
            pt2 = (int(b.center_x), int(b.center_y))
            cv2.line(frame, pt1, pt2, _COL_CYAN, 1, cv2.LINE_AA)

        # Number each target
        for o in queue:
            cx = int(o.target.det.center_x)
            cy = int(o.target.det.center_y)
            cv2.putText(
                frame, str(o.rank + 1), (cx - 6, cy + 5),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, _COL_WHITE, 2,
            )

    def _draw_active_reticle(
        self, frame: np.ndarray, order: EngagementOrder, w: int, h: int
    ) -> None:
        """Animated reticle on the currently-engaged target."""
        cx = int(order.target.det.center_x)
        cy = int(order.target.det.center_y)
        r = 30
        cv2.circle(frame, (cx, cy), r, _COL_RED, 2)
        cv2.circle(frame, (cx, cy), r + 6, _COL_RED, 1)
        # Cross
        cv2.line(frame, (cx - r - 10, cy), (cx - r + 5, cy), _COL_RED, 2)
        cv2.line(frame, (cx + r - 5, cy), (cx + r + 10, cy), _COL_RED, 2)
        cv2.line(frame, (cx, cy - r - 10), (cx, cy - r + 5), _COL_RED, 2)
        cv2.line(frame, (cx, cy + r - 5), (cx, cy + r + 10), _COL_RED, 2)
        cv2.putText(
            frame, "ENGAGING", (cx - 35, cy - r - 14),
            cv2.FONT_HERSHEY_SIMPLEX, 0.45, _COL_RED, 1,
        )

    def _draw_state_badge(self, frame: np.ndarray, engine: SentryV2Engine) -> None:
        state = engine.state
        name = state.name
        col = {
            SentryV2State.PAUSED: _COL_GRAY,
            SentryV2State.GUARDING: _COL_GREEN,
            SentryV2State.ENGAGING: _COL_RED,
            SentryV2State.RETURNING: _COL_YELLOW,
        }.get(state, _COL_WHITE)

        cv2.rectangle(frame, (8, 8), (180, 34), (0, 0, 0), -1)
        cv2.rectangle(frame, (8, 8), (180, 34), col, 2)
        cv2.putText(
            frame, f"SENTRY: {name}", (14, 28),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, col, 1,
        )

    def _draw_stats(self, frame: np.ndarray, engine: SentryV2Engine, h: int) -> None:
        stats = engine.get_engagement_stats()
        line = (
            f"Targets: {stats['targets_visible']}  "
            f"Qualified: {stats['targets_qualified']}  "
            f"Queue: {stats['queue_length']}  "
            f"Engaged: {stats['engagements_total']}"
        )
        cv2.putText(
            frame, line, (10, h - 12),
            cv2.FONT_HERSHEY_SIMPLEX, 0.4, _COL_WHITE, 1,
        )

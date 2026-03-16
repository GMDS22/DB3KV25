"""
Smart Sentry v2 — Overlay (HUD Rendering)

Draws a simplified HUD focused on one moving target at a time.
"""

from __future__ import annotations

import cv2
import numpy as np
import time
from typing import Optional

from .sentry_v2_config import SentryV2Config
from .sentry_v2_engine import SentryV2Engine, SentryV2State
from .threat_scorer import TrackedTarget


# Colour palette (BGR)
_COL_GREEN = (0, 255, 0)
_COL_RED = (0, 0, 255)
_COL_YELLOW = (0, 255, 255)
_COL_CYAN = (255, 255, 0)
_COL_MAGENTA = (255, 0, 255)
_COL_WHITE = (255, 255, 255)
_COL_ORANGE = (0, 165, 255)
_COL_GRAY = (128, 128, 128)
_COL_BLACK = (0, 0, 0)
_COL_RETICLE_GREEN = (90, 255, 180)
_COL_RETICLE_RED = (70, 95, 255)
_COL_RETICLE_YELLOW = (110, 230, 255)
_COL_RETICLE_GRAY = (150, 150, 150)
_COL_PANEL_FILL = (16, 18, 24)
_COL_PANEL_BORDER = (82, 88, 98)
_COL_PANEL_TEXT = (228, 232, 238)
_COL_PANEL_MUTED = (155, 164, 176)


class SentryV2Overlay:
    """Renders the Smart Sentry HUD on a BGR frame."""

    def __init__(self, config: SentryV2Config):
        self.cfg = config
        self._last_fire_time: float = 0.0
        self._last_fire_burst_count: int = 0

    def update_config(self, config: SentryV2Config) -> None:
        self.cfg = config

    def note_fire_event(self, burst_count: int) -> None:
        self._last_fire_time = time.time()
        self._last_fire_burst_count = max(1, int(burst_count))

    # ------------------------------------------------------------------ #
    # Main draw call
    # ------------------------------------------------------------------ #

    def draw(self, frame: np.ndarray, engine: SentryV2Engine) -> np.ndarray:
        """Draw all overlays onto *frame* (mutates in place, also returns it)."""
        if not self.cfg.show_overlay:
            return frame

        h, w = frame.shape[:2]

        # Guard crosshair
        if self.cfg.show_guard_crosshair:
            self._draw_guard_crosshair(frame, w, h, engine)

        primary = self._get_primary_target(engine)
        if primary is not None:
            self._draw_primary_target(frame, primary, engine)

        self._draw_state_badge(frame, engine)
        self._draw_auto_trigger_badge(frame)
        self._draw_tracking_debug(frame, engine)
        self._draw_fire_feedback(frame, w, h)

        return frame

    # ------------------------------------------------------------------ #
    # Primitives
    # ------------------------------------------------------------------ #

    def _get_crosshair_color(self, engine: SentryV2Engine) -> tuple[int, int, int]:
        return {
            SentryV2State.PAUSED: _COL_RETICLE_GRAY,
            SentryV2State.GUARDING: _COL_RETICLE_GREEN,
            SentryV2State.ENGAGING: _COL_RETICLE_RED,
            SentryV2State.RETURNING: _COL_RETICLE_YELLOW,
        }.get(engine.state, _COL_RETICLE_GREEN)

    @staticmethod
    def _draw_panel(
        frame: np.ndarray,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        accent: tuple[int, int, int],
    ) -> None:
        cv2.rectangle(frame, (x1, y1), (x2, y2), _COL_BLACK, -1)
        cv2.rectangle(frame, (x1, y1), (x2, y2), _COL_PANEL_FILL, -1)
        cv2.rectangle(frame, (x1, y1), (x2, y2), _COL_PANEL_BORDER, 1, cv2.LINE_AA)
        cv2.line(frame, (x1 + 1, y1 + 1), (x2 - 1, y1 + 1), accent, 2, cv2.LINE_AA)

    @staticmethod
    def _draw_target_corners(
        frame: np.ndarray,
        x: int,
        y: int,
        w: int,
        h: int,
        color: tuple[int, int, int],
    ) -> None:
        corner = max(10, min(w, h) // 4)
        thickness = 2
        for p1, p2 in (
            ((x, y), (x + corner, y)),
            ((x, y), (x, y + corner)),
            ((x + w, y), (x + w - corner, y)),
            ((x + w, y), (x + w, y + corner)),
            ((x, y + h), (x + corner, y + h)),
            ((x, y + h), (x, y + h - corner)),
            ((x + w, y + h), (x + w - corner, y + h)),
            ((x + w, y + h), (x + w, y + h - corner)),
        ):
            cv2.line(frame, p1, p2, _COL_BLACK, thickness + 2, cv2.LINE_AA)
            cv2.line(frame, p1, p2, color, thickness, cv2.LINE_AA)

    @staticmethod
    def _pulse_strength(engine: SentryV2Engine) -> float:
        if engine.state != SentryV2State.ENGAGING:
            return 0.0
        return 0.5 + (0.5 * np.sin(time.time() * 7.5))

    def _fire_flash_strength(self) -> float:
        elapsed = time.time() - self._last_fire_time
        if elapsed < 0.0 or elapsed > 0.24:
            return 0.0
        return max(0.0, 1.0 - (elapsed / 0.24))

    @staticmethod
    def _draw_reticle_segment(
        frame: np.ndarray,
        p1: tuple[int, int],
        p2: tuple[int, int],
        color: tuple[int, int, int],
    ) -> None:
        cv2.line(frame, p1, p2, _COL_BLACK, 4, cv2.LINE_AA)
        cv2.line(frame, p1, p2, color, 2, cv2.LINE_AA)
        cv2.line(frame, p1, p2, _COL_WHITE, 1, cv2.LINE_AA)

    def _draw_guard_crosshair(self, frame: np.ndarray, w: int, h: int, engine: SentryV2Engine) -> None:
        cx, cy = w // 2, h // 2
        color = self._get_crosshair_color(engine)
        radius = max(16, min(w, h) // 32)
        pulse = self._pulse_strength(engine)
        outer_radius = radius + 12 + int(round(pulse * 4.0))
        arm_len = radius + 24
        arm_gap = radius - 2
        tick_len = max(10, radius // 2)

        cv2.circle(frame, (cx, cy), outer_radius, _COL_BLACK, 3, cv2.LINE_AA)
        cv2.circle(frame, (cx, cy), outer_radius, (70, 70, 70), 1, cv2.LINE_AA)
        if pulse > 0.0:
            pulse_radius = outer_radius + 6 + int(round(pulse * 5.0))
            cv2.circle(frame, (cx, cy), pulse_radius, color, 1, cv2.LINE_AA)

        cv2.circle(frame, (cx, cy), radius, _COL_BLACK, 4, cv2.LINE_AA)
        cv2.circle(frame, (cx, cy), radius, color, 2, cv2.LINE_AA)
        cv2.circle(frame, (cx, cy), max(2, radius // 4), _COL_WHITE, -1, cv2.LINE_AA)

        self._draw_reticle_segment(frame, (cx - arm_len, cy), (cx - arm_gap, cy), color)
        self._draw_reticle_segment(frame, (cx + arm_gap, cy), (cx + arm_len, cy), color)
        self._draw_reticle_segment(frame, (cx, cy - arm_len), (cx, cy - arm_gap), color)
        self._draw_reticle_segment(frame, (cx, cy + arm_gap), (cx, cy + arm_len), color)

        self._draw_reticle_segment(frame, (cx - outer_radius - tick_len, cy), (cx - outer_radius - 4, cy), color)
        self._draw_reticle_segment(frame, (cx + outer_radius + 4, cy), (cx + outer_radius + tick_len, cy), color)
        self._draw_reticle_segment(frame, (cx, cy - outer_radius - tick_len), (cx, cy - outer_radius - 4), color)
        self._draw_reticle_segment(frame, (cx, cy + outer_radius + 4), (cx, cy + outer_radius + tick_len), color)

        diamond_r = max(4, radius // 3)
        diamond = np.array([
            (cx, cy - diamond_r),
            (cx + diamond_r, cy),
            (cx, cy + diamond_r),
            (cx - diamond_r, cy),
        ], dtype=np.int32)
        cv2.polylines(frame, [diamond], True, _COL_BLACK, 3, cv2.LINE_AA)
        cv2.polylines(frame, [diamond], True, color, 1, cv2.LINE_AA)

    def _get_primary_target(self, engine: SentryV2Engine) -> Optional[TrackedTarget]:
        if engine.active_order is not None:
            return engine.active_order.target
        if engine.last_targets:
            return engine.last_targets[0]
        return None

    def _draw_primary_target(
        self, frame: np.ndarray, target: TrackedTarget, engine: SentryV2Engine,
    ) -> None:
        bx, by, bw, bh = target.det.bbox
        col = self._get_crosshair_color(engine)
        prefix = {
            SentryV2State.ENGAGING: "ENGAGING",
            SentryV2State.RETURNING: "LOCKED",
        }.get(engine.state, "TRACKING")

        cv2.rectangle(frame, (bx, by), (bx + bw, by + bh), _COL_BLACK, 3, cv2.LINE_AA)
        cv2.rectangle(frame, (bx, by), (bx + bw, by + bh), col, 1, cv2.LINE_AA)
        self._draw_target_corners(frame, bx, by, bw, bh, col)

        tx = int(target.det.center_x)
        ty = int(target.det.center_y)
        cv2.circle(frame, (tx, ty), 4, _COL_BLACK, -1, cv2.LINE_AA)
        cv2.circle(frame, (tx, ty), 2, _COL_WHITE, -1, cv2.LINE_AA)

        label = f"{prefix}: {self._build_target_name(target)}"
        label_w = max(150, min(360, 10 + (len(label) * 8)))
        label_y1 = max(6, by - 28)
        label_y2 = label_y1 + 22
        self._draw_panel(frame, bx, label_y1, bx + label_w, label_y2, col)
        cv2.putText(
            frame, label, (bx + 8, label_y2 - 7),
            cv2.FONT_HERSHEY_SIMPLEX, 0.48, _COL_PANEL_TEXT, 1, cv2.LINE_AA,
        )

    def _build_target_name(self, target: TrackedTarget) -> str:
        class_name = (target.det.class_name or "").strip().lower()
        color_name = (self.cfg.detection_mode.color_preset or "").strip().lower()
        if class_name and class_name not in {"moving_object", "unknown"}:
            return f"moving {class_name}"
        if color_name and color_name not in {"", "any", "custom"}:
            return f"{color_name} moving object"
        return "moving object"

    def _draw_state_badge(self, frame: np.ndarray, engine: SentryV2Engine) -> None:
        state = engine.state
        name = state.name
        col = self._get_crosshair_color(engine)

        self._draw_panel(frame, 8, 8, 220, 44, col)
        cv2.putText(
            frame, "SMART SENTRY V2", (16, 23),
            cv2.FONT_HERSHEY_SIMPLEX, 0.40, _COL_PANEL_MUTED, 1, cv2.LINE_AA,
        )
        cv2.putText(
            frame, name, (16, 37),
            cv2.FONT_HERSHEY_SIMPLEX, 0.56, _COL_PANEL_TEXT, 1, cv2.LINE_AA,
        )

    def _draw_auto_trigger_badge(self, frame: np.ndarray) -> None:
        enabled = bool(self.cfg.engagement.auto_trigger_enabled)
        accent = _COL_RETICLE_RED if enabled else _COL_RETICLE_GREEN
        text = "AUTO FIRE ON" if enabled else "AUTO FIRE OFF"
        hint = "LIVE" if enabled else "SAFE"

        x2 = frame.shape[1] - 8
        x1 = x2 - 174
        y1 = 8
        y2 = 44
        self._draw_panel(frame, x1, y1, x2, y2, accent)
        cv2.putText(
            frame, hint, (x1 + 10, y1 + 15),
            cv2.FONT_HERSHEY_SIMPLEX, 0.38, _COL_PANEL_MUTED, 1, cv2.LINE_AA,
        )
        cv2.putText(
            frame, text, (x1 + 10, y2 - 8),
            cv2.FONT_HERSHEY_SIMPLEX, 0.54, accent, 1, cv2.LINE_AA,
        )

    def _draw_fire_feedback(self, frame: np.ndarray, w: int, h: int) -> None:
        strength = self._fire_flash_strength()
        if strength <= 0.0:
            return

        cx, cy = w // 2, h // 2
        flash_color = _COL_RETICLE_RED if self.cfg.engagement.auto_trigger_enabled else _COL_ORANGE
        ring_radius = max(28, min(w, h) // 18) + int(round(12.0 * strength))
        outer_radius = ring_radius + 18 + int(round(16.0 * strength))
        alpha = 0.18 * strength

        overlay = frame.copy()
        cv2.circle(overlay, (cx, cy), outer_radius, flash_color, -1, cv2.LINE_AA)
        cv2.addWeighted(overlay, alpha, frame, 1.0 - alpha, 0.0, frame)

        cv2.circle(frame, (cx, cy), outer_radius, _COL_BLACK, 3, cv2.LINE_AA)
        cv2.circle(frame, (cx, cy), outer_radius, flash_color, 2, cv2.LINE_AA)
        cv2.circle(frame, (cx, cy), ring_radius, _COL_WHITE, 1, cv2.LINE_AA)

        label = f"TRIGGER x{self._last_fire_burst_count}"
        label_w = max(150, min(220, 18 + (len(label) * 9)))
        x1 = max(8, cx - (label_w // 2))
        x2 = min(w - 8, x1 + label_w)
        x1 = x2 - label_w
        y1 = max(52, cy + outer_radius + 10)
        y2 = y1 + 26
        self._draw_panel(frame, x1, y1, x2, y2, flash_color)
        cv2.putText(
            frame, label, (x1 + 10, y2 - 8),
            cv2.FONT_HERSHEY_SIMPLEX, 0.54, _COL_PANEL_TEXT, 1, cv2.LINE_AA,
        )

    def _draw_tracking_debug(self, frame: np.ndarray, engine: SentryV2Engine) -> None:
        stats = engine.get_engagement_stats()
        lines = [
            f"ERR  pan {stats['last_err_pan_deg']:+.2f}   tilt {stats['last_err_tilt_deg']:+.2f}",
            f"LOCK {stats['aim_lock_frames']}   QUEUE {stats['queue_position'] + 1}/{max(1, stats['queue_length'])}",
        ]
        if stats.get("reacquire_recent") and stats.get("reacquire_note"):
            lines.append(f"REACQ {stats['reacquire_note']}")

        x1 = 8
        y1 = 52
        width = 270
        height = 30 + (18 * len(lines))
        self._draw_panel(frame, x1, y1, x1 + width, y1 + height, self._get_crosshair_color(engine))
        cv2.putText(
            frame, "TRACKING DIAGNOSTICS", (x1 + 8, y1 + 16),
            cv2.FONT_HERSHEY_SIMPLEX, 0.38, _COL_PANEL_MUTED, 1, cv2.LINE_AA,
        )
        y = y1 + 34
        for line in lines:
            cv2.putText(
                frame, line, (x1 + 10, y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.43, _COL_PANEL_TEXT, 1, cv2.LINE_AA,
            )
            y += 17

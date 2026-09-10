"""
SMART SENTRY V3 — Overlay (HUD Rendering)

Draws a simplified HUD focused on one moving target at a time.
"""

from __future__ import annotations

import cv2
import numpy as np
import time
from typing import List, Optional

from .sentry_v2_config import SentryV2Config
from .sentry_v2_no_fire_masks import project_mask_to_frame
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
_COL_FIRE_FLASH = (40, 90, 255)      # BGR: bright orange-red used during fire events
_COL_PANEL_FILL = (16, 18, 24)
_COL_PANEL_BORDER = (82, 88, 98)
_COL_PANEL_TEXT = (228, 232, 238)
_COL_PANEL_MUTED = (155, 164, 176)
_UI_BASE_W = 960.0
_UI_BASE_H = 540.0

# ── Aesthetic constants ──────────────────────────────────────────────────────
# All text is drawn at fixed pixel sizes (no resolution scaling) using
# FONT_HERSHEY_DUPLEX for a cleaner, thinner look.  Backgrounds are replaced
# with a thin drop-shadow so text is legible without opaque boxes.
_FONT = cv2.FONT_HERSHEY_DUPLEX
_FS_TINY   = 0.32   # small captions / muted headers
_FS_SMALL  = 0.38   # secondary info lines
_FS_MEDIUM = 0.44   # primary labels
_FS_LARGE  = 0.52   # state name / big badge


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

    @staticmethod
    def _ui_scale(frame: np.ndarray) -> float:
        h, w = frame.shape[:2]
        scale = min(float(w) / _UI_BASE_W, float(h) / _UI_BASE_H)
        return max(0.55, min(3.0, scale))

    @classmethod
    def _scaled_px(cls, frame: np.ndarray, value: float, minimum: int = 1) -> int:
        return max(int(minimum), int(round(float(value) * cls._ui_scale(frame))))

    @staticmethod
    def _clamp_pct(value: float, low: float = 0.0, high: float = 100.0) -> float:
        return float(np.clip(float(value), low, high))

    def _font_scale(self, frame: np.ndarray, base_scale: float) -> float:
        size_pct = float(getattr(self.cfg, "overlay_text_size_pct", 100.0) or 100.0)
        return max(0.20, float(base_scale) * (self._clamp_pct(size_pct, 0.0, 200.0) / 100.0))

    def _text_size(self, frame: np.ndarray, text: str, base_scale: float, thickness: int = 1) -> tuple[int, int, int]:
        (w, h), baseline = cv2.getTextSize(
            text,
            _FONT,
            self._font_scale(frame, base_scale),
            1,
        )
        return w, h, baseline

    def _put_text(
        self,
        frame: np.ndarray,
        text: str,
        origin: tuple[int, int],
        base_scale: float,
        color: tuple[int, int, int],
        thickness: int = 1,
        *,
        background_opacity_pct: float | None = None,
        text_opacity_pct: float | None = None,
    ) -> None:
        alpha = self._clamp_pct(text_opacity_pct if text_opacity_pct is not None else getattr(self.cfg, "overlay_text_opacity_pct", 100.0), 0.0, 100.0) / 100.0
        bg_alpha = self._clamp_pct(background_opacity_pct if background_opacity_pct is not None else getattr(self.cfg, "overlay_text_background_opacity_pct", 0.0), 0.0, 100.0) / 100.0
        ox, oy = origin
        text_scale = self._font_scale(frame, base_scale)
        (tw, th), _ = cv2.getTextSize(text, _FONT, text_scale, 1)

        if bg_alpha > 0.0:
            pad_x = max(4, int(round(0.18 * tw)))
            pad_y = max(4, int(round(0.35 * th)))
            x0 = max(0, ox - pad_x)
            y0 = max(0, oy - th - pad_y)
            x1 = min(frame.shape[1], ox + tw + pad_x)
            y1 = min(frame.shape[0], oy + pad_y)
            panel = frame.copy()
            overlay = frame.copy()
            cv2.rectangle(overlay, (x0, y0), (x1, y1), _COL_PANEL_FILL, -1, cv2.LINE_AA)
            cv2.addWeighted(overlay, bg_alpha, panel, 1.0 - bg_alpha, 0.0, panel)
            frame[:] = panel

        if alpha < 1.0:
            overlay = frame.copy()
            cv2.putText(overlay, text, (ox + 1, oy + 1), _FONT, text_scale, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(overlay, text, origin, _FONT, text_scale, color, 1, cv2.LINE_AA)
            cv2.addWeighted(overlay, alpha, frame, 1.0 - alpha, 0.0, frame)
            return

        cv2.putText(frame, text, (ox + 1, oy + 1), _FONT,
                    text_scale, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, text, origin,              _FONT,
                    text_scale, color,    1, cv2.LINE_AA)

    # ------------------------------------------------------------------ #
    # Main draw call
    # ------------------------------------------------------------------ #

    def draw(
        self,
        frame: np.ndarray,
        engine: SentryV2Engine,
        *,
        include_target_boxes: bool = True,
    ) -> np.ndarray:
        """Draw all overlays onto *frame* (mutates in place, also returns it)."""
        if not self.cfg.show_overlay:
            return frame

        h, w = frame.shape[:2]

        # Guard crosshair
        if self.cfg.show_guard_crosshair:
            self._draw_guard_crosshair(frame, w, h, engine)

        if self.cfg.show_no_fire_masks and self.cfg.no_fire_masks:
            self._draw_no_fire_masks(frame, engine, w, h)

        if self.cfg.show_engagement_zone:
            self._draw_engagement_zone(frame, engine, w, h)

        display_targets = self._get_display_targets(engine) if include_target_boxes else []
        self._draw_forensic_object_debug(frame, engine)
        primary = display_targets[0] if display_targets else None
        self._draw_detection_size_tag(frame, primary)
        if primary is not None:
            self._draw_primary_target(frame, primary, engine)
            for queue_index, target in enumerate(display_targets[1:], start=2):
                self._draw_secondary_target(frame, target, queue_index)

        self._draw_state_badge(frame, engine)
        auto_badge_bottom = self._draw_auto_trigger_badge(frame)
        self._draw_target_classes_badge(frame, engine, top_y=auto_badge_bottom + self._scaled_px(frame, 10))
        self._draw_tracking_debug(frame, engine)
        self._draw_fire_feedback(frame, w, h)

        return frame

    def _draw_forensic_object_debug(self, frame: np.ndarray, engine: SentryV2Engine) -> None:
        entries = list(engine.get_forensic_overlay_entries()) if hasattr(engine, "get_forensic_overlay_entries") else []
        if not entries:
            return
        planner_state = str(getattr(engine, "_engage_phase", "") or "")
        for entry in entries:
            bbox = list(entry.get("bbox", [0, 0, 0, 0]) or [0, 0, 0, 0])
            if len(bbox) != 4:
                continue
            bx, by, bw, bh = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
            status = str(entry.get("status", "ignored") or "ignored").lower()
            if status == "qualified":
                color = _COL_GREEN
            elif status == "candidate":
                color = _COL_YELLOW
            elif status == "rejected":
                color = _COL_RED
            else:
                color = _COL_GRAY

            if bw > 1 and bh > 1:
                cv2.rectangle(frame, (bx, by), (bx + bw, by + bh), color, 1, cv2.LINE_AA)

            tracker_id = int(entry.get("track_id", -1) or -1)
            class_name = str(entry.get("class_name", "") or "")
            conf = float(entry.get("confidence", 0.0) or 0.0)
            motion = float(entry.get("motion_score", 0.0) or 0.0)
            shape = float(entry.get("shape_score", 0.0) or 0.0)
            threat = float(entry.get("threat_score", 0.0) or 0.0)
            reject_reason = str(entry.get("rejection_reason", "") or "")

            label = (
                f"ID{tracker_id} {class_name} c={conf:.2f} m={motion:.2f} "
                f"sh={shape:.2f} th={threat:.2f} {status.upper()}"
            )
            if reject_reason:
                label += f" r={reject_reason}"
            if planner_state:
                label += f" p={planner_state}"

            label_y = max(12, by - 6)
            self._put_text(frame, label, (max(2, bx), label_y), _FS_TINY, color)

    def _draw_detection_size_tag(self, frame: np.ndarray, target: Optional[TrackedTarget]) -> None:
        """Draw a pixel size tag for the current primary target only."""
        if target is None:
            return
        det = target.det
        bx, by, bw, bh = det.bbox
        label = f"{det.class_name}  {int(bw)}x{int(bh)}px"
        x = max(4, int(bx))
        y = max(14, int(by) - 8)
        self._put_text(frame, label, (x, y), _FS_TINY, _COL_PANEL_MUTED)

    def _draw_engagement_zone(self, frame: np.ndarray, engine: SentryV2Engine, w: int, h: int) -> None:
        """Draw the center fire/lock window in frame coordinates."""
        hfov = float(max(1.0, getattr(self.cfg.guard, "camera_hfov", 1.0)))
        vfov = float(max(1.0, getattr(self.cfg.guard, "camera_vfov", 1.0)))
        eng = self.cfg.engagement
        tol_pan = float(eng.fire_trigger_enter_pan_tolerance if eng.auto_trigger_enabled else eng.aim_lock_pan_tolerance)
        tol_tilt = float(eng.fire_trigger_enter_tilt_tolerance if eng.auto_trigger_enabled else eng.aim_lock_tilt_tolerance)

        half_w = max(4, int(round((tol_pan / hfov) * w)))
        half_h = max(4, int(round((tol_tilt / vfov) * h)))
        cx = w // 2
        cy = h // 2
        x1 = max(0, cx - half_w)
        x2 = min(w - 1, cx + half_w)
        y1 = max(0, cy - half_h)
        y2 = min(h - 1, cy + half_h)

        accent = _COL_RETICLE_RED if eng.auto_trigger_enabled else _COL_RETICLE_YELLOW
        axes = (max(4, (x2 - x1) // 2), max(4, (y2 - y1) // 2))
        overlay = frame.copy()
        cv2.ellipse(overlay, (cx, cy), axes, 0, 0, 360, accent, -1, cv2.LINE_AA)
        cv2.addWeighted(overlay, 0.10, frame, 0.90, 0.0, dst=frame)
        cv2.ellipse(frame, (cx, cy), axes, 0, 0, 360, _COL_BLACK, 3, cv2.LINE_AA)
        cv2.ellipse(frame, (cx, cy), axes, 0, 0, 360, accent, 1, cv2.LINE_AA)

    def apply_scope_view(self, frame: np.ndarray, engine: SentryV2Engine) -> np.ndarray:
        """Apply a display-only round scope view during engaging mode."""
        if not bool(getattr(self.cfg, "scope_view_enabled", False)):
            return frame
        if engine.state != SentryV2State.ENGAGING:
            return frame

        h, w = frame.shape[:2]
        center_x = w // 2
        center_y = h // 2
        radius_pct = float(np.clip(getattr(self.cfg, "scope_radius_pct", 35), 20, 60)) / 100.0
        scope_radius = max(36, int(min(h, w) * radius_pct))
        vignette_opacity = float(np.clip(getattr(self.cfg, "scope_vignette_opacity", 60), 0, 100)) / 100.0
        if vignette_opacity <= 0.0:
            vignette_opacity = 0.0

        yy, xx = np.ogrid[:h, :w]
        dist = np.sqrt(((xx - center_x) ** 2) + ((yy - center_y) ** 2))
        feather = max(12.0, float(scope_radius) * 0.18)
        alpha = np.clip((dist - float(scope_radius)) / feather, 0.0, 1.0) * vignette_opacity

        scoped = frame.astype(np.float32)
        scoped *= (1.0 - alpha[..., None])
        scoped = np.clip(scoped, 0, 255).astype(np.uint8)

        flash = self._fire_flash_strength()
        ring_color = _COL_FIRE_FLASH if flash > 0.0 else _COL_WHITE
        inner_ring_color = _COL_FIRE_FLASH if flash > 0.0 else _COL_BLACK
        crosshair_color = _COL_FIRE_FLASH if flash > 0.0 else _COL_BLACK
        tick_color = _COL_BLACK

        # Outer ring (scope boundary)
        cv2.circle(scoped, (center_x, center_y), scope_radius + 4, _COL_BLACK, 5, cv2.LINE_AA)
        cv2.circle(scoped, (center_x, center_y), scope_radius + 4, ring_color, 2, cv2.LINE_AA)
        cv2.circle(scoped, (center_x, center_y), scope_radius - 6, _COL_BLACK, 2, cv2.LINE_AA)
        cv2.circle(scoped, (center_x, center_y), scope_radius - 6, inner_ring_color, 1, cv2.LINE_AA)

        # Fire-flash: pulsing expanded ring
        if flash > 0.0:
            flash_r = scope_radius + 6 + int(round(flash * 10.0))
            cv2.circle(scoped, (center_x, center_y), flash_r, _COL_BLACK, 3, cv2.LINE_AA)
            cv2.circle(scoped, (center_x, center_y), flash_r, _COL_FIRE_FLASH,
                       1 + int(round(flash * 2.0)), cv2.LINE_AA)
            # Subtle red fill tint inside scope
            tint = scoped.copy()
            cv2.circle(tint, (center_x, center_y), scope_radius - 2, _COL_FIRE_FLASH, -1, cv2.LINE_AA)
            cv2.addWeighted(tint, 0.07 * flash, scoped, 1.0, 0.0, scoped)

        # Scope crosshair lines with center gap
        gap = max(10, scope_radius // 10)
        arm_end = scope_radius - 10
        arm_color = crosshair_color

        def _scope_arm(p1: tuple, p2: tuple) -> None:
            cv2.line(scoped, p1, p2, _COL_BLACK, 4, cv2.LINE_AA)
            cv2.line(scoped, p1, p2, arm_color, 2, cv2.LINE_AA)

        _scope_arm((center_x - arm_end, center_y), (center_x - gap, center_y))
        _scope_arm((center_x + gap, center_y), (center_x + arm_end, center_y))
        _scope_arm((center_x, center_y - arm_end), (center_x, center_y - gap))
        _scope_arm((center_x, center_y + gap), (center_x, center_y + arm_end))

        # Tick marks at 1/3 and 2/3 along each arm
        tick_h = max(4, scope_radius // 14)
        for tick_d in (scope_radius // 3, (2 * scope_radius) // 3):
            # Horizontal arm ticks
            for tx in (center_x - tick_d, center_x + tick_d):
                cv2.line(scoped, (tx, center_y - tick_h), (tx, center_y + tick_h),
                         tick_color, 1, cv2.LINE_AA)
            # Vertical arm ticks
            for ty in (center_y - tick_d, center_y + tick_d):
                cv2.line(scoped, (center_x - tick_h, ty), (center_x + tick_h, ty),
                         tick_color, 1, cv2.LINE_AA)

        # Phase label
        engage_phase = str(getattr(engine, "_engage_phase", ""))
        if flash > 0.0:
            phase_label = "FIRING"
            label_color = _COL_FIRE_FLASH
        elif engage_phase == "precision":
            phase_label = "ALIGNING"
            label_color = _COL_PANEL_TEXT
        else:
            phase_label = "SCOPE VIEW"
            label_color = _COL_PANEL_TEXT

        self._put_text(
            scoped,
            phase_label,
            (max(self._scaled_px(scoped, 12), center_x - self._scaled_px(scoped, 52)), max(self._scaled_px(scoped, 24), center_y - scope_radius - self._scaled_px(scoped, 14))),
            0.5,
            label_color,
        )
        return scoped

    def _draw_no_fire_masks(self, frame: np.ndarray, engine: SentryV2Engine, w: int, h: int) -> None:
        overlay = frame.copy()
        active_mask_name = str(getattr(engine, "_last_no_fire_mask_name", "") or "")
        for mask in self.cfg.no_fire_masks:
            if not bool(mask.visible) or len(mask.vertices) < 3:
                continue
            points = project_mask_to_frame(
                mask,
                engine.current_pan,
                engine.current_tilt,
                self.cfg.guard.camera_hfov,
                self.cfg.guard.camera_vfov,
                w,
                h,
            )
            if len(points) < 3:
                continue

            poly = np.array(points, dtype=np.int32)
            fill = (30, 60, 180)
            stroke = (70, 120, 255)
            if active_mask_name and str(mask.name) == active_mask_name:
                fill = (40, 40, 220)
                stroke = (90, 90, 255)

            cv2.fillPoly(overlay, [poly], fill)
            cv2.polylines(frame, [poly], True, stroke, 2, cv2.LINE_AA)
            label_pt = tuple(poly[0])
            self._put_text(
                frame,
                str(mask.name or "NO-FIRE"),
                (int(label_pt[0]) + self._scaled_px(frame, 8), int(label_pt[1]) - self._scaled_px(frame, 8)),
                0.46,
                _COL_PANEL_TEXT,
            )

        cv2.addWeighted(overlay, 0.18, frame, 0.82, 0.0, dst=frame)

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
        # No opaque background — draw only a thin 1px accent underline so
        # the text group is visually anchored without covering the video.
        cv2.line(frame, (x1, y2), (x2, y2), (0, 0, 0), 2, cv2.LINE_AA)
        cv2.line(frame, (x1, y2), (x2, y2), accent,    1, cv2.LINE_AA)

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
        cv2.line(frame, p1, p2, _COL_BLACK, 2, cv2.LINE_AA)
        cv2.line(frame, p1, p2, color, 1, cv2.LINE_AA)

    def _draw_guard_crosshair(self, frame: np.ndarray, w: int, h: int, engine: SentryV2Engine) -> None:
        cx, cy = w // 2, h // 2
        color = self._get_crosshair_color(engine)
        flash = self._fire_flash_strength()
        if flash > 0.0:
            color = _COL_FIRE_FLASH
        radius = max(16, min(w, h) // 32)
        pulse = self._pulse_strength(engine)
        outer_radius = radius + 12 + int(round(pulse * 4.0))
        arm_len = radius + 24
        arm_gap = radius - 2
        tick_len = max(10, radius // 2)

        cv2.circle(frame, (cx, cy), outer_radius, _COL_BLACK, 2, cv2.LINE_AA)
        cv2.circle(frame, (cx, cy), outer_radius, (70, 70, 70), 1, cv2.LINE_AA)
        if pulse > 0.0:
            pulse_radius = outer_radius + 6 + int(round(pulse * 5.0))
            cv2.circle(frame, (cx, cy), pulse_radius, color, 1, cv2.LINE_AA)

        # Fire-flash: expanding ring that fades out
        if flash > 0.0:
            fire_ring_r = outer_radius + 8 + int(round(flash * 14.0))
            cv2.circle(frame, (cx, cy), fire_ring_r, _COL_BLACK, 2, cv2.LINE_AA)
            cv2.circle(frame, (cx, cy), fire_ring_r, _COL_FIRE_FLASH,
                       1 + int(round(flash * 2.0)), cv2.LINE_AA)

        cv2.circle(frame, (cx, cy), radius, _COL_BLACK, 2, cv2.LINE_AA)
        cv2.circle(frame, (cx, cy), radius, color, 1, cv2.LINE_AA)

        # Center dot — larger and fire-colored during flash
        dot_r = max(2, radius // 4) + int(round(flash * 3.0))
        dot_col = _COL_FIRE_FLASH if flash > 0.5 else _COL_WHITE
        cv2.circle(frame, (cx, cy), dot_r, dot_col, -1, cv2.LINE_AA)

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
        cv2.polylines(frame, [diamond], True, _COL_BLACK, 2, cv2.LINE_AA)
        cv2.polylines(frame, [diamond], True, color, 1, cv2.LINE_AA)

    def _get_primary_target(self, engine: SentryV2Engine) -> Optional[TrackedTarget]:
        if engine.active_order is not None:
            active_track_id = int(engine.active_order.target.det.track_id)
            for target in engine.last_targets:
                if int(target.det.track_id) == active_track_id:
                    return target
            if engine.state == SentryV2State.ENGAGING:
                return None
            return engine.active_order.target
        if engine.last_targets:
            return engine.last_targets[0]
        return None

    def _get_display_targets(self, engine: SentryV2Engine) -> List[TrackedTarget]:
        targets: List[TrackedTarget] = []
        seen_track_ids: set[int] = set()

        active = self._get_primary_target(engine)
        if active is not None:
            track_id = int(active.det.track_id)
            seen_track_ids.add(track_id)
            targets.append(active)

        max_targets = max(1, int(getattr(self.cfg.engagement, "max_queue_length", 1)))
        ordered = list(engine.last_targets)

        for target in ordered:
            track_id = int(target.det.track_id)
            if track_id in seen_track_ids:
                continue
            seen_track_ids.add(track_id)
            targets.append(target)
            if len(targets) >= max_targets:
                break

        return targets[:max_targets]

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
        if self.cfg.show_threat_scores:
            label += f"  THR {target.threat_score:.2f}"
        _, lh, lb = self._text_size(frame, label, _FS_MEDIUM)
        label_y = max(lh + 4, by - 6)
        self._put_text(frame, label, (bx, label_y), _FS_MEDIUM, _COL_PANEL_TEXT)

        if self.cfg.show_threat_scores:
            metrics = f"C {target.det.confidence:.2f}  P {target.persistence:.1f}s  V {target.speed:.2f}"
            _, mh, mb = self._text_size(frame, metrics, _FS_SMALL)
            metrics_y = min(frame.shape[0] - 4, by + bh + mh + 6)
            self._put_text(frame, metrics, (bx, metrics_y), _FS_SMALL, _COL_PANEL_MUTED)

    def _draw_secondary_target(self, frame: np.ndarray, target: TrackedTarget, queue_index: int) -> None:
        bx, by, bw, bh = target.det.bbox
        col = _COL_CYAN

        cv2.rectangle(frame, (bx, by), (bx + bw, by + bh), _COL_BLACK, 2, cv2.LINE_AA)
        cv2.rectangle(frame, (bx, by), (bx + bw, by + bh), col, 1, cv2.LINE_AA)
        self._draw_target_corners(frame, bx, by, bw, bh, col)

        label = f"T{queue_index}: {self._build_target_name(target)}"
        if self.cfg.show_threat_scores:
            label += f"  {target.threat_score:.2f}"
        _, lh, _ = self._text_size(frame, label, _FS_SMALL)
        label_y = max(lh + 4, by - 6)
        self._put_text(frame, label, (bx, label_y), _FS_SMALL, col)

    def _build_target_name(self, target: TrackedTarget) -> str:
        identity_label = str(getattr(target.det, "identity_label", "") or "").strip()
        if identity_label:
            return identity_label
        class_name = (target.det.class_name or "").strip().lower()
        color_name = (self.cfg.detection_mode.color_preset or "").strip().lower()
        if class_name and class_name not in {"moving_object", "unknown"}:
            return class_name
        if color_name and color_name not in {"", "any", "custom"}:
            return f"{color_name} object"
        return "object"

    def _draw_state_badge(self, frame: np.ndarray, engine: SentryV2Engine) -> None:
        state = engine.state
        name = state.name
        col = self._get_crosshair_color(engine)
        margin = 10
        _, nh, _ = self._text_size(frame, name, _FS_LARGE)
        self._put_text(
            frame,
            name,
            (margin, margin + nh),
            _FS_LARGE,
            col,
            background_opacity_pct=getattr(self.cfg, "overlay_text_background_opacity_pct", 0.0),
            text_opacity_pct=getattr(self.cfg, "overlay_text_opacity_pct", 100.0),
        )

    def _draw_auto_trigger_badge(self, frame: np.ndarray) -> int:
        enabled = bool(self.cfg.engagement.auto_trigger_enabled)
        accent = _COL_RETICLE_RED if enabled else _COL_RETICLE_GREEN
        text = "AUTO FIRE ON" if enabled else "AUTO FIRE OFF"
        hint = "LIVE" if enabled else "SAFE"
        fw = frame.shape[1]
        margin = 10
        _, hh, _ = self._text_size(frame, hint, _FS_TINY)
        tw, th, _ = self._text_size(frame, text, _FS_MEDIUM)
        rx = fw - margin - max(tw, self._text_size(frame, hint, _FS_TINY)[0])
        self._put_text(frame, hint,  (rx, margin + hh),          _FS_TINY,   _COL_PANEL_MUTED,
                       background_opacity_pct=getattr(self.cfg, "overlay_text_background_opacity_pct", 0.0),
                       text_opacity_pct=getattr(self.cfg, "overlay_text_opacity_pct", 100.0))
        self._put_text(frame, text,  (rx, margin + hh + 4 + th), _FS_MEDIUM, accent,
                       background_opacity_pct=getattr(self.cfg, "overlay_text_background_opacity_pct", 0.0),
                       text_opacity_pct=getattr(self.cfg, "overlay_text_opacity_pct", 100.0))
        return margin + hh + 4 + th

    def _active_target_classes(self, engine: SentryV2Engine) -> List[str]:
        target_cfg = getattr(getattr(engine, "cfg", None), "target_filter", None)
        raw_classes = list(getattr(target_cfg, "allowed_classes", []) or [])
        deduped: List[str] = []
        seen: set[str] = set()
        for item in raw_classes:
            cleaned = str(item or "").strip()
            if not cleaned:
                continue
            key = cleaned.lower()
            if key in seen:
                continue
            seen.add(key)
            deduped.append(cleaned.title())
        return deduped

    @staticmethod
    def _wrap_target_class_lines(items: List[str], max_chars: int = 38) -> List[str]:
        if not items:
            return ["All detectable classes"]
        lines: List[str] = []
        current = ""
        for item in items:
            segment = item if not current else f"{current}, {item}"
            if len(segment) <= max_chars:
                current = segment
                continue
            if current:
                lines.append(current)
            current = item
        if current:
            lines.append(current)
        return lines

    def _draw_target_classes_badge(self, frame: np.ndarray, engine: SentryV2Engine, *, top_y: int) -> None:
        classes = self._active_target_classes(engine)
        header = f"TARGET CLASSES ({len(classes)})" if classes else "TARGET CLASSES"
        lines = self._wrap_target_class_lines(classes)

        margin = 10
        frame_w = frame.shape[1]
        max_width = 0
        header_w, header_h, _ = self._text_size(frame, header, _FS_TINY)
        max_width = max(max_width, header_w)
        for line in lines:
            line_w, _, _ = self._text_size(frame, line, _FS_SMALL)
            max_width = max(max_width, line_w)
        origin_x = max(margin, frame_w - margin - max_width)

        y = max(top_y, margin + header_h)
        self._put_text(frame, header, (origin_x, y), _FS_TINY, _COL_PANEL_MUTED,
                       background_opacity_pct=getattr(self.cfg, "overlay_text_background_opacity_pct", 0.0),
                       text_opacity_pct=getattr(self.cfg, "overlay_text_opacity_pct", 100.0))

        _, line_h, _ = self._text_size(frame, "Target", _FS_SMALL)
        y += line_h + 5
        for line in lines:
            self._put_text(frame, line, (origin_x, y), _FS_SMALL, _COL_PANEL_TEXT,
                           background_opacity_pct=getattr(self.cfg, "overlay_text_background_opacity_pct", 0.0),
                           text_opacity_pct=getattr(self.cfg, "overlay_text_opacity_pct", 100.0))
            y += line_h + 3

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
        _, lh, _ = self._text_size(frame, label, _FS_MEDIUM)
        lw, _, _ = self._text_size(frame, label, _FS_MEDIUM)
        lx = max(8, cx - lw // 2)
        ly = min(h - 6, cy + outer_radius + lh + 10)
        self._put_text(frame, label, (lx, ly), _FS_MEDIUM, _COL_PANEL_TEXT)

    def _draw_tracking_debug(self, frame: np.ndarray, engine: SentryV2Engine) -> None:
        stats = engine.get_engagement_stats()
        engage_phase = str(stats.get("engage_phase", ""))
        lines = [
            f"ERR  pan {stats['last_err_pan_deg']:+.2f}   tilt {stats['last_err_tilt_deg']:+.2f}",
            f"LOCK {stats['aim_lock_frames']}   QUEUE {stats['queue_position'] + 1}/{max(1, stats['queue_length'])}",
        ]
        veto_line = ""
        if engage_phase:
            lines.append(f"PHASE {engage_phase.upper()}")
        if stats.get("reacquire_recent") and stats.get("reacquire_note"):
            lines.append(f"REACQ {stats['reacquire_note']}")
        if bool(getattr(self.cfg, "show_fire_veto_overlay", True)):
            veto_reason = str(stats.get("fire_veto_reason", "") or "").strip()
            if bool(stats.get("fire_veto_recent", False)) and veto_reason:
                prefix = "person auto-fire blocked:"
                if veto_reason.lower().startswith(prefix):
                    veto_reason = veto_reason[len(prefix):].strip()
                if len(veto_reason) > 64:
                    veto_reason = veto_reason[:61].rstrip() + "..."
                veto_line = f"VETO {veto_reason}"

        margin = 10
        _, header_h, _ = self._text_size(frame, "TRACKING DIAGNOSTICS", _FS_TINY)
        _, line_h, _ = self._text_size(frame, lines[0], _FS_SMALL)
        line_count = len(lines) + (1 if veto_line else 0)
        block_height = header_h + 6 + (line_count * (line_h + 3))
        y = max(margin + header_h, frame.shape[0] - margin - block_height + header_h)
        self._put_text(frame, "TRACKING DIAGNOSTICS", (margin, y), _FS_TINY, _COL_PANEL_MUTED,
                       background_opacity_pct=getattr(self.cfg, "overlay_text_background_opacity_pct", 0.0),
                       text_opacity_pct=getattr(self.cfg, "overlay_text_opacity_pct", 100.0))
        y += line_h + 6
        for line in lines:
            self._put_text(frame, line, (margin, y), _FS_SMALL, _COL_PANEL_TEXT,
                           background_opacity_pct=getattr(self.cfg, "overlay_text_background_opacity_pct", 0.0),
                           text_opacity_pct=getattr(self.cfg, "overlay_text_opacity_pct", 100.0))
            y += line_h + 3
        if veto_line:
            self._put_text(frame, veto_line, (margin, y), _FS_SMALL, _COL_RETICLE_RED,
                           background_opacity_pct=getattr(self.cfg, "overlay_text_background_opacity_pct", 0.0),
                           text_opacity_pct=getattr(self.cfg, "overlay_text_opacity_pct", 100.0))

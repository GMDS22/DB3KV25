"""
SMART SENTRY — AI Visualization Dashboard Widgets
==================================================
Lightweight, non-blocking PyQt5 widgets for the futuristic AI interface:

  AICoreWidget       – Audio-reactive 2-D AI orb (30 FPS, QTimer-driven).
                       Supports an optional DB3000 logo watermark drawn at
                       50 % opacity behind the animated orb rings.  Enable
                       via ``set_static_logo(pixmap, enabled=True)``.
  AIReasoningPanel   – Copilot-style live reasoning stream (colored sections)
  AITelemetryPanel   – Real-time system telemetry key-value grid
  AISignals          – QObject signal carrier for cross-thread UI updates
  _VideoOrbOverlay   – Event-filter helper that pins a child widget to the
                       top-right corner of a resizable container

Threading contract:
  All widget methods MUST be called on the Qt main thread.
  Emit AISignals from worker threads; they are auto-delivered to slots in
  the main thread via Qt's queued connection mechanism.
"""

from __future__ import annotations

import math
import time
from typing import Dict, List, Optional, Tuple

from PyQt5.QtCore import (
    QEvent, QObject, QPointF, QRectF, Qt, QTimer, pyqtSignal,
)
from PyQt5.QtGui import (
    QBrush, QColor, QConicalGradient, QLinearGradient, QPainter,
    QPainterPath, QPen, QRadialGradient, QPalette, QPixmap,
)
from PyQt5.QtWidgets import (
    QFrame, QGridLayout, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget,
)


# ══════════════════════════════════════════════════════════════════════════════
#  SIGNAL CARRIER
# ══════════════════════════════════════════════════════════════════════════════

class AISignals(QObject):
    """Signal carrier for the AI visualization dashboard.

    Emit from background worker threads; connect slots in the UI thread.
    All connections use Qt.AutoConnection so delivery is queued when the
    emitter lives on a different thread.

    Signals
    -------
    reasoning_update(dict)
        Keys: ``section`` (str), ``content`` (str), ``replace`` (bool, opt.)
        Sections: "input" | "ai" | "validation" | "tuning" | "execution" |
                  "system" | "error"
    telemetry_update(dict)
        Arbitrary key→value mapping for the telemetry panel.
    ai_state_update(str)
        State name: "idle" | "listening" | "thinking" | "speaking"
    amplitude_update(float)
        TTS amplitude in [0.0, 1.0], updated per audio chunk.
    """

    reasoning_update = pyqtSignal(dict)
    telemetry_update = pyqtSignal(dict)
    ai_state_update  = pyqtSignal(str)
    amplitude_update = pyqtSignal(float)


# ══════════════════════════════════════════════════════════════════════════════
#  1. AI CORE ORB  (audio-reactive, state-driven)
# ══════════════════════════════════════════════════════════════════════════════

_STATE_PALETTE: Dict[str, Tuple[str, str, str]] = {
    # (background, core highlight, glow/accent)
    "idle":      ("#0d1f14", "#2aff7a", "#14e060"),
    "listening": ("#0d1a2a", "#4ab4ff", "#20a8f0"),
    "thinking":  ("#1a0d2a", "#c87aff", "#aa50e0"),
    "speaking":  ("#2a1a08", "#ffca50", "#ffaa10"),
}

_ROTATION_SPEED: Dict[str, float] = {
    "idle":      0.4,
    "listening": 1.2,
    "thinking":  2.8,
    "speaking":  1.6,
}

_PULSE_SPEED: Dict[str, float] = {
    "idle":      1.0,
    "listening": 2.0,
    "thinking":  3.5,
    "speaking":  2.5,
}


_AI_DASHBOARD_FALLBACK_THEME = {
    "panel_bg": "#0d1018",
    "panel_alt_bg": "#0b1610",
    "field_bg": "#080c10",
    "field_text": "#7a8898",
    "border": "#1a2e24",
    "text": "#d9e2ec",
    "muted": "#7a8898",
    "subtle": "#3a5848",
    "accent": "#8050c0",
    "accent_mid": "#1a2a38",
    "accent_soft": "#3a5848",
    "status_info": "#3878a0",
    "status_ok": "#2e8858",
    "status_warn": "#c09030",
    "status_error": "#883030",
    "status_meta": "#2c3830",
    "scroll_handle": "#1a2a38",
    "hero_bg": "#0d1018",
    "hero_text": "#e6edf4",
    "hero_subtle": "#90a0b0",
    "radius": 8,
}


def _resolve_ai_dashboard_theme(theme_tokens: Optional[dict] = None) -> dict:
    tokens = dict(theme_tokens or {})
    fallback = dict(_AI_DASHBOARD_FALLBACK_THEME)
    return {
        "panel_bg": str(tokens.get("status_card_bg") or tokens.get("panel_rgba") or fallback["panel_bg"]),
        "panel_alt_bg": str(tokens.get("status_subframe_bg") or tokens.get("surface_alt_rgba") or fallback["panel_alt_bg"]),
        "field_bg": str(tokens.get("field_rgba") or fallback["field_bg"]),
        "field_text": str(tokens.get("field_text") or tokens.get("text") or fallback["field_text"]),
        "border": str(tokens.get("status_card_border") or tokens.get("border") or fallback["border"]),
        "text": str(tokens.get("text") or fallback["text"]),
        "muted": str(tokens.get("muted") or fallback["muted"]),
        "subtle": str(tokens.get("status_card_title") or tokens.get("accent") or fallback["subtle"]),
        "accent": str(tokens.get("accent") or fallback["accent"]),
        "accent_mid": str(tokens.get("accent_mid") or fallback["accent_mid"]),
        "accent_soft": str(tokens.get("accent_soft") or tokens.get("border") or fallback["accent_soft"]),
        "status_info": str(tokens.get("status_info") or fallback["status_info"]),
        "status_ok": str(tokens.get("status_ok") or fallback["status_ok"]),
        "status_warn": str(tokens.get("status_warn") or fallback["status_warn"]),
        "status_error": str(tokens.get("status_error") or fallback["status_error"]),
        "status_meta": str(tokens.get("status_meta") or fallback["status_meta"]),
        "scroll_handle": str(tokens.get("scroll_handle") or fallback["scroll_handle"]),
        "hero_bg": str(tokens.get("hero_mid") or tokens.get("hero_start") or fallback["hero_bg"]),
        "hero_text": str(tokens.get("hero_text") or tokens.get("text") or fallback["hero_text"]),
        "hero_subtle": str(tokens.get("hero_subtle") or tokens.get("muted") or fallback["hero_subtle"]),
        "radius": int(tokens.get("status_card_radius") or tokens.get("radius") or fallback["radius"]),
    }


def _reasoning_section_colors(theme: dict) -> Dict[str, str]:
    return {
        "input": theme["status_warn"],
        "ai": theme["status_info"],
        "validation": theme["accent"],
        "tuning": theme["accent"],
        "execution": theme["status_ok"],
        "system": theme["muted"],
        "error": theme["status_error"],
        "info": theme["status_info"],
    }


def _with_alpha(color: QColor, alpha: int) -> QColor:
    tinted = QColor(color)
    tinted.setAlpha(max(0, min(255, int(alpha))))
    return tinted


def _blend_colors(base: QColor, overlay: QColor, ratio: float, *, alpha: Optional[int] = None) -> QColor:
    mix = max(0.0, min(1.0, float(ratio)))
    inv = 1.0 - mix
    blended = QColor(
        int(base.red() * inv + overlay.red() * mix),
        int(base.green() * inv + overlay.green() * mix),
        int(base.blue() * inv + overlay.blue() * mix),
        int(base.alpha() * inv + overlay.alpha() * mix),
    )
    if alpha is not None:
        blended.setAlpha(max(0, min(255, int(alpha))))
    return blended


class AICoreWidget(QWidget):
    """Lightweight 2-D audio-reactive AI orb.

    Visual Behaviour
    ----------------
    * **Idle**     – slow pulsing glow, low brightness
    * **Listening** – subtle waveform expansion, blue tones
    * **Thinking**  – faster pulse, rotating shimmer, purple tones
    * **Speaking**  – strong pulse synced to audio amplitude, amber tones

    External API
    ------------
    ``set_state(state: str)``
        Drive the state machine.  Accepted values: idle / listening /
        thinking / speaking.
    ``set_amplitude(amp: float)``
        Feed audio amplitude in [0.0, 1.0] from the TTS worker.

    Implementation notes
    --------------------
    All rendering is done in ``paintEvent`` via QPainter primitives
    (radial gradient + arc).  A 33 ms QTimer drives ``update()`` at ≈30 FPS.
    No blocking I/O or heavy computation occurs on the paint path.
    """

    _TICK_MS = 33  # ≈30 FPS

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self._state      = "idle"
        self._amplitude  = 0.0
        self._angle      = 0.0   # rotating arc angle (degrees)
        self._pulse_t    = 0.0   # time base for sin-wave pulsing
        self._theme_highlight: Optional[QColor] = None
        self._static_logo_enabled = False
        self._static_logo_pixmap = QPixmap()
        self._logo_draw_scale: float = 1.82  # scale relative to max_r; >2.0 exceeds orb diameter
        self._logo_opacity: float = 0.50

        self.setMinimumSize(64, 64)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self._timer = QTimer(self)
        self._timer.setInterval(self._TICK_MS)
        self._timer.timeout.connect(self._tick)
        self._timer.start()
        # Guard against the parent destroying the widget without calling
        # closeEvent (e.g. when a parent QWidget is deleted directly). The
        # destroyed signal is emitted before the C++ object is invalidated so
        # _timer.stop() is always safe to call here.
        self.destroyed.connect(self._timer.stop)

    # ── public API ────────────────────────────────────────────────────────────

    def set_state(self, state: str) -> None:
        """Set animation state. Silently ignores unknown states."""
        s = str(state or "idle").lower().strip()
        if s not in _STATE_PALETTE:
            s = "idle"
        self._state = s

    def set_amplitude(self, amp: float) -> None:
        """Update audio amplitude (0.0–1.0) to drive orb intensity."""
        self._amplitude = max(0.0, min(1.0, float(amp or 0.0)))

    def apply_theme_tokens(self, theme_tokens: Optional[dict] = None) -> None:
        if theme_tokens is None:
            self._theme_highlight = None
            return
        accent = QColor(str(theme_tokens.get("accent") or ""))
        self._theme_highlight = accent if accent.isValid() else None

    def set_static_logo(self, pixmap: Optional[QPixmap], *, enabled: bool = True) -> None:
        self._static_logo_enabled = bool(enabled)
        if isinstance(pixmap, QPixmap) and not pixmap.isNull():
            self._static_logo_pixmap = QPixmap(pixmap)
        else:
            self._static_logo_pixmap = QPixmap()
        self.update()

    def set_logo_scale(self, scale: float) -> None:
        """Set logo draw size relative to the orb's max_r.

        Default 1.82 keeps the logo inside the orb rings.
        Values >2.0 make the logo slightly larger than the orb diameter,
        useful for the home-screen hero orb watermark.
        """
        self._logo_draw_scale = max(0.5, float(scale))
        self.update()

    def set_logo_opacity(self, opacity: float) -> None:
        self._logo_opacity = max(0.0, min(1.0, float(opacity)))
        self.update()

    # ── Qt lifecycle ──────────────────────────────────────────────────────────

    def closeEvent(self, event) -> None:  # noqa: N802
        """Stop the animation timer before the widget is closed.

        Without this, the 33 ms QTimer keeps firing after the widget is hidden
        or its parent window is closed — wasting CPU and risking a
        use-after-free crash if Qt's object tree has already started teardown.
        The ``destroyed`` signal connection in ``__init__`` covers the case
        where the widget is deleted directly (no closeEvent call).
        """
        self._timer.stop()
        super().closeEvent(event)

    # ── internal ──────────────────────────────────────────────────────────────

    def _tick(self) -> None:
        rot_speed = _ROTATION_SPEED.get(self._state, 0.4)
        self._angle = (self._angle + rot_speed) % 360.0
        self._pulse_t += self._TICK_MS / 1000.0
        # Natural amplitude decay when not actively fed
        if self._state not in ("speaking", "listening"):
            self._amplitude = max(0.0, self._amplitude - 0.025)
        self.update()

    def paintEvent(self, _event) -> None:  # noqa: N802
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        w, h   = float(self.width()), float(self.height())
        cx, cy = w / 2.0, h / 2.0
        max_r  = min(w, h) / 2.0 - 3.0

        # Theme-accented renderer inspired by the home logo: outer ring,
        # rotating dash ring, pulsing inner glow, bright AI core, orbit dots,
        # and subtle scan lines during active conversation.
        state_bg_hex, _state_core_hex, state_glow_hex = _STATE_PALETTE.get(self._state, _STATE_PALETTE["idle"])
        state_bg = QColor(state_bg_hex)
        state_glow = QColor(state_glow_hex)
        theme_core = QColor(self._theme_highlight) if self._theme_highlight is not None else QColor(self.palette().color(QPalette.Highlight))
        if not theme_core.isValid() or theme_core.alpha() == 0:
            _fallback = _STATE_PALETTE.get(self._state, _STATE_PALETTE["idle"])[1]
            theme_core = QColor(_fallback)
        shell_color = _blend_colors(theme_core, state_glow, 0.30)
        bright_color = _blend_colors(shell_color, QColor(255, 255, 255), 0.24)
        deep_color = _blend_colors(state_bg, shell_color, 0.18)

        if self._static_logo_enabled and not self._static_logo_pixmap.isNull():
            # Draw the logo watermark behind the animation.
            draw_size = int(max(76.0, min(max_r * self._logo_draw_scale, min(w, h))))
            logo = self._static_logo_pixmap.scaled(
                draw_size,
                draw_size,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
            left = int(cx - logo.width() / 2.0)
            top = int(cy - logo.height() / 2.0)
            painter.setOpacity(self._logo_opacity)
            painter.drawPixmap(left, top, logo)
            painter.setOpacity(1.0)

        spd   = _PULSE_SPEED.get(self._state, 1.0)
        pulse = 0.5 + 0.5 * math.sin(self._pulse_t * spd * math.pi)
        amp   = 0.25 + 0.75 * self._amplitude
        conv_active = self._state in ("listening", "thinking", "speaking")
        activity = min(1.0, 0.18 + 0.26 * pulse + 0.44 * amp + (0.18 if conv_active else 0.0))

        # Deep field glow keeps the home orb substantial even while idle.
        field_r = max_r * (1.10 + 0.06 * pulse + 0.12 * amp)
        field = QRadialGradient(cx, cy, field_r)
        field.setColorAt(0.0, _with_alpha(_blend_colors(deep_color, shell_color, 0.26), 70 if conv_active else 40))
        field.setColorAt(0.46, _with_alpha(shell_color, 40 if conv_active else 20))
        field.setColorAt(1.0, _with_alpha(shell_color, 0))
        painter.setBrush(QBrush(field))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(QPointF(cx, cy), field_r, field_r)

        # Outer ambient glow
        glow_r = max_r * (0.78 + 0.08 * pulse + 0.1 * amp)
        glow = QRadialGradient(cx, cy, glow_r)
        glow.setColorAt(0.0, _with_alpha(bright_color, 92 if conv_active else 58))
        glow.setColorAt(0.58, _with_alpha(shell_color, 46 if conv_active else 26))
        glow.setColorAt(1.0, _with_alpha(shell_color, 0))
        painter.setBrush(QBrush(glow))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(QPointF(cx, cy), glow_r, glow_r)

        # Static guide rings make the orb feel like a complete home-screen centerpiece.
        painter.setBrush(Qt.NoBrush)
        guide_pen = QPen(_with_alpha(shell_color, 34 if conv_active else 20))
        guide_pen.setWidthF(max(0.8, max_r * 0.012))
        painter.setPen(guide_pen)
        for radius_factor in (0.96, 0.84, 0.56):
            guide_r = max_r * radius_factor
            painter.drawEllipse(QPointF(cx, cy), guide_r, guide_r)

        # Rotating energy spokes add motion density without blocking the center.
        spoke_count = 22 if conv_active else 16
        spoke_width = max(1.0, max_r * 0.012)
        base_spoke_r = max_r * 0.90
        for index in range(spoke_count):
            angle = (index / float(spoke_count)) * math.pi * 2.0 + math.radians(self._angle * (1.8 if conv_active else 0.72))
            spoke_wave = 0.5 + 0.5 * math.sin((self._pulse_t * (4.6 if conv_active else 2.4)) + index * 0.58)
            spoke_len = max_r * (0.035 + (0.085 if conv_active else 0.045) * spoke_wave * (0.45 + amp))
            inner_pt = QPointF(cx + base_spoke_r * math.cos(angle), cy + base_spoke_r * math.sin(angle))
            outer_pt = QPointF(
                cx + (base_spoke_r + spoke_len) * math.cos(angle),
                cy + (base_spoke_r + spoke_len) * math.sin(angle),
            )
            spoke_pen = QPen(_with_alpha(bright_color, 72 + int(108 * spoke_wave * (0.35 + activity))))
            spoke_pen.setWidthF(spoke_width)
            spoke_pen.setCapStyle(Qt.RoundCap)
            painter.setPen(spoke_pen)
            painter.drawLine(inner_pt, outer_pt)

        # Outer ring
        outer_r = max_r * 0.9
        outer_pen = QPen(_with_alpha(shell_color, 54 if conv_active else 34))
        outer_pen.setWidthF(max(1.0, max_r * 0.035))
        painter.setPen(outer_pen)
        painter.setBrush(Qt.NoBrush)
        painter.drawEllipse(QPointF(cx, cy), outer_r, outer_r)

        # Primary rotating shell.
        ring_r = max_r * 0.7
        ring_gradient = QConicalGradient(cx, cy, -self._angle * (1.1 if conv_active else 0.48))
        ring_gradient.setColorAt(0.00, _with_alpha(shell_color, 0))
        ring_gradient.setColorAt(0.12, _with_alpha(bright_color, 225 if conv_active else 150))
        ring_gradient.setColorAt(0.30, _with_alpha(shell_color, 82 if conv_active else 48))
        ring_gradient.setColorAt(0.58, _with_alpha(shell_color, 18 if conv_active else 10))
        ring_gradient.setColorAt(1.00, _with_alpha(shell_color, 0))
        ring_pen = QPen()
        ring_pen.setBrush(QBrush(ring_gradient))
        ring_pen.setWidthF(max(1.6, max_r * 0.06))
        ring_pen.setCapStyle(Qt.RoundCap)
        dash_len = max(18.0, ring_r * (0.95 if conv_active else 0.65))
        gap_len = max(120.0, ring_r * 6.2)
        ring_pen.setDashPattern([dash_len, gap_len])
        ring_pen.setDashOffset(-self._angle * (2.5 if conv_active else 1.2))
        painter.setPen(ring_pen)
        painter.drawEllipse(QPointF(cx, cy), ring_r, ring_r)

        # Secondary segmented shells make the idle state feel less empty.
        arc_specs = (
            (0.82, 94, 0.0, 0.024, 160, 1.35),
            (0.60, 62, 132.0, 0.018, 132, -2.0),
            (0.46, 40, 246.0, 0.014, 112, 2.6),
        )
        for radius_factor, span_deg, phase_deg, width_factor, alpha, speed_factor in arc_specs:
            arc_r = max_r * radius_factor
            arc_pen = QPen(_with_alpha(_blend_colors(shell_color, bright_color, 0.18 if speed_factor > 0 else 0.08), alpha if conv_active else int(alpha * 0.74)))
            arc_pen.setWidthF(max(1.0, max_r * width_factor))
            arc_pen.setCapStyle(Qt.RoundCap)
            painter.setPen(arc_pen)
            start = int((phase_deg + self._angle * speed_factor) * 16)
            painter.drawArc(QRectF(cx - arc_r, cy - arc_r, arc_r * 2.0, arc_r * 2.0), start, int(span_deg * 16))

        # Pulse ripples give the core a conversational breathing pattern.
        ripple_pen_w = max(0.8, max_r * 0.011)
        for ripple_index in range(2 if conv_active else 1):
            ripple_phase = (pulse + ripple_index * 0.34) % 1.0
            ripple_r = max_r * (0.34 + ripple_index * 0.10 + ripple_phase * (0.18 if conv_active else 0.10))
            ripple_alpha = int((1.0 - ripple_phase) * (72 if conv_active else 34))
            ripple_pen = QPen(_with_alpha(shell_color, ripple_alpha))
            ripple_pen.setWidthF(ripple_pen_w)
            painter.setPen(ripple_pen)
            painter.setBrush(Qt.NoBrush)
            painter.drawEllipse(QPointF(cx, cy), ripple_r, ripple_r)

        # Inner pulse
        pulse_r = max_r * (0.34 + 0.06 * pulse + 0.06 * amp)
        pulse_grad = QRadialGradient(cx, cy, pulse_r)
        inner_glow = _with_alpha(_blend_colors(bright_color, QColor(255, 255, 255), 0.14), int(54 + 112 * pulse))
        edge_glow = _with_alpha(shell_color, 0)
        pulse_grad.setColorAt(0.0, inner_glow)
        pulse_grad.setColorAt(0.52, _with_alpha(shell_color, 40 if conv_active else 22))
        pulse_grad.setColorAt(1.0, edge_glow)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(pulse_grad))
        painter.drawEllipse(QPointF(cx, cy), pulse_r, pulse_r)

        # Lens field inside the orb makes the center feel deeper than a flat glow.
        lens_r = max_r * (0.54 + 0.02 * pulse + 0.03 * amp)
        lens_grad = QRadialGradient(cx, cy, lens_r)
        lens_grad.setColorAt(0.0, _with_alpha(_blend_colors(bright_color, QColor(255, 255, 255), 0.08), 54 if conv_active else 28))
        lens_grad.setColorAt(0.68, _with_alpha(_blend_colors(deep_color, shell_color, 0.26), 46 if conv_active else 24))
        lens_grad.setColorAt(1.0, _with_alpha(deep_color, 0))
        painter.setBrush(QBrush(lens_grad))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(QPointF(cx, cy), lens_r, lens_r)

        # AI core and iris.
        iris_r = max_r * (0.17 + 0.025 * pulse + 0.02 * amp)
        iris = QPainterPath()
        iris.moveTo(cx, cy - iris_r)
        iris.lineTo(cx + iris_r * 0.82, cy)
        iris.lineTo(cx, cy + iris_r)
        iris.lineTo(cx - iris_r * 0.82, cy)
        iris.closeSubpath()
        iris_grad = QLinearGradient(cx, cy - iris_r, cx, cy + iris_r)
        iris_grad.setColorAt(0.0, _with_alpha(_blend_colors(bright_color, QColor(255, 255, 255), 0.22), 168 if conv_active else 110))
        iris_grad.setColorAt(0.5, _with_alpha(shell_color, 72 if conv_active else 42))
        iris_grad.setColorAt(1.0, _with_alpha(deep_color, 18 if conv_active else 10))
        painter.setBrush(QBrush(iris_grad))
        painter.setPen(Qt.NoPen)
        painter.drawPath(iris)

        core_r = max_r * (0.13 + 0.03 * pulse + 0.03 * amp)
        core_grad = QRadialGradient(cx, cy, core_r * 1.55)
        core_grad.setColorAt(0.0, QColor(255, 255, 255, 245 if conv_active else 220))
        core_grad.setColorAt(0.35, _with_alpha(_blend_colors(bright_color, QColor(255, 255, 255), 0.20), 214 if conv_active else 170))
        core_grad.setColorAt(1.0, _with_alpha(shell_color, 0))
        painter.setBrush(QBrush(core_grad))
        painter.drawEllipse(QPointF(cx, cy), core_r * 1.28, core_r * 1.28)

        painter.setBrush(QBrush(QColor(255, 255, 255, 236 if conv_active else 208)))
        painter.drawEllipse(QPointF(cx, cy), core_r, core_r)

        core_ring_pen = QPen(_with_alpha(bright_color, 160 if conv_active else 104))
        core_ring_pen.setWidthF(max(0.8, max_r * 0.010))
        painter.setPen(core_ring_pen)
        painter.setBrush(Qt.NoBrush)
        painter.drawEllipse(QPointF(cx, cy), core_r * 1.78, core_r * 1.78)

        # Orbit dots (counter-rotating)
        orbit_r = max_r * 0.8
        phase = math.radians(self._angle * (1.9 if conv_active else 0.9))
        dots = (
            (0.0, max_r * 0.045, 228),
            (math.pi * 0.5, max_r * 0.036, 188),
            (math.pi, max_r * 0.041, 210),
            (math.pi * 1.5, max_r * 0.033, 165),
        )
        painter.setPen(Qt.NoPen)
        for base_angle, dot_r, dot_alpha in dots:
            a = base_angle - phase
            dx = orbit_r * math.cos(a)
            dy = orbit_r * math.sin(a)
            painter.setBrush(QBrush(QColor(255, 255, 255, dot_alpha if conv_active else int(dot_alpha * 0.70))))
            painter.drawEllipse(QPointF(cx + dx, cy + dy), dot_r, dot_r)

        # Micro satellites keep the large home-screen orb from feeling sparse.
        satellite_count = 8 if conv_active else 6
        satellite_r = max_r * 0.93
        for index in range(satellite_count):
            sat_angle = (index / float(satellite_count)) * math.pi * 2.0 + math.radians(self._angle * (-1.25 if conv_active else -0.55))
            sat_wobble = max_r * 0.022 * (0.5 + 0.5 * math.sin(self._pulse_t * 2.6 + index * 0.9))
            sat_x = cx + (satellite_r + sat_wobble) * math.cos(sat_angle)
            sat_y = cy + (satellite_r + sat_wobble) * math.sin(sat_angle)
            sat_radius = max_r * (0.012 + (0.004 if index % 2 else 0.0))
            painter.setBrush(QBrush(_with_alpha(bright_color, 116 if conv_active else 64)))
            painter.drawEllipse(QPointF(sat_x, sat_y), sat_radius, sat_radius)

        # Scanning lines only during active conversation
        if conv_active:
            cross_alpha = int(26 + 42 * pulse)
            cross_pen = QPen(QColor(255, 255, 255, cross_alpha))
            cross_pen.setWidthF(max(0.9, max_r * 0.014))
            painter.setPen(cross_pen)
            scan_span = max_r * 0.73
            painter.drawLine(QPointF(cx - scan_span, cy), QPointF(cx + scan_span, cy))
            painter.drawLine(QPointF(cx, cy - scan_span), QPointF(cx, cy + scan_span))

            # Faint sweep arc gives the "AI scanning" feel.
            sweep_pen = QPen(QColor(theme_core.red(), theme_core.green(), theme_core.blue(), 105))
            sweep_pen.setWidthF(max(1.0, max_r * 0.03))
            sweep_pen.setCapStyle(Qt.RoundCap)
            painter.setPen(sweep_pen)
            sweep_rect = QRectF(cx - ring_r, cy - ring_r, ring_r * 2.0, ring_r * 2.0)
            start = int((self._angle * 2.0) * 16)
            painter.drawArc(sweep_rect, start, int(74 * 16))

            beam_pen = QPen(_with_alpha(bright_color, 74))
            beam_pen.setWidthF(max(1.0, max_r * 0.015))
            beam_pen.setCapStyle(Qt.RoundCap)
            painter.setPen(beam_pen)
            beam_angle = math.radians(self._angle * 1.35)
            beam_span = max_r * 0.78
            painter.drawLine(
                QPointF(cx - beam_span * math.cos(beam_angle), cy - beam_span * math.sin(beam_angle)),
                QPointF(cx + beam_span * math.cos(beam_angle), cy + beam_span * math.sin(beam_angle)),
            )

        painter.end()


# ══════════════════════════════════════════════════════════════════════════════
#  2. AI REASONING PANEL  (copilot-style stream)
# ══════════════════════════════════════════════════════════════════════════════

# Section accent colours — subdued, not neon
_SECTION_COLORS: Dict[str, str] = {
    "input":      "#8a7040",   # dim amber
    "ai":         "#3878a0",   # dim blue
    "validation": "#906030",   # dim orange
    "tuning":     "#684890",   # dim purple
    "execution":  "#2e8858",   # dim green
    "system":     "#486858",   # muted teal
    "error":      "#883030",   # dim red
    "info":       "#3a6860",   # dim teal
}

# Compact icon per section (single character)
_SECTION_ICONS: Dict[str, str] = {
    "input":      "&#9678;",   # ◎
    "ai":         "&#9672;",   # ◈
    "validation": "&#9671;",   # ◇
    "tuning":     "&#8987;",   # ⟳
    "execution":  "&#10022;",  # ✦
    "system":     "&#9702;",   # ◦
    "error":      "&#10005;",  # ✕
    "info":       "&middot;",  # ·
}

_REASONING_BASE_STYLE = """
QTextEdit {{
    background-color: #080c10;
    color: #7a8898;
    font-family: "Consolas", "Courier New", monospace;
    font-size: {fs}pt;
    border: none;
    border-radius: 0px;
    selection-background-color: #1a2a38;
    padding: 4px 8px;
}}
QScrollBar:vertical {{
    background: #080c10;
    width: 6px;
    border-radius: 3px;
}}
QScrollBar::handle:vertical {{
    background: #1a2a38;
    border-radius: 3px;
    min-height: 16px;
}}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    height: 0px;
}}
"""

_REASONING_HEADER_STYLE = (
    "color: #3a5848; font-family: Consolas, monospace; font-size: 7pt;"
    " font-weight: bold; background: #080c10; padding: 2px 8px;"
    " border-bottom: 1px solid #10181e; letter-spacing: 1px;"
)

_REASONING_PANEL_STYLE = (
    "QWidget#aiReasoningPanel {"
    " background: #080c10;"
    " border: none;"
    "}"
)


class AIReasoningPanel(QWidget):
    """Copilot-style AI reasoning stream.

    Feed entries via ``update_reasoning(payload)`` where *payload* is::

        {
            "section": "input" | "ai" | "validation" | "tuning" |
                       "execution" | "system" | "error" | "info",
            "content": "human-readable text",
            "replace": bool  (optional, default False)
        }

    Color coding
    ------------
    * **input**      → amber
    * **ai**         → sky-blue
    * **validation** → orange
    * **tuning**     → purple
    * **execution**  → green
    * **system**     → muted teal
    * **error**      → red

    The panel is read-only and auto-scrolls on each update.
    """

    def __init__(
        self,
        parent: Optional[QWidget] = None,
        *,
        font_size: int = 8,
        max_lines: int = 200,
    ) -> None:
        super().__init__(parent)
        self.setObjectName("aiReasoningPanel")
        self._font_size  = font_size
        self._max_lines  = max_lines
        self._entries: List[dict] = []
        self._theme = _resolve_ai_dashboard_theme()

        lay = QVBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)

        header = QLabel("  AI REASONING")
        self._header = header
        header.setFixedHeight(17)
        lay.addWidget(header)

        self._txt = QTextEdit()
        self._txt.setReadOnly(True)
        self._txt.setLineWrapMode(QTextEdit.NoWrap)
        self._txt.setMinimumHeight(50)
        lay.addWidget(self._txt, 1)

        self.apply_theme_tokens()

    # ── public API ────────────────────────────────────────────────────────────

    def update_reasoning(self, payload: dict) -> None:
        """Append or replace an entry in the reasoning stream."""
        section = str(payload.get("section", "system") or "system").lower()
        content = str(payload.get("content", "") or "").strip()
        if not content:
            return

        entry = {
            "section": section,
            "content": content,
            "timestamp": time.strftime("%H:%M"),
        }

        if payload.get("replace", False):
            self._entries = [item for item in self._entries if item.get("section") != section]

        self._entries.append(entry)
        if len(self._entries) > self._max_lines:
            self._entries = self._entries[-self._max_lines :]

        self._render_history()

    def apply_theme_tokens(self, theme_tokens: Optional[dict] = None) -> None:
        self._theme = _resolve_ai_dashboard_theme(theme_tokens)
        radius = max(6, int(self._theme["radius"]))
        self._header.setStyleSheet(
            f"color: {self._theme['subtle']}; font-family: Consolas, monospace; font-size: 7pt;"
            f" font-weight: bold; background: {self._theme['field_bg']}; padding: 2px 8px;"
            f" border-bottom: 1px solid {self._theme['border']}; letter-spacing: 1px;"
        )
        self._txt.setStyleSheet(
            "QTextEdit {"
            f"background-color: {self._theme['field_bg']};"
            f"color: {self._theme['field_text']};"
            ' font-family: "Consolas", "Courier New", monospace;'
            f" font-size: {self._font_size}pt;"
            " border: none;"
            " border-radius: 0px;"
            f" selection-background-color: {self._theme['accent_mid']};"
            " padding: 4px 8px;"
            "}"
            "QScrollBar:vertical {"
            f"background: {self._theme['field_bg']};"
            " width: 6px;"
            " border-radius: 3px;"
            "}"
            "QScrollBar::handle:vertical {"
            f"background: {self._theme['scroll_handle']};"
            " border-radius: 3px;"
            " min-height: 16px;"
            "}"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {"
            " height: 0px;"
            "}"
        )
        self.setStyleSheet(
            f"QWidget#aiReasoningPanel {{ background: {self._theme['field_bg']}; border: 1px solid {self._theme['border']}; border-radius: {radius}px; }}"
        )
        self._render_history()

    def _render_history(self) -> None:
        if not self._entries:
            self._txt.clear()
            return
        section_colors = _reasoning_section_colors(self._theme)
        lines: List[str] = []
        for entry in self._entries:
            section = str(entry.get("section", "system") or "system")
            accent = section_colors.get(section, self._theme["muted"])
            icon = _SECTION_ICONS.get(section, "&middot;")
            safe = (str(entry.get("content", "") or "")
                .replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;"))
            timestamp = str(entry.get("timestamp", "") or "")
            lines.append(
                f'<span style="color:{self._theme["status_meta"]};font-size:7pt;">{timestamp}&nbsp;&nbsp;</span>'
                f'<span style="color:{accent};">{icon}&nbsp;&nbsp;</span>'
                f'<span style="color:{self._theme["field_text"]};">{safe}</span>'
            )

        self._txt.setHtml("<br>".join(lines))
        sb = self._txt.verticalScrollBar()
        if sb is not None:
            sb.setValue(sb.maximum())

    def clear(self) -> None:
        """Clear all history."""
        self._entries.clear()
        self._txt.clear()

    # Convenience wrappers ────────────────────────────────────────────────────

    def append_system(self, text: str) -> None:
        self.update_reasoning({"section": "system", "content": text})

    def append_input(self, text: str) -> None:
        self.update_reasoning({"section": "input", "content": text})

    def append_ai(self, text: str) -> None:
        self.update_reasoning({"section": "ai", "content": text})

    def append_execution(self, text: str) -> None:
        self.update_reasoning({"section": "execution", "content": text})

    def append_error(self, text: str) -> None:
        self.update_reasoning({"section": "error", "content": text})


# ══════════════════════════════════════════════════════════════════════════════
#  3. SYSTEM TELEMETRY PANEL
# ══════════════════════════════════════════════════════════════════════════════

_TELEM_PANEL_STYLE = """
QWidget#aiTelemetryPanel {
    background: #0b1610;
    border: 1px solid #1a2e20;
    border-radius: 4px;
}
"""

_TELEM_HEADER_STYLE = (
    "color: #40e080; font-family: Consolas, monospace; font-size: 8pt;"
    " font-weight: bold; background: #0b1610; padding: 2px 6px;"
    " border-bottom: 1px solid #1a2e20;"
)

_TELEM_KEY_STYLE   = "color: #60b0a0; font-family: Consolas, monospace; font-size: 8pt;"
_TELEM_VALUE_STYLE = (
    "color: #e0f8e8; font-family: Consolas, monospace;"
    " font-size: 8pt; font-weight: bold;"
)

_DISPLAY_KEYS: List[Tuple[str, str]] = [
    ("mode",        "MODE"),
    ("target_lock", "TARGET LOCK"),
    ("speed",       "SPEED"),
    ("brightness",  "BRIGHTNESS"),
    ("fps",         "FPS"),
    ("latency_ms",  "LATENCY"),
    ("ai_state",    "AI STATE"),
    ("voice",       "VOICE"),
    ("detection",   "DETECTION"),
    ("tracking",    "TRACKING"),
]


class AITelemetryPanel(QWidget):
    """Real-time system state display, updated at 5–10 Hz.

    Call ``update_telemetry(payload)`` with a dict mapping telemetry key
    names to string values.  Unknown keys are silently ignored.

    Recognised keys (all optional)
    --------------------------------
    mode, target_lock, speed, brightness, fps, latency_ms,
    ai_state, voice, detection, tracking
    """

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setObjectName("aiTelemetryPanel")
        self.setMinimumWidth(220)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self._value_labels: Dict[str, QLabel] = {}
        self._key_labels: List[QLabel] = []
        self._theme = _resolve_ai_dashboard_theme()

        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        header = QLabel("  ◉ SYSTEM TELEMETRY")
        self._header = header
        header.setFixedHeight(22)
        outer.addWidget(header)

        inner = QWidget()
        inner.setObjectName("aiTelemInner")
        self._inner = inner
        grid = QGridLayout(inner)
        grid.setContentsMargins(8, 6, 8, 6)
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(3)
        grid.setColumnStretch(1, 1)
        outer.addWidget(inner, 1)

        for row, (key, display_label) in enumerate(_DISPLAY_KEYS):
            k = QLabel(f"{display_label}:")
            self._key_labels.append(k)
            v = QLabel("—")
            grid.addWidget(k, row, 0)
            grid.addWidget(v, row, 1)
            self._value_labels[key] = v

        outer.addStretch(1)
        self.apply_theme_tokens()

    def apply_theme_tokens(self, theme_tokens: Optional[dict] = None) -> None:
        self._theme = _resolve_ai_dashboard_theme(theme_tokens)
        radius = max(6, int(self._theme["radius"]))
        self._header.setStyleSheet(
            f"color: {self._theme['status_ok']}; font-family: Consolas, monospace; font-size: 8pt;"
            f" font-weight: bold; background: {self._theme['panel_alt_bg']}; padding: 2px 6px;"
            f" border-bottom: 1px solid {self._theme['border']};"
        )
        for label in self._key_labels:
            label.setStyleSheet(
                f"color: {self._theme['subtle']}; font-family: Consolas, monospace; font-size: 8pt;"
            )
        for label in self._value_labels.values():
            label.setStyleSheet(
                f"color: {self._theme['text']}; font-family: Consolas, monospace; font-size: 8pt; font-weight: bold;"
            )
        self.setStyleSheet(
            f"QWidget#aiTelemetryPanel {{ background: {self._theme['panel_alt_bg']}; border: 1px solid {self._theme['border']}; border-radius: {radius}px; }}"
        )
        self._inner.setStyleSheet(f"background: {self._theme['panel_alt_bg']};")

    # ── public API ────────────────────────────────────────────────────────────

    def update_telemetry(self, payload: dict) -> None:
        """Bulk-update displayed values from a dict."""
        for key, val in payload.items():
            lbl = self._value_labels.get(str(key))
            if lbl is not None:
                lbl.setText(str(val) if val is not None else "—")

    def set_value(self, key: str, value: str) -> None:
        """Update a single telemetry value."""
        lbl = self._value_labels.get(str(key))
        if lbl is not None:
            lbl.setText(str(value) if value is not None else "—")


# ══════════════════════════════════════════════════════════════════════════════
#  4. VIDEO ORB OVERLAY POSITIONER  (event-filter helper)
# ══════════════════════════════════════════════════════════════════════════════

class _VideoOrbOverlay(QObject):
    """Event-filter that keeps *orb* pinned to the top-right of *container*.

    Install once after both widgets are created::

        _VideoOrbOverlay(video_container, ai_orb_widget)

    The orb widget must already be a *child* of *container* so Qt clips and
    paints it correctly.  This helper only manages its position/visibility.
    """

    def __init__(
        self,
        container: QWidget,
        orb: QWidget,
        *,
        margin: int = 10,
    ) -> None:
        super().__init__(container)
        self._container = container
        self._orb       = orb
        self._margin    = margin
        container.installEventFilter(self)
        self._reposition()

    def eventFilter(self, obj: QObject, event: QEvent) -> bool:
        if obj is self._container and event.type() == QEvent.Resize:
            self._reposition()
        return False

    def _reposition(self) -> None:
        cw = self._container.width()
        ow = self._orb.width()
        oh = self._orb.height()
        self._orb.move(cw - ow - self._margin, self._margin)
        self._orb.raise_()


# ══════════════════════════════════════════════════════════════════════════════
#  5. UNIFIED AI CORE PANEL  (replaces hero banner + AI Presence panel)
# ══════════════════════════════════════════════════════════════════════════════

_AI_CORE_PANEL_STYLE = """
QWidget#aiCorePanel {
    background: #0d1018;
    border: 1px solid #1a2e24;
    border-radius: 8px;
}
"""

_AI_CORE_HEADER_STYLE = (
    "QWidget#aiCorePanelHeader {"
    " background: #0d1018;"
    " border-radius: 8px 8px 0px 0px;"
    "}"
)

_AI_CORE_SEP_STYLE = (
    "background: #111820; border: none; max-height: 1px; min-height: 1px;"
)

# state → (color hex, display label)
_AI_CORE_STATE_DISPLAY: Dict[str, Tuple[str, str]] = {
    "idle":      ("#2e8858", "IDLE"),
    "listening": ("#2878b0", "LISTENING"),
    "thinking":  ("#8050c0", "THINKING"),
    "speaking":  ("#c09030", "SPEAKING"),
}


class AICorePanelWidget(QWidget):
    """Unified AI identity panel.

    Combines the Smart Sentry hero banner and AI Presence stream into a
    single cohesive visual block::

        ┌──────────────────────────────────────────┐
        │  [ORB]   SMART SENTRY                    │
        │           v3.5  —  Subtitle              │
        │           ● STATUS: IDLE                 │  ← color per state
        │           [Wake Up]  [Go Rest]            │
        ├──────────────────────────────────────────┤
        │  AI REASONING  ───────────────────────── │
        │  12:34  ◈  Running analysis task         │
        │  12:35  ✦  Plan auto-applied — 2 actions │
        └──────────────────────────────────────────┘

    External API
    ------------
    ``set_state(state)``        "idle" | "listening" | "thinking" | "speaking"
    ``set_amplitude(amp)``      0.0–1.0 audio amplitude
    ``set_status_text(text)``   Override state label text
    ``reasoning_panel``         Embedded ``AIReasoningPanel``
    ``orb``                     Embedded ``AICoreWidget``
    ``wake_button``             QPushButton — connect ``clicked`` externally
    ``rest_button``             QPushButton — connect ``clicked`` externally
    ``title_label``             QLabel (main title text)
    ``subtitle_label``          QLabel (subtitle/version text)
    ``badge_label``             QLabel (optional release badge)
    """

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setObjectName("aiCorePanel")
        self._state: str = "idle"
        self._theme = _resolve_ai_dashboard_theme()

        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        # ── Header ────────────────────────────────────────────────────────────
        hdr = QWidget()
        hdr.setObjectName("aiCorePanelHeader")
        self._header = hdr
        hdr_lay = QHBoxLayout(hdr)
        hdr_lay.setContentsMargins(12, 10, 12, 10)
        hdr_lay.setSpacing(16)
        self._header_layout = hdr_lay  # exposed for responsive metrics

        # Orb — larger for better visual presence in the hero header.
        self._orb = AICoreWidget()
        self._orb.setFixedSize(132, 132)
        hdr_lay.addWidget(self._orb, alignment=Qt.AlignVCenter | Qt.AlignLeft)
        hdr_lay.addSpacing(10)

        # Text column host keeps title/subtitle truly centered in available width.
        self._text_col_host = QWidget()
        text_col = QVBoxLayout(self._text_col_host)
        text_col.setContentsMargins(0, 2, 0, 2)
        text_col.setSpacing(3)
        text_col.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        self.title_label = QLabel("SMART SENTRY")
        self.title_label.setObjectName("sentryV3HeroTitle")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setWordWrap(False)
        self.title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        text_col.addWidget(self.title_label)

        self.subtitle_label = QLabel("")
        self.subtitle_label.setObjectName("sentryV3HeroSubtitle")
        self.subtitle_label.setAlignment(Qt.AlignCenter)
        self.subtitle_label.setWordWrap(False)
        self.subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        text_col.addWidget(self.subtitle_label)

        self._state_lbl = QLabel("&#9679; STATUS:  IDLE")
        self._state_lbl.setObjectName("aiCorePanelStateLabel")
        self._state_lbl.setAlignment(Qt.AlignCenter)
        text_col.addWidget(self._state_lbl)

        self.badge_label = QLabel("")
        self.badge_label.setObjectName("sentryV3HeroBadge")
        self.badge_label.setAlignment(Qt.AlignCenter)
        self.badge_label.setVisible(False)
        text_col.addWidget(self.badge_label)

        text_col.addStretch(1)
        hdr_lay.addWidget(self._text_col_host, 1, alignment=Qt.AlignVCenter)

        # Action buttons column (wrapped so width can be balanced responsively).
        self._action_col_host = QWidget()
        act_col = QVBoxLayout(self._action_col_host)
        act_col.setContentsMargins(0, 0, 0, 0)
        act_col.setSpacing(6)
        act_col.setAlignment(Qt.AlignTop)
        self._action_col = act_col  # exposed for responsive metrics

        self.wake_button = QPushButton("Wake Up")
        self.wake_button.setObjectName("aiCorePanelWake")
        self.wake_button.setMinimumHeight(30)
        act_col.addWidget(self.wake_button)

        self.rest_button = QPushButton("Go Rest")
        self.rest_button.setObjectName("aiCorePanelRest")
        self.rest_button.setMinimumHeight(30)
        act_col.addWidget(self.rest_button)

        hdr_lay.addWidget(self._action_col_host, alignment=Qt.AlignTop | Qt.AlignRight)
        outer.addWidget(hdr)

        # ── Separator ─────────────────────────────────────────────────────────
        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        self._separator = sep
        outer.addWidget(sep)

        # ── Reasoning stream ──────────────────────────────────────────────────
        self._reasoning_panel = AIReasoningPanel(font_size=8)
        outer.addWidget(self._reasoning_panel, stretch=1)

        self.apply_theme_tokens()

    # ── public API ────────────────────────────────────────────────────────────

    @property
    def reasoning_panel(self) -> "AIReasoningPanel":
        return self._reasoning_panel

    @property
    def orb(self) -> AICoreWidget:
        return self._orb

    @property
    def state_label(self) -> QLabel:
        return self._state_lbl

    def apply_theme_tokens(self, theme_tokens: Optional[dict] = None) -> None:
        self._theme = _resolve_ai_dashboard_theme(theme_tokens)
        radius = max(8, int(self._theme["radius"]) + 2)
        self._orb.apply_theme_tokens(theme_tokens)
        self._reasoning_panel.apply_theme_tokens(theme_tokens)
        self._header.setStyleSheet(
            f"QWidget#aiCorePanelHeader {{ background: {self._theme['hero_bg']}; border-top-left-radius: {radius}px; border-top-right-radius: {radius}px; }}"
        )
        self._separator.setStyleSheet(
            f"background: {self._theme['border']}; border: none; max-height: 1px; min-height: 1px;"
        )
        self.badge_label.setStyleSheet(
            f"color: {self._theme['hero_subtle']}; font-size: 7pt; font-style: italic;"
        )
        self.setStyleSheet(
            f"QWidget#aiCorePanel {{ background: {self._theme['panel_bg']}; border: 1px solid {self._theme['border']}; border-radius: {radius}px; }}"
        )
        self._apply_state_label_style()

    def _apply_state_label_style(self) -> None:
        state_color = {
            "idle": self._theme["status_ok"],
            "listening": self._theme["status_info"],
            "thinking": self._theme["accent"],
            "speaking": self._theme["status_warn"],
        }.get(self._state, self._theme["status_ok"])
        self._state_lbl.setStyleSheet(
            f"color: {state_color}; font-family: Consolas, monospace; font-size: 9.2pt; font-weight: 700; letter-spacing: 1px;"
        )

    def set_state(self, state: str) -> None:
        """Drive orb animation + state badge color and text."""
        s = str(state or "idle").lower().strip()
        if s not in _AI_CORE_STATE_DISPLAY:
            s = "idle"
        self._state = s
        self._orb.set_state(s)
        _color, label = _AI_CORE_STATE_DISPLAY[s]
        self._state_lbl.setText(f"&#9679; STATUS:  {label}")
        self._apply_state_label_style()

    def set_amplitude(self, amp: float) -> None:
        """Feed audio amplitude (0–1) to the orb."""
        self._orb.set_amplitude(amp)

    def set_status_text(self, text: str) -> None:
        """Override the state label with arbitrary status text (short)."""
        safe = str(text or "").strip()[:100]
        if safe:
            self._state_lbl.setText(f"&#9679;  {safe}")
            self._apply_state_label_style()

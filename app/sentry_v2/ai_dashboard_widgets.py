"""
SMART SENTRY — AI Visualization Dashboard Widgets
==================================================
Lightweight, non-blocking PyQt5 widgets for the futuristic AI interface:

  AICoreWidget       – Audio-reactive 2-D AI orb (30 FPS, QTimer-driven)
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
    QPainterPath, QPen, QRadialGradient, QPalette,
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

        self.setMinimumSize(64, 64)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self._timer = QTimer(self)
        self._timer.setInterval(self._TICK_MS)
        self._timer.timeout.connect(self._tick)
        self._timer.start()

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
        max_r  = min(w, h) / 2.0 - 4.0

        # Theme-accented tesseract renderer
        theme_core = QColor(self.palette().color(QPalette.Highlight))
        if not theme_core.isValid() or theme_core.alpha() == 0:
            _fallback = _STATE_PALETTE.get(self._state, _STATE_PALETTE["idle"])[1]
            theme_core = QColor(_fallback)
        theme_glow = QColor(theme_core)
        theme_glow.setAlpha(0)

        spd   = _PULSE_SPEED.get(self._state, 1.0)
        pulse = 0.5 + 0.5 * math.sin(self._pulse_t * spd * math.pi)
        amp   = 0.25 + 0.75 * self._amplitude
        scale = min(max_r * 0.70, max_r * (0.55 + 0.22 * pulse + 0.18 * amp))

        # Soft radial glow in active theme color
        glow_r = scale + 18.0 + (8.0 * pulse)
        glow = QRadialGradient(cx, cy, glow_r)
        c0 = QColor(theme_core)
        c0.setAlpha(int(50 + 70 * pulse))
        c1 = QColor(theme_core)
        c1.setAlpha(0)
        glow.setColorAt(0.0, c0)
        glow.setColorAt(1.0, c1)
        painter.setBrush(QBrush(glow))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(QPointF(cx, cy), glow_r, glow_r)

        # Animated tesseract wireframe (two nested rotating cubes projected to 2D)
        cube = [
            (-1.0, -1.0, -1.0), (1.0, -1.0, -1.0), (1.0, 1.0, -1.0), (-1.0, 1.0, -1.0),
            (-1.0, -1.0,  1.0), (1.0, -1.0,  1.0), (1.0, 1.0,  1.0), (-1.0, 1.0,  1.0),
        ]
        edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7),
        ]

        ang = math.radians(self._angle)
        ax = ang * 0.9
        ay = ang * (1.5 if self._state == "thinking" else 1.1)
        az = ang * (0.7 if self._state == "idle" else 1.2)

        def _rot(vx: float, vy: float, vz: float, rx: float, ry: float, rz: float):
            cy0, sy0 = math.cos(rx), math.sin(rx)
            y1, z1 = vy * cy0 - vz * sy0, vy * sy0 + vz * cy0
            cx0, sx0 = math.cos(ry), math.sin(ry)
            x2, z2 = vx * cx0 + z1 * sx0, -vx * sx0 + z1 * cx0
            cz0, sz0 = math.cos(rz), math.sin(rz)
            x3, y3 = x2 * cz0 - y1 * sz0, x2 * sz0 + y1 * cz0
            return x3, y3, z2

        def _proj(vx: float, vy: float, vz: float, scl: float):
            f = 1.6 / (vz + 3.2)
            return QPointF(cx + vx * f * scl, cy + vy * f * scl)

        outer = [_rot(x, y, z, ax, ay, az) for (x, y, z) in cube]
        inner = [_rot(x * 0.58, y * 0.58, z * 0.58, ax + 0.8, ay - 0.5, az + 0.4) for (x, y, z) in cube]
        outer2 = [_proj(x, y, z, scale) for (x, y, z) in outer]
        inner2 = [_proj(x, y, z, scale) for (x, y, z) in inner]

        line_color = QColor(theme_core)
        line_color.setAlpha(int(125 + 90 * pulse))
        pen = QPen(line_color)
        pen.setWidth(max(1, int(1 + 2 * amp)))
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)

        for a, b in edges:
            painter.drawLine(outer2[a], outer2[b])
            painter.drawLine(inner2[a], inner2[b])
            painter.drawLine(outer2[a], inner2[a])

        # Active arc ring around the tesseract
        ring_r = scale + 9.0 + 4.0 * pulse
        ring_rect = QRectF(cx - ring_r, cy - ring_r, ring_r * 2.0, ring_r * 2.0)
        ring_pen = QPen(QColor(line_color))
        ring_pen.setWidth(max(1, int(1 + 2 * amp)))
        painter.setPen(ring_pen)
        span = int(92 + 88 * pulse)
        start = int(self._angle * 16)
        painter.drawArc(ring_rect, start, span * 16)
        painter.drawArc(ring_rect, (start + 180 * 16) % (360 * 16), max(8, span // 2) * 16)

        if self._state in ("thinking", "speaking"):
            sl_pen = QPen(QColor(0, 0, 0, 18))
            sl_pen.setWidth(1)
            painter.setPen(sl_pen)
            y = 0
            while y < int(h):
                painter.drawLine(0, y, int(w), y)
                y += 3

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
        self._history: List[str] = []

        lay = QVBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)

        header = QLabel("  AI REASONING")
        header.setStyleSheet(_REASONING_HEADER_STYLE)
        header.setFixedHeight(17)
        lay.addWidget(header)

        self._txt = QTextEdit()
        self._txt.setReadOnly(True)
        self._txt.setLineWrapMode(QTextEdit.NoWrap)
        self._txt.setStyleSheet(_REASONING_BASE_STYLE.format(fs=font_size))
        self._txt.setMinimumHeight(50)
        lay.addWidget(self._txt, 1)

        self.setStyleSheet(_REASONING_PANEL_STYLE)

    # ── public API ────────────────────────────────────────────────────────────

    def update_reasoning(self, payload: dict) -> None:
        """Append or replace an entry in the reasoning stream."""
        section = str(payload.get("section", "system") or "system").lower()
        content = str(payload.get("content", "") or "").strip()
        if not content:
            return

        accent = _SECTION_COLORS.get(section, _SECTION_COLORS["system"])
        icon   = _SECTION_ICONS.get(section, "&middot;")
        ts     = time.strftime("%H:%M")
        # Escape HTML special chars in content
        safe   = (content
                  .replace("&", "&amp;")
                  .replace("<", "&lt;")
                  .replace(">", "&gt;"))
        line   = (
            f'<span style="color:#2c3830;font-size:7pt;">{ts}&nbsp;&nbsp;</span>'
            f'<span style="color:{accent};">{icon}&nbsp;&nbsp;</span>'
            f'<span style="color:#7a8898;">{safe}</span>'
        )

        if payload.get("replace", False):
            # Remove previous entries for this section
            tag = icon
            self._history = [h for h in self._history if tag not in h]

        self._history.append(line)
        if len(self._history) > self._max_lines:
            self._history = self._history[-self._max_lines :]

        self._txt.setHtml("<br>".join(self._history))
        sb = self._txt.verticalScrollBar()
        if sb is not None:
            sb.setValue(sb.maximum())

    def clear(self) -> None:
        """Clear all history."""
        self._history.clear()
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
        self._value_labels: Dict[str, QLabel] = {}

        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        header = QLabel("  ◉ SYSTEM TELEMETRY")
        header.setStyleSheet(_TELEM_HEADER_STYLE)
        header.setFixedHeight(22)
        outer.addWidget(header)

        inner = QWidget()
        inner.setObjectName("aiTelemInner")
        grid = QGridLayout(inner)
        grid.setContentsMargins(8, 6, 8, 6)
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(3)
        grid.setColumnStretch(1, 1)
        outer.addWidget(inner, 1)

        for row, (key, display_label) in enumerate(_DISPLAY_KEYS):
            k = QLabel(f"{display_label}:")
            k.setStyleSheet(_TELEM_KEY_STYLE)
            v = QLabel("—")
            v.setStyleSheet(_TELEM_VALUE_STYLE)
            grid.addWidget(k, row, 0)
            grid.addWidget(v, row, 1)
            self._value_labels[key] = v

        outer.addStretch(1)
        self.setStyleSheet(_TELEM_PANEL_STYLE)
        # Extra inner background
        inner.setStyleSheet("background: #0b1610;")

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
        │  12:35  ✦  Plan ready — 2 actions staged │
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

        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        # ── Header ────────────────────────────────────────────────────────────
        hdr = QWidget()
        hdr.setObjectName("aiCorePanelHeader")
        hdr.setStyleSheet(_AI_CORE_HEADER_STYLE)
        hdr_lay = QHBoxLayout(hdr)
        hdr_lay.setContentsMargins(12, 10, 12, 10)
        hdr_lay.setSpacing(16)
        self._header_layout = hdr_lay  # exposed for responsive metrics

        # Orb — large, centered vertically
        self._orb = AICoreWidget()
        self._orb.setFixedSize(110, 110)
        hdr_lay.addWidget(self._orb, alignment=Qt.AlignVCenter)
        hdr_lay.addSpacing(8)

        # Text column: title + subtitle + state badge
        text_col = QVBoxLayout()
        text_col.setContentsMargins(0, 2, 0, 2)
        text_col.setSpacing(3)

        self.title_label = QLabel("SMART SENTRY")
        self.title_label.setObjectName("sentryV3HeroTitle")
        self.title_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        text_col.addWidget(self.title_label)

        self.subtitle_label = QLabel("")
        self.subtitle_label.setObjectName("sentryV3HeroSubtitle")
        self.subtitle_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        text_col.addWidget(self.subtitle_label)

        self._state_lbl = QLabel("&#9679; STATUS:  IDLE")
        self._state_lbl.setObjectName("aiCorePanelStateLabel")
        self._state_lbl.setStyleSheet(
            "color: #2e8858; font-family: Consolas, monospace;"
            " font-size: 8pt; font-weight: 700; letter-spacing: 1px;"
        )
        text_col.addWidget(self._state_lbl)

        self.badge_label = QLabel("")
        self.badge_label.setObjectName("sentryV3HeroBadge")
        self.badge_label.setStyleSheet(
            "color: #3a5040; font-size: 7pt; font-style: italic;"
        )
        self.badge_label.setVisible(False)
        text_col.addWidget(self.badge_label)

        text_col.addStretch(1)
        hdr_lay.addLayout(text_col, stretch=1)

        # Action buttons column
        act_col = QVBoxLayout()
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

        hdr_lay.addLayout(act_col)
        outer.addWidget(hdr)

        # ── Separator ─────────────────────────────────────────────────────────
        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        sep.setStyleSheet(_AI_CORE_SEP_STYLE)
        outer.addWidget(sep)

        # ── Reasoning stream ──────────────────────────────────────────────────
        self._reasoning_panel = AIReasoningPanel(font_size=8)
        outer.addWidget(self._reasoning_panel, stretch=1)

        # ── Outer border ──────────────────────────────────────────────────────
        self.setStyleSheet(_AI_CORE_PANEL_STYLE)

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

    def set_state(self, state: str) -> None:
        """Drive orb animation + state badge color and text."""
        s = str(state or "idle").lower().strip()
        if s not in _AI_CORE_STATE_DISPLAY:
            s = "idle"
        self._state = s
        self._orb.set_state(s)
        color, label = _AI_CORE_STATE_DISPLAY[s]
        self._state_lbl.setText(f"&#9679; STATUS:  {label}")
        self._state_lbl.setStyleSheet(
            f"color: {color}; font-family: Consolas, monospace;"
            " font-size: 8pt; font-weight: 700; letter-spacing: 1px;"
        )

    def set_amplitude(self, amp: float) -> None:
        """Feed audio amplitude (0–1) to the orb."""
        self._orb.set_amplitude(amp)

    def set_status_text(self, text: str) -> None:
        """Override the state label with arbitrary status text (short)."""
        safe = str(text or "").strip()[:100]
        if safe:
            self._state_lbl.setText(f"&#9679;  {safe}")

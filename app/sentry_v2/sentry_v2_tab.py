"""
SMART SENTRY V2.3.2 — Tab Widget (PyQt5 UI)

Self-contained tab for the main DADBOT application.
Provides:
  - Live video feed with overlay
  - Detection mode selector (all 11 modes from main app)
  - Target filter panel (class whitelist, confidence, size, zone)
  - Color detection settings (preset, min/max area, fusion)
  - Threat scoring tunables
  - Engagement settings with precision aiming
  - Guard position controls
  - Auto-trigger toggle
  - Trigger mode selector (Water MOSFET / Projectile BB)
  - Manual controls (D-pad, speed, LED, laser, safety, home, fire)
  - Status panel / engagement log
"""

from __future__ import annotations

from collections import deque
import json
import importlib
import os
import queue
import re
import subprocess
import sys
import tempfile
import threading
import time
import traceback
from pathlib import Path

from typing import Callable, Dict, Iterable, List, Optional, Tuple

import cv2
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QCheckBox, QSlider, QGroupBox, QFrame, QSizePolicy,
    QSpacerItem, QScrollArea, QDoubleSpinBox, QSpinBox,
    QComboBox, QListWidget, QListWidgetItem, QAbstractItemView,
    QTabWidget, QTabBar, QTextEdit, QGridLayout, QLineEdit, QSplitter, QMessageBox,
    QProgressBar,
    QFileDialog,
    QBoxLayout,
    QShortcut,
    QStyle,
    QStylePainter,
    QStyleOptionTab,
)
from PyQt5.QtCore import Qt, pyqtSignal, QTimer, QEvent, QObject, QProcess, QProcessEnvironment, QSize, QUrl, QRectF, QPointF, QRect, QPropertyAnimation, QEasingCurve, QThread
from PyQt5.QtGui import QImage, QPixmap, QColor, QIcon, QDesktopServices, QPainter, QPainterPath, QPen, QKeySequence, QCursor
try:
    from PyQt5.QtTextToSpeech import QTextToSpeech
except Exception:
    QTextToSpeech = None
try:
    from runtime_paths import app_root_path, runtime_root_path
except ImportError:
    from app.runtime_paths import app_root_path, runtime_root_path
try:
    from smart_sentry_meta import get_app_title, get_version
except ImportError:
    from app.smart_sentry_meta import get_app_title, get_version


def _windows_hidden_subprocess_kwargs() -> dict:
    if os.name != "nt":
        return {}
    kwargs: dict = {}
    creationflags = int(getattr(subprocess, "CREATE_NO_WINDOW", 0) or 0)
    if creationflags:
        kwargs["creationflags"] = creationflags
    startupinfo_cls = getattr(subprocess, "STARTUPINFO", None)
    if startupinfo_cls is not None:
        startupinfo = startupinfo_cls()
        startupinfo.dwFlags |= int(getattr(subprocess, "STARTF_USESHOWWINDOW", 0) or 0)
        startupinfo.wShowWindow = 0
        kwargs["startupinfo"] = startupinfo
    return kwargs

from .sentry_v2_config import (
    SentryV2Config,
    EngagementConfig,
    ThemeConfig,
    YOLO_COCO_CLASSES,
    NoFireMaskConfig,
    NoFireMaskVertex,
    PIRSensorConfig,
)
from .sentry_v2_engine import SentryV2Engine, SentryV2State
from .sentry_v2_overlay import SentryV2Overlay
from .sentry_v2_comm import SentryV2Comm
from .sentry_v2_detector import SentryV2Detector
from .sentry_v2_no_fire_masks import angular_vertex_from_normalized_point, project_mask_to_frame
from .prompted_targets import (
    PromptedMediaSelectionDialog,
    PromptedSelection,
    PromptedTargetLibrary,
    PromptedTargetMatcher,
)
from .sentry_v2_video_canvas import SentryV2VideoCanvas
from .simple_tracker import SimpleBBoxTracker
from .sound_engine import SentryV2SoundEngine
from .sentry_v2_tooltips import SENTRY_V2_TOOLTIPS
from .face_identity import FaceIdentityLibrary, FaceIdentityRuntime, FaceMatchResult
from .sentry_v2_config import (
    SENTRY_PAN_MAX,
    SENTRY_PAN_MIN,
    SENTRY_TILT_MAX,
    SENTRY_TILT_MIN,
)
from .target_filter import DetectedObject
from .assistant import AssistantReply, LocalAssistantService, OllamaClient


MANUAL_TRIGGER_SERVO_LATCH_MS = 160


class NoWheelScrollFilter(QObject):
    """Event filter to block mouse wheel scrolling on spinboxes and sliders."""
    def eventFilter(self, obj, event):
        if event.type() == QEvent.Wheel:
            return True  # Block the wheel event
        return super().eventFilter(obj, event)


class CompactSettingsTabWidget(QTabWidget):
    """Tab widget that stays compact because each settings page scrolls independently."""

    _MIN_COMPACT_HEIGHT = 360
    _MAX_COMPACT_HEIGHT = 640

    def _compact_height(self) -> int:
        tab_bar = self.tabBar()
        tab_height = 0
        if tab_bar is not None:
            estimated_tab_stack = max(220, self.count() * 38 + 32)
            tab_height = min(tab_bar.sizeHint().height(), estimated_tab_stack)
        current = self.currentWidget()
        page_height = 0
        if current is not None:
            page_height = max(current.minimumSizeHint().height(), current.sizeHint().height()) + 24
        return max(self._MIN_COMPACT_HEIGHT, tab_height, min(max(tab_height, page_height), self._MAX_COMPACT_HEIGHT))

    def minimumSizeHint(self) -> QSize:
        hint = super().minimumSizeHint()
        return QSize(hint.width(), self._compact_height())

    def sizeHint(self) -> QSize:
        hint = super().sizeHint()
        return QSize(hint.width(), self._compact_height())


class ResponsiveIconTabBar(QTabBar):
    """Top tab bar that grows icons and tab cells with the available panel width."""

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self.setDrawBase(False)
        self.setExpanding(True)
        self.setElideMode(Qt.ElideNone)

    def _metrics(self) -> Tuple[int, int, int]:
        count = max(1, self.count())
        parent = self.parentWidget()
        current_width = self.width()
        available_width = current_width if current_width > 0 else (parent.width() if parent is not None else 0)
        available_width = max(300, available_width)
        spacing_total = max(0, (count - 1) * 3)
        tab_width = max(40, int((available_width - spacing_total) / count))
        tab_height = max(48, min(92, int(tab_width * 0.84)))
        icon_size = max(20, min(42, int(min(tab_width, tab_height) * 0.56)))
        return tab_width, tab_height, icon_size

    def _sync_icon_size(self) -> None:
        _tab_width, _tab_height, icon_size = self._metrics()
        size = QSize(icon_size, icon_size)
        if self.iconSize() != size:
            self.setIconSize(size)

    def tabSizeHint(self, index: int) -> QSize:
        _ = index
        tab_width, tab_height, _icon_size = self._metrics()
        return QSize(tab_width, tab_height)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self._sync_icon_size()
        self.updateGeometry()

    def showEvent(self, event) -> None:
        super().showEvent(event)
        self._sync_icon_size()

    def tabInserted(self, index: int) -> None:
        super().tabInserted(index)
        self._sync_icon_size()

    def paintEvent(self, event) -> None:
        _ = event
        painter = QStylePainter(self)
        icon_size = self.iconSize()
        for index in range(self.count()):
            option = QStyleOptionTab()
            self.initStyleOption(option, index)
            icon = QIcon(option.icon)
            option.text = ""
            option.icon = QIcon()
            painter.drawControl(QStyle.CE_TabBarTabShape, option)
            if icon.isNull():
                continue
            icon_rect = QRect(
                option.rect.x() + max(0, (option.rect.width() - icon_size.width()) // 2),
                option.rect.y() + max(0, (option.rect.height() - icon_size.height()) // 2),
                icon_size.width(),
                icon_size.height(),
            )
            mode = QIcon.Normal if option.state & QStyle.State_Enabled else QIcon.Disabled
            state = QIcon.On if option.state & QStyle.State_Selected else QIcon.Off
            icon.paint(painter, icon_rect, Qt.AlignCenter, mode, state)


# Detection mode list (same indices as main app)
DETECTION_MODES: List[str] = [
    "Frame Difference",            # 0
    "Background Subtraction",      # 1
    "YOLO Object Detection",       # 2
    "Hybrid: Frame Diff + BackSub",# 3
    "Hybrid: Frame Diff + YOLO",   # 4
    "Hybrid: BackSub + YOLO (Best)",# 5
    "Color Detection",             # 6
    "Hybrid: Color + Frame Diff",  # 7
    "Hybrid: Color + BackSub",     # 8
    "Hybrid: Color + YOLO",        # 9
    "Motion-Locked Filtered Target",  # 10
]

STANDARD_CAMERA_RESOLUTIONS: List[Tuple[int, int]] = [
    (320, 240),
    (424, 240),
    (640, 360),
    (640, 480),
    (800, 600),
    (960, 540),
    (1280, 720),
    (1280, 800),
    (1280, 960),
    (1600, 900),
    (1920, 1080),
]

# Color presets available
COLOR_PRESETS: List[str] = [
    "any", "red", "green", "blue", "yellow", "orange", "purple",
    "cyan", "white", "black", "grey", "custom",
]

SOUND_PERSONALITY_OPTIONS: List[Tuple[str, str]] = [
    ("sentinel", "Sentinel"),
    ("hunter", "Hunter"),
    ("stealth", "Stealth"),
    ("playful", "Playful"),
]
SOUND_PERSONALITY_LABELS = {key: label for key, label in SOUND_PERSONALITY_OPTIONS}

HUMAN_VOICE_STYLE_PRESETS = {
    "neutral": {"label": "Neutral Assistant", "rate": 100, "pitch": 100, "volume": 85},
    "operator": {"label": "Quiet Operator", "rate": 92, "pitch": 94, "volume": 72},
    "alert": {"label": "Alert Guard", "rate": 108, "pitch": 102, "volume": 92},
    "warm": {"label": "Warm Greeter", "rate": 97, "pitch": 108, "volume": 86},
}

APP_ROOT_PATH = app_root_path()
RUNTIME_ROOT_PATH = runtime_root_path()

SMART_SENTRY_RELEASE_VERSION = get_version()
SMART_SENTRY_RELEASE_VERSION_TOKEN = SMART_SENTRY_RELEASE_VERSION.replace(".", "_")
CANONICAL_CUSTOM_PRESET_RELATIVE_PATH = f"app/config/smart_sentry_v{SMART_SENTRY_RELEASE_VERSION_TOKEN}_custom_presets.json"
CANONICAL_SETTINGS_RELATIVE_PATH = f"app/config/smart_sentry_v{SMART_SENTRY_RELEASE_VERSION_TOKEN}_settings.json"
CANONICAL_PROMPTED_TARGETS_RELATIVE_PATH = f"app/config/smart_sentry_v{SMART_SENTRY_RELEASE_VERSION_TOKEN}_prompted_targets.json"
CANONICAL_FACE_LIBRARY_RELATIVE_PATH = f"app/config/smart_sentry_v{SMART_SENTRY_RELEASE_VERSION_TOKEN}_faces.json"
CANONICAL_CUSTOM_PRESET_PATH = APP_ROOT_PATH / "config" / f"smart_sentry_v{SMART_SENTRY_RELEASE_VERSION_TOKEN}_custom_presets.json"
CANONICAL_SETTINGS_PATH = APP_ROOT_PATH / "config" / f"smart_sentry_v{SMART_SENTRY_RELEASE_VERSION_TOKEN}_settings.json"
CANONICAL_PROMPTED_TARGETS_PATH = APP_ROOT_PATH / "config" / f"smart_sentry_v{SMART_SENTRY_RELEASE_VERSION_TOKEN}_prompted_targets.json"
CANONICAL_FACE_LIBRARY_PATH = APP_ROOT_PATH / "config" / f"smart_sentry_v{SMART_SENTRY_RELEASE_VERSION_TOKEN}_faces.json"

SMART_SENTRY_V2_3_2_CUSTOM_PRESET_PATH = APP_ROOT_PATH / "config" / "smart_sentry_v2_3_2_custom_presets.json"
SMART_SENTRY_V2_3_1_CUSTOM_PRESET_PATH = APP_ROOT_PATH / "config" / "smart_sentry_v2_3_1_custom_presets.json"
LEGACY_SMART_SENTRY_V3_CUSTOM_PRESET_PATH = APP_ROOT_PATH / "config" / "smart_sentry_v3_custom_presets.json"
LEGACY_SENTRY_V2_CUSTOM_PRESET_PATH = APP_ROOT_PATH / "config" / "sentry_v2_custom_presets.json"
SMART_SENTRY_V2_3_2_SETTINGS_PATH = APP_ROOT_PATH / "config" / "smart_sentry_v2_3_2_settings.json"
SMART_SENTRY_V2_3_1_SETTINGS_PATH = APP_ROOT_PATH / "config" / "smart_sentry_v2_3_1_settings.json"
LEGACY_SMART_SENTRY_V3_SETTINGS_PATH = APP_ROOT_PATH / "config" / "smart_sentry_v3_settings.json"
LEGACY_SENTRY_V2_SETTINGS_PATH = APP_ROOT_PATH / "config" / "sentry_v2_settings.json"
SMART_SENTRY_V2_3_2_PROMPTED_TARGETS_PATH = APP_ROOT_PATH / "config" / "smart_sentry_v2_3_2_prompted_targets.json"
SMART_SENTRY_V2_3_1_PROMPTED_TARGETS_PATH = APP_ROOT_PATH / "config" / "smart_sentry_v2_3_1_prompted_targets.json"
LEGACY_SMART_SENTRY_V3_PROMPTED_TARGETS_PATH = APP_ROOT_PATH / "config" / "smart_sentry_v3_prompted_targets.json"
LEGACY_SENTRY_V2_PROMPTED_TARGETS_PATH = APP_ROOT_PATH / "config" / "sentry_v2_prompted_targets.json"
SMART_SENTRY_V2_3_2_FACE_LIBRARY_PATH = APP_ROOT_PATH / "config" / "smart_sentry_v2_3_2_faces.json"
SMART_SENTRY_SHORTCUT_KEYS_DOC_PATH = APP_ROOT_PATH.parent / "SMART_SENTRY_SHORTCUT_KEYS.md"
SENTRY_V2_SNAPSHOT_DIR = RUNTIME_ROOT_PATH / "snapshots"
SENTRY_V2_LOG_EXPORT_DIR = SENTRY_V2_SNAPSHOT_DIR / "serial_log_exports"
SENTRY_V2_PANEL_MIN_WIDTH = 420
SENTRY_V2_PANEL_DEFAULT_WIDTH = 520
SENTRY_V2_VIDEO_MIN_WIDTH = 180
SENTRY_V2_WIDGET_MIN_WIDTH = SENTRY_V2_PANEL_MIN_WIDTH + SENTRY_V2_VIDEO_MIN_WIDTH + 28
SMART_SENTRY_V2_WIFI_SSID = "SMART-SENTRY-V2.3"
SMART_SENTRY_V2_WIFI_PASSWORD = "db3000pass"
SMART_SENTRY_V3_WIFI_SSID = "SMART-SENTRY-V3"
SMART_SENTRY_V3_WIFI_PASSWORD = "smartv3pass"
SMART_SENTRY_RELEASE_TITLE = get_app_title("Smart Sentry")
SMART_SENTRY_RELEASE_SUBTITLE = "ESP32 WiFi + USB Control"
SMART_SENTRY_RELEASE_BADGE = ""


def _build_pin_assignment_dialog_content(mode_index: int, tokens: Dict[str, str]) -> Tuple[str, str]:
    heading_color = tokens.get("text", "#f5f7fa")
    body_color = tokens.get("subtle_text", heading_color)
    note_color = tokens.get("status_meta", body_color)
    accent_color = tokens.get("accent", heading_color)
    border_color = tokens.get("border", note_color)

    def section(title: str) -> str:
        return f"<div style='font-weight:700; color:{accent_color}; margin:10px 0 4px 0;'>{title}</div>"

    def row(label: str, description: str) -> str:
        return (
            "<tr>"
            f"<td style='padding:4px 8px; font-weight:700; color:{heading_color}; border-bottom:1px solid {border_color}; vertical-align:top;'>{label}</td>"
            f"<td style='padding:4px 8px; color:{body_color}; border-bottom:1px solid {border_color}; vertical-align:top;'>{description}</td>"
            "</tr>"
        )

    def table(*rows: str) -> str:
        return "<table style='border-collapse:collapse; width:100%; margin-bottom:8px;'>" + "".join(rows) + "</table>"

    pir_rows = table(
        row("PIR S1 / Sensor 0 / GPIO35", "Right zone cue (~45 deg). App logs show this as S1."),
        row("PIR S2 / Sensor 1 / GPIO34", "Front zone cue (~135 deg). App logs show this as S2."),
        row("PIR S3 / Sensor 2 / GPIO39 (VN)", "Left zone cue (~225 deg). ESP32 expansion board silk label: VN. App logs show this as S3."),
    )

    if mode_index == SentryV2Comm.MODE_WIFI_FULL:
        title = "Waveshare Pin Assignments"
        text = "".join([
            f"<div style='font-size:13px; line-height:1.4; color:{body_color};'>",
            f"<div style='font-weight:700; color:{heading_color}; margin-bottom:8px;'>Waveshare Servo Driver HAT single-board bridge</div>",
            f"<div style='margin-bottom:8px; color:{body_color};'>PC to bridge: WiFi/UDP on {SMART_SENTRY_V3_WIFI_SSID}<br>Pan/Tilt bus servos: local bus UART on GPIO18/GPIO19 at 1000000 baud<br>Use the Waveshare 40-pin header numbers exactly as shown here</div>",
            section("Header-backed outputs"),
            table(
                row("Header 7 / GPIO4", "Buzzer — passive buzzer / tone output"),
                row("Header 13 / GPIO27", "Trigger MOSFET — water-mode fire relay"),
                row("Header 22 / GPIO25", "Accessory relay"),
                row("Header 37 / GPIO26", "Spare relay"),
            ),
            section("Direct ESP32 GPIO outputs (not on 40-pin header)"),
            table(
                row("GPIO2", "Status LED — mirrors command activity"),
                row("GPIO13", "Trigger servo PWM (LEDC) — projectile fire"),
                row("GPIO12", "Pan servo PWM (LEDC)"),
                row("GPIO14", "Tilt servo PWM (LEDC)"),
                row("GPIO32", "LED relay — controlled via accessory commands"),
                row("GPIO33", "Laser relay — controlled via accessory commands"),
            ),
            f"<div style='color:{note_color}; margin:-2px 0 8px 0;'>GPIO32 and GPIO33 are direct ESP32 outputs. They are not exposed on the 40-pin header and require direct wiring to the ESP32 board.</div>",
            section("Communication"),
            table(
                row("GPIO16 (UART2 RX)", "Debug board TX — bus-servo UART bridge"),
                row("GPIO17 (UART2 TX)", "Debug board RX — bus-servo UART bridge"),
                row("GPIO18 / GPIO19", "Yahboom bus-servo alternative UART RX/TX"),
                row("Header 10 / GPIO15", "FlySky FS-iA6 i-Bus RX"),
                row("Header 8 / GPIO14", "Reserved RC TX / telemetry path"),
            ),
            section("Onboard PIR inputs (input-only)"),
            pir_rows,
            f"<div style='color:{note_color}; margin:-2px 0 8px 0;'>GPIO35, GPIO34, and GPIO39 are input-only lines. On the ESP32 expansion board, VN = GPIO39. They are not part of the 40-pin header output assignments.</div>",
            section("ADC current sense (input-only)"),
            table(
                row("GPIO36 (VP)", "Pan motor current sense ADC"),
                row("GPIO39 (VN)", "Tilt current sense ADC — disabled when PIR S3 active"),
                row("GPIO34", "Total current sense ADC — disabled when PIR S2 active"),
            ),
            section("Reserved"),
            table(
                row("Header 29 / GPIO5", "Speaker reserved only"),
                row("GPIO0", "BOOT button — reserved for boot strapping"),
            ),
            f"<div style='color:{note_color}; margin-top:8px;'>This is the current flashed Smart Sentry Waveshare map with all accessory pins shown.</div>",
            "</div>",
        ])
        return title, text

    if mode_index == SentryV2Comm.MODE_DUAL_ESP32_WIFI:
        title = "Dual ESP32 WiFi Pin Assignments"
        text = "".join([
            f"<div style='font-size:13px; line-height:1.4; color:{body_color};'>",
            f"<div style='font-weight:700; color:{heading_color}; margin-bottom:8px;'>Dual ESP32 WiFi topology</div>",
            f"<div style='margin-bottom:8px; color:{body_color};'>Primary ESP32 handles IO and accessories over WiFi.<br>Secondary ESP32 handles Yahboom bus-servo motion over its own WiFi bridge.</div>",
            section("Primary ESP32 — trigger outputs"),
            table(
                row("GPIO27", "Trigger MOSFET — water-mode fire relay"),
                row("GPIO13", "Trigger servo PWM (LEDC) — projectile fire"),
            ),
            section("Primary ESP32 — accessory outputs"),
            table(
                row("GPIO2", "Status LED — mirrors command activity"),
                row("GPIO4", "Buzzer — passive buzzer / tone output"),
                row("GPIO32", "LED relay — controlled via accessory commands"),
                row("GPIO33", "Laser relay — controlled via accessory commands"),
                row("GPIO25", "Accessory relay"),
                row("GPIO26", "Spare relay"),
            ),
            section("Primary ESP32 — servo PWM"),
            table(
                row("GPIO12", "Pan servo PWM (LEDC)"),
                row("GPIO14", "Tilt servo PWM (LEDC)"),
            ),
            section("Primary ESP32 — communication"),
            table(
                row("GPIO16 (UART2 RX)", "Debug board TX — bus-servo UART bridge"),
                row("GPIO17 (UART2 TX)", "Debug board RX — bus-servo UART bridge"),
                row("Secondary servo bridge", "Pan/Tilt Yahboom motion path via secondary ESP32"),
            ),
            section("Primary ESP32 PIR inputs (input-only)"),
            pir_rows,
            section("Primary ESP32 — ADC current sense (input-only)"),
            table(
                row("GPIO36 (VP)", "Pan motor current sense ADC"),
                row("GPIO39 (VN)", "Tilt current sense ADC — disabled when PIR S3 active"),
                row("GPIO34", "Total current sense ADC — disabled when PIR S2 active"),
            ),
            f"<div style='color:{note_color}; margin-top:8px;'>GPIO32/33 require direct wiring. PIR sensing follows GPIO35/GPIO34/GPIO39 on the primary ESP32.</div>",
            "</div>",
        ])
        return title, text

    if mode_index == SentryV2Comm.MODE_WIFI_DEBUG_USB:
        title = "WiFi IO Pin Assignments"
        text = "".join([
            f"<div style='font-size:13px; line-height:1.4; color:{body_color};'>",
            f"<div style='font-weight:700; color:{heading_color}; margin-bottom:8px;'>ESP32 WiFi IO with Debug Board USB motion</div>",
            f"<div style='margin-bottom:8px; color:{body_color};'>PC to ESP32: WiFi/UDP for trigger, PIR, and accessories<br>Debug Board to PC: USB serial for pan/tilt bus-servo motion</div>",
            section("Trigger outputs"),
            table(
                row("GPIO27", "Trigger MOSFET — water-mode fire relay"),
                row("GPIO13", "Trigger servo PWM (LEDC) — projectile fire"),
            ),
            section("Accessory outputs"),
            table(
                row("GPIO2", "Status LED — mirrors command activity"),
                row("GPIO4", "Buzzer — passive buzzer / tone output"),
                row("GPIO32", "LED relay — controlled via accessory commands"),
                row("GPIO33", "Laser relay — controlled via accessory commands"),
                row("GPIO25", "Accessory relay"),
                row("GPIO26", "Spare relay"),
            ),
            section("Communication — pan/tilt motion path"),
            table(
                row("GPIO16 (UART2 RX)", "Debug board TX — bus-servo UART bridge"),
                row("GPIO17 (UART2 TX)", "Debug board RX — bus-servo UART bridge"),
            ),
            f"<div style='color:{note_color}; margin:-2px 0 8px 0;'>Pan/tilt is driven by the Debug Board over USB serial. GPIO12 and GPIO14 (Waveshare servo header PWM) are not used in this mode.</div>",
            section("PIR inputs (input-only)"),
            pir_rows,
            f"<div style='color:{note_color}; margin:-2px 0 8px 0;'>ESP32 expansion board: VN = GPIO39. Compare GPIO35 (S1), GPIO34 (S2), GPIO39/VN (S3) if only one PIR fires.</div>",
            section("ADC current sense (input-only)"),
            table(
                row("GPIO36 (VP)", "Pan motor current sense ADC"),
                row("GPIO39 (VN)", "Tilt current sense ADC — disabled when PIR S3 active"),
                row("GPIO34", "Total current sense ADC — disabled when PIR S2 active"),
            ),
            f"<div style='color:{note_color}; margin-top:8px;'>GPIO32 (LED relay) and GPIO33 (Laser relay) require direct wiring to the ESP32 board — they are not on the standard debug board connector.</div>",
            "</div>",
        ])
        return title, text

    title = "Connection Pin Notes"
    text = "".join([
        f"<div style='font-size:13px; line-height:1.4; color:{body_color};'>",
        f"<div style='font-weight:700; color:{heading_color}; margin-bottom:8px;'>Current connection mode</div>",
        f"<div style='margin-bottom:8px; color:{body_color};'>This mode is USB-centered, so the key assignments live on the selected COM ports rather than on a WiFi bridge header map.</div>",
        table(
            row("ESP32 USB", "Primary ASCII IO link when using direct USB"),
            row("Debug Board USB", "Pan/Tilt bus-servo motion path in dual-USB layouts"),
        ),
        section("Complete ESP32 accessory map (all modes)"),
        table(
            row("GPIO2", "Status LED"),
            row("GPIO4", "Buzzer"),
            row("GPIO13", "Trigger servo PWM"),
            row("GPIO27", "Trigger MOSFET"),
            row("GPIO32", "LED relay"),
            row("GPIO33", "Laser relay"),
            row("GPIO25", "Accessory relay"),
            row("GPIO26", "Spare relay"),
            row("GPIO35", "PIR S1 — right zone"),
            row("GPIO34", "PIR S2 — front zone"),
            row("GPIO39 (VN)", "PIR S3 — left zone"),
        ),
        f"<div style='color:{note_color}; margin-top:8px;'>Switch to a WiFi mode to see the full sectioned pin map. Active PIR wiring: S1/GPIO35, S2/GPIO34, S3/GPIO39.</div>",
        "</div>",
    ])
    return title, text

SETTINGS_TAB_SPECS: List[Tuple[str, str, str]] = [
    ("Connection", "system", "#72decf"),
    ("Master Profiles", "profiles", "#b4efc0"),
    ("Detection Mode", "sensing", "#f2cf7c"),
    ("Target Library", "library", "#efb184"),
    ("Target Filter", "filter", "#9cc5ff"),
    ("Threat Scoring", "threat", "#8fdef2"),
    ("Engagement", "engage", "#ff9f9a"),
    ("Guard", "guard", "#8ed7bf"),
    ("Theme", "theme", "accent"),
    ("Manual Control", "command", "#dde7ef"),
    ("Facial Recognition", "facial", "#f6a6db"),
    ("Shortcut Keys", "shortcuts", "#a5b2ff"),
    ("AI Assistant", "ai", "#95e3f4"),
]

SETTINGS_TAB_NAV_LABELS = {
    "Connection": "CONNECTION",
    "Master Profiles": "MASTER PROFILES",
    "Detection Mode": "DETECTION MODE",
    "Target Library": "TARGET LIBRARY",
    "Target Filter": "TARGET FILTER",
    "Threat Scoring": "THREAT SCORING",
    "Engagement": "ENGAGEMENT",
    "Guard": "GUARD",
    "Theme": "THEME",
    "Manual Control": "MANUAL CONTROL",
    "Facial Recognition": "FACIAL RECOGNITION",
    "Shortcut Keys": "SHORTCUT KEYS",
    "AI Assistant": "AI ASSISTANT",
}

# Release-hold convention: keep unfinished tabs out of the active release UI until validated.
SETTINGS_TAB_RELEASE_HOLDS: Dict[str, Dict[str, str]] = {
    "Facial Recognition": {
        "badge": "Release Hold",
        "message": f"Temporarily disabled for the Smart Sentry v{SMART_SENTRY_RELEASE_VERSION} release while the face-recognition workflow completes release validation.",
    },
    "AI Assistant": {
        "badge": "Release Hold",
        "message": f"Temporarily disabled for the Smart Sentry v{SMART_SENTRY_RELEASE_VERSION} release while the local assistant workflow completes release validation.",
    },
}

SERIAL_LOG_FILTER_SPECS: List[Tuple[str, str]] = [
    ("all", "All"),
    ("system", "System"),
    ("pir", "PIR"),
    ("movement", "Move"),
    ("camera", "Camera"),
    ("safety", "Safety"),
    ("accessory", "Accessory"),
]


def _build_settings_tab_icon(icon_key: str, color_value: str, size: int = 18) -> QIcon:
    color = QColor(color_value)
    stroke = QPen(color)
    stroke.setWidthF(max(1.3, size * 0.10))
    stroke.setCapStyle(Qt.RoundCap)
    stroke.setJoinStyle(Qt.RoundJoin)

    fill = QColor(color)
    fill.setAlpha(58)

    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.transparent)

    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing, True)
    painter.setPen(stroke)
    painter.setBrush(fill)

    unit = float(size)
    left = unit * 0.16
    top = unit * 0.16
    right = unit * 0.84
    bottom = unit * 0.84
    center_x = unit * 0.50
    center_y = unit * 0.50

    if icon_key == "system":
        screen = QRectF(unit * 0.18, unit * 0.22, unit * 0.64, unit * 0.38)
        painter.drawRoundedRect(screen, 2.2, 2.2)
        painter.drawLine(QPointF(unit * 0.50, unit * 0.60), QPointF(unit * 0.50, unit * 0.74))
        painter.drawLine(QPointF(unit * 0.34, unit * 0.74), QPointF(unit * 0.66, unit * 0.74))
    elif icon_key == "profiles":
        for offset in (0.00, 0.10, 0.20):
            rect = QRectF(unit * (0.16 + offset), unit * (0.18 + offset), unit * 0.42, unit * 0.30)
            painter.drawRoundedRect(rect, 2.0, 2.0)
    elif icon_key == "sensing":
        eye = QPainterPath()
        eye.moveTo(left, center_y)
        eye.quadTo(QPointF(center_x, top), QPointF(right, center_y))
        eye.quadTo(QPointF(center_x, bottom), QPointF(left, center_y))
        painter.drawPath(eye)
        painter.setBrush(color)
        painter.drawEllipse(QRectF(unit * 0.42, unit * 0.42, unit * 0.16, unit * 0.16))
        painter.setBrush(fill)
    elif icon_key == "library":
        folder = QPainterPath()
        folder.moveTo(unit * 0.16, unit * 0.34)
        folder.lineTo(unit * 0.36, unit * 0.34)
        folder.lineTo(unit * 0.42, unit * 0.26)
        folder.lineTo(unit * 0.82, unit * 0.26)
        folder.lineTo(unit * 0.82, unit * 0.74)
        folder.lineTo(unit * 0.16, unit * 0.74)
        folder.closeSubpath()
        painter.drawPath(folder)
    elif icon_key == "filter":
        funnel = QPainterPath()
        funnel.moveTo(unit * 0.18, unit * 0.24)
        funnel.lineTo(unit * 0.82, unit * 0.24)
        funnel.lineTo(unit * 0.58, unit * 0.48)
        funnel.lineTo(unit * 0.58, unit * 0.76)
        funnel.lineTo(unit * 0.42, unit * 0.66)
        funnel.lineTo(unit * 0.42, unit * 0.48)
        funnel.closeSubpath()
        painter.drawPath(funnel)
    elif icon_key == "threat":
        shield = QPainterPath()
        shield.moveTo(center_x, unit * 0.14)
        shield.lineTo(unit * 0.78, unit * 0.26)
        shield.lineTo(unit * 0.72, unit * 0.62)
        shield.quadTo(QPointF(center_x, unit * 0.86), QPointF(unit * 0.28, unit * 0.62))
        shield.lineTo(unit * 0.22, unit * 0.26)
        shield.closeSubpath()
        painter.drawPath(shield)
        painter.drawLine(QPointF(center_x, unit * 0.30), QPointF(center_x, unit * 0.56))
        painter.drawPoint(QPointF(center_x, unit * 0.70))
    elif icon_key == "engage":
        painter.drawEllipse(QRectF(unit * 0.24, unit * 0.24, unit * 0.52, unit * 0.52))
        painter.drawLine(QPointF(center_x, unit * 0.10), QPointF(center_x, unit * 0.32))
        painter.drawLine(QPointF(center_x, unit * 0.68), QPointF(center_x, unit * 0.90))
        painter.drawLine(QPointF(unit * 0.10, center_y), QPointF(unit * 0.32, center_y))
        painter.drawLine(QPointF(unit * 0.68, center_y), QPointF(unit * 0.90, center_y))
    elif icon_key == "guard":
        painter.drawArc(QRectF(unit * 0.30, unit * 0.16, unit * 0.40, unit * 0.36), 30 * 16, 120 * 16)
        painter.drawRoundedRect(QRectF(unit * 0.24, unit * 0.42, unit * 0.52, unit * 0.34), 2.4, 2.4)
    elif icon_key == "theme":
        painter.drawEllipse(QRectF(unit * 0.16, unit * 0.18, unit * 0.60, unit * 0.60))
        painter.setBrush(color)
        for dot_x, dot_y in ((0.34, 0.32), (0.50, 0.28), (0.58, 0.42)):
            painter.drawEllipse(QRectF(unit * dot_x, unit * dot_y, unit * 0.08, unit * 0.08))
        painter.setBrush(fill)
        painter.drawEllipse(QRectF(unit * 0.48, unit * 0.54, unit * 0.26, unit * 0.18))
    elif icon_key == "command":
        for line_x, knob_y in ((0.28, 0.36), (0.50, 0.56), (0.72, 0.30)):
            painter.drawLine(QPointF(unit * line_x, unit * 0.20), QPointF(unit * line_x, unit * 0.80))
            painter.setBrush(color)
            painter.drawEllipse(QRectF(unit * (line_x - 0.07), unit * (knob_y - 0.07), unit * 0.14, unit * 0.14))
            painter.setBrush(fill)
    elif icon_key == "facial":
        painter.drawEllipse(QRectF(unit * 0.28, unit * 0.18, unit * 0.44, unit * 0.38))
        painter.drawArc(QRectF(unit * 0.32, unit * 0.34, unit * 0.36, unit * 0.22), 200 * 16, 140 * 16)
        painter.drawLine(QPointF(unit * 0.18, unit * 0.24), QPointF(unit * 0.28, unit * 0.24))
        painter.drawLine(QPointF(unit * 0.18, unit * 0.24), QPointF(unit * 0.18, unit * 0.34))
        painter.drawLine(QPointF(unit * 0.82, unit * 0.24), QPointF(unit * 0.72, unit * 0.24))
        painter.drawLine(QPointF(unit * 0.82, unit * 0.24), QPointF(unit * 0.82, unit * 0.34))
        painter.drawLine(QPointF(unit * 0.18, unit * 0.76), QPointF(unit * 0.28, unit * 0.76))
        painter.drawLine(QPointF(unit * 0.18, unit * 0.76), QPointF(unit * 0.18, unit * 0.66))
        painter.drawLine(QPointF(unit * 0.82, unit * 0.76), QPointF(unit * 0.72, unit * 0.76))
        painter.drawLine(QPointF(unit * 0.82, unit * 0.76), QPointF(unit * 0.82, unit * 0.66))
    elif icon_key == "shortcuts":
        painter.drawRoundedRect(QRectF(unit * 0.16, unit * 0.24, unit * 0.68, unit * 0.48), 3.0, 3.0)
        for key_x in (0.26, 0.42, 0.58):
            painter.drawRoundedRect(QRectF(unit * key_x, unit * 0.34, unit * 0.10, unit * 0.12), 1.8, 1.8)
        painter.drawRoundedRect(QRectF(unit * 0.26, unit * 0.52, unit * 0.38, unit * 0.10), 1.8, 1.8)
    elif icon_key == "ai":
        painter.drawRoundedRect(QRectF(unit * 0.22, unit * 0.18, unit * 0.56, unit * 0.50), 3.0, 3.0)
        painter.drawLine(QPointF(unit * 0.34, unit * 0.68), QPointF(unit * 0.28, unit * 0.82))
        painter.drawLine(QPointF(unit * 0.66, unit * 0.68), QPointF(unit * 0.72, unit * 0.82))
        painter.drawLine(QPointF(unit * 0.50, unit * 0.68), QPointF(unit * 0.50, unit * 0.86))
        painter.drawEllipse(QRectF(unit * 0.34, unit * 0.34, unit * 0.08, unit * 0.08))
        painter.drawEllipse(QRectF(unit * 0.58, unit * 0.34, unit * 0.08, unit * 0.08))
        painter.drawArc(QRectF(unit * 0.38, unit * 0.38, unit * 0.24, unit * 0.18), 210 * 16, 120 * 16)
    else:
        painter.drawRoundedRect(QRectF(unit * 0.22, unit * 0.22, unit * 0.56, unit * 0.56), 3.0, 3.0)

    painter.end()
    return QIcon(pixmap)


def _clamp_int_range(value: float, minimum: int, maximum: int) -> int:
    return max(minimum, min(maximum, int(round(value))))

DETECTION_PRESETS = {
    "frame_diff": {
        "label": "Frame Difference",
        "description": "Strict raw motion-only detection tuned to ignore slow drift and background noise.",
        "tooltip_key": "preset_detection_frame_diff",
        "settings": {
            "detection_mode": 0,
            "min_contour_area": 920.0,
            "max_contour_area": 6800.0,
            "yolo_min_area": 180,
            "yolo_confidence": 0.60,
            "color_preset": "any",
            "color_min_area": 160,
            "color_max_area": 18000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 20,
            "motion_ignore_after_move_s": 0.24,
            "motion_gate_threshold": 2.2,
        },
    },
    "backsub": {
        "label": "Background Subtraction",
        "description": "Foreground extraction tuned to reject shadow noise and broad scene shimmer.",
        "tooltip_key": "preset_detection_backsub",
        "settings": {
            "detection_mode": 1,
            "min_contour_area": 720.0,
            "max_contour_area": 5400.0,
            "yolo_min_area": 180,
            "yolo_confidence": 0.56,
            "color_preset": "any",
            "color_min_area": 160,
            "color_max_area": 18000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 20,
            "motion_ignore_after_move_s": 0.24,
            "motion_gate_threshold": 1.15,
        },
    },
    "yolo": {
        "label": "YOLO Precision",
        "description": "High-certainty class-driven detection that heavily favors confident object IDs.",
        "tooltip_key": "preset_detection_yolo",
        "settings": {
            "detection_mode": 2,
            "min_contour_area": 468.0,
            "max_contour_area": 4680.0,
            "yolo_min_area": 220,
            "yolo_confidence": 0.58,
            "color_preset": "any",
            "color_min_area": 120,
            "color_max_area": 20000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 15,
            "motion_ignore_after_move_s": 0.06,
            "motion_gate_threshold": 1.0,
        },
    },
    "dual_motion": {
        "label": "Dual Motion",
        "description": "Two-stage motion confirmation for conservative motion tracking.",
        "tooltip_key": "preset_detection_dual_motion",
        "settings": {
            "detection_mode": 3,
            "min_contour_area": 1180.0,
            "max_contour_area": 8200.0,
            "yolo_min_area": 180,
            "yolo_confidence": 0.58,
            "color_preset": "any",
            "color_min_area": 160,
            "color_max_area": 24000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 20,
            "motion_ignore_after_move_s": 0.22,
            "motion_gate_threshold": 1.9,
        },
    },
    "motion_yolo": {
        "label": "Motion-Gated YOLO",
        "description": "YOLO is only trusted after a meaningful motion gate is crossed.",
        "tooltip_key": "preset_detection_motion_yolo",
        "settings": {
            "detection_mode": 4,
            "min_contour_area": 624.0,
            "max_contour_area": 6240.0,
            "yolo_min_area": 260,
            "yolo_confidence": 0.60,
            "color_preset": "any",
            "color_min_area": 140,
            "color_max_area": 22000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 20,
            "motion_ignore_after_move_s": 0.10,
            "motion_gate_threshold": 2.4,
        },
    },
    "best_hybrid": {
        "label": "Best Hybrid YOLO",
        "description": "Most permissive hybrid stack, intended to find and keep targets quickly.",
        "tooltip_key": "preset_detection_best_hybrid",
        "settings": {
            "detection_mode": 5,
            "min_contour_area": 420.0,
            "max_contour_area": 4200.0,
            "yolo_min_area": 95,
            "yolo_confidence": 0.34,
            "color_preset": "any",
            "color_min_area": 140,
            "color_max_area": 22000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 15,
            "motion_ignore_after_move_s": 0.06,
            "motion_gate_threshold": 0.55,
        },
    },
    "color": {
        "label": "Color Watch",
        "description": "Pure color-mask tracking for color-tuned objects (not class-aware).",
        "tooltip_key": "preset_detection_color",
        "settings": {
            "detection_mode": 6,
            "min_contour_area": 468.0,
            "max_contour_area": 4680.0,
            "yolo_min_area": 180,
            "yolo_confidence": 0.45,
            "color_preset": "red",
            "color_min_area": 220,
            "color_max_area": 20000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 25,
            "motion_ignore_after_move_s": 0.04,
            "motion_gate_threshold": 1.0,
        },
    },
    "color_motion": {
        "label": "Color + Motion",
        "description": "Color mask plus frame-diff motion for moving colored objects. With the shipped red-color preset and a specific color selected, detections must overlap both the selected color and motion before they count.",
        "tooltip_key": "preset_detection_color_motion",
        "settings": {
            "detection_mode": 7,
            "min_contour_area": 310.0,
            "max_contour_area": 3100.0,
            "yolo_min_area": 180,
            "yolo_confidence": 0.45,
            "color_preset": "red",
            "color_min_area": 30,
            "color_max_area": 14000,
            "color_fusion_strategy": "OR",
            "color_fusion_overlap": 10,
            "motion_ignore_after_move_s": 0.02,
            "motion_gate_threshold": 0.8,
        },
    },
    "color_backsub": {
        "label": "Color + Background",
        "description": "Color mask plus foreground agreement for moving colored objects. With the shipped red-color preset and a specific color selected, detections must overlap both the selected color and foreground motion.",
        "tooltip_key": "preset_detection_color_backsub",
        "settings": {
            "detection_mode": 8,
            "min_contour_area": 468.0,
            "max_contour_area": 4680.0,
            "yolo_min_area": 180,
            "yolo_confidence": 0.45,
            "color_preset": "red",
            "color_min_area": 120,
            "color_max_area": 20000,
            "color_fusion_strategy": "OR",
            "color_fusion_overlap": 12,
            "motion_ignore_after_move_s": 0.02,
            "motion_gate_threshold": 1.0,
        },
    },
    "color_yolo": {
        "label": "Color + YOLO",
        "description": "Color mask fused with YOLO for class-aware colored-object follow. With the shipped red-color preset and a specific color selected, detections must overlap both the selected color and the YOLO box.",
        "tooltip_key": "preset_detection_color_yolo",
        "settings": {
            "detection_mode": 9,
            "min_contour_area": 468.0,
            "max_contour_area": 4680.0,
            "yolo_min_area": 90,
            "yolo_confidence": 0.36,
            "color_preset": "red",
            "color_min_area": 100,
            "color_max_area": 20000,
            "color_fusion_strategy": "OR",
            "color_fusion_overlap": 10,
            "motion_ignore_after_move_s": 0.02,
            "motion_gate_threshold": 1.0,
        },
    },
    "motion_locked": {
        "label": "Motion-Locked Filtered",
        "description": "Filtered sentry mode that favors a single credible moving target over raw volume.",
        "tooltip_key": "preset_detection_motion_locked",
        "settings": {
            "detection_mode": 10,
            "min_contour_area": 820.0,
            "max_contour_area": 6200.0,
            "yolo_min_area": 180,
            "yolo_confidence": 0.48,
            "color_preset": "any",
            "color_min_area": 110,
            "color_max_area": 20000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 12,
            "motion_ignore_after_move_s": 0.12,
            "motion_gate_threshold": 1.85,
        },
    },
    "observer_motion_watch": {
        "label": "Observer Motion Watch",
        "description": "Wide-motion observer mode for tiny and far movers, even when YOLO cannot classify them.",
        "tooltip_key": "preset_detection_observer_motion_watch",
        "settings": {
            "detection_mode": 1,
            "min_contour_area": 36.0,
            "max_contour_area": 120000.0,
            "yolo_min_area": 0,
            "yolo_confidence": 0.18,
            "color_preset": "any",
            "color_min_area": 24,
            "color_max_area": 240000,
            "color_fusion_strategy": "OR",
            "color_fusion_overlap": 8,
            "motion_ignore_after_move_s": 0.02,
            "motion_gate_threshold": 0.35,
        },
    },
    "dog_follow": {
        "label": "Dog Follow",
        "description": "Motion-locked YOLO tuned for medium/large moving dogs with stable center follow.",
        "tooltip_key": "preset_detection_dog_follow",
        "settings": {
            "detection_mode": 10,
            "min_contour_area": 936.0,
            "max_contour_area": 9360.0,
            "yolo_min_area": 140,
            "yolo_confidence": 0.40,
            "color_preset": "any",
            "color_min_area": 120,
            "color_max_area": 24000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 12,
            "motion_ignore_after_move_s": 0.03,
            "motion_gate_threshold": 1.0,
        },
    },
    "cat_follow": {
        "label": "Cat Follow",
        "description": "Motion-locked YOLO tuned for smaller agile cats with tighter small-target tracking.",
        "tooltip_key": "preset_detection_cat_follow",
        "settings": {
            "detection_mode": 10,
            "min_contour_area": 650.0,
            "max_contour_area": 6500.0,
            "yolo_min_area": 70,
            "yolo_confidence": 0.34,
            "color_preset": "any",
            "color_min_area": 80,
            "color_max_area": 18000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 10,
            "motion_ignore_after_move_s": 0.02,
            "motion_gate_threshold": 0.9,
        },
    },
    "rat_like_follow": {
        "label": "Rat-Like Small Follow",
        "description": "Small-rat YOLO tracker using permissive tiny-area gating so tracking stays live even when the rat pauses.",
        "tooltip_key": "preset_detection_rat_like_follow",
        "settings": {
            "detection_mode": 2,
            "min_contour_area": 234.0,
            "max_contour_area": 2340.0,
            "yolo_min_area": 12,
            "yolo_confidence": 0.18,
            "color_preset": "any",
            "color_min_area": 35,
            "color_max_area": 10000,
            "color_fusion_strategy": "OR",
            "color_fusion_overlap": 8,
            "motion_ignore_after_move_s": 0.01,
            "motion_gate_threshold": 0.7,
        },
    },
    "person_yolo": {
        "label": "Person YOLO",
        "description": "Pure YOLO detection tuned for person-class tracking at any range. Lower confidence gate catches partially occluded and distant subjects. Minimum-area gate filters noise while still allowing a person at 8–10 m. No motion gate — YOLO confidence is the sole trigger so stationary people are tracked continuously.",
        "tooltip_key": "preset_detection_person_yolo",
        "settings": {
            "detection_mode": 2,
            "min_contour_area": 2340.0,
            "max_contour_area": 0.0,
            "yolo_min_area": 1200,
            "yolo_confidence": 0.44,
            "color_preset": "any",
            "color_min_area": 160,
            "color_max_area": 60000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 15,
            "motion_ignore_after_move_s": 0.08,
            "motion_gate_threshold": 1.0,
        },
    },
}

# Method-scoped baseline presets used to generate size variants.
MODE_BASE_PRESET: dict[int, str] = {
    0: "frame_diff",
    1: "backsub",
    2: "yolo",
    3: "dual_motion",
    4: "motion_yolo",
    5: "best_hybrid",
    6: "color",
    7: "color_motion",
    8: "color_backsub",
    9: "color_yolo",
    10: "motion_locked",
}

# Per-method target-size profiles. Multipliers are applied on top of
# the method baseline preset so each detection method has consistent
# size options while preserving method-specific behavior.
TARGET_SIZE_PRESETS = {
    "small": {
        "label": "Small Target",
        "description": "Raised small-target sizing floor for compact targets, with a tighter upper size cap than the larger bands.",
        "min_scale": 0.85,
        "max_scale": 0.90,
        "yolo_conf_delta": 0.02,
    },
    "medium": {
        "label": "Medium Target",
        "description": "Raised medium-target sizing floor; starts where the previous large band began.",
        "min_scale": 2.60,
        "max_scale": 1.80,
        "yolo_conf_delta": 0.08,
    },
    "large": {
        "label": "Large Target",
        "description": "Highest target-size floor for only the biggest close-range detections, suppressing medium and small clutter.",
        "min_scale": 5.20,
        "max_scale": 3.60,
        "yolo_conf_delta": 0.14,
    },
}

SNIPER_CENTER_RADIUS_PRESETS = {
    "small": 0.045,
    "medium": 0.060,
    "large": 0.080,
}

TARGET_FILTER_PRESETS = {
    "wide_net": {
        "label": "Wide Net",
        "description": "Almost no filtering; use this when you want maximum candidate volume.",
        "tooltip_key": "preset_filter_wide_net",
        "settings": {
            "allowed_classes": [],
            "min_confidence": 0.22,
            "min_size_ratio": 0.00005,
            "max_size_ratio": 0.15,
        },
    },
    "observer_all_movers": {
        "label": "Observer All Movers",
        "description": "Observation filter that accepts any moving object and keeps tiny or far targets in play.",
        "tooltip_key": "preset_filter_observer_all_movers",
        "settings": {
            "allowed_classes": [],
            "min_confidence": 0.18,
            "min_size_ratio": 0.0,
            "max_size_ratio": 0.0,
            "shape_filter_enabled": False,
            "shape_profile_name": "",
            "semantic_min_confirm_frames": 1,
            "semantic_min_confirm_confidence": 0.0,
            "semantic_confirm_ttl_s": 0.6,
        },
    },
    "human_focus": {
        "label": "Human Focus",
        "description": "Rejects everything except person-class detections. Confidence gate lowered to accept partially visible or side-on subjects while the shape filter still rejects any box wider than it is tall.",
        "tooltip_key": "preset_filter_human_focus",
        "settings": {
            "allowed_classes": ["person"],
            "min_confidence": 0.52,
            "min_size_ratio": 0.001,
            "max_size_ratio": 0.35,
            "shape_filter_enabled": True,
            "shape_profile_name": "person",
            "semantic_min_confirm_frames": 2,
            "semantic_min_confirm_confidence": 0.58,
            "semantic_confirm_ttl_s": 0.8,
        },
    },
    "car_focus": {
        "label": "Car Focus",
        "description": "Single-class car filter with shape and confirmation safety.",
        "tooltip_key": "preset_filter_car_focus",
        "settings": {
            "allowed_classes": ["car"],
            "min_confidence": 0.54,
            "min_size_ratio": 0.003,
            "max_size_ratio": 0.0,
            "shape_filter_enabled": True,
            "shape_profile_name": "car",
            "semantic_min_confirm_frames": 2,
            "semantic_min_confirm_confidence": 0.60,
            "semantic_confirm_ttl_s": 0.8,
        },
    },
    "vehicle_watch": {
        "label": "Vehicle Watch",
        "description": "Keeps only large vehicle classes and drops small-object clutter.",
        "tooltip_key": "preset_filter_vehicle_watch",
        "settings": {
            "allowed_classes": ["car", "truck", "bus", "motorcycle", "bicycle"],
            "min_confidence": 0.52,
            "min_size_ratio": 0.005,
            "max_size_ratio": 0.0,
        },
    },
    "small_movers": {
        "label": "Small Movers",
        "description": "Prefers small distant movers that stricter filters would ignore.",
        "tooltip_key": "preset_filter_small_movers",
        "settings": {
            "allowed_classes": ["dog", "dogs", "cat", "cats", "bird", "sports ball"],
            "min_confidence": 0.22,
            "min_size_ratio": 0.00008,
            "max_size_ratio": 0.08,
        },
    },
    "large_close": {
        "label": "Large Close",
        "description": "Only dominant nearby targets survive this filter.",
        "tooltip_key": "preset_filter_large_close",
        "settings": {
            "allowed_classes": [],
            "min_confidence": 0.72,
            "min_size_ratio": 0.015,
            "max_size_ratio": 0.30,
        },
    },
    "dog_focus": {
        "label": "Dog Focus",
        "description": "Class-locked dog tracking with medium target-size constraints.",
        "tooltip_key": "preset_filter_dog_focus",
        "settings": {
            "allowed_classes": ["dog", "dogs"],
            "min_confidence": 0.40,
            "min_size_ratio": 0.0003,
            "max_size_ratio": 0.10,
            "shape_filter_enabled": True,
            "shape_profile_name": "dog",
            "semantic_min_confirm_frames": 2,
            "semantic_min_confirm_confidence": 0.48,
            "semantic_confirm_ttl_s": 0.8,
        },
    },
    "cat_focus": {
        "label": "Cat Focus",
        "description": "Class-locked cat tracking with tighter small-target size constraints.",
        "tooltip_key": "preset_filter_cat_focus",
        "settings": {
            "allowed_classes": ["cat", "cats"],
            "min_confidence": 0.34,
            "min_size_ratio": 0.00015,
            "max_size_ratio": 0.06,
            "shape_filter_enabled": True,
            "shape_profile_name": "cat",
            "semantic_min_confirm_frames": 2,
            "semantic_min_confirm_confidence": 0.42,
            "semantic_confirm_ttl_s": 0.8,
        },
    },
    "bird_focus": {
        "label": "Bird Focus",
        "description": "Class-locked bird tracking with shape and confirmation safety.",
        "tooltip_key": "preset_filter_bird_focus",
        "settings": {
            "allowed_classes": ["bird", "birds"],
            "min_confidence": 0.34,
            "min_size_ratio": 0.00008,
            "max_size_ratio": 0.05,
            "shape_filter_enabled": True,
            "shape_profile_name": "bird",
            "semantic_min_confirm_frames": 2,
            "semantic_min_confirm_confidence": 0.42,
            "semantic_confirm_ttl_s": 0.8,
        },
    },
    "rat_like_motion": {
        "label": "Rat-Like Motion",
        "description": "Rat class-focused tiny-target filter tuned for the ratdogcat animal model.",
        "tooltip_key": "preset_filter_rat_like_motion",
        "settings": {
            "allowed_classes": ["rat"],
            "min_confidence": 0.18,
            "min_size_ratio": 0.00005,
            "max_size_ratio": 0.04,
            "shape_filter_enabled": True,
            "shape_profile_name": "rat",
            "semantic_min_confirm_frames": 3,
            "semantic_min_confirm_confidence": 0.72,
            "semantic_confirm_ttl_s": 0.8,
        },
    },
    "person_focus_closest": {
        "label": "Person — Closest First",
        "description": "Person-class lock with no upper size limit so the closest person filling most of the frame is still tracked. Confidence gate is permissive enough to keep walking, crouching, or partially occluded subjects in play. Confirm in a single strong frame for fast-walking responsiveness.",
        "tooltip_key": "preset_filter_person_focus_closest",
        "settings": {
            "allowed_classes": ["person"],
            "min_confidence": 0.44,
            "min_size_ratio": 0.0015,
            "max_size_ratio": 0.0,
            "shape_filter_enabled": True,
            "shape_profile_name": "person",
            "semantic_min_confirm_frames": 1,
            "semantic_min_confirm_confidence": 0.48,
            "semantic_confirm_ttl_s": 1.0,
        },
    },
    "sniper_small_motion": {
        "label": "Sniper Small Motion/Color",
        "description": "Size-only sniper filter for tiny rodent-scale targets in motion/color modes.",
        "tooltip_key": "preset_filter_sniper_small_motion",
        "settings": {
            "allowed_classes": [],
            "min_confidence": 0.32,
            "min_size_ratio": 0.00005,
            "max_size_ratio": 0.04,
        },
    },
    "sniper_medium_motion": {
        "label": "Sniper Medium Motion/Color",
        "description": "Size-only sniper filter for medium cat/dog scale targets in motion/color modes.",
        "tooltip_key": "preset_filter_sniper_medium_motion",
        "settings": {
            "allowed_classes": [],
            "min_confidence": 0.40,
            "min_size_ratio": 0.0002,
            "max_size_ratio": 0.10,
        },
    },
    "sniper_large_motion": {
        "label": "Sniper Large Motion/Color",
        "description": "Size-only sniper filter for person-scale targets in motion/color modes.",
        "tooltip_key": "preset_filter_sniper_large_motion",
        "settings": {
            "allowed_classes": [],
            "min_confidence": 0.50,
            "min_size_ratio": 0.001,
            "max_size_ratio": 0.0,
        },
    },
    "sniper_small_rodent": {
        "label": "Sniper Small Rodent",
        "description": "Class-locked sniper filter for rat/small-rodent style detections.",
        "tooltip_key": "preset_filter_sniper_small_rodent",
        "settings": {
            "allowed_classes": ["rat", "mouse"],
            "min_confidence": 0.30,
            "min_size_ratio": 0.00005,
            "max_size_ratio": 0.04,
            "shape_filter_enabled": True,
            "shape_profile_name": "rat",
            "semantic_min_confirm_frames": 3,
            "semantic_min_confirm_confidence": 0.68,
            "semantic_confirm_ttl_s": 0.8,
        },
    },
    "sniper_medium_pet": {
        "label": "Sniper Medium Cat/Dog",
        "description": "Class-locked sniper filter for medium cat/dog targets.",
        "tooltip_key": "preset_filter_sniper_medium_pet",
        "settings": {
            "allowed_classes": ["cat", "cats", "dog", "dogs"],
            "min_confidence": 0.44,
            "min_size_ratio": 0.0002,
            "max_size_ratio": 0.10,
        },
    },
    "sniper_large_person": {
        "label": "Sniper Large Person",
        "description": "Class-locked sniper filter for person targets with no upper size ceiling. Stricter than person_focus_closest — requires two consecutive confirmed frames before the target is live, making it appropriate for precision fire contexts.",
        "tooltip_key": "preset_filter_sniper_large_person",
        "settings": {
            "allowed_classes": ["person"],
            "min_confidence": 0.50,
            "min_size_ratio": 0.0015,
            "max_size_ratio": 0.0,
            "shape_filter_enabled": True,
            "shape_profile_name": "person",
            "semantic_min_confirm_frames": 2,
            "semantic_min_confirm_confidence": 0.56,
            "semantic_confirm_ttl_s": 0.9,
        },
    },
}

BUS_SERVO_TIME_PRESETS = {
    "smooth": {
        "label": "Smooth",
        "description": "Deliberately slow motion for visibly measured tracking.",
        "tooltip_key": "preset_servo_smooth",
        "move_time_ms": 110,
    },
    "balanced": {
        "label": "Balanced",
        "description": "Moderate movement timing for general sentry use.",
        "tooltip_key": "preset_servo_balanced",
        "move_time_ms": 60,
    },
    "fast": {
        "label": "Fast",
        "description": "Fast, obvious snap response for aggressive tracking.",
        "tooltip_key": "preset_servo_fast",
        "move_time_ms": 28,
    },
}

_DEFAULT_ENGAGEMENT_LIMITS = EngagementConfig()
_PRECISION_TILT_STEP_RATIO = float(_DEFAULT_ENGAGEMENT_LIMITS.precision_max_tilt_step) / max(
    0.001,
    float(_DEFAULT_ENGAGEMENT_LIMITS.precision_max_pan_step),
)


def _normalize_engagement_precision_limits(settings: dict, raw_settings: Optional[dict] = None) -> dict:
    """Backfill per-axis precision limits from the legacy single-step control."""
    resolved = dict(settings)
    raw = raw_settings if isinstance(raw_settings, dict) else resolved

    raw_step = raw.get("precision_max_step")
    if raw_step is None:
        return resolved

    try:
        step_value = float(raw_step)
    except (TypeError, ValueError):
        return resolved

    promote_single_step = False
    raw_pan = raw.get("precision_max_pan_step")
    raw_tilt = raw.get("precision_max_tilt_step")
    if raw_pan is None and raw_tilt is None:
        promote_single_step = True
    else:
        try:
            pan_is_default = abs(float(raw_pan) - float(_DEFAULT_ENGAGEMENT_LIMITS.precision_max_pan_step)) <= 0.005
            tilt_is_default = abs(float(raw_tilt) - float(_DEFAULT_ENGAGEMENT_LIMITS.precision_max_tilt_step)) <= 0.005
            step_differs = abs(step_value - float(_DEFAULT_ENGAGEMENT_LIMITS.precision_max_step)) > 0.005
            promote_single_step = pan_is_default and tilt_is_default and step_differs
        except (TypeError, ValueError):
            promote_single_step = False

    if promote_single_step:
        pan_step = max(0.05, step_value)
        tilt_step = max(0.05, pan_step * _PRECISION_TILT_STEP_RATIO)
        resolved["precision_max_pan_step"] = round(pan_step, 3)
        resolved["precision_max_tilt_step"] = round(tilt_step, 3)

    return resolved

MASTER_PROFILE_PRESETS = {
    "demo_observer": {
        "label": "Demo Observer",
        "description": "Wide-net observer profile for spotting tiny and far moving objects without class lock or auto-fire.",
        "tooltip_key": "preset_master_demo_observer",
        "detection": "observer_motion_watch",
        "filter": "observer_all_movers",
        "threat": "small_target_follow",
        "engagement": "demo_track_multi",
        "servo": "smooth",
    },
    "indoor_precision": {
        "label": "Indoor Precision",
        "description": "Most selective profile for short-range indoor spaces.",
        "tooltip_key": "preset_master_indoor_precision",
        "detection": "yolo",
        "filter": "human_focus",
        "threat": "class_first",
        "engagement": "indoor_precision",
        "servo": "smooth",
    },
    "balanced_sentry": {
        "label": "Balanced Sentry",
        "description": "Middle-ground profile between conservative tracking and active engagement.",
        "tooltip_key": "preset_master_balanced_sentry",
        "detection": "motion_locked",
        "filter": "sniper_medium_motion",
        "threat": "balanced_guard",
        "engagement": "balanced_response",
        "servo": "balanced",
    },
    "vehicle_intercept": {
        "label": "Vehicle Intercept",
        "description": "Tracks larger fast movers with wider aim tolerance and quicker handoff.",
        "tooltip_key": "preset_master_vehicle_intercept",
        "detection": "motion_yolo",
        "filter": "vehicle_watch",
        "threat": "speed_hunter",
        "engagement": "outdoor_chase",
        "servo": "balanced",
    },
    "aggressive_pursuit": {
        "label": "Aggressive Pursuit",
        "description": "Highest-tempo profile with permissive detection, fast slew, and heavy firing.",
        "tooltip_key": "preset_master_aggressive_pursuit",
        "detection": "best_hybrid",
        "filter": "wide_net",
        "threat": "speed_hunter",
        "engagement": "saturation_burst",
        "servo": "fast",
    },
    "dog_tracker": {
        "label": "Dog Tracker",
        "description": "Dog-specific tracking profile with class lock and center-follow engagement.",
        "tooltip_key": "preset_master_dog_tracker",
        "detection": "dog_follow",
        "filter": "dog_focus",
        "threat": "pet_center_lock",
        "engagement": "dog_follow_center",
        "servo": "balanced",
    },
    "cat_tracker": {
        "label": "Cat Tracker",
        "description": "Cat-specific tracking profile for agile small targets with tight center lock.",
        "tooltip_key": "preset_master_cat_tracker",
        "detection": "cat_follow",
        "filter": "cat_focus",
        "threat": "pet_center_lock",
        "engagement": "cat_follow_center",
        "servo": "balanced",
    },
    "rat_like_tracker": {
        "label": "Rat-Like Tracker",
        "description": "Rat-specific YOLO tracking profile with tiny-size constraints, high center bias, and continuous follow when the rat pauses.",
        "tooltip_key": "preset_master_rat_like_tracker",
        "detection": "rat_like_follow",
        "filter": "rat_like_motion",
        "threat": "small_target_follow",
        "engagement": "rat_follow_center",
        "servo": "fast",
    },
    "color_follow_small": {
        "label": "Color Follow Small",
        "description": "Tracks and aims at small colored objects. Uses OR fusion so even a static colored blob triggers tracking. Pick your color preset after applying.",
        "tooltip_key": "preset_master_color_follow_small",
        "detection": "color_motion",
        "filter": "small_movers",
        "threat": "small_target_follow",
        "engagement": "color_follow_track",
        "servo": "balanced",
    },
    "person_track_fire": {
        "label": "Person Track + Fire",
        "description": "Full person-tracking pipeline. YOLO-only detection catches still and moving people alike. Person-class filter rejects non-human detections and has no upper size limit for close-range subjects. Closest-person scoring keeps the nearest adult prioritised. Person-scale engagement tolerances maintain aim lock through natural body sway and brief occlusions.",
        "tooltip_key": "preset_master_person_track_fire",
        "detection": "person_yolo",
        "filter": "person_focus_closest",
        "threat": "person_closest_center",
        "engagement": "person_track_fire",
        "servo": "balanced",
    },
    "sniper_movement_small": {
        "label": "Sniper Movement Small",
        "description": "Motion-locked sniper profile for small rodent-sized targets.",
        "tooltip_key": "preset_master_sniper_movement_small",
        "detection": "mode_10__small",
        "filter": "sniper_small_motion",
        "threat": "sniper_small_center_lock",
        "engagement": "sniper_small_center",
        "servo": "smooth",
    },
    "sniper_movement_medium": {
        "label": "Sniper Movement Medium",
        "description": "Motion-locked sniper profile for medium cat/dog-sized targets.",
        "tooltip_key": "preset_master_sniper_movement_medium",
        "detection": "mode_10__medium",
        "filter": "sniper_medium_motion",
        "threat": "sniper_medium_center_lock",
        "engagement": "sniper_medium_center",
        "servo": "smooth",
    },
    "sniper_movement_large": {
        "label": "Sniper Movement Large",
        "description": "Motion-locked sniper profile for large person-scale targets.",
        "tooltip_key": "preset_master_sniper_movement_large",
        "detection": "mode_10__large",
        "filter": "sniper_large_motion",
        "threat": "sniper_large_center_lock",
        "engagement": "sniper_large_center",
        "servo": "smooth",
    },
    "sniper_color_small": {
        "label": "Sniper Color Small",
        "description": "Color-led sniper profile for small rodent-sized colored targets.",
        "tooltip_key": "preset_master_sniper_color_small",
        "detection": "mode_8__small",
        "filter": "sniper_small_motion",
        "threat": "sniper_small_center_lock",
        "engagement": "sniper_small_center",
        "servo": "smooth",
    },
    "sniper_color_medium": {
        "label": "Sniper Color Medium",
        "description": "Color-led sniper profile for medium cat/dog-sized colored targets.",
        "tooltip_key": "preset_master_sniper_color_medium",
        "detection": "mode_8__medium",
        "filter": "sniper_medium_motion",
        "threat": "sniper_medium_center_lock",
        "engagement": "sniper_medium_center",
        "servo": "smooth",
    },
    "sniper_color_large": {
        "label": "Sniper Color Large",
        "description": "Color-led sniper profile for person-scale colored targets.",
        "tooltip_key": "preset_master_sniper_color_large",
        "detection": "mode_8__large",
        "filter": "sniper_large_motion",
        "threat": "sniper_large_center_lock",
        "engagement": "sniper_large_center",
        "servo": "smooth",
    },
    "sniper_yolo_small": {
        "label": "Sniper YOLO Small",
        "description": "YOLO sniper profile for rat/small-rodent class targets.",
        "tooltip_key": "preset_master_sniper_yolo_small",
        "detection": "mode_2__small",
        "filter": "sniper_small_rodent",
        "threat": "sniper_small_center_lock",
        "engagement": "sniper_small_center",
        "servo": "smooth",
    },
    "sniper_yolo_medium": {
        "label": "Sniper YOLO Medium",
        "description": "YOLO sniper profile for cat/dog targets.",
        "tooltip_key": "preset_master_sniper_yolo_medium",
        "detection": "mode_2__medium",
        "filter": "sniper_medium_pet",
        "threat": "sniper_medium_center_lock",
        "engagement": "sniper_medium_center",
        "servo": "smooth",
    },
    "sniper_yolo_large": {
        "label": "Sniper YOLO Large",
        "description": "YOLO sniper profile for person targets.",
        "tooltip_key": "preset_master_sniper_yolo_large",
        "detection": "mode_2__large",
        "filter": "sniper_large_person",
        "threat": "sniper_large_center_lock",
        "engagement": "sniper_large_center",
        "servo": "smooth",
    },
    "sniper_hybrid_small": {
        "label": "Sniper Hybrid Small",
        "description": "Hybrid sniper profile for small rodent targets with strict center fire gate.",
        "tooltip_key": "preset_master_sniper_hybrid_small",
        "detection": "mode_4__small",
        "filter": "sniper_small_rodent",
        "threat": "sniper_small_center_lock",
        "engagement": "sniper_small_center",
        "servo": "smooth",
    },
    "sniper_hybrid_medium": {
        "label": "Sniper Hybrid Medium",
        "description": "Hybrid sniper profile for medium cat/dog targets with strict center fire gate.",
        "tooltip_key": "preset_master_sniper_hybrid_medium",
        "detection": "mode_4__medium",
        "filter": "sniper_medium_pet",
        "threat": "sniper_medium_center_lock",
        "engagement": "sniper_medium_center",
        "servo": "smooth",
    },
    "sniper_hybrid_large": {
        "label": "Sniper Hybrid Large",
        "description": "Hybrid sniper profile for person targets with strict center fire gate.",
        "tooltip_key": "preset_master_sniper_hybrid_large",
        "detection": "mode_4__large",
        "filter": "sniper_large_person",
        "threat": "sniper_large_center_lock",
        "engagement": "sniper_large_center",
        "servo": "smooth",
    },
}

THREAT_AI_PRESETS = {
    "balanced_guard": {
        "label": "Balanced Guard",
        "description": "Keeps center bias and class weighting in relatively even balance.",
        "tooltip_key": "preset_threat_balanced_guard",
        "weights": {
            "w_proximity": 0.38,
            "w_size": 0.08,
            "w_confidence": 0.08,
            "w_class_priority": 0.16,
            "w_speed": 0.08,
            "w_persistence": 0.12,
            "w_approach": 0.10,
        },
        "use_ml_model": False,
    },
    "crosshair_snap": {
        "label": "Crosshair Snap",
        "description": "Strongly center-biased so on-axis targets dominate the queue.",
        "tooltip_key": "preset_threat_crosshair_snap",
        "weights": {
            "w_proximity": 0.68,
            "w_size": 0.03,
            "w_confidence": 0.04,
            "w_class_priority": 0.08,
            "w_speed": 0.02,
            "w_persistence": 0.03,
            "w_approach": 0.12,
        },
        "use_ml_model": False,
    },
    "speed_hunter": {
        "label": "Speed Hunter",
        "description": "Overweights velocity so fast movers can outrank centered slow targets.",
        "tooltip_key": "preset_threat_speed_hunter",
        "weights": {
            "w_proximity": 0.28,
            "w_size": 0.04,
            "w_confidence": 0.06,
            "w_class_priority": 0.08,
            "w_speed": 0.24,
            "w_persistence": 0.20,
            "w_approach": 0.10,
        },
        "use_ml_model": False,
    },
    "big_target_bias": {
        "label": "Big Target Bias",
        "description": "Prioritizes targets that occupy a large chunk of the frame.",
        "tooltip_key": "preset_threat_big_target_bias",
        "weights": {
            "w_proximity": 0.30,
            "w_size": 0.30,
            "w_confidence": 0.12,
            "w_class_priority": 0.12,
            "w_speed": 0.04,
            "w_persistence": 0.06,
            "w_approach": 0.06,
        },
        "use_ml_model": False,
    },
    "class_first": {
        "label": "Class First",
        "description": "Configured class priorities dominate, even against more central motion.",
        "tooltip_key": "preset_threat_class_first",
        "weights": {
            "w_proximity": 0.28,
            "w_size": 0.06,
            "w_confidence": 0.14,
            "w_class_priority": 0.34,
            "w_speed": 0.04,
            "w_persistence": 0.08,
            "w_approach": 0.06,
        },
        "use_ml_model": False,
    },
    "pet_center_lock": {
        "label": "Pet Center Lock",
        "description": "Strong center lock with moderate class weighting for pet tracking.",
        "tooltip_key": "preset_threat_pet_center_lock",
        "weights": {
            "w_proximity": 0.56,
            "w_size": 0.08,
            "w_confidence": 0.10,
            "w_class_priority": 0.16,
            "w_speed": 0.03,
            "w_persistence": 0.04,
            "w_approach": 0.03,
        },
        "use_ml_model": False,
    },
    "small_target_follow": {
        "label": "Small Target Follow",
        "description": "Center bias plus speed/persistence to hold tiny moving targets.",
        "tooltip_key": "preset_threat_small_target_follow",
        "weights": {
            "w_proximity": 0.50,
            "w_size": 0.04,
            "w_confidence": 0.06,
            "w_class_priority": 0.06,
            "w_speed": 0.16,
            "w_persistence": 0.10,
            "w_approach": 0.08,
        },
        "use_ml_model": False,
    },
    "person_closest_center": {
        "label": "Person — Closest + Center",
        "description": "Prioritises the closest (largest) person in frame with strong size dominance and solid center bias. Speed and persistence are weighted so a walking person stays tracked through directional changes. Class priority weight is intentionally lean because the filter already enforces person-only.",
        "tooltip_key": "preset_threat_person_closest_center",
        "weights": {
            "w_proximity": 0.30,
            "w_size": 0.34,
            "w_confidence": 0.12,
            "w_class_priority": 0.08,
            "w_speed": 0.06,
            "w_persistence": 0.08,
            "w_approach": 0.02,
        },
        "use_ml_model": False,
    },
    "sniper_small_center_lock": {
        "label": "Sniper Small Center Lock",
        "description": "Sniper scoring for tiny targets: hard center bias with enough class confidence to avoid noise.",
        "tooltip_key": "preset_threat_sniper_small_center_lock",
        "weights": {
            "w_proximity": 0.60,
            "w_size": 0.06,
            "w_confidence": 0.08,
            "w_class_priority": 0.14,
            "w_speed": 0.04,
            "w_persistence": 0.05,
            "w_approach": 0.03,
        },
        "use_ml_model": False,
    },
    "sniper_medium_center_lock": {
        "label": "Sniper Medium Center Lock",
        "description": "Sniper scoring for cat/dog scale targets with very strong center priority.",
        "tooltip_key": "preset_threat_sniper_medium_center_lock",
        "weights": {
            "w_proximity": 0.62,
            "w_size": 0.09,
            "w_confidence": 0.10,
            "w_class_priority": 0.12,
            "w_speed": 0.02,
            "w_persistence": 0.03,
            "w_approach": 0.02,
        },
        "use_ml_model": False,
    },
    "sniper_large_center_lock": {
        "label": "Sniper Large Center Lock",
        "description": "Sniper scoring for person-scale targets with center bias and moderate size preference.",
        "tooltip_key": "preset_threat_sniper_large_center_lock",
        "weights": {
            "w_proximity": 0.58,
            "w_size": 0.17,
            "w_confidence": 0.10,
            "w_class_priority": 0.10,
            "w_speed": 0.01,
            "w_persistence": 0.02,
            "w_approach": 0.02,
        },
        "use_ml_model": False,
    },
}

ENGAGEMENT_PRESETS = {
    "demo_track": {
        "label": "Demo Track Only",
        "description": "Tracking-only preset with the slowest corrections and no auto-fire.",
        "tooltip_key": "preset_engage_demo_track",
        "settings": {
            "auto_trigger_enabled": False,
            "trigger_mode_bb": False,
            "min_threat_score": 0.70,
            "burst_count": 1,
            "burst_interval_ms": 120,
            "inter_target_cooldown": 2.0,
            "cycle_cooldown": 3.5,
            "max_queue_length": 1,
            "optimize_slew_order": False,
            "engagement_speed": 24,
            "precision_aim_enabled": True,
            "precision_settle_time": 1.35,
            "precision_max_step": 0.28,
            "precision_deadzone_pan_deg": 0.10,
            "precision_deadzone_tilt_deg": 0.08,
            "precision_error_ema": 0.55,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 2.50,
            "aim_lock_tilt_tolerance": 2.00,
            "aim_lock_required_frames": 3,
            "fire_trigger_enter_pan_tolerance": 2.00,
            "fire_trigger_enter_tilt_tolerance": 1.60,
            "fire_trigger_exit_pan_tolerance": 2.80,
            "fire_trigger_exit_tilt_tolerance": 2.20,
            "fire_recenter_pan_tolerance": 2.50,
            "fire_recenter_tilt_tolerance": 2.00,
            "target_loss_timeout": 1.90,
        },
    },
    "demo_track_multi": {
        "label": "Demo Track Observer x5",
        "description": "Tracking-only observer preset that keeps up to five moving candidates visible while staying slow and non-firing.",
        "tooltip_key": "preset_engage_demo_track_multi",
        "settings": {
            "auto_trigger_enabled": False,
            "trigger_mode_bb": False,
            "min_threat_score": 0.08,
            "burst_count": 1,
            "burst_interval_ms": 120,
            "inter_target_cooldown": 0.40,
            "cycle_cooldown": 0.60,
            "max_queue_length": 5,
            "optimize_slew_order": False,
            "engagement_speed": 24,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.80,
            "precision_max_step": 0.28,
            "precision_deadzone_pan_deg": 0.10,
            "precision_deadzone_tilt_deg": 0.08,
            "precision_error_ema": 0.55,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 2.50,
            "aim_lock_tilt_tolerance": 2.00,
            "aim_lock_required_frames": 3,
            "fire_trigger_enter_pan_tolerance": 2.00,
            "fire_trigger_enter_tilt_tolerance": 1.60,
            "fire_trigger_exit_pan_tolerance": 2.80,
            "fire_trigger_exit_tilt_tolerance": 2.20,
            "fire_recenter_pan_tolerance": 2.50,
            "fire_recenter_tilt_tolerance": 2.00,
            "target_loss_timeout": 1.20,
        },
    },
    "indoor_precision": {
        "label": "Indoor Precision",
        "description": "Highly selective auto-fire tuned for close-range indoor testing.",
        "tooltip_key": "preset_engage_indoor_precision",
        "settings": {
            "auto_trigger_enabled": True,
            "trigger_mode_bb": True,
            "min_threat_score": 0.28,
            "burst_count": 1,
            "burst_interval_ms": 100,
            "inter_target_cooldown": 1.80,
            "cycle_cooldown": 3.10,
            "max_queue_length": 1,
            "optimize_slew_order": False,
            "engagement_speed": 32,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.90,
            "precision_max_step": 0.32,
            "precision_deadzone_pan_deg": 0.08,
            "precision_deadzone_tilt_deg": 0.06,
            "precision_error_ema": 0.52,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 2.00,
            "aim_lock_tilt_tolerance": 1.60,
            "aim_lock_required_frames": 3,
            "fire_trigger_enter_pan_tolerance": 1.80,
            "fire_trigger_enter_tilt_tolerance": 1.40,
            "fire_trigger_exit_pan_tolerance": 2.50,
            "fire_trigger_exit_tilt_tolerance": 2.00,
            "fire_recenter_pan_tolerance": 2.20,
            "fire_recenter_tilt_tolerance": 1.80,
            "target_loss_timeout": 2.00,
        },
    },
    "balanced_response": {
        "label": "Balanced Response",
        "description": "Middle-ground preset with controlled auto-fire and moderate recovery.",
        "tooltip_key": "preset_engage_balanced_response",
        "settings": {
            "auto_trigger_enabled": True,
            "trigger_mode_bb": True,
            "min_threat_score": 0.26,
            "burst_count": 2,
            "burst_interval_ms": 70,
            "inter_target_cooldown": 1.00,
            "cycle_cooldown": 2.00,
            "max_queue_length": 1,
            "optimize_slew_order": False,
            "engagement_speed": 62,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.50,
            "precision_max_step": 0.72,
            "precision_deadzone_pan_deg": 0.10,
            "precision_deadzone_tilt_deg": 0.08,
            "precision_error_ema": 0.40,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 2.50,
            "aim_lock_tilt_tolerance": 2.00,
            "aim_lock_required_frames": 2,
            "fire_trigger_enter_pan_tolerance": 2.20,
            "fire_trigger_enter_tilt_tolerance": 1.80,
            "fire_trigger_exit_pan_tolerance": 3.00,
            "fire_trigger_exit_tilt_tolerance": 2.40,
            "fire_recenter_pan_tolerance": 2.80,
            "fire_recenter_tilt_tolerance": 2.20,
            "target_loss_timeout": 1.10,
        },
    },
    "outdoor_chase": {
        "label": "Outdoor Chase",
        "description": "Fast-moving outdoor preset with quick handoff and wider fire tolerances.",
        "tooltip_key": "preset_engage_outdoor_chase",
        "settings": {
            "auto_trigger_enabled": True,
            "trigger_mode_bb": True,
            "min_threat_score": 0.28,
            "burst_count": 2,
            "burst_interval_ms": 55,
            "inter_target_cooldown": 0.55,
            "cycle_cooldown": 1.30,
            "max_queue_length": 1,
            "optimize_slew_order": False,
            "engagement_speed": 90,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.20,
            "precision_max_step": 1.30,
            "precision_deadzone_pan_deg": 0.13,
            "precision_deadzone_tilt_deg": 0.10,
            "precision_error_ema": 0.30,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 3.00,
            "aim_lock_tilt_tolerance": 2.50,
            "aim_lock_required_frames": 2,
            "fire_trigger_enter_pan_tolerance": 2.80,
            "fire_trigger_enter_tilt_tolerance": 2.20,
            "fire_trigger_exit_pan_tolerance": 3.50,
            "fire_trigger_exit_tilt_tolerance": 2.80,
            "fire_recenter_pan_tolerance": 3.20,
            "fire_recenter_tilt_tolerance": 2.60,
            "target_loss_timeout": 0.80,
        },
    },
    "saturation_burst": {
        "label": "Saturation Burst",
        "description": "Most aggressive preset with permissive lock rules and sustained bursts.",
        "tooltip_key": "preset_engage_saturation_burst",
        "settings": {
            "auto_trigger_enabled": True,
            "trigger_mode_bb": True,
            "min_threat_score": 0.24,
            "burst_count": 3,
            "burst_interval_ms": 42,
            "inter_target_cooldown": 0.35,
            "cycle_cooldown": 1.00,
            "max_queue_length": 1,
            "optimize_slew_order": False,
            "engagement_speed": 96,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.14,
            "precision_max_step": 1.55,
            "precision_deadzone_pan_deg": 0.16,
            "precision_deadzone_tilt_deg": 0.13,
            "precision_error_ema": 0.28,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 3.50,
            "aim_lock_tilt_tolerance": 2.80,
            "aim_lock_required_frames": 2,
            "fire_trigger_enter_pan_tolerance": 3.00,
            "fire_trigger_enter_tilt_tolerance": 2.40,
            "fire_trigger_exit_pan_tolerance": 4.00,
            "fire_trigger_exit_tilt_tolerance": 3.20,
            "fire_recenter_pan_tolerance": 3.50,
            "fire_recenter_tilt_tolerance": 2.80,
            "target_loss_timeout": 0.70,
        },
    },
    "dog_follow_center": {
        "label": "Dog Follow Center",
        "description": "Tracking-first dog profile with tight centering and continuous follow behavior.",
        "tooltip_key": "preset_engage_dog_follow_center",
        "settings": {
            "auto_trigger_enabled": False,
            "trigger_mode_bb": True,
            "min_threat_score": 0.28,
            "burst_count": 1,
            "burst_interval_ms": 90,
            "inter_target_cooldown": 0.35,
            "cycle_cooldown": 0.90,
            "max_queue_length": 1,
            "optimize_slew_order": False,
            "engagement_speed": 86,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.22,
            "precision_max_step": 1.18,
            "precision_deadzone_pan_deg": 0.08,
            "precision_deadzone_tilt_deg": 0.07,
            "precision_error_ema": 0.42,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 2.20,
            "aim_lock_tilt_tolerance": 1.80,
            "aim_lock_required_frames": 3,
            "fire_trigger_enter_pan_tolerance": 2.00,
            "fire_trigger_enter_tilt_tolerance": 1.60,
            "fire_trigger_exit_pan_tolerance": 2.80,
            "fire_trigger_exit_tilt_tolerance": 2.20,
            "fire_recenter_pan_tolerance": 2.50,
            "fire_recenter_tilt_tolerance": 2.00,
            "target_loss_timeout": 0.70,
        },
    },
    "cat_follow_center": {
        "label": "Cat Follow Center",
        "description": "Small agile target follow with tighter deadzones and fast reacquire.",
        "tooltip_key": "preset_engage_cat_follow_center",
        "settings": {
            "auto_trigger_enabled": False,
            "trigger_mode_bb": True,
            "min_threat_score": 0.24,
            "burst_count": 1,
            "burst_interval_ms": 90,
            "inter_target_cooldown": 0.28,
            "cycle_cooldown": 0.75,
            "max_queue_length": 1,
            "optimize_slew_order": False,
            "engagement_speed": 92,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.16,
            "precision_max_step": 1.42,
            "precision_deadzone_pan_deg": 0.07,
            "precision_deadzone_tilt_deg": 0.06,
            "precision_error_ema": 0.44,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 2.00,
            "aim_lock_tilt_tolerance": 1.60,
            "aim_lock_required_frames": 2,
            "fire_trigger_enter_pan_tolerance": 1.80,
            "fire_trigger_enter_tilt_tolerance": 1.50,
            "fire_trigger_exit_pan_tolerance": 2.50,
            "fire_trigger_exit_tilt_tolerance": 2.00,
            "fire_recenter_pan_tolerance": 2.20,
            "fire_recenter_tilt_tolerance": 1.80,
            "target_loss_timeout": 0.55,
        },
    },
    "rat_follow_center": {
        "label": "Rat-Like Follow Center",
        "description": "Very small fast-mover follow profile with high-speed corrections and center lock.",
        "tooltip_key": "preset_engage_rat_follow_center",
        "settings": {
            "auto_trigger_enabled": False,
            "trigger_mode_bb": True,
            "min_threat_score": 0.18,
            "burst_count": 1,
            "burst_interval_ms": 80,
            "inter_target_cooldown": 0.18,
            "cycle_cooldown": 0.55,
            "max_queue_length": 1,
            "optimize_slew_order": False,
            "engagement_speed": 100,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.10,
            "precision_max_step": 1.80,
            "precision_deadzone_pan_deg": 0.06,
            "precision_deadzone_tilt_deg": 0.05,
            "precision_error_ema": 0.46,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 1.80,
            "aim_lock_tilt_tolerance": 1.40,
            "aim_lock_required_frames": 2,
            "fire_trigger_enter_pan_tolerance": 1.60,
            "fire_trigger_enter_tilt_tolerance": 1.30,
            "fire_trigger_exit_pan_tolerance": 2.20,
            "fire_trigger_exit_tilt_tolerance": 1.80,
            "fire_recenter_pan_tolerance": 2.00,
            "fire_recenter_tilt_tolerance": 1.60,
            "target_loss_timeout": 0.35,
        },
    },
    "color_follow_track": {
        "label": "Color Follow Track",
        "description": "Permissive tracking preset tuned for color-detected small objects. Low threat threshold and responsive corrections keep the turret locked even on tiny colored blobs.",
        "tooltip_key": "preset_engage_color_follow_track",
        "settings": {
            "auto_trigger_enabled": False,
            "trigger_mode_bb": True,
            "min_threat_score": 0.16,
            "burst_count": 1,
            "burst_interval_ms": 90,
            "inter_target_cooldown": 0.22,
            "cycle_cooldown": 0.60,
            "max_queue_length": 1,
            "optimize_slew_order": False,
            "engagement_speed": 94,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.14,
            "precision_max_step": 1.48,
            "precision_deadzone_pan_deg": 0.07,
            "precision_deadzone_tilt_deg": 0.06,
            "precision_error_ema": 0.42,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 2.00,
            "aim_lock_tilt_tolerance": 1.60,
            "aim_lock_required_frames": 2,
            "fire_trigger_enter_pan_tolerance": 1.80,
            "fire_trigger_enter_tilt_tolerance": 1.40,
            "fire_trigger_exit_pan_tolerance": 2.50,
            "fire_trigger_exit_tilt_tolerance": 2.00,
            "fire_recenter_pan_tolerance": 2.20,
            "fire_recenter_tilt_tolerance": 1.80,
            "target_loss_timeout": 0.50,
        },
    },
    "person_track_fire": {
        "label": "Person Track + Fire",
        "description": "Person-scale engagement profile. Servo speed and correction step are tuned for a walking adult. Lock tolerances are wider than pet presets so the turret holds aim through natural body sway. Extended loss timeout (3 s) keeps tracking through brief occlusions such as a door frame or another person walking in front.",
        "tooltip_key": "preset_engage_person_track_fire",
        "settings": {
            "auto_trigger_enabled": True,
            "trigger_mode_bb": True,
            "min_threat_score": 0.26,
            "burst_count": 2,
            "burst_interval_ms": 80,
            "inter_target_cooldown": 1.50,
            "cycle_cooldown": 2.50,
            "max_queue_length": 1,
            "optimize_slew_order": False,
            "engagement_speed": 78,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.26,
            "precision_max_step": 1.05,
            "precision_deadzone_pan_deg": 0.10,
            "precision_deadzone_tilt_deg": 0.08,
            "precision_error_ema": 0.42,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 2.50,
            "aim_lock_tilt_tolerance": 2.00,
            "aim_lock_required_frames": 2,
            "fire_trigger_enter_pan_tolerance": 2.50,
            "fire_trigger_enter_tilt_tolerance": 2.00,
            "fire_trigger_exit_pan_tolerance": 3.20,
            "fire_trigger_exit_tilt_tolerance": 2.50,
            "fire_recenter_pan_tolerance": 3.00,
            "fire_recenter_tilt_tolerance": 2.40,
            "target_loss_timeout": 3.00,
            "aim_lock_timeout": 2.50,
        },
    },
    "sniper_small_center": {
        "label": "Sniper Small Center",
        "description": "Ultra-precise sniper engagement for rats/small rodents. Fires only when dead-center lock is sustained.",
        "tooltip_key": "preset_engage_sniper_small_center",
        "settings": {
            "auto_trigger_enabled": True,
            "trigger_mode_bb": True,
            "min_threat_score": 0.56,
            "burst_count": 1,
            "burst_interval_ms": 150,
            "inter_target_cooldown": 2.20,
            "cycle_cooldown": 3.40,
            "max_queue_length": 1,
            "optimize_slew_order": False,
            "engagement_speed": 34,
            "precision_aim_enabled": True,
            "precision_settle_time": 1.05,
            "precision_max_step": 0.24,
            "precision_deadzone_pan_deg": 0.040,
            "precision_deadzone_tilt_deg": 0.035,
            "precision_error_ema": 0.36,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 1.00,
            "aim_lock_tilt_tolerance": 0.80,
            "aim_lock_required_frames": 8,
            "fire_trigger_enter_pan_tolerance": 0.80,
            "fire_trigger_enter_tilt_tolerance": 0.60,
            "fire_trigger_exit_pan_tolerance": 1.20,
            "fire_trigger_exit_tilt_tolerance": 1.00,
            "fire_recenter_pan_tolerance": 1.10,
            "fire_recenter_tilt_tolerance": 0.90,
            "target_loss_timeout": 2.80,
            "aim_lock_timeout": 3.50,
            "continuous_hunt_on_loss": True,
        },
    },
    "sniper_medium_center": {
        "label": "Sniper Medium Center",
        "description": "Precision sniper engagement for cat/dog targets. Strict center lock before trigger.",
        "tooltip_key": "preset_engage_sniper_medium_center",
        "settings": {
            "auto_trigger_enabled": True,
            "trigger_mode_bb": True,
            "min_threat_score": 0.52,
            "burst_count": 1,
            "burst_interval_ms": 140,
            "inter_target_cooldown": 2.00,
            "cycle_cooldown": 3.10,
            "max_queue_length": 1,
            "optimize_slew_order": False,
            "engagement_speed": 36,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.95,
            "precision_max_step": 0.26,
            "precision_deadzone_pan_deg": 0.045,
            "precision_deadzone_tilt_deg": 0.040,
            "precision_error_ema": 0.38,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 1.20,
            "aim_lock_tilt_tolerance": 1.00,
            "aim_lock_required_frames": 7,
            "fire_trigger_enter_pan_tolerance": 1.00,
            "fire_trigger_enter_tilt_tolerance": 0.80,
            "fire_trigger_exit_pan_tolerance": 1.50,
            "fire_trigger_exit_tilt_tolerance": 1.20,
            "fire_recenter_pan_tolerance": 1.40,
            "fire_recenter_tilt_tolerance": 1.10,
            "target_loss_timeout": 2.60,
            "aim_lock_timeout": 3.20,
            "continuous_hunt_on_loss": True,
        },
    },
    "sniper_large_center": {
        "label": "Sniper Large Center",
        "description": "Precision sniper engagement for person-scale targets. Requires sustained center confirmation before fire.",
        "tooltip_key": "preset_engage_sniper_large_center",
        "settings": {
            "auto_trigger_enabled": True,
            "trigger_mode_bb": True,
            "min_threat_score": 0.50,
            "burst_count": 1,
            "burst_interval_ms": 130,
            "inter_target_cooldown": 1.90,
            "cycle_cooldown": 2.90,
            "max_queue_length": 1,
            "optimize_slew_order": False,
            "engagement_speed": 40,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.88,
            "precision_max_step": 0.30,
            "precision_deadzone_pan_deg": 0.050,
            "precision_deadzone_tilt_deg": 0.045,
            "precision_error_ema": 0.40,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 1.40,
            "aim_lock_tilt_tolerance": 1.10,
            "aim_lock_required_frames": 6,
            "fire_trigger_enter_pan_tolerance": 1.50,
            "fire_trigger_enter_tilt_tolerance": 1.20,
            "fire_trigger_exit_pan_tolerance": 2.00,
            "fire_trigger_exit_tilt_tolerance": 1.60,
            "fire_recenter_pan_tolerance": 1.80,
            "fire_recenter_tilt_tolerance": 1.40,
            "target_loss_timeout": 2.50,
            "aim_lock_timeout": 3.00,
            "continuous_hunt_on_loss": True,
        },
    },
}

_ENGAGEMENT_PRESET_ADVANCED_OVERRIDES = {
    "demo_track": {
        "precision_kp": 0.024,
        "precision_kd": 0.014,
        "precision_reversal_brake": 0.18,
    },
    "demo_track_multi": {
        "precision_kp": 0.026,
        "precision_kd": 0.014,
        "precision_reversal_brake": 0.20,
        "predictive_min_persistence_s": 0.10,
    },
    "indoor_precision": {
        "precision_kp": 0.031,
        "precision_kd": 0.014,
        "precision_reversal_brake": 0.20,
        "predictive_lead_time_s": 0.08,
        "predictive_fire_extra_lead_s": 0.02,
        "predictive_min_persistence_s": 0.12,
    },
    "balanced_response": {
        "precision_kp": 0.038,
        "precision_kd": 0.013,
        "precision_reversal_brake": 0.24,
        "predictive_lead_time_s": 0.14,
        "predictive_fire_extra_lead_s": 0.03,
        "predictive_min_persistence_s": 0.10,
        "loss_direction_pursuit_s": 0.22,
    },
    "outdoor_chase": {
        "precision_kp": 0.042,
        "precision_kd": 0.015,
        "precision_reversal_brake": 0.26,
        "predictive_lead_time_s": 0.19,
        "predictive_fire_extra_lead_s": 0.05,
        "predictive_min_persistence_s": 0.08,
        "predictive_max_lead_pan_deg": 4.2,
        "predictive_max_lead_tilt_deg": 2.6,
        "loss_direction_pursuit_s": 0.34,
        "target_loss_timeout": 0.95,
    },
    "saturation_burst": {
        "precision_kp": 0.047,
        "precision_kd": 0.017,
        "precision_reversal_brake": 0.24,
        "predictive_lead_time_s": 0.22,
        "predictive_fire_extra_lead_s": 0.06,
        "predictive_min_persistence_s": 0.06,
        "predictive_max_lead_pan_deg": 4.6,
        "predictive_max_lead_tilt_deg": 2.8,
        "loss_direction_pursuit_s": 0.30,
        "target_loss_timeout": 0.90,
    },
    "dog_follow_center": {
        "precision_kp": 0.040,
        "precision_kd": 0.014,
        "precision_reversal_brake": 0.24,
        "predictive_lead_time_s": 0.15,
        "predictive_fire_extra_lead_s": 0.03,
        "predictive_min_persistence_s": 0.08,
        "target_loss_timeout": 0.85,
        "continuous_hunt_on_loss": True,
    },
    "cat_follow_center": {
        "precision_kp": 0.043,
        "precision_kd": 0.016,
        "precision_reversal_brake": 0.22,
        "predictive_lead_time_s": 0.18,
        "predictive_fire_extra_lead_s": 0.04,
        "predictive_min_persistence_s": 0.08,
        "target_loss_timeout": 0.70,
        "continuous_hunt_on_loss": True,
    },
    "rat_follow_center": {
        "precision_kp": 0.048,
        "precision_kd": 0.018,
        "precision_reversal_brake": 0.20,
        "predictive_lead_time_s": 0.20,
        "predictive_fire_extra_lead_s": 0.04,
        "predictive_min_persistence_s": 0.06,
        "predictive_max_lead_pan_deg": 4.4,
        "predictive_max_lead_tilt_deg": 2.4,
        "target_loss_timeout": 0.50,
        "continuous_hunt_on_loss": True,
        "loss_direction_pursuit_s": 0.24,
        "loss_local_search_pan_deg": 45.0,
        "loss_local_search_tilt_deg": 45.0,
        "loss_search_step_interval_s": 0.16,
    },
    "color_follow_track": {
        "precision_kp": 0.043,
        "precision_kd": 0.015,
        "precision_reversal_brake": 0.24,
        "target_loss_timeout": 0.65,
        "continuous_hunt_on_loss": True,
    },
    "person_track_fire": {
        "precision_kp": 0.036,
        "precision_kd": 0.013,
        "precision_reversal_brake": 0.25,
        "predictive_lead_time_s": 0.14,
        "predictive_fire_extra_lead_s": 0.03,
        "predictive_min_persistence_s": 0.10,
        "target_loss_timeout": 3.20,
    },
    "sniper_small_center": {
        "precision_kp": 0.028,
        "precision_kd": 0.015,
        "precision_reversal_brake": 0.18,
        "predictive_lead_time_s": 0.09,
        "predictive_fire_extra_lead_s": 0.02,
        "predictive_min_persistence_s": 0.14,
        "predictive_max_lead_pan_deg": 2.6,
        "predictive_max_lead_tilt_deg": 1.6,
    },
    "sniper_medium_center": {
        "precision_kp": 0.030,
        "precision_kd": 0.015,
        "precision_reversal_brake": 0.20,
        "predictive_lead_time_s": 0.11,
        "predictive_fire_extra_lead_s": 0.03,
        "predictive_min_persistence_s": 0.14,
        "predictive_max_lead_pan_deg": 2.8,
        "predictive_max_lead_tilt_deg": 1.8,
    },
    "sniper_large_center": {
        "precision_kp": 0.032,
        "precision_kd": 0.014,
        "precision_reversal_brake": 0.22,
        "predictive_lead_time_s": 0.12,
        "predictive_fire_extra_lead_s": 0.03,
        "predictive_min_persistence_s": 0.12,
        "predictive_max_lead_pan_deg": 3.0,
        "predictive_max_lead_tilt_deg": 2.0,
    },
}

for _preset_name, _override_settings in _ENGAGEMENT_PRESET_ADVANCED_OVERRIDES.items():
    if _preset_name not in ENGAGEMENT_PRESETS:
        continue
    _merged_settings = dict(ENGAGEMENT_PRESETS[_preset_name].get("settings", {}))
    _merged_settings.update(_override_settings)
    ENGAGEMENT_PRESETS[_preset_name]["settings"] = _normalize_engagement_precision_limits(_merged_settings, _merged_settings)

AIM_LOCK_FIRE_GATE_PRESETS = {
    "stable_lock": {
        "label": "Stable Lock",
        "tooltip_key": "preset_aim_gate_stable_lock",
        "settings": {
            "precision_deadzone_pan_deg": 0.07,
            "precision_deadzone_tilt_deg": 0.06,
            "precision_error_ema": 0.40,
            "aim_lock_pan_tolerance": 2.00,
            "aim_lock_tilt_tolerance": 1.60,
            "aim_lock_required_frames": 4,
            "fire_trigger_enter_pan_tolerance": 1.80,
            "fire_trigger_enter_tilt_tolerance": 1.40,
            "fire_trigger_exit_pan_tolerance": 2.50,
            "fire_trigger_exit_tilt_tolerance": 2.00,
            "fire_recenter_pan_tolerance": 2.20,
            "fire_recenter_tilt_tolerance": 1.80,
            "target_loss_timeout": 1.20,
        },
    },
    "balanced_lock": {
        "label": "Balanced Lock",
        "tooltip_key": "preset_aim_gate_balanced_lock",
        "settings": {
            "precision_deadzone_pan_deg": 0.10,
            "precision_deadzone_tilt_deg": 0.08,
            "precision_error_ema": 0.48,
            "aim_lock_pan_tolerance": 2.50,
            "aim_lock_tilt_tolerance": 2.00,
            "aim_lock_required_frames": 3,
            "fire_trigger_enter_pan_tolerance": 2.20,
            "fire_trigger_enter_tilt_tolerance": 1.80,
            "fire_trigger_exit_pan_tolerance": 3.00,
            "fire_trigger_exit_tilt_tolerance": 2.40,
            "fire_recenter_pan_tolerance": 2.80,
            "fire_recenter_tilt_tolerance": 2.20,
            "target_loss_timeout": 0.95,
        },
    },
    "fast_lock": {
        "label": "Fast Lock",
        "tooltip_key": "preset_aim_gate_fast_lock",
        "settings": {
            "precision_deadzone_pan_deg": 0.16,
            "precision_deadzone_tilt_deg": 0.13,
            "precision_error_ema": 0.62,
            "aim_lock_pan_tolerance": 3.50,
            "aim_lock_tilt_tolerance": 2.80,
            "aim_lock_required_frames": 2,
            "fire_trigger_enter_pan_tolerance": 3.00,
            "fire_trigger_enter_tilt_tolerance": 2.40,
            "fire_trigger_exit_pan_tolerance": 4.00,
            "fire_trigger_exit_tilt_tolerance": 3.20,
            "fire_recenter_pan_tolerance": 3.50,
            "fire_recenter_tilt_tolerance": 2.80,
            "target_loss_timeout": 0.65,
        },
    },
}

SENTRY_V2_THEME = """
QWidget#sentryV2Root {
    background-color: #171310;
    color: #f1e8df;
    font-family: "Segoe UI";
    font-size: 10pt;
}
QWidget#sentryV2Root QLabel {
    color: #dacbbe;
}
QWidget#sentryV2Root QScrollArea,
QWidget#sentryV2Root QScrollArea > QWidget > QWidget {
    background-color: #19130f;
    border: none;
}
QWidget#sentryV2Root QGroupBox {
    background-color: #241b16;
    border: 1px solid #4d362a;
    border-radius: 16px;
    margin-top: 14px;
    padding: 14px 12px 12px 12px;
    font-weight: 600;
}
QWidget#sentryV2Root QGroupBox::title {
    subcontrol-origin: margin;
    left: 12px;
    padding: 0 8px;
    color: #f2a65a;
}
QWidget#sentryV2Root QWidget#sentryV2PinnedBottom,
QWidget#sentryV2Root QWidget#sentryV2PinnedTop {
    background-color: transparent;
    border: none;
}
QWidget#sentryV2Root QWidget#sentryV2LeftPane,
QWidget#sentryV2Root QWidget#sentryV2RightPane {
    background-color: transparent;
    border: none;
}
QWidget#sentryV2Root QSplitter {
    background-color: transparent;
}
QWidget#sentryV2Root QSplitter::handle {
    background-color: transparent;
    border: none;
}
QWidget#sentryV2Root QSplitter::handle:horizontal {
    background-color: transparent;
    border: none;
    border-radius: 0;
    margin: 0;
}
QWidget#sentryV2Root QSplitter::handle:vertical {
    background-color: transparent;
    border: none;
    border-radius: 0;
    margin: 0;
}
QWidget#sentryV2Root QFrame#sentryV3Hero {
    background:qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #342117,
        stop:0.58 #4b2c1d,
        stop:1 #6d4125);
    border: 1px solid #8d5d37;
    border-radius: 18px;
}
QWidget#sentryV2Root QLabel#sentryV3HeroTitle {
    color: #fff4ea;
    font-size: 18pt;
    font-weight: 700;
}
QWidget#sentryV2Root QLabel#sentryV3HeroSubtitle {
    color: #e6cdb7;
    font-size: 10.5pt;
}
QWidget#sentryV2Root QLabel#sentryV3HeroBadge {
    background-color: rgba(28, 19, 13, 0.55);
    color: #ffd9aa;
    border: 1px solid #b17a49;
    border-radius: 14px;
    padding: 8px 14px;
    font-size: 10pt;
    font-weight: 700;
}
QWidget#sentryV2Root QWidget#sentryV2ToggleRow {
    background-color: #1d1612;
    border: 1px solid #433026;
    border-radius: 14px;
}
QWidget#sentryV2Root QWidget#sentryV2PinnedBottom QGroupBox {
    margin-top: 8px;
    padding: 12px 10px 10px 10px;
}
QWidget#sentryV2Root QWidget#sentryV2PinnedBottom QLabel {
    color: #d6c8bc;
}
QWidget#sentryV2Root QTabWidget::pane {
    background-color: #1a1410;
    border: 1px solid #50382b;
    border-radius: 14px;
    top: -1px;
}
QWidget#sentryV2Root QTabBar::tab {
    background-color: #281f1a;
    border: 1px solid #52382b;
    border-radius: 10px;
    padding: 6px 4px;
    min-height: 34px;
}
QWidget#sentryV2Root QTabBar::tab:left {
    min-width: 46px;
    max-width: 54px;
    margin-bottom: 4px;
}
QWidget#sentryV2Root QTabBar::tab:top {
    border-bottom: none;
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
    margin-right: 6px;
}
QWidget#sentryV2Root QTabBar::tab:selected {
    background-color: #5d3926;
    border-color: #f2a65a;
    color: #fff6ee;
}
QWidget#sentryV2Root QTabBar::tab:selected:left {
    border-left: 4px solid #f2a65a;
}
QWidget#sentryV2Root QTabBar::tab:hover:!selected {
    background-color: #38261d;
    color: #f8eee5;
}
QWidget#sentryV2Root QPushButton {
    background-color: #4a2e22;
    color: #f9f0e7;
    border: 1px solid #8b5d43;
    border-radius: 10px;
    padding: 5px 10px;
    min-height: 28px;
}
QWidget#sentryV2Root QPushButton:hover {
    background-color: #5b3929;
    border-color: #d8a15c;
}
QWidget#sentryV2Root QPushButton:pressed {
    background-color: #3d251c;
}
QWidget#sentryV2Root QPushButton:checked {
    background-color: #76511f;
    border-color: #f2a65a;
    color: #fff8f0;
}
QWidget#sentryV2Root QPushButton:disabled {
    background-color: #2b211c;
    color: #817366;
    border-color: #483b34;
}
QWidget#sentryV2Root QPushButton[buttonRole="primary"] {
    background-color: #8c4327;
    border-color: #d47d4d;
    color: #fff7ef;
    font-weight: 700;
}
QWidget#sentryV2Root QPushButton[buttonRole="primary"]:hover {
    background-color: #a24f2d;
    border-color: #e39c6d;
}
QWidget#sentryV2Root QPushButton[buttonRole="primary"]:pressed {
    background-color: #73351d;
}
QWidget#sentryV2Root QPushButton[buttonRole="preset"] {
    background-color: #382921;
    border-color: #735441;
    color: #f5ece2;
    font-weight: 600;
    padding: 5px 8px;
    min-height: 30px;
}
QWidget#sentryV2Root QPushButton[buttonRole="preset"]:hover {
    background-color: #463328;
    border-color: #8d6a54;
}
QWidget#sentryV2Root QPushButton[buttonRole="utility"] {
    background-color: #302520;
    border-color: #5f493d;
    color: #eadfd4;
}
QWidget#sentryV2Root QPushButton[buttonRole="utility"]:hover {
    background-color: #3b2d26;
    border-color: #7b5d4e;
}
QWidget#sentryV2Root QPushButton[buttonRole="dpad"] {
    background-color: #4a3629;
    border: 1px solid #b28357;
    border-radius: 12px;
    color: #fff3e7;
    font-weight: 700;
    font-size: 15px;
    min-height: 40px;
    padding: 6px 8px;
}
QWidget#sentryV2Root QPushButton[buttonRole="dpad"]:hover {
    background-color: #5a4331;
    border-color: #d5a776;
}
QWidget#sentryV2Root QPushButton[buttonRole="dpad"]:pressed {
    background-color: #3b2c21;
    border-color: #9b744f;
}
QWidget#sentryV2Root QPushButton[buttonRole="dpadArrow"] {
    background-color: #5b3125;
    border: 1px solid #cf8656;
    border-radius: 12px;
    color: #fff6ef;
    font-weight: 700;
    font-size: 15px;
    min-height: 40px;
    padding: 6px 8px;
}
QWidget#sentryV2Root QPushButton[buttonRole="dpadArrow"]:hover {
    background-color: #6b3c2c;
    border-color: #e9ab77;
}
QWidget#sentryV2Root QPushButton[buttonRole="dpadArrow"]:pressed {
    background-color: #48291f;
    border-color: #b9784c;
}
QWidget#sentryV2Root QPushButton[buttonRole="mode"] {
    background-color: #38442a;
    border-color: #6d8450;
    color: #f0f8e8;
    font-weight: 600;
}
QWidget#sentryV2Root QPushButton[buttonRole="mode"]:hover {
    background-color: #435133;
    border-color: #89a263;
}
QWidget#sentryV2Root QPushButton[buttonRole="danger"] {
    background-color: #642c23;
    border-color: #c06a58;
    color: #fff2ee;
    font-weight: 700;
}
QWidget#sentryV2Root QPushButton[buttonRole="danger"]:hover {
    background-color: #7a362a;
    border-color: #da7b66;
}
QWidget#sentryV2Root QPushButton[buttonRole="danger"]:pressed {
    background-color: #52221b;
}
QWidget#sentryV2Root QLineEdit,
QWidget#sentryV2Root QComboBox,
QWidget#sentryV2Root QSpinBox,
QWidget#sentryV2Root QDoubleSpinBox,
QWidget#sentryV2Root QListWidget,
QWidget#sentryV2Root QTextEdit {
    background-color: #14100d;
    color: #f0e8df;
    border: 1px solid #5b4739;
    border-radius: 8px;
    padding: 5px 7px;
    selection-background-color: #b15d35;
    selection-color: #fff7ef;
}
QWidget#sentryV2Root QLineEdit:focus,
QWidget#sentryV2Root QComboBox:focus,
QWidget#sentryV2Root QSpinBox:focus,
QWidget#sentryV2Root QDoubleSpinBox:focus,
QWidget#sentryV2Root QListWidget:focus,
QWidget#sentryV2Root QTextEdit:focus {
    border-color: #e0a169;
}
QWidget#sentryV2Root QComboBox::drop-down {
    border: none;
    width: 22px;
}
QWidget#sentryV2Root QAbstractItemView {
    background-color: #18120f;
    color: #f0e8df;
    border: 1px solid #5b4739;
    selection-background-color: #b15d35;
}
QWidget#sentryV2Root QCheckBox {
    spacing: 8px;
}
QWidget#sentryV2Root QCheckBox::indicator {
    width: 16px;
    height: 16px;
    border-radius: 4px;
    border: 1px solid #6d5749;
    background-color: #14100d;
}
QWidget#sentryV2Root QCheckBox::indicator:checked {
    background-color: #f2a65a;
    border-color: #f2a65a;
}
QWidget#sentryV2Root QSlider::groove:horizontal {
    height: 6px;
    border-radius: 3px;
    background-color: #352820;
}
QWidget#sentryV2Root QSlider::handle:horizontal {
    width: 16px;
    margin: -5px 0;
    border-radius: 8px;
    background-color: #f2bb79;
    border: 1px solid #ffd6a3;
}
QWidget#sentryV2Root QScrollBar:vertical {
    background-color: #19130f;
    width: 12px;
    margin: 2px;
}
QWidget#sentryV2Root QScrollBar::handle:vertical {
    background-color: #5d4535;
    border-radius: 6px;
    min-height: 24px;
}
QWidget#sentryV2Root QScrollBar:horizontal {
    background-color: #19130f;
    height: 12px;
    margin: 2px;
}
QWidget#sentryV2Root QScrollBar::handle:horizontal {
    background-color: #5d4535;
    border-radius: 6px;
    min-width: 24px;
}
QWidget#sentryV2Root QScrollBar::add-line,
QWidget#sentryV2Root QScrollBar::sub-line,
QWidget#sentryV2Root QScrollBar::add-page,
QWidget#sentryV2Root QScrollBar::sub-page {
    background: none;
    border: none;
}
QLabel#sentryV2Video {
    background-color: #130e0b;
    color: #a28d79;
    border: 1px solid #50382b;
    border-radius: 0px;
}
QTextEdit#sentryV2Log {
    background-color: #17110e;
    border: 1px solid #644635;
}
"""

SENTRY_V2_STANDALONE_THEME = """
QMainWindow {
    background-color: #120e0c;
    color: #f0e8df;
}
QToolTip {
    background-color: #fde2b0;
    color: #221610;
    border: 1px solid #b07b49;
    padding: 4px 6px;
}
"""

THEME_PRESETS = {
    "ember": {
        "label": "Ember Forge",
        "description": "Warm copper and charcoal styling close to the current Smart Sentry look.",
        "is_light": False,
        "root_bg": "#171310",
        "surface": "#241b16",
        "surface_alt": "#1d1612",
        "panel": "#1a1410",
        "field": "#14100d",
        "border": "#50382b",
        "text": "#f1e8df",
        "muted": "#dacbbe",
        "accent": "#f2a65a",
        "accent_soft": "#d47d4d",
        "hero_start": "#342117",
        "hero_mid": "#4b2c1d",
        "hero_end": "#6d4125",
        "video_bg": "#130e0b",
        "video_text": "#a28d79",
        "tooltip_bg": "#fde2b0",
        "tooltip_text": "#221610",
    },
    "graphite": {
        "label": "Graphite Ops",
        "description": "Neutral steel and slate for a flatter operator console.",
        "is_light": False,
        "root_bg": "#111418",
        "surface": "#1a2027",
        "surface_alt": "#151b21",
        "panel": "#12181d",
        "field": "#0f1419",
        "border": "#384654",
        "text": "#edf2f7",
        "muted": "#b9c6d2",
        "accent": "#8fb2d8",
        "accent_soft": "#6f92b8",
        "hero_start": "#18212b",
        "hero_mid": "#243242",
        "hero_end": "#31475d",
        "video_bg": "#0d1116",
        "video_text": "#8ea2b8",
        "tooltip_bg": "#d8e3ee",
        "tooltip_text": "#16202a",
    },
    "forest": {
        "label": "Forest Watch",
        "description": "Muted greens with a surveillance-console feel for outdoor setups.",
        "is_light": False,
        "root_bg": "#10150f",
        "surface": "#182118",
        "surface_alt": "#131a13",
        "panel": "#111811",
        "field": "#0d130d",
        "border": "#34503b",
        "text": "#edf4ea",
        "muted": "#c3d5c4",
        "accent": "#8fcf7c",
        "accent_soft": "#6fa660",
        "hero_start": "#1f3120",
        "hero_mid": "#2b442c",
        "hero_end": "#446a43",
        "video_bg": "#0d120d",
        "video_text": "#8ea58a",
        "tooltip_bg": "#d9eed2",
        "tooltip_text": "#162114",
    },
    "ocean": {
        "label": "Ocean Relay",
        "description": "Teal-blue glass for a cleaner, more technical telemetry look.",
        "is_light": False,
        "root_bg": "#0e1519",
        "surface": "#152229",
        "surface_alt": "#112026",
        "panel": "#101b20",
        "field": "#0b1519",
        "border": "#315763",
        "text": "#ebf5f7",
        "muted": "#c1d8dd",
        "accent": "#5cc9c9",
        "accent_soft": "#4aa8b4",
        "hero_start": "#123039",
        "hero_mid": "#184451",
        "hero_end": "#236678",
        "video_bg": "#0a1114",
        "video_text": "#86a9b2",
        "tooltip_bg": "#d3eef0",
        "tooltip_text": "#132228",
    },
    "crimson": {
        "label": "Crimson Alert",
        "description": "Deep red tactical styling with stronger alert contrast.",
        "is_light": False,
        "root_bg": "#180f11",
        "surface": "#241517",
        "surface_alt": "#1d1113",
        "panel": "#180f11",
        "field": "#130b0c",
        "border": "#5e3438",
        "text": "#f6eaeb",
        "muted": "#dcc7ca",
        "accent": "#ef7f74",
        "accent_soft": "#d6655a",
        "hero_start": "#381819",
        "hero_mid": "#562223",
        "hero_end": "#783132",
        "video_bg": "#12090a",
        "video_text": "#aa8b8d",
        "tooltip_bg": "#f3d5ce",
        "tooltip_text": "#291415",
    },
    "sand": {
        "label": "Sand Table",
        "description": "A lighter warm control room theme with dark text and softer contrast.",
        "is_light": True,
        "root_bg": "#e8dccb",
        "surface": "#f4eadc",
        "surface_alt": "#eadfce",
        "panel": "#efe5d5",
        "field": "#fff8f0",
        "border": "#af967d",
        "text": "#33261d",
        "muted": "#5b4b40",
        "accent": "#b86d2f",
        "accent_soft": "#985725",
        "hero_start": "#dbc09f",
        "hero_mid": "#cfaf84",
        "hero_end": "#c58e56",
        "video_bg": "#f6ecde",
        "video_text": "#6b5647",
        "tooltip_bg": "#fff8ea",
        "tooltip_text": "#32251b",
    },
    "violet_radar": {
        "label": "Violet Radar",
        "description": "Cool indigo surfaces with sharp radar-screen accents.",
        "is_light": False,
        "root_bg": "#12111a",
        "surface": "#1b1828",
        "surface_alt": "#171522",
        "panel": "#13111c",
        "field": "#0f0d16",
        "border": "#4e4572",
        "text": "#f1edfb",
        "muted": "#cbc3e4",
        "accent": "#a78bfa",
        "accent_soft": "#8f73dd",
        "hero_start": "#231c3a",
        "hero_mid": "#332655",
        "hero_end": "#513987",
        "video_bg": "#0e0c14",
        "video_text": "#958aad",
        "tooltip_bg": "#ece5ff",
        "tooltip_text": "#241b38",
    },
    "solar": {
        "label": "Solar Signal",
        "description": "High-energy amber and steel for a brighter operator deck.",
        "is_light": False,
        "root_bg": "#161311",
        "surface": "#231c16",
        "surface_alt": "#1d1712",
        "panel": "#17120e",
        "field": "#130f0b",
        "border": "#6f5433",
        "text": "#f8efe1",
        "muted": "#e0cfbb",
        "accent": "#ffbf47",
        "accent_soft": "#dd9835",
        "hero_start": "#463016",
        "hero_mid": "#68441a",
        "hero_end": "#91601f",
        "video_bg": "#100c08",
        "video_text": "#ab9372",
        "tooltip_bg": "#fff1cb",
        "tooltip_text": "#35230f",
    },
    "ice": {
        "label": "Ice Array",
        "description": "Bright frosted panels with blue telemetry accents.",
        "is_light": True,
        "root_bg": "#dfeaf1",
        "surface": "#edf5fa",
        "surface_alt": "#dfeaf1",
        "panel": "#e7f0f6",
        "field": "#f9fcfe",
        "border": "#8ea8b8",
        "text": "#1f2a33",
        "muted": "#495b68",
        "accent": "#2e8bc0",
        "accent_soft": "#216f9d",
        "hero_start": "#bdd8e8",
        "hero_mid": "#9ec7df",
        "hero_end": "#70a9cf",
        "video_bg": "#f2f8fb",
        "video_text": "#587080",
        "tooltip_bg": "#ffffff",
        "tooltip_text": "#22313c",
    },
}


def _clamp_int(value: int, minimum: int, maximum: int) -> int:
    return max(minimum, min(maximum, int(value)))


def _hex_to_rgb(color: str) -> Tuple[int, int, int]:
    value = color.strip().lstrip("#")
    if len(value) != 6:
        raise ValueError(f"Expected 6-digit hex color, got {color!r}")
    return int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16)


def _mix_hex(color_a: str, color_b: str, ratio: float) -> str:
    ratio = max(0.0, min(1.0, float(ratio)))
    a_r, a_g, a_b = _hex_to_rgb(color_a)
    b_r, b_g, b_b = _hex_to_rgb(color_b)
    mixed = (
        round(a_r + (b_r - a_r) * ratio),
        round(a_g + (b_g - a_g) * ratio),
        round(a_b + (b_b - a_b) * ratio),
    )
    return f"#{mixed[0]:02x}{mixed[1]:02x}{mixed[2]:02x}"


def _rgba_hex(color: str, alpha_pct: int) -> str:
    red, green, blue = _hex_to_rgb(color)
    alpha = _clamp_int(alpha_pct, 0, 100)
    return f"rgba({red}, {green}, {blue}, {alpha}%)"


class SentryV2TabWidget(QWidget):
    """Primary Smart Sentry desktop control surface and runtime host."""

    # Signals for main app integration.
    turret_move_requested = pyqtSignal(float, float)
    fire_requested = pyqtSignal(int)
    manual_move_requested = pyqtSignal(int, int)
    manual_fire_requested = pyqtSignal(int)
    connection_operation_finished = pyqtSignal(str, bool, str, object, str)
    detection_result_ready = pyqtSignal(object, object, int)
    command_result_ready = pyqtSignal(str, bool, str)
    sentry_enabled_changed = pyqtSignal(bool)
    detection_mode_changed = pyqtSignal(int)
    color_preset_changed = pyqtSignal(str)
    pir_event_received = pyqtSignal(int, float)
    # Thread-safe camera open result signals (emitted from bg thread, handled on main thread)
    _cam_bg_opened = pyqtSignal(object, str, str, int, int, bool)   # (src, backend, backend_name), src_text, kind, rw, rh, rfs
    _cam_bg_failed = pyqtSignal(str)                                 # src_text
    _cam_url_error = pyqtSignal(str)                                 # error message from URL-open bg thread
    _cam_url_ready = pyqtSignal(str, str, int, int, int)             # display_label, source_text, w, h, gen
    _cam_url_status = pyqtSignal(str)                                # live status text from URL-open bg thread
    _yolo_load_result = pyqtSignal(bool, str, str)                   # ok, model_name, error_text
    wifi_autojoin_result = pyqtSignal(bool, str)
    assistant_reply_ready = pyqtSignal(object)
    assistant_models_ready = pyqtSignal(bool, object, str)
    _log_requested = pyqtSignal(str)

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.setObjectName("sentryV2Root")
        self.setMinimumWidth(SENTRY_V2_WIDGET_MIN_WIDTH)
        app = QApplication.instance()
        if app is not None:
            app.installEventFilter(self)

        # Config (try loading saved, else defaults)
        self.config = self._load_settings_config()

        # Standalone communication
        self._comm = SentryV2Comm()
        self._comm.invert_pan = self.config.connection.invert_pan
        self._comm.invert_tilt = self.config.connection.invert_tilt
        self._comm.trigger_mode_bb = self.config.engagement.trigger_mode_bb
        self._sync_comm_runtime_settings_from_config()
        self._comm.set_on_pir_event(self._emit_comm_pir_event)
        self._comm.set_on_transport_log(self._emit_comm_transport_log)
        self._sound_engine = SentryV2SoundEngine(self._queue_sound_tone)
        self._sound_engine.set_enabled(bool(getattr(self.config.sound, "enabled", True)))
        self._sound_engine.set_profile(self._sound_personality_key(), self._sound_attitude_pct())
        self._speech_engine = None
        self._speech_available: bool = False
        self._speech_voice_names: List[str] = []
        self._speech_state_label: str = "waiting"
        self._last_spoken_ai_response: str = ""
        self._assistant_busy: bool = False
        self._assistant_models_loading: bool = False
        self._assistant_available: bool = False
        self._assistant_last_error: str = ""
        self._assistant_models: List[str] = []
        self._assistant_last_reply: Optional[AssistantReply] = None
        self._init_human_speech_engine()
        self._face_library = self._load_face_identity_library()
        self._face_runtime = FaceIdentityRuntime(self._face_library)

        # Standalone detector
        self._detector = SentryV2Detector()
        self._tracker = SimpleBBoxTracker()

        # Engine
        self.engine = SentryV2Engine(self.config)
        self.engine.on_fire(self._on_engine_fire)
        self.engine.on_move(self._on_engine_move)
        self.engine.on_state_change(self._on_engine_state_change)
        self._pan_tilt_motion_enabled: bool = True
        self.engine.set_motion_enabled(self._pan_tilt_motion_enabled)

        # Overlay
        self.overlay = SentryV2Overlay(self.config)

        # Host app integration
        self._main_window_ref: Optional[QWidget] = None
        self._host_hardware_managed: bool = False

        # Track accessory states locally for button text
        self._led_on = False
        self._auto_led_pwm: int = 0
        self._scene_luma: float = 128.0
        self._auto_lighting_frame_counter: int = 0
        self._laser_on = False
        self._acc_on = False
        self._spare_on = False
        self._safety_armed = False
        self._control_source_mode = "app"

        # Own camera
        self._cap: Optional[cv2.VideoCapture] = None
        self._local_source_kind: str = ""
        self._local_source_label: str = ""
        self._test_media_image_frame: Optional[np.ndarray] = None
        self._test_media_last_frame: Optional[np.ndarray] = None
        self._test_media_paused: bool = False
        self._test_media_loop_enabled: bool = True
        self._grab_fail_count: int = 0
        self._MAX_GRAB_FAILS: int = 90  # tolerate brief camera stalls before recovery/close
        self._camera_black_frame_count: int = 0
        self._MAX_CAMERA_BLACK_FRAMES: int = 8
        self._camera_partial_frame_count: int = 0
        self._MAX_CAMERA_PARTIAL_FRAMES: int = 6
        self._CAMERA_HEALTH_GRACE_AFTER_OPEN_S: float = 2.0
        self._camera_health_grace_until_s: float = 0.0
        self._camera_open_in_progress: bool = False
        self._camera_recovery_attempts: int = 0
        self._MAX_CAMERA_RECOVERY_ATTEMPTS: int = 3
        self._camera_recovery_in_progress: bool = False
        self._startup_retry_count: int = -1  # tracks auto-open retries
        # Wire thread-safe camera open result signals
        self._cam_bg_opened.connect(self._on_camera_probe_ready)
        self._cam_bg_failed.connect(self._on_camera_open_failed)
        self._cam_url_error.connect(self._on_url_open_error)
        self._cam_url_ready.connect(self._on_url_ready)
        self._cam_url_status.connect(self._on_url_status_update)
        self._log_requested.connect(self._log)
        self._cam_timer = QTimer(self)
        self._cam_timer.timeout.connect(self._grab_frame)

        # Non-blocking burst fire state
        self._burst_timer = QTimer(self)
        self._burst_timer.setSingleShot(True)
        self._burst_timer.timeout.connect(self._advance_fire_burst)
        self._manual_projectile_fire_release_timer = QTimer(self)
        self._manual_projectile_fire_release_timer.setSingleShot(True)
        self._manual_projectile_fire_release_timer.timeout.connect(self._flush_manual_projectile_fire_release)
        self._manual_projectile_fire_latched: bool = False
        self._manual_projectile_fire_release_pan: float = 0.0
        self._manual_projectile_fire_release_tilt: float = 0.0
        self._manual_sweep_timer = QTimer(self)
        self._manual_sweep_timer.setSingleShot(True)
        self._manual_sweep_timer.timeout.connect(self._advance_manual_sweep)
        self._guided_move_timer = QTimer(self)
        self._guided_move_timer.setSingleShot(True)
        self._guided_move_timer.timeout.connect(self._advance_guided_move)
        self._shutdown_rest_timer = QTimer(self)
        self._shutdown_rest_timer.setSingleShot(True)
        self._shutdown_rest_timer.timeout.connect(self._finalize_graceful_shutdown)
        self._manual_sweep_steps: deque[tuple[float, float, int, str]] = deque()
        self._manual_sweep_active: bool = False
        self._guided_move_steps: deque[tuple[float, float, int]] = deque()
        self._guided_move_active: bool = False
        self._guided_move_finalize_guard: bool = False
        self._guided_move_final_pan: float = self.config.guard.guard_pan
        self._guided_move_final_tilt: float = self.config.guard.guard_tilt
        self._guided_move_log_message: str = ""
        self._burst_remaining: int = 0
        self._burst_interval_ms: int = 50
        self._burst_pan: float = 90.0
        self._burst_tilt: float = 50.0
        self._burst_phase_on: bool = False
        self._last_commanded_pan: float = self.config.guard.guard_pan
        self._last_commanded_tilt: float = self.config.guard.guard_tilt
        self._last_commanded_pose_time_s: float = 0.0
        self._last_commanded_move_time_ms: int = self._get_manual_move_time_ms()
        self._last_tracking_move_time_ms: int = 0
        self._last_tracking_suppression_s: float = 0.0
        self._last_reacquire_note_seen: str = ""
        self._last_pir_note_seen: str = ""
        self._last_blocked_mask_seen: str = ""
        self._last_mask_trace_snapshot: str = ""
        self._last_scope_view_active: bool = False
        self._last_detected_objects: List[DetectedObject] = []
        self._last_display_frame: Optional[np.ndarray] = None
        self._last_raw_frame: Optional[np.ndarray] = None
        self._last_processed_frame_s: float = 0.0
        self._display_frame_interval_s: float = 1.0 / 15.0
        self._busy_display_frame_interval_s: float = 1.0 / 10.0
        self._last_display_present_s: float = 0.0
        self._force_next_display_refresh: bool = True
        self._busy_preview_skip_target_boxes: bool = True
        self._busy_preview_skip_scope_view: bool = True
        self._preview_perf_mode: str = "startup"
        self._sound_prev_visible_targets: int = 0
        self._sound_prev_qualified_targets: int = 0
        self._sound_lock_active: bool = False
        self._tracking_diag_last_key: str = ""
        self._tracking_diag_last_log_s: float = 0.0
        self._tracking_diag_min_interval_s: float = 0.75
        self._last_sound_transport_warn_s: float = 0.0
        self._last_face_matches: List[FaceMatchResult] = []
        self._last_face_match_eval_s: float = 0.0
        self._last_face_person_boxes: List[Tuple[int, int, int, int]] = []
        self._last_face_runtime_status_text: str = ""
        self._last_announced_identity_at: Dict[str, float] = {}
        self._last_gesture_identity_at: Dict[str, float] = {}
        self._shortcut_bindings: List[QShortcut] = []
        self._manual_keyboard_fire_active: bool = False
        self._pir_last_event_sensor: Optional[int] = None
        self._pir_last_event_time_s: float = 0.0
        self._pir_event_count: int = 0
        self._last_camera_source_text: str = str(self.config.connection.camera_source or "").strip() or "0"
        self._last_camera_width: int = int(self.config.connection.camera_width)
        self._last_camera_height: int = int(self.config.connection.camera_height)
        self._mask_capture_active: bool = False
        self._mask_draft_vertices: List[NoFireMaskVertex] = []
        self._prompted_capture_active: bool = False
        self._prompted_list_syncing: bool = False
        self._prompted_detail_syncing: bool = False
        self._show_video_feed: bool = True  # Toggle to hide video display
        self._applying_master_preset: bool = False
        self._applying_servo_preset: bool = False
        self._applying_detection_preset: bool = False
        self._applying_filter_preset: bool = False
        self._applying_threat_preset: bool = False
        self._applying_engagement_preset: bool = False
        self._cleanup_started: bool = False
        self._closing: bool = False
        self._shutdown_in_progress: bool = False
        self._shutdown_complete_callback: Optional[Callable[[], None]] = None
        self._startup_rest_completed: bool = False
        self._startup_rest_pending: bool = bool(getattr(self.config.guard, "rest_on_startup_enabled", True))
        self._startup_rest_schedule_token: int = 0
        self._connection_busy: bool = False
        self._comm_task_queue: "queue.Queue[object]" = queue.Queue()
        self._pending_move_lock = threading.Lock()
        self._pending_move_commands = deque()
        self._manual_move_priority_until: float = 0.0
        self._manual_position_hold_s: float = 1.25
        self._guided_move_allow_rest_tilt: bool = False
        self._last_visible_command_text: str = ""
        self._comm_worker_stop = threading.Event()
        self._comm_worker = threading.Thread(target=self._comm_worker_loop, name="sentry-v2-comm-worker", daemon=True)
        self._comm_worker.start()
        self._detector_frame_lock = threading.Lock()
        self._detector_pending_frame: Optional[np.ndarray] = None
        self._detector_worker_stop = threading.Event()
        self._detector_worker_busy: bool = False
        self._detector_runtime_generation: int = 0
        self._last_detector_error: str = ""
        self._last_detector_error_seen: str = ""
        # URL stream reader thread state (background thread owns the cap for HTTP streams)
        self._url_stream_active: bool = False
        self._url_stream_stop: threading.Event = threading.Event()
        self._url_stream_frame: Optional[np.ndarray] = None
        self._url_stream_frame_lock: threading.Lock = threading.Lock()
        self._url_stream_gen: int = 0  # incremented each open so old threads self-terminate
        self._detector_worker = threading.Thread(target=self._detector_worker_loop, name="sentry-v2-detector-worker", daemon=True)
        self._detector_worker.start()
        self._yolo_auto_load_pending: bool = False
        self._yolo_model_entries: list[tuple[str, str]] = []
        self._prompted_target_library = self._load_prompted_target_library()
        self._prompted_matcher = PromptedTargetMatcher(self._prompted_target_library)
        self._custom_master_profiles: dict[str, dict] = {}
        self._active_master_profile_name: Optional[str] = None
        self._selected_custom_master_profile_name: Optional[str] = None
        self._responsive_button_grids: list[QGridLayout] = []
        self._responsive_box_layouts: list[tuple[QBoxLayout, str]] = []
        self._load_custom_master_profiles()
        self.connection_operation_finished.connect(self._on_connection_operation_finished)
        self.detection_result_ready.connect(self._on_detection_result_ready)
        self.command_result_ready.connect(self._on_command_result_ready)
        self.pir_event_received.connect(self._on_comm_pir_event_received)
        self._yolo_load_result.connect(self._on_yolo_load_result)
        self.assistant_reply_ready.connect(self._on_ai_assistant_reply_ready)
        self.assistant_models_ready.connect(self._on_ai_assistant_models_ready)
        self._yolo_loading: bool = False
        self._yolo_runtime_prepared: bool = False
        self._yolo_runtime_diag_dumped: bool = False
        self._runtime_lib_paths_prepared: bool = False
        self._runtime_dll_dir_handles: list[object] = []
        self._startup_autoconnect_active: bool = False
        self._startup_autoconnect_retry: int = 0
        self._pending_quiet_save: bool = False
        self._last_wifi_autojoin_attempt_s: float = 0.0
        self._last_wifi_link_refresh_s: float = 0.0
        self._wifi_autojoin_inflight: bool = False
        self._wifi_runtime_refresh_inflight: bool = False
        self._last_wifi_autojoin_note: str = ""
        self._last_runtime_snapshot_json_path: Optional[Path] = None
        self._last_runtime_snapshot_markdown_path: Optional[Path] = None
        self._last_log_export_path: Optional[Path] = None
        self._right_panel: Optional[QWidget] = None
        self._tabs_nav_layout: Optional[QHBoxLayout] = None
        self._tabs_nav_title_label: Optional[QLabel] = None
        self._hero_layout: Optional[QHBoxLayout] = None
        self._hero_action_row: Optional[QVBoxLayout] = None
        self._hero_actions_layout: Optional[QVBoxLayout] = None
        self._hero_title_label: Optional[QLabel] = None
        self._hero_subtitle_label: Optional[QLabel] = None
        self._hero_badge_label: Optional[QLabel] = None
        self._manual_control_buttons: list[QPushButton] = []
        self._responsive_lists: list[tuple[QListWidget, str]] = []
        self._responsive_labels: list[tuple[QLabel, str]] = []
        self._log_entries: list[tuple[str, str, str]] = []
        self._log_paused: bool = False
        self._log_filter_key: str = "all"
        self._log_paused_pending_count: int = 0
        self._log_filter_buttons: Dict[str, QPushButton] = {}
        self._layout_restore_attempts: int = 0
        self._layout_restore_complete: bool = False

        # Build UI
        self._build_ui()
        self._apply_theme()
        self._install_global_shortcuts()

        self._quiet_save_timer = QTimer(self)
        self._quiet_save_timer.setSingleShot(True)
        self._quiet_save_timer.timeout.connect(self._flush_quiet_config_save)

        # Status refresh timer
        self._status_timer = QTimer(self)
        self._status_timer.timeout.connect(self._refresh_status)
        self._status_timer.start(1200)
        QTimer.singleShot(0, self._refresh_ai_provider_status)
        self._link_watchdog_timer = QTimer(self)
        self._link_watchdog_timer.timeout.connect(self._connection_watchdog_tick)
        self._link_watchdog_timer.start(2000)
        self.wifi_autojoin_result.connect(self._on_wifi_autojoin_result)
        self._schedule_startup_tasks()

    def _load_settings_config(self) -> SentryV2Config:
        """Load settings from the active release path and migrate older aliases forward."""
        canonical = CANONICAL_SETTINGS_PATH
        selected = canonical
        for candidate in [
            CANONICAL_SETTINGS_PATH,
            SMART_SENTRY_V2_3_2_SETTINGS_PATH,
            SMART_SENTRY_V2_3_1_SETTINGS_PATH,
            LEGACY_SMART_SENTRY_V3_SETTINGS_PATH,
            LEGACY_SENTRY_V2_SETTINGS_PATH,
        ]:
            if candidate.exists():
                selected = candidate
                break

        cfg = SentryV2Config.load(str(selected))
        cfg.config_path = CANONICAL_SETTINGS_RELATIVE_PATH
        prompted_value = str(cfg.prompted_library_path or CANONICAL_PROMPTED_TARGETS_RELATIVE_PATH)
        normalized_prompted = prompted_value.replace("\\", "/")
        if normalized_prompted.endswith("smart_sentry_v3_prompted_targets.json") or normalized_prompted.endswith("sentry_v2_prompted_targets.json") or normalized_prompted.endswith("smart_sentry_v2_3_1_prompted_targets.json") or normalized_prompted.endswith("smart_sentry_v2_3_2_prompted_targets.json"):
            cfg.prompted_library_path = CANONICAL_PROMPTED_TARGETS_RELATIVE_PATH
        prompted = Path(str(cfg.prompted_library_path or CANONICAL_PROMPTED_TARGETS_RELATIVE_PATH))
        if prompted.is_absolute():
            cfg.prompted_library_path = self._portable_path_string(prompted)

        if selected != canonical and selected.exists():
            try:
                cfg.save(str(canonical))
            except Exception as exc:
                print(f"[SENTRY_V2_TAB] Failed to migrate legacy settings to active canonical path: {exc}", flush=True)

        return cfg

    def _sync_legacy_settings_copy(self, cfg: Optional[SentryV2Config] = None) -> None:
        """Legacy config aliases are no longer maintained for the 2.3.2 runtime package."""
        return

    def _portable_path_string(self, path_obj: Path) -> str:
        """Prefer repo-relative paths so settings stay portable across machines."""
        repo_root = self._repo_root_path().resolve()
        try:
            return path_obj.resolve().relative_to(repo_root).as_posix()
        except Exception:
            return str(path_obj)

    def _custom_master_preset_path(self) -> Path:
        if CANONICAL_CUSTOM_PRESET_PATH.exists():
            return CANONICAL_CUSTOM_PRESET_PATH
        if SMART_SENTRY_V2_3_2_CUSTOM_PRESET_PATH.exists():
            return SMART_SENTRY_V2_3_2_CUSTOM_PRESET_PATH
        if SMART_SENTRY_V2_3_1_CUSTOM_PRESET_PATH.exists():
            return SMART_SENTRY_V2_3_1_CUSTOM_PRESET_PATH
        if LEGACY_SMART_SENTRY_V3_CUSTOM_PRESET_PATH.exists():
            return LEGACY_SMART_SENTRY_V3_CUSTOM_PRESET_PATH
        if LEGACY_SENTRY_V2_CUSTOM_PRESET_PATH.exists():
            return LEGACY_SENTRY_V2_CUSTOM_PRESET_PATH
        return CANONICAL_CUSTOM_PRESET_PATH

    def _schedule_startup_tasks(self) -> None:
        """CHANGE WARNING: Startup work here couples camera bring-up, transport auto-connect, and YOLO warmup; keep expensive work deferred when quick startup is enabled."""
        if bool(getattr(self.config, "quick_startup_enabled", True)):
            self._log("Quick startup enabled: deferring auto camera open and auto-connect; scheduling lazy YOLO model load.")
            self._schedule_auto_yolo_load(2500)
            QTimer.singleShot(0, self._schedule_startup_rest_move)
            return
        self._schedule_auto_yolo_load(1200)
        QTimer.singleShot(800, self._auto_open_camera_on_startup)
        QTimer.singleShot(1000, lambda: self._auto_connect_on_startup(0))
        QTimer.singleShot(0, self._schedule_startup_rest_move)

    def _auto_open_camera_on_startup(self, _retry: int = 0) -> None:
        self._log(f"[CAM-DEBUG] _auto_open_camera_on_startup called: retry={_retry}, closing={self._closing}, has_source={self._has_local_source()}")
        if self._closing or self._has_local_source():
            return
        self._startup_retry_count = _retry
        try:
            self._toggle_camera()
        except Exception as exc:
            self._set_camera_status(f"Auto-open failed: {exc}", "error")
            self._log(f"[CAM-DEBUG] Auto-open exception (attempt {_retry+1}): {exc}")
            if not self._closing and not self._has_local_source() and _retry < 3:
                delay = 1500 * (_retry + 1)
                QTimer.singleShot(delay, lambda r=_retry+1: self._auto_open_camera_on_startup(r))

    def _auto_connect_on_startup(self, _retry: int = 0) -> None:
        """Auto-connect on startup if in WiFi mode and not already connected."""
        if self._host_controls_hardware():
            return  # Host app manages connection
        if self._comm.is_connected():
            return  # Already connected
        if self._connection_busy:
            return  # Connection operation in progress

        # Only auto-connect for WiFi modes (2=WiFi+Debug, 3=WiFi Full)
        mode = self.config.connection.connection_type
        if mode not in (2, 3):
            return

        # In mode 2, resolve the live Debug Board COM port at startup.
        # Windows can reassign COM numbers across reconnects or between PCs.
        if mode == 2:
            configured_port = str(self._edit_debug_port.text() or self.config.connection.debug_port or "").strip()
            resolved_debug = self._resolve_serial_port("debug", configured_port)
            if resolved_debug:
                if resolved_debug != configured_port:
                    self._log(f"Auto-connect resolved Debug Board COM port: {resolved_debug}")
                self._edit_debug_port.setText(resolved_debug)
                self.config.connection.debug_port = resolved_debug
            elif _retry < 4:
                delay_ms = 1000 * (_retry + 1)
                self._log(
                    f"Auto-connect wait: Debug Board COM port not resolved yet (retry {_retry + 1}/4 in {delay_ms}ms)"
                )
                QTimer.singleShot(delay_ms, lambda r=_retry + 1: self._auto_connect_on_startup(r))
                return

        self._startup_autoconnect_active = True
        self._startup_autoconnect_retry = _retry

        self._log(f"Auto-connecting in mode {mode} (attempt {_retry + 1})...")
        self._toggle_connection()

    def _has_rest_move_transport(self) -> bool:
        return bool(self._host_controls_hardware() or self._comm.is_connected())

    def _rest_position(self) -> Tuple[float, float]:
        guard = self.config.guard
        pan_min, pan_max = sorted((float(guard.pan_min), float(guard.pan_max)))
        rest_pan = min(pan_max, max(pan_min, float(getattr(guard, "rest_pan", guard.guard_pan))))
        rest_tilt = min(SENTRY_TILT_MAX, max(SENTRY_TILT_MIN, float(getattr(guard, "rest_tilt", guard.guard_tilt))))
        return rest_pan, rest_tilt

    def _rest_position_text(self) -> str:
        pan, tilt = self._rest_position()
        return f"P{pan:.0f} T{tilt:.0f}"

    def _play_rest_cue(self, *, closing: bool = False) -> None:
        if not bool(getattr(self.config.sound, "enabled", True)):
            return
        if not bool(getattr(self.config.sound, "rest_cue_enabled", True)):
            return
        self._sound_engine.note_rest_position(closing=closing)

    def _play_home_cue(self, *, waking_from_rest: bool = False) -> None:
        if not bool(getattr(self.config.sound, "enabled", True)):
            return
        if not bool(getattr(self.config.sound, "rest_cue_enabled", True)):
            return
        self._sound_engine.note_home_position(waking_from_rest=waking_from_rest)

    def _is_near_rest_position(self, pan: float, tilt: float, *, tolerance_deg: float) -> bool:
        rest_pan, rest_tilt = self._rest_position()
        return max(abs(float(pan) - rest_pan), abs(float(tilt) - rest_tilt)) <= float(max(1.0, tolerance_deg))

    def _guided_move_profile(self, maneuver: str, start_pan: float, start_tilt: float) -> Tuple[float, float, float]:
        guard = self.config.guard
        approach_window = float(max(4.0, getattr(guard, "guided_move_approach_window_deg", 18.0) or 18.0))
        if maneuver == "rest":
            cruise_speed = float(max(2.0, getattr(guard, "rest_move_speed_dps", 14.0) or 14.0))
            approach_speed = float(max(1.0, getattr(guard, "rest_move_approach_speed_dps", 5.0) or 5.0))
            return cruise_speed, min(cruise_speed, approach_speed), approach_window

        cruise_speed = float(max(2.0, getattr(guard, "home_move_speed_dps", 24.0) or 24.0))
        approach_speed = float(max(1.0, getattr(guard, "home_move_approach_speed_dps", 11.0) or 11.0))
        if self._is_near_rest_position(start_pan, start_tilt, tolerance_deg=max(6.0, approach_window * 0.45)):
            cruise_speed *= 0.72
            approach_speed *= 0.65
        return cruise_speed, min(cruise_speed, approach_speed), approach_window

    def _build_guided_move_steps(
        self,
        start_pan: float,
        start_tilt: float,
        target_pan: float,
        target_tilt: float,
        *,
        maneuver: str,
        cruise_speed_dps: float,
        approach_speed_dps: float,
        approach_window_deg: float,
    ) -> list[tuple[float, float, int]]:
        total_distance = max(abs(float(target_pan) - float(start_pan)), abs(float(target_tilt) - float(start_tilt)))
        if total_distance < 0.35:
            speed = max(1.0, float(approach_speed_dps))
            move_time_ms = int(max(90, min(2200, round((max(total_distance, 0.1) / speed) * 1000.0))))
            return [(float(target_pan), float(target_tilt), move_time_ms)]

        window = max(4.0, float(approach_window_deg))
        step_denominator = max(2.2, window * (0.22 if maneuver == "rest" else 0.26))
        min_steps = 8 if maneuver == "rest" else 6
        max_steps = 22 if maneuver == "rest" else 16
        step_count = int(max(min_steps, min(max_steps, round(total_distance / step_denominator) + 2)))
        min_stage_ms = 70 if maneuver == "rest" else 85
        steps: list[tuple[float, float, int]] = []
        prev_pan = float(start_pan)
        prev_tilt = float(start_tilt)
        for index in range(1, step_count + 1):
            progress = float(index) / float(step_count)
            eased = 1.0 - ((1.0 - progress) ** 2.45)
            next_pan = float(start_pan) + ((float(target_pan) - float(start_pan)) * eased)
            next_tilt = float(start_tilt) + ((float(target_tilt) - float(start_tilt)) * eased)
            segment_distance = max(abs(next_pan - prev_pan), abs(next_tilt - prev_tilt), 0.05)
            remaining_distance = max(abs(float(target_pan) - next_pan), abs(float(target_tilt) - next_tilt))
            slowdown_mix = 1.0 - min(1.0, remaining_distance / window)
            speed_dps = float(cruise_speed_dps) - ((float(cruise_speed_dps) - float(approach_speed_dps)) * slowdown_mix)
            move_time_ms = int(round((segment_distance / max(1.0, speed_dps)) * 1000.0))
            tail_bias_ms = 40.0 if maneuver == "rest" else 55.0
            move_time_ms = int(max(min_stage_ms, min(2200, move_time_ms + int(round(tail_bias_ms * slowdown_mix)))))
            steps.append((next_pan, next_tilt, move_time_ms))
            prev_pan = next_pan
            prev_tilt = next_tilt
        return steps

    @staticmethod
    def _guided_move_interval_ms(move_time_ms: int, maneuver: str) -> int:
        overlap_ratio = 0.52 if maneuver == "rest" else 0.58
        minimum = 40 if maneuver == "rest" else 55
        return int(max(minimum, min(900, round(float(move_time_ms) * overlap_ratio))))

    def _finish_guided_move(self, *, cancelled: bool = False) -> None:
        was_active = bool(self._guided_move_active)
        finalize_guard = bool(self._guided_move_finalize_guard)
        final_pan = float(self._guided_move_final_pan)
        final_tilt = float(self._guided_move_final_tilt)
        log_message = str(self._guided_move_log_message or "")
        self._guided_move_timer.stop()
        self._guided_move_steps.clear()
        self._guided_move_active = False
        self._guided_move_finalize_guard = False
        self._guided_move_allow_rest_tilt = False
        self._guided_move_log_message = ""
        if not was_active:
            return
        if not cancelled and finalize_guard:
            self.engine.hold_current_guard_position(final_pan, final_tilt)
        if not cancelled:
            self._refresh_status()
            if log_message and not self._closing:
                self._log(log_message)

    def _advance_guided_move(self) -> None:
        if self._closing:
            self._finish_guided_move(cancelled=True)
            return
        if not self._guided_move_steps:
            self._finish_guided_move(cancelled=False)
            return

        target_pan, target_tilt, move_time_ms = self._guided_move_steps.popleft()
        self.engine.current_pan = float(target_pan)
        self.engine.current_tilt = float(target_tilt)
        if self._host_controls_hardware():
            self.turret_move_requested.emit(float(target_pan), float(target_tilt))
        else:
            self._queue_move_command(
                float(target_pan),
                float(target_tilt),
                move_time_ms=int(move_time_ms),
                manual_override=True,
                allow_rest_tilt=bool(self._guided_move_allow_rest_tilt),
            )
        self._remember_commanded_position(float(target_pan), float(target_tilt), move_time_ms=int(move_time_ms))
        self._suppress_motion_detection()
        self._refresh_status()
        next_interval_ms = self._guided_move_interval_ms(int(move_time_ms), "rest" if self._guided_move_allow_rest_tilt else "home")
        self._guided_move_timer.start(next_interval_ms)

    def _start_guided_position_move(
        self,
        target_pan: float,
        target_tilt: float,
        *,
        maneuver: str,
        hold_guard: bool = False,
        log_message: str = "",
    ) -> int:
        allow_rest_tilt = maneuver == "rest"
        target_pan, target_tilt = self._clamp_manual_angles(target_pan, target_tilt, allow_rest_tilt=allow_rest_tilt)
        start_pan, start_tilt = self._clamp_manual_angles(
            float(self.engine.current_pan),
            float(self.engine.current_tilt),
            allow_rest_tilt=allow_rest_tilt,
        )
        if self._host_controls_hardware():
            self._move_to_absolute_position(
                target_pan,
                target_tilt,
                hold_guard=hold_guard,
                log_message=log_message,
                allow_rest_tilt=allow_rest_tilt,
            )
            return int(self._get_manual_move_time_ms())

        total_distance = max(abs(target_pan - start_pan), abs(target_tilt - start_tilt))
        if total_distance < 0.35:
            self._move_to_absolute_position(target_pan, target_tilt, hold_guard=hold_guard, log_message=log_message)
            return int(self._get_manual_move_time_ms())

        self._finish_manual_sweep()
        self._finish_guided_move(cancelled=True)
        cruise_speed, approach_speed, approach_window = self._guided_move_profile(maneuver, start_pan, start_tilt)
        steps = self._build_guided_move_steps(
            start_pan,
            start_tilt,
            target_pan,
            target_tilt,
            maneuver=maneuver,
            cruise_speed_dps=cruise_speed,
            approach_speed_dps=approach_speed,
            approach_window_deg=approach_window,
        )
        if not steps:
            self._move_to_absolute_position(target_pan, target_tilt, hold_guard=hold_guard, log_message=log_message)
            return int(self._get_manual_move_time_ms())

        total_duration_ms = int(sum(step[2] + 80 for step in steps))
        self._manual_move_priority_until = max(
            float(getattr(self, "_manual_move_priority_until", 0.0) or 0.0),
            time.time() + max(1.25, (float(total_duration_ms) / 1000.0) + 0.40),
        )
        self._guided_move_steps = deque((float(pan), float(tilt), int(move_time_ms)) for pan, tilt, move_time_ms in steps)
        self._guided_move_active = True
        self._guided_move_finalize_guard = bool(hold_guard)
        self._guided_move_allow_rest_tilt = bool(allow_rest_tilt)
        self._guided_move_final_pan = float(target_pan)
        self._guided_move_final_tilt = float(target_tilt)
        self._guided_move_log_message = str(log_message or "")
        self._advance_guided_move()
        return total_duration_ms

    def _move_to_rest(self, *, reason: str = "manual", log_message: str = "") -> None:
        pan, tilt = self._rest_position()
        self._play_rest_cue(closing=(reason == "close"))
        message = log_message or {
            "startup": f"Startup rest position: {self._rest_position_text()}",
            "close": f"Closing to rest position: {self._rest_position_text()}",
        }.get(reason, f"Moving to rest: {self._rest_position_text()}")
        return self._start_guided_position_move(pan, tilt, maneuver="rest", hold_guard=False, log_message=message)

    def _schedule_startup_rest_move(self) -> None:
        if self._closing or self._cleanup_started or self._shutdown_in_progress:
            return
        if not bool(getattr(self.config.guard, "rest_on_startup_enabled", True)):
            self._startup_rest_pending = False
            return
        if self._startup_rest_completed:
            return
        if not self._has_rest_move_transport():
            self._startup_rest_pending = True
            return
        self._startup_rest_pending = False
        self._startup_rest_completed = True
        delay_ms = max(0, int(getattr(self.config.guard, "rest_startup_delay_ms", 900) or 0))
        self._startup_rest_schedule_token += 1
        token = int(self._startup_rest_schedule_token)
        QTimer.singleShot(delay_ms, lambda current_token=token: self._execute_startup_rest_move(current_token))

    def _execute_startup_rest_move(self, token: Optional[int] = None) -> None:
        if self._closing or self._cleanup_started or self._shutdown_in_progress:
            return
        if token is not None and int(token) != int(getattr(self, "_startup_rest_schedule_token", 0)):
            return
        if not bool(getattr(self.config.guard, "rest_on_startup_enabled", True)):
            self._startup_rest_pending = False
            return
        if not self._has_rest_move_transport():
            self._startup_rest_completed = False
            self._startup_rest_pending = True
            return
        self._move_to_rest(reason="startup")

    def begin_graceful_shutdown(self, on_complete: Optional[Callable[[], None]] = None) -> bool:
        if on_complete is not None:
            self._shutdown_complete_callback = on_complete
        if self._cleanup_started:
            callback = self._shutdown_complete_callback
            self._shutdown_complete_callback = None
            if callback is not None:
                QTimer.singleShot(0, callback)
            return True
        if self._shutdown_in_progress:
            return True

        self._shutdown_in_progress = True
        self._startup_rest_pending = False
        try:
            self._stop_fire_burst(send_release=True)
        except Exception:
            pass
        try:
            self._finish_manual_sweep()
        except Exception:
            pass
        try:
            self.engine.stop()
        except Exception:
            pass

        if bool(getattr(self.config.guard, "rest_on_close_enabled", True)) and self._has_rest_move_transport():
            planned_move_ms = int(self._move_to_rest(reason="close") or 0)
            timeout_ms = max(
                300,
                int(getattr(self.config.guard, "rest_close_timeout_ms", 1600) or 1600),
                planned_move_ms + 300,
            )
            self._shutdown_rest_timer.start(timeout_ms)
        else:
            QTimer.singleShot(0, self._finalize_graceful_shutdown)
        return True

    def _finalize_graceful_shutdown(self) -> None:
        if self._cleanup_started:
            return
        self._shutdown_rest_timer.stop()
        callback = self._shutdown_complete_callback
        self._shutdown_complete_callback = None
        self.cleanup()
        if callback is not None:
            QTimer.singleShot(0, callback)

    def cleanup(self) -> None:
        """Stop timers and release all resources. Safe to call multiple times."""
        if self._cleanup_started:
            return
        self._cleanup_started = True
        self._closing = True
        app = QApplication.instance()
        if app is not None:
            try:
                app.removeEventFilter(self)
            except Exception:
                pass
        self._shutdown_in_progress = False
        self._shutdown_rest_timer.stop()
        self._comm_worker_stop.set()
        self._detector_worker_stop.set()
        self._guided_move_timer.stop()
        with self._pending_move_lock:
            self._pending_move_commands.clear()
            self._manual_move_priority_until = 0.0
        with self._detector_frame_lock:
            self._detector_pending_frame = None
        try:
            self._comm_task_queue.put_nowait(None)
        except Exception:
            pass
        try:
            self._sound_engine.close()
        except Exception:
            pass
        try:
            self._stop_human_speech()
        except Exception:
            pass
        self._cam_timer.stop()
        self._burst_timer.stop()
        self._manual_sweep_timer.stop()
        self._guided_move_timer.stop()
        self._status_timer.stop()
        self._link_watchdog_timer.stop()
        self._quiet_save_timer.stop()
        try:
            self.engine.stop()
        except Exception:
            pass
        self._stop_fire_burst(send_release=False)
        self._close_camera()
        self._comm.disconnect()

    def closeEvent(self, event):
        """Release camera and serial on close."""
        if self._cleanup_started:
            try:
                if event is not None:
                    event.accept()
            except Exception:
                pass
            super().closeEvent(event)
            return
        try:
            if event is not None:
                event.ignore()
        except Exception:
            pass
        self.begin_graceful_shutdown(on_complete=self.close)

    # ================================================================== #
    #  UI Construction
    # ================================================================== #

    def _build_ui(self) -> None:
        root = QVBoxLayout(self)
        root.setContentsMargins(8, 8, 8, 8)
        # CHANGE WARNING: Keep the settings tab container compact in both axes. Hidden pages must not force the right pane wider or taller than the visible viewport because each page already scrolls independently.

        self._main_splitter = QSplitter(Qt.Horizontal)
        self._main_splitter.setChildrenCollapsible(False)
        self._main_splitter.setHandleWidth(8)
        self._main_splitter.splitterMoved.connect(self._on_main_splitter_moved)

        self._layout_splitter = QSplitter(Qt.Vertical)
        self._layout_splitter.setChildrenCollapsible(False)
        self._layout_splitter.setHandleWidth(8)
        self._layout_splitter.splitterMoved.connect(self._on_layout_splitter_moved)

        # --- Left: video feed ---
        self._video_label = SentryV2VideoCanvas("Waiting for video...")
        self._video_label.setObjectName("sentryV2Video")
        self._video_label.setAlignment(Qt.AlignCenter)
        self._video_label.setMinimumSize(SENTRY_V2_VIDEO_MIN_WIDTH, 180)
        self._video_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        logo_path = APP_ROOT_PATH / "LOGO.png"
        if logo_path.is_file():
            self._video_label.set_placeholder_pixmap(QPixmap(str(logo_path)))
            self._video_label.set_placeholder_text("Camera Off\nOpen Camera to Start")
            self._video_label.set_placeholder_enabled(False)
        self._video_label.frameClicked.connect(self._on_video_frame_clicked)
        self._video_label.frameRightClicked.connect(self._on_video_frame_right_clicked)
        self._video_label.roiSelected.connect(self._on_video_roi_selected)

        left_panel = QWidget()
        left_panel.setObjectName("sentryV2LeftPane")
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(0)

        # Wrap video label + quick-access chip bar in a container
        _video_container = QWidget()
        _video_container_lay = QVBoxLayout(_video_container)
        _video_container_lay.setContentsMargins(0, 0, 0, 0)
        _video_container_lay.setSpacing(0)
        _video_container_lay.addWidget(self._video_label, 1)

        # Quick-access chip bar
        _qa_chip_bar = QWidget()
        _qa_chip_bar.setObjectName("sentryV2QAChipBar")
        _qa_chip_bar_lay = QHBoxLayout(_qa_chip_bar)
        _qa_chip_bar_lay.setContentsMargins(4, 2, 4, 2)
        _qa_chip_bar_lay.setSpacing(8)

        self._chk_auto_lighting_qa = QCheckBox("Auto Lighting")
        self._chk_auto_lighting_qa.setChecked(bool(getattr(self.config.lighting, "auto_lighting_enabled", False)))
        self._chk_auto_lighting_qa.toggled.connect(self._on_auto_lighting_toggled)
        self._set_theme_role(self._chk_auto_lighting_qa, "compactValue")
        _qa_chip_bar_lay.addWidget(self._chk_auto_lighting_qa)

        self._lbl_auto_luma_qa = QLabel("")
        self._set_theme_role(self._lbl_auto_luma_qa, "mutedCompact")
        _qa_chip_bar_lay.addWidget(self._lbl_auto_luma_qa)
        _qa_chip_bar_lay.addStretch(1)

        _video_container_lay.addWidget(_qa_chip_bar, 0)

        self._layout_splitter.addWidget(_video_container)

        self._bottom_info_splitter = QSplitter(Qt.Horizontal)
        self._bottom_info_splitter.setChildrenCollapsible(False)
        self._bottom_info_splitter.setHandleWidth(8)
        self._bottom_info_splitter.splitterMoved.connect(self._on_bottom_info_splitter_moved)
        self._bottom_info_splitter.addWidget(self._build_log_group())
        self._bottom_info_splitter.addWidget(self._build_status_group())
        self._bottom_info_splitter.setStretchFactor(0, 2)
        self._bottom_info_splitter.setStretchFactor(1, 3)
        self._layout_splitter.addWidget(self._bottom_info_splitter)
        self._layout_splitter.setStretchFactor(0, 5)
        self._layout_splitter.setStretchFactor(1, 1)
        left_layout.addWidget(self._layout_splitter)
        self._main_splitter.addWidget(left_panel)

        # --- Right: full-height controls with fixed tabs and per-page scrolling ---
        panel_layout = QVBoxLayout()
        panel_layout.setContentsMargins(0, 0, 0, 0)
        panel_layout.setSpacing(6)

        pinned_top = QWidget()
        pinned_top.setObjectName("sentryV2PinnedTop")
        pinned_top_layout = QVBoxLayout(pinned_top)
        pinned_top_layout.setContentsMargins(4, 2, 4, 6)
        pinned_top_layout.setSpacing(8)

        hero = QFrame()
        hero.setObjectName("sentryV3Hero")
        hero_layout = QHBoxLayout(hero)
        self._hero_layout = hero_layout
        hero_layout.setContentsMargins(18, 14, 18, 14)
        hero_layout.setSpacing(14)

        hero_text_layout = QVBoxLayout()
        hero_text_layout.setContentsMargins(0, 0, 0, 0)
        hero_text_layout.setSpacing(2)
        hero_title = QLabel(SMART_SENTRY_RELEASE_TITLE)
        self._hero_title_label = hero_title
        hero_title.setObjectName("sentryV3HeroTitle")
        hero_title.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        hero_subtitle = QLabel(SMART_SENTRY_RELEASE_SUBTITLE)
        self._hero_subtitle_label = hero_subtitle
        hero_subtitle.setObjectName("sentryV3HeroSubtitle")
        hero_subtitle.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        hero_text_layout.addWidget(hero_title)
        hero_text_layout.addWidget(hero_subtitle)
        hero_layout.addLayout(hero_text_layout, stretch=1)

        hero_actions_layout = QVBoxLayout()
        self._hero_actions_layout = hero_actions_layout
        hero_actions_layout.setContentsMargins(0, 0, 0, 0)
        hero_actions_layout.setSpacing(8)
        hero_actions_layout.setAlignment(Qt.AlignTop)

        hero_action_row = QVBoxLayout()
        self._hero_action_row = hero_action_row
        hero_action_row.setContentsMargins(0, 0, 0, 0)
        hero_action_row.setSpacing(8)

        self._btn_header_wake = QPushButton("Wake Up")
        self._btn_header_wake.setMinimumHeight(34)
        self._set_button_role(self._btn_header_wake, "utility")
        self._btn_header_wake.setToolTip("Move the turret back to the configured ready position.")
        self._btn_header_wake.clicked.connect(self._on_home_clicked)
        hero_action_row.addWidget(self._btn_header_wake)

        self._btn_header_rest = QPushButton("Go Rest")
        self._btn_header_rest.setMinimumHeight(34)
        self._set_button_role(self._btn_header_rest, "utility")
        self._btn_header_rest.setToolTip("Move the turret to the configured rest position.")
        self._btn_header_rest.clicked.connect(self._on_rest_clicked)
        hero_action_row.addWidget(self._btn_header_rest)

        hero_actions_layout.addLayout(hero_action_row)

        hero_badge = QLabel(SMART_SENTRY_RELEASE_BADGE)
        self._hero_badge_label = hero_badge
        hero_badge.setObjectName("sentryV3HeroBadge")
        hero_badge.setVisible(bool(SMART_SENTRY_RELEASE_BADGE.strip()))
        hero_actions_layout.addWidget(hero_badge, alignment=Qt.AlignRight | Qt.AlignTop)
        hero_layout.addLayout(hero_actions_layout)
        pinned_top_layout.addWidget(hero)

        toggle_row = QWidget()
        toggle_row.setObjectName("sentryV2ToggleRow")
        toggle_row_layout = QHBoxLayout(toggle_row)
        toggle_row_layout.setContentsMargins(12, 8, 12, 8)
        toggle_row_layout.setSpacing(16)

        # Enable toggle
        self._chk_enable = QCheckBox("Enable Smart Sentry")
        self._set_theme_role(self._chk_enable, "headlineToggle")
        self._chk_enable.toggled.connect(self._on_enable_toggled)
        toggle_row_layout.addWidget(self._chk_enable)

        # Show video feed toggle
        self._chk_show_video = QCheckBox("Show Video Feed")
        self._set_theme_role(self._chk_show_video, "headlineToggle")
        self._chk_show_video.setChecked(True)
        self._chk_show_video.toggled.connect(self._on_show_video_toggled)
        self._chk_show_video.setToolTip("Toggle video display on/off (detection continues running)")
        toggle_row_layout.addWidget(self._chk_show_video)
        toggle_row_layout.addStretch(1)

        self._btn_quick_keys = QPushButton("Quick Keys")
        self._btn_quick_keys.setMinimumHeight(30)
        self._set_button_role(self._btn_quick_keys, "utility")
        self._btn_quick_keys.setToolTip("Open the Smart Sentry keyboard shortcut quick reference.")
        self._btn_quick_keys.clicked.connect(self._open_shortcut_quick_view)
        toggle_row_layout.addWidget(self._btn_quick_keys)
        pinned_top_layout.addWidget(toggle_row)

        panel_layout.addWidget(pinned_top)

        tabs_nav = QWidget()
        tabs_nav.setObjectName("sentryV2TabsNav")
        tabs_nav_layout = QHBoxLayout(tabs_nav)
        self._tabs_nav_layout = tabs_nav_layout
        tabs_nav_layout.setContentsMargins(6, 6, 6, 6)
        tabs_nav_layout.setSpacing(10)
        tabs_nav_title = QLabel("")
        self._tabs_nav_title_label = tabs_nav_title
        tabs_nav_title.setObjectName("sentryV2TabsNavTitle")
        tabs_nav_title.setVisible(False)
        tabs_nav_layout.addWidget(tabs_nav_title)
        self._settings_nav_label = QLabel("")
        self._settings_nav_label.setObjectName("sentryV2TabsNavCount")
        self._settings_nav_label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        tabs_nav_layout.addWidget(self._settings_nav_label)
        tabs_nav_layout.addStretch(1)
        self._btn_prev_settings_tab = QPushButton("❮")
        self._btn_prev_settings_tab.setToolTip("Go to the previous settings tab")
        self._btn_prev_settings_tab.clicked.connect(self._select_previous_settings_tab)
        self._btn_prev_settings_tab.setFixedSize(34, 26)
        self._btn_prev_settings_tab.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self._set_button_role(self._btn_prev_settings_tab, "dpadArrow")
        tabs_nav_layout.addWidget(self._btn_prev_settings_tab)
        self._btn_next_settings_tab = QPushButton("❯")
        self._btn_next_settings_tab.setToolTip("Go to the next settings tab")
        self._btn_next_settings_tab.clicked.connect(self._select_next_settings_tab)
        self._btn_next_settings_tab.setFixedSize(34, 26)
        self._btn_next_settings_tab.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self._set_button_role(self._btn_next_settings_tab, "dpadArrow")
        tabs_nav_layout.addWidget(self._btn_next_settings_tab)
        panel_layout.addWidget(tabs_nav)

        # Sub-tabs for settings categories
        self._settings_tabs = CompactSettingsTabWidget()
        self._settings_tabs.setTabBar(ResponsiveIconTabBar(self._settings_tabs))
        self._settings_tabs.setTabPosition(QTabWidget.North)
        self._settings_tabs.setUsesScrollButtons(False)
        self._settings_tabs.tabBar().setExpanding(True)
        self._settings_tabs.tabBar().setElideMode(Qt.ElideNone)
        self._settings_tabs.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        self._settings_tabs.currentChanged.connect(lambda _index: QTimer.singleShot(0, self._settings_tabs.updateGeometry))
        self._settings_tabs.currentChanged.connect(self._update_settings_tab_nav_label)

        self._settings_tab_release_holds = dict(SETTINGS_TAB_RELEASE_HOLDS)
        self._settings_tab_specs = [
            spec for spec in SETTINGS_TAB_SPECS
            if spec[0] not in self._settings_tab_release_holds
        ]
        self._settings_tab_titles = [title for title, _icon_key, _color in self._settings_tab_specs]
        settings_pages = [
            self._build_connection_tab,
            self._build_master_profiles_tab,
            self._build_detection_tab,
            self._build_prompted_targets_tab,
            self._build_filter_tab,
            self._build_scoring_tab,
            self._build_engagement_tab,
            self._build_guard_tab,
            self._build_theme_tab,
            self._build_controls_tab,
            self._build_facial_recognition_tab,
            self._build_shortcut_keys_tab,
            self._build_ai_assistant_tab,
        ]
        for (title, _icon_key, _color), builder in zip(SETTINGS_TAB_SPECS, settings_pages):
            if title in self._settings_tab_release_holds:
                continue
            page = builder()
            index = self._settings_tabs.addTab(self._wrap_settings_tab(page), "")
            self._settings_tabs.setTabToolTip(index, title)
            self._settings_tabs.setTabWhatsThis(index, title)
        for index in range(self._settings_tabs.count()):
            page = self._settings_tabs.widget(index)
            if page is not None:
                page.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        self._apply_settings_tab_colors()
        self._update_settings_tab_nav_label(self._settings_tabs.currentIndex())

        panel_layout.addWidget(self._settings_tabs, stretch=1)

        right_panel = QWidget()
        self._right_panel = right_panel
        right_panel.setObjectName("sentryV2RightPane")
        right_panel.setMinimumWidth(SENTRY_V2_PANEL_MIN_WIDTH)
        right_panel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(6)
        right_layout.addLayout(panel_layout, stretch=1)

        pinned_bottom = QWidget()
        pinned_bottom.setObjectName("sentryV2PinnedBottom")
        pinned_bottom_layout = QHBoxLayout(pinned_bottom)
        pinned_bottom_layout.setContentsMargins(0, 0, 0, 0)
        pinned_bottom_layout.setSpacing(0)

        self._btn_save_config = QPushButton("SAVE SETTINGS")
        self._btn_save_config.setObjectName("sentryV2PinnedSave")
        self._btn_save_config.setMinimumHeight(36)
        self._btn_save_config.setMinimumWidth(0)
        self._btn_save_config.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self._set_button_role(self._btn_save_config, "primary")
        self._btn_save_config.clicked.connect(self._save_config)
        self._apply_tooltip(self._btn_save_config, "save_settings")
        pinned_bottom_layout.addWidget(self._btn_save_config)
        right_layout.addWidget(pinned_bottom)

        self._main_splitter.addWidget(right_panel)
        self._main_splitter.setStretchFactor(0, 5)
        self._main_splitter.setStretchFactor(1, 3)

        root.addWidget(self._main_splitter)

        QTimer.singleShot(0, self._apply_saved_layout_state)
        QTimer.singleShot(0, self._update_responsive_layout)
        QTimer.singleShot(0, self._reflow_all_responsive_button_grids)

        self._apply_all_tooltips()
        self._disable_wheel_scroll_on_all_inputs()


    def _apply_theme(self) -> None:
        tokens = self._theme_tokens()
        radius = tokens["radius"]
        radius_small = max(6, radius - 6)
        radius_medium = max(8, radius - 4)
        radius_large = radius + 4
        ui_scale = float(tokens.get("ui_scale", 1.0) or 1.0)
        base_font = tokens["base_font_pt"]
        hero_title = tokens["hero_title_pt"]
        hero_subtitle = tokens["hero_subtitle_pt"]
        hero_badge = tokens["hero_badge_pt"]
        nav_title = tokens["nav_title_pt"]
        nav_count = tokens["nav_count_pt"]
        status_font = tokens["status_font_pt"]
        group_margin_top = max(10, int(round(12 * ui_scale)))
        group_pad_top = max(10, int(round(12 * ui_scale)))
        group_pad_side = max(8, int(round(10 * ui_scale)))
        group_pad_bottom = max(8, int(round(10 * ui_scale)))
        title_left = max(8, int(round(10 * ui_scale)))
        title_pad_x = max(5, int(round(7 * ui_scale)))
        badge_pad_y = max(7, int(round(7 * ui_scale)))
        badge_pad_x = max(10, int(round(12 * ui_scale)))
        tab_pad_y = max(7, int(round(7 * ui_scale)))
        tab_pad_x = max(7, int(round(7 * ui_scale)))
        tab_min_h = max(42, int(round(44 * ui_scale)))
        button_pad_y = max(4, int(round(4 * ui_scale)))
        button_pad_x = max(7, int(round(7 * ui_scale)))
        button_min_h = max(23, int(round(21 * ui_scale)))
        preset_pad_y = max(4, int(round(4 * ui_scale)))
        preset_pad_x = max(6, int(round(6 * ui_scale)))
        preset_min_h = max(24, int(round(22 * ui_scale)))
        dpad_min_h = max(32, int(round(30 * ui_scale)))
        dpad_pad_y = max(5, int(round(4 * ui_scale)))
        dpad_pad_x = max(6, int(round(5 * ui_scale)))
        field_pad_y = max(5, int(round(4 * ui_scale)))
        field_pad_x = max(7, int(round(6 * ui_scale)))
        checkbox_spacing = max(8, int(round(8 * ui_scale)))
        checkbox_indicator = max(16, int(round(16 * ui_scale)))
        slider_handle = max(16, int(round(16 * ui_scale)))
        slider_margin = max(5, int(round(5 * ui_scale)))
        scroll_thickness = max(12, int(round(12 * ui_scale)))
        scroll_handle_min = max(24, int(round(24 * ui_scale)))
        stylesheet = f"""
QWidget#sentryV2Root {{
    background-color: transparent;
    color: {tokens['text']};
    font-family: "Segoe UI Variable Text", "Segoe UI";
    font-size: {base_font:.2f}pt;
}}
QWidget#sentryV2Root QLabel {{
    color: {tokens['muted']};
}}
QWidget#sentryV2Root QScrollArea,
QWidget#sentryV2Root QScrollArea > QWidget > QWidget {{
    background-color: transparent;
    border: none;
}}
QWidget#sentryV2Root QGroupBox {{
    background-color: {tokens['surface_rgba']};
    border: 1px solid {tokens['border']};
    border-radius: {radius_large}px;
    margin-top: {group_margin_top}px;
    padding: {group_pad_top}px {group_pad_side}px {group_pad_bottom}px {group_pad_side}px;
    font-weight: 600;
}}
QWidget#sentryV2Root QGroupBox::title {{
    subcontrol-origin: margin;
    left: {title_left}px;
    padding: 0 {title_pad_x}px;
    color: {tokens['accent']};
    font-size: {max(base_font, status_font + 0.2):.2f}pt;
    font-weight: 700;
}}
QWidget#sentryV2Root QWidget#sentryV2PinnedBottom,
QWidget#sentryV2Root QWidget#sentryV2PinnedTop {{
    background-color: transparent;
    border: none;
}}
QWidget#sentryV2Root QWidget#sentryV2LeftPane,
QWidget#sentryV2Root QWidget#sentryV2RightPane {{
    background-color: transparent;
    border: none;
}}
QWidget#sentryV2Root QFrame#sentryV2QuickAccess {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 {tokens['hero_start']},
        stop:0.45 {tokens['hero_mid']},
        stop:1 {tokens['surface_alt_rgba']});
    border: 1px solid {tokens['accent_soft']};
    border-radius: {radius_large}px;
}}
QWidget#sentryV2Root QFrame#sentryV2QuickAccess[drawerExpanded="true"] {{
    border-color: {tokens['accent']};
}}
QWidget#sentryV2Root QFrame#sentryV2QuickAccessHeader {{
    background-color: rgba(12, 10, 8, 0.18);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: {radius_medium + 2}px;
}}
QWidget#sentryV2Root QLabel#sentryV2QuickAccessTitle {{
    color: {tokens['hero_text']};
    font-family: "Segoe UI Variable Display", "Segoe UI Semibold", "Segoe UI";
    font-size: {max(base_font + 0.7, 10.6):.2f}pt;
    font-weight: 800;
}}
QWidget#sentryV2Root QLabel#sentryV2QuickAccessHint {{
    color: {tokens['hero_subtle']};
    font-size: {max(status_font + 0.1, 9.2):.2f}pt;
    font-weight: 600;
}}
QWidget#sentryV2Root QPushButton#sentryV2QuickAccessHandle {{
    background-color: rgba(255, 255, 255, 0.08);
    color: {tokens['hero_text']};
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: {radius_medium + 2}px;
    padding: 4px 12px;
    min-height: {max(button_min_h - 4, 28)}px;
    font-size: {max(base_font - 0.1, 9.4):.2f}pt;
    font-weight: 700;
}}
QWidget#sentryV2Root QPushButton#sentryV2QuickAccessHandle:hover {{
    background-color: {tokens['accent_faint']};
    border-color: {tokens['accent']};
}}
QWidget#sentryV2Root QPushButton[quickAccessChip="true"] {{
    border-radius: {radius_medium + 1}px;
    min-height: {max(button_min_h - 6, 28)}px;
    max-height: {max(button_min_h - 1, 32)}px;
    padding: {max(button_pad_y - 1, 3)}px {max(button_pad_x - 4, 8)}px;
    font-size: {max(base_font - 0.35, 9.2):.2f}pt;
    font-weight: 700;
}}
QWidget#sentryV2Root QSplitter {{
    background-color: transparent;
}}
QWidget#sentryV2Root QSplitter::handle {{
    background-color: transparent;
    border: none;
}}
QWidget#sentryV2Root QSplitter::handle:horizontal {{
    background-color: transparent;
    border: none;
    border-radius: 0;
    margin: 0;
}}
QWidget#sentryV2Root QSplitter::handle:vertical {{
    background-color: transparent;
    border: none;
    border-radius: 0;
    margin: 0;
}}
QWidget#sentryV2Root QFrame#sentryV3Hero {{
    background:qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 {tokens['hero_start']},
        stop:0.58 {tokens['hero_mid']},
        stop:1 {tokens['hero_end']});
    border: 1px solid {tokens['accent_soft']};
    border-radius: {radius_large + 2}px;
}}
QWidget#sentryV2Root QLabel#sentryV3HeroTitle {{
    color: {tokens['hero_text']};
    font-family: "Segoe UI Variable Display", "Segoe UI Semibold", "Segoe UI";
    font-size: {hero_title:.2f}pt;
    font-weight: 800;
}}
QWidget#sentryV2Root QLabel#sentryV3HeroSubtitle {{
    color: {tokens['hero_subtle']};
    font-family: "Segoe UI Variable Text", "Segoe UI";
    font-size: {hero_subtitle:.2f}pt;
    font-weight: 600;
}}
QWidget#sentryV2Root QLabel#sentryV3HeroBadge {{
    background-color: {tokens['hero_badge_bg']};
    color: {tokens['hero_badge_text']};
    border: 1px solid {tokens['accent_soft']};
    border-radius: {radius_medium + 4}px;
    padding: {badge_pad_y}px {badge_pad_x}px;
    font-size: {hero_badge:.2f}pt;
    font-weight: 800;
}}
QWidget#sentryV2Root QPushButton#sentryV2PinnedSave {{
    min-height: {max(button_min_h + 6, 36)}px;
    min-width: 0px;
    font-size: {max(base_font + 0.8, 10.8):.2f}pt;
    font-weight: 800;
}}
QWidget#sentryV2Root QWidget#sentryV2TabsNav {{
    background-color: {tokens['surface_alt_rgba']};
    border: 1px solid {tokens['border']};
    border-radius: {radius_medium + 2}px;
    padding: 4px 7px;
}}
QWidget#sentryV2Root QLabel#sentryV2TabsNavTitle {{
    color: {tokens['hero_text']};
    font-family: "Segoe UI Variable Display", "Segoe UI Semibold", "Segoe UI";
    font-size: {nav_title:.2f}pt;
    font-weight: 700;
}}
QWidget#sentryV2Root QLabel#sentryV2TabsNavCount {{
    color: {tokens['accent']};
    font-family: "Segoe UI Variable Display", "Segoe UI Semibold", "Segoe UI";
    font-size: {nav_count:.2f}pt;
    font-weight: 700;
    padding-left: 8px;
}}
QWidget#sentryV2Root QWidget#sentryV2ToggleRow {{
    background-color: {tokens['surface_alt_rgba']};
    border: 1px solid {tokens['border']};
    border-radius: {radius_medium + 2}px;
}}
QWidget#sentryV2Root QWidget#sentryV2PinnedBottom QGroupBox {{
    margin-top: 8px;
    padding: 12px 10px 10px 10px;
}}
QWidget#sentryV2Root QWidget#sentryV2PinnedBottom QLabel {{
    color: {tokens['muted']};
}}
QWidget#sentryV2Root QTabWidget::pane {{
    background-color: {tokens['panel_rgba']};
    border: 1px solid {tokens['border']};
    border-radius: {radius_large}px;
    top: -1px;
}}
QWidget#sentryV2Root QTabBar::tab {{
    background-color: {tokens['surface_alt_rgba']};
    border: 1px solid {tokens['border']};
    border-radius: {radius_medium}px;
    padding: {tab_pad_y}px {tab_pad_x}px;
    min-height: {tab_min_h}px;
    min-width: 0px;
}}
QWidget#sentryV2Root QTabBar::tab:left {{
    min-width: 46px;
    max-width: 54px;
    margin-bottom: 4px;
}}
QWidget#sentryV2Root QTabBar::tab:top {{
    border-bottom: none;
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
    min-width: 0px;
    min-height: 60px;
    margin-right: 3px;
}}
QWidget#sentryV2Root QTabBar::tab:selected {{
    background-color: {tokens['accent_mid']};
    border-color: {tokens['accent']};
    color: {tokens['hero_text']};
}}
QWidget#sentryV2Root QTabBar::tab:selected:left {{
    border-left: 4px solid {tokens['accent']};
}}
QWidget#sentryV2Root QTabBar::tab:hover:!selected {{
    background-color: {tokens['accent_faint']};
    color: {tokens['hero_text']};
}}
QWidget#sentryV2Root QPushButton {{
    background-color: {tokens['button_bg']};
    color: {tokens['button_text']};
    border: 1px solid {tokens['button_border']};
    border-radius: {radius_medium}px;
    padding: {button_pad_y}px {button_pad_x}px;
    min-height: {button_min_h}px;
}}
QWidget#sentryV2Root QPushButton:hover {{
    background-color: {tokens['button_hover']};
    border-color: {tokens['accent']};
}}
QWidget#sentryV2Root QPushButton:pressed {{
    background-color: {tokens['button_pressed']};
}}
QWidget#sentryV2Root QPushButton:checked {{
    background-color: {tokens['button_checked']};
    border-color: {tokens['accent']};
    color: {tokens['hero_text']};
}}
QWidget#sentryV2Root QPushButton:disabled {{
    background-color: {tokens['button_disabled']};
    color: {tokens['disabled_text']};
    border-color: {tokens['disabled_border']};
}}
QWidget#sentryV2Root QPushButton[buttonRole="primary"] {{
    background-color: {tokens['primary_button_bg']};
    border-color: {tokens['primary_button_border']};
    color: {tokens['hero_text']};
    font-weight: 700;
}}
QWidget#sentryV2Root QPushButton[buttonRole="primary"]:hover {{
    background-color: {tokens['primary_button_hover']};
    border-color: {tokens['accent']};
}}
QWidget#sentryV2Root QPushButton[buttonRole="primary"]:pressed {{
    background-color: {tokens['primary_button_pressed']};
}}
QWidget#sentryV2Root QPushButton[buttonRole="preset"] {{
    background-color: {tokens['surface_alt_rgba']};
    border-color: {tokens['button_border']};
    color: {tokens['button_text']};
    font-weight: 600;
    padding: {preset_pad_y}px {preset_pad_x}px;
    min-height: {preset_min_h}px;
}}
QWidget#sentryV2Root QPushButton[buttonRole="preset"]:hover {{
    background-color: {tokens['button_hover']};
    border-color: {tokens['accent']};
}}
QWidget#sentryV2Root QPushButton[buttonRole="utility"] {{
    background-color: {tokens['surface_alt_rgba']};
    border-color: {tokens['button_border']};
    color: {tokens['button_text']};
}}
QWidget#sentryV2Root QPushButton[buttonRole="utility"]:hover {{
    background-color: {tokens['button_hover']};
    border-color: {tokens['accent']};
}}
QWidget#sentryV2Root QPushButton[buttonRole="dpad"] {{
    background-color: {tokens['accent_mid']};
    border: 1px solid {tokens['accent']};
    border-radius: {radius_medium + 2}px;
    color: {tokens['hero_text']};
    font-weight: 700;
    font-size: {base_font:.2f}pt;
    min-height: {dpad_min_h}px;
    padding: {dpad_pad_y}px {dpad_pad_x}px;
}}
QWidget#sentryV2Root QPushButton[buttonRole="dpad"]:hover {{
    background-color: {tokens['primary_button_hover']};
    border-color: {tokens['accent']};
}}
QWidget#sentryV2Root QPushButton[buttonRole="dpad"]:pressed {{
    background-color: {tokens['primary_button_pressed']};
    border-color: {tokens['accent_soft']};
}}
QWidget#sentryV2Root QPushButton[buttonRole="dpadArrow"] {{
    background-color: {tokens['accent_faint']};
    border: 1px solid {tokens['accent_soft']};
    border-radius: {radius_medium + 2}px;
    color: {tokens['hero_text']};
    font-weight: 800;
    font-size: {max(base_font + 3.2, 14.0):.2f}pt;
    min-height: {max(dpad_min_h - 8, 26)}px;
    padding: {max(dpad_pad_y - 2, 2)}px {max(dpad_pad_x - 3, 5)}px;
}}
QWidget#sentryV2Root QPushButton[buttonRole="dpadArrow"]:hover {{
    background-color: {tokens['accent_mid']};
    border-color: {tokens['accent']};
}}
QWidget#sentryV2Root QPushButton[buttonRole="dpadArrow"]:pressed {{
    background-color: {tokens['primary_button_pressed']};
    border-color: {tokens['accent_soft']};
}}
QWidget#sentryV2Root QPushButton[buttonRole="mode"] {{
    background-color: {tokens['mode_button_bg']};
    border-color: {tokens['mode_button_border']};
    color: {tokens['mode_button_text']};
    font-weight: 600;
}}
QWidget#sentryV2Root QPushButton[buttonRole="mode"]:hover {{
    background-color: {tokens['mode_button_hover']};
    border-color: {tokens['accent']};
}}
QWidget#sentryV2Root QPushButton[buttonRole="danger"] {{
    background-color: {tokens['danger_button_bg']};
    border-color: {tokens['danger_button_border']};
    color: {tokens['hero_text']};
    font-weight: 700;
}}
QWidget#sentryV2Root QPushButton[buttonRole="danger"]:hover {{
    background-color: {tokens['danger_button_hover']};
    border-color: {tokens['danger_button_border']};
}}
QWidget#sentryV2Root QPushButton[buttonRole="danger"]:pressed {{
    background-color: {tokens['danger_button_pressed']};
}}
QWidget#sentryV2Root QLineEdit,
QWidget#sentryV2Root QComboBox,
QWidget#sentryV2Root QSpinBox,
QWidget#sentryV2Root QDoubleSpinBox,
QWidget#sentryV2Root QListWidget,
QWidget#sentryV2Root QTextEdit {{
    background-color: {tokens['field_rgba']};
    color: {tokens['field_text']};
    border: 1px solid {tokens['field_border']};
    border-radius: {radius_small}px;
    padding: {field_pad_y}px {field_pad_x}px;
    selection-background-color: {tokens['accent_mid']};
    selection-color: {tokens['hero_text']};
}}
QWidget#sentryV2Root QLineEdit:focus,
QWidget#sentryV2Root QComboBox:focus,
QWidget#sentryV2Root QSpinBox:focus,
QWidget#sentryV2Root QDoubleSpinBox:focus,
QWidget#sentryV2Root QListWidget:focus,
QWidget#sentryV2Root QTextEdit:focus {{
    border-color: {tokens['accent']};
}}
QWidget#sentryV2Root QComboBox::drop-down {{
    border: none;
    width: 22px;
}}
QWidget#sentryV2Root QAbstractItemView {{
    background-color: {tokens['panel_rgba']};
    color: {tokens['field_text']};
    border: 1px solid {tokens['field_border']};
    selection-background-color: {tokens['accent_mid']};
}}
QWidget#sentryV2Root QCheckBox {{
    color: {tokens['text']};
    spacing: {checkbox_spacing}px;
}}
QWidget#sentryV2Root QCheckBox:disabled {{
    color: {tokens['disabled_text']};
}}
QWidget#sentryV2Root QCheckBox::indicator {{
    width: {checkbox_indicator}px;
    height: {checkbox_indicator}px;
    border-radius: 4px;
    border: 1px solid {tokens['field_border']};
    background-color: {tokens['field_rgba']};
}}
QWidget#sentryV2Root QCheckBox::indicator:checked {{
    background-color: {tokens['accent']};
    border-color: {tokens['accent']};
}}
QWidget#sentryV2Root QSlider::groove:horizontal {{
    height: 6px;
    border-radius: 3px;
    background-color: {tokens['slider_groove']};
}}
QWidget#sentryV2Root QSlider::handle:horizontal {{
    width: {slider_handle}px;
    margin: -{slider_margin}px 0;
    border-radius: 8px;
    background-color: {tokens['accent']};
    border: 1px solid {tokens['accent_soft']};
}}
QWidget#sentryV2Root QScrollBar:vertical {{
    background-color: transparent;
    width: {scroll_thickness}px;
    margin: 2px;
}}
QWidget#sentryV2Root QScrollBar::handle:vertical {{
    background-color: {tokens['scroll_handle']};
    border-radius: 6px;
    min-height: {scroll_handle_min}px;
}}
QWidget#sentryV2Root QScrollBar:horizontal {{
    background-color: transparent;
    height: {scroll_thickness}px;
    margin: 2px;
}}
QWidget#sentryV2Root QScrollBar::handle:horizontal {{
    background-color: {tokens['scroll_handle']};
    border-radius: 6px;
    min-width: {scroll_handle_min}px;
}}
QWidget#sentryV2Root QScrollBar::add-line,
QWidget#sentryV2Root QScrollBar::sub-line,
QWidget#sentryV2Root QScrollBar::add-page,
QWidget#sentryV2Root QScrollBar::sub-page {{
    background: none;
    border: none;
}}
QLabel#sentryV2Video {{
    background-color: {tokens['video_bg_rgba']};
    color: {tokens['video_text']};
    border: 1px solid {tokens['border']};
    border-radius: 0px;
}}
QTextEdit#sentryV2Log {{
    background-color: {tokens['panel_rgba']};
    border: 1px solid {tokens['border']};
    border-radius: {radius_medium}px;
    padding: 6px 8px;
    font-family: "Consolas", "Cascadia Mono", "Courier New", monospace;
    font-size: {max(10.0, base_font - 0.2):.2f}pt;
    line-height: 1.35;
}}
QWidget#sentryV2Root QLabel[themeRole="subtle"] {{
    color: {tokens['subtle_text']};
    font-size: {max(status_font + 0.2, base_font - 0.1):.2f}pt;
}}
QWidget#sentryV2Root QLabel[themeRole="subtleBody"] {{
    color: {tokens['subtle_text']};
    font-size: {max(base_font + 0.1, 10.0):.2f}pt;
}}
QWidget#sentryV2Root QLabel[themeRole="mutedCompact"] {{
    color: {tokens['muted']};
    font-size: {max(status_font + 0.1, 9.8):.2f}pt;
}}
QWidget#sentryV2Root QLabel[themeRole="sectionPadded"] {{
    color: {tokens['accent']};
    font-weight: 700;
    padding-top: 4px;
}}
QWidget#sentryV2Root QLabel[themeRole="summary"] {{
    color: {tokens['text']};
    font-size: {max(base_font + 0.2, 10.2):.2f}pt;
}}
QWidget#sentryV2Root QLabel[themeRole="statusMeta"] {{
    color: {tokens['status_meta']};
    font-size: {status_font:.2f}pt;
}}
QWidget#sentryV2Root QLabel[themeRole="statusStrong"] {{
    color: {tokens['status_neutral']};
    font-weight: bold;
    font-size: {max(status_font + 0.3, 10.2):.2f}pt;
}}
QWidget#sentryV2Root QLabel[themeRole="compactValue"] {{
    color: {tokens['text']};
    font-weight: 700;
    font-size: {max(status_font + 0.4, 10.2):.2f}pt;
}}
QWidget#sentryV2Root QLabel[themeRole="value"] {{
    color: {tokens['text']};
    font-weight: 700;
    font-size: {max(base_font + 0.2, 10.2):.2f}pt;
}}
QWidget#sentryV2Root QLabel[themeRole="section"] {{
    color: {tokens['accent']};
    font-weight: 700;
    font-size: {max(base_font + 0.5, 10.6):.2f}pt;
}}
QWidget#sentryV2Root QCheckBox[themeRole="headlineToggle"] {{
    color: {tokens['text']};
    font-weight: 700;
    font-size: {max(base_font + 0.4, 10.6):.2f}pt;
}}
"""
        self.setStyleSheet(stylesheet)
        self._apply_status_panel_theme()
        self._apply_settings_tab_colors()
        self._update_responsive_layout()
        self._sync_camera_status_style()
        self._sync_connection_status_style()
        self._sync_auto_trigger_checkbox_style()

        window = self.window()
        if window is not None and getattr(window, "sentry_v2_tab", None) is self:
            try:
                window_radius = max(6, radius - 6)
                window.setStyleSheet(
                    f"QMainWindow {{ background-color: transparent; color: {tokens['text']}; }}"
                    f"QWidget#smartSentryWindowRoot {{ background-color: {tokens['root_bg_rgba']}; color: {tokens['text']}; border: 1px solid {tokens['border']}; border-radius: {radius_large}px; }}"
                    f"QWidget#smartSentryWindowControls {{ background-color: {tokens['surface_alt_rgba']}; border-bottom: 1px solid {tokens['border']}; border-top-left-radius: {radius_large}px; border-top-right-radius: {radius_large}px; }}"
                    f"QWidget#smartSentryWindowControls QPushButton {{ min-width: 28px; max-width: 28px; min-height: 24px; max-height: 24px; background-color: {tokens['button_bg']}; color: {tokens['button_text']}; border: 1px solid {tokens['button_border']}; border-radius: {window_radius}px; }}"
                    f"QWidget#smartSentryWindowControls QPushButton:hover {{ background-color: {tokens['button_hover']}; border-color: {tokens['accent']}; }}"
                    f"QWidget#smartSentryWindowControls QPushButton:pressed {{ background-color: {tokens['button_pressed']}; border-color: {tokens['accent_soft']}; }}"
                    f"QToolTip {{ background-color: {tokens['tooltip_bg']}; color: {tokens['tooltip_text']}; border: 1px solid {tokens['accent_soft']}; padding: 4px 6px; }}"
                )
                window.setWindowOpacity(max(0.7, min(1.0, tokens["window_opacity"] / 100.0)))
            except Exception:
                pass
        if hasattr(self, "_status_timer"):
            try:
                self._refresh_status()
            except Exception:
                pass

    def _apply_settings_tab_colors(self) -> None:
        if not hasattr(self, "_settings_tabs") or self._settings_tabs is None:
            return
        tab_bar = self._settings_tabs.tabBar()
        if hasattr(tab_bar, "_sync_icon_size"):
            try:
                tab_bar._sync_icon_size()
            except Exception:
                pass
        else:
            tab_bar.setIconSize(QSize(24, 24))
        tokens = self._theme_tokens()
        for idx, (_title, icon_key, color_value) in enumerate(getattr(self, "_settings_tab_specs", SETTINGS_TAB_SPECS)):
            if idx < tab_bar.count():
                resolved_color = tokens["accent"] if color_value == "accent" else color_value
                tab_bar.setTabTextColor(idx, QColor(resolved_color))
                tab_bar.setTabIcon(idx, _build_settings_tab_icon(icon_key, resolved_color, max(24, tab_bar.iconSize().width() or 24)))

    def _update_settings_tab_nav_label(self, index: int) -> None:
        if not hasattr(self, "_settings_tabs") or self._settings_tabs is None:
            return
        count = self._settings_tabs.count()
        if count <= 0:
            label_text = ""
        else:
            safe_index = max(0, min(int(index), count - 1))
            tab_titles = getattr(self, "_settings_tab_titles", [])
            tab_title = tab_titles[safe_index] if safe_index < len(tab_titles) else self._settings_tabs.tabToolTip(safe_index)
            nav_title = SETTINGS_TAB_NAV_LABELS.get(str(tab_title), str(tab_title).upper())
            label_text = f"{safe_index + 1}/{count} {nav_title}"
        if hasattr(self, "_settings_nav_label") and self._settings_nav_label is not None:
            self._settings_nav_label.setText(label_text)
        enabled_count = sum(1 for tab_index in range(count) if self._settings_tabs.isTabEnabled(tab_index)) if count > 0 else 0
        can_navigate = enabled_count > 1
        if hasattr(self, "_btn_prev_settings_tab") and self._btn_prev_settings_tab is not None:
            self._btn_prev_settings_tab.setEnabled(can_navigate)
        if hasattr(self, "_btn_next_settings_tab") and self._btn_next_settings_tab is not None:
            self._btn_next_settings_tab.setEnabled(can_navigate)

    def _find_navigable_settings_tab(self, start_index: int, step: int) -> int:
        if not hasattr(self, "_settings_tabs") or self._settings_tabs is None:
            return start_index
        count = self._settings_tabs.count()
        if count <= 0:
            return start_index
        for offset in range(1, count + 1):
            candidate = (start_index + (step * offset)) % count
            if self._settings_tabs.isTabEnabled(candidate):
                return candidate
        return start_index

    def _select_previous_settings_tab(self) -> None:
        if not hasattr(self, "_settings_tabs") or self._settings_tabs is None:
            return
        count = self._settings_tabs.count()
        if count <= 1:
            return
        self._settings_tabs.setCurrentIndex(self._find_navigable_settings_tab(self._settings_tabs.currentIndex(), -1))

    def _select_next_settings_tab(self) -> None:
        if not hasattr(self, "_settings_tabs") or self._settings_tabs is None:
            return
        count = self._settings_tabs.count()
        if count <= 1:
            return
        self._settings_tabs.setCurrentIndex(self._find_navigable_settings_tab(self._settings_tabs.currentIndex(), 1))

    def _wrap_settings_tab(self, content: QWidget) -> QScrollArea:
        content.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        scroll = QScrollArea()
        scroll.setFrameShape(QFrame.NoFrame)
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setMinimumHeight(0)
        scroll.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        scroll.setWidget(content)
        return scroll

    def _disable_wheel_scroll(self, widget: QWidget) -> None:
        """Disable mouse wheel scrolling on spinboxes, sliders, and comboboxes."""
        wheel_filter = NoWheelScrollFilter()
        widget.installEventFilter(wheel_filter)

    def _disable_wheel_scroll_on_all_inputs(self) -> None:
        """Recursively disable wheel scroll on all spinboxes, sliders, and comboboxes in the widget tree."""
        def disable_recursive(widget: QWidget) -> None:
            # Apply filter to this widget if it's a numeric input type
            if isinstance(widget, (QSpinBox, QDoubleSpinBox, QSlider, QComboBox)):
                self._disable_wheel_scroll(widget)
            
            # Recursively process children
            for child in widget.findChildren(QWidget):
                if isinstance(child, (QSpinBox, QDoubleSpinBox, QSlider, QComboBox)):
                    self._disable_wheel_scroll(child)
        
        disable_recursive(self)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self._update_responsive_layout()

    def showEvent(self, event) -> None:
        super().showEvent(event)
        if not self._layout_restore_complete:
            QTimer.singleShot(0, self._apply_saved_layout_state)

    def _on_main_splitter_moved(self, _pos: int, _index: int) -> None:
        self._capture_layout_state()
        self._save_config_quietly()
        self._update_responsive_layout()

    def _on_layout_splitter_moved(self, _pos: int, _index: int) -> None:
        self._capture_layout_state()
        self._save_config_quietly()

    def _on_bottom_info_splitter_moved(self, _pos: int, _index: int) -> None:
        self._capture_layout_state()
        self._save_config_quietly()

    def _sync_settings_panel_width(self) -> None:
        return

    def _sync_settings_tab_bar_metrics(self) -> None:
        if not hasattr(self, "_settings_tabs") or self._settings_tabs is None:
            return
        tab_bar = self._settings_tabs.tabBar()
        if tab_bar is None:
            return
        count = max(1, self._settings_tabs.count())
        metrics = self._responsive_panel_metrics()
        available_width = max(260, min(int(metrics["panel_width"]) - 18, tab_bar.width() or self._settings_tabs.width() or self.width()))
        per_tab_width = max(28.0, float(available_width) / float(count))
        icon_px = _clamp_int_range(per_tab_width * 0.48, 20, 38)
        bar_height = _clamp_int_range(per_tab_width * 0.80, int(metrics["tab_bar_height_min"]), int(metrics["tab_bar_height_max"]))
        tab_bar.setIconSize(QSize(icon_px, icon_px))
        tab_bar.setMinimumHeight(bar_height)
        tab_bar.setMaximumHeight(bar_height)
        tab_bar.updateGeometry()

    def _settings_panel_width(self) -> int:
        panel_width = 0
        if self._right_panel is not None:
            panel_width = self._right_panel.width()
        if panel_width <= 0 and hasattr(self, "_main_splitter"):
            sizes = self._main_splitter.sizes()
            if len(sizes) > 1:
                panel_width = int(sizes[1])
        if panel_width <= 0 and hasattr(self, "_settings_tabs"):
            panel_width = self._settings_tabs.width()
        if panel_width <= 0:
            panel_width = SENTRY_V2_PANEL_DEFAULT_WIDTH
        return max(SENTRY_V2_PANEL_MIN_WIDTH, int(panel_width))

    def _responsive_panel_metrics(self) -> dict[str, int | bool]:
        panel_width = self._settings_panel_width()
        panel_height = self.height() if self.height() > 0 else 880
        compact = panel_width < 500
        dense = panel_width < 620
        nav_button = _clamp_int_range(panel_width * 0.082, 34, 52)
        nav_button_height = _clamp_int_range(nav_button * 0.74, 26, 38)
        manual_button_width = _clamp_int_range((panel_width - 86) / 5.0, 58, 94)
        manual_button_height = _clamp_int_range(manual_button_width * 0.50, 32, 44)
        list_height = _clamp_int_range(panel_height * 0.18, 112, 220)
        waypoint_height = _clamp_int_range(panel_height * 0.12, 88, 150)
        mask_height = _clamp_int_range(panel_height * 0.14, 96, 176)
        return {
            "panel_width": panel_width,
            "panel_height": panel_height,
            "compact": compact,
            "dense": dense,
            "nav_button": nav_button,
            "nav_button_height": nav_button_height,
            "nav_spacing": 5 if compact else 8,
            "nav_margin_x": 8 if compact else 12,
            "tab_bar_height_min": 42 if compact else 46,
            "tab_bar_height_max": 60 if compact else 72,
            "manual_button_width": manual_button_width,
            "manual_button_height": manual_button_height,
            "class_list_height": list_height,
            "waypoint_list_height": waypoint_height,
            "mask_list_height": mask_height,
        }

    def _update_settings_nav_controls(self) -> None:
        metrics = self._responsive_panel_metrics()
        button_width = int(metrics["nav_button"])
        button_height = int(metrics["nav_button_height"])
        if self._tabs_nav_layout is not None:
            left_margin = int(metrics["nav_margin_x"])
            right_margin = 6
            self._tabs_nav_layout.setContentsMargins(left_margin, right_margin, right_margin, right_margin)
            self._tabs_nav_layout.setSpacing(int(metrics["nav_spacing"]))
        if self._tabs_nav_title_label is not None:
            self._tabs_nav_title_label.setText("")
            self._tabs_nav_title_label.setVisible(False)
        for button in (getattr(self, "_btn_prev_settings_tab", None), getattr(self, "_btn_next_settings_tab", None)):
            if button is None:
                continue
            button.setMinimumSize(28, 26)
            button.setMaximumSize(56, 38)
            button.setFixedSize(button_width, button_height)

    def _update_manual_control_button_sizes(self) -> None:
        if not self._manual_control_buttons:
            return
        metrics = self._responsive_panel_metrics()
        button_w = int(metrics["manual_button_width"])
        button_h = int(metrics["manual_button_height"])
        for button in self._manual_control_buttons:
            button.setFixedSize(button_w, button_h)

    def _update_responsive_header_metrics(self) -> None:
        title_label = getattr(self, "_hero_title_label", None)
        subtitle_label = getattr(self, "_hero_subtitle_label", None)
        badge_label = getattr(self, "_hero_badge_label", None)
        wake_button = getattr(self, "_btn_header_wake", None)
        rest_button = getattr(self, "_btn_header_rest", None)
        if any(widget is None for widget in (title_label, subtitle_label, badge_label, wake_button, rest_button)):
            return

        metrics = self._responsive_panel_metrics()
        panel_width = int(metrics["panel_width"])
        compact = bool(metrics["compact"])
        width_ratio = max(0.0, min(1.0, (panel_width - 340.0) / 260.0))
        tokens = self._theme_tokens()

        title_scale = 0.80 + (0.24 * width_ratio)
        subtitle_scale = 0.84 + (0.18 * width_ratio)
        badge_scale = 0.86 + (0.14 * width_ratio)
        button_scale = 0.80 + (0.20 * width_ratio)

        title_pt = max(16.0, float(tokens["hero_title_pt"]) * title_scale)
        subtitle_pt = max(10.4, float(tokens["hero_subtitle_pt"]) * subtitle_scale)
        badge_pt = max(9.6, float(tokens["hero_badge_pt"]) * badge_scale)
        button_pt = max(9.2, float(tokens["base_font_pt"]) * button_scale)
        button_width = _clamp_int_range(panel_width * 0.28, 94, 148)
        button_height = _clamp_int_range(button_width * 0.38, 32, 40)

        title_label.setStyleSheet(f"font-size: {title_pt:.2f}pt;")
        subtitle_label.setStyleSheet(f"font-size: {subtitle_pt:.2f}pt;")
        badge_label.setStyleSheet(f"font-size: {badge_pt:.2f}pt;")
        badge_label.setVisible(bool(badge_label.text().strip()))

        for button in (wake_button, rest_button):
            button.setMinimumWidth(0)
            button.setFixedSize(button_width, button_height)
            button.setStyleSheet(f"font-size: {button_pt:.2f}pt; font-weight: 700;")

        if self._hero_layout is not None:
            hero_margin_x = 12 if compact else 18
            hero_margin_y = 12 if compact else 14
            self._hero_layout.setContentsMargins(hero_margin_x, hero_margin_y, hero_margin_x, hero_margin_y)
            self._hero_layout.setSpacing(10 if compact else 14)
        if self._hero_actions_layout is not None:
            self._hero_actions_layout.setSpacing(6 if compact else 8)
        if self._hero_action_row is not None:
            self._hero_action_row.setSpacing(6 if compact else 8)

    def _register_responsive_list(self, widget: Optional[QListWidget], role: str) -> None:
        if widget is None:
            return
        entry = (widget, role)
        if entry not in self._responsive_lists:
            self._responsive_lists.append(entry)

    def _register_responsive_label(self, widget: Optional[QLabel], role: str) -> None:
        if widget is None:
            return
        entry = (widget, role)
        if entry not in self._responsive_labels:
            self._responsive_labels.append(entry)

    def _register_responsive_box_layout(self, layout: Optional[QBoxLayout], role: str) -> None:
        if layout is None:
            return
        entry = (layout, role)
        if entry not in self._responsive_box_layouts:
            self._responsive_box_layouts.append(entry)

    def _update_responsive_lists(self) -> None:
        if not self._responsive_lists:
            return
        metrics = self._responsive_panel_metrics()
        height_map = {
            "allowed_classes": int(metrics["class_list_height"]),
            "waypoint_list": int(metrics["waypoint_list_height"]),
            "mask_list": int(metrics["mask_list_height"]),
        }
        for widget, role in self._responsive_lists:
            max_height = height_map.get(role)
            if max_height is not None:
                widget.setMaximumHeight(max_height)

    def _update_responsive_labels(self) -> None:
        if not self._responsive_labels:
            return
        panel_width = int(self._responsive_panel_metrics()["panel_width"])
        width_map = {
            "weight_label": _clamp_int_range(panel_width * 0.23, 90, 132),
            "weight_value": _clamp_int_range(panel_width * 0.08, 34, 48),
            "zoom_value": _clamp_int_range(panel_width * 0.10, 42, 60),
        }
        for widget, role in self._responsive_labels:
            width = width_map.get(role)
            if width is None:
                continue
            widget.setMinimumWidth(width)
            widget.setMaximumWidth(width)

    def _update_responsive_box_layouts(self) -> None:
        if not self._responsive_box_layouts:
            return
        panel_width = int(self._responsive_panel_metrics()["panel_width"])
        threshold_map = {
            "dense_row": 560,
            "compact_row": 500,
            "action_row": 460,
        }
        for layout, role in self._responsive_box_layouts:
            threshold = threshold_map.get(role, 500)
            direction = QBoxLayout.TopToBottom if panel_width < threshold else QBoxLayout.LeftToRight
            if layout.direction() != direction:
                layout.setDirection(direction)

    def _update_responsive_layout(self) -> None:
        self._sync_settings_tab_bar_metrics()
        self._update_responsive_header_metrics()
        self._update_settings_nav_controls()
        self._update_manual_control_button_sizes()
        self._update_responsive_lists()
        self._update_responsive_labels()
        self._update_responsive_box_layouts()
        self._reflow_all_responsive_button_grids()

    def _set_theme_role(self, widget: Optional[QWidget], role: str) -> None:
        if widget is None:
            return
        widget.setProperty("themeRole", role)
        widget.style().unpolish(widget)
        widget.style().polish(widget)
        widget.update()

    def _set_button_role(self, button: Optional[QPushButton], role: str) -> None:
        if button is None:
            return
        button.setProperty("buttonRole", role)
        button.style().unpolish(button)
        button.style().polish(button)
        button.update()

    def _style_button_row(self, buttons: list[QPushButton], role: str = "utility") -> None:
        for button in buttons:
            self._set_button_role(button, role)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    def _compact_combo_box(self, combo: Optional[QComboBox], minimum_chars: int = 14) -> None:
        if combo is None:
            return
        combo.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        combo.setMinimumContentsLength(max(6, minimum_chars))
        combo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    def _responsive_button_grid_columns(self, grid: QGridLayout, button_count: int) -> int:
        parent = grid.parentWidget()
        available_width = parent.width() if parent is not None else SENTRY_V2_PANEL_MIN_WIDTH
        if available_width <= 0:
            available_width = SENTRY_V2_PANEL_MIN_WIDTH
        if button_count <= 1:
            return 1
        if available_width < 420:
            return 1
        if available_width < 680 or button_count <= 4:
            return 2
        return 3

    def _register_responsive_button_grid(self, grid: QGridLayout) -> None:
        if grid not in self._responsive_button_grids:
            self._responsive_button_grids.append(grid)

    def _reflow_responsive_button_grid(self, grid: QGridLayout) -> None:
        buttons: List[QPushButton] = []
        while grid.count():
            item = grid.takeAt(0)
            widget = item.widget() if item is not None else None
            if isinstance(widget, QPushButton):
                buttons.append(widget)
        if not buttons:
            return

        columns = self._responsive_button_grid_columns(grid, len(buttons))
        for column in range(3):
            grid.setColumnStretch(column, 0)

        if columns == 1:
            grid.setColumnStretch(0, 1)
            grid.setColumnStretch(1, 2)
            grid.setColumnStretch(2, 1)
            for index, button in enumerate(buttons):
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                grid.addWidget(button, index, 1)
            return

        for index, button in enumerate(buttons):
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            grid.addWidget(button, index // columns, index % columns)
        for column in range(columns):
            grid.setColumnStretch(column, 1)

    def _reflow_all_responsive_button_grids(self) -> None:
        for grid in list(self._responsive_button_grids):
            self._reflow_responsive_button_grid(grid)

    def _normalize_preset_grid_button_widths(self, grid: QGridLayout) -> None:
        """Make preset buttons responsive to the available panel width."""
        for i in range(grid.count()):
            item = grid.itemAt(i)
            widget = item.widget() if item is not None else None
            if isinstance(widget, QPushButton):
                self._set_button_role(widget, "preset")
                widget.setMinimumHeight(30)
                widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self._register_responsive_button_grid(grid)
        self._reflow_responsive_button_grid(grid)

    def _apply_tooltip(self, widget: QWidget | None, key: str) -> None:
        """Apply a predefined tooltip to a widget if both exist."""
        try:
            if widget is None:
                return
            text = SENTRY_V2_TOOLTIPS.get(key, "")
            if text and hasattr(widget, "setToolTip"):
                widget.setToolTip(text)
        except Exception:
            pass

    def _apply_all_tooltips(self) -> None:
        """Apply Smart Sentry tooltips after the full UI has been constructed."""
        widget_map = {
            self._chk_enable: "enable_sentry",
            self._edit_cam_source: "camera_source",
            self._combo_cam_resolution: "camera_width",
            self._btn_cam: "camera_toggle",
            self._combo_conn_type: "connection_mode",
            self._edit_esp32_port: "esp32_port",
            self._combo_esp32_ports: "esp32_port_list",
            self._spin_esp32_baud: "esp32_baud",
            self._edit_debug_port: "debug_port",
            self._combo_debug_ports: "debug_port_list",
            self._spin_debug_baud: "debug_baud",
            self._spin_pan_id: "pan_servo_id",
            self._spin_tilt_id: "tilt_servo_id",
            self._spin_servo_time: "servo_move_time",
            self._edit_udp_host: "udp_host",
            self._spin_udp_port: "udp_port",
            self._chk_invert_pan: "invert_pan",
            self._chk_invert_tilt: "invert_tilt",
            self._btn_connect: "connect_toggle",
            self._combo_detection_mode: "detection_mode",
            self._spin_min_contour: "min_contour_area",
            self._spin_max_contour: "max_contour_area",
            self._combo_yolo_model: "yolo_model",
            self._edit_yolo_classes: "yolo_classes",
            self._spin_yolo_conf: "yolo_confidence",
            self._spin_yolo_min_area: "yolo_min_area",
            self._combo_color_preset: "color_preset",
            self._spin_color_min: "color_min_area",
            self._spin_color_max: "color_max_area",
            self._combo_fusion: "fusion_strategy",
            self._spin_fusion_overlap: "fusion_overlap",
            self._spin_motion_thresh: "motion_gate_threshold",
            self._spin_motion_ignore: "motion_ignore_after_move_s",
            self._class_list: "allowed_classes",
            self._spin_min_conf: "min_confidence",
            self._spin_min_size: "min_size",
            self._spin_max_size: "max_size",
            self._chk_ml: "ml_refinement",
            self._chk_auto_trigger: "auto_trigger",
            self._combo_trigger_mode: "trigger_mode",
            self._spin_min_threat: "min_threat",
            self._spin_burst: "burst_shots",
            self._spin_burst_interval: "burst_interval",
            self._spin_inter_cd: "inter_target_cooldown",
            self._spin_cycle_cd: "cycle_cooldown",
            self._spin_max_queue: "max_targets_per_cycle",
            self._chk_optimize: "optimize_travel",
            self._slider_speed: "engagement_speed",
            self._chk_precision: "precision_enable",
            self._spin_prec_settle: "precision_settle",
            self._spin_prec_step: "precision_step",
            self._spin_deadzone_pan: "precision_deadzone_pan",
            self._spin_deadzone_tilt: "precision_deadzone_tilt",
            self._spin_error_ema: "precision_error_ema",
            self._spin_aim_lock_pan: "aim_lock_pan_tolerance",
            self._spin_aim_lock_tilt: "aim_lock_tilt_tolerance",
            self._spin_aim_lock_frames: "aim_lock_required_frames",
            self._spin_fire_enter_pan: "fire_trigger_enter_pan",
            self._spin_fire_enter_tilt: "fire_trigger_enter_tilt",
            self._spin_fire_exit_pan: "fire_trigger_exit_pan",
            self._spin_fire_exit_tilt: "fire_trigger_exit_tilt",
            self._spin_recenter_pan: "fire_recenter_pan",
            self._spin_recenter_tilt: "fire_recenter_tilt",
            self._spin_target_loss_timeout: "target_loss_timeout",
            self._chk_continuous_hunt_loss: "continuous_hunt_on_loss",
            self._chk_adaptive_loss_recovery: "adaptive_loss_recovery_enabled",
            self._combo_loss_search_style: "loss_search_style",
            self._spin_loss_search_rounds: "loss_search_rounds",
            self._spin_loss_handoff_pursuit: "loss_handoff_pursuit_time_s",
            self._spin_loss_handoff_backoff: "loss_handoff_backoff_pan_deg",
            self._spin_loss_handoff_tilt: "loss_handoff_tilt_step_deg",
            self._spin_loss_retry_sparse: "loss_persistent_retry_passes_sparse",
            self._spin_loss_retry_crowded: "loss_persistent_retry_passes_crowded",
            self._spin_loss_switch_margin: "loss_switch_score_margin",
            self._spin_loss_crowd_threshold: "loss_scene_crowding_threshold",
            self._spin_loss_personality: "loss_personality_intensity",
            self._spin_loss_velocity_bias: "loss_personality_velocity_bias",
            self._combo_guard_mode: "guard_mode",
            self._spin_guard_pan: "guard_pan",
            self._spin_guard_tilt: "guard_tilt",
            self._spin_pan_min: "pan_limit_min",
            self._spin_pan_max: "pan_limit_max",
            self._spin_tilt_min: "tilt_limit_min",
            self._spin_tilt_max: "tilt_limit_max",
            self._spin_sweep_min: "sweep_min",
            self._spin_sweep_max: "sweep_max",
            self._spin_sweep_tilt: "sweep_tilt",
            self._spin_sweep_speed: "sweep_speed",
            self._wp_list: "waypoint_list",
            self._spin_wp_dwell: "waypoint_dwell",
            self._spin_wp_speed: "waypoint_speed",
            self._spin_rnd_pan_min: "random_pan_min",
            self._spin_rnd_pan_max: "random_pan_max",
            self._spin_rnd_tilt_min: "random_tilt_min",
            self._spin_rnd_tilt_max: "random_tilt_max",
            self._spin_rnd_dwell: "random_dwell",
            self._spin_rnd_speed: "random_speed",
            self._spin_hfov: "camera_hfov",
            self._spin_vfov: "camera_vfov",
            self._chk_overlay: "show_overlay",
            self._chk_scores: "show_scores",
            self._chk_zone: "show_zone",
            self._spin_step: "manual_step",
            self._btn_led: "led_toggle",
            self._btn_laser: "laser_toggle",
            self._btn_safety: "safety_toggle",
            self._btn_fire: "manual_fire",
        }
        optional_widget_keys = {
            "_chk_human_voice_enabled": "human_voice_enabled",
            "_chk_mute_buzzer_for_human_voice": "mute_buzzer_when_human_voice_enabled",
            "_combo_human_voice_style": "human_voice_style",
            "_combo_human_voice": "human_voice_name",
            "_btn_test_human_voice": "human_voice_test",
            "_slider_human_voice_rate": "human_voice_rate",
            "_slider_human_voice_pitch": "human_voice_pitch",
            "_slider_human_voice_volume": "human_voice_volume",
            "_btn_human_voice_fallback": "human_voice_fallback",
            "_btn_human_voice_stop": "human_voice_stop",
            "_btn_human_voice_refresh": "human_voice_refresh",
            "_btn_human_voice_validate": "human_voice_validate",
            "_btn_human_voice_validate_all": "human_voice_validate_all",
            "_chk_ai_auto_speak": "ai_auto_speak",
            "_btn_ai_speak_last": "ai_speak_last",
            "_lbl_ai_examples": "ai_request_examples",
        }
        for attr_name, tooltip_key in optional_widget_keys.items():
            widget = getattr(self, attr_name, None)
            if widget is not None:
                widget_map[widget] = tooltip_key
        for widget, key in widget_map.items():
            self._apply_tooltip(widget, key)

        weight_tooltip_keys = {
            "w_proximity": "weight_proximity",
            "w_size": "weight_size",
            "w_confidence": "weight_confidence",
            "w_class_priority": "weight_class_priority",
            "w_speed": "weight_speed",
            "w_persistence": "weight_persistence",
            "w_approach": "weight_approach",
        }
        for key, slider in getattr(self, "_weight_sliders", {}).items():
            self._apply_tooltip(slider, weight_tooltip_keys.get(key, key))

        for widget, key in getattr(self, "_extra_tooltip_widgets", []):
            self._apply_tooltip(widget, key)

        self._apply_missing_button_tooltips()

    def _default_button_tooltip(self, button: QPushButton) -> str:
        text = " ".join(str(button.text() or "").split())
        if not text:
            return ""

        symbol_tooltips = {
            "▲": "Move tilt up by the configured manual step.",
            "▼": "Move tilt down by the configured manual step.",
            "◀": "Move pan left by the configured manual step.",
            "▶": "Move pan right by the configured manual step.",
            "↖": "Move pan left and tilt up by the configured manual step.",
            "↗": "Move pan right and tilt up by the configured manual step.",
            "↙": "Move pan left and tilt down by the configured manual step.",
            "↘": "Move pan right and tilt down by the configured manual step.",
            "HOME": "Move to the configured guard home pan and tilt position.",
            "RUN SWEEP": "Run a slow manual sweep using the configured sweep pan range and tilt limits.",
            "SAVE": "Save the current Smart Sentry settings to disk.",
        }
        mapped = symbol_tooltips.get(text.upper())
        if mapped:
            return mapped

        action = "Toggle" if button.isCheckable() else "Activate"
        return f"{action} {text.lower()}."

    def _apply_missing_button_tooltips(self) -> None:
        for button in self.findChildren(QPushButton):
            try:
                if str(button.toolTip() or "").strip():
                    continue
                tooltip = self._default_button_tooltip(button)
                if tooltip:
                    button.setToolTip(tooltip)
            except Exception:
                continue

    # ------------------------------------------------------------------ #
    #  Master Profiles Tab
    # ------------------------------------------------------------------ #

    def _build_master_profiles_tab(self) -> QWidget:
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(6)

        intro = QLabel(
            "Master profiles apply coordinated Detection, Target Filter, Threat AI, Engage, and bus-servo timing presets in one click. "
            "Each tab can still be tuned independently afterward."
        )
        intro.setWordWrap(True)
        self._set_theme_role(intro, "subtleBody")
        lay.addWidget(intro)

        preset_grp = QGroupBox("Coordinated Profiles")
        preset_lay = QVBoxLayout(preset_grp)
        preset_lay.setSpacing(4)

        self._master_profiles_grid = QGridLayout()
        preset_lay.addLayout(self._master_profiles_grid)
        self._rebuild_master_profile_buttons()

        self._lbl_master_profile = QLabel("")
        self._lbl_master_profile.setWordWrap(True)
        self._set_theme_role(self._lbl_master_profile, "mutedCompact")
        preset_lay.addWidget(self._lbl_master_profile)
        lay.addWidget(preset_grp)

        save_grp = QGroupBox("Manage Custom Presets")
        save_lay = QVBoxLayout(save_grp)

        select_row = QHBoxLayout()
        select_row.addWidget(QLabel("Saved preset:"))
        self._combo_custom_master_profiles = QComboBox()
        self._combo_custom_master_profiles.currentIndexChanged.connect(self._on_custom_master_profile_selected)
        self._apply_tooltip(self._combo_custom_master_profiles, "custom_master_profile_select")
        select_row.addWidget(self._combo_custom_master_profiles, 1)
        btn_use_active_custom = QPushButton("Use Active")
        self._set_button_role(btn_use_active_custom, "utility")
        btn_use_active_custom.clicked.connect(self._select_active_custom_master_profile_for_edit)
        self._apply_tooltip(btn_use_active_custom, "custom_master_use_active")
        select_row.addWidget(btn_use_active_custom)
        btn_new_custom = QPushButton("New")
        self._set_button_role(btn_new_custom, "utility")
        btn_new_custom.clicked.connect(self._clear_custom_master_profile_editor)
        self._apply_tooltip(btn_new_custom, "custom_master_new")
        select_row.addWidget(btn_new_custom)
        self._register_responsive_box_layout(select_row, "dense_row")
        save_lay.addLayout(select_row)

        save_row = QHBoxLayout()
        save_row.addWidget(QLabel("Preset name:"))
        self._edit_custom_master_name = QLineEdit()
        self._edit_custom_master_name.setPlaceholderText("Example: Yellow Indoor Sniper")
        self._apply_tooltip(self._edit_custom_master_name, "custom_master_name")
        save_row.addWidget(self._edit_custom_master_name, 1)
        self._btn_update_custom_master = QPushButton("Update")
        self._set_button_role(self._btn_update_custom_master, "utility")
        self._btn_update_custom_master.clicked.connect(self._update_selected_custom_master_profile)
        self._apply_tooltip(self._btn_update_custom_master, "custom_master_update")
        save_row.addWidget(self._btn_update_custom_master)
        btn_save_custom = QPushButton("Save New")
        self._set_button_role(btn_save_custom, "utility")
        btn_save_custom.clicked.connect(self._save_new_custom_master_profile)
        self._apply_tooltip(btn_save_custom, "custom_master_save_as_new")
        save_row.addWidget(btn_save_custom)
        self._register_responsive_box_layout(save_row, "dense_row")
        save_lay.addLayout(save_row)
        self._lbl_custom_master_info = QLabel(
            "Select a saved custom preset to edit/update it, or click New and enter a unique preset name to save the current stack as a new coordinated profile."
        )
        self._lbl_custom_master_info.setWordWrap(True)
        self._set_theme_role(self._lbl_custom_master_info, "mutedCompact")
        save_lay.addWidget(self._lbl_custom_master_info)
        lay.addWidget(save_grp)

        summary_grp = QGroupBox("Current Stack")
        summary_lay = QVBoxLayout(summary_grp)
        summary_lay.setSpacing(3)
        self._lbl_master_stack = QLabel("")
        self._lbl_master_stack.setWordWrap(True)
        self._set_theme_role(self._lbl_master_stack, "summary")
        summary_lay.addWidget(self._lbl_master_stack)
        lay.addWidget(summary_grp)

        lay.addStretch()
        self._update_master_stack_summary()
        self._set_master_profile_label(self._match_master_profile_name())
        self._rebuild_custom_master_profile_combo()
        return w

    def _build_theme_tab(self) -> QWidget:
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(6)

        intro = QLabel(
            "Choose a visual preset, then fine-tune opacity, contrast, accent strength, and radius. "
            "Changes apply live and save automatically."
        )
        intro.setWordWrap(True)
        self._set_theme_role(intro, "subtleBody")
        lay.addWidget(intro)

        preset_grp = QGroupBox("Theme Presets")
        preset_lay = QVBoxLayout(preset_grp)
        preset_lay.setSpacing(6)

        preset_row = QHBoxLayout()
        preset_row.addWidget(QLabel("Preset:"))
        self._combo_theme_preset = QComboBox()
        for key, data in THEME_PRESETS.items():
            self._combo_theme_preset.addItem(data["label"], key)
        self._combo_theme_preset.currentIndexChanged.connect(self._on_theme_preset_changed)
        preset_row.addWidget(self._combo_theme_preset, 1)
        btn_theme_apply = QPushButton("Apply")
        self._set_button_role(btn_theme_apply, "utility")
        btn_theme_apply.clicked.connect(self._apply_theme)
        preset_row.addWidget(btn_theme_apply)
        self._register_responsive_box_layout(preset_row, "compact_row")
        preset_lay.addLayout(preset_row)

        quick_presets = QGridLayout()
        quick_presets.setHorizontalSpacing(6)
        quick_presets.setVerticalSpacing(6)
        for index, (key, data) in enumerate(THEME_PRESETS.items()):
            btn = QPushButton(data["label"])
            self._set_button_role(btn, "preset")
            btn.clicked.connect(lambda _checked=False, preset_key=key: self._select_theme_preset(preset_key))
            quick_presets.addWidget(btn, index // 2, index % 2)
        self._normalize_preset_grid_button_widths(quick_presets)
        preset_lay.addLayout(quick_presets)

        self._lbl_theme_preset_desc = QLabel("")
        self._lbl_theme_preset_desc.setWordWrap(True)
        self._set_theme_role(self._lbl_theme_preset_desc, "mutedCompact")
        preset_lay.addWidget(self._lbl_theme_preset_desc)
        lay.addWidget(preset_grp)

        tune_grp = QGroupBox("Fine Tuning")
        tune_lay = QGridLayout(tune_grp)
        tune_lay.setHorizontalSpacing(8)
        tune_lay.setVerticalSpacing(8)

        def add_slider_row(row: int, label_text: str, minimum: int, maximum: int):
            label = QLabel(label_text)
            slider = QSlider(Qt.Horizontal)
            slider.setRange(minimum, maximum)
            slider.setSingleStep(1)
            value_label = QLabel("")
            value_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            tune_lay.addWidget(label, row, 0)
            tune_lay.addWidget(slider, row, 1)
            tune_lay.addWidget(value_label, row, 2)
            return slider, value_label

        self._slider_theme_accent, self._lbl_theme_accent = add_slider_row(0, "Accent Strength", 60, 140)
        self._slider_theme_surface_opacity, self._lbl_theme_surface_opacity = add_slider_row(1, "Panel Transparency", 55, 100)
        self._slider_theme_video_opacity, self._lbl_theme_video_opacity = add_slider_row(2, "Video Panel Opacity", 55, 100)
        self._slider_theme_window_opacity, self._lbl_theme_window_opacity = add_slider_row(3, "Window Opacity", 70, 100)
        self._slider_theme_contrast, self._lbl_theme_contrast = add_slider_row(4, "Contrast", 85, 125)
        self._slider_theme_radius, self._lbl_theme_radius = add_slider_row(5, "Corner Radius", 8, 24)

        for slider in (
            self._slider_theme_accent,
            self._slider_theme_surface_opacity,
            self._slider_theme_video_opacity,
            self._slider_theme_window_opacity,
            self._slider_theme_contrast,
            self._slider_theme_radius,
        ):
            slider.valueChanged.connect(self._on_theme_settings_changed)

        note = QLabel(
            "Window opacity only affects the standalone Smart Sentry window. When this tab is embedded in another host window, "
            "the host stays opaque and only the panel surfaces become more transparent."
        )
        note.setWordWrap(True)
        self._set_theme_role(note, "subtleBody")
        tune_lay.addWidget(note, 7, 0, 1, 3)
        lay.addWidget(tune_grp)

        summary_grp = QGroupBox("Theme Summary")
        summary_lay = QVBoxLayout(summary_grp)
        self._lbl_theme_summary = QLabel("")
        self._lbl_theme_summary.setWordWrap(True)
        self._set_theme_role(self._lbl_theme_summary, "summary")
        summary_lay.addWidget(self._lbl_theme_summary)

        button_row = QHBoxLayout()
        button_row.addStretch(1)
        btn_theme_reset = QPushButton("Reset Default")
        self._set_button_role(btn_theme_reset, "utility")
        btn_theme_reset.clicked.connect(self._reset_theme_defaults)
        button_row.addWidget(btn_theme_reset)
        summary_lay.addLayout(button_row)
        lay.addWidget(summary_grp)

        lay.addStretch()
        self._sync_theme_widgets()
        return w

    # ------------------------------------------------------------------ #
    #  Connection Tab
    # ------------------------------------------------------------------ #

    def _build_connection_tab(self) -> QWidget:
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(6)

        # ---- Camera ----
        cam_grp = QGroupBox("Camera")
        cam_lay = QGridLayout(cam_grp)
        cam_lay.addWidget(QLabel("Source:"), 0, 0)
        self._edit_cam_source = QLineEdit(self.config.connection.camera_source)
        self._edit_cam_source.setPlaceholderText("Blank defaults to camera 0, or enter camera index/URL")
        self._apply_tooltip(self._edit_cam_source, "camera_source")
        cam_lay.addWidget(self._edit_cam_source, 0, 1)

        cam_lay.addWidget(QLabel("Resolution:"), 1, 0)
        self._combo_cam_resolution = QComboBox()
        self._compact_combo_box(self._combo_cam_resolution, minimum_chars=12)
        self._populate_camera_resolution_combo(self.config.connection.camera_width, self.config.connection.camera_height)
        self._apply_tooltip(self._combo_cam_resolution, "camera_width")
        self._combo_cam_resolution.currentIndexChanged.connect(self._on_camera_resolution_changed)
        cam_lay.addWidget(self._combo_cam_resolution, 1, 1)

        cam_lay.addWidget(QLabel("Webcam zoom:"), 2, 0)
        webcam_zoom_row = QHBoxLayout()
        self._slider_webcam_zoom = QSlider(Qt.Horizontal)
        self._slider_webcam_zoom.setRange(40, 200)
        self._slider_webcam_zoom.setSingleStep(5)
        self._slider_webcam_zoom.setPageStep(10)
        self._slider_webcam_zoom.setValue(int(getattr(self.config.connection, "webcam_zoom_pct", 100)))
        self._slider_webcam_zoom.valueChanged.connect(self._on_source_zoom_changed)
        webcam_zoom_row.addWidget(self._slider_webcam_zoom, 1)
        self._lbl_webcam_zoom = QLabel("")
        self._lbl_webcam_zoom.setMinimumWidth(56)
        self._register_responsive_label(self._lbl_webcam_zoom, "zoom_value")
        webcam_zoom_row.addWidget(self._lbl_webcam_zoom)
        cam_lay.addLayout(webcam_zoom_row, 2, 1)

        cam_lay.addWidget(QLabel("Test source zoom:"), 3, 0)
        test_zoom_row = QHBoxLayout()
        self._slider_test_zoom = QSlider(Qt.Horizontal)
        self._slider_test_zoom.setRange(25, 200)
        self._slider_test_zoom.setSingleStep(5)
        self._slider_test_zoom.setPageStep(10)
        self._slider_test_zoom.setValue(int(getattr(self.config.connection, "test_source_zoom_pct", 100)))
        self._slider_test_zoom.valueChanged.connect(self._on_source_zoom_changed)
        test_zoom_row.addWidget(self._slider_test_zoom, 1)
        self._lbl_test_zoom = QLabel("")
        self._lbl_test_zoom.setMinimumWidth(56)
        self._register_responsive_label(self._lbl_test_zoom, "zoom_value")
        test_zoom_row.addWidget(self._lbl_test_zoom)
        cam_lay.addLayout(test_zoom_row, 3, 1)

        lbl_live_section = QLabel("Live Camera")
        self._set_theme_role(lbl_live_section, "sectionPadded")
        cam_lay.addWidget(lbl_live_section, 4, 0, 1, 2)

        self._btn_cam = QPushButton("Open Camera")
        self._set_button_role(self._btn_cam, "primary")
        self._btn_cam.clicked.connect(self._toggle_camera)
        self._apply_tooltip(self._btn_cam, "camera_toggle")
        live_action_row = QHBoxLayout()
        live_action_row.addWidget(self._btn_cam)

        # One-click return to webcam after a test video/image session ends
        self._btn_return_to_camera = QPushButton("\u21a9 Back")
        self._set_button_role(self._btn_return_to_camera, "primary")
        self._btn_return_to_camera.clicked.connect(self._return_to_camera)
        self._btn_return_to_camera.setEnabled(False)
        self._btn_return_to_camera.setToolTip(
            "Close the current test source and reopen the last webcam"
        )
        live_action_row.addWidget(self._btn_return_to_camera)
        self._register_responsive_box_layout(live_action_row, "action_row")
        cam_lay.addLayout(live_action_row, 5, 0, 1, 2)

        lbl_media_section = QLabel("Media Inputs")
        self._set_theme_role(lbl_media_section, "sectionPadded")
        cam_lay.addWidget(lbl_media_section, 6, 0, 1, 2)

        self._btn_test_media = QPushButton("Open Media...")
        self._set_button_role(self._btn_test_media, "utility")
        self._btn_test_media.clicked.connect(self._browse_test_media)
        cam_lay.addWidget(self._btn_test_media, 7, 0, 1, 2)

        cam_lay.addWidget(QLabel("Video URL:"), 8, 0)
        self._edit_video_url = QLineEdit()
        self._edit_video_url.setPlaceholderText("Paste a YouTube or direct video URL")
        url_col = QVBoxLayout()
        url_col.setSpacing(4)
        url_col.addWidget(self._edit_video_url)

        self._btn_open_video_url = QPushButton("Open URL")
        self._set_button_role(self._btn_open_video_url, "utility")
        self._btn_open_video_url.clicked.connect(self._open_video_url)
        url_button_row = QHBoxLayout()
        url_button_row.addStretch(1)
        url_button_row.addWidget(self._btn_open_video_url)
        url_col.addLayout(url_button_row)
        cam_lay.addLayout(url_col, 8, 1)

        lbl_playback_section = QLabel("Playback")
        self._set_theme_role(lbl_playback_section, "sectionPadded")
        cam_lay.addWidget(lbl_playback_section, 9, 0, 1, 2)

        resolution_action_grid = QGridLayout()
        resolution_action_grid.setHorizontalSpacing(6)
        resolution_action_grid.setVerticalSpacing(4)
        self._btn_apply_camera_resolution = QPushButton("Apply Res")
        self._set_button_role(self._btn_apply_camera_resolution, "utility")
        self._btn_apply_camera_resolution.clicked.connect(self._apply_camera_resolution)
        resolution_action_grid.addWidget(self._btn_apply_camera_resolution, 0, 0)

        self._btn_restart_app = QPushButton("Restart")
        self._set_button_role(self._btn_restart_app, "utility")
        self._btn_restart_app.clicked.connect(self._restart_application)
        resolution_action_grid.addWidget(self._btn_restart_app, 0, 1)
        self._style_button_row([self._btn_apply_camera_resolution, self._btn_restart_app], "utility")
        self._register_responsive_button_grid(resolution_action_grid)
        self._reflow_responsive_button_grid(resolution_action_grid)

        media_ctrl_grid = QGridLayout()
        media_ctrl_grid.setHorizontalSpacing(6)
        media_ctrl_grid.setVerticalSpacing(4)
        self._btn_test_media_play = QPushButton("Play")
        self._set_button_role(self._btn_test_media_play, "utility")
        self._btn_test_media_play.clicked.connect(self._play_test_media)
        media_ctrl_grid.addWidget(self._btn_test_media_play, 0, 0)

        self._btn_test_media_pause = QPushButton("Pause")
        self._set_button_role(self._btn_test_media_pause, "utility")
        self._btn_test_media_pause.clicked.connect(self._pause_test_media)
        media_ctrl_grid.addWidget(self._btn_test_media_pause, 0, 1)

        self._btn_test_media_step = QPushButton("Step")
        self._set_button_role(self._btn_test_media_step, "utility")
        self._btn_test_media_step.clicked.connect(self._step_test_media_frame)
        media_ctrl_grid.addWidget(self._btn_test_media_step, 1, 0)

        self._btn_test_media_restart = QPushButton("Restart")
        self._set_button_role(self._btn_test_media_restart, "utility")
        self._btn_test_media_restart.clicked.connect(self._restart_test_media)
        media_ctrl_grid.addWidget(self._btn_test_media_restart, 1, 1)

        self._chk_test_media_loop = QCheckBox("Loop")
        self._chk_test_media_loop.setChecked(True)
        self._chk_test_media_loop.toggled.connect(self._on_test_media_loop_toggled)
        self._style_button_row(
            [self._btn_test_media_play, self._btn_test_media_pause, self._btn_test_media_step, self._btn_test_media_restart],
            "utility",
        )
        self._register_responsive_button_grid(media_ctrl_grid)
        self._reflow_responsive_button_grid(media_ctrl_grid)
        playback_col = QVBoxLayout()
        playback_col.setSpacing(4)
        playback_col.addLayout(media_ctrl_grid)
        loop_row = QHBoxLayout()
        loop_row.addStretch(1)
        loop_row.addWidget(self._chk_test_media_loop)
        playback_col.addLayout(loop_row)
        cam_lay.addLayout(playback_col, 10, 0, 1, 2)

        lbl_maintenance_section = QLabel("Maintenance")
        self._set_theme_role(lbl_maintenance_section, "sectionPadded")
        cam_lay.addWidget(lbl_maintenance_section, 11, 0, 1, 2)

        cam_lay.addLayout(resolution_action_grid, 12, 0, 1, 2)

        self._lbl_cam_status = QLabel("Camera closed")
        self._camera_status_level = "neutral"
        self._lbl_cam_status.setStyleSheet(self._camera_status_style(self._camera_status_level))
        cam_lay.addWidget(self._lbl_cam_status, 13, 0, 1, 2)
        self._on_source_zoom_changed()
        self._update_test_media_controls()

        lay.addWidget(cam_grp)

        # Connect / disconnect
        btn_row = QHBoxLayout()
        self._btn_connect = QPushButton("Connect")
        self._set_button_role(self._btn_connect, "primary")
        self._btn_connect.clicked.connect(self._toggle_connection)
        self._apply_tooltip(self._btn_connect, "connect_toggle")
        btn_row.addWidget(self._btn_connect)
        lay.addLayout(btn_row)

        # Connection mode selector
        type_grp = QGroupBox("Connection Mode")
        type_lay = QVBoxLayout(type_grp)
        self._combo_conn_type = QComboBox()
        self._compact_combo_box(self._combo_conn_type, minimum_chars=18)
        self._combo_conn_type.addItems(SentryV2Comm.MODE_LABELS)
        self._combo_conn_type.setCurrentIndex(self.config.connection.connection_type)
        self._combo_conn_type.currentIndexChanged.connect(self._on_conn_type_changed)
        self._apply_tooltip(self._combo_conn_type, "connection_mode")
        type_lay.addWidget(self._combo_conn_type)
        self._lbl_mode_hint = QLabel("")
        self._lbl_mode_hint.setWordWrap(True)
        self._set_theme_role(self._lbl_mode_hint, "mutedCompact")
        type_lay.addWidget(self._lbl_mode_hint)
        self._btn_wifi_pinout = QPushButton("Pin Assignments")
        self._set_button_role(self._btn_wifi_pinout, "utility")
        self._btn_wifi_pinout.clicked.connect(self._show_full_wifi_pinout)
        self._apply_tooltip(self._btn_wifi_pinout, "wifi_pinout")
        type_lay.addWidget(self._btn_wifi_pinout)
        lay.addWidget(type_grp)

        # --- ESP32 Serial settings (modes 0, 1) ---
        self._grp_esp32_serial = QGroupBox("ESP32 Serial (USB)")
        esp_lay = QGridLayout(self._grp_esp32_serial)

        esp_lay.addWidget(QLabel("COM Port:"), 0, 0)
        self._edit_esp32_port = QLineEdit(self.config.connection.esp32_port)
        self._apply_tooltip(self._edit_esp32_port, "esp32_port")
        esp_lay.addWidget(self._edit_esp32_port, 0, 1)
        btn_scan_esp = QPushButton("Scan")
        self._set_button_role(btn_scan_esp, "utility")
        btn_scan_esp.clicked.connect(lambda: self._scan_ports("esp32"))
        self._apply_tooltip(btn_scan_esp, "scan_esp32_ports")
        esp_lay.addWidget(btn_scan_esp, 0, 2)

        self._combo_esp32_ports = QComboBox()
        self._compact_combo_box(self._combo_esp32_ports, minimum_chars=14)
        self._combo_esp32_ports.setPlaceholderText("Available ports...")
        self._combo_esp32_ports.currentTextChanged.connect(
            lambda _: self._on_port_selected("esp32"))
        self._apply_tooltip(self._combo_esp32_ports, "esp32_port_list")
        esp_lay.addWidget(self._combo_esp32_ports, 1, 0, 1, 3)

        esp_lay.addWidget(QLabel("Baud Rate:"), 2, 0)
        self._spin_esp32_baud = QSpinBox()
        self._spin_esp32_baud.setRange(9600, 921600)
        self._spin_esp32_baud.setSingleStep(9600)
        self._spin_esp32_baud.setValue(self.config.connection.esp32_baud)
        self._apply_tooltip(self._spin_esp32_baud, "esp32_baud")
        esp_lay.addWidget(self._spin_esp32_baud, 2, 1, 1, 2)

        lay.addWidget(self._grp_esp32_serial)

        # --- Debug Board Serial settings (modes 1, 2) ---
        self._grp_debug_serial = QGroupBox("Debug Board Serial (USB)")
        dbg_lay = QGridLayout(self._grp_debug_serial)

        dbg_lay.addWidget(QLabel("COM Port:"), 0, 0)
        self._edit_debug_port = QLineEdit(self.config.connection.debug_port)
        self._apply_tooltip(self._edit_debug_port, "debug_port")
        dbg_lay.addWidget(self._edit_debug_port, 0, 1)
        btn_scan_dbg = QPushButton("Scan")
        self._set_button_role(btn_scan_dbg, "utility")
        btn_scan_dbg.clicked.connect(lambda: self._scan_ports("debug"))
        self._apply_tooltip(btn_scan_dbg, "scan_debug_ports")
        dbg_lay.addWidget(btn_scan_dbg, 0, 2)

        self._combo_debug_ports = QComboBox()
        self._compact_combo_box(self._combo_debug_ports, minimum_chars=14)
        self._combo_debug_ports.setPlaceholderText("Available ports...")
        self._combo_debug_ports.currentTextChanged.connect(
            lambda _: self._on_port_selected("debug"))
        self._apply_tooltip(self._combo_debug_ports, "debug_port_list")
        dbg_lay.addWidget(self._combo_debug_ports, 1, 0, 1, 3)

        dbg_lay.addWidget(QLabel("Baud Rate:"), 2, 0)
        self._spin_debug_baud = QSpinBox()
        self._spin_debug_baud.setRange(9600, 921600)
        self._spin_debug_baud.setSingleStep(9600)
        self._spin_debug_baud.setValue(self.config.connection.debug_baud)
        self._apply_tooltip(self._spin_debug_baud, "debug_baud")
        dbg_lay.addWidget(self._spin_debug_baud, 2, 1, 1, 2)

        lay.addWidget(self._grp_debug_serial)

        # --- Servo settings (modes 1, 2) ---
        self._grp_servo = QGroupBox("Bus Servo")
        srv_lay = QGridLayout(self._grp_servo)

        srv_lay.addWidget(QLabel("Pan ID:"), 0, 0)
        self._spin_pan_id = QSpinBox()
        self._spin_pan_id.setRange(0, 253)
        self._spin_pan_id.setValue(self.config.connection.pan_servo_id)
        self._apply_tooltip(self._spin_pan_id, "pan_servo_id")
        srv_lay.addWidget(self._spin_pan_id, 0, 1)

        srv_lay.addWidget(QLabel("Tilt ID:"), 1, 0)
        self._spin_tilt_id = QSpinBox()
        self._spin_tilt_id.setRange(0, 253)
        self._spin_tilt_id.setValue(self.config.connection.tilt_servo_id)
        self._apply_tooltip(self._spin_tilt_id, "tilt_servo_id")
        srv_lay.addWidget(self._spin_tilt_id, 1, 1)

        srv_lay.addWidget(QLabel("Move Time (ms):"), 2, 0)
        self._spin_servo_time = QSpinBox()
        self._spin_servo_time.setRange(0, 1000)
        self._spin_servo_time.setSingleStep(5)
        self._spin_servo_time.setValue(self.config.connection.bus_servo_time_ms)
        self._spin_servo_time.valueChanged.connect(self._on_servo_time_changed)
        self._apply_tooltip(self._spin_servo_time, "servo_move_time")
        srv_lay.addWidget(self._spin_servo_time, 2, 1)

        srv_lay.addWidget(QLabel("Move Time Presets:"), 3, 0)
        self._combo_servo_time_preset = QComboBox()
        self._compact_combo_box(self._combo_servo_time_preset, minimum_chars=12)
        self._combo_servo_time_preset.currentIndexChanged.connect(self._on_servo_time_preset_selected)
        srv_lay.addWidget(self._combo_servo_time_preset, 3, 1)
        self._rebuild_servo_time_preset_combo()

        self._lbl_servo_time_preset = QLabel("")
        self._lbl_servo_time_preset.setWordWrap(True)
        self._set_theme_role(self._lbl_servo_time_preset, "mutedCompact")
        srv_lay.addWidget(self._lbl_servo_time_preset, 4, 0, 1, 2)
        self._set_servo_time_preset_label(self._match_servo_time_preset_name())

        lay.addWidget(self._grp_servo)

        # --- WiFi UDP settings (modes 2, 3) ---
        self._grp_udp = QGroupBox("WiFi UDP")
        udp_lay = QGridLayout(self._grp_udp)

        udp_lay.addWidget(QLabel("Host:"), 0, 0)
        self._edit_udp_host = QLineEdit(self.config.connection.udp_host)
        self._apply_tooltip(self._edit_udp_host, "udp_host")
        udp_lay.addWidget(self._edit_udp_host, 0, 1)

        udp_lay.addWidget(QLabel("Port:"), 1, 0)
        self._spin_udp_port = QSpinBox()
        self._spin_udp_port.setRange(1, 65535)
        self._spin_udp_port.setValue(self.config.connection.udp_port)
        self._apply_tooltip(self._spin_udp_port, "udp_port")
        udp_lay.addWidget(self._spin_udp_port, 1, 1)

        udp_lay.addWidget(QLabel("WiFi Adapter:"), 2, 0)
        self._combo_wifi_adapter = QComboBox()
        self._combo_wifi_adapter.setToolTip(
            "Select the Windows WiFi adapter to use for the ESP32 SSID.\n"
            "'(auto)' uses the first available adapter.\n"
            "Set to your dedicated USB dongle (e.g. SMART SENTRY CON) to prevent\n"
            "Windows from switching to a different adapter during reconnects."
        )
        self._combo_wifi_adapter.addItem("(auto)", "")
        _saved_iface = str(getattr(self.config.connection, "wifi_interface", "") or "").strip()
        _iface_names = self._enumerate_windows_wifi_interfaces()
        _iface_set: set = set()
        for _iname in _iface_names:
            if _iname and _iname not in _iface_set:
                self._combo_wifi_adapter.addItem(_iname, _iname)
                _iface_set.add(_iname)
        if _saved_iface and _saved_iface not in _iface_set:
            self._combo_wifi_adapter.addItem(_saved_iface, _saved_iface)
        _target_idx = 0
        if _saved_iface:
            for _i in range(self._combo_wifi_adapter.count()):
                if self._combo_wifi_adapter.itemData(_i) == _saved_iface:
                    _target_idx = _i
                    break
        self._combo_wifi_adapter.setCurrentIndex(_target_idx)
        udp_lay.addWidget(self._combo_wifi_adapter, 2, 1)

        lay.addWidget(self._grp_udp)

        # --- Secondary ESP32 WiFi settings (mode 4) ---
        self._grp_servo_udp = QGroupBox("Secondary ESP32 WiFi")
        servo_udp_lay = QGridLayout(self._grp_servo_udp)

        servo_udp_lay.addWidget(QLabel("Host:"), 0, 0)
        self._edit_servo_udp_host = QLineEdit(self.config.connection.servo_udp_host)
        self._apply_tooltip(self._edit_servo_udp_host, "servo_udp_host")
        servo_udp_lay.addWidget(self._edit_servo_udp_host, 0, 1)

        servo_udp_lay.addWidget(QLabel("Port:"), 1, 0)
        self._spin_servo_udp_port = QSpinBox()
        self._spin_servo_udp_port.setRange(1, 65535)
        self._spin_servo_udp_port.setValue(self.config.connection.servo_udp_port)
        self._apply_tooltip(self._spin_servo_udp_port, "servo_udp_port")
        servo_udp_lay.addWidget(self._spin_servo_udp_port, 1, 1)

        lay.addWidget(self._grp_servo_udp)

        # Direction inversion
        inv_grp = QGroupBox("Direction")
        inv_lay = QVBoxLayout(inv_grp)
        self._chk_invert_pan = QCheckBox("Invert Pan")
        self._chk_invert_pan.setChecked(self.config.connection.invert_pan)
        self._chk_invert_pan.toggled.connect(self._on_invert_changed)
        self._apply_tooltip(self._chk_invert_pan, "invert_pan")
        inv_lay.addWidget(self._chk_invert_pan)
        self._chk_invert_tilt = QCheckBox("Invert Tilt")
        self._chk_invert_tilt.setChecked(self.config.connection.invert_tilt)
        self._chk_invert_tilt.toggled.connect(self._on_invert_changed)
        self._apply_tooltip(self._chk_invert_tilt, "invert_tilt")
        inv_lay.addWidget(self._chk_invert_tilt)
        lay.addWidget(inv_grp)

        # Status
        self._lbl_conn_status = QLabel("Disconnected")
        self._connection_status_level = "error"
        self._lbl_conn_status.setStyleSheet(self._connection_status_style(self._connection_status_level))
        lay.addWidget(self._lbl_conn_status)

        self._lbl_last_cmd = QLabel("")
        self._lbl_last_cmd.setStyleSheet(self._compact_status_style("neutral"))
        self._lbl_last_cmd.setWordWrap(True)
        lay.addWidget(self._lbl_last_cmd)

        lay.addStretch()

        # Initial visibility
        self._update_conn_panel_visibility()

        return w

    # ------------------------------------------------------------------ #
    #  Detection Mode Tab
    # ------------------------------------------------------------------ #

    def _build_detection_tab(self) -> QWidget:
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(4)

        # Detection mode selector
        grp_mode = QGroupBox("Detection Method")
        mode_lay = QVBoxLayout(grp_mode)

        self._combo_detection_mode = QComboBox()
        for name in DETECTION_MODES:
            self._combo_detection_mode.addItem(name)
        self._combo_detection_mode.setCurrentIndex(self.config.detection_mode.detection_mode)
        self._combo_detection_mode.currentIndexChanged.connect(self._on_detection_mode_changed)
        self._apply_tooltip(self._combo_detection_mode, "detection_mode")
        mode_lay.addWidget(self._combo_detection_mode)

        # Description label
        self._lbl_mode_desc = QLabel("")
        self._lbl_mode_desc.setWordWrap(True)
        self._set_theme_role(self._lbl_mode_desc, "subtleBody")
        mode_lay.addWidget(self._lbl_mode_desc)
        self._update_mode_description()

        lay.addWidget(grp_mode)

        # Method-scoped target-size presets
        preset_grp = QGroupBox("Target Size Presets")
        preset_lay = QVBoxLayout(preset_grp)
        preset_row = QHBoxLayout()
        preset_row.addWidget(QLabel("Size Profile:"))

        self._combo_target_size_preset = QComboBox()
        for size_key, profile in TARGET_SIZE_PRESETS.items():
            self._combo_target_size_preset.addItem(profile["label"], size_key)
        preset_row.addWidget(self._combo_target_size_preset)

        btn_apply_size = QPushButton("Apply")
        self._set_button_role(btn_apply_size, "utility")
        btn_apply_size.clicked.connect(self._apply_selected_target_size_preset)
        preset_row.addWidget(btn_apply_size)
        self._register_responsive_box_layout(preset_row, "compact_row")
        preset_lay.addLayout(preset_row)

        self._lbl_detection_preset = QLabel("")
        self._lbl_detection_preset.setWordWrap(True)
        self._set_theme_role(self._lbl_detection_preset, "mutedCompact")
        preset_lay.addWidget(self._lbl_detection_preset)

        lay.addWidget(preset_grp)

        # --- Contour settings (modes 0,1,3,7,8) ---
        self._grp_contour = QGroupBox("Contour Settings")
        contour_lay = QGridLayout(self._grp_contour)

        contour_lay.addWidget(QLabel("Min Area (px):"), 0, 0)
        self._spin_min_contour = QDoubleSpinBox()
        self._spin_min_contour.setRange(0, 5000000)
        self._spin_min_contour.setSingleStep(100)
        self._spin_min_contour.setDecimals(0)
        self._spin_min_contour.setValue(self.config.detection_mode.min_contour_area)
        self._spin_min_contour.valueChanged.connect(self._on_detection_settings_changed)
        self._apply_tooltip(self._spin_min_contour, "min_contour_area")
        contour_lay.addWidget(self._spin_min_contour, 0, 1)

        contour_lay.addWidget(QLabel("Max Area (px):"), 1, 0)
        self._spin_max_contour = QDoubleSpinBox()
        self._spin_max_contour.setRange(0, 5000000)
        self._spin_max_contour.setSingleStep(10000)
        self._spin_max_contour.setDecimals(0)
        self._spin_max_contour.setValue(self.config.detection_mode.max_contour_area)
        self._spin_max_contour.valueChanged.connect(self._on_detection_settings_changed)
        self._apply_tooltip(self._spin_max_contour, "max_contour_area")
        contour_lay.addWidget(self._spin_max_contour, 1, 1)

        self._lbl_contour_ratio = QLabel()
        self._set_theme_role(self._lbl_contour_ratio, "mutedCompact")
        contour_lay.addWidget(self._lbl_contour_ratio, 2, 0, 1, 2)

        lay.addWidget(self._grp_contour)

        # --- YOLO settings (modes 2,4,5,9,10) ---
        self._grp_yolo = QGroupBox("YOLO Settings")
        yolo_lay = QGridLayout(self._grp_yolo)

        yolo_lay.addWidget(QLabel("Model Folder:"), 0, 0)
        self._edit_yolo_model_dir = QLineEdit()
        self._edit_yolo_model_dir.setReadOnly(True)
        self._edit_yolo_model_dir.setPlaceholderText("Using bundled/default YOLO model folders")
        yolo_lay.addWidget(self._edit_yolo_model_dir, 0, 1)
        self._btn_browse_yolo_dir = QPushButton("Browse...")
        self._set_button_role(self._btn_browse_yolo_dir, "utility")
        self._btn_browse_yolo_dir.clicked.connect(self._browse_yolo_model_dir)
        yolo_lay.addWidget(self._btn_browse_yolo_dir, 0, 2)
        self._btn_refresh_yolo_models = QPushButton("Refresh")
        self._set_button_role(self._btn_refresh_yolo_models, "utility")
        self._btn_refresh_yolo_models.clicked.connect(self._scan_yolo_models)
        yolo_lay.addWidget(self._btn_refresh_yolo_models, 0, 3)

        yolo_lay.addWidget(QLabel("Model:"), 1, 0)
        self._combo_yolo_model = QComboBox()
        self._combo_yolo_model.setPlaceholderText("Select model...")
        self._scan_yolo_models()
        self._combo_yolo_model.currentIndexChanged.connect(self._on_yolo_model_selection_changed)
        self._apply_tooltip(self._combo_yolo_model, "yolo_model")
        yolo_lay.addWidget(self._combo_yolo_model, 1, 1, 1, 2)
        self._btn_load_yolo = QPushButton("Load")
        self._set_button_role(self._btn_load_yolo, "utility")
        self._btn_load_yolo.clicked.connect(self._load_yolo_model)
        self._apply_tooltip(self._btn_load_yolo, "load_yolo_model")
        yolo_lay.addWidget(self._btn_load_yolo, 1, 3)

        yolo_lay.addWidget(QLabel("Classes:"), 2, 0)
        self._edit_yolo_classes = QLineEdit(", ".join(self.config.target_filter.allowed_classes))
        self._edit_yolo_classes.setPlaceholderText("person, car, dog ...")
        self._edit_yolo_classes.editingFinished.connect(self._on_yolo_classes_changed)
        self._apply_tooltip(self._edit_yolo_classes, "yolo_classes")
        yolo_lay.addWidget(self._edit_yolo_classes, 2, 1, 1, 3)

        yolo_lay.addWidget(QLabel("Confidence:"), 3, 0)
        self._spin_yolo_conf = QDoubleSpinBox()
        self._spin_yolo_conf.setRange(0.05, 1.0)
        self._spin_yolo_conf.setSingleStep(0.05)
        self._spin_yolo_conf.setDecimals(2)
        self._spin_yolo_conf.setValue(self.config.detection_mode.yolo_confidence)
        self._spin_yolo_conf.valueChanged.connect(self._on_detection_settings_changed)
        self._apply_tooltip(self._spin_yolo_conf, "yolo_confidence")
        yolo_lay.addWidget(self._spin_yolo_conf, 3, 1, 1, 3)

        yolo_lay.addWidget(QLabel("Min Area (px):"), 4, 0)
        self._spin_yolo_min_area = QSpinBox()
        self._spin_yolo_min_area.setRange(0, 10000000)
        self._spin_yolo_min_area.setSingleStep(100)
        self._spin_yolo_min_area.setValue(self.config.detection_mode.yolo_min_area)
        self._spin_yolo_min_area.valueChanged.connect(self._on_detection_settings_changed)
        self._apply_tooltip(self._spin_yolo_min_area, "yolo_min_area")
        yolo_lay.addWidget(self._spin_yolo_min_area, 4, 1, 1, 3)

        self._lbl_yolo_status = QLabel("No model loaded")
        self._lbl_yolo_status.setStyleSheet(self._compact_status_style("neutral", bold=True))
        yolo_lay.addWidget(self._lbl_yolo_status, 5, 0, 1, 4)
        self._set_yolo_status("info", "Model not loaded yet")

        lay.addWidget(self._grp_yolo)

        # --- Color settings (modes 6,7,8,9) ---
        self._grp_color = QGroupBox("Color Detection Settings")
        color_lay = QGridLayout(self._grp_color)

        color_lay.addWidget(QLabel("Color Preset:"), 0, 0)
        self._combo_color_preset = QComboBox()
        for p in COLOR_PRESETS:
            self._combo_color_preset.addItem(p)
        idx = COLOR_PRESETS.index(self.config.detection_mode.color_preset) if self.config.detection_mode.color_preset in COLOR_PRESETS else 0
        self._combo_color_preset.setCurrentIndex(idx)
        self._combo_color_preset.currentIndexChanged.connect(self._on_color_settings_changed)
        self._apply_tooltip(self._combo_color_preset, "color_preset")
        color_lay.addWidget(self._combo_color_preset, 0, 1)

        color_lay.addWidget(QLabel("Min Area (px):"), 1, 0)
        self._spin_color_min = QSpinBox()
        self._spin_color_min.setRange(1, 5000000)
        self._spin_color_min.setSingleStep(50)
        self._spin_color_min.setValue(self.config.detection_mode.color_min_area)
        self._spin_color_min.valueChanged.connect(self._on_color_settings_changed)
        self._apply_tooltip(self._spin_color_min, "color_min_area")
        color_lay.addWidget(self._spin_color_min, 1, 1)

        color_lay.addWidget(QLabel("Max Area (px):"), 2, 0)
        self._spin_color_max = QSpinBox()
        self._spin_color_max.setRange(1, 5000000)
        self._spin_color_max.setSingleStep(1000)
        self._spin_color_max.setValue(self.config.detection_mode.color_max_area)
        self._spin_color_max.valueChanged.connect(self._on_color_settings_changed)
        self._apply_tooltip(self._spin_color_max, "color_max_area")
        color_lay.addWidget(self._spin_color_max, 2, 1)

        self._lbl_color_ratio = QLabel()
        self._set_theme_role(self._lbl_color_ratio, "mutedCompact")
        color_lay.addWidget(self._lbl_color_ratio, 5, 0, 1, 2)

        color_lay.addWidget(QLabel("Fusion Strategy:"), 3, 0)
        self._combo_fusion = QComboBox()
        self._combo_fusion.addItems(["AND", "OR"])
        self._combo_fusion.setCurrentText(self.config.detection_mode.color_fusion_strategy)
        self._combo_fusion.currentTextChanged.connect(self._on_color_settings_changed)
        self._apply_tooltip(self._combo_fusion, "fusion_strategy")
        color_lay.addWidget(self._combo_fusion, 3, 1)

        color_lay.addWidget(QLabel("Fusion Overlap (%):"), 4, 0)
        self._spin_fusion_overlap = QSpinBox()
        self._spin_fusion_overlap.setRange(0, 100)
        self._spin_fusion_overlap.setValue(self.config.detection_mode.color_fusion_overlap)
        self._spin_fusion_overlap.valueChanged.connect(self._on_color_settings_changed)
        self._apply_tooltip(self._spin_fusion_overlap, "fusion_overlap")
        color_lay.addWidget(self._spin_fusion_overlap, 4, 1)

        lay.addWidget(self._grp_color)

        # --- Motion gate threshold (modes 4,5) ---
        self._grp_motion = QGroupBox("Motion Gate")
        motion_lay = QHBoxLayout(self._grp_motion)
        motion_lay.addWidget(QLabel("Threshold (%):"))
        self._spin_motion_thresh = QDoubleSpinBox()
        self._spin_motion_thresh.setRange(0.1, 50.0)
        self._spin_motion_thresh.setSingleStep(0.5)
        self._spin_motion_thresh.setValue(self.config.detection_mode.motion_gate_threshold)
        self._spin_motion_thresh.valueChanged.connect(self._on_detection_settings_changed)
        self._apply_tooltip(self._spin_motion_thresh, "motion_gate_threshold")
        motion_lay.addWidget(self._spin_motion_thresh)
        self._register_responsive_box_layout(motion_lay, "compact_row")

        lay.addWidget(self._grp_motion)

        self._grp_motion_recovery = QGroupBox("Motion Recovery")
        motion_recovery_lay = QHBoxLayout(self._grp_motion_recovery)
        motion_recovery_lay.addWidget(QLabel("Ignore after move (s):"))
        self._spin_motion_ignore = QDoubleSpinBox()
        self._spin_motion_ignore.setRange(0.0, 1.0)
        self._spin_motion_ignore.setSingleStep(0.01)
        self._spin_motion_ignore.setDecimals(2)
        self._spin_motion_ignore.setValue(self.config.detection_mode.motion_ignore_after_move_s)
        self._spin_motion_ignore.valueChanged.connect(self._on_detection_settings_changed)
        self._apply_tooltip(self._spin_motion_ignore, "motion_ignore_after_move_s")
        motion_recovery_lay.addWidget(self._spin_motion_ignore)
        self._register_responsive_box_layout(motion_recovery_lay, "compact_row")
        lay.addWidget(self._grp_motion_recovery)

        lay.addStretch()

        # Initial visibility
        self._update_detection_panel_visibility()
        self._sync_target_size_preset_combo()
        self._set_detection_preset_label(self._match_detection_preset_name())
        return w

    def _build_prompted_targets_tab(self) -> QWidget:
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(6)

        intro = QLabel(
            "Create reusable prompted targets from the live feed, an image, or a video clip. "
            "The saved target library auto-loads and runs alongside the normal detector stack."
        )
        intro.setWordWrap(True)
        self._set_theme_role(intro, "subtleBody")
        lay.addWidget(intro)

        runtime_grp = QGroupBox("Prompted Runtime")
        runtime_lay = QVBoxLayout(runtime_grp)
        self._chk_prompted_enabled = QCheckBox("Enable Prompted Targets")
        self._chk_prompted_enabled.setChecked(bool(self.config.prompted_targets_enabled))
        self._chk_prompted_enabled.toggled.connect(self._on_prompted_settings_changed)
        self._apply_tooltip(self._chk_prompted_enabled, "prompted_enabled")
        runtime_lay.addWidget(self._chk_prompted_enabled)
        self._chk_prompted_auto_fire = QCheckBox("Allow Auto-Fire For Prompted Matches")
        self._chk_prompted_auto_fire.setChecked(bool(self.config.prompted_allow_auto_fire))
        self._chk_prompted_auto_fire.toggled.connect(self._on_prompted_settings_changed)
        self._apply_tooltip(self._chk_prompted_auto_fire, "prompted_auto_fire")
        runtime_lay.addWidget(self._chk_prompted_auto_fire)
        self._chk_prompted_append_selected = QCheckBox("Append imports to selected target")
        self._apply_tooltip(self._chk_prompted_append_selected, "prompted_append_selected")
        runtime_lay.addWidget(self._chk_prompted_append_selected)
        lay.addWidget(runtime_grp)

        naming_grp = QGroupBox("Target Naming")
        naming_lay = QHBoxLayout(naming_grp)
        naming_lay.addWidget(QLabel("Base name:"))
        self._edit_prompted_name = QLineEdit()
        self._edit_prompted_name.setPlaceholderText("Example: Yellow Drill")
        self._apply_tooltip(self._edit_prompted_name, "prompted_name")
        naming_lay.addWidget(self._edit_prompted_name, 1)
        self._register_responsive_box_layout(naming_lay, "compact_row")
        lay.addWidget(naming_grp)

        import_grp = QGroupBox("Create Targets")
        import_lay = QGridLayout(import_grp)
        self._btn_prompted_live = QPushButton("Add From Live")
        self._set_button_role(self._btn_prompted_live, "primary")
        self._btn_prompted_live.clicked.connect(self._toggle_prompted_live_capture)
        self._apply_tooltip(self._btn_prompted_live, "prompted_live")
        import_lay.addWidget(self._btn_prompted_live, 0, 0)
        self._btn_prompted_image = QPushButton("Browse Image")
        self._set_button_role(self._btn_prompted_image, "utility")
        self._btn_prompted_image.clicked.connect(self._browse_prompted_image)
        self._apply_tooltip(self._btn_prompted_image, "prompted_image")
        import_lay.addWidget(self._btn_prompted_image, 0, 1)
        self._btn_prompted_video = QPushButton("Browse Video")
        self._set_button_role(self._btn_prompted_video, "utility")
        self._btn_prompted_video.clicked.connect(self._browse_prompted_video)
        self._apply_tooltip(self._btn_prompted_video, "prompted_video")
        import_lay.addWidget(self._btn_prompted_video, 0, 2)
        self._lbl_prompted_status = QLabel("")
        self._lbl_prompted_status.setWordWrap(True)
        self._set_theme_role(self._lbl_prompted_status, "mutedCompact")
        import_lay.addWidget(self._lbl_prompted_status, 1, 0, 1, 3)
        lay.addWidget(import_grp)

        library_grp = QGroupBox("Prompted Target Library")
        library_lay = QVBoxLayout(library_grp)
        self._prompted_target_list = QListWidget()
        self._prompted_target_list.itemChanged.connect(self._on_prompted_target_item_changed)
        self._prompted_target_list.itemSelectionChanged.connect(self._on_prompted_target_selected)
        self._apply_tooltip(self._prompted_target_list, "prompted_target_list")
        library_lay.addWidget(self._prompted_target_list)

        detail_grid = QGridLayout()
        detail_grid.addWidget(QLabel("Min score:"), 0, 0)
        self._spin_prompted_min_score = QDoubleSpinBox()
        self._spin_prompted_min_score.setDecimals(2)
        self._spin_prompted_min_score.setRange(0.05, 0.99)
        self._spin_prompted_min_score.setSingleStep(0.01)
        self._spin_prompted_min_score.valueChanged.connect(self._on_prompted_profile_settings_changed)
        self._apply_tooltip(self._spin_prompted_min_score, "prompted_min_score")
        detail_grid.addWidget(self._spin_prompted_min_score, 0, 1)

        detail_grid.addWidget(QLabel("Confirm hits:"), 0, 2)
        self._spin_prompted_confirm_hits = QSpinBox()
        self._spin_prompted_confirm_hits.setRange(1, 10)
        self._spin_prompted_confirm_hits.valueChanged.connect(self._on_prompted_profile_settings_changed)
        self._apply_tooltip(self._spin_prompted_confirm_hits, "prompted_confirm_hits")
        detail_grid.addWidget(self._spin_prompted_confirm_hits, 0, 3)

        detail_grid.addWidget(QLabel("Lost timeout:"), 1, 0)
        self._spin_prompted_lost_timeout = QDoubleSpinBox()
        self._spin_prompted_lost_timeout.setDecimals(2)
        self._spin_prompted_lost_timeout.setRange(0.10, 10.0)
        self._spin_prompted_lost_timeout.setSingleStep(0.10)
        self._spin_prompted_lost_timeout.valueChanged.connect(self._on_prompted_profile_settings_changed)
        self._apply_tooltip(self._spin_prompted_lost_timeout, "prompted_lost_timeout")
        detail_grid.addWidget(self._spin_prompted_lost_timeout, 1, 1)

        detail_grid.addWidget(QLabel("Search padding:"), 1, 2)
        self._spin_prompted_search_padding = QSpinBox()
        self._spin_prompted_search_padding.setRange(16, 512)
        self._spin_prompted_search_padding.setSingleStep(8)
        self._spin_prompted_search_padding.valueChanged.connect(self._on_prompted_profile_settings_changed)
        self._apply_tooltip(self._spin_prompted_search_padding, "prompted_search_padding")
        detail_grid.addWidget(self._spin_prompted_search_padding, 1, 3)

        detail_grid.addWidget(QLabel("Global scan every:"), 2, 0)
        self._spin_prompted_global_interval = QSpinBox()
        self._spin_prompted_global_interval.setRange(1, 30)
        self._spin_prompted_global_interval.valueChanged.connect(self._on_prompted_profile_settings_changed)
        self._apply_tooltip(self._spin_prompted_global_interval, "prompted_global_interval")
        detail_grid.addWidget(self._spin_prompted_global_interval, 2, 1)

        self._lbl_prompted_examples = QLabel("Examples: 0")
        detail_grid.addWidget(self._lbl_prompted_examples, 2, 2, 1, 2)
        library_lay.addLayout(detail_grid)

        button_row = QHBoxLayout()
        self._btn_prompted_rename = QPushButton("Rename")
        self._set_button_role(self._btn_prompted_rename, "utility")
        self._btn_prompted_rename.clicked.connect(self._rename_selected_prompted_target)
        self._apply_tooltip(self._btn_prompted_rename, "prompted_rename")
        button_row.addWidget(self._btn_prompted_rename)
        self._btn_prompted_remove_last_example = QPushButton("Remove Last")
        self._set_button_role(self._btn_prompted_remove_last_example, "utility")
        self._btn_prompted_remove_last_example.clicked.connect(self._remove_last_prompted_example)
        self._apply_tooltip(self._btn_prompted_remove_last_example, "prompted_remove_last_example")
        button_row.addWidget(self._btn_prompted_remove_last_example)
        self._btn_prompted_remove = QPushButton("Remove")
        self._set_button_role(self._btn_prompted_remove, "utility")
        self._btn_prompted_remove.clicked.connect(self._remove_selected_prompted_target)
        self._apply_tooltip(self._btn_prompted_remove, "prompted_remove")
        button_row.addWidget(self._btn_prompted_remove)
        self._register_responsive_box_layout(button_row, "action_row")
        library_lay.addLayout(button_row)
        lay.addWidget(library_grp, 1)

        self._rebuild_prompted_target_list()
        return w

    # ------------------------------------------------------------------ #
    #  Target Filter Tab
    # ------------------------------------------------------------------ #

    def _build_filter_tab(self) -> QWidget:
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(4)

        preset_grp = QGroupBox("Target Filter Presets")
        preset_lay = QVBoxLayout(preset_grp)
        preset_lay.setSpacing(4)

        preset_btn_grid = QGridLayout()
        visible_filter_presets = [
            (name, preset)
            for name, preset in TARGET_FILTER_PRESETS.items()
            if not str(name).startswith("custom_")
        ]
        for index, (preset_name, preset) in enumerate(visible_filter_presets):
            btn = QPushButton(preset["label"])
            self._apply_tooltip(btn, preset.get("tooltip_key", ""))
            btn.clicked.connect(lambda _checked=False, name=preset_name: self._apply_filter_preset(name))
            preset_btn_grid.addWidget(btn, index // 2, index % 2)
        self._normalize_preset_grid_button_widths(preset_btn_grid)
        preset_lay.addLayout(preset_btn_grid)

        self._lbl_filter_preset = QLabel("")
        self._lbl_filter_preset.setWordWrap(True)
        self._set_theme_role(self._lbl_filter_preset, "mutedCompact")
        preset_lay.addWidget(self._lbl_filter_preset)
        lay.addWidget(preset_grp)

        # Class whitelist
        grp = QGroupBox("Allowed YOLO Classes")
        g_lay = QVBoxLayout(grp)
        self._class_list = QListWidget()
        self._class_list.setSelectionMode(QAbstractItemView.MultiSelection)
        allowed = set(self.config.target_filter.allowed_classes)
        class_names = list(YOLO_COCO_CLASSES)
        if "rat" not in class_names:
            class_names.append("rat")
        for cls_name in class_names:
            item = QListWidgetItem(cls_name)
            self._class_list.addItem(item)
            if cls_name in allowed:
                item.setSelected(True)
        self._class_list.setMaximumHeight(160)
        self._register_responsive_list(self._class_list, "allowed_classes")
        self._class_list.itemSelectionChanged.connect(self._on_class_selection_changed)
        self._apply_tooltip(self._class_list, "allowed_classes")
        g_lay.addWidget(self._class_list)

        btn_row = QHBoxLayout()
        btn_all = QPushButton("All")
        btn_all.clicked.connect(self._select_all_classes)
        btn_none = QPushButton("None")
        btn_none.clicked.connect(self._select_no_classes)
        self._style_button_row([btn_all, btn_none], "utility")
        self._apply_tooltip(btn_all, "select_all_classes")
        self._apply_tooltip(btn_none, "select_no_classes")
        btn_row.addWidget(btn_all)
        btn_row.addWidget(btn_none)
        g_lay.addLayout(btn_row)
        lay.addWidget(grp)

        # Confidence
        conf_row = QHBoxLayout()
        conf_row.addWidget(QLabel("Min Confidence:"))
        self._spin_min_conf = QDoubleSpinBox()
        self._spin_min_conf.setRange(0.1, 0.99)
        self._spin_min_conf.setSingleStep(0.05)
        self._spin_min_conf.setValue(self.config.target_filter.min_confidence)
        self._spin_min_conf.valueChanged.connect(self._on_filter_changed)
        self._apply_tooltip(self._spin_min_conf, "min_confidence")
        conf_row.addWidget(self._spin_min_conf)
        lay.addLayout(conf_row)

        # Min size ratio
        size_row = QHBoxLayout()
        size_row.addWidget(QLabel("Min Size (%):"))
        self._spin_min_size = QDoubleSpinBox()
        self._spin_min_size.setRange(0.0, 50.0)
        self._spin_min_size.setSingleStep(0.1)
        self._spin_min_size.setDecimals(2)
        self._spin_min_size.setValue(self.config.target_filter.min_size_ratio * 100)
        self._spin_min_size.valueChanged.connect(self._on_filter_changed)
        self._apply_tooltip(self._spin_min_size, "min_size")
        size_row.addWidget(self._spin_min_size)
        lay.addLayout(size_row)

        # Max size ratio
        maxs_row = QHBoxLayout()
        maxs_row.addWidget(QLabel("Max Size (%, 0=none):"))
        self._spin_max_size = QDoubleSpinBox()
        self._spin_max_size.setRange(0.0, 100.0)
        self._spin_max_size.setSingleStep(0.5)
        self._spin_max_size.setDecimals(2)
        self._spin_max_size.setValue(self.config.target_filter.max_size_ratio * 100)
        self._spin_max_size.valueChanged.connect(self._on_filter_changed)
        self._apply_tooltip(self._spin_max_size, "max_size")
        maxs_row.addWidget(self._spin_max_size)
        lay.addLayout(maxs_row)

        lay.addStretch()
        self._set_filter_preset_label(self._match_filter_preset_name())
        return w

    # ------------------------------------------------------------------ #
    #  Threat AI Tab
    # ------------------------------------------------------------------ #

    def _build_scoring_tab(self) -> QWidget:
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(4)

        preset_grp = QGroupBox("Threat Behavior Presets")
        preset_lay = QVBoxLayout(preset_grp)
        preset_lay.setSpacing(4)

        preset_btn_grid = QGridLayout()
        visible_threat_presets = [
            (name, preset)
            for name, preset in THREAT_AI_PRESETS.items()
            if not str(name).startswith("custom_")
        ]
        for index, (preset_name, preset) in enumerate(visible_threat_presets):
            btn = QPushButton(preset["label"])
            self._apply_tooltip(btn, preset.get("tooltip_key", ""))
            btn.clicked.connect(lambda _checked=False, name=preset_name: self._apply_threat_preset(name))
            preset_btn_grid.addWidget(btn, index // 2, index % 2)
        self._normalize_preset_grid_button_widths(preset_btn_grid)
        preset_lay.addLayout(preset_btn_grid)

        self._lbl_threat_preset = QLabel("")
        self._lbl_threat_preset.setWordWrap(True)
        self._set_theme_role(self._lbl_threat_preset, "mutedCompact")
        preset_lay.addWidget(self._lbl_threat_preset)
        lay.addWidget(preset_grp)

        lay.addWidget(QLabel("Threat Score Weights (higher = more important):"))

        self._weight_sliders = {}
        self._weight_value_labels = {}
        weights = [
            ("w_proximity", "Proximity to center", self.config.threat_scoring.w_proximity),
            ("w_size", "Object size", self.config.threat_scoring.w_size),
            ("w_confidence", "Detection confidence", self.config.threat_scoring.w_confidence),
            ("w_class_priority", "Class priority", self.config.threat_scoring.w_class_priority),
            ("w_speed", "Movement speed", self.config.threat_scoring.w_speed),
            ("w_persistence", "Time in frame", self.config.threat_scoring.w_persistence),
            ("w_approach", "Approaching center", self.config.threat_scoring.w_approach),
        ]

        for key, label, default in weights:
            row = QHBoxLayout()
            lbl = QLabel(f"{label}:")
            lbl.setMinimumWidth(120)
            self._register_responsive_label(lbl, "weight_label")
            row.addWidget(lbl)
            slider = QSlider(Qt.Horizontal)
            slider.setRange(0, 100)
            slider.setValue(int(default * 100))
            slider.valueChanged.connect(self._on_scoring_changed)
            weight_tooltip_keys = {
                "w_proximity": "weight_proximity",
                "w_size": "weight_size",
                "w_confidence": "weight_confidence",
                "w_class_priority": "weight_class_priority",
                "w_speed": "weight_speed",
                "w_persistence": "weight_persistence",
                "w_approach": "weight_approach",
            }
            self._apply_tooltip(slider, weight_tooltip_keys.get(key, key))
            row.addWidget(slider)
            val_lbl = QLabel(f"{default:.2f}")
            val_lbl.setMinimumWidth(35)
            self._register_responsive_label(val_lbl, "weight_value")
            slider.valueChanged.connect(lambda v, l=val_lbl: l.setText(f"{v / 100:.2f}"))
            row.addWidget(val_lbl)
            self._weight_sliders[key] = slider
            self._weight_value_labels[key] = val_lbl
            lay.addLayout(row)

        # ML toggle
        self._chk_ml = QCheckBox("Enable ML scoring refinement (requires sklearn)")
        self._chk_ml.setChecked(self.config.threat_scoring.use_ml_model)
        self._chk_ml.toggled.connect(self._on_scoring_changed)
        self._apply_tooltip(self._chk_ml, "ml_refinement")
        lay.addWidget(self._chk_ml)

        # ML training mode toggle
        self._chk_log_ml_training = QCheckBox("Log for ML Training")
        self._chk_log_ml_training.setChecked(False)
        self._chk_log_ml_training.toggled.connect(self._on_ml_training_toggled)
        self._chk_log_ml_training.setToolTip(
            "Enable to capture manual fire events for ML model training. "
            "When enabled, each time you fire, that decision will be logged as training data."
        )
        lay.addWidget(self._chk_log_ml_training)

        # ML training buttons
        ml_btn_lay = QHBoxLayout()
        
        btn_train = QPushButton("Train ML")
        btn_train.clicked.connect(self._train_ml_model)
        btn_train.setToolTip("Train a new ML model from logged engagement decisions")
        ml_btn_lay.addWidget(btn_train)
        
        btn_save = QPushButton("Save ML")
        btn_save.clicked.connect(self._save_ml_model)
        btn_save.setToolTip("Save the trained ML model to disk")
        ml_btn_lay.addWidget(btn_save)
        
        btn_clear = QPushButton("Clear Logs")
        btn_clear.clicked.connect(self._clear_ml_logs)
        btn_clear.setToolTip("Clear all logged engagement data")
        ml_btn_lay.addWidget(btn_clear)
        
        btn_stats = QPushButton("Log Stats")
        btn_stats.clicked.connect(self._show_ml_stats)
        btn_stats.setToolTip("Show summary of logged engagement data")
        ml_btn_lay.addWidget(btn_stats)

        self._btn_open_ml_folder = QPushButton("Open ML Folder")
        self._btn_open_ml_folder.clicked.connect(self._open_ml_data_folder)
        self._btn_open_ml_folder.setToolTip("Open the folder containing saved ML training data or the saved ML model")
        ml_btn_lay.addWidget(self._btn_open_ml_folder)

        self._style_button_row([btn_train], "primary")
        self._style_button_row([btn_save, btn_stats, self._btn_open_ml_folder], "utility")
        self._style_button_row([btn_clear], "danger")

        ml_btn_lay.addStretch()
        
        lay.addLayout(ml_btn_lay)

        self._lbl_ml_status = QLabel("")
        self._lbl_ml_status.setWordWrap(True)
        self._set_theme_role(self._lbl_ml_status, "mutedCompact")
        lay.addWidget(self._lbl_ml_status)

        self._lbl_ml_description = QLabel(
            "How it works: the hand-tuned threat score always runs first. Optional ML refinement only changes final ranking after "
            "a trained model exists and ML refinement is enabled. 'Log for ML Training' currently records manual fire decisions to "
            "config/ml_training_data.json. After enough records are collected, click Train ML, then Save ML, then enable ML scoring refinement."
        )
        self._lbl_ml_description.setWordWrap(True)
        self._set_theme_role(self._lbl_ml_description, "mutedCompact")
        lay.addWidget(self._lbl_ml_description)

        self._refresh_ml_feature_status()

        self._set_threat_preset_label(self._match_threat_preset_name())

        lay.addStretch()
        return w

    # ------------------------------------------------------------------ #
    #  Engagement Tab
    # ------------------------------------------------------------------ #

    def _build_engagement_tab(self) -> QWidget:
        """CHANGE WARNING: Engagement preset controls here feed directly into live fire-gate tolerances; keep compact UI changes wired to the same preset application methods rather than duplicating tolerance logic."""
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(4)

        preset_grp = QGroupBox("Engagement Behavior Presets")
        preset_lay = QVBoxLayout(preset_grp)
        preset_lay.setSpacing(4)

        preset_btn_grid = QGridLayout()
        visible_engage_presets = [
            (name, preset)
            for name, preset in ENGAGEMENT_PRESETS.items()
            if not str(name).startswith("custom_")
        ]
        for index, (preset_name, preset) in enumerate(visible_engage_presets):
            btn = QPushButton(preset["label"])
            self._apply_tooltip(btn, preset.get("tooltip_key", ""))
            btn.clicked.connect(lambda _checked=False, name=preset_name: self._apply_engagement_preset(name))
            preset_btn_grid.addWidget(btn, index // 2, index % 2)
        self._normalize_preset_grid_button_widths(preset_btn_grid)
        preset_lay.addLayout(preset_btn_grid)

        self._lbl_engagement_preset = QLabel("")
        self._lbl_engagement_preset.setWordWrap(True)
        self._set_theme_role(self._lbl_engagement_preset, "mutedCompact")
        preset_lay.addWidget(self._lbl_engagement_preset)
        lay.addWidget(preset_grp)

        # Auto-Trigger toggle (prominent)
        self._chk_auto_trigger = QCheckBox("Auto-Trigger")
        self._set_theme_role(self._chk_auto_trigger, "headlineToggle")
        self._chk_auto_trigger.setChecked(self.config.engagement.auto_trigger_enabled)
        self._chk_auto_trigger.toggled.connect(self._on_auto_trigger_toggled)
        self._apply_tooltip(self._chk_auto_trigger, "auto_trigger")
        lay.addWidget(self._chk_auto_trigger)

        # Trigger mode
        trig_row = QHBoxLayout()
        trig_row.addWidget(QLabel("Trigger Mode:"))
        self._combo_trigger_mode = QComboBox()
        self._compact_combo_box(self._combo_trigger_mode, minimum_chars=16)
        self._combo_trigger_mode.addItems(["Water (MOSFET)", "Projectile (GPIO13 Servo)"])
        self._combo_trigger_mode.setCurrentIndex(1 if self.config.engagement.trigger_mode_bb else 0)
        self._combo_trigger_mode.currentIndexChanged.connect(self._on_trigger_mode_changed)
        self._apply_tooltip(self._combo_trigger_mode, "trigger_mode")
        trig_row.addWidget(self._combo_trigger_mode)
        lay.addLayout(trig_row)

        self._grp_trigger_servo = QGroupBox("Projectile Trigger Servo")
        trigger_servo_lay = QGridLayout(self._grp_trigger_servo)
        trigger_servo_lay.setHorizontalSpacing(6)
        trigger_servo_lay.setVerticalSpacing(4)

        trigger_servo_lay.addWidget(QLabel("Rest angle:"), 0, 0)
        self._spin_trigger_servo_rest_deg = QSpinBox()
        self._spin_trigger_servo_rest_deg.setRange(0, 180)
        self._spin_trigger_servo_rest_deg.setValue(int(getattr(self.config.engagement, "trigger_servo_rest_deg", 0)))
        self._spin_trigger_servo_rest_deg.valueChanged.connect(self._on_trigger_servo_settings_changed)
        self._apply_tooltip(self._spin_trigger_servo_rest_deg, "trigger_servo_rest_deg")
        trigger_servo_lay.addWidget(self._spin_trigger_servo_rest_deg, 0, 1)

        trigger_servo_lay.addWidget(QLabel("Fire angle:"), 0, 2)
        self._spin_trigger_servo_fire_deg = QSpinBox()
        self._spin_trigger_servo_fire_deg.setRange(0, 180)
        self._spin_trigger_servo_fire_deg.setValue(int(getattr(self.config.engagement, "trigger_servo_fire_deg", 45)))
        self._spin_trigger_servo_fire_deg.valueChanged.connect(self._on_trigger_servo_settings_changed)
        self._apply_tooltip(self._spin_trigger_servo_fire_deg, "trigger_servo_fire_deg")
        trigger_servo_lay.addWidget(self._spin_trigger_servo_fire_deg, 0, 3)

        trigger_servo_lay.addWidget(QLabel("Speed (deg/s):"), 1, 0)
        self._spin_trigger_servo_speed_dps = QSpinBox()
        self._spin_trigger_servo_speed_dps.setRange(10, 5000)
        self._spin_trigger_servo_speed_dps.setSingleStep(10)
        self._spin_trigger_servo_speed_dps.setValue(int(getattr(self.config.engagement, "trigger_servo_speed_dps", 360)))
        self._spin_trigger_servo_speed_dps.valueChanged.connect(self._on_trigger_servo_settings_changed)
        self._apply_tooltip(self._spin_trigger_servo_speed_dps, "trigger_servo_speed_dps")
        trigger_servo_lay.addWidget(self._spin_trigger_servo_speed_dps, 1, 1)

        self._lbl_trigger_travel = QLabel("")
        self._set_theme_role(self._lbl_trigger_travel, "statusMeta")
        trigger_servo_lay.addWidget(self._lbl_trigger_travel, 1, 2, 1, 2)

        self._lbl_trigger_servo_status = QLabel("Trigger-servo path: waiting for bridge capability packet")
        self._lbl_trigger_servo_status.setWordWrap(True)
        self._set_theme_role(self._lbl_trigger_servo_status, "statusStrong")
        trigger_servo_lay.addWidget(self._lbl_trigger_servo_status, 2, 0, 1, 4)

        lay.addWidget(self._grp_trigger_servo)
        self._refresh_trigger_servo_summary()

        # Min threat to engage
        row = QHBoxLayout()
        row.addWidget(QLabel("Min threat to engage:"))
        self._spin_min_threat = QDoubleSpinBox()
        self._spin_min_threat.setRange(0.05, 0.95)
        self._spin_min_threat.setSingleStep(0.05)
        self._spin_min_threat.setValue(self.config.engagement.min_threat_score)
        self._spin_min_threat.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_min_threat, "min_threat")
        row.addWidget(self._spin_min_threat)
        lay.addLayout(row)

        # Burst count
        row2 = QHBoxLayout()
        row2.addWidget(QLabel("Burst shots:"))
        self._spin_burst = QSpinBox()
        self._spin_burst.setRange(1, 10)
        self._spin_burst.setValue(self.config.engagement.burst_count)
        self._spin_burst.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_burst, "burst_shots")
        row2.addWidget(self._spin_burst)
        lay.addLayout(row2)

        # Burst interval
        row3 = QHBoxLayout()
        row3.addWidget(QLabel("Burst interval (ms):"))
        self._spin_burst_interval = QSpinBox()
        self._spin_burst_interval.setRange(20, 500)
        self._spin_burst_interval.setSingleStep(10)
        self._spin_burst_interval.setValue(self.config.engagement.burst_interval_ms)
        self._spin_burst_interval.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_burst_interval, "burst_interval")
        row3.addWidget(self._spin_burst_interval)
        lay.addLayout(row3)

        # Inter-target cooldown
        row4 = QHBoxLayout()
        row4.addWidget(QLabel("Target cooldown (s):"))
        self._spin_inter_cd = QDoubleSpinBox()
        self._spin_inter_cd.setRange(0.1, 5.0)
        self._spin_inter_cd.setSingleStep(0.1)
        self._spin_inter_cd.setValue(self.config.engagement.inter_target_cooldown)
        self._spin_inter_cd.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_inter_cd, "inter_target_cooldown")
        row4.addWidget(self._spin_inter_cd)
        lay.addLayout(row4)

        # Cycle cooldown
        row5 = QHBoxLayout()
        row5.addWidget(QLabel("Cycle cooldown (s):"))
        self._spin_cycle_cd = QDoubleSpinBox()
        self._spin_cycle_cd.setRange(0.5, 30.0)
        self._spin_cycle_cd.setSingleStep(0.5)
        self._spin_cycle_cd.setValue(self.config.engagement.cycle_cooldown)
        self._spin_cycle_cd.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_cycle_cd, "cycle_cooldown")
        row5.addWidget(self._spin_cycle_cd)
        lay.addLayout(row5)

        # Max queue
        row6 = QHBoxLayout()
        self._lbl_max_queue = QLabel("Max targets/cycle:")
        row6.addWidget(self._lbl_max_queue)
        self._spin_max_queue = QSpinBox()
        self._spin_max_queue.setRange(1, 10)
        self._spin_max_queue.setValue(self.config.engagement.max_queue_length)
        self._spin_max_queue.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_max_queue, "max_targets_per_cycle")
        row6.addWidget(self._spin_max_queue)
        lay.addLayout(row6)

        # Optimize slew
        self._chk_optimize = QCheckBox("Optimise travel order")
        self._chk_optimize.setChecked(self.config.engagement.optimize_slew_order)
        self._chk_optimize.toggled.connect(self._on_engagement_changed)
        self._apply_tooltip(self._chk_optimize, "optimize_travel")
        lay.addWidget(self._chk_optimize)
        self._sync_single_target_ui()

        # Engagement speed
        row7 = QHBoxLayout()
        row7.addWidget(QLabel("Engagement speed:"))
        self._slider_speed = QSlider(Qt.Horizontal)
        self._slider_speed.setRange(10, 100)
        self._slider_speed.setValue(self.config.engagement.engagement_speed)
        self._slider_speed.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._slider_speed, "engagement_speed")
        row7.addWidget(self._slider_speed)
        self._lbl_speed = QLabel(str(self.config.engagement.engagement_speed))
        self._slider_speed.valueChanged.connect(lambda v: self._lbl_speed.setText(str(v)))
        row7.addWidget(self._lbl_speed)
        lay.addLayout(row7)

        # --- Precision Aiming ---
        prec_grp = QGroupBox("Precision Aiming (small/distant targets)")
        prec_lay = QGridLayout(prec_grp)

        self._chk_precision = QCheckBox("Precision refinement")
        self._chk_precision.setChecked(self.config.engagement.precision_aim_enabled)
        self._chk_precision.toggled.connect(self._on_engagement_changed)
        self._apply_tooltip(self._chk_precision, "precision_enable")
        prec_lay.addWidget(self._chk_precision, 0, 0, 1, 2)

        prec_lay.addWidget(QLabel("Settle time (s):"), 1, 0)
        self._spin_prec_settle = QDoubleSpinBox()
        self._spin_prec_settle.setRange(0.1, 3.0)
        self._spin_prec_settle.setSingleStep(0.1)
        self._spin_prec_settle.setValue(self.config.engagement.precision_settle_time)
        self._spin_prec_settle.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_prec_settle, "precision_settle")
        prec_lay.addWidget(self._spin_prec_settle, 1, 1)

        prec_lay.addWidget(QLabel("Max step (deg):"), 2, 0)
        self._spin_prec_step = QDoubleSpinBox()
        self._spin_prec_step.setRange(0.1, 5.0)
        self._spin_prec_step.setSingleStep(0.1)
        self._spin_prec_step.setValue(self.config.engagement.precision_max_step)
        self._spin_prec_step.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_prec_step, "precision_step")
        prec_lay.addWidget(self._spin_prec_step, 2, 1)

        lay.addWidget(prec_grp)

        advanced_grp = QGroupBox("Advanced Aim Lock And Fire Gate")
        advanced_lay = QGridLayout(advanced_grp)

        preset_row = QHBoxLayout()
        preset_row.addWidget(QLabel("Preset:"))
        self._combo_aim_gate_preset = QComboBox()
        self._compact_combo_box(self._combo_aim_gate_preset, minimum_chars=18)
        for preset_name, preset in AIM_LOCK_FIRE_GATE_PRESETS.items():
            self._combo_aim_gate_preset.addItem(str(preset["label"]), preset_name)
        self._apply_tooltip(self._combo_aim_gate_preset, "aim_gate_preset_combo")
        preset_row.addWidget(self._combo_aim_gate_preset, 1)

        btn_apply_aim_gate_preset = QPushButton("Apply Preset")
        self._set_button_role(btn_apply_aim_gate_preset, "utility")
        btn_apply_aim_gate_preset.clicked.connect(self._apply_selected_aim_lock_fire_gate_preset)
        self._apply_tooltip(btn_apply_aim_gate_preset, "aim_gate_preset_combo")
        preset_row.addWidget(btn_apply_aim_gate_preset)
        preset_row.addStretch(1)
        advanced_lay.addLayout(preset_row, 0, 0, 1, 2)

        advanced_lay.addWidget(QLabel("Deadzone Pan / Tilt (deg):"), 1, 0)
        deadzone_row = QHBoxLayout()
        self._spin_deadzone_pan = QDoubleSpinBox()
        self._spin_deadzone_pan.setRange(0.0, 3.0)
        self._spin_deadzone_pan.setSingleStep(0.01)
        self._spin_deadzone_pan.setDecimals(2)
        self._spin_deadzone_pan.setValue(self.config.engagement.precision_deadzone_pan_deg)
        self._spin_deadzone_pan.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_deadzone_pan, "precision_deadzone_pan")
        deadzone_row.addWidget(self._spin_deadzone_pan)
        self._spin_deadzone_tilt = QDoubleSpinBox()
        self._spin_deadzone_tilt.setRange(0.0, 3.0)
        self._spin_deadzone_tilt.setSingleStep(0.01)
        self._spin_deadzone_tilt.setDecimals(2)
        self._spin_deadzone_tilt.setValue(self.config.engagement.precision_deadzone_tilt_deg)
        self._spin_deadzone_tilt.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_deadzone_tilt, "precision_deadzone_tilt")
        deadzone_row.addWidget(self._spin_deadzone_tilt)
        advanced_lay.addLayout(deadzone_row, 1, 1)

        advanced_lay.addWidget(QLabel("Error EMA:"), 2, 0)
        self._spin_error_ema = QDoubleSpinBox()
        self._spin_error_ema.setRange(0.0, 1.0)
        self._spin_error_ema.setSingleStep(0.05)
        self._spin_error_ema.setDecimals(2)
        self._spin_error_ema.setValue(self.config.engagement.precision_error_ema)
        self._spin_error_ema.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_error_ema, "precision_error_ema")
        advanced_lay.addWidget(self._spin_error_ema, 2, 1)

        advanced_lay.addWidget(QLabel("Aim lock Pan / Tilt (deg):"), 3, 0)
        aim_lock_row = QHBoxLayout()
        self._spin_aim_lock_pan = QDoubleSpinBox()
        self._spin_aim_lock_pan.setRange(0.1, 5.0)
        self._spin_aim_lock_pan.setSingleStep(0.05)
        self._spin_aim_lock_pan.setDecimals(2)
        self._spin_aim_lock_pan.setValue(self.config.engagement.aim_lock_pan_tolerance)
        self._spin_aim_lock_pan.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_aim_lock_pan, "aim_lock_pan_tolerance")
        aim_lock_row.addWidget(self._spin_aim_lock_pan)
        self._spin_aim_lock_tilt = QDoubleSpinBox()
        self._spin_aim_lock_tilt.setRange(0.1, 5.0)
        self._spin_aim_lock_tilt.setSingleStep(0.05)
        self._spin_aim_lock_tilt.setDecimals(2)
        self._spin_aim_lock_tilt.setValue(self.config.engagement.aim_lock_tilt_tolerance)
        self._spin_aim_lock_tilt.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_aim_lock_tilt, "aim_lock_tilt_tolerance")
        aim_lock_row.addWidget(self._spin_aim_lock_tilt)
        advanced_lay.addLayout(aim_lock_row, 3, 1)

        advanced_lay.addWidget(QLabel("Aim lock frames:"), 4, 0)
        self._spin_aim_lock_frames = QSpinBox()
        self._spin_aim_lock_frames.setRange(1, 20)
        self._spin_aim_lock_frames.setValue(self.config.engagement.aim_lock_required_frames)
        self._spin_aim_lock_frames.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_aim_lock_frames, "aim_lock_required_frames")
        advanced_lay.addWidget(self._spin_aim_lock_frames, 4, 1)

        advanced_lay.addWidget(QLabel("Fire enter Pan / Tilt (deg):"), 5, 0)
        fire_enter_row = QHBoxLayout()
        self._spin_fire_enter_pan = QDoubleSpinBox()
        self._spin_fire_enter_pan.setRange(0.05, 5.0)
        self._spin_fire_enter_pan.setSingleStep(0.02)
        self._spin_fire_enter_pan.setDecimals(2)
        self._spin_fire_enter_pan.setValue(self.config.engagement.fire_trigger_enter_pan_tolerance)
        self._spin_fire_enter_pan.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_fire_enter_pan, "fire_trigger_enter_pan")
        fire_enter_row.addWidget(self._spin_fire_enter_pan)
        self._spin_fire_enter_tilt = QDoubleSpinBox()
        self._spin_fire_enter_tilt.setRange(0.05, 5.0)
        self._spin_fire_enter_tilt.setSingleStep(0.02)
        self._spin_fire_enter_tilt.setDecimals(2)
        self._spin_fire_enter_tilt.setValue(self.config.engagement.fire_trigger_enter_tilt_tolerance)
        self._spin_fire_enter_tilt.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_fire_enter_tilt, "fire_trigger_enter_tilt")
        fire_enter_row.addWidget(self._spin_fire_enter_tilt)
        advanced_lay.addLayout(fire_enter_row, 5, 1)

        advanced_lay.addWidget(QLabel("Center fire radius (deg):"), 6, 0)
        center_radius_row = QVBoxLayout()

        center_radius_edit_row = QHBoxLayout()
        self._spin_center_fire_radius = QDoubleSpinBox()
        self._spin_center_fire_radius.setRange(0.02, 1.00)
        self._spin_center_fire_radius.setSingleStep(0.01)
        self._spin_center_fire_radius.setDecimals(3)
        self._spin_center_fire_radius.setValue(
            max(0.02, min(1.0, (self.config.engagement.fire_trigger_enter_pan_tolerance + self.config.engagement.fire_trigger_enter_tilt_tolerance) * 0.5))
        )
        self._apply_tooltip(self._spin_center_fire_radius, "center_fire_radius")
        center_radius_edit_row.addWidget(self._spin_center_fire_radius)

        btn_apply_center_radius = QPushButton("Apply Radius")
        self._set_button_role(btn_apply_center_radius, "utility")
        btn_apply_center_radius.clicked.connect(self._on_apply_center_fire_radius)
        self._apply_tooltip(btn_apply_center_radius, "center_fire_radius")
        center_radius_edit_row.addWidget(btn_apply_center_radius)
        center_radius_row.addLayout(center_radius_edit_row)

        center_radius_preset_row = QHBoxLayout()
        self._combo_center_radius_preset = QComboBox()
        self._compact_combo_box(self._combo_center_radius_preset, minimum_chars=18)
        self._combo_center_radius_preset.addItem("Sniper Small", "small")
        self._combo_center_radius_preset.addItem("Sniper Medium", "medium")
        self._combo_center_radius_preset.addItem("Sniper Large", "large")
        self._apply_tooltip(self._combo_center_radius_preset, "center_fire_radius_profile")
        center_radius_preset_row.addWidget(self._combo_center_radius_preset, 1)

        btn_apply_center_radius_preset = QPushButton("Load Sniper Preset")
        self._set_button_role(btn_apply_center_radius_preset, "utility")
        btn_apply_center_radius_preset.clicked.connect(self._apply_selected_center_radius_profile)
        self._apply_tooltip(btn_apply_center_radius_preset, "center_fire_radius_profile")
        center_radius_preset_row.addWidget(btn_apply_center_radius_preset)
        center_radius_row.addLayout(center_radius_preset_row)

        self._style_button_row([btn_apply_center_radius, btn_apply_aim_gate_preset, btn_apply_center_radius_preset], "utility")
        advanced_lay.addLayout(center_radius_row, 6, 1)

        self._lbl_center_fire_radius_hint = QLabel("")
        self._lbl_center_fire_radius_hint.setWordWrap(True)
        self._set_theme_role(self._lbl_center_fire_radius_hint, "mutedCompact")
        advanced_lay.addWidget(self._lbl_center_fire_radius_hint, 7, 0, 1, 2)

        advanced_lay.addWidget(QLabel("Fire exit Pan / Tilt (deg):"), 8, 0)
        fire_exit_row = QHBoxLayout()
        self._spin_fire_exit_pan = QDoubleSpinBox()
        self._spin_fire_exit_pan.setRange(0.05, 5.0)
        self._spin_fire_exit_pan.setSingleStep(0.02)
        self._spin_fire_exit_pan.setDecimals(2)
        self._spin_fire_exit_pan.setValue(self.config.engagement.fire_trigger_exit_pan_tolerance)
        self._spin_fire_exit_pan.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_fire_exit_pan, "fire_trigger_exit_pan")
        fire_exit_row.addWidget(self._spin_fire_exit_pan)
        self._spin_fire_exit_tilt = QDoubleSpinBox()
        self._spin_fire_exit_tilt.setRange(0.05, 5.0)
        self._spin_fire_exit_tilt.setSingleStep(0.02)
        self._spin_fire_exit_tilt.setDecimals(2)
        self._spin_fire_exit_tilt.setValue(self.config.engagement.fire_trigger_exit_tilt_tolerance)
        self._spin_fire_exit_tilt.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_fire_exit_tilt, "fire_trigger_exit_tilt")
        fire_exit_row.addWidget(self._spin_fire_exit_tilt)
        advanced_lay.addLayout(fire_exit_row, 8, 1)

        advanced_lay.addWidget(QLabel("Recenter Pan / Tilt (deg):"), 9, 0)
        recenter_row = QHBoxLayout()
        self._spin_recenter_pan = QDoubleSpinBox()
        self._spin_recenter_pan.setRange(0.1, 5.0)
        self._spin_recenter_pan.setSingleStep(0.05)
        self._spin_recenter_pan.setDecimals(2)
        self._spin_recenter_pan.setValue(self.config.engagement.fire_recenter_pan_tolerance)
        self._spin_recenter_pan.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_recenter_pan, "fire_recenter_pan")
        recenter_row.addWidget(self._spin_recenter_pan)
        self._spin_recenter_tilt = QDoubleSpinBox()
        self._spin_recenter_tilt.setRange(0.1, 5.0)
        self._spin_recenter_tilt.setSingleStep(0.05)
        self._spin_recenter_tilt.setDecimals(2)
        self._spin_recenter_tilt.setValue(self.config.engagement.fire_recenter_tilt_tolerance)
        self._spin_recenter_tilt.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_recenter_tilt, "fire_recenter_tilt")
        recenter_row.addWidget(self._spin_recenter_tilt)
        advanced_lay.addLayout(recenter_row, 9, 1)

        advanced_lay.addWidget(QLabel("Target loss timeout (s):"), 10, 0)
        self._spin_target_loss_timeout = QDoubleSpinBox()
        self._spin_target_loss_timeout.setRange(0.10, 10.0)
        self._spin_target_loss_timeout.setSingleStep(0.05)
        self._spin_target_loss_timeout.setDecimals(2)
        self._spin_target_loss_timeout.setValue(self.config.engagement.target_loss_timeout)
        self._spin_target_loss_timeout.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_target_loss_timeout, "target_loss_timeout")
        advanced_lay.addWidget(self._spin_target_loss_timeout, 10, 1)

        advanced_lay.addWidget(QLabel("Continuous hunt on loss:"), 11, 0)
        self._chk_continuous_hunt_loss = QCheckBox("Keep hunting on loss")
        self._chk_continuous_hunt_loss.setChecked(bool(getattr(self.config.engagement, "continuous_hunt_on_loss", False)))
        self._chk_continuous_hunt_loss.toggled.connect(self._on_engagement_changed)
        self._apply_tooltip(self._chk_continuous_hunt_loss, "continuous_hunt_on_loss")
        advanced_lay.addWidget(self._chk_continuous_hunt_loss, 11, 1)

        after_loss_grp = QGroupBox("After Target Loss")
        after_loss_lay = QGridLayout(after_loss_grp)
        after_loss_lay.addWidget(QLabel("Adaptive search:"), 0, 0)
        self._chk_adaptive_loss_recovery = QCheckBox("Enable adaptive after-loss search")
        self._chk_adaptive_loss_recovery.setChecked(bool(getattr(self.config.engagement, "adaptive_loss_recovery_enabled", True)))
        self._chk_adaptive_loss_recovery.toggled.connect(self._on_engagement_changed)
        after_loss_lay.addWidget(self._chk_adaptive_loss_recovery, 0, 1, 1, 2)

        after_loss_lay.addWidget(QLabel("Search style (loss + PIR):"), 1, 0)
        self._combo_loss_search_style = QComboBox()
        self._combo_loss_search_style.addItem("Hunting", "hunting")
        self._combo_loss_search_style.addItem("Fast Reacquire", "fast_reacquire")
        loss_style = str(getattr(self.config.engagement, "loss_search_style", getattr(self.config.pir_guard, "search_style", "hunting")) or "hunting")
        loss_style_index = max(0, self._combo_loss_search_style.findData(loss_style))
        self._combo_loss_search_style.setCurrentIndex(loss_style_index)
        self._combo_loss_search_style.currentIndexChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._combo_loss_search_style, "loss_search_style")
        after_loss_lay.addWidget(self._combo_loss_search_style, 1, 1)

        after_loss_lay.addWidget(QLabel("Hunt rounds (loss + PIR):"), 1, 2)
        self._spin_loss_search_rounds = QSpinBox()
        self._spin_loss_search_rounds.setRange(1, 4)
        self._spin_loss_search_rounds.setValue(int(getattr(self.config.engagement, "loss_search_rounds", getattr(self.config.pir_guard, "search_rounds", 1)) or 1))
        self._spin_loss_search_rounds.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_loss_search_rounds, "loss_search_rounds")
        after_loss_lay.addWidget(self._spin_loss_search_rounds, 1, 3)

        after_loss_lay.addWidget(QLabel("Quick handoff pursuit (s):"), 2, 0)
        self._spin_loss_handoff_pursuit = QDoubleSpinBox()
        self._spin_loss_handoff_pursuit.setRange(0.05, 1.50)
        self._spin_loss_handoff_pursuit.setSingleStep(0.01)
        self._spin_loss_handoff_pursuit.setDecimals(2)
        self._spin_loss_handoff_pursuit.setValue(float(getattr(self.config.engagement, "loss_handoff_pursuit_time_s", 0.14)))
        self._spin_loss_handoff_pursuit.valueChanged.connect(self._on_engagement_changed)
        after_loss_lay.addWidget(self._spin_loss_handoff_pursuit, 2, 1)

        after_loss_lay.addWidget(QLabel("Back-off pan / tilt step (deg):"), 3, 0)
        loss_handoff_row = QHBoxLayout()
        self._spin_loss_handoff_backoff = QDoubleSpinBox()
        self._spin_loss_handoff_backoff.setRange(0.20, 8.0)
        self._spin_loss_handoff_backoff.setSingleStep(0.10)
        self._spin_loss_handoff_backoff.setDecimals(2)
        self._spin_loss_handoff_backoff.setValue(float(getattr(self.config.engagement, "loss_handoff_backoff_pan_deg", 1.4)))
        self._spin_loss_handoff_backoff.valueChanged.connect(self._on_engagement_changed)
        loss_handoff_row.addWidget(self._spin_loss_handoff_backoff)
        self._spin_loss_handoff_tilt = QDoubleSpinBox()
        self._spin_loss_handoff_tilt.setRange(0.10, 5.0)
        self._spin_loss_handoff_tilt.setSingleStep(0.05)
        self._spin_loss_handoff_tilt.setDecimals(2)
        self._spin_loss_handoff_tilt.setValue(float(getattr(self.config.engagement, "loss_handoff_tilt_step_deg", 0.9)))
        self._spin_loss_handoff_tilt.valueChanged.connect(self._on_engagement_changed)
        loss_handoff_row.addWidget(self._spin_loss_handoff_tilt)
        after_loss_lay.addLayout(loss_handoff_row, 3, 1)

        after_loss_lay.addWidget(QLabel("Sparse / crowded retry passes:"), 4, 0)
        loss_retry_row = QHBoxLayout()
        self._spin_loss_retry_sparse = QSpinBox()
        self._spin_loss_retry_sparse.setRange(1, 6)
        self._spin_loss_retry_sparse.setValue(int(getattr(self.config.engagement, "loss_persistent_retry_passes_sparse", 2)))
        self._spin_loss_retry_sparse.valueChanged.connect(self._on_engagement_changed)
        loss_retry_row.addWidget(self._spin_loss_retry_sparse)
        self._spin_loss_retry_crowded = QSpinBox()
        self._spin_loss_retry_crowded.setRange(1, 6)
        self._spin_loss_retry_crowded.setValue(int(getattr(self.config.engagement, "loss_persistent_retry_passes_crowded", 1)))
        self._spin_loss_retry_crowded.valueChanged.connect(self._on_engagement_changed)
        loss_retry_row.addWidget(self._spin_loss_retry_crowded)
        after_loss_lay.addLayout(loss_retry_row, 4, 1)

        after_loss_lay.addWidget(QLabel("Switch margin / crowd threshold:"), 5, 0)
        loss_switch_row = QHBoxLayout()
        self._spin_loss_switch_margin = QDoubleSpinBox()
        self._spin_loss_switch_margin.setRange(0.00, 1.00)
        self._spin_loss_switch_margin.setSingleStep(0.01)
        self._spin_loss_switch_margin.setDecimals(2)
        self._spin_loss_switch_margin.setValue(float(getattr(self.config.engagement, "loss_switch_score_margin", 0.12)))
        self._spin_loss_switch_margin.valueChanged.connect(self._on_engagement_changed)
        loss_switch_row.addWidget(self._spin_loss_switch_margin)
        self._spin_loss_crowd_threshold = QSpinBox()
        self._spin_loss_crowd_threshold.setRange(1, 8)
        self._spin_loss_crowd_threshold.setValue(int(getattr(self.config.engagement, "loss_scene_crowding_threshold", 3)))
        self._spin_loss_crowd_threshold.valueChanged.connect(self._on_engagement_changed)
        loss_switch_row.addWidget(self._spin_loss_crowd_threshold)
        after_loss_lay.addLayout(loss_switch_row, 5, 1)

        after_loss_lay.addWidget(QLabel("Personality intensity / velocity bias:"), 6, 0)
        loss_personality_row = QHBoxLayout()
        self._spin_loss_personality = QDoubleSpinBox()
        self._spin_loss_personality.setRange(0.00, 1.00)
        self._spin_loss_personality.setSingleStep(0.05)
        self._spin_loss_personality.setDecimals(2)
        self._spin_loss_personality.setValue(float(getattr(self.config.engagement, "loss_personality_intensity", 0.35)))
        self._spin_loss_personality.valueChanged.connect(self._on_engagement_changed)
        loss_personality_row.addWidget(self._spin_loss_personality)
        self._spin_loss_velocity_bias = QDoubleSpinBox()
        self._spin_loss_velocity_bias.setRange(0.00, 1.00)
        self._spin_loss_velocity_bias.setSingleStep(0.05)
        self._spin_loss_velocity_bias.setDecimals(2)
        self._spin_loss_velocity_bias.setValue(float(getattr(self.config.engagement, "loss_personality_velocity_bias", 0.40)))
        self._spin_loss_velocity_bias.valueChanged.connect(self._on_engagement_changed)
        loss_personality_row.addWidget(self._spin_loss_velocity_bias)
        after_loss_lay.addLayout(loss_personality_row, 6, 1)

        advanced_lay.addWidget(after_loss_grp, 12, 0, 1, 2)

        self._update_center_fire_radius_hint()

        lay.addWidget(advanced_grp)

        self._set_engagement_preset_label(self._match_engagement_preset_name())
        tuning_grp = QGroupBox("Precision Tuning Data Logger")
        tuning_lay = QVBoxLayout(tuning_grp)
        self._chk_precision_logging = QCheckBox("Precision tuning logger")
        self._chk_precision_logging.setChecked(False)
        self._chk_precision_logging.toggled.connect(self._on_precision_logging_toggled)
        tuning_lay.addWidget(self._chk_precision_logging)
        export_row = QHBoxLayout()
        btn_export_csv = QPushButton("Export CSV")
        btn_export_csv.clicked.connect(self._on_export_precision_csv)
        export_row.addWidget(btn_export_csv)
        btn_export_json = QPushButton("Export JSON")
        btn_export_json.clicked.connect(self._on_export_precision_json)
        export_row.addWidget(btn_export_json)
        btn_summary = QPushButton("Print Summary")
        btn_summary.clicked.connect(self._on_print_precision_summary)
        export_row.addWidget(btn_summary)
        self._style_button_row([btn_export_csv, btn_export_json, btn_summary], "utility")
        tuning_lay.addLayout(export_row)
        lay.addWidget(tuning_grp)

        self._update_size_ratio_hints()

        lay.addStretch()
        return w

    # ------------------------------------------------------------------ #
    #  Guard Position Tab
    # ------------------------------------------------------------------ #

    def _build_guard_tab(self) -> QWidget:
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(4)

        # --- Guard mode selector ---
        mode_row = QHBoxLayout()
        mode_row.addWidget(QLabel("Guard Mode:"))
        self._combo_guard_mode = QComboBox()
        self._combo_guard_mode.addItems([
            "Static (Fixed Position)",
            "Slow Sweep (Pan L↔R)",
            "Waypoint Patrol",
            "Random Scan",
        ])
        self._combo_guard_mode.setCurrentIndex(self.config.guard.guard_mode)
        self._combo_guard_mode.currentIndexChanged.connect(self._on_guard_mode_changed)
        self._apply_tooltip(self._combo_guard_mode, "guard_mode")
        mode_row.addWidget(self._combo_guard_mode)
        lay.addLayout(mode_row)

        # --- Static guard position (always visible) ---
        static_grp = QGroupBox("Guard Position (Home)")
        static_lay = QVBoxLayout(static_grp)
        static_lay.setSpacing(3)

        row = QHBoxLayout()
        row.addWidget(QLabel("Guard Pan (deg):"))
        self._spin_guard_pan = QDoubleSpinBox()
        self._spin_guard_pan.setRange(SENTRY_PAN_MIN, SENTRY_PAN_MAX)
        self._spin_guard_pan.setSingleStep(1.0)
        self._spin_guard_pan.setValue(self.config.guard.guard_pan)
        self._spin_guard_pan.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_guard_pan, "guard_pan")
        row.addWidget(self._spin_guard_pan)
        static_lay.addLayout(row)

        row2 = QHBoxLayout()
        row2.addWidget(QLabel("Guard Tilt (deg):"))
        self._spin_guard_tilt = QDoubleSpinBox()
        self._spin_guard_tilt.setRange(SENTRY_TILT_MIN, SENTRY_TILT_MAX)
        self._spin_guard_tilt.setSingleStep(1.0)
        self._spin_guard_tilt.setValue(self.config.guard.guard_tilt)
        self._spin_guard_tilt.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_guard_tilt, "guard_tilt")
        row2.addWidget(self._spin_guard_tilt)
        static_lay.addLayout(row2)

        row3 = QHBoxLayout()
        row3.addWidget(QLabel("Rest Pan (deg):"))
        self._spin_rest_pan = QDoubleSpinBox()
        self._spin_rest_pan.setRange(SENTRY_PAN_MIN, SENTRY_PAN_MAX)
        self._spin_rest_pan.setSingleStep(1.0)
        self._spin_rest_pan.setValue(float(getattr(self.config.guard, "rest_pan", self.config.guard.guard_pan)))
        self._spin_rest_pan.valueChanged.connect(self._on_guard_changed)
        row3.addWidget(self._spin_rest_pan)
        static_lay.addLayout(row3)

        row4 = QHBoxLayout()
        row4.addWidget(QLabel("Rest Tilt (deg):"))
        self._spin_rest_tilt = QDoubleSpinBox()
        self._spin_rest_tilt.setRange(SENTRY_TILT_MIN, SENTRY_TILT_MAX)
        self._spin_rest_tilt.setSingleStep(1.0)
        self._spin_rest_tilt.setValue(float(getattr(self.config.guard, "rest_tilt", self.config.guard.guard_tilt)))
        self._spin_rest_tilt.valueChanged.connect(self._on_guard_changed)
        row4.addWidget(self._spin_rest_tilt)
        static_lay.addLayout(row4)

        rest_option_row = QHBoxLayout()
        self._chk_rest_on_startup = QCheckBox("Startup to Rest")
        self._chk_rest_on_startup.setChecked(bool(getattr(self.config.guard, "rest_on_startup_enabled", True)))
        self._chk_rest_on_startup.toggled.connect(self._on_guard_changed)
        rest_option_row.addWidget(self._chk_rest_on_startup)
        self._chk_rest_on_close = QCheckBox("Close to Rest")
        self._chk_rest_on_close.setChecked(bool(getattr(self.config.guard, "rest_on_close_enabled", True)))
        self._chk_rest_on_close.toggled.connect(self._on_guard_changed)
        rest_option_row.addWidget(self._chk_rest_on_close)
        static_lay.addLayout(rest_option_row)

        motion_note = QLabel(
            "Home and Rest use a stepped ease-out move. Wake Up from the rest position automatically uses a calmer Home profile, while Home from elsewhere stays smoother without feeling sluggish."
        )
        motion_note.setWordWrap(True)
        self._set_theme_role(motion_note, "subtleBody")
        static_lay.addWidget(motion_note)

        motion_tune_grp = QGroupBox("Home / Rest Return Motion")
        motion_tune_lay = QGridLayout(motion_tune_grp)
        motion_tune_lay.setHorizontalSpacing(8)
        motion_tune_lay.setVerticalSpacing(6)

        motion_tune_lay.addWidget(QLabel("Home speed (deg/s):"), 0, 0)
        self._spin_home_move_speed = QDoubleSpinBox()
        self._spin_home_move_speed.setRange(2.0, 90.0)
        self._spin_home_move_speed.setDecimals(1)
        self._spin_home_move_speed.setSingleStep(0.5)
        self._spin_home_move_speed.setValue(float(getattr(self.config.guard, "home_move_speed_dps", 24.0)))
        self._spin_home_move_speed.valueChanged.connect(self._on_guard_changed)
        motion_tune_lay.addWidget(self._spin_home_move_speed, 0, 1)

        motion_tune_lay.addWidget(QLabel("Home final approach (deg/s):"), 0, 2)
        self._spin_home_move_approach_speed = QDoubleSpinBox()
        self._spin_home_move_approach_speed.setRange(1.0, 60.0)
        self._spin_home_move_approach_speed.setDecimals(1)
        self._spin_home_move_approach_speed.setSingleStep(0.5)
        self._spin_home_move_approach_speed.setValue(float(getattr(self.config.guard, "home_move_approach_speed_dps", 11.0)))
        self._spin_home_move_approach_speed.valueChanged.connect(self._on_guard_changed)
        motion_tune_lay.addWidget(self._spin_home_move_approach_speed, 0, 3)

        motion_tune_lay.addWidget(QLabel("Rest speed (deg/s):"), 1, 0)
        self._spin_rest_move_speed = QDoubleSpinBox()
        self._spin_rest_move_speed.setRange(2.0, 90.0)
        self._spin_rest_move_speed.setDecimals(1)
        self._spin_rest_move_speed.setSingleStep(0.5)
        self._spin_rest_move_speed.setValue(float(getattr(self.config.guard, "rest_move_speed_dps", 14.0)))
        self._spin_rest_move_speed.valueChanged.connect(self._on_guard_changed)
        motion_tune_lay.addWidget(self._spin_rest_move_speed, 1, 1)

        motion_tune_lay.addWidget(QLabel("Rest final approach (deg/s):"), 1, 2)
        self._spin_rest_move_approach_speed = QDoubleSpinBox()
        self._spin_rest_move_approach_speed.setRange(1.0, 60.0)
        self._spin_rest_move_approach_speed.setDecimals(1)
        self._spin_rest_move_approach_speed.setSingleStep(0.5)
        self._spin_rest_move_approach_speed.setValue(float(getattr(self.config.guard, "rest_move_approach_speed_dps", 5.0)))
        self._spin_rest_move_approach_speed.valueChanged.connect(self._on_guard_changed)
        motion_tune_lay.addWidget(self._spin_rest_move_approach_speed, 1, 3)

        motion_tune_lay.addWidget(QLabel("Slowdown window (deg):"), 2, 0)
        self._spin_guided_move_window = QDoubleSpinBox()
        self._spin_guided_move_window.setRange(4.0, 90.0)
        self._spin_guided_move_window.setDecimals(1)
        self._spin_guided_move_window.setSingleStep(1.0)
        self._spin_guided_move_window.setValue(float(getattr(self.config.guard, "guided_move_approach_window_deg", 18.0)))
        self._spin_guided_move_window.valueChanged.connect(self._on_guard_changed)
        motion_tune_lay.addWidget(self._spin_guided_move_window, 2, 1)

        static_lay.addWidget(motion_tune_grp)

        limit_row_1 = QHBoxLayout()
        limit_row_1.addWidget(QLabel("Pan Min / Max:"))
        self._spin_pan_min = QDoubleSpinBox()
        self._spin_pan_min.setRange(SENTRY_PAN_MIN, SENTRY_PAN_MAX)
        self._spin_pan_min.setValue(self.config.guard.pan_min)
        self._spin_pan_min.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_pan_min, "pan_limit_min")
        limit_row_1.addWidget(self._spin_pan_min)
        self._spin_pan_max = QDoubleSpinBox()
        self._spin_pan_max.setRange(SENTRY_PAN_MIN, SENTRY_PAN_MAX)
        self._spin_pan_max.setValue(self.config.guard.pan_max)
        self._spin_pan_max.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_pan_max, "pan_limit_max")
        limit_row_1.addWidget(self._spin_pan_max)
        static_lay.addLayout(limit_row_1)

        limit_row_2 = QHBoxLayout()
        limit_row_2.addWidget(QLabel("Tilt Min / Max:"))
        self._spin_tilt_min = QDoubleSpinBox()
        self._spin_tilt_min.setRange(SENTRY_TILT_MIN, SENTRY_TILT_MAX)
        self._spin_tilt_min.setValue(self.config.guard.tilt_min)
        self._spin_tilt_min.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_tilt_min, "tilt_limit_min")
        limit_row_2.addWidget(self._spin_tilt_min)
        self._spin_tilt_max = QDoubleSpinBox()
        self._spin_tilt_max.setRange(SENTRY_TILT_MIN, SENTRY_TILT_MAX)
        self._spin_tilt_max.setValue(self.config.guard.tilt_max)
        self._spin_tilt_max.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_tilt_max, "tilt_limit_max")
        limit_row_2.addWidget(self._spin_tilt_max)
        static_lay.addLayout(limit_row_2)

        btn_row = QHBoxLayout()
        btn = QPushButton("Go To Guard")
        self._set_button_role(btn, "primary")
        btn.clicked.connect(self._go_to_guard)
        self._apply_tooltip(btn, "go_guard")
        btn_row.addWidget(btn)
        btn_rest = QPushButton("Go To Rest")
        self._set_button_role(btn_rest, "utility")
        btn_rest.clicked.connect(self._on_rest_clicked)
        btn_row.addWidget(btn_rest)
        btn2 = QPushButton("Set As Guard")
        self._set_button_role(btn2, "utility")
        self._apply_tooltip(btn2, "set_current_guard")
        btn2.clicked.connect(self._set_current_as_guard)
        btn_row.addWidget(btn2)
        btn_set_rest = QPushButton("Set As Rest")
        self._set_button_role(btn_set_rest, "utility")
        btn_set_rest.clicked.connect(self._set_current_as_rest)
        btn_row.addWidget(btn_set_rest)
        static_lay.addLayout(btn_row)
        lay.addWidget(static_grp)

        # --- Sweep settings (mode 1) ---
        self._grp_sweep = QGroupBox("Sweep Settings")
        sweep_lay = QVBoxLayout(self._grp_sweep)
        sweep_lay.setSpacing(3)

        sr1 = QHBoxLayout()
        sr1.addWidget(QLabel("Pan Min (deg):"))
        self._spin_sweep_min = QDoubleSpinBox()
        self._spin_sweep_min.setRange(SENTRY_PAN_MIN, SENTRY_PAN_MAX)
        self._spin_sweep_min.setValue(self.config.guard.sweep_pan_min)
        self._spin_sweep_min.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_sweep_min, "sweep_min")
        sr1.addWidget(self._spin_sweep_min)
        sr1.addWidget(QLabel("Pan Max:"))
        self._spin_sweep_max = QDoubleSpinBox()
        self._spin_sweep_max.setRange(SENTRY_PAN_MIN, SENTRY_PAN_MAX)
        self._spin_sweep_max.setValue(self.config.guard.sweep_pan_max)
        self._spin_sweep_max.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_sweep_max, "sweep_max")
        sr1.addWidget(self._spin_sweep_max)
        sweep_lay.addLayout(sr1)

        sr2 = QHBoxLayout()
        sr2.addWidget(QLabel("Tilt (deg):"))
        self._spin_sweep_tilt = QDoubleSpinBox()
        self._spin_sweep_tilt.setRange(SENTRY_TILT_MIN, SENTRY_TILT_MAX)
        self._spin_sweep_tilt.setValue(self.config.guard.sweep_tilt)
        self._spin_sweep_tilt.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_sweep_tilt, "sweep_tilt")
        sr2.addWidget(self._spin_sweep_tilt)
        sr2.addWidget(QLabel("Speed (deg/s):"))
        self._spin_sweep_speed = QDoubleSpinBox()
        self._spin_sweep_speed.setRange(1.0, 30.0)
        self._spin_sweep_speed.setSingleStep(0.5)
        self._spin_sweep_speed.setValue(self.config.guard.sweep_speed)
        self._spin_sweep_speed.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_sweep_speed, "sweep_speed")
        sr2.addWidget(self._spin_sweep_speed)
        sweep_lay.addLayout(sr2)
        lay.addWidget(self._grp_sweep)

        # --- Waypoint settings (mode 2) ---
        self._grp_waypoint = QGroupBox("Waypoint Patrol")
        wp_lay = QVBoxLayout(self._grp_waypoint)
        wp_lay.setSpacing(3)

        self._wp_list = QListWidget()
        self._wp_list.setMaximumHeight(100)
        self._register_responsive_list(self._wp_list, "waypoint_list")
        self._apply_tooltip(self._wp_list, "waypoint_list")
        for wp in self.config.guard.patrol_waypoints:
            self._wp_list.addItem(f"P{wp[0]:.0f} T{wp[1]:.0f}")
        wp_lay.addWidget(self._wp_list)

        wp_btn_row = QHBoxLayout()
        btn_add = QPushButton("Add Current Pos")
        btn_add.clicked.connect(self._wp_add_current)
        self._apply_tooltip(btn_add, "waypoint_add")
        wp_btn_row.addWidget(btn_add)
        btn_rm = QPushButton("Remove Selected")
        btn_rm.clicked.connect(self._wp_remove_selected)
        self._apply_tooltip(btn_rm, "waypoint_remove")
        wp_btn_row.addWidget(btn_rm)
        btn_clr = QPushButton("Clear All")
        btn_clr.clicked.connect(self._wp_clear)
        self._apply_tooltip(btn_clr, "waypoint_clear")
        wp_btn_row.addWidget(btn_clr)
        self._style_button_row([btn_add, btn_rm], "utility")
        self._style_button_row([btn_clr], "danger")
        wp_lay.addLayout(wp_btn_row)

        wr1 = QHBoxLayout()
        wr1.addWidget(QLabel("Dwell (s):"))
        self._spin_wp_dwell = QDoubleSpinBox()
        self._spin_wp_dwell.setRange(0.5, 30.0)
        self._spin_wp_dwell.setSingleStep(0.5)
        self._spin_wp_dwell.setValue(self.config.guard.patrol_dwell)
        self._spin_wp_dwell.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_wp_dwell, "waypoint_dwell")
        wr1.addWidget(self._spin_wp_dwell)
        wr1.addWidget(QLabel("Speed (deg/s):"))
        self._spin_wp_speed = QDoubleSpinBox()
        self._spin_wp_speed.setRange(1.0, 30.0)
        self._spin_wp_speed.setSingleStep(0.5)
        self._spin_wp_speed.setValue(self.config.guard.patrol_speed)
        self._spin_wp_speed.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_wp_speed, "waypoint_speed")
        wr1.addWidget(self._spin_wp_speed)
        wp_lay.addLayout(wr1)
        lay.addWidget(self._grp_waypoint)

        # --- Random scan settings (mode 3) ---
        self._grp_random = QGroupBox("Random Scan")
        rnd_lay = QVBoxLayout(self._grp_random)
        rnd_lay.setSpacing(3)

        rr1 = QHBoxLayout()
        rr1.addWidget(QLabel("Pan Min:"))
        self._spin_rnd_pan_min = QDoubleSpinBox()
        self._spin_rnd_pan_min.setRange(SENTRY_PAN_MIN, SENTRY_PAN_MAX)
        self._spin_rnd_pan_min.setValue(self.config.guard.random_pan_min)
        self._spin_rnd_pan_min.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_rnd_pan_min, "random_pan_min")
        rr1.addWidget(self._spin_rnd_pan_min)
        rr1.addWidget(QLabel("Max:"))
        self._spin_rnd_pan_max = QDoubleSpinBox()
        self._spin_rnd_pan_max.setRange(SENTRY_PAN_MIN, SENTRY_PAN_MAX)
        self._spin_rnd_pan_max.setValue(self.config.guard.random_pan_max)
        self._spin_rnd_pan_max.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_rnd_pan_max, "random_pan_max")
        rr1.addWidget(self._spin_rnd_pan_max)
        rnd_lay.addLayout(rr1)

        rr2 = QHBoxLayout()
        rr2.addWidget(QLabel("Tilt Min:"))
        self._spin_rnd_tilt_min = QDoubleSpinBox()
        self._spin_rnd_tilt_min.setRange(SENTRY_TILT_MIN, SENTRY_TILT_MAX)
        self._spin_rnd_tilt_min.setValue(self.config.guard.random_tilt_min)
        self._spin_rnd_tilt_min.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_rnd_tilt_min, "random_tilt_min")
        rr2.addWidget(self._spin_rnd_tilt_min)
        rr2.addWidget(QLabel("Max:"))
        self._spin_rnd_tilt_max = QDoubleSpinBox()
        self._spin_rnd_tilt_max.setRange(SENTRY_TILT_MIN, SENTRY_TILT_MAX)
        self._spin_rnd_tilt_max.setValue(self.config.guard.random_tilt_max)
        self._spin_rnd_tilt_max.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_rnd_tilt_max, "random_tilt_max")
        rr2.addWidget(self._spin_rnd_tilt_max)
        rnd_lay.addLayout(rr2)

        rr3 = QHBoxLayout()
        rr3.addWidget(QLabel("Dwell (s):"))
        self._spin_rnd_dwell = QDoubleSpinBox()
        self._spin_rnd_dwell.setRange(0.5, 30.0)
        self._spin_rnd_dwell.setSingleStep(0.5)
        self._spin_rnd_dwell.setValue(self.config.guard.random_dwell)
        self._spin_rnd_dwell.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_rnd_dwell, "random_dwell")
        rr3.addWidget(self._spin_rnd_dwell)
        rr3.addWidget(QLabel("Speed (deg/s):"))
        self._spin_rnd_speed = QDoubleSpinBox()
        self._spin_rnd_speed.setRange(1.0, 30.0)
        self._spin_rnd_speed.setSingleStep(0.5)
        self._spin_rnd_speed.setValue(self.config.guard.random_speed)
        self._spin_rnd_speed.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_rnd_speed, "random_speed")
        rr3.addWidget(self._spin_rnd_speed)
        rnd_lay.addLayout(rr3)
        lay.addWidget(self._grp_random)

        # --- Camera FOV ---
        fov_grp = QGroupBox("Camera FOV")
        fov_lay = QVBoxLayout(fov_grp)
        fov_lay.setSpacing(3)

        row3 = QHBoxLayout()
        row3.addWidget(QLabel("HFOV (deg):"))
        self._spin_hfov = QDoubleSpinBox()
        self._spin_hfov.setRange(30.0, 180.0)
        self._spin_hfov.setSingleStep(5.0)
        self._spin_hfov.setValue(self.config.guard.camera_hfov)
        self._spin_hfov.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_hfov, "camera_hfov")
        row3.addWidget(self._spin_hfov)
        row3.addWidget(QLabel("VFOV:"))
        self._spin_vfov = QDoubleSpinBox()
        self._spin_vfov.setRange(20.0, 140.0)
        self._spin_vfov.setSingleStep(5.0)
        self._spin_vfov.setValue(self.config.guard.camera_vfov)
        self._spin_vfov.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_vfov, "camera_vfov")
        row3.addWidget(self._spin_vfov)
        fov_lay.addLayout(row3)
        lay.addWidget(fov_grp)

        scope_grp = QGroupBox("Scope View")
        scope_lay = QVBoxLayout(scope_grp)
        scope_lay.setSpacing(4)

        self._chk_scope_view = QCheckBox("Enable scope view during ENGAGING")
        self._chk_scope_view.setChecked(self.config.scope_view_enabled)
        self._chk_scope_view.toggled.connect(self._on_scope_view_changed)
        self._apply_tooltip(self._chk_scope_view, "scope_view_enabled")
        scope_lay.addWidget(self._chk_scope_view)

        scope_radius_row = QHBoxLayout()
        scope_radius_row.addWidget(QLabel("Scope radius (%):"))
        self._spin_scope_radius = QSpinBox()
        self._spin_scope_radius.setRange(20, 60)
        self._spin_scope_radius.setSingleStep(1)
        self._spin_scope_radius.setValue(int(self.config.scope_radius_pct))
        self._spin_scope_radius.valueChanged.connect(self._on_scope_view_changed)
        self._apply_tooltip(self._spin_scope_radius, "scope_radius")
        scope_radius_row.addWidget(self._spin_scope_radius)
        scope_lay.addLayout(scope_radius_row)

        scope_vignette_row = QHBoxLayout()
        scope_vignette_row.addWidget(QLabel("Vignette opacity (%):"))
        self._spin_scope_vignette = QSpinBox()
        self._spin_scope_vignette.setRange(0, 100)
        self._spin_scope_vignette.setSingleStep(5)
        self._spin_scope_vignette.setValue(int(self.config.scope_vignette_opacity))
        self._spin_scope_vignette.valueChanged.connect(self._on_scope_view_changed)
        self._apply_tooltip(self._spin_scope_vignette, "scope_vignette")
        scope_vignette_row.addWidget(self._spin_scope_vignette)
        scope_lay.addLayout(scope_vignette_row)

        lay.addWidget(scope_grp)

        mask_grp = QGroupBox("No-Fire Masks")
        mask_lay = QVBoxLayout(mask_grp)
        mask_lay.setSpacing(4)

        name_row = QHBoxLayout()
        name_row.addWidget(QLabel("Mask Name:"))
        self._edit_mask_name = QLineEdit()
        self._edit_mask_name.setPlaceholderText("No-fire zone name")
        self._edit_mask_name.setText(self._next_no_fire_mask_name())
        self._apply_tooltip(self._edit_mask_name, "no_fire_mask_name")
        name_row.addWidget(self._edit_mask_name)
        mask_lay.addLayout(name_row)

        self._btn_mask_capture = QPushButton("Capture")
        self._btn_mask_capture.setCheckable(True)
        self._set_button_role(self._btn_mask_capture, "mode")
        self._btn_mask_capture.toggled.connect(self._on_mask_capture_toggled)
        self._apply_tooltip(self._btn_mask_capture, "no_fire_mask_capture")
        mask_lay.addWidget(self._btn_mask_capture)

        draft_row = QHBoxLayout()
        self._btn_mask_finish = QPushButton("Finish Mask")
        self._set_button_role(self._btn_mask_finish, "utility")
        self._btn_mask_finish.clicked.connect(self._finish_no_fire_mask)
        self._apply_tooltip(self._btn_mask_finish, "no_fire_mask_finish")
        draft_row.addWidget(self._btn_mask_finish)
        self._btn_mask_undo = QPushButton("Undo Vertex")
        self._set_button_role(self._btn_mask_undo, "utility")
        self._btn_mask_undo.clicked.connect(self._undo_no_fire_mask_vertex)
        self._apply_tooltip(self._btn_mask_undo, "no_fire_mask_undo")
        draft_row.addWidget(self._btn_mask_undo)
        self._btn_mask_clear = QPushButton("Clear Draft")
        self._set_button_role(self._btn_mask_clear, "danger")
        self._btn_mask_clear.clicked.connect(self._clear_no_fire_mask_draft)
        self._apply_tooltip(self._btn_mask_clear, "no_fire_mask_clear")
        draft_row.addWidget(self._btn_mask_clear)
        mask_lay.addLayout(draft_row)

        self._lbl_mask_draft = QLabel("Draft: 0 vertices")
        mask_lay.addWidget(self._lbl_mask_draft)

        self._mask_list = QListWidget()
        self._mask_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self._mask_list.setMaximumHeight(120)
        self._register_responsive_list(self._mask_list, "mask_list")
        mask_lay.addWidget(self._mask_list)

        manage_row = QHBoxLayout()
        self._btn_mask_toggle = QPushButton("Toggle")
        self._set_button_role(self._btn_mask_toggle, "utility")
        self._btn_mask_toggle.clicked.connect(self._toggle_selected_no_fire_masks)
        self._apply_tooltip(self._btn_mask_toggle, "no_fire_mask_toggle")
        manage_row.addWidget(self._btn_mask_toggle)
        self._btn_mask_remove = QPushButton("Remove")
        self._set_button_role(self._btn_mask_remove, "danger")
        self._btn_mask_remove.clicked.connect(self._remove_selected_no_fire_masks)
        self._apply_tooltip(self._btn_mask_remove, "no_fire_mask_remove")
        manage_row.addWidget(self._btn_mask_remove)
        self._register_responsive_box_layout(draft_row, "dense_row")
        self._register_responsive_box_layout(manage_row, "dense_row")
        mask_lay.addLayout(manage_row)

        self._chk_show_no_fire_masks = QCheckBox("Show no-fire masks")
        self._chk_show_no_fire_masks.setChecked(self.config.show_no_fire_masks)
        self._chk_show_no_fire_masks.toggled.connect(self._on_overlay_changed)
        self._apply_tooltip(self._chk_show_no_fire_masks, "show_no_fire_masks")
        mask_lay.addWidget(self._chk_show_no_fire_masks)

        self._chk_mask_trace = QCheckBox("Trace mask diagnostics")
        self._chk_mask_trace.setChecked(False)
        self._apply_tooltip(self._chk_mask_trace, "mask_trace")
        mask_lay.addWidget(self._chk_mask_trace)

        self._btn_mask_trace_dump = QPushButton("Dump Snapshot")
        self._set_button_role(self._btn_mask_trace_dump, "utility")
        self._btn_mask_trace_dump.clicked.connect(self._dump_mask_trace_snapshot)
        self._apply_tooltip(self._btn_mask_trace_dump, "mask_trace_dump")
        mask_lay.addWidget(self._btn_mask_trace_dump)

        lay.addWidget(mask_grp)

        # --- PIR Guard (Blind-Spot Detection) ---
        pir_grp = QGroupBox("PIR Guard (Blind-Spot Detection)")
        pir_lay = QVBoxLayout(pir_grp)
        pir_lay.setSpacing(3)

        # Master enable
        self._chk_pir_enabled = QCheckBox("Enable PIR sensors")
        self._chk_pir_enabled.setChecked(self.config.pir_guard.pir_enabled)
        self._chk_pir_enabled.toggled.connect(self._on_pir_enabled_changed)
        self._apply_tooltip(self._chk_pir_enabled, "pir_enabled")
        pir_lay.addWidget(self._chk_pir_enabled)

        self._chk_pir_event_blink = QCheckBox("Blink ESP32 GPIO2 LED on PIR event")
        self._chk_pir_event_blink.setChecked(bool(getattr(self.config.pir_guard, "pir_event_blink_enabled", False)))
        self._chk_pir_event_blink.toggled.connect(self._on_pir_settings_changed)
        self._apply_tooltip(self._chk_pir_event_blink, "pir_event_blink_enabled")
        pir_lay.addWidget(self._chk_pir_event_blink)

        pir_hint = QLabel(
            "For roughly 120° physical spacing, keep one sensor as the active owner of a target crossing adjacent PIR cones. "
            "The lockout below suppresses near-simultaneous cross-sensor overlap in software."
        )
        pir_hint.setWordWrap(True)
        self._set_theme_role(pir_hint, "mutedCompact")
        pir_lay.addWidget(pir_hint)

        # PIR sensors table (3 rows: pan cue angle, tilt cue angle, enabled)
        sensors = self.config.pir_guard.sensors
        if len(sensors) < 3:
            # Ensure at least three sensors exist in config to match the UI.
            # Equal 90° spacing: S0=45° (right), S1=135° (front), S2=225° (left).
            default_pans = [45.0, 135.0, 225.0]
            for j in range(len(sensors), 3):
                sensors.append(
                    PIRSensorConfig(pin_id=j, cue_pan=default_pans[j], cue_tilt=35.0, enabled=False)
                )

        self._pir_spin_cues = []  # List of (pan spin, tilt spin, enabled checkbox) tuples
        for i in range(3):
            sensor_name = f"Sensor {i+1}"
            row = QHBoxLayout()
            row.addWidget(QLabel(f"{sensor_name}:"))
            
            # Pan cue angle
            pan_spin = QDoubleSpinBox()
            pan_spin.setRange(SENTRY_PAN_MIN, SENTRY_PAN_MAX)
            pan_spin.setSingleStep(1.0)
            pan_spin.setValue(self.config.pir_guard.sensors[i].cue_pan)
            pan_spin.setMaximumWidth(80)
            pan_spin.valueChanged.connect(lambda val, idx=i, field='cue_pan': self._on_pir_sensor_changed(idx, field, val))
            self._apply_tooltip(pan_spin, "pir_cue_pan")
            row.addWidget(QLabel("Pan:"))
            row.addWidget(pan_spin)
            
            # Tilt cue angle
            tilt_spin = QDoubleSpinBox()
            tilt_spin.setRange(SENTRY_TILT_MIN, SENTRY_TILT_MAX)
            tilt_spin.setSingleStep(1.0)
            tilt_spin.setValue(self.config.pir_guard.sensors[i].cue_tilt)
            tilt_spin.setMaximumWidth(80)
            tilt_spin.valueChanged.connect(lambda val, idx=i, field='cue_tilt': self._on_pir_sensor_changed(idx, field, val))
            self._apply_tooltip(tilt_spin, "pir_cue_tilt")
            row.addWidget(QLabel("Tilt:"))
            row.addWidget(tilt_spin)
            
            # Enabled checkbox
            chk_enabled = QCheckBox("Active")
            chk_enabled.setChecked(self.config.pir_guard.sensors[i].enabled)
            chk_enabled.toggled.connect(lambda checked, idx=i: self._on_pir_sensor_enabled(idx, checked))
            self._apply_tooltip(chk_enabled, "pir_sensor_enabled")
            row.addWidget(chk_enabled)
            
            row.addStretch()
            pir_lay.addLayout(row)
            self._pir_spin_cues.append((pan_spin, tilt_spin, chk_enabled))

        # Scan behavior options
        scan_row1 = QHBoxLayout()
        scan_row1.addWidget(QLabel("Scan Pan Range (deg):"))
        self._spin_pir_scan_pan_range = QDoubleSpinBox()
        self._spin_pir_scan_pan_range.setRange(5.0, 90.0)
        self._spin_pir_scan_pan_range.setSingleStep(1.0)
        self._spin_pir_scan_pan_range.setValue(self.config.pir_guard.scan_pan_range)
        self._spin_pir_scan_pan_range.valueChanged.connect(self._on_pir_settings_changed)
        self._apply_tooltip(self._spin_pir_scan_pan_range, "pir_scan_pan_range")
        scan_row1.addWidget(self._spin_pir_scan_pan_range)
        
        scan_row1.addWidget(QLabel("Tilt Range (deg):"))
        self._spin_pir_scan_tilt_range = QDoubleSpinBox()
        self._spin_pir_scan_tilt_range.setRange(5.0, 90.0)
        self._spin_pir_scan_tilt_range.setSingleStep(1.0)
        self._spin_pir_scan_tilt_range.setValue(self.config.pir_guard.scan_tilt_range)
        self._spin_pir_scan_tilt_range.valueChanged.connect(self._on_pir_settings_changed)
        self._apply_tooltip(self._spin_pir_scan_tilt_range, "pir_scan_tilt_range")
        scan_row1.addWidget(self._spin_pir_scan_tilt_range)
        pir_lay.addLayout(scan_row1)

        scan_row2 = QHBoxLayout()
        scan_row2.addWidget(QLabel("Grid Resolution:"))
        self._spin_pir_grid_res = QSpinBox()
        self._spin_pir_grid_res.setRange(2, 6)
        self._spin_pir_grid_res.setValue(self.config.pir_guard.scan_grid_resolution)
        self._spin_pir_grid_res.valueChanged.connect(self._on_pir_settings_changed)
        self._apply_tooltip(self._spin_pir_grid_res, "pir_grid_resolution")
        scan_row2.addWidget(self._spin_pir_grid_res)
        
        scan_row2.addWidget(QLabel("Scan Speed (deg/s):"))
        self._spin_pir_scan_speed = QDoubleSpinBox()
        self._spin_pir_scan_speed.setRange(1.0, 30.0)
        self._spin_pir_scan_speed.setSingleStep(0.5)
        self._spin_pir_scan_speed.setValue(self.config.pir_guard.scan_speed)
        self._spin_pir_scan_speed.valueChanged.connect(self._on_pir_settings_changed)
        self._apply_tooltip(self._spin_pir_scan_speed, "pir_scan_speed")
        scan_row2.addWidget(self._spin_pir_scan_speed)
        pir_lay.addLayout(scan_row2)

        scan_row3 = QHBoxLayout()
        scan_row3.addWidget(QLabel("Cue Hold (s):"))
        self._spin_pir_cue_hold = QDoubleSpinBox()
        self._spin_pir_cue_hold.setRange(0.05, 2.0)
        self._spin_pir_cue_hold.setSingleStep(0.02)
        self._spin_pir_cue_hold.setDecimals(2)
        self._spin_pir_cue_hold.setValue(float(getattr(self.config.pir_guard, "cue_hold_time_s", 0.18)))
        self._spin_pir_cue_hold.valueChanged.connect(self._on_pir_settings_changed)
        self._apply_tooltip(self._spin_pir_cue_hold, "pir_cue_hold_time")
        scan_row3.addWidget(self._spin_pir_cue_hold)

        scan_row3.addWidget(QLabel("Confirmation Timeout (s):"))
        self._spin_pir_confirm_timeout = QDoubleSpinBox()
        self._spin_pir_confirm_timeout.setRange(0.5, 10.0)
        self._spin_pir_confirm_timeout.setSingleStep(0.2)
        self._spin_pir_confirm_timeout.setValue(self.config.pir_guard.confirmation_timeout)
        self._spin_pir_confirm_timeout.valueChanged.connect(self._on_pir_settings_changed)
        self._apply_tooltip(self._spin_pir_confirm_timeout, "pir_confirm_timeout")
        scan_row3.addWidget(self._spin_pir_confirm_timeout)
        
        self._chk_pir_scan_enabled = QCheckBox("Scan on No-Detection")
        self._chk_pir_scan_enabled.setChecked(self.config.pir_guard.scan_on_no_detect)
        self._chk_pir_scan_enabled.toggled.connect(self._on_pir_settings_changed)
        self._apply_tooltip(self._chk_pir_scan_enabled, "pir_scan_on_no_detect")
        scan_row3.addWidget(self._chk_pir_scan_enabled)
        
        scan_row3.addStretch()
        pir_lay.addLayout(scan_row3)

        scan_row4 = QHBoxLayout()
        scan_row4.addWidget(QLabel("Cross-Sensor Lockout (ms):"))
        self._spin_pir_cross_lockout_ms = QSpinBox()
        self._spin_pir_cross_lockout_ms.setRange(0, 3000)
        self._spin_pir_cross_lockout_ms.setSingleStep(50)
        self._spin_pir_cross_lockout_ms.setValue(int(getattr(self.config.pir_guard, "cross_sensor_lockout_ms", 800)))
        self._spin_pir_cross_lockout_ms.valueChanged.connect(self._on_pir_settings_changed)
        self._apply_tooltip(self._spin_pir_cross_lockout_ms, "pir_cross_lockout_ms")
        scan_row4.addWidget(self._spin_pir_cross_lockout_ms)

        self._btn_pir_layout_120 = QPushButton("Use 120° PIR")
        self._set_button_role(self._btn_pir_layout_120, "utility")
        self._btn_pir_layout_120.clicked.connect(self._apply_pir_120_layout)
        self._btn_pir_layout_120.setToolTip("Apply a non-overlapping three-sector PIR layout for sensors spaced roughly 120° apart")
        scan_row4.addWidget(self._btn_pir_layout_120)
        scan_row4.addStretch()
        pir_lay.addLayout(scan_row4)

        # Status display
        self._lbl_pir_status = QLabel("Status: Idle")
        pir_lay.addWidget(self._lbl_pir_status)

        lay.addWidget(pir_grp)

        # Overlay toggles
        self._chk_overlay = QCheckBox("Show overlay")
        self._chk_overlay.setChecked(self.config.show_overlay)
        self._chk_overlay.toggled.connect(self._on_overlay_changed)
        self._apply_tooltip(self._chk_overlay, "show_overlay")
        lay.addWidget(self._chk_overlay)

        self._chk_scores = QCheckBox("Show threat scores")
        self._chk_scores.setChecked(self.config.show_threat_scores)
        self._chk_scores.toggled.connect(self._on_overlay_changed)
        self._apply_tooltip(self._chk_scores, "show_scores")
        lay.addWidget(self._chk_scores)

        self._chk_zone = QCheckBox("Show engagement zone")
        self._chk_zone.setChecked(self.config.show_engagement_zone)
        self._chk_zone.toggled.connect(self._on_overlay_changed)
        self._apply_tooltip(self._chk_zone, "show_zone")
        lay.addWidget(self._chk_zone)

        self._chk_guard_crosshair = QCheckBox("Show guard crosshair")
        self._chk_guard_crosshair.setChecked(self.config.show_guard_crosshair)
        self._chk_guard_crosshair.toggled.connect(self._on_overlay_changed)
        self._apply_tooltip(self._chk_guard_crosshair, "show_guard_crosshair")
        lay.addWidget(self._chk_guard_crosshair)

        self._refresh_no_fire_mask_list()
        self._update_mask_editor_ui()

        lay.addStretch()

        # Set initial visibility of mode-specific groups
        self._update_guard_mode_visibility(self.config.guard.guard_mode)

        return w

    def _build_facial_recognition_tab(self) -> QWidget:
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(6)

        intro = QLabel(
            "Identify known faces from imported images or the live camera feed. Friendly profiles can be announced and optionally excluded from engagement."
        )
        intro.setWordWrap(True)
        self._set_theme_role(intro, "subtleBody")
        lay.addWidget(intro)

        runtime_grp = QGroupBox("Recognition Runtime")
        runtime_lay = QGridLayout(runtime_grp)
        self._chk_face_enabled = QCheckBox("Enable face recognition")
        self._chk_face_enabled.setChecked(bool(self.config.face_recognition.enabled))
        self._chk_face_enabled.toggled.connect(self._on_face_runtime_settings_changed)
        runtime_lay.addWidget(self._chk_face_enabled, 0, 0, 1, 2)

        runtime_lay.addWidget(QLabel("Match threshold:"), 1, 0)
        self._spin_face_threshold = QDoubleSpinBox()
        self._spin_face_threshold.setRange(0.50, 0.99)
        self._spin_face_threshold.setDecimals(2)
        self._spin_face_threshold.setSingleStep(0.01)
        self._spin_face_threshold.setValue(float(self.config.face_recognition.recognition_threshold))
        self._spin_face_threshold.valueChanged.connect(self._on_face_runtime_settings_changed)
        runtime_lay.addWidget(self._spin_face_threshold, 1, 1)

        runtime_lay.addWidget(QLabel("Min face size (px):"), 2, 0)
        self._spin_face_min_size = QSpinBox()
        self._spin_face_min_size.setRange(32, 256)
        self._spin_face_min_size.setValue(int(self.config.face_recognition.min_face_size_px))
        self._spin_face_min_size.valueChanged.connect(self._on_face_runtime_settings_changed)
        runtime_lay.addWidget(self._spin_face_min_size, 2, 1)

        self._chk_face_suppress = QCheckBox("Suppress friendly known faces from engagement")
        self._chk_face_suppress.setChecked(bool(self.config.face_recognition.suppress_known_faces_from_engagement))
        self._chk_face_suppress.toggled.connect(self._on_face_runtime_settings_changed)
        runtime_lay.addWidget(self._chk_face_suppress, 3, 0, 1, 2)

        self._chk_face_announce = QCheckBox("Speak recognized names when faces are matched")
        self._chk_face_announce.setChecked(bool(self.config.face_recognition.announce_known_faces))
        self._chk_face_announce.toggled.connect(self._on_face_runtime_settings_changed)
        runtime_lay.addWidget(self._chk_face_announce, 4, 0, 1, 2)

        self._chk_face_gesture = QCheckBox("Friendly reaction gesture for recognized family")
        self._chk_face_gesture.setChecked(bool(self.config.face_recognition.cute_gesture_enabled))
        self._chk_face_gesture.toggled.connect(self._on_face_runtime_settings_changed)
        runtime_lay.addWidget(self._chk_face_gesture, 5, 0, 1, 2)

        self._lbl_face_runtime_status = QLabel("")
        self._lbl_face_runtime_status.setWordWrap(True)
        self._set_theme_role(self._lbl_face_runtime_status, "mutedCompact")
        runtime_lay.addWidget(self._lbl_face_runtime_status, 6, 0, 1, 2)
        lay.addWidget(runtime_grp)

        enroll_grp = QGroupBox("Known Faces")
        enroll_lay = QGridLayout(enroll_grp)
        enroll_lay.addWidget(QLabel("Profile Name:"), 0, 0)
        self._edit_face_profile_name = QLineEdit()
        self._edit_face_profile_name.setPlaceholderText("Example: Mom")
        enroll_lay.addWidget(self._edit_face_profile_name, 0, 1, 1, 2)

        enroll_lay.addWidget(QLabel("Notes:"), 1, 0)
        self._edit_face_profile_notes = QLineEdit()
        self._edit_face_profile_notes.setPlaceholderText("Optional note about this face profile")
        enroll_lay.addWidget(self._edit_face_profile_notes, 1, 1, 1, 2)

        self._chk_face_profile_friendly = QCheckBox("Friendly / family profile")
        self._chk_face_profile_friendly.setChecked(True)
        enroll_lay.addWidget(self._chk_face_profile_friendly, 2, 0, 1, 3)

        self._chk_face_profile_announce = QCheckBox("Announce this name when recognized")
        self._chk_face_profile_announce.setChecked(True)
        enroll_lay.addWidget(self._chk_face_profile_announce, 3, 0, 1, 3)

        self._chk_face_profile_gesture = QCheckBox("Allow friendly reaction gesture")
        self._chk_face_profile_gesture.setChecked(True)
        enroll_lay.addWidget(self._chk_face_profile_gesture, 4, 0, 1, 3)

        self._face_profile_list = QListWidget()
        self._face_profile_list.currentItemChanged.connect(self._on_face_profile_selected)
        enroll_lay.addWidget(self._face_profile_list, 5, 0, 1, 3)

        btn_import_faces = QPushButton("Add Images")
        self._set_button_role(btn_import_faces, "utility")
        btn_import_faces.clicked.connect(self._register_face_from_images)
        enroll_lay.addWidget(btn_import_faces, 6, 0)

        btn_capture_face = QPushButton("Add Live")
        self._set_button_role(btn_capture_face, "utility")
        btn_capture_face.clicked.connect(self._register_face_from_live_frame)
        enroll_lay.addWidget(btn_capture_face, 6, 1)

        btn_remove_face = QPushButton("Remove")
        self._set_button_role(btn_remove_face, "utility")
        btn_remove_face.clicked.connect(self._remove_selected_face_profile)
        enroll_lay.addWidget(btn_remove_face, 6, 2)
        lay.addWidget(enroll_grp)

        test_row = QHBoxLayout()
        btn_test = QPushButton("Test Frame")
        self._set_button_role(btn_test, "utility")
        btn_test.clicked.connect(self._run_face_recognition_test)
        test_row.addWidget(btn_test)
        test_row.addStretch(1)
        lay.addLayout(test_row)

        lay.addStretch()
        self._rebuild_face_profile_list()
        self._update_face_runtime_status()
        return w

    def _build_shortcut_keys_tab(self) -> QWidget:
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(6)

        intro = QLabel(
            "Keyboard shortcuts stay active while the Smart Sentry window is focused. Use Quick Keys at the top for the same reference sheet at any time."
        )
        intro.setWordWrap(True)
        self._set_theme_role(intro, "subtleBody")
        lay.addWidget(intro)

        global_grp = QGroupBox("Shortcut Runtime")
        global_lay = QVBoxLayout(global_grp)
        self._chk_shortcuts_enabled = QCheckBox("Enable window-focused keyboard shortcuts")
        self._chk_shortcuts_enabled.setChecked(bool(self.config.shortcuts.enabled))
        self._chk_shortcuts_enabled.toggled.connect(self._on_shortcuts_enabled_changed)
        global_lay.addWidget(self._chk_shortcuts_enabled)

        self._chk_manual_keyboard_enabled = QCheckBox("Enable manual keyboard movement and fire keys (W/A/S/D + Space)")
        self._chk_manual_keyboard_enabled.setChecked(bool(getattr(self.config.shortcuts, "manual_controls_enabled", False)))
        self._chk_manual_keyboard_enabled.toggled.connect(self._on_manual_shortcuts_enabled_changed)
        global_lay.addWidget(self._chk_manual_keyboard_enabled)

        manual_note = QLabel(
            "Disabled by default so focused-window key presses cannot accidentally move the turret or fire while safety is armed."
        )
        manual_note.setWordWrap(True)
        self._set_theme_role(manual_note, "mutedCompact")
        global_lay.addWidget(manual_note)

        self._lbl_shortcut_summary = QLabel("")
        self._lbl_shortcut_summary.setWordWrap(True)
        self._set_theme_role(self._lbl_shortcut_summary, "mutedCompact")
        global_lay.addWidget(self._lbl_shortcut_summary)

        btn_row = QHBoxLayout()
        btn_reload = QPushButton("Reload")
        self._set_button_role(btn_reload, "utility")
        btn_reload.clicked.connect(self._install_global_shortcuts)
        btn_row.addWidget(btn_reload)

        btn_open_doc = QPushButton("Quick Guide")
        self._set_button_role(btn_open_doc, "utility")
        btn_open_doc.clicked.connect(self._open_shortcut_quick_view)
        btn_row.addWidget(btn_open_doc)
        btn_row.addStretch(1)
        self._register_responsive_box_layout(btn_row, "dense_row")
        global_lay.addLayout(btn_row)
        lay.addWidget(global_grp)

        behavior_grp = QGroupBox("Assigned Keys")
        behavior_lay = QVBoxLayout(behavior_grp)
        self._lbl_shortcut_keys = QLabel("")
        self._lbl_shortcut_keys.setWordWrap(True)
        self._set_theme_role(self._lbl_shortcut_keys, "subtleBody")
        behavior_lay.addWidget(self._lbl_shortcut_keys)
        lay.addWidget(behavior_grp)

        lay.addStretch()
        self._update_shortcut_labels()
        return w

    def _build_ai_assistant_tab(self) -> QWidget:
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(6)

        intro = QLabel(
            "Local offline assistant powered by Ollama. It uses deterministic runtime checks plus a local model for analysis, coaching, and operator Q and A while keeping live actions permission-gated."
        )
        intro.setWordWrap(True)
        self._set_theme_role(intro, "subtleBody")
        lay.addWidget(intro)

        session_grp = QGroupBox("Local Model Bridge")
        session_lay = QGridLayout(session_grp)
        session_lay.addWidget(QLabel("Assistant Mode:"), 0, 0)
        self._combo_ai_mode = QComboBox()
        self._combo_ai_mode.addItem("Read-Only Advisor", "read_only")
        self._combo_ai_mode.addItem("Guided Tuning", "guided_tuning")
        self._combo_ai_mode.addItem("Runtime Analyst", "mode_recommendations")
        self._combo_ai_mode.addItem("Conversational Voice", "conversational_voice")
        mode_index = max(0, self._combo_ai_mode.findData(str(self.config.ai_assistant.mode or "guided_tuning")))
        self._combo_ai_mode.setCurrentIndex(mode_index)
        self._combo_ai_mode.currentIndexChanged.connect(self._on_ai_assistant_settings_changed)
        session_lay.addWidget(self._combo_ai_mode, 0, 1, 1, 2)

        session_lay.addWidget(QLabel("Ollama Endpoint:"), 1, 0)
        self._edit_ai_endpoint = QLineEdit(str(getattr(self.config.ai_assistant, "endpoint_url", "http://localhost:11434") or "http://localhost:11434"))
        self._edit_ai_endpoint.editingFinished.connect(self._on_ai_assistant_settings_changed)
        session_lay.addWidget(self._edit_ai_endpoint, 1, 1, 1, 2)

        session_lay.addWidget(QLabel("Fast Model:"), 2, 0)
        self._combo_ai_model = QComboBox()
        self._combo_ai_model.setEditable(True)
        self._combo_ai_model.currentTextChanged.connect(self._on_ai_assistant_settings_changed)
        session_lay.addWidget(self._combo_ai_model, 2, 1, 1, 2)

        session_lay.addWidget(QLabel("Analyst Model:"), 3, 0)
        self._combo_ai_analyst_model = QComboBox()
        self._combo_ai_analyst_model.setEditable(True)
        self._combo_ai_analyst_model.currentTextChanged.connect(self._on_ai_assistant_settings_changed)
        session_lay.addWidget(self._combo_ai_analyst_model, 3, 1, 1, 2)

        session_lay.addWidget(QLabel("Model Tier:"), 4, 0)
        model_tier_row = QHBoxLayout()
        model_tier_row.setContentsMargins(0, 0, 0, 0)
        model_tier_row.setSpacing(6)
        self._btn_ai_use_fast_model = QPushButton("Fast")
        self._btn_ai_use_fast_model.setCheckable(True)
        self._set_button_role(self._btn_ai_use_fast_model, "utility")
        self._btn_ai_use_fast_model.clicked.connect(lambda: self._set_ai_model_tier("fast"))
        model_tier_row.addWidget(self._btn_ai_use_fast_model)
        self._btn_ai_use_analyst_model = QPushButton("Analyst")
        self._btn_ai_use_analyst_model.setCheckable(True)
        self._set_button_role(self._btn_ai_use_analyst_model, "utility")
        self._btn_ai_use_analyst_model.clicked.connect(lambda: self._set_ai_model_tier("analyst"))
        model_tier_row.addWidget(self._btn_ai_use_analyst_model)
        model_tier_row.addStretch(1)
        model_tier_host = QWidget()
        model_tier_host.setLayout(model_tier_row)
        session_lay.addWidget(model_tier_host, 4, 1, 1, 2)

        self._lbl_ai_provider_status = QLabel("Checking local model service...")
        self._set_theme_role(self._lbl_ai_provider_status, "mutedCompact")
        session_lay.addWidget(self._lbl_ai_provider_status, 5, 0, 1, 3)

        self._chk_ai_enabled = QCheckBox("Enable in-app AI assistant")
        self._chk_ai_enabled.setChecked(bool(self.config.ai_assistant.enabled))
        self._chk_ai_enabled.toggled.connect(self._on_ai_assistant_settings_changed)
        session_lay.addWidget(self._chk_ai_enabled, 6, 0, 1, 3)

        self._chk_ai_allow_modes = QCheckBox("Allow the assistant to suggest or switch detection modes")
        self._chk_ai_allow_modes.setChecked(bool(self.config.ai_assistant.allow_mode_switch))
        self._chk_ai_allow_modes.toggled.connect(self._on_ai_assistant_settings_changed)
        session_lay.addWidget(self._chk_ai_allow_modes, 7, 0, 1, 3)

        self._chk_ai_allow_tuning = QCheckBox("Allow the assistant to draft tuning or runtime-setting changes")
        self._chk_ai_allow_tuning.setChecked(bool(self.config.ai_assistant.allow_setting_drafts))
        self._chk_ai_allow_tuning.toggled.connect(self._on_ai_assistant_settings_changed)
        session_lay.addWidget(self._chk_ai_allow_tuning, 8, 0, 1, 3)

        self._chk_ai_allow_analysis = QCheckBox("Allow runtime-state analysis and summaries")
        self._chk_ai_allow_analysis.setChecked(bool(self.config.ai_assistant.allow_runtime_analysis))
        self._chk_ai_allow_analysis.toggled.connect(self._on_ai_assistant_settings_changed)
        session_lay.addWidget(self._chk_ai_allow_analysis, 9, 0, 1, 3)

        self._chk_ai_allow_actions = QCheckBox("Allow supported local actions to execute from explicit operator requests")
        self._chk_ai_allow_actions.setChecked(bool(getattr(self.config.ai_assistant, "allow_action_execution", True)))
        self._chk_ai_allow_actions.toggled.connect(self._on_ai_assistant_settings_changed)
        session_lay.addWidget(self._chk_ai_allow_actions, 10, 0, 1, 3)

        self._chk_ai_include_logs = QCheckBox("Include recent log lines in local AI prompts")
        self._chk_ai_include_logs.setChecked(bool(getattr(self.config.ai_assistant, "include_recent_logs", True)))
        self._chk_ai_include_logs.toggled.connect(self._on_ai_assistant_settings_changed)
        session_lay.addWidget(self._chk_ai_include_logs, 11, 0, 1, 3)

        btn_refresh_models = QPushButton("Refresh")
        self._set_button_role(btn_refresh_models, "utility")
        btn_refresh_models.clicked.connect(self._refresh_ai_provider_status)
        session_lay.addWidget(btn_refresh_models, 12, 0)

        btn_check_provider = QPushButton("Check Ollama")
        self._set_button_role(btn_check_provider, "utility")
        btn_check_provider.clicked.connect(self._refresh_ai_provider_status)
        session_lay.addWidget(btn_check_provider, 12, 1)

        lay.addWidget(session_grp)

        lay.addWidget(self._build_ai_voice_validation_group())

        coach_grp = QGroupBox("Assistant Workspace")
        coach_lay = QVBoxLayout(coach_grp)
        self._tabs_ai_workspace = QTabWidget()

        self._ai_assistant_page = QWidget()
        assistant_lay = QVBoxLayout(self._ai_assistant_page)
        assistant_lay.setContentsMargins(0, 0, 0, 0)
        assistant_lay.setSpacing(6)

        prompt_row = QHBoxLayout()
        self._edit_ai_prompt = QLineEdit()
        self._edit_ai_prompt.setPlaceholderText("Example: explain why nothing is engaging, summarize runtime state, or explicitly say switch to color detection")
        self._edit_ai_prompt.returnPressed.connect(self._run_ai_assistant_request)
        prompt_row.addWidget(self._edit_ai_prompt)
        btn_chat = QPushButton("Run Request")
        self._set_button_role(btn_chat, "utility")
        btn_chat.clicked.connect(self._run_ai_assistant_request)
        prompt_row.addWidget(btn_chat)
        assistant_lay.addLayout(prompt_row)

        self._txt_ai_output = QTextEdit()
        self._txt_ai_output.setReadOnly(True)
        self._txt_ai_output.setMinimumHeight(180)
        assistant_lay.addWidget(self._txt_ai_output)

        self._lbl_ai_examples = QLabel(
            "Try: 'why is nothing engaging?', 'summarize the current runtime', 'switch to color detection', 'enable human voice', 'go rest', or 'draft safer settings'."
        )
        self._lbl_ai_examples.setWordWrap(True)
        self._set_theme_role(self._lbl_ai_examples, "mutedCompact")
        assistant_lay.addWidget(self._lbl_ai_examples)

        self._tabs_ai_workspace.addTab(self._ai_assistant_page, "Assistant")

        self._ai_runtime_page = QWidget()
        runtime_lay = QVBoxLayout(self._ai_runtime_page)
        runtime_lay.setContentsMargins(0, 0, 0, 0)
        runtime_lay.setSpacing(6)

        self._lbl_ai_runtime_snapshot = QLabel(self._assistant_runtime_snapshot())
        self._lbl_ai_runtime_snapshot.setWordWrap(True)
        self._set_theme_role(self._lbl_ai_runtime_snapshot, "mutedCompact")
        runtime_lay.addWidget(self._lbl_ai_runtime_snapshot)

        runtime_btn_row = QHBoxLayout()
        btn_snapshot = QPushButton("Analyze")
        self._set_button_role(btn_snapshot, "utility")
        btn_snapshot.clicked.connect(self._run_ai_assistant_analysis)
        runtime_btn_row.addWidget(btn_snapshot)
        btn_suggest = QPushButton("Draft Tips")
        self._set_button_role(btn_suggest, "utility")
        btn_suggest.clicked.connect(self._run_ai_assistant_recommendations)
        runtime_btn_row.addWidget(btn_suggest)
        runtime_btn_row.addStretch(1)
        self._register_responsive_box_layout(runtime_btn_row, "dense_row")
        runtime_lay.addLayout(runtime_btn_row)

        self._txt_ai_runtime_output = QTextEdit()
        self._txt_ai_runtime_output.setReadOnly(True)
        self._txt_ai_runtime_output.setMinimumHeight(180)
        runtime_lay.addWidget(self._txt_ai_runtime_output)

        self._tabs_ai_workspace.addTab(self._ai_runtime_page, "Runtime Analyst")
        coach_lay.addWidget(self._tabs_ai_workspace)
        lay.addWidget(coach_grp)

        lay.addStretch()
        self._set_ai_model_tier(str(getattr(self.config.ai_assistant, "preferred_model_tier", "fast") or "fast"), persist=False)
        self._sync_ai_model_combo_entries([])
        self._append_ai_output(
            "Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline."
        )
        self._append_ai_output(
            "Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.",
            task_kind="analysis",
        )
        return w

    def _build_ai_voice_validation_group(self) -> QGroupBox:
        voice_grp = QGroupBox("AI Voice Validation")
        voice_lay = QVBoxLayout(voice_grp)
        voice_lay.setSpacing(6)

        intro = QLabel(
            "Validate the speech path used by spoken assistant replies. This checks Qt voice routing, selected voice application, and speech-state transitions before you rely on AI auto-speak."
        )
        intro.setWordWrap(True)
        self._set_theme_role(intro, "subtleBody")
        voice_lay.addWidget(intro)

        self._chk_ai_auto_speak = QCheckBox("Speak assistant replies with the local human voice")
        self._chk_ai_auto_speak.setChecked(bool(self.config.ai_assistant.auto_speak_responses))
        self._chk_ai_auto_speak.setEnabled(self._human_voice_supported())
        self._chk_ai_auto_speak.toggled.connect(self._on_ai_assistant_settings_changed)
        voice_lay.addWidget(self._chk_ai_auto_speak)

        self._lbl_ai_voice_validation_status = QLabel("AI voice route: waiting")
        self._lbl_ai_voice_validation_status.setWordWrap(True)
        self._set_theme_role(self._lbl_ai_voice_validation_status, "statusStrong")
        voice_lay.addWidget(self._lbl_ai_voice_validation_status)

        self._lbl_human_voice_diag_backend = QLabel("Backend: waiting")
        self._lbl_human_voice_diag_backend.setWordWrap(True)
        self._set_theme_role(self._lbl_human_voice_diag_backend, "mutedCompact")
        voice_lay.addWidget(self._lbl_human_voice_diag_backend)

        self._lbl_human_voice_diag_selected = QLabel("Selected voice: waiting")
        self._lbl_human_voice_diag_selected.setWordWrap(True)
        self._set_theme_role(self._lbl_human_voice_diag_selected, "mutedCompact")
        voice_lay.addWidget(self._lbl_human_voice_diag_selected)

        self._lbl_human_voice_diag_state = QLabel("Speech state: waiting")
        self._lbl_human_voice_diag_state.setWordWrap(True)
        self._set_theme_role(self._lbl_human_voice_diag_state, "mutedCompact")
        voice_lay.addWidget(self._lbl_human_voice_diag_state)

        self._lbl_human_voice_diag_route = QLabel("Route: Windows SAPI uses the current default playback device")
        self._lbl_human_voice_diag_route.setWordWrap(True)
        self._set_theme_role(self._lbl_human_voice_diag_route, "mutedCompact")
        voice_lay.addWidget(self._lbl_human_voice_diag_route)

        btn_row = QHBoxLayout()
        self._btn_ai_speak_last = QPushButton("Speak Reply")
        self._set_button_role(self._btn_ai_speak_last, "utility")
        self._btn_ai_speak_last.setEnabled(self._human_voice_supported())
        self._btn_ai_speak_last.clicked.connect(self._speak_last_ai_output)
        btn_row.addWidget(self._btn_ai_speak_last)

        self._btn_human_voice_refresh = QPushButton("Refresh")
        self._set_button_role(self._btn_human_voice_refresh, "utility")
        self._btn_human_voice_refresh.clicked.connect(self._on_refresh_human_voice_diagnostics_clicked)
        btn_row.addWidget(self._btn_human_voice_refresh)

        self._btn_human_voice_stop = QPushButton("Stop Voice")
        self._set_button_role(self._btn_human_voice_stop, "utility")
        self._btn_human_voice_stop.clicked.connect(self._on_stop_human_voice_clicked)
        btn_row.addWidget(self._btn_human_voice_stop)
        self._register_responsive_box_layout(btn_row, "dense_row")
        voice_lay.addLayout(btn_row)

        validate_row = QHBoxLayout()
        self._btn_human_voice_validate = QPushButton("Test Voice")
        self._set_button_role(self._btn_human_voice_validate, "utility")
        self._btn_human_voice_validate.clicked.connect(self._on_validate_human_voices_clicked)
        validate_row.addWidget(self._btn_human_voice_validate)

        self._btn_human_voice_validate_all = QPushButton("Scan Voices")
        self._set_button_role(self._btn_human_voice_validate_all, "utility")
        self._btn_human_voice_validate_all.clicked.connect(self._on_validate_all_human_voices_clicked)
        validate_row.addWidget(self._btn_human_voice_validate_all)

        self._btn_human_voice_fallback = QPushButton("Fallback")
        self._set_button_role(self._btn_human_voice_fallback, "utility")
        self._btn_human_voice_fallback.clicked.connect(self._on_test_human_voice_fallback_clicked)
        validate_row.addWidget(self._btn_human_voice_fallback)
        validate_row.addStretch(1)
        self._register_responsive_box_layout(validate_row, "dense_row")
        voice_lay.addLayout(validate_row)

        self._lbl_human_voice_diag_validation = QLabel("Validation: not run yet")
        self._lbl_human_voice_diag_validation.setWordWrap(True)
        self._set_theme_role(self._lbl_human_voice_diag_validation, "mutedCompact")
        voice_lay.addWidget(self._lbl_human_voice_diag_validation)
        return voice_grp

    # ------------------------------------------------------------------ #
    #  Manual Controls Tab
    # ------------------------------------------------------------------ #

    def _build_controls_tab(self) -> QWidget:
        """CHANGE WARNING: Manual controls here share the same clamped absolute-move path as Home/Move to Guard and now also host runtime snapshot export; keep this tab aligned with guard limits and live runtime state sources."""
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(6)

        command_intro = QLabel(
            "This command deck keeps the most-used runtime actions close together: link control, app-triggered sweep, output toggles, source selection, guarded fire, and runtime exports."
        )
        command_intro.setWordWrap(True)
        self._set_theme_role(command_intro, "subtleBody")
        lay.addWidget(command_intro)

        quick_grp = QGroupBox("Quick Actions")
        quick_lay = QGridLayout(quick_grp)
        quick_lay.setHorizontalSpacing(8)
        quick_lay.setVerticalSpacing(8)

        self._btn_quick_link = QPushButton("Link")
        self._btn_quick_link.setMinimumHeight(34)
        self._set_button_role(self._btn_quick_link, "primary")
        self._btn_quick_link.setToolTip(
            "Connect or disconnect the active Smart Sentry link. Use the header Wake Up and Go Rest buttons for manual position testing, Export for a timestamped read-only runtime capture, and Open Folder to jump to the saved files."
        )
        self._btn_quick_link.clicked.connect(self._toggle_connection)
        quick_lay.addWidget(self._btn_quick_link, 0, 0)

        btn_quick_save = QPushButton("Save")
        btn_quick_save.setMinimumHeight(34)
        self._set_button_role(btn_quick_save, "utility")
        btn_quick_save.setToolTip("Write the current Smart Sentry settings to disk immediately.")
        btn_quick_save.clicked.connect(self._save_config)
        quick_lay.addWidget(btn_quick_save, 0, 1)

        self._btn_export_runtime_snapshot = QPushButton("Export")
        self._btn_export_runtime_snapshot.setMinimumHeight(34)
        self._set_button_role(self._btn_export_runtime_snapshot, "utility")
        self._btn_export_runtime_snapshot.clicked.connect(self._export_runtime_snapshot)
        self._apply_tooltip(self._btn_export_runtime_snapshot, "export_runtime_snapshot")
        quick_lay.addWidget(self._btn_export_runtime_snapshot, 0, 2)

        self._btn_open_runtime_snapshot_folder = QPushButton("Open Folder")
        self._btn_open_runtime_snapshot_folder.setMinimumHeight(34)
        self._set_button_role(self._btn_open_runtime_snapshot_folder, "utility")
        self._btn_open_runtime_snapshot_folder.clicked.connect(self._open_runtime_snapshot_folder)
        self._apply_tooltip(self._btn_open_runtime_snapshot_folder, "open_runtime_snapshot_folder")
        quick_lay.addWidget(self._btn_open_runtime_snapshot_folder, 0, 3)
        self._register_responsive_button_grid(quick_lay)
        self._reflow_responsive_button_grid(quick_lay)

        lay.addWidget(quick_grp)

        rest_grp = QGroupBox("Rest Position")
        rest_lay = QGridLayout(rest_grp)
        rest_lay.setHorizontalSpacing(8)
        rest_lay.setVerticalSpacing(8)

        rest_note = QLabel(
            "Go Rest moves from the current angle to this rest position. Wake Up returns to the Guard Pan and Guard Tilt ready position."
        )
        rest_note.setWordWrap(True)
        self._set_theme_role(rest_note, "subtleBody")
        rest_lay.addWidget(rest_note, 0, 0, 1, 4)

        rest_lay.addWidget(QLabel("Rest Pan (deg):"), 1, 0)
        self._spin_command_rest_pan = QDoubleSpinBox()
        self._spin_command_rest_pan.setRange(SENTRY_PAN_MIN, SENTRY_PAN_MAX)
        self._spin_command_rest_pan.setSingleStep(1.0)
        self._spin_command_rest_pan.setValue(float(getattr(self.config.guard, "rest_pan", self.config.guard.guard_pan)))
        self._spin_command_rest_pan.setToolTip("Rest angle used by Go Rest. Wake Up returns to Guard Pan instead.")
        self._spin_command_rest_pan.valueChanged.connect(self._on_command_rest_position_changed)
        rest_lay.addWidget(self._spin_command_rest_pan, 1, 1)

        rest_lay.addWidget(QLabel("Rest Tilt (deg):"), 1, 2)
        self._spin_command_rest_tilt = QDoubleSpinBox()
        self._spin_command_rest_tilt.setRange(SENTRY_TILT_MIN, SENTRY_TILT_MAX)
        self._spin_command_rest_tilt.setSingleStep(1.0)
        self._spin_command_rest_tilt.setValue(float(getattr(self.config.guard, "rest_tilt", self.config.guard.guard_tilt)))
        self._spin_command_rest_tilt.setToolTip("Rest angle used by Go Rest. Wake Up returns to Guard Tilt instead.")
        self._spin_command_rest_tilt.valueChanged.connect(self._on_command_rest_position_changed)
        rest_lay.addWidget(self._spin_command_rest_tilt, 1, 3)

        btn_set_rest_current = QPushButton("Set As Rest")
        btn_set_rest_current.setMinimumHeight(34)
        self._set_button_role(btn_set_rest_current, "utility")
        btn_set_rest_current.clicked.connect(self._set_current_as_rest)
        self._apply_tooltip(btn_set_rest_current, "set_current_rest")
        rest_lay.addWidget(btn_set_rest_current, 2, 0, 1, 2)

        lay.addWidget(rest_grp)

        # --- D-pad manual movement ---
        dpad_grp = QGroupBox("Manual Turret Control")
        dpad_lay = QVBoxLayout(dpad_grp)

        # Speed / step controls
        spd_row = QHBoxLayout()
        spd_row.addWidget(QLabel("Step (deg):"))
        self._spin_step = QSpinBox()
        self._spin_step.setRange(1, 20)
        self._spin_step.setValue(5)
        self._apply_tooltip(self._spin_step, "manual_step")
        spd_row.addWidget(self._spin_step)
        dpad_lay.addLayout(spd_row)

        motion_row = QHBoxLayout()
        self._btn_motion_enable = QPushButton("Auto Motion: ON")
        self._btn_motion_enable.setCheckable(True)
        self._btn_motion_enable.setChecked(True)
        self._set_button_role(self._btn_motion_enable, "mode")
        self._btn_motion_enable.toggled.connect(self._on_pan_tilt_motion_toggled)
        self._btn_motion_enable.setToolTip("Disable automatic pan/tilt tracking and guard slews while keeping the Debug Board, PIR sensors, serial logging, and manual recovery controls active")
        motion_row.addWidget(self._btn_motion_enable)
        dpad_lay.addLayout(motion_row)

        motion_note = QLabel("When disabled, Smart Sentry tracking and PIR-driven slews stop sending pan/tilt moves, but manual arrows, Home, and Move to Guard still work.")
        motion_note.setWordWrap(True)
        self._set_theme_role(motion_note, "mutedCompact")
        dpad_lay.addWidget(motion_note)

        # Centered manual movement grid
        manual_button_w = 92
        manual_button_h = 40
        arrow_symbols = {
            "up_left": "\u2196",
            "up": "\u25B2",
            "up_right": "\u2197",
            "left": "\u25C0",
            "right": "\u25B6",
            "down_left": "\u2199",
            "down": "\u25BC",
            "down_right": "\u2198",
        }

        grid = QGridLayout()
        grid.setHorizontalSpacing(6)
        grid.setVerticalSpacing(6)
        for column in range(5):
            grid.setColumnStretch(column, 1)

        btn_top_left = QPushButton("TOP LEFT")
        btn_top_left.setFixedSize(manual_button_w, manual_button_h)
        self._set_button_role(btn_top_left, "utility")
        btn_top_left.clicked.connect(lambda: self._move_to_manual_corner("min", "max"))
        self._apply_tooltip(btn_top_left, "manual_top_left")
        grid.addWidget(btn_top_left, 0, 0, alignment=Qt.AlignCenter)

        btn_diag_up_left = QPushButton(arrow_symbols["up_left"])
        btn_diag_up_left.setFixedSize(manual_button_w, manual_button_h)
        self._set_button_role(btn_diag_up_left, "dpadArrow")
        btn_diag_up_left.clicked.connect(lambda: self._manual_move(-1, 1))
        self._apply_tooltip(btn_diag_up_left, "manual_up_left")
        grid.addWidget(btn_diag_up_left, 0, 1, alignment=Qt.AlignCenter)

        btn_max_tilt = QPushButton("MAX TILT")
        btn_max_tilt.setFixedSize(manual_button_w, manual_button_h)
        self._set_button_role(btn_max_tilt, "utility")
        btn_max_tilt.clicked.connect(lambda: self._move_to_manual_limit("tilt", "max"))
        self._apply_tooltip(btn_max_tilt, "manual_max_tilt")
        grid.addWidget(btn_max_tilt, 0, 2, alignment=Qt.AlignCenter)

        btn_diag_up_right = QPushButton(arrow_symbols["up_right"])
        btn_diag_up_right.setFixedSize(manual_button_w, manual_button_h)
        self._set_button_role(btn_diag_up_right, "dpadArrow")
        btn_diag_up_right.clicked.connect(lambda: self._manual_move(1, 1))
        self._apply_tooltip(btn_diag_up_right, "manual_up_right")
        grid.addWidget(btn_diag_up_right, 0, 3, alignment=Qt.AlignCenter)

        btn_top_right = QPushButton("TOP RIGHT")
        btn_top_right.setFixedSize(manual_button_w, manual_button_h)
        self._set_button_role(btn_top_right, "utility")
        btn_top_right.clicked.connect(lambda: self._move_to_manual_corner("max", "max"))
        self._apply_tooltip(btn_top_right, "manual_top_right")
        grid.addWidget(btn_top_right, 0, 4, alignment=Qt.AlignCenter)

        btn_up = QPushButton("\u25B2")  # up arrow
        btn_up.setFixedSize(manual_button_w, manual_button_h)
        self._set_button_role(btn_up, "dpadArrow")
        btn_up.clicked.connect(lambda: self._manual_move(0, 1))
        self._apply_tooltip(btn_up, "manual_up")
        grid.addWidget(btn_up, 1, 2, alignment=Qt.AlignCenter)

        btn_min_pan = QPushButton("MIN PAN")
        btn_min_pan.setFixedSize(manual_button_w, manual_button_h)
        self._set_button_role(btn_min_pan, "utility")
        btn_min_pan.clicked.connect(lambda: self._move_to_manual_limit("pan", "min"))
        self._apply_tooltip(btn_min_pan, "manual_min_pan")
        grid.addWidget(btn_min_pan, 2, 0, alignment=Qt.AlignCenter)

        btn_left = QPushButton("\u25C0")  # left arrow
        btn_left.setFixedSize(manual_button_w, manual_button_h)
        self._set_button_role(btn_left, "dpadArrow")
        btn_left.clicked.connect(lambda: self._manual_move(-1, 0))
        self._apply_tooltip(btn_left, "manual_left")
        grid.addWidget(btn_left, 2, 1, alignment=Qt.AlignCenter)

        btn_home = QPushButton("HOME")
        btn_home.setFixedSize(manual_button_w, manual_button_h)
        self._set_button_role(btn_home, "dpad")
        self._apply_tooltip(btn_home, "manual_home")
        btn_home.clicked.connect(self._on_home_clicked)
        grid.addWidget(btn_home, 2, 2, alignment=Qt.AlignCenter)

        btn_right = QPushButton("\u25B6")  # right arrow
        btn_right.setFixedSize(manual_button_w, manual_button_h)
        self._set_button_role(btn_right, "dpadArrow")
        btn_right.clicked.connect(lambda: self._manual_move(1, 0))
        self._apply_tooltip(btn_right, "manual_right")
        grid.addWidget(btn_right, 2, 3, alignment=Qt.AlignCenter)

        btn_max_pan = QPushButton("MAX PAN")
        btn_max_pan.setFixedSize(manual_button_w, manual_button_h)
        self._set_button_role(btn_max_pan, "utility")
        btn_max_pan.clicked.connect(lambda: self._move_to_manual_limit("pan", "max"))
        self._apply_tooltip(btn_max_pan, "manual_max_pan")
        grid.addWidget(btn_max_pan, 2, 4, alignment=Qt.AlignCenter)

        btn_down = QPushButton("\u25BC")  # down arrow
        btn_down.setFixedSize(manual_button_w, manual_button_h)
        self._set_button_role(btn_down, "dpadArrow")
        btn_down.clicked.connect(lambda: self._manual_move(0, -1))
        self._apply_tooltip(btn_down, "manual_down")
        grid.addWidget(btn_down, 3, 2, alignment=Qt.AlignCenter)

        btn_diag_down_left = QPushButton(arrow_symbols["down_left"])
        btn_diag_down_left.setFixedSize(manual_button_w, manual_button_h)
        self._set_button_role(btn_diag_down_left, "dpadArrow")
        btn_diag_down_left.clicked.connect(lambda: self._manual_move(-1, -1))
        self._apply_tooltip(btn_diag_down_left, "manual_down_left")
        grid.addWidget(btn_diag_down_left, 4, 1, alignment=Qt.AlignCenter)

        btn_min_tilt = QPushButton("MIN TILT")
        btn_min_tilt.setFixedSize(manual_button_w, manual_button_h)
        self._set_button_role(btn_min_tilt, "utility")
        btn_min_tilt.clicked.connect(lambda: self._move_to_manual_limit("tilt", "min"))
        self._apply_tooltip(btn_min_tilt, "manual_min_tilt")
        grid.addWidget(btn_min_tilt, 4, 2, alignment=Qt.AlignCenter)

        btn_diag_down_right = QPushButton(arrow_symbols["down_right"])
        btn_diag_down_right.setFixedSize(manual_button_w, manual_button_h)
        self._set_button_role(btn_diag_down_right, "dpadArrow")
        btn_diag_down_right.clicked.connect(lambda: self._manual_move(1, -1))
        self._apply_tooltip(btn_diag_down_right, "manual_down_right")
        grid.addWidget(btn_diag_down_right, 4, 3, alignment=Qt.AlignCenter)

        btn_bottom_left = QPushButton("BOT LEFT")
        btn_bottom_left.setFixedSize(manual_button_w, manual_button_h)
        self._set_button_role(btn_bottom_left, "utility")
        btn_bottom_left.clicked.connect(lambda: self._move_to_manual_corner("min", "min"))
        self._apply_tooltip(btn_bottom_left, "manual_bottom_left")
        grid.addWidget(btn_bottom_left, 4, 0, alignment=Qt.AlignCenter)

        btn_bottom_right = QPushButton("BOT RIGHT")
        btn_bottom_right.setFixedSize(manual_button_w, manual_button_h)
        self._set_button_role(btn_bottom_right, "utility")
        btn_bottom_right.clicked.connect(lambda: self._move_to_manual_corner("max", "min"))
        self._apply_tooltip(btn_bottom_right, "manual_bottom_right")
        grid.addWidget(btn_bottom_right, 4, 4, alignment=Qt.AlignCenter)

        self._manual_control_buttons = [
            btn_top_left,
            btn_diag_up_left,
            btn_max_tilt,
            btn_diag_up_right,
            btn_top_right,
            btn_up,
            btn_min_pan,
            btn_left,
            btn_home,
            btn_right,
            btn_max_pan,
            btn_down,
            btn_diag_down_left,
            btn_min_tilt,
            btn_diag_down_right,
            btn_bottom_left,
            btn_bottom_right,
        ]

        dpad_lay.addLayout(grid)

        preset_note = QLabel("Corner presets use pan-and-tilt limit combinations, while arrow buttons use the configured step size. All manual controls share the same clamp path as guard/Home moves.")
        preset_note.setWordWrap(True)
        self._set_theme_role(preset_note, "mutedCompact")
        dpad_lay.addWidget(preset_note)

        self._btn_manual_sweep = QPushButton("RUN SWEEP")
        self._btn_manual_sweep.setMinimumHeight(34)
        self._set_button_role(self._btn_manual_sweep, "primary")
        self._btn_manual_sweep.clicked.connect(self._on_manual_sweep_clicked)
        self._btn_manual_sweep.setToolTip("Run a slow manual sweep using the configured sweep pan range and tilt limits")
        dpad_lay.addWidget(self._btn_manual_sweep)

        lay.addWidget(dpad_grp)

        # --- Outputs ---
        acc_grp = QGroupBox("Bridge Outputs")
        acc_lay = QGridLayout(acc_grp)

        self._btn_led = QPushButton("LED: OFF")
        self._btn_led.setCheckable(True)
        self._set_button_role(self._btn_led, "mode")
        self._btn_led.toggled.connect(self._on_led_toggled)
        self._apply_tooltip(self._btn_led, "led_toggle")
        acc_lay.addWidget(self._btn_led, 0, 0)

        self._btn_laser = QPushButton("Laser: OFF")
        self._btn_laser.setCheckable(True)
        self._set_button_role(self._btn_laser, "mode")
        self._btn_laser.toggled.connect(self._on_laser_toggled)
        self._apply_tooltip(self._btn_laser, "laser_toggle")
        acc_lay.addWidget(self._btn_laser, 0, 1)

        self._btn_acc = QPushButton("ACC: OFF")
        self._btn_acc.setCheckable(True)
        self._set_button_role(self._btn_acc, "mode")
        self._btn_acc.toggled.connect(self._on_acc_toggled)
        self._apply_tooltip(self._btn_acc, "acc_toggle")
        acc_lay.addWidget(self._btn_acc, 0, 2)

        self._btn_spare = QPushButton("Spare: OFF")
        self._btn_spare.setCheckable(True)
        self._set_button_role(self._btn_spare, "mode")
        self._btn_spare.toggled.connect(self._on_spare_toggled)
        self._apply_tooltip(self._btn_spare, "spare_toggle")
        acc_lay.addWidget(self._btn_spare, 1, 0)

        acc_note = QLabel("These toggles drive bridge-owned outputs only. Trigger arming and fire remain in the guarded section below.")
        acc_note.setWordWrap(True)
        self._set_theme_role(acc_note, "mutedCompact")
        acc_lay.addWidget(acc_note, 1, 1, 1, 2)

        self._lbl_optional_outputs_status = QLabel("Optional outputs: waiting for bridge capability packet")
        self._lbl_optional_outputs_status.setWordWrap(True)
        self._set_theme_role(self._lbl_optional_outputs_status, "statusStrong")
        acc_lay.addWidget(self._lbl_optional_outputs_status, 2, 0, 1, 3)

        lay.addWidget(acc_grp)

        # --- Auto Lighting Control ---
        lighting_grp = QGroupBox("Auto Lighting Control")
        lighting_lay = QVBoxLayout(lighting_grp)

        lighting_note = QLabel(
            "When enabled the LED intensity is adjusted automatically based on scene brightness. "
            "The LED button must be ON for auto-lighting to drive the output."
        )
        lighting_note.setWordWrap(True)
        self._set_theme_role(lighting_note, "subtle")
        lighting_lay.addWidget(lighting_note)

        self._chk_auto_lighting = QCheckBox("Auto Lighting: OFF")
        self._chk_auto_lighting.setChecked(bool(getattr(self.config.lighting, "auto_lighting_enabled", False)))
        self._chk_auto_lighting.toggled.connect(self._on_auto_lighting_toggled)
        lighting_lay.addWidget(self._chk_auto_lighting)

        pwm_row = QHBoxLayout()
        pwm_row.addWidget(QLabel("Manual LED PWM:"))
        self._slider_led_pwm = QSlider(Qt.Horizontal)
        self._slider_led_pwm.setRange(0, 255)
        self._slider_led_pwm.setSingleStep(5)
        self._slider_led_pwm.setPageStep(20)
        self._slider_led_pwm.setValue(int(max(0, min(255, getattr(self.config.lighting, "led_pwm_value", 255)))))
        self._slider_led_pwm.valueChanged.connect(self._on_led_pwm_slider_changed)
        pwm_row.addWidget(self._slider_led_pwm, 1)
        self._lbl_led_pwm = QLabel("255")
        self._lbl_led_pwm.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self._set_theme_role(self._lbl_led_pwm, "compactValue")
        pwm_row.addWidget(self._lbl_led_pwm)
        lighting_lay.addLayout(pwm_row)

        thresh_row = QHBoxLayout()
        thresh_row.addWidget(QLabel("Dark threshold (0-255):"))
        self._spin_auto_brightness_threshold = QSpinBox()
        self._spin_auto_brightness_threshold.setRange(0, 255)
        self._spin_auto_brightness_threshold.setValue(int(max(0, min(255, getattr(self.config.lighting, "auto_brightness_threshold", 80)))))
        self._spin_auto_brightness_threshold.valueChanged.connect(self._on_auto_brightness_threshold_changed)
        thresh_row.addWidget(self._spin_auto_brightness_threshold)
        thresh_row.addStretch(1)
        lighting_lay.addLayout(thresh_row)

        pwm_range_row = QHBoxLayout()
        pwm_range_row.addWidget(QLabel("Auto PWM range:"))
        self._spin_auto_pwm_min = QSpinBox()
        self._spin_auto_pwm_min.setRange(0, 255)
        self._spin_auto_pwm_min.setValue(int(max(0, min(255, getattr(self.config.lighting, "auto_pwm_min", 60)))))
        self._spin_auto_pwm_min.setPrefix("min: ")
        self._spin_auto_pwm_min.valueChanged.connect(lambda _: self._on_auto_pwm_range_changed())
        pwm_range_row.addWidget(self._spin_auto_pwm_min)
        self._spin_auto_pwm_max = QSpinBox()
        self._spin_auto_pwm_max.setRange(0, 255)
        self._spin_auto_pwm_max.setValue(int(max(0, min(255, getattr(self.config.lighting, "auto_pwm_max", 255)))))
        self._spin_auto_pwm_max.setPrefix("max: ")
        self._spin_auto_pwm_max.valueChanged.connect(lambda _: self._on_auto_pwm_range_changed())
        pwm_range_row.addWidget(self._spin_auto_pwm_max)
        pwm_range_row.addStretch(1)
        lighting_lay.addLayout(pwm_range_row)

        self._lbl_auto_luma = QLabel("Scene luma: --  PWM: --")
        self._set_theme_role(self._lbl_auto_luma, "mutedCompact")
        lighting_lay.addWidget(self._lbl_auto_luma)

        lay.addWidget(lighting_grp)

        source_grp = QGroupBox("Source And Interlocks")
        source_lay = QVBoxLayout(source_grp)

        source_note = QLabel("Use the UI button or FlySky CH6 to request APP or RC control source. Trigger output is currently gated by software safety and fault state only.")
        source_note.setWordWrap(True)
        self._set_theme_role(source_note, "subtle")
        source_lay.addWidget(source_note)

        self._btn_control_source = QPushButton("Control Source: APP")
        self._btn_control_source.setCheckable(True)
        self._set_button_role(self._btn_control_source, "mode")
        self._btn_control_source.toggled.connect(self._on_control_source_toggled)
        source_lay.addWidget(self._btn_control_source)

        self._lbl_control_source_status = QLabel("FlySky mode: waiting for bridge runtime")
        self._lbl_control_source_status.setWordWrap(True)
        self._set_theme_role(self._lbl_control_source_status, "statusStrong")
        source_lay.addWidget(self._lbl_control_source_status)

        # --- Safety and Manual Fire ---
        fire_grp = QGroupBox("Fire Control And Sound")
        fire_lay = QVBoxLayout(fire_grp)

        fire_note = QLabel("Arm Safety before using manual fire. Safety is isolated here so it is not visually mixed with ordinary accessory toggles.")
        fire_note.setWordWrap(True)
        self._set_theme_role(fire_note, "subtle")
        fire_lay.addWidget(fire_note)

        self._btn_safety = QPushButton("Safety: LOCKED")
        self._btn_safety.setCheckable(True)
        self._set_button_role(self._btn_safety, "danger")
        self._btn_safety.toggled.connect(self._on_safety_toggled)
        self._apply_tooltip(self._btn_safety, "safety_toggle")
        fire_lay.addWidget(self._btn_safety)

        self._btn_fire = QPushButton("FIRE")
        self._set_button_role(self._btn_fire, "danger")
        self._btn_fire.setMinimumHeight(36)
        self._btn_fire.pressed.connect(lambda: self._on_manual_fire(1))
        self._btn_fire.released.connect(lambda: self._on_manual_fire(0))
        self._apply_tooltip(self._btn_fire, "manual_fire")
        fire_lay.addWidget(self._btn_fire)

        self._chk_sound_enabled = QCheckBox("Sound: ON")
        self._chk_sound_enabled.setChecked(bool(getattr(self.config.sound, "enabled", True)))
        self._chk_sound_enabled.toggled.connect(self._on_sound_enabled_changed)
        self._apply_tooltip(self._chk_sound_enabled, "sound_enabled")
        fire_lay.addWidget(self._chk_sound_enabled)

        sound_row = QHBoxLayout()
        sound_row.addWidget(QLabel("Volume:"))
        self._slider_sound_volume = QSlider(Qt.Horizontal)
        self._slider_sound_volume.setRange(0, 100)
        self._slider_sound_volume.setSingleStep(5)
        self._slider_sound_volume.setPageStep(10)
        self._slider_sound_volume.setValue(int(max(0, min(100, int(getattr(self.config.sound, "volume_pct", 100) or 100)))))
        self._slider_sound_volume.valueChanged.connect(self._on_sound_volume_changed)
        self._apply_tooltip(self._slider_sound_volume, "sound_volume")
        sound_row.addWidget(self._slider_sound_volume, 1)
        self._lbl_sound_volume = QLabel("100%")
        self._lbl_sound_volume.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self._set_theme_role(self._lbl_sound_volume, "compactValue")
        sound_row.addWidget(self._lbl_sound_volume)
        fire_lay.addLayout(sound_row)

        personality_row = QHBoxLayout()
        personality_row.addWidget(QLabel("Personality:"))
        self._combo_sound_personality = QComboBox()
        for personality_key, personality_label in SOUND_PERSONALITY_OPTIONS:
            self._combo_sound_personality.addItem(personality_label, personality_key)
        self._combo_sound_personality.currentIndexChanged.connect(self._on_sound_personality_changed)
        personality_row.addWidget(self._combo_sound_personality, 1)
        fire_lay.addLayout(personality_row)

        attitude_row = QHBoxLayout()
        attitude_row.addWidget(QLabel("Attitude:"))
        self._slider_sound_attitude = QSlider(Qt.Horizontal)
        self._slider_sound_attitude.setRange(0, 100)
        self._slider_sound_attitude.setSingleStep(5)
        self._slider_sound_attitude.setPageStep(10)
        self._slider_sound_attitude.valueChanged.connect(self._on_sound_attitude_changed)
        attitude_row.addWidget(self._slider_sound_attitude, 1)
        self._lbl_sound_attitude = QLabel("60%")
        self._lbl_sound_attitude.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self._set_theme_role(self._lbl_sound_attitude, "compactValue")
        attitude_row.addWidget(self._lbl_sound_attitude)
        fire_lay.addLayout(attitude_row)

        self._lbl_sound_profile = QLabel("Profile: Sentinel")
        self._lbl_sound_profile.setWordWrap(True)
        self._set_theme_role(self._lbl_sound_profile, "statusStrong")
        fire_lay.addWidget(self._lbl_sound_profile)

        self._chk_human_voice_enabled = QCheckBox("Human voice speech")
        self._chk_human_voice_enabled.setChecked(bool(getattr(self.config.sound, "human_voice_enabled", False)))
        self._chk_human_voice_enabled.setEnabled(self._human_voice_supported())
        self._chk_human_voice_enabled.toggled.connect(self._on_human_voice_enabled_changed)
        fire_lay.addWidget(self._chk_human_voice_enabled)

        self._chk_mute_buzzer_for_human_voice = QCheckBox("Mute ESP32 buzzer while human voice mode is enabled")
        self._chk_mute_buzzer_for_human_voice.setChecked(bool(getattr(self.config.sound, "mute_buzzer_when_human_voice_enabled", True)))
        self._chk_mute_buzzer_for_human_voice.toggled.connect(self._on_mute_buzzer_for_human_voice_changed)
        fire_lay.addWidget(self._chk_mute_buzzer_for_human_voice)

        human_style_row = QHBoxLayout()
        human_style_row.addWidget(QLabel("Speech Style:"))
        self._combo_human_voice_style = QComboBox()
        for style_key, style_data in HUMAN_VOICE_STYLE_PRESETS.items():
            self._combo_human_voice_style.addItem(str(style_data["label"]), style_key)
        self._combo_human_voice_style.currentIndexChanged.connect(self._on_human_voice_style_changed)
        human_style_row.addWidget(self._combo_human_voice_style, 1)
        fire_lay.addLayout(human_style_row)

        human_voice_row = QHBoxLayout()
        human_voice_row.addWidget(QLabel("Voice:"))
        self._combo_human_voice = QComboBox()
        self._combo_human_voice.currentIndexChanged.connect(self._on_human_voice_name_changed)
        human_voice_row.addWidget(self._combo_human_voice, 1)
        self._btn_test_human_voice = QPushButton("Test Voice")
        self._set_button_role(self._btn_test_human_voice, "utility")
        self._btn_test_human_voice.clicked.connect(self._on_test_human_voice_clicked)
        human_voice_row.addWidget(self._btn_test_human_voice)
        fire_lay.addLayout(human_voice_row)

        human_rate_row = QHBoxLayout()
        human_rate_row.addWidget(QLabel("Voice Rate:"))
        self._slider_human_voice_rate = QSlider(Qt.Horizontal)
        self._slider_human_voice_rate.setRange(50, 150)
        self._slider_human_voice_rate.setSingleStep(5)
        self._slider_human_voice_rate.setValue(int(getattr(self.config.sound, "human_voice_rate_pct", 100) or 100))
        self._slider_human_voice_rate.valueChanged.connect(self._on_human_voice_rate_changed)
        human_rate_row.addWidget(self._slider_human_voice_rate, 1)
        self._lbl_human_voice_rate = QLabel("100%")
        self._set_theme_role(self._lbl_human_voice_rate, "compactValue")
        human_rate_row.addWidget(self._lbl_human_voice_rate)
        fire_lay.addLayout(human_rate_row)

        human_pitch_row = QHBoxLayout()
        human_pitch_row.addWidget(QLabel("Voice Pitch:"))
        self._slider_human_voice_pitch = QSlider(Qt.Horizontal)
        self._slider_human_voice_pitch.setRange(50, 150)
        self._slider_human_voice_pitch.setSingleStep(5)
        self._slider_human_voice_pitch.setValue(int(getattr(self.config.sound, "human_voice_pitch_pct", 100) or 100))
        self._slider_human_voice_pitch.valueChanged.connect(self._on_human_voice_pitch_changed)
        human_pitch_row.addWidget(self._slider_human_voice_pitch, 1)
        self._lbl_human_voice_pitch = QLabel("100%")
        self._set_theme_role(self._lbl_human_voice_pitch, "compactValue")
        human_pitch_row.addWidget(self._lbl_human_voice_pitch)
        fire_lay.addLayout(human_pitch_row)

        human_volume_row = QHBoxLayout()
        human_volume_row.addWidget(QLabel("Voice Volume:"))
        self._slider_human_voice_volume = QSlider(Qt.Horizontal)
        self._slider_human_voice_volume.setRange(0, 100)
        self._slider_human_voice_volume.setSingleStep(5)
        self._slider_human_voice_volume.setValue(int(getattr(self.config.sound, "human_voice_volume_pct", 85) or 85))
        self._slider_human_voice_volume.valueChanged.connect(self._on_human_voice_volume_changed)
        human_volume_row.addWidget(self._slider_human_voice_volume, 1)
        self._lbl_human_voice_volume = QLabel("85%")
        self._set_theme_role(self._lbl_human_voice_volume, "compactValue")
        human_volume_row.addWidget(self._lbl_human_voice_volume)
        fire_lay.addLayout(human_volume_row)

        self._lbl_human_voice_status = QLabel("Human voice: waiting")
        self._lbl_human_voice_status.setWordWrap(True)
        self._set_theme_role(self._lbl_human_voice_status, "statusStrong")
        fire_lay.addWidget(self._lbl_human_voice_status)

        self._lbl_sound_status = QLabel("Sound link: waiting")
        self._lbl_sound_status.setWordWrap(True)
        self._set_theme_role(self._lbl_sound_status, "statusStrong")
        fire_lay.addWidget(self._lbl_sound_status)

        self._lbl_fire_interlock_status = QLabel("Manual fire interlock: waiting")
        self._lbl_fire_interlock_status.setWordWrap(True)
        self._set_theme_role(self._lbl_fire_interlock_status, "statusStrong")
        fire_lay.addWidget(self._lbl_fire_interlock_status)

        self._refresh_sound_toggle_text()
        self._sync_sound_widgets()

        lay.addWidget(source_grp)
        lay.addWidget(fire_grp)

        lay.addStretch()
        return w

    # ------------------------------------------------------------------ #
    #  Status + Log Groups
    # ------------------------------------------------------------------ #

    def _build_status_group(self) -> QGroupBox:
        grp = QGroupBox("Command Status")
        grp.setMinimumHeight(120)
        grp.setMaximumHeight(16777215)
        grp.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        lay = QVBoxLayout(grp)
        lay.setContentsMargins(8, 8, 8, 8)
        lay.setSpacing(6)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setFrameShape(QFrame.NoFrame)
        scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        lay.addWidget(scroll, stretch=1)

        content = QWidget()
        scroll.setWidget(content)
        content_lay = QVBoxLayout(content)
        content_lay.setContentsMargins(0, 0, 2, 0)
        content_lay.setSpacing(6)

        def _make_status_card(title: str, value: str, accent: str) -> tuple[QFrame, QLabel]:
            frame = QFrame()
            frame.setObjectName("sentryV2StatusCard")
            frame.setProperty("accentColor", accent)
            frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            card_layout = QVBoxLayout(frame)
            card_layout.setContentsMargins(8, 6, 8, 6)
            card_layout.setSpacing(2)

            title_lbl = QLabel(title)
            title_lbl.setProperty("themeRole", "statusCardTitle")
            card_layout.addWidget(title_lbl)

            value_lbl = QLabel(value)
            value_lbl.setWordWrap(True)
            value_lbl.setProperty("themeRole", "statusCardValue")
            card_layout.addWidget(value_lbl)
            return frame, value_lbl

        self._lbl_hw_monitor_title = QLabel("Bridge • Tracking • Hardware Snapshot")
        self._lbl_hw_monitor_title.setProperty("themeRole", "statusSectionTitle")
        content_lay.addWidget(self._lbl_hw_monitor_title)

        card_row = QHBoxLayout()
        card_row.setSpacing(6)

        state_card, self._lbl_state = _make_status_card("STATE", "PAUSED", "#e0a169")
        fire_card, self._lbl_hw_safety = _make_status_card("FIRE PATH", "BLOCKED", "#d87a62")
        target_card, self._lbl_stats = _make_status_card("TARGETS", "0 visible", "#94bf7d")

        card_row.addWidget(state_card, 1)
        card_row.addWidget(fire_card, 1)
        card_row.addWidget(target_card, 1)
        content_lay.addLayout(card_row)

        position_frame = QFrame()
        position_frame.setObjectName("sentryV2StatusSubframe")
        position_layout = QGridLayout(position_frame)
        position_layout.setContentsMargins(8, 7, 8, 7)
        position_layout.setHorizontalSpacing(8)
        position_layout.setVerticalSpacing(4)

        self._lbl_angles = QLabel("Pan 0.0°")
        self._lbl_angles.setProperty("themeRole", "statusValue")
        position_layout.addWidget(self._lbl_angles, 0, 0)

        self._bar_pan_status = QProgressBar()
        self._bar_pan_status.setRange(0, 1000)
        self._bar_pan_status.setTextVisible(False)
        self._bar_pan_status.setFixedHeight(10)
        self._bar_pan_status.setProperty("barRole", "pan")
        position_layout.addWidget(self._bar_pan_status, 0, 1)

        self._lbl_angles_controls = QLabel("Tilt 0.0°")
        self._lbl_angles_controls.setProperty("themeRole", "statusValue")
        position_layout.addWidget(self._lbl_angles_controls, 1, 0)

        self._bar_tilt_status = QProgressBar()
        self._bar_tilt_status.setRange(0, 1000)
        self._bar_tilt_status.setTextVisible(False)
        self._bar_tilt_status.setFixedHeight(10)
        self._bar_tilt_status.setProperty("barRole", "tilt")
        position_layout.addWidget(self._bar_tilt_status, 1, 1)

        content_lay.addWidget(position_frame)

        detail_grid = QGridLayout()
        detail_grid.setHorizontalSpacing(10)
        detail_grid.setVerticalSpacing(3)

        self._lbl_motion_gate = QLabel("Tracking: idle")
        self._lbl_motion_gate.setWordWrap(True)
        self._lbl_motion_gate.setProperty("themeRole", "statusDetail")
        detail_grid.addWidget(self._lbl_motion_gate, 0, 0)

        self._lbl_servo_feedback = QLabel("Feedback: inactive")
        self._lbl_servo_feedback.setWordWrap(True)
        self._lbl_servo_feedback.setProperty("themeRole", "statusDetail")
        detail_grid.addWidget(self._lbl_servo_feedback, 0, 1)

        self._lbl_hw_servo_health = QLabel("Servo monitor: waiting")
        self._lbl_hw_servo_health.setWordWrap(True)
        self._lbl_hw_servo_health.setProperty("themeRole", "statusDetail")
        detail_grid.addWidget(self._lbl_hw_servo_health, 1, 0)

        self._lbl_hw_current = QLabel("Current: unavailable")
        self._lbl_hw_current.setWordWrap(True)
        self._lbl_hw_current.setProperty("themeRole", "statusDetail")
        detail_grid.addWidget(self._lbl_hw_current, 1, 1)

        self._lbl_no_fire_status = QLabel("No-fire: clear")
        self._lbl_no_fire_status.setWordWrap(True)
        self._lbl_no_fire_status.setProperty("themeRole", "statusDetail")
        detail_grid.addWidget(self._lbl_no_fire_status, 2, 0)

        self._lbl_recovery_status = QLabel("Recovery: idle")
        self._lbl_recovery_status.setWordWrap(True)
        self._lbl_recovery_status.setProperty("themeRole", "statusDetail")
        detail_grid.addWidget(self._lbl_recovery_status, 2, 1)

        content_lay.addLayout(detail_grid)

        bridge_frame = QFrame()
        bridge_frame.setObjectName("sentryV2StatusSubframe")
        bridge_layout = QVBoxLayout(bridge_frame)
        bridge_layout.setContentsMargins(8, 7, 8, 7)
        bridge_layout.setSpacing(3)

        bridge_title = QLabel("Bridge Runtime")
        bridge_title.setProperty("themeRole", "statusSectionTitle")
        bridge_layout.addWidget(bridge_title)

        self._lbl_bridge_runtime = QLabel("Bridge: waiting")
        self._lbl_bridge_runtime.setWordWrap(True)
        self._lbl_bridge_runtime.setProperty("themeRole", "statusDetail")
        bridge_layout.addWidget(self._lbl_bridge_runtime)

        self._lbl_bridge_caps = QLabel("Caps: waiting")
        self._lbl_bridge_caps.setWordWrap(True)
        self._lbl_bridge_caps.setProperty("themeRole", "statusDetail")
        bridge_layout.addWidget(self._lbl_bridge_caps)

        self._lbl_bridge_warning = QLabel("Bridge warning: none")
        self._lbl_bridge_warning.setWordWrap(True)
        self._lbl_bridge_warning.setProperty("themeRole", "statusBadge")
        bridge_layout.addWidget(self._lbl_bridge_warning)

        content_lay.addWidget(bridge_frame)
        content_lay.addStretch(1)

        return grp

    def _build_log_group(self) -> QGroupBox:
        grp = QGroupBox("Serial / Transport Output")
        grp.setMinimumHeight(120)
        grp.setMaximumHeight(16777215)
        grp.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        lay = QVBoxLayout(grp)
        lay.setContentsMargins(8, 8, 8, 8)
        lay.setSpacing(6)

        self._log_text = QTextEdit()
        self._log_text.setObjectName("sentryV2Log")
        self._log_text.setReadOnly(True)
        lay.addWidget(self._log_text, stretch=1)

        filter_row = QHBoxLayout()
        filter_row.setContentsMargins(0, 0, 0, 0)
        filter_row.setSpacing(4)

        def _log_chip(text: str, *, role: str = "utility", checkable: bool = False) -> QPushButton:
            b = QPushButton(text)
            b.setCheckable(checkable)
            b.setProperty("quickAccessChip", "true")
            b.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
            b.setMinimumWidth(48)
            self._set_button_role(b, role)
            return b

        self._btn_log_pause = _log_chip("Pause", role="utility")
        self._btn_log_pause.clicked.connect(lambda: self._set_log_pause(True))
        filter_row.addWidget(self._btn_log_pause)

        self._btn_log_resume = _log_chip("Resume", role="primary")
        self._btn_log_resume.clicked.connect(lambda: self._set_log_pause(False))
        filter_row.addWidget(self._btn_log_resume)

        self._lbl_log_state = QLabel("Live")
        self._lbl_log_state.setObjectName("sentryV2QuickAccessHint")
        filter_row.addWidget(self._lbl_log_state)

        filter_row.addSpacing(6)
        for key, label in SERIAL_LOG_FILTER_SPECS:
            button = _log_chip(label, role="mode", checkable=True)
            button.clicked.connect(lambda _checked=False, selected=key: self._set_log_filter(selected))
            filter_row.addWidget(button)
            self._log_filter_buttons[key] = button

        filter_row.addSpacing(6)

        btn_export = _log_chip("Export", role="utility")
        btn_export.clicked.connect(self._export_serial_log)
        self._apply_tooltip(btn_export, "export_serial_log")
        filter_row.addWidget(btn_export)

        btn_open_folder = _log_chip("Log Folder", role="utility")
        btn_open_folder.clicked.connect(self._open_serial_log_folder)
        self._apply_tooltip(btn_open_folder, "open_serial_log_folder")
        filter_row.addWidget(btn_open_folder)

        btn_clear = _log_chip("Clear", role="danger")
        btn_clear.clicked.connect(self._clear_serial_log)
        filter_row.addWidget(btn_clear)

        filter_row.addStretch(1)
        lay.addLayout(filter_row)

        self._sync_log_controls()

        return grp

    def _apply_saved_log_panel_height(self) -> None:
        if not hasattr(self, "_layout_splitter"):
            return
        total_height = max(1, self._layout_splitter.size().height())
        lower_height = max(150, min(300, int(total_height * 0.24)))
        video_height = max(1, total_height - lower_height)
        self._layout_splitter.setSizes([video_height, lower_height])

    def _apply_bottom_info_panel_widths(self) -> None:
        if not hasattr(self, "_bottom_info_splitter"):
            return
        total_width = max(1, self._bottom_info_splitter.size().width())
        if total_width <= 1:
            total_width = max(520, int(self.width() * 0.44))
        log_width = max(220, int(total_width * 0.40))
        status_width = max(260, total_width - log_width)
        self._bottom_info_splitter.setSizes([log_width, status_width])

    def _splitter_sizes_if_ready(self, splitter: QSplitter) -> list[int]:
        sizes = [int(v) for v in splitter.sizes()]
        if len(sizes) < 2:
            return []
        if splitter.orientation() == Qt.Horizontal:
            axis_extent = splitter.size().width()
        else:
            axis_extent = splitter.size().height()
        if axis_extent <= 32 or sum(sizes) <= 32:
            return []
        return sizes

    def _layout_geometry_ready(self) -> bool:
        if self.width() <= 32 or self.height() <= 32:
            return False
        for splitter_name in ("_main_splitter", "_layout_splitter", "_bottom_info_splitter"):
            splitter = getattr(self, splitter_name, None)
            if splitter is None:
                return False
            if not self._splitter_sizes_if_ready(splitter):
                return False
        return True

    def _capture_layout_state(self) -> None:
        if hasattr(self, "_main_splitter"):
            panel_sizes = self._splitter_sizes_if_ready(self._main_splitter)
            if panel_sizes:
                self.config.main_splitter_sizes = panel_sizes
                self.config.settings_panel_width = max(SENTRY_V2_PANEL_MIN_WIDTH, int(panel_sizes[1]))
        if hasattr(self, "_layout_splitter"):
            layout_sizes = self._splitter_sizes_if_ready(self._layout_splitter)
            if layout_sizes:
                self.config.layout_splitter_sizes = layout_sizes
        if hasattr(self, "_bottom_info_splitter"):
            bottom_sizes = self._splitter_sizes_if_ready(self._bottom_info_splitter)
            if bottom_sizes:
                self.config.bottom_info_splitter_sizes = bottom_sizes

    def _apply_saved_layout_state(self) -> None:
        if not self.isVisible() or self.width() <= 32 or self.height() <= 32:
            if self._layout_restore_attempts < 6:
                self._layout_restore_attempts += 1
                QTimer.singleShot(0, self._apply_saved_layout_state)
            return

        main_sizes = [int(v) for v in getattr(self.config, "main_splitter_sizes", []) if int(v) > 0]
        if len(main_sizes) >= 2:
            self._main_splitter.setSizes(main_sizes[:2])
        else:
            saved_panel_width = int(getattr(self.config, "settings_panel_width", SENTRY_V2_PANEL_DEFAULT_WIDTH) or SENTRY_V2_PANEL_DEFAULT_WIDTH)
            self._apply_panel_width(saved_panel_width)

        layout_sizes = [int(v) for v in getattr(self.config, "layout_splitter_sizes", []) if int(v) > 0]
        if len(layout_sizes) >= 2:
            self._layout_splitter.setSizes(layout_sizes[:2])
        else:
            self._apply_saved_log_panel_height()

        bottom_sizes = [int(v) for v in getattr(self.config, "bottom_info_splitter_sizes", []) if int(v) > 0]
        if len(bottom_sizes) >= 2:
            self._bottom_info_splitter.setSizes(bottom_sizes[:2])
        else:
            self._apply_bottom_info_panel_widths()

        self._layout_restore_complete = True
        self._layout_restore_attempts = 0
        if self._layout_geometry_ready():
            self._capture_layout_state()
        self._update_responsive_layout()

    def restore_window_geometry(self, window: QWidget) -> None:
        width = max(int(window.minimumWidth() or 1), int(getattr(self.config, "window_width", 1280) or 1280))
        height = max(int(window.minimumHeight() or 1), int(getattr(self.config, "window_height", 860) or 860))
        window.resize(width, height)
        pos_x = int(getattr(self.config, "window_x", -1) or -1)
        pos_y = int(getattr(self.config, "window_y", -1) or -1)
        if pos_x >= 0 and pos_y >= 0:
            window.move(pos_x, pos_y)
        if bool(getattr(self.config, "window_maximized", False)):
            window.showMaximized()

    def persist_window_geometry(self, window: QWidget, *, immediate: bool = False) -> None:
        self._capture_layout_state()
        normal_geometry = window.normalGeometry() if hasattr(window, "normalGeometry") else None
        geometry = normal_geometry if window.isMaximized() and normal_geometry is not None and normal_geometry.isValid() else window.geometry()
        if geometry is not None and geometry.isValid():
            self.config.window_x = int(geometry.x())
            self.config.window_y = int(geometry.y())
            self.config.window_width = max(int(window.minimumWidth() or 1), int(geometry.width()))
            self.config.window_height = max(int(window.minimumHeight() or 1), int(geometry.height()))
        self.config.window_maximized = bool(window.isMaximized())
        if immediate:
            self._pending_quiet_save = True
            self._flush_quiet_config_save()
        else:
            self._save_config_quietly()

    # ================================================================== #
    #  Public API (called by main app)
    # ================================================================== #

    def process_frame(
        self, frame: np.ndarray, detections: Optional[list] = None,
        *, _from_own_camera: bool = False,
        use_internal_detector: bool = False,
    ) -> None:
        """
        Called by main app every frame, or by own camera timer.

        ``detections`` format: list of (x, y, w, h, score) or
        (x, y, w, h, score, class_id) tuples.

        When sentry v2 has its own camera open, external (main app)
        calls are ignored to avoid frame conflicts.
        """
        if self._closing:
            return
        # Discard stale own-camera results that were queued before the source was
        # closed (e.g. a webcam frame processed by the detector AFTER _close_camera
        # was called for a new URL/test-video open).  Without this guard the old
        # webcam frame is painted over the "Opening URL…" label, making it look as
        # though the camera never closed.
        if _from_own_camera and not self._local_source_kind:
            return
        # Own camera takes priority — skip external pushes
        if self._has_local_source() and not _from_own_camera:
            return
        now = time.time()
        self._last_processed_frame_s = now
        h, w_frame = frame.shape[:2]
        self._last_raw_frame = frame if _from_own_camera else frame.copy()

        raw_detections = detections or []
        if use_internal_detector and not _from_own_camera:
            mode = self.config.detection_mode.detection_mode
            raw_detections = self._detector.detect(frame, mode)
        else:
            mode = self.config.detection_mode.detection_mode

        # Update frame dimensions in config
        self.config.guard.frame_width = w_frame
        self.config.guard.frame_height = h

        base_objects = self._raw_detections_to_objects(raw_detections, w_frame, h)
        engine_objects, face_matches = self._apply_face_identity_to_objects(frame, base_objects, now)
        self._last_face_matches = list(face_matches)
        self._update_face_runtime_status()
        prompted_objects: List[DetectedObject] = []
        if bool(self.config.prompted_targets_enabled):
            prompted_objects = self._prompted_matcher.detect(frame, engine_objects, now)
        det_objects = self._tracker.assign_tracks(engine_objects + prompted_objects, now)

        # Auto-lighting: sample scene brightness every N frames
        self._auto_lighting_frame_counter += 1
        interval = max(1, int(getattr(self.config.lighting, "auto_sample_interval_frames", 8)))
        if self._auto_lighting_frame_counter >= interval:
            self._auto_lighting_frame_counter = 0
            self._update_auto_lighting(frame)

        # Run engine
        self._sync_engine_pose_from_feedback()
        self.engine.update(det_objects, now)
        self._log_tracking_pipeline_diagnostics(det_objects, now)
        self._update_sound_runtime_cues()
        self._last_detected_objects = list(det_objects)

        if self._show_video_feed and not self._should_present_display_frame(now):
            self._set_preview_perf_mode("throttled")
            return

        # Copy frame so overlay drawing doesn't corrupt main app's buffer
        display = self._build_display_frame(
            frame,
            mode=mode,
            use_internal_detector=use_internal_detector,
        )
        self._last_display_frame = display

        # Update video label (only if show_video_feed is enabled)
        if self._show_video_feed:
            self._show_frame(display)
            self._mark_display_present(now, mode="full")
        else:
            # Show black frame with status text
            black_frame = np.zeros_like(display)
            hidden_text = "Video Feed Hidden"
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.7
            thickness = 1
            (tw, th), _ = cv2.getTextSize(hidden_text, font, font_scale, thickness)
            tx = max(8, (display.shape[1] - tw) // 2)
            ty = max(th + 8, (display.shape[0] + th) // 2)
            cv2.putText(black_frame, hidden_text, (tx, ty), font, font_scale, (108, 108, 108), thickness, cv2.LINE_AA)
            self._show_frame(black_frame)
            self._mark_display_present(now, mode="hidden")

    def _should_present_display_frame(self, now: float, *, busy: bool = False) -> bool:
        if self._force_next_display_refresh or self._last_display_present_s <= 0.0:
            return True
        interval = self._busy_display_frame_interval_s if busy else self._display_frame_interval_s
        return (now - self._last_display_present_s) >= interval

    def _set_preview_perf_mode(self, mode: str) -> None:
        mode_text = str(mode or "unknown").strip() or "unknown"
        if mode_text == self._preview_perf_mode:
            return
        self._preview_perf_mode = mode_text
        self._log(f"[PREVIEW] render_mode={mode_text}")

    def _mark_display_present(self, now: float, *, mode: str) -> None:
        self._last_display_present_s = now
        self._force_next_display_refresh = False
        self._set_preview_perf_mode(mode)

    @staticmethod
    def _is_probable_camera_blackout(frame: np.ndarray) -> bool:
        if frame is None or frame.size == 0:
            return False
        try:
            frame_max = int(frame.max())
            frame_mean = float(frame.mean())
        except Exception:
            return False
        return frame_max <= 12 and frame_mean <= 2.5

    @staticmethod
    def _is_probable_partial_frame(frame: np.ndarray) -> bool:
        """Detect frames where camera content occupies only a sub-rectangle.

        After a USB webcam driver glitch on Windows (MSMF/DSHOW), the camera
        can enter a degraded state where it returns a full-size frame buffer
        but only populates the upper-left portion with actual video data; the
        remainder stays zero-filled (black).  The existing blackout detector
        misses this because the frame is *not* entirely black.

        Strategy: sample the bottom-right quadrant.  If it is near-black while
        the top-left quadrant has real content, this is a partial frame.
        """
        if frame is None or frame.size == 0:
            return False
        try:
            h, w = frame.shape[:2]
            if h < 32 or w < 32:
                return False
            # Top-left 25 % of the frame
            tl = frame[: h // 4, : w // 4]
            # Bottom-right 25 % of the frame
            br = frame[h * 3 // 4 :, w * 3 // 4 :]
            tl_mean = float(tl.mean())
            br_max = int(br.max())
            br_mean = float(br.mean())
            # Content in top-left but bottom-right is dead black
            return tl_mean > 8.0 and br_max <= 6 and br_mean <= 1.5
        except Exception:
            return False

    @staticmethod
    def _crop_to_content(frame: np.ndarray) -> np.ndarray:
        """Crop a partial frame to its actual content area.

        Scans rows/columns from the edges inward to find the boundary where
        content ends and the black padding begins.  Returns the cropped frame
        or the original if no significant padding is detected.
        """
        try:
            h, w = frame.shape[:2]
            if h < 32 or w < 32:
                return frame
            gray = frame if frame.ndim == 2 else frame.max(axis=2)
            threshold = 6

            # Find last row with content (scan from bottom up)
            row_max = gray.max(axis=1)
            content_rows = int(np.where(row_max > threshold)[0][-1]) + 1 if (row_max > threshold).any() else h

            # Find last column with content (scan from right)
            col_max = gray.max(axis=0)
            content_cols = int(np.where(col_max > threshold)[0][-1]) + 1 if (col_max > threshold).any() else w

            # Only crop if padding is significant (> 15 % of each dimension)
            if content_rows < h * 0.85 and content_cols < w * 0.85:
                cropped = frame[:content_rows, :content_cols]
                if cropped.size > 0 and cropped.shape[0] >= 16 and cropped.shape[1] >= 16:
                    return cropped
        except Exception:
            pass
        return frame

    def _is_usable_camera_probe_frame(self, frame: Optional[np.ndarray]) -> bool:
        if frame is None:
            return False
        if self._is_probable_camera_blackout(frame):
            return False
        if self._is_probable_partial_frame(frame):
            return False
        return True

    def _handle_camera_frame_health(self, frame: np.ndarray) -> bool:
        if self._local_source_kind != "camera":
            self._camera_black_frame_count = 0
            self._camera_partial_frame_count = 0
            return False

        now_t = time.time()
        grace_until = float(getattr(self, "_camera_health_grace_until_s", 0.0) or 0.0)
        if now_t < grace_until:
            self._camera_black_frame_count = 0
            self._camera_partial_frame_count = 0
            return False

        # --- Full blackout check ---
        is_blackout = self._is_probable_camera_blackout(frame)
        is_partial = self._is_probable_partial_frame(frame)
        if is_blackout:
            self._camera_black_frame_count += 1
            if self._camera_black_frame_count >= self._MAX_CAMERA_BLACK_FRAMES:
                self._camera_black_frame_count = 0
                if self._attempt_camera_recovery("Camera is returning repeated black frames."):
                    return True
                self._log("Camera blackout persisted — auto-closing source")
                self._close_camera()
                return True
            return False
        else:
            self._camera_black_frame_count = 0

        # --- Partial frame check (content only in upper-left quadrant) ---
        if self._is_probable_partial_frame(frame):
            self._camera_partial_frame_count += 1
            if self._camera_partial_frame_count == 1:
                self._log(
                    "[CAMERA-HEALTH] Partial frame detected — camera content "
                    "occupies only part of the buffer (possible driver degradation)"
                )
            if self._camera_partial_frame_count >= self._MAX_CAMERA_PARTIAL_FRAMES:
                self._camera_partial_frame_count = 0
                if self._attempt_camera_recovery(
                    "Camera is returning partial frames (content only in upper-left)."
                ):
                    return True
                self._log("Camera partial-frame condition persisted — auto-closing source")
                self._close_camera()
                return True
            return False
        else:
            self._camera_partial_frame_count = 0

        return False

    def _should_show_live_preview_fallback(self, now: float) -> bool:
        if not self._show_video_feed:
            return False
        if not self._should_present_display_frame(now, busy=True):
            return False
        processed_age_s = now - float(getattr(self, "_last_processed_frame_s", 0.0) or 0.0)
        stale_threshold_s = max(0.20, self._busy_display_frame_interval_s * 2.5)
        return self._detector_worker_busy or processed_age_s >= stale_threshold_s

    def _present_live_preview_frame(self, frame: np.ndarray, now: float) -> None:
        display = self._build_display_frame(
            frame,
            mode=self.config.detection_mode.detection_mode,
            use_internal_detector=False,
            include_target_boxes=not self._busy_preview_skip_target_boxes,
            include_scope_view=not self._busy_preview_skip_scope_view,
        )
        self._last_display_frame = display
        self._show_frame(display)
        self._mark_display_present(now, mode="busy-lite")

    def _build_display_frame(
        self,
        frame: np.ndarray,
        *,
        mode: int,
        use_internal_detector: bool,
        include_target_boxes: bool = True,
        include_scope_view: bool = True,
    ) -> np.ndarray:
        display = frame.copy()
        display = self.overlay.draw(display, self.engine, include_target_boxes=include_target_boxes)
        self._draw_face_identity_overlays(display, list(getattr(self, "_last_face_matches", []) or []))
        if include_scope_view and self._scope_view_active():
            display = self.overlay.apply_scope_view(display, self.engine)
        self._draw_no_fire_mask_draft(display)
        self._draw_color_gate_status(display, mode, use_internal_detector)
        return display

    def set_enabled(self, enabled: bool) -> None:
        self._chk_enable.setChecked(enabled)

    def is_enabled(self) -> bool:
        return self._chk_enable.isChecked()

    def get_detection_mode(self) -> int:
        """Return the currently selected detection mode index."""
        return self._combo_detection_mode.currentIndex()

    def sync_accessory_states(self, led: bool, laser: bool, safety_armed: bool) -> None:
        """Legacy shim — sentry v2 manages its own state."""
        pass

    # ================================================================== #
    #  Event Handlers
    # ================================================================== #

    def _on_enable_toggled(self, checked: bool) -> None:
        if checked:
            self._apply_all_config()
            self._detector.reset()
            self._tracker.reset()
            self._prompted_matcher.reset()
            self.engine.start()
            self._log("Smart Sentry ENABLED")
        else:
            self._stop_fire_burst(send_release=True)
            self.engine.stop()
            self._prompted_matcher.reset()
            self._set_prompted_capture_active(False)
            self._log("Smart Sentry DISABLED")
        self.sentry_enabled_changed.emit(checked)

    def _on_show_video_toggled(self, checked: bool) -> None:
        """Toggle video display (detection continues running regardless)."""
        self._show_video_feed = checked
        if not checked:
            # Show black frame immediately — don't wait for the next detection cycle
            # (with YOLO that delay can be 100–500 ms, making the toggle feel broken).
            if self._last_display_frame is not None:
                black = np.zeros_like(self._last_display_frame)
                label = "Video Feed Hidden"
                font, scale, thick = cv2.FONT_HERSHEY_SIMPLEX, 0.7, 1
                (tw, th), _ = cv2.getTextSize(label, font, scale, thick)
                tx = max(8, (black.shape[1] - tw) // 2)
                ty = max(th + 8, (black.shape[0] + th) // 2)
                cv2.putText(black, label, (tx, ty), font, scale, (108, 108, 108), thick, cv2.LINE_AA)
                self._show_frame(black)
            else:
                self._video_label.clear_frame("Video Feed Hidden")
        status = "shown" if checked else "hidden"
        self._log(f"Video feed {status} (detection running)")

    def _on_engine_fire(self, burst_count: int) -> None:
        active_order = getattr(self.engine, "active_order", None)
        active_det = getattr(getattr(active_order, "target", None), "det", None)
        if active_det is not None and str(getattr(active_det, "source", "")) == "prompted":
            if not bool(self.config.prompted_allow_auto_fire):
                self._log("Auto-fire suppressed for prompted target (manual-fire-only).")
                return
        pan = self.engine.current_pan
        tilt = self.engine.current_tilt
        interval = self.config.engagement.burst_interval_ms
        self.overlay.note_fire_event(burst_count)
        self._sound_engine.note_fire(burst_count, self._current_sound_area_ratio())
        if self._host_controls_hardware():
            self.fire_requested.emit(int(burst_count))
            self._log(f"FIRE! Burst: {burst_count}")
            return
        self._start_fire_burst(pan, tilt, burst_count, interval)
        self._log(f"FIRE! Burst: {burst_count}")

    def _engine_pir_motion_active(self) -> bool:
        engine = getattr(self, "engine", None)
        if engine is None:
            return False
        return bool(getattr(engine, "_pir_cue_mode", False))

    def _describe_engine_auto_move(self, pan: float, tilt: float) -> Optional[str]:
        engine = getattr(self, "engine", None)
        if engine is None:
            return None

        sensor_id = int(getattr(engine, "_pir_cue_sensor_id", -1) or -1)
        if bool(getattr(engine, "_pir_cue_mode", False)):
            sensor_text = f" S{sensor_id + 1}" if sensor_id >= 0 else ""
            if bool(getattr(engine, "_pir_scan_mode", False)):
                manager = getattr(engine, "_pir_manager", None)
                step_index = int(getattr(manager, "_scan_index", 0) or 0) if manager is not None else 0
                total_steps = len(getattr(manager, "_scan_points", []) or []) if manager is not None else 0
                step_text = f" {max(1, step_index)}/{max(1, total_steps)}" if total_steps else ""
                return f"PIR search move{sensor_text}{step_text}"
            return f"PIR cue move{sensor_text}"

        loss_phase = str(getattr(engine, "_loss_recovery_phase", "") or "").strip()
        if loss_phase:
            return f"Recovery move {loss_phase.replace('_', ' ')}"
        return None

    def _on_engine_move(self, pan: float, tilt: float) -> None:
        if time.time() < float(getattr(self, "_manual_move_priority_until", 0.0) or 0.0):
            return
        move_note = self._describe_engine_auto_move(pan, tilt)
        move_delta = self._get_command_delta(pan, tilt)
        move_time_ms = self._get_tracking_move_time_ms(move_delta)
        if self._should_defer_auto_move(move_time_ms, move_delta):
            if move_note and move_note.lower().startswith("pir "):
                self._log(f"{move_note} pending (waiting for previous move to settle)")
            self._resync_engine_pose_after_deferred_move()
            return
        self._last_tracking_move_time_ms = int(move_time_ms)
        self._sound_engine.note_tracking_move(move_delta, self._current_sound_area_ratio())
        if self._host_controls_hardware():
            self.turret_move_requested.emit(float(pan), float(tilt))
        else:
            self._queue_move_command(pan, tilt, move_time_ms=move_time_ms)
        self._remember_commanded_position(pan, tilt, move_time_ms=move_time_ms)
        suppression_s = self._get_tracking_motion_suppression_s(move_delta)
        self._last_tracking_suppression_s = float(suppression_s)
        if suppression_s > 0.0:
            self._suppress_motion_detection(suppression_s)
        if move_note:
            self._log(f"{move_note} -> pan {float(pan):.1f} tilt {float(tilt):.1f}")

    def _on_engine_state_change(self, old: SentryV2State, new: SentryV2State) -> None:
        self._lbl_state.setText(f"State: {new.name}")
        self._log(f"State: {old.name} -> {new.name}")
        old_scope = self._scope_view_active_for_state(old)
        new_scope = self._scope_view_active_for_state(new)
        if old_scope != new_scope:
            self._last_scope_view_active = new_scope
            self._log("Scope view: ON (ENGAGING display mode)" if new_scope else "Scope view: OFF (normal video restored)")

    def _log_tracking_pipeline_diagnostics(self, detections: List[DetectedObject], now: float) -> None:
        person_visible = [det for det in detections if str(getattr(det, "class_name", "")).strip().lower() == "person"]
        diagnostics = list(getattr(self.engine, "last_filter_diagnostics", []) or [])
        person_decisions = [
            decision for decision in diagnostics
            if str(getattr(decision, "class_name", "")).strip().lower() == "person"
        ]
        person_qualified = [decision for decision in person_decisions if bool(getattr(decision, "passed", False))]
        active_order = getattr(self.engine, "active_order", None)
        active_det = getattr(getattr(active_order, "target", None), "det", None)
        engaged_person = bool(active_det is not None and str(getattr(active_det, "class_name", "")).strip().lower() == "person")

        if engaged_person:
            stage = "engaged"
        elif person_qualified:
            stage = "qualified"
        elif person_visible:
            stage = "visible_filtered"
        else:
            stage = "idle"

        lead_visible = max(person_visible, key=lambda det: float(getattr(det, "confidence", 0.0)), default=None)
        lead_decision = max(person_decisions, key=lambda decision: float(getattr(decision, "confidence", 0.0)), default=None)
        lead_track_id = int(getattr(lead_decision, "track_id", getattr(lead_visible, "track_id", -1)))
        lead_conf = float(getattr(lead_decision, "confidence", getattr(lead_visible, "confidence", 0.0)) or 0.0)
        lead_reason = str(getattr(lead_decision, "reason", "")) if lead_decision is not None else ""
        lead_detail = str(getattr(lead_decision, "detail", "")) if lead_decision is not None else ""
        lead_hits = int(getattr(lead_decision, "confirm_hits", 0) or 0) if lead_decision is not None else 0
        lead_required = int(getattr(lead_decision, "confirm_required", 1) or 1) if lead_decision is not None else 1
        engaged_track_id = int(getattr(active_det, "track_id", -1) or -1) if engaged_person else -1

        state_name = str(getattr(self.engine.state, "name", self.engine.state))
        diag_key = "|".join([
            stage,
            state_name,
            str(len(person_visible)),
            str(len(person_qualified)),
            str(1 if engaged_person else 0),
            str(lead_track_id),
            lead_reason,
            lead_detail,
            str(engaged_track_id),
        ])
        if diag_key == self._tracking_diag_last_key and (now - self._tracking_diag_last_log_s) < self._tracking_diag_min_interval_s:
            return

        self._tracking_diag_last_key = diag_key
        self._tracking_diag_last_log_s = now

        if stage == "idle":
            self._log(f"[TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state={state_name}")
            return

        message = (
            f"[TRACKDBG] person pipeline: visible={len(person_visible)} qualified={len(person_qualified)} "
            f"engaged={1 if engaged_person else 0} state={state_name}"
        )
        if lead_track_id >= 0:
            message += f" lead_track={lead_track_id} conf={lead_conf:.2f}"
        if stage == "visible_filtered" and lead_reason:
            message += f" reason={lead_reason}"
            if lead_detail:
                message += f" ({lead_detail})"
        elif stage == "qualified" and lead_decision is not None:
            message += f" reason=qualified ({lead_hits}/{max(1, lead_required)})"
        elif stage == "engaged" and engaged_track_id >= 0:
            message += f" active_track={engaged_track_id}"
        self._log(message)

    def _emit_comm_pir_event(self, sensor_id: int, timestamp: float) -> None:
        try:
            self.pir_event_received.emit(int(sensor_id), float(timestamp))
        except Exception as exc:
            if not self._closing:
                self._report_runtime_warning("PIR signal emit failed", exc)

    def _emit_comm_transport_log(self, message: str) -> None:
        text = str(message or "").strip()
        if not text:
            return
        try:
            self._log_requested.emit(text)
        except Exception as exc:
            if not self._closing:
                self._report_runtime_warning("Comm log emit failed", exc)

    def _on_comm_pir_event_received(self, sensor_id: int, timestamp: float) -> None:
        self._pir_last_event_sensor = int(sensor_id)
        self._pir_last_event_time_s = float(timestamp)
        self._pir_event_count += 1
        engine_state = self.engine.state if self.engine is not None else None
        pir_runtime_active = bool(
            self.engine is not None
            and engine_state != SentryV2State.PAUSED
            and bool(getattr(self.config.pir_guard, "pir_enabled", False))
        )
        self.engine.on_pir_sensor_fired(int(sensor_id), float(timestamp))
        if pir_runtime_active:
            self._sound_engine.note_pir_event(sensor_id)
        if hasattr(self, "_lbl_pir_status"):
            self._update_pir_status_display()
        sensor_label = f"S{int(sensor_id) + 1}"
        if not pir_runtime_active:
            if engine_state == SentryV2State.PAUSED:
                self._log(f"PIR event ignored: {sensor_label} (sentry paused)")
            elif not bool(getattr(self.config.pir_guard, "pir_enabled", False)):
                self._log(f"PIR event ignored: {sensor_label} (PIR guard disabled)")
            else:
                state_name = engine_state.name if engine_state is not None else "?"
                self._log(f"PIR event queued without hunt: {sensor_label} (engine={state_name})")
            return
        state_name = self.engine.state.name if self.engine else "?"
        self._log(f"PIR event: {sensor_label} (engine={state_name})")
        pir_note = str(getattr(self.engine, "_last_pir_note", "") or "") if self.engine is not None else ""
        if pir_note and pir_note != self._last_pir_note_seen:
            self._last_pir_note_seen = pir_note
            self._log(pir_note)

    def _set_label_content(self, label: QLabel, text: str, style: Optional[str] = None) -> None:
        if label.text() != text:
            label.setText(text)
        if style is not None and label.styleSheet() != style:
            label.setStyleSheet(style)

    def eventFilter(self, obj, event):
        if event is not None and event.type() in (QEvent.KeyPress, QEvent.KeyRelease, QEvent.ApplicationDeactivate, QEvent.WindowDeactivate):
            try:
                if self._handle_manual_keyboard_shortcut_event(obj, event):
                    return True
            except Exception:
                pass
        if event is not None and event.type() == QEvent.Wheel:
            try:
                if bool(event.modifiers() & Qt.ShiftModifier) and self._event_targets_this_widget(obj):
                    angle_delta = int(event.angleDelta().y())
                    if angle_delta != 0:
                        self._adjust_panel_zoom(1 if angle_delta > 0 else -1)
                        event.accept()
                        return True
            except Exception:
                pass
        return super().eventFilter(obj, event)

    def _event_targets_this_widget(self, obj: object) -> bool:
        widget = obj if isinstance(obj, QWidget) else None
        while widget is not None:
            if widget is self:
                return True
            widget = widget.parentWidget()
        return False

    def _manual_keyboard_shortcuts_enabled(self) -> bool:
        return bool(self.config.shortcuts.enabled) and bool(getattr(self.config.shortcuts, "manual_controls_enabled", False))

    def _manual_keyboard_focus_is_editing(self) -> bool:
        widget = QApplication.focusWidget()
        while widget is not None:
            if widget is self:
                return False
            if isinstance(widget, (QLineEdit, QTextEdit, QSpinBox, QDoubleSpinBox, QComboBox)):
                return True
            widget = widget.parentWidget()
        return False

    def _release_manual_keyboard_fire(self) -> bool:
        if not bool(getattr(self, "_manual_keyboard_fire_active", False)):
            return False
        self._manual_keyboard_fire_active = False
        self._on_manual_fire(0)
        return True

    def _handle_manual_keyboard_shortcut_event(self, obj: object, event: QEvent) -> bool:
        if event is None:
            return False
        event_type = event.type()
        if event_type in (QEvent.ApplicationDeactivate, QEvent.WindowDeactivate):
            return self._release_manual_keyboard_fire()
        if event_type not in (QEvent.KeyPress, QEvent.KeyRelease):
            return False
        if not self._event_targets_this_widget(obj):
            return False
        if not self._manual_keyboard_shortcuts_enabled():
            return False
        if self._manual_keyboard_focus_is_editing():
            return False
        if int(event.modifiers()) != int(Qt.NoModifier):
            return False
        key = int(event.key())
        if key not in (Qt.Key_W, Qt.Key_A, Qt.Key_S, Qt.Key_D, Qt.Key_Space):
            return False
        if bool(event.isAutoRepeat()):
            event.accept()
            return True
        if event_type == QEvent.KeyPress:
            if key == Qt.Key_W:
                self._manual_move(0, 1)
            elif key == Qt.Key_A:
                self._manual_move(-1, 0)
            elif key == Qt.Key_S:
                self._manual_move(0, -1)
            elif key == Qt.Key_D:
                self._manual_move(1, 0)
            elif key == Qt.Key_Space and not self._manual_keyboard_fire_active:
                self._manual_keyboard_fire_active = True
                self._on_manual_fire(1)
            event.accept()
            return True
        if key == Qt.Key_Space:
            released = self._release_manual_keyboard_fire()
            event.accept()
            return released or True
        return False

    def _adjust_panel_zoom(self, direction: int) -> None:
        theme_cfg = self._theme_config()
        current_scale = int(getattr(theme_cfg, "font_scale_pct", 100) or 100)
        next_scale = _clamp_int(current_scale + (int(direction) * 25), 50, 280)
        if next_scale == current_scale:
            return
        theme_cfg.font_scale_pct = next_scale
        self._apply_theme()
        self._save_config_quietly()
        self._log(f"Panel zoom: {next_scale}%")

    def _status_two_line_markup(
        self,
        primary_text: str,
        secondary_text: str,
        *,
        primary_color: Optional[str] = None,
        secondary_color: Optional[str] = None,
    ) -> str:
        tokens = self._theme_tokens()
        status_font = float(tokens["status_font_pt"])
        primary = primary_color or tokens["status_neutral"]
        secondary = secondary_color or tokens["status_meta"]
        return (
            f"<span style='font-size:{status_font:.2f}pt; font-weight:700; color:{primary};'>{primary_text}</span><br>"
            f"<span style='font-size:{status_font:.2f}pt; color:{secondary};'>{secondary_text}</span>"
        )

    def _status_metric_markup(self, metrics: List[Tuple[object, str]]) -> str:
        tokens = self._theme_tokens()
        status_font = float(tokens["status_font_pt"])
        parts = []
        for value, label in metrics:
            parts.append(
                f"<span style='font-size:{status_font:.2f}pt; font-weight:700; color:{tokens['text']};'>{value}</span>"
                f"<span style='font-size:{status_font:.2f}pt; color:{tokens['status_meta']};'> {label}</span>"
            )
        return "&nbsp;&nbsp;".join(parts)

    def _compact_status_style(self, level: str = "neutral", *, bold: bool = False) -> str:
        tokens = self._theme_tokens()
        color_map = {
            "neutral": tokens["status_neutral"],
            "info": tokens["status_info"],
            "ok": tokens["status_ok"],
            "warn": tokens["status_warn"],
            "error": tokens["status_error"],
            "accent": tokens["accent"],
            "meta": tokens["status_meta"],
        }
        weight = "bold" if bold else "normal"
        return f"font-weight: {weight}; color: {color_map.get(level, tokens['status_neutral'])}; font-size: {tokens['base_font_pt']:.2f}pt;"

    def _camera_status_style(self, level: str = "neutral") -> str:
        return self._compact_status_style(level)

    def _connection_status_style(self, level: str = "neutral") -> str:
        return self._compact_status_style(level, bold=True)

    def _set_camera_status(self, text: str, level: str = "neutral") -> None:
        self._camera_status_level = str(level or "neutral")
        if hasattr(self, "_lbl_cam_status") and self._lbl_cam_status is not None:
            self._set_label_content(self._lbl_cam_status, text, self._camera_status_style(self._camera_status_level))

    def _set_connection_status(self, text: str, level: str = "neutral") -> None:
        self._connection_status_level = str(level or "neutral")
        if hasattr(self, "_lbl_conn_status") and self._lbl_conn_status is not None:
            self._set_label_content(self._lbl_conn_status, text, self._connection_status_style(self._connection_status_level))

    def _sync_camera_status_style(self) -> None:
        if hasattr(self, "_lbl_cam_status") and self._lbl_cam_status is not None:
            level = str(getattr(self, "_camera_status_level", "neutral") or "neutral")
            self._lbl_cam_status.setStyleSheet(self._camera_status_style(level))

    def _sync_connection_status_style(self) -> None:
        if hasattr(self, "_lbl_conn_status") and self._lbl_conn_status is not None:
            level = str(getattr(self, "_connection_status_level", "neutral") or "neutral")
            self._lbl_conn_status.setStyleSheet(self._connection_status_style(level))

    def _sync_auto_trigger_checkbox_style(self) -> None:
        if not hasattr(self, "_chk_auto_trigger") or self._chk_auto_trigger is None:
            return
        level = "error" if self._chk_auto_trigger.isChecked() else "ok"
        style = self._compact_status_style(level, bold=True)
        base_font = self._theme_tokens()["base_font_pt"]
        self._chk_auto_trigger.setStyleSheet(f"{style} font-size: {base_font:.2f}pt;")

    def _status_text_style(self, level: str = "neutral", *, compact: bool = True, badge: bool = False) -> str:
        tokens = self._theme_tokens()
        color_map = {
            "neutral": tokens["status_neutral"],
            "info": tokens["status_info"],
            "ok": tokens["status_ok"],
            "warn": tokens["status_warn"],
            "error": tokens["status_error"],
            "accent": tokens["accent"],
        }
        text_color = color_map.get(level, tokens["status_neutral"])
        font_size = int(max(10, round(float(tokens["base_font_pt"]))))
        if badge:
            background = _rgba_hex(tokens["root_bg"], 30 if tokens["is_light"] else 48)
            border = _mix_hex(text_color, tokens["border"], 0.30)
            return (
                f"font-weight: bold; color: {text_color}; font-size: {font_size}px; "
                f"background-color: {background}; border: 1px solid {border}; border-radius: 6px; padding: 4px;"
            )
        return f"font-weight: bold; color: {text_color}; font-size: {font_size}px;"

    def _status_meta_color(self) -> str:
        return self._theme_tokens()["status_meta"]

    def _apply_status_panel_theme(self) -> None:
        if not hasattr(self, "_lbl_hw_monitor_title"):
            return
        tokens = self._theme_tokens()
        for frame in self.findChildren(QFrame, "sentryV2StatusCard"):
            accent = str(frame.property("accentColor") or tokens["accent"])
            frame.setStyleSheet(
                "QFrame#sentryV2StatusCard {"
                f"background-color: {tokens['status_card_bg']}; border: 1px solid {tokens['status_card_border']}; "
                f"border-left: 3px solid {accent}; border-radius: {tokens['status_card_radius']}px;"
                "}"
            )
        for frame in self.findChildren(QFrame, "sentryV2StatusSubframe"):
            frame.setStyleSheet(
                "QFrame#sentryV2StatusSubframe {"
                f"background-color: {tokens['status_subframe_bg']}; border: 1px solid {tokens['status_card_border']}; "
                f"border-radius: {tokens['status_card_radius']}px;"
                "}"
            )
        for label in self.findChildren(QLabel):
            role = str(label.property("themeRole") or "")
            if role == "statusCardTitle":
                label.setStyleSheet(f"color: {tokens['status_card_title']}; font-size: {tokens['base_font_pt'] + 0.4:.2f}pt; font-weight: 700; letter-spacing: 0.2px;")
            elif role == "statusCardValue":
                label.setStyleSheet(f"color: {tokens['status_card_value']}; font-size: {tokens['base_font_pt'] + 0.9:.2f}pt; font-weight: 800;")
            elif role == "statusSectionTitle":
                label.setStyleSheet(f"font-weight: 700; color: {tokens['status_section_title']}; font-size: {tokens['base_font_pt'] + 0.5:.2f}pt;")
            elif role == "statusValue":
                label.setStyleSheet(f"font-weight: 800; color: {tokens['status_card_value']}; font-size: {tokens['base_font_pt'] + 0.5:.2f}pt;")
            elif role == "statusDetail":
                label.setStyleSheet(self._status_text_style("neutral"))
            elif role == "statusBadge":
                label.setStyleSheet(self._status_text_style("neutral", badge=True))
        if hasattr(self, "_bar_pan_status"):
            self._bar_pan_status.setStyleSheet(
                "QProgressBar {"
                f"background: {tokens['status_progress_bg']}; border: 1px solid {tokens['status_card_border']}; border-radius: 5px;"
                "}"
                f"QProgressBar::chunk {{background: {tokens['status_progress_pan']}; border-radius: 4px;}}"
            )
        if hasattr(self, "_bar_tilt_status"):
            self._bar_tilt_status.setStyleSheet(
                "QProgressBar {"
                f"background: {tokens['status_progress_bg']}; border: 1px solid {tokens['status_card_border']}; border-radius: 5px;"
                "}"
                f"QProgressBar::chunk {{background: {tokens['status_progress_tilt']}; border-radius: 4px;}}"
            )

    # ------------------------------------------------------------------ #
    #  Connection handlers
    # ------------------------------------------------------------------ #

    def _on_conn_type_changed(self, index: int) -> None:
        self.config.connection.connection_type = index
        self._update_conn_panel_visibility()

    _MODE_HINTS = [
        "Single USB cable — full ASCII protocol to ESP32.",
        "Two USB cables — bus servo to Debug Board + IO to ESP32.",
        "One USB cable — Debug Board stays on USB, ESP32 IO goes over WiFi.",
        "No runtime USB — PC talks to the Waveshare bridge over WiFi, and the local bus-servo UART runs on GPIO18/GPIO19.",
        "No USB cables — Primary ESP32 handles IO, Secondary ESP32 (Yahboom board) handles servos.",
    ]

    def _wifi_credentials_for_mode(self, mode: int) -> tuple[str, str]:
        if int(mode) == SentryV2Comm.MODE_WIFI_FULL:
            return SMART_SENTRY_V3_WIFI_SSID, SMART_SENTRY_V3_WIFI_PASSWORD
        if int(mode) in {
            SentryV2Comm.MODE_WIFI_DEBUG_USB,
            SentryV2Comm.MODE_DUAL_ESP32_WIFI,
        }:
            return SMART_SENTRY_V2_WIFI_SSID, SMART_SENTRY_V2_WIFI_PASSWORD
        return SMART_SENTRY_V2_WIFI_SSID, SMART_SENTRY_V2_WIFI_PASSWORD

    def _wifi_credentials_candidates_for_mode(self, mode: int) -> list[tuple[str, str]]:
        mode_index = int(mode)
        if mode_index == SentryV2Comm.MODE_WIFI_FULL:
            # Some deployed Waveshare bridges still advertise the v2.3 SSID.
            # Accept both to avoid autojoin churn/disconnect loops.
            return [
                (SMART_SENTRY_V3_WIFI_SSID, SMART_SENTRY_V3_WIFI_PASSWORD),
                (SMART_SENTRY_V2_WIFI_SSID, SMART_SENTRY_V2_WIFI_PASSWORD),
            ]
        if mode_index in {
            SentryV2Comm.MODE_WIFI_DEBUG_USB,
            SentryV2Comm.MODE_DUAL_ESP32_WIFI,
        }:
            return [(SMART_SENTRY_V2_WIFI_SSID, SMART_SENTRY_V2_WIFI_PASSWORD)]
        return [(SMART_SENTRY_V2_WIFI_SSID, SMART_SENTRY_V2_WIFI_PASSWORD)]

    def _pin_assignment_button_text(self, mode_index: int) -> str:
        if mode_index == SentryV2Comm.MODE_WIFI_FULL:
            return "Waveshare Pin Assignments"
        if mode_index == SentryV2Comm.MODE_DUAL_ESP32_WIFI:
            return "Dual ESP32 Pin Assignments"
        if mode_index == SentryV2Comm.MODE_WIFI_DEBUG_USB:
            return "WiFi IO Pin Assignments"
        return "Pin Assignments"

    def _show_full_wifi_pinout(self) -> None:
        mode_index = self._combo_conn_type.currentIndex() if hasattr(self, "_combo_conn_type") else SentryV2Comm.MODE_ESP32_USB
        msg = QMessageBox(self)
        tokens = self._theme_tokens()
        title, text = _build_pin_assignment_dialog_content(mode_index, tokens)
        msg.setWindowTitle(title)
        msg.setIcon(QMessageBox.Information)
        msg.setTextFormat(Qt.RichText)
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Ok)
        dialog_radius = max(6, int(tokens["radius"]) - 6)
        msg.setStyleSheet(
            f"QMessageBox {{ background-color: {tokens['panel_rgba']}; color: {tokens['text']}; }}"
            f"QMessageBox QLabel {{ color: {tokens['text']}; font-size: 13px; }}"
            f"QPushButton {{ min-width: 84px; padding: 6px 12px; background-color: {tokens['button_bg']}; color: {tokens['button_text']}; border: 1px solid {tokens['button_border']}; border-radius: {dialog_radius}px; }}"
            f"QPushButton:hover {{ background-color: {tokens['button_hover']}; border-color: {tokens['accent']}; }}"
            f"QPushButton:pressed {{ background-color: {tokens['button_pressed']}; border-color: {tokens['accent_soft']}; }}"
        )
        msg.exec_()

    def _update_conn_panel_visibility(self) -> None:
        m = self._combo_conn_type.currentIndex()
        self._lbl_mode_hint.setText(self._MODE_HINTS[m])
        self._btn_wifi_pinout.setText(self._pin_assignment_button_text(m))
        # ESP32 serial panel: modes 0, 1
        self._grp_esp32_serial.setVisible(m in (0, 1))
        # Debug board serial panel: modes 1, 2
        self._grp_debug_serial.setVisible(m in (1, 2))
        # Servo panel: modes 1, 2 (bus servo)
        self._grp_servo.setVisible(m in (1, 2))
        # UDP panel: modes 2, 3
        self._grp_udp.setVisible(m in (2, 3))
        # Secondary ESP32 UDP panel: mode 4
        self._grp_servo_udp.setVisible(m == 4)

    def _scan_ports(self, target: str = "esp32") -> None:
        combo = self._combo_esp32_ports if target == "esp32" else self._combo_debug_ports
        combo.clear()
        ports = SentryV2Comm.list_serial_ports()
        for dev, desc in ports:
            combo.addItem(f"{dev}  —  {desc}", dev)

        if ports:
            combo.setCurrentIndex(0)
            self._on_port_selected(target)
        else:
            combo.addItem("(no ports found)")

        self._log(f"Scan ({target}): {len(ports)} port(s) found")

    def _list_serial_ports_normalized(self) -> list[tuple[str, str]]:
        ports: list[tuple[str, str]] = []
        try:
            for dev, desc in SentryV2Comm.list_serial_ports():
                normalized = SentryV2Comm._normalize_serial_port_name(str(dev or "").strip())
                if normalized:
                    ports.append((normalized, str(desc or "").strip()))
        except Exception:
            return []
        return ports

    def _resolve_serial_port(self, target: str, preferred_port: str = "") -> str:
        ports = self._list_serial_ports_normalized()
        if not ports:
            return SentryV2Comm._normalize_serial_port_name(preferred_port)

        available = {port.upper(): port for port, _desc in ports}
        preferred = SentryV2Comm._normalize_serial_port_name(preferred_port)
        if preferred and preferred.upper() in available:
            return available[preferred.upper()]

        non_system_ports = [
            (port, desc)
            for port, desc in ports
            if "communications port" not in str(desc or "").strip().lower()
        ]
        if len(non_system_ports) == 1:
            return non_system_ports[0][0]

        keyword_scores = {
            "debug": {
                "usb-serial": 6,
                "ch340": 6,
                "wch": 5,
                "usb serial": 5,
                "cp210": 3,
                "uart": 2,
            },
            "esp32": {
                "esp32": 8,
                "cp210": 6,
                "silicon labs": 5,
                "usb-serial": 3,
                "ch340": 3,
                "uart": 2,
            },
        }
        scored: list[tuple[int, str]] = []
        for port, desc in non_system_ports:
            text = str(desc or "").lower()
            score = 0
            for token, weight in keyword_scores.get(target, {}).items():
                if token in text:
                    score += int(weight)
            scored.append((score, port))

        if scored:
            scored.sort(key=lambda item: (item[0], item[1]), reverse=True)
            best_score, best_port = scored[0]
            if best_score > 0:
                return best_port

        return non_system_ports[0][0] if len(non_system_ports) == 1 else ""

    def _on_port_selected(self, target: str = "esp32") -> None:
        if target == "esp32":
            idx = self._combo_esp32_ports.currentIndex()
            dev = self._combo_esp32_ports.itemData(idx)
            if dev:
                self._edit_esp32_port.setText(dev)
            else:
                # Fallback: show text if there is no data payload
                self._edit_esp32_port.setText(self._combo_esp32_ports.currentText())
        else:
            idx = self._combo_debug_ports.currentIndex()
            dev = self._combo_debug_ports.itemData(idx)
            if dev:
                self._edit_debug_port.setText(dev)
            else:
                self._edit_debug_port.setText(self._combo_debug_ports.currentText())

    def _on_invert_changed(self) -> None:
        self.config.connection.invert_pan = self._chk_invert_pan.isChecked()
        self.config.connection.invert_tilt = self._chk_invert_tilt.isChecked()
        self._comm.invert_pan = self.config.connection.invert_pan
        self._comm.invert_tilt = self.config.connection.invert_tilt

    def _toggle_connection(self) -> None:
        if self._host_controls_hardware():
            self._set_connection_status("Host-managed by main app", "ok")
            self._log("Connection handled by main app while embedded")
            return
        if self._connection_busy:
            self._log("Connection operation already in progress")
            return
        if self._comm.is_connected():
            self._start_connection_operation("disconnect")
            return

        # Read settings from UI into config
        m = self._combo_conn_type.currentIndex()
        cc = self.config.connection
        cc.connection_type = m

        # Prefer the user's typed value. Dropdown values are only a convenience
        # after a scan and must not silently override a manually entered COM port.
        typed_esp32 = self._edit_esp32_port.text().strip()
        esp32_data = self._combo_esp32_ports.itemData(self._combo_esp32_ports.currentIndex())
        if typed_esp32:
            cc.esp32_port = typed_esp32
        elif esp32_data:
            cc.esp32_port = str(esp32_data).strip()
        else:
            cc.esp32_port = ""

        cc.esp32_baud = self._spin_esp32_baud.value()

        typed_debug = self._edit_debug_port.text().strip()
        debug_data = self._combo_debug_ports.itemData(self._combo_debug_ports.currentIndex())
        if typed_debug:
            cc.debug_port = typed_debug
        elif debug_data:
            cc.debug_port = str(debug_data).strip()
        else:
            cc.debug_port = ""

        if m in (0, 1):
            resolved_esp32 = self._resolve_serial_port("esp32", cc.esp32_port)
            if resolved_esp32 and resolved_esp32 != cc.esp32_port:
                self._log(f"Auto-selected ESP32 COM port: {resolved_esp32}")
                self._edit_esp32_port.setText(resolved_esp32)
            if resolved_esp32:
                cc.esp32_port = resolved_esp32

        if m in (1, 2):
            resolved_debug = self._resolve_serial_port("debug", cc.debug_port)
            if resolved_debug and resolved_debug != cc.debug_port:
                self._log(f"Auto-selected Debug Board COM port: {resolved_debug}")
                self._edit_debug_port.setText(resolved_debug)
            if resolved_debug:
                cc.debug_port = resolved_debug

        cc.debug_baud = self._spin_debug_baud.value()
        cc.udp_host = self._edit_udp_host.text().strip()
        cc.udp_port = self._spin_udp_port.value()
        cc.wifi_interface = str(self._combo_wifi_adapter.currentData() or "").strip()
        cc.servo_udp_host = self._edit_servo_udp_host.text().strip()
        cc.servo_udp_port = self._spin_servo_udp_port.value()
        cc.pan_servo_id = self._spin_pan_id.value()
        cc.tilt_servo_id = self._spin_tilt_id.value()
        cc.bus_servo_time_ms = self._spin_servo_time.value()

        # Push servo config to comm
        self._comm.pan_servo_id = cc.pan_servo_id
        self._comm.tilt_servo_id = cc.tilt_servo_id
        self._comm.bus_servo_time_ms = cc.bus_servo_time_ms
        self._comm.trigger_mode_bb = (self._combo_trigger_mode.currentIndex() == 1)

        self._start_connection_operation(
            "connect",
            mode=m,
            esp32_port=cc.esp32_port,
            esp32_baud=cc.esp32_baud,
            debug_port=cc.debug_port,
            debug_baud=cc.debug_baud,
            udp_host=cc.udp_host,
            udp_port=cc.udp_port,
            initial_pan=float(self.engine.current_pan),
            initial_tilt=float(self.engine.current_tilt),
            initial_move_time_ms=int(self._get_manual_move_time_ms()),
            pir_enabled=bool(self.config.pir_guard.pir_enabled),
            motion_enabled=bool(self._pan_tilt_motion_enabled),
        )

    def _start_connection_operation(self, operation: str, **kwargs) -> None:
        if self._closing:
            return
        self._connection_busy = True
        is_connect = operation == "connect"
        self._btn_connect.setEnabled(False)
        self._btn_connect.setText("Connecting..." if is_connect else "Disconnecting...")
        self._set_connection_status("Connecting..." if is_connect else "Disconnecting...", "warn")
        self._log("Connecting..." if is_connect else "Disconnecting...")

        def _worker() -> None:
            ok = False
            info = "Disconnected"
            err = ""
            details = {}
            try:
                if operation == "connect":
                    ok = self._comm.connect(
                        int(kwargs.get("mode", 0)),
                        esp32_port=str(kwargs.get("esp32_port", "")),
                        esp32_baud=int(kwargs.get("esp32_baud", 115200)),
                        debug_port=str(kwargs.get("debug_port", "")),
                        debug_baud=int(kwargs.get("debug_baud", 115200)),
                        udp_host=str(kwargs.get("udp_host", "192.168.4.1")),
                        udp_port=int(kwargs.get("udp_port", 9000)),
                    )
                    if ok:
                        if bool(kwargs.get("motion_enabled", True)):
                            initial_move_ok = self._comm.send_movement(
                                float(kwargs.get("initial_pan", 90.0)),
                                float(kwargs.get("initial_tilt", 50.0)),
                                move_time_ms=int(kwargs.get("initial_move_time_ms", 20)),
                            )
                            if not initial_move_ok:
                                self.command_result_ready.emit(
                                    "move",
                                    False,
                                    getattr(self._comm, "_last_error", "") or "initial movement send failed after connect",
                                )
                        pir_enabled = bool(kwargs.get("pir_enabled", False))
                        pir_ok = self._comm.send_pir_enabled(pir_enabled)
                        if pir_enabled and not pir_ok:
                            self.command_result_ready.emit(
                                "send_pir_enabled",
                                False,
                                getattr(self._comm, "_last_error", "") or "PIR enable command failed",
                            )
                    info = self._comm.connection_info()
                else:
                    self._comm.disconnect()
                    ok = not self._comm.is_connected()
                    info = "Disconnected"
                err = str(getattr(self._comm, "_last_error", "") or "")
                details = dict(getattr(self._comm, "_connect_details", {}) or {})
            except Exception as exc:
                err = str(exc)
            self.connection_operation_finished.emit(operation, bool(ok), err, details, info)

        threading.Thread(target=_worker, name=f"sentry-v2-{operation}", daemon=True).start()

    def _format_connection_details(self, details: object, fallback: str) -> str:
        detail_lines = []
        if isinstance(details, dict):
            for name, pair in details.items():
                try:
                    link_ok, val = pair
                except Exception:
                    continue
                mark = "\u2705" if link_ok else "\u274C"
                detail_lines.append(f"{mark} {name}: {val}")
        return "\n".join(detail_lines) if detail_lines else fallback

    def _on_connection_operation_finished(
        self,
        operation: str,
        ok: bool,
        err: str,
        details: object,
        info: str,
    ) -> None:
        self._connection_busy = False
        if self._closing:
            return
        self._btn_connect.setEnabled(True)

        if operation == "disconnect":
            self._btn_connect.setText("Connect")
            self._set_connection_status("Disconnected", "error")
            self._log("Disconnected")
            self._startup_autoconnect_active = False
            self._startup_autoconnect_retry = 0
            return

        if ok:
            self._btn_connect.setText("Disconnect")
            conn_text = self._format_connection_details(details, info)
            mode2_degraded_io = (
                int(self.config.connection.connection_type) == 2
                and (
                    getattr(self._comm, "_sock", None) is None
                    or getattr(self._comm, "_udp_target", None) is None
                )
            )
            self._set_connection_status(conn_text, "warn" if mode2_degraded_io else "ok")
            self._log(f"Connected: {info}")
            fire_mode = "Projectile (ESP32 GPIO13 Servo)" if self._comm.trigger_mode_bb else "Water (MOSFET)"
            safety_state = "ARMED" if self._safety_armed else "LOCKED"
            auto_trigger_state = "ON" if bool(self.config.engagement.auto_trigger_enabled) else "OFF"
            self._log(f"Fire config: mode={fire_mode} | safety={safety_state} | auto-trigger={auto_trigger_state}")
            if mode2_degraded_io:
                self._log(
                    "Connection warning: Debug Board pan/tilt movement is available, but ESP32 WiFi IO is unavailable. GPIO13 trigger-servo and PIR enable commands will not work until the WiFi link reconnects"
                )
            else:
                self._queue_runtime_trigger_config_if_connected()
            self._startup_autoconnect_active = False
            self._startup_autoconnect_retry = 0
            self._schedule_auto_yolo_load(300)
            self._schedule_startup_rest_move()
        else:
            self._btn_connect.setText("Connect")
            failure_text = self._format_connection_details(details, f"FAILED: {err or 'unknown error'}")
            self._set_connection_status(failure_text, "error")
            self._log(f"Connection failed: {err or 'unknown error'}")

            # Startup-only retry for transient Windows COM enumeration race.
            # Applies only to mode 2 and only when the error indicates COM port
            # file not found (e.g. \\.\COM28 not ready yet).
            err_text = str(err or "")
            mode = int(self.config.connection.connection_type)
            if (
                self._startup_autoconnect_active
                and mode == 2
                and self._startup_autoconnect_retry < 4
                and ("could not open port" in err_text.lower())
                and ("filenotfounderror" in err_text.lower() or "cannot find the file" in err_text.lower())
            ):
                next_retry = self._startup_autoconnect_retry + 1
                delay_ms = 1200 * next_retry
                self._startup_autoconnect_retry = next_retry
                self._log(
                    f"Auto-connect retry scheduled ({next_retry}/4) after transient COM open failure"
                )
                QTimer.singleShot(delay_ms, lambda r=next_retry: self._auto_connect_on_startup(r))
            else:
                self._startup_autoconnect_active = False

    # ------------------------------------------------------------------ #
    #  Camera management
    # ------------------------------------------------------------------ #

    def _toggle_camera(self) -> None:
        if self._has_local_source():
            self._close_camera()
            return
        src_text = self._edit_cam_source.text().strip()
        if not src_text:
            src_text = "0"
            self._edit_cam_source.setText(src_text)
            self._set_camera_status("Camera source blank. Defaulting to standalone camera index 0.", "neutral")
            self._log("Camera source blank; defaulting to standalone camera index 0")
        # Save to config
        selected_width, selected_height = self._selected_camera_dimensions()
        self._remember_camera_source(src_text, selected_width, selected_height)
        self.config.connection.camera_source = src_text
        self.config.connection.camera_width = selected_width
        self.config.connection.camera_height = selected_height
        # Parse source: integer index or string path/URL
        try:
            src = int(src_text)
        except ValueError:
            src = src_text

        # Conflict check: prevent opening the same camera index as the main app.
        # When the main app is on Auto, index 0 is the most common device on single-camera setups.
        if isinstance(src, int) and self._host_controls_hardware():
            main_win = self._get_main_window()
            if main_win is not None:
                main_cap = getattr(main_win, "cap", None)
                main_combo = getattr(main_win, "camera_index_combo", None)
                main_text = ""
                try:
                    if main_combo is not None:
                        main_text = (main_combo.currentText() or "").strip().lower()
                except Exception:
                    main_text = ""
                same_source = main_text == str(src)
                auto_zero_conflict = main_text in ("", "auto") and src == 0
                if main_cap is not None and main_cap.isOpened() and (same_source or auto_zero_conflict):
                    self._set_camera_status(
                        f"Camera index {src} is already reserved by the main app. Use another index or URL.",
                        "error",
                    )
                    self._log(f"Camera open blocked: index {src} is in use by main app")
                    return

        try:
            self._open_video_capture_source(src, src_text, "camera", request_frame_size=True)
        except Exception as e:
            self._set_camera_status(f"Error: {e}", "error")
            self._log(f"Camera error: {e}")

    def _browse_test_media(self) -> None:
        start_dir = Path.cwd()
        current_source = str(self._local_source_label or "").strip()
        if current_source:
            try:
                candidate = Path(current_source).expanduser()
                if candidate.exists():
                    start_dir = candidate.parent if candidate.is_file() else candidate
            except Exception:
                pass
        selected_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Test Video or Image",
            str(start_dir),
            "Media Files (*.mp4 *.avi *.mov *.mkv *.wmv *.webm *.jpg *.jpeg *.png *.bmp *.tif *.tiff);;Video Files (*.mp4 *.avi *.mov *.mkv *.wmv *.webm);;Image Files (*.jpg *.jpeg *.png *.bmp *.tif *.tiff);;All Files (*.*)",
        )
        if not selected_path:
            return
        self._open_test_media(selected_path)

    def _open_video_url(self) -> None:
        video_url = str(getattr(self, "_edit_video_url", None).text() if hasattr(self, "_edit_video_url") else "").strip()
        if not video_url:
            self._set_camera_status("Video URL is blank", "error")
            return
        # Close any existing source.  This also sets _url_stream_stop so any
        # in-flight worker for a previous URL will see it and exit.
        self._close_camera(log_close=False)
        self._video_label.set_placeholder_enabled(False)
        self._video_label.clear_frame("Opening URL\u2026")
        self._set_camera_status("Resolving URL\u2026", "neutral")
        self._log(f"Resolving video URL: {video_url}")
        # Bump generation so any leftover threads from a previous URL ignore their frames
        self._url_stream_gen += 1
        self._url_stream_stop.clear()
        gen = self._url_stream_gen
        threading.Thread(
            target=self._url_stream_worker,
            args=(video_url, gen),
            daemon=True,
            name="url-stream-worker",
        ).start()

    def _resolve_video_stream_source(self, video_url: str) -> tuple[str, str]:
        lowered = video_url.strip().lower()
        is_web_video = lowered.startswith("http://") or lowered.startswith("https://")
        is_youtube = "youtube.com/" in lowered or "youtu.be/" in lowered
        if not is_web_video:
            return video_url, video_url
        if not is_youtube:
            return video_url, video_url

        try:
            import yt_dlp
        except Exception as exc:
            raise RuntimeError("yt-dlp is required for YouTube URLs") from exc

        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "skip_download": True,
            "noplaylist": True,
            "format": "best[ext=mp4]/best",
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
        if not isinstance(info, dict):
            raise RuntimeError("Unable to resolve video URL")

        if "entries" in info and info["entries"]:
            first_entry = next((entry for entry in info["entries"] if entry), None)
            if isinstance(first_entry, dict):
                info = first_entry

        stream_url = str(info.get("url") or "").strip()
        if not stream_url:
            requested_formats = info.get("requested_formats") or []
            if requested_formats and isinstance(requested_formats, list):
                stream_url = str(requested_formats[0].get("url") or "").strip()
        if not stream_url:
            raise RuntimeError("No playable stream URL found")

        title = str(info.get("title") or video_url).strip()
        return stream_url, title

    def _open_test_media(self, selected_path: str) -> None:
        media_path = Path(selected_path).expanduser()
        if not media_path.exists():
            self._set_camera_status(f"Test media not found: {selected_path}", "error")
            self._log(f"Test media open failed: {selected_path}")
            return

        image_suffixes = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}
        try:
            if media_path.suffix.lower() in image_suffixes:
                self._open_image_source(media_path)
            else:
                self._open_video_capture_source(str(media_path), str(media_path), "test_video", request_frame_size=False)
        except Exception as exc:
            self._set_camera_status(f"Test media error: {exc}", "error")
            self._log(f"Test media error: {exc}")

    def _play_test_media(self) -> None:
        if self._local_source_kind != "test_video":
            return
        if not self._test_media_paused:
            return
        self._test_media_paused = False
        self._update_test_media_controls()
        self._log("Test video resumed")
        self._grab_frame()

    def _pause_test_media(self) -> None:
        if self._local_source_kind != "test_video":
            return
        if self._test_media_paused:
            return
        self._test_media_paused = True
        self._update_test_media_controls()
        self._log("Test video paused")

    def _apply_camera_resolution(self) -> None:
        width, height = self._selected_camera_dimensions()
        source_text = self._edit_cam_source.text().strip() or "0"
        self.config.connection.camera_source = source_text
        self.config.connection.camera_width = int(width)
        self.config.connection.camera_height = int(height)
        self.config.guard.frame_width = int(width)
        self.config.guard.frame_height = int(height)
        self._remember_camera_source(source_text, width, height)
        self._push_config()
        self._save_config()

        if self._local_source_kind == "camera" and self._has_local_source():
            self._set_camera_status(f"Reopening camera at {width} x {height}...", "warn")
            self._close_camera(log_close=False)
            QTimer.singleShot(0, self._toggle_camera)
            self._log(f"Applying camera resolution by reopening local source: {width} x {height}")
            return

        self._set_camera_status(
            f"Resolution saved: {width} x {height}. Use Restart App if the main/shared feed still shows the old size.",
            "warn",
        )
        self._log(f"Camera resolution saved: {width} x {height}")

    def _restart_application(self) -> None:
        self._save_config()
        self._close_camera(log_close=False)
        repo_root = self._repo_root_path()
        args = list(sys.argv) if list(sys.argv) else [str((repo_root / "run.py").resolve())]

        process = QProcess(self)
        env = QProcessEnvironment.systemEnvironment()
        env.insert("SMART_SENTRY_V3_RELAUNCH_DELAY_MS", "1200")
        env.insert("SMART_SENTRY_V3_RELAUNCH_FROM_PID", str(os.getpid()))
        process.setProcessEnvironment(env)
        process.setWorkingDirectory(str(repo_root))
        started = process.startDetached(sys.executable, args)
        if isinstance(started, tuple):
            started = bool(started[0])
        if not started:
            self._set_camera_status("Restart failed: unable to relaunch the app", "error")
            self._log("Restart failed: detached relaunch did not start")
            return

        self._log("Restarting application to apply saved settings")
        app = QApplication.instance()
        if app is not None:
            QTimer.singleShot(0, app.quit)

    def _on_source_zoom_changed(self) -> None:
        cc = self.config.connection
        cc.webcam_zoom_pct = int(self._slider_webcam_zoom.value())
        cc.test_source_zoom_pct = int(self._slider_test_zoom.value())
        self._lbl_webcam_zoom.setText(f"{cc.webcam_zoom_pct}%")
        self._lbl_test_zoom.setText(f"{cc.test_source_zoom_pct}%")

    def _active_source_zoom_pct(self) -> int:
        if self._local_source_kind == "camera":
            return int(getattr(self.config.connection, "webcam_zoom_pct", 100))
        if self._local_source_kind in {"test_video", "test_image", "url_stream"}:
            return int(getattr(self.config.connection, "test_source_zoom_pct", 100))
        return 100

    def _apply_source_zoom(self, frame: np.ndarray) -> np.ndarray:
        zoom_pct = self._active_source_zoom_pct()
        return self._apply_zoom_pct_to_frame(frame, zoom_pct)

    @staticmethod
    def _apply_zoom_pct_to_frame(frame: np.ndarray, zoom_pct: int) -> np.ndarray:
        if frame is None:
            return frame
        h, w = frame.shape[:2]
        if h <= 1 or w <= 1:
            return frame
        zoom_scale = max(0.25, min(2.0, float(zoom_pct) / 100.0))
        if abs(zoom_scale - 1.0) < 0.001:
            return frame

        if zoom_scale > 1.0:
            crop_w = max(2, min(w, int(round(w / zoom_scale))))
            crop_h = max(2, min(h, int(round(h / zoom_scale))))
            x1 = max(0, (w - crop_w) // 2)
            y1 = max(0, (h - crop_h) // 2)
            cropped = frame[y1:y1 + crop_h, x1:x1 + crop_w]
            return cv2.resize(cropped, (w, h), interpolation=cv2.INTER_LINEAR)

        scaled_w = max(2, int(round(w * zoom_scale)))
        scaled_h = max(2, int(round(h * zoom_scale)))
        shrunk = cv2.resize(frame, (scaled_w, scaled_h), interpolation=cv2.INTER_AREA)
        pad_left = max(0, (w - scaled_w) // 2)
        pad_right = max(0, w - scaled_w - pad_left)
        pad_top = max(0, (h - scaled_h) // 2)
        pad_bottom = max(0, h - scaled_h - pad_top)
        return cv2.copyMakeBorder(
            shrunk,
            pad_top,
            pad_bottom,
            pad_left,
            pad_right,
            cv2.BORDER_CONSTANT,
            value=(0, 0, 0),
        )

    def _step_test_media_frame(self) -> None:
        if self._local_source_kind != "test_video":
            return
        self._test_media_paused = True
        frame = self._read_next_test_video_frame(force_step=True)
        if frame is None:
            return
        self._queue_local_frame(frame)
        self._update_test_media_controls()

    def _restart_test_media(self) -> None:
        if self._local_source_kind == "test_image" and self._test_media_image_frame is not None:
            self._queue_local_frame(self._test_media_image_frame.copy())
            self._log("Test image reloaded")
            return
        if self._local_source_kind != "test_video" or self._cap is None:
            return
        self._cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        frame = self._read_next_test_video_frame(force_step=True)
        if frame is not None:
            self._queue_local_frame(frame)
        self._log("Test video restarted")

    def _return_to_camera(self) -> None:
        """Close the current test source and reopen the last known webcam."""
        src = getattr(self, "_last_camera_source_text", "").strip()
        if not src:
            self._log("Return to camera: no previous camera source saved")
            return
        self._close_camera(log_close=False)
        self._log(f"Returning to camera: {src}")
        try:
            cam_src: int | str = int(src)
        except ValueError:
            cam_src = src
        try:
            self._open_video_capture_source(cam_src, src, "camera", request_frame_size=True)
        except Exception as exc:
            self._set_camera_status(f"Return to camera failed: {exc}", "error")
            self._log(f"Return to camera failed: {exc}")

    def _on_test_media_loop_toggled(self, checked: bool) -> None:
        self._test_media_loop_enabled = bool(checked)

    def _update_test_media_controls(self) -> None:
        if not hasattr(self, "_btn_test_media_pause"):
            return
        is_test_video = self._local_source_kind == "test_video"
        is_test_image = self._local_source_kind == "test_image"
        self._btn_test_media_play.setEnabled(is_test_video and self._test_media_paused)
        self._btn_test_media_pause.setEnabled(is_test_video and not self._test_media_paused)
        self._btn_test_media_step.setEnabled(is_test_video)
        self._btn_test_media_restart.setEnabled(is_test_video or is_test_image)
        self._chk_test_media_loop.setEnabled(is_test_video)
        # "Back to Camera" is only useful when a test source is active and we
        # know which camera to return to.
        if hasattr(self, "_btn_return_to_camera"):
            can_return = (
                self._local_source_kind in {"test_video", "test_image", "url_stream"}
                and bool(getattr(self, "_last_camera_source_text", "").strip())
            )
            self._btn_return_to_camera.setEnabled(can_return)

    def _queue_local_frame(self, frame: np.ndarray) -> None:
        if self._local_source_kind in {"test_video", "test_image"}:
            self._test_media_last_frame = frame.copy()
        effective_frame = self._apply_source_zoom(frame)
        now = time.time()
        if self._should_show_live_preview_fallback(now):
            self._present_live_preview_frame(effective_frame, now)
        with self._detector_frame_lock:
            self._detector_pending_frame = effective_frame

    def _read_next_test_video_frame(self, *, force_step: bool = False) -> Optional[np.ndarray]:
        if self._cap is None or not self._cap.isOpened():
            return None
        if self._test_media_paused and not force_step and self._test_media_last_frame is not None:
            return self._test_media_last_frame.copy()

        ret, frame = self._cap.read()
        if (not ret or frame is None) and self._test_media_loop_enabled:
            self._cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = self._cap.read()
        if not ret or frame is None:
            self._test_media_paused = True
            self._update_test_media_controls()
            self._set_camera_status("Test video paused at end of file", "warn")
            return None
        return frame

    def _open_image_source(self, media_path: Path) -> None:
        frame = cv2.imread(str(media_path))
        if frame is None:
            raise RuntimeError(f"Failed to decode image: {media_path}")

        self._close_camera(log_close=False)
        self._test_media_image_frame = frame
        self._test_media_last_frame = frame.copy()
        self._test_media_paused = False
        self._local_source_kind = "test_image"
        self._local_source_label = str(media_path)
        self._grab_fail_count = 0
        self._sync_source_dimensions(frame.shape[1], frame.shape[0])
        self._btn_cam.setText("Close Source")
        self._set_camera_status(f"Test image: {media_path.name}  ({frame.shape[1]}x{frame.shape[0]})", "ok")
        self._cam_timer.start(250)
        self._update_test_media_controls()
        self._log(f"Test image loaded: {media_path.name} ({frame.shape[1]}x{frame.shape[0]})")
        self._schedule_auto_yolo_load(150)

    def _open_video_capture_source(
        self,
        src: int | str,
        source_text: str,
        source_kind: str,
        *,
        request_frame_size: bool,
    ) -> None:
        if isinstance(src, int) and source_kind == "camera" and self._camera_open_in_progress:
            self._log(f"[CAM-DEBUG] Ignoring duplicate camera open request for {src} while another open is in progress")
            return

        self._close_camera(log_close=False)
        self._video_label.set_placeholder_enabled(False)
        self._video_label.clear_frame("Opening camera...")
        requested_w = int(self.config.connection.camera_width)
        requested_h = int(self.config.connection.camera_height)

        if isinstance(src, int):
            # Open integer-index cameras in a background thread so DSHOW/MSMF
            # driver init doesn't freeze the Qt event loop.
            self._camera_open_in_progress = True
            self._set_camera_status("Opening camera…", "neutral")
            self._log(f"[CAM-DEBUG] Starting background open for index {src} ({requested_w}x{requested_h})")

            def _open_bg(
                _src=src, _src_text=source_text, _sk=source_kind,
                _rw=requested_w, _rh=requested_h, _rfs=request_frame_size,
            ) -> None:
                selected_backend = None
                backends = (
                    (cv2.CAP_MSMF, "MSMF"),
                    (None, "DEFAULT"),
                    (cv2.CAP_DSHOW, "DSHOW"),
                ) if os.name == "nt" else ((None, "DEFAULT"),)
                for backend, bname in backends:
                    try:
                        c = cv2.VideoCapture(_src) if backend is None else cv2.VideoCapture(_src, backend)
                        time.sleep(0.5)  # let driver settle
                        if not c.isOpened():
                            c.release()
                            continue
                        # Verify at least one readable frame — MSMF can report
                        # isOpened=True but then immediately fail on grabFrame
                        ok, _frame = c.read()
                        usable_frame = self._detach_capture_frame(_frame) if ok else None
                        # Reject frames that are valid buffers but still
                        # degraded during startup. Give the camera a few extra
                        # reads before declaring this backend unusable.
                        if usable_frame is not None and not self._is_usable_camera_probe_frame(usable_frame):
                            got_real = False
                            for _warmup in range(8):
                                time.sleep(0.15)
                                ok2, _fr2 = c.read()
                                uf2 = self._detach_capture_frame(_fr2) if ok2 else None
                                if self._is_usable_camera_probe_frame(uf2):
                                    usable_frame = uf2
                                    got_real = True
                                    break
                            if not got_real:
                                usable_frame = None  # treat as unusable
                        if usable_frame is not None:
                            selected_backend = (_src, backend, bname)
                            c.release()
                            break
                        c.release()
                    except Exception as _e:
                        pass
                # Emit thread-safe signal back to main thread
                if selected_backend is not None:
                    self._cam_bg_opened.emit(selected_backend, _src_text, _sk, _rw, _rh, _rfs)
                else:
                    self._cam_bg_failed.emit(_src_text)

            threading.Thread(target=_open_bg, daemon=True, name="cam-open-bg").start()
        else:
            # URLs / file paths — open directly (rarely slow on startup)
            cap = cv2.VideoCapture(src)
            if not cap.isOpened():
                cap.release()
                raise RuntimeError(f"Failed to open: {source_text}")
            self._finish_camera_open(cap, source_text, source_kind, requested_w, requested_h, request_frame_size)

    @staticmethod
    def _tune_capture_for_low_latency(cap: "cv2.VideoCapture") -> None:
        try:
            cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        except Exception:
            pass

    @staticmethod
    def _detach_capture_frame(frame: Optional[np.ndarray]) -> Optional[np.ndarray]:
        if not isinstance(frame, np.ndarray) or frame.size == 0 or frame.ndim < 2:
            return None
        try:
            return np.ascontiguousarray(frame).copy()
        except Exception:
            return None

    def _on_camera_probe_ready(
        self,
        probe_result: object,
        source_text: str,
        source_kind: str,
        requested_w: int,
        requested_h: int,
        request_frame_size: bool,
    ) -> None:
        if self._closing:
            self._camera_open_in_progress = False
            return
        try:
            src, backend, backend_name = probe_result
        except Exception:
            self._camera_open_in_progress = False
            self._on_camera_open_failed(source_text)
            return

        self._log(f"[CAM-DEBUG] Reopening camera on UI thread with backend {backend_name}")
        try:
            cap = cv2.VideoCapture(src) if backend is None else cv2.VideoCapture(src, backend)
        except Exception as exc:
            self._camera_open_in_progress = False
            self._log(f"Camera open failed on UI thread ({backend_name}): {exc}")
            self._on_camera_open_failed(source_text)
            return
        if cap is None or not cap.isOpened():
            if cap is not None:
                try:
                    cap.release()
                except Exception:
                    pass
            self._camera_open_in_progress = False
            self._log(f"Camera open failed on UI thread with backend {backend_name}: {source_text}")
            self._on_camera_open_failed(source_text)
            return
        self._finish_camera_open(cap, source_text, source_kind, requested_w, requested_h, request_frame_size)

    def _finish_camera_open(
        self,
        cap: "cv2.VideoCapture",
        source_text: str,
        source_kind: str,
        requested_w: int,
        requested_h: int,
        request_frame_size: bool,
    ) -> None:
        """Called on the Qt main thread after the camera has been opened."""
        if self._closing:
            try:
                cap.release()
            except Exception:
                pass
            return
        self._tune_capture_for_low_latency(cap)
        if request_frame_size:
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, requested_w)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, requested_h)

        actual_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        actual_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # Discard a few warm-up frames — some USB webcams (especially on
        # Windows DSHOW) deliver black frames right after open while the
        # sensor initialises.  Reading them here keeps the grab timer from
        # immediately counting blackout frames.
        if source_kind == "camera":
            for _warmup in range(5):
                try:
                    _ok, _wf = cap.read()
                except Exception:
                    break
        self._cap = cap
        self._local_source_kind = source_kind
        self._local_source_label = source_text
        self._test_media_image_frame = None
        self._test_media_last_frame = None
        self._test_media_paused = False
        self._grab_fail_count = 0
        self._camera_open_in_progress = False
        # Only reset recovery attempts when NOT in a recovery cycle —
        # otherwise the counter never advances and recovery loops forever.
        if not self._camera_recovery_in_progress:
            self._camera_recovery_attempts = 0
        self._camera_recovery_in_progress = False
        self._camera_health_grace_until_s = time.time() + float(self._CAMERA_HEALTH_GRACE_AFTER_OPEN_S)
        self._cam_timer.start(50)
        self._btn_cam.setText("Close Source")

        if source_kind == "camera":
            self._remember_camera_source(source_text, self.config.connection.camera_width, self.config.connection.camera_height)

        if actual_w > 0 and actual_h > 0:
            self._sync_source_dimensions(actual_w, actual_h)

        status_resolution = f"{actual_w}x{actual_h}"
        if source_kind == "camera" and request_frame_size and (actual_w != requested_w or actual_h != requested_h):
            status_resolution = f"requested {requested_w}x{requested_h}, got {actual_w}x{actual_h}"
        if source_kind == "test_video":
            status_prefix, status_name = "Test video", Path(source_text).name
        else:
            status_prefix, status_name = "Open", source_text
        self._set_camera_status(f"{status_prefix}: {status_name}  ({status_resolution})", "ok")
        if source_kind == "test_video":
            self._log(f"Test video opened: {source_text} ({actual_w}x{actual_h})")
        else:
            if request_frame_size and (actual_w != requested_w or actual_h != requested_h):
                self._log(f"Camera opened: {source_text} requested {requested_w}x{requested_h}, actual {actual_w}x{actual_h}")
            else:
                self._log(f"Camera opened: {source_text} ({actual_w}x{actual_h})")
        self._update_test_media_controls()
        self._schedule_auto_yolo_load(300)

    def _url_stream_worker(self, url: str, gen: int) -> None:
        """Single background thread that owns the ENTIRE lifecycle of a URL stream cap.

        Resolve URL  →  open cap (CAP_FFMPEG, no COM/MSMF)  →  test-read  →
        signal main thread  →  continuous read loop  →  release cap.

        The cap is NEVER handed to any other thread.  This eliminates the
        Windows DSHOW/MSMF COM single-threaded-apartment affinity problem.
        """
        cap = None
        try:
            # ── Step 1: resolve URL (yt-dlp for YouTube, passthrough otherwise) ──
            print(f"[URL-WORKER] Step 1: resolving URL: {url[:80]}", flush=True)
            self._cam_url_status.emit("Resolving URL (yt-dlp)\u2026")
            try:
                stream_source, display_label = self._resolve_video_stream_source(url)
            except Exception as exc:
                print(f"[URL-WORKER] Resolve failed: {exc}", flush=True)
                self._cam_url_error.emit(str(exc))
                return

            print(f"[URL-WORKER] Resolved to: {stream_source[:80]}, label={display_label[:50]}", flush=True)

            if self._url_stream_gen != gen or self._url_stream_stop.is_set():
                print("[URL-WORKER] Superseded after resolve — exiting", flush=True)
                return

            # ── Step 2: open the cap IN THIS THREAD ──────────────────────────────
            self._cam_url_status.emit("Opening stream\u2026")
            print("[URL-WORKER] Step 2: opening VideoCapture(CAP_FFMPEG)...", flush=True)
            try:
                cap = cv2.VideoCapture(stream_source, cv2.CAP_FFMPEG)
                if not cap.isOpened():
                    try:
                        cap.release()
                    except Exception:
                        pass
                    # Fallback: let OpenCV pick the backend
                    print("[URL-WORKER] CAP_FFMPEG failed, trying default backend...", flush=True)
                    cap = cv2.VideoCapture(stream_source)
                print(f"[URL-WORKER] cap.isOpened()={cap.isOpened()}", flush=True)
                if not cap.isOpened():
                    self._cam_url_error.emit(f"Failed to open stream: {display_label}")
                    return
                self._tune_capture_for_low_latency(cap)
            except Exception as exc:
                print(f"[URL-WORKER] VideoCapture exception: {exc}", flush=True)
                self._cam_url_error.emit(f"VideoCapture error: {exc}")
                return

            if self._url_stream_gen != gen or self._url_stream_stop.is_set():
                print("[URL-WORKER] Superseded after open — exiting", flush=True)
                return

            # ── Step 3: verify the stream delivers frames (IN THIS THREAD) ───────
            self._cam_url_status.emit("Waiting for first frame\u2026")
            print("[URL-WORKER] Step 3: seeking first frame...", flush=True)
            first_frame = None
            try:
                for _attempt in range(10):
                    ret, fr = cap.read()
                    print(f"[URL-WORKER] frame attempt {_attempt+1}: ret={ret}, shape={fr.shape if (fr is not None and ret) else None}", flush=True)
                    if ret and fr is not None:
                        first_frame = self._detach_capture_frame(fr)
                        if first_frame is not None:
                            break
                    time.sleep(0.4)
            except Exception as exc:
                print(f"[URL-WORKER] cap.read() exception: {exc}", flush=True)
                self._cam_url_error.emit(f"Stream read error: {exc}")
                return

            if first_frame is None:
                print("[URL-WORKER] No first frame after 10 attempts", flush=True)
                self._cam_url_error.emit(f"Stream opened but returned no frames: {display_label}")
                return

            if self._url_stream_gen != gen or self._url_stream_stop.is_set():
                print("[URL-WORKER] Superseded after first-frame — exiting", flush=True)
                return

            # ── Step 4: get dimensions, store first frame, signal main thread ────
            w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) or first_frame.shape[1]
            h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) or first_frame.shape[0]
            print(f"[URL-WORKER] Step 4: stream ready {w}x{h}, emitting _cam_url_ready", flush=True)
            with self._url_stream_frame_lock:
                self._url_stream_frame = first_frame
            self._cam_url_ready.emit(display_label, stream_source, w, h, gen)

            # ── Step 5: continuous read loop — all in THIS thread ─────────────
            print("[URL-WORKER] Step 5: entering continuous read loop", flush=True)
            consecutive_fails = 0
            frames_read = 0
            try:
                while (
                    not self._url_stream_stop.is_set()
                    and self._url_stream_gen == gen
                ):
                    ret, frame = cap.read()
                    if not ret or frame is None:
                        consecutive_fails += 1
                        if consecutive_fails >= 60:  # ~3 s without a single frame
                            print(f"[URL-WORKER] 60 consecutive read failures — stopping (frames_read={frames_read})", flush=True)
                            # NOTE: self._log() is NOT safe from a background thread — use signal instead
                            self._cam_url_error.emit("Stream ended (no more frames)")
                            break
                        time.sleep(0.05)
                        continue
                    consecutive_fails = 0
                    frames_read += 1
                    if frames_read == 1:
                        print("[URL-WORKER] first loop-frame delivered to buffer", flush=True)
                    if self._url_stream_gen == gen:
                        safe_frame = self._detach_capture_frame(frame)
                        if safe_frame is None:
                            continue
                        with self._url_stream_frame_lock:
                            self._url_stream_frame = safe_frame
            except Exception as exc:
                print(f"[URL-WORKER] read loop exception: {exc}", flush=True)
            print(f"[URL-WORKER] exiting read loop, frames_read={frames_read}", flush=True)
        except Exception as exc:
            # Catch-all so the user always gets an error message, never a silent hang
            print(f"[URL-WORKER] UNHANDLED exception: {exc}", flush=True)
            try:
                self._cam_url_error.emit(f"URL stream error: {exc}")
            except Exception:
                pass
        finally:
            if cap is not None:
                try:
                    cap.release()
                except Exception:
                    pass
            if self._url_stream_gen == gen:
                self._url_stream_active = False
            print("[URL-WORKER] thread done", flush=True)

    def _on_url_ready(self, display_label: str, source_text: str, w: int, h: int, gen: int) -> None:
        """Called on the Qt main thread once the URL stream has delivered its first frame."""
        print(f"[URL-MAIN] _on_url_ready: gen={gen}, active_gen={self._url_stream_gen}, closing={self._closing}", flush=True)
        if self._closing or self._url_stream_gen != gen:
            print("[URL-MAIN] _on_url_ready: ignoring (wrong gen or closing)", flush=True)
            return
        self._local_source_kind = "url_stream"
        self._local_source_label = display_label
        self._url_stream_active = True
        self._test_media_image_frame = None
        self._test_media_last_frame = None
        self._test_media_paused = False
        self._grab_fail_count = 0
        self._cam_timer.start(50)
        self._btn_cam.setText("Close Source")
        if w > 0 and h > 0:
            self._sync_source_dimensions(w, h)
        self._set_camera_status(f"URL stream: {display_label}  ({w}x{h})", "ok")
        self._log(f"URL stream opened: {display_label} ({w}x{h})")
        self._update_test_media_controls()
        self._schedule_auto_yolo_load(300)
        print(f"[URL-MAIN] _on_url_ready: timer started, source_kind=url_stream", flush=True)

    def _on_url_status_update(self, msg: str) -> None:
        """Called on Qt main thread with live status text from the URL worker."""
        if self._closing:
            return
        self._set_camera_status(msg, "meta")

    def _on_camera_open_failed(self, source_text: str) -> None:
        """Called on Qt main thread when the background camera open failed."""
        if self._closing:
            self._camera_open_in_progress = False
            return
        self._camera_open_in_progress = False
        retry = getattr(self, "_startup_retry_count", -1)
        self._log(f"Camera open failed: {source_text} (attempt {retry+1})")
        self._btn_cam.setText("Open Source")
        if retry >= 0 and not self._has_local_source() and retry < 3:
            # Retry with increasing back-off (1.5s, 3s, 4.5s)
            delay = 1500 * (retry + 1)
            self._set_camera_status(f"Retrying camera ({retry+1}/3)…", "warn")
            QTimer.singleShot(delay, lambda r=retry+1: self._auto_open_camera_on_startup(r))
        else:
            self._startup_retry_count = -1
            self._set_camera_status(f"Failed to open: {source_text}", "error")

    def _on_url_open_error(self, msg: str) -> None:
        """Called on Qt main thread when the background URL resolve/open failed."""
        if self._closing:
            return
        self._set_camera_status(f"Video URL error: {msg}", "error")
        self._log(f"Video URL error: {msg}")
        self._btn_cam.setText("Open Source")
        # Show the error prominently on the video canvas, not just the status label
        self._video_label.set_placeholder_enabled(False)
        self._video_label.clear_frame(f"URL Error:\n{msg[:80]}")

    def _remember_camera_source(self, source_text: str, width: int, height: int) -> None:
        source_value = str(source_text or "").strip() or "0"
        self._last_camera_source_text = source_value
        self._last_camera_width = int(max(120, width))
        self._last_camera_height = int(max(120, height))

    def _attempt_camera_recovery(self, reason: str) -> bool:
        if self._closing or self._local_source_kind != "camera":
            return False
        if self._camera_recovery_in_progress:
            return True
        if self._camera_recovery_attempts >= self._MAX_CAMERA_RECOVERY_ATTEMPTS:
            return False

        src = str(getattr(self, "_last_camera_source_text", "") or "").strip()
        if not src:
            return False

        self._camera_recovery_attempts += 1
        attempt = self._camera_recovery_attempts
        self._camera_recovery_in_progress = True
        self._log(
            f"{reason} Attempting camera recovery ({attempt}/{self._MAX_CAMERA_RECOVERY_ATTEMPTS})"
        )
        self._set_camera_status(
            f"Camera stalled. Reopening source ({attempt}/{self._MAX_CAMERA_RECOVERY_ATTEMPTS})...",
            "warn",
        )
        self._close_camera(log_close=False)

        def _reopen() -> None:
            if self._closing:
                self._camera_recovery_in_progress = False
                return
            try:
                cam_src: int | str
                try:
                    cam_src = int(src)
                except ValueError:
                    cam_src = src
                self._open_video_capture_source(cam_src, src, "camera", request_frame_size=True)
            except Exception as exc:
                self._camera_recovery_in_progress = False
                self._set_camera_status(f"Camera recovery failed: {exc}", "error")
                self._log(f"Camera recovery failed ({attempt}/{self._MAX_CAMERA_RECOVERY_ATTEMPTS}): {exc}")

        # Give the camera driver enough time to fully release before reopening
        QTimer.singleShot(1500, _reopen)
        return True

    def _sync_source_dimensions(self, width: int, height: int) -> None:
        if width <= 0 or height <= 0:
            return
        self.config.guard.frame_width = int(width)
        self.config.guard.frame_height = int(height)

    def _has_local_source(self) -> bool:
        return self._cap is not None or self._test_media_image_frame is not None or self._url_stream_active

    def _close_camera(self, *, log_close: bool = True) -> None:
        self._cam_timer.stop()
        self._grab_fail_count = 0
        self._camera_black_frame_count = 0
        self._camera_partial_frame_count = 0
        self._camera_health_grace_until_s = 0.0
        self._last_display_frame = None
        # Signal URL reader thread to stop; it will release the cap itself.
        self._url_stream_stop.set()
        self._url_stream_active = False
        with self._url_stream_frame_lock:
            self._url_stream_frame = None
        if self._cap is not None:
            try:
                self._cap.release()
            except Exception:
                pass
            self._cap = None
        self._test_media_image_frame = None
        self._test_media_last_frame = None
        self._test_media_paused = False
        self._local_source_kind = ""
        self._local_source_label = ""
        if log_close:
            self._camera_recovery_attempts = 0
            self._camera_recovery_in_progress = False
        try:
            self._btn_cam.setText("Open Camera")
            self._set_camera_status("Source closed", "neutral")
            if log_close:
                self._video_label.set_placeholder_enabled(True)
                self._video_label.clear_frame("Camera Off\nOpen Camera to Start")
            else:
                self._video_label.set_placeholder_enabled(False)
                self._video_label.clear_frame("Waiting for video...")
        except RuntimeError as exc:
            if not self._closing:
                self._report_runtime_warning("Camera close UI update skipped", exc)
        self._update_test_media_controls()
        if log_close:
            self._log("Camera closed")

    def _grab_frame(self) -> None:
        """Timer-driven: grab a frame from own camera, run detection, push to engine."""
        if self._closing:
            return
        frame: Optional[np.ndarray] = None
        if self._test_media_image_frame is not None:
            frame = self._test_media_image_frame.copy()
        elif self._local_source_kind == "test_video":
            frame = self._read_next_test_video_frame()
        elif self._local_source_kind == "url_stream":
            if not self._url_stream_active:
                # Reader thread has exited — count as grab failure and auto-close
                self._grab_fail_count += 1
                if self._grab_fail_count >= self._MAX_GRAB_FAILS:
                    self._log("URL stream ended — auto-closing source")
                    self._close_camera()
                return
            with self._url_stream_frame_lock:
                frame = self._url_stream_frame
                self._url_stream_frame = None  # consume so we don't repeat the same frame
        else:
            if self._cap is None or not self._cap.isOpened():
                return
            try:
                ret, frame = self._cap.read()
            except cv2.error as exc:
                self._grab_fail_count += 1
                if self._grab_fail_count == 1 or self._grab_fail_count % 5 == 0:
                    self._log(f"Camera read error: {exc}")
                if self._grab_fail_count >= self._MAX_GRAB_FAILS:
                    if self._attempt_camera_recovery("Camera read errors persisted."):
                        return
                    self._log("Camera read errors persisted — auto-closing")
                    self._close_camera()
                return
            if not ret or frame is None:
                self._grab_fail_count += 1
                if self._grab_fail_count >= self._MAX_GRAB_FAILS:
                    if self._attempt_camera_recovery(
                        f"Camera had {self._grab_fail_count} consecutive grab failures."
                    ):
                        return
                    self._log(f"Camera: {self._grab_fail_count} consecutive grab failures — auto-closing")
                    self._close_camera()
                return
        if frame is None:
            return
        safe_frame = self._detach_capture_frame(frame)
        if safe_frame is None:
            self._grab_fail_count += 1
            if self._grab_fail_count == 1 or self._grab_fail_count % 5 == 0:
                self._log("Camera returned a malformed frame buffer")
            if self._grab_fail_count >= self._MAX_GRAB_FAILS:
                if self._attempt_camera_recovery("Camera returned malformed frame buffers."):
                    return
                self._log("Camera returned malformed frame buffers — auto-closing")
                self._close_camera()
            return
        self._grab_fail_count = 0
        if self._handle_camera_frame_health(safe_frame):
            return
        self._queue_local_frame(safe_frame)

    def _detector_worker_loop(self) -> None:
        while not self._detector_worker_stop.is_set():
            frame = None
            generation = 0
            with self._detector_frame_lock:
                if self._detector_pending_frame is not None:
                    frame = self._detector_pending_frame
                    self._detector_pending_frame = None
                    generation = int(self._detector_runtime_generation)
            if frame is None:
                time.sleep(0.01)
                continue
            try:
                self._detector_worker_busy = True
                mode = self.config.detection_mode.detection_mode
                raw_boxes = self._detector.detect(frame, mode)
                if not self._closing:
                    self.detection_result_ready.emit(frame, raw_boxes, generation)
            except Exception as exc:
                # Store error locally — do NOT write to self._comm from this thread.
                self._last_detector_error = str(exc)
            finally:
                self._detector_worker_busy = False

    def _on_detection_result_ready(self, frame: object, raw_boxes: object, generation: int) -> None:
        if self._closing:
            return
        try:
            if frame is None:
                return
            if int(generation) != int(self._detector_runtime_generation):
                return
            self.process_frame(frame, raw_boxes or [], _from_own_camera=True)
        except Exception as exc:
            self._log(f"Detection result error: {exc}")

    def _invalidate_detector_runtime(self) -> None:
        self._detector_runtime_generation += 1
        latest_frame: Optional[np.ndarray] = None
        if self._last_raw_frame is not None:
            try:
                latest_frame = self._apply_source_zoom(self._last_raw_frame.copy())
            except Exception:
                latest_frame = None
        with self._detector_frame_lock:
            self._detector_pending_frame = latest_frame
        self._last_detector_error = ""
        self._force_next_display_refresh = True
        self._last_display_present_s = 0.0
        self._last_processed_frame_s = 0.0

    # ------------------------------------------------------------------ #
    #  Detection mode handlers
    # ------------------------------------------------------------------ #

    def _on_detection_mode_changed(self, index: int) -> None:
        self.config.detection_mode.detection_mode = index
        self._update_mode_description()
        self._update_detection_panel_visibility()
        if index in {2, 4, 5, 9, 10} and "Runtime ready:" not in self._lbl_yolo_status.text():
            self._set_yolo_status("pending", "YOLO mode selected. Load a model to activate inference")
        self._sync_target_size_preset_combo()
        self._detector.reset()
        self._tracker.reset()
        self._prompted_matcher.reset()
        self._invalidate_detector_runtime()
        self._reset_detection_runtime_if_active()
        self.detection_mode_changed.emit(index)
        if not self._applying_detection_preset:
            self._set_detection_preset_label(self._match_detection_preset_name())
        if not self._applying_master_preset:
            self._set_master_profile_label(self._match_master_profile_name())
            self._update_master_stack_summary()
        self._push_config()
        self._log(f"Detection mode: {DETECTION_MODES[index]}")

    @staticmethod
    def _clamp_float(value: float, low: float, high: float) -> float:
        return max(low, min(high, float(value)))

    def _make_method_size_preset_name(self, mode: int, size_key: str) -> str:
        return f"mode_{int(mode)}__{size_key}"

    def _parse_method_size_preset_name(self, name: Optional[str]) -> Optional[Tuple[int, str]]:
        if not name or not isinstance(name, str) or not name.startswith("mode_"):
            return None
        try:
            head, size_key = name.split("__", 1)
            mode = int(head.replace("mode_", ""))
            if size_key in TARGET_SIZE_PRESETS:
                return mode, size_key
        except Exception:
            return None
        return None

    def _get_generated_method_size_settings(self, mode: int, size_key: str) -> Optional[dict]:
        base_key = MODE_BASE_PRESET.get(int(mode))
        profile = TARGET_SIZE_PRESETS.get(size_key)
        if not base_key or base_key not in DETECTION_PRESETS or not profile:
            return None

        settings = dict(DETECTION_PRESETS[base_key]["settings"])
        min_scale = float(profile.get("min_scale", 1.0))
        max_scale = float(profile.get("max_scale", 1.0))
        conf_delta = float(profile.get("yolo_conf_delta", 0.0))

        settings["detection_mode"] = int(mode)
        settings["min_contour_area"] = float(settings["min_contour_area"]) * min_scale
        settings["max_contour_area"] = float(settings["max_contour_area"]) * max_scale
        settings["yolo_min_area"] = int(max(0, round(float(settings["yolo_min_area"]) * min_scale)))
        settings["yolo_confidence"] = self._clamp_float(float(settings["yolo_confidence"]) + conf_delta, 0.05, 1.0)
        settings["color_min_area"] = int(max(1, round(float(settings["color_min_area"]) * min_scale)))
        settings["color_max_area"] = int(max(1, round(float(settings["color_max_area"]) * max_scale)))

        if settings["max_contour_area"] <= settings["min_contour_area"]:
            settings["max_contour_area"] = settings["min_contour_area"] + 1.0
        if settings["color_max_area"] <= settings["color_min_area"]:
            settings["color_max_area"] = settings["color_min_area"] + 1

        return self._tighten_detection_size_windows(settings)

    def _get_size_band_multipliers(self, mode: int) -> Tuple[float, float]:
        """Return (contour_max_multiplier, color_max_multiplier) for a mode."""
        m = int(mode)
        if m == 2:
            # Pure YOLO: contour gates are secondary, keep a bit wider.
            return 10.0, 8.0
        if m in (6, 7, 8, 9):
            # Color-led modes benefit from tighter max windows.
            return 6.0, 5.0
        if m == 10:
            # Motion-locked filtered mode should stay conservative.
            return 5.5, 4.5
        # Motion/hybrid defaults
        return 8.0, 6.0

    def _tighten_detection_size_windows(self, settings: dict) -> dict:
        """Keep preset min/max area windows reasonably close for target-size consistency."""
        normalized = dict(settings)
        mode = int(normalized.get("detection_mode", 0))
        contour_mult, color_mult = self._get_size_band_multipliers(mode)

        min_contour = max(1.0, float(normalized["min_contour_area"]))
        max_contour = float(normalized["max_contour_area"])
        contour_cap = min_contour * contour_mult
        if max_contour > contour_cap:
            max_contour = contour_cap
        if max_contour <= min_contour:
            max_contour = min_contour + 1.0

        min_color = max(1.0, float(normalized["color_min_area"]))
        max_color = float(normalized["color_max_area"])
        color_cap = min_color * color_mult
        if max_color > color_cap:
            max_color = color_cap
        if max_color <= min_color:
            max_color = min_color + 1.0

        normalized["min_contour_area"] = float(min_contour)
        normalized["max_contour_area"] = float(max_contour)
        normalized["color_min_area"] = int(round(min_color))
        normalized["color_max_area"] = int(round(max_color))
        return normalized

    def _sync_target_size_preset_combo(self) -> None:
        if not hasattr(self, "_combo_target_size_preset"):
            return
        matched = self._match_detection_preset_name()
        parsed = self._parse_method_size_preset_name(matched)
        size_key = parsed[1] if parsed else "medium"

        index = self._combo_target_size_preset.findData(size_key)
        if index < 0:
            index = self._combo_target_size_preset.findData("medium")
        if index >= 0:
            self._combo_target_size_preset.blockSignals(True)
            self._combo_target_size_preset.setCurrentIndex(index)
            self._combo_target_size_preset.blockSignals(False)

    def _apply_selected_target_size_preset(self) -> None:
        if not hasattr(self, "_combo_target_size_preset"):
            return
        size_key = str(self._combo_target_size_preset.currentData() or "medium")
        mode = int(self._combo_detection_mode.currentIndex())
        generated_settings = self._get_generated_method_size_settings(mode, size_key)
        if not generated_settings:
            return

        generated_name = self._make_method_size_preset_name(mode, size_key)
        self._apply_detection_settings(generated_settings, generated_name)

    def _reset_detection_runtime_if_active(self) -> None:
        if self.engine.get_state_name() == "PAUSED":
            return
        self._stop_fire_burst(send_release=True)
        self.engine.stop()
        self.engine.start()
        self._log("Detection runtime reset")

    def _on_detection_settings_changed(self) -> None:
        dm = self.config.detection_mode
        dm.min_contour_area = self._spin_min_contour.value()
        dm.max_contour_area = self._spin_max_contour.value()
        dm.yolo_min_area = self._spin_yolo_min_area.value()
        dm.yolo_confidence = self._spin_yolo_conf.value()
        dm.motion_gate_threshold = self._spin_motion_thresh.value()
        dm.motion_ignore_after_move_s = self._spin_motion_ignore.value()
        self._update_size_ratio_hints()
        if not self._applying_detection_preset:
            self._set_detection_preset_label(self._match_detection_preset_name())
        if not self._applying_master_preset:
            self._set_master_profile_label(self._match_master_profile_name())
            self._update_master_stack_summary()
        self._push_config()
        self._note_sound_settings_changed()

    def _scan_yolo_models(self) -> None:
        """Populate the YOLO model combo from known YOLO model directories."""
        self._combo_yolo_model.clear()
        self._yolo_model_entries = self._discover_yolo_models()
        self._update_yolo_model_dir_display()
        for label, path in self._yolo_model_entries:
            self._combo_yolo_model.addItem(label, path)

        if not self._yolo_model_entries:
            self._set_yolo_status("error", "No YOLO models found")
            return

        selected_index = self._preferred_yolo_model_index()
        if selected_index >= 0:
            self._combo_yolo_model.setCurrentIndex(selected_index)
        current_label = self._combo_yolo_model.currentText()
        if current_label:
            self.config.detection_mode.yolo_model_name = current_label
            self._set_yolo_status("info", f"Model selected: {current_label}")

    def _browse_yolo_model_dir(self) -> None:
        initial_dir = self._current_yolo_model_dir()
        selected_dir = QFileDialog.getExistingDirectory(
            self,
            "Select YOLO Models Folder",
            str(initial_dir) if initial_dir else str(self._repo_root_path()),
        )
        if not selected_dir:
            return
        chosen_path = Path(selected_dir).expanduser()
        self.config.detection_mode.yolo_model_dir = str(chosen_path)
        self._scan_yolo_models()
        self._save_config_quietly()

    def _update_yolo_model_dir_display(self) -> None:
        if not hasattr(self, "_edit_yolo_model_dir"):
            return
        current_dir = self._current_yolo_model_dir()
        if current_dir is None:
            self._edit_yolo_model_dir.clear()
            self._edit_yolo_model_dir.setPlaceholderText("Using bundled/default YOLO model folders")
            return
        self._edit_yolo_model_dir.setText(str(current_dir))
        self._edit_yolo_model_dir.setCursorPosition(0)

    def _configured_yolo_model_dir(self) -> Path | None:
        configured = str(getattr(self.config.detection_mode, "yolo_model_dir", "") or "").strip()
        if not configured:
            return None
        try:
            return Path(configured).expanduser().resolve()
        except Exception:
            return Path(configured).expanduser()

    def _release_yolo_model_dir(self) -> Path | None:
        if not getattr(sys, "frozen", False):
            return None
        try:
            return (Path(sys.executable).resolve().parent / "YOLO_MODELS").resolve()
        except Exception:
            return Path(sys.executable).parent / "YOLO_MODELS"

    def _default_yolo_model_dirs(self) -> list[Path]:
        defaults: list[Path] = []
        raw_candidates: list[Path] = [self._repo_root_path() / "YOLO_MODELS"]
        release_dir = self._release_yolo_model_dir()
        if release_dir is not None:
            raw_candidates.append(release_dir)
        raw_candidates.append(Path.cwd() / "YOLO_MODELS")
        for candidate in raw_candidates:
            try:
                resolved = candidate.resolve()
            except Exception:
                resolved = candidate
            if resolved not in defaults:
                defaults.append(resolved)
        return defaults

    def _is_default_yolo_model_dir(self, candidate: Path | None) -> bool:
        if candidate is None:
            return False
        try:
            resolved = candidate.resolve()
        except Exception:
            resolved = candidate
        return any(resolved == default_dir for default_dir in self._default_yolo_model_dirs())

    def _current_yolo_model_dir(self) -> Path | None:
        configured_dir = self._configured_yolo_model_dir()
        if configured_dir is not None and not self._is_default_yolo_model_dir(configured_dir):
            return configured_dir
        candidate_dirs = self._candidate_yolo_model_dirs()
        return candidate_dirs[0] if candidate_dirs else configured_dir

    def _load_yolo_model(self) -> None:
        """Start a background-thread YOLO model load so the event loop never freezes."""
        model_name = self._combo_yolo_model.currentText().strip()
        model_path = self._combo_yolo_model.currentData()
        if not model_name or not model_path:
            self._set_yolo_status("error", "No model selected")
            return
        if self._yolo_loading:
            return  # already loading; ignore concurrent request
        prepare_error = self._prepare_yolo_runtime()
        if prepare_error:
            self._set_yolo_status("error", f"Runtime unavailable: {model_name} ({prepare_error})")
            self._log(f"YOLO runtime prepare failed: {prepare_error}")
            return
        self._yolo_loading = True
        self._set_yolo_status("pending", f"Loading model: {model_name}")
        self._btn_load_yolo.setEnabled(False)

        def _do_load(_path: str = model_path, _name: str = model_name) -> None:
            try:
                ok = self._detector.load_yolo(_path)
                err = "" if ok else (getattr(self._detector, "_last_error", "") or "unknown error")
            except Exception as exc:
                ok = False
                err = str(exc)
            self._yolo_load_result.emit(ok, _name, err)

        threading.Thread(target=_do_load, daemon=True, name="yolo-loader").start()

    def _prepare_frozen_runtime_library_paths(self) -> None:
        if self._runtime_lib_paths_prepared or not getattr(sys, "frozen", False):
            return

        candidate_dirs: list[Path] = []
        for candidate in [
            RUNTIME_ROOT_PATH,
            Path(sys.executable).parent,
            RUNTIME_ROOT_PATH / "torch" / "lib",
            RUNTIME_ROOT_PATH / "PyQt5" / "Qt5" / "bin",
            RUNTIME_ROOT_PATH / "numpy.libs",
            RUNTIME_ROOT_PATH / "scipy.libs",
        ]:
            try:
                if candidate.is_dir() and candidate not in candidate_dirs:
                    candidate_dirs.append(candidate)
            except Exception:
                continue

        if not candidate_dirs:
            self._runtime_lib_paths_prepared = True
            return

        path_parts = os.environ.get("PATH", "").split(os.pathsep) if os.environ.get("PATH") else []
        normalized_path_parts = {
            os.path.normcase(os.path.abspath(part))
            for part in path_parts
            if part
        }
        add_dll_directory = getattr(os, "add_dll_directory", None)
        dll_dir_handles = list(getattr(self, "_runtime_dll_dir_handles", []))

        for folder in candidate_dirs:
            folder_text = os.path.abspath(str(folder))
            normalized_folder = os.path.normcase(folder_text)
            if normalized_folder not in normalized_path_parts:
                path_parts.insert(0, folder_text)
                normalized_path_parts.add(normalized_folder)
            if add_dll_directory is not None:
                try:
                    dll_dir_handles.append(add_dll_directory(folder_text))
                except Exception:
                    pass

        os.environ["PATH"] = os.pathsep.join(path_parts)
        self._runtime_dll_dir_handles = dll_dir_handles
        self._runtime_lib_paths_prepared = True

    def _prepare_yolo_runtime(self) -> str:
        if self._yolo_runtime_prepared:
            return ""
        try:
            self._emit_yolo_runtime_diagnostics("prepare-start")
            os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")
            os.environ.setdefault("OMP_NUM_THREADS", "1")
            os.environ.setdefault("MKL_NUM_THREADS", "1")
            os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")
            os.environ.setdefault("CUDA_VISIBLE_DEVICES", "")
            self._prepare_frozen_runtime_library_paths()
            self._sanitize_frozen_import_search_path()
            self._prune_pyinstaller_path_hooks_for_yolo()
            self._install_frozen_ultralytics_git_stub()
            self._prime_frozen_ultralytics_import_cache()
            import torch  # noqa: F401
            from ultralytics import YOLO as _YOLO  # noqa: F401
            self._yolo_runtime_prepared = True
            self._emit_yolo_runtime_diagnostics("prepare-ok")
            return ""
        except Exception as exc:
            self._yolo_runtime_prepared = False
            self._emit_yolo_runtime_diagnostics(
                "prepare-failed",
                error_text=f"{type(exc).__name__}: {exc}",
                trace_text=traceback.format_exc(),
            )
            return f"{type(exc).__name__}: {exc}"

    def _yolo_runtime_diag_log_path(self) -> Path:
        candidates = [
            RUNTIME_ROOT_PATH / "logs" / "yolo_runtime_diag.log",
            Path(os.environ.get("TEMP", os.environ.get("TMP", os.path.expanduser("~")))) / "yolo_runtime_diag.log",
        ]
        for candidate in candidates:
            try:
                candidate.parent.mkdir(parents=True, exist_ok=True)
                # Quick writeability check
                probe = candidate.parent / ".diag_probe"
                probe.write_text("x")
                probe.unlink(missing_ok=True)
                return candidate
            except Exception:
                continue
        return candidates[-1]

    def _emit_yolo_runtime_diagnostics(self, stage: str, error_text: str = "", trace_text: str = "") -> None:
        # Keep startup noise low: emit once unless we are recording a failure.
        if self._yolo_runtime_diag_dumped and stage != "prepare-failed":
            return
        should_mark_dumped = stage in {"prepare-start", "prepare-ok", "prepare-failed"}
        if should_mark_dumped:
            self._yolo_runtime_diag_dumped = True

        payload: dict = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "stage": str(stage or "").strip(),
            "frozen": bool(getattr(sys, "frozen", False)),
            "sys_executable": str(sys.executable),
            "cwd": str(Path.cwd()),
            "runtime_root": str(RUNTIME_ROOT_PATH),
            "app_root": str(APP_ROOT_PATH),
            "error": str(error_text or "").strip(),
            "path_head": [
                part
                for part in (os.environ.get("PATH", "").split(os.pathsep) if os.environ.get("PATH") else [])
                if str(part or "").strip()
            ][:16],
            "sys_path_head": [
                str(part)
                for part in list(sys.path)[:20]
            ],
        }
        if trace_text:
            payload["traceback"] = trace_text

        folder_checks = {}
        for candidate in [
            RUNTIME_ROOT_PATH,
            RUNTIME_ROOT_PATH / "torch" / "lib",
            RUNTIME_ROOT_PATH / "PyQt5" / "Qt5" / "bin",
            RUNTIME_ROOT_PATH / "numpy.libs",
            RUNTIME_ROOT_PATH / "scipy.libs",
        ]:
            key = str(candidate)
            try:
                folder_checks[key] = bool(candidate.is_dir())
            except Exception:
                folder_checks[key] = False
        payload["folder_checks"] = folder_checks

        module_locations = {}
        for module_name in ["torch", "ultralytics", "cv2"]:
            try:
                spec = importlib.util.find_spec(module_name)
                module_locations[module_name] = str(getattr(spec, "origin", "")) if spec else ""
            except Exception as exc:
                module_locations[module_name] = f"spec-error: {exc}"
        payload["module_locations"] = module_locations

        diag_path = self._yolo_runtime_diag_log_path()
        try:
            diag_path.parent.mkdir(parents=True, exist_ok=True)
            with diag_path.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(payload, ensure_ascii=True))
                handle.write("\n")
            self._log(f"YOLO runtime diagnostic captured: {self._portable_path_string(diag_path)}")
        except Exception:
            pass

    def _prime_frozen_ultralytics_import_cache(self) -> None:
        if not getattr(sys, "frozen", False):
            return
        try:
            import importlib.machinery as _machinery
        except Exception:
            return

        loader_details = (
            (_machinery.SourceFileLoader, _machinery.SOURCE_SUFFIXES),
            (_machinery.SourcelessFileLoader, _machinery.BYTECODE_SUFFIXES),
            (_machinery.ExtensionFileLoader, _machinery.EXTENSION_SUFFIXES),
        )

        candidate_dirs: list[Path] = []
        ultralytics_root = RUNTIME_ROOT_PATH / "ultralytics"
        if ultralytics_root.is_dir():
            candidate_dirs.append(ultralytics_root)
            utils_dir = ultralytics_root / "utils"
            if utils_dir.is_dir():
                candidate_dirs.append(utils_dir)

        for directory in candidate_dirs:
            key = str(directory)
            if key in sys.path_importer_cache:
                continue
            try:
                finder = _machinery.FileFinder(key, *loader_details)
                sys.path_importer_cache[key] = finder
            except Exception:
                continue

    def _sanitize_frozen_import_search_path(self) -> None:
        if not getattr(sys, "frozen", False):
            return
        cleaned: list[str] = []
        seen: set[str] = set()
        for entry in list(sys.path):
            text = str(entry or "").strip()
            if not text:
                continue
            try:
                normalized = os.path.normcase(os.path.abspath(text))
            except Exception:
                continue
            if normalized in seen:
                continue
            seen.add(normalized)
            cleaned.append(text)
        if cleaned:
            sys.path[:] = cleaned

    def _prune_pyinstaller_path_hooks_for_yolo(self) -> None:
        if not getattr(sys, "frozen", False):
            return
        try:
            original_hooks = list(getattr(sys, "path_hooks", []))
            filtered_hooks = [
                hook
                for hook in original_hooks
                if "pyimod02_importers" not in str(getattr(hook, "__module__", ""))
            ]
            if len(filtered_hooks) == len(original_hooks):
                return
            sys.path_hooks[:] = filtered_hooks
            for key in list(sys.path_importer_cache.keys()):
                key_text = str(key or "")
                if "ultralytics" in key_text.lower():
                    sys.path_importer_cache.pop(key, None)
            importlib.invalidate_caches()
        except Exception:
            return

    def _install_frozen_ultralytics_git_stub(self) -> None:
        if not getattr(sys, "frozen", False):
            return
        if "ultralytics.utils.git" in sys.modules:
            return
        try:
            import types

            stub = types.ModuleType("ultralytics.utils.git")

            class _GitRepo:
                def __init__(self, *args, **kwargs):
                    self.root = None
                    self.gitdir = None

                @property
                def is_repo(self) -> bool:
                    return False

                @property
                def branch(self):
                    return None

                @property
                def commit(self):
                    return None

                @property
                def origin(self):
                    return None

            stub.GitRepo = _GitRepo
            sys.modules["ultralytics.utils.git"] = stub
        except Exception:
            return

    def _on_yolo_load_result(self, ok: bool, model_name: str, err: str) -> None:
        """Called on Qt main thread when the background YOLO load completes."""
        self._yolo_loading = False
        if hasattr(self, "_btn_load_yolo"):
            self._btn_load_yolo.setEnabled(True)
        if self._closing:
            return
        if ok:
            self._set_yolo_status("ok", f"Runtime ready: {model_name}")
            self.config.detection_mode.yolo_model_name = model_name
            try:
                self.config.save()
            except Exception as exc:
                self._log(f"YOLO selection save failed: {exc}")
            self._log(f"YOLO model loaded: {model_name}")
        else:
            reason = (err or "unknown error").strip()
            if len(reason) > 80:
                reason = reason[:77] + "..."
            self._set_yolo_status("error", f"Runtime unavailable: {model_name} ({reason})")
            self._log(f"YOLO load failed: {model_name} — {err}")

    def _on_yolo_model_selection_changed(self, index: int) -> None:
        if index < 0:
            return
        model_name = self._combo_yolo_model.itemText(index).strip()
        model_path = str(self._combo_yolo_model.itemData(index) or "").strip()
        if not model_name:
            return
        self.config.detection_mode.yolo_model_name = model_name
        if model_path:
            try:
                self.config.detection_mode.yolo_model_dir = str(Path(model_path).resolve().parent)
            except Exception:
                self.config.detection_mode.yolo_model_dir = str(Path(model_path).parent)
            self._update_yolo_model_dir_display()
            self._save_config_quietly()
        if "Runtime ready:" not in self._lbl_yolo_status.text():
            self._set_yolo_status("info", f"Model selected: {model_name}")

    def _set_yolo_status(self, level: str, message: str) -> None:
        if not hasattr(self, "_lbl_yolo_status"):
            return
        level_key = (level or "info").lower().strip()
        style_map = {
            "ok": ("ok", "OK"),
            "pending": ("warn", "WAIT"),
            "error": ("error", "ERR"),
            "info": ("info", "INFO"),
        }
        style_level, badge = style_map.get(level_key, style_map["info"])
        self._lbl_yolo_status.setText(f"[{badge}] {message}")
        self._lbl_yolo_status.setStyleSheet(self._compact_status_style(style_level, bold=True))
        self._lbl_yolo_status.setToolTip(message)

    def _repo_root_path(self) -> Path:
        return RUNTIME_ROOT_PATH

    def _candidate_yolo_model_dirs(self) -> list[Path]:
        dirs: list[Path] = []
        configured_dir = self._configured_yolo_model_dir()
        candidates: list[Path] = []
        if configured_dir is not None and not self._is_default_yolo_model_dir(configured_dir):
            candidates.append(configured_dir)
        release_dir = self._release_yolo_model_dir()
        if release_dir is not None:
            candidates.append(release_dir)
        candidates.extend([
            self._repo_root_path() / "YOLO_MODELS",
            Path.cwd() / "YOLO_MODELS",
        ])
        for candidate in candidates:
            try:
                resolved = candidate.resolve()
            except Exception:
                resolved = candidate
            if resolved not in dirs and resolved.is_dir():
                dirs.append(resolved)
        return dirs

    def _discover_yolo_models(self) -> list[tuple[str, str]]:
        return self._discover_yolo_models_in_dirs(self._candidate_yolo_model_dirs())

    def _discover_yolo_models_in_dirs(self, model_dirs: list[Path]) -> list[tuple[str, str]]:
        supported_suffixes = {".pt", ".onnx", ".engine", ".torchscript"}
        discovered: dict[str, str] = {}
        for models_dir in model_dirs:
            for model_file in sorted(models_dir.rglob("*")):
                if not model_file.is_file() or model_file.suffix.lower() not in supported_suffixes:
                    continue
                relative_label = model_file.relative_to(models_dir).as_posix()
                discovered.setdefault(relative_label, str(model_file.resolve()))
        return sorted(discovered.items(), key=lambda item: self._yolo_model_sort_key(item[0]))

    def _yolo_model_sort_key(self, label: str) -> tuple[int, int, str]:
        name = Path(label).name.lower()
        if name.startswith("yolo"):
            size_rank = 9
            for suffix, rank in (("11n", 0), ("v8n", 0), ("11s", 1), ("v8s", 1), ("11m", 2), ("v8m", 2), ("11l", 3), ("v8l", 3), ("11x", 4), ("v8x", 4)):
                if suffix in name:
                    size_rank = rank
                    break
            return (0, size_rank, name)
        return (1, 99, name)

    def _preferred_yolo_model_index(self) -> int:
        if not self._yolo_model_entries:
            return -1

        preferred = (self.config.detection_mode.yolo_model_name or "").strip().lower()
        if preferred:
            for index, (label, path) in enumerate(self._yolo_model_entries):
                if preferred in {label.lower(), Path(label).name.lower(), Path(path).name.lower(), path.lower()}:
                    return index
        return 0

    def _schedule_auto_yolo_load(self, delay_ms: int = 250) -> None:
        if self._closing or self._yolo_auto_load_pending:
            return
        self._yolo_auto_load_pending = True

        def _run() -> None:
            self._yolo_auto_load_pending = False
            self._auto_load_selected_yolo_model()

        QTimer.singleShot(max(0, int(delay_ms)), _run)

    def _auto_load_selected_yolo_model(self) -> None:
        if self._closing:
            return
        if self._combo_yolo_model.count() == 0:
            self._scan_yolo_models()
        if self._combo_yolo_model.count() == 0:
            return
        current_path = str(self._combo_yolo_model.currentData() or "")
        if (
            current_path
            and os.path.abspath(current_path) == getattr(self._detector, "_yolo_model_path", "")
            and bool(getattr(self._detector, "_yolo_loaded", False))
        ):
            return
        self._load_yolo_model()

    def _on_yolo_classes_changed(self) -> None:
        classes = self._edit_yolo_classes.text().strip()
        self._detector.set_yolo_classes(classes)
        selected = [c.strip().lower() for c in classes.split(",") if c.strip()]
        self.config.target_filter.allowed_classes = selected
        for i in range(self._class_list.count()):
            item = self._class_list.item(i)
            item.setSelected(item.text() in selected)
        if not self._applying_filter_preset:
            self._set_filter_preset_label(self._match_filter_preset_name())
        if not self._applying_master_preset:
            self._set_master_profile_label(self._match_master_profile_name())
            self._update_master_stack_summary()
        self._push_config()
        self._note_sound_settings_changed()
        self._log(f"YOLO classes: {classes}")
        self._note_sound_settings_changed()

    def _on_color_settings_changed(self) -> None:
        dm = self.config.detection_mode
        dm.color_preset = self._combo_color_preset.currentText()
        dm.color_min_area = self._spin_color_min.value()
        dm.color_max_area = self._spin_color_max.value()
        dm.color_fusion_strategy = self._combo_fusion.currentText()
        dm.color_fusion_overlap = self._spin_fusion_overlap.value()
        self._update_size_ratio_hints()
        self.color_preset_changed.emit(dm.color_preset)
        
        # Log the color preset change for user feedback
        mode_name = DETECTION_MODES[dm.detection_mode] if dm.detection_mode < len(DETECTION_MODES) else "Unknown"
        color_info = f"Color: {dm.color_preset.upper()} | Area: {dm.color_min_area}-{dm.color_max_area}px"
        self._log(f"[COLOR DETECTION] {mode_name} - {color_info}")
        
        if not self._applying_detection_preset:
            self._set_detection_preset_label(self._match_detection_preset_name())
        if not self._applying_master_preset:
            self._set_master_profile_label(self._match_master_profile_name())
            self._update_master_stack_summary()
        self._push_config()
        self._note_sound_settings_changed()

    def _update_size_ratio_hints(self) -> None:
        if hasattr(self, "_lbl_contour_ratio") and hasattr(self, "_spin_min_contour") and hasattr(self, "_spin_max_contour"):
            min_contour = max(1.0, float(self._spin_min_contour.value()))
            max_contour = max(1.0, float(self._spin_max_contour.value()))
            contour_ratio = max_contour / min_contour
            self._lbl_contour_ratio.setText(f"Size window ratio: max/min = {contour_ratio:.2f}x")

        if hasattr(self, "_lbl_color_ratio") and hasattr(self, "_spin_color_min") and hasattr(self, "_spin_color_max"):
            min_color = max(1.0, float(self._spin_color_min.value()))
            max_color = max(1.0, float(self._spin_color_max.value()))
            color_ratio = max_color / min_color
            self._lbl_color_ratio.setText(f"Color window ratio: max/min = {color_ratio:.2f}x")

    def _update_detection_panel_visibility(self) -> None:
        """Show/hide detection sub-panels based on selected mode."""
        mode = self._combo_detection_mode.currentIndex()
        contour_modes = {0, 1, 3, 7, 8, 10}
        yolo_modes = {2, 4, 5, 9, 10}
        color_modes = {6, 7, 8, 9, 10}
        motion_modes = {4, 5}
        motion_sensitive_modes = {0, 1, 3, 4, 5, 7, 8, 10}

        self._grp_contour.setVisible(mode in contour_modes)
        self._grp_yolo.setVisible(mode in yolo_modes)
        self._grp_color.setVisible(mode in color_modes)
        self._grp_motion.setVisible(mode in motion_modes)
        self._grp_motion_recovery.setVisible(mode in motion_sensitive_modes)

    def _update_mode_description(self) -> None:
        descs = {
            0: "Detects motion by comparing consecutive frames.",
            1: "Learns background over time, detects foreground objects.",
            2: "Uses YOLO neural network for object detection (most accurate).",
            3: "Requires both frame difference and background subtraction to agree on the target.",
            4: "Requires both frame-difference motion and YOLO overlap before a target is valid.",
            5: "Requires both background subtraction and YOLO overlap before a target is valid.",
            6: "Detects objects by color using HSV filtering.",
            7: "Requires both color detection and frame-difference motion for moving colored objects.",
            8: "Requires both color detection and background subtraction agreement.",
            9: "Requires both color detection and YOLO overlap for colored object identification.",
            10: "Motion is mandatory. Size is applied to moving blobs, and optional color and class filters refine which moving object is tracked. Only one target is shown and engaged at a time.",
        }
        idx = self._combo_detection_mode.currentIndex()
        self._lbl_mode_desc.setText(descs.get(idx, ""))

    # ------------------------------------------------------------------ #
    #  Config change handlers
    # ------------------------------------------------------------------ #

    def _on_class_selection_changed(self) -> None:
        selected = [item.text() for item in self._class_list.selectedItems()]
        self.config.target_filter.allowed_classes = selected
        if hasattr(self, "_edit_yolo_classes"):
            self._edit_yolo_classes.blockSignals(True)
            self._edit_yolo_classes.setText(", ".join(selected))
            self._edit_yolo_classes.blockSignals(False)
        self._detector.set_yolo_classes(",".join(selected))
        if not self._applying_filter_preset:
            self._set_filter_preset_label(self._match_filter_preset_name())
        if not self._applying_master_preset:
            self._set_master_profile_label(self._match_master_profile_name())
            self._update_master_stack_summary()
        self._push_config()
        self._note_sound_settings_changed()

    def _on_filter_changed(self) -> None:
        self.config.target_filter.min_confidence = self._spin_min_conf.value()
        self.config.target_filter.min_size_ratio = self._spin_min_size.value() / 100.0
        self.config.target_filter.max_size_ratio = self._spin_max_size.value() / 100.0
        if not self._applying_filter_preset:
            self._set_filter_preset_label(self._match_filter_preset_name())
        if not self._applying_master_preset:
            self._set_master_profile_label(self._match_master_profile_name())
            self._update_master_stack_summary()
        self._push_config()
        self._note_sound_settings_changed()

    def _on_scoring_changed(self) -> None:
        ts = self.config.threat_scoring
        for key, slider in self._weight_sliders.items():
            setattr(ts, key, slider.value() / 100.0)
        ts.use_ml_model = self._chk_ml.isChecked()
        if not self._applying_threat_preset:
            self._set_threat_preset_label(self._match_threat_preset_name())
        if not self._applying_master_preset:
            self._set_master_profile_label(self._match_master_profile_name())
            self._update_master_stack_summary()
        self._push_config()

    def _on_ml_training_toggled(self, checked: bool) -> None:
        """Handle ML training mode toggle."""
        if self.engine:
            self.engine.set_ml_training_mode(checked)
            mode = "enabled" if checked else "disabled"
            self._log(f"ML training logging {mode}")
        self._refresh_ml_feature_status()

    def _resolved_ml_training_data_path(self) -> Path:
        default_path = Path("config/ml_training_data.json")
        if self.engine:
            try:
                data_file = Path(str(self.engine.get_ml_logger().data_file))
                if data_file.is_absolute():
                    return data_file
                return (self._repo_root_path() / data_file).resolve()
            except Exception:
                pass
        return (self._repo_root_path() / default_path).resolve()

    def _resolved_ml_model_path(self) -> Path:
        configured = Path(str(self.config.threat_scoring.ml_model_path or "config/smart_sentry_v3_threat_model.pkl"))
        if configured.is_absolute():
            return configured
        return (self._repo_root_path() / configured).resolve()

    def _refresh_ml_feature_status(self) -> None:
        if not hasattr(self, "_lbl_ml_status"):
            return

        try:
            sklearn_available = importlib.util.find_spec("sklearn") is not None
        except Exception:
            sklearn_available = False

        training_path = self._resolved_ml_training_data_path()
        model_path = self._resolved_ml_model_path()

        stats = self.engine.get_ml_logger_stats() if self.engine else {}
        total_records = int(stats.get("total_records", 0))
        by_source = dict(stats.get("by_source", {})) if stats else {}
        manual_fire_records = int(by_source.get("manual_fire", 0))
        model_exists = model_path.exists()
        data_exists = total_records > 0 or training_path.exists()

        self._lbl_ml_status.setText(
            f"ML runtime: sklearn {'available' if sklearn_available else 'missing'} | "
            f"logged records {total_records} | manual fire samples {manual_fire_records} | "
            f"saved model {'present' if model_exists else 'missing'}"
        )

        if hasattr(self, "_btn_open_ml_folder"):
            self._btn_open_ml_folder.setEnabled(data_exists or model_exists)

    def _open_ml_data_folder(self) -> None:
        training_path = self._resolved_ml_training_data_path()
        model_path = self._resolved_ml_model_path()
        folder_path: Optional[Path] = None

        if training_path.exists():
            folder_path = training_path.parent
        elif model_path.exists():
            folder_path = model_path.parent

        if folder_path is None:
            self._log("No saved ML training data or ML model file exists yet")
            self._refresh_ml_feature_status()
            return

        try:
            if not QDesktopServices.openUrl(QUrl.fromLocalFile(str(folder_path))):
                raise RuntimeError(f"could not open folder: {folder_path}")
            self._log(f"Opened ML data folder: {self._portable_path_string(folder_path)}")
        except Exception as exc:
            self._log(f"Open ML data folder failed: {exc}")

    def _on_precision_logging_toggled(self, checked: bool) -> None:
        """Enable or disable precision tuning logger in engine."""
        if self.engine:
            self.engine.set_precision_logging_enabled(checked)
            mode = "enabled" if checked else "disabled"
            self._log(f"Precision tuning logger {mode}")

    def _on_export_precision_csv(self) -> None:
        """Export precision tuning data to CSV."""
        if not self.engine:
            self._log("No engine running - cannot export precision CSV")
            return
        if not self.engine.is_precision_logging_enabled():
            self._log("Precision logger is OFF - enable 'Precision Tuning Logger' first")
            return
        csv_path, _ = self.engine.export_precision_logs()
        if csv_path:
            self._log(f"Precision CSV exported: {csv_path}")
        else:
            self._log("No precision tuning data available to export")

    def _on_export_precision_json(self) -> None:
        """Export precision tuning summary to JSON."""
        if not self.engine:
            self._log("No engine running - cannot export precision JSON")
            return
        if not self.engine.is_precision_logging_enabled():
            self._log("Precision logger is OFF - enable 'Precision Tuning Logger' first")
            return
        _, json_path = self.engine.export_precision_logs()
        if json_path:
            self._log(f"Precision summary exported: {json_path}")
        else:
            self._log("No precision tuning summary available to export")

    def _on_print_precision_summary(self) -> None:
        """Print precision tuning summary to console/log."""
        if not self.engine:
            self._log("No engine running - cannot print precision summary")
            return
        self.engine.print_precision_summary()
        self._log("Precision tuning summary printed to console")

    def _train_ml_model(self) -> None:
        """Train a new ML model from logged engagement data."""
        if not self.engine:
            self._log("No engine running — cannot train ML model")
            return
        
        stats = self.engine.get_ml_logger_stats()
        total = stats.get("total_records", 0)
        
        if total < 10:
            self._log(f"Not enough data to train: {total} records (need ≥10)")
            return
        
        self._log(f"Training ML model from {total} engagement records...")
        success = self.engine.train_ml_model()
        
        if success:
            self._log(f"✓ ML model trained successfully from {total} examples")
        else:
            self._log(f"✗ ML model training failed")
        self._refresh_ml_feature_status()

    def _save_ml_model(self) -> None:
        """Save the trained ML model to disk."""
        if not self.engine:
            self._log("No engine running — cannot save ML model")
            return
        
        path = self.config.threat_scoring.ml_model_path
        success = self.engine.save_ml_model(path)
        
        if success:
            self._log(f"✓ ML model saved to: {path}")
        else:
            self._log(f"✗ Failed to save ML model to: {path}")
        self._refresh_ml_feature_status()

    def _clear_ml_logs(self) -> None:
        """Clear all logged engagement data."""
        if not self.engine:
            self._log("No engine running")
            return
        
        self.engine.get_ml_logger().clear()
        self.engine.save_ml_training_data()
        self._log("✓ Engagement logs cleared")
        self._refresh_ml_feature_status()

    def _show_ml_stats(self) -> None:
        """Show summary statistics of logged engagement data."""
        if not self.engine:
            self._log("No engine running")
            return
        
        stats = self.engine.get_ml_logger_stats()
        total = stats.get("total_records", 0)
        engaged = stats.get("engaged_count", 0)
        ignored = stats.get("ignored_count", 0)
        rate = stats.get("engagement_rate", 0.0)
        
        self._log(f"ML Engagement Log Statistics:")
        self._log(f"  Total records: {total}")
        self._log(f"  Engaged: {engaged}  |  Ignored: {ignored}")
        self._log(f"  Engagement rate: {rate*100:.1f}%")
        
        classes = stats.get("class_distribution", {})
        if classes:
            self._log(f"  Classes detected: {', '.join(f'{c}({count})' for c, count in classes.items())}")
        data_file = stats.get("data_file", "")
        if data_file:
            self._log(f"  Data file: {self._portable_path_string(Path(str(data_file)))}")
        self._refresh_ml_feature_status()

    def _on_engagement_changed(self) -> None:
        eg = self.config.engagement
        eg.min_threat_score = self._spin_min_threat.value()
        eg.burst_count = self._spin_burst.value()
        eg.burst_interval_ms = self._spin_burst_interval.value()
        eg.inter_target_cooldown = self._spin_inter_cd.value()
        eg.cycle_cooldown = self._spin_cycle_cd.value()
        eg.max_queue_length = self._spin_max_queue.value()
        eg.single_target_only = eg.max_queue_length <= 1
        eg.optimize_slew_order = self._chk_optimize.isChecked()
        if eg.single_target_only:
            eg.optimize_slew_order = False
        self._sync_single_target_ui()
        eg.engagement_speed = self._slider_speed.value()
        eg.precision_aim_enabled = self._chk_precision.isChecked()
        eg.precision_settle_time = self._spin_prec_settle.value()
        eg.precision_max_step = self._spin_prec_step.value()
        eg.precision_deadzone_pan_deg = self._spin_deadzone_pan.value()
        eg.precision_deadzone_tilt_deg = self._spin_deadzone_tilt.value()
        eg.precision_error_ema = self._spin_error_ema.value()
        eg.aim_lock_pan_tolerance = self._spin_aim_lock_pan.value()
        eg.aim_lock_tilt_tolerance = self._spin_aim_lock_tilt.value()
        eg.aim_lock_required_frames = self._spin_aim_lock_frames.value()
        eg.fire_trigger_enter_pan_tolerance = self._spin_fire_enter_pan.value()
        eg.fire_trigger_enter_tilt_tolerance = self._spin_fire_enter_tilt.value()
        eg.fire_trigger_exit_pan_tolerance = self._spin_fire_exit_pan.value()
        eg.fire_trigger_exit_tilt_tolerance = self._spin_fire_exit_tilt.value()
        eg.fire_recenter_pan_tolerance = self._spin_recenter_pan.value()
        eg.fire_recenter_tilt_tolerance = self._spin_recenter_tilt.value()
        eg.target_loss_timeout = self._spin_target_loss_timeout.value()
        eg.continuous_hunt_on_loss = self._chk_continuous_hunt_loss.isChecked()
        eg.adaptive_loss_recovery_enabled = self._chk_adaptive_loss_recovery.isChecked()
        eg.loss_search_style = str(self._combo_loss_search_style.currentData() or "hunting")
        eg.loss_search_rounds = self._spin_loss_search_rounds.value()
        eg.loss_handoff_pursuit_time_s = self._spin_loss_handoff_pursuit.value()
        eg.loss_handoff_backoff_pan_deg = self._spin_loss_handoff_backoff.value()
        eg.loss_handoff_tilt_step_deg = self._spin_loss_handoff_tilt.value()
        eg.loss_persistent_retry_passes_sparse = self._spin_loss_retry_sparse.value()
        eg.loss_persistent_retry_passes_crowded = self._spin_loss_retry_crowded.value()
        eg.loss_switch_score_margin = self._spin_loss_switch_margin.value()
        eg.loss_scene_crowding_threshold = self._spin_loss_crowd_threshold.value()
        eg.loss_personality_intensity = self._spin_loss_personality.value()
        eg.loss_personality_velocity_bias = self._spin_loss_velocity_bias.value()
        self.config.pir_guard.search_style = eg.loss_search_style
        self.config.pir_guard.search_rounds = eg.loss_search_rounds
        self._update_center_fire_radius_hint()
        if not self._applying_engagement_preset:
            self._set_engagement_preset_label(self._match_engagement_preset_name())
        if not self._applying_master_preset:
            self._set_master_profile_label(self._match_master_profile_name())
            self._update_master_stack_summary()
        self._push_config()

    def _sync_single_target_ui(self) -> None:
        if not hasattr(self, "_spin_max_queue") or not hasattr(self, "_chk_optimize"):
            return
        max_queue_length = max(1, int(getattr(self.config.engagement, "max_queue_length", 1) or 1))
        single_target_only = max_queue_length <= 1
        self.config.engagement.single_target_only = single_target_only
        if single_target_only:
            self.config.engagement.optimize_slew_order = False
            self._chk_optimize.blockSignals(True)
            self._chk_optimize.setChecked(False)
            self._chk_optimize.blockSignals(False)
        self._spin_max_queue.blockSignals(True)
        self._spin_max_queue.setValue(max_queue_length)
        self._spin_max_queue.blockSignals(False)
        self._spin_max_queue.setEnabled(True)
        self._chk_optimize.setEnabled(not single_target_only)
        if hasattr(self, "_lbl_max_queue"):
            self._lbl_max_queue.setEnabled(True)

    def _update_center_fire_radius_hint(self) -> None:
        if not hasattr(self, "_lbl_center_fire_radius_hint"):
            return
        enter_pan = float(self._spin_fire_enter_pan.value())
        enter_tilt = float(self._spin_fire_enter_tilt.value())
        radius = (enter_pan + enter_tilt) * 0.5
        if hasattr(self, "_spin_center_fire_radius"):
            self._spin_center_fire_radius.blockSignals(True)
            self._spin_center_fire_radius.setValue(max(0.02, min(1.0, radius)))
            self._spin_center_fire_radius.blockSignals(False)
        self._lbl_center_fire_radius_hint.setText(
            f"Center radius: {radius:.3f} deg (Pan {enter_pan:.3f}, Tilt {enter_tilt:.3f})"
        )

    def _on_apply_center_fire_radius(self) -> None:
        radius = float(self._spin_center_fire_radius.value())
        radius = max(0.02, min(1.0, radius))

        # Map a single center-proximity radius into related fire/lock tolerances.
        fire_enter_pan = radius
        fire_enter_tilt = radius * 0.90
        fire_exit_pan = radius * 1.45
        fire_exit_tilt = radius * 1.30
        recenter_pan = radius * 1.65
        recenter_tilt = radius * 1.45
        aim_lock_pan = radius * 1.60
        aim_lock_tilt = radius * 1.35
        deadzone_pan = max(0.0, min(3.0, radius * 0.55))
        deadzone_tilt = max(0.0, min(3.0, radius * 0.48))

        lock_frames = 12
        if radius > 0.06:
            lock_frames = 10
        if radius > 0.10:
            lock_frames = 8

        updates = [
            (self._spin_fire_enter_pan, fire_enter_pan),
            (self._spin_fire_enter_tilt, fire_enter_tilt),
            (self._spin_fire_exit_pan, fire_exit_pan),
            (self._spin_fire_exit_tilt, fire_exit_tilt),
            (self._spin_recenter_pan, recenter_pan),
            (self._spin_recenter_tilt, recenter_tilt),
            (self._spin_aim_lock_pan, aim_lock_pan),
            (self._spin_aim_lock_tilt, aim_lock_tilt),
            (self._spin_deadzone_pan, deadzone_pan),
            (self._spin_deadzone_tilt, deadzone_tilt),
        ]
        for widget, value in updates:
            widget.blockSignals(True)
            widget.setValue(value)
            widget.blockSignals(False)

        self._spin_aim_lock_frames.blockSignals(True)
        self._spin_aim_lock_frames.setValue(lock_frames)
        self._spin_aim_lock_frames.blockSignals(False)

        self._on_engagement_changed()
        self._log(
            f"Center fire radius applied: {radius:.3f} deg (strict center trigger zone)"
        )

    def _apply_selected_aim_lock_fire_gate_preset(self) -> None:
        if not hasattr(self, "_combo_aim_gate_preset"):
            return
        preset_name = str(self._combo_aim_gate_preset.currentData() or "")
        if preset_name:
            self._apply_aim_lock_fire_gate_preset(preset_name)

    def _apply_sniper_center_radius_profile(self, profile: str) -> None:
        radius = SNIPER_CENTER_RADIUS_PRESETS.get(profile)
        if radius is None:
            return
        self._spin_center_fire_radius.blockSignals(True)
        self._spin_center_fire_radius.setValue(float(radius))
        self._spin_center_fire_radius.blockSignals(False)
        self._on_apply_center_fire_radius()
        self._log(f"Sniper center profile applied: {profile} ({float(radius):.3f} deg)")

    def _apply_selected_center_radius_profile(self) -> None:
        if not hasattr(self, "_combo_center_radius_preset"):
            return
        profile = str(self._combo_center_radius_preset.currentData() or "")
        if profile:
            self._apply_sniper_center_radius_profile(profile)

    def _on_guard_changed(self) -> None:
        g = self.config.guard
        g.guard_pan = self._spin_guard_pan.value()
        g.guard_tilt = self._spin_guard_tilt.value()
        g.rest_pan = self._spin_rest_pan.value()
        g.rest_tilt = self._spin_rest_tilt.value()
        g.rest_on_startup_enabled = bool(self._chk_rest_on_startup.isChecked())
        g.rest_on_close_enabled = bool(self._chk_rest_on_close.isChecked())
        g.home_move_speed_dps = float(self._spin_home_move_speed.value())
        g.home_move_approach_speed_dps = float(self._spin_home_move_approach_speed.value())
        g.rest_move_speed_dps = float(self._spin_rest_move_speed.value())
        g.rest_move_approach_speed_dps = float(self._spin_rest_move_approach_speed.value())
        g.guided_move_approach_window_deg = float(self._spin_guided_move_window.value())
        g.pan_min = self._spin_pan_min.value()
        g.pan_max = self._spin_pan_max.value()
        g.tilt_min = self._spin_tilt_min.value()
        g.tilt_max = self._spin_tilt_max.value()
        g.camera_hfov = self._spin_hfov.value()
        g.camera_vfov = self._spin_vfov.value()
        # Sweep
        g.sweep_pan_min = self._spin_sweep_min.value()
        g.sweep_pan_max = self._spin_sweep_max.value()
        g.sweep_tilt = self._spin_sweep_tilt.value()
        g.sweep_speed = self._spin_sweep_speed.value()
        # Waypoint
        g.patrol_dwell = self._spin_wp_dwell.value()
        g.patrol_speed = self._spin_wp_speed.value()
        # Random
        g.random_pan_min = self._spin_rnd_pan_min.value()
        g.random_pan_max = self._spin_rnd_pan_max.value()
        g.random_tilt_min = self._spin_rnd_tilt_min.value()
        g.random_tilt_max = self._spin_rnd_tilt_max.value()
        g.random_dwell = self._spin_rnd_dwell.value()
        g.random_speed = self._spin_rnd_speed.value()
        pan_min, pan_max = sorted((g.pan_min, g.pan_max))
        tilt_min, tilt_max = sorted((g.tilt_min, g.tilt_max))
        g.guard_pan = min(pan_max, max(pan_min, g.guard_pan))
        g.guard_tilt = min(tilt_max, max(tilt_min, g.guard_tilt))
        g.rest_pan = min(pan_max, max(pan_min, g.rest_pan))
        g.rest_tilt = min(SENTRY_TILT_MAX, max(SENTRY_TILT_MIN, g.rest_tilt))
        g.home_move_speed_dps = max(2.0, float(g.home_move_speed_dps))
        g.home_move_approach_speed_dps = max(1.0, min(g.home_move_speed_dps, float(g.home_move_approach_speed_dps)))
        g.rest_move_speed_dps = max(2.0, float(g.rest_move_speed_dps))
        g.rest_move_approach_speed_dps = max(1.0, min(g.rest_move_speed_dps, float(g.rest_move_approach_speed_dps)))
        g.guided_move_approach_window_deg = max(4.0, float(g.guided_move_approach_window_deg))
        g.sweep_pan_min = min(pan_max, max(pan_min, g.sweep_pan_min))
        g.sweep_pan_max = min(pan_max, max(pan_min, g.sweep_pan_max))
        if g.sweep_pan_min > g.sweep_pan_max:
            g.sweep_pan_min, g.sweep_pan_max = g.sweep_pan_max, g.sweep_pan_min
        g.sweep_tilt = min(tilt_max, max(tilt_min, g.sweep_tilt))
        g.random_pan_min = min(pan_max, max(pan_min, g.random_pan_min))
        g.random_pan_max = min(pan_max, max(pan_min, g.random_pan_max))
        if g.random_pan_min > g.random_pan_max:
            g.random_pan_min, g.random_pan_max = g.random_pan_max, g.random_pan_min
        g.random_tilt_min = min(tilt_max, max(tilt_min, g.random_tilt_min))
        g.random_tilt_max = min(tilt_max, max(tilt_min, g.random_tilt_max))
        if g.random_tilt_min > g.random_tilt_max:
            g.random_tilt_min, g.random_tilt_max = g.random_tilt_max, g.random_tilt_min
        self._spin_guard_pan.blockSignals(True)
        self._spin_guard_pan.setValue(g.guard_pan)
        self._spin_guard_pan.blockSignals(False)
        self._spin_guard_tilt.blockSignals(True)
        self._spin_guard_tilt.setValue(g.guard_tilt)
        self._spin_guard_tilt.blockSignals(False)
        self._spin_rest_pan.blockSignals(True)
        self._spin_rest_pan.setValue(g.rest_pan)
        self._spin_rest_pan.blockSignals(False)
        self._spin_rest_tilt.blockSignals(True)
        self._spin_rest_tilt.setValue(g.rest_tilt)
        self._spin_rest_tilt.blockSignals(False)
        self._spin_home_move_speed.blockSignals(True)
        self._spin_home_move_speed.setValue(g.home_move_speed_dps)
        self._spin_home_move_speed.blockSignals(False)
        self._spin_home_move_approach_speed.blockSignals(True)
        self._spin_home_move_approach_speed.setValue(g.home_move_approach_speed_dps)
        self._spin_home_move_approach_speed.blockSignals(False)
        self._spin_rest_move_speed.blockSignals(True)
        self._spin_rest_move_speed.setValue(g.rest_move_speed_dps)
        self._spin_rest_move_speed.blockSignals(False)
        self._spin_rest_move_approach_speed.blockSignals(True)
        self._spin_rest_move_approach_speed.setValue(g.rest_move_approach_speed_dps)
        self._spin_rest_move_approach_speed.blockSignals(False)
        self._spin_guided_move_window.blockSignals(True)
        self._spin_guided_move_window.setValue(g.guided_move_approach_window_deg)
        self._spin_guided_move_window.blockSignals(False)
        if hasattr(self, "_spin_command_rest_pan"):
            self._spin_command_rest_pan.blockSignals(True)
            self._spin_command_rest_pan.setValue(g.rest_pan)
            self._spin_command_rest_pan.blockSignals(False)
        if hasattr(self, "_spin_command_rest_tilt"):
            self._spin_command_rest_tilt.blockSignals(True)
            self._spin_command_rest_tilt.setValue(g.rest_tilt)
            self._spin_command_rest_tilt.blockSignals(False)
        self._push_config()
        self._refresh_status()
        if g.rest_on_startup_enabled and not self._startup_rest_completed:
            self._startup_rest_pending = True
            self._schedule_startup_rest_move()
        self._note_sound_settings_changed()

    def _on_command_rest_position_changed(self) -> None:
        if not hasattr(self, "_spin_rest_pan") or not hasattr(self, "_spin_rest_tilt"):
            return
        self._spin_rest_pan.blockSignals(True)
        self._spin_rest_pan.setValue(self._spin_command_rest_pan.value())
        self._spin_rest_pan.blockSignals(False)
        self._spin_rest_tilt.blockSignals(True)
        self._spin_rest_tilt.setValue(self._spin_command_rest_tilt.value())
        self._spin_rest_tilt.blockSignals(False)
        self._on_guard_changed()

    def _on_guard_mode_changed(self, index: int) -> None:
        self.config.guard.guard_mode = index
        self._update_guard_mode_visibility(index)
        self._push_config()
        modes = ["Static", "Slow Sweep", "Waypoint Patrol", "Random Scan"]
        self._log(f"Guard mode: {modes[index]}")

    def _update_guard_mode_visibility(self, mode: int) -> None:
        self._grp_sweep.setVisible(mode == 1)
        self._grp_waypoint.setVisible(mode == 2)
        self._grp_random.setVisible(mode == 3)

    def _wp_add_current(self) -> None:
        pan = self.engine.current_pan
        tilt = self.engine.current_tilt
        self.config.guard.patrol_waypoints.append((pan, tilt))
        self._wp_list.addItem(f"P{pan:.0f} T{tilt:.0f}")
        self._push_config()
        self._log(f"Waypoint added: P{pan:.0f} T{tilt:.0f}")

    def _wp_remove_selected(self) -> None:
        row = self._wp_list.currentRow()
        if row >= 0 and row < len(self.config.guard.patrol_waypoints):
            self.config.guard.patrol_waypoints.pop(row)
            self._wp_list.takeItem(row)
            self._push_config()

    def _wp_clear(self) -> None:
        self.config.guard.patrol_waypoints.clear()
        self._wp_list.clear()
        self._push_config()

    def _on_overlay_changed(self) -> None:
        self.config.show_overlay = self._chk_overlay.isChecked()
        self.config.show_threat_scores = self._chk_scores.isChecked()
        self.config.show_engagement_zone = self._chk_zone.isChecked()
        self.config.show_guard_crosshair = self._chk_guard_crosshair.isChecked()
        self.config.show_no_fire_masks = self._chk_show_no_fire_masks.isChecked()
        self.overlay.update_config(self.config)
        self._note_sound_settings_changed()

    def _populate_camera_resolution_combo(self, width: int, height: int) -> None:
        self._combo_cam_resolution.blockSignals(True)
        self._combo_cam_resolution.clear()
        current = (int(width), int(height))
        resolutions = list(STANDARD_CAMERA_RESOLUTIONS)
        if current not in resolutions:
            resolutions.append(current)
        for res_w, res_h in sorted(set(resolutions), key=lambda item: (item[0] * item[1], item[0], item[1])):
            self._combo_cam_resolution.addItem(f"{res_w} x {res_h}", (int(res_w), int(res_h)))
        index = -1
        for item_index in range(self._combo_cam_resolution.count()):
            data = self._combo_cam_resolution.itemData(item_index)
            if isinstance(data, tuple) and len(data) == 2 and int(data[0]) == current[0] and int(data[1]) == current[1]:
                index = item_index
                break
        if index < 0:
            fallback = (1280, 720)
            for item_index in range(self._combo_cam_resolution.count()):
                data = self._combo_cam_resolution.itemData(item_index)
                if isinstance(data, tuple) and len(data) == 2 and int(data[0]) == fallback[0] and int(data[1]) == fallback[1]:
                    index = item_index
                    break
        if index >= 0:
            self._combo_cam_resolution.setCurrentIndex(index)
        self._combo_cam_resolution.blockSignals(False)

    def _selected_camera_dimensions(self) -> Tuple[int, int]:
        data = self._combo_cam_resolution.currentData()
        if isinstance(data, tuple) and len(data) == 2:
            return int(data[0]), int(data[1])
        return int(self.config.connection.camera_width), int(self.config.connection.camera_height)

    def _set_camera_dimensions(self, width: int, height: int) -> None:
        self._populate_camera_resolution_combo(int(width), int(height))

    def _on_camera_resolution_changed(self, _index: int) -> None:
        width, height = self._selected_camera_dimensions()
        self.config.connection.camera_width = int(width)
        self.config.connection.camera_height = int(height)

    def _on_scope_view_changed(self) -> None:
        self.config.scope_view_enabled = self._chk_scope_view.isChecked()
        self.config.scope_radius_pct = int(self._spin_scope_radius.value())
        self.config.scope_vignette_opacity = int(self._spin_scope_vignette.value())
        self._last_scope_view_active = self._scope_view_active()
        self._push_config()
        self._note_sound_settings_changed()

    def _on_pir_enabled_changed(self, checked: bool) -> None:
        """Handle master PIR enable/disable."""
        self.config.pir_guard.pir_enabled = bool(checked)
        self._push_config()
        self._save_config_quietly()
        self._note_sound_settings_changed()
        if not self._host_controls_hardware() and self._comm.is_connected():
            self._queue_comm_task("send_pir_enabled", bool(checked))
        self._log(f"PIR guard {'enabled' if checked else 'disabled'}")

    def _on_pir_sensor_changed(self, idx: int, field: str, value: float) -> None:
        """Handle PIR sensor cue angle changes."""
        if idx < len(self.config.pir_guard.sensors):
            if field == 'cue_pan':
                self.config.pir_guard.sensors[idx].cue_pan = value
            elif field == 'cue_tilt':
                self.config.pir_guard.sensors[idx].cue_tilt = value
            self._push_config()

    def _on_pir_sensor_enabled(self, idx: int, enabled: bool) -> None:
        """Handle PIR sensor enable/disable."""
        if idx < len(self.config.pir_guard.sensors):
            self.config.pir_guard.sensors[idx].enabled = bool(enabled)
            self._push_config()

    def _on_pir_settings_changed(self) -> None:
        """Handle PIR scan and confirmation settings."""
        pg = self.config.pir_guard
        pg.scan_pan_range = self._spin_pir_scan_pan_range.value()
        pg.scan_tilt_range = self._spin_pir_scan_tilt_range.value()
        pg.scan_grid_resolution = self._spin_pir_grid_res.value()
        pg.scan_speed = self._spin_pir_scan_speed.value()
        pg.cue_hold_time_s = self._spin_pir_cue_hold.value()
        pg.confirmation_timeout = self._spin_pir_confirm_timeout.value()
        pg.scan_on_no_detect = self._chk_pir_scan_enabled.isChecked()
        pg.cross_sensor_lockout_ms = int(self._spin_pir_cross_lockout_ms.value())
        pg.pir_event_blink_enabled = bool(self._chk_pir_event_blink.isChecked())
        self._sync_comm_runtime_settings_from_config()
        self._push_config()
        self._save_config_quietly()
        self._queue_runtime_trigger_config_if_connected()
        self._note_sound_settings_changed()

    def _apply_pir_120_layout(self) -> None:
        recommended_pans = [270.0, 150.0, 30.0]
        recommended_tilt = 55.0
        while len(self.config.pir_guard.sensors) < 3:
            idx = len(self.config.pir_guard.sensors)
            self.config.pir_guard.sensors.append(PIRSensorConfig(pin_id=idx, cue_pan=recommended_pans[idx], cue_tilt=recommended_tilt, enabled=True))
        for idx, pan in enumerate(recommended_pans[:3]):
            sensor = self.config.pir_guard.sensors[idx]
            sensor.cue_pan = float(pan)
            sensor.cue_tilt = float(recommended_tilt)
            sensor.enabled = True
            if idx < len(self._pir_spin_cues):
                pan_spin, tilt_spin, chk_enabled = self._pir_spin_cues[idx]
                pan_spin.blockSignals(True)
                pan_spin.setValue(float(pan))
                pan_spin.blockSignals(False)
                tilt_spin.blockSignals(True)
                tilt_spin.setValue(float(recommended_tilt))
                tilt_spin.blockSignals(False)
                chk_enabled.blockSignals(True)
                chk_enabled.setChecked(True)
                chk_enabled.blockSignals(False)
        self._spin_pir_scan_pan_range.blockSignals(True)
        self._spin_pir_scan_pan_range.setValue(45.0)
        self._spin_pir_scan_pan_range.blockSignals(False)
        self._spin_pir_scan_tilt_range.blockSignals(True)
        self._spin_pir_scan_tilt_range.setValue(45.0)
        self._spin_pir_scan_tilt_range.blockSignals(False)
        if hasattr(self, "_spin_loss_search_rounds"):
            self._spin_loss_search_rounds.blockSignals(True)
            self._spin_loss_search_rounds.setValue(1)
            self._spin_loss_search_rounds.blockSignals(False)
        self._spin_pir_cross_lockout_ms.blockSignals(True)
        self._spin_pir_cross_lockout_ms.setValue(800)
        self._spin_pir_cross_lockout_ms.blockSignals(False)
        self._on_pir_settings_changed()
        self._log("Applied PIR 120° layout: cues=270/150/30, scan pan=45°, tilt=45°, hunt rounds=1, cross-sensor lockout=800ms")

    def _on_pan_tilt_motion_toggled(self, checked: bool) -> None:
        self._pan_tilt_motion_enabled = bool(checked)
        self.engine.set_motion_enabled(self._pan_tilt_motion_enabled)
        self._btn_motion_enable.setText(
            "Auto Motion: ON" if self._pan_tilt_motion_enabled else "Auto Motion: OFF"
        )
        self._log(
            "Automatic pan/tilt movement enabled" if self._pan_tilt_motion_enabled else "Automatic pan/tilt movement disabled; manual arrows/Home/Move to Guard still remain active"
        )

    def _pan_tilt_motion_blocked(self, reason: str) -> bool:
        if self._pan_tilt_motion_enabled:
            return False
        self._log(reason)
        self._refresh_status()
        return True

    def _update_pir_status_display(self) -> None:
        """Update PIR status label in Guard tab."""
        if not self.engine or not hasattr(self.engine, '_pir_manager'):
            self._set_label_content(self._lbl_pir_status, "Status: Engine not ready")
            return
        mgr = self.engine._pir_manager
        status_text = mgr.get_status_text()
        queued = mgr.peek_queue_count()
        if queued > 0:
            status_text += f"  [{queued} sensor(s) pending]"
        runtime = self._comm.get_io_runtime_snapshot()
        runtime_pir = runtime.get("pir_enabled")
        runtime_text = "HW ?" if runtime_pir is None else ("HW ON" if int(runtime_pir) != 0 else "HW OFF")
        last_sensor = self._pir_last_event_sensor
        last_time = self._pir_last_event_time_s
        if last_sensor is not None and last_time > 0.0:
            age_s = max(0.0, time.time() - last_time)
            last_text = f"Last S{int(last_sensor) + 1} {age_s:.1f}s ago"
        else:
            last_text = "Last none"
        self._set_label_content(
            self._lbl_pir_status,
            f"Status: {status_text} | {runtime_text} | {last_text} | Count {self._pir_event_count}",
        )

    def _scope_view_active_for_state(self, state: SentryV2State) -> bool:
        return bool(self.config.scope_view_enabled and state == SentryV2State.ENGAGING)

    def _scope_view_active(self) -> bool:
        return self._scope_view_active_for_state(self.engine.state)

    def _next_no_fire_mask_name(self) -> str:
        index = len(self.config.no_fire_masks) + 1
        existing = {str(mask.name).strip().lower() for mask in self.config.no_fire_masks}
        while f"No-Fire Zone {index}".lower() in existing:
            index += 1
        return f"No-Fire Zone {index}"

    def _refresh_no_fire_mask_list(self) -> None:
        self._mask_list.clear()
        for idx, mask in enumerate(self.config.no_fire_masks):
            state = "ON" if bool(mask.enabled) else "OFF"
            item = QListWidgetItem(f"[{state}] {mask.name} ({len(mask.vertices)} pts)")
            item.setData(Qt.UserRole, idx)
            self._mask_list.addItem(item)

    def _update_mask_editor_ui(self) -> None:
        draft_count = len(self._mask_draft_vertices)
        detail = " | click live video to add points" if self._mask_capture_active else ""
        self._lbl_mask_draft.setText(
            f"Draft: {draft_count} vertex{'es' if draft_count != 1 else ''}{detail}"
        )
        self._btn_mask_finish.setEnabled(draft_count >= 3)
        self._btn_mask_undo.setEnabled(draft_count > 0)
        self._btn_mask_clear.setEnabled(draft_count > 0)
        self._btn_mask_capture.setText(
            "Stop Capture" if self._mask_capture_active else "Capture From Video"
        )

    def _on_mask_capture_toggled(self, checked: bool) -> None:
        if checked and self._prompted_capture_active:
            self._set_prompted_capture_active(False)
        self._mask_capture_active = bool(checked)
        self._update_mask_editor_ui()
        self._log(
            "No-fire mask capture enabled: click the live video to add vertices"
            if checked else
            "No-fire mask capture stopped"
        )

    def _on_video_frame_clicked(self, frame_x: float, frame_y: float) -> None:
        if not self._mask_capture_active:
            return
        frame_w = max(1.0, float(self.config.guard.frame_width or 1))
        frame_h = max(1.0, float(self.config.guard.frame_height or 1))
        norm_x = float(frame_x) / frame_w
        norm_y = float(frame_y) / frame_h
        vertex = angular_vertex_from_normalized_point(
            norm_x,
            norm_y,
            self.engine.current_pan,
            self.engine.current_tilt,
            self.config.guard.camera_hfov,
            self.config.guard.camera_vfov,
        )
        self._mask_draft_vertices.append(vertex)
        self._update_mask_editor_ui()
        self._log(f"Added no-fire vertex {len(self._mask_draft_vertices)} at P{vertex.pan:.2f} T{vertex.tilt:.2f}")

    def _on_video_frame_right_clicked(self, frame_x: float, frame_y: float) -> None:
        if not self._mask_capture_active:
            return
        if len(self._mask_draft_vertices) < 3:
            self._log("Right-click close ignored: no-fire mask needs at least 3 vertices")
            return
        self._finish_no_fire_mask()

    def _clear_no_fire_mask_draft(self) -> None:
        self._mask_draft_vertices.clear()
        self._update_mask_editor_ui()

    def _undo_no_fire_mask_vertex(self) -> None:
        if not self._mask_draft_vertices:
            return
        self._mask_draft_vertices.pop()
        self._update_mask_editor_ui()

    def _finish_no_fire_mask(self) -> None:
        if len(self._mask_draft_vertices) < 3:
            self._log("No-fire mask needs at least 3 vertices")
            return
        name = self._edit_mask_name.text().strip() or self._next_no_fire_mask_name()
        mask = NoFireMaskConfig(
            name=name,
            enabled=True,
            vertices=[NoFireMaskVertex(pan=v.pan, tilt=v.tilt) for v in self._mask_draft_vertices],
        )
        self.config.no_fire_masks.append(mask)
        self._mask_draft_vertices.clear()
        self._mask_capture_active = False
        self._btn_mask_capture.setChecked(False)
        self._refresh_no_fire_mask_list()
        self._update_mask_editor_ui()
        self._push_config()
        self._edit_mask_name.setText(self._next_no_fire_mask_name())
        self._log(f"Saved no-fire mask '{name}' with {len(mask.vertices)} vertices")

    def _selected_no_fire_mask_indexes(self) -> List[int]:
        indexes: List[int] = []
        for item in self._mask_list.selectedItems():
            idx = item.data(Qt.UserRole)
            if isinstance(idx, int):
                indexes.append(idx)
        return sorted(set(indexes))

    def _toggle_selected_no_fire_masks(self) -> None:
        indexes = self._selected_no_fire_mask_indexes()
        if not indexes:
            return
        for idx in indexes:
            if 0 <= idx < len(self.config.no_fire_masks):
                self.config.no_fire_masks[idx].enabled = not bool(self.config.no_fire_masks[idx].enabled)
        self._refresh_no_fire_mask_list()
        self._push_config()
        self._log(f"Toggled {len(indexes)} no-fire mask(s)")

    def _remove_selected_no_fire_masks(self) -> None:
        indexes = self._selected_no_fire_mask_indexes()
        if not indexes:
            return
        for idx in reversed(indexes):
            if 0 <= idx < len(self.config.no_fire_masks):
                self.config.no_fire_masks.pop(idx)
        self._refresh_no_fire_mask_list()
        self._push_config()
        self._edit_mask_name.setText(self._next_no_fire_mask_name())
        self._log(f"Removed {len(indexes)} no-fire mask(s)")

    # ------------------------------------------------------------------ #
    #  Auto-trigger / trigger mode
    # ------------------------------------------------------------------ #

    def _on_auto_trigger_toggled(self, checked: bool) -> None:
        self.config.engagement.auto_trigger_enabled = checked
        self._sync_auto_trigger_checkbox_style()
        if not self._applying_master_preset:
            self._set_master_profile_label(self._match_master_profile_name())
            self._update_master_stack_summary()
        self._push_config()
        self._save_config_quietly()
        self._log(f"Auto-trigger: {'ON' if checked else 'OFF'}")

    def _refresh_trigger_servo_summary(self) -> None:
        if not hasattr(self, "_lbl_trigger_travel"):
            return
        rest_deg = int(self._spin_trigger_servo_rest_deg.value())
        fire_deg = int(self._spin_trigger_servo_fire_deg.value())
        speed_dps = int(self._spin_trigger_servo_speed_dps.value())
        travel_deg = abs(fire_deg - rest_deg)
        est_ms = int(round((travel_deg / max(1, speed_dps)) * 1000.0)) if travel_deg else 0
        self._lbl_trigger_travel.setText(f"Travel: {travel_deg} deg | Estimated move: {est_ms} ms")

    def _apply_trigger_servo_widget_values_from_settings(self, settings: dict) -> None:
        if not hasattr(self, "_spin_trigger_servo_rest_deg"):
            return
        widget_values = [
            (
                self._spin_trigger_servo_rest_deg,
                int(settings.get("trigger_servo_rest_deg", self.config.engagement.trigger_servo_rest_deg)),
            ),
            (
                self._spin_trigger_servo_fire_deg,
                int(settings.get("trigger_servo_fire_deg", self.config.engagement.trigger_servo_fire_deg)),
            ),
            (
                self._spin_trigger_servo_speed_dps,
                int(settings.get("trigger_servo_speed_dps", self.config.engagement.trigger_servo_speed_dps)),
            ),
        ]
        for widget, value in widget_values:
            widget.blockSignals(True)
            widget.setValue(int(value))
            widget.blockSignals(False)
        self._refresh_trigger_servo_summary()

    def _sync_comm_runtime_settings_from_config(self) -> None:
        engagement = self.config.engagement
        guard = self.config.guard
        pir_guard = self.config.pir_guard
        self._comm.trigger_servo_rest_deg = int(getattr(engagement, "trigger_servo_rest_deg", 0))
        self._comm.trigger_servo_fire_deg = int(getattr(engagement, "trigger_servo_fire_deg", 45))
        self._comm.trigger_servo_speed_dps = int(getattr(engagement, "trigger_servo_speed_dps", 360))
        self._comm.rest_pan = float(getattr(guard, "rest_pan", guard.guard_pan))
        self._comm.rest_tilt = float(getattr(guard, "rest_tilt", guard.guard_tilt))
        self._comm.pir_event_blink_enabled = bool(getattr(pir_guard, "pir_event_blink_enabled", False))

    def _queue_runtime_trigger_config_if_connected(self) -> None:
        # CHANGE WARNING: runtime trigger-servo tuning is transport-specific in the
        # comm layer, not here. If a live connection exists, let the comm layer
        # choose serial vs UDP so these controls do not silently become WiFi-only.
        if self._host_controls_hardware() or not self._comm.is_connected():
            return
        self._queue_comm_task("send_trigger_runtime_config")

    def _on_trigger_servo_settings_changed(self) -> None:
        rest_deg = int(self._spin_trigger_servo_rest_deg.value())
        fire_deg = int(self._spin_trigger_servo_fire_deg.value())
        if fire_deg < rest_deg:
            fire_deg = rest_deg
            self._spin_trigger_servo_fire_deg.blockSignals(True)
            self._spin_trigger_servo_fire_deg.setValue(fire_deg)
            self._spin_trigger_servo_fire_deg.blockSignals(False)
        self.config.engagement.trigger_servo_rest_deg = rest_deg
        self.config.engagement.trigger_servo_fire_deg = fire_deg
        self.config.engagement.trigger_servo_speed_dps = int(self._spin_trigger_servo_speed_dps.value())
        self._sync_comm_runtime_settings_from_config()
        self._refresh_trigger_servo_summary()
        self._push_config()
        self._save_config_quietly()
        self._queue_runtime_trigger_config_if_connected()
        self._note_sound_settings_changed()

    def _on_trigger_mode_changed(self, index: int) -> None:
        is_bb = (index == 1)
        self.config.engagement.trigger_mode_bb = is_bb
        self._comm.trigger_mode_bb = is_bb
        self._sync_comm_runtime_settings_from_config()
        if self._host_controls_hardware():
            pass
        elif self._comm.is_connected():
            self._queue_comm_task("send_command",
                self.engine.current_pan,
                self.engine.current_tilt,
                fire=0,
                move_time_ms=self._get_manual_move_time_ms(),
            )
            self._queue_runtime_trigger_config_if_connected()
        self._note_sound_settings_changed()
        if not self._applying_master_preset:
            self._set_master_profile_label(self._match_master_profile_name())
            self._update_master_stack_summary()
        self._push_config()
        self._save_config_quietly()
        mode_name = "Projectile (ESP32 GPIO13 Servo)" if is_bb else "Water (MOSFET)"
        self._log(f"Trigger mode: {mode_name}")

    # ------------------------------------------------------------------ #
    #  Manual control handlers
    # ------------------------------------------------------------------ #

    def _move_to_absolute_position(
        self,
        pan: float,
        tilt: float,
        *,
        hold_guard: bool = False,
        log_message: str = "",
        allow_rest_tilt: bool = False,
    ) -> None:
        self._finish_guided_move(cancelled=True)
        pan, tilt = self._clamp_manual_angles(pan, tilt, allow_rest_tilt=allow_rest_tilt)
        move_time_ms = self._get_manual_move_time_ms()
        self._manual_move_priority_until = max(
            float(getattr(self, "_manual_move_priority_until", 0.0) or 0.0),
            time.time() + float(getattr(self, "_manual_position_hold_s", 1.25) or 1.25),
        )
        if hold_guard:
            self.engine.hold_current_guard_position(pan, tilt)
        else:
            self.engine.current_pan = pan
            self.engine.current_tilt = tilt
        if self._host_controls_hardware():
            self.turret_move_requested.emit(float(pan), float(tilt))
        else:
            self._queue_move_command(pan, tilt, move_time_ms=move_time_ms, manual_override=True)
        self._remember_commanded_position(pan, tilt, move_time_ms=move_time_ms)
        self._suppress_motion_detection()
        self._refresh_status()
        if log_message:
            self._log(log_message)

    def _move_to_manual_limit(self, axis: str, direction: str) -> None:
        guard = self.config.guard
        pan = float(self.engine.current_pan)
        tilt = float(self.engine.current_tilt)
        if axis == "pan":
            pan = float(guard.pan_max if direction == "max" else guard.pan_min)
            label = "Max pan" if direction == "max" else "Min pan"
        else:
            tilt = float(guard.tilt_max if direction == "max" else guard.tilt_min)
            label = "Max tilt" if direction == "max" else "Min tilt"
        self._move_to_absolute_position(pan, tilt, log_message=f"Manual preset: {label} (P{pan:.0f} T{tilt:.0f})")

    def _move_to_manual_corner(self, pan_side: str, tilt_side: str) -> None:
        guard = self.config.guard
        pan = float(guard.pan_max if pan_side == "max" else guard.pan_min)
        tilt = float(guard.tilt_max if tilt_side == "max" else guard.tilt_min)
        label = f"{'Right' if pan_side == 'max' else 'Left'} / {'Top' if tilt_side == 'max' else 'Bottom'}"
        self._move_to_absolute_position(pan, tilt, log_message=f"Manual preset: {label} corner (P{pan:.0f} T{tilt:.0f})")

    def _manual_move(self, pan_dir: int, tilt_dir: int) -> None:
        self._finish_guided_move(cancelled=True)
        step = self._spin_step.value()
        new_pan = self.engine.current_pan + pan_dir * step
        new_tilt = self.engine.current_tilt + tilt_dir * step
        new_pan, new_tilt = self._clamp_manual_angles(new_pan, new_tilt)
        move_time_ms = self._get_manual_move_time_ms()
        self._manual_move_priority_until = max(
            float(getattr(self, "_manual_move_priority_until", 0.0) or 0.0),
            time.time() + float(getattr(self, "_manual_position_hold_s", 1.25) or 1.25),
        )
        self.engine.current_pan = new_pan
        self.engine.current_tilt = new_tilt
        if self._host_controls_hardware():
            self.manual_move_requested.emit(int(pan_dir * step), int(tilt_dir * step))
        else:
            self._queue_move_command(new_pan, new_tilt, move_time_ms=move_time_ms, manual_override=True)
        self._remember_commanded_position(new_pan, new_tilt, move_time_ms=move_time_ms)
        self._suppress_motion_detection()
        self._refresh_status()

    def _on_home_clicked(self) -> None:
        self._startup_rest_schedule_token += 1
        self._startup_rest_pending = False
        self._startup_rest_completed = True
        pan = self._spin_guard_pan.value()
        tilt = self._spin_guard_tilt.value()
        waking_from_rest = self._is_near_rest_position(float(self.engine.current_pan), float(self.engine.current_tilt), tolerance_deg=8.0)
        self._play_home_cue(waking_from_rest=waking_from_rest)
        self._start_guided_position_move(pan, tilt, maneuver="home", hold_guard=True, log_message="Go Home")

    def _on_rest_clicked(self) -> None:
        self._move_to_rest()

    def _set_manual_sweep_button_state(self, active: bool) -> None:
        self._manual_sweep_active = bool(active)
        if hasattr(self, "_btn_manual_sweep"):
            self._btn_manual_sweep.setEnabled(not active)
            self._btn_manual_sweep.setText("SWEEPING..." if active else "RUN SWEEP")

    def _get_manual_sweep_move_time_ms(
        self,
        from_pan: float,
        from_tilt: float,
        to_pan: float,
        to_tilt: float,
    ) -> int:
        delta_deg = max(abs(float(to_pan) - float(from_pan)), abs(float(to_tilt) - float(from_tilt)), 1.0)
        sweep_speed = max(0.5, float(getattr(self.config.guard, "sweep_speed", 6.0) or 6.0))
        timed_move_ms = int(round((delta_deg / sweep_speed) * 1000.0))
        return int(max(self._get_manual_move_time_ms(), min(30000, timed_move_ms)))

    def _finish_manual_sweep(self, *, log_message: str = "") -> None:
        self._manual_sweep_timer.stop()
        self._manual_sweep_steps.clear()
        was_active = bool(getattr(self, "_manual_sweep_active", False))
        self._set_manual_sweep_button_state(False)
        if log_message and was_active and not self._closing:
            self._log(log_message)

    def _advance_manual_sweep(self) -> None:
        if self._closing:
            self._finish_manual_sweep()
            return
        if not self._manual_sweep_steps:
            self._finish_manual_sweep(log_message="Manual sweep complete")
            return

        target_pan, target_tilt, move_time_ms, label = self._manual_sweep_steps.popleft()
        self._manual_move_priority_until = max(
            float(getattr(self, "_manual_move_priority_until", 0.0) or 0.0),
            time.time() + max(1.25, float(move_time_ms) / 1000.0 + 0.25),
        )
        self.engine.current_pan = float(target_pan)
        self.engine.current_tilt = float(target_tilt)
        if self._host_controls_hardware():
            self.turret_move_requested.emit(float(target_pan), float(target_tilt))
        else:
            self._queue_move_command(float(target_pan), float(target_tilt), move_time_ms=int(move_time_ms), manual_override=True)
        self._remember_commanded_position(float(target_pan), float(target_tilt), move_time_ms=int(move_time_ms))
        self._suppress_motion_detection()
        self._refresh_status()
        self._log(f"Manual sweep: {label} (P{float(target_pan):.0f} T{float(target_tilt):.0f})")
        self._manual_sweep_timer.start(max(180, int(move_time_ms) + 180))

    def _on_manual_sweep_clicked(self) -> None:
        self._finish_guided_move(cancelled=True)
        if self._host_controls_hardware():
            self._log("Manual sweep unavailable while hardware is managed by the host application")
            return
        if self._manual_sweep_active:
            self._log("Manual sweep already in progress")
            return

        guard = self.config.guard
        current_pan, current_tilt = self._clamp_manual_angles(float(self.engine.current_pan), float(self.engine.current_tilt))
        pan_min, pan_max = sorted((float(guard.sweep_pan_min), float(guard.sweep_pan_max)))
        tilt_min, tilt_max = sorted((float(guard.tilt_min), float(guard.tilt_max)))
        sweep_tilt = min(tilt_max, max(tilt_min, float(guard.sweep_tilt)))

        raw_targets = [
            (pan_min, current_tilt, "pan min"),
            (pan_max, current_tilt, "pan max"),
        ]
        if abs(sweep_tilt - current_tilt) >= 0.1:
            raw_targets.append((pan_max, sweep_tilt, "tilt stage"))
        raw_targets.extend([
            (pan_max, tilt_min, "tilt min"),
            (pan_max, tilt_max, "tilt max"),
        ])

        steps: deque[tuple[float, float, int, str]] = deque()
        last_pan = float(current_pan)
        last_tilt = float(current_tilt)
        for target_pan, target_tilt, label in raw_targets:
            target_pan, target_tilt = self._clamp_manual_angles(float(target_pan), float(target_tilt))
            if max(abs(target_pan - last_pan), abs(target_tilt - last_tilt)) < 0.1:
                continue
            move_time_ms = self._get_manual_sweep_move_time_ms(last_pan, last_tilt, target_pan, target_tilt)
            steps.append((float(target_pan), float(target_tilt), int(move_time_ms), str(label)))
            last_pan = float(target_pan)
            last_tilt = float(target_tilt)

        if not steps:
            self._log("Manual sweep skipped: already at configured sweep and tilt limits")
            return

        self._manual_sweep_steps = steps
        self._set_manual_sweep_button_state(True)
        self._log(
            f"Manual sweep started: pan {pan_min:.0f}→{pan_max:.0f}, then tilt {tilt_min:.0f}→{tilt_max:.0f} at {float(guard.sweep_speed):.1f} deg/s"
        )
        QTimer.singleShot(0, self._advance_manual_sweep)

    def _on_led_toggled(self, checked: bool) -> None:
        self._led_on = checked
        self._btn_led.setText(f"LED: {'ON' if checked else 'OFF'}")
        if not self._host_controls_hardware():
            if checked:
                auto_enabled = bool(getattr(self.config.lighting, "auto_lighting_enabled", False))
                if auto_enabled:
                    # Auto-lighting drives PWM; let next brightness sample set it
                    self._queue_comm_task("set_led_pwm", self._auto_led_pwm or 1, self.engine.current_pan, self.engine.current_tilt)
                else:
                    pwm = int(max(0, min(255, getattr(self.config.lighting, "led_pwm_value", 255))))
                    self._queue_comm_task("set_led_pwm", pwm, self.engine.current_pan, self.engine.current_tilt)
            else:
                self._queue_comm_task("set_led_pwm", 0, self.engine.current_pan, self.engine.current_tilt)

    def _on_laser_toggled(self, checked: bool) -> None:
        self._laser_on = checked
        self._btn_laser.setText(f"Laser: {'ON' if checked else 'OFF'}")
        if not self._host_controls_hardware():
            self._queue_comm_task("set_laser", checked, self.engine.current_pan, self.engine.current_tilt)

    def _on_acc_toggled(self, checked: bool) -> None:
        self._acc_on = checked
        self._btn_acc.setText(f"ACC: {'ON' if checked else 'OFF'}")
        if not self._host_controls_hardware():
            self._queue_comm_task("set_acc", checked, self.engine.current_pan, self.engine.current_tilt)

    def _on_spare_toggled(self, checked: bool) -> None:
        self._spare_on = checked
        self._btn_spare.setText(f"Spare: {'ON' if checked else 'OFF'}")
        if not self._host_controls_hardware():
            self._queue_comm_task("set_spare", checked, self.engine.current_pan, self.engine.current_tilt)

    def _on_control_source_toggled(self, checked: bool) -> None:
        mode = "rc" if checked else "app"
        self._control_source_mode = mode
        self._btn_control_source.setText(f"Control Source: {'FLYSKY' if checked else 'APP'}")
        if hasattr(self, "_lbl_control_source_status"):
            self._set_label_content(
                self._lbl_control_source_status,
                f"FlySky mode request: {'RC' if checked else 'APP'}",
                f"font-weight: bold; color: {'#8fe3c4' if checked else '#97a8b8'}; font-size: 10px;",
            )
        if not self._host_controls_hardware():
            self._queue_comm_task("set_control_source_mode", mode)

    def _on_safety_toggled(self, checked: bool) -> None:
        self._safety_armed = checked
        self._btn_safety.setText(f"Safety: {'ARMED' if checked else 'LOCKED'}")
        if not self._host_controls_hardware():
            self._queue_comm_task("set_safety", checked, self.engine.current_pan, self.engine.current_tilt)

    def _on_manual_fire(self, state: int) -> None:
        host_controls_hardware = self._host_controls_hardware()
        if state and not self._safety_armed:
            self._log("Manual fire blocked: Safety is LOCKED")
            if not host_controls_hardware:
                self._queue_comm_task("send_command",
                    self.engine.current_pan,
                    self.engine.current_tilt,
                    fire=0,
                    move_time_ms=self._get_manual_move_time_ms(),
                )
            return
        pan = self.engine.current_pan
        tilt = self.engine.current_tilt
        if state and not host_controls_hardware:
            if not self._comm.trigger_mode_bb:
                self._log("Manual fire note: trigger mode is Water (MOSFET), not Projectile (ESP32 GPIO13 Servo)")
            _comm_mode = getattr(self._comm, "_mode", None)
            _udp_broken = (
                getattr(self._comm, "_sock", None) is None
                or getattr(self._comm, "_udp_target", None) is None
            )
            if _udp_broken and _comm_mode in (
                self._comm.MODE_WIFI_DEBUG_USB,
                self._comm.MODE_WIFI_FULL,
                self._comm.MODE_DUAL_ESP32_WIFI,
            ):
                self._log(
                    "Manual fire unavailable: WiFi/UDP link to ESP32 is not connected "
                    "(mode %d) — check that the PC is connected to the SMART-SENTRY WiFi AP "
                    "and try reconnecting from the Connection tab." % _comm_mode
                )
        if host_controls_hardware:
            self.manual_fire_requested.emit(int(state))
            return
        if self._comm.trigger_mode_bb:
            if not state:
                return
            self._queue_comm_task("send_command", pan, tilt, fire=1, move_time_ms=self._get_manual_move_time_ms())
            self._arm_manual_projectile_fire_release(pan, tilt)
            return
        self._queue_comm_task("send_command", pan, tilt, fire=state, move_time_ms=self._get_manual_move_time_ms())

    def _arm_manual_projectile_fire_release(self, pan: float, tilt: float) -> None:
        self._manual_projectile_fire_release_pan = float(pan)
        self._manual_projectile_fire_release_tilt = float(tilt)
        self._manual_projectile_fire_latched = True
        self._manual_projectile_fire_release_timer.stop()
        self._manual_projectile_fire_release_timer.start(MANUAL_TRIGGER_SERVO_LATCH_MS)

    def _flush_manual_projectile_fire_release(self) -> None:
        if not bool(getattr(self, "_manual_projectile_fire_latched", False)):
            return
        self._manual_projectile_fire_latched = False
        if self._closing or self._host_controls_hardware():
            return
        self._queue_comm_task(
            "send_command",
            float(getattr(self, "_manual_projectile_fire_release_pan", self.engine.current_pan)),
            float(getattr(self, "_manual_projectile_fire_release_tilt", self.engine.current_tilt)),
            fire=0,
            move_time_ms=self._get_manual_move_time_ms(),
        )

    # ------------------------------------------------------------------ #
    #  Guard position buttons
    # ------------------------------------------------------------------ #

    def _go_to_guard(self) -> None:
        pan = self._spin_guard_pan.value()
        tilt = self._spin_guard_tilt.value()
        self._move_to_absolute_position(pan, tilt, hold_guard=True, log_message=f"Moving to guard: P{pan:.0f} T{tilt:.0f}")

    def _set_current_as_guard(self) -> None:
        pan = self.engine.current_pan
        tilt = self.engine.current_tilt
        self._spin_guard_pan.blockSignals(True)
        self._spin_guard_pan.setValue(pan)
        self._spin_guard_pan.blockSignals(False)
        self._spin_guard_tilt.blockSignals(True)
        self._spin_guard_tilt.setValue(tilt)
        self._spin_guard_tilt.blockSignals(False)
        self._on_guard_changed()
        self._refresh_status()
        self._log(f"Guard set to current: P{pan:.0f} T{tilt:.0f}")

    def _set_current_as_rest(self) -> None:
        pan = self.engine.current_pan
        tilt = self.engine.current_tilt
        self._spin_rest_pan.blockSignals(True)
        self._spin_rest_pan.setValue(pan)
        self._spin_rest_pan.blockSignals(False)
        self._spin_rest_tilt.blockSignals(True)
        self._spin_rest_tilt.setValue(tilt)
        self._spin_rest_tilt.blockSignals(False)
        if hasattr(self, "_spin_command_rest_pan"):
            self._spin_command_rest_pan.blockSignals(True)
            self._spin_command_rest_pan.setValue(pan)
            self._spin_command_rest_pan.blockSignals(False)
        if hasattr(self, "_spin_command_rest_tilt"):
            self._spin_command_rest_tilt.blockSignals(True)
            self._spin_command_rest_tilt.setValue(tilt)
            self._spin_command_rest_tilt.blockSignals(False)
        self._on_guard_changed()
        self._refresh_status()
        self._log(f"Rest set to current: P{pan:.0f} T{tilt:.0f}")

    def _select_all_classes(self) -> None:
        self._class_list.selectAll()

    def _select_no_classes(self) -> None:
        self._class_list.clearSelection()

    def _save_config(self) -> None:
        try:
            self._capture_layout_state()
            # Persist connection settings from UI
            cc = self.config.connection
            cc.connection_type = self._combo_conn_type.currentIndex()
            cc.esp32_port = self._edit_esp32_port.text().strip()
            cc.esp32_baud = self._spin_esp32_baud.value()
            cc.debug_port = self._edit_debug_port.text().strip()
            cc.debug_baud = self._spin_debug_baud.value()
            cc.udp_host = self._edit_udp_host.text().strip()
            cc.udp_port = self._spin_udp_port.value()
            cc.wifi_interface = str(self._combo_wifi_adapter.currentData() or "").strip()
            cc.servo_udp_host = self._edit_servo_udp_host.text().strip()
            cc.servo_udp_port = self._spin_servo_udp_port.value()
            cc.pan_servo_id = self._spin_pan_id.value()
            cc.tilt_servo_id = self._spin_tilt_id.value()
            cc.bus_servo_time_ms = self._spin_servo_time.value()
            cc.invert_pan = self._chk_invert_pan.isChecked()
            cc.invert_tilt = self._chk_invert_tilt.isChecked()
            cc.camera_source = self._edit_cam_source.text().strip()
            selected_width, selected_height = self._selected_camera_dimensions()
            cc.camera_width = selected_width
            cc.camera_height = selected_height
            cc.webcam_zoom_pct = int(self._slider_webcam_zoom.value())
            cc.test_source_zoom_pct = int(self._slider_test_zoom.value())
            self.config.prompted_targets_enabled = bool(getattr(self, "_chk_prompted_enabled", None) and self._chk_prompted_enabled.isChecked())
            self.config.prompted_allow_auto_fire = bool(getattr(self, "_chk_prompted_auto_fire", None) and self._chk_prompted_auto_fire.isChecked())
            self.config.prompted_library_path = self._portable_path_string(self._resolved_prompted_library_path())
            self.config.face_recognition.library_path = self._portable_path_string(self._resolved_face_library_path())
            self.config.shortcuts.quick_view_doc_path = self._portable_path_string(SMART_SENTRY_SHORTCUT_KEYS_DOC_PATH)
            self.config.config_path = CANONICAL_SETTINGS_RELATIVE_PATH
            self.config.save(str(CANONICAL_SETTINGS_PATH))
            self._sync_legacy_settings_copy()
            self._save_prompted_target_library()
            self._save_face_identity_library()
            self._log(f"Settings saved: {self.config.config_path}")
        except Exception as e:
            self._log(f"Save error: {e}")

    def _save_config_quietly(self) -> None:
        self._pending_quiet_save = True
        self._quiet_save_timer.start(450)

    def _flush_quiet_config_save(self) -> None:
        if not self._pending_quiet_save:
            return
        self._pending_quiet_save = False
        try:
            self._capture_layout_state()
            self.config.face_recognition.library_path = self._portable_path_string(self._resolved_face_library_path())
            self.config.shortcuts.quick_view_doc_path = self._portable_path_string(SMART_SENTRY_SHORTCUT_KEYS_DOC_PATH)
            self.config.config_path = CANONICAL_SETTINGS_RELATIVE_PATH
            self.config.save(str(CANONICAL_SETTINGS_PATH))
            self._sync_legacy_settings_copy()
        except Exception as exc:
            self._log(f"Save error: {exc}")

    def _windows_wifi_current_ssid(self) -> str:
        if os.name != "nt":
            return ""
        try:
            result = subprocess.run(
                ["netsh", "wlan", "show", "interfaces"],
                capture_output=True,
                text=True,
                timeout=6,
                check=False,
                **_windows_hidden_subprocess_kwargs(),
            )
        except Exception:
            return ""
        output = f"{result.stdout}\n{result.stderr}"
        preferred_ssid = ""
        fallback_ssid = ""
        in_connected_block = False
        for raw_line in output.splitlines():
            line = raw_line.strip()
            lower_line = line.lower()
            if not line or ":" not in line:
                continue
            key, value = line.split(":", 1)
            key = key.strip().lower()
            value = value.strip()
            if key == "state":
                in_connected_block = "connected" in value.lower()
                continue
            if key == "ssid" and value:
                if in_connected_block:
                    preferred_ssid = value
                    break
                fallback_ssid = value
                continue
        if preferred_ssid:
            return preferred_ssid
        if fallback_ssid:
            return fallback_ssid
        return ""

    def _normalize_ssid(self, ssid: str) -> str:
        return str(ssid or "").strip().casefold()

    def _ssid_matches_expected(self, candidate_ssid: str, expected_ssids: Iterable[str]) -> bool:
        normalized_candidate = self._normalize_ssid(candidate_ssid)
        if not normalized_candidate:
            return False
        return normalized_candidate in {
            self._normalize_ssid(expected)
            for expected in expected_ssids
            if str(expected or "").strip()
        }

    def _windows_wifi_network_available(self, ssid: str) -> bool:
        if os.name != "nt" or not ssid:
            return False
        try:
            result = subprocess.run(
                ["netsh", "wlan", "show", "networks", "mode=bssid"],
                capture_output=True,
                text=True,
                timeout=8,
                check=False,
                **_windows_hidden_subprocess_kwargs(),
            )
        except Exception:
            return False
        normalized_target = self._normalize_ssid(ssid)
        for raw_line in f"{result.stdout}\n{result.stderr}".splitlines():
            line = str(raw_line or "").strip()
            if not line.startswith("SSID ") or ":" not in line:
                continue
            _key, value = line.split(":", 1)
            if self._normalize_ssid(value) == normalized_target:
                return True
        return False

    def _windows_wifi_profile_exists(self, ssid: str) -> bool:
        if os.name != "nt" or not ssid:
            return False
        try:
            result = subprocess.run(
                ["netsh", "wlan", "show", "profiles"],
                capture_output=True,
                text=True,
                timeout=6,
                check=False,
                **_windows_hidden_subprocess_kwargs(),
            )
        except Exception:
            return False
        normalized_target = self._normalize_ssid(ssid)
        for raw_line in f"{result.stdout}\n{result.stderr}".splitlines():
            line = str(raw_line or "").strip()
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            if "all user profile" not in key.strip().lower():
                continue
            if self._normalize_ssid(value) == normalized_target:
                return True
        return False

    def _windows_wifi_profile_text(self, ssid: str, *, include_key: bool = False) -> str:
        if os.name != "nt" or not ssid:
            return ""
        command = ["netsh", "wlan", "show", "profile", f"name={ssid}"]
        if include_key:
            command.append("key=clear")
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=8,
                check=False,
                **_windows_hidden_subprocess_kwargs(),
            )
        except Exception:
            return ""
        return f"{result.stdout}\n{result.stderr}"

    def _enumerate_windows_wifi_interfaces(self) -> list:
        """Return a list of Windows WiFi interface names from netsh."""
        if os.name != "nt":
            return []
        try:
            result = subprocess.run(
                ["netsh", "wlan", "show", "interfaces"],
                capture_output=True,
                text=True,
                timeout=6,
                check=False,
                **_windows_hidden_subprocess_kwargs(),
            )
        except Exception:
            return []
        names = []
        for raw_line in (result.stdout or "").splitlines():
            line = raw_line.strip()
            if line.lower().startswith("name") and ":" in line:
                name = line.split(":", 1)[1].strip()
                if name:
                    names.append(name)
        return names

    def _windows_wifi_primary_interface_name(self) -> str:
        if os.name != "nt":
            return ""
        # If the user has configured a specific adapter, use it directly.
        preferred = str(getattr(self.config.connection, "wifi_interface", "") or "").strip()
        if preferred:
            return preferred
        try:
            result = subprocess.run(
                ["netsh", "wlan", "show", "interfaces"],
                capture_output=True,
                text=True,
                timeout=6,
                check=False,
                **_windows_hidden_subprocess_kwargs(),
            )
        except Exception:
            return ""
        output = f"{result.stdout}\n{result.stderr}"
        for raw_line in output.splitlines():
            line = raw_line.strip()
            lower_line = line.lower()
            if lower_line.startswith("name") and ":" in line:
                return line.split(":", 1)[1].strip()
        return ""

    def _windows_wifi_delete_profile(self, ssid: str) -> None:
        if os.name != "nt" or not ssid:
            return
        try:
            subprocess.run(
                ["netsh", "wlan", "delete", "profile", f"name={ssid}"],
                capture_output=True,
                text=True,
                timeout=8,
                check=False,
                **_windows_hidden_subprocess_kwargs(),
            )
        except Exception:
            pass

    def _windows_wifi_profile_is_compatible(self, ssid: str, password: str) -> bool:
        profile_text = self._windows_wifi_profile_text(ssid, include_key=True).lower()
        if not profile_text:
            return False
        auth_ok = "wpa2" in profile_text and "wpa3" not in profile_text
        auto_ok = "connect automatically" in profile_text
        key_ok = f"key content            : {password.lower()}" in profile_text
        return auth_ok and auto_ok and key_ok

    def _ensure_windows_wifi_profile(self, ssid: str, password: str) -> bool:
        if self._windows_wifi_profile_exists(ssid) and self._windows_wifi_profile_is_compatible(ssid, password):
            return True
        if self._windows_wifi_profile_exists(ssid):
            self._windows_wifi_delete_profile(ssid)
        profile_xml = (
            "<?xml version=\"1.0\"?>\n"
            "<WLANProfile xmlns=\"http://www.microsoft.com/networking/WLAN/profile/v1\">\n"
            f"  <name>{ssid}</name>\n"
            "  <SSIDConfig>\n"
            "    <SSID>\n"
            f"      <name>{ssid}</name>\n"
            "    </SSID>\n"
            "  </SSIDConfig>\n"
            "  <connectionType>ESS</connectionType>\n"
            "  <connectionMode>auto</connectionMode>\n"
            "  <MSM>\n"
            "    <security>\n"
            "      <authEncryption>\n"
            "        <authentication>WPA2PSK</authentication>\n"
            "        <encryption>AES</encryption>\n"
            "        <useOneX>false</useOneX>\n"
            "      </authEncryption>\n"
            "      <sharedKey>\n"
            "        <keyType>passPhrase</keyType>\n"
            "        <protected>false</protected>\n"
            f"        <keyMaterial>{password}</keyMaterial>\n"
            "      </sharedKey>\n"
            "    </security>\n"
            "  </MSM>\n"
            "</WLANProfile>\n"
        )
        temp_path = ""
        try:
            with tempfile.NamedTemporaryFile("w", suffix=".xml", delete=False, encoding="utf-8") as handle:
                handle.write(profile_xml)
                temp_path = handle.name
            result = subprocess.run(
                ["netsh", "wlan", "add", "profile", f"filename={temp_path}", "user=current"],
                capture_output=True,
                text=True,
                timeout=8,
                check=False,
                **_windows_hidden_subprocess_kwargs(),
            )
            return result.returncode == 0 and self._windows_wifi_profile_is_compatible(ssid, password)
        except Exception:
            return False
        finally:
            if temp_path:
                try:
                    os.unlink(temp_path)
                except Exception:
                    pass

    def _start_windows_wifi_autojoin(self) -> None:
        if self._wifi_autojoin_inflight or os.name != "nt":
            return
        mode = int(getattr(self.config.connection, "connection_type", 0) or 0)
        if mode not in (2, 3, 4):
            return
        now = time.time()
        if now - self._last_wifi_autojoin_attempt_s < 8.0:
            return
        credential_candidates = self._wifi_credentials_candidates_for_mode(mode)
        ssid, password = credential_candidates[0]
        acceptable_ssids = {candidate_ssid for candidate_ssid, _candidate_password in credential_candidates}
        acceptable_ssids_normalized = {
            self._normalize_ssid(candidate_ssid)
            for candidate_ssid in acceptable_ssids
        }
        self._last_wifi_autojoin_attempt_s = now
        self._wifi_autojoin_inflight = True

        def _worker() -> None:
            message = ""
            ok = False
            try:
                current_ssid = self._windows_wifi_current_ssid()
                if self._normalize_ssid(current_ssid) in acceptable_ssids_normalized:
                    ok = True
                    message = f"Windows WiFi already on {current_ssid}"
                else:
                    selected_credentials: tuple[str, str] | None = None
                    for candidate_ssid, candidate_password in credential_candidates:
                        if self._windows_wifi_network_available(candidate_ssid):
                            selected_credentials = (candidate_ssid, candidate_password)
                            break
                    if selected_credentials is None:
                        visible_list = ", ".join(sorted(acceptable_ssids))
                        message = f"ESP32 WiFi SSID not visible yet ({visible_list})"
                    else:
                        ssid, password = selected_credentials
                        if not self._ensure_windows_wifi_profile(ssid, password):
                            message = f"Failed to prepare Windows WiFi profile for {ssid}"
                            self.wifi_autojoin_result.emit(False, message)
                            return
                        interface_name = self._windows_wifi_primary_interface_name()
                        connect_cmd = ["netsh", "wlan", "connect", f"name={ssid}", f"ssid={ssid}"]
                        if interface_name:
                            connect_cmd.append(f"interface={interface_name}")
                        result = subprocess.run(
                            connect_cmd,
                            capture_output=True,
                            text=True,
                            timeout=10,
                            check=False,
                            **_windows_hidden_subprocess_kwargs(),
                        )
                        time.sleep(2.5)
                        ok = self._ssid_matches_expected(self._windows_wifi_current_ssid(), [ssid])
                        if ok:
                            message = f"Windows WiFi connected to {ssid}"
                        else:
                            detail = (result.stdout or result.stderr or "connect failed").strip()
                            message = f"Windows WiFi auto-connect failed: {detail}"
            except Exception as exc:
                message = f"Windows WiFi auto-connect error: {exc}"
            self.wifi_autojoin_result.emit(ok, message)

        threading.Thread(target=_worker, name="sentry-v2-wifi-autojoin", daemon=True).start()

    def _on_wifi_autojoin_result(self, ok: bool, message: str) -> None:
        self._wifi_autojoin_inflight = False
        note = str(message or "").strip()
        if not note or note == self._last_wifi_autojoin_note:
            return
        self._last_wifi_autojoin_note = note
        if ok:
            self._log(note)
        elif "not visible yet" not in note.lower():
            self._log(note)

    def _connection_watchdog_tick(self) -> None:
        if self._closing or self._host_controls_hardware() or self._connection_busy:
            return
        mode = int(getattr(self.config.connection, "connection_type", 0) or 0)
        if mode not in (2, 3, 4):
            return
        now = time.time()
        current_ssid = self._windows_wifi_current_ssid() if os.name == "nt" else ""
        expected_credentials = self._wifi_credentials_candidates_for_mode(mode)
        expected_ssids = {ssid for ssid, _password in expected_credentials}
        expected_ssids_normalized = {
            self._normalize_ssid(ssid)
            for ssid in expected_ssids
        }
        on_esp32_wifi = self._normalize_ssid(current_ssid) in expected_ssids_normalized

        mode2_transport_alive = (
            mode == 2
            and self._comm.is_connected()
            and bool(getattr(self._comm, "_bus_ser", None) is not None)
        )

        if not on_esp32_wifi and not mode2_transport_alive:
            self._start_windows_wifi_autojoin()

        if mode == 3 and not self._comm.is_connected():
            if not on_esp32_wifi:
                return
            if now - self._last_wifi_link_refresh_s >= 10.0:
                self._last_wifi_link_refresh_s = now
                self._auto_connect_on_startup(0)
            return

        io_runtime = self._comm.get_io_runtime_snapshot()
        io_age = io_runtime.get("age_s")
        io_stale = io_age is None or float(io_age) > 4.0
        udp_ready = bool(getattr(self._comm, "_sock", None) is not None and getattr(self._comm, "_udp_target", None) is not None)

        if mode in (2, 3) and (not udp_ready or io_stale):
            if not on_esp32_wifi or self._wifi_runtime_refresh_inflight:
                return
            if now - self._last_wifi_link_refresh_s >= 10.0:
                self._last_wifi_link_refresh_s = now
                self._wifi_runtime_refresh_inflight = True
                self._queue_comm_task(
                    "refresh_wifi_runtime_link",
                    str(self.config.connection.udp_host or "192.168.4.1"),
                    int(self.config.connection.udp_port or 9000),
                    bool(self.config.pir_guard.pir_enabled),
                )

    def _collect_runtime_snapshot(self) -> dict:
        def _path_entry(path_obj: Path) -> dict:
            try:
                resolved = path_obj.resolve()
            except Exception:
                resolved = path_obj
            return {
                "path": self._portable_path_string(resolved),
                "absolute_path": str(resolved),
                "exists": resolved.exists(),
            }

        def _summarize_detection(det: object) -> Optional[dict]:
            if det is None:
                return None
            result = {
                "class_name": str(getattr(det, "class_name", "") or ""),
                "source": str(getattr(det, "source", "") or ""),
            }
            score = getattr(det, "score", None)
            if score is not None:
                try:
                    result["score"] = float(score)
                except Exception:
                    result["score"] = score
            bbox_keys = ("x", "y", "w", "h")
            if all(hasattr(det, key) for key in bbox_keys):
                result["bbox"] = {
                    "x": int(getattr(det, "x")),
                    "y": int(getattr(det, "y")),
                    "w": int(getattr(det, "w")),
                    "h": int(getattr(det, "h")),
                }
            return result

        def _summarize_tracked_target(target: object) -> dict:
            det = getattr(target, "det", None)
            raw_track_id = getattr(target, "target_id", None)
            if raw_track_id is None:
                raw_track_id = getattr(target, "track_id", None)
            if raw_track_id is None and det is not None:
                raw_track_id = getattr(det, "track_id", None)

            raw_score = getattr(target, "threat_score", None)
            if raw_score is None:
                raw_score = getattr(target, "score", None)

            return {
                "track_id": str(raw_track_id or ""),
                "score": float(raw_score or 0.0),
                "persistence": float(getattr(target, "persistence", 0.0) or 0.0),
                "heading_x": float(getattr(target, "heading_x", 0.0) or 0.0),
                "heading_y": float(getattr(target, "heading_y", 0.0) or 0.0),
                "detection": _summarize_detection(det),
            }

        def _recent_log_lines(limit: int = 20) -> list[str]:
            if not hasattr(self, "_log_text") or self._log_text is None:
                return []
            lines = [line.strip() for line in self._log_text.toPlainText().splitlines() if line.strip()]
            return lines[-limit:]

        raw_shape = None
        if self._last_raw_frame is not None:
            raw_shape = {
                "width": int(self._last_raw_frame.shape[1]),
                "height": int(self._last_raw_frame.shape[0]),
                "channels": int(self._last_raw_frame.shape[2]) if len(self._last_raw_frame.shape) > 2 else 1,
            }

        display_shape = None
        if self._last_display_frame is not None:
            display_shape = {
                "width": int(self._last_display_frame.shape[1]),
                "height": int(self._last_display_frame.shape[0]),
                "channels": int(self._last_display_frame.shape[2]) if len(self._last_display_frame.shape) > 2 else 1,
            }

        selected_model_path = str(self._combo_yolo_model.currentData() or "").strip() if hasattr(self, "_combo_yolo_model") else ""
        detector_model_path = str(getattr(self._detector, "_yolo_model_path", "") or "").strip()
        active_order = getattr(self.engine, "active_order", None)
        active_target = getattr(active_order, "target", None)
        active_detection = getattr(active_target, "det", None)
        servo_feedback = self._comm.get_servo_feedback_snapshot()
        io_runtime = self._comm.get_io_runtime_snapshot()
        bridge_caps = self._comm.get_bridge_caps_snapshot()

        payload = {
            "generated_at_local": time.strftime("%Y-%m-%d %H:%M:%S"),
            "generated_at_epoch_s": time.time(),
            "config": self.config.to_dict(),
            "engine_state": {
                "state": self.engine.state.name,
                "motion_enabled": bool(self.engine.is_motion_enabled()),
                "current_pan": float(self.engine.current_pan),
                "current_tilt": float(self.engine.current_tilt),
                "guard_pan": float(self.config.guard.guard_pan),
                "guard_tilt": float(self.config.guard.guard_tilt),
                "queue_length": len(getattr(self.engine, "_queue", [])),
                "queue_index": int(getattr(self.engine, "_queue_index", 0) or 0),
                "engage_phase": str(getattr(self.engine, "_engage_phase", "") or ""),
                "active_order": {
                    "target": _summarize_tracked_target(active_target) if active_target is not None else None,
                    "target_pan": float(getattr(active_order, "pan", 0.0) or 0.0) if active_order is not None else None,
                    "target_tilt": float(getattr(active_order, "tilt", 0.0) or 0.0) if active_order is not None else None,
                    "burst_count": int(self.config.engagement.burst_count) if active_order is not None else None,
                    "detection": _summarize_detection(active_detection),
                },
                "visible_targets": [_summarize_tracked_target(target) for target in list(getattr(self.engine, "last_targets", []))[:8]],
                "qualified_count": len(getattr(self.engine, "last_qualified", [])),
                "engagement_log_entries": len(getattr(self.engine, "engagement_log", [])),
                "last_reacquire_note": str(getattr(self.engine, "_last_reacquire_note", "") or ""),
                "active_no_fire_mask": str(getattr(self.engine, "_last_no_fire_mask_name", "") or ""),
                "loss_recovery_phase": str(getattr(self.engine, "_loss_recovery_phase", "") or ""),
            },
            "comm_telemetry": {
                "is_connected": bool(self._comm.is_connected()),
                "connection_status_label": str(self._lbl_conn_status.text()) if hasattr(self, "_lbl_conn_status") else "",
                "host_hardware_managed": bool(self._host_controls_hardware()),
                "bridge_caps": bridge_caps,
                "configured_mode_index": int(self.config.connection.connection_type),
                "configured_mode_label": SentryV2Comm.MODE_LABELS[int(self.config.connection.connection_type)] if 0 <= int(self.config.connection.connection_type) < len(SentryV2Comm.MODE_LABELS) else "Unknown",
                "mode_index": int(getattr(self._comm, "_mode", 0) or 0),
                "mode_label": SentryV2Comm.MODE_LABELS[int(getattr(self._comm, "_mode", 0) or 0)] if 0 <= int(getattr(self._comm, "_mode", 0) or 0) < len(SentryV2Comm.MODE_LABELS) else "Unknown",
                "trigger_mode_bb": bool(self._comm.trigger_mode_bb),
                "last_command": str(getattr(self._comm, "_last_cmd", "") or ""),
                "last_error": str(getattr(self._comm, "_last_error", "") or ""),
                "wifi_io_socket_active": bool(getattr(self._comm, "_sock", None) is not None),
                "wifi_io_target": str(getattr(self._comm, "_udp_target", None) or ""),
                "servo_feedback": servo_feedback,
                "io_runtime": io_runtime,
            },
            "camera_status": {
                "capture_open": bool(self._cap is not None and self._cap.isOpened()),
                "source_kind": str(self._local_source_kind or ""),
                "source_label": str(self._local_source_label or ""),
                "remembered_source": str(self._last_camera_source_text or ""),
                "requested_width": int(self._last_camera_width),
                "requested_height": int(self._last_camera_height),
                "selected_resolution": {
                    "width": int(self._selected_camera_dimensions()[0]),
                    "height": int(self._selected_camera_dimensions()[1]),
                } if hasattr(self, "_combo_cam_resolution") else None,
                "raw_frame": raw_shape,
                "display_frame": display_shape,
                "show_video_feed": bool(self._show_video_feed),
                "test_media_paused": bool(self._test_media_paused),
                "test_media_loop_enabled": bool(self._test_media_loop_enabled),
                "grab_fail_count": int(self._grab_fail_count),
                "black_frame_count": int(self._camera_black_frame_count),
                "partial_frame_count": int(self._camera_partial_frame_count),
                "camera_recovery_attempts": int(self._camera_recovery_attempts),
                "camera_recovery_in_progress": bool(self._camera_recovery_in_progress),
            },
            "yolo_status": {
                "status_label": str(self._lbl_yolo_status.text()) if hasattr(self, "_lbl_yolo_status") else "",
                "selected_model_name": str(self._combo_yolo_model.currentText()) if hasattr(self, "_combo_yolo_model") else "",
                "selected_model_path": self._portable_path_string(Path(selected_model_path)) if selected_model_path else "",
                "loaded_model_path": self._portable_path_string(Path(detector_model_path)) if detector_model_path else "",
                "detector_loaded": bool(getattr(self._detector, "_yolo_loaded", False)),
                "target_classes": [str(name) for name in getattr(self._detector, "_yolo_target_classes", [])],
                "allowed_classes": [str(name) for name in self.config.target_filter.allowed_classes],
                "confidence": float(self.config.detection_mode.yolo_confidence),
                "min_area": int(self.config.detection_mode.yolo_min_area),
            },
            "assistant_runtime": {
                "provider_available": bool(getattr(self, "_assistant_available", False)),
                "provider_status_label": self._assistant_model_status_text(),
                "installed_models": [str(model) for model in list(getattr(self, "_assistant_models", []) or [])],
                "selected_prompt_model": self._selected_ai_model_for_task("prompt"),
                "selected_prompt_installed": self._selected_ai_model_for_task("prompt") in set(getattr(self, "_assistant_models", []) or []),
                "selected_analysis_model": self._selected_ai_model_for_task("analysis"),
                "speech_supported": bool(self._human_voice_supported()),
                "human_voice_enabled": bool(getattr(self.config.sound, "human_voice_enabled", False)),
                "auto_speak": bool(getattr(self.config.ai_assistant, "auto_speak_responses", False)),
                "voice_status": self._assistant_voice_route_status()[0],
            },
            "external_file_references": {
                "settings_json": _path_entry(CANONICAL_SETTINGS_PATH),
                "legacy_settings_json": _path_entry(LEGACY_SMART_SENTRY_V3_SETTINGS_PATH if LEGACY_SMART_SENTRY_V3_SETTINGS_PATH.exists() else LEGACY_SENTRY_V2_SETTINGS_PATH),
                "custom_master_presets": _path_entry(self._custom_master_preset_path()),
                "prompted_target_library": _path_entry(self._resolved_prompted_library_path()),
                "snapshot_dir": _path_entry(SENTRY_V2_SNAPSHOT_DIR),
                "selected_yolo_model": _path_entry(Path(selected_model_path)) if selected_model_path else None,
                "candidate_yolo_model_dirs": [_path_entry(path_obj) for path_obj in self._candidate_yolo_model_dirs()],
            },
            "recent_log_lines": _recent_log_lines(),
        }
        return payload

    def _render_runtime_snapshot_markdown(self, payload: dict) -> str:
        engine_state = payload.get("engine_state", {})
        comm = payload.get("comm_telemetry", {})
        camera = payload.get("camera_status", {})
        yolo = payload.get("yolo_status", {})
        exported_files = payload.get("exported_files", {})
        active_order = engine_state.get("active_order", {}) or {}
        active_target = active_order.get("target") or {}
        external_refs = payload.get("external_file_references", {})
        recent_logs = payload.get("recent_log_lines", [])

        lines = [
            f"# {SMART_SENTRY_RELEASE_TITLE} Runtime Snapshot",
            "",
            f"- Generated: {payload.get('generated_at_local', '')}",
            f"- Engine state: {engine_state.get('state', '')}",
            f"- Connection: {comm.get('connection_status_label', '')}",
            f"- Camera: {camera.get('source_label', '') or camera.get('remembered_source', '')}",
            f"- YOLO: {yolo.get('status_label', '')}",
        ]

        if exported_files:
            lines.extend([
                "",
                "## Exported Files",
                "",
                f"- JSON: {exported_files.get('json', '')}",
                f"- Markdown: {exported_files.get('markdown', '')}",
            ])

        lines.extend([
            "",
            "## Engine",
            "",
            f"- Motion enabled: {engine_state.get('motion_enabled')}",
            f"- Current pan/tilt: {engine_state.get('current_pan')} / {engine_state.get('current_tilt')}",
            f"- Guard pan/tilt: {engine_state.get('guard_pan')} / {engine_state.get('guard_tilt')}",
            f"- Queue length/index: {engine_state.get('queue_length')} / {engine_state.get('queue_index')}",
            f"- Engage phase: {engine_state.get('engage_phase', '')}",
            f"- Visible targets: {len(engine_state.get('visible_targets', []))}",
            f"- Qualified count: {engine_state.get('qualified_count')}",
            f"- Active no-fire mask: {engine_state.get('active_no_fire_mask', '') or 'none'}",
            f"- Last reacquire note: {engine_state.get('last_reacquire_note', '') or 'none'}",
        ])

        lines.extend([
            "",
            "## Active Target",
            "",
            f"- Track ID: {active_target.get('track_id', '') or 'none'}",
            f"- Class: {((active_target.get('detection') or {}).get('class_name', '')) or 'none'}",
            f"- Score: {active_target.get('score', '') if active_target else 'none'}",
            f"- Aim pan/tilt: {active_order.get('target_pan', '')} / {active_order.get('target_tilt', '')}",
            f"- Burst count: {active_order.get('burst_count', '')}",
        ])

        lines.extend([
            "",
            "## Communications",
            "",
            f"- Connected: {comm.get('is_connected')}",
            f"- Host managed: {comm.get('host_hardware_managed')}",
            f"- Mode: {comm.get('mode_label', '')}",
            f"- Trigger mode: {'Projectile (ESP32 GPIO13 Servo)' if comm.get('trigger_mode_bb') else 'Water (MOSFET)'}",
            f"- Last command: {comm.get('last_command', '') or 'none'}",
            f"- Last error: {comm.get('last_error', '') or 'none'}",
        ])

        servo_feedback = comm.get("servo_feedback", {}) or {}
        io_runtime = comm.get("io_runtime", {}) or {}
        lines.extend([
            "",
            "## Telemetry",
            "",
            f"- Servo feedback age (s): {servo_feedback.get('age_s')}",
            f"- Servo feedback pan/tilt: {servo_feedback.get('pan_deg')} / {servo_feedback.get('tilt_deg')}",
            f"- IO runtime source: {io_runtime.get('source', '')}",
            f"- IO runtime age (s): {io_runtime.get('age_s')}",
            f"- Safety/mode: {io_runtime.get('safety')} / {io_runtime.get('mode')}",
            f"- Current fault: {io_runtime.get('current_fault')}",
            f"- Total current (mA): {io_runtime.get('total_mA')}",
        ])

        lines.extend([
            "",
            "## Camera",
            "",
            f"- Capture open: {camera.get('capture_open')}",
            f"- Source kind: {camera.get('source_kind', '')}",
            f"- Source label: {camera.get('source_label', '') or camera.get('remembered_source', '')}",
            f"- Requested resolution: {camera.get('requested_width')} x {camera.get('requested_height')}",
            f"- Raw frame: {camera.get('raw_frame')}",
            f"- Display frame: {camera.get('display_frame')}",
            f"- Blackout frame count: {camera.get('black_frame_count')}",
            f"- Recovery attempts/in progress: {camera.get('camera_recovery_attempts')} / {camera.get('camera_recovery_in_progress')}",
        ])

        lines.extend([
            "",
            "## YOLO",
            "",
            f"- Selected model: {yolo.get('selected_model_name', '')}",
            f"- Selected model path: {yolo.get('selected_model_path', '') or 'none'}",
            f"- Loaded model path: {yolo.get('loaded_model_path', '') or 'none'}",
            f"- Detector loaded: {yolo.get('detector_loaded')}",
            f"- Allowed classes: {', '.join(yolo.get('allowed_classes', [])) or 'all'}",
            f"- Confidence/min area: {yolo.get('confidence')} / {yolo.get('min_area')}",
        ])

        lines.extend([
            "",
            "## External Files",
            "",
        ])
        for key, value in external_refs.items():
            if value is None:
                lines.append(f"- {key}: none")
                continue
            if isinstance(value, list):
                joined = ", ".join(str(item.get("path", "")) for item in value)
                lines.append(f"- {key}: {joined}")
                continue
            lines.append(f"- {key}: {value.get('path', '')} (exists={value.get('exists')})")

        if recent_logs:
            lines.extend([
                "",
                "## Recent Log Lines",
                "",
                "```text",
                *recent_logs,
                "```",
            ])

        return "\n".join(lines) + "\n"

    def _export_runtime_snapshot(self) -> None:
        try:
            SENTRY_V2_SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
            payload = self._collect_runtime_snapshot()
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            json_path = SENTRY_V2_SNAPSHOT_DIR / f"sentry_v2_runtime_snapshot_{timestamp}.json"
            md_path = SENTRY_V2_SNAPSHOT_DIR / f"sentry_v2_runtime_snapshot_{timestamp}.md"
            payload["exported_files"] = {
                "json": self._portable_path_string(json_path),
                "markdown": self._portable_path_string(md_path),
            }
            markdown = self._render_runtime_snapshot_markdown(payload)
            json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
            md_path.write_text(markdown, encoding="utf-8")
            self._last_runtime_snapshot_json_path = json_path
            self._last_runtime_snapshot_markdown_path = md_path
            self._log(f"Runtime data exported: {self._portable_path_string(json_path)}")
            self._log(f"Runtime data summary: {self._portable_path_string(md_path)}")
        except Exception as exc:
            self._log(f"Runtime data export failed: {exc}")

    def _open_runtime_snapshot_folder(self) -> None:
        try:
            SENTRY_V2_SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
            latest_path = self._last_runtime_snapshot_json_path
            folder_path = SENTRY_V2_SNAPSHOT_DIR
            if latest_path is not None and latest_path.exists():
                folder_path = latest_path.parent
            if not QDesktopServices.openUrl(QUrl.fromLocalFile(str(folder_path))):
                raise RuntimeError(f"could not open folder: {folder_path}")
            if latest_path is not None and latest_path.exists():
                self._log(f"Opened runtime export folder: {self._portable_path_string(folder_path)} (latest: {self._portable_path_string(latest_path)})")
            else:
                self._log(f"Opened runtime export folder: {self._portable_path_string(folder_path)}")
        except Exception as exc:
            self._log(f"Open export folder failed: {exc}")

    def _export_serial_log(self) -> None:
        try:
            if not hasattr(self, "_log_text") or self._log_text is None:
                self._log("Serial log export failed: log panel is unavailable")
                return
            log_text = self._serialize_log_entries(include_filter=False)
            if not log_text.strip():
                self._log("Serial log export skipped: log panel is empty")
                return
            SENTRY_V2_LOG_EXPORT_DIR.mkdir(parents=True, exist_ok=True)
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            export_path = SENTRY_V2_LOG_EXPORT_DIR / f"sentry_v2_serial_log_{timestamp}.txt"
            header = [
                f"# {SMART_SENTRY_RELEASE_TITLE} Serial Log Export",
                f"# Exported: {time.strftime('%Y-%m-%d %H:%M:%S')}",
                "",
            ]
            export_path.write_text("\n".join(header) + log_text.rstrip() + "\n", encoding="utf-8")
            self._last_log_export_path = export_path
            self._log(f"Serial log exported: {self._portable_path_string(export_path)}")
        except Exception as exc:
            self._log(f"Serial log export failed: {exc}")

    def _open_serial_log_folder(self) -> None:
        try:
            SENTRY_V2_LOG_EXPORT_DIR.mkdir(parents=True, exist_ok=True)
            latest_path = self._last_log_export_path
            folder_path = SENTRY_V2_LOG_EXPORT_DIR
            if latest_path is not None and latest_path.exists():
                folder_path = latest_path.parent
            if not QDesktopServices.openUrl(QUrl.fromLocalFile(str(folder_path))):
                raise RuntimeError(f"could not open folder: {folder_path}")
            if latest_path is not None and latest_path.exists():
                self._log(
                    f"Opened serial log export folder: {self._portable_path_string(folder_path)} (latest: {self._portable_path_string(latest_path)})"
                )
            else:
                self._log(f"Opened serial log export folder: {self._portable_path_string(folder_path)}")
        except Exception as exc:
            self._log(f"Open serial log folder failed: {exc}")

    def _resolved_prompted_library_path(self) -> Path:
        configured = Path(str(self.config.prompted_library_path or CANONICAL_PROMPTED_TARGETS_RELATIVE_PATH))
        known_relative_prompted_paths = {
            Path(CANONICAL_PROMPTED_TARGETS_RELATIVE_PATH),
            Path("app/config/smart_sentry_v2_3_2_prompted_targets.json"),
            Path("app/config/smart_sentry_v2_3_1_prompted_targets.json"),
            Path("app/config/smart_sentry_v3_prompted_targets.json"),
            Path("app/config/sentry_v2_prompted_targets.json"),
        }
        if configured in known_relative_prompted_paths:
            for candidate in [
                CANONICAL_PROMPTED_TARGETS_PATH,
                SMART_SENTRY_V2_3_2_PROMPTED_TARGETS_PATH,
                SMART_SENTRY_V2_3_1_PROMPTED_TARGETS_PATH,
                LEGACY_SMART_SENTRY_V3_PROMPTED_TARGETS_PATH,
                LEGACY_SENTRY_V2_PROMPTED_TARGETS_PATH,
            ]:
                if candidate.exists():
                    return candidate.resolve()
        if configured.is_absolute():
            return configured
        return (self._repo_root_path() / configured).resolve()

    def _load_prompted_target_library(self) -> PromptedTargetLibrary:
        return PromptedTargetLibrary.load(str(self._resolved_prompted_library_path()))

    def _save_prompted_target_library(self) -> None:
        try:
            self._prompted_target_library.save(str(self._resolved_prompted_library_path()))
        except Exception as exc:
            self._log(f"Prompted target save failed: {exc}")

    def _resolved_face_library_path(self) -> Path:
        configured = Path(str(self.config.face_recognition.library_path or CANONICAL_FACE_LIBRARY_RELATIVE_PATH))
        if configured in {Path(CANONICAL_FACE_LIBRARY_RELATIVE_PATH), Path("app/config/smart_sentry_v2_3_2_faces.json")}:
            if CANONICAL_FACE_LIBRARY_PATH.exists():
                return CANONICAL_FACE_LIBRARY_PATH.resolve()
            if SMART_SENTRY_V2_3_2_FACE_LIBRARY_PATH.exists():
                return SMART_SENTRY_V2_3_2_FACE_LIBRARY_PATH.resolve()
        if configured.is_absolute():
            return configured
        return (self._repo_root_path() / configured).resolve()

    def _load_face_identity_library(self) -> FaceIdentityLibrary:
        return FaceIdentityLibrary.load(str(self._resolved_face_library_path()))

    def _save_face_identity_library(self) -> None:
        try:
            self._face_library.save(str(self._resolved_face_library_path()))
        except Exception as exc:
            self._log(f"Face library save failed: {exc}")

    def _selected_face_profile_id(self) -> Optional[str]:
        if not hasattr(self, "_face_profile_list"):
            return None
        item = self._face_profile_list.currentItem()
        if item is None:
            return None
        profile_id = str(item.data(Qt.UserRole) or "")
        return profile_id or None

    def _selected_face_profile(self):
        profile_id = self._selected_face_profile_id()
        if not profile_id:
            return None
        for profile in self._face_library.profiles:
            if str(profile.profile_id) == profile_id:
                return profile
        return None

    def _rebuild_face_profile_list(self) -> None:
        if not hasattr(self, "_face_profile_list"):
            return
        selected_id = self._selected_face_profile_id()
        self._face_profile_list.blockSignals(True)
        self._face_profile_list.clear()
        for profile in self._face_library.profiles:
            suffix = "friendly" if bool(profile.friendly) else "watch"
            item = QListWidgetItem(f"{profile.name} ({len(profile.embeddings)} samples, {suffix})")
            item.setData(Qt.UserRole, str(profile.profile_id))
            self._face_profile_list.addItem(item)
            if selected_id and str(profile.profile_id) == selected_id:
                item.setSelected(True)
                self._face_profile_list.setCurrentItem(item)
        self._face_profile_list.blockSignals(False)
        self._on_face_profile_selected()
        self._update_face_runtime_status()

    def _on_face_profile_selected(self) -> None:
        profile = self._selected_face_profile()
        if not hasattr(self, "_edit_face_profile_name"):
            return
        if profile is None:
            self._edit_face_profile_name.clear()
            self._edit_face_profile_notes.clear()
            self._chk_face_profile_friendly.setChecked(True)
            self._chk_face_profile_announce.setChecked(True)
            self._chk_face_profile_gesture.setChecked(True)
            return
        self._edit_face_profile_name.setText(str(profile.name))
        self._edit_face_profile_notes.setText(str(profile.notes or ""))
        self._chk_face_profile_friendly.setChecked(bool(profile.friendly))
        self._chk_face_profile_announce.setChecked(bool(profile.announce_name))
        self._chk_face_profile_gesture.setChecked(bool(profile.cute_gesture))

    def _update_face_runtime_status(self) -> None:
        if not hasattr(self, "_lbl_face_runtime_status"):
            return
        match_text = "none"
        if self._last_face_matches:
            top = max(self._last_face_matches, key=lambda item: float(item.confidence))
            match_text = f"{top.name} ({top.confidence:.2f})"
        status_text = (
            f"Known profiles: {len(self._face_library.profiles)} | last recognized: {match_text} | file: {self._portable_path_string(self._resolved_face_library_path())}"
        )
        if status_text == self._last_face_runtime_status_text:
            return
        self._last_face_runtime_status_text = status_text
        self._lbl_face_runtime_status.setText(status_text)

    def _on_face_runtime_settings_changed(self) -> None:
        cfg = self.config.face_recognition
        cfg.enabled = bool(self._chk_face_enabled.isChecked())
        cfg.recognition_threshold = float(self._spin_face_threshold.value())
        cfg.min_face_size_px = int(self._spin_face_min_size.value())
        cfg.suppress_known_faces_from_engagement = bool(self._chk_face_suppress.isChecked())
        cfg.announce_known_faces = bool(self._chk_face_announce.isChecked())
        cfg.cute_gesture_enabled = bool(self._chk_face_gesture.isChecked())
        cfg.library_path = self._portable_path_string(self._resolved_face_library_path())
        self._save_config_quietly()
        self._update_face_runtime_status()

    def _register_face_from_images(self) -> None:
        name = str(getattr(self, "_edit_face_profile_name", QLineEdit()).text()).strip()
        if not name:
            self._log("Face registration aborted: enter a profile name first")
            return
        paths, _selected_filter = QFileDialog.getOpenFileNames(
            self,
            "Select Face Images",
            str(self._repo_root_path()),
            "Images (*.png *.jpg *.jpeg *.bmp *.webp)",
        )
        if not paths:
            return
        vectors = self._face_runtime.build_embeddings_from_images(paths, min_face_size_px=int(self.config.face_recognition.min_face_size_px))
        if not vectors:
            self._log(f"Face registration failed for {name}: no usable face found in selected images")
            return
        profile = self._face_library.upsert_profile(
            name,
            vectors,
            friendly=bool(self._chk_face_profile_friendly.isChecked()),
            announce_name=bool(self._chk_face_profile_announce.isChecked()),
            cute_gesture=bool(self._chk_face_profile_gesture.isChecked()),
            notes=str(self._edit_face_profile_notes.text().strip()),
        )
        if profile is None:
            self._log(f"Face registration failed for {name}")
            return
        self._face_runtime.refresh_library(self._face_library)
        self._save_face_identity_library()
        self._save_config_quietly()
        self._rebuild_face_profile_list()
        self._log(f"Face profile updated: {profile.name} (+{len(vectors)} image sample(s))")

    def _register_face_from_live_frame(self) -> None:
        name = str(getattr(self, "_edit_face_profile_name", QLineEdit()).text()).strip()
        if not name:
            self._log("Live face registration aborted: enter a profile name first")
            return
        frame = getattr(self, "_last_raw_frame", None)
        if frame is None or getattr(frame, "size", 0) == 0:
            self._log("Live face registration unavailable: no camera frame captured yet")
            return
        vector = self._face_runtime.extract_primary_embedding(frame, min_face_size_px=int(self.config.face_recognition.min_face_size_px))
        if vector is None:
            self._log(f"Live face registration failed for {name}: no clear face found in the current frame")
            return
        profile = self._face_library.upsert_profile(
            name,
            [vector],
            friendly=bool(self._chk_face_profile_friendly.isChecked()),
            announce_name=bool(self._chk_face_profile_announce.isChecked()),
            cute_gesture=bool(self._chk_face_profile_gesture.isChecked()),
            notes=str(self._edit_face_profile_notes.text().strip()),
        )
        if profile is None:
            self._log(f"Live face registration failed for {name}")
            return
        self._face_runtime.refresh_library(self._face_library)
        self._save_face_identity_library()
        self._save_config_quietly()
        self._rebuild_face_profile_list()
        self._log(f"Live face registered: {profile.name}")

    def _remove_selected_face_profile(self) -> None:
        profile = self._selected_face_profile()
        if profile is None:
            self._log("Face removal skipped: no profile selected")
            return
        removed = self._face_library.remove_profile(str(profile.profile_id))
        if not removed:
            self._log(f"Face removal failed: {profile.name}")
            return
        self._face_runtime.refresh_library(self._face_library)
        self._save_face_identity_library()
        self._rebuild_face_profile_list()
        self._save_config_quietly()
        self._log(f"Face profile removed: {profile.name}")

    def _run_face_recognition_test(self) -> None:
        frame = getattr(self, "_last_raw_frame", None)
        if frame is None or getattr(frame, "size", 0) == 0:
            self._log("Face test unavailable: no frame available")
            return
        matches = self._face_runtime.match_known_faces(
            frame,
            min_face_size_px=int(self.config.face_recognition.min_face_size_px),
            threshold=float(self.config.face_recognition.recognition_threshold),
        )
        self._last_face_matches = list(matches)
        self._update_face_runtime_status()
        if not matches:
            self._log("Face test complete: no known face matched the current frame")
            return
        summary = ", ".join(f"{match.name} {match.confidence:.2f}" for match in matches[:4])
        self._log(f"Face test matched: {summary}")

    def _face_person_boxes(self, objects: List[DetectedObject]) -> Optional[List[Tuple[int, int, int, int]]]:
        person_boxes = [tuple(det.bbox) for det in objects if str(det.class_name or "").strip().lower() == "person"]
        return person_boxes or None

    def _face_match_refresh_interval_s(self, frame: np.ndarray) -> float:
        height, width = frame.shape[:2]
        pixels = int(height * width)
        interval = 0.85
        if pixels >= (1280 * 720):
            interval = 1.15
        if pixels >= (1920 * 1080):
            interval = 1.65
        if bool(getattr(self, "_detector_worker_busy", False)):
            interval = max(interval, 2.0)
        if bool(getattr(self.config, "prompted_targets_enabled", False)):
            interval += 0.15
        return interval

    def _face_person_boxes_similar(
        self,
        current: List[Tuple[int, int, int, int]],
        previous: List[Tuple[int, int, int, int]],
    ) -> bool:
        if len(current) != len(previous):
            return False
        if not current:
            return True
        current_sorted = sorted(current)
        previous_sorted = sorted(previous)
        return all(self._bbox_iou(a, b) >= 0.5 for a, b in zip(current_sorted, previous_sorted))

    @staticmethod
    def _bbox_iou(a: Tuple[int, int, int, int], b: Tuple[int, int, int, int]) -> float:
        ax, ay, aw, ah = a
        bx, by, bw, bh = b
        ax2, ay2 = ax + aw, ay + ah
        bx2, by2 = bx + bw, by + bh
        ix1 = max(ax, bx)
        iy1 = max(ay, by)
        ix2 = min(ax2, bx2)
        iy2 = min(ay2, by2)
        iw = max(0, ix2 - ix1)
        ih = max(0, iy2 - iy1)
        inter = iw * ih
        if inter <= 0:
            return 0.0
        union = max(1, (aw * ah) + (bw * bh) - inter)
        return inter / union

    def _annotate_objects_with_face_matches(
        self,
        objects: List[DetectedObject],
        matches: List[FaceMatchResult],
    ) -> List[DetectedObject]:
        annotated = list(objects)
        for match in matches:
            best_det = None
            best_score = 0.0
            for det in annotated:
                score = self._bbox_iou(tuple(det.bbox), tuple(match.bbox))
                if score > best_score:
                    best_det = det
                    best_score = score
            if best_det is None or best_score < 0.05:
                continue
            best_det.identity_label = str(match.name)
            best_det.identity_confidence = float(match.confidence)
            best_det.identity_profile_id = str(match.profile_id)
            best_det.friendly_identity = bool(match.friendly)
        filtered: List[DetectedObject] = []
        for det in annotated:
            is_suppressed = bool(
                det.identity_label
                and det.friendly_identity
                and self.config.face_recognition.suppress_known_faces_from_engagement
            )
            if not is_suppressed:
                filtered.append(det)
        return filtered

    def _apply_face_identity_to_objects(self, frame: np.ndarray, objects: List[DetectedObject], now: float) -> Tuple[List[DetectedObject], List[FaceMatchResult]]:
        if not bool(self.config.face_recognition.enabled) or not self._face_library.profiles:
            self._last_face_match_eval_s = 0.0
            self._last_face_person_boxes = []
            return list(objects), []
        person_boxes = list(self._face_person_boxes(objects) or [])
        if not person_boxes:
            self._last_face_match_eval_s = now
            self._last_face_person_boxes = []
            return list(objects), []

        refresh_interval_s = self._face_match_refresh_interval_s(frame)
        last_eval_s = float(getattr(self, "_last_face_match_eval_s", 0.0) or 0.0)
        elapsed_s = now - last_eval_s if last_eval_s > 0.0 else refresh_interval_s
        box_layout_changed = not self._face_person_boxes_similar(
            person_boxes,
            list(getattr(self, "_last_face_person_boxes", []) or []),
        )
        should_refresh = (
            not self._last_face_matches
            or elapsed_s >= refresh_interval_s
            or (box_layout_changed and elapsed_s >= 0.45)
        )

        if should_refresh:
            matches = self._face_runtime.match_known_faces(
                frame,
                min_face_size_px=int(self.config.face_recognition.min_face_size_px),
                person_boxes=person_boxes,
                threshold=float(self.config.face_recognition.recognition_threshold),
            )
            self._last_face_match_eval_s = now
            self._last_face_person_boxes = list(person_boxes)
        else:
            matches = list(getattr(self, "_last_face_matches", []) or [])

        filtered = self._annotate_objects_with_face_matches(objects, matches)
        best_match = max(matches, key=lambda item: float(item.confidence), default=None)
        if should_refresh and best_match is not None:
            self._maybe_announce_face_match(best_match, now)
            self._maybe_run_friendly_identity_gesture(best_match, now)
        return filtered, matches

    def _maybe_announce_face_match(self, match: FaceMatchResult, now: float) -> None:
        if not bool(self.config.face_recognition.announce_known_faces) or not bool(match.announce_name):
            return
        key = str(match.profile_id or match.name).strip().lower()
        if not key:
            return
        last_at = float(self._last_announced_identity_at.get(key, 0.0) or 0.0)
        cooldown_s = float(getattr(self.config.sound, "name_announce_cooldown_s", 18.0) or 18.0)
        if now - last_at < cooldown_s:
            return
        self._last_announced_identity_at[key] = now
        if bool(getattr(self.config.sound, "human_voice_enabled", False)):
            phrase = f"Hello {match.name}." if bool(match.friendly) else f"Recognized {match.name}."
            self._speak_human_phrase(phrase)
        if bool(getattr(self.config.sound, "robot_voice_enabled", False)) and not self._buzzer_suppressed_for_human_voice():
            self._sound_engine.note_identity_recognized(match.name, friendly=bool(match.friendly))
        self._log(f"Recognized face: {match.name} ({match.confidence:.2f})")

    def _maybe_run_friendly_identity_gesture(self, match: FaceMatchResult, now: float) -> None:
        if not bool(match.friendly and match.cute_gesture):
            return
        if not bool(self.config.face_recognition.cute_gesture_enabled):
            return
        if self.engine.state == SentryV2State.ENGAGING:
            return
        key = str(match.profile_id or match.name).strip().lower()
        last_at = float(self._last_gesture_identity_at.get(key, 0.0) or 0.0)
        cooldown_s = float(getattr(self.config.face_recognition, "gesture_cooldown_s", 30.0) or 30.0)
        if now - last_at < cooldown_s:
            return
        self._last_gesture_identity_at[key] = now
        pan = float(self.engine.current_pan)
        tilt = float(self.engine.current_tilt)
        greet_tilt = min(float(self.config.guard.tilt_max), max(float(self.config.guard.tilt_min), tilt + 3.0))
        self._manual_move_priority_until = max(float(getattr(self, "_manual_move_priority_until", 0.0) or 0.0), now + 1.4)
        if not self._host_controls_hardware():
            self._queue_move_command(pan, greet_tilt, move_time_ms=220, manual_override=True)
            QTimer.singleShot(320, lambda p=pan, t=tilt: self._queue_move_command(p, t, move_time_ms=260, manual_override=True))
        self._log(f"Friendly greeting: {match.name}")

    def _draw_face_identity_overlays(self, frame: np.ndarray, matches: List[FaceMatchResult]) -> None:
        for match in matches:
            x, y, w, h = [int(v) for v in match.bbox]
            color = (90, 230, 120) if bool(match.friendly) else (255, 210, 80)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2, cv2.LINE_AA)
            label = f"{match.name} {match.confidence:.2f}"
            ty = max(18, y - 8)
            cv2.putText(frame, label, (x, ty), cv2.FONT_HERSHEY_DUPLEX, 0.48, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(frame, label, (x, ty), cv2.FONT_HERSHEY_DUPLEX, 0.48, color, 1, cv2.LINE_AA)

    def _manual_shortcut_definitions(self) -> List[Tuple[str, str, Callable[[], None], str]]:
        if not bool(getattr(self.config.shortcuts, "manual_controls_enabled", False)):
            return []
        return [
            ("Manual pan left", "Ctrl+Shift+Left", lambda: self._manual_move(-1, 0), "Nudge the turret left"),
            ("Manual pan right", "Ctrl+Shift+Right", lambda: self._manual_move(1, 0), "Nudge the turret right"),
            ("Manual tilt up", "Ctrl+Shift+Up", lambda: self._manual_move(0, 1), "Nudge the turret up"),
            ("Manual tilt down", "Ctrl+Shift+Down", lambda: self._manual_move(0, -1), "Nudge the turret down"),
        ]

    def _shortcut_definitions(self) -> List[Tuple[str, str, Callable[[], None], str]]:
        definitions = [
            ("Quick keys", "Ctrl+Alt+Q", self._open_shortcut_quick_view, "Open the shortcut reference"),
            ("Enable / disable sentry", "Ctrl+Alt+E", lambda: self._chk_enable.toggle(), "Toggle Smart Sentry runtime"),
            ("Toggle connection", "Ctrl+Alt+C", self._toggle_connection, "Connect or disconnect the controller link"),
            ("Open / close camera", "Ctrl+Alt+O", self._toggle_camera, "Open or close the active camera source"),
            ("Show / hide video", "Ctrl+Alt+V", lambda: self._chk_show_video.toggle(), "Toggle the preview feed"),
            ("Go home", "Ctrl+Alt+W", self._on_home_clicked, "Move to the configured home position"),
            ("Go rest", "Ctrl+Alt+R", self._on_rest_clicked, "Move to the configured rest position"),
            ("Save settings", "Ctrl+Alt+S", self._save_config, "Write current settings to disk"),
            ("Previous tab", "Ctrl+Alt+Left", self._select_previous_settings_tab, "Move to the previous settings tab"),
            ("Next tab", "Ctrl+Alt+Right", self._select_next_settings_tab, "Move to the next settings tab"),
            ("Toggle safety", "Ctrl+Alt+1", lambda: self._btn_safety.toggle(), "Arm or lock safety"),
            ("Toggle LED", "Ctrl+Alt+2", lambda: self._btn_led.toggle(), "Toggle LED output"),
            ("Toggle laser", "Ctrl+Alt+3", lambda: self._btn_laser.toggle(), "Toggle laser output"),
            ("Toggle ACC", "Ctrl+Alt+4", lambda: self._btn_acc.toggle(), "Toggle ACC output"),
            ("Toggle auto lighting", "Ctrl+Alt+L", lambda: self._chk_auto_lighting.toggle() if hasattr(self, "_chk_auto_lighting") else None, "Toggle automatic LED brightness control"),
            ("Zoom UI in", "Ctrl+Alt+Plus", lambda: self._adjust_panel_zoom(1), "Increase panel zoom"),
            ("Zoom UI out", "Ctrl+Alt+Minus", lambda: self._adjust_panel_zoom(-1), "Decrease panel zoom"),
        ]
        definitions.extend(self._manual_shortcut_definitions())
        return definitions

    def _shortcut_display_lines(self) -> List[str]:
        runtime_suffix = "" if bool(self.config.shortcuts.enabled) else " [shortcut runtime disabled]"
        manual_suffix = "" if self._manual_keyboard_shortcuts_enabled() else " [manual movement/fire disabled]"
        return [
            f"Ctrl+Alt+Q - Quick keys{runtime_suffix}",
            f"Ctrl+Alt+E - Enable / disable sentry{runtime_suffix}",
            f"Ctrl+Alt+C - Toggle connection{runtime_suffix}",
            f"Ctrl+Alt+O - Open / close camera{runtime_suffix}",
            f"Ctrl+Alt+V - Show / hide video{runtime_suffix}",
            f"Ctrl+Alt+W - Go home{runtime_suffix}",
            f"Ctrl+Alt+R - Go rest{runtime_suffix}",
            f"Ctrl+Alt+S - Save settings{runtime_suffix}",
            f"Ctrl+Alt+Left - Previous tab{runtime_suffix}",
            f"Ctrl+Alt+Right - Next tab{runtime_suffix}",
            f"Ctrl+Alt+1 - Toggle safety{runtime_suffix}",
            f"Ctrl+Alt+2 - Toggle LED{runtime_suffix}",
            f"Ctrl+Alt+3 - Toggle laser{runtime_suffix}",
            f"Ctrl+Alt+4 - Toggle ACC{runtime_suffix}",
            f"Ctrl+Alt+Plus - Zoom UI in{runtime_suffix}",
            f"Ctrl+Alt+Minus - Zoom UI out{runtime_suffix}",
            f"Ctrl+Shift+Left - Manual pan left{manual_suffix}",
            f"Ctrl+Shift+Right - Manual pan right{manual_suffix}",
            f"Ctrl+Shift+Up - Manual tilt up{manual_suffix}",
            f"Ctrl+Shift+Down - Manual tilt down{manual_suffix}",
            f"A - Manual pan left{manual_suffix}",
            f"D - Manual pan right{manual_suffix}",
            f"W - Manual tilt up{manual_suffix}",
            f"S - Manual tilt down{manual_suffix}",
            f"Space - Manual fire{manual_suffix}",
        ]

    def _clear_shortcuts(self) -> None:
        self._release_manual_keyboard_fire()
        for shortcut in list(getattr(self, "_shortcut_bindings", [])):
            try:
                shortcut.setEnabled(False)
                shortcut.disconnect()
                shortcut.deleteLater()
            except Exception:
                pass
        self._shortcut_bindings = []

    def _install_global_shortcuts(self) -> None:
        self._clear_shortcuts()
        if not bool(self.config.shortcuts.enabled):
            self._update_shortcut_labels()
            return
        bindings: List[QShortcut] = []
        for _label, sequence, handler, _description in self._shortcut_definitions():
            shortcut = QShortcut(QKeySequence(sequence), self)
            shortcut.setContext(Qt.WindowShortcut)
            shortcut.activated.connect(handler)
            bindings.append(shortcut)
        self._shortcut_bindings = bindings
        self._update_shortcut_labels()

    def _update_shortcut_labels(self) -> None:
        lines = self._shortcut_display_lines()
        base_count = 16 if bool(self.config.shortcuts.enabled) else 0
        manual_count = 9 if self._manual_keyboard_shortcuts_enabled() else 0
        summary = (
            f"Shortcuts: {base_count + manual_count} active commands | runtime: {'enabled' if self.config.shortcuts.enabled else 'disabled'} | "
            f"manual movement/fire: {'enabled' if getattr(self.config.shortcuts, 'manual_controls_enabled', False) else 'disabled'}"
        )
        if hasattr(self, "_lbl_shortcut_summary"):
            self._lbl_shortcut_summary.setText(summary)
        if hasattr(self, "_lbl_shortcut_keys"):
            self._lbl_shortcut_keys.setText("\n".join(lines))

    def _on_shortcuts_enabled_changed(self) -> None:
        self.config.shortcuts.enabled = bool(self._chk_shortcuts_enabled.isChecked())
        self.config.shortcuts.quick_view_doc_path = self._portable_path_string(SMART_SENTRY_SHORTCUT_KEYS_DOC_PATH)
        self._install_global_shortcuts()
        self._save_config_quietly()

    def _on_manual_shortcuts_enabled_changed(self) -> None:
        self.config.shortcuts.manual_controls_enabled = bool(self._chk_manual_keyboard_enabled.isChecked())
        self.config.shortcuts.quick_view_doc_path = self._portable_path_string(SMART_SENTRY_SHORTCUT_KEYS_DOC_PATH)
        if not self.config.shortcuts.manual_controls_enabled:
            self._release_manual_keyboard_fire()
        self._install_global_shortcuts()
        self._save_config_quietly()

    def _open_shortcut_quick_view(self) -> None:
        path = SMART_SENTRY_SHORTCUT_KEYS_DOC_PATH
        if not path.exists():
            self._log(f"Shortcut reference missing: {self._portable_path_string(path)}")
            return
        if not QDesktopServices.openUrl(QUrl.fromLocalFile(str(path))):
            self._log(f"Shortcut reference open failed: {self._portable_path_string(path)}")
            return
        self._log(f"Shortcut reference opened: {self._portable_path_string(path)}")

    def _on_ai_assistant_settings_changed(self) -> None:
        if not hasattr(self, "_chk_ai_enabled") or not hasattr(self, "_combo_ai_mode"):
            return
        cfg = self.config.ai_assistant
        cfg.enabled = bool(self._chk_ai_enabled.isChecked())
        cfg.mode = str(self._combo_ai_mode.currentData() or "guided_tuning")
        cfg.endpoint_url = str(getattr(self, "_edit_ai_endpoint", QLineEdit()).text()).strip() or "http://localhost:11434"
        cfg.preferred_model_tier = self._current_ai_model_tier()
        cfg.model = self._current_ai_model(analyst=False)
        cfg.analyst_model = self._current_ai_model(analyst=True)
        cfg.allow_mode_switch = bool(self._chk_ai_allow_modes.isChecked())
        cfg.allow_setting_drafts = bool(self._chk_ai_allow_tuning.isChecked())
        cfg.allow_runtime_analysis = bool(self._chk_ai_allow_analysis.isChecked())
        cfg.allow_action_execution = bool(getattr(self, "_chk_ai_allow_actions", None) and self._chk_ai_allow_actions.isChecked())
        cfg.include_recent_logs = bool(getattr(self, "_chk_ai_include_logs", None) and self._chk_ai_include_logs.isChecked())
        cfg.auto_speak_responses = bool(getattr(self, "_chk_ai_auto_speak", None) and self._chk_ai_auto_speak.isChecked())
        self._update_ai_runtime_snapshot_view()
        self._save_config_quietly()

    def _create_ai_service(self) -> LocalAssistantService:
        cfg = self.config.ai_assistant
        client = OllamaClient(
            host=str(getattr(cfg, "endpoint_url", "http://localhost:11434") or "http://localhost:11434"),
            timeout_s=float(getattr(cfg, "request_timeout_s", 45.0) or 45.0),
        )
        return LocalAssistantService(client=client)

    def _sync_ai_model_combo_entries(self, models: List[str]) -> None:
        fast_current = str(getattr(self.config.ai_assistant, "model", "llama3.2:latest") or "llama3.2:latest")
        analyst_current = str(getattr(self.config.ai_assistant, "analyst_model", "gpt-oss:20b") or "gpt-oss:20b")
        shared = []
        for item in [fast_current, analyst_current, *[str(model) for model in models]]:
            cleaned = str(item or "").strip()
            if cleaned and cleaned not in shared:
                shared.append(cleaned)
        for combo, current in ((getattr(self, "_combo_ai_model", None), fast_current), (getattr(self, "_combo_ai_analyst_model", None), analyst_current)):
            if combo is None:
                continue
            combo.blockSignals(True)
            combo.clear()
            combo.addItems(shared)
            combo.setEditText(current)
            combo.blockSignals(False)

    def _current_ai_model(self, *, analyst: bool) -> str:
        combo = getattr(self, "_combo_ai_analyst_model", None) if analyst else getattr(self, "_combo_ai_model", None)
        if combo is not None:
            value = str(combo.currentText() or "").strip()
            if value:
                return value
        if analyst:
            return str(getattr(self.config.ai_assistant, "analyst_model", "gpt-oss:20b") or "gpt-oss:20b")
        return str(getattr(self.config.ai_assistant, "model", "llama3.2:latest") or "llama3.2:latest")

    def _current_ai_model_tier(self) -> str:
        if getattr(self, "_btn_ai_use_analyst_model", None) and self._btn_ai_use_analyst_model.isChecked():
            return "analyst"
        return "fast"

    def _set_ai_model_tier(self, tier: str, *, persist: bool = True) -> None:
        resolved = "analyst" if str(tier or "").strip().lower() == "analyst" else "fast"
        if getattr(self, "_btn_ai_use_fast_model", None) is not None:
            self._btn_ai_use_fast_model.blockSignals(True)
            self._btn_ai_use_fast_model.setChecked(resolved == "fast")
            self._btn_ai_use_fast_model.blockSignals(False)
        if getattr(self, "_btn_ai_use_analyst_model", None) is not None:
            self._btn_ai_use_analyst_model.blockSignals(True)
            self._btn_ai_use_analyst_model.setChecked(resolved == "analyst")
            self._btn_ai_use_analyst_model.blockSignals(False)
        if hasattr(self, "_lbl_ai_provider_status"):
            selected_model = self._current_ai_model(analyst=(resolved == "analyst"))
            self._lbl_ai_provider_status.setText(f"Selected {resolved} model tier: {selected_model}")
        if persist:
            self._on_ai_assistant_settings_changed()

    def _selected_ai_model_for_task(self, task_kind: str) -> str:
        if task_kind in ("analysis", "recommendations"):
            return self._current_ai_model(analyst=(self._current_ai_model_tier() != "fast"))
        if self._current_ai_model_tier() == "analyst":
            return self._current_ai_model(analyst=True)
        return self._current_ai_model(analyst=False)

    def _assistant_voice_route_status(self) -> tuple[str, bool]:
        auto_speak = bool(getattr(self.config.ai_assistant, "auto_speak_responses", False))
        human_voice_enabled = bool(getattr(self.config.sound, "human_voice_enabled", False))
        speech_supported = bool(self._human_voice_supported())
        if not auto_speak:
            return "auto-speak off", False
        if not speech_supported:
            return "speech backend unavailable", False
        if not human_voice_enabled:
            return "human voice off", False
        return "spoken replies ready", True

    def _assistant_model_status_text(self) -> str:
        prompt_model = self._selected_ai_model_for_task("prompt")
        available_models = set(getattr(self, "_assistant_models", []) or [])
        provider_available = bool(getattr(self, "_assistant_available", False))
        if not provider_available:
            return f"Ollama unavailable. Replies will fall back to deterministic guidance. Selected model: {prompt_model}"
        if available_models and prompt_model not in available_models:
            return f"Ollama reachable, but selected model {prompt_model} is not installed locally."
        return f"Ollama ready. Selected prompt model: {prompt_model}"

    def _update_ai_runtime_snapshot_view(self) -> None:
        if hasattr(self, "_lbl_ai_runtime_snapshot"):
            self._lbl_ai_runtime_snapshot.setText(self._assistant_runtime_snapshot())

    def _focus_ai_workspace(self, task_kind: str) -> None:
        tabs = getattr(self, "_tabs_ai_workspace", None)
        if tabs is None:
            return
        if task_kind in ("analysis", "recommendations") and hasattr(self, "_ai_runtime_page"):
            tabs.setCurrentWidget(self._ai_runtime_page)
            return
        if hasattr(self, "_ai_assistant_page"):
            tabs.setCurrentWidget(self._ai_assistant_page)

    def _refresh_ai_provider_status(self) -> None:
        self._on_ai_assistant_settings_changed()
        if self._assistant_models_loading:
            return
        self._assistant_models_loading = True
        if hasattr(self, "_lbl_ai_provider_status"):
            self._lbl_ai_provider_status.setText("Checking Ollama endpoint and installed models...")

        endpoint = str(getattr(self.config.ai_assistant, "endpoint_url", "http://localhost:11434") or "http://localhost:11434")

        def _worker() -> None:
            try:
                service = self._create_ai_service()
                models = service.list_models()
                message = f"Ollama ready at {endpoint}. {len(models)} model(s) detected."
                self.assistant_models_ready.emit(True, models, message)
            except Exception as exc:
                self.assistant_models_ready.emit(False, [], f"Ollama unavailable at {endpoint}: {exc}")

        threading.Thread(target=_worker, name="sentry-v2-ai-models", daemon=True).start()

    def _on_ai_assistant_models_ready(self, ok: bool, models: object, message: str) -> None:
        self._assistant_models_loading = False
        self._assistant_available = bool(ok)
        self._assistant_models = [str(item) for item in (models or []) if str(item).strip()]
        self._assistant_last_error = "" if ok else str(message or "")
        self._sync_ai_model_combo_entries(self._assistant_models)
        if hasattr(self, "_lbl_ai_provider_status"):
            voice_status, _voice_ready = self._assistant_voice_route_status()
            provider_text = str(message or ("Ollama ready" if ok else "Ollama unavailable"))
            self._lbl_ai_provider_status.setText(f"{provider_text} | voice: {voice_status}")

    def _assistant_runtime_snapshot(self) -> str:
        visible_targets = len(getattr(self, "_last_detected_objects", []) or [])
        known_faces = ", ".join(f"{match.name} {match.confidence:.2f}" for match in self._last_face_matches[:3]) or "none"
        voice_status, _voice_ready = self._assistant_voice_route_status()
        return (
            f"State: {self.engine.state.name} | sentry: {'enabled' if self._chk_enable.isChecked() else 'disabled'} | "
            f"mode: {self._assistant_detection_mode_name()} ({self._combo_detection_mode.currentIndex()}) | targets: {visible_targets} | "
            f"faces: {known_faces} | face recognition: {'on' if self.config.face_recognition.enabled else 'off'} | "
            f"shortcuts: {'on' if self.config.shortcuts.enabled else 'off'} | connection: {self._connection_status_level} | "
            f"camera: {'open' if self._has_local_source() else 'closed'} | human voice: {'on' if self.config.sound.human_voice_enabled else 'off'} ({self._assistant_human_voice_style_key()}) | "
            f"ai model: {self._selected_ai_model_for_task('prompt')} | ai voice: {voice_status}"
        )

    def _assistant_set_busy(self, busy: bool, note: str = "") -> None:
        self._assistant_busy = bool(busy)
        if hasattr(self, "_lbl_ai_provider_status") and note:
            self._lbl_ai_provider_status.setText(note)

    def _start_ai_background_task(self, task_kind: str, prompt: str = "") -> None:
        if self._assistant_busy:
            self._append_ai_output("Assistant request already in progress. Wait for the current local response first.", task_kind=task_kind)
            return
        if not bool(self.config.ai_assistant.enabled):
            self._append_ai_output("Assistant is disabled.", task_kind=task_kind)
            return
        self._on_ai_assistant_settings_changed()
        self._focus_ai_workspace(task_kind)
        snapshot = self._collect_runtime_snapshot()
        self._update_ai_runtime_snapshot_view()
        model = self._selected_ai_model_for_task(task_kind)
        include_logs = bool(getattr(self.config.ai_assistant, "include_recent_logs", True))
        self._assistant_set_busy(True, f"Running local assistant task with {model}...")

        def _worker() -> None:
            service = self._create_ai_service()
            if task_kind == "analysis":
                reply = service.analyze_runtime(snapshot, model=model, include_logs=include_logs)
            elif task_kind == "recommendations":
                reply = service.recommend_settings(snapshot, model=model, include_logs=include_logs)
            else:
                reply = service.answer_operator_prompt(prompt, snapshot, model=model, include_logs=include_logs)
            self.assistant_reply_ready.emit({
                "task_kind": task_kind,
                "prompt": prompt,
                "reply": reply,
            })

        threading.Thread(target=_worker, name=f"sentry-v2-ai-{task_kind}", daemon=True).start()

    def _execute_supported_ai_actions(self, actions: List[object]) -> List[str]:
        notes: List[str] = []
        if not bool(getattr(self.config.ai_assistant, "allow_action_execution", True)):
            return ["Supported actions were detected, but assistant action execution is disabled."]
        for raw_action in actions:
            action_type = str(getattr(raw_action, "action_type", "") or "")
            payload = dict(getattr(raw_action, "payload", {}) or {})
            if action_type == "go_home":
                self._on_home_clicked()
                notes.append("Moved to the guard home position.")
            elif action_type == "go_rest":
                self._on_rest_clicked()
                notes.append("Moved to the configured rest position.")
            elif action_type == "set_detection_mode":
                mode_index = int(payload.get("mode_index", 10) or 10)
                mode_label = DETECTION_MODES[mode_index] if 0 <= mode_index < len(DETECTION_MODES) else f"Mode {mode_index}"
                notes.append(self._assistant_apply_detection_mode(mode_index, mode_label))
            elif action_type == "toggle_face_recognition" and hasattr(self, "_chk_face_enabled"):
                enabled = bool(payload.get("enabled", True))
                self._chk_face_enabled.setChecked(enabled)
                notes.append(f"Face recognition {'enabled' if enabled else 'disabled'}." )
            elif action_type == "toggle_shortcuts" and hasattr(self, "_chk_shortcuts_enabled"):
                enabled = bool(payload.get("enabled", True))
                self._chk_shortcuts_enabled.setChecked(enabled)
                notes.append(f"Shortcuts {'enabled' if enabled else 'disabled'}." )
            elif action_type == "toggle_human_voice" and hasattr(self, "_chk_human_voice_enabled"):
                enabled = bool(payload.get("enabled", True))
                self._chk_human_voice_enabled.setChecked(enabled)
                notes.append(f"Human voice {'enabled' if enabled else 'disabled'}." )
            elif action_type == "toggle_ai_auto_speak" and hasattr(self, "_chk_ai_auto_speak"):
                enabled = bool(payload.get("enabled", True))
                self._chk_ai_auto_speak.setChecked(enabled)
                self._on_ai_assistant_settings_changed()
                notes.append(f"Assistant auto-speak {'enabled' if enabled else 'disabled'}." )
            elif action_type == "set_human_voice_style":
                style_key = str(payload.get("style_key", "neutral") or "neutral")
                self._apply_human_voice_style(style_key)
                style_label = str(HUMAN_VOICE_STYLE_PRESETS.get(self._human_voice_style_key(), HUMAN_VOICE_STYLE_PRESETS["neutral"])["label"])
                notes.append(f"Human voice style set to {style_label}.")
            elif action_type == "move_position":
                target_pan = payload.get("pan", self.engine.current_pan)
                target_tilt = payload.get("tilt", self.engine.current_tilt)
                try:
                    pan = float(target_pan)
                    tilt = float(target_tilt)
                except Exception:
                    notes.append("Requested position could not be parsed into numeric pan/tilt values.")
                else:
                    clamped_pan, clamped_tilt = self._clamp_manual_angles(pan, tilt)
                    self._move_to_absolute_position(
                        clamped_pan,
                        clamped_tilt,
                        log_message=f"Assistant position command: P{clamped_pan:.1f} T{clamped_tilt:.1f}",
                    )
                    if abs(clamped_pan - pan) > 0.01 or abs(clamped_tilt - tilt) > 0.01:
                        notes.append(f"Moved to clamped position pan {clamped_pan:.1f}, tilt {clamped_tilt:.1f} within safe limits.")
                    else:
                        notes.append(f"Moved to requested position pan {clamped_pan:.1f}, tilt {clamped_tilt:.1f}.")
            elif action_type == "connect_link":
                if self._comm.is_connected():
                    notes.append("Controller link was already connected.")
                else:
                    self._toggle_connection()
                    notes.append("Controller link connection requested.")
            elif action_type == "disconnect_link":
                if not self._comm.is_connected():
                    notes.append("Controller link was already disconnected.")
                else:
                    self._toggle_connection()
                    notes.append("Controller link disconnect requested.")
            elif action_type == "toggle_camera":
                should_open = bool(payload.get("open", True))
                if should_open and not self._has_local_source():
                    self._toggle_camera()
                    notes.append("Camera open requested.")
                elif not should_open and self._has_local_source():
                    self._toggle_camera()
                    notes.append("Camera close requested.")
                else:
                    notes.append(f"Camera was already {'open' if should_open else 'closed'}." )
        self._refresh_human_voice_diagnostics()
        return notes

    def _render_ai_reply(self, reply: AssistantReply, *, task_kind: str, action_notes: List[str]) -> str:
        lines: List[str] = []
        title = {
            "analysis": "Analysis",
            "recommendations": "Recommendations",
            "prompt": "Assistant",
        }.get(task_kind, "Assistant")
        origin_label = "Ollama" if str(reply.source or "") == "ollama" else "Deterministic fallback"
        origin = f"{origin_label} / {reply.model}" if reply.model else origin_label
        lines.append(f"{title} [{origin}]")
        if reply.error and str(reply.source or "") != "ollama":
            lines.append("The local model reply was unavailable, so this response used the built-in deterministic fallback.")
            lines.append("")
        if action_notes:
            lines.append("Local Action Result:")
            for item in action_notes:
                lines.append(f"- {item}")
            lines.append("")
        lines.append(str(reply.text or "").strip())
        if reply.findings and task_kind in ("analysis", "recommendations"):
            lines.append("")
            lines.append("Supporting Findings:")
            for finding in reply.findings[:4]:
                lines.append(f"- [{finding.severity}] {finding.title}: {finding.detail}")
        if reply.recommendations and task_kind == "recommendations":
            lines.append("")
            lines.append("Supporting Recommendations:")
            for item in reply.recommendations[:5]:
                lines.append(f"- {item}")
        if reply.error:
            lines.append("")
            lines.append(f"Model note: {reply.error}")
        return "\n".join(lines).strip()

    def _on_ai_assistant_reply_ready(self, payload: object) -> None:
        self._assistant_set_busy(False)
        if not isinstance(payload, dict):
            self._append_ai_output("Assistant reply payload was invalid.")
            return
        task_kind = str(payload.get("task_kind") or "prompt")
        reply = payload.get("reply")
        if not isinstance(reply, AssistantReply):
            self._append_ai_output("Assistant reply was invalid.")
            return
        self._assistant_last_reply = reply
        action_notes: List[str] = []
        if task_kind == "prompt" and reply.actions:
            action_notes = self._execute_supported_ai_actions(reply.actions)
        conversational = bool(self.config.ai_assistant.mode == "conversational_voice")
        rendered = self._assistant_format_response(self._render_ai_reply(reply, task_kind=task_kind, action_notes=action_notes), conversational=conversational)
        self._append_ai_output(rendered, speak=conversational, task_kind=task_kind)
        self._update_ai_runtime_snapshot_view()
        voice_status, _voice_ready = self._assistant_voice_route_status()
        status = f"Local assistant completed with {'Ollama' if reply.source == 'ollama' else 'deterministic fallback'} | voice: {voice_status}"
        if hasattr(self, "_lbl_ai_provider_status"):
            self._lbl_ai_provider_status.setText(status)
        self._log(f"AI assistant {task_kind}: source={reply.source} model={reply.model or 'n/a'} error={reply.error or 'none'}")

    def _append_ai_output(self, text: str, *, speak: bool = False, task_kind: str = "prompt") -> None:
        target = getattr(self, "_txt_ai_runtime_output", None) if task_kind in ("analysis", "recommendations") else getattr(self, "_txt_ai_output", None)
        if target is not None:
            target.append(text)
        self._last_spoken_ai_response = self._assistant_speech_summary(text)
        if speak:
            self._maybe_speak_ai_output(self._last_spoken_ai_response)

    def _assistant_speech_summary(self, text: str) -> str:
        raw = " ".join(str(text or "").split()).strip()
        if not raw:
            return ""
        raw = re.sub(r"\b(?:Analysis|Recommendations|Assistant) \[[^\]]+\]\s*", "", raw)
        raw = re.sub(r"\b(?:Supporting Findings|Supporting Recommendations|Model note):", ".", raw, flags=re.IGNORECASE)
        sentence_parts = re.split(r"(?<=[.!?])\s+", raw)
        compact = " ".join(part.strip() for part in sentence_parts[:3] if part.strip()).strip()
        return compact[:280].strip()

    def _maybe_speak_ai_output(self, text: str) -> None:
        if not bool(getattr(self.config.ai_assistant, "auto_speak_responses", False)):
            return
        self._speak_human_phrase(text)

    def _speak_last_ai_output(self) -> None:
        if not self._last_spoken_ai_response:
            self._append_ai_output("No assistant reply is available to speak yet.")
            return
        if not self._speak_human_phrase(self._last_spoken_ai_response):
            self._append_ai_output("Human voice speech is unavailable or disabled. Enable it and validate the route in AI Voice Validation first.")

    def _assistant_detection_mode_name(self) -> str:
        mode_index = int(self._combo_detection_mode.currentIndex()) if hasattr(self, "_combo_detection_mode") else 0
        if 0 <= mode_index < len(DETECTION_MODES):
            return str(DETECTION_MODES[mode_index])
        return f"Mode {mode_index}"

    def _assistant_human_voice_style_key(self) -> str:
        style = str(getattr(self.config.sound, "human_voice_style", "neutral") or "neutral").strip().lower()
        return style if style in HUMAN_VOICE_STYLE_PRESETS else "neutral"

    def _assistant_format_response(self, text: str, *, conversational: bool) -> str:
        raw_text = str(text or "").replace("\r\n", "\n").replace("\r", "\n")
        if conversational:
            cleaned = " ".join(raw_text.split()).strip()
        else:
            cleaned_lines = [line.rstrip() for line in raw_text.split("\n")]
            while cleaned_lines and not cleaned_lines[0].strip():
                cleaned_lines.pop(0)
            while cleaned_lines and not cleaned_lines[-1].strip():
                cleaned_lines.pop()
            cleaned = "\n".join(cleaned_lines).strip()
        if not conversational or not cleaned:
            return cleaned
        prefix = {
            "neutral": "Assistant update.",
            "operator": "Operator update.",
            "alert": "Attention.",
            "warm": "Certainly.",
        }.get(self._assistant_human_voice_style_key(), "Assistant update.")
        if cleaned.lower().startswith(prefix.lower()):
            return cleaned
        return f"{prefix} {cleaned}"

    def _assistant_apply_detection_mode(self, mode_index: int, label: str) -> str:
        if not bool(self.config.ai_assistant.allow_mode_switch):
            return "Assistant mode switching is disabled in the current settings."
        if not hasattr(self, "_combo_detection_mode"):
            return "Detection mode controls are unavailable in this runtime."
        mode_index = int(max(0, min(len(DETECTION_MODES) - 1, int(mode_index))))
        self._combo_detection_mode.setCurrentIndex(mode_index)
        self._log(f"AI assistant changed detection mode to {label}")
        return f"I switched Smart Sentry to {label}."

    def _run_ai_assistant_analysis(self) -> None:
        if not bool(self.config.ai_assistant.enabled and self.config.ai_assistant.allow_runtime_analysis):
            self._append_ai_output("Assistant analysis is disabled in the current settings.", task_kind="analysis")
            return
        self._start_ai_background_task("analysis")

    def _run_ai_assistant_recommendations(self) -> None:
        if not bool(self.config.ai_assistant.enabled and self.config.ai_assistant.allow_setting_drafts):
            self._append_ai_output("Assistant recommendation drafts are disabled.", task_kind="recommendations")
            return
        self._start_ai_background_task("recommendations")

    def _run_ai_assistant_request(self) -> None:
        prompt = str(getattr(self, "_edit_ai_prompt", QLineEdit()).text()).strip()
        if not prompt:
            self._append_ai_output("Enter a request first.")
            return
        if not bool(self.config.ai_assistant.enabled):
            self._append_ai_output("Assistant is disabled.")
            return
        lower_prompt = prompt.lower()
        if "analy" in lower_prompt or "status" in lower_prompt:
            self._run_ai_assistant_analysis()
            self._edit_ai_prompt.clear()
            return
        elif "suggest" in lower_prompt or "recommend" in lower_prompt:
            self._run_ai_assistant_recommendations()
            self._edit_ai_prompt.clear()
            return
        elif ("speak" in lower_prompt or "say" in lower_prompt) and ("summary" in lower_prompt or "status" in lower_prompt):
            summary = self._assistant_runtime_snapshot()
            spoken = self._speak_human_phrase(summary)
            response = f"Status summary: {summary}"
            if not spoken:
                response += " Human voice speech is currently disabled or unavailable, so I returned the summary as text only."
            conversational = bool(self.config.ai_assistant.mode == "conversational_voice")
            self._append_ai_output(self._assistant_format_response(response, conversational=conversational), speak=conversational)
            self._edit_ai_prompt.clear()
            return
        self._start_ai_background_task("prompt", prompt)
        self._edit_ai_prompt.clear()

    def _reset_prompted_runtime(self) -> None:
        self._prompted_matcher.refresh_library_cache()

    def _selected_prompted_target_id(self) -> Optional[str]:
        if not hasattr(self, "_prompted_target_list"):
            return None
        item = self._prompted_target_list.currentItem()
        if item is None:
            return None
        target_id = str(item.data(Qt.UserRole) or "")
        return target_id or None

    def _selected_prompted_target(self):
        target_id = self._selected_prompted_target_id()
        if not target_id:
            return None
        return self._prompted_target_library.get_profile(target_id)

    def _rebuild_prompted_target_list(self) -> None:
        if not hasattr(self, "_prompted_target_list"):
            return
        selected_id = self._selected_prompted_target_id()
        self._prompted_list_syncing = True
        self._prompted_target_list.blockSignals(True)
        self._prompted_target_list.clear()
        for profile in self._prompted_target_library.profiles:
            item = QListWidgetItem(f"{profile.name} ({len(profile.examples)} examples)")
            item.setData(Qt.UserRole, profile.target_id)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            item.setCheckState(Qt.Checked if profile.enabled else Qt.Unchecked)
            self._prompted_target_list.addItem(item)
            if selected_id and profile.target_id == selected_id:
                item.setSelected(True)
        self._prompted_target_list.blockSignals(False)
        self._prompted_list_syncing = False
        self._on_prompted_target_selected()
        self._update_prompted_status_label()

    def _on_prompted_settings_changed(self) -> None:
        self.config.prompted_targets_enabled = bool(self._chk_prompted_enabled.isChecked())
        self.config.prompted_allow_auto_fire = bool(self._chk_prompted_auto_fire.isChecked())
        if not self.config.prompted_targets_enabled:
            self._reset_prompted_runtime()
        self._update_prompted_status_label()

    def _on_prompted_target_selected(self) -> None:
        profile = self._selected_prompted_target()
        self._prompted_detail_syncing = True
        if hasattr(self, "_btn_prompted_rename"):
            self._btn_prompted_rename.setEnabled(profile is not None)
        if hasattr(self, "_btn_prompted_remove_last_example"):
            self._btn_prompted_remove_last_example.setEnabled(profile is not None and bool(profile.examples if profile is not None else []))
        if hasattr(self, "_btn_prompted_remove"):
            self._btn_prompted_remove.setEnabled(profile is not None)
        if profile is not None and hasattr(self, "_edit_prompted_name"):
            self._edit_prompted_name.setText(str(profile.name))
        if hasattr(self, "_spin_prompted_min_score"):
            self._spin_prompted_min_score.setEnabled(profile is not None)
            self._spin_prompted_confirm_hits.setEnabled(profile is not None)
            self._spin_prompted_lost_timeout.setEnabled(profile is not None)
            self._spin_prompted_search_padding.setEnabled(profile is not None)
            self._spin_prompted_global_interval.setEnabled(profile is not None)
            if profile is not None:
                self._spin_prompted_min_score.setValue(float(profile.min_match_score))
                self._spin_prompted_confirm_hits.setValue(int(profile.min_confirm_hits))
                self._spin_prompted_lost_timeout.setValue(float(profile.lost_timeout_s))
                self._spin_prompted_search_padding.setValue(int(profile.local_search_padding_px))
                self._spin_prompted_global_interval.setValue(int(profile.full_frame_search_interval))
                self._lbl_prompted_examples.setText(f"Examples: {len(profile.examples)}")
            else:
                self._lbl_prompted_examples.setText("Examples: 0")
        self._prompted_detail_syncing = False
        self._update_prompted_status_label()

    def _on_prompted_target_item_changed(self, item: QListWidgetItem) -> None:
        if self._prompted_list_syncing:
            return
        target_id = str(item.data(Qt.UserRole) or "")
        profile = self._prompted_target_library.get_profile(target_id)
        if profile is None:
            return
        profile.enabled = item.checkState() == Qt.Checked
        self._save_prompted_target_library()
        self._reset_prompted_runtime()
        self._update_prompted_status_label()

    def _on_prompted_profile_settings_changed(self) -> None:
        if self._prompted_detail_syncing:
            return
        profile = self._selected_prompted_target()
        if profile is None:
            return
        profile.min_match_score = float(self._spin_prompted_min_score.value())
        profile.min_confirm_hits = int(self._spin_prompted_confirm_hits.value())
        profile.lost_timeout_s = float(self._spin_prompted_lost_timeout.value())
        profile.local_search_padding_px = int(self._spin_prompted_search_padding.value())
        profile.full_frame_search_interval = int(self._spin_prompted_global_interval.value())
        self._save_prompted_target_library()
        self._reset_prompted_runtime()
        self._update_prompted_status_label()

    def _rename_selected_prompted_target(self) -> None:
        profile = self._selected_prompted_target()
        if profile is None:
            return
        new_name = str(self._edit_prompted_name.text().strip() or "")
        if not new_name:
            self._log("Enter a target name before renaming.")
            return
        profile.name = new_name
        self._save_prompted_target_library()
        self._reset_prompted_runtime()
        self._rebuild_prompted_target_list()
        self._log(f"Prompted target renamed: {new_name}")

    def _remove_last_prompted_example(self) -> None:
        profile = self._selected_prompted_target()
        if profile is None:
            return
        updated = self._prompted_target_library.remove_last_example(profile.target_id)
        if updated is None:
            return
        if not updated.examples:
            removed_name = str(updated.name)
            self._prompted_target_library.remove_target(updated.target_id)
            self._log(f"Removed final example and deleted prompted target: {removed_name}")
        else:
            self._log(f"Removed last prompted example from {updated.name}.")
        self._save_prompted_target_library()
        self._reset_prompted_runtime()
        self._rebuild_prompted_target_list()

    def _remove_selected_prompted_target(self) -> None:
        profile = self._selected_prompted_target()
        if profile is None:
            return
        removed_name = str(profile.name)
        self._prompted_target_library.remove_target(profile.target_id)
        self._save_prompted_target_library()
        self._reset_prompted_runtime()
        self._rebuild_prompted_target_list()
        self._log(f"Prompted target removed: {removed_name}")

    def _set_prompted_capture_active(self, active: bool) -> None:
        self._prompted_capture_active = bool(active)
        if hasattr(self, "_video_label"):
            self._video_label.set_roi_selection_enabled(bool(active))
        if hasattr(self, "_btn_prompted_live"):
            self._btn_prompted_live.setText("Stop Live Capture" if active else "Add From Live")
        self._update_prompted_status_label()

    def _toggle_prompted_live_capture(self) -> None:
        if self._prompted_capture_active:
            self._set_prompted_capture_active(False)
            self._log("Prompted live capture stopped.")
            return
        if self._last_raw_frame is None:
            self._log("Prompted live capture needs an active frame first.")
            return
        if self._mask_capture_active:
            self._log("Disable no-fire mask capture before prompted live capture.")
            return
        self._set_prompted_capture_active(True)
        self._log("Prompted live capture enabled: drag a box on the live video.")

    def _browse_prompted_image(self) -> None:
        path, _selected_filter = QFileDialog.getOpenFileName(
            self,
            "Select Target Image",
            str(Path(__file__).resolve().parents[2]),
            "Images (*.png *.jpg *.jpeg *.bmp *.webp);;All files (*.*)",
        )
        if not path:
            return
        image = cv2.imread(path)
        if image is None:
            self._log(f"Could not load image: {path}")
            return
        dialog = PromptedMediaSelectionDialog(
            title="Select Prompted Targets From Image",
            image=image,
            theme_tokens=self._theme_tokens(),
            parent=self,
        )
        if dialog.exec_() != dialog.Accepted:
            return
        selections = dialog.selections()
        for selection in selections:
            selection.source_path = path
        self._append_or_create_prompted_targets(selections, "image")

    def _browse_prompted_video(self) -> None:
        path, _selected_filter = QFileDialog.getOpenFileName(
            self,
            "Select Target Video",
            str(Path(__file__).resolve().parents[2]),
            "Videos (*.mp4 *.avi *.mov *.mkv *.wmv *.m4v);;All files (*.*)",
        )
        if not path:
            return
        dialog = PromptedMediaSelectionDialog(
            title="Select Prompted Targets From Video",
            video_path=path,
            theme_tokens=self._theme_tokens(),
            parent=self,
        )
        if dialog.exec_() != dialog.Accepted:
            return
        selections = dialog.selections()
        for selection in selections:
            selection.source_path = path
        self._append_or_create_prompted_targets(selections, "video")

    def _append_or_create_prompted_targets(self, selections: List[PromptedSelection], source_label: str) -> None:
        if not selections:
            return
        selected_profile = self._selected_prompted_target() if self._chk_prompted_append_selected.isChecked() else None
        if selected_profile is not None:
            self._prompted_target_library.append_examples(selected_profile.target_id, selections)
            self._save_prompted_target_library()
            self._reset_prompted_runtime()
            self._rebuild_prompted_target_list()
            self._log(f"Added {len(selections)} {source_label} example(s) to {selected_profile.name}.")
            return

        base_name = str(self._edit_prompted_name.text().strip() or "")
        created = 0
        if len(selections) == 1:
            name = base_name or self._prompted_target_library.next_default_name()
            if self._prompted_target_library.add_new_target(name, selections) is not None:
                created += 1
        else:
            for index, selection in enumerate(selections, start=1):
                name = f"{base_name} {index}".strip() if base_name else self._prompted_target_library.next_default_name()
                if self._prompted_target_library.add_new_target(name, [selection]) is not None:
                    created += 1
        if created > 0:
            self._save_prompted_target_library()
            self._reset_prompted_runtime()
            self._rebuild_prompted_target_list()
            self._log(f"Created {created} prompted target(s) from {source_label}.")

    def _on_video_roi_selected(self, frame_x: float, frame_y: float, width: float, height: float) -> None:
        if not self._prompted_capture_active:
            return
        if self._last_raw_frame is None:
            self._log("Prompted capture failed: no current frame available.")
            self._set_prompted_capture_active(False)
            return
        selection = PromptedSelection(
            frame=self._last_raw_frame.copy(),
            bbox=(int(round(frame_x)), int(round(frame_y)), max(1, int(round(width))), max(1, int(round(height)))),
            source_type="live",
        )
        self._append_or_create_prompted_targets([selection], "live")
        self._set_prompted_capture_active(False)

    def _update_prompted_status_label(self) -> None:
        if not hasattr(self, "_lbl_prompted_status"):
            return
        enabled_count = sum(1 for profile in self._prompted_target_library.profiles if profile.enabled)
        total_count = len(self._prompted_target_library.profiles)
        status = "ON" if self.config.prompted_targets_enabled else "OFF"
        live_hint = " | live capture armed" if self._prompted_capture_active else ""
        selected = self._selected_prompted_target()
        selected_hint = f" | Selected: {selected.name}" if selected is not None else ""
        self._lbl_prompted_status.setText(
            f"Runtime: {status} | Targets: {enabled_count}/{total_count} enabled | "
            f"Auto-fire: {'ON' if self.config.prompted_allow_auto_fire else 'OFF'}{selected_hint}{live_hint}"
        )

    # ------------------------------------------------------------------ #
    #  Internal helpers
    # ------------------------------------------------------------------ #

    def set_host_main_window(self, main_window: Optional[QWidget]) -> None:
        self._main_window_ref = main_window
        self._host_hardware_managed = main_window is not None
        self._apply_theme()

    def _host_controls_hardware(self) -> bool:
        return bool(self._host_hardware_managed and self._main_window_ref is not None)

    def _theme_config(self) -> ThemeConfig:
        theme_cfg = getattr(self.config, "theme", None)
        if theme_cfg is None:
            self.config.theme = ThemeConfig()
            theme_cfg = self.config.theme
        return theme_cfg

    def _theme_tokens(self) -> dict:
        theme_cfg = self._theme_config()
        preset = THEME_PRESETS.get(str(theme_cfg.preset or "ember"), THEME_PRESETS["ember"])
        is_light = bool(preset.get("is_light", False))
        accent_strength = _clamp_int(getattr(theme_cfg, "accent_strength_pct", 100), 60, 140)
        contrast_pct = _clamp_int(getattr(theme_cfg, "contrast_pct", 100), 85, 125)
        surface_opacity = _clamp_int(getattr(theme_cfg, "surface_opacity_pct", 94), 55, 100)
        video_opacity = _clamp_int(getattr(theme_cfg, "video_panel_opacity_pct", 100), 55, 100)
        window_opacity = _clamp_int(getattr(theme_cfg, "window_opacity_pct", 100), 70, 100)
        radius = _clamp_int(getattr(theme_cfg, "corner_radius_px", 14), 8, 24)
        font_scale_pct = _clamp_int(getattr(theme_cfg, "font_scale_pct", 100), 50, 280)

        accent_boost = (accent_strength - 100) / 40.0
        contrast_boost = (contrast_pct - 100) / 25.0
        accent_target = "#ffffff" if not is_light else "#1b130d"
        text_target = "#ffffff" if not is_light else "#120e0c"
        subtle_target = "#f5ede4" if not is_light else "#2f2318"
        dark_sink = preset["root_bg"] if not is_light else "#efe4d5"

        if accent_boost >= 0:
            accent = _mix_hex(preset["accent"], accent_target, accent_boost * 0.32)
            accent_soft = _mix_hex(preset["accent_soft"], accent_target, accent_boost * 0.22)
        else:
            accent = _mix_hex(preset["accent"], dark_sink, abs(accent_boost) * 0.34)
            accent_soft = _mix_hex(preset["accent_soft"], dark_sink, abs(accent_boost) * 0.28)

        if contrast_boost >= 0:
            text = _mix_hex(preset["text"], text_target, contrast_boost * 0.25)
            muted = _mix_hex(preset["muted"], subtle_target, contrast_boost * 0.20)
            border = _mix_hex(preset["border"], accent if not is_light else text_target, contrast_boost * 0.16)
        else:
            text = _mix_hex(preset["text"], preset["muted"], abs(contrast_boost) * 0.22)
            muted = _mix_hex(preset["muted"], preset["surface"], abs(contrast_boost) * 0.18)
            border = _mix_hex(preset["border"], preset["surface"], abs(contrast_boost) * 0.20)

        ui_scale = max(0.50, min(2.80, float(font_scale_pct) / 100.0))
        base_font_pt = 9.8 * ui_scale
        shell_opacity = max(28, min(surface_opacity, window_opacity) - 12)
        hero_text = text if is_light else _mix_hex(text, "#ffffff", 0.10)
        button_alpha = surface_opacity
        button_hover_alpha = min(100, surface_opacity)
        button_pressed_alpha = max(40, surface_opacity - 10)
        button_disabled_alpha = max(26, surface_opacity - 34)
        accent_alpha = min(100, surface_opacity)
        accent_faint_alpha = max(22, min(70, surface_opacity - 18))
        accent_mid_hex = _mix_hex(accent, preset["surface"], 0.38 if not is_light else 0.18)
        button_hover_hex = _mix_hex(preset["surface_alt"], accent, 0.16 if not is_light else 0.12)
        button_pressed_hex = _mix_hex(preset["surface_alt"], preset["root_bg"], 0.30 if not is_light else 0.10)
        button_checked_hex = _mix_hex(preset["surface"], accent, 0.34 if not is_light else 0.22)
        button_disabled_hex = _mix_hex(preset["surface"], preset["root_bg"], 0.45 if not is_light else 0.18)
        primary_button_hex = _mix_hex(accent, preset["hero_mid"], 0.22 if not is_light else 0.10)
        primary_button_hover_hex = _mix_hex(accent, text_target, 0.18 if not is_light else 0.06)
        primary_button_pressed_hex = _mix_hex(accent_soft, preset["root_bg"], 0.22 if not is_light else 0.05)
        mode_button_hex = _mix_hex(preset["surface_alt"], accent, 0.12)
        mode_button_hover_hex = _mix_hex(preset["surface_alt"], accent, 0.20)
        danger_button_hex = _mix_hex("#c45c54", preset["surface_alt"], 0.34 if not is_light else 0.18)
        danger_button_hover_hex = _mix_hex("#d97166", preset["surface_alt"], 0.22 if not is_light else 0.12)
        danger_button_pressed_hex = _mix_hex("#9d4941", preset["surface_alt"], 0.24 if not is_light else 0.10)
        hero_badge_bg_hex = _mix_hex(preset["surface_alt"], preset["root_bg"], 0.35)

        return {
            "preset_label": preset["label"],
            "preset_description": preset["description"],
            "is_light": is_light,
            "root_bg": preset["root_bg"],
            "root_bg_rgba": _rgba_hex(preset["root_bg"], shell_opacity),
            "surface_rgba": _rgba_hex(preset["surface"], surface_opacity),
            "surface_alt_rgba": _rgba_hex(preset["surface_alt"], min(100, surface_opacity)),
            "panel_rgba": _rgba_hex(preset["panel"], max(55, surface_opacity - 4)),
            "field_rgba": _rgba_hex(preset["field"], min(100, surface_opacity + 2)),
            "field_text": text,
            "field_border": border,
            "border": border,
            "text": text,
            "muted": muted,
            "subtle_text": muted,
            "accent": accent,
            "accent_soft": accent_soft,
            "accent_mid": _rgba_hex(accent_mid_hex, accent_alpha),
            "accent_faint": _rgba_hex(accent, accent_faint_alpha),
            "button_bg": _rgba_hex(preset["surface_alt"], button_alpha),
            "button_text": text,
            "button_border": border,
            "button_hover": _rgba_hex(button_hover_hex, button_hover_alpha),
            "button_pressed": _rgba_hex(button_pressed_hex, button_pressed_alpha),
            "button_checked": _rgba_hex(button_checked_hex, button_alpha),
            "button_disabled": _rgba_hex(button_disabled_hex, button_disabled_alpha),
            "disabled_text": _mix_hex(muted, preset["surface"], 0.35),
            "disabled_border": _mix_hex(border, preset["surface"], 0.26),
            "primary_button_bg": _rgba_hex(primary_button_hex, button_alpha),
            "primary_button_border": accent_soft,
            "primary_button_hover": _rgba_hex(primary_button_hover_hex, button_hover_alpha),
            "primary_button_pressed": _rgba_hex(primary_button_pressed_hex, button_pressed_alpha),
            "mode_button_bg": _rgba_hex(mode_button_hex, button_alpha),
            "mode_button_border": _mix_hex(border, accent, 0.28),
            "mode_button_text": hero_text,
            "mode_button_hover": _rgba_hex(mode_button_hover_hex, button_hover_alpha),
            "danger_button_bg": _rgba_hex(danger_button_hex, button_alpha),
            "danger_button_border": _mix_hex("#e88074", accent_soft, 0.30),
            "danger_button_hover": _rgba_hex(danger_button_hover_hex, button_hover_alpha),
            "danger_button_pressed": _rgba_hex(danger_button_pressed_hex, button_pressed_alpha),
            "slider_groove": _mix_hex(preset["surface_alt"], border, 0.35),
            "scroll_handle": _mix_hex(border, accent, 0.16),
            "hero_start": _rgba_hex(preset["hero_start"], min(100, surface_opacity + 4)),
            "hero_mid": _rgba_hex(preset["hero_mid"], min(100, surface_opacity + 2)),
            "hero_end": _rgba_hex(preset["hero_end"], min(100, surface_opacity + 6)),
            "hero_text": hero_text,
            "hero_subtle": _mix_hex(hero_text, muted, 0.35),
            "hero_badge_bg": _rgba_hex(hero_badge_bg_hex, max(38, min(100, surface_opacity - 12))),
            "hero_badge_text": hero_text,
            "tooltip_bg": preset["tooltip_bg"],
            "tooltip_text": preset["tooltip_text"],
            "video_bg_rgba": _rgba_hex(preset["video_bg"], video_opacity),
            "video_text": preset["video_text"],
            "window_opacity": window_opacity,
            "radius": radius,
            "status_neutral": _mix_hex(muted, text, 0.15),
            "status_info": _mix_hex(accent, text, 0.10 if not is_light else 0.18),
            "status_ok": _mix_hex("#4dbb74", text, 0.18 if not is_light else 0.08),
            "status_warn": _mix_hex("#d9a63e", text, 0.18 if not is_light else 0.06),
            "status_error": _mix_hex("#d8645f", text, 0.14 if not is_light else 0.05),
            "status_meta": _mix_hex(muted, preset["field"], 0.05 if not is_light else 0.20),
            "status_card_bg": _rgba_hex(_mix_hex(preset["surface"], preset["panel"], 0.35), min(100, surface_opacity + 2)),
            "status_subframe_bg": _rgba_hex(_mix_hex(preset["surface_alt"], preset["panel"], 0.30), min(100, surface_opacity)),
            "status_card_border": _mix_hex(border, accent, 0.12),
            "status_card_title": _mix_hex(accent, text, 0.22 if not is_light else 0.14),
            "status_card_value": _mix_hex(text, accent, 0.05 if not is_light else 0.02),
            "status_section_title": _mix_hex(accent, text, 0.20 if not is_light else 0.12),
            "status_progress_bg": _rgba_hex(_mix_hex(preset["field"], preset["panel"], 0.25), 100),
            "status_progress_pan": _mix_hex(accent, preset["hero_mid"], 0.22 if not is_light else 0.12),
            "status_progress_tilt": _mix_hex("#63b572", accent, 0.28 if not is_light else 0.12),
            "status_card_radius": max(6, radius - 6),
            "ui_scale": ui_scale,
            "base_font_pt": base_font_pt,
            "hero_title_pt": max(20.0, 20.8 + ((ui_scale - 1.0) * 3.8)),
            "hero_subtitle_pt": max(12.8, 13.4 + ((ui_scale - 1.0) * 2.2)),
            "hero_badge_pt": max(11.2, 11.8 + ((ui_scale - 1.0) * 1.7)),
            "nav_title_pt": max(11.6, base_font_pt + 1.4),
            "nav_count_pt": max(12.6, base_font_pt + 2.2),
            "status_font_pt": base_font_pt,
        }

    def _select_theme_preset(self, preset_key: str) -> None:
        if not hasattr(self, "_combo_theme_preset"):
            return
        index = self._combo_theme_preset.findData(preset_key)
        if index >= 0:
            self._combo_theme_preset.setCurrentIndex(index)

    def _sync_theme_widgets(self) -> None:
        if not hasattr(self, "_combo_theme_preset"):
            return
        theme_cfg = self._theme_config()
        widgets = [
            self._combo_theme_preset,
            self._slider_theme_accent,
            self._slider_theme_surface_opacity,
            self._slider_theme_video_opacity,
            self._slider_theme_window_opacity,
            self._slider_theme_contrast,
            self._slider_theme_radius,
        ]
        for widget in widgets:
            widget.blockSignals(True)
        try:
            preset_index = self._combo_theme_preset.findData(str(theme_cfg.preset or "ember"))
            if preset_index < 0:
                preset_index = self._combo_theme_preset.findData("ember")
            if preset_index >= 0:
                self._combo_theme_preset.setCurrentIndex(preset_index)
            self._slider_theme_accent.setValue(_clamp_int(theme_cfg.accent_strength_pct, 60, 140))
            self._slider_theme_surface_opacity.setValue(_clamp_int(theme_cfg.surface_opacity_pct, 55, 100))
            self._slider_theme_video_opacity.setValue(_clamp_int(theme_cfg.video_panel_opacity_pct, 55, 100))
            self._slider_theme_window_opacity.setValue(_clamp_int(theme_cfg.window_opacity_pct, 70, 100))
            self._slider_theme_contrast.setValue(_clamp_int(theme_cfg.contrast_pct, 85, 125))
            self._slider_theme_radius.setValue(_clamp_int(theme_cfg.corner_radius_px, 8, 24))
        finally:
            for widget in widgets:
                widget.blockSignals(False)

        tokens = self._theme_tokens()
        self._lbl_theme_preset_desc.setText(tokens["preset_description"])
        self._lbl_theme_accent.setText(f"{self._slider_theme_accent.value()}%")
        self._lbl_theme_surface_opacity.setText(f"{self._slider_theme_surface_opacity.value()}%")
        self._lbl_theme_video_opacity.setText(f"{self._slider_theme_video_opacity.value()}%")
        self._lbl_theme_window_opacity.setText(f"{self._slider_theme_window_opacity.value()}%")
        self._lbl_theme_contrast.setText(f"{self._slider_theme_contrast.value()}%")
        self._lbl_theme_radius.setText(f"{self._slider_theme_radius.value()} px")
        self._lbl_theme_summary.setText(
            f"Preset: {tokens['preset_label']}\n"
            f"Accent {self._slider_theme_accent.value()}% | Panels {self._slider_theme_surface_opacity.value()}% | "
            f"Video {self._slider_theme_video_opacity.value()}% | Window {self._slider_theme_window_opacity.value()}%\n"
            f"Contrast {self._slider_theme_contrast.value()}% | Radius {self._slider_theme_radius.value()} px"
        )

    def _on_theme_preset_changed(self, _index: int) -> None:
        if not hasattr(self, "_combo_theme_preset"):
            return
        self._theme_config().preset = str(self._combo_theme_preset.currentData() or "ember")
        self._sync_theme_widgets()
        self._apply_theme()
        self._save_config_quietly()

    def _on_theme_settings_changed(self, _value: int) -> None:
        theme_cfg = self._theme_config()
        theme_cfg.accent_strength_pct = int(self._slider_theme_accent.value())
        theme_cfg.surface_opacity_pct = int(self._slider_theme_surface_opacity.value())
        theme_cfg.video_panel_opacity_pct = int(self._slider_theme_video_opacity.value())
        theme_cfg.window_opacity_pct = int(self._slider_theme_window_opacity.value())
        theme_cfg.contrast_pct = int(self._slider_theme_contrast.value())
        theme_cfg.corner_radius_px = int(self._slider_theme_radius.value())
        self._sync_theme_widgets()
        self._apply_theme()
        self._save_config_quietly()

    def _reset_theme_defaults(self) -> None:
        self.config.theme = ThemeConfig()
        self._sync_theme_widgets()
        self._apply_theme()
        self._save_config_quietly()

    def _get_main_window(self):
        return self._main_window_ref

    def _apply_default_panel_width(self) -> None:
        self._apply_panel_width(SENTRY_V2_PANEL_DEFAULT_WIDTH)

    def _apply_panel_width(self, width: int) -> None:
        width = max(SENTRY_V2_PANEL_MIN_WIDTH, int(width))
        total_width = self._main_splitter.size().width()
        if total_width <= 0:
            total_width = max(self.width(), width + SENTRY_V2_VIDEO_MIN_WIDTH)
        left_width = max(SENTRY_V2_VIDEO_MIN_WIDTH, total_width - width)
        self._main_splitter.setSizes([left_width, width])
        self._update_responsive_layout()

    def _on_servo_time_changed(self, value: int) -> None:
        move_time = int(value)
        self.config.connection.bus_servo_time_ms = move_time
        self._comm.bus_servo_time_ms = move_time
        self._sync_servo_time_preset_combo()
        if not self._applying_servo_preset:
            self._set_servo_time_preset_label(self._match_servo_time_preset_name())
        if not self._applying_master_preset:
            self._set_master_profile_label(self._match_master_profile_name())
            self._update_master_stack_summary()

    def _rebuild_servo_time_preset_combo(self) -> None:
        if not hasattr(self, "_combo_servo_time_preset"):
            return
        combo = self._combo_servo_time_preset
        combo.blockSignals(True)
        combo.clear()
        combo.addItem("Custom / Current Value", "")
        for preset_name, preset in BUS_SERVO_TIME_PRESETS.items():
            combo.addItem(preset["label"], preset_name)
            index = combo.count() - 1
            self._apply_tooltip(combo, "servo_move_time")
            combo.setItemData(index, SENTRY_V2_TOOLTIPS.get(preset.get("tooltip_key", ""), ""), Qt.ToolTipRole)
        combo.blockSignals(False)
        self._sync_servo_time_preset_combo()

    def _sync_servo_time_preset_combo(self) -> None:
        if not hasattr(self, "_combo_servo_time_preset"):
            return
        matched = self._match_servo_time_preset_name() or ""
        combo = self._combo_servo_time_preset
        index = combo.findData(matched)
        if index < 0:
            index = 0
        combo.blockSignals(True)
        combo.setCurrentIndex(index)
        combo.blockSignals(False)

    def _on_servo_time_preset_selected(self, index: int) -> None:
        if index < 0 or not hasattr(self, "_combo_servo_time_preset"):
            return
        preset_name = str(self._combo_servo_time_preset.itemData(index) or "")
        if not preset_name:
            return
        self._apply_servo_time_preset(preset_name)

    def _set_master_profile_label(self, preset_name: Optional[str]) -> None:
        if not hasattr(self, "_lbl_master_profile"):
            return
        all_profiles = self._get_master_profiles()
        if preset_name and preset_name in all_profiles:
            self._active_master_profile_name = preset_name
            preset = all_profiles[preset_name]
            self._lbl_master_profile.setText(f"Active profile: {preset['label']} | {preset['description']}")
        else:
            self._active_master_profile_name = None
            self._lbl_master_profile.setText("Active profile: Custom | A mixed stack of individual presets or manual tuning is active.")

    def _set_servo_time_preset_label(self, preset_name: Optional[str]) -> None:
        if not hasattr(self, "_lbl_servo_time_preset"):
            return
        if preset_name and preset_name in BUS_SERVO_TIME_PRESETS:
            preset = BUS_SERVO_TIME_PRESETS[preset_name]
            self._lbl_servo_time_preset.setText(
                f"Active move-time preset: {preset['label']} | {preset['move_time_ms']} ms | {preset['description']}"
            )
        else:
            current = int(self._spin_servo_time.value()) if hasattr(self, "_spin_servo_time") else int(self.config.connection.bus_servo_time_ms)
            self._lbl_servo_time_preset.setText(f"Active move-time preset: Custom | {current} ms")

    def _update_master_stack_summary(self) -> None:
        if not hasattr(self, "_lbl_master_stack"):
            return
        detect = self._match_detection_preset_name() or "Custom"
        filt = self._match_filter_preset_name() or "Custom"
        threat = self._match_threat_preset_name() or "Custom"
        engage = self._match_engagement_preset_name() or "Custom"
        servo = self._match_servo_time_preset_name() or "Custom"
        detect_label = DETECTION_PRESETS[detect]["label"] if detect in DETECTION_PRESETS else detect
        filter_label = TARGET_FILTER_PRESETS[filt]["label"] if filt in TARGET_FILTER_PRESETS else filt
        threat_label = THREAT_AI_PRESETS[threat]["label"] if threat in THREAT_AI_PRESETS else threat
        engage_label = ENGAGEMENT_PRESETS[engage]["label"] if engage in ENGAGEMENT_PRESETS else engage
        servo_label = BUS_SERVO_TIME_PRESETS[servo]["label"] if servo in BUS_SERVO_TIME_PRESETS else servo
        self._lbl_master_stack.setText(
            f"Detection: {detect_label}\n"
            f"Target Filter: {filter_label}\n"
            f"Threat AI: {threat_label}\n"
            f"Engage: {engage_label}\n"
            f"Bus Servo Move Time: {servo_label} ({int(self.config.connection.bus_servo_time_ms)} ms)"
        )

    def _set_detection_preset_label(self, preset_name: Optional[str]) -> None:
        if not hasattr(self, "_lbl_detection_preset"):
            return
        if preset_name and preset_name in DETECTION_PRESETS:
            preset = DETECTION_PRESETS[preset_name]
            self._lbl_detection_preset.setText(f"Active preset: {preset['label']} | {preset['description']}")
            return
        parsed = self._parse_method_size_preset_name(preset_name)
        if parsed:
            mode, size_key = parsed
            mode_label = DETECTION_MODES[mode] if 0 <= mode < len(DETECTION_MODES) else f"Mode {mode}"
            profile = TARGET_SIZE_PRESETS[size_key]
            self._lbl_detection_preset.setText(
                f"Active preset: {mode_label} / {profile['label']} | {profile['description']}"
            )
        else:
            self._lbl_detection_preset.setText("Active preset: Custom | Manual Detection tuning in use.")

    def _set_filter_preset_label(self, preset_name: Optional[str]) -> None:
        if not hasattr(self, "_lbl_filter_preset"):
            return
        if preset_name and preset_name in TARGET_FILTER_PRESETS:
            preset = TARGET_FILTER_PRESETS[preset_name]
            self._lbl_filter_preset.setText(f"Active preset: {preset['label']} | {preset['description']}")
        else:
            self._lbl_filter_preset.setText("Active preset: Custom | Manual Target Filter tuning in use.")

    def _set_threat_preset_label(self, preset_name: Optional[str]) -> None:
        if not hasattr(self, "_lbl_threat_preset"):
            return
        if preset_name and preset_name in THREAT_AI_PRESETS:
            preset = THREAT_AI_PRESETS[preset_name]
            self._lbl_threat_preset.setText(f"Active preset: {preset['label']} | {preset['description']}")
        else:
            self._lbl_threat_preset.setText("Active preset: Custom | Manual Threat AI tuning in use.")

    def _set_engagement_preset_label(self, preset_name: Optional[str]) -> None:
        if not hasattr(self, "_lbl_engagement_preset"):
            return
        if preset_name and preset_name in ENGAGEMENT_PRESETS:
            preset = ENGAGEMENT_PRESETS[preset_name]
            self._lbl_engagement_preset.setText(f"Active preset: {preset['label']} | {preset['description']}")
        else:
            self._lbl_engagement_preset.setText("Active preset: Custom | Manual Engage tuning in use.")

    def _match_detection_preset_name(self) -> Optional[str]:
        dm = self.config.detection_mode
        for preset_name, preset in DETECTION_PRESETS.items():
            matched = True
            for key, value in preset["settings"].items():
                current_value = getattr(dm, key)
                if isinstance(value, float):
                    if abs(float(current_value) - float(value)) > 0.005:
                        matched = False
                        break
                else:
                    if current_value != value:
                        matched = False
                        break
            if matched:
                return preset_name

        mode = int(dm.detection_mode)
        for size_key in TARGET_SIZE_PRESETS.keys():
            generated = self._get_generated_method_size_settings(mode, size_key)
            if not generated:
                continue
            matched = True
            for key, value in generated.items():
                current_value = getattr(dm, key)
                if isinstance(value, float):
                    if abs(float(current_value) - float(value)) > 0.005:
                        matched = False
                        break
                else:
                    if current_value != value:
                        matched = False
                        break
            if matched:
                return self._make_method_size_preset_name(mode, size_key)
        return None

    def _match_filter_preset_name(self) -> Optional[str]:
        tf = self.config.target_filter
        current_classes = [str(name).lower() for name in tf.allowed_classes]
        for preset_name, preset in TARGET_FILTER_PRESETS.items():
            settings = preset["settings"]
            preset_classes = [str(name).lower() for name in settings["allowed_classes"]]
            if current_classes != preset_classes:
                continue
            if abs(float(tf.min_confidence) - float(settings["min_confidence"])) > 0.005:
                continue
            if abs(float(tf.min_size_ratio) - float(settings["min_size_ratio"])) > 0.0001:
                continue
            if abs(float(tf.max_size_ratio) - float(settings["max_size_ratio"])) > 0.0001:
                continue
            return preset_name
        return None

    def _match_servo_time_preset_name(self) -> Optional[str]:
        current = int(self.config.connection.bus_servo_time_ms)
        for preset_name, preset in BUS_SERVO_TIME_PRESETS.items():
            if current == int(preset["move_time_ms"]):
                return preset_name
        return None

    def _match_master_profile_name(self) -> Optional[str]:
        detection_name = self._match_detection_preset_name()
        filter_name = self._match_filter_preset_name()
        threat_name = self._match_threat_preset_name()
        engagement_name = self._match_engagement_preset_name()
        servo_name = self._match_servo_time_preset_name()
        for preset_name, preset in self._get_master_profiles().items():
            if (
                detection_name == preset["detection"]
                and filter_name == preset["filter"]
                and threat_name == preset["threat"]
                and engagement_name == preset["engagement"]
                and servo_name == preset["servo"]
            ):
                return preset_name
        return None

    def _match_threat_preset_name(self) -> Optional[str]:
        ts = self.config.threat_scoring
        for preset_name, preset in THREAT_AI_PRESETS.items():
            matched = True
            for key, value in preset["weights"].items():
                if abs(float(getattr(ts, key)) - float(value)) > 0.005:
                    matched = False
                    break
            if matched and bool(ts.use_ml_model) == bool(preset.get("use_ml_model", False)):
                return preset_name
        return None

    def _match_engagement_preset_name(self) -> Optional[str]:
        eg = self.config.engagement
        for preset_name, preset in ENGAGEMENT_PRESETS.items():
            settings = self._resolved_engagement_preset_settings(preset)
            matched = True
            for key, value in settings.items():
                current_value = getattr(eg, key)
                if isinstance(value, float):
                    if abs(float(current_value) - float(value)) > 0.005:
                        matched = False
                        break
                else:
                    if current_value != value:
                        matched = False
                        break
            if matched:
                return preset_name
        return None

    def _resolved_engagement_preset_settings(self, preset: dict) -> dict:
        settings = dict(vars(EngagementConfig()))
        raw_settings = dict(preset.get("settings", {}))
        settings.update(raw_settings)
        settings = _normalize_engagement_precision_limits(settings, raw_settings)
        max_queue_length = max(1, int(settings.get("max_queue_length", 1) or 1))
        settings["max_queue_length"] = max_queue_length
        # The visible queue control is the source of truth. Preserve explicit
        # single-target presets only when they also request a single slot.
        if bool(settings.get("single_target_only", False)) and max_queue_length <= 1:
            settings["max_queue_length"] = 1
            settings["optimize_slew_order"] = False
            settings["single_target_only"] = True
        else:
            settings["single_target_only"] = max_queue_length <= 1
        return settings

    def _apply_threat_preset(self, preset_name_or_settings: str | dict) -> None:
        # Handle both preset name (string) and direct settings (dict) from master profiles
        if isinstance(preset_name_or_settings, dict):
            # Direct settings dict from master profile
            weights = preset_name_or_settings.get("weights", {})
            use_ml_model = preset_name_or_settings.get("use_ml_model", False)
            preset_label = None
            preset_dict = None
        else:
            preset_dict = THREAT_AI_PRESETS.get(preset_name_or_settings)
            if not preset_dict:
                return
            weights = preset_dict["weights"]
            use_ml_model = preset_dict.get("use_ml_model", False)
            preset_label = preset_name_or_settings

        self._applying_threat_preset = True
        try:
            for key, value in weights.items():
                if key in self._weight_sliders:
                    slider = self._weight_sliders[key]
                    slider.blockSignals(True)
                    slider.setValue(int(round(float(value) * 100.0)))
                    slider.blockSignals(False)
                    if key in self._weight_value_labels:
                        self._weight_value_labels[key].setText(f"{float(value):.2f}")
            self._chk_ml.blockSignals(True)
            self._chk_ml.setChecked(bool(use_ml_model))
            self._chk_ml.blockSignals(False)
            self._on_scoring_changed()
            if preset_label:
                self._set_threat_preset_label(preset_label)
            if preset_dict:
                self._log(f"Threat AI preset: {preset_dict['label']}")
            if not self._applying_master_preset:
                self._set_master_profile_label(self._match_master_profile_name())
                self._update_master_stack_summary()
        finally:
            self._applying_threat_preset = False

    def _apply_detection_preset(self, preset_name_or_settings: str | dict) -> None:
        # Handle both preset name (string) and direct settings (dict) from master profiles
        if isinstance(preset_name_or_settings, dict):
            # Direct settings dict from master profile
            self._apply_detection_settings(dict(preset_name_or_settings), None)
            return
        
        preset = DETECTION_PRESETS.get(preset_name_or_settings)
        if preset:
            self._apply_detection_settings(dict(preset["settings"]), preset_name_or_settings)
            return

        parsed = self._parse_method_size_preset_name(preset_name_or_settings)
        if not parsed:
            return
        mode, size_key = parsed
        generated = self._get_generated_method_size_settings(mode, size_key)
        if not generated:
            return
        self._apply_detection_settings(generated, preset_name_or_settings)

    def _apply_detection_settings(self, settings: dict, preset_name_for_label: Optional[str] = None) -> None:
        if not settings:
            return

        settings = self._tighten_detection_size_windows(settings)

        self._applying_detection_preset = True
        try:
            self._combo_detection_mode.blockSignals(True)
            self._combo_detection_mode.setCurrentIndex(int(settings["detection_mode"]))
            self._combo_detection_mode.blockSignals(False)

            widget_values = [
                (self._spin_min_contour, settings["min_contour_area"]),
                (self._spin_max_contour, settings["max_contour_area"]),
                (self._spin_yolo_min_area, settings["yolo_min_area"]),
                (self._spin_yolo_conf, settings["yolo_confidence"]),
                (self._spin_color_min, settings["color_min_area"]),
                (self._spin_color_max, settings["color_max_area"]),
                (self._spin_fusion_overlap, settings["color_fusion_overlap"]),
                (self._spin_motion_thresh, settings["motion_gate_threshold"]),
                (self._spin_motion_ignore, settings["motion_ignore_after_move_s"]),
            ]
            for widget, value in widget_values:
                widget.blockSignals(True)
                widget.setValue(value)
                widget.blockSignals(False)

            self._combo_color_preset.blockSignals(True)
            color_index = COLOR_PRESETS.index(settings["color_preset"]) if settings["color_preset"] in COLOR_PRESETS else 0
            self._combo_color_preset.setCurrentIndex(color_index)
            self._combo_color_preset.blockSignals(False)

            self._combo_fusion.blockSignals(True)
            self._combo_fusion.setCurrentText(settings["color_fusion_strategy"])
            self._combo_fusion.blockSignals(False)

            dm = self.config.detection_mode
            for key, value in settings.items():
                setattr(dm, key, value)

            self._update_mode_description()
            self._update_detection_panel_visibility()
            self._update_size_ratio_hints()
            self._sync_target_size_preset_combo()
            self._detector.reset()
            self._tracker.reset()
            self._prompted_matcher.reset()
            self._invalidate_detector_runtime()
            self._reset_detection_runtime_if_active()
            self.detection_mode_changed.emit(int(settings["detection_mode"]))
            self._push_config()
            self._set_detection_preset_label(preset_name_for_label or self._match_detection_preset_name())
            if not self._applying_master_preset:
                self._set_master_profile_label(self._match_master_profile_name())
                self._update_master_stack_summary()
            if preset_name_for_label and preset_name_for_label in DETECTION_PRESETS:
                self._log(f"Detection preset: {DETECTION_PRESETS[preset_name_for_label]['label']}")
            elif preset_name_for_label:
                parsed = self._parse_method_size_preset_name(preset_name_for_label)
                if parsed:
                    mode, size_key = parsed
                    mode_label = DETECTION_MODES[mode] if 0 <= mode < len(DETECTION_MODES) else f"Mode {mode}"
                    size_label = TARGET_SIZE_PRESETS[size_key]["label"]
                    self._log(f"Detection preset: {mode_label} / {size_label}")
                else:
                    self._log("Detection preset applied")
            else:
                self._log("Detection preset applied")
        finally:
            self._applying_detection_preset = False

    def _apply_filter_preset(self, preset_name_or_settings: str | dict) -> None:
        # Handle both preset name (string) and direct settings (dict) from master profiles
        if isinstance(preset_name_or_settings, dict):
            settings = preset_name_or_settings
            preset_label = None
            preset_dict = None
        else:
            preset_dict = TARGET_FILTER_PRESETS.get(preset_name_or_settings)
            if not preset_dict:
                return
            settings = preset_dict["settings"]
            preset_label = preset_name_or_settings

        self._applying_filter_preset = True
        try:
            self._spin_min_conf.blockSignals(True)
            self._spin_min_conf.setValue(float(settings["min_confidence"]))
            self._spin_min_conf.blockSignals(False)

            self._spin_min_size.blockSignals(True)
            self._spin_min_size.setValue(float(settings["min_size_ratio"]) * 100.0)
            self._spin_min_size.blockSignals(False)

            self._spin_max_size.blockSignals(True)
            self._spin_max_size.setValue(float(settings["max_size_ratio"]) * 100.0)
            self._spin_max_size.blockSignals(False)

            allowed = {str(name).lower() for name in settings["allowed_classes"]}
            self._class_list.blockSignals(True)
            for i in range(self._class_list.count()):
                item = self._class_list.item(i)
                item.setSelected(item.text().lower() in allowed)
            self._class_list.blockSignals(False)

            if hasattr(self, "_edit_yolo_classes"):
                self._edit_yolo_classes.blockSignals(True)
                self._edit_yolo_classes.setText(", ".join(settings["allowed_classes"]))
                self._edit_yolo_classes.blockSignals(False)

            tf = self.config.target_filter
            tf.allowed_classes = list(settings["allowed_classes"])
            tf.min_confidence = float(settings["min_confidence"])
            tf.min_size_ratio = float(settings["min_size_ratio"])
            tf.max_size_ratio = float(settings["max_size_ratio"])
            tf.shape_filter_enabled = bool(settings.get("shape_filter_enabled", False))
            tf.shape_profile_name = str(settings.get("shape_profile_name", "") or "")
            tf.semantic_min_confirm_frames = int(settings.get("semantic_min_confirm_frames", 1) or 1)
            tf.semantic_min_confirm_confidence = float(settings.get("semantic_min_confirm_confidence", 0.0) or 0.0)
            tf.semantic_confirm_ttl_s = float(settings.get("semantic_confirm_ttl_s", 0.8) or 0.8)
            self._detector.set_yolo_classes(",".join(tf.allowed_classes))
            self._push_config()
            if preset_label:
                self._set_filter_preset_label(preset_label)
            if preset_dict:
                self._log(f"Target Filter preset: {preset_dict['label']}")
            if not self._applying_master_preset:
                self._set_master_profile_label(self._match_master_profile_name())
                self._update_master_stack_summary()
        finally:
            self._applying_filter_preset = False

    def _apply_servo_time_preset(self, preset_name_or_time_ms: str | int) -> None:
        # Handle both preset name (string) and direct move_time_ms (int) from master profiles
        if isinstance(preset_name_or_time_ms, int):
            # Direct move_time_ms value from master profile
            move_time_ms = preset_name_or_time_ms
            preset_label = None
            preset_dict = None
        else:
            preset_dict = BUS_SERVO_TIME_PRESETS.get(preset_name_or_time_ms)
            if not preset_dict:
                return
            move_time_ms = int(preset_dict["move_time_ms"])
            preset_label = preset_name_or_time_ms

        self._applying_servo_preset = True
        try:
            self._spin_servo_time.blockSignals(True)
            self._spin_servo_time.setValue(move_time_ms)
            self._spin_servo_time.blockSignals(False)
            self._on_servo_time_changed(move_time_ms)
            if preset_label:
                self._set_servo_time_preset_label(preset_label)
            if preset_dict:
                self._log(f"Servo move-time preset: {preset_dict['label']} ({move_time_ms} ms)")
            if not self._applying_master_preset:
                self._set_master_profile_label(self._match_master_profile_name())
                self._update_master_stack_summary()
        finally:
            self._applying_servo_preset = False

    def _apply_master_profile(self, preset_name: str) -> None:
        preset = self._get_master_profiles().get(preset_name)
        if not preset:
            return

        self._applying_master_preset = True
        try:
            self._apply_detection_preset(preset["detection"])
            self._apply_filter_preset(preset["filter"])
            self._apply_threat_preset(preset["threat"])
            self._apply_engagement_preset(preset["engagement"])
            self._apply_servo_time_preset(preset["servo"])
            self._active_master_profile_name = preset_name
            self._set_master_profile_label(preset_name)
            self._set_custom_master_profile_edit_target(
                preset_name if preset_name in self._custom_master_profiles else None,
                populate_name=False,
                clear_if_none=False,
            )
            self._update_master_stack_summary()
            self._log(f"Master profile: {preset['label']}")
        finally:
            self._applying_master_preset = False

    def _get_master_profiles(self) -> dict:
        merged = dict(MASTER_PROFILE_PRESETS)
        merged.update(self._custom_master_profiles)
        return merged

    def _rebuild_master_profile_buttons(self) -> None:
        if not hasattr(self, "_master_profiles_grid"):
            return
        grid: QGridLayout = self._master_profiles_grid
        while grid.count():
            item = grid.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        for index, (preset_name, preset) in enumerate(self._get_master_profiles().items()):
            btn = QPushButton(preset["label"])
            self._apply_tooltip(btn, preset.get("tooltip_key", ""))
            btn.clicked.connect(lambda _checked=False, name=preset_name: self._apply_master_profile(name))
            grid.addWidget(btn, index // 2, index % 2)
        self._normalize_preset_grid_button_widths(grid)

    @staticmethod
    def _sanitize_custom_preset_name(name: str) -> str:
        cleaned = "".join(ch.lower() if ch.isalnum() else "_" for ch in name.strip())
        while "__" in cleaned:
            cleaned = cleaned.replace("__", "_")
        return cleaned.strip("_")

    def _custom_master_profile_display_name(self, master_key: str) -> str:
        preset = self._custom_master_profiles.get(master_key, {})
        label = str(preset.get("label", "Custom")).replace("Custom: ", "", 1).strip()
        if label:
            return label
        return str(master_key).replace("custom_master__", "", 1)

    def _selected_custom_master_profile_key(self) -> Optional[str]:
        selected_key = getattr(self, "_selected_custom_master_profile_name", None)
        if selected_key in self._custom_master_profiles:
            return selected_key
        return None

    def _find_custom_master_profile_by_label(self, name: str) -> Optional[str]:
        target = name.strip().lower()
        if not target:
            return None
        for master_key in self._custom_master_profiles.keys():
            if self._custom_master_profile_display_name(master_key).lower() == target:
                return master_key
        return None

    def _make_unique_custom_preset_slug(self, base_slug: str) -> str:
        candidate = base_slug
        suffix = 2
        while f"custom_master__{candidate}" in self._custom_master_profiles:
            candidate = f"{base_slug}_{suffix}"
            suffix += 1
        return candidate

    def _update_custom_master_profile_editor_state(self) -> None:
        selected_key = self._selected_custom_master_profile_key()
        if hasattr(self, "_btn_update_custom_master"):
            self._btn_update_custom_master.setEnabled(selected_key is not None)
        if not hasattr(self, "_lbl_custom_master_info"):
            return
        if selected_key:
            name = self._custom_master_profile_display_name(selected_key)
            self._lbl_custom_master_info.setText(
                f"Editing saved custom preset: {name}. Tune the current stack, then click Update Selected to overwrite it. Click New to clear the editor and Save As New to create another preset."
            )
        else:
            self._lbl_custom_master_info.setText(
                "Select a saved custom preset to edit/update it, or click New and enter a unique preset name to save the current stack as a new coordinated profile."
            )

    def _set_custom_master_profile_edit_target(
        self,
        master_key: Optional[str],
        *,
        populate_name: bool = True,
        clear_if_none: bool = False,
    ) -> None:
        if master_key not in self._custom_master_profiles:
            master_key = None
        self._selected_custom_master_profile_name = master_key
        if hasattr(self, "_combo_custom_master_profiles"):
            combo = self._combo_custom_master_profiles
            combo.blockSignals(True)
            index = combo.findData(master_key or "")
            if index < 0:
                index = 0
            combo.setCurrentIndex(index)
            combo.blockSignals(False)
        if hasattr(self, "_edit_custom_master_name") and populate_name:
            if master_key:
                self._edit_custom_master_name.setText(self._custom_master_profile_display_name(master_key))
            elif clear_if_none:
                self._edit_custom_master_name.clear()
        self._update_custom_master_profile_editor_state()

    def _rebuild_custom_master_profile_combo(self) -> None:
        if not hasattr(self, "_combo_custom_master_profiles"):
            return
        selected_key = self._selected_custom_master_profile_key()
        combo = self._combo_custom_master_profiles
        combo.blockSignals(True)
        combo.clear()
        combo.addItem("New custom preset...", "")
        items = sorted(
            self._custom_master_profiles.items(),
            key=lambda item: self._custom_master_profile_display_name(item[0]).lower(),
        )
        for master_key, _preset in items:
            combo.addItem(self._custom_master_profile_display_name(master_key), master_key)
        index = combo.findData(selected_key or "")
        if index < 0:
            index = 0
        combo.setCurrentIndex(index)
        combo.blockSignals(False)
        self._update_custom_master_profile_editor_state()

    def _on_custom_master_profile_selected(self, index: int) -> None:
        if not hasattr(self, "_combo_custom_master_profiles"):
            return
        master_key = str(self._combo_custom_master_profiles.itemData(index) or "")
        self._set_custom_master_profile_edit_target(master_key or None, populate_name=True, clear_if_none=True)

    def _select_active_custom_master_profile_for_edit(self) -> None:
        matched_name = self._match_master_profile_name()
        target_key = matched_name if matched_name in self._custom_master_profiles else None
        if not target_key:
            self._log("No active custom master preset to edit. Select one from the list or click Save As New.")
            return
        self._set_custom_master_profile_edit_target(target_key, populate_name=True)

    def _clear_custom_master_profile_editor(self) -> None:
        self._set_custom_master_profile_edit_target(None, populate_name=True, clear_if_none=True)

    def _save_new_custom_master_profile(self) -> None:
        self._save_current_custom_master_profile(update_existing=False)

    def _update_selected_custom_master_profile(self) -> None:
        self._save_current_custom_master_profile(update_existing=True)

    def _capture_current_detection_settings(self) -> dict:
        dm = self.config.detection_mode
        return {
            "detection_mode": int(dm.detection_mode),
            "min_contour_area": float(dm.min_contour_area),
            "max_contour_area": float(dm.max_contour_area),
            "yolo_min_area": int(dm.yolo_min_area),
            "yolo_confidence": float(dm.yolo_confidence),
            "color_preset": str(dm.color_preset),
            "color_min_area": int(dm.color_min_area),
            "color_max_area": int(dm.color_max_area),
            "color_fusion_strategy": str(dm.color_fusion_strategy),
            "color_fusion_overlap": int(dm.color_fusion_overlap),
            "motion_ignore_after_move_s": float(dm.motion_ignore_after_move_s),
            "motion_gate_threshold": float(dm.motion_gate_threshold),
        }

    def _capture_current_filter_settings(self) -> dict:
        tf = self.config.target_filter
        return {
            "allowed_classes": [str(c) for c in tf.allowed_classes],
            "min_confidence": float(tf.min_confidence),
            "min_size_ratio": float(tf.min_size_ratio),
            "max_size_ratio": float(tf.max_size_ratio),
            "shape_filter_enabled": bool(getattr(tf, "shape_filter_enabled", False)),
            "shape_profile_name": str(getattr(tf, "shape_profile_name", "") or ""),
            "semantic_min_confirm_frames": int(getattr(tf, "semantic_min_confirm_frames", 1) or 1),
            "semantic_min_confirm_confidence": float(getattr(tf, "semantic_min_confirm_confidence", 0.0) or 0.0),
            "semantic_confirm_ttl_s": float(getattr(tf, "semantic_confirm_ttl_s", 0.8) or 0.8),
        }

    def _capture_current_threat_settings(self) -> dict:
        ts = self.config.threat_scoring
        return {
            "weights": {
                "w_proximity": float(ts.w_proximity),
                "w_size": float(ts.w_size),
                "w_confidence": float(ts.w_confidence),
                "w_class_priority": float(ts.w_class_priority),
                "w_speed": float(ts.w_speed),
                "w_persistence": float(ts.w_persistence),
                "w_approach": float(ts.w_approach),
            },
            "use_ml_model": bool(ts.use_ml_model),
        }

    def _capture_current_engagement_settings(self) -> dict:
        return dict(vars(self.config.engagement))

    def _register_custom_master_profile_bundle(self, slug: str, display_name: str, payload: dict) -> str:
        detection_key = f"custom_det__{slug}"
        filter_key = f"custom_filter__{slug}"
        threat_key = f"custom_threat__{slug}"
        engagement_key = f"custom_engage__{slug}"
        servo_key = f"custom_servo__{slug}"
        master_key = f"custom_master__{slug}"

        DETECTION_PRESETS[detection_key] = {
            "label": f"Custom Detection: {display_name}",
            "description": "User-saved detection snapshot.",
            "tooltip_key": "",
            "settings": dict(payload["detection"]),
        }
        TARGET_FILTER_PRESETS[filter_key] = {
            "label": f"Custom Filter: {display_name}",
            "description": "User-saved target filter snapshot.",
            "tooltip_key": "",
            "settings": dict(payload["filter"]),
        }
        THREAT_AI_PRESETS[threat_key] = {
            "label": f"Custom Threat: {display_name}",
            "description": "User-saved threat scoring snapshot.",
            "tooltip_key": "",
            "weights": dict(payload["threat"]["weights"]),
            "use_ml_model": bool(payload["threat"].get("use_ml_model", False)),
        }
        ENGAGEMENT_PRESETS[engagement_key] = {
            "label": f"Custom Engage: {display_name}",
            "description": "User-saved engagement snapshot.",
            "tooltip_key": "",
            "settings": dict(payload["engagement"]),
        }
        BUS_SERVO_TIME_PRESETS[servo_key] = {
            "label": f"Custom Servo: {display_name}",
            "description": "User-saved bus-servo move time.",
            "tooltip_key": "",
            "move_time_ms": int(payload["servo_move_time_ms"]),
        }

        self._custom_master_profiles[master_key] = {
            "label": f"Custom: {display_name}",
            "description": "User-saved full preset snapshot.",
            "tooltip_key": "",
            "detection": detection_key,
            "filter": filter_key,
            "threat": threat_key,
            "engagement": engagement_key,
            "servo": servo_key,
        }
        return master_key

    def _load_custom_master_profiles(self) -> None:
        self._custom_master_profiles = {}
        path = self._custom_master_preset_path()
        try:
            if not path.exists():
                return
            data = json.loads(path.read_text(encoding="utf-8"))
            profiles = data.get("profiles", {}) if isinstance(data, dict) else {}
            if not isinstance(profiles, dict):
                return
            for slug, entry in profiles.items():
                if not isinstance(entry, dict):
                    continue
                display_name = str(entry.get("name", "")).strip() or str(slug)
                detection = entry.get("detection")
                filter_settings = entry.get("filter")
                threat = entry.get("threat")
                engagement = entry.get("engagement")
                servo_move_time_ms = entry.get("servo_move_time_ms")
                if not all([isinstance(detection, dict), isinstance(filter_settings, dict), isinstance(threat, dict), isinstance(engagement, dict)]):
                    continue
                if not isinstance(servo_move_time_ms, int):
                    continue
                payload = {
                    "detection": detection,
                    "filter": filter_settings,
                    "threat": threat,
                    "engagement": engagement,
                    "servo_move_time_ms": int(servo_move_time_ms),
                }
                self._register_custom_master_profile_bundle(str(slug), display_name, payload)
        except Exception as exc:
            print(f"[SENTRY_V2_TAB] Failed to load custom master presets: {exc}")

    def _save_custom_master_profiles_to_disk(self) -> bool:
        path = self._custom_master_preset_path()
        profiles_out: dict[str, dict] = {}
        for master_key, preset in self._custom_master_profiles.items():
            slug = master_key.replace("custom_master__", "", 1)
            detection_key = preset.get("detection", "")
            filter_key = preset.get("filter", "")
            threat_key = preset.get("threat", "")
            engagement_key = preset.get("engagement", "")
            servo_key = preset.get("servo", "")
            if detection_key not in DETECTION_PRESETS:
                continue
            if filter_key not in TARGET_FILTER_PRESETS:
                continue
            if threat_key not in THREAT_AI_PRESETS:
                continue
            if engagement_key not in ENGAGEMENT_PRESETS:
                continue
            if servo_key not in BUS_SERVO_TIME_PRESETS:
                continue
            label = str(preset.get("label", "Custom")).replace("Custom: ", "", 1)
            profiles_out[slug] = {
                "name": label,
                "detection": dict(DETECTION_PRESETS[detection_key]["settings"]),
                "filter": dict(TARGET_FILTER_PRESETS[filter_key]["settings"]),
                "threat": {
                    "weights": dict(THREAT_AI_PRESETS[threat_key]["weights"]),
                    "use_ml_model": bool(THREAT_AI_PRESETS[threat_key].get("use_ml_model", False)),
                },
                "engagement": dict(ENGAGEMENT_PRESETS[engagement_key]["settings"]),
                "servo_move_time_ms": int(BUS_SERVO_TIME_PRESETS[servo_key]["move_time_ms"]),
            }
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            payload = {
                "version": 1,
                "profiles": profiles_out,
            }
            path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
            return True
        except Exception as exc:
            self._log(f"Failed to save custom presets: {exc}")
            return False

    def _save_current_custom_master_profile(self, update_existing: bool = False) -> None:
        if not hasattr(self, "_edit_custom_master_name"):
            return
        raw_name = self._edit_custom_master_name.text().strip()
        selected_key = self._selected_custom_master_profile_key()

        if update_existing:
            if not selected_key:
                self._log("Custom preset update aborted: select a saved custom preset first")
                return
            display_name = raw_name or self._custom_master_profile_display_name(selected_key)
            duplicate_key = self._find_custom_master_profile_by_label(display_name)
            if duplicate_key and duplicate_key != selected_key:
                self._log("Custom preset update aborted: that name already belongs to another saved custom preset")
                return
            slug = str(selected_key).replace("custom_master__", "", 1)
        else:
            if not raw_name:
                self._log("Custom preset save aborted: enter a preset name to save a new custom preset")
                return
            if self._find_custom_master_profile_by_label(raw_name):
                self._log("Custom preset save aborted: that name already exists. Select it and click Update Selected, or choose a different name")
                return
            slug = self._sanitize_custom_preset_name(raw_name)
            if not slug:
                self._log("Custom preset save aborted: invalid preset name")
                return
            slug = self._make_unique_custom_preset_slug(slug)
            display_name = raw_name

        payload = {
            "detection": self._capture_current_detection_settings(),
            "filter": self._capture_current_filter_settings(),
            "threat": self._capture_current_threat_settings(),
            "engagement": self._capture_current_engagement_settings(),
            "servo_move_time_ms": int(self.config.connection.bus_servo_time_ms),
        }
        master_key = self._register_custom_master_profile_bundle(slug, display_name, payload)
        if not self._save_custom_master_profiles_to_disk():
            return

        self._rebuild_master_profile_buttons()
        self._rebuild_custom_master_profile_combo()
        self._rebuild_servo_time_preset_combo()
        self._active_master_profile_name = master_key
        self._set_master_profile_label(master_key)
        self._set_custom_master_profile_edit_target(master_key, populate_name=True)
        self._update_master_stack_summary()
        if update_existing:
            self._log(f"Updated custom master preset: {display_name}")
        else:
            self._log(f"Saved new custom master preset: {display_name}")

    def _apply_aim_lock_fire_gate_preset(self, preset_name: str) -> None:
        preset = AIM_LOCK_FIRE_GATE_PRESETS.get(preset_name)
        if not preset:
            return

        settings = preset["settings"]
        widgets = [
            (self._spin_deadzone_pan, settings["precision_deadzone_pan_deg"]),
            (self._spin_deadzone_tilt, settings["precision_deadzone_tilt_deg"]),
            (self._spin_error_ema, settings["precision_error_ema"]),
            (self._spin_aim_lock_pan, settings["aim_lock_pan_tolerance"]),
            (self._spin_aim_lock_tilt, settings["aim_lock_tilt_tolerance"]),
            (self._spin_aim_lock_frames, settings["aim_lock_required_frames"]),
            (self._spin_fire_enter_pan, settings["fire_trigger_enter_pan_tolerance"]),
            (self._spin_fire_enter_tilt, settings["fire_trigger_enter_tilt_tolerance"]),
            (self._spin_fire_exit_pan, settings["fire_trigger_exit_pan_tolerance"]),
            (self._spin_fire_exit_tilt, settings["fire_trigger_exit_tilt_tolerance"]),
            (self._spin_recenter_pan, settings["fire_recenter_pan_tolerance"]),
            (self._spin_recenter_tilt, settings["fire_recenter_tilt_tolerance"]),
            (self._spin_target_loss_timeout, settings["target_loss_timeout"]),
        ]
        for widget, value in widgets:
            widget.blockSignals(True)
            widget.setValue(value)
            widget.blockSignals(False)

        eg = self.config.engagement
        for key, value in settings.items():
            setattr(eg, key, value)
        self._on_engagement_changed()
        self._log(f"Aim lock/fire gate preset: {preset['label']}")

    def _apply_engagement_preset(self, preset_name_or_settings: str | dict) -> None:
        # Handle both preset name (string) and direct settings (dict) from master profiles
        if isinstance(preset_name_or_settings, dict):
            settings = preset_name_or_settings
            preset_label = None
            preset_log_label = "custom/master settings"
        else:
            preset = ENGAGEMENT_PRESETS.get(preset_name_or_settings)
            if not preset:
                return
            settings = self._resolved_engagement_preset_settings(preset)
            preset_label = preset_name_or_settings
            preset_log_label = str(preset["label"])

        self._applying_engagement_preset = True
        try:
            self._chk_auto_trigger.blockSignals(True)
            self._chk_auto_trigger.setChecked(bool(settings["auto_trigger_enabled"]))
            self._chk_auto_trigger.blockSignals(False)

            self._combo_trigger_mode.blockSignals(True)
            self._combo_trigger_mode.setCurrentIndex(1 if settings["trigger_mode_bb"] else 0)
            self._combo_trigger_mode.blockSignals(False)
            self._apply_trigger_servo_widget_values_from_settings(settings)

            widget_values = [
                (self._spin_min_threat, settings["min_threat_score"]),
                (self._spin_burst, settings["burst_count"]),
                (self._spin_burst_interval, settings["burst_interval_ms"]),
                (self._spin_inter_cd, settings["inter_target_cooldown"]),
                (self._spin_cycle_cd, settings["cycle_cooldown"]),
                (self._spin_max_queue, settings["max_queue_length"]),
                (self._slider_speed, settings["engagement_speed"]),
                (self._spin_prec_settle, settings["precision_settle_time"]),
                (self._spin_prec_step, settings["precision_max_step"]),
                (self._spin_deadzone_pan, settings.get("precision_deadzone_pan_deg", self.config.engagement.precision_deadzone_pan_deg)),
                (self._spin_deadzone_tilt, settings.get("precision_deadzone_tilt_deg", self.config.engagement.precision_deadzone_tilt_deg)),
                (self._spin_error_ema, settings.get("precision_error_ema", self.config.engagement.precision_error_ema)),
                (self._spin_aim_lock_pan, settings.get("aim_lock_pan_tolerance", self.config.engagement.aim_lock_pan_tolerance)),
                (self._spin_aim_lock_tilt, settings.get("aim_lock_tilt_tolerance", self.config.engagement.aim_lock_tilt_tolerance)),
                (self._spin_aim_lock_frames, settings.get("aim_lock_required_frames", self.config.engagement.aim_lock_required_frames)),
                (self._spin_fire_enter_pan, settings.get("fire_trigger_enter_pan_tolerance", self.config.engagement.fire_trigger_enter_pan_tolerance)),
                (self._spin_fire_enter_tilt, settings.get("fire_trigger_enter_tilt_tolerance", self.config.engagement.fire_trigger_enter_tilt_tolerance)),
                (self._spin_fire_exit_pan, settings.get("fire_trigger_exit_pan_tolerance", self.config.engagement.fire_trigger_exit_pan_tolerance)),
                (self._spin_fire_exit_tilt, settings.get("fire_trigger_exit_tilt_tolerance", self.config.engagement.fire_trigger_exit_tilt_tolerance)),
                (self._spin_recenter_pan, settings.get("fire_recenter_pan_tolerance", self.config.engagement.fire_recenter_pan_tolerance)),
                (self._spin_recenter_tilt, settings.get("fire_recenter_tilt_tolerance", self.config.engagement.fire_recenter_tilt_tolerance)),
                (self._spin_target_loss_timeout, settings.get("target_loss_timeout", self.config.engagement.target_loss_timeout)),
            ]
            for widget, value in widget_values:
                widget.blockSignals(True)
                widget.setValue(value)
                widget.blockSignals(False)

            self._lbl_speed.setText(str(int(settings["engagement_speed"])))

            self._chk_optimize.blockSignals(True)
            self._chk_optimize.setChecked(bool(settings["optimize_slew_order"]))
            self._chk_optimize.blockSignals(False)

            self._chk_precision.blockSignals(True)
            self._chk_precision.setChecked(bool(settings["precision_aim_enabled"]))
            self._chk_precision.blockSignals(False)

            self._chk_continuous_hunt_loss.blockSignals(True)
            self._chk_continuous_hunt_loss.setChecked(
                bool(settings.get("continuous_hunt_on_loss", self.config.engagement.continuous_hunt_on_loss))
            )
            self._chk_continuous_hunt_loss.blockSignals(False)

            eg = self.config.engagement
            for key, value in settings.items():
                setattr(eg, key, value)
            self._comm.trigger_mode_bb = bool(settings["trigger_mode_bb"])
            self._sync_comm_runtime_settings_from_config()
            self._sync_single_target_ui()
            self._on_engagement_changed()
            self._queue_runtime_trigger_config_if_connected()
            if preset_label:
                self._set_engagement_preset_label(preset_label)
            if not self._applying_master_preset:
                self._set_master_profile_label(self._match_master_profile_name())
                self._update_master_stack_summary()
            self._log(f"Engagement preset: {preset_log_label}")
        finally:
            self._applying_engagement_preset = False

    def _start_fire_burst(self, pan: float, tilt: float, burst_count: int, interval_ms: int) -> None:
        self._stop_fire_burst(send_release=True)
        self._burst_pan = pan
        self._burst_tilt = tilt
        self._burst_remaining = max(1, int(burst_count))
        self._burst_interval_ms = max(10, int(interval_ms))
        self._burst_phase_on = True
        self._queue_comm_task("send_command", self._burst_pan, self._burst_tilt, fire=1)
        self._burst_timer.start(self._burst_interval_ms)

    def _advance_fire_burst(self) -> None:
        if self._burst_remaining <= 0:
            self._stop_fire_burst(send_release=False)
            return

        if self._burst_phase_on:
            self._queue_comm_task("send_command", self._burst_pan, self._burst_tilt, fire=0)
            self._burst_remaining -= 1
            if self._burst_remaining <= 0:
                self._stop_fire_burst(send_release=False)
                return
            self._burst_phase_on = False
            self._burst_timer.start(self._burst_interval_ms)
            return

        self._burst_phase_on = True
        self._queue_comm_task("send_command", self._burst_pan, self._burst_tilt, fire=1)
        self._burst_timer.start(self._burst_interval_ms)

    def _stop_fire_burst(self, *, send_release: bool) -> None:
        self._burst_timer.stop()
        if send_release and self._burst_phase_on and not self._closing:
            self._queue_comm_task("send_command", self._burst_pan, self._burst_tilt, fire=0)
        self._burst_remaining = 0
        self._burst_phase_on = False

    def _queue_move_command(
        self,
        pan: float,
        tilt: float,
        *,
        fire: int = 0,
        move_time_ms: Optional[int] = None,
        manual_override: bool = False,
        allow_rest_tilt: bool = False,
    ) -> None:
        if self._closing:
            return
        # CHANGE WARNING: automatic motion-disable must not strand manual recovery controls.
        if not self._pan_tilt_motion_enabled and not manual_override:
            return
        move_time = int(self._get_manual_move_time_ms() if move_time_ms is None else move_time_ms)
        queued_move = (float(pan), float(tilt), int(fire), move_time, bool(manual_override), bool(allow_rest_tilt))
        now = time.time()
        with self._pending_move_lock:
            if manual_override:
                # CHANGE WARNING: manual arrows/Home/Move to Guard share this
                # worker with engine tracking slews. Keep manual recovery moves
                # briefly dominant so a live tracking frame cannot overwrite them
                # before they are sent to the Debug Board.
                self._manual_move_priority_until = max(
                    self._manual_move_priority_until,
                    now + float(getattr(self, "_manual_position_hold_s", 1.25) or 1.25),
                )
                if self._pending_move_commands:
                    self._pending_move_commands = deque(
                        cmd for cmd in self._pending_move_commands if bool(cmd[4])
                    )
                self._pending_move_commands.append(queued_move)
            else:
                if now < self._manual_move_priority_until:
                    return
                if self._pending_move_commands and not bool(self._pending_move_commands[-1][4]):
                    self._pending_move_commands[-1] = queued_move
                else:
                    self._pending_move_commands.append(queued_move)

            while len(self._pending_move_commands) > 6:
                self._pending_move_commands.popleft()

    def _queue_comm_task(self, task_name: str, *args, **kwargs) -> None:
        if self._closing:
            return
        try:
            self._comm_task_queue.put_nowait((task_name, args, kwargs))
        except Exception as exc:
            self._report_runtime_warning(f"Comm task enqueue failed ({task_name})", exc)

    def _comm_worker_loop(self) -> None:
        while not self._comm_worker_stop.is_set():
            task = None
            try:
                task = self._comm_task_queue.get(timeout=0.03)
            except queue.Empty:
                task = None
            except Exception:
                task = None

            if task is None:
                if self._comm_worker_stop.is_set():
                    break
            else:
                try:
                    task_name, args, kwargs = task
                    self._execute_comm_task(task_name, *args, **kwargs)
                except Exception as exc:
                    self.command_result_ready.emit("task", False, str(exc))

            move_command = None
            with self._pending_move_lock:
                if self._pending_move_commands:
                    move_command = self._pending_move_commands.popleft()
            if move_command is not None and not self._closing:
                try:
                    pan, tilt, fire, move_time, _manual_override, _allow_rest_tilt = move_command
                    if int(fire) != 0:
                        ok = self._comm.send_command(pan, tilt, fire=fire, move_time_ms=move_time, allow_rest_tilt=_allow_rest_tilt)
                        detail = getattr(self._comm, "_last_error", "") or ""
                        if ok and _manual_override:
                            detail = getattr(self._comm, "_last_cmd", "") or ""
                    else:
                        ok = self._comm.send_movement(pan, tilt, move_time_ms=move_time, allow_rest_tilt=_allow_rest_tilt)
                        detail = ""
                        if _manual_override:
                            detail = getattr(self._comm, "_last_cmd", "") or ""
                        if not ok:
                            detail = getattr(self._comm, "_last_error", "") or "movement command failed"
                    self.command_result_ready.emit(
                        "move",
                        bool(ok),
                        detail,
                    )
                except Exception as exc:
                    self.command_result_ready.emit("move", False, str(exc))

    def _execute_comm_task(self, task_name: str, *args, **kwargs) -> None:
        if task_name == "send_command":
            ok = self._comm.send_command(*args, **kwargs)
            self.command_result_ready.emit(
                task_name,
                bool(ok),
                getattr(self._comm, "_last_error", "") or getattr(self._comm, "_last_cmd", "") or "",
            )
            return
        if task_name == "set_led":
            ok = self._comm.set_led(*args, **kwargs)
            self.command_result_ready.emit("set_led", bool(ok), getattr(self._comm, "_last_error", "") or "")
            return
        if task_name == "set_led_pwm":
            ok = self._comm.set_led_pwm(*args, **kwargs)
            self.command_result_ready.emit("set_led_pwm", bool(ok), getattr(self._comm, "_last_error", "") or "")
            return
        if task_name == "set_laser":
            ok = self._comm.set_laser(*args, **kwargs)
            self.command_result_ready.emit("set_laser", bool(ok), getattr(self._comm, "_last_error", "") or "")
            return
        if task_name == "set_acc":
            ok = self._comm.set_acc(*args, **kwargs)
            self.command_result_ready.emit("set_acc", bool(ok), getattr(self._comm, "_last_error", "") or "")
            return
        if task_name == "set_spare":
            ok = self._comm.set_spare(*args, **kwargs)
            self.command_result_ready.emit("set_spare", bool(ok), getattr(self._comm, "_last_error", "") or "")
            return
        if task_name == "set_safety":
            ok = self._comm.set_safety(*args, **kwargs)
            self.command_result_ready.emit("set_safety", bool(ok), getattr(self._comm, "_last_error", "") or "")
            return
        if task_name == "set_control_source_mode":
            ok = self._comm.set_control_source_mode(*args, **kwargs)
            self.command_result_ready.emit("set_control_source_mode", bool(ok), getattr(self._comm, "_last_error", "") or getattr(self._comm, "_last_cmd", "") or "")
            return
        if task_name == "send_pir_enabled":
            ok = self._comm.send_pir_enabled(*args, **kwargs)
            self.command_result_ready.emit("send_pir_enabled", bool(ok), getattr(self._comm, "_last_error", "") or getattr(self._comm, "_last_cmd", "") or "")
            return
        if task_name == "send_sweep":
            ok = self._comm.send_sweep(*args, **kwargs)
            self.command_result_ready.emit("send_sweep", bool(ok), getattr(self._comm, "_last_error", "") or getattr(self._comm, "_last_cmd", "") or "")
            return
        if task_name == "send_sound":
            ok = self._comm.send_sound(*args, **kwargs)
            self.command_result_ready.emit("send_sound", bool(ok), getattr(self._comm, "_last_error", "") or getattr(self._comm, "_last_cmd", "") or "")
            return
        if task_name == "send_trigger_runtime_config":
            ok = self._comm.send_trigger_runtime_config(*args, **kwargs)
            self.command_result_ready.emit("send_trigger_runtime_config", bool(ok), getattr(self._comm, "_last_error", "") or getattr(self._comm, "_last_cmd", "") or "")
            return
        if task_name == "refresh_wifi_runtime_link":
            host = str(args[0]) if len(args) >= 1 else str(self.config.connection.udp_host or "192.168.4.1")
            port = int(args[1]) if len(args) >= 2 else int(self.config.connection.udp_port or 9000)
            pir_enabled = bool(args[2]) if len(args) >= 3 else bool(self.config.pir_guard.pir_enabled)
            ok = self._comm.refresh_primary_udp_link(host, port)
            detail = getattr(self._comm, "_last_error", "") or getattr(self._comm, "_last_cmd", "") or ""
            if ok:
                self._comm.send_trigger_runtime_config()
                self._comm.send_pir_enabled(pir_enabled)
                detail = f"WiFi runtime link refreshed: {host}:{port}"
            self.command_result_ready.emit("refresh_wifi_runtime_link", bool(ok), detail)
            return

    def _update_last_command_label(self, cmd_text: str) -> None:
        text = str(cmd_text or "").strip()
        if not text:
            return
        self._last_visible_command_text = text
        if hasattr(self, "_lbl_last_cmd") and self._lbl_last_cmd is not None:
            self._set_label_content(self._lbl_last_cmd, f"Last: {text}", self._compact_status_style("neutral"))

    def _on_command_result_ready(self, command_name: str, ok: bool, detail: str) -> None:
        if self._closing:
            return
        if command_name == "refresh_wifi_runtime_link":
            self._wifi_runtime_refresh_inflight = False
        if ok:
            if detail:
                self._update_last_command_label(detail)
            if command_name == "refresh_wifi_runtime_link":
                self._log(str(detail or "WiFi runtime link refreshed"))
            return
        detail_text = str(detail or "command failed")
        if command_name == "move":
            if not self._host_controls_hardware() and not self._comm.is_connected():
                self._log("Move skipped: hardware is not connected yet")
                return
            self._log(f"Move failed: {detail_text}")
        elif command_name == "refresh_wifi_runtime_link":
            self._log(f"WiFi runtime refresh failed: {detail_text}")
        else:
            self._log(f"{command_name} failed: {detail_text}")

    def _push_config(self) -> None:
        """Push current config to engine, overlay, and detector."""
        self.engine.update_config(self.config)
        self.overlay.update_config(self.config)
        self._sync_detector_params()

    def _sync_detector_params(self) -> None:
        """Synchronize detector parameters from current config."""
        dm = self.config.detection_mode
        d = self._detector
        d.min_contour = dm.min_contour_area
        d.max_contour = dm.max_contour_area
        d.yolo_min_area = dm.yolo_min_area
        d.yolo_confidence = dm.yolo_confidence
        d.motion_gate_threshold = dm.motion_gate_threshold
        d.color_preset = dm.color_preset
        d.color_min_area = dm.color_min_area
        d.color_max_area = dm.color_max_area
        d.color_fusion_strategy = dm.color_fusion_strategy
        d.color_fusion_overlap = dm.color_fusion_overlap
        d.custom_hsv_lower = (dm.custom_h_min, dm.custom_s_min, dm.custom_v_min)
        d.custom_hsv_upper = (dm.custom_h_max, dm.custom_s_max, dm.custom_v_max)
        d.set_yolo_classes(",".join(self.config.target_filter.allowed_classes))

    def _clamp_manual_angles(self, pan: float, tilt: float, *, allow_rest_tilt: bool = False) -> Tuple[float, float]:
        g = self.config.guard
        pan_min, pan_max = sorted((g.pan_min, g.pan_max))
        if allow_rest_tilt:
            tilt_min, tilt_max = SENTRY_TILT_MIN, SENTRY_TILT_MAX
        else:
            tilt_min, tilt_max = sorted((g.tilt_min, g.tilt_max))
        return (
            max(pan_min, min(pan_max, pan)),
            max(tilt_min, min(tilt_max, tilt)),
        )

    def _sync_engine_pose_from_feedback(self) -> None:
        # CHANGE WARNING: Precision aiming uses engine.current_pan/current_tilt as
        # its live reference. Do not overwrite that reference with delayed bus-servo
        # readback while a new commanded move is still in flight, or the precision
        # loop will chase stale feedback and oscillate.
        feedback = self._comm.get_servo_feedback_snapshot()
        feedback_age = feedback.get("age_s")
        feedback_pan = feedback.get("pan_deg")
        feedback_tilt = feedback.get("tilt_deg")
        if feedback_pan is None or feedback_tilt is None or feedback_age is None:
            return
        if float(feedback_age) > 1.0:
            return
        now = time.time()
        commanded_pan = float(getattr(self, "_last_commanded_pan", feedback_pan))
        commanded_tilt = float(getattr(self, "_last_commanded_tilt", feedback_tilt))
        command_age_s = now - float(getattr(self, "_last_commanded_pose_time_s", 0.0) or 0.0)
        move_time_s = max(0.0, float(getattr(self, "_last_commanded_move_time_ms", 0) or 0) / 1000.0)
        settle_window_s = max(0.18, min(1.25, move_time_s + 0.18))
        feedback_to_command_err = max(
            abs(float(feedback_pan) - commanded_pan),
            abs(float(feedback_tilt) - commanded_tilt),
        )
        if command_age_s < settle_window_s and feedback_to_command_err > 1.5:
            return
        pan, tilt = self._clamp_manual_angles(float(feedback_pan), float(feedback_tilt))
        self.engine.current_pan = pan
        self.engine.current_tilt = tilt

    def _remember_commanded_position(self, pan: float, tilt: float, *, move_time_ms: Optional[int] = None) -> None:
        self._last_commanded_pan = float(pan)
        self._last_commanded_tilt = float(tilt)
        self._last_commanded_pose_time_s = time.time()
        if move_time_ms is not None:
            self._last_commanded_move_time_ms = max(0, int(move_time_ms))

    def _tracking_move_settle_window_s(self, move_time_ms: int) -> float:
        commanded_s = max(0.0, float(move_time_ms) / 1000.0)
        return max(0.09, min(0.42, (commanded_s * 0.82) + 0.03))

    def _resync_engine_pose_after_deferred_move(self) -> None:
        feedback = self._comm.get_servo_feedback_snapshot()
        if bool(feedback.get("active")) and str(feedback.get("source") or "") == "debug-board":
            feedback_pan = feedback.get("pan_deg")
            feedback_tilt = feedback.get("tilt_deg")
            feedback_age = feedback.get("age_s")
            try:
                feedback_age_s = float(feedback_age) if feedback_age is not None else 999.0
            except Exception:
                feedback_age_s = 999.0
            if feedback_pan is not None and feedback_tilt is not None and feedback_age_s <= 1.2:
                pan, tilt = self._clamp_manual_angles(float(feedback_pan), float(feedback_tilt))
                self.engine.current_pan = pan
                self.engine.current_tilt = tilt
                return
        pan, tilt = self._clamp_manual_angles(
            float(getattr(self, "_last_commanded_pan", self.engine.current_pan)),
            float(getattr(self, "_last_commanded_tilt", self.engine.current_tilt)),
        )
        self.engine.current_pan = pan
        self.engine.current_tilt = tilt

    def _should_defer_auto_move(self, move_time_ms: int, move_delta: float) -> bool:
        if self._host_controls_hardware():
            return False

        if self._engine_pir_motion_active():
            return False

        preview_window_s = max(self._display_frame_interval_s * 1.15, 0.08)
        if self.engine.state == SentryV2State.ENGAGING:
            if not self._should_defer_tracking_move(move_time_ms):
                return False
            if move_delta <= 1.2:
                return True

        commanded_at = float(getattr(self, "_last_commanded_pose_time_s", 0.0) or 0.0)
        if commanded_at <= 0.0:
            return False

        now = time.time()
        command_age_s = max(0.0, now - commanded_at)
        settle_window_s = max(
            self._tracking_move_settle_window_s(int(move_time_ms)),
            preview_window_s,
        )
        if self.engine.state != SentryV2State.ENGAGING or move_delta >= 1.2:
            settle_window_s = max(settle_window_s, min(0.58, (float(move_time_ms) / 1000.0) + 0.08))
        if command_age_s >= settle_window_s:
            return False

        feedback = self._comm.get_servo_feedback_snapshot()
        if not bool(feedback.get("active")):
            return move_delta >= 0.9 and command_age_s < preview_window_s
        if str(feedback.get("source") or "") != "debug-board":
            return move_delta >= 0.9 and command_age_s < preview_window_s

        feedback_age = feedback.get("age_s")
        if feedback_age is None:
            return True
        try:
            feedback_age_s = float(feedback_age)
        except Exception:
            feedback_age_s = 999.0
        if feedback_age_s > 0.45:
            return True

        feedback_pan = feedback.get("pan_deg")
        feedback_tilt = feedback.get("tilt_deg")
        if feedback_pan is None or feedback_tilt is None:
            return True

        commanded_pan = float(getattr(self, "_last_commanded_pan", feedback_pan))
        commanded_tilt = float(getattr(self, "_last_commanded_tilt", feedback_tilt))
        remaining_error = max(
            abs(float(feedback_pan) - commanded_pan),
            abs(float(feedback_tilt) - commanded_tilt),
        )
        tolerance = 0.85 if self.engine.state == SentryV2State.ENGAGING else 0.55
        if move_delta >= 2.5:
            tolerance = max(tolerance, 0.95)
        elif move_delta >= 1.2:
            tolerance = max(tolerance, 0.70)
        return remaining_error > tolerance

    def _should_defer_tracking_move(self, move_time_ms: int) -> bool:
        if self._host_controls_hardware():
            return False
        if self.engine.state != SentryV2State.ENGAGING:
            return False

        commanded_at = float(getattr(self, "_last_commanded_pose_time_s", 0.0) or 0.0)
        if commanded_at <= 0.0:
            return False

        now = time.time()
        command_age_s = max(0.0, now - commanded_at)
        settle_window_s = self._tracking_move_settle_window_s(int(move_time_ms))
        if command_age_s >= settle_window_s:
            return False

        feedback = self._comm.get_servo_feedback_snapshot()
        if not bool(feedback.get("active")):
            return False
        if str(feedback.get("source") or "") != "debug-board":
            return False

        feedback_age = feedback.get("age_s")
        if feedback_age is None:
            return True

        try:
            feedback_age_s = float(feedback_age)
        except Exception:
            feedback_age_s = 999.0
        if feedback_age_s > 0.35:
            return True

        feedback_pan = feedback.get("pan_deg")
        feedback_tilt = feedback.get("tilt_deg")
        if feedback_pan is None or feedback_tilt is None:
            return True

        commanded_pan = float(getattr(self, "_last_commanded_pan", feedback_pan))
        commanded_tilt = float(getattr(self, "_last_commanded_tilt", feedback_tilt))
        remaining_error = max(
            abs(float(feedback_pan) - commanded_pan),
            abs(float(feedback_tilt) - commanded_tilt),
        )
        return remaining_error > 0.85

    def _get_command_delta(self, pan: float, tilt: float) -> float:
        prev_pan = float(getattr(self, "_last_commanded_pan", pan))
        prev_tilt = float(getattr(self, "_last_commanded_tilt", tilt))
        return float(max(abs(float(pan) - prev_pan), abs(float(tilt) - prev_tilt)))

    def _get_manual_move_time_ms(self) -> int:
        return int(max(70, int(self.config.connection.bus_servo_time_ms)))

    def _get_tracking_move_time_ms(self, move_delta: float) -> int:
        base_time = int(max(20, int(self.config.connection.bus_servo_time_ms)))
        speed_value = int(np.clip(self.config.engagement.engagement_speed, 10, 100))

        # Manual move-time should still influence tracking, but it should not act
        # as a hard floor or all presets collapse toward the same slow feel.
        dynamic_time = int(round(np.interp(speed_value, [10, 100], [145, 16])))
        manual_influence = float(np.interp(speed_value, [10, 100], [1.00, 0.18]))
        tracking_time = int(round(dynamic_time + ((base_time - 20) * manual_influence)))

        if move_delta <= 0.8:
            tracking_time = max(tracking_time, int(round(np.interp(speed_value, [10, 100], [92, 28]))))
        elif move_delta <= 2.5:
            tracking_time = max(tracking_time, int(round(np.interp(speed_value, [10, 100], [70, 20]))))

        return int(max(16, min(220, tracking_time)))

    def _get_tracking_motion_suppression_s(self, move_delta: float) -> float:
        mode = int(self.config.detection_mode.detection_mode)
        motion_sensitive_modes = {0, 1, 3, 4, 5, 7, 8, 10}
        if mode not in motion_sensitive_modes:
            return 0.0
        base_suppression = float(max(0.0, self.config.detection_mode.motion_ignore_after_move_s))
        if move_delta <= 0.35:
            return 0.0
        if mode in {7, 8}:
            # Keep hybrid color modes responsive while still suppressing obvious self-motion.
            if move_delta <= 1.0:
                return min(base_suppression, 0.015)
            if move_delta <= 2.5:
                return min(base_suppression, 0.025)
            return min(base_suppression, 0.04)
        if mode == 10:
            if move_delta <= 1.0:
                return min(base_suppression, 0.03)
            if move_delta <= 2.5:
                return min(base_suppression, 0.05)
            return min(base_suppression, 0.07)
        if move_delta <= 1.0:
            return min(base_suppression, 0.04)
        if move_delta <= 2.5:
            return min(base_suppression, 0.06)
        return min(base_suppression, 0.09)

    def _queue_sound_tone(self, freq_hz: int, duration_ms: int) -> None:
        if self._closing or self._host_controls_hardware():
            return
        if not bool(getattr(self.config.sound, "enabled", True)):
            return
        if self._buzzer_suppressed_for_human_voice():
            return
        volume_pct = self._sound_volume_pct()
        if volume_pct <= 0:
            return
        if not self._comm.can_send_sound():
            now = time.time()
            if now - float(getattr(self, "_last_sound_transport_warn_s", 0.0) or 0.0) >= 5.0:
                self._last_sound_transport_warn_s = now
                self._log(self._comm.sound_transport_info())
            return
        self._queue_comm_task("send_sound", int(freq_hz), int(duration_ms), volume_pct)

    def _human_voice_supported(self) -> bool:
        return bool(QTextToSpeech is not None and getattr(self, "_speech_available", False))

    def _mute_buzzer_for_human_voice_enabled(self) -> bool:
        return bool(getattr(self.config.sound, "mute_buzzer_when_human_voice_enabled", True))

    def _buzzer_suppressed_for_human_voice(self) -> bool:
        return bool(self._mute_buzzer_for_human_voice_enabled() and getattr(self.config.sound, "human_voice_enabled", False))

    def _human_voice_name(self) -> str:
        return str(getattr(self.config.sound, "human_voice_name", "") or "").strip()

    def _human_voice_backend_summary(self) -> str:
        engine = getattr(self, "_speech_engine", None)
        if engine is None or QTextToSpeech is None:
            return "unavailable"
        try:
            engines = list(engine.availableEngines() or [])
        except Exception:
            engines = []
        return ", ".join(str(item) for item in engines if str(item).strip()) or "no backend reported"

    def _human_voice_style_key(self) -> str:
        style = str(getattr(self.config.sound, "human_voice_style", "neutral") or "neutral").strip().lower()
        return style if style in HUMAN_VOICE_STYLE_PRESETS else "neutral"

    def _human_voice_rate_pct(self) -> int:
        return int(max(50, min(150, int(getattr(self.config.sound, "human_voice_rate_pct", 100) or 100))))

    def _human_voice_pitch_pct(self) -> int:
        return int(max(50, min(150, int(getattr(self.config.sound, "human_voice_pitch_pct", 100) or 100))))

    def _human_voice_volume_pct(self) -> int:
        return int(max(0, min(100, int(getattr(self.config.sound, "human_voice_volume_pct", 85) or 85))))

    def _apply_human_voice_style(self, style_key: str, *, save: bool = True) -> None:
        normalized = str(style_key or "neutral").strip().lower()
        preset = HUMAN_VOICE_STYLE_PRESETS.get(normalized, HUMAN_VOICE_STYLE_PRESETS["neutral"])
        self.config.sound.human_voice_style = normalized if normalized in HUMAN_VOICE_STYLE_PRESETS else "neutral"
        self.config.sound.human_voice_rate_pct = int(preset["rate"])
        self.config.sound.human_voice_pitch_pct = int(preset["pitch"])
        self.config.sound.human_voice_volume_pct = int(preset["volume"])
        self._sync_sound_widgets()
        if save:
            self._save_config_quietly()

    def _set_human_voice_runtime_state(self, label: str) -> None:
        self._speech_state_label = str(label or "waiting").strip() or "waiting"
        if hasattr(self, "_lbl_human_voice_status"):
            self._sync_sound_widgets()

    def _refresh_human_voice_diagnostics(self) -> None:
        if hasattr(self, "_lbl_human_voice_diag_backend"):
            self._lbl_human_voice_diag_backend.setText(f"Backend: {self._human_voice_backend_summary()}")
        engine = getattr(self, "_speech_engine", None)
        actual_voice = ""
        if engine is not None and hasattr(engine, "voice"):
            try:
                actual_voice = str(engine.voice().name() or "").strip()
            except Exception:
                actual_voice = ""
        selected_voice = self._human_voice_name() or (self._speech_voice_names[0] if self._speech_voice_names else "default voice")
        if hasattr(self, "_lbl_human_voice_diag_selected"):
            if actual_voice and actual_voice != selected_voice:
                self._lbl_human_voice_diag_selected.setText(f"Selected voice: {selected_voice} | engine voice: {actual_voice}")
            else:
                self._lbl_human_voice_diag_selected.setText(f"Selected voice: {actual_voice or selected_voice}")
        if hasattr(self, "_lbl_human_voice_diag_state"):
            route_mode = "buzzer muted" if self._buzzer_suppressed_for_human_voice() else "buzzer allowed"
            self._lbl_human_voice_diag_state.setText(
                f"Speech state: {getattr(self, '_speech_state_label', 'waiting')} | Human voice {'ON' if getattr(self.config.sound, 'human_voice_enabled', False) else 'OFF'} | {route_mode}"
            )
        if hasattr(self, "_lbl_human_voice_diag_route"):
            route_note = "Windows SAPI uses the current default playback device"
            if self._buzzer_suppressed_for_human_voice():
                route_note += " | ESP32 buzzer is intentionally muted while human voice mode is enabled"
            self._lbl_human_voice_diag_route.setText(f"Route: {route_note}")
        if hasattr(self, "_lbl_ai_voice_validation_status"):
            auto_speak = bool(getattr(self.config.ai_assistant, "auto_speak_responses", False))
            human_voice_enabled = bool(getattr(self.config.sound, "human_voice_enabled", False))
            selected_voice = self._human_voice_name() or (self._speech_voice_names[0] if self._speech_voice_names else "default voice")
            if not self._human_voice_supported():
                readiness = "unavailable"
            elif auto_speak and human_voice_enabled:
                readiness = "ready"
            elif auto_speak and not human_voice_enabled:
                readiness = "auto-speak armed but human voice is off"
            elif human_voice_enabled:
                readiness = "manual speech only"
            else:
                readiness = "text-only"
            self._lbl_ai_voice_validation_status.setText(
                f"AI voice route: {readiness} | auto-speak {'ON' if auto_speak else 'OFF'} | voice {selected_voice}"
            )

    def _on_human_speech_state_changed(self, state: object) -> None:
        if QTextToSpeech is None:
            return
        ready_state = getattr(QTextToSpeech, "Ready", None)
        speaking_state = getattr(QTextToSpeech, "Speaking", None)
        paused_state = getattr(QTextToSpeech, "Paused", None)
        backend_error_state = getattr(QTextToSpeech, "BackendError", None)
        if state == speaking_state:
            self._set_human_voice_runtime_state("speaking")
        elif state == paused_state:
            self._set_human_voice_runtime_state("paused")
        elif state == backend_error_state:
            self._set_human_voice_runtime_state("error")
            self._log("Human voice backend reported an error while trying to speak")
        elif state == ready_state:
            self._set_human_voice_runtime_state("ready")

    def _init_human_speech_engine(self) -> None:
        self._speech_available = False
        self._speech_voice_names = []
        if QTextToSpeech is None:
            self._speech_state_label = "unavailable"
            return
        try:
            self._speech_engine = QTextToSpeech(self)
            self._speech_available = bool(self._speech_engine.availableEngines())
            self._speech_voice_names = [str(voice.name()) for voice in list(self._speech_engine.availableVoices() or []) if str(voice.name()).strip()]
            if hasattr(self._speech_engine, "stateChanged"):
                self._speech_engine.stateChanged.connect(self._on_human_speech_state_changed)
            self._speech_state_label = "ready" if self._speech_available else "unavailable"
            self._sync_human_speech_engine()
        except Exception:
            self._speech_engine = None
            self._speech_available = False
            self._speech_voice_names = []
            self._speech_state_label = "unavailable"

    def _sync_human_speech_engine(self) -> None:
        engine = getattr(self, "_speech_engine", None)
        if engine is None:
            return
        try:
            voices = list(engine.availableVoices() or [])
            if voices and self._human_voice_name():
                target = self._human_voice_name().lower()
                for voice in voices:
                    if str(voice.name()).strip().lower() == target:
                        engine.setVoice(voice)
                        break
            engine.setRate((float(self._human_voice_rate_pct()) - 100.0) / 50.0)
            engine.setPitch((float(self._human_voice_pitch_pct()) - 100.0) / 50.0)
            engine.setVolume(float(self._human_voice_volume_pct()) / 100.0)
        except Exception:
            pass

    def _stop_human_speech(self) -> None:
        engine = getattr(self, "_speech_engine", None)
        if engine is None:
            return
        try:
            engine.stop()
            self._speech_state_label = "ready"
        except Exception:
            pass

    def _speak_human_phrase(self, text: str, *, interrupt: bool = True) -> bool:
        cleaned = " ".join(str(text or "").split()).strip()
        if not cleaned or not bool(getattr(self.config.sound, "human_voice_enabled", False)):
            return False
        engine = getattr(self, "_speech_engine", None)
        if engine is None or not self._human_voice_supported():
            self._set_human_voice_runtime_state("unavailable")
            return False
        try:
            self._sync_human_speech_engine()
            if interrupt:
                engine.stop()
            engine.say(cleaned)
            self._set_human_voice_runtime_state("speaking")
            return True
        except Exception as exc:
            self._set_human_voice_runtime_state("error")
            self._report_runtime_warning("Human speech unavailable", exc)
            return False

    def _current_sound_area_ratio(self) -> Optional[float]:
        active_order = getattr(self.engine, "active_order", None)
        active_det = getattr(getattr(active_order, "target", None), "det", None)
        if active_det is not None and hasattr(active_det, "area_ratio"):
            try:
                return float(active_det.area_ratio)
            except Exception:
                return None
        targets = list(getattr(self.engine, "last_targets", []) or [])
        if targets:
            det = getattr(targets[0], "det", None)
            if det is not None and hasattr(det, "area_ratio"):
                try:
                    return float(det.area_ratio)
                except Exception:
                    return None
        return None

    def _update_sound_runtime_cues(self) -> None:
        visible_targets = int(len(getattr(self.engine, "last_targets", []) or []))
        qualified_targets = int(len(getattr(self.engine, "last_qualified", []) or []))
        had_visible = self._sound_prev_visible_targets > 0
        has_visible = visible_targets > 0
        had_qualified = self._sound_prev_qualified_targets > 0
        has_qualified = qualified_targets > 0
        area_ratio = self._current_sound_area_ratio()

        if has_visible and not had_visible:
            self._sound_engine.note_detection_acquired(area_ratio, qualified=has_qualified)
        elif has_qualified and not had_qualified:
            self._sound_engine.note_detection_acquired(area_ratio, qualified=True)
        elif had_visible and not has_visible:
            self._sound_engine.note_target_lost()

        lock_frames = int(getattr(self.engine, "_aim_lock_frames", 0) or 0)
        lock_required = max(1, int(getattr(self.config.engagement, "aim_lock_required_frames", 1) or 1))
        lock_active = bool(
            self.engine.state == SentryV2State.ENGAGING
            and getattr(self.engine, "active_order", None) is not None
            and lock_frames >= lock_required
        )
        if lock_active and not self._sound_lock_active:
            self._sound_engine.note_target_lock(area_ratio)

        self._sound_prev_visible_targets = visible_targets
        self._sound_prev_qualified_targets = qualified_targets
        self._sound_lock_active = lock_active

    def _note_sound_settings_changed(self) -> None:
        self._sound_engine.set_profile(self._sound_personality_key(), self._sound_attitude_pct())
        if bool(getattr(self.config.sound, "enabled", True)):
            self._sound_engine.note_settings_changed()

    def _update_auto_lighting(self, frame: "np.ndarray") -> None:
        """Sample frame luminance and adjust LED PWM when auto-lighting is enabled."""
        if not bool(getattr(self.config.lighting, "auto_lighting_enabled", False)):
            return
        if not self._led_on:
            return
        try:
            import cv2 as _cv2
            gray = _cv2.cvtColor(frame, _cv2.COLOR_BGR2GRAY)
            luma = float(gray.mean())
        except Exception:
            return
        self._scene_luma = luma
        threshold = int(getattr(self.config.lighting, "auto_brightness_threshold", 80))
        pwm_min = int(max(0, min(255, getattr(self.config.lighting, "auto_pwm_min", 60))))
        pwm_max = int(max(0, min(255, getattr(self.config.lighting, "auto_pwm_max", 255))))
        if luma < threshold:
            # Dark scene: ramp PWM up toward max as scene gets darker
            dark_ratio = max(0.0, min(1.0, 1.0 - luma / max(1.0, float(threshold))))
            new_pwm = int(pwm_min + dark_ratio * (pwm_max - pwm_min))
        else:
            new_pwm = 0
        if new_pwm != self._auto_led_pwm:
            self._auto_led_pwm = new_pwm
            luma_text = f"luma:{luma:.0f} pwm:{new_pwm}"
            if hasattr(self, "_lbl_auto_luma"):
                self._lbl_auto_luma.setText(f"Scene luma: {luma:.0f}  PWM: {new_pwm}")
            if hasattr(self, "_lbl_auto_luma_qa"):
                self._lbl_auto_luma_qa.setText(luma_text)
            if not self._host_controls_hardware():
                self._queue_comm_task(
                    "set_led_pwm",
                    new_pwm,
                    self.engine.current_pan,
                    self.engine.current_tilt,
                )

    def _sound_volume_pct(self) -> int:
        return int(max(0, min(100, int(getattr(self.config.sound, "volume_pct", 100) or 100))))

    def _sound_personality_key(self) -> str:
        personality = str(getattr(self.config.sound, "personality", "sentinel") or "sentinel").strip().lower()
        return personality if personality in SOUND_PERSONALITY_LABELS else "sentinel"

    def _sound_attitude_pct(self) -> int:
        return int(max(0, min(100, int(getattr(self.config.sound, "attitude_pct", 60) or 60))))

    def _sync_sound_widgets(self) -> None:
        enabled = bool(getattr(self.config.sound, "enabled", True))
        volume_pct = self._sound_volume_pct()
        personality = self._sound_personality_key()
        attitude_pct = self._sound_attitude_pct()
        human_voice_enabled = bool(getattr(self.config.sound, "human_voice_enabled", False))
        human_voice_style = self._human_voice_style_key()
        human_voice_rate = self._human_voice_rate_pct()
        human_voice_pitch = self._human_voice_pitch_pct()
        human_voice_volume = self._human_voice_volume_pct()
        voice_names = list(getattr(self, "_speech_voice_names", []) or [])
        for attr_name in ("_chk_sound_enabled",):
            if hasattr(self, attr_name):
                widget = getattr(self, attr_name)
                widget.blockSignals(True)
                widget.setChecked(enabled)
                widget.blockSignals(False)
        if hasattr(self, "_slider_sound_volume"):
            self._slider_sound_volume.blockSignals(True)
            self._slider_sound_volume.setValue(volume_pct)
            self._slider_sound_volume.setEnabled(enabled)
            self._slider_sound_volume.blockSignals(False)
        if hasattr(self, "_combo_sound_personality"):
            combo_index = max(0, self._combo_sound_personality.findData(personality))
            self._combo_sound_personality.blockSignals(True)
            self._combo_sound_personality.setCurrentIndex(combo_index)
            self._combo_sound_personality.setEnabled(enabled)
            self._combo_sound_personality.blockSignals(False)
        if hasattr(self, "_slider_sound_attitude"):
            self._slider_sound_attitude.blockSignals(True)
            self._slider_sound_attitude.setValue(attitude_pct)
            self._slider_sound_attitude.setEnabled(enabled)
            self._slider_sound_attitude.blockSignals(False)
        if hasattr(self, "_lbl_sound_volume"):
            self._lbl_sound_volume.setText("Muted" if volume_pct <= 0 else f"{volume_pct}%")
        if hasattr(self, "_lbl_sound_attitude"):
            self._lbl_sound_attitude.setText(f"{attitude_pct}%")
        if hasattr(self, "_lbl_sound_profile"):
            self._lbl_sound_profile.setText(
                f"Profile: {SOUND_PERSONALITY_LABELS.get(personality, 'Sentinel')} • attitude {attitude_pct}%"
            )
        if hasattr(self, "_chk_human_voice_enabled"):
            self._chk_human_voice_enabled.blockSignals(True)
            self._chk_human_voice_enabled.setChecked(human_voice_enabled)
            self._chk_human_voice_enabled.setEnabled(self._human_voice_supported())
            self._chk_human_voice_enabled.blockSignals(False)
        if hasattr(self, "_combo_human_voice_style"):
            style_index = max(0, self._combo_human_voice_style.findData(human_voice_style))
            self._combo_human_voice_style.blockSignals(True)
            self._combo_human_voice_style.setCurrentIndex(style_index)
            self._combo_human_voice_style.setEnabled(self._human_voice_supported())
            self._combo_human_voice_style.blockSignals(False)
        if hasattr(self, "_combo_human_voice"):
            self._combo_human_voice.blockSignals(True)
            self._combo_human_voice.clear()
            for voice_name in voice_names:
                self._combo_human_voice.addItem(voice_name, voice_name)
            if voice_names:
                voice_name = self._human_voice_name()
                voice_index = max(0, self._combo_human_voice.findData(voice_name)) if voice_name else 0
                self._combo_human_voice.setCurrentIndex(voice_index)
            self._combo_human_voice.setEnabled(bool(voice_names) and self._human_voice_supported())
            self._combo_human_voice.blockSignals(False)
        if hasattr(self, "_slider_human_voice_rate"):
            self._slider_human_voice_rate.blockSignals(True)
            self._slider_human_voice_rate.setValue(human_voice_rate)
            self._slider_human_voice_rate.setEnabled(self._human_voice_supported())
            self._slider_human_voice_rate.blockSignals(False)
        if hasattr(self, "_slider_human_voice_pitch"):
            self._slider_human_voice_pitch.blockSignals(True)
            self._slider_human_voice_pitch.setValue(human_voice_pitch)
            self._slider_human_voice_pitch.setEnabled(self._human_voice_supported())
            self._slider_human_voice_pitch.blockSignals(False)
        if hasattr(self, "_slider_human_voice_volume"):
            self._slider_human_voice_volume.blockSignals(True)
            self._slider_human_voice_volume.setValue(human_voice_volume)
            self._slider_human_voice_volume.setEnabled(self._human_voice_supported())
            self._slider_human_voice_volume.blockSignals(False)
        if hasattr(self, "_lbl_human_voice_rate"):
            self._lbl_human_voice_rate.setText(f"{human_voice_rate}%")
        if hasattr(self, "_lbl_human_voice_pitch"):
            self._lbl_human_voice_pitch.setText(f"{human_voice_pitch}%")
        if hasattr(self, "_lbl_human_voice_volume"):
            self._lbl_human_voice_volume.setText("Muted" if human_voice_volume <= 0 else f"{human_voice_volume}%")
        if hasattr(self, "_lbl_human_voice_status"):
            if not self._human_voice_supported():
                self._lbl_human_voice_status.setText("Human voice: unavailable in the current runtime")
            else:
                state_label = str(getattr(self, "_speech_state_label", "ready") or "ready")
                status = f"enabled / {state_label}" if human_voice_enabled else state_label
                voice_name = self._human_voice_name() or (voice_names[0] if voice_names else "default voice")
                style_label = str(HUMAN_VOICE_STYLE_PRESETS.get(human_voice_style, HUMAN_VOICE_STYLE_PRESETS["neutral"])["label"])
                self._lbl_human_voice_status.setText(f"Human voice: {status} • {voice_name} • {style_label}")
        if hasattr(self, "_btn_test_human_voice"):
            self._btn_test_human_voice.setEnabled(self._human_voice_supported())
        if hasattr(self, "_chk_mute_buzzer_for_human_voice"):
            self._chk_mute_buzzer_for_human_voice.blockSignals(True)
            self._chk_mute_buzzer_for_human_voice.setChecked(self._mute_buzzer_for_human_voice_enabled())
            self._chk_mute_buzzer_for_human_voice.setEnabled(self._human_voice_supported())
            self._chk_mute_buzzer_for_human_voice.blockSignals(False)
        if hasattr(self, "_btn_human_voice_fallback"):
            self._btn_human_voice_fallback.setEnabled(self._human_voice_supported())
        if hasattr(self, "_btn_human_voice_stop"):
            self._btn_human_voice_stop.setEnabled(self._human_voice_supported())
        if hasattr(self, "_btn_human_voice_refresh"):
            self._btn_human_voice_refresh.setEnabled(True)
        if hasattr(self, "_btn_human_voice_validate"):
            self._btn_human_voice_validate.setEnabled(self._human_voice_supported())
        if hasattr(self, "_btn_human_voice_validate_all"):
            self._btn_human_voice_validate_all.setEnabled(self._human_voice_supported() and bool(voice_names))
        if hasattr(self, "_chk_ai_auto_speak"):
            self._chk_ai_auto_speak.blockSignals(True)
            self._chk_ai_auto_speak.setChecked(bool(getattr(self.config.ai_assistant, "auto_speak_responses", False)))
            self._chk_ai_auto_speak.setEnabled(self._human_voice_supported())
            self._chk_ai_auto_speak.blockSignals(False)
        if hasattr(self, "_btn_ai_speak_last"):
            self._btn_ai_speak_last.setEnabled(self._human_voice_supported())
        self._refresh_human_voice_diagnostics()
        if hasattr(self, "_lbl_sound_status") and self._buzzer_suppressed_for_human_voice() and bool(getattr(self.config.sound, "enabled", True)):
            self._set_label_content(
                self._lbl_sound_status,
                f"ESP32 buzzer muted while human voice mode is enabled | {SOUND_PERSONALITY_LABELS.get(personality, 'Sentinel')} {attitude_pct}% | Volume {volume_pct}%",
                self._status_text_style("neutral"),
            )
        self._sound_engine.set_profile(personality, attitude_pct)
        self._sync_human_speech_engine()

    def _set_optional_toggle_availability(self, button: QPushButton, *, available: bool, on_label: str, off_label: str, unavailable_label: str) -> None:
        if not available:
            button.blockSignals(True)
            button.setChecked(False)
            button.blockSignals(False)
            button.setEnabled(False)
            button.setText(unavailable_label)
            return
        button.setEnabled(True)
        button.setText(on_label if button.isChecked() else off_label)

    def _apply_bridge_capability_controls(self, bridge_caps: dict) -> None:
        caps_age = bridge_caps.get("age_s") if isinstance(bridge_caps, dict) else None
        caps_source = str((bridge_caps or {}).get("source") or "inactive") if isinstance(bridge_caps, dict) else "inactive"

        led_available = True
        laser_available = True
        trigger_servo_available = True
        if caps_age is not None:
            led_available = bridge_caps.get("led_relay_assigned") is not False
            laser_available = bridge_caps.get("laser_relay_assigned") is not False
            trigger_servo_available = bridge_caps.get("trigger_servo_assigned") is not False

        if hasattr(self, "_btn_led"):
            self._set_optional_toggle_availability(
                self._btn_led,
                available=led_available,
                on_label="LED: ON",
                off_label="LED: OFF",
                unavailable_label="LED: N/A",
            )
            if not led_available:
                self._led_on = False
        if hasattr(self, "_btn_laser"):
            self._set_optional_toggle_availability(
                self._btn_laser,
                available=laser_available,
                on_label="Laser: ON",
                off_label="Laser: OFF",
                unavailable_label="Laser: N/A",
            )
            if not laser_available:
                self._laser_on = False

        if hasattr(self, "_lbl_optional_outputs_status"):
            if caps_age is None and caps_source == "waiting":
                text = "Optional outputs: waiting for bridge capability packet"
                style = self._compact_status_style("meta", bold=True)
            elif caps_age is None:
                text = "Optional outputs: capability-driven availability is only shown in bridge mode"
                style = self._compact_status_style("meta", bold=True)
            else:
                parts = []
                parts.append("LED assigned" if led_available else "LED unassigned")
                parts.append("Laser assigned" if laser_available else "Laser unassigned")
                text = "Optional outputs: " + " • ".join(parts)
                style = self._compact_status_style("ok", bold=True) if (led_available or laser_available) else self._compact_status_style("meta", bold=True)
            self._set_label_content(self._lbl_optional_outputs_status, text, style)

        if hasattr(self, "_grp_trigger_servo"):
            self._grp_trigger_servo.setEnabled(trigger_servo_available)
        if hasattr(self, "_lbl_trigger_servo_status"):
            if caps_age is None and caps_source == "waiting":
                text = "Trigger-servo path: waiting for bridge capability packet"
                style = self._compact_status_style("meta", bold=True)
            elif caps_age is None:
                text = "Trigger-servo path: capability-driven availability is only shown in bridge mode"
                style = self._compact_status_style("meta", bold=True)
            elif trigger_servo_available:
                text = "Trigger-servo path: assigned and configurable"
                style = self._compact_status_style("ok", bold=True)
            else:
                text = "Trigger-servo path: unassigned on current Waveshare map; water or MOSFET fire path still works"
                style = self._compact_status_style("meta", bold=True)
            self._set_label_content(self._lbl_trigger_servo_status, text, style)

    def _refresh_sound_toggle_text(self) -> None:
        if hasattr(self, "_chk_sound_enabled"):
            self._chk_sound_enabled.setText(f"Sound: {'ON' if self._chk_sound_enabled.isChecked() else 'OFF'}")

    def _on_sound_enabled_changed(self, checked: bool) -> None:
        self.config.sound.enabled = bool(checked)
        self._sound_engine.set_enabled(bool(checked))
        self._sync_sound_widgets()
        self._refresh_sound_toggle_text()
        self._save_config_quietly()
        if checked:
            self._sound_engine.note_settings_changed()

    def _on_sound_volume_changed(self, value: int) -> None:
        self.config.sound.volume_pct = int(max(0, min(100, int(value))))
        self._sync_sound_widgets()
        self._save_config_quietly()
        if bool(getattr(self.config.sound, "enabled", True)) and self._sound_volume_pct() > 0:
            self._sound_engine.note_settings_changed()

    def _on_auto_lighting_toggled(self, checked: bool) -> None:
        self.config.lighting.auto_lighting_enabled = bool(checked)
        if hasattr(self, "_chk_auto_lighting"):
            self._chk_auto_lighting.setText(f"Auto Lighting: {'ON' if checked else 'OFF'}")
        if hasattr(self, "_chk_auto_lighting_qa"):
            self._chk_auto_lighting_qa.blockSignals(True)
            self._chk_auto_lighting_qa.setChecked(checked)
            self._chk_auto_lighting_qa.blockSignals(False)
        self._save_config_quietly()

    def _on_led_pwm_slider_changed(self, value: int) -> None:
        self.config.lighting.led_pwm_value = int(max(0, min(255, value)))
        if hasattr(self, "_lbl_led_pwm"):
            self._lbl_led_pwm.setText(str(value))
        # Only drive PWM directly if auto-lighting is off and LED is on
        if not bool(getattr(self.config.lighting, "auto_lighting_enabled", False)) and self._led_on:
            if not self._host_controls_hardware():
                self._queue_comm_task(
                    "set_led_pwm",
                    int(max(0, min(255, value))),
                    self.engine.current_pan,
                    self.engine.current_tilt,
                )
        self._save_config_quietly()

    def _on_auto_brightness_threshold_changed(self, value: int) -> None:
        self.config.lighting.auto_brightness_threshold = int(max(0, min(255, value)))
        self._save_config_quietly()

    def _on_auto_pwm_range_changed(self) -> None:
        if hasattr(self, "_spin_auto_pwm_min") and hasattr(self, "_spin_auto_pwm_max"):
            self.config.lighting.auto_pwm_min = int(max(0, min(255, self._spin_auto_pwm_min.value())))
            self.config.lighting.auto_pwm_max = int(max(0, min(255, self._spin_auto_pwm_max.value())))
        self._save_config_quietly()

    def _on_sound_personality_changed(self, index: int) -> None:
        if not hasattr(self, "_combo_sound_personality"):
            return
        personality = str(self._combo_sound_personality.itemData(index) or "sentinel").strip().lower()
        if personality not in SOUND_PERSONALITY_LABELS:
            personality = "sentinel"
        self.config.sound.personality = personality
        self._sync_sound_widgets()
        self._save_config_quietly()
        self._note_sound_settings_changed()

    def _on_sound_attitude_changed(self, value: int) -> None:
        self.config.sound.attitude_pct = int(max(0, min(100, int(value))))
        self._sync_sound_widgets()
        self._save_config_quietly()
        self._note_sound_settings_changed()

    def _on_human_voice_enabled_changed(self, checked: bool) -> None:
        self.config.sound.human_voice_enabled = bool(checked)
        self._set_human_voice_runtime_state("ready" if checked else "disabled")
        self._sync_sound_widgets()
        self._save_config_quietly()
        if checked:
            self._speak_human_phrase("Human voice speech is now enabled.")

    def _on_human_voice_style_changed(self, index: int) -> None:
        if not hasattr(self, "_combo_human_voice_style"):
            return
        style_key = str(self._combo_human_voice_style.itemData(index) or "neutral").strip().lower()
        self._apply_human_voice_style(style_key)

    def _on_mute_buzzer_for_human_voice_changed(self, checked: bool) -> None:
        self.config.sound.mute_buzzer_when_human_voice_enabled = bool(checked)
        self._sync_sound_widgets()
        self._save_config_quietly()

    def _on_human_voice_name_changed(self, index: int) -> None:
        if not hasattr(self, "_combo_human_voice"):
            return
        voice_name = str(self._combo_human_voice.itemData(index) or "").strip()
        self.config.sound.human_voice_name = voice_name
        self._sync_sound_widgets()
        self._save_config_quietly()

    def _on_human_voice_rate_changed(self, value: int) -> None:
        self.config.sound.human_voice_rate_pct = int(max(50, min(150, int(value))))
        self._sync_sound_widgets()
        self._save_config_quietly()

    def _on_human_voice_pitch_changed(self, value: int) -> None:
        self.config.sound.human_voice_pitch_pct = int(max(50, min(150, int(value))))
        self._sync_sound_widgets()
        self._save_config_quietly()

    def _on_human_voice_volume_changed(self, value: int) -> None:
        self.config.sound.human_voice_volume_pct = int(max(0, min(100, int(value))))
        self._sync_sound_widgets()
        self._save_config_quietly()

    def _on_test_human_voice_clicked(self) -> None:
        if not self._human_voice_supported():
            self._set_human_voice_runtime_state("unavailable")
            self._log("Human voice test unavailable: Qt text-to-speech is not ready")
            return
        if not bool(getattr(self.config.sound, "human_voice_enabled", False)):
            self.config.sound.human_voice_enabled = True
            self._sync_sound_widgets()
            self._save_config_quietly()
        test_voice = self._human_voice_name() or (self._speech_voice_names[0] if self._speech_voice_names else "default voice")
        style_label = str(HUMAN_VOICE_STYLE_PRESETS.get(self._human_voice_style_key(), HUMAN_VOICE_STYLE_PRESETS["neutral"])["label"])
        if self._speak_human_phrase(f"Hello. Smart Sentry human voice mode is online. Voice {test_voice}. Style {style_label}."):
            self._log(f"Human voice test started using {test_voice} ({style_label})")
        else:
            self._log("Human voice test failed to start")

    def _on_test_human_voice_fallback_clicked(self) -> None:
        if not self._human_voice_supported():
            self._set_human_voice_runtime_state("unavailable")
            self._log("Fallback voice test unavailable: Qt text-to-speech is not ready")
            return
        if not bool(getattr(self.config.sound, "human_voice_enabled", False)):
            self.config.sound.human_voice_enabled = True
            self._set_human_voice_runtime_state("ready")
            self._sync_sound_widgets()
            self._save_config_quietly()
        phrase = "This is the Smart Sentry fallback voice check. If you hear this, Windows SAPI playback is working."
        if self._speak_human_phrase(phrase):
            self._log("Fallback voice phrase started")
        else:
            self._log("Fallback voice phrase failed to start")

    def _on_stop_human_voice_clicked(self) -> None:
        self._stop_human_speech()
        self._refresh_human_voice_diagnostics()
        self._log("Human voice playback stopped")

    def _on_refresh_human_voice_diagnostics_clicked(self) -> None:
        self._refresh_human_voice_diagnostics()
        self._log(
            f"Voice diagnostics: backend={self._human_voice_backend_summary()} voice={self._human_voice_name() or 'default voice'} state={getattr(self, '_speech_state_label', 'waiting')} buzzer_muted={self._buzzer_suppressed_for_human_voice()}"
        )

    def _on_validate_human_voices_clicked(self) -> None:
        self._run_human_voice_validation(scan_all=False)

    def _on_validate_all_human_voices_clicked(self) -> None:
        self._run_human_voice_validation(scan_all=True)

    def _run_human_voice_validation(self, *, scan_all: bool) -> None:
        if not self._human_voice_supported():
            self._set_human_voice_runtime_state("unavailable")
            if hasattr(self, "_lbl_human_voice_diag_validation"):
                self._lbl_human_voice_diag_validation.setText("Validation: Qt text-to-speech is unavailable in the current runtime")
            self._log("Voice validation unavailable: Qt text-to-speech is not ready")
            return
        if not bool(getattr(self.config.sound, "human_voice_enabled", False)):
            self.config.sound.human_voice_enabled = True
            self._set_human_voice_runtime_state("ready")
            self._sync_sound_widgets()
            self._save_config_quietly()
        app = QApplication.instance()
        engine = getattr(self, "_speech_engine", None)
        original_voice = self._human_voice_name()
        selected_voice = original_voice or (self._speech_voice_names[0] if self._speech_voice_names else "")
        target_voices = list(getattr(self, "_speech_voice_names", []) or []) if scan_all else ([selected_voice] if selected_voice else [])
        if not target_voices:
            summary = "Validation: no Qt voices are available to test"
            if hasattr(self, "_lbl_human_voice_diag_validation"):
                self._lbl_human_voice_diag_validation.setText(summary)
            self._log(summary)
            return
        results: List[str] = []
        passed = 0
        for voice_name in target_voices:
            index = self._combo_human_voice.findData(voice_name) if hasattr(self, "_combo_human_voice") else -1
            if index >= 0:
                self._combo_human_voice.setCurrentIndex(index)
                self._on_human_voice_name_changed(index)
            else:
                self.config.sound.human_voice_name = str(voice_name)
                self._sync_human_speech_engine()
            started = self._speak_human_phrase(f"Voice validation. {voice_name}.")
            deadline = time.time() + (0.75 if scan_all else 0.55)
            seen_states: List[str] = []
            while app is not None and time.time() < deadline:
                app.processEvents()
                state_label = str(getattr(self, "_speech_state_label", "waiting") or "waiting")
                if not seen_states or seen_states[-1] != state_label:
                    seen_states.append(state_label)
            engine_voice = ""
            if engine is not None and hasattr(engine, "voice"):
                try:
                    engine_voice = str(engine.voice().name() or "").strip()
                except Exception:
                    engine_voice = ""
            state_label = str(getattr(self, "_speech_state_label", "waiting") or "waiting")
            if not seen_states:
                seen_states.append(state_label)
            engine_matches = engine_voice.lower() == str(voice_name).strip().lower()
            speech_transition_seen = any(state in {"speaking", "paused", "ready"} for state in seen_states)
            accepted = bool(started and engine_matches and speech_transition_seen)
            if accepted:
                passed += 1
            state_chain = "->".join(seen_states)
            status_text = "pass" if accepted else "check"
            results.append(f"{voice_name}: {status_text} (engine={engine_voice or 'none'} states={state_chain})")
            self._stop_human_speech()
        if original_voice:
            restore_index = self._combo_human_voice.findData(original_voice) if hasattr(self, "_combo_human_voice") else -1
            if restore_index >= 0:
                self._combo_human_voice.setCurrentIndex(restore_index)
                self._on_human_voice_name_changed(restore_index)
            else:
                self.config.sound.human_voice_name = original_voice
                self._sync_human_speech_engine()
        self._refresh_human_voice_diagnostics()
        mode_label = "all voices" if scan_all else "current voice"
        if scan_all:
            summary = f"Validation: {passed}/{len(target_voices)} voices passed during {mode_label} scan"
        else:
            summary = f"Validation: {'pass' if passed else 'check'} for {target_voices[0]} during {mode_label} test"
        if hasattr(self, "_lbl_human_voice_diag_validation"):
            self._lbl_human_voice_diag_validation.setText(
                summary
                + " | "
                + " | ".join(results)
                + " | This confirms Qt voice selection and speech-state transitions, not physical speaker audibility."
            )
        self._log(summary + " | " + " | ".join(results))

    def _suppress_motion_detection(self, seconds: Optional[float] = None) -> None:
        suppress_for = self.config.detection_mode.motion_ignore_after_move_s if seconds is None else seconds
        if suppress_for > 0:
            self._detector.suppress_motion(float(suppress_for))

    def _apply_all_config(self) -> None:
        """Read all UI controls into config before start."""
        self._on_detection_mode_changed(self._combo_detection_mode.currentIndex())
        if hasattr(self, "_chk_prompted_enabled"):
            self._on_prompted_settings_changed()
        self._on_detection_settings_changed()
        self._on_color_settings_changed()
        self._on_filter_changed()
        self._on_class_selection_changed()
        self._on_scoring_changed()
        self._on_engagement_changed()
        self._on_guard_changed()
        self._on_scope_view_changed()
        self._on_overlay_changed()

    def _raw_detections_to_objects(
        self, raw: list, frame_w: int, frame_h: int
    ) -> List[DetectedObject]:
        """
        Convert main-app detection format to DetectedObject list.

        Accepted formats per item:
          (x, y, w, h, score)
          (x, y, w, h, score, class_id)
        """
        result: List[DetectedObject] = []
        for i, det in enumerate(raw):
            if len(det) < 5:
                continue
            x, y, w, h = int(det[0]), int(det[1]), int(det[2]), int(det[3])
            score = float(det[4])
            class_id = int(det[5]) if len(det) >= 6 else 0
            class_name, source = self._resolve_class_and_source(class_id)
            cx = x + w / 2.0
            cy = y + h / 2.0
            result.append(DetectedObject(
                track_id=i,
                class_name=class_name,
                confidence=score,
                bbox=(x, y, w, h),
                center_x=cx,
                center_y=cy,
                source=source,
                frame_width=frame_w,
                frame_height=frame_h,
            ))
        return result

    def _convert_detections(
        self, raw: list, frame_w: int, frame_h: int, timestamp: Optional[float] = None
    ) -> List[DetectedObject]:
        result = self._raw_detections_to_objects(raw, frame_w, frame_h)
        return self._tracker.assign_tracks(result, timestamp or time.time())

    def _resolve_class_and_source(self, class_id: int) -> Tuple[str, str]:
        if class_id == -1:
            return "motion", "frame_diff"
        if class_id == -2:
            return "foreground", "backsub"
        if class_id == -3:
            return "color", "color"
        if class_id == -4:
            return "moving_object", "motion_locked"

        # Use currently loaded model names first so custom models (e.g. ratdogcat.pt)
        # map class IDs to correct labels instead of hard-coded COCO labels.
        model_names = getattr(getattr(self._detector, "_yolo_model", None), "names", None)
        try:
            if isinstance(model_names, dict):
                name = model_names.get(class_id)
                if isinstance(name, str) and name.strip():
                    return name.strip().lower(), "yolo"
            elif isinstance(model_names, (list, tuple)) and 0 <= class_id < len(model_names):
                name = model_names[class_id]
                if isinstance(name, str) and name.strip():
                    return name.strip().lower(), "yolo"
        except Exception:
            pass

        if 0 <= class_id < len(YOLO_COCO_CLASSES):
            return YOLO_COCO_CLASSES[class_id], "yolo"
        return "unknown", "yolo"

    def _show_frame(self, frame: np.ndarray) -> None:
        """Convert BGR frame to QPixmap and display."""
        try:
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rgb = np.ascontiguousarray(rgb)
            h, w, ch = rgb.shape
            bytes_per_line = int(rgb.strides[0])
            qimg = QImage(rgb.data, w, h, bytes_per_line, QImage.Format_RGB888).copy()
            pixmap = QPixmap.fromImage(qimg)
            self._video_label.set_frame(pixmap, w, h)
        except Exception as e:
            print(f"[SENTRY_V2] _show_frame error: {e}")

    def _draw_no_fire_mask_draft(self, frame: np.ndarray) -> None:
        if not self._mask_draft_vertices:
            return
        draft_mask = NoFireMaskConfig(
            name="draft",
            enabled=True,
            vertices=[NoFireMaskVertex(pan=v.pan, tilt=v.tilt) for v in self._mask_draft_vertices],
        )
        points = project_mask_to_frame(
            draft_mask,
            self.engine.current_pan,
            self.engine.current_tilt,
            self.config.guard.camera_hfov,
            self.config.guard.camera_vfov,
            frame.shape[1],
            frame.shape[0],
        )
        for px, py in points:
            cv2.circle(frame, (int(px), int(py)), 5, (0, 196, 255), -1)
        if len(points) >= 2:
            for start, end in zip(points[:-1], points[1:]):
                cv2.line(frame, start, end, (0, 196, 255), 2, cv2.LINE_AA)
        if len(points) >= 3:
            cv2.line(frame, points[-1], points[0], (0, 128, 220), 1, cv2.LINE_AA)
        anchor = points[-1]
        cv2.putText(
            frame,
            f"MASK DRAFT: {len(points)} pts",
            (int(anchor[0]) + 8, int(anchor[1]) - 8),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            (0, 196, 255),
            1,
            cv2.LINE_AA,
        )

    def _draw_color_gate_status(self, frame: np.ndarray, mode: int, use_internal_detector: bool) -> None:
        if mode not in (6, 7, 8, 9, 10):
            return

        if not use_internal_detector:
            text = "Color Gate: external detector"
            color = (132, 188, 255)
        else:
            status = self._detector.get_last_color_gate_status()
            if not status:
                text = "Color Gate: waiting..."
                color = (160, 160, 160)
            else:
                preset = str(status.get("preset") or "any")
                color_boxes = int(status.get("color_boxes", 0))
                gate_boxes = int(status.get("gate_boxes", 0))
                final_boxes = int(status.get("final_boxes", 0))

                if preset in ("", "any"):
                    state = "BROAD"
                    color = (132, 188, 255)
                else:
                    state = "PASS" if final_boxes > 0 else "FAIL"
                    color = (120, 230, 120) if final_boxes > 0 else (95, 120, 255)

                text = (
                    f"Color Gate {state}: {preset} "
                    f"(color={color_boxes}, gate={gate_boxes}, final={final_boxes})"
                )

        x = 10
        y = frame.shape[0] - 12
        font = cv2.FONT_HERSHEY_DUPLEX
        font_scale = 0.38
        cv2.putText(frame, text, (x + 1, y + 1), font, font_scale, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, text, (x, y),           font, font_scale, color,    1, cv2.LINE_AA)

    def _refresh_status(self) -> None:
        """Periodic status label update."""
        stats = self.engine.get_engagement_stats()
        feedback = self._comm.get_servo_feedback_snapshot()
        io_runtime = self._comm.get_io_runtime_snapshot()
        bridge_caps = self._comm.get_bridge_caps_snapshot()

        detector_error = str(getattr(self, "_last_detector_error", "") or "").strip()
        if detector_error and detector_error != getattr(self, "_last_detector_error_seen", ""):
            self._last_detector_error_seen = detector_error
            self._log(f"[WARN] Detector worker error: {detector_error}")

        # YOLO-mode-active-but-not-loaded warning — emit once per 10s to log so it's visible
        _yolo_modes = {2, 4, 5, 9, 10}
        cur_det_mode = self.config.detection_mode.detection_mode
        if cur_det_mode in _yolo_modes and not getattr(self._detector, "_yolo_loaded", False):
            now = __import__("time").monotonic()
            if now - getattr(self, "_last_yolo_warn_t", 0.0) > 10.0:
                self._last_yolo_warn_t = now
                self._log("[WARN] YOLO detection active but no model loaded — load a model in the Detection tab")
                self._set_yolo_status("error", "YOLO mode active but no model loaded — click Load in Detection tab")

        state_name = str(stats['state'] or 'PAUSED').strip().upper()
        motion_enabled = bool(stats.get('motion_enabled', True))
        state_level = {
            'PAUSED': 'neutral',
            'GUARDING': 'info',
            'ENGAGING': 'ok',
            'RETURNING': 'warn',
        }.get(state_name, 'info')
        self._set_label_content(
            self._lbl_state,
            self._status_two_line_markup(
                state_name,
                f"Pan/Tilt {'ON' if motion_enabled else 'OFF'}",
                primary_color=self._theme_tokens()["status_neutral"],
                secondary_color=self._status_meta_color(),
            ),
            self._status_text_style(state_level, compact=False),
        )

        visible_targets = int(stats.get('targets_visible', 0) or 0)
        qualified_targets = int(stats.get('targets_qualified', 0) or 0)
        active_engagements = int(stats.get('active_engagements', 0) or 0)
        if state_name in {"GUARDING", "RETURNING"} and visible_targets <= 0:
            self._sound_engine.note_guard_tick(
                scanning=bool(
                    state_name == "RETURNING"
                    or int(getattr(self.config.guard, "guard_mode", 0) or 0) != 0
                    or bool(getattr(self.engine, "_pir_cue_mode", False))
                    or bool(getattr(self.engine, "_pir_scan_mode", False))
                )
            )
        self._set_label_content(
            self._lbl_stats,
            self._status_metric_markup([
                (visible_targets, "vis"),
                (qualified_targets, "ready"),
                (active_engagements, "active"),
            ]),
            self._status_text_style('ok', compact=False),
        )
        if hasattr(self, "_lbl_motion_gate"):
            if not motion_enabled:
                gate_text = "Tracking: Auto Motion OFF"
                gate_color = "#ffae42"
            elif visible_targets > 0 and qualified_targets <= 0:
                gate_text = "Tracking: visible targets filtered before engage"
                gate_color = "#ffd27a"
            elif qualified_targets > 0:
                gate_text = "Tracking: qualified target ready"
                gate_color = "#8fe3c4"
            else:
                gate_text = "Tracking: idle"
                gate_color = "#97a8b8"
            self._set_label_content(
                self._lbl_motion_gate,
                f"{gate_text} | Lock {int(stats.get('aim_lock_frames', 0) or 0)} | "
                f"Move {int(getattr(self, '_last_tracking_move_time_ms', 0))}ms | "
                f"Suppress {float(getattr(self, '_last_tracking_suppression_s', 0.0)):.2f}s",
                f"font-weight: bold; color: {gate_color}; font-size: {self._theme_tokens()['status_font_pt']:.2f}pt;",
            )
        current_pan = float(self.engine.current_pan)
        current_tilt = float(self.engine.current_tilt)
        feedback_age = feedback.get("age_s")
        feedback_pan = feedback.get("pan_deg")
        feedback_tilt = feedback.get("tilt_deg")
        feedback_live = (
            feedback_pan is not None
            and feedback_tilt is not None
            and feedback_age is not None
            and float(feedback_age) <= 1.5
        )
        display_pan = float(feedback_pan) if feedback_live else current_pan
        display_tilt = float(feedback_tilt) if feedback_live else current_tilt
        guard = self.config.guard
        pan_span = max(0.1, float(guard.pan_max) - float(guard.pan_min))
        tilt_span = max(0.1, float(guard.tilt_max) - float(guard.tilt_min))
        pan_progress = int(max(0, min(1000, round(((display_pan - float(guard.pan_min)) / pan_span) * 1000.0))))
        tilt_progress = int(max(0, min(1000, round(((display_tilt - float(guard.tilt_min)) / tilt_span) * 1000.0))))
        pan_source_text = "meas" if feedback_live else "est"
        tilt_source_text = "meas" if feedback_live else "est"
        self._set_label_content(self._lbl_angles, f"Pan {display_pan:.1f}° ({pan_source_text})  [{guard.pan_min:.0f}..{guard.pan_max:.0f}]")
        self._bar_pan_status.setValue(pan_progress)
        if hasattr(self, "_lbl_angles_controls"):
            commanded_pan = float(getattr(self, "_last_commanded_pan", current_pan))
            commanded_tilt = float(getattr(self, "_last_commanded_tilt", current_tilt))
            self._set_label_content(
                self._lbl_angles_controls,
                f"Tilt {display_tilt:.1f}° ({tilt_source_text})  [{guard.tilt_min:.0f}..{guard.tilt_max:.0f}]   Cmd {commanded_pan:.1f}/{commanded_tilt:.1f}°",
            )
            self._bar_tilt_status.setValue(tilt_progress)
        caps_age = bridge_caps.get("age_s")
        switch_supported = None
        if caps_age is not None:
            switch_supported = bridge_caps.get("switch_supported")
        safety_text = "LOCKED"
        trigger_text = "Water"
        switch_text = None
        hw_arm_text = None
        fire_blocked = True
        current_fault = None
        hw_arm_enabled_value = None
        switch_in_value = None

        if hasattr(self, "_lbl_hw_safety"):
            io_age = io_runtime.get("age_s")
            io_is_live = io_age is not None and float(io_age) <= 2.0
            safety_value = io_runtime.get("safety") if io_is_live else None
            mode_value = io_runtime.get("mode") if io_is_live else None
            switch_in_value = io_runtime.get("switch_in") if io_is_live else None
            hw_arm_enabled_value = io_runtime.get("hw_arm_enabled") if io_is_live else None
            current_fault = io_runtime.get("current_fault") if io_is_live else None
            if safety_value is None:
                safety_text = "ARMED" if self._safety_armed else "LOCKED"
            else:
                safety_text = "ARMED" if int(safety_value) == 0 else "LOCKED"
            if mode_value is None:
                trigger_text = "Projectile" if self.config.engagement.trigger_mode_bb else "Water"
            else:
                trigger_text = "Projectile" if int(mode_value) == 1 else "Water"
            switch_text = None if switch_in_value is None else ("CLOSED" if int(switch_in_value) != 0 else "OPEN")
            hw_arm_text = None if hw_arm_enabled_value is None else ("ENABLED" if int(hw_arm_enabled_value) != 0 else "BLOCKED")
            fire_blocked = (safety_text != "ARMED") or bool(current_fault)
            if switch_supported is True and hw_arm_enabled_value is not None and int(hw_arm_enabled_value) == 0:
                fire_blocked = True

        if hasattr(self, "_lbl_sound_status"):
            sound_enabled = bool(getattr(self.config.sound, "enabled", True))
            sound_personality = SOUND_PERSONALITY_LABELS.get(self._sound_personality_key(), "Sentinel")
            if not sound_enabled:
                sound_text = "Sound disabled"
                sound_color = "#97a8b8"
            elif self._buzzer_suppressed_for_human_voice():
                sound_text = "ESP32 buzzer muted while human voice mode is enabled"
                sound_color = "#97a8b8"
            else:
                sound_text = self._comm.sound_transport_info()
                if self._comm.is_sound_link_verified():
                    sound_color = "#8fe3c4"
                elif self._comm.can_send_sound():
                    sound_color = "#ffd27a"
                else:
                    sound_color = "#ffae42"
            self._set_label_content(
                self._lbl_sound_status,
                f"{sound_text} | {sound_personality} {self._sound_attitude_pct()}% | Volume {self._sound_volume_pct()}%",
                self._status_text_style("ok" if sound_color == "#8fe3c4" else "warn" if sound_color == "#ffd27a" else "error" if sound_color == "#ffae42" else "neutral"),
            )
            if current_fault is not None and bool(current_fault):
                fire_path_text = "FAULT TRIPPED"
            elif switch_supported is True and hw_arm_enabled_value is not None and int(hw_arm_enabled_value) == 0:
                fire_path_text = "SWITCH OPEN"
            elif safety_text != "ARMED":
                fire_path_text = "SAFETY LOCKED"
            elif switch_supported is False:
                fire_path_text = "SOFTWARE ARMED"
            elif hw_arm_enabled_value is not None and int(hw_arm_enabled_value) != 0:
                fire_path_text = "PHYSICALLY ARMED"
            else:
                fire_path_text = "READY UNKNOWN"
            if current_fault is None:
                current_fault_text = "unknown"
                safety_color = "#ffd27a" if safety_text == "ARMED" and not fire_blocked else "#ff8a7a"
            else:
                current_fault_text = "TRIPPED" if bool(current_fault) else "clear"
                safety_color = "#ff8a7a" if fire_blocked else "#8fe3c4"
            status_parts = [f"Safety {safety_text}", trigger_text, f"Fault {current_fault_text}"]
            if switch_supported is True and switch_text is not None:
                status_parts.append(f"Switch {switch_text}")
            if switch_supported is True and hw_arm_text is not None:
                status_parts.append(f"HW arm {hw_arm_text}")
            elif switch_supported is False:
                status_parts.append("No HW switch")
            self._set_label_content(
                self._lbl_hw_safety,
                self._status_two_line_markup(
                    fire_path_text,
                    " • ".join(status_parts),
                    primary_color=safety_color,
                    secondary_color=self._status_meta_color(),
                ),
                f"color: {safety_color};",
            )

        if hasattr(self, "_lbl_hw_servo_health"):
            feedback_age = feedback.get("age_s")
            diag_age = feedback.get("diag_age_s")
            source = str(feedback.get("source") or "inactive")
            if feedback_age is not None and float(feedback_age) <= 1.5:
                status_word = "live"
                color = "#8fe3c4"
            elif source == "waiting":
                status_word = "waiting"
                color = "#ffd27a"
            elif feedback_age is not None:
                status_word = "stale"
                color = "#ffd27a"
            else:
                status_word = "inactive"
                color = "#97a8b8"
            pan_voltage = feedback.get("pan_voltage_v")
            tilt_voltage = feedback.get("tilt_voltage_v")
            pan_load = feedback.get("pan_load_raw")
            tilt_load = feedback.get("tilt_load_raw")
            voltage_text = (
                f"Pan {float(pan_voltage):.1f}V | Tilt {float(tilt_voltage):.1f}V"
                if pan_voltage is not None and tilt_voltage is not None
                else "Voltage: waiting"
            )
            load_text = (
                f"Load P {int(pan_load):+d} | T {int(tilt_load):+d}"
                if pan_load is not None and tilt_load is not None
                else "Load waiting"
            )
            age_text = f"diag {float(diag_age):.1f}s" if diag_age is not None else "diag --"
            self._set_label_content(
                self._lbl_hw_servo_health,
                f"Servo {status_word} • {voltage_text} • {load_text} • {age_text}",
                self._status_text_style("ok" if color == "#8fe3c4" else "warn" if color == "#ffd27a" else "neutral"),
            )

        if hasattr(self, "_lbl_hw_current"):
            io_age = io_runtime.get("age_s")
            io_is_live = io_age is not None and float(io_age) <= 2.0
            pan_m_a = io_runtime.get("pan_mA") if io_is_live else None
            pan_m_a_valid = io_runtime.get("pan_mA_valid") if io_is_live else None
            tilt_m_a = io_runtime.get("tilt_mA") if io_is_live else None
            tilt_m_a_valid = io_runtime.get("tilt_mA_valid") if io_is_live else None
            total_m_a = io_runtime.get("total_mA") if io_is_live else None
            total_m_a_valid = io_runtime.get("total_mA_valid") if io_is_live else None
            current_fault = io_runtime.get("current_fault") if io_is_live else None
            pan_supported = bridge_caps.get("current_pan_supported") if caps_age is not None else None
            tilt_supported = bridge_caps.get("current_tilt_supported") if caps_age is not None else None
            total_supported = bridge_caps.get("current_total_supported") if caps_age is not None else None

            def _current_field_text(label: str, value: object, valid: object, supported: object) -> str:
                if valid is False or supported is False:
                    return f"{label} n/a"
                if value is not None:
                    return f"{label} {int(value)}mA"
                return f"{label} waiting"

            has_any_current_state = any(
                item is not None
                for item in (
                    pan_m_a,
                    tilt_m_a,
                    total_m_a,
                    pan_m_a_valid,
                    tilt_m_a_valid,
                    total_m_a_valid,
                    pan_supported,
                    tilt_supported,
                    total_supported,
                )
            )

            if not has_any_current_state:
                if io_runtime.get("source") in ("esp32-state", "esp32-ack"):
                    text = "Current: runtime is live but this firmware has not exposed current telemetry metadata yet"
                    color = "#ffd27a"
                elif io_runtime.get("source") == "waiting":
                    text = "Current: waiting for ESP32 state"
                    color = "#97a8b8"
                else:
                    text = "Current: unavailable in this connection mode"
                    color = "#97a8b8"
            else:
                pan_text = _current_field_text("Pan", pan_m_a, pan_m_a_valid, pan_supported)
                tilt_text = _current_field_text("Tilt", tilt_m_a, tilt_m_a_valid, tilt_supported)
                total_text = _current_field_text("Total", total_m_a, total_m_a_valid, total_supported)
                text = f"Current: {pan_text} | {tilt_text} | {total_text}"
                if bool(current_fault):
                    color = "#ff8a7a"
                elif False in (pan_m_a_valid, tilt_m_a_valid, total_m_a_valid, pan_supported, tilt_supported, total_supported):
                    color = "#ffd27a"
                else:
                    color = "#8fe3c4"
            self._set_label_content(self._lbl_hw_current, text, self._status_text_style("error" if color == "#ff8a7a" else "ok" if color == "#8fe3c4" else "warn" if color == "#ffd27a" else "neutral"))

        if hasattr(self, "_lbl_bridge_runtime"):
            io_age = io_runtime.get("age_s")
            io_is_live = io_age is not None and float(io_age) <= 2.0
            switch_in = io_runtime.get("switch_in") if io_is_live else None
            hw_arm_enabled = io_runtime.get("hw_arm_enabled") if io_is_live else None
            control_source_mode = str(io_runtime.get("control_source_mode") or "") if io_is_live else ""
            control_source_active = str(io_runtime.get("control_source_active") or "") if io_is_live else ""
            if switch_supported is False and caps_age is not None:
                age_text = f"age {float(io_age):.1f}s" if io_age is not None else "age --"
                source_text = f" • src {control_source_active or control_source_mode}" if (control_source_active or control_source_mode) else ""
                text = f"Bridge: NO HARDWARE SWITCH • software safety only{source_text} • {age_text}"
                color = "#8fe3c4" if not fire_blocked else "#ffd27a"
            elif switch_in is None and hw_arm_enabled is None:
                source = str(io_runtime.get("source") or "inactive")
                if source in ("esp32-state", "esp32-ack"):
                    text = "Bridge: runtime live but this firmware has not reported switch/interlock fields"
                    color = "#ffd27a"
                elif source == "waiting":
                    text = "Bridge: waiting for switch runtime"
                    color = "#97a8b8"
                else:
                    text = "Bridge: inactive in this connection mode"
                    color = "#97a8b8"
            else:
                switch_text = "closed" if int(switch_in or 0) != 0 else "open"
                age_text = f"age {float(io_age):.1f}s" if io_age is not None else "age --"
                headline = "PHYSICALLY ARMED" if int(hw_arm_enabled or 0) != 0 else "TRIGGER BLOCKED BY HARDWARE"
                source_text = f" • src {control_source_active or control_source_mode}" if (control_source_active or control_source_mode) else ""
                text = f"Bridge: {headline} • switch {switch_text}{source_text} • {age_text}"
                color = "#8fe3c4" if int(hw_arm_enabled or 0) != 0 else "#ff8a7a"
            self._set_label_content(self._lbl_bridge_runtime, text, self._status_text_style("error" if color == "#ff8a7a" else "ok" if color == "#8fe3c4" else "warn" if color == "#ffd27a" else "neutral"))

        if hasattr(self, "_lbl_bridge_warning"):
            io_age = io_runtime.get("age_s")
            io_is_live = io_age is not None and float(io_age) <= 2.0
            hw_arm_enabled = io_runtime.get("hw_arm_enabled") if io_is_live else None
            switch_in = io_runtime.get("switch_in") if io_is_live else None
            if caps_age is not None and switch_supported is False:
                text = "Bridge warning: none, hardware interlock is disabled in current firmware"
                level = "ok"
            elif caps_age is not None and hw_arm_enabled is not None and int(hw_arm_enabled) == 0:
                switch_state = "OPEN" if int(switch_in or 0) == 0 else "UNKNOWN"
                text = f"Bridge warning: trigger path blocked by hardware interlock ({switch_state})"
                level = "error"
            elif caps_age is not None and hw_arm_enabled is not None and int(hw_arm_enabled) != 0:
                text = "Bridge warning: none, physical arm path is enabled"
                level = "ok"
            elif caps_age is not None:
                text = "Bridge warning: waiting for live switch/interlock state"
                level = "warn"
            elif io_runtime.get("source") in ("esp32-state", "esp32-ack"):
                text = "Bridge warning: firmware runtime is live but no capability packet has been seen yet"
                level = "warn"
            else:
                text = "Bridge warning: unavailable in this connection mode"
                level = "neutral"
            self._set_label_content(self._lbl_bridge_warning, text, self._status_text_style(level, badge=True))

        if hasattr(self, "_lbl_bridge_caps"):
            caps_source = str(bridge_caps.get("source") or "inactive")
            pins = bridge_caps.get("pins") or {}
            switch_role = str(bridge_caps.get("switch_role") or "")
            if caps_age is not None:
                role = str(bridge_caps.get("role") or "bridge")
                sound_text = "sound on" if bool(bridge_caps.get("sound_supported")) else "sound off"
                header_text = "header locked" if bool(bridge_caps.get("header_reference_locked")) else "header open"
                rc_supported = bridge_caps.get("rc_input_supported")
                rc_planned = str(bridge_caps.get("rc_input_planned") or "")
                rc_rx_pin = pins.get("header_rc_uart_rx_planned")
                rc_switch_channel = bridge_caps.get("rc_source_switch_channel")
                if rc_supported is True:
                    rc_text = "rc on"
                elif rc_planned:
                    if rc_rx_pin is not None and rc_switch_channel is not None:
                        rc_text = f"fs-ia6 plan H{rc_rx_pin}/CH{rc_switch_channel}"
                    elif rc_rx_pin is not None:
                        rc_text = f"rc plan H{rc_rx_pin}"
                    else:
                        rc_text = "rc planned"
                else:
                    rc_text = "rc off"
                trigger_pin = pins.get("header_trigger_mosfet")
                switch_pin = pins.get("header_switch_in")
                if trigger_pin is not None and switch_supported is True and switch_pin is not None:
                    pin_text = f"trig H{trigger_pin} • switch H{switch_pin}"
                elif trigger_pin is not None and switch_supported is False:
                    pin_text = f"trig H{trigger_pin} • no hw switch"
                elif pins:
                    pin_text = "gpio map published"
                else:
                    pin_text = "header pins partial"
                if switch_supported is True and switch_role:
                    text = f"Caps: {role} • {sound_text} • {rc_text} • {header_text} • {switch_role} • {pin_text}"
                else:
                    text = f"Caps: {role} • {sound_text} • {rc_text} • {header_text} • {pin_text}"
                color = "#8fe3c4"
            elif caps_source == "waiting":
                text = "Caps: waiting for bridge capability packet"
                color = "#97a8b8"
            elif io_runtime.get("source") in ("esp32-state", "esp32-ack"):
                text = "Caps: runtime is live but this firmware has not sent a capability packet"
                color = "#ffd27a"
            else:
                text = "Caps: unavailable in this connection mode"
                color = "#97a8b8"
            self._set_label_content(self._lbl_bridge_caps, text, self._status_text_style("ok" if color == "#8fe3c4" else "neutral"))
        self._apply_bridge_capability_controls(bridge_caps)
        if hasattr(self, "_btn_control_source"):
            io_age = io_runtime.get("age_s")
            io_is_live = io_age is not None and float(io_age) <= 2.0
            runtime_mode = str(io_runtime.get("control_source_mode") or "") if io_is_live else ""
            runtime_active = str(io_runtime.get("control_source_active") or "") if io_is_live else ""
            if runtime_mode in ("app", "rc"):
                checked = runtime_mode == "rc"
                if self._btn_control_source.isChecked() != checked:
                    self._btn_control_source.blockSignals(True)
                    self._btn_control_source.setChecked(checked)
                    self._btn_control_source.blockSignals(False)
                self._control_source_mode = runtime_mode
                self._btn_control_source.setText(f"Control Source: {'FLYSKY' if checked else 'APP'}")
            if hasattr(self, "_lbl_control_source_status"):
                rc_link_active = io_runtime.get("rc_link_active") if io_is_live else None
                rc_override_active = io_runtime.get("rc_override_active") if io_is_live else None
                rc_failsafe_active = io_runtime.get("rc_failsafe_active") if io_is_live else None
                rc_frame_age_ms = io_runtime.get("rc_frame_age_ms") if io_is_live else None
                rc_channels = io_runtime.get("rc_channels") if io_is_live else {}
                if runtime_mode:
                    detail = f"Mode {runtime_mode.upper()}"
                    if runtime_active:
                        detail += f" • active {runtime_active.upper()}"
                    if rc_link_active is not None:
                        detail += f" • rc link {'ON' if bool(rc_link_active) else 'OFF'}"
                    if rc_override_active is not None:
                        detail += f" • override {'ON' if bool(rc_override_active) else 'OFF'}"
                    if rc_failsafe_active is not None:
                        detail += f" • failsafe {'ON' if bool(rc_failsafe_active) else 'OFF'}"
                    if rc_frame_age_ms is not None:
                        detail += f" • {int(rc_frame_age_ms)}ms"
                    if isinstance(rc_channels, dict) and rc_channels:
                        ch4 = rc_channels.get("ch4_us")
                        ch5 = rc_channels.get("ch5_us")
                        ch6 = rc_channels.get("ch6_us")
                        channel_parts = []
                        if ch4 is not None:
                            channel_parts.append(f"CH4 {int(ch4)}")
                        if ch5 is not None:
                            channel_parts.append(f"CH5 {int(ch5)}")
                        if ch6 is not None:
                            channel_parts.append(f"CH6 {int(ch6)}")
                        if channel_parts:
                            detail += " • " + " / ".join(channel_parts)
                        style = self._compact_status_style("ok", bold=True) if runtime_mode == "rc" else self._compact_status_style("meta", bold=True)
                        self._set_label_content(self._lbl_control_source_status, f"FlySky mode: {detail}", style)
                    else:
                        self._set_label_content(self._lbl_control_source_status, "FlySky mode: waiting for bridge runtime", self._compact_status_style("meta", bold=True))
            if hasattr(self, "_lbl_fire_interlock_status"):
                io_age = io_runtime.get("age_s")
                io_is_live = io_age is not None and float(io_age) <= 2.0
                hw_arm_enabled = io_runtime.get("hw_arm_enabled") if io_is_live else None
                switch_in = io_runtime.get("switch_in") if io_is_live else None
                current_fault = io_runtime.get("current_fault") if io_is_live else None
                if switch_supported is False:
                    if current_fault is not None and bool(current_fault):
                        text = "Manual fire interlock: blocked by fault"
                        style = self._status_text_style("error")
                    elif safety_text != "ARMED":
                        text = "Manual fire interlock: software safety still locked"
                        style = self._status_text_style("warn")
                    else:
                        text = "Manual fire interlock: ready, no hardware switch configured"
                        style = self._status_text_style("ok")
                elif hw_arm_enabled is None:
                    text = "Manual fire interlock: waiting for bridge hardware state"
                    style = self._status_text_style("neutral")
                elif current_fault is not None and bool(current_fault):
                    text = "Manual fire interlock: blocked by fault"
                    style = self._status_text_style("error")
                elif int(hw_arm_enabled) == 0:
                    switch_state = "open" if int(switch_in or 0) == 0 else "not enabled"
                    text = f"Manual fire interlock: blocked, switch {switch_state}"
                    style = self._status_text_style("error")
                elif safety_text != "ARMED":
                    text = "Manual fire interlock: hardware ready, software safety still locked"
                    style = self._status_text_style("warn")
                else:
                    text = "Manual fire interlock: ready, press FIRE to command trigger path"
                    style = self._status_text_style("ok")
                self._set_label_content(self._lbl_fire_interlock_status, text, style)
        if hasattr(self, "_lbl_servo_feedback"):
            feedback_age = feedback.get("age_s")
            feedback_pan = feedback.get("pan_deg")
            feedback_tilt = feedback.get("tilt_deg")
            if feedback_pan is not None and feedback_tilt is not None and feedback_age is not None:
                pan_err = float(feedback_pan) - current_pan
                tilt_err = float(feedback_tilt) - current_tilt
                is_stale = float(feedback_age) > 1.5
                status_word = "stale" if is_stale else "live"
                self._set_label_content(
                    self._lbl_servo_feedback,
                    f"Feedback {status_word} • Meas {float(feedback_pan):.1f}/{float(feedback_tilt):.1f}° • "
                    f"Err {pan_err:+.1f}/{tilt_err:+.1f}° • age {float(feedback_age):.2f}s",
                    self._status_text_style("warn" if is_stale else "ok"),
                )
            else:
                source = str(feedback.get("source") or "inactive")
                last_error = str(feedback.get("last_error") or "").strip()
                commanded_pose_time = float(getattr(self, "_last_commanded_pose_time_s", 0.0) or 0.0)
                commanded_pan = float(getattr(self, "_last_commanded_pan", current_pan))
                commanded_tilt = float(getattr(self, "_last_commanded_tilt", current_tilt))
                command_age_s = max(0.0, time.time() - commanded_pose_time) if commanded_pose_time > 0.0 else None
                if source == "waiting":
                    message = last_error or "Waiting for first servo feedback reply"
                    style = self._status_text_style("warn")
                elif source == "disconnected":
                    message = "Disconnected"
                    style = self._status_text_style("neutral")
                else:
                    message = "Inactive in this connection mode"
                    style = self._status_text_style("neutral")
                if command_age_s is not None:
                    self._set_label_content(
                        self._lbl_servo_feedback,
                        f"Feedback pending • Cmd {commanded_pan:.1f}/{commanded_tilt:.1f}° • UI {current_pan:.1f}/{current_tilt:.1f}° • {message} • age {command_age_s:.2f}s",
                        style,
                    )
                else:
                    self._set_label_content(self._lbl_servo_feedback, f"Feedback: {message}", style)
        blocked_mask = str(stats.get('no_fire_mask') or '')
        if hasattr(self, "_lbl_no_fire_status"):
            if blocked_mask:
                self._set_label_content(self._lbl_no_fire_status, f"No-fire: blocked by {blocked_mask}", self._status_text_style("error"))
            else:
                self._set_label_content(self._lbl_no_fire_status, "No-fire: clear", self._status_text_style("ok"))
        if hasattr(self, "_lbl_recovery_status"):
            loss_phase = str(stats.get('loss_recovery_phase') or '').strip()
            if loss_phase:
                phase_text = loss_phase.replace('_', ' ').title()
                reacquire_note = str(stats.get('reacquire_note') or '').strip()
                if reacquire_note:
                    self._set_label_content(self._lbl_recovery_status, f"Recovery: {phase_text} • {reacquire_note}", self._status_text_style("warn"))
                else:
                    self._set_label_content(self._lbl_recovery_status, f"Recovery: {phase_text}", self._status_text_style("warn"))
            else:
                self._set_label_content(self._lbl_recovery_status, "Recovery: idle", self._status_text_style("neutral"))
        if blocked_mask != self._last_blocked_mask_seen:
            if blocked_mask:
                self._log(f"No-fire mask active: {blocked_mask}")
            elif self._last_blocked_mask_seen:
                self._log("No-fire mask cleared")
            self._last_blocked_mask_seen = blocked_mask
        if getattr(self, "_chk_mask_trace", None) is not None and self._chk_mask_trace.isChecked():
            self._emit_mask_trace(blocked_mask)
        elif self._last_mask_trace_snapshot:
            self._last_mask_trace_snapshot = ""
        reacquire_note = str(stats.get('reacquire_note') or '')
        if stats.get('reacquire_recent') and reacquire_note and reacquire_note != self._last_reacquire_note_seen:
            self._last_reacquire_note_seen = reacquire_note
            self._log(f"Tracking {reacquire_note}")
        pir_note = str(stats.get('pir_note') or '')
        if stats.get('pir_recent') and pir_note and pir_note != self._last_pir_note_seen:
            self._last_pir_note_seen = pir_note
            self._log(pir_note)
        # Update last-command diagnostic in connection tab
        if hasattr(self, "_lbl_last_cmd") and self._last_visible_command_text:
            self._set_label_content(self._lbl_last_cmd, f"Last: {self._last_visible_command_text}", self._compact_status_style("neutral"))
        
        # Update PIR status display in Guard tab
        if hasattr(self, "_lbl_pir_status"):
            self._update_pir_status_display()
        self._update_prompted_status_label()

    def _dump_mask_trace_snapshot(self) -> None:
        blocked_mask = str(self.engine.get_engagement_stats().get('no_fire_mask') or '')
        self._emit_mask_trace(blocked_mask, force=True)

    def _emit_mask_trace(self, blocked_mask: str, force: bool = False) -> None:
        frame_w = max(1, int(self.config.guard.frame_width or 1))
        frame_h = max(1, int(self.config.guard.frame_height or 1))
        summaries: List[str] = []
        for mask in self.config.no_fire_masks:
            if not bool(mask.enabled):
                continue
            points = project_mask_to_frame(
                mask,
                self.engine.current_pan,
                self.engine.current_tilt,
                self.config.guard.camera_hfov,
                self.config.guard.camera_vfov,
                frame_w,
                frame_h,
            )
            visible_points = sum(1 for px, py in points if 0 <= int(px) < frame_w and 0 <= int(py) < frame_h)
            summaries.append(f"{mask.name}:{visible_points}/{len(points)}")
        snapshot = (
            f"pan={self.engine.current_pan:.1f}|tilt={self.engine.current_tilt:.1f}|"
            f"blocked={blocked_mask or '-'}|masks={';'.join(summaries) if summaries else 'none'}"
        )
        if force or snapshot != self._last_mask_trace_snapshot:
            self._last_mask_trace_snapshot = snapshot
            self._log(f"Mask trace: {snapshot}")

    def _classify_log_message(self, msg: str) -> str:
        text = str(msg or "").lower()
        if "pir" in text:
            return "pir"
        if any(token in text for token in ("fire", "safety", "mask", "blocked", "warn", "engag")):
            return "safety"
        if any(token in text for token in ("laser", "led", "acc", "spare", "control source", "app ctrl")):
            return "accessory"
        if any(token in text for token in ("camera", "video", "snapshot", "frame", "model", "yolo")):
            return "camera"
        if any(token in text for token in ("move", "pan", "tilt", "rest", "home", "sweep", "patrol", "tracking", "recovery", "search", "hunt", "servo", "feedback", "guard")):
            return "movement"
        return "system"

    def _format_log_line(self, timestamp: str, category: str, msg: str) -> str:
        label = category.upper()
        return f"[{timestamp}] [{label}] {msg}"

    def _entry_matches_log_filter(self, category: str) -> bool:
        active_filter = str(getattr(self, "_log_filter_key", "all") or "all")
        return active_filter == "all" or active_filter == str(category)

    def _serialize_log_entries(self, *, include_filter: bool) -> str:
        lines: List[str] = []
        for timestamp, category, msg in getattr(self, "_log_entries", []):
            if include_filter and not self._entry_matches_log_filter(category):
                continue
            lines.append(self._format_log_line(timestamp, category, msg))
        return "\n".join(lines)

    def _render_serial_log(self, *, force_scroll: bool = False) -> None:
        if not hasattr(self, "_log_text") or self._log_text is None:
            return
        scroll_bar = self._log_text.verticalScrollBar()
        was_at_bottom = force_scroll or scroll_bar.value() >= max(0, scroll_bar.maximum() - 6)
        self._log_text.setPlainText(self._serialize_log_entries(include_filter=True))
        if was_at_bottom:
            scroll_bar.setValue(scroll_bar.maximum())

    def _sync_log_controls(self) -> None:
        paused = bool(getattr(self, "_log_paused", False))
        pending = int(getattr(self, "_log_paused_pending_count", 0) or 0)
        if hasattr(self, "_btn_log_pause"):
            self._btn_log_pause.setEnabled(not paused)
        if hasattr(self, "_btn_log_resume"):
            self._btn_log_resume.setEnabled(paused)
            self._btn_log_resume.setText(f"Resume ({pending})" if paused and pending > 0 else "Resume")
        if hasattr(self, "_lbl_log_state"):
            self._lbl_log_state.setText(f"Paused ({pending} queued)" if paused and pending > 0 else ("Paused" if paused else "Live"))
        for key, button in getattr(self, "_log_filter_buttons", {}).items():
            button.blockSignals(True)
            button.setChecked(str(key) == str(getattr(self, "_log_filter_key", "all")))
            button.blockSignals(False)

    def _set_log_pause(self, paused: bool) -> None:
        self._log_paused = bool(paused)
        if not self._log_paused:
            self._log_paused_pending_count = 0
            self._render_serial_log(force_scroll=True)
        self._sync_log_controls()

    def _set_log_filter(self, filter_key: str) -> None:
        selected = str(filter_key or "all")
        if selected not in dict(SERIAL_LOG_FILTER_SPECS):
            selected = "all"
        self._log_filter_key = selected
        self._render_serial_log(force_scroll=True)
        self._sync_log_controls()

    def _clear_serial_log(self) -> None:
        self._log_entries.clear()
        self._log_paused_pending_count = 0
        if hasattr(self, "_log_text") and self._log_text is not None:
            self._log_text.clear()
        self._sync_log_controls()

    def _log(self, msg: str) -> None:
        if QThread.currentThread() != self.thread():
            try:
                self._log_requested.emit(str(msg))
            except Exception:
                print(f"[SENTRY_V2_TAB] {msg}", flush=True)
            return
        ts = time.strftime("%H:%M:%S")
        category = self._classify_log_message(msg)
        self._log_entries.append((ts, category, str(msg)))
        if bool(getattr(self, "_log_paused", False)):
            self._log_paused_pending_count += 1
            self._sync_log_controls()
            return
        self._render_serial_log(force_scroll=True)
        self._sync_log_controls()

    def _report_runtime_warning(self, context: str, exc: Exception) -> None:
        message = f"{context}: {exc}"
        try:
            if hasattr(self, "_log_text") and self._log_text is not None and not self._closing:
                self._log(f"[WARN] {message}")
                return
        except Exception:
            pass
        print(f"[SENTRY_V2_TAB] {message}", flush=True)

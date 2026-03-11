"""
Smart Sentry v2 — Tab Widget (PyQt5 UI)

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

import time
from typing import List, Optional, Tuple

import cv2
import numpy as np
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QCheckBox, QSlider, QGroupBox, QFrame, QSizePolicy,
    QSpacerItem, QScrollArea, QDoubleSpinBox, QSpinBox,
    QComboBox, QListWidget, QListWidgetItem, QAbstractItemView,
    QTabWidget, QTextEdit, QGridLayout,
)
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtGui import QImage, QPixmap

from .sentry_v2_config import SentryV2Config, YOLO_COCO_CLASSES
from .sentry_v2_engine import SentryV2Engine, SentryV2State
from .sentry_v2_overlay import SentryV2Overlay
from .target_filter import DetectedObject

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
    "Filtered Target Mode",        # 10
]

# Color presets available
COLOR_PRESETS: List[str] = [
    "red", "green", "blue", "yellow", "orange", "purple",
    "cyan", "white", "black", "custom",
]


class SentryV2TabWidget(QWidget):
    """
    Complete Smart Sentry v2 tab widget.

    Signals for main app integration:
        turret_move_requested(pan, tilt)
        fire_requested(burst_count)
        sentry_enabled_changed(enabled)
        detection_mode_changed(mode_index)
        trigger_mode_changed(is_bb)
        toggle_led_requested(on)
        toggle_laser_requested(on)
        toggle_safety_requested()
        go_home_requested()
        manual_move_requested(pan_delta, tilt_delta)
        manual_fire_requested(state)  # 1=press, 0=release
        auto_trigger_changed(enabled)
        color_preset_changed(preset_name)
    """

    # Core signals (same as v1 interface)
    turret_move_requested = pyqtSignal(float, float)
    fire_requested = pyqtSignal(int)
    sentry_enabled_changed = pyqtSignal(bool)

    # New signals for extended controls
    detection_mode_changed = pyqtSignal(int)
    trigger_mode_changed = pyqtSignal(bool)
    toggle_led_requested = pyqtSignal(bool)
    toggle_laser_requested = pyqtSignal(bool)
    toggle_safety_requested = pyqtSignal()
    go_home_requested = pyqtSignal()
    manual_move_requested = pyqtSignal(int, int)  # pan_step, tilt_step
    manual_fire_requested = pyqtSignal(int)        # 1=press, 0=release
    auto_trigger_changed = pyqtSignal(bool)
    color_preset_changed = pyqtSignal(str)

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)

        # Config (try loading saved, else defaults)
        self.config = SentryV2Config.load("config/sentry_v2_settings.json")

        # Engine
        self.engine = SentryV2Engine(self.config)
        self.engine.on_fire(self._on_engine_fire)
        self.engine.on_move(self._on_engine_move)
        self.engine.on_state_change(self._on_engine_state_change)

        # Overlay
        self.overlay = SentryV2Overlay(self.config)

        # Track accessory states locally for button text
        self._led_on = False
        self._laser_on = False
        self._safety_armed = False

        # Build UI
        self._build_ui()

        # Status refresh timer
        self._status_timer = QTimer(self)
        self._status_timer.timeout.connect(self._refresh_status)
        self._status_timer.start(500)

    # ================================================================== #
    #  UI Construction
    # ================================================================== #

    def _build_ui(self) -> None:
        root = QHBoxLayout(self)
        root.setContentsMargins(4, 4, 4, 4)

        # --- Left: video feed ---
        self._video_label = QLabel("Waiting for video...")
        self._video_label.setAlignment(Qt.AlignCenter)
        self._video_label.setMinimumSize(480, 360)
        self._video_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self._video_label.setStyleSheet("background: #111; color: #888;")
        root.addWidget(self._video_label, stretch=3)

        # --- Right: controls in scrollable panel ---
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setMaximumWidth(420)

        panel = QWidget()
        panel_layout = QVBoxLayout(panel)
        panel_layout.setContentsMargins(4, 4, 4, 4)
        panel_layout.setSpacing(6)

        # Enable toggle
        self._chk_enable = QCheckBox("Enable Smart Sentry")
        self._chk_enable.setStyleSheet("font-weight: bold; font-size: 13px;")
        self._chk_enable.toggled.connect(self._on_enable_toggled)
        panel_layout.addWidget(self._chk_enable)

        # Sub-tabs for settings categories
        settings_tabs = QTabWidget()
        settings_tabs.setTabPosition(QTabWidget.North)

        settings_tabs.addTab(self._build_detection_tab(), "Detection")
        settings_tabs.addTab(self._build_filter_tab(), "Target Filter")
        settings_tabs.addTab(self._build_scoring_tab(), "Threat AI")
        settings_tabs.addTab(self._build_engagement_tab(), "Engage")
        settings_tabs.addTab(self._build_guard_tab(), "Guard")
        settings_tabs.addTab(self._build_controls_tab(), "Controls")

        panel_layout.addWidget(settings_tabs, stretch=1)

        # Status / log
        panel_layout.addWidget(self._build_status_group())

        scroll.setWidget(panel)
        root.addWidget(scroll, stretch=1)

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
        mode_lay.addWidget(self._combo_detection_mode)

        # Description label
        self._lbl_mode_desc = QLabel("")
        self._lbl_mode_desc.setWordWrap(True)
        self._lbl_mode_desc.setStyleSheet("color: #aaa; font-size: 11px;")
        mode_lay.addWidget(self._lbl_mode_desc)
        self._update_mode_description()

        lay.addWidget(grp_mode)

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
        contour_lay.addWidget(self._spin_min_contour, 0, 1)

        contour_lay.addWidget(QLabel("Max Area (px):"), 1, 0)
        self._spin_max_contour = QDoubleSpinBox()
        self._spin_max_contour.setRange(0, 5000000)
        self._spin_max_contour.setSingleStep(10000)
        self._spin_max_contour.setDecimals(0)
        self._spin_max_contour.setValue(self.config.detection_mode.max_contour_area)
        self._spin_max_contour.valueChanged.connect(self._on_detection_settings_changed)
        contour_lay.addWidget(self._spin_max_contour, 1, 1)

        lay.addWidget(self._grp_contour)

        # --- YOLO settings (modes 2,4,5,9,10) ---
        self._grp_yolo = QGroupBox("YOLO Settings")
        yolo_lay = QGridLayout(self._grp_yolo)

        yolo_lay.addWidget(QLabel("Min Area (px):"), 0, 0)
        self._spin_yolo_min_area = QSpinBox()
        self._spin_yolo_min_area.setRange(0, 10000000)
        self._spin_yolo_min_area.setSingleStep(100)
        self._spin_yolo_min_area.setValue(self.config.detection_mode.yolo_min_area)
        self._spin_yolo_min_area.valueChanged.connect(self._on_detection_settings_changed)
        yolo_lay.addWidget(self._spin_yolo_min_area, 0, 1)

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
        color_lay.addWidget(self._combo_color_preset, 0, 1)

        color_lay.addWidget(QLabel("Min Area (px):"), 1, 0)
        self._spin_color_min = QSpinBox()
        self._spin_color_min.setRange(1, 5000000)
        self._spin_color_min.setSingleStep(50)
        self._spin_color_min.setValue(self.config.detection_mode.color_min_area)
        self._spin_color_min.valueChanged.connect(self._on_color_settings_changed)
        color_lay.addWidget(self._spin_color_min, 1, 1)

        color_lay.addWidget(QLabel("Max Area (px):"), 2, 0)
        self._spin_color_max = QSpinBox()
        self._spin_color_max.setRange(1, 5000000)
        self._spin_color_max.setSingleStep(1000)
        self._spin_color_max.setValue(self.config.detection_mode.color_max_area)
        self._spin_color_max.valueChanged.connect(self._on_color_settings_changed)
        color_lay.addWidget(self._spin_color_max, 2, 1)

        color_lay.addWidget(QLabel("Fusion Strategy:"), 3, 0)
        self._combo_fusion = QComboBox()
        self._combo_fusion.addItems(["AND", "OR"])
        self._combo_fusion.setCurrentText(self.config.detection_mode.color_fusion_strategy)
        self._combo_fusion.currentTextChanged.connect(self._on_color_settings_changed)
        color_lay.addWidget(self._combo_fusion, 3, 1)

        color_lay.addWidget(QLabel("Fusion Overlap (%):"), 4, 0)
        self._spin_fusion_overlap = QSpinBox()
        self._spin_fusion_overlap.setRange(0, 100)
        self._spin_fusion_overlap.setValue(self.config.detection_mode.color_fusion_overlap)
        self._spin_fusion_overlap.valueChanged.connect(self._on_color_settings_changed)
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
        motion_lay.addWidget(self._spin_motion_thresh)

        lay.addWidget(self._grp_motion)

        lay.addStretch()

        # Initial visibility
        self._update_detection_panel_visibility()
        return w

    # ------------------------------------------------------------------ #
    #  Target Filter Tab
    # ------------------------------------------------------------------ #

    def _build_filter_tab(self) -> QWidget:
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(4)

        # Class whitelist
        grp = QGroupBox("Allowed YOLO Classes")
        g_lay = QVBoxLayout(grp)
        self._class_list = QListWidget()
        self._class_list.setSelectionMode(QAbstractItemView.MultiSelection)
        allowed = set(self.config.target_filter.allowed_classes)
        for cls_name in YOLO_COCO_CLASSES:
            item = QListWidgetItem(cls_name)
            self._class_list.addItem(item)
            if cls_name in allowed:
                item.setSelected(True)
        self._class_list.setMaximumHeight(160)
        self._class_list.itemSelectionChanged.connect(self._on_class_selection_changed)
        g_lay.addWidget(self._class_list)

        btn_row = QHBoxLayout()
        btn_all = QPushButton("All")
        btn_all.clicked.connect(self._select_all_classes)
        btn_none = QPushButton("None")
        btn_none.clicked.connect(self._select_no_classes)
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
        maxs_row.addWidget(self._spin_max_size)
        lay.addLayout(maxs_row)

        lay.addStretch()
        return w

    # ------------------------------------------------------------------ #
    #  Threat AI Tab
    # ------------------------------------------------------------------ #

    def _build_scoring_tab(self) -> QWidget:
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(4)

        lay.addWidget(QLabel("Threat Score Weights (higher = more important):"))

        self._weight_sliders = {}
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
            row.addWidget(lbl)
            slider = QSlider(Qt.Horizontal)
            slider.setRange(0, 100)
            slider.setValue(int(default * 100))
            slider.valueChanged.connect(self._on_scoring_changed)
            row.addWidget(slider)
            val_lbl = QLabel(f"{default:.2f}")
            val_lbl.setMinimumWidth(35)
            slider.valueChanged.connect(lambda v, l=val_lbl: l.setText(f"{v / 100:.2f}"))
            row.addWidget(val_lbl)
            self._weight_sliders[key] = slider
            lay.addLayout(row)

        # ML toggle
        self._chk_ml = QCheckBox("Enable ML scoring refinement (requires sklearn)")
        self._chk_ml.setChecked(self.config.threat_scoring.use_ml_model)
        self._chk_ml.toggled.connect(self._on_scoring_changed)
        lay.addWidget(self._chk_ml)

        lay.addStretch()
        return w

    # ------------------------------------------------------------------ #
    #  Engagement Tab
    # ------------------------------------------------------------------ #

    def _build_engagement_tab(self) -> QWidget:
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(4)

        # Auto-Trigger toggle (prominent)
        self._chk_auto_trigger = QCheckBox("Auto-Trigger (fire automatically)")
        self._chk_auto_trigger.setStyleSheet("font-weight: bold; color: #ff6644;")
        self._chk_auto_trigger.setChecked(self.config.engagement.auto_trigger_enabled)
        self._chk_auto_trigger.toggled.connect(self._on_auto_trigger_toggled)
        lay.addWidget(self._chk_auto_trigger)

        # Trigger mode
        trig_row = QHBoxLayout()
        trig_row.addWidget(QLabel("Trigger Mode:"))
        self._combo_trigger_mode = QComboBox()
        self._combo_trigger_mode.addItems(["Water (MOSFET)", "Projectile (BB Servo)"])
        self._combo_trigger_mode.setCurrentIndex(1 if self.config.engagement.trigger_mode_bb else 0)
        self._combo_trigger_mode.currentIndexChanged.connect(self._on_trigger_mode_changed)
        trig_row.addWidget(self._combo_trigger_mode)
        lay.addLayout(trig_row)

        # Min threat to engage
        row = QHBoxLayout()
        row.addWidget(QLabel("Min threat to engage:"))
        self._spin_min_threat = QDoubleSpinBox()
        self._spin_min_threat.setRange(0.05, 0.95)
        self._spin_min_threat.setSingleStep(0.05)
        self._spin_min_threat.setValue(self.config.engagement.min_threat_score)
        self._spin_min_threat.valueChanged.connect(self._on_engagement_changed)
        row.addWidget(self._spin_min_threat)
        lay.addLayout(row)

        # Burst count
        row2 = QHBoxLayout()
        row2.addWidget(QLabel("Burst shots:"))
        self._spin_burst = QSpinBox()
        self._spin_burst.setRange(1, 10)
        self._spin_burst.setValue(self.config.engagement.burst_count)
        self._spin_burst.valueChanged.connect(self._on_engagement_changed)
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
        row3.addWidget(self._spin_burst_interval)
        lay.addLayout(row3)

        # Inter-target cooldown
        row4 = QHBoxLayout()
        row4.addWidget(QLabel("Inter-target cooldown (s):"))
        self._spin_inter_cd = QDoubleSpinBox()
        self._spin_inter_cd.setRange(0.1, 5.0)
        self._spin_inter_cd.setSingleStep(0.1)
        self._spin_inter_cd.setValue(self.config.engagement.inter_target_cooldown)
        self._spin_inter_cd.valueChanged.connect(self._on_engagement_changed)
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
        row5.addWidget(self._spin_cycle_cd)
        lay.addLayout(row5)

        # Max queue
        row6 = QHBoxLayout()
        row6.addWidget(QLabel("Max targets per cycle:"))
        self._spin_max_queue = QSpinBox()
        self._spin_max_queue.setRange(1, 10)
        self._spin_max_queue.setValue(self.config.engagement.max_queue_length)
        self._spin_max_queue.valueChanged.connect(self._on_engagement_changed)
        row6.addWidget(self._spin_max_queue)
        lay.addLayout(row6)

        # Optimize slew
        self._chk_optimize = QCheckBox("Optimise servo travel order")
        self._chk_optimize.setChecked(self.config.engagement.optimize_slew_order)
        self._chk_optimize.toggled.connect(self._on_engagement_changed)
        lay.addWidget(self._chk_optimize)

        # Engagement speed
        row7 = QHBoxLayout()
        row7.addWidget(QLabel("Engagement speed:"))
        self._slider_speed = QSlider(Qt.Horizontal)
        self._slider_speed.setRange(10, 100)
        self._slider_speed.setValue(self.config.engagement.engagement_speed)
        self._slider_speed.valueChanged.connect(self._on_engagement_changed)
        row7.addWidget(self._slider_speed)
        self._lbl_speed = QLabel(str(self.config.engagement.engagement_speed))
        self._slider_speed.valueChanged.connect(lambda v: self._lbl_speed.setText(str(v)))
        row7.addWidget(self._lbl_speed)
        lay.addLayout(row7)

        # --- Precision Aiming ---
        prec_grp = QGroupBox("Precision Aiming (small/distant targets)")
        prec_lay = QGridLayout(prec_grp)

        self._chk_precision = QCheckBox("Enable precision refinement")
        self._chk_precision.setChecked(self.config.engagement.precision_aim_enabled)
        self._chk_precision.toggled.connect(self._on_engagement_changed)
        prec_lay.addWidget(self._chk_precision, 0, 0, 1, 2)

        prec_lay.addWidget(QLabel("Settle time (s):"), 1, 0)
        self._spin_prec_settle = QDoubleSpinBox()
        self._spin_prec_settle.setRange(0.1, 3.0)
        self._spin_prec_settle.setSingleStep(0.1)
        self._spin_prec_settle.setValue(self.config.engagement.precision_settle_time)
        self._spin_prec_settle.valueChanged.connect(self._on_engagement_changed)
        prec_lay.addWidget(self._spin_prec_settle, 1, 1)

        prec_lay.addWidget(QLabel("Max step (deg):"), 2, 0)
        self._spin_prec_step = QDoubleSpinBox()
        self._spin_prec_step.setRange(0.1, 5.0)
        self._spin_prec_step.setSingleStep(0.1)
        self._spin_prec_step.setValue(self.config.engagement.precision_max_step)
        self._spin_prec_step.valueChanged.connect(self._on_engagement_changed)
        prec_lay.addWidget(self._spin_prec_step, 2, 1)

        lay.addWidget(prec_grp)

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

        # Guard pan
        row = QHBoxLayout()
        row.addWidget(QLabel("Guard Pan (deg):"))
        self._spin_guard_pan = QDoubleSpinBox()
        self._spin_guard_pan.setRange(5.0, 185.0)
        self._spin_guard_pan.setSingleStep(1.0)
        self._spin_guard_pan.setValue(self.config.guard.guard_pan)
        self._spin_guard_pan.valueChanged.connect(self._on_guard_changed)
        row.addWidget(self._spin_guard_pan)
        lay.addLayout(row)

        # Guard tilt
        row2 = QHBoxLayout()
        row2.addWidget(QLabel("Guard Tilt (deg):"))
        self._spin_guard_tilt = QDoubleSpinBox()
        self._spin_guard_tilt.setRange(10.0, 130.0)
        self._spin_guard_tilt.setSingleStep(1.0)
        self._spin_guard_tilt.setValue(self.config.guard.guard_tilt)
        self._spin_guard_tilt.valueChanged.connect(self._on_guard_changed)
        row2.addWidget(self._spin_guard_tilt)
        lay.addLayout(row2)

        # Camera FOV
        row3 = QHBoxLayout()
        row3.addWidget(QLabel("Camera HFOV (deg):"))
        self._spin_hfov = QDoubleSpinBox()
        self._spin_hfov.setRange(30.0, 180.0)
        self._spin_hfov.setSingleStep(5.0)
        self._spin_hfov.setValue(self.config.guard.camera_hfov)
        self._spin_hfov.valueChanged.connect(self._on_guard_changed)
        row3.addWidget(self._spin_hfov)
        lay.addLayout(row3)

        row4 = QHBoxLayout()
        row4.addWidget(QLabel("Camera VFOV (deg):"))
        self._spin_vfov = QDoubleSpinBox()
        self._spin_vfov.setRange(20.0, 140.0)
        self._spin_vfov.setSingleStep(5.0)
        self._spin_vfov.setValue(self.config.guard.camera_vfov)
        self._spin_vfov.valueChanged.connect(self._on_guard_changed)
        row4.addWidget(self._spin_vfov)
        lay.addLayout(row4)

        # Go to guard button
        btn = QPushButton("Go To Guard Position")
        btn.clicked.connect(self._go_to_guard)
        lay.addWidget(btn)

        # Set current as guard
        btn2 = QPushButton("Set Current Position As Guard")
        btn2.setToolTip("Uses turret's current pan/tilt as the new guard position")
        btn2.clicked.connect(self._set_current_as_guard)
        lay.addWidget(btn2)

        # Overlay toggles
        lay.addWidget(QLabel(""))  # spacer
        self._chk_overlay = QCheckBox("Show overlay")
        self._chk_overlay.setChecked(self.config.show_overlay)
        self._chk_overlay.toggled.connect(self._on_overlay_changed)
        lay.addWidget(self._chk_overlay)

        self._chk_scores = QCheckBox("Show threat scores")
        self._chk_scores.setChecked(self.config.show_threat_scores)
        self._chk_scores.toggled.connect(self._on_overlay_changed)
        lay.addWidget(self._chk_scores)

        self._chk_zone = QCheckBox("Show engagement zone")
        self._chk_zone.setChecked(self.config.show_engagement_zone)
        self._chk_zone.toggled.connect(self._on_overlay_changed)
        lay.addWidget(self._chk_zone)

        lay.addStretch()
        return w

    # ------------------------------------------------------------------ #
    #  Manual Controls Tab
    # ------------------------------------------------------------------ #

    def _build_controls_tab(self) -> QWidget:
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(4, 4, 4, 4)
        lay.setSpacing(6)

        # --- D-pad manual movement ---
        dpad_grp = QGroupBox("Manual Movement")
        dpad_lay = QVBoxLayout(dpad_grp)

        # Speed / step controls
        spd_row = QHBoxLayout()
        spd_row.addWidget(QLabel("Step (deg):"))
        self._spin_step = QSpinBox()
        self._spin_step.setRange(1, 20)
        self._spin_step.setValue(5)
        spd_row.addWidget(self._spin_step)
        dpad_lay.addLayout(spd_row)

        # D-pad grid
        grid = QGridLayout()
        btn_up = QPushButton("\u25B2")  # up arrow
        btn_up.setFixedSize(50, 40)
        btn_up.clicked.connect(lambda: self._manual_move(0, -1))
        grid.addWidget(btn_up, 0, 1)

        btn_left = QPushButton("\u25C0")  # left arrow
        btn_left.setFixedSize(50, 40)
        btn_left.clicked.connect(lambda: self._manual_move(-1, 0))
        grid.addWidget(btn_left, 1, 0)

        btn_home = QPushButton("H")
        btn_home.setFixedSize(50, 40)
        btn_home.setToolTip("Go Home")
        btn_home.clicked.connect(self._on_home_clicked)
        grid.addWidget(btn_home, 1, 1)

        btn_right = QPushButton("\u25B6")  # right arrow
        btn_right.setFixedSize(50, 40)
        btn_right.clicked.connect(lambda: self._manual_move(1, 0))
        grid.addWidget(btn_right, 1, 2)

        btn_down = QPushButton("\u25BC")  # down arrow
        btn_down.setFixedSize(50, 40)
        btn_down.clicked.connect(lambda: self._manual_move(0, 1))
        grid.addWidget(btn_down, 2, 1)

        dpad_lay.addLayout(grid)
        lay.addWidget(dpad_grp)

        # --- Accessories ---
        acc_grp = QGroupBox("Accessories")
        acc_lay = QGridLayout(acc_grp)

        self._btn_led = QPushButton("LED: OFF")
        self._btn_led.setCheckable(True)
        self._btn_led.toggled.connect(self._on_led_toggled)
        acc_lay.addWidget(self._btn_led, 0, 0)

        self._btn_laser = QPushButton("Laser: OFF")
        self._btn_laser.setCheckable(True)
        self._btn_laser.toggled.connect(self._on_laser_toggled)
        acc_lay.addWidget(self._btn_laser, 0, 1)

        self._btn_safety = QPushButton("Safety: LOCKED")
        self._btn_safety.setCheckable(True)
        self._btn_safety.setStyleSheet("QPushButton:checked { background: #cc3333; color: white; }")
        self._btn_safety.toggled.connect(self._on_safety_toggled)
        acc_lay.addWidget(self._btn_safety, 1, 0, 1, 2)

        lay.addWidget(acc_grp)

        # --- Manual Fire ---
        fire_grp = QGroupBox("Fire Control")
        fire_lay = QVBoxLayout(fire_grp)

        self._btn_fire = QPushButton("FIRE")
        self._btn_fire.setStyleSheet(
            "QPushButton { background: #444; color: white; font-weight: bold; font-size: 14px; padding: 8px; }"
            "QPushButton:pressed { background: #cc2222; }"
        )
        self._btn_fire.pressed.connect(lambda: self._on_manual_fire(1))
        self._btn_fire.released.connect(lambda: self._on_manual_fire(0))
        fire_lay.addWidget(self._btn_fire)

        lay.addWidget(fire_grp)

        lay.addStretch()
        return w

    # ------------------------------------------------------------------ #
    #  Status Group
    # ------------------------------------------------------------------ #

    def _build_status_group(self) -> QGroupBox:
        grp = QGroupBox("Status")
        lay = QVBoxLayout(grp)
        self._lbl_state = QLabel("State: PAUSED")
        self._lbl_state.setStyleSheet("font-weight: bold;")
        lay.addWidget(self._lbl_state)

        self._lbl_stats = QLabel("Targets: 0 | Qualified: 0 | Engaged: 0")
        lay.addWidget(self._lbl_stats)

        self._log_text = QTextEdit()
        self._log_text.setReadOnly(True)
        self._log_text.setMaximumHeight(120)
        self._log_text.setStyleSheet("font-size: 11px; font-family: monospace;")
        lay.addWidget(self._log_text)

        # Save config button
        btn_save = QPushButton("Save Settings")
        btn_save.clicked.connect(self._save_config)
        lay.addWidget(btn_save)

        return grp

    # ================================================================== #
    #  Public API (called by main app)
    # ================================================================== #

    def process_frame(
        self, frame: np.ndarray, detections: list
    ) -> None:
        """
        Called by main app every frame.

        ``detections`` format: list of (x, y, w, h, score) or
        (x, y, w, h, score, class_id) tuples.
        """
        now = time.time()
        h, w_frame = frame.shape[:2]

        # Update frame dimensions in config
        self.config.guard.frame_width = w_frame
        self.config.guard.frame_height = h

        # Convert raw detections to DetectedObject list
        det_objects = self._convert_detections(detections, w_frame, h)

        # Run engine
        self.engine.update(det_objects, now)

        # Draw overlay
        frame = self.overlay.draw(frame, self.engine)

        # Update video label
        self._show_frame(frame)

    def set_enabled(self, enabled: bool) -> None:
        self._chk_enable.setChecked(enabled)

    def is_enabled(self) -> bool:
        return self._chk_enable.isChecked()

    def get_detection_mode(self) -> int:
        """Return the currently selected detection mode index."""
        return self._combo_detection_mode.currentIndex()

    def sync_accessory_states(self, led: bool, laser: bool, safety_armed: bool) -> None:
        """Sync button states from main app without re-emitting signals."""
        self._led_on = led
        self._laser_on = laser
        self._safety_armed = safety_armed
        self._btn_led.blockSignals(True)
        self._btn_led.setChecked(led)
        self._btn_led.setText(f"LED: {'ON' if led else 'OFF'}")
        self._btn_led.blockSignals(False)
        self._btn_laser.blockSignals(True)
        self._btn_laser.setChecked(laser)
        self._btn_laser.setText(f"Laser: {'ON' if laser else 'OFF'}")
        self._btn_laser.blockSignals(False)
        self._btn_safety.blockSignals(True)
        self._btn_safety.setChecked(safety_armed)
        self._btn_safety.setText(f"Safety: {'ARMED' if safety_armed else 'LOCKED'}")
        self._btn_safety.blockSignals(False)

    # ================================================================== #
    #  Event Handlers
    # ================================================================== #

    def _on_enable_toggled(self, checked: bool) -> None:
        if checked:
            self._apply_all_config()
            self.engine.start()
            self._log("Smart Sentry ENABLED")
        else:
            self.engine.stop()
            self._log("Smart Sentry DISABLED")
        self.sentry_enabled_changed.emit(checked)

    def _on_engine_fire(self, burst_count: int) -> None:
        self.fire_requested.emit(burst_count)
        self._log(f"FIRE! Burst: {burst_count}")

    def _on_engine_move(self, pan: float, tilt: float) -> None:
        self.turret_move_requested.emit(pan, tilt)

    def _on_engine_state_change(self, old: SentryV2State, new: SentryV2State) -> None:
        self._lbl_state.setText(f"State: {new.name}")
        self._log(f"State: {old.name} -> {new.name}")

    # ------------------------------------------------------------------ #
    #  Detection mode handlers
    # ------------------------------------------------------------------ #

    def _on_detection_mode_changed(self, index: int) -> None:
        self.config.detection_mode.detection_mode = index
        self._update_mode_description()
        self._update_detection_panel_visibility()
        self.detection_mode_changed.emit(index)
        self._push_config()
        self._log(f"Detection mode: {DETECTION_MODES[index]}")

    def _on_detection_settings_changed(self) -> None:
        dm = self.config.detection_mode
        dm.min_contour_area = self._spin_min_contour.value()
        dm.max_contour_area = self._spin_max_contour.value()
        dm.yolo_min_area = self._spin_yolo_min_area.value()
        dm.motion_gate_threshold = self._spin_motion_thresh.value()
        self._push_config()

    def _on_color_settings_changed(self) -> None:
        dm = self.config.detection_mode
        dm.color_preset = self._combo_color_preset.currentText()
        dm.color_min_area = self._spin_color_min.value()
        dm.color_max_area = self._spin_color_max.value()
        dm.color_fusion_strategy = self._combo_fusion.currentText()
        dm.color_fusion_overlap = self._spin_fusion_overlap.value()
        self.color_preset_changed.emit(dm.color_preset)
        self._push_config()

    def _update_detection_panel_visibility(self) -> None:
        """Show/hide detection sub-panels based on selected mode."""
        mode = self._combo_detection_mode.currentIndex()
        contour_modes = {0, 1, 3, 7, 8}
        yolo_modes = {2, 4, 5, 9, 10}
        color_modes = {6, 7, 8, 9}
        motion_modes = {4, 5}

        self._grp_contour.setVisible(mode in contour_modes)
        self._grp_yolo.setVisible(mode in yolo_modes)
        self._grp_color.setVisible(mode in color_modes)
        self._grp_motion.setVisible(mode in motion_modes)

    def _update_mode_description(self) -> None:
        descs = {
            0: "Detects motion by comparing consecutive frames.",
            1: "Learns background over time, detects foreground objects.",
            2: "Uses YOLO neural network for object detection (most accurate).",
            3: "Combines frame difference and background subtraction.",
            4: "Frame difference gates YOLO: only runs YOLO when motion detected.",
            5: "Background subtraction gates YOLO (recommended hybrid).",
            6: "Detects objects by color using HSV filtering.",
            7: "Color detection + frame difference for moving colored objects.",
            8: "Color detection + background subtraction.",
            9: "Color detection fused with YOLO for precise colored object ID.",
            10: "Filtered target mode with advanced criteria.",
        }
        idx = self._combo_detection_mode.currentIndex()
        self._lbl_mode_desc.setText(descs.get(idx, ""))

    # ------------------------------------------------------------------ #
    #  Config change handlers
    # ------------------------------------------------------------------ #

    def _on_class_selection_changed(self) -> None:
        selected = [item.text() for item in self._class_list.selectedItems()]
        self.config.target_filter.allowed_classes = selected
        self._push_config()

    def _on_filter_changed(self) -> None:
        self.config.target_filter.min_confidence = self._spin_min_conf.value()
        self.config.target_filter.min_size_ratio = self._spin_min_size.value() / 100.0
        self.config.target_filter.max_size_ratio = self._spin_max_size.value() / 100.0
        self._push_config()

    def _on_scoring_changed(self) -> None:
        ts = self.config.threat_scoring
        for key, slider in self._weight_sliders.items():
            setattr(ts, key, slider.value() / 100.0)
        ts.use_ml_model = self._chk_ml.isChecked()
        self._push_config()

    def _on_engagement_changed(self) -> None:
        eg = self.config.engagement
        eg.min_threat_score = self._spin_min_threat.value()
        eg.burst_count = self._spin_burst.value()
        eg.burst_interval_ms = self._spin_burst_interval.value()
        eg.inter_target_cooldown = self._spin_inter_cd.value()
        eg.cycle_cooldown = self._spin_cycle_cd.value()
        eg.max_queue_length = self._spin_max_queue.value()
        eg.optimize_slew_order = self._chk_optimize.isChecked()
        eg.engagement_speed = self._slider_speed.value()
        eg.precision_aim_enabled = self._chk_precision.isChecked()
        eg.precision_settle_time = self._spin_prec_settle.value()
        eg.precision_max_step = self._spin_prec_step.value()
        self._push_config()

    def _on_guard_changed(self) -> None:
        g = self.config.guard
        g.guard_pan = self._spin_guard_pan.value()
        g.guard_tilt = self._spin_guard_tilt.value()
        g.camera_hfov = self._spin_hfov.value()
        g.camera_vfov = self._spin_vfov.value()
        self._push_config()

    def _on_overlay_changed(self) -> None:
        self.config.show_overlay = self._chk_overlay.isChecked()
        self.config.show_threat_scores = self._chk_scores.isChecked()
        self.config.show_engagement_zone = self._chk_zone.isChecked()
        self.overlay.update_config(self.config)

    # ------------------------------------------------------------------ #
    #  Auto-trigger / trigger mode
    # ------------------------------------------------------------------ #

    def _on_auto_trigger_toggled(self, checked: bool) -> None:
        self.config.engagement.auto_trigger_enabled = checked
        self.auto_trigger_changed.emit(checked)
        self._push_config()
        self._log(f"Auto-trigger: {'ON' if checked else 'OFF'}")

    def _on_trigger_mode_changed(self, index: int) -> None:
        is_bb = (index == 1)
        self.config.engagement.trigger_mode_bb = is_bb
        self.trigger_mode_changed.emit(is_bb)
        self._push_config()
        mode_name = "Projectile (BB)" if is_bb else "Water (MOSFET)"
        self._log(f"Trigger mode: {mode_name}")

    # ------------------------------------------------------------------ #
    #  Manual control handlers
    # ------------------------------------------------------------------ #

    def _manual_move(self, pan_dir: int, tilt_dir: int) -> None:
        step = self._spin_step.value()
        self.manual_move_requested.emit(pan_dir * step, tilt_dir * step)

    def _on_home_clicked(self) -> None:
        self.go_home_requested.emit()
        self._log("Go Home")

    def _on_led_toggled(self, checked: bool) -> None:
        self._led_on = checked
        self._btn_led.setText(f"LED: {'ON' if checked else 'OFF'}")
        self.toggle_led_requested.emit(checked)

    def _on_laser_toggled(self, checked: bool) -> None:
        self._laser_on = checked
        self._btn_laser.setText(f"Laser: {'ON' if checked else 'OFF'}")
        self.toggle_laser_requested.emit(checked)

    def _on_safety_toggled(self, checked: bool) -> None:
        self._safety_armed = checked
        self._btn_safety.setText(f"Safety: {'ARMED' if checked else 'LOCKED'}")
        self.toggle_safety_requested.emit()

    def _on_manual_fire(self, state: int) -> None:
        self.manual_fire_requested.emit(state)

    # ------------------------------------------------------------------ #
    #  Guard position buttons
    # ------------------------------------------------------------------ #

    def _go_to_guard(self) -> None:
        pan = self._spin_guard_pan.value()
        tilt = self._spin_guard_tilt.value()
        self.turret_move_requested.emit(pan, tilt)
        self._log(f"Moving to guard: P{pan:.0f} T{tilt:.0f}")

    def _set_current_as_guard(self) -> None:
        pan = self.engine.current_pan
        tilt = self.engine.current_tilt
        self._spin_guard_pan.setValue(pan)
        self._spin_guard_tilt.setValue(tilt)
        self._log(f"Guard set to current: P{pan:.0f} T{tilt:.0f}")

    def _select_all_classes(self) -> None:
        self._class_list.selectAll()

    def _select_no_classes(self) -> None:
        self._class_list.clearSelection()

    def _save_config(self) -> None:
        try:
            self.config.save()
            self._log("Settings saved")
        except Exception as e:
            self._log(f"Save error: {e}")

    # ------------------------------------------------------------------ #
    #  Internal helpers
    # ------------------------------------------------------------------ #

    def _push_config(self) -> None:
        """Push current config to engine and overlay."""
        self.engine.update_config(self.config)
        self.overlay.update_config(self.config)

    def _apply_all_config(self) -> None:
        """Read all UI controls into config before start."""
        self._on_detection_mode_changed(self._combo_detection_mode.currentIndex())
        self._on_detection_settings_changed()
        self._on_color_settings_changed()
        self._on_filter_changed()
        self._on_class_selection_changed()
        self._on_scoring_changed()
        self._on_engagement_changed()
        self._on_guard_changed()
        self._on_overlay_changed()

    def _convert_detections(
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
            class_name = (
                YOLO_COCO_CLASSES[class_id]
                if 0 <= class_id < len(YOLO_COCO_CLASSES)
                else "unknown"
            )
            cx = x + w / 2.0
            cy = y + h / 2.0
            result.append(DetectedObject(
                track_id=i,
                class_name=class_name,
                confidence=score,
                bbox=(x, y, w, h),
                center_x=cx,
                center_y=cy,
                frame_width=frame_w,
                frame_height=frame_h,
            ))
        return result

    def _show_frame(self, frame: np.ndarray) -> None:
        """Convert BGR frame to QPixmap and display."""
        try:
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rgb = np.ascontiguousarray(rgb)
            h, w, ch = rgb.shape
            qimg = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888).copy()
            pixmap = QPixmap.fromImage(qimg)
            label_size = self._video_label.size()
            if label_size.width() > 0 and label_size.height() > 0:
                scaled = pixmap.scaled(
                    label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
                self._video_label.setPixmap(scaled)
            else:
                self._video_label.setPixmap(pixmap)
        except Exception as e:
            print(f"[SENTRY_V2] _show_frame error: {e}")

    def _refresh_status(self) -> None:
        """Periodic status label update."""
        stats = self.engine.get_engagement_stats()
        self._lbl_state.setText(f"State: {stats['state']}")
        self._lbl_stats.setText(
            f"Targets: {stats['targets_visible']} | "
            f"Qualified: {stats['targets_qualified']} | "
            f"Engaged: {stats['engagements_total']}"
        )

    def _log(self, msg: str) -> None:
        ts = time.strftime("%H:%M:%S")
        self._log_text.append(f"[{ts}] {msg}")
        # Auto-scroll
        sb = self._log_text.verticalScrollBar()
        sb.setValue(sb.maximum())

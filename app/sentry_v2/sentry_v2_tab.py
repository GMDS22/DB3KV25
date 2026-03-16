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

import os
import time
from typing import List, Optional, Tuple

import cv2
import numpy as np
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QCheckBox, QSlider, QGroupBox, QFrame, QSizePolicy,
    QSpacerItem, QScrollArea, QDoubleSpinBox, QSpinBox,
    QComboBox, QListWidget, QListWidgetItem, QAbstractItemView,
    QTabWidget, QTextEdit, QGridLayout, QLineEdit, QSplitter,
)
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtGui import QImage, QPixmap

from .sentry_v2_config import SentryV2Config, YOLO_COCO_CLASSES
from .sentry_v2_engine import SentryV2Engine, SentryV2State
from .sentry_v2_overlay import SentryV2Overlay
from .sentry_v2_comm import SentryV2Comm
from .sentry_v2_detector import SentryV2Detector
from .simple_tracker import SimpleBBoxTracker
from .sentry_v2_tooltips import SENTRY_V2_TOOLTIPS
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
    "Motion-Locked Filtered Target",  # 10
]

# Color presets available
COLOR_PRESETS: List[str] = [
    "any", "red", "green", "blue", "yellow", "orange", "purple",
    "cyan", "white", "black", "custom",
]

DETECTION_PRESETS = {
    "frame_diff": {
        "label": "Frame Difference",
        "description": "Raw motion-only detection with tighter contour limits.",
        "tooltip_key": "preset_detection_frame_diff",
        "settings": {
            "detection_mode": 0,
            "min_contour_area": 650.0,
            "max_contour_area": 90000.0,
            "yolo_min_area": 180,
            "yolo_confidence": 0.55,
            "color_preset": "any",
            "color_min_area": 160,
            "color_max_area": 180000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 20,
            "motion_ignore_after_move_s": 0.18,
            "motion_gate_threshold": 1.4,
        },
    },
    "backsub": {
        "label": "Background Subtraction",
        "description": "Foreground extractor with broader contour acceptance.",
        "tooltip_key": "preset_detection_backsub",
        "settings": {
            "detection_mode": 1,
            "min_contour_area": 320.0,
            "max_contour_area": 180000.0,
            "yolo_min_area": 180,
            "yolo_confidence": 0.50,
            "color_preset": "any",
            "color_min_area": 160,
            "color_max_area": 200000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 20,
            "motion_ignore_after_move_s": 0.16,
            "motion_gate_threshold": 1.0,
        },
    },
    "yolo": {
        "label": "YOLO Precision",
        "description": "Object-ID driven mode with higher YOLO certainty.",
        "tooltip_key": "preset_detection_yolo",
        "settings": {
            "detection_mode": 2,
            "min_contour_area": 250.0,
            "max_contour_area": 250000.0,
            "yolo_min_area": 260,
            "yolo_confidence": 0.62,
            "color_preset": "any",
            "color_min_area": 120,
            "color_max_area": 250000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 15,
            "motion_ignore_after_move_s": 0.10,
            "motion_gate_threshold": 1.0,
        },
    },
    "dual_motion": {
        "label": "Dual Motion",
        "description": "Frame diff plus background subtraction for stricter motion confirmation.",
        "tooltip_key": "preset_detection_dual_motion",
        "settings": {
            "detection_mode": 3,
            "min_contour_area": 420.0,
            "max_contour_area": 150000.0,
            "yolo_min_area": 180,
            "yolo_confidence": 0.50,
            "color_preset": "any",
            "color_min_area": 160,
            "color_max_area": 200000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 20,
            "motion_ignore_after_move_s": 0.16,
            "motion_gate_threshold": 1.1,
        },
    },
    "motion_yolo": {
        "label": "Motion-Gated YOLO",
        "description": "Motion must happen before YOLO is trusted.",
        "tooltip_key": "preset_detection_motion_yolo",
        "settings": {
            "detection_mode": 4,
            "min_contour_area": 360.0,
            "max_contour_area": 140000.0,
            "yolo_min_area": 220,
            "yolo_confidence": 0.54,
            "color_preset": "any",
            "color_min_area": 140,
            "color_max_area": 220000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 20,
            "motion_ignore_after_move_s": 0.14,
            "motion_gate_threshold": 1.8,
        },
    },
    "best_hybrid": {
        "label": "Best Hybrid YOLO",
        "description": "Balanced backsub plus YOLO combination.",
        "tooltip_key": "preset_detection_best_hybrid",
        "settings": {
            "detection_mode": 5,
            "min_contour_area": 260.0,
            "max_contour_area": 180000.0,
            "yolo_min_area": 180,
            "yolo_confidence": 0.40,
            "color_preset": "any",
            "color_min_area": 140,
            "color_max_area": 220000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 15,
            "motion_ignore_after_move_s": 0.12,
            "motion_gate_threshold": 0.8,
        },
    },
    "color": {
        "label": "Color Watch",
        "description": "Pure red-color tracking for obvious color-only testing.",
        "tooltip_key": "preset_detection_color",
        "settings": {
            "detection_mode": 6,
            "min_contour_area": 250.0,
            "max_contour_area": 250000.0,
            "yolo_min_area": 180,
            "yolo_confidence": 0.45,
            "color_preset": "red",
            "color_min_area": 180,
            "color_max_area": 160000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 25,
            "motion_ignore_after_move_s": 0.08,
            "motion_gate_threshold": 1.0,
        },
    },
    "color_motion": {
        "label": "Color + Motion",
        "description": "Red color must also be moving in frame-diff space.",
        "tooltip_key": "preset_detection_color_motion",
        "settings": {
            "detection_mode": 7,
            "min_contour_area": 520.0,
            "max_contour_area": 120000.0,
            "yolo_min_area": 180,
            "yolo_confidence": 0.45,
            "color_preset": "red",
            "color_min_area": 160,
            "color_max_area": 140000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 35,
            "motion_ignore_after_move_s": 0.16,
            "motion_gate_threshold": 1.0,
        },
    },
    "color_backsub": {
        "label": "Color + Background",
        "description": "Red color must also look like foreground.",
        "tooltip_key": "preset_detection_color_backsub",
        "settings": {
            "detection_mode": 8,
            "min_contour_area": 320.0,
            "max_contour_area": 150000.0,
            "yolo_min_area": 180,
            "yolo_confidence": 0.45,
            "color_preset": "red",
            "color_min_area": 160,
            "color_max_area": 160000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 28,
            "motion_ignore_after_move_s": 0.14,
            "motion_gate_threshold": 1.0,
        },
    },
    "color_yolo": {
        "label": "Color + YOLO",
        "description": "Red color must also satisfy YOLO object detection.",
        "tooltip_key": "preset_detection_color_yolo",
        "settings": {
            "detection_mode": 9,
            "min_contour_area": 250.0,
            "max_contour_area": 180000.0,
            "yolo_min_area": 180,
            "yolo_confidence": 0.50,
            "color_preset": "red",
            "color_min_area": 140,
            "color_max_area": 180000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 42,
            "motion_ignore_after_move_s": 0.12,
            "motion_gate_threshold": 1.0,
        },
    },
    "motion_locked": {
        "label": "Motion-Locked Filtered",
        "description": "Sentry-focused single moving target with optional color and YOLO refinement.",
        "tooltip_key": "preset_detection_motion_locked",
        "settings": {
            "detection_mode": 10,
            "min_contour_area": 250.0,
            "max_contour_area": 250000.0,
            "yolo_min_area": 180,
            "yolo_confidence": 0.38,
            "color_preset": "any",
            "color_min_area": 120,
            "color_max_area": 250000,
            "color_fusion_strategy": "AND",
            "color_fusion_overlap": 15,
            "motion_ignore_after_move_s": 0.12,
            "motion_gate_threshold": 1.0,
        },
    },
}

TARGET_FILTER_PRESETS = {
    "wide_net": {
        "label": "Wide Net",
        "description": "Allows nearly anything through so target volume stays high.",
        "tooltip_key": "preset_filter_wide_net",
        "settings": {
            "allowed_classes": [],
            "min_confidence": 0.30,
            "min_size_ratio": 0.0008,
            "max_size_ratio": 0.0,
        },
    },
    "human_focus": {
        "label": "Human Focus",
        "description": "Filters hard toward person detections only.",
        "tooltip_key": "preset_filter_human_focus",
        "settings": {
            "allowed_classes": ["person"],
            "min_confidence": 0.48,
            "min_size_ratio": 0.0012,
            "max_size_ratio": 0.45,
        },
    },
    "vehicle_watch": {
        "label": "Vehicle Watch",
        "description": "Keeps vehicles and rejects smaller object classes.",
        "tooltip_key": "preset_filter_vehicle_watch",
        "settings": {
            "allowed_classes": ["car", "truck", "bus", "motorcycle", "bicycle"],
            "min_confidence": 0.42,
            "min_size_ratio": 0.0035,
            "max_size_ratio": 0.0,
        },
    },
    "small_movers": {
        "label": "Small Movers",
        "description": "Keeps smaller or farther targets in play.",
        "tooltip_key": "preset_filter_small_movers",
        "settings": {
            "allowed_classes": ["person", "dog", "cat", "bird", "sports ball"],
            "min_confidence": 0.32,
            "min_size_ratio": 0.0005,
            "max_size_ratio": 0.10,
        },
    },
    "large_close": {
        "label": "Large Close",
        "description": "Only obvious, large, near detections survive.",
        "tooltip_key": "preset_filter_large_close",
        "settings": {
            "allowed_classes": [],
            "min_confidence": 0.60,
            "min_size_ratio": 0.0120,
            "max_size_ratio": 0.35,
        },
    },
}

BUS_SERVO_TIME_PRESETS = {
    "smooth": {
        "label": "Smooth",
        "description": "Slower, smoother turret movement for careful tracking.",
        "tooltip_key": "preset_servo_smooth",
        "move_time_ms": 90,
    },
    "balanced": {
        "label": "Balanced",
        "description": "Moderate movement timing for general sentry use.",
        "tooltip_key": "preset_servo_balanced",
        "move_time_ms": 55,
    },
    "fast": {
        "label": "Fast",
        "description": "Snappier movement timing for aggressive response.",
        "tooltip_key": "preset_servo_fast",
        "move_time_ms": 35,
    },
}

MASTER_PROFILE_PRESETS = {
    "demo_observer": {
        "label": "Demo Observer",
        "description": "Calm, visibly slow whole-stack behavior for observation and tuning.",
        "tooltip_key": "preset_master_demo_observer",
        "detection": "motion_locked",
        "filter": "wide_net",
        "threat": "crosshair_snap",
        "engagement": "demo_track",
        "servo": "smooth",
    },
    "indoor_precision": {
        "label": "Indoor Precision",
        "description": "Conservative full-stack profile for close indoor testing.",
        "tooltip_key": "preset_master_indoor_precision",
        "detection": "yolo",
        "filter": "human_focus",
        "threat": "class_first",
        "engagement": "indoor_precision",
        "servo": "smooth",
    },
    "balanced_sentry": {
        "label": "Balanced Sentry",
        "description": "General-purpose coordinated sentry behavior.",
        "tooltip_key": "preset_master_balanced_sentry",
        "detection": "motion_locked",
        "filter": "wide_net",
        "threat": "balanced_guard",
        "engagement": "balanced_response",
        "servo": "balanced",
    },
    "vehicle_intercept": {
        "label": "Vehicle Intercept",
        "description": "Faster coordinated profile for larger moving machines.",
        "tooltip_key": "preset_master_vehicle_intercept",
        "detection": "motion_yolo",
        "filter": "vehicle_watch",
        "threat": "speed_hunter",
        "engagement": "outdoor_chase",
        "servo": "balanced",
    },
    "aggressive_pursuit": {
        "label": "Aggressive Pursuit",
        "description": "Most forceful coordinated stack with fast tracking and aggressive firing.",
        "tooltip_key": "preset_master_aggressive_pursuit",
        "detection": "best_hybrid",
        "filter": "wide_net",
        "threat": "speed_hunter",
        "engagement": "saturation_burst",
        "servo": "fast",
    },
}

THREAT_AI_PRESETS = {
    "balanced_guard": {
        "label": "Balanced Guard",
        "description": "General-purpose prioritization with strong center and class awareness.",
        "tooltip_key": "preset_threat_balanced_guard",
        "weights": {
            "w_proximity": 0.26,
            "w_size": 0.12,
            "w_confidence": 0.10,
            "w_class_priority": 0.24,
            "w_speed": 0.08,
            "w_persistence": 0.10,
            "w_approach": 0.10,
        },
        "use_ml_model": False,
    },
    "crosshair_snap": {
        "label": "Crosshair Snap",
        "description": "Almost entirely center-biased so on-axis targets beat everything else.",
        "tooltip_key": "preset_threat_crosshair_snap",
        "weights": {
            "w_proximity": 0.58,
            "w_size": 0.04,
            "w_confidence": 0.06,
            "w_class_priority": 0.10,
            "w_speed": 0.03,
            "w_persistence": 0.03,
            "w_approach": 0.16,
        },
        "use_ml_model": False,
    },
    "speed_hunter": {
        "label": "Speed Hunter",
        "description": "Hunts the fastest movers even when they are off-center.",
        "tooltip_key": "preset_threat_speed_hunter",
        "weights": {
            "w_proximity": 0.08,
            "w_size": 0.06,
            "w_confidence": 0.06,
            "w_class_priority": 0.10,
            "w_speed": 0.42,
            "w_persistence": 0.20,
            "w_approach": 0.08,
        },
        "use_ml_model": False,
    },
    "big_target_bias": {
        "label": "Big Target Bias",
        "description": "Rewards large, close, visually dominant detections.",
        "tooltip_key": "preset_threat_big_target_bias",
        "weights": {
            "w_proximity": 0.14,
            "w_size": 0.48,
            "w_confidence": 0.16,
            "w_class_priority": 0.10,
            "w_speed": 0.04,
            "w_persistence": 0.04,
            "w_approach": 0.04,
        },
        "use_ml_model": False,
    },
    "class_first": {
        "label": "Class First",
        "description": "Configured target classes dominate ranking over raw motion.",
        "tooltip_key": "preset_threat_class_first",
        "weights": {
            "w_proximity": 0.10,
            "w_size": 0.06,
            "w_confidence": 0.18,
            "w_class_priority": 0.50,
            "w_speed": 0.04,
            "w_persistence": 0.06,
            "w_approach": 0.06,
        },
        "use_ml_model": False,
    },
}

ENGAGEMENT_PRESETS = {
    "demo_track": {
        "label": "Demo Track Only",
        "description": "No auto-fire, slow visible corrections, and long settle windows.",
        "tooltip_key": "preset_engage_demo_track",
        "settings": {
            "auto_trigger_enabled": False,
            "trigger_mode_bb": False,
            "min_threat_score": 0.55,
            "burst_count": 1,
            "burst_interval_ms": 90,
            "inter_target_cooldown": 1.6,
            "cycle_cooldown": 3.0,
            "max_queue_length": 1,
            "optimize_slew_order": False,
            "engagement_speed": 32,
            "precision_aim_enabled": True,
            "precision_settle_time": 1.10,
            "precision_max_step": 0.40,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 0.45,
            "aim_lock_tilt_tolerance": 0.40,
            "aim_lock_required_frames": 6,
            "target_loss_timeout": 1.60,
        },
    },
    "indoor_precision": {
        "label": "Indoor Precision",
        "description": "Very cautious and exact for tight spaces and close targets.",
        "tooltip_key": "preset_engage_indoor_precision",
        "settings": {
            "auto_trigger_enabled": True,
            "trigger_mode_bb": True,
            "min_threat_score": 0.50,
            "burst_count": 1,
            "burst_interval_ms": 85,
            "inter_target_cooldown": 1.30,
            "cycle_cooldown": 2.60,
            "max_queue_length": 1,
            "optimize_slew_order": False,
            "engagement_speed": 38,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.95,
            "precision_max_step": 0.45,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 0.55,
            "aim_lock_tilt_tolerance": 0.50,
            "aim_lock_required_frames": 5,
            "target_loss_timeout": 1.35,
        },
    },
    "balanced_response": {
        "label": "Balanced Response",
        "description": "Default all-round behavior with controlled auto-engage timing.",
        "tooltip_key": "preset_engage_balanced_response",
        "settings": {
            "auto_trigger_enabled": True,
            "trigger_mode_bb": True,
            "min_threat_score": 0.30,
            "burst_count": 2,
            "burst_interval_ms": 60,
            "inter_target_cooldown": 0.7,
            "cycle_cooldown": 1.8,
            "max_queue_length": 1,
            "optimize_slew_order": False,
            "engagement_speed": 58,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.45,
            "precision_max_step": 0.85,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 1.00,
            "aim_lock_tilt_tolerance": 0.90,
            "aim_lock_required_frames": 4,
            "target_loss_timeout": 1.00,
        },
    },
    "outdoor_chase": {
        "label": "Outdoor Chase",
        "description": "Fast and tolerant so motion across a wider scene stays engaged.",
        "tooltip_key": "preset_engage_outdoor_chase",
        "settings": {
            "auto_trigger_enabled": True,
            "trigger_mode_bb": True,
            "min_threat_score": 0.18,
            "burst_count": 2,
            "burst_interval_ms": 45,
            "inter_target_cooldown": 0.35,
            "cycle_cooldown": 1.0,
            "max_queue_length": 1,
            "optimize_slew_order": False,
            "engagement_speed": 82,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.22,
            "precision_max_step": 1.55,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 1.80,
            "aim_lock_tilt_tolerance": 1.60,
            "aim_lock_required_frames": 2,
            "target_loss_timeout": 0.75,
        },
    },
    "saturation_burst": {
        "label": "Saturation Burst",
        "description": "Most aggressive preset with longer bursts and minimal cooldown.",
        "tooltip_key": "preset_engage_saturation_burst",
        "settings": {
            "auto_trigger_enabled": True,
            "trigger_mode_bb": True,
            "min_threat_score": 0.15,
            "burst_count": 5,
            "burst_interval_ms": 30,
            "inter_target_cooldown": 0.20,
            "cycle_cooldown": 0.75,
            "max_queue_length": 1,
            "optimize_slew_order": False,
            "engagement_speed": 72,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.18,
            "precision_max_step": 1.20,
            "fire_requires_lock": False,
            "aim_lock_pan_tolerance": 2.20,
            "aim_lock_tilt_tolerance": 2.00,
            "aim_lock_required_frames": 1,
            "target_loss_timeout": 0.65,
        },
    },
}


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

    # Signals for main app integration (only what main app truly needs)
    sentry_enabled_changed = pyqtSignal(bool)
    detection_mode_changed = pyqtSignal(int)
    color_preset_changed = pyqtSignal(str)

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)

        # Config (try loading saved, else defaults)
        self.config = SentryV2Config.load("app/config/sentry_v2_settings.json")

        # Standalone communication
        self._comm = SentryV2Comm()
        self._comm.invert_pan = self.config.connection.invert_pan
        self._comm.invert_tilt = self.config.connection.invert_tilt
        self._comm.trigger_mode_bb = self.config.engagement.trigger_mode_bb

        # Standalone detector
        self._detector = SentryV2Detector()
        self._tracker = SimpleBBoxTracker()

        # Engine
        self.engine = SentryV2Engine(self.config)
        self.engine.on_fire(self._on_engine_fire)
        self.engine.on_move(self._on_engine_move)
        self.engine.on_state_change(self._on_engine_state_change)

        # Overlay
        self.overlay = SentryV2Overlay(self.config)

        # Host app integration
        self._main_window_ref: Optional[QWidget] = None

        # Track accessory states locally for button text
        self._led_on = False
        self._laser_on = False
        self._safety_armed = False

        # Own camera
        self._cap: Optional[cv2.VideoCapture] = None
        self._grab_fail_count: int = 0
        self._MAX_GRAB_FAILS: int = 30  # auto-close after ~1s of failures
        self._cam_timer = QTimer(self)
        self._cam_timer.timeout.connect(self._grab_frame)

        # Non-blocking burst fire state
        self._burst_timer = QTimer(self)
        self._burst_timer.setSingleShot(True)
        self._burst_timer.timeout.connect(self._advance_fire_burst)
        self._burst_remaining: int = 0
        self._burst_interval_ms: int = 50
        self._burst_pan: float = 90.0
        self._burst_tilt: float = 50.0
        self._burst_phase_on: bool = False
        self._last_commanded_pan: float = self.config.guard.guard_pan
        self._last_commanded_tilt: float = self.config.guard.guard_tilt
        self._last_tracking_move_time_ms: int = 0
        self._last_tracking_suppression_s: float = 0.0
        self._last_reacquire_note_seen: str = ""
        self._applying_master_preset: bool = False
        self._applying_servo_preset: bool = False
        self._applying_detection_preset: bool = False
        self._applying_filter_preset: bool = False
        self._applying_threat_preset: bool = False
        self._applying_engagement_preset: bool = False

        # Build UI
        self._build_ui()

        # Status refresh timer
        self._status_timer = QTimer(self)
        self._status_timer.timeout.connect(self._refresh_status)
        self._status_timer.start(500)

    def cleanup(self) -> None:
        """Stop timers and release all resources. Safe to call multiple times."""
        self._cam_timer.stop()
        self._status_timer.stop()
        self._stop_fire_burst(send_release=True)
        self._close_camera()
        self._comm.disconnect()

    def closeEvent(self, event):
        """Release camera and serial on close."""
        self.cleanup()
        super().closeEvent(event)

    # ================================================================== #
    #  UI Construction
    # ================================================================== #

    def _build_ui(self) -> None:
        root = QVBoxLayout(self)
        root.setContentsMargins(4, 4, 4, 4)

        self._main_splitter = QSplitter(Qt.Horizontal)
        self._main_splitter.setChildrenCollapsible(False)

        # --- Left: video feed ---
        self._video_label = QLabel("Waiting for video...")
        self._video_label.setAlignment(Qt.AlignCenter)
        self._video_label.setMinimumSize(480, 360)
        self._video_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self._video_label.setStyleSheet("background: #111; color: #888;")
        self._main_splitter.addWidget(self._video_label)

        # --- Right: controls in scrollable panel ---
        self._settings_scroll = QScrollArea()
        self._settings_scroll.setWidgetResizable(True)
        self._settings_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._settings_scroll.setMinimumWidth(300)

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

        settings_tabs.addTab(self._build_master_profiles_tab(), "Master Profiles")
        settings_tabs.addTab(self._build_connection_tab(), "Connection")
        settings_tabs.addTab(self._build_detection_tab(), "Detection")
        settings_tabs.addTab(self._build_filter_tab(), "Target Filter")
        settings_tabs.addTab(self._build_scoring_tab(), "Threat AI")
        settings_tabs.addTab(self._build_engagement_tab(), "Engage")
        settings_tabs.addTab(self._build_guard_tab(), "Guard")
        settings_tabs.addTab(self._build_controls_tab(), "Controls")

        panel_layout.addWidget(settings_tabs, stretch=1)

        # Status / log
        panel_layout.addWidget(self._build_status_group())
        panel_layout.addWidget(self._build_panel_width_group())

        self._settings_scroll.setWidget(panel)
        self._main_splitter.addWidget(self._settings_scroll)
        self._main_splitter.setStretchFactor(0, 3)
        self._main_splitter.setStretchFactor(1, 0)
        root.addWidget(self._main_splitter)

        QTimer.singleShot(0, self._apply_saved_panel_width)

        self._apply_all_tooltips()

    def _build_panel_width_group(self) -> QGroupBox:
        grp = QGroupBox("Panel Layout")
        lay = QHBoxLayout(grp)
        lay.addWidget(QLabel("Panel Width:"))

        self._slider_panel_width = QSlider(Qt.Horizontal)
        self._slider_panel_width.setRange(320, 820)
        self._slider_panel_width.setValue(int(self.config.settings_panel_width))
        self._slider_panel_width.valueChanged.connect(self._on_panel_width_changed)
        self._slider_panel_width.setToolTip(
            "Adjust the Smart Sentry settings panel width. Drag right for easier access to dense controls."
        )
        lay.addWidget(self._slider_panel_width)

        self._lbl_panel_width = QLabel(f"{int(self.config.settings_panel_width)} px")
        self._lbl_panel_width.setMinimumWidth(56)
        lay.addWidget(self._lbl_panel_width)
        return grp

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
            self._spin_cam_w: "camera_width",
            self._spin_cam_h: "camera_height",
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
        intro.setStyleSheet("color: #aaa; font-size: 11px;")
        lay.addWidget(intro)

        preset_grp = QGroupBox("Coordinated Profiles")
        preset_lay = QVBoxLayout(preset_grp)
        preset_lay.setSpacing(4)

        preset_btn_grid = QGridLayout()
        for index, (preset_name, preset) in enumerate(MASTER_PROFILE_PRESETS.items()):
            btn = QPushButton(preset["label"])
            self._apply_tooltip(btn, preset.get("tooltip_key", ""))
            btn.clicked.connect(lambda _checked=False, name=preset_name: self._apply_master_profile(name))
            preset_btn_grid.addWidget(btn, index // 2, index % 2)
        preset_lay.addLayout(preset_btn_grid)

        self._lbl_master_profile = QLabel("")
        self._lbl_master_profile.setWordWrap(True)
        self._lbl_master_profile.setStyleSheet("color: #999; font-size: 10px;")
        preset_lay.addWidget(self._lbl_master_profile)
        lay.addWidget(preset_grp)

        summary_grp = QGroupBox("Current Stack")
        summary_lay = QVBoxLayout(summary_grp)
        summary_lay.setSpacing(3)
        self._lbl_master_stack = QLabel("")
        self._lbl_master_stack.setWordWrap(True)
        self._lbl_master_stack.setStyleSheet("font-size: 11px;")
        summary_lay.addWidget(self._lbl_master_stack)
        lay.addWidget(summary_grp)

        lay.addStretch()
        self._update_master_stack_summary()
        self._set_master_profile_label(self._match_master_profile_name())
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
        self._edit_cam_source.setPlaceholderText("Blank = main app feed, or enter secondary camera index/URL")
        self._apply_tooltip(self._edit_cam_source, "camera_source")
        cam_lay.addWidget(self._edit_cam_source, 0, 1)

        cam_lay.addWidget(QLabel("Width:"), 1, 0)
        self._spin_cam_w = QSpinBox()
        self._spin_cam_w.setRange(160, 3840)
        self._spin_cam_w.setSingleStep(160)
        self._spin_cam_w.setValue(self.config.connection.camera_width)
        self._apply_tooltip(self._spin_cam_w, "camera_width")
        cam_lay.addWidget(self._spin_cam_w, 1, 1)

        cam_lay.addWidget(QLabel("Height:"), 2, 0)
        self._spin_cam_h = QSpinBox()
        self._spin_cam_h.setRange(120, 2160)
        self._spin_cam_h.setSingleStep(120)
        self._spin_cam_h.setValue(self.config.connection.camera_height)
        self._apply_tooltip(self._spin_cam_h, "camera_height")
        cam_lay.addWidget(self._spin_cam_h, 2, 1)

        self._btn_cam = QPushButton("Open Camera")
        self._btn_cam.setStyleSheet("font-weight: bold; padding: 4px;")
        self._btn_cam.clicked.connect(self._toggle_camera)
        self._apply_tooltip(self._btn_cam, "camera_toggle")
        cam_lay.addWidget(self._btn_cam, 3, 0, 1, 2)

        self._lbl_cam_status = QLabel("Camera closed")
        self._lbl_cam_status.setStyleSheet("color: #888; font-size: 10px;")
        cam_lay.addWidget(self._lbl_cam_status, 4, 0, 1, 2)

        lay.addWidget(cam_grp)

        # Connection mode selector
        type_grp = QGroupBox("Connection Mode")
        type_lay = QVBoxLayout(type_grp)
        self._combo_conn_type = QComboBox()
        self._combo_conn_type.addItems(SentryV2Comm.MODE_LABELS)
        self._combo_conn_type.setCurrentIndex(self.config.connection.connection_type)
        self._combo_conn_type.currentIndexChanged.connect(self._on_conn_type_changed)
        self._apply_tooltip(self._combo_conn_type, "connection_mode")
        type_lay.addWidget(self._combo_conn_type)
        self._lbl_mode_hint = QLabel("")
        self._lbl_mode_hint.setWordWrap(True)
        self._lbl_mode_hint.setStyleSheet("color: #aaa; font-size: 10px;")
        type_lay.addWidget(self._lbl_mode_hint)
        lay.addWidget(type_grp)

        # --- ESP32 Serial settings (modes 0, 1) ---
        self._grp_esp32_serial = QGroupBox("ESP32 Serial (USB)")
        esp_lay = QGridLayout(self._grp_esp32_serial)

        esp_lay.addWidget(QLabel("COM Port:"), 0, 0)
        self._edit_esp32_port = QLineEdit(self.config.connection.esp32_port)
        self._apply_tooltip(self._edit_esp32_port, "esp32_port")
        esp_lay.addWidget(self._edit_esp32_port, 0, 1)
        btn_scan_esp = QPushButton("Scan")
        btn_scan_esp.setFixedWidth(50)
        btn_scan_esp.clicked.connect(lambda: self._scan_ports("esp32"))
        self._apply_tooltip(btn_scan_esp, "scan_esp32_ports")
        esp_lay.addWidget(btn_scan_esp, 0, 2)

        self._combo_esp32_ports = QComboBox()
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
        btn_scan_dbg.setFixedWidth(50)
        btn_scan_dbg.clicked.connect(lambda: self._scan_ports("debug"))
        self._apply_tooltip(btn_scan_dbg, "scan_debug_ports")
        dbg_lay.addWidget(btn_scan_dbg, 0, 2)

        self._combo_debug_ports = QComboBox()
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

        move_preset_row = QHBoxLayout()
        move_preset_row.addWidget(QLabel("Move Time Presets:"))
        for preset_name, preset in BUS_SERVO_TIME_PRESETS.items():
            btn = QPushButton(preset["label"])
            btn.setMaximumWidth(84)
            self._apply_tooltip(btn, preset.get("tooltip_key", ""))
            btn.clicked.connect(lambda _checked=False, name=preset_name: self._apply_servo_time_preset(name))
            move_preset_row.addWidget(btn)
        srv_lay.addLayout(move_preset_row, 3, 0, 1, 2)

        self._lbl_servo_time_preset = QLabel("")
        self._lbl_servo_time_preset.setWordWrap(True)
        self._lbl_servo_time_preset.setStyleSheet("color: #888; font-size: 10px;")
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

        lay.addWidget(self._grp_udp)

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

        # Connect / disconnect
        btn_row = QHBoxLayout()
        self._btn_connect = QPushButton("Connect")
        self._btn_connect.setStyleSheet(
            "QPushButton { font-weight: bold; padding: 6px; }"
        )
        self._btn_connect.clicked.connect(self._toggle_connection)
        self._apply_tooltip(self._btn_connect, "connect_toggle")
        btn_row.addWidget(self._btn_connect)
        lay.addLayout(btn_row)

        # Status
        self._lbl_conn_status = QLabel("Disconnected")
        self._lbl_conn_status.setStyleSheet("color: #cc3333; font-weight: bold;")
        lay.addWidget(self._lbl_conn_status)

        self._lbl_last_cmd = QLabel("")
        self._lbl_last_cmd.setStyleSheet("color: #888; font-size: 10px;")
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

        preset_grp = QGroupBox("Detection Presets")
        preset_lay = QVBoxLayout(preset_grp)
        preset_lay.setSpacing(4)

        preset_btn_grid = QGridLayout()
        for index, (preset_name, preset) in enumerate(DETECTION_PRESETS.items()):
            btn = QPushButton(preset["label"])
            self._apply_tooltip(btn, preset.get("tooltip_key", ""))
            btn.clicked.connect(lambda _checked=False, name=preset_name: self._apply_detection_preset(name))
            preset_btn_grid.addWidget(btn, index // 2, index % 2)
        preset_lay.addLayout(preset_btn_grid)

        self._lbl_detection_preset = QLabel("")
        self._lbl_detection_preset.setWordWrap(True)
        self._lbl_detection_preset.setStyleSheet("color: #999; font-size: 10px;")
        preset_lay.addWidget(self._lbl_detection_preset)
        lay.addWidget(preset_grp)

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

        lay.addWidget(self._grp_contour)

        # --- YOLO settings (modes 2,4,5,9,10) ---
        self._grp_yolo = QGroupBox("YOLO Settings")
        yolo_lay = QGridLayout(self._grp_yolo)

        yolo_lay.addWidget(QLabel("Model:"), 0, 0)
        self._combo_yolo_model = QComboBox()
        self._combo_yolo_model.setPlaceholderText("Select model...")
        self._scan_yolo_models()
        self._apply_tooltip(self._combo_yolo_model, "yolo_model")
        yolo_lay.addWidget(self._combo_yolo_model, 0, 1)
        btn_load_yolo = QPushButton("Load")
        btn_load_yolo.setFixedWidth(50)
        btn_load_yolo.clicked.connect(self._load_yolo_model)
        self._apply_tooltip(btn_load_yolo, "load_yolo_model")
        yolo_lay.addWidget(btn_load_yolo, 0, 2)

        yolo_lay.addWidget(QLabel("Classes:"), 1, 0)
        self._edit_yolo_classes = QLineEdit(", ".join(self.config.target_filter.allowed_classes))
        self._edit_yolo_classes.setPlaceholderText("person, car, dog ...")
        self._edit_yolo_classes.editingFinished.connect(self._on_yolo_classes_changed)
        self._apply_tooltip(self._edit_yolo_classes, "yolo_classes")
        yolo_lay.addWidget(self._edit_yolo_classes, 1, 1, 1, 2)

        yolo_lay.addWidget(QLabel("Confidence:"), 2, 0)
        self._spin_yolo_conf = QDoubleSpinBox()
        self._spin_yolo_conf.setRange(0.05, 1.0)
        self._spin_yolo_conf.setSingleStep(0.05)
        self._spin_yolo_conf.setDecimals(2)
        self._spin_yolo_conf.setValue(self.config.detection_mode.yolo_confidence)
        self._spin_yolo_conf.valueChanged.connect(self._on_detection_settings_changed)
        self._apply_tooltip(self._spin_yolo_conf, "yolo_confidence")
        yolo_lay.addWidget(self._spin_yolo_conf, 2, 1, 1, 2)

        yolo_lay.addWidget(QLabel("Min Area (px):"), 3, 0)
        self._spin_yolo_min_area = QSpinBox()
        self._spin_yolo_min_area.setRange(0, 10000000)
        self._spin_yolo_min_area.setSingleStep(100)
        self._spin_yolo_min_area.setValue(self.config.detection_mode.yolo_min_area)
        self._spin_yolo_min_area.valueChanged.connect(self._on_detection_settings_changed)
        self._apply_tooltip(self._spin_yolo_min_area, "yolo_min_area")
        yolo_lay.addWidget(self._spin_yolo_min_area, 3, 1, 1, 2)

        self._lbl_yolo_status = QLabel("No model loaded")
        self._lbl_yolo_status.setStyleSheet("color: #888; font-size: 10px;")
        yolo_lay.addWidget(self._lbl_yolo_status, 4, 0, 1, 3)

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

        lay.addWidget(self._grp_motion)

        lay.addStretch()

        # Initial visibility
        self._update_detection_panel_visibility()
        self._set_detection_preset_label(self._match_detection_preset_name())
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
        for index, (preset_name, preset) in enumerate(TARGET_FILTER_PRESETS.items()):
            btn = QPushButton(preset["label"])
            self._apply_tooltip(btn, preset.get("tooltip_key", ""))
            btn.clicked.connect(lambda _checked=False, name=preset_name: self._apply_filter_preset(name))
            preset_btn_grid.addWidget(btn, index // 2, index % 2)
        preset_lay.addLayout(preset_btn_grid)

        self._lbl_filter_preset = QLabel("")
        self._lbl_filter_preset.setWordWrap(True)
        self._lbl_filter_preset.setStyleSheet("color: #999; font-size: 10px;")
        preset_lay.addWidget(self._lbl_filter_preset)
        lay.addWidget(preset_grp)

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
        self._apply_tooltip(self._class_list, "allowed_classes")
        g_lay.addWidget(self._class_list)

        btn_row = QHBoxLayout()
        btn_all = QPushButton("All")
        btn_all.clicked.connect(self._select_all_classes)
        btn_none = QPushButton("None")
        btn_none.clicked.connect(self._select_no_classes)
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
        for index, (preset_name, preset) in enumerate(THREAT_AI_PRESETS.items()):
            btn = QPushButton(preset["label"])
            self._apply_tooltip(btn, preset.get("tooltip_key", ""))
            btn.clicked.connect(lambda _checked=False, name=preset_name: self._apply_threat_preset(name))
            preset_btn_grid.addWidget(btn, index // 2, index % 2)
        preset_lay.addLayout(preset_btn_grid)

        self._lbl_threat_preset = QLabel("")
        self._lbl_threat_preset.setWordWrap(True)
        self._lbl_threat_preset.setStyleSheet("color: #999; font-size: 10px;")
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

        self._set_threat_preset_label(self._match_threat_preset_name())

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

        preset_grp = QGroupBox("Engagement Behavior Presets")
        preset_lay = QVBoxLayout(preset_grp)
        preset_lay.setSpacing(4)

        preset_btn_grid = QGridLayout()
        for index, (preset_name, preset) in enumerate(ENGAGEMENT_PRESETS.items()):
            btn = QPushButton(preset["label"])
            self._apply_tooltip(btn, preset.get("tooltip_key", ""))
            btn.clicked.connect(lambda _checked=False, name=preset_name: self._apply_engagement_preset(name))
            preset_btn_grid.addWidget(btn, index // 2, index % 2)
        preset_lay.addLayout(preset_btn_grid)

        self._lbl_engagement_preset = QLabel("")
        self._lbl_engagement_preset.setWordWrap(True)
        self._lbl_engagement_preset.setStyleSheet("color: #999; font-size: 10px;")
        preset_lay.addWidget(self._lbl_engagement_preset)
        lay.addWidget(preset_grp)

        # Auto-Trigger toggle (prominent)
        self._chk_auto_trigger = QCheckBox("Auto-Trigger (fire automatically)")
        self._chk_auto_trigger.setStyleSheet(
            "font-weight: bold; color: #ff4d4d;"
            if self.config.engagement.auto_trigger_enabled
            else "font-weight: bold; color: #66dd88;"
        )
        self._chk_auto_trigger.setChecked(self.config.engagement.auto_trigger_enabled)
        self._chk_auto_trigger.toggled.connect(self._on_auto_trigger_toggled)
        self._apply_tooltip(self._chk_auto_trigger, "auto_trigger")
        lay.addWidget(self._chk_auto_trigger)

        # Trigger mode
        trig_row = QHBoxLayout()
        trig_row.addWidget(QLabel("Trigger Mode:"))
        self._combo_trigger_mode = QComboBox()
        self._combo_trigger_mode.addItems(["Water (MOSFET)", "Projectile (BB Servo)"])
        self._combo_trigger_mode.setCurrentIndex(1 if self.config.engagement.trigger_mode_bb else 0)
        self._combo_trigger_mode.currentIndexChanged.connect(self._on_trigger_mode_changed)
        self._apply_tooltip(self._combo_trigger_mode, "trigger_mode")
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
        row4.addWidget(QLabel("Inter-target cooldown (s):"))
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
        row6.addWidget(QLabel("Max targets per cycle:"))
        self._spin_max_queue = QSpinBox()
        self._spin_max_queue.setRange(1, 10)
        self._spin_max_queue.setValue(self.config.engagement.max_queue_length)
        self._spin_max_queue.valueChanged.connect(self._on_engagement_changed)
        self._apply_tooltip(self._spin_max_queue, "max_targets_per_cycle")
        row6.addWidget(self._spin_max_queue)
        lay.addLayout(row6)

        # Optimize slew
        self._chk_optimize = QCheckBox("Optimise servo travel order")
        self._chk_optimize.setChecked(self.config.engagement.optimize_slew_order)
        self._chk_optimize.toggled.connect(self._on_engagement_changed)
        self._apply_tooltip(self._chk_optimize, "optimize_travel")
        lay.addWidget(self._chk_optimize)

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

        self._chk_precision = QCheckBox("Enable precision refinement")
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

        self._set_engagement_preset_label(self._match_engagement_preset_name())

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
        self._spin_guard_pan.setRange(5.0, 185.0)
        self._spin_guard_pan.setSingleStep(1.0)
        self._spin_guard_pan.setValue(self.config.guard.guard_pan)
        self._spin_guard_pan.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_guard_pan, "guard_pan")
        row.addWidget(self._spin_guard_pan)
        static_lay.addLayout(row)

        row2 = QHBoxLayout()
        row2.addWidget(QLabel("Guard Tilt (deg):"))
        self._spin_guard_tilt = QDoubleSpinBox()
        self._spin_guard_tilt.setRange(10.0, 130.0)
        self._spin_guard_tilt.setSingleStep(1.0)
        self._spin_guard_tilt.setValue(self.config.guard.guard_tilt)
        self._spin_guard_tilt.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_guard_tilt, "guard_tilt")
        row2.addWidget(self._spin_guard_tilt)
        static_lay.addLayout(row2)

        limit_row_1 = QHBoxLayout()
        limit_row_1.addWidget(QLabel("Pan Min / Max:"))
        self._spin_pan_min = QDoubleSpinBox()
        self._spin_pan_min.setRange(0.0, 220.0)
        self._spin_pan_min.setValue(self.config.guard.pan_min)
        self._spin_pan_min.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_pan_min, "pan_limit_min")
        limit_row_1.addWidget(self._spin_pan_min)
        self._spin_pan_max = QDoubleSpinBox()
        self._spin_pan_max.setRange(0.0, 220.0)
        self._spin_pan_max.setValue(self.config.guard.pan_max)
        self._spin_pan_max.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_pan_max, "pan_limit_max")
        limit_row_1.addWidget(self._spin_pan_max)
        static_lay.addLayout(limit_row_1)

        limit_row_2 = QHBoxLayout()
        limit_row_2.addWidget(QLabel("Tilt Min / Max:"))
        self._spin_tilt_min = QDoubleSpinBox()
        self._spin_tilt_min.setRange(0.0, 130.0)
        self._spin_tilt_min.setValue(self.config.guard.tilt_min)
        self._spin_tilt_min.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_tilt_min, "tilt_limit_min")
        limit_row_2.addWidget(self._spin_tilt_min)
        self._spin_tilt_max = QDoubleSpinBox()
        self._spin_tilt_max.setRange(0.0, 130.0)
        self._spin_tilt_max.setValue(self.config.guard.tilt_max)
        self._spin_tilt_max.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_tilt_max, "tilt_limit_max")
        limit_row_2.addWidget(self._spin_tilt_max)
        static_lay.addLayout(limit_row_2)

        btn_row = QHBoxLayout()
        btn = QPushButton("Go To Guard Position")
        btn.clicked.connect(self._go_to_guard)
        self._apply_tooltip(btn, "go_guard")
        btn_row.addWidget(btn)
        btn2 = QPushButton("Set Current As Guard")
        self._apply_tooltip(btn2, "set_current_guard")
        btn2.clicked.connect(self._set_current_as_guard)
        btn_row.addWidget(btn2)
        static_lay.addLayout(btn_row)
        lay.addWidget(static_grp)

        # --- Sweep settings (mode 1) ---
        self._grp_sweep = QGroupBox("Sweep Settings")
        sweep_lay = QVBoxLayout(self._grp_sweep)
        sweep_lay.setSpacing(3)

        sr1 = QHBoxLayout()
        sr1.addWidget(QLabel("Pan Min (deg):"))
        self._spin_sweep_min = QDoubleSpinBox()
        self._spin_sweep_min.setRange(5.0, 185.0)
        self._spin_sweep_min.setValue(self.config.guard.sweep_pan_min)
        self._spin_sweep_min.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_sweep_min, "sweep_min")
        sr1.addWidget(self._spin_sweep_min)
        sr1.addWidget(QLabel("Pan Max:"))
        self._spin_sweep_max = QDoubleSpinBox()
        self._spin_sweep_max.setRange(5.0, 185.0)
        self._spin_sweep_max.setValue(self.config.guard.sweep_pan_max)
        self._spin_sweep_max.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_sweep_max, "sweep_max")
        sr1.addWidget(self._spin_sweep_max)
        sweep_lay.addLayout(sr1)

        sr2 = QHBoxLayout()
        sr2.addWidget(QLabel("Tilt (deg):"))
        self._spin_sweep_tilt = QDoubleSpinBox()
        self._spin_sweep_tilt.setRange(10.0, 130.0)
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
        self._spin_rnd_pan_min.setRange(5.0, 185.0)
        self._spin_rnd_pan_min.setValue(self.config.guard.random_pan_min)
        self._spin_rnd_pan_min.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_rnd_pan_min, "random_pan_min")
        rr1.addWidget(self._spin_rnd_pan_min)
        rr1.addWidget(QLabel("Max:"))
        self._spin_rnd_pan_max = QDoubleSpinBox()
        self._spin_rnd_pan_max.setRange(5.0, 185.0)
        self._spin_rnd_pan_max.setValue(self.config.guard.random_pan_max)
        self._spin_rnd_pan_max.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_rnd_pan_max, "random_pan_max")
        rr1.addWidget(self._spin_rnd_pan_max)
        rnd_lay.addLayout(rr1)

        rr2 = QHBoxLayout()
        rr2.addWidget(QLabel("Tilt Min:"))
        self._spin_rnd_tilt_min = QDoubleSpinBox()
        self._spin_rnd_tilt_min.setRange(10.0, 130.0)
        self._spin_rnd_tilt_min.setValue(self.config.guard.random_tilt_min)
        self._spin_rnd_tilt_min.valueChanged.connect(self._on_guard_changed)
        self._apply_tooltip(self._spin_rnd_tilt_min, "random_tilt_min")
        rr2.addWidget(self._spin_rnd_tilt_min)
        rr2.addWidget(QLabel("Max:"))
        self._spin_rnd_tilt_max = QDoubleSpinBox()
        self._spin_rnd_tilt_max.setRange(10.0, 130.0)
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

        lay.addStretch()

        # Set initial visibility of mode-specific groups
        self._update_guard_mode_visibility(self.config.guard.guard_mode)

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
        self._apply_tooltip(self._spin_step, "manual_step")
        spd_row.addWidget(self._spin_step)
        dpad_lay.addLayout(spd_row)

        # D-pad grid
        grid = QGridLayout()
        btn_up = QPushButton("\u25B2")  # up arrow
        btn_up.setFixedSize(50, 40)
        btn_up.clicked.connect(lambda: self._manual_move(0, -1))
        self._apply_tooltip(btn_up, "manual_up")
        grid.addWidget(btn_up, 0, 1)

        btn_left = QPushButton("\u25C0")  # left arrow
        btn_left.setFixedSize(50, 40)
        btn_left.clicked.connect(lambda: self._manual_move(-1, 0))
        self._apply_tooltip(btn_left, "manual_left")
        grid.addWidget(btn_left, 1, 0)

        btn_home = QPushButton("H")
        btn_home.setFixedSize(50, 40)
        self._apply_tooltip(btn_home, "manual_home")
        btn_home.clicked.connect(self._on_home_clicked)
        grid.addWidget(btn_home, 1, 1)

        btn_right = QPushButton("\u25B6")  # right arrow
        btn_right.setFixedSize(50, 40)
        btn_right.clicked.connect(lambda: self._manual_move(1, 0))
        self._apply_tooltip(btn_right, "manual_right")
        grid.addWidget(btn_right, 1, 2)

        btn_down = QPushButton("\u25BC")  # down arrow
        btn_down.setFixedSize(50, 40)
        btn_down.clicked.connect(lambda: self._manual_move(0, 1))
        self._apply_tooltip(btn_down, "manual_down")
        grid.addWidget(btn_down, 2, 1)

        dpad_lay.addLayout(grid)
        lay.addWidget(dpad_grp)

        # --- Accessories ---
        acc_grp = QGroupBox("Accessories")
        acc_lay = QGridLayout(acc_grp)

        self._btn_led = QPushButton("LED: OFF")
        self._btn_led.setCheckable(True)
        self._btn_led.toggled.connect(self._on_led_toggled)
        self._apply_tooltip(self._btn_led, "led_toggle")
        acc_lay.addWidget(self._btn_led, 0, 0)

        self._btn_laser = QPushButton("Laser: OFF")
        self._btn_laser.setCheckable(True)
        self._btn_laser.toggled.connect(self._on_laser_toggled)
        self._apply_tooltip(self._btn_laser, "laser_toggle")
        acc_lay.addWidget(self._btn_laser, 0, 1)

        self._btn_safety = QPushButton("Safety: LOCKED")
        self._btn_safety.setCheckable(True)
        self._btn_safety.setStyleSheet("QPushButton:checked { background: #cc3333; color: white; }")
        self._btn_safety.toggled.connect(self._on_safety_toggled)
        self._apply_tooltip(self._btn_safety, "safety_toggle")
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
        self._apply_tooltip(self._btn_fire, "manual_fire")
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
        self._apply_tooltip(btn_save, "save_settings")
        lay.addWidget(btn_save)

        return grp

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
        # Own camera takes priority — skip external pushes
        if self._cap is not None and not _from_own_camera:
            return
        now = time.time()
        h, w_frame = frame.shape[:2]

        raw_detections = detections or []
        if use_internal_detector and not _from_own_camera:
            mode = self.config.detection_mode.detection_mode
            raw_detections = self._detector.detect(frame, mode)

        # Update frame dimensions in config
        self.config.guard.frame_width = w_frame
        self.config.guard.frame_height = h

        # Convert raw detections to DetectedObject list
        det_objects = self._convert_detections(raw_detections, w_frame, h, now)

        # Run engine
        self.engine.update(det_objects, now)

        # Copy frame so overlay drawing doesn't corrupt main app's buffer
        display = frame.copy()

        # Draw overlay
        display = self.overlay.draw(display, self.engine)

        # Update video label
        self._show_frame(display)

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
            self.engine.start()
            self._log("Smart Sentry ENABLED")
        else:
            self._stop_fire_burst(send_release=True)
            self.engine.stop()
            self._log("Smart Sentry DISABLED")
        self.sentry_enabled_changed.emit(checked)

    def _on_engine_fire(self, burst_count: int) -> None:
        pan = self.engine.current_pan
        tilt = self.engine.current_tilt
        interval = self.config.engagement.burst_interval_ms
        self.overlay.note_fire_event(burst_count)
        self._start_fire_burst(pan, tilt, burst_count, interval)
        self._log(f"FIRE! Burst: {burst_count}")

    def _on_engine_move(self, pan: float, tilt: float) -> None:
        move_delta = self._get_command_delta(pan, tilt)
        move_time_ms = self._get_tracking_move_time_ms(move_delta)
        self._last_tracking_move_time_ms = int(move_time_ms)
        self._comm.send_command(pan, tilt, move_time_ms=move_time_ms)
        self._remember_commanded_position(pan, tilt)
        suppression_s = self._get_tracking_motion_suppression_s(move_delta)
        self._last_tracking_suppression_s = float(suppression_s)
        if suppression_s > 0.0:
            self._suppress_motion_detection(suppression_s)

    def _on_engine_state_change(self, old: SentryV2State, new: SentryV2State) -> None:
        self._lbl_state.setText(f"State: {new.name}")
        self._log(f"State: {old.name} -> {new.name}")

    # ------------------------------------------------------------------ #
    #  Connection handlers
    # ------------------------------------------------------------------ #

    def _on_conn_type_changed(self, index: int) -> None:
        self.config.connection.connection_type = index
        self._update_conn_panel_visibility()

    _MODE_HINTS = [
        "Single USB cable — full ASCII protocol to ESP32.",
        "Two USB cables — bus servo to Debug Board + IO to ESP32.",
        "One USB cable — bus servo to Debug Board, IO over WiFi to ESP32.",
        "No USB — everything sent wirelessly. Debug board wired to ESP32.",
    ]

    def _update_conn_panel_visibility(self) -> None:
        m = self._combo_conn_type.currentIndex()
        self._lbl_mode_hint.setText(self._MODE_HINTS[m])
        # ESP32 serial panel: modes 0, 1
        self._grp_esp32_serial.setVisible(m in (0, 1))
        # Debug board serial panel: modes 1, 2
        self._grp_debug_serial.setVisible(m in (1, 2))
        # Servo panel: modes 1, 2 (bus servo)
        self._grp_servo.setVisible(m in (1, 2))
        # UDP panel: modes 2, 3
        self._grp_udp.setVisible(m in (2, 3))

    def _scan_ports(self, target: str = "esp32") -> None:
        combo = self._combo_esp32_ports if target == "esp32" else self._combo_debug_ports
        combo.clear()
        ports = SentryV2Comm.list_serial_ports()
        for dev, desc in ports:
            combo.addItem(f"{dev}  —  {desc}", dev)
        if not ports:
            combo.addItem("(no ports found)")
        self._log(f"Scan ({target}): {len(ports)} port(s) found")

    def _on_port_selected(self, target: str = "esp32") -> None:
        if target == "esp32":
            idx = self._combo_esp32_ports.currentIndex()
            dev = self._combo_esp32_ports.itemData(idx)
            if dev:
                self._edit_esp32_port.setText(dev)
        else:
            idx = self._combo_debug_ports.currentIndex()
            dev = self._combo_debug_ports.itemData(idx)
            if dev:
                self._edit_debug_port.setText(dev)

    def _on_invert_changed(self) -> None:
        self.config.connection.invert_pan = self._chk_invert_pan.isChecked()
        self.config.connection.invert_tilt = self._chk_invert_tilt.isChecked()
        self._comm.invert_pan = self.config.connection.invert_pan
        self._comm.invert_tilt = self.config.connection.invert_tilt

    def _toggle_connection(self) -> None:
        if self._comm.is_connected():
            self._comm.disconnect()
            self._btn_connect.setText("Connect")
            self._lbl_conn_status.setText("Disconnected")
            self._lbl_conn_status.setStyleSheet("color: #cc3333; font-weight: bold;")
            self._log("Disconnected")
            return

        # Read settings from UI into config
        m = self._combo_conn_type.currentIndex()
        cc = self.config.connection
        cc.connection_type = m
        cc.esp32_port = self._edit_esp32_port.text().strip()
        cc.esp32_baud = self._spin_esp32_baud.value()
        cc.debug_port = self._edit_debug_port.text().strip()
        cc.debug_baud = self._spin_debug_baud.value()
        cc.udp_host = self._edit_udp_host.text().strip()
        cc.udp_port = self._spin_udp_port.value()
        cc.pan_servo_id = self._spin_pan_id.value()
        cc.tilt_servo_id = self._spin_tilt_id.value()
        cc.bus_servo_time_ms = self._spin_servo_time.value()

        # Push servo config to comm
        self._comm.pan_servo_id = cc.pan_servo_id
        self._comm.tilt_servo_id = cc.tilt_servo_id
        self._comm.bus_servo_time_ms = cc.bus_servo_time_ms
        self._comm.trigger_mode_bb = (self._combo_trigger_mode.currentIndex() == 1)

        ok = self._comm.connect(
            m,
            esp32_port=cc.esp32_port,
            esp32_baud=cc.esp32_baud,
            debug_port=cc.debug_port,
            debug_baud=cc.debug_baud,
            udp_host=cc.udp_host,
            udp_port=cc.udp_port,
        )

        if ok:
            self._btn_connect.setText("Disconnect")
            self._comm.send_command(
                self.engine.current_pan,
                self.engine.current_tilt,
                fire=0,
                move_time_ms=self._get_manual_move_time_ms(),
            )
            info = self._comm.connection_info()
            # Build per-link detail lines
            details = getattr(self._comm, "_connect_details", {})
            detail_lines = []
            for name, (link_ok, val) in details.items():
                mark = "\u2705" if link_ok else "\u274C"
                detail_lines.append(f"{mark} {name}: {val}")
            detail_text = "\n".join(detail_lines) if detail_lines else info
            self._lbl_conn_status.setText(detail_text)
            self._lbl_conn_status.setStyleSheet("color: #33cc33; font-weight: bold;")
            self._log(f"Connected: {info}")
        else:
            # Show per-link status even on failure
            details = getattr(self._comm, "_connect_details", {})
            detail_lines = []
            for name, (link_ok, val) in details.items():
                mark = "\u2705" if link_ok else "\u274C"
                detail_lines.append(f"{mark} {name}: {val}")
            if detail_lines:
                self._lbl_conn_status.setText("\n".join(detail_lines))
            else:
                err = self._comm._last_error or "unknown error"
                self._lbl_conn_status.setText(f"FAILED: {err}")
            self._lbl_conn_status.setStyleSheet("color: #cc3333; font-weight: bold;")
            self._log(f"Connection failed: {self._comm._last_error}")

    # ------------------------------------------------------------------ #
    #  Camera management
    # ------------------------------------------------------------------ #

    def _toggle_camera(self) -> None:
        if self._cap is not None:
            self._close_camera()
            return
        src_text = self._edit_cam_source.text().strip()
        if not src_text:
            self._lbl_cam_status.setText("Using main app feed. Enter a secondary camera index or URL to open one here.")
            self._lbl_cam_status.setStyleSheet("color: #888; font-size: 10px;")
            self._log("Own camera not opened: using main app feed")
            return
        # Save to config
        self.config.connection.camera_source = src_text
        self.config.connection.camera_width = self._spin_cam_w.value()
        self.config.connection.camera_height = self._spin_cam_h.value()
        # Parse source: integer index or string path/URL
        try:
            src = int(src_text)
        except ValueError:
            src = src_text

        # Conflict check: prevent opening the same camera index as the main app.
        # When the main app is on Auto, index 0 is the most common device on single-camera setups.
        if isinstance(src, int):
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
                    self._lbl_cam_status.setText(
                        f"Camera index {src} is already reserved by the main app. Use another index or URL."
                    )
                    self._lbl_cam_status.setStyleSheet("color: #cc3333; font-size: 10px;")
                    self._log(f"Camera open blocked: index {src} is in use by main app")
                    return

        try:
            cap = cv2.VideoCapture(src)
            if not cap.isOpened():
                self._lbl_cam_status.setText(f"Failed to open: {src_text}")
                self._lbl_cam_status.setStyleSheet("color: #cc3333; font-size: 10px;")
                self._log(f"Camera open failed: {src_text}")
                return
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.config.connection.camera_width)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.config.connection.camera_height)
            self._cap = cap
            self._grab_fail_count = 0
            self._cam_timer.start(33)  # ~30 fps
            self._btn_cam.setText("Close Camera")
            actual_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            actual_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self._lbl_cam_status.setText(f"Open: {src_text}  ({actual_w}x{actual_h})")
            self._lbl_cam_status.setStyleSheet("color: #33cc33; font-size: 10px;")
            self._log(f"Camera opened: {src_text} ({actual_w}x{actual_h})")
        except Exception as e:
            self._lbl_cam_status.setText(f"Error: {e}")
            self._lbl_cam_status.setStyleSheet("color: #cc3333; font-size: 10px;")
            self._log(f"Camera error: {e}")

    def _close_camera(self) -> None:
        self._cam_timer.stop()
        self._grab_fail_count = 0
        if self._cap is not None:
            try:
                self._cap.release()
            except Exception:
                pass
            self._cap = None
        try:
            self._btn_cam.setText("Open Camera")
            self._lbl_cam_status.setText("Camera closed")
            self._lbl_cam_status.setStyleSheet("color: #888; font-size: 10px;")
            self._video_label.setText("Waiting for video...")
        except RuntimeError:
            pass  # widget already destroyed during shutdown
        self._log("Camera closed")

    def _grab_frame(self) -> None:
        """Timer-driven: grab a frame from own camera, run detection, push to engine."""
        if self._cap is None or not self._cap.isOpened():
            return
        ret, frame = self._cap.read()
        if not ret or frame is None:
            self._grab_fail_count += 1
            if self._grab_fail_count >= self._MAX_GRAB_FAILS:
                self._log(f"Camera: {self._grab_fail_count} consecutive grab failures — auto-closing")
                self._close_camera()
            return
        self._grab_fail_count = 0
        # Run own detection
        mode = self.config.detection_mode.detection_mode
        raw_boxes = self._detector.detect(frame, mode)
        self.process_frame(frame, raw_boxes, _from_own_camera=True)

    # ------------------------------------------------------------------ #
    #  Detection mode handlers
    # ------------------------------------------------------------------ #

    def _on_detection_mode_changed(self, index: int) -> None:
        self.config.detection_mode.detection_mode = index
        self._update_mode_description()
        self._update_detection_panel_visibility()
        self._detector.reset()
        self._tracker.reset()
        self.detection_mode_changed.emit(index)
        if not self._applying_detection_preset:
            self._set_detection_preset_label(self._match_detection_preset_name())
        if not self._applying_master_preset:
            self._set_master_profile_label(self._match_master_profile_name())
            self._update_master_stack_summary()
        self._push_config()
        self._log(f"Detection mode: {DETECTION_MODES[index]}")

    def _on_detection_settings_changed(self) -> None:
        dm = self.config.detection_mode
        dm.min_contour_area = self._spin_min_contour.value()
        dm.max_contour_area = self._spin_max_contour.value()
        dm.yolo_min_area = self._spin_yolo_min_area.value()
        dm.yolo_confidence = self._spin_yolo_conf.value()
        dm.motion_gate_threshold = self._spin_motion_thresh.value()
        if not self._applying_detection_preset:
            self._set_detection_preset_label(self._match_detection_preset_name())
        if not self._applying_master_preset:
            self._set_master_profile_label(self._match_master_profile_name())
            self._update_master_stack_summary()
        self._push_config()

    def _scan_yolo_models(self) -> None:
        """Populate the YOLO model combo from YOLO_MODELS/ directory."""
        self._combo_yolo_model.clear()
        models_dir = "YOLO_MODELS"
        if os.path.isdir(models_dir):
            for f in sorted(os.listdir(models_dir)):
                if f.endswith(".pt"):
                    self._combo_yolo_model.addItem(f)

    def _load_yolo_model(self) -> None:
        model_name = self._combo_yolo_model.currentText()
        if not model_name:
            self._lbl_yolo_status.setText("No model selected")
            return
        model_path = os.path.join("YOLO_MODELS", model_name)
        self._lbl_yolo_status.setText(f"Loading {model_name}...")
        self._lbl_yolo_status.repaint()
        ok = self._detector.load_yolo(model_path)
        if ok:
            self._lbl_yolo_status.setText(f"Loaded: {model_name}")
            self._lbl_yolo_status.setStyleSheet("color: #33cc33; font-size: 10px;")
            self._log(f"YOLO model loaded: {model_name}")
        else:
            self._lbl_yolo_status.setText("Load FAILED")
            self._lbl_yolo_status.setStyleSheet("color: #cc3333; font-size: 10px;")
            self._log(f"YOLO load failed: {model_name}")

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
        self._log(f"YOLO classes: {classes}")

    def _on_color_settings_changed(self) -> None:
        dm = self.config.detection_mode
        dm.color_preset = self._combo_color_preset.currentText()
        dm.color_min_area = self._spin_color_min.value()
        dm.color_max_area = self._spin_color_max.value()
        dm.color_fusion_strategy = self._combo_fusion.currentText()
        dm.color_fusion_overlap = self._spin_fusion_overlap.value()
        self.color_preset_changed.emit(dm.color_preset)
        if not self._applying_detection_preset:
            self._set_detection_preset_label(self._match_detection_preset_name())
        if not self._applying_master_preset:
            self._set_master_profile_label(self._match_master_profile_name())
            self._update_master_stack_summary()
        self._push_config()

    def _update_detection_panel_visibility(self) -> None:
        """Show/hide detection sub-panels based on selected mode."""
        mode = self._combo_detection_mode.currentIndex()
        contour_modes = {0, 1, 3, 7, 8, 10}
        yolo_modes = {2, 4, 5, 9, 10}
        color_modes = {6, 7, 8, 9, 10}
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

    def _on_engagement_changed(self) -> None:
        eg = self.config.engagement
        eg.min_threat_score = self._spin_min_threat.value()
        eg.burst_count = self._spin_burst.value()
        eg.burst_interval_ms = self._spin_burst_interval.value()
        eg.inter_target_cooldown = self._spin_inter_cd.value()
        eg.cycle_cooldown = self._spin_cycle_cd.value()
        eg.max_queue_length = self._spin_max_queue.value()
        eg.optimize_slew_order = self._chk_optimize.isChecked()
        if eg.single_target_only:
            eg.max_queue_length = 1
            eg.optimize_slew_order = False
            self._spin_max_queue.blockSignals(True)
            self._spin_max_queue.setValue(1)
            self._spin_max_queue.blockSignals(False)
            self._chk_optimize.blockSignals(True)
            self._chk_optimize.setChecked(False)
            self._chk_optimize.blockSignals(False)
        eg.engagement_speed = self._slider_speed.value()
        eg.precision_aim_enabled = self._chk_precision.isChecked()
        eg.precision_settle_time = self._spin_prec_settle.value()
        eg.precision_max_step = self._spin_prec_step.value()
        if not self._applying_engagement_preset:
            self._set_engagement_preset_label(self._match_engagement_preset_name())
        if not self._applying_master_preset:
            self._set_master_profile_label(self._match_master_profile_name())
            self._update_master_stack_summary()
        self._push_config()

    def _on_guard_changed(self) -> None:
        g = self.config.guard
        g.guard_pan = self._spin_guard_pan.value()
        g.guard_tilt = self._spin_guard_tilt.value()
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
        self._push_config()

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
        self.overlay.update_config(self.config)

    # ------------------------------------------------------------------ #
    #  Auto-trigger / trigger mode
    # ------------------------------------------------------------------ #

    def _on_auto_trigger_toggled(self, checked: bool) -> None:
        self.config.engagement.auto_trigger_enabled = checked
        self._chk_auto_trigger.setStyleSheet(
            "font-weight: bold; color: #ff4d4d;" if checked else "font-weight: bold; color: #66dd88;"
        )
        if not self._applying_master_preset:
            self._set_master_profile_label(self._match_master_profile_name())
            self._update_master_stack_summary()
        self._push_config()
        self._log(f"Auto-trigger: {'ON' if checked else 'OFF'}")

    def _on_trigger_mode_changed(self, index: int) -> None:
        is_bb = (index == 1)
        self.config.engagement.trigger_mode_bb = is_bb
        self._comm.trigger_mode_bb = is_bb
        if self._comm.is_connected():
            self._comm.send_command(
                self.engine.current_pan,
                self.engine.current_tilt,
                fire=0,
                move_time_ms=self._get_manual_move_time_ms(),
            )
        if not self._applying_master_preset:
            self._set_master_profile_label(self._match_master_profile_name())
            self._update_master_stack_summary()
        self._push_config()
        mode_name = "Projectile (BB)" if is_bb else "Water (MOSFET)"
        self._log(f"Trigger mode: {mode_name}")

    # ------------------------------------------------------------------ #
    #  Manual control handlers
    # ------------------------------------------------------------------ #

    def _manual_move(self, pan_dir: int, tilt_dir: int) -> None:
        step = self._spin_step.value()
        new_pan = self.engine.current_pan + pan_dir * step
        new_tilt = self.engine.current_tilt + tilt_dir * step
        new_pan, new_tilt = self._clamp_manual_angles(new_pan, new_tilt)
        self.engine.current_pan = new_pan
        self.engine.current_tilt = new_tilt
        self._comm.send_command(new_pan, new_tilt, move_time_ms=self._get_manual_move_time_ms())
        self._remember_commanded_position(new_pan, new_tilt)
        self._suppress_motion_detection()

    def _on_home_clicked(self) -> None:
        pan = self._spin_guard_pan.value()
        tilt = self._spin_guard_tilt.value()
        pan, tilt = self._clamp_manual_angles(pan, tilt)
        self.engine.current_pan = pan
        self.engine.current_tilt = tilt
        self._comm.send_command(pan, tilt, move_time_ms=self._get_manual_move_time_ms())
        self._remember_commanded_position(pan, tilt)
        self._suppress_motion_detection()
        self._log("Go Home")

    def _on_led_toggled(self, checked: bool) -> None:
        self._led_on = checked
        self._btn_led.setText(f"LED: {'ON' if checked else 'OFF'}")
        self._comm.set_led(checked, self.engine.current_pan, self.engine.current_tilt)

    def _on_laser_toggled(self, checked: bool) -> None:
        self._laser_on = checked
        self._btn_laser.setText(f"Laser: {'ON' if checked else 'OFF'}")
        self._comm.set_laser(checked, self.engine.current_pan, self.engine.current_tilt)

    def _on_safety_toggled(self, checked: bool) -> None:
        self._safety_armed = checked
        self._btn_safety.setText(f"Safety: {'ARMED' if checked else 'LOCKED'}")
        self._comm.set_safety(checked, self.engine.current_pan, self.engine.current_tilt)

    def _on_manual_fire(self, state: int) -> None:
        if state and not self._safety_armed:
            self._log("Manual fire blocked: Safety is LOCKED")
            self._comm.send_command(
                self.engine.current_pan,
                self.engine.current_tilt,
                fire=0,
                move_time_ms=self._get_manual_move_time_ms(),
            )
            return
        pan = self.engine.current_pan
        tilt = self.engine.current_tilt
        self._comm.send_command(pan, tilt, fire=state, move_time_ms=self._get_manual_move_time_ms())

    # ------------------------------------------------------------------ #
    #  Guard position buttons
    # ------------------------------------------------------------------ #

    def _go_to_guard(self) -> None:
        pan = self._spin_guard_pan.value()
        tilt = self._spin_guard_tilt.value()
        pan, tilt = self._clamp_manual_angles(pan, tilt)
        self.engine.current_pan = pan
        self.engine.current_tilt = tilt
        self._comm.send_command(pan, tilt, move_time_ms=self._get_manual_move_time_ms())
        self._remember_commanded_position(pan, tilt)
        self._suppress_motion_detection()
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
            # Persist connection settings from UI
            cc = self.config.connection
            cc.connection_type = self._combo_conn_type.currentIndex()
            cc.esp32_port = self._edit_esp32_port.text().strip()
            cc.esp32_baud = self._spin_esp32_baud.value()
            cc.debug_port = self._edit_debug_port.text().strip()
            cc.debug_baud = self._spin_debug_baud.value()
            cc.udp_host = self._edit_udp_host.text().strip()
            cc.udp_port = self._spin_udp_port.value()
            cc.pan_servo_id = self._spin_pan_id.value()
            cc.tilt_servo_id = self._spin_tilt_id.value()
            cc.bus_servo_time_ms = self._spin_servo_time.value()
            cc.invert_pan = self._chk_invert_pan.isChecked()
            cc.invert_tilt = self._chk_invert_tilt.isChecked()
            cc.camera_source = self._edit_cam_source.text().strip()
            cc.camera_width = self._spin_cam_w.value()
            cc.camera_height = self._spin_cam_h.value()
            self.config.settings_panel_width = int(self._slider_panel_width.value())
            self.config.save()
            self._log("Settings saved")
        except Exception as e:
            self._log(f"Save error: {e}")

    # ------------------------------------------------------------------ #
    #  Internal helpers
    # ------------------------------------------------------------------ #

    def set_host_main_window(self, main_window: Optional[QWidget]) -> None:
        self._main_window_ref = main_window

    def _get_main_window(self):
        """Walk parent chain to find the main application window (best-effort)."""
        if self._main_window_ref is not None:
            return self._main_window_ref
        w = self.parent()
        while w is not None:
            if hasattr(w, "cap"):  # main window has self.cap
                return w
            w = w.parent() if hasattr(w, "parent") else None
        return None

    def _on_panel_width_changed(self, value: int) -> None:
        width = int(value)
        self.config.settings_panel_width = width
        self._lbl_panel_width.setText(f"{width} px")
        self._apply_panel_width(width)

    def _apply_saved_panel_width(self) -> None:
        self._apply_panel_width(int(self.config.settings_panel_width))

    def _apply_panel_width(self, width: int) -> None:
        width = max(320, min(820, int(width)))
        total_width = self._main_splitter.size().width()
        if total_width <= 0:
            total_width = max(self.width(), width + 720)
        left_width = max(480, total_width - width)
        self._main_splitter.setSizes([left_width, width])

    def _on_servo_time_changed(self, value: int) -> None:
        move_time = int(value)
        self.config.connection.bus_servo_time_ms = move_time
        self._comm.bus_servo_time_ms = move_time
        if not self._applying_servo_preset:
            self._set_servo_time_preset_label(self._match_servo_time_preset_name())
        if not self._applying_master_preset:
            self._set_master_profile_label(self._match_master_profile_name())
            self._update_master_stack_summary()

    def _set_master_profile_label(self, preset_name: Optional[str]) -> None:
        if not hasattr(self, "_lbl_master_profile"):
            return
        if preset_name and preset_name in MASTER_PROFILE_PRESETS:
            preset = MASTER_PROFILE_PRESETS[preset_name]
            self._lbl_master_profile.setText(f"Active profile: {preset['label']} | {preset['description']}")
        else:
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
        for preset_name, preset in MASTER_PROFILE_PRESETS.items():
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
            matched = True
            for key, value in preset["settings"].items():
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

    def _apply_threat_preset(self, preset_name: str) -> None:
        preset = THREAT_AI_PRESETS.get(preset_name)
        if not preset:
            return

        self._applying_threat_preset = True
        try:
            for key, value in preset["weights"].items():
                slider = self._weight_sliders[key]
                slider.blockSignals(True)
                slider.setValue(int(round(float(value) * 100.0)))
                slider.blockSignals(False)
                if key in self._weight_value_labels:
                    self._weight_value_labels[key].setText(f"{float(value):.2f}")
            self._chk_ml.blockSignals(True)
            self._chk_ml.setChecked(bool(preset.get("use_ml_model", False)))
            self._chk_ml.blockSignals(False)
            self._on_scoring_changed()
            self._set_threat_preset_label(preset_name)
            if not self._applying_master_preset:
                self._set_master_profile_label(self._match_master_profile_name())
                self._update_master_stack_summary()
            self._log(f"Threat AI preset: {preset['label']}")
        finally:
            self._applying_threat_preset = False

    def _apply_detection_preset(self, preset_name: str) -> None:
        preset = DETECTION_PRESETS.get(preset_name)
        if not preset:
            return

        settings = preset["settings"]
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
            self._detector.reset()
            self._tracker.reset()
            self.detection_mode_changed.emit(int(settings["detection_mode"]))
            self._push_config()
            self._set_detection_preset_label(preset_name)
            if not self._applying_master_preset:
                self._set_master_profile_label(self._match_master_profile_name())
                self._update_master_stack_summary()
            self._log(f"Detection preset: {preset['label']}")
        finally:
            self._applying_detection_preset = False

    def _apply_filter_preset(self, preset_name: str) -> None:
        preset = TARGET_FILTER_PRESETS.get(preset_name)
        if not preset:
            return

        settings = preset["settings"]
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
            self._detector.set_yolo_classes(",".join(tf.allowed_classes))
            self._push_config()
            self._set_filter_preset_label(preset_name)
            if not self._applying_master_preset:
                self._set_master_profile_label(self._match_master_profile_name())
                self._update_master_stack_summary()
            self._log(f"Target Filter preset: {preset['label']}")
        finally:
            self._applying_filter_preset = False

    def _apply_servo_time_preset(self, preset_name: str) -> None:
        preset = BUS_SERVO_TIME_PRESETS.get(preset_name)
        if not preset:
            return

        self._applying_servo_preset = True
        try:
            self._spin_servo_time.blockSignals(True)
            self._spin_servo_time.setValue(int(preset["move_time_ms"]))
            self._spin_servo_time.blockSignals(False)
            self._on_servo_time_changed(int(preset["move_time_ms"]))
            self._set_servo_time_preset_label(preset_name)
            if not self._applying_master_preset:
                self._set_master_profile_label(self._match_master_profile_name())
                self._update_master_stack_summary()
            self._log(f"Servo move-time preset: {preset['label']} ({int(preset['move_time_ms'])} ms)")
        finally:
            self._applying_servo_preset = False

    def _apply_master_profile(self, preset_name: str) -> None:
        preset = MASTER_PROFILE_PRESETS.get(preset_name)
        if not preset:
            return

        self._applying_master_preset = True
        try:
            self._apply_detection_preset(preset["detection"])
            self._apply_filter_preset(preset["filter"])
            self._apply_threat_preset(preset["threat"])
            self._apply_engagement_preset(preset["engagement"])
            self._apply_servo_time_preset(preset["servo"])
            self._set_master_profile_label(preset_name)
            self._update_master_stack_summary()
            self._log(f"Master profile: {preset['label']}")
        finally:
            self._applying_master_preset = False

    def _apply_engagement_preset(self, preset_name: str) -> None:
        preset = ENGAGEMENT_PRESETS.get(preset_name)
        if not preset:
            return

        settings = preset["settings"]
        self._applying_engagement_preset = True
        try:
            self._chk_auto_trigger.blockSignals(True)
            self._chk_auto_trigger.setChecked(bool(settings["auto_trigger_enabled"]))
            self._chk_auto_trigger.blockSignals(False)

            self._combo_trigger_mode.blockSignals(True)
            self._combo_trigger_mode.setCurrentIndex(1 if settings["trigger_mode_bb"] else 0)
            self._combo_trigger_mode.blockSignals(False)

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

            eg = self.config.engagement
            for key, value in settings.items():
                setattr(eg, key, value)
            self._comm.trigger_mode_bb = bool(settings["trigger_mode_bb"])
            self._on_engagement_changed()
            self._set_engagement_preset_label(preset_name)
            if not self._applying_master_preset:
                self._set_master_profile_label(self._match_master_profile_name())
                self._update_master_stack_summary()
            self._log(f"Engagement preset: {preset['label']}")
        finally:
            self._applying_engagement_preset = False

    def _start_fire_burst(self, pan: float, tilt: float, burst_count: int, interval_ms: int) -> None:
        self._stop_fire_burst(send_release=True)
        self._burst_pan = pan
        self._burst_tilt = tilt
        self._burst_remaining = max(1, int(burst_count))
        self._burst_interval_ms = max(10, int(interval_ms))
        self._burst_phase_on = True
        self._comm.send_command(self._burst_pan, self._burst_tilt, fire=1)
        self._burst_timer.start(self._burst_interval_ms)

    def _advance_fire_burst(self) -> None:
        if self._burst_remaining <= 0:
            self._stop_fire_burst(send_release=False)
            return

        if self._burst_phase_on:
            self._comm.send_command(self._burst_pan, self._burst_tilt, fire=0)
            self._burst_remaining -= 1
            if self._burst_remaining <= 0:
                self._stop_fire_burst(send_release=False)
                return
            self._burst_phase_on = False
            self._burst_timer.start(self._burst_interval_ms)
            return

        self._burst_phase_on = True
        self._comm.send_command(self._burst_pan, self._burst_tilt, fire=1)
        self._burst_timer.start(self._burst_interval_ms)

    def _stop_fire_burst(self, *, send_release: bool) -> None:
        self._burst_timer.stop()
        if send_release and self._burst_phase_on:
            self._comm.send_command(self._burst_pan, self._burst_tilt, fire=0)
        self._burst_remaining = 0
        self._burst_phase_on = False

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
        d.color_fusion_overlap = dm.color_fusion_overlap
        d.custom_hsv_lower = (dm.custom_h_min, dm.custom_s_min, dm.custom_v_min)
        d.custom_hsv_upper = (dm.custom_h_max, dm.custom_s_max, dm.custom_v_max)
        d.set_yolo_classes(",".join(self.config.target_filter.allowed_classes))

    def _clamp_manual_angles(self, pan: float, tilt: float) -> Tuple[float, float]:
        g = self.config.guard
        pan_min, pan_max = sorted((g.pan_min, g.pan_max))
        tilt_min, tilt_max = sorted((g.tilt_min, g.tilt_max))
        return (
            max(pan_min, min(pan_max, pan)),
            max(tilt_min, min(tilt_max, tilt)),
        )

    def _remember_commanded_position(self, pan: float, tilt: float) -> None:
        self._last_commanded_pan = float(pan)
        self._last_commanded_tilt = float(tilt)

    def _get_command_delta(self, pan: float, tilt: float) -> float:
        prev_pan = float(getattr(self, "_last_commanded_pan", pan))
        prev_tilt = float(getattr(self, "_last_commanded_tilt", tilt))
        return float(max(abs(float(pan) - prev_pan), abs(float(tilt) - prev_tilt)))

    def _get_manual_move_time_ms(self) -> int:
        return int(max(70, int(self.config.connection.bus_servo_time_ms)))

    def _get_tracking_move_time_ms(self, move_delta: float) -> int:
        base_time = int(max(20, int(self.config.connection.bus_servo_time_ms)))
        speed_value = int(np.clip(self.config.engagement.engagement_speed, 10, 100))
        dynamic_time = int(round(np.interp(speed_value, [10, 100], [120, 35])))
        if move_delta <= 0.8:
            dynamic_time = max(dynamic_time, 70)
        elif move_delta <= 2.5:
            dynamic_time = max(dynamic_time, 55)
        return int(max(base_time, dynamic_time))

    def _get_tracking_motion_suppression_s(self, move_delta: float) -> float:
        mode = int(self.config.detection_mode.detection_mode)
        motion_sensitive_modes = {0, 1, 3, 4, 5, 7, 8, 10}
        if mode not in motion_sensitive_modes:
            return 0.0
        base_suppression = float(max(0.0, self.config.detection_mode.motion_ignore_after_move_s))
        if move_delta <= 0.35:
            return 0.0
        if move_delta <= 1.0:
            return min(base_suppression, 0.05)
        if move_delta <= 2.5:
            return min(base_suppression, 0.08)
        return min(base_suppression, 0.12)

    def _suppress_motion_detection(self, seconds: Optional[float] = None) -> None:
        suppress_for = self.config.detection_mode.motion_ignore_after_move_s if seconds is None else seconds
        if suppress_for > 0:
            self._detector.suppress_motion(float(suppress_for))

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
        self, raw: list, frame_w: int, frame_h: int, timestamp: Optional[float] = None
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
            if class_id == -1:
                class_name = "motion"
                source = "frame_diff"
            elif class_id == -2:
                class_name = "foreground"
                source = "backsub"
            elif class_id == -3:
                class_name = "color"
                source = "color"
            elif class_id == -4:
                class_name = "moving_object"
                source = "motion_locked"
            else:
                class_name = (
                    YOLO_COCO_CLASSES[class_id]
                    if 0 <= class_id < len(YOLO_COCO_CLASSES)
                    else "unknown"
                )
                source = "yolo"
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
        return self._tracker.assign_tracks(result, timestamp or time.time())

    def _show_frame(self, frame: np.ndarray) -> None:
        """Convert BGR frame to QPixmap and display."""
        try:
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rgb = np.ascontiguousarray(rgb)
            h, w, ch = rgb.shape
            bytes_per_line = int(rgb.strides[0])
            qimg = QImage(rgb.data, w, h, bytes_per_line, QImage.Format_RGB888).copy()
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
            f"Engaged: {stats['engagements_total']}\n"
            f"Err P/T: {stats['last_err_pan_deg']:+.2f}/{stats['last_err_tilt_deg']:+.2f} | "
            f"Lock: {stats['aim_lock_frames']} | "
            f"Move: {int(getattr(self, '_last_tracking_move_time_ms', 0))}ms | "
            f"Suppress: {float(getattr(self, '_last_tracking_suppression_s', 0.0)):.2f}s"
        )
        reacquire_note = str(stats.get('reacquire_note') or '')
        if stats.get('reacquire_recent') and reacquire_note and reacquire_note != self._last_reacquire_note_seen:
            self._last_reacquire_note_seen = reacquire_note
            self._log(f"Tracking {reacquire_note}")
        # Update last-command diagnostic in connection tab
        if hasattr(self, "_lbl_last_cmd"):
            cmd = self._comm._last_cmd
            if cmd:
                self._lbl_last_cmd.setText(f"Last: {cmd}")

    def _log(self, msg: str) -> None:
        ts = time.strftime("%H:%M:%S")
        self._log_text.append(f"[{ts}] {msg}")
        # Auto-scroll
        sb = self._log_text.verticalScrollBar()
        sb.setValue(sb.maximum())

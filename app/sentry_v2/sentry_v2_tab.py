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

import json
import os
import queue
import sys
import threading
import time
from pathlib import Path
from typing import List, Optional, Tuple

import cv2
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QCheckBox, QSlider, QGroupBox, QFrame, QSizePolicy,
    QSpacerItem, QScrollArea, QDoubleSpinBox, QSpinBox,
    QComboBox, QListWidget, QListWidgetItem, QAbstractItemView,
    QTabWidget, QTextEdit, QGridLayout, QLineEdit, QSplitter, QMessageBox,
    QFileDialog,
)
from PyQt5.QtCore import Qt, pyqtSignal, QTimer, QEvent, QObject, QProcess, QProcessEnvironment
from PyQt5.QtGui import QImage, QPixmap, QColor, QIcon

from .sentry_v2_config import (
    SentryV2Config,
    EngagementConfig,
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
from .sentry_v2_tooltips import SENTRY_V2_TOOLTIPS
from .sentry_v2_config import (
    SENTRY_PAN_MAX,
    SENTRY_PAN_MIN,
    SENTRY_TILT_MAX,
    SENTRY_TILT_MIN,
)
from .target_filter import DetectedObject


class NoWheelScrollFilter(QObject):
    """Event filter to block mouse wheel scrolling on spinboxes and sliders."""
    def eventFilter(self, obj, event):
        if event.type() == QEvent.Wheel:
            return True  # Block the wheel event
        return super().eventFilter(obj, event)


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
    (1024, 576),
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

CUSTOM_MASTER_PRESET_PATH = Path(__file__).resolve().parents[1] / "config" / "sentry_v2_custom_presets.json"
SENTRY_V2_SETTINGS_PATH = Path(__file__).resolve().parents[1] / "config" / "sentry_v2_settings.json"
LEGACY_SENTRY_V2_SETTINGS_PATH = Path(__file__).resolve().parents[1] / "app" / "config" / "sentry_v2_settings.json"
SENTRY_V2_PANEL_MIN_WIDTH = 560
SENTRY_V2_PANEL_DEFAULT_WIDTH = 620
SENTRY_V2_VIDEO_MIN_WIDTH = 120
SENTRY_V2_WIDGET_MIN_WIDTH = SENTRY_V2_PANEL_MIN_WIDTH + SENTRY_V2_VIDEO_MIN_WIDTH + 28

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
        "description": "Color mask plus frame-diff motion for moving colored objects. With the shipped red-color preset, detections must overlap both the selected color and motion before they count.",
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
        "description": "Color mask plus foreground agreement for moving colored objects. With the shipped red-color preset, detections must overlap both the selected color and foreground motion.",
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
        "description": "Color mask fused with YOLO for class-aware colored-object follow. With the shipped red-color preset, detections must overlap both the selected color and the YOLO box.",
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
            "aim_lock_pan_tolerance": 0.28,
            "aim_lock_tilt_tolerance": 0.24,
            "aim_lock_required_frames": 8,
            "fire_trigger_enter_pan_tolerance": 0.18,
            "fire_trigger_enter_tilt_tolerance": 0.15,
            "fire_trigger_exit_pan_tolerance": 0.28,
            "fire_trigger_exit_tilt_tolerance": 0.22,
            "fire_recenter_pan_tolerance": 0.24,
            "fire_recenter_tilt_tolerance": 0.20,
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
            "aim_lock_pan_tolerance": 0.28,
            "aim_lock_tilt_tolerance": 0.24,
            "aim_lock_required_frames": 4,
            "fire_trigger_enter_pan_tolerance": 0.18,
            "fire_trigger_enter_tilt_tolerance": 0.15,
            "fire_trigger_exit_pan_tolerance": 0.28,
            "fire_trigger_exit_tilt_tolerance": 0.22,
            "fire_recenter_pan_tolerance": 0.24,
            "fire_recenter_tilt_tolerance": 0.20,
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
            "min_threat_score": 0.52,
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
            "aim_lock_pan_tolerance": 0.18,
            "aim_lock_tilt_tolerance": 0.14,
            "aim_lock_required_frames": 8,
            "fire_trigger_enter_pan_tolerance": 0.12,
            "fire_trigger_enter_tilt_tolerance": 0.09,
            "fire_trigger_exit_pan_tolerance": 0.18,
            "fire_trigger_exit_tilt_tolerance": 0.14,
            "fire_recenter_pan_tolerance": 0.18,
            "fire_recenter_tilt_tolerance": 0.14,
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
            "min_threat_score": 0.36,
            "burst_count": 2,
            "burst_interval_ms": 70,
            "inter_target_cooldown": 1.00,
            "cycle_cooldown": 2.00,
            "max_queue_length": 1,
            "optimize_slew_order": False,
            "engagement_speed": 54,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.62,
            "precision_max_step": 0.55,
            "precision_deadzone_pan_deg": 0.10,
            "precision_deadzone_tilt_deg": 0.08,
            "precision_error_ema": 0.46,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 0.30,
            "aim_lock_tilt_tolerance": 0.24,
            "aim_lock_required_frames": 6,
            "fire_trigger_enter_pan_tolerance": 0.17,
            "fire_trigger_enter_tilt_tolerance": 0.13,
            "fire_trigger_exit_pan_tolerance": 0.26,
            "fire_trigger_exit_tilt_tolerance": 0.20,
            "fire_recenter_pan_tolerance": 0.30,
            "fire_recenter_tilt_tolerance": 0.24,
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
            "engagement_speed": 78,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.28,
            "precision_max_step": 1.05,
            "precision_deadzone_pan_deg": 0.13,
            "precision_deadzone_tilt_deg": 0.10,
            "precision_error_ema": 0.36,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 0.42,
            "aim_lock_tilt_tolerance": 0.34,
            "aim_lock_required_frames": 4,
            "fire_trigger_enter_pan_tolerance": 0.22,
            "fire_trigger_enter_tilt_tolerance": 0.17,
            "fire_trigger_exit_pan_tolerance": 0.32,
            "fire_trigger_exit_tilt_tolerance": 0.25,
            "fire_recenter_pan_tolerance": 0.40,
            "fire_recenter_tilt_tolerance": 0.32,
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
            "engagement_speed": 84,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.22,
            "precision_max_step": 1.25,
            "precision_deadzone_pan_deg": 0.16,
            "precision_deadzone_tilt_deg": 0.13,
            "precision_error_ema": 0.34,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 0.52,
            "aim_lock_tilt_tolerance": 0.42,
            "aim_lock_required_frames": 4,
            "fire_trigger_enter_pan_tolerance": 0.24,
            "fire_trigger_enter_tilt_tolerance": 0.19,
            "fire_trigger_exit_pan_tolerance": 0.36,
            "fire_trigger_exit_tilt_tolerance": 0.28,
            "fire_recenter_pan_tolerance": 0.46,
            "fire_recenter_tilt_tolerance": 0.36,
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
            "engagement_speed": 76,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.32,
            "precision_max_step": 0.90,
            "precision_deadzone_pan_deg": 0.08,
            "precision_deadzone_tilt_deg": 0.07,
            "precision_error_ema": 0.50,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 0.26,
            "aim_lock_tilt_tolerance": 0.21,
            "aim_lock_required_frames": 4,
            "fire_trigger_enter_pan_tolerance": 0.14,
            "fire_trigger_enter_tilt_tolerance": 0.12,
            "fire_trigger_exit_pan_tolerance": 0.22,
            "fire_trigger_exit_tilt_tolerance": 0.18,
            "fire_recenter_pan_tolerance": 0.24,
            "fire_recenter_tilt_tolerance": 0.20,
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
            "engagement_speed": 82,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.26,
            "precision_max_step": 1.10,
            "precision_deadzone_pan_deg": 0.07,
            "precision_deadzone_tilt_deg": 0.06,
            "precision_error_ema": 0.54,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 0.20,
            "aim_lock_tilt_tolerance": 0.16,
            "aim_lock_required_frames": 3,
            "fire_trigger_enter_pan_tolerance": 0.11,
            "fire_trigger_enter_tilt_tolerance": 0.09,
            "fire_trigger_exit_pan_tolerance": 0.17,
            "fire_trigger_exit_tilt_tolerance": 0.14,
            "fire_recenter_pan_tolerance": 0.20,
            "fire_recenter_tilt_tolerance": 0.16,
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
            "engagement_speed": 92,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.18,
            "precision_max_step": 1.45,
            "precision_deadzone_pan_deg": 0.06,
            "precision_deadzone_tilt_deg": 0.05,
            "precision_error_ema": 0.58,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 0.16,
            "aim_lock_tilt_tolerance": 0.13,
            "aim_lock_required_frames": 2,
            "fire_trigger_enter_pan_tolerance": 0.09,
            "fire_trigger_enter_tilt_tolerance": 0.07,
            "fire_trigger_exit_pan_tolerance": 0.14,
            "fire_trigger_exit_tilt_tolerance": 0.11,
            "fire_recenter_pan_tolerance": 0.16,
            "fire_recenter_tilt_tolerance": 0.13,
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
            "engagement_speed": 88,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.22,
            "precision_max_step": 1.20,
            "precision_deadzone_pan_deg": 0.07,
            "precision_deadzone_tilt_deg": 0.06,
            "precision_error_ema": 0.52,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 0.22,
            "aim_lock_tilt_tolerance": 0.18,
            "aim_lock_required_frames": 3,
            "fire_trigger_enter_pan_tolerance": 0.12,
            "fire_trigger_enter_tilt_tolerance": 0.10,
            "fire_trigger_exit_pan_tolerance": 0.18,
            "fire_trigger_exit_tilt_tolerance": 0.14,
            "fire_recenter_pan_tolerance": 0.20,
            "fire_recenter_tilt_tolerance": 0.16,
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
            "engagement_speed": 68,
            "precision_aim_enabled": True,
            "precision_settle_time": 0.38,
            "precision_max_step": 0.80,
            "precision_deadzone_pan_deg": 0.10,
            "precision_deadzone_tilt_deg": 0.08,
            "precision_error_ema": 0.50,
            "fire_requires_lock": True,
            "aim_lock_pan_tolerance": 0.40,
            "aim_lock_tilt_tolerance": 0.32,
            "aim_lock_required_frames": 5,
            "fire_trigger_enter_pan_tolerance": 0.24,
            "fire_trigger_enter_tilt_tolerance": 0.19,
            "fire_trigger_exit_pan_tolerance": 0.36,
            "fire_trigger_exit_tilt_tolerance": 0.28,
            "fire_recenter_pan_tolerance": 0.38,
            "fire_recenter_tilt_tolerance": 0.30,
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
            "aim_lock_pan_tolerance": 0.080,
            "aim_lock_tilt_tolerance": 0.060,
            "aim_lock_required_frames": 12,
            "fire_trigger_enter_pan_tolerance": 0.050,
            "fire_trigger_enter_tilt_tolerance": 0.040,
            "fire_trigger_exit_pan_tolerance": 0.080,
            "fire_trigger_exit_tilt_tolerance": 0.060,
            "fire_recenter_pan_tolerance": 0.090,
            "fire_recenter_tilt_tolerance": 0.070,
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
            "aim_lock_pan_tolerance": 0.090,
            "aim_lock_tilt_tolerance": 0.070,
            "aim_lock_required_frames": 10,
            "fire_trigger_enter_pan_tolerance": 0.060,
            "fire_trigger_enter_tilt_tolerance": 0.050,
            "fire_trigger_exit_pan_tolerance": 0.090,
            "fire_trigger_exit_tilt_tolerance": 0.070,
            "fire_recenter_pan_tolerance": 0.100,
            "fire_recenter_tilt_tolerance": 0.080,
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
            "aim_lock_pan_tolerance": 0.110,
            "aim_lock_tilt_tolerance": 0.080,
            "aim_lock_required_frames": 9,
            "fire_trigger_enter_pan_tolerance": 0.080,
            "fire_trigger_enter_tilt_tolerance": 0.060,
            "fire_trigger_exit_pan_tolerance": 0.120,
            "fire_trigger_exit_tilt_tolerance": 0.090,
            "fire_recenter_pan_tolerance": 0.130,
            "fire_recenter_tilt_tolerance": 0.100,
            "target_loss_timeout": 2.50,
            "aim_lock_timeout": 3.00,
            "continuous_hunt_on_loss": True,
        },
    },
}

AIM_LOCK_FIRE_GATE_PRESETS = {
    "stable_lock": {
        "label": "Stable Lock",
        "tooltip_key": "preset_aim_gate_stable_lock",
        "settings": {
            "precision_deadzone_pan_deg": 0.07,
            "precision_deadzone_tilt_deg": 0.06,
            "precision_error_ema": 0.40,
            "aim_lock_pan_tolerance": 0.18,
            "aim_lock_tilt_tolerance": 0.14,
            "aim_lock_required_frames": 8,
            "fire_trigger_enter_pan_tolerance": 0.12,
            "fire_trigger_enter_tilt_tolerance": 0.09,
            "fire_trigger_exit_pan_tolerance": 0.18,
            "fire_trigger_exit_tilt_tolerance": 0.14,
            "fire_recenter_pan_tolerance": 0.18,
            "fire_recenter_tilt_tolerance": 0.14,
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
            "aim_lock_pan_tolerance": 0.30,
            "aim_lock_tilt_tolerance": 0.24,
            "aim_lock_required_frames": 5,
            "fire_trigger_enter_pan_tolerance": 0.18,
            "fire_trigger_enter_tilt_tolerance": 0.14,
            "fire_trigger_exit_pan_tolerance": 0.28,
            "fire_trigger_exit_tilt_tolerance": 0.22,
            "fire_recenter_pan_tolerance": 0.30,
            "fire_recenter_tilt_tolerance": 0.24,
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
            "aim_lock_pan_tolerance": 0.50,
            "aim_lock_tilt_tolerance": 0.40,
            "aim_lock_required_frames": 2,
            "fire_trigger_enter_pan_tolerance": 0.24,
            "fire_trigger_enter_tilt_tolerance": 0.19,
            "fire_trigger_exit_pan_tolerance": 0.36,
            "fire_trigger_exit_tilt_tolerance": 0.28,
            "fire_recenter_pan_tolerance": 0.44,
            "fire_recenter_tilt_tolerance": 0.34,
            "target_loss_timeout": 0.65,
        },
    },
}

SENTRY_V2_THEME = """
QWidget#sentryV2Root {
    background-color: #101720;
    color: #e6edf3;
    font-family: "Segoe UI";
    font-size: 10pt;
}
QWidget#sentryV2Root QLabel {
    color: #d8e2ec;
}
QWidget#sentryV2Root QScrollArea,
QWidget#sentryV2Root QScrollArea > QWidget > QWidget {
    background-color: #101821;
    border: none;
}
QWidget#sentryV2Root QGroupBox {
    background-color: #16212c;
    border: 1px solid #304255;
    border-radius: 12px;
    margin-top: 12px;
    padding: 12px 10px 10px 10px;
    font-weight: 600;
}
QWidget#sentryV2Root QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 6px;
    color: #86d7ff;
}
QWidget#sentryV2Root QWidget#sentryV2PinnedBottom {
    background-color: #101821;
    border-top: 1px solid #2f4459;
    border-radius: 10px 10px 0 0;
    padding-top: 4px;
}
QWidget#sentryV2Root QWidget#sentryV2PinnedTop {
    background-color: #101821;
    border-bottom: 1px solid #2f4459;
    border-radius: 0 0 10px 10px;
    padding: 4px 0 2px 0;
}
QWidget#sentryV2Root QWidget#sentryV2PinnedBottom QGroupBox {
    margin-top: 8px;
    padding: 10px 8px 8px 8px;
}
QWidget#sentryV2Root QWidget#sentryV2PinnedBottom QLabel {
    color: #d2dde7;
}
QWidget#sentryV2Root QTabWidget::pane {
    background-color: #131d28;
    border: 1px solid #304255;
    border-radius: 10px;
    top: -1px;
}
QWidget#sentryV2Root QTabBar::tab {
    background-color: #1a2531;
    border: 1px solid #304255;
    border-radius: 8px;
    padding: 4px 2px;
    min-height: 30px;
}
QWidget#sentryV2Root QTabBar::tab:left {
    min-width: 40px;
    max-width: 48px;
    margin-bottom: 3px;
}
QWidget#sentryV2Root QTabBar::tab:top {
    border-bottom: none;
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
    margin-right: 6px;
}
QWidget#sentryV2Root QTabBar::tab:selected {
    background-color: #23374a;
    border-color: #6ec4ff;
    color: #f4fbff;
}
QWidget#sentryV2Root QTabBar::tab:selected:left {
    border-left: 3px solid #6ec4ff;
}
QWidget#sentryV2Root QTabBar::tab:hover:!selected {
    background-color: #213140;
    color: #eef6ff;
}
QWidget#sentryV2Root QPushButton {
    background-color: #22364a;
    color: #edf5fb;
    border: 1px solid #3d5e7a;
    border-radius: 8px;
    padding: 4px 8px;
    min-height: 26px;
}
QWidget#sentryV2Root QPushButton:hover {
    background-color: #2c4862;
    border-color: #66a3cf;
}
QWidget#sentryV2Root QPushButton:pressed {
    background-color: #1c3042;
}
QWidget#sentryV2Root QPushButton:checked {
    background-color: #1f6c72;
    border-color: #39b0ba;
    color: #f6fffb;
}
QWidget#sentryV2Root QPushButton:disabled {
    background-color: #1a2430;
    color: #6f7d8a;
    border-color: #2f3f50;
}
QWidget#sentryV2Root QPushButton[buttonRole="primary"] {
    background-color: #1c4f78;
    border-color: #2f7fb9;
    color: #f5fbff;
    font-weight: 700;
}
QWidget#sentryV2Root QPushButton[buttonRole="primary"]:hover {
    background-color: #23608f;
    border-color: #4c97cc;
}
QWidget#sentryV2Root QPushButton[buttonRole="primary"]:pressed {
    background-color: #173f5f;
}
QWidget#sentryV2Root QPushButton[buttonRole="preset"] {
    background-color: #24364a;
    border-color: #41627f;
    color: #f0f7fc;
    font-weight: 600;
    padding: 5px 8px;
    min-height: 30px;
}
QWidget#sentryV2Root QPushButton[buttonRole="preset"]:hover {
    background-color: #2b4259;
    border-color: #5c85a8;
}
QWidget#sentryV2Root QPushButton[buttonRole="utility"] {
    background-color: #1e2b38;
    border-color: #31495f;
    color: #dce7f2;
}
QWidget#sentryV2Root QPushButton[buttonRole="utility"]:hover {
    background-color: #243545;
    border-color: #44627e;
}
QWidget#sentryV2Root QPushButton[buttonRole="dpad"] {
    background-color: #2a3d52;
    border: 1px solid #5b84aa;
    border-radius: 12px;
    color: #f4fbff;
    font-weight: 700;
    font-size: 15px;
    min-height: 40px;
    padding: 6px 8px;
}
QWidget#sentryV2Root QPushButton[buttonRole="dpad"]:hover {
    background-color: #334b64;
    border-color: #79a8d4;
}
QWidget#sentryV2Root QPushButton[buttonRole="dpad"]:pressed {
    background-color: #223446;
    border-color: #4f7599;
}
QWidget#sentryV2Root QPushButton[buttonRole="mode"] {
    background-color: #234033;
    border-color: #366a53;
    color: #eefbf4;
    font-weight: 600;
}
QWidget#sentryV2Root QPushButton[buttonRole="mode"]:hover {
    background-color: #2b4c3e;
    border-color: #4d8569;
}
QWidget#sentryV2Root QPushButton[buttonRole="danger"] {
    background-color: #5a2a2a;
    border-color: #a54a4a;
    color: #fff8f8;
    font-weight: 700;
}
QWidget#sentryV2Root QPushButton[buttonRole="danger"]:hover {
    background-color: #703232;
    border-color: #c85b5b;
}
QWidget#sentryV2Root QPushButton[buttonRole="danger"]:pressed {
    background-color: #472020;
}
QWidget#sentryV2Root QLineEdit,
QWidget#sentryV2Root QComboBox,
QWidget#sentryV2Root QSpinBox,
QWidget#sentryV2Root QDoubleSpinBox,
QWidget#sentryV2Root QListWidget,
QWidget#sentryV2Root QTextEdit {
    background-color: #0c1117;
    color: #eef5fb;
    border: 1px solid #31404e;
    border-radius: 8px;
    padding: 5px 7px;
    selection-background-color: #2b8a6e;
    selection-color: #ffffff;
}
QWidget#sentryV2Root QLineEdit:focus,
QWidget#sentryV2Root QComboBox:focus,
QWidget#sentryV2Root QSpinBox:focus,
QWidget#sentryV2Root QDoubleSpinBox:focus,
QWidget#sentryV2Root QListWidget:focus,
QWidget#sentryV2Root QTextEdit:focus {
    border-color: #5da6d8;
}
QWidget#sentryV2Root QComboBox::drop-down {
    border: none;
    width: 22px;
}
QWidget#sentryV2Root QAbstractItemView {
    background-color: #10171e;
    color: #eef5fb;
    border: 1px solid #31404e;
    selection-background-color: #2b8a6e;
}
QWidget#sentryV2Root QCheckBox {
    spacing: 8px;
}
QWidget#sentryV2Root QCheckBox::indicator {
    width: 16px;
    height: 16px;
    border-radius: 4px;
    border: 1px solid #4d6277;
    background-color: #0c1117;
}
QWidget#sentryV2Root QCheckBox::indicator:checked {
    background-color: #35b8c3;
    border-color: #35b8c3;
}
QWidget#sentryV2Root QSlider::groove:horizontal {
    height: 6px;
    border-radius: 3px;
    background-color: #243140;
}
QWidget#sentryV2Root QSlider::handle:horizontal {
    width: 16px;
    margin: -5px 0;
    border-radius: 8px;
    background-color: #78c8ff;
    border: 1px solid #a5dafd;
}
QWidget#sentryV2Root QScrollBar:vertical {
    background-color: #121922;
    width: 12px;
    margin: 2px;
}
QWidget#sentryV2Root QScrollBar::handle:vertical {
    background-color: #395169;
    border-radius: 6px;
    min-height: 24px;
}
QWidget#sentryV2Root QScrollBar:horizontal {
    background-color: #121922;
    height: 12px;
    margin: 2px;
}
QWidget#sentryV2Root QScrollBar::handle:horizontal {
    background-color: #395169;
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
    background-color: #0b1016;
    color: #6f7d8a;
    border: 1px solid #2a3745;
    border-radius: 12px;
}
QTextEdit#sentryV2Log {
    background-color: #0f1721;
    border: 1px solid #33485f;
}
"""

SENTRY_V2_STANDALONE_THEME = """
QMainWindow {
    background-color: #0f141a;
    color: #e6edf3;
}
QToolTip {
    background-color: #fff6c4;
    color: #101820;
    border: 1px solid #85754e;
    padding: 4px 6px;
}
"""


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

    # Signals for main app integration.
    turret_move_requested = pyqtSignal(float, float)
    fire_requested = pyqtSignal(int)
    manual_move_requested = pyqtSignal(int, int)
    manual_fire_requested = pyqtSignal(int)
    connection_operation_finished = pyqtSignal(str, bool, str, object, str)
    detection_result_ready = pyqtSignal(object, object)
    command_result_ready = pyqtSignal(str, bool, str)
    sentry_enabled_changed = pyqtSignal(bool)
    detection_mode_changed = pyqtSignal(int)
    color_preset_changed = pyqtSignal(str)
    pir_event_received = pyqtSignal(int, float)
    # Thread-safe camera open result signals (emitted from bg thread, handled on main thread)
    _cam_bg_opened = pyqtSignal(object, str, str, int, int, bool)   # cap, src_text, kind, rw, rh, rfs
    _cam_bg_failed = pyqtSignal(str)                                 # src_text
    _cam_url_error = pyqtSignal(str)                                 # error message from URL-open bg thread
    _cam_url_ready = pyqtSignal(str, str, int, int, int)             # display_label, source_text, w, h, gen
    _cam_url_status = pyqtSignal(str)                                # live status text from URL-open bg thread
    _yolo_load_result = pyqtSignal(bool, str, str)                   # ok, model_name, error_text

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.setObjectName("sentryV2Root")
        self.setMinimumWidth(SENTRY_V2_WIDGET_MIN_WIDTH)

        # Config (try loading saved, else defaults)
        self.config = self._load_settings_config()

        # Standalone communication
        self._comm = SentryV2Comm()
        self._comm.invert_pan = self.config.connection.invert_pan
        self._comm.invert_tilt = self.config.connection.invert_tilt
        self._comm.trigger_mode_bb = self.config.engagement.trigger_mode_bb
        self._comm.set_on_pir_event(self._emit_comm_pir_event)

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
        self._laser_on = False
        self._acc_on = False
        self._spare_on = False
        self._safety_armed = False

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
        self._camera_recovery_attempts: int = 0
        self._MAX_CAMERA_RECOVERY_ATTEMPTS: int = 2
        self._camera_recovery_in_progress: bool = False
        self._startup_retry_count: int = -1  # tracks auto-open retries
        # Wire thread-safe camera open result signals
        self._cam_bg_opened.connect(self._finish_camera_open)
        self._cam_bg_failed.connect(self._on_camera_open_failed)
        self._cam_url_error.connect(self._on_url_open_error)
        self._cam_url_ready.connect(self._on_url_ready)
        self._cam_url_status.connect(self._on_url_status_update)
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
        self._last_blocked_mask_seen: str = ""
        self._last_mask_trace_snapshot: str = ""
        self._last_scope_view_active: bool = False
        self._last_detected_objects: List[DetectedObject] = []
        self._last_display_frame: Optional[np.ndarray] = None
        self._last_raw_frame: Optional[np.ndarray] = None
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
        self._connection_busy: bool = False
        self._comm_task_queue: "queue.Queue[object]" = queue.Queue()
        self._pending_move_lock = threading.Lock()
        self._pending_move_command: Optional[Tuple[float, float, int, int]] = None
        self._comm_worker_stop = threading.Event()
        self._comm_worker = threading.Thread(target=self._comm_worker_loop, name="sentry-v2-comm-worker", daemon=True)
        self._comm_worker.start()
        self._detector_frame_lock = threading.Lock()
        self._detector_pending_frame: Optional[np.ndarray] = None
        self._detector_worker_stop = threading.Event()
        self._detector_worker_busy: bool = False
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
        self._load_custom_master_profiles()
        self.connection_operation_finished.connect(self._on_connection_operation_finished)
        self.detection_result_ready.connect(self._on_detection_result_ready)
        self.command_result_ready.connect(self._on_command_result_ready)
        self.pir_event_received.connect(self._on_comm_pir_event_received)
        self._yolo_load_result.connect(self._on_yolo_load_result)
        self._yolo_loading: bool = False
        self._startup_autoconnect_active: bool = False
        self._startup_autoconnect_retry: int = 0

        # Build UI
        self._build_ui()
        self._apply_theme()

        # Status refresh timer
        self._status_timer = QTimer(self)
        self._status_timer.timeout.connect(self._refresh_status)
        self._status_timer.start(500)
        self._schedule_startup_tasks()

    def _load_settings_config(self) -> SentryV2Config:
        """Load settings from the canonical path and only fall back to legacy once if needed."""
        canonical = SENTRY_V2_SETTINGS_PATH
        legacy = LEGACY_SENTRY_V2_SETTINGS_PATH

        selected = canonical if canonical.exists() else legacy

        cfg = SentryV2Config.load(str(selected))
        cfg.config_path = "app/config/sentry_v2_settings.json"
        prompted = Path(str(cfg.prompted_library_path or "app/config/sentry_v2_prompted_targets.json"))
        if prompted.is_absolute():
            cfg.prompted_library_path = self._portable_path_string(prompted)

        if selected == legacy and legacy.exists():
            try:
                cfg.save(str(canonical))
            except Exception as exc:
                print(f"[SENTRY_V2_TAB] Failed to migrate legacy settings to canonical path: {exc}", flush=True)

        return cfg

    def _portable_path_string(self, path_obj: Path) -> str:
        """Prefer repo-relative paths so settings stay portable across machines."""
        repo_root = self._repo_root_path().resolve()
        try:
            return path_obj.resolve().relative_to(repo_root).as_posix()
        except Exception:
            return str(path_obj)

    def _schedule_startup_tasks(self) -> None:
        """CHANGE WARNING: Startup work here couples camera bring-up, transport auto-connect, and YOLO warmup; keep expensive work deferred when quick startup is enabled."""
        if bool(getattr(self.config, "quick_startup_enabled", True)):
            self._log("Quick startup enabled: deferring auto camera open, auto-connect, and YOLO model load until requested.")
            return
        self._schedule_auto_yolo_load(1200)
        QTimer.singleShot(800, self._auto_open_camera_on_startup)
        QTimer.singleShot(1000, lambda: self._auto_connect_on_startup(0))

    def _auto_open_camera_on_startup(self, _retry: int = 0) -> None:
        self._log(f"[CAM-DEBUG] _auto_open_camera_on_startup called: retry={_retry}, closing={self._closing}, has_source={self._has_local_source()}")
        if self._closing or self._has_local_source():
            return
        self._startup_retry_count = _retry
        try:
            self._toggle_camera()
        except Exception as exc:
            self._lbl_cam_status.setText(f"Auto-open failed: {exc}")
            self._lbl_cam_status.setStyleSheet("color: #cc3333; font-size: 10px;")
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

    def cleanup(self) -> None:
        """Stop timers and release all resources. Safe to call multiple times."""
        if self._cleanup_started:
            return
        self._cleanup_started = True
        self._closing = True
        self._comm_worker_stop.set()
        self._detector_worker_stop.set()
        with self._pending_move_lock:
            self._pending_move_command = None
        with self._detector_frame_lock:
            self._detector_pending_frame = None
        try:
            self._comm_task_queue.put_nowait(None)
        except Exception:
            pass
        self._cam_timer.stop()
        self._burst_timer.stop()
        self._status_timer.stop()
        try:
            self.engine.stop()
        except Exception:
            pass
        self._stop_fire_burst(send_release=False)
        self._close_camera()
        self._comm.disconnect()

    def closeEvent(self, event):
        """Release camera and serial on close."""
        self._closing = True
        try:
            if event is not None:
                event.accept()
        except Exception:
            pass
        QTimer.singleShot(0, self.cleanup)
        super().closeEvent(event)

    # ================================================================== #
    #  UI Construction
    # ================================================================== #

    def _build_ui(self) -> None:
        root = QVBoxLayout(self)
        root.setContentsMargins(4, 4, 4, 4)
        # CHANGE WARNING: Keep settings tab pages horizontally ignorable so hidden page size hints do not force the right pane wider than the visible viewport.

        self._main_splitter = QSplitter(Qt.Horizontal)
        self._main_splitter.setChildrenCollapsible(False)
        self._main_splitter.setHandleWidth(8)
        self._main_splitter.splitterMoved.connect(self._on_main_splitter_moved)

        self._layout_splitter = QSplitter(Qt.Vertical)
        self._layout_splitter.setChildrenCollapsible(False)
        self._layout_splitter.setHandleWidth(8)

        # --- Left: video feed ---
        self._video_label = SentryV2VideoCanvas("Waiting for video...")
        self._video_label.setObjectName("sentryV2Video")
        self._video_label.setAlignment(Qt.AlignCenter)
        self._video_label.setMinimumSize(SENTRY_V2_VIDEO_MIN_WIDTH, 180)
        self._video_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self._video_label.setStyleSheet("background-color: #0b1016; color: #6f7d8a;")
        logo_path = Path(__file__).resolve().parents[1] / "LOGO.png"
        if logo_path.is_file():
            self._video_label.set_placeholder_pixmap(QPixmap(str(logo_path)))
            self._video_label.set_placeholder_text("Camera Off\nOpen Camera to Start")
            self._video_label.set_placeholder_enabled(False)
        self._video_label.frameClicked.connect(self._on_video_frame_clicked)
        self._video_label.frameRightClicked.connect(self._on_video_frame_right_clicked)
        self._video_label.roiSelected.connect(self._on_video_roi_selected)

        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(0)
        self._layout_splitter.addWidget(self._video_label)
        self._layout_splitter.addWidget(self._build_log_group())
        self._layout_splitter.setStretchFactor(0, 6)
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
        pinned_top_layout.setContentsMargins(8, 4, 8, 4)
        pinned_top_layout.setSpacing(4)

        # Enable toggle
        self._chk_enable = QCheckBox("Enable Smart Sentry")
        self._chk_enable.setStyleSheet("font-weight: bold; font-size: 13px;")
        self._chk_enable.toggled.connect(self._on_enable_toggled)
        pinned_top_layout.addWidget(self._chk_enable)

        # Show video feed toggle
        self._chk_show_video = QCheckBox("Show Video Feed")
        self._chk_show_video.setChecked(True)
        self._chk_show_video.toggled.connect(self._on_show_video_toggled)
        self._chk_show_video.setToolTip("Toggle video display on/off (detection continues running)")
        pinned_top_layout.addWidget(self._chk_show_video)

        panel_layout.addWidget(pinned_top)

        # Sub-tabs for settings categories
        self._settings_tabs = QTabWidget()
        self._settings_tabs.setTabPosition(QTabWidget.West)
        self._settings_tabs.setUsesScrollButtons(False)
        self._settings_tabs.tabBar().setExpanding(False)
        self._settings_tabs.tabBar().setElideMode(Qt.ElideNone)
        self._settings_tabs.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)

        self._settings_tabs.addTab(self._wrap_settings_tab(self._build_connection_tab()), "Connection")
        self._settings_tabs.addTab(self._wrap_settings_tab(self._build_master_profiles_tab()), "Master Profiles")
        self._settings_tabs.addTab(self._wrap_settings_tab(self._build_detection_tab()), "Detection")
        self._settings_tabs.addTab(self._wrap_settings_tab(self._build_prompted_targets_tab()), "Prompted Targets")
        self._settings_tabs.addTab(self._wrap_settings_tab(self._build_filter_tab()), "Target Filter")
        self._settings_tabs.addTab(self._wrap_settings_tab(self._build_scoring_tab()), "Threat AI")
        self._settings_tabs.addTab(self._wrap_settings_tab(self._build_engagement_tab()), "Engage")
        self._settings_tabs.addTab(self._wrap_settings_tab(self._build_guard_tab()), "Guard")
        self._settings_tabs.addTab(self._wrap_settings_tab(self._build_controls_tab()), "Controls")
        for index in range(self._settings_tabs.count()):
            page = self._settings_tabs.widget(index)
            if page is not None:
                page.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        self._apply_settings_tab_colors()

        panel_layout.addWidget(self._settings_tabs, stretch=1)

        right_panel = QWidget()
        right_panel.setMinimumWidth(SENTRY_V2_PANEL_MIN_WIDTH)
        right_panel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(6)
        right_layout.addLayout(panel_layout, stretch=1)

        pinned_bottom = QWidget()
        pinned_bottom.setObjectName("sentryV2PinnedBottom")
        pinned_bottom_layout = QVBoxLayout(pinned_bottom)
        pinned_bottom_layout.setContentsMargins(0, 0, 0, 0)
        pinned_bottom_layout.setSpacing(4)
        pinned_bottom_layout.addWidget(self._build_status_group())
        right_layout.addWidget(pinned_bottom)

        self._main_splitter.addWidget(right_panel)
        self._main_splitter.setStretchFactor(0, 3)
        self._main_splitter.setStretchFactor(1, 0)

        root.addWidget(self._main_splitter)

        QTimer.singleShot(0, self._apply_default_panel_width)
        QTimer.singleShot(0, self._apply_saved_log_panel_height)
        QTimer.singleShot(0, self._reflow_all_responsive_button_grids)

        self._apply_all_tooltips()
        self._disable_wheel_scroll_on_all_inputs()


    def _apply_theme(self) -> None:
        self.setStyleSheet(SENTRY_V2_THEME)

    def _apply_settings_tab_colors(self) -> None:
        if not hasattr(self, "_settings_tabs") or self._settings_tabs is None:
            return
        tab_bar = self._settings_tabs.tabBar()
        tab_bar.setIconSize(QPixmap(10, 10).size())
        tab_colors = [
            "#8cc4ff",  # Connection
            "#a9f1c0",  # Master Profiles
            "#f5d27a",  # Detection
            "#f7b48a",  # Prompted Targets
            "#d7b3ff",  # Target Filter
            "#9fd8ff",  # Threat AI
            "#ffb7cf",  # Engage
            "#9fe3d3",  # Guard
            "#c6d2e3",  # Controls
        ]
        for idx, color in enumerate(tab_colors):
            if idx < tab_bar.count():
                tab_bar.setTabTextColor(idx, QColor(color))
                marker = QPixmap(10, 10)
                marker.fill(QColor(color))
                tab_bar.setTabIcon(idx, QIcon(marker))

    def _wrap_settings_tab(self, content: QWidget) -> QScrollArea:
        content.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        scroll = QScrollArea()
        scroll.setFrameShape(QFrame.NoFrame)
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
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
        self._reflow_all_responsive_button_grids()

    def _on_main_splitter_moved(self, _pos: int, _index: int) -> None:
        self._reflow_all_responsive_button_grids()

    def _sync_settings_panel_width(self) -> None:
        return

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
        return 1 if available_width < 430 else 2

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

        self._master_profiles_grid = QGridLayout()
        preset_lay.addLayout(self._master_profiles_grid)
        self._rebuild_master_profile_buttons()

        self._lbl_master_profile = QLabel("")
        self._lbl_master_profile.setWordWrap(True)
        self._lbl_master_profile.setStyleSheet("color: #999; font-size: 10px;")
        preset_lay.addWidget(self._lbl_master_profile)
        lay.addWidget(preset_grp)

        save_grp = QGroupBox("Manage Custom Presets")
        save_lay = QVBoxLayout(save_grp)

        select_row = QHBoxLayout()
        select_row.addWidget(QLabel("Saved preset:"))
        self._combo_custom_master_profiles = QComboBox()
        self._combo_custom_master_profiles.currentIndexChanged.connect(self._on_custom_master_profile_selected)
        select_row.addWidget(self._combo_custom_master_profiles, 1)
        btn_use_active_custom = QPushButton("Use Active")
        self._set_button_role(btn_use_active_custom, "utility")
        btn_use_active_custom.clicked.connect(self._select_active_custom_master_profile_for_edit)
        select_row.addWidget(btn_use_active_custom)
        btn_new_custom = QPushButton("New")
        self._set_button_role(btn_new_custom, "utility")
        btn_new_custom.clicked.connect(self._clear_custom_master_profile_editor)
        select_row.addWidget(btn_new_custom)
        save_lay.addLayout(select_row)

        save_row = QHBoxLayout()
        save_row.addWidget(QLabel("Preset name:"))
        self._edit_custom_master_name = QLineEdit()
        self._edit_custom_master_name.setPlaceholderText("Example: Yellow Indoor Sniper")
        save_row.addWidget(self._edit_custom_master_name, 1)
        self._btn_update_custom_master = QPushButton("Update Selected")
        self._set_button_role(self._btn_update_custom_master, "utility")
        self._btn_update_custom_master.clicked.connect(self._update_selected_custom_master_profile)
        save_row.addWidget(self._btn_update_custom_master)
        btn_save_custom = QPushButton("Save As New")
        self._set_button_role(btn_save_custom, "utility")
        btn_save_custom.clicked.connect(self._save_new_custom_master_profile)
        save_row.addWidget(btn_save_custom)
        save_lay.addLayout(save_row)
        self._lbl_custom_master_info = QLabel(
            "Select a saved custom preset to edit/update it, or click New and enter a unique preset name to save the current stack as a new coordinated profile."
        )
        self._lbl_custom_master_info.setStyleSheet("color: #999; font-size: 10px;")
        self._lbl_custom_master_info.setWordWrap(True)
        save_lay.addWidget(self._lbl_custom_master_info)
        lay.addWidget(save_grp)

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
        self._rebuild_custom_master_profile_combo()
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
        test_zoom_row.addWidget(self._lbl_test_zoom)
        cam_lay.addLayout(test_zoom_row, 3, 1)

        lbl_live_section = QLabel("Live Camera")
        lbl_live_section.setStyleSheet("font-weight: bold; color: #cfe8ff; padding-top: 4px;")
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
        cam_lay.addLayout(live_action_row, 5, 0, 1, 2)

        lbl_media_section = QLabel("Media Inputs")
        lbl_media_section.setStyleSheet("font-weight: bold; color: #cfe8ff; padding-top: 4px;")
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
        lbl_playback_section.setStyleSheet("font-weight: bold; color: #cfe8ff; padding-top: 4px;")
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
        lbl_maintenance_section.setStyleSheet("font-weight: bold; color: #cfe8ff; padding-top: 4px;")
        cam_lay.addWidget(lbl_maintenance_section, 11, 0, 1, 2)

        cam_lay.addLayout(resolution_action_grid, 12, 0, 1, 2)

        self._lbl_cam_status = QLabel("Camera closed")
        self._lbl_cam_status.setStyleSheet("color: #888; font-size: 10px;")
        cam_lay.addWidget(self._lbl_cam_status, 13, 0, 1, 2)
        self._on_source_zoom_changed()
        self._update_test_media_controls()

        lay.addWidget(cam_grp)

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
        self._lbl_mode_hint.setStyleSheet("color: #aaa; font-size: 10px;")
        type_lay.addWidget(self._lbl_mode_hint)
        self._btn_wifi_pinout = QPushButton("WiFi Pinout")
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

        # Connect / disconnect
        btn_row = QHBoxLayout()
        self._btn_connect = QPushButton("Connect")
        self._set_button_role(self._btn_connect, "primary")
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
        preset_lay.addLayout(preset_row)

        self._lbl_detection_preset = QLabel("")
        self._lbl_detection_preset.setWordWrap(True)
        self._lbl_detection_preset.setStyleSheet("color: #999; font-size: 10px;")
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
        self._lbl_contour_ratio.setStyleSheet("color: #999; font-size: 10px;")
        contour_lay.addWidget(self._lbl_contour_ratio, 2, 0, 1, 2)

        lay.addWidget(self._grp_contour)

        # --- YOLO settings (modes 2,4,5,9,10) ---
        self._grp_yolo = QGroupBox("YOLO Settings")
        yolo_lay = QGridLayout(self._grp_yolo)

        yolo_lay.addWidget(QLabel("Model:"), 0, 0)
        self._combo_yolo_model = QComboBox()
        self._combo_yolo_model.setPlaceholderText("Select model...")
        self._scan_yolo_models()
        self._combo_yolo_model.currentIndexChanged.connect(self._on_yolo_model_selection_changed)
        self._apply_tooltip(self._combo_yolo_model, "yolo_model")
        yolo_lay.addWidget(self._combo_yolo_model, 0, 1)
        self._btn_load_yolo = QPushButton("Load")
        self._set_button_role(self._btn_load_yolo, "utility")
        self._btn_load_yolo.clicked.connect(self._load_yolo_model)
        self._apply_tooltip(self._btn_load_yolo, "load_yolo_model")
        yolo_lay.addWidget(self._btn_load_yolo, 0, 2)

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
        self._lbl_color_ratio.setStyleSheet("color: #999; font-size: 10px;")
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
        intro.setStyleSheet("color: #aaa; font-size: 11px;")
        lay.addWidget(intro)

        runtime_grp = QGroupBox("Prompted Runtime")
        runtime_lay = QVBoxLayout(runtime_grp)
        self._chk_prompted_enabled = QCheckBox("Enable Prompted Targets")
        self._chk_prompted_enabled.setChecked(bool(self.config.prompted_targets_enabled))
        self._chk_prompted_enabled.toggled.connect(self._on_prompted_settings_changed)
        runtime_lay.addWidget(self._chk_prompted_enabled)
        self._chk_prompted_auto_fire = QCheckBox("Allow Auto-Fire For Prompted Matches")
        self._chk_prompted_auto_fire.setChecked(bool(self.config.prompted_allow_auto_fire))
        self._chk_prompted_auto_fire.toggled.connect(self._on_prompted_settings_changed)
        runtime_lay.addWidget(self._chk_prompted_auto_fire)
        self._chk_prompted_append_selected = QCheckBox("Append imports to selected target")
        runtime_lay.addWidget(self._chk_prompted_append_selected)
        lay.addWidget(runtime_grp)

        naming_grp = QGroupBox("Target Naming")
        naming_lay = QHBoxLayout(naming_grp)
        naming_lay.addWidget(QLabel("Base name:"))
        self._edit_prompted_name = QLineEdit()
        self._edit_prompted_name.setPlaceholderText("Example: Yellow Drill")
        naming_lay.addWidget(self._edit_prompted_name, 1)
        lay.addWidget(naming_grp)

        import_grp = QGroupBox("Create Targets")
        import_lay = QGridLayout(import_grp)
        self._btn_prompted_live = QPushButton("Add From Live")
        self._set_button_role(self._btn_prompted_live, "primary")
        self._btn_prompted_live.clicked.connect(self._toggle_prompted_live_capture)
        import_lay.addWidget(self._btn_prompted_live, 0, 0)
        self._btn_prompted_image = QPushButton("Browse Image")
        self._set_button_role(self._btn_prompted_image, "utility")
        self._btn_prompted_image.clicked.connect(self._browse_prompted_image)
        import_lay.addWidget(self._btn_prompted_image, 0, 1)
        self._btn_prompted_video = QPushButton("Browse Video")
        self._set_button_role(self._btn_prompted_video, "utility")
        self._btn_prompted_video.clicked.connect(self._browse_prompted_video)
        import_lay.addWidget(self._btn_prompted_video, 0, 2)
        self._lbl_prompted_status = QLabel("")
        self._lbl_prompted_status.setWordWrap(True)
        self._lbl_prompted_status.setStyleSheet("color: #888; font-size: 10px;")
        import_lay.addWidget(self._lbl_prompted_status, 1, 0, 1, 3)
        lay.addWidget(import_grp)

        library_grp = QGroupBox("Prompted Target Library")
        library_lay = QVBoxLayout(library_grp)
        self._prompted_target_list = QListWidget()
        self._prompted_target_list.itemChanged.connect(self._on_prompted_target_item_changed)
        self._prompted_target_list.itemSelectionChanged.connect(self._on_prompted_target_selected)
        library_lay.addWidget(self._prompted_target_list)

        detail_grid = QGridLayout()
        detail_grid.addWidget(QLabel("Min score:"), 0, 0)
        self._spin_prompted_min_score = QDoubleSpinBox()
        self._spin_prompted_min_score.setDecimals(2)
        self._spin_prompted_min_score.setRange(0.05, 0.99)
        self._spin_prompted_min_score.setSingleStep(0.01)
        self._spin_prompted_min_score.valueChanged.connect(self._on_prompted_profile_settings_changed)
        detail_grid.addWidget(self._spin_prompted_min_score, 0, 1)

        detail_grid.addWidget(QLabel("Confirm hits:"), 0, 2)
        self._spin_prompted_confirm_hits = QSpinBox()
        self._spin_prompted_confirm_hits.setRange(1, 10)
        self._spin_prompted_confirm_hits.valueChanged.connect(self._on_prompted_profile_settings_changed)
        detail_grid.addWidget(self._spin_prompted_confirm_hits, 0, 3)

        detail_grid.addWidget(QLabel("Lost timeout:"), 1, 0)
        self._spin_prompted_lost_timeout = QDoubleSpinBox()
        self._spin_prompted_lost_timeout.setDecimals(2)
        self._spin_prompted_lost_timeout.setRange(0.10, 10.0)
        self._spin_prompted_lost_timeout.setSingleStep(0.10)
        self._spin_prompted_lost_timeout.valueChanged.connect(self._on_prompted_profile_settings_changed)
        detail_grid.addWidget(self._spin_prompted_lost_timeout, 1, 1)

        detail_grid.addWidget(QLabel("Search padding:"), 1, 2)
        self._spin_prompted_search_padding = QSpinBox()
        self._spin_prompted_search_padding.setRange(16, 512)
        self._spin_prompted_search_padding.setSingleStep(8)
        self._spin_prompted_search_padding.valueChanged.connect(self._on_prompted_profile_settings_changed)
        detail_grid.addWidget(self._spin_prompted_search_padding, 1, 3)

        detail_grid.addWidget(QLabel("Global scan every:"), 2, 0)
        self._spin_prompted_global_interval = QSpinBox()
        self._spin_prompted_global_interval.setRange(1, 30)
        self._spin_prompted_global_interval.valueChanged.connect(self._on_prompted_profile_settings_changed)
        detail_grid.addWidget(self._spin_prompted_global_interval, 2, 1)

        self._lbl_prompted_examples = QLabel("Examples: 0")
        detail_grid.addWidget(self._lbl_prompted_examples, 2, 2, 1, 2)
        library_lay.addLayout(detail_grid)

        button_row = QHBoxLayout()
        self._btn_prompted_rename = QPushButton("Rename")
        self._set_button_role(self._btn_prompted_rename, "utility")
        self._btn_prompted_rename.clicked.connect(self._rename_selected_prompted_target)
        button_row.addWidget(self._btn_prompted_rename)
        self._btn_prompted_remove_last_example = QPushButton("Remove Last")
        self._set_button_role(self._btn_prompted_remove_last_example, "utility")
        self._btn_prompted_remove_last_example.clicked.connect(self._remove_last_prompted_example)
        button_row.addWidget(self._btn_prompted_remove_last_example)
        self._btn_prompted_remove = QPushButton("Remove")
        self._set_button_role(self._btn_prompted_remove, "utility")
        self._btn_prompted_remove.clicked.connect(self._remove_selected_prompted_target)
        button_row.addWidget(self._btn_prompted_remove)
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
        self._lbl_filter_preset.setStyleSheet("color: #999; font-size: 10px;")
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

        self._style_button_row([btn_train], "primary")
        self._style_button_row([btn_save, btn_stats], "utility")
        self._style_button_row([btn_clear], "danger")

        ml_btn_lay.addStretch()
        
        lay.addLayout(ml_btn_lay)

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
        self._lbl_engagement_preset.setStyleSheet("color: #999; font-size: 10px;")
        preset_lay.addWidget(self._lbl_engagement_preset)
        lay.addWidget(preset_grp)

        # Auto-Trigger toggle (prominent)
        self._chk_auto_trigger = QCheckBox("Auto-Trigger")
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
        self._compact_combo_box(self._combo_trigger_mode, minimum_chars=16)
        self._combo_trigger_mode.addItems(["Water (MOSFET)", "Projectile (GPIO13 Servo)"])
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
        for preset_name, preset in AIM_LOCK_FIRE_GATE_PRESETS.items():
            btn = QPushButton(preset["label"])
            self._set_button_role(btn, "utility")
            self._apply_tooltip(btn, preset.get("tooltip_key", ""))
            btn.clicked.connect(lambda _checked=False, name=preset_name: self._apply_aim_lock_fire_gate_preset(name))
            preset_row.addWidget(btn)
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
        center_radius_row = QHBoxLayout()
        self._spin_center_fire_radius = QDoubleSpinBox()
        self._spin_center_fire_radius.setRange(0.02, 1.00)
        self._spin_center_fire_radius.setSingleStep(0.01)
        self._spin_center_fire_radius.setDecimals(3)
        self._spin_center_fire_radius.setValue(
            max(0.02, min(1.0, (self.config.engagement.fire_trigger_enter_pan_tolerance + self.config.engagement.fire_trigger_enter_tilt_tolerance) * 0.5))
        )
        center_radius_row.addWidget(self._spin_center_fire_radius)
        btn_apply_center_radius = QPushButton("Apply Radius")
        self._set_button_role(btn_apply_center_radius, "utility")
        btn_apply_center_radius.clicked.connect(self._on_apply_center_fire_radius)
        center_radius_row.addWidget(btn_apply_center_radius)

        btn_sniper_small = QPushButton("Sniper Small")
        self._set_button_role(btn_sniper_small, "utility")
        btn_sniper_small.clicked.connect(lambda _checked=False: self._apply_sniper_center_radius_profile("small"))
        center_radius_row.addWidget(btn_sniper_small)

        btn_sniper_medium = QPushButton("Sniper Medium")
        self._set_button_role(btn_sniper_medium, "utility")
        btn_sniper_medium.clicked.connect(lambda _checked=False: self._apply_sniper_center_radius_profile("medium"))
        center_radius_row.addWidget(btn_sniper_medium)

        btn_sniper_large = QPushButton("Sniper Large")
        self._set_button_role(btn_sniper_large, "utility")
        btn_sniper_large.clicked.connect(lambda _checked=False: self._apply_sniper_center_radius_profile("large"))
        center_radius_row.addWidget(btn_sniper_large)
        self._style_button_row([btn_apply_center_radius, btn_sniper_small, btn_sniper_medium, btn_sniper_large], "utility")
        advanced_lay.addLayout(center_radius_row, 6, 1)

        self._lbl_center_fire_radius_hint = QLabel("")
        self._lbl_center_fire_radius_hint.setStyleSheet("color: #999; font-size: 10px;")
        self._lbl_center_fire_radius_hint.setWordWrap(True)
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
        btn2 = QPushButton("Set As Guard")
        self._set_button_role(btn2, "utility")
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
        scope_lay.addWidget(self._chk_scope_view)

        scope_radius_row = QHBoxLayout()
        scope_radius_row.addWidget(QLabel("Scope radius (%):"))
        self._spin_scope_radius = QSpinBox()
        self._spin_scope_radius.setRange(20, 60)
        self._spin_scope_radius.setSingleStep(1)
        self._spin_scope_radius.setValue(int(self.config.scope_radius_pct))
        self._spin_scope_radius.valueChanged.connect(self._on_scope_view_changed)
        scope_radius_row.addWidget(self._spin_scope_radius)
        scope_lay.addLayout(scope_radius_row)

        scope_vignette_row = QHBoxLayout()
        scope_vignette_row.addWidget(QLabel("Vignette opacity (%):"))
        self._spin_scope_vignette = QSpinBox()
        self._spin_scope_vignette.setRange(0, 100)
        self._spin_scope_vignette.setSingleStep(5)
        self._spin_scope_vignette.setValue(int(self.config.scope_vignette_opacity))
        self._spin_scope_vignette.valueChanged.connect(self._on_scope_view_changed)
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
        name_row.addWidget(self._edit_mask_name)
        mask_lay.addLayout(name_row)

        self._btn_mask_capture = QPushButton("Capture From Video")
        self._btn_mask_capture.setCheckable(True)
        self._set_button_role(self._btn_mask_capture, "mode")
        self._btn_mask_capture.toggled.connect(self._on_mask_capture_toggled)
        mask_lay.addWidget(self._btn_mask_capture)

        draft_row = QHBoxLayout()
        self._btn_mask_finish = QPushButton("Finish Mask")
        self._set_button_role(self._btn_mask_finish, "utility")
        self._btn_mask_finish.clicked.connect(self._finish_no_fire_mask)
        draft_row.addWidget(self._btn_mask_finish)
        self._btn_mask_undo = QPushButton("Undo Vertex")
        self._set_button_role(self._btn_mask_undo, "utility")
        self._btn_mask_undo.clicked.connect(self._undo_no_fire_mask_vertex)
        draft_row.addWidget(self._btn_mask_undo)
        self._btn_mask_clear = QPushButton("Clear Draft")
        self._set_button_role(self._btn_mask_clear, "danger")
        self._btn_mask_clear.clicked.connect(self._clear_no_fire_mask_draft)
        draft_row.addWidget(self._btn_mask_clear)
        mask_lay.addLayout(draft_row)

        self._lbl_mask_draft = QLabel("Draft: 0 vertices")
        mask_lay.addWidget(self._lbl_mask_draft)

        self._mask_list = QListWidget()
        self._mask_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self._mask_list.setMaximumHeight(120)
        mask_lay.addWidget(self._mask_list)

        manage_row = QHBoxLayout()
        self._btn_mask_toggle = QPushButton("Toggle Selected")
        self._set_button_role(self._btn_mask_toggle, "utility")
        self._btn_mask_toggle.clicked.connect(self._toggle_selected_no_fire_masks)
        manage_row.addWidget(self._btn_mask_toggle)
        self._btn_mask_remove = QPushButton("Remove Selected")
        self._set_button_role(self._btn_mask_remove, "danger")
        self._btn_mask_remove.clicked.connect(self._remove_selected_no_fire_masks)
        manage_row.addWidget(self._btn_mask_remove)
        mask_lay.addLayout(manage_row)

        self._chk_show_no_fire_masks = QCheckBox("Show no-fire masks")
        self._chk_show_no_fire_masks.setChecked(self.config.show_no_fire_masks)
        self._chk_show_no_fire_masks.toggled.connect(self._on_overlay_changed)
        mask_lay.addWidget(self._chk_show_no_fire_masks)

        self._chk_mask_trace = QCheckBox("Trace mask diagnostics")
        self._chk_mask_trace.setChecked(False)
        mask_lay.addWidget(self._chk_mask_trace)

        self._btn_mask_trace_dump = QPushButton("Dump Snapshot")
        self._set_button_role(self._btn_mask_trace_dump, "utility")
        self._btn_mask_trace_dump.clicked.connect(self._dump_mask_trace_snapshot)
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

        pir_hint = QLabel(
            "For roughly 120° physical spacing, keep one sensor as the active owner of a target crossing adjacent PIR cones. "
            "The lockout below suppresses near-simultaneous cross-sensor overlap in software."
        )
        pir_hint.setWordWrap(True)
        pir_hint.setStyleSheet("color: #97a8b8; font-size: 10px;")
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
        lay.addWidget(self._chk_guard_crosshair)

        self._refresh_no_fire_mask_list()
        self._update_mask_editor_ui()

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
        motion_note.setStyleSheet("color: #97a8b8; font-size: 10px;")
        dpad_lay.addWidget(motion_note)

        # D-pad grid
        grid = QGridLayout()
        grid.setHorizontalSpacing(4)
        grid.setVerticalSpacing(4)
        btn_up = QPushButton("\u25B2")  # up arrow
        btn_up.setFixedSize(66, 54)
        self._set_button_role(btn_up, "dpad")
        btn_up.clicked.connect(lambda: self._manual_move(0, 1))
        self._apply_tooltip(btn_up, "manual_up")
        grid.addWidget(btn_up, 0, 1)

        btn_left = QPushButton("\u25C0")  # left arrow
        btn_left.setFixedSize(66, 54)
        self._set_button_role(btn_left, "dpad")
        btn_left.clicked.connect(lambda: self._manual_move(-1, 0))
        self._apply_tooltip(btn_left, "manual_left")
        grid.addWidget(btn_left, 1, 0)

        btn_home = QPushButton("HOME")
        btn_home.setFixedSize(84, 62)
        self._set_button_role(btn_home, "dpad")
        btn_home.setStyleSheet("font-size: 11px; letter-spacing: 0.5px;")
        self._apply_tooltip(btn_home, "manual_home")
        btn_home.clicked.connect(self._on_home_clicked)
        grid.addWidget(btn_home, 1, 1)

        btn_right = QPushButton("\u25B6")  # right arrow
        btn_right.setFixedSize(66, 54)
        self._set_button_role(btn_right, "dpad")
        btn_right.clicked.connect(lambda: self._manual_move(1, 0))
        self._apply_tooltip(btn_right, "manual_right")
        grid.addWidget(btn_right, 1, 2)

        btn_down = QPushButton("\u25BC")  # down arrow
        btn_down.setFixedSize(66, 54)
        self._set_button_role(btn_down, "dpad")
        btn_down.clicked.connect(lambda: self._manual_move(0, -1))
        self._apply_tooltip(btn_down, "manual_down")
        grid.addWidget(btn_down, 2, 1)

        dpad_lay.addLayout(grid)
        lay.addWidget(dpad_grp)

        # --- Accessories ---
        acc_grp = QGroupBox("Accessories")
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

        acc_note = QLabel("Accessories stay separate from arming and fire controls.")
        acc_note.setWordWrap(True)
        acc_note.setStyleSheet("color: #97a8b8; font-size: 10px;")
        acc_lay.addWidget(acc_note, 1, 1, 1, 2)

        lay.addWidget(acc_grp)

        # --- Safety and Manual Fire ---
        fire_grp = QGroupBox("Safety & Fire")
        fire_lay = QVBoxLayout(fire_grp)

        fire_note = QLabel("Arm Safety before using manual fire. Safety is isolated here so it is not visually mixed with ordinary accessory toggles.")
        fire_note.setWordWrap(True)
        fire_note.setStyleSheet("color: #c9d7e3; font-size: 10px;")
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

        lay.addWidget(fire_grp)

        lay.addStretch()
        return w

    # ------------------------------------------------------------------ #
    #  Status + Log Groups
    # ------------------------------------------------------------------ #

    def _build_status_group(self) -> QGroupBox:
        grp = QGroupBox("Status")
        lay = QVBoxLayout(grp)
        self._lbl_state = QLabel("State: PAUSED")
        self._lbl_state.setStyleSheet("font-weight: bold;")
        self._lbl_state.setWordWrap(True)
        lay.addWidget(self._lbl_state)

        self._lbl_stats = QLabel("Targets: 0 | Qualified: 0 | Engaged: 0")
        self._lbl_stats.setWordWrap(True)
        lay.addWidget(self._lbl_stats)

        self._lbl_angles = QLabel("Angles: Pan 0.0° [0..270] | Tilt 0.0° [0..110]")
        self._lbl_angles.setStyleSheet("font-weight: bold;")
        self._lbl_angles.setWordWrap(True)
        lay.addWidget(self._lbl_angles)

        self._lbl_angles_controls = QLabel("Current Commanded: Pan 0.0° | Tilt 0.0°")
        self._lbl_angles_controls.setStyleSheet("font-weight: bold;")
        self._lbl_angles_controls.setWordWrap(True)
        lay.addWidget(self._lbl_angles_controls)

        self._lbl_no_fire_status = QLabel("No-fire mask: clear")
        self._lbl_no_fire_status.setStyleSheet("font-weight: bold; color: #8fe3c4;")
        self._lbl_no_fire_status.setWordWrap(True)
        lay.addWidget(self._lbl_no_fire_status)

        self._lbl_recovery_status = QLabel("Recovery: idle")
        self._lbl_recovery_status.setStyleSheet("font-weight: bold; color: #97a8b8;")
        self._lbl_recovery_status.setWordWrap(True)
        lay.addWidget(self._lbl_recovery_status)

        # Save config button
        btn_save = QPushButton("Save")
        self._set_button_role(btn_save, "primary")
        btn_save.clicked.connect(self._save_config)
        self._apply_tooltip(btn_save, "save_settings")
        lay.addWidget(btn_save)

        return grp

    def _build_log_group(self) -> QGroupBox:
        grp = QGroupBox("Serial Output")
        grp.setMinimumHeight(110)
        grp.setMaximumHeight(220)

        lay = QVBoxLayout(grp)
        lay.setContentsMargins(8, 8, 8, 8)
        lay.setSpacing(6)

        self._log_text = QTextEdit()
        self._log_text.setObjectName("sentryV2Log")
        self._log_text.setReadOnly(True)
        self._log_text.setStyleSheet("font-size: 11px; font-family: Consolas, 'Courier New', monospace;")
        lay.addWidget(self._log_text, stretch=1)

        controls = QHBoxLayout()
        controls.addStretch(1)
        btn_clear = QPushButton("Clear")
        self._set_button_role(btn_clear, "utility")
        btn_clear.clicked.connect(self._log_text.clear)
        controls.addWidget(btn_clear)
        lay.addLayout(controls)

        return grp

    def _apply_saved_log_panel_height(self) -> None:
        if not hasattr(self, "_layout_splitter"):
            return
        total_height = max(1, self._layout_splitter.size().height())
        log_height = max(110, min(190, int(total_height * 0.18)))
        self._layout_splitter.setSizes([max(1, total_height - log_height), log_height])

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
        h, w_frame = frame.shape[:2]
        self._last_raw_frame = frame.copy()

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
        prompted_objects: List[DetectedObject] = []
        if bool(self.config.prompted_targets_enabled):
            prompted_objects = self._prompted_matcher.detect(frame, base_objects, now)
        det_objects = self._tracker.assign_tracks(base_objects + prompted_objects, now)

        # Run engine
        self.engine.update(det_objects, now)
        self._last_detected_objects = list(det_objects)

        # Copy frame so overlay drawing doesn't corrupt main app's buffer
        display = frame.copy()

        # Draw overlay
        display = self.overlay.draw(display, self.engine)
        if self._scope_view_active():
            display = self.overlay.apply_scope_view(display, self.engine)
        self._draw_no_fire_mask_draft(display)
        self._draw_color_gate_status(display, mode, use_internal_detector)
        self._last_display_frame = display.copy()

        # Update video label (only if show_video_feed is enabled)
        if self._show_video_feed:
            self._show_frame(display)
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
        if self._host_controls_hardware():
            self.fire_requested.emit(int(burst_count))
            self._log(f"FIRE! Burst: {burst_count}")
            return
        self._start_fire_burst(pan, tilt, burst_count, interval)
        self._log(f"FIRE! Burst: {burst_count}")

    def _on_engine_move(self, pan: float, tilt: float) -> None:
        move_delta = self._get_command_delta(pan, tilt)
        move_time_ms = self._get_tracking_move_time_ms(move_delta)
        self._last_tracking_move_time_ms = int(move_time_ms)
        if self._host_controls_hardware():
            self.turret_move_requested.emit(float(pan), float(tilt))
        else:
            self._queue_move_command(pan, tilt, move_time_ms=move_time_ms)
        self._remember_commanded_position(pan, tilt)
        suppression_s = self._get_tracking_motion_suppression_s(move_delta)
        self._last_tracking_suppression_s = float(suppression_s)
        if suppression_s > 0.0:
            self._suppress_motion_detection(suppression_s)

    def _on_engine_state_change(self, old: SentryV2State, new: SentryV2State) -> None:
        self._lbl_state.setText(f"State: {new.name}")
        self._log(f"State: {old.name} -> {new.name}")
        old_scope = self._scope_view_active_for_state(old)
        new_scope = self._scope_view_active_for_state(new)
        if old_scope != new_scope:
            self._last_scope_view_active = new_scope
            self._log("Scope view: ON (ENGAGING display mode)" if new_scope else "Scope view: OFF (normal video restored)")

    def _emit_comm_pir_event(self, sensor_id: int, timestamp: float) -> None:
        try:
            self.pir_event_received.emit(int(sensor_id), float(timestamp))
        except Exception as exc:
            if not self._closing:
                self._report_runtime_warning("PIR signal emit failed", exc)

    def _on_comm_pir_event_received(self, sensor_id: int, timestamp: float) -> None:
        self.engine.on_pir_sensor_fired(int(sensor_id), float(timestamp))
        if hasattr(self, "_lbl_pir_status"):
            self._update_pir_status_display()
        state_name = self.engine.state.name if self.engine else "?"
        self._log(f"PIR event: sensor {int(sensor_id)} (engine={state_name})")

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
        "No runtime USB — PC talks to ESP32 over WiFi, Debug Board stays on ESP32 UART2 (GPIO16/17).",
        "No USB cables — Primary ESP32 handles IO, Secondary ESP32 (Yahboom board) handles servos.",
    ]

    def _show_full_wifi_pinout(self) -> None:
        text = (
            "<div style='font-size:13px; line-height:1.35;'>"
            "<div style='font-weight:700; color:#0f1720; margin-bottom:8px;'>ESP32 DevKit v1 full WiFi runtime</div>"
            "<div style='margin-bottom:8px; color:#1e2936;'>"
            "PC to ESP32: WiFi/UDP only<br>"
            "Debug Board to ESP32: UART2"
            "</div>"
            "<table style='border-collapse:collapse; width:100%; margin-bottom:8px;'>"
            "<tr><td style='padding:3px 8px; font-weight:700; color:#0f1720;'>GPIO16</td><td style='padding:3px 8px; color:#1e2936;'>UART2 RX from Debug Board TX</td></tr>"
            "<tr><td style='padding:3px 8px; font-weight:700; color:#0f1720;'>GPIO17</td><td style='padding:3px 8px; color:#1e2936;'>UART2 TX to Debug Board RX</td></tr>"
            "</table>"
            "<div style='font-weight:700; color:#0f1720; margin:8px 0 4px 0;'>Accessory IO</div>"
            "<table style='border-collapse:collapse; width:100%; margin-bottom:8px;'>"
            "<tr><td style='padding:3px 8px; font-weight:700; color:#0f1720;'>GPIO27</td><td style='padding:3px 8px; color:#1e2936;'>Trigger MOSFET (Water)</td></tr>"
            "<tr><td style='padding:3px 8px; font-weight:700; color:#0f1720;'>GPIO13</td><td style='padding:3px 8px; color:#1e2936;'>Trigger Servo (Projectile)</td></tr>"
            "<tr><td style='padding:3px 8px; font-weight:700; color:#0f1720;'>GPIO32</td><td style='padding:3px 8px; color:#1e2936;'>LED Relay</td></tr>"
            "<tr><td style='padding:3px 8px; font-weight:700; color:#0f1720;'>GPIO33</td><td style='padding:3px 8px; color:#1e2936;'>Laser Relay</td></tr>"
            "<tr><td style='padding:3px 8px; font-weight:700; color:#0f1720;'>GPIO25</td><td style='padding:3px 8px; color:#1e2936;'>Accessory Relay (G token)</td></tr>"
            "<tr><td style='padding:3px 8px; font-weight:700; color:#0f1720;'>GPIO26</td><td style='padding:3px 8px; color:#1e2936;'>Spare Relay (A token)</td></tr>"
            "</table>"
            "<div style='font-weight:700; color:#0f1720; margin:8px 0 4px 0;'>PIR Sensors</div>"
            "<table style='border-collapse:collapse; width:100%; margin-bottom:8px;'>"
            "<tr><td style='padding:3px 8px; font-weight:700; color:#0f1720;'>GPIO35</td><td style='padding:3px 8px; color:#1e2936;'>PIR Sensor 0 (right zone, cue ~45°)</td></tr>"
            "<tr><td style='padding:3px 8px; font-weight:700; color:#0f1720;'>GPIO34</td><td style='padding:3px 8px; color:#1e2936;'>PIR Sensor 1 (front zone, cue ~135°)</td></tr>"
            "<tr><td style='padding:3px 8px; font-weight:700; color:#0f1720;'>GPIO39</td><td style='padding:3px 8px; color:#1e2936;'>PIR Sensor 2 (left zone, cue ~225°)</td></tr>"
            "</table>"
            "<div style='font-weight:700; color:#0f1720; margin:8px 0 4px 0;'>Current Sensors</div>"
            "<table style='border-collapse:collapse; width:100%; margin-bottom:8px;'>"
            "<tr><td style='padding:3px 8px; font-weight:700; color:#0f1720;'>GPIO36</td><td style='padding:3px 8px; color:#1e2936;'>Pan Current</td></tr>"
            "<tr><td style='padding:3px 8px; font-weight:700; color:#0f1720;'>GPIO39</td><td style='padding:3px 8px; color:#1e2936;'>Tilt Current (shared pin when PIR is not used)</td></tr>"
            "<tr><td style='padding:3px 8px; font-weight:700; color:#0f1720;'>GPIO34</td><td style='padding:3px 8px; color:#1e2936;'>Total Current (shared pin when PIR is not used)</td></tr>"
            "</table>"
            "<div style='color:#334155; margin-top:8px;'>"
            "ESP32 USB is still useful for flashing and bench diagnostics, but is not part of normal full-WiFi runtime control."
            "</div>"
            "</div>"
        )
        msg = QMessageBox(self)
        msg.setWindowTitle("ESP32 Full WiFi Pinout")
        msg.setIcon(QMessageBox.Information)
        msg.setTextFormat(Qt.RichText)
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setStyleSheet(
            "QMessageBox { background-color: #f7fafc; }"
            "QMessageBox QLabel { color: #0f1720; font-size: 13px; }"
            "QPushButton { min-width: 84px; padding: 6px 12px; background: #1f4e79; color: #ffffff; border-radius: 6px; }"
            "QPushButton:hover { background: #255f94; }"
        )
        msg.exec_()

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
            self._lbl_conn_status.setText("Host-managed by main app")
            self._lbl_conn_status.setStyleSheet("color: #33cc33; font-weight: bold;")
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
        self._lbl_conn_status.setText("Connecting..." if is_connect else "Disconnecting...")
        self._lbl_conn_status.setStyleSheet("color: #d0b060; font-weight: bold;")
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
                            self._comm.send_movement(
                                float(kwargs.get("initial_pan", 90.0)),
                                float(kwargs.get("initial_tilt", 50.0)),
                                move_time_ms=int(kwargs.get("initial_move_time_ms", 20)),
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
            self._lbl_conn_status.setText("Disconnected")
            self._lbl_conn_status.setStyleSheet("color: #cc3333; font-weight: bold;")
            self._log("Disconnected")
            self._startup_autoconnect_active = False
            self._startup_autoconnect_retry = 0
            return

        if ok:
            self._btn_connect.setText("Disconnect")
            self._lbl_conn_status.setText(self._format_connection_details(details, info))
            mode2_degraded_io = (
                int(self.config.connection.connection_type) == 2
                and (
                    getattr(self._comm, "_sock", None) is None
                    or getattr(self._comm, "_udp_target", None) is None
                )
            )
            self._lbl_conn_status.setStyleSheet(
                "color: #ffae42; font-weight: bold;" if mode2_degraded_io else "color: #33cc33; font-weight: bold;"
            )
            self._log(f"Connected: {info}")
            fire_mode = "Projectile (ESP32 GPIO13 Servo)" if self._comm.trigger_mode_bb else "Water (MOSFET)"
            safety_state = "ARMED" if self._safety_armed else "LOCKED"
            auto_trigger_state = "ON" if bool(self.config.engagement.auto_trigger_enabled) else "OFF"
            self._log(f"Fire config: mode={fire_mode} | safety={safety_state} | auto-trigger={auto_trigger_state}")
            if mode2_degraded_io:
                self._log(
                    "Connection warning: Debug Board pan/tilt movement is available, but ESP32 WiFi IO is unavailable. GPIO13 trigger-servo and PIR enable commands will not work until the WiFi link reconnects"
                )
            self._startup_autoconnect_active = False
            self._startup_autoconnect_retry = 0
            self._schedule_auto_yolo_load(300)
        else:
            self._btn_connect.setText("Connect")
            failure_text = self._format_connection_details(details, f"FAILED: {err or 'unknown error'}")
            self._lbl_conn_status.setText(failure_text)
            self._lbl_conn_status.setStyleSheet("color: #cc3333; font-weight: bold;")
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
            self._lbl_cam_status.setText("Camera source blank. Defaulting to standalone camera index 0.")
            self._lbl_cam_status.setStyleSheet("color: #888; font-size: 10px;")
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
                    self._lbl_cam_status.setText(
                        f"Camera index {src} is already reserved by the main app. Use another index or URL."
                    )
                    self._lbl_cam_status.setStyleSheet("color: #cc3333; font-size: 10px;")
                    self._log(f"Camera open blocked: index {src} is in use by main app")
                    return

        try:
            self._open_video_capture_source(src, src_text, "camera", request_frame_size=True)
        except Exception as e:
            self._lbl_cam_status.setText(f"Error: {e}")
            self._lbl_cam_status.setStyleSheet("color: #cc3333; font-size: 10px;")
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
            self._lbl_cam_status.setText("Video URL is blank")
            self._lbl_cam_status.setStyleSheet("color: #cc3333; font-size: 10px;")
            return
        # Close any existing source.  This also sets _url_stream_stop so any
        # in-flight worker for a previous URL will see it and exit.
        self._close_camera(log_close=False)
        self._video_label.set_placeholder_enabled(False)
        self._video_label.clear_frame("Opening URL\u2026")
        self._lbl_cam_status.setText("Resolving URL\u2026")
        self._lbl_cam_status.setStyleSheet("color: #aaaaaa; font-size: 10px;")
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
            self._lbl_cam_status.setText(f"Test media not found: {selected_path}")
            self._lbl_cam_status.setStyleSheet("color: #cc3333; font-size: 10px;")
            self._log(f"Test media open failed: {selected_path}")
            return

        image_suffixes = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}
        try:
            if media_path.suffix.lower() in image_suffixes:
                self._open_image_source(media_path)
            else:
                self._open_video_capture_source(str(media_path), str(media_path), "test_video", request_frame_size=False)
        except Exception as exc:
            self._lbl_cam_status.setText(f"Test media error: {exc}")
            self._lbl_cam_status.setStyleSheet("color: #cc3333; font-size: 10px;")
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
            self._lbl_cam_status.setText(f"Reopening camera at {width} x {height}...")
            self._lbl_cam_status.setStyleSheet("color: #d0b060; font-size: 10px;")
            self._close_camera(log_close=False)
            QTimer.singleShot(0, self._toggle_camera)
            self._log(f"Applying camera resolution by reopening local source: {width} x {height}")
            return

        self._lbl_cam_status.setText(
            f"Resolution saved: {width} x {height}. Use Restart App if the main/shared feed still shows the old size."
        )
        self._lbl_cam_status.setStyleSheet("color: #d0b060; font-size: 10px;")
        self._log(f"Camera resolution saved: {width} x {height}")

    def _restart_application(self) -> None:
        self._save_config()
        self._close_camera(log_close=False)
        repo_root = self._repo_root_path()
        args = list(sys.argv) if list(sys.argv) else [str((repo_root / "run.py").resolve())]

        process = QProcess(self)
        env = QProcessEnvironment.systemEnvironment()
        env.insert("DB3000_RELAUNCH_DELAY_MS", "1200")
        env.insert("DB3000_RELAUNCH_FROM_PID", str(os.getpid()))
        process.setProcessEnvironment(env)
        process.setWorkingDirectory(str(repo_root))
        started = process.startDetached(sys.executable, args)
        if isinstance(started, tuple):
            started = bool(started[0])
        if not started:
            self._lbl_cam_status.setText("Restart failed: unable to relaunch the app")
            self._lbl_cam_status.setStyleSheet("color: #cc3333; font-size: 10px;")
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
            self._lbl_cam_status.setText(f"Return to camera failed: {exc}")
            self._lbl_cam_status.setStyleSheet("color: #cc3333; font-size: 10px;")
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
        self._test_media_last_frame = frame.copy()
        effective_frame = self._apply_source_zoom(frame)
        if self._show_video_feed and self._detector_worker_busy:
            if self._last_display_frame is not None and self._last_display_frame.shape[:2] == effective_frame.shape[:2]:
                self._show_frame(self._last_display_frame)
            else:
                display = effective_frame.copy()
                display = self.overlay.draw(display, self.engine)
                if self._scope_view_active():
                    display = self.overlay.apply_scope_view(display, self.engine)
                self._draw_no_fire_mask_draft(display)
                self._draw_color_gate_status(display, self.config.detection_mode.detection_mode, False)
                self._show_frame(display)
        with self._detector_frame_lock:
            self._detector_pending_frame = effective_frame.copy()

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
            self._lbl_cam_status.setText("Test video paused at end of file")
            self._lbl_cam_status.setStyleSheet("color: #d0b060; font-size: 10px;")
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
        self._lbl_cam_status.setText(f"Test image: {media_path.name}  ({frame.shape[1]}x{frame.shape[0]})")
        self._lbl_cam_status.setStyleSheet("color: #33cc33; font-size: 10px;")
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
        self._close_camera(log_close=False)
        self._video_label.set_placeholder_enabled(False)
        self._video_label.clear_frame("Opening camera...")
        requested_w = int(self.config.connection.camera_width)
        requested_h = int(self.config.connection.camera_height)

        if isinstance(src, int):
            # Open integer-index cameras in a background thread so DSHOW/MSMF
            # driver init doesn't freeze the Qt event loop.
            self._lbl_cam_status.setText("Opening camera…")
            self._lbl_cam_status.setStyleSheet("color: #aaaaaa; font-size: 10px;")
            self._log(f"[CAM-DEBUG] Starting background open for index {src} ({requested_w}x{requested_h})")

            def _open_bg(
                _src=src, _src_text=source_text, _sk=source_kind,
                _rw=requested_w, _rh=requested_h, _rfs=request_frame_size,
            ) -> None:
                cap = None
                backends = (
                    (cv2.CAP_DSHOW, "DSHOW"),
                    (cv2.CAP_MSMF, "MSMF"),
                    (None, "DEFAULT"),
                ) if os.name == "nt" else ((None, "DEFAULT"),)
                for backend, bname in backends:
                    try:
                        c = cv2.VideoCapture(_src) if backend is None else cv2.VideoCapture(_src, backend)
                        time.sleep(0.5)  # let driver settle
                        if not c.isOpened():
                            print(f"[CAM-BG] index={_src} backend={bname} not opened", flush=True)
                            c.release()
                            continue
                        # Verify at least one readable frame — MSMF can report
                        # isOpened=True but then immediately fail on grabFrame
                        ok, _frame = c.read()
                        print(f"[CAM-BG] index={_src} backend={bname} opened=True read_ok={ok}", flush=True)
                        if ok:
                            cap = c
                            break
                        c.release()
                    except Exception as _e:
                        print(f"[CAM-BG] index={_src} backend={bname} exception: {_e}", flush=True)
                # Emit thread-safe signal back to main thread
                if cap is not None and cap.isOpened():
                    print(f"[CAM-BG] SUCCESS index={_src}, emitting opened signal", flush=True)
                    self._cam_bg_opened.emit(cap, _src_text, _sk, _rw, _rh, _rfs)
                else:
                    if cap is not None:
                        try:
                            cap.release()
                        except Exception:
                            pass
                    print(f"[CAM-BG] FAILED index={_src}, emitting failed signal", flush=True)
                    self._cam_bg_failed.emit(_src_text)

            threading.Thread(target=_open_bg, daemon=True, name="cam-open-bg").start()
        else:
            # URLs / file paths — open directly (rarely slow on startup)
            cap = cv2.VideoCapture(src)
            if not cap.isOpened():
                cap.release()
                raise RuntimeError(f"Failed to open: {source_text}")
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
        if request_frame_size:
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, requested_w)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, requested_h)

        actual_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        actual_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self._cap = cap
        self._local_source_kind = source_kind
        self._local_source_label = source_text
        self._test_media_image_frame = None
        self._test_media_last_frame = None
        self._test_media_paused = False
        self._grab_fail_count = 0
        self._camera_recovery_attempts = 0
        self._camera_recovery_in_progress = False
        self._cam_timer.start(33)
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
        self._lbl_cam_status.setText(f"{status_prefix}: {status_name}  ({status_resolution})")
        self._lbl_cam_status.setStyleSheet("color: #33cc33; font-size: 10px;")
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
                        first_frame = fr
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
                        with self._url_stream_frame_lock:
                            self._url_stream_frame = frame
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
        self._cam_timer.start(33)
        self._btn_cam.setText("Close Source")
        if w > 0 and h > 0:
            self._sync_source_dimensions(w, h)
        self._lbl_cam_status.setText(f"URL stream: {display_label}  ({w}x{h})")
        self._lbl_cam_status.setStyleSheet("color: #33cc33; font-size: 10px;")
        self._log(f"URL stream opened: {display_label} ({w}x{h})")
        self._update_test_media_controls()
        self._schedule_auto_yolo_load(300)
        print(f"[URL-MAIN] _on_url_ready: timer started, source_kind=url_stream", flush=True)

    def _on_url_status_update(self, msg: str) -> None:
        """Called on Qt main thread with live status text from the URL worker."""
        if self._closing:
            return
        self._lbl_cam_status.setText(msg)
        self._lbl_cam_status.setStyleSheet("color: #aaaaaa; font-size: 10px;")

    def _on_camera_open_failed(self, source_text: str) -> None:
        """Called on Qt main thread when the background camera open failed."""
        if self._closing:
            return
        retry = getattr(self, "_startup_retry_count", -1)
        self._log(f"Camera open failed: {source_text} (attempt {retry+1})")
        self._btn_cam.setText("Open Source")
        if retry >= 0 and not self._has_local_source() and retry < 3:
            # Retry with increasing back-off (1.5s, 3s, 4.5s)
            delay = 1500 * (retry + 1)
            self._lbl_cam_status.setText(f"Retrying camera ({retry+1}/3)…")
            self._lbl_cam_status.setStyleSheet("color: #d0a030; font-size: 10px;")
            QTimer.singleShot(delay, lambda r=retry+1: self._auto_open_camera_on_startup(r))
        else:
            self._startup_retry_count = -1
            self._lbl_cam_status.setText(f"Failed to open: {source_text}")
            self._lbl_cam_status.setStyleSheet("color: #cc3333; font-size: 10px;")

    def _on_url_open_error(self, msg: str) -> None:
        """Called on Qt main thread when the background URL resolve/open failed."""
        if self._closing:
            return
        self._lbl_cam_status.setText(f"Video URL error: {msg}")
        self._lbl_cam_status.setStyleSheet("color: #cc3333; font-size: 10px;")
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
        self._lbl_cam_status.setText(
            f"Camera stalled. Reopening source ({attempt}/{self._MAX_CAMERA_RECOVERY_ATTEMPTS})..."
        )
        self._lbl_cam_status.setStyleSheet("color: #d0b060; font-size: 10px;")
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
                self._lbl_cam_status.setText(f"Camera recovery failed: {exc}")
                self._lbl_cam_status.setStyleSheet("color: #cc3333; font-size: 10px;")
                self._log(f"Camera recovery failed ({attempt}/{self._MAX_CAMERA_RECOVERY_ATTEMPTS}): {exc}")

        QTimer.singleShot(250, _reopen)
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
            self._lbl_cam_status.setText("Source closed")
            self._lbl_cam_status.setStyleSheet("color: #888; font-size: 10px;")
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
        self._grab_fail_count = 0
        self._queue_local_frame(frame)

    def _detector_worker_loop(self) -> None:
        while not self._detector_worker_stop.is_set():
            frame = None
            with self._detector_frame_lock:
                if self._detector_pending_frame is not None:
                    frame = self._detector_pending_frame
                    self._detector_pending_frame = None
            if frame is None:
                time.sleep(0.01)
                continue
            try:
                self._detector_worker_busy = True
                mode = self.config.detection_mode.detection_mode
                raw_boxes = self._detector.detect(frame, mode)
                if not self._closing:
                    self.detection_result_ready.emit(frame, raw_boxes)
            except Exception as exc:
                # Store error locally — do NOT write to self._comm from this thread.
                self._last_detector_error = str(exc)
            finally:
                self._detector_worker_busy = False

    def _on_detection_result_ready(self, frame: object, raw_boxes: object) -> None:
        if self._closing:
            return
        try:
            if frame is None:
                return
            self.process_frame(frame, raw_boxes or [], _from_own_camera=True)
        except Exception as exc:
            self._log(f"Detection result error: {exc}")

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

    def _scan_yolo_models(self) -> None:
        """Populate the YOLO model combo from known YOLO model directories."""
        self._combo_yolo_model.clear()
        self._yolo_model_entries = self._discover_yolo_models()
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

    def _load_yolo_model(self) -> None:
        """Start a background-thread YOLO model load so the event loop never freezes."""
        model_name = self._combo_yolo_model.currentText().strip()
        model_path = self._combo_yolo_model.currentData()
        if not model_name or not model_path:
            self._set_yolo_status("error", "No model selected")
            return
        if self._yolo_loading:
            return  # already loading; ignore concurrent request
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
        if not model_name:
            return
        self.config.detection_mode.yolo_model_name = model_name
        if "Runtime ready:" not in self._lbl_yolo_status.text():
            self._set_yolo_status("info", f"Model selected: {model_name}")

    def _set_yolo_status(self, level: str, message: str) -> None:
        if not hasattr(self, "_lbl_yolo_status"):
            return
        level_key = (level or "info").lower().strip()
        style_map = {
            "ok": ("#33cc33", "OK"),
            "pending": ("#d0b060", "WAIT"),
            "error": ("#cc3333", "ERR"),
            "info": ("#8ea4b8", "INFO"),
        }
        color, badge = style_map.get(level_key, style_map["info"])
        self._lbl_yolo_status.setText(f"[{badge}] {message}")
        self._lbl_yolo_status.setStyleSheet(f"color: {color}; font-size: 10px; font-weight: 600;")
        self._lbl_yolo_status.setToolTip(message)

    def _repo_root_path(self) -> Path:
        return Path(__file__).resolve().parents[2]

    def _candidate_yolo_model_dirs(self) -> list[Path]:
        dirs: list[Path] = []
        for candidate in (
            self._repo_root_path() / "YOLO_MODELS",
            self._repo_root_path() / "app" / "YOLO_MODELS",
            self._repo_root_path() / "app" / "models",
            Path.cwd() / "YOLO_MODELS",
        ):
            resolved = candidate.resolve()
            if resolved not in dirs and resolved.is_dir():
                dirs.append(resolved)
        return dirs

    def _discover_yolo_models(self) -> list[tuple[str, str]]:
        supported_suffixes = {".pt", ".onnx", ".engine", ".torchscript"}
        discovered: dict[str, str] = {}
        for models_dir in self._candidate_yolo_model_dirs():
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
        self._log(f"YOLO classes: {classes}")

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

    def _on_ml_training_toggled(self, checked: bool) -> None:
        """Handle ML training mode toggle."""
        if self.engine:
            self.engine.set_ml_training_mode(checked)
            mode = "enabled" if checked else "disabled"
            self._log(f"ML training logging {mode}")

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

    def _clear_ml_logs(self) -> None:
        """Clear all logged engagement data."""
        if not self.engine:
            self._log("No engine running")
            return
        
        self.engine.get_ml_logger().clear()
        self._log("✓ Engagement logs cleared")

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

    def _apply_sniper_center_radius_profile(self, profile: str) -> None:
        radius = SNIPER_CENTER_RADIUS_PRESETS.get(profile)
        if radius is None:
            return
        self._spin_center_fire_radius.blockSignals(True)
        self._spin_center_fire_radius.setValue(float(radius))
        self._spin_center_fire_radius.blockSignals(False)
        self._on_apply_center_fire_radius()
        self._log(f"Sniper center profile applied: {profile} ({float(radius):.3f} deg)")

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
        pan_min, pan_max = sorted((g.pan_min, g.pan_max))
        tilt_min, tilt_max = sorted((g.tilt_min, g.tilt_max))
        g.guard_pan = min(pan_max, max(pan_min, g.guard_pan))
        g.guard_tilt = min(tilt_max, max(tilt_min, g.guard_tilt))
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
        self._push_config()
        self._refresh_status()

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

    def _on_pir_enabled_changed(self, checked: bool) -> None:
        """Handle master PIR enable/disable."""
        self.config.pir_guard.pir_enabled = bool(checked)
        self._push_config()
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
        pg.confirmation_timeout = self._spin_pir_confirm_timeout.value()
        pg.scan_on_no_detect = self._chk_pir_scan_enabled.isChecked()
        pg.cross_sensor_lockout_ms = int(self._spin_pir_cross_lockout_ms.value())
        self._push_config()

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
        self._spin_pir_scan_pan_range.setValue(20.0)
        self._spin_pir_scan_pan_range.blockSignals(False)
        self._spin_pir_scan_tilt_range.blockSignals(True)
        self._spin_pir_scan_tilt_range.setValue(12.0)
        self._spin_pir_scan_tilt_range.blockSignals(False)
        self._spin_pir_cross_lockout_ms.blockSignals(True)
        self._spin_pir_cross_lockout_ms.setValue(800)
        self._spin_pir_cross_lockout_ms.blockSignals(False)
        self._on_pir_settings_changed()
        self._log("Applied PIR 120° layout: cues=270/150/30, scan pan=20°, tilt=12°, cross-sensor lockout=800ms")

    def _on_pan_tilt_motion_toggled(self, checked: bool) -> None:
        self._pan_tilt_motion_enabled = bool(checked)
        self.engine.set_motion_enabled(self._pan_tilt_motion_enabled)
        self._btn_motion_enable.setText(
            "Auto Motion: ON" if self._pan_tilt_motion_enabled else "Auto Motion: OFF"
        )
        self._btn_motion_enable.setStyleSheet(
            "font-weight: bold; color: #66dd88;" if self._pan_tilt_motion_enabled else "font-weight: bold; color: #ffae42;"
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
            self._lbl_pir_status.setText("Status: Engine not ready")
            return
        mgr = self.engine._pir_manager
        status_text = mgr.get_status_text()
        queued = mgr.peek_queue_count()
        if queued > 0:
            status_text += f"  [{queued} sensor(s) pending]"
        self._lbl_pir_status.setText(f"Status: {status_text}")

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
        self._chk_auto_trigger.setStyleSheet(
            "font-weight: bold; color: #ff4d4d;" if checked else "font-weight: bold; color: #66dd88;"
        )
        if not self._applying_master_preset:
            self._set_master_profile_label(self._match_master_profile_name())
            self._update_master_stack_summary()
        self._push_config()
        self._save_config_quietly()
        self._log(f"Auto-trigger: {'ON' if checked else 'OFF'}")

    def _on_trigger_mode_changed(self, index: int) -> None:
        is_bb = (index == 1)
        self.config.engagement.trigger_mode_bb = is_bb
        self._comm.trigger_mode_bb = is_bb
        if self._host_controls_hardware():
            pass
        elif self._comm.is_connected():
            self._queue_comm_task("send_command",
                self.engine.current_pan,
                self.engine.current_tilt,
                fire=0,
                move_time_ms=self._get_manual_move_time_ms(),
            )
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

    def _manual_move(self, pan_dir: int, tilt_dir: int) -> None:
        step = self._spin_step.value()
        new_pan = self.engine.current_pan + pan_dir * step
        new_tilt = self.engine.current_tilt + tilt_dir * step
        new_pan, new_tilt = self._clamp_manual_angles(new_pan, new_tilt)
        self.engine.current_pan = new_pan
        self.engine.current_tilt = new_tilt
        if self._host_controls_hardware():
            self.manual_move_requested.emit(int(pan_dir * step), int(tilt_dir * step))
        else:
            self._queue_move_command(new_pan, new_tilt, move_time_ms=self._get_manual_move_time_ms(), manual_override=True)
        self._remember_commanded_position(new_pan, new_tilt)
        self._suppress_motion_detection()
        self._refresh_status()

    def _on_home_clicked(self) -> None:
        pan = self._spin_guard_pan.value()
        tilt = self._spin_guard_tilt.value()
        pan, tilt = self._clamp_manual_angles(pan, tilt)
        self.engine.hold_current_guard_position(pan, tilt)
        if self._host_controls_hardware():
            self.turret_move_requested.emit(float(pan), float(tilt))
        else:
            self._queue_move_command(pan, tilt, move_time_ms=self._get_manual_move_time_ms(), manual_override=True)
        self._remember_commanded_position(pan, tilt)
        self._suppress_motion_detection()
        self._refresh_status()
        self._log("Go Home")

    def _on_led_toggled(self, checked: bool) -> None:
        self._led_on = checked
        self._btn_led.setText(f"LED: {'ON' if checked else 'OFF'}")
        if not self._host_controls_hardware():
            self._queue_comm_task("set_led", checked, self.engine.current_pan, self.engine.current_tilt)

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

    def _on_safety_toggled(self, checked: bool) -> None:
        self._safety_armed = checked
        self._btn_safety.setText(f"Safety: {'ARMED' if checked else 'LOCKED'}")
        if not self._host_controls_hardware():
            self._queue_comm_task("set_safety", checked, self.engine.current_pan, self.engine.current_tilt)

    def _on_manual_fire(self, state: int) -> None:
        if state and not self._safety_armed:
            self._log("Manual fire blocked: Safety is LOCKED")
            if not self._host_controls_hardware():
                self._queue_comm_task("send_command",
                    self.engine.current_pan,
                    self.engine.current_tilt,
                    fire=0,
                    move_time_ms=self._get_manual_move_time_ms(),
                )
            return
        pan = self.engine.current_pan
        tilt = self.engine.current_tilt
        if state and not self._host_controls_hardware():
            if not self._comm.trigger_mode_bb:
                self._log("Manual fire note: trigger mode is Water (MOSFET), not Projectile (ESP32 GPIO13 Servo)")
            if (
                getattr(self._comm, "_mode", None) == self._comm.MODE_WIFI_DEBUG_USB
                and (
                    getattr(self._comm, "_sock", None) is None
                    or getattr(self._comm, "_udp_target", None) is None
                )
            ):
                self._log("Manual fire unavailable: mode 2 routes trigger IO to ESP32 WiFi/GPIO13, and the WiFi link is not connected")
        if self._host_controls_hardware():
            self.manual_fire_requested.emit(int(state))
        else:
            self._queue_comm_task("send_command", pan, tilt, fire=state, move_time_ms=self._get_manual_move_time_ms())

    # ------------------------------------------------------------------ #
    #  Guard position buttons
    # ------------------------------------------------------------------ #

    def _go_to_guard(self) -> None:
        pan = self._spin_guard_pan.value()
        tilt = self._spin_guard_tilt.value()
        pan, tilt = self._clamp_manual_angles(pan, tilt)
        self.engine.hold_current_guard_position(pan, tilt)
        if self._host_controls_hardware():
            self.turret_move_requested.emit(float(pan), float(tilt))
        else:
            self._queue_move_command(pan, tilt, move_time_ms=self._get_manual_move_time_ms(), manual_override=True)
        self._remember_commanded_position(pan, tilt)
        self._suppress_motion_detection()
        self._refresh_status()
        self._log(f"Moving to guard: P{pan:.0f} T{tilt:.0f}")

    def _set_current_as_guard(self) -> None:
        pan = self.engine.current_pan
        tilt = self.engine.current_tilt
        self._spin_guard_pan.setValue(pan)
        self._spin_guard_tilt.setValue(tilt)
        self._refresh_status()
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
            self.config.config_path = "app/config/sentry_v2_settings.json"
            self.config.save(str(SENTRY_V2_SETTINGS_PATH))
            self._save_prompted_target_library()
            self._log(f"Settings saved: {self.config.config_path}")
        except Exception as e:
            self._log(f"Save error: {e}")

    def _save_config_quietly(self) -> None:
        try:
            self.config.config_path = "app/config/sentry_v2_settings.json"
            self.config.save(str(SENTRY_V2_SETTINGS_PATH))
        except Exception as exc:
            self._log(f"Save error: {exc}")

    def _resolved_prompted_library_path(self) -> Path:
        configured = Path(str(self.config.prompted_library_path or "app/config/sentry_v2_prompted_targets.json"))
        if configured.is_absolute():
            return configured
        return (Path(__file__).resolve().parents[2] / configured).resolve()

    def _load_prompted_target_library(self) -> PromptedTargetLibrary:
        return PromptedTargetLibrary.load(str(self._resolved_prompted_library_path()))

    def _save_prompted_target_library(self) -> None:
        try:
            self._prompted_target_library.save(str(self._resolved_prompted_library_path()))
        except Exception as exc:
            self._log(f"Prompted target save failed: {exc}")

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
        dialog = PromptedMediaSelectionDialog(title="Select Prompted Targets From Image", image=image, parent=self)
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
        dialog = PromptedMediaSelectionDialog(title="Select Prompted Targets From Video", video_path=path, parent=self)
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

    def _host_controls_hardware(self) -> bool:
        return bool(self._host_hardware_managed and self._main_window_ref is not None)

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
        self._reflow_all_responsive_button_grids()

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
        settings.update(dict(preset.get("settings", {})))
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
        path = CUSTOM_MASTER_PRESET_PATH
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
        path = CUSTOM_MASTER_PRESET_PATH
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
        else:
            preset = ENGAGEMENT_PRESETS.get(preset_name_or_settings)
            if not preset:
                return
            settings = self._resolved_engagement_preset_settings(preset)
            preset_label = preset_name_or_settings

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
            self._sync_single_target_ui()
            self._on_engagement_changed()
            if preset_label:
                self._set_engagement_preset_label(preset_label)
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
    ) -> None:
        if self._closing:
            return
        # CHANGE WARNING: automatic motion-disable must not strand manual recovery controls.
        if not self._pan_tilt_motion_enabled and not manual_override:
            return
        move_time = int(self._get_manual_move_time_ms() if move_time_ms is None else move_time_ms)
        with self._pending_move_lock:
            self._pending_move_command = (float(pan), float(tilt), int(fire), move_time)

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
                if self._pending_move_command is not None:
                    move_command = self._pending_move_command
                    self._pending_move_command = None
            if move_command is not None and not self._closing:
                try:
                    pan, tilt, fire, move_time = move_command
                    if int(fire) != 0:
                        ok = self._comm.send_command(pan, tilt, fire=fire, move_time_ms=move_time)
                    else:
                        ok = self._comm.send_movement(pan, tilt, move_time_ms=move_time)
                    self.command_result_ready.emit(
                        "move",
                        bool(ok),
                        getattr(self._comm, "_last_error", "") or getattr(self._comm, "_last_cmd", "") or "",
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
        if task_name == "send_pir_enabled":
            ok = self._comm.send_pir_enabled(*args, **kwargs)
            self.command_result_ready.emit("send_pir_enabled", bool(ok), getattr(self._comm, "_last_error", "") or getattr(self._comm, "_last_cmd", "") or "")
            return

    def _on_command_result_ready(self, command_name: str, ok: bool, detail: str) -> None:
        if self._closing:
            return
        if hasattr(self, "_lbl_last_cmd") and getattr(self._comm, "_last_cmd", ""):
            self._lbl_last_cmd.setText(f"Last: {self._comm._last_cmd}")
        if ok:
            return
        detail_text = str(detail or "command failed")
        if command_name == "move":
            self._log(f"Move failed: {detail_text}")
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

        self._lbl_state.setText(f"State: {stats['state']}")
        self._lbl_stats.setText(
            f"Targets: {stats['targets_visible']} | "
            f"Qualified: {stats['targets_qualified']} | "
            f"Engaged: {stats['engagements_total']}\n"
            f"Err P/T: {stats['last_err_pan_deg']:+.2f}/{stats['last_err_tilt_deg']:+.2f} | "
            f"Lock: {stats['aim_lock_frames']} | "
            f"Move: {int(getattr(self, '_last_tracking_move_time_ms', 0))}ms | "
            f"Suppress: {float(getattr(self, '_last_tracking_suppression_s', 0.0)):.2f}s | "
            f"Pan/Tilt: {'ON' if stats.get('motion_enabled', True) else 'OFF'}"
        )
        current_pan = float(self.engine.current_pan)
        current_tilt = float(self.engine.current_tilt)
        guard = self.config.guard
        self._lbl_angles.setText(
            f"Angles: Pan {current_pan:.1f}° [{guard.pan_min:.0f}..{guard.pan_max:.0f}] | "
            f"Tilt {current_tilt:.1f}° [{guard.tilt_min:.0f}..{guard.tilt_max:.0f}]"
        )
        if hasattr(self, "_lbl_angles_controls"):
            self._lbl_angles_controls.setText(
                f"Current Commanded: Pan {current_pan:.1f}° | Tilt {current_tilt:.1f}°"
            )
        blocked_mask = str(stats.get('no_fire_mask') or '')
        if hasattr(self, "_lbl_no_fire_status"):
            if blocked_mask:
                self._lbl_no_fire_status.setText(f"No-fire mask: BLOCKED by {blocked_mask}")
                self._lbl_no_fire_status.setStyleSheet("font-weight: bold; color: #ff8a7a;")
            else:
                self._lbl_no_fire_status.setText("No-fire mask: clear")
                self._lbl_no_fire_status.setStyleSheet("font-weight: bold; color: #8fe3c4;")
        if hasattr(self, "_lbl_recovery_status"):
            loss_phase = str(stats.get('loss_recovery_phase') or '').strip()
            if loss_phase:
                phase_text = loss_phase.replace('_', ' ').title()
                reacquire_note = str(stats.get('reacquire_note') or '').strip()
                if reacquire_note:
                    self._lbl_recovery_status.setText(f"Recovery: {phase_text} | Note: {reacquire_note}")
                else:
                    self._lbl_recovery_status.setText(f"Recovery: {phase_text}")
                self._lbl_recovery_status.setStyleSheet("font-weight: bold; color: #ffd27a;")
            else:
                self._lbl_recovery_status.setText("Recovery: idle")
                self._lbl_recovery_status.setStyleSheet("font-weight: bold; color: #97a8b8;")
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
        # Update last-command diagnostic in connection tab
        if hasattr(self, "_lbl_last_cmd"):
            cmd = self._comm._last_cmd
            if cmd:
                self._lbl_last_cmd.setText(f"Last: {cmd}")
        
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

    def _log(self, msg: str) -> None:
        ts = time.strftime("%H:%M:%S")
        self._log_text.append(f"[{ts}] {msg}")
        # Auto-scroll
        sb = self._log_text.verticalScrollBar()
        sb.setValue(sb.maximum())

    def _report_runtime_warning(self, context: str, exc: Exception) -> None:
        message = f"{context}: {exc}"
        try:
            if hasattr(self, "_log_text") and self._log_text is not None and not self._closing:
                self._log(f"[WARN] {message}")
                return
        except Exception:
            pass
        print(f"[SENTRY_V2_TAB] {message}", flush=True)

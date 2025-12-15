# [MAIN FILE]
# ==========================================================
#  Movement_Detect_Yolo_me.py
#  ----------------------------------------------------------
#  MAIN APPLICATION FILE for the automated turret UI.
#
#  This file:
#   • Creates all main PyQt widgets, controls, and tracking logic.
#   • Loads and applies presets from turret_presets.py.
#   • Uses TurretEnhancements (from turret_enhancements.py) to handle:
#       - Top "ARM SYSTEM" bar
#       - Status bar (FPS, serial, mode, etc.)
#       - Serial console styling & audio feedback
#
#  When editing this file:
#   - Do NOT copy code from turret_enhancements.py here.
#   - Keep 'self.enhancer = TurretEnhancements(self)' intact.
#   - Only modify the main UI layout, behavior logic, and signal handling.
#
#  Dependencies:
#   • turret_enhancements.py (must be in same folder)
#   • turret_presets.py
#   • sounds/ folder (fire.wav, lockon.wav, startup.wav)
# ==========================================================
import base64
import json
import random  # For guard mode random positions
import os
from pathlib import Path
import math  # For NaN/Inf checks in serial validation
from datetime import datetime

# === AGENT-MANAGED BLOCK START ===
# The following markers and logic were added programmatically by the assistant
# to provide 'hold-on-loss' behavior and to ensure this section is not
# accidentally removed or replaced by automated edits. Keep these comments
# in place when editing this file by hand. Minimal, intentional changes are ok.
# AgentChangeID: HOLD_ON_LOSS_v1
# Date: 2025-10-22
# === AGENT-MANAGED BLOCK END ===

# ========== DEBUGGING & DIAGNOSTICS CONFIG ==========
# Set to True to enable debug output. Set to False for production (default).
# When True, detailed frame-by-frame diagnostics will be logged to the serial output.
DEBUG = False

# === END CONFIG ===
import sys
import time
import inspect
from typing import Any, cast
import importlib

import cv2
import numpy as np
import serial
from PyQt5.QtCore import QByteArray, Qt, QTimer, QEvent, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap, QFont, QKeySequence, QTextCursor
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDockWidget,
    QDoubleSpinBox,
    QFileDialog,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSlider,
    QSpinBox,
    QStyleFactory,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

# State logger for debugging and diagnostics (optional)
try:
    from state_logger import StateLogger
except ImportError:
    # Fallback: simple no-op state logger if module not available
    class StateLogger:
        def __init__(self, writer=None):
            self.writer = writer
        def enable(self, enabled):
            pass
        def log(self, msg):
            pass
        def dump_to_file(self, fname, append=False):
            pass

from theme_manager import ThemeManager
from turret_enhancements import TurretEnhancements
from turret_presets import PRESETS
from yolo_detector import YoloDetector
from behavior_presets import BehaviorPresets  # For user-saved behavior presets

# Import centralized logger for error tracking
try:
    from helpers.logger import get_logger, log_exception
    logger = get_logger()
except ImportError:
    # Fallback if logger not available
    logger = None
    def log_exception(e, ctx=""):
        print(f"ERROR [{ctx}]: {e}")

try:
    # Prefer the cleaned core shortcuts module; fall back to legacy file if present
    import keyboard_shortcuts_core as ks
except Exception as e:
    if logger: log_exception(e, "Loading keyboard_shortcuts_core")
    import keyboard_shortcuts as ks
# Layout manager mixin providing save/load/clear presets and menu wiring
try:
    from layout_manager import LayoutManagerMixin
except Exception:
    # If the extracted mixin isn't available for some reason, define a no-op fallback
    class LayoutManagerMixin:
        def init_layout_menu(self):
            return
        def auto_load_default_layout(self):
            return

# Checklist panel for code validation
try:
    from checklist_panel import ChecklistPanel
except Exception:
    ChecklistPanel = None

# Try to register QTextCursor as a Qt metatype to avoid queued-argument warnings
# Use guarded lookup since some PyQt5 builds may not expose qRegisterMetaType directly
try:
    import PyQt5.QtCore as _QtCore
    _qr = getattr(_QtCore, 'qRegisterMetaType', None)
    if callable(_qr):
        try:
            _qr(QTextCursor, 'QTextCursor')
        except Exception:
            try:
                _qr('QTextCursor')
            except Exception:
                pass
except Exception:
    pass

# Additional robust attempts to register the QTextCursor meta-type.
# Some PyQt builds require the type name string; others accept the Python type.
try:
    from PyQt5.QtCore import qRegisterMetaType
    try:
        qRegisterMetaType('QTextCursor')
    except Exception:
        try:
            qRegisterMetaType(QTextCursor, 'QTextCursor')
        except Exception:
            pass
except Exception:
    pass

# Idle modes system
try:
    from idle_modes import IdleModes
    from idle_settings_window import IdleSettingsWindow
except Exception:
    IdleModes = None
    IdleSettingsWindow = None

# Keyboard shortcuts and floating panel windows
try:
    from keyboard_shortcuts_window import KeyboardShortcutsWindow
except Exception:
    KeyboardShortcutsWindow = None

try:
    from code_fixer import CodeFixer
except Exception:
    CodeFixer = None

# Floating panel window
try:
    from floating_panel_window import FloatingPanelWindow
except Exception:
    FloatingPanelWindow = None

# RUNTIME BANNER: moved into the module main guard to avoid printing when
# the module is imported by other code (helps satisfy linters that expect
# imports at the top of the file).


# Prevent external runtime monkey-patches from applying their own init_ui/layout.
# Set to False only when you explicitly want to allow external reference patches.
_DISABLE_EXTERNAL_PATCHES = True


# Custom button class that detects mouse clicks directly (workaround for signal failures)
class ClickDetectButton(QPushButton):
    """
    Custom QPushButton that detects mouse clicks directly via mousePressEvent.
    This is a workaround for PyQt5 clicked signal not firing reliably.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_click_callback = None
        self._click_count = 0
    
    def set_click_handler(self, callback):
        """Set callback to be called on mouse clicks."""
        self.on_click_callback = callback
    
    def mousePressEvent(self, e):
        """Detect mouse button press and call callback."""
        try:
            if e.button() == Qt.LeftButton:
                self._click_count += 1
                print(f"[CLICK-DETECT] Button clicked (count: {self._click_count})")
                if self.on_click_callback and callable(self.on_click_callback):
                    self.on_click_callback()
                    try:
                        self.repaint()
                        self.update()
                        QApplication.processEvents()
                    except Exception:
                        pass
            super().mousePressEvent(e)
        except Exception as ex:
            print(f"[CLICK-DETECT ERROR] {ex}")
            import traceback
            traceback.print_exc()
            super().mousePressEvent(e)

# Standard COCO 80 classes used as a sensible default when dataset/classes.txt is missing
YOLO_COCO_CLASSES = [
    "person",
    "bicycle",
    "car",
    "motorcycle",
    "airplane",
    "bus",
    "train",
    "truck",
    "boat",
    "traffic light",
    "fire hydrant",
    "stop sign",
    "parking meter",
    "bench",
    "bird",
    "cat",
    "dog",
    "rat",
    "horse",
    "sheep",
    "cow",
    "elephant",
    "bear",
    "zebra",
    "giraffe",
    "backpack",
    "umbrella",
    "handbag",
    "tie",
    "suitcase",
    "frisbee",
    "skis",
    "snowboard",
    "sports ball",
    "kite",
    "baseball bat",
    "baseball glove",
    "skateboard",
    "surfboard",
    "tennis racket",
    "bottle",
    "wine glass",
    "cup",
    "fork",
    "knife",
    "spoon",
    "bowl",
    "banana",
    "apple",
    "sandwich",
    "orange",
    "broccoli",
    "carrot",
    "hot dog",
    "pizza",
    "donut",
    "cake",
    "chair",
    "couch",
    "potted plant",
    "bed",
    "dining table",
    "toilet",
    "tv",
    "laptop",
    "mouse",
    "remote",
    "keyboard",
    "cell phone",
    "microwave",
    "oven",
    "toaster",
    "sink",
    "refrigerator",
    "book",
    "clock",
    "vase",
    "scissors",
    "teddy bear",
    "hair drier",
    "toothbrush",
]


# ============================================================================
# BULLETPROOF AUTOTRACKING STATE MANAGER
# ============================================================================
# This class prevents state corruption and regressions by:
# 1. Centralizing all state transitions through defensive methods
# 2. Validating state consistency before each update
# 3. Auto-correcting common corruption patterns
# 4. Maintaining a transaction log for debugging
# ============================================================================
class AutotrackingStateManager:
    """
    Manages the state of the autotracking system to prevent regression bugs
    where previously fixed issues come back randomly due to state corruption.
    """
    
    def __init__(self, app_instance, enable_logging=True):
        self.app = app_instance
        self.enable_logging = enable_logging
        self.transaction_log = []
        self.max_log_entries = 1000
        
    def log_transition(self, event_name, old_state, new_state, reason=""):
        """Record a state transition for debugging"""
        if not self.enable_logging:
            return
            
        entry = {
            "timestamp": time.time(),
            "event": event_name,
            "old_state": dict(old_state),
            "new_state": dict(new_state),
            "reason": reason
        }
        self.transaction_log.append(entry)
        
        # Keep log from growing unbounded
        if len(self.transaction_log) > self.max_log_entries:
            self.transaction_log = self.transaction_log[-500:]
    
    def get_current_state(self):
        """Snapshot the current system state"""
        return {
            "tracking_active": getattr(self.app, "tracking_active", False),
            "aiming_active": getattr(self.app, "aiming_active", False),
            "manual_override": getattr(self.app, "manual_override", False),
            "trigger_fired": getattr(self.app, "trigger_fired", False),
            "target_locked": getattr(self.app, "target_locked", False),
            "_in_go_home": getattr(self.app, "_in_go_home", False),
            "auto_fire_active": getattr(self.app, "auto_fire_active", False),
        }
    
    def validate_state_consistency(self):
        """
        Check if state is consistent and auto-correct common corruption patterns.
        Returns tuple (is_valid, problems_fixed)
        """
        problems = []
        
        tracking = getattr(self.app, "tracking_active", False)
        aiming = getattr(self.app, "aiming_active", False)
        firing = getattr(self.app, "trigger_fired", False)
        go_home = getattr(self.app, "_in_go_home", False)
        manual = getattr(self.app, "manual_override", False)
        
        # BULLETPROOF RULE 1: If tracking enabled, aiming should also be enabled
        if tracking and not aiming:
            problems.append("CORRUPTION: tracking=ON but aiming=OFF")
            self.app.aiming_active = True
        
        # BULLETPROOF RULE 2: If firing, must have tracking or manual override
        if firing and not (tracking or manual):
            problems.append("CORRUPTION: firing=ON but tracking=OFF and manual=OFF")
            self.app.trigger_fired = False
        
        # BULLETPROOF RULE 3: If go_home is active, tracking should be off
        if go_home and tracking:
            problems.append("CORRUPTION: go_home=ON but tracking=ON")
            self.app.tracking_active = False
            self.app.aiming_active = False
        
        # BULLETPROOF RULE 4: Detection must ALWAYS be running (suppression is deprecated/removed)
        # This prevents the "detection loss" bug from returning.
        # Legacy suppression code has been deprecated - detection should never be suppressed.
        suppress_until = getattr(self.app, "_suppress_detection_until", 0.0)
        if suppress_until > time.time():
            problems.append("CRITICAL: Detection suppression detected! (Should be fully removed)")
            self.app._suppress_detection_until = 0.0  # Force clear legacy suppression
        
        # BULLETPROOF RULE 5: Manual override should timeout properly
        # If manual_override is True but suppression window expired, clear it
        manual_suppress_until = getattr(self.app, "_manual_override_until", 0.0)
        if manual and manual_suppress_until < time.time():
            problems.append("CORRUPTION: manual_override=ON but suppression window expired")
            self.app.manual_override = False
        
        # BULLETPROOF RULE 6: Aiming without tracking is unusual (should only happen during re-acquisition)
        # Track it but don't auto-fix (might be intentional re-acquisition state)
        if aiming and not tracking:
            # Log but don't corrupt - might be valid re-acquisition in progress
            pass
        
        return (len(problems) == 0, problems)
    
    def ensure_tracking_active(self, reason=""):
        """Safely enable tracking with state validation"""
        old_state = self.get_current_state()
        
        # Pre-flight checks
        if getattr(self.app, "_in_go_home", False):
            return False  # Can't start tracking during home move
        
        # Enable tracking
        self.app.tracking_active = True
        self.app.aiming_active = True
        
        # Ensure detection is NOT suppressed
        self.app._suppress_detection_until = 0.0
        
        new_state = self.get_current_state()
        self.log_transition("tracking_enable", old_state, new_state, reason)
        return True
    
    def ensure_tracking_disabled(self, reason=""):
        """Safely disable tracking with state validation"""
        old_state = self.get_current_state()
        
        # Disable tracking
        self.app.tracking_active = False
        self.app.aiming_active = False
        self.app.trigger_fired = False
        self.app.target_locked = False
        
        new_state = self.get_current_state()
        self.log_transition("tracking_disable", old_state, new_state, reason)
        return True
    
    def ensure_firing_stopped(self, reason=""):
        """Safely stop all firing with state validation"""
        old_state = self.get_current_state()
        
        self.app.trigger_fired = False
        if hasattr(self.app, "stop_firing"):
            try:
                self.app.stop_firing()
            except Exception:
                pass
        
        new_state = self.get_current_state()
        self.log_transition("firing_stop", old_state, new_state, reason)
        return True
    
    def export_transaction_log(self, filepath=None):
        """Save transaction log to file for post-mortem analysis"""
        if not filepath:
            filepath = os.path.join(os.path.dirname(__file__), "tracking_state_log.json")
        
        try:
            with open(filepath, 'w') as f:
                json.dump(self.transaction_log, f, indent=2)
            return filepath
        except Exception as e:
            print(f"Error exporting transaction log: {e}")
            return None


class TrackingApp(QMainWindow, LayoutManagerMixin):
    # Signal to safely append serial/log text on the GUI thread
    serial_text_signal = pyqtSignal(str)
    # Signal to carry serial connection results from background thread
    serial_connect_result = pyqtSignal(object)
    def _apply_tooltip_styles_and_texts(self):
        from PyQt5.QtWidgets import QToolTip
        from PyQt5.QtGui import QFont, QPalette, QColor
        try:
            QToolTip.setFont(QFont("Segoe UI", 9))
            pal = QPalette()
            pal.setColor(QPalette.ToolTipBase, QColor("#fffacd"))
            pal.setColor(QPalette.ToolTipText, QColor("#000000"))
            QToolTip.setPalette(pal)
        except Exception:
            pass

        tips = {
            "connect_button": "Open or close the selected serial port connection.",
            "serial_connect_button": "Open or close the selected serial port connection.",
            "serial_port_combo": "Select the serial (COM) port for the device.",
            "serial_port_input": "Type or select the serial (COM) port (e.g., COM3).",
            "serial_baud_combo": "Select the baud rate for the serial connection.",
            "serial_baud_input": "Enter the baud rate (e.g., 115200).",
            "serial_output": "Serial console — incoming and outgoing serial messages appear here.",
            "tracking_toggle": "Enable or disable the autotracking system.",
            "aiming_toggle": "Enable or disable automatic aiming assistance.",
            "fire_button": "Manual fire control (use only when safe).",
            "sound_checkbox": "Toggle UI sound effects (notifications and alerts).",
            "overshoot_input": "Percent overshoot applied to motion gain; positive = more aggressive.",
            "lost_hold_input": "When target is lost, keep aiming at the last known position for this many seconds (0 = disable).",
            "hold_infinite_checkbox": "Hold the last known target position indefinitely after loss (no timeout).",
            "aim_aggression_slider": "How aggressively the turret recenters on target: 0=conservative, 50=balanced, 100=very aggressive (may overshoot).",
            "final_approach_boost_checkbox": "Enable speed boost and reduced smoothing when the target is very close to improve final centering.",
            "lock_target_btn": "Snap to the last detected target at maximum speed. If armed, fires automatically when position is reached.",
            "fire_indicator": "Indicates a requested fire event from the host. Pulses when a fire is requested and remains extended when MCU confirms.",
        }
        for attr, text in tips.items():
            try:
                w = getattr(self, attr, None)
                if w is not None and hasattr(w, "setToolTip"):
                    w.setToolTip(text)
            except Exception:
                pass

    def _init_shortcut_and_notes_tabs(self):
        from PyQt5.QtWidgets import QTabWidget, QTextEdit, QLabel, QWidget, QVBoxLayout, QScrollArea, QDockWidget
        from PyQt5.QtCore import Qt
        import json
        import os
        
        # === CREATE CENTRAL TAB WIDGET for Video, Shortcuts, Notes ===
        # This is the primary central widget where all three are dockable
        self.main_tab_widget = QTabWidget()
        self.main_tab_widget.setDocumentMode(False)
        self.main_tab_widget.setTabsClosable(False)
        
        # === HOME TAB (First Tab) ===
        home_container = QWidget()
        home_layout = QVBoxLayout(home_container)
        home_layout.setContentsMargins(0, 0, 0, 0)
        home_layout.setSpacing(0)
        
        # Create home screen with logo/branding
        home_content = QWidget()
        home_content_layout = QVBoxLayout(home_content)
        home_content_layout.setContentsMargins(20, 20, 20, 20)
        home_content_layout.setSpacing(20)
        home_content.setStyleSheet("background-color: #2d2d2d;")  # Match window dark grey
        
        # Add title
        title_label = QLabel("AI TRACKING TURRET V4.0")
        title_font = QFont()
        title_font.setPointSize(24)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setStyleSheet("color: #00FF00; text-align: center; background-color: #2d2d2d;")
        title_label.setAlignment(Qt.AlignCenter)
        home_content_layout.addWidget(title_label)
        
        # Add logo/placeholder area with responsive sizing
        logo_label = QLabel()
        logo_label.setAlignment(Qt.AlignCenter)
        logo_label.setMinimumHeight(150)
        logo_label.setMaximumHeight(400)
        logo_label.setStyleSheet("background-color: #2d2d2d;")  # Match background
        logo_label.setScaledContents(False)
        
        # Try to load logo image
        try:
            logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
            if os.path.exists(logo_path):
                pixmap = QPixmap(logo_path)
                if not pixmap.isNull():
                    # Scale logo responsively - max 80% of available height
                    max_height = int(400 * 0.8)
                    scaled = pixmap.scaledToHeight(max_height, Qt.SmoothTransformation)
                    logo_label.setPixmap(scaled)
                else:
                    logo_label.setText("🏆 LOGO PLACEHOLDER")
                    logo_label.setStyleSheet("color: #00FF00; font-size: 48px; background-color: #2d2d2d;")
            else:
                # Use placeholder
                logo_label.setText("🏆 LOGO PLACEHOLDER")
                logo_label.setStyleSheet("color: #00FF00; font-size: 48px; background-color: #2d2d2d;")
        except Exception:
            logo_label.setText("🏆 LOGO PLACEHOLDER")
            logo_label.setStyleSheet("color: #00FF00; font-size: 48px; background-color: #2d2d2d;")
        
        logo_label.setMinimumSize(200, 150)
        home_content_layout.addWidget(logo_label, stretch=1)
        
        # Add status section
        status_label = QLabel("System Status")
        status_font = QFont()
        status_font.setPointSize(14)
        status_font.setBold(True)
        status_label.setFont(status_font)
        status_label.setStyleSheet("color: #00FF00; background-color: #2d2d2d;")
        home_content_layout.addWidget(status_label)
        
        # Status info
        status_info = QLabel(
            "• Press 'Connect' to initialize serial connection\n"
            "• Enable 'Start Tracking' to begin object detection\n"
            "• Enable 'Start Aiming' to activate servo control\n"
            "• Check 'Code Checker' from Tools menu for diagnostics"
        )
        status_info.setStyleSheet("color: #FFFFFF; font-size: 11px; line-height: 1.6; background-color: #2d2d2d;")
        home_content_layout.addWidget(status_info)
        
        # Tilt Safety Status (NEW)
        self.tilt_safety_label = QLabel("🛡️ Tilt Safety: OK")
        self.tilt_safety_label.setStyleSheet("color: #00FF00; font-size: 10px; background-color: #2d2d2d;")
        home_content_layout.addWidget(self.tilt_safety_label)
        
        home_content_layout.addStretch()
        
        scroll_home = QScrollArea()
        scroll_home.setWidgetResizable(True)
        scroll_home.setWidget(home_content)
        home_layout.addWidget(scroll_home)
        
        self.main_tab_widget.addTab(home_container, "🏠 Home")

        # === VIDEO TAB ===
        if not hasattr(self, "video_frame") or self.video_frame is None:
            self.video_frame = QFrame()
            video_layout = QVBoxLayout(self.video_frame)
            video_layout.setContentsMargins(0, 0, 0, 0)
            if getattr(self, "video_label", None) is not None:
                video_layout.addWidget(self.video_label)
        
        self.main_tab_widget.addTab(self.video_frame, "📹 Video")

        # Shortcuts tab removed - now in Tools menu as "Keyboard Shortcuts" window
        
        # === NOTES TAB ===
        notes_container = QWidget()
        notes_layout = QVBoxLayout(notes_container)
        notes_layout.setContentsMargins(8, 8, 8, 8)

        notepad_widget = None
        try:
            from notepad_window import NotepadWidget
            notepad_widget = NotepadWidget()
            notes_layout.addWidget(notepad_widget)
            self.notepad_widget = notepad_widget
        except ImportError:
            self.notes_edit = QTextEdit()
            self.notes_edit.setPlaceholderText("Enter your notes here...")
            
            notes_file = os.path.join(os.path.dirname(__file__), "UserNotes.json")
            try:
                if os.path.exists(notes_file):
                    with open(notes_file, 'r') as f:
                        notes_data = json.load(f)
                        self.notes_edit.setPlainText(notes_data.get("notes", ""))
            except Exception as e:
                print(f"Error loading notes: {e}")

            notes_layout.addWidget(self.notes_edit)

        self.main_tab_widget.addTab(notes_container, "📝 Notes")
        
        # === SERIAL SETTINGS TAB ===
        serial_settings_container = QWidget()
        serial_settings_layout = QVBoxLayout(serial_settings_container)
        serial_settings_layout.setContentsMargins(16, 16, 16, 16)
        
        # Create a form-like layout for serial settings
        from PyQt5.QtWidgets import QFormLayout, QGroupBox
        
        serial_form = QFormLayout()
        
        # COM Port / Serial Port selection
        try:
            port_label = QLabel("Serial Port:")
            if getattr(self, "com_port_input", None) is None:
                self.com_port_input = QLineEdit()
                self.com_port_input.setText("COM3")
            serial_form.addRow(port_label, self.com_port_input)
        except Exception:
            pass
        
        # Baud Rate
        try:
            baud_label = QLabel("Baud Rate:")
            if getattr(self, "baud_rate_input", None) is None:
                self.baud_rate_input = QSpinBox()
                self.baud_rate_input.setRange(2400, 115200)
                self.baud_rate_input.setValue(115200)
            serial_form.addRow(baud_label, self.baud_rate_input)
        except Exception:
            pass
        
        # Data Bits
        try:
            databits_label = QLabel("Data Bits:")
            if getattr(self, "data_bits_combo", None) is None:
                self.data_bits_combo = QComboBox()
                self.data_bits_combo.addItems(["5", "6", "7", "8"])
                self.data_bits_combo.setCurrentText("8")
            serial_form.addRow(databits_label, self.data_bits_combo)
        except Exception:
            pass
        
        # Stop Bits
        try:
            stopbits_label = QLabel("Stop Bits:")
            if getattr(self, "stop_bits_combo", None) is None:
                self.stop_bits_combo = QComboBox()
                self.stop_bits_combo.addItems(["1", "1.5", "2"])
                self.stop_bits_combo.setCurrentText("1")
            serial_form.addRow(stopbits_label, self.stop_bits_combo)
        except Exception:
            pass
        
        # Parity
        try:
            parity_label = QLabel("Parity:")
            if getattr(self, "parity_combo", None) is None:
                self.parity_combo = QComboBox()
                self.parity_combo.addItems(["None", "Even", "Odd"])
                self.parity_combo.setCurrentText("None")
            serial_form.addRow(parity_label, self.parity_combo)
        except Exception:
            pass
        
        # Flow Control
        try:
            flowctrl_label = QLabel("Flow Control:")
            if getattr(self, "flow_control_combo", None) is None:
                self.flow_control_combo = QComboBox()
                self.flow_control_combo.addItems(["None", "RTS/CTS", "XON/XOFF"])
                self.flow_control_combo.setCurrentText("None")
            serial_form.addRow(flowctrl_label, self.flow_control_combo)
        except Exception:
            pass
        
        # Timeout setting
        try:
            timeout_label = QLabel("Read Timeout (ms):")
            if getattr(self, "serial_timeout_spinbox", None) is None:
                self.serial_timeout_spinbox = QSpinBox()
                self.serial_timeout_spinbox.setRange(0, 10000)
                self.serial_timeout_spinbox.setValue(100)
            serial_form.addRow(timeout_label, self.serial_timeout_spinbox)
        except Exception:
            pass
        
        # === AUDIO/SOUND SETTINGS ===
        try:
            audio_separator = QLabel("─" * 40)
            audio_separator.setStyleSheet("color: #666;")
            serial_form.addRow(audio_separator)
            
            # Sound Toggle
            sound_label = QLabel("Enable Sound:")
            if getattr(self, "sound_enabled_checkbox", None) is None:
                self.sound_enabled_checkbox = QCheckBox("Audio Effects")
                self.sound_enabled_checkbox.setChecked(True)
            try:
                self._safe_connect("sound_enabled_checkbox", "toggled", self.save_settings)
            except Exception:
                pass
            serial_form.addRow(sound_label, self.sound_enabled_checkbox)
            
            # Sound Volume Control
            volume_label = QLabel("Volume Level:")
            volume_container = QWidget()
            volume_layout = QHBoxLayout(volume_container)
            volume_layout.setContentsMargins(0, 0, 0, 0)
            
            if getattr(self, "sound_volume_slider", None) is None:
                self.sound_volume_slider = QSlider(Qt.Horizontal)
                self.sound_volume_slider.setRange(0, 100)
                self.sound_volume_slider.setValue(80)
                self.sound_volume_slider.setTickPosition(QSlider.TicksBelow)
                self.sound_volume_slider.setTickInterval(10)
            
            if getattr(self, "volume_label_display", None) is None:
                self.volume_label_display = QLabel("80%")
                self.volume_label_display.setMinimumWidth(40)
                self.volume_label_display.setStyleSheet("font-weight: bold; color: #00ff99;")
            
            try:
                def on_volume_changed(value):
                    try:
                        self.volume_label_display.setText(f"{value}%")
                        self.save_settings()
                    except Exception:
                        pass
                self.sound_volume_slider.sliderMoved.connect(on_volume_changed)
                self.sound_volume_slider.valueChanged.connect(on_volume_changed)
            except Exception:
                pass
            
            volume_layout.addWidget(self.sound_volume_slider, 1)
            volume_layout.addWidget(self.volume_label_display)
            serial_form.addRow(volume_label, volume_container)
        except Exception as e:
            print(f"Error adding audio controls: {e}")
        
        # Group the settings
        settings_group = QGroupBox("Serial Connection Settings")
        settings_group.setLayout(serial_form)
        serial_settings_layout.addWidget(settings_group)
        
        # Action buttons
        button_layout = QHBoxLayout()
        
        try:
            if getattr(self, "serial_apply_btn", None) is None:
                self.serial_apply_btn = QPushButton("Apply Settings")
            try:
                self._safe_connect("serial_apply_btn", "clicked", self.apply_serial_settings)
            except Exception:
                try:
                    self.serial_apply_btn.clicked.connect(self.apply_serial_settings)
                except Exception:
                    pass
            button_layout.addWidget(self.serial_apply_btn)
        except Exception:
            pass
        
        try:
            if getattr(self, "serial_default_btn", None) is None:
                self.serial_default_btn = QPushButton("Reset to Defaults")
            try:
                self._safe_connect("serial_default_btn", "clicked", self.reset_serial_settings)
            except Exception:
                try:
                    self.serial_default_btn.clicked.connect(self.reset_serial_settings)
                except Exception:
                    pass
            button_layout.addWidget(self.serial_default_btn)
        except Exception:
            pass
        
        button_layout.addStretch()
        serial_settings_layout.addLayout(button_layout)
        serial_settings_layout.addStretch()
        
        self.main_tab_widget.addTab(serial_settings_container, "⚙️ Serial Settings")
        
        # === RECORDING SETTINGS TAB (HIDDEN BY DEFAULT) ===
        try:
            recording_settings_container = QWidget()
            recording_settings_layout = QVBoxLayout(recording_settings_container)
            recording_settings_layout.setContentsMargins(16, 16, 16, 16)
            
            recording_form = QFormLayout()
            
            # Video Recording Enable
            try:
                record_enable_label = QLabel("Enable Recording:")
                if getattr(self, "recording_enabled_checkbox", None) is None:
                    self.recording_enabled_checkbox = QCheckBox("Record Video")
                    self.recording_enabled_checkbox.setChecked(False)
                try:
                    self._safe_connect("recording_enabled_checkbox", "toggled", self.save_settings)
                except Exception:
                    pass
                recording_form.addRow(record_enable_label, self.recording_enabled_checkbox)
            except Exception:
                pass
            
            # Auto-Record Setting
            try:
                autorecord_label = QLabel("Auto-Record:")
                if getattr(self, "autorecord_checkbox", None) is None:
                    self.autorecord_checkbox = QCheckBox("Start recording when tracking starts")
                    self.autorecord_checkbox.setChecked(False)
                try:
                    self._safe_connect("autorecord_checkbox", "toggled", self.save_settings)
                except Exception:
                    pass
                recording_form.addRow(autorecord_label, self.autorecord_checkbox)
            except Exception:
                pass
            
            # Video Format Selection
            try:
                format_label = QLabel("Video Format:")
                if getattr(self, "video_format_combo", None) is None:
                    self.video_format_combo = QComboBox()
                    self.video_format_combo.addItems(["MP4 (H.264)", "AVI (MJPEG)", "MOV (H.264)"])
                try:
                    self._safe_connect("video_format_combo", "currentIndexChanged", self.save_settings)
                except Exception:
                    pass
                recording_form.addRow(format_label, self.video_format_combo)
            except Exception:
                pass
            
            # Frame Rate Selection
            try:
                fps_label = QLabel("Frame Rate:")
                if getattr(self, "fps_combo", None) is None:
                    self.fps_combo = QComboBox()
                    self.fps_combo.addItems(["24 FPS", "30 FPS", "60 FPS"])
                    self.fps_combo.setCurrentText("30 FPS")
                try:
                    self._safe_connect("fps_combo", "currentIndexChanged", self.save_settings)
                except Exception:
                    pass
                recording_form.addRow(fps_label, self.fps_combo)
            except Exception:
                pass
            
            # Video Quality
            try:
                quality_label = QLabel("Video Quality:")
                if getattr(self, "quality_combo", None) is None:
                    self.quality_combo = QComboBox()
                    self.quality_combo.addItems(["Low (1000 kbps)", "Medium (5000 kbps)", "High (15000 kbps)"])
                    self.quality_combo.setCurrentText("Medium (5000 kbps)")
                try:
                    self._safe_connect("quality_combo", "currentIndexChanged", self.save_settings)
                except Exception:
                    pass
                recording_form.addRow(quality_label, self.quality_combo)
            except Exception:
                pass
            
            # Recording Directory
            try:
                dir_label = QLabel("Save Location:")
                dir_container = QWidget()
                dir_layout = QHBoxLayout(dir_container)
                dir_layout.setContentsMargins(0, 0, 0, 0)
                
                if getattr(self, "recording_dir_input", None) is None:
                    self.recording_dir_input = QLineEdit()
                    self.recording_dir_input.setText(os.path.join(os.path.expanduser("~"), "Videos", "Turret"))
                
                if getattr(self, "browse_dir_btn", None) is None:
                    self.browse_dir_btn = QPushButton("Browse...")
                    self.browse_dir_btn.setMaximumWidth(100)
                try:
                    self._safe_connect("browse_dir_btn", "clicked", self.browse_recording_directory)
                except Exception:
                    try:
                        self.browse_dir_btn.clicked.connect(self.browse_recording_directory)
                    except Exception:
                        pass
                
                dir_layout.addWidget(self.recording_dir_input)
                dir_layout.addWidget(self.browse_dir_btn)
                recording_form.addRow(dir_label, dir_container)
            except Exception:
                pass
            
            # Storage Limit
            try:
                storage_label = QLabel("Storage Limit (GB):")
                if getattr(self, "storage_limit_spinbox", None) is None:
                    self.storage_limit_spinbox = QDoubleSpinBox()
                    self.storage_limit_spinbox.setRange(0.1, 1000.0)
                    self.storage_limit_spinbox.setValue(10.0)
                    self.storage_limit_spinbox.setSingleStep(0.5)
                try:
                    self._safe_connect("storage_limit_spinbox", "valueChanged", self.save_settings)
                except Exception:
                    pass
                recording_form.addRow(storage_label, self.storage_limit_spinbox)
            except Exception:
                pass
            
            # Auto-Cleanup when limit reached
            try:
                cleanup_label = QLabel("Auto-Cleanup:")
                if getattr(self, "autocleanup_checkbox", None) is None:
                    self.autocleanup_checkbox = QCheckBox("Delete oldest files when limit reached")
                    self.autocleanup_checkbox.setChecked(True)
                try:
                    self._safe_connect("autocleanup_checkbox", "toggled", self.save_settings)
                except Exception:
                    pass
                recording_form.addRow(cleanup_label, self.autocleanup_checkbox)
            except Exception:
                pass
            
            # Current Storage Usage
            try:
                usage_label = QLabel("Storage Usage:")
                if getattr(self, "storage_usage_label", None) is None:
                    self.storage_usage_label = QLabel("Calculating...")
                    self.storage_usage_label.setStyleSheet("color: #0099ff;")
                recording_form.addRow(usage_label, self.storage_usage_label)
            except Exception:
                pass
            
            # Recording Controls Group
            recording_group = QGroupBox("Video Recording Settings")
            recording_group.setLayout(recording_form)
            recording_settings_layout.addWidget(recording_group)
            
            # Action buttons
            recording_button_layout = QHBoxLayout()
            
            try:
                if getattr(self, "record_apply_btn", None) is None:
                    self.record_apply_btn = QPushButton("Apply Settings")
                try:
                    self._safe_connect("record_apply_btn", "clicked", self.apply_recording_settings)
                except Exception:
                    try:
                        self.record_apply_btn.clicked.connect(self.apply_recording_settings)
                    except Exception:
                        pass
                recording_button_layout.addWidget(self.record_apply_btn)
            except Exception:
                pass
            
            try:
                if getattr(self, "record_test_btn", None) is None:
                    self.record_test_btn = QPushButton("Test Recording")
                try:
                    self._safe_connect("record_test_btn", "clicked", self.test_recording)
                except Exception:
                    try:
                        self.record_test_btn.clicked.connect(self.test_recording)
                    except Exception:
                        pass
                recording_button_layout.addWidget(self.record_test_btn)
            except Exception:
                pass
            
            recording_button_layout.addStretch()
            recording_settings_layout.addLayout(recording_button_layout)
            recording_settings_layout.addStretch()
            
            # Create Recording Settings tab and HIDE it by default
            recording_tab_index = self.main_tab_widget.addTab(recording_settings_container, "🎬 Recording Settings")
            self.recording_settings_tab_index = recording_tab_index
            # Hide the tab by removing it or set a property
            # We'll use a property to track that it's hidden but still accessible via menu
            self.recording_settings_hidden = True
            
        except Exception as e:
            print(f"Error creating recording settings tab: {e}")
        
        # Set default tab index to Home
        self.main_tab_widget.setCurrentIndex(0)
        
        # Set as central widget
        self.setCentralWidget(self.main_tab_widget)
        
        # Set default size
        try:
            self.resize(1600, 1000)
            self.setMinimumSize(800, 600)
        except Exception:
            pass

        # BULLETPROOF FIX: Set up auto-save timer for notes (every 5 seconds)
        try:
            self._notes_autosave_timer = QTimer(self)
            self._notes_autosave_timer.timeout.connect(self.save_notes)
            self._notes_autosave_timer.start(5000)  # Auto-save every 5 seconds
        except Exception as e:
            print(f"Error setting up notes autosave: {e}")

    def save_notes(self):
        """Save notes to file - called both by auto-save timer and on app close."""
        try:
            # If using standalone notepad widget, delegate to it
            if hasattr(self, "notepad_widget") and self.notepad_widget is not None:
                try:
                    if hasattr(self.notepad_widget, "save_file"):
                        self.notepad_widget.save_file()
                except Exception as e:
                    print(f"Error saving notepad: {e}")
            # Otherwise save the inline notes editor if present
            elif hasattr(self, "notes_edit"):
                try:
                    notes_file = os.path.join(os.path.dirname(__file__), "UserNotes.json")
                    notes_data = {"notes": self.notes_edit.toPlainText()}
                    with open(notes_file, 'w') as f:
                        json.dump(notes_data, f, indent=2)
                except Exception as e:
                    print(f"Error saving notes: {e}")
        except Exception as e:
            print(f"Error in save_notes: {e}")

    def setup_dockable_tabs(self):
        """Convert main tabs (Video, Shortcuts, Notes) to dockable widgets.
        
        This method creates dock widgets for the Video, Shortcuts, and Notes tabs,
        allowing users to rearrange them as separate dockable windows.
        """
        try:
            if not hasattr(self, "main_tab_widget"):
                return
            
            # Extract tabs and convert to docks
            tab_widget = self.main_tab_widget
            
            for i in range(tab_widget.count()):
                tab_title = tab_widget.tabText(i)
                tab_content = tab_widget.widget(i)
                
                # Skip video tab as it's the central widget, but create docks for others
                if tab_title.lower() in ["shortcuts", "notes"]:
                    try:
                        # Create a dock widget for this tab
                        dock = QDockWidget(tab_title, self)
                        dock.setObjectName(f"Dock_{tab_title}")
                        dock.setWidget(tab_content)
                        
                        # Add dock to the left side
                        self.addDockWidget(
                            self._qt_dock_area("LeftDockWidgetArea", 1), dock
                        )
                        
                        # Store reference for later
                        setattr(self, f"dock_{tab_title.lower()}", dock)
                    except Exception as e:
                        print(f"Error creating dock for {tab_title}: {e}")
        except Exception as e:
            print(f"Error in setup_dockable_tabs: {e}")

    SETTINGS_FILE = "settings.json"
    PREFERRED_FILE = "preferred_defaults.json"
    STEP_INCREMENT = 5
    # Preferred default dock column width (px). Used as a conservative cap so
    # left/right dock columns default to a reasonable size matching the UI
    # sketch the user provided.
    DEFAULT_DOCK_COLUMN_WIDTH = 320
    # (static-analysis helpers removed) - avoid reassigning imported Qt widget names

    def __init__(self):
        super().__init__()
        # Flag to track if UI initialization failed due to Qt errors
        self._ui_init_failed = False
        # Explicit typed widget attributes to help static analysis and IDEs
        # (these are assigned actual widget instances in init_ui()).
        # Instance widget attributes (declared with concrete types so static
        # analyzers know these attributes are widgets after init_ui runs).
        # They are assigned actual widget instances inside init_ui().
        self.video_label: QLabel
        self.sniper_view_label: QLabel
        self.tilt_safety_label: QLabel  # Tilt safety status indicator (NEW)
        self.tracking_btn: QPushButton
        self.aiming_btn: QPushButton
        self.aiming_active: bool
        self.home_pan_input: QSpinBox
        self.home_tilt_input: QSpinBox
        self.go_home_button: QPushButton
        self.pan_min_input: QSpinBox
        self.pan_max_input: QSpinBox
        self.tilt_min_input: QSpinBox
        self.tilt_max_input: QSpinBox
        self.detection_mode_combo: QComboBox
        self.yolo_model_combo: QComboBox
        self.yolo_confidence_input: QDoubleSpinBox
        self.yolo_classes_input: QLineEdit
        self.open_trainer_btn: QPushButton
        self.lost_hold_input: QDoubleSpinBox
        self.hold_infinite_checkbox: QCheckBox
        self.snap_threshold_slider: QSlider
        self.smoothing_input: QDoubleSpinBox
        self.movement_sensitivity_slider: QSlider
        self.tracking_speed_slider: QSlider
        self.manual_speed_slider: QSlider
        self.position_label: QLabel
        self.serial_output: QTextEdit
        self.save_defaults_btn: QPushButton
        self.target_locked = False
        # Hardware / runtime handles
        self.ser = None
        self.cap = None
        self._camera_open_needed = False  # Flag to trigger camera re-opening when resolution changes
        self._serial_connection_in_progress = False  # FIX DEC15: Prevent concurrent connection attempts

        # ARDUINO CONSTRAINTS (defaults — load_settings will override if file exists)
        # UPDATED DEC 8, 2025: New pan/tilt limits for extended servo range
        self.PAN_MIN = 0      # Full left coverage (updated from 5)
        self.PAN_MAX = 220    # Extended horizontal sweep (updated from 185)
        self.TILT_MIN = 0     # Full bottom coverage (updated from 18)
        self.TILT_MAX = 70    # Optimized vertical range (updated from 90)

        # Home defaults
        # NOTE: prefer a lower/resting tilt so the camera looks slightly down by default
        self.HOME_PAN = 90
        self.HOME_TILT = 40  # lowered from 80 to avoid resting tilted-up at startup
        self.HOME_SPEED = 5  # Default homing speed: 5% (smooth, not jerky - reduced for 7.4V fast servo)
        # Max degrees per second at 100% home speed (used by host-side interpolation)
        # Reduced from 15 to 8 deg/sec for smoother home movement with faster servo at 7.4V
        self.HOME_MAX_SPEED_DEG_PER_SEC = 8.0

        # Internal state
        self.prev_pan_angle = self.HOME_PAN
        self.prev_tilt_angle = self.HOME_TILT
        self.target_pan = self.HOME_PAN
        self.target_tilt = self.HOME_TILT
        # CRITICAL FIX DEC1: Initialize last_sent values to prevent untracked servo movement at startup
        # FIX DEC9: Use sentinel values (-9999) to ensure FIRST COMMAND IS ALWAYS SENT
        # If initialized to HOME_PAN/HOME_TILT, the redundant command filter would block the initial move
        # Sentinel values force comparison to fail on first cycle, guaranteeing servo gets activated
        self.last_sent_pan = -9999  # Sentinel: no servo position has been sent yet
        self.last_sent_tilt = -9999  # Sentinel: no servo position has been sent yet
        # CRITICAL FIX DEC8: Initialize last_known values for detection loss fallback chain
        # FIX DEC8b: Keep as FLOAT not INT to preserve sub-degree precision
        # Truncating to int causes 3-5° cumulative drift per 10 frames
        # These store the last detected position and are used when target is lost and hold window expires
        # Without these, manual_override=True case skips position restoration entirely
        self.last_known_pan = float(self.HOME_PAN)
        self.last_known_tilt = float(self.HOME_TILT)
        self.trigger_fired = False
        self.last_trigger_time = 0.0
        self._firing_start_time = 0.0  # Track when firing started (for timeout)
        self._max_firing_duration = 3.0  # Max seconds to fire continuously (default: 3 sec)
        self.prev_frame_time = time.time()
        
        # Diagnostic counter for send_serial_command calls
        self._send_serial_cmd_count = 0

        # Static configuration
        self.STEP_INCREMENT = 5  # Default step size for manual control
        self.PREFERRED_FILE = "preferred_defaults.json"
        self.SETTINGS_FILE = "settings.json"

        # Controls state
        self.trigger_mode_bb = False
        self.relay1_state = 0
        self.relay2_state = 0
        self.safety_state = 1
        # BULLETPROOF FIX: Tilt safety switch - only blocks if this is True AND switch connected
        self.tilt_safety_switch_enabled = False  # User must enable in settings if they have the switch
        self.tilt_safety_triggered = False
        # Auto-fire flag (controlled by the Auto-Fire checkbox)
        self.auto_fire_enabled = False
        # Whether tracking loop is actively controlling targeting
        self.tracking_active = False
        # Whether servos are allowed to move (aiming enabled)
        self.aiming_active = False
        # Whether tracking was active before a manual override (used to resume)
        self.tracking_was_active = False
        # Infinite hold toggle (when True, never timeout hold)
        self.hold_infinite = False
        
        # ========== QUICK TARGET LOCK FEATURE ==========
        # When user presses "Lock Target" button, turret moves to last detected position
        # then resumes normal autotracking. This is a temporary override to move faster.
        self.target_lock_active = False        # Is target lock currently active?
        self.target_lock_pan = None            # Target pan angle to move to
        self.target_lock_tilt = None           # Target tilt angle to move to
        self.target_lock_start_time = None     # When lock was initiated (for timeout)
        self.target_lock_timeout = 5.0         # Max seconds to spend moving to target
        self.target_lock_tolerance = 3.0       # Within ±3 degrees = arrived at target

        # ========== FIXED: INITIALIZE MISSING idle_behavior ATTRIBUTE ==========
        # This attribute was being set in polling but never initialized
        # causing AttributeError if accessed before first save
        self.idle_behavior = "rest"

        # Manual control and overrides
        self.manual_override = False
        self._manual_override_until = 0.0
        self._manual_override_active = False
        self._pressed_keys = set()  # For tracking keyboard input
        
        # Idle modes system
        self.idle_modes = None
        self.idle_settings_window = None
        self.home_screen_timer = None
        # DEC14: DISABLED idle_modes initialization - causes recursion error during startup
        # TODO: Re-enable after fixing recursion issue in IdleModes class
        # if IdleModes is not None:
        #     self.idle_modes = IdleModes()
        
        # Home screen auto-hide timer (for Rest Mode)
        self._home_screen_hide_timer = None
        self._home_screen_hide_delay = 3000  # 3 seconds (adjustable)
        # Pan/Tilt inversion flags (use lowercase attribute names)
        self.flip_pan_direction = False
        self.flip_tilt_direction = False
        # Internal guard to enforce indefinite hold behavior
        # FIX-PERM: HOLD_ON_LOSS_v1 - Do not remove this guard
        self._hold_infinite_active = False
        # Hold target when lost: seconds to hold last-known position before allowing idle behavior
        self.lost_hold_seconds = 5.0
        
        # ========== AIM AGGRESSION SETTINGS (NEW - Dec 2024) ==========
        # aim_aggression: 0-100, controls how aggressively turret pursues center
        #   0 = conservative/lazy, 100 = maximum aggression
        self.aim_aggression = 50  # Default: balanced aggression
        # final_approach_boost: When True, applies 2-3x speed boost when within 2x deadzone
        self.final_approach_boost = True  # Default: enabled for accurate centering
        
        # ========== QUICK STRIKE STATE (NEW - Dec 2024) ==========
        # Quick Strike: Snap to target at max speed, fire, then resume autotracking
        self.quick_strike_active = False  # Is quick strike in progress?
        self.quick_strike_target_pan = 90.0  # Target pan angle for quick strike
        self.quick_strike_target_tilt = 45.0  # Target tilt angle for quick strike
        self.quick_strike_start_time = 0.0  # When quick strike started (for timeout)
        self.quick_strike_fired = False  # Has the quick strike already fired?
        self.last_target_center = None  # (x, y) pixel coords of last detected target center
        
        # ========== HUD COLOR PALETTE (Unified - Dec 2024) ==========
        # All HUD elements use these colors - no ad-hoc BGR values
        # Color hierarchy:
        #   Green  → locked / ready
        #   Cyan   → normal status
        #   Gray   → debug info
        #   Yellow → values (pan/tilt)
        #   Red    → fire / danger ONLY
        self.HUD_CYAN = (255, 255, 0)      # Normal status (BGR format)
        self.HUD_ORANGE = (0, 165, 255)    # Warning/Alert
        self.HUD_RED = (0, 0, 255)         # Danger/Fire ONLY
        self.HUD_GREEN = (0, 255, 0)       # Safe/OK/Locked
        self.HUD_GRAY = (180, 180, 180)    # Debug/Idle info
        self.HUD_WHITE = (255, 255, 255)   # Primary text
        self.HUD_BLACK = (0, 0, 0)         # Outlines/backgrounds
        self.HUD_YELLOW = (0, 255, 255)    # Values (pan/tilt) - BGR format
        
        # ========== HUD FONT STYLES (Unified - Dec 2024) ==========
        # All HUD text uses these styles - no inline font sizes
        # Sizes tuned for 1280x720 - compact and non-intrusive
        self.HUD_FONT = cv2.FONT_HERSHEY_SIMPLEX
        self.HUD_FONT_HEADER = {'scale': 0.55, 'thickness': 2}    # Headers/titles
        self.HUD_FONT_STATUS = {'scale': 0.45, 'thickness': 1}    # Status indicators
        self.HUD_FONT_DEBUG = {'scale': 0.38, 'thickness': 1}     # Debug/small info
        self.HUD_FONT_ALERT = {'scale': 0.75, 'thickness': 2}     # Large alerts (Quick Strike)
        
        # ========== HUD LAYOUT GRID (Fixed positioning - Dec 2024) ==========
        # Fixed margins and line spacing to prevent overlap
        self.HUD_MARGIN = 15                # Edge margin in pixels
        self.HUD_LINE_HEIGHT = 25           # Vertical spacing between lines
        self.HUD_PADDING = 5                # Text box padding
        
        # ========== HUD DATA CONTRACT (Required - Dec 2024) ==========
        # These values are populated in update_frame() and drawn in _add_crosshair_and_scope()
        # CRITICAL: All keys are REQUIRED. No .get() fallbacks allowed in rendering.
        # If a value crashes, fix it at the SOURCE, not with a placeholder.
        self.hud_data = {
            'fps': 0.0,                    # float: current FPS
            'detection_mode': 'FrameDiff', # str: detection algorithm name
            'resolution': '1280x720',      # str: WxH format
            'pan': 90.0,                   # float: current pan angle
            'tilt': 45.0,                  # float: current tilt angle
            'idle_mode': None,             # str or None: idle mode name
            'safety_state': True,          # bool: True=SAFE, False=ARMED
            'trigger_fired': False,        # bool: is firing now
            'quick_strike_active': False,  # bool: quick strike in progress
            'has_target': False,           # bool: target currently detected
            'debug_lines': [],             # list[str]: debug overlay lines
            'recording': False,            # bool: recording active
        }
        
        # Auto-tracking from idle modes: when True, detections during idle will automatically
        # exit idle mode and resume active tracking (critical for continuous tracking-idle-resume cycle)
        self.auto_tracking_enabled = True  # FIX: Was never initialized, breaking idle-to-tracking auto-resume
        # Rapid-fire MOSFET control defaults
        # rapid_fire_rate_hz: integer pulses per second (1..200)
        self.rapid_fire_rate_hz = 1
        # rapid_fire_duty: fraction (0.0-1.0) representing on-time per period
        self.rapid_fire_duty = 0.5
        # Whether rapid-fire is enabled (UI toggle)
        self.rapid_fire_enabled = False
        # Timer used to schedule rapid-fire pulses (created lazily)
        self.rapid_fire_timer = None
        # Internal flag indicating whether the next pulse phase is ON (True) or OFF (False)
        self._rapid_fire_on = False
        # Cached ms durations used by the rapid-fire scheduler (populated when started)
        self._rapid_on_ms = 0
        self._rapid_off_ms = 0
        
        # ========== TILT ENCODER FEEDBACK & PID CONTROL ==========
        # Tilt axis rotary encoder integration (11-26-2025)
        # Provides accurate position feedback for improved tracking accuracy
        
        # Encoder state tracking
        self.tilt_encoder_enabled = False        # Whether encoder feedback is active
        self.tilt_encoder_position = self.HOME_TILT  # Last known encoder-based tilt position
        self.tilt_encoder_raw_count = 0          # Raw encoder pulse count
        self.tilt_servo_target = self.HOME_TILT  # Target position sent to servo
        self.tilt_position_error = 0.0           # Difference between target and encoder position
        self.last_encoder_read_time = time.time()
        
        # PID tuning parameters (can be adjusted via UI or config file)
        self.tilt_pid_kp = 1.2    # Proportional gain (increased for snappier response)
        self.tilt_pid_ki = 0.08   # Integral gain (slightly increased)
        self.tilt_pid_kd = 0.3    # Derivative gain (increased for smooth damping)
        self.tilt_pid_enabled = False  # Whether PID correction is actively applied
        
        # Encoder calibration
        # ENCODER_STEPS_PER_REV: typical rotary encoder steps per full rotation
        # TILT_DEGREES_PER_ENCODER_PULSE: how many degrees each pulse represents
        self.encoder_steps_per_rev = 20      # Adjust based on your specific encoder
        self.tilt_degrees_per_pulse = 1      # 1 pulse = 1 degree (adjust as needed)
        
        # PID integral/derivative state
        self._tilt_pid_integral = 0.0
        self._tilt_pid_last_error = 0.0
        self._tilt_pid_last_update_time = time.time()
        
        # Homing speed adjustment via Arduino
        self.home_speed_percent = 5  # Matches new default (1-100%, reduced from 15% for 7.4V servo)
        self._home_speed_changed = False  # Flag to resend HOMESPEED command when changed
        
        # ========== REDUNDANT COMMAND FILTER ==========
        # Cache previous command tokens to detect when nothing has changed
        # This prevents servo jitter from repeated identical commands
        self._last_fire_token = 0
        self._last_led_token = 0
        self._last_laser_token = 0
        self._last_safety_token = 1
        self._last_mode_token = 0
        
        # ========== VIDEO FRAME RATIO SETTINGS ==========
        # FIXED RESOLUTION: Camera always captures at 1280x720 (16:9 HD)
        # Resolution selector removed from UI - Dec 2024
        # 
        # ⚠️ CRITICAL: TO CHANGE RESOLUTION, YOU MUST EDIT ALL 3 LINES BELOW:
        # 1. self.frame_ratio_setting = "WIDTHxHEIGHT"  (must match key in frame_ratio_options)
        # 2. self.frame_width = WIDTH   (must match width in the tuple)
        # 3. self.frame_height = HEIGHT (must match height in the tuple)
        # 
        # Example: To change to 640x480:
        #   self.frame_ratio_setting = "640x480"
        #   self.frame_width = 640
        #   self.frame_height = 480
        # 
        # ⚠️ DO NOT modify frame_width/frame_height anywhere else in the code!
        # These values are set here at initialization and updated ONLY when camera opens.
        # See CAMERA_RESOLUTION_GUIDE.md for complete instructions.
        # 
        self.frame_ratio_options = {
            "640x480": (640, 480),    # Legacy: 4:3 aspect ratio
            "800x600": (800, 600),    # Legacy: 4:3 aspect ratio
            "1024x768": (1024, 768),  # Legacy: 4:3 aspect ratio
            "1280x720": (1280, 720),  # 16:9 aspect ratio (HD) - CURRENT DEFAULT
        }
        self.frame_ratio_setting = "1280x720"  # FIXED resolution - change all 3 lines together
        self.frame_width = 1280   # FIXED frame width in pixels - must match setting above
        self.frame_height = 720   # FIXED frame height in pixels - must match setting above
        
        # ========== HYBRID DETECTION MODE PARAMETERS ==========
        # Defaults for hybrid detection modes (3, 4, 5)
        self.fusion_strategy_mode = 0  # 0=AND/strict, 1=OR/lenient
        self.motion_gate_threshold = 1.0  # % of frame pixels that must move (for mode 4)
        self.overlap_threshold = 30.0  # % overlap required for BackSub+YOLO match (for mode 5)
        
        # ========== RESOLUTION METADATA & PERFORMANCE HINTS ==========
        # Maps resolution to recommended detection parameters and performance info
        self.resolution_metadata = {
            "640x480 (Fast)": {"max_contour_pct": 0.85, "label": "Fast (4:3)", "fov_est": "~100°", "processing": "⚡⚡⚡ Fastest"},
            "800x600 (Balanced)": {"max_contour_pct": 0.85, "label": "Balanced (4:3)", "fov_est": "~110°", "processing": "⚡⚡ Fast"},
            "1024x768 (High Precision)": {"max_contour_pct": 0.85, "label": "Precision (4:3)", "fov_est": "~120°", "processing": "⚡ Standard"},
            "1280x720 (HD)": {"max_contour_pct": 0.85, "label": "HD (16:9)", "fov_est": "~130°", "processing": "⚡ Standard"},
        }
        
        # ========== END TILT ENCODER FEEDBACK ==========
        
        # ========== STATE MACHINE POLLING (Bypass Qt Signal Failures) ==========
        # Track previous state to detect changes without relying on Qt signals
        self._last_idle_mode_state = None  # Last known idle mode (rest/guard/watch/search/None)
        self._last_idle_behavior_combo_index = -1  # Last known combo selection
        self._last_resolution_index = -1  # Last known resolution combo index
        
        # Serial log control state
        self.serial_paused = False
        self.serial_tx_paused = False
        
        # Separate window instances (initialized on demand)
        self._idle_settings_window = None
        self._keyboard_shortcuts_window = None
        self._yolo_floating_panel = None  # Floating YOLO settings panel (created on demand)

        
        # Watch mode settings
        self._watch_position_pan = self.HOME_PAN
        self._watch_position_tilt = self.HOME_TILT
        
        # Guard mode settings
        self._guard_rest_time = 5.0  # seconds to stay at each position
        self._last_guard_move = 0.0
        self._guard_speed = 0.6
        self._guard_pan_range = (20, 160)  # min/max pan for random positions
        self._guard_tilt_range = (30, 90)  # min/max tilt for random positions

        # Initialize detector/backsub state before building UI so init_ui
        # can safely call into `self.yolo_detector` and related helpers.
        # Provide a small stub so UI code can safely call detector methods even when
        # the real YOLO backend or packages are not installed on the system.
        class _YoloStub:
            def __init__(self):
                self.model_loaded = False

            def find_models(self):
                return []

            def load_model(self, m):
                self.model_loaded = False

            def set_target_classes(self, c):
                pass

            def detect(self, frame, conf=0.5):
                return []

        try:
            # Try to construct the real detector; fall back to the stub on any error
            try:
                # Pass the enhancer so YOLO can play detect sounds (debounced)
                self.yolo_detector = YoloDetector(
                    enhancer=getattr(self, "enhancer", None)
                )
            except Exception:
                self.yolo_detector = _YoloStub()
        except Exception:
            self.yolo_detector = _YoloStub()

        # Background subtractor used by background-subtraction detection mode
        self.backSub = None

        # Keep a small history of last detections for fallback/testing
        self.last_detections: list[tuple[int, int, int, int]] = []
        # Diagnostic frame counter for throttled per-frame logs
        self._frame_diag_counter = 0

        # Wire up the top ARM button to the main safety toggle function
        # NOTE: avoid calling _safe_connect_path here because the enhancer
        # may not yet exist during early init — that produced noisy
        # "CONNECT FAIL" messages in user logs. Only attempt a quiet
        # direct connect when an enhancer instance is already present.
        try:
            enh = getattr(self, "enhancer", None)
            if enh is not None:
                btn = getattr(enh, "arm_toggle_btn", None)
                if btn is not None:
                    try:
                        conn = getattr(getattr(btn, "toggled", None), "connect", None)
                        if callable(conn):
                            conn(self.toggle_safety)
                    except Exception:
                        pass
        except Exception:
            pass

        # Call UI builder and load settings
        try:
            self.init_ui()
        except Exception as ui_error:
            # Qt threading issues may occur during UI initialization (known pre-existing issue)
            # Log the error but continue - the app can still track and aim via backend
            error_str = str(ui_error)
            if "Cannot queue arguments" in error_str or "QTextCursor" in error_str:
                print(f"[INIT] Qt GUI initialization error (non-critical): {error_str}")
                print("[INIT] Continuing with headless mode - tracking backend will still work")
            else:
                print(f"[INIT] UI initialization error: {error_str}")
                import traceback
                traceback.print_exc()
            # Set a flag so we know UI failed to initialize
            self._ui_init_failed = True

        # Connect serial text signal so background code can safely emit plain strings
        try:
            self.serial_text_signal.connect(self._append_serial_text)
        except Exception:
            pass
        try:
            self.serial_connect_result.connect(self._handle_serial_connection_result)
        except Exception:
            pass
        
        # Initialize TurretEnhancements BEFORE AutotrackingStateManager
        # (moved from later in __init__ to ensure enhancer exists for state manager)
        try:
            try:
                self.enhancer = TurretEnhancements(self)
                try:
                    self._safe_append_log("[APP INIT] TurretEnhancements initialized")
                except Exception:
                    print("[APP INIT] TurretEnhancements initialized")
            except Exception as e:
                try:
                    import traceback
                    tb = traceback.format_exc()
                except Exception:
                    tb = None
                try:
                    if tb:
                        print(f"[APP INIT] Error initializing TurretEnhancements: {e}")
                        print(tb)
                    else:
                        print(f"[APP INIT] Error initializing TurretEnhancements: {e}")
                except Exception:
                    pass
                self.enhancer = None
        except Exception:
            self.enhancer = None
        
        # BULLETPROOF FIX: Initialize AutotrackingStateManager
        # This prevents regressions where old bugs come back due to state corruption
        try:
            self.state_manager = AutotrackingStateManager(self, enable_logging=True)
            if self.enhancer:
                self.enhancer.log_serial_output("[INIT] Bulletproof state manager initialized", fire=False)
        except Exception as e:
            print(f"Warning: Failed to initialize state manager: {e}")
            self.state_manager = None
        
        # Assert key widgets are initialized to help static analyzers and IDEs
        # narrow Optional[...] types to concrete widget types. This does not
        # affect runtime behavior but reduces many 'attribute on None' warnings.
        try:
            self._assert_widgets_initialized()
        except Exception:
            # If asserts fail in unusual runtime (e.g., partial UI), continue
            # but keep analyzer benefits in normal runs.
            pass
        # Initialize Layout menu (provided by layout_manager.LayoutManagerMixin)
        try:
            self.init_layout_menu()
        except Exception:
            pass
        # Emit a quick widget presence summary to the serial/console for debugging
        try:
            self._debug_widget_signal_presence()
        except Exception:
            pass
        # Inform static analyzers and IDEs that these Optional[...] attributes
        # now hold concrete widget instances. This uses typing.cast which is a
        # no-op at runtime but improves static type narrowing.
        try:
            self.video_label = cast(QLabel, self.video_label)
            self.sniper_view_label = cast(QLabel, self.sniper_view_label)
            self.tracking_btn = cast(QPushButton, self.tracking_btn)
            self.aiming_btn = cast(QPushButton, self.aiming_btn)
            self.home_pan_input = cast(QSpinBox, self.home_pan_input)
            self.home_tilt_input = cast(QSpinBox, self.home_tilt_input)
            self.go_home_button = cast(QPushButton, self.go_home_button)
            self.pan_min_input = cast(QSpinBox, self.pan_min_input)
            self.pan_max_input = cast(QSpinBox, self.pan_max_input)
            self.tilt_min_input = cast(QSpinBox, self.tilt_min_input)
            self.tilt_max_input = cast(QSpinBox, self.tilt_max_input)
            self.detection_mode_combo = cast(QComboBox, self.detection_mode_combo)
            self.yolo_model_combo = cast(QComboBox, self.yolo_model_combo)
            self.yolo_confidence_input = cast(
                QDoubleSpinBox, self.yolo_confidence_input
            )
            self.yolo_classes_input = cast(QLineEdit, self.yolo_classes_input)
            self.open_trainer_btn = cast(QPushButton, self.open_trainer_btn)
            self.lost_hold_input = cast(QDoubleSpinBox, self.lost_hold_input)
            self.hold_infinite_checkbox = cast(QCheckBox, self.hold_infinite_checkbox)
            self.snap_threshold_slider = cast(QSlider, self.snap_threshold_slider)
            self.smoothing_input = cast(QDoubleSpinBox, self.smoothing_input)
            self.movement_sensitivity_slider = cast(
                QSlider, self.movement_sensitivity_slider
            )
            self.tracking_speed_slider = cast(QSlider, self.tracking_speed_slider)
            self.manual_speed_slider = cast(QSlider, self.manual_speed_slider)
            self.position_label = cast(QLabel, self.position_label)
            self.serial_output = cast(QTextEdit, self.serial_output)
        except Exception:
            pass
        # Lightweight state logger that writes to the serial log pane
        try:
            # Setup pause/buffer flags so UI log output can be paused/resumed
            # without losing messages.
            self.serial_log_paused = False
            self._serial_log_buffer = []

            # Instance-level serial write helper (thread-safe UI enqueue)
            def _serial_write(text, force=False):
                try:
                    # CHECK FOR TILT SAFETY MESSAGES (ONLY RESPECT IF ENABLED)
                    if isinstance(text, str):
                        if "[SAFETY] TILT SAFETY SWITCH TRIGGERED" in text:
                            # BULLETPROOF FIX: Only trigger if user confirmed switch is connected
                            if getattr(self, "tilt_safety_switch_enabled", False):
                                self.tilt_safety_triggered = True
                                try:
                                    self.tilt_safety_label.setText("🛡️ Tilt Safety: TRIGGERED!")
                                    self.tilt_safety_label.setStyleSheet("color: #FF3333; font-size: 10px; background-color: #2d2d2d; font-weight: bold;")
                                except Exception:
                                    pass
                            else:
                                # Switch not enabled - just display message, don't block movement
                                try:
                                    self.tilt_safety_label.setText("🛡️ Tilt Safety: Not Enabled")
                                    self.tilt_safety_label.setStyleSheet("color: #FFFF00; font-size: 10px; background-color: #2d2d2d;")
                                except Exception:
                                    pass
                        elif "[SAFETY] Tilt safety switch reset" in text:
                            self.tilt_safety_triggered = False
                            try:
                                if getattr(self, "tilt_safety_switch_enabled", False):
                                    self.tilt_safety_label.setText("🛡️ Tilt Safety: OK")
                                else:
                                    self.tilt_safety_label.setText("🛡️ Tilt Safety: OK (Disabled)")
                                self.tilt_safety_label.setStyleSheet("color: #00FF00; font-size: 10px; background-color: #2d2d2d;")
                            except Exception:
                                pass
                    
                    # Prefer the enhancer (formats messages and buffers safely) when available.
                    enh = getattr(self, "enhancer", None)
                    if enh is not None:
                        try:
                            # Let the enhancer decide buffering/formatting.
                            try:
                                # Play fire sound only if text contains FIRE or caller flagged it.
                                is_fire = isinstance(text, str) and ("FIRE" in text.upper())
                                enh.log_serial_output(text, fire=is_fire)
                            except Exception:
                                enh.log_serial_output(text)
                            # Update buffer indicator (if present) to reflect any buffered lines.
                            try:
                                bl = getattr(self, "serial_buffer_label", None)
                                if bl is not None:
                                    buf = getattr(self, "_serial_log_buffer", None) or []
                                    bl.setText(f"Paused — {len(buf)} buffered" if getattr(self, "serial_log_paused", False) else "")
                            except Exception:
                                pass
                            return
                        except Exception:
                            # Fall back to local behavior if enhancer fails for any reason.
                            pass

                    # Fallback: respect pause/buffering at main level.
                    if getattr(self, "serial_log_paused", False) and not force:
                        try:
                            self._serial_log_buffer.append(text)
                        except Exception:
                            self._serial_log_buffer = [text]
                        try:
                            bl = getattr(self, "serial_buffer_label", None)
                            if bl is not None:
                                bl.setText(f"Paused — {len(self._serial_log_buffer)} buffered")
                        except Exception:
                            pass
                        return
                    try:
                        try:
                            # Emit plain string to be appended on GUI thread
                            self.serial_text_signal.emit(text)
                        except Exception:
                            try:
                                self.serial_output.append(text)
                            except Exception:
                                pass
                    except Exception:
                        try:
                            self.serial_output.append(text)
                        except Exception:
                            pass
                except Exception:
                    pass

            # Flush buffered messages to the UI (called on resume)
            def _serial_flush_buffer():
                try:
                    buf = getattr(self, "_serial_log_buffer", None)
                    if buf:
                        for t in buf:
                            try:
                                # Prefer enhancer for formatted flush if available
                                if getattr(self, "enhancer", None) is not None:
                                    try:
                                        self.enhancer.log_serial_output(t)
                                    except Exception:
                                        try:
                                            self.serial_text_signal.emit(t)
                                        except Exception:
                                            try:
                                                self.serial_output.append(t)
                                            except Exception:
                                                pass
                                else:
                                    try:
                                        self.serial_text_signal.emit(t)
                                    except Exception:
                                        try:
                                            self.serial_output.append(t)
                                        except Exception:
                                            pass
                            except Exception:
                                try:
                                    self.serial_output.append(t)
                                except Exception:
                                    pass
                        self._serial_log_buffer = []
                        try:
                            bl = getattr(self, "serial_buffer_label", None)
                            if bl is not None:
                                bl.setText("")
                        except Exception:
                            pass
                except Exception:
                    pass

            # Toggle pause state (bound to UI toggle control)
            def _toggle_serial_pause(checked):
                try:
                    self.serial_log_paused = bool(checked)
                    # update button label if present
                    try:
                        if getattr(self, "pause_serial_btn", None):
                            self.pause_serial_btn.setText(
                                "Resume Log" if self.serial_log_paused else "Pause Log"
                            )
                    except Exception:
                        pass
                    # Update buffer indicator immediately
                    try:
                        bl = getattr(self, "serial_buffer_label", None)
                        if bl is not None:
                            buf = getattr(self, "_serial_log_buffer", None) or []
                            bl.setText(f"Paused — {len(buf)} buffered" if self.serial_log_paused else "")
                    except Exception:
                        pass
                    if not self.serial_log_paused:
                        _serial_flush_buffer()
                except Exception:
                    pass

            def _clear_serial_log():
                try:
                    try:
                        self.serial_output.clear()
                    except Exception:
                        pass
                    try:
                        self._serial_log_buffer = []
                    except Exception:
                        pass
                    try:
                        bl = getattr(self, "serial_buffer_label", None)
                        if bl is not None:
                            bl.setText("")
                    except Exception:
                        pass
                except Exception:
                    pass

            # Export handler (bound to Export button in UI); keep inside __init__ to avoid touching class scope.
            def _export_serial_log():
                try:
                    # Combine buffered entries and current UI text for export
                    buf = getattr(self, "_serial_log_buffer", None) or []
                    current = ""
                    try:
                        current = self.serial_output.toPlainText()
                    except Exception:
                        pass
                    combined = "\n".join(buf) + ("\n" + current if current else "") if buf else current
                    # Ask user where to save
                    try:
                        path, _ = QFileDialog.getSaveFileName(self, "Save Serial Log", "serial_log.txt", "Text Files (*.txt);;All files (*.*)")
                        if path:
                            try:
                                with open(path, "w", encoding="utf-8") as f:
                                    f.write(combined)
                                try:
                                    self._serial_write(f"Saved serial log to {path}")
                                except Exception:
                                    pass
                            except Exception as e:
                                try:
                                    self._serial_write(f"Failed to save serial log: {e}")
                                except Exception:
                                    pass
                    except Exception:
                        # If QFileDialog not available (headless), write to a default file
                        try:
                            with open("serial_log_export.txt", "w", encoding="utf-8") as f:
                                f.write(combined)
                            try:
                                self._serial_write("Saved serial log to serial_log_export.txt")
                            except Exception:
                                pass
                        except Exception:
                            pass
                except Exception:
                    pass

            # Toggle hardware serial TX (opt-in, dangerous) — default off
            def _toggle_serial_tx(checked):
                try:
                    self.serial_tx_paused = bool(checked)
                    try:
                        if getattr(self, "pause_serial_tx_btn", None):
                            self.pause_serial_tx_btn.setText("Resume TX" if self.serial_tx_paused else "Pause TX")
                    except Exception:
                        pass
                    try:
                        # Inform operator when toggled
                        if self.serial_tx_paused:
                            self._serial_write("SERIAL TX PAUSED by operator (no hardware commands will be sent)")
                        else:
                            self._serial_write("SERIAL TX RESUMED")
                    except Exception:
                        pass
                except Exception:
                    pass

            # expose as instance-bound helpers so UI wiring can use them
            self._serial_write = _serial_write
            self._serial_flush_buffer = _serial_flush_buffer
            self.toggle_serial_pause = _toggle_serial_pause
            self.clear_serial_log = _clear_serial_log
            self.export_serial_log = _export_serial_log
            self.toggle_serial_tx = _toggle_serial_tx
            # Connect UI controls to these handlers if they exist (safe, idempotent)
            try:
                if getattr(self, "pause_serial_btn", None) and not getattr(self, "_pause_serial_btn_connected", False):
                    try:
                        self._safe_connect("pause_serial_btn", "toggled", self.toggle_serial_pause)
                    except Exception:
                        try:
                            self.pause_serial_btn.toggled.connect(self.toggle_serial_pause)
                        except Exception:
                            pass
                    try:
                        self._pause_serial_btn_connected = True
                    except Exception:
                        pass
            except Exception:
                pass
            try:
                if getattr(self, "clear_serial_btn", None) and not getattr(self, "_clear_serial_btn_connected", False):
                    try:
                        self._safe_connect("clear_serial_btn", "clicked", self.clear_serial_log)
                    except Exception:
                        try:
                            self.clear_serial_btn.clicked.connect(self.clear_serial_log)
                        except Exception:
                            pass
                    try:
                        self._clear_serial_btn_connected = True
                    except Exception:
                        pass
            except Exception:
                pass
            try:
                if getattr(self, "export_serial_btn", None) and not getattr(self, "_export_serial_btn_connected", False):
                    try:
                        self._safe_connect("export_serial_btn", "clicked", self.export_serial_log)
                    except Exception:
                        try:
                            self.export_serial_btn.clicked.connect(self.export_serial_log)
                        except Exception:
                            pass
                    try:
                        self._export_serial_btn_connected = True
                    except Exception:
                        pass
            except Exception:
                pass
            try:
                if getattr(self, "pause_serial_tx_btn", None) and not getattr(self, "_pause_serial_tx_btn_connected", False):
                    try:
                        self._safe_connect("pause_serial_tx_btn", "toggled", self.toggle_serial_tx)
                    except Exception:
                        try:
                            self.pause_serial_tx_btn.toggled.connect(self.toggle_serial_tx)
                        except Exception:
                            pass
                    try:
                        self._pause_serial_tx_btn_connected = True
                    except Exception:
                        pass
            except Exception:
                pass

            # Ensure writer marshals UI updates to the Qt main thread
            def _ui_writer(text):
                try:
                    # use central helper which respects pause/buffering
                    self._serial_write(text)
                except Exception:
                    try:
                        self.serial_output.append(text)
                    except Exception:
                        pass

            self.state_logger = StateLogger(writer=_ui_writer)
        except Exception:
            # fallback: create with no writer
            self.state_logger = StateLogger()
        # Reset styles before applying enhancements to ensure a clean slate
        self.reset_styles()

        try:
            self.load_settings()
            
            # ===== SET MODE 5 (BackSub+YOLO) AS DEFAULT ON FIRST RUN =====
            # If detection mode is still at 0 (Frame Difference), user hasn't customized it yet.
            # Set to Mode 5 (BackSub + YOLO) for best tracking performance.
            try:
                current_mode = self._safe_current_index("detection_mode_combo", 0)
                # Check if settings file exists (not first run if it does)
                import os
                settings_exists = os.path.isfile(self.SETTINGS_FILE)
                
                if not settings_exists and current_mode == 0:
                    # First run: set default to Mode 5 (BackSub + YOLO)
                    self.detection_mode_combo.setCurrentIndex(5)
                    self.save_settings()  # Persist the new default
                    try:
                        if hasattr(self, "enhancer"):
                            self.enhancer.log_serial_output(
                                "[INIT] First run: Set detection mode to Mode 5 (BackSub + YOLO - Best)",
                                fire=False
                            )
                    except Exception:
                        print("[INIT] First run: Set detection mode to Mode 5 (BackSub + YOLO - Best)")
            except Exception:
                pass
            
            # Only call update_mode when enhancer initialized
            try:
                if getattr(self, 'enhancer', None):
                    self.enhancer.update_mode(self.detection_mode_combo.currentText())
            except Exception:
                pass
            try:
                # Attempt to auto-load the preferred layout (if present)
                self.auto_load_default_layout()
            except Exception:
                pass
        except Exception as e:
            # store the error to show later in the UI
            self._load_error_message = str(e)

        try:
            # Ensure main window can receive keyboard focus for shortcuts
            try:
                self.setFocusPolicy(Qt.StrongFocus)
                self.setFocus()
            except Exception:
                try:
                    self.setFocus()
                except Exception:
                    pass
        except Exception:
            pass

        # Diagnostic: enumerate presence of important widgets and exposed signals
        try:
            self._debug_widget_signal_presence()
        except Exception:
            pass

        # Timers
        self.timer = QTimer(self)
        try:
            self._safe_connect("timer", "timeout", self.update_frame)
        except Exception:
            try:
                try:
                    if not self._safe_connect("timer", "timeout", self.update_frame):
                        try:
                            # Guarded direct connect fallback
                            sig = getattr(getattr(self, "timer", None), "timeout", None)
                            conn = getattr(sig, "connect", None)
                            if callable(conn):
                                conn(self.update_frame)
                        except Exception:
                            pass
                except Exception:
                    pass
            except Exception:
                pass
        # Start frame timer with error handling to detect silent failures
        try:
            self.timer.start(30)
            if not self.timer.isActive():
                try:
                    if hasattr(self, "enhancer"):
                        self.enhancer.log_serial_output(
                            "⚠️ CRITICAL: Frame timer failed to start! Detection will not run.",
                            fire=False,
                        )
                except Exception:
                    pass
        except Exception as e:
            try:
                if hasattr(self, "enhancer"):
                    self.enhancer.log_serial_output(
                        f"⚠️ CRITICAL: Frame timer start exception: {e}",
                        fire=False,
                    )
            except Exception:
                pass

        self.serial_timer = QTimer(self)
        try:
            self._safe_connect("serial_timer", "timeout", self.send_serial_command)
        except Exception:
            try:
                try:
                    if not self._safe_connect(
                        "serial_timer", "timeout", self.send_serial_command
                    ):
                        try:
                            sig = getattr(
                                getattr(self, "serial_timer", None), "timeout", None
                            )
                            conn = getattr(sig, "connect", None)
                            if callable(conn):
                                conn(self.send_serial_command)
                        except Exception:
                            pass
                except Exception:
                    pass
            except Exception:
                pass

        # Auto-toggle Force Exact Dock Widths at startup to equalize panel columns
        # Use a single-shot timer to execute after window is fully initialized
        try:
            QTimer.singleShot(500, self._auto_equalize_docks_on_startup)
        except Exception:
            pass

    def _calculate_max_contour_for_resolution(self, resolution_label="640x480 (Fast)"):
        """
        Calculate appropriate max_contour threshold based on selected resolution.
        Returns the max pixel count that represents 85% of frame area (to avoid large objects/shadows).
        """
        try:
            # Get resolution dimensions
            if resolution_label not in self.frame_ratio_options:
                resolution_label = "640x480 (Fast)"  # Fallback
            
            width, height = self.frame_ratio_options[resolution_label]
            frame_area = width * height
            
            # Use 85% of total frame area as default max_contour threshold
            max_contour = int(frame_area * 0.85)
            
            return max_contour
        except Exception as e:
            print(f"[RES-CALC] Error calculating max_contour: {e}")
            return 1400000  # Safe fallback for 1920x1080
    
    def _auto_equalize_docks_on_startup(self):
        """
        Auto-toggle Force Exact Dock Widths to equalize panel columns at startup.
        This is called via QTimer.singleShot after window initialization is complete.
        """
        try:
            if getattr(self, "force_exact_action", None) is not None:
                # Enable it first (will apply fixed widths)
                try:
                    self.force_exact_action.setChecked(True)
                    self.force_exact_dock_widths = True
                    self.equalize_dock_columns()
                except Exception:
                    pass
                # Then disable it (will remove fixed constraints but keep equalized widths)
                try:
                    self.force_exact_action.setChecked(False)
                    self.force_exact_dock_widths = False
                    # Remove max-width constraints so layout becomes flexible again
                    docks = [d for d in self.findChildren(QDockWidget)]
                    for d in docks:
                        try:
                            d.setMaximumWidth(16777215)
                        except Exception:
                            pass
                        try:
                            w = d.widget()
                            if w is not None:
                                try:
                                    w.setMaximumWidth(16777215)
                                except Exception:
                                    pass
                                try:
                                    w.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                                except Exception:
                                    pass
                        except Exception:
                            pass
                    self.equalize_dock_columns()
                except Exception:
                    pass
        except Exception:
            pass
    
    def _assert_widgets_initialized(self):
        """Assert the presence of key widgets so static analysis tools know
        these attributes are not None after UI initialization.
        """
        assert self.video_label is not None
        assert self.sniper_view_label is not None
        assert self.tracking_btn is not None
        assert self.aiming_btn is not None
        assert self.home_pan_input is not None
        assert self.home_tilt_input is not None
        assert self.go_home_button is not None
        assert self.pan_min_input is not None
        assert self.pan_max_input is not None
        assert self.tilt_min_input is not None
        assert self.tilt_max_input is not None
        assert self.detection_mode_combo is not None
        assert self.yolo_model_combo is not None
        assert self.yolo_confidence_input is not None
        assert self.yolo_classes_input is not None
        assert self.open_trainer_btn is not None
        assert self.lost_hold_input is not None
        assert self.hold_infinite_checkbox is not None
        assert self.snap_threshold_slider is not None
        assert self.smoothing_input is not None
        assert self.movement_sensitivity_slider is not None
        assert self.tracking_speed_slider is not None
        assert self.manual_speed_slider is not None
        assert self.position_label is not None
        assert self.serial_output is not None
        # Additional network/serial UI controls often referenced
        if hasattr(self, "connect_button"):
            assert self.connect_button is not None
        if hasattr(self, "com_port_input"):
            assert self.com_port_input is not None
        if hasattr(self, "baud_rate_input"):
            assert self.baud_rate_input is not None
        self.serial_timer.start(50)
        # ==========================================
        # POLISHED GLOBAL UI THEME
        # ==========================================
        self.setStyleSheet(
            """
        QMainWindow {
            background-color: #101010;
        }

        QWidget {
            background-color: #151515;
            color: #e0e0e0;
            font-family: 'Segoe UI';
            /* slightly smaller font so labels and controls fit better */
            font-size: 9.0pt;
            border: none;
        }

        QGroupBox {
            border: 1px solid #888;
            border-radius: 10px;
            margin-top: 10px;
            font-weight: bold;
            color: #eaeaea;
            padding: 8px;
        }

        QPushButton {
            background-color: #222;
            color: #f0f0f0;
            border: 1px solid #888;
            border-radius: 8px;
            /* reduced padding and a small min-height to keep buttons compact */
            padding: 2px 6px;
            min-height: 22px;
        }

        QPushButton:hover {
            background-color: #2e2e2e;
        }

        QPushButton:checked {
            background-color: #ff3333;
            border: 1px solid #ff5555;
            color: #fff;
        }

        QLabel {
            color: #eaeaea;
        }

        QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox {
            background-color: #1d1d1d;
            color: #f0f0f0;
            border: 1px solid #666;
            border-radius: 6px;
            /* slightly reduced padding and enforce a small min-height */
            padding: 2px;
            min-height: 20px;
        }

        QTextEdit, QPlainTextEdit {
            background-color: #0d0d0d;
            color: #00ff88;
            border: 1px solid #666;
            border-radius: 8px;
            font-family: Consolas;
            font-size: 10pt;
        }

        QStatusBar {
            background-color: #181818;
            border-top: 1px solid #666;
            color: #00ff99;
            font-family: Consolas;
            font-size: 10pt;
        }

        QDockWidget::title {
            background-color: #202020;
            border: 1px solid #555;
            border-radius: 8px;
            padding: 4px;
            color: #ccc;
        }

        QScrollBar:vertical {
            background: #1a1a1a;
            width: 12px;
        }

        QScrollBar::handle:vertical {
            background: #555;
            border-radius: 6px;
        }

        QScrollBar::handle:vertical:hover {
            background: #777;
        }
        
        /* pressed state for buttons and improved checkbox visibility */
        QPushButton:pressed {
            background-color: #1f1f1f;
            border: 1px solid #aaa;
            color: #ffffff;
        }

        QCheckBox {
            color: #eaeaea;
        }
        QCheckBox::indicator {
            width: 16px;
            height: 16px;
            border-radius: 3px;
            background-color: #1d1d1d;
            border: 1px solid #666;
        }
        QCheckBox::indicator:checked {
            background-color: #ff3333;
            border: 1px solid #ff5555;
        }
        
        /* Tooltip styling - light background with dark text for readability */
        QToolTip {
            background-color: #FFFACD;
            color: #000000;
            border: 1px solid #666;
            border-radius: 4px;
            padding: 3px 6px;
            font-size: 10pt;
            font-family: 'Segoe UI';
        }
        """
        )

    def init_ui(self):
        # Authoritative UI builder
        self.setWindowTitle("AUTO TURRET CONTROL SYSTEM")

        try:
            QApplication.setStyle(QStyleFactory.create("Fusion"))
        except Exception:
            pass
        try:
            self._apply_tooltip_styles_and_texts()
        except Exception:
            pass
        # Create video frame first since it's referenced in shortcut tabs
        self.video_frame = QFrame()
        video_layout = QVBoxLayout(self.video_frame)
        video_layout.setContentsMargins(0, 0, 0, 0)

        if getattr(self, "video_label", None) is None:
            self.video_label = QLabel()
        try:
            lbl = getattr(self, "video_label", None)
            if lbl is not None:
                try:
                    try:
                        lbl.setAlignment(cast(Any, getattr(Qt, "AlignCenter", 0)))
                    except Exception:
                        pass
                    lbl.setText("No Camera Feed")
                except Exception:
                    pass
        except Exception:
            pass

        # use safe widget caller for methods that static analyzer may flag
        try:
            self._safe_widget_call("video_label", "setScaledContents", False)
            self._safe_widget_call(
                "video_label",
                "setSizePolicy",
                QSizePolicy.Expanding,
                QSizePolicy.Expanding,
            )
        except Exception:
            pass
        video_layout.addWidget(self.video_label)
        # Ensure core detection widgets exist early so load_settings() can apply saved values.
        try:
            if getattr(self, "min_contour_input", None) is None:
                self.min_contour_input = QSpinBox()
                try:
                    # sensible defaults; actual UI layout will place this widget later
                    self.min_contour_input.setRange(0, 2000000)
                    self.min_contour_input.setSingleStep(50)
                    self.min_contour_input.setValue(300)
                    self.min_contour_input.setSuffix(" px")
                except Exception:
                    pass
                try:
                    self._safe_connect("min_contour_input", "valueChanged", self.save_settings)
                except Exception:
                    pass
        except Exception:
            pass
        
        # Maximum contour size control - allows filtering out large objects
        try:
            if getattr(self, "max_contour_input", None) is None:
                self.max_contour_input = QSpinBox()
                try:
                    # sensible defaults; actual UI layout will place this widget later
                    # Calculate max_contour based on current resolution setting
                    self.max_contour_input.setRange(100, 2000000)
                    self.max_contour_input.setSingleStep(50)
                    initial_max_contour = self._calculate_max_contour_for_resolution(self.frame_ratio_setting)
                    self.max_contour_input.setValue(initial_max_contour)
                    self.max_contour_input.setSuffix(" px")
                except Exception:
                    pass
                try:
                    self._safe_connect("max_contour_input", "valueChanged", self.save_settings)
                except Exception:
                    pass
        except Exception:
            pass

        # Apply theme manager if present
        try:
            self.theme_manager = getattr(self, "theme_manager", ThemeManager())
            try:
                self.theme_manager.apply_theme("dark")
            except Exception:
                pass
        except Exception:
            pass
        
        # Force tooltip styling after theme is applied to ensure visibility
        try:
            app = QApplication.instance()
            if app is not None:
                current_style = app.styleSheet()
                app.setStyleSheet(current_style + """
                    QToolTip {
                        background-color: #FFFACD !important;
                        color: #000000 !important;
                        border: 1px solid #666;
                        padding: 4px;
                        font-size: 9pt;
                    }
                """)
        except Exception:
            pass

        # Initialize shortcut and notes tabs with the video frame
        self._init_shortcut_and_notes_tabs()

        # Sniper view dock (hidden by default)
        if getattr(self, "sniper_dock", None) is None:
            self.sniper_dock = QDockWidget("Sniper Scope", self)
        self.sniper_dock.setObjectName("SniperScopeDock")
        
        # Create sniper container with video label and zoom control
        sniper_container = QWidget()
        sniper_layout = QVBoxLayout()
        sniper_layout.setSpacing(6)
        sniper_layout.setContentsMargins(6, 6, 6, 6)
        
        # Zoom control
        zoom_control_layout = QHBoxLayout()
        zoom_control_layout.addWidget(QLabel("Zoom:"))
        if getattr(self, "sniper_zoom_slider", None) is None:
            self.sniper_zoom_slider = QSlider(Qt.Horizontal)
            self.sniper_zoom_slider.setRange(5, 40)  # 0.5x to 4.0x
            self.sniper_zoom_slider.setValue(10)  # Default 1.0x
            self.sniper_zoom_slider.setTickPosition(QSlider.TicksBelow)
            self.sniper_zoom_slider.setTickInterval(5)
        zoom_control_layout.addWidget(self.sniper_zoom_slider)
        if getattr(self, "sniper_zoom_label", None) is None:
            self.sniper_zoom_label = QLabel("1.0x")
            self.sniper_zoom_label.setMinimumWidth(40)
            self.sniper_zoom_label.setStyleSheet("color: #00ff99;")
        zoom_control_layout.addWidget(self.sniper_zoom_label)
        sniper_layout.addLayout(zoom_control_layout)
        
        # Video display label
        if getattr(self, "sniper_view_label", None) is None:
            self.sniper_view_label = QLabel("No Target")
        try:
            sv = getattr(self, "sniper_view_label", None)
            if sv is not None:
                try:
                    try:
                        sv.setAlignment(cast(Any, getattr(Qt, "AlignCenter", 0)))
                    except Exception:
                        pass
                except Exception:
                    pass
                try:
                    self._safe_widget_call(
                        "sniper_view_label", "setScaledContents", True
                    )
                except Exception:
                    pass
                try:
                    sv.setStyleSheet("background-color: black; border: 2px solid #444;")
                except Exception:
                    pass
        except Exception:
            pass
        sniper_layout.addWidget(self.sniper_view_label)
        sniper_container.setLayout(sniper_layout)
        
        try:
            def on_sniper_zoom_changed(val):
                try:
                    zoom = val / 10.0
                    self.sniper_zoom_label.setText(f"{zoom:.1f}x")
                except Exception:
                    pass
            self.sniper_zoom_slider.valueChanged.connect(on_sniper_zoom_changed)
        except Exception:
            pass
        
        try:
            self.sniper_dock.setWidget(sniper_container)
        except Exception:
            pass
        # Make sniper dock behave like other widgets: allow closing, floating,
        # and resizing when floating. Install an event filter so we can detect
        # user-initiated closes and respect that intent (don't auto-reopen).
        try:
            # Allow all features (movable/floatable/closable/tabable)
            try:
                self.sniper_dock.setFeatures(QDockWidget.AllDockWidgetFeatures)
            except Exception:
                try:
                    # Fallback: at least allow movable/floatable/closable
                    self.sniper_dock.setFeatures(
                        QDockWidget.DockWidgetMovable
                        | QDockWidget.DockWidgetFloatable
                        | QDockWidget.DockWidgetClosable
                    )
                except Exception:
                    pass
            # Make label expand so floating sniper windows are resizable
            try:
                self._safe_widget_call(
                    "sniper_view_label", "setSizePolicy", QSizePolicy.Expanding, QSizePolicy.Expanding
                )
            except Exception:
                pass
            try:
                sv = getattr(self, "sniper_view_label", None)
                if sv is not None:
                    try:
                        sv.setMinimumSize(120, 60)
                    except Exception:
                        pass
            except Exception:
                pass
            # Track whether the user explicitly closed the sniper dock so we
            # don't auto-show it against their wishes.
            try:
                self._sniper_user_closed = False
            except Exception:
                pass
            try:
                # Install event filter to capture Close events from the dock
                # (user clicking the close button triggers a QEvent.Close).
                try:
                    self.sniper_dock.installEventFilter(self)
                except Exception:
                    pass
            except Exception:
                pass
        except Exception:
            pass
        # Initially hide until first use (preserve older behavior)
        try:
            self.sniper_dock.hide()
        except Exception:
            pass

        # ===== SCOPE VISUAL SETTINGS FLOATING WINDOW =====
        try:
            if getattr(self, "scope_settings_window", None) is None:
                self.scope_settings_window = QMainWindow()
                self.scope_settings_window.setWindowTitle("Scope Visual Settings")
                self.scope_settings_window.setGeometry(100, 100, 550, 650)
                
                scope_widget = QWidget()
                scope_layout = QGridLayout()
                scope_layout.setSpacing(8)
                scope_layout.setContentsMargins(12, 12, 12, 12)
                
                r = 0
                
                # Crosshair Length (5-50% of frame, default 30%)
                scope_layout.addWidget(QLabel("Crosshair Length %:"), r, 0)
                self.crosshair_length_slider = QSlider(Qt.Horizontal)
                self.crosshair_length_slider.setRange(5, 50)
                self.crosshair_length_slider.setValue(30)
                self.crosshair_length_slider.setTickPosition(QSlider.TicksBelow)
                self.crosshair_length_slider.setTickInterval(5)
                self.crosshair_length_label = QLabel("30%")
                self.crosshair_length_label.setMinimumWidth(35)
                self.crosshair_length_label.setStyleSheet("color: #00ff99;")
                
                def on_crosshair_length_changed(val):
                    self.crosshair_length_label.setText(f"{val}%")
                    self.save_settings()
                self.crosshair_length_slider.valueChanged.connect(on_crosshair_length_changed)
                scope_layout.addWidget(self.crosshair_length_slider, r, 1)
                scope_layout.addWidget(self.crosshair_length_label, r, 2)
                r += 1
                
                # Center Gap (0-30, default 10)
                scope_layout.addWidget(QLabel("Center Gap:"), r, 0)
                self.gap_slider = QSlider(Qt.Horizontal)
                self.gap_slider.setRange(0, 30)
                self.gap_slider.setValue(10)
                self.gap_slider.setTickPosition(QSlider.TicksBelow)
                self.gap_slider.setTickInterval(3)
                self.gap_label = QLabel("10")
                self.gap_label.setMinimumWidth(35)
                self.gap_label.setStyleSheet("color: #00ff99;")
                
                def on_gap_changed(val):
                    self.gap_label.setText(str(val))
                    self.save_settings()
                self.gap_slider.valueChanged.connect(on_gap_changed)
                scope_layout.addWidget(self.gap_slider, r, 1)
                scope_layout.addWidget(self.gap_label, r, 2)
                r += 1
                
                # Crosshair Thickness (1-4, default 2)
                scope_layout.addWidget(QLabel("Crosshair Thickness:"), r, 0)
                self.crosshair_thickness_slider = QSlider(Qt.Horizontal)
                self.crosshair_thickness_slider.setRange(1, 4)
                self.crosshair_thickness_slider.setValue(2)
                self.crosshair_thickness_slider.setTickPosition(QSlider.TicksBelow)
                self.crosshair_thickness_slider.setTickInterval(1)
                self.crosshair_thickness_label = QLabel("2")
                self.crosshair_thickness_label.setMinimumWidth(35)
                self.crosshair_thickness_label.setStyleSheet("color: #00ff99;")
                
                def on_thickness_changed(val):
                    self.crosshair_thickness_label.setText(str(val))
                    self.save_settings()
                self.crosshair_thickness_slider.valueChanged.connect(on_thickness_changed)
                scope_layout.addWidget(self.crosshair_thickness_slider, r, 1)
                scope_layout.addWidget(self.crosshair_thickness_label, r, 2)
                r += 1
                
                # Scope Radius % (25-50, default 35)
                scope_layout.addWidget(QLabel("Scope Radius %:"), r, 0)
                self.scope_radius_percent_slider = QSlider(Qt.Horizontal)
                self.scope_radius_percent_slider.setRange(25, 50)
                self.scope_radius_percent_slider.setValue(35)
                self.scope_radius_percent_slider.setTickPosition(QSlider.TicksBelow)
                self.scope_radius_percent_slider.setTickInterval(5)
                self.scope_radius_percent_label = QLabel("35%")
                self.scope_radius_percent_label.setMinimumWidth(35)
                self.scope_radius_percent_label.setStyleSheet("color: #00ff99;")
                
                def on_scope_radius_changed(val):
                    self.scope_radius_percent_label.setText(f"{val}%")
                    self.save_settings()
                self.scope_radius_percent_slider.valueChanged.connect(on_scope_radius_changed)
                scope_layout.addWidget(self.scope_radius_percent_slider, r, 1)
                scope_layout.addWidget(self.scope_radius_percent_label, r, 2)
                r += 1
                
                # Corner Size (20-80, default 40)
                scope_layout.addWidget(QLabel("Corner Size:"), r, 0)
                self.corner_size_slider = QSlider(Qt.Horizontal)
                self.corner_size_slider.setRange(20, 80)
                self.corner_size_slider.setValue(40)
                self.corner_size_slider.setTickPosition(QSlider.TicksBelow)
                self.corner_size_slider.setTickInterval(5)
                self.corner_size_label = QLabel("40")
                self.corner_size_label.setMinimumWidth(35)
                self.corner_size_label.setStyleSheet("color: #00ff99;")
                
                def on_corner_size_changed(val):
                    self.corner_size_label.setText(str(val))
                    self.save_settings()
                self.corner_size_slider.valueChanged.connect(on_corner_size_changed)
                scope_layout.addWidget(self.corner_size_slider, r, 1)
                scope_layout.addWidget(self.corner_size_label, r, 2)
                r += 1
                
                # Status Text Scale (8-15 for 0.8-1.5, default 12 for 1.2)
                scope_layout.addWidget(QLabel("Status Text Scale:"), r, 0)
                self.status_text_scale_slider = QSlider(Qt.Horizontal)
                self.status_text_scale_slider.setRange(8, 15)
                self.status_text_scale_slider.setValue(12)
                self.status_text_scale_slider.setTickPosition(QSlider.TicksBelow)
                self.status_text_scale_slider.setTickInterval(1)
                self.status_text_scale_label = QLabel("1.2")
                self.status_text_scale_label.setMinimumWidth(35)
                self.status_text_scale_label.setStyleSheet("color: #00ff99;")
                
                def on_text_scale_changed(val):
                    scale = val / 10.0
                    self.status_text_scale_label.setText(f"{scale:.1f}")
                    self.save_settings()
                self.status_text_scale_slider.valueChanged.connect(on_text_scale_changed)
                scope_layout.addWidget(self.status_text_scale_slider, r, 1)
                scope_layout.addWidget(self.status_text_scale_label, r, 2)
                r += 1
                
                # Vignette Opacity (0-100, default 50)
                scope_layout.addWidget(QLabel("Vignette Opacity:"), r, 0)
                self.vignette_opacity_slider_scope = QSlider(Qt.Horizontal)
                self.vignette_opacity_slider_scope.setRange(0, 100)
                self.vignette_opacity_slider_scope.setValue(50)
                self.vignette_opacity_slider_scope.setTickPosition(QSlider.TicksBelow)
                self.vignette_opacity_slider_scope.setTickInterval(10)
                self.vignette_opacity_label_scope = QLabel("50%")
                self.vignette_opacity_label_scope.setMinimumWidth(35)
                self.vignette_opacity_label_scope.setStyleSheet("color: #00ff99;")
                
                def on_vignette_opacity_scope_changed(val):
                    self.vignette_opacity_label_scope.setText(f"{val}%")
                    self.save_settings()
                self.vignette_opacity_slider_scope.valueChanged.connect(on_vignette_opacity_scope_changed)
                scope_layout.addWidget(self.vignette_opacity_slider_scope, r, 1)
                scope_layout.addWidget(self.vignette_opacity_label_scope, r, 2)
                r += 1
                
                # Text BG Opacity (0-100, default 100)
                scope_layout.addWidget(QLabel("Text BG Opacity:"), r, 0)
                self.text_bg_opacity_slider_scope = QSlider(Qt.Horizontal)
                self.text_bg_opacity_slider_scope.setRange(0, 100)
                self.text_bg_opacity_slider_scope.setValue(100)
                self.text_bg_opacity_slider_scope.setTickPosition(QSlider.TicksBelow)
                self.text_bg_opacity_slider_scope.setTickInterval(10)
                self.text_bg_opacity_label_scope = QLabel("100%")
                self.text_bg_opacity_label_scope.setMinimumWidth(35)
                self.text_bg_opacity_label_scope.setStyleSheet("color: #00ff99;")
                
                def on_text_bg_opacity_scope_changed(val):
                    self.text_bg_opacity_label_scope.setText(f"{val}%")
                    self.save_settings()
                self.text_bg_opacity_slider_scope.valueChanged.connect(on_text_bg_opacity_scope_changed)
                scope_layout.addWidget(self.text_bg_opacity_slider_scope, r, 1)
                scope_layout.addWidget(self.text_bg_opacity_label_scope, r, 2)
                r += 1
                
                # Preset Buttons
                scope_layout.addWidget(QLabel("─" * 50), r, 0, 1, 3)
                r += 1
                scope_layout.addWidget(QLabel("Presets:"), r, 0, 1, 3)
                r += 1
                
                def apply_cinematic_preset():
                    self.crosshair_length_slider.setValue(25)
                    self.gap_slider.setValue(5)
                    self.crosshair_thickness_slider.setValue(1)
                    self.scope_radius_percent_slider.setValue(40)
                    self.corner_size_slider.setValue(50)
                    self.status_text_scale_slider.setValue(13)
                    self.vignette_opacity_slider_scope.setValue(30)
                    self.text_bg_opacity_slider_scope.setValue(80)
                
                def apply_tactical_preset():
                    self.crosshair_length_slider.setValue(35)
                    self.gap_slider.setValue(12)
                    self.crosshair_thickness_slider.setValue(2)
                    self.scope_radius_percent_slider.setValue(35)
                    self.corner_size_slider.setValue(40)
                    self.status_text_scale_slider.setValue(10)
                    self.vignette_opacity_slider_scope.setValue(60)
                    self.text_bg_opacity_slider_scope.setValue(100)
                
                def apply_precision_preset():
                    self.crosshair_length_slider.setValue(40)
                    self.gap_slider.setValue(15)
                    self.crosshair_thickness_slider.setValue(3)
                    self.scope_radius_percent_slider.setValue(30)
                    self.corner_size_slider.setValue(30)
                    self.status_text_scale_slider.setValue(9)
                    self.vignette_opacity_slider_scope.setValue(70)
                    self.text_bg_opacity_slider_scope.setValue(90)
                
                def reset_to_tactical():
                    apply_tactical_preset()
                
                cinema_btn = QPushButton("Cinematic")
                cinema_btn.clicked.connect(apply_cinematic_preset)
                cinema_btn.setStyleSheet("background-color: #2d2d2d; color: #00ff99; border: 1px solid #444; padding: 5px;")
                scope_layout.addWidget(cinema_btn, r, 0)
                
                tactical_btn = QPushButton("Tactical")
                tactical_btn.clicked.connect(apply_tactical_preset)
                tactical_btn.setStyleSheet("background-color: #2d2d2d; color: #00ff99; border: 1px solid #444; padding: 5px;")
                scope_layout.addWidget(tactical_btn, r, 1)
                
                precision_btn = QPushButton("Precision")
                precision_btn.clicked.connect(apply_precision_preset)
                precision_btn.setStyleSheet("background-color: #2d2d2d; color: #00ff99; border: 1px solid #444; padding: 5px;")
                scope_layout.addWidget(precision_btn, r, 2)
                r += 1
                
                reset_btn = QPushButton("Reset to Tactical")
                reset_btn.clicked.connect(reset_to_tactical)
                reset_btn.setStyleSheet("background-color: #2d2d2d; color: #ffaa00; border: 1px solid #555; padding: 7px; font-weight: bold;")
                scope_layout.addWidget(reset_btn, r, 0, 1, 3)
                
                scope_widget.setLayout(scope_layout)
                scope_widget.setStyleSheet("background-color: #1a1a1a; color: white;")
                self.scope_settings_window.setCentralWidget(scope_widget)
                self.scope_settings_window.setStyleSheet("background-color: #1a1a1a; color: white;")
                self.scope_settings_window.hide()
        except Exception as e:
            print(f"[WARN] Failed to create scope settings window: {e}")

        # --- Build panels (create all names that load_settings expects) ---
        # Configuration & Connection
        settings_group = QGroupBox("Configuration & Connection")
        settings_layout = QGridLayout()
        settings_layout.setSpacing(6)
        settings_layout.setContentsMargins(8, 8, 8, 8)
        settings_layout.addWidget(QLabel("COM Port:"), 0, 0)
        if getattr(self, "com_port_input", None) is None:
            self.com_port_input = QLineEdit()
        try:
            if not getattr(self.com_port_input, "text", lambda: "")():
                self.com_port_input.setText("COM3")
        except Exception:
            pass
        settings_layout.addWidget(self.com_port_input, 0, 1)
        settings_layout.addWidget(QLabel("Baud Rate:"), 1, 0)
        if getattr(self, "baud_rate_input", None) is None:
            self.baud_rate_input = QSpinBox()
        try:
            if getattr(self, "baud_rate_input", None) is not None:
                try:
                    self._safe_widget_call("baud_rate_input", "setRange", 2400, 115200)
                    # prefer safe call for setValue too
                    self._safe_widget_call("baud_rate_input", "setValue", 115200)
                except Exception:
                    pass
        except Exception:
            pass
        settings_layout.addWidget(self.baud_rate_input, 1, 1)
        if getattr(self, "connect_button", None) is None:
            self.connect_button = QPushButton("Connect")
        try:
            btn = getattr(self, "connect_button", None)
            if btn is not None:
                try:
                    try:
                        self._safe_connect(
                            "connect_button",
                            "clicked",
                            lambda: self.handle_connect_sound(),
                        )
                    except Exception:
                        try:
                            try:
                                if not self._safe_connect_path(
                                    "sound_connect_btn",
                                    "clicked",
                                    lambda: self.handle_connect_sound(),
                                ):
                                    try:
                                        try:
                                            # prefer _safe_connect for signal objects
                                            if not self._safe_connect(
                                                "btn",
                                                "clicked",
                                                lambda: self.handle_connect_sound(),
                                            ):
                                                try:
                                                    try:
                                                        if not self._safe_connect(
                                                            "connect_button",
                                                            "clicked",
                                                            lambda: self.handle_connect_sound(),
                                                        ):
                                                            sig = getattr(
                                                                btn, "clicked", None
                                                            )
                                                            conn = getattr(
                                                                sig, "connect", None
                                                            )
                                                            if callable(conn):
                                                                conn(
                                                                    lambda: self.handle_connect_sound()
                                                                )
                                                    except Exception:
                                                        pass
                                                except Exception:
                                                    pass
                                        except Exception:
                                            pass
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                        except Exception:
                            pass
                except Exception:
                    pass
        except Exception:
            pass
        settings_layout.addWidget(self.connect_button, 2, 0, 1, 2)

        if getattr(self, "sound_checkbox", None) is None:
            self.sound_checkbox = QCheckBox("Sound Effects")
        try:
            scb = getattr(self, "sound_checkbox", None)
            if scb is not None:
                try:
                    scb.setChecked(bool(getattr(self, "sound_enabled", True)))
                except Exception:
                    pass
                try:
                    scb.setToolTip("Toggle UI sound effects (notifications and alerts).")
                except Exception:
                    pass
                try:
                    try:
                        self._safe_connect(
                            "sound_checkbox",
                            "stateChanged",
                            lambda s: self.set_sound_enabled(s),
                        )
                    except Exception:
                        try:
                            try:
                                if not self._safe_connect_path(
                                    "sound_checkbox",
                                    "stateChanged",
                                    lambda s: self.set_sound_enabled(s),
                                ):
                                    try:
                                        try:
                                            if not self._safe_connect(
                                                "scb",
                                                "stateChanged",
                                                lambda s: self.set_sound_enabled(s),
                                            ):
                                                try:
                                                    try:
                                                        if not self._safe_connect(
                                                            "sound_checkbox",
                                                            "stateChanged",
                                                            lambda s: self.set_sound_enabled(
                                                                s
                                                            ),
                                                        ):
                                                            sig = getattr(
                                                                scb,
                                                                "stateChanged",
                                                                None,
                                                            )
                                                            conn = getattr(
                                                                sig, "connect", None
                                                            )
                                                            if callable(conn):
                                                                conn(
                                                                    lambda s: self.set_sound_enabled(
                                                                        s
                                                                    )
                                                                )
                                                    except Exception:
                                                        pass
                                                except Exception:
                                                    pass
                                        except Exception:
                                            pass
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                        except Exception:
                            pass
                except Exception:
                    pass
        except Exception:
            pass
        settings_layout.addWidget(self.sound_checkbox, 3, 0, 1, 2)

        # Small status label to show override/suspend states (manual, go-home, hold)
        self.override_status_label = QLabel("")
        try:
            try:
                self.override_status_label.setAlignment(
                    cast(Any, getattr(Qt, "AlignCenter", 0))
                )
            except Exception:
                pass
        except Exception:
            pass
        settings_layout.addWidget(self.override_status_label, 6, 0, 1, 2)

        # Camera selection (allow user to prefer a specific camera index or use Auto)
        if getattr(self, "camera_index_combo", None) is None:
            self.camera_index_combo = QComboBox()
            try:
                if self.camera_index_combo.count() == 0:
                    self.camera_index_combo.addItems(["Auto", "0", "1", "2", "3", "4"])
            except Exception:
                pass
        settings_layout.addWidget(self.camera_index_combo, 5, 1)

        # Tracking toggle (replaces separate Start/Stop buttons)
        if getattr(self, "tracking_btn", None) is None:
            self.tracking_btn = QPushButton("Start Tracking")
            try:
                self.tracking_btn.setCheckable(True)
            except Exception:
                pass
        try:
            try:
                # Use 'toggled' for checkable toggle buttons to avoid double-press issues
                self._safe_connect("tracking_btn", "toggled", self.toggle_tracking)
            except Exception:
                # Best-effort fallback to direct signal connect
                try:
                    btn = getattr(self, "tracking_btn", None)
                    if btn is not None:
                        sig = getattr(btn, "toggled", None)
                        conn = getattr(sig, "connect", None)
                        if callable(conn):
                            conn(self.toggle_tracking)
                except Exception:
                    pass
        except Exception:
            pass

        # Aiming toggle (repurposed from the old Stop Tracking button)
        if getattr(self, "aiming_btn", None) is None:
            self.aiming_btn = QPushButton("Start Aiming")
            try:
                self.aiming_btn.setCheckable(True)
            except Exception:
                pass
        try:
            try:
                # Use 'toggled' for checkable toggle buttons to avoid double-press issues
                self._safe_connect("aiming_btn", "toggled", self.toggle_aiming)
            except Exception:
                try:
                    btn2 = getattr(self, "aiming_btn", None)
                    if btn2 is not None:
                        sig = getattr(btn2, "toggled", None)
                        conn = getattr(sig, "connect", None)
                        if callable(conn):
                            conn(self.toggle_aiming)
                except Exception:
                    pass
        except Exception:
            pass

        # Place the tracking and aiming buttons in the settings layout
        try:
            settings_layout.addWidget(self.tracking_btn, 4, 0)
            settings_layout.addWidget(self.aiming_btn, 4, 1)
        except Exception:
            try:
                settings_layout.addWidget(self.tracking_btn, 4, 0)
            except Exception:
                pass
        settings_group.setLayout(settings_layout)

        # Home position
        home_group = QGroupBox("Home Position (°)")
        home_layout = QGridLayout()
        home_layout.setSpacing(6)
        home_layout.setContentsMargins(8, 8, 8, 8)
        
        # Row 0: Home Pan / Home Tilt / Go Home Button (redesigned 6-column layout)
        home_layout.addWidget(QLabel("Home Pan:"), 0, 0)
        if getattr(self, "home_pan_input", None) is None:
            self.home_pan_input = QSpinBox()
        try:
            try:
                self._safe_widget_call(
                    "home_pan_input", "setRange", self.PAN_MIN, self.PAN_MAX
                )
                self._safe_widget_call("home_pan_input", "setValue", self.HOME_PAN)
                self._safe_connect("home_pan_input", "valueChanged", self.save_settings)
            except Exception:
                pass
        except Exception:
            pass
        home_layout.addWidget(self.home_pan_input, 0, 1)
        home_layout.addWidget(QLabel("Home Tilt:"), 0, 2)
        if getattr(self, "home_tilt_input", None) is None:
            self.home_tilt_input = QSpinBox()
        try:
            try:
                self._safe_widget_call(
                    "home_tilt_input", "setRange", self.TILT_MIN, self.TILT_MAX
                )
                self._safe_widget_call("home_tilt_input", "setValue", self.HOME_TILT)
                self._safe_connect(
                    "home_tilt_input", "valueChanged", self.save_settings
                )
            except Exception:
                pass
        except Exception:
            pass
        home_layout.addWidget(self.home_tilt_input, 0, 3)
        if getattr(self, "go_home_button", None) is None:
            self.go_home_button = QPushButton("Go Home")
        try:
            go_btn = getattr(self, "go_home_button", None)
            if go_btn is not None:
                try:
                    try:
                        self._safe_connect("go_home_button", "clicked", self.go_home)
                    except Exception:
                        try:
                            try:
                                if not self._safe_connect_path(
                                    "go_home_btn", "clicked", self.go_home
                                ):
                                    try:
                                        try:
                                            if not self._safe_connect(
                                                "go_btn", "clicked", self.go_home
                                            ):
                                                try:
                                                    try:
                                                        if not self._safe_connect(
                                                            "go_home_button",
                                                            "clicked",
                                                            self.go_home,
                                                        ):
                                                            sig = getattr(
                                                                go_btn, "clicked", None
                                                            )
                                                            conn = getattr(
                                                                sig, "connect", None
                                                            )
                                                            if callable(conn):
                                                                conn(self.go_home)
                                                    except Exception:
                                                        pass
                                                except Exception:
                                                    pass
                                        except Exception:
                                            pass
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                        except Exception:
                            pass
                except Exception:
                    pass
        except Exception:
            pass
        home_layout.addWidget(self.go_home_button, 0, 4, 1, 2)
        
        # Row 1: Idle mode toggle button (full width)
        if getattr(self, "idle_mode_toggle_btn", None) is None:
            self.idle_mode_toggle_btn = ClickDetectButton("Enable Idle Mode")
        try:
            self.idle_mode_toggle_btn.setCheckable(True)
            self.idle_mode_toggle_btn.setEnabled(True)
            # Use the custom click handler instead of signals
            self.idle_mode_toggle_btn.set_click_handler(self.toggle_idle_mode)
            if getattr(self, "enhancer", None):
                self.enhancer.log_serial_output("[IDLE] Toggle button created with direct click detection", fire=False)
        except Exception as e:
            try:
                # Fallback: try old signal method
                sig = getattr(self.idle_mode_toggle_btn, "clicked", None)
                conn = getattr(sig, "connect", None)
                if callable(conn):
                    conn(self.toggle_idle_mode)
                    if getattr(self, "enhancer", None):
                        self.enhancer.log_serial_output("[IDLE] Toggle button fallback connection succeeded", fire=False)
            except Exception as fallback_err:
                if getattr(self, "enhancer", None):
                    self.enhancer.log_serial_output(f"[IDLE] Button connection failed: {str(fallback_err)}", fire=False)
        try:
            btn = getattr(self, "idle_mode_toggle_btn", None)
            if btn is not None and not btn.isEnabled():
                btn.setEnabled(True)
                if getattr(self, "enhancer", None):
                    self.enhancer.log_serial_output("[IDLE] Button was disabled, re-enabled", fire=False)
        except Exception:
            pass
        home_layout.addWidget(self.idle_mode_toggle_btn, 1, 0, 1, 6)
        
        # Row 2: Section header for target loss behavior
        header_loss = QLabel("═══ TARGET LOSS BEHAVIOR ═══")
        header_loss.setStyleSheet("color: #888; font-weight: bold; padding: 4px 0px;")
        home_layout.addWidget(header_loss, 2, 0, 1, 6)
        
        # Row 3: HOME return behavior and suppress detection
        try:
            home_layout.addWidget(QLabel("On lost target:"), 3, 0)
            if getattr(self, "home_return_mode_combo", None) is None:
                self.home_return_mode_combo = QComboBox()
                try:
                    self.home_return_mode_combo.addItems(
                        ["Immediate", "Slow", "Disabled"]
                    )
                except Exception:
                    pass
            try:
                # default selection from current attribute
                try:
                    idx = self.home_return_mode_combo.findText(
                        str(getattr(self, "home_return_mode", "Immediate"))
                    )
                    if idx != -1:
                        self.home_return_mode_combo.setCurrentIndex(idx)
                except Exception:
                    pass
                # persist when changed
                try:
                    self._safe_connect(
                        "home_return_mode_combo",
                        "currentIndexChanged",
                        self.save_settings,
                    )
                except Exception:
                    try:
                        sig = getattr(
                            self.home_return_mode_combo, "currentIndexChanged", None
                        )
                        conn = getattr(sig, "connect", None)
                        if callable(conn):
                            conn(self.save_settings)
                    except Exception:
                        pass
            except Exception:
                pass
            home_layout.addWidget(self.home_return_mode_combo, 3, 1, 1, 2)
            home_layout.addWidget(QLabel("Suppress detection (s):"), 3, 3)
            if getattr(self, "home_return_suspend_input", None) is None:
                self.home_return_suspend_input = QDoubleSpinBox()
                try:
                    self.home_return_suspend_input.setRange(0.0, 30.0)
                    self.home_return_suspend_input.setSingleStep(0.5)
                    self.home_return_suspend_input.setValue(
                        float(getattr(self, "home_move_suspend_seconds", 2.0))
                    )
                except Exception:
                    pass
            try:
                self._safe_connect(
                    "home_return_suspend_input", "valueChanged", self.save_settings
                )
            except Exception:
                try:
                    sig = getattr(self.home_return_suspend_input, "valueChanged", None)
                    conn = getattr(sig, "connect", None)
                    if callable(conn):
                        conn(self.save_settings)
                except Exception:
                    pass
            home_layout.addWidget(self.home_return_suspend_input, 3, 4, 1, 2)
        except Exception:
            pass
        
        # Row 4: Section header for idle mode settings
        header_idle = QLabel("═══ IDLE MODE SETTINGS ═══")
        header_idle.setStyleSheet("color: #888; font-weight: bold; padding: 4px 0px;")
        home_layout.addWidget(header_idle, 4, 0, 1, 6)
        
        # Row 5: Idle behavior and Guard movement speed (no crowding)
        try:
            home_layout.addWidget(QLabel("Idle behavior:"), 5, 0)
            if getattr(self, "idle_behavior_combo", None) is None:
                self.idle_behavior_combo = QComboBox()
                try:
                    # Display-friendly labels for new idle modes (no "Home" - not an idle mode)
                    self.idle_behavior_combo.addItems(["Rest", "Guard", "Watch", "Search"])
                except Exception:
                    pass
                    
                # Watch mode is now fully configured in Idle Settings window (Tools → ⚙️ Idle Settings)
                # Set Watch Position button has been removed - configure watch limits in Idle Settings instead
                    
            try:
                # Set default selection from current attribute (capitalize for display)
                try:
                    display = str(getattr(self, "idle_behavior", "home")).capitalize()
                    idx = self.idle_behavior_combo.findText(display)
                    if idx != -1:
                        self.idle_behavior_combo.setCurrentIndex(idx)
                except Exception:
                    pass
                # NOTE: Signal connection removed (11-12-2025)
                # We use polling in update_frame() instead to avoid conflicts
                # between signal-driven changes and polling-driven changes.
                # This prevents race conditions when button and combo both try to change mode.
            except Exception:
                pass
            home_layout.addWidget(self.idle_behavior_combo, 5, 1, 1, 2)
            
            # Guard mode movement speed slider (now properly placed in row 5 without crowding)
            home_layout.addWidget(QLabel("Guard Movement Speed:"), 5, 3)
            if getattr(self, "guard_speed_slider", None) is None:
                self.guard_speed_slider = QSlider(Qt.Horizontal)
                try:
                    self.guard_speed_slider.setRange(1, 100)
                    self.guard_speed_slider.setValue(50)
                    self.guard_speed_slider.setTickPosition(QSlider.TicksBelow)
                    self.guard_speed_slider.setTickInterval(10)
                    self.guard_speed_slider.setMaximumWidth(150)
                except Exception:
                    pass
            
            if getattr(self, "guard_speed_label", None) is None:
                self.guard_speed_label = QLabel("50%")
                try:
                    self.guard_speed_label.setMinimumWidth(30)
                    self.guard_speed_label.setStyleSheet("color: #00ff99; font-weight: bold;")
                except Exception:
                    pass
            
            try:
                def on_guard_speed_changed(value):
                    try:
                        self.guard_speed_label.setText(f"{value}%")
                        if self.idle_modes is not None:
                            self.idle_modes.guard_set_movement_speed(value)
                            self.save_settings()
                    except Exception:
                        pass
                
                self.guard_speed_slider.valueChanged.connect(on_guard_speed_changed)
            except Exception:
                pass
            home_layout.addWidget(self.guard_speed_slider, 5, 4)
            home_layout.addWidget(self.guard_speed_label, 5, 5)
        except Exception:
            pass
        home_group.setLayout(home_layout)

        # Servo limits
        limits_group = QGroupBox("Servo Limits (°)")
        limits_layout = QGridLayout()
        limits_layout.setSpacing(6)
        limits_layout.setContentsMargins(8, 8, 8, 8)
        limits_layout.addWidget(QLabel("PAN Min:"), 0, 0)
        if getattr(self, "pan_min_input", None) is None:
            self.pan_min_input = QSpinBox()
        try:
            try:
                self._safe_widget_call("pan_min_input", "setRange", 0, 180)
                self._safe_widget_call("pan_min_input", "setValue", self.PAN_MIN)
            except Exception:
                pass
        except Exception:
            pass
        limits_layout.addWidget(self.pan_min_input, 0, 1)
        limits_layout.addWidget(QLabel("PAN Max:"), 1, 0)
        if getattr(self, "pan_max_input", None) is None:
            self.pan_max_input = QSpinBox()
        try:
            try:
                self._safe_widget_call("pan_max_input", "setRange", 0, 270)
                self._safe_widget_call("pan_max_input", "setValue", self.PAN_MAX)
            except Exception:
                pass
        except Exception:
            pass
        limits_layout.addWidget(self.pan_max_input, 1, 1)
        limits_layout.addWidget(QLabel("TILT Min:"), 2, 0)
        if getattr(self, "tilt_min_input", None) is None:
            self.tilt_min_input = QSpinBox()
        try:
            try:
                self._safe_widget_call("tilt_min_input", "setRange", 0, 180)
                self._safe_widget_call("tilt_min_input", "setValue", self.TILT_MIN)
            except Exception:
                pass
        except Exception:
            pass
        limits_layout.addWidget(self.tilt_min_input, 2, 1)
        limits_layout.addWidget(QLabel("TILT Max:"), 3, 0)
        if getattr(self, "tilt_max_input", None) is None:
            self.tilt_max_input = QSpinBox()
        try:
            try:
                self._safe_widget_call("tilt_max_input", "setRange", 0, 180)
                self._safe_widget_call("tilt_max_input", "setValue", self.TILT_MAX)
            except Exception:
                pass
        except Exception:
            pass
        limits_layout.addWidget(self.tilt_max_input, 3, 1)
        if getattr(self, "apply_limits_button", None) is None:
            self.apply_limits_button = QPushButton("Apply New Limits")
        try:
            apply_btn = getattr(self, "apply_limits_button", None)
            if apply_btn is not None:
                try:
                    try:
                        self._safe_connect(
                            "apply_limits_button", "clicked", self.apply_new_limits
                        )
                    except Exception:
                        try:
                            try:
                                if not self._safe_connect_path(
                                    "apply_limits_btn", "clicked", self.apply_new_limits
                                ):
                                    try:
                                        try:
                                            if not self._safe_connect(
                                                "apply_btn",
                                                "clicked",
                                                self.apply_new_limits,
                                            ):
                                                try:
                                                    try:
                                                        if not self._safe_connect(
                                                            "apply_limits_button",
                                                            "clicked",
                                                            self.apply_new_limits,
                                                        ):
                                                            sig = getattr(
                                                                apply_btn,
                                                                "clicked",
                                                                None,
                                                            )
                                                            conn = getattr(
                                                                sig, "connect", None
                                                            )
                                                            if callable(conn):
                                                                conn(
                                                                    self.apply_new_limits
                                                                )
                                                    except Exception:
                                                        pass
                                                except Exception:
                                                    pass
                                        except Exception:
                                            pass
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                        except Exception:
                            pass
                except Exception:
                    pass
        except Exception:
            pass
        limits_layout.addWidget(self.apply_limits_button, 4, 0, 1, 2)
        limits_group.setLayout(limits_layout)

        # Target Detection
        detection_group = QGroupBox("Target Detection Settings")
        detection_layout = QGridLayout()
        detection_layout.setSpacing(6)
        detection_layout.setContentsMargins(8, 8, 8, 8)
        # row index for grid
        r = 0

        # Camera selection combo
        if getattr(self, "camera_index_combo", None) is None:
            self.camera_index_combo = QComboBox()
        try:
            if self.camera_index_combo.count() == 0:
                # 'Auto' will let the app try indices 0..4; otherwise pick an index
                self.camera_index_combo.addItems(["Auto", "0", "1", "2", "3", "4"])
            combo = getattr(self, "camera_index_combo", None)
            if combo is not None:
                try:
                    try:
                        # connect via safe helper to avoid attribute-on-None and analyzer warnings
                        self._safe_connect(
                            "camera_index_combo",
                            "currentIndexChanged",
                            self.save_settings,
                        )
                    except Exception:
                        try:
                            try:
                                if not self._safe_connect(
                                    "combo", "currentIndexChanged", self.save_settings
                                ):
                                    try:
                                        try:
                                            if not self._safe_connect(
                                                "combo",
                                                "currentIndexChanged",
                                                self.save_settings,
                                            ):
                                                try:
                                                    try:
                                                        if not self._safe_connect(
                                                            "camera_index_combo",
                                                            "currentIndexChanged",
                                                            self.save_settings,
                                                        ):
                                                            sig = getattr(
                                                                combo,
                                                                "currentIndexChanged",
                                                                None,
                                                            )
                                                            conn = getattr(
                                                                sig, "connect", None
                                                            )
                                                            if callable(conn):
                                                                conn(self.save_settings)
                                                    except Exception:
                                                        pass
                                                except Exception:
                                                    pass
                                        except Exception:
                                            pass
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                        except Exception:
                            pass
                except Exception:
                    pass
        except Exception:
            pass

        # FIX DEC8: Removed premature widget re-read during init_ui
        # Widget initialization race condition was causing Pan to jump from 90° to 2° at startup.
        # The problem: _safe_int_widget_value() was called BEFORE home_pan_input widget received its value,
        # returning uninitialized QSpinBox default (2) instead of self.HOME_PAN (90).
        # This overwrite happened during UI construction, before load_settings() could restore saved values.
        # Solution: Don't re-read from widgets during init_ui. Home values are already set in __init__ (lines 905-906).
        # The widgets will get their proper values in lines 2285-2314 (widget creation with setValue calls),
        # and load_settings() will restore any saved values at line 1107.

        if getattr(self, "threshold_input", None) is None:
            self.threshold_input = QSpinBox()
        try:
            self._safe_widget_call("threshold_input", "setRange", 0, 255)
            self._safe_widget_call("threshold_input", "setValue", 40)
            self._safe_connect("threshold_input", "valueChanged", self.save_settings)
        except Exception:
            pass
        # Ensure the threshold label is present (fix missing label in screenshot)
        detection_layout.addWidget(QLabel("Detection Threshold:"), r, 0)
        detection_layout.addWidget(self.threshold_input, r, 1)
        r += 1

        detection_layout.addWidget(QLabel("Blur Kernel Size (odd num):"), r, 0)
        if getattr(self, "blur_kernel_input", None) is None:
            self.blur_kernel_input = QSpinBox()
        try:
            try:
                self._safe_widget_call("blur_kernel_input", "setRange", 1, 21)
                self._safe_widget_call("blur_kernel_input", "setSingleStep", 2)
                self._safe_widget_call("blur_kernel_input", "setValue", 5)
                self._safe_connect(
                    "blur_kernel_input", "valueChanged", self.save_settings
                )
            except Exception:
                pass
        except Exception:
            pass
        detection_layout.addWidget(self.blur_kernel_input, r, 1)
        r += 1

        detection_layout.addWidget(QLabel("Dilation Iterations:"), r, 0)
        if getattr(self, "dilate_iter_input", None) is None:
            self.dilate_iter_input = QSpinBox()
        try:
            try:
                self._safe_widget_call("dilate_iter_input", "setRange", 1, 10)
                self._safe_widget_call("dilate_iter_input", "setValue", 2)
                self._safe_connect(
                    "dilate_iter_input", "valueChanged", self.save_settings
                )
            except Exception:
                pass
        except Exception:
            pass
        detection_layout.addWidget(self.dilate_iter_input, r, 1)
        r += 1

        detection_layout.addWidget(QLabel("Detection Mode:"), r, 0)
        if getattr(self, "detection_mode_combo", None) is None:
            self.detection_mode_combo = QComboBox()
        try:
            try:
                if self.detection_mode_combo.count() == 0:
                    self._safe_widget_call(
                        "detection_mode_combo",
                        "addItems",
                        [
                            "Frame Difference",
                            "Background Subtraction",
                            "YOLO Object Detection",
                            "Hybrid: Frame Diff + BackSub",
                            "Hybrid: Frame Diff + YOLO",
                            "Hybrid: BackSub + YOLO (Best)",
                        ],
                    )
            except Exception:
                pass
            try:
                dcombo = getattr(self, "detection_mode_combo", None)
                if dcombo is not None:
                    try:
                        self._safe_connect(
                            "detection_mode_combo",
                            "currentIndexChanged",
                            self.save_settings,
                        )
                    except Exception:
                        try:
                            try:
                                if not self._safe_connect(
                                    "dcombo", "currentIndexChanged", self.save_settings
                                ):
                                    try:
                                        try:
                                            if not self._safe_connect(
                                                "dcombo",
                                                "currentIndexChanged",
                                                self.save_settings,
                                            ):
                                                try:
                                                    try:
                                                        if not self._safe_connect(
                                                            "detection_mode_combo",
                                                            "currentIndexChanged",
                                                            self.save_settings,
                                                        ):
                                                            sig = getattr(
                                                                dcombo,
                                                                "currentIndexChanged",
                                                                None,
                                                            )
                                                            conn = getattr(
                                                                sig, "connect", None
                                                            )
                                                            if callable(conn):
                                                                conn(self.save_settings)
                                                    except Exception:
                                                        pass
                                                except Exception:
                                                    pass
                                        except Exception:
                                            pass
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                        except Exception:
                            pass
                    try:
                        self._safe_connect(
                            "detection_mode_combo",
                            "currentIndexChanged",
                            self.on_detection_mode_change,
                        )
                    except Exception:
                        try:
                            try:
                                if not self._safe_connect(
                                    "dcombo",
                                    "currentIndexChanged",
                                    self.on_detection_mode_change,
                                ):
                                    try:
                                        try:
                                            if not self._safe_connect(
                                                "dcombo",
                                                "currentIndexChanged",
                                                self.on_detection_mode_change,
                                            ):
                                                try:
                                                    try:
                                                        if not self._safe_connect(
                                                            "detection_mode_combo",
                                                            "currentIndexChanged",
                                                            self.on_detection_mode_change,
                                                        ):
                                                            sig = getattr(
                                                                dcombo,
                                                                "currentIndexChanged",
                                                                None,
                                                            )
                                                            conn = getattr(
                                                                sig, "connect", None
                                                            )
                                                            if callable(conn):
                                                                conn(
                                                                    self.on_detection_mode_change
                                                                )
                                                    except Exception:
                                                        pass
                                                except Exception:
                                                    pass
                                        except Exception:
                                            pass
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                        except Exception:
                            pass
            except Exception:
                pass
        except Exception:
            pass
        detection_layout.addWidget(self.detection_mode_combo, r, 1)
        r += 1
        # Debug toggle: gate verbose pipeline prints
        if getattr(self, "debug_checkbox", None) is None:
            self.debug_checkbox = QCheckBox("Debug")
        try:
            # default off; preserve across sessions
            self._safe_connect("debug_checkbox", "stateChanged", self.save_settings)
            self._safe_widget_call("debug_checkbox", "setChecked", False)
        except Exception:
            pass
        # Warmup frames for BackgroundSubtractor (skip detections while building background)
        detection_layout.addWidget(QLabel("BackSub Warmup Frames:"), r, 0)
        if getattr(self, "backsub_warmup_input", None) is None:
            self.backsub_warmup_input = QSpinBox()
        try:
            self._safe_widget_call("backsub_warmup_input", "setRange", 0, 300)
            self._safe_widget_call("backsub_warmup_input", "setValue", 30)
            self._safe_connect(
                "backsub_warmup_input", "valueChanged", self.save_settings
            )
        except Exception:
            pass
        detection_layout.addWidget(self.backsub_warmup_input, r, 1)
        r += 1
        
        # Minimum contour size - filter out small noise/specks
        detection_layout.addWidget(QLabel("Min Contour Size (px):"), r, 0)
        if getattr(self, "min_contour_input", None) is None:
            self.min_contour_input = QSpinBox()
        try:
            self._safe_widget_call("min_contour_input", "setRange", 0, 2000000)
            self._safe_widget_call("min_contour_input", "setSingleStep", 50)
            self._safe_widget_call("min_contour_input", "setValue", 300)
            self._safe_connect("min_contour_input", "valueChanged", self.save_settings)
        except Exception:
            pass
        detection_layout.addWidget(self.min_contour_input, r, 1)
        r += 1
        
        # Maximum contour size - filter out large objects (e.g., full frame)
        detection_layout.addWidget(QLabel("Max Contour Size (px):"), r, 0)
        if getattr(self, "max_contour_input", None) is None:
            self.max_contour_input = QSpinBox()
        try:
            self._safe_widget_call("max_contour_input", "setRange", 100, 2000000)
            self._safe_widget_call("max_contour_input", "setSingleStep", 50)
            # Calculate max_contour based on current resolution setting
            initial_max_contour = self._calculate_max_contour_for_resolution(self.frame_ratio_setting)
            self._safe_widget_call("max_contour_input", "setValue", initial_max_contour)
            self._safe_connect("max_contour_input", "valueChanged", self.save_settings)
        except Exception:
            pass
        detection_layout.addWidget(self.max_contour_input, r, 1)
        r += 1

        detection_layout.addWidget(self.debug_checkbox, r, 1)
        r += 1
        detection_group.setLayout(detection_layout)

        # YOLO settings
        if getattr(self, "yolo_settings_group", None) is None:
            self.yolo_settings_group = QGroupBox("YOLO Settings")
        yolo_layout = QGridLayout()
        yolo_layout.setSpacing(6)
        yolo_layout.setContentsMargins(8, 8, 8, 8)
        y = 0
        yolo_layout.addWidget(QLabel("YOLO Model:"), y, 0)
        if getattr(self, "yolo_model_combo", None) is None:
            self.yolo_model_combo = QComboBox()

        # Set balanced widths for the model selector and browse button
        self.yolo_model_combo.setMinimumWidth(85)

        # Browse button to allow selecting models outside the default models dir
        if getattr(self, "yolo_browse_btn", None) is None:
            self.yolo_browse_btn = QPushButton("Browse...")

        # Match browse button width to combo for visual balance
        self.yolo_browse_btn.setMinimumWidth(85)

        try:
            try:
                models = self.yolo_detector.find_models()
            except Exception:
                models = []
            try:
                if self.yolo_model_combo.count() == 0:
                    self._safe_widget_call("yolo_model_combo", "addItems", models)
            except Exception:
                pass
            try:
                ycombo = getattr(self, "yolo_model_combo", None)
                if ycombo is not None:
                    try:
                        self._safe_connect(
                            "yolo_model_combo",
                            "currentIndexChanged",
                            self.save_settings,
                        )
                    except Exception:
                        try:
                            sig = getattr(ycombo, "currentIndexChanged", None)
                            conn = getattr(sig, "connect", None)
                            if callable(conn):
                                conn(self.save_settings)
                        except Exception:
                            pass
                    try:
                        self._safe_connect(
                            "yolo_model_combo",
                            "currentIndexChanged",
                            self.on_yolo_model_changed,
                        )
                    except Exception:
                        try:
                            sig2 = getattr(ycombo, "currentIndexChanged", None)
                            conn2 = getattr(sig2, "connect", None)
                            if callable(conn2):
                                conn2(self.on_yolo_model_changed)
                        except Exception:
                            pass
            except Exception:
                pass
            # Connect the browse button (safe connect)
            try:
                self._safe_connect("yolo_browse_btn", "clicked", self.browse_yolo_model)
            except Exception:
                try:
                    btn = getattr(self, "yolo_browse_btn", None)
                    if btn is not None:
                        sig = getattr(btn, "clicked", None)
                        conn = getattr(sig, "connect", None)
                        if callable(conn):
                            conn(self.browse_yolo_model)
                except Exception:
                    pass
        except Exception:
            pass
        try:
            container = QWidget()
            h = QHBoxLayout()
            h.setContentsMargins(0, 0, 0, 0)
            h.setSpacing(6)
            # Align vertically so combo and button baseline match
            try:
                h.setAlignment(Qt.AlignVCenter)
            except Exception:
                pass
            # Allow combo to expand into available space and keep browse button compact
            try:
                self.yolo_model_combo.setSizePolicy(
                    QSizePolicy.Expanding, QSizePolicy.Preferred
                )
            except Exception:
                pass
            try:
                self.yolo_browse_btn.setSizePolicy(
                    QSizePolicy.Minimum, QSizePolicy.Preferred
                )
            except Exception:
                pass
            # Match the browse button height to the combo's sizeHint for pixel-perfect alignment
            try:
                sh = self.yolo_model_combo.sizeHint()
                if sh is not None and hasattr(sh, "height"):
                    hval = int(sh.height())
                    try:
                        self.yolo_browse_btn.setFixedHeight(hval)
                    except Exception:
                        pass
            except Exception:
                pass
            h.addWidget(self.yolo_model_combo)
            h.addWidget(self.yolo_browse_btn)
            container.setLayout(h)
            # Place container spanning the two input columns so the browse button sits
            # directly next to the combo and doesn't float to the far right.
            yolo_layout.addWidget(container, y, 1, 1, 2)
        except Exception:
            # Fallback: keep the original placement if anything goes wrong
            yolo_layout.addWidget(self.yolo_model_combo, y, 1)
            try:
                yolo_layout.addWidget(self.yolo_browse_btn, y, 2)
            except Exception:
                pass
        y += 1
        # Add a button to open the external YOLO Trainer window
        try:
            if getattr(self, "open_trainer_btn", None) is None:
                self.open_trainer_btn = QPushButton("Open YOLO Trainer")

            # (removed an outdated, conflicting width limit)

            try:
                obtn = getattr(self, "open_trainer_btn", None)
                if obtn is not None:
                    try:
                        self._safe_connect(
                            "open_trainer_btn", "clicked", self.open_yolo_trainer
                        )
                    except Exception:
                        try:
                            try:
                                if not self._safe_connect_path(
                                    "open_trainer_btn",
                                    "clicked",
                                    self.open_yolo_trainer,
                                ):
                                    try:
                                        try:
                                            if not self._safe_connect(
                                                "obtn",
                                                "clicked",
                                                self.open_yolo_trainer,
                                            ):
                                                try:
                                                    try:
                                                        if not self._safe_connect(
                                                            "open_trainer_btn",
                                                            "clicked",
                                                            self.open_yolo_trainer,
                                                        ):
                                                            sig = getattr(
                                                                obtn, "clicked", None
                                                            )
                                                            conn = getattr(
                                                                sig, "connect", None
                                                            )
                                                            if callable(conn):
                                                                conn(
                                                                    self.open_yolo_trainer
                                                                )
                                                    except Exception:
                                                        pass
                                                except Exception:
                                                    pass
                                        except Exception:
                                            pass
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                        except Exception:
                            pass
            except Exception:
                pass
            # Make trainer button span both input columns for a full-width appearance
            self.open_trainer_btn.setMinimumWidth(170)
            # Span across columns 1 and 2 (rowspan=1, colspan=2)
            yolo_layout.addWidget(self.open_trainer_btn, y, 1, 1, 2)
            y += 1
        except Exception:
            pass
        yolo_layout.addWidget(QLabel("Confidence Threshold:"), y, 0)
        if getattr(self, "yolo_confidence_input", None) is None:
            self.yolo_confidence_input = QDoubleSpinBox()

            # Set width to match full width
            self.yolo_confidence_input.setMinimumWidth(170)

            try:
                yc = getattr(self, "yolo_confidence_input", None)
                if yc is not None:
                    try:
                        try:
                            self._safe_widget_call(
                                "yolo_confidence_input", "setRange", 0.1, 1.0
                            )
                            self._safe_widget_call(
                                "yolo_confidence_input", "setSingleStep", 0.05
                            )
                            self._safe_widget_call(
                                "yolo_confidence_input", "setValue", 0.5
                            )
                            self._safe_connect(
                                "yolo_confidence_input",
                                "valueChanged",
                                self.save_settings,
                            )
                        except Exception:
                            pass
                    except Exception:
                        pass
            except Exception:
                pass
        yolo_layout.addWidget(self.yolo_confidence_input, y, 1)
        y += 1
        yolo_layout.addWidget(QLabel("Target Classes (csv):"), y, 0)
        if getattr(self, "yolo_classes_input", None) is None:
            self.yolo_classes_input = QLineEdit()

            # Set width to match dropdown
            self.yolo_classes_input.setMinimumWidth(85)

        try:
            yc2 = getattr(self, "yolo_classes_input", None)
            if yc2 is not None:
                try:
                    if not yc2.text():
                        try:
                            self._safe_widget_call(
                                "yolo_classes_input", "setText", "person"
                            )
                        except Exception:
                            pass
                    try:
                        try:
                            self._safe_connect(
                                "yolo_classes_input", "textChanged", self.save_settings
                            )
                            # Also update detector classes live when the CSV text changes
                            try:
                                self._safe_connect(
                                    "yolo_classes_input",
                                    "textChanged",
                                    self.update_yolo_target_classes,
                                )
                            except Exception:
                                pass
                        except Exception:
                            try:
                                if not self._safe_connect_path(
                                    "yclass_input", "textChanged", self.save_settings
                                ):
                                    try:
                                        try:
                                            if not self._safe_connect(
                                                "yc2", "textChanged", self.save_settings
                                            ):
                                                try:
                                                    try:
                                                        if not self._safe_connect(
                                                            "yolo_classes_input",
                                                            "textChanged",
                                                            self.save_settings,
                                                        ):
                                                            sig = getattr(
                                                                yc2, "textChanged", None
                                                            )
                                                            conn = getattr(
                                                                sig, "connect", None
                                                            )
                                                            if callable(conn):
                                                                conn(self.save_settings)
                                                    except Exception:
                                                        pass
                                                except Exception:
                                                    pass
                                        except Exception:
                                            pass
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                    except Exception:
                        pass
                except Exception:
                    pass
        except Exception:
            pass
        # Place the text field and a small chooser button side-by-side
        try:
            if getattr(self, "yolo_pick_classes_btn", None) is None:
                self.yolo_pick_classes_btn = QPushButton("Pick...")

                # Set width to match browse button
                self.yolo_pick_classes_btn.setMinimumWidth(85)

                try:
                    self.yolo_pick_classes_btn.clicked.connect(
                        self.open_yolo_class_picker
                    )
                except Exception:
                    pass
            container = QWidget()
            h = QHBoxLayout()
            h.setContentsMargins(0, 0, 0, 0)
            h.addWidget(self.yolo_classes_input)
            h.addWidget(self.yolo_pick_classes_btn)
            container.setLayout(h)
            yolo_layout.addWidget(container, y, 1)
            y += 1
        except Exception:
            pass
        # Additional YOLO settings: Max Results and Min Area
        yolo_layout.addWidget(QLabel("Max Results (0=all):"), y, 0)
        if getattr(self, "yolo_max_results_input", None) is None:
            self.yolo_max_results_input = QSpinBox()
            try:
                self.yolo_max_results_input.setRange(0, 100)
                self.yolo_max_results_input.setValue(0)
                # Set width to match full width
                self.yolo_max_results_input.setMinimumWidth(170)
            except Exception:
                pass
        try:
            self._safe_connect(
                "yolo_max_results_input", "valueChanged", self.save_settings
            )
        except Exception:
            try:
                sig = getattr(self.yolo_max_results_input, "valueChanged", None)
                conn = getattr(sig, "connect", None)
                if callable(conn):
                    conn(self.save_settings)
            except Exception:
                pass
        yolo_layout.addWidget(self.yolo_max_results_input, y, 1)
        y += 1

        yolo_layout.addWidget(QLabel("Min Area (px):"), y, 0)
        if getattr(self, "yolo_min_area_input", None) is None:
            self.yolo_min_area_input = QSpinBox()
            try:
                self.yolo_min_area_input.setRange(0, 10000000)
                self.yolo_min_area_input.setValue(0)
                # Set width to match full width
                self.yolo_min_area_input.setMinimumWidth(170)
            except Exception:
                pass
        try:
            self._safe_connect(
                "yolo_min_area_input", "valueChanged", self.save_settings
            )
        except Exception:
            try:
                sig = getattr(self.yolo_min_area_input, "valueChanged", None)
                conn = getattr(sig, "connect", None)
                if callable(conn):
                    conn(self.save_settings)
            except Exception:
                pass
        yolo_layout.addWidget(self.yolo_min_area_input, y, 1)
        y += 1
        # Small status label to show current detection count for easier debugging
        try:
            if getattr(self, "yolo_detect_status_label", None) is None:
                self.yolo_detect_status_label = QLabel("Idle")
            yolo_layout.addWidget(QLabel("Detect Status:"), y, 0)
            yolo_layout.addWidget(self.yolo_detect_status_label, y, 1, 1, 2)
            y += 1
        except Exception:
            pass
        self.yolo_settings_group.setLayout(yolo_layout)

        # >>> Make the widget shrink to fit <<<
        # Allow the YOLO settings group to be resized by the dock area. Using
        # QSizePolicy.Preferred horizontally instead of Maximum ensures the
        # right column (dock) remains adjustable by the user.
        self.yolo_settings_group.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Preferred
        )

        # ========== HYBRID DETECTION MODE SETTINGS ==========
        # Controls for tuning hybrid mode fusion strategies and thresholds
        if getattr(self, "hybrid_settings_group", None) is None:
            self.hybrid_settings_group = QGroupBox("Hybrid Detection Settings")
        hybrid_layout = QGridLayout()
        hybrid_layout.setSpacing(6)
        hybrid_layout.setContentsMargins(8, 8, 8, 8)
        h = 0

        # Fusion strategy for modes 3 and 4
        hybrid_layout.addWidget(QLabel("Fusion Strategy:"), h, 0)
        if getattr(self, "fusion_strategy_combo", None) is None:
            self.fusion_strategy_combo = QComboBox()
            try:
                self._safe_widget_call(
                    "fusion_strategy_combo",
                    "addItems",
                    ["Strict (AND)", "Lenient (OR)"],
                )
            except Exception:
                pass
            try:
                self._safe_connect(
                    "fusion_strategy_combo", "currentIndexChanged", self.save_settings
                )
            except Exception:
                pass
        hybrid_layout.addWidget(self.fusion_strategy_combo, h, 1)
        h += 1

        # Frame Diff + YOLO motion gate threshold (for mode 4)
        hybrid_layout.addWidget(QLabel("Motion Gate % (FrameDiff+YOLO):"), h, 0)
        if getattr(self, "motion_gate_threshold_input", None) is None:
            self.motion_gate_threshold_input = QDoubleSpinBox()
            try:
                self.motion_gate_threshold_input.setRange(0.0, 100.0)
                self.motion_gate_threshold_input.setValue(1.0)
                self.motion_gate_threshold_input.setSingleStep(0.1)
                self._safe_connect(
                    "motion_gate_threshold_input", "valueChanged", self.save_settings
                )
            except Exception:
                pass
        hybrid_layout.addWidget(self.motion_gate_threshold_input, h, 1)
        h += 1

        # BackSub + YOLO overlap threshold (for mode 5)
        hybrid_layout.addWidget(QLabel("Overlap Threshold % (BackSub+YOLO):"), h, 0)
        if getattr(self, "overlap_threshold_input", None) is None:
            self.overlap_threshold_input = QDoubleSpinBox()
            try:
                self.overlap_threshold_input.setRange(0.0, 100.0)
                self.overlap_threshold_input.setValue(30.0)
                self.overlap_threshold_input.setSingleStep(5.0)
                self._safe_connect(
                    "overlap_threshold_input", "valueChanged", self.save_settings
                )
            except Exception:
                pass
        hybrid_layout.addWidget(self.overlap_threshold_input, h, 1)
        h += 1

        self.hybrid_settings_group.setLayout(hybrid_layout)
        self.hybrid_settings_group.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Preferred
        )
        # Set minimum height so YOLO panel has adequate space when shown
        self.yolo_settings_group.setMinimumHeight(400)
        self.yolo_settings_group.adjustSize()
        # <<< End >>>

        # Prepare tracking widgets (Slider + label). Placement into the
        # Behavior panel is done later so the widgets appear inside the
        # `Tracking Behavior` dock (avoid creating a separate groupbox).
        if getattr(self, "tracking_speed_slider", None) is None:
            self.tracking_speed_slider = QSlider()
            try:
                try:
                    self.tracking_speed_slider.setOrientation(
                        cast(Any, self._qt_enum("Horizontal", 1))
                    )
                except Exception:
                    pass
            except Exception:
                pass
        try:
            try:
                self._safe_widget_call("tracking_speed_slider", "setRange", 1, 100)
                self._safe_widget_call("tracking_speed_slider", "setValue", 65)
                self._safe_connect(
                    "tracking_speed_slider", "valueChanged", self.save_settings
                )
            except Exception:
                pass
        except Exception:
            pass

        if getattr(self, "tracking_speed_label", None) is None:
            try:
                cur_val = self._safe_int_widget_value("tracking_speed_slider", 40)
            except Exception:
                cur_val = 40
            self.tracking_speed_label = QLabel(f"{cur_val}%")
        try:
            try:
                self.tracking_speed_label.setFixedWidth(40)
                self._safe_connect(
                    "tracking_speed_slider",
                    "valueChanged",
                    lambda v: self.tracking_speed_label.setText(f"{v}%"),
                )
            except Exception:
                pass
        except Exception:
            pass
        
        # Tracking controls are now placed inside the unified Behavior & Presets dock
        # created by create_behavior_tracking_panel(). Do not add a separate dock here.

        # Create behavior controls group
        # Keep as attributes so other methods (and the unified panel) can reuse them
        # Create a dedicated container widget that will be used as the
        # scroll area's content. Parent the container to self so it has a
        # stable owner; the QGroupBox will be parented to this container.
        behavior_container = getattr(self, "behavior_container", None) or QWidget(self)
        self.behavior_container = behavior_container

        # Make the behavior group a child of the container so its lifetime
        # is tied to the container which is itself owned by the scroll area.
        behavior_group = getattr(self, "behavior_group", None) or QGroupBox("Tracking Behavior", behavior_container)
        self.behavior_group = behavior_group
        behavior_layout = getattr(self, "behavior_layout", None) or QGridLayout()
        behavior_layout.setSpacing(6)
        behavior_layout.setContentsMargins(8, 8, 8, 8)
        # Expose as an attribute so other helpers can find/modify it
        self.behavior_layout = behavior_layout
        br = getattr(self, "_behavior_row_counter", 0) or 0
        self._behavior_row_counter = br

        # Prepare behavior scroll area and attach the container so ownership is stable.
        behavior_scroll = QScrollArea()
        try:
            behavior_group.setLayout(behavior_layout)
        except Exception:
            pass

        # Ensure the behavior_container actually displays the behavior_group
        if behavior_container.layout() is None:
            try:
                cont_layout = QVBoxLayout(behavior_container)
                cont_layout.setContentsMargins(0, 0, 0, 0)
                cont_layout.setSpacing(6)
                cont_layout.addWidget(behavior_group)
                behavior_container.setLayout(cont_layout)
            except Exception:
                pass

        behavior_scroll.setWidget(behavior_container)
        behavior_scroll.setWidgetResizable(True)
        # Keep a reference on self so later code reuses the same scroll area
        self.behavior_scroll = behavior_scroll

        # --- QUICK FIX: ensure tracking slider is actually in the behavior_layout ---
        try:
            # defensive lookups
            bl = getattr(self, "behavior_layout", None)
            bs = getattr(self, "behavior_scroll", None)
            if bl is not None:
                # quick check: look for slider or label already in the layout (handles direct widgets)
                def _in_layout(widget):
                    try:
                        if widget is None:
                            return False
                        for i in range(bl.count()):
                            it = bl.itemAt(i)
                            if not it:
                                continue
                            try:
                                w = it.widget()
                                if w is widget:
                                    return True
                            except Exception:
                                pass
                        return False
                    except Exception:
                        return False

                if getattr(self, "tracking_speed_slider", None) and not _in_layout(self.tracking_speed_slider):
                    # attach parent so ownership is stable (prevents some orphaning issues)
                    try:
                        self.tracking_speed_slider.setParent(getattr(self, "behavior_container", self))
                    except Exception:
                        pass
                    try:
                        # top insert at row 0 (safe — will be ignored if grid cell occupied)
                        bl.addWidget(QLabel("Tracking Speed"), 0, 0)
                    except Exception:
                        pass
                    try:
                        speed_row = QHBoxLayout()
                        speed_row.addWidget(self.tracking_speed_slider)
                        if getattr(self, "tracking_speed_label", None):
                            speed_row.addWidget(self.tracking_speed_label)
                        bl.addLayout(speed_row, 0, 1)
                    except Exception:
                        # fallback: attempt to add slider/label individually
                        try:
                            bl.addWidget(self.tracking_speed_slider, 0, 1)
                        except Exception:
                            pass
                        try:
                            if getattr(self, "tracking_speed_label", None):
                                bl.addWidget(self.tracking_speed_label, 0, 2)
                        except Exception:
                            pass
        except Exception:
            pass
        # --- end quick fix ---

        # Ensure the behavior group has a sensible minimum size so its
        # widgets are visible when docked (helps avoid collapsed empty area).
        try:
            behavior_group.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            try:
                behavior_group.adjustSize()
            except Exception:
                pass
            try:
                behavior_group.setMinimumWidth(280)
            except Exception:
                pass
            try:
                behavior_scroll.setMinimumWidth(280)
            except Exception:
                pass
        except Exception:
            pass

        behavior_layout.addWidget(QLabel("Tracking Speed"), br, 0)
        speed_row = QHBoxLayout()
        speed_row.addWidget(self.tracking_speed_slider)
        speed_row.addWidget(self.tracking_speed_label)
        behavior_layout.addLayout(speed_row, br, 1)
        br += 1

        # Create presets group
        # Create a small presets group inside the behavior panel. Parent it
        # to the main window as well so it remains owned even while docks
        # are created/changed during UI setup.
        presets_group = QGroupBox("Behavior Presets", self)
        presets_layout = QVBoxLayout()
        presets_layout.setSpacing(6)
        presets_layout.setContentsMargins(8, 8, 8, 8)
        presets_group.setLayout(presets_layout)
        
        # Dock creation for Behavior & Presets will be handled centrally by
        # create_behavior_tracking_panel() to provide a single unified dock and
        # avoid duplicate panels. Do not create docks here.

        # movement sensitivity
        behavior_layout.addWidget(QLabel("Movement Sensitivity"), br, 0)
        sensitivity_row = QHBoxLayout()
        if getattr(self, "movement_sensitivity_slider", None) is None:
            self.movement_sensitivity_slider = QSlider()
            try:
                try:
                    self.movement_sensitivity_slider.setOrientation(
                        cast(Any, self._qt_enum("Horizontal", 1))
                    )
                except Exception:
                    pass
            except Exception:
                pass
        try:
            try:
                self._safe_widget_call(
                    "movement_sensitivity_slider", "setRange", 1, 100
                )
                self._safe_widget_call("movement_sensitivity_slider", "setValue", 45)
                self._safe_connect(
                    "movement_sensitivity_slider", "valueChanged", self.save_settings
                )
            except Exception:
                pass
        except Exception:
            pass
        if getattr(self, "movement_sensitivity_label", None) is None:
            self.movement_sensitivity_label = QLabel("25%")
        try:
            try:
                self.movement_sensitivity_label.setFixedWidth(40)
                self._safe_connect(
                    "movement_sensitivity_slider",
                    "valueChanged",
                    lambda v: self.movement_sensitivity_label.setText(f"{v}%"),
                )
            except Exception:
                pass
        except Exception:
            pass
        sensitivity_row.addWidget(self.movement_sensitivity_slider)
        sensitivity_row.addWidget(self.movement_sensitivity_label)
        behavior_layout.addLayout(sensitivity_row, br, 1)
        br += 1

        # smoothing
        behavior_layout.addWidget(QLabel("Smoothing (0.1 - 0.8):"), br, 0)
        if getattr(self, "smoothing_input", None) is None:
            self.smoothing_input = QDoubleSpinBox()
        try:
            try:
                self._safe_widget_call("smoothing_input", "setRange", 0.1, 0.8)
                self._safe_widget_call("smoothing_input", "setSingleStep", 0.05)
                self._safe_widget_call("smoothing_input", "setValue", 0.35)
                self._safe_connect(
                    "smoothing_input", "valueChanged", self.save_settings
                )
            except Exception:
                pass
        except Exception:
            pass
        behavior_layout.addWidget(self.smoothing_input, br, 1)
        br += 1

        # overshoot percentage: allow small intentional overshoot compensation
        behavior_layout.addWidget(QLabel("Overshoot (%):"), br, 0)
        if getattr(self, "overshoot_input", None) is None:
            self.overshoot_input = QSpinBox()
        try:
            try:
                self._safe_widget_call("overshoot_input", "setRange", -100, 100)
                self._safe_widget_call("overshoot_input", "setValue", 0)
                self._safe_connect(
                    "overshoot_input", "valueChanged", self.save_settings
                )
            except Exception:
                pass
        except Exception:
            pass
        try:
            self.overshoot_input.setToolTip(
                "Percent overshoot applied to motion gain; positive = more aggressive."
            )
        except Exception:
            pass
        behavior_layout.addWidget(self.overshoot_input, br, 1)
        br += 1

        # ========== CAMERA RESOLUTION - REMOVED (Dec 2024) ==========
        # Resolution selector removed - camera now uses fixed 1280x720
        # The frame_ratio_combo widget is NOT created to prevent any UI interaction
        # Internal frame_width/frame_height are set to 1280x720 in __init__

        # deadzone and snap
        behavior_layout.addWidget(QLabel("Deadzone (pixels)"), br, 0)
        deadzone_row = QHBoxLayout()
        if getattr(self, "deadzone_slider", None) is None:
            self.deadzone_slider = QSlider()
            try:
                try:
                    self.deadzone_slider.setOrientation(
                        cast(Any, self._qt_enum("Horizontal", 1))
                    )
                except Exception:
                    pass
            except Exception:
                pass
        try:
            try:
                self._safe_widget_call("deadzone_slider", "setRange", 0, 200)
                self._safe_widget_call("deadzone_slider", "setValue", 8)
                self._safe_connect(
                    "deadzone_slider", "valueChanged", self.save_settings
                )
            except Exception:
                pass
        except Exception:
            pass
        if getattr(self, "deadzone_label", None) is None:
            try:
                dz = self._safe_int_widget_value("deadzone_slider", 20)
            except Exception:
                dz = 20
            self.deadzone_label = QLabel(str(dz))
        try:
            try:
                self.deadzone_label.setFixedWidth(40)
                self._safe_connect(
                    "deadzone_slider",
                    "valueChanged",
                    lambda v: self.deadzone_label.setText(str(v)),
                )
            except Exception:
                pass
        except Exception:
            pass
        deadzone_row.addWidget(self.deadzone_slider)
        deadzone_row.addWidget(self.deadzone_label)
        behavior_layout.addLayout(deadzone_row, br, 1)
        br += 1

        behavior_layout.addWidget(QLabel("Snap Threshold (px)"), br, 0)
        snap_row = QHBoxLayout()
        if getattr(self, "snap_threshold_slider", None) is None:
            self.snap_threshold_slider = QSlider()
            try:
                try:
                    self.snap_threshold_slider.setOrientation(
                        cast(Any, self._qt_enum("Horizontal", 1))
                    )
                except Exception:
                    pass
            except Exception:
                pass
        try:
            if getattr(self, "snap_threshold_slider", None) is not None:
                try:
                    self._safe_widget_call("snap_threshold_slider", "setRange", 0, 400)
                    self._safe_widget_call("snap_threshold_slider", "setValue", 40)
                    try:
                        try:
                            self._safe_connect(
                                "snap_threshold_slider",
                                "valueChanged",
                                self.save_settings,
                            )
                        except Exception:
                            try:
                                if not self._safe_connect(
                                    "snap_threshold_slider",
                                    "valueChanged",
                                    self.save_settings,
                                ):
                                    try:
                                        try:
                                            if not self._safe_connect(
                                                "snap_threshold_slider",
                                                "valueChanged",
                                                self.save_settings,
                                            ):
                                                try:
                                                    try:
                                                        if not self._safe_connect(
                                                            "snap_threshold_slider",
                                                            "valueChanged",
                                                            self.save_settings,
                                                        ):
                                                            sig = getattr(
                                                                self.snap_threshold_slider,
                                                                "valueChanged",
                                                                None,
                                                            )
                                                            conn = getattr(
                                                                sig, "connect", None
                                                            )
                                                            if callable(conn):
                                                                conn(self.save_settings)
                                                    except Exception:
                                                        pass
                                                except Exception:
                                                    pass
                                        except Exception:
                                            pass
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                    except Exception:
                        pass
                except Exception:
                    pass
        except Exception:
            pass
        if getattr(self, "snap_threshold_label", None) is None:
            try:
                sv = self._safe_int_widget_value("snap_threshold_slider", 80)
            except Exception:
                sv = 80
            self.snap_threshold_label = QLabel(str(sv))
        try:
            self.snap_threshold_label.setFixedWidth(40)
            try:
                self._safe_connect(
                    "snap_threshold_slider",
                    "valueChanged",
                    lambda v: self.snap_threshold_label.setText(str(v)),
                )
            except Exception:
                try:
                    try:
                        if not self._safe_connect(
                            "snap_threshold_slider",
                            "valueChanged",
                            lambda v: self.snap_threshold_label.setText(str(v)),
                        ):
                            try:
                                try:
                                    if not self._safe_connect(
                                        "snap_threshold_slider",
                                        "valueChanged",
                                        lambda v: self.snap_threshold_label.setText(
                                            str(v)
                                        ),
                                    ):
                                        try:
                                            try:
                                                if not self._safe_connect(
                                                    "snap_threshold_slider",
                                                    "valueChanged",
                                                    lambda v: self.snap_threshold_label.setText(
                                                        str(v)
                                                    ),
                                                ):
                                                    sig = getattr(
                                                        self.snap_threshold_slider,
                                                        "valueChanged",
                                                        None,
                                                    )
                                                    conn = getattr(sig, "connect", None)
                                                    if callable(conn):
                                                        conn(
                                                            lambda v: self.snap_threshold_label.setText(
                                                                str(v)
                                                            )
                                                        )
                                            except Exception:
                                                pass
                                        except Exception:
                                            pass
                                except Exception:
                                    pass
                            except Exception:
                                pass
                    except Exception:
                        pass
                except Exception:
                    pass
        except Exception:
            pass
        snap_row.addWidget(self.snap_threshold_slider)
        snap_row.addWidget(self.snap_threshold_label)
        behavior_layout.addLayout(snap_row, br, 1)
        br += 1

        # Hold target position for a configurable time after detection loss
        behavior_layout.addWidget(QLabel("Hold target on loss (s):"), br, 0)
        if getattr(self, "lost_hold_input", None) is None:
            self.lost_hold_input = QDoubleSpinBox()
        try:
            if getattr(self, "lost_hold_input", None) is not None:
                try:
                    self._safe_widget_call("lost_hold_input", "setRange", 0.0, 60.0)
                    self._safe_widget_call("lost_hold_input", "setSingleStep", 0.5)
                    try:
                        self._safe_widget_call(
                            "lost_hold_input",
                            "setValue",
                            getattr(self, "lost_hold_seconds", 5.0),
                        )
                    except Exception:
                        pass
                    try:
                        try:
                            self._safe_connect(
                                "lost_hold_input",
                                "valueChanged",
                                lambda v: setattr(self, "lost_hold_seconds", float(v))
                                or self.save_settings(),
                            )
                        except Exception:
                            try:
                                if not self._safe_connect(
                                    "lost_hold_input",
                                    "valueChanged",
                                    lambda v: setattr(
                                        self, "lost_hold_seconds", float(v)
                                    )
                                    or self.save_settings(),
                                ):
                                    try:
                                        try:
                                            if not self._safe_connect(
                                                "lost_hold_input",
                                                "valueChanged",
                                                lambda v: (
                                                    setattr(
                                                        self,
                                                        "lost_hold_seconds",
                                                        float(v),
                                                    ),
                                                    self.save_settings(),
                                                ),
                                            ):
                                                try:
                                                    try:
                                                        if not self._safe_connect(
                                                            "lost_hold_input",
                                                            "valueChanged",
                                                            lambda v: (
                                                                setattr(
                                                                    self,
                                                                    "lost_hold_seconds",
                                                                    float(v),
                                                                ),
                                                                self.save_settings(),
                                                            ),
                                                        ):
                                                            sig = getattr(
                                                                self.lost_hold_input,
                                                                "valueChanged",
                                                                None,
                                                            )
                                                            conn = getattr(
                                                                sig, "connect", None
                                                            )
                                                            if callable(conn):
                                                                conn(
                                                                    lambda v: (
                                                                        setattr(
                                                                            self,
                                                                            "lost_hold_seconds",
                                                                            float(v),
                                                                        ),
                                                                        self.save_settings(),
                                                                    )
                                                                )
                                                    except Exception:
                                                        pass
                                                except Exception:
                                                    pass
                                        except Exception:
                                            pass
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                    except Exception:
                        pass
                    try:
                        self._safe_widget_call(
                            "lost_hold_input",
                            "setToolTip",
                            "When target is lost, keep aiming at the last known position for this many seconds (0 = disable).",
                        )
                    except Exception:
                        pass
                except Exception:
                    pass
        except Exception:
            pass
        # 'Hold indefinitely' checkbox (when checked, never timeout the hold)
        try:
            if getattr(self, "hold_infinite_checkbox", None) is None:
                self.hold_infinite_checkbox = QCheckBox(
                    "Hold indefinitely (no timeout)"
                )
            hic = getattr(self, "hold_infinite_checkbox", None)
            if hic is not None:
                try:
                    try:
                        try:
                            self._safe_connect(
                                "hold_infinite_checkbox",
                                "stateChanged",
                                lambda s: setattr(self, "hold_infinite", bool(s)),
                            )
                        except Exception:
                            try:
                                try:
                                    if not self._safe_connect(
                                        "hic",
                                        "stateChanged",
                                        lambda s: setattr(
                                            self, "hold_infinite", bool(s)
                                        ),
                                    ):
                                        try:
                                            try:
                                                if not self._safe_connect(
                                                    "hic",
                                                    "stateChanged",
                                                    lambda s: setattr(
                                                        self, "hold_infinite", bool(s)
                                                    ),
                                                ):
                                                    try:
                                                        try:
                                                            if not self._safe_connect(
                                                                "hold_infinite_checkbox",
                                                                "stateChanged",
                                                                lambda s: setattr(
                                                                    self,
                                                                    "hold_infinite",
                                                                    bool(s),
                                                                ),
                                                            ):
                                                                sig = getattr(
                                                                    hic,
                                                                    "stateChanged",
                                                                    None,
                                                                )
                                                                conn = getattr(
                                                                    sig, "connect", None
                                                                )
                                                                if callable(conn):
                                                                    conn(
                                                                        lambda s: setattr(
                                                                            self,
                                                                            "hold_infinite",
                                                                            bool(s),
                                                                        )
                                                                    )
                                                        except Exception:
                                                            pass
                                                    except Exception:
                                                        pass
                                            except Exception:
                                                pass
                                        except Exception:
                                            pass
                                except Exception:
                                    pass
                            except Exception:
                                pass
                    except Exception:
                        pass
                    try:
                        try:
                            self._safe_connect(
                                "hold_infinite_checkbox",
                                "stateChanged",
                                self.save_settings,
                            )
                        except Exception:
                            try:
                                try:
                                    if not self._safe_connect(
                                        "hic", "stateChanged", self.save_settings
                                    ):
                                        try:
                                            try:
                                                if not self._safe_connect(
                                                    "hic",
                                                    "stateChanged",
                                                    self.save_settings,
                                                ):
                                                    try:
                                                        try:
                                                            if not self._safe_connect(
                                                                "hold_infinite_checkbox",
                                                                "stateChanged",
                                                                self.save_settings,
                                                            ):
                                                                sig = getattr(
                                                                    hic,
                                                                    "stateChanged",
                                                                    None,
                                                                )
                                                                conn = getattr(
                                                                    sig, "connect", None
                                                                )
                                                                if callable(conn):
                                                                    conn(
                                                                        self.save_settings
                                                                    )
                                                        except Exception:
                                                            pass
                                                    except Exception:
                                                        pass
                                            except Exception:
                                                pass
                                        except Exception:
                                            pass
                                except Exception:
                                    pass
                            except Exception:
                                pass
                    except Exception:
                        pass
                    try:
                        hic.setToolTip(
                            "When checked, hold the last known target position indefinitely after loss (no timeout). Use to lock aim at the last seen point."
                        )
                    except Exception:
                        pass
                except Exception:
                    pass
        except Exception:
            pass
        # place both in same row (spinbox right, checkbox below it)
        behavior_layout.addWidget(self.lost_hold_input, br, 1)
        br += 1
        behavior_layout.addWidget(self.hold_infinite_checkbox, br, 0, 1, 2)
        br += 1

        # ========== AIM AGGRESSION SLIDER (NEW - Dec 2024) ==========
        # Controls how aggressively the turret pursues center
        # 0 = conservative/lazy, 100 = maximum aggression with boosted final approach
        behavior_layout.addWidget(QLabel("Aim Aggression (%):"), br, 0)
        aim_aggression_row = QHBoxLayout()
        if getattr(self, "aim_aggression_slider", None) is None:
            self.aim_aggression_slider = QSlider()
        try:
            self.aim_aggression_slider.setOrientation(Qt.Horizontal)
            self.aim_aggression_slider.setRange(0, 100)
            self.aim_aggression_slider.setValue(int(getattr(self, "aim_aggression", 50)))
        except Exception:
            pass
        if getattr(self, "aim_aggression_label", None) is None:
            self.aim_aggression_label = QLabel(str(getattr(self, "aim_aggression", 50)))
        try:
            self.aim_aggression_label.setFixedWidth(30)
        except Exception:
            pass
        try:
            self._safe_connect(
                "aim_aggression_slider",
                "valueChanged",
                lambda v: (
                    setattr(self, "aim_aggression", v),
                    self.aim_aggression_label.setText(str(v)),
                    self.save_settings()
                )
            )
        except Exception:
            pass
        try:
            self.aim_aggression_slider.setToolTip(
                "How aggressively the turret recenters on target: 0=conservative, 50=balanced, 100=very aggressive (may overshoot)."
            )
        except Exception:
            pass
        aim_aggression_row.addWidget(self.aim_aggression_slider)
        aim_aggression_row.addWidget(self.aim_aggression_label)
        behavior_layout.addLayout(aim_aggression_row, br, 1)
        br += 1

        # ========== FINAL APPROACH BOOST CHECKBOX (NEW - Dec 2024) ==========
        # When enabled, applies 2-3x speed multiplier and reduces smoothing
        # when target is within 2x deadzone radius for snappy centering
        if getattr(self, "final_approach_boost_checkbox", None) is None:
            self.final_approach_boost_checkbox = QCheckBox("Final Approach Boost")
        try:
            self.final_approach_boost_checkbox.setChecked(
                bool(getattr(self, "final_approach_boost", True))
            )
        except Exception:
            pass
        try:
            self._safe_connect(
                "final_approach_boost_checkbox",
                "stateChanged",
                lambda s: (
                    setattr(self, "final_approach_boost", bool(s)),
                    self.save_settings()
                )
            )
        except Exception:
            pass
        try:
            self.final_approach_boost_checkbox.setToolTip(
                "Enable speed boost and reduced smoothing when the target is very close to improve final centering."
            )
        except Exception:
            pass
        behavior_layout.addWidget(self.final_approach_boost_checkbox, br, 0, 1, 2)
        br += 1

        # some toggles
        if getattr(self, "invert_pan_checkbox", None) is None:
            self.invert_pan_checkbox = QCheckBox("Invert PAN Movement")
        try:
            try:
                self._safe_connect(
                    "invert_pan_checkbox",
                    "stateChanged",
                    lambda s: self.set_flip_pan(bool(s)),
                )
            except Exception:
                try:
                    try:
                        if not self._safe_connect(
                            "invert_pan_checkbox",
                            "stateChanged",
                            lambda s: self.set_flip_pan(bool(s)),
                        ):
                            try:
                                try:
                                    if not self._safe_connect(
                                        "invert_pan_checkbox",
                                        "stateChanged",
                                        lambda s: self.set_flip_pan(bool(s)),
                                    ):
                                        sig = getattr(
                                            self.invert_pan_checkbox,
                                            "stateChanged",
                                            None,
                                        )
                                        conn = getattr(sig, "connect", None)
                                        if callable(conn):
                                            conn(lambda s: self.set_flip_pan(bool(s)))
                                except Exception:
                                    pass
                            except Exception:
                                pass
                    except Exception:
                        pass
                except Exception:
                    pass
            try:
                self._safe_connect(
                    "invert_pan_checkbox", "stateChanged", self.save_settings
                )
            except Exception:
                try:
                    try:
                        if not self._safe_connect(
                            "invert_pan_checkbox", "stateChanged", self.save_settings
                        ):
                            try:
                                try:
                                    if not self._safe_connect(
                                        "invert_pan_checkbox",
                                        "stateChanged",
                                        self.save_settings,
                                    ):
                                        sig = getattr(
                                            self.invert_pan_checkbox,
                                            "stateChanged",
                                            None,
                                        )
                                        conn = getattr(sig, "connect", None)
                                        if callable(conn):
                                            conn(self.save_settings)
                                except Exception:
                                    pass
                            except Exception:
                                pass
                    except Exception:
                        pass
                except Exception:
                    pass
        except Exception:
            pass
        behavior_layout.addWidget(self.invert_pan_checkbox, br, 0, 1, 2)
        br += 1

        if getattr(self, "invert_tilt_checkbox", None) is None:
            self.invert_tilt_checkbox = QCheckBox("Invert TILT Movement")
        try:
            try:
                self._safe_connect(
                    "invert_tilt_checkbox",
                    "stateChanged",
                    lambda s: self.set_flip_tilt(bool(s)),
                )
            except Exception:
                try:
                    try:
                        if not self._safe_connect(
                            "invert_tilt_checkbox",
                            "stateChanged",
                            lambda s: self.set_flip_tilt(bool(s)),
                        ):
                            try:
                                try:
                                    if not self._safe_connect(
                                        "invert_tilt_checkbox",
                                        "stateChanged",
                                        lambda s: self.set_flip_tilt(bool(s)),
                                    ):
                                        sig = getattr(
                                            self.invert_tilt_checkbox,
                                            "stateChanged",
                                            None,
                                        )
                                        conn = getattr(sig, "connect", None)
                                        if callable(conn):
                                            conn(lambda s: self.set_flip_tilt(bool(s)))
                                except Exception:
                                    pass
                            except Exception:
                                pass
                    except Exception:
                        pass
                except Exception:
                    pass
                try:
                    if not self._safe_connect(
                        "invert_tilt_checkbox", "stateChanged", self.save_settings
                    ):
                        try:
                            sig = getattr(
                                self.invert_tilt_checkbox, "stateChanged", None
                            )
                            conn = getattr(sig, "connect", None)
                            if callable(conn):
                                conn(self.save_settings)
                        except Exception:
                            pass
                except Exception:
                    pass
        except Exception:
            pass
        behavior_layout.addWidget(self.invert_tilt_checkbox, br, 0, 1, 2)
        br += 1

        if getattr(self, "flip_checkbox", None) is None:
            self.flip_checkbox = QCheckBox("Flip Frame (180\u00b0)")
        try:
            try:
                if not self._safe_connect(
                    "flip_checkbox", "stateChanged", self.save_settings
                ):
                    try:
                        sig = getattr(self.flip_checkbox, "stateChanged", None)
                        conn = getattr(sig, "connect", None)
                        if callable(conn):
                            conn(self.save_settings)
                    except Exception:
                        pass
            except Exception:
                pass
        except Exception:
            pass
        behavior_layout.addWidget(self.flip_checkbox, br, 0, 1, 2)
        br += 1

        # presets
        behavior_layout.addWidget(QLabel("Preset:"), br, 0)
        if getattr(self, "preset_combo", None) is None:
            self.preset_combo = QComboBox()
        try:
            if self.preset_combo.count() == 0:
                self.preset_combo.addItems(list(PRESETS.keys()))
            self._safe_connect("preset_combo", "currentIndexChanged", self.apply_preset)
        except Exception:
            pass
        behavior_layout.addWidget(self.preset_combo, br, 1)
        br += 1
        behavior_group.setLayout(behavior_layout)
        behavior_group.setLayout(behavior_layout)

        # Accessories
        accessory_group = QGroupBox("Accessories")
        accessory_layout = QVBoxLayout()
        accessory_layout.setSpacing(6)
        accessory_layout.setContentsMargins(8, 8, 8, 8)
        if getattr(self, "relay1_button", None) is None:
            self.relay1_button = QPushButton("LED (Relay1): OFF")
        try:
            self.relay1_button.setCheckable(True)
            self._safe_connect("relay1_button", "clicked", lambda: self.toggle_relay(1))
        except Exception:
            pass
        accessory_layout.addWidget(self.relay1_button)
        if getattr(self, "relay2_button", None) is None:
            self.relay2_button = QPushButton("LASER (Relay2): OFF")
        try:
            self.relay2_button.setCheckable(True)
            self._safe_connect("relay2_button", "clicked", lambda: self.toggle_relay(2))
        except Exception:
            pass
        accessory_layout.addWidget(self.relay2_button)
        # MOSFET Hold toggle (manual latch for MOSFET ON/OFF). Respects Safety and Trigger Mode.
        if getattr(self, "mosfet_hold_btn", None) is None:
            self.mosfet_hold_btn = QPushButton("MOSFET: OFF")
        try:
            self.mosfet_hold_btn.setCheckable(True)
            # prefer toggled signal which provides the checked state
            try:
                self._safe_connect("mosfet_hold_btn", "toggled", self._on_mosfet_hold_toggled)
            except Exception:
                try:
                    # fallback: clicked -> call with current checked state
                    self._safe_connect("mosfet_hold_btn", "clicked", lambda _: self._on_mosfet_hold_toggled(getattr(self, "mosfet_hold_btn", None) and self.mosfet_hold_btn.isChecked()))
                except Exception:
                    pass
        except Exception:
            pass
        accessory_layout.addWidget(self.mosfet_hold_btn)
        accessory_group.setLayout(accessory_layout)

        # Manual Movement & Firing (vertical, wrapped)
        manual_group = QGroupBox("Manual Movement & Firing")
        manual_layout = QVBoxLayout()
        manual_layout.setSpacing(8)
        manual_layout.setContentsMargins(8, 8, 8, 8)
        # step size
        manual_settings = QGridLayout()
        manual_settings.addWidget(QLabel("Step Size:"), 0, 0)
        if getattr(self, "step_size_input", None) is None:
            self.step_size_input = QSpinBox()
        try:
            self.step_size_input.setRange(1, 20)
            self.step_size_input.setValue(self.STEP_INCREMENT)
            self._safe_connect("step_size_input", "valueChanged", self.save_settings)
        except Exception:
            pass
        manual_settings.addWidget(self.step_size_input, 0, 1)
        # manual speed
        manual_settings.addWidget(QLabel("Manual Speed:"), 1, 0)
        speed_row2 = QHBoxLayout()
        if getattr(self, "manual_speed_slider", None) is None:
            self.manual_speed_slider = QSlider()
            try:
                try:
                    self.manual_speed_slider.setOrientation(
                        cast(Any, self._qt_enum("Horizontal", 1))
                    )
                except Exception:
                    pass
            except Exception:
                pass
        try:
            self.manual_speed_slider.setRange(1, 100)
            # Ensure a sensible default initial value so the visual knob
            # matches the textual label on first run.
            try:
                self.manual_speed_slider.setValue(50)
            except Exception:
                pass
            self._safe_connect(
                "manual_speed_slider", "valueChanged", self.save_settings
            )
        except Exception:
            pass
        if getattr(self, "manual_speed_label", None) is None:
            self.manual_speed_label = QLabel("50%")
        try:
            self.manual_speed_label.setFixedWidth(40)
            self._safe_connect(
                "manual_speed_slider",
                "valueChanged",
                lambda v: self.manual_speed_label.setText(f"{v}%"),
            )
        except Exception:
            pass
        speed_row2.addWidget(self.manual_speed_slider)
        speed_row2.addWidget(self.manual_speed_label)
        manual_settings.addLayout(speed_row2, 1, 1)
        
        # ========== TILT ENCODER & PID CONTROLS ==========
        # Encoder feedback enable toggle
        manual_settings.addWidget(QLabel("Tilt Encoder:"), 2, 0)
        if getattr(self, "encoder_enable_checkbox", None) is None:
            self.encoder_enable_checkbox = QCheckBox("Enable Feedback")
            self.encoder_enable_checkbox.setChecked(False)
            self._safe_connect(
                "encoder_enable_checkbox",
                "stateChanged",
                lambda: self.enable_encoder_feedback(
                    self.encoder_enable_checkbox.isChecked() if getattr(self, "encoder_enable_checkbox", None) else False
                )
            )
        manual_settings.addWidget(self.encoder_enable_checkbox, 2, 1)
        
        # PID control enable toggle
        manual_settings.addWidget(QLabel("PID Control:"), 3, 0)
        if getattr(self, "pid_enable_checkbox", None) is None:
            self.pid_enable_checkbox = QCheckBox("Enable Correction")
            self.pid_enable_checkbox.setChecked(False)
            self._safe_connect(
                "pid_enable_checkbox",
                "stateChanged",
                lambda: self.enable_tilt_pid_control(
                    self.pid_enable_checkbox.isChecked() if getattr(self, "pid_enable_checkbox", None) else False
                )
            )
        manual_settings.addWidget(self.pid_enable_checkbox, 3, 1)
        
        # Homing speed control
        manual_settings.addWidget(QLabel("Homing Speed:"), 4, 0)
        homing_speed_row = QHBoxLayout()
        if getattr(self, "home_speed_slider", None) is None:
            self.home_speed_slider = QSlider()
            try:
                self.home_speed_slider.setOrientation(
                    cast(Any, self._qt_enum("Horizontal", 1))
                )
            except Exception:
                pass
        try:
            self.home_speed_slider.setRange(1, 100)
            self.home_speed_slider.setValue(self.home_speed_percent)
            self._safe_connect(
                "home_speed_slider",
                "valueChanged",
                lambda v: self.set_home_speed(v)
            )
        except Exception:
            pass
        if getattr(self, "home_speed_label", None) is None:
            self.home_speed_label = QLabel(f"{self.home_speed_percent}%")
        try:
            self.home_speed_label.setFixedWidth(40)
            self._safe_connect(
                "home_speed_slider",
                "valueChanged",
                lambda v: self.home_speed_label.setText(f"{v}%"),
            )
        except Exception:
            pass
        homing_speed_row.addWidget(self.home_speed_slider)
        homing_speed_row.addWidget(self.home_speed_label)
        manual_settings.addLayout(homing_speed_row, 4, 1)
        # ========== END TILT ENCODER & PID CONTROLS ==========
        
        manual_layout.addLayout(manual_settings)

        # Dpad
        pad_layout = QGridLayout()
        pad_layout.setSpacing(6)
        if getattr(self, "btn_up", None) is None:
            self.btn_up = QPushButton("▲")
        if getattr(self, "btn_down", None) is None:
            self.btn_down = QPushButton("▼")
        if getattr(self, "btn_left", None) is None:
            self.btn_left = QPushButton("◀")
        if getattr(self, "btn_right", None) is None:
            self.btn_right = QPushButton("▶")
        if getattr(self, "btn_center", None) is None:
            self.btn_center = QPushButton("●")
        for b in (
            self.btn_up,
            self.btn_down,
            self.btn_left,
            self.btn_right,
            self.btn_center,
        ):
            try:
                b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                b.setMinimumSize(28, 28)
                try:
                    # Ensure buttons are enabled so manual controls always accept input
                    b.setEnabled(True)
                except Exception:
                    pass
            except Exception:
                pass
        pad_layout.addWidget(self.btn_up, 0, 1)
        pad_layout.addWidget(self.btn_left, 1, 0)
        pad_layout.addWidget(self.btn_center, 1, 1)
        pad_layout.addWidget(self.btn_right, 1, 2)
        pad_layout.addWidget(self.btn_down, 2, 1)
        # Connect D-pad buttons to manual movement (pressed = start move, released = stop)
        try:
            # Use lambdas that read current step size at call time via safe helper
            # NOTE: tilt direction inverted in firmware; flip the sign here so
            # the UI arrows match physical motion. Use safe helper to read step
            # size at call time.
            self._safe_connect(
                "btn_up",
                "pressed",
                lambda _=None: self.move_manual(
                    pan=0,
                    tilt=self._safe_int_widget_value(
                        "step_size_input", self.STEP_INCREMENT
                    ),
                ),
            )
            self._safe_connect("btn_up", "released", self.manual_control_released)
            self._safe_connect(
                "btn_down",
                "pressed",
                lambda _=None: self.move_manual(
                    pan=0,
                    tilt=-self._safe_int_widget_value(
                        "step_size_input", self.STEP_INCREMENT
                    ),
                ),
            )
            self._safe_connect("btn_down", "released", self.manual_control_released)
            self._safe_connect(
                "btn_left",
                "pressed",
                lambda _=None: self.move_manual(
                    pan=-self._safe_int_widget_value(
                        "step_size_input", self.STEP_INCREMENT
                    ),
                    tilt=0,
                ),
            )
            self._safe_connect("btn_left", "released", self.manual_control_released)
            self._safe_connect(
                "btn_right",
                "pressed",
                lambda _=None: self.move_manual(
                    pan=self._safe_int_widget_value(
                        "step_size_input", self.STEP_INCREMENT
                    ),
                    tilt=0,
                ),
            )
            self._safe_connect("btn_right", "released", self.manual_control_released)
            self._safe_connect(
                "btn_center", "pressed", lambda _=None: self.move_manual(pan=0, tilt=0)
            )
            self._safe_connect("btn_center", "released", self.manual_control_released)
        except Exception:
            pass
        for i in range(3):
            pad_layout.setRowStretch(i, 1)
            pad_layout.setColumnStretch(i, 1)
        manual_layout.addLayout(pad_layout)

        # position label
        pos_layout = QHBoxLayout()
        if getattr(self, "position_label", None) is None:
            self.position_label = QLabel("PAN: 90° TILT: 80°")
        try:
            try:
                self.position_label.setAlignment(
                    cast(Any, getattr(Qt, "AlignCenter", 0))
                )
            except Exception:
                pass
        except Exception:
            pass
        pos_layout.addWidget(self.position_label)
        manual_layout.addLayout(pos_layout)

        # fire controls
        fire_controls = QGridLayout()
        fire_controls.addWidget(QLabel("Trigger Mode:"), 0, 0)
        if getattr(self, "trigger_mode_combo", None) is None:
            self.trigger_mode_combo = QComboBox()
        try:
            if self.trigger_mode_combo.count() == 0:
                self.trigger_mode_combo.addItem("Water (MOSFET)")
                self.trigger_mode_combo.addItem("Projectile (BB Servo)")
            self._safe_connect(
                "trigger_mode_combo", "currentIndexChanged", self.set_trigger_mode
            )
        except Exception:
            pass
        fire_controls.addWidget(self.trigger_mode_combo, 0, 1)
        fire_controls.addWidget(QLabel("Auto-Fire Cooldown (s):"), 1, 0)
        if getattr(self, "trigger_cooldown_input", None) is None:
            self.trigger_cooldown_input = QDoubleSpinBox()
        try:
            self.trigger_cooldown_input.setRange(0.1, 10.0)
            self.trigger_cooldown_input.setValue(1.5)
            self._safe_connect(
                "trigger_cooldown_input", "valueChanged", self.save_settings
            )
        except Exception:
            pass
        fire_controls.addWidget(self.trigger_cooldown_input, 1, 1)
        # NOTE: manual_auto_fire_checkbox removed. Auto-fire is now controlled by the Safety (ARM) button.
        if getattr(self, "safety_button", None) is None:
            self.safety_button = QPushButton("Safety: LOCKED (No Fire)")
        try:
            self.safety_button.setCheckable(True)
            self.safety_button.setChecked(
                False if getattr(self, "safety_state", 1) == 1 else True
            )
            self._safe_connect("safety_button", "clicked", self.toggle_safety)
        except Exception:
            pass
        # place safety button in row 2 (single authoritative control for arming/auto-fire)
        fire_controls.addWidget(self.safety_button, 2, 0, 1, 2)
        # Rapid-fire MOSFET controls (rate, duty, enable)
        try:
            fire_controls.addWidget(QLabel("Rapid-Fire (Hz):"), 3, 0)
            if getattr(self, "rapid_fire_rate_spin", None) is None:
                self.rapid_fire_rate_spin = QSpinBox()
            try:
                # Reasonable default: 1 Hz..200 Hz, step 1
                self.rapid_fire_rate_spin.setRange(1, getattr(self, "rapid_fire_max_hz", 200))
                self.rapid_fire_rate_spin.setValue(getattr(self, "rapid_fire_rate_hz", 1))
                self.rapid_fire_rate_spin.setSingleStep(1)
                try:
                    self._safe_connect(
                        "rapid_fire_rate_spin", "valueChanged", self._on_rapid_rate_changed
                    )
                except Exception:
                    try:
                        self.rapid_fire_rate_spin.valueChanged.connect(self._on_rapid_rate_changed)
                    except Exception:
                        pass
            except Exception:
                pass
            fire_controls.addWidget(self.rapid_fire_rate_spin, 3, 1)

            fire_controls.addWidget(QLabel("Duty (%):"), 5, 0)
            if getattr(self, "rapid_fire_duty_slider", None) is None:
                self.rapid_fire_duty_slider = QSlider(Qt.Horizontal)
            try:
                self.rapid_fire_duty_slider.setRange(1, 100)
                self.rapid_fire_duty_slider.setValue(int(getattr(self, "rapid_fire_duty", 0.5) * 100))
                try:
                    self._safe_connect(
                        "rapid_fire_duty_slider", "valueChanged", self._on_rapid_duty_changed
                    )
                except Exception:
                    try:
                        self.rapid_fire_duty_slider.valueChanged.connect(self._on_rapid_duty_changed)
                    except Exception:
                        pass
            except Exception:
                pass
            fire_controls.addWidget(self.rapid_fire_duty_slider, 5, 1)

            if getattr(self, "rapid_fire_enable_checkbox", None) is None:
                self.rapid_fire_enable_checkbox = QCheckBox("Enable Rapid-Fire")
            try:
                try:
                    self._safe_connect(
                        "rapid_fire_enable_checkbox", "toggled", self._on_rapid_fire_toggled
                    )
                except Exception:
                    try:
                        self.rapid_fire_enable_checkbox.toggled.connect(self._on_rapid_fire_toggled)
                    except Exception:
                        pass
            except Exception:
                pass
            fire_controls.addWidget(self.rapid_fire_enable_checkbox, 6, 0, 1, 2)
            # Export rapid-fire preset to file
            if getattr(self, "export_rapid_btn", None) is None:
                self.export_rapid_btn = QPushButton("Export RF Preset")
            try:
                try:
                    self._safe_connect("export_rapid_btn", "clicked", self.export_rapid_fire_preset)
                except Exception:
                    try:
                        self.export_rapid_btn.clicked.connect(self.export_rapid_fire_preset)
                    except Exception:
                        pass
            except Exception:
                pass
            fire_controls.addWidget(self.export_rapid_btn, 7, 0, 1, 2)
        except Exception:
            pass
        if getattr(self, "fire_button", None) is None:
            self.fire_button = QPushButton("FIRE (Manual)")
        try:
            self._safe_connect("fire_button", "pressed", lambda: self.set_fire_state(1))
            self._safe_connect(
                "fire_button", "released", lambda: self.set_fire_state(0)
            )
        except Exception:
            pass
        fire_controls.addWidget(self.fire_button, 4, 0, 1, 2)
        
        # ========== QUICK STRIKE BUTTON ==========
        # Quick Strike: Snap to last detected target at maximum speed, fire if armed, resume tracking
        if getattr(self, "lock_target_btn", None) is None:
            self.lock_target_btn = QPushButton("⚡ Quick Strike")
        try:
            self.lock_target_btn.setToolTip(
                "Snap to the last detected target at maximum speed. If armed, fires automatically when position is reached."
            )
            self._safe_connect("lock_target_btn", "clicked", self.quick_target_lock)
        except Exception:
            pass
        fire_controls.addWidget(self.lock_target_btn, 5, 0, 1, 2)
        # ========== END QUICK STRIKE BUTTON ==========
        
        manual_layout.addLayout(fire_controls)
        manual_group.setLayout(manual_layout)

        # Serial / Log output
        serial_output_group = QGroupBox("Serial / Log Output")
        serial_output_layout = QVBoxLayout()

        # Add small control row (Pause / Clear)
        try:
            serial_control_row = QHBoxLayout()
            # Pause/Resume Log button
            if getattr(self, "pause_serial_btn", None) is None:
                self.pause_serial_btn = QPushButton("Pause Log")
            try:
                self.pause_serial_btn.setCheckable(True)
                # wire to instance-bound toggle helper (safe connect may be deferred)
                try:
                    self._safe_connect("pause_serial_btn", "toggled", self.toggle_serial_pause)
                except Exception:
                    try:
                        self.pause_serial_btn.toggled.connect(self.toggle_serial_pause)
                    except Exception:
                        pass
            except Exception:
                pass

            # Clear Log button
            if getattr(self, "clear_serial_btn", None) is None:
                self.clear_serial_btn = QPushButton("Clear Log")
            try:
                self._safe_connect("clear_serial_btn", "clicked", self.clear_serial_log)
            except Exception:
                try:
                    self.clear_serial_btn.clicked.connect(self.clear_serial_log)
                except Exception:
                    pass

            # Export Log button
            if getattr(self, "export_serial_btn", None) is None:
                self.export_serial_btn = QPushButton("Export Log")
            try:
                # connect if handler already exists; if not, _safe_connect in __init__ will attach later
                try:
                    self._safe_connect("export_serial_btn", "clicked", self.export_serial_log)
                except Exception:
                    try:
                        self.export_serial_btn.clicked.connect(self.export_serial_log)
                    except Exception:
                        pass
            except Exception:
                pass

            # Pause hardware serial TX (opt-in; disabled by default)
            if getattr(self, "pause_serial_tx_btn", None) is None:
                self.pause_serial_tx_btn = QPushButton("Pause TX")
            try:
                self.pause_serial_tx_btn.setCheckable(True)
                try:
                    self._safe_connect("pause_serial_tx_btn", "toggled", self.toggle_serial_tx)
                except Exception:
                    try:
                        self.pause_serial_tx_btn.toggled.connect(self.toggle_serial_tx)
                    except Exception:
                        pass
            except Exception:
                pass

            # Small buffer indicator label (shows "Paused — N buffered")
            if getattr(self, "serial_buffer_label", None) is None:
                try:
                    self.serial_buffer_label = QLabel("")
                    self.serial_buffer_label.setStyleSheet("color: #ffcc00; font-size: 9pt;")
                except Exception:
                    self.serial_buffer_label = QLabel("")

            serial_control_row.addWidget(self.pause_serial_btn)
            serial_control_row.addWidget(self.clear_serial_btn)
            serial_control_row.addWidget(self.export_serial_btn)
            serial_control_row.addWidget(self.pause_serial_tx_btn)
            serial_control_row.addStretch()
            serial_control_row.addWidget(self.serial_buffer_label)
            serial_output_layout.addLayout(serial_control_row)
        except Exception:
            # best-effort: continue without control row
            pass

        if getattr(self, "serial_output", None) is None:
            self.serial_output = QTextEdit()
        try:
            self.serial_output.setReadOnly(True)
        except Exception:
            pass
        serial_output_layout.addWidget(self.serial_output)
        serial_output_group.setLayout(serial_output_layout)

        # System status group
        status_group = QGroupBox("System")
        status_layout = QVBoxLayout()
        if getattr(self, "save_layout_btn", None) is None:
            self.save_layout_btn = QPushButton("Save Layout")
        try:
            self._safe_connect("save_layout_btn", "clicked", self.save_dock_layout)
        except Exception:
            pass
        status_layout.addWidget(self.save_layout_btn)
        if getattr(self, "reset_layout_btn", None) is None:
            self.reset_layout_btn = QPushButton("Reset Layout")
        try:
            self._safe_connect("reset_layout_btn", "clicked", self.reset_layout)
        except Exception:
            pass
        status_layout.addWidget(self.reset_layout_btn)
        if getattr(self, "save_defaults_btn", None) is None:
            self.save_defaults_btn = QPushButton("Save Settings as Default")
        try:
            self._safe_connect(
                "save_defaults_btn", "clicked", self.save_current_as_default
            )
        except Exception:
            pass
        status_layout.addWidget(self.save_defaults_btn)
        status_group.setLayout(status_layout)

        # Wrap behavior and manual groups in scroll areas for tall content
        try:
            # If we prepared a behavior_scroll earlier (with a dedicated
            # container), reuse it. Otherwise create a new QScrollArea and
            # attach the authoritative content (prefer the container if
            # available to ensure stable ownership).
            if getattr(self, 'behavior_container', None) is not None:
                # Prefer to reuse an existing scroll area if it exists on self
                behavior_scroll = getattr(self, 'behavior_scroll', None)
                if behavior_scroll is None:
                    behavior_scroll = QScrollArea()
                    behavior_scroll.setWidget(self.behavior_container)
                    behavior_scroll.setWidgetResizable(True)
                    self.behavior_scroll = behavior_scroll
            else:
                behavior_scroll = QScrollArea()
                try:
                    behavior_scroll.setWidget(behavior_group)
                except Exception:
                    # fallback to set as-is; some codepaths expect the raw group
                    pass
                behavior_scroll.setWidgetResizable(True)
        except Exception:
            behavior_scroll = behavior_group
        try:
            manual_scroll = QScrollArea()
            manual_scroll.setWidget(manual_group)
            manual_scroll.setWidgetResizable(True)
        except Exception:
            manual_scroll = manual_group

        # (duplicate wrap removed) — behavior_scroll and manual_scroll were
        # prepared above with preference for an existing self.behavior_container
        # and self.behavior_scroll. Avoid recreating them here which could
        # overwrite the container-backed scroll area and orphan widgets.

        # Add docks (use add_dock helper to avoid duplicates)
        try:
            self.add_dock("Configuration & Connection", settings_group, "left")
            self.add_dock("Home Position", home_group, "left")
            self.add_dock("Servo Limits", limits_group, "left")
            self.add_dock("Accessories", accessory_group, "left")

            self.add_dock("Target Detection", detection_group, "right")
            # YOLO Settings panel is created dynamically as floating window when YOLO mode is selected
                    
            self.add_dock("Tracking Behavior", behavior_scroll, "right")

            try:
                self._ensure_tracking_controls_attached()
            except Exception as e:
                print("Tracking slider restore failed:", e)

            try:
                # Create the presets panel with Save/Apply/Delete controls
                self.create_behavior_tracking_panel()
            except Exception as e:
                print("Presets panel creation failed:", e)
            
            self.add_dock("Manual Movement & Firing", manual_scroll, "right")
            # Place Serial/Log and System docks in the left column to match
            # the user's preferred layout (keeps logs and system controls together).
            # Place the Serial / Log Output in the bottom (workspace) area so it
            # occupies only the central video width between left/right docks.
            try:
                self.add_dock("Serial / Log Output", serial_output_group, "bottom")
            except Exception:
                # fallback to left if bottom isn't supported on this platform
                try:
                    self.add_dock("Serial / Log Output", serial_output_group, "left")
                except Exception:
                    pass
            self.add_dock("System", status_group, "left")
            try:
                # add sniper dock to right as a dock widget (avoid duplicates)
                if getattr(self, "sniper_dock", None) is not None:
                    try:
                        # use helper to resolve the enum in a way the analyzer accepts
                        area = self._qt_dock_area("RightDockWidgetArea", 2)
                        try:
                            self.addDockWidget(cast(Any, area), self.sniper_dock)
                        except Exception:
                            try:
                                # fallback: attempt via helper directly
                                self.addDockWidget(
                                    self._qt_dock_area("RightDockWidgetArea", 2),
                                    self.sniper_dock,
                                )
                            except Exception:
                                pass
                    except Exception:
                        pass
            except Exception:
                pass
        except Exception:
            pass

        # Arrange docks deterministically to match the requested default layout.
        # Left column: Configuration & Connection -> System/Home (tabbed) -> Servo Limits -> Accessories -> Serial / Log Output
        # Right column: Sniper View -> Target Detection -> YOLO Settings -> Manual Movement & Firing / Tracking Behavior (tabbed)
        try:

            def _dock_variants(title):
                """Find a QDockWidget by several likely objectName/windowTitle variants."""
                try:
                    # Try common name forms used by add_dock (spaces -> underscores)
                    candidates = [
                        title,
                        title.replace(" ", "_"),
                        title.replace(" ", "_").replace("&", "_"),
                        title.replace("/", "_"),
                        title.replace(" / ", "_"),
                    ]
                    for n in candidates:
                        try:
                            obj = f"Dock_{n}"
                            d = self.findChild(QDockWidget, obj)
                            if d is not None:
                                return d
                        except Exception:
                            pass
                except Exception:
                    pass
                try:
                    # Fallback: match by windowTitle
                    for d in self.findChildren(QDockWidget):
                        try:
                            if d.windowTitle() == title:
                                return d
                        except Exception:
                            pass
                except Exception:
                    pass
                # Special-case: sniper dock may be pre-created with its own objectName
                try:
                    if title.lower().startswith("sniper"):
                        return getattr(self, "sniper_dock", None)
                except Exception:
                    pass
                return None

            # Resolve all docks we care about
            cfg = _dock_variants("Configuration & Connection")
            sys_dock = _dock_variants("System")
            home_dock = _dock_variants("Home Position")
            servo = _dock_variants("Servo Limits")
            acc = _dock_variants("Accessories")
            serial_dock = _dock_variants("Serial / Log Output")
            sniper = _dock_variants("Sniper Scope") or getattr(
                self, "sniper_dock", None
            )
            target = _dock_variants("Target Detection")
            yolo = _dock_variants("YOLO Settings")
            track = _dock_variants("Tracking Behavior")
            manual = _dock_variants("Manual Movement & Firing")

            # Helper to get Qt.Vertical safely
            try:
                orient_vertical = getattr(Qt, "Vertical", None)
            except Exception:
                orient_vertical = None

            # Left column ordering using splitDockWidget to stack vertically
            try:
                if cfg and sys_dock:
                    try:
                        # Place System below Configuration
                        self.splitDockWidget(cfg, sys_dock, orient_vertical)
                    except Exception:
                        pass
                if sys_dock and home_dock:
                    try:
                        # Tab System with Home Position
                        self.tabifyDockWidget(sys_dock, home_dock)
                    except Exception:
                        pass
                if cfg and servo:
                    try:
                        # Ensure Servo Limits sits beneath Configuration (or beneath system group)
                        self.splitDockWidget(cfg, servo, orient_vertical)
                    except Exception:
                        pass
                if servo and acc:
                    try:
                        self.splitDockWidget(servo, acc, orient_vertical)
                    except Exception:
                        pass
                if acc and serial_dock:
                    try:
                        self.splitDockWidget(acc, serial_dock, orient_vertical)
                    except Exception:
                        pass
            except Exception:
                pass

            # Right column ordering
            try:
                if sniper and target:
                    try:
                        self.splitDockWidget(sniper, target, orient_vertical)
                    except Exception:
                        pass
                if target and yolo:
                    try:
                        self.splitDockWidget(target, yolo, orient_vertical)
                    except Exception:
                        pass
                # Place the manual/tracking stack after YOLO
                if yolo and manual:
                    try:
                        self.splitDockWidget(yolo, manual, orient_vertical)
                    except Exception:
                        pass
                if manual and track:
                    try:
                        self.tabifyDockWidget(manual, track)
                    except Exception:
                        pass
                # Make manual widget taller so buttons are visible by default
                try:
                    if manual is not None:
                        mw = manual.widget()
                        if mw is not None:
                            try:
                                mw.setMinimumHeight(320)
                            except Exception:
                                pass
                except Exception:
                    pass
            except Exception:
                pass

            # Ensure sniper dock is explicitly placed in the right area
            # Default behavior: make the sniper a small floating scope (matches screenshot).
            try:
                if sniper is not None:
                    try:
                        # Make it floating by default so it appears as a small scope window.
                        try:
                            sniper.setFloating(True)
                        except Exception:
                            pass
                        # Give it a reasonable default floating size after the main window shows
                        try:
                            QTimer.singleShot(
                                120, lambda: (sniper.resize(360, 180), sniper.raise_())
                            )
                        except Exception:
                            try:
                                sniper.resize(360, 180)
                            except Exception:
                                pass
                    except Exception:
                        pass
            except Exception:
                pass

            # Final equalize to balance columns
            try:
                QTimer.singleShot(200, lambda: self.equalize_dock_columns())
            except Exception:
                try:
                    self.equalize_dock_columns()
                except Exception:
                    pass
        except Exception:
            pass

        # Dock behavior: allow nesting and tabbing
        try:
            self.setDockOptions(
                QMainWindow.AllowNestedDocks
                | QMainWindow.AllowTabbedDocks
                | QMainWindow.AnimatedDocks
            )
        except Exception:
            pass

        # Ensure equal starting column widths (non-destructive)
        try:
            QTimer.singleShot(250, lambda: self.equalize_dock_columns())
            # Ensure default stacked two-column layout after docks are created
            try:
                QTimer.singleShot(300, lambda: self.enforce_default_dock_layout())
            except Exception:
                pass
        except Exception:
            pass

        # Final window size
        try:
            self.setMinimumSize(1200, 800)
            self.setGeometry(100, 100, 1200, 800)
        except Exception:
            pass

        # Re-apply tooltip styles and texts after full UI is built to ensure all widgets receive tooltips
        try:
            self._apply_tooltip_styles_and_texts()
        except Exception:
            pass

        # Add a simple menu for diagnostics: Logging on/off and Dump Logs
        try:
            menubar = self.menuBar()
            tools_menu = None
            if menubar is not None:
                try:
                    tools_menu = menubar.addMenu("Tools")
                except Exception:
                    tools_menu = None
                # Add Help -> User Manual action (minimal, single try)
                try:
                    help_menu = menubar.addMenu("Help")
                    manual_action = help_menu.addAction("User Manual")
                    conn = getattr(manual_action, "triggered", None)
                    if conn is not None:
                        try:
                            c = getattr(conn, "connect", None)
                            if callable(c):
                                c(self.open_manual_window)
                        except Exception:
                            try:
                                manual_action.triggered.connect(self.open_manual_window)
                            except Exception:
                                pass
                except Exception:
                    pass

            if tools_menu is not None:
                # Servo Calibration Tool
                servo_calib_action = tools_menu.addAction("📏 Servo Calibration")
                try:
                    def open_servo_calibration():
                        try:
                            from subprocess import Popen
                            import sys
                            Popen([sys.executable, "servo_calibration_tool.py"])
                        except Exception as e:
                            try:
                                if hasattr(self, "enhancer"):
                                    self.enhancer.log_serial_output(
                                        f"Error opening servo calibration tool: {e}",
                                        fire=False,
                                    )
                            except Exception:
                                pass
                    servo_calib_action.triggered.connect(open_servo_calibration)
                except Exception:
                    pass
                
                # Idle Settings
                idle_settings_action = tools_menu.addAction("⚙️ Idle Settings")
                try:
                    def open_idle_settings():
                        try:
                            if not hasattr(self, '_idle_settings_window') or self._idle_settings_window is None:
                                self._idle_settings_window = IdleSettingsWindow(self, self.idle_modes)
                            self._idle_settings_window.show()
                            self._idle_settings_window.raise_()
                            self._idle_settings_window.activateWindow()
                        except Exception as e:
                            print(f"Error opening idle settings: {e}")
                    idle_settings_action.triggered.connect(open_idle_settings)
                except Exception:
                    pass
                
                # Keyboard Shortcuts
                keyboard_action = tools_menu.addAction("⌨️ Keyboard Shortcuts")
                try:
                    def open_keyboard_shortcuts():
                        try:
                            if KeyboardShortcutsWindow is not None:
                                if not hasattr(self, '_keyboard_shortcuts_window') or self._keyboard_shortcuts_window is None:
                                    self._keyboard_shortcuts_window = KeyboardShortcutsWindow(self, self)
                                self._keyboard_shortcuts_window.show()
                                self._keyboard_shortcuts_window.raise_()
                                self._keyboard_shortcuts_window.activateWindow()
                        except Exception as e:
                            print(f"Error opening keyboard shortcuts: {e}")
                    keyboard_action.triggered.connect(open_keyboard_shortcuts)
                except Exception:
                    pass
                
                # CODE FIXER - Search, Analyze & Fix Code
                code_fixer_action = tools_menu.addAction("🔧 Code Fixer")
                try:
                    def open_code_fixer():
                        try:
                            if CodeFixer is not None:
                                if not hasattr(self, '_code_fixer_window') or self._code_fixer_window is None:
                                    self._code_fixer_window = CodeFixer(os.path.dirname(os.path.abspath(__file__)), self)
                                self._code_fixer_window.show()
                                self._code_fixer_window.raise_()
                                self._code_fixer_window.activateWindow()
                        except Exception as e:
                            print(f"Error opening code fixer: {e}")
                    code_fixer_action.triggered.connect(open_code_fixer)
                except Exception:
                    pass
                
                # Floating Panel
                panel_action = tools_menu.addAction("📦 Floating Panel")
                try:
                    def open_floating_panel():
                        try:
                            if FloatingPanelWindow is not None:
                                if not hasattr(self, '_floating_panel_window') or self._floating_panel_window is None:
                                    self._floating_panel_window = FloatingPanelWindow(self)
                                self._floating_panel_window.show()
                                self._floating_panel_window.raise_()
                                self._floating_panel_window.activateWindow()
                        except Exception as e:
                            print(f"Error opening floating panel: {e}")
                    panel_action.triggered.connect(open_floating_panel)
                except Exception:
                    pass
                
                # Widget Management submenu
                try:
                    widget_mgmt_menu = tools_menu.addMenu("📦 Widget Management")
                    
                    def move_to_panel(widget_name, dock_widget):
                        """Move a dock widget to the floating panel."""
                        try:
                            if hasattr(self, '_floating_panel_window') and self._floating_panel_window:
                                self._floating_panel_window.add_dock_widget(dock_widget)
                                self.removeDockWidget(dock_widget)
                        except Exception as e:
                            print(f"Error moving {widget_name} to panel: {e}")
                    
                    # Add quick access to common widgets if they exist
                    try:
                        if hasattr(self, 'manual_control_dock') and self.manual_control_dock:
                            action = widget_mgmt_menu.addAction("Move Manual Control to Panel")
                            action.triggered.connect(lambda: move_to_panel("Manual Control", self.manual_control_dock))
                    except Exception:
                        pass
                    
                    try:
                        if hasattr(self, 'tracking_behavior_dock') and self.tracking_behavior_dock:
                            action = widget_mgmt_menu.addAction("Move Tracking Behavior to Panel")
                            action.triggered.connect(lambda: move_to_panel("Tracking Behavior", self.tracking_behavior_dock))
                    except Exception:
                        pass
                    
                    try:
                        if hasattr(self, 'video_dock') and self.video_dock:
                            action = widget_mgmt_menu.addAction("Move Video Feed to Panel")
                            action.triggered.connect(lambda: move_to_panel("Video Feed", self.video_dock))
                    except Exception:
                        pass
                    
                    widget_mgmt_menu.addSeparator()
                    
                    def return_all_to_main():
                        """Return all widgets from panel back to main window."""
                        try:
                            if hasattr(self, '_floating_panel_window') and self._floating_panel_window:
                                for dock in list(self._floating_panel_window.get_docked_widgets()):
                                    self._floating_panel_window.remove_dock_widget(dock)
                                    self.addDockWidget(cast(Any, Qt.LeftDockWidgetArea), dock)
                        except Exception as e:
                            print(f"Error returning widgets: {e}")
                    
                    action = widget_mgmt_menu.addAction("Return All to Main Window")
                    action.triggered.connect(return_all_to_main)
                    
                except Exception as e:
                    print(f"Error setting up widget management menu: {e}")
                
                tools_menu.addSeparator()
                
                # Disable / Enable State Logging
                self.toggle_log_action = cast(Any, tools_menu.addAction("Disable State Logging"))
                try:
                    self.toggle_log_action.setCheckable(True)
                    self.toggle_log_action.setChecked(False)
                except Exception:
                    pass

                def _toggle_log(checked):
                    enabled = not bool(checked)
                    try:
                        self.state_logger.enable(enabled)
                    except Exception:
                        pass
                    try:
                        self.toggle_log_action.setText(
                            "Enable State Logging" if not enabled else "Disable State Logging"
                        )
                    except Exception:
                        pass

                try:
                    conn = getattr(self.toggle_log_action, "toggled", None)
                    if conn is not None:
                        try:
                            c = getattr(conn, "connect", None)
                            if callable(c):
                                c(_toggle_log)
                        except Exception:
                            pass
                except Exception:
                    pass

                # Auto-equalize docks toggle
                self.auto_equalize_action = cast(Any, tools_menu.addAction("Auto Equalize Dock Columns"))
                try:
                    self.auto_equalize_action.setCheckable(True)
                    self.auto_equalize_action.setChecked(bool(getattr(self, "auto_equalize_dock_columns", True)))
                except Exception:
                    pass

                def _toggle_auto_equalize(checked):
                    enabled = bool(checked)
                    try:
                        self.auto_equalize_dock_columns = enabled
                    except Exception:
                        pass
                    try:
                        self.auto_equalize_action.setText(
                            "Auto Equalize Dock Columns" if enabled else "Auto Equalize Dock Columns (disabled)"
                        )
                    except Exception:
                        pass
                    if enabled:
                        try:
                            self.equalize_dock_columns()
                        except Exception:
                            pass

                try:
                    conn = getattr(self.auto_equalize_action, "toggled", None)
                    if conn is not None:
                        try:
                            c = getattr(conn, "connect", None)
                            if callable(c):
                                c(_toggle_auto_equalize)
                        except Exception:
                            pass
                except Exception:
                    pass

                # Force exact dock widths (optional)
                self.force_exact_action = cast(Any, tools_menu.addAction("Force Exact Dock Widths"))
                try:
                    self.force_exact_action.setCheckable(True)
                    self.force_exact_action.setChecked(bool(getattr(self, "force_exact_dock_widths", False)))
                except Exception:
                    pass

                def _toggle_force_exact(checked):
                    enabled = bool(checked)
                    try:
                        self.force_exact_dock_widths = enabled
                    except Exception:
                        pass
                    try:
                        self.force_exact_action.setText(
                            "Force Exact Dock Widths" if enabled else "Force Exact Dock Widths (disabled)"
                        )
                    except Exception:
                        pass

                    if not enabled:
                        # remove max-width constraints so layout becomes flexible again
                        try:
                            docks = [d for d in self.findChildren(QDockWidget)]
                            for d in docks:
                                try:
                                    d.setMaximumWidth(16777215)
                                except Exception:
                                    pass
                                try:
                                    w = d.widget()
                                    if w is not None:
                                        try:
                                            w.setMaximumWidth(16777215)
                                        except Exception:
                                            pass
                                        try:
                                            w.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                                        except Exception:
                                            pass
                                except Exception:
                                    pass
                        except Exception:
                            pass

                    try:
                        self.equalize_dock_columns()
                    except Exception:
                        pass

                try:
                    conn = getattr(self.force_exact_action, "toggled", None)
                    if conn is not None:
                        try:
                            c = getattr(conn, "connect", None)
                            if callable(c):
                                c(_toggle_force_exact)
                        except Exception:
                            pass
                except Exception:
                    pass

                # Auto-show sniper toggle
                self.auto_show_sniper_action = cast(Any, tools_menu.addAction("Auto-show Sniper"))
                try:
                    self.auto_show_sniper_action.setCheckable(True)
                    self.auto_show_sniper_action.setChecked(bool(getattr(self, "auto_show_sniper", True)))
                except Exception:
                    pass

                def _toggle_auto_show_sniper(checked):
                    enabled = bool(checked)
                    try:
                        self.auto_show_sniper = enabled
                    except Exception:
                        pass
                    try:
                        self.auto_show_sniper_action.setText(
                            "Auto-show Sniper" if enabled else "Auto-show Sniper (disabled)"
                        )
                    except Exception:
                        pass
                    try:
                        self.save_settings()
                    except Exception:
                        pass

                try:
                    conn = getattr(self.auto_show_sniper_action, "toggled", None)
                    if conn is not None:
                        try:
                            c = getattr(conn, "connect", None)
                            if callable(c):
                                c(_toggle_auto_show_sniper)
                        except Exception:
                            pass
                except Exception:
                    pass

                # Add separator before checklist
                tools_menu.addSeparator()
                
                # Code Checklist action
                if ChecklistPanel is not None:
                    self.show_checklist_action = cast(Any, tools_menu.addAction("📋 Show Code Checklist"))
                    
                    def _show_checklist():
                        try:
                            if not hasattr(self, '_checklist_panel') or self._checklist_panel is None:
                                self._checklist_panel = ChecklistPanel(self)
                            self._checklist_panel.show()
                            self._checklist_panel.raise_()
                            self._checklist_panel.activateWindow()
                        except Exception as e:
                            try:
                                if hasattr(self, "enhancer") and self.enhancer:
                                    self.enhancer.log_serial_output(f"Checklist panel error: {e}", fire=False)
                            except Exception:
                                print(f"Checklist error: {e}")
                    
                    try:
                        conn_checklist = getattr(self.show_checklist_action, "triggered", None)
                        if conn_checklist is not None:
                            try:
                                c_checklist = getattr(conn_checklist, "connect", None)
                                if callable(c_checklist):
                                    c_checklist(_show_checklist)
                            except Exception:
                                pass
                    except Exception:
                        pass
                
                # Idle Settings action
                if IdleSettingsWindow is not None:
                    self.show_idle_settings_action = cast(Any, tools_menu.addAction("⚙️ Idle Settings"))
                    
                    def _show_idle_settings():
                        try:
                            if not hasattr(self, '_idle_settings_window') or self._idle_settings_window is None:
                                self._idle_settings_window = IdleSettingsWindow(self, self.idle_modes)
                            self._idle_settings_window.show()
                            self._idle_settings_window.raise_()
                            self._idle_settings_window.activateWindow()
                        except Exception as e:
                            try:
                                if hasattr(self, "enhancer") and self.enhancer:
                                    self.enhancer.log_serial_output(f"Idle settings error: {e}", fire=False)
                            except Exception:
                                print(f"Idle settings error: {e}")
                    
                    try:
                        conn_idle = getattr(self.show_idle_settings_action, "triggered", None)
                        if conn_idle is not None:
                            try:
                                c_idle = getattr(conn_idle, "connect", None)
                                if callable(c_idle):
                                    c_idle(_show_idle_settings)
                            except Exception:
                                pass
                    except Exception:
                        pass

                # Dump logs action
                self.dump_logs_action = cast(Any, tools_menu.addAction("Dump State Log to file..."))

                def _dump_logs():
                    try:
                        fname = os.path.join(os.getcwd(), "state_log.txt")
                        self.state_logger.dump_to_file(fname, append=False)
                        try:
                            if hasattr(self, "enhancer") and self.enhancer:
                                self.enhancer.log_serial_output(f"State log dumped to: {fname}", fire=False)
                        except Exception:
                            pass
                    except Exception as e:
                        try:
                            if hasattr(self, "enhancer") and self.enhancer:
                                self.enhancer.log_serial_output(f"State log dump failed: {e}", fire=False)
                        except Exception:
                            pass

                try:
                    conn2 = getattr(self.dump_logs_action, "triggered", None)
                    if conn2 is not None:
                        try:
                            c2 = getattr(conn2, "connect", None)
                            if callable(c2):
                                c2(_dump_logs)
                        except Exception:
                            pass
                except Exception:
                    pass
        except Exception:
            pass

        # Attach enhancer helpers
        try:
            if hasattr(self, "enhancer"):
                try:
                    self.enhancer.attach_serial_console(self.serial_output)
                except Exception:
                    pass
                try:
                    self.enhancer.style_toggle_button(
                        getattr(self, "safety_button", None)
                    )
                    self.enhancer.style_toggle_button(
                        getattr(self, "relay1_button", None)
                    )
                    self.enhancer.style_toggle_button(
                        getattr(self, "relay2_button", None)
                    )
                except Exception:
                    pass
        except Exception:
            pass

        # Widgets menu: quick open/restore of any docked widget and a persistent
        # bottom 'Workspace' dock that is empty by default (user can dock into it).
        try:
            try:
                widgets_menu = menubar.addMenu("Widgets")
            except Exception:
                widgets_menu = None
            try:
                # Insert Widgets menu before Tools for convenience if Tools exists
                if widgets_menu is not None and tools_menu is not None:
                    try:
                        menubar.insertMenu(tools_menu.menuAction(), widgets_menu)
                    except Exception:
                        pass
            except Exception:
                pass

            # Build a list of known docks and backing widgets (local variables from init_ui)
            try:
                widget_items = [
                    ("Configuration & Connection", settings_group),
                    ("Home Position", home_group),
                    ("Servo Limits", limits_group),
                    ("Accessories", accessory_group),
                    ("Target Detection", detection_group),
                    ("YOLO Settings", getattr(self, "yolo_settings_group", None)),
                    ("Tracking Behavior", behavior_group),
                    ("Manual Movement & Firing", manual_group),
                    ("Serial / Log Output", serial_output_group),
                    ("System", status_group),
                    ("Sniper Scope", getattr(self, "sniper_dock", None)),
                    ("Workspace", workspace_container),
                ]
            except Exception:
                widget_items = []
            
            # Auto-discover any dock widgets not in the list
            try:
                found_titles = {t for t, _ in widget_items}
                for dock in self.findChildren(QDockWidget):
                    title = dock.windowTitle()
                    if title and title not in found_titles and title != "Panels":
                        # Add discovered docks with None backing widget
                        widget_items.append((title, None))
            except Exception:
                pass

            def _find_dock_by_title(t):
                try:
                    for d in self.findChildren(QDockWidget):
                        try:
                            if d.windowTitle() == t:
                                return d
                        except Exception:
                            pass
                except Exception:
                    pass
                return None

            def _make_toggle(title, backing_widget):
                try:
                    act = cast(Any, widgets_menu.addAction(title))
                except Exception:
                    return
                try:
                    act.setCheckable(True)
                except Exception:
                    pass

                # initialize checked state
                try:
                    d = _find_dock_by_title(title)
                    if d is not None:
                        try:
                            act.setChecked(bool(d.isVisible()))
                        except Exception:
                            pass
                except Exception:
                    pass

                def _toggle(checked, title=title, action_ref=act, bw=backing_widget):
                    try:
                        d = _find_dock_by_title(title)
                        if d is not None:
                            try:
                                if checked:
                                    d.show()
                                    try:
                                        d.raise_()
                                    except Exception:
                                        pass
                                else:
                                    d.hide()
                                try:
                                    action_ref.setChecked(bool(d.isVisible()))
                                except Exception:
                                    pass
                                # If the user toggled the sniper dock via the Widgets menu,
                                # record that intent so auto-update logic won't re-open it
                                try:
                                    if title.lower().startswith("sniper"):
                                        try:
                                            self._sniper_user_closed = not bool(checked)
                                        except Exception:
                                            pass
                                except Exception:
                                    pass
                            except Exception:
                                pass
                        else:
                            # try to recreate from backing widget if available
                            try:
                                if bw is not None:
                                    nd = self.add_dock(title, bw, "left")
                                    if nd is not None and checked:
                                        try:
                                            nd.show()
                                            nd.raise_()
                                        except Exception:
                                            pass
                                        try:
                                            action_ref.setChecked(True)
                                        except Exception:
                                            pass
                            except Exception:
                                pass
                    except Exception:
                        pass

                try:
                    # connect the QAction toggled -> _toggle
                    try:
                        conn = getattr(act, "toggled", None)
                        if conn is not None:
                            try:
                                c = getattr(conn, "connect", None)
                                if callable(c):
                                    c(_toggle)
                            except Exception:
                                pass
                    except Exception:
                        pass
                except Exception:
                    pass

                # Sync the action when the dock's visibility changes
                try:
                    d = _find_dock_by_title(title)
                    if d is not None:
                        try:
                            vchg = getattr(d, "visibilityChanged", None)
                            if vchg is not None:
                                try:
                                    vchg.connect(lambda vis, a=act: a.setChecked(bool(vis)))
                                except Exception:
                                    pass
                        except Exception:
                            pass
                except Exception:
                    pass

            # create items
            try:
                for t, w in widget_items:
                    try:
                        _make_toggle(t, w)
                    except Exception:
                        pass
            except Exception:
                pass
            
            # Add Scope Visual Settings floating window toggle
            try:
                if widgets_menu is not None:
                    widgets_menu.addSeparator()
                    scope_settings_action = widgets_menu.addAction("Scope Visual Settings")
                    self.scope_settings_action = scope_settings_action
                    scope_settings_action.setCheckable(True)
                    scope_settings_action.setChecked(False)
                    
                    def toggle_scope_settings(checked):
                        try:
                            scope_window = getattr(self, 'scope_settings_window', None)
                            if scope_window is not None:
                                if checked:
                                    scope_window.show()
                                    scope_window.raise_()
                                    scope_window.activateWindow()
                                else:
                                    scope_window.hide()
                        except Exception:
                            pass
                    
                    scope_settings_action.toggled.connect(toggle_scope_settings)
                    
                    # Sync action when window visibility changes (via close button)
                    try:
                        scope_window = getattr(self, 'scope_settings_window', None)
                        if scope_window is not None:
                            def on_scope_window_closed():
                                try:
                                    scope_settings_action.setChecked(False)
                                except Exception:
                                    pass
                            scope_window.closeEvent = lambda event: (on_scope_window_closed(), event.accept())
                    except Exception:
                        pass
            except Exception:
                pass
        except Exception:
            pass

    def reset_styles(self):
        """Clears all local stylesheets from widgets before applying the global theme."""
        for widget in self.findChildren(QWidget):
            widget.setStyleSheet("")
    def open_manual_window(self):
        """Open a non-modal dialog that displays the Markdown user manual with
        a small search toolbar (case/whole-word/highlight-all, prev/next navigation).

        The dialog is non-blocking and reused if already open.
        """
        try:
            # Localize imports to avoid touching top-level imports
            from PyQt5.QtWidgets import (
                QDialog,
                QTextBrowser,
                QToolBar,
                QToolButton,
                QTextEdit,
                QLineEdit,
                QLabel,
                QVBoxLayout,
                QCheckBox,
            )
            from PyQt5.QtGui import QTextCursor, QTextCharFormat, QColor
            from PyQt5.QtCore import Qt
            import re, os

            # Reuse existing dialog if present
            if getattr(self, "manual_dialog", None) is not None:
                try:
                    self.manual_dialog.show()
                    self.manual_dialog.raise_()
                    self.manual_dialog.activateWindow()
                    return
                except Exception:
                    pass

            dlg = QDialog(self)
            dlg.setWindowTitle("User Manual")
            try:
                dlg.setWindowFlags(
                    dlg.windowFlags()
                    | Qt.WindowType.WindowMinimizeButtonHint
                    | Qt.WindowType.WindowMaximizeButtonHint
                    | Qt.WindowType.WindowCloseButtonHint
                )
            except Exception:
                try:
                    dlg.setWindowFlags(Qt.WindowType.Window)
                except Exception:
                    pass
            dlg.setModal(False)
            dlg.resize(920, 680)

            layout = QVBoxLayout(dlg)

            # Toolbar and search controls
            toolbar = QToolBar()
            search_box = QLineEdit()
            search_box.setPlaceholderText("Search manual (Enter = next)")
            prev_btn = QToolButton(); prev_btn.setText("◀")
            next_btn = QToolButton(); next_btn.setText("▶")
            case_cb = QCheckBox("Case")
            whole_cb = QCheckBox("Whole")
            highlight_cb = QCheckBox("Highlight All"); highlight_cb.setChecked(True)
            match_label = QLabel("")

            try:
                toolbar.addWidget(QLabel("Find:"))
                toolbar.addWidget(search_box)
                toolbar.addWidget(prev_btn)
                toolbar.addWidget(next_btn)
                toolbar.addWidget(match_label)
                toolbar.addSeparator()
                toolbar.addWidget(case_cb)
                toolbar.addWidget(whole_cb)
                toolbar.addWidget(highlight_cb)
            except Exception:
                pass

            layout.addWidget(toolbar)

            # Markdown viewer
            manual = QTextBrowser()
            manual.setOpenExternalLinks(True)

            content = ""
            try:
                base = os.path.dirname(__file__)
                # Try multiple manual locations (prefer complete version)
                possible_paths = [
                    os.path.join(base, "USER_MANUAL_COMPLETE.md"),  # NEW: Complete version
                    os.path.join(os.getcwd(), "USER_MANUAL_COMPLETE.md"),
                    os.path.join(base, "docs", "USER_MANUAL.md"),  # OLD: Legacy location
                    os.path.join(os.getcwd(), "docs", "USER_MANUAL.md"),
                    os.path.join(base, "USER_MANUAL.md"),
                ]
                
                path = None
                for p in possible_paths:
                    if os.path.exists(p):
                        path = p
                        break
                
                if path and os.path.exists(path):
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
            except Exception:
                content = ""

            # Convert Markdown to HTML for better rendering
            try:
                try:
                    import markdown
                    html_content = markdown.markdown(content, extensions=['tables', 'fenced_code'])
                except ImportError:
                    # Fallback: simple Markdown-to-HTML conversion
                    import re
                    html_content = content
                    # Headers
                    html_content = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html_content, flags=re.MULTILINE)
                    html_content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html_content, flags=re.MULTILINE)
                    html_content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html_content, flags=re.MULTILINE)
                    # Bold and italic
                    html_content = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', html_content)
                    html_content = re.sub(r'\*(.+?)\*', r'<i>\1</i>', html_content)
                    html_content = re.sub(r'_(.+?)_', r'<i>\1</i>', html_content)
                    # Code blocks
                    html_content = re.sub(r'```(.+?)```', r'<pre><code>\1</code></pre>', html_content, flags=re.DOTALL)
                    # Inline code
                    html_content = re.sub(r'`(.+?)`', r'<code>\1</code>', html_content)
                    # Links
                    html_content = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', html_content)
                    # Lists
                    html_content = re.sub(r'^- (.+)$', r'<li>\1</li>', html_content, flags=re.MULTILINE)
                    html_content = re.sub(r'(<li>.+</li>)', r'<ul>\1</ul>', html_content, flags=re.DOTALL)
                    # Line breaks
                    html_content = html_content.replace('\n', '<br>')
                
                manual.setHtml(html_content)
            except Exception:
                try:
                    manual.setPlainText(content)
                except Exception:
                    pass

            layout.addWidget(manual)

            # Dialog state
            dlg.manual_browser = manual
            dlg.search_box = search_box
            dlg.prev_btn = prev_btn
            dlg.next_btn = next_btn
            dlg.case_cb = case_cb
            dlg.whole_cb = whole_cb
            dlg.highlight_cb = highlight_cb
            dlg.match_label = match_label
            dlg.matches = []
            dlg.current_index = -1

            def _clear_highlights():
                try:
                    manual.setExtraSelections([])
                except Exception:
                    pass

            def _update_highlights():
                try:
                    extra = []
                    fmt_all = QTextCharFormat()
                    fmt_cur = QTextCharFormat()
                    if dlg.highlight_cb.isChecked():
                        fmt_all.setBackground(QColor("#ffff88"))
                    fmt_cur.setBackground(QColor("#ffcc66"))
                    doc = manual.document()
                    if not dlg.matches:
                        manual.setExtraSelections([])
                        return
                    if not dlg.highlight_cb.isChecked():
                        idx = dlg.current_index if 0 <= dlg.current_index < len(dlg.matches) else 0
                        s, e = dlg.matches[idx]
                        sel = QTextEdit.ExtraSelection()
                        cur = QTextCursor(doc)
                        cur.setPosition(s)
                        cur.setPosition(e, QTextCursor.KeepAnchor)
                        sel.cursor = cur
                        sel.format = fmt_cur
                        extra.append(sel)
                        manual.setExtraSelections(extra)
                        return
                    for i, (s, e) in enumerate(dlg.matches):
                        sel = QTextEdit.ExtraSelection()
                        cur = QTextCursor(doc)
                        cur.setPosition(s)
                        cur.setPosition(e, QTextCursor.KeepAnchor)
                        sel.cursor = cur
                        sel.format = fmt_cur if i == dlg.current_index else fmt_all
                        extra.append(sel)
                    manual.setExtraSelections(extra)
                except Exception:
                    pass

            def _go_to_current():
                try:
                    if not dlg.matches:
                        return
                    if dlg.current_index < 0:
                        dlg.current_index = 0
                    s, e = dlg.matches[dlg.current_index]
                    c = manual.textCursor()
                    c.setPosition(s)
                    c.setPosition(e, QTextCursor.KeepAnchor)
                    manual.setTextCursor(c)
                    try:
                        manual.ensureCursorVisible()
                    except Exception:
                        try:
                            manual.centerCursor()
                        except Exception:
                            pass
                    try:
                        dlg.match_label.setText(f"{dlg.current_index+1}/{len(dlg.matches)}")
                    except Exception:
                        pass
                except Exception:
                    pass

            def _find_matches():
                try:
                    q = search_box.text()
                    text = manual.toPlainText() or ""
                    if not q:
                        dlg.matches = []
                        dlg.current_index = -1
                        dlg.match_label.setText("0/0")
                        _clear_highlights()
                        return
                    flags = 0
                    if not case_cb.isChecked():
                        flags = re.IGNORECASE
                    pattern = re.escape(q)
                    if whole_cb.isChecked():
                        pattern = r"\b" + pattern + r"\b"
                    matches = []
                    for m in re.finditer(pattern, text, flags):
                        matches.append((m.start(), m.end()))
                    dlg.matches = matches
                    if not matches:
                        dlg.current_index = -1
                        dlg.match_label.setText("0/0")
                        _clear_highlights()
                        return
                    if dlg.current_index < 0 or dlg.current_index >= len(matches):
                        dlg.current_index = 0
                    dlg.match_label.setText(f"{dlg.current_index+1}/{len(matches)}")
                    _update_highlights()
                    _go_to_current()
                except Exception:
                    pass

            def _next():
                try:
                    if not dlg.matches:
                        return
                    dlg.current_index = (dlg.current_index + 1) % len(dlg.matches)
                    _update_highlights()
                    _go_to_current()
                except Exception:
                    pass

            def _prev():
                try:
                    if not dlg.matches:
                        return
                    dlg.current_index = (dlg.current_index - 1) % len(dlg.matches)
                    _update_highlights()
                    _go_to_current()
                except Exception:
                    pass

            try:
                search_box.textChanged.connect(lambda _=None: _find_matches())
                search_box.returnPressed.connect(lambda: _next())
                next_btn.clicked.connect(lambda: _next())
                prev_btn.clicked.connect(lambda: _prev())
                case_cb.toggled.connect(lambda _=None: _find_matches())
                whole_cb.toggled.connect(lambda _=None: _find_matches())
                highlight_cb.toggled.connect(lambda _=None: _update_highlights())
            except Exception:
                pass

            self.manual_dialog = dlg
            dlg.show()
        except Exception as e:
            try:
                self._safe_append_log(f"Failed to open manual dialog: {e}")
            except Exception:
                pass
    def eventFilter(self, a0, a1):
        """Capture Close events from the sniper dock so we can remember when
        the user explicitly closed it and avoid re-showing it automatically.
        Also lightly instrument clicks inside the settings area to help
        identify which UI actions set detection-suppression flags.
        """
        try:
            sniper = getattr(self, "sniper_dock", None)
            # Detect user close on the sniper dock
            if sniper is not None and a0 is sniper:
                try:
                    close_type = getattr(QEvent, "Close", None)
                    t = a1.type() if hasattr(a1, "type") else None
                    if close_type is not None and t == close_type:
                        # mark as user-closed so auto-update won't reopen it
                        self._sniper_user_closed = True
                except Exception:
                    pass

            # Instrument mouse clicks inside the settings area so we can quickly
            # identify which UI interaction triggers suppression behavior.
            try:
                mouse_press = getattr(QEvent, "MouseButtonPress", None)
                t2 = a1.type() if hasattr(a1, "type") else None
                if mouse_press is not None and t2 == mouse_press:
                    settings_grp = getattr(self, "settings_group", None) or getattr(self, "video_frame", None)
                    if settings_grp is not None and hasattr(settings_grp, "isAncestorOf") and settings_grp.isAncestorOf(a0):
                        try:
                            name = a0.objectName() if hasattr(a0, "objectName") else str(a0)
                        except Exception:
                            try:
                                name = str(a0)
                            except Exception:
                                name = "unknown"
                        diag = (
                            f"[UI CLICK] widget={name} type={type(a0).__name__} "
                            f"aiming_active={getattr(self,'aiming_active',False)} "
                            f"tracking_active={getattr(self,'tracking_active',False)} "
                            f"_suppress_detection_until={getattr(self,'_suppress_detection_until',0)} "
                            f"_suspend_tracking_until={getattr(self,'_suspend_tracking_until',0)}"
                        )
                        try:
                            if hasattr(self, "enhancer") and self.enhancer:
                                self.enhancer.log_serial_output(diag, fire=False)
                            else:
                                self._safe_append_log(diag)
                        except Exception:
                            try:
                                self._safe_append_log(diag)
                            except Exception:
                                pass
            except Exception:
                pass
        except Exception:
            pass

        # Return False so normal event processing continues.
        return False

    def keyPressEvent(self, event):
        """Handle global keyboard shortcuts for manual control and actions.

        Supports AWDS and Arrow keys for manual pan/tilt, Space for momentary
        fire, K to toggle Safety, T to toggle trigger mode, R to toggle rapid-fire,
        E to export rapid-fire preset, L to save layout, H to Go Home, C to center.
        """
        try:
            key = event.key()
            # avoid re-processing auto-repeat repeats for toggle actions, but allow repeats for movement
            is_repeat = False
            try:
                is_repeat = event.isAutoRepeat()
            except Exception:
                is_repeat = False

            step = self._safe_int_widget_value("step_size_input", self.STEP_INCREMENT)

            # Movement: W / Up
            if key in (Qt.Key.Key_W, Qt.Key.Key_Up):
                self.move_manual(pan=0, tilt=step)
                self._pressed_keys.add(key)
                return
            if key in (Qt.Key.Key_S, Qt.Key.Key_Down):
                self.move_manual(pan=0, tilt=-step)
                self._pressed_keys.add(key)
                return
            if key in (Qt.Key.Key_A, Qt.Key.Key_Left):
                self.move_manual(pan=-step, tilt=0)
                self._pressed_keys.add(key)
                return
            if key in (Qt.Key.Key_D, Qt.Key.Key_Right):
                self.move_manual(pan=step, tilt=0)
                self._pressed_keys.add(key)
                return

            # Center / Home
            if key == Qt.Key.Key_C:
                try:
                    self.move_manual(pan=0, tilt=0)
                except Exception:
                    pass
                return
            if key == Qt.Key.Key_H:
                try:
                    self.go_home()
                except Exception:
                    pass
                return

            # Fire (momentary)
            if key == Qt.Key_Space:
                try:
                    self.set_fire_state(1)
                    self._pressed_keys.add(key)
                except Exception:
                    pass
                return

            # Toggles and other actions (ignore repeats)
            if is_repeat:
                try:
                    super().keyPressEvent(event)
                except Exception:
                    pass
                return

            if key == Qt.Key.Key_K:
                try:
                    self.toggle_safety()
                except Exception:
                    pass
                return

            if key == Qt.Key.Key_T:
                try:
                    # toggle between MOSFET (0) and BB (1)
                    self.set_trigger_mode(0 if self.trigger_mode_bb else 1)
                except Exception:
                    pass
                return

            if key == Qt.Key.Key_R:
                try:
                    cur = bool(getattr(self, "rapid_fire_enabled", False))
                    if getattr(self, "rapid_fire_enable_checkbox", None) is not None:
                        self.rapid_fire_enable_checkbox.setChecked(not cur)
                    else:
                        if not cur:
                            self.start_rapid_fire()
                        else:
                            self.stop_rapid_fire()
                except Exception:
                    pass
                return

            if key == Qt.Key.Key_E:
                try:
                    self.export_rapid_fire_preset()
                except Exception:
                    pass
                return

            if key == Qt.Key.Key_L:
                try:
                    self.save_layout_profile()
                except Exception:
                    pass
                return

            # Additional manual shortcuts
            if key == Qt.Key.Key_M:
                try:
                    # Treat toggle actions as non-repeat only
                    if is_repeat:
                        try:
                            super().keyPressEvent(event)
                        except Exception:
                            pass
                        return
                    btn = getattr(self, "mosfet_hold_btn", None)
                    if btn is not None:
                        try:
                            btn.setChecked(not btn.isChecked())
                        except Exception:
                            try:
                                # fallback: call handler directly
                                self._on_mosfet_hold_toggled(not bool(getattr(self, "trigger_fired", False)))
                            except Exception:
                                pass
                    else:
                        try:
                            # toggle internal state directly
                            self._on_mosfet_hold_toggled(not bool(getattr(self, "trigger_fired", False)))
                        except Exception:
                            pass
                except Exception:
                    pass
                return

            if key == Qt.Key_1:
                try:
                    self.toggle_relay(1)
                except Exception:
                    pass
                return

            if key == Qt.Key_2:
                try:
                    self.toggle_relay(2)
                except Exception:
                    pass
                return

            if key == Qt.Key_BracketLeft:
                try:
                    cur = self._safe_int_widget_value("step_size_input", self.STEP_INCREMENT)
                    new = max(1, cur - 1)
                    self._safe_widget_call("step_size_input", "setValue", new)
                except Exception:
                    pass
                return

            if key == Qt.Key_BracketRight:
                try:
                    cur = self._safe_int_widget_value("step_size_input", self.STEP_INCREMENT)
                    new = min(99, cur + 1)
                    self._safe_widget_call("step_size_input", "setValue", new)
                except Exception:
                    pass
                return

            if key in (Qt.Key_Plus, Qt.Key_Equal):
                try:
                    cur = self._safe_int_widget_value("manual_speed_slider", 50)
                    new = min(100, cur + 5)
                    self._safe_widget_call("manual_speed_slider", "setValue", new)
                except Exception:
                    pass
                return

            if key in (Qt.Key_Minus, Qt.Key_Underscore):
                try:
                    cur = self._safe_int_widget_value("manual_speed_slider", 50)
                    new = max(1, cur - 5)
                    self._safe_widget_call("manual_speed_slider", "setValue", new)
                except Exception:
                    pass
                return

        except Exception:
            pass
        try:
            super().keyPressEvent(event)
        except Exception:
            pass

    def keyReleaseEvent(self, event):
        """Handle key release events for momentary actions (fire) and manual release semantics."""
        try:
            key = event.key()
            # If fire key released, clear fire
            if key == Qt.Key_Space:
                try:
                    self.set_fire_state(0)
                except Exception:
                    pass
                try:
                    if key in self._pressed_keys:
                        self._pressed_keys.discard(key)
                except Exception:
                    pass
                return

            # If movement key released, call manual_control_released to clear override
            if key in (Qt.Key_W, Qt.Key_S, Qt.Key_A, Qt.Key_D, Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right):
                try:
                    self.manual_control_released()
                except Exception:
                    pass
                try:
                    if key in self._pressed_keys:
                        self._pressed_keys.discard(key)
                except Exception:
                    pass
                return
        except Exception:
            pass
        try:
            super().keyReleaseEvent(event)
        except Exception:
            pass

    def create_behavior_tracking_panel(self):
        """Creates a standalone Behavior Presets dock (presets only)."""
        # All PyQt5 imports are available at module level

        # Ensure behavior_presets manager exists (stores user presets)
        try:
            if getattr(self, "behavior_presets", None) is None:
                try:
                    self.behavior_presets = BehaviorPresets()
                except Exception:
                    self.behavior_presets = None
        except Exception:
            self.behavior_presets = None

        # The presets group lives inside its own scroll area; parent it to
        # the main window to ensure a stable ownership chain.
        presets_group = QGroupBox("Behavior Presets", self)
        presets_layout = QVBoxLayout()
        presets_group.setLayout(presets_layout)

        try:
            presets_layout.addWidget(QLabel("Saved Presets:"))
        except Exception:
            pass

        # preset list
        if getattr(self, "preset_list", None) is None:
            try:
                self.preset_list = QListWidget()
            except Exception:
                # fallback
                self.preset_list = globals().get("QTextEdit", None) and globals()["QTextEdit"]()
                try:
                    self.preset_list.setReadOnly(True)
                except Exception:
                    pass
        try:
            presets_layout.addWidget(self.preset_list)
        except Exception:
            pass

        # name + buttons
        name_row = QHBoxLayout()
        if getattr(self, "preset_name_input", None) is None:
            try:
                self.preset_name_input = QLineEdit()
                self.preset_name_input.setPlaceholderText("New preset name")
            except Exception:
                self.preset_name_input = QLineEdit()
        name_row.addWidget(self.preset_name_input)

        if getattr(self, "save_preset_btn", None) is None:
            self.save_preset_btn = QPushButton("Save")
        if getattr(self, "apply_preset_btn", None) is None:
            self.apply_preset_btn = QPushButton("Apply")
        if getattr(self, "delete_preset_btn", None) is None:
            self.delete_preset_btn = QPushButton("Delete")

        name_row.addWidget(self.save_preset_btn)
        name_row.addWidget(self.apply_preset_btn)
        name_row.addWidget(self.delete_preset_btn)
        presets_layout.addLayout(name_row)

        # Scroll area for presets group
        scroll = QScrollArea()
        try:
            scroll.setWidgetResizable(True)
            scroll.setWidget(presets_group)
        except Exception:
            pass

        # Add presets dock
        try:
            self.add_dock("Behavior Presets", scroll, "right")
            try:
                if "Behavior Presets" not in getattr(self, "widget_items", []):
                    self.widget_items.append("Behavior Presets")
            except Exception:
                pass
        except Exception as e:
            print("Failed to add presets dock:", e)

        # Connect buttons
        try:
            self._safe_connect("save_preset_btn", "clicked", self.save_behavior_preset)
            self._safe_connect("apply_preset_btn", "clicked", self.load_behavior_preset)
            self._safe_connect("delete_preset_btn", "clicked", self.delete_behavior_preset)
        except Exception:
            try:
                self.save_preset_btn.clicked.connect(self.save_behavior_preset)
                self.apply_preset_btn.clicked.connect(self.load_behavior_preset)
                self.delete_preset_btn.clicked.connect(self.delete_behavior_preset)
            except Exception:
                pass

        # Double-click loads preset
        try:
            if hasattr(self.preset_list, "itemDoubleClicked"):
                self.preset_list.itemDoubleClicked.connect(
                    lambda it: self.load_behavior_preset(getattr(it, "text", lambda: str(it))())
                )
        except Exception:
            pass

        # Initial population
        try:
            self._refresh_preset_list()
        except Exception:
            pass

    def _safe_widget_call(self, attr_name: str, method_name: str, *args, **kwargs):
        """Call a widget method if present. Returns True if the call or set
        succeeded, False otherwise.
        """
        w = getattr(self, attr_name, None)
        if w is None:
            return False
        try:
            m = getattr(w, method_name, None)
            if callable(m):
                m(*args, **kwargs)
                return True
        except Exception:
            try:
                setattr(w, method_name, args[0] if args else None)
                return True
            except Exception:
                return False
        return False

    def _get_widget_value(self, attr_name: str, default=None):
        """Safely retrieve a widget's value() or text() if present, else return default."""
        # Prefer the centralized safe widget method caller which already
        # handles missing widgets and method-call exceptions.
        val = self._safe_widget_method_return(attr_name, "value", None)
        if val is not None:
            return val
        val = self._safe_widget_method_return(attr_name, "text", None)
        if val is not None:
            return val
        return default

    def _safe_widget_method_return(
        self, attr_name: str, method_name: str, default=None, *args, **kwargs
    ):
        """Call a widget method and return its value, or default if widget/method missing."""
        w = getattr(self, attr_name, None)
        if w is None:
            return default
        try:
            m = getattr(w, method_name, None)
            if callable(m):
                return m(*args, **kwargs)
        except Exception:
            pass
        return default

    def _safe_int_widget_value(self, attr_name: str, default=0):
        """Return an int value from widget.value() or default if unavailable."""
        val = self._safe_widget_method_return(attr_name, "value", default)
        # Narrow common types to keep static analyzer happier
        try:
            if isinstance(val, int):
                return val
            if isinstance(val, float):
                return int(val)
            if isinstance(val, str):
                try:
                    return int(val)
                except Exception:
                    try:
                        return int(float(val))
                    except Exception:
                        return int(default)
            # Fallback: convert via string to reduce unknown-type issues
            try:
                return int(str(val))
            except Exception:
                try:
                    return int(float(str(val)))
                except Exception:
                    return int(default)
        except Exception:
            return int(default)

    def _safe_float_widget_value(self, attr_name: str, default=0.0):
        """Return a float value from widget.value() or default if unavailable."""
        val = self._safe_widget_method_return(attr_name, "value", default)
        try:
            if isinstance(val, float):
                return val
            if isinstance(val, int):
                return float(val)
            if isinstance(val, str):
                try:
                    return float(val)
                except Exception:
                    return float(default)
            try:
                return float(str(val))
            except Exception:
                return float(default)
        except Exception:
            return float(default)

    def _safe_append_log(self, text: str):
        """Append text to serial_output widget if present, else no-op."""
        try:
            # First, prefer emitting the typed signal so worker threads can
            # safely request GUI updates without passing Qt C++ objects.
            if getattr(self, "serial_text_signal", None) is not None:
                try:
                    self.serial_text_signal.emit(str(text))
                    return True
                except Exception:
                    pass
            # If we're on the main thread, call the widget directly.
            try:
                import threading
                if threading.current_thread() is threading.main_thread():
                    if getattr(self, "serial_output", None) is not None:
                        try:
                            self._safe_widget_call("serial_output", "append", text)
                            return True
                        except Exception:
                            return False
            except Exception:
                pass
            # If not on main thread and signal failed, schedule a main-thread
            # callback that appends the plain string (safe to queue).
            try:
                from PyQt5.QtCore import QTimer
                QTimer.singleShot(0, lambda t=text: self._append_serial_text(t))
                return True
            except Exception:
                pass
        except Exception:
            pass
        try:
            # If UI isn't ready, also print to console so the developer can
            # see connect failures when running from a terminal.
            print(f"[UI LOG] {text}")
        except Exception:
            pass
        return False

    def _append_serial_text(self, text: str):
        """Slot: append plain text to the serial_output widget on GUI thread."""
        try:
            if getattr(self, "serial_output", None) is not None:
                try:
                    # Prefer the safe widget call helper (handles missing widget)
                    self._safe_widget_call("serial_output", "append", str(text))
                    return True
                except Exception:
                    try:
                        # Fallback: direct append
                        self.serial_output.append(str(text))
                        return True
                    except Exception:
                        pass
        except Exception:
            pass
        try:
            # Final fallback: print to console for diagnostics
            print(f"[UI LOG] {text}")
        except Exception:
            pass
        return False

    def _safe_connect(self, attr_name: str, signal_name: str, callback):
        """Safely connect a widget signal to a callback if the widget exists."""
        w = getattr(self, attr_name, None)
        if w is None:
            try:
                # Help debugging: log missing widget connect attempt
                cbname = getattr(callback, "__name__", repr(callback))
                self._safe_append_log(
                    f"CONNECT FAIL: widget '{attr_name}' missing for signal '{signal_name}' -> {cbname}"
                )
            except Exception:
                pass
            return False
        try:
            sig = getattr(w, signal_name, None)
            if sig is None:
                return False
            # Prefer using a callable 'connect' attribute if present
            try:
                conn = getattr(sig, "connect", None)
                if callable(conn):
                    conn(callback)
                    return True
            except Exception:
                pass
            # Fallback: if sig itself is callable and returns a signal-like object
            if callable(sig):
                try:
                    maybe_sig = sig()
                    conn2 = getattr(maybe_sig, "connect", None)
                    if callable(conn2):
                        conn2(callback)
                        return True
                except Exception:
                    pass
        except Exception:
            pass
        try:
            cbname = getattr(callback, "__name__", repr(callback))
            self._safe_append_log(
                f"CONNECT FAIL: '{attr_name}.{signal_name}' -> {cbname}"
            )
        except Exception:
            pass
        return False

    def _safe_connect_path(self, dotted_attr: str, signal_name: str, callback):
        """Safely follow a dotted attribute path from self and connect its signal.

        Example: _safe_connect_path('enhancer.arm_toggle_btn', 'toggled', cb)
        This will attempt: getattr(self, 'enhancer').arm_toggle_btn.toggled.connect(cb)
        Returns True if connected, False otherwise.
        """
        try:
            parts = (
                dotted_attr.split(".")
                if isinstance(dotted_attr, str)
                else [dotted_attr]
            )
            obj = self
            for p in parts:
                obj = getattr(obj, p, None)
                if obj is None:
                    try:
                        cbname = getattr(callback, "__name__", repr(callback))
                        self._safe_append_log(
                            f"CONNECT FAIL: path '{dotted_attr}' missing (failed at '{p}') for signal '{signal_name}' -> {cbname}"
                        )
                    except Exception:
                        pass
                    return False
            sig = getattr(obj, signal_name, None)
            if sig is None:
                return False
            try:
                conn = getattr(sig, "connect", None)
                if callable(conn):
                    conn(callback)
                    return True
            except Exception:
                pass
            # Sometimes the attribute is a function that returns a signal-like object
            if callable(sig):
                try:
                    maybe_sig = sig()
                    conn2 = getattr(maybe_sig, "connect", None)
                    if callable(conn2):
                        conn2(callback)
                        return True
                except Exception:
                    pass
        except Exception:
            pass
        try:
            cbname = getattr(callback, "__name__", repr(callback))
            self._safe_append_log(
                f"CONNECT FAIL: path '{dotted_attr}.{signal_name}' -> {cbname}"
            )
        except Exception:
            pass
        return False

    def _safe_enhancer_log(self, text: str, fire=False):
        """Safely call enhancer.log_serial_output() if enhancer is available, else use direct append."""
        try:
            if getattr(self, "enhancer", None) is not None:
                try:
                    self.enhancer.log_serial_output(text, fire=fire)
                except Exception:
                    # Fallback to direct serial output
                    self._safe_append_log(text)
            else:
                self._safe_append_log(text)
        except Exception:
            pass

    def _on_idle_behavior_changed(self, idx):
        """Handler for idle behavior combo changes.
        
        NOTE (DEC8-2025): This handler is no longer connected to any signal.
        Combo changes are now handled exclusively by the polling mechanism in update_frame().
        This avoids conflicts between signal-driven and polling-driven state changes.
        
        Keeping this method for potential future use or manual calls, but it's not wired to signals.
        """
        try:
            widget = getattr(self, "idle_behavior_combo", None)
            text = None
            # If index provided, try to use it first
            try:
                if isinstance(idx, int) and widget is not None:
                    try:
                        text = widget.itemText(idx)
                    except Exception:
                        text = None
            except Exception:
                pass
            # Fallback to currentText if available
            if text is None and widget is not None:
                try:
                    text = widget.currentText()
                except Exception:
                    try:
                        text = getattr(widget, "text", None)
                    except Exception:
                        text = None
            if text is None:
                text = getattr(self, "idle_behavior", "home")
            try:
                self.idle_behavior = str(text).strip().lower()
            except Exception:
                try:
                    self.idle_behavior = "home"
                except Exception:
                    pass
        except Exception:
            pass
        try:
            # Save settings (this might still be useful for manual calls)
            self.save_settings()
        except Exception:
            pass

    def _qt_enum(self, name: str, fallback: int):
        """Return a Qt enum value by name or a fallback integer.

        This helps static analyzers that can't resolve Qt attributes in files
        without importing PyQt5 at analysis time.
        """
        try:
            from PyQt5.QtCore import Qt

            return getattr(Qt, name, fallback)
        except Exception:
            return fallback

    def _qt_dock_area(self, name: str, fallback):
        """Return a DockWidgetArea enum value (typed) or fallback."""
        try:
            from PyQt5.QtCore import Qt as _Qt

            val = getattr(_Qt, name, fallback)
            return cast(Any, val)
        except Exception:
            return fallback

    def _qt_orientation(self, name: str, fallback):
        """Return an Orientation enum value or fallback (typed for analyzer)."""
        try:
            from PyQt5.QtCore import Qt as _Qt

            val = getattr(_Qt, name, fallback)
            return cast(Any, val)
        except Exception:
            return fallback

    def _debug_widget_signal_presence(self):
        """Debug helper: print which important widgets exist and whether
        they expose common signals (clicked, pressed, released, valueChanged).
        This logs to the serial pane or console for developer visibility.
        """
        try:
            widgets = [
                "tracking_btn",
                "aiming_btn",
                "go_home_button",
                "connect_button",
                "btn_up",
                "btn_down",
                "btn_left",
                "btn_right",
                "btn_center",
                "fire_button",
                "safety_button",
                "open_trainer_btn",
            ]
            for wname in widgets:
                obj = getattr(self, wname, None)
                if obj is None:
                    self._safe_append_log(f"WIDGET MISSING: {wname}")
                    continue
                # check common signals
                signals = [
                    "clicked",
                    "pressed",
                    "released",
                    "valueChanged",
                    "stateChanged",
                    "toggled",
                ]
                present = []
                for s in signals:
                    if hasattr(obj, s) or callable(getattr(obj, s, None)):
                        present.append(s)
                self._safe_append_log(
                    f"WIDGET: {wname} present; signals: {', '.join(present)}"
                )
        except Exception:
            pass

    def _safe_current_index(self, attr_name: str, default: int = 0):
        """Safely return currentIndex() of a combo if present, else default."""
        try:
            obj = getattr(self, attr_name, None)
            if obj is None:
                return default
            try:
                return int(obj.currentIndex())
            except Exception:
                try:
                    return int(obj.currentIndex())
                except Exception:
                    return default
        except Exception:
            return default

    def _cap_read(self):
        """Safely read from the video capture. Returns (ret, frame) or (False, None)."""
        cap = getattr(self, "cap", None)
        if cap is None:
            return False, None
        try:
            return cap.read()
        except Exception:
            return False, None

    def _cap_release(self):
        """Safely release video capture if present."""
        cap = getattr(self, "cap", None)
        if cap is None:
            return False
        try:
            if hasattr(cap, "release"):
                cap.release()
                return True
        except Exception:
            pass
        return False

    def _safe_open_serial(self, port, baud, **kwargs):
        """Open serial port safely with validation. Returns serial.Serial or None on failure."""
        try:
            p = str(port).strip() if port is not None else ""
            b = int(baud)
        except Exception:
            try:
                p = str(port).strip()
            except Exception:
                p = ""
            try:
                b = int(str(baud))
            except Exception:
                b = 115200
        
        # ========== SERIAL PORT PARAMETER VALIDATION ==========
        # Validate baud rate is within safe range
        valid_bauds = [300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 28800, 38400, 57600, 115200, 230400, 460800]
        if b not in valid_bauds:
            try:
                self._safe_enhancer_log(
                    f"[SERIAL] Warning: Baud rate {b} not in standard list. Using nearest valid rate (115200).",
                    fire=False
                )
            except Exception:
                pass
            b = 115200
        
        # Validate port is not empty
        if not p:
            try:
                self._safe_enhancer_log("[SERIAL] Error: No COM port specified.", fire=False)
            except Exception:
                pass
            return None

        # ========== BULLETPROOF FIX: Windows COM port timeout protection ==========
        # On Windows, opening a COM port can hang indefinitely if device not connected
        
        def _set_windows_com_timeout(port_name):
            """Set Windows COM port timeout at OS level before opening."""
            if os.name != "nt":
                return
            try:
                import ctypes
                kernel32 = ctypes.windll.kernel32
                # Attempt to open port to initialize it (sets timeouts)
                handle = kernel32.CreateFileW(port_name, 0xC0000000, 0, None, 3, 0x80, None)
                if handle and handle != -1:
                    kernel32.CloseHandle(handle)
            except Exception:
                pass  # Timeout setting is optional - don't block
        
        # Helper to attempt opening a port and log failures in the UI when possible
        def _try_open(port_name):
            try:
                # Pre-initialize Windows COM port to set timeouts
                _set_windows_com_timeout(port_name)
                # Now open with Python timeout settings
                ser = serial.Serial(port_name, b, **kwargs)
                try:
                    self._safe_append_log(f"Serial opened: {port_name} @ {b}")
                except Exception:
                    pass
                return ser
            except Exception as e:
                try:
                    self._safe_append_log(f"Serial open failed for {port_name}: {e}")
                except Exception:
                    pass
                return None

        # First, try the provided port string directly
        ser = _try_open(p)
        if ser is not None:
            return ser

        # On Windows some COM numbers >= 10 require the "\\\\.\\COM#" device path.
        # Try the Windows extended name as a fallback.
        try:
            if os.name == "nt" and isinstance(p, str) and p.upper().startswith("COM"):
                try:
                    num = int(p[3:])
                    if num >= 10:
                        alt = "\\\\.\\" + p
                        ser = _try_open(alt)
                        if ser is not None:
                            return ser
                except Exception:
                    # number parsing failed — ignore
                    pass
        except Exception:
            pass

        # No success
        return None

    def _ensure_frame(self, frame, default_shape=(480, 640, 3)):
        """Ensure returned object is an ndarray image. If frame is None or invalid,
        return a zero-filled ndarray of default_shape. This helps static analysis
        and prevents passing None into cv2 functions."""
        try:
            if frame is None:
                return np.zeros(default_shape, dtype=np.uint8)
            # If it's already an ndarray, cast and return
            if isinstance(frame, np.ndarray):
                return frame
            # Try to convert common buffer-like types
            try:
                arr = np.asarray(frame)
                if arr is None:
                    return np.zeros(default_shape, dtype=np.uint8)
                return arr
            except Exception:
                return np.zeros(default_shape, dtype=np.uint8)
        except Exception:
            return np.zeros(default_shape, dtype=np.uint8)

    def add_dock(self, title, widget, area=None):
        """Create or replace a dock widget for a given widget and add it to the main window.

        This helper ensures a single dock with the same title/objectName exists and
        configures allowed areas and basic features. It accepts QWidget subclasses
        (including QScrollArea) as `widget`.
        """
        try:
            # Ensure dock options allow nesting/tabbing
            try:
                self.setDockOptions(
                    QMainWindow.AllowNestedDocks
                    | QMainWindow.AllowTabbedDocks
                    | QMainWindow.AnimatedDocks
                )
            except Exception:
                pass

            # Build a safe object name and remove any existing dock with same title to avoid duplicates
            obj_name = f"Dock_{title.replace(' ', '_')}"
            # avoid Qt enum default in signature to satisfy static analyzer
            try:
                if area is None:
                    area = getattr(Qt, "LeftDockWidgetArea", None)
            except Exception:
                area = None
            try:
                for d in list(self.findChildren(QDockWidget)):
                    try:
                        if (d.objectName() == obj_name) or (d.windowTitle() == title):
                            try:
                                self.removeDockWidget(d)
                            except Exception:
                                pass
                            try:
                                d.deleteLater()
                            except Exception:
                                pass
                    except Exception:
                        pass
            except Exception:
                pass

            dock = QDockWidget(title, self)
            dock.setObjectName(obj_name)
            try:
                try:
                    left_area = getattr(Qt, "LeftDockWidgetArea", None)
                    right_area = getattr(Qt, "RightDockWidgetArea", None)
                    allowed = None
                    if left_area is not None and right_area is not None:
                        allowed = left_area | right_area
                    elif left_area is not None:
                        allowed = left_area
                    elif right_area is not None:
                        allowed = right_area
                    if allowed is not None:
                        dock.setAllowedAreas(allowed)
                except Exception:
                    pass
            except Exception:
                pass
            try:
                dock.setFeatures(
                    QDockWidget.DockWidgetMovable
                    | QDockWidget.DockWidgetFloatable
                    | QDockWidget.DockWidgetClosable
                )
            except Exception:
                pass

            # If the provided widget is already a QDockWidget, just reparent; else set as content
            try:
                dock.setWidget(widget)
            except Exception:
                try:
                    # last resort: wrap in a simple container
                    container = QWidget()
                    layout = QVBoxLayout(container)
                    layout.setContentsMargins(0, 0, 0, 0)
                    layout.addWidget(widget)
                    dock.setWidget(container)
                except Exception:
                    pass

                try:
                    # Resolve area which may be None, a Qt constant, or a string like 'left'/'right'
                    try:
                        resolved_area = None
                        if area is None:
                            resolved_area = self._qt_dock_area("LeftDockWidgetArea", 1)
                        else:
                            # Map common string keywords to Qt dock areas
                            try:
                                if isinstance(area, str):
                                    a = area.lower()
                                    if a.startswith("left"):
                                        resolved_area = self._qt_dock_area(
                                            "LeftDockWidgetArea", 1
                                        )
                                    elif a.startswith("right"):
                                        resolved_area = self._qt_dock_area(
                                            "RightDockWidgetArea", 2
                                        )
                                    elif a.startswith("bottom") or a.startswith("down"):
                                        resolved_area = self._qt_dock_area(
                                            "BottomDockWidgetArea", 4
                                        )
                                    else:
                                        # unknown string: fallback to left
                                        resolved_area = self._qt_dock_area(
                                            "LeftDockWidgetArea", 1
                                        )
                                else:
                                    # assume it's already a Qt enum/int; cast for analyzer
                                    resolved_area = cast(Any, area)
                            except Exception:
                                resolved_area = self._qt_dock_area(
                                    "LeftDockWidgetArea", 1
                                )

                        # Finally add the dock using the resolved area (typed via _qt_dock_area)
                        try:
                            self.addDockWidget(resolved_area, dock)
                        except Exception:
                            # Last resort: try explicit LeftDockWidgetArea int
                            try:
                                self.addDockWidget(
                                    self._qt_dock_area("LeftDockWidgetArea", 1), dock
                                )
                            except Exception:
                                pass
                    except Exception:
                        try:
                            self.addDockWidget(
                                self._qt_dock_area("LeftDockWidgetArea", 1), dock
                            )
                        except Exception:
                            pass
                except Exception:
                    pass
            return dock
        except Exception:
            return None

    def equalize_dock_columns(self):
        """Ensure left/right dock columns use the same width and apply a consistent groupbox style.

        This is called after docks are created and again after restoring window state so
        Qt's restoreState doesn't re-introduce mismatched widths.
        """
        try:
            # Respect user preference: allow disabling automatic equalization.
            try:
                if not getattr(self, "auto_equalize_dock_columns", True):
                    return
            except Exception:
                pass
            # Only consider dock widgets docked in the main window (skip floating)
            docks = [d for d in self.findChildren(QDockWidget) if not d.isFloating()]
            try:
                left_const = getattr(Qt, "LeftDockWidgetArea", None)
            except Exception:
                left_const = None
            try:
                right_const = getattr(Qt, "RightDockWidgetArea", None)
            except Exception:
                right_const = None
            left_docks = [
                d
                for d in docks
                if (left_const is not None and self.dockWidgetArea(d) == left_const)
            ]
            right_docks = [
                d
                for d in docks
                if (right_const is not None and self.dockWidgetArea(d) == right_const)
            ]
            all_docks = left_docks + right_docks
            if not all_docks:
                return

            # Compute candidate widths from various hints (widget, dock size, sizeHint)
            widths = []
            for d in all_docks:
                try:
                    cand = None
                    w = d.widget()
                    if w is not None:
                        try:
                            cand = int(w.width() or w.sizeHint().width())
                        except Exception:
                            try:
                                cand = int(w.sizeHint().width())
                            except Exception:
                                cand = None
                    if not cand:
                        try:
                            cand = int(d.width() or d.sizeHint().width())
                        except Exception:
                            cand = None
                    widths.append(int(cand or 340))
                except Exception:
                    widths.append(340)

            # Compute available width and reserve a reasonable central area so docks
            # cannot force the central widget to collapse. Use DEFAULT_DOCK_COLUMN_WIDTH
            # as a conservative preferred width to match the UI sketch provided.
            total_w = self.width() if hasattr(self, "width") else 1200
            central_min = max(300, int(total_w * 0.45))
            # Per-column cap is remaining width split across left/right docks
            per_column_cap = max(200, int(max(200, (total_w - central_min) / 2)))
            # Pick candidate from content hints
            candidate = max(widths)
            if candidate < 200:
                candidate = 200
            # Target width should prefer DEFAULT_DOCK_COLUMN_WIDTH but never exceed
            # the per-column cap (available space). This keeps both columns near the
            # user's requested visual guide while remaining responsive.
            try:
                pref = int(getattr(self, "DEFAULT_DOCK_COLUMN_WIDTH", 320))
            except Exception:
                pref = 320
            target_width = min(pref, per_column_cap, candidate)

            # Ensure central widget has a minimum width before we force dock widths
            try:
                cw = self.centralWidget()
                if cw is not None:
                    try:
                        cw.setMinimumWidth(central_min)
                    except Exception:
                        pass
            except Exception:
                pass

            # Apply fixed horizontal sizing for dock columns (Preferred: Fixed width)
            for d in all_docks:
                try:
                    # If operator requested strict equality, force exact widths.
                    # Use setFixedWidth for stronger enforcement and also set
                    # the widget's size policy to Fixed. This is intrusive
                    # but guarantees visual equality where possible.
                    if getattr(self, "force_exact_dock_widths", False):
                        try:
                            d.setFixedWidth(int(target_width))
                        except Exception:
                            try:
                                d.setMinimumWidth(int(target_width))
                            except Exception:
                                pass
                        try:
                            w = d.widget()
                            if w is not None:
                                try:
                                    w.setFixedWidth(int(target_width))
                                except Exception:
                                    try:
                                        w.setMinimumWidth(int(target_width))
                                    except Exception:
                                        pass
                                try:
                                    w.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                                except Exception:
                                    pass
                        except Exception:
                            pass
                    else:
                        # Only set a minimum width and prefer flexible policy so docks can be nested/tabbed.
                        d.setMinimumWidth(int(target_width))
                        try:
                            d.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                        except Exception:
                            pass
                except Exception:
                    # Fallback: try setting inner widget
                    try:
                        w = d.widget()
                        if w is not None:
                            w.setMinimumWidth(int(target_width))
                            try:
                                w.setSizePolicy(
                                    QSizePolicy.Preferred, QSizePolicy.Preferred
                                )
                            except Exception:
                                pass
                    except Exception:
                        pass

            # Also request Qt to resize docks to the target width (helps when layout/restore overrides direct width hints)
            try:
                if left_docks:
                    try:
                        orient = getattr(Qt, "Vertical", None)
                        if orient is None:
                            orient = self._qt_enum("Vertical", 2)
                        try:
                            self.resizeDocks(
                                left_docks,
                                [target_width] * len(left_docks),
                                cast(Any, orient),
                            )
                        except Exception:
                            try:
                                # Fallback to explicit orient resolved helper
                                fallback_orient = self._qt_orientation("Vertical", 2)
                                self.resizeDocks(
                                    left_docks,
                                    [target_width] * len(left_docks),
                                    cast(Any, fallback_orient),
                                )
                            except Exception:
                                pass
                    except Exception:
                        pass
                if right_docks:
                    try:
                        orient = getattr(Qt, "Vertical", None)
                        if orient is None:
                            orient = self._qt_enum("Vertical", 2)
                        try:
                            self.resizeDocks(
                                right_docks,
                                [target_width] * len(right_docks),
                                cast(Any, orient),
                            )
                        except Exception:
                            try:
                                fallback_orient = self._qt_orientation("Vertical", 2)
                                self.resizeDocks(
                                    right_docks,
                                    [target_width] * len(right_docks),
                                    cast(Any, fallback_orient),
                                )
                            except Exception:
                                pass
                    except Exception:
                        pass
            except Exception:
                pass

            # Apply consistent background to groupboxes and scroll viewports inside docks
            consistent_bg = """
                QGroupBox { background-color: #151515; border: 1px solid #888; border-radius: 10px; margin-top: 10px; font-weight: bold; color: #eaeaea; padding: 8px; }
                QScrollArea QWidget { background-color: #151515; }
            """
            for g in self.findChildren(QGroupBox):
                try:
                    g.setStyleSheet(consistent_bg)
                except Exception:
                    pass

            # Also ensure QDockWidget contents have matching background and style scroll viewports
            try:
                from PyQt5.QtWidgets import QScrollArea

                def apply_style_recursive(widget):
                    # Avoid modifying the central video widgets
                    try:
                        if widget in (
                            getattr(self, "video_frame", None),
                            getattr(self, "video_label", None),
                            getattr(self, "sniper_view_label", None),
                        ):
                            return
                    except Exception:
                        pass
                    try:
                        if widget is not None:
                            try:
                                widget.setStyleSheet(consistent_bg)
                            except Exception:
                                pass
                            # Recurse into children
                            try:
                                for c in widget.findChildren(QWidget):
                                    try:
                                        c.setStyleSheet(consistent_bg)
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                    except Exception:
                        pass

                for d in all_docks:
                    try:
                        d.setStyleSheet("QDockWidget { background-color: #151515; }")
                        w = d.widget()
                        if w is not None:
                            try:
                                apply_style_recursive(w)
                            except Exception:
                                pass
                            # If it's a scroll area, also style its viewport
                            try:
                                if isinstance(w, QScrollArea):
                                    try:
                                        w.viewport().setStyleSheet(
                                            "background-color: #151515;"
                                        )
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                    except Exception:
                        pass
            except Exception:
                pass

            # Report final dock widths to serial console (but skip terminal prints)
            try:
                if hasattr(self, "enhancer"):
                    # Measure actual widths after the resize attempt so the log
                    # reflects what the UI ended up with (helps debugging).
                    try:
                        applied_left = [str(int(d.width())) for d in left_docks] if left_docks else []
                    except Exception:
                        applied_left = []
                    try:
                        applied_right = [str(int(d.width())) for d in right_docks] if right_docks else []
                    except Exception:
                        applied_right = []
                    applied_summary = ""
                    try:
                        if applied_left or applied_right:
                            applied_summary = (
                                " (applied widths -> L: "
                                + (",".join(applied_left) if applied_left else "-")
                                + " R: "
                                + (",".join(applied_right) if applied_right else "-")
                                + ")"
                            )
                    except Exception:
                        applied_summary = ""

                    self.enhancer.log_serial_output(
                        f"Dock widths equalized to {target_width}px.{applied_summary}",
                        fire=False,
                    )
                    # If applied widths don't match the target, emit per-dock diagnostics
                    try:
                        all_vals = []
                        for s in (applied_left + applied_right):
                            try:
                                all_vals.append(int(s))
                            except Exception:
                                pass
                        mismatch = False
                        if all_vals:
                            try:
                                mismatch = any(int(v) != int(target_width) for v in all_vals)
                            except Exception:
                                mismatch = True
                        if mismatch:
                            try:
                                self.enhancer.log_serial_output(
                                    "[DIAG] Dock equalize mismatch detected - emitting per-dock details:",
                                    fire=False,
                                )
                            except Exception:
                                pass
                            # Left docks diagnostics
                            try:
                                for d in left_docks:
                                    try:
                                        w = d.widget()
                                        try:
                                            hint = w.sizeHint().width() if w is not None else None
                                        except Exception:
                                            hint = None
                                        try:
                                            self.enhancer.log_serial_output(
                                                f"[DIAG] LEFT '{d.windowTitle()}': floating={d.isFloating()} width={int(d.width())} min={d.minimumWidth()} max={d.maximumWidth()} hint={hint}",
                                                fire=False,
                                            )
                                        except Exception:
                                            pass
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                            # Right docks diagnostics
                            try:
                                for d in right_docks:
                                    try:
                                        w = d.widget()
                                        try:
                                            hint = w.sizeHint().width() if w is not None else None
                                        except Exception:
                                            hint = None
                                        try:
                                            self.enhancer.log_serial_output(
                                                f"[DIAG] RIGHT '{d.windowTitle()}': floating={d.isFloating()} width={int(d.width())} min={d.minimumWidth()} max={d.maximumWidth()} hint={hint}",
                                                fire=False,
                                            )
                                        except Exception:
                                            pass
                                    except Exception:
                                        pass
                            except Exception:
                                pass
                            # Central and layout hints
                            try:
                                cw = self.centralWidget()
                                try:
                                    ct_hint = cw.sizeHint().width() if cw is not None else None
                                except Exception:
                                    ct_hint = None
                                try:
                                    self.enhancer.log_serial_output(
                                        f"[DIAG] layout: total_w={total_w} central_min={central_min} per_column_cap={per_column_cap} candidate={candidate} pref={pref} target={target_width} central_hint={ct_hint}",
                                        fire=False,
                                    )
                                except Exception:
                                    pass
                            except Exception:
                                pass
                    except Exception:
                        pass
            except Exception:
                pass
        except Exception as e:
            print(f"[WARN] equalize_dock_columns failed: {e}")

    def enforce_default_dock_layout(self):
        """Arrange docks into two stacked columns (left/right) in a stable default layout.

        This function is idempotent and safe to call multiple times. It attempts to
        place a reasonable set of docks into the left column and the remaining
        docks into the right column, stacked in the order they were added.
        """
        try:
            # Gather non-floating docks in deterministic order
            docks = [d for d in self.findChildren(QDockWidget) if not d.isFloating()]
            if not docks:
                return

            # Simple split heuristic: left column gets first N docks, right gets remainder
            # Aim for roughly equal numbers per column and prefer key groups on left
            # Prefer these core left-side groups when present
            preferred_left = [
                "Configuration & Connection",
                "Home Position",
                "Servo Limits",
                "Accessories",
            ]

            left_list = []
            right_list = []

            # First, place any preferred-left docks on the left in their existing order
            for d in docks:
                try:
                    if d.windowTitle() in preferred_left:
                        left_list.append(d)
                except Exception:
                    pass

            # Fill remaining docks by alternating into right/left to balance columns
            for d in docks:
                try:
                    if d in left_list:
                        continue
                    if len(left_list) <= len(right_list):
                        left_list.append(d)
                    else:
                        right_list.append(d)
                except Exception:
                    pass

            # Resolve Qt dock area enums
            try:
                left_area = getattr(
                    Qt, "LeftDockWidgetArea", None
                ) or self._qt_dock_area("LeftDockWidgetArea", 1)
                right_area = getattr(
                    Qt, "RightDockWidgetArea", None
                ) or self._qt_dock_area("RightDockWidgetArea", 2)
            except Exception:
                left_area = self._qt_dock_area("LeftDockWidgetArea", 1)
                right_area = self._qt_dock_area("RightDockWidgetArea", 2)

            # Add docks to main window in the requested columns
            for d in left_list:
                try:
                    # Ensure dock is not floating and is visible before attempting to add
                    try:
                        d.setFloating(False)
                    except Exception:
                        pass
                    try:
                        d.setVisible(True)
                    except Exception:
                        pass
                    try:
                        d.setFeatures(
                            QDockWidget.DockWidgetMovable
                            | QDockWidget.DockWidgetFloatable
                            | QDockWidget.DockWidgetClosable
                        )
                    except Exception:
                        pass
                    if self.dockWidgetArea(d) != left_area:
                        try:
                            self.addDockWidget(left_area, d)
                        except Exception:
                            try:
                                self.addDockWidget(
                                    self._qt_dock_area("LeftDockWidgetArea", 1), d
                                )
                            except Exception:
                                pass
                except Exception:
                    pass

            for d in right_list:
                try:
                    try:
                        d.setFloating(False)
                    except Exception:
                        pass
                    try:
                        d.setVisible(True)
                    except Exception:
                        pass
                    try:
                        d.setFeatures(
                            QDockWidget.DockWidgetMovable
                            | QDockWidget.DockWidgetFloatable
                            | QDockWidget.DockWidgetClosable
                        )
                    except Exception:
                        pass
                    if self.dockWidgetArea(d) != right_area:
                        try:
                            self.addDockWidget(right_area, d)
                        except Exception:
                            try:
                                self.addDockWidget(
                                    self._qt_dock_area("RightDockWidgetArea", 2), d
                                )
                            except Exception:
                                pass
                except Exception:
                    pass

            # Finally equalize widths after ordering
            try:
                QTimer.singleShot(150, lambda: self.equalize_dock_columns())
            except Exception:
                pass
        except Exception:
            pass

    def set_sound_enabled(self, state):
        """Handler for sound checkbox changes. Accepts Qt state int or bool."""
        try:
            enabled = (
                (state == Qt.CheckState.Checked)
                if isinstance(state, int)
                else bool(state)
            )
        except Exception:
            enabled = bool(state)
        self.sound_enabled = bool(enabled)
        # Save immediately so preference persists across sessions
        try:
            self.save_settings()
        except Exception:
            pass
        try:
            if hasattr(self, "enhancer"):
                self.enhancer.log_serial_output(
                    f"Sound effects {'ENABLED' if self.sound_enabled else 'DISABLED'}",
                    fire=False,
                )
        except Exception:
            pass

    def toggle_tracking_panel(self, checked):
        """Legacy method, no longer needed with dock widgets."""
        pass

    def set_flip_pan(self, val: bool):
        self.flip_pan_direction = bool(val)
        self.enhancer.log_serial_output(
            f"Invert PAN set to: {self.flip_pan_direction}", fire=False
        )
        self.save_settings()  # V4 Save

    def set_flip_tilt(self, val: bool):
        self.flip_tilt_direction = bool(val)
        self.enhancer.log_serial_output(
            f"Invert TILT set to: {self.flip_tilt_direction}", fire=False
        )
        self.save_settings()

    def on_detection_mode_change(self, idx=None):
        # robust handler: accept index change signal or manual call
        try:
            mode_text = self.detection_mode_combo.currentText().lower()
            is_yolo = "yolo" in mode_text or "object detection" in mode_text
            is_hybrid = "hybrid" in mode_text
            self.enhancer.update_mode(self.detection_mode_combo.currentText())

            # Show/hide YOLO floating panel based on detection mode
            if is_yolo and not is_hybrid:
                # Show YOLO settings only for pure YOLO mode (mode 2)
                self._show_yolo_floating_panel()
            else:
                # Hide YOLO floating panel for other modes
                self._hide_yolo_floating_panel()

            # Manage visibility of hybrid settings panel
            try:
                if hasattr(self, "hybrid_settings_group"):
                    if is_hybrid:
                        self.hybrid_settings_group.show()
                    else:
                        self.hybrid_settings_group.hide()
            except Exception:
                pass

            # ensure the yolo group exists
            if hasattr(self, "yolo_settings_group"):
                if is_yolo and not is_hybrid:
                    # populate models each time to refresh list (prevents empty combo causing strange collapse)
                    try:
                        models = self.yolo_detector.find_models() or []
                        # Keep current selection if possible (support external paths)
                        try:
                            cur = (
                                self.yolo_model_combo.currentText()
                                if self.yolo_model_combo.count() > 0
                                else ""
                            )
                        except Exception:
                            cur = ""
                        self.yolo_model_combo.blockSignals(True)
                        self.yolo_model_combo.clear()
                        self.yolo_model_combo.addItems(models)
                        # If the previous selection was an external path, re-add it so it remains selectable
                        try:
                            if cur and cur not in models:
                                self.yolo_model_combo.addItem(cur)
                        except Exception:
                            pass
                        # restore selection
                        try:
                            self.yolo_model_combo.setCurrentText(cur)
                        except Exception:
                            pass
                    except Exception as e:
                        # log into serial console
                        if hasattr(self, "enhancer"):
                            self.enhancer.log_serial_output(
                                f"YOLO model refresh failed: {e}"
                            )
                        else:
                            print("YOLO model refresh failed:", e)
                    finally:
                        try:
                            self.yolo_model_combo.blockSignals(False)
                        except Exception:
                            pass
                # If user switched detection modes explicitly, clear any lingering
                # manual override so the newly selected detection mode takes effect
                # immediately rather than being blocked by a stale manual override.
                if getattr(self, "manual_override", False) or (
                    getattr(self, "_manual_override_until", 0) > time.time()
                ):
                    try:
                        self.manual_override = False
                        self._manual_override_until = 0.0
                        if getattr(self, "tracking_was_active", False):
                            self.tracking_active = True
                            self.tracking_was_active = False
                        try:
                            if hasattr(self, "enhancer"):
                                self.enhancer.log_serial_output(
                                    "Manual override cleared due to detection mode change",
                                    fire=False,
                                )
                        except Exception:
                            pass
                    except Exception:
                        pass
        except Exception as e:
            # fallback: log error
            if hasattr(self, "enhancer"):
                self.enhancer.log_serial_output(f"on_detection_mode_change error: {e}")
            else:
                print("on_detection_mode_change error:", e)

    def on_yolo_model_changed(self, idx):
        model_name = self.yolo_model_combo.currentText()
        if model_name:
            try:
                self.yolo_detector.load_model(model_name)
                if hasattr(self, "enhancer"):
                    self.enhancer.log_serial_output(f"Loaded YOLO model: {model_name}")
                try:
                    if getattr(self, "state_logger", None):
                        self.state_logger.log(f">>> YOLO model loaded: {model_name}")
                except Exception:
                    pass
                
                # CRITICAL FIX: Set target classes immediately after loading model
                # This ensures custom models (Rat, Cat, Dog) work with their classes
                try:
                    classes = (
                        self._safe_widget_method_return(
                            "yolo_classes_input", "text", "person"
                        )
                        or "person"
                    )
                    self.yolo_detector.set_target_classes(classes)
                    if hasattr(self, "enhancer"):
                        self.enhancer.log_serial_output(f"YOLO target classes: {classes}")
                except Exception:
                    pass
            except Exception as e:
                if hasattr(self, "enhancer"):
                    self.enhancer.log_serial_output(
                        f"Failed to load YOLO model {model_name}: {e}"
                    )

    def browse_yolo_model(self):
        """Open a file dialog to pick a YOLO model file (allows browsing outside models dir)."""
        try:
            start_dir = (
                getattr(self.yolo_detector, "models_dir", "YOLO_MODELS")
                or "YOLO_MODELS"
            )
            path, _ = QFileDialog.getOpenFileName(
                self,
                "Select YOLO model",
                start_dir,
                "YOLO Model Files (*.pt);;All Files (*)",
            )
            if not path:
                return
            # Add the selected path to the combo if it's not already present so existing
            # code that reads the combo's currentText continues to work.
            try:
                idx = self.yolo_model_combo.findText(path)
                if idx == -1:
                    self.yolo_model_combo.addItem(path)
                    idx = self.yolo_model_combo.findText(path)
                if idx != -1:
                    self.yolo_model_combo.setCurrentIndex(idx)
            except Exception:
                try:
                    # fallback: set text via safe method
                    self._safe_widget_call("yolo_model_combo", "setCurrentText", path)
                except Exception:
                    pass
            # Attempt to load the model immediately and persist selection
            try:
                self.yolo_detector.load_model(path)
                try:
                    if hasattr(self, "enhancer"):
                        self.enhancer.log_serial_output(f"Loaded YOLO model: {path}")
                except Exception:
                    pass
                try:
                    self.save_settings()
                except Exception:
                    pass
            except Exception as e:
                try:
                    if hasattr(self, "enhancer"):
                        self.enhancer.log_serial_output(
                            f"Failed to load YOLO model {path}: {e}"
                        )
                except Exception:
                    pass
        except Exception:
            pass

    def _show_yolo_floating_panel(self):
        """Show YOLO settings as a floating panel window."""
        try:
            # Create floating panel if it doesn't exist
            if self._yolo_floating_panel is None:
                from PyQt5.QtWidgets import QMainWindow
                from PyQt5.QtCore import Qt
                
                # Create a new QMainWindow for the floating panel
                self._yolo_floating_panel = QMainWindow()
                self._yolo_floating_panel.setWindowTitle("YOLO Settings")
                self._yolo_floating_panel.setCentralWidget(self.yolo_settings_group)
                self._yolo_floating_panel.setWindowFlags(
                    Qt.Window | Qt.WindowStaysOnTopHint
                )
                
                # Optimized minimum size: 380x280px contains all controls comfortably
                # - Width: 380px = labels (80px) + spacing (6px) + controls (170px) + margins (16px + 8px)
                # - Height: 280px = title bar (25px) + 4 rows (60px ea) + spacing (20px) + margins (16px)
                self._yolo_floating_panel.resize(380, 280)
                self._yolo_floating_panel.setMinimumSize(380, 280)
                
                # Position near top-right of main window
                try:
                    main_geo = self.geometry()
                    self._yolo_floating_panel.move(
                        main_geo.right() - 420,
                        main_geo.top() + 100
                    )
                except Exception:
                    pass
            
            # Show the floating panel
            self._yolo_floating_panel.show()
            self._yolo_floating_panel.raise_()
            self._yolo_floating_panel.activateWindow()
        except Exception as e:
            try:
                if hasattr(self, "enhancer"):
                    self.enhancer.log_serial_output(
                        f"Failed to show YOLO panel: {e}",
                        fire=False
                    )
            except Exception:
                print(f"Failed to show YOLO panel: {e}")

    def _hide_yolo_floating_panel(self):
        """Hide YOLO settings floating panel."""
        try:
            if self._yolo_floating_panel is not None:
                self._yolo_floating_panel.hide()
        except Exception:
            pass

    def open_yolo_trainer(self):
        try:
            # lazy import to avoid heavy import during startup; use importlib so
            # missing optional trainer module doesn't raise a static-import error
            try:
                module = importlib.import_module("yolo_trainer_window")
                YoloTrainerWindow = getattr(module, "YoloTrainerWindow", None)
                if YoloTrainerWindow is None:
                    raise ImportError("YoloTrainerWindow not found in module")
            except Exception:
                try:
                    if hasattr(self, "enhancer"):
                        self.enhancer.log_serial_output(
                            "YOLO trainer module not available.",
                            fire=False,
                        )
                except Exception:
                    pass
                return

            model_text = (
                self.yolo_model_combo.currentText()
                if getattr(self, "yolo_model_combo", None)
                and self.yolo_model_combo.count() > 0
                else "yolov8n.pt"
            )
            self.trainer_window = YoloTrainerWindow(model_path=model_text)
            self.trainer_window.show()
            # bring to front if possible
            try:
                self.trainer_window.raise_()
            except Exception:
                pass

            # If the trainer window exposes a finished signal or a callback attribute,
            # connect it so we can prompt the user to apply the trained weights when done.
            try:
                connected = False
                # Prefer safe path connection first
                try:
                    if self._safe_connect_path(
                        "trainer_window", "training_finished", self._on_trainer_finished
                    ):
                        connected = True
                except Exception:
                    pass

                # If safe path didn't connect, try direct attribute signal.connect guard
                if not connected:
                    try:
                        tw = getattr(self, "trainer_window", None)
                        if tw is not None:
                            sig = getattr(tw, "training_finished", None)
                            if sig is not None:
                                c = getattr(sig, "connect", None)
                                if callable(c):
                                    c(self._on_trainer_finished)
                                    connected = True
                    except Exception:
                        pass

                # Try alternate signal name
                if not connected:
                    try:
                        if self._safe_connect_path(
                            "trainer_window",
                            "training_finished_signal",
                            self._on_trainer_finished,
                        ):
                            connected = True
                    except Exception:
                        pass
                if not connected:
                    try:
                        tw = getattr(self, "trainer_window", None)
                        if tw is not None:
                            sig2 = getattr(tw, "training_finished_signal", None)
                            if sig2 is not None:
                                c2 = getattr(sig2, "connect", None)
                                if callable(c2):
                                    c2(self._on_trainer_finished)
                                    connected = True
                    except Exception:
                        pass

                # Final fallback: set a callable attribute the trainer may call directly
                if not connected:
                    try:
                        setattr(
                            self.trainer_window,
                            "on_training_finished",
                            self._on_trainer_finished,
                        )
                        # Also set a callback to be notified when classes.txt changes so the main UI
                        # can refresh the class picker contents immediately after adding/removing classes
                        try:
                            setattr(
                                self.trainer_window,
                                "on_classes_changed",
                                self._on_trainer_classes_changed,
                            )
                        except Exception:
                            pass
                    except Exception:
                        pass
                # Always set the classes-changed callback when possible so the main UI
                # can react to class edits regardless of how we connected training signals.
                try:
                    try:
                        setattr(
                            self.trainer_window,
                            "on_classes_changed",
                            self._on_trainer_classes_changed,
                        )
                    except Exception:
                        pass
                except Exception:
                    pass
            except Exception:
                pass
        except Exception as e:
            try:
                self.enhancer.log_serial_output(f"Failed to open trainer window: {e}")
            except Exception:
                print("Failed to open trainer window:", e)

    def _on_trainer_classes_changed(self, classes_file_path=None):
        """Callback from trainer window when dataset/classes.txt is updated.

        We cache the classes so the class picker dialog shows the current list
        immediately after the trainer writes the file.
        """
        try:
            classes = []
            if classes_file_path and os.path.exists(classes_file_path):
                try:
                    with open(classes_file_path, "r", encoding="utf-8") as f:
                        classes = [ln.strip() for ln in f if ln.strip()]
                except Exception:
                    classes = []
            # fallback: try canonical dataset/classes.txt
            if not classes:
                cf = os.path.join(os.getcwd(), "dataset", "classes.txt")
                try:
                    if os.path.exists(cf):
                        with open(cf, "r", encoding="utf-8") as f:
                            classes = [ln.strip() for ln in f if ln.strip()]
                except Exception:
                    classes = []
            # store cached list for dialog use
            try:
                self._cached_yolo_classes = classes
            except Exception:
                pass
            try:
                if hasattr(self, "enhancer"):
                    self.enhancer.log_serial_output(
                        f"YOLO classes updated ({len(classes)})", fire=False
                    )
            except Exception:
                pass
        except Exception:
            try:
                if hasattr(self, "enhancer"):
                    self.enhancer.log_serial_output(
                        "Error while refreshing YOLO classes", fire=False
                    )
            except Exception:
                pass

    def open_yolo_class_picker(self):
        """Open a small dialog to pick one or more target classes.

        The source of truth is `dataset/classes.txt`. If the trainer updated
        classes.txt it will call back into `_on_trainer_classes_changed` which
        populates an in-memory cache used here for immediate refresh. If the
        cache is empty we read the file on demand and finally fall back to the
        embedded COCO defaults.
        """
        try:
            from PyQt5.QtWidgets import (
                QDialog,
                QDialogButtonBox,
                QListWidget,
                QListWidgetItem,
                QVBoxLayout,
            )
        except Exception as e:
            msg = f"PyQt5 import failed: {e}"
            try:
                if hasattr(self, "enhancer"):
                    self.enhancer.log_serial_output(msg)
            except Exception:
                pass
            return

        # prepare class list: prefer cached classes written by trainer, else read file
        classes = getattr(self, "_cached_yolo_classes", None) or []
        if not classes:
            classes_file = os.path.join(os.getcwd(), "dataset", "classes.txt")
            try:
                if os.path.exists(classes_file):
                    with open(classes_file, "r", encoding="utf-8") as f:
                        classes = [ln.strip() for ln in f if ln.strip()]
            except Exception:
                classes = []
        if not classes:
            try:
                classes = list(YOLO_COCO_CLASSES)
            except Exception:
                classes = []

        dlg = QDialog(self)
        dlg.setWindowTitle("Pick YOLO target classes")
        layout = QVBoxLayout(dlg)
        lw = QListWidget()
        lw.setSelectionMode(lw.MultiSelection)
        for c in classes:
            it = QListWidgetItem(c)
            lw.addItem(it)

        # pre-select any currently-set classes
        try:
            cur = ""
            if getattr(self, "yolo_classes_input", None) is not None:
                cur = self.yolo_classes_input.text() or ""
            cur_set = set([s.strip() for s in cur.split(",") if s.strip()])
            for i in range(lw.count()):
                itm = lw.item(i)
                if itm and hasattr(itm, "text") and itm.text() in cur_set:
                    if hasattr(itm, "setSelected"):
                        itm.setSelected(True)
        except Exception:
            pass

        layout.addWidget(lw)
        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btns.accepted.connect(dlg.accept)
        btns.rejected.connect(dlg.reject)
        layout.addWidget(btns)

        if dlg.exec_() == QDialog.Accepted:
            sel = []
            for i in range(lw.count()):
                itm = lw.item(i)
                if (
                    itm is not None
                    and hasattr(itm, "isSelected")
                    and hasattr(itm, "text")
                ):
                    try:
                        if itm.isSelected():
                            sel.append(itm.text())
                    except Exception:
                        pass
            try:
                if getattr(self, "yolo_classes_input", None) is not None:
                    self.yolo_classes_input.setText(",".join(sel))
            except Exception:
                pass
            # persist settings and update detector target classes
            try:
                if hasattr(self, "save_settings"):
                    try:
                        self.save_settings()
                    except Exception:
                        pass
            except Exception:
                pass
            try:
                if getattr(self, "yolo_detector", None) is not None:
                    try:
                        self.yolo_detector.set_target_classes(sel)
                    except Exception:
                        pass
            except Exception:
                pass

    def update_yolo_target_classes(self, text_or_list):
        """Update the detector's target classes from a text string or list.

        This is connected to the yolo_classes_input.textChanged signal so
        manual edits to the CSV field apply immediately.
        """
        try:
            if getattr(self, "yolo_detector", None) is not None:
                try:
                    # if signal provides text string, pass directly; if list, pass list
                    self.yolo_detector.set_target_classes(text_or_list)
                    try:
                        self.enhancer.log_serial_output(
                            f"YOLO target classes updated: {text_or_list}", fire=False
                        )
                    except Exception:
                        pass
                except Exception:
                    pass
        except Exception:
            pass

    def _on_trainer_finished(self, weights_path=None):
        """Called when the trainer finishes. Prompts the user to apply the trained weights.

        weights_path: optional path string provided by the trainer. If not provided,
        the trainer window may expose an attribute with the last weights path.
        """
        try:
            # Attempt to resolve a path string
            wp = None
            try:
                if isinstance(weights_path, str) and weights_path:
                    wp = weights_path
            except Exception:
                wp = None

            # try to find a path on the trainer window if not supplied
            try:
                if not wp and getattr(self, "trainer_window", None) is not None:
                    for attr in ("last_weights_path", "weights_path", "final_weights"):
                        try:
                            val = getattr(self.trainer_window, attr, None)
                            if isinstance(val, str) and val:
                                wp = val
                                break
                        except Exception:
                            pass
            except Exception:
                pass

            # Build prompt text
            if wp:
                text = f"Training finished. Use trained weights:\n{wp}\n\nClick Yes to set this model and reload the detector now."
            else:
                text = "Training finished. No weights path was provided by the trainer.\nDo you want to reload the current YOLO model now?"

            # Prompt user (import QMessageBox locally to avoid global import issues)
            try:
                from PyQt5.QtWidgets import QMessageBox
            except Exception:
                QMessageBox = None
            if QMessageBox is None:
                # Unable to show GUI prompt; print and exit handler
                try:
                    print("Training finished:", wp)
                except Exception:
                    pass
                return
            resp = QMessageBox.question(
                self, "Training Finished", text, QMessageBox.Yes | QMessageBox.No
            )

            if resp != QMessageBox.Yes:
                return

            # If user accepted and we have a path, add to combo and load
            if wp:
                # add to model combo if missing
                found = False
                try:
                    model_combo = getattr(self, "yolo_model_combo", None)
                    if model_combo is not None:
                        for i in range(model_combo.count()):
                            try:
                                if model_combo.itemText(i) == wp:
                                    model_combo.setCurrentIndex(i)
                                    found = True
                                    break
                            except Exception:
                                continue
                except Exception:
                    pass

                if not found:
                    try:
                        model_combo = getattr(self, "yolo_model_combo", None)
                        if model_combo is not None:
                            model_combo.addItem(wp)
                            model_combo.setCurrentIndex(model_combo.count() - 1)
                    except Exception:
                        pass

                # Attempt to load into the running detector
                try:
                    self.yolo_detector.load_model(wp)
                    try:
                        if hasattr(self, "enhancer"):
                            self.enhancer.log_serial_output(
                                f"Applied trained model: {wp}", fire=False
                            )
                    except Exception:
                        pass
                except Exception as e:
                    try:
                        QMessageBox.warning(
                            self, "Reload Failed", f"Failed to load trained model: {e}"
                        )
                    except Exception:
                        pass
            else:
                # No wp provided: reload current selection
                try:
                    model_combo = getattr(self, "yolo_model_combo", None)
                    sel = model_combo.currentText() if model_combo is not None else None
                    if sel:
                        try:
                            self.yolo_detector.load_model(sel)
                            try:
                                if hasattr(self, "enhancer"):
                                    self.enhancer.log_serial_output(
                                        f"Reloaded YOLO model: {sel}", fire=False
                                    )
                            except Exception:
                                pass
                        except Exception as e:
                            try:
                                QMessageBox.warning(
                                    self,
                                    "Reload Failed",
                                    f"Failed to load YOLO model: {e}",
                                )
                            except Exception:
                                pass
                except Exception:
                    pass
        except Exception as e:
            try:
                if hasattr(self, "enhancer"):
                    self.enhancer.log_serial_output(
                        f"Trainer finished handler error: {e}", fire=False
                    )
            except Exception:
                print("Trainer finished handler error:", e)

        # Nested open_yolo_class_picker removed (moved earlier). See class-level method.
        """Helper to apply default values to all UI widgets."""

        # Called when settings file is missing or corrupt
        def safe_call(attr_name, method_name, *args, **kwargs):
            w = getattr(self, attr_name, None)
            if w is None:
                return False
            try:
                m = getattr(w, method_name, None)
                if callable(m):
                    m(*args, **kwargs)
                    return True
            except Exception:
                try:
                    # last resort: try to set property directly
                    setattr(w, method_name, args[0] if args else None)
                    return True
                except Exception:
                    return False
            return False

        safe_call("com_port_input", "setText", "COM3")
        safe_call("baud_rate_input", "setValue", 115200)
        # Optimized smoothing for responsive tracking with minimal lag
        safe_call("smoothing_input", "setValue", 0.65)
        # Lowered default so small objects near the camera are detected
        safe_call("min_contour_input", "setValue", 300)
        safe_call("threshold_input", "setValue", 40)
        safe_call("trigger_cooldown_input", "setValue", 1.5)
        # Default to flipped frame; common mounting can require this
        safe_call("flip_checkbox", "setChecked", True)
        safe_call("trigger_mode_combo", "setCurrentIndex", 0)  # MOSFET
        # Optimized for smooth, precise tracking with quick response
        safe_call("tracking_speed_slider", "setValue", 65)
        safe_call("movement_sensitivity_slider", "setValue", 45)
        safe_call("blur_kernel_input", "setValue", 5)
        safe_call("dilate_iter_input", "setValue", 2)
        # Debug default: off
        safe_call("debug_checkbox", "setChecked", False)
        # BackSub warmup default (frames to build background before emitting detections)
        safe_call("backsub_warmup_input", "setValue", 30)
        # overshoot default (0% = no overshoot)
        safe_call("overshoot_input", "setValue", 0)
        # Default to Background Subtraction for more robust stationary-camera detection
        # index 1 corresponds to "Background Subtraction"
        safe_call("detection_mode_combo", "setCurrentIndex", 1)
        safe_call("relay1_button", "setChecked", False)
        if getattr(self, "relay1_button", None):
            try:
                self.relay1_button.setText("LED (Relay1): OFF")
            except Exception:
                pass
        safe_call("relay2_button", "setChecked", False)
        if getattr(self, "relay2_button", None):
            try:
                self.relay2_button.setText("LASER (Relay2): OFF")
            except Exception:
                pass
        # Safety defaults: LOCKED (no fire). Button semantics: checked=True -> ARMED
        safe_call("safety_button", "setChecked", False)
        if getattr(self, "safety_button", None):
            try:
                self.safety_button.setText("Safety: LOCKED (No Fire)")
            except Exception:
                pass
        self.safety_state = 1  # Sync internal var (1 = locked/safe)
        # Invert pan/tilt by default for common builds
        safe_call("invert_pan_checkbox", "setChecked", True)
        safe_call("invert_tilt_checkbox", "setChecked", True)
        safe_call("home_pan_input", "setValue", 90)
        safe_call("home_tilt_input", "setValue", 40)  # FIXED: Changed from 80 to match __init__ and Arduino
        safe_call("pan_min_input", "setValue", 0)
        safe_call("pan_max_input", "setValue", 185)
        safe_call("tilt_min_input", "setValue", 18)
        safe_call("tilt_max_input", "setValue", 110)

        # Default preset index (Balanced)
        try:
            if getattr(self, "preset_combo", None) is not None:
                safe_call("preset_combo", "setCurrentIndex", 1)
        except Exception:
            pass

        # Also set internal defaults (always set these without touching widgets)
        # CRITICAL FIX: Keep consistent with __init__ values
        self.HOME_PAN = 90
        self.HOME_TILT = 40  # FIXED: Match Arduino default (40°), not 80°
        self.prev_pan_angle = self.HOME_PAN
        self.prev_tilt_angle = self.HOME_TILT
        self.target_pan = self.HOME_PAN
        self.target_tilt = self.HOME_TILT
        self.PAN_MIN = 0      # Full left coverage (updated from 5)
        self.PAN_MAX = 220    # Extended horizontal sweep (updated from 185)
        self.TILT_MIN = 0     # Full bottom coverage (updated from 18)
        self.TILT_MAX = 70    # Optimized vertical range (updated from 90)

        # --- Technical / testing tooltips (safe to add even if widgets are missing) ---
        try:
            # Detection & preprocessing
            safe_call(
                "detection_mode_combo",
                "setToolTip",
                "Detection Mode: 0=FrameDiff (fastest motion), 1=BackgroundSub (stationary), 2=YOLO AI (accurate), 3-5=Hybrid modes",
            )
            safe_call(
                "min_contour_input",
                "setToolTip",
                "Minimum object size (pixels). Lower=detect tiny (may cause false positives). Higher=only large (better stability). Start at 500. Typical: 200-1000.",
            )
            safe_call(
                "max_contour_input",
                "setToolTip",
                "Maximum object size (pixels). Prevents tracking huge objects/shadows. Default: 1400000 (~85% frame). Lower=ignore large areas. Keep default unless filtering unwanted detections.",
            )
            safe_call(
                "threshold_input",
                "setToolTip",
                "Pixel threshold (0-255). Lower (20-50)=sensitive, catches motion. Higher (100-200)=ignores noise/shadows. Default: 30. Too low=false positives; too high=misses targets.",
            )
            safe_call(
                "blur_kernel_input",
                "setToolTip",
                "Blur kernel (must be odd: 3,5,7,9...). 3=minimal, 5-7=balanced (recommended), 9+=heavy smoothing. Reduces noise and camera artifacts.",
            )
            safe_call(
                "dilate_iter_input",
                "setToolTip",
                "Dilation iterations (1-10). Expands detected regions to fill gaps. 1-2=minimal, 3-5=good for fragmented detections, 6+=merges objects. Use when detection breaks into pieces.",
            )
            safe_call(
                "backsub_warmup_input",
                "setToolTip",
                "BackgroundSub warmup frames (10-300). Allows algorithm to learn static background. Too low=false positives at startup. Typical: 30-50 frames (1-2 seconds at 30fps).",
            )
            safe_call(
                "overshoot_input",
                "setToolTip",
                "Overshoot (0-50%). Adds leading movement to predict target motion. 0%=disabled. 5-10%=subtle leading (good). 20%+=aggressive (may overshoot). Use for moving targets.",
            )

            # Behavior / control tuning
            safe_call(
                "smoothing_input",
                "setToolTip",
                "Smoothing factor (0.0-1.0). 0=jerky, 0.3-0.5=balanced (recommended), 0.7-1.0=slow/fluid. Higher=smoother servo motion for unstable detection.",
            )
            safe_call(
                "tracking_speed_slider",
                "setToolTip",
                "Tracking speed (0-100%). 0-20%=slow/smooth, 30-60%=balanced (recommended), 70-100%=fast/aggressive. Higher=overshoot risk. Start at 50%.",
            )
            safe_call(
                "movement_sensitivity_slider",
                "setToolTip",
                "Sensitivity (0-100%). 0-20%=very sensitive (detects tiny movements), 30-50%=normal (recommended), 60-100%=insensitive. Too low=jittery; too high=misses targets.",
            )
            safe_call(
                "trigger_cooldown_input",
                "setToolTip",
                "Trigger cooldown (seconds). Minimum delay between fires. 0=fires every frame (dangerous!). 0.5-1.0=short, 2-5=standard. Prevents over-firing and ammo waste.",
            )

            # Debug & diagnostics
            safe_call(
                "debug_checkbox",
                "setToolTip",
                "Debug mode (expert only). Enables verbose logging for troubleshooting. Shows frame analysis and serial data. Warning: Generates lots of output. Use only when diagnosing issues.",
            )

            # Serial / YOLO model controls
            safe_call(
                "com_port_input",
                "setToolTip",
                "Serial COM port (e.g., COM3). USB port where Arduino connects. Windows: COM3-COM12 typical. Check Device Manager or use AUTO. Wrong port=no servo movement.",
            )
            safe_call(
                "baud_rate_input",
                "setToolTip",
                "Baud rate (bits/second). 9600=slow/reliable, 115200=fast (standard, recommended). Must match Arduino firmware. Wrong speed=garbled commands, servo errors.",
            )
            safe_call(
                "yolo_model_combo",
                "setToolTip",
                "YOLO model: nano=fastest/least accurate, small=balanced (recommended), medium=accurate, large=most accurate/slowest. Used in Mode 2 only.",
            )
        except Exception:
            # Non-critical: if tooltips fail, ignore
            pass
        self.trigger_mode_bb = False
        self.relay1_state = 0
        self.relay2_state = 0
        # Keep internal flags in sync with defaults
        self.flip_pan_direction = True
        self.flip_tilt_direction = True

    def load_servo_calibration(self):
        """Load servo calibration values from servo_calibration.json
        
        Applies individually to pan and tilt:
        - Pan: Uses discovered full range
        - Tilt: Uses safe limits (18-90° by default)
        """
        calib_file = "servo_calibration.json"
        
        try:
            if os.path.exists(calib_file):
                with open(calib_file, "r") as f:
                    calib = json.load(f)
                
                # Apply PAN calibration (full range) - UPDATED DEC 8, 2025
                old_pan_min, old_pan_max = self.PAN_MIN, self.PAN_MAX
                self.PAN_MIN = calib.get("pan_min", 0)
                self.PAN_MAX = calib.get("pan_max", 220)
                
                # Apply TILT calibration (safe limits) - UPDATED DEC 8, 2025
                old_tilt_min, old_tilt_max = self.TILT_MIN, self.TILT_MAX
                self.TILT_MIN = calib.get("tilt_min", 0)
                self.TILT_MAX = calib.get("tilt_max", 70)
                
                try:
                    if hasattr(self, "enhancer"):
                        self.enhancer.log_serial_output(
                            f"[CALIBRATION] Pan: {self.PAN_MIN}-{self.PAN_MAX}° | "
                            f"Tilt: {self.TILT_MIN}-{self.TILT_MAX}°",
                            fire=False,
                        )
                except Exception:
                    pass
                
                return True
        except Exception as e:
            try:
                if hasattr(self, "enhancer"):
                    self.enhancer.log_serial_output(
                        f"[WARNING] Failed to load servo calibration: {e}",
                        fire=False,
                    )
            except Exception:
                pass
        
        return False

    def load_settings(self):
        """Load saved settings from JSON file if available."""
        # Load servo calibration first (applies pan/tilt limits)
        self.load_servo_calibration()
        
        settings_path = self.SETTINGS_FILE
        preferred_path = self.PREFERRED_FILE

        # Guard: if UI widgets are not yet created (import-time patching or partial init),
        # avoid trying to access them. Fall back to defaults and postpone loading.
        core_widgets = ["threshold_input", "min_contour_input", "blur_kernel_input"]
        for w in core_widgets:
            if not hasattr(self, w):
                try:
                    print(
                        f"[INFO] load_settings: widget '{w}' missing - applying defaults and deferring load."
                    )
                    if hasattr(self, "enhancer"):
                        self.enhancer.log_serial_output(
                            f"[INFO] load_settings: widget '{w}' missing - using defaults.",
                            fire=False,
                        )
                except Exception:
                    pass
                self.load_default_settings_to_ui()
                return

        if not os.path.exists(settings_path):
            print("[INFO] No settings file found. Using defaults.")
            self.enhancer.log_serial_output(
                "[INFO] No settings file found. Using defaults.", fire=False
            )

            self.load_default_settings_to_ui()
            # If user has preferred defaults, apply them now so first-run uses their preferred settings
            try:
                if os.path.exists(preferred_path):
                    # load preferred into UI and persist as settings.json
                    self.load_preferred_defaults_action()
                else:
                    # Persist the default settings to settings.json
                    try:
                        self.save_settings()
                    except Exception:
                        pass
            except Exception:
                try:
                    self.save_settings()
                except Exception:
                    pass
            return

        try:
            with open(settings_path, "r") as f:
                settings = json.load(f)

            # Restore auto-equalize preference early so layout calls can respect it
            try:
                self.auto_equalize_dock_columns = bool(
                    settings.get("auto_equalize_dock_columns", True)
                )
            except Exception:
                pass
            
            # Restore window maximize preference
            try:
                self.window_maximized_on_startup = bool(
                    settings.get("window_maximized_on_startup", True)
                )
                if self.window_maximized_on_startup:
                    self.showMaximized()
            except Exception:
                self.showMaximized()  # Default: maximize
            
            try:
                if getattr(self, "auto_equalize_action", None) is not None:
                    try:
                        self.auto_equalize_action.setChecked(
                            bool(getattr(self, "auto_equalize_dock_columns", True))
                        )
                    except Exception:
                        pass
            except Exception:
                pass

            # force_exact_dock_widths is now auto-toggled on startup via _auto_equalize_docks_on_startup()
            # Do not restore from settings - always start fresh with auto-equalization
            # The menu item remains functional for manual use during runtime

            # Restore Auto-show Sniper preference (controls whether the
            # Sniper Scope is auto-opened on detections). Default is True.
            try:
                self.auto_show_sniper = bool(settings.get("auto_show_sniper", True))
            except Exception:
                self.auto_show_sniper = True
            try:
                if getattr(self, "auto_show_sniper_action", None) is not None:
                    try:
                        self.auto_show_sniper_action.setChecked(
                            bool(getattr(self, "auto_show_sniper", True))
                        )
                    except Exception:
                        pass
            except Exception:
                pass

            # --- Load Tuning/Detection ---
            self._safe_widget_call(
                "threshold_input", "setValue", settings.get("threshold", 40)
            )
            self._safe_widget_call(
                "min_contour_input", "setValue", settings.get("min_contour", 1000)
            )
            self._safe_widget_call(
                "max_contour_input", "setValue", settings.get("max_contour", 1400000)
            )
            # restore debug checkbox
            self._safe_widget_call(
                "debug_checkbox", "setChecked", settings.get("debug_mode", False)
            )
            self._safe_widget_call(
                "blur_kernel_input", "setValue", settings.get("blur_kernel", 5)
            )
            self._safe_widget_call(
                "dilate_iter_input", "setValue", settings.get("dilate_iter", 2)
            )
            # restore BackSub warmup
            self._safe_widget_call(
                "backsub_warmup_input", "setValue", settings.get("backsub_warmup", 30)
            )
            self._safe_widget_call(
                "overshoot_input", "setValue", settings.get("overshoot_percent", 0)
            )
            self._safe_widget_call(
                "deadzone_slider", "setValue", settings.get("deadzone", 20)
            )
            self._safe_widget_call(
                "tracking_speed_slider", "setValue", settings.get("tracking_speed", 50)
            )
            self._safe_widget_call(
                "trigger_cooldown_input",
                "setValue",
                settings.get("trigger_cooldown", 1.5),
            )

            self.auto_tracking_enabled = settings.get("auto_tracking", False)
            self.detection_enabled = settings.get("detection_enabled", False)

            # Default to True for invert and flip if not present in settings (safer for many mounts)
            self._safe_widget_call(
                "invert_pan_checkbox", "setChecked", settings.get("invert_pan", True)
            )
            self._safe_widget_call(
                "invert_tilt_checkbox", "setChecked", settings.get("invert_tilt", True)
            )
            self._safe_widget_call(
                "flip_checkbox", "setChecked", settings.get("flip_image", True)
            )

            # tooltips for detection widgets
            try:
                self._safe_widget_call(
                    "threshold_input",
                    "setToolTip",
                    "Pixel difference threshold for frame-diff/backsub (0-255).",
                )
                self._safe_widget_call(
                    "min_contour_input",
                    "setToolTip",
                    "Minimum contour area (px) to consider a detection.",
                )
                self._safe_widget_call(
                    "blur_kernel_input",
                    "setToolTip",
                    "Gaussian blur kernel size (odd). Helps reduce noise.",
                )
                self._safe_widget_call(
                    "dilate_iter_input",
                    "setToolTip",
                    "Number of dilation iterations after morphology.",
                )
                self._safe_widget_call(
                    "detection_mode_combo",
                    "setToolTip",
                    "Choose detection mode: FrameDiff, BackgroundSub, or YOLO.",
                )
                self._safe_widget_call(
                    "debug_checkbox",
                    "setToolTip",
                    "Enable verbose pipeline debug prints to console.",
                )
                self._safe_widget_call(
                    "backsub_warmup_input",
                    "setToolTip",
                    "Number of frames BackgroundSub will observe before emitting detections.",
                )
                self._safe_widget_call(
                    "overshoot_input",
                    "setToolTip",
                    "Percent overshoot added to pan/tilt command. Applies to all detection modes.",
                )
            except Exception:
                pass

            # --- Load Hardware/Config (Old logic, merged) ---
            self._safe_widget_call(
                "com_port_input", "setText", settings.get("com_port", "COM3")
            )
            self._safe_widget_call(
                "baud_rate_input", "setValue", settings.get("baud_rate", 115200)
            )
            self._safe_widget_call(
                "smoothing_input", "setValue", settings.get("smoothing_factor", 0.5)
            )
            self._safe_widget_call(
                "movement_sensitivity_slider",
                "setValue",
                settings.get("movement_sensitivity", 50),
            )
            self._safe_widget_call(
                "detection_mode_combo",
                "setCurrentIndex",
                settings.get("detection_mode_index", 0),
            )

            # Load manual control settings
            try:
                self._safe_widget_call(
                    "step_size_input",
                    "setValue",
                    settings.get("step_size", self.STEP_INCREMENT),
                )
                self._safe_widget_call(
                    "manual_speed_slider", "setValue", settings.get("manual_speed", 50)
                )
            except Exception:
                pass

            # --- Load Limits (UPDATED DEC 8, 2025) ---
            self.PAN_MIN = int(settings.get("pan_min", 0))
            self.PAN_MAX = int(settings.get("pan_max", 220))
            self.TILT_MIN = int(settings.get("tilt_min", 0))
            self.TILT_MAX = int(settings.get("tilt_max", 70))
            self._safe_widget_call("pan_min_input", "setValue", self.PAN_MIN)
            self._safe_widget_call("pan_max_input", "setValue", self.PAN_MAX)
            self._safe_widget_call("tilt_min_input", "setValue", self.TILT_MIN)
            self._safe_widget_call("tilt_max_input", "setValue", self.TILT_MAX)

            # --- Load Home & State ---
            self.HOME_PAN = int(settings.get("home_pan", self.HOME_PAN))
            self.HOME_TILT = int(settings.get("home_tilt", self.HOME_TILT))
            self._safe_widget_call(
                "home_pan_input",
                "setValue",
                int(np.clip(self.HOME_PAN, self.PAN_MIN, self.PAN_MAX)),
            )
            self._safe_widget_call(
                "home_tilt_input",
                "setValue",
                int(np.clip(self.HOME_TILT, self.TILT_MIN, self.TILT_MAX)),
            )

            self.prev_pan_angle = settings.get("last_pan_angle", self.HOME_PAN)
            self.prev_tilt_angle = settings.get("last_tilt_angle", self.HOME_TILT)
            self.target_pan = self.prev_pan_angle
            self.target_tilt = self.prev_tilt_angle
            
            # Load opacity settings
            self._safe_widget_call(
                "vignette_opacity_slider", "setValue", settings.get("vignette_opacity", 50)
            )
            self._safe_widget_call(
                "text_bg_opacity_slider", "setValue", settings.get("text_bg_opacity", 100)
            )
            
            # Load scope visual settings from floating window sliders
            self._safe_widget_call(
                "crosshair_length_slider", "setValue", settings.get("crosshair_length", 30)
            )
            self._safe_widget_call(
                "gap_slider", "setValue", settings.get("gap", 10)
            )
            self._safe_widget_call(
                "crosshair_thickness_slider", "setValue", settings.get("crosshair_thickness", 2)
            )
            self._safe_widget_call(
                "scope_radius_percent_slider", "setValue", settings.get("scope_radius_pct", 35)
            )
            self._safe_widget_call(
                "corner_size_slider", "setValue", settings.get("corner_size", 40)
            )
            self._safe_widget_call(
                "status_text_scale_slider", "setValue", settings.get("status_text_scale_x10", 12)
            )
            
            # Load scope window opacity settings specifically for floating window
            self._safe_widget_call(
                "vignette_opacity_slider_scope", "setValue", settings.get("vignette_opacity", 50)
            )
            self._safe_widget_call(
                "text_bg_opacity_slider_scope", "setValue", settings.get("text_bg_opacity", 100)
            )

            self.trigger_mode_bb = settings.get(
                "trigger_mode_bb", False
            )  # Default to MOSFET
            self.trigger_mode_combo.setCurrentIndex(1 if self.trigger_mode_bb else 0)

            # Manual-mode auto-fire setting
            manual_auto = settings.get("manual_auto_fire", False)
            try:
                self.manual_auto_fire_checkbox.setChecked(bool(manual_auto))
            except Exception:
                pass

            # Sound effects toggle
            try:
                sound_on = settings.get("sound_enabled", True)
                self.sound_enabled = bool(sound_on)
                try:
                    self.sound_checkbox.setChecked(self.sound_enabled)
                except Exception:
                    pass
            except Exception:
                pass

            # --- Load Relay States ---
            self.relay1_state = settings.get("relay1", 0)
            self.relay2_state = settings.get("relay2", 0)
            self.relay1_button.setChecked(bool(self.relay1_state))
            self.relay1_button.setText(
                "LED (Relay1): ON" if self.relay1_state else "LED (Relay1): OFF"
            )
            self.relay2_button.setChecked(bool(self.relay2_state))
            self.relay2_button.setText(
                "LASER (Relay2): ON" if self.relay2_state else "LASER (Relay2): OFF"
            )

            # --- Load Safety State (using user's key 'safety_lock') ---
            # 'safety_lock' is stored as True when LOCKED (safe). Button checked==ARMED
            is_locked = settings.get("safety_lock", True)
            # Map to button semantics: checked=True means ARMED, so invert
            try:
                self.safety_button.setChecked(False if is_locked else True)
            except Exception:
                pass

            # Sync internal variable and text
            if is_locked:
                self.safety_state = 1
                self.safety_button.setText("Safety: LOCKED (No Fire)")
            else:
                self.safety_state = 0
                self.safety_button.setText("Safety: ARMED (Can Fire)")

            # ========== FIXED: INITIALIZE TILT_SAFETY_LABEL STATE ==========
            # Match label text to actual tilt_safety_switch_enabled setting
            # (Previously always showed OK even if disabled)
            try:
                if hasattr(self, "tilt_safety_label"):
                    if self.tilt_safety_switch_enabled:
                        self.tilt_safety_label.setText("🛡️ Tilt Safety: Enabled")
                        self.tilt_safety_label.setStyleSheet("color: #00FF00; font-size: 10px; background-color: #2d2d2d;")
                    else:
                        self.tilt_safety_label.setText("🛡️ Tilt Safety: Disabled")
                        self.tilt_safety_label.setStyleSheet("color: #FFFF00; font-size: 10px; background-color: #2d2d2d;")
            except Exception:
                pass

            self.enhancer.log_serial_output("Settings loaded successfully.")

            # Restore snap threshold if present
            try:
                snap_val = settings.get("snap_threshold", None)
                if (
                    snap_val is not None
                    and getattr(self, "snap_threshold_slider", None) is not None
                ):
                    self.snap_threshold_slider.setValue(int(snap_val))
            except Exception:
                pass

            # --- Load Aim Aggression Settings (NEW - Dec 2024) ---
            try:
                self.aim_aggression = int(settings.get("aim_aggression", 50))
                self.final_approach_boost = bool(settings.get("final_approach_boost", True))
                # Update UI widgets if present
                if getattr(self, "aim_aggression_slider", None) is not None:
                    self.aim_aggression_slider.setValue(self.aim_aggression)
                if getattr(self, "aim_aggression_label", None) is not None:
                    self.aim_aggression_label.setText(str(self.aim_aggression))
                if getattr(self, "final_approach_boost_checkbox", None) is not None:
                    self.final_approach_boost_checkbox.setChecked(self.final_approach_boost)
            except Exception:
                pass

            # --- Load Hold Behavior Settings ---
            try:
                self.lost_hold_seconds = float(
                    settings.get(
                        "hold_seconds", getattr(self, "lost_hold_seconds", 5.0)
                    )
                )
                # 'hold_infinite' when True -> never time out the hold (infinite hold)
                self.hold_infinite = bool(
                    settings.get("hold_infinite", getattr(self, "hold_infinite", False))
                )
                try:
                    # update UI widgets if present
                    if getattr(self, "lost_hold_input", None) is not None:
                        self.lost_hold_input.setValue(self.lost_hold_seconds)
                    if getattr(self, "hold_infinite_checkbox", None) is not None:
                        self.hold_infinite_checkbox.setChecked(self.hold_infinite)
                    # Load HOME-return behavior settings
                    try:
                        hr = settings.get("home_return_mode", None)
                        if hr is not None:
                            try:
                                self.home_return_mode = str(hr)
                            except Exception:
                                self.home_return_mode = "Immediate"
                            try:
                                if (
                                    getattr(self, "home_return_mode_combo", None)
                                    is not None
                                ):
                                    idx = self.home_return_mode_combo.findText(
                                        str(self.home_return_mode)
                                    )
                                    if idx != -1:
                                        self.home_return_mode_combo.setCurrentIndex(idx)
                            except Exception:
                                pass
                    except Exception:
                        pass
                    try:
                        # Restore idle behavior selection if present
                        ib = settings.get("idle_behavior", None)
                        if ib is not None:
                            try:
                                self.idle_behavior = str(ib).strip().lower()
                            except Exception:
                                self.idle_behavior = "home"
                            try:
                                if getattr(self, "idle_behavior_combo", None) is not None:
                                    idx = self.idle_behavior_combo.findText(
                                        str(self.idle_behavior).capitalize()
                                    )
                                    if idx != -1:
                                        self.idle_behavior_combo.setCurrentIndex(idx)
                            except Exception:
                                pass
                    except Exception:
                        pass
                    try:
                        # Restore idle mode toggle button state if present
                        idle_enabled = settings.get("idle_mode_enabled", False)
                        if idle_enabled:
                            try:
                                if getattr(self, "idle_mode_toggle_btn", None) is not None:
                                    self.idle_mode_toggle_btn.setChecked(True)
                                    self.idle_mode_toggle_btn.setText("Disable Idle Mode")
                                    # Also activate the idle mode
                                    idle_modes = getattr(self, "idle_modes", None)
                                    if idle_modes is not None:
                                        idle_behavior = str(getattr(self, "idle_behavior", "rest")).lower()
                                        idle_modes.set_mode(idle_behavior)
                            except Exception:
                                pass
                    except Exception:
                        pass
                    try:
                        try:
                            rf_rate = int(settings.get("rapid_fire_rate_hz", getattr(self, "rapid_fire_rate_hz", 1)))
                        except Exception:
                            rf_rate = int(getattr(self, "rapid_fire_rate_hz", 1))
                        try:
                            self.rapid_fire_rate_hz = rf_rate
                            if getattr(self, "rapid_fire_rate_spin", None) is not None:
                                try:
                                    self.rapid_fire_rate_spin.setValue(int(self.rapid_fire_rate_hz))
                                except Exception:
                                    pass
                        except Exception:
                            pass

                        try:
                            rf_duty = int(settings.get("rapid_fire_duty_percent", int(getattr(self, "rapid_fire_duty", 0.5) * 100)))
                        except Exception:
                            rf_duty = int(getattr(self, "rapid_fire_duty", 0.5) * 100)
                        try:
                            self.rapid_fire_duty = float(rf_duty) / 100.0
                            if getattr(self, "rapid_fire_duty_slider", None) is not None:
                                try:
                                    self.rapid_fire_duty_slider.setValue(int(rf_duty))
                                except Exception:
                                    pass
                        except Exception:
                            pass

                        try:
                            rf_enabled = bool(settings.get("rapid_fire_enabled", getattr(self, "rapid_fire_enabled", False)))
                        except Exception:
                            rf_enabled = bool(getattr(self, "rapid_fire_enabled", False))
                        try:
                            self.rapid_fire_enabled = rf_enabled
                            if getattr(self, "rapid_fire_enable_checkbox", None) is not None:
                                try:
                                    self.rapid_fire_enable_checkbox.setChecked(bool(rf_enabled))
                                except Exception:
                                    pass
                        except Exception:
                            pass
                    except Exception:
                        pass
                    except Exception:
                        pass
                    try:
                        suspend_sec = float(
                            settings.get(
                                "home_move_suspend_seconds",
                                getattr(self, "home_move_suspend_seconds", 2.0),
                            )
                        )
                        self.home_move_suspend_seconds = suspend_sec
                        if getattr(self, "home_return_suspend_input", None) is not None:
                            try:
                                self.home_return_suspend_input.setValue(
                                    float(self.home_move_suspend_seconds)
                                )
                            except Exception:
                                pass
                    except Exception:
                        pass
                    # Restore camera selection if present
                    if getattr(self, "camera_index_combo", None) is not None:
                        try:
                            ci = int(settings.get("camera_index", 0))
                            # Clamp to valid range
                            if ci < 0:
                                ci = 0
                            if ci > (self.camera_index_combo.count() - 1):
                                ci = 0
                            self.camera_index_combo.setCurrentIndex(ci)
                        except Exception:
                            try:
                                # fallback: set to Auto
                                self.camera_index_combo.setCurrentIndex(0)
                            except Exception:
                                pass
                    
                    # Restore frame ratio (resolution) setting if present
                    if getattr(self, "frame_ratio_combo", None) is not None:
                        try:
                            frame_ratio = str(settings.get("frame_ratio_setting", "640x480"))
                            idx = self.frame_ratio_combo.findText(frame_ratio)
                            if idx >= 0:
                                self.frame_ratio_combo.setCurrentIndex(idx)
                            # Trigger the handler to update frame dimensions
                            self._on_frame_ratio_changed(frame_ratio)
                        except Exception:
                            try:
                                # fallback: use default 640x480
                                self.frame_ratio_combo.setCurrentIndex(0)
                                self._on_frame_ratio_changed("640x480")
                            except Exception:
                                pass
                except Exception:
                    pass
            except Exception:
                # keep defaults if anything goes wrong
                pass

            # Restore splitter sizes if present
            sizes = settings.get("splitter_sizes", None)
            try:
                if sizes and getattr(self, "splitter", None) is not None:
                    # sizes should be a list of ints
                    self.splitter.setSizes(list(sizes))
            except Exception:
                pass

            # --- Load YOLO Settings ---
            yolo_model = settings.get("yolo_model")
            if yolo_model:
                index = self.yolo_model_combo.findText(yolo_model)
                if index != -1:
                    self.yolo_model_combo.setCurrentIndex(index)
            self.yolo_confidence_input.setValue(settings.get("yolo_confidence", 0.5))
            self.yolo_classes_input.setText(settings.get("yolo_classes", "person"))
            # Restore additional YOLO settings if present
            try:
                if getattr(self, "yolo_max_results_input", None) is not None:
                    try:
                        self.yolo_max_results_input.setValue(
                            int(settings.get("yolo_max_results", 0))
                        )
                    except Exception:
                        pass
                if getattr(self, "yolo_min_area_input", None) is not None:
                    try:
                        self.yolo_min_area_input.setValue(
                            int(settings.get("yolo_min_area", 0))
                        )
                    except Exception:
                        pass
            except Exception:
                pass
            # Update detector target classes from persisted setting
            try:
                classes = settings.get("yolo_classes", "")
                if getattr(self, "yolo_detector", None) is not None:
                    try:
                        self.yolo_detector.set_target_classes(classes)
                    except Exception:
                        pass
            except Exception:
                pass

            # --- Load Hybrid Detection Settings ---
            try:
                if getattr(self, "fusion_strategy_combo", None) is not None:
                    fusion_idx = settings.get("fusion_strategy", 0)
                    self.fusion_strategy_combo.setCurrentIndex(int(fusion_idx))
                if getattr(self, "motion_gate_threshold_input", None) is not None:
                    motion_gate = settings.get("motion_gate_threshold", 1.0)
                    self.motion_gate_threshold_input.setValue(float(motion_gate))
                if getattr(self, "overlap_threshold_input", None) is not None:
                    overlap = settings.get("overlap_threshold", 30.0)
                    self.overlap_threshold_input.setValue(float(overlap))
            except Exception:
                pass

            self.on_detection_mode_change(self.detection_mode_combo.currentIndex())

            # Restore window/dock geometry/state if present
            try:
                ws = settings.get("window_state", None)
                if ws and isinstance(ws, str):
                    raw = base64.b64decode(ws)
                    self.restoreState(QByteArray(raw))

                wg = settings.get("window_geometry", None)
                if wg and isinstance(wg, str):
                    rawg = base64.b64decode(wg)
                    self.restoreGeometry(QByteArray(rawg))
            
                # If settings include sniper visibility/floating preferences,
                # apply them now. Persisted 'sniper_visible' explicitly hides
                # the sniper and marks it as user-closed so it won't be auto-shown.
                try:
                    sniper_vis = settings.get("sniper_visible", None)
                    sniper_float = settings.get("sniper_floating", None)
                    sniper_dock = getattr(self, "sniper_dock", None)
                    if sniper_dock is not None:
                        try:
                            if sniper_float is not None:
                                try:
                                    sniper_dock.setFloating(bool(sniper_float))
                                except Exception:
                                    pass
                        except Exception:
                            pass
                        try:
                            if sniper_vis is not None:
                                if bool(sniper_vis):
                                    try:
                                        sniper_dock.show()
                                        sniper_dock.raise_()
                                    except Exception:
                                        pass
                                    try:
                                        self._sniper_user_closed = False
                                    except Exception:
                                        pass
                                else:
                                    try:
                                        sniper_dock.hide()
                                    except Exception:
                                        pass
                                    try:
                                        # Treat persisted hidden as user-closed to avoid auto-show
                                        self._sniper_user_closed = True
                                    except Exception:
                                        pass
                        except Exception:
                            pass
                except Exception:
                    pass
            except Exception:
                pass

            # Re-equalize dock widths after restoring geometry/state (delayed)
            try:
                try:
                    # Refresh saved layout list UI so Layout dock reflects persisted profiles
                    try:
                        self._refresh_layout_list()
                    except Exception:
                        pass
                except Exception:
                    pass
                QTimer.singleShot(200, lambda: self.equalize_dock_columns())
            except Exception:
                pass

        except Exception as e:
            print(f"[WARN] Could not load settings: {e}")
            self.enhancer.log_serial_output(
                f"Load settings error: {e}. Using defaults.", fire=False
            )
            self.load_default_settings_to_ui()

    def save_settings(self):
        """Save current settings to JSON file."""

        # Build settings dict via helper so other routines can reuse it
        def get_settings_dict():
            # Use getattr to avoid exceptions if save_settings is triggered during UI construction
            def val(widget_name, default=None, attr="value"):
                # Use safe helpers to avoid attribute-on-None and provide typed defaults
                if attr == "value":
                    return self._safe_widget_method_return(
                        widget_name, "value", default
                    )
                if attr == "text":
                    return self._safe_widget_method_return(widget_name, "text", default)
                if attr == "checked":
                    return self._safe_widget_method_return(
                        widget_name, "isChecked", default
                    )
                if attr == "index":
                    return self._safe_widget_method_return(
                        widget_name, "currentIndex", default
                    )
                if attr == "currentText":
                    return self._safe_widget_method_return(
                        widget_name, "currentText", default
                    )
                # Fallback to getattr
                w = getattr(self, widget_name, None)
                if w is None:
                    return default
                try:
                    return getattr(w, attr)
                except Exception:
                    return default

            settings = {
                # New parameters from user request
                "threshold": val("threshold_input", 40),
                "min_contour": val("min_contour_input", 300),
                "max_contour": val("max_contour_input", 1400000),
                "debug_mode": val("debug_checkbox", False, "checked"),
                "blur_kernel": val("blur_kernel_input", 5),
                "dilate_iter": val("dilate_iter_input", 2),
                "overshoot_percent": val("overshoot_input", 0),
                "deadzone": val("deadzone_slider", 40),
                "tracking_speed": val("tracking_speed_slider", 50),
                "trigger_cooldown": val("trigger_cooldown_input", 1.5),
                "auto_tracking": getattr(self, "auto_tracking_enabled", False),
                "detection_enabled": getattr(self, "detection_enabled", False),
                "invert_pan": val("invert_pan_checkbox", False, "checked"),
                "invert_tilt": val("invert_tilt_checkbox", False, "checked"),
                "step_size": val("step_size_input", self.STEP_INCREMENT),
                "manual_speed": val("manual_speed_slider", 50),
                "flip_image": val("flip_checkbox", False, "checked"),
                # store as True when LOCKED; button checked==ARMED so invert
                "safety_lock": (not val("safety_button", False, "checked")),
                # Old parameters from existing code, merged
                "com_port": val("com_port_input", "COM3", "text"),
                "baud_rate": val("baud_rate_input", 115200),
                "smoothing_factor": val("smoothing_input", 0.5),
                "movement_sensitivity": val("movement_sensitivity_slider", 50),
                "detection_mode_index": val("detection_mode_combo", 0, "index"),
                "home_pan": val("home_pan_input", 90),
                "home_tilt": val("home_tilt_input", 40),
                "snap_threshold": val("snap_threshold_slider", 40),
                # Aim aggression settings (NEW - Dec 2024)
                "aim_aggression": getattr(self, "aim_aggression", 50),
                "final_approach_boost": getattr(self, "final_approach_boost", True),
                "manual_auto_fire": val("manual_auto_fire_checkbox", False, "checked"),
                "sound_enabled": getattr(self, "sound_enabled", True),
                "sound_volume": val("sound_volume_slider", 80),
                # Recording settings
                "recording_enabled": val("recording_enabled_checkbox", False, "checked"),
                "autorecord": val("autorecord_checkbox", False, "checked"),
                "video_format": val("video_format_combo", "MP4 (H.264)", "currentText"),
                "fps": val("fps_combo", 30, "currentText"),
                "quality": val("quality_combo", "Medium (5000 kbps)", "currentText"),
                "recording_dir": val("recording_dir_input", str(Path.home() / "Videos" / "Turret"), "text"),
                "storage_limit_gb": val("storage_limit_spinbox", 10.0),
                "autocleanup": val("autocleanup_checkbox", True, "checked"),
                "last_pan_angle": getattr(self, "prev_pan_angle", 90),
                "last_tilt_angle": getattr(self, "prev_tilt_angle", 40),
                "trigger_mode_bb": getattr(self, "trigger_mode_bb", False),
                "relay1": getattr(self, "relay1_state", 0),
                "relay2": getattr(self, "relay2_state", 0),
                "safety_state": getattr(
                    self, "safety_state", 1
                ),  # Keep internal state too
                "pan_min": getattr(self, "PAN_MIN", 5),
                "pan_max": getattr(self, "PAN_MAX", 185),
                "backsub_warmup": val("backsub_warmup_input", 30),
                "tilt_min": getattr(self, "TILT_MIN", 18),
                "tilt_max": getattr(self, "TILT_MAX", 110),
                "yolo_model": val("yolo_model_combo", None, "currentText"),
                "yolo_confidence": val("yolo_confidence_input", 0.5),
                "yolo_classes": val("yolo_classes_input", "person", "text"),
                "yolo_max_results": val("yolo_max_results_input", 0),
                "yolo_min_area": val("yolo_min_area_input", 0),
                "preset_index": self._safe_current_index("preset_combo", 1),
                # Hybrid detection mode settings
                "fusion_strategy": val("fusion_strategy_combo", 0, "index"),
                "motion_gate_threshold": val("motion_gate_threshold_input", 1.0),
                "overlap_threshold": val("overlap_threshold_input", 30.0),
                # new hold behavior settings
                "hold_seconds": getattr(self, "lost_hold_seconds", 5.0),
                "hold_infinite": getattr(self, "hold_infinite", False),
                # Home-return behavior
                "home_return_mode": val(
                    "home_return_mode_combo",
                    str(getattr(self, "home_return_mode", "Immediate")),
                    "currentText",
                ),
                # Idle behavior (what to do after hold-on-loss expires)
                "idle_behavior": val(
                    "idle_behavior_combo",
                    str(getattr(self, "idle_behavior", "home")).capitalize(),
                    "currentText",
                ),
                # Idle mode toggle button state
                "idle_mode_enabled": val("idle_mode_toggle_btn", False, "checked"),
                # Rapid-fire MOSFET settings
                "rapid_fire_rate_hz": val("rapid_fire_rate_spin", getattr(self, "rapid_fire_rate_hz", 1)),
                "rapid_fire_enabled": val("rapid_fire_enable_checkbox", getattr(self, "rapid_fire_enabled", False), "checked"),
                "rapid_fire_duty_percent": val("rapid_fire_duty_slider", int(getattr(self, "rapid_fire_duty", 0.5) * 100)),
                "home_move_suspend_seconds": val(
                    "home_return_suspend_input",
                    getattr(self, "home_move_suspend_seconds", 2.0),
                ),
                # UI behavior toggles
                "auto_equalize_dock_columns": getattr(self, "auto_equalize_dock_columns", True),
                # force_exact_dock_widths is auto-toggled on startup, not persisted
                # Whether the sniper dock should be auto-shown when detections appear
                "auto_show_sniper": getattr(self, "auto_show_sniper", True),
                # Whether window should be maximized on startup
                "window_maximized_on_startup": getattr(self, "window_maximized_on_startup", True),
                # Persist whether the sniper dock was visible/floating when saved
                "sniper_visible": bool(
                    getattr(getattr(self, "sniper_dock", None), "isVisible", lambda: False)()
                ),
                "sniper_floating": bool(
                    getattr(getattr(self, "sniper_dock", None), "isFloating", lambda: False)()
                ),
                # Camera selection: 'Auto' (0) or specific index (1..5 mapping to 0..4)
                "camera_index": self._safe_current_index("camera_index_combo", 0),
                # Frame ratio (resolution) setting
                "frame_ratio_setting": getattr(self, "frame_ratio_setting", "640x480"),
                # Opacity controls for visual effects
                "vignette_opacity": val("vignette_opacity_slider", 50),
                "text_bg_opacity": val("text_bg_opacity_slider", 100),
                # Scope visual settings (floating window)
                "crosshair_length": val("crosshair_length_slider", 30),
                "gap": val("gap_slider", 10),
                "crosshair_thickness": val("crosshair_thickness_slider", 2),
                "scope_radius_pct": val("scope_radius_percent_slider", 35),
                "corner_size": val("corner_size_slider", 40),
                "status_text_scale_x10": val("status_text_scale_slider", 12),
                # Save main window geometry and dock/widget state (base64 encoded)
                "window_state": None,
                "window_geometry": None,
            }

            # Capture window state and geometry
            if hasattr(self, "saveState"):
                st = self.saveState()
                settings["window_state"] = base64.b64encode(st.data()).decode("ascii")
            if hasattr(self, "saveGeometry"):
                geom = self.saveGeometry()
                settings["window_geometry"] = base64.b64encode(geom.data()).decode(
                    "ascii"
                )

            return settings

        try:
            settings = get_settings_dict()
            settings_path = self.SETTINGS_FILE
            try:
                # Preserve any existing 'layouts' profiles to avoid accidental overwrite
                try:
                    if os.path.exists(settings_path):
                        try:
                            with open(settings_path, "r") as oldf:
                                old = json.load(oldf) or {}
                        except Exception:
                            old = {}
                        if isinstance(old, dict) and "layouts" in old:
                            try:
                                # merge layouts into our settings unless already present
                                if "layouts" not in settings:
                                    settings["layouts"] = old.get("layouts", {})
                            except Exception:
                                pass
                except Exception:
                    pass

                with open(settings_path, "w") as f:
                    json.dump(settings, f, indent=4)
            except Exception as e:
                # best-effort save: ignore
                print(f"Could not write settings to file: {e}")
            # self.serial_output.append("Settings saved.") # Too spammy for auto-save
        except Exception as e:
            print(f"[WARN] Could not save settings: {e}")
            try:
                try:
                    # use central writer which respects pause/buffer
                    if getattr(self, "_serial_write", None):
                        self._serial_write(f"Save settings error: {e}")
                    else:
                        self.serial_output.append(f"Save settings error: {e}")
                except Exception:
                    try:
                        self.serial_output.append(f"Save settings error: {e}")
                    except Exception:
                        pass
            except Exception:
                pass

    def save_dock_layout(self):
        """Save current window/dock layout immediately to settings.json (base64 encoded)."""
        try:
            # Delay the actual save slightly to let Qt process any pending
            # layout changes (useful if user drags a dock then immediately
            # clicks Save Layout). Use a short singleShot timer; if QTimer
            # isn't available for any reason, fall back to immediate save.
            def _do_save():
                try:
                    # Read existing settings if present
                    s = {}
                    try:
                        if os.path.exists(self.SETTINGS_FILE):
                            with open(self.SETTINGS_FILE, "r") as f:
                                s = json.load(f) or {}
                    except Exception:
                        s = s or {}

                    # Capture state/geometry from the QMainWindow
                    try:
                        st = self.saveState()
                        s["window_state"] = base64.b64encode(st.data()).decode("ascii")
                    except Exception:
                        pass
                    try:
                        geom = self.saveGeometry()
                        s["window_geometry"] = base64.b64encode(geom.data()).decode(
                            "ascii"
                        )
                    except Exception:
                        pass

                    # Persist into settings.json (merge with existing settings)
                    try:
                        with open(self.SETTINGS_FILE, "w") as f:
                            json.dump(s, f, indent=4)
                        try:
                            self.enhancer.log_serial_output(
                                "Layout saved successfully.", fire=False
                            )
                        except Exception:
                            pass
                    except Exception as e:
                        try:
                            self.enhancer.log_serial_output(
                                f"Layout save failed: {e}", fire=False
                            )
                        except Exception:
                            pass

                    # Also write layout snapshot to preferred defaults so the
                    # layout becomes part of the user's preferred profile.
                    try:
                        prefs = {}
                        if os.path.exists(self.PREFERRED_FILE):
                            try:
                                with open(self.PREFERRED_FILE, "r") as pf:
                                    prefs = json.load(pf) or {}
                            except Exception:
                                prefs = prefs or {}
                        # Store layout keys (may overwrite if present)
                        if "window_state" in s:
                            prefs["window_state"] = s.get("window_state")
                        if "window_geometry" in s:
                            prefs["window_geometry"] = s.get("window_geometry")
                        # Record whether the sniper dock is floating so we can restore that intent
                        try:
                            sniper = getattr(self, "sniper_dock", None)
                            if sniper is not None:
                                try:
                                    prefs["sniper_floating"] = bool(sniper.isFloating())
                                except Exception:
                                    pass
                        except Exception:
                            pass
                        try:
                            with open(self.PREFERRED_FILE, "w") as pf:
                                json.dump(prefs, pf, indent=4)
                        except Exception:
                            pass
                    except Exception:
                        pass
                
                except Exception:
                    pass

                

            try:
                QTimer.singleShot(150, _do_save)
            except Exception:
                # Fallback to immediate write if timers fail for any reason
                _do_save()
        except Exception:
            pass

    def _refresh_layout_list(self):
        """Populate the Layout list widget from saved profiles in settings.json."""
        try:
            s = {}
            try:
                if os.path.exists(self.SETTINGS_FILE):
                    with open(self.SETTINGS_FILE, "r") as f:
                        s = json.load(f) or {}
            except Exception:
                s = s or {}

            layouts = s.get("layouts", {}) if isinstance(s, dict) else {}

            try:
                if getattr(self, "layout_list", None) is not None:
                    # Clear existing entries if widget supports it
                    if getattr(self.layout_list, "clear", None):
                        try:
                            self.layout_list.clear()
                        except Exception:
                            pass
                    # Populate list
                    for name in sorted(layouts.keys()):
                        try:
                            if getattr(self.layout_list, "addItem", None):
                                self.layout_list.addItem(name)
                            else:
                                # Fallback: append text if it's a QTextEdit
                                if getattr(self.layout_list, "append", None):
                                    try:
                                        self.layout_list.append(name)
                                    except Exception:
                                        pass
                                else:
                                    try:
                                        cur = (
                                            self.layout_list.toPlainText()
                                            if getattr(self.layout_list, "toPlainText", None)
                                            else ""
                                        )
                                        self.layout_list.setPlainText(
                                            (cur + "\n" + name).strip()
                                        )
                                    except Exception:
                                        pass
                        except Exception:
                            pass
            except Exception:
                pass
        except Exception:
            pass

    def _gather_current_settings(self):
        """Collect a broad set of current UI settings into a dict for presets."""
        s = {}
        try:
            def safe_int(name, fallback=0):
                try:
                    w = getattr(self, name, None)
                    if w is None:
                        return int(fallback)
                    if hasattr(w, 'value'):
                        return int(w.value())
                    if hasattr(w, 'text'):
                        return int(w.text())
                    return int(fallback)
                except Exception:
                    return int(fallback)

            def safe_float(name, fallback=0.0):
                try:
                    w = getattr(self, name, None)
                    if w is None:
                        return float(fallback)
                    if hasattr(w, 'value'):
                        return float(w.value())
                    if hasattr(w, 'text'):
                        return float(w.text())
                    return float(fallback)
                except Exception:
                    return float(fallback)

            def safe_text(name, fallback=''):
                try:
                    w = getattr(self, name, None)
                    if w is None:
                        return str(fallback)
                    if hasattr(w, 'text'):
                        return str(w.text())
                    if hasattr(w, 'currentText'):
                        try:
                            return str(w.currentText())
                        except Exception:
                            return str(fallback)
                    return str(fallback)
                except Exception:
                    return str(fallback)

            # Servo limits & Home
            s['pan_min'] = safe_int('pan_min_input', getattr(self, 'PAN_MIN', 0))
            s['pan_max'] = safe_int('pan_max_input', getattr(self, 'PAN_MAX', 180))
            s['tilt_min'] = safe_int('tilt_min_input', getattr(self, 'TILT_MIN', 0))
            s['tilt_max'] = safe_int('tilt_max_input', getattr(self, 'TILT_MAX', 180))
            s['home_pan'] = safe_int('home_pan_input', getattr(self, 'HOME_PAN', 90))
            s['home_tilt'] = safe_int('home_tilt_input', getattr(self, 'HOME_TILT', 40))

            # Detection / YOLO
            try:
                s['detection_mode'] = getattr(self, 'detection_mode_combo', None) and self.detection_mode_combo.currentText() or ''
            except Exception:
                s['detection_mode'] = ''
            s['yolo_model'] = safe_text('yolo_model_combo', '')
            s['yolo_confidence'] = safe_float('yolo_confidence_input', 0.5)
            s['yolo_classes'] = safe_text('yolo_classes_input', '')

            # Behavior tuning
            try:
                s['tracking_speed'] = getattr(self, 'tracking_speed_slider', None) and int(self.tracking_speed_slider.value()) or safe_int('tracking_speed_slider', 40)
            except Exception:
                s['tracking_speed'] = safe_int('tracking_speed_slider', 40)
            try:
                s['movement_sensitivity'] = getattr(self, 'movement_sensitivity_slider', None) and int(self.movement_sensitivity_slider.value()) or safe_int('movement_sensitivity_slider', 25)
            except Exception:
                s['movement_sensitivity'] = safe_int('movement_sensitivity_slider', 25)
            s['smoothing'] = safe_float('smoothing_input', 0.95)
            s['snap_threshold'] = safe_int('snap_threshold_slider', 80)
            s['deadzone'] = safe_int('deadzone_slider', 20)
            s['overshoot_percent'] = safe_int('overshoot_input', 0)
            s['hold_seconds'] = safe_float('lost_hold_input', getattr(self, 'lost_hold_seconds', 5.0))
            s['hold_infinite'] = bool(getattr(self, 'hold_infinite', False))

            # Manual & rapid-fire
            s['rapid_fire_enabled'] = bool(getattr(self, 'rapid_fire_enabled', False))
            s['rapid_fire_rate_hz'] = int(getattr(self, 'rapid_fire_rate_hz', getattr(getattr(self, 'rapid_fire_rate_spin', None), 'value', 1) if getattr(self, 'rapid_fire_rate_spin', None) else 1))
            s['rapid_fire_duty'] = float(getattr(self, 'rapid_fire_duty', 0.5))

            # Config
            try:
                s['com_port'] = getattr(self, 'com_port_input', None) and (self.com_port_input.text() or '') or ''
            except Exception:
                s['com_port'] = ''
            try:
                s['baud_rate'] = getattr(self, 'baud_rate_input', None) and int(self.baud_rate_input.value()) or 115200
            except Exception:
                s['baud_rate'] = 115200

            # UI and misc
            s['invert_pan'] = bool(getattr(getattr(self, 'invert_pan_checkbox', None), 'isChecked', lambda: False)())
            s['invert_tilt'] = bool(getattr(getattr(self, 'invert_tilt_checkbox', None), 'isChecked', lambda: False)())
            s['flip_image'] = bool(getattr(getattr(self, 'flip_checkbox', None), 'isChecked', lambda: False)())
            s['manual_speed'] = safe_int('manual_speed_slider', 50)
            s['step_size'] = safe_int('step_size_input', self.STEP_INCREMENT)

            # Preserve any additional flags the app keeps on self
            s['auto_tracking'] = getattr(self, 'auto_tracking_enabled', False)
            s['detection_enabled'] = getattr(self, 'detection_enabled', False)

        except Exception:
            # Best-effort: return whatever we collected
            pass
        return s

    def _apply_preset_to_ui(self, preset: dict):
        """Apply a preset dict to UI widgets where possible."""
        try:
            if not isinstance(preset, dict):
                return

            def try_set(widget_name, val):
                try:
                    w = getattr(self, widget_name, None)
                    if w is None:
                        return
                    if hasattr(w, 'setValue'):
                        try:
                            w.setValue(val)
                            return
                        except Exception:
                            pass
                    if hasattr(w, 'setText'):
                        try:
                            w.setText(str(val))
                            return
                        except Exception:
                            pass
                except Exception:
                    pass

            # Servo/home
            for key in ('pan_min','pan_max','tilt_min','tilt_max','home_pan','home_tilt'):
                if key in preset:
                    try_set(key + '_input', preset[key])

            # Detection
            if 'detection_mode' in preset and getattr(self, 'detection_mode_combo', None):
                try:
                    txt = str(preset.get('detection_mode',''))
                    idx = self.detection_mode_combo.findText(txt)
                    if idx != -1:
                        self.detection_mode_combo.setCurrentIndex(idx)
                except Exception:
                    pass

            for key in ('threshold','blur_kernel','dilate_iter','min_contour'):
                if key in preset:
                    try_set(key + '_input', preset[key])

            # YOLO
            if 'yolo_model' in preset and getattr(self, 'yolo_model_combo', None):
                try:
                    model = str(preset['yolo_model'])
                    if self.yolo_model_combo.findText(model) == -1:
                        try:
                            self.yolo_model_combo.addItem(model)
                        except Exception:
                            pass
                    try:
                        self.yolo_model_combo.setCurrentText(model)
                    except Exception as e:
                        if logger: log_exception(e, "Setting yolo_model_combo text")
                except Exception as e:
                    if logger: log_exception(e, "Loading YOLO model from preset")
            if 'yolo_confidence' in preset and getattr(self, 'yolo_confidence_input', None):
                try: 
                    self.yolo_confidence_input.setValue(float(preset['yolo_confidence']))
                except Exception as e:
                    if logger: log_exception(e, "Setting yolo_confidence from preset")
            if 'yolo_classes' in preset and getattr(self, 'yolo_classes_input', None):
                try: 
                    self.yolo_classes_input.setText(str(preset['yolo_classes']))
                except Exception as e:
                    if logger: log_exception(e, "Setting yolo_classes from preset")

            # Behavior/others - FIXED: explicit slider mapping (critical fix)
            if 'tracking_speed' in preset:
                try_set('tracking_speed_slider', int(preset['tracking_speed']))
            if 'movement_sensitivity' in preset:
                try_set('movement_sensitivity_slider', int(preset['movement_sensitivity']))
            if 'snap_threshold' in preset:
                try_set('snap_threshold_slider', int(preset['snap_threshold']))
            if 'deadzone' in preset:
                try_set('deadzone_slider', int(preset['deadzone']))
            
            # CRITICAL FIX: smoothing_factor (preset key) -> smoothing_input (widget name)
            if 'smoothing_factor' in preset:
                try_set('smoothing_input', float(preset['smoothing_factor']))
            elif 'smoothing' in preset:
                try_set('smoothing_input', float(preset['smoothing']))
            
            for key in ('overshoot_percent','hold_seconds'):
                if key in preset:
                    try:
                        try_set(key + '_input', preset[key])
                    except Exception:
                        pass

            if 'rapid_fire_enabled' in preset:
                try:
                    self.rapid_fire_enabled = bool(preset['rapid_fire_enabled'])
                    if getattr(self, 'rapid_fire_enable_checkbox', None):
                        try: 
                            self.rapid_fire_enable_checkbox.setChecked(self.rapid_fire_enabled)
                        except Exception as e:
                            if logger: log_exception(e, "Setting rapid_fire checkbox")
                except Exception as e:
                    if logger: log_exception(e, "Setting rapid_fire_enabled from preset")

            # --- Aim Aggression Settings (DEC 2024) ---
            if 'aim_aggression' in preset:
                try:
                    self.aim_aggression = int(preset['aim_aggression'])
                    if getattr(self, 'aim_aggression_slider', None):
                        self.aim_aggression_slider.setValue(self.aim_aggression)
                    if getattr(self, 'aim_aggression_label', None):
                        self.aim_aggression_label.setText(str(self.aim_aggression))
                except Exception as e:
                    if logger: log_exception(e, "Setting aim_aggression from preset")

            if 'final_approach_boost' in preset:
                try:
                    self.final_approach_boost = bool(preset['final_approach_boost'])
                    if getattr(self, 'final_approach_boost_checkbox', None):
                        self.final_approach_boost_checkbox.setChecked(self.final_approach_boost)
                except Exception as e:
                    if logger: log_exception(e, "Setting final_approach_boost from preset")

            if 'com_port' in preset and getattr(self, 'com_port_input', None):
                try: 
                    self.com_port_input.setText(str(preset['com_port']))
                except Exception as e:
                    if logger: log_exception(e, "Setting COM port from preset")
            if 'baud_rate' in preset and getattr(self, 'baud_rate_input', None):
                try: 
                    self.baud_rate_input.setValue(int(preset['baud_rate']))
                except Exception as e:
                    if logger: log_exception(e, "Setting baud rate from preset")
            if 'sound_enabled' in preset and getattr(self, 'sound_checkbox', None):
                try: 
                    self.sound_checkbox.setChecked(bool(preset['sound_enabled']))
                except Exception as e:
                    if logger: log_exception(e, "Setting sound_enabled from preset")

            # After setting widget values, try to update any dependent UI
            try:
                self._update_ui_from_settings()
            except Exception as e:
                if logger: log_exception(e, "Updating UI from settings after preset load")

        except Exception:
            pass

    def _ensure_tracking_controls_attached(self):
        """Ensure the tracking-related widgets are present in the behavior layout.

        This is defensive: if the centralized create_behavior_tracking_panel()
        failed to parent the tracking controls, this will gather the existing
        widget instances (sliders, spinboxes, labels, checkboxes) and place
        them into a small grouped container inside the `behavior_layout` so
        the Tracking Behavior dock is never empty.
        """
        try:
            bg = getattr(self, 'behavior_group', None)
            bl = getattr(self, 'behavior_layout', None)
            if bg is None or bl is None:
                return

            # Quick presence check: if any of the main widgets is already
            # present in the behavior_layout, assume everything is fine.
            def widget_in_layout(w):
                try:
                    if w is None:
                        return False
                    for i in range(bl.count()):
                        it = bl.itemAt(i)
                        try:
                            if getattr(it, 'widget', None) and it.widget() is w:
                                return True
                        except Exception:
                            pass
                    return False
                except Exception:
                    return False

            key_widgets = [
                getattr(self, 'tracking_speed_slider', None),
                getattr(self, 'movement_sensitivity_slider', None),
                getattr(self, 'smoothing_input', None),
            ]
            for w in key_widgets:
                if w is not None and widget_in_layout(w):
                    return  # already present

            # Not present — build a small container and add known widgets into it.
            try:
                # Parent the restored tracking container to the main
                # behavior_group so the C++ object has a stable owner.
                tg = QGroupBox("Tracking Controls (restored)", bg)
            except Exception:
                try:
                    tg = QGroupBox("Tracking Controls", bg)
                except Exception:
                    tg = None

            if tg is None:
                return

            try:
                tlay = QGridLayout()
            except Exception:
                tlay = None

            if tlay is None:
                return

            row = 0
            try:
                # Tracking Speed
                try:
                    tlay.addWidget(QLabel("Tracking Speed"), row, 0)
                    speed_row = QHBoxLayout()
                    try:
                        if getattr(self, 'tracking_speed_slider', None) is not None:
                            speed_row.addWidget(self.tracking_speed_slider)
                    except Exception:
                        pass
                    try:
                        if getattr(self, 'tracking_speed_label', None) is not None:
                            speed_row.addWidget(self.tracking_speed_label)
                    except Exception:
                        pass
                    tlay.addLayout(speed_row, row, 1)
                    row += 1
                except Exception:
                    pass

                # Movement Sensitivity
                try:
                    tlay.addWidget(QLabel("Movement Sensitivity"), row, 0)
                    ms_row = QHBoxLayout()
                    try:
                        if getattr(self, 'movement_sensitivity_slider', None) is not None:
                            ms_row.addWidget(self.movement_sensitivity_slider)
                    except Exception:
                        pass
                    try:
                        if getattr(self, 'movement_sensitivity_label', None) is not None:
                            ms_row.addWidget(self.movement_sensitivity_label)
                    except Exception:
                        pass
                    tlay.addLayout(ms_row, row, 1)
                    row += 1
                except Exception:
                    pass

                # Smoothing
                try:
                    tlay.addWidget(QLabel("Smoothing (0.0 - 1.0):"), row, 0)
                    if getattr(self, 'smoothing_input', None) is not None:
                        tlay.addWidget(self.smoothing_input, row, 1)
                    row += 1
                except Exception:
                    pass

                # Overshoot
                try:
                    tlay.addWidget(QLabel("Overshoot (%):"), row, 0)
                    if getattr(self, 'overshoot_input', None) is not None:
                        tlay.addWidget(self.overshoot_input, row, 1)
                    row += 1
                except Exception:
                    pass

                # Deadzone
                try:
                    tlay.addWidget(QLabel("Deadzone (pixels)"), row, 0)
                    dz_row = QHBoxLayout()
                    try:
                        if getattr(self, 'deadzone_slider', None) is not None:
                            dz_row.addWidget(self.deadzone_slider)
                    except Exception:
                        pass
                    try:
                        if getattr(self, 'deadzone_label', None) is not None:
                            dz_row.addWidget(self.deadzone_label)
                    except Exception:
                        pass
                    tlay.addLayout(dz_row, row, 1)
                    row += 1
                except Exception:
                    pass

                # Snap Threshold
                try:
                    tlay.addWidget(QLabel("Snap Threshold (px)"), row, 0)
                    st_row = QHBoxLayout()
                    try:
                        if getattr(self, 'snap_threshold_slider', None) is not None:
                            st_row.addWidget(self.snap_threshold_slider)
                    except Exception:
                        pass
                    try:
                        if getattr(self, 'snap_threshold_label', None) is not None:
                            st_row.addWidget(self.snap_threshold_label)
                    except Exception:
                        pass
                    tlay.addLayout(st_row, row, 1)
                    row += 1
                except Exception:
                    pass

                # Hold on loss
                try:
                    tlay.addWidget(QLabel("Hold target on loss (s):"), row, 0)
                    if getattr(self, 'lost_hold_input', None) is not None:
                        tlay.addWidget(self.lost_hold_input, row, 1)
                    row += 1
                except Exception:
                    pass

                # Checkboxes (invert, flip, hold infinite)
                try:
                    if getattr(self, 'hold_infinite_checkbox', None) is not None:
                        tlay.addWidget(self.hold_infinite_checkbox, row, 0, 1, 2)
                        row += 1
                except Exception:
                    pass
                try:
                    if getattr(self, 'invert_pan_checkbox', None) is not None:
                        tlay.addWidget(self.invert_pan_checkbox, row, 0, 1, 2)
                        row += 1
                except Exception:
                    pass
                try:
                    if getattr(self, 'invert_tilt_checkbox', None) is not None:
                        tlay.addWidget(self.invert_tilt_checkbox, row, 0, 1, 2)
                        row += 1
                except Exception:
                    pass
                try:
                    if getattr(self, 'flip_checkbox', None) is not None:
                        tlay.addWidget(self.flip_checkbox, row, 0, 1, 2)
                        row += 1
                except Exception:
                    pass

                # Preset combo
                try:
                    tlay.addWidget(QLabel('Preset:'), row, 0)
                    if getattr(self, 'preset_combo', None) is not None:
                        tlay.addWidget(self.preset_combo, row, 1)
                        row += 1
                except Exception:
                    pass

            except Exception:
                pass

            try:
                tg.setLayout(tlay)
            except Exception:
                pass

            try:
                # Add to behavior layout at the next free row
                br = getattr(self, '_behavior_row_counter', 0) or 0
                try:
                    bl.addWidget(tg, br, 0, 1, 2)
                except Exception:
                    try:
                        bl.addWidget(tg)
                    except Exception:
                        pass
                try:
                    self._behavior_row_counter = br + 1
                except Exception:
                    pass
            except Exception:
                pass

            try:
                # Try logging to enhancer or stdout to help debugging
                try:
                    self.enhancer.log_serial_output("Tracking controls restored into Behavior panel", fire=False)
                except Exception:
                    try:
                        print("Tracking controls restored into Behavior panel")
                    except Exception:
                        pass
            except Exception:
                pass

        except Exception:
            pass

    def save_behavior_preset(self, name=None):
        """Save current settings as a named behavior preset."""
        try:
            # Determine name from input or selection
            if not name:
                try:
                    if getattr(self, "preset_name_input", None) is not None:
                        name = str(self.preset_name_input.text()).strip()
                except Exception:
                    name = ""

            if not name:
                try:
                    if (
                        getattr(self, "preset_list", None) is not None
                        and getattr(self.preset_list, "currentItem", None)
                    ):
                        ci = self.preset_list.currentItem()
                        try:
                            name = ci.text()
                        except Exception:
                            name = str(ci)
                except Exception:
                    # ignore selection-read errors and continue
                    pass

            if not name:
                try:
                    self.enhancer.log_serial_output(
                        "Please enter a preset name to save.", fire=False
                    )
                except Exception:
                    pass
                return

            # Collect current settings. Prefer a centralized gatherer if present
            try:
                if hasattr(self, "_gather_current_settings"):
                    settings = self._gather_current_settings()
                else:
                    # Fallback: collect a minimal set
                    settings = {
                        "tracking_enabled": getattr(self, "tracking_enabled", False),
                        "guarding_mode": getattr(self, "guarding_mode", False),
                        "movement_detection": getattr(self, "movement_detection_enabled", False),
                        "aim_mode": getattr(self, "aim_mode", "center"),
                        "detection_threshold": getattr(self, "detection_threshold", 0.5),
                        "trigger_threshold": getattr(self, "trigger_threshold", 0.7),
                        "rapid_fire": getattr(self, "rapid_fire_enabled", False),
                        "fire_mode": getattr(self, "fire_mode", "single"),
                        "safe_zones": getattr(self, "safe_zones", []).copy(),
                        "tracking_bounds": getattr(self, "tracking_bounds", None),
                        "sensitivity": getattr(self, "sensitivity", 1.0),
                        "aim_point": getattr(self, "aim_point", "center"),
                    }
            except Exception:
                settings = {}

            # Save preset
            if getattr(self, "behavior_presets", None) is not None:
                self.behavior_presets.add_preset(name, settings)
                try:
                    self.enhancer.log_serial_output(
                        f"Behavior preset '{name}' saved.", fire=False
                    )
                except Exception:
                    pass

                # Clear input
                try:
                    if getattr(self, "preset_name_input", None) is not None:
                        self.preset_name_input.clear()
                except Exception:
                    pass

                # Refresh preset list
                try:
                    self._refresh_preset_list()
                except Exception:
                    pass
            else:
                try:
                    self.enhancer.log_serial_output(
                        "Error: Behavior presets manager not initialized", fire=False
                    )
                except Exception:
                    pass

        except Exception as e:
            try:
                self.enhancer.log_serial_output(
                    f"Error saving behavior preset: {e}", fire=False
                )
            except Exception:
                pass

    def _refresh_preset_list(self):
        """Refresh the list of saved behavior presets (user presets only)."""
        try:
            if getattr(self, "preset_list", None) is None:
                return

            # Clear existing entries
            try:
                if hasattr(self.preset_list, "clear"):
                    self.preset_list.clear()
            except Exception:
                pass

            # Only add user-saved presets (factory presets are removed)
            try:
                if getattr(self, "behavior_presets", None) is not None:
                    user_presets = self.behavior_presets.list_presets()
                    for pname in user_presets:
                        try:
                            self.preset_list.addItem(pname)
                            try:
                                it = self.preset_list.item(self.preset_list.count() - 1)
                                try:
                                    it.setData(Qt.UserRole, "user")
                                except Exception:
                                    pass
                            except Exception:
                                pass
                        except Exception:
                            pass
            except Exception:
                pass
        except Exception as e:
            try:
                self.enhancer.log_serial_output(f"Error refreshing preset list: {e}", fire=False)
            except Exception:
                pass
    def _update_ui_from_settings(self):
        """Update UI elements to reflect current settings after loading a preset."""
        try:
            # Update checkboxes
            for widget, attr in [
                ("tracking_checkbox", "tracking_enabled"),
                ("guarding_checkbox", "guarding_mode"),
                ("movement_detection_checkbox", "movement_detection_enabled"),
                ("rapid_fire_checkbox", "rapid_fire_enabled")
            ]:
                try:
                    if hasattr(self, widget):
                        getattr(self, widget).setChecked(getattr(self, attr, False))
                except Exception:
                    pass

            # Update sliders
            for widget, attr, scale in [
                ("detection_threshold_slider", "detection_threshold", 100),
                ("trigger_threshold_slider", "trigger_threshold", 100),
                ("sensitivity_slider", "sensitivity", 100)
            ]:
                try:
                    if hasattr(self, widget):
                        getattr(self, widget).setValue(int(getattr(self, attr, 0.5) * scale))
                except Exception:
                    pass

            # Update comboboxes
            for widget, attr in [
                ("aim_mode_combo", "aim_mode"),
                ("fire_mode_combo", "fire_mode")
            ]:
                try:
                    if hasattr(self, widget):
                        combo = getattr(self, widget)
                        value = getattr(self, attr, "")
                        index = combo.findText(value)
                        if index >= 0:
                            combo.setCurrentIndex(index)
                except Exception:
                    pass
        except Exception as e:
            try:
                self.enhancer.log_serial_output(
                    f"Error updating UI from settings: {e}", fire=False
                )
            except Exception:
                pass

    def load_behavior_preset(self, name: str = None):
        """Load a named behavior preset."""
        try:
            if not name:
                try:
                    if (
                        getattr(self, "preset_list", None) is not None
                        and getattr(self.preset_list, "currentItem", None)
                    ):
                        ci = self.preset_list.currentItem()
                        try:
                            name = ci.text()
                        except Exception:
                            name = str(ci)
                except Exception:
                    name = None

            if not name:
                try:
                    self.enhancer.log_serial_output(
                        "No preset selected to load.", fire=False
                    )
                except Exception:
                    pass
                return

            if getattr(self, "behavior_presets", None) is not None:
                try:
                    settings = self.behavior_presets.get_preset(name)
                    if settings:
                        # Apply settings via centralized applier if available
                        try:
                            if hasattr(self, "_apply_preset_to_ui"):
                                try:
                                    self._apply_preset_to_ui(settings)
                                except Exception:
                                    # fallback to piecemeal apply below
                                    raise
                            else:
                                # fallback: apply a few known attributes
                                self.tracking_enabled = settings.get("tracking_enabled", False)
                                self.guarding_mode = settings.get("guarding_mode", False)
                                self.movement_detection_enabled = settings.get("movement_detection", False)
                                self.aim_mode = settings.get("aim_mode", "center")
                                self.detection_threshold = settings.get("detection_threshold", 0.5)
                                self.trigger_threshold = settings.get("trigger_threshold", 0.7)
                                self.rapid_fire_enabled = settings.get("rapid_fire", False)
                                self.fire_mode = settings.get("fire_mode", "single")

                            # Also mirror a few container-style fields
                            if "safe_zones" in settings:
                                self.safe_zones = settings["safe_zones"].copy()
                            if "tracking_bounds" in settings and settings["tracking_bounds"]:
                                self.tracking_bounds = settings["tracking_bounds"].copy()

                            # Ensure UI reflects the applied settings
                            try:
                                self._update_ui_from_settings()
                            except Exception:
                                pass

                            try:
                                self.enhancer.log_serial_output(
                                    f"Behavior preset '{name}' loaded.", fire=False
                                )
                            except Exception:
                                pass
                        except Exception as e:
                            try:
                                self.enhancer.log_serial_output(
                                    f"Error applying preset settings: {e}", fire=False
                                )
                            except Exception:
                                pass
                    else:
                        try:
                            self.enhancer.log_serial_output(
                                f"Preset '{name}' not found.", fire=False
                            )
                        except Exception:
                            pass
                except Exception as e:
                    try:
                        self.enhancer.log_serial_output(
                            f"Error loading preset: {e}", fire=False
                        )
                    except Exception:
                        pass
            else:
                try:
                    self.enhancer.log_serial_output(
                        "Error: Behavior presets manager not initialized", fire=False
                    )
                except Exception:
                    pass
        except Exception as e:
            try:
                self.enhancer.log_serial_output(
                    f"Error loading preset: {e}", fire=False
                )
            except Exception:
                pass

    def delete_behavior_preset(self):
        """Delete the selected behavior preset."""
        try:
            name = None
            try:
                if (
                    getattr(self, "preset_list", None) is not None
                    and getattr(self.preset_list, "currentItem", None)
                ):
                    ci = self.preset_list.currentItem()
                    try:
                        name = ci.text()
                    except Exception:
                        name = str(ci)
            except Exception:
                pass

            if not name:
                try:
                    self.enhancer.log_serial_output(
                        "No preset selected to delete.", fire=False
                    )
                except Exception:
                    pass
                return
            # Prevent deletion of factory presets (they are read-only)
            try:
                ci = getattr(self.preset_list, 'currentItem', lambda: None)()
                if ci is not None:
                    try:
                        src = ci.data(Qt.UserRole)
                    except Exception:
                        src = None
                    if src == 'factory':
                        try:
                            self.enhancer.log_serial_output(
                                f"Cannot delete built-in preset '{name}'.", fire=False
                            )
                        except Exception:
                            pass
                        return
            except Exception:
                pass

            if getattr(self, "behavior_presets", None) is not None:
                try:
                    ok = self.behavior_presets.delete_preset(name)
                    if ok:
                        try:
                            self.enhancer.log_serial_output(
                                f"Behavior preset '{name}' deleted.", fire=False
                            )
                        except Exception:
                            pass
                    else:
                        try:
                            self.enhancer.log_serial_output(
                                f"Preset '{name}' not found in user presets.", fire=False
                            )
                        except Exception:
                            pass
                    try:
                        self._refresh_preset_list()
                    except Exception:
                        pass
                except Exception as e:
                    try:
                        self.enhancer.log_serial_output(
                            f"Error deleting preset: {e}", fire=False
                        )
                    except Exception:
                        pass
            else:
                try:
                    self.enhancer.log_serial_output(
                        "Error: Behavior presets manager not initialized", fire=False
                    )
                except Exception:
                    pass
        except Exception:
            pass

    def delete_layout_profile(self):
        """Delete the currently selected or named layout profile."""
        try:
            name = ""
            try:
                if (
                    getattr(self, "layout_list", None) is not None
                    and getattr(self.layout_list, "currentItem", None)
                ):
                    ci = self.layout_list.currentItem()
                    try:
                        name = ci.text()
                    except Exception:
                        name = str(ci)
            except Exception:
                pass

            if not name:
                try:
                    if getattr(self, "layout_name_input", None) is not None:
                        name = str(self.layout_name_input.text()).strip()
                except Exception:
                    name = ""

            if not name:
                try:
                    self.enhancer.log_serial_output(
                        "No layout selected to delete.", fire=False
                    )
                except Exception:
                    pass
                return

            s = {}
            try:
                if os.path.exists(self.SETTINGS_FILE):
                    with open(self.SETTINGS_FILE, "r") as f:
                        s = json.load(f) or {}
            except Exception:
                s = s or {}

            try:
                layouts = s.get("layouts", {}) if isinstance(s, dict) else {}
                if name in layouts:
                    try:
                        del layouts[name]
                        s["layouts"] = layouts
                        with open(self.SETTINGS_FILE, "w") as f:
                            json.dump(s, f, indent=4)
                        try:
                            self.enhancer.log_serial_output(
                                f"Layout profile '{name}' deleted.", fire=False
                            )
                        except Exception:
                            pass
                    except Exception as e:
                        try:
                            self.enhancer.log_serial_output(
                                f"Error deleting layout profile: {e}", fire=False
                            )
                        except Exception:
                            pass
            except Exception:
                pass

            try:
                self._refresh_layout_list()
            except Exception:
                pass
        except Exception:
            pass

    def save_preferred_defaults(self):
        """Save the current UI settings as the user's preferred defaults."""
        try:
            settings = {
                "invert_pan": getattr(
                    self.invert_pan_checkbox, "isChecked", lambda: True
                )(),
                "invert_tilt": getattr(
                    self.invert_tilt_checkbox, "isChecked", lambda: True
                )(),
                "flip_image": getattr(self.flip_checkbox, "isChecked", lambda: True)(),
                "detection_mode_index": getattr(
                    self.detection_mode_combo, "currentIndex", lambda: 1
                )(),
                "smoothing_factor": getattr(
                    self.smoothing_input, "value", lambda: 0.95
                )(),
                "movement_sensitivity": getattr(
                    self.movement_sensitivity_slider, "value", lambda: 25
                )(),
                "deadzone": getattr(self.deadzone_slider, "value", lambda: 20)(),
                "snap_threshold": getattr(
                    self.snap_threshold_slider, "value", lambda: 80
                )(),
                "tracking_speed": getattr(
                    self.tracking_speed_slider, "value", lambda: 40
                )(),
                # Add COM and relay defaults
                "com_port": getattr(self.com_port_input, "text", lambda: "COM3")(),
                "baud_rate": getattr(self.baud_rate_input, "value", lambda: 115200)(),
                "relay1": getattr(self.relay1_button, "isChecked", lambda: False)(),
                "relay2": getattr(self.relay2_button, "isChecked", lambda: False)(),
                "safety_lock": getattr(self.safety_button, "isChecked", lambda: True)(),
                # YOLO tuning defaults
                "yolo_confidence": getattr(
                    self.yolo_confidence_input, "value", lambda: 0.5
                )(),
                "yolo_classes": getattr(
                    self.yolo_classes_input, "text", lambda: "person"
                )(),
                "yolo_max_results": getattr(
                    self, "yolo_max_results_input", lambda: 0
                )(),
                "yolo_min_area": getattr(self, "yolo_min_area_input", lambda: 0)(),
            }
            preferred_path = self.PREFERRED_FILE
            try:
                with open(preferred_path, "w") as f:
                    json.dump(settings, f, indent=4)
            except Exception:
                pass
            self.enhancer.log_serial_output("Preferred defaults saved.", fire=False)
        except Exception as e:
            self.enhancer.log_serial_output(
                f"Error saving preferred defaults: {e}", fire=False
            )

    def save_current_as_default(self):
        """Callback for UI button: save the current UI settings as preferred defaults
        and persist them immediately to settings.json so the next app run will use
        these values as the defaults.
        """
        try:
            # Persist preferred_defaults.json (human-readable file)
            try:
                self.save_preferred_defaults()
            except Exception:
                pass

            # Also update settings.json so next run reads these values directly
            try:
                self.save_settings()
            except Exception:
                pass

            try:
                self.enhancer.log_serial_output(
                    "Current settings saved as defaults and persisted to settings.json",
                    fire=False,
                )
            except Exception:
                pass
        except Exception as e:
            try:
                self.enhancer.log_serial_output(
                    f"Error saving current settings as defaults: {e}", fire=False
                )
            except Exception:
                pass

    def _pulse_fire_indicator(self, pulse_ms: int = 400, confirmed: bool = False):
        """Visual pulse for the on-screen fire indicator. Non-blocking.
        pulse_ms: base pulse duration in milliseconds
        confirmed: if True, extend pulse to emphasize MCU confirmation
        """
        try:
            # Prefer the TurretEnhancements top-bar indicator if available
            enh = getattr(self, "enhancer", None)
            if enh is not None and hasattr(enh, "pulse_fire_indicator"):
                try:
                    enh.pulse_fire_indicator(pulse_ms=pulse_ms, confirmed=confirmed)
                    return
                except Exception:
                    pass

            # Fallback: if a local indicator exists, use it (legacy)
            ind = getattr(self, "fire_indicator", None)
            if ind is None:
                return
            # Respect the Safety state: do not show the indicator when Safety is LOCKED
            try:
                if getattr(self, "safety_state", 1) != 0:
                    return
            except Exception:
                pass
            dur = int(pulse_ms if not confirmed else max(pulse_ms, 1000))
            try:
                ind.setStyleSheet(
                    "background: red; border: 1px solid #400; border-radius: 7px;"
                )
            except Exception:
                pass

            # restore after dur milliseconds
            try:

                def _restore():
                    try:
                        ind.setStyleSheet(
                            "background: lightgray; border: 1px solid #222; border-radius: 7px;"
                        )
                    except Exception:
                        pass

                QTimer.singleShot(dur, _restore)
            except Exception:
                pass
        except Exception:
            pass

    def load_preferred_defaults_action(self):
        """Load preferred defaults (if present) into the UI and persist to settings.json."""
        try:
            preferred_path = self.PREFERRED_FILE
            if not os.path.exists(preferred_path):
                self.enhancer.log_serial_output(
                    "No preferred defaults file found.", fire=False
                )
                return
            with open(preferred_path, "r") as f:
                prefs = json.load(f)
            # Apply a safe set of keys
            try:
                if "invert_pan" in prefs:
                    self.invert_pan_checkbox.setChecked(bool(prefs["invert_pan"]))
                if "invert_tilt" in prefs:
                    self.invert_tilt_checkbox.setChecked(bool(prefs["invert_tilt"]))
                if "flip_image" in prefs:
                    self.flip_checkbox.setChecked(bool(prefs["flip_image"]))
                if "detection_mode_index" in prefs:
                    try:
                        self._safe_widget_call(
                            "detection_mode_combo",
                            "setCurrentIndex",
                            int(prefs["detection_mode_index"]),
                        )
                    except Exception:
                        pass
                if "smoothing_factor" in prefs:
                    try:
                        self._safe_widget_call(
                            "smoothing_input",
                            "setValue",
                            float(prefs["smoothing_factor"]),
                        )
                    except Exception:
                        pass
                if "movement_sensitivity" in prefs:
                    try:
                        self._safe_widget_call(
                            "movement_sensitivity_slider",
                            "setValue",
                            int(prefs["movement_sensitivity"]),
                        )
                    except Exception:
                        pass
                if "deadzone" in prefs:
                    try:
                        self._safe_widget_call(
                            "deadzone_slider", "setValue", int(prefs["deadzone"])
                        )
                    except Exception:
                        pass
                if "snap_threshold" in prefs:
                    try:
                        self._safe_widget_call(
                            "snap_threshold_slider",
                            "setValue",
                            int(prefs["snap_threshold"]),
                        )
                    except Exception:
                        pass
                if "tracking_speed" in prefs:
                    try:
                        self._safe_widget_call(
                            "tracking_speed_slider",
                            "setValue",
                            int(prefs["tracking_speed"]),
                        )
                    except Exception:
                        pass
                # YOLO preferences
                if "yolo_confidence" in prefs:
                    try:
                        if getattr(self, "yolo_confidence_input", None) is not None:
                            self.yolo_confidence_input.setValue(
                                float(prefs["yolo_confidence"])
                            )
                    except Exception:
                        pass
                if "yolo_classes" in prefs:
                    try:
                        if getattr(self, "yolo_classes_input", None) is not None:
                            self.yolo_classes_input.setText(str(prefs["yolo_classes"]))
                            try:
                                if getattr(self, "yolo_detector", None) is not None:
                                    self.yolo_detector.set_target_classes(
                                        prefs["yolo_classes"]
                                    )
                            except Exception:
                                pass
                    except Exception:
                        pass
                if "yolo_max_results" in prefs:
                    try:
                        if getattr(self, "yolo_max_results_input", None) is not None:
                            self.yolo_max_results_input.setValue(
                                int(prefs["yolo_max_results"])
                            )
                    except Exception:
                        pass
                if "yolo_min_area" in prefs:
                    try:
                        if getattr(self, "yolo_min_area_input", None) is not None:
                            self.yolo_min_area_input.setValue(
                                int(prefs["yolo_min_area"])
                            )
                    except Exception:
                        pass
                if "home_return_mode" in prefs:
                    try:
                        mode = str(prefs["home_return_mode"])
                        if getattr(self, "home_return_mode_combo", None) is not None:
                            try:
                                idx = self.home_return_mode_combo.findText(mode)
                                if idx != -1:
                                    self.home_return_mode_combo.setCurrentIndex(idx)
                                else:
                                    # fall back to attribute
                                    self.home_return_mode = mode
                            except Exception:
                                pass
                    except Exception:
                        pass
                if "home_move_suspend_seconds" in prefs:
                    try:
                        sec = float(prefs["home_move_suspend_seconds"])
                        self.home_move_suspend_seconds = sec
                        try:
                            if (
                                getattr(self, "home_return_suspend_input", None)
                                is not None
                            ):
                                self.home_return_suspend_input.setValue(sec)
                        except Exception:
                            pass
                    except Exception:
                        pass
                # Apply COM/relay defaults if present
                if "com_port" in prefs:
                    try:
                        self._safe_widget_call(
                            "com_port_input", "setText", str(prefs["com_port"])
                        )
                    except Exception:
                        pass
                if "baud_rate" in prefs:
                    try:
                        self._safe_widget_call(
                            "baud_rate_input", "setValue", int(prefs["baud_rate"])
                        )
                    except Exception:
                        pass
                if "relay1" in prefs:
                    try:
                        self.relay1_button.setChecked(bool(prefs["relay1"]))
                        self.relay1_state = 1 if prefs["relay1"] else 0
                        self.relay1_button.setText(
                            "LED (Relay1): ON"
                            if prefs["relay1"]
                            else "LED (Relay1): OFF"
                        )
                    except Exception:
                        pass
                if "relay2" in prefs:
                    try:
                        self.relay2_button.setChecked(bool(prefs["relay2"]))
                        self.relay2_state = 1 if prefs["relay2"] else 0
                        self.relay2_button.setText(
                            "LASER (Relay2): ON"
                            if prefs["relay2"]
                            else "LASER (Relay2): OFF"
                        )
                    except Exception:
                        pass
                if "safety_lock" in prefs:
                    try:
                        locked = bool(prefs["safety_lock"])
                        # prefs store True => LOCKED. Button checked means ARMED, so invert
                        try:
                            self.safety_button.setChecked(False if locked else True)
                        except Exception:
                            pass
                        self.safety_state = 1 if locked else 0
                        self.safety_button.setText(
                            "Safety: LOCKED (No Fire)"
                            if locked
                            else "Safety: ARMED (Can Fire)"
                        )
                    except Exception:
                        pass
            except Exception:
                pass
            # If preferred defaults include a saved window/dock layout, apply it now
            try:
                if "window_state" in prefs and isinstance(
                    prefs.get("window_state"), str
                ):
                    try:
                        raw = base64.b64decode(prefs.get("window_state"))
                        self.restoreState(QByteArray(raw))
                    except Exception:
                        pass
                if "window_geometry" in prefs and isinstance(
                    prefs.get("window_geometry"), str
                ):
                    try:
                        rawg = base64.b64decode(prefs.get("window_geometry"))
                        self.restoreGeometry(QByteArray(rawg))
                    except Exception:
                        pass
                # re-equalize dock widths after restoring geometry/state
                try:
                    QTimer.singleShot(200, lambda: self.equalize_dock_columns())
                except Exception:
                    try:
                        self.equalize_dock_columns()
                    except Exception:
                        pass
                # If user explicitly saved a sniper floating preference, reapply it now
                try:
                    sniper_pref = prefs.get("sniper_floating", None)
                    if sniper_pref is not None:
                        try:
                            sniper_dock = getattr(self, "sniper_dock", None)
                            if sniper_dock is None:
                                # try to find by objectName used by add_dock
                                try:
                                    sniper_dock = self.findChild(
                                        QDockWidget, "SniperScopeDock"
                                    )
                                except Exception:
                                    sniper_dock = getattr(self, "sniper_dock", None)
                            if sniper_dock is not None:
                                try:
                                    sniper_dock.setFloating(bool(sniper_pref))
                                    # ensure reasonable size for floating sniper
                                    if bool(sniper_pref):
                                        try:
                                            sniper_dock.resize(360, 180)
                                        except Exception:
                                            pass
                                except Exception:
                                    pass
                        except Exception:
                            pass
                except Exception:
                    pass
            except Exception:
                pass
            # Persist these preferences into settings.json so they become active defaults
            try:
                self.save_settings()
                self.enhancer.log_serial_output(
                    "Preferred defaults applied and saved to settings.json", fire=False
                )
            except Exception:
                self.enhancer.log_serial_output(
                    "Error persisting preferred defaults.", fire=False
                )

        except Exception as e:
            self.enhancer.log_serial_output(
                f"Error loading preferred defaults: {e}", fire=False
            )
            pass

    def apply_preset(self, index: int):
        """Apply preset settings from turret_presets.py - INCLUDES ALL DETECTION SETTINGS"""
        try:
            preset_names = list(PRESETS.keys())
            if index < 0 or index >= len(preset_names):
                return

            name = preset_names[index]
            preset = PRESETS[name]

            # Apply only defined fields (skip blanks)
            if not preset:
                self.enhancer.log_serial_output(
                    f"Preset '{name}' is empty — skipping.", fire=False
                )
                return

            # ========== TRACKING BEHAVIOR SETTINGS ==========
            if "tracking_speed" in preset:
                self.tracking_speed_slider.setValue(int(preset["tracking_speed"]))
            if "movement_sensitivity" in preset:
                self.movement_sensitivity_slider.setValue(
                    int(preset["movement_sensitivity"])
                )
            if "smoothing_factor" in preset:
                self.smoothing_input.setValue(float(preset["smoothing_factor"]))
            if "deadzone" in preset:
                self.deadzone_slider.setValue(int(preset["deadzone"]))
            if "snap_threshold" in preset:
                self.snap_threshold_slider.setValue(int(preset["snap_threshold"]))

            # ========== MOTION DETECTION SETTINGS (CRITICAL FIX - WAS MISSING!) ==========
            # These were being completely ignored! Now they apply from presets
            if "threshold" in preset:
                try:
                    self.threshold_input.setValue(int(preset["threshold"]))
                except Exception:
                    pass
            if "blur_kernel" in preset:
                try:
                    self.blur_kernel_input.setValue(int(preset["blur_kernel"]))
                except Exception:
                    pass
            if "dilate_iter" in preset:
                try:
                    self.dilate_iter_input.setValue(int(preset["dilate_iter"]))
                except Exception:
                    pass
            if "min_contour" in preset:
                try:
                    self.min_contour_input.setValue(int(preset["min_contour"]))
                except Exception:
                    pass

            # ========== DETECTION MODE ==========
            if "detection_mode" in preset:
                try:
                    txt = str(preset.get("detection_mode", ""))
                    idx = self.detection_mode_combo.findText(txt)
                    if idx != -1:
                        self.detection_mode_combo.setCurrentIndex(idx)
                except Exception:
                    pass

            # ========== YOLO DETECTION PARAMETERS ==========
            if "yolo_confidence" in preset:
                self.yolo_confidence_input.setValue(float(preset["yolo_confidence"]))
            if "yolo_classes" in preset:
                self.yolo_classes_input.setText(str(preset["yolo_classes"]))
            if "yolo_model" in preset:
                idx = self.yolo_model_combo.findText(preset["yolo_model"])
                if idx != -1:
                    self.yolo_model_combo.setCurrentIndex(idx)

            # Persist settings
            self.save_settings()
            self.enhancer.log_serial_output(f"Applied preset: {name}", fire=False)

        except Exception as e:
            if hasattr(self, "enhancer"):
                self.enhancer.log_serial_output(
                    f"Error applying preset: {e}", fire=False
                )
            else:
                print(f"Error applying preset: {e}")

    def reset_layout(self):
        """Reset saved collapsible layout by removing 'sections' from settings.json
        and reverting all registered headers to their default (checked=True).
        """
        try:
            # Attempt to remove 'sections' from settings file
            settings_path = self.SETTINGS_FILE
            if os.path.exists(settings_path):
                try:
                    with open(settings_path, "r") as f:
                        s = json.load(f)
                except Exception:
                    s = {}
                if isinstance(s, dict) and "sections" in s:
                    try:
                        s.pop("sections", None)
                        try:
                            with open(settings_path, "w") as f:
                                json.dump(s, f, indent=4)
                        except Exception:
                            pass
                    except Exception:
                        pass

            # Reset in-memory headers to default (checked=True)
            try:
                for k, hdr in getattr(self, "section_headers", {}).items():
                    try:
                        hdr.setChecked(True)
                    except Exception:
                        pass
            except Exception:
                pass

            self.enhancer.log_serial_output(
                "Layout reset: cleared saved section states.", fire=False
            )

            # Persist the reset state immediately
            try:
                self.save_settings()
            except Exception:
                pass
        except Exception as e:
            try:
                self.enhancer.log_serial_output(f"Reset layout failed: {e}", fire=False)
            except Exception:
                pass

    def _connect_serial_async(self, port, baud):
        """Background worker for serial connection with timeout protection.
        Runs in separate thread to prevent GUI freeze.
        Updates UI via thread-safe QTimer.singleShot() callback.
        
        BULLETPROOF FIX: Adds 5-second timeout to prevent hanging on unresponsive devices.
        """
        import threading
        import time
        
        def _do_connect():
            """Blocking connection work in background thread with timeout protection."""
            CONNECT_TIMEOUT = 5.0
            start_time = time.time()
            
            result = {
                'success': False,
                'port': port,
                'baud': baud,
                'error': None,
                'ser': None,
                'elapsed_time': 0
            }
            
            try:
                # Attempt to open serial connection
                result['ser'] = self._safe_open_serial(
                    port, baud, timeout=0.1, write_timeout=1
                )
                result['success'] = (result['ser'] is not None)
                if not result['success']:
                    result['error'] = "Failed to open port - device may not be responding"
            except Exception as e:
                result['success'] = False
                result['error'] = f"Connection error: {str(e)}"
                result['ser'] = None
            
            # Calculate elapsed time
            elapsed = time.time() - start_time
            result['elapsed_time'] = elapsed
            
            # Check if we exceeded timeout
            if elapsed > CONNECT_TIMEOUT:
                result['success'] = False
                result['error'] = f"Connection timeout - device not responding (took {elapsed:.1f}s)"
                if result['ser'] is not None:
                    try:
                        result['ser'].close()
                    except:
                        pass
                    result['ser'] = None
            
            # Provide helpful error hints
            if not result['success'] and result['error']:
                error_lower = result['error'].lower()
                if "access denied" in error_lower or "cannot open" in error_lower:
                    result['error'] += " [Port may be locked by another program]"
                elif "file not found" in error_lower or "no such device" in error_lower:
                    result['error'] += " [Check COM port and Arduino connection]"
                elif "timeout" in error_lower:
                    result['error'] += " [Try pressing RESET on Arduino]"
            
            # Marshal result back to main Qt thread
            def _update_ui():
                try:
                    self._handle_serial_connection_result(result)
                except Exception as e:
                    try:
                        self._safe_enhancer_log(f"[SERIAL] Callback error: {e}")
                    except:
                        print(f"[SERIAL] Callback error: {e}")
            
            # Prefer emitting a typed signal from the worker thread so
            # Qt/pyqt won't attempt to queue C++ Qt types (e.g. QTextCursor).
            # Fall back to the previous QTimer.singleShot approach if emit fails.
            try:
                self.serial_connect_result.emit(result)
            except Exception:
                try:
                    from PyQt5.QtCore import QTimer
                    QTimer.singleShot(0, _update_ui)
                except Exception:
                    _update_ui()
        
        # Start connection in background thread
        bg_thread = threading.Thread(target=_do_connect, daemon=True, name="SerialConnect")
        bg_thread.start()

    def _handle_serial_connection_result(self, result):
        """Handle serial connection result from background thread.
        Runs on main Qt thread so it's safe to update GUI.
        Provides clear error messages and status feedback.
        """
        self._serial_connection_in_progress = False
        
        if result['success'] and result['ser'] is not None:
            # ========== CONNECTION SUCCEEDED ==========
            self.ser = result['ser']
            elapsed = result.get('elapsed_time', 0)
            self._safe_enhancer_log(f"✓ Connected to {result['port']} @ {result['baud']} baud (took {elapsed:.2f}s)")
            
            # Update button
            try:
                if hasattr(self, 'connect_button') and self.connect_button is not None:
                    self.connect_button.setText("Disconnect")
                    self.connect_button.setEnabled(True)
                else:
                    self._safe_widget_call("connect_button", "setText", "Disconnect")
                    self._safe_widget_call("connect_button", "setEnabled", True)
            except Exception:
                pass
            
            # Update status label
            try:
                if hasattr(self, 'connection_status_label'):
                    self.connection_status_label.setText(
                        f"✓ Connected to {result['port']} @ {result['baud']} baud"
                    )
                    self.connection_status_label.setStyleSheet(
                        "color: #00FF00; background-color: #2d2d2d; padding: 4px; border-radius: 3px;"
                    )
            except Exception:
                pass
            
            # Update enhancer status
            try:
                if getattr(self, "enhancer", None):
                    self.enhancer.update_serial_status(True)
            except Exception:
                pass
        
        else:
            # ========== CONNECTION FAILED ==========
            error_msg = result.get('error', 'Unknown error')
            elapsed = result.get('elapsed_time', 0)
            self._safe_enhancer_log(f"✗ Connection FAILED: {error_msg}")
            
            # Update button
            try:
                if hasattr(self, 'connect_button') and self.connect_button is not None:
                    self.connect_button.setText("Connect")
                    self.connect_button.setEnabled(True)
                else:
                    self._safe_widget_call("connect_button", "setText", "Connect")
                    self._safe_widget_call("connect_button", "setEnabled", True)
            except Exception:
                pass
            
            # Update status label with error
            try:
                if hasattr(self, 'connection_status_label'):
                    self.connection_status_label.setText(f"✗ {error_msg}")
                    self.connection_status_label.setStyleSheet(
                        "color: #FF6666; background-color: #2d2d2d; padding: 4px; border-radius: 3px;"
                    )
            except Exception:
                pass
            
            # Close failed connection
            if result.get('ser') is not None:
                try:
                    result['ser'].close()
                except Exception:
                    pass

    def connect_serial(self):
        """Handle serial connect/disconnect. Uses async connection to prevent GUI freeze.
        
        Connection flow:
        1. Check if connection already in progress (return early if so)
        2. Validate COM port is selected
        3. Show "Connecting..." UI feedback
        4. Call _connect_serial_async() to connect in background thread
        5. Callback (_handle_serial_connection_result) updates UI when done
        
        Disconnect flow:
        1. Close serial port (blocking but fast)
        2. Update UI
        3. Close camera if open
        """

        if self.ser is None or not getattr(self.ser, "is_open", False):
            # Connection mode
            # Check if connection is already in progress
            if getattr(self, '_serial_connection_in_progress', False):
                self._safe_enhancer_log("Connection attempt already in progress, please wait...")
                return False
            
            port = self._safe_widget_method_return("com_port_input", "text", "")
            baud = self._safe_int_widget_value("baud_rate_input", 115200)
            
            # Validate port is not empty
            if not port or port.strip() == "":
                self._safe_enhancer_log("COM port not specified. Please select a valid port.")
                try:
                    if hasattr(self, 'connection_status_label'):
                        self.connection_status_label.setText("✗ No COM port specified")
                        self.connection_status_label.setStyleSheet("color: #FF6666; background-color: #2d2d2d; padding: 4px; border-radius: 3px;")
                except Exception:
                    pass
                return False
            
            # Mark connection as in progress
            self._serial_connection_in_progress = True
            
            # Update UI to show connecting state
            try:
                if hasattr(self, 'connect_button') and self.connect_button is not None:
                    self.connect_button.setText("Connecting...")
                    self.connect_button.setEnabled(False)
                else:
                    self._safe_widget_call("connect_button", "setText", "Connecting...")
                    self._safe_widget_call("connect_button", "setEnabled", False)
            except Exception:
                pass
            
            try:
                if hasattr(self, 'connection_status_label'):
                    self.connection_status_label.setText(f"Connecting to {port} @ {baud}...")
                    self.connection_status_label.setStyleSheet("color: #FFFF00; background-color: #2d2d2d; padding: 4px; border-radius: 3px;")
            except Exception:
                pass
            
            # Close old connection if it exists but is not open
            if self.ser and not self.ser.is_open:
                try:
                    if getattr(self, "enhancer", None):
                        self.enhancer.update_serial_status(False)
                    self.ser.close()
                except Exception:
                    pass
            
            # Start async connection in background thread
            # This prevents the GUI from freezing during the potentially long serial open
            self._connect_serial_async(port, baud)
            return  # Don't block, callback will handle the rest

        else:
            try:
                if getattr(self, "enhancer", None):
                    self.enhancer.update_serial_status(False)
                self.ser.close()
                return True  # Disconnected successfully
            except Exception as e:
                self._safe_enhancer_log(f"Error during disconnect: {e}")
                return False  # Error during disconnect
            finally:
                self.ser = None
                self._safe_enhancer_log("Disconnected.")
                if getattr(self, "enhancer", None):
                    self.enhancer.update_serial_status(False)
                try:
                    self.connect_button.setText("Connect")
                except Exception:
                    pass
                # Update connection status label
                try:
                    if hasattr(self, 'connection_status_label'):
                        self.connection_status_label.setText("Disconnected")
                        self.connection_status_label.setStyleSheet("color: #999999; background-color: #2d2d2d; padding: 4px; border-radius: 3px;")
                except Exception:
                    pass
                # Close camera on disconnect
                try:
                    if (
                        getattr(self, "cap", None) is not None
                        and getattr(self.cap, "isOpened", lambda: False)()
                    ):
                        try:
                            # use safe helper to release the capture
                            self._cap_release()
                        except Exception:
                            pass
                        # Clear references and update UI
                        try:
                            self.cap = None
                        except Exception:
                            self.cap = None
                        try:
                            self.video_label.clear()
                            self.video_label.setText("Camera Feed")
                        except Exception:
                            pass
                        # BULLETPROOF FIX: Disable buttons on disconnect, but ensure clean state
                        try:
                            if getattr(self, "tracking_btn", None) is not None:
                                self.tracking_btn.setEnabled(False)
                                self.tracking_btn.setChecked(False)
                                self.tracking_btn.setText("Start Tracking")
                        except Exception:
                            pass
                        try:
                            if getattr(self, "aiming_btn", None) is not None:
                                self.aiming_btn.setEnabled(False)
                                self.aiming_btn.setChecked(False)
                                self.aiming_btn.setText("Start Aiming")
                        except Exception:
                            pass
                        try:
                            self._safe_enhancer_log(
                                "Camera closed (auto on disconnect)."
                            )
                        except Exception:
                            pass
                        try:
                            if getattr(self, "state_logger", None):
                                self.state_logger.log("Camera feed stopped")
                        except Exception:
                            pass
                except Exception:
                    pass

    def set_trigger_mode(self, index):
        self.trigger_mode_bb = index == 1
        mode_text = (
            "Projectile (BB/Servo)" if self.trigger_mode_bb else "Water (MOSFET)"
        )
        self._safe_enhancer_log(f"Trigger mode set to: {mode_text}", fire=False)
        self.save_settings()  # V4 Save

    def open_camera(self, indices=None):
        """Attempt to open a camera. If the user selected a preferred camera in the UI
        it will be tried first, otherwise the method will try indices 0..4.
        Returns an opened cv2.VideoCapture or None."""
        last_err = None

        # Determine preferred index from UI if available
        preferred = None
        try:
            if getattr(self, "camera_index_combo", None) is not None:
                txt = self.camera_index_combo.currentText()
                if txt and txt.lower() != "auto":
                    try:
                        preferred = int(txt)
                    except Exception:
                        preferred = None
        except Exception:
            preferred = None

        # Build try order: preferred first if present, then fallback range
        try_indices = []
        if preferred is not None:
            try_indices.append(preferred)
            for i in range(0, 5):
                if i != preferred:
                    try_indices.append(i)
        else:
            # If caller supplied explicit indices, use them; otherwise try 0..4
            if indices is not None:
                try_indices = list(indices)
            else:
                try_indices = list(range(0, 5))

        for idx in try_indices:
            try:
                # Simple, proven camera opening logic
                # Open camera with default backend
                cap = cv2.VideoCapture(int(idx))
                
                time.sleep(0.05)
                
                if cap.isOpened():
                    print(f"[CAMERA] Successfully opened camera {idx}")
                    
                    # Get target resolution
                    if hasattr(self, "frame_ratio_options") and hasattr(self, "frame_ratio_setting"):
                        width, height = self.frame_ratio_options.get(
                            self.frame_ratio_setting, (1280, 720)
                        )
                    else:
                        width, height = 1280, 720
                    
                    # Set resolution
                    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
                    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
                    time.sleep(0.05)
                    
                    # Get actual resolution from camera
                    actual_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                    actual_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                    
                    print(f"[CAMERA] Resolution: {actual_w}x{actual_h}")
                    
                    try:
                        self.enhancer.log_serial_output(
                            f"[CAMERA] Opened camera {idx}: {actual_w}x{actual_h}",
                            fire=False
                        )
                    except Exception:
                        pass
                    
                    # ⚠️ CRITICAL: Update frame_width/height with ACTUAL camera resolution
                    # This is the ONLY place (other than __init__) where these values should be modified.
                    # The actual resolution may differ from requested if camera doesn't support it.
                    # These values become the SOURCE OF TRUTH for all frame calculations.
                    # DO NOT modify frame_width/height anywhere else (especially not in update_frame).
                    self.frame_width = actual_w if actual_w > 0 else width
                    self.frame_height = actual_h if actual_h > 0 else height
                    
                    try:
                        if getattr(self, "state_logger", None):
                            self.state_logger.log("Camera feed started")
                    except Exception:
                        pass
                    
                    return cap
                else:
                    cap.release()
            
            except Exception as e:
                last_err = e
                try:
                    self.enhancer.log_serial_output(
                        f"open_camera: error opening index {idx}: {e}", fire=False
                    )
                except Exception:
                    pass

        # All attempts failed
        try:
            if last_err is not None:
                self.enhancer.log_serial_output(
                    f"open_camera: all indices failed; last error: {last_err}",
                    fire=False,
                )
            else:
                self.enhancer.log_serial_output(
                    "open_camera: no camera opened on tested indices", fire=False
                )
        except Exception:
            pass
        return None

    def handle_connect_sound(self):
        """Perform serial connection/disconnection and play sound only if successful."""
        try:
            # Check if we're connecting or disconnecting
            connecting = self.ser is None or not getattr(self.ser, "is_open", False)

            # Attempt the operation
            if self.connect_serial():
                # Only play sound if the operation was successful AND we were connecting
                if connecting and hasattr(self, "enhancer") and self.enhancer:
                    try:
                        self.enhancer.play_sound(self.enhancer.connect_sound)
                    except Exception:
                        pass
        except Exception:
            # connect_serial logs its own errors; ignore here
            pass

    def toggle_relay(self, relay_number):
        if relay_number == 1:
            self.relay1_state = 1 - self.relay1_state
            text = "LED (Relay1): ON" if self.relay1_state else "LED (Relay1): OFF"
            self.relay1_button.setText(text)  #
            self.enhancer.log_serial_output(
                f"LED (Relay 1) set to: {'ON' if self.relay1_state else 'OFF'}",
                fire=False,
            )
        elif relay_number == 2:
            self.relay2_state = 1 - self.relay2_state
            text = "LASER (Relay2): ON" if self.relay2_state else "LASER (Relay2): OFF"
            self.relay2_button.setText(text)  #
            self.enhancer.log_serial_output(
                f"LASER (Relay 2) set to: {'ON' if self.relay2_state else 'OFF'}",
                fire=False,
            )
        self.save_settings()  # V4 Save

    def toggle_safety(self, checked=None):
        """Toggle the safety state. safety_state: 1 = locked (no fire), 0 = unlocked (allow firing).
        Button appearance: Unchecked = LOCKED (safe), Checked = ARMED (unsafe)."""
        # If called from a button, 'checked' will be provided
        if checked is not None:
            self.safety_state = (
                0 if checked else 1
            )  # checked=ARMED(0), unchecked=SAFE(1)
        else:  # Called from old safety button
            self.safety_state = 1 - getattr(self, "safety_state", 1)

        if self.safety_state == 1:  # LOCKED/SAFE
            self.safety_button.setText("Safety: LOCKED (No Fire)")
            self.safety_button.setChecked(False)  # Button appears unpressed when safe
            self.enhancer.arm_toggle_btn.setChecked(False)  # Sync top bar
        else:  # ARMED/UNSAFE
            self.safety_button.setText("Safety: ARMED (Can Fire)")
            self.safety_button.setChecked(True)  # Button appears pressed when armed
            self.enhancer.arm_toggle_btn.setChecked(True)  # Sync top bar

        self.enhancer.log_serial_output(
            f"Safety state set to: {'LOCKED' if self.safety_state==1 else 'ARMED'}",
            fire=False,
        )
        try:
            if getattr(self, "state_logger", None):
                self.state_logger.log(
                    "Safety engaged" if self.safety_state == 1 else "Safety released"
                )
        except Exception:
            pass
        self.save_settings()  # V4 Save
        try:
            # If safety locked, ensure MOSFET hold and rapid-fire are disabled
            if getattr(self, "safety_state", 1) == 1:
                try:
                    if getattr(self, "mosfet_hold_btn", None) is not None and self.mosfet_hold_btn.isChecked():
                        try:
                            self.mosfet_hold_btn.setChecked(False)
                        except Exception:
                            pass
                    # Stop rapid-fire if active
                    if getattr(self, "rapid_fire_timer_active", False):
                        try:
                            self.stop_rapid_fire()
                        except Exception:
                            pass
                except Exception:
                    pass
        except Exception:
            pass

    def toggle_auto_fire(self, state):
        """Handler for manual-mode auto-fire checkbox state change.
        Plays an armed sound when enabled (checked).
        """
        try:
            checked = (
                (state == Qt.CheckState.Checked)
                if isinstance(state, int)
                else bool(state)
            )
        except Exception:
            checked = bool(state)

        if checked:
            self.auto_fire_enabled = True
            try:
                if hasattr(self, "enhancer") and self.enhancer:
                    self.enhancer.play_sound(self.enhancer.armed_sound)
            except Exception:
                pass
        else:
            self.auto_fire_enabled = False

    def set_fire_state(self, state):
        """Manual fire button (momentary). Only fires if safety allows it."""
        if state == 1:
            if self.safety_state == 0:
                self.trigger_fired = True
                self.enhancer.log_serial_output("MANUAL FIRE: TRIGGERED", fire=True)
                self.enhancer.play_fire()
                try:
                    # Send command immediately to Arduino
                    self.send_serial_command()
                except Exception:
                    pass
                try:
                    # Pulse the UI indicator to show the host requested a fire
                    self._pulse_fire_indicator()
                except Exception:
                    pass
            else:
                self.enhancer.log_serial_output(
                    "MANUAL FIRE: BLOCKED BY SAFETY", fire=False
                )
        else:
            self.trigger_fired = False
            try:
                # Send command immediately to Arduino to stop firing
                self.send_serial_command()
            except Exception:
                pass

    def _on_mosfet_hold_toggled(self, checked):
        """Toggle a latched MOSFET ON/OFF. Respects safety and trigger mode and will send a command immediately."""
        try:
            active = bool(checked)
        except Exception:
            active = bool(checked)
        
        # Disallow in BB trigger mode
        if getattr(self, "trigger_mode_bb", False):
            try:
                self.enhancer.log_serial_output("MOSFET hold only available in MOSFET trigger mode.", fire=False)
            except Exception:
                pass
            return
        
        # Disallow when safety locked
        if active and getattr(self, "safety_state", 1) == 1:
            try:
                self.enhancer.log_serial_output("Cannot enable MOSFET hold: Safety is LOCKED.", fire=False)
            except Exception:
                pass
            return
        
        # Disallow while rapid-fire is active
        if getattr(self, "rapid_fire_timer_active", False) and active:
            try:
                self.enhancer.log_serial_output("Cannot enable MOSFET hold while Rapid-fire is active.", fire=False)
            except Exception:
                pass
            return
        
        # All checks passed - Apply new state and send serial command immediately
        try:
            self.trigger_fired = bool(active)
            
            # Update button text
            if getattr(self, "mosfet_hold_btn", None) is not None:
                try:
                    self.mosfet_hold_btn.setText("MOSFET: ON" if active else "MOSFET: OFF")
                except Exception:
                    pass
            
            # Send command to Arduino
            try:
                self.send_serial_command()
            except Exception:
                pass
            
            # Log status
            try:
                self.enhancer.log_serial_output(f"MOSFET hold {'ENABLED' if active else 'DISABLED'}", fire=False)
            except Exception:
                pass
            
            # Play fire sound if enabling
            if active:
                try:
                    self.enhancer.play_fire()
                except Exception:
                    pass
                try:
                    self._pulse_fire_indicator()
                except Exception:
                    pass
        except Exception:
            pass

    # --- Rapid-fire MOSFET support ---
    def _on_rapid_rate_changed(self, val):
        try:
            self.rapid_fire_rate_hz = int(val)
        except Exception:
            try:
                self.rapid_fire_rate_hz = int(getattr(self, "rapid_fire_rate_hz", 1))
            except Exception:
                self.rapid_fire_rate_hz = 1
        try:
            # If running, update timer intervals immediately
            if getattr(self, "rapid_fire_timer_active", False):
                self._update_rapid_intervals()
        except Exception:
            pass
        try:
            self.save_settings()
        except Exception:
            pass

    def _on_rapid_duty_changed(self, val):
        try:
            pct = int(val)
            pct = max(1, min(100, pct))
            self.rapid_fire_duty = float(pct) / 100.0
        except Exception:
            try:
                self.rapid_fire_duty = float(getattr(self, "rapid_fire_duty", 0.5))
            except Exception:
                self.rapid_fire_duty = 0.5
        try:
            if getattr(self, "rapid_fire_timer_active", False):
                self._update_rapid_intervals()
        except Exception:
            pass
        try:
            self.save_settings()
        except Exception:
            pass

    def _on_rapid_fire_toggled(self, checked):
        try:
            active = bool(checked)
        except Exception:
            active = bool(checked)

        # Only allow rapid-fire in MOSFET mode and when safety is ARMED (safety_state == 0)
        try:
            if getattr(self, "trigger_mode_bb", False):
                # BB servo mode - rapid MOSFET not supported
                try:
                    self.enhancer.log_serial_output(
                        "Rapid-fire is only supported in MOSFET trigger mode.", fire=False
                    )
                except Exception:
                    pass
                # revert toggle in UI
                try:
                    if getattr(self, "rapid_fire_enable_checkbox", None) is not None:
                        self.rapid_fire_enable_checkbox.setChecked(False)
                except Exception:
                    pass
                return
        except Exception:
            pass

        # Disallow rapid-fire when safety is LOCKED (safety_state != 0)
        if active and getattr(self, "safety_state", 1) != 0:
            try:
                self.enhancer.log_serial_output(
                    "Rapid-fire blocked: Safety is LOCKED. Must be ARMED first.", fire=False
                )
            except Exception:
                pass
            return

        # Toggle active state
        try:
            self.rapid_fire_enabled = bool(active)
        except Exception:
            self.rapid_fire_enabled = False

        try:
            if self.rapid_fire_enabled:
                self.start_rapid_fire()
            else:
                self.stop_rapid_fire()
        except Exception:
            pass

        try:
            self.save_settings()
        except Exception:
            pass

    def _on_frame_ratio_changed(self, ratio_label):
        """
        Handle frame ratio (resolution) change from UI dropdown.
        Updates frame_width, frame_height, adjusts max_contour, and re-opens camera with new resolution.
        
        This is called when user changes the camera resolution selector.
        All tracking calculations that depend on frame dimensions will automatically
        use the updated values on the next frame.
        """
        try:
            print(f"[RES-CHANGE] _on_frame_ratio_changed called with: '{ratio_label}'")
            
            if ratio_label not in self.frame_ratio_options:
                print(f"[RES-CHANGE] ERROR: '{ratio_label}' not in frame_ratio_options. Available: {list(self.frame_ratio_options.keys())}")
                return
            
            # Get new dimensions from options dict
            width, height = self.frame_ratio_options[ratio_label]
            
            # ⚠️ CRITICAL: Update frame dimensions when resolution changes
            # This is one of only TWO places where frame_width/height should be modified:
            # 1. Here (when user changes resolution via UI)
            # 2. In open_camera() (when camera opens and reports actual resolution)
            # DO NOT modify these values anywhere else in the code!
            self.frame_ratio_setting = ratio_label
            old_width = self.frame_width
            old_height = self.frame_height
            self.frame_width = width
            self.frame_height = height
            
            print(f"[RES-CHANGE] Updated frame dimensions: {old_width}x{old_height} -> {width}x{height}")
            print(f"[RES-CHANGE] self.frame_width={self.frame_width}, self.frame_height={self.frame_height}")
            
            # Auto-calculate and update max_contour based on new resolution
            try:
                new_max_contour = self._calculate_max_contour_for_resolution(ratio_label)
                if hasattr(self, "max_contour_input") and self.max_contour_input is not None:
                    self.max_contour_input.blockSignals(True)  # Prevent triggering save during update
                    self.max_contour_input.setValue(new_max_contour)
                    self.max_contour_input.blockSignals(False)
                    print(f"[RES-CHANGE] Auto-adjusted max_contour: {new_max_contour} px for {ratio_label}")
            except Exception as e:
                print(f"[RES-CHANGE] Could not auto-adjust max_contour: {e}")
            
            # Log metadata about this resolution
            try:
                if ratio_label in self.resolution_metadata:
                    meta = self.resolution_metadata[ratio_label]
                    print(f"[RES-CHANGE] Resolution info: {meta['label']}, FOV: {meta['fov_est']}, Performance: {meta['processing']}")
            except Exception:
                pass
            
            # Log the change with before/after
            try:
                self.enhancer.log_serial_output(
                    f"Resolution changed: {old_width}x{old_height} -> {ratio_label} ({width}x{height})",
                    fire=False
                )
            except Exception:
                pass
            
            # Re-open camera with new resolution in background to apply changes
            # This happens asynchronously without blocking the UI
            try:
                # Close current camera if open
                if self.cap is not None:
                    try:
                        self.cap.release()
                        print(f"[RES-CHANGE] Camera released successfully")
                    except Exception as e:
                        print(f"[RES-CHANGE] Error releasing camera: {e}")
                    self.cap = None
                
                # Signal that we need to re-open camera with new settings
                self._camera_open_needed = True
                print(f"[RES-CHANGE] Set _camera_open_needed = True")
                
                # Log success
                try:
                    self.enhancer.log_serial_output(
                        f"Camera will re-open with new resolution {ratio_label}",
                        fire=False
                    )
                except Exception:
                    pass
            except Exception as e:
                print(f"[RES-CHANGE] Exception during camera re-open: {e}")
                try:
                    self.enhancer.log_serial_output(
                        f"[RESOLUTION CHANGE] Error re-opening camera: {e}",
                        fire=False
                    )
                except Exception:
                    pass
            
            # Save settings ONCE at the end to persist resolution change
            try:
                self.save_settings()
            except Exception as e:
                print(f"[RES-CHANGE] Error saving settings: {e}")
            
        except Exception as e:
            print(f"[RES-CHANGE] FATAL ERROR: {e}")
            import traceback
            traceback.print_exc()
            try:
                self.enhancer.log_serial_output(
                    f"[FRAME_RATIO ERROR] {str(e)}",
                    fire=False
                )
            except Exception:
                pass

    def _update_rapid_intervals(self):
        """Recompute on/off intervals (ms) from rate and duty and apply to running timer."""
        try:
            rate = max(1, int(getattr(self, "rapid_fire_rate_hz", 1)))
            period_ms = max(1, int(1000.0 / float(rate)))
            on_ms = max(1, int(period_ms * float(getattr(self, "rapid_fire_duty", 0.5))))
            off_ms = max(1, period_ms - on_ms)
            self._rapid_on_ms = on_ms
            self._rapid_off_ms = off_ms
            # If timer is active, adjust next interval to reflect new values
            if getattr(self, "rapid_fire_timer_active", False) and getattr(self, "rapid_fire_timer", None) is not None:
                try:
                    next_ms = self._rapid_on_ms if getattr(self, "_rapid_fire_on", False) else self._rapid_off_ms
                    # Ensure timer exists before calling methods
                    timer = getattr(self, "rapid_fire_timer", None)
                    if timer is not None:
                        try:
                            timer.start(next_ms)
                        except Exception:
                            # fallback: stop/start
                            try:
                                timer.stop()
                                timer.start(next_ms)
                            except Exception:
                                pass
                except Exception:
                    pass
        except Exception:
            pass

    def start_rapid_fire(self):
        """Begin periodic rapid-fire pulses using a QTimer that toggles ON/OFF phases."""
        try:
            # guard: do not start if in BB servo mode
            if getattr(self, "trigger_mode_bb", False):
                try:
                    self.enhancer.log_serial_output("Cannot start rapid-fire: not in MOSFET mode.", fire=False)
                except Exception:
                    pass
                return

            # guard: safety must be ARMED (0)
            if getattr(self, "safety_state", 1) == 1:
                try:
                    self.enhancer.log_serial_output("Cannot start rapid-fire: Safety is LOCKED.", fire=False)
                except Exception:
                    pass
                # ensure UI reflects disabled state
                try:
                    if getattr(self, "rapid_fire_enable_checkbox", None) is not None:
                        self.rapid_fire_enable_checkbox.setChecked(False)
                except Exception:
                    pass
                return

            # create timer lazily
            if getattr(self, "rapid_fire_timer", None) is None:
                try:
                    self.rapid_fire_timer = QTimer()
                    self.rapid_fire_timer.setSingleShot(False)
                    try:
                        self.rapid_fire_timer.timeout.connect(self._rapid_fire_tick)
                    except Exception:
                        try:
                            # fallback: use lambda wrapper
                            self.rapid_fire_timer.timeout.connect(lambda: self._rapid_fire_tick())
                        except Exception:
                            pass
                except Exception:
                    self.rapid_fire_timer = None

            # compute intervals
            self._update_rapid_intervals()

            # mark active
            self.rapid_fire_timer_active = True

            # Check if target is in deadzone before initial pulse
            in_deadzone = False
            try:
                # Use actual frame dimensions from self.frame_width/height
                # This respects resolution changes from the camera resolution selector
                w = getattr(self, "frame_width", 640)
                h = getattr(self, "frame_height", 480)
                cx = w // 2
                cy = h // 2
                deadzone_val = self._safe_int_widget_value("deadzone_slider", 40)
                # Check if any detection is in deadzone
                if hasattr(self, "last_detections") and self.last_detections:
                    for x_box, y_box, w_box, h_box in self.last_detections:
                        tx = int(x_box + w_box / 2)
                        ty = int(y_box + h_box / 2)
                        dist = ((tx - cx) ** 2 + (ty - cy) ** 2) ** 0.5
                        if dist <= deadzone_val:
                            in_deadzone = True
                            break
            except Exception:
                pass

            # Only fire initial pulse if target is in deadzone
            if in_deadzone:
                try:
                    self._rapid_fire_on = True
                    self.trigger_fired = True
                    # send an immediate on-command
                    try:
                        self.send_serial_command()
                    except Exception:
                        pass
                except Exception:
                    pass
            else:
                # No target in deadzone - start in OFF state
                self._rapid_fire_on = False
                self.trigger_fired = False

            # start timer for ON phase
            try:
                if getattr(self, "rapid_fire_timer", None) is not None:
                    try:
                        self.rapid_fire_timer.start(getattr(self, "_rapid_on_ms", 1))
                    except Exception:
                        try:
                            self.rapid_fire_timer.start(1)
                        except Exception:
                            pass
            except Exception:
                pass
            try:
                self.enhancer.log_serial_output("Rapid-fire started.", fire=False)
            except Exception:
                pass
        except Exception:
            pass

    def stop_rapid_fire(self):
        try:
            # stop timer and ensure the MOSFET is in OFF state
            try:
                if getattr(self, "rapid_fire_timer", None) is not None:
                    try:
                        self.rapid_fire_timer.stop()
                    except Exception:
                        pass
            except Exception:
                pass
            try:
                self.rapid_fire_timer_active = False
            except Exception:
                pass
            try:
                # ensure MOSFET off
                self.trigger_fired = False
                try:
                    self.send_serial_command()
                except Exception:
                    pass
            except Exception:
                pass
            try:
                self.enhancer.log_serial_output("Rapid-fire stopped.", fire=False)
            except Exception:
                pass
        except Exception:
            pass

    def _rapid_fire_tick(self):
        """Internal timer callback toggling ON/OFF phases and sending commands."""
        try:
            if not getattr(self, "rapid_fire_timer_active", False):
                try:
                    if getattr(self, "rapid_fire_timer", None) is not None:
                        try:
                            self.rapid_fire_timer.stop()
                        except Exception:
                            pass
                except Exception:
                    pass
                return

            # Only proceed if safety is off
            if getattr(self, "safety_state", 1) != 0:
                return

            # First check if target is in deadzone before firing
            in_deadzone = False
            try:
                # Use actual frame dimensions from self.frame_width/height
                # This respects resolution changes from the camera resolution selector
                w = getattr(self, "frame_width", 640)
                h = getattr(self, "frame_height", 480)
                cx = w // 2
                cy = h // 2
                deadzone_val = self._safe_int_widget_value("deadzone_slider", 40)
                # Check if any detection is in deadzone
                if hasattr(self, "last_detections") and self.last_detections:
                    for x_box, y_box, w_box, h_box in self.last_detections:
                        tx = int(x_box + w_box / 2)
                        ty = int(y_box + h_box / 2)
                        dist = ((tx - cx) ** 2 + (ty - cy) ** 2) ** 0.5
                        if dist <= deadzone_val:
                            in_deadzone = True
                            break
            except Exception:
                pass

            # Only proceed with firing cycle if target is in deadzone
            if not in_deadzone:
                # Target not in deadzone - stop firing and keep checking
                try:
                    self._rapid_fire_on = False
                    self.trigger_fired = False
                    try:
                        self.send_serial_command()
                    except Exception:
                        pass
                    next_ms = getattr(self, "_rapid_off_ms", 1)
                    if getattr(self, "rapid_fire_timer", None) is not None:
                        self.rapid_fire_timer.start(max(1, int(next_ms)))
                except Exception:
                    pass
                return

            # Target is in deadzone - proceed with firing cycle
            try:
                if getattr(self, "_rapid_fire_on", False):
                    # ON -> switch to OFF
                    try:
                        self._rapid_fire_on = False
                        self.trigger_fired = False
                        try:
                            self.send_serial_command()
                        except Exception:
                            pass
                        # schedule next ON after off interval
                        try:
                            next_ms = getattr(self, "_rapid_off_ms", 1)
                            if getattr(self, "rapid_fire_timer", None) is not None:
                                self.rapid_fire_timer.start(max(1, int(next_ms)))
                        except Exception:
                            pass
                    except Exception:
                        pass
                else:
                    # OFF -> switch to ON (already verified target is in deadzone)
                    try:
                        self._rapid_fire_on = True
                        self.trigger_fired = True
                        try:
                            self.send_serial_command()
                        except Exception:
                            pass
                        # schedule next OFF after on interval
                        try:
                            next_ms = getattr(self, "_rapid_on_ms", 1)
                            if getattr(self, "rapid_fire_timer", None) is not None:
                                self.rapid_fire_timer.start(max(1, int(next_ms)))
                        except Exception:
                            pass
                    except Exception:
                        pass
            except Exception:
                pass
        except Exception:
            pass

    def export_rapid_fire_preset(self):
        """Export the current rapid-fire settings to a JSON file chosen by the user."""
        try:
            preset = {
                "rapid_fire_rate_hz": int(getattr(self, "rapid_fire_rate_hz", 1)),
                "rapid_fire_duty_percent": int(getattr(self, "rapid_fire_duty", 0.5) * 100),
                "created_at": time.time(),
            }
        except Exception:
            preset = {"rapid_fire_rate_hz": 1, "rapid_fire_duty_percent": 50, "created_at": time.time()}

        try:
            fname, _ = QFileDialog.getSaveFileName(self, "Export Rapid-Fire Preset", "rapid_fire_preset.json", "RapidFire Preset (*.json);;All Files (*)")
            if not fname:
                return
            try:
                with open(fname, "w") as f:
                    json.dump(preset, f, indent=4)
                try:
                    self.enhancer.log_serial_output(f"Rapid-fire preset exported to {fname}", fire=False)
                except Exception:
                    pass
            except Exception as e:
                try:
                    self.enhancer.log_serial_output(f"Failed to export preset: {e}", fire=False)
                except Exception:
                    pass
        except Exception:
            pass

    def move_manual(self, pan=0, tilt=0):
        """Handle manual movement with speed control and sound effects."""
        # Start of manual movement - set manual override flag but DO NOT stop detection.
        # We want the operator to be able to move the turret while detection remains
        # active; manual_override and a short suppression timer ensure operator control
        # temporarily takes precedence without disabling detection entirely.
        if not self.manual_override:
            self.manual_override = True
            self.tracking_was_active = self.tracking_active  # Remember state
            # Set temporary suppression so detection/tracking doesn't fight manual input
            # DEFENSIVE: Validate timeout is within reasonable bounds (max 5 seconds)
            suppress_secs = min(getattr(self, "manual_control_suppress_seconds", 1.0), 5.0)
            self._manual_override_until = time.time() + suppress_secs
            # Play movement sound if enabled
            try:
                if getattr(self, "sound_enabled", True):
                    mv = getattr(self.enhancer, "movement_sound", None)
                    if mv is not None:
                        try:
                            self.enhancer.play_sound(mv)
                        except Exception:
                            pass
            except Exception:
                pass
            # update UI status indicator
            try:
                if getattr(self, "override_status_label", None):
                    self.override_status_label.setText("Manual Override: active")
            except Exception:
                pass

        pan_dir = -1 if self.flip_pan_direction else 1
        tilt_dir = -1 if self.flip_tilt_direction else 1

        # Apply manual speed scaling (1-100% -> 0.1-1.0)
        speed_scale = self._safe_int_widget_value("manual_speed_slider", 50) / 100.0

        # ========== ENCODER-AWARE LIMIT PROTECTION ==========
        # If encoder is enabled and has detected physical boundaries, use those.
        # Otherwise, fall back to user-configured soft limits.
        encoder_aware_tilt_min = self.TILT_MIN
        encoder_aware_tilt_max = self.TILT_MAX
        
        if getattr(self, "tilt_encoder_enabled", False) and hasattr(self, "encoder_tilt_min_detected"):
            # Use encoder-detected boundaries (physical hard stops)
            encoder_aware_tilt_min = getattr(self, "encoder_tilt_min_detected", self.TILT_MIN)
            encoder_aware_tilt_max = getattr(self, "encoder_tilt_max_detected", self.TILT_MAX)
            tilt_position = getattr(self, "tilt_position_error", 0.0)
            try:
                if self.enhancer:
                    self.enhancer.log_serial_output(
                        f"[ENCODER LIMIT] min={encoder_aware_tilt_min:.1f}° max={encoder_aware_tilt_max:.1f}° pos_err={tilt_position:.1f}°",
                        fire=False,
                    )
            except Exception:
                pass

        if pan != 0:
            if isinstance(pan, int):
                scaled_pan = pan * speed_scale
                self.target_pan += scaled_pan * pan_dir
                # Log pan movement
                try:
                    if self.enhancer:
                        self.enhancer.log_serial_output(
                            f"Manual PAN: {scaled_pan * pan_dir:+.1f}° (to {self.target_pan:.1f}°) [Speed: {speed_scale*100:.0f}%]",
                            fire=False,
                        )
                except Exception:
                    pass
            else:
                self.target_pan = pan
        if tilt != 0:
            if isinstance(tilt, int):
                scaled_tilt = tilt * speed_scale
                old_tilt = self.target_tilt
                self.target_tilt += scaled_tilt * tilt_dir
                # Log tilt movement with direction
                move_direction = "UP" if scaled_tilt * tilt_dir > 0 else "DOWN"
                try:
                    if self.enhancer:
                        self.enhancer.log_serial_output(
                            f"Manual TILT: {move_direction} by {abs(scaled_tilt * tilt_dir):+.1f}° (from {old_tilt:.1f}° to {self.target_tilt:.1f}°) [Speed: {speed_scale*100:.0f}%]",
                            fire=False,
                        )
                except Exception:
                    pass
            else:
                self.target_tilt = tilt

        # Update position display
        try:
            self.position_label.setText(
                f"PAN: {self.target_pan:.1f}° TILT: {self.target_tilt:.1f}°"
            )
        except Exception:
            pass

        # Keep targets as floats so small nudges accumulate; integer conversion
        # is performed only when sending to the hardware.
        self.target_pan = float(np.clip(self.target_pan, self.PAN_MIN, self.PAN_MAX))
        
        # ========== CRITICAL FIX: USE ENCODER-AWARE LIMITS FOR MANUAL MOVEMENT ==========
        # This ensures manual movement respects encoder-detected physical boundaries
        self.target_tilt = float(
            np.clip(self.target_tilt, encoder_aware_tilt_min, encoder_aware_tilt_max)
        )
        
        # Log the clamping if it occurred
        if self.target_tilt != float(np.clip(self.target_tilt, self.TILT_MIN, self.TILT_MAX)):
            try:
                if self.enhancer:
                    self.enhancer.log_serial_output(
                        f"[CLAMP] Tilt clamped to encoder limits: {self.target_tilt:.1f}° (encoder: {encoder_aware_tilt_min:.1f}°-{encoder_aware_tilt_max:.1f}°, soft: {self.TILT_MIN}°-{self.TILT_MAX}°)",
                        fire=False,
                    )
            except Exception:
                pass

        try:
            if self.enhancer:
                self.enhancer.log_serial_output(
                    f"Manual Move: PAN={self.target_pan:.1f}° TILT={self.target_tilt:.1f}° [encoder_limits={encoder_aware_tilt_min:.1f}°-{encoder_aware_tilt_max:.1f}°]",
                    fire=False,
                )
        except Exception:
            pass
        # Send an immediate serial update so manual controls feel responsive
        try:
            self.send_serial_command()
        except Exception:
            pass

    def pan_left(self):
        """Pan turret left by step size."""
        step_size = self._safe_int_widget_value("step_size_input", self.STEP_INCREMENT)
        self.move_manual(pan=-step_size, tilt=0)

    def pan_right(self):
        """Pan turret right by step size."""
        step_size = self._safe_int_widget_value("step_size_input", self.STEP_INCREMENT)
        self.move_manual(pan=step_size, tilt=0)

    def tilt_up(self):
        """Tilt turret up by step size."""
        step_size = self._safe_int_widget_value("step_size_input", self.STEP_INCREMENT)
        self.move_manual(pan=0, tilt=step_size)

    def tilt_down(self):
        """Tilt turret down by step size."""
        step_size = self._safe_int_widget_value("step_size_input", self.STEP_INCREMENT)
        self.move_manual(pan=0, tilt=-step_size)

    def quick_target_lock(self):
        """
        QUICK STRIKE: Instantly snap to last detected target at maximum speed.
        
        Behavior:
        1. Capture current target position from last_detections or last_target_center
        2. Convert pixel coords to pan/tilt angles
        3. Enter quick_strike mode (bypasses detection, moves at max speed)
        4. When position reached: auto-fire if armed, then resume autotracking
        
        Safety: Only activates if a target has been detected. 2-second timeout.
        """
        try:
            # Check if quick strike is already active (prevent double-click)
            if getattr(self, "quick_strike_active", False):
                self.enhancer.log_serial_output("[⚡ STRIKE] Already in progress - wait for completion", fire=False)
                return
            
            # Get target center from last_target_center or calculate from last_detections
            target_x, target_y = None, None
            
            # First try last_target_center (set during tracking)
            if getattr(self, "last_target_center", None):
                target_x, target_y = self.last_target_center
            
            # Fallback: calculate from last_detections bounding box
            if target_x is None and getattr(self, "last_detections", None) and len(self.last_detections) > 0:
                try:
                    # Get largest detection by area
                    det = max(self.last_detections, key=lambda b: b[2] * b[3])
                    x_box, y_box, w_box, h_box = det
                    target_x = x_box + w_box / 2.0
                    target_y = y_box + h_box / 2.0
                except Exception:
                    pass
            
            # No target available
            if target_x is None or target_y is None:
                self.enhancer.log_serial_output("[⚡ STRIKE] ❌ No target detected - cannot strike", fire=False)
                return
            
            frame_width = getattr(self, "frame_width", 640)
            frame_height = getattr(self, "frame_height", 480)
            
            # Convert pixel coordinates to pan/tilt angles
            # Use same FOV settings as normal tracking for consistency
            horizontal_fov = 110.0  # degrees
            vertical_fov = 85.0  # degrees
            
            # Calculate pixel deviation from frame center
            pixel_deviation_x = target_x - (frame_width / 2.0)
            pixel_deviation_y = target_y - (frame_height / 2.0)
            
            # Convert to angle offset
            degrees_per_pixel_x = horizontal_fov / frame_width
            degrees_per_pixel_y = vertical_fov / frame_height
            
            pan_offset = pixel_deviation_x * degrees_per_pixel_x
            tilt_offset = -pixel_deviation_y * degrees_per_pixel_y  # Inverted
            
            # Calculate target angles from current position (more accurate than HOME)
            current_pan = getattr(self, "target_pan", getattr(self, "HOME_PAN", 90))
            current_tilt = getattr(self, "target_tilt", getattr(self, "HOME_TILT", 45))
            
            # Since err_x/err_y represent deviation, we add the offset to current position
            # But we're starting from pixel deviation, so use home as reference
            target_pan = float(np.clip(
                self.HOME_PAN + pan_offset,
                self.PAN_MIN,
                self.PAN_MAX
            ))
            target_tilt = float(np.clip(
                self.HOME_TILT + tilt_offset,
                self.TILT_MIN,
                self.TILT_MAX
            ))
            
            # Activate Quick Strike mode
            self.quick_strike_active = True
            self.quick_strike_target_pan = target_pan
            self.quick_strike_target_tilt = target_tilt
            self.quick_strike_start_time = time.time()
            self.quick_strike_fired = False
            
            # Log activation
            self.enhancer.log_serial_output(
                f"[⚡ STRIKE] Engaging! Target at pixel ({target_x:.0f}, {target_y:.0f})",
                fire=False
            )
            self.enhancer.log_serial_output(
                f"[⚡ STRIKE] Moving to Pan={target_pan:.1f}° Tilt={target_tilt:.1f}° at MAX SPEED",
                fire=False
            )
            
        except Exception as e:
            self.enhancer.log_serial_output(
                f"[⚡ STRIKE] ❌ Error: {e}",
                fire=False
            )
            self.quick_strike_active = False

    def manual_control_released(self):
        """Called when a manual control button is released."""
        # Keep manual_override True until suppression expires; releasing button
        # only ends the local pressed state. This allows tiny nudges without
        # permanently disabling the manual override behavior.
        if self.manual_override:
            try:
                # Short-circuit: if manual override timer already expired, clear it
                if time.time() >= getattr(self, "_manual_override_until", 0):
                    self.manual_override = False
                    if self.tracking_was_active:
                        self.tracking_active = True
                        self.tracking_was_active = False
                        self.enhancer.log_serial_output(
                            "Resumed tracking after manual move", fire=False
                        )
                else:
                    # Keep manual_override True until the suppression window finishes
                    self.enhancer.log_serial_output(
                        "Manual control released; operator override remains until suppression expires",
                        fire=False,
                    )
            except Exception:
                self.manual_override = False
        # update UI status if cleared
        try:
            if getattr(self, "override_status_label", None):
                if not self.manual_override:
                    self.override_status_label.setText("")
        except Exception:
            pass

    def set_manual_position(self, pan=None, tilt=None):
        if self.tracking_active:
            self.stop_tracking()

        if pan is not None:
            # allow fractional manual set
            try:
                self.target_pan = float(pan)
            except Exception:
                try:
                    self.target_pan = float(int(pan))
                except Exception:
                    self.target_pan = float(getattr(self, "HOME_PAN", 90))
        if tilt is not None:
            try:
                self.target_tilt = float(tilt)
            except Exception:
                try:
                    self.target_tilt = float(int(tilt))
                except Exception:
                    self.target_tilt = float(getattr(self, "HOME_TILT", 40))
        self.target_pan = float(np.clip(self.target_pan, self.PAN_MIN, self.PAN_MAX))
        self.target_tilt = float(
            np.clip(self.target_tilt, self.TILT_MIN, self.TILT_MAX)
        )
        self.enhancer.log_serial_output(
            f"Manual Set: PAN={self.target_pan}\u00b0, TILT={self.target_tilt}\u00b0",
            fire=False,
        )

    def go_home(self):
        """Move turret to its defined home position with smooth interpolation and reset tracking state cleanly."""
        try:
            # Read UI inputs safely, fall back to defaults if unavailable
            self.target_pan = float(self._safe_int_widget_value("home_pan_input", self.HOME_PAN))
            self.target_tilt = float(self._safe_int_widget_value("home_tilt_input", self.HOME_TILT))
        except Exception:
            self.target_pan = float(getattr(self, "HOME_PAN", 90))
            self.target_tilt = float(getattr(self, "HOME_TILT", 40))

        # Clamp to servo limits
        self.target_pan = float(np.clip(self.target_pan, self.PAN_MIN, self.PAN_MAX))
        self.target_tilt = float(np.clip(self.target_tilt, self.TILT_MIN, self.TILT_MAX))

        # --- HARD RESET PHASE ---
        try:
            # Stop current actions
            self.tracking_active = False
            self.aiming_active = False
            self.manual_override = False
            self._hold_last_position = False
            self._idle_state = None
            self._in_go_home = True

            # CRITICAL FIX: Define suspend_time for QTimer callback
            # This was commented out but is still needed for the timer delay
            suspend_time = float(getattr(self, "home_move_suspend_seconds", 2.5))
            
            # SMOOTH HOMING: Use slider value for home speed (default 5% for smooth movement)
            # User can adjust with the "Homing Speed" slider in Manual Control panel
            # Lower values = slower, smoother movement (better for fast servos)
            home_speed_pct = float(getattr(self, "home_speed_percent", 5))  # Default 5% (was 15%)
            home_speed_pct = float(np.clip(home_speed_pct, 1, 100))  # Clamp to valid range
            
            # BULLETPROOF FIX: NO DETECTION SUPPRESSION
            # Detection should continue running during home move
            # This allows immediate re-acquisition when home completes
            # REMOVED: self._suppress_detection_until = now + suspend_time
            # REMOVED: self._suspend_tracking_until = now + suspend_time

            # BULLETPROOF FIX: PRESERVE DETECTION HISTORY
            # Keep last_detections so if target is still visible, we can re-lock immediately
            # DISABLED clearing: if hasattr(self, "last_detections"): self.last_detections.clear()
            
            # Only clear current target position, not history
            self.target_x = None
            self.target_y = None
            self.target_locked = False

            # Reset servo state memory
            self.prev_pan_angle = self.target_pan
            self.prev_tilt_angle = self.target_tilt
            self.last_sent_pan = int(self.target_pan)
            self.last_sent_tilt = int(self.target_tilt)

            # Update UI
            if getattr(self, "override_status_label", None):
                self.override_status_label.setText("Returning Home...")
            self.enhancer.log_serial_output("[RESET] Tracking + Idle state cleared before Go Home", fire=False)

        except Exception as e:
            print(f"go_home reset error: {e}")

        # --- HOST-SIDE INTERPOLATED HOME MOVE ---
        try:
            # Use host-side interpolation to step toward home slowly and safely.
            # home_speed_pct is already transformed by exponential scaling above and
            # represents an effective percentage in the range ~0.5-100.
            normalized = float(home_speed_pct) / 100.0
            max_deg_per_sec = float(getattr(self, "HOME_MAX_SPEED_DEG_PER_SEC", 15.0))
            speed_deg_per_sec = max_deg_per_sec * normalized
            # Interval for interpolation steps (ms)
            interval_ms = int(getattr(self, "home_interpolate_interval_ms", 50))
            # Minimum step to ensure progress; otherwise very small speeds may stall
            step_deg = max(0.05, speed_deg_per_sec * (interval_ms / 1000.0))

            # Prepare interpolation state
            self._go_home_target_pan = float(self.target_pan)
            self._go_home_target_tilt = float(self.target_tilt)
            self._go_home_step_deg = float(step_deg)

            # Baseline current position comes from last_sent_* (reflects hardware)
            current_pan = float(getattr(self, "last_sent_pan", getattr(self, "prev_pan_angle", self.HOME_PAN)))
            current_tilt = float(getattr(self, "last_sent_tilt", getattr(self, "prev_tilt_angle", self.HOME_TILT)))

            try:
                # Clean up any previous timer
                if getattr(self, "_go_home_timer", None) is not None:
                    try:
                        self._go_home_timer.stop()
                        self._go_home_timer.deleteLater()
                    except Exception:
                        pass

                self._go_home_timer = QTimer()
                self._go_home_timer.setInterval(int(interval_ms))

                def _home_step():
                    try:
                        pan_now = float(getattr(self, "last_sent_pan", current_pan))
                        tilt_now = float(getattr(self, "last_sent_tilt", current_tilt))
                        pan_err = self._go_home_target_pan - pan_now
                        tilt_err = self._go_home_target_tilt - tilt_now

                        # If within small tolerance, finalize and stop timer
                        if abs(pan_err) <= 0.25 and abs(tilt_err) <= 0.25:
                            self.target_pan = float(self._go_home_target_pan)
                            self.target_tilt = float(self._go_home_target_tilt)
                            try:
                                self._go_home_timer.stop()
                                self._go_home_timer.deleteLater()
                            except Exception:
                                pass
                            self._in_go_home = False
                            # restore tracking/aiming state
                            self.tracking_active = True
                            self.aiming_active = True
                            try:
                                getattr(self.override_status_label, "setText", lambda x: None)("")
                            except Exception:
                                pass
                            self.enhancer.log_serial_output("Host-interpolated Go Home complete, tracking resumed", fire=False)
                            try:
                                self.send_serial_command()
                            except Exception:
                                pass
                            return

                        def step_to(curr, err):
                            if abs(err) <= self._go_home_step_deg:
                                return curr + err
                            return curr + (self._go_home_step_deg if err > 0 else -self._go_home_step_deg)

                        new_pan = float(np.clip(step_to(pan_now, pan_err), self.PAN_MIN, self.PAN_MAX))
                        new_tilt = float(np.clip(step_to(tilt_now, tilt_err), self.TILT_MIN, self.TILT_MAX))

                        self.target_pan = new_pan
                        self.target_tilt = new_tilt

                        # Send command to hardware (if connected); send_serial_command is defensive
                        try:
                            if self.ser is not None and getattr(self.ser, "is_open", False):
                                self.send_serial_command()
                        except Exception:
                            pass
                    except Exception as e:
                        try:
                            self.enhancer.log_serial_output(f"_home_step exception: {e}", fire=False)
                        except Exception:
                            pass

                # Start the timer and do an immediate step
                try:
                    self._go_home_timer.timeout.connect(_home_step)
                    self._go_home_timer.start()
                    QTimer.singleShot(0, _home_step)
                    self.enhancer.log_serial_output(f"Started host-side interpolated Go Home (speed_deg/s={speed_deg_per_sec:.3f}, step_deg={self._go_home_step_deg:.3f})", fire=False)
                except Exception as e:
                    self.enhancer.log_serial_output(f"Error starting home interpolation timer: {e}", fire=False)
            except Exception:
                pass
        except Exception as e:
            self.enhancer.log_serial_output(f"Error performing host-side Go Home: {e}", fire=False)

        # --- RESTORE PHASE ---
        try:
            # After delay, start fresh tracking from home position
            def _complete_go_home():
                try:
                    setattr(self, "_in_go_home", False)
                    setattr(self, "tracking_active", True)
                    setattr(self, "aiming_active", True)
                    setattr(self, "target_x", None)
                    setattr(self, "target_y", None)
                    # CRITICAL: Clear detection history so we don't immediately re-lock to old target
                    if hasattr(self, "last_detections"):
                        self.last_detections.clear()
                    # Reset last_seen_time so hold window doesn't trigger
                    setattr(self, "last_seen_time", 0.0)
                    getattr(self.override_status_label, "setText", lambda x: None)("")
                    self.enhancer.log_serial_output("Go Home complete — fresh tracking started at home (detection history cleared)", fire=False)
                except Exception as e:
                    print(f"go_home completion error: {e}")
            
            QTimer.singleShot(int(suspend_time * 1000), _complete_go_home)
        except Exception:
            pass



    def apply_new_limits(self):
        """Update servo min/max limits from UI and save to settings."""
        # read safely from widgets
        try:
            self.PAN_MIN = self._safe_int_widget_value("pan_min_input", self.PAN_MIN)
        except Exception:
            pass
        try:
            self.PAN_MAX = self._safe_int_widget_value("pan_max_input", self.PAN_MAX)
        except Exception:
            pass
        try:
            self.TILT_MIN = self._safe_int_widget_value("tilt_min_input", self.TILT_MIN)
        except Exception:
            pass
        try:
            self.TILT_MAX = self._safe_int_widget_value("tilt_max_input", self.TILT_MAX)
        except Exception:
            pass

        # keep as floats so any fractional targets are preserved
        self.target_pan = float(np.clip(self.target_pan, self.PAN_MIN, self.PAN_MAX))
        self.target_tilt = float(
            np.clip(self.target_tilt, self.TILT_MIN, self.TILT_MAX)
        )

        try:
            self._safe_widget_call(
                "home_pan_input", "setRange", self.PAN_MIN, self.PAN_MAX
            )
        except Exception:
            pass
        try:
            self._safe_widget_call(
                "home_tilt_input", "setRange", self.TILT_MIN, self.TILT_MAX
            )
        except Exception:
            pass

        self.enhancer.log_serial_output(
            f"New Limits Applied → PAN[{self.PAN_MIN}, {self.PAN_MAX}], TILT[{self.TILT_MIN}, {self.TILT_MAX}]",
            fire=False,
        )

        try:
            if self.ser and getattr(self.ser, "is_open", False):
                cmd = f"LIMITS P{self.PAN_MIN}X{self.PAN_MAX}Y{self.TILT_MIN}Z{self.TILT_MAX}\n"
                try:
                    self.ser.write(cmd.encode("utf-8"))
                    self.enhancer.log_serial_output(f"SENT: {cmd.strip()}", fire=False)
                except Exception as e:
                    self.enhancer.log_serial_output(
                        f"Error sending limits: {e}", fire=False
                    )
        except Exception:
            pass

        try:
            self.save_settings()
        except Exception:
            pass

    def _add_crosshair_and_scope(self, frame):
        """Add sniper scope crosshair and unified HUD overlay.
        
        ALL HUD elements are drawn here using a grid-based layout.
        
        CRITICAL: Do NOT add fallback placeholders like '???'.
        All HUD data must be required and validated at the source (update_frame).
        If a key is missing, the code SHOULD crash to expose the bug.
        """
        try:
            h, w = frame.shape[:2]
            center_x, center_y = w // 2, h // 2
            
            # Get HUD constants (these are always initialized in __init__)
            HUD_CYAN = self.HUD_CYAN
            HUD_ORANGE = self.HUD_ORANGE
            HUD_RED = self.HUD_RED
            HUD_GREEN = self.HUD_GREEN
            HUD_GRAY = self.HUD_GRAY
            HUD_WHITE = self.HUD_WHITE
            HUD_BLACK = self.HUD_BLACK
            HUD_YELLOW = self.HUD_YELLOW
            
            HUD_FONT = self.HUD_FONT
            HUD_MARGIN = self.HUD_MARGIN
            HUD_LINE_HEIGHT = self.HUD_LINE_HEIGHT
            HUD_PADDING = self.HUD_PADDING
            
            # Font styles - direct access, no fallbacks
            FONT_HEADER = self.HUD_FONT_HEADER
            FONT_STATUS = self.HUD_FONT_STATUS
            FONT_DEBUG = self.HUD_FONT_DEBUG
            FONT_ALERT = self.HUD_FONT_ALERT
            
            # HUD data - direct access, MUST exist (validated in update_frame)
            hud_data = self.hud_data
            
            # Extract required values - NO .get(), crash if missing
            pan = float(hud_data['pan'])
            tilt = float(hud_data['tilt'])
            fps = float(hud_data['fps'])
            detection_mode = str(hud_data['detection_mode'])
            resolution = str(hud_data['resolution'])
            idle_mode = hud_data['idle_mode']
            safety_state = bool(hud_data['safety_state'])
            trigger_fired = bool(hud_data['trigger_fired'])
            quick_strike_active = bool(hud_data['quick_strike_active'])
            has_target = bool(hud_data['has_target'])
            debug_lines = hud_data['debug_lines']
            recording = bool(hud_data['recording'])
            
            # Get tracking/aiming state
            tracking = getattr(self, 'tracking_active', False)
            aiming = getattr(self, 'aiming_active', False)
            
            # Get text background opacity
            text_bg_opacity = getattr(self, 'text_bg_opacity_slider_scope', None)
            bg_opacity = text_bg_opacity.value() / 100.0 if text_bg_opacity is not None else 0.7
            
            # ========== HELPER: Draw text with background ==========
            def draw_text_with_bg(text, pos, font_style, color, align='left'):
                scale = font_style['scale']
                thickness = font_style['thickness']
                text_size = cv2.getTextSize(text, HUD_FONT, scale, thickness)[0]
                
                if align == 'center':
                    x = pos[0] - text_size[0] // 2
                elif align == 'right':
                    x = pos[0] - text_size[0]
                else:
                    x = pos[0]
                y = pos[1]
                
                if bg_opacity > 0:
                    overlay = frame.copy()
                    cv2.rectangle(overlay,
                                  (x - HUD_PADDING, y - text_size[1] - HUD_PADDING),
                                  (x + text_size[0] + HUD_PADDING, y + HUD_PADDING),
                                  HUD_BLACK, -1)
                    cv2.addWeighted(overlay, bg_opacity, frame, 1 - bg_opacity, 0, frame)
                
                cv2.putText(frame, text, (x, y), HUD_FONT, scale, HUD_BLACK, thickness + 1, cv2.LINE_AA)
                cv2.putText(frame, text, (x, y), HUD_FONT, scale, color, thickness, cv2.LINE_AA)
            
            # ========== CROSSHAIR DRAWING ==========
            if aiming and has_target:
                crosshair_color = HUD_GREEN
            elif tracking:
                crosshair_color = HUD_CYAN
            else:
                crosshair_color = HUD_GRAY
            
            # Scope settings with safe defaults
            crosshair_length_slider = getattr(self, 'crosshair_length_slider', None)
            crosshair_length = int(min(w, h) * (crosshair_length_slider.value() / 100.0)) if crosshair_length_slider else int(min(w, h) * 0.30)
            
            gap_slider = getattr(self, 'gap_slider', None)
            gap = gap_slider.value() if gap_slider else 10
            
            thickness_slider = getattr(self, 'crosshair_thickness_slider', None)
            crosshair_thickness = thickness_slider.value() if thickness_slider else 2
            
            radius_slider = getattr(self, 'scope_radius_percent_slider', None)
            scope_radius_pct = radius_slider.value() / 100.0 if radius_slider else 0.35
            
            corner_slider = getattr(self, 'corner_size_slider', None)
            corner_size = corner_slider.value() if corner_slider else 40
            
            # Horizontal lines
            cv2.line(frame, (center_x - crosshair_length, center_y), (center_x - gap, center_y), crosshair_color, crosshair_thickness)
            cv2.line(frame, (center_x + gap, center_y), (center_x + crosshair_length, center_y), crosshair_color, crosshair_thickness)
            
            # Vertical lines
            cv2.line(frame, (center_x, center_y - crosshair_length), (center_x, center_y - gap), crosshair_color, crosshair_thickness)
            cv2.line(frame, (center_x, center_y + gap), (center_x, center_y + crosshair_length), crosshair_color, crosshair_thickness)
            
            # Center dot
            cv2.circle(frame, (center_x, center_y), 3, crosshair_color, -1)
            
            # Scope ring
            scope_radius = int(min(h, w) * scope_radius_pct)
            cv2.circle(frame, (center_x, center_y), scope_radius, (100, 100, 100), 3)
            
            # Vignette
            mask = np.zeros((h, w, 3), dtype=np.uint8)
            cv2.circle(mask, (center_x, center_y), scope_radius, (255, 255, 255), -1)
            vignette = mask.astype(float) / 255.0
            vignette_slider = getattr(self, 'vignette_opacity_slider_scope', None)
            darkness = vignette_slider.value() / 100.0 if vignette_slider else 0.7
            min_brightness = 1.0 - darkness
            frame = (frame.astype(float) * (min_brightness + (1.0 - min_brightness) * vignette)).astype(np.uint8)
            
            # Corner markers
            corners = [(corner_size, corner_size), (w - corner_size, corner_size),
                       (corner_size, h - corner_size), (w - corner_size, h - corner_size)]
            for cx, cy in corners:
                cv2.line(frame, (cx - 15, cy), (cx + 15, cy), HUD_GRAY, 2)
                cv2.line(frame, (cx, cy - 15), (cx, cy + 15), HUD_GRAY, 2)
            
            # Distance rings
            for radius in [scope_radius // 2, scope_radius * 3 // 4]:
                cv2.circle(frame, (center_x, center_y), radius, (80, 80, 80), 1)
            
            # ========== HUD ELEMENTS (Grid Layout) ==========
            
            # --- TOP-LEFT: Debug info (only when enabled) ---
            if debug_lines:
                y_pos = HUD_MARGIN + 15
                for line in debug_lines:
                    draw_text_with_bg(line, (HUD_MARGIN, y_pos), FONT_DEBUG, HUD_GRAY)
                    y_pos += 18
            
            # --- TOP-CENTER: Quick Strike Alert ---
            if quick_strike_active:
                strike_text = "QUICK STRIKE"
                text_size = cv2.getTextSize(strike_text, HUD_FONT, FONT_ALERT['scale'], FONT_ALERT['thickness'])[0]
                text_x = (w - text_size[0]) // 2
                text_y = 50
                
                overlay = frame.copy()
                cv2.rectangle(overlay, (text_x - 10, text_y - text_size[1] - 10),
                              (text_x + text_size[0] + 10, text_y + 10), HUD_ORANGE, -1)
                cv2.addWeighted(overlay, 0.8, frame, 0.2, 0, frame)
                cv2.putText(frame, strike_text, (text_x, text_y), HUD_FONT, 
                           FONT_ALERT['scale'], HUD_WHITE, FONT_ALERT['thickness'], cv2.LINE_AA)
            
            # --- TOP-RIGHT: Status indicators ---
            # Status (Green=locked, Cyan=tracking, Gray=idle)
            if has_target and aiming:
                status_text = "LOCKED"
                status_color = HUD_GREEN
            elif tracking:
                status_text = "TRACKING"
                status_color = HUD_CYAN
            else:
                status_text = "READY"
                status_color = HUD_GRAY
            draw_text_with_bg(status_text, (w - HUD_MARGIN, HUD_MARGIN + 15), FONT_HEADER, status_color, align='right')
            
            # FPS (Gray - debug info)
            if fps > 0:
                draw_text_with_bg(f"FPS: {fps:.0f}", (w - HUD_MARGIN, HUD_MARGIN + 38), FONT_DEBUG, HUD_GRAY, align='right')
            
            # Safety (Green=safe, Red=armed)
            safety_text = "SAFE" if safety_state else "ARMED"
            safety_color = HUD_GREEN if safety_state else HUD_RED
            draw_text_with_bg(safety_text, (w - HUD_MARGIN, HUD_MARGIN + 58), FONT_STATUS, safety_color, align='right')
            
            # Fire indicator (Red - danger only)
            if trigger_fired:
                draw_text_with_bg("FIRE", (w - HUD_MARGIN, HUD_MARGIN + 78), FONT_STATUS, HUD_RED, align='right')
            
            # --- BOTTOM-LEFT: Mode info ---
            bottom_y = h - HUD_MARGIN
            
            # Resolution (Gray - debug)
            draw_text_with_bg(f"RES: {resolution}", (HUD_MARGIN, bottom_y), FONT_DEBUG, HUD_GRAY)
            
            # Detection mode (Cyan - normal status)
            draw_text_with_bg(f"MODE: {detection_mode}", (HUD_MARGIN, bottom_y - 20), FONT_STATUS, HUD_CYAN)
            
            # Idle/Tracking status
            if idle_mode and str(idle_mode).lower() != 'none':
                status_indicator = f"IDLE: {str(idle_mode).upper()}"
                indicator_color = HUD_GREEN
            elif tracking and aiming:
                status_indicator = "TRACKING"
                indicator_color = HUD_CYAN
            else:
                status_indicator = "STANDBY"
                indicator_color = HUD_GRAY
            draw_text_with_bg(status_indicator, (HUD_MARGIN, bottom_y - 40), FONT_STATUS, indicator_color)
            
            # Recording (Red - important alert)
            if recording:
                draw_text_with_bg("REC", (HUD_MARGIN, bottom_y - 60), FONT_STATUS, HUD_RED)
            
            # --- BOTTOM-RIGHT: Pan/Tilt (ALWAYS DRAWN - Yellow for values) ---
            # This is UNCONDITIONAL - no if, no check, always visible
            coord_text = f"Pan: {pan:.1f} | Tilt: {tilt:.1f}"
            draw_text_with_bg(coord_text, (w - HUD_MARGIN, h - HUD_MARGIN), FONT_STATUS, HUD_YELLOW, align='right')
            
            return frame
            
        except Exception as e:
            print(f"[HUD ERROR] _add_crosshair_and_scope: {e}")
            import traceback
            traceback.print_exc()
            return frame

    def update_frame(self):
        # NOTE: Idle button now uses direct click detection (ClickDetectButton class)
        # No need for polling - direct mouse events work reliably
        
        # ========== RESOLUTION POLLING - REMOVED (Dec 2024) ==========\n        # Camera resolution selector removed from UI\n        # Camera now uses fixed 1280x720 resolution set in __init__\n        # No polling or dynamic resolution changes occur\n        \n        # POLLING: Check idle behavior combo state changes (bypass Qt signals)
        # This detects when user changes the idle behavior dropdown without clicking the button
        # DEC14: DISABLED - Causing recursion error. Will reinvestigate separately.
        # try:
        #     idle_combo = getattr(self, "idle_behavior_combo", None)
        #     if idle_combo is not None:
        #         try:
        #             current_idx = idle_combo.currentIndex()
        #             current_text = idle_combo.currentText()
        #             
        #             # Initialize on first check
        #             if not hasattr(self, "_last_idle_behavior_combo_index"):
        #                 self._last_idle_behavior_combo_index = current_idx
        #                 # Update the runtime attribute to match combo (for consistency)
        #                 try:
        #                     self.idle_behavior = current_text.lower() if current_text else "rest"
        #                 except Exception:
        #                     pass
        #                 print(f"[IDLE-POLLING] Init idle behavior: {current_text} (idx={current_idx})")
        #             # Detect change in combo selection
        #             elif current_idx != self._last_idle_behavior_combo_index:
        #                 old_idx = self._last_idle_behavior_combo_index
        #                 self._last_idle_behavior_combo_index = current_idx
        #                 print(f"[IDLE-POLLING] Idle behavior changed: idx {old_idx} -> {current_idx} (text: {current_text})")
        #                 
        #                 # Update runtime attribute for consistency
        #                 try:
        #                     self.idle_behavior = current_text.lower() if current_text else "rest"
        #                 except Exception:
        #                     pass
        #                 
        #                 # User changed the combo - automatically activate that mode
        #                 try:
        #                     idle_modes = getattr(self, "idle_modes", None)
        #                     if idle_modes is not None:
        #                         # Convert combo text to lowercase mode name
        #                         new_mode = current_text.lower()
        #                         old_mode = idle_modes.get_mode()
        #                         idle_modes.set_mode(new_mode)
        #                         print(f"[IDLE-POLLING] Activated: {new_mode} (was: {old_mode})")
        #                         self._last_idle_mode_state = new_mode
        #                         try:
        #                             if getattr(self, "enhancer", None):
        #                                 self.enhancer.log_serial_output(
        #                                     f"[IDLE] Activated {new_mode.upper()} mode via combo selection", 
        #                                     fire=False
        #                                 )
        #                         except Exception:
        #                             pass
        #                 except Exception as combo_err:
        #                     print(f"[IDLE-POLLING ERROR] Could not activate mode: {str(combo_err)}")
        #                     import traceback
        #                     traceback.print_exc()
        #         except RecursionError:
        #             print(f"[IDLE-POLLING ERROR] RecursionError in idle combo")
        #         except Exception as e:
        #             print(f"[IDLE-POLLING ERROR] Combo state: {str(e)}")
        #             import traceback
        #             traceback.print_exc()
        # except RecursionError:
        #     print(f"[IDLE-POLLING FATAL] RecursionError in idle combo check")
        # except Exception as e:
        #     print(f"[IDLE-POLLING FATAL] Combo check: {str(e)}")
        #     import traceback
        #     traceback.print_exc()
        # POLLING: Detect idle mode state changes (on/off) and sync button text
        # This ensures button always shows correct state regardless of how idle mode is toggled
        # DEC14: DISABLED - Causing recursion error. Will reinvestigate separately.
        # try:
        #     try:
        #         idle_modes = getattr(self, "idle_modes", None)
        #         if idle_modes is not None:
        #             current_idle_mode = idle_modes.get_mode()
        #             
        #             # Initialize on first check (set both to None initially)
        #             if not hasattr(self, '_idle_mode_state_initialized'):
        #                 self._idle_mode_state_initialized = True
        #                 self._last_idle_mode_state = current_idle_mode  # Initialize tracking
        #                 print(f"[IDLE-STATE-POLL] Init idle mode: {current_idle_mode if current_idle_mode else 'OFF'}")
        #             
        #             # Detect change in idle mode state
        #             if current_idle_mode != self._last_idle_mode_state:
        #                 # Idle mode state changed!
        #                 old_state = self._last_idle_mode_state
        #                 self._last_idle_mode_state = current_idle_mode
        #                 
        #                 print(f"[IDLE-STATE-POLL] State changed: {old_state} -> {current_idle_mode}")
        #                 
        #                 # Sync button text to match current state
        #                 try:
        #                     btn = getattr(self, "idle_mode_toggle_btn", None)
        #                     if btn is not None:
        #                         if current_idle_mode is None:
        #                             # Idle is OFF - button should say "Enable"
        #                             btn.setText("Enable Idle Mode")
        #                             btn.setChecked(False)
        #                         else:
        #                             # Idle is ON - button should say "Disable"
        #                             btn.setText("Disable Idle Mode")
        #                             btn.setChecked(True)
        #                         btn.repaint()
        #                         btn.update()
        #                         print(f"[IDLE-STATE-POLL] Button text synced")
        #                 except Exception as btn_err:
        #                     print(f"[IDLE-STATE-POLL] Could not sync button: {str(btn_err)}")
        #                 
        #                 try:
        #                     if getattr(self, "enhancer", None):
        #                         if current_idle_mode is None:
        #                             self.enhancer.log_serial_output("[IDLE-STATE] Mode turned OFF", fire=False)
        #                         else:
        #                             self.enhancer.log_serial_output(
        #                                 f"[IDLE-STATE] Mode ON: {current_idle_mode.upper()}", 
        #                                 fire=False
        #                             )
        #                 except Exception:
        #                     pass
        #     except RecursionError:
        #         print(f"[IDLE-STATE-POLL RECURSION] Detected and skipped to prevent stack overflow")
        # except RecursionError:
        #     print(f"[IDLE-STATE-POLL RECURSION FATAL] Detected and caught")
        # except Exception as e:
        #     print(f"[IDLE-STATE-POLL ERROR] {str(e)}")
        #     import traceback
        #     traceback.print_exc()
        
        # Check if camera needs to be re-opened (either from start_tracking or resolution change)
        # FIX DEC14: CRITICAL - Use background thread to prevent UI freeze!
        # OpenCV camera opening can block for 5-30 seconds on slow/unavailable cameras
        if getattr(self, "_camera_open_needed", False) and getattr(self, "tracking_active", False):
            try:
                self._camera_open_needed = False
                # Open camera in background thread to avoid blocking main Qt event loop
                import threading
                def _open_camera_bg():
                    try:
                        cap = self.open_camera(range(0, 5))
                        if cap is not None and getattr(cap, "isOpened", lambda: False)():
                            self.cap = cap
                            try:
                                self.enhancer.log_serial_output(
                                    f"Camera opened successfully: {self.frame_width}x{self.frame_height}",
                                    fire=False
                                )
                            except Exception:
                                pass
                        else:
                            try:
                                self.enhancer.log_serial_output(
                                    "Camera opening failed - device not available",
                                    fire=False
                                )
                            except Exception:
                                pass
                    except Exception as e:
                        try:
                            self.enhancer.log_serial_output(
                                f"[CAMERA ERROR] {str(e)}",
                                fire=False
                            )
                        except Exception:
                            pass
                
                # Start camera opening in background thread (daemon so it doesn't block shutdown)
                bg_thread = threading.Thread(target=_open_camera_bg, daemon=True)
                bg_thread.start()
            except Exception as e:
                try:
                    self.enhancer.log_serial_output(
                        f"[CAMERA REOPEN ERROR] {str(e)}",
                        fire=False
                    )
                except Exception:
                    pass
        
        # BULLETPROOF FIX: Validate state at the start of every frame
        # This catches and auto-corrects corruption from any source
        # DISABLED DEC14: Causing recursion error during startup
        # try:
        #     if self.state_manager:
        #         is_valid, problems = self.state_manager.validate_state_consistency()
        #         if not is_valid:
        #             for problem in problems:
        #                 self.enhancer.log_serial_output(f"[STATE FIX] {problem}", fire=False)
        # except Exception:
        #     pass
        
        # ========== FIXED: ADD tracking_active/aiming_active SYNC CHECK ==========
        # Prevent inconsistent state where tracking is active but aiming is not
        # (would cause turret to detect target but not move servos)
        try:
            tracking = getattr(self, "tracking_active", False)
            aiming = getattr(self, "aiming_active", False)
            # If tracking active but aiming not, sync them
            if tracking and not aiming:
                self.aiming_active = True  # Auto-enable aiming when tracking starts
                try:
                    if hasattr(self, "aiming_btn"):
                        self.aiming_btn.setChecked(True)
                except Exception:
                    pass
                try:
                    if hasattr(self, "enhancer"):
                        self.enhancer.log_serial_output(
                            "[AUTO-SYNC] Aiming auto-enabled with tracking",
                            fire=False
                        )
                except Exception:
                    pass
        except Exception:
            pass
        
        # Local initializations to help static analysis and ensure defined locals
        frame1 = None
        frame2 = None
        boxes = []
        new_pan = None
        new_tilt = None
        # Ensure debug error variables are always defined for all code paths
        err_x = 0.0
        err_y = 0.0

        # If we were performing a user-initiated Go Home move, and the
        # suspend period has expired, clear the go-home flag and ensure
        # the system state reflects the final home position. This prevents
        # the detector from immediately overriding the user intent.
        if getattr(self, "_in_go_home", False):
            try:
                self._in_go_home = False
                # make sure hold/last-sent values are set to the home angles
                self.last_known_pan = int(getattr(self, "target_pan", getattr(self, "last_sent_pan", self.prev_pan_angle)))
                self.last_known_tilt = int(getattr(self, "target_tilt", getattr(self, "last_sent_tilt", self.prev_tilt_angle)))
                self.last_sent_pan = int(getattr(self, "last_known_pan", getattr(self, "last_sent_pan", self.prev_pan_angle)))
                self.last_sent_tilt = int(getattr(self, "last_known_tilt", getattr(self, "last_sent_tilt", self.prev_tilt_angle)))
                # DISABLED: Don't auto-resume - let user control with buttons
                # self.tracking_active = True
                # self.aiming_active = True
                self.enhancer.log_serial_output("Go Home complete — awaiting user input.", fire=False)
            except Exception:
                pass
        # Auto-resume tracking/aiming if detection found after idle/home
        # DISABLED: Only resume if user explicitly pressed the button
        # if not self.tracking_active and hasattr(self, "last_detections") and self.last_detections:
        #     self.tracking_active = True
        #     self.aiming_active = True
        #     self.enhancer.log_serial_output("Detection found after idle — auto-resuming tracking/aiming.", fire=False)

        # Helper to safely set QLabel pixmaps on the Qt main thread. Scheduling
        # via QTimer.singleShot avoids painting from non-GUI threads and reduces
        # QPainter warnings when labels haven't fully initialized.
        def _queue_set_pixmap(lbl, pm):
            try:
                if lbl is None or pm is None:
                    return False

                def _do_set(pm=pm, lbl=lbl):
                    try:
                        if getattr(lbl, "setPixmap", None):
                            lbl.setPixmap(pm)
                    except Exception as _e:
                        try:
                            import traceback

                            tb = traceback.format_exc()
                            if getattr(self, "enhancer", None):
                                try:
                                    self.enhancer.log_serial_output(
                                        f"setPixmap exception: {_e}\n{tb}", fire=False
                                    )
                                except Exception:
                                    print("setPixmap exception:", _e)
                                    print(tb)
                            else:
                                print("setPixmap exception:", _e)
                                print(tb)
                        except Exception:
                            pass

                try:
                    QTimer.singleShot(0, _do_set)
                    return True
                except Exception:
                    # fallback to direct call if scheduling fails
                    _do_set()
                    return True
            except Exception:
                return False

        # Try to read frame safely using helper. If camera not available, bail early.
        try:
            ok, frame1 = self._cap_read()
        except Exception:
            ok, frame1 = False, None
        if not ok or frame1 is None:
            # update a status label if available and return without processing
            try:
                self._safe_widget_call("lblStatus", "setText", "Camera not available")
            except Exception:
                pass
            return

        if not self.cap or not getattr(self.cap, "isOpened", lambda: False)():
            try:
                # read home inputs (integers) but store as floats for accumulation
                self.target_pan = float(
                    self._safe_int_widget_value("home_pan_input", self.HOME_PAN)
                )
            except Exception:
                # fall back to class defaults if widget access fails
                try:
                    self.target_pan = float(getattr(self, "HOME_PAN", 90))
                except Exception:
                    self.target_pan = 90.0
            try:
                self.target_tilt = float(
                    self._safe_int_widget_value("home_tilt_input", self.HOME_TILT)
                )
            except Exception:
                try:
                    self.target_tilt = float(getattr(self, "HOME_TILT", 40))
                except Exception:
                    self.target_tilt = 40.0
            self.trigger_fired = False
            # create a placeholder blank frame so downstream drawing code
            # can always assume `frame1` is an image (reduces analyzer and
            # runtime None issues). Use a conservative default size.
            try:
                frame1 = np.zeros((480, 640, 3), dtype=np.uint8)
                frame2 = frame1.copy()
            except Exception:
                frame1 = None
                frame2 = None
            # continue to drawing/convert for display
        else:
            # Read the latest camera frame (frame1) before running detection
            try:
                ret1, frame1 = self._cap_read()
            except Exception:
                ret1, frame1 = False, None
            if not ret1 or frame1 is None:
                return
            # help static analyzer: cast frame to ndarray type when available
            try:
                frame1 = cast(np.ndarray, frame1)
            except Exception:
                pass
            try:
                if (
                    frame1 is not None
                    and getattr(self, "flip_checkbox", None)
                    and self.flip_checkbox.isChecked()
                ):
                    frame1 = cv2.flip(frame1, 1)
            except Exception:
                pass

        # Normalize frame1 to ndarray to prevent passing None to cv2 calls
        try:
            frame1 = self._ensure_frame(frame1)
        except Exception:
            frame1 = np.zeros((480, 640, 3), dtype=np.uint8)
        
        # ========== RESOLUTION CONFIGURATION - DO NOT MODIFY ==========
        # WARNING: DO NOT update frame_width/height here on every frame!
        # 
        # Resolution is set ONCE when camera opens (see open_camera() around line 12353).
        # The camera opening code already:
        #   1. Requests the configured resolution (from frame_ratio_setting)
        #   2. Gets the ACTUAL resolution the camera provides
        #   3. Updates self.frame_width and self.frame_height with actual values
        #   4. Logs the resolution for debugging
        # 
        # DO NOT add code here to recalculate resolution from frame.shape every frame because:
        #   - It's inefficient (wastes CPU every frame)
        #   - It's redundant (camera resolution doesn't change mid-stream)
        #   - It contradicts the FIXED resolution design (see line 1358-1360)
        #   - It creates confusion about source of truth for resolution
        # 
        # If you need to change resolution:
        #   - Modify lines 1358-1360 (frame_ratio_setting, frame_width, frame_height)
        #   - Restart the camera (it will read new settings from those lines)
        #   - See CAMERA_RESOLUTION_GUIDE.md for detailed instructions
        # 
        # The frame_width/height values are the SOURCE OF TRUTH for all calculations
        # including deadzone, detection regions, servo angle calculations, etc.
        # They are set once at camera open and remain stable during operation.

            # If we were performing a user-initiated Go Home move, and the
            # suspend period has expired, clear the go-home flag and ensure
            # the system state reflects the final home position. This prevents
            # the detector from immediately overriding the user intent.
            if getattr(self, "_in_go_home", False):
                try:
                    self._in_go_home = False
                    # make sure hold/last-sent values are set to the home angles
                    self.last_known_pan = int(
                        getattr(
                            self,
                            "target_pan",
                            getattr(self, "last_sent_pan", self.prev_pan_angle),
                        )
                    )
                    self.last_known_tilt = int(
                        getattr(
                            self,
                            "target_tilt",
                            getattr(self, "last_sent_tilt", self.prev_tilt_angle),
                        )
                    )
                    self.last_sent_pan = int(
                        getattr(
                            self,
                            "last_known_pan",
                            getattr(self, "last_sent_pan", self.prev_pan_angle),
                        )
                    )
                    self.last_sent_tilt = int(
                        getattr(
                            self,
                            "last_known_tilt",
                            getattr(self, "last_sent_tilt", self.prev_tilt_angle),
                        )
                    )
                    # Keep prev angles as floats to preserve fractional adjustments
                    try:
                        self.prev_pan_angle = float(self.last_sent_pan)
                        self.prev_tilt_angle = float(self.last_sent_tilt)
                    except Exception:
                        self.prev_pan_angle = float(int(self.last_sent_pan))
                        self.prev_tilt_angle = float(int(self.last_sent_tilt))
                except Exception:
                    pass
        # If manual operator override suppression is active, treat like a transient suspend
        # We also automatically clear the manual_override flag when the suppression
        # window expires so the tracker can resume without requiring another
        # button release event (previous behavior could leave manual_override True
        # indefinitely until another release occurred).
        now_ts = time.time()
        if getattr(self, "_manual_override_until", 0) > now_ts:
            # while suppression active, prevent detection/tracker from updating
            # target_pan/tilt based on detections; we still run detection for UI but
            # ignore its output when computing new target angles.
            self._manual_override_active = True
        else:
            # suppression expired
            self._manual_override_active = False
            # ========== FIXED: CLEAR manual_override FLAG UNCONDITIONALLY ==========
            # Previously only cleared if tracking_was_active, causing users to get stuck
            # in manual override mode. Now always clear when timeout expires.
            if getattr(self, "manual_override", False):
                try:
                    self.manual_override = False
                    if getattr(self, "tracking_was_active", False):
                        self.tracking_active = True
                        # FIX: Always clear tracking_was_active flag after resume to prevent double-resume attempts
                        self.tracking_was_active = False
                        try:
                            if hasattr(self, "enhancer"):
                                self.enhancer.log_serial_output(
                                    "Resumed tracking after manual override timeout",
                                    fire=False,
                                )
                        except Exception:
                            pass
                except Exception:
                    # Ensure manual_override is cleared in case of unexpected errors
                    try:
                        self.manual_override = False
                    except Exception:
                        pass

                # BULLETPROOF FIX: No wait for suppression - immediately clear go_home when done
                # This allows detection to resume immediately
                try:
                    if getattr(self, "_in_go_home", False):
                        # Don't check suppress_until - just check if steps finished
                        finished_steps = (
                            getattr(self, "_go_home_step", 0)
                            >= getattr(self, "_go_home_step_total", 0)
                            if getattr(self, "_go_home_step_total", 0) > 0
                            else True
                        )
                        if finished_steps:
                            try:
                                self._in_go_home = False
                                self.last_known_pan = int(
                                    getattr(
                                        self,
                                        "target_pan",
                                        getattr(
                                            self, "last_sent_pan", self.prev_pan_angle
                                        ),
                                    )
                                )
                                self.last_known_tilt = int(
                                    getattr(
                                        self,
                                        "target_tilt",
                                        getattr(
                                            self, "last_sent_tilt", self.prev_tilt_angle
                                        ),
                                    )
                                )
                                self.last_sent_pan = int(
                                    getattr(
                                        self,
                                        "last_known_pan",
                                        getattr(
                                            self, "last_sent_pan", self.prev_pan_angle
                                        ),
                                    )
                                )
                                self.last_sent_tilt = int(
                                    getattr(
                                        self,
                                        "last_known_tilt",
                                        getattr(
                                            self, "last_sent_tilt", self.prev_tilt_angle
                                        ),
                                    )
                                )
                                try:
                                    self.prev_pan_angle = float(self.last_sent_pan)
                                    self.prev_tilt_angle = float(self.last_sent_tilt)
                                except Exception:
                                    pass
                            except Exception:
                                pass
                except Exception:
                    pass

        # Update small override status label to keep operator informed
        try:
            lbl = getattr(self, "override_status_label", None)
            if lbl:
                if getattr(self, "_in_go_home", False) or (
                    getattr(self, "_suspend_tracking_until", 0) > time.time()
                ):
                    lbl.setText("Go Home: active")
                elif getattr(self, "_manual_override_active", False) or getattr(
                    self, "manual_override", False
                ):
                    lbl.setText("Manual Override: active")
                elif getattr(self, "_hold_infinite_active", False) or getattr(
                    self, "hold_infinite", False
                ):
                    lbl.setText("Hold: active")
                else:
                    lbl.setText("")
        except Exception:
            pass

        # Decide whether we should run detection even if tracking is stopped
        manual_auto = False
        try:
            manual_auto = bool(
                getattr(self, "manual_auto_fire_checkbox", None)
                and self.manual_auto_fire_checkbox.isChecked()
            )
        except Exception:
            manual_auto = False

        if not (self.tracking_active or manual_auto):
            # No detection running (fully stopped)
            self.last_detections = []
            self.trigger_fired = False
        else:
            # ========== CRITICAL FIX: CAMERA FALLBACK RETRY LOGIC ==========
            # If camera read fails, retry up to 3 times before suppressing detection
            # This prevents turret locking if camera is briefly unavailable
            ret2, frame2 = False, None
            camera_retry_count = 0
            max_camera_retries = 3
            while not ret2 and camera_retry_count < max_camera_retries:
                try:
                    ret2, frame2 = self._cap_read()
                    if ret2 and frame2 is not None:
                        break
                    camera_retry_count += 1
                except Exception:
                    camera_retry_count += 1
            
            if not ret2 or frame2 is None:
                return
            try:
                if (
                    getattr(self, "flip_checkbox", None)
                    and self.flip_checkbox.isChecked()
                ):
                    frame2 = cv2.flip(frame2, 1)
            except Exception:
                pass
            try:
                frame2 = cast(np.ndarray, frame2)
            except Exception:
                pass

            try:
                frame2 = self._ensure_frame(frame2)
            except Exception:
                frame2 = np.zeros((480, 640, 3), dtype=np.uint8)

            # Ensure numeric defaults for pan/tilt blending variables
            try:
                new_pan = (
                    float(new_pan)
                    if new_pan is not None
                    else float(getattr(self, "prev_pan_angle", 90))
                )
            except Exception:
                new_pan = float(getattr(self, "prev_pan_angle", 90))
            try:
                new_tilt = (
                    float(new_tilt)
                    if new_tilt is not None
                    else float(getattr(self, "prev_tilt_angle", 40))
                )
            except Exception:
                new_tilt = float(getattr(self, "prev_tilt_angle", 40))

        # --- Detection Mode Logic ---
        detection_mode = int(self._safe_current_index("detection_mode_combo", 0) or 0)

        # BULLETPROOF FIX: NEVER SUPPRESS DETECTION
        # Detection should ALWAYS run - even during home moves
        # This ensures immediate re-acquisition when turret stops moving
        # The suppression variables are DEPRECATED and should be removed
        boxes = []
        # Detection always runs now - no suppression windows
        suppressed = False  # Always run detection
        # diagnostics for counts (used in throttled logging)
        contours_raw = 0
        contours_filtered = 0
        fg_nonzero = 0
        yolo_boxes_len = 0

        # Brief diagnostic when debug mode is enabled: report detection mode and counts
        try:
            if (
                getattr(self, "debug_checkbox", None)
                and getattr(self.debug_checkbox, "isChecked", lambda: False)()
            ):
                try:
                    dm = int(
                        self._safe_current_index("detection_mode_combo", 0) or 0
                    )
                except Exception:
                    dm = 0
                try:
                    model_loaded = bool(
                        getattr(self.yolo_detector, "model_loaded", False)
                    )
                except Exception:
                    model_loaded = False
                try:
                    back_exists = self.backSub is not None
                except Exception:
                    back_exists = False
                try:
                    if hasattr(self, "enhancer"):
                        self.enhancer.log_serial_output(
                            f"[DETECT DIAG] mode={dm} yolo_loaded={model_loaded} backSub={back_exists}",
                            fire=False,
                        )
                except Exception:
                    pass
        except Exception:
            pass

        if detection_mode == 0:  # Frame Difference
            if suppressed:
                boxes = []
            else:
                # Ensure frames are valid ndarrays and have matching shapes before absdiff
                try:
                    frame1 = self._ensure_frame(frame1)
                except Exception:
                    frame1 = np.zeros((480, 640, 3), dtype=np.uint8)
                try:
                    frame2 = self._ensure_frame(frame2)
                except Exception:
                    frame2 = frame1.copy()
                try:
                    if frame1.shape != frame2.shape:
                        try:
                            frame2 = cv2.resize(
                                frame2, (frame1.shape[1], frame1.shape[0])
                            )
                        except Exception:
                            frame2 = frame1.copy()
                    diff = cv2.absdiff(frame1, frame2)
                except Exception:
                    # If absdiff fails for any reason, skip this detection pass
                    diff = np.zeros_like(frame1)
                gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
                k_size = int(self._safe_int_widget_value("blur_kernel_input", 5))
                # ensure odd kernel size
                if k_size % 2 == 0:
                    k_size = max(1, k_size - 1)
                blur = cv2.GaussianBlur(gray, (k_size, k_size), 0)
                _, thresh = cv2.threshold(
                    blur,
                    int(self._safe_int_widget_value("threshold_input", 40)),
                    255,
                    cv2.THRESH_BINARY,
                )
                # small morphology to reduce speckle (opening: erosion followed by dilation)
                kernel = np.ones((3, 3), np.uint8)
                opened = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
                dilated = cv2.dilate(
                    opened,
                    kernel,
                    iterations=int(self._safe_int_widget_value("dilate_iter_input", 2)),
                )
                contours, _ = cv2.findContours(
                    dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
                )
                contours_raw = len(contours)
                minc = float(self._safe_float_widget_value("min_contour_input", 300.0))
                maxc = float(self._safe_float_widget_value("max_contour_input", 1400000.0))
                frame_area = (
                    float(frame1.shape[0] * frame1.shape[1])
                    if frame1 is not None
                    else 640.0 * 480.0
                )
                # filter out tiny specks and objects larger than max_contour_input
                contours = [
                    c
                    for c in contours
                    if (
                        cv2.contourArea(c) > minc
                        and cv2.contourArea(c) < maxc
                    )
                ]
                contours_filtered = len(contours)
                try:
                    if (
                        getattr(self, "debug_checkbox", None)
                        and getattr(self.debug_checkbox, "isChecked", lambda: False)()
                    ):
                        print(
                            f"[PIPELINE DEBUG] FrameDiff contours_raw={contours_raw} filtered={contours_filtered} minc={minc}"
                        )
                except Exception:
                    pass
                for c in contours:
                    boxes.append(cv2.boundingRect(c))

        elif detection_mode == 1:  # Background Subtraction
            if suppressed:
                boxes = []
            else:
                # Ensure background subtractor exists if this mode is active
                if self.backSub is None:
                    self.backSub = cv2.createBackgroundSubtractorMOG2()
                    try:
                        self.enhancer.log_serial_output(
                            "Initialized Background Subtractor.", fire=False
                        )
                    except Exception:
                        pass

                # Manage warmup: apply but skip detections while background model stabilizes
                try:
                    warmup_remaining = int(getattr(self, "backsub_warmup", 0))
                except Exception:
                    warmup_remaining = 0
                fgMask = self.backSub.apply(frame1)
                try:
                    fg_nonzero = int((fgMask > 0).sum())
                except Exception:
                    fg_nonzero = 0
                # prepare min contour and frame area for subsequent filtering/diagnostics
                try:
                    minc = float(
                        self._safe_float_widget_value("min_contour_input", 300.0)
                    )
                except Exception:
                    minc = 300.0
                frame_area = (
                    float(frame1.shape[0] * frame1.shape[1])
                    if frame1 is not None
                    else 640.0 * 480.0
                )

                if warmup_remaining > 0:
                    try:
                        # decrement warmup counter and skip producing contours this frame
                        self.backsub_warmup = max(0, warmup_remaining - 1)
                    except Exception:
                        self.backsub_warmup = 0
                    contours = []
                    contours_raw = 0
                    contours_filtered = 0
                else:
                    # Apply small morphology to remove noise and close small holes
                    try:
                        k2 = np.ones((3, 3), np.uint8)
                        fgMask = cv2.morphologyEx(
                            fgMask, cv2.MORPH_OPEN, k2, iterations=1
                        )
                    except Exception:
                        pass
                    contours, _ = cv2.findContours(
                        fgMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
                    )
                    contours_raw = len(contours)
                    minc = float(
                        self._safe_float_widget_value("min_contour_input", 300.0)
                    )
                    maxc = float(
                        self._safe_float_widget_value("max_contour_input", 1400000.0)
                    )
                    frame_area = (
                        float(frame1.shape[0] * frame1.shape[1])
                        if frame1 is not None
                        else 640.0 * 480.0
                    )
                    contours = [
                        c
                        for c in contours
                        if (
                            cv2.contourArea(c) > minc
                            and cv2.contourArea(c) < maxc
                        )
                    ]
                    contours_filtered = len(contours)
                try:
                    if (
                        getattr(self, "debug_checkbox", None)
                        and getattr(self.debug_checkbox, "isChecked", lambda: False)()
                    ):
                        print(
                            f"[PIPELINE DEBUG] BackSub fg_nonzero={fg_nonzero} contours_raw={contours_raw} filtered={contours_filtered} minc={minc}"
                        )
                except Exception:
                    pass
                for c in contours:
                    boxes.append(cv2.boundingRect(c))

        elif detection_mode == 2:  # YOLO
            if suppressed:
                boxes = []
            else:
                try:
                    boxes = []
                    try:
                        model_loaded = bool(
                            getattr(self.yolo_detector, "model_loaded", False)
                        )
                    except Exception:
                        model_loaded = False
                    
                    # DEBUG: Report YOLO model load status
                    try:
                        if (
                            getattr(self, "debug_checkbox", None)
                            and getattr(
                                self.debug_checkbox, "isChecked", lambda: False
                            )()
                        ):
                            model_name = getattr(self.yolo_detector, "model_name", "None")
                            print(f"[YOLO DEBUG] model_loaded={model_loaded}, model_name={model_name}")
                    except Exception:
                        pass
                    
                    if model_loaded:
                        # CRITICAL FIX: Always set target classes before detection
                        # This allows model changes and class input changes to take effect immediately
                        try:
                            classes = (
                                self._safe_widget_method_return(
                                    "yolo_classes_input", "text", "person"
                                )
                                or "person"
                            )
                            self.yolo_detector.set_target_classes(classes)
                        except Exception:
                            pass
                        
                        boxes = self.yolo_detector.detect(
                            frame1,
                            self._safe_float_widget_value("yolo_confidence_input", 0.5),
                        )
                        try:
                            yolo_boxes_len = len(boxes)
                        except Exception:
                            yolo_boxes_len = 0
                        try:
                            if (
                                getattr(self, "debug_checkbox", None)
                                and getattr(
                                    self.debug_checkbox, "isChecked", lambda: False
                                )()
                            ):
                                print(
                                    f"[PIPELINE DEBUG] YOLO returned {yolo_boxes_len} boxes"
                                )
                        except Exception:
                            pass
                    else:
                        # try a best-effort load if combo has selection
                        model_name = (
                            self._safe_widget_method_return(
                                "yolo_model_combo", "currentText", ""
                            )
                            or ""
                        )
                        if model_name:
                            # DEBUG: Report attempting model load
                            try:
                                if (
                                    getattr(self, "debug_checkbox", None)
                                    and getattr(
                                        self.debug_checkbox, "isChecked", lambda: False
                                    )()
                                ):
                                    print(f"[YOLO DEBUG] Attempting to load model: {model_name}")
                            except Exception:
                                pass
                            
                            try:
                                load_success = self.yolo_detector.load_model(model_name)
                                if not load_success:
                                    try:
                                        if hasattr(self, "enhancer"):
                                            self.enhancer.log_serial_output(
                                                f"YOLO: Failed to load model {model_name}",
                                                fire=False
                                            )
                                    except Exception:
                                        pass
                            except Exception as e:
                                try:
                                    if hasattr(self, "enhancer"):
                                        self.enhancer.log_serial_output(
                                            f"YOLO: Error loading model {model_name}: {e}",
                                            fire=False
                                        )
                                except Exception:
                                    pass
                            try:
                                classes = (
                                    self._safe_widget_method_return(
                                        "yolo_classes_input", "text", "person"
                                    )
                                    or "person"
                                )
                                self.yolo_detector.set_target_classes(classes)
                            except Exception:
                                pass
                            try:
                                self.enhancer.log_serial_output(
                                    f"Loaded YOLO model: {model_name}"
                                )
                            except Exception:
                                pass
                            try:
                                boxes = self.yolo_detector.detect(
                                    frame1,
                                    self._safe_float_widget_value(
                                        "yolo_confidence_input", 0.5
                                    ),
                                )
                                try:
                                    yolo_boxes_len = len(boxes)
                                except Exception:
                                    yolo_boxes_len = 0
                            except Exception as e:
                                boxes = []
                                try:
                                    if hasattr(self, "enhancer"):
                                        self.enhancer.log_serial_output(
                                            f"YOLO detect error: {e}",
                                            fire=False
                                        )
                                except Exception:
                                    pass
                        else:
                            # No model selected in combo
                            try:
                                if (
                                    getattr(self, "debug_checkbox", None)
                                    and getattr(
                                        self.debug_checkbox, "isChecked", lambda: False
                                    )()
                                ):
                                    print("[YOLO DEBUG] No model selected in combo")
                            except Exception:
                                pass
                except Exception as e:
                    boxes = []
                    try:
                        if hasattr(self, "enhancer"):
                            self.enhancer.log_serial_output(
                                f"YOLO outer exception: {e}"
                            )
                    except Exception:
                        pass

            # Do NOT reuse stale `self.last_detections` as a movement fallback.
            # Re-using the last detections here causes the tracker to continue
            # driving the servos toward a stale position when the detector
            # actually returned no results (this produced the slow drift/tilt
            # behavior). If external tests need injected detections, they
            # should set a dedicated test flag (not enabled by default).

            # Apply YOLO-specific post-processing: allow the user to filter by
            # minimum box area and limit the number of results considered. These
            # settings live in the YOLO settings group and are intentionally
            # applied here (host-side) so the detector remains simple.
            try:
                if int(detection_mode) == 2 and boxes:
                    try:
                        min_area = int(
                            self._safe_int_widget_value("yolo_min_area_input", 0) or 0
                        )
                    except Exception:
                        min_area = 0
                    if min_area > 0:
                        try:
                            boxes = [
                                b for b in boxes if (int(b[2]) * int(b[3])) >= min_area
                            ]
                        except Exception:
                            pass
                    try:
                        max_results = int(
                            self._safe_int_widget_value("yolo_max_results_input", 0)
                            or 0
                        )
                    except Exception:
                        max_results = 0
                    if max_results > 0 and boxes:
                        try:
                            boxes = sorted(
                                boxes, key=lambda box: box[2] * box[3], reverse=True
                            )[:max_results]
                        except Exception:
                            pass
            except Exception:
                pass

        # ========== HYBRID DETECTION MODES (3, 4, 5) ==========
        elif detection_mode == 3:  # Hybrid: Frame Diff + Background Subtraction
            try:
                # Get fusion strategy (0=AND/strict, 1=OR/lenient)
                fusion_idx = self._safe_current_index("fusion_strategy_combo", 0)
                use_or = bool(fusion_idx == 1)  # True for OR, False for AND

                # Run frame difference detection
                framediff_boxes = []
                try:
                    frame1 = self._ensure_frame(frame1)
                    frame2 = self._ensure_frame(frame2)
                    if frame1.shape != frame2.shape:
                        frame2 = cv2.resize(frame2, (frame1.shape[1], frame1.shape[0]))
                    diff = cv2.absdiff(frame1, frame2)
                    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
                    k_size = int(self._safe_int_widget_value("blur_kernel_input", 5))
                    if k_size % 2 == 0:
                        k_size = max(1, k_size - 1)
                    blur = cv2.GaussianBlur(gray, (k_size, k_size), 0)
                    _, thresh = cv2.threshold(blur, int(self._safe_int_widget_value("threshold_input", 40)), 255, cv2.THRESH_BINARY)
                    kernel = np.ones((3, 3), np.uint8)
                    opened = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
                    dilated = cv2.dilate(opened, kernel, iterations=int(self._safe_int_widget_value("dilate_iter_input", 2)))
                    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                    minc = float(self._safe_float_widget_value("min_contour_input", 300.0))
                    maxc = float(self._safe_float_widget_value("max_contour_input", 1400000.0))
                    contours = [c for c in contours if minc < cv2.contourArea(c) < maxc]
                    framediff_boxes = [cv2.boundingRect(c) for c in contours]
                except Exception:
                    framediff_boxes = []

                # Run background subtraction detection
                backsub_boxes = []
                try:
                    if self.backSub is None:
                        self.backSub = cv2.createBackgroundSubtractorMOG2()
                    fgMask = self.backSub.apply(frame1)
                    warmup_remaining = int(getattr(self, "backsub_warmup", 0))
                    if warmup_remaining <= 0:
                        k2 = np.ones((3, 3), np.uint8)
                        fgMask = cv2.morphologyEx(fgMask, cv2.MORPH_OPEN, k2, iterations=1)
                        contours, _ = cv2.findContours(fgMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                        minc = float(self._safe_float_widget_value("min_contour_input", 300.0))
                        maxc = float(self._safe_float_widget_value("max_contour_input", 1400000.0))
                        contours = [c for c in contours if minc < cv2.contourArea(c) < maxc]
                        backsub_boxes = [cv2.boundingRect(c) for c in contours]
                    else:
                        self.backsub_warmup = max(0, warmup_remaining - 1)
                except Exception:
                    backsub_boxes = []

                # Fuse boxes: AND (intersection) or OR (union)
                if use_or:
                    # Union: include boxes from either detector
                    boxes = framediff_boxes + backsub_boxes
                else:
                    # Intersection (strict): only boxes present in both masks
                    # Check overlapping boxes: keep framediff boxes that overlap with backsub boxes
                    boxes = []
                    for fd_box in framediff_boxes:
                        fd_x, fd_y, fd_w, fd_h = fd_box
                        for bs_box in backsub_boxes:
                            bs_x, bs_y, bs_w, bs_h = bs_box
                            # Simple overlap check
                            if (fd_x < bs_x + bs_w and fd_x + fd_w > bs_x and
                                fd_y < bs_y + bs_h and fd_y + fd_h > bs_y):
                                boxes.append(fd_box)
                                break

                try:
                    if (getattr(self, "debug_checkbox", None) and getattr(self.debug_checkbox, "isChecked", lambda: False)()):
                        fusion_str = "OR" if use_or else "AND"
                        print(f"[HYBRID MODE 3] FrameDiff={len(framediff_boxes)}, BackSub={len(backsub_boxes)}, Fused({fusion_str})={len(boxes)}")
                except Exception:
                    pass
            except Exception as e:
                boxes = []
                try:
                    if hasattr(self, "enhancer"):
                        self.enhancer.log_serial_output(f"Hybrid Mode 3 error: {e}", fire=False)
                except Exception:
                    pass

        elif detection_mode == 4:  # Hybrid: Frame Diff (gate) + YOLO
            try:
                # Get motion gate threshold (percentage of frame that must move)
                motion_threshold_pct = self._safe_float_widget_value("motion_gate_threshold_input", 1.0) / 100.0

                # Run frame difference to detect motion
                try:
                    frame1 = self._ensure_frame(frame1)
                    frame2 = self._ensure_frame(frame2)
                    if frame1.shape != frame2.shape:
                        frame2 = cv2.resize(frame2, (frame1.shape[1], frame1.shape[0]))
                    diff = cv2.absdiff(frame1, frame2)
                    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
                    _, thresh = cv2.threshold(gray, int(self._safe_int_widget_value("threshold_input", 40)), 255, cv2.THRESH_BINARY)
                    motion_pixels = (thresh > 0).sum()
                    frame_area = float(frame1.shape[0] * frame1.shape[1])
                    motion_fraction = motion_pixels / frame_area if frame_area > 0 else 0.0
                except Exception:
                    motion_fraction = 0.0

                # Only run expensive YOLO if motion detected above threshold
                boxes = []
                if motion_fraction > motion_threshold_pct:
                    try:
                        model_loaded = bool(getattr(self.yolo_detector, "model_loaded", False))
                        if model_loaded:
                            try:
                                classes = self._safe_widget_method_return("yolo_classes_input", "text", "person") or "person"
                                self.yolo_detector.set_target_classes(classes)
                            except Exception:
                                pass
                            # Add timeout to prevent freeze
                            start = time.time()
                            boxes = self.yolo_detector.detect(frame1, self._safe_float_widget_value("yolo_confidence_input", 0.5))
                            elapsed = time.time() - start
                            if elapsed > 1.0:  # If detection took >1 sec, skip next frame
                                print(f"[HYBRID] YOLO detection slow ({elapsed:.2f}s) - throttling")
                        else:
                            model_name = self._safe_widget_method_return("yolo_model_combo", "currentText", "") or ""
                            if model_name:
                                try:
                                    start = time.time()
                                    self.yolo_detector.load_model(model_name)
                                    elapsed = time.time() - start
                                    if elapsed > 2.0:
                                        print(f"[HYBRID] YOLO model load slow ({elapsed:.2f}s)")
                                    classes = self._safe_widget_method_return("yolo_classes_input", "text", "person") or "person"
                                    self.yolo_detector.set_target_classes(classes)
                                    boxes = self.yolo_detector.detect(frame1, self._safe_float_widget_value("yolo_confidence_input", 0.5))
                                except Exception as ex:
                                    print(f"[HYBRID] YOLO error: {ex}")
                                    boxes = []
                    except Exception:
                        boxes = []

                try:
                    if (getattr(self, "debug_checkbox", None) and getattr(self.debug_checkbox, "isChecked", lambda: False)()):
                        print(f"[HYBRID MODE 4] Motion={motion_fraction*100:.1f}% (gate={motion_threshold_pct*100:.1f}%), YOLO boxes={len(boxes)}")
                except Exception:
                    pass
            except Exception as e:
                boxes = []
                try:
                    if hasattr(self, "enhancer"):
                        self.enhancer.log_serial_output(f"Hybrid Mode 4 error: {e}", fire=False)
                except Exception:
                    pass

        elif detection_mode == 5:  # Hybrid: Background Subtraction + YOLO (Best)
            try:
                # Get overlap threshold (percentage)
                overlap_threshold = self._safe_float_widget_value("overlap_threshold_input", 30.0) / 100.0

                # Run background subtraction to find motion regions
                backsub_boxes = []
                try:
                    if self.backSub is None:
                        self.backSub = cv2.createBackgroundSubtractorMOG2()
                    fgMask = self.backSub.apply(frame1)
                    warmup_remaining = int(getattr(self, "backsub_warmup", 0))
                    if warmup_remaining <= 0:
                        k2 = np.ones((3, 3), np.uint8)
                        fgMask = cv2.morphologyEx(fgMask, cv2.MORPH_OPEN, k2, iterations=1)
                        contours, _ = cv2.findContours(fgMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                        minc = float(self._safe_float_widget_value("min_contour_input", 300.0))
                        maxc = float(self._safe_float_widget_value("max_contour_input", 1400000.0))
                        contours = [c for c in contours if minc < cv2.contourArea(c) < maxc]
                        backsub_boxes = [cv2.boundingRect(c) for c in contours]
                    else:
                        self.backsub_warmup = max(0, warmup_remaining - 1)
                except Exception:
                    backsub_boxes = []

                # Run YOLO on full frame
                yolo_boxes = []
                try:
                    model_loaded = bool(getattr(self.yolo_detector, "model_loaded", False))
                    if model_loaded:
                        try:
                            classes = self._safe_widget_method_return("yolo_classes_input", "text", "person") or "person"
                            self.yolo_detector.set_target_classes(classes)
                        except Exception:
                            pass
                        # Add timeout monitoring
                        start = time.time()
                        yolo_boxes = self.yolo_detector.detect(frame1, self._safe_float_widget_value("yolo_confidence_input", 0.5))
                        elapsed = time.time() - start
                        if elapsed > 1.0:
                            print(f"[HYBRID MODE 5] YOLO detection slow ({elapsed:.2f}s) - throttling")
                    else:
                        model_name = self._safe_widget_method_return("yolo_model_combo", "currentText", "") or ""
                        if model_name:
                            try:
                                start = time.time()
                                self.yolo_detector.load_model(model_name)
                                elapsed = time.time() - start
                                if elapsed > 2.0:
                                    print(f"[HYBRID MODE 5] YOLO model load slow ({elapsed:.2f}s)")
                                classes = self._safe_widget_method_return("yolo_classes_input", "text", "person") or "person"
                                self.yolo_detector.set_target_classes(classes)
                                yolo_boxes = self.yolo_detector.detect(frame1, self._safe_float_widget_value("yolo_confidence_input", 0.5))
                            except Exception as ex:
                                print(f"[HYBRID MODE 5] YOLO error: {ex}")
                                yolo_boxes = []
                except Exception:
                    yolo_boxes = []

                # Filter YOLO detections: keep only those overlapping with motion regions
                boxes = []
                for yolo_box in yolo_boxes:
                    y_x, y_y, y_w, y_h = yolo_box
                    for bs_box in backsub_boxes:
                        bs_x, bs_y, bs_w, bs_h = bs_box
                        # Calculate intersection area
                        x_left = max(y_x, bs_x)
                        y_top = max(y_y, bs_y)
                        x_right = min(y_x + y_w, bs_x + bs_w)
                        y_bottom = min(y_y + y_h, bs_y + bs_h)
                        
                        if x_right > x_left and y_bottom > y_top:
                            intersection_area = (x_right - x_left) * (y_bottom - y_top)
                            yolo_area = y_w * y_h
                            overlap_ratio = intersection_area / yolo_area if yolo_area > 0 else 0.0
                            
                            if overlap_ratio >= overlap_threshold:
                                boxes.append(yolo_box)
                                break

                # Fallback: if no overlapping detections but YOLO found objects, use YOLO only
                if not boxes and yolo_boxes:
                    boxes = yolo_boxes

                try:
                    if (getattr(self, "debug_checkbox", None) and getattr(self.debug_checkbox, "isChecked", lambda: False)()):
                        print(f"[HYBRID MODE 5] BackSub={len(backsub_boxes)}, YOLO={len(yolo_boxes)}, Filtered(overlap>={overlap_threshold*100:.0f}%)={len(boxes)}")
                except Exception:
                    pass
            except Exception as e:
                boxes = []
                try:
                    if hasattr(self, "enhancer"):
                        self.enhancer.log_serial_output(f"Hybrid Mode 5 error: {e}", fire=False)
                except Exception:
                    pass

        # If we're in a slow Go-Home sequence, progress an interpolation step
        try:
            if (
                getattr(self, "_in_go_home", False)
                and getattr(self, "_go_home_step_total", 0) > 0
            ):
                # Determine configured mode (prefer widget if present)
                try:
                    mode = getattr(self, "home_return_mode", "Immediate")
                    wmode = self._safe_widget_method_return(
                        "home_return_mode_combo", "currentText", None
                    )
                    if wmode:
                        mode = str(wmode)
                except Exception:
                    mode = getattr(self, "home_return_mode", "Immediate")
                if str(mode).strip().lower() == "slow":
                    try:
                        step = int(getattr(self, "_go_home_step", 0))
                        total = int(getattr(self, "_go_home_step_total", 1))
                        start_pan = float(
                            getattr(
                                self,
                                "_go_home_start_pan",
                                getattr(self, "prev_pan_angle", 90),
                            )
                        )
                        start_tilt = float(
                            getattr(
                                self,
                                "_go_home_start_tilt",
                                getattr(self, "prev_tilt_angle", 40),
                            )
                        )
                        tgt_pan = float(
                            getattr(
                                self,
                                "_go_home_target_pan",
                                getattr(self, "HOME_PAN", 90),
                            )
                        )
                        tgt_tilt = float(
                            getattr(
                                self,
                                "_go_home_target_tilt",
                                getattr(self, "HOME_TILT", 40),
                            )
                        )
                        frac = float(min(step + 1, total)) / float(max(1, total))
                        new_pan = start_pan + (tgt_pan - start_pan) * frac
                        new_tilt = start_tilt + (tgt_tilt - start_tilt) * frac
                        self.target_pan = float(
                            np.clip(new_pan, self.PAN_MIN, self.PAN_MAX)
                        )
                        self.target_tilt = float(
                            np.clip(new_tilt, self.TILT_MIN, self.TILT_MAX)
                        )
                        # Send incremental command to move toward home
                        try:
                            self.send_serial_command()
                        except Exception:
                            pass
                        # advance step
                        self._go_home_step = step + 1
                        # finalize if done
                        if self._go_home_step >= total:
                            try:
                                self._in_go_home = False
                                # FIX DEC8: Keep FLOAT precision to prevent 3-5° drift per 10 frames
                                # INT truncation loses fractional parts that accumulate to 100°+ over time
                                self.last_known_pan = float(self.target_pan)
                                self.last_known_tilt = float(self.target_tilt)
                                self.last_sent_pan = int(self.target_pan)
                                self.last_sent_tilt = int(self.target_tilt)
                                self.prev_pan_angle = float(self.target_pan)
                                self.prev_tilt_angle = float(self.target_tilt)
                            except Exception:
                                pass
                    except Exception:
                        pass
        except Exception:
            pass

    # --- Unified Target Handling (applies to FrameDiff, BackSub, YOLO) ---
        # Any detection mode that produced `boxes` should follow the same
        # target selection, locking, smoothing, and hold-on-loss behavior.
        # If the detection pipeline produced no boxes for this frame but
        # there exists a recently-seen `last_detections` value, reuse it so
        # downstream logic (locking / auto-fire) can operate on the most
        # recently-observed detection. This is useful for tests that inject
        # `last_detections` directly and for brief frames where the detector
        # may have missed the object but recent state indicates a valid target.
        try:
            if not boxes and getattr(self, "last_detections", None):
                try:
                    now_check = time.time()
                    last_seen = float(getattr(self, "last_seen_time", 0.0))
                    hold_window = float(getattr(self, "lost_hold_seconds", 5.0))
                except Exception:
                    now_check = time.time()
                    last_seen = 0.0
                    hold_window = 5.0

                # Only reuse last_detections if it was seen recently (within hold window)
                if (now_check - last_seen) <= hold_window:
                    try:
                        # Normalize tuples to int values
                        boxes = [tuple(int(v) for v in d) for d in self.last_detections]
                    except Exception:
                        try:
                            boxes = list(self.last_detections)
                        except Exception:
                            boxes = []

        except Exception:
            # Fall through to the unified handling below
            pass

        try:
            # Update small detect status label if present so operator sees current counts
            try:
                if getattr(self, "yolo_detect_status_label", None) is not None:
                    try:
                        self.yolo_detect_status_label.setText(f"{len(boxes)} boxes")
                    except Exception:
                        pass
            except Exception:
                pass
            # initialize locals so static analysis understands types
            err_x = 0.0
            err_y = 0.0
            gain = 0.0
            smoothing = 1.0

            # COMPREHENSIVE DEBUG: Log state before entering boxes check
            try:
                tracking_on = getattr(self, "tracking_active", False)
                aiming_on = getattr(self, "aiming_active", False)
                boxes_count = len(boxes) if boxes else 0
                detection_mode_val = int(self._safe_current_index("detection_mode_combo", 0) or 0)
                
                # Log this info whenever debug is on OR if we have no boxes (to diagnose detection loss)
                should_log = (
                    (getattr(self, "debug_checkbox", None) and getattr(self.debug_checkbox, "isChecked", lambda: False)())
                    or boxes_count == 0
                )
                
                if should_log and hasattr(self, "enhancer"):
                    self.enhancer.log_serial_output(
                        f"[TRACKING DIAG] boxes={boxes_count} tracking={tracking_on} aiming={aiming_on} mode={detection_mode_val}",
                        fire=False
                    )
            except Exception:
                pass

            if boxes:
                # --- PATCH: Instantly interrupt sweep/guard on detection ---
                # If we were in sweep/guard idle, reset any sweep/guard state so tracking resumes immediately
                if hasattr(self, "idle_behavior") and str(getattr(self, "idle_behavior", "")).strip().lower() in ("sweep", "guard"):
                    # Reset sweep/guard state so next loss will start a new sweep/guard
                    if hasattr(self, "_sweep_dir"):
                        del self._sweep_dir
                    if hasattr(self, "_guard_center_pan"):
                        del self._guard_center_pan
                # If we were in a hold window, forcibly reset the last_seen_time so we don't hold position
                self.last_seen_time = time.time()
                # Play detect sound once when first locking on
                if not getattr(self, "target_locked", False):
                    try:
                        self.enhancer.play_detect()
                    except Exception:
                        pass
                    try:
                        if getattr(self, "state_logger", None):
                            self.state_logger.log("Target detected")
                    except Exception:
                        pass

                self.target_locked = True

                # ========== CRITICAL IDLE MODE AUTO-TRACKING FIX ==========
                # When in idle modes (guard/watch/search) AND auto_tracking_enabled:
                # FORCE enable both tracking and aiming to exit idle and track target
                try:
                    # FIX DEC8: Check ACTUAL idle mode state, not just dropdown selection
                    # idle_modes.get_mode() returns None (OFF) or mode name (ON)
                    # self.idle_behavior always has a value (just the dropdown selection)
                    idle_modes = getattr(self, "idle_modes", None)
                    actual_idle_mode = None
                    if idle_modes is not None:
                        actual_idle_mode = idle_modes.get_mode()  # None=OFF, "guard"/etc=ON
                    
                    auto_track_enabled = getattr(self, "auto_tracking_enabled", False)
                    
                    # FORCE tracking/aiming ON ONLY if idle mode is actually OFF
                    # (actual_idle_mode is None means idle is not active)
                    if actual_idle_mode is None and auto_track_enabled:
                        # BULLETPROOF: Force enable both flags immediately
                        if not getattr(self, "tracking_active", False):
                            self.tracking_active = True
                            try:
                                if getattr(self, "tracking_btn", None) is not None:
                                    self.tracking_btn.setChecked(True)
                                    self.tracking_btn.setText("Stop Tracking")
                            except Exception:
                                pass
                            try:
                                self.enhancer.log_serial_output(
                                    "🎯 AUTO-TRACKING ACTIVATED (idle mode disabled, detection found)", 
                                    fire=False
                                )
                            except Exception:
                                pass
                        
                        if not getattr(self, "aiming_active", False):
                            self.aiming_active = True
                            try:
                                if getattr(self, "aiming_btn", None) is not None:
                                    self.aiming_btn.setChecked(True)
                                    self.aiming_btn.setText("Stop Aiming")
                            except Exception:
                                pass
                            try:
                                self.enhancer.log_serial_output(
                                    "✓ Auto-aiming ENABLED (auto-tracking detected target)", 
                                    fire=False
                                )
                            except Exception:
                                pass
                    
                    # STANDARD PATH: Re-acquisition when tracking already active
                    elif getattr(self, "tracking_active", False) and not getattr(self, "aiming_active", False):
                        # Tracking is on but aiming is off - auto-enable aiming to let servos move
                        self.aiming_active = True
                        try:
                            if getattr(self, "aiming_btn", None) is not None:
                                self.aiming_btn.setChecked(True)
                                self.aiming_btn.setText("Stop Aiming")
                        except Exception:
                            pass
                        try:
                            self.enhancer.log_serial_output("✓ Auto-aiming enabled (re-acquisition after loss)", fire=False)
                        except Exception:
                            pass
                except Exception as e:
                    try:
                        self.enhancer.log_serial_output(f"[WARN] Idle mode auto-tracking error: {e}", fire=False)
                    except Exception:
                        pass
                
                # DEBUG: Log when detection finds a box
                try:
                    if hasattr(self, "enhancer"):
                        self.enhancer.log_serial_output(
                            f"[DETECT] Box found: x={int(x)} y={int(y)} w={int(w)} h={int(h)} aiming_active={getattr(self,'aiming_active',False)}",
                            fire=False
                        )
                except Exception:
                    pass

                # Select the largest box by area (w * h)
                try:
                    x, y, w, h = max(boxes, key=lambda box: box[2] * box[3])
                except Exception:
                    x = y = w = h = 0

                try:
                    # Normalize and store last_detections in the expected format
                    self.last_detections = [(int(x), int(y), int(w), int(h))]
                    # Store target center for Quick Strike feature
                    self.last_target_center = (x + w / 2.0, y + h / 2.0)
                except Exception:
                    pass

                try:
                    self.last_seen_time = time.time()
                except Exception:
                    self.last_seen_time = 0.0

                try:
                    if getattr(self, "state_logger", None):
                        self.state_logger.log(
                            "Locking on target"
                            if not getattr(self, "target_locked", False)
                            else "Tracking target"
                        )
                except Exception:
                    pass

                # Only update tracking position if not in manual override or manual suppression
                if not (
                    getattr(self, "manual_override", False)
                    or getattr(self, "_manual_override_active", False)
                ):
                    try:
                        # FIX DEC8: Use floating point division to preserve sub-pixel precision
                        # Integer division loses 0.5-0.8 pixels per frame, accumulating 2-3° drift per 1000 frames
                        cx = x + w / 2.0
                        cy = y + h / 2.0
                        if frame1 is not None:
                            # Use stored frame dimensions (set by frame ratio selector)
                            # This ensures all calculations are consistent with selected resolution
                            frame_h = self.frame_height
                            frame_w = self.frame_width
                            # FIX DEC8b #2: Use floating-point division to prevent 0.5px deadzone oscillation
                            # Integer division (frame_w // 2) creates 0.5px misalignment:
                            # - frame_w=640 → center=320 (correct)
                            # - frame_w=641 → center=320 (should be 320.5 - loses precision)
                            # - This causes deadzone boundary to oscillate +/-1px
                            # Float division preserves sub-pixel precision: 640/2.0 = 320.0, 641/2.0 = 320.5
                            err_x = cx - frame_w / 2.0
                            err_y = cy - frame_h / 2.0
                        smoothing = float(
                            self._safe_float_widget_value("smoothing_input", 0.35)
                        )
                        
                        # FIXED: Clamp smoothing to expanded range
                        # 0 = instant snap, 1 = no movement. User-configurable range 0.1-0.8
                        # 0.1-0.3 = aggressive tracking, 0.4-0.6 = balanced, 0.7-0.8 = smooth
                        smoothing = float(np.clip(smoothing, 0.1, 0.8))
                        
                        # FIX DEC8b #4: Apply smoothing parameter changes gradually over 10 frames
                        # Old approach: Blended smoothing value (0.9*old + 0.1*new) caused mid-track position snaps
                        # When user adjusted smoothing from 0.35 to 0.65, the blend ratio inverted instantly
                        # This caused target position to snap 0.3° on next frame, then oscillate as it stabilized
                        # New approach: Transition the PARAMETER gradually instead of the BLEND
                        # Track transition progress over 10 frames (faster than old approach but stable)
                        if not hasattr(self, "_smoothing_transition_frames"):
                            self._smoothing_transition_frames = 0  # frames into transition
                            self._smoothing_old_value = smoothing
                            self._smoothing_new_value = smoothing
                        
                        # Check if smoothing parameter changed
                        if smoothing != self._smoothing_new_value:
                            # Parameter changed - start new transition
                            self._smoothing_old_value = self._tracking_frame_smoothing  # Current smoothed value
                            self._smoothing_new_value = smoothing  # Target value
                            self._smoothing_transition_frames = 0  # Reset counter
                        
                        # Progress transition (10 frames total)
                        if self._smoothing_transition_frames < 10:
                            progress = self._smoothing_transition_frames / 10.0
                            smoothing = (1 - progress) * self._smoothing_old_value + progress * self._smoothing_new_value
                            self._smoothing_transition_frames += 1
                        else:
                            smoothing = self._smoothing_new_value
                        
                        self._tracking_frame_smoothing = smoothing
                        
                        # Base gain is controlled by movement sensitivity; modulate it
                        # by the tracking speed slider so users can tune responsiveness
                        # without changing the sensitivity slider semantics.
                        try:
                            sensitivity = float(
                                self._safe_float_widget_value(
                                    "movement_sensitivity_slider", 25
                                )
                            )
                            
                            # FIXED: SYMMETRIC SCALING for both sliders (0-100 range)
                            # sensitivity=1   -> mult=0.11 (slow response)
                            # sensitivity=50  -> mult=0.55 (balanced, default)
                            # sensitivity=100 -> mult=1.0  (fast response)
                            sensitivity_mult = 0.1 + (sensitivity / 100.0) * 0.9
                            
                            track_speed = float(
                                self._safe_int_widget_value(
                                    "tracking_speed_slider", 50
                                )
                            )
                            # FIXED: Symmetric scaling for tracking_speed (0-100 range)
                            # speed=1   -> mult=0.11 (slow)
                            # speed=50  -> mult=0.55 (balanced)
                            # speed=100 -> mult=1.0  (fast)
                            track_speed_mult = 0.1 + (track_speed / 100.0) * 0.9
                            
                            # ========== AGGRESSIVE TRACKING - DECEMBER 2024 UPGRADE ==========
                            # INCREASED base gain from 0.005 to 0.01 for much faster response
                            base_gain = 0.01  # Doubled from 0.005 for more aggressive tracking
                            gain = base_gain * sensitivity_mult * track_speed_mult
                            
                            # Apply aim_aggression modifier (0-100 slider)
                            # aggression=0   -> 0.5x gain (very cautious)
                            # aggression=50  -> 1.0x gain (balanced)
                            # aggression=100 -> 2.0x gain (maximum aggression)
                            try:
                                aim_aggression = getattr(self, "aim_aggression", 50)
                                aggression_mult = 0.5 + (aim_aggression / 100.0) * 1.5
                                gain = gain * aggression_mult
                            except Exception:
                                pass
                            
                            # Initial gain cap before distance-based boosts
                            gain = float(np.clip(gain, 0.0001, 0.04))
                            
                            # ========== DISTANCE-BASED ADAPTIVE GAIN (3 ZONES) ==========
                            # ZONE 1: FAR (>3x deadzone) - Normal tracking, no boost
                            # ZONE 2: NEAR (1.5x-3x deadzone) - 1.5x boost for faster approach
                            # ZONE 3: FINAL APPROACH (<1.5x deadzone) - 2.5x boost for precise centering
                            try:
                                deadzone_val = int(
                                    self._safe_int_widget_value("deadzone_slider", 8)
                                )
                                # Calculate distance from center using both error components
                                total_error = (abs(err_x)**2 + abs(err_y)**2)**0.5
                                
                                # Define zone boundaries
                                final_approach_threshold = deadzone_val * 1.5  # Very close
                                near_threshold = deadzone_val * 3.0  # Getting close
                                
                                if total_error <= final_approach_threshold:
                                    # ZONE 3: FINAL APPROACH - Aggressive centering
                                    if getattr(self, "final_approach_boost", True):
                                        gain = gain * 2.5  # Strong boost for precise centering
                                    else:
                                        gain = gain * 1.8  # Moderate boost if disabled
                                elif total_error <= near_threshold:
                                    # ZONE 2: NEAR - Moderate boost
                                    gain = gain * 1.5
                                # ZONE 1: FAR - No boost (default gain)
                                
                            except Exception:
                                pass  # If zone calc fails, use unmodified gain
                            
                            # Mode-specific gain caps (INCREASED for YOLO)
                            try:
                                detection_mode = int(self._safe_current_index("detection_mode_combo", 0) or 0)
                            except Exception:
                                detection_mode = 0
                            
                            if detection_mode == 2:  # YOLO
                                # INCREASED cap from 0.05 to 0.08 for more aggressive YOLO tracking
                                gain = float(np.clip(gain, 0.0001, 0.08))
                            else:  # Frame Diff or BackSub
                                # INCREASED cap from 0.02 to 0.04 for faster motion tracking
                                gain = float(np.clip(gain, 0.0001, 0.04))
                        except Exception:
                            gain = 0.0025
                    except Exception:
                        # Outer tracking block exception
                        err_x = 0.0
                        err_y = 0.0
                        gain = 0.0

                # ========== QUICK STRIKE MOVEMENT LOGIC ==========
                # When quick_strike_active, bypass normal tracking and move at max speed to target
                if getattr(self, "quick_strike_active", False):
                    try:
                        # Check for timeout (2 seconds max)
                        quick_strike_elapsed = time.time() - getattr(self, "quick_strike_start_time", 0)
                        if quick_strike_elapsed > 2.0:
                            self.enhancer.log_serial_output(
                                f"[⚡ STRIKE] ⏰ Timeout after {quick_strike_elapsed:.1f}s - aborting",
                                fire=False
                            )
                            self.quick_strike_active = False
                        else:
                            # Get current position
                            current_pan = float(getattr(self, "last_sent_pan", getattr(self, "target_pan", 90)))
                            current_tilt = float(getattr(self, "last_sent_tilt", getattr(self, "target_tilt", 45)))
                            
                            # Get target position
                            target_pan = getattr(self, "quick_strike_target_pan", current_pan)
                            target_tilt = getattr(self, "quick_strike_target_tilt", current_tilt)
                            
                            # Calculate distance to target
                            pan_error = abs(target_pan - current_pan)
                            tilt_error = abs(target_tilt - current_tilt)
                            
                            # Check if position reached (within 2° tolerance)
                            position_reached = pan_error < 2.0 and tilt_error < 2.0
                            
                            if position_reached:
                                # Position reached - fire if armed and not already fired
                                if not getattr(self, "quick_strike_fired", False):
                                    self.quick_strike_fired = True
                                    
                                    # Fire if safety is off and auto-fire or rapid-fire is enabled
                                    should_fire = (
                                        self.safety_state == 0 and
                                        (getattr(self, "auto_fire_enabled", False) or 
                                         getattr(self, "rapid_fire_enabled", False))
                                    )
                                    
                                    if should_fire:
                                        self.trigger_fired = True
                                        self.enhancer.log_serial_output(
                                            f"[⚡ STRIKE] 🎯 TARGET HIT! Fired at Pan={target_pan:.1f}° Tilt={target_tilt:.1f}°",
                                            fire=True
                                        )
                                        try:
                                            self.enhancer.play_fire()
                                        except Exception:
                                            pass
                                        try:
                                            self.send_serial_command()
                                        except Exception:
                                            pass
                                    else:
                                        self.enhancer.log_serial_output(
                                            f"[⚡ STRIKE] ✓ Position reached (no fire - safety on or auto-fire disabled)",
                                            fire=False
                                        )
                                    
                                    # Complete - resume normal tracking
                                    self.quick_strike_active = False
                                    self.enhancer.log_serial_output(
                                        "[⚡ STRIKE] Complete - resuming autotracking",
                                        fire=False
                                    )
                            else:
                                # Move toward target at MAXIMUM speed (no smoothing, max rate)
                                max_step = 10.0  # Maximum degrees per frame for quick strike
                                
                                # Calculate step toward target
                                if pan_error > 0.1:
                                    pan_step = min(max_step, pan_error)
                                    if target_pan < current_pan:
                                        pan_step = -pan_step
                                    new_pan = current_pan + pan_step
                                else:
                                    new_pan = target_pan
                                
                                if tilt_error > 0.1:
                                    tilt_step = min(max_step, tilt_error)
                                    if target_tilt < current_tilt:
                                        tilt_step = -tilt_step
                                    new_tilt = current_tilt + tilt_step
                                else:
                                    new_tilt = target_tilt
                                
                                # Clamp to limits
                                new_pan = float(np.clip(new_pan, self.PAN_MIN, self.PAN_MAX))
                                new_tilt = float(np.clip(new_tilt, self.TILT_MIN, self.TILT_MAX))
                                
                                # Set target positions directly
                                self.target_pan = new_pan
                                self.target_tilt = new_tilt
                                
                                # Send command immediately
                                try:
                                    self.send_serial_command()
                                except Exception:
                                    pass
                                
                                # Debug log
                                if getattr(self, "debug_checkbox", None) and self.debug_checkbox.isChecked():
                                    self.enhancer.log_serial_output(
                                        f"[⚡ STRIKE] Moving: {current_pan:.1f}→{new_pan:.1f} pan, {current_tilt:.1f}→{new_tilt:.1f} tilt (err: {pan_error:.1f}°, {tilt_error:.1f}°)",
                                        fire=False
                                    )
                    except Exception as e:
                        self.enhancer.log_serial_output(f"[⚡ STRIKE] Error: {e}", fire=False)
                        self.quick_strike_active = False
                # ========== END QUICK STRIKE LOGIC ==========

                # Normal tracking - skip if quick strike is active
                if getattr(self, "quick_strike_active", False):
                    pass  # Quick strike handles its own movement
                elif not (
                    getattr(self, "manual_override", False)
                    or getattr(self, "_manual_override_active", False)
                ):
                    pan_dir = -1 if getattr(self, "flip_pan_direction", False) else 1
                    tilt_dir = -1 if getattr(self, "flip_tilt_direction", False) else 1

                    # BULLETPROOF: Use consistent previous positions
                    # These should reflect the ACTUAL last position sent to hardware
                    prev_pan = float(getattr(self, "last_sent_pan", getattr(self, "prev_pan_angle", 90)))
                    prev_tilt = float(getattr(self, "last_sent_tilt", getattr(self, "prev_tilt_angle", 40)))
                    
                    # SAFE: Ensure prev positions are within limits (defensive)
                    prev_pan = float(np.clip(prev_pan, self.PAN_MIN, self.PAN_MAX))
                    prev_tilt = float(np.clip(prev_tilt, self.TILT_MIN, self.TILT_MAX))
                    
                    # STUCK DETECTION: If we're at a limit and the error still suggests moving further,
                    # we might be "stuck". Reduce the target value slightly to help escape.
                    at_pan_min = abs(prev_pan - self.PAN_MIN) < 2.0
                    at_pan_max = abs(prev_pan - self.PAN_MAX) < 2.0
                    at_tilt_min = abs(prev_tilt - self.TILT_MIN) < 2.0
                    at_tilt_max = abs(prev_tilt - self.TILT_MAX) < 2.0

                    # Calculate new target positions
                    # Note: tilt typically inverts (higher Y error = lower tilt), so we subtract
                    new_pan = prev_pan + (err_x * gain) * pan_dir
                    new_tilt = prev_tilt - (err_y * gain) * tilt_dir
                    
                    # ========== COMPREHENSIVE TILT DIAGNOSTICS ==========
                    # Log detailed calculation steps to verify tilt is calculated correctly
                    try:
                        if getattr(self, "debug_checkbox", None) and self.debug_checkbox.isChecked():
                            tilt_delta = (err_y * gain) * tilt_dir
                            self.enhancer.log_serial_output(
                                f"[TILT_CALC_DIAG] err_y={err_y:.1f} gain={gain:.4f} tilt_dir={tilt_dir} delta={tilt_delta:.4f} prev_tilt={prev_tilt:.2f} new_tilt={new_tilt:.4f}",
                                fire=False
                            )
                    except Exception:
                        pass
                    
                    # ========== ENCODER-BASED TILT BOOST (GUARDED BY PID) ==========
                    # CRITICAL FIX: Encoder boost ONLY applies when BOTH encoder AND PID are enabled
                    # When PID is disabled, encoder has ZERO effect on tilt calculation
                    try:
                        # SAFETY GATE: Both conditions must be true
                        if self.tilt_pid_enabled and getattr(self, "tilt_encoder_enabled", False):
                            encoder_error = getattr(self, "tilt_position_error", 0.0)
                            # Only apply boost if encoder error is meaningful
                            if abs(encoder_error) > 0.5:
                                # Calculate boost factor (1.0 = no boost, up to 2.5 = 2.5x boost)
                                encoder_boost = 1.0 + min(abs(encoder_error) / 10.0, 1.5)
                                
                                # CRITICAL FIX: Check if we should apply boost
                                # Apply ONLY if movement direction matches encoder error direction
                                tilt_delta = new_tilt - prev_tilt
                                # If positive error (need to move up) and moving up, boost
                                # If negative error (need to move down) and moving down, boost
                                if (tilt_delta < 0 and encoder_error < 0) or (tilt_delta > 0 and encoder_error > 0):
                                    # Movement is toward the error - boost it
                                    boosted_tilt = prev_tilt - (err_y * gain * encoder_boost) * tilt_dir
                                    
                                    # ========== ENCODER-PROTECTED BOOST CLAMPING ==========
                                    # Ensure boosted tilt respects encoder boundaries
                                    encoder_aware_boost_min = self.TILT_MIN
                                    encoder_aware_boost_max = self.TILT_MAX
                                    if self.tilt_encoder_enabled and hasattr(self, "encoder_tilt_min_detected"):
                                        encoder_aware_boost_min = self.encoder_tilt_min_detected
                                        encoder_aware_boost_max = self.encoder_tilt_max_detected
                                    
                                    new_tilt = float(np.clip(boosted_tilt, encoder_aware_boost_min, encoder_aware_boost_max))
                    except Exception:
                        pass

                    # Apply overshoot percent (positive -> more aggressive; negative -> undershoot)
                    try:
                        overshoot = (
                            float(self._safe_float_widget_value("overshoot_input", 0.0))
                            / 100.0
                        )
                        if overshoot != 0.0:
                            # compute delta from prev and apply overshoot multiplier
                            try:
                                dpan = new_pan - prev_pan
                                dtilt = new_tilt - prev_tilt
                                new_pan = prev_pan + dpan * (1.0 + overshoot)
                                new_tilt = prev_tilt + dtilt * (1.0 + overshoot)
                            except Exception:
                                pass
                    except Exception:
                        pass

                    # BULLETPROOF: Clamp new_pan and new_tilt BEFORE snap/smoothing decision
                    # This prevents out-of-bounds values from contaminating all downstream calculations
                    # and ensures smooth, predictable behavior within physical limits.
                    
                    # ========== ENCODER-AWARE LIMIT CLAMPING ==========
                    # Use encoder-detected limits if available, otherwise use soft limits
                    clamping_tilt_min = self.TILT_MIN
                    clamping_tilt_max = self.TILT_MAX
                    
                    if self.tilt_encoder_enabled and hasattr(self, "encoder_tilt_min_detected"):
                        clamping_tilt_min = self.encoder_tilt_min_detected
                        clamping_tilt_max = self.encoder_tilt_max_detected
                    
                    new_pan = float(np.clip(new_pan, self.PAN_MIN, self.PAN_MAX))
                    new_tilt = float(np.clip(new_tilt, clamping_tilt_min, clamping_tilt_max))
                    
                    # AGGRESSIVE UNSTICK LOGIC: If we've been stuck at boundary for multiple frames,
                    # force movement away from the boundary regardless of target position
                    stuck_frame_threshold = 5  # Frames before we consider it "stuck"
                    
                    # Track frames stuck at each boundary
                    if not hasattr(self, "_frames_at_tilt_max"):
                        self._frames_at_tilt_max = 0
                    if not hasattr(self, "_frames_at_tilt_min"):
                        self._frames_at_tilt_min = 0
                    if not hasattr(self, "_frames_at_pan_max"):
                        self._frames_at_pan_max = 0
                    if not hasattr(self, "_frames_at_pan_min"):
                        self._frames_at_pan_min = 0
                    
                    # Check if stuck and force escape
                    if at_tilt_max and new_tilt == self.TILT_MAX:
                        self._frames_at_tilt_max += 1
                        if self._frames_at_tilt_max > stuck_frame_threshold:
                            # Forcibly move away from max tilt
                            new_tilt = self.TILT_MAX - 5.0  # Force 5° movement down
                    else:
                        self._frames_at_tilt_max = 0
                    
                    if at_tilt_min and new_tilt == self.TILT_MIN:
                        self._frames_at_tilt_min += 1
                        if self._frames_at_tilt_min > stuck_frame_threshold:
                            # Forcibly move away from min tilt
                            new_tilt = self.TILT_MIN + 5.0
                    else:
                        self._frames_at_tilt_min = 0
                    
                    if at_pan_max and new_pan == self.PAN_MAX:
                        self._frames_at_pan_max += 1
                        if self._frames_at_pan_max > stuck_frame_threshold:
                            new_pan = self.PAN_MAX - 5.0
                    else:
                        self._frames_at_pan_max = 0
                    
                    if at_pan_min and new_pan == self.PAN_MIN:
                        self._frames_at_pan_min += 1
                        if self._frames_at_pan_min > stuck_frame_threshold:
                            new_pan = self.PAN_MIN + 5.0
                    else:
                        self._frames_at_pan_min = 0
                    
                    # UNSTICK LOGIC: If clamped at a boundary and we're still trying to go past it,
                    # nudge inward slightly to break the "stuck" state
                    if at_pan_min and new_pan == self.PAN_MIN and err_x < 0:
                        # At min pan and trying to go further left - nudge right
                        new_pan = self.PAN_MIN + 2.0
                    elif at_pan_max and new_pan == self.PAN_MAX and err_x > 0:
                        # At max pan and trying to go further right - nudge left
                        new_pan = self.PAN_MAX - 2.0
                    
                    if at_tilt_min and new_tilt == self.TILT_MIN and err_y > 0:
                        # At min tilt and trying to go further down (err_y positive) - nudge up
                        new_tilt = self.TILT_MIN + 2.0
                    elif at_tilt_max and new_tilt == self.TILT_MAX and err_y < 0:
                        # At max tilt and trying to go further up (err_y negative) - nudge down
                        new_tilt = self.TILT_MAX - 2.0

                    # TRACKING GOAL: Keep yellow dot (target center) INSIDE the deadzone circle
                    # Deadzone defines the pixel radius around frame center that we consider "good enough".
                    # If the dot is inside the deadzone, do not move. If outside, move to chase it.
                    deadzone_px = int(
                        self._safe_int_widget_value("deadzone_slider", 8)
                    )
                    # FIX DEC8b #6: Increase effective deadzone by 1px to account for sub-pixel oscillation
                    # Sub-pixel noise in detections causes ±0.5px oscillation around center
                    # Adding 1px buffer prevents repeated deadzone entry/exit cycles
                    deadzone_px = deadzone_px + 1
                    # Snap threshold is INDEPENDENT: Default to 4-5x deadzone size for proper two-stage tracking
                    # This allows smooth approach when far away, snap recovery when target jumps far
                    snap_px = int(
                        self._safe_int_widget_value("snap_threshold_slider", deadzone_px * 5)
                    )

                    # ========== AIMING OVERRIDE: GUARANTEE DEADZONE ENTRY ==========
                    # When aiming_active=True, force aggressive movement toward deadzone
                    # This overrides the normal "deadzone hold" logic to ensure target entry
                    aiming_active = getattr(self, "aiming_active", False)
                    
                    # If target is inside deadzone AND aiming is NOT active, hold current position (no aiming)
                    if abs(err_x) <= deadzone_px and abs(err_y) <= deadzone_px and not aiming_active:
                        target_pan_val = prev_pan
                        target_tilt_val = prev_tilt
                    else:
                        # ========== EMERGENCY SNAP FOR AIMING FAR TARGETS ==========
                        # When aiming_active and target is far (>5x deadzone), snap directly
                        # This ensures fast target acquisition during active aiming
                        if aiming_active and (abs(err_x) > snap_px * 1.5 or abs(err_y) > snap_px * 1.5):
                            # Snap directly to target without smoothing for fast acquisition
                            target_pan_val = new_pan
                            target_tilt_val = new_tilt
                            # FIX DEC8b #5: Consolidated rate-limiting (single, consistent application)
                            # Problem: Double rate-limiting caused oscillation - snap decision THEN per-frame cap
                            # Solution: Apply rate limit once, immediately after snap decision, with proper direction
                            # This prevents undershooting the target (which causes oscillation on next frame)
                            # DEC 2024: Increased from 5° to 8° for more aggressive tracking
                            max_pan_step = 8.0  # degrees per frame (increased for aggressive tracking)
                            max_tilt_step = 8.0
                            # Single consolidated check - no double-limiting
                            pan_delta = target_pan_val - prev_pan
                            tilt_delta = target_tilt_val - prev_tilt
                            
                            # Apply rate limit symmetrically (both directions)
                            if abs(pan_delta) > max_pan_step:
                                target_pan_val = prev_pan + (max_pan_step if pan_delta > 0 else -max_pan_step)
                            if abs(tilt_delta) > max_tilt_step:
                                target_tilt_val = prev_tilt + (max_tilt_step if tilt_delta > 0 else -max_tilt_step)
                        # If the target is clearly outside the snap threshold we snap to the computed angle
                        # (fast response when target is far away)
                        elif abs(err_x) > snap_px or abs(err_y) > snap_px:
                            target_pan_val = new_pan
                            target_tilt_val = new_tilt
                        else:
                            # ========== ADAPTIVE SMOOTHING FOR DEADZONE PRECISION ==========
                            # When target is very close to deadzone (within 2.5x radius when aiming,
                            # or 3x when passive), reduce smoothing for aggressive final push into deadzone.
                            # Otherwise use configured smoothing for stable tracking.
                            adaptive_smoothing = smoothing
                            # Adaptive smoothing: reduce smoothing near deadzone for snappy response
                            threshold_for_adaptive = deadzone_px * 1.5
                            
                            if abs(err_x) <= threshold_for_adaptive or abs(err_y) <= threshold_for_adaptive:
                                # FIX DEC8: Use consistent smoothing regardless of aiming state
                                # Different smoothing on aiming toggle causes 1-2 frame stick artifact near deadzone
                                adaptive_smoothing = 0.05  # Consistent regardless of aiming state
                            
                            # Smooth (IIR) blend between previous and new with adaptive filter
                            # When target is approaching the deadzone, blend smoothly to avoid jitter
                            target_pan_val = (1 - adaptive_smoothing) * prev_pan + adaptive_smoothing * new_pan
                            target_tilt_val = (1 - adaptive_smoothing) * prev_tilt + adaptive_smoothing * new_tilt
                            
                            # ========== MICRO-ADJUSTMENT FOR PRECISION AIMING ==========
                            # When close to deadzone (within 3x the deadzone radius for aiming,
                            # or 2x for passive tracking), force movements to ensure entry.
                            # Larger deadzones get stronger push; smaller deadzones get gentler control.
                            # When aiming: 3x threshold ensures aggressive final push from further away
                            # When passive: 2x threshold for normal precision
                            threshold_for_push = deadzone_px * 3.0 if aiming_active else deadzone_px * 2.0
                            
                            # FIX DEC8b #3: Gradient-based micro-adjustment instead of fixed min_push
                            # Old approach: min_push override caused overshooting when error was small
                            # Example: err_x=2px, gain=0.0075 → movement=0.015° → capped to min_push=0.5° (33x overshoot)
                            # New approach: Scale movement smoothly from deadzone boundary to threshold
                            # When err_x > threshold: use full gain (fast approach)
                            # When err_x near deadzone: reduce gain (smooth approach, no overshoot)
                            # This creates smooth gradient instead of threshold snap
                            
                            if abs(err_x) <= threshold_for_push and abs(err_x) > deadzone_px:
                                # Target is close horizontally - apply gradient-scaled adjustment
                                # Gradient: 0% at deadzone edge, 100% at threshold distance
                                distance_from_deadzone = abs(err_x) - deadzone_px  # pixels beyond deadzone
                                gradient_distance = threshold_for_push - deadzone_px  # total range
                                gradient_factor = distance_from_deadzone / gradient_distance if gradient_distance > 0 else 1.0
                                
                                # Scale gain by gradient (smoother approach, no overshooting)
                                # When very close (gradient_factor ≈ 0): minimal movement
                                # When approaching threshold (gradient_factor ≈ 1): full gain movement
                                scaled_gain = gain * gradient_factor
                                pan_micro_movement = abs(err_x * scaled_gain) * pan_dir
                                
                                if err_x > 0:
                                    target_pan_val = prev_pan + pan_micro_movement  # Move right
                                else:
                                    target_pan_val = prev_pan - pan_micro_movement  # Move left
                            
                            if abs(err_y) <= threshold_for_push and abs(err_y) > deadzone_px:
                                # Target is close vertically - apply gradient-scaled adjustment
                                # ========== CRITICAL FIX: GUARANTEED TILT ENTRY IN AIMING ==========
                                # Use gradient-scaled gain for tilt (matching pan), ensuring smooth entry
                                # This ensures tilt responds with same sensitivity as pan during precision aiming
                                distance_from_deadzone = abs(err_y) - deadzone_px  # pixels beyond deadzone
                                gradient_distance = threshold_for_push - deadzone_px  # total range
                                gradient_factor = distance_from_deadzone / gradient_distance if gradient_distance > 0 else 1.0
                                
                                # Scale gain by gradient for smooth approach
                                scaled_gain = gain * gradient_factor
                                tilt_micro_movement = abs(err_y * scaled_gain) * tilt_dir
                                
                                if err_y > 0:
                                    target_tilt_val = prev_tilt - tilt_micro_movement  # Move down (inverted)
                                else:
                                    target_tilt_val = prev_tilt + tilt_micro_movement  # Move up

                    try:
                        # Keep the running target as float so small fractional updates
                        # accumulate across frames (then we int() only when sending to hardware).
                        self.target_pan = float(
                            np.clip(target_pan_val, self.PAN_MIN, self.PAN_MAX)
                        )
                        self.target_tilt = float(
                            np.clip(target_tilt_val, self.TILT_MIN, self.TILT_MAX)
                        )
                        
                        # ========== TILT DIAGNOSTICS ==========
                        # Log detailed tilt information when debug is enabled
                        try:
                            if getattr(self, "debug_checkbox", None) and self.debug_checkbox.isChecked():
                                # Determine which path was taken
                                path_info = "UNKNOWN"
                                if abs(err_x) <= deadzone_px and abs(err_y) <= deadzone_px:
                                    path_info = "DEADZONE_HOLD"
                                elif abs(err_x) > snap_px or abs(err_y) > snap_px:
                                    path_info = "SNAP_FAST"
                                elif abs(err_y) <= deadzone_px * 2.0 and abs(err_y) > deadzone_px:
                                    path_info = "MICRO_ADJUST"
                                else:
                                    path_info = "SMOOTH_IIR"
                                
                                self.enhancer.log_serial_output(
                                    f"[TILT_DIAG] path={path_info} err_y={err_y:.1f} gain={gain:.4f} new_tilt_raw={target_tilt_val:.4f}° final={self.target_tilt:.4f}° prev={prev_tilt:.2f}° limits=[{self.TILT_MIN},{self.TILT_MAX}] deadzone={deadzone_px} snap={snap_px}",
                                    fire=False
                                )
                        except Exception:
                            pass
                        
                        # ========== PRECISION AIMING VERIFICATION ==========
                        # Log when target is very close to deadzone (for verification of precision)
                        try:
                            dist_to_deadzone = min(abs(err_x), abs(err_y)) - deadzone_px
                            if 0 <= dist_to_deadzone <= 2.0:  # Within 2 pixels of entering deadzone
                                if getattr(self, "debug_checkbox", None) and self.debug_checkbox.isChecked():
                                    self.enhancer.log_serial_output(
                                        f"[PRECISION AIM] yellow_dot approaching deadzone: dist_to_edge={dist_to_deadzone:.1f}px err_x={err_x:.1f} err_y={err_y:.1f}",
                                        fire=False
                                    )
                        except Exception:
                            pass
                        
                        # BULLETPROOF: Rate-limit tilt changes to prevent jerky movements
                        # If tilt delta is too large, gradually step toward target instead of jumping
                        try:
                            last_tilt = float(getattr(self, "last_sent_tilt", self.target_tilt))
                            tilt_delta = abs(self.target_tilt - last_tilt)
                            
                            # SMART RATE LIMITING: Reduce max_step when approaching limits
                            # DEC 2024: Increased from 5°/frame to 8°/frame for aggressive tracking
                            # Normal: 8°/frame, Near limit (< 10° away): 2.5°/frame
                            dist_to_min = self.target_tilt - self.TILT_MIN
                            dist_to_max = self.TILT_MAX - self.target_tilt
                            min_dist_to_boundary = min(dist_to_min, dist_to_max)
                            
                            if min_dist_to_boundary < 10:
                                # Very close to boundary - move slowly
                                max_tilt_step = 2.5
                            elif min_dist_to_boundary < 20:
                                # Approaching boundary - moderate speed
                                max_tilt_step = 4.0
                            else:
                                # Safe distance from boundaries - aggressive speed
                                max_tilt_step = 8.0
                            
                            if tilt_delta > max_tilt_step:
                                # Step toward target gradually
                                if self.target_tilt > last_tilt:
                                    self.target_tilt = last_tilt + max_tilt_step
                                else:
                                    self.target_tilt = last_tilt - max_tilt_step
                                
                                # Ensure still within limits after rate limiting
                                self.target_tilt = float(
                                    np.clip(self.target_tilt, self.TILT_MIN, self.TILT_MAX)
                                )
                        except Exception:
                            pass
                        
                        # DEBUG: Log target computation
                        try:
                            if (getattr(self, "debug_checkbox", None) and getattr(self.debug_checkbox, "isChecked", lambda: False)()):
                                if hasattr(self, "enhancer"):
                                    self.enhancer.log_serial_output(
                                        f"[TARGET] pan={self.target_pan:.1f} tilt={self.target_tilt:.1f} (raw: pan={target_pan_val:.1f} tilt={target_tilt_val:.1f}) err_x={err_x:.1f} err_y={err_y:.1f} gain={gain:.4f}",
                                        fire=False
                                    )
                        except Exception:
                            pass
                    except Exception:
                        pass
                    # Debug: show computed targets and related state
                    try:
                        dbg = bool(
                            getattr(self, "debug_checkbox", None)
                            and self.debug_checkbox.isChecked()
                        )
                    except Exception:
                        dbg = False
                    if dbg:
                        try:
                            dline = (
                                f"[DBG] Computed target_pan={getattr(self,'target_pan',None)} target_tilt={getattr(self,'target_tilt',None)} "
                                f"err_x={err_x:.1f} err_y={err_y:.1f} gain={gain:.4f} smoothing={smoothing:.3f} "
                                f"aiming_active={getattr(self,'aiming_active',False)} tracking_active={getattr(self,'tracking_active',False)}"
                            )
                            if (
                                hasattr(self, "enhancer")
                                and getattr(self, "enhancer", None) is not None
                            ):
                                self.enhancer.log_serial_output(dline, fire=False)
                            else:
                                print(dline)
                        except Exception:
                            pass
                    # cache the last known commanded pan/tilt so we can hold them if the
                    # target is lost for a short configurable duration
                    try:
                        # FIX DEC8: Keep FLOAT precision to prevent 3-5° drift per 10 frames
                        # INT truncation loses fractional parts that accumulate to 100°+ over time
                        self.last_known_pan = float(self.target_pan)
                        self.last_known_tilt = float(self.target_tilt)
                    except Exception:
                        pass

                    # Immediately send serial command for responsive auto-aiming when enabled.
                    try:
                        if getattr(self, "tracking_active", False) and getattr(
                            self, "aiming_active", False
                        ):
                            try:
                                self.send_serial_command()
                            except Exception:
                                pass
                    except Exception:
                        pass

            else:
                # --- Target Lost: Hold Last Position for a configurable time ---
                # AIMING PRIORITY: If target reappears during hold window, keep turret aiming immediately
                # This gives aiming/centering priority over idle behaviors
                # ========== FIXED: READ lost_hold_seconds FROM UI WIDGET IN REAL-TIME ==========
                # Instead of using cached value, read from UI to ensure user changes apply immediately
                hold_window = self._safe_float_widget_value("lost_hold_input", 5.0)
                
                # REACQUISITION ACCELERATION: If tracking_active, accelerate timeout from 5s to 2s
                # This prioritizes re-centering a reacquired target over idle mode behavior
                if getattr(self, "tracking_active", False):
                    hold_window = min(hold_window, 2.0)  # Max 2 sec hold during active tracking
                
                now_ts = time.time()
                time_since_seen = now_ts - getattr(self, "last_seen_time", 0.0)

                if not self.manual_override:
                    # If user requested infinite hold, never timeout
                    if getattr(self, "hold_infinite", False):
                        self.target_pan = float(
                            getattr(
                                self,
                                "last_known_pan",
                                getattr(
                                    self,
                                    "last_sent_pan",
                                    getattr(self, "prev_pan_angle", 90),
                                ),
                            )
                        )
                        self.target_tilt = float(
                            getattr(
                                self,
                                "last_known_tilt",
                                getattr(
                                    self,
                                    "last_sent_tilt",
                                    getattr(self, "prev_tilt_angle", 40),
                                ),
                            )
                        )
                        try:
                            self.last_sent_pan = int(self.target_pan)
                            self.last_sent_tilt = int(self.target_tilt)
                            # preserve fractional prev angles
                            self.prev_pan_angle = float(self.target_pan)
                            self.prev_tilt_angle = float(self.target_tilt)
                            self._hold_infinite_active = True
                        except Exception:
                            pass
                    else:
                        if time_since_seen <= hold_window:
                            # hold the last commanded position for the configured window
                            self.target_pan = float(
                                getattr(
                                    self,
                                    "last_known_pan",
                                    getattr(
                                        self,
                                        "last_sent_pan",
                                        getattr(self, "prev_pan_angle", 90),
                                    ),
                                )
                            )
                            self.target_tilt = float(
                                getattr(
                                    self,
                                    "last_known_tilt",
                                    getattr(
                                        self,
                                        "last_sent_tilt",
                                        getattr(self, "prev_tilt_angle", 40),
                                    ),
                                )
                            )
                        else:
                            # hold window expired -> consult configured HOME-return mode
                            try:
                                # Prefer widget value if present, otherwise use attribute
                                mode = getattr(self, "home_return_mode", "Immediate")
                                try:
                                    wmode = self._safe_widget_method_return(
                                        "home_return_mode_combo", "currentText", None
                                    )
                                    if wmode:
                                        mode = str(wmode)
                                except Exception:
                                    pass
                                mode_lower = (str(mode) or "Immediate").strip().lower()

                                # Idle behavior override by `self.idle_behavior` attribute.
                                try:
                                    idle_beh = str(
                                        getattr(self, "idle_behavior", "")
                                    ).strip().lower()
                                except Exception:
                                    idle_beh = ""

                                home_pan = float(getattr(self, "HOME_PAN", 90))
                                home_tilt = float(getattr(self, "HOME_TILT", 40))
                                home_pan = float(np.clip(home_pan, self.PAN_MIN, self.PAN_MAX))
                                home_tilt = float(np.clip(home_tilt, self.TILT_MIN, self.TILT_MAX))

                                nowt = time.time()

                                # Handle idle behaviors: sweep, watch, or guard
                                if idle_beh == "sweep":
                                    try:
                                        # Check if it's time to move (respect rest time)
                                        if (nowt - float(getattr(self, "_last_sweep_time", 0.0))) >= float(getattr(self, "_sweep_rest_time", 3.0)):
                                            margin = int(getattr(self, "_sweep_margin", 5))
                                            speed = float(getattr(self, "_sweep_speed", 0.8))
                                            if not hasattr(self, "_sweep_dir"):
                                                self._sweep_dir = False
                                            prev_pan = float(getattr(self, "prev_pan_angle", home_pan))
                                            pan = prev_pan + (speed if not self._sweep_dir else -speed)
                                        if pan >= (self.PAN_MAX - margin):
                                            self._sweep_dir = True
                                            pan = self.PAN_MAX - margin
                                        elif pan <= (self.PAN_MIN + margin):
                                            self._sweep_dir = False
                                            pan = self.PAN_MIN + margin
                                        self.target_pan = float(np.clip(pan, self.PAN_MIN, self.PAN_MAX))
                                        self.target_tilt = float(
                                            getattr(self, "last_known_tilt", getattr(self, "prev_tilt_angle", home_tilt))
                                        )
                                        try:
                                            if getattr(self, "tracking_active", False) and getattr(self, "aiming_active", False):
                                                self.send_serial_command()
                                        except Exception:
                                            pass
                                    except Exception:
                                        pass

                                elif idle_beh == "watch":
                                    # Watch mode - stay at watch position until detection
                                    try:
                                        self.target_pan = float(self._watch_position_pan)
                                        self.target_tilt = float(self._watch_position_tilt)
                                    except Exception:
                                        # Fallback to home position
                                        self.target_pan = float(home_pan)
                                        self.target_tilt = float(home_tilt)

                                elif idle_beh == "guard":
                                    try:
                                        # Check if it's time to move to a new random position
                                        if not hasattr(self, "_last_guard_move") or \
                                           (nowt - float(getattr(self, "_last_guard_move", 0.0))) >= float(getattr(self, "_guard_rest_time", 5.0)):
                                            # Generate new random position
                                            pan_min = float(getattr(self, "_guard_pan_range", (20, 160))[0])
                                            pan_max = float(getattr(self, "_guard_pan_range", (20, 160))[1])
                                            tilt_min = float(getattr(self, "_guard_tilt_range", (30, 90))[0])
                                            tilt_max = float(getattr(self, "_guard_tilt_range", (30, 90))[1])
                                            
                                            self.target_pan = float(random.uniform(pan_min, pan_max))
                                            self.target_tilt = float(random.uniform(tilt_min, tilt_max))
                                            self._last_guard_move = nowt
                                    except Exception:
                                        # Fallback to current position
                                        if getattr(self, "_guard_center_pan", None) is None:
                                            self._guard_center_pan = int(
                                                getattr(
                                                    self,
                                                    "last_known_pan",
                                                    getattr(self, "prev_pan_angle", home_pan),
                                                )
                                            )
                                        center = float(self._guard_center_pan)
                                        rng = int(getattr(self, "_guard_range", 15))
                                        speed = float(getattr(self, "_guard_speed", 0.6))
                                        if not hasattr(self, "_sweep_dir"):
                                            self._sweep_dir = False
                                        pan = float(getattr(self, "prev_pan_angle", center)) + (speed if not self._sweep_dir else -speed)
                                        left = max(self.PAN_MIN + 1, center - rng)
                                        right = min(self.PAN_MAX - 1, center + rng)
                                        if pan >= right:
                                            self._sweep_dir = True
                                            pan = right
                                        elif pan <= left:
                                            self._sweep_dir = False
                                            pan = left
                                        self.target_pan = float(np.clip(pan, self.PAN_MIN, self.PAN_MAX))
                                        self.target_tilt = float(
                                            getattr(self, "last_known_tilt", getattr(self, "prev_tilt_angle", home_tilt))
                                        )
                                        try:
                                            if getattr(self, "tracking_active", False) and getattr(self, "aiming_active", False):
                                                self.send_serial_command()
                                        except Exception:
                                            pass
                                    except Exception:
                                        pass

                                else:
                                    # Disabled: keep last-known / last-sent position (no auto-home)
                                    if mode_lower in ("disabled", "none", "off"):
                                        try:
                                            self.target_pan = float(
                                                getattr(
                                                    self,
                                                    "last_known_pan",
                                                    getattr(
                                                        self,
                                                        "last_sent_pan",
                                                        getattr(self, "prev_pan_angle", 90),
                                                    ),
                                                )
                                            )
                                            self.target_tilt = float(
                                                getattr(
                                                    self,
                                                    "last_known_tilt",
                                                    getattr(
                                                        self,
                                                        "last_sent_tilt",
                                                        getattr(
                                                            self, "prev_tilt_angle", 40
                                                        ),
                                                    ),
                                                )
                                            )
                                        except Exception:
                                            pass

                                    # Slow: interpolate to home over several frames to avoid abrupt motion
                                    elif mode_lower == "slow":
                                        try:
                                            self._in_go_home = True
                                            # suppress detection while the go-home completes
                                            try:
                                                suspend = float(
                                                    self._safe_float_widget_value(
                                                        "home_return_suspend_input",
                                                        getattr(
                                                            self,
                                                            "home_move_suspend_seconds",
                                                            2.0,
                                                        ),
                                                    )
                                                )
                                            except Exception:
                                                pass  # BULLETPROOF FIX: No detection suppression
                                            # Detection always active - removed suppression logic
                                            # Removed: suspend = 2.0; self._suppress_detection_until = nowt + suspend

                                            # initialize interpolation parameters
                                            try:
                                                self._go_home_step = 0
                                                self._go_home_step_total = int(
                                                    max(
                                                        1,
                                                        getattr(
                                                            self, "go_home_slow_steps", 6
                                                        ),
                                                    )
                                                )
                                                self._go_home_start_pan = float(
                                                    getattr(
                                                        self,
                                                        "prev_pan_angle",
                                                        self.target_pan,
                                                    )
                                                )
                                                self._go_home_start_tilt = float(
                                                    getattr(
                                                        self,
                                                        "prev_tilt_angle",
                                                        self.target_tilt,
                                                    )
                                                )
                                                self._go_home_target_pan = float(home_pan)
                                                self._go_home_target_tilt = float(home_tilt)
                                                # Start at current position; interpolation will begin in the main loop
                                                self.target_pan = float(
                                                    self._go_home_start_pan
                                                )
                                                self.target_tilt = float(
                                                    self._go_home_start_tilt
                                                )
                                            except Exception:
                                                pass
                                            # kick-off: send a first command so MCU registers current position
                                            try:
                                                self.send_serial_command()
                                            except Exception:
                                                pass
                                        except Exception:
                                            pass

                                    # Immediate: jump to home and send command now
                                    else:
                                        try:
                                            self._in_go_home = True
                                            try:
                                                suspend = float(
                                                    self._safe_float_widget_value(
                                                        "home_return_suspend_input",
                                                        getattr(
                                                            self,
                                                            "home_move_suspend_seconds",
                                                            2.0,
                                                        ),
                                                    )
                                                )
                                            except Exception:
                                                try:
                                                    suspend = float(
                                                        getattr(
                                                            self,
                                                            "home_move_suspend_seconds",
                                                            2.0,
                                                        )
                                                    )
                                                except Exception:
                                                    pass  # BULLETPROOF FIX: No detection suppression
                                            # Detection always active - removed suppression logic
                                            # Removed: suspend = 2.0; self._suppress_detection_until = nowt + suspend

                                            self.target_pan = float(home_pan)
                                            self.target_tilt = float(home_tilt)
                                            # Align prev angles to avoid fractional drift
                                            try:
                                                self.prev_pan_angle = float(self.target_pan)
                                                self.prev_tilt_angle = float(
                                                    self.target_tilt
                                                )
                                            except Exception:
                                                pass
                                            try:
                                                self.last_known_pan = int(self.target_pan)
                                                self.last_known_tilt = int(self.target_tilt)
                                                self.last_sent_pan = int(self.target_pan)
                                                self.last_sent_tilt = int(self.target_tilt)
                                            except Exception:
                                                pass
                                            # Send an immediate command to reposition if serial is available
                                            try:
                                                self.send_serial_command()
                                            except Exception:
                                                pass
                                        except Exception:
                                            pass
                            except Exception:
                                # Fallback: preserve previous behavior if anything fails
                                try:
                                    self.target_pan = float(
                                        getattr(
                                            self,
                                            "last_sent_pan",
                                            getattr(self, "prev_pan_angle", 90),
                                        )
                                    )
                                    self.target_tilt = float(
                                        getattr(
                                            self,
                                            "last_sent_tilt",
                                            getattr(self, "prev_tilt_angle", 40),
                                        )
                                    )
                                except Exception:
                                    pass
                else:
                    # CRITICAL FIX DEC8: manual_override=True failsafe
                    # When user is manually controlling, still restore position on detection loss
                    # Otherwise turret position never updates and defaults to minimum (PAN_MIN=5, TILT_MIN=18)
                    try:
                        self.target_pan = float(
                            getattr(
                                self,
                                "last_known_pan",
                                getattr(
                                    self,
                                    "last_sent_pan",
                                    getattr(self, "prev_pan_angle", float(self.HOME_PAN)),
                                ),
                            )
                        )
                        self.target_tilt = float(
                            getattr(
                                self,
                                "last_known_tilt",
                                getattr(
                                    self,
                                    "last_sent_tilt",
                                    getattr(self, "prev_tilt_angle", float(self.HOME_TILT)),
                                ),
                            )
                        )
                    except Exception:
                        pass

                # clear detection/lock state
                try:
                    if getattr(self, "state_logger", None):
                        if getattr(self, "target_locked", False):
                            self.state_logger.log("Lost target")
                        else:
                            self.state_logger.log("On standby (searching)")
                except Exception:
                    pass
                self.target_locked = False
                self.last_detections = []
                self.trigger_fired = False
                if not getattr(self, "hold_infinite", False):
                    self._hold_infinite_active = False
                
                # ========== AUTO-STOP TRACKING ON TARGET LOSS (TIMEOUT) ==========
                # When no target detected for hold_window seconds, automatically stop tracking
                # and enter idle mode (if configured)
                try:
                    hold_window = getattr(self, "lost_hold_seconds", 5.0)
                    now_ts = time.time()
                    time_since_seen = now_ts - getattr(self, "last_seen_time", 0.0)
                    
                    # If hold window has expired and tracking is still on, stop it
                    if time_since_seen > hold_window and getattr(self, "tracking_active", False):
                        self.tracking_active = False
                        self.aiming_active = False
                        try:
                            if getattr(self, "tracking_btn", None) is not None:
                                self.tracking_btn.setChecked(False)
                                self.tracking_btn.setText("Start Tracking")
                        except Exception:
                            pass
                        try:
                            if getattr(self, "aiming_btn", None) is not None:
                                self.aiming_btn.setChecked(False)
                                self.aiming_btn.setText("Start Aiming")
                        except Exception:
                            pass
                        try:
                            self.enhancer.log_serial_output(
                                f"[TRACK] Hold window expired ({hold_window:.1f}s) - stopped tracking, entering idle mode",
                                fire=False
                            )
                        except Exception:
                            pass
                except Exception:
                    pass
                
                # ========== IDLE MODE BEHAVIOR ON TARGET LOSS ==========
                # When target is lost, enter configured idle behavior
                # (Guard, Watch, Search, or Sweep modes)
                try:
                    idle_beh = str(getattr(self, "idle_behavior", "")).strip().lower()
                    # Idle modes only activate when tracking is OFF
                    # This prevents interference with manual tracking
                    if idle_beh in ("guard", "watch", "search", "sweep"):
                        # Idle mode is configured - position updates handled in _update_idle_mode_positions()
                        # No action needed here - idle mode will take over target positioning
                        pass
                except Exception:
                    pass
        except Exception:
            pass

        try:
            h_f, w_f = frame1.shape[:2]
            cx, cy = w_f // 2, h_f // 2
            deadzone = getattr(self, "deadzone_slider", None)
            deadzone_val = (
                self._safe_int_widget_value("deadzone_slider", 40)
                if deadzone is not None
                else 40
            )

            color = (255, 255, 255)
            size = 40
            gap = 20
            thickness = 2

            cv2.line(
                frame1, (cx - size, cy - size), (cx - gap, cy - size), color, thickness
            )
            cv2.line(
                frame1, (cx + gap, cy - size), (cx + size, cy - size), color, thickness
            )
            cv2.line(
                frame1, (cx - size, cy + size), (cx - gap, cy + size), color, thickness
            )
            cv2.line(
                frame1, (cx + gap, cy + size), (cx + size, cy + size), color, thickness
            )
            cv2.line(
                frame1, (cx - size, cy - size), (cx - size, cy - gap), color, thickness
            )
            cv2.line(
                frame1, (cx - size, cy + gap), (cx - size, cy + size), color, thickness
            )
            cv2.line(
                frame1, (cx + size, cy - size), (cx + size, cy - gap), color, thickness
            )
            cv2.line(
                frame1, (cx + size, cy + gap), (cx + size, cy + size), color, thickness
            )
            cv2.circle(frame1, (cx, cy), 3, (255, 255, 255), -1)
            cv2.circle(frame1, (cx, cy), int(deadzone_val), (0, 200, 255), 1)

            # Store clean frame BEFORE drawing detection rectangles for sniper view
            self._frame_for_sniper = frame1.copy()
            
            if hasattr(self, "last_detections") and self.last_detections:
                for x_box, y_box, w_box, h_box in self.last_detections:
                    tx = int(x_box + w_box / 2)
                    ty = int(y_box + h_box / 2)

                    dist = ((tx - cx) ** 2 + (ty - cy) ** 2) ** 0.5

                    if dist <= deadzone_val:
                        color_box = (0, 0, 255)  # red = locked
                        label = "LOCKED"
                        cooldown = self._safe_float_widget_value(
                            "trigger_cooldown_input", 1.5
                        )
                        now = time.time()
                        # Only auto-fire when turret is ARMED (safety_state==0)
                        if self.safety_state == 0:
                            # Handle both rapid fire and normal auto-fire
                            if getattr(self, "rapid_fire_enabled", False):
                                # Check if we should stop firing due to timeout
                                if self.trigger_fired and (now - self._firing_start_time) > self._max_firing_duration:
                                    # Firing timeout reached - stop firing
                                    self.trigger_fired = False
                                    self.enhancer.log_serial_output(f"[RAPID-FIRE] Firing timeout ({self._max_firing_duration:.1f}s) - stopped", fire=False)
                                    msg = None
                                else:
                                    # Start or continue firing
                                    if not self.trigger_fired:
                                        self._firing_start_time = now  # Record firing start time
                                    self.trigger_fired = True
                                    msg = f"[RAPID-FIRE] Target locked & firing (dist={dist:.1f}px)"
                            elif getattr(self, "auto_fire_enabled", False) and (now - self.last_trigger_time >= cooldown):
                                self.trigger_fired = True
                                self.last_trigger_time = now
                                msg = f"[AUTO-FIRE] Target locked & fired (dist={dist:.1f}px, cooldown={cooldown:.2f}s)"
                            else:
                                msg = None

                            if msg:
                                # SEND COMMAND TO ARDUINO (was missing!)
                                self.send_serial_command()
                                self.enhancer.log_serial_output(msg, fire=True)
                                try:
                                    self._pulse_fire_indicator()
                                except Exception:
                                    pass
                    else:
                        color_box = (0, 255, 255)  # yellow = normal
                        label = f"{int(dist)}px"

                    # Anti-aliased rectangle and text
                    cv2.rectangle(
                        frame1,
                        (x_box, y_box),
                        (x_box + w_box, y_box + h_box),
                        color_box,
                        2,
                        cv2.LINE_AA,
                    )
                    cv2.circle(frame1, (tx, ty), 5, color_box, -1, cv2.LINE_AA)
                    cv2.putText(
                        frame1,
                        label,
                        (x_box, y_box - 8),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 0, 0),
                        3,
                        cv2.LINE_AA,
                    )
                    cv2.putText(
                        frame1,
                        label,
                        (x_box, y_box - 8),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        color_box,
                        1,
                        cv2.LINE_AA,
                    )

            # FPS calculation and update
            if hasattr(self, "prev_frame_time"):
                current_time = time.time()
                delta = current_time - self.prev_frame_time
                self.prev_frame_time = current_time
                if delta > 0:
                    self.enhancer.update_fps(1.0 / delta)

        except Exception:
            pass

        # Throttled detection diagnostics (every 10 frames) to help debugging
        try:
            self._frame_diag_counter = getattr(self, "_frame_diag_counter", 0) + 1
            if self._frame_diag_counter >= 10:
                self._frame_diag_counter = 0
                try:
                    detection_mode = int(
                        self._safe_current_index("detection_mode_combo", 0) or 0
                    )
                except Exception:
                    detection_mode = 0
                try:
                    model_loaded = bool(
                        getattr(
                            getattr(self, "yolo_detector", None), "model_loaded", False
                        )
                    )
                except Exception:
                    model_loaded = False
                try:
                    back_exists = getattr(self, "backSub", None) is not None
                except Exception:
                    back_exists = False
                try:
                    boxes_count = len(boxes) if boxes else 0
                except Exception:
                    boxes_count = 0
                try:
                    if (
                        getattr(self, "debug_checkbox", None)
                        and getattr(self.debug_checkbox, "isChecked", lambda: False)()
                    ):
                        msg = f"[DETECT DIAG] mode={detection_mode} boxes={boxes_count} frame={frame1.shape if hasattr(frame1, 'shape') else None} yolo_loaded={model_loaded} backSub={back_exists} contours_raw={locals().get('contours_raw', None)} contours_filtered={locals().get('contours_filtered', None)} fg_nonzero={locals().get('fg_nonzero', None)} yolo_hits={locals().get('yolo_boxes_len', None)}"
                        print(msg)
                        try:
                            self.enhancer.log_serial_output(msg, fire=False)
                        except Exception:
                            pass
                except Exception:
                    try:
                        if (
                            getattr(self, "debug_checkbox", None)
                            and getattr(
                                self.debug_checkbox, "isChecked", lambda: False
                            )()
                        ):
                            print(
                                f"[DETECT DIAG] mode={detection_mode} boxes={boxes_count} frame={getattr(frame1, 'shape', None)} yolo_loaded={model_loaded} backSub={back_exists}"
                            )
                    except Exception:
                        pass
        except Exception:
            pass

        # ========== HUD DATA COLLECTION (Required data contract) ==========
        # Populate self.hud_data with REQUIRED values for _add_crosshair_and_scope()
        # CRITICAL: Do NOT add fallback placeholders like '???'.
        # All HUD data must be required and validated HERE at the source.
        # If a value is unknown, set a real numeric/string fallback.
        
        # Pan/Tilt - ALWAYS have real values
        _pan = self.target_pan if hasattr(self, 'target_pan') and self.target_pan is not None else 90.0
        _tilt = self.target_tilt if hasattr(self, 'target_tilt') and self.target_tilt is not None else 45.0
        self.hud_data['pan'] = float(_pan)
        self.hud_data['tilt'] = float(_tilt)
        
        # FPS - extract from enhancer or use 0
        _fps = 0.0
        try:
            if hasattr(self, "enhancer") and self.enhancer is not None:
                fps_text = getattr(self.enhancer, "current_fps_text", "")
                if "FPS" in fps_text:
                    import re
                    match = re.search(r"(\d+\.?\d*)\s*FPS", fps_text)
                    if match:
                        _fps = float(match.group(1))
        except:
            pass
        self.hud_data['fps'] = _fps
        
        # Detection mode - get current mode name
        _det_mode = "FrameDiff"
        try:
            det_idx = self._safe_current_index("detection_mode_combo", 0)
            det_names = ["FrameDiff", "BackSub", "YOLO", "Hybrid", "Motion", "Color"]
            _det_mode = det_names[det_idx] if det_idx < len(det_names) else "FrameDiff"
        except:
            pass
        self.hud_data['detection_mode'] = _det_mode
        
        # Resolution - use configured values (not querying from camera)
        _res_w = self.frame_width
        _res_h = self.frame_height
        self.hud_data['resolution'] = f"{_res_w}x{_res_h}"
        
        # Idle mode - string or None
        _idle = None
        try:
            idle_obj = getattr(self, 'idle_modes', None)
            if idle_obj is not None:
                mode = idle_obj.get_mode()
                if mode is not None and str(mode).lower() != "none":
                    _idle = str(mode)
        except:
            pass
        self.hud_data['idle_mode'] = _idle
        
        # Safety state - True=SAFE, False=ARMED
        self.hud_data['safety_state'] = bool(getattr(self, 'safety_state', 1) == 1)
        
        # Trigger fired - bool
        self.hud_data['trigger_fired'] = bool(getattr(self, 'trigger_fired', False))
        
        # Quick strike active - bool
        self.hud_data['quick_strike_active'] = bool(getattr(self, 'quick_strike_active', False))
        
        # Has target - bool based on detections
        self.hud_data['has_target'] = bool(getattr(self, 'last_detections', None))
        
        # Recording - bool
        self.hud_data['recording'] = bool(getattr(self, '_test_recording_active', False))
        
        # Debug lines - only when debug checkbox is enabled
        _dbg_lines = []
        try:
            debug_on = bool(
                getattr(self, "debug_checkbox", None) and
                getattr(self.debug_checkbox, "isChecked", lambda: False)()
            )
            if debug_on:
                if "err_x" in locals():
                    _dbg_lines.append(f"err_x={int(err_x)}")
                if "err_y" in locals():
                    _dbg_lines.append(f"err_y={int(err_y)}")
                _dbg_lines.append(f"pan={int(self.hud_data['pan'])}")
                _dbg_lines.append(f"tilt={int(self.hud_data['tilt'])}")
        except:
            pass
        self.hud_data['debug_lines'] = _dbg_lines

        # --- Sniper view widget update ---
        if hasattr(self, "last_detections") and self.last_detections:
            # Only auto-show the sniper dock if the user hasn't explicitly closed it
            if (
                not self.sniper_dock.isVisible()
                and not getattr(self, "_sniper_user_closed", False)
                and getattr(self, "auto_show_sniper", True)
            ):
                # Position the dock on first show
                main_geo = self.geometry()
                self.sniper_dock.setGeometry(
                    main_geo.right() - 250, main_geo.top() + 80, 220, 220
                )
                self.sniper_dock.show()

            try:
                (x, y, w, h) = self.last_detections[0]
                cx, cy = x + w // 2, y + h // 2

                # Crop a region around the target from CLEAN frame (no detection rectangles)
                sniper_frame = getattr(self, '_frame_for_sniper', frame1)
                zoom_size = max(w, h) * 1.5
                x1 = max(int(cx - zoom_size / 2), 0)
                y1 = max(int(cy - zoom_size / 2), 0)
                x2 = min(int(cx + zoom_size / 2), sniper_frame.shape[1])
                y2 = min(int(cy + zoom_size / 2), sniper_frame.shape[0])
                zoom = sniper_frame[y1:y2, x1:x2]

                if zoom.size > 0:
                    # Convert to pixmap and display (guarded to avoid QPainter warnings
                    # when the paint device / pixmap is not valid). We defensively
                    # check sizes and null pixmaps before setting on the label.
                    try:
                        zoom_rgb = cv2.cvtColor(zoom, cv2.COLOR_BGR2RGB)
                        h_z, w_z, ch_z = zoom_rgb.shape
                        if w_z > 0 and h_z > 0:
                            qimg_zoom = QImage(
                                zoom_rgb.data, w_z, h_z, ch_z * w_z, QImage.Format_RGB888
                            )
                            pix_zoom = QPixmap.fromImage(qimg_zoom)
                            if not pix_zoom.isNull() and getattr(self, "sniper_view_label", None):
                                try:
                                    lbl_size = self.sniper_view_label.size()
                                    if lbl_size.width() > 0 and lbl_size.height() > 0:
                                        try:
                                            scaled = pix_zoom.scaled(
                                                lbl_size,
                                                Qt.AspectRatioMode.KeepAspectRatio,
                                                Qt.TransformationMode.SmoothTransformation,
                                            )
                                            # Queue pixmap update on the Qt main thread
                                            _queue_set_pixmap(self.sniper_view_label, scaled)
                                        except Exception:
                                            # fallback to direct pixmap set (queued)
                                            try:
                                                _queue_set_pixmap(self.sniper_view_label, pix_zoom)
                                            except Exception:
                                                try:
                                                    self.sniper_view_label.clear()
                                                except Exception:
                                                    pass
                                    else:
                                        try:
                                            _queue_set_pixmap(self.sniper_view_label, pix_zoom)
                                        except Exception:
                                            try:
                                                self.sniper_view_label.clear()
                                            except Exception:
                                                pass
                                except Exception:
                                    # label may be invalid; clear safely
                                    try:
                                        self.sniper_view_label.clear()
                                    except Exception:
                                        pass
                    except Exception as e:
                        try:
                            if getattr(self, "enhancer", None):
                                self.enhancer.log_serial_output(f"Sniper view error: {e}", fire=False)
                        except Exception:
                            print("Sniper view error:", e)
            except Exception as e:
                self.enhancer.log_serial_output(f"Sniper view error: {e}", fire=True)
        else:
            # Always keep sniper dock visible even if no detections — but
            # respect explicit user-closure so we don't force it back open.
            try:
                if (
                    not self.sniper_dock.isVisible()
                    and not getattr(self, "_sniper_user_closed", False)
                    and getattr(self, "auto_show_sniper", True)
                ):
                    main_geo = self.geometry()
                    self.sniper_dock.setGeometry(
                        main_geo.right() - 250, main_geo.top() + 80, 220, 220
                    )
                    self.sniper_dock.show()
            except Exception:
                pass
            # Clear sniper view to blank when no target
            try:
                self.sniper_view_label.clear()
                self.sniper_view_label.setText("No Target")
            except Exception:
                pass

        # Convert the final frame (with all overlays) to RGB for display
        rgb = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
        # Add sniper scope crosshair and unified HUD overlay
        rgb = self._add_crosshair_and_scope(rgb)
        
        # NOTE: All HUD elements (opacity info, status, etc.) are now drawn
        # in _add_crosshair_and_scope() using grid-based layout
        
        # 🔒 FORCE contiguous memory (CRITICAL)
        rgb = np.ascontiguousarray(rgb)

        h, w, ch = rgb.shape
        bytes_per_line = w * ch  # MUST be width * channels

        qimg = QImage(
            rgb.data,
            w,
            h,
            bytes_per_line,
            QImage.Format_RGB888
        )

        pixmap = QPixmap.fromImage(qimg)

        self.video_label.setPixmap(
            pixmap.scaled(
                self.video_label.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

        # ========== CRITICAL FIX (DEC10): UNCONDITIONAL SERIAL COMMAND ==========
        # MUST send command every frame to MCU, even when no detection occurs.
        # Without this, when boxes is empty and idle modes don't match, the MCU never
        # receives target_pan/target_tilt updates, causing servo to stay stuck at last
        # position or default to minimum (Pan=0°, Tilt=min).
        #
        # This ensures:
        # 1. MCU gets HOME position when detection fails (not MIN position)
        # 2. Idle mode movements are transmitted to hardware  
        # 3. Manual control updates reach MCU consistently
        # 4. send_serial_command() internally guards against unnecessary transmissions
        #
        # DO NOT add conditional checks here - the condition guard is in send_serial_command()
        # which checks MCU connection, safety state, and other factors.
        try:
            self.send_serial_command()
        except Exception:
            pass

    def _update_idle_mode_positions(self):
        """Update turret positions based on active idle mode.
        
        This is called before send_serial_command() to allow idle modes to
        control target_pan/tilt when no tracking/aiming/manual control is active.
        
        CRITICAL GUARD: Checks tracking_active and manual_override flags
        to prevent idle mode from overwriting active tracking. This guard is essential
        to prevent idle mode logic from fighting active tracking position updates.
        
        BULLETPROOF FIX (DEC4): Properly disengage idle mode when tracking becomes active
        to prevent state corruption and ensure clean transitions.
        """
        try:
            # BULLETPROOF: Check if tracking/manual override became active
            # If so, properly disengage idle mode to prevent state corruption
            idle_modes = getattr(self, 'idle_modes', None)
            tracking_active = getattr(self, 'tracking_active', False)
            manual_override = getattr(self, 'manual_override', False)
            
            if (tracking_active or manual_override) and idle_modes is not None:
                current_idle_mode = idle_modes.get_mode()
                if current_idle_mode is not None:
                    # IMPORTANT: Disengage idle mode cleanly to prevent state mismatch
                    # This clears active_mode and resets internal state variables
                    try:
                        idle_modes.disengage_immediately()
                        try:
                            if hasattr(self, 'enhancer') and self.enhancer:
                                self.enhancer.log_serial_output(
                                    f"[IDLE] Disengaged {current_idle_mode} mode (tracking/manual override active)",
                                    fire=False
                                )
                        except Exception:
                            pass
                    except Exception:
                        pass
                    # Also clear idle mode state timers to prevent stale data
                    try:
                        if hasattr(self, '_idle_mode_state_time'):
                            delattr(self, '_idle_mode_state_time')
                        if hasattr(self, '_idle_mode_state_index'):
                            delattr(self, '_idle_mode_state_index')
                        if hasattr(self, '_idle_mode_last_target'):
                            delattr(self, '_idle_mode_last_target')
                        if hasattr(self, '_rest_mode_start_time'):
                            delattr(self, '_rest_mode_start_time')
                        # Bug #2 FIX: Clean up search and watch mode state variables
                        if hasattr(self, '_search_target_pan'):
                            delattr(self, '_search_target_pan')
                        if hasattr(self, '_search_target_tilt'):
                            delattr(self, '_search_target_tilt')
                        if hasattr(self, '_watch_direction'):
                            delattr(self, '_watch_direction')
                    except Exception:
                        pass
            
            # Don't update idle positions if manual override or tracking is active
            if manual_override or tracking_active:
                return
            
            idle_modes = getattr(self, 'idle_modes', None)
            if idle_modes is None:
                return
            
            current_mode = idle_modes.get_mode()
            if current_mode is None:
                return
            
            current_time = time.time()
            
            # Initialize idle mode timing tracking if not present
            if not hasattr(self, '_idle_mode_state_time'):
                self._idle_mode_state_time = current_time
                self._idle_mode_state_index = 0
                self._idle_mode_last_target = (self.target_pan, self.target_tilt)
            
            # REST MODE: Hold current position
            if current_mode == 'rest':
                # Rest mode just holds position
                # Implement auto-hide: hide video after 3 seconds, show on next user input
                try:
                    # Initialize REST mode timer on first rest activation
                    if not hasattr(self, '_rest_mode_start_time'):
                        self._rest_mode_start_time = current_time
                    
                    elapsed_rest = current_time - self._rest_mode_start_time
                    hide_delay = getattr(self, '_home_screen_hide_delay', 3000) / 1000.0  # Convert ms to seconds
                    
                    # Hide home tab after delay
                    if elapsed_rest > hide_delay:
                        try:
                            # Switch to home tab (index 0) and hide video
                            if getattr(self, 'main_tab_widget', None) is not None:
                                if self.main_tab_widget.currentIndex() != 0:
                                    self.main_tab_widget.setCurrentIndex(0)
                                
                                # Clear video display
                                if getattr(self, 'video_label', None) is not None:
                                    self.video_label.clear()
                        except Exception:
                            pass
                except Exception:
                    pass
            
            # GUARD MODE: Patrol between points with smooth interpolated movement
            elif current_mode == 'guard':
                guard_config = idle_modes.get_guard_config()
                dwell_time = guard_config.get('dwell_time', 5)
                movement_speed = guard_config.get('movement_speed', 50) / 100.0  # Convert 1-100% to 0.01-1.0
                
                # Initialize guard motion state if not already present
                if not hasattr(self, '_guard_target_pan'):
                    next_point = idle_modes.guard_get_next_point()
                    self._guard_target_pan = float(next_point[0])
                    self._guard_target_tilt = float(next_point[1])
                    self._guard_in_motion = False
                    self._guard_move_start_time = None
                    self._idle_mode_state_time = current_time
                
                elapsed = current_time - self._idle_mode_state_time
                
                # DWELL PHASE: Stay at current position
                if elapsed <= dwell_time:
                    if not self._guard_in_motion:
                        # Hold position during dwell
                        self.target_pan = self._guard_target_pan
                        self.target_tilt = self._guard_target_tilt
                
                # MOTION PHASE: Smooth interpolation to next point
                else:
                    if not self._guard_in_motion:
                        # Start moving to next point
                        self._guard_in_motion = True
                        self._guard_move_start_time = current_time
                        self._guard_move_start_pan = self.target_pan
                        self._guard_move_start_tilt = self.target_tilt
                    
                    # Calculate movement distance and progress
                    move_elapsed = current_time - self._guard_move_start_time
                    pan_diff = abs(self._guard_target_pan - self._guard_move_start_pan)
                    tilt_diff = abs(self._guard_target_tilt - self._guard_move_start_tilt)
                    total_distance = np.sqrt(pan_diff**2 + tilt_diff**2)
                    
                    # Calculate transition time based on distance and speed
                    # At 100% speed: 45° takes 0.5 sec. At 50%: 45° takes 1.0 sec
                    base_move_time = max(0.2, total_distance / (45.0 * movement_speed + 0.1))
                    progress = min(1.0, move_elapsed / base_move_time)
                    
                    # Smooth easing: quadratic ease-in-out for natural motion
                    if progress < 0.5:
                        easing = 2 * progress * progress
                    else:
                        easing = 1 - 2 * (1 - progress) ** 2
                    
                    # Interpolate current position smoothly toward target
                    self.target_pan = self._guard_move_start_pan + (self._guard_target_pan - self._guard_move_start_pan) * easing
                    self.target_tilt = self._guard_move_start_tilt + (self._guard_target_tilt - self._guard_move_start_tilt) * easing
                    
                    # Check if motion is complete (progress reached 100%)
                    if progress >= 1.0:
                        # Snap to exact final position
                        self.target_pan = self._guard_target_pan
                        self.target_tilt = self._guard_target_tilt
                        
                        # Prepare for next patrol point and reset dwell timer
                        self._guard_in_motion = False
                        next_point = idle_modes.guard_get_next_point()
                        self._guard_target_pan = float(next_point[0])
                        self._guard_target_tilt = float(next_point[1])
                        self._idle_mode_state_time = current_time  # Reset dwell timer
            
            # WATCH MODE: Sweep between two positions
            elif current_mode == 'watch':
                watch_config = idle_modes.get_watch_config()
                left_limit = watch_config.get('left_limit', 45)
                right_limit = watch_config.get('right_limit', 135)
                pause_time = watch_config.get('pause_time', 2)
                sweep_speed = watch_config.get('sweep_speed', 50) / 100.0  # Convert % to 0-1
                
                elapsed = current_time - self._idle_mode_state_time
                
                # Get direction and limits
                if not hasattr(self, '_watch_direction'):
                    self._watch_direction = 1  # 1 = right, -1 = left
                
                # Pan speed: max 2.5°/frame at 30fps = 75°/sec at 100%
                pan_speed = 75.0 * sweep_speed / 30.0  # degrees per update cycle
                
                # Check if pause time at end of sweep
                if elapsed > pause_time:
                    # Move toward limit
                    new_pan = self.target_pan + (pan_speed * self._watch_direction)
                    
                    # Check if we've reached limit
                    if self._watch_direction == 1 and new_pan >= right_limit:
                        self.target_pan = float(right_limit)
                        self._watch_direction = -1  # Reverse direction
                        self._idle_mode_state_time = current_time  # Start pause time
                    elif self._watch_direction == -1 and new_pan <= left_limit:
                        self.target_pan = float(left_limit)
                        self._watch_direction = 1  # Reverse direction
                        self._idle_mode_state_time = current_time  # Start pause time
                    else:
                        self.target_pan = float(np.clip(new_pan, left_limit, right_limit))
            
            # SEARCH MODE: Random movement in area
            elif current_mode == 'search':
                search_config = idle_modes.get_search_config()
                movement_style = search_config.get('movement_style', 'random')
                direction_change_time = search_config.get('direction_changes', 5)
                
                elapsed = current_time - self._idle_mode_state_time
                
                # Get new random position when time expires
                if elapsed > direction_change_time or not hasattr(self, '_search_target_pan'):
                    next_pos = idle_modes.search_get_next_position()
                    self._search_target_pan = float(next_pos[0])
                    self._search_target_tilt = float(next_pos[1])
                    self._idle_mode_state_time = current_time
                
                # Smooth movement toward target
                search_speed = idle_modes.search_get_speed()
                
                # Calculate distance to target
                pan_diff = self._search_target_pan - self.target_pan
                tilt_diff = self._search_target_tilt - self.target_tilt
                distance = np.sqrt(pan_diff**2 + tilt_diff**2)
                
                # Move toward target with speed control
                if distance > 1.0:  # Only move if distance > 1 degree
                    speed_factor = (search_speed / 100.0)  # 0-1
                    max_step = 3.0 * speed_factor  # Max 3°/cycle at 100% speed
                    
                    # Normalize and scale movement
                    if distance > 0:
                        pan_step = (pan_diff / distance) * max_step
                        tilt_step = (tilt_diff / distance) * max_step
                        
                        self.target_pan = float(np.clip(
                            self.target_pan + pan_step,
                            search_config['search_area']['pan_min'],
                            search_config['search_area']['pan_max']
                        ))
                        self.target_tilt = float(np.clip(
                            self.target_tilt + tilt_step,
                            search_config['search_area']['tilt_min'],
                            search_config['search_area']['tilt_max']
                        ))
            
            # Clear REST mode timer if mode has changed away from REST
            else:
                try:
                    if hasattr(self, '_rest_mode_start_time'):
                        delattr(self, '_rest_mode_start_time')
                    # Bug #3 FIX: Also clean up watch and search mode variables when switching modes
                    if hasattr(self, '_watch_direction'):
                        delattr(self, '_watch_direction')
                    if hasattr(self, '_search_target_pan'):
                        delattr(self, '_search_target_pan')
                    if hasattr(self, '_search_target_tilt'):
                        delattr(self, '_search_target_tilt')
                except Exception:
                    pass
                    
        except Exception as e:
            # Log error but don't crash - idle modes are non-critical
            try:
                if hasattr(self, 'enhancer'):
                    self.enhancer.log_serial_output(f"Idle mode update error: {e}", fire=False)
            except Exception:
                pass

    def send_serial_command(self):
        # ========== QUICK TARGET LOCK OVERRIDE ==========
        # If target lock is active, move toward target position instead of normal tracking
        # This temporarily overrides detection/tracking until we reach the target or timeout
        try:
            if getattr(self, "target_lock_active", False):
                current_time = time.time()
                lock_start = getattr(self, "target_lock_start_time", current_time)
                lock_timeout = getattr(self, "target_lock_timeout", 5.0)
                
                # Check timeout - if exceeded, cancel lock and resume normal tracking
                if current_time - lock_start > lock_timeout:
                    self.target_lock_active = False
                    self.enhancer.log_serial_output(
                        "[LOCK] ⏱️ Timeout - resuming autotracking",
                        fire=False
                    )
                    # Let normal tracking resume in the next iteration
                    # (this iteration will still use the timeout-triggered pan/tilt values)
                else:
                    # Lock still active - move toward target
                    target_pan = getattr(self, "target_lock_pan", 90)
                    target_tilt = getattr(self, "target_lock_tilt", 40)
                    current_pan = getattr(self, "last_sent_pan", getattr(self, "prev_pan_angle", 90))
                    current_tilt = getattr(self, "last_sent_tilt", getattr(self, "prev_tilt_angle", 40))
                    
                    # Calculate distance to target
                    pan_distance = abs(target_pan - current_pan)
                    tilt_distance = abs(target_tilt - current_tilt)
                    tolerance = getattr(self, "target_lock_tolerance", 3.0)
                    
                    # Check if we've reached the target (within tolerance)
                    if pan_distance <= tolerance and tilt_distance <= tolerance:
                        # Arrived at target! Resume normal tracking
                        self.target_lock_active = False
                        self.enhancer.log_serial_output(
                            f"[LOCK] ✅ Arrived at target (pan={target_pan:.0f}°, tilt={target_tilt:.0f}°)",
                            fire=False
                        )
                        # Resume normal autotracking if it was active before
                        if getattr(self, "tracking_was_active", False):
                            self.tracking_active = True
                            self.enhancer.log_serial_output(
                                "[LOCK] Resuming autotracking",
                                fire=False
                            )
                    else:
                        # Still moving toward target - use target position as servo command
                        self.target_pan = target_pan
                        self.target_tilt = target_tilt
                        # Don't exit send_serial_command() yet - continue below to send the command
        except Exception as e:
            # If lock processing fails, clean up and continue with normal command
            self.target_lock_active = False
            try:
                self.enhancer.log_serial_output(
                    f"[LOCK ERROR] {e}",
                    fire=False
                )
            except Exception:
                pass
        
        # ========== END QUICK TARGET LOCK OVERRIDE ==========
        
        # Increment diagnostic counter
        self._send_serial_cmd_count = getattr(self, "_send_serial_cmd_count", 0) + 1
        
        # Update idle mode positions before sending (if no manual/tracking override)
        try:
            self._update_idle_mode_positions()
        except Exception:
            pass
        
        # Use target_pan/tilt as intended, but only update last_sent_* when writing to serial.
        target_pan_raw = getattr(self, "target_pan", 90)
        target_tilt_raw = getattr(self, "target_tilt", 40)
        
        # ========== FIXED: VALIDATE PAN/TILT ANGLES BEFORE COMMAND ENCODING ==========
        # Ensure pan/tilt angles are valid numbers (not NaN, not Inf)
        # If invalid, log warning and use safe defaults instead of malformed command
        try:
            if not isinstance(target_pan_raw, (int, float)):
                target_pan_raw = 90
            elif math.isnan(target_pan_raw) or math.isinf(target_pan_raw):
                target_pan_raw = 90
            if not isinstance(target_tilt_raw, (int, float)):
                target_tilt_raw = 40
            elif math.isnan(target_tilt_raw) or math.isinf(target_tilt_raw):
                target_tilt_raw = 40
        except Exception:
            target_pan_raw = 90
            target_tilt_raw = 40
        
        # ========== CRITICAL FIX: USE ROUNDING FOR FRACTIONAL ANGLES ==========
        # ISSUE: int() truncates: 50.7° becomes 50° (loses 0.7°)
        # RESULT: Tilt appears unresponsive - fractional movements accumulate but never reach MCU
        # SOLUTION: round() properly converts: 50.7° becomes 51° (preserves fractional accuracy)
        # This ensures both pan and tilt respond equally to small tracking corrections
        pan_angle = int(np.round(np.clip(target_pan_raw, self.PAN_MIN, self.PAN_MAX)))
        tilt_angle = int(np.round(np.clip(target_tilt_raw, self.TILT_MIN, self.TILT_MAX)))
        
        # ========== TRANSMISSION DIAGNOSTICS ==========
        # Log rounding impact to verify fractional values are properly converted
        try:
            if getattr(self, "debug_checkbox", None) and self.debug_checkbox.isChecked():
                pan_rounded = target_pan_raw - int(target_pan_raw)
                tilt_rounded = target_tilt_raw - int(target_tilt_raw)
                self.enhancer.log_serial_output(
                    f"[TILT_SEND] raw={target_tilt_raw:.4f}° → rounded_int={tilt_angle}° (frac={tilt_rounded:.4f} loss={-tilt_rounded if target_tilt_raw > 0 else tilt_rounded:.4f})",
                    fire=False
                )
        except Exception:
            pass
        
        # ========== FIXED: UPDATE POSITION LABEL DURING TRACKING ==========
        # Position label should show current target pan/tilt values while tracking is active
        # (Previously only updated in manual control, showing stale values during tracking)
        try:
            if getattr(self, "tracking_active", False) and hasattr(self, "position_label"):
                self.position_label.setText(f"Pan: {pan_angle}° | Tilt: {tilt_angle}°")
        except Exception:
            pass
        
        # DIAGNOSTIC: Log when approaching minimum position (indicates potential tracking issue)
        if pan_angle <= self.PAN_MIN + 5 or tilt_angle <= self.TILT_MIN + 5:
            try:
                if getattr(self, "enhancer", None):
                    self.enhancer.log_serial_output(
                        f"[SERVO] Warning: approaching MIN position - pan={pan_angle}° (MIN={self.PAN_MIN}), tilt={tilt_angle}° (MIN={self.TILT_MIN})",
                        fire=False
                    )
            except Exception:
                pass

        # If MCU reports tilt safety locked, avoid sending new tilt targets to
        # prevent host/firmware fighting. Use the last_sent_tilt as the desired
        # angle to keep commands stable while the MCU enforces the safe position.
        try:
            if getattr(self, "_mcu_tilt_safety_locked", False):
                tilt_angle = int(getattr(self, "last_sent_tilt", tilt_angle))
        except Exception:
            pass

        # self.prev_pan_angle = pan_angle
        # self.prev_tilt_angle = tilt_angle

        # Predefine debug_on so later references are always bound even if
        # the diagnostic logging block raises an exception.
        debug_on = False

        fire_token = 1 if self.trigger_fired else 0
        led_token = int(self.relay1_state)
        laser_token = int(self.relay2_state)
        acc3_token = 0
        safety_token = int(self.safety_state)
        mode_token = 1 if self.trigger_mode_bb else 0

        command = f"P{pan_angle}T{tilt_angle}F{fire_token}L{led_token}R{laser_token}G{acc3_token}S{safety_token}M{mode_token}\n"
        
        # ========== BULLETPROOF FIX: PREVENT REDUNDANT SERVO COMMANDS ==========
        # ISSUE: Sending same command repeatedly causes servo jitter/hunting/twitching
        # The servo can't distinguish between "move to 40°" and "stay at 40°"
        # SOLUTION: Only send command if the ROUNDED integer values actually changed
        # This prevents the servo from receiving duplicate commands while tracking micro-movements
        should_send = True
        last_pan = int(getattr(self, "last_sent_pan", -9999))
        last_tilt = int(getattr(self, "last_sent_tilt", -9999))
        
        if (pan_angle == last_pan and 
            tilt_angle == last_tilt and 
            fire_token == int(getattr(self, "_last_fire_token", 0)) and
            led_token == int(getattr(self, "_last_led_token", 0)) and
            laser_token == int(getattr(self, "_last_laser_token", 0)) and
            safety_token == int(getattr(self, "_last_safety_token", 0)) and
            mode_token == int(getattr(self, "_last_mode_token", 0))):
            should_send = False

        # Log unchanged commands only in debug mode
        if not should_send and debug_on:
            try:
                if getattr(self, "enhancer", None):
                    self.enhancer.log_serial_output(
                        f"[REDUNDANT] Command unchanged: P{pan_angle}T{tilt_angle} (skipping send)",
                        fire=False
                    )
            except Exception:
                pass

        # Log the command (useful for verification even if serial is not connected)
        try:
            # If Debug is enabled, include an expanded diagnostic line showing key internal state
            debug_on = False
            try:
                debug_on = bool(
                    getattr(self, "debug_checkbox", None)
                    and self.debug_checkbox.isChecked()
                )
            except Exception:
                debug_on = False

            # Only log if we're actually sending or debug is on
            if should_send or debug_on:
                msg = f"WILL SEND: {command.strip()}"
                if debug_on:
                    try:
                        st = (
                            f"[DBG] prev_pan={getattr(self,'prev_pan_angle',None)} prev_tilt={getattr(self,'prev_tilt_angle',None)} "
                            f"last_sent_pan={getattr(self,'last_sent_pan',None)} last_sent_tilt={getattr(self,'last_sent_tilt',None)} "
                            f"target_pan={getattr(self,'target_pan',None)} target_tilt={getattr(self,'target_tilt',None)} "
                            f"manual_override={getattr(self,'manual_override',False)} _manual_override_active={getattr(self,'_manual_override_active',False)} safety_state={getattr(self,'safety_state',None)} aiming_active={getattr(self,'aiming_active',False)}"
                        )
                        msg = msg + " " + st
                    except Exception:
                        pass

                if (
                    hasattr(self, "enhancer")
                    and getattr(self, "enhancer", None) is not None
                ):
                    try:
                        self.enhancer.log_serial_output(msg, fire=False)
                    except Exception:
                        try:
                            self._safe_append_log(msg)
                        except Exception:
                            pass
                else:
                    try:
                        # Fallback: always print to console when running headless tests
                        print(msg)
                    except Exception:
                        try:
                            self._safe_append_log(msg)
                        except Exception:
                            pass
        except Exception:
            pass

        # ========== ONLY SEND IF COMMAND ACTUALLY CHANGED ==========
        if not should_send:
            return  # Skip sending - command is identical to last time

        if self.ser is not None and getattr(self.ser, "is_open", False):
            try:
                # Optionally suppress actual hardware writes when operator toggles Pause TX
                if getattr(self, "serial_tx_paused", False):
                    # Do not write to hardware, but still record intended last_sent values so
                    # hold/restore logic behaves consistently in simulated or paused-TX modes.
                    self.last_sent_pan = pan_angle
                    self.last_sent_tilt = tilt_angle
                    # FIX DEC8: Update prev from sent integer values (not fractional target)
                    self.prev_pan_angle = float(pan_angle)
                    self.prev_tilt_angle = float(tilt_angle)
                    # Optionally log the suppression in debug mode
                    try:
                        if debug_on:
                            if hasattr(self, "enhancer"):
                                try:
                                    self.enhancer.log_serial_output(
                                        "SERIAL TX PAUSED — suppressed sending command", fire=False
                                    )
                                except Exception:
                                    try:
                                        self._serial_write("SERIAL TX PAUSED — suppressed sending command")
                                    except Exception:
                                        pass
                            else:
                                try:
                                    self._serial_write("SERIAL TX PAUSED — suppressed sending command")
                                except Exception:
                                    pass
                    except Exception:
                        pass
                else:
                    self.ser.write(command.encode("utf-8"))
                    # update last_sent_* only when we actually wrote to serial
                    self.last_sent_pan = pan_angle
                    self.last_sent_tilt = tilt_angle
                    # FIX DEC8: Update prev_pan_angle/prev_tilt_angle from SENT integer values
                    # NOT from target_pan/target_tilt (which have fractional parts)
                    # This prevents oscillation from fractional-to-integer rounding mismatches
                    # The key insight: prev values must match what MCU actually received
                    self.prev_pan_angle = float(pan_angle)  # Use what was ACTUALLY sent to MCU
                    self.prev_tilt_angle = float(tilt_angle)

                    # read a possible response
                    try:
                        if self.ser.in_waiting > 0:
                            response = self.ser.readline().decode("utf-8").strip()
                            if response:
                                # use enhancer if attached to color logs
                                try:
                                    is_fire = "FIRE" in response.upper()
                                    if hasattr(self, "enhancer"):
                                        self.enhancer.log_serial_output(
                                            f"ARDUINO: {response}", fire=is_fire
                                        )
                                    else:
                                        try:
                                            self._safe_append_log(f"ARDUINO: {response}")
                                        except Exception:
                                            pass
                                    # --- Host-side parsing of MCU safety messages ---
                                    try:
                                        uresp = response.upper()
                                        # If the MCU reports a tilt safety trigger, remember it so the
                                        # host can avoid sending tilt commands and entering a fight
                                        # with the firmware's safety override.
                                        if "TILT SAFETY SWITCH TRIGGERED" in uresp or "SAFETY LOCKED" in uresp:
                                            try:
                                                self._mcu_tilt_safety_locked = True
                                                if hasattr(self, "enhancer"):
                                                    self.enhancer.log_serial_output(
                                                        "[HOST] MCU reports tilt safety LOCKED — suppressing tilt commands",
                                                        fire=False,
                                                    )
                                                else:
                                                    try:
                                                        self._safe_append_log("[HOST] MCU reports tilt safety LOCKED — suppressing tilt commands")
                                                    except Exception:
                                                        pass
                                            except Exception:
                                                pass
                                        # Clear lock when MCU reports reset/disabled state
                                        if (
                                            "TILT SAFETY SWITCH RESET" in uresp
                                            or "TILT SAFETY HANDLER DISABLED" in uresp
                                            or "TILT SAFETY SWITCH ENABLED" in uresp
                                            or "TILT SAFETY HANDLER DISABLED" in uresp
                                        ):
                                            try:
                                                self._mcu_tilt_safety_locked = False
                                                if hasattr(self, "enhancer"):
                                                    self.enhancer.log_serial_output(
                                                        "[HOST] MCU reports tilt safety CLEARED",
                                                        fire=False,
                                                    )
                                                else:
                                                    try:
                                                        self._safe_append_log("[HOST] MCU reports tilt safety CLEARED")
                                                    except Exception:
                                                        pass
                                            except Exception:
                                                pass
                                    except Exception:
                                        pass
                                    
                                    # --- Parse encoder feedback from MCU ---
                                    try:
                                        if "ENCODER_TILT" in response:
                                            self.parse_encoder_response(response)
                                    except Exception:
                                        pass
                                    
                                    # extend the UI pulse when MCU confirms a fire
                                    if is_fire:
                                        try:
                                            self._pulse_fire_indicator(confirmed=True)
                                        except Exception:
                                            pass
                                except Exception:
                                    try:
                                        self._safe_append_log(f"ARDUINO: {response}")
                                    except Exception:
                                        pass
                    except Exception:
                        pass
            except Exception as e:
                try:
                    if hasattr(self, "enhancer"):
                        self.enhancer.log_serial_output(f"Serial Write Error: {e}")
                    else:
                        try:
                            self._safe_append_log(f"Serial Write Error: {e}")
                        except Exception:
                            pass
                except Exception:
                    try:
                        self._safe_append_log(f"Serial Write Error: {e}")
                    except Exception:
                        pass
                # try to close and cleanup
                try:
                    self.ser.close()
                except Exception:
                    pass
                self.ser = None
                try:
                    self.connect_button.setText("Connect")
                except Exception:
                    pass

        # If serial wasn't open, still update last_sent_* so hold-on-loss logic
        # can prefer the most recently intended angles (helps simulated/run-without-serial).
        try:
            if not (self.ser is not None and getattr(self.ser, "is_open", False)):
                # record the intended values as 'last_sent' so hold logic can use them
                self.last_sent_pan = pan_angle
                self.last_sent_tilt = tilt_angle
                # FIX DEC8: Update prev from sent integer values (not fractional target)
                self.prev_pan_angle = float(pan_angle)
                self.prev_tilt_angle = float(tilt_angle)
        except Exception:
            pass

        # --- Tilt Encoder Feedback & PID Update ---
        # NOTE: Encoder is ONLY active when PID control is ENABLED
        # When PID is disabled, encoder has ZERO effect on auto-tracking
        # Poll encoder periodically (every 30ms for snappy tracking)
        # More frequent polling = more responsive tilt boost
        try:
            now = time.time()
            # CRITICAL GATE: Only process encoder if PID is enabled
            # This ensures encoder never affects tracking logic when PID is disabled
            if self.tilt_pid_enabled:  # <-- MASTER GATE FOR ALL ENCODER OPERATIONS
                if now - self.last_encoder_read_time >= 0.03:  # 30ms polling interval
                    if self.tilt_encoder_enabled:
                        self.request_encoder_feedback()
                        self.last_encoder_read_time = now
                    
                    # CRITICAL FIX: Update target tilt BEFORE calculating boost
                    # This ensures encoder position_error is calculated against current target
                    try:
                        self.tilt_servo_target = int(getattr(self, "target_tilt", self.HOME_TILT))
                    except Exception:
                        self.tilt_servo_target = int(self.HOME_TILT)
                    
                    # Monitor PID behavior for tuning purposes
                    if self.tilt_pid_enabled:
                        self.update_tilt_pid_control()
            else:
                # CRITICAL FIX: When PID is disabled, disable encoder too and reset all state
                # This prevents encoder from interfering with normal tilt movement
                self.tilt_encoder_enabled = False
                self.tilt_position_error = 0.0
                self._tilt_pid_integral = 0.0
                self._tilt_pid_last_error = 0.0
        except Exception:
            pass

        # ========== CACHE CURRENT COMMAND TOKENS FOR NEXT CYCLE ==========
        # Store the tokens we sent this cycle so next cycle can detect if anything changed
        self._last_fire_token = fire_token
        self._last_led_token = led_token
        self._last_laser_token = laser_token
        self._last_safety_token = safety_token
        self._last_mode_token = mode_token

        # ensure we reset trigger_fired
        self.trigger_fired = False

    # ========== TILT ENCODER FEEDBACK FUNCTIONS ==========
    
    def request_encoder_feedback(self):
        """Request current tilt encoder position from Arduino."""
        try:
            if self.ser is not None and getattr(self.ser, "is_open", False):
                self.ser.write(b"GET_ENCODER\n")
                return True
        except Exception:
            pass
        return False
    
    def parse_encoder_response(self, response):
        """
        Parse encoder feedback response from Arduino.
        Expected format: ENCODER_TILT,<tilt>,RAW_COUNT,<count>
        CRITICAL: This is now always processed to sync position on reconnect
        Previously was guarded by PID enablement, causing position loss on disconnect
        """
        try:
            if "ENCODER_TILT" in response:
                parts = response.split(',')
                if len(parts) >= 4:
                    tilt_str = parts[1].strip()
                    count_str = parts[3].strip()
                    
                    # ENCODER CLAMP FIX: Constrain encoder readings to physical limits (18-90°)
                    # Without this, encoder can report 94°, 98°, 110°+ when tilt oscillates at limit
                    # This causes massive corrective movements making system "go crazy"
                    raw_tilt = float(tilt_str)
                    self.tilt_encoder_position = max(18, min(90, raw_tilt))
                    
                    if raw_tilt != self.tilt_encoder_position:
                        self.enhancer.log_serial_output(
                            f"[ENCODER CLAMP] Raw {raw_tilt:.1f}° -> Clamped {self.tilt_encoder_position:.1f}°",
                            fire=False
                        )
                    
                    self.tilt_encoder_raw_count = int(count_str)
                    
                    # POSITION SYNC FIX: Update last_sent_tilt when we get encoder feedback
                    # This ensures Go Home uses the actual hardware position as baseline
                    # Especially important on reconnect when physical position may differ from host's cached value
                    self.last_sent_tilt = int(self.tilt_encoder_position)
                    
                    # Only do PID-related processing if PID is enabled
                    if self.tilt_pid_enabled:
                        # CRITICAL FIX: Calculate position error correctly
                        # Error = target - actual
                        self.tilt_position_error = self.tilt_servo_target - self.tilt_encoder_position
                        
                        # ========== ENCODER LIMIT DETECTION ==========
                        # Track the physical boundaries detected by the encoder
                        # When the encoder reports a position, it's a physical constraint
                        if not hasattr(self, "encoder_tilt_min_detected"):
                            self.encoder_tilt_min_detected = self.tilt_encoder_position
                            self.encoder_tilt_max_detected = self.tilt_encoder_position
                        else:
                            # Update min if we found a lower position
                            if self.tilt_encoder_position < self.encoder_tilt_min_detected:
                                self.encoder_tilt_min_detected = self.tilt_encoder_position
                                self.enhancer.log_serial_output(
                                    f"[ENCODER LIMIT] NEW MIN DETECTED: {self.encoder_tilt_min_detected:.1f}°",
                                    fire=False
                                )
                            # Update max if we found a higher position
                            if self.tilt_encoder_position > self.encoder_tilt_max_detected:
                                self.encoder_tilt_max_detected = self.tilt_encoder_position
                                self.enhancer.log_serial_output(
                                    f"[ENCODER LIMIT] NEW MAX DETECTED: {self.encoder_tilt_max_detected:.1f}°",
                                    fire=False
                                )
                    
                    # Log encoder update if debug enabled (always log position sync)
                    try:
                        if getattr(self, "debug_checkbox", None) and self.debug_checkbox.isChecked():
                            self.enhancer.log_serial_output(
                                f"[ENCODER] Tilt: {self.tilt_encoder_position:.1f}° (target: {self.tilt_servo_target}°, error: {self.tilt_position_error:+.1f}°, limits: {self.encoder_tilt_min_detected:.1f}°-{self.encoder_tilt_max_detected:.1f}°, PID_ON={self.tilt_pid_enabled})",
                                fire=False
                            )
                    except Exception:
                        pass
                    
                    return True
        except Exception:
            pass
        return False
    
    def update_tilt_pid_control(self):
        """
        Update PID-based tilt correction using encoder feedback.
        NOTE: This is informational only. The Arduino handles PID corrections.
        This Python function monitors PID behavior for tuning purposes.
        """
        if not self.tilt_pid_enabled or not self.tilt_encoder_enabled:
            return
        
        try:
            now = time.time()
            dt = now - self._tilt_pid_last_update_time
            
            # Only update every 100ms (for monitoring, not control)
            if dt < 0.1:
                return
            
            self._tilt_pid_last_update_time = now
            
            # Calculate error
            error = self.tilt_position_error  # Already calculated in parse_encoder_response
            
            # PID calculations (monitoring only - Arduino handles actual corrections)
            # Proportional
            p_term = self.tilt_pid_kp * error
            
            # Integral (with anti-windup)
            self._tilt_pid_integral += error * dt
            self._tilt_pid_integral = max(min(self._tilt_pid_integral, 5.0), -5.0)
            i_term = self.tilt_pid_ki * self._tilt_pid_integral
            
            # Derivative
            d_term = self.tilt_pid_kd * (error - self._tilt_pid_last_error) / dt if dt > 0 else 0
            self._tilt_pid_last_error = error
            
            # Total PID output (for monitoring)
            pid_output = p_term + i_term + d_term
            
            # Log PID monitoring data if debug enabled
            if abs(error) > 0.5:  # Only log if there's meaningful error
                try:
                    if getattr(self, "debug_checkbox", None) and self.debug_checkbox.isChecked():
                        self.enhancer.log_serial_output(
                            f"[PID_MON] error={error:+.2f}° P={p_term:.2f} I={i_term:.2f} D={d_term:.2f} output={pid_output:.2f}",
                            fire=False
                        )
                except Exception:
                    pass
        
        except Exception as e:
            try:
                self.enhancer.log_serial_output(f"[PID_MON ERROR] {str(e)}", fire=False)
            except Exception:
                pass
    
    def enable_encoder_feedback(self, enable=True):
        """Enable or disable tilt encoder feedback processing."""
        self.tilt_encoder_enabled = enable
        try:
            status = "ENABLED" if enable else "DISABLED"
            self.enhancer.log_serial_output(
                f"Tilt encoder feedback: {status}",
                fire=False
            )
        except Exception:
            pass
    
    def enable_tilt_pid_control(self, enable=True):
        """Enable or disable PID-based tilt correction."""
        self.tilt_pid_enabled = enable
        try:
            status = "ENABLED" if enable else "DISABLED"
            self.enhancer.log_serial_output(
                f"Tilt PID control: {status}",
                fire=False
            )
        except Exception:
            pass
    
    def set_home_speed(self, speed_percent):
        """
        Set homing speed on Arduino (1-100%).
        Lower values = slower, smoother homing.
        """
        try:
            speed_percent = int(np.clip(speed_percent, 1, 100))
            self.home_speed_percent = speed_percent
            
            if self.ser is not None and getattr(self.ser, "is_open", False):
                command = f"HOMESPEED_S{speed_percent}\n"
                self.ser.write(command.encode("utf-8"))
                self.enhancer.log_serial_output(
                    f"Homing speed: {speed_percent}%",
                    fire=False
                )
                return True
        except Exception as e:
            try:
                self.enhancer.log_serial_output(f"[HOMESPEED ERROR] {str(e)}", fire=False)
            except Exception:
                pass
        return False

    # ========== END TILT ENCODER FEEDBACK FUNCTIONS ==========

    def _diagnostic_check_serial_connection(self):
        """Check and log serial connection status for debugging NO MOVEMENT issues."""
        try:
            ser_is_none = self.ser is None
            ser_is_open = False
            ser_port = "NONE"
            if self.ser is not None:
                ser_is_open = getattr(self.ser, "is_open", False)
                ser_port = getattr(self.ser, "port", "UNKNOWN")
            
            tx_paused = getattr(self, "serial_tx_paused", False)
            tracking = getattr(self, "tracking_active", False)
            aiming = getattr(self, "aiming_active", False)
            cmd_count = getattr(self, "_send_serial_cmd_count", 0)
            
            diag_msg = (
                f"[SERIAL DIAG] ser_is_none={ser_is_none} ser_is_open={ser_is_open} "
                f"port={ser_port} tx_paused={tx_paused} tracking={tracking} aiming={aiming} "
                f"send_cmd_calls={cmd_count}"
            )
            
            if hasattr(self, "enhancer"):
                try:
                    self.enhancer.log_serial_output(diag_msg, fire=False)
                except Exception:
                    print(diag_msg)
            else:
                print(diag_msg)
            
            # Also log potential issues
            if ser_is_none:
                issue_msg = "[ISSUE] Serial port object is None - not connected!"
                if hasattr(self, "enhancer"):
                    try:
                        self.enhancer.log_serial_output(issue_msg, fire=False)
                    except Exception:
                        print(issue_msg)
                else:
                    print(issue_msg)
            elif not ser_is_open:
                issue_msg = "[ISSUE] Serial port is closed - connection not open!"
                if hasattr(self, "enhancer"):
                    try:
                        self.enhancer.log_serial_output(issue_msg, fire=False)
                    except Exception:
                        print(issue_msg)
                else:
                    print(issue_msg)
            
            if tx_paused:
                issue_msg = "[ISSUE] TX Pause is ACTIVE - commands are suppressed!"
                if hasattr(self, "enhancer"):
                    try:
                        self.enhancer.log_serial_output(issue_msg, fire=False)
                    except Exception:
                        print(issue_msg)
                else:
                    print(issue_msg)
        except Exception as e:
            try:
                if hasattr(self, "enhancer"):
                    self.enhancer.log_serial_output(f"[DIAG ERROR] {e}", fire=False)
                else:
                    print(f"[DIAG ERROR] {e}")
            except Exception:
                pass

    def start_tracking(self):
        """Enable tracking process."""
        # CRITICAL FIX DEC14: Don't block main thread opening camera!
        # Instead, set flag and let update_frame() open it in background via threading
        # This prevents GUI freeze when camera is slow/unavailable
        
        # Check if camera is already open
        try:
            cap_ok = bool(
                getattr(self, "cap", None)
                and getattr(self.cap, "isOpened", lambda: False)()
            )
        except Exception:
            cap_ok = False

        # Enable tracking IMMEDIATELY - don't wait for camera!
        # If camera not open, it will be opened asynchronously without blocking UI
        self.tracking_active = True
        
        if not cap_ok:
            # Flag that we need to open camera, but don't do it on main thread!
            self._camera_open_needed = True
            try:
                self.enhancer.log_serial_output(
                    "Tracking started. Opening camera in background...",
                    fire=False,
                )
            except Exception:
                pass
        # CRITICAL FIX: Auto-enable aiming when tracking starts (was missing!)
        # This ensures servos move when targets are detected
        self.aiming_active = True
        
        # Auto-switch to Video tab when tracking starts so user sees camera feed
        try:
            if hasattr(self, 'main_tab_widget'):
                self.main_tab_widget.setCurrentIndex(1)  # Index 1 is Video tab
        except Exception:
            pass
        
        # Ensure the frame/update timer is running when tracking starts
        try:
            if getattr(self, "timer", None) is not None:
                self.timer.start(30)
        except Exception:
            pass
        # Update tracking toggle UI state
        try:
            self._safe_widget_call("tracking_btn", "setChecked", True)
            self._safe_widget_call("tracking_btn", "setText", "Stop Tracking")
        except Exception:
            pass
        try:
            # Ensure aiming toggle is available/enabled when tracking starts
            self._safe_widget_call("aiming_btn", "setEnabled", True)
            # Also update aiming button to reflect that it's now enabled
            self._safe_widget_call("aiming_btn", "setChecked", True)
        except Exception:
            pass
        # Disable idle mode button when tracking starts (can't be idle while tracking)
        try:
            idle_modes = getattr(self, "idle_modes", None)
            if idle_modes is not None:
                idle_modes.set_mode(None)  # Disable any active idle mode
            self._safe_widget_call("idle_mode_toggle_btn", "setChecked", False)
            self._safe_widget_call("idle_mode_toggle_btn", "setText", "Enable Idle Mode")
        except Exception:
            pass
        # Ensure Flip Frame (180°) is enabled by default when tracking starts
        try:
            # Use the safe helper in case UI not yet created
            self._safe_widget_call("flip_checkbox", "setChecked", True)
        except Exception:
            pass
        self.enhancer.log_serial_output("Tracking started.", fire=False)
        
        # CRITICAL FIX DEC14: Move heavy initialization to background thread!
        # YOLO model loading can block for 10-30 seconds, freezing the GUI
        # Instead, spawn async task and let tracking run immediately
        import threading
        def _init_detection_async():
            """Initialize detection model in background without blocking UI."""
            try:
                # DIAGNOSTIC: Log serial connection status now that tracking has started
                self._diagnostic_check_serial_connection()
                
                # Initialize background subtractor if that mode is selected
                try:
                    detection_mode = int(
                        self._safe_current_index("detection_mode_combo", 0) or 0
                    )
                    try:
                        self.enhancer.log_serial_output(
                            f"Starting tracking with detection mode index: {detection_mode}",
                            fire=False,
                        )
                    except Exception:
                        pass
                    if detection_mode == 1:
                        try:
                            self.backSub = cv2.createBackgroundSubtractorMOG2()
                            # initialize warmup counter (frames to observe before emitting detections)
                            try:
                                self.backsub_warmup = int(
                                    self._safe_int_widget_value("backsub_warmup_input", 30)
                                )
                            except Exception:
                                self.backsub_warmup = 30
                            self.enhancer.log_serial_output(
                                "Using Background Subtraction mode.", fire=False
                            )
                        except Exception:
                            pass
                    elif detection_mode == 2:
                        try:
                            model_name = (
                                self._safe_widget_method_return(
                                    "yolo_model_combo", "currentText", ""
                                )
                                or ""
                            )
                            try:
                                ml = bool(getattr(self.yolo_detector, "model_loaded", False))
                            except Exception:
                                ml = False
                            # Also report available YOLO models for diagnostics
                            try:
                                models = []
                                try:
                                    models = list(self.yolo_detector.find_models())
                                except Exception:
                                    models = []
                                self.enhancer.log_serial_output(
                                    f"Available YOLO models: {models}", fire=False
                                )
                            except Exception:
                                pass
                            try:
                                self.enhancer.log_serial_output(
                                    f"YOLO model requested: {model_name}; model_loaded={ml}",
                                    fire=False,
                                )
                            except Exception:
                                pass
                            if model_name:
                                try:
                                    print(f"[YOLO-INIT] Starting model load in background: {model_name}")
                                    self.yolo_detector.load_model(model_name)
                                    print(f"[YOLO-INIT] Model loaded successfully")
                                except Exception as e:
                                    print(f"[YOLO-INIT] Error loading model: {e}")
                                    pass
                                try:
                                    classes = (
                                        self._safe_widget_method_return(
                                            "yolo_classes_input", "text", "person"
                                        )
                                        or "person"
                                    )
                                    self.yolo_detector.set_target_classes(classes)
                                except Exception:
                                    pass
                                try:
                                    self.enhancer.log_serial_output(
                                        f"Using YOLO mode with model: {model_name}", fire=False
                                    )
                                except Exception:
                                    pass
                        except Exception:
                            pass
                except Exception:
                    pass
            except Exception as e:
                print(f"[INIT-ASYNC ERROR] {e}")
                import traceback
                traceback.print_exc()
        
        # Start detection initialization in background thread (daemon so doesn't block shutdown)
        try:
            init_thread = threading.Thread(target=_init_detection_async, daemon=True)
            init_thread.start()
        except Exception as e:
            print(f"[INIT THREAD ERROR] {e}")
            # Fallback: run synchronously if threading fails (not ideal but safer than hanging)
            try:
                _init_detection_async()
            except Exception:
                pass
        
        try:
            self.last_trigger_time = time.time()
        except Exception:
            self.last_trigger_time = 0.0

    def stop_tracking(self):
        """Disable tracking process."""
        self.tracking_active = False
        # CRITICAL FIX: Disable aiming when tracking stops (keep them in sync)
        self.aiming_active = False
        # Clear detections and update UI
        try:
            self.last_detections = []
        except Exception:
            pass
        try:
            self.video_label.clear()
            self.video_label.setText("Tracking Stopped")
        except Exception:
            pass
        try:
            self._safe_widget_call("tracking_btn", "setChecked", False)
            self._safe_widget_call("tracking_btn", "setText", "Start Tracking")
            # Also update aiming button to reflect disabled state
            self._safe_widget_call("aiming_btn", "setChecked", False)
        except Exception:
            pass
        self.enhancer.log_serial_output("Tracking stopped.", fire=False)
        # Play stop autotrack sound if available
        try:
            if hasattr(self, "enhancer") and self.enhancer:
                try:
                    self.enhancer.play_sound(self.enhancer.stop_autotrack_sound)
                except Exception:
                    pass
        except Exception:
            pass

    def toggle_aiming(self, checked=None):
        """Toggle aiming mode (servo movement enable/disable).

        If `checked` is provided (from a toggled(bool) signal), use it to set
        the aiming_active state. Otherwise, invert the current state.
        """
        try:
            if checked is None:
                self.aiming_active = not getattr(self, "aiming_active", False)
            else:
                # Ensure boolean
                try:
                    self.aiming_active = bool(checked)
                except Exception:
                    self.aiming_active = bool(getattr(self, "aiming_active", False))
        except Exception:
            self.aiming_active = False
        try:
            # Update button text if available
            if getattr(self, "aiming_btn", None) is not None:
                try:
                    self.aiming_btn.setText(
                        "Stop Aiming" if self.aiming_active else "Start Aiming"
                    )
                except Exception:
                    pass
        except Exception:
            pass
        try:
            if hasattr(self, "enhancer"):
                self.enhancer.log_serial_output(
                    (
                        "Aiming activated (servos enabled)."
                        if self.aiming_active
                        else "Aiming stopped (servos locked)."
                    ),
                    fire=False,
                )
        except Exception:
            pass
        # Ensure UI checked state matches internal flag and keep the frame timer
        # running so detection doesn't get paused on some platforms when toggling
        # the aiming button. Also emit a compact diagnostic to help users trace
        # state changes (low-risk, readonly info).
        try:
            try:
                self._safe_widget_call("aiming_btn", "setChecked", self.aiming_active)
            except Exception:
                # best-effort: if helper not available, try direct attribute
                try:
                    if getattr(self, "aiming_btn", None) is not None:
                        self.aiming_btn.setChecked(self.aiming_active)
                except Exception:
                    pass
        except Exception:
            pass
        try:
            if getattr(self, "tracking_active", False) and getattr(self, "timer", None) is not None:
                try:
                    self.timer.start(30)
                except Exception:
                    pass
        except Exception:
            pass
        try:
            # BULLETPROOF FIX: DETECTION SUPPRESSION DEPRECATED
            # Detection always runs - no need to manage suppression windows
            # All suppression code removed to prevent regression of detection loss
            if not getattr(self, "_in_go_home", False):
                # Detection is always active - no suppression to clear
                pass
        except Exception:
            pass
        try:
            # Emit a concise diagnostic line so the user can see what changed
            diag = (
                f"[AIM DIAG] aiming_active={getattr(self,'aiming_active',False)} "
                f"tracking_active={getattr(self,'tracking_active',False)} "
                f"manual_override={getattr(self,'manual_override',False)} "
                f"_manual_override_active={getattr(self,'_manual_override_active',False)} "
                f"_manual_override_until={getattr(self,'_manual_override_until',0)} "
                f"_suspend_tracking_until={getattr(self,'_suspend_tracking_until',0)} "
                f"_suppress_detection_until={getattr(self,'_suppress_detection_until',0)} "
                f"_in_go_home={getattr(self,'_in_go_home',False)} "
                f"backSub={'yes' if getattr(self,'backSub',None) is not None else 'no'}"
            )
            if hasattr(self, "enhancer"):
                try:
                    self.enhancer.log_serial_output(diag, fire=False)
                except Exception:
                    try:
                        self._safe_append_log(diag)
                    except Exception:
                        pass
            else:
                try:
                    print(diag)
                except Exception:
                    pass
        except Exception:
            pass

    def toggle_tracking(self, checked=None):
        """Toggle object detection tracking.
        
        If `checked` is provided (from a toggled(bool) signal), use it to set
        the tracking_active state. Otherwise, invert the current state.
        """
        try:
            if checked is None:
                tracking_was_active = getattr(self, "tracking_active", False)
                self.tracking_active = not tracking_was_active
            else:
                # Ensure boolean
                try:
                    self.tracking_active = bool(checked)
                except Exception:
                    self.tracking_active = bool(getattr(self, "tracking_active", False))
        except Exception:
            self.tracking_active = False
        
        try:
            if self.tracking_active:
                self.start_tracking()
                try:
                    if getattr(self, "tracking_btn", None) is not None:
                        self.tracking_btn.setText("Stop Tracking")
                        try:
                            self.tracking_btn.setChecked(True)
                        except Exception:
                            pass
                except Exception:
                    pass
            else:
                self.stop_tracking()
                try:
                    if getattr(self, "tracking_btn", None) is not None:
                        self.tracking_btn.setText("Start Tracking")
                        try:
                            self.tracking_btn.setChecked(False)
                        except Exception:
                            pass
                except Exception:
                    pass
        except Exception:
            pass

    def toggle_idle_mode(self):
        """Toggle idle mode on/off. Uses selected idle behavior from dropdown."""
        try:
            btn = getattr(self, "idle_mode_toggle_btn", None)
            if btn is None:
                if getattr(self, "enhancer", None):
                    self.enhancer.log_serial_output("[IDLE] ERROR: Toggle button not found", fire=False)
                return
            if not btn.isEnabled():
                if getattr(self, "enhancer", None):
                    self.enhancer.log_serial_output("[IDLE] ERROR: Toggle button is disabled", fire=False)
                return
            
            idle_modes = getattr(self, "idle_modes", None)
            if idle_modes is None:
                if getattr(self, "enhancer", None):
                    self.enhancer.log_serial_output("[IDLE] ERROR: Idle modes system not initialized", fire=False)
                return
            
            idle_behavior_combo = getattr(self, "idle_behavior_combo", None)
            if idle_behavior_combo is None:
                if getattr(self, "enhancer", None):
                    self.enhancer.log_serial_output("[IDLE] ERROR: Idle behavior dropdown not found", fire=False)
                return
            
            selected_behavior = idle_behavior_combo.currentText().lower()
            if not selected_behavior or selected_behavior.strip() == "":
                if getattr(self, "enhancer", None):
                    self.enhancer.log_serial_output("[IDLE] ERROR: No behavior selected in dropdown", fire=False)
                return
            
            current_mode = idle_modes.get_mode()
            
            # If idle mode is currently ACTIVE (current_mode is not None), toggle OFF
            if current_mode is not None:
                idle_modes.set_mode(None)
                # FIX: Reset combo polling tracker to prevent it from immediately re-enabling
                try:
                    combo_idx = idle_behavior_combo.currentIndex()
                    self._last_idle_behavior_combo_index = combo_idx
                except Exception:
                    pass
                
                try:
                    btn.setText("Enable Idle Mode")
                    btn.setChecked(False)
                    btn.repaint()
                    btn.update()
                except Exception:
                    pass
                if getattr(self, "enhancer", None):
                    self.enhancer.log_serial_output(f"[IDLE] Disabled idle mode (was: {current_mode})", fire=False)
                print(f"[IDLE-TOGGLE] Disabled - mode is now OFF")
            # If idle mode is currently OFF (current_mode is None), toggle ON with selected behavior
            else:
                idle_modes.set_mode(selected_behavior)
                # FIX: Reset combo polling tracker to prevent conflicts
                try:
                    combo_idx = idle_behavior_combo.currentIndex()
                    self._last_idle_behavior_combo_index = combo_idx
                except Exception:
                    pass
                
                try:
                    btn.setText("Disable Idle Mode")
                    btn.setChecked(True)
                    btn.repaint()
                    btn.update()
                except Exception:
                    pass
                if getattr(self, "enhancer", None):
                    self.enhancer.log_serial_output(f"[IDLE] Enabled {selected_behavior.capitalize()} mode", fire=False)
                print(f"[IDLE-TOGGLE] Enabled {selected_behavior} mode")
        except Exception as e:
            import traceback
            if getattr(self, "enhancer", None):
                self.enhancer.log_serial_output(f"[IDLE] CRITICAL ERROR: {str(e)}", fire=False)
                self.enhancer.log_serial_output(f"[IDLE] Traceback: {traceback.format_exc()}", fire=False)

    def toggle_serial_pause(self, checked):
        """Pause or resume serial log output."""
        try:
            self.serial_paused = checked
            status = "PAUSED" if checked else "ACTIVE"
            if getattr(self, "enhancer", None):
                self.enhancer.log_serial_output(
                    f"[SERIAL] Logging {status}"
                )
            if getattr(self, "serial_buffer_label", None):
                if checked:
                    self.serial_buffer_label.setText("Paused")
                else:
                    self.serial_buffer_label.setText("")
        except Exception as e:
            print(f"[ERROR] toggle_serial_pause: {e}")

    def toggle_serial_tx(self, checked):
        """Pause or resume serial TX (transmission to hardware)."""
        try:
            self.serial_tx_paused = checked
            status = "PAUSED" if checked else "ACTIVE"
            if getattr(self, "enhancer", None):
                self.enhancer.log_serial_output(
                    f"[SERIAL] TX {status}"
                )
        except Exception as e:
            print(f"[ERROR] toggle_serial_tx: {e}")

    def clear_serial_log(self):
        """Clear the serial output log."""
        try:
            if getattr(self, "serial_output", None):
                self.serial_output.clear()
                if getattr(self, "enhancer", None):
                    self.enhancer.log_serial_output(
                        "[SERIAL] Log cleared"
                    )
        except Exception as e:
            print(f"[ERROR] clear_serial_log: {e}")

    def export_serial_log(self):
        """Export serial log to a file."""
        try:
            if not getattr(self, "serial_output", None):
                return
            
            # Get text to export
            text = self.serial_output.toPlainText()
            if not text:
                if getattr(self, "enhancer", None):
                    self.enhancer.log_serial_output(
                        "[SERIAL] Nothing to export - log is empty"
                    )
                return
            
            # Create filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"serial_log_{timestamp}.txt"
            
            # Save to file
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(text)
                
                if getattr(self, "enhancer", None):
                    self.enhancer.log_serial_output(
                        f"[SERIAL] Log exported to {filename}"
                    )
            except Exception as e:
                if getattr(self, "enhancer", None):
                    self.enhancer.log_serial_output(
                        f"[SERIAL] Export failed: {e}"
                    )
        except Exception as e:
            print(f"[ERROR] export_serial_log: {e}")

    def apply_serial_settings(self):
        """Apply serial configuration settings."""
        try:
            # Collect settings from widgets
            settings = {}
            
            # COM Port
            if getattr(self, "com_port_input", None):
                settings["port"] = self.com_port_input.text()
            
            # Baud rate
            if getattr(self, "baud_rate_input", None):
                settings["baud_rate"] = int(self.baud_rate_input.value())
            
            # Data bits
            if getattr(self, "data_bits_combo", None):
                settings["data_bits"] = int(self.data_bits_combo.currentText())
            
            # Stop bits
            if getattr(self, "stop_bits_combo", None):
                stop_bits_text = self.stop_bits_combo.currentText()
                settings["stop_bits"] = float(stop_bits_text) if "." in stop_bits_text else int(stop_bits_text)
            
            # Parity
            if getattr(self, "parity_combo", None):
                settings["parity"] = self.parity_combo.currentText()
            
            # Flow control
            if getattr(self, "flow_control_combo", None):
                settings["flow_control"] = self.flow_control_combo.currentText()
            
            # Read timeout
            if getattr(self, "serial_timeout_spinbox", None):
                settings["timeout"] = self.serial_timeout_spinbox.value()
            
            # Save to settings.json
            try:
                existing_settings = {}
                if os.path.exists("settings.json"):
                    with open("settings.json", 'r') as f:
                        existing_settings = json.load(f)
                
                existing_settings["serial_settings"] = settings
                
                with open("settings.json", 'w') as f:
                    json.dump(existing_settings, f, indent=4)
                
                if getattr(self, "enhancer", None):
                    self.enhancer.log_serial_output(
                        "[SERIAL] Settings applied and saved"
                    )
            except Exception as e:
                if getattr(self, "enhancer", None):
                    self.enhancer.log_serial_output(
                        f"[SERIAL] Failed to save settings: {e}"
                    )
        except Exception as e:
            print(f"[ERROR] apply_serial_settings: {e}")

    def reset_serial_settings(self):
        """Reset serial settings to defaults."""
        try:
            # Reset to defaults
            if getattr(self, "com_port_input", None):
                self.com_port_input.setText("COM3")
            
            if getattr(self, "baud_rate_input", None):
                self.baud_rate_input.setValue(115200)
            
            if getattr(self, "data_bits_combo", None):
                self.data_bits_combo.setCurrentText("8")
            
            if getattr(self, "stop_bits_combo", None):
                self.stop_bits_combo.setCurrentText("1")
            
            if getattr(self, "parity_combo", None):
                self.parity_combo.setCurrentText("None")
            
            if getattr(self, "flow_control_combo", None):
                self.flow_control_combo.setCurrentText("None")
            
            if getattr(self, "serial_timeout_spinbox", None):
                self.serial_timeout_spinbox.setValue(100)
            
            if getattr(self, "enhancer", None):
                self.enhancer.log_serial_output(
                    "[SERIAL] Settings reset to defaults"
                )
        except Exception as e:
            print(f"[ERROR] reset_serial_settings: {e}")

    def browse_recording_directory(self):
        """Open file dialog to select recording directory."""
        try:
            from PyQt5.QtWidgets import QFileDialog
            
            # Get current directory from input field or use default
            current_dir = ""
            if getattr(self, "recording_dir_input", None):
                current_dir = self.recording_dir_input.text()
            
            # If empty or invalid, use default
            if not current_dir:
                current_dir = str(Path.home() / "Videos" / "Turret")
            
            # Open directory selection dialog
            selected_dir = QFileDialog.getExistingDirectory(
                self,
                "Select Recording Directory",
                current_dir,
                QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
            )
            
            # Update input field if user selected a directory
            if selected_dir:
                if getattr(self, "recording_dir_input", None):
                    self.recording_dir_input.setText(selected_dir)
                    # Auto-save the selection
                    self.save_settings()
                    if getattr(self, "enhancer", None):
                        self.enhancer.log_serial_output(
                            f"[RECORDING] Directory set to: {selected_dir}"
                        )
        except Exception as e:
            print(f"[ERROR] browse_recording_directory: {e}")
            if getattr(self, "enhancer", None):
                self.enhancer.log_serial_output(
                    f"[RECORDING] Failed to select directory: {e}"
                )

    def apply_recording_settings(self):
        """Apply and save recording configuration settings."""
        try:
            # Collect recording settings from widgets
            settings = {}
            
            # Recording enabled
            if getattr(self, "recording_enabled_checkbox", None):
                settings["recording_enabled"] = self.recording_enabled_checkbox.isChecked()
            
            # Auto-record on tracking start
            if getattr(self, "autorecord_checkbox", None):
                settings["autorecord"] = self.autorecord_checkbox.isChecked()
            
            # Video format
            if getattr(self, "video_format_combo", None):
                settings["video_format"] = self.video_format_combo.currentText()
            
            # FPS
            if getattr(self, "fps_combo", None):
                settings["fps"] = int(self.fps_combo.currentText())
            
            # Quality
            if getattr(self, "quality_combo", None):
                settings["quality"] = self.quality_combo.currentText()
            
            # Recording directory
            if getattr(self, "recording_dir_input", None):
                settings["recording_dir"] = self.recording_dir_input.text()
            
            # Storage limit in GB
            if getattr(self, "storage_limit_spinbox", None):
                settings["storage_limit_gb"] = self.storage_limit_spinbox.value()
            
            # Auto-cleanup enabled
            if getattr(self, "autocleanup_checkbox", None):
                settings["autocleanup"] = self.autocleanup_checkbox.isChecked()
            
            # Save to settings.json
            try:
                existing_settings = {}
                if os.path.exists("settings.json"):
                    with open("settings.json", 'r') as f:
                        existing_settings = json.load(f)
                
                existing_settings["recording_settings"] = settings
                
                with open("settings.json", 'w') as f:
                    json.dump(existing_settings, f, indent=4)
                
                if getattr(self, "enhancer", None):
                    self.enhancer.log_serial_output(
                        "[RECORDING] Settings applied and saved"
                    )
            except Exception as e:
                if getattr(self, "enhancer", None):
                    self.enhancer.log_serial_output(
                        f"[RECORDING] Failed to save settings: {e}"
                    )
        except Exception as e:
            print(f"[ERROR] apply_recording_settings: {e}")

    def test_recording(self):
        """Start/stop test recording for verification."""
        try:
            # Check if we already have a test recording in progress
            if getattr(self, "_test_recording_active", False):
                # Stop the test recording
                self._test_recording_active = False
                if getattr(self, "record_test_btn", None):
                    self.record_test_btn.setText("Test Recording")
                
                if getattr(self, "enhancer", None):
                    self.enhancer.log_serial_output(
                        "[RECORDING] Test recording stopped"
                    )
                return
            
            # Start test recording
            self._test_recording_active = True
            if getattr(self, "record_test_btn", None):
                self.record_test_btn.setText("Stop Testing")
            
            # Get recording settings
            recording_dir = ""
            if getattr(self, "recording_dir_input", None):
                recording_dir = self.recording_dir_input.text()
            
            if not recording_dir:
                recording_dir = str(Path.home() / "Videos" / "Turret")
            
            # Create directory if it doesn't exist
            try:
                Path(recording_dir).mkdir(parents=True, exist_ok=True)
            except Exception as e:
                if getattr(self, "enhancer", None):
                    self.enhancer.log_serial_output(
                        f"[RECORDING] Failed to create directory: {e}"
                    )
                self._test_recording_active = False
                return
            
            # Log start of test recording
            if getattr(self, "enhancer", None):
                self.enhancer.log_serial_output(
                    f"[RECORDING] Test recording started - saving to {recording_dir}"
                )
            
            # Get video format and determine extension
            video_format = "MP4 (H.264)"
            if getattr(self, "video_format_combo", None):
                video_format = self.video_format_combo.currentText()
            
            ext_map = {
                "MP4 (H.264)": ".mp4",
                "AVI (MJPEG)": ".avi",
                "MOV (H.265)": ".mov"
            }
            ext = ext_map.get(video_format, ".mp4")
            
            # Create test filename with timestamp
            import time
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            test_filename = f"test_recording_{timestamp}{ext}"
            test_filepath = str(Path(recording_dir) / test_filename)
            
            # Store test recording info for update_frame to use
            self._test_recording_filepath = test_filepath
            self._test_recording_format = video_format
            
            if getattr(self, "enhancer", None):
                self.enhancer.log_serial_output(
                    f"[RECORDING] Test file: {test_filename}"
                )
        except Exception as e:
            print(f"[ERROR] test_recording: {e}")
            self._test_recording_active = False
            if getattr(self, "enhancer", None):
                self.enhancer.log_serial_output(
                    f"[RECORDING] Test recording error: {e}"
                )

    def changeEvent(self, event):
        """Override to prevent docks and widgets from hiding when app is minimized."""
        try:
            from PyQt5.QtCore import QEvent
            
            if event.type() == QEvent.WindowStateChange:
                # When window state changes (minimize/restore), ensure docks stay visible
                if not self.isMinimized():
                    # App is being restored - re-show all dock widgets that should be visible
                    try:
                        from PyQt5.QtWidgets import QDockWidget
                        for dock in self.findChildren(QDockWidget):
                            if dock and not getattr(dock, '_user_closed', False):
                                # Only restore docks that weren't explicitly closed by user
                                if dock.isHidden():
                                    dock.show()
                    except Exception:
                        pass
        except Exception:
            pass
        
        # Call parent implementation
        super().changeEvent(event)

    def closeEvent(self, a0):
        """Ensure cleanup of resources and auto-save notes when the window is closed."""
        # Close all floating windows before app exit
        try:
            scope_window = getattr(self, 'scope_settings_window', None)
            if scope_window is not None:
                try:
                    scope_window.close()
                except Exception:
                    pass
        except Exception:
            pass
        
        # BULLETPROOF FIX: Save notes on close
        try:
            self.save_notes()
        except Exception:
            pass
        
        self.save_settings()  # V4 Save on close

        self.tracking_active = False
        self.running = False

        cap_obj = getattr(self, "cap", None)
        if cap_obj is not None:
            try:
                cap_obj.release()
            except Exception:
                pass

        ser_obj = getattr(self, "ser", None)
        if ser_obj is not None and getattr(ser_obj, "is_open", False):
            try:
                safe_cmd = f"P{getattr(self, 'prev_pan_angle', 90)}T{getattr(self, 'prev_tilt_angle', 40)}F0L0R0G0S1M0\n"
                try:
                    ser_obj.write(safe_cmd.encode("utf-8"))
                except Exception:
                    pass
                time.sleep(0.1)
                try:
                    ser_obj.close()
                except Exception:
                    pass
            except Exception:
                pass
        
        # BULLETPROOF FIX: Accept close event properly
        a0.accept()

        # NOTE: removed stray a0.accept() which ran at import time and could
        # raise a NameError. Below we attempt to apply optional UI/runtime
        # patches in a safe, non-destructive way.


if not _DISABLE_EXTERNAL_PATCHES:
    try:
        # Optional runtime patches (non-destructive). If these files are present
        # they will monkey-patch TrackingApp to apply additional UI fixes and hold-on-loss behavior.
        try:
            module = importlib.import_module("FINAL_FIXES_REFERENCE")
            patch_tracking_app = getattr(module, "patch_tracking_app", None)
            if callable(patch_tracking_app):
                try:
                    patch_tracking_app(TrackingApp)
                except Exception:
                    pass
        except Exception:
            pass

        try:
            module = importlib.import_module("FIX_Hold_Position_NoDrift")
            patch_hold_on_loss = getattr(module, "patch_hold_on_loss", None)
            if callable(patch_hold_on_loss):
                try:
                    patch_hold_on_loss(TrackingApp)
                except Exception:
                    pass
        except Exception:
            pass

        try:
            # Apply the gold UI layout last so it can override earlier patches if needed
            module = importlib.import_module("UI_LAYOUT_REFERENCE")
            patch_ui_layout = getattr(module, "patch_ui_layout", None)
            if callable(patch_ui_layout):
                try:
                    patch_ui_layout(TrackingApp)
                except Exception:
                    pass
        except Exception:
            pass
    except Exception:
        pass

if __name__ == "__main__":
    # Runtime banner (only when executed as a script)
    try:
        print("Running:", os.path.abspath(__file__))
        print("===MOVEMENT_DETECT_YOLO_ME EDITED_BY_AGENT v20251021===")
    except Exception:
        pass

    try:
        print("[MAIN] Creating QApplication...")
        app = QApplication(sys.argv)
        print("[MAIN] QApplication created successfully")
        
        print("[MAIN] Creating TrackingApp instance...")
        ex = TrackingApp()
        print("[MAIN] TrackingApp instance created successfully")
        
        # Window will be maximized by load_settings() if flag is enabled (default: True)
        # Fallback: ensure we show the window
        print("[MAIN] About to show window...")
        if not ex.isMaximized():
            ex.show()
        print("[MAIN] Window shown, entering event loop...")
        
        print("[MAIN] Running app.exec_()...")
        sys.exit(app.exec_())
    except Exception as e:
        print(f"[MAIN] CRITICAL ERROR: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


"""
Sentry Mode Tab Widget for Main App Integration

This widget provides a self-contained UI for Sentry Ambush Mode,
including its own video display, controls, and status panel.

Designed to be added as a tab in the main DADBOT application.

AGENT-MANAGED FILE: Sentry Mode Integration (Dec 2024)
See CHANGE_IMPACT_REFERENCE.md Section 12 for dependency information.
DO NOT MODIFY without checking cross-system impacts.
"""

import numpy as np
import cv2
import time
from typing import Optional, Callable, List, Tuple
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QCheckBox, QSlider, QGroupBox, QFrame, QSizePolicy,
    QSpacerItem, QScrollArea
)
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtGui import QImage, QPixmap, QMouseEvent

# Import sentry components
try:
    from .sentry_config import SentryConfig
    from .sentry_controller import SentryController, SentryState, FireCommand
    from .trackers.byte_tracker import ByteTracker
except ImportError:
    from sentry_config import SentryConfig
    from sentry_controller import SentryController, SentryState, FireCommand
    from trackers.byte_tracker import ByteTracker


class ClickableVideoLabel(QLabel):
    """
    QLabel that emits signals for mouse events on the video feed.
    Used for setting guard points, drawing tracks, adding ambush points.
    """
    clicked = pyqtSignal(float, float)  # Normalized x, y (0-1)
    dragged = pyqtSignal(float, float)  # For drawing tracks
    released = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self._drawing = False
    
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self._drawing = True
            norm_x = event.x() / max(1, self.width())
            norm_y = event.y() / max(1, self.height())
            self.clicked.emit(norm_x, norm_y)
    
    def mouseMoveEvent(self, event: QMouseEvent):
        if self._drawing:
            norm_x = event.x() / max(1, self.width())
            norm_y = event.y() / max(1, self.height())
            self.dragged.emit(norm_x, norm_y)
    
    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self._drawing = False
            self.released.emit()


class SentryTabWidget(QWidget):
    """
    Complete Sentry Mode tab widget with video display and controls.
    
    This widget:
    - Displays video feed with sentry overlay
    - Provides controls for sentry mode operation
    - Handles mouse input for setting points/drawing tracks
    - Emits signals for turret control (to be connected by main app)
    
    Signals:
        turret_move_requested: (pan, tilt) - Request to move turret
        fire_requested: (burst_count) - Request to fire
        sentry_enabled_changed: (enabled) - Sentry mode toggled
        manual_move_requested: (pan_delta, tilt_delta) - Manual turret control
    """
    
    # Signals for main app integration
    # AGENT-MANAGED: Signal definitions for main app communication (Dec 2024)
    # See CHANGE_IMPACT_REFERENCE.md Section 12 for signal flow documentation
    turret_move_requested = pyqtSignal(float, float)  # pan, tilt (absolute position)
    fire_requested = pyqtSignal(int)  # burst_count
    sentry_enabled_changed = pyqtSignal(bool)  # enabled state
    manual_move_requested = pyqtSignal(int, int)  # pan_delta, tilt_delta (relative movement)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Sentry components
        self.config = SentryConfig()
        self.controller = SentryController(self.config)
        self.tracker = ByteTracker(track_thresh=0.5, track_buffer=30)
        
        # State
        self.sentry_enabled = False
        self.click_mode = None  # 'guard', 'ambush', 'draw_track'
        self.drawing_track = False
        self.drawn_points = []
        
        # Frame tracking
        self.last_frame = None
        self.last_processed_frame = None
        
        # Register controller callbacks
        self.controller.on_fire(self._on_fire_command)
        self.controller.on_turret_move(self._on_turret_move)
        
        # Build UI
        self._setup_ui()
    
    def _setup_ui(self):
        """Build the user interface."""
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.setSpacing(10)
        
        # === LEFT SIDE: Video Display ===
        video_container = QWidget()
        video_layout = QVBoxLayout(video_container)
        video_layout.setContentsMargins(0, 0, 0, 0)
        
        # Video label with click handling
        self.video_label = ClickableVideoLabel()
        self.video_label.setMinimumSize(640, 480)
        self.video_label.setStyleSheet("background-color: #1a1a2e; border: 2px solid #4a4a6a;")
        self.video_label.setAlignment(Qt.AlignCenter)
        self.video_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Connect video click signals
        self.video_label.clicked.connect(self._on_video_click)
        self.video_label.dragged.connect(self._on_video_drag)
        self.video_label.released.connect(self._on_video_release)
        
        video_layout.addWidget(self.video_label)
        
        # Mode indicator below video
        self.mode_label = QLabel("Click video to interact when mode selected")
        self.mode_label.setStyleSheet("color: #888; font-style: italic;")
        self.mode_label.setAlignment(Qt.AlignCenter)
        video_layout.addWidget(self.mode_label)
        
        main_layout.addWidget(video_container, stretch=3)
        
        # === RIGHT SIDE: Controls ===
        control_scroll = QScrollArea()
        control_scroll.setWidgetResizable(True)
        control_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        control_scroll.setMaximumWidth(300)
        control_scroll.setMinimumWidth(250)
        
        control_widget = QWidget()
        control_layout = QVBoxLayout(control_widget)
        control_layout.setSpacing(10)
        
        # --- Enable/Disable Group ---
        enable_group = QGroupBox("🎯 Sentry Control")
        enable_layout = QVBoxLayout(enable_group)
        
        self.enable_checkbox = QCheckBox("Enable Sentry Mode")
        self.enable_checkbox.setStyleSheet("font-weight: bold; font-size: 14px;")
        self.enable_checkbox.stateChanged.connect(self._on_enable_changed)
        enable_layout.addWidget(self.enable_checkbox)
        
        self.fire_checkbox = QCheckBox("Auto-Fire Enabled")
        self.fire_checkbox.stateChanged.connect(self._on_fire_enable_changed)
        enable_layout.addWidget(self.fire_checkbox)
        
        control_layout.addWidget(enable_group)
        
        # --- Status Group ---
        status_group = QGroupBox("📊 Status")
        status_layout = QVBoxLayout(status_group)
        
        self.state_label = QLabel("State: IDLE")
        self.state_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #4fc3f7;")
        status_layout.addWidget(self.state_label)
        
        self.tracks_label = QLabel("Confirmed Tracks: 0")
        status_layout.addWidget(self.tracks_label)
        
        self.target_label = QLabel("Active Targets: 0")
        status_layout.addWidget(self.target_label)
        
        self.turret_label = QLabel("Turret: P90 T90")
        status_layout.addWidget(self.turret_label)
        
        control_layout.addWidget(status_group)
        
        # --- Point Setting Group ---
        points_group = QGroupBox("📍 Set Points")
        points_layout = QVBoxLayout(points_group)
        
        self.guard_btn = QPushButton("🎯 Set Guard Point")
        self.guard_btn.setToolTip("Click to set the center of the watch zone")
        self.guard_btn.clicked.connect(lambda: self._set_click_mode('guard'))
        points_layout.addWidget(self.guard_btn)
        
        self.ambush_btn = QPushButton("💀 Add Ambush Point")
        self.ambush_btn.setToolTip("Click to add a manual ambush/kill zone")
        self.ambush_btn.clicked.connect(lambda: self._set_click_mode('ambush'))
        points_layout.addWidget(self.ambush_btn)
        
        self.draw_btn = QPushButton("✏️ Draw Track Path")
        self.draw_btn.setToolTip("Click and drag to draw expected target path")
        self.draw_btn.clicked.connect(lambda: self._set_click_mode('draw_track'))
        points_layout.addWidget(self.draw_btn)
        
        self.cancel_btn = QPushButton("❌ Cancel Mode")
        self.cancel_btn.setEnabled(False)
        self.cancel_btn.clicked.connect(self._cancel_mode)
        points_layout.addWidget(self.cancel_btn)
        
        control_layout.addWidget(points_group)
        
        # --- Actions Group ---
        actions_group = QGroupBox("🔧 Actions")
        actions_layout = QVBoxLayout(actions_group)
        
        self.reset_btn = QPushButton("🔄 Reset All Tracks")
        self.reset_btn.setToolTip("Clear all learned tracks and start fresh")
        self.reset_btn.clicked.connect(self._reset_tracks)
        actions_layout.addWidget(self.reset_btn)
        
        self.force_learn_btn = QPushButton("📚 Force Learning Mode")
        self.force_learn_btn.clicked.connect(lambda: self.controller.force_learning_mode())
        actions_layout.addWidget(self.force_learn_btn)
        
        self.force_watch_btn = QPushButton("👁️ Force Watching Mode")
        self.force_watch_btn.clicked.connect(lambda: self.controller.force_watching_mode())
        actions_layout.addWidget(self.force_watch_btn)
        
        control_layout.addWidget(actions_group)
        
        # =========================================================================
        # AGENT-MANAGED BLOCK: Manual Turret Control (Dec 2024)
        # See CHANGE_IMPACT_REFERENCE.md Section 12 for manual control documentation
        # DO NOT MODIFY without checking cross-system impacts
        # =========================================================================
        manual_group = QGroupBox("🎮 Manual Control")
        manual_layout = QVBoxLayout(manual_group)
        
        # Direction buttons in a grid layout
        from PyQt5.QtWidgets import QGridLayout
        dir_grid = QGridLayout()
        dir_grid.setSpacing(2)
        
        # Up button
        self.btn_up = QPushButton("▲")
        self.btn_up.setFixedSize(50, 40)
        self.btn_up.setToolTip("Tilt up")
        self.btn_up.pressed.connect(lambda: self._manual_move(0, 5))
        self.btn_up.setAutoRepeat(True)
        self.btn_up.setAutoRepeatInterval(100)
        dir_grid.addWidget(self.btn_up, 0, 1)
        
        # Left button
        self.btn_left = QPushButton("◀")
        self.btn_left.setFixedSize(50, 40)
        self.btn_left.setToolTip("Pan left")
        self.btn_left.pressed.connect(lambda: self._manual_move(-5, 0))
        self.btn_left.setAutoRepeat(True)
        self.btn_left.setAutoRepeatInterval(100)
        dir_grid.addWidget(self.btn_left, 1, 0)
        
        # Center button
        self.btn_center = QPushButton("●")
        self.btn_center.setFixedSize(50, 40)
        self.btn_center.setToolTip("Center turret at home position")
        self.btn_center.clicked.connect(self._center_turret)
        dir_grid.addWidget(self.btn_center, 1, 1)
        
        # Right button
        self.btn_right = QPushButton("▶")
        self.btn_right.setFixedSize(50, 40)
        self.btn_right.setToolTip("Pan right")
        self.btn_right.pressed.connect(lambda: self._manual_move(5, 0))
        self.btn_right.setAutoRepeat(True)
        self.btn_right.setAutoRepeatInterval(100)
        dir_grid.addWidget(self.btn_right, 1, 2)
        
        # Down button
        self.btn_down = QPushButton("▼")
        self.btn_down.setFixedSize(50, 40)
        self.btn_down.setToolTip("Tilt down")
        self.btn_down.pressed.connect(lambda: self._manual_move(0, -5))
        self.btn_down.setAutoRepeat(True)
        self.btn_down.setAutoRepeatInterval(100)
        dir_grid.addWidget(self.btn_down, 2, 1)
        
        manual_layout.addLayout(dir_grid)
        
        # Set Ambush at Current Position button
        self.set_ambush_here_btn = QPushButton("💀 Set Ambush HERE")
        self.set_ambush_here_btn.setToolTip("Set current turret position as ambush point")
        self.set_ambush_here_btn.setStyleSheet("background-color: #8b0000; color: white; font-weight: bold;")
        self.set_ambush_here_btn.clicked.connect(self._set_ambush_at_current)
        manual_layout.addWidget(self.set_ambush_here_btn)
        
        # Aim at Ambush button
        self.aim_ambush_btn = QPushButton("🎯 Aim at Ambush Point")
        self.aim_ambush_btn.setToolTip("Move turret to best ambush point")
        self.aim_ambush_btn.clicked.connect(self._aim_at_ambush)
        manual_layout.addWidget(self.aim_ambush_btn)
        
        control_layout.addWidget(manual_group)
        # ========== END AGENT-MANAGED BLOCK: Manual Turret Control ==========
        
        # --- Settings Group ---
        settings_group = QGroupBox("⚙️ Settings")
        settings_layout = QVBoxLayout(settings_group)
        
        # Peripheral radius slider
        periph_label = QLabel("Peripheral Zone Size:")
        settings_layout.addWidget(periph_label)
        
        self.periph_slider = QSlider(Qt.Horizontal)
        self.periph_slider.setRange(10, 50)
        self.periph_slider.setValue(int(self.config.peripheral_outer_radius * 100))
        self.periph_slider.valueChanged.connect(self._on_periph_changed)
        settings_layout.addWidget(self.periph_slider)
        
        # Confidence threshold slider
        conf_label = QLabel("Fire Confidence Threshold:")
        settings_layout.addWidget(conf_label)
        
        self.conf_slider = QSlider(Qt.Horizontal)
        self.conf_slider.setRange(30, 90)
        self.conf_slider.setValue(int(self.config.fire_confidence_threshold * 100))
        self.conf_slider.valueChanged.connect(self._on_conf_changed)
        settings_layout.addWidget(self.conf_slider)
        
        # Debug overlay toggle
        self.debug_checkbox = QCheckBox("Show Debug Overlay")
        self.debug_checkbox.setChecked(self.config.show_debug_overlay)
        self.debug_checkbox.stateChanged.connect(
            lambda s: setattr(self.config, 'show_debug_overlay', s == Qt.Checked)
        )
        settings_layout.addWidget(self.debug_checkbox)
        
        control_layout.addWidget(settings_group)
        
        # Spacer
        control_layout.addSpacerItem(
            QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )
        
        control_scroll.setWidget(control_widget)
        main_layout.addWidget(control_scroll, stretch=1)
    
    # =========================================================================
    # PUBLIC METHODS - Called by main app
    # =========================================================================
    
    def process_frame(self, frame: np.ndarray, 
                      detections: List[Tuple[int, int, int, int, float]] = None) -> np.ndarray:
        """
        Process a video frame through sentry mode.
        
        Called by main app's video loop to update sentry and get overlay frame.
        
        Args:
            frame: BGR frame from camera
            detections: Optional list of (x, y, w, h, score) detections from main app's detector
                       If None, sentry will not track (camera-only preview)
        
        Returns:
            Frame with sentry overlay drawn
        
        AGENT-MANAGED: Sentry tab integration (Dec 2024)
        """
        if frame is None:
            return None
            
        self.last_frame = frame.copy()
        
        # Always update video display so user sees the camera feed
        if not self.sentry_enabled:
            # Show frame with basic info overlay when not enabled
            display_frame = frame.copy()
            h, w = display_frame.shape[:2]
            cv2.putText(display_frame, "Sentry: Disabled - Check 'Enable Sentry Mode' to start",
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 100, 255), 2)
            cv2.putText(display_frame, f"Frame: {w}x{h} | Detections: {len(detections) if detections else 0}",
                       (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
            self._update_video_display(display_frame)
            return frame
        
        # Run ByteTracker on detections
        if detections:
            tracks = self.tracker.update(detections)
            # Debug: log track count periodically
            if len(tracks) > 0 and int(time.time()) % 5 == 0:
                print(f"[SENTRY TAB] ByteTracker: {len(detections)} detections -> {len(tracks)} tracks")
        else:
            tracks = []
        
        # Update sentry controller
        processed = self.controller.update(tracks, frame.copy())
        if processed is None:
            processed = frame.copy()
        self.last_processed_frame = processed
        
        # Update status labels
        self._update_status()
        
        # Update video display with processed frame
        self._update_video_display(processed)
        
        # Draw currently drawing track
        if self.click_mode == 'draw_track' and len(self.drawn_points) > 1:
            self._draw_current_track(processed)
        
        return processed
    
    def set_enabled(self, enabled: bool):
        """Enable or disable sentry mode."""
        self.enable_checkbox.setChecked(enabled)
    
    def is_enabled(self) -> bool:
        """Check if sentry mode is enabled."""
        return self.sentry_enabled
    
    def reset(self):
        """Reset sentry mode state."""
        self._reset_tracks()
    
    # =========================================================================
    # INTERNAL METHODS
    # =========================================================================
    
    def _update_video_display(self, frame: np.ndarray):
        """Update the video label with a frame."""
        if frame is None:
            return
        
        # Convert BGR to RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Create QImage
        h, w, ch = rgb.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
        
        # Scale to label size while maintaining aspect ratio
        scaled = qt_image.scaled(
            self.video_label.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        
        self.video_label.setPixmap(QPixmap.fromImage(scaled))
    
    def _update_status(self):
        """Update status labels from controller state."""
        # State
        state_colors = {
            SentryState.IDLE: "#888888",
            SentryState.LEARNING: "#4fc3f7",
            SentryState.WATCHING: "#81c784",
            SentryState.AIMING: "#ffb74d",
            SentryState.FIRING: "#e57373",
            SentryState.COOLDOWN: "#9575cd"
        }
        state = self.controller.state
        color = state_colors.get(state, "#ffffff")
        self.state_label.setText(f"State: {state.name}")
        self.state_label.setStyleSheet(f"font-size: 16px; font-weight: bold; color: {color};")
        
        # Tracks
        confirmed = len(self.controller.path_analyzer.confirmed_paths)
        pending = len(self.controller.path_analyzer.pending_tracks)
        self.tracks_label.setText(f"Confirmed: {confirmed} | Pending: {pending}")
        
        # Targets
        active = len(self.controller.peripheral_sensor.targets)
        self.target_label.setText(f"Active Targets: {active}")
        
        # Turret position
        pan, tilt = self.controller.get_turret_position()
        self.turret_label.setText(f"Turret: P{pan:.0f} T{tilt:.0f}")
    
    def _draw_current_track(self, frame: np.ndarray):
        """Draw the currently being drawn track on frame."""
        if len(self.drawn_points) < 2:
            return
        
        h, w = frame.shape[:2]
        for i in range(1, len(self.drawn_points)):
            pt1 = (int(self.drawn_points[i-1][0] * w), int(self.drawn_points[i-1][1] * h))
            pt2 = (int(self.drawn_points[i][0] * w), int(self.drawn_points[i][1] * h))
            cv2.line(frame, pt1, pt2, (0, 255, 255), 3)
    
    def _set_click_mode(self, mode: str):
        """Set the current click mode."""
        self.click_mode = mode
        self.cancel_btn.setEnabled(True)
        
        # Update button states
        self.guard_btn.setEnabled(mode != 'guard')
        self.ambush_btn.setEnabled(mode != 'ambush')
        self.draw_btn.setEnabled(mode != 'draw_track')
        
        # Update mode label
        mode_text = {
            'guard': "🎯 Click on video to set GUARD POINT",
            'ambush': "💀 Click on video to add AMBUSH POINT",
            'draw_track': "✏️ Click and DRAG to draw track path"
        }
        self.mode_label.setText(mode_text.get(mode, ""))
        self.mode_label.setStyleSheet("color: #ffeb3b; font-weight: bold;")
    
    def _cancel_mode(self):
        """Cancel current click mode."""
        self.click_mode = None
        self.cancel_btn.setEnabled(False)
        self.drawn_points = []
        self.drawing_track = False
        
        # Reset button states
        self.guard_btn.setEnabled(True)
        self.ambush_btn.setEnabled(True)
        self.draw_btn.setEnabled(True)
        
        # Reset mode label
        self.mode_label.setText("Click video to interact when mode selected")
        self.mode_label.setStyleSheet("color: #888; font-style: italic;")
    
    def _reset_tracks(self):
        """Reset all tracks and restart learning."""
        self.tracker.reset()
        self.controller.stop()
        self.controller.start()
        self._update_status()
    
    # =========================================================================
    # SIGNAL HANDLERS
    # =========================================================================
    
    def _on_enable_changed(self, state: int):
        """Handle enable checkbox change."""
        self.sentry_enabled = (state == Qt.Checked)
        
        if self.sentry_enabled:
            self.controller.start()
        else:
            self.controller.stop()
        
        self.sentry_enabled_changed.emit(self.sentry_enabled)
        self._update_status()
    
    def _on_fire_enable_changed(self, state: int):
        """Handle fire enable checkbox change."""
        if state == Qt.Checked:
            self.controller.enable_fire()
        else:
            self.controller.disable_fire()
    
    def _on_periph_changed(self, value: int):
        """Handle peripheral size slider change."""
        self.config.peripheral_outer_radius = value / 100.0
        self.config.peripheral_inner_radius = self.config.peripheral_outer_radius * 0.3
    
    def _on_conf_changed(self, value: int):
        """Handle confidence threshold slider change."""
        self.config.fire_confidence_threshold = value / 100.0
    
    def _on_video_click(self, norm_x: float, norm_y: float):
        """Handle click on video."""
        if self.click_mode == 'guard':
            self.controller.set_guard_point(norm_x, norm_y)
            self._cancel_mode()
        
        elif self.click_mode == 'ambush':
            self.controller.add_manual_ambush_point(norm_x, norm_y)
            self._cancel_mode()
        
        elif self.click_mode == 'draw_track':
            self.drawing_track = True
            self.drawn_points = [(norm_x, norm_y)]
    
    def _on_video_drag(self, norm_x: float, norm_y: float):
        """Handle drag on video (for drawing tracks)."""
        if self.click_mode == 'draw_track' and self.drawing_track:
            if self.drawn_points:
                last_x, last_y = self.drawn_points[-1]
                dist = ((norm_x - last_x)**2 + (norm_y - last_y)**2)**0.5
                if dist > 0.01:  # Minimum distance threshold
                    self.drawn_points.append((norm_x, norm_y))
    
    def _on_video_release(self):
        """Handle mouse release on video."""
        if self.click_mode == 'draw_track' and self.drawing_track:
            self.drawing_track = False
            
            if len(self.drawn_points) >= 5:
                self._submit_drawn_track()
            else:
                print("[SENTRY] Track too short - draw a longer path")
            
            self.drawn_points = []
            self._cancel_mode()
    
    def _submit_drawn_track(self):
        """Submit a manually drawn track to the path analyzer."""
        if len(self.drawn_points) < 5:
            return
        
        # Import here to avoid circular imports
        try:
            from .track_recorder import TrackPoint, Track
        except ImportError:
            from track_recorder import TrackPoint, Track
        
        points = []
        current_time = time.time()
        
        for i, (x, y) in enumerate(self.drawn_points):
            # Estimate velocity from consecutive points
            if i > 0:
                prev_x, prev_y = self.drawn_points[i-1]
                vx = (x - prev_x) * 30  # Assume 30 fps
                vy = (y - prev_y) * 30
            else:
                vx, vy = 0.0, 0.0
            
            points.append(TrackPoint(
                x=x, y=y,
                timestamp=current_time + i * 0.033,
                velocity_x=vx,
                velocity_y=vy,
                speed=(vx**2 + vy**2)**0.5
            ))
        
        track = Track(
            track_id=-1,
            points=points,
            created_at=current_time,
            last_updated=current_time + len(points) * 0.033,
            is_active=False,
            is_complete=True
        )
        
        # Submit to path analyzer using analyze_track() which handles matching
        print(f"[SENTRY] Submitted manual track with {len(points)} points")
        confirmed = self.controller.path_analyzer.analyze_track(track)
        if confirmed:
            print(f"[SENTRY] Track confirmed as pattern! Ambush point: {confirmed.ambush_point}")
        else:
            print(f"[SENTRY] Track added to pending (need 2+ similar tracks for confirmation)")
    
    # =========================================================================
    # AGENT-MANAGED BLOCK: Manual Control Methods (Dec 2024)
    # See CHANGE_IMPACT_REFERENCE.md Section 12 for manual control documentation
    # =========================================================================
    
    def _manual_move(self, pan_delta: int, tilt_delta: int):
        """
        Request manual turret movement (relative).
        
        Emits manual_move_requested signal which main app handles
        by calling move_manual() with manual_override flag set.
        
        Args:
            pan_delta: Degrees to move pan (+right, -left)
            tilt_delta: Degrees to move tilt (+up, -down)
        """
        self.manual_move_requested.emit(pan_delta, tilt_delta)
    
    def _center_turret(self):
        """Center the turret at home position (90/90)."""
        self.turret_move_requested.emit(90.0, 90.0)
        print("[SENTRY] Centering turret to P90 T90")
    
    def _set_ambush_at_current(self):
        """
        Set the current turret position as a manual ambush point.
        
        Converts current pan/tilt angles to normalized frame coordinates
        and adds to the path analyzer's ambush points.
        """
        # Get current turret position from controller
        pan, tilt = self.controller.get_turret_position()
        
        # Convert pan/tilt to normalized frame coordinates
        # Pan 0-180 maps to X 0-1 (left to right)
        # Tilt: higher tilt = lower in frame (inverted)
        norm_x = pan / 180.0
        norm_y = 1.0 - (tilt / 180.0)
        
        # Clamp to valid range
        norm_x = max(0.0, min(1.0, norm_x))
        norm_y = max(0.0, min(1.0, norm_y))
        
        # Add as ambush point
        self.controller.add_manual_ambush_point(norm_x, norm_y)
        print(f"[SENTRY] Set ambush at turret position: P{pan:.0f} T{tilt:.0f} -> ({norm_x:.2f}, {norm_y:.2f})")
        
        # Update status display
        self._update_status()
    
    def _aim_at_ambush(self):
        """
        Move turret to aim at the primary (highest priority) ambush point.
        
        Gets the first ambush point from the path analyzer and converts
        its normalized coordinates back to pan/tilt angles.
        """
        # Get all ambush points sorted by priority
        ambush_points = self.controller.path_analyzer.get_all_ambush_points()
        if not ambush_points:
            print("[SENTRY] No ambush points set - draw tracks or click 'Set Ambush HERE'")
            return
        
        # Use the first (highest priority) ambush point
        norm_x, norm_y, confidence = ambush_points[0]
        
        # Convert normalized coords back to pan/tilt
        pan = norm_x * 180.0
        tilt = (1.0 - norm_y) * 180.0  # Invert Y
        
        # Clamp to safe servo range
        pan = max(5, min(175, pan))
        tilt = max(30, min(150, tilt))
        
        self.turret_move_requested.emit(pan, tilt)
        print(f"[SENTRY] Aiming at ambush: ({norm_x:.2f}, {norm_y:.2f}) conf={confidence:.2f} -> P{pan:.0f} T{tilt:.0f}")
    
    # ========== END AGENT-MANAGED BLOCK: Manual Control Methods ==========
    
    # =========================================================================
    # CONTROLLER CALLBACKS
    # =========================================================================
    
    def _on_turret_move(self, pan: float, tilt: float):
        """Handle turret move request from sentry controller."""
        self.turret_move_requested.emit(pan, tilt)
    
    def _on_fire_command(self, command: FireCommand):
        """Handle fire command from sentry controller."""
        self.fire_requested.emit(command.burst_count)

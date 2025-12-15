"""
Calibration Panel - Qt UI for Manual Turret Calibration
=========================================================
Provides an interactive grid-based interface for calibrating the turret's
pan/tilt angles relative to the fixed camera view.

Features:
- Visual grid overlay on camera frame
- Point-by-point calibration workflow
- Manual pan/tilt slider controls
- Progress tracking
- Data validation and persistence

Author: Auto-Turret Calibration System
Date: December 2025
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSlider,
                             QPushButton, QProgressBar, QGroupBox, QMessageBox,
                             QFileDialog, QComboBox, QSpinBox, QGridLayout)
from PyQt5.QtCore import Qt, pyqtSignal, QTimer, QSize
from PyQt5.QtGui import QPixmap, QImage, QFont, QColor, QPainter, QPen
import cv2
import numpy as np
import logging

from calibration_grid_mapper import CalibrationGridMapper

logger = logging.getLogger(__name__)


class CalibrationGridOverlay:
    """Renders a calibration grid overlay on video frames."""
    
    def __init__(self, mapper: CalibrationGridMapper):
        """
        Args:
            mapper: CalibrationGridMapper instance
        """
        self.mapper = mapper
        self.highlight_point = None  # (grid_x, grid_y) to highlight
        self.grid_color = (0, 255, 0)  # Green in BGR
        self.calibrated_color = (0, 255, 0)  # Green
        self.uncalibrated_color = (0, 0, 255)  # Red
        self.highlight_color = (255, 255, 0)  # Cyan
    
    def draw_grid(self, frame: np.ndarray, highlight_grid_point=None) -> np.ndarray:
        """
        Draw calibration grid overlay on frame.
        
        Args:
            frame: Input video frame (BGR format)
            highlight_grid_point: (grid_x, grid_y) to highlight, or None
            
        Returns:
            Frame with grid drawn
        """
        frame = frame.copy()
        height, width = frame.shape[:2]
        
        # Draw grid lines
        for grid_y in range(self.mapper.grid_height):
            for grid_x in range(self.mapper.grid_width):
                pos = self.mapper.get_grid_pixel_position(grid_x, grid_y)
                if pos:
                    pixel_x, pixel_y = pos
                    
                    # Determine point color based on calibration status
                    point = self.mapper.get_calibration_point(grid_x, grid_y)
                    
                    if highlight_grid_point == (grid_x, grid_y):
                        color = self.highlight_color
                        radius = 12
                    elif point:
                        color = self.calibrated_color
                        radius = 8
                    else:
                        color = self.uncalibrated_color
                        radius = 8
                    
                    # Draw circle at grid point
                    cv2.circle(frame, (pixel_x, pixel_y), radius, color, 2)
                    
                    # Draw text label
                    text = f"({grid_x},{grid_y})"
                    cv2.putText(frame, text, (pixel_x + 15, pixel_y - 10),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)
        
        # Draw grid lines between points
        for grid_y in range(self.mapper.grid_height):
            for grid_x in range(self.mapper.grid_width - 1):
                pos1 = self.mapper.get_grid_pixel_position(grid_x, grid_y)
                pos2 = self.mapper.get_grid_pixel_position(grid_x + 1, grid_y)
                if pos1 and pos2:
                    cv2.line(frame, pos1, pos2, self.grid_color, 1)
        
        for grid_x in range(self.mapper.grid_width):
            for grid_y in range(self.mapper.grid_height - 1):
                pos1 = self.mapper.get_grid_pixel_position(grid_x, grid_y)
                pos2 = self.mapper.get_grid_pixel_position(grid_x, grid_y + 1)
                if pos1 and pos2:
                    cv2.line(frame, pos1, pos2, self.grid_color, 1)
        
        return frame


class CalibrationPanel(QWidget):
    """Qt widget for manual turret calibration interface."""
    
    # Signals
    calibration_complete = pyqtSignal()
    calibration_point_added = pyqtSignal(int, int, float, float)  # grid_x, grid_y, pan, tilt
    pan_requested = pyqtSignal(float)  # pan angle
    tilt_requested = pyqtSignal(float)  # tilt angle
    
    def __init__(self, parent=None, frame_width=1280, frame_height=720):
        """
        Initialize calibration panel.
        
        Args:
            parent: Parent Qt widget
            frame_width: Camera frame width
            frame_height: Camera frame height
        """
        super().__init__(parent)
        
        self.frame_width = frame_width
        self.frame_height = frame_height
        
        # Create mapper
        self.mapper = CalibrationGridMapper(frame_width, frame_height, 
                                           grid_width=4, grid_height=4)
        
        # Create grid overlay renderer
        self.overlay = CalibrationGridOverlay(self.mapper)
        
        # Current calibration point being edited
        self.current_grid_x = 0
        self.current_grid_y = 0
        
        # Current servo angles
        self.current_pan_angle = 0.0
        self.current_tilt_angle = 0.0
        
        # Setup UI
        self._setup_ui()
    
    def _setup_ui(self):
        """Build the calibration panel UI."""
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Turret Calibration")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Calibration progress
        progress_layout = QHBoxLayout()
        progress_layout.addWidget(QLabel("Progress:"))
        
        self.progress_label = QLabel("0 / 16")
        progress_layout.addWidget(self.progress_label)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(16)
        self.progress_bar.setValue(0)
        progress_layout.addWidget(self.progress_bar)
        
        layout.addLayout(progress_layout)
        
        # Grid point selector
        grid_select_group = QGroupBox("Select Grid Point")
        grid_select_layout = QGridLayout()
        
        # Grid X selector (0-3)
        grid_select_layout.addWidget(QLabel("Grid X:"), 0, 0)
        self.grid_x_spin = QSpinBox()
        self.grid_x_spin.setMinimum(0)
        self.grid_x_spin.setMaximum(3)
        self.grid_x_spin.setValue(0)
        self.grid_x_spin.valueChanged.connect(self._on_grid_x_changed)
        grid_select_layout.addWidget(self.grid_x_spin, 0, 1)
        
        # Grid Y selector (0-3)
        grid_select_layout.addWidget(QLabel("Grid Y:"), 0, 2)
        self.grid_y_spin = QSpinBox()
        self.grid_y_spin.setMinimum(0)
        self.grid_y_spin.setMaximum(3)
        self.grid_y_spin.setValue(0)
        self.grid_y_spin.valueChanged.connect(self._on_grid_y_changed)
        grid_select_layout.addWidget(self.grid_y_spin, 0, 3)
        
        # Next button
        self.next_button = QPushButton("Next Point")
        self.next_button.clicked.connect(self._on_next_point)
        grid_select_layout.addWidget(self.next_button, 0, 4)
        
        grid_select_group.setLayout(grid_select_layout)
        layout.addWidget(grid_select_group)
        
        # Pan/Tilt controls
        servo_group = QGroupBox("Servo Controls")
        servo_layout = QVBoxLayout()
        
        # Pan control
        pan_layout = QHBoxLayout()
        pan_layout.addWidget(QLabel("Pan:"))
        
        self.pan_slider = QSlider(Qt.Horizontal)
        self.pan_slider.setMinimum(-90)
        self.pan_slider.setMaximum(90)
        self.pan_slider.setValue(0)
        self.pan_slider.setTickPosition(QSlider.TicksBelow)
        self.pan_slider.setTickInterval(10)
        self.pan_slider.sliderMoved.connect(self._on_pan_slider_changed)
        self.pan_slider.sliderReleased.connect(self._on_pan_slider_released)
        pan_layout.addWidget(self.pan_slider)
        
        self.pan_value_label = QLabel("0°")
        self.pan_value_label.setMinimumWidth(40)
        pan_layout.addWidget(self.pan_value_label)
        
        servo_layout.addLayout(pan_layout)
        
        # Tilt control
        tilt_layout = QHBoxLayout()
        tilt_layout.addWidget(QLabel("Tilt:"))
        
        self.tilt_slider = QSlider(Qt.Horizontal)
        self.tilt_slider.setMinimum(-45)
        self.tilt_slider.setMaximum(45)
        self.tilt_slider.setValue(0)
        self.tilt_slider.setTickPosition(QSlider.TicksBelow)
        self.tilt_slider.setTickInterval(5)
        self.tilt_slider.sliderMoved.connect(self._on_tilt_slider_changed)
        self.tilt_slider.sliderReleased.connect(self._on_tilt_slider_released)
        tilt_layout.addWidget(self.tilt_slider)
        
        self.tilt_value_label = QLabel("0°")
        self.tilt_value_label.setMinimumWidth(40)
        tilt_layout.addWidget(self.tilt_value_label)
        
        servo_layout.addLayout(tilt_layout)
        
        servo_group.setLayout(servo_layout)
        layout.addWidget(servo_group)
        
        # Calibration actions
        actions_group = QGroupBox("Calibration Actions")
        actions_layout = QVBoxLayout()
        
        # Save point button
        self.save_point_button = QPushButton("✓ Save Calibration Point")
        self.save_point_button.setStyleSheet(
            "QPushButton { background-color: #4CAF50; color: white; font-weight: bold; }"
        )
        self.save_point_button.clicked.connect(self._on_save_point)
        actions_layout.addWidget(self.save_point_button)
        
        # File operations
        file_layout = QHBoxLayout()
        
        self.save_calib_button = QPushButton("Save Calibration")
        self.save_calib_button.clicked.connect(self._on_save_calibration)
        file_layout.addWidget(self.save_calib_button)
        
        self.load_calib_button = QPushButton("Load Calibration")
        self.load_calib_button.clicked.connect(self._on_load_calibration)
        file_layout.addWidget(self.load_calib_button)
        
        self.clear_button = QPushButton("Clear All")
        self.clear_button.setStyleSheet(
            "QPushButton { background-color: #f44336; color: white; }"
        )
        self.clear_button.clicked.connect(self._on_clear_calibration)
        file_layout.addWidget(self.clear_button)
        
        actions_layout.addLayout(file_layout)
        
        actions_group.setLayout(actions_layout)
        layout.addWidget(actions_group)
        
        # Status display
        self.status_label = QLabel("Ready to calibrate. Select a grid point and adjust sliders.")
        self.status_label.setWordWrap(True)
        layout.addWidget(self.status_label)
        
        layout.addStretch()
        
        self.setLayout(layout)
    
    def _on_grid_x_changed(self, value):
        """Handle grid X selection change."""
        self.current_grid_x = value
        self._update_status()
    
    def _on_grid_y_changed(self, value):
        """Handle grid Y selection change."""
        self.current_grid_y = value
        self._update_status()
    
    def _on_next_point(self):
        """Move to next uncalibrated point."""
        uncalibrated = self.mapper.get_uncalibrated_points()
        if uncalibrated:
            next_x, next_y = uncalibrated[0]
            self.grid_x_spin.blockSignals(True)
            self.grid_y_spin.blockSignals(True)
            self.grid_x_spin.setValue(next_x)
            self.grid_y_spin.setValue(next_y)
            self.grid_x_spin.blockSignals(False)
            self.grid_y_spin.blockSignals(False)
            self.current_grid_x = next_x
            self.current_grid_y = next_y
            self._update_status()
        else:
            self.status_label.setText("✓ All points calibrated!")
    
    def _on_pan_slider_changed(self, value):
        """Handle pan slider movement."""
        self.current_pan_angle = float(value)
        self.pan_value_label.setText(f"{value}°")
    
    def _on_pan_slider_released(self):
        """Handle pan slider release - send to turret."""
        self.pan_requested.emit(self.current_pan_angle)
    
    def _on_tilt_slider_changed(self, value):
        """Handle tilt slider movement."""
        self.current_tilt_angle = float(value)
        self.tilt_value_label.setText(f"{value}°")
    
    def _on_tilt_slider_released(self):
        """Handle tilt slider release - send to turret."""
        self.tilt_requested.emit(self.current_tilt_angle)
    
    def _on_save_point(self):
        """Save current calibration point."""
        success = self.mapper.add_calibration_point(
            self.current_grid_x,
            self.current_grid_y,
            self.current_pan_angle,
            self.current_tilt_angle
        )
        
        if success:
            self.calibration_point_added.emit(
                self.current_grid_x, self.current_grid_y,
                self.current_pan_angle, self.current_tilt_angle
            )
            self._update_progress()
            self._update_status()
            
            # Auto-move to next point
            if not self.mapper.calibration_complete:
                self._on_next_point()
            else:
                self.calibration_complete.emit()
                QMessageBox.information(self, "Calibration Complete",
                                      "All calibration points have been saved!")
        else:
            QMessageBox.warning(self, "Error", 
                              f"Failed to save point: {self.mapper.last_error}")
    
    def _on_save_calibration(self):
        """Save calibration data to file."""
        filepath, _ = QFileDialog.getSaveFileName(
            self, "Save Calibration", "",
            "Calibration Files (*.calib.json);;All Files (*)"
        )
        if filepath:
            if self.mapper.save_calibration(filepath):
                QMessageBox.information(self, "Success",
                                      f"Calibration saved to {filepath}")
            else:
                QMessageBox.warning(self, "Error",
                                  f"Failed to save: {self.mapper.last_error}")
    
    def _on_load_calibration(self):
        """Load calibration data from file."""
        filepath, _ = QFileDialog.getOpenFileName(
            self, "Load Calibration", "",
            "Calibration Files (*.calib.json);;All Files (*)"
        )
        if filepath:
            if self.mapper.load_calibration(filepath):
                self._update_progress()
                self._update_status()
                QMessageBox.information(self, "Success",
                                      f"Calibration loaded from {filepath}")
            else:
                QMessageBox.warning(self, "Error",
                                  f"Failed to load: {self.mapper.last_error}")
    
    def _on_clear_calibration(self):
        """Clear all calibration data."""
        reply = QMessageBox.question(self, "Clear Calibration",
                                    "Clear all calibration data?",
                                    QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.mapper.clear_calibration()
            self._update_progress()
            self._update_status()
    
    def _update_progress(self):
        """Update progress display."""
        completed, total = self.mapper.get_progress()
        self.progress_label.setText(f"{completed} / {total}")
        self.progress_bar.setValue(completed)
    
    def _update_status(self):
        """Update status display."""
        point = self.mapper.get_calibration_point(self.current_grid_x, self.current_grid_y)
        if point:
            status = (f"Grid ({self.current_grid_x}, {self.current_grid_y}) - "
                     f"Already calibrated (pan={point.pan_angle}°, tilt={point.tilt_angle}°)")
        else:
            status = (f"Grid ({self.current_grid_x}, {self.current_grid_y}) - "
                     f"Current angles: pan={self.current_pan_angle}°, tilt={self.current_tilt_angle}°")
        self.status_label.setText(status)
    
    def draw_overlay_on_frame(self, frame: np.ndarray) -> np.ndarray:
        """Draw calibration overlay on frame."""
        return self.overlay.draw_grid(frame, 
                                     highlight_grid_point=(self.current_grid_x, 
                                                          self.current_grid_y))
    
    def get_mapper(self) -> CalibrationGridMapper:
        """Get the calibration mapper instance."""
        return self.mapper
    
    def is_calibration_complete(self) -> bool:
        """Check if calibration is complete."""
        return self.mapper.calibration_complete

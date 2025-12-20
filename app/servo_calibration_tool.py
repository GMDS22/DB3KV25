#!/usr/bin/env python3
"""
Servo Calibration Tool for Pan & Tilt Servos
=============================================

This tool allows you to:
1. Discover the full range of the PAN servo (expects >200°)
2. Verify/adjust TILT servo safe limits (currently 0-70°)
3. Save calibrated values to servo_calibration.json
4. Apply values to main app and Arduino sketch

Usage:
    python servo_calibration_tool.py

Controls:
    Pan Tab:
        - "Find Min" / "Find Max": Auto-sweep to find limits
        - Manual controls: ±1°, ±5°, ±10°
        - Speed slider: Adjust sweep speed (slow/medium/fast)
    
    Tilt Tab:
        - Test buttons verify current limits
        - Manual adjustment if needed
        - Confirm to save

Date: December 3, 2025
"""

import sys
import json
import time
import serial
import serial.tools.list_ports
from pathlib import Path
from typing import Optional, Tuple

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTabWidget, QGroupBox, QLabel, QPushButton, QSpinBox, QSlider,
    QComboBox, QTextEdit, QMessageBox, QFormLayout, QDoubleSpinBox,
    QProgressBar, QCheckBox
)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QObject
from PyQt5.QtGui import QFont, QColor


# Use a stable, script-relative calibration path so running the tool from
# different working directories does not create multiple calibration files.
BASE_DIR = Path(__file__).resolve().parent
CALIB_FILE = BASE_DIR / "servo_calibration.json"


class SerialCommands:
    """Commands sent to Arduino for servo control
    
    Command format matches main app protocol:
    P<pan>T<tilt>F<fire>L<led>R<laser>G<acc>S<safety>M<mode>\n
    
    Example: P90T54F0L0R0G0S1M0\n
    """
    
    @staticmethod
    def move_pan(angle: int) -> str:
        """Command to move pan servo to angle (0-255)
        
        Keep tilt at safe middle position (54°) during pan calibration
        """
        tilt = 54
        return f"P{angle}T{tilt}F0L0R0G0S1M0\n"
    
    @staticmethod
    def move_tilt(angle: int) -> str:
        """Command to move tilt servo to angle (0-255)
        
        Keep pan at center (90°) during tilt testing
        """
        pan = 90
        return f"P{pan}T{angle}F0L0R0G0S1M0\n"
    
    @staticmethod
    def move_both(pan: int, tilt: int) -> str:
        """Command to move both servos"""
        return f"P{pan}T{tilt}F0L0R0G0S1M0\n"
    
    @staticmethod
    def query_position() -> str:
        """Query current servo position - tracked locally in tool"""
        # Tool maintains position state internally
        return "POS?\n"


class SerialWorker(QObject):
    """Worker thread for serial communication"""
    
    position_updated = pyqtSignal(int, int)  # pan, tilt
    error_occurred = pyqtSignal(str)  # error message
    
    def __init__(self, port: str, baudrate: int = 115200):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.ser = None
        self.connected = False
        
    def connect(self) -> bool:
        """Connect to Arduino"""
        try:
            self.ser = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=1.0,
                write_timeout=1.0
            )
            time.sleep(2)  # Wait for Arduino reset
            self.connected = True
            return True
        except Exception as e:
            self.error_occurred.emit(f"Connection failed: {e}")
            return False
    
    def disconnect(self):
        """Disconnect from Arduino"""
        if self.ser and self.ser.is_open:
            self.ser.close()
        self.connected = False
    
    def send_command(self, command: str) -> bool:
        """Send command to Arduino"""
        if not self.connected or not self.ser:
            self.error_occurred.emit("Not connected to Arduino")
            return False
        
        try:
            self.ser.write(command.encode())
            self.ser.flush()
            return True
        except Exception as e:
            self.error_occurred.emit(f"Send failed: {e}")
            return False
    
    def read_response(self) -> Optional[str]:
        """Read response from Arduino"""
        if not self.connected or not self.ser:
            return None
        
        try:
            if self.ser.in_waiting:
                response = self.ser.readline().decode().strip()
                return response
        except Exception as e:
            self.error_occurred.emit(f"Read failed: {e}")
        
        return None


class ServoCalibrationTool(QMainWindow):
    """Main servo calibration GUI"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Servo Calibration Tool")
        self.setGeometry(100, 100, 900, 700)
        
        # Serial worker
        self.serial_worker = None
        self.connected = False
        
        # Calibration data
        self.pan_min = 5
        self.pan_max = 185
        self.tilt_min = 18
        self.tilt_max = 90
        self.current_pan = 90
        self.current_tilt = 40
        
        # Load existing calibration if available
        self.load_calibration()
        
        # Build UI
        self.init_ui()
        
    def init_ui(self):
        """Build user interface"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Connection section
        conn_group = QGroupBox("Serial Connection")
        conn_layout = QHBoxLayout()
        
        # COM port selector
        conn_layout.addWidget(QLabel("COM Port:"))
        self.com_combo = QComboBox()
        self.refresh_ports()
        conn_layout.addWidget(self.com_combo)
        
        # Refresh button
        refresh_btn = QPushButton("Refresh Ports")
        refresh_btn.clicked.connect(self.refresh_ports)
        conn_layout.addWidget(refresh_btn)
        
        # Connect button
        self.connect_btn = QPushButton("Connect")
        self.connect_btn.clicked.connect(self.toggle_connection)
        conn_layout.addWidget(self.connect_btn)
        
        # Status label
        self.status_label = QLabel("Disconnected")
        self.status_label.setStyleSheet("color: red; font-weight: bold;")
        conn_layout.addWidget(self.status_label)
        
        conn_layout.addStretch()
        conn_group.setLayout(conn_layout)
        main_layout.addWidget(conn_group)
        
        # Tab widget for Pan/Tilt
        tabs = QTabWidget()
        tabs.addTab(self.create_pan_tab(), "🔧 Pan Calibration (Full Range)")
        tabs.addTab(self.create_tilt_tab(), "🔧 Tilt Calibration (Safe Limits)")
        main_layout.addWidget(tabs)
        
        # Info/Log section
        log_group = QGroupBox("Status Log")
        log_layout = QVBoxLayout()
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setMaximumHeight(150)
        self.log_text.setStyleSheet("background-color: #1a1a1a; color: #00ff88; font-family: Consolas;")
        log_layout.addWidget(self.log_text)
        log_group.setLayout(log_layout)
        main_layout.addWidget(log_group)
        
        # Save/Cancel buttons
        button_layout = QHBoxLayout()
        save_btn = QPushButton("Save & Close")
        save_btn.setStyleSheet("background-color: #00aa00; font-weight: bold;")
        save_btn.clicked.connect(self.save_and_close)
        button_layout.addWidget(save_btn)
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.close)
        button_layout.addWidget(cancel_btn)
        
        button_layout.addStretch()
        main_layout.addLayout(button_layout)
    
    def create_pan_tab(self) -> QWidget:
        """Create PAN calibration tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Current values display
        info_group = QGroupBox("Current Pan Range")
        info_layout = QFormLayout()
        
        self.pan_min_display = QLabel(f"{self.pan_min}°")
        self.pan_max_display = QLabel(f"{self.pan_max}°")
        self.pan_current_display = QLabel(f"{self.current_pan}°")
        
        info_layout.addRow("Min Found:", self.pan_min_display)
        info_layout.addRow("Max Found:", self.pan_max_display)
        info_layout.addRow("Current Position:", self.pan_current_display)
        info_group.setLayout(info_layout)
        layout.addWidget(info_group)
        
        # Speed control
        speed_group = QGroupBox("Sweep Speed (Slower = More Careful)")
        speed_layout = QHBoxLayout()
        speed_layout.addWidget(QLabel("Slow"))
        self.pan_speed_slider = QSlider(Qt.Horizontal)
        self.pan_speed_slider.setMinimum(1)
        self.pan_speed_slider.setMaximum(3)
        self.pan_speed_slider.setValue(2)
        speed_layout.addWidget(self.pan_speed_slider)
        speed_layout.addWidget(QLabel("Fast"))
        speed_group.setLayout(speed_layout)
        layout.addWidget(speed_group)
        
        # Auto-find buttons
        find_group = QGroupBox("Auto-Find Limits (CAREFUL - Servo may stall)")
        find_layout = QHBoxLayout()
        
        find_min_btn = QPushButton("Find MIN")
        find_min_btn.setStyleSheet("background-color: #ff6600; font-weight: bold;")
        find_min_btn.clicked.connect(self.pan_find_min)
        find_layout.addWidget(find_min_btn)
        
        find_max_btn = QPushButton("Find MAX")
        find_max_btn.setStyleSheet("background-color: #ff6600; font-weight: bold;")
        find_max_btn.clicked.connect(self.pan_find_max)
        find_layout.addWidget(find_max_btn)
        
        find_layout.addStretch()
        find_group.setLayout(find_layout)
        layout.addWidget(find_group)
        
        # Manual controls
        manual_group = QGroupBox("Manual Controls")
        manual_layout = QVBoxLayout()
        
        # Spinner for direct angle entry
        spinner_layout = QHBoxLayout()
        spinner_layout.addWidget(QLabel("Move to angle:"))
        self.pan_angle_spin = QSpinBox()
        self.pan_angle_spin.setMinimum(0)
        self.pan_angle_spin.setMaximum(255)
        self.pan_angle_spin.setValue(self.current_pan)
        spinner_layout.addWidget(self.pan_angle_spin)
        
        pan_move_btn = QPushButton("Move")
        pan_move_btn.clicked.connect(lambda: self.pan_move_to(self.pan_angle_spin.value()))
        spinner_layout.addWidget(pan_move_btn)
        spinner_layout.addStretch()
        manual_layout.addLayout(spinner_layout)
        
        # Increment buttons
        inc_layout = QHBoxLayout()
        
        for inc in [-10, -5, -1, 1, 5, 10]:
            btn = QPushButton(f"{inc:+d}°")
            btn.clicked.connect(lambda checked, i=inc: self.pan_increment(i))
            inc_layout.addWidget(btn)
        
        inc_layout.addStretch()
        manual_layout.addLayout(inc_layout)
        manual_group.setLayout(manual_layout)
        layout.addWidget(manual_group)
        
        # Reset button
        reset_group = QGroupBox("Reset")
        reset_layout = QHBoxLayout()
        reset_btn = QPushButton("Reset to Factory Defaults (5-185°)")
        reset_btn.setStyleSheet("background-color: #cc0000; color: white;")
        reset_btn.clicked.connect(self.pan_reset)
        reset_layout.addWidget(reset_btn)
        reset_layout.addStretch()
        reset_group.setLayout(reset_layout)
        layout.addWidget(reset_group)
        
        layout.addStretch()
        widget.setLayout(layout)
        return widget
    
    def create_tilt_tab(self) -> QWidget:
        """Create TILT calibration tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Current values display
        info_group = QGroupBox("Current Tilt Range (Safe Limits)")
        info_layout = QFormLayout()
        
        info_layout.addRow(
            QLabel("Current Range:"),
            QLabel(f"{self.tilt_min}° to {self.tilt_max}°")
        )
        
        self.tilt_current_display = QLabel(f"{self.current_tilt}°")
        info_layout.addRow("Current Position:", self.tilt_current_display)
        
        info_group.setLayout(info_layout)
        layout.addWidget(info_group)
        
        # Safety note
        note_group = QGroupBox("⚠️ Safety Note")
        note_layout = QVBoxLayout()
        note_text = QLabel(
            "Tilt servo is limited to safe range (18-90°) to prevent damage.\n"
            "You can verify the limits work correctly or make small adjustments."
        )
        note_text.setWordWrap(True)
        note_layout.addWidget(note_text)
        note_group.setLayout(note_layout)
        layout.addWidget(note_group)
        
        # Test limits
        test_group = QGroupBox("Test Current Limits")
        test_layout = QHBoxLayout()
        
        test_min_btn = QPushButton("Move to MIN (18°)")
        test_min_btn.clicked.connect(lambda: self.tilt_move_to(self.tilt_min))
        test_layout.addWidget(test_min_btn)
        
        test_mid_btn = QPushButton("Move to MID (54°)")
        test_mid_btn.clicked.connect(lambda: self.tilt_move_to(54))
        test_layout.addWidget(test_mid_btn)
        
        test_max_btn = QPushButton("Move to MAX (90°)")
        test_max_btn.clicked.connect(lambda: self.tilt_move_to(self.tilt_max))
        test_layout.addWidget(test_max_btn)
        
        test_layout.addStretch()
        test_group.setLayout(test_layout)
        layout.addWidget(test_group)
        
        # Manual adjustment (optional)
        adjust_group = QGroupBox("Manual Adjustment (Optional)")
        adjust_layout = QVBoxLayout()
        
        adjust_note = QLabel(
            "Only adjust if you've verified the servo can safely move beyond current limits.\n"
            "Recommended: Leave at default 18-90° unless you have a specific reason to change."
        )
        adjust_note.setWordWrap(True)
        adjust_layout.addWidget(adjust_note)
        
        adjust_form = QFormLayout()
        self.tilt_min_spin = QSpinBox()
        self.tilt_min_spin.setMinimum(0)
        self.tilt_min_spin.setMaximum(90)
        self.tilt_min_spin.setValue(self.tilt_min)
        adjust_form.addRow("Min Angle:", self.tilt_min_spin)
        
        self.tilt_max_spin = QSpinBox()
        self.tilt_max_spin.setMinimum(18)
        self.tilt_max_spin.setMaximum(180)
        self.tilt_max_spin.setValue(self.tilt_max)
        adjust_form.addRow("Max Angle:", self.tilt_max_spin)
        
        adjust_layout.addLayout(adjust_form)
        adjust_group.setLayout(adjust_layout)
        layout.addWidget(adjust_group)
        
        # Confirm/Reset buttons
        button_group = QGroupBox("Save/Reset")
        button_layout = QHBoxLayout()
        
        confirm_btn = QPushButton("✓ Confirm Tilt Settings")
        confirm_btn.setStyleSheet("background-color: #00aa00;")
        confirm_btn.clicked.connect(self.tilt_confirm)
        button_layout.addWidget(confirm_btn)
        
        reset_btn = QPushButton("↻ Reset to Safe Defaults (18-90°)")
        reset_btn.setStyleSheet("background-color: #cc0000; color: white;")
        reset_btn.clicked.connect(self.tilt_reset)
        button_layout.addWidget(reset_btn)
        
        button_layout.addStretch()
        button_group.setLayout(button_layout)
        layout.addWidget(button_group)
        
        layout.addStretch()
        widget.setLayout(layout)
        return widget
    
    def refresh_ports(self):
        """Refresh available COM ports"""
        self.com_combo.clear()
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.com_combo.addItem(port.device)
        
        if len(ports) == 0:
            self.com_combo.addItem("No ports found")
    
    def toggle_connection(self):
        """Connect/disconnect from Arduino"""
        if self.connected:
            self.disconnect_arduino()
        else:
            self.connect_arduino()
    
    def connect_arduino(self):
        """Connect to Arduino"""
        port = self.com_combo.currentText()
        if port == "No ports found" or not port:
            QMessageBox.warning(self, "Error", "No COM port selected")
            return
        
        self.serial_worker = SerialWorker(port)
        self.serial_worker.error_occurred.connect(lambda msg: self.log(f"❌ {msg}"))
        
        if self.serial_worker.connect():
            self.connected = True
            self.connect_btn.setText("Disconnect")
            self.status_label.setText("Connected ✓")
            self.status_label.setStyleSheet("color: green; font-weight: bold;")
            self.log(f"✓ Connected to {port}")
            self.log("✓ Ready to calibrate - Click 'Find MIN' or 'Find MAX' to start")
        else:
            self.log(f"❌ Failed to connect to {port}")
    
    def disconnect_arduino(self):
        """Disconnect from Arduino"""
        if self.serial_worker:
            self.serial_worker.disconnect()
        self.connected = False
        self.connect_btn.setText("Connect")
        self.status_label.setText("Disconnected")
        self.status_label.setStyleSheet("color: red; font-weight: bold;")
        self.log("Disconnected from Arduino")
    
    def log(self, message: str):
        """Log message to status text"""
        timestamp = time.strftime("%H:%M:%S")
        self.log_text.append(f"[{timestamp}] {message}")
    
    def pan_move_to(self, angle: int):
        """Move pan to specific angle"""
        if not self.connected:
            self.log("❌ Not connected to Arduino")
            return
        
        self.current_pan = angle
        cmd = SerialCommands.move_pan(angle)
        self.serial_worker.send_command(cmd)
        self.pan_current_display.setText(f"{angle}°")
        self.pan_angle_spin.setValue(angle)
        self.log(f"🔄 Pan → {angle}° (cmd: {cmd.strip()})")
    
    def pan_increment(self, delta: int):
        """Increment pan position"""
        new_angle = max(0, min(255, self.current_pan + delta))
        self.pan_move_to(new_angle)
    
    def pan_find_min(self):
        """Auto-sweep to find minimum pan angle"""
        if not self.connected:
            self.log("❌ Not connected to Arduino")
            return
        
        self.log("🔍 Finding PAN minimum... Move slowly toward limit...")
        self.log("⚠️  Servo will stall when hitting physical limit")
        
        # Get speed setting
        speed_val = self.pan_speed_slider.value()
        step = 1 if speed_val == 1 else (2 if speed_val == 2 else 5)
        
        # Sweep downward from current position
        for angle in range(self.current_pan, -1, -step):
            self.pan_move_to(angle)
            time.sleep(0.1 * (4 - speed_val))  # Slower = longer delays
        
        self.pan_min = 0
        self.pan_min_display.setText(f"{self.pan_min}°")
        self.log(f"✓ Pan minimum found at {self.pan_min}°")
    
    def pan_find_max(self):
        """Auto-sweep to find maximum pan angle"""
        if not self.connected:
            self.log("❌ Not connected to Arduino")
            return
        
        self.log("🔍 Finding PAN maximum... Move slowly toward limit...")
        self.log("⚠️  Servo will stall when hitting physical limit")
        
        # Get speed setting
        speed_val = self.pan_speed_slider.value()
        step = 1 if speed_val == 1 else (2 if speed_val == 2 else 5)
        
        # Sweep upward from current position
        for angle in range(self.current_pan, 256, step):
            if angle > 255:
                break
            self.pan_move_to(angle)
            time.sleep(0.1 * (4 - speed_val))  # Slower = longer delays
        
        self.pan_max = 255
        self.pan_max_display.setText(f"{self.pan_max}°")
        self.log(f"✓ Pan maximum found at {self.pan_max}°")
    
    def pan_reset(self):
        """Reset pan to factory defaults"""
        reply = QMessageBox.question(
            self, "Reset Pan",
            "Reset PAN to factory defaults (5-185°)?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.pan_min = 5
            self.pan_max = 185
            self.pan_min_display.setText(f"{self.pan_min}°")
            self.pan_max_display.setText(f"{self.pan_max}°")
            self.log("Pan reset to factory defaults (5-185°)")
    
    def tilt_move_to(self, angle: int):
        """Move tilt to specific angle"""
        if not self.connected:
            self.log("❌ Not connected to Arduino")
            return
        
        self.current_tilt = angle
        cmd = SerialCommands.move_tilt(angle)
        self.serial_worker.send_command(cmd)
        self.tilt_current_display.setText(f"{angle}°")
        self.log(f"🔄 Tilt → {angle}° (cmd: {cmd.strip()})")
    
    def tilt_confirm(self):
        """Confirm tilt adjustments"""
        self.tilt_min = self.tilt_min_spin.value()
        self.tilt_max = self.tilt_max_spin.value()
        
        if self.tilt_min >= self.tilt_max:
            QMessageBox.warning(self, "Error", "Min must be less than Max")
            return
        
        self.log(f"✓ Tilt range confirmed: {self.tilt_min}° - {self.tilt_max}°")
    
    def tilt_reset(self):
        """Reset tilt to safe defaults"""
        reply = QMessageBox.question(
            self, "Reset Tilt",
            "Reset TILT to safe defaults (0-70°)?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.tilt_min = 0
            self.tilt_max = 70
            self.tilt_min_spin.setValue(0)
            self.tilt_max_spin.setValue(70)
            self.log("Tilt reset to safe defaults (0-70°)")
    
    def load_calibration(self):
        """Load existing calibration from file"""
        calib_file = CALIB_FILE
        if calib_file.exists():
            try:
                with open(calib_file) as f:
                    data = json.load(f)
                    self.pan_min = data.get("pan_min", 0)
                    self.pan_max = data.get("pan_max", 220)
                    self.tilt_min = data.get("tilt_min", 0)
                    self.tilt_max = data.get("tilt_max", 70)
            except Exception as e:
                print(f"Failed to load calibration: {e}")
    
    def save_calibration(self):
        """Save calibration to file"""
        data = {
            "pan_min": self.pan_min,
            "pan_max": self.pan_max,
            "tilt_min": self.tilt_min,
            "tilt_max": self.tilt_max,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        try:
            with open(CALIB_FILE, "w") as f:
                json.dump(data, f, indent=2)
            self.log(f"✓ Calibration saved to {CALIB_FILE}")
            return True
        except Exception as e:
            self.log(f"Failed to save calibration: {e}")
            return False
    
    def save_and_close(self):
        """Save calibration and close"""
        if self.save_calibration():
            QMessageBox.information(
                self, "Success",
                "Calibration saved!\n\n"
                "Next steps:\n"
                "1. Close this tool\n"
                "2. Restart the main tracking app\n"
                "3. Limits will be automatically applied"
            )
            self.close()
    
    def closeEvent(self, event):
        """Handle window close"""
        if self.connected:
            self.disconnect_arduino()
        event.accept()


def main():
    app = QApplication(sys.argv)
    window = ServoCalibrationTool()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

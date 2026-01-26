from __future__ import annotations

import json
import os
import threading

import cv2
import numpy as np
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
    QMainWindow,
)

from .presets import PRESETS, SERIAL_DEFAULTS, BUS_SERVO_CONFIG, AIM_DEFAULTS, TRACKING_DEFAULTS
from .serial_devices import SerialController
from .worker import VisionWorker


SETTINGS_FILE = os.path.join(os.path.dirname(__file__), "settings.json")


def load_settings() -> dict:
    if not os.path.exists(SETTINGS_FILE):
        return {}
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_settings(data: dict) -> None:
    try:
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception:
        pass


class AutoTrackLabWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("AutoTrack Lab (First-Lock / Quick Strike)")
        self._settings = load_settings()
        self._serial_connected = False

        preset_name = self._settings.get("preset", "Balanced")
        self.current_preset = PRESETS.get(preset_name, PRESETS["Balanced"])

        self.controller = SerialController(BUS_SERVO_CONFIG, AIM_DEFAULTS)

        self.worker = VisionWorker(self.controller, self.current_preset, TRACKING_DEFAULTS)
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.started.connect(self.worker.run)
        self.worker.frame_ready.connect(self._on_frame)
        self.worker.status.connect(self._on_status)
        self.worker.fps.connect(self._on_fps)

        self._build_ui()
        self._apply_settings()
        self._apply_dark_theme()
        self._start_tracking()

    def closeEvent(self, event) -> None:  # noqa: N802
        try:
            self.worker.stop()
            self.worker_thread.quit()
            self.worker_thread.wait(1000)
        except Exception:
            pass
        try:
            self.controller.close()
        except Exception:
            pass
        self._save_settings()
        event.accept()

    def _build_ui(self) -> None:
        root = QWidget()
        layout = QGridLayout()
        root.setLayout(layout)
        self.setCentralWidget(root)

        self.video_label = QLabel("Camera")
        self.video_label.setAlignment(Qt.AlignCenter)
        self.video_label.setMinimumSize(640, 480)
        layout.addWidget(self.video_label, 0, 0, 2, 1)

        side = QVBoxLayout()
        layout.addLayout(side, 0, 1, 2, 1)

        side.addWidget(self._build_connection_group())
        side.addWidget(self._build_tracking_group())
        side.addWidget(self._build_manual_group())
        side.addWidget(self._build_trigger_group())
        side.addStretch(1)

        self.status_label = QLabel("Idle")
        side.addWidget(self.status_label)

        self.debug_label = QLabel("")
        self.debug_label.setWordWrap(True)
        side.addWidget(self.debug_label)

    def _build_connection_group(self) -> QGroupBox:
        box = QGroupBox("Connections")
        grid = QGridLayout()
        box.setLayout(grid)

        self.nano_port = QLineEdit(SERIAL_DEFAULTS["nano_port"])
        self.bus_port = QLineEdit(SERIAL_DEFAULTS["bus_port"])
        self.nano_baud = QSpinBox()
        self.nano_baud.setMaximum(921600)
        self.nano_baud.setValue(SERIAL_DEFAULTS["nano_baud"])
        self.bus_baud = QSpinBox()
        self.bus_baud.setMaximum(921600)
        self.bus_baud.setValue(SERIAL_DEFAULTS["bus_baud"])

        self.camera_combo = QComboBox()
        self.camera_combo.addItems(["0", "1", "2", "3", "4"])
        self.camera_combo.currentTextChanged.connect(self._on_camera_changed)

        grid.addWidget(QLabel("Nano COM"), 0, 0)
        grid.addWidget(self.nano_port, 0, 1)
        grid.addWidget(QLabel("Bus COM"), 1, 0)
        grid.addWidget(self.bus_port, 1, 1)
        grid.addWidget(QLabel("Nano Baud"), 2, 0)
        grid.addWidget(self.nano_baud, 2, 1)
        grid.addWidget(QLabel("Bus Baud"), 3, 0)
        grid.addWidget(self.bus_baud, 3, 1)
        grid.addWidget(QLabel("Camera"), 4, 0)
        grid.addWidget(self.camera_combo, 4, 1)

        self.connect_btn = QPushButton("Connect")
        self.connect_btn.clicked.connect(self._toggle_serial)
        grid.addWidget(self.connect_btn, 5, 0, 1, 2)
        return box

    def _build_tracking_group(self) -> QGroupBox:
        box = QGroupBox("Tracking")
        layout = QVBoxLayout()
        box.setLayout(layout)

        row = QHBoxLayout()
        self.preset_combo = QComboBox()
        self.preset_combo.addItems(list(PRESETS.keys()))
        self.preset_combo.currentTextChanged.connect(self._on_preset_changed)
        row.addWidget(QLabel("Preset"))
        row.addWidget(self.preset_combo)
        layout.addLayout(row)

        mode_row = QHBoxLayout()
        self.mode_combo = QComboBox()
        self.mode_combo.addItems(["follow", "quick"])
        self.mode_combo.currentTextChanged.connect(self._on_mode_changed)
        mode_row.addWidget(QLabel("Mode"))
        mode_row.addWidget(self.mode_combo)
        layout.addLayout(mode_row)

        self.start_btn = QPushButton("Start Tracking")
        self.stop_btn = QPushButton("Stop Tracking")
        self.start_btn.clicked.connect(self._start_tracking)
        self.stop_btn.clicked.connect(self._stop_tracking)
        layout.addWidget(self.start_btn)
        layout.addWidget(self.stop_btn)
        return box

    def _build_manual_group(self) -> QGroupBox:
        box = QGroupBox("Manual Aim")
        grid = QGridLayout()
        box.setLayout(grid)

        self.step_spin = QDoubleSpinBox()
        self.step_spin.setRange(0.5, 15.0)
        self.step_spin.setSingleStep(0.5)
        self.step_spin.setValue(AIM_DEFAULTS["manual_step_deg"])

        btn_up = QPushButton("Up")
        btn_down = QPushButton("Down")
        btn_left = QPushButton("Left")
        btn_right = QPushButton("Right")
        btn_center = QPushButton("Center")

        btn_up.clicked.connect(lambda: self._nudge(0, -self.step_spin.value()))
        btn_down.clicked.connect(lambda: self._nudge(0, self.step_spin.value()))
        btn_left.clicked.connect(lambda: self._nudge(-self.step_spin.value(), 0))
        btn_right.clicked.connect(lambda: self._nudge(self.step_spin.value(), 0))
        btn_center.clicked.connect(self._center)

        grid.addWidget(QLabel("Step (deg)"), 0, 0)
        grid.addWidget(self.step_spin, 0, 1)
        grid.addWidget(btn_up, 1, 1)
        grid.addWidget(btn_left, 2, 0)
        grid.addWidget(btn_center, 2, 1)
        grid.addWidget(btn_right, 2, 2)
        grid.addWidget(btn_down, 3, 1)
        return box

    def _build_trigger_group(self) -> QGroupBox:
        box = QGroupBox("Trigger / IO")
        layout = QVBoxLayout()
        box.setLayout(layout)

        self.armed_check = QCheckBox("ARMED")
        self.armed_check.toggled.connect(self._on_armed)
        layout.addWidget(self.armed_check)

        mode_row = QHBoxLayout()
        self.trigger_mode_combo = QComboBox()
        self.trigger_mode_combo.addItems(["Water (M0)", "Projectile (M1)"])
        self.trigger_mode_combo.currentIndexChanged.connect(self._on_trigger_mode)
        mode_row.addWidget(QLabel("Trigger Mode"))
        mode_row.addWidget(self.trigger_mode_combo)
        layout.addLayout(mode_row)

        io_row = QHBoxLayout()
        self.led_check = QCheckBox("LED")
        self.laser_check = QCheckBox("Laser")
        self.led_check.toggled.connect(lambda v: self.controller.set_led(v))
        self.laser_check.toggled.connect(lambda v: self.controller.set_laser(v))
        io_row.addWidget(self.led_check)
        io_row.addWidget(self.laser_check)
        layout.addLayout(io_row)

        self.fire_btn = QPushButton("Fire")
        self.fire_btn.clicked.connect(self._fire)
        layout.addWidget(self.fire_btn)
        return box

    def _apply_settings(self) -> None:
        self.nano_port.setText(self._settings.get("nano_port", SERIAL_DEFAULTS["nano_port"]))
        self.bus_port.setText(self._settings.get("bus_port", SERIAL_DEFAULTS["bus_port"]))
        self.nano_baud.setValue(int(self._settings.get("nano_baud", SERIAL_DEFAULTS["nano_baud"])))
        self.bus_baud.setValue(int(self._settings.get("bus_baud", SERIAL_DEFAULTS["bus_baud"])))
        self.preset_combo.setCurrentText(self._settings.get("preset", "Balanced"))
        self.mode_combo.setCurrentText(self._settings.get("mode", "follow"))
        self.camera_combo.setCurrentText(str(self._settings.get("camera_index", 0)))

    def _save_settings(self) -> None:
        data = {
            "nano_port": self.nano_port.text().strip(),
            "bus_port": self.bus_port.text().strip(),
            "nano_baud": self.nano_baud.value(),
            "bus_baud": self.bus_baud.value(),
            "preset": self.preset_combo.currentText(),
            "mode": self.mode_combo.currentText(),
            "camera_index": int(self.camera_combo.currentText()),
        }
        save_settings(data)

    def _toggle_serial(self) -> None:
        if self._serial_connected:
            self.controller.close()
            self._serial_connected = False
            self.connect_btn.setText("Connect")
            self.status_label.setText("Serial disconnected")
            return

        def _connect() -> None:
            try:
                self.controller.connect(
                    SERIAL_DEFAULTS["mode"],
                    self.nano_port.text().strip(),
                    int(self.nano_baud.value()),
                    self.bus_port.text().strip(),
                    int(self.bus_baud.value()),
                )
                self._serial_connected = True
                self.connect_btn.setText("Disconnect")
                self.status_label.setText("Serial connected")
            except Exception as exc:
                self._serial_connected = False
                self.connect_btn.setText("Connect")
                self.status_label.setText(f"Serial error: {exc}")

        threading.Thread(target=_connect, daemon=True).start()

    def _start_tracking(self) -> None:
        if not self.worker_thread.isRunning():
            self.worker_thread.start()
        self.worker.set_tracking_enabled(True)
        self.status_label.setText("Tracking started")

    def _stop_tracking(self) -> None:
        self.worker.set_tracking_enabled(False)
        self.status_label.setText("Tracking stopped")

    def _on_preset_changed(self, name: str) -> None:
        self.current_preset = PRESETS.get(name, PRESETS["Balanced"])
        self.worker.set_preset(self.current_preset)
        self.status_label.setText(f"Preset: {name}")

    def _on_mode_changed(self, mode: str) -> None:
        self.worker.set_mode(mode)
        self.status_label.setText(f"Mode: {mode}")

    def _on_camera_changed(self, value: str) -> None:
        try:
            index = int(value)
        except Exception:
            index = 0
        self.worker.set_camera_index(index)
        self.status_label.setText(f"Camera: {index}")

    def _on_trigger_mode(self, idx: int) -> None:
        self.controller.set_trigger_mode(projectile=idx == 1)

    def _on_armed(self, armed: bool) -> None:
        self.controller.set_safety(armed)

    def _fire(self) -> None:
        self.controller.fire_pulse(duration_ms=120)

    def _nudge(self, dpan: float, dtilt: float) -> None:
        self.controller.nudge(dpan, dtilt, time_ms=120)

    def _center(self) -> None:
        pan = AIM_DEFAULTS["pan_center"]
        tilt = AIM_DEFAULTS["tilt_center"]
        self.controller.set_pose(pan, tilt, time_ms=180)

    def _on_frame(self, frame: np.ndarray, info: dict) -> None:
        overlay = frame.copy()
        bbox = info.get("bbox")
        candidate = info.get("candidate")
        if candidate:
            x1, y1, x2, y2 = candidate
            cv2.rectangle(overlay, (x1, y1), (x2, y2), (80, 80, 255), 1)
        if bbox:
            x1, y1, x2, y2 = bbox
            cv2.rectangle(overlay, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)
            cv2.drawMarker(overlay, (cx, cy), (0, 255, 0), cv2.MARKER_CROSS, 12, 2)
        if info.get("locked"):
            cv2.putText(overlay, "LOCK", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(
            overlay,
            f"{info.get('mode', '')} | {info.get('detector', '')} | {info.get('message', '')}",
            (10, overlay.shape[0] - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 0),
            2,
        )
        rgb = cv2.cvtColor(overlay, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape
        bytes_per_line = ch * w
        qimg = QImage(rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.video_label.setPixmap(QPixmap.fromImage(qimg))

    def _on_status(self, text: str) -> None:
        self.debug_label.setText(text)

    def _on_fps(self, value: float) -> None:
        self.status_label.setText(f"FPS: {value:.1f}")

    def _apply_dark_theme(self) -> None:
        self.setStyleSheet(
            """
            QMainWindow { background-color: #1e1e1e; color: #e0e0e0; }
            QLabel { color: #e0e0e0; }
            QGroupBox {
                border: 1px solid #3a3a3a;
                margin-top: 6px;
                color: #e0e0e0;
            }
            QGroupBox::title { subcontrol-origin: margin; left: 8px; padding: 0 4px; }
            QPushButton {
                background-color: #2d2d2d;
                color: #e0e0e0;
                border: 1px solid #444;
                padding: 6px;
            }
            QPushButton:hover { background-color: #3a3a3a; }
            QLineEdit, QSpinBox, QDoubleSpinBox, QComboBox {
                background-color: #2a2a2a;
                color: #e0e0e0;
                border: 1px solid #444;
                padding: 3px;
            }
            QCheckBox { color: #e0e0e0; }
            """
        )

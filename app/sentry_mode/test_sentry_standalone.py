"""
Standalone Test Harness for Sentry Ambush Mode.

This script runs the Sentry Mode independently of the main turret app.
It provides a minimal PyQt5 + OpenCV interface for testing and development.

Usage:
    python test_sentry_standalone.py
    
    Or with options:
    python test_sentry_standalone.py --camera 0 --yolo yolov8n.pt
    
    With Arduino connection:
    python test_sentry_standalone.py --port COM3 --baud 115200

Controls:
    Q / ESC     - Quit
    SPACE       - Toggle fire enable
    L           - Force learning mode
    W           - Force watching mode
    R           - Reset all tracks
    G           - Set guard point (click after pressing)
    A           - Add manual ambush point (click after pressing)
    C           - Clear manual ambush points
    S           - Save configuration
    D           - Toggle debug overlay
    T           - Toggle Arduino connection
"""

import sys
import os
import time
import argparse
import cv2
import numpy as np

# === Fix imports for standalone execution ===
# Add the sentry_mode directory itself to path so modules can find each other
_sentry_dir = os.path.dirname(os.path.abspath(__file__))
if _sentry_dir not in sys.path:
    sys.path.insert(0, _sentry_dir)

# Also add parent directory for potential app-level imports
_app_dir = os.path.dirname(_sentry_dir)
if _app_dir not in sys.path:
    sys.path.insert(0, _app_dir)

from typing import List, Tuple, Optional

# Try to import PyQt5 for GUI, fallback to OpenCV-only mode
try:
    from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                                 QHBoxLayout, QLabel, QPushButton, QSlider, 
                                 QGroupBox, QCheckBox, QComboBox, QStatusBar)
    from PyQt5.QtCore import Qt, QTimer, pyqtSignal
    from PyQt5.QtGui import QImage, QPixmap
    HAS_PYQT = True
except ImportError:
    HAS_PYQT = False
    print("[WARNING] PyQt5 not available, running in OpenCV-only mode")

# Import sentry components - use direct imports since we added sentry_mode to path
from sentry_config import SentryConfig
from track_recorder import TrackRecorder, Track
from path_analyzer import PathAnalyzer, ConfirmedPath
from trajectory_predictor import TrajectoryPredictor, PredictionResult
from peripheral_sensor import PeripheralSensor, ZoneEvent, ZoneType
from sentry_overlay import SentryOverlay
from trackers.byte_tracker import ByteTracker

# Import controller after other modules are available
from sentry_controller import SentryController, SentryState, FireCommand

# Try to import YOLO
try:
    from ultralytics import YOLO
    HAS_YOLO = True
except ImportError:
    HAS_YOLO = False
    print("[WARNING] Ultralytics YOLO not available, using motion detection fallback")

# Try to import serial for Arduino connection
try:
    import serial
    import serial.tools.list_ports
    HAS_SERIAL = True
except ImportError:
    HAS_SERIAL = False
    print("[WARNING] PySerial not available, Arduino connection disabled")


class TurretSerial:
    """
    Serial communication with Arduino turret.
    
    Sends commands in format: P{pan}T{tilt}F{fire}L{led}R{laser}G{acc}S{safety}M{mode}
    """
    
    def __init__(self, port: str = None, baud: int = 115200):
        self.port = port
        self.baud = baud
        self.serial: Optional[serial.Serial] = None
        self.connected = False
        
        # Current state
        self.pan = 90
        self.tilt = 45
        self.fire = 0
        self.led = 0
        self.laser = 0
        self.safety = 1  # Start in safe mode
        
        # Last command sent (to avoid duplicates)
        self.last_command = ""
    
    @staticmethod
    def list_ports() -> List[str]:
        """List available serial ports."""
        if not HAS_SERIAL:
            return []
        ports = serial.tools.list_ports.comports()
        return [p.device for p in ports]
    
    def connect(self, port: str = None) -> bool:
        """Connect to Arduino."""
        if not HAS_SERIAL:
            print("[SERIAL] PySerial not available")
            return False
        
        port = port or self.port
        if not port:
            # Try to auto-detect
            ports = self.list_ports()
            if ports:
                port = ports[0]
                print(f"[SERIAL] Auto-detected port: {port}")
            else:
                print("[SERIAL] No serial ports found")
                return False
        
        try:
            self.serial = serial.Serial(port, self.baud, timeout=1)
            self.port = port
            self.connected = True
            time.sleep(2)  # Wait for Arduino to reset
            print(f"[SERIAL] Connected to {port} @ {self.baud} baud")
            
            # Send initial safe position
            self.send_command()
            return True
            
        except Exception as e:
            print(f"[SERIAL] Connection failed: {e}")
            self.connected = False
            return False
    
    def disconnect(self) -> None:
        """Disconnect from Arduino."""
        if self.serial and self.serial.is_open:
            # Send safe command before disconnecting
            self.safety = 1
            self.fire = 0
            self.send_command()
            time.sleep(0.1)
            self.serial.close()
        self.connected = False
        print("[SERIAL] Disconnected")
    
    def send_command(self) -> bool:
        """Send current state to Arduino."""
        if not self.connected or not self.serial:
            return False
        
        # Build command string
        command = f"P{int(self.pan)}T{int(self.tilt)}F{self.fire}L{self.led}R{self.laser}G0S{self.safety}M0\n"
        
        # Skip if same as last command (reduce serial traffic)
        if command == self.last_command:
            return True
        
        try:
            self.serial.write(command.encode())
            self.last_command = command
            print(f"[SERIAL] Sent: {command.strip()}")
            return True
        except Exception as e:
            print(f"[SERIAL] Send error: {e}")
            self.connected = False
            return False
    
    def move_to(self, pan: float, tilt: float) -> bool:
        """Move turret to position."""
        self.pan = max(5, min(185, pan))
        self.tilt = max(20, min(130, tilt))
        return self.send_command()
    
    def fire_burst(self, count: int = 1, interval_ms: int = 50) -> None:
        """Fire a burst of shots."""
        if not self.connected:
            return
        
        for i in range(count):
            self.fire = 1
            self.send_command()
            time.sleep(interval_ms / 1000.0)
            self.fire = 0
            self.send_command()
            if i < count - 1:
                time.sleep(interval_ms / 1000.0)
    
    def set_safety(self, safe: bool) -> None:
        """Set safety state."""
        self.safety = 1 if safe else 0
        self.send_command()
    
    def set_laser(self, on: bool) -> None:
        """Set laser state."""
        self.laser = 1 if on else 0
        self.send_command()
    
    def set_led(self, on: bool) -> None:
        """Set LED state."""
        self.led = 1 if on else 0
        self.send_command()


class MotionDetector:
    """Simple motion detection fallback when YOLO is not available."""
    
    def __init__(self, min_area: int = 500):
        self.min_area = min_area
        self.bg_subtractor = cv2.createBackgroundSubtractorMOG2(
            history=500, varThreshold=50, detectShadows=False
        )
        self.prev_frame = None
    
    def detect(self, frame: np.ndarray) -> List[Tuple[int, int, int, int, float]]:
        """
        Detect motion in frame.
        
        Returns:
            List of (x, y, w, h, score) detections
        """
        # Apply background subtraction
        fg_mask = self.bg_subtractor.apply(frame)
        
        # Threshold and clean up
        _, thresh = cv2.threshold(fg_mask, 127, 255, cv2.THRESH_BINARY)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        
        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        detections = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area < self.min_area:
                continue
            
            x, y, w, h = cv2.boundingRect(contour)
            
            # Score based on area (larger = higher confidence)
            score = min(1.0, area / 5000)
            
            detections.append((x, y, w, h, score))
        
        return detections


class YOLODetector:
    """YOLO object detector wrapper."""
    
    def __init__(self, model_path: str, confidence: float = 0.5, 
                 target_classes: List[str] = None):
        self.model = YOLO(model_path)
        self.confidence = confidence
        self.target_classes = target_classes or []
        
        # Get class names
        self.class_names = self.model.names
    
    def detect(self, frame: np.ndarray) -> List[Tuple[int, int, int, int, float]]:
        """
        Run YOLO detection on frame.
        
        Returns:
            List of (x, y, w, h, score) detections
        """
        results = self.model(frame, verbose=False, conf=self.confidence)
        
        detections = []
        for result in results:
            boxes = result.boxes
            for box in boxes:
                # Get class name
                cls_id = int(box.cls[0])
                cls_name = self.class_names[cls_id]
                
                # Filter by target classes if specified
                if self.target_classes and cls_name not in self.target_classes:
                    continue
                
                # Get bounding box
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                w = x2 - x1
                h = y2 - y1
                
                score = float(box.conf[0])
                
                detections.append((int(x1), int(y1), int(w), int(h), score))
        
        return detections


class SentryTestWindow:
    """
    Test window for Sentry Mode using OpenCV highgui.
    
    This is the fallback when PyQt5 is not available.
    """
    
    def __init__(self, camera_id: int = 0, yolo_model: str = None, 
                 serial_port: str = None, baud_rate: int = 115200):
        self.camera_id = camera_id
        self.yolo_model = yolo_model
        
        # Initialize Arduino serial connection
        self.turret = TurretSerial(serial_port, baud_rate)
        if serial_port:
            self.turret.connect(serial_port)
        
        # Initialize camera
        self.cap = cv2.VideoCapture(camera_id)
        if not self.cap.isOpened():
            raise RuntimeError(f"Could not open camera {camera_id}")
        
        # Set resolution
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        # Initialize detector
        if yolo_model and HAS_YOLO:
            self.detector = YOLODetector(yolo_model)
            print(f"[INFO] Using YOLO model: {yolo_model}")
        else:
            self.detector = MotionDetector()
            print("[INFO] Using motion detection")
        
        # Initialize tracker
        self.tracker = ByteTracker(track_thresh=0.5, track_buffer=30)
        
        # Initialize sentry controller
        self.config = SentryConfig()
        self.controller = SentryController(self.config)
        
        # Register callbacks
        self.controller.on_fire(self._on_fire)
        self.controller.on_turret_move(self._on_turret_move)
        self.controller.on_state_change(self._on_state_change)
        
        # UI state
        self.running = True
        self.mode = "normal"  # 'normal', 'set_guard', 'set_ambush', 'draw_track'
        self.last_click = None
        
        # Manual track drawing
        self.drawing_track = False
        self.drawn_points = []  # List of (norm_x, norm_y) points
        
        # Turret position tracking for visual feedback
        self.current_pan = 90.0
        self.current_tilt = 90.0
        self.aim_target = None  # (norm_x, norm_y) where turret is aiming
        
        # FPS tracking
        self.frame_times = []
        self.fps = 0.0
        
        # Window name
        self.window_name = "Sentry Ambush Mode - Test"
        
        # Start sentry
        self.controller.start()
    
    def _on_fire(self, command: FireCommand) -> None:
        """Handle fire command - send to Arduino."""
        print(f"[FIRE] Track {command.track_id} at ({command.ambush_point[0]:.2f}, "
              f"{command.ambush_point[1]:.2f}) - Confidence: {command.confidence:.2f}")
        
        # Send fire command to Arduino
        if self.turret.connected:
            self.turret.fire_burst(
                count=command.burst_count,
                interval_ms=self.config.burst_interval_ms
            )
    
    def _on_turret_move(self, pan: float, tilt: float) -> None:
        """Handle turret move command - send to Arduino."""
        print(f"[TURRET] Moving to Pan: {pan:.1f}, Tilt: {tilt:.1f}")
        
        # Track current position for visual feedback
        self.current_pan = pan
        self.current_tilt = tilt
        
        # Calculate aim target in normalized coords (approximate)
        # Pan: 0-180 -> x: 0-1, Tilt: 0-180 -> y: 0-1
        self.aim_target = (pan / 180.0, tilt / 180.0)
        
        # Send move command to Arduino
        if self.turret.connected:
            self.turret.move_to(pan, tilt)
        else:
            print(f"[TURRET] (No Arduino - would move to P{pan:.0f} T{tilt:.0f})")
    
    def _on_state_change(self, old_state: SentryState, new_state: SentryState) -> None:
        """Handle state change."""
        pass  # Logged by controller
    
    def _mouse_callback(self, event, x, y, flags, param):
        """Handle mouse events."""
        h, w = param['frame_size']
        norm_x = x / w
        norm_y = y / h
        
        if event == cv2.EVENT_LBUTTONDOWN:
            self.last_click = (x, y)
            
            if self.mode == "set_guard":
                self.controller.set_guard_point(norm_x, norm_y)
                self.mode = "normal"
                print(f"[UI] Guard point set to ({norm_x:.2f}, {norm_y:.2f})")
            
            elif self.mode == "set_ambush":
                self.controller.add_manual_ambush_point(norm_x, norm_y)
                self.mode = "normal"
                print(f"[UI] Ambush point added at ({norm_x:.2f}, {norm_y:.2f})")
            
            elif self.mode == "draw_track":
                # Start drawing a track
                self.drawing_track = True
                self.drawn_points = [(norm_x, norm_y)]
                print(f"[UI] Started drawing track at ({norm_x:.2f}, {norm_y:.2f})")
        
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing_track and self.mode == "draw_track":
                # Add point if moved enough distance
                if self.drawn_points:
                    last_x, last_y = self.drawn_points[-1]
                    dist = ((norm_x - last_x)**2 + (norm_y - last_y)**2)**0.5
                    if dist > 0.01:  # Minimum distance threshold
                        self.drawn_points.append((norm_x, norm_y))
        
        elif event == cv2.EVENT_LBUTTONUP:
            if self.drawing_track and self.mode == "draw_track":
                self.drawing_track = False
                if len(self.drawn_points) >= 5:
                    # Submit the drawn track
                    self._submit_drawn_track()
                else:
                    print("[UI] Track too short - draw a longer path")
                    self.drawn_points = []
    
    def run(self) -> None:
        """Main loop."""
        cv2.namedWindow(self.window_name)
        
        # Show initial frame to confirm window
        dummy = np.zeros((480, 640, 3), dtype=np.uint8)
        cv2.putText(dummy, "Initializing camera...", (200, 240),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow(self.window_name, dummy)
        cv2.waitKey(100)
        
        while self.running:
            # Read frame
            ret, frame = self.cap.read()
            if not ret:
                print("[ERROR] Failed to read frame")
                # Show error on screen
                cv2.putText(dummy, "Camera error - Press Q to quit", (150, 280),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.imshow(self.window_name, dummy)
                key = cv2.waitKey(1000) & 0xFF
                if key == ord('q') or key == 27:
                    break
                continue
            
            frame_size = frame.shape[:2]
            
            # Set up mouse callback
            cv2.setMouseCallback(self.window_name, self._mouse_callback, 
                               {'frame_size': frame_size})
            
            # Run detection
            detections = self.detector.detect(frame)
            
            # Run tracker
            tracks = self.tracker.update(detections)
            
            # Update sentry controller
            frame = self.controller.update(tracks, frame)
            
            # Calculate FPS
            self.frame_times.append(time.time())
            if len(self.frame_times) > 30:
                self.frame_times.pop(0)
            if len(self.frame_times) > 1:
                self.fps = len(self.frame_times) / (self.frame_times[-1] - self.frame_times[0])
            
            # Draw FPS
            cv2.putText(frame, f"FPS: {self.fps:.1f}", (10, frame.shape[0] - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            
            # Draw mode indicator
            if self.mode != "normal":
                mode_text = f"Click to set: {self.mode.replace('_', ' ').upper()}"
                cv2.putText(frame, mode_text, (frame.shape[1] // 2 - 100, 30),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
            
            # Draw fire status
            fire_status = "FIRE: ON" if self.controller.fire_enabled else "FIRE: OFF"
            color = (0, 0, 255) if self.controller.fire_enabled else (100, 100, 100)
            cv2.putText(frame, fire_status, (frame.shape[1] - 100, frame.shape[0] - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            
            # Draw Arduino status
            arduino_status = "ARDUINO: CONNECTED" if self.turret.connected else "ARDUINO: OFF"
            arduino_color = (0, 255, 0) if self.turret.connected else (100, 100, 100)
            cv2.putText(frame, arduino_status, (frame.shape[1] - 200, frame.shape[0] - 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, arduino_color, 2)
            
            # Draw turret aim position (big crosshair showing where turret is pointing)
            if self.aim_target:
                aim_x = int(self.aim_target[0] * frame.shape[1])
                aim_y = int(self.aim_target[1] * frame.shape[0])
                # Draw large crosshair
                cv2.line(frame, (aim_x - 30, aim_y), (aim_x + 30, aim_y), (0, 0, 255), 3)
                cv2.line(frame, (aim_x, aim_y - 30), (aim_x, aim_y + 30), (0, 0, 255), 3)
                cv2.circle(frame, (aim_x, aim_y), 20, (0, 0, 255), 2)
                cv2.putText(frame, f"AIM P{self.current_pan:.0f} T{self.current_tilt:.0f}",
                           (aim_x + 25, aim_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            
            # Draw current track being drawn
            if self.mode == "draw_track" and len(self.drawn_points) > 1:
                h, w = frame.shape[:2]
                for i in range(1, len(self.drawn_points)):
                    pt1 = (int(self.drawn_points[i-1][0] * w), int(self.drawn_points[i-1][1] * h))
                    pt2 = (int(self.drawn_points[i][0] * w), int(self.drawn_points[i][1] * h))
                    cv2.line(frame, pt1, pt2, (255, 255, 0), 3)
                # Draw arrow at end
                if len(self.drawn_points) >= 2:
                    end = (int(self.drawn_points[-1][0] * w), int(self.drawn_points[-1][1] * h))
                    cv2.circle(frame, end, 8, (255, 255, 0), -1)
            
            # Show frame
            cv2.imshow(self.window_name, frame)
            
            # Handle keyboard
            key = cv2.waitKey(1) & 0xFF
            self._handle_key(key)
        
        # Cleanup
        self.controller.stop()
        self.turret.disconnect()
        self.cap.release()
        cv2.destroyAllWindows()
    
    def _handle_key(self, key: int) -> None:
        """Handle keyboard input."""
        if key == ord('q') or key == 27:  # Q or ESC
            self.running = False
        
        elif key == ord(' '):  # Space - toggle fire
            if self.controller.fire_enabled:
                self.controller.disable_fire()
            else:
                self.controller.enable_fire()
        
        elif key == ord('l'):  # L - learning mode
            self.controller.force_learning_mode()
        
        elif key == ord('w'):  # W - watching mode
            self.controller.force_watching_mode()
        
        elif key == ord('r'):  # R - reset
            self.tracker.reset()
            self.controller.stop()
            self.controller.start()
            print("[UI] Reset all tracks")
        
        elif key == ord('g'):  # G - set guard point
            self.mode = "set_guard"
            print("[UI] Click to set guard point")
        
        elif key == ord('a'):  # A - add ambush point
            self.mode = "set_ambush"
            print("[UI] Click to add ambush point")
        
        elif key == ord('c'):  # C - clear manual points
            self.controller.clear_manual_ambush_points()
            print("[UI] Cleared manual ambush points")
        
        elif key == ord('s'):  # S - save
            self.controller._save_tracks()
            self.config.save()
            print("[UI] Configuration saved")
        
        elif key == ord('d'):  # D - toggle debug
            self.config.show_debug_overlay = not self.config.show_debug_overlay
            print(f"[UI] Debug overlay: {self.config.show_debug_overlay}")
        
        elif key == ord('t'):  # T - toggle Arduino connection
            if self.turret.connected:
                self.turret.disconnect()
                print("[UI] Arduino disconnected")
            else:
                if self.turret.connect():
                    print("[UI] Arduino connected")
                else:
                    print("[UI] Arduino connection failed")
        
        elif key == ord('p'):  # P - draw track (path)
            if self.mode == "draw_track":
                self.mode = "normal"
                self.drawn_points = []
                print("[UI] Cancelled track drawing")
            else:
                self.mode = "draw_track"
                print("[UI] DRAW MODE: Click and drag to draw a track path")
        
        elif key == ord('x'):  # X - cancel current mode
            self.mode = "normal"
            self.drawn_points = []
            print("[UI] Cancelled current mode")
    
    def _submit_drawn_track(self) -> None:
        """Submit manually drawn track to the path analyzer."""
        if len(self.drawn_points) < 5:
            print("[UI] Track too short")
            return
        
        # Create a fake track from drawn points
        import time as time_module
        from track_recorder import TrackPoint, Track
        
        points = []
        current_time = time_module.time()
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
                timestamp=current_time + i * 0.033,  # ~30fps timing
                velocity_x=vx, velocity_y=vy,
                speed=(vx**2 + vy**2)**0.5
            ))
        
        # Create track
        track = Track(
            track_id=-1,  # Manual track
            points=points,
            created_at=current_time,
            last_updated=current_time + len(points) * 0.033,
            is_active=False,
            is_complete=True
        )
        
        # Submit to path analyzer using analyze_track() which handles matching
        print(f"[UI] Submitted manual track with {len(points)} points")
        confirmed = self.controller.path_analyzer.analyze_track(track)
        if confirmed:
            print(f"[UI] Track confirmed as pattern! Ambush point: {confirmed.ambush_point}")
        else:
            print(f"[UI] Track added to pending (need 2+ similar tracks for confirmation)")
        
        # Clear drawn points
        self.drawn_points = []
        self.mode = "normal"


if HAS_PYQT:
    class SentryTestWindowQt(QMainWindow):
        """
        Test window for Sentry Mode using PyQt5.
        
        Provides a more complete UI with controls and status display.
        """
        
        def __init__(self, camera_id: int = 0, yolo_model: str = None):
            super().__init__()
            
            self.camera_id = camera_id
            self.yolo_model = yolo_model
            
            # Initialize camera
            self.cap = cv2.VideoCapture(camera_id)
            if not self.cap.isOpened():
                raise RuntimeError(f"Could not open camera {camera_id}")
            
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            
            # Initialize detector
            if yolo_model and HAS_YOLO:
                self.detector = YOLODetector(yolo_model)
            else:
                self.detector = MotionDetector()
            
            # Initialize tracker
            self.tracker = ByteTracker(track_thresh=0.5, track_buffer=30)
            
            # Initialize sentry controller
            self.config = SentryConfig()
            self.controller = SentryController(self.config)
            
            # Register callbacks
            self.controller.on_fire(self._on_fire)
            self.controller.on_turret_move(self._on_turret_move)
            
            # Setup UI
            self._setup_ui()
            
            # FPS tracking
            self.frame_times = []
            self.fps = 0.0
            
            # Click mode
            self.click_mode = None
            
            # Start timer for frame updates
            self.timer = QTimer()
            self.timer.timeout.connect(self._update_frame)
            self.timer.start(33)  # ~30 FPS
            
            # Start sentry
            self.controller.start()
        
        def _setup_ui(self):
            """Setup the user interface."""
            self.setWindowTitle("Sentry Ambush Mode - Test Harness")
            self.setGeometry(100, 100, 1000, 700)
            
            # Central widget
            central = QWidget()
            self.setCentralWidget(central)
            
            # Main layout
            layout = QHBoxLayout(central)
            
            # Video display
            self.video_label = QLabel()
            self.video_label.setMinimumSize(640, 480)
            self.video_label.mousePressEvent = self._on_video_click
            layout.addWidget(self.video_label, stretch=3)
            
            # Control panel
            control_panel = QWidget()
            control_layout = QVBoxLayout(control_panel)
            control_panel.setMaximumWidth(300)
            layout.addWidget(control_panel)
            
            # State group
            state_group = QGroupBox("State")
            state_layout = QVBoxLayout(state_group)
            
            self.state_label = QLabel("State: IDLE")
            self.state_label.setStyleSheet("font-size: 16px; font-weight: bold;")
            state_layout.addWidget(self.state_label)
            
            self.stats_label = QLabel("Stats: ...")
            state_layout.addWidget(self.stats_label)
            
            control_layout.addWidget(state_group)
            
            # Fire control group
            fire_group = QGroupBox("Fire Control")
            fire_layout = QVBoxLayout(fire_group)
            
            self.fire_checkbox = QCheckBox("Enable Auto-Fire")
            self.fire_checkbox.stateChanged.connect(self._on_fire_toggle)
            fire_layout.addWidget(self.fire_checkbox)
            
            self.burst_checkbox = QCheckBox("Burst Mode")
            self.burst_checkbox.setChecked(self.config.burst_enabled)
            self.burst_checkbox.stateChanged.connect(
                lambda s: setattr(self.config, 'burst_enabled', s == Qt.Checked)
            )
            fire_layout.addWidget(self.burst_checkbox)
            
            control_layout.addWidget(fire_group)
            
            # Mode control group
            mode_group = QGroupBox("Mode Control")
            mode_layout = QVBoxLayout(mode_group)
            
            btn_learning = QPushButton("Force Learning Mode")
            btn_learning.clicked.connect(self.controller.force_learning_mode)
            mode_layout.addWidget(btn_learning)
            
            btn_watching = QPushButton("Force Watching Mode")
            btn_watching.clicked.connect(self.controller.force_watching_mode)
            mode_layout.addWidget(btn_watching)
            
            btn_reset = QPushButton("Reset All Tracks")
            btn_reset.clicked.connect(self._reset_tracks)
            mode_layout.addWidget(btn_reset)
            
            control_layout.addWidget(mode_group)
            
            # Manual points group
            points_group = QGroupBox("Manual Points")
            points_layout = QVBoxLayout(points_group)
            
            btn_guard = QPushButton("Set Guard Point (Click)")
            btn_guard.clicked.connect(lambda: setattr(self, 'click_mode', 'guard'))
            points_layout.addWidget(btn_guard)
            
            btn_ambush = QPushButton("Add Ambush Point (Click)")
            btn_ambush.clicked.connect(lambda: setattr(self, 'click_mode', 'ambush'))
            points_layout.addWidget(btn_ambush)
            
            btn_clear = QPushButton("Clear Manual Points")
            btn_clear.clicked.connect(self.controller.clear_manual_ambush_points)
            points_layout.addWidget(btn_clear)
            
            control_layout.addWidget(points_group)
            
            # Debug group
            debug_group = QGroupBox("Debug")
            debug_layout = QVBoxLayout(debug_group)
            
            self.debug_checkbox = QCheckBox("Show Debug Overlay")
            self.debug_checkbox.setChecked(self.config.show_debug_overlay)
            self.debug_checkbox.stateChanged.connect(
                lambda s: setattr(self.config, 'show_debug_overlay', s == Qt.Checked)
            )
            debug_layout.addWidget(self.debug_checkbox)
            
            btn_save = QPushButton("Save Configuration")
            btn_save.clicked.connect(self._save_config)
            debug_layout.addWidget(btn_save)
            
            control_layout.addWidget(debug_group)
            
            # Spacer
            control_layout.addStretch()
            
            # Status bar
            self.statusBar().showMessage("Ready")
        
        def _update_frame(self):
            """Update video frame."""
            ret, frame = self.cap.read()
            if not ret:
                return
            
            # Run detection
            detections = self.detector.detect(frame)
            
            # Run tracker
            tracks = self.tracker.update(detections)
            
            # Update sentry controller
            frame = self.controller.update(tracks, frame)
            
            # Calculate FPS
            self.frame_times.append(time.time())
            if len(self.frame_times) > 30:
                self.frame_times.pop(0)
            if len(self.frame_times) > 1:
                self.fps = len(self.frame_times) / (self.frame_times[-1] - self.frame_times[0])
            
            # Draw FPS
            cv2.putText(frame, f"FPS: {self.fps:.1f}", (10, frame.shape[0] - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            
            # Draw click mode hint
            if self.click_mode:
                hint = f"Click video to set {self.click_mode} point"
                cv2.putText(frame, hint, (frame.shape[1] // 2 - 120, 30),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
            
            # Convert to Qt format
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame_rgb.shape
            bytes_per_line = ch * w
            qt_image = QImage(frame_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.video_label.setPixmap(QPixmap.fromImage(qt_image))
            
            # Update state display
            self.state_label.setText(f"State: {self.controller.get_state_name()}")
            
            stats = self.controller.get_stats()
            stats_text = "\n".join([f"{k}: {v}" for k, v in stats.items()])
            self.stats_label.setText(stats_text)
        
        def _on_video_click(self, event):
            """Handle click on video."""
            if not self.click_mode:
                return
            
            # Get click position relative to video
            x = event.pos().x()
            y = event.pos().y()
            
            # Normalize
            label_w = self.video_label.width()
            label_h = self.video_label.height()
            
            norm_x = x / label_w
            norm_y = y / label_h
            
            if self.click_mode == 'guard':
                self.controller.set_guard_point(norm_x, norm_y)
                self.statusBar().showMessage(f"Guard point set to ({norm_x:.2f}, {norm_y:.2f})")
            
            elif self.click_mode == 'ambush':
                self.controller.add_manual_ambush_point(norm_x, norm_y)
                self.statusBar().showMessage(f"Ambush point added at ({norm_x:.2f}, {norm_y:.2f})")
            
            self.click_mode = None
        
        def _on_fire_toggle(self, state):
            """Handle fire enable toggle."""
            if state == Qt.Checked:
                self.controller.enable_fire()
            else:
                self.controller.disable_fire()
        
        def _on_fire(self, command: FireCommand):
            """Handle fire command."""
            self.statusBar().showMessage(
                f"FIRE! Track {command.track_id} - Confidence: {command.confidence:.2f}"
            )
        
        def _on_turret_move(self, pan: float, tilt: float):
            """Handle turret move."""
            self.statusBar().showMessage(f"Turret: Pan={pan:.1f}, Tilt={tilt:.1f}")
        
        def _reset_tracks(self):
            """Reset all tracks."""
            self.tracker.reset()
            self.controller.stop()
            self.controller.start()
            self.statusBar().showMessage("All tracks reset")
        
        def _save_config(self):
            """Save configuration."""
            self.controller._save_tracks()
            self.config.save()
            self.statusBar().showMessage("Configuration saved")
        
        def closeEvent(self, event):
            """Handle window close."""
            self.timer.stop()
            self.controller.stop()
            self.cap.release()
            event.accept()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Sentry Ambush Mode Test Harness")
    parser.add_argument('--camera', type=int, default=0, help='Camera ID')
    parser.add_argument('--yolo', type=str, default=None, 
                       help='Path to YOLO model (e.g., yolov8n.pt)')
    parser.add_argument('--no-gui', action='store_true',
                       help='Run in OpenCV-only mode (no PyQt5)')
    parser.add_argument('--port', type=str, default=None,
                       help='Serial port for Arduino (e.g., COM3)')
    parser.add_argument('--baud', type=int, default=115200,
                       help='Baud rate for Arduino (default: 115200)')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("  SENTRY AMBUSH MODE - TEST HARNESS")
    print("=" * 60)
    print(f"  Camera: {args.camera}")
    print(f"  YOLO Model: {args.yolo or 'None (using motion detection)'}")
    print(f"  GUI Mode: {'OpenCV' if args.no_gui or not HAS_PYQT else 'PyQt5'}")
    print(f"  Arduino Port: {args.port or 'None (press T to connect)'}")
    print("=" * 60)
    print()
    print("Controls:")
    print("  SPACE  - Toggle auto-fire")
    print("  G      - Set guard point (then click)")
    print("  A      - Add ambush point (then click)")
    print("  P      - Draw track path (click and drag)")
    print("  L      - Force learning mode")
    print("  W      - Force watching mode")
    print("  R      - Reset all tracks")
    print("  T      - Toggle Arduino connection")
    print("  D      - Toggle debug overlay")
    print("  X      - Cancel current mode")
    print("  Q/ESC  - Quit")
    print()
    
    if HAS_PYQT and not args.no_gui:
        app = QApplication(sys.argv)
        window = SentryTestWindowQt(args.camera, args.yolo)
        window.show()
        sys.exit(app.exec_())
    else:
        window = SentryTestWindow(
            camera_id=args.camera, 
            yolo_model=args.yolo,
            serial_port=args.port,
            baud_rate=args.baud
        )
        window.run()


if __name__ == "__main__":
    main()

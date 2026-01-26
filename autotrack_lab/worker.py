from __future__ import annotations

import time
from dataclasses import dataclass

import cv2
import numpy as np
from PyQt5.QtCore import QObject, pyqtSignal

from .tracking import TargetLock, YoloDetector, SimpleBlobDetector


@dataclass
class FrameInfo:
    locked: bool = False
    mode: str = "follow"
    preset: str = "Balanced"
    message: str = ""


class VisionWorker(QObject):
    frame_ready = pyqtSignal(np.ndarray, dict)
    status = pyqtSignal(str)
    fps = pyqtSignal(float)

    def __init__(self, controller, preset: dict, tracking_defaults: dict, camera_index: int = 0) -> None:
        super().__init__()
        self.controller = controller
        self.preset = preset
        self.tracking_defaults = tracking_defaults
        self.camera_index = camera_index
        self._restart_camera = False
        self._running = False
        self._tracking_enabled = False
        self._mode = "follow"
        self._frame_idx = 0
        self._last_fps_time = time.time()
        self._fps_count = 0
        self._last_strike_time = 0.0
        self.lock = TargetLock()
        self.detector_mode = tracking_defaults.get("detector", "blob")
        self.detector = YoloDetector(
            tracking_defaults.get("yolo_model", "yolov8n.pt"),
            tracking_defaults.get("yolo_conf", 0.45),
        )
        self.blob_detector = SimpleBlobDetector(
            min_area=int(tracking_defaults.get("blob_min_area", 800)),
            max_area_ratio=float(tracking_defaults.get("blob_max_area_ratio", 0.4)),
        )
        self.tracker_type = tracking_defaults.get("tracker_type", "CSRT")
        self._tracker_available = True
        self._candidate_bbox: tuple[int, int, int, int] | None = None
        self._candidate_hits = 0

    def set_preset(self, preset: dict) -> None:
        self.preset = preset

    def set_mode(self, mode: str) -> None:
        self._mode = mode

    def set_tracking_enabled(self, enabled: bool) -> None:
        self._tracking_enabled = enabled
        if not enabled:
            self.lock.reset()

    def set_camera_index(self, index: int) -> None:
        self.camera_index = int(index)
        self._restart_camera = True

    def stop(self) -> None:
        self._running = False

    def run(self) -> None:
        cap = self._open_camera()
        if cap is None:
            self.status.emit("Camera open failed (see debug output)")
            return
        self._running = True
        self.status.emit("Camera ready")
        while self._running:
            if self._restart_camera:
                self._restart_camera = False
                try:
                    cap.release()
                except Exception:
                    pass
                cap = self._open_camera()
                if cap is None:
                    self.status.emit("Camera reopen failed")
                    break
            ok, frame = cap.read()
            if not ok:
                self.status.emit("Camera read failed")
                time.sleep(0.05)
                continue
            self._frame_idx += 1
            info = self._process_frame(frame)
            self._emit_fps()
            self.frame_ready.emit(frame, info)
        cap.release()
        self.status.emit("Camera stopped")

    def _open_camera(self) -> cv2.VideoCapture | None:
        backends = [
            ("DSHOW", cv2.CAP_DSHOW),
            ("MSMF", cv2.CAP_MSMF),
            ("ANY", cv2.CAP_ANY),
        ]
        indexes = [self.camera_index, 0, 1, 2]
        self.status.emit(f"[CAM] OpenCV {cv2.__version__}")
        for idx in indexes:
            for name, backend in backends:
                try:
                    cap = cv2.VideoCapture(int(idx), backend)
                    if cap.isOpened():
                        w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
                        h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
                        self.status.emit(f"[CAM] Opened index={idx} backend={name} {int(w)}x{int(h)}")
                        return cap
                    self.status.emit(f"[CAM] Failed index={idx} backend={name}")
                    cap.release()
                except Exception as exc:
                    self.status.emit(f"[CAM] Error index={idx} backend={name}: {exc}")
        return None

    def _process_frame(self, frame: np.ndarray) -> dict:
        info = FrameInfo(locked=self.lock.bbox is not None, mode=self._mode)
        if self._tracking_enabled:
            self._update_tracking(frame, info)
        else:
            info.message = "Tracking idle"
        payload = info.__dict__
        payload["bbox"] = self.lock.bbox
        payload["candidate"] = self._candidate_bbox
        payload["detector"] = self.detector_mode
        return payload

    def _update_tracking(self, frame: np.ndarray, info: FrameInfo) -> None:
        refresh = self._frame_idx % int(self.preset["detect_interval"]) == 0
        if self.lock.bbox is None and refresh:
            try:
                if self.detector_mode == "yolo":
                    detections = self.detector.detect(frame)
                else:
                    detections = self.blob_detector.detect(frame)
                if detections:
                    first = detections[0]
                    if self._candidate_bbox == first.bbox:
                        self._candidate_hits += 1
                    else:
                        self._candidate_bbox = first.bbox
                        self._candidate_hits = 1
                    if self._candidate_hits >= 2:
                        self.lock.acquire(frame, first.bbox, self.tracker_type)
                        self._tracker_available = self.lock.tracker is not None
                        info.message = "Locked first detection"
            except Exception as exc:
                info.message = "Detection error"
                self.status.emit(f"[DETECT] Failed: {exc}")
        elif self.lock.bbox is not None:
            if self._tracker_available:
                ok = self.lock.update(frame)
                if not ok and self.lock.lost_count > int(self.preset["lost_max"]):
                    self.lock.reset()
                    self._candidate_bbox = None
                    self._candidate_hits = 0
                    info.message = "Lock lost"
            else:
                # Tracker unavailable: keep re-detecting to update lock
                if refresh:
                    if self.detector_mode == "yolo":
                        detections = self.detector.detect(frame)
                    else:
                        detections = self.blob_detector.detect(frame)
                    if detections:
                        first = detections[0]
                        self.lock.acquire(frame, first.bbox, self.tracker_type)
                        info.message = "Locked (detector only)"
                    else:
                        self.lock.lost_count += 1
                        if self.lock.lost_count > int(self.preset["lost_max"]):
                            self.lock.reset()
                            self._candidate_bbox = None
                            self._candidate_hits = 0
                            info.message = "Lock lost"

        if self.lock.bbox is None:
            info.locked = False
            info.message = info.message or "No target"
            return

        center = self.lock.center()
        if center is None:
            return
        vx, vy = self.lock.velocity()
        if self._mode == "quick":
            self._quick_strike(frame, center, (vx, vy), info)
        else:
            self._follow(frame, center, info)
        info.locked = True

    def _follow(self, frame: np.ndarray, center: tuple[float, float], info: FrameInfo) -> None:
        aim_x, aim_y = center
        self._aim_at(frame, aim_x, aim_y, info)
        info.message = "Follow lock"

    def _quick_strike(
        self,
        frame: np.ndarray,
        center: tuple[float, float],
        velocity: tuple[float, float],
        info: FrameInfo,
    ) -> None:
        now = time.time()
        cooldown = self.preset["strike_cooldown_ms"] / 1000.0
        if now - self._last_strike_time < cooldown:
            info.message = "Quick strike cooldown"
            return
        vx, vy = velocity
        speed = (vx * vx + vy * vy) ** 0.5
        lead_time = self.preset["lead_time_ms"] / 1000.0
        if speed <= float(self.preset["settle_speed_px"]):
            aim_x, aim_y = center
            info.message = "Quick strike: settled"
        else:
            aim_x = center[0] + vx * lead_time
            aim_y = center[1] + vy * lead_time
            info.message = "Quick strike: predicted"
        self._aim_at(frame, aim_x, aim_y, info)
        self._last_strike_time = now

    def _aim_at(self, frame: np.ndarray, aim_x: float, aim_y: float, info: FrameInfo) -> None:
        h, w = frame.shape[:2]
        dx = aim_x - (w / 2.0)
        dy = aim_y - (h / 2.0)
        px_per_deg_x = float(self.preset["pixels_per_degree_x"])
        px_per_deg_y = float(self.preset["pixels_per_degree_y"])
        gain = float(self.preset["aim_gain"])
        delta_pan = -dx / px_per_deg_x * gain
        delta_tilt = dy / px_per_deg_y * gain
        max_step = float(self.preset["max_step_deg"])
        delta_pan = float(np.clip(delta_pan, -max_step, max_step))
        delta_tilt = float(np.clip(delta_tilt, -max_step, max_step))
        pan, tilt = self.controller.get_pose()
        target_pan = pan + delta_pan
        target_tilt = tilt + delta_tilt
        time_ms = int(self.preset["bus_time_ms"])
        self.controller.set_pose(target_pan, target_tilt, time_ms=time_ms)

    def _emit_fps(self) -> None:
        self._fps_count += 1
        now = time.time()
        if now - self._last_fps_time >= 1.0:
            fps = self._fps_count / (now - self._last_fps_time)
            self._fps_count = 0
            self._last_fps_time = now
            self.fps.emit(fps)

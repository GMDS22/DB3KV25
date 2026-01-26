from __future__ import annotations

from dataclasses import dataclass, field
from collections import deque
import time

import cv2
import numpy as np

try:
    from ultralytics import YOLO  # type: ignore
except Exception:
    YOLO = None


@dataclass
class Detection:
    bbox: tuple[int, int, int, int]
    conf: float
    cls_id: int


class YoloDetector:
    def __init__(self, model_path: str, conf: float) -> None:
        self.model_path = model_path
        self.conf = conf
        self.model = None

    def load(self) -> None:
        if YOLO is None:
            raise RuntimeError("Ultralytics not installed.")
        self.model = YOLO(self.model_path)

    def detect(self, frame: np.ndarray) -> list[Detection]:
        if self.model is None:
            self.load()
        results = self.model.predict(frame, conf=self.conf, verbose=False)
        dets: list[Detection] = []
        for r in results:
            if r.boxes is None:
                continue
            for b in r.boxes:
                xyxy = b.xyxy[0].cpu().numpy().astype(int)
                x1, y1, x2, y2 = xyxy.tolist()
                dets.append(Detection((x1, y1, x2, y2), float(b.conf[0]), int(b.cls[0])))
        return dets


class SimpleBlobDetector:
    def __init__(self, min_area: int = 800, max_area_ratio: float = 0.4) -> None:
        self.min_area = min_area
        self.max_area_ratio = max_area_ratio

    def detect(self, frame: np.ndarray) -> list[Detection]:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (7, 7), 0)
        _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            return []
        frame_area = float(frame.shape[0] * frame.shape[1])
        max_area = frame_area * float(self.max_area_ratio)
        contours = [
            c
            for c in contours
            if self.min_area <= cv2.contourArea(c) <= max_area
        ]
        if not contours:
            return []
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        return [Detection((x, y, x + w, y + h), 1.0, 0)]


def create_tracker(tracker_type: str):
    t = tracker_type.upper()
    def _legacy(name: str):
        try:
            legacy = getattr(cv2, "legacy", None)
            if legacy and hasattr(legacy, name):
                return getattr(legacy, name)()
        except Exception:
            return None
        return None

    def _direct(name: str):
        try:
            if hasattr(cv2, name):
                return getattr(cv2, name)()
        except Exception:
            return None
        return None

    if t == "CSRT":
        return _direct("TrackerCSRT_create") or _legacy("TrackerCSRT_create")
    if t == "KCF":
        return _direct("TrackerKCF_create") or _legacy("TrackerKCF_create")
    if t == "MOSSE":
        return _direct("TrackerMOSSE_create") or _legacy("TrackerMOSSE_create")
    return _direct("TrackerCSRT_create") or _legacy("TrackerCSRT_create")


@dataclass
class TargetLock:
    bbox: tuple[int, int, int, int] | None = None
    tracker: any = None
    last_seen: float = 0.0
    lost_count: int = 0
    centers: deque[tuple[float, float, float]] = field(default_factory=lambda: deque(maxlen=6))

    def reset(self) -> None:
        self.bbox = None
        self.tracker = None
        self.last_seen = 0.0
        self.lost_count = 0
        self.centers.clear()

    def acquire(self, frame: np.ndarray, bbox: tuple[int, int, int, int], tracker_type: str) -> None:
        x1, y1, x2, y2 = bbox
        self.bbox = bbox
        self.last_seen = time.time()
        self.lost_count = 0
        self.tracker = create_tracker(tracker_type)
        if self.tracker is not None:
            self.tracker.init(frame, (x1, y1, x2 - x1, y2 - y1))
        self._record_center(bbox)

    def update(self, frame: np.ndarray) -> bool:
        if self.tracker is None:
            self.lost_count += 1
            return False
        ok, rect = self.tracker.update(frame)
        if not ok:
            self.lost_count += 1
            return False
        x, y, w, h = rect
        bbox = (int(x), int(y), int(x + w), int(y + h))
        self.bbox = bbox
        self.last_seen = time.time()
        self.lost_count = 0
        self._record_center(bbox)
        return True

    def _record_center(self, bbox: tuple[int, int, int, int]) -> None:
        x1, y1, x2, y2 = bbox
        cx = (x1 + x2) / 2.0
        cy = (y1 + y2) / 2.0
        self.centers.append((cx, cy, time.time()))

    def velocity(self) -> tuple[float, float]:
        if len(self.centers) < 2:
            return 0.0, 0.0
        (x1, y1, t1), (x2, y2, t2) = self.centers[-2], self.centers[-1]
        dt = max(1e-3, t2 - t1)
        return (x2 - x1) / dt, (y2 - y1) / dt

    def center(self) -> tuple[float, float] | None:
        if not self.bbox:
            return None
        x1, y1, x2, y2 = self.bbox
        return ((x1 + x2) / 2.0, (y1 + y2) / 2.0)

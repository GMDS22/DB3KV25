from __future__ import annotations

import queue
import threading
import time
import uuid
import zlib
from pathlib import Path
from typing import Any, Callable, Dict, Optional, Tuple

import cv2
import numpy as np


class SnapshotCaptureService:
    """Asynchronous snapshot capture with frame-key deduplication."""

    def __init__(
        self,
        *,
        base_dir: Path,
        frame_provider: Optional[Callable[[], Optional[np.ndarray]]] = None,
        queue_size: int = 96,
        jpeg_quality: int = 85,
    ):
        self.base_dir = Path(base_dir)
        self._frame_provider = frame_provider
        self._jpeg_quality = int(max(40, min(100, jpeg_quality)))
        self._queue: queue.Queue[Dict[str, Any]] = queue.Queue(maxsize=max(8, int(queue_size)))
        self._stop_event = threading.Event()
        self._thread: Optional[threading.Thread] = None
        self._lock = threading.Lock()
        self._dedup_relpath: Dict[Tuple[str, str], str] = {}
        self._dropped_requests = 0
        self._transient_failures = 0
        self._write_failures = 0
        self._last_error = ""

    def start(self) -> None:
        if self._thread is not None and self._thread.is_alive():
            return
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run, name="mission-snapshot-writer", daemon=True)
        self._thread.start()

    def stop(self, timeout_s: float = 2.0) -> None:
        self._stop_event.set()
        try:
            self._queue.put_nowait({"kind": "stop"})
        except Exception:
            pass
        if self._thread is not None:
            self._thread.join(timeout=max(0.1, float(timeout_s)))
            self._thread = None

    def set_frame_provider(self, frame_provider: Callable[[], Optional[np.ndarray]]) -> None:
        self._frame_provider = frame_provider

    def health_snapshot(self) -> Dict[str, Any]:
        with self._lock:
            return {
                "queue_size": int(self._queue.qsize()),
                "dropped_requests": int(self._dropped_requests),
                "transient_failures": int(self._transient_failures),
                "write_failures": int(self._write_failures),
                "dedup_entries": int(len(self._dedup_relpath)),
                "last_error": str(self._last_error or ""),
            }

    def request_capture(
        self,
        *,
        mission_id: str,
        event_type: str,
        track_id: Optional[int] = None,
        bbox: Optional[Tuple[int, int, int, int]] = None,
        timestamp: Optional[float] = None,
    ) -> Optional[Dict[str, Any]]:
        if not mission_id:
            return None
        provider = self._frame_provider
        if provider is None:
            return None
        frame = provider()
        if frame is None:
            return None

        frame_key = self._frame_key(frame)
        dedup_key = (str(mission_id), frame_key)
        with self._lock:
            existing = self._dedup_relpath.get(dedup_key)
        if existing:
            return {
                "media_id": f"{mission_id}:{frame_key}",
                "kind": "snapshot",
                "rel_path": existing,
                "frame_key": frame_key,
                "timestamp": float(timestamp or time.time()),
                "dedup": True,
            }

        mission_dir = self.base_dir / mission_id / "snapshots"
        mission_dir.mkdir(parents=True, exist_ok=True)
        filename = f"frame_{frame_key}_{uuid.uuid4().hex[:6]}.jpg"
        abs_path = mission_dir / filename
        rel_path = f"{mission_id}/snapshots/{filename}"

        with self._lock:
            self._dedup_relpath[dedup_key] = rel_path

        payload = {
            "kind": "write_snapshot",
            "mission_id": str(mission_id),
            "abs_path": str(abs_path),
            "frame_key": frame_key,
            "rel_path": rel_path,
            "frame": frame,
            "bbox": tuple(int(v) for v in bbox) if bbox is not None and len(bbox) == 4 else None,
        }
        try:
            self._queue.put_nowait(payload)
        except queue.Full:
            with self._lock:
                self._dropped_requests += 1
                self._dedup_relpath.pop(dedup_key, None)
            return None

        return {
            "media_id": f"{mission_id}:{frame_key}",
            "kind": "snapshot",
            "rel_path": rel_path,
            "frame_key": frame_key,
            "timestamp": float(timestamp or time.time()),
            "dedup": False,
            "event_type": str(event_type),
            "track_id": int(track_id) if track_id is not None else -1,
        }

    def _run(self) -> None:
        while not self._stop_event.is_set():
            try:
                cmd = self._queue.get(timeout=0.2)
            except queue.Empty:
                continue

            kind = str(cmd.get("kind") or "")
            if kind == "stop":
                break
            if kind != "write_snapshot":
                continue

            frame = cmd.get("frame")
            if not isinstance(frame, np.ndarray) or frame.size == 0:
                continue
            abs_path = Path(str(cmd.get("abs_path") or ""))
            frame_key = str(cmd.get("frame_key") or "")
            mission_id = str(cmd.get("mission_id") or "")
            dedup_key = (mission_id, frame_key)
            ok = False
            try:
                abs_path.parent.mkdir(parents=True, exist_ok=True)
                ok = bool(cv2.imwrite(str(abs_path), frame, [int(cv2.IMWRITE_JPEG_QUALITY), int(self._jpeg_quality)]))
            except Exception:
                ok = False

            if not ok:
                with self._lock:
                    self._transient_failures += 1
                try:
                    time.sleep(0.02)
                    abs_path.parent.mkdir(parents=True, exist_ok=True)
                    ok = bool(cv2.imwrite(str(abs_path), frame, [int(cv2.IMWRITE_JPEG_QUALITY), int(self._jpeg_quality)]))
                except Exception as exc:
                    with self._lock:
                        self._write_failures += 1
                        self._last_error = str(exc)
                        self._dedup_relpath.pop(dedup_key, None)
                    print(f"[MISSION_ARCHIVE] snapshot write failed: {exc}", flush=True)

            if not ok:
                with self._lock:
                    self._write_failures += 1
                    self._last_error = "cv2.imwrite returned false"
                    self._dedup_relpath.pop(dedup_key, None)

    @staticmethod
    def _frame_key(frame: np.ndarray) -> str:
        if frame is None or frame.size == 0:
            return "empty"
        h, w = frame.shape[:2]
        small = cv2.resize(frame, (64, 36), interpolation=cv2.INTER_AREA)
        crc = zlib.crc32(small.tobytes()) & 0xFFFFFFFF
        return f"{w}x{h}_{crc:08x}"

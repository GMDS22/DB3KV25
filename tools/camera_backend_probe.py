from __future__ import annotations

import json
import time

import cv2
import numpy as np


def is_probable_partial_frame(frame: np.ndarray | None) -> bool:
    if frame is None or not isinstance(frame, np.ndarray) or frame.size == 0 or frame.ndim < 2:
        return False
    h, w = frame.shape[:2]
    if h < 32 or w < 32:
        return False
    tl = frame[: max(16, h // 4), : max(16, w // 4)]
    br = frame[h - max(16, h // 4) :, w - max(16, w // 4) :]
    if tl.size == 0 or br.size == 0:
        return False
    tl_mean = float(np.mean(tl))
    br_mean = float(np.mean(br))
    br_max = int(np.max(br))
    return tl_mean > 8.0 and br_max <= 6 and br_mean <= 1.5


def probe_backend(name: str, backend: int | None) -> dict[str, object]:
    cap = None
    result: dict[str, object] = {
        "backend": name,
        "opened": False,
        "actual": None,
        "frames_read": 0,
        "partial_frames": 0,
        "black_frames": 0,
        "first_partial_at": None,
        "sample": [],
    }
    try:
        cap = cv2.VideoCapture(0) if backend is None else cv2.VideoCapture(0, backend)
        time.sleep(0.5)
        if not cap.isOpened():
            return result
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        result["opened"] = True
        result["actual"] = [int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))]
        start = time.time()
        while time.time() - start < 8.0:
            ok, frame = cap.read()
            if not ok or frame is None:
                time.sleep(0.05)
                continue
            result["frames_read"] = int(result["frames_read"]) + 1
            is_partial = is_probable_partial_frame(frame)
            is_black = float(np.mean(frame)) <= 2.0
            if is_partial:
                result["partial_frames"] = int(result["partial_frames"]) + 1
                if result["first_partial_at"] is None:
                    result["first_partial_at"] = round(time.time() - start, 3)
            if is_black:
                result["black_frames"] = int(result["black_frames"]) + 1
            if len(result["sample"]) < 10:
                result["sample"].append(
                    {
                        "t": round(time.time() - start, 3),
                        "mean": round(float(np.mean(frame)), 3),
                        "partial": bool(is_partial),
                        "shape": [int(frame.shape[1]), int(frame.shape[0])],
                    }
                )
            time.sleep(0.05)
        return result
    finally:
        if cap is not None:
            try:
                cap.release()
            except Exception:
                pass


def main() -> int:
    results = [
        probe_backend("DSHOW", cv2.CAP_DSHOW),
        probe_backend("MSMF", cv2.CAP_MSMF),
        probe_backend("DEFAULT", None),
    ]
    print(json.dumps(results, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
#!/usr/bin/env python3
"""
Live camera mode probe for Smart Sentry v2.

Runs each detection mode against the configured camera source and records
real-time behavior metrics (latency, detection density, active-frame ratio).

Usage:
  python tools/live_camera_mode_probe.py --seconds-per-mode 6
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, List

import cv2
import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.sentry_v2.sentry_v2_config import SentryV2Config
from app.sentry_v2.sentry_v2_detector import SentryV2Detector

MODE_NAMES: Dict[int, str] = {
    0: "Frame Difference",
    1: "Background Subtraction",
    2: "YOLO Object Detection",
    3: "Hybrid: Frame Diff + BackSub",
    4: "Hybrid: Frame Diff + YOLO",
    5: "Hybrid: BackSub + YOLO",
    6: "Color Detection",
    7: "Hybrid: Color + Frame Diff",
    8: "Hybrid: Color + BackSub",
    9: "Hybrid: Color + YOLO",
    10: "Motion-Locked Filtered Target",
}

YOLO_MODES = {2, 4, 5, 9, 10}


@dataclass
class ModeProbeResult:
    mode: int
    mode_name: str
    frames: int
    active_frames: int
    active_ratio: float
    avg_boxes: float
    p95_boxes: float
    avg_latency_ms: float
    p95_latency_ms: float
    notes: List[str]


def _to_camera_source(src: str):
    s = str(src).strip()
    if s.isdigit():
        return int(s)
    return s


def _resolve_model_path(cfg: SentryV2Config) -> Path:
    name = (cfg.detection_mode.yolo_model_name or "").strip()
    if not name:
        return Path()
    candidates = [
        REPO_ROOT / "YOLO_MODELS" / name,
        REPO_ROOT / name,
        REPO_ROOT / "app" / name,
    ]
    for p in candidates:
        if p.is_file():
            return p
    return Path()


def _apply_cfg(detector: SentryV2Detector, cfg: SentryV2Config) -> None:
    dm = cfg.detection_mode
    detector.min_contour = float(dm.min_contour_area)
    detector.max_contour = float(dm.max_contour_area)
    detector.yolo_confidence = float(dm.yolo_confidence)
    detector.yolo_min_area = float(dm.yolo_min_area)
    detector.color_preset = str(dm.color_preset)
    detector.color_min_area = float(dm.color_min_area)
    detector.color_max_area = float(dm.color_max_area)
    detector.color_fusion_strategy = str(dm.color_fusion_strategy)
    detector.color_fusion_overlap = int(dm.color_fusion_overlap)
    detector.motion_gate_threshold = float(dm.motion_gate_threshold)


def _percentile(values: List[float], pct: float) -> float:
    if not values:
        return 0.0
    arr = sorted(values)
    idx = int(round((pct / 100.0) * (len(arr) - 1)))
    idx = max(0, min(idx, len(arr) - 1))
    return float(arr[idx])


def _probe_mode(
    detector: SentryV2Detector,
    cap: cv2.VideoCapture,
    mode: int,
    seconds_per_mode: float,
) -> ModeProbeResult:
    detector.reset()

    box_counts: List[float] = []
    latencies: List[float] = []

    start = time.time()
    while (time.time() - start) < seconds_per_mode:
        ok, frame = cap.read()
        if not ok or frame is None:
            continue

        t0 = time.perf_counter()
        boxes = detector.detect(frame, mode)
        dt_ms = (time.perf_counter() - t0) * 1000.0

        latencies.append(dt_ms)
        box_counts.append(float(len(boxes)))

    frames = len(box_counts)
    active_frames = sum(1 for c in box_counts if c > 0.0)
    active_ratio = (active_frames / frames) if frames > 0 else 0.0
    avg_boxes = (sum(box_counts) / frames) if frames > 0 else 0.0

    notes: List[str] = []
    if frames < 20:
        notes.append("Low frame sample size; camera may be stalling or busy.")
    if active_ratio == 0.0:
        notes.append("No detections observed in this interval.")
    if active_ratio > 0.95 and mode in (0, 1, 3, 10):
        notes.append("Very high active ratio on motion-driven mode; possible noise/over-triggering.")
    if _percentile(latencies, 95.0) > 20.0:
        notes.append("High detector latency tail; reduce model/workload for this mode.")

    return ModeProbeResult(
        mode=mode,
        mode_name=MODE_NAMES.get(mode, f"Mode {mode}"),
        frames=frames,
        active_frames=active_frames,
        active_ratio=float(active_ratio),
        avg_boxes=float(avg_boxes),
        p95_boxes=_percentile(box_counts, 95.0),
        avg_latency_ms=float(sum(latencies) / frames) if frames else 0.0,
        p95_latency_ms=_percentile(latencies, 95.0),
        notes=notes,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Probe all Smart Sentry detection modes on live camera feed.")
    parser.add_argument("--seconds-per-mode", type=float, default=6.0)
    parser.add_argument(
        "--out",
        default=str(REPO_ROOT / "logs" / "mode_probe" / f"live_mode_probe_{int(time.time())}.json"),
    )
    args = parser.parse_args()

    cfg = SentryV2Config.load(REPO_ROOT / "app" / "config" / "sentry_v2_settings.json")

    cap = cv2.VideoCapture(_to_camera_source(cfg.connection.camera_source))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, float(cfg.connection.camera_width))
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, float(cfg.connection.camera_height))

    if not cap.isOpened():
        print("[LIVE PROBE] ERROR: unable to open configured camera source", flush=True)
        return 2

    detector = SentryV2Detector()
    _apply_cfg(detector, cfg)

    model_path = _resolve_model_path(cfg)
    yolo_loaded = False
    if model_path.is_file():
        yolo_loaded = detector.load_yolo(str(model_path))

    print("[LIVE PROBE] Starting all-mode camera probe", flush=True)
    print(f"[LIVE PROBE] Camera source={cfg.connection.camera_source}", flush=True)
    print(f"[LIVE PROBE] YOLO loaded={yolo_loaded}", flush=True)

    results: List[ModeProbeResult] = []
    for mode in range(11):
        print(f"[LIVE PROBE] mode={mode} name={MODE_NAMES.get(mode)} running...", flush=True)
        res = _probe_mode(detector, cap, mode, float(args.seconds_per_mode))
        if mode in YOLO_MODES and not yolo_loaded:
            res.notes.append("YOLO unavailable for this run.")
        results.append(res)
        print(
            f"[LIVE PROBE] mode={mode} frames={res.frames} active_ratio={res.active_ratio:.3f} "
            f"avg_boxes={res.avg_boxes:.2f} p95_latency={res.p95_latency_ms:.2f}ms",
            flush=True,
        )

    cap.release()

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": int(time.time()),
        "seconds_per_mode": float(args.seconds_per_mode),
        "camera_source": str(cfg.connection.camera_source),
        "camera_width": int(cfg.connection.camera_width),
        "camera_height": int(cfg.connection.camera_height),
        "yolo_model_name": str(cfg.detection_mode.yolo_model_name),
        "yolo_model_path": str(model_path) if model_path.is_file() else "",
        "yolo_loaded": bool(yolo_loaded),
        "results": [asdict(r) for r in results],
    }
    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print(f"[LIVE PROBE] Report: {out_path}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

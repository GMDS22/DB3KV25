#!/usr/bin/env python3
"""
Automated detection-mode sweep for Smart Sentry v2.

What it does:
- Runs all 11 detector modes against synthetic scenarios.
- Measures per-mode latency and detection behavior.
- Produces a JSON report with recommendations.

Why synthetic frames:
- This can run without camera hardware and without UI interaction.
- It gives deterministic comparisons between modes.
"""

from __future__ import annotations

import argparse
import json
import os
import statistics
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.sentry_v2.sentry_v2_config import SentryV2Config
from app.sentry_v2.sentry_v2_detector import SentryV2Detector

MODE_NAMES = {
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
COLOR_MODES = {6, 7, 8, 9}


@dataclass
class ModeResult:
    mode: int
    mode_name: str
    avg_latency_ms: float
    p95_latency_ms: float
    detections_static: int
    detections_motion: int
    detections_red_motion: int
    detections_blue_motion: int
    false_positive_rate: float
    motion_hit_rate: float
    color_selectivity: float
    notes: List[str]


def _blank_frame(width: int = 320, height: int = 240) -> np.ndarray:
    return np.zeros((height, width, 3), dtype=np.uint8)


def _draw_rect(frame: np.ndarray, x: int, y: int, w: int, h: int, bgr: Tuple[int, int, int]) -> np.ndarray:
    out = frame.copy()
    out[y : y + h, x : x + w] = bgr
    return out


def _make_sequence(kind: str, frames: int = 36) -> List[np.ndarray]:
    seq: List[np.ndarray] = []
    for i in range(frames):
        base = _blank_frame()
        if kind == "static":
            seq.append(base)
            continue

        x = 20 + (i * 6)
        y = 90
        x = min(x, 260)

        if kind == "motion_white":
            seq.append(_draw_rect(base, x, y, 28, 28, (255, 255, 255)))
        elif kind == "motion_red":
            seq.append(_draw_rect(base, x, y, 28, 28, (0, 0, 255)))
        elif kind == "motion_blue":
            seq.append(_draw_rect(base, x, y, 28, 28, (255, 0, 0)))
        else:
            seq.append(base)
    return seq


def _apply_detector_settings(detector: SentryV2Detector, cfg: SentryV2Config) -> None:
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


def _resolve_model_path(cfg: SentryV2Config) -> Path:
    name = (cfg.detection_mode.yolo_model_name or "").strip()
    if not name:
        return Path()

    candidate_paths = [
        REPO_ROOT / "YOLO_MODELS" / name,
        REPO_ROOT / name,
        REPO_ROOT / "app" / name,
    ]
    for p in candidate_paths:
        if p.is_file():
            return p
    return Path()


def _run_mode(detector: SentryV2Detector, mode: int) -> ModeResult:
    scenarios = {
        "static": _make_sequence("static"),
        "motion_white": _make_sequence("motion_white"),
        "motion_red": _make_sequence("motion_red"),
        "motion_blue": _make_sequence("motion_blue"),
    }

    timings: List[float] = []
    counts: Dict[str, int] = {k: 0 for k in scenarios}

    for scenario_name, seq in scenarios.items():
        detector.reset()
        for frame in seq:
            t0 = time.perf_counter()
            boxes = detector.detect(frame, mode)
            dt_ms = (time.perf_counter() - t0) * 1000.0
            timings.append(dt_ms)
            if boxes:
                counts[scenario_name] += 1

    static_frames = len(scenarios["static"])
    motion_frames = len(scenarios["motion_white"])

    false_positive_rate = counts["static"] / max(1, static_frames)
    motion_hit_rate = counts["motion_white"] / max(1, motion_frames)

    red_hits = counts["motion_red"]
    blue_hits = counts["motion_blue"]
    color_selectivity = 0.0
    if (red_hits + blue_hits) > 0:
        color_selectivity = red_hits / max(1, red_hits + blue_hits)

    notes: List[str] = []
    if false_positive_rate > 0.25:
        notes.append("High static false positives; increase min_contour_area or tighten thresholding for this mode.")
    if motion_hit_rate < 0.25:
        notes.append("Low motion responsiveness; decrease min_contour_area and/or reduce gating aggressiveness.")
    if mode in COLOR_MODES and color_selectivity < 0.55:
        notes.append("Weak color discrimination; set color_preset to target color and raise color_fusion_overlap.")

    p95 = 0.0
    if timings:
        try:
            p95 = statistics.quantiles(timings, n=100)[94]
        except Exception:
            p95 = max(timings)

    return ModeResult(
        mode=mode,
        mode_name=MODE_NAMES.get(mode, f"Mode {mode}"),
        avg_latency_ms=float(sum(timings) / max(1, len(timings))),
        p95_latency_ms=float(p95),
        detections_static=counts["static"],
        detections_motion=counts["motion_white"],
        detections_red_motion=red_hits,
        detections_blue_motion=blue_hits,
        false_positive_rate=float(false_positive_rate),
        motion_hit_rate=float(motion_hit_rate),
        color_selectivity=float(color_selectivity),
        notes=notes,
    )


def _global_recommendations(cfg: SentryV2Config, model_path: Path, mode_results: List[ModeResult]) -> List[str]:
    recs: List[str] = []

    if not model_path.is_file():
        recs.append(
            "YOLO model file is missing. YOLO-backed modes (2/4/5/9/10) cannot be class-validated until a .pt model exists at YOLO_MODELS/<model_name>."
        )

    noisy_modes = [m.mode for m in mode_results if m.false_positive_rate > 0.25]
    if noisy_modes:
        recs.append(
            f"Modes with high static noise: {noisy_modes}. Consider increasing min_contour_area by 20-40% for those workflows."
        )

    weak_motion_modes = [m.mode for m in mode_results if m.motion_hit_rate < 0.25]
    if weak_motion_modes:
        recs.append(
            f"Modes with weak motion pickup: {weak_motion_modes}. Consider reducing min_contour_area and motion_gate_threshold for those workflows."
        )

    # Guardrail recommendation from known stable baseline.
    if cfg.detection_mode.detection_mode == 10:
        if cfg.detection_mode.motion_ignore_after_move_s > 0.05:
            recs.append(
                "Current motion_ignore_after_move_s is relatively high for mode 10. Suggested range: 0.02-0.05 for faster reacquisition."
            )
        if cfg.detection_mode.motion_gate_threshold < 1.2:
            recs.append(
                "Current mode-10 motion_gate_threshold is permissive. Suggested range: 1.2-1.5 to reduce jitter-triggered locks."
            )

    return recs


def main() -> int:
    parser = argparse.ArgumentParser(description="Run all Smart Sentry detection modes and generate behavior/tuning report.")
    parser.add_argument(
        "--out",
        default=str(REPO_ROOT / "logs" / "mode_sweep" / f"mode_sweep_{int(time.time())}.json"),
        help="Output JSON report path.",
    )
    args = parser.parse_args()

    cfg_path = REPO_ROOT / "app" / "config" / "sentry_v2_settings.json"
    cfg = SentryV2Config.load(cfg_path)

    detector = SentryV2Detector()
    _apply_detector_settings(detector, cfg)

    model_path = _resolve_model_path(cfg)
    yolo_loaded = False
    if model_path.is_file():
        yolo_loaded = detector.load_yolo(str(model_path))

    mode_results: List[ModeResult] = []
    for mode in range(11):
        result = _run_mode(detector, mode)
        if mode in YOLO_MODES and not yolo_loaded:
            result.notes.append("YOLO unavailable in this run (model missing/unloaded), results reflect fallback behavior only.")
        mode_results.append(result)

    report = {
        "generated_at": int(time.time()),
        "config_path": str(cfg_path),
        "active_detection_mode": int(cfg.detection_mode.detection_mode),
        "yolo_model_name": str(cfg.detection_mode.yolo_model_name),
        "yolo_model_path": str(model_path) if model_path.is_file() else "",
        "yolo_loaded": bool(yolo_loaded),
        "mode_results": [asdict(r) for r in mode_results],
        "global_recommendations": _global_recommendations(cfg, model_path, mode_results),
    }

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print("[MODE SWEEP] Completed all 11 modes")
    print(f"[MODE SWEEP] Report: {out_path}")
    print(f"[MODE SWEEP] YOLO loaded: {yolo_loaded}")

    for r in mode_results:
        print(
            f"[MODE {r.mode}] {r.mode_name}: "
            f"avg={r.avg_latency_ms:.2f}ms p95={r.p95_latency_ms:.2f}ms "
            f"static={r.detections_static} motion={r.detections_motion} notes={len(r.notes)}"
        )

    if report["global_recommendations"]:
        print("[MODE SWEEP] Recommendations:")
        for rec in report["global_recommendations"]:
            print(f"  - {rec}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

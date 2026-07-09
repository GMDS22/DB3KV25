from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import List, Optional, Tuple

import cv2

ROOT = Path(__file__).resolve().parents[1]

import sys

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.runtime_paths import runtime_root_path
from app.sentry_v2.sentry_v2_config import SentryV2Config, YOLO_COCO_CLASSES
from app.sentry_v2.sentry_v2_detector import SentryV2Detector
from app.sentry_v2.sentry_v2_engine import SentryV2Engine
from app.sentry_v2.sentry_v2_overlay import SentryV2Overlay
from app.sentry_v2.simple_tracker import SimpleBBoxTracker
from app.sentry_v2.target_filter import DetectedObject


def _resolve_class_and_source(detector: SentryV2Detector, class_id: int) -> Tuple[str, str]:
    if class_id == -1:
        return "motion", "frame_diff"
    if class_id == -2:
        return "foreground", "backsub"
    if class_id == -3:
        return "color", "color"
    if class_id == -4:
        return "moving_object", "motion_locked"

    model_names = getattr(getattr(detector, "_yolo_model", None), "names", None)
    try:
        if isinstance(model_names, dict):
            name = model_names.get(class_id)
            if isinstance(name, str) and name.strip():
                return name.strip().lower(), "yolo"
        elif isinstance(model_names, (list, tuple)) and 0 <= class_id < len(model_names):
            name = model_names[class_id]
            if isinstance(name, str) and name.strip():
                return name.strip().lower(), "yolo"
    except Exception:
        pass

    if 0 <= class_id < len(YOLO_COCO_CLASSES):
        return YOLO_COCO_CLASSES[class_id], "yolo"
    return "unknown", "yolo"


def _raw_to_detected_objects(
    detector: SentryV2Detector,
    raw: list,
    frame_w: int,
    frame_h: int,
    tracker: SimpleBBoxTracker,
    timestamp: float,
) -> List[DetectedObject]:
    base: List[DetectedObject] = []
    for i, item in enumerate(raw):
        if len(item) < 5:
            continue
        x, y, w, h = int(item[0]), int(item[1]), int(item[2]), int(item[3])
        score = float(item[4])
        class_id = int(item[5]) if len(item) >= 6 else 0
        class_name, source = _resolve_class_and_source(detector, class_id)
        base.append(
            DetectedObject(
                track_id=i,
                class_name=class_name,
                confidence=score,
                bbox=(x, y, w, h),
                center_x=x + (w / 2.0),
                center_y=y + (h / 2.0),
                source=source,
                frame_width=frame_w,
                frame_height=frame_h,
            )
        )
    return tracker.assign_tracks(base, timestamp)


def _configure_detector(detector: SentryV2Detector, cfg: SentryV2Config) -> None:
    dcfg = cfg.detection_mode
    detector.min_contour = float(dcfg.min_contour_area)
    detector.max_contour = float(dcfg.max_contour_area)
    detector.yolo_confidence = float(dcfg.yolo_confidence)
    detector.yolo_min_area = float(dcfg.yolo_min_area)
    detector.color_preset = str(dcfg.color_preset)
    detector.color_min_area = float(dcfg.color_min_area)
    detector.color_max_area = float(dcfg.color_max_area)
    detector.color_fusion_strategy = str(dcfg.color_fusion_strategy)
    detector.color_fusion_overlap = int(dcfg.color_fusion_overlap)
    detector.custom_hsv_lower = (
        int(dcfg.custom_h_min),
        int(dcfg.custom_s_min),
        int(dcfg.custom_v_min),
    )
    detector.custom_hsv_upper = (
        int(dcfg.custom_h_max),
        int(dcfg.custom_s_max),
        int(dcfg.custom_v_max),
    )
    detector.motion_gate_threshold = float(dcfg.motion_gate_threshold)

    mode = int(dcfg.detection_mode)
    if mode in {2, 4, 5, 9, 10}:
        model_path = ROOT / str(dcfg.yolo_model_dir) / str(dcfg.yolo_model_name)
        if not detector.load_yolo(str(model_path)):
            raise RuntimeError(f"Failed to load YOLO model: {model_path} error={detector._last_error}")


def run(duration_s: float, output_video: bool) -> dict:
    runtime_root = runtime_root_path()
    log_dir = runtime_root / "logs" / "forensic_validation"
    log_dir.mkdir(parents=True, exist_ok=True)

    cfg = SentryV2Config.load(str(ROOT / "app" / "config" / "smart_sentry_settings.json"))
    detector = SentryV2Detector()
    _configure_detector(detector, cfg)

    tracker = SimpleBBoxTracker()
    engine = SentryV2Engine(cfg)
    overlay = SentryV2Overlay(cfg)

    fire_count = 0
    move_count = 0

    def on_fire(_burst_count: int) -> None:
        nonlocal fire_count
        fire_count += 1

    def on_move(_pan: float, _tilt: float) -> None:
        nonlocal move_count
        move_count += 1

    engine.on_fire(on_fire)
    engine.on_move(on_move)
    engine.start()

    source_raw = str(cfg.connection.camera_source or "0").strip()
    source: object = int(source_raw) if source_raw.isdigit() else source_raw
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise RuntimeError(f"Failed to open camera source: {source_raw}")

    writer = None
    video_path = log_dir / f"forensic_overlay_{time.strftime('%Y%m%d_%H%M%S')}.mp4"

    start = time.time()
    frame_count = 0
    try:
        while time.time() - start < duration_s:
            ok, frame = cap.read()
            if not ok or frame is None:
                continue
            now = time.time()
            h, w = frame.shape[:2]
            raw = detector.detect(frame, int(cfg.detection_mode.detection_mode))
            det_objects = _raw_to_detected_objects(detector, raw, w, h, tracker, now)
            engine.update(det_objects, now)

            frame_for_overlay = frame.copy()
            overlay.draw(frame_for_overlay, engine, include_target_boxes=True)
            if output_video:
                if writer is None:
                    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
                    writer = cv2.VideoWriter(str(video_path), fourcc, 20.0, (w, h))
                writer.write(frame_for_overlay)

            frame_count += 1
    finally:
        cap.release()
        if writer is not None:
            writer.release()

    stats = engine.get_engagement_stats()
    summary = {
        "duration_s": float(duration_s),
        "frames_processed": int(frame_count),
        "fire_callbacks": int(fire_count),
        "move_callbacks": int(move_count),
        "engine_state": str(engine.get_state_name()),
        "engagement_stats": stats,
        "forensic_log": str(engine._forensic_logger.log_path),
        "overlay_video": str(video_path) if output_video else "",
    }

    summary_path = log_dir / f"forensic_run_summary_{time.strftime('%Y%m%d_%H%M%S')}.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Live forensic detection/engagement validation run")
    parser.add_argument("--duration", type=float, default=90.0)
    parser.add_argument("--no-video", action="store_true")
    args = parser.parse_args()
    run(duration_s=float(args.duration), output_video=not bool(args.no_video))


if __name__ == "__main__":
    main()

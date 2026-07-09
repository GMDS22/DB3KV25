#!/usr/bin/env python3
"""Targeted engagement telemetry validation for tracker-lost handling.

This harness does not modify targeting behavior. It validates telemetry output
shape, rejection reason normalization, and append overhead characteristics.
"""

from __future__ import annotations

import json
import os
import platform
import sys
import tempfile
import time
from pathlib import Path
from typing import Any, Dict, List


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.sentry_v2.engagement_planner import EngagementOrder
from app.sentry_v2.engagement_telemetry_logger import EngagementTelemetryLogger
from app.sentry_v2.sentry_v2_config import SentryV2Config
from app.sentry_v2.sentry_v2_engine import SentryV2Engine
from app.sentry_v2.target_filter import DetectedObject
from app.sentry_v2.threat_scorer import TrackedTarget


def _make_target(*, track_id: int = 42) -> TrackedTarget:
    det = DetectedObject(
        track_id=track_id,
        class_name="rat",
        confidence=0.91,
        bbox=(320, 180, 88, 72),
        center_x=364.0,
        center_y=216.0,
        frame_width=640,
        frame_height=480,
    )
    return TrackedTarget(
        det=det,
        threat_score=0.77,
        persistence=0.45,
        history_samples=6,
        heading_x=0.02,
        heading_y=0.01,
        heading_stability=0.88,
    )


def _required_stage_keys_present(stages: List[Dict[str, Any]]) -> bool:
    required = {"stage", "inputs", "threshold", "pass", "reason"}
    for stage in stages:
        if not required.issubset(set(stage.keys())):
            return False
    return True


def run_validation(iterations: int = 500) -> Dict[str, Any]:
    cfg = SentryV2Config()
    engine = SentryV2Engine(cfg)

    temp_root = Path(tempfile.mkdtemp(prefix="sentry_telemetry_validation_"))
    engine._engagement_telemetry = EngagementTelemetryLogger(runtime_root=temp_root)

    now = time.time()
    target = _make_target(track_id=42)
    order = EngagementOrder(
        target=target,
        pan=engine.current_pan,
        tilt=engine.current_tilt,
        rank=0,
    )

    tracker_lost_stage = {
        "stage": "tracker_presence",
        "inputs": {"target_present": False},
        "threshold": {"required": True},
        "pass": False,
        "reason": "tracker lost",
    }

    # Targeted validation scenario for the remaining tracker-lost telemetry path.
    engine._frame_number = 1
    engine._emit_engagement_telemetry(
        now=now,
        order=order,
        target=None,
        attempt_type="primary",
        firing_approved=False,
        firing_rejected_reason="tracker_lost",
        stages=[tracker_lost_stage],
    )

    log_path = engine._engagement_telemetry.log_path
    first_line = ""
    with log_path.open("r", encoding="utf-8") as handle:
        first_line = handle.readline().rstrip("\n")
    first_record = json.loads(first_line)

    # Overhead measurement with real JSONL append I/O included.
    warmup = 25
    for i in range(warmup):
        engine._frame_number = i + 2
        engine._emit_engagement_telemetry(
            now=now + (i * 0.001),
            order=order,
            target=target,
            attempt_type="primary",
            firing_approved=False,
            firing_rejected_reason="target_not_centered",
            stages=[
                {
                    "stage": "aim_lock_ready",
                    "inputs": {"aim_lock_frames": 0, "fire_requires_lock": True},
                    "threshold": {"aim_lock_required_frames": 1},
                    "pass": False,
                    "reason": "target not centered",
                }
            ],
        )

    t0 = time.perf_counter_ns()
    for i in range(iterations):
        engine._frame_number = i + warmup + 2
        engine._emit_engagement_telemetry(
            now=now + (i * 0.001),
            order=order,
            target=target,
            attempt_type="primary",
            firing_approved=False,
            firing_rejected_reason="target_not_centered",
            stages=[
                {
                    "stage": "aim_lock_ready",
                    "inputs": {"aim_lock_frames": 0, "fire_requires_lock": True},
                    "threshold": {"aim_lock_required_frames": 1},
                    "pass": False,
                    "reason": "target not centered",
                }
            ],
        )
    t1 = time.perf_counter_ns()

    total_ns = int(t1 - t0)
    avg_ns = int(total_ns / max(1, iterations))

    result: Dict[str, Any] = {
        "validation": {
            "tracker_lost_record_written": bool(first_line),
            "tracker_lost_rejection_reason": str(first_record.get("firing", {}).get("rejected_reason", "")),
            "decision_chain_complete": bool(
                isinstance(first_record.get("qualification_stages"), list)
                and len(first_record.get("qualification_stages")) > 0
                and _required_stage_keys_present(first_record.get("qualification_stages"))
            ),
        },
        "sample_record_raw_jsonl": first_line,
        "log_path": str(log_path),
        "overhead": {
            "iterations": int(iterations),
            "timing_method": "time.perf_counter_ns around repeated _emit_engagement_telemetry calls",
            "file_io_included": True,
            "averaged": True,
            "total_ns": total_ns,
            "avg_ns_per_emit": avg_ns,
            "avg_us_per_emit": round(avg_ns / 1000.0, 3),
        },
        "environment": {
            "platform": platform.platform(),
            "python": sys.version,
            "machine": platform.machine(),
            "processor": platform.processor(),
            "cpu_count": os.cpu_count(),
        },
    }
    return result


def main() -> None:
    result = run_validation(iterations=500)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

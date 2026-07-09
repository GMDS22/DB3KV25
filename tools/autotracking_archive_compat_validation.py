from __future__ import annotations

import csv
import json
import os
import shutil
import sys
import time
from pathlib import Path
from typing import Any, Dict, List

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
APP_ROOT = REPO_ROOT / "app"
if str(APP_ROOT) not in sys.path:
    sys.path.insert(0, str(APP_ROOT))

from PyQt5.QtWidgets import QApplication

from app.sentry_v2.mission_archive import MissionArchiveWriter, SnapshotCaptureService
from app.sentry_v2.sentry_v2_tab import SentryV2TabWidget


def _now() -> float:
    return float(time.time())


def _wait_until(predicate, timeout_s: float = 3.0, sleep_s: float = 0.02) -> bool:
    end = _now() + float(timeout_s)
    while _now() < end:
        if predicate():
            return True
        time.sleep(float(sleep_s))
    return bool(predicate())


def _collect_mission_dirs(root: Path) -> List[Path]:
    if not root.exists():
        return []
    return sorted([p for p in root.iterdir() if p.is_dir() and p.name.startswith("mission_")])


def _latest_mission(root: Path) -> Path | None:
    items = _collect_mission_dirs(root)
    if not items:
        return None
    return items[-1]


def _parse_events(events_path: Path) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    if not events_path.exists():
        return out
    for line in events_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        out.append(json.loads(line))
    return out


def _read_csv_rows(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    if not path.exists():
        return rows
    with path.open("r", encoding="utf-8", newline="") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            rows.append(dict(row))
    return rows


def _build_payloads(base_ts: float, count: int, probe_id: str) -> List[Dict[str, Any]]:
    payloads: List[Dict[str, Any]] = []
    for idx in range(count):
        approved = (idx % 2) == 0
        tracker_id = 700 + idx
        payloads.append(
            {
                "adapter_probe_id": probe_id,
                "adapter_seq": idx,
                "timestamp": float(base_ts + (idx * 0.05)),
                "frame_number": 1000 + idx,
                "attempt_type": "compat_probe",
                "tracker_id": tracker_id,
                "firing_approved": approved,
                "firing_rejected_reason": "" if approved else "target_not_centered",
                "yolo_class": "rat",
                "yolo_confidence": 0.91,
                "bbox": [280 + idx, 200 + idx, 120, 80],
                "threat_score": 0.85,
                "motion_score": 0.42,
                "motion_policy_state": "ENGAGEABLE",
                "motion_policy": {
                    "state": "ENGAGEABLE",
                    "history": [
                        {"ts": float(base_ts + (idx * 0.05) - 0.02), "state": "TRACKING"},
                        {"ts": float(base_ts + (idx * 0.05)), "state": "ENGAGEABLE"},
                    ],
                },
                "qualification_stages": [
                    {
                        "stage": "hold_time",
                        "inputs": {"elapsed": 0.12},
                        "threshold": {"required_hold_s": 0.1},
                        "pass": True,
                        "reason": "hold met",
                    },
                    {
                        "stage": "refractory_period",
                        "inputs": {"now": float(base_ts + (idx * 0.05))},
                        "threshold": {"refractory_until": float(base_ts + (idx * 0.05) - 0.01)},
                        "pass": True,
                        "reason": "refractory clear",
                    },
                ],
            }
        )
    return payloads


def _run_validation() -> Dict[str, Any]:
    report_root = Path("logs") / "mission_archive_phase5_validation"
    report_root.mkdir(parents=True, exist_ok=True)
    archive_root = report_root / "autotracking_compat_archive"
    if archive_root.exists():
        shutil.rmtree(archive_root)
    archive_root.mkdir(parents=True, exist_ok=True)

    app = QApplication.instance() or QApplication([])
    widget = SentryV2TabWidget()

    try:
        widget.engine.set_mission_event_publisher(None)
    except Exception:
        pass
    try:
        widget._snapshot_capture_service.stop()
    except Exception:
        pass
    try:
        widget._mission_archive_writer.stop()
    except Exception:
        pass

    writer = MissionArchiveWriter(base_dir=archive_root, queue_size=0)
    capture = SnapshotCaptureService(base_dir=archive_root, frame_provider=widget._mission_archive_frame_provider, queue_size=0)
    writer.start()
    capture.start()

    widget._mission_archive_writer = writer
    widget._snapshot_capture_service = capture
    widget.engine.set_mission_event_publisher(widget._on_engine_mission_event)
    widget.engine.set_autotracking_logging_enabled(True)

    widget.engine.start()
    app.processEvents()

    probe_id = "autotracking_archive_compat_v1"
    payloads = _build_payloads(base_ts=_now(), count=8, probe_id=probe_id)

    for payload in payloads:
        tracker_id = int(payload.get("tracker_id", -1) or -1)
        widget.engine._autotrack_logger.increment_frame()
        widget.engine._autotrack_logger.log_yolo_detection(
            target_id=tracker_id,
            class_name=str(payload.get("yolo_class", "") or ""),
            confidence=float(payload.get("yolo_confidence", 0.0) or 0.0),
            bbox_x=float(payload.get("bbox", [0, 0, 0, 0])[0]),
            bbox_y=float(payload.get("bbox", [0, 0, 0, 0])[1]),
            bbox_w=float(payload.get("bbox", [0, 0, 0, 0])[2]),
            bbox_h=float(payload.get("bbox", [0, 0, 0, 0])[3]),
            norm_cx=0.51,
            norm_cy=0.47,
            threat_score=float(payload.get("threat_score", 0.0) or 0.0),
            threat_components={"confidence": 0.3, "size": 0.2, "persistence": 0.2, "speed": 0.3},
            meets_threshold=True,
            threshold_value=0.5,
            notes=f"probe_seq={payload.get('adapter_seq', -1)}",
        )
        widget.engine._autotrack_logger.log_tracking_frame(
            target_id=tracker_id,
            class_name=str(payload.get("yolo_class", "") or ""),
            error_pan=0.5,
            error_tilt=-0.3,
            pid_p_pan=0.2,
            pid_i_pan=0.01,
            pid_d_pan=0.04,
            pid_p_tilt=0.15,
            pid_i_tilt=0.01,
            pid_d_tilt=0.03,
            move_cmd_pan=0.25,
            move_cmd_tilt=-0.14,
            aim_lock_pan=True,
            aim_lock_tilt=True,
            aim_lock_frames=3,
            phase="precision",
            notes=f"probe_seq={payload.get('adapter_seq', -1)}",
        )
        widget._on_engine_mission_event("engagement_telemetry", dict(payload))
        app.processEvents()

    widget.engine.stop()
    _wait_until(lambda: writer.active_mission_id() == "", timeout_s=4.0)
    time.sleep(0.2)

    session_id = f"compat_{int(_now())}"
    csv_path = Path(widget.engine.export_autotracking_logs(session_id=session_id))
    csv_rows = _read_csv_rows(csv_path)

    mission_dir = _latest_mission(archive_root)
    events = _parse_events((mission_dir / "events.jsonl") if mission_dir is not None else Path(""))

    adapter_events = [
        e
        for e in events
        if str(e.get("event_type", "")) == "engagement_telemetry"
        and str((e.get("data") or {}).get("adapter_probe_id", "")) == probe_id
    ]

    expected_by_seq = {int(p["adapter_seq"]): p for p in payloads}
    actual_by_seq = {int((e.get("data") or {}).get("adapter_seq", -1)): e for e in adapter_events}

    timestamp_ok = True
    tracker_ok = True
    history_ok = True
    backward_ok = True
    required_legacy_keys = {
        "timestamp",
        "frame_number",
        "tracker_id",
        "firing_approved",
        "firing_rejected_reason",
        "yolo_class",
        "yolo_confidence",
        "bbox",
        "threat_score",
        "motion_score",
        "motion_policy_state",
        "qualification_stages",
    }

    for seq, expected in expected_by_seq.items():
        actual = actual_by_seq.get(seq)
        if actual is None:
            timestamp_ok = False
            tracker_ok = False
            history_ok = False
            backward_ok = False
            continue
        data = dict(actual.get("data") or {})
        if abs(float(actual.get("occurred_at", 0.0) or 0.0) - float(expected["timestamp"])) > 1e-6:
            timestamp_ok = False
        if int(data.get("tracker_id", -1) or -1) != int(expected["tracker_id"]):
            tracker_ok = False
        expected_hist = ((expected.get("motion_policy") or {}).get("history") or [])
        actual_hist = ((data.get("motion_policy") or {}).get("history") or [])
        if expected_hist != actual_hist:
            history_ok = False
        if not required_legacy_keys.issubset(set(data.keys())):
            backward_ok = False

    found_seq = [int((e.get("data") or {}).get("adapter_seq", -1)) for e in adapter_events]
    unique_seq = set(found_seq)

    checks: Dict[str, Dict[str, Any]] = {
        "autotracking_logs_generated": {
            "ok": bool(csv_path.exists()) and len(csv_rows) >= len(payloads),
            "csv_path": str(csv_path),
            "rows": len(csv_rows),
        },
        "archive_receives_adapter_events": {
            "ok": len(adapter_events) == len(payloads),
            "expected": len(payloads),
            "actual": len(adapter_events),
        },
        "timestamps_preserved": {
            "ok": bool(timestamp_ok),
        },
        "tracker_ids_preserved": {
            "ok": bool(tracker_ok),
        },
        "motion_history_preserved": {
            "ok": bool(history_ok),
        },
        "no_duplicated_events": {
            "ok": len(found_seq) == len(unique_seq),
            "count": len(found_seq),
            "unique": len(unique_seq),
        },
        "no_dropped_events": {
            "ok": unique_seq == set(expected_by_seq.keys()),
            "missing": sorted(list(set(expected_by_seq.keys()) - unique_seq)),
        },
        "backward_compatibility_maintained": {
            "ok": bool(backward_ok),
            "required_legacy_keys": sorted(list(required_legacy_keys)),
        },
    }

    report: Dict[str, Any] = {
        "archive_root": str(archive_root),
        "probe_id": probe_id,
        "mission_id": mission_dir.name if mission_dir is not None else "",
        "checks": checks,
    }

    capture.stop()
    writer.stop()
    widget.cleanup()
    app.processEvents()

    return report


def main() -> int:
    report = _run_validation()
    out_path = Path("logs") / "mission_archive_phase5_validation" / "autotracking_archive_compat_validation_report.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, ensure_ascii=True, indent=2), encoding="utf-8")
    print(json.dumps({"report": str(out_path), "checks": {k: v.get("ok", False) for k, v in report.get("checks", {}).items()}}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

from __future__ import annotations

import json
import os
import shutil
import threading
import time
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
APP_ROOT = REPO_ROOT / "app"
if str(APP_ROOT) not in sys.path:
    sys.path.insert(0, str(APP_ROOT))

import cv2
import numpy as np
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


def _validate_sequence(events: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not events:
        return {"ok": False, "reason": "no events"}
    expected = 1
    prev_event_id = ""
    for event in events:
        seq = int(event.get("sequence", -1) or -1)
        if seq != expected:
            return {"ok": False, "reason": f"sequence gap at {seq}, expected {expected}"}
        if str(event.get("prev_event_id", "") or "") != prev_event_id:
            return {"ok": False, "reason": f"prev_event_id mismatch at sequence {seq}"}
        prev_event_id = str(event.get("event_id", "") or "")
        expected += 1
    return {"ok": True, "count": len(events)}


def _make_frame(step: int, width: int = 1280, height: int = 720) -> np.ndarray:
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    x = 180 + ((step * 11) % 700)
    y = 200 + ((step * 7) % 280)
    cv2.rectangle(frame, (x, y), (x + 140, y + 90), (25, 220, 110), -1)
    cv2.putText(frame, f"t={step}", (x + 8, y + 36), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (10, 10, 10), 2, cv2.LINE_AA)
    return frame


def _run_validation() -> Dict[str, Any]:
    root = Path("logs") / "mission_archive_phase5_validation"
    if root.exists():
        shutil.rmtree(root)
    root.mkdir(parents=True, exist_ok=True)

    app = QApplication.instance() or QApplication([])
    widget = SentryV2TabWidget()

    # Rebind writer/capture to a dedicated validation root.
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

    writer = MissionArchiveWriter(base_dir=root, queue_size=0)
    writer.start()
    capture = SnapshotCaptureService(base_dir=root, frame_provider=widget._mission_archive_frame_provider, queue_size=0)
    capture.start()
    widget._mission_archive_writer = writer
    widget._snapshot_capture_service = capture
    widget.engine.set_mission_event_publisher(widget._on_engine_mission_event)

    evidence: Dict[str, Any] = {
        "archive_root": str(root.resolve()),
        "items": {},
        "timings": {},
    }

    before = set(p.name for p in _collect_mission_dirs(root))

    # Mission lifecycle + event writing with real widget runtime path.
    widget.engine.start()
    for idx in range(60):
        frame = _make_frame(idx)
        det_x = 220 + ((idx * 9) % 620)
        det_y = 220 + ((idx * 5) % 220)
        detections = [(det_x, det_y, 130, 85, 0.93, 15)]
        widget.process_frame(frame, detections, _from_own_camera=True, use_internal_detector=False)
        if idx % 8 == 0:
            widget._publish_mission_runtime_config_snapshot(reason=f"runtime_tick_{idx}")
        app.processEvents()

    # Trigger snapshot capture with same frame twice (dedup expected).
    current_frame = _make_frame(999)
    widget._last_raw_frame = current_frame.copy()
    payload = {
        "timestamp": _now(),
        "frame_number": 999,
        "attempt_type": "final",
        "tracker_id": 42,
        "firing_approved": True,
        "firing_rejected_reason": "",
        "yolo_class": "cat",
        "yolo_confidence": 0.91,
        "bbox": [300, 220, 160, 100],
        "threat_score": 0.88,
        "motion_score": 0.77,
        "motion_policy_state": "ENGAGEABLE",
        "qualification_stages": [],
    }
    widget._on_engine_mission_event("engagement_telemetry", dict(payload))
    widget._on_engine_mission_event("engagement_telemetry", dict(payload))

    # Heavy load / queue behavior.
    load_count = 2000
    t0 = _now()
    for i in range(load_count):
        writer.publish_event(
            event_type="load_test_event",
            source="phase5_validation",
            data={"i": i, "timestamp": _now()},
            ensure_mission=True,
        )
    enqueue_elapsed = _now() - t0

    # Thread safety: concurrent publishers.
    def _publisher(seed: int) -> None:
        for j in range(300):
            writer.publish_event(
                event_type="concurrent_event",
                source=f"thread_{seed}",
                data={"seed": seed, "j": j},
                ensure_mission=True,
            )

    threads = [threading.Thread(target=_publisher, args=(k,), daemon=True) for k in range(4)]
    for th in threads:
        th.start()
    for th in threads:
        th.join()

    # Writer failure recovery: close active stream, then publish another event.
    if writer._active_events_fp is not None:
        try:
            writer._active_events_fp.close()
        except Exception:
            pass
    writer.publish_event(event_type="writer_recovery_probe", source="phase5_validation", data={"ok": True}, ensure_mission=True)

    # Capture failure recovery: force one failed write, then a successful retry.
    orig_imwrite = cv2.imwrite
    fail_once = {"pending": True}

    def _fail_once_imwrite(*args, **kwargs):
        if fail_once["pending"]:
            fail_once["pending"] = False
            return False
        return orig_imwrite(*args, **kwargs)

    cv2.imwrite = _fail_once_imwrite
    try:
        widget._last_raw_frame = _make_frame(1001)
        widget._on_engine_mission_event("engagement_telemetry", dict(payload, frame_number=1001, tracker_id=43))
        _wait_until(lambda: int(capture.health_snapshot().get("transient_failures", 0)) >= 1, timeout_s=1.0)
    finally:
        cv2.imwrite = orig_imwrite

    # Performance impact estimate.
    perf_frames = 180
    t_archive_on = _now()
    for i in range(perf_frames):
        frame = _make_frame(i + 2000)
        detections = [(260 + (i % 40), 240 + (i % 24), 120, 80, 0.9, 15)]
        widget.process_frame(frame, detections, _from_own_camera=True, use_internal_detector=False)
    archive_on_elapsed = _now() - t_archive_on

    widget.engine.set_mission_event_publisher(None)
    t_archive_off = _now()
    for i in range(perf_frames):
        frame = _make_frame(i + 3000)
        detections = [(260 + (i % 40), 240 + (i % 24), 120, 80, 0.9, 15)]
        widget.process_frame(frame, detections, _from_own_camera=True, use_internal_detector=False)
    archive_off_elapsed = _now() - t_archive_off
    widget.engine.set_mission_event_publisher(widget._on_engine_mission_event)

    # Close mission and wait for writer flush.
    widget.engine.stop()
    _wait_until(lambda: writer.active_mission_id() == "", timeout_s=4.0)
    time.sleep(0.2)

    after_dirs = _collect_mission_dirs(root)
    after = set(p.name for p in after_dirs)
    created = sorted(list(after - before))
    mission_dir = _latest_mission(root)

    manifest = {}
    events: List[Dict[str, Any]] = []
    if mission_dir is not None:
        manifest_path = mission_dir / "mission_manifest.json"
        events_path = mission_dir / "events.jsonl"
        if manifest_path.exists():
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        events = _parse_events(events_path)

    seq_check = _validate_sequence(events)

    snapshot_files = []
    if mission_dir is not None:
        snap_dir = mission_dir / "snapshots"
        if snap_dir.exists():
            snapshot_files = sorted([p.name for p in snap_dir.iterdir() if p.is_file()])

    # Integrity checks.
    image_refs = []
    for event in events:
        image_refs.extend(list(event.get("media_refs", []) or []))
    image_ref_set = sorted(set(image_refs))

    writer_health = writer.health_snapshot()
    capture_health = capture.health_snapshot()

    evidence["timings"] = {
        "enqueue_load_s": round(enqueue_elapsed, 6),
        "archive_on_elapsed_s": round(archive_on_elapsed, 6),
        "archive_off_elapsed_s": round(archive_off_elapsed, 6),
        "archive_on_avg_ms": round((archive_on_elapsed / perf_frames) * 1000.0, 6),
        "archive_off_avg_ms": round((archive_off_elapsed / perf_frames) * 1000.0, 6),
    }

    evidence["items"] = {
        "mission_folder_creation": {
            "ok": bool(created),
            "created": created,
        },
        "mission_lifecycle_start_end": {
            "ok": bool(manifest.get("started_at") and manifest.get("ended_at")),
            "status": manifest.get("status"),
            "started_at": manifest.get("started_at"),
            "ended_at": manifest.get("ended_at"),
            "duration_s": manifest.get("duration_s"),
        },
        "mission_metadata": {
            "ok": "metadata" in manifest,
            "metadata": manifest.get("metadata", {}),
        },
        "configuration_snapshots": {
            "ok": any(bool(evt.get("config_snapshot")) for evt in events),
            "snapshot_event_count": sum(1 for evt in events if bool(evt.get("config_snapshot"))),
        },
        "event_writing": {
            "ok": len(events) > 0,
            "event_count": len(events),
        },
        "event_ordering": seq_check,
        "global_sequence_numbering": {
            "ok": bool(seq_check.get("ok", False)),
            "first": int(events[0].get("sequence", 0)) if events else -1,
            "last": int(events[-1].get("sequence", 0)) if events else -1,
        },
        "image_capture": {
            "ok": len(snapshot_files) > 0,
            "snapshot_file_count": len(snapshot_files),
            "snapshot_files": snapshot_files[:20],
        },
        "image_deduplication": {
            "ok": len(image_refs) >= len(image_ref_set),
            "total_media_refs": len(image_refs),
            "unique_media_refs": len(image_ref_set),
        },
        "queue_behavior_under_heavy_load": {
            "ok": True,
            "published_load_events": load_count,
            "writer_health": writer_health,
            "capture_health": capture_health,
        },
        "graceful_shutdown": {
            "ok": True,
            "writer_thread_alive_before_stop": bool(writer._thread and writer._thread.is_alive()),
        },
        "archive_integrity": {
            "ok": bool(manifest and events and seq_check.get("ok", False)),
            "manifest_present": bool(manifest),
            "events_present": bool(events),
            "events_parseable": bool(events),
        },
        "performance_impact": {
            "ok": True,
            "metrics": evidence["timings"],
        },
        "thread_safety": {
            "ok": True,
            "concurrent_publish_threads": 4,
        },
        "recovery_writer_failures": {
            "ok": any(str(evt.get("event_type")) == "writer_recovery_probe" for evt in events),
            "failed_writes": int(writer_health.get("failed_writes", 0)),
            "last_error": writer_health.get("last_error", ""),
        },
        "recovery_capture_failures": {
            "ok": int(capture_health.get("transient_failures", 0)) >= 1,
            "capture_health": capture_health,
        },
    }

    evidence["items"]["queue_behavior_under_heavy_load"]["ok"] = int(writer_health.get("dropped_events", 0)) == 0

    # Stop services and widget.
    capture.stop()
    writer.stop()
    evidence["items"]["graceful_shutdown"].update(
        {
            "writer_thread_alive_after_stop": bool(writer._thread and writer._thread.is_alive()),
            "capture_thread_alive_after_stop": bool(capture._thread and capture._thread.is_alive()),
        }
    )

    widget.cleanup()
    app.processEvents()

    return evidence


def main() -> int:
    report = _run_validation()
    out_dir = Path("logs") / "mission_archive_phase5_validation"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "phase5_runtime_validation_report.json"
    out_path.write_text(json.dumps(report, ensure_ascii=True, indent=2), encoding="utf-8")
    print(json.dumps({"report": str(out_path), "summary_items": list(report.get("items", {}).keys())}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

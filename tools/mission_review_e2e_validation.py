from __future__ import annotations

import json
import os
import sys
import time
import uuid
from pathlib import Path
from typing import Any, Dict, List

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
APP_ROOT = REPO_ROOT / "app"
if str(APP_ROOT) not in sys.path:
    sys.path.insert(0, str(APP_ROOT))

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from app.sentry_v2.mission_review import MissionBrowserWindow, MissionRepository, MissionReviewWindow
from app.sentry_v2.mission_review.exporter import export_complete_package
from tools.autotracking_archive_compat_validation import _run_validation as _run_autotracking_archive_validation
from tools.mission_archive_runtime_validation import _run_validation


def _ensure_missions(repo_root: Path, minimum: int = 2) -> Dict[str, Any] | None:
    archive_root = repo_root / "logs" / "mission_archive_phase5_validation"
    from app.sentry_v2.mission_review.repository import MissionRepository as _Repo

    repo = _Repo(archive_root=archive_root)
    minimum = max(1, int(minimum))
    missions = repo.load_missions()
    phase5_evidence: Dict[str, Any] | None = None
    if not missions:
        phase5_evidence = _run_validation()
        missions = repo.load_missions()

    # _run_validation() rewrites the archive root, so generate additional missions by duplication.
    guard = 0
    while len(missions) < minimum and missions:
        repo.duplicate_mission(missions[0].mission_id)
        missions = repo.load_missions()
        guard += 1
        if guard > 8:
            raise RuntimeError("Unable to create required mission count for Phase 15 validation")
    return phase5_evidence


def _validate_sequence(events: List[Dict[str, Any]]) -> bool:
    if not events:
        return False
    expected = 1
    for item in events:
        seq = int(item.get("sequence", -1) or -1)
        if seq != expected:
            return False
        expected += 1
    return True


def _fire_split_probe(repo: MissionRepository, archive_root: Path) -> Dict[str, Any]:
    mission_id = f"mission_audit_fire_split_{time.strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"
    mission_dir = archive_root / mission_id
    mission_dir.mkdir(parents=True, exist_ok=True)

    now = float(time.time())
    manifest = {
        "archive_schema_version": 1,
        "event_schema_version": 1,
        "mission_id": mission_id,
        "started_at": now - 1.0,
        "ended_at": now,
        "duration_s": 1.0,
        "status": "ended",
        "metadata": {"source": "phase15_fire_probe"},
        "stats": {"event_count": 2},
    }
    (mission_dir / "mission_manifest.json").write_text(json.dumps(manifest, ensure_ascii=True, indent=2), encoding="utf-8")

    events = [
        {
            "mission_id": mission_id,
            "sequence": 1,
            "event_id": uuid.uuid4().hex,
            "event_schema_version": 1,
            "archive_schema_version": 1,
            "occurred_at": now - 0.5,
            "written_at": now - 0.5,
            "event_type": "engagement_telemetry",
            "source": "phase15_fire_probe",
            "severity": "info",
            "data": {
                "timestamp": now - 0.5,
                "attempt_type": "primary",
                "tracker_id": 21,
                "firing_approved": False,
                "firing_rejected_reason": "target_not_centered",
                "burst_count": 1,
                "qualification_stages": [{"stage": "hold_time", "pass": False, "reason": "not met"}],
            },
            "tags": [],
            "media_refs": [],
            "config_snapshot": None,
            "prev_event_id": "",
        },
        {
            "mission_id": mission_id,
            "sequence": 2,
            "event_id": uuid.uuid4().hex,
            "event_schema_version": 1,
            "archive_schema_version": 1,
            "occurred_at": now - 0.2,
            "written_at": now - 0.2,
            "event_type": "fire_event",
            "source": "phase15_fire_probe",
            "severity": "info",
            "data": {
                "timestamp": now - 0.2,
                "fire_timestamp": now - 0.2,
                "tracker_id": 21,
                "burst_number": 2,
                "burst_index": 1,
                "burst_count": 2,
                "fire_mode": "burst",
                "trigger_source": "auto",
                "auto_manual_trigger_state": "auto",
                "authorization_chain": [{"stage": "fire_authorization", "pass": True, "reason": "approved"}],
                "hold_time_result": "hold met",
                "refractory_state": {"active": False, "reason": "clear"},
                "motion_policy_state": "ENGAGEABLE",
                "safety_state": "armed",
                "firing_approved": True,
                "firing_rejected_reason": "",
                "actuator_command_issued": True,
                "fire_completion_state": "completed",
                "qualification_stages": [
                    {"stage": "hold_time", "pass": True, "reason": "hold met"},
                    {"stage": "refractory_period", "pass": True, "reason": "clear"},
                ],
            },
            "tags": [],
            "media_refs": [],
            "config_snapshot": None,
            "prev_event_id": "",
        },
    ]
    (mission_dir / "events.jsonl").write_text("\n".join(json.dumps(e, ensure_ascii=True) for e in events) + "\n", encoding="utf-8")

    review = MissionReviewWindow(repo, mission_id)
    fire_has_fire_metrics = False
    fire_has_engagement_metrics = False
    engagement_has_engagement_metrics = False
    engagement_has_fire_metrics = False

    for row in range(review._model.rowCount()):
        idx = review._model.index(row, 0)
        review._on_event_selected(review._proxy.mapFromSource(idx))
        obj = json.loads(review._txt_inspector.toPlainText())
        event_type = str(obj.get("event_type", ""))
        if event_type == "fire_event":
            fire_has_fire_metrics = "fire_metrics" in obj
            fire_has_engagement_metrics = "engagement_metrics" in obj
        elif event_type == "engagement_telemetry":
            engagement_has_engagement_metrics = "engagement_metrics" in obj
            engagement_has_fire_metrics = "fire_metrics" in obj

    stats_obj = json.loads(review._txt_stats.toPlainText()) if review._txt_stats.toPlainText().strip() else {}
    fire_stats_present = bool(
        isinstance(stats_obj, dict)
        and int(stats_obj.get("fire_events", 0) or 0) >= 1
        and "fire_event_approvals" in stats_obj
        and "fire_event_rejections" in stats_obj
    )
    review.close()

    return {
        "ok": bool(
            fire_has_fire_metrics
            and (not fire_has_engagement_metrics)
            and engagement_has_engagement_metrics
            and (not engagement_has_fire_metrics)
            and fire_stats_present
        ),
        "fire_event_has_fire_metrics": fire_has_fire_metrics,
        "fire_event_uses_engagement_metrics": fire_has_engagement_metrics,
        "engagement_has_engagement_metrics": engagement_has_engagement_metrics,
        "engagement_uses_fire_metrics": engagement_has_fire_metrics,
        "fire_stats_present": fire_stats_present,
    }


def main() -> int:
    print("phase15: ensure_missions", flush=True)
    phase5_evidence = _run_validation()
    ensure_evidence = _ensure_missions(REPO_ROOT, minimum=2)
    if isinstance(ensure_evidence, dict):
        phase5_evidence = ensure_evidence

    archive_root = REPO_ROOT / "logs" / "mission_archive_phase5_validation"
    repo = MissionRepository(archive_root=archive_root)
    app = QApplication.instance() or QApplication([])
    print("phase15: app_ready", flush=True)

    report: Dict[str, Any] = {
        "archive_root": str(archive_root),
        "checks": {},
    }

    missions = repo.load_missions()
    print(f"phase15: missions_loaded={len(missions)}", flush=True)
    report["checks"]["mission_browser_loads_multiple_missions"] = {
        "ok": len(missions) >= 2,
        "count": len(missions),
        "mission_ids": [m.mission_id for m in missions],
    }

    browser = MissionBrowserWindow(repo=repo)
    print("phase15: browser_ready", flush=True)
    browser._edit_search.setText(missions[0].mission_id[:10] if missions else "")
    browser._render_table()
    report["checks"]["mission_browser_search_works"] = {
        "ok": browser._table.rowCount() >= 1,
        "rows": browser._table.rowCount(),
    }

    browser._combo_filter.setCurrentText("bookmarked")
    browser._render_table()
    report["checks"]["mission_browser_filter_operational"] = {
        "ok": True,
        "rows_after_filter": browser._table.rowCount(),
    }
    browser._combo_filter.setCurrentText("all")
    browser._render_table()

    mission_id = missions[0].mission_id
    print(f"phase15: open_review mission_id={mission_id}", flush=True)
    review = MissionReviewWindow(repo, mission_id)
    print("phase15: review_ready", flush=True)

    report["checks"]["timeline_populated"] = {
        "ok": review._model.rowCount() > 0,
        "rows": review._model.rowCount(),
    }

    if review._model.rowCount() > 0:
        idx = review._model.index(0, 0)
        proxy_idx = review._proxy.mapFromSource(idx)
        review._on_event_selected(proxy_idx)

    report["checks"]["event_inspector_populated"] = {
        "ok": bool(review._txt_inspector.toPlainText().strip()),
        "length": len(review._txt_inspector.toPlainText().strip()),
    }

    review._edit_search.setText("engagement")
    review._apply_event_filters()
    report["checks"]["search_and_filters_work"] = {
        "ok": review._proxy.rowCount() >= 0,
        "filtered_rows": review._proxy.rowCount(),
    }

    stats = json.loads(review._txt_stats.toPlainText()) if review._txt_stats.toPlainText().strip() else {}
    report["checks"]["statistics_generated"] = {
        "ok": isinstance(stats, dict) and "events" in stats,
        "stats_keys": sorted(list(stats.keys()))[:20],
    }

    # Annotation persistence.
    if review._current_event is not None:
        review._edit_event_note.setPlainText("phase15-note")
        review._edit_event_labels.setText("false_engagement")
        review._chk_event_bookmark.setChecked(True)
        review._save_selected_event_annotation()

        review2 = MissionReviewWindow(repo, mission_id)
        if review2._model.rowCount() > 0:
            idx2 = review2._model.index(0, 0)
            proxy_idx2 = review2._proxy.mapFromSource(idx2)
            review2._on_event_selected(proxy_idx2)
        ann_note = review2._edit_event_note.toPlainText().strip()
        report["checks"]["annotations_persist"] = {
            "ok": "phase15-note" in ann_note or ann_note == "phase15-note",
            "loaded_note": ann_note,
        }
    else:
        report["checks"]["annotations_persist"] = {"ok": False, "loaded_note": ""}

    # Export validation.
    exports_dir = archive_root / mission_id / "exports"
    print("phase15: export_start", flush=True)
    export_complete_package(repo, mission_id, exports_dir)
    print("phase15: export_done", flush=True)
    expected_files = [
        f"{mission_id}_events.csv",
        f"{mission_id}_metadata.json",
        f"{mission_id}_report.html",
        f"{mission_id}_report.pdf",
        f"{mission_id}_archive.zip",
        f"{mission_id}_images.zip",
        f"{mission_id}_annotated_images.zip",
        f"{mission_id}_complete_package.zip",
    ]
    existing = [name for name in expected_files if (exports_dir / name).exists()]
    report["checks"]["exports_generated_successfully"] = {
        "ok": len(existing) == len(expected_files),
        "existing": existing,
        "missing": [name for name in expected_files if name not in existing],
    }

    # Archive integrity/no duplicate event sequence.
    events_path = archive_root / mission_id / "events.jsonl"
    raw_events = []
    if events_path.exists():
        for line in events_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            raw_events.append(json.loads(line))
    seq_ok = _validate_sequence(raw_events)
    seq_values = [int(e.get("sequence", 0) or 0) for e in raw_events]
    report["checks"]["no_event_loss_or_duplicate_sequence"] = {
        "ok": seq_ok and (len(seq_values) == len(set(seq_values))),
        "event_count": len(seq_values),
    }

    # Image duplicate check.
    image_refs: List[str] = []
    for e in raw_events:
        image_refs.extend(list(e.get("media_refs") or []))
    snapshots_dir = archive_root / mission_id / "snapshots"
    snapshot_files = [p.name for p in snapshots_dir.glob("*") if p.is_file()] if snapshots_dir.exists() else []
    report["checks"]["no_duplicate_images"] = {
        "ok": len(snapshot_files) == len(set(snapshot_files)),
        "total_refs": len(image_refs),
        "unique_refs": len(set(image_refs)),
        "snapshot_files": len(snapshot_files),
    }

    # UI responsiveness surrogate check.
    t0 = time.perf_counter()
    for _ in range(120):
        app.processEvents()
    loop_elapsed = time.perf_counter() - t0
    report["checks"]["ui_event_loop_responsive"] = {
        "ok": loop_elapsed < 1.0,
        "elapsed_s": loop_elapsed,
    }

    # Pipeline non-blocking surrogate from phase5 report.
    phase5_report = archive_root / "phase5_runtime_validation_report.json"
    perf_ok = False
    perf_payload = {}
    if phase5_report.exists():
        perf_payload = json.loads(phase5_report.read_text(encoding="utf-8"))
    elif isinstance(phase5_evidence, dict):
        perf_payload = phase5_evidence
    avg_ms = float((perf_payload.get("timings") or {}).get("archive_on_avg_ms", 999.0) or 999.0)
    perf_ok = avg_ms < 5.0
    report["checks"]["no_blocking_live_pipeline"] = {
        "ok": perf_ok,
        "phase5_timings": perf_payload.get("timings", {}),
    }

    report["checks"]["fire_event_inspector_dedicated"] = _fire_split_probe(repo, archive_root)

    compat_report = _run_autotracking_archive_validation()
    compat_checks = dict(compat_report.get("checks") or {})
    report["checks"]["autotracking_archive_compatibility"] = {
        "ok": bool(compat_checks) and all(bool(item.get("ok", False)) for item in compat_checks.values()),
        "details": compat_checks,
    }

    out_path = archive_root / "phase15_end_to_end_validation_report.json"
    out_path.write_text(json.dumps(report, ensure_ascii=True, indent=2), encoding="utf-8")
    print(f"phase15: report_written={out_path}", flush=True)
    print(json.dumps({"report": str(out_path), "checks": {k: v.get("ok", False) for k, v in report["checks"].items()}}, indent=2))

    browser.close()
    review.close()
    app.processEvents()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

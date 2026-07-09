from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional


def _latest_jsonl(log_dir: Path) -> Optional[Path]:
    files = sorted(log_dir.glob("forensic_validation_*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)
    return files[0] if files else None


def _load_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        text = line.strip()
        if not text:
            continue
        rows.append(json.loads(text))
    return rows


def analyze(path: Path) -> Dict[str, Any]:
    rows = _load_jsonl(path)
    detections = [r for r in rows if str(r.get("event_type", "")) == "detection_evaluation"]
    planner = [r for r in rows if str(r.get("event_type", "")) == "planner_selection"]
    engagements = [r for r in rows if str(r.get("event_type", "")) == "engagement_attempt"]

    qual_counter = Counter(str(r.get("qualification_status", "unknown")) for r in detections)
    reject_reasons = Counter(str(r.get("rejection_reason", "")).strip() for r in detections if str(r.get("rejection_reason", "")).strip())

    first_selected_by_event: List[int] = []
    for r in planner:
        selected = list(r.get("selected_track_ids", []) or [])
        if selected:
            first_selected_by_event.append(int(selected[0]))

    tracker_switches = 0
    prev = None
    for track_id in first_selected_by_event:
        if prev is not None and track_id != prev:
            tracker_switches += 1
        prev = track_id

    stationary_engagements = [
        r for r in engagements
        if bool((r.get("stationary_analysis") or {}).get("is_stationary", False))
    ]
    wrong_class_engagements = [
        r for r in engagements
        if bool((r.get("wrong_class_analysis") or {}).get("outside_configured_classes", False))
    ]
    false_engagements = [
        r for r in engagements
        if bool(r.get("firing_approved", False)) and (
            bool((r.get("stationary_analysis") or {}).get("is_stationary", False))
            or bool((r.get("wrong_class_analysis") or {}).get("outside_configured_classes", False))
        )
    ]

    false_positive_sources = Counter()
    for r in false_engagements:
        if bool((r.get("wrong_class_analysis") or {}).get("outside_configured_classes", False)):
            false_positive_sources["wrong_class_allowed"] += 1
        if bool((r.get("stationary_analysis") or {}).get("is_stationary", False)):
            false_positive_sources["stationary_target_approved"] += 1

    top_false_source = ""
    if false_positive_sources:
        top_false_source = false_positive_sources.most_common(1)[0][0]

    summary = {
        "forensic_log": str(path),
        "total_records": int(len(rows)),
        "total_detections": int(len(detections)),
        "total_qualified_targets": int(qual_counter.get("qualified", 0)),
        "total_rejected_targets": int(qual_counter.get("rejected", 0)),
        "total_tracker_switches": int(tracker_switches),
        "total_planner_selection_events": int(len(planner)),
        "total_engagement_attempts": int(len(engagements)),
        "total_false_engagements": int(len(false_engagements)),
        "total_stationary_object_engagements": int(len(stationary_engagements)),
        "total_wrong_class_engagements": int(len(wrong_class_engagements)),
        "rejection_reasons_ranked": [
            {"reason": reason, "count": int(count)} for reason, count in reject_reasons.most_common()
        ],
        "false_positive_sources": [
            {"source": source, "count": int(count)} for source, count in false_positive_sources.most_common()
        ],
        "biggest_false_positive_source": str(top_false_source),
        "sample_false_engagements": false_engagements[:10],
    }

    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze forensic validation JSONL output")
    parser.add_argument("--log", type=str, default="")
    args = parser.parse_args()

    default_dir = Path("logs/forensic_validation")
    if args.log:
        log_path = Path(args.log)
    else:
        latest = _latest_jsonl(default_dir)
        if latest is None:
            raise SystemExit("No forensic validation log files found.")
        log_path = latest

    summary = analyze(log_path)
    out_path = Path("logs/forensic_validation") / f"forensic_analysis_{log_path.stem}.json"
    out_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

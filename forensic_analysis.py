#!/usr/bin/env python3
"""
Forensic Mission Analysis Tool

Analyzes forensic_detection_evaluation events from Smart Sentry mission logs,
extracting qualification status, rejection reasons, and tracking characteristics.
"""

import json
import pathlib
import collections
import sys
from typing import Dict, List, Tuple


def analyze_mission_log(log_path: pathlib.Path) -> None:
    """Analyze a single mission's forensic events."""
    if not log_path.exists():
        print(f"ERROR: Log file not found: {log_path}")
        return

    reasons = collections.Counter()
    status = collections.Counter()
    track = collections.defaultdict(list)
    count = 0

    try:
        lines = log_path.read_text(encoding='utf-8').splitlines()
    except Exception as e:
        print(f"ERROR reading log file: {e}")
        return

    for line in lines:
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except Exception:
            continue

        data = rec.get('data') or {}
        if not isinstance(data, dict):
            continue
        if rec.get('event_type') != 'forensic_detection_evaluation':
            continue

        count += 1
        reason = data.get('rejection_reason')
        if reason:
            reasons[str(reason)] += 1

        status[str(data.get('qualification_status', 'unknown'))] += 1

        tid = data.get('tracker_id')
        if tid is not None:
            ts = float(data.get('timestamp', 0) or 0)
            track[int(tid)].append(ts)

    # Compute span statistics for long-lived tracks
    spans: List[Tuple[int, float, int]] = []
    for tid, ts in track.items():
        if len(ts) > 1:
            span = max(ts) - min(ts)
            spans.append((tid, span, len(ts)))

    # Print results
    print(f"\n{'='*60}")
    print(f"Mission: {log_path.parent.name}")
    print(f"{'='*60}")
    print(f"\nTotal forensic evaluations: {count}")
    print(f"\nQualification Status (top 5):")
    for status_str, cnt in status.most_common(5):
        print(f"  {status_str:30s}: {cnt:5d}")

    print(f"\nRejection Reasons (top 10):")
    for reason_str, cnt in reasons.most_common(10):
        print(f"  {reason_str:40s}: {cnt:5d}")

    print(f"\nLongest-Lived Tracks (by time span):")
    for tid, span, count_frames in sorted(spans, key=lambda x: x[1], reverse=True)[:10]:
        print(f"  Tracker {tid:3d}: span={span:7.2f}s  frames={count_frames:3d}")


def main():
    if len(sys.argv) > 1:
        log_path = pathlib.Path(sys.argv[1])
        analyze_mission_log(log_path)
    else:
        # Default: analyze most recent mission
        mission_dir = pathlib.Path(r'f:\SMART SENTRY_v2a\logs\mission_archive')
        if not mission_dir.exists():
            print(f"Default mission archive not found: {mission_dir}")
            print(f"Usage: python forensic_analysis.py <path_to_events.jsonl>")
            sys.exit(1)

        missions = sorted([d for d in mission_dir.iterdir() if d.is_dir()], reverse=True)
        if not missions:
            print(f"No missions found in: {mission_dir}")
            sys.exit(1)

        for mission in missions[:3]:  # Analyze top 3 most recent
            events_file = mission / 'events.jsonl'
            if events_file.exists():
                analyze_mission_log(events_file)


if __name__ == '__main__':
    main()

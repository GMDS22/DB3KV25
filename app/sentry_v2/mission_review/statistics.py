from __future__ import annotations

from collections import Counter, defaultdict
from typing import Dict, Iterable

from .repository import MissionEvent


def compute_mission_statistics(events: Iterable[MissionEvent]) -> Dict[str, object]:
    items = list(events)
    if not items:
        return {
            "duration_s": 0.0,
            "events": 0,
            "detections": 0,
            "unique_targets": 0,
            "average_confidence": 0.0,
            "average_threat_score": 0.0,
            "planner_selections": 0,
            "planner_cancellations": 0,
            "motion_policy_transitions": 0,
            "track_only_transitions": 0,
            "fire_approvals": 0,
            "fire_rejections": 0,
            "shots_fired": 0,
            "burst_count": 0,
            "fire_events": 0,
            "fire_event_approvals": 0,
            "fire_event_rejections": 0,
            "fire_event_burst_total": 0,
            "fire_event_completions": 0,
            "false_engagements": 0,
            "false_positives": 0,
            "state_transitions": {},
            "rejection_reasons": {},
        }

    start = min(float(e.occurred_at) for e in items)
    end = max(float(e.occurred_at) for e in items)
    duration_s = max(0.0, end - start)

    detections = [e for e in items if e.category == "detection"]
    engagements = [e for e in items if e.category == "engagement"]
    trackers = {int(e.tracker_id) for e in items if int(e.tracker_id) >= 0}

    confidences = [float(e.confidence) for e in items if float(e.confidence) > 0.0]
    threats = [float(e.threat_score) for e in items if float(e.threat_score) > 0.0]

    rejection = Counter(str(e.decision) for e in items if str(e.decision))
    state_transitions = Counter(
        f"{str(e.data.get('from_state', ''))}->{str(e.data.get('to_state', ''))}"
        for e in items
        if e.event_type == "engine_state_transition"
    )

    fire_approvals = 0
    fire_rejections = 0
    burst_count = 0
    shots_fired = 0
    fire_events = 0
    fire_event_approvals = 0
    fire_event_rejections = 0
    fire_event_burst_total = 0
    fire_event_completions = 0
    for e in items:
        if e.event_type != "engagement_telemetry":
            if e.category == "fire" or "fire" in str(e.event_type).lower():
                fire_events += 1
                approved = bool(e.data.get("firing_approved", e.data.get("fire_approved", False)))
                burst = int(e.data.get("burst_count", e.data.get("burst_number", 1)) or 1)
                fire_event_burst_total += max(1, burst)
                if approved:
                    fire_event_approvals += 1
                else:
                    fire_event_rejections += 1
                if str(e.data.get("fire_completion_state", "")).strip().lower() in {"completed", "fired", "done"}:
                    fire_event_completions += 1
            continue
        if bool(e.data.get("firing_approved", False)):
            fire_approvals += 1
            burst = int(e.data.get("burst_count", 1) or 1)
            burst_count += burst
            shots_fired += burst
        else:
            fire_rejections += 1

    planner_selections = sum(1 for e in items if e.event_type == "planner_selection")
    planner_cancellations = sum(1 for e in items if "cancel" in str(e.decision).lower())
    motion_policy_transitions = sum(1 for e in items if e.event_type == "motion_policy_transition")
    track_only_transitions = sum(
        1
        for e in items
        if e.event_type == "motion_policy_transition" and str(e.data.get("to_state", "")) == "TRACK_ONLY"
    )

    return {
        "duration_s": duration_s,
        "fps_estimate": (len(items) / duration_s) if duration_s > 0.0 else 0.0,
        "events": len(items),
        "detections": len(detections),
        "tracking_duration_s": sum(
            1.0
            for e in items
            if e.category in {"tracking", "detection"} and int(e.tracker_id) >= 0
        ),
        "unique_targets": len(trackers),
        "average_confidence": (sum(confidences) / len(confidences)) if confidences else 0.0,
        "average_threat_score": (sum(threats) / len(threats)) if threats else 0.0,
        "planner_selections": planner_selections,
        "planner_cancellations": planner_cancellations,
        "motion_policy_transitions": motion_policy_transitions,
        "track_only_transitions": track_only_transitions,
        "fire_approvals": fire_approvals,
        "fire_rejections": fire_rejections,
        "shots_fired": shots_fired,
        "burst_count": burst_count,
        "fire_events": fire_events,
        "fire_event_approvals": fire_event_approvals,
        "fire_event_rejections": fire_event_rejections,
        "fire_event_burst_total": fire_event_burst_total,
        "fire_event_completions": fire_event_completions,
        "false_engagements": sum(1 for e in items if "false_engagement" in e.data.get("labels", [])),
        "false_positives": sum(1 for e in items if "false_positive" in e.data.get("labels", [])),
        "state_transitions": dict(state_transitions),
        "rejection_reasons": dict(rejection),
        "pir_activations": sum(1 for e in items if "pir" in e.event_type.lower()),
        "safety_events": sum(1 for e in items if "safety" in e.event_type.lower()),
        "camera_disconnects": sum(1 for e in items if "camera_disconnect" in e.event_type.lower()),
        "yolo_restarts": sum(1 for e in items if "yolo" in e.event_type.lower() and "restart" in e.event_type.lower()),
    }

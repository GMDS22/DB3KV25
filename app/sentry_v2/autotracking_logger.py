"""
Autotracking & YOLO Detection Logger

Captures detailed flow of YOLO detections through threat scoring and engagement promotion.
Logs engagement state transitions, tracking corrections, and movement decisions for analysis.

Key events logged:
  - YOLO detection (raw detection with confidence, class, position)
  - Threat scoring (computed score, factors contributing to score)
  - Engagement promotion (when target meets threshold for engagement queue)
  - Engagement state transitions (aim -> precision -> fire)
  - Tracking corrections (error, PID components, movement commands)
  - Loss recovery (when target is lost and recovery begins)
  - Target re-acquisition (when lost target is found again)

Usage:
  logger = AutotrackingLogger()
  logger.log_yolo_detection(det_obj, threat_score, meets_threshold)
  logger.log_engagement_promoted(target, timestamp)
  logger.log_engagement_transition(phase_from, phase_to, reason)
  logger.log_tracking_frame(error_pan, error_tilt, corrections, etc.)
  csv_path = logger.export_csv()
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional, List, Dict, Any
import time


@dataclass
class AutotrackingEvent:
    """Single autotracking event log entry."""
    timestamp_ms: int
    frame_id: int
    event_type: str  # "yolo_detection", "threat_score", "engagement_promoted", "state_transition", "tracking_frame", "loss_event", "reacquisition"
    target_id: int = 0
    class_name: str = ""
    
    # YOLO detection fields
    detection_confidence: float = 0.0
    detection_bbox_x: float = 0.0
    detection_bbox_y: float = 0.0
    detection_bbox_w: float = 0.0
    detection_bbox_h: float = 0.0
    norm_cx: float = 0.0  # normalized center x (0.0-1.0)
    norm_cy: float = 0.0  # normalized center y (0.0-1.0)
    
    # Threat scoring fields
    threat_score: float = 0.0
    threat_score_proximity: float = 0.0
    threat_score_size: float = 0.0
    threat_score_confidence: float = 0.0
    threat_score_persistence: float = 0.0
    threat_score_speed: float = 0.0
    meets_threshold: bool = False
    threshold_value: float = 0.5
    
    # Engagement fields
    phase_transition_from: str = ""  # "aim", "precision", "fire", "cooldown", "loss_recovery"
    phase_transition_to: str = ""
    transition_reason: str = ""
    queue_position: int = 0
    
    # Tracking correction fields
    error_pan_deg: float = 0.0
    error_tilt_deg: float = 0.0
    error_magnitude: float = 0.0
    pid_p_pan: float = 0.0
    pid_i_pan: float = 0.0
    pid_d_pan: float = 0.0
    pid_p_tilt: float = 0.0
    pid_i_tilt: float = 0.0
    pid_d_tilt: float = 0.0
    move_cmd_pan: float = 0.0
    move_cmd_tilt: float = 0.0
    move_magnitude: float = 0.0
    
    # Lock status fields
    aim_lock_pan: bool = False
    aim_lock_tilt: bool = False
    aim_lock_frames: int = 0
    
    # Loss/recovery fields
    target_lost: bool = False
    recovery_protocol: str = ""
    recovery_phase: str = ""
    
    # Metadata
    notes: str = ""


class AutotrackingLogger:
    """
    Logs YOLO detection -> threat score -> engagement promotion flow
    for analysis of autotracking behavior and engagement decisions.
    """

    def __init__(self, log_dir: str = "logs/autotracking"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.events: List[AutotrackingEvent] = []
        self.session_started = time.time()
        self.frame_id = 0
        self._max_events = 10000  # Prevent unbounded memory growth

    def log_yolo_detection(
        self,
        target_id: int,
        class_name: str,
        confidence: float,
        bbox_x: float,
        bbox_y: float,
        bbox_w: float,
        bbox_h: float,
        norm_cx: float,
        norm_cy: float,
        threat_score: float = 0.0,
        threat_components: Optional[Dict[str, float]] = None,
        meets_threshold: bool = False,
        threshold_value: float = 0.5,
        notes: str = "",
    ) -> None:
        """Log a raw YOLO detection with threat score."""
        now_ms = int((time.time() - self.session_started) * 1000)
        
        components = threat_components or {}
        event = AutotrackingEvent(
            timestamp_ms=now_ms,
            frame_id=self.frame_id,
            event_type="yolo_detection",
            target_id=target_id,
            class_name=class_name,
            detection_confidence=confidence,
            detection_bbox_x=bbox_x,
            detection_bbox_y=bbox_y,
            detection_bbox_w=bbox_w,
            detection_bbox_h=bbox_h,
            norm_cx=norm_cx,
            norm_cy=norm_cy,
            threat_score=threat_score,
            threat_score_proximity=components.get("proximity", 0.0),
            threat_score_size=components.get("size", 0.0),
            threat_score_confidence=components.get("confidence", 0.0),
            threat_score_persistence=components.get("persistence", 0.0),
            threat_score_speed=components.get("speed", 0.0),
            meets_threshold=meets_threshold,
            threshold_value=threshold_value,
            notes=notes,
        )
        self._add_event(event)

    def log_engagement_promoted(
        self,
        target_id: int,
        class_name: str,
        threat_score: float,
        queue_position: int = 0,
        notes: str = "",
    ) -> None:
        """Log when a target threatens and is promoted to engagement queue."""
        now_ms = int((time.time() - self.session_started) * 1000)
        event = AutotrackingEvent(
            timestamp_ms=now_ms,
            frame_id=self.frame_id,
            event_type="engagement_promoted",
            target_id=target_id,
            class_name=class_name,
            threat_score=threat_score,
            queue_position=queue_position,
            notes=notes,
        )
        self._add_event(event)

    def log_state_transition(
        self,
        phase_from: str,
        phase_to: str,
        reason: str = "",
        target_id: int = 0,
        notes: str = "",
    ) -> None:
        """Log engagement state transitions (aim -> precision -> fire -> etc)."""
        now_ms = int((time.time() - self.session_started) * 1000)
        event = AutotrackingEvent(
            timestamp_ms=now_ms,
            frame_id=self.frame_id,
            event_type="state_transition",
            target_id=target_id,
            phase_transition_from=phase_from,
            phase_transition_to=phase_to,
            transition_reason=reason,
            notes=notes,
        )
        self._add_event(event)

    def log_tracking_frame(
        self,
        target_id: int,
        class_name: str,
        error_pan: float,
        error_tilt: float,
        pid_p_pan: float,
        pid_i_pan: float,
        pid_d_pan: float,
        pid_p_tilt: float,
        pid_i_tilt: float,
        pid_d_tilt: float,
        move_cmd_pan: float,
        move_cmd_tilt: float,
        aim_lock_pan: bool = False,
        aim_lock_tilt: bool = False,
        aim_lock_frames: int = 0,
        phase: str = "precision",
        notes: str = "",
    ) -> None:
        """Log a single tracking correction frame during engagement."""
        import math
        now_ms = int((time.time() - self.session_started) * 1000)
        error_mag = math.sqrt(error_pan**2 + error_tilt**2)
        move_mag = math.sqrt(move_cmd_pan**2 + move_cmd_tilt**2)
        
        event = AutotrackingEvent(
            timestamp_ms=now_ms,
            frame_id=self.frame_id,
            event_type="tracking_frame",
            target_id=target_id,
            class_name=class_name,
            error_pan_deg=error_pan,
            error_tilt_deg=error_tilt,
            error_magnitude=error_mag,
            pid_p_pan=pid_p_pan,
            pid_i_pan=pid_i_pan,
            pid_d_pan=pid_d_pan,
            pid_p_tilt=pid_p_tilt,
            pid_i_tilt=pid_i_tilt,
            pid_d_tilt=pid_d_tilt,
            move_cmd_pan=move_cmd_pan,
            move_cmd_tilt=move_cmd_tilt,
            move_magnitude=move_mag,
            aim_lock_pan=aim_lock_pan,
            aim_lock_tilt=aim_lock_tilt,
            aim_lock_frames=aim_lock_frames,
            phase_transition_to=phase,
            notes=notes,
        )
        self._add_event(event)

    def log_loss_event(
        self,
        target_id: int,
        class_name: str,
        recovery_protocol: str = "",
        notes: str = "",
    ) -> None:
        """Log when an engaged target is lost and recovery begins."""
        now_ms = int((time.time() - self.session_started) * 1000)
        event = AutotrackingEvent(
            timestamp_ms=now_ms,
            frame_id=self.frame_id,
            event_type="loss_event",
            target_id=target_id,
            class_name=class_name,
            target_lost=True,
            recovery_protocol=recovery_protocol,
            notes=notes,
        )
        self._add_event(event)

    def log_reacquisition(
        self,
        target_id: int,
        class_name: str,
        threat_score: float = 0.0,
        notes: str = "",
    ) -> None:
        """Log when a lost target is re-acquired."""
        now_ms = int((time.time() - self.session_started) * 1000)
        event = AutotrackingEvent(
            timestamp_ms=now_ms,
            frame_id=self.frame_id,
            event_type="reacquisition",
            target_id=target_id,
            class_name=class_name,
            threat_score=threat_score,
            notes=notes,
        )
        self._add_event(event)

    def increment_frame(self) -> None:
        """Increment frame counter (call once per video frame)."""
        self.frame_id += 1

    def get_summary(self, recent_limit: int = 5) -> Dict[str, Any]:
        """Return compact autotracking summary statistics for runtime analysis."""
        event_counts: Dict[str, int] = {}
        promoted: List[AutotrackingEvent] = []
        lost: List[AutotrackingEvent] = []
        reacq: List[AutotrackingEvent] = []
        tracking: List[AutotrackingEvent] = []
        threshold_hits = 0

        for evt in self.events:
            event_counts[evt.event_type] = event_counts.get(evt.event_type, 0) + 1
            if evt.event_type == "engagement_promoted":
                promoted.append(evt)
            elif evt.event_type == "loss_event":
                lost.append(evt)
            elif evt.event_type == "reacquisition":
                reacq.append(evt)
            elif evt.event_type == "tracking_frame":
                tracking.append(evt)
            elif evt.event_type == "yolo_detection" and bool(evt.meets_threshold):
                threshold_hits += 1

        avg_promoted_threat_score = None
        if promoted:
            avg_promoted_threat_score = round(
                sum(float(evt.threat_score) for evt in promoted) / max(1, len(promoted)),
                3,
            )

        avg_tracking_error_deg = None
        avg_move_magnitude = None
        max_aim_lock_frames = 0
        if tracking:
            avg_tracking_error_deg = round(
                sum(float(evt.error_magnitude) for evt in tracking) / max(1, len(tracking)),
                3,
            )
            avg_move_magnitude = round(
                sum(float(evt.move_magnitude) for evt in tracking) / max(1, len(tracking)),
                3,
            )
            max_aim_lock_frames = max(int(evt.aim_lock_frames) for evt in tracking)

        recent_events: List[Dict[str, Any]] = []
        for evt in self.events[-max(0, int(recent_limit)):]:
            recent_events.append({
                "event_type": str(evt.event_type),
                "target_id": int(evt.target_id),
                "class_name": str(evt.class_name),
                "phase": str(evt.phase_transition_to or evt.phase_transition_from or ""),
                "threat_score": round(float(evt.threat_score), 3) if evt.threat_score else 0.0,
                "error_magnitude": round(float(evt.error_magnitude), 3) if evt.error_magnitude else 0.0,
                "aim_lock_frames": int(evt.aim_lock_frames),
                "notes": str(evt.notes or "")[:120],
            })

        return {
            "session_duration_s": round(max(0.0, time.time() - self.session_started), 2),
            "total_events": int(len(self.events)),
            "total_frames": int(self.frame_id),
            "event_counts": event_counts,
            "detections_meeting_threshold": int(threshold_hits),
            "promoted_targets": int(len(promoted)),
            "loss_events": int(len(lost)),
            "reacquisitions": int(len(reacq)),
            "tracking_frames": int(len(tracking)),
            "avg_promoted_threat_score": avg_promoted_threat_score,
            "avg_tracking_error_deg": avg_tracking_error_deg,
            "avg_move_magnitude": avg_move_magnitude,
            "max_aim_lock_frames": int(max_aim_lock_frames),
            "recent_events": recent_events,
        }

    def export_csv(self, session_id: str = "") -> str:
        """Export events to CSV and return path."""
        if not session_id:
            session_id = str(int(self.session_started)).replace(".", "_")
        
        csv_path = self.log_dir / f"autotracking_{session_id}.csv"
        
        if not self.events:
            print(f"[AUTOTRACK_LOGGER] No events to export", flush=True)
            return str(csv_path)
        
        try:
            with open(csv_path, "w", newline="") as f:
                fieldnames = [
                    "timestamp_ms", "frame_id", "event_type", "target_id", "class_name",
                    "detection_confidence", "norm_cx", "norm_cy", "threat_score", "meets_threshold",
                    "phase_from", "phase_to", "transition_reason",
                    "error_pan_deg", "error_tilt_deg", "error_magnitude",
                    "pid_p_pan", "pid_i_pan", "pid_d_pan",
                    "pid_p_tilt", "pid_i_tilt", "pid_d_tilt",
                    "move_cmd_pan", "move_cmd_tilt", "move_magnitude",
                    "aim_lock_pan", "aim_lock_tilt", "aim_lock_frames",
                    "target_lost", "recovery_protocol", "notes"
                ]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for evt in self.events:
                    writer.writerow({
                        "timestamp_ms": evt.timestamp_ms,
                        "frame_id": evt.frame_id,
                        "event_type": evt.event_type,
                        "target_id": evt.target_id,
                        "class_name": evt.class_name,
                        "detection_confidence": evt.detection_confidence,
                        "norm_cx": evt.norm_cx,
                        "norm_cy": evt.norm_cy,
                        "threat_score": evt.threat_score,
                        "meets_threshold": evt.meets_threshold,
                        "phase_from": evt.phase_transition_from,
                        "phase_to": evt.phase_transition_to,
                        "transition_reason": evt.transition_reason,
                        "error_pan_deg": evt.error_pan_deg,
                        "error_tilt_deg": evt.error_tilt_deg,
                        "error_magnitude": evt.error_magnitude,
                        "pid_p_pan": evt.pid_p_pan,
                        "pid_i_pan": evt.pid_i_pan,
                        "pid_d_pan": evt.pid_d_pan,
                        "pid_p_tilt": evt.pid_p_tilt,
                        "pid_i_tilt": evt.pid_i_tilt,
                        "pid_d_tilt": evt.pid_d_tilt,
                        "move_cmd_pan": evt.move_cmd_pan,
                        "move_cmd_tilt": evt.move_cmd_tilt,
                        "move_magnitude": evt.move_magnitude,
                        "aim_lock_pan": evt.aim_lock_pan,
                        "aim_lock_tilt": evt.aim_lock_tilt,
                        "aim_lock_frames": evt.aim_lock_frames,
                        "target_lost": evt.target_lost,
                        "recovery_protocol": evt.recovery_protocol,
                        "notes": evt.notes,
                    })
            print(f"[AUTOTRACK_LOGGER] Exported {len(self.events)} events to {csv_path}", flush=True)
            return str(csv_path)
        except Exception as e:
            print(f"[AUTOTRACK_LOGGER] Export failed: {e}", flush=True)
            return str(csv_path)

    def print_summary(self) -> None:
        """Print summary statistics."""
        if not self.events:
            print("[AUTOTRACK_LOGGER] No events logged", flush=True)
            return
        
        # Count event types
        type_counts = {}
        for evt in self.events:
            type_counts[evt.event_type] = type_counts.get(evt.event_type, 0) + 1
        
        # Find promoted targets
        promoted = [e for e in self.events if e.event_type == "engagement_promoted"]
        lost = [e for e in self.events if e.event_type == "loss_event"]
        reacq = [e for e in self.events if e.event_type == "reacquisition"]
        
        print(f"\n[AUTOTRACK_LOGGER] === Summary ===", flush=True)
        print(f"Total events: {len(self.events)}", flush=True)
        print(f"Total frames: {self.frame_id}", flush=True)
        print(f"Event types: {type_counts}", flush=True)
        print(f"Promoted targets: {len(promoted)}", flush=True)
        print(f"Loss events: {len(lost)}", flush=True)
        print(f"Re-acquisitions: {len(reacq)}", flush=True)
        
        if promoted:
            avg_score = sum(e.threat_score for e in promoted) / len(promoted)
            print(f"Average threat score (promoted): {avg_score:.3f}", flush=True)

    def _add_event(self, event: AutotrackingEvent) -> None:
        """Add event and manage memory."""
        self.events.append(event)
        if len(self.events) > self._max_events:
            # Remove oldest half
            self.events = self.events[self._max_events // 2:]

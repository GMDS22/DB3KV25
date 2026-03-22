"""
Precision Aiming Dynamics Logger

Captures per-frame engagement data for tuning analysis:
  - Pan/Tilt error, velocity, corrections
  - PID state (proportional, integral, derivative components)
  - Lock quality, overshoot detection
  - Auto-exports CSV for analysis

Usage:
  logger = PrecisionTuningLogger()
  logger.start_engagement(target_id="T1")
  # ... each frame ...
  logger.log_frame(
      current_pan=90.5,
      current_tilt=50.2,
      target_pan=90.0,
      target_tilt=50.0,
      pid_p_pan=0.01,
      pid_i_pan=0.0,
      pid_d_pan=0.002,
      fired=False
  )
  logger.end_engagement()
  csv_path = logger.export_csv()
"""

from __future__ import annotations

import csv
import json
import os
import time
from dataclasses import dataclass, field, asdict
from copy import deepcopy
from pathlib import Path
from typing import Optional, List, Dict


@dataclass
class PrecisionFrame:
    """Single frame of precision aiming data."""
    timestamp_ms: int
    frame_id: int
    error_pan_deg: float
    error_tilt_deg: float
    error_magnitude_deg: float
    current_pan: float
    current_tilt: float
    target_pan: float
    target_tilt: float
    pid_p_pan: float
    pid_i_pan: float
    pid_d_pan: float
    pid_p_tilt: float
    pid_i_tilt: float
    pid_d_tilt: float
    move_cmd_pan: float
    move_cmd_tilt: float
    deadzone_pan: float
    deadzone_tilt: float
    within_deadzone: bool
    overshoot_pan: bool
    overshoot_tilt: bool
    lock_stable: bool
    fired: bool
    phase: str = "aim"  # "aim", "precision", "fire", "cooldown"


@dataclass
class EngagementSession:
    """Single engagement with one or more targets."""
    session_id: str
    start_time: float
    end_time: Optional[float] = None
    target_ids: List[str] = field(default_factory=list)
    frames: List[PrecisionFrame] = field(default_factory=list)
    mode: int = 0
    config_snapshot: Dict = field(default_factory=dict)


class PrecisionTuningLogger:
    """
    Logs precision aiming dynamics for offline tuning analysis.
    
    Key metrics:
    - Error magnitude and direction per axis
    - PID component contributions (P, I, D)
    - Deadzone effectiveness (reducing jitter)
    - Overshoot patterns (Kp too high or Kd too low)
    - Lock stability (target held steady)
    """

    def __init__(self, log_dir: str = "logs/precision_tuning"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.sessions: List[EngagementSession] = []
        self.current_session: Optional[EngagementSession] = None
        self.frame_counter: int = 0

    def start_engagement(
        self,
        target_id: str = "unknown",
        mode: int = 0,
        config_snapshot: Optional[Dict] = None,
    ) -> str:
        """Start logging a new engagement session."""
        session_id = f"eng_{int(time.time()*1000)}"
        self.current_session = EngagementSession(
            session_id=session_id,
            start_time=time.time(),
            target_ids=[target_id],
            mode=int(mode),
            config_snapshot=config_snapshot or {},
        )
        self.frame_counter = 0
        return session_id

    def log_frame(
        self,
        current_pan: float,
        current_tilt: float,
        target_pan: float,
        target_tilt: float,
        pid_p_pan: float = 0.0,
        pid_i_pan: float = 0.0,
        pid_d_pan: float = 0.0,
        pid_p_tilt: float = 0.0,
        pid_i_tilt: float = 0.0,
        pid_d_tilt: float = 0.0,
        move_cmd_pan: float = 0.0,
        move_cmd_tilt: float = 0.0,
        deadzone_pan: float = 0.18,
        deadzone_tilt: float = 0.15,
        within_deadzone: Optional[bool] = None,
        fired: bool = False,
        lock_stable: bool = False,
        phase: str = "aim",
    ) -> None:
        """Log one frame of precision aiming data."""
        if not self.current_session:
            return

        self.frame_counter += 1

        # Calculate error (how far off target)
        err_pan = target_pan - current_pan
        err_tilt = target_tilt - current_tilt
        err_mag = (err_pan**2 + err_tilt**2) ** 0.5

        # Detect overshoot: moving away from target
        overshoot_pan = (move_cmd_pan > 0.0 and err_pan < 0.0) or (
            move_cmd_pan < 0.0 and err_pan > 0.0
        )
        overshoot_tilt = (move_cmd_tilt > 0.0 and err_tilt < 0.0) or (
            move_cmd_tilt < 0.0 and err_tilt > 0.0
        )

        # Within deadzone? Allow caller override, else compute from errors.
        if within_deadzone is None:
            within_deadzone = abs(err_pan) <= deadzone_pan and abs(err_tilt) <= deadzone_tilt

        frame = PrecisionFrame(
            timestamp_ms=int((time.time() - self.current_session.start_time) * 1000),
            frame_id=self.frame_counter,
            error_pan_deg=float(err_pan),
            error_tilt_deg=float(err_tilt),
            error_magnitude_deg=float(err_mag),
            current_pan=float(current_pan),
            current_tilt=float(current_tilt),
            target_pan=float(target_pan),
            target_tilt=float(target_tilt),
            pid_p_pan=float(pid_p_pan),
            pid_i_pan=float(pid_i_pan),
            pid_d_pan=float(pid_d_pan),
            pid_p_tilt=float(pid_p_tilt),
            pid_i_tilt=float(pid_i_tilt),
            pid_d_tilt=float(pid_d_tilt),
            move_cmd_pan=float(move_cmd_pan),
            move_cmd_tilt=float(move_cmd_tilt),
            deadzone_pan=float(deadzone_pan),
            deadzone_tilt=float(deadzone_tilt),
            within_deadzone=bool(within_deadzone),
            overshoot_pan=bool(overshoot_pan),
            overshoot_tilt=bool(overshoot_tilt),
            lock_stable=bool(lock_stable),
            fired=bool(fired),
            phase=str(phase),
        )
        self.current_session.frames.append(frame)

    def end_engagement(self) -> Optional[str]:
        """End current engagement and return session ID."""
        if not self.current_session:
            return None

        self.current_session.end_time = time.time()
        session_id = self.current_session.session_id
        self.sessions.append(self.current_session)
        self.current_session = None
        self.frame_counter = 0
        return session_id

    def _get_export_sessions(self, session_id: Optional[str] = None) -> List[EngagementSession]:
        """Collect sessions for export, including the current in-progress session if it has frames."""
        sessions: List[EngagementSession] = list(self.sessions)
        if self.current_session is not None and self.current_session.frames:
            snapshot = deepcopy(self.current_session)
            if snapshot.end_time is None:
                snapshot.end_time = time.time()
            sessions.append(snapshot)

        if session_id:
            return [s for s in sessions if s.session_id == session_id]
        return sessions

    def export_csv(self, session_id: Optional[str] = None) -> str:
        """Export session(s) as CSV for analysis."""
        sessions = self._get_export_sessions(session_id)

        if not sessions:
            return ""

        csv_path = self.log_dir / f"precision_tuning_{int(time.time())}.csv"

        with open(csv_path, "w", newline="") as f:
            writer = None
            for session in sessions:
                if not session.frames:
                    continue

                if writer is None:
                    fieldnames = [
                        "session_id",
                        "frame_id",
                        "timestamp_ms",
                        "phase",
                        "error_pan_deg",
                        "error_tilt_deg",
                        "error_magnitude_deg",
                        "current_pan",
                        "current_tilt",
                        "target_pan",
                        "target_tilt",
                        "pid_p_pan",
                        "pid_i_pan",
                        "pid_d_pan",
                        "pid_p_tilt",
                        "pid_i_tilt",
                        "pid_d_tilt",
                        "move_cmd_pan",
                        "move_cmd_tilt",
                        "deadzone_pan",
                        "deadzone_tilt",
                        "within_deadzone",
                        "overshoot_pan",
                        "overshoot_tilt",
                        "lock_stable",
                        "fired",
                    ]
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()

                for frame in session.frames:
                    row = asdict(frame)
                    row["session_id"] = session.session_id
                    writer.writerow(row)

        print(f"[TUNING] Precision logs exported: {csv_path}")
        return str(csv_path)

    def export_summary(self, session_id: Optional[str] = None) -> str:
        """Export JSON summary for quick analysis."""
        sessions = self._get_export_sessions(session_id)

        summaries = []
        for session in sessions:
            if not session.frames:
                continue

            frames = session.frames
            errors_pan = [f.error_pan_deg for f in frames]
            errors_tilt = [f.error_tilt_deg for f in frames]
            overshoots = sum(1 for f in frames if f.overshoot_pan or f.overshoot_tilt)
            locks = sum(1 for f in frames if f.lock_stable)
            deadzones = sum(1 for f in frames if f.within_deadzone)

            summary = {
                "session_id": session.session_id,
                "mode": session.mode,
                "duration_ms": int((session.end_time - session.start_time) * 1000)
                if session.end_time
                else 0,
                "frames": len(frames),
                "targets": session.target_ids,
                "error_pan_avg": sum(errors_pan) / len(errors_pan) if errors_pan else 0.0,
                "error_pan_max": max(errors_pan) if errors_pan else 0.0,
                "error_tilt_avg": sum(errors_tilt) / len(errors_tilt) if errors_tilt else 0.0,
                "error_tilt_max": max(errors_tilt) if errors_tilt else 0.0,
                "overshoot_frames": overshoots,
                "overshoot_percent": (overshoots / len(frames) * 100.0) if frames else 0.0,
                "lock_frames": locks,
                "lock_percent": (locks / len(frames) * 100.0) if frames else 0.0,
                "deadzone_frames": deadzones,
                "deadzone_percent": (deadzones / len(frames) * 100.0) if frames else 0.0,
            }
            summaries.append(summary)

        json_path = self.log_dir / f"precision_summary_{int(time.time())}.json"
        with open(json_path, "w") as f:
            json.dump(summaries, f, indent=2)

        print(f"[TUNING] Precision summary exported: {json_path}")
        return str(json_path)

    def print_summary(self, session_id: Optional[str] = None) -> None:
        """Print human-readable summary of last session."""
        if session_id:
            sessions = [s for s in self.sessions if s.session_id == session_id]
        else:
            sessions = self.sessions[-1:]

        for session in sessions:
            if not session.frames:
                continue

            frames = session.frames
            errors_pan = [f.error_pan_deg for f in frames]
            errors_tilt = [f.error_tilt_deg for f in frames]
            overshoots = sum(1 for f in frames if f.overshoot_pan or f.overshoot_tilt)
            locks = sum(1 for f in frames if f.lock_stable)

            print(f"\n[PRECISION TUNING SUMMARY] Session {session.session_id}")
            print(f"  Mode: {session.mode}")
            print(f"  Duration: {(session.end_time - session.start_time):.2f}s")
            print(f"  Frames: {len(frames)}")
            print(
                f"  Pan Error:  avg={sum(errors_pan)/len(errors_pan):+.3f}°  max={max(errors_pan):+.3f}°"
            )
            print(
                f"  Tilt Error: avg={sum(errors_tilt)/len(errors_tilt):+.3f}°  max={max(errors_tilt):+.3f}°"
            )
            print(f"  Overshoots: {overshoots}/{len(frames)} ({overshoots/len(frames)*100:.1f}%)")
            print(f"  Lock Quality: {locks}/{len(frames)} ({locks/len(frames)*100:.1f}%)")

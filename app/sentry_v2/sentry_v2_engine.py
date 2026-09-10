"""
SMART SENTRY V3 — Engine (Core State Machine)

The engine ties together all components:
    TargetFilter  →  ThreatScorer  →  EngagementPlanner  →  fire / move

State machine:
    GUARDING  — stationary, watching all detections
    ENGAGING  — executing engagement queue (snap-aim-fire per target)
    RETURNING — moving back to guard position after engagement
    PAUSED    — user paused / disabled

The engine is *frame-driven*: the tab calls ``engine.update(detections, frame)``
on every camera frame and the engine emits callbacks for turret/fire actions.
"""

from __future__ import annotations

import random
import time
import inspect
from enum import Enum, auto
from typing import Any, Callable, Dict, List, Optional, Tuple

from .sentry_v2_config import SentryV2Config
from .sentry_v2_no_fire_masks import find_blocking_mask
from .target_filter import (
    DetectedObject,
    FilterDecision,
    SEMANTIC_IDENTITY_CLASSES,
    SHAPE_FILTER_PROFILES,
    SHAPE_PROFILE_ALIASES,
    TargetFilter,
)
from .threat_scorer import ThreatScorer, TrackedTarget
from .engagement_planner import EngagementPlanner, EngagementOrder
from .ml_training_logger import MLTrainingLogger
from .sentry_v2_pir_manager import SentryV2PIRManager
from .precision_tuning_logger import PrecisionTuningLogger
from .autotracking_logger import AutotrackingLogger
from .engagement_telemetry_logger import EngagementTelemetryLogger
from .forensic_validation_logger import ForensicValidationLogger
from .scene_memory import SceneMemory


NON_SEMANTIC_REACQUIRE_CLASSES = {"moving_object", "motion", "foreground", "color", "unknown"}
NON_SEMANTIC_PREDICTION_CLASSES = NON_SEMANTIC_REACQUIRE_CLASSES | {""}


class SentryV2State(Enum):
    PAUSED = auto()
    GUARDING = auto()
    ENGAGING = auto()
    RETURNING = auto()


class SentryV2Engine:
    """
    Frame-driven sentry engine.

    Callbacks (set via ``on_*`` helpers):
      on_fire(burst_count: int)           — fire command
      on_move(pan: float, tilt: float)    — absolute turret move
      on_state_change(old, new)           — state transitions
    """

    def __init__(self, config: SentryV2Config):
        self.cfg = config
        self.state = SentryV2State.PAUSED

        # ML Training Logger (tracks manual and auto engagement decisions)
        self._ml_logger = MLTrainingLogger()
        self._log_ml_training = False  # User toggles this to enable training data capture

        # Precision Tuning Logger (tracks per-frame aiming dynamics for tuning)
        self._precision_logger = PrecisionTuningLogger()
        self._log_precision_tuning = False  # User toggles this to enable precision logging

        # Autotracking Logger (tracks YOLO detection flow and engagement promotion)
        self._autotrack_logger = AutotrackingLogger()
        self._log_autotracking = False  # User toggles this to enable autotracking logging

        # Sub-systems
        self._filter = TargetFilter(config.target_filter)
        self._scorer = ThreatScorer(config.threat_scoring, config.target_filter, self._ml_logger)
        self._planner = EngagementPlanner(config.engagement, config.guard, config.no_fire_masks)
        self._pir_manager = SentryV2PIRManager(config.pir_guard)
        self._scene_memory = SceneMemory()
        self._engagement_telemetry = EngagementTelemetryLogger()
        self._forensic_logger = ForensicValidationLogger()
        self._forensic_overlay_entries: List[Dict[str, Any]] = []
        self._forensic_track_state: Dict[int, Dict[str, float]] = {}
        self._motion_policy_state: Dict[int, Dict[str, Any]] = {}
        self._last_motion_policy_snapshots: Dict[int, Dict[str, Any]] = {}
        self._last_motion_policy_engageable_ids: List[int] = []
        self._frame_number: int = 0
        self._last_update_timestamp: float = 0.0
        self._last_fire_gate_trace: Dict[str, Any] = {}
        self.last_profile_timings_ms: Dict[str, float] = {}

        # Turret state (tracked by main app, seeded from guard config)
        self.current_pan: float = config.guard.guard_pan
        self.current_tilt: float = config.guard.guard_tilt
        self._last_commanded_pan: float = self.current_pan
        self._last_commanded_tilt: float = self.current_tilt
        self._last_command_time: float = 0.0
        self._last_command_move_time_s: float = 0.0
        self._last_measured_pose_time: float = 0.0

        # Engagement queue
        self._queue: List[EngagementOrder] = []
        self._queue_index: int = 0
        self._engage_phase: str = "aim"   # "aim" (coarse acquire/settle) → "precision" → "fire" → "cooldown"
        self._phase_start: float = 0.0

        # Precision aiming PID state
        self._pid_integral_pan: float = 0.0
        self._pid_integral_tilt: float = 0.0
        self._pid_prev_err_pan: float = 0.0
        self._pid_prev_err_tilt: float = 0.0
        self._smoothed_err_pan: float = 0.0
        self._smoothed_err_tilt: float = 0.0
        self._aim_lock_frames: int = 0
        self._target_lost_since: float = 0.0
        self._active_target_last_center: Optional[Tuple[float, float]] = None
        self._active_target_last_bbox: Optional[Tuple[int, int, int, int]] = None
        self._active_target_last_heading_norm: Tuple[float, float] = (0.0, 0.0)
        self._active_target_last_history_samples: int = 0
        self._active_target_last_heading_stability: float = 0.0
        self._active_target_last_seen_time: float = 0.0
        self._active_target_last_aim_pan: float = self.current_pan
        self._active_target_last_aim_tilt: float = self.current_tilt
        self._active_target_last_class: str = ""
        self._active_target_last_source: str = ""
        self._last_err_pan_deg: float = 0.0
        self._last_err_tilt_deg: float = 0.0
        self._err_pan_rate_deg_s: float = 0.0
        self._err_tilt_rate_deg_s: float = 0.0
        self._last_error_sample_time: float = 0.0
        self._trigger_hold_start: float = 0.0
        self._trigger_gate_active: bool = False
        self._trigger_refractory_until: float = 0.0
        self._active_reacquire_confirm_pending_frames: int = 0
        self._active_reacquire_confirm_pending_until: float = 0.0
        self._last_reacquire_note: str = ""
        self._last_reacquire_time: float = 0.0
        self._last_pir_note: str = ""
        self._last_pir_time: float = 0.0
        self._last_no_fire_mask_name: str = ""
        self._track_identity_cache: Dict[int, Dict[str, object]] = {}
        self._last_fire_veto_reason: str = ""
        self._last_fire_veto_time: float = 0.0
        self._loss_recovery_phase: str = ""
        self._loss_recovery_protocol: str = ""
        self._loss_recovery_context: Dict[str, object] = {}
        self._loss_recovery_retry_count: int = 0
        self._loss_recovery_anchor_pan: float = self.current_pan
        self._loss_recovery_anchor_tilt: float = self.current_tilt
        self._loss_recovery_last_move_time: float = 0.0
        self._loss_recovery_search_index: int = 0

        # Precision logging session tracking
        self._current_precision_engagement_id: Optional[str] = None
        self._precision_logging_faulted: bool = False

        # Cached PID components for logging (set after each _compute_visual_servo_correction call)
        self._last_pid_p_pan: float = 0.0
        self._last_pid_i_pan: float = 0.0
        self._last_pid_d_pan: float = 0.0
        self._last_pid_p_tilt: float = 0.0
        self._last_pid_i_tilt: float = 0.0
        self._last_pid_d_tilt: float = 0.0

        # Timing
        self._last_engage_time: float = 0.0
        self._return_start: float = 0.0

        # Per-frame results (exposed for overlay)
        self.last_detections: List[DetectedObject] = []
        self.last_filter_diagnostics: List[FilterDecision] = []
        self.last_targets: List[TrackedTarget] = []
        self.last_qualified: List[DetectedObject] = []
        self.last_queue: List[EngagementOrder] = []
        self.active_order: Optional[EngagementOrder] = None
        self.engagement_log: List[Dict] = []  # recent engagement history

        # Patrol state (guard modes 1-3)
        self._patrol_target_pan: float = config.guard.guard_pan
        self._patrol_target_tilt: float = config.guard.guard_tilt
        self._patrol_sweep_dir: int = 1          # +1 = sweeping right, -1 = left
        self._patrol_wp_index: int = 0            # current waypoint index
        self._patrol_dwell_start: float = 0.0     # when we arrived at current point
        self._patrol_dwelling: bool = False       # True = waiting at a point
        self._patrol_last_update: float = 0.0     # for dt calculation
        self._patrol_initialized: bool = False    # set on first patrol tick

        # PIR state (guard mode PIR cueing)
        self._pir_cue_mode: bool = False          # In PIR cue pursuit?
        self._pir_cue_sensor_id: int = -1
        self._pir_cue_pan: float = 0.0
        self._pir_cue_tilt: float = 0.0
        self._pir_cue_slew_start: float = 0.0
        self._pir_scan_mode: bool = False         # In adaptive scan?
        self._pir_scan_awaiting_settle: bool = False  # Waiting for servo settle before next scan point
        self._pir_settle_start: float = 0.0

        # Acoustic guard state (USB microphone anomaly trigger)
        self._sound_alert_pending: bool = False
        self._sound_alert_pending_since: float = 0.0
        self._sound_alert_pending_level_db: float = 0.0
        self._sound_alert_pending_baseline_db: float = 0.0
        self._sound_alert_active: bool = False
        self._sound_alert_deferred_until_guard_clear: bool = False
        self._sound_alert_phase: str = ""
        self._sound_alert_phase_started: float = 0.0
        self._sound_alert_last_update: float = 0.0
        self._sound_alert_last_started: float = 0.0
        self._sound_alert_points: List[Tuple[float, float]] = []
        self._sound_alert_point_index: int = 0
        self._sound_alert_step_started: bool = False
        self._sound_alert_step_arrived_time: float = 0.0
        self._sound_alert_sweep_stage: int = 0
        self._sound_alert_note: str = ""
        self._sound_alert_note_time: float = 0.0

        # Stationary-target release protocol state
        self._stationary_release_track_id: int = -1
        self._stationary_release_anchor_center: Optional[Tuple[float, float]] = None
        self._stationary_release_since: float = 0.0
        self._stationary_release_fire_cycles: int = 0
        self._stationary_release_suppress_until: float = 0.0

        # Sentry behaviour state (modes 0=Watchful, 1=Curious, 2=Strict)
        self._behaviour_watchful_last_move: float = 0.0   # cooldown for watchful follow ticks
        self._behaviour_curious_glance_active: bool = False
        self._behaviour_curious_glance_start: float = 0.0
        self._behaviour_curious_glance_pan: float = 0.0
        self._behaviour_curious_glance_tilt: float = 0.0
        self._behaviour_curious_last_glance: float = 0.0  # last time a glance was initiated

        # Callbacks
        self._cb_fire: Optional[Callable[[int], None]] = None
        self._cb_move: Optional[Callable[[float, float], None]] = None
        self._cb_state: Optional[Callable[[SentryV2State, SentryV2State], None]] = None
        self._cb_pir_trace: Optional[Callable[[Dict[str, Any]], None]] = None
        self._cb_mission_event: Optional[Callable[[str, Dict[str, Any]], None]] = None
        self._motion_enabled: bool = True
        self._pir_manager.set_trace_callback(self._on_pir_manager_trace)

    # ------------------------------------------------------------------ #
    # Callback registration
    # ------------------------------------------------------------------ #

    def on_fire(self, cb: Callable[[int], None]) -> None:
        self._cb_fire = cb

    def on_move(self, cb: Callable[[float, float], None]) -> None:
        self._cb_move = cb

    def set_pir_trace_callback(self, cb: Optional[Callable[[Dict[str, Any]], None]]) -> None:
        """Register optional PIR diagnostics callback (non-functional tracing only)."""
        self._cb_pir_trace = cb

    def _emit_pir_trace(self, action: str, **fields: Any) -> None:
        callback = self._cb_pir_trace
        if callback is None:
            return
        frame = inspect.currentframe()
        caller = frame.f_back if frame is not None else None
        payload: Dict[str, Any] = {
            "component": "engine",
            "action": str(action),
            "timestamp": float(time.time()),
            "engine_state": str(self.state.name),
            "planner_state": self._current_planner_state(),
            "pir_state": self._current_pir_state(),
            "function": caller.f_code.co_name if caller is not None else "",
            "filename": __file__,
            "line": int(caller.f_lineno) if caller is not None else 0,
        }
        payload.update(fields)
        try:
            callback(payload)
        except Exception:
            pass

    def _on_pir_manager_trace(self, payload: Dict[str, Any]) -> None:
        merged = dict(payload or {})
        merged.setdefault("engine_state", str(self.state.name))
        merged.setdefault("planner_state", self._current_planner_state())
        merged.setdefault("pir_state", self._current_pir_state())
        callback = self._cb_pir_trace
        if callback is None:
            return
        try:
            callback(merged)
        except Exception:
            pass

    def on_state_change(self, cb: Callable[[SentryV2State, SentryV2State], None]) -> None:
        self._cb_state = cb

    def set_mission_event_publisher(self, cb: Optional[Callable[[str, Dict[str, Any]], None]]) -> None:
        self._cb_mission_event = cb

    def _publish_mission_event(self, event_type: str, payload: Dict[str, Any]) -> None:
        callback = self._cb_mission_event
        if callback is None:
            return
        try:
            callback(str(event_type), dict(payload or {}))
        except Exception as exc:
            self._report_runtime_warning("Mission archive publish failed", exc)

    def _report_runtime_warning(self, context: str, exc: Exception) -> None:
        print(f"[SENTRY_V2_ENGINE] {context}: {exc}", flush=True)

    def set_precision_logging_enabled(self, enabled: bool) -> None:
        """Enable or disable precision aiming tuning logger."""
        self._log_precision_tuning = bool(enabled)
        if enabled:
            self._precision_logging_faulted = False

    def set_motion_enabled(self, enabled: bool) -> None:
        self._motion_enabled = bool(enabled)

    def is_motion_enabled(self) -> bool:
        return bool(self._motion_enabled)

    def is_precision_logging_enabled(self) -> bool:
        """Check if precision logging is currently enabled."""
        return self._log_precision_tuning

    def _set_pir_note(self, note: str, *, when: Optional[float] = None) -> None:
        self._last_pir_note = str(note or "")
        self._last_pir_time = float(time.time() if when is None else when)

    def export_precision_logs(self, session_id: Optional[str] = None) -> Tuple[Optional[str], Optional[str]]:
        """
        Export precision logs to CSV and JSON summary files.

        Returns: (csv_path, json_path) of exported files, or ("", "") if no data.
        """
        return self._precision_logger.export_csv(session_id), self._precision_logger.export_summary(session_id)

    def print_precision_summary(self) -> None:
        """Print precision tuning summary to console."""
        self._precision_logger.print_summary()

    def set_autotracking_logging_enabled(self, enabled: bool) -> None:
        """Enable or disable autotracking and YOLO detection logging."""
        self._log_autotracking = bool(enabled)

    def is_autotracking_logging_enabled(self) -> bool:
        """Check if autotracking logging is currently enabled."""
        return self._log_autotracking

    def export_autotracking_logs(self, session_id: Optional[str] = None) -> str:
        """Export autotracking logs to CSV."""
        return self._autotrack_logger.export_csv(session_id or "")

    def get_autotracking_summary(self) -> Dict:
        """Return structured autotracking summary statistics for runtime consumers."""
        summary = dict(self._autotrack_logger.get_summary())
        summary["logging_enabled"] = bool(self._log_autotracking)
        return summary

    def print_autotracking_summary(self) -> None:
        """Print autotracking summary to console."""
        self._autotrack_logger.print_summary()

    # ------------------------------------------------------------------ #
    # Lifecycle
    # ------------------------------------------------------------------ #

    def start(self) -> None:
        """Activate sentry — move to guard position and start watching."""
        self._reset_runtime_state()
        self._change_state(SentryV2State.GUARDING)
        self._move_turret(self.cfg.guard.guard_pan, self.cfg.guard.guard_tilt)

    def _reset_runtime_state(self) -> None:
        self._filter.reset()
        self._queue.clear()
        self.last_queue = []
        self.last_detections = []
        self.last_filter_diagnostics = []
        self.last_targets = []
        self.last_qualified = []
        self._queue_index = 0
        self.active_order = None
        self._last_engage_time = 0.0
        self._reset_precision_state()
        self._active_target_last_center = None
        self._active_target_last_bbox = None
        self._active_target_last_heading_norm = (0.0, 0.0)
        self._active_target_last_history_samples = 0
        self._active_target_last_heading_stability = 0.0
        self._active_target_last_seen_time = 0.0
        self._active_target_last_aim_pan = self.current_pan
        self._active_target_last_aim_tilt = self.current_tilt
        self._active_target_last_class = ""
        self._active_target_last_source = ""
        self._last_err_pan_deg = 0.0
        self._last_err_tilt_deg = 0.0
        self._active_reacquire_confirm_pending_frames = 0
        self._active_reacquire_confirm_pending_until = 0.0
        self._last_reacquire_note = ""
        self._last_reacquire_time = 0.0
        self._last_pir_note = ""
        self._last_pir_time = 0.0
        self._last_no_fire_mask_name = ""
        self._track_identity_cache.clear()
        self._last_fire_veto_reason = ""
        self._last_fire_veto_time = 0.0
        self._return_start = 0.0
        self._last_fire_gate_trace = {}
        self._reset_loss_recovery_state()
        self._pir_cue_mode = False
        self._pir_cue_sensor_id = -1
        self._pir_scan_mode = False
        self._pir_scan_awaiting_settle = False
        self._pir_settle_start = 0.0
        self._pir_manager.cancel_active_cue()
        self._patrol_target_pan = self.current_pan
        self._patrol_target_tilt = self.current_tilt
        self._patrol_sweep_dir = 1
        self._patrol_wp_index = 0
        self._patrol_dwell_start = 0.0
        self._patrol_dwelling = False
        self._patrol_last_update = 0.0
        self._patrol_initialized = False
        self._behaviour_watchful_last_move = 0.0
        self._behaviour_curious_glance_active = False
        self._behaviour_curious_glance_start = 0.0
        self._behaviour_curious_glance_pan = 0.0
        self._behaviour_curious_glance_tilt = 0.0
        self._behaviour_curious_last_glance = 0.0
        self._sound_alert_pending = False
        self._sound_alert_pending_since = 0.0
        self._sound_alert_pending_level_db = 0.0
        self._sound_alert_pending_baseline_db = 0.0
        self._sound_alert_active = False
        self._sound_alert_deferred_until_guard_clear = False
        self._sound_alert_phase = ""
        self._sound_alert_phase_started = 0.0
        self._sound_alert_last_update = 0.0
        self._sound_alert_points = []
        self._sound_alert_point_index = 0
        self._sound_alert_step_started = False
        self._sound_alert_step_arrived_time = 0.0
        self._sound_alert_sweep_stage = 0
        self._sound_alert_note = ""
        self._sound_alert_note_time = 0.0
        self._stationary_release_track_id = -1
        self._stationary_release_anchor_center = None
        self._stationary_release_since = 0.0
        self._stationary_release_fire_cycles = 0
        self._stationary_release_suppress_until = 0.0
        if self._log_precision_tuning and self._current_precision_engagement_id:
            self._precision_logger.end_engagement()
            self._current_precision_engagement_id = None

    def hold_current_guard_position(self, pan: Optional[float] = None, tilt: Optional[float] = None) -> None:
        if pan is not None or tilt is not None:
            target_pan = self.current_pan if pan is None else float(pan)
            target_tilt = self.current_tilt if tilt is None else float(tilt)
            self.current_pan, self.current_tilt = self._clamp_angles(target_pan, target_tilt)
        self.cfg.guard.guard_pan = self.current_pan
        self.cfg.guard.guard_tilt = self.current_tilt
        self._reset_runtime_state()
        self._last_engage_time = time.time()
        self._change_state(SentryV2State.GUARDING)

    def stop(self) -> None:
        self._change_state(SentryV2State.PAUSED)
        self._reset_runtime_state()

    # ------------------------------------------------------------------ #
    # Config hot-reload
    # ------------------------------------------------------------------ #

    def update_config(self, config: SentryV2Config) -> None:
        self.cfg = config
        self._filter.update_config(config.target_filter)
        self._scorer.update_config(config.threat_scoring, config.target_filter)
        self._planner.update_config(config.engagement, config.guard, config.no_fire_masks)
        self._pir_manager.update_config(config.pir_guard)

    # ------------------------------------------------------------------ #
    # Main per-frame update
    # ------------------------------------------------------------------ #

    def update(
        self,
        detections: List[DetectedObject],
        timestamp: Optional[float] = None,
    ) -> None:
        """Call once per camera frame with current detections."""
        now = timestamp or time.time()
        self._frame_number += 1
        self._last_update_timestamp = now
        self.last_profile_timings_ms = {}

        # Increment frame counter for logging
        if self._log_autotracking:
            self._autotrack_logger.increment_frame()

        if self.state == SentryV2State.PAUSED:
            return

        self._last_no_fire_mask_name = ""
        self.last_detections = list(detections)
        self._update_track_identity_cache(detections, now)

        # 1. Filter
        filter_started = time.perf_counter()
        qualified, diagnostics = self._filter.filter_with_diagnostics(detections, now)
        filter_ms = (time.perf_counter() - filter_started) * 1000.0
        self.last_filter_diagnostics = diagnostics
        self.last_qualified = qualified
        
        # Diagnostic logging: show YOLO detections before and after filtering
        if self._log_autotracking and detections:
            for det in detections:
                decision = next((d for d in diagnostics if int(d.track_id) == int(det.track_id)), None)
                status = "PASS" if decision and decision.passed else "REJECT"
                reason = decision.reason if decision else "no_decision"
                self._autotrack_logger.log_note(
                    f"YOLO: class={det.class_name} conf={det.confidence:.2f} size={det.area_ratio:.5f} {status} ({reason})"
                )

        # 2. Score
        scoring_started = time.perf_counter()
        scored = self._scorer.score(qualified, now)
        threat_scoring_ms = (time.perf_counter() - scoring_started) * 1000.0
        self.last_profile_timings_ms = {"target_filter_ms": filter_ms, "threat_scoring_ms": threat_scoring_ms}
        engageable_targets, motion_snapshots = self._apply_motion_policy_to_targets(scored, now)
        self.last_targets = scored
        self._last_motion_policy_snapshots = {int(item.get("track_id", -1)): dict(item) for item in motion_snapshots}
        self._last_motion_policy_engageable_ids = [int(target.det.track_id) for target in engageable_targets]
        self._emit_forensic_detection_records(detections, diagnostics, scored, now)

        # 2b. Record detections in scene memory for class-prior tracking.
        for _t in scored:
            self._scene_memory.record(_t.det, now)

        # Log YOLO detections if autotracking logging enabled
        if self._log_autotracking and scored:
            for target in scored:
                det = target.det
                self._autotrack_logger.log_yolo_detection(
                    target_id=target.target_id,
                    class_name=det.class_name,
                    confidence=det.confidence,
                    bbox_x=det.bbox[0],
                    bbox_y=det.bbox[1],
                    bbox_w=det.bbox[2],
                    bbox_h=det.bbox[3],
                    norm_cx=det.norm_cx,
                    norm_cy=det.norm_cy,
                    threat_score=target.threat_score,
                    threat_components={
                        "proximity": target.threat_score * 0.2,  # Approximate
                        "size": target.threat_score * 0.2,
                        "confidence": target.threat_score * 0.2,
                        "persistence": target.threat_score * 0.2,
                        "speed": target.threat_score * 0.2,
                    },
                    meets_threshold=(target.threat_score >= self.cfg.engagement.min_threat_score),
                    threshold_value=self.cfg.engagement.min_threat_score,
                    notes=f"source={det.source}",
                )

        # 3. State-specific logic
        if self.state == SentryV2State.GUARDING:
            self._update_guarding(scored, now)
        elif self.state == SentryV2State.ENGAGING:
            self._update_engaging(now)
        elif self.state == SentryV2State.RETURNING:
            self._update_returning(now)

    def _forensic_motion_threshold(self) -> float:
        configured = float(getattr(self.cfg.detection_mode, "motion_gate_threshold", 1.0) or 1.0)
        return float(max(0.05, configured))

    def _update_forensic_track_state(self, detections: List[DetectedObject], now: float) -> Dict[int, Dict[str, float]]:
        motion_map: Dict[int, Dict[str, float]] = {}
        threshold = self._forensic_motion_threshold()
        for det in detections:
            track_id = int(det.track_id)
            cx = float(det.norm_cx)
            cy = float(det.norm_cy)
            state = self._forensic_track_state.get(track_id)
            if state is None:
                state = {
                    "first_seen": now,
                    "last_seen": now,
                    "last_cx": cx,
                    "last_cy": cy,
                    "vx": 0.0,
                    "vy": 0.0,
                    "speed": 0.0,
                }
            else:
                dt = max(1e-6, now - float(state.get("last_seen", now)))
                vx = (cx - float(state.get("last_cx", cx))) / dt
                vy = (cy - float(state.get("last_cy", cy))) / dt
                state["vx"] = float(vx)
                state["vy"] = float(vy)
                state["speed"] = float((vx * vx + vy * vy) ** 0.5)
                state["last_seen"] = now
                state["last_cx"] = cx
                state["last_cy"] = cy
            self._forensic_track_state[track_id] = state
            speed = float(state.get("speed", 0.0) or 0.0)
            age = max(0.0, now - float(state.get("first_seen", now)))
            motion_map[track_id] = {
                "detection_age_s": float(age),
                "vx": float(state.get("vx", 0.0) or 0.0),
                "vy": float(state.get("vy", 0.0) or 0.0),
                "speed": speed,
                "moving": bool(speed >= threshold),
                "stationary": bool(speed < threshold),
            }

        stale_ids = [
            tid
            for tid, track_state in self._forensic_track_state.items()
            if (now - float(track_state.get("last_seen", now))) > 8.0
        ]
        for tid in stale_ids:
            self._forensic_track_state.pop(int(tid), None)

        return motion_map

    def _format_forensic_stage_records(
        self,
        det: DetectedObject,
        decision: Optional[FilterDecision],
        target: Optional[TrackedTarget],
        motion_state: Dict[str, float],
    ) -> List[Dict[str, Any]]:
        stages = self._build_filter_stage_records(det, decision, target)
        speed = float(motion_state.get("speed", 0.0) or 0.0)
        threshold = self._forensic_motion_threshold()
        policy_state = dict(self._motion_policy_state.get(int(getattr(det, "track_id", -1) or -1), {}) or {})
        stages.append(
            {
                "stage": "motion_filter",
                "inputs": {
                    "motion_score": speed,
                    "vx": float(motion_state.get("vx", 0.0) or 0.0),
                    "vy": float(motion_state.get("vy", 0.0) or 0.0),
                    "motion_policy_state": str(policy_state.get("state", "TRACKING") or "TRACKING"),
                    "recent_motion_distance_px": float(policy_state.get("recent_motion_distance_px", 0.0) or 0.0),
                    "average_velocity_px_s": float(policy_state.get("average_velocity_px_s", 0.0) or 0.0),
                    "motion_confidence": float(policy_state.get("motion_confidence", 0.0) or 0.0),
                    "stationary_duration_s": float(policy_state.get("stationary_duration_s", 0.0) or 0.0),
                },
                "threshold": {
                    "moving_threshold": threshold,
                    "configured_motion_gate_threshold": float(
                        getattr(self.cfg.detection_mode, "motion_gate_threshold", threshold) or threshold
                    ),
                    "motion_recent_distance_px": float(getattr(self.cfg.engagement, "motion_recent_distance_px", 18.0) or 18.0),
                    "motion_average_velocity_px_s": float(getattr(self.cfg.engagement, "motion_average_velocity_px_s", 10.0) or 10.0),
                    "motion_confidence_min": float(getattr(self.cfg.engagement, "motion_confidence_min", 0.35) or 0.35),
                    "motion_stationary_timeout_s": float(getattr(self.cfg.engagement, "motion_stationary_timeout_s", 4.0) or 4.0),
                },
                "pass": bool(policy_state.get("motion_allowed", True)),
                "reason": str(policy_state.get("suppression_reason", "motion policy evaluated") or "motion policy evaluated"),
            }
        )
        stages.append(
            {
                "stage": "hold_time",
                "inputs": {
                    "trigger_hold_start": float(getattr(self, "_trigger_hold_start", 0.0) or 0.0),
                    "trigger_gate_active": bool(getattr(self, "_trigger_gate_active", False)),
                },
                "threshold": {
                    "required_hold_s": float(getattr(self.cfg.engagement, "fire_trigger_hold_time", 0.0) or 0.0),
                },
                "pass": bool(target is not None),
                "reason": "evaluated during fire authorization path",
            }
        )
        stages.append(
            {
                "stage": "target_centering",
                "inputs": {
                    "last_err_pan_deg": float(getattr(self, "_last_err_pan_deg", 0.0) or 0.0),
                    "last_err_tilt_deg": float(getattr(self, "_last_err_tilt_deg", 0.0) or 0.0),
                },
                "threshold": {
                    "pan_tolerance": float(getattr(self.cfg.engagement, "fire_trigger_enter_pan_tolerance", 0.0) or 0.0),
                    "tilt_tolerance": float(getattr(self.cfg.engagement, "fire_trigger_enter_tilt_tolerance", 0.0) or 0.0),
                },
                "pass": bool(target is not None),
                "reason": "evaluated during engage/fire phases",
            }
        )
        stages.append(
            {
                "stage": "planner_qualification",
                "inputs": {
                    "threat_score": float(getattr(target, "threat_score", 0.0) or 0.0) if target is not None else 0.0,
                },
                "threshold": {
                    "min_threat_score": float(getattr(self.cfg.engagement, "min_threat_score", 0.0) or 0.0),
                },
                "pass": bool(target is not None and float(getattr(target, "threat_score", 0.0) or 0.0) >= float(getattr(self.cfg.engagement, "min_threat_score", 0.0) or 0.0)),
                "reason": "target included in scored candidate set" if target is not None else "target not scored/qualified",
            }
        )
        stages.append(
            {
                "stage": "safety_gates",
                "inputs": self._current_safety_state(time.time()),
                "threshold": {
                    "auto_trigger_enabled": bool(getattr(self.cfg.engagement, "auto_trigger_enabled", False)),
                },
                "pass": bool(target is not None),
                "reason": "evaluated per fire attempt",
            }
        )
        stages.append(
            {
                "stage": "fire_authorization",
                "inputs": {
                    "state": str(self.state.name),
                    "engage_phase": str(getattr(self, "_engage_phase", "") or ""),
                },
                "threshold": {
                    "fire_requires_lock": bool(getattr(self.cfg.engagement, "fire_requires_lock", False)),
                },
                "pass": bool(target is not None),
                "reason": "evaluated inside engagement update path",
            }
        )
        return stages

    def _emit_forensic_detection_records(
        self,
        detections: List[DetectedObject],
        diagnostics: List[FilterDecision],
        scored: List[TrackedTarget],
        now: float,
    ) -> None:
        decision_by_track: Dict[int, FilterDecision] = {
            int(dec.track_id): dec for dec in diagnostics
        }
        target_by_track: Dict[int, TrackedTarget] = {
            int(target.det.track_id): target for target in scored
        }
        threshold = float(getattr(self.cfg.engagement, "min_threat_score", 0.0) or 0.0)
        selected_track_ids = {
            int(order.target.det.track_id)
            for order in list(getattr(self, "_queue", []) or [])
        }
        active_track_id = int(getattr(getattr(self, "active_order", None), "target", None).det.track_id) if getattr(self, "active_order", None) is not None else -1
        motion_map = self._update_forensic_track_state(detections, now)
        overlay_entries: List[Dict[str, Any]] = []

        for det in detections:
            track_id = int(det.track_id)
            decision = decision_by_track.get(track_id)
            target = target_by_track.get(track_id)
            policy_state = dict(self._motion_policy_state.get(track_id, {}) or {})
            motion_state = motion_map.get(track_id, {
                "detection_age_s": 0.0,
                "vx": 0.0,
                "vy": 0.0,
                "speed": 0.0,
                "moving": False,
                "stationary": True,
            })
            shape_info = self._shape_profile_telemetry(det)
            inside_zone = bool(
                self.cfg.target_filter.engagement_zone[0] <= det.norm_cx <= self.cfg.target_filter.engagement_zone[2]
                and self.cfg.target_filter.engagement_zone[1] <= det.norm_cy <= self.cfg.target_filter.engagement_zone[3]
            )
            semantic_hits = int(getattr(decision, "confirm_hits", 0) or 0) if decision is not None else 0
            semantic_required = int(getattr(decision, "confirm_required", 1) or 1) if decision is not None else 1

            if decision is not None and not bool(decision.passed):
                qualification_status = "rejected"
                rejection_reason = str(decision.reason)
            elif track_id == active_track_id or track_id in selected_track_ids:
                qualification_status = "qualified"
                rejection_reason = ""
            elif target is not None and float(getattr(target, "threat_score", 0.0) or 0.0) < threshold:
                qualification_status = "candidate"
                rejection_reason = "below_threat_threshold"
            elif policy_state and str(policy_state.get("state", "TRACKING") or "TRACKING") == "TRACK_ONLY":
                qualification_status = "track_only"
                rejection_reason = str(policy_state.get("suppression_reason", "motion policy suppressed") or "motion policy suppressed")
            elif target is not None:
                qualification_status = "candidate"
                rejection_reason = ""
            else:
                qualification_status = "ignored"
                rejection_reason = "not_scored"

            stages = self._format_forensic_stage_records(det, decision, target, motion_state)
            record: Dict[str, Any] = {
                "event_type": "detection_evaluation",
                "frame_number": int(self._frame_number),
                "timestamp": float(now),
                "state": str(self.state.name),
                "planner_state": self._current_planner_state(),
                "pir_state": self._current_pir_state(),
                "tracker_id": track_id,
                "yolo_class": str(det.class_name),
                "yolo_confidence": float(det.confidence),
                "bbox": [int(det.bbox[0]), int(det.bbox[1]), int(det.bbox[2]), int(det.bbox[3])],
                "detection_age_s": float(motion_state.get("detection_age_s", 0.0) or 0.0),
                "motion_score": float(motion_state.get("speed", 0.0) or 0.0),
                "motion_policy_state": str(policy_state.get("state", "TRACKING") or "TRACKING"),
                "motion_policy": {
                    "state": str(policy_state.get("state", "TRACKING") or "TRACKING"),
                    "previous_state": str(policy_state.get("previous_state", "") or ""),
                    "suppression_reason": str(policy_state.get("suppression_reason", "") or ""),
                    "suppression_timestamp": float(policy_state.get("suppression_timestamp", 0.0) or 0.0),
                    "suppression_expiry": float(policy_state.get("suppression_expiry", 0.0) or 0.0),
                    "next_eligible_evaluation_time": float(policy_state.get("next_eligible_evaluation_time", 0.0) or 0.0),
                    "recent_motion_distance_px": float(policy_state.get("recent_motion_distance_px", 0.0) or 0.0),
                    "average_velocity_px_s": float(policy_state.get("average_velocity_px_s", 0.0) or 0.0),
                    "motion_confidence": float(policy_state.get("motion_confidence", 0.0) or 0.0),
                    "stationary_duration_s": float(policy_state.get("stationary_duration_s", 0.0) or 0.0),
                    "motion_window_s": float(policy_state.get("motion_window_s", self._motion_policy_window_s()) or self._motion_policy_window_s()),
                    "motion_allowed": bool(policy_state.get("motion_allowed", True)),
                    "profile_mode": str(policy_state.get("profile_mode", self._motion_policy_mode()) or self._motion_policy_mode()),
                    "history": list(policy_state.get("history", []) or []),
                },
                "shape_score": float(shape_info.get("shape_score", 0.0) or 0.0),
                "semantic_confirmation": {
                    "count": semantic_hits,
                    "required": semantic_required,
                },
                "threat_score": float(getattr(target, "threat_score", 0.0) or 0.0) if target is not None else 0.0,
                "target_velocity": {
                    "vx": float(motion_state.get("vx", 0.0) or 0.0),
                    "vy": float(motion_state.get("vy", 0.0) or 0.0),
                    "speed": float(motion_state.get("speed", 0.0) or 0.0),
                },
                "is_moving": bool(motion_state.get("moving", False)),
                "is_stationary": bool(motion_state.get("stationary", True)),
                "inside_engagement_zone": bool(inside_zone),
                "qualification_status": str(qualification_status),
                "rejection_reason": str(rejection_reason),
                "filter_stages": stages,
            }
            self._forensic_logger.append(record)
            self._publish_mission_event("forensic_detection_evaluation", record)
            overlay_entries.append(
                {
                    "track_id": track_id,
                    "class_name": str(det.class_name),
                    "confidence": float(det.confidence),
                    "bbox": [int(det.bbox[0]), int(det.bbox[1]), int(det.bbox[2]), int(det.bbox[3])],
                    "motion_score": float(motion_state.get("speed", 0.0) or 0.0),
                    "motion_policy_state": str(policy_state.get("state", "TRACKING") or "TRACKING"),
                    "motion_policy_reason": str(policy_state.get("suppression_reason", "") or ""),
                    "shape_score": float(shape_info.get("shape_score", 0.0) or 0.0),
                    "threat_score": float(getattr(target, "threat_score", 0.0) or 0.0) if target is not None else 0.0,
                    "status": str(qualification_status),
                    "rejection_reason": str(rejection_reason),
                    "planner_state": str(getattr(self, "_engage_phase", "") or ""),
                }
            )
        self._forensic_overlay_entries = overlay_entries

    def get_forensic_overlay_entries(self) -> List[Dict[str, Any]]:
        return list(self._forensic_overlay_entries)

    def _log_planner_selection_event(
        self,
        *,
        now: float,
        context: str,
        input_targets: List[TrackedTarget],
        queue: List[EngagementOrder],
    ) -> None:
        ranking = sorted(
            [
                {
                    "track_id": int(t.det.track_id),
                    "class_name": str(t.det.class_name),
                    "threat_score": float(t.threat_score),
                    "selected": bool(any(int(o.target.det.track_id) == int(t.det.track_id) for o in queue)),
                }
                for t in input_targets
            ],
            key=lambda item: float(item.get("threat_score", 0.0)),
            reverse=True,
        )

        selection_chain: List[Dict[str, Any]] = []
        for rank_item in ranking:
            tid = int(rank_item["track_id"])
            queue_match = next((o for o in queue if int(o.target.det.track_id) == tid), None)
            decision = self._find_filter_decision_for_track(tid)
            if queue_match is not None:
                reason = f"selected rank={int(queue_match.rank)}"
            elif decision is not None and not bool(decision.passed):
                reason = f"rejected filter={decision.reason}"
            elif float(rank_item["threat_score"]) < float(getattr(self.cfg.engagement, "min_threat_score", 0.0) or 0.0):
                reason = "below planner threat threshold"
            else:
                reason = "not selected by queue constraints or slew optimization"
            selection_chain.append(
                {
                    "track_id": tid,
                    "class_name": str(rank_item["class_name"]),
                    "threat_score": float(rank_item["threat_score"]),
                    "selected": bool(queue_match is not None),
                    "selection_reason": reason,
                }
            )

        selected_ids = [int(order.target.det.track_id) for order in queue]
        first_selected_threat = float(queue[0].target.threat_score) if queue else 0.0
        highest_candidate_threat = float(ranking[0]["threat_score"]) if ranking else 0.0
        higher_candidate_exists = bool(highest_candidate_threat > first_selected_threat + 1e-9)

        self._forensic_logger.append(
            {
                "event_type": "planner_selection",
                "frame_number": int(self._frame_number),
                "timestamp": float(now),
                "context": str(context),
                "selected_track_ids": selected_ids,
                "selected_order": [
                    {
                        "track_id": int(order.target.det.track_id),
                        "class_name": str(order.target.det.class_name),
                        "threat_score": float(order.target.threat_score),
                        "rank": int(order.rank),
                        "planned_pan": float(order.pan),
                        "planned_tilt": float(order.tilt),
                    }
                    for order in queue
                ],
                "ranking": selection_chain,
                "higher_scored_candidate_than_first_selected": bool(higher_candidate_exists),
                "planner_state": self._current_planner_state(),
            }
        )
        self._publish_mission_event(
            "planner_selection",
            {
                "frame_number": int(self._frame_number),
                "timestamp": float(now),
                "context": str(context),
                "selected_track_ids": selected_ids,
                "selected_order": [
                    {
                        "track_id": int(order.target.det.track_id),
                        "class_name": str(order.target.det.class_name),
                        "threat_score": float(order.target.threat_score),
                        "rank": int(order.rank),
                        "planned_pan": float(order.pan),
                        "planned_tilt": float(order.tilt),
                    }
                    for order in queue
                ],
                "ranking": selection_chain,
                "planner_state": self._current_planner_state(),
            },
        )

    # ------------------------------------------------------------------ #
    # PIR event interface (called by comm when sensor data arrives)
    # ------------------------------------------------------------------ #

    def on_pir_sensor_fired(self, sensor_id: int, timestamp: Optional[float] = None) -> None:
        """Called when a PIR sensor event is received from ESP32."""
        now = timestamp or time.time()
        queue_before = int(self._pir_manager.peek_queue_count())
        self._emit_pir_trace(
            "pir_event_received",
            sensor_id=int(sensor_id),
            event_timestamp=float(now),
            queue_before=queue_before,
            pir_can_trigger_search=bool(self.state != SentryV2State.PAUSED and self.cfg.pir_guard.pir_enabled),
        )

        # Ignore stale/pre-enable PIR hits. Queuing them while PAUSED causes the
        # first enable cycle to consume old events and lunge toward a sensor cue
        # that the operator did not request.
        if self.state == SentryV2State.PAUSED or not self.cfg.pir_guard.pir_enabled:
            reason = "paused" if self.state == SentryV2State.PAUSED else "pir_disabled"
            self._emit_pir_trace("pir_event_blocked", sensor_id=int(sensor_id), reason=reason)
            return

        self._pir_manager.on_pir_event(sensor_id, now)
        queue_after_enqueue = int(self._pir_manager.peek_queue_count())
        self._emit_pir_trace(
            "pir_event_processed_by_manager",
            sensor_id=int(sensor_id),
            queue_before=queue_before,
            queue_after=queue_after_enqueue,
        )

        # PIR is a blind-spot cueing input, not a higher-priority override than a
        # camera-confirmed active engagement. Queue the PIR event immediately, but
        # only convert it into motion outside live ENGAGING tracking.
        if self.state == SentryV2State.ENGAGING:
            self._emit_pir_trace(
                "pir_event_deferred_engaging",
                sensor_id=int(sensor_id),
                reason="engaging_state_blocks_immediate_cue",
                queue_length=int(self._pir_manager.peek_queue_count()),
            )
            return

        cue = self._pir_manager.get_next_cue(now)
        if cue is None:
            self._emit_pir_trace(
                "pir_event_no_cue_available",
                sensor_id=int(sensor_id),
                queue_length=int(self._pir_manager.peek_queue_count()),
            )
            return

        if self.state == SentryV2State.RETURNING:
            self._queue.clear()
            self._queue_index = 0
            self.active_order = None
            self._reset_precision_state()
            if self._log_precision_tuning and self._current_precision_engagement_id:
                self._precision_logger.end_engagement()
                self._current_precision_engagement_id = None
            self._change_state(SentryV2State.GUARDING)

        self._pir_cue_mode = True
        self._pir_cue_sensor_id = int(cue.sensor_id)
        self._pir_cue_pan = cue.cue_pan
        self._pir_cue_tilt = cue.cue_tilt
        self._pir_cue_slew_start = now
        self._pir_scan_mode = False
        self._pir_scan_awaiting_settle = False
        self._pir_settle_start = 0.0
        self._set_pir_note(
            f"PIR cue S{int(cue.sensor_id) + 1} -> pan {float(cue.cue_pan):.1f} tilt {float(cue.cue_tilt):.1f}",
            when=now,
        )
        self._emit_pir_trace(
            "pir_cue_started",
            sensor_id=int(cue.sensor_id),
            cue_pan=float(cue.cue_pan),
            cue_tilt=float(cue.cue_tilt),
            queue_length=int(self._pir_manager.peek_queue_count()),
        )
        self._move_turret(self._pir_cue_pan, self._pir_cue_tilt)

    def _set_sound_alert_note(self, note: str, *, when: Optional[float] = None) -> None:
        self._sound_alert_note = str(note or "")
        self._sound_alert_note_time = float(time.time() if when is None else when)

    def _stationary_release_enabled(self) -> bool:
        return bool(getattr(self.cfg.engagement, "stationary_release_enabled", True))

    def _stationary_release_motion_threshold_px(self, det: DetectedObject) -> float:
        configured_px = float(getattr(self.cfg.engagement, "stationary_release_motion_px", 36.0) or 36.0)
        bbox = tuple(int(v) for v in det.bbox)
        diag_px = ((float(bbox[2]) ** 2) + (float(bbox[3]) ** 2)) ** 0.5
        adaptive_px = max(configured_px, min(140.0, diag_px * 0.45))
        return float(max(12.0, adaptive_px))

    def _note_stationary_release_fire(self, det: DetectedObject, now: float) -> None:
        if not self._stationary_release_enabled():
            return
        track_id = int(det.track_id)
        center = (float(det.center_x), float(det.center_y))
        if self._stationary_release_track_id != track_id or self._stationary_release_anchor_center is None:
            self._stationary_release_track_id = track_id
            self._stationary_release_anchor_center = center
            self._stationary_release_since = now
            self._stationary_release_fire_cycles = 1
            self._stationary_release_suppress_until = 0.0
            return

        threshold_px = self._stationary_release_motion_threshold_px(det)
        anchor_x, anchor_y = self._stationary_release_anchor_center
        movement_px = ((center[0] - anchor_x) ** 2 + (center[1] - anchor_y) ** 2) ** 0.5
        if movement_px <= threshold_px:
            self._stationary_release_fire_cycles += 1
            self._stationary_release_anchor_center = (
                (anchor_x * 0.82) + (center[0] * 0.18),
                (anchor_y * 0.82) + (center[1] * 0.18),
            )
            return

        # Target moved materially; treat as a fresh engagement track.
        self._stationary_release_anchor_center = center
        self._stationary_release_since = now
        self._stationary_release_fire_cycles = 1
        self._stationary_release_suppress_until = 0.0

    def _apply_stationary_release_protocol(self, targets: List[TrackedTarget], now: float) -> List[TrackedTarget]:
        if not self._stationary_release_enabled() or not targets:
            return targets

        lead = targets[0]
        lead_track_id = int(lead.det.track_id)
        if self._stationary_release_track_id != lead_track_id:
            return targets
        if self._stationary_release_anchor_center is None:
            return targets

        center = (float(lead.det.center_x), float(lead.det.center_y))
        threshold_px = self._stationary_release_motion_threshold_px(lead.det)
        anchor_x, anchor_y = self._stationary_release_anchor_center
        movement_px = ((center[0] - anchor_x) ** 2 + (center[1] - anchor_y) ** 2) ** 0.5

        if movement_px > threshold_px:
            # Lead target is no longer stationary enough to suppress.
            self._stationary_release_anchor_center = center
            self._stationary_release_since = now
            self._stationary_release_fire_cycles = 0
            self._stationary_release_suppress_until = 0.0
            return targets

        # Smooth anchor in place so small detector jitter does not collapse dwell time.
        self._stationary_release_anchor_center = (
            (anchor_x * 0.88) + (center[0] * 0.12),
            (anchor_y * 0.88) + (center[1] * 0.12),
        )

        if self._stationary_release_suppress_until > now:
            self._last_reacquire_note = (
                f"stationary release active t{lead_track_id} ({self._stationary_release_suppress_until - now:.1f}s)"
            )
            return [t for t in targets if int(t.det.track_id) != lead_track_id]

        min_cycles = int(max(1, int(getattr(self.cfg.engagement, "stationary_release_min_fire_cycles", 3) or 3)))
        hold_s = float(max(0.5, float(getattr(self.cfg.engagement, "stationary_release_hold_s", 8.0) or 8.0)))
        dwell_s = max(0.0, now - float(self._stationary_release_since or now))
        if self._stationary_release_fire_cycles >= min_cycles and dwell_s >= hold_s:
            suppress_s = float(max(2.0, float(getattr(self.cfg.engagement, "stationary_release_suppress_s", 10.0) or 10.0)))
            self._stationary_release_suppress_until = now + suppress_s
            self._last_reacquire_note = (
                f"stationary release t{lead_track_id}: {self._stationary_release_fire_cycles} fire cycles, "
                f"{dwell_s:.1f}s dwell"
            )
            self._set_pir_note(
                f"Static target released for {suppress_s:.0f}s (track {lead_track_id})",
                when=now,
            )
            return [t for t in targets if int(t.det.track_id) != lead_track_id]

        return targets

    def _should_force_stationary_release_in_single_target(
        self,
        order: EngagementOrder,
        tracked_target: Optional[TrackedTarget],
        now: float,
    ) -> bool:
        """Return True when a single-target engage loop should release a static target."""
        if not self._stationary_release_enabled() or tracked_target is None:
            return False

        det = tracked_target.det
        track_id = int(det.track_id)
        if self._stationary_release_track_id != track_id:
            return False
        if self._stationary_release_anchor_center is None:
            return False

        if self._stationary_release_suppress_until > now:
            self._last_reacquire_note = (
                f"stationary release active t{track_id} ({self._stationary_release_suppress_until - now:.1f}s)"
            )
            return True

        center = (float(det.center_x), float(det.center_y))
        threshold_px = self._stationary_release_motion_threshold_px(det)
        anchor_x, anchor_y = self._stationary_release_anchor_center
        movement_px = ((center[0] - anchor_x) ** 2 + (center[1] - anchor_y) ** 2) ** 0.5
        if movement_px > threshold_px:
            return False

        min_cycles = int(max(1, int(getattr(self.cfg.engagement, "stationary_release_min_fire_cycles", 3) or 3)))
        hold_s = float(max(0.5, float(getattr(self.cfg.engagement, "stationary_release_hold_s", 8.0) or 8.0)))
        dwell_s = max(0.0, now - float(self._stationary_release_since or now))
        if self._stationary_release_fire_cycles < min_cycles or dwell_s < hold_s:
            return False

        suppress_s = float(max(2.0, float(getattr(self.cfg.engagement, "stationary_release_suppress_s", 10.0) or 10.0)))
        self._stationary_release_suppress_until = now + suppress_s
        self._last_reacquire_note = (
            f"stationary release t{track_id}: {self._stationary_release_fire_cycles} fire cycles, {dwell_s:.1f}s dwell"
        )
        self._set_pir_note(
            f"Static target released for {suppress_s:.0f}s (track {track_id})",
            when=now,
        )
        return True

    def on_sound_anomaly_detected(
        self,
        level_db: float,
        baseline_db: float,
        timestamp: Optional[float] = None,
    ) -> None:
        """Queue a non-interruptive acoustic alert workflow."""
        now = float(timestamp or time.time())
        cfg = getattr(self.cfg, "acoustic_guard", None)
        if self.state == SentryV2State.PAUSED or cfg is None or not bool(getattr(cfg, "enabled", False)):
            return

        cooldown_s = max(0.5, float(getattr(cfg, "event_cooldown_s", 8.0) or 8.0))
        if self._sound_alert_last_started > 0.0 and (now - self._sound_alert_last_started) < cooldown_s:
            return

        # Keep only the strongest pending event in a burst.
        if self._sound_alert_pending:
            if float(level_db) <= float(self._sound_alert_pending_level_db):
                return
        self._sound_alert_pending = True
        self._sound_alert_pending_since = now
        self._sound_alert_pending_level_db = float(level_db)
        self._sound_alert_pending_baseline_db = float(baseline_db)
        self._sound_alert_deferred_until_guard_clear = self.state in {SentryV2State.ENGAGING, SentryV2State.RETURNING}
        self._set_sound_alert_note(
            f"Acoustic anomaly queued ({float(level_db):.1f}dB vs {float(baseline_db):.1f}dB baseline)",
            when=now,
        )

    def _defer_sound_alert_until_guard_clear(self, now: float) -> None:
        if not self._sound_alert_active:
            return
        self._cancel_sound_alert(reason="Acoustic alert deferred: visual target acquired")
        self._sound_alert_pending = True
        self._sound_alert_pending_since = max(float(now), float(self._sound_alert_pending_since or 0.0))
        self._sound_alert_deferred_until_guard_clear = True
        self._set_sound_alert_note("Acoustic alert deferred until guard is clear", when=now)

    def _cancel_sound_alert(self, *, reason: str = "") -> None:
        self._sound_alert_active = False
        self._sound_alert_phase = ""
        self._sound_alert_phase_started = 0.0
        self._sound_alert_last_update = 0.0
        self._sound_alert_points = []
        self._sound_alert_point_index = 0
        self._sound_alert_step_started = False
        self._sound_alert_step_arrived_time = 0.0
        self._sound_alert_sweep_stage = 0
        if reason:
            self._set_sound_alert_note(reason)

    def _start_sound_alert_sequence(self, now: float) -> None:
        self._sound_alert_pending = False
        self._sound_alert_pending_since = 0.0
        self._sound_alert_active = True
        self._sound_alert_deferred_until_guard_clear = False
        self._sound_alert_phase = "initial_search"
        self._sound_alert_phase_started = now
        self._sound_alert_last_update = now
        self._sound_alert_points = self._build_sound_initial_points()
        self._sound_alert_point_index = 0
        self._sound_alert_step_started = False
        self._sound_alert_step_arrived_time = 0.0
        self._sound_alert_sweep_stage = 0
        self._sound_alert_last_started = now
        self._set_sound_alert_note("Acoustic alert: initial search pattern")

    def _build_sound_initial_points(self) -> List[Tuple[float, float]]:
        guard_tilt = self._clamp_tilt(float(self.cfg.guard.guard_tilt))
        guard_pan = float(self.cfg.guard.guard_pan)
        offset = max(5.0, float(getattr(self.cfg.acoustic_guard, "quick_lr_offset_deg", 22.0) or 22.0))
        # Quick-search pattern anchored to guard pan: left -> center -> right.
        raw_points = (guard_pan - offset, guard_pan, guard_pan + offset)
        points: List[Tuple[float, float]] = []
        for pan in raw_points:
            points.append((self._clamp_pan(float(pan)), guard_tilt))
        return points

    def _sound_alert_hold_s(self, attr: str, fallback: float) -> float:
        cfg = getattr(self.cfg, "acoustic_guard", None)
        if cfg is None:
            return float(fallback)
        return max(0.05, float(getattr(cfg, attr, fallback) or fallback))

    def _update_sound_alert_sequence(self, now: float) -> None:
        if not self._sound_alert_active:
            return

        dt = 0.0 if self._sound_alert_last_update <= 0.0 else max(0.0, now - self._sound_alert_last_update)
        self._sound_alert_last_update = now

        phase = str(self._sound_alert_phase or "")
        if phase == "initial_search":
            if self._sound_alert_point_index >= len(self._sound_alert_points):
                self._sound_alert_phase = "sweep"
                self._sound_alert_sweep_stage = 0
                self._sound_alert_phase_started = now
                self._set_sound_alert_note("Acoustic alert: secondary sweep scan", when=now)
                return

            target_pan, target_tilt = self._sound_alert_points[self._sound_alert_point_index]
            quick_speed = max(45.0, float(getattr(self.cfg.guard, "sweep_speed", 22.0)) * 2.8)
            if not self._sound_alert_step_started:
                self._sound_alert_step_started = True
                self._sound_alert_phase_started = now
                self._sound_alert_step_arrived_time = 0.0
                self._set_sound_alert_note(
                    f"Acoustic alert: quick search {self._sound_alert_point_index + 1}/{len(self._sound_alert_points)} -> pan {target_pan:.1f}",
                    when=now,
                )
            # If already at this waypoint, dwell before advancing.
            if self._sound_alert_step_arrived_time > 0.0:
                hold_s = self._sound_alert_hold_s("quick_lr_hold_s", 0.26)
                if (now - self._sound_alert_step_arrived_time) >= hold_s:
                    self._sound_alert_point_index += 1
                    self._sound_alert_step_started = False
                    self._sound_alert_step_arrived_time = 0.0
                return
            arrived = self._patrol_move_toward(target_pan, target_tilt, quick_speed, dt)
            if arrived:
                self._sound_alert_step_arrived_time = now
            return

        if phase == "sweep":
            pan_min, pan_max = sorted((float(self.cfg.guard.sweep_pan_min), float(self.cfg.guard.sweep_pan_max)))
            if abs(pan_max - pan_min) < 1.0:
                pan_min, pan_max = sorted((float(self.cfg.guard.pan_min), float(self.cfg.guard.pan_max)))
            sweep_speed = max(2.0, float(getattr(self.cfg.acoustic_guard, "sweep_speed_dps", self.cfg.guard.sweep_speed)))
            base_tilt = float(self.cfg.guard.sweep_tilt)
            tilt_span = 7.0
            tilt_low = self._clamp_tilt(base_tilt - tilt_span)
            tilt_high = self._clamp_tilt(base_tilt + tilt_span)
            if self._sound_alert_sweep_stage == 0:
                arrived = self._patrol_move_toward(pan_min, tilt_low, sweep_speed, dt)
                if arrived:
                    self._sound_alert_sweep_stage = 1
                return
            if self._sound_alert_sweep_stage == 1:
                arrived = self._patrol_move_toward(pan_max, tilt_high, sweep_speed, dt)
                if arrived:
                    self._sound_alert_sweep_stage = 2
                return
            if self._sound_alert_sweep_stage == 2:
                arrived = self._patrol_move_toward(pan_min, base_tilt, sweep_speed, dt)
                if arrived:
                    mode = int(getattr(self.cfg.guard, "guard_mode", 0) or 0)
                    if mode == 0:
                        self._move_turret(self.cfg.guard.guard_pan, self.cfg.guard.guard_tilt)
                    self._patrol_initialized = False
                    self._cancel_sound_alert(reason="Acoustic alert: clear, resume guard")
                return

        self._cancel_sound_alert(reason="Acoustic alert reset")

    # ------------------------------------------------------------------ #
    # GUARDING state
    # ------------------------------------------------------------------ #

    def _update_guarding(self, targets: List[TrackedTarget], now: float) -> None:
        """
        In GUARDING: patrol or hold position, and watch for threats.
        If scoreable threats exist above threshold, plan engagement.
        Also handles PIR sensor cues for blind-spot detection.
        """
        motion_policy_ids = set(int(track_id) for track_id in list(getattr(self, "_last_motion_policy_engageable_ids", []) or []))
        targets_for_engagement = [target for target in self._apply_stationary_release_protocol(targets, now) if int(target.det.track_id) in motion_policy_ids]

        # Check for threats first — engagement always takes priority
        if targets_for_engagement:
            if now - self._last_engage_time >= self.cfg.engagement.cycle_cooldown:
                # Apply scene-memory class-prior as a soft tiebreaker so classes
                # observed more often in this session are preferred when threat
                # scores are similar.  The bias is capped at 20 % to avoid
                # overriding a genuine threat-score difference.
                targets_for_engagement = self._scene_memory.order_candidates_by_prior(
                    targets_for_engagement, now
                )
                queue = self._planner.plan(targets_for_engagement, self.current_pan, self.current_tilt)
                if queue:
                    self._log_planner_selection_event(
                        now=now,
                        context="guarding_primary",
                        input_targets=list(targets_for_engagement),
                        queue=list(queue),
                    )
                    # Log engagement promotion for primary target
                    if self._log_autotracking and queue:
                        first_target = queue[0].target
                        self._autotrack_logger.log_engagement_promoted(
                            target_id=first_target.target_id,
                            class_name=first_target.det.class_name,
                            threat_score=first_target.threat_score,
                            queue_position=0,
                            notes=f"yolo_detection -> engagement, {len(queue)} in queue",
                        )
                    
                    self._queue = queue
                    self.last_queue = queue
                    self._queue_index = 0
                    self._patrol_initialized = False  # reset patrol on re-entry
                    self._reset_precision_state()
                    if self._sound_alert_active:
                        self._defer_sound_alert_until_guard_clear(now)
                    self._change_state(SentryV2State.ENGAGING)
                    first = self._queue[0]
                    self.active_order = first
                    self._remember_active_target(first.target.det)
                    self._start_order_engagement(first, now)
                    # Target found — complete active cue but preserve queued
                    # events so other sensor zones are hunted after this engage.
                    self._pir_manager.complete_active_cue()
                    self._pir_cue_mode = False
                    return

        # Check for PIR cues if enabled and no threats
        if self.cfg.pir_guard.pir_enabled and not self._pir_cue_mode:
            cue = self._pir_manager.get_next_cue(now)
            if cue is not None:
                # Start PIR cue pursuit
                self._pir_cue_mode = True
                self._pir_cue_sensor_id = int(cue.sensor_id)
                self._pir_cue_pan = cue.cue_pan
                self._pir_cue_tilt = cue.cue_tilt
                self._pir_cue_slew_start = now
                self._pir_scan_mode = False
                self._pir_scan_awaiting_settle = False
                self._pir_settle_start = 0.0
                self._set_pir_note(
                    f"PIR cue S{int(cue.sensor_id) + 1} -> pan {float(cue.cue_pan):.1f} tilt {float(cue.cue_tilt):.1f}",
                    when=now,
                )
                self._emit_pir_trace(
                    "pir_cue_started_from_guarding",
                    sensor_id=int(cue.sensor_id),
                    cue_pan=float(cue.cue_pan),
                    cue_tilt=float(cue.cue_tilt),
                    queue_length=int(self._pir_manager.peek_queue_count()),
                )
                self._move_turret(self._pir_cue_pan, self._pir_cue_tilt)
                return
        
        # Handle active PIR cue mode
        if self._pir_cue_mode:
            if self._pir_scan_mode:
                # In adaptive scan mode
                self._update_pir_scan(targets, now)
            else:
                # Waiting for confirmation at cue point
                self._update_pir_confirmation(targets, now)
            return

        acoustic_cfg = getattr(self.cfg, "acoustic_guard", None)
        if acoustic_cfg is not None:
            ttl_s = max(1.0, float(getattr(acoustic_cfg, "queue_ttl_s", 14.0) or 14.0))
            if (
                self._sound_alert_pending
                and not self._sound_alert_deferred_until_guard_clear
                and self._sound_alert_pending_since > 0.0
                and (now - self._sound_alert_pending_since) > ttl_s
            ):
                self._sound_alert_pending = False
                self._sound_alert_pending_since = 0.0
                self._set_sound_alert_note("Acoustic alert expired before execution", when=now)

            if bool(getattr(acoustic_cfg, "enabled", False)):
                if self._sound_alert_active:
                    self._update_sound_alert_sequence(now)
                    return
                if self._sound_alert_pending:
                    self._start_sound_alert_sequence(now)
                    return

        # No threats and no PIR cues — behaviour + patrol logic
        behaviour = self.cfg.guard.sentry_behaviour
        if behaviour == 0:  # Watchful: track any mover, only engage valid targets
            if not self._update_watchful_tracking(now):
                self._update_patrol(now)
        elif behaviour == 1:  # Curious Guard: glance at movers, only engage valid targets
            if not self._update_curious_glance(now):
                self._update_patrol(now)
        else:  # Strict (2): only move for valid targets
            self._update_patrol(now)

    def _update_watchful_tracking(self, now: float) -> bool:
        """Watchful mode: softly track the most prominent mover when no valid targets.

        Returns True if a tracking move was issued (caller should suppress patrol).
        """
        WATCHFUL_MOVE_INTERVAL = 0.25  # max 4 move commands per second
        WATCHFUL_DEADZONE_DEG = 0.9
        WATCHFUL_MAX_STEP_DEG = 4.5
        raw = self.last_detections
        if not raw:
            return False
        if now - self._behaviour_watchful_last_move < WATCHFUL_MOVE_INTERVAL:
            # Let patrol continue between watchful micro-tracks instead of
            # freezing when noisy raw detections keep arriving.
            return False
        # Pick the detection with the largest bbox area (most prominent mover)
        best = max(
            raw,
            key=lambda d: (d.bbox[2] * d.bbox[3]) if (d.bbox and len(d.bbox) >= 4) else 0.0,
        )
        target_pan, target_tilt = self._planner.aim_from_normalized_center(
            float(best.norm_cx), float(best.norm_cy),
            self.current_pan, self.current_tilt,
        )
        dp = float(target_pan) - float(self.current_pan)
        dtilt = float(target_tilt) - float(self.current_tilt)
        max_axis_delta = max(abs(dp), abs(dtilt))
        if max_axis_delta < WATCHFUL_DEADZONE_DEG:
            return False
        if max_axis_delta > WATCHFUL_MAX_STEP_DEG:
            ratio = WATCHFUL_MAX_STEP_DEG / max_axis_delta
            target_pan = float(self.current_pan) + (dp * ratio)
            target_tilt = float(self.current_tilt) + (dtilt * ratio)
        self._behaviour_watchful_last_move = now
        self._move_turret(target_pan, target_tilt)
        return True

    def _update_curious_glance(self, now: float) -> bool:
        """Curious Guard mode: brief periodic glance at non-qualifying movers.

        Returns True if a glance is currently active (caller should suppress patrol).
        """
        CURIOUS_MAX_GLANCE_STEP_DEG = 8.0
        g = self.cfg.guard
        if self._behaviour_curious_glance_active:
            # Already glancing — check if dwell time is up
            if now - self._behaviour_curious_glance_start >= g.curious_glance_dwell_s:
                # Dwell complete — cancel glance, return to guard home
                self._behaviour_curious_glance_active = False
                self._behaviour_curious_last_glance = now
                self._move_turret(g.guard_pan, g.guard_tilt)
            return True  # suppress patrol while glancing

        # Not glancing — check if enough time has passed and there are raw detections
        if now - self._behaviour_curious_last_glance < g.curious_glance_interval_s:
            return False  # too soon since last glance

        raw = self.last_detections
        if not raw:
            return False

        # Pick the most prominent unqualified detection
        best = max(
            raw,
            key=lambda d: (d.bbox[2] * d.bbox[3]) if (d.bbox and len(d.bbox) >= 4) else 0.0,
        )
        glance_pan, glance_tilt = self._planner.aim_from_normalized_center(
            float(best.norm_cx), float(best.norm_cy),
            self.current_pan, self.current_tilt,
        )
        dp = float(glance_pan) - float(self.current_pan)
        dtilt = float(glance_tilt) - float(self.current_tilt)
        max_axis_delta = max(abs(dp), abs(dtilt))
        if max_axis_delta > CURIOUS_MAX_GLANCE_STEP_DEG:
            ratio = CURIOUS_MAX_GLANCE_STEP_DEG / max_axis_delta
            glance_pan = float(self.current_pan) + (dp * ratio)
            glance_tilt = float(self.current_tilt) + (dtilt * ratio)
        self._behaviour_curious_glance_active = True
        self._behaviour_curious_glance_start = now
        self._behaviour_curious_glance_pan = glance_pan
        self._behaviour_curious_glance_tilt = glance_tilt
        self._move_turret(glance_pan, glance_tilt)
        return True

    def _update_pir_confirmation(self, targets: List[TrackedTarget], now: float) -> None:
        """Wait for camera to confirm a target at the PIR cue point."""
        # Hold very briefly at the cue center, then move immediately into a
        # local hunt around that PIR zone if vision still sees nothing.
        settle_time = self._pir_cue_hold_time()
        slew_elapsed = now - self._pir_cue_slew_start
        
        if slew_elapsed < settle_time:
            return  # Still slewing
        
        # Check if we found targets above threshold
        if targets:
            # Found a target — complete cue (preserve queue) and engage.
            active_sensor_id = int(getattr(self, "_pir_cue_sensor_id", -1))
            self._pir_cue_mode = False
            self._pir_cue_sensor_id = -1
            self._pir_manager.complete_active_cue()
            if active_sensor_id >= 0:
                self._set_pir_note(f"PIR confirmed target S{active_sensor_id + 1} -> engage", when=now)
            # Trigger engagement
            if now - self._last_engage_time >= self.cfg.engagement.cycle_cooldown:
                queue = self._planner.plan(targets, self.current_pan, self.current_tilt)
                if queue:
                    self._log_planner_selection_event(
                        now=now,
                        context="pir_confirmation",
                        input_targets=list(targets),
                        queue=list(queue),
                    )
                    self._queue = queue
                    self.last_queue = queue
                    self._queue_index = 0
                    self._patrol_initialized = False
                    self._reset_precision_state()
                    self._change_state(SentryV2State.ENGAGING)
                    first = self._queue[0]
                    self.active_order = first
                    self._remember_active_target(first.target.det)
                    self._start_order_engagement(first, now)
                    self._emit_pir_trace(
                        "pir_consumed_target_confirmed_engage",
                        sensor_id=active_sensor_id,
                        action_taken="target_acquisition_engage",
                        queue_length=int(self._pir_manager.peek_queue_count()),
                    )
            return
        
        # No target confirmed at cue point
        if self.cfg.pir_guard.scan_on_no_detect:
            # Start a localized hunt around the PIR cue point first, then widen.
            self._pir_scan_mode = True
            self._pir_manager.start_scan(
                self._pir_cue_pan,
                self._pir_cue_tilt,
                sensor_id=self._pir_cue_sensor_id,
                search_style=getattr(self.cfg.pir_guard, "search_style", "hunting"),
            )
            total_steps = max(1, len(getattr(self._pir_manager, "_scan_points", []) or []))
            active_sensor_id = int(getattr(self, "_pir_cue_sensor_id", -1))
            sensor_text = f" S{active_sensor_id + 1}" if active_sensor_id >= 0 else ""
            self._set_pir_note(f"PIR search start{sensor_text} ({total_steps} points)", when=now)
            self._emit_pir_trace(
                "pir_search_started_no_detect",
                sensor_id=active_sensor_id,
                total_steps=int(total_steps),
                action_taken="scan",
                queue_length=int(self._pir_manager.peek_queue_count()),
            )
            next_point = self._pir_manager.get_next_scan_point()
            if next_point is not None:
                # Apply organic jitter on the very first scan move too
                jitter_rng = random.Random(int(now * 1000) % 7919)
                scan_pan = self._clamp_pan(next_point[0] + jitter_rng.gauss(0.0, 0.40))
                scan_tilt = self._clamp_tilt(next_point[1] + jitter_rng.gauss(0.0, 0.25))
                self._move_turret(scan_pan, scan_tilt)
                step_index = max(1, int(getattr(self._pir_manager, "_scan_index", 0) or 1))
                self._set_pir_note(
                    f"PIR search step{sensor_text} {step_index}/{total_steps} -> pan {scan_pan:.1f} tilt {scan_tilt:.1f}",
                    when=now,
                )
                self._pir_scan_awaiting_settle = True
                self._pir_settle_start = now
            else:
                self._emit_pir_trace(
                    "pir_search_no_points",
                    sensor_id=active_sensor_id,
                    action_taken="no_action_return_home",
                    reason="scan_grid_empty",
                    queue_length=int(self._pir_manager.peek_queue_count()),
                )
                self._finish_pir_no_target()
        else:
            # No search enabled, finish this cue and fall back to guard/patrol.
            self._emit_pir_trace(
                "pir_no_detect_scan_disabled",
                sensor_id=int(getattr(self, "_pir_cue_sensor_id", -1)),
                action_taken="no_action_return_home",
                reason="scan_on_no_detect_disabled",
                queue_length=int(self._pir_manager.peek_queue_count()),
            )
            self._finish_pir_no_target()

    def _update_pir_scan(self, targets: List[TrackedTarget], now: float) -> None:
        """Run adaptive scan grid at PIR cue location."""
        # If we found targets during scan, engage them
        if targets:
            active_sensor_id = int(getattr(self, "_pir_cue_sensor_id", -1))
            self._pir_cue_mode = False
            self._pir_cue_sensor_id = -1
            self._pir_scan_mode = False
            self._pir_manager.complete_active_cue()
            if active_sensor_id >= 0:
                self._set_pir_note(f"PIR confirmed target S{active_sensor_id + 1} -> engage", when=now)
            if now - self._last_engage_time >= self.cfg.engagement.cycle_cooldown:
                queue = self._planner.plan(targets, self.current_pan, self.current_tilt)
                if queue:
                    self._log_planner_selection_event(
                        now=now,
                        context="pir_scan",
                        input_targets=list(targets),
                        queue=list(queue),
                    )
                    self._queue = queue
                    self.last_queue = queue
                    self._queue_index = 0
                    self._patrol_initialized = False
                    self._reset_precision_state()
                    self._change_state(SentryV2State.ENGAGING)
                    first = self._queue[0]
                    self.active_order = first
                    self._remember_active_target(first.target.det)
                    self._start_order_engagement(first, now)
                    self._emit_pir_trace(
                        "pir_scan_consumed_target_confirmed_engage",
                        sensor_id=active_sensor_id,
                        action_taken="target_acquisition_engage",
                        queue_length=int(self._pir_manager.peek_queue_count()),
                    )
            return
        
        # Wait for servo settle before moving to next scan point
        if self._pir_scan_awaiting_settle:
            settle_time = self._pir_scan_settle_time()
            if now - self._pir_settle_start < settle_time:
                return  # Still settling
            self._pir_scan_awaiting_settle = False
        
        # Move to next scan point
        next_point = self._pir_manager.get_next_scan_point()
        if next_point is not None:
            # Add subtle organic jitter for natural-looking PIR hunt movement
            jitter_rng = random.Random(int(now * 1000) % 9973)
            jitter_pan = jitter_rng.gauss(0.0, 0.40)
            jitter_tilt = jitter_rng.gauss(0.0, 0.25)
            scan_pan = self._clamp_pan(next_point[0] + jitter_pan)
            scan_tilt = self._clamp_tilt(next_point[1] + jitter_tilt)
            self._move_turret(scan_pan, scan_tilt)
            active_sensor_id = int(getattr(self, "_pir_cue_sensor_id", -1))
            sensor_text = f" S{active_sensor_id + 1}" if active_sensor_id >= 0 else ""
            step_index = max(1, int(getattr(self._pir_manager, "_scan_index", 0) or 1))
            total_steps = max(1, len(getattr(self._pir_manager, "_scan_points", []) or []))
            self._set_pir_note(
                f"PIR search step{sensor_text} {step_index}/{total_steps} -> pan {scan_pan:.1f} tilt {scan_tilt:.1f}",
                when=now,
            )
            self._emit_pir_trace(
                "pir_scan_step",
                sensor_id=active_sensor_id,
                step_index=int(step_index),
                total_steps=int(total_steps),
                scan_pan=float(scan_pan),
                scan_tilt=float(scan_tilt),
                queue_length=int(self._pir_manager.peek_queue_count()),
            )
            self._pir_scan_awaiting_settle = True
            self._pir_settle_start = now
        else:
            # Search complete with no target. Explicitly return home so a static
            # guard configuration cannot remain parked at the final hunt point.
            self._emit_pir_trace(
                "pir_scan_exhausted_no_target",
                sensor_id=int(getattr(self, "_pir_cue_sensor_id", -1)),
                action_taken="no_action_return_home",
                reason="scan_exhausted",
                queue_length=int(self._pir_manager.peek_queue_count()),
            )
            self._finish_pir_no_target()

    def _pir_scan_settle_time(self) -> float:
        style = self._normalized_search_style(getattr(self.cfg.pir_guard, "search_style", "hunting"))
        speed = float(max(1.0, self.cfg.pir_guard.scan_speed))
        base = 0.10 if style == "fast_reacquire" else 0.12
        return float(min(0.70, max(base, (2.2 / speed) + base)))

    # ------------------------------------------------------------------ #
    # ENGAGING state
    # ------------------------------------------------------------------ #

    def _update_engaging(self, now: float) -> None:
        """
        Work through the engagement queue:
          aim → (precision refinement) → fire → inter-target cooldown → next
        """
        if self._queue_index >= len(self._queue):
            # All targets engaged — start returning.
            if self._log_precision_tuning and self._current_precision_engagement_id:
                self._precision_logger.end_engagement()
                self._current_precision_engagement_id = None
            self._start_return_to_guard(now)
            return

        order = self._queue[self._queue_index]
        self.active_order = order
        elapsed = now - self._phase_start

        if self._engage_phase == "aim":
            self._last_err_pan_deg = 0.0
            self._last_err_tilt_deg = 0.0
            # Scale acquire/settle time with engagement speed — fast presets
            # still get a real startup settle window before precision begins.
            speed_ratio = float(max(10, min(100, int(getattr(self.cfg.engagement, "engagement_speed", 80) or 80))) - 10) / 90.0
            aim_settle_time = max(0.02, 0.20 * (1.0 - speed_ratio * 0.92))
            if self._acquire_phase_ready(now, aim_settle_time):
                target = self._find_active_target(order)
                if target is not None:
                    raw_err_pan, raw_err_tilt = self._compute_target_angle_error(target.det)
                    if self._needs_additional_coarse_acquire(raw_err_pan, raw_err_tilt):
                        self._phase_start = now
                        self._issue_coarse_acquire_move(order, target=target, now=now)
                        return
                if self.cfg.engagement.precision_aim_enabled:
                    self._enter_precision_phase(now, order)
                else:
                    self._begin_fire(order, now)

        elif self._engage_phase == "precision":
            settle = self.cfg.engagement.precision_settle_time
            target = self._find_active_target(order)
            target_det = target.det if target is not None else None
            if target_det is None:
                if self._target_lost_since <= 0.0:
                    self._target_lost_since = now
                    self._loss_recovery_retry_count = 0
                    if self._loss_recovery_enabled():
                        self._start_loss_recovery(now)
                if self._loss_recovery_enabled():
                    self._update_loss_recovery(now)
                # Wide reacquire: if scan panned to where YOLO sees a qualifying
                # target of the correct class anywhere in frame, re-engage immediately
                # rather than waiting for the strict pixel-proximity check.
                # Use a relaxed threshold matching _has_visible_reacquire_candidate so
                # a target that paused loss-recovery (score near but below min_score,
                # or high persistence) can still be re-engaged here instead of waiting
                # out the full target_loss_timeout (a visible-target freeze of up to 2s).
                if self._loss_recovery_phase and self.last_targets:
                    anchor_class = str(getattr(self, "_active_target_last_class", "") or "").strip().lower()
                    min_score = self.cfg.engagement.min_threat_score
                    relaxed_reacquire_score = max(0.20, min_score * 0.65)
                    candidates = [
                        t for t in self.last_targets
                        if t.threat_score >= relaxed_reacquire_score
                        and (not anchor_class or str(t.det.class_name or "").strip().lower() == anchor_class)
                    ]
                    if candidates:
                        best = max(candidates, key=lambda t: (t.threat_score, float(t.persistence)))
                        old_id = int(order.target.det.track_id)
                        order.target = best
                        self._remember_active_target(best.det, target=best)
                        self._target_lost_since = 0.0
                        self._reset_loss_recovery_state()
                        self._last_reacquire_note = f"scan reacquire {old_id}->{int(best.det.track_id)}"
                        self._last_reacquire_time = now
                        return  # re-engage on next frame
                if (now - self._target_lost_since) >= self.cfg.engagement.target_loss_timeout:
                    if self._should_retry_loss_recovery():
                        self._restart_loss_recovery(now)
                        return
                    self._advance_queue(now)
                return
            self._target_lost_since = 0.0
            self._reset_loss_recovery_state()

            if not self._planner.target_is_reachable(target, self.current_pan, self.current_tilt):
                self._last_reacquire_note = (
                    f"target released: servo envelope exceeded for track {int(target.det.track_id)}"
                )
                self._advance_queue(now)
                return

            aim_err_pan, aim_err_tilt = self._compute_tracking_angle_error(target, now, for_fire=False)
            corr_pan, corr_tilt, lock_pan, lock_tilt = self._compute_visual_servo_correction(
                aim_err_pan,
                aim_err_tilt,
                use_fire_limits=False,
            )
            self._update_error_rates(aim_err_pan, aim_err_tilt, now)
            self._last_err_pan_deg = float(aim_err_pan)
            self._last_err_tilt_deg = float(aim_err_tilt)
            self._record_active_target_solution(target, now, aim_err_pan, aim_err_tilt)

            if self._log_precision_tuning:
                eng = self.cfg.engagement
                target_pan = self.current_pan + aim_err_pan
                target_tilt = self.current_tilt + aim_err_tilt
                deadzone_pan = float(eng.precision_deadzone_pan_deg)
                deadzone_tilt = float(eng.precision_deadzone_tilt_deg)
                within_deadzone = abs(lock_pan) <= deadzone_pan and abs(lock_tilt) <= deadzone_tilt
                self._safe_log_precision_frame(
                    current_pan=self.current_pan,
                    current_tilt=self.current_tilt,
                    target_pan=target_pan,
                    target_tilt=target_tilt,
                    pid_p_pan=self._last_pid_p_pan,
                    pid_i_pan=self._last_pid_i_pan,
                    pid_d_pan=self._last_pid_d_pan,
                    pid_p_tilt=self._last_pid_p_tilt,
                    pid_i_tilt=self._last_pid_i_tilt,
                    pid_d_tilt=self._last_pid_d_tilt,
                    move_cmd_pan=corr_pan,
                    move_cmd_tilt=corr_tilt,
                    within_deadzone=within_deadzone,
                    deadzone_pan=deadzone_pan,
                    deadzone_tilt=deadzone_tilt,
                    phase="precision",
                    fired=False,
                )

            # Log autotracking correction frame
            if self._log_autotracking and target is not None:
                self._autotrack_logger.log_tracking_frame(
                    target_id=target.target_id,
                    class_name=target.det.class_name,
                    error_pan=aim_err_pan,
                    error_tilt=aim_err_tilt,
                    pid_p_pan=self._last_pid_p_pan,
                    pid_i_pan=self._last_pid_i_pan,
                    pid_d_pan=self._last_pid_d_pan,
                    pid_p_tilt=self._last_pid_p_tilt,
                    pid_i_tilt=self._last_pid_i_tilt,
                    pid_d_tilt=self._last_pid_d_tilt,
                    move_cmd_pan=corr_pan,
                    move_cmd_tilt=corr_tilt,
                    aim_lock_pan=self._has_aim_lock(lock_pan, 0.0),
                    aim_lock_tilt=self._has_aim_lock(0.0, lock_tilt),
                    aim_lock_frames=self._aim_lock_frames,
                    phase="precision",
                    notes=f"lock={self._has_aim_lock(lock_pan, lock_tilt)}",
                )

            if self._has_aim_lock(lock_pan, lock_tilt):
                self._aim_lock_frames += 1
            else:
                self._aim_lock_frames = 0

            # Allow early fire when aim has been rock-steady for enough frames,
            # even before settle time expires (rewards fast-converging presets).
            early_lock = self._aim_lock_frames >= max(1, self.cfg.engagement.aim_lock_required_frames)
            settle_met = elapsed >= settle

            # =================================================================================
            # CRITICAL AUTO-TRIGGER LOGIC - DO NOT DISABLE WITHOUT USER APPROVAL
            # This is the primary auto-fire mechanism that MUST work when auto_trigger_enabled=True
            # =================================================================================
            primary_auto_enabled = bool(self.cfg.engagement.auto_trigger_enabled)
            primary_settle_or_lock = bool(settle_met or early_lock)
            primary_ready = bool(self._ready_to_fire())
            primary_has_target = bool(target is not None)
            primary_gate_pass = False
            if primary_auto_enabled and primary_settle_or_lock and primary_ready and primary_has_target:
                primary_gate_pass = bool(self._trigger_should_fire(target, lock_pan, lock_tilt, now))

            if primary_auto_enabled and primary_settle_or_lock and primary_ready and primary_has_target and primary_gate_pass:
                self._begin_fire(order, now)
                return

            if primary_has_target:
                if not primary_auto_enabled:
                    primary_reason = "auto_trigger_disabled"
                    primary_stages = [
                        {
                            "stage": "auto_trigger_enabled",
                            "inputs": {"auto_trigger_enabled": False},
                            "threshold": {"required": True},
                            "pass": False,
                            "reason": "planner veto",
                        }
                    ]
                elif not primary_settle_or_lock:
                    primary_reason = "target_not_centered"
                    primary_stages = [
                        {
                            "stage": "precision_settle_or_lock",
                            "inputs": {
                                "settle_met": bool(settle_met),
                                "early_lock": bool(early_lock),
                                "elapsed": float(elapsed),
                            },
                            "threshold": {
                                "precision_settle_time": float(settle),
                                "aim_lock_required_frames": int(self.cfg.engagement.aim_lock_required_frames),
                            },
                            "pass": False,
                            "reason": "target not centered",
                        }
                    ]
                elif not primary_ready:
                    primary_reason = "target_not_centered"
                    primary_stages = [
                        {
                            "stage": "aim_lock_ready",
                            "inputs": {
                                "aim_lock_frames": int(self._aim_lock_frames),
                                "fire_requires_lock": bool(self.cfg.engagement.fire_requires_lock),
                            },
                            "threshold": {
                                "aim_lock_required_frames": int(self.cfg.engagement.aim_lock_required_frames),
                            },
                            "pass": False,
                            "reason": "target not centered",
                        }
                    ]
                else:
                    primary_reason = str((self._last_fire_gate_trace or {}).get("reason", "unknown rejection path") or "unknown rejection path")
                    primary_stages = list((self._last_fire_gate_trace or {}).get("stages", []) or [])

                self._emit_engagement_telemetry(
                    now=now,
                    order=order,
                    target=target,
                    attempt_type="primary",
                    firing_approved=False,
                    firing_rejected_reason=primary_reason,
                    stages=primary_stages,
                )
            elif primary_auto_enabled and primary_settle_or_lock and primary_ready:
                self._emit_engagement_telemetry(
                    now=now,
                    order=order,
                    target=None,
                    attempt_type="primary",
                    firing_approved=False,
                    firing_rejected_reason="tracker_lost",
                    stages=[
                        {
                            "stage": "tracker_presence",
                            "inputs": {"target_present": False},
                            "threshold": {"required": True},
                            "pass": False,
                            "reason": "tracker lost",
                        }
                    ],
                )

            # =================================================================================
            # BACKUP AUTO-TRIGGER LOGIC - DO NOT DISABLE WITHOUT USER APPROVAL  
            # Fallback firing mechanism for timeout scenarios
            # =================================================================================
            backup_auto_enabled = bool(self.cfg.engagement.auto_trigger_enabled)
            backup_refractory_clear = bool(now >= self._trigger_refractory_until)
            backup_timeout_met = bool(elapsed >= float(self.cfg.engagement.aim_lock_timeout))
            backup_has_target = bool(target is not None)
            backup_ready = bool(self._ready_to_fire())
            backup_target_ok = bool(target is not None and self._target_meets_fire_requirements(target, now=now))
            backup_aim_lock = bool(self._has_aim_lock(lock_pan, lock_tilt))
            backup_mask_clear = bool(self._current_no_fire_mask() is None)

            if (
                backup_auto_enabled
                and backup_refractory_clear
                and backup_timeout_met
                and backup_has_target
                and backup_ready
                and backup_target_ok
                and backup_aim_lock
                and backup_mask_clear
            ):
                self._begin_fire(order, now)
                return

            if backup_has_target and backup_timeout_met:
                backup_stages = [
                    {
                        "stage": "auto_trigger_enabled",
                        "inputs": {"auto_trigger_enabled": bool(backup_auto_enabled)},
                        "threshold": {"required": True},
                        "pass": bool(backup_auto_enabled),
                        "reason": "auto-trigger enabled" if backup_auto_enabled else "planner veto",
                    },
                    {
                        "stage": "refractory_period",
                        "inputs": {"now": float(now)},
                        "threshold": {"refractory_until": float(self._trigger_refractory_until)},
                        "pass": bool(backup_refractory_clear),
                        "reason": "refractory period satisfied" if backup_refractory_clear else "refractory period",
                    },
                    {
                        "stage": "aim_lock_timeout",
                        "inputs": {"elapsed": float(elapsed)},
                        "threshold": {"aim_lock_timeout": float(self.cfg.engagement.aim_lock_timeout)},
                        "pass": bool(backup_timeout_met),
                        "reason": "timeout satisfied" if backup_timeout_met else "hold-time requirement not satisfied",
                    },
                    {
                        "stage": "aim_lock_ready",
                        "inputs": {"aim_lock_frames": int(self._aim_lock_frames)},
                        "threshold": {"aim_lock_required_frames": int(self.cfg.engagement.aim_lock_required_frames)},
                        "pass": bool(backup_ready),
                        "reason": "aim lock ready" if backup_ready else "target not centered",
                    },
                    {
                        "stage": "target_fire_requirements",
                        "inputs": {
                            "confidence": float(getattr(getattr(target, "det", None), "confidence", 0.0) or 0.0) if target is not None else 0.0,
                            "persistence": float(getattr(target, "persistence", 0.0) or 0.0) if target is not None else 0.0,
                        },
                        "threshold": {
                            "min_confidence": float(self.cfg.engagement.fire_trigger_min_confidence),
                            "min_persistence": float(self.cfg.engagement.fire_trigger_min_persistence),
                        },
                        "pass": bool(backup_target_ok),
                        "reason": "requirements satisfied" if backup_target_ok else "confidence below threshold",
                    },
                    {
                        "stage": "center_lock",
                        "inputs": {"lock_pan": float(lock_pan), "lock_tilt": float(lock_tilt)},
                        "threshold": {
                            "aim_lock_pan_tolerance": float(self.cfg.engagement.aim_lock_pan_tolerance),
                            "aim_lock_tilt_tolerance": float(self.cfg.engagement.aim_lock_tilt_tolerance),
                        },
                        "pass": bool(backup_aim_lock),
                        "reason": "target centered" if backup_aim_lock else "target not centered",
                    },
                    {
                        "stage": "no_fire_mask",
                        "inputs": {"active_mask": str(self._last_no_fire_mask_name or "")},
                        "threshold": {"requires_clear_mask": True},
                        "pass": bool(backup_mask_clear),
                        "reason": "mask clear" if backup_mask_clear else "mask block",
                    },
                ]
                if backup_auto_enabled and backup_refractory_clear and backup_timeout_met and backup_has_target and backup_ready and backup_target_ok and backup_aim_lock and backup_mask_clear:
                    backup_reason = "approved"
                elif not backup_auto_enabled:
                    backup_reason = "auto_trigger_disabled"
                elif not backup_refractory_clear:
                    backup_reason = "refractory_period"
                elif not backup_ready or not backup_aim_lock:
                    backup_reason = "target_not_centered"
                elif not backup_target_ok:
                    backup_reason = "target_quality_below_threshold"
                elif not backup_mask_clear:
                    backup_reason = "mask_block"
                else:
                    backup_reason = "unknown rejection path"

                self._emit_engagement_telemetry(
                    now=now,
                    order=order,
                    target=target,
                    attempt_type="backup",
                    firing_approved=False,
                    firing_rejected_reason=backup_reason,
                    stages=backup_stages,
                )
            elif backup_auto_enabled and backup_timeout_met and not backup_has_target:
                self._emit_engagement_telemetry(
                    now=now,
                    order=order,
                    target=None,
                    attempt_type="backup",
                    firing_approved=False,
                    firing_rejected_reason="tracker_lost",
                    stages=[
                        {
                            "stage": "tracker_presence",
                            "inputs": {"target_present": False},
                            "threshold": {"required": True},
                            "pass": False,
                            "reason": "tracker lost",
                        }
                    ],
                )

            if corr_pan != 0.0 or corr_tilt != 0.0:
                self._move_turret(self.current_pan + corr_pan, self.current_tilt + corr_tilt)

        elif self._engage_phase == "fire":
            tracked_target = self._find_active_target(order)
            tracked_det = tracked_target.det if tracked_target is not None else None
            if tracked_det is not None:
                if not self._has_recent_measured_pose(
                    now,
                    max_age_s=self._engagement_pose_freshness_s(for_fire=True),
                ):
                    self._last_reacquire_note = "fire stale pose -> precision"
                    self._last_reacquire_time = now
                    self._engage_phase = "precision"
                    self._phase_start = now
                    self._reset_precision_state()
                    return
                self._last_err_pan_deg, self._last_err_tilt_deg = self._compute_tracking_angle_error(
                    tracked_target,
                    now,
                    for_fire=True,
                )
                self._record_active_target_solution(
                    tracked_target,
                    now,
                    self._last_err_pan_deg,
                    self._last_err_tilt_deg,
                )
                if self.cfg.engagement.fire_micro_adjust_enabled:
                    if self._should_return_to_precision(self._last_err_pan_deg, self._last_err_tilt_deg):
                        self._engage_phase = "precision"
                        self._phase_start = now
                        self._reset_precision_state()
                        return

                    corr_pan, corr_tilt, _, _ = self._compute_visual_servo_correction(
                        self._last_err_pan_deg,
                        self._last_err_tilt_deg,
                        use_fire_limits=True,
                    )

                    if self._log_precision_tuning:
                        eng = self.cfg.engagement
                        target_pan = self.current_pan + self._last_err_pan_deg
                        target_tilt = self.current_tilt + self._last_err_tilt_deg
                        deadzone_pan = float(eng.precision_deadzone_pan_deg)
                        deadzone_tilt = float(eng.precision_deadzone_tilt_deg)
                        within_deadzone = (
                            abs(self._last_err_pan_deg) <= deadzone_pan
                            and abs(self._last_err_tilt_deg) <= deadzone_tilt
                        )
                        self._safe_log_precision_frame(
                            current_pan=self.current_pan,
                            current_tilt=self.current_tilt,
                            target_pan=target_pan,
                            target_tilt=target_tilt,
                            pid_p_pan=self._last_pid_p_pan,
                            pid_i_pan=self._last_pid_i_pan,
                            pid_d_pan=self._last_pid_d_pan,
                            pid_p_tilt=self._last_pid_p_tilt,
                            pid_i_tilt=self._last_pid_i_tilt,
                            pid_d_tilt=self._last_pid_d_tilt,
                            move_cmd_pan=corr_pan,
                            move_cmd_tilt=corr_tilt,
                            within_deadzone=within_deadzone,
                            deadzone_pan=deadzone_pan,
                            deadzone_tilt=deadzone_tilt,
                            phase="fire",
                            fired=True,
                        )

                    if corr_pan != 0.0 or corr_tilt != 0.0:
                        self._move_turret(self.current_pan + corr_pan, self.current_tilt + corr_tilt)
            else:
                self._last_err_pan_deg = 0.0
                self._last_err_tilt_deg = 0.0

            burst_duration = (
                self.cfg.engagement.burst_count
                * self.cfg.engagement.burst_interval_ms
                / 1000.0
            )
            wait = burst_duration + self.cfg.engagement.inter_target_cooldown
            if elapsed >= wait:
                if self.cfg.engagement.single_target_only and tracked_det is not None:
                    if self._should_force_stationary_release_in_single_target(order, tracked_target, now):
                        self._advance_queue(now)
                        return
                    self._engage_phase = "precision"
                    self._phase_start = now
                    self._reset_precision_state()
                    return

                self._queue_index += 1
                if self._queue_index < len(self._queue):
                    if self._log_precision_tuning and self._current_precision_engagement_id:
                        self._precision_logger.end_engagement()
                        self._current_precision_engagement_id = None
                    nxt = self._queue[self._queue_index]
                    self.active_order = nxt
                    self._remember_active_target(nxt.target.det)
                    self._start_order_engagement(nxt, now)
                else:
                    if self._log_precision_tuning and self._current_precision_engagement_id:
                        self._precision_logger.end_engagement()
                        self._current_precision_engagement_id = None
                    self._start_return_to_guard(now)

    def _find_active_target(self, order: EngagementOrder) -> Optional[TrackedTarget]:
        now = time.time()
        for target in self.last_targets:
            if target.det.track_id == order.target.det.track_id:
                self._clear_active_reacquire_confirm_pending()
                self._remember_active_target(target.det, target=target)
                return target
        reacquired = self._find_reacquire_target(order)
        if reacquired is not None:
            old_track_id = int(order.target.det.track_id)
            order.target = reacquired
            self._remember_active_target(reacquired.det, target=reacquired)
            new_track_id = int(reacquired.det.track_id)
            if new_track_id != old_track_id:
                self._last_reacquire_note = f"reacquire {old_track_id}->{new_track_id}"
                self._last_reacquire_time = now
                self._arm_active_reacquire_confirm_pending(old_track_id=old_track_id, new_track_id=new_track_id, now=now)
            else:
                self._clear_active_reacquire_confirm_pending()
            return reacquired
        pending_det = self._match_active_reacquire_confirm_pending_detection(order)
        if pending_det is not None:
            self._remember_active_target(pending_det, timestamp=now)
            self._active_reacquire_confirm_pending_frames = max(0, self._active_reacquire_confirm_pending_frames - 1)
            self._last_reacquire_note = f"reacquire confirm pending {int(pending_det.track_id)}"
            self._last_reacquire_time = now
            return order.target
        self._clear_active_reacquire_confirm_pending()
        return None

    def _find_reacquire_target(self, order: EngagementOrder) -> Optional[TrackedTarget]:
        if not self.last_targets and not self.last_detections:
            return None

        anchor_center = self._active_target_last_center or (
            float(order.target.det.center_x),
            float(order.target.det.center_y),
        )
        anchor_bbox = self._active_target_last_bbox or order.target.det.bbox
        anchor_class = str(order.target.det.class_name or "").strip().lower()
        anchor_source = str(order.target.det.source or "").strip().lower()
        frame_w = float(max(1, self.cfg.guard.frame_width))
        frame_h = float(max(1, self.cfg.guard.frame_height))
        loss_age = max(0.0, time.time() - float(self._active_target_last_seen_time or 0.0))
        heading_x, heading_y = self._active_target_heading_norm(loss_age)
        if loss_age > 0.0:
            anchor_center = (
                max(0.0, min(frame_w, anchor_center[0] + (heading_x * frame_w * loss_age))),
                max(0.0, min(frame_h, anchor_center[1] + (heading_y * frame_h * loss_age))),
            )
        anchor_diag = ((float(anchor_bbox[2]) ** 2) + (float(anchor_bbox[3]) ** 2)) ** 0.5
        anchor_area = self._bbox_area(anchor_bbox)
        reacquire_radius_px = max(72.0, min(frame_w, frame_h) * 0.16, anchor_diag * 0.60)
        reacquire_radius_px *= min(1.9, 1.0 + (loss_age * 1.35))
        if self._adaptive_loss_recovery_enabled():
            visible_count = int(self._loss_recovery_context.get("visible_target_count", len(self.last_targets)) or len(self.last_targets))
            crowd_threshold = max(1, int(getattr(self.cfg.engagement, "loss_scene_crowding_threshold", 3) or 3))
            expand_scale = max(1.0, float(getattr(self.cfg.engagement, "loss_persistent_expand_scale", 1.18) or 1.18))
            if visible_count <= 0:
                reacquire_radius_px *= expand_scale
            elif visible_count >= crowd_threshold:
                reacquire_radius_px *= 0.82

        best_target: Optional[TrackedTarget] = None
        best_cost = float("inf")
        current_time = time.time()
        scored_track_ids = {int(target.det.track_id) for target in self.last_targets}
        candidate_targets: List[Tuple[TrackedTarget, bool]] = [(target, False) for target in self.last_targets]
        provisional_conf_floor = max(
            0.30,
            float(getattr(self.cfg.target_filter, "min_confidence", 0.5) or 0.5) * 0.70,
        )
        provisional_dets: List[DetectedObject] = []

        for det in self.last_detections:
            det_track_id = int(det.track_id)
            if det_track_id in scored_track_ids:
                continue

            target_class = str(det.class_name or "").strip().lower()
            target_source = str(det.source or "").strip().lower()
            if anchor_source and target_source and target_source != anchor_source:
                continue
            if anchor_class and anchor_class not in NON_SEMANTIC_REACQUIRE_CLASSES:
                if target_class and target_class != anchor_class:
                    continue

            dist_px = ((float(det.center_x) - anchor_center[0]) ** 2 + (float(det.center_y) - anchor_center[1]) ** 2) ** 0.5
            iou = self._bbox_iou(anchor_bbox, det.bbox)
            area_similarity = min(anchor_area, self._bbox_area(det.bbox)) / max(anchor_area, self._bbox_area(det.bbox))
            if dist_px > reacquire_radius_px and iou < 0.08:
                continue
            if area_similarity < 0.35 and iou < 0.12:
                continue
            if float(det.confidence) < provisional_conf_floor and iou < 0.18 and dist_px > (reacquire_radius_px * 0.55):
                continue
            provisional_dets.append(det)

        if provisional_dets:
            for target in self._scorer.score(provisional_dets, current_time):
                candidate_targets.append((target, True))

        for target, provisional in candidate_targets:
            det = target.det
            target_class = str(det.class_name or "").strip().lower()
            target_source = str(det.source or "").strip().lower()
            if anchor_source and target_source and target_source != anchor_source:
                continue
            if provisional:
                if float(det.confidence) < provisional_conf_floor:
                    continue
            elif target.threat_score < (self.cfg.engagement.min_threat_score * 0.70):
                continue
            if anchor_class and anchor_class not in NON_SEMANTIC_REACQUIRE_CLASSES:
                if target_class and target_class != anchor_class:
                    continue

            dist_px = ((float(det.center_x) - anchor_center[0]) ** 2 + (float(det.center_y) - anchor_center[1]) ** 2) ** 0.5
            iou = self._bbox_iou(anchor_bbox, det.bbox)
            area_similarity = min(anchor_area, self._bbox_area(det.bbox)) / max(anchor_area, self._bbox_area(det.bbox))
            if dist_px > reacquire_radius_px and iou < 0.08:
                continue
            if area_similarity < 0.35 and iou < 0.12:
                continue

            cost = (
                (dist_px / max(1.0, reacquire_radius_px))
                - (iou * 0.85)
                - (area_similarity * 0.35)
                - (target.threat_score * (0.14 if provisional else 0.20))
            )
            if provisional:
                cost += 0.08
            if self._adaptive_loss_recovery_enabled():
                visible_count = int(self._loss_recovery_context.get("visible_target_count", len(self.last_targets)) or len(self.last_targets))
                crowd_threshold = max(1, int(getattr(self.cfg.engagement, "loss_scene_crowding_threshold", 3) or 3))
                if visible_count >= crowd_threshold:
                    cost += 0.08
            if cost < best_cost:
                best_cost = cost
                best_target = target

        if best_target is None or best_cost > 0.75:
            return None
        return best_target

    def _arm_active_reacquire_confirm_pending(
        self,
        *,
        old_track_id: int,
        new_track_id: int,
        now: Optional[float] = None,
    ) -> None:
        current_time = float(now if now is not None else time.time())
        self._active_reacquire_confirm_pending_frames = 2
        self._active_reacquire_confirm_pending_until = current_time + 0.30
        self._last_reacquire_note = f"reacquire {old_track_id}->{new_track_id}"
        self._last_reacquire_time = current_time

    def _clear_active_reacquire_confirm_pending(self) -> None:
        self._active_reacquire_confirm_pending_frames = 0
        self._active_reacquire_confirm_pending_until = 0.0

    def _match_active_reacquire_confirm_pending_detection(
        self,
        order: EngagementOrder,
    ) -> Optional[DetectedObject]:
        if self._active_reacquire_confirm_pending_frames <= 0:
            return None
        current_time = time.time()
        if current_time > float(self._active_reacquire_confirm_pending_until or 0.0):
            return None
        if not self.last_detections or not self.last_filter_diagnostics:
            return None

        anchor_center = self._active_target_last_center or (
            float(order.target.det.center_x),
            float(order.target.det.center_y),
        )
        anchor_bbox = self._active_target_last_bbox or order.target.det.bbox
        anchor_class = str(getattr(self, "_active_target_last_class", "") or order.target.det.class_name or "").strip().lower()
        anchor_source = str(getattr(self, "_active_target_last_source", "") or order.target.det.source or "").strip().lower()
        frame_w = float(max(1, self.cfg.guard.frame_width))
        frame_h = float(max(1, self.cfg.guard.frame_height))
        anchor_diag = ((float(anchor_bbox[2]) ** 2) + (float(anchor_bbox[3]) ** 2)) ** 0.5
        pending_radius_px = max(64.0, min(frame_w, frame_h) * 0.14, anchor_diag * 0.52)
        diagnostics_by_track = {
            int(decision.track_id): decision
            for decision in self.last_filter_diagnostics
            if not bool(decision.passed)
        }

        best_det: Optional[DetectedObject] = None
        best_score = float("inf")
        for det in self.last_detections:
            decision = diagnostics_by_track.get(int(det.track_id))
            if decision is None:
                continue
            if int(decision.confirm_required) <= 1 or int(decision.confirm_hits) >= int(decision.confirm_required):
                continue
            target_class = str(det.class_name or "").strip().lower()
            target_source = str(det.source or "").strip().lower()
            if anchor_source and target_source and target_source != anchor_source:
                continue
            if anchor_class and anchor_class not in NON_SEMANTIC_REACQUIRE_CLASSES:
                if target_class and target_class != anchor_class:
                    continue
            dist_px = ((float(det.center_x) - anchor_center[0]) ** 2 + (float(det.center_y) - anchor_center[1]) ** 2) ** 0.5
            iou = self._bbox_iou(anchor_bbox, det.bbox)
            if dist_px > pending_radius_px and iou < 0.10:
                continue
            score = (dist_px / max(1.0, pending_radius_px)) - (iou * 0.60)
            if score < best_score:
                best_score = score
                best_det = det
        return best_det

    def _remember_active_target(
        self,
        det: DetectedObject,
        *,
        target: Optional[TrackedTarget] = None,
        timestamp: Optional[float] = None,
    ) -> None:
        self._active_target_last_center = (float(det.center_x), float(det.center_y))
        self._active_target_last_bbox = tuple(int(v) for v in det.bbox)
        if target is not None:
            self._active_target_last_heading_norm = (float(target.heading_x), float(target.heading_y))
            self._active_target_last_history_samples = int(getattr(target, "history_samples", 0) or 0)
            self._active_target_last_heading_stability = float(getattr(target, "heading_stability", 0.0) or 0.0)
            self._active_target_last_class = str(target.det.class_name or "").strip().lower()
            self._active_target_last_source = str(target.det.source or "").strip().lower()
        else:
            self._active_target_last_heading_norm = (0.0, 0.0)
            self._active_target_last_history_samples = 0
            self._active_target_last_heading_stability = 0.0
            self._active_target_last_class = str(det.class_name or "").strip().lower()
            self._active_target_last_source = str(det.source or "").strip().lower()
        self._active_target_last_seen_time = float(timestamp or time.time())

    @staticmethod
    def _bbox_iou(a: Tuple[int, int, int, int], b: Tuple[int, int, int, int]) -> float:
        ax1, ay1, aw, ah = a
        bx1, by1, bw, bh = b
        ax2, ay2 = ax1 + aw, ay1 + ah
        bx2, by2 = bx1 + bw, by1 + bh

        ix1 = max(ax1, bx1)
        iy1 = max(ay1, by1)
        ix2 = min(ax2, bx2)
        iy2 = min(ay2, by2)
        iw = max(0, ix2 - ix1)
        ih = max(0, iy2 - iy1)
        inter = iw * ih
        if inter <= 0:
            return 0.0

        area_a = aw * ah
        area_b = bw * bh
        union = max(1, area_a + area_b - inter)
        return inter / union

    @staticmethod
    def _bbox_area(bbox: Tuple[int, int, int, int]) -> float:
        return float(max(1, bbox[2] * bbox[3]))

    def _has_aim_lock(self, err_pan: float, err_tilt: float) -> bool:
        return (
            abs(err_pan) <= self.cfg.engagement.aim_lock_pan_tolerance
            and abs(err_tilt) <= self.cfg.engagement.aim_lock_tilt_tolerance
        )

    def _ready_to_fire(self) -> bool:
        if not self.cfg.engagement.fire_requires_lock:
            return True
        return self._aim_lock_frames >= max(1, self.cfg.engagement.aim_lock_required_frames)

    def _person_identity_fire_authorization_window_s(self) -> float:
        loss_timeout = float(getattr(self.cfg.engagement, "target_loss_timeout", 1.4) or 1.4)
        return max(1.75, min(3.0, loss_timeout + 0.40))

    def _set_fire_veto_reason(self, reason: str, now: float) -> None:
        self._last_fire_veto_reason = str(reason or "")
        self._last_fire_veto_time = float(now)

    def _normalized_rejection_reason(self, reason: str) -> str:
        reason_key = str(reason or "").strip().lower()
        mapping = {
            "class_rejected": "class not allowed",
            "low_confidence": "confidence below threshold",
            "shape_rejected": "shape mismatch",
            "semantic_confirm_pending": "semantic confirmation failed",
            "tracker_lost": "tracker lost",
            "target_not_centered": "target not centered",
            "refractory_period": "refractory period",
            "planner_veto": "planner veto",
            "safety_lock": "safety lock",
            "no_fire_mask_block": "mask block",
            "pir_requirement_not_satisfied": "PIR requirement not satisfied",
            "person_fire_authorization_failed": "safety lock",
            "target_quality_below_threshold": "confidence below threshold",
            "hold_time_not_met": "hold-time requirement not satisfied",
            "auto_trigger_disabled": "planner veto",
            "prompted_auto_fire_disabled": "planner veto",
            "mask_block": "mask block",
        }
        if reason_key in mapping:
            return mapping[reason_key]
        return reason_key or "unknown rejection path"

    def _shape_profile_telemetry(self, det: DetectedObject) -> Dict[str, Any]:
        profile_name = str(getattr(self.cfg.target_filter, "shape_profile_name", "") or "").strip().lower()
        if not profile_name:
            profile_name = str(getattr(det, "class_name", "") or "").strip().lower()
        profile_name = SHAPE_PROFILE_ALIASES.get(profile_name, profile_name)
        profile = SHAPE_FILTER_PROFILES.get(profile_name)

        width = max(1.0, float(det.bbox[2]))
        height = max(1.0, float(det.bbox[3]))
        aspect_ratio = width / height
        score = 1.0
        passed = True
        reason = "shape profile accepted"
        min_aspect_ratio = 0.0
        max_aspect_ratio = 0.0

        if profile:
            min_aspect_ratio = float(profile.get("min_aspect_ratio", 0.0) or 0.0)
            max_aspect_ratio = float(profile.get("max_aspect_ratio", 0.0) or 0.0)
            if min_aspect_ratio > 0.0 and aspect_ratio < min_aspect_ratio:
                passed = False
                score = max(0.0, aspect_ratio / max(min_aspect_ratio, 1e-6))
                reason = "shape mismatch"
            elif max_aspect_ratio > 0.0 and aspect_ratio > max_aspect_ratio:
                passed = False
                score = max(0.0, max_aspect_ratio / max(aspect_ratio, 1e-6))
                reason = "shape mismatch"
        else:
            reason = "shape profile unavailable; check skipped"

        return {
            "shape_profile_used": profile_name,
            "shape_score": float(round(score, 6)),
            "aspect_ratio": float(round(aspect_ratio, 6)),
            "min_aspect_ratio": float(min_aspect_ratio),
            "max_aspect_ratio": float(max_aspect_ratio),
            "shape_passed": bool(passed),
            "shape_reason": reason,
        }

    def _find_filter_decision_for_track(self, track_id: int) -> Optional[FilterDecision]:
        for decision in self.last_filter_diagnostics:
            if int(getattr(decision, "track_id", -1) or -1) == int(track_id):
                return decision
        return None

    def _build_filter_stage_records(
        self,
        det: DetectedObject,
        decision: Optional[FilterDecision],
        target: Optional[TrackedTarget],
    ) -> List[Dict[str, Any]]:
        allowed_classes = [str(item) for item in list(getattr(self.cfg.target_filter, "allowed_classes", []) or [])]
        class_allowed = (not allowed_classes) or (str(det.class_name) in allowed_classes)
        confidence_threshold = float(getattr(self.cfg.target_filter, "min_confidence", 0.0) or 0.0)
        conf_pass = float(det.confidence) >= confidence_threshold
        min_size_ratio = float(getattr(self.cfg.target_filter, "min_size_ratio", 0.0) or 0.0)
        max_size_ratio = float(getattr(self.cfg.target_filter, "max_size_ratio", 0.0) or 0.0)
        area_ratio = float(det.area_ratio)
        min_size_pass = area_ratio >= min_size_ratio
        max_size_pass = (max_size_ratio <= 0.0) or (area_ratio <= max_size_ratio)
        zone = list(getattr(self.cfg.target_filter, "engagement_zone", [0.0, 0.0, 1.0, 1.0]) or [0.0, 0.0, 1.0, 1.0])
        zone_pass = bool(zone[0] <= det.norm_cx <= zone[2] and zone[1] <= det.norm_cy <= zone[3])
        semantic_required = max(1, int(getattr(self.cfg.target_filter, "semantic_min_confirm_frames", 1) or 1))
        semantic_hits = int(getattr(decision, "confirm_hits", 0) or 0) if decision is not None else 0
        semantic_pass = semantic_required <= 1 or semantic_hits >= semantic_required
        shape_info = self._shape_profile_telemetry(det)

        stages: List[Dict[str, Any]] = [
            {
                "stage": "class_whitelist",
                "inputs": {"class_name": str(det.class_name)},
                "threshold": {"allowed_classes": allowed_classes},
                "pass": bool(class_allowed),
                "reason": "class accepted" if class_allowed else "class not allowed",
            },
            {
                "stage": "confidence_threshold",
                "inputs": {"confidence": float(det.confidence)},
                "threshold": {"min_confidence": confidence_threshold},
                "pass": bool(conf_pass),
                "reason": "confidence accepted" if conf_pass else "confidence below threshold",
            },
            {
                "stage": "size_min",
                "inputs": {"area_ratio": area_ratio},
                "threshold": {"min_size_ratio": min_size_ratio},
                "pass": bool(min_size_pass),
                "reason": "size accepted" if min_size_pass else "size too small",
            },
            {
                "stage": "size_max",
                "inputs": {"area_ratio": area_ratio},
                "threshold": {"max_size_ratio": max_size_ratio},
                "pass": bool(max_size_pass),
                "reason": "size accepted" if max_size_pass else "size too large",
            },
            {
                "stage": "engagement_zone",
                "inputs": {"norm_center": [float(det.norm_cx), float(det.norm_cy)]},
                "threshold": {"zone": zone},
                "pass": bool(zone_pass),
                "reason": "inside zone" if zone_pass else "outside zone",
            },
            {
                "stage": "shape_profile",
                "inputs": {
                    "aspect_ratio": float(shape_info["aspect_ratio"]),
                    "shape_profile": str(shape_info["shape_profile_used"]),
                },
                "threshold": {
                    "min_aspect_ratio": float(shape_info["min_aspect_ratio"]),
                    "max_aspect_ratio": float(shape_info["max_aspect_ratio"]),
                },
                "pass": bool(shape_info["shape_passed"]),
                "reason": str(shape_info["shape_reason"]),
            },
            {
                "stage": "semantic_confirmation",
                "inputs": {
                    "confirm_hits": semantic_hits,
                    "decision_reason": str(getattr(decision, "reason", "") or ""),
                    "decision_detail": str(getattr(decision, "detail", "") or ""),
                },
                "threshold": {
                    "semantic_min_confirm_frames": semantic_required,
                    "semantic_min_confirm_confidence": float(
                        getattr(self.cfg.target_filter, "semantic_min_confirm_confidence", 0.0) or 0.0
                    ),
                },
                "pass": bool(semantic_pass),
                "reason": "semantic confirmation passed" if semantic_pass else "semantic confirmation failed",
            },
        ]

        if target is not None:
            min_threat = float(getattr(self.cfg.engagement, "min_threat_score", 0.0) or 0.0)
            threat_score = float(getattr(target, "threat_score", 0.0) or 0.0)
            threat_pass = threat_score >= min_threat
            stages.append(
                {
                    "stage": "threat_threshold",
                    "inputs": {"threat_score": threat_score},
                    "threshold": {"min_threat_score": min_threat},
                    "pass": bool(threat_pass),
                    "reason": "planner candidate accepted" if threat_pass else "planner veto",
                }
            )

        return stages

    def _build_gate_stage_records(self, stages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        gate_stages: List[Dict[str, Any]] = []
        for stage in stages:
            gate_stages.append(
                {
                    "stage": str(stage.get("stage", "")),
                    "inputs": dict(stage.get("inputs", {}) or {}),
                    "threshold": dict(stage.get("threshold", {}) or {}),
                    "pass": bool(stage.get("pass", False)),
                    "reason": str(stage.get("reason", "") or ""),
                }
            )
        return gate_stages

    def _current_planner_state(self) -> Dict[str, Any]:
        return {
            "engage_phase": str(getattr(self, "_engage_phase", "") or ""),
            "queue_index": int(getattr(self, "_queue_index", 0) or 0),
            "queue_length": int(len(getattr(self, "_queue", []) or [])),
            "loss_recovery_phase": str(getattr(self, "_loss_recovery_phase", "") or ""),
            "reacquire_note": str(getattr(self, "_last_reacquire_note", "") or ""),
        }

    def _current_pir_state(self) -> Dict[str, Any]:
        return {
            "pir_enabled": bool(getattr(self.cfg.pir_guard, "pir_enabled", False)),
            "pir_cue_mode": bool(getattr(self, "_pir_cue_mode", False)),
            "pir_scan_mode": bool(getattr(self, "_pir_scan_mode", False)),
            "pir_sensor_id": int(getattr(self, "_pir_cue_sensor_id", -1) or -1),
            "pir_queue_length": int(self._pir_manager.peek_queue_count()),
            "pir_status": str(self._pir_manager.get_status_text()),
        }

    def _current_safety_state(self, now: float) -> Dict[str, Any]:
        return {
            "auto_trigger_enabled": bool(getattr(self.cfg.engagement, "auto_trigger_enabled", False)),
            "fire_refractory_until": float(getattr(self, "_trigger_refractory_until", 0.0) or 0.0),
            "fire_refractory_active": bool(now < float(getattr(self, "_trigger_refractory_until", 0.0) or 0.0)),
            "no_fire_mask": str(getattr(self, "_last_no_fire_mask_name", "") or ""),
            "fire_veto_reason": str(getattr(self, "_last_fire_veto_reason", "") or ""),
            "trigger_gate_active": bool(getattr(self, "_trigger_gate_active", False)),
            "trigger_hold_start": float(getattr(self, "_trigger_hold_start", 0.0) or 0.0),
        }

    def _motion_policy_mode(self) -> str:
        return str(getattr(self.cfg.engagement, "motion_policy_mode", "allow_stationary") or "allow_stationary").strip().lower()

    def _motion_policy_window_s(self) -> float:
        return max(0.20, float(getattr(self.cfg.engagement, "motion_recent_window_s", 1.25) or 1.25))

    def _motion_policy_entry(self, track_id: int) -> Dict[str, Any]:
        return self._motion_policy_state.setdefault(
            int(track_id),
            {
                "track_id": int(track_id),
                "state": "TRACKING",
                "previous_state": "",
                "suppression_reason": "",
                "suppression_timestamp": 0.0,
                "suppression_expiry": 0.0,
                "next_eligible_evaluation_time": 0.0,
                "recent_motion_distance_px": 0.0,
                "average_velocity_px_s": 0.0,
                "motion_confidence": 0.0,
                "stationary_duration_s": 0.0,
                "motion_window_s": self._motion_policy_window_s(),
                "last_evaluated": 0.0,
                "history": [],
                "last_motion_detected": False,
                "motion_samples": 0,
            },
        )

    def _record_motion_policy_transition(
        self,
        track_id: int,
        new_state: str,
        now: float,
        reason: str,
    ) -> Dict[str, Any]:
        entry = self._motion_policy_entry(track_id)
        new_state = str(new_state or "TRACKING")
        previous_state = str(entry.get("state", "TRACKING") or "TRACKING")
        if previous_state != new_state:
            history = list(entry.get("history", []) or [])
            history.append(
                {
                    "timestamp": float(now),
                    "from": previous_state,
                    "to": new_state,
                    "reason": str(reason or ""),
                }
            )
            entry["history"] = history[-20:]
            entry["previous_state"] = previous_state
            entry["state"] = new_state
            self._publish_mission_event(
                "motion_policy_transition",
                {
                    "timestamp": float(now),
                    "frame_number": int(self._frame_number),
                    "track_id": int(track_id),
                    "from_state": str(previous_state),
                    "to_state": str(new_state),
                    "reason": str(reason or ""),
                },
            )
        else:
            entry["state"] = new_state
        entry["last_evaluated"] = float(now)
        return entry

    def _evaluate_motion_policy(self, target: TrackedTarget, now: float) -> Dict[str, Any]:
        det = target.det
        track_id = int(det.track_id)
        entry = self._motion_policy_entry(track_id)
        mode = self._motion_policy_mode()
        if (
            str(det.class_name or "").strip().lower() in SEMANTIC_IDENTITY_CLASSES
            and mode == "allow_stationary"
        ):
            mode = "require_recent_motion"
        motion_snapshot = self._scorer.get_motion_history_snapshot(det, now, window_s=self._motion_policy_window_s())
        engage_mode_allowed = bool(getattr(self.cfg.engagement, "motion_allow_stationary_engagement", True))
        recent_distance_px = float(motion_snapshot.recent_motion_distance_px)
        average_velocity_px_s = float(motion_snapshot.average_velocity_px_s)
        motion_confidence = float(motion_snapshot.motion_confidence)
        stationary_duration_s = float(motion_snapshot.stationary_duration_s)

        recent_distance_threshold_px = max(0.0, float(getattr(self.cfg.engagement, "motion_recent_distance_px", 18.0) or 18.0))
        average_velocity_threshold_px_s = max(0.0, float(getattr(self.cfg.engagement, "motion_average_velocity_px_s", 10.0) or 10.0))
        motion_confidence_min = max(0.0, float(getattr(self.cfg.engagement, "motion_confidence_min", 0.35) or 0.35))
        stationary_timeout_s = max(0.0, float(getattr(self.cfg.engagement, "motion_stationary_timeout_s", 4.0) or 4.0))
        suppression_cooldown_s = max(0.0, float(getattr(self.cfg.engagement, "motion_suppression_cooldown_s", 1.5) or 1.5))

        recent_motion_ok = bool(
            recent_distance_px >= recent_distance_threshold_px
            or average_velocity_px_s >= average_velocity_threshold_px_s
            or motion_confidence >= motion_confidence_min
        )

        suppression_reason = str(entry.get("suppression_reason", "") or "")
        suppression_timestamp = float(entry.get("suppression_timestamp", 0.0) or 0.0)
        suppression_expiry = float(entry.get("suppression_expiry", 0.0) or 0.0)
        next_eval = float(entry.get("next_eligible_evaluation_time", 0.0) or 0.0)
        current_state = str(entry.get("state", "TRACKING") or "TRACKING")

        if current_state == "TRACK_ONLY" and mode != "allow_stationary" and now < next_eval and not recent_motion_ok:
            entry.update(
                {
                    "track_id": track_id,
                    "motion_window_s": float(self._motion_policy_window_s()),
                    "recent_motion_distance_px": recent_distance_px,
                    "average_velocity_px_s": average_velocity_px_s,
                    "motion_confidence": motion_confidence,
                    "stationary_duration_s": stationary_duration_s,
                    "recent_motion_detected": bool(motion_snapshot.recent_motion_detected),
                    "motion_samples": int(motion_snapshot.sample_count),
                    "suppression_reason": str(suppression_reason or "recent motion below threshold"),
                    "suppression_timestamp": float(suppression_timestamp or now),
                    "suppression_expiry": float(suppression_expiry or next_eval),
                    "next_eligible_evaluation_time": float(next_eval),
                    "profile_mode": mode,
                    "motion_allowed": False,
                    "motion_context": {
                        "track_id": track_id,
                        "recent_motion_distance_px": recent_distance_px,
                        "average_velocity_px_s": average_velocity_px_s,
                        "motion_confidence": motion_confidence,
                        "stationary_duration_s": stationary_duration_s,
                        "recent_motion_detected": bool(motion_snapshot.recent_motion_detected),
                    },
                }
            )
            return entry

        if mode == "tracking_only":
            new_state = "TRACK_ONLY"
            suppression_reason = "profile tracking_only"
            if suppression_timestamp <= 0.0:
                suppression_timestamp = float(now)
            if suppression_expiry <= 0.0:
                suppression_expiry = float(now + suppression_cooldown_s)
            next_eval = max(next_eval, suppression_expiry)
        elif mode == "require_recent_motion":
            if recent_motion_ok:
                new_state = "ENGAGEABLE"
                suppression_reason = ""
                suppression_timestamp = 0.0
                suppression_expiry = 0.0
                next_eval = float(now)
            else:
                if stationary_duration_s >= stationary_timeout_s:
                    new_state = "TRACK_ONLY"
                    suppression_reason = "recent motion timeout"
                else:
                    new_state = "TRACKING"
                    suppression_reason = "recent motion below threshold"
                if suppression_timestamp <= 0.0:
                    suppression_timestamp = float(now)
                if suppression_expiry <= 0.0:
                    suppression_expiry = float(now + suppression_cooldown_s)
                next_eval = max(next_eval, suppression_expiry)
        else:
            new_state = "ENGAGEABLE" if engage_mode_allowed else "TRACK_ONLY"
            if not engage_mode_allowed:
                suppression_reason = "profile stationary disallows engagement"
                if suppression_timestamp <= 0.0:
                    suppression_timestamp = float(now)
                if suppression_expiry <= 0.0:
                    suppression_expiry = float(now + suppression_cooldown_s)
                next_eval = max(next_eval, suppression_expiry)
            else:
                suppression_reason = ""
                suppression_timestamp = 0.0
                suppression_expiry = 0.0
                next_eval = float(now)

        if current_state in {"ENGAGING", "FIRE_AUTHORIZATION", "FIRED", "POST_ENGAGEMENT"}:
            new_state = current_state

        entry = self._record_motion_policy_transition(
            track_id,
            new_state,
            now,
            suppression_reason or ("recent motion confirmed" if new_state == "ENGAGEABLE" else ""),
        )
        entry.update(
            {
                "track_id": track_id,
                "motion_window_s": float(self._motion_policy_window_s()),
                "recent_motion_distance_px": recent_distance_px,
                "average_velocity_px_s": average_velocity_px_s,
                "motion_confidence": motion_confidence,
                "stationary_duration_s": stationary_duration_s,
                "recent_motion_detected": bool(motion_snapshot.recent_motion_detected),
                "motion_samples": int(motion_snapshot.sample_count),
                "suppression_reason": str(suppression_reason or ""),
                "suppression_timestamp": float(suppression_timestamp),
                "suppression_expiry": float(suppression_expiry),
                "next_eligible_evaluation_time": float(next_eval),
                "profile_mode": mode,
                "motion_allowed": bool(new_state == "ENGAGEABLE"),
                "motion_context": {
                    "track_id": track_id,
                    "recent_motion_distance_px": recent_distance_px,
                    "average_velocity_px_s": average_velocity_px_s,
                    "motion_confidence": motion_confidence,
                    "stationary_duration_s": stationary_duration_s,
                    "recent_motion_detected": bool(motion_snapshot.recent_motion_detected),
                },
            }
        )
        return entry

    def _apply_motion_policy_to_targets(
        self,
        targets: List[TrackedTarget],
        now: float,
    ) -> Tuple[List[TrackedTarget], List[Dict[str, Any]]]:
        engageable: List[TrackedTarget] = []
        snapshots: List[Dict[str, Any]] = []
        active_track_ids = {int(t.det.track_id) for t in targets}
        suppression_cooldown_s = max(0.0, float(getattr(self.cfg.engagement, "motion_suppression_cooldown_s", 1.5) or 1.5))

        for target in targets:
            entry = self._evaluate_motion_policy(target, now)
            snapshots.append(dict(entry))
            if str(entry.get("state", "TRACKING") or "TRACKING") == "ENGAGEABLE":
                engageable.append(target)
            elif str(entry.get("state", "TRACKING") or "TRACKING") == "TRACK_ONLY" and float(entry.get("next_eligible_evaluation_time", 0.0) or 0.0) <= 0.0:
                entry["next_eligible_evaluation_time"] = float(now + suppression_cooldown_s)

        stale_track_ids = [
            track_id
            for track_id in list(self._motion_policy_state.keys())
            if track_id not in active_track_ids
            and (now - float(self._motion_policy_state.get(track_id, {}).get("last_evaluated", now) or now)) > max(0.5, float(self.cfg.engagement.target_loss_timeout))
        ]
        for track_id in stale_track_ids:
            entry = self._motion_policy_state.get(track_id)
            if entry is None:
                continue
            current_state = str(entry.get("state", "TRACKING") or "TRACKING")
            if current_state not in {"LOST", "EXPIRED"}:
                lost_state = self._record_motion_policy_transition(track_id, "LOST", now, "target not visible")
                lost_state["suppression_reason"] = "target not visible"
                lost_state["suppression_timestamp"] = float(now)
                lost_state["suppression_expiry"] = float(now + max(0.5, float(self.cfg.engagement.target_loss_timeout)))
                lost_state["next_eligible_evaluation_time"] = float(lost_state["suppression_expiry"])
                lost_state["state"] = "EXPIRED" if (now - float(lost_state.get("suppression_timestamp", now))) > float(self.cfg.engagement.target_loss_timeout) else "LOST"

        return engageable, snapshots

    def _emit_engagement_telemetry(
        self,
        *,
        now: float,
        order: Optional[EngagementOrder],
        target: Optional[TrackedTarget],
        attempt_type: str,
        firing_approved: bool,
        firing_rejected_reason: str,
        stages: List[Dict[str, Any]],
    ) -> None:
        tracked_target = target
        if tracked_target is None and order is not None:
            tracked_target = order.target

        det: Optional[DetectedObject] = tracked_target.det if tracked_target is not None else None
        decision = None
        if det is not None:
            decision = self._find_filter_decision_for_track(int(getattr(det, "track_id", -1) or -1))

        if det is not None:
            shape_info = self._shape_profile_telemetry(det)
            yolo_class = str(getattr(det, "class_name", "") or "")
            yolo_confidence = float(getattr(det, "confidence", 0.0) or 0.0)
            bbox = tuple(int(v) for v in getattr(det, "bbox", (0, 0, 0, 0)))
            tracker_id = int(getattr(det, "track_id", -1) or -1)
            motion_policy_state = dict(self._motion_policy_state.get(tracker_id, {}) or {})
            semantic_hits = int(getattr(decision, "confirm_hits", 0) or 0) if decision is not None else 0
            semantic_required = int(getattr(decision, "confirm_required", 1) or 1) if decision is not None else 1
            filter_stages = self._build_filter_stage_records(det, decision, tracked_target)
            motion_score = float(getattr(tracked_target, "speed", 0.0) or 0.0) if tracked_target is not None else 0.0
            threat_score = float(getattr(tracked_target, "threat_score", 0.0) or 0.0) if tracked_target is not None else 0.0
        else:
            shape_info = {
                "shape_profile_used": "",
                "shape_score": 0.0,
            }
            yolo_class = ""
            yolo_confidence = 0.0
            bbox = (0, 0, 0, 0)
            tracker_id = -1
            semantic_hits = 0
            semantic_required = 1
            filter_stages = []
            motion_score = 0.0
            threat_score = 0.0
            motion_policy_state = {}

        combined_stages = list(filter_stages) + self._build_gate_stage_records(stages)
        final_gate_result = {
            "approved": bool(firing_approved),
            "reason": "approved" if firing_approved else str(firing_rejected_reason or "rejected"),
            "stages": list(combined_stages),
        }
        rejection_reason = str(firing_rejected_reason or "").strip()
        if not firing_approved:
            rejection_reason = self._normalized_rejection_reason(rejection_reason)

        record: Dict[str, Any] = {
            "timestamp": float(now),
            "timestamp_local": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now)),
            "frame_number": int(self._frame_number),
            "attempt_type": str(attempt_type),
            "tracker_id": tracker_id,
            "yolo_class": yolo_class,
            "yolo_confidence": yolo_confidence,
            "bbox": {
                "x": int(bbox[0]),
                "y": int(bbox[1]),
                "w": int(bbox[2]),
                "h": int(bbox[3]),
                "area_ratio": float((int(bbox[2]) * int(bbox[3])) / max(1, self.cfg.guard.frame_width * self.cfg.guard.frame_height)),
            },
            "motion_score": motion_score,
            "motion_policy_state": str(motion_policy_state.get("state", "TRACKING") or "TRACKING"),
            "motion_policy": {
                "state": str(motion_policy_state.get("state", "TRACKING") or "TRACKING"),
                "previous_state": str(motion_policy_state.get("previous_state", "") or ""),
                "suppression_reason": str(motion_policy_state.get("suppression_reason", "") or ""),
                "suppression_timestamp": float(motion_policy_state.get("suppression_timestamp", 0.0) or 0.0),
                "suppression_expiry": float(motion_policy_state.get("suppression_expiry", 0.0) or 0.0),
                "next_eligible_evaluation_time": float(motion_policy_state.get("next_eligible_evaluation_time", 0.0) or 0.0),
                "recent_motion_distance_px": float(motion_policy_state.get("recent_motion_distance_px", 0.0) or 0.0),
                "average_velocity_px_s": float(motion_policy_state.get("average_velocity_px_s", 0.0) or 0.0),
                "motion_confidence": float(motion_policy_state.get("motion_confidence", 0.0) or 0.0),
                "stationary_duration_s": float(motion_policy_state.get("stationary_duration_s", 0.0) or 0.0),
                "motion_window_s": float(motion_policy_state.get("motion_window_s", self._motion_policy_window_s()) or self._motion_policy_window_s()),
                "motion_allowed": bool(motion_policy_state.get("motion_allowed", True)),
                "profile_mode": str(motion_policy_state.get("profile_mode", self._motion_policy_mode()) or self._motion_policy_mode()),
                "history": list(motion_policy_state.get("history", []) or []),
            },
            "shape_profile_used": str(shape_info.get("shape_profile_used", "") or ""),
            "shape_score": float(shape_info.get("shape_score", 0.0) or 0.0),
            "semantic_confirmation": {
                "count": semantic_hits,
                "required": semantic_required,
            },
            "threat_score": threat_score,
            "planner_state": self._current_planner_state(),
            "pir_state": self._current_pir_state(),
            "sentry_state": str(getattr(self.state, "name", self.state)),
            "safety_state": self._current_safety_state(now),
            "firing": {
                "approved": bool(firing_approved),
                "rejected_reason": "" if firing_approved else rejection_reason,
            },
            "final_gate_result": final_gate_result,
            "qualification_stages": combined_stages,
        }

        try:
            self._engagement_telemetry.append(record)
        except Exception as exc:
            self._report_runtime_warning("Engagement telemetry append failed", exc)

        bbox_data = record.get("bbox", {})
        self._publish_mission_event(
            "engagement_telemetry",
            {
                "timestamp": float(now),
                "frame_number": int(self._frame_number),
                "attempt_type": str(attempt_type),
                "tracker_id": int(tracker_id),
                "firing_approved": bool(firing_approved),
                "firing_rejected_reason": str(rejection_reason),
                "yolo_class": str(yolo_class),
                "yolo_confidence": float(yolo_confidence),
                "bbox": [
                    int(bbox_data.get("x", 0) or 0),
                    int(bbox_data.get("y", 0) or 0),
                    int(bbox_data.get("w", 0) or 0),
                    int(bbox_data.get("h", 0) or 0),
                ],
                "threat_score": float(threat_score),
                "motion_score": float(motion_score),
                "motion_policy_state": str(motion_policy_state.get("state", "TRACKING") or "TRACKING"),
                "final_gate_result": dict(final_gate_result),
                "qualification_stages": list(combined_stages),
            },
        )

        try:
            frame = inspect.currentframe()
            caller = frame.f_back if frame is not None else None
            motion_threshold = self._forensic_motion_threshold()
            stationary = bool(float(motion_score) < float(motion_threshold))
            allowed_classes = [str(c) for c in list(getattr(self.cfg.target_filter, "allowed_classes", []) or [])]
            class_allowed = (not allowed_classes) or (str(yolo_class) in allowed_classes)
            self._forensic_logger.append(
                {
                    "event_type": "engagement_attempt",
                    "frame_number": int(self._frame_number),
                    "attempt_type": str(attempt_type),
                    "tracker_id": int(tracker_id),
                    "yolo_class": str(yolo_class),
                    "class_allowed": bool(class_allowed),
                    "allowed_classes": allowed_classes,
                    "firing_approved": bool(firing_approved),
                    "firing_rejected_reason": str(rejection_reason),
                    "threat_score": float(threat_score),
                    "motion_score": float(motion_score),
                    "motion_policy_state": str(motion_policy_state.get("state", "TRACKING") or "TRACKING"),
                    "motion_policy": {
                        "state": str(motion_policy_state.get("state", "TRACKING") or "TRACKING"),
                        "previous_state": str(motion_policy_state.get("previous_state", "") or ""),
                        "suppression_reason": str(motion_policy_state.get("suppression_reason", "") or ""),
                        "suppression_timestamp": float(motion_policy_state.get("suppression_timestamp", 0.0) or 0.0),
                        "suppression_expiry": float(motion_policy_state.get("suppression_expiry", 0.0) or 0.0),
                        "next_eligible_evaluation_time": float(motion_policy_state.get("next_eligible_evaluation_time", 0.0) or 0.0),
                        "recent_motion_distance_px": float(motion_policy_state.get("recent_motion_distance_px", 0.0) or 0.0),
                        "average_velocity_px_s": float(motion_policy_state.get("average_velocity_px_s", 0.0) or 0.0),
                        "motion_confidence": float(motion_policy_state.get("motion_confidence", 0.0) or 0.0),
                        "stationary_duration_s": float(motion_policy_state.get("stationary_duration_s", 0.0) or 0.0),
                        "motion_window_s": float(motion_policy_state.get("motion_window_s", self._motion_policy_window_s()) or self._motion_policy_window_s()),
                        "motion_allowed": bool(motion_policy_state.get("motion_allowed", True)),
                        "profile_mode": str(motion_policy_state.get("profile_mode", self._motion_policy_mode()) or self._motion_policy_mode()),
                        "history": list(motion_policy_state.get("history", []) or []),
                    },
                    "stationary_analysis": {
                        "is_stationary": bool(stationary),
                        "moving_threshold": float(motion_threshold),
                        "motion_filter_enabled": False,
                        "stationary_targeting_allowed_by_design": True,
                        "approving_function": caller.f_code.co_name if caller is not None else "",
                        "approving_filename": __file__,
                        "approving_line": int(caller.f_lineno) if caller is not None else 0,
                    },
                    "wrong_class_analysis": {
                        "outside_configured_classes": bool(not class_allowed),
                        "semantic_confirmation": {
                            "count": int(semantic_hits),
                            "required": int(semantic_required),
                        },
                        "planner_state": self._current_planner_state(),
                        "decision_chain": combined_stages,
                    },
                    "planner_state": self._current_planner_state(),
                    "pir_state": self._current_pir_state(),
                    "safety_state": self._current_safety_state(now),
                }
            )
        except Exception as exc:
            self._report_runtime_warning("Forensic engagement append failed", exc)

    def _prune_track_identity_cache(self, now: float) -> None:
        max_age = max(5.0, self._person_identity_fire_authorization_window_s() * 3.0)
        stale_track_ids = [
            track_id
            for track_id, entry in self._track_identity_cache.items()
            if (now - float(entry.get("seen_at", 0.0) or 0.0)) > max_age
        ]
        for track_id in stale_track_ids:
            self._track_identity_cache.pop(track_id, None)

    def _cache_track_identity_observation(self, det: DetectedObject, now: float) -> Optional[Dict[str, object]]:
        if str(getattr(det, "class_name", "") or "").strip().lower() != "person":
            return None

        identity_label = str(getattr(det, "identity_label", "") or "").strip()
        identity_profile_id = str(getattr(det, "identity_profile_id", "") or "").strip()
        if not (identity_label or identity_profile_id):
            return None

        entry = {
            "label": identity_label,
            "profile_id": identity_profile_id,
            "friendly": bool(getattr(det, "friendly_identity", False)),
            "confidence": float(getattr(det, "identity_confidence", 0.0) or 0.0),
            "seen_at": float(now),
        }
        try:
            track_id = int(getattr(det, "track_id", -1) or -1)
        except Exception:
            track_id = -1
        if track_id >= 0:
            self._track_identity_cache[track_id] = entry
        return entry

    def _update_track_identity_cache(self, detections: List[DetectedObject], now: float) -> None:
        self._prune_track_identity_cache(now)
        for det in detections:
            self._cache_track_identity_observation(det, now)

    def _resolve_person_fire_identity(self, target: TrackedTarget, now: float) -> Optional[Dict[str, object]]:
        direct_entry = self._cache_track_identity_observation(target.det, now)
        if direct_entry is not None:
            return direct_entry

        try:
            track_id = int(getattr(target.det, "track_id", -1) or -1)
        except Exception:
            track_id = -1
        if track_id < 0:
            return None

        cached = self._track_identity_cache.get(track_id)
        if cached is None:
            return None

        age_s = max(0.0, now - float(cached.get("seen_at", 0.0) or 0.0))
        if age_s > self._person_identity_fire_authorization_window_s():
            return None
        return cached

    def _person_target_is_fire_authorized(self, target: TrackedTarget, now: float) -> bool:
        class_name = str(getattr(target.det, "class_name", "") or "").strip().lower()
        if class_name != "person":
            return True
        allow_unknown = bool(getattr(self.cfg.face_recognition, "fire_on_unknown_persons", True))
        if not bool(getattr(self.cfg.face_recognition, "enabled", False)):
            if allow_unknown:
                self._last_fire_veto_reason = ""
                return True
            self._set_fire_veto_reason(
                "person auto-fire blocked: face recognition disabled and unknown-person policy is deny",
                now,
            )
            return False

        direct_identity_entry = self._cache_track_identity_observation(target.det, now)
        if direct_identity_entry is not None:
            if bool(direct_identity_entry.get("friendly", False)):
                label = str(
                    direct_identity_entry.get("label", "")
                    or direct_identity_entry.get("profile_id", "")
                    or "known face"
                ).strip()
                self._set_fire_veto_reason(f"person auto-fire blocked: friendly identity {label}", now)
                return False

            self._last_fire_veto_reason = ""
            return True

        identity_entry = self._resolve_person_fire_identity(target, now)
        if identity_entry is not None and bool(identity_entry.get("friendly", False)):
            label = str(identity_entry.get("label", "") or identity_entry.get("profile_id", "") or "known face").strip()
            self._set_fire_veto_reason(f"person auto-fire blocked: recent friendly identity {label}", now)
            return False

        if identity_entry is not None:
            self._last_fire_veto_reason = ""
            return True

        if allow_unknown:
            self._last_fire_veto_reason = ""
            return True
        self._set_fire_veto_reason(
            "person auto-fire blocked: unknown person and policy requires known hostile identity",
            now,
        )

        return False

    def _target_meets_fire_requirements(self, target: TrackedTarget, *, now: Optional[float] = None) -> bool:
        """Run the complete, current target-quality gate used by every fire path."""
        eng = self.cfg.engagement
        check_time = time.time() if now is None else float(now)
        stages: List[Dict[str, Any]] = []

        def reject(stage: str, reason: str, inputs: Dict[str, Any], threshold: Dict[str, Any]) -> bool:
            stages.append({"stage": stage, "inputs": inputs, "threshold": threshold, "pass": False, "reason": reason})
            self._last_fire_gate_trace = {"approved": False, "reason": reason, "stages": stages}
            self._set_fire_veto_reason(reason, check_time)
            return False

        class_name = str(getattr(target.det, "class_name", "") or "").strip().lower()
        motion_entry = self._motion_policy_state.get(int(target.det.track_id), {})
        track_age_s = float(getattr(target, "age", getattr(target, "persistence", 0.0)) or 0.0)
        displacement = float(motion_entry.get("recent_motion_distance_px", 0.0) or 0.0)
        if track_age_s > 5.0 and class_name in SEMANTIC_IDENTITY_CLASSES and displacement < 18.0:
            return reject("stale_target_block", f"target too old ({track_age_s:.1f}s) with insufficient motion/displacement ({displacement:.1f}px)", {"track_age_s": track_age_s, "displacement_px": displacement}, {"max_age_s": 5.0, "min_displacement_px": 18.0})
        if class_name in SEMANTIC_IDENTITY_CLASSES and self._motion_policy_mode() != "allow_stationary" and not bool(motion_entry.get("motion_allowed", False)):
            return reject("motion_policy", str(motion_entry.get("suppression_reason", "motion policy rejected target") or "motion policy rejected target"), {"motion_allowed": False}, {"motion_policy_mode": self._motion_policy_mode()})
        current_detection = next(
            (det for det in self.last_detections if int(getattr(det, "track_id", -1) or -1) == int(target.det.track_id)),
            None,
        )
        if current_detection is None:
            return reject("target_continuity", "target continuity failed: detection is not current", {}, {"current_frame_required": True})

        decision = self._find_filter_decision_for_track(int(target.det.track_id))
        if decision is None or not bool(getattr(decision, "passed", False)):
            return reject(
                "fresh_target_validation",
                "fresh target validation failed",
                {"track_id": int(target.det.track_id), "decision": str(getattr(decision, "reason", "missing") or "missing")},
                {"filter_decision_pass": True},
            )
        stages.append({"stage": "fresh_target_validation", "inputs": {"track_id": int(target.det.track_id)}, "threshold": {"filter_decision_pass": True}, "pass": True, "reason": "current filter decision passed"})

        shape_info = self._shape_profile_telemetry(current_detection)
        if not bool(shape_info.get("shape_passed", False)):
            return reject("shape_profile", "shape profile rejected", {"shape_profile": shape_info.get("shape_profile_used", "")}, {"aspect_ratio": [shape_info.get("min_aspect_ratio", 0.0), shape_info.get("max_aspect_ratio", 0.0)]})
        stages.append({"stage": "shape_profile", "inputs": {"shape_profile": shape_info.get("shape_profile_used", ""), "aspect_ratio": shape_info.get("aspect_ratio", 0.0)}, "threshold": {"min": shape_info.get("min_aspect_ratio", 0.0), "max": shape_info.get("max_aspect_ratio", 0.0)}, "pass": True, "reason": "shape profile passed"})

        semantic_pass = class_name not in SEMANTIC_IDENTITY_CLASSES or int(getattr(decision, "confirm_hits", 0) or 0) >= max(1, int(getattr(decision, "confirm_required", 1) or 1))
        if not semantic_pass:
            return reject("semantic_confirmation", "semantic confirmation failed", {"hits": int(getattr(decision, "confirm_hits", 0) or 0)}, {"required": int(getattr(decision, "confirm_required", 1) or 1)})
        stages.append({"stage": "semantic_confirmation", "inputs": {"hits": int(getattr(decision, "confirm_hits", 0) or 0)}, "threshold": {"required": int(getattr(decision, "confirm_required", 1) or 1)}, "pass": True, "reason": "semantic confirmation passed"})

        stages.append({"stage": "track_age", "inputs": {"track_age_s": track_age_s}, "threshold": {"stale_block_age_s": 5.0}, "pass": True, "reason": "track age accepted"})

        motion_mode = self._motion_policy_mode()

        # Check motion policy for animal targets in require_recent_motion mode
        if (
            class_name in SEMANTIC_IDENTITY_CLASSES
            and motion_mode != "allow_stationary"
            and not bool(motion_entry.get("motion_allowed", False))
        ):
            self._set_fire_veto_reason(
                str(motion_entry.get("suppression_reason", "motion policy rejected target") or "motion policy rejected target"),
                check_time,
            )
            return False

        motion_distance = float(motion_entry.get("recent_motion_distance_px", 0.0) or 0.0)
        motion_confidence = float(motion_entry.get("motion_confidence", 0.0) or 0.0)
        velocity = float(motion_entry.get("average_velocity_px_s", 0.0) or 0.0)
        motion_pass = class_name not in SEMANTIC_IDENTITY_CLASSES or (motion_distance >= 18.0 and motion_confidence >= float(getattr(eng, "motion_confidence_min", 0.45) or 0.45))
        if not motion_pass:
            return reject("motion_evidence", "meaningful displacement and corroborating motion required", {"displacement_px": motion_distance, "motion_confidence": motion_confidence, "velocity_px_s": velocity}, {"min_displacement_px": 18.0, "min_motion_confidence": float(getattr(eng, "motion_confidence_min", 0.45) or 0.45)})
        stages.append({"stage": "motion_evidence", "inputs": {"displacement_px": motion_distance, "motion_confidence": motion_confidence, "velocity_px_s": velocity}, "threshold": {"min_displacement_px": 18.0, "min_motion_confidence": float(getattr(eng, "motion_confidence_min", 0.45) or 0.45)}, "pass": True, "reason": "motion evidence passed"})

        if not self._person_target_is_fire_authorized(target, check_time):
            return reject("person_fire_authorization", "person identity authorization failed", {"class_name": class_name}, {"authorization_required": True})
        quality_pass = float(target.det.confidence) >= float(eng.fire_trigger_min_confidence) and float(target.persistence) >= float(eng.fire_trigger_min_persistence)
        if not quality_pass:
            return reject("target_quality", "confidence or persistence below fire threshold", {"confidence": float(target.det.confidence), "persistence": float(target.persistence)}, {"min_confidence": float(eng.fire_trigger_min_confidence), "min_persistence": float(eng.fire_trigger_min_persistence)})
        stages.append({"stage": "target_quality", "inputs": {"confidence": float(target.det.confidence), "persistence": float(target.persistence)}, "threshold": {"min_confidence": float(eng.fire_trigger_min_confidence), "min_persistence": float(eng.fire_trigger_min_persistence)}, "pass": True, "reason": "target quality passed"})
        self._last_fire_gate_trace = {"approved": True, "reason": "approved", "stages": stages}
        return True

    def _engagement_pose_freshness_s(self, *, for_fire: bool = False) -> float:
        # ENGAGING needs materially fresher pose than patrol/returning. Fire
        # phase is stricter so micro-adjust and firing never run on delayed
        # debug-board feedback while the target is still moving.  The runtime
        # exports show the current debug-board cadence can land around 0.45 s
        # resets instead of using the measured pose we already have.
        return 0.48 if for_fire else 0.55

    def _engagement_response_scale(self, *, use_fire_limits: bool) -> float:
        speed_value = int(max(10, min(100, int(getattr(self.cfg.engagement, "engagement_speed", 80) or 80))))
        ratio = float(speed_value - 10) / 90.0
        # Scale ranges [0.65, 1.0]: slow presets are dampened, fast presets are
        # at full authority.  Previously exceeded 1.0 at high speeds, which
        # actual servo position, producing visible overshoot on initial lock-on.
        scale = min(1.0, 0.65 + (ratio * 0.85))
        if use_fire_limits:
            scale = min(scale, 1.0)
        return scale

    def _inflight_correction_scale(self, *, use_fire_limits: bool) -> float:
        if use_fire_limits:
            return 1.0
        if not self._has_recent_measured_pose():
            return 1.0

        command_started_at = float(getattr(self, "_last_command_time", 0.0) or 0.0)
        if command_started_at <= 0.0:
            return 1.0

        command_age_s = max(0.0, time.time() - command_started_at)
        settle_window_s = self._command_settle_window_s(0.06)
        if command_age_s >= settle_window_s:
            return 1.0

        remaining_pan = abs(float(self.current_pan) - float(self._last_commanded_pan))
        remaining_tilt = abs(float(self.current_tilt) - float(self._last_commanded_tilt))
        remaining_error = max(remaining_pan, remaining_tilt)
        if remaining_error <= 0.85:
            return 1.0

        progress_scale = max(0.50, min(1.0, command_age_s / max(0.04, settle_window_s)))
        remaining_scale = max(0.60, min(1.0, 1.0 - ((remaining_error - 0.85) / 1.8)))
        return min(progress_scale, remaining_scale)

    def _safe_log_precision_frame(self, **kwargs: object) -> None:
        if not self._log_precision_tuning or self._precision_logging_faulted:
            return
        try:
            self._precision_logger.log_frame(**kwargs)
        except Exception as exc:
            self._precision_logging_faulted = True
            self._log_precision_tuning = False
            self._report_runtime_warning("Precision frame logging disabled after logger failure", exc)

    def _current_no_fire_mask(self) -> Optional[object]:
        mask = find_blocking_mask(self.cfg.no_fire_masks, self.current_pan, self.current_tilt)
        self._last_no_fire_mask_name = str(mask.name) if mask is not None else ""
        return mask

    def _advance_queue(self, now: float) -> None:
        self._queue_index += 1
        self._reset_precision_state()
        if self._queue_index < len(self._queue):
            nxt = self._queue[self._queue_index]
            self.active_order = nxt
            self._remember_active_target(nxt.target.det, target=nxt.target, timestamp=now)
            self._start_order_engagement(nxt, now)
        else:
            self._last_engage_time = now
            self._return_start = now
            self.active_order = None
            self._active_target_last_center = None
            self._active_target_last_bbox = None
            self._active_target_last_heading_norm = (0.0, 0.0)
            self._active_target_last_seen_time = 0.0
            self._active_target_last_class = ""
            self._active_target_last_source = ""
            self._start_return_to_guard(now, immediate_move=True)

    def _start_return_to_guard(self, now: float, *, immediate_move: bool = False) -> None:
        self._last_engage_time = now
        self._return_start = now
        self.active_order = None
        self._active_target_last_center = None
        self._active_target_last_bbox = None
        self._active_target_last_heading_norm = (0.0, 0.0)
        self._active_target_last_seen_time = 0.0
        self._active_target_last_class = ""
        self._active_target_last_source = ""
        self._reset_precision_state()
        if immediate_move or self.cfg.guard.guard_mode == 0:
            gp, gt = self._planner.get_return_position()
            self._move_turret(gp, gt)
        self._change_state(SentryV2State.RETURNING)

    def _start_order_engagement(self, order: EngagementOrder, now: float) -> None:
        """Start engagement with a coarse acquire move before precision."""
        self._reset_precision_state()
        self._remember_active_target(order.target.det, target=order.target, timestamp=now)
        self._record_motion_policy_transition(int(order.target.det.track_id), "ENGAGING", now, "planner selected target")
        # Seed aim anchors to the new order's planned position so that
        # loss recovery (if triggered immediately) searches near the
        # correct target, not the previous engagement's last aim point.
        self._active_target_last_aim_pan = self._clamp_pan(order.pan)
        self._active_target_last_aim_tilt = self._clamp_tilt(order.tilt)
        self._engage_phase = "aim"
        self._phase_start = now
        target = self._find_active_target(order)
        self._issue_coarse_acquire_move(order, target=target, now=now)

    def _coarse_acquire_handoff_tolerances(self) -> Tuple[float, float]:
        eng = self.cfg.engagement
        pan_tol = max(
            2.0,
            float(getattr(eng, "aim_lock_pan_tolerance", 0.65) or 0.65) * 3.0,
            float(getattr(eng, "precision_max_pan_step", getattr(eng, "precision_max_step", 0.85)) or 0.85) * 2.0,
        )
        tilt_tol = max(
            1.6,
            float(getattr(eng, "aim_lock_tilt_tolerance", 0.55) or 0.55) * 3.0,
            float(getattr(eng, "precision_max_tilt_step", getattr(eng, "precision_max_step", 0.85)) or 0.85) * 2.0,
        )
        return float(pan_tol), float(tilt_tol)

    def _needs_additional_coarse_acquire(self, err_pan: float, err_tilt: float) -> bool:
        pan_tol, tilt_tol = self._coarse_acquire_handoff_tolerances()
        return abs(float(err_pan)) > pan_tol or abs(float(err_tilt)) > tilt_tol

    def _coarse_acquire_step(self, err_pan: float, err_tilt: float) -> Tuple[float, float]:
        max_step_pan = max(1.9, float(getattr(self.cfg.engagement, "precision_max_pan_step", 0.0) or 0.0) * 2.35)
        max_step_tilt = max(1.5, float(getattr(self.cfg.engagement, "precision_max_tilt_step", 0.0) or 0.0) * 2.35)
        # Large first errors get a slightly softer cap to reduce initial overshoot,
        # while still keeping acquisition noticeably quick.
        if abs(float(err_pan)) >= 8.0:
            max_step_pan *= 0.82
        if abs(float(err_tilt)) >= 6.0:
            max_step_tilt *= 0.82
        step_pan = max(-max_step_pan, min(max_step_pan, float(err_pan)))
        step_tilt = max(-max_step_tilt, min(max_step_tilt, float(err_tilt)))
        return float(step_pan), float(step_tilt)

    def _issue_coarse_acquire_move(
        self,
        order: EngagementOrder,
        *,
        target: Optional[TrackedTarget],
        now: float,
    ) -> None:
        if target is not None:
            # Initial acquire must be derived from live target position, but keep
            # the first jump bounded to avoid abrupt moves from stale queue plans.
            # Use raw (non-predictive) target error for the first acquire move;
            # predictive lead can overshoot during guard->engage handoff.
            err_pan, err_tilt = self._compute_target_angle_error(target.det)
            self._record_active_target_solution(target, now, err_pan, err_tilt)
            step_pan, step_tilt = self._coarse_acquire_step(err_pan, err_tilt)
            self._move_turret(self.current_pan + step_pan, self.current_tilt + step_tilt)
        else:
            self._move_turret(order.pan, order.tilt)

    def _has_visible_reacquire_candidate(self) -> bool:
        if not self.last_targets:
            return False
        anchor_class = str(getattr(self, "_active_target_last_class", "") or "").strip().lower()
        min_score = float(self.cfg.engagement.min_threat_score)
        min_conf = max(
            0.35,
            float(getattr(self.cfg.target_filter, "min_confidence", 0.5) or 0.5) * 0.72,
        )
        relaxed_score = max(0.30, min_score * 0.65)
        for target in self.last_targets:
            det = target.det
            class_name = str(det.class_name or "").strip().lower()
            if anchor_class and anchor_class not in NON_SEMANTIC_REACQUIRE_CLASSES and class_name != anchor_class:
                continue
            if float(det.confidence) < min_conf:
                continue
            if float(target.threat_score) >= relaxed_score or float(target.persistence) >= 0.10:
                return True
        return False

    def _enter_precision_phase(self, now: float, order: EngagementOrder) -> None:
        """Switch to precision phase after the coarse acquire stage has settled."""
        self._engage_phase = "precision"
        self._phase_start = now
        self._reset_precision_state()

        target = self._find_active_target(order)
        if not self._log_precision_tuning or self._precision_logging_faulted:
            return

        target_id = str(target.det.track_id) if target is not None else "unknown"
        config_snapshot = {
            "precision_kp": float(self.cfg.engagement.precision_kp),
            "precision_ki": float(self.cfg.engagement.precision_ki),
            "precision_kd": float(self.cfg.engagement.precision_kd),
            "precision_deadzone_pan_deg": float(self.cfg.engagement.precision_deadzone_pan_deg),
            "precision_deadzone_tilt_deg": float(self.cfg.engagement.precision_deadzone_tilt_deg),
            "precision_settle_time": float(self.cfg.engagement.precision_settle_time),
            "precision_max_step": float(self.cfg.engagement.precision_max_step),
            "precision_max_pan_step": float(self.cfg.engagement.precision_max_pan_step),
            "precision_max_tilt_step": float(self.cfg.engagement.precision_max_tilt_step),
        }
        detection_mode = int(getattr(self.cfg.detection_mode, "detection_mode", 0))
        try:
            self._precision_logger.start_engagement(target_id, detection_mode, config_snapshot)
            self._current_precision_engagement_id = target_id
        except Exception as exc:
            self._precision_logging_faulted = True
            self._log_precision_tuning = False
            self._current_precision_engagement_id = None
            self._report_runtime_warning("Precision session start failed; precision logging disabled", exc)

    def _begin_fire(self, order: EngagementOrder, now: float) -> None:
        """Transition to fire phase — respects auto_trigger_enabled gate."""
        if not self._target_meets_fire_requirements(order.target, now=now):
            self._trigger_gate_active = False
            self._trigger_hold_start = 0.0
            self._emit_engagement_telemetry(
                now=now,
                order=order,
                target=order.target,
                attempt_type="final",
                firing_approved=False,
                firing_rejected_reason=str((self._last_fire_gate_trace or {}).get("reason", "target_fire_authorization_failed")),
                stages=list((self._last_fire_gate_trace or {}).get("stages", []) or []),
            )
            return

        self._record_motion_policy_transition(int(order.target.det.track_id), "FIRE_AUTHORIZATION", now, "final fire gate entered")

        blocked_mask = self._current_no_fire_mask()
        prompted_auto_fire_allowed = True
        if str(getattr(order.target.det, "source", "")) == "prompted":
            prompted_auto_fire_allowed = bool(getattr(self.cfg, "prompted_allow_auto_fire", False))
        self._engage_phase = "fire"
        self._phase_start = now
        self._trigger_gate_active = False
        self._trigger_hold_start = 0.0
        self._trigger_refractory_until = max(
            self._trigger_refractory_until,
            now + float(self.cfg.engagement.fire_trigger_refractory_time),
        )

        # Log manual fire to ML training logger if enabled
        if self._log_ml_training:
            target = order.target
            self._ml_logger.log_manual_fire(
                target.det,
                speed=target.speed,
                persistence=target.persistence,
                approach_rate=target.approach_rate,
            )
            self._ml_logger.save()

        # =================================================================================
        # AUTO-TRIGGER FIRE GATE — DO NOT MODIFY WITHOUT OWNER APPROVAL (GMDS22)
        # This is the sole check that gates physical firing. The conditions:
        #   1. auto_trigger_enabled must be True (user-controlled default=OFF toggle)
        #   2. No active no-fire mask at current turret position
        #   3. "prompted" targets require prompted_allow_auto_fire flag
        # DO NOT add new conditions here. DO NOT add silent disablers elsewhere.
        # =================================================================================
        fired = (
            self.cfg.engagement.auto_trigger_enabled
            and blocked_mask is None
            and prompted_auto_fire_allowed
        )

        final_stages: List[Dict[str, Any]] = [
            {
                "stage": "auto_trigger_enabled",
                "inputs": {"auto_trigger_enabled": bool(self.cfg.engagement.auto_trigger_enabled)},
                "threshold": {"required": True},
                "pass": bool(self.cfg.engagement.auto_trigger_enabled),
                "reason": "auto-trigger enabled" if bool(self.cfg.engagement.auto_trigger_enabled) else "planner veto",
            },
            {
                "stage": "no_fire_mask",
                "inputs": {"active_mask": str(getattr(blocked_mask, "name", "") if blocked_mask is not None else "")},
                "threshold": {"requires_clear_mask": True},
                "pass": bool(blocked_mask is None),
                "reason": "mask clear" if blocked_mask is None else "mask block",
            },
            {
                "stage": "prompted_auto_fire_policy",
                "inputs": {"source": str(getattr(order.target.det, "source", "") or "")},
                "threshold": {"prompted_allow_auto_fire": bool(getattr(self.cfg, "prompted_allow_auto_fire", False))},
                "pass": bool(prompted_auto_fire_allowed),
                "reason": "prompted policy satisfied" if prompted_auto_fire_allowed else "planner veto",
            },
        ]

        if fired:
            final_reason = "approved"
        elif not bool(self.cfg.engagement.auto_trigger_enabled):
            final_reason = "auto_trigger_disabled"
        elif blocked_mask is not None:
            final_reason = "mask_block"
        elif not prompted_auto_fire_allowed:
            final_reason = "prompted_auto_fire_disabled"
        else:
            final_reason = "unknown rejection path"

        self._emit_engagement_telemetry(
            now=now,
            order=order,
            target=order.target,
            attempt_type="final",
            firing_approved=bool(fired),
            firing_rejected_reason=final_reason,
            stages=list((self._last_fire_gate_trace or {}).get("stages", []) or []) + final_stages,
        )

        if fired:
            burst = self.cfg.engagement.burst_count
            if self._cb_fire:
                self._cb_fire(burst)
                self._note_stationary_release_fire(order.target.det, now)
            self._record_motion_policy_transition(int(order.target.det.track_id), "FIRED", now, "fire callback executed")
            self._record_motion_policy_transition(int(order.target.det.track_id), "POST_ENGAGEMENT", now, "post-fire cooldown")
            self.engagement_log.append({
                "track_id": order.target.det.track_id,
                "class": order.target.det.class_name,
                "threat": round(order.target.threat_score, 2),
                "pan": round(order.pan, 1),
                "tilt": round(order.tilt, 1),
                "time": now,
                "fired": fired,
                "blocked_by_mask": str(blocked_mask.name) if blocked_mask is not None else "",
            })
        # Keep log bounded
        if len(self.engagement_log) > 100:
            self.engagement_log = self.engagement_log[-100:]

    def _reset_precision_state(self) -> None:
        self._pid_integral_pan = 0.0
        self._pid_integral_tilt = 0.0
        self._pid_prev_err_pan = 0.0
        self._pid_prev_err_tilt = 0.0
        self._smoothed_err_pan = 0.0
        self._smoothed_err_tilt = 0.0
        self._err_pan_rate_deg_s = 0.0
        self._err_tilt_rate_deg_s = 0.0
        self._last_error_sample_time = 0.0
        self._aim_lock_frames = 0
        self._target_lost_since = 0.0
        self._trigger_hold_start = 0.0
        self._trigger_gate_active = False
        self._clear_active_reacquire_confirm_pending()
        self._reset_loss_recovery_state()

    def _compute_target_angle_error(self, det: DetectedObject) -> Tuple[float, float]:
        fw = float(max(1, det.frame_width or self.cfg.guard.frame_width or 640))
        fh = float(max(1, det.frame_height or self.cfg.guard.frame_height or 480))
        norm_cx = float(det.center_x) / fw
        norm_cy = float(det.center_y) / fh
        return self._planner.pixel_error_to_angle_error(norm_cx, norm_cy)

    def _compute_tracking_angle_error(
        self,
        target: TrackedTarget,
        now: float,
        *,
        for_fire: bool,
    ) -> Tuple[float, float]:
        raw_err_pan, raw_err_tilt = self._compute_target_angle_error(target.det)
        eng = self.cfg.engagement
        if not self._prediction_enabled_for_target(target):
            return raw_err_pan, raw_err_tilt

        lead_time = max(0.0, float(getattr(eng, "predictive_lead_time_s", 0.0) or 0.0))
        if for_fire:
            lead_time += max(0.0, float(getattr(eng, "predictive_fire_extra_lead_s", 0.0) or 0.0))
        min_persistence = max(0.05, float(getattr(eng, "predictive_min_persistence_s", 0.18) or 0.18))
        lead_scale = min(1.0, max(0.0, float(target.persistence) / min_persistence))
        lead_time *= lead_scale
        if lead_time <= 0.0:
            return raw_err_pan, raw_err_tilt

        heading_x, heading_y = self._clamp_prediction_heading_norm(
            float(target.heading_x),
            float(target.heading_y),
            lead_time,
        )
        predicted_norm_cx = max(0.0, min(1.0, float(target.det.norm_cx) + (heading_x * lead_time)))
        predicted_norm_cy = max(0.0, min(1.0, float(target.det.norm_cy) + (heading_y * lead_time)))
        pred_err_pan, pred_err_tilt = self._planner.pixel_error_to_angle_error(predicted_norm_cx, predicted_norm_cy)
        max_lead_pan = max(0.0, float(getattr(eng, "predictive_max_lead_pan_deg", 0.0) or 0.0))
        lead_pan = max(-max_lead_pan, min(max_lead_pan, pred_err_pan - raw_err_pan))
        # Screen-space vertical motion is easily polluted by the turret's own tilt
        # movement, which can make live tracking climb away from the target.
        # Keep raw visual centering on tilt and reserve prediction for pan only.
        lead_tilt = 0.0
        return raw_err_pan + lead_pan, raw_err_tilt + lead_tilt

    def _record_active_target_solution(
        self,
        target: TrackedTarget,
        now: float,
        aim_err_pan: float,
        aim_err_tilt: float,
    ) -> None:
        self._remember_active_target(target.det, target=target, timestamp=now)
        self._active_target_last_aim_pan = self._clamp_pan(self.current_pan + float(aim_err_pan))
        self._active_target_last_aim_tilt = self._clamp_tilt(self.current_tilt + float(aim_err_tilt))

    def _active_target_heading_norm(self, reference_window_s: float) -> Tuple[float, float]:
        if not self._stored_target_is_prediction_eligible():
            return 0.0, 0.0
        return self._clamp_prediction_heading_norm(
            float(self._active_target_last_heading_norm[0]),
            float(self._active_target_last_heading_norm[1]),
            max(0.08, float(reference_window_s)),
        )

    def _active_target_heading_deg_s(self, reference_window_s: float) -> Tuple[float, float]:
        heading_x, heading_y = self._active_target_heading_norm(reference_window_s)
        return (
            float(heading_x) * float(self.cfg.guard.camera_hfov),
            -(float(heading_y) * float(self.cfg.guard.camera_vfov)),
        )

    def _prediction_enabled_for_target(self, target: TrackedTarget) -> bool:
        eng = self.cfg.engagement
        if not bool(getattr(eng, "predictive_aim_enabled", True)):
            return False
        class_name = str(target.det.class_name or "").strip().lower()
        source_name = str(target.det.source or "").strip().lower()
        if class_name in NON_SEMANTIC_PREDICTION_CLASSES:
            return False
        if source_name in {"frame_diff", "backsub", "color"}:
            return False
        min_persistence = max(0.05, float(getattr(eng, "predictive_min_persistence_s", 0.18) or 0.18))
        if float(target.persistence) < min_persistence:
            return False
        if int(getattr(target, "history_samples", 0) or 0) < 4:
            return False
        if float(getattr(target, "heading_stability", 0.0) or 0.0) < 0.60:
            return False
        return True

    def _stored_target_is_prediction_eligible(self) -> bool:
        if self._active_target_last_class in NON_SEMANTIC_PREDICTION_CLASSES:
            return False
        if self._active_target_last_source in {"frame_diff", "backsub", "color"}:
            return False
        if int(self._active_target_last_history_samples or 0) < 4:
            return False
        if float(self._active_target_last_heading_stability or 0.0) < 0.60:
            return False
        return True

    def _clamp_prediction_heading_norm(
        self,
        heading_x: float,
        heading_y: float,
        lead_time_s: float,
    ) -> Tuple[float, float]:
        eng = self.cfg.engagement
        lead_time = max(0.08, float(lead_time_s))
        max_lead_pan = max(0.1, float(getattr(eng, "predictive_max_lead_pan_deg", 0.0) or 0.0))
        max_lead_tilt = max(0.1, float(getattr(eng, "predictive_max_lead_tilt_deg", 0.0) or 0.0))
        max_norm_x = max_lead_pan / max(1.0, float(self.cfg.guard.camera_hfov))
        max_norm_y = max_lead_tilt / max(1.0, float(self.cfg.guard.camera_vfov))
        max_heading_x = max_norm_x / lead_time
        max_heading_y = max_norm_y / lead_time
        return (
            max(-max_heading_x, min(max_heading_x, float(heading_x))),
            max(-max_heading_y, min(max_heading_y, float(heading_y))),
        )

    def _loss_recovery_enabled(self) -> bool:
        eng = self.cfg.engagement
        if not bool(getattr(eng, "loss_recovery_enabled", True)):
            return False
        if self._pir_cue_mode or self._pir_scan_mode:
            return False
        return bool(
            getattr(eng, "loss_direction_pursuit_enabled", True)
            or getattr(eng, "loss_local_search_enabled", True)
            or getattr(eng, "loss_expanding_search_enabled", True)
        )

    def _adaptive_loss_recovery_enabled(self) -> bool:
        return bool(getattr(self.cfg.engagement, "adaptive_loss_recovery_enabled", True))

    def _normalized_search_style(self, style: object) -> str:
        text = str(style or "hunting").strip().lower()
        if text in {"fast", "fast_reacquire", "fast-reacquire", "reacquire"}:
            return "fast_reacquire"
        return "hunting"

    def _loss_search_style(self) -> str:
        return self._normalized_search_style(getattr(self.cfg.engagement, "loss_search_style", "hunting"))

    def _loss_search_rounds(self) -> int:
        return max(1, int(getattr(self.cfg.engagement, "loss_search_rounds", 1) or 1))

    def _pir_cue_hold_time(self) -> float:
        configured = float(getattr(self.cfg.pir_guard, "cue_hold_time_s", 0.18) or 0.18)
        configured = max(0.05, min(configured, float(getattr(self.cfg.pir_guard, "confirmation_timeout", 1.2) or 1.2)))
        if self._normalized_search_style(getattr(self.cfg.pir_guard, "search_style", "hunting")) == "fast_reacquire":
            return min(configured, 0.14)
        return configured

    def _finish_pir_no_target(self) -> None:
        """Clear the active PIR cue and explicitly command a return home."""
        active_sensor_id = int(getattr(self, "_pir_cue_sensor_id", -1))
        self._pir_cue_mode = False
        self._pir_cue_sensor_id = -1
        self._pir_scan_mode = False
        self._pir_scan_awaiting_settle = False
        self._pir_settle_start = 0.0
        self._pir_manager.complete_active_cue()
        gp, gt = self._planner.get_return_position()
        sensor_text = f" S{active_sensor_id + 1}" if active_sensor_id >= 0 else ""
        self._set_pir_note(f"PIR no target{sensor_text} -> return home {gp:.1f}/{gt:.1f}")
        self._emit_pir_trace(
            "pir_no_target_return_home",
            sensor_id=active_sensor_id,
            return_pan=float(gp),
            return_tilt=float(gt),
            queue_length=int(self._pir_manager.peek_queue_count()),
        )
        self._move_turret(gp, gt)
        self._patrol_initialized = False
        self._patrol_last_update = 0.0

    def _loss_search_step_interval(self, phase: str) -> float:
        base = max(0.08, float(getattr(self.cfg.engagement, "loss_search_step_interval_s", 0.18) or 0.18))
        style = self._loss_search_style()
        phase_key = str(phase or "local_search")
        if "expand" in phase_key:
            scale = 1.00 if style == "fast_reacquire" else 1.22
        elif "handoff" in phase_key:
            scale = 0.90 if style == "fast_reacquire" else 1.08
        else:
            scale = 0.96 if style == "fast_reacquire" else 1.15
        return float(max(0.11, min(0.45, base * scale)))

    def _search_point_distance(
        self,
        source: Tuple[float, float],
        target: Tuple[float, float],
    ) -> float:
        pan_delta = abs(float(target[0]) - float(source[0]))
        tilt_delta = abs(float(target[1]) - float(source[1]))
        return pan_delta + (tilt_delta * 1.15)

    def _smooth_search_path(
        self,
        points: List[Tuple[float, float]],
        start_pan: float,
        start_tilt: float,
    ) -> List[Tuple[float, float]]:
        remaining = list(points)
        ordered: List[Tuple[float, float]] = []
        current = (float(start_pan), float(start_tilt))
        while remaining:
            next_index = min(
                range(len(remaining)),
                key=lambda idx: self._search_point_distance(current, remaining[idx]),
            )
            point = remaining.pop(next_index)
            ordered.append(point)
            current = point
        return ordered

    def _apply_loss_search_rounds(
        self,
        points: List[Tuple[float, float]],
        center_pan: float,
        center_tilt: float,
    ) -> List[Tuple[float, float]]:
        rounds = self._loss_search_rounds()
        if not points:
            return []

        style = self._loss_search_style()
        scale_step = 0.18 if style == "fast_reacquire" else 0.12
        ordered_points: List[Tuple[float, float]] = []
        seen: set[Tuple[float, float]] = set()
        start_pan = float(center_pan)
        start_tilt = float(center_tilt)

        for round_index in range(rounds):
            scale = 1.0 + (scale_step * round_index)
            round_points: List[Tuple[float, float]] = []
            round_seen: set[Tuple[float, float]] = set()
            for point_pan, point_tilt in points:
                scaled_point = (
                    self._clamp_pan(center_pan + ((point_pan - center_pan) * scale)),
                    self._clamp_tilt(center_tilt + ((point_tilt - center_tilt) * scale)),
                )
                if scaled_point in round_seen:
                    continue
                round_seen.add(scaled_point)
                round_points.append(scaled_point)
            for point in self._smooth_search_path(round_points, start_pan, start_tilt):
                if point in seen:
                    continue
                seen.add(point)
                ordered_points.append(point)
            if ordered_points:
                start_pan, start_tilt = ordered_points[-1]

        return ordered_points

    def _active_recovery_order(self) -> Optional[EngagementOrder]:
        if 0 <= self._queue_index < len(self._queue):
            return self._queue[self._queue_index]
        return self.active_order

    def _best_loss_recovery_alternative_target(self) -> Optional[TrackedTarget]:
        order = self._active_recovery_order()
        exclude_track_id = int(order.target.det.track_id) if order is not None else -1
        best_target: Optional[TrackedTarget] = None
        best_score = float("-inf")
        for target in self.last_targets:
            if int(target.det.track_id) == exclude_track_id:
                continue
            if target.threat_score < (self.cfg.engagement.min_threat_score * 0.70):
                continue
            if best_target is None or target.threat_score > best_score:
                best_target = target
                best_score = float(target.threat_score)
        return best_target

    def _capture_loss_recovery_context(self, now: float) -> None:
        order = self._active_recovery_order()
        best_alternative = self._best_loss_recovery_alternative_target()
        visible_count = len(self.last_targets)
        crowd_threshold = max(1, int(getattr(self.cfg.engagement, "loss_scene_crowding_threshold", 3) or 3))
        lost_track_id = int(order.target.det.track_id) if order is not None else -1
        lost_threat = float(order.target.threat_score) if order is not None else 0.0
        lost_persistence = float(getattr(order.target, "persistence", 0.0) or 0.0) if order is not None else 0.0
        self._loss_recovery_context = {
            "lost_track_id": lost_track_id,
            "lost_target_threat": lost_threat,
            "lost_target_persistence": lost_persistence,
            "visible_target_count": visible_count,
            "scene_sparse": visible_count < crowd_threshold,
            "scene_crowded": visible_count >= crowd_threshold,
            "best_alternative_score": float(best_alternative.threat_score) if best_alternative is not None else 0.0,
            "started_at": now,
        }

    def _select_loss_recovery_protocol(self) -> str:
        eng = self.cfg.engagement
        visible_count = len(self.last_targets)
        self._loss_recovery_context["visible_target_count"] = visible_count
        crowd_threshold = max(1, int(getattr(eng, "loss_scene_crowding_threshold", 3) or 3))
        self._loss_recovery_context["scene_sparse"] = visible_count < crowd_threshold
        self._loss_recovery_context["scene_crowded"] = visible_count >= crowd_threshold
        if visible_count > 0:
            return str(getattr(eng, "loss_recovery_protocol_new_target", "rapid_handoff_search") or "rapid_handoff_search")
        return str(getattr(eng, "loss_recovery_protocol_no_detection", "persistent_reacquire_search") or "persistent_reacquire_search")

    def _should_switch_to_visible_target(self, target: TrackedTarget) -> bool:
        lost_score = float(self._loss_recovery_context.get("lost_target_threat", 0.0) or 0.0)
        lost_persistence = float(self._loss_recovery_context.get("lost_target_persistence", 0.0) or 0.0)
        margin = max(0.0, float(getattr(self.cfg.engagement, "loss_switch_score_margin", 0.12) or 0.12))
        persistence_bias = max(0.0, float(getattr(self.cfg.engagement, "loss_switch_persistence_bias", 0.05) or 0.05))
        required_score = lost_score + margin + (lost_persistence * persistence_bias)
        if bool(self._loss_recovery_context.get("scene_crowded", False)):
            required_score -= margin * 0.45
        return float(target.threat_score) >= required_score

    def _handoff_to_visible_target(self, target: TrackedTarget, now: float) -> None:
        order = self._active_recovery_order()
        if order is None:
            return
        pan, tilt = self._planner._pixel_to_pantilt(target, self.current_pan, self.current_tilt)
        order.target = target
        order.pan = pan
        order.tilt = tilt
        self.active_order = order
        self._target_lost_since = 0.0
        self._reset_loss_recovery_state()
        self._remember_active_target(target.det, target=target, timestamp=now)
        self._last_reacquire_note = f"loss handoff -> {int(target.det.track_id)}"
        self._last_reacquire_time = now
        self._start_order_engagement(order, now)

    def _loss_recovery_personality_profile(self) -> Dict[str, float]:
        eng = self.cfg.engagement
        intensity = max(0.0, float(getattr(eng, "loss_personality_intensity", 0.35) or 0.35))
        velocity_bias = max(0.0, float(getattr(eng, "loss_personality_velocity_bias", 0.40) or 0.40))
        order_variation = max(0.0, float(getattr(eng, "loss_personality_order_variation", 0.30) or 0.30))
        seed = int(self._loss_recovery_context.get("lost_track_id", 0) or 0) * 131
        seed += (self._loss_recovery_retry_count + 1) * 17
        rng = random.Random(seed)
        heading_pan, heading_tilt = self._active_target_heading_norm(0.12)
        pan_bias = (heading_pan * velocity_bias) + (rng.uniform(-0.45, 0.45) * order_variation)
        tilt_bias = (heading_tilt * velocity_bias) + (rng.uniform(-0.35, 0.35) * order_variation)
        return {
            "pan_bias": pan_bias * intensity,
            "tilt_bias": tilt_bias * intensity,
            "intensity": intensity,
        }

    def _start_loss_recovery(self, now: float) -> None:
        if not self._loss_recovery_enabled():
            self._reset_loss_recovery_state()
            return
        self._capture_loss_recovery_context(now)
        # Start the first recovery pass from the live runtime pose rather than
        # the last requested aim point so reacquire does not chase a target from
        # a commanded pose the turret never physically reached.
        self._loss_recovery_anchor_pan = float(self.current_pan)
        self._loss_recovery_anchor_tilt = float(self.current_tilt)
        self._loss_recovery_last_move_time = 0.0
        self._loss_recovery_search_index = 0
        self._loss_recovery_protocol = self._select_loss_recovery_protocol()
        self._loss_recovery_phase = self._loss_recovery_protocol
        self._last_reacquire_note = "loss pursuit"
        self._last_reacquire_time = now

    def _reset_loss_recovery_state(self) -> None:
        self._loss_recovery_phase = ""
        self._loss_recovery_protocol = ""
        self._loss_recovery_context = {}
        self._loss_recovery_retry_count = 0
        self._loss_recovery_anchor_pan = float(self.current_pan)
        self._loss_recovery_anchor_tilt = float(self.current_tilt)
        self._loss_recovery_last_move_time = 0.0
        self._loss_recovery_search_index = 0

    def _should_retry_loss_recovery(self) -> bool:
        if not bool(getattr(self.cfg.engagement, "continuous_hunt_on_loss", False)):
            return False
        if int(getattr(self.cfg.guard, "guard_mode", 0) or 0) == 0:
            return False
        if self._adaptive_loss_recovery_enabled():
            visible_count = int(self._loss_recovery_context.get("visible_target_count", 0) or 0)
            crowd_threshold = max(1, int(getattr(self.cfg.engagement, "loss_scene_crowding_threshold", 3) or 3))
            max_retries = int(getattr(self.cfg.engagement, "loss_persistent_retry_passes_sparse", 2) or 2)
            if visible_count >= crowd_threshold:
                max_retries = int(getattr(self.cfg.engagement, "loss_persistent_retry_passes_crowded", 1) or 1)
            return self._loss_recovery_retry_count < max(0, max_retries - 1)
        return self._loss_recovery_retry_count < 1

    def _restart_loss_recovery(self, now: float) -> None:
        self._loss_recovery_retry_count += 1
        self._target_lost_since = now
        self._capture_loss_recovery_context(now)
        self._loss_recovery_anchor_pan = float(self.current_pan)
        self._loss_recovery_anchor_tilt = float(self.current_tilt)
        self._loss_recovery_last_move_time = 0.0
        self._loss_recovery_search_index = 0
        self._loss_recovery_protocol = self._select_loss_recovery_protocol()
        self._loss_recovery_phase = self._loss_recovery_protocol
        self._last_reacquire_note = "loss retry"
        self._last_reacquire_time = now
        self._aim_lock_frames = 0
        self._last_err_pan_deg = 0.0
        self._last_err_tilt_deg = 0.0

    def _update_loss_recovery(self, now: float) -> None:
        if self._target_lost_since <= 0.0 or not self._loss_recovery_enabled():
            return

        # If credible targets are visible, stop the search and let the main loop reacquire immediately
        if self.last_targets:
            min_score = self.cfg.engagement.min_threat_score
            if any(target.threat_score >= min_score for target in self.last_targets):
                return
        if self._has_visible_reacquire_candidate():
            return

        if self._adaptive_loss_recovery_enabled():
            best_alternative = self._best_loss_recovery_alternative_target()
            if best_alternative is not None:
                self._loss_recovery_context["best_alternative_score"] = float(best_alternative.threat_score)
                if self._should_switch_to_visible_target(best_alternative):
                    self._handoff_to_visible_target(best_alternative, now)
                    return
            protocol = self._select_loss_recovery_protocol()
            if protocol != self._loss_recovery_protocol:
                self._loss_recovery_protocol = protocol
                self._loss_recovery_search_index = 0

        eng = self.cfg.engagement
        loss_elapsed = max(0.0, now - self._target_lost_since)
        timeout = max(0.1, float(eng.target_loss_timeout))
        if loss_elapsed >= timeout:
            return

        if self._adaptive_loss_recovery_enabled() and self._loss_recovery_protocol == "rapid_handoff_search":
            self._update_rapid_handoff_recovery(now, loss_elapsed, timeout)
            return
        if self._adaptive_loss_recovery_enabled() and self._loss_recovery_protocol == "persistent_reacquire_search":
            self._update_persistent_recovery(now, loss_elapsed, timeout)
            return
        pursuit_window = min(
            max(0.0, float(getattr(eng, "loss_direction_pursuit_s", 0.0) or 0.0)),
            timeout * 0.55,
        )

        if (
            bool(getattr(eng, "loss_direction_pursuit_enabled", True))
            and pursuit_window > 0.0
            and loss_elapsed <= pursuit_window
        ):
            if self._loss_recovery_phase != "pursuit":
                self._loss_recovery_phase = "pursuit"
                self._last_reacquire_note = "loss pursuit"
                self._last_reacquire_time = now
            if (now - self._loss_recovery_last_move_time) >= 0.08:
                heading_pan_deg_s, heading_tilt_deg_s = self._active_target_heading_deg_s(loss_elapsed + 0.08)
                lookahead = min(pursuit_window, loss_elapsed + float(getattr(eng, "predictive_lead_time_s", 0.0) or 0.0))
                pursuit_pan = self._loss_recovery_anchor_pan + (heading_pan_deg_s * lookahead)
                pursuit_tilt = self._loss_recovery_anchor_tilt + (heading_tilt_deg_s * lookahead)
                self._move_loss_recovery_target(pursuit_pan, pursuit_tilt, now)
            return

        local_points = self._loss_recovery_local_search_points(pursuit_window)
        expanding_points = self._loss_recovery_expanding_search_points(pursuit_window)
        search_points: List[Tuple[float, float]] = []
        search_points.extend(local_points)
        search_points.extend(expanding_points)
        if not search_points:
            return
        local_count = len(local_points)
        point_index = min(self._loss_recovery_search_index, len(search_points) - 1)
        next_phase = "local_search" if point_index < local_count else "expanding_search"
        step_interval = self._loss_search_step_interval(next_phase)
        if (now - self._loss_recovery_last_move_time) < step_interval:
            return
        if self._loss_recovery_phase != next_phase:
            self._loss_recovery_phase = next_phase
            self._last_reacquire_note = "loss local scan" if next_phase == "local_search" else "loss expanding scan"
            self._last_reacquire_time = now
        point = search_points[min(self._loss_recovery_search_index, len(search_points) - 1)]
        if self._loss_recovery_search_index < (len(search_points) - 1):
            self._loss_recovery_search_index += 1
        self._move_loss_recovery_target(point[0], point[1], now)

    def _update_rapid_handoff_recovery(self, now: float, loss_elapsed: float, timeout: float) -> None:
        eng = self.cfg.engagement
        handoff_timeout = min(timeout, max(0.12, float(getattr(eng, "loss_handoff_max_duration_s", 0.38) or 0.38)))
        if loss_elapsed >= handoff_timeout:
            return
        pursuit_window = min(handoff_timeout * 0.45, max(0.0, float(getattr(eng, "loss_handoff_pursuit_time_s", 0.14) or 0.14)))
        if pursuit_window > 0.0 and loss_elapsed <= pursuit_window:
            if self._loss_recovery_phase != "rapid_handoff_search:pursuit":
                self._loss_recovery_phase = "rapid_handoff_search:pursuit"
                self._last_reacquire_note = "rapid handoff pursuit"
                self._last_reacquire_time = now
            if (now - self._loss_recovery_last_move_time) >= 0.06:
                heading_pan_deg_s, heading_tilt_deg_s = self._active_target_heading_deg_s(loss_elapsed + 0.06)
                lookahead = min(pursuit_window, loss_elapsed + float(getattr(eng, "predictive_lead_time_s", 0.0) or 0.0))
                pursuit_pan = self._loss_recovery_anchor_pan + (heading_pan_deg_s * lookahead)
                pursuit_tilt = self._loss_recovery_anchor_tilt + (heading_tilt_deg_s * lookahead)
                self._move_loss_recovery_target(pursuit_pan, pursuit_tilt, now)
            return
        step_interval = self._loss_search_step_interval("rapid_handoff_search:scan")
        if (now - self._loss_recovery_last_move_time) < step_interval:
            return
        points = self._rapid_handoff_search_points(pursuit_window)
        if not points:
            return
        point_index = min(self._loss_recovery_search_index, len(points) - 1)
        self._loss_recovery_phase = "rapid_handoff_search:scan"
        self._last_reacquire_note = "rapid handoff scan"
        self._last_reacquire_time = now
        point = points[point_index]
        if self._loss_recovery_search_index < (len(points) - 1):
            self._loss_recovery_search_index += 1
        self._move_loss_recovery_target(point[0], point[1], now)

    def _update_persistent_recovery(self, now: float, loss_elapsed: float, timeout: float) -> None:
        eng = self.cfg.engagement
        pursuit_window = min(
            max(0.0, float(getattr(eng, "loss_direction_pursuit_s", 0.0) or 0.0)),
            timeout * 0.45,
        )
        if pursuit_window > 0.0 and loss_elapsed <= pursuit_window:
            if self._loss_recovery_phase != "persistent_reacquire_search:pursuit":
                self._loss_recovery_phase = "persistent_reacquire_search:pursuit"
                self._last_reacquire_note = "persistent pursuit"
                self._last_reacquire_time = now
            if (now - self._loss_recovery_last_move_time) >= 0.08:
                heading_pan_deg_s, heading_tilt_deg_s = self._active_target_heading_deg_s(loss_elapsed + 0.08)
                lookahead = min(pursuit_window, loss_elapsed + float(getattr(eng, "predictive_lead_time_s", 0.0) or 0.0))
                pursuit_pan = self._loss_recovery_anchor_pan + (heading_pan_deg_s * lookahead)
                pursuit_tilt = self._loss_recovery_anchor_tilt + (heading_tilt_deg_s * lookahead)
                self._move_loss_recovery_target(pursuit_pan, pursuit_tilt, now)
            return
        points = self._persistent_loss_recovery_points(pursuit_window)
        if not points:
            return
        point_index = min(self._loss_recovery_search_index, len(points) - 1)
        local_count = min(len(points), len(self._loss_recovery_local_search_points(pursuit_window)))
        next_phase = (
            "persistent_reacquire_search:local"
            if point_index < local_count else
            "persistent_reacquire_search:expand"
        )
        step_interval = self._loss_search_step_interval(next_phase)
        if (now - self._loss_recovery_last_move_time) < step_interval:
            return
        self._loss_recovery_phase = next_phase
        self._last_reacquire_note = "persistent reacquire"
        self._last_reacquire_time = now
        point = points[point_index]
        if self._loss_recovery_search_index < (len(points) - 1):
            self._loss_recovery_search_index += 1
        self._move_loss_recovery_target(point[0], point[1], now)

    def _loss_recovery_search_origin(self, pursuit_window: float) -> Tuple[float, float]:
        heading_pan_deg_s, heading_tilt_deg_s = self._active_target_heading_deg_s(max(0.08, pursuit_window))
        center_pan = self._loss_recovery_anchor_pan + (heading_pan_deg_s * max(0.0, pursuit_window))
        center_tilt = self._loss_recovery_anchor_tilt + (heading_tilt_deg_s * max(0.0, pursuit_window))
        if self._adaptive_loss_recovery_enabled():
            profile = self._loss_recovery_personality_profile()
            pan_span = max(0.6, float(getattr(self.cfg.engagement, "loss_local_search_pan_deg", 3.5) or 3.5))
            tilt_span = max(0.4, float(getattr(self.cfg.engagement, "loss_local_search_tilt_deg", 2.0) or 2.0))
            center_pan += pan_span * 0.18 * float(profile.get("pan_bias", 0.0) or 0.0)
            center_tilt += tilt_span * 0.14 * float(profile.get("tilt_bias", 0.0) or 0.0)
        return center_pan, center_tilt

    def _loss_recovery_local_search_points(self, pursuit_window: float) -> List[Tuple[float, float]]:
        if not bool(getattr(self.cfg.engagement, "loss_local_search_enabled", True)):
            return []
        center_pan, center_tilt = self._loss_recovery_search_origin(pursuit_window)
        pan_span = max(0.6, float(getattr(self.cfg.engagement, "loss_local_search_pan_deg", 3.5) or 3.5))
        tilt_span = max(0.4, float(getattr(self.cfg.engagement, "loss_local_search_tilt_deg", 2.0) or 2.0))
        profile: Dict[str, float] = {}
        if self._adaptive_loss_recovery_enabled():
            profile = self._loss_recovery_personality_profile()
            pan_span *= 1.0 + (0.20 * float(profile.get("pan_bias", 0.0) or 0.0))
            tilt_span *= 1.0 + (0.16 * float(profile.get("tilt_bias", 0.0) or 0.0))

        heading_pan, heading_tilt = self._active_target_heading_norm(max(0.10, pursuit_window))
        pan_dir = 1.0 if heading_pan >= 0.0 else -1.0
        tilt_dir = 1.0 if heading_tilt >= 0.0 else -1.0
        if abs(heading_pan) < 0.08:
            pan_dir = 1.0 if float(profile.get("pan_bias", 0.0) or 0.0) >= 0.0 else -1.0
        if abs(heading_tilt) < 0.08:
            tilt_dir = 1.0 if float(profile.get("tilt_bias", 0.0) or 0.0) >= 0.0 else -1.0

        style = self._loss_search_style()
        if style == "fast_reacquire":
            near_pan = max(0.45, pan_span * 0.52)
            near_tilt = max(0.30, tilt_span * 0.56)
            mid_pan = max(near_pan + 0.35, pan_span * 0.82)
            mid_tilt = max(near_tilt + 0.25, tilt_span * 0.78)
        else:
            near_pan = max(0.35, pan_span * 0.28)
            near_tilt = max(0.22, tilt_span * 0.32)
            mid_pan = max(near_pan + 0.30, pan_span * 0.56)
            mid_tilt = max(near_tilt + 0.20, tilt_span * 0.58)

        points: List[Tuple[float, float]] = []
        seen: set[Tuple[float, float]] = set()

        def _append_point(pan: float, tilt: float) -> None:
            point = (self._clamp_pan(pan), self._clamp_tilt(tilt))
            if point in seen:
                return
            seen.add(point)
            points.append(point)

        _append_point(center_pan, center_tilt)

        local_pattern = [
            (pan_dir * near_pan, 0.0),
            (pan_dir * near_pan * 0.70, tilt_dir * near_tilt),
            (pan_dir * near_pan * 0.70, -tilt_dir * near_tilt),
            (0.0, tilt_dir * near_tilt),
            (0.0, -tilt_dir * near_tilt),
            (-pan_dir * near_pan * 0.45, 0.0),
            (pan_dir * mid_pan, 0.0),
            (pan_dir * mid_pan * 0.72, tilt_dir * mid_tilt),
            (pan_dir * mid_pan * 0.72, -tilt_dir * mid_tilt),
            (0.0, tilt_dir * mid_tilt),
            (0.0, -tilt_dir * mid_tilt),
            (pan_span, 0.0),
            (-pan_span, 0.0),
            (0.0, tilt_span),
            (0.0, -tilt_span),
            (pan_span * 0.65, tilt_span * 0.65),
            (-pan_span * 0.65, tilt_span * 0.65),
            (pan_span * 0.65, -tilt_span * 0.65),
            (-pan_span * 0.65, -tilt_span * 0.65),
        ]
        if style != "fast_reacquire":
            local_pattern[11:11] = [
                (-pan_dir * near_pan * 0.55, tilt_dir * near_tilt * 0.90),
                (-pan_dir * near_pan * 0.55, -tilt_dir * near_tilt * 0.90),
            ]

        for pan_offset, tilt_offset in local_pattern:
            _append_point(center_pan + pan_offset, center_tilt + tilt_offset)
        return self._apply_loss_search_rounds(points, center_pan, center_tilt)

    def _loss_recovery_expanding_search_points(self, pursuit_window: float) -> List[Tuple[float, float]]:
        if not bool(getattr(self.cfg.engagement, "loss_expanding_search_enabled", True)):
            return []
        center_pan, center_tilt = self._loss_recovery_search_origin(pursuit_window)
        base_pan = max(0.6, float(getattr(self.cfg.engagement, "loss_local_search_pan_deg", 3.5) or 3.5))
        base_tilt = max(0.4, float(getattr(self.cfg.engagement, "loss_local_search_tilt_deg", 2.0) or 2.0))
        pan_step = max(0.5, float(getattr(self.cfg.engagement, "loss_expanding_search_pan_step_deg", 3.0) or 3.0))
        tilt_step = max(0.3, float(getattr(self.cfg.engagement, "loss_expanding_search_tilt_step_deg", 1.5) or 1.5))
        ring_count = max(0, int(getattr(self.cfg.engagement, "loss_expanding_search_rings", 2) or 0))
        points: List[Tuple[float, float]] = []
        for ring_idx in range(1, ring_count + 1):
            pan_span = base_pan + (pan_step * ring_idx)
            tilt_span = base_tilt + (tilt_step * ring_idx)
            if self._adaptive_loss_recovery_enabled():
                pan_span *= max(1.0, float(getattr(self.cfg.engagement, "loss_persistent_expand_scale", 1.18) or 1.18))
                tilt_span *= 1.0 + ((max(1.0, float(getattr(self.cfg.engagement, "loss_persistent_expand_scale", 1.18) or 1.18)) - 1.0) * 0.65)
            points.extend([
                (center_pan + pan_span, center_tilt),
                (center_pan - pan_span, center_tilt),
                (center_pan, center_tilt + tilt_span),
                (center_pan, center_tilt - tilt_span),
                (center_pan + pan_span, center_tilt + tilt_span),
                (center_pan - pan_span, center_tilt + tilt_span),
                (center_pan + pan_span, center_tilt - tilt_span),
                (center_pan - pan_span, center_tilt - tilt_span),
            ])
        return self._apply_loss_search_rounds(points, center_pan, center_tilt)

    def _rapid_handoff_search_points(self, pursuit_window: float) -> List[Tuple[float, float]]:
        center_pan, center_tilt = self._loss_recovery_search_origin(pursuit_window)
        profile = self._loss_recovery_personality_profile()
        heading_pan, heading_tilt = self._active_target_heading_norm(0.10)
        if abs(heading_pan) < 0.08:
            heading_pan = 1.0 if float(profile.get("pan_bias", 0.0) or 0.0) >= 0.0 else -1.0
        if abs(heading_tilt) < 0.08:
            heading_tilt = 1.0 if float(profile.get("tilt_bias", 0.0) or 0.0) >= 0.0 else -1.0
        backoff_pan = max(0.4, float(getattr(self.cfg.engagement, "loss_handoff_backoff_pan_deg", 1.4) or 1.4))
        tilt_step = max(0.2, float(getattr(self.cfg.engagement, "loss_handoff_tilt_step_deg", 0.9) or 0.9))
        return self._apply_loss_search_rounds([
            (center_pan - (backoff_pan * heading_pan), center_tilt),
            (center_pan - (backoff_pan * 0.45 * heading_pan), center_tilt + (tilt_step * max(0.5, heading_tilt))),
            (center_pan - (backoff_pan * 0.35 * heading_pan), center_tilt - (tilt_step * max(0.5, heading_tilt))),
            (center_pan, center_tilt),
        ], center_pan, center_tilt)

    def _persistent_loss_recovery_points(self, pursuit_window: float) -> List[Tuple[float, float]]:
        local_points = self._loss_recovery_local_search_points(pursuit_window)
        expanding_points = self._loss_recovery_expanding_search_points(pursuit_window)
        base_points: List[Tuple[float, float]] = []
        base_points.extend(local_points)
        base_points.extend(expanding_points)
        if not base_points:
            return []
        visible_count = int(self._loss_recovery_context.get("visible_target_count", 0) or 0)
        crowd_threshold = max(1, int(getattr(self.cfg.engagement, "loss_scene_crowding_threshold", 3) or 3))
        pass_count = int(getattr(self.cfg.engagement, "loss_persistent_retry_passes_sparse", 2) or 2)
        if visible_count >= crowd_threshold:
            pass_count = int(getattr(self.cfg.engagement, "loss_persistent_retry_passes_crowded", 1) or 1)
        pass_count = max(1, pass_count)
        center_pan, center_tilt = self._loss_recovery_search_origin(pursuit_window)
        points: List[Tuple[float, float]] = []
        for pass_index in range(pass_count):
            scale = 1.0 + (0.10 * pass_index)
            for point_pan, point_tilt in base_points:
                points.append((
                    center_pan + ((point_pan - center_pan) * scale),
                    center_tilt + ((point_tilt - center_tilt) * scale),
                ))
        return points

    def _move_loss_recovery_target(self, pan: float, tilt: float, now: float) -> None:
        target_pan = self._clamp_pan(pan)
        target_tilt = self._clamp_tilt(tilt)
        if abs(target_pan - self.current_pan) < 0.05 and abs(target_tilt - self.current_tilt) < 0.05:
            return
        phase = str(self._loss_recovery_phase or "")
        if "expand" in phase or self._loss_recovery_retry_count > 0:
            # Keep a little variation only on wider recovery passes; tight first
            # pursuit/local reacquire steps should stay literal.
            jitter_seed = int(self._loss_recovery_search_index * 97 + int(now * 100) % 137)
            jitter_rng = random.Random(jitter_seed)
            target_pan = self._clamp_pan(target_pan + jitter_rng.gauss(0.0, 0.14))
            target_tilt = self._clamp_tilt(target_tilt + jitter_rng.gauss(0.0, 0.09))
        self._loss_recovery_last_move_time = now
        self._move_turret(target_pan, target_tilt)

    def _clamp_pan(self, pan: float) -> float:
        return float(max(self.cfg.guard.pan_min, min(self.cfg.guard.pan_max, pan)))

    def _clamp_tilt(self, tilt: float) -> float:
        return float(max(self.cfg.guard.tilt_min, min(self.cfg.guard.tilt_max, tilt)))

    def _update_error_rates(self, err_pan: float, err_tilt: float, now: float) -> None:
        if self._last_error_sample_time > 0.0:
            dt = max(0.001, now - self._last_error_sample_time)
            self._err_pan_rate_deg_s = abs((float(err_pan) - self._last_err_pan_deg) / dt)
            self._err_tilt_rate_deg_s = abs((float(err_tilt) - self._last_err_tilt_deg) / dt)
        else:
            self._err_pan_rate_deg_s = 0.0
            self._err_tilt_rate_deg_s = 0.0
        self._last_error_sample_time = now

    def _trigger_should_fire(
        self,
        target: TrackedTarget,
        lock_pan: float,
        lock_tilt: float,
        now: float,
    ) -> bool:
        """
        Simplified fire gate: check only essential conditions.
        
        Gate conditions (all must be true to fire):
          1. Not in refractory period
          2. No fire mask blocking current aim
          3. Target is centered within firing tolerance
          4. Target has minimum confidence and persistence
          5. Hold time requirement met
        """
        eng = self.cfg.engagement
        stage_trace: List[Dict[str, Any]] = []

        def _push_stage(name: str, inputs: Dict[str, Any], threshold: Dict[str, Any], passed: bool, reason: str) -> None:
            stage_trace.append(
                {
                    "stage": str(name),
                    "inputs": dict(inputs),
                    "threshold": dict(threshold),
                    "pass": bool(passed),
                    "reason": str(reason),
                }
            )
        
        # Refractory check: prevent rapid re-firing
        if now < self._trigger_refractory_until:
            self._trigger_hold_start = 0.0
            self._trigger_gate_active = False
            _push_stage(
                "refractory_period",
                {"now": float(now)},
                {"refractory_until": float(self._trigger_refractory_until)},
                False,
                "refractory period",
            )
            self._last_fire_gate_trace = {
                "approved": False,
                "reason": "refractory_period",
                "stages": stage_trace,
            }
            return False
        _push_stage(
            "refractory_period",
            {"now": float(now)},
            {"refractory_until": float(self._trigger_refractory_until)},
            True,
            "refractory period satisfied",
        )

        # No-fire mask check: safety-critical
        if self._current_no_fire_mask() is not None:
            self._trigger_hold_start = 0.0
            self._trigger_gate_active = False
            _push_stage(
                "no_fire_mask",
                {"active_mask": str(self._last_no_fire_mask_name or "")},
                {"requires_clear_mask": True},
                False,
                "mask block",
            )
            self._last_fire_gate_trace = {
                "approved": False,
                "reason": "no_fire_mask_block",
                "stages": stage_trace,
            }
            return False
        _push_stage(
            "no_fire_mask",
            {"active_mask": ""},
            {"requires_clear_mask": True},
            True,
            "mask clear",
        )

        if not self._target_meets_fire_requirements(target, now=now):
            self._trigger_hold_start = 0.0
            self._trigger_gate_active = False
            return False
        stage_trace.extend(list((self._last_fire_gate_trace or {}).get("stages", []) or []))

        if not self._person_target_is_fire_authorized(target, now):
            self._trigger_hold_start = 0.0
            self._trigger_gate_active = False
            _push_stage(
                "person_fire_authorization",
                {
                    "class_name": str(getattr(target.det, "class_name", "") or ""),
                    "fire_veto_reason": str(self._last_fire_veto_reason or ""),
                },
                {"authorization_required": True},
                False,
                "safety lock",
            )
            self._last_fire_gate_trace = {
                "approved": False,
                "reason": "person_fire_authorization_failed",
                "stages": stage_trace,
            }
            return False
        _push_stage(
            "person_fire_authorization",
            {
                "class_name": str(getattr(target.det, "class_name", "") or ""),
                "fire_veto_reason": str(self._last_fire_veto_reason or ""),
            },
            {"authorization_required": True},
            True,
            "authorization accepted",
        )

        policy_state = self._motion_policy_state.get(int(getattr(target.det, "track_id", -1) or -1), {})
        policy_mode = self._motion_policy_mode()
        policy_lifecycle = str(policy_state.get("state", "TRACKING") or "TRACKING")
        policy_motion_allowed = bool(policy_state.get("motion_allowed", True))
        if policy_mode != "allow_stationary" and not policy_motion_allowed:
            self._trigger_hold_start = 0.0
            self._trigger_gate_active = False
            self._set_fire_veto_reason(
                str(policy_state.get("suppression_reason", "motion policy suppressed") or "motion policy suppressed"),
                now,
            )
            _push_stage(
                "motion_policy",
                {
                    "state": policy_lifecycle,
                    "suppression_reason": str(policy_state.get("suppression_reason", "") or ""),
                    "recent_motion_distance_px": float(policy_state.get("recent_motion_distance_px", 0.0) or 0.0),
                    "average_velocity_px_s": float(policy_state.get("average_velocity_px_s", 0.0) or 0.0),
                    "motion_confidence": float(policy_state.get("motion_confidence", 0.0) or 0.0),
                    "stationary_duration_s": float(policy_state.get("stationary_duration_s", 0.0) or 0.0),
                },
                {
                    "motion_policy_mode": policy_mode,
                    "motion_stationary_timeout_s": float(getattr(self.cfg.engagement, "motion_stationary_timeout_s", 4.0) or 4.0),
                },
                False,
                "motion policy rejected target",
            )
            self._last_fire_gate_trace = {
                "approved": False,
                "reason": "motion_policy_block",
                "stages": stage_trace,
            }
            return False
        _push_stage(
            "motion_policy",
            {
                "state": policy_lifecycle,
                "suppression_reason": str(policy_state.get("suppression_reason", "") or ""),
                "recent_motion_distance_px": float(policy_state.get("recent_motion_distance_px", 0.0) or 0.0),
                "average_velocity_px_s": float(policy_state.get("average_velocity_px_s", 0.0) or 0.0),
                "motion_confidence": float(policy_state.get("motion_confidence", 0.0) or 0.0),
                "stationary_duration_s": float(policy_state.get("stationary_duration_s", 0.0) or 0.0),
            },
            {
                "motion_policy_mode": policy_mode,
                "motion_stationary_timeout_s": float(getattr(self.cfg.engagement, "motion_stationary_timeout_s", 4.0) or 4.0),
            },
            True,
            "motion policy accepted",
        )

        # Centering check: use hysteresis (wider exit than enter)
        enter_pan = float(eng.fire_trigger_enter_pan_tolerance)
        enter_tilt = float(eng.fire_trigger_enter_tilt_tolerance)
        exit_pan = max(enter_pan, float(eng.fire_trigger_exit_pan_tolerance))
        exit_tilt = max(enter_tilt, float(eng.fire_trigger_exit_tilt_tolerance))
        gate_pan = exit_pan if self._trigger_gate_active else enter_pan
        gate_tilt = exit_tilt if self._trigger_gate_active else enter_tilt

        centered = abs(lock_pan) <= gate_pan and abs(lock_tilt) <= gate_tilt
        _push_stage(
            "centering",
            {
                "lock_pan": float(lock_pan),
                "lock_tilt": float(lock_tilt),
                "gate_pan": float(gate_pan),
                "gate_tilt": float(gate_tilt),
            },
            {
                "enter_pan": float(enter_pan),
                "enter_tilt": float(enter_tilt),
                "exit_pan": float(exit_pan),
                "exit_tilt": float(exit_tilt),
            },
            bool(centered),
            "target centered" if centered else "target not centered",
        )
        
        # Target quality check: simplified - only confidence and persistence
        trustworthy = (
            float(target.det.confidence) >= float(eng.fire_trigger_min_confidence)
            and float(target.persistence) >= float(eng.fire_trigger_min_persistence)
        )
        _push_stage(
            "target_quality",
            {
                "confidence": float(target.det.confidence),
                "persistence": float(target.persistence),
            },
            {
                "min_confidence": float(eng.fire_trigger_min_confidence),
                "min_persistence": float(eng.fire_trigger_min_persistence),
            },
            bool(trustworthy),
            "quality accepted" if trustworthy else "confidence below threshold",
        )

        if not (centered and trustworthy):
            self._trigger_hold_start = 0.0
            self._trigger_gate_active = False
            self._last_fire_gate_trace = {
                "approved": False,
                "reason": "target_not_centered" if not centered else "target_quality_below_threshold",
                "stages": stage_trace,
            }
            return False

        # Hold time accumulation
        if self._trigger_hold_start <= 0.0:
            self._trigger_hold_start = now
            self._trigger_gate_active = True
            _push_stage(
                "hold_time",
                {
                    "hold_start": float(self._trigger_hold_start),
                    "hold_elapsed": 0.0,
                },
                {"required_hold_time_s": float(eng.fire_trigger_hold_time)},
                False,
                "hold-time requirement not satisfied",
            )
            self._last_fire_gate_trace = {
                "approved": False,
                "reason": "hold_time_not_met",
                "stages": stage_trace,
            }
            return False

        self._trigger_gate_active = True
        hold_elapsed = now - self._trigger_hold_start
        hold_pass = hold_elapsed >= float(eng.fire_trigger_hold_time)
        _push_stage(
            "hold_time",
            {
                "hold_start": float(self._trigger_hold_start),
                "hold_elapsed": float(hold_elapsed),
            },
            {"required_hold_time_s": float(eng.fire_trigger_hold_time)},
            bool(hold_pass),
            "hold-time requirement satisfied" if hold_pass else "hold-time requirement not satisfied",
        )
        self._last_fire_gate_trace = {
            "approved": bool(hold_pass),
            "reason": "approved" if hold_pass else "hold_time_not_met",
            "stages": stage_trace,
        }
        return hold_pass

    def _compute_visual_servo_correction(
        self,
        err_pan: float,
        err_tilt: float,
        *,
        use_fire_limits: bool,
    ) -> Tuple[float, float, float, float]:
        eng = self.cfg.engagement
        alpha = max(0.0, min(1.0, float(eng.precision_error_ema)))
        # Seed the EMA with the first real error so the filter doesn't
        # start cold from 0 and under-correct on the opening frames.
        first_frame = (self._smoothed_err_pan == 0.0 and self._smoothed_err_tilt == 0.0
                       and (abs(err_pan) > 0.01 or abs(err_tilt) > 0.01))
        if alpha <= 0.0 or first_frame:
            self._smoothed_err_pan = err_pan
            self._smoothed_err_tilt = err_tilt
        else:
            self._smoothed_err_pan = (alpha * err_pan) + ((1.0 - alpha) * self._smoothed_err_pan)
            self._smoothed_err_tilt = (alpha * err_tilt) + ((1.0 - alpha) * self._smoothed_err_tilt)

        lock_pan = self._smoothed_err_pan
        lock_tilt = self._smoothed_err_tilt

        deadzone_pan = float(eng.precision_deadzone_pan_deg)
        deadzone_tilt = float(eng.precision_deadzone_tilt_deg)
        if use_fire_limits:
            # Keep fire-phase tracking alive: use a tighter deadzone while
            # micro-adjusting so moving targets are actively recentered.
            deadzone_pan = min(deadzone_pan, 0.18)
            deadzone_tilt = min(deadzone_tilt, 0.16)
        ctrl_pan = 0.0 if abs(lock_pan) <= deadzone_pan else lock_pan
        ctrl_tilt = 0.0 if abs(lock_tilt) <= deadzone_tilt else lock_tilt

        if ctrl_pan != 0.0 and ctrl_pan * self._pid_prev_err_pan < 0.0:
            self._pid_integral_pan *= float(eng.precision_reversal_brake)
        if ctrl_tilt != 0.0 and ctrl_tilt * self._pid_prev_err_tilt < 0.0:
            self._pid_integral_tilt *= float(eng.precision_reversal_brake)

        if not use_fire_limits and eng.precision_ki != 0.0:
            self._pid_integral_pan += ctrl_pan
            self._pid_integral_tilt += ctrl_tilt
            integral_limit = max(6.0, float(eng.precision_max_step) * 8.0)
            self._pid_integral_pan = max(-integral_limit, min(integral_limit, self._pid_integral_pan))
            self._pid_integral_tilt = max(-integral_limit, min(integral_limit, self._pid_integral_tilt))

        # Seed prev_err on the first frame so D-term starts at zero rather than
        # firing at full error magnitude (kd * full_err amplifies the first step).
        if first_frame:
            self._pid_prev_err_pan = ctrl_pan
            self._pid_prev_err_tilt = ctrl_tilt

        d_pan = ctrl_pan - self._pid_prev_err_pan
        d_tilt = ctrl_tilt - self._pid_prev_err_tilt
        self._pid_prev_err_pan = ctrl_pan
        self._pid_prev_err_tilt = ctrl_tilt

        corr_pan = eng.precision_kp * ctrl_pan + eng.precision_ki * self._pid_integral_pan + eng.precision_kd * d_pan
        corr_tilt = eng.precision_kp * ctrl_tilt + eng.precision_ki * self._pid_integral_tilt + eng.precision_kd * d_tilt

        response_scale = self._engagement_response_scale(use_fire_limits=use_fire_limits)
        response_scale *= self._inflight_correction_scale(use_fire_limits=use_fire_limits)
        corr_pan *= response_scale
        corr_tilt *= response_scale

        # Cache PID components for logging
        self._last_pid_p_pan = float(eng.precision_kp) * ctrl_pan
        self._last_pid_i_pan = float(eng.precision_ki) * self._pid_integral_pan
        self._last_pid_d_pan = float(eng.precision_kd) * d_pan
        self._last_pid_p_tilt = float(eng.precision_kp) * ctrl_tilt
        self._last_pid_i_tilt = float(eng.precision_ki) * self._pid_integral_tilt
        self._last_pid_d_tilt = float(eng.precision_kd) * d_tilt

        if use_fire_limits:
            fire_window_pan = max(0.8, float(getattr(eng, "fire_recenter_pan_tolerance", 0.0) or 0.0))
            fire_window_tilt = max(0.8, float(getattr(eng, "fire_recenter_tilt_tolerance", 0.0) or 0.0))
            fire_pan_limit = float(eng.fire_micro_adjust_max_pan_step)
            fire_tilt_limit = float(eng.fire_micro_adjust_max_tilt_step)
            precision_pan_limit = float(eng.precision_max_pan_step) if float(eng.precision_max_pan_step) > 0.0 else float(eng.precision_max_step)
            precision_tilt_limit = float(eng.precision_max_tilt_step) if float(eng.precision_max_tilt_step) > 0.0 else float(eng.precision_max_step)
            # Keep fire-phase micro-adjust conservative. The widened v4 limits
            # let noisy vertical error walk the turret away from the target.
            pan_limit = max(
                fire_pan_limit,
                min(precision_pan_limit * 0.55, fire_pan_limit + ((abs(lock_pan) / fire_window_pan) * 0.22)),
            )
            tilt_limit = max(
                fire_tilt_limit,
                min(precision_tilt_limit * 0.55, fire_tilt_limit + ((abs(lock_tilt) / fire_window_tilt) * 0.18)),
            )
        else:
            pan_limit = float(eng.precision_max_pan_step) if float(eng.precision_max_pan_step) > 0.0 else float(eng.precision_max_step)
            tilt_limit = float(eng.precision_max_tilt_step) if float(eng.precision_max_tilt_step) > 0.0 else float(eng.precision_max_step)

        corr_pan = max(-pan_limit, min(pan_limit, corr_pan))
        corr_tilt = max(-tilt_limit, min(tilt_limit, corr_tilt))

        return corr_pan, corr_tilt, lock_pan, lock_tilt

    def _should_return_to_precision(self, err_pan: float, err_tilt: float) -> bool:
        if not self._has_recent_measured_pose(max_age_s=self._engagement_pose_freshness_s(for_fire=True)):
            return True
        eng = self.cfg.engagement
        # Keep moving targets centered: while in fire phase, if target error drifts
        # beyond a tighter threshold, switch back to precision immediately.
        fire_center_tol = max(0.0, float(getattr(eng, "fire_center_tolerance_deg", 3.5)))
        dynamic_pan_tol = max(0.8, fire_center_tol * 0.4)
        dynamic_tilt_tol = max(0.8, fire_center_tol * 0.4)
        recenter_pan_tol = min(float(eng.fire_recenter_pan_tolerance), dynamic_pan_tol)
        recenter_tilt_tol = min(float(eng.fire_recenter_tilt_tolerance), dynamic_tilt_tol)
        return (
            abs(err_pan) > recenter_pan_tol
            or abs(err_tilt) > recenter_tilt_tol
        )

    # ------------------------------------------------------------------ #
    # RETURNING state
    # ------------------------------------------------------------------ #

    def _update_returning(self, now: float) -> None:
        """Wait briefly, then return to guard/patrol position."""
        if now - self._return_start >= self.cfg.engagement.return_delay:
            mode = self.cfg.guard.guard_mode
            if mode == 0:
                # Static guard — move back to guard point
                gp, gt = self._planner.get_return_position()
                self._move_turret(gp, gt)
            # Patrol modes intentionally do not force a home nudge here;
            # they should resume patrol naturally from current pose.
            self._queue.clear()
            self.last_queue = []
            self._queue_index = 0
            self.active_order = None
            self._last_engage_time = now
            self._patrol_initialized = False  # patrol will re-init on next tick
            self._change_state(SentryV2State.GUARDING)

    # ------------------------------------------------------------------ #
    # Patrol logic (guard modes 1-3)
    # ------------------------------------------------------------------ #

    def _update_patrol(self, now: float) -> None:
        """Drive turret movement for non-static guard modes."""
        mode = self.cfg.guard.guard_mode
        if mode == 0:
            return  # static — nothing to do

        dt = now - self._patrol_last_update if self._patrol_last_update > 0 else 0.0
        self._patrol_last_update = now
        # Clamp dt to avoid jumps after pauses (engagement, tab switch, etc.)
        dt = min(dt, 0.15)

        if not self._patrol_initialized:
            self._patrol_init(mode, now)
            self._patrol_initialized = True
            return

        if mode == 1:
            self._patrol_sweep(dt, now)
        elif mode == 2:
            self._patrol_waypoint(dt, now)
        elif mode == 3:
            self._patrol_random(dt, now)

    def _patrol_init(self, mode: int, now: float) -> None:
        """Initialize patrol state for the given mode."""
        g = self.cfg.guard
        if mode == 1:  # Sweep
            self._patrol_target_pan = g.sweep_pan_min
            self._patrol_target_tilt = g.sweep_tilt
            self._patrol_sweep_dir = 1
        elif mode == 2:  # Waypoint
            wps = g.patrol_waypoints
            if wps:
                self._patrol_wp_index = 0
                self._patrol_target_pan = wps[0][0]
                self._patrol_target_tilt = wps[0][1]
            else:
                self._patrol_target_pan = g.guard_pan
                self._patrol_target_tilt = g.guard_tilt
            self._patrol_dwelling = False
        elif mode == 3:  # Random
            self._patrol_pick_random_target()
            self._patrol_dwelling = False
        self._patrol_dwell_start = now

    def _patrol_sweep(self, dt: float, now: float) -> None:
        """Slow continuous pan sweep at fixed tilt."""
        g = self.cfg.guard
        speed = g.sweep_speed  # deg/sec
        step = speed * dt

        new_pan = self.current_pan + step * self._patrol_sweep_dir

        # Reverse at boundaries
        if new_pan >= g.sweep_pan_max:
            new_pan = g.sweep_pan_max
            self._patrol_sweep_dir = -1
        elif new_pan <= g.sweep_pan_min:
            new_pan = g.sweep_pan_min
            self._patrol_sweep_dir = 1

        self._move_turret(new_pan, g.sweep_tilt)

    def _patrol_waypoint(self, dt: float, now: float) -> None:
        """Move between waypoints with dwell pauses."""
        g = self.cfg.guard
        wps = g.patrol_waypoints
        if not wps:
            return

        if self._patrol_dwelling:
            if now - self._patrol_dwell_start >= g.patrol_dwell:
                # Advance to next waypoint
                self._patrol_wp_index = (self._patrol_wp_index + 1) % len(wps)
                wp = wps[self._patrol_wp_index]
                self._patrol_target_pan = wp[0]
                self._patrol_target_tilt = wp[1]
                self._patrol_dwelling = False
            return

        # Interpolate toward current waypoint target
        arrived = self._patrol_move_toward(
            self._patrol_target_pan, self._patrol_target_tilt,
            g.patrol_speed, dt
        )
        if arrived:
            self._patrol_dwelling = True
            self._patrol_dwell_start = now

    def _patrol_random(self, dt: float, now: float) -> None:
        """Move to random positions with dwell pauses."""
        g = self.cfg.guard

        if self._patrol_dwelling:
            if now - self._patrol_dwell_start >= g.random_dwell:
                self._patrol_pick_random_target()
                self._patrol_dwelling = False
            return

        arrived = self._patrol_move_toward(
            self._patrol_target_pan, self._patrol_target_tilt,
            g.random_speed, dt
        )
        if arrived:
            self._patrol_dwelling = True
            self._patrol_dwell_start = now

    def _patrol_pick_random_target(self) -> None:
        g = self.cfg.guard
        self._patrol_target_pan = random.uniform(g.random_pan_min, g.random_pan_max)
        self._patrol_target_tilt = random.uniform(g.random_tilt_min, g.random_tilt_max)

    def _patrol_move_toward(
        self, target_pan: float, target_tilt: float,
        speed: float, dt: float,
    ) -> bool:
        """
        Smoothly interpolate current position toward target at *speed* deg/sec.
        Returns True when within 0.3° of the target (arrived).
        """
        target_pan, target_tilt = self._clamp_angles(target_pan, target_tilt)
        dp = target_pan - self.current_pan
        dtilt = target_tilt - self.current_tilt
        dist = (dp ** 2 + dtilt ** 2) ** 0.5

        if dist < 0.3:
            self._move_turret(target_pan, target_tilt)
            return True

        max_step = speed * dt
        if max_step >= dist:
            self._move_turret(target_pan, target_tilt)
            return True

        # Unit vector × step
        ratio = max_step / dist
        new_pan = self.current_pan + dp * ratio
        new_tilt = self.current_tilt + dtilt * ratio
        self._move_turret(new_pan, new_tilt)
        return False

    # ------------------------------------------------------------------ #
    # Turret helpers
    # ------------------------------------------------------------------ #

    def _has_recent_measured_pose(self, now: Optional[float] = None, *, max_age_s: float = 1.2) -> bool:
        measured_at = float(getattr(self, "_last_measured_pose_time", 0.0) or 0.0)
        if measured_at <= 0.0:
            return False
        sample_now = time.time() if now is None else float(now)
        return (sample_now - measured_at) <= max(0.01, float(max_age_s))

    def update_runtime_pose(
        self,
        pan: float,
        tilt: float,
        *,
        measured: bool = True,
        timestamp: Optional[float] = None,
    ) -> None:
        pan, tilt = self._clamp_angles(pan, tilt)
        self.current_pan = pan
        self.current_tilt = tilt
        if measured:
            self._last_measured_pose_time = time.time() if timestamp is None else float(timestamp)

    def note_commanded_move(
        self,
        pan: float,
        tilt: float,
        *,
        move_time_s: float = 0.0,
        timestamp: Optional[float] = None,
    ) -> None:
        pan, tilt = self._clamp_angles(pan, tilt)
        self._last_commanded_pan = pan
        self._last_commanded_tilt = tilt
        self._last_command_time = time.time() if timestamp is None else float(timestamp)
        self._last_command_move_time_s = max(0.0, float(move_time_s or 0.0))

    def _command_settle_window_s(self, min_settle_s: float) -> float:
        move_time_s = max(0.0, float(getattr(self, "_last_command_move_time_s", 0.0) or 0.0))
        settle_from_move_s = max(0.09, min(0.42, (move_time_s * 0.82) + 0.03))
        return max(float(min_settle_s), settle_from_move_s)

    def _acquire_phase_ready(self, now: float, min_settle_s: float) -> bool:
        command_started_at = float(self._last_command_time or self._phase_start or now)
        command_age_s = max(0.0, now - command_started_at)
        settle_s = self._command_settle_window_s(min_settle_s)
        if command_age_s < settle_s:
            return False
        if not self._has_recent_measured_pose(now):
            return True
        remaining_pan = abs(float(self.current_pan) - float(self._last_commanded_pan))
        remaining_tilt = abs(float(self.current_tilt) - float(self._last_commanded_tilt))
        if max(remaining_pan, remaining_tilt) <= 1.25:
            return True
        hard_timeout_s = max(settle_s, min(0.58, float(self._last_command_move_time_s or 0.0) + 0.08))
        return command_age_s >= hard_timeout_s

    def _move_turret(self, pan: float, tilt: float) -> None:
        pan, tilt = self._clamp_angles(pan, tilt)
        if not self._motion_enabled:
            return
        # When fresh measured pose is available, keep it as the live control
        # reference and treat this as a commanded move only.
        if not self._has_recent_measured_pose():
            self.current_pan = pan
            self.current_tilt = tilt
        if self._cb_move:
            self._cb_move(pan, tilt)

    def _clamp_angles(self, pan: float, tilt: float) -> Tuple[float, float]:
        guard = self.cfg.guard
        pan_min, pan_max = sorted((guard.pan_min, guard.pan_max))
        tilt_min, tilt_max = sorted((guard.tilt_min, guard.tilt_max))
        return (
            max(pan_min, min(pan_max, pan)),
            max(tilt_min, min(tilt_max, tilt)),
        )

    # ------------------------------------------------------------------ #
    # State machine
    # ------------------------------------------------------------------ #

    def _change_state(self, new: SentryV2State) -> None:
        if new == self.state:
            return
        old = self.state
        self.state = new
        if self._cb_state:
            self._cb_state(old, new)
        self._publish_mission_event(
            "engine_state_transition",
            {
                "timestamp": float(time.time()),
                "frame_number": int(self._frame_number),
                "from_state": str(old.name),
                "to_state": str(new.name),
            },
        )

    # ------------------------------------------------------------------ #
    # External queries
    # ------------------------------------------------------------------ #

    def get_state_name(self) -> str:
        return self.state.name

    def get_engagement_stats(self) -> Dict:
        active_track_id = int(getattr(getattr(self, "active_order", None), "target", None).det.track_id) if getattr(self, "active_order", None) is not None else -1
        active_motion_policy = dict(self._motion_policy_state.get(active_track_id, {}) or {}) if active_track_id >= 0 else {}
        return {
            "state": self.state.name,
            "engage_phase": str(getattr(self, "_engage_phase", "")),
            "targets_detected": len(self.last_detections),
            "targets_visible": len(self.last_targets),
            "targets_qualified": len(self.last_qualified),
            "active_engagements": 1 if self.active_order is not None else 0,
            "queue_length": len(self._queue),
            "queue_position": self._queue_index,
            "engagements_total": len(self.engagement_log),
            "aim_lock_frames": self._aim_lock_frames,
            "last_err_pan_deg": round(self._last_err_pan_deg, 3),
            "last_err_tilt_deg": round(self._last_err_tilt_deg, 3),
            "reacquire_note": self._last_reacquire_note,
            "reacquire_recent": bool(self._last_reacquire_time and (time.time() - self._last_reacquire_time) <= 2.0),
            "pir_note": self._last_pir_note,
            "pir_recent": bool(self._last_pir_time and (time.time() - self._last_pir_time) <= 2.5),
            "pir_cue_mode": bool(self._pir_cue_mode),
            "pir_scan_mode": bool(self._pir_scan_mode),
            "pir_sensor_id": int(self._pir_cue_sensor_id),
            "pir_queue_length": int(self._pir_manager.peek_queue_count()),
            "pir_status": self._pir_manager.get_status_text(),
            "sound_alert_pending": bool(self._sound_alert_pending),
            "sound_alert_active": bool(self._sound_alert_active),
            "sound_alert_deferred_until_guard_clear": bool(self._sound_alert_deferred_until_guard_clear),
            "sound_alert_phase": str(self._sound_alert_phase),
            "sound_alert_note": str(self._sound_alert_note),
            "sound_alert_recent": bool(self._sound_alert_note_time and (time.time() - self._sound_alert_note_time) <= 3.0),
            "loss_recovery_phase": self._loss_recovery_phase,
            "no_fire_mask": self._last_no_fire_mask_name,
            "fire_veto_reason": self._last_fire_veto_reason,
            "fire_veto_recent": bool(self._last_fire_veto_time and (time.time() - self._last_fire_veto_time) <= 3.0),
            "motion_policy": {
                "mode": self._motion_policy_mode(),
                "active_track_id": active_track_id,
                "active_state": str(active_motion_policy.get("state", "") or ""),
                "suppression_reason": str(active_motion_policy.get("suppression_reason", "") or ""),
                "suppression_expiry": float(active_motion_policy.get("suppression_expiry", 0.0) or 0.0),
                "next_eligible_evaluation_time": float(active_motion_policy.get("next_eligible_evaluation_time", 0.0) or 0.0),
                "recent_motion_distance_px": float(active_motion_policy.get("recent_motion_distance_px", 0.0) or 0.0),
                "average_velocity_px_s": float(active_motion_policy.get("average_velocity_px_s", 0.0) or 0.0),
                "motion_confidence": float(active_motion_policy.get("motion_confidence", 0.0) or 0.0),
                "stationary_duration_s": float(active_motion_policy.get("stationary_duration_s", 0.0) or 0.0),
                "history": list(active_motion_policy.get("history", []) or []),
            },
            "engagement_telemetry_log": str(self._engagement_telemetry.log_path),
            "engagement_telemetry_run_id": str(self._engagement_telemetry.run_id),
            "frame_number": int(self._frame_number),
            "motion_enabled": bool(self._motion_enabled),
            "motion_policy_state_count": int(len(self._motion_policy_state)),
            "filter_rejections": [
                {
                    "track_id": int(decision.track_id),
                    "class_name": str(decision.class_name),
                    "source": str(decision.source),
                    "passed": bool(decision.passed),
                    "reason": str(decision.reason),
                    "detail": str(decision.detail),
                    "confirm_hits": int(decision.confirm_hits),
                    "confirm_required": int(decision.confirm_required),
                }
                for decision in self.last_filter_diagnostics[:12]
                if not decision.passed
            ],
        }

    # ------------------------------------------------------------------ #
    # ML Training (Optional)
    # ------------------------------------------------------------------ #

    def get_ml_logger(self) -> MLTrainingLogger:
        """Return the ML training logger for recording engagement data."""
        return self._ml_logger

    def save_ml_training_data(self) -> bool:
        """Persist the current ML training examples to disk."""
        return bool(self._ml_logger.save())

    def train_ml_model(self) -> bool:
        """
        Train a new ML model from logged engagement data.
        Returns True on success.
        """
        features, labels = self._ml_logger.get_training_data()
        if len(features) < 10:
            return False
        
        success = self._scorer.train_ml_model(features, labels)
        return success

    def save_ml_model(self, path: str) -> bool:
        """Save the trained ML model to a pickle file."""
        try:
            self._scorer.save_ml_model(path)
            return True
        except Exception:
            return False

    def set_ml_training_mode(self, enable: bool) -> None:
        """Enable/disable manual fire logging for ML training."""
        self._log_ml_training = bool(enable)

    def get_ml_logger_stats(self) -> Dict:
        """Get statistics about logged engagement data."""
        return self._ml_logger.summary_stats()

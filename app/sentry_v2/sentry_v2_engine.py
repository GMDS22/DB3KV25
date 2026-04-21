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
from enum import Enum, auto
from typing import Callable, Dict, List, Optional, Tuple

from .sentry_v2_config import SentryV2Config
from .sentry_v2_no_fire_masks import find_blocking_mask
from .target_filter import DetectedObject, FilterDecision, TargetFilter
from .threat_scorer import ThreatScorer, TrackedTarget
from .engagement_planner import EngagementPlanner, EngagementOrder
from .ml_training_logger import MLTrainingLogger
from .sentry_v2_pir_manager import SentryV2PIRManager
from .precision_tuning_logger import PrecisionTuningLogger
from .autotracking_logger import AutotrackingLogger


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

        # Turret state (tracked by main app, seeded from guard config)
        self.current_pan: float = config.guard.guard_pan
        self.current_tilt: float = config.guard.guard_tilt

        # Engagement queue
        self._queue: List[EngagementOrder] = []
        self._queue_index: int = 0
        self._engage_phase: str = "aim"   # "aim" → "precision" → "fire" → "cooldown"
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
        self._last_reacquire_note: str = ""
        self._last_reacquire_time: float = 0.0
        self._last_pir_note: str = ""
        self._last_pir_time: float = 0.0
        self._last_no_fire_mask_name: str = ""
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
        self._motion_enabled: bool = True

    # ------------------------------------------------------------------ #
    # Callback registration
    # ------------------------------------------------------------------ #

    def on_fire(self, cb: Callable[[int], None]) -> None:
        self._cb_fire = cb

    def on_move(self, cb: Callable[[float, float], None]) -> None:
        self._cb_move = cb

    def on_state_change(self, cb: Callable[[SentryV2State, SentryV2State], None]) -> None:
        self._cb_state = cb

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
        self._active_target_last_seen_time = 0.0
        self._active_target_last_aim_pan = self.current_pan
        self._active_target_last_aim_tilt = self.current_tilt
        self._active_target_last_class = ""
        self._active_target_last_source = ""
        self._last_err_pan_deg = 0.0
        self._last_err_tilt_deg = 0.0
        self._last_reacquire_note = ""
        self._last_reacquire_time = 0.0
        self._last_pir_note = ""
        self._last_pir_time = 0.0
        self._return_start = 0.0
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

        # Increment frame counter for logging
        if self._log_autotracking:
            self._autotrack_logger.increment_frame()

        if self.state == SentryV2State.PAUSED:
            return

        self._last_no_fire_mask_name = ""
        self.last_detections = list(detections)

        # 1. Filter
        qualified, diagnostics = self._filter.filter_with_diagnostics(detections, now)
        self.last_filter_diagnostics = diagnostics
        self.last_qualified = qualified

        # 2. Score
        scored = self._scorer.score(qualified, now)
        self.last_targets = scored

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

    # ------------------------------------------------------------------ #
    # PIR event interface (called by comm when sensor data arrives)
    # ------------------------------------------------------------------ #

    def on_pir_sensor_fired(self, sensor_id: int, timestamp: Optional[float] = None) -> None:
        """Called when a PIR sensor event is received from ESP32."""
        now = timestamp or time.time()

        # Ignore stale/pre-enable PIR hits. Queuing them while PAUSED causes the
        # first enable cycle to consume old events and lunge toward a sensor cue
        # that the operator did not request.
        if self.state == SentryV2State.PAUSED or not self.cfg.pir_guard.pir_enabled:
            return

        self._pir_manager.on_pir_event(sensor_id, now)

        # PIR is a blind-spot cueing input, not a higher-priority override than a
        # camera-confirmed active engagement. Queue the PIR event immediately, but
        # only convert it into motion outside live ENGAGING tracking.
        if self.state == SentryV2State.ENGAGING:
            return

        cue = self._pir_manager.get_next_cue(now)
        if cue is None:
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
        self._move_turret(self._pir_cue_pan, self._pir_cue_tilt)

    # ------------------------------------------------------------------ #
    # GUARDING state
    # ------------------------------------------------------------------ #

    def _update_guarding(self, targets: List[TrackedTarget], now: float) -> None:
        """
        In GUARDING: patrol or hold position, and watch for threats.
        If scoreable threats exist above threshold, plan engagement.
        Also handles PIR sensor cues for blind-spot detection.
        """
        # Check for threats first — engagement always takes priority
        if targets:
            if now - self._last_engage_time >= self.cfg.engagement.cycle_cooldown:
                queue = self._planner.plan(targets, self.current_pan, self.current_tilt)
                if queue:
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
        raw = self.last_detections
        if not raw:
            return False
        if now - self._behaviour_watchful_last_move < WATCHFUL_MOVE_INTERVAL:
            return True  # detections exist, suppress patrol even on cooldown
        # Pick the detection with the largest bbox area (most prominent mover)
        best = max(
            raw,
            key=lambda d: (d.bbox[2] * d.bbox[3]) if (d.bbox and len(d.bbox) >= 4) else 0.0,
        )
        target_pan, target_tilt = self._planner.aim_from_normalized_center(
            float(best.norm_cx), float(best.norm_cy),
            self.current_pan, self.current_tilt,
        )
        self._behaviour_watchful_last_move = now
        self._move_turret(target_pan, target_tilt)
        return True

    def _update_curious_glance(self, now: float) -> bool:
        """Curious Guard mode: brief periodic glance at non-qualifying movers.

        Returns True if a glance is currently active (caller should suppress patrol).
        """
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
                self._finish_pir_no_target()
        else:
            # No search enabled, finish this cue and fall back to guard/patrol.
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
            self._pir_scan_awaiting_settle = True
            self._pir_settle_start = now
        else:
            # Search complete with no target. Explicitly return home so a static
            # guard configuration cannot remain parked at the final hunt point.
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
            # Scale aim settle with engagement speed — fast presets skip delay
            speed_ratio = float(max(10, min(100, int(getattr(self.cfg.engagement, "engagement_speed", 80) or 80))) - 10) / 90.0
            aim_settle_time = max(0.06, 0.35 * (1.0 - speed_ratio * 0.75))
            if elapsed >= aim_settle_time:
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
                if (now - self._target_lost_since) >= self.cfg.engagement.target_loss_timeout:
                    if self._should_retry_loss_recovery():
                        self._restart_loss_recovery(now)
                        return
                    self._advance_queue(now)
                return
            self._target_lost_since = 0.0
            self._reset_loss_recovery_state()

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
            if (
                self.cfg.engagement.auto_trigger_enabled
                and (settle_met or early_lock)
                and self._ready_to_fire()
                and target is not None
                and self._trigger_should_fire(target, lock_pan, lock_tilt, now)
            ):
                self._begin_fire(order, now)
                return

            # =================================================================================
            # BACKUP AUTO-TRIGGER LOGIC - DO NOT DISABLE WITHOUT USER APPROVAL  
            # Fallback firing mechanism for timeout scenarios
            # =================================================================================
            if (
                self.cfg.engagement.auto_trigger_enabled
                and now >= self._trigger_refractory_until
                and elapsed >= float(self.cfg.engagement.aim_lock_timeout)
                and target is not None
                and self._ready_to_fire()
                and self._target_meets_fire_requirements(target)
                and self._has_aim_lock(lock_pan, lock_tilt)
                and self._current_no_fire_mask() is None
            ):
                self._begin_fire(order, now)
                return

            if corr_pan != 0.0 or corr_tilt != 0.0:
                self._move_turret(self.current_pan + corr_pan, self.current_tilt + corr_tilt)

        elif self._engage_phase == "fire":
            tracked_target = self._find_active_target(order)
            tracked_det = tracked_target.det if tracked_target is not None else None
            if tracked_det is not None:
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
        for target in self.last_targets:
            if target.det.track_id == order.target.det.track_id:
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
                self._last_reacquire_time = time.time()
            return reacquired
        return None

    def _find_reacquire_target(self, order: EngagementOrder) -> Optional[TrackedTarget]:
        if not self.last_targets:
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

        for target in self.last_targets:
            det = target.det
            target_class = str(det.class_name or "").strip().lower()
            target_source = str(det.source or "").strip().lower()
            if anchor_source and target_source and target_source != anchor_source:
                continue
            if target.threat_score < (self.cfg.engagement.min_threat_score * 0.70):
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
                - (target.threat_score * 0.20)
            )
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
            self._active_target_last_class = str(target.det.class_name or "").strip().lower()
            self._active_target_last_source = str(target.det.source or "").strip().lower()
        else:
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

    def _target_meets_fire_requirements(self, target: TrackedTarget) -> bool:
        eng = self.cfg.engagement
        return (
            float(target.det.confidence) >= float(eng.fire_trigger_min_confidence)
            and float(target.persistence) >= float(eng.fire_trigger_min_persistence)
        )

    def _engagement_response_scale(self, *, use_fire_limits: bool) -> float:
        speed_value = int(max(10, min(100, int(getattr(self.cfg.engagement, "engagement_speed", 80) or 80))))
        ratio = float(speed_value - 10) / 90.0
        # Scale ranges [0.65, 1.0]: slow presets are dampened, fast presets are
        # at full authority.  Previously exceeded 1.0 at high speeds, which
        # amplified corrections and caused commanded_pan to race ahead of the
        # actual servo position, producing visible overshoot on initial lock-on.
        scale = min(1.0, 0.65 + (ratio * 0.85))
        if use_fire_limits:
            scale = min(scale, 1.0)
        return scale

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
        """Start engagement for a queued order with a stable first step."""
        self._reset_precision_state()
        self._remember_active_target(order.target.det, target=order.target, timestamp=now)
        # Seed aim anchors to the new order's planned position so that
        # loss recovery (if triggered immediately) searches near the
        # correct target, not the previous engagement's last aim point.
        self._active_target_last_aim_pan = self._clamp_pan(order.pan)
        self._active_target_last_aim_tilt = self._clamp_tilt(order.tilt)
        if self.cfg.engagement.precision_aim_enabled:
            # Avoid a blind first snap that can jump in the wrong direction.
            self._enter_precision_phase(now, order)
            return

        self._engage_phase = "aim"
        self._phase_start = now
        self._move_turret(order.pan, order.tilt)

    def _enter_precision_phase(self, now: float, order: EngagementOrder) -> None:
        """Switch to precision phase and start optional precision logging session."""
        self._engage_phase = "precision"
        self._phase_start = now
        self._reset_precision_state()

        target = self._find_active_target(order)
        if target is not None:
            initial_err_pan, initial_err_tilt = self._compute_tracking_angle_error(target, now, for_fire=False)
            initial_corr_pan, initial_corr_tilt, _, _ = self._compute_visual_servo_correction(
                initial_err_pan,
                initial_err_tilt,
                use_fire_limits=False,
            )
            if abs(initial_corr_pan) > 0.01 or abs(initial_corr_tilt) > 0.01:
                self._move_turret(self.current_pan + initial_corr_pan, self.current_tilt + initial_corr_tilt)

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
        if fired:
            burst = self.cfg.engagement.burst_count
            if self._cb_fire:
                self._cb_fire(burst)
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
        max_lead_tilt = max(0.0, float(getattr(eng, "predictive_max_lead_tilt_deg", 0.0) or 0.0))
        lead_pan = max(-max_lead_pan, min(max_lead_pan, pred_err_pan - raw_err_pan))
        lead_tilt = max(-max_lead_tilt, min(max_lead_tilt, pred_err_tilt - raw_err_tilt))
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
        return True

    def _stored_target_is_prediction_eligible(self) -> bool:
        if self._active_target_last_class in NON_SEMANTIC_PREDICTION_CLASSES:
            return False
        if self._active_target_last_source in {"frame_diff", "backsub", "color"}:
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
        self._loss_recovery_anchor_pan = float(self._active_target_last_aim_pan)
        self._loss_recovery_anchor_tilt = float(self._active_target_last_aim_tilt)
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
        # Add subtle organic jitter so search movements don't look robotic.
        # Seeded from the search index for repeatability, but visually natural.
        jitter_seed = int(self._loss_recovery_search_index * 97 + int(now * 100) % 137)
        jitter_rng = random.Random(jitter_seed)
        jitter_pan = jitter_rng.gauss(0.0, 0.35)
        jitter_tilt = jitter_rng.gauss(0.0, 0.22)
        target_pan = self._clamp_pan(target_pan + jitter_pan)
        target_tilt = self._clamp_tilt(target_tilt + jitter_tilt)
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
        eng = self.cfg.engagement
        if now < self._trigger_refractory_until:
            self._trigger_hold_start = 0.0
            self._trigger_gate_active = False
            return False

        enter_pan = float(eng.fire_trigger_enter_pan_tolerance)
        enter_tilt = float(eng.fire_trigger_enter_tilt_tolerance)
        exit_pan = max(enter_pan, float(eng.fire_trigger_exit_pan_tolerance))
        exit_tilt = max(enter_tilt, float(eng.fire_trigger_exit_tilt_tolerance))
        gate_pan = exit_pan if self._trigger_gate_active else enter_pan
        gate_tilt = exit_tilt if self._trigger_gate_active else enter_tilt

        centered = abs(lock_pan) <= gate_pan and abs(lock_tilt) <= gate_tilt
        stable = (
            self._err_pan_rate_deg_s <= float(eng.fire_trigger_max_pan_rate)
            and self._err_tilt_rate_deg_s <= float(eng.fire_trigger_max_tilt_rate)
        )
        trustworthy = (
            float(target.det.confidence) >= float(eng.fire_trigger_min_confidence)
            and float(target.persistence) >= float(eng.fire_trigger_min_persistence)
        )

        if self._current_no_fire_mask() is not None:
            self._trigger_hold_start = 0.0
            self._trigger_gate_active = False
            return False

        if not (centered and stable and trustworthy):
            self._trigger_hold_start = 0.0
            self._trigger_gate_active = False
            return False

        if self._trigger_hold_start <= 0.0:
            self._trigger_hold_start = now
            self._trigger_gate_active = True
            return False

        self._trigger_gate_active = True
        hold_elapsed = now - self._trigger_hold_start
        return hold_elapsed >= float(eng.fire_trigger_hold_time)

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
            pan_limit = float(eng.fire_micro_adjust_max_pan_step)
            tilt_limit = float(eng.fire_micro_adjust_max_tilt_step)
        else:
            pan_limit = float(eng.precision_max_pan_step) if float(eng.precision_max_pan_step) > 0.0 else float(eng.precision_max_step)
            tilt_limit = float(eng.precision_max_tilt_step) if float(eng.precision_max_tilt_step) > 0.0 else float(eng.precision_max_step)

        corr_pan = max(-pan_limit, min(pan_limit, corr_pan))
        corr_tilt = max(-tilt_limit, min(tilt_limit, corr_tilt))

        return corr_pan, corr_tilt, lock_pan, lock_tilt

    def _should_return_to_precision(self, err_pan: float, err_tilt: float) -> bool:
        eng = self.cfg.engagement
        return (
            abs(err_pan) > float(eng.fire_recenter_pan_tolerance)
            or abs(err_tilt) > float(eng.fire_recenter_tilt_tolerance)
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
            else:
                # Patrol modes — nudge turret toward guard home so it doesn't
                # stay stranded at the last engagement point while patrol re-inits.
                gp, gt = self._planner.get_return_position()
                self._move_turret(gp, gt)
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

    def _move_turret(self, pan: float, tilt: float) -> None:
        pan, tilt = self._clamp_angles(pan, tilt)
        if not self._motion_enabled:
            return
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

    # ------------------------------------------------------------------ #
    # External queries
    # ------------------------------------------------------------------ #

    def get_state_name(self) -> str:
        return self.state.name

    def get_engagement_stats(self) -> Dict:
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
            "loss_recovery_phase": self._loss_recovery_phase,
            "no_fire_mask": self._last_no_fire_mask_name,
            "motion_enabled": bool(self._motion_enabled),
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

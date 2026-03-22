"""
Smart Sentry v2 — Engine (Core State Machine)

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
from .target_filter import DetectedObject, TargetFilter
from .threat_scorer import ThreatScorer, TrackedTarget
from .engagement_planner import EngagementPlanner, EngagementOrder
from .ml_training_logger import MLTrainingLogger
from .sentry_v2_pir_manager import SentryV2PIRManager
from .precision_tuning_logger import PrecisionTuningLogger


NON_SEMANTIC_REACQUIRE_CLASSES = {"moving_object", "motion", "foreground", "color", "unknown"}


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
        self._last_no_fire_mask_name: str = ""

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
        self._pir_cue_pan: float = 0.0
        self._pir_cue_tilt: float = 0.0
        self._pir_cue_slew_start: float = 0.0
        self._pir_scan_mode: bool = False         # In adaptive scan?
        self._pir_scan_awaiting_settle: bool = False  # Waiting for servo settle before next scan point
        self._pir_settle_start: float = 0.0

        # ML training logger (optional: logs engagement decisions for model training)
        self._ml_logger = MLTrainingLogger()

        # Callbacks
        self._cb_fire: Optional[Callable[[int], None]] = None
        self._cb_move: Optional[Callable[[float, float], None]] = None
        self._cb_state: Optional[Callable[[SentryV2State, SentryV2State], None]] = None

    # ------------------------------------------------------------------ #
    # Callback registration
    # ------------------------------------------------------------------ #

    def on_fire(self, cb: Callable[[int], None]) -> None:
        self._cb_fire = cb

    def on_move(self, cb: Callable[[float, float], None]) -> None:
        self._cb_move = cb

    def on_state_change(self, cb: Callable[[SentryV2State, SentryV2State], None]) -> None:
        self._cb_state = cb

    def set_precision_logging_enabled(self, enabled: bool) -> None:
        """Enable or disable precision aiming tuning logger."""
        self._log_precision_tuning = bool(enabled)
        if enabled:
            self._precision_logging_faulted = False

    def is_precision_logging_enabled(self) -> bool:
        """Check if precision logging is currently enabled."""
        return self._log_precision_tuning

    def export_precision_logs(self, session_id: Optional[str] = None) -> Tuple[Optional[str], Optional[str]]:
        """
        Export precision logs to CSV and JSON summary files.

        Returns: (csv_path, json_path) of exported files, or ("", "") if no data.
        """
        return self._precision_logger.export_csv(session_id), self._precision_logger.export_summary(session_id)

    def print_precision_summary(self) -> None:
        """Print precision tuning summary to console."""
        self._precision_logger.print_summary()

    # ------------------------------------------------------------------ #
    # Lifecycle
    # ------------------------------------------------------------------ #

    def start(self) -> None:
        """Activate sentry — move to guard position and start watching."""
        self._change_state(SentryV2State.GUARDING)
        self._move_turret(self.cfg.guard.guard_pan, self.cfg.guard.guard_tilt)

    def stop(self) -> None:
        self._change_state(SentryV2State.PAUSED)
        if self._log_precision_tuning and self._current_precision_engagement_id:
            self._precision_logger.end_engagement()
            self._current_precision_engagement_id = None
        self._queue.clear()
        self._queue_index = 0
        self.active_order = None
        self._reset_precision_state()
        self._active_target_last_center = None
        self._active_target_last_bbox = None
        self._last_err_pan_deg = 0.0
        self._last_err_tilt_deg = 0.0
        self._last_reacquire_note = ""
        self._last_reacquire_time = 0.0

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

        if self.state == SentryV2State.PAUSED:
            return

        self._last_no_fire_mask_name = ""

        # 1. Filter
        qualified = self._filter.filter(detections)
        self.last_qualified = qualified

        # 2. Score
        scored = self._scorer.score(qualified, now)
        self.last_targets = scored

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
        self._pir_manager.on_pir_event(sensor_id, now)

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
                    # If PIR cue was active, cancel it (real target found)
                    self._pir_manager.cancel_active_cue()
                    self._pir_cue_mode = False
                    return

        # Check for PIR cues if enabled and no threats
        if self.cfg.pir_guard.pir_enabled and not self._pir_cue_mode:
            cue = self._pir_manager.get_next_cue(now)
            if cue is not None:
                # Start PIR cue pursuit
                self._pir_cue_mode = True
                self._pir_cue_pan = cue.cue_pan
                self._pir_cue_tilt = cue.cue_tilt
                self._pir_cue_slew_start = now
                self._pir_scan_mode = False
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

        # No threats and no PIR cues — run patrol logic
        self._update_patrol(now)

    def _update_pir_confirmation(self, targets: List[TrackedTarget], now: float) -> None:
        """Wait for camera to confirm a target at the PIR cue point."""
        # Check if servo has settled
        settle_time = 0.35
        slew_elapsed = now - self._pir_cue_slew_start
        
        if slew_elapsed < settle_time:
            return  # Still slewing
        
        # Check if we found targets above threshold
        if targets:
            # Found a target! Cancel PIR mode and let normal engagement take over
            self._pir_cue_mode = False
            self._pir_manager.cancel_active_cue()
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
            # Start adaptive scan
            self._pir_scan_mode = True
            self._pir_manager.start_scan(self._pir_cue_pan, self._pir_cue_tilt)
            self._pir_scan_awaiting_settle = False
            self._pir_settle_start = 0.0
        else:
            # No scan enabled, just cancel and return to patrol
            self._pir_cue_mode = False
            self._pir_manager.cancel_active_cue()
            self._patrol_initialized = False

    def _update_pir_scan(self, targets: List[TrackedTarget], now: float) -> None:
        """Run adaptive scan grid at PIR cue location."""
        # If we found targets during scan, engage them
        if targets:
            self._pir_cue_mode = False
            self._pir_scan_mode = False
            self._pir_manager.cancel_active_cue()
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
            settle_time = 0.25
            if now - self._pir_settle_start < settle_time:
                return  # Still settling
            self._pir_scan_awaiting_settle = False
        
        # Move to next scan point
        next_point = self._pir_manager.get_next_scan_point()
        if next_point is not None:
            self._move_turret(next_point[0], next_point[1])
            self._pir_scan_awaiting_settle = True
            self._pir_settle_start = now
        else:
            # Scan complete, no target found
            self._pir_cue_mode = False
            self._pir_scan_mode = False
            self._pir_manager.cancel_active_cue()
            self._patrol_initialized = False

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
            self._last_engage_time = now
            self._return_start = now
            self._change_state(SentryV2State.RETURNING)
            return

        order = self._queue[self._queue_index]
        self.active_order = order
        elapsed = now - self._phase_start

        if self._engage_phase == "aim":
            self._last_err_pan_deg = 0.0
            self._last_err_tilt_deg = 0.0
            aim_settle_time = 0.35
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
                if (now - self._target_lost_since) >= self.cfg.engagement.target_loss_timeout:
                    if bool(getattr(self.cfg.engagement, "continuous_hunt_on_loss", False)):
                        # Stay in precision/hunt mode and keep trying to reacquire
                        # instead of returning to guard.
                        self._aim_lock_frames = 0
                        self._last_err_pan_deg = 0.0
                        self._last_err_tilt_deg = 0.0
                        return
                    self._advance_queue(now)
                return
            self._target_lost_since = 0.0

            raw_err_pan, raw_err_tilt = self._compute_target_angle_error(target_det)
            corr_pan, corr_tilt, lock_pan, lock_tilt = self._compute_visual_servo_correction(
                raw_err_pan,
                raw_err_tilt,
                use_fire_limits=False,
            )
            self._update_error_rates(raw_err_pan, raw_err_tilt, now)
            self._last_err_pan_deg = float(raw_err_pan)
            self._last_err_tilt_deg = float(raw_err_tilt)

            if self._log_precision_tuning:
                eng = self.cfg.engagement
                target_pan = self.current_pan + raw_err_pan
                target_tilt = self.current_tilt + raw_err_tilt
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

            if self._has_aim_lock(lock_pan, lock_tilt):
                self._aim_lock_frames += 1
            else:
                self._aim_lock_frames = 0

            if (
                self.cfg.engagement.auto_trigger_enabled
                and elapsed >= settle
                and self._ready_to_fire()
                and target is not None
                and self._trigger_should_fire(target, lock_pan, lock_tilt, now)
            ):
                self._begin_fire(order, now)
                return

            if (
                self.cfg.engagement.auto_trigger_enabled
                and elapsed >= float(self.cfg.engagement.aim_lock_timeout)
                and target is not None
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
                self._last_err_pan_deg, self._last_err_tilt_deg = self._compute_target_angle_error(tracked_det)
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
                    self._last_engage_time = now
                    self._return_start = now
                    self.active_order = None
                    self._change_state(SentryV2State.RETURNING)

    def _find_active_target(self, order: EngagementOrder) -> Optional[TrackedTarget]:
        for target in self.last_targets:
            if target.det.track_id == order.target.det.track_id:
                self._remember_active_target(target.det)
                return target
        reacquired = self._find_reacquire_target(order)
        if reacquired is not None:
            old_track_id = int(order.target.det.track_id)
            order.target = reacquired
            self._remember_active_target(reacquired.det)
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
        anchor_diag = ((float(anchor_bbox[2]) ** 2) + (float(anchor_bbox[3]) ** 2)) ** 0.5
        anchor_area = self._bbox_area(anchor_bbox)
        reacquire_radius_px = max(72.0, min(frame_w, frame_h) * 0.16, anchor_diag * 0.60)

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
            if cost < best_cost:
                best_cost = cost
                best_target = target

        if best_target is None or best_cost > 0.75:
            return None
        return best_target

    def _remember_active_target(self, det: DetectedObject) -> None:
        self._active_target_last_center = (float(det.center_x), float(det.center_y))
        self._active_target_last_bbox = tuple(int(v) for v in det.bbox)

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

    def _safe_log_precision_frame(self, **kwargs: object) -> None:
        if not self._log_precision_tuning or self._precision_logging_faulted:
            return
        try:
            self._precision_logger.log_frame(**kwargs)
        except Exception:
            self._precision_logging_faulted = True
            self._log_precision_tuning = False

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
            self._remember_active_target(nxt.target.det)
            self._start_order_engagement(nxt, now)
        else:
            self._last_engage_time = now
            self._return_start = now
            self.active_order = None
            self._active_target_last_center = None
            self._active_target_last_bbox = None
            self._change_state(SentryV2State.RETURNING)

    def _start_order_engagement(self, order: EngagementOrder, now: float) -> None:
        """Start engagement for a queued order with a stable first step."""
        self._reset_precision_state()
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

        if not self._log_precision_tuning or self._precision_logging_faulted:
            return

        target = self._find_active_target(order)
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
        except Exception:
            self._precision_logging_faulted = True
            self._log_precision_tuning = False
            self._current_precision_engagement_id = None

    def _begin_fire(self, order: EngagementOrder, now: float) -> None:
        """Transition to fire phase — respects auto_trigger_enabled gate."""
        blocked_mask = self._current_no_fire_mask()
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

        # Only actually fire if auto-trigger is enabled
        if self.cfg.engagement.auto_trigger_enabled and blocked_mask is None:
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
            "fired": self.cfg.engagement.auto_trigger_enabled and blocked_mask is None,
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

    def _compute_target_angle_error(self, det: DetectedObject) -> Tuple[float, float]:
        fw = float(max(1, det.frame_width or self.cfg.guard.frame_width or 640))
        fh = float(max(1, det.frame_height or self.cfg.guard.frame_height or 480))
        norm_cx = float(det.center_x) / fw
        norm_cy = float(det.center_y) / fh
        return self._planner.pixel_error_to_angle_error(norm_cx, norm_cy)

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
        return (now - self._trigger_hold_start) >= float(eng.fire_trigger_hold_time)

    def _compute_visual_servo_correction(
        self,
        err_pan: float,
        err_tilt: float,
        *,
        use_fire_limits: bool,
    ) -> Tuple[float, float, float, float]:
        eng = self.cfg.engagement
        alpha = max(0.0, min(1.0, float(eng.precision_error_ema)))
        if alpha <= 0.0:
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

        d_pan = ctrl_pan - self._pid_prev_err_pan
        d_tilt = ctrl_tilt - self._pid_prev_err_tilt
        self._pid_prev_err_pan = ctrl_pan
        self._pid_prev_err_tilt = ctrl_tilt

        corr_pan = eng.precision_kp * ctrl_pan + eng.precision_ki * self._pid_integral_pan + eng.precision_kd * d_pan
        corr_tilt = eng.precision_kp * ctrl_tilt + eng.precision_ki * self._pid_integral_tilt + eng.precision_kd * d_tilt

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
            # For static mode, return to guard point; for patrol modes,
            # the patrol logic will smoothly resume from current position.
            if self.cfg.guard.guard_mode == 0:
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
        print(f"DEBUG: PID MOVE (engine): pan={pan:.3f}, tilt={tilt:.3f}")
        pan, tilt = self._clamp_angles(pan, tilt)
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
            "targets_visible": len(self.last_targets),
            "targets_qualified": len(self.last_qualified),
            "queue_length": len(self._queue),
            "queue_position": self._queue_index,
            "engagements_total": len(self.engagement_log),
            "aim_lock_frames": self._aim_lock_frames,
            "last_err_pan_deg": round(self._last_err_pan_deg, 3),
            "last_err_tilt_deg": round(self._last_err_tilt_deg, 3),
            "reacquire_note": self._last_reacquire_note,
            "reacquire_recent": bool(self._last_reacquire_time and (time.time() - self._last_reacquire_time) <= 2.0),
            "no_fire_mask": self._last_no_fire_mask_name,
        }

    # ------------------------------------------------------------------ #
    # ML Training (Optional)
    # ------------------------------------------------------------------ #

    def get_ml_logger(self) -> MLTrainingLogger:
        """Return the ML training logger for recording engagement data."""
        return self._ml_logger

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

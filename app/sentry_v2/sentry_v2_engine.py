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
from .target_filter import DetectedObject, TargetFilter
from .threat_scorer import ThreatScorer, TrackedTarget
from .engagement_planner import EngagementPlanner, EngagementOrder


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

        # Sub-systems
        self._filter = TargetFilter(config.target_filter)
        self._scorer = ThreatScorer(config.threat_scoring, config.target_filter)
        self._planner = EngagementPlanner(config.engagement, config.guard)

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

    # ------------------------------------------------------------------ #
    # Lifecycle
    # ------------------------------------------------------------------ #

    def start(self) -> None:
        """Activate sentry — move to guard position and start watching."""
        self._change_state(SentryV2State.GUARDING)
        self._move_turret(self.cfg.guard.guard_pan, self.cfg.guard.guard_tilt)

    def stop(self) -> None:
        self._change_state(SentryV2State.PAUSED)
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
        self._planner.update_config(config.engagement, config.guard)

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
    # GUARDING state
    # ------------------------------------------------------------------ #

    def _update_guarding(self, targets: List[TrackedTarget], now: float) -> None:
        """
        In GUARDING: patrol or hold position, and watch for threats.
        If scoreable threats exist above threshold, plan engagement.
        """
        # Check for threats first — engagement always takes priority
        if targets:
            if now - self._last_engage_time >= self.cfg.engagement.cycle_cooldown:
                queue = self._planner.plan(targets, self.current_pan, self.current_tilt)
                if queue:
                    self._queue = queue
                    self.last_queue = queue
                    self._queue_index = 0
                    self._engage_phase = "aim"
                    self._phase_start = now
                    self._patrol_initialized = False  # reset patrol on re-entry
                    self._reset_precision_state()
                    self._change_state(SentryV2State.ENGAGING)
                    first = self._queue[0]
                    self.active_order = first
                    self._remember_active_target(first.target.det)
                    self._move_turret(first.pan, first.tilt)
                    return

        # No threats — run patrol logic
        self._update_patrol(now)

    # ------------------------------------------------------------------ #
    # ENGAGING state
    # ------------------------------------------------------------------ #

    def _update_engaging(self, now: float) -> None:
        """
        Work through the engagement queue:
          aim → (precision refinement) → fire → inter-target cooldown → next
        """
        if self._queue_index >= len(self._queue):
            # All targets engaged — start returning
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
            # Give servo time to reach target (~300ms should be enough)
            aim_settle_time = 0.35
            if elapsed >= aim_settle_time:
                # Check if precision aiming is enabled
                if self.cfg.engagement.precision_aim_enabled:
                    self._engage_phase = "precision"
                    self._phase_start = now
                    self._reset_precision_state()
                else:
                    self._begin_fire(order, now)

        elif self._engage_phase == "precision":
            # Live visual-servo refinement using the latest target center.
            settle = self.cfg.engagement.precision_settle_time
            target = self._find_active_target(order)
            target_det = target.det if target is not None else None
            if target_det is None:
                if self._target_lost_since <= 0.0:
                    self._target_lost_since = now
                if (now - self._target_lost_since) >= self.cfg.engagement.target_loss_timeout:
                    self._advance_queue(now)
                return
            else:
                self._target_lost_since = 0.0

            raw_err_pan, raw_err_tilt = self._compute_target_angle_error(target_det)

            corr_pan, corr_tilt, lock_pan, lock_tilt = self._compute_visual_servo_correction(
                raw_err_pan,
                raw_err_tilt,
                use_fire_limits=False,
            )
            self._update_error_rates(lock_pan, lock_tilt, now)
            self._last_err_pan_deg = float(raw_err_pan)
            self._last_err_tilt_deg = float(raw_err_tilt)

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

            if corr_pan != 0.0 or corr_tilt != 0.0:
                new_pan = self.current_pan + corr_pan
                new_tilt = self.current_tilt + corr_tilt
                self._move_turret(new_pan, new_tilt)

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
                    if corr_pan != 0.0 or corr_tilt != 0.0:
                        self._move_turret(self.current_pan + corr_pan, self.current_tilt + corr_tilt)
            else:
                self._last_err_pan_deg = 0.0
                self._last_err_tilt_deg = 0.0
            # Wait for burst duration + inter-target cooldown
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
                # Move to next target
                self._queue_index += 1
                if self._queue_index < len(self._queue):
                    nxt = self._queue[self._queue_index]
                    self.active_order = nxt
                    self._remember_active_target(nxt.target.det)
                    self._move_turret(nxt.pan, nxt.tilt)
                    self._engage_phase = "aim"
                    self._phase_start = now
                    self._reset_precision_state()
                else:
                    # Done
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
        frame_w = float(max(1, self.cfg.guard.frame_width))
        frame_h = float(max(1, self.cfg.guard.frame_height))
        anchor_diag = ((float(anchor_bbox[2]) ** 2) + (float(anchor_bbox[3]) ** 2)) ** 0.5
        reacquire_radius_px = max(90.0, min(frame_w, frame_h) * 0.22, anchor_diag * 0.75)

        best_target: Optional[TrackedTarget] = None
        best_cost = float("inf")

        for target in self.last_targets:
            det = target.det
            target_class = str(det.class_name or "").strip().lower()
            if anchor_class and anchor_class not in {"moving_object", "motion", "foreground", "color", "unknown"}:
                if target_class and target_class != anchor_class:
                    continue

            dist_px = ((float(det.center_x) - anchor_center[0]) ** 2 + (float(det.center_y) - anchor_center[1]) ** 2) ** 0.5
            iou = self._bbox_iou(anchor_bbox, det.bbox)
            if dist_px > reacquire_radius_px and iou < 0.05:
                continue

            cost = dist_px - (iou * reacquire_radius_px * 0.75) - (target.threat_score * 20.0)
            if cost < best_cost:
                best_cost = cost
                best_target = target

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

    def _has_aim_lock(self, err_pan: float, err_tilt: float) -> bool:
        return (
            abs(err_pan) <= self.cfg.engagement.aim_lock_pan_tolerance
            and abs(err_tilt) <= self.cfg.engagement.aim_lock_tilt_tolerance
        )

    def _ready_to_fire(self) -> bool:
        if not self.cfg.engagement.fire_requires_lock:
            return True
        return self._aim_lock_frames >= max(1, self.cfg.engagement.aim_lock_required_frames)

    def _advance_queue(self, now: float) -> None:
        self._queue_index += 1
        self._reset_precision_state()
        if self._queue_index < len(self._queue):
            nxt = self._queue[self._queue_index]
            self.active_order = nxt
            self._remember_active_target(nxt.target.det)
            self._move_turret(nxt.pan, nxt.tilt)
            self._engage_phase = "aim"
            self._phase_start = now
        else:
            self._last_engage_time = now
            self._return_start = now
            self.active_order = None
            self._active_target_last_center = None
            self._active_target_last_bbox = None
            self._change_state(SentryV2State.RETURNING)

    def _begin_fire(self, order: EngagementOrder, now: float) -> None:
        """Transition to fire phase — respects auto_trigger_enabled gate."""
        self._engage_phase = "fire"
        self._phase_start = now
        self._trigger_gate_active = False
        self._trigger_hold_start = 0.0
        self._trigger_refractory_until = max(
            self._trigger_refractory_until,
            now + float(self.cfg.engagement.fire_trigger_refractory_time),
        )

        # Only actually fire if auto-trigger is enabled
        if self.cfg.engagement.auto_trigger_enabled:
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
            "fired": self.cfg.engagement.auto_trigger_enabled,
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
        }

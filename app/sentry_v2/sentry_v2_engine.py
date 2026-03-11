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

        # Timing
        self._last_engage_time: float = 0.0
        self._return_start: float = 0.0

        # Per-frame results (exposed for overlay)
        self.last_targets: List[TrackedTarget] = []
        self.last_qualified: List[DetectedObject] = []
        self.last_queue: List[EngagementOrder] = []
        self.active_order: Optional[EngagementOrder] = None
        self.engagement_log: List[Dict] = []  # recent engagement history

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
        In GUARDING: turret is stationary at guard position.
        If scoreable threats exist above threshold, plan engagement.
        """
        if not targets:
            return

        # Respect cycle cooldown
        if now - self._last_engage_time < self.cfg.engagement.cycle_cooldown:
            return

        queue = self._planner.plan(targets, self.current_pan, self.current_tilt)
        if queue:
            self._queue = queue
            self.last_queue = queue
            self._queue_index = 0
            self._engage_phase = "aim"
            self._phase_start = now
            self._change_state(SentryV2State.ENGAGING)
            # Start aiming at first target
            first = self._queue[0]
            self.active_order = first
            self._move_turret(first.pan, first.tilt)

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
            # Give servo time to reach target (~300ms should be enough)
            aim_settle_time = 0.35
            if elapsed >= aim_settle_time:
                # Check if precision aiming is enabled
                if self.cfg.engagement.precision_aim_enabled:
                    self._engage_phase = "precision"
                    self._phase_start = now
                    # Reset PID state
                    self._pid_integral_pan = 0.0
                    self._pid_integral_tilt = 0.0
                    self._pid_prev_err_pan = 0.0
                    self._pid_prev_err_tilt = 0.0
                else:
                    self._begin_fire(order, now)

        elif self._engage_phase == "precision":
            # PID refinement using latest detection position
            settle = self.cfg.engagement.precision_settle_time
            if elapsed >= settle:
                self._begin_fire(order, now)
            else:
                # Find the tracked target matching this order in latest detections
                target_det = None
                for t in self.last_targets:
                    if t.det.track_id == order.target.det.track_id:
                        target_det = t.det
                        break
                if target_det is None and self.last_qualified:
                    # Fallback: use nearest qualified detection
                    target_det = self.last_qualified[0] if self.last_qualified else None

                if target_det is not None:
                    # Compute error between current aim and target center
                    fw = self.cfg.guard.frame_width or 640
                    fh = self.cfg.guard.frame_height or 480
                    norm_cx = target_det.center_x / fw
                    norm_cy = target_det.center_y / fh
                    # Target should be at frame center (0.5, 0.5)
                    err_pan = (norm_cx - 0.5) * self.cfg.guard.camera_hfov
                    err_tilt = (norm_cy - 0.5) * self.cfg.guard.camera_vfov

                    # PID computation
                    kp = self.cfg.engagement.precision_kp
                    ki = self.cfg.engagement.precision_ki
                    kd = self.cfg.engagement.precision_kd
                    max_step = self.cfg.engagement.precision_max_step

                    self._pid_integral_pan += err_pan
                    self._pid_integral_tilt += err_tilt
                    d_pan = err_pan - self._pid_prev_err_pan
                    d_tilt = err_tilt - self._pid_prev_err_tilt
                    self._pid_prev_err_pan = err_pan
                    self._pid_prev_err_tilt = err_tilt

                    corr_pan = kp * err_pan + ki * self._pid_integral_pan + kd * d_pan
                    corr_tilt = kp * err_tilt + ki * self._pid_integral_tilt + kd * d_tilt

                    # Clamp corrections
                    corr_pan = max(-max_step, min(max_step, corr_pan))
                    corr_tilt = max(-max_step, min(max_step, corr_tilt))

                    new_pan = self.current_pan + corr_pan
                    new_tilt = self.current_tilt + corr_tilt
                    self._move_turret(new_pan, new_tilt)

        elif self._engage_phase == "fire":
            # Wait for burst duration + inter-target cooldown
            burst_duration = (
                self.cfg.engagement.burst_count
                * self.cfg.engagement.burst_interval_ms
                / 1000.0
            )
            wait = burst_duration + self.cfg.engagement.inter_target_cooldown
            if elapsed >= wait:
                # Move to next target
                self._queue_index += 1
                if self._queue_index < len(self._queue):
                    nxt = self._queue[self._queue_index]
                    self.active_order = nxt
                    self._move_turret(nxt.pan, nxt.tilt)
                    self._engage_phase = "aim"
                    self._phase_start = now
                else:
                    # Done
                    self._last_engage_time = now
                    self._return_start = now
                    self.active_order = None
                    self._change_state(SentryV2State.RETURNING)

    def _begin_fire(self, order: EngagementOrder, now: float) -> None:
        """Transition to fire phase — respects auto_trigger_enabled gate."""
        self._engage_phase = "fire"
        self._phase_start = now

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

    # ------------------------------------------------------------------ #
    # RETURNING state
    # ------------------------------------------------------------------ #

    def _update_returning(self, now: float) -> None:
        """Wait briefly, then return to guard position."""
        if now - self._return_start >= self.cfg.engagement.return_delay:
            gp, gt = self._planner.get_return_position()
            self._move_turret(gp, gt)
            self._change_state(SentryV2State.GUARDING)

    # ------------------------------------------------------------------ #
    # Turret helpers
    # ------------------------------------------------------------------ #

    def _move_turret(self, pan: float, tilt: float) -> None:
        self.current_pan = pan
        self.current_tilt = tilt
        if self._cb_move:
            self._cb_move(pan, tilt)

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
        }

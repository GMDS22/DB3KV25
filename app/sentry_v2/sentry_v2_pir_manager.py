"""
SMART SENTRY V3 — PIR Sensor Manager

Manages PIR sensor state, debouncing, and cue generation for blind-spot detection.
"""

from __future__ import annotations

import time
import inspect
from typing import Callable, Dict, List, Optional, Tuple

from .sentry_v2_config import PIRGuardConfig, PIRSensorConfig


class PIRSensorEvent:
    """Single PIR sensor event with timestamp."""
    
    def __init__(self, sensor_id: int, cue_pan: float, cue_tilt: float, timestamp: float):
        self.sensor_id = sensor_id
        self.cue_pan = cue_pan
        self.cue_tilt = cue_tilt
        self.timestamp = timestamp


class SentryV2PIRManager:
    """Manages PIR sensor state and generates turret cues."""
    
    def __init__(self, config: PIRGuardConfig):
        self.cfg = config
        self._trace_callback: Optional[Callable[[Dict[str, object]], None]] = None
        
        # Debounce tracking per sensor: {sensor_id: last_fire_time}
        self._last_fire_time: dict = {}
        
        # Queue of pending cue events
        self._cue_queue: List[PIRSensorEvent] = []
        self._last_accepted_event_time: float = 0.0
        self._last_accepted_sensor_id: Optional[int] = None
        
        # Current active cue (being pursued by turret)
        self._active_cue: Optional[PIRSensorEvent] = None
        self._active_cue_start: float = 0.0
        
        # Scan state (if adaptive scan is active)
        self._scan_active: bool = False
        self._scan_points: List[Tuple[float, float]] = []  # (pan, tilt) scan grid
        self._scan_index: int = 0
        self._scan_point_visited: set = set()  # Track visited points during scan
        self._scan_reference_point: Optional[Tuple[float, float]] = None

    def set_trace_callback(self, callback: Optional[Callable[[Dict[str, object]], None]]) -> None:
        """Register an optional diagnostics callback for PIR queue/state tracing."""
        self._trace_callback = callback

    def _trace(self, action: str, **fields: object) -> None:
        callback = self._trace_callback
        if callback is None:
            return
        frame = inspect.currentframe()
        caller = frame.f_back if frame is not None else None
        payload: Dict[str, object] = {
            "component": "pir_manager",
            "action": str(action),
            "timestamp": float(time.time()),
            "function": caller.f_code.co_name if caller is not None else "",
            "filename": __file__,
            "line": int(caller.f_lineno) if caller is not None else 0,
            "queue_length": int(len(self._cue_queue)),
            "active_cue": bool(self._active_cue is not None),
        }
        payload.update(fields)
        try:
            callback(payload)
        except Exception:
            pass

    def _search_style(self, override: Optional[str] = None) -> str:
        style = str(override or getattr(self.cfg, "search_style", "hunting") or "hunting").strip().lower()
        if style in {"fast", "fast_reacquire", "fast-reacquire", "reacquire"}:
            return "fast_reacquire"
        return "hunting"

    def _sensor_pan_bias(self, sensor_id: Optional[int], center_pan: float) -> float:
        if sensor_id is not None and 0 <= int(sensor_id) < len(self.cfg.sensors):
            cue_pan = float(self.cfg.sensors[int(sensor_id)].cue_pan)
        else:
            cue_pan = float(center_pan)
        delta = cue_pan - 135.0
        if abs(delta) < 4.0:
            return 0.0
        return 1.0 if delta > 0.0 else -1.0

    def _append_unique_point(
        self,
        points: List[Tuple[float, float]],
        seen: set[Tuple[float, float]],
        pan: float,
        tilt: float,
    ) -> None:
        point = (
            max(0.0, min(270.0, float(pan))),
            max(0.0, min(110.0, float(tilt))),
        )
        if point in seen:
            return
        seen.add(point)
        points.append(point)

    def _point_distance(
        self,
        source: Tuple[float, float],
        target: Tuple[float, float],
    ) -> float:
        pan_delta = abs(float(target[0]) - float(source[0]))
        tilt_delta = abs(float(target[1]) - float(source[1]))
        return pan_delta + (tilt_delta * 1.15)

    def _smooth_path(
        self,
        points: List[Tuple[float, float]],
        start: Tuple[float, float],
    ) -> List[Tuple[float, float]]:
        remaining = list(points)
        ordered: List[Tuple[float, float]] = []
        current = (float(start[0]), float(start[1]))
        while remaining:
            next_index = min(
                range(len(remaining)),
                key=lambda idx: self._point_distance(current, remaining[idx]),
            )
            point = remaining.pop(next_index)
            ordered.append(point)
            current = point
        return ordered

    def _apply_search_rounds(
        self,
        points: List[Tuple[float, float]],
        center_pan: float,
        center_tilt: float,
        search_style: str,
    ) -> List[Tuple[float, float]]:
        rounds = max(1, int(getattr(self.cfg, "search_rounds", 1) or 1))
        if not points:
            return []

        ordered_rounds: List[Tuple[float, float]] = []
        seen: set[Tuple[float, float]] = set()
        current_start = (float(center_pan), float(center_tilt))
        scale_step = 0.18 if search_style == "fast_reacquire" else 0.12

        for round_index in range(rounds):
            scale = 1.0 + (scale_step * round_index)
            round_points: List[Tuple[float, float]] = []
            round_seen: set[Tuple[float, float]] = set()
            for point_pan, point_tilt in points:
                scaled_pan = center_pan + ((point_pan - center_pan) * scale)
                scaled_tilt = center_tilt + ((point_tilt - center_tilt) * scale)
                self._append_unique_point(round_points, round_seen, scaled_pan, scaled_tilt)
            for point in self._smooth_path(round_points, current_start):
                if point in seen:
                    continue
                seen.add(point)
                ordered_rounds.append(point)
            current_start = ordered_rounds[-1] if ordered_rounds else current_start

        return ordered_rounds

    def _local_hunt_points(
        self,
        center_pan: float,
        center_tilt: float,
        pan_range: float,
        tilt_range: float,
        sensor_id: Optional[int],
        search_style: str,
    ) -> List[Tuple[float, float]]:
        points: List[Tuple[float, float]] = []
        seen: set[Tuple[float, float]] = set()
        bias_pan = self._sensor_pan_bias(sensor_id, center_pan)
        bias_primary = bias_pan if abs(bias_pan) >= 0.1 else 1.0

        if search_style == "fast_reacquire":
            near_pan = max(1.2, pan_range * 0.32)
            near_tilt = max(0.8, tilt_range * 0.32)
            mid_pan = max(near_pan + 0.6, pan_range * 0.58)
            mid_tilt = max(near_tilt + 0.4, tilt_range * 0.55)
        else:
            near_pan = max(1.0, pan_range * 0.22)
            near_tilt = max(0.7, tilt_range * 0.24)
            mid_pan = max(near_pan + 0.8, pan_range * 0.46)
            mid_tilt = max(near_tilt + 0.5, tilt_range * 0.44)

        local_pattern = [
            (bias_primary * near_pan, 0.0),
            (bias_primary * near_pan * 0.62, near_tilt * 0.80),
            (bias_primary * near_pan * 0.62, -near_tilt * 0.80),
            (0.0, near_tilt),
            (0.0, -near_tilt),
            (-bias_primary * near_pan * 0.42, 0.0),
            (bias_primary * mid_pan, 0.0),
            (bias_primary * mid_pan * 0.72, mid_tilt * 0.82),
            (bias_primary * mid_pan * 0.72, -mid_tilt * 0.82),
        ]
        if search_style != "fast_reacquire":
            local_pattern.extend([
                (-bias_primary * near_pan * 0.48, near_tilt * 0.75),
                (-bias_primary * near_pan * 0.48, -near_tilt * 0.75),
                (0.0, mid_tilt),
                (0.0, -mid_tilt),
            ])

        for pan_offset, tilt_offset in local_pattern:
            self._append_unique_point(points, seen, center_pan + pan_offset, center_tilt + tilt_offset)
        return self._apply_search_rounds(points, center_pan, center_tilt, search_style)
        
    def update_config(self, config: PIRGuardConfig) -> None:
        """Hot-reload configuration."""
        self.cfg = config
        queue_before = int(len(self._cue_queue))
        # Clear internal state on config change
        self._last_fire_time.clear()
        self._cue_queue.clear()
        self._active_cue = None
        self._scan_active = False
        self._scan_reference_point = None
        self._last_accepted_event_time = 0.0
        self._last_accepted_sensor_id = None
        self._trace("config_update_reset", queue_before=queue_before, queue_after=int(len(self._cue_queue)))
        
    def on_pir_event(self, sensor_id: int, timestamp: float) -> None:
        """Called when a PIR sensor fires. Handles debouncing and queueing."""
        queue_before = int(len(self._cue_queue))
        self._trace("event_received", sensor_id=int(sensor_id), event_timestamp=float(timestamp), queue_before=queue_before)
        if not self.cfg.pir_enabled:
            self._trace("event_ignored_disabled", sensor_id=int(sensor_id), queue_before=queue_before)
            return
        
        if sensor_id < 0 or sensor_id >= len(self.cfg.sensors):
            self._trace("event_ignored_invalid_sensor", sensor_id=int(sensor_id), queue_before=queue_before)
            return
        
        sensor = self.cfg.sensors[sensor_id]
        if not sensor.enabled:
            self._trace("event_ignored_sensor_disabled", sensor_id=int(sensor_id), queue_before=queue_before)
            return
        
        # Check debounce
        now = timestamp or time.time()
        last_fire = self._last_fire_time.get(sensor_id, 0.0)
        debounce_s = sensor.debounce_ms / 1000.0
        
        if now - last_fire < debounce_s:
            self._trace(
                "event_ignored_debounce",
                sensor_id=int(sensor_id),
                event_timestamp=float(now),
                last_fire_timestamp=float(last_fire),
                debounce_s=float(debounce_s),
                delta_s=float(now - last_fire),
                queue_before=queue_before,
            )
            return  # Still in debounce period

        configured_cross_lockout_s = max(0.0, float(getattr(self.cfg, "cross_sensor_lockout_ms", 0) or 0) / 1000.0)
        cross_lockout_cap_s = min(0.18, max(0.08, debounce_s * 0.35))
        cross_lockout_s = min(configured_cross_lockout_s, cross_lockout_cap_s)
        if (
            cross_lockout_s > 0.0
            and self._last_accepted_sensor_id is not None
            and int(self._last_accepted_sensor_id) != int(sensor_id)
            and (now - self._last_accepted_event_time) < cross_lockout_s
        ):
            self._trace(
                "event_ignored_cross_sensor_lockout",
                sensor_id=int(sensor_id),
                previous_sensor_id=int(self._last_accepted_sensor_id),
                cross_lockout_s=float(cross_lockout_s),
                delta_s=float(now - self._last_accepted_event_time),
                queue_before=queue_before,
            )
            return
        
        self._last_fire_time[sensor_id] = now
        self._last_accepted_event_time = now
        self._last_accepted_sensor_id = int(sensor_id)
        
        # Create cue event and queue it
        event = PIRSensorEvent(
            sensor_id=sensor_id,
            cue_pan=sensor.cue_pan,
            cue_tilt=sensor.cue_tilt,
            timestamp=now,
        )
        self._cue_queue.append(event)
        self._trace(
            "event_enqueued",
            sensor_id=int(sensor_id),
            cue_pan=float(sensor.cue_pan),
            cue_tilt=float(sensor.cue_tilt),
            event_timestamp=float(now),
            queue_before=queue_before,
            queue_after=int(len(self._cue_queue)),
        )
    
    def has_pending_cue(self) -> bool:
        """Check if there's a queued or active cue waiting to be processed."""
        return len(self._cue_queue) > 0 or self._active_cue is not None
    
    def get_next_cue(self, now: float) -> Optional[PIRSensorEvent]:
        """
        Get the next cue to process.
        Returns None if no cues available or if active cue is still being pursued.
        """
        if not self.cfg.pir_enabled:
            self._trace("get_next_cue_disabled", now=float(now))
            return None
        
        # If there's an active cue, check if it has timed out
        if self._active_cue is not None:
            if now - self._active_cue_start < self.cfg.confirmation_timeout:
                self._trace(
                    "active_cue_still_pending",
                    now=float(now),
                    active_sensor_id=int(self._active_cue.sensor_id),
                    active_age_s=float(now - self._active_cue_start),
                    confirmation_timeout_s=float(self.cfg.confirmation_timeout),
                )
                return None  # Still pursuing current cue
            else:
                self._trace(
                    "active_cue_confirmation_timeout",
                    now=float(now),
                    active_sensor_id=int(self._active_cue.sensor_id),
                    active_age_s=float(now - self._active_cue_start),
                    confirmation_timeout_s=float(self.cfg.confirmation_timeout),
                )
                self._active_cue = None  # Timeout reached, clear it
        
        # Discard stale events before popping (data_timeout_ms guard)
        timeout_s = self.cfg.data_timeout_ms / 1000.0
        while self._cue_queue:
            if now - self._cue_queue[0].timestamp > timeout_s:
                expired = self._cue_queue[0]
                self._cue_queue.pop(0)  # too old, discard
                self._trace(
                    "queued_event_expired",
                    now=float(now),
                    sensor_id=int(expired.sensor_id),
                    event_timestamp=float(expired.timestamp),
                    age_s=float(now - expired.timestamp),
                    timeout_s=float(timeout_s),
                    queue_after=int(len(self._cue_queue)),
                )
            else:
                break

        # Try to get next from queue
        if self._cue_queue:
            queue_before = int(len(self._cue_queue))
            cue = self._cue_queue.pop(0)
            self._active_cue = cue
            self._active_cue_start = now
            self._scan_active = False  # Reset scan state
            self._scan_index = 0
            self._trace(
                "event_dequeued_to_active",
                now=float(now),
                sensor_id=int(cue.sensor_id),
                cue_pan=float(cue.cue_pan),
                cue_tilt=float(cue.cue_tilt),
                event_timestamp=float(cue.timestamp),
                queue_before=queue_before,
                queue_after=int(len(self._cue_queue)),
            )
            return cue

        self._trace("queue_empty_no_cue", now=float(now))
        return None
    
    def generate_scan_grid(
        self,
        center_pan: float,
        center_tilt: float,
        sensor_id: Optional[int] = None,
        search_style: Optional[str] = None,
    ) -> List[Tuple[float, float]]:
        """
        Generate an ordered search pattern centered at the cue point.
        Returns list of (pan, tilt) points to visit, starting at center and
        expanding outward in the same kind of center-first search rhythm used
        by target-loss recovery.
        """
        pan_range = self._effective_scan_pan_range()
        tilt_range = self.cfg.scan_tilt_range
        resolution = self.cfg.scan_grid_resolution

        def _clamp_point(pan: float, tilt: float) -> Tuple[float, float]:
            return (
                max(0.0, min(270.0, float(pan))),
                max(0.0, min(110.0, float(tilt))),
            )

        if resolution <= 1:
            return [_clamp_point(center_pan, center_tilt)]

        points: List[Tuple[float, float]] = []
        seen: set[Tuple[float, float]] = set()
        style = self._search_style(search_style)

        def _append_point(pan: float, tilt: float) -> None:
            self._append_unique_point(points, seen, pan, tilt)

        _append_point(center_pan, center_tilt)

        for point_pan, point_tilt in self._local_hunt_points(
            center_pan,
            center_tilt,
            pan_range,
            tilt_range,
            sensor_id,
            style,
        ):
            _append_point(point_pan, point_tilt)

        ring_count = max(1, int(resolution) - 1)
        pan_bias = self._sensor_pan_bias(sensor_id, center_pan)
        pan_order = [1.0, -1.0] if pan_bias >= 0.0 else [-1.0, 1.0]
        for ring in range(1, ring_count + 1):
            scale = float(ring) / float(ring_count)
            pan_step = pan_range * scale
            tilt_step = tilt_range * scale

            # Center-first expanding search: early points stay biased toward
            # the firing sensor's sector before the pattern mirrors outward.
            for sign in pan_order:
                _append_point(center_pan + (pan_step * sign), center_tilt)
            _append_point(center_pan, center_tilt + tilt_step)
            _append_point(center_pan, center_tilt - tilt_step)
            for sign in pan_order:
                _append_point(center_pan + (pan_step * sign), center_tilt + tilt_step)
                _append_point(center_pan + (pan_step * sign), center_tilt - tilt_step)

        return self._apply_search_rounds(points, center_pan, center_tilt, style)

    def _effective_scan_pan_range(self) -> float:
        configured = float(max(5.0, self.cfg.scan_pan_range))
        enabled_cues = [
            float(sensor.cue_pan)
            for sensor in self.cfg.sensors
            if bool(getattr(sensor, "enabled", False))
        ]
        if len(enabled_cues) < 2:
            return configured

        normalized = sorted((cue % 360.0) for cue in enabled_cues)
        separations: List[float] = []
        for idx, cue in enumerate(normalized):
            nxt = normalized[(idx + 1) % len(normalized)]
            delta = (nxt - cue) % 360.0
            if delta > 0.0:
                separations.append(delta)
        if not separations:
            return configured

        min_separation = min(separations)
        non_overlap_limit = max(5.0, min_separation * 0.45)
        return float(min(configured, non_overlap_limit))
    
    def start_scan(
        self,
        center_pan: float,
        center_tilt: float,
        sensor_id: Optional[int] = None,
        search_style: Optional[str] = None,
    ) -> None:
        """Start an adaptive scan at the cue location."""
        self._scan_active = True
        self._scan_points = self.generate_scan_grid(
            center_pan,
            center_tilt,
            sensor_id=sensor_id,
            search_style=search_style,
        )
        center_point = (float(max(0.0, min(270.0, center_pan))), float(max(0.0, min(110.0, center_tilt))))
        if len(self._scan_points) > 1 and self._scan_points[0] == center_point:
            self._scan_points = self._scan_points[1:]
        self._scan_index = 0
        self._scan_point_visited.clear()
        self._scan_reference_point = center_point
    
    def get_next_scan_point(self) -> Optional[Tuple[float, float]]:
        """Get the next point in the scan grid. Returns None if scan complete."""
        if not self._scan_active or not self._scan_points:
            return None
        
        if self._scan_index >= len(self._scan_points):
            self._scan_active = False
            self._scan_reference_point = None
            return None
        
        point = self._scan_points[self._scan_index]
        self._scan_index += 1
        self._scan_reference_point = point
        return point
    
    def complete_active_cue(self) -> None:
        """Mark the active cue as resolved (target found/engaged).

        Clears only the active cue and scan state — queued events from
        other sensors are preserved so the hunt protocol can continue
        investigating remaining zones.
        """
        queue_before = int(len(self._cue_queue))
        active_sensor_id = int(self._active_cue.sensor_id) if self._active_cue is not None else -1
        self._active_cue = None
        self._scan_active = False
        self._scan_reference_point = None
        # _cue_queue intentionally NOT cleared here
        self._trace(
            "active_cue_completed",
            active_sensor_id=active_sensor_id,
            queue_before=queue_before,
            queue_after=int(len(self._cue_queue)),
        )

    def cancel_active_cue(self) -> None:
        """Cancel the active cue and clear the entire queue (full stop).

        Use this when giving up (scan exhausted, no-scan mode, config
        reload, or feature disabled).  Do NOT call this on target-found
        — use complete_active_cue() instead to preserve queued events.
        """
        queue_before = int(len(self._cue_queue))
        active_sensor_id = int(self._active_cue.sensor_id) if self._active_cue is not None else -1
        self._active_cue = None
        self._scan_active = False
        self._cue_queue.clear()
        self._scan_reference_point = None
        self._trace(
            "active_cue_cancelled_and_queue_cleared",
            active_sensor_id=active_sensor_id,
            queue_before=queue_before,
            queue_after=int(len(self._cue_queue)),
        )

    def peek_queue_count(self) -> int:
        """Return number of events waiting in queue (excludes active cue)."""
        return len(self._cue_queue)

    def get_scan_reference_point(self) -> Optional[Tuple[float, float]]:
        return self._scan_reference_point
    
    def get_status_text(self) -> str:
        """Return human-readable status string for overlay/UI."""
        if not self.cfg.pir_enabled:
            return "PIR: disabled"

        if self._scan_active:
            sensor_label = ""
            if self._active_cue is not None:
                sensor_label = f" s{int(self._active_cue.sensor_id) + 1}"
            total_points = max(1, len(self._scan_points))
            current_index = min(total_points, max(1, int(self._scan_index) or 1))
            return f"PIR: scanning{sensor_label} {current_index}/{total_points}"
        
        if self._active_cue is not None:
            return f"PIR: cue s{int(self._active_cue.sensor_id) + 1} active"
        
        if len(self._cue_queue) > 0:
            return f"PIR: {len(self._cue_queue)} queued"
        
        return "PIR: idle"

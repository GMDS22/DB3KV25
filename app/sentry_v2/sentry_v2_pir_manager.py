"""
Smart Sentry v2 — PIR Sensor Manager

Manages PIR sensor state, debouncing, and cue generation for blind-spot detection.
"""

from __future__ import annotations

import time
from typing import List, Optional, Tuple

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
        
        # Debounce tracking per sensor: {sensor_id: last_fire_time}
        self._last_fire_time: dict = {}
        
        # Queue of pending cue events
        self._cue_queue: List[PIRSensorEvent] = []
        
        # Current active cue (being pursued by turret)
        self._active_cue: Optional[PIRSensorEvent] = None
        self._active_cue_start: float = 0.0
        
        # Scan state (if adaptive scan is active)
        self._scan_active: bool = False
        self._scan_points: List[Tuple[float, float]] = []  # (pan, tilt) scan grid
        self._scan_index: int = 0
        self._scan_point_visited: set = set()  # Track visited points during scan
        self._scan_reference_point: Optional[Tuple[float, float]] = None
        
    def update_config(self, config: PIRGuardConfig) -> None:
        """Hot-reload configuration."""
        self.cfg = config
        # Clear internal state on config change
        self._last_fire_time.clear()
        self._cue_queue.clear()
        self._active_cue = None
        self._scan_active = False
        self._scan_reference_point = None
        
    def on_pir_event(self, sensor_id: int, timestamp: float) -> None:
        """Called when a PIR sensor fires. Handles debouncing and queueing."""
        if not self.cfg.pir_enabled:
            return
        
        if sensor_id < 0 or sensor_id >= len(self.cfg.sensors):
            return
        
        sensor = self.cfg.sensors[sensor_id]
        if not sensor.enabled:
            return
        
        # Check debounce
        now = timestamp or time.time()
        last_fire = self._last_fire_time.get(sensor_id, 0.0)
        debounce_s = sensor.debounce_ms / 1000.0
        
        if now - last_fire < debounce_s:
            return  # Still in debounce period
        
        self._last_fire_time[sensor_id] = now
        
        # Create cue event and queue it
        event = PIRSensorEvent(
            sensor_id=sensor_id,
            cue_pan=sensor.cue_pan,
            cue_tilt=sensor.cue_tilt,
            timestamp=now,
        )
        self._cue_queue.append(event)
    
    def has_pending_cue(self) -> bool:
        """Check if there's a queued or active cue waiting to be processed."""
        return len(self._cue_queue) > 0 or self._active_cue is not None
    
    def get_next_cue(self, now: float) -> Optional[PIRSensorEvent]:
        """
        Get the next cue to process.
        Returns None if no cues available or if active cue is still being pursued.
        """
        if not self.cfg.pir_enabled:
            return None
        
        # If there's an active cue, check if it has timed out
        if self._active_cue is not None:
            if now - self._active_cue_start < self.cfg.confirmation_timeout:
                return None  # Still pursuing current cue
            else:
                self._active_cue = None  # Timeout reached, clear it
        
        # Discard stale events before popping (data_timeout_ms guard)
        timeout_s = self.cfg.data_timeout_ms / 1000.0
        while self._cue_queue:
            if now - self._cue_queue[0].timestamp > timeout_s:
                self._cue_queue.pop(0)  # too old, discard
            else:
                break

        # Try to get next from queue
        if self._cue_queue:
            cue = self._cue_queue.pop(0)
            self._active_cue = cue
            self._active_cue_start = now
            self._scan_active = False  # Reset scan state
            self._scan_index = 0
            return cue

        return None
    
    def generate_scan_grid(self, center_pan: float, center_tilt: float) -> List[Tuple[float, float]]:
        """
        Generate a scan grid centered at the cue point.
        Returns list of (pan, tilt) points to visit.
        """
        pan_range = self.cfg.scan_pan_range
        tilt_range = self.cfg.scan_tilt_range
        resolution = self.cfg.scan_grid_resolution
        
        grid = []
        
        # Generate grid points
        for i in range(resolution):
            for j in range(resolution):
                # Normalized position (-1 to 1)
                norm_pan = (i - (resolution - 1) / 2.0) / max(1, (resolution - 1) / 2.0) if resolution > 1 else 0.0
                norm_tilt = (j - (resolution - 1) / 2.0) / max(1, (resolution - 1) / 2.0) if resolution > 1 else 0.0
                
                p = center_pan + norm_pan * pan_range
                t = center_tilt + norm_tilt * tilt_range
                
                # Clamp to valid ranges
                p = max(0.0, min(270.0, p))
                t = max(0.0, min(110.0, t))
                
                grid.append((p, t))
        
        return grid
    
    def start_scan(self, center_pan: float, center_tilt: float) -> None:
        """Start an adaptive scan at the cue location."""
        self._scan_active = True
        self._scan_points = self.generate_scan_grid(center_pan, center_tilt)
        self._scan_index = 0
        self._scan_point_visited.clear()
        self._scan_reference_point = (float(center_pan), float(center_tilt))
    
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
        self._active_cue = None
        self._scan_active = False
        self._scan_reference_point = None
        # _cue_queue intentionally NOT cleared here

    def cancel_active_cue(self) -> None:
        """Cancel the active cue and clear the entire queue (full stop).

        Use this when giving up (scan exhausted, no-scan mode, config
        reload, or feature disabled).  Do NOT call this on target-found
        — use complete_active_cue() instead to preserve queued events.
        """
        self._active_cue = None
        self._scan_active = False
        self._cue_queue.clear()
        self._scan_reference_point = None

    def peek_queue_count(self) -> int:
        """Return number of events waiting in queue (excludes active cue)."""
        return len(self._cue_queue)

    def get_scan_reference_point(self) -> Optional[Tuple[float, float]]:
        return self._scan_reference_point
    
    def get_status_text(self) -> str:
        """Return human-readable status string for overlay/UI."""
        if not self.cfg.pir_enabled:
            return "PIR: disabled"
        
        if self._active_cue is not None:
            return f"PIR: cue {self._active_cue.sensor_id} active"
        
        if len(self._cue_queue) > 0:
            return f"PIR: {len(self._cue_queue)} queued"
        
        if self._scan_active:
            return f"PIR: scanning {self._scan_index}/{len(self._scan_points)}"
        
        return "PIR: idle"

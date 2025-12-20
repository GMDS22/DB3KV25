"""
Peripheral Sensor - Detects when targets enter/exit the peripheral zone.

The peripheral zone is a ring around the guard point.
This module triggers prediction sequences when targets enter the zone.
"""

import numpy as np
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional, Set
from enum import Enum
import time

# Support both relative imports (when used as package) and absolute imports (standalone)
try:
    from .sentry_config import SentryConfig
except ImportError:
    from sentry_config import SentryConfig


class ZoneType(Enum):
    """Types of zones in the sentry system."""
    OUTSIDE = "outside"           # Beyond peripheral zone
    PERIPHERAL = "peripheral"     # In the detection ring
    GUARD = "guard"              # At the guard point
    KILL = "kill"                # In the kill zone (ambush point)


@dataclass
class ZoneEvent:
    """Event when a target crosses zone boundaries."""
    track_id: int
    event_type: str           # 'enter_peripheral', 'exit_peripheral', 'enter_kill', 'exit_kill'
    from_zone: ZoneType
    to_zone: ZoneType
    position: Tuple[float, float]  # Normalized position
    velocity: Tuple[float, float]  # Velocity at crossing
    timestamp: float
    
    def __str__(self) -> str:
        return f"ZoneEvent({self.event_type}, track={self.track_id}, pos=({self.position[0]:.2f}, {self.position[1]:.2f}))"


@dataclass
class TrackedTarget:
    """State tracking for a target in the peripheral system."""
    track_id: int
    current_zone: ZoneType = ZoneType.OUTSIDE
    last_position: Tuple[float, float] = (0.0, 0.0)
    last_velocity: Tuple[float, float] = (0.0, 0.0)
    entry_time: Optional[float] = None        # When entered peripheral
    predicted_exit_time: Optional[float] = None
    matched_path_id: Optional[int] = None     # If matched to a confirmed path
    fire_authorized: bool = False             # Whether this target can be fired upon


class PeripheralSensor:
    """
    Manages the peripheral zone detection system.
    
    The peripheral zone is a ring around the guard point:
    - Inside inner radius: GUARD zone (at the watched spot)
    - Between inner and outer: PERIPHERAL zone (detection ring)
    - Outside outer radius: OUTSIDE (ignored)
    
    Kill zones are separate circles at ambush points.
    
    Responsibilities:
    - Track which zone each target is in
    - Generate events when targets cross zone boundaries
    - Trigger prediction sequences on peripheral entry
    - Coordinate with trajectory predictor for intercept timing
    """
    
    def __init__(self, config=None):
        """
        Initialize the peripheral sensor.
        
        Args:
            config: SentryConfig instance or None for defaults
        """
        self.config = config or SentryConfig()
        
        # Guard point (center of attention)
        self.guard_point: Tuple[float, float] = self.config.guard_point
        
        # Zone radii (normalized 0.0-1.0)
        self.inner_radius: float = self.config.peripheral_inner_radius
        self.outer_radius: float = self.config.peripheral_outer_radius
        self.kill_zone_radius: float = self.config.kill_zone_radius
        
        # Active kill zones (ambush points)
        self.kill_zones: List[Tuple[float, float]] = []
        
        # Tracked targets and their zone state
        self.targets: Dict[int, TrackedTarget] = {}
        
        # Event queue
        self.pending_events: List[ZoneEvent] = []
        
        # Callback for zone events
        self._event_callbacks: List[callable] = []
        
        # Statistics
        self.total_peripheral_entries: int = 0
        self.total_kill_zone_entries: int = 0
    
    def set_guard_point(self, x: float, y: float) -> None:
        """
        Set the center point being guarded.
        
        Args:
            x, y: Normalized coordinates (0.0-1.0)
        """
        self.guard_point = (x, y)
    
    def set_kill_zones(self, points: List[Tuple[float, float]]) -> None:
        """
        Set active kill zone (ambush) points.
        
        Args:
            points: List of (x, y) normalized coordinates
        """
        self.kill_zones = list(points)
    
    def add_kill_zone(self, x: float, y: float) -> None:
        """Add a kill zone at the specified point."""
        self.kill_zones.append((x, y))
    
    def clear_kill_zones(self) -> None:
        """Remove all kill zones."""
        self.kill_zones.clear()
    
    def register_event_callback(self, callback: callable) -> None:
        """
        Register a callback to be called on zone events.
        
        Callback signature: callback(event: ZoneEvent) -> None
        """
        self._event_callbacks.append(callback)
    
    def _determine_zone(self, x: float, y: float) -> Tuple[ZoneType, Optional[int]]:
        """
        Determine which zone a point is in.
        
        Args:
            x, y: Normalized coordinates
            
        Returns:
            (ZoneType, kill_zone_index or None)
        """
        # Check kill zones first (highest priority)
        for i, (kx, ky) in enumerate(self.kill_zones):
            dist = np.sqrt((x - kx)**2 + (y - ky)**2)
            if dist <= self.kill_zone_radius:
                return (ZoneType.KILL, i)
        
        # Check distance from guard point
        gx, gy = self.guard_point
        dist_to_guard = np.sqrt((x - gx)**2 + (y - gy)**2)
        
        if dist_to_guard <= self.inner_radius:
            return (ZoneType.GUARD, None)
        elif dist_to_guard <= self.outer_radius:
            return (ZoneType.PERIPHERAL, None)
        else:
            return (ZoneType.OUTSIDE, None)
    
    def update(self, detections: List[Tuple[int, float, float, float, float]],
               timestamp: Optional[float] = None) -> List[ZoneEvent]:
        """
        Update sensor with new detections.
        
        Args:
            detections: List of (track_id, x, y, vx, vy) - normalized coordinates
            timestamp: Current time, or None for current time
            
        Returns:
            List of zone crossing events
        """
        timestamp = timestamp or time.time()
        events = []
        seen_ids: Set[int] = set()
        
        for det in detections:
            track_id = det[0]
            x, y = det[1], det[2]
            vx = det[3] if len(det) > 3 else 0.0
            vy = det[4] if len(det) > 4 else 0.0
            
            seen_ids.add(track_id)
            
            # Determine current zone
            new_zone, kill_zone_idx = self._determine_zone(x, y)
            
            # Get or create target state
            if track_id not in self.targets:
                self.targets[track_id] = TrackedTarget(
                    track_id=track_id,
                    current_zone=ZoneType.OUTSIDE,
                    last_position=(x, y),
                    last_velocity=(vx, vy)
                )
            
            target = self.targets[track_id]
            old_zone = target.current_zone
            
            # Check for zone transition
            if new_zone != old_zone:
                event = self._create_zone_event(
                    track_id, old_zone, new_zone, 
                    x, y, vx, vy, timestamp
                )
                events.append(event)
                
                # Update target state
                target.current_zone = new_zone
                
                if new_zone == ZoneType.PERIPHERAL and old_zone == ZoneType.OUTSIDE:
                    target.entry_time = timestamp
                    target.fire_authorized = False  # Reset authorization
                    self.total_peripheral_entries += 1
                
                if new_zone == ZoneType.KILL:
                    self.total_kill_zone_entries += 1
                    target.fire_authorized = True  # Authorize fire
            
            # Update position/velocity
            target.last_position = (x, y)
            target.last_velocity = (vx, vy)
        
        # Clean up targets that have left
        lost_ids = set(self.targets.keys()) - seen_ids
        for track_id in lost_ids:
            target = self.targets[track_id]
            if target.current_zone != ZoneType.OUTSIDE:
                # Generate exit event
                event = self._create_zone_event(
                    track_id, target.current_zone, ZoneType.OUTSIDE,
                    target.last_position[0], target.last_position[1],
                    target.last_velocity[0], target.last_velocity[1],
                    timestamp
                )
                events.append(event)
            del self.targets[track_id]
        
        # Store and dispatch events
        self.pending_events.extend(events)
        for event in events:
            for callback in self._event_callbacks:
                try:
                    callback(event)
                except Exception as e:
                    print(f"Error in zone event callback: {e}")
        
        return events
    
    def _create_zone_event(self, track_id: int, 
                           from_zone: ZoneType, to_zone: ZoneType,
                           x: float, y: float,
                           vx: float, vy: float,
                           timestamp: float) -> ZoneEvent:
        """Create a zone crossing event."""
        # Determine event type
        if to_zone == ZoneType.PERIPHERAL and from_zone == ZoneType.OUTSIDE:
            event_type = "enter_peripheral"
        elif from_zone == ZoneType.PERIPHERAL and to_zone == ZoneType.OUTSIDE:
            event_type = "exit_peripheral"
        elif to_zone == ZoneType.KILL:
            event_type = "enter_kill"
        elif from_zone == ZoneType.KILL:
            event_type = "exit_kill"
        elif to_zone == ZoneType.GUARD:
            event_type = "enter_guard"
        elif from_zone == ZoneType.GUARD:
            event_type = "exit_guard"
        else:
            event_type = f"transition_{from_zone.value}_to_{to_zone.value}"
        
        return ZoneEvent(
            track_id=track_id,
            event_type=event_type,
            from_zone=from_zone,
            to_zone=to_zone,
            position=(x, y),
            velocity=(vx, vy),
            timestamp=timestamp
        )
    
    def get_targets_in_zone(self, zone: ZoneType) -> List[TrackedTarget]:
        """Get all targets currently in a specific zone."""
        return [t for t in self.targets.values() if t.current_zone == zone]
    
    def get_targets_in_peripheral(self) -> List[TrackedTarget]:
        """Get all targets in the peripheral zone."""
        return self.get_targets_in_zone(ZoneType.PERIPHERAL)
    
    def get_targets_in_kill_zone(self) -> List[TrackedTarget]:
        """Get all targets in any kill zone."""
        return self.get_targets_in_zone(ZoneType.KILL)
    
    def is_target_authorized_to_fire(self, track_id: int) -> bool:
        """Check if a target is authorized for firing."""
        if track_id not in self.targets:
            return False
        return self.targets[track_id].fire_authorized
    
    def authorize_fire(self, track_id: int) -> bool:
        """Manually authorize firing on a target."""
        if track_id not in self.targets:
            return False
        self.targets[track_id].fire_authorized = True
        return True
    
    def revoke_fire_authorization(self, track_id: int) -> bool:
        """Revoke fire authorization for a target."""
        if track_id not in self.targets:
            return False
        self.targets[track_id].fire_authorized = False
        return True
    
    def get_zone_geometry(self) -> dict:
        """
        Get zone geometry for visualization.
        
        Returns:
            Dictionary with all zone definitions
        """
        return {
            'guard_point': self.guard_point,
            'inner_radius': self.inner_radius,
            'outer_radius': self.outer_radius,
            'kill_zone_radius': self.kill_zone_radius,
            'kill_zones': list(self.kill_zones)
        }
    
    def pop_events(self) -> List[ZoneEvent]:
        """Get and clear all pending events."""
        events = list(self.pending_events)
        self.pending_events.clear()
        return events
    
    def clear_all(self) -> None:
        """Clear all tracking state."""
        self.targets.clear()
        self.pending_events.clear()
        self.kill_zones.clear()
    
    def get_stats(self) -> dict:
        """Get sensor statistics."""
        return {
            'tracked_targets': len(self.targets),
            'targets_in_peripheral': len(self.get_targets_in_peripheral()),
            'targets_in_kill_zone': len(self.get_targets_in_kill_zone()),
            'kill_zones_active': len(self.kill_zones),
            'total_peripheral_entries': self.total_peripheral_entries,
            'total_kill_zone_entries': self.total_kill_zone_entries,
            'pending_events': len(self.pending_events)
        }

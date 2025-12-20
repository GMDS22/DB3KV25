"""
Track Recorder - Records and stores trajectory history for detected targets.

Stores position history with timestamps for each tracked object ID.
Handles track lifecycle: creation, update, expiration, and persistence.
"""

import time
import json
import numpy as np
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Tuple, Optional
from pathlib import Path
from collections import deque

# Support both relative imports (when used as package) and absolute imports (standalone)
try:
    from .sentry_config import SentryConfig
except ImportError:
    from sentry_config import SentryConfig


@dataclass
class TrackPoint:
    """Single point in a trajectory."""
    x: float                    # Normalized X position (0.0-1.0)
    y: float                    # Normalized Y position (0.0-1.0)
    timestamp: float            # Unix timestamp
    velocity_x: float = 0.0     # Velocity in X direction (normalized/second)
    velocity_y: float = 0.0     # Velocity in Y direction (normalized/second)
    speed: float = 0.0          # Magnitude of velocity
    bbox: Tuple[int, int, int, int] = (0, 0, 0, 0)  # Original bounding box (x, y, w, h)
    
    def to_dict(self) -> dict:
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: dict) -> 'TrackPoint':
        if 'bbox' in data and isinstance(data['bbox'], list):
            data['bbox'] = tuple(data['bbox'])
        return cls(**data)


@dataclass 
class Track:
    """Complete trajectory for a single object."""
    track_id: int                           # Unique identifier from ByteTrack
    points: List[TrackPoint] = field(default_factory=list)
    created_at: float = field(default_factory=time.time)
    last_updated: float = field(default_factory=time.time)
    is_active: bool = True                  # Currently being tracked
    is_complete: bool = False               # Target exited frame/peripheral
    pass_count: int = 0                     # Times this pattern was observed
    entry_direction: Optional[str] = None   # 'left', 'right', 'top', 'bottom'
    exit_direction: Optional[str] = None    # Where target exited
    average_speed: float = 0.0              # Average speed over track
    
    def add_point(self, point: TrackPoint) -> None:
        """Add a point to the trajectory."""
        self.points.append(point)
        self.last_updated = point.timestamp
        
        # Update average speed (running average)
        if len(self.points) > 1:
            speeds = [p.speed for p in self.points if p.speed > 0]
            if speeds:
                self.average_speed = sum(speeds) / len(speeds)
    
    def get_positions(self) -> np.ndarray:
        """Get all positions as numpy array [[x, y], ...]."""
        return np.array([[p.x, p.y] for p in self.points])
    
    def get_last_n_points(self, n: int) -> List[TrackPoint]:
        """Get last N points for prediction."""
        return self.points[-n:] if len(self.points) >= n else self.points
    
    def get_duration(self) -> float:
        """Get track duration in seconds."""
        if len(self.points) < 2:
            return 0.0
        return self.points[-1].timestamp - self.points[0].timestamp
    
    def get_total_distance(self) -> float:
        """Get total distance traveled (normalized units)."""
        if len(self.points) < 2:
            return 0.0
        total = 0.0
        for i in range(1, len(self.points)):
            dx = self.points[i].x - self.points[i-1].x
            dy = self.points[i].y - self.points[i-1].y
            total += np.sqrt(dx*dx + dy*dy)
        return total
    
    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            'track_id': self.track_id,
            'points': [p.to_dict() for p in self.points],
            'created_at': self.created_at,
            'last_updated': self.last_updated,
            'is_active': self.is_active,
            'is_complete': self.is_complete,
            'pass_count': self.pass_count,
            'entry_direction': self.entry_direction,
            'exit_direction': self.exit_direction,
            'average_speed': self.average_speed
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Track':
        """Create from dictionary."""
        points = [TrackPoint.from_dict(p) for p in data.pop('points', [])]
        track = cls(**data)
        track.points = points
        return track


class TrackRecorder:
    """
    Records and manages trajectory history for all tracked objects.
    
    Responsibilities:
    - Create new tracks when new objects are detected
    - Update tracks with new positions and velocities
    - Mark tracks as complete when objects exit
    - Expire old tracks based on time threshold
    - Persist tracks to JSON for session continuity
    """
    
    def __init__(self, config=None):
        """
        Initialize the track recorder.
        
        Args:
            config: SentryConfig instance or None for defaults
        """
        self.config = config or SentryConfig()
        
        # Active tracks (currently being tracked)
        self.active_tracks: Dict[int, Track] = {}
        
        # Completed tracks (target exited, ready for analysis)
        self.completed_tracks: List[Track] = []
        
        # All historical tracks (for pattern matching)
        self.track_history: deque = deque(maxlen=self.config.max_stored_tracks)
        
        # Frame dimensions (set on first update)
        self.frame_width: int = 640
        self.frame_height: int = 480
        
        # Velocity smoothing state
        self._prev_positions: Dict[int, Tuple[float, float, float]] = {}  # track_id: (x, y, timestamp)
    
    def set_frame_dimensions(self, width: int, height: int) -> None:
        """Set frame dimensions for normalization."""
        self.frame_width = width
        self.frame_height = height
    
    def update(self, detections: List[Tuple[int, int, int, int, int]], 
               timestamp: Optional[float] = None) -> List[Track]:
        """
        Update tracks with new detections from ByteTrack.
        
        Args:
            detections: List of (track_id, x, y, w, h) tuples from tracker
            timestamp: Current timestamp, or None to use current time
            
        Returns:
            List of currently active Track objects
        """
        timestamp = timestamp or time.time()
        seen_ids = set()
        
        for det in detections:
            track_id, x, y, w, h = det[:5]
            seen_ids.add(track_id)
            
            # Normalize position to 0.0-1.0 range
            center_x = (x + w/2) / self.frame_width
            center_y = (y + h/2) / self.frame_height
            
            # Calculate velocity
            velocity_x, velocity_y, speed = self._calculate_velocity(
                track_id, center_x, center_y, timestamp
            )
            
            # Create track point
            point = TrackPoint(
                x=center_x,
                y=center_y,
                timestamp=timestamp,
                velocity_x=velocity_x,
                velocity_y=velocity_y,
                speed=speed,
                bbox=(x, y, w, h)
            )
            
            # Update or create track
            if track_id in self.active_tracks:
                self.active_tracks[track_id].add_point(point)
            else:
                # New track
                track = Track(track_id=track_id)
                track.entry_direction = self._determine_entry_direction(center_x, center_y)
                track.add_point(point)
                self.active_tracks[track_id] = track
        
        # Mark tracks that weren't seen as potentially complete
        lost_ids = set(self.active_tracks.keys()) - seen_ids
        for track_id in lost_ids:
            track = self.active_tracks[track_id]
            # If track hasn't been updated for a short while, mark as complete
            if timestamp - track.last_updated > 0.5:  # 500ms grace period
                self._complete_track(track_id, timestamp)
        
        # Expire old tracks from history
        self._expire_old_tracks(timestamp)
        
        return list(self.active_tracks.values())
    
    def _calculate_velocity(self, track_id: int, x: float, y: float, 
                           timestamp: float) -> Tuple[float, float, float]:
        """Calculate velocity for a track point using EMA smoothing."""
        if track_id in self._prev_positions:
            prev_x, prev_y, prev_t = self._prev_positions[track_id]
            dt = timestamp - prev_t
            
            if dt > 0.001:  # Avoid division by zero
                raw_vx = (x - prev_x) / dt
                raw_vy = (y - prev_y) / dt
                raw_speed = np.sqrt(raw_vx**2 + raw_vy**2)
                
                # Apply EMA smoothing
                alpha = self.config.velocity_smoothing
                if track_id in self.active_tracks and self.active_tracks[track_id].points:
                    last_point = self.active_tracks[track_id].points[-1]
                    vx = alpha * raw_vx + (1 - alpha) * last_point.velocity_x
                    vy = alpha * raw_vy + (1 - alpha) * last_point.velocity_y
                    speed = np.sqrt(vx**2 + vy**2)
                else:
                    vx, vy, speed = raw_vx, raw_vy, raw_speed
            else:
                vx, vy, speed = 0.0, 0.0, 0.0
        else:
            vx, vy, speed = 0.0, 0.0, 0.0
        
        # Update previous position
        self._prev_positions[track_id] = (x, y, timestamp)
        
        return vx, vy, speed
    
    def _determine_entry_direction(self, x: float, y: float) -> str:
        """Determine which edge the target entered from."""
        # Check proximity to edges
        left_dist = x
        right_dist = 1.0 - x
        top_dist = y
        bottom_dist = 1.0 - y
        
        min_dist = min(left_dist, right_dist, top_dist, bottom_dist)
        
        if min_dist == left_dist:
            return 'left'
        elif min_dist == right_dist:
            return 'right'
        elif min_dist == top_dist:
            return 'top'
        else:
            return 'bottom'
    
    def _complete_track(self, track_id: int, timestamp: float) -> None:
        """Mark a track as complete and move to completed list."""
        if track_id not in self.active_tracks:
            return
            
        track = self.active_tracks.pop(track_id)
        track.is_active = False
        track.is_complete = True
        
        # Determine exit direction from last position
        if track.points:
            last_point = track.points[-1]
            track.exit_direction = self._determine_entry_direction(last_point.x, last_point.y)
        
        # Only keep tracks with sufficient length
        if len(track.points) >= self.config.min_track_length:
            self.completed_tracks.append(track)
            self.track_history.append(track)
        
        # Clean up velocity state
        if track_id in self._prev_positions:
            del self._prev_positions[track_id]
    
    def _expire_old_tracks(self, current_time: float) -> None:
        """Remove tracks that are too old from history."""
        expiry_threshold = current_time - self.config.track_expiry_seconds
        
        # Remove from completed tracks
        self.completed_tracks = [
            t for t in self.completed_tracks 
            if t.last_updated > expiry_threshold
        ]
    
    def get_recent_completed_tracks(self, 
                                     time_window: Optional[float] = None) -> List[Track]:
        """
        Get completed tracks within a time window.
        
        Args:
            time_window: Seconds to look back, or None for config default
            
        Returns:
            List of completed Track objects
        """
        time_window = time_window or self.config.track_similarity_time_window
        cutoff = time.time() - time_window
        return [t for t in self.completed_tracks if t.last_updated > cutoff]
    
    def get_all_tracks_for_analysis(self) -> List[Track]:
        """Get all tracks (active + completed) for pattern analysis."""
        all_tracks = list(self.completed_tracks)
        all_tracks.extend(self.active_tracks.values())
        return all_tracks
    
    def clear_completed_tracks(self) -> None:
        """Clear all completed tracks (after analysis)."""
        self.completed_tracks.clear()
    
    def force_complete_all(self) -> List[Track]:
        """Force-complete all active tracks (e.g., on mode switch)."""
        timestamp = time.time()
        completed = []
        for track_id in list(self.active_tracks.keys()):
            self._complete_track(track_id, timestamp)
            if self.completed_tracks:
                completed.append(self.completed_tracks[-1])
        return completed
    
    def save_to_file(self, path: Optional[str] = None) -> None:
        """Save track history to JSON file."""
        save_path = Path(path) if path else Path(__file__).parent / self.config.tracks_save_path
        save_path.parent.mkdir(parents=True, exist_ok=True)
        
        data = {
            'saved_at': time.time(),
            'tracks': [t.to_dict() for t in self.track_history]
        }
        
        with open(save_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_from_file(self, path: Optional[str] = None) -> int:
        """
        Load track history from JSON file.
        
        Returns:
            Number of tracks loaded
        """
        load_path = Path(path) if path else Path(__file__).parent / self.config.tracks_save_path
        
        if not load_path.exists():
            return 0
        
        try:
            with open(load_path, 'r') as f:
                data = json.load(f)
            
            tracks = [Track.from_dict(t) for t in data.get('tracks', [])]
            self.track_history.clear()
            self.track_history.extend(tracks)
            
            return len(tracks)
        except Exception as e:
            print(f"Error loading tracks: {e}")
            return 0
    
    def get_stats(self) -> dict:
        """Get statistics about recorded tracks."""
        return {
            'active_tracks': len(self.active_tracks),
            'completed_tracks': len(self.completed_tracks),
            'history_size': len(self.track_history),
            'total_points': sum(len(t.points) for t in self.active_tracks.values())
        }

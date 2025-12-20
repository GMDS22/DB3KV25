"""
Path Analyzer - Clusters trajectories and identifies repeating movement patterns.

Uses spatial similarity (Fréchet distance) to group similar paths.
Identifies "confirmed" tracks after multiple passes on same pattern.
Determines optimal ambush points along confirmed tracks.
"""

import numpy as np
from dataclasses import dataclass, field
from typing import List, Tuple, Optional, Dict
from collections import defaultdict
import time

# Support both relative imports (when used as package) and absolute imports (standalone)
try:
    from .track_recorder import Track, TrackPoint
    from .sentry_config import SentryConfig
except ImportError:
    from track_recorder import Track, TrackPoint
    from sentry_config import SentryConfig


@dataclass
class ConfirmedPath:
    """A confirmed movement pattern with multiple observations."""
    path_id: int                                # Unique identifier
    representative_track: Track                 # Best example of this path
    matched_tracks: List[Track] = field(default_factory=list)  # All tracks matching this pattern
    pass_count: int = 1                         # Number of times observed
    first_seen: float = field(default_factory=time.time)
    last_seen: float = field(default_factory=time.time)
    ambush_point: Optional[Tuple[float, float]] = None  # Optimal point to aim
    ambush_point_idx: int = 0                   # Index in representative track
    average_speed_at_ambush: float = 0.0        # Expected speed at ambush point
    average_time_to_ambush: float = 0.0         # Expected time from entry to ambush
    confidence: float = 0.0                     # How confident we are in this path (0.0-1.0)
    entry_direction: Optional[str] = None       # Typical entry direction
    
    def update_confidence(self) -> None:
        """Update confidence based on observations."""
        # More passes = higher confidence (diminishing returns)
        pass_factor = min(1.0, self.pass_count / 5.0)
        
        # Recency factor
        age = time.time() - self.last_seen
        recency_factor = max(0.0, 1.0 - age / 300.0)  # Decays over 5 minutes
        
        # Speed consistency factor
        if len(self.matched_tracks) >= 2:
            speeds = [t.average_speed for t in self.matched_tracks if t.average_speed > 0]
            if speeds:
                mean_speed = np.mean(speeds)
                std_speed = np.std(speeds)
                if mean_speed > 0:
                    consistency_factor = max(0.0, 1.0 - std_speed / mean_speed)
                else:
                    consistency_factor = 0.5
            else:
                consistency_factor = 0.5
        else:
            consistency_factor = 0.5
        
        self.confidence = 0.4 * pass_factor + 0.3 * recency_factor + 0.3 * consistency_factor


class PathAnalyzer:
    """
    Analyzes recorded tracks to find repeating movement patterns.
    
    Responsibilities:
    - Compare track similarity using Fréchet distance
    - Cluster similar tracks together
    - Identify confirmed paths (2+ passes)
    - Calculate optimal ambush points
    - Rank paths by priority for multi-track ambush
    """
    
    def __init__(self, config=None):
        """
        Initialize the path analyzer.
        
        Args:
            config: SentryConfig instance or None for defaults
        """
        self.config = config or SentryConfig()
        
        # Confirmed paths that have been observed multiple times
        self.confirmed_paths: List[ConfirmedPath] = []
        
        # Pending tracks waiting for pattern match
        self.pending_tracks: List[Track] = []
        
        # Path ID counter
        self._next_path_id: int = 1
        
        # Manual ambush points set by user
        self.manual_ambush_points: List[Tuple[float, float]] = []
    
    def analyze_track(self, track: Track) -> Optional[ConfirmedPath]:
        """
        Analyze a completed track for pattern matching.
        
        Args:
            track: Completed Track object to analyze
            
        Returns:
            ConfirmedPath if track matched/created a confirmed pattern, None otherwise
        """
        if len(track.points) < self.config.min_track_length:
            return None
        
        # Check against existing confirmed paths
        for confirmed in self.confirmed_paths:
            similarity = self._compute_path_similarity(track, confirmed.representative_track)
            
            if similarity >= (1.0 - self.config.path_similarity_threshold):
                # Match found - update confirmed path
                confirmed.matched_tracks.append(track)
                confirmed.pass_count += 1
                confirmed.last_seen = time.time()
                confirmed.update_confidence()
                
                # Recalculate ambush point with new data
                self._update_ambush_point(confirmed)
                
                return confirmed
        
        # Check against pending tracks
        for pending in self.pending_tracks:
            similarity = self._compute_path_similarity(track, pending)
            
            if similarity >= (1.0 - self.config.path_similarity_threshold):
                # Second observation - promote to confirmed
                confirmed = self._create_confirmed_path(pending, track)
                self.pending_tracks.remove(pending)
                return confirmed
        
        # No match - add to pending
        self.pending_tracks.append(track)
        
        # Limit pending tracks
        while len(self.pending_tracks) > self.config.max_stored_tracks:
            self.pending_tracks.pop(0)
        
        return None
    
    def _compute_path_similarity(self, track1: Track, track2: Track) -> float:
        """
        Compute similarity between two tracks using discrete Fréchet distance.
        
        Returns:
            Similarity score 0.0-1.0 (1.0 = identical paths)
        """
        points1 = track1.get_positions()
        points2 = track2.get_positions()
        
        if len(points1) < 2 or len(points2) < 2:
            return 0.0
        
        # Resample to same number of points for fair comparison
        n_samples = 20
        points1_resampled = self._resample_path(points1, n_samples)
        points2_resampled = self._resample_path(points2, n_samples)
        
        # Compute discrete Fréchet distance
        frechet_dist = self._frechet_distance(points1_resampled, points2_resampled)
        
        # Normalize to 0-1 similarity (max possible distance is sqrt(2) for normalized coords)
        max_dist = np.sqrt(2)
        similarity = max(0.0, 1.0 - frechet_dist / max_dist)
        
        # Also check direction consistency
        dir1 = points1[-1] - points1[0]
        dir2 = points2[-1] - points2[0]
        
        # Cosine similarity of overall direction
        norm1 = np.linalg.norm(dir1)
        norm2 = np.linalg.norm(dir2)
        
        if norm1 > 0.01 and norm2 > 0.01:
            dir_similarity = np.dot(dir1, dir2) / (norm1 * norm2)
            dir_similarity = (dir_similarity + 1.0) / 2.0  # Map from [-1,1] to [0,1]
        else:
            dir_similarity = 0.5
        
        # Combined similarity (70% path, 30% direction)
        return 0.7 * similarity + 0.3 * dir_similarity
    
    def _resample_path(self, points: np.ndarray, n_samples: int) -> np.ndarray:
        """Resample path to fixed number of evenly spaced points."""
        if len(points) == n_samples:
            return points
        
        # Calculate cumulative distance along path
        distances = np.zeros(len(points))
        for i in range(1, len(points)):
            distances[i] = distances[i-1] + np.linalg.norm(points[i] - points[i-1])
        
        total_dist = distances[-1]
        if total_dist < 0.001:
            return np.tile(points[0], (n_samples, 1))
        
        # Sample at evenly spaced distances
        sample_distances = np.linspace(0, total_dist, n_samples)
        resampled = np.zeros((n_samples, 2))
        
        for i, d in enumerate(sample_distances):
            # Find segment containing this distance
            idx = np.searchsorted(distances, d)
            if idx == 0:
                resampled[i] = points[0]
            elif idx >= len(points):
                resampled[i] = points[-1]
            else:
                # Interpolate between points
                t = (d - distances[idx-1]) / (distances[idx] - distances[idx-1])
                resampled[i] = points[idx-1] + t * (points[idx] - points[idx-1])
        
        return resampled
    
    def _frechet_distance(self, P: np.ndarray, Q: np.ndarray) -> float:
        """Compute discrete Fréchet distance between two paths."""
        n, m = len(P), len(Q)
        
        # Dynamic programming table
        ca = np.full((n, m), -1.0)
        
        def _c(i: int, j: int) -> float:
            if ca[i, j] > -0.5:
                return ca[i, j]
            
            d = np.linalg.norm(P[i] - Q[j])
            
            if i == 0 and j == 0:
                ca[i, j] = d
            elif i > 0 and j == 0:
                ca[i, j] = max(_c(i-1, 0), d)
            elif i == 0 and j > 0:
                ca[i, j] = max(_c(0, j-1), d)
            else:
                ca[i, j] = max(min(_c(i-1, j), _c(i-1, j-1), _c(i, j-1)), d)
            
            return ca[i, j]
        
        return _c(n-1, m-1)
    
    def _create_confirmed_path(self, track1: Track, track2: Track) -> ConfirmedPath:
        """Create a new confirmed path from two matching tracks."""
        # Use the longer/more complete track as representative
        if len(track1.points) >= len(track2.points):
            representative = track1
        else:
            representative = track2
        
        confirmed = ConfirmedPath(
            path_id=self._next_path_id,
            representative_track=representative,
            matched_tracks=[track1, track2],
            pass_count=2,
            first_seen=min(track1.created_at, track2.created_at),
            last_seen=time.time(),
            entry_direction=representative.entry_direction
        )
        self._next_path_id += 1
        
        # Calculate initial ambush point
        self._update_ambush_point(confirmed)
        confirmed.update_confidence()
        
        self.confirmed_paths.append(confirmed)
        
        # Limit confirmed paths
        self._prune_confirmed_paths()
        
        return confirmed
    
    def _update_ambush_point(self, confirmed: ConfirmedPath) -> None:
        """Calculate optimal ambush point for a confirmed path."""
        track = confirmed.representative_track
        points = track.points
        
        if len(points) < 3:
            return
        
        # Find point with best combination of:
        # 1. Distance from edges (more centered = better)
        # 2. Consistent speed (less acceleration = more predictable)
        # 3. Not too early or late in track
        
        best_score = -1.0
        best_idx = len(points) // 2  # Default to middle
        
        for i in range(len(points) // 4, 3 * len(points) // 4):
            point = points[i]
            
            # Edge distance score (prefer center of frame)
            edge_dist = min(point.x, 1.0 - point.x, point.y, 1.0 - point.y)
            edge_score = edge_dist * 4  # Max score 1.0 at center
            
            # Speed consistency score
            if i > 0 and i < len(points) - 1:
                speed_diff = abs(points[i].speed - points[i-1].speed)
                if points[i].speed > 0:
                    accel_factor = speed_diff / points[i].speed
                else:
                    accel_factor = 0
                speed_score = max(0.0, 1.0 - accel_factor * 2)
            else:
                speed_score = 0.5
            
            # Position in track score (prefer middle portions)
            progress = i / len(points)
            position_score = 1.0 - abs(progress - 0.5) * 2
            
            # Combined score
            score = 0.3 * edge_score + 0.4 * speed_score + 0.3 * position_score
            
            if score > best_score:
                best_score = score
                best_idx = i
        
        # Set ambush point
        ambush_point = points[best_idx]
        confirmed.ambush_point = (ambush_point.x, ambush_point.y)
        confirmed.ambush_point_idx = best_idx
        
        # Calculate average speed at ambush point
        speeds = []
        for track in confirmed.matched_tracks:
            if len(track.points) > best_idx:
                speeds.append(track.points[best_idx].speed)
        if speeds:
            confirmed.average_speed_at_ambush = np.mean(speeds)
        
        # Calculate average time from entry to ambush
        times = []
        for track in confirmed.matched_tracks:
            if len(track.points) > best_idx and len(track.points) > 0:
                time_to_ambush = track.points[best_idx].timestamp - track.points[0].timestamp
                times.append(time_to_ambush)
        if times:
            confirmed.average_time_to_ambush = np.mean(times)
    
    def _prune_confirmed_paths(self) -> None:
        """Remove low-priority paths if we exceed max_ambush_points."""
        if len(self.confirmed_paths) <= self.config.max_ambush_points:
            return
        
        # Sort by priority
        method = self.config.ambush_priority_method
        
        if method == 'frequency':
            key = lambda p: p.pass_count
        elif method == 'recency':
            key = lambda p: p.last_seen
        elif method == 'speed':
            key = lambda p: p.average_speed_at_ambush
        elif method == 'confidence':
            key = lambda p: p.confidence
        else:
            key = lambda p: p.pass_count
        
        self.confirmed_paths.sort(key=key, reverse=True)
        self.confirmed_paths = self.confirmed_paths[:self.config.max_ambush_points]
    
    def add_manual_ambush_point(self, x: float, y: float) -> None:
        """
        Add a manually specified ambush point.
        
        Args:
            x, y: Normalized coordinates (0.0-1.0)
        """
        if not self.config.manual_ambush_enabled:
            return
        
        self.manual_ambush_points.append((x, y))
        
        # Limit manual points
        while len(self.manual_ambush_points) > self.config.max_ambush_points:
            self.manual_ambush_points.pop(0)
    
    def clear_manual_ambush_points(self) -> None:
        """Clear all manual ambush points."""
        self.manual_ambush_points.clear()
    
    def get_all_ambush_points(self) -> List[Tuple[float, float, float]]:
        """
        Get all ambush points (manual + confirmed) with confidence.
        
        Returns:
            List of (x, y, confidence) tuples
        """
        points = []
        
        # Manual points have max confidence
        for x, y in self.manual_ambush_points:
            points.append((x, y, 1.0))
        
        # Confirmed path ambush points
        for confirmed in self.confirmed_paths:
            if confirmed.ambush_point:
                x, y = confirmed.ambush_point
                points.append((x, y, confirmed.confidence))
        
        return points
    
    def get_best_ambush_point(self) -> Optional[Tuple[float, float, float]]:
        """
        Get the highest priority ambush point.
        
        Returns:
            (x, y, confidence) tuple or None if no ambush points
        """
        points = self.get_all_ambush_points()
        if not points:
            return None
        
        # Sort by confidence
        points.sort(key=lambda p: p[2], reverse=True)
        return points[0]
    
    def get_confirmed_path_for_point(self, x: float, y: float, 
                                      threshold: float = 0.1) -> Optional[ConfirmedPath]:
        """
        Find the confirmed path that a point belongs to.
        
        Args:
            x, y: Normalized coordinates
            threshold: Distance threshold for matching
            
        Returns:
            ConfirmedPath if found, None otherwise
        """
        for confirmed in self.confirmed_paths:
            if confirmed.ambush_point:
                ax, ay = confirmed.ambush_point
                dist = np.sqrt((x - ax)**2 + (y - ay)**2)
                if dist < threshold:
                    return confirmed
        return None
    
    def expire_old_paths(self, max_age: Optional[float] = None) -> int:
        """
        Remove paths that haven't been seen recently.
        
        Args:
            max_age: Maximum age in seconds, or None for config default
            
        Returns:
            Number of paths removed
        """
        max_age = max_age or self.config.track_expiry_seconds
        cutoff = time.time() - max_age
        
        original_count = len(self.confirmed_paths)
        self.confirmed_paths = [p for p in self.confirmed_paths if p.last_seen > cutoff]
        
        # Also clean pending tracks
        self.pending_tracks = [t for t in self.pending_tracks if t.last_updated > cutoff]
        
        return original_count - len(self.confirmed_paths)
    
    def get_stats(self) -> dict:
        """Get analyzer statistics."""
        return {
            'confirmed_paths': len(self.confirmed_paths),
            'pending_tracks': len(self.pending_tracks),
            'manual_ambush_points': len(self.manual_ambush_points),
            'total_observations': sum(p.pass_count for p in self.confirmed_paths),
            'average_confidence': np.mean([p.confidence for p in self.confirmed_paths]) if self.confirmed_paths else 0.0
        }

"""
Sentry Overlay - HUD visualization for Sentry Ambush Mode.

Draws all visual elements on the video frame:
- Peripheral zone boundaries
- Confirmed tracks as colored lines
- Ambush points with crosshairs
- Prediction vectors and countdown
- Status information and debug data
"""

import cv2
import numpy as np
from typing import List, Tuple, Optional, Dict
import time

# Support both relative imports (when used as package) and absolute imports (standalone)
try:
    from .track_recorder import Track
    from .path_analyzer import ConfirmedPath
    from .trajectory_predictor import PredictionResult
    from .peripheral_sensor import ZoneType, TrackedTarget
    from .sentry_config import SentryConfig
except ImportError:
    from track_recorder import Track
    from path_analyzer import ConfirmedPath
    from trajectory_predictor import PredictionResult
    from peripheral_sensor import ZoneType, TrackedTarget
    from sentry_config import SentryConfig


class SentryOverlay:
    """
    Renders all Sentry Mode visualizations on the video frame.
    
    Responsibilities:
    - Draw peripheral zone (inner/outer circles)
    - Draw confirmed tracks as colored paths
    - Draw learning tracks in different color
    - Mark ambush points with crosshairs
    - Show prediction vectors
    - Display countdown to fire
    - Show confidence meters
    - Render debug information
    """
    
    def __init__(self, config=None):
        """
        Initialize the overlay renderer.
        
        Args:
            config: SentryConfig instance or None for defaults
        """
        self.config = config or SentryConfig()
        
        # Frame dimensions (set on first render)
        self.frame_width: int = 640
        self.frame_height: int = 480
        
        # Animation state
        self.pulse_phase: float = 0.0
        self.last_render_time: float = time.time()
        
        # Fire countdown state
        self.fire_countdown: Optional[float] = None
        self.fire_countdown_start: Optional[float] = None
    
    def set_frame_dimensions(self, width: int, height: int) -> None:
        """Set frame dimensions for coordinate conversion."""
        self.frame_width = width
        self.frame_height = height
    
    def _norm_to_pixel(self, x: float, y: float) -> Tuple[int, int]:
        """Convert normalized coordinates to pixel coordinates."""
        px = int(x * self.frame_width)
        py = int(y * self.frame_height)
        return (px, py)
    
    def _norm_radius_to_pixels(self, r: float) -> int:
        """Convert normalized radius to pixel radius."""
        # Use average of width/height for consistent circles
        avg_dim = (self.frame_width + self.frame_height) / 2
        return int(r * avg_dim)
    
    def render(self, frame: np.ndarray,
               guard_point: Tuple[float, float],
               inner_radius: float,
               outer_radius: float,
               confirmed_paths: List[ConfirmedPath] = None,
               pending_tracks: List[Track] = None,
               active_tracks: List[Track] = None,
               kill_zones: List[Tuple[float, float]] = None,
               predictions: Dict[int, PredictionResult] = None,
               tracked_targets: Dict[int, TrackedTarget] = None,
               state_name: str = "UNKNOWN",
               stats: dict = None) -> np.ndarray:
        """
        Render all sentry mode overlays on frame.
        
        Args:
            frame: OpenCV frame to draw on (modified in place)
            guard_point: (x, y) normalized guard point
            inner_radius: Inner peripheral radius (normalized)
            outer_radius: Outer peripheral radius (normalized)
            confirmed_paths: List of confirmed movement patterns
            pending_tracks: Tracks waiting for pattern match
            active_tracks: Currently active tracks
            kill_zones: List of (x, y) ambush points
            predictions: Dict of track_id -> PredictionResult
            tracked_targets: Dict of track_id -> TrackedTarget
            state_name: Current state machine state
            stats: Statistics dictionary for debug display
            
        Returns:
            Frame with overlays drawn
        """
        # Update dimensions from frame
        self.frame_height, self.frame_width = frame.shape[:2]
        
        # Update animation
        current_time = time.time()
        dt = current_time - self.last_render_time
        self.last_render_time = current_time
        self.pulse_phase = (self.pulse_phase + dt * 2) % (2 * np.pi)
        
        # Draw layers from back to front
        self._draw_peripheral_zone(frame, guard_point, inner_radius, outer_radius)
        
        if pending_tracks:
            self._draw_learning_tracks(frame, pending_tracks)
        
        if confirmed_paths:
            self._draw_confirmed_paths(frame, confirmed_paths)
        
        if kill_zones:
            self._draw_kill_zones(frame, kill_zones)
        
        if active_tracks:
            self._draw_active_tracks(frame, active_tracks)
        
        if predictions and self.config.show_prediction_path:
            self._draw_predictions(frame, predictions)
        
        if tracked_targets and self.config.show_velocity_vectors:
            self._draw_velocity_vectors(frame, tracked_targets)
        
        # Draw HUD elements
        self._draw_state_indicator(frame, state_name)
        
        if self.config.show_confidence_meter and confirmed_paths:
            self._draw_confidence_meter(frame, confirmed_paths)
        
        if self.config.show_debug_overlay and stats:
            self._draw_debug_info(frame, stats)
        
        # Draw fire countdown if active
        if self.fire_countdown is not None:
            self._draw_fire_countdown(frame)
        
        return frame
    
    def _draw_peripheral_zone(self, frame: np.ndarray,
                               guard_point: Tuple[float, float],
                               inner_radius: float,
                               outer_radius: float) -> None:
        """Draw the peripheral zone rings."""
        center = self._norm_to_pixel(*guard_point)
        inner_r = self._norm_radius_to_pixels(inner_radius)
        outer_r = self._norm_radius_to_pixels(outer_radius)
        
        color = self.config.color_peripheral_zone
        thickness = self.config.zone_line_thickness
        
        # Pulsing effect for outer ring
        pulse = int(20 * np.sin(self.pulse_phase))
        pulse_color = tuple(min(255, c + pulse) for c in color)
        
        # Outer ring (peripheral boundary)
        cv2.circle(frame, center, outer_r, pulse_color, thickness)
        
        # Inner ring (guard zone boundary)
        cv2.circle(frame, center, inner_r, color, thickness)
        
        # Guard point crosshair
        cross_size = 10
        cv2.line(frame, 
                 (center[0] - cross_size, center[1]),
                 (center[0] + cross_size, center[1]),
                 color, 1)
        cv2.line(frame,
                 (center[0], center[1] - cross_size),
                 (center[0], center[1] + cross_size),
                 color, 1)
        
        # Label
        cv2.putText(frame, "GUARD ZONE", 
                    (center[0] - 40, center[1] - inner_r - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)
    
    def _draw_learning_tracks(self, frame: np.ndarray, 
                               tracks: List[Track]) -> None:
        """Draw tracks that are still in learning phase."""
        color = self.config.color_learning_track
        thickness = 1
        
        for track in tracks:
            if len(track.points) < 2:
                continue
            
            # Draw track as dashed line
            points = [self._norm_to_pixel(p.x, p.y) for p in track.points]
            
            for i in range(0, len(points) - 1, 2):
                if i + 1 < len(points):
                    cv2.line(frame, points[i], points[i + 1], color, thickness)
    
    def _draw_confirmed_paths(self, frame: np.ndarray,
                               paths: List[ConfirmedPath]) -> None:
        """Draw confirmed movement patterns."""
        color = self.config.color_confirmed_track
        thickness = self.config.track_line_thickness
        
        for path in paths:
            track = path.representative_track
            if len(track.points) < 2:
                continue
            
            # Draw track as solid line with gradient intensity
            points = [self._norm_to_pixel(p.x, p.y) for p in track.points]
            
            for i in range(len(points) - 1):
                # Fade color based on position
                alpha = i / len(points)
                faded_color = tuple(int(c * (0.5 + 0.5 * alpha)) for c in color)
                cv2.line(frame, points[i], points[i + 1], faded_color, thickness)
            
            # Draw pass count label
            if path.ambush_point:
                ambush_px = self._norm_to_pixel(*path.ambush_point)
                label = f"x{path.pass_count}"
                cv2.putText(frame, label,
                            (ambush_px[0] + 15, ambush_px[1] - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)
    
    def _draw_kill_zones(self, frame: np.ndarray,
                          kill_zones: List[Tuple[float, float]]) -> None:
        """Draw kill zones (ambush points) with crosshairs."""
        color = self.config.color_ambush_point
        kill_color = self.config.color_kill_zone
        radius = self._norm_radius_to_pixels(self.config.kill_zone_radius)
        
        for i, (x, y) in enumerate(kill_zones):
            center = self._norm_to_pixel(x, y)
            
            # Kill zone circle with pulsing
            pulse = int(30 * np.sin(self.pulse_phase + i * 0.5))
            pulse_radius = max(5, radius + pulse // 3)
            
            cv2.circle(frame, center, pulse_radius, kill_color, 2)
            
            # Crosshair
            cross_size = 15
            cv2.line(frame,
                     (center[0] - cross_size, center[1]),
                     (center[0] + cross_size, center[1]),
                     color, 2)
            cv2.line(frame,
                     (center[0], center[1] - cross_size),
                     (center[0], center[1] + cross_size),
                     color, 2)
            
            # Diagonal lines for emphasis
            diag = cross_size // 2
            cv2.line(frame,
                     (center[0] - diag, center[1] - diag),
                     (center[0] + diag, center[1] + diag),
                     color, 1)
            cv2.line(frame,
                     (center[0] + diag, center[1] - diag),
                     (center[0] - diag, center[1] + diag),
                     color, 1)
            
            # Ambush point label
            cv2.putText(frame, f"AMBUSH {i+1}",
                        (center[0] - 30, center[1] - radius - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)
    
    def _draw_active_tracks(self, frame: np.ndarray,
                            tracks: List[Track]) -> None:
        """Draw currently active (being tracked) targets."""
        for track in tracks:
            if not track.points:
                continue
            
            # Get last position
            last = track.points[-1]
            center = self._norm_to_pixel(last.x, last.y)
            
            # Draw detection box if available
            if last.bbox and last.bbox != (0, 0, 0, 0):
                x, y, w, h = last.bbox
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            
            # Draw track trail (last N points)
            trail_length = min(20, len(track.points))
            if trail_length > 1:
                trail_points = track.points[-trail_length:]
                for i in range(len(trail_points) - 1):
                    p1 = self._norm_to_pixel(trail_points[i].x, trail_points[i].y)
                    p2 = self._norm_to_pixel(trail_points[i + 1].x, trail_points[i + 1].y)
                    alpha = (i + 1) / trail_length
                    color = (0, int(255 * alpha), int(255 * (1 - alpha)))
                    cv2.line(frame, p1, p2, color, 1)
            
            # Track ID label
            cv2.putText(frame, f"ID:{track.track_id}",
                        (center[0] + 10, center[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
    
    def _draw_predictions(self, frame: np.ndarray,
                          predictions: Dict[int, PredictionResult]) -> None:
        """Draw prediction vectors and paths."""
        color = self.config.color_prediction_vector
        
        for track_id, pred in predictions.items():
            # Current predicted position
            start = self._norm_to_pixel(pred.predicted_x - pred.predicted_velocity_x * 0.1,
                                         pred.predicted_y - pred.predicted_velocity_y * 0.1)
            
            # Predicted future position
            end_x = pred.predicted_x + pred.predicted_velocity_x * pred.prediction_time
            end_y = pred.predicted_y + pred.predicted_velocity_y * pred.prediction_time
            end = self._norm_to_pixel(end_x, end_y)
            
            # Draw arrow
            cv2.arrowedLine(frame, start, end, color, 2, tipLength=0.2)
            
            # ETA label
            if pred.time_to_point > 0:
                mid = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
                cv2.putText(frame, f"ETA:{pred.time_to_point:.2f}s",
                            mid, cv2.FONT_HERSHEY_SIMPLEX, 0.35, color, 1)
    
    def _draw_velocity_vectors(self, frame: np.ndarray,
                                targets: Dict[int, TrackedTarget]) -> None:
        """Draw velocity vectors for tracked targets."""
        for track_id, target in targets.items():
            x, y = target.last_position
            vx, vy = target.last_velocity
            
            # Scale velocity for visualization
            scale = 50  # pixels per unit velocity
            
            start = self._norm_to_pixel(x, y)
            end = (int(start[0] + vx * scale * self.frame_width),
                   int(start[1] + vy * scale * self.frame_height))
            
            # Color based on zone
            if target.current_zone == ZoneType.KILL:
                color = (0, 0, 255)  # Red
            elif target.current_zone == ZoneType.PERIPHERAL:
                color = (0, 255, 255)  # Yellow
            else:
                color = (100, 100, 100)  # Gray
            
            cv2.arrowedLine(frame, start, end, color, 1, tipLength=0.3)
    
    def _draw_state_indicator(self, frame: np.ndarray, state_name: str) -> None:
        """Draw current state indicator in top-right corner."""
        # State colors
        state_colors = {
            "LEARNING": (0, 255, 255),     # Yellow
            "WATCHING": (255, 255, 0),     # Cyan
            "AIMING": (0, 165, 255),       # Orange
            "FIRING": (0, 0, 255),         # Red
            "COOLDOWN": (128, 128, 128),   # Gray
        }
        
        color = state_colors.get(state_name, (255, 255, 255))
        
        # Background box
        text_size = cv2.getTextSize(state_name, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0]
        x = self.frame_width - text_size[0] - 20
        y = 30
        
        cv2.rectangle(frame, (x - 10, y - text_size[1] - 5),
                      (x + text_size[0] + 5, y + 5), (0, 0, 0), -1)
        cv2.rectangle(frame, (x - 10, y - text_size[1] - 5),
                      (x + text_size[0] + 5, y + 5), color, 2)
        
        cv2.putText(frame, state_name, (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        
        # Sentry mode label
        cv2.putText(frame, "SENTRY MODE", (x - 10, y + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200, 200, 200), 1)
    
    def _draw_confidence_meter(self, frame: np.ndarray,
                                paths: List[ConfirmedPath]) -> None:
        """Draw confidence meter for confirmed paths."""
        if not paths:
            return
        
        # Average confidence
        avg_conf = np.mean([p.confidence for p in paths])
        
        # Meter position (bottom-left)
        x, y = 20, self.frame_height - 40
        width, height = 100, 15
        
        # Background
        cv2.rectangle(frame, (x, y), (x + width, y + height), (50, 50, 50), -1)
        
        # Fill based on confidence
        fill_width = int(width * avg_conf)
        
        # Color gradient from red to green
        if avg_conf < 0.5:
            color = (0, int(255 * avg_conf * 2), 255)
        else:
            color = (0, 255, int(255 * (1 - avg_conf) * 2))
        
        cv2.rectangle(frame, (x, y), (x + fill_width, y + height), color, -1)
        
        # Border
        cv2.rectangle(frame, (x, y), (x + width, y + height), (200, 200, 200), 1)
        
        # Label
        cv2.putText(frame, f"CONF: {avg_conf:.0%}",
                    (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200, 200, 200), 1)
    
    def _draw_debug_info(self, frame: np.ndarray, stats: dict) -> None:
        """Draw debug information."""
        y = 20
        line_height = 18
        x = 10
        
        cv2.putText(frame, "SENTRY DEBUG", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        y += line_height
        
        for key, value in stats.items():
            text = f"{key}: {value}"
            cv2.putText(frame, text, (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 200, 0), 1)
            y += line_height
    
    def _draw_fire_countdown(self, frame: np.ndarray) -> None:
        """Draw fire countdown overlay."""
        if self.fire_countdown is None:
            return
        
        # Large centered countdown
        center_x = self.frame_width // 2
        center_y = self.frame_height // 2
        
        # Countdown text
        if self.fire_countdown > 0:
            text = f"{self.fire_countdown:.2f}"
            color = (0, 255, 255)  # Yellow
        else:
            text = "FIRE!"
            color = (0, 0, 255)  # Red
        
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 2.0, 3)[0]
        text_x = center_x - text_size[0] // 2
        text_y = center_y + text_size[1] // 2
        
        # Shadow
        cv2.putText(frame, text, (text_x + 2, text_y + 2),
                    cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 0, 0), 4)
        
        # Main text
        cv2.putText(frame, text, (text_x, text_y),
                    cv2.FONT_HERSHEY_SIMPLEX, 2.0, color, 3)
    
    def set_fire_countdown(self, seconds: Optional[float]) -> None:
        """
        Set fire countdown value.
        
        Args:
            seconds: Seconds until fire, or None to clear
        """
        self.fire_countdown = seconds
        if seconds is not None and self.fire_countdown_start is None:
            self.fire_countdown_start = time.time()
        elif seconds is None:
            self.fire_countdown_start = None
    
    def clear_fire_countdown(self) -> None:
        """Clear fire countdown display."""
        self.fire_countdown = None
        self.fire_countdown_start = None

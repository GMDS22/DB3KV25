"""
Trajectory Predictor - Predicts target positions using Kalman filter.

Provides position/velocity estimation, time-to-arrival calculations,
and lead time computation for predictive firing.
"""

import numpy as np
from typing import Tuple, Optional, List
from dataclasses import dataclass
import time

# Support both relative imports (when used as package) and absolute imports (standalone)
try:
    from .track_recorder import Track, TrackPoint
    from .sentry_config import SentryConfig
except ImportError:
    from track_recorder import Track, TrackPoint
    from sentry_config import SentryConfig


@dataclass
class PredictionResult:
    """Result of trajectory prediction."""
    predicted_x: float              # Predicted X position (normalized)
    predicted_y: float              # Predicted Y position (normalized)
    predicted_velocity_x: float     # Predicted X velocity
    predicted_velocity_y: float     # Predicted Y velocity
    predicted_speed: float          # Predicted speed magnitude
    time_to_point: float           # Time to reach a specific point (seconds)
    confidence: float              # Prediction confidence (0.0-1.0)
    prediction_time: float         # How far ahead this prediction is (seconds)


class KalmanFilter2D:
    """
    2D Kalman Filter for position and velocity estimation.
    
    State vector: [x, y, vx, vy]
    Measurement: [x, y]
    """
    
    def __init__(self, process_noise: float = 0.03, measurement_noise: float = 0.1):
        """
        Initialize Kalman filter.
        
        Args:
            process_noise: Higher = more responsive to changes
            measurement_noise: Higher = trust measurements less
        """
        # State vector [x, y, vx, vy]
        self.state = np.zeros(4)
        
        # State covariance matrix
        self.P = np.eye(4) * 1.0
        
        # State transition matrix (will be updated with dt)
        self.F = np.eye(4)
        
        # Measurement matrix (we observe x, y)
        self.H = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0]
        ], dtype=float)
        
        # Process noise covariance
        self.Q = np.eye(4) * process_noise
        
        # Measurement noise covariance
        self.R = np.eye(2) * measurement_noise
        
        # Identity matrix for updates
        self.I = np.eye(4)
        
        # Tracking state
        self.initialized = False
        self.last_update_time: Optional[float] = None
    
    def reset(self) -> None:
        """Reset filter state."""
        self.state = np.zeros(4)
        self.P = np.eye(4) * 1.0
        self.initialized = False
        self.last_update_time = None
    
    def initialize(self, x: float, y: float, timestamp: float) -> None:
        """Initialize filter with first measurement."""
        self.state = np.array([x, y, 0.0, 0.0])
        self.P = np.eye(4) * 1.0
        self.initialized = True
        self.last_update_time = timestamp
    
    def predict(self, dt: float) -> np.ndarray:
        """
        Predict state forward by dt seconds.
        
        Args:
            dt: Time step in seconds
            
        Returns:
            Predicted state [x, y, vx, vy]
        """
        # Update transition matrix with current dt
        self.F = np.array([
            [1, 0, dt, 0],
            [0, 1, 0, dt],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ], dtype=float)
        
        # Predict state
        predicted_state = self.F @ self.state
        
        # Predict covariance
        self.P = self.F @ self.P @ self.F.T + self.Q
        
        return predicted_state
    
    def update(self, x: float, y: float, timestamp: float) -> np.ndarray:
        """
        Update filter with new measurement.
        
        Args:
            x, y: Measured position (normalized)
            timestamp: Measurement timestamp
            
        Returns:
            Updated state [x, y, vx, vy]
        """
        if not self.initialized:
            self.initialize(x, y, timestamp)
            return self.state
        
        # Calculate dt
        dt = timestamp - self.last_update_time if self.last_update_time else 0.016
        dt = max(0.001, min(dt, 1.0))  # Clamp to reasonable range
        
        # Predict step
        self.predict(dt)
        
        # Measurement
        z = np.array([x, y])
        
        # Innovation
        y_innov = z - self.H @ self.state
        
        # Innovation covariance
        S = self.H @ self.P @ self.H.T + self.R
        
        # Kalman gain
        K = self.P @ self.H.T @ np.linalg.inv(S)
        
        # Update state
        self.state = self.state + K @ y_innov
        
        # Update covariance
        self.P = (self.I - K @ self.H) @ self.P
        
        self.last_update_time = timestamp
        
        return self.state
    
    def get_state(self) -> Tuple[float, float, float, float]:
        """Get current state as tuple (x, y, vx, vy)."""
        return tuple(self.state)
    
    def predict_position(self, lookahead: float) -> Tuple[float, float]:
        """
        Predict position at lookahead seconds in the future.
        
        Args:
            lookahead: Seconds ahead to predict
            
        Returns:
            (predicted_x, predicted_y)
        """
        x, y, vx, vy = self.state
        return (x + vx * lookahead, y + vy * lookahead)


class TrajectoryPredictor:
    """
    Predicts target trajectories and calculates intercept timing.
    
    Responsibilities:
    - Maintain Kalman filter per active track
    - Predict future positions
    - Calculate time-to-arrival at ambush point
    - Compute lead time for predictive firing
    """
    
    def __init__(self, config=None):
        """
        Initialize the trajectory predictor.
        
        Args:
            config: SentryConfig instance or None for defaults
        """
        self.config = config or SentryConfig()
        
        # Kalman filter per track ID
        self.filters: dict[int, KalmanFilter2D] = {}
        
        # Recent predictions for visualization
        self.last_predictions: dict[int, PredictionResult] = {}
    
    def update_track(self, track_id: int, x: float, y: float, 
                     timestamp: Optional[float] = None) -> np.ndarray:
        """
        Update prediction for a track with new measurement.
        
        Args:
            track_id: Unique track identifier
            x, y: Current position (normalized 0.0-1.0)
            timestamp: Measurement time, or None for current time
            
        Returns:
            Filtered state [x, y, vx, vy]
        """
        timestamp = timestamp or time.time()
        
        if track_id not in self.filters:
            self.filters[track_id] = KalmanFilter2D(
                process_noise=self.config.kalman_process_noise,
                measurement_noise=self.config.kalman_measurement_noise
            )
        
        return self.filters[track_id].update(x, y, timestamp)
    
    def predict_position(self, track_id: int, 
                         lookahead: float = None) -> Optional[Tuple[float, float]]:
        """
        Predict where a track will be in the future.
        
        Args:
            track_id: Track to predict for
            lookahead: Seconds ahead, or None for config default
            
        Returns:
            (predicted_x, predicted_y) or None if track not found
        """
        lookahead = lookahead or self.config.prediction_lookahead
        
        if track_id not in self.filters:
            return None
        
        return self.filters[track_id].predict_position(lookahead)
    
    def calculate_time_to_point(self, track_id: int, 
                                 target_x: float, target_y: float) -> Optional[float]:
        """
        Calculate time for track to reach a specific point.
        
        Uses linear extrapolation from current velocity.
        
        Args:
            track_id: Track to calculate for
            target_x, target_y: Target point (normalized)
            
        Returns:
            Estimated time in seconds, or None if cannot determine
        """
        if track_id not in self.filters:
            return None
        
        x, y, vx, vy = self.filters[track_id].get_state()
        
        # Distance to target
        dx = target_x - x
        dy = target_y - y
        distance = np.sqrt(dx*dx + dy*dy)
        
        # Speed
        speed = np.sqrt(vx*vx + vy*vy)
        
        if speed < self.config.min_speed_threshold / 1000:  # Convert to normalized
            return None  # Target not moving
        
        # Check if target is moving toward the point
        # Dot product of velocity and direction to target
        if distance > 0.001:
            dir_x = dx / distance
            dir_y = dy / distance
            approach_speed = vx * dir_x + vy * dir_y
            
            if approach_speed < 0.001:
                return None  # Moving away from target
            
            return distance / approach_speed
        
        return 0.0  # Already at target
    
    def calculate_intercept(self, track_id: int, 
                            ambush_x: float, ambush_y: float,
                            kill_zone_radius: float = None) -> Optional[PredictionResult]:
        """
        Calculate full intercept prediction for ambush.
        
        Args:
            track_id: Track to calculate for
            ambush_x, ambush_y: Ambush point (normalized)
            kill_zone_radius: Radius around ambush point, or None for config
            
        Returns:
            PredictionResult with all intercept data, or None
        """
        kill_zone_radius = kill_zone_radius or self.config.kill_zone_radius
        
        if track_id not in self.filters:
            return None
        
        kf = self.filters[track_id]
        x, y, vx, vy = kf.get_state()
        
        speed = np.sqrt(vx*vx + vy*vy)
        
        # Time to ambush point
        time_to_point = self.calculate_time_to_point(track_id, ambush_x, ambush_y)
        
        if time_to_point is None:
            return None
        
        # Calculate confidence based on:
        # 1. Prediction certainty (lower covariance = higher confidence)
        # 2. How directly the target is approaching
        # 3. Speed consistency
        
        # Direction to ambush point
        dx = ambush_x - x
        dy = ambush_y - y
        dist = np.sqrt(dx*dx + dy*dy)
        
        if dist > 0.001 and speed > 0.001:
            dir_x, dir_y = dx / dist, dy / dist
            vel_x, vel_y = vx / speed, vy / speed
            
            # How aligned is velocity with direction to target?
            alignment = vel_x * dir_x + vel_y * dir_y
            alignment = max(0.0, alignment)  # Only consider approaching
        else:
            alignment = 0.0
        
        # Covariance factor (lower trace = more certain)
        cov_trace = np.trace(kf.P)
        cov_factor = max(0.0, 1.0 - cov_trace / 4.0)
        
        # Combined confidence
        confidence = 0.5 * alignment + 0.5 * cov_factor
        
        # Predicted position at intercept time
        pred_x, pred_y = kf.predict_position(time_to_point)
        
        result = PredictionResult(
            predicted_x=pred_x,
            predicted_y=pred_y,
            predicted_velocity_x=vx,
            predicted_velocity_y=vy,
            predicted_speed=speed,
            time_to_point=time_to_point,
            confidence=confidence,
            prediction_time=time_to_point
        )
        
        self.last_predictions[track_id] = result
        
        return result
    
    def calculate_fire_lead_time(self, prediction: PredictionResult,
                                  mechanical_delay: float = None) -> float:
        """
        Calculate when to fire to hit target at ambush point.
        
        Args:
            prediction: PredictionResult from calculate_intercept
            mechanical_delay: Mechanical delay to account for, or None for config
            
        Returns:
            Time from now until fire command should be sent (seconds)
        """
        mechanical_delay = mechanical_delay or self.config.mechanical_lead_time
        
        # Account for mechanical delay
        fire_time = prediction.time_to_point - mechanical_delay
        
        # Account for fire window (fire slightly early for margin)
        fire_time -= self.config.fire_window_before
        
        return max(0.0, fire_time)
    
    def should_fire_now(self, track_id: int, 
                        ambush_x: float, ambush_y: float) -> Tuple[bool, float, str]:
        """
        Determine if we should fire at this moment.
        
        Args:
            track_id: Track to check
            ambush_x, ambush_y: Ambush point
            
        Returns:
            (should_fire, confidence, reason)
        """
        prediction = self.calculate_intercept(track_id, ambush_x, ambush_y)
        
        if prediction is None:
            return (False, 0.0, "No prediction available")
        
        # Check confidence threshold
        if prediction.confidence < self.config.fire_confidence_threshold:
            return (False, prediction.confidence, 
                    f"Confidence too low: {prediction.confidence:.2f}")
        
        # Calculate optimal fire time
        fire_lead = self.calculate_fire_lead_time(prediction)
        
        # Fire window check
        if fire_lead <= 0:
            # Check if within late fire window
            if prediction.time_to_point <= self.config.fire_window_after:
                return (True, prediction.confidence, "Target at ambush point - FIRE!")
            else:
                return (False, prediction.confidence, 
                        f"Target passed ambush point by {prediction.time_to_point:.3f}s")
        
        if fire_lead <= 0.016:  # Within one frame (~60fps)
            return (True, prediction.confidence, 
                    f"Optimal fire window - ETA: {prediction.time_to_point:.3f}s")
        
        return (False, prediction.confidence, 
                f"Waiting for fire window: {fire_lead:.3f}s remaining")
    
    def get_prediction_path(self, track_id: int, 
                            steps: int = 10, 
                            total_time: float = 1.0) -> List[Tuple[float, float]]:
        """
        Get predicted path for visualization.
        
        Args:
            track_id: Track to predict for
            steps: Number of points in path
            total_time: How far ahead to predict (seconds)
            
        Returns:
            List of (x, y) tuples along predicted path
        """
        if track_id not in self.filters:
            return []
        
        path = []
        dt = total_time / steps
        
        for i in range(steps):
            t = dt * (i + 1)
            pos = self.filters[track_id].predict_position(t)
            path.append(pos)
        
        return path
    
    def remove_track(self, track_id: int) -> None:
        """Remove tracking state for a track ID."""
        if track_id in self.filters:
            del self.filters[track_id]
        if track_id in self.last_predictions:
            del self.last_predictions[track_id]
    
    def clear_all(self) -> None:
        """Clear all tracking state."""
        self.filters.clear()
        self.last_predictions.clear()
    
    def get_stats(self) -> dict:
        """Get predictor statistics."""
        return {
            'active_filters': len(self.filters),
            'last_predictions': len(self.last_predictions)
        }

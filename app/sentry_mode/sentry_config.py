"""
Sentry Mode Configuration - All constants and tunable parameters.

This file centralizes all configuration for the Sentry Ambush Mode.
Modify these values to tune behavior without changing logic code.
"""

import json
import os
from dataclasses import dataclass, field, asdict
from typing import List, Tuple, Optional
from pathlib import Path


@dataclass
class SentryConfig:
    """
    Configuration container for Sentry Ambush Mode.
    
    All parameters are documented with their purpose and valid ranges.
    """
    
    # =========================================================================
    # ZONE GEOMETRY
    # =========================================================================
    
    # Guard point - the center of attention (normalized 0.0-1.0 of frame)
    guard_point: Tuple[float, float] = (0.5, 0.5)
    
    # Peripheral zone - ring around guard point where targets are detected
    # Inner radius: inside this, target is "at guard point"
    # Outer radius: outside this, target is ignored
    peripheral_inner_radius: float = 0.15  # 15% of frame width
    peripheral_outer_radius: float = 0.45  # 45% of frame width
    
    # Kill zone - the ambush point radius (normalized)
    kill_zone_radius: float = 0.08  # 8% of frame width
    
    # =========================================================================
    # LEARNING PHASE
    # =========================================================================
    
    # Minimum passes through similar path before track is "confirmed"
    min_passes_to_confirm: int = 2
    
    # Time window to consider tracks as "same pattern" (seconds)
    track_similarity_time_window: float = 30.0
    
    # Spatial similarity threshold (0.0-1.0, lower = stricter matching)
    # Uses normalized Fréchet distance
    path_similarity_threshold: float = 0.15
    
    # Minimum track length (points) to be considered valid
    min_track_length: int = 10
    
    # Maximum tracks to store in memory
    max_stored_tracks: int = 50
    
    # Track expiry time (seconds) - tracks older than this are forgotten
    track_expiry_seconds: float = 300.0  # 5 minutes
    
    # =========================================================================
    # TRAJECTORY PREDICTION (Kalman Filter)
    # =========================================================================
    
    # Process noise - higher = more responsive, lower = smoother
    kalman_process_noise: float = 0.03
    
    # Measurement noise - higher = trust measurements less
    kalman_measurement_noise: float = 0.1
    
    # Prediction lookahead (seconds) - how far ahead to predict
    prediction_lookahead: float = 0.5
    
    # Velocity smoothing factor (0.0-1.0) - EMA for speed calculation
    velocity_smoothing: float = 0.3
    
    # Minimum speed threshold (pixels/second) - below this, target is "stopped"
    min_speed_threshold: float = 10.0
    
    # =========================================================================
    # FIRING LOGIC
    # =========================================================================
    
    # Fire window - time tolerance around predicted arrival (seconds)
    fire_window_before: float = 0.05  # Fire this early
    fire_window_after: float = 0.10   # Fire this late (reaction buffer)
    
    # Burst mode settings
    burst_enabled: bool = True
    burst_count: int = 3          # Shots per burst
    burst_interval_ms: int = 50   # Milliseconds between shots
    
    # Lead time compensation (seconds) - account for mechanical delay
    mechanical_lead_time: float = 0.02
    
    # Confidence threshold - minimum prediction confidence to fire (0.0-1.0)
    fire_confidence_threshold: float = 0.7
    
    # Cooldown between engagements (seconds)
    fire_cooldown: float = 1.0
    
    # =========================================================================
    # MULTI-TRACK AMBUSH
    # =========================================================================
    
    # Maximum confirmed tracks to maintain ambush points for
    max_ambush_points: int = 3
    
    # Priority ranking method: 'frequency', 'recency', 'speed', 'confidence'
    ambush_priority_method: str = 'frequency'
    
    # Allow manual ambush point override
    manual_ambush_enabled: bool = True
    
    # =========================================================================
    # VISUALIZATION / HUD
    # =========================================================================
    
    # Colors (BGR format for OpenCV)
    color_peripheral_zone: Tuple[int, int, int] = (255, 255, 0)    # Cyan
    color_confirmed_track: Tuple[int, int, int] = (0, 255, 0)      # Green
    color_learning_track: Tuple[int, int, int] = (0, 255, 255)     # Yellow
    color_ambush_point: Tuple[int, int, int] = (0, 0, 255)         # Red
    color_prediction_vector: Tuple[int, int, int] = (255, 0, 255)  # Magenta
    color_kill_zone: Tuple[int, int, int] = (0, 100, 255)          # Orange
    
    # Line thickness
    zone_line_thickness: int = 2
    track_line_thickness: int = 2
    
    # Show debug info
    show_debug_overlay: bool = True
    show_velocity_vectors: bool = True
    show_prediction_path: bool = True
    show_confidence_meter: bool = True
    
    # =========================================================================
    # PERSISTENCE
    # =========================================================================
    
    # Save confirmed tracks to JSON for session persistence
    persist_tracks: bool = True
    tracks_save_path: str = "config/sentry_tracks.json"
    
    # Auto-save interval (seconds)
    auto_save_interval: float = 60.0
    
    # =========================================================================
    # DETECTION SETTINGS
    # =========================================================================
    
    # YOLO confidence threshold for this mode
    yolo_confidence: float = 0.5
    
    # Target classes (empty = all classes)
    target_classes: List[str] = field(default_factory=lambda: ["mouse", "rat", "bird", "cat"])
    
    # Minimum detection box area (pixels²) to consider
    min_detection_area: int = 500
    
    # =========================================================================
    # STATE MACHINE TIMING
    # =========================================================================
    
    # Learning phase minimum duration (seconds) before transitioning
    min_learning_duration: float = 5.0
    
    # Watching phase timeout - return to learning if no action (seconds)
    watching_timeout: float = 60.0
    
    # Aiming phase max duration (seconds) - abort if target doesn't arrive
    aiming_timeout: float = 3.0
    
    # =========================================================================
    # METHODS
    # =========================================================================
    
    def to_dict(self) -> dict:
        """Convert config to dictionary for JSON serialization."""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: dict) -> 'SentryConfig':
        """Create config from dictionary."""
        # Handle tuple conversion from JSON lists
        if 'guard_point' in data and isinstance(data['guard_point'], list):
            data['guard_point'] = tuple(data['guard_point'])
        for color_key in [k for k in data.keys() if k.startswith('color_')]:
            if isinstance(data[color_key], list):
                data[color_key] = tuple(data[color_key])
        return cls(**data)
    
    def save(self, path: Optional[str] = None) -> None:
        """Save configuration to JSON file."""
        save_path = Path(path) if path else Path(__file__).parent / "config" / "sentry_defaults.json"
        save_path.parent.mkdir(parents=True, exist_ok=True)
        with open(save_path, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
    
    @classmethod
    def load(cls, path: Optional[str] = None) -> 'SentryConfig':
        """Load configuration from JSON file, or return defaults if not found."""
        load_path = Path(path) if path else Path(__file__).parent / "config" / "sentry_defaults.json"
        if load_path.exists():
            with open(load_path, 'r') as f:
                data = json.load(f)
            return cls.from_dict(data)
        return cls()  # Return defaults


# Default configuration instance
DEFAULT_CONFIG = SentryConfig()

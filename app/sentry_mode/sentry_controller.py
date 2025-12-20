"""
Sentry Controller - Main orchestrator for Sentry Ambush Mode.

Coordinates all components and manages the state machine:
LEARNING → WATCHING → AIMING → FIRING → (back to WATCHING)

Provides a clean interface for integration with the main app.
"""

import time
import json
import numpy as np
from enum import Enum, auto
from typing import Optional, List, Tuple, Callable, Dict, Any
from dataclasses import dataclass
from pathlib import Path

# Support both relative imports (when used as package) and absolute imports (standalone)
try:
    from .sentry_config import SentryConfig
    from .track_recorder import TrackRecorder, Track
    from .path_analyzer import PathAnalyzer, ConfirmedPath
    from .trajectory_predictor import TrajectoryPredictor, PredictionResult
    from .peripheral_sensor import PeripheralSensor, ZoneEvent, ZoneType
    from .sentry_overlay import SentryOverlay
except ImportError:
    from sentry_config import SentryConfig
    from track_recorder import TrackRecorder, Track
    from path_analyzer import PathAnalyzer, ConfirmedPath
    from trajectory_predictor import TrajectoryPredictor, PredictionResult
    from peripheral_sensor import PeripheralSensor, ZoneEvent, ZoneType
    from sentry_overlay import SentryOverlay


class SentryState(Enum):
    """State machine states for Sentry Mode."""
    IDLE = auto()           # Not active
    LEARNING = auto()       # Studying target movement patterns
    WATCHING = auto()       # Turret aimed at ambush point, waiting
    AIMING = auto()         # Target entering, calculating intercept
    FIRING = auto()         # Executing fire command
    COOLDOWN = auto()       # Post-fire cooldown period


@dataclass
class FireCommand:
    """Command to fire at a target."""
    track_id: int
    ambush_point: Tuple[float, float]
    confidence: float
    burst_count: int
    timestamp: float
    reason: str


class SentryController:
    """
    Main controller for Sentry Ambush Mode.
    
    Orchestrates all subsystems:
    - TrackRecorder: Records target trajectories
    - PathAnalyzer: Identifies repeated patterns
    - TrajectoryPredictor: Predicts interception timing
    - PeripheralSensor: Detects zone transitions
    - SentryOverlay: Renders visualizations
    
    State Machine:
    1. LEARNING: Observe targets, record tracks, identify patterns
    2. WATCHING: Turret at ambush point, peripheral sensor active
    3. AIMING: Target entering, calculating optimal fire time
    4. FIRING: Execute fire command (burst or single)
    5. COOLDOWN: Post-fire delay before returning to WATCHING
    
    The firing mechanism is INDEPENDENT of the main app's dead-zone logic.
    It fires based on trajectory prediction and time-to-arrival calculations.
    """
    
    def __init__(self, config: Optional[SentryConfig] = None):
        """
        Initialize the Sentry Controller.
        
        Args:
            config: SentryConfig instance, path to config JSON, or None for defaults
        """
        # Load configuration
        if isinstance(config, str):
            self.config = SentryConfig.load(config)
        elif config is None:
            self.config = SentryConfig()
        else:
            self.config = config
        
        # Initialize subsystems
        self.track_recorder = TrackRecorder(self.config)
        self.path_analyzer = PathAnalyzer(self.config)
        self.predictor = TrajectoryPredictor(self.config)
        self.peripheral_sensor = PeripheralSensor(self.config)
        self.overlay = SentryOverlay(self.config)
        
        # State machine
        self.state = SentryState.IDLE
        self.state_start_time: float = time.time()
        self.previous_state: SentryState = SentryState.IDLE
        
        # Current engagement state
        self.current_target_id: Optional[int] = None
        self.current_ambush_point: Optional[Tuple[float, float]] = None
        self.current_prediction: Optional[PredictionResult] = None
        
        # Turret position (for main app integration)
        self.turret_pan: float = 90.0   # Home position
        self.turret_tilt: float = 45.0  # Home position
        
        # Fire control
        self.fire_enabled: bool = False
        self.last_fire_time: float = 0.0
        self.pending_fire_command: Optional[FireCommand] = None
        self.burst_shots_remaining: int = 0
        self.last_burst_time: float = 0.0
        
        # Callbacks for integration
        self._fire_callbacks: List[Callable[[FireCommand], None]] = []
        self._turret_move_callbacks: List[Callable[[float, float], None]] = []
        self._state_change_callbacks: List[Callable[[SentryState, SentryState], None]] = []
        
        # Frame dimensions
        self.frame_width: int = 640
        self.frame_height: int = 480
        
        # Auto-save timer
        self._last_save_time: float = time.time()
        
        # Register zone event handler
        self.peripheral_sensor.register_event_callback(self._on_zone_event)
    
    # =========================================================================
    # MAIN LOOP METHODS
    # =========================================================================
    
    def start(self) -> None:
        """Start sentry mode - transition to LEARNING state."""
        self._change_state(SentryState.LEARNING)
        
        # Load persisted tracks if enabled
        if self.config.persist_tracks:
            self._load_persisted_tracks()
    
    def stop(self) -> None:
        """Stop sentry mode - transition to IDLE."""
        # Save tracks before stopping
        if self.config.persist_tracks:
            self._save_tracks()
        
        self._change_state(SentryState.IDLE)
        self.current_target_id = None
        self.current_ambush_point = None
        self.pending_fire_command = None
    
    def update(self, detections: List[Tuple[int, int, int, int, int]],
               frame: Optional[np.ndarray] = None,
               timestamp: Optional[float] = None) -> np.ndarray:
        """
        Main update loop - call this every frame.
        
        Args:
            detections: List of (track_id, x, y, w, h) from ByteTrack
            frame: Current video frame for overlay rendering
            timestamp: Current timestamp, or None for current time
            
        Returns:
            Frame with sentry overlays (or original frame if None provided)
        """
        timestamp = timestamp or time.time()
        
        if self.state == SentryState.IDLE:
            return frame if frame is not None else np.zeros((self.frame_height, self.frame_width, 3), dtype=np.uint8)
        
        # Update frame dimensions
        if frame is not None:
            self.frame_height, self.frame_width = frame.shape[:2]
            self.track_recorder.set_frame_dimensions(self.frame_width, self.frame_height)
            self.overlay.set_frame_dimensions(self.frame_width, self.frame_height)
        
        # Update subsystems
        active_tracks = self.track_recorder.update(detections, timestamp)
        
        # Process completed tracks through analyzer
        for track in self.track_recorder.completed_tracks:
            confirmed = self.path_analyzer.analyze_track(track)
            if confirmed:
                self._on_path_confirmed(confirmed)
        self.track_recorder.clear_completed_tracks()
        
        # Update predictor with active tracks
        for track in active_tracks:
            if track.points:
                last = track.points[-1]
                self.predictor.update_track(
                    track.track_id, last.x, last.y, last.timestamp
                )
        
        # Update peripheral sensor
        sensor_detections = [
            (t.track_id, t.points[-1].x, t.points[-1].y,
             t.points[-1].velocity_x, t.points[-1].velocity_y)
            for t in active_tracks if t.points
        ]
        self.peripheral_sensor.update(sensor_detections, timestamp)
        
        # Update kill zones from confirmed paths
        ambush_points = self.path_analyzer.get_all_ambush_points()
        self.peripheral_sensor.set_kill_zones([(x, y) for x, y, _ in ambush_points])
        
        # State machine update
        self._update_state_machine(timestamp)
        
        # Handle pending fire commands
        self._process_fire_commands(timestamp)
        
        # Auto-save check
        if (self.config.persist_tracks and 
            timestamp - self._last_save_time > self.config.auto_save_interval):
            self._save_tracks()
            self._last_save_time = timestamp
        
        # Render overlays
        if frame is not None:
            frame = self._render_frame(frame, timestamp)
        
        return frame
    
    # =========================================================================
    # STATE MACHINE
    # =========================================================================
    
    def _change_state(self, new_state: SentryState) -> None:
        """Transition to a new state."""
        if new_state == self.state:
            return
        
        old_state = self.state
        self.previous_state = old_state
        self.state = new_state
        self.state_start_time = time.time()
        
        # Notify callbacks
        for callback in self._state_change_callbacks:
            try:
                callback(old_state, new_state)
            except Exception as e:
                print(f"Error in state change callback: {e}")
        
        print(f"[SENTRY] State: {old_state.name} → {new_state.name}")
    
    def _update_state_machine(self, timestamp: float) -> None:
        """Update state machine based on current conditions."""
        state_duration = timestamp - self.state_start_time
        
        if self.state == SentryState.LEARNING:
            self._update_learning_state(state_duration, timestamp)
        
        elif self.state == SentryState.WATCHING:
            self._update_watching_state(state_duration, timestamp)
        
        elif self.state == SentryState.AIMING:
            self._update_aiming_state(state_duration, timestamp)
        
        elif self.state == SentryState.FIRING:
            self._update_firing_state(state_duration, timestamp)
        
        elif self.state == SentryState.COOLDOWN:
            self._update_cooldown_state(state_duration, timestamp)
    
    def _update_learning_state(self, duration: float, timestamp: float) -> None:
        """Update LEARNING state logic."""
        # Check if we have confirmed paths and minimum learning time passed
        if (duration >= self.config.min_learning_duration and 
            len(self.path_analyzer.confirmed_paths) > 0):
            
            # Get best ambush point
            best = self.path_analyzer.get_best_ambush_point()
            if best:
                self.current_ambush_point = (best[0], best[1])
                self._aim_turret_at_ambush()
                self._change_state(SentryState.WATCHING)
    
    def _update_watching_state(self, duration: float, timestamp: float) -> None:
        """Update WATCHING state logic."""
        # Check for timeout
        if duration > self.config.watching_timeout:
            # Return to learning if no action
            self._change_state(SentryState.LEARNING)
            return
        
        # Check for targets entering peripheral zone
        peripheral_targets = self.peripheral_sensor.get_targets_in_peripheral()
        
        for target in peripheral_targets:
            # Check if this target is approaching an ambush point
            if self.current_ambush_point:
                result = self.predictor.calculate_intercept(
                    target.track_id,
                    self.current_ambush_point[0],
                    self.current_ambush_point[1]
                )
                
                if result and result.confidence >= self.config.fire_confidence_threshold:
                    self.current_target_id = target.track_id
                    self.current_prediction = result
                    self._change_state(SentryState.AIMING)
                    return
    
    def _update_aiming_state(self, duration: float, timestamp: float) -> None:
        """Update AIMING state logic."""
        # Check timeout
        if duration > self.config.aiming_timeout:
            self._change_state(SentryState.WATCHING)
            self.current_target_id = None
            self.current_prediction = None
            self.overlay.clear_fire_countdown()
            return
        
        # Verify target still exists and is approaching
        if self.current_target_id is None or self.current_ambush_point is None:
            self._change_state(SentryState.WATCHING)
            return
        
        # Update prediction
        result = self.predictor.calculate_intercept(
            self.current_target_id,
            self.current_ambush_point[0],
            self.current_ambush_point[1]
        )
        
        if result is None:
            # Lost target
            self._change_state(SentryState.WATCHING)
            self.current_target_id = None
            self.overlay.clear_fire_countdown()
            return
        
        self.current_prediction = result
        
        # Update countdown display
        fire_lead = self.predictor.calculate_fire_lead_time(result)
        self.overlay.set_fire_countdown(fire_lead)
        
        # Check if we should fire
        should_fire, confidence, reason = self.predictor.should_fire_now(
            self.current_target_id,
            self.current_ambush_point[0],
            self.current_ambush_point[1]
        )
        
        if should_fire and self.fire_enabled:
            self._initiate_fire(self.current_target_id, confidence, reason)
            self._change_state(SentryState.FIRING)
    
    def _update_firing_state(self, duration: float, timestamp: float) -> None:
        """Update FIRING state logic."""
        # Firing is handled by _process_fire_commands
        # This state waits for burst to complete
        
        if self.burst_shots_remaining <= 0 and self.pending_fire_command is None:
            self.overlay.clear_fire_countdown()
            self._change_state(SentryState.COOLDOWN)
    
    def _update_cooldown_state(self, duration: float, timestamp: float) -> None:
        """Update COOLDOWN state logic."""
        if duration >= self.config.fire_cooldown:
            self.current_target_id = None
            self.current_prediction = None
            self._change_state(SentryState.WATCHING)
    
    # =========================================================================
    # FIRE CONTROL
    # =========================================================================
    
    def enable_fire(self) -> None:
        """Enable automatic firing."""
        self.fire_enabled = True
        print("[SENTRY] Fire ENABLED")
    
    def disable_fire(self) -> None:
        """Disable automatic firing."""
        self.fire_enabled = False
        print("[SENTRY] Fire DISABLED")
    
    def _initiate_fire(self, track_id: int, confidence: float, reason: str) -> None:
        """Initiate a fire command."""
        if not self.current_ambush_point:
            return
        
        burst_count = self.config.burst_count if self.config.burst_enabled else 1
        
        command = FireCommand(
            track_id=track_id,
            ambush_point=self.current_ambush_point,
            confidence=confidence,
            burst_count=burst_count,
            timestamp=time.time(),
            reason=reason
        )
        
        self.pending_fire_command = command
        self.burst_shots_remaining = burst_count
        
        print(f"[SENTRY] FIRE INITIATED - Track {track_id}, Confidence: {confidence:.2f}, Reason: {reason}")
    
    def _process_fire_commands(self, timestamp: float) -> None:
        """Process pending fire commands and bursts."""
        if self.burst_shots_remaining <= 0:
            return
        
        # Check burst timing
        if timestamp - self.last_burst_time < self.config.burst_interval_ms / 1000.0:
            return
        
        # Execute fire
        self.burst_shots_remaining -= 1
        self.last_burst_time = timestamp
        self.last_fire_time = timestamp
        
        print(f"[SENTRY] FIRE! ({self.config.burst_count - self.burst_shots_remaining}/{self.config.burst_count})")
        
        # Notify callbacks
        if self.pending_fire_command:
            for callback in self._fire_callbacks:
                try:
                    callback(self.pending_fire_command)
                except Exception as e:
                    print(f"Error in fire callback: {e}")
        
        # Clear command after burst complete
        if self.burst_shots_remaining <= 0:
            self.pending_fire_command = None
    
    # =========================================================================
    # TURRET CONTROL
    # =========================================================================
    
    def _aim_turret_at_ambush(self) -> None:
        """Point turret at current ambush point."""
        if not self.current_ambush_point:
            return
        
        # Convert normalized coordinates to pan/tilt angles
        # This is a simplified mapping - adjust based on your servo setup
        x, y = self.current_ambush_point
        
        # Map X (0-1) to pan angle (typically 0-180)
        # Assuming 0.5 = center = 90 degrees
        pan = 90 + (x - 0.5) * 180
        pan = max(5, min(185, pan))
        
        # Map Y (0-1) to tilt angle
        # Assuming 0.5 = center = 75 degrees (midpoint of typical 20-130 range)
        tilt = 75 + (y - 0.5) * 110
        tilt = max(20, min(130, tilt))
        
        self.turret_pan = pan
        self.turret_tilt = tilt
        
        # Notify callbacks
        print(f"[SENTRY] Notifying {len(self._turret_move_callbacks)} turret move callbacks...")
        for callback in self._turret_move_callbacks:
            try:
                callback(pan, tilt)
            except Exception as e:
                print(f"Error in turret move callback: {e}")
        
        print(f"[SENTRY] Turret aimed at ambush point: Pan={pan:.1f}, Tilt={tilt:.1f}")
    
    def get_turret_position(self) -> Tuple[float, float]:
        """Get current turret position."""
        return (self.turret_pan, self.turret_tilt)
    
    # =========================================================================
    # MANUAL CONTROLS
    # =========================================================================
    
    def set_guard_point(self, x: float, y: float) -> None:
        """
        Manually set the guard point.
        
        Args:
            x, y: Normalized coordinates (0.0-1.0)
        """
        self.config.guard_point = (x, y)
        self.peripheral_sensor.set_guard_point(x, y)
        print(f"[SENTRY] Guard point set to ({x:.2f}, {y:.2f})")
    
    def add_manual_ambush_point(self, x: float, y: float) -> None:
        """
        Manually add an ambush point.
        
        Args:
            x, y: Normalized coordinates (0.0-1.0)
        """
        self.path_analyzer.add_manual_ambush_point(x, y)
        
        # If in watching state, update aim
        if self.state == SentryState.WATCHING:
            self.current_ambush_point = (x, y)
            self._aim_turret_at_ambush()
        
        print(f"[SENTRY] Manual ambush point added at ({x:.2f}, {y:.2f})")
    
    def clear_manual_ambush_points(self) -> None:
        """Clear all manually set ambush points."""
        self.path_analyzer.clear_manual_ambush_points()
        print("[SENTRY] Manual ambush points cleared")
    
    def force_learning_mode(self) -> None:
        """Force transition to learning mode."""
        self._change_state(SentryState.LEARNING)
        self.current_ambush_point = None
        self.current_target_id = None
    
    def force_watching_mode(self) -> None:
        """Force transition to watching mode (if ambush points exist)."""
        best = self.path_analyzer.get_best_ambush_point()
        if best:
            self.current_ambush_point = (best[0], best[1])
            self._aim_turret_at_ambush()
            self._change_state(SentryState.WATCHING)
        else:
            print("[SENTRY] Cannot watch - no ambush points defined")
    
    # =========================================================================
    # EVENT HANDLERS
    # =========================================================================
    
    def _on_zone_event(self, event: ZoneEvent) -> None:
        """Handle zone crossing events from peripheral sensor."""
        if event.event_type == "enter_peripheral":
            print(f"[SENTRY] Target {event.track_id} entered peripheral zone")
        
        elif event.event_type == "enter_kill":
            print(f"[SENTRY] Target {event.track_id} entered KILL ZONE!")
        
        elif event.event_type == "exit_peripheral":
            # Track completed its path through peripheral
            if event.track_id == self.current_target_id:
                self.current_target_id = None
    
    def _on_path_confirmed(self, path: ConfirmedPath) -> None:
        """Handle newly confirmed path."""
        print(f"[SENTRY] Path CONFIRMED! ID={path.path_id}, "
              f"Pass count={path.pass_count}, Confidence={path.confidence:.2f}")
        
        if path.ambush_point:
            print(f"         Ambush point: ({path.ambush_point[0]:.2f}, {path.ambush_point[1]:.2f})")
    
    # =========================================================================
    # CALLBACK REGISTRATION
    # =========================================================================
    
    def on_fire(self, callback: Callable[[FireCommand], None]) -> None:
        """Register callback for fire events."""
        self._fire_callbacks.append(callback)
    
    def on_turret_move(self, callback: Callable[[float, float], None]) -> None:
        """Register callback for turret movement."""
        self._turret_move_callbacks.append(callback)
        print(f"[SENTRY] Registered turret move callback (total: {len(self._turret_move_callbacks)})")
    
    def on_state_change(self, callback: Callable[[SentryState, SentryState], None]) -> None:
        """Register callback for state changes."""
        self._state_change_callbacks.append(callback)
    
    # =========================================================================
    # RENDERING
    # =========================================================================
    
    def _render_frame(self, frame: np.ndarray, timestamp: float) -> np.ndarray:
        """Render all overlays on frame."""
        return self.overlay.render(
            frame=frame,
            guard_point=self.config.guard_point,
            inner_radius=self.config.peripheral_inner_radius,
            outer_radius=self.config.peripheral_outer_radius,
            confirmed_paths=self.path_analyzer.confirmed_paths,
            pending_tracks=self.path_analyzer.pending_tracks,
            active_tracks=list(self.track_recorder.active_tracks.values()),
            kill_zones=[(x, y) for x, y, _ in self.path_analyzer.get_all_ambush_points()],
            predictions=self.predictor.last_predictions,
            tracked_targets=self.peripheral_sensor.targets,
            state_name=self.state.name,
            stats=self.get_stats() if self.config.show_debug_overlay else None
        )
    
    # =========================================================================
    # PERSISTENCE
    # =========================================================================
    
    def _save_tracks(self) -> None:
        """Save confirmed tracks to file."""
        try:
            save_path = Path(__file__).parent / "config" / "sentry_tracks.json"
            save_path.parent.mkdir(parents=True, exist_ok=True)
            
            data = {
                'saved_at': time.time(),
                'confirmed_paths': [
                    {
                        'path_id': p.path_id,
                        'pass_count': p.pass_count,
                        'ambush_point': p.ambush_point,
                        'confidence': p.confidence,
                        'entry_direction': p.entry_direction,
                        'track': p.representative_track.to_dict()
                    }
                    for p in self.path_analyzer.confirmed_paths
                ],
                'manual_ambush_points': self.path_analyzer.manual_ambush_points
            }
            
            with open(save_path, 'w') as f:
                json.dump(data, f, indent=2)
            
            print(f"[SENTRY] Saved {len(self.path_analyzer.confirmed_paths)} confirmed paths")
        except Exception as e:
            print(f"[SENTRY] Error saving tracks: {e}")
    
    def _load_persisted_tracks(self) -> None:
        """Load confirmed tracks from file."""
        try:
            load_path = Path(__file__).parent / "config" / "sentry_tracks.json"
            if not load_path.exists():
                return
            
            with open(load_path, 'r') as f:
                data = json.load(f)
            
            # Restore manual ambush points
            for point in data.get('manual_ambush_points', []):
                self.path_analyzer.add_manual_ambush_point(*point)
            
            print(f"[SENTRY] Loaded {len(data.get('confirmed_paths', []))} confirmed paths")
        except Exception as e:
            print(f"[SENTRY] Error loading tracks: {e}")
    
    # =========================================================================
    # STATS & INFO
    # =========================================================================
    
    def get_stats(self) -> dict:
        """Get comprehensive statistics."""
        return {
            'state': self.state.name,
            'fire_enabled': self.fire_enabled,
            'active_tracks': len(self.track_recorder.active_tracks),
            'confirmed_paths': len(self.path_analyzer.confirmed_paths),
            'pending_tracks': len(self.path_analyzer.pending_tracks),
            'peripheral_targets': len(self.peripheral_sensor.get_targets_in_peripheral()),
            'current_target': self.current_target_id,
            'ambush_points': len(self.path_analyzer.get_all_ambush_points()),
        }
    
    def get_state_name(self) -> str:
        """Get current state name."""
        return self.state.name
    
    def is_active(self) -> bool:
        """Check if sentry mode is active."""
        return self.state != SentryState.IDLE

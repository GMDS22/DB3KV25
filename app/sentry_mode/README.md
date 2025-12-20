# Sentry Ambush Mode

**Intelligent Guard Turret System for Predictive Target Engagement**

## Overview

Sentry Ambush Mode is an advanced tracking system that learns target movement patterns, identifies repeating paths, calculates optimal ambush points, and fires predictively based on trajectory prediction and time-to-arrival calculations.

Unlike traditional tracking modes that reactively follow targets, Sentry Mode uses a **proactive ambush strategy**:

1. **Learn** - Observe targets passing through the scene
2. **Identify** - Detect repeating movement patterns (tracks)
3. **Position** - Aim turret at optimal ambush point
4. **Predict** - Calculate when target will arrive at ambush point
5. **Intercept** - Fire at the exact moment of predicted arrival

---

## Key Features

### 🎯 Pattern Learning
- Records all target trajectories through the peripheral zone
- Uses Fréchet distance for path similarity comparison
- Automatically identifies repeating movement patterns
- Confirms tracks after 2+ observations of same pattern

### 🔮 Trajectory Prediction
- Kalman filter for smooth position/velocity estimation
- Calculates time-to-arrival at ambush points
- Computes lead time for mechanical delay compensation
- Confidence-based firing decisions

### 🛡️ Zone-Based Detection
- Configurable peripheral zone (ring around guard point)
- Separate kill zones at ambush points
- Event-driven zone transition detection
- Independent of main app's dead-zone logic

### 📊 Visual Overlays
- Peripheral zone boundary display
- Confirmed tracks drawn as colored paths
- Ambush points marked with crosshairs
- Prediction vectors and ETA countdown
- Confidence meters and state indicators

### 💾 Persistence
- Confirmed tracks saved to JSON
- Session continuity across restarts
- Manual ambush points preserved
- Auto-save at configurable intervals

### 🔫 Predictive Firing
- Fires based on trajectory prediction, NOT dead-zone
- Configurable fire window (before/after predicted arrival)
- Burst mode with configurable shot count and interval
- Mechanical delay compensation

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                       SENTRY CONTROLLER                             │
│                    (State Machine Orchestrator)                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────┐ │
│  │  TrackRecorder  │  │   PathAnalyzer  │  │ TrajectoryPredictor │ │
│  │                 │  │                 │  │                     │ │
│  │ • Record tracks │  │ • Cluster paths │  │ • Kalman filter     │ │
│  │ • Store history │  │ • Confirm patterns│ │ • Speed calculation │ │
│  │ • Calc velocity │  │ • Find ambush pts│ │ • Intercept timing  │ │
│  └────────┬────────┘  └────────┬────────┘  └──────────┬──────────┘ │
│           │                    │                      │            │
│           └────────────────────┼──────────────────────┘            │
│                                │                                   │
│  ┌─────────────────┐  ┌───────┴───────┐  ┌─────────────────────┐  │
│  │PeripheralSensor │  │ SentryOverlay │  │    ByteTracker      │  │
│  │                 │  │               │  │                     │  │
│  │ • Zone detection│  │ • Draw HUD    │  │ • Multi-object      │  │
│  │ • Entry/exit    │  │ • Tracks      │  │   tracking          │  │
│  │ • Fire auth     │  │ • Zones       │  │ • Persistent IDs    │  │
│  └─────────────────┘  └───────────────┘  └─────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## State Machine

```
                    ┌──────────────────────────────────────────┐
                    │                                          │
                    ▼                                          │
             ┌─────────────┐                                   │
     ┌──────▶│   LEARNING  │◀─────────────────────────────┐    │
     │       │  (studying) │                               │    │
     │       └──────┬──────┘                               │    │
     │              │                                      │    │
     │              │ 2+ passes confirmed                  │    │
     │              ▼                                      │    │
     │       ┌─────────────┐                               │    │
     │       │  WATCHING   │  Turret at ambush point       │    │
     │       │  (waiting)  │  Peripheral sensor active     │    │
     │       └──────┬──────┘                               │    │
     │              │                                      │    │
     │              │ Target enters, prediction confident  │    │
     │              ▼                                      │    │
     │       ┌─────────────┐                               │    │
     │       │   AIMING    │  Calculating intercept        │    │
     │       │ (predicting)│  Countdown to fire            │    │
     │       └──────┬──────┘                               │    │
     │              │                                      │    │
     │              │ Fire window reached                  │    │
     │              ▼                                      │    │
     │       ┌─────────────┐                               │    │
     │       │   FIRING    │  Execute fire command         │    │
     │       │             │  (burst if enabled)           │    │
     │       └──────┬──────┘                               │    │
     │              │                                      │    │
     │              │ Fire complete                        │    │
     │              ▼                                      │    │
     │       ┌─────────────┐                               │    │
     │       │  COOLDOWN   │  Brief delay                  │    │
     │       │             │                               │    │
     │       └──────┬──────┘                               │    │
     │              │                                      │    │
     │              └──────────────────────────────────────┘    │
     │                                                          │
     │  Timeout without action                                  │
     └──────────────────────────────────────────────────────────┘
```

---

## Module Reference

### `sentry_config.py`
Configuration dataclass with all tunable parameters:
- Zone geometry (guard point, peripheral radii, kill zone size)
- Learning thresholds (min passes, similarity threshold)
- Kalman filter settings
- Fire control (window, burst, lead time)
- Visualization colors and options

### `track_recorder.py`
Records and stores trajectory history:
- `TrackPoint`: Single point with position, velocity, timestamp
- `Track`: Complete trajectory for one object
- `TrackRecorder`: Manages all active and completed tracks

### `path_analyzer.py`
Analyzes tracks for repeating patterns:
- `ConfirmedPath`: Verified movement pattern with ambush point
- `PathAnalyzer`: Clusters tracks, calculates optimal ambush points
- Uses Fréchet distance for path similarity

### `trajectory_predictor.py`
Predicts target positions and intercept timing:
- `KalmanFilter2D`: Position/velocity estimation
- `TrajectoryPredictor`: Time-to-arrival, lead time calculation
- `PredictionResult`: Full prediction with confidence

### `peripheral_sensor.py`
Zone-based detection and event generation:
- `ZoneType`: OUTSIDE, PERIPHERAL, GUARD, KILL
- `ZoneEvent`: Zone crossing event
- `PeripheralSensor`: Tracks which zone each target is in

### `sentry_overlay.py`
HUD visualization:
- Draws zones, tracks, ambush points
- Prediction vectors and countdown
- State indicator and debug info

### `sentry_controller.py`
Main orchestrator:
- `SentryState`: State machine enum
- `FireCommand`: Fire action data
- `SentryController`: Coordinates all components

### `trackers/byte_tracker.py`
Bundled ByteTrack implementation:
- Multi-object tracking with persistent IDs
- Uses both high and low confidence detections
- IoU-based association

---

## Quick Start

### Standalone Testing

```bash
# Navigate to sentry_mode directory
cd app/sentry_mode

# Run with default camera and motion detection
python test_sentry_standalone.py

# Run with YOLO detection
python test_sentry_standalone.py --yolo path/to/yolov8n.pt

# Specify camera
python test_sentry_standalone.py --camera 1
```

### Controls (Standalone Test)

| Key | Action |
|-----|--------|
| `SPACE` | Toggle auto-fire enable |
| `G` | Set guard point (click after) |
| `A` | Add manual ambush point (click after) |
| `L` | Force learning mode |
| `W` | Force watching mode |
| `R` | Reset all tracks |
| `C` | Clear manual ambush points |
| `S` | Save configuration |
| `D` | Toggle debug overlay |
| `Q` / `ESC` | Quit |

### Integration with Main App

```python
from app.sentry_mode import SentryController, SentryConfig

# Create controller
config = SentryConfig()
sentry = SentryController(config)

# Register callbacks
sentry.on_fire(lambda cmd: send_fire_command(cmd))
sentry.on_turret_move(lambda pan, tilt: move_turret(pan, tilt))

# Start sentry mode
sentry.start()

# In your main loop:
def process_frame(frame, detections):
    # detections = [(track_id, x, y, w, h), ...]
    frame = sentry.update(detections, frame)
    return frame

# Stop when done
sentry.stop()
```

---

## Configuration Guide

### Zone Geometry

```python
# Guard point - center of attention (normalized 0.0-1.0)
guard_point = (0.5, 0.5)  # Center of frame

# Peripheral zone radii (normalized)
peripheral_inner_radius = 0.15  # 15% of frame
peripheral_outer_radius = 0.45  # 45% of frame

# Kill zone size around ambush points
kill_zone_radius = 0.08  # 8% of frame
```

### Learning Parameters

```python
# How many times a path must be observed to be confirmed
min_passes_to_confirm = 2

# How similar paths must be to match (lower = stricter)
path_similarity_threshold = 0.15

# How long to keep tracks in memory
track_expiry_seconds = 300.0  # 5 minutes
```

### Fire Control

```python
# Confidence required to fire
fire_confidence_threshold = 0.7

# Fire window around predicted arrival
fire_window_before = 0.05  # Fire 50ms early
fire_window_after = 0.10   # Allow 100ms late

# Burst settings
burst_enabled = True
burst_count = 3
burst_interval_ms = 50

# Mechanical delay compensation
mechanical_lead_time = 0.02  # 20ms
```

### Priority Methods

The `ambush_priority_method` setting determines which ambush point gets priority when multiple confirmed paths exist:

- `'frequency'` - Most frequently observed path
- `'recency'` - Most recently active path
- `'speed'` - Fastest targets (harder to hit manually)
- `'confidence'` - Highest prediction confidence

---

## How It Differs from Main App Tracking

| Aspect | Main App | Sentry Mode |
|--------|----------|-------------|
| **Strategy** | Reactive tracking | Proactive ambush |
| **Movement** | Continuous servo tracking | Static aim at ambush point |
| **Fire Trigger** | Dead-zone based (target centered) | Prediction based (target approaching) |
| **Learning** | No pattern learning | Learns repeating paths |
| **Multiple Targets** | Tracks single target | Monitors all, engages one |

---

## Files Structure

```
app/sentry_mode/
├── __init__.py                 # Module exports
├── sentry_config.py            # Configuration dataclass
├── sentry_controller.py        # Main orchestrator
├── track_recorder.py           # Trajectory recording
├── path_analyzer.py            # Pattern matching
├── trajectory_predictor.py     # Kalman filter & prediction
├── peripheral_sensor.py        # Zone detection
├── sentry_overlay.py           # HUD rendering
├── test_sentry_standalone.py   # Standalone test harness
├── README.md                   # This file
├── config/
│   ├── sentry_defaults.json    # Default configuration
│   └── sentry_tracks.json      # Persisted tracks (auto-created)
└── trackers/
    ├── __init__.py
    └── byte_tracker.py         # ByteTrack implementation
```

---

## Dependencies

**Required:**
- Python 3.8+
- NumPy
- OpenCV (cv2)

**Optional:**
- PyQt5 (for GUI test harness)
- Ultralytics (for YOLO detection)

All core sentry logic works without PyQt5 or YOLO - the test harness falls back to OpenCV-only mode with motion detection.

---

## Future Integration

When ready to integrate with the main turret app:

1. **Add as detection mode** in `turret_presets.py`
2. **Add UI controls** via `ui_builder.py` 
3. **Connect callbacks** in `MAIN_FILE_SINGLE_CAM.py`:
   - `on_fire()` → existing fire command system
   - `on_turret_move()` → existing servo control
4. **Add preset** for sentry-specific settings

The module is designed to be self-contained and drop-in ready.

---

## Troubleshooting

### "No tracks confirmed"
- Ensure targets are passing through the peripheral zone
- Check `min_passes_to_confirm` - default is 2
- Lower `path_similarity_threshold` if paths aren't matching

### "Fire not triggering"
- Verify fire is enabled (`controller.enable_fire()`)
- Check `fire_confidence_threshold` - lower if predictions aren't confident enough
- Ensure target is approaching an ambush point, not just passing through

### "Tracks expiring too fast"
- Increase `track_expiry_seconds`
- Enable `persist_tracks` to save across sessions

### "Predictions inaccurate"
- Adjust Kalman filter: lower `kalman_process_noise` for smoother predictions
- Increase `velocity_smoothing` for less jittery speed estimates

---

## License

Part of DB3000V4.1 Turret Control System.

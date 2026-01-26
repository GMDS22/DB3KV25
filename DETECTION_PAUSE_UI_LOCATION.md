# Detection Pause Feature - UI Location & Usage

## WHERE TO FIND IT

### Main Window Layout
```
┌─────────────────────────────────────────────────────────────┐
│  DB3000 Turret Control                                      │
├─────────────────┬───────────────────────┬───────────────────┤
│                 │                       │  TRACKING         │
│  LEFT PANEL     │   CAMERA VIEW         │  BEHAVIOR         │
│  (Detection,    │   (Center)            │  PANEL            │
│   Camera,       │                       │  ◄── HERE         │
│   Trigger)      │                       │                   │
│                 │                       │                   │
│                 │                       │  ┌──────────────┐ │
│                 │                       │  │ Tracking     │ │
│                 │                       │  │ Speed        │ │
│                 │                       │  ├──────────────┤ │
│                 │                       │  │ Deadzone     │ │
│                 │                       │  ├──────────────┤ │
│                 │                       │  │ Detection    │ │
│                 │                       │  │ Pause (ms) ◄─┼─ THIS SLIDER
│                 │                       │  │ [====|====]  │ │
│                 │                       │  │     1000     │ │
│                 │                       │  ├──────────────┤ │
│                 │                       │  │ Other        │ │
│                 │                       │  │ Settings...  │ │
│                 │                       │  └──────────────┘ │
└─────────────────┴───────────────────────┴───────────────────┘
```

### Step-by-Step Location
1. **Launch the app** (`run.py` or `MAIN_FILE_SINGLE_CAM.py`)
2. **Look at the RIGHT side** of the window
3. **Find the "Tracking Behavior" dock panel**
4. **Scroll down** if needed to see:
   - Tracking Speed slider
   - Deadzone slider
   - **Detection Pause (ms)** ← THIS IS IT
   - Other tracking settings below

### Visual Hierarchy (Vertical Order)
```
Tracking Behavior Panel:
├── Tracking Speed (0-100)
├── Deadzone (pixels)
├── Detection Pause (ms) ◄─── HERE (0-2000ms)
├── Trigger Cooldown
├── Aim Aggression
├── Final Approach Boost
├── Hold Behavior
└── ... other settings
```

## WHAT THE SLIDER DOES

**Label:** "Detection Pause (ms)"
**Range:** 0 - 2000 milliseconds
**Default:** 1000ms (1 second)
**Unit Display:** Shows current value next to slider (e.g., "1000")

### Behavior When Active
1. Target enters big scope circle → Detection pause **starts**
2. Yellow targeting dot **stops updating** for configured duration
3. **Video continues playing** (NOT frozen)
4. Pan/tilt servos **continue aiming** to last known yellow-dot position
5. After pause expires → Detection **resumes** normally

### Use Cases
- **Problem:** Target jitters when near center, causing pan/tilt to oscillate
- **Solution:** Set pause to 1000-1500ms so servos can settle before firing
- **Problem:** Quick moving targets need faster response
- **Solution:** Set pause to 0-500ms for minimal delay

## SETTINGS PERSISTENCE

**File:** `settings.json` (workspace root)
**Key:** `"detection_pause_ms": 1000`
**Type:** Integer (milliseconds)
**Saved:** Automatically when slider moves

Example `settings.json` entry:
```json
{
  "detection_pause_ms": 1000,
  "deadzone": 40,
  "tracking_speed": 84,
  ...
}
```

## TOOLTIP (Hover Over Slider)
```
When target enters the big scope circle, pause detection updates for this 
duration. Video continues playing - only detection is paused so pan/tilt 
can precisely center the target before firing.
```

## INTERACTION WITH OTHER FEATURES

### Works With
- ✅ All detection modes (0-9, including YOLO, Frame Diff, Color)
- ✅ Sentry Mode (pause applies during predictive tracking)
- ✅ Autotracking + Autorecord
- ✅ Manual override (pause disabled during manual control)

### Does NOT Affect
- ❌ Video frame rate (video continues smoothly)
- ❌ Recording frame rate (recording continues normally)
- ❌ Manual keyboard control (pause only applies during auto-detection)
- ❌ Tilt safety checks (safety always active)

## TECHNICAL DETAILS

### Code Locations
- **UI Construction:** `app/ui_builder.py` lines ~1150-1200
- **Detection Logic:** `app/MAIN_FILE_SINGLE_CAM.py` lines ~18480-18520
- **State Variables:**
  - `self.detection_pause_ms` - Configured pause duration
  - `self._detection_pause_until` - Timestamp when pause expires
  - `self._was_in_scope` - Track scope entry for edge detection

### Pause Trigger Condition
```python
# Target enters scope when distance < scope_radius
scope_radius = min(frame_height, frame_width) * (scope_radius_pct / 100.0)
dist_to_center = sqrt((cx - center_x)^2 + (cy - center_y)^2)
in_scope = (dist_to_center <= scope_radius)

# Pause starts on scope entry (transition from outside to inside)
if in_scope and not was_in_scope:
    pause_until = now + (detection_pause_ms / 1000.0)
```

### Pause Active Check
```python
# Skip detection update if currently paused
if time.time() < self._detection_pause_until:
    # Keep using last known target position
    pass  # Don't update last_target_center
else:
    # Update normally
    self.last_target_center = (cx, cy)
```

## TROUBLESHOOTING

### Slider Not Visible
1. Check "Tracking Behavior" dock is open: `View → Widgets → Tracking Behavior`
2. Scroll down inside the panel (panel may be taller than visible area)
3. Reset layout: `View → Reset Layout` then restart app

### Pause Not Working
1. Verify slider value > 0 (value shown next to slider)
2. Enable tracking: Click "Start Tracking" button
3. Check target actually enters scope circle (see yellow ring in view)
4. Disable manual override (release keyboard control)

### Pause Too Short/Long
- **Too aggressive:** Increase to 1500-2000ms
- **Too sluggish:** Decrease to 500-800ms
- **Instant fire desired:** Set to 0ms (disables pause)

## CHANGELOG
- **2026-01-26:** Feature implemented (replaces old "Scope Settle Pause" concept)
- **2026-01-26:** Renamed from `scope_entry_freeze` to `detection_pause` for clarity
- **2026-01-26:** Added proper load/save persistence and UI visibility

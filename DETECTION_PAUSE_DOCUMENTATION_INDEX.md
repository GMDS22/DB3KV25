# Detection Pause Feature - Complete Documentation Index

**Feature:** Detection Pause (Tracking Behavior Control)  
**Version:** 1.0  
**Date:** 2026-01-26

---

## Quick Reference

**UI Location:** Tracking Behavior Panel (Right Dock) → "Detection Pause (ms)" slider  
**Range:** 0-2000 milliseconds  
**Default:** 1000ms (1 second)  
**Settings Key:** `detection_pause_ms` in `settings.json`

---

## Documentation Files

### 1. **DETECTION_PAUSE_UI_LOCATION.md**
Complete user guide with:
- Visual UI layout diagrams
- Step-by-step location instructions
- Behavior description and use cases
- Settings persistence details
- Troubleshooting guide
- Technical implementation details

### 2. **CHANGE_IMPACT_REFERENCE.md**
Developer/agent reference with:
- Subsystem impact analysis
- Critical invariants
- Integration points with other features
- State variables and code locations
- Affected files list

### 3. **README.md**
Quick overview section:
- Feature summary
- Key behaviors
- UI location
- Settings persistence
- Link to detailed documentation

### 4. **RECENT_UPDATES.json**
Changelog entry:
```json
{
  "date": "2026-01-26",
  "title": "Detection Pause feature: pause detection updates (not video) when target enters scope circle. Configurable 0-2000ms (default 1s), allows pan/tilt to precisely center target before firing. Video continues playing smoothly."
}
```

---

## Code Locations

### UI Construction
**File:** `app/ui_builder.py`  
**Lines:** ~1150-1200  
**Widgets:**
- `detection_pause_slider` (QSlider, 0-2000 range)
- `detection_pause_label` (QLabel, displays current value)

### Detection Logic
**File:** `app/MAIN_FILE_SINGLE_CAM.py`

**State Initialization (line ~1689):**
```python
self.detection_pause_ms = 1000
self._detection_pause_until = 0.0
self._was_in_scope = False
```

**Load Settings (line ~11685):**
```python
self.detection_pause_ms = int(settings.get("detection_pause_ms", 1000))
# Update UI widgets
```

**Save Settings (line ~12050):**
```python
"detection_pause_ms": val("detection_pause_slider", 1000),
```

**Pause Logic (lines ~18480-18520):**
```python
# Detect scope entry
if in_scope and not self._was_in_scope:
    self._detection_pause_until = now + (pause_ms / 1000.0)

# Skip detection update if paused
if time.time() < self._detection_pause_until:
    pass  # Keep using last_target_center
else:
    self.last_target_center = (cx, cy)
```

---

## Feature Behavior Flow

```
┌─────────────────────────────────────────────────┐
│ 1. Target detected outside scope circle        │
│    → Normal tracking, detection updates        │
└──────────────────┬──────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────┐
│ 2. Target ENTERS scope circle (edge detected)  │
│    → Pause starts: _detection_pause_until set  │
└──────────────────┬──────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────┐
│ 3. During pause (time < pause_until)           │
│    → Detection updates SKIPPED                 │
│    → last_target_center FROZEN                 │
│    → Video continues playing                   │
│    → Servos continue aiming to frozen position │
└──────────────────┬──────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────┐
│ 4. Pause expires (time >= pause_until)         │
│    → Detection updates RESUME                  │
│    → Normal tracking continues                 │
└─────────────────────────────────────────────────┘
```

---

## Integration with Other Features

### ✅ Compatible With
- All detection modes (0-9): YOLO, Frame Diff, Background Sub, Color Detection
- Sentry Mode: Pause applies during predictive tracking
- Autotracking: Pause works during auto-tracking sessions
- Autorecord: Recording continues unaffected during pause
- All trigger modes: Water/Projectile, Safety, Cooldown

### ❌ Disabled When
- Manual override active (keyboard control)
- Manual suppression active
- Tracking stopped

### 🔄 Interactions
- **Deadzone:** Pause helps servos reach deadzone before firing
- **Tracking Speed:** Faster speed benefits from longer pause
- **Aim Aggression:** Works with aggressive aiming profiles
- **Quick Strike:** Pause allows single decisive move to succeed

---

## Settings Persistence Example

**File:** `settings.json` (workspace root)

```json
{
  "detection_pause_ms": 1500,
  "deadzone": 40,
  "tracking_speed": 84,
  "scope_radius_pct": 50,
  "autorecord": false,
  ...
}
```

---

## Troubleshooting Checklist

### Slider Not Visible
1. ☐ Check "Tracking Behavior" dock is open: `View → Widgets → Tracking Behavior`
2. ☐ Scroll down in panel (may be below visible area)
3. ☐ Try `View → Reset Layout` then restart

### Pause Not Working
1. ☐ Verify slider value > 0 (shown next to slider)
2. ☐ Enable tracking: Click "Start Tracking"
3. ☐ Target must actually enter scope circle (big yellow ring)
4. ☐ Disable manual override (release keyboard control)
5. ☐ Check scope_radius_pct setting (default 50%)

### Pause Too Short/Long
- **Too aggressive:** Increase to 1500-2000ms
- **Too sluggish:** Decrease to 500-800ms  
- **No pause wanted:** Set to 0ms

### Video Freezing (Should NOT Happen)
If video freezes, this is a BUG (detection pause should NOT freeze video):
1. Report issue with steps to reproduce
2. Temporary workaround: Set detection_pause_ms to 0

---

## Test Validation

**Test File:** None currently (feature relies on integration tests)  
**Validation Steps:**
1. Launch app with test_app_start.py ✅
2. Verify slider present in Tracking Behavior panel ✅
3. Adjust slider, check settings.json persistence ✅
4. Enable tracking, move target into scope circle
5. Confirm detection pauses, video continues
6. Confirm servos continue aiming to frozen position

---

## Version History

**v1.0 (2026-01-26):**
- Initial implementation
- UI slider in Tracking Behavior panel
- Load/save settings persistence
- Edge detection for scope entry
- Documentation complete (this file + DETECTION_PAUSE_UI_LOCATION.md + CHANGE_IMPACT_REFERENCE.md)

---

## Future Enhancements (Not Yet Implemented)

- [ ] Visual indicator when pause is active (HUD overlay)
- [ ] Separate pause duration for Sentry Mode
- [ ] Configurable trigger condition (scope entry vs deadzone entry vs custom radius)
- [ ] Pause counter/statistics in debug mode
- [ ] Test script for detection pause behavior validation

---

## Related Features

- **Scope Radius %:** Defines big scope circle size (affects pause trigger)
- **Deadzone:** Target area for firing eligibility
- **Tracking Speed:** Servo movement rate during tracking
- **Aim Aggression:** Auto Strike single-movement behavior
- **Quick Strike:** Manual trigger during tracking hold

---

## Contact & Support

For issues or questions about Detection Pause:
1. Check `DETECTION_PAUSE_UI_LOCATION.md` troubleshooting section
2. Review `CHANGE_IMPACT_REFERENCE.md` for technical details
3. Check `RECENT_UPDATES.json` for latest changes
4. Submit issue with reproduction steps if bug found

# PIR Guard Quick Start Guide

## Feature Summary
3-sensor blind-spot motion detection with adaptive turret search when no target confirmed. Uses existing Smart Sentry v2 guard mode.

## Enabling PIR Guard

### Step 1: Open Smart Sentry v2
- Launch the main DADBOT app
- Switch to **Smart Sentry v2** tab
- Click the **Guard** settings tab

### Step 2: Enable PIR Master Switch
- Find **"PIR Guard (Blind-Spot Detection)"** panel
- Check **"Enable PIR sensors"** checkbox
- UI will show 3 sensor configuration rows

### Step 3: Configure Each Sensor
For each sensor (1, 2, 3):
1. Check **"Active"** checkbox to enable that sensor
2. Set **Pan** angle (0-270°) where sensor covers
   - 270° = left rear
   - 150° = front left
   - 30° = front right
3. Set **Tilt** angle (0-110°) for that sensor
   - 15° = slightly upward from center
4. Leave **Debounce** at default (200ms minimum between fires)

### Step 4: Configure Scan Behavior
- **Scan Pan Range**: Width of area to search left/right (default 25°)
- **Scan Tilt Range**: Height of area to search up/down (default 15°)
- **Grid Resolution**: How many points to scan (3-4 recommended, higher = slower but thorough)
- **Scan Speed**: How fast to move between scan points (12°/s default)
- **Confirmation Timeout**: How long to wait at cue point before starting scan (1.0s default)
- Check **"Scan on No-Detection"** to auto-search if target not found at cue

### Step 5: Test
- Wave hand in front of each sensor
- Turret should slew to that sensor's cue angle
- If no target found, turret will run scan grid
- If target appears during scan, it will engage normally
- If scan times out, returns to guard patrol

## Behavior Explained

### What Happens When PIR Fires

```
1. PIR sensor detects motion
   ↓
2. Debounce check (minimum 200ms since last fire)
   ↓
3. Turret slews to sensor's configured Pan/Tilt cue angles
   ↓
4. Wait "Confirmation Timeout" seconds for camera to find target
   ↓
5a. Target found → Engage normally (fire automatically if rules allow)
   ↓
5b. No target found AND "Scan on No-Detection" enabled
    ↓
    Run adaptive scan grid around cue point
    ↓
    a) Target found during scan → Engage normally
    b) Scan completes → Return to guard patrol
```

## Default Sensor Setup (If You Don't Change Angles)

| Sensor | Pan | Tilt | Coverage |
|--------|-----|------|----------|
| 1 | 270° | 15° | Left rear |
| 2 | 150° | 15° | Front left |
| 3 | 30° | 15° | Front right |

This covers ~270° around the turret base. Adjust angles to match where your actual sensors are mounted.

## Scan Grid Example

With **Grid Resolution = 3** and **Scan Pan Range = 25°, Tilt Range = 15°**:

Turret will scan a 3×3 grid (9 points) around the cue point:
```
      TL    TM    TR
      .     .     .
      ML    MC    MR
      .     .     .
      BL    BM    BR
```

Each point gets held for ~250ms while camera looks for targets. Total scan time ~2-3 seconds.

## Tuning Tips

### Slow/Thorough Search (Rats)
- Grid Resolution: 5-6 (detailed grid)
- Scan Speed: 6-9 deg/s (slower movement)
- Grid Range: Full range (30° × 20°)

### Fast/Broad Search (Larger Animals)
- Grid Resolution: 2-3 (coarse grid)
- Scan Speed: 15-25 deg/s (faster movement)
- Grid Range: Smaller (15° × 10°)

### Conservative (Wait Longer for Camera)
- Confirmation Timeout: 2-3 seconds
- Scan On No-Detect: Disabled (return to patrol instead)

### Aggressive (Quick Search)
- Confirmation Timeout: 0.5 seconds
- Scan On No-Detect: Enabled
- Grid Resolution: 2

## Configuration File Location

Settings saved automatically to:
```
app/config/sentry_v2_settings.json
```

To reset PIR settings to defaults:
1. Close the app
2. Open `sentry_v2_settings.json`
3. Delete or clear the `"pir_guard"` section
4. Save and restart app

## Troubleshooting

### Turret Not Moving When I Wave Hand
- [ ] Check "Enable PIR sensors" is checked
- [ ] Check that sensor's "Active" checkbox is enabled
- [ ] Verify Pan/Tilt angles are within valid range (0-270° and 0-110°)
- [ ] Make sure turret is in GUARDING state (not ENGAGING or RETURNING)
- [ ] Check that motion is detected in front of the sensor

### Turret Keeps Returning to Patrol
- [ ] Check "Scan on No-Detection" is enabled if you want scanning
- [ ] Reduce "Confirmation Timeout" so it starts scanning sooner
- [ ] Increase "Grid Resolution" to check more points

### Turret Scans Too Slowly
- [ ] Increase "Scan Speed" (12-20 deg/s is typical)
- [ ] Decrease "Grid Resolution" (2-3 is fast)
- [ ] Decrease "Scan Pan/Tilt Range" to cover less area

### Turret Scans Too Fast
- [ ] Decrease "Scan Speed"
- [ ] Increase "Grid Resolution"
- [ ] Settings persist, so restart app if you want to reset

## FAQ

**Q: Do I need PIR sensors to use Smart Sentry?**
A: No. PIR is optional and defaults to OFF. Everything works normally without sensors.

**Q: Can I use different types of sensors?**
A: Not yet. Current implementation is hardcoded for PIR motion sensors. Future versions could support LD2450 mmWave, lidar, or other sensor types.

**Q: How many sensors can I have?**
A: Currently 3 sensors maximum (fixed in code). Can be expanded to support more if needed.

**Q: What happens if a sensor disconnects?**
A: Smart Sentry ignores missing data. If no PIR event is received, turret performs normal guard patrol.

**Q: Can PIR events interrupt an active engagement?**
A: No. PIR only affects the GUARDING state. If turret is already firing, PIR is ignored.

**Q: Does PIR work with all detection modes?**
A: Yes. PIR is independent of detection mode (YOLO, color, difference, etc.). The scan grid uses whatever detector is currently active.

## Next Steps After Setup

1. **Mount Sensors**: Install 3 PIR sensors around turret base at angles matching your software config
2. **Calibrate Angles**: Adjust Pan/Tilt values until turret points at each sensor's center
3. **Test Event**: Trigger each sensor with hand motion, verify turret response
4. **Tune Grid**: Adjust grid resolution and scan speed for your target animal type
5. **Monitor Logs**: Watch engagement log to see how often PIR cues result in actual engagements
6. **Iterate**: Adjust timeout/range based on false alarm rate

---

**Need Help?** Check the full implementation document: `PIR_GUARD_IMPLEMENTATION_COMPLETE.md`

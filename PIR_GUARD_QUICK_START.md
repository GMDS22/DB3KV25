# PIR Guard Quick Start Guide

## Feature Summary
3-sensor blind-spot motion detection with cue-first confirmation, a short cue hold, and a localized hunt around the triggered zone when no target is confirmed at the cue point. Uses the live Smart Sentry v2.3.2 Guard workflow.

For the full editor-facing behavior contract that also covers visual target tracking, target-loss reacquire, preset intent, and fire gating, read `SMART_SENTRY_AUTOTRACKING_BEHAVIOR_BLUEPRINT.md`.

## Enabling PIR Guard

### Step 1: Open Smart Sentry v2
- Launch Smart Sentry v2 from its standalone launcher
- Click the **Guard** settings tab

### Step 2: Enable PIR Master Switch
- Find **"PIR Guard (Blind-Spot Detection)"** panel
- Check **"Enable PIR sensors"** checkbox
- UI will show 3 sensor configuration rows

### Step 3: Configure Each Sensor
For each sensor (1, 2, 3):
1. Check **"Active"** checkbox to enable that sensor
2. Set **Pan** angle (0-270°) where sensor covers
   - Current default 3-zone layout is 45°, 135°, 225° across the 0-270° arc
   - Adjust these to match your actual physical mounting
3. Set **Tilt** angle (0-110°) for that sensor
   - Current default is 35° for each zone
4. Leave **Debounce** at the default unless you are chasing repeat-trigger noise
   - Current default is 500 ms per sensor

### Step 4: Configure Scan Behavior
- **Scan Pan Range**: Width of area to search left/right from the cue point (current default 45°)
- **Scan Tilt Range**: Height of area to search up/down (current default 45°)
- **Grid Resolution**: How many points to scan per axis (current default 3, so a 3x3 grid)
- **Scan Speed**: How fast to move between scan points (12°/s default)
- **Cue Hold**: How long to stay at the exact cue point before leaving it for the local hunt (current default 0.18 s)
- **Confirmation Timeout**: Broader PIR confirmation budget (current default 1.2 s)
- **Search Style**: `Hunting` for a more careful local-zone search first, or `Fast Reacquire` for less dwell and quicker widening
- **Hunt Rounds**: Shared number of hunt passes used by PIR and target-loss recovery (current default 1)
- Check **"Scan on No-Detection"** to auto-search if target not found at cue

### Step 5: Test
- Wave hand in front of each sensor
- Turret should slew to that sensor's cue angle
- If no target is found at the cue point, the turret should immediately start an offset scan move
- If target appears during scan, it will engage normally
- If scan completes without a target, current builds immediately command the configured guard/home position

## Behavior Explained

### What Happens When PIR Fires

```
1. PIR sensor detects motion
   ↓
2. Debounce check (minimum 200ms since last fire)
   ↓
3. Turret slews to sensor's configured Pan/Tilt cue angles
   ↓
4. Wait the short "Cue Hold" time for camera confirmation at the exact cue point
   ↓
5a. Target found → Engage normally (fire automatically if rules allow)
   ↓
5b. No target found AND "Scan on No-Detection" enabled
    ↓
    Run localized hunt around cue point, then widen through the PIR zone
    ↓
    a) Target found during scan → Engage normally
   b) Scan completes → Return to configured guard/home position
```

Important live behavior detail:

- The cue point already covers the center of the search area.
- In current builds, the first scan move after a no-detect is the first offset point, not the center again.
- The early hunt points stay close to the triggered zone before the wider search fans out.
- `Cue Hold` is the intentional wait before the hunt. There is no intentional stationary wait after the hunt completes.
- If you do not see a visible offset move, either `Cue Hold` is still too high for your preference, `Scan on No-Detection` is off, or you are on an older build.

## Default Sensor Setup (If You Don't Change Angles)

| Sensor | Pan | Tilt | Coverage |
|--------|-----|------|----------|
| 1 | 45° | 35° | Right zone |
| 2 | 135° | 35° | Front zone |
| 3 | 225° | 35° | Left zone |

This covers the full 0-270° pan arc with three equal 90° sectors. Adjust angles to match where your actual sensors are mounted.

## Scan Grid Example

With **Grid Resolution = 3** and **Scan Pan Range = 45°, Tilt Range = 45°**:

Turret will scan a 3×3 grid (9 points) around the cue point:
```
      TL    TM    TR
      .     .     .
      ML    MC    MR
      .     .     .
      BL    BM    BR
```

Current live behavior visits the cue center during the confirmation phase, then begins the scan from one of the offset points. Total scan time depends on your scan speed, settle time, and grid size.

## Tuning Tips

### Slow/Thorough Search (Rats)
- Grid Resolution: 5-6 (detailed grid)
- Scan Speed: 6-9 deg/s (slower movement)
- Grid Range: Full range (30° × 20°)

### Fast/Broad Search (Larger Animals)
- Grid Resolution: 2-3 (coarse grid)
- Scan Speed: 15-25 deg/s (faster movement)
- Grid Range: Smaller (15° × 10°)

### Conservative (Wait Longer At Cue)
- Cue Hold: 0.25-0.40 seconds
- Confirmation Timeout: 1.2-2.0 seconds
- Scan On No-Detect: Disabled (return to guard/home instead of scanning)

Important: if you are trying to remove a pause after the PIR hunt finishes, do not look for a separate post-hunt dwell setting. That pause is not an intended feature. Reduce `Cue Hold` only for the pre-hunt wait, and update to a build with the explicit return-home fix if the turret still stays parked after a completed no-target hunt.

### Aggressive (Quick Search)
- Cue Hold: 0.08-0.14 seconds
- Search Style: Fast Reacquire
- Scan On No-Detect: Enabled
- Grid Resolution: 2

## Configuration File Location

Settings saved automatically to:
```
app/config/smart_sentry_v2_3_2_settings.json
```

To reset PIR settings to defaults:
1. Close the app
2. Open `smart_sentry_v2_3_2_settings.json`
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
- [ ] Reduce "Cue Hold" so it leaves the cue sooner
- [ ] Increase "Grid Resolution" to check more points

### Turret Slews to Cue But Search Still Looks Motionless
- [ ] Confirm `Scan on No-Detection` is enabled
- [ ] Confirm your build includes the updated offset-first scan behavior
- [ ] Increase `Scan Pan Range` slightly if your offsets are too small to notice
- [ ] Lower `Cue Hold` if you want the offset hunt to begin sooner
- [ ] Use `Fast Reacquire` if you want less dwell and quicker widening

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
A: PIR cues do not hijack a confirmed active engagement. Current Smart Sentry behavior queues or defers PIR-driven work so blind-spot sensing remains available without abruptly stealing control from an existing camera-confirmed target.

**Q: Does PIR work with all detection modes?**
A: Yes. PIR is independent of detection mode (YOLO, color, difference, etc.). The scan grid uses whatever detector is currently active.

**Q: Why does the turret move to the cue point first and only then search?**
A: That is the intended live contract. PIR is treated as a blind-spot cue, not a target confirmation. Smart Sentry first checks the configured cue point briefly, then starts a local hunt around that zone only if the camera still sees nothing.

## Next Steps After Setup

1. **Mount Sensors**: Install 3 PIR sensors around turret base at angles matching your software config
2. **Calibrate Angles**: Adjust Pan/Tilt values until turret points at each sensor's center
3. **Test Event**: Trigger each sensor with hand motion, verify turret response
4. **Tune Grid**: Adjust grid resolution and scan speed for your target animal type
5. **Monitor Logs**: Watch engagement log to see how often PIR cues result in actual engagements
6. **Iterate**: Adjust timeout/range based on false alarm rate

---

**Need Help?** Check the full implementation document: `PIR_GUARD_IMPLEMENTATION_COMPLETE.md`

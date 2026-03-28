"""
PRECISION AIMING TUNING GUIDE

Your turret exhibits two symptoms:
1. Sometimes OVERSHOOTS a lot (moves past target)
2. Sometimes NAILS micro-adjustments (precise lock)

This guide shows how to diagnose and fix what's happening.

═══════════════════════════════════════════════════════════════════════════════
STEP 1: ENABLE LOGGING AND CAPTURE DATA
═══════════════════════════════════════════════════════════════════════════════

Current workflow:
  1. Run app with sentry enabled
  2. Point at targets, fire a few engagements
  3. App auto-logs to: logs/precision_tuning/precision_tuning_TIMESTAMP.csv
  4. After running, reload CSV in Excel or Python
  5. Analyze patterns, adjust settings, test again

To enable detailed logging:
  - Run app normally
  - Engage targets in the same detection mode multiple times
  - Each engagement generates one row per frame
  - After 5-10 engagements, export CSV (see bottom of sentry log tab for export button)

═══════════════════════════════════════════════════════════════════════════════
STEP 2: INTERPRET THE CSV LOGS
═══════════════════════════════════════════════════════════════════════════════

Key Columns:
  
  error_pan_deg, error_tilt_deg
    → Angle between turret and target (positive = need to move right/up)
    → Goal: Keep this close to 0°
  
  phase
    → "aim" = snap-aim (fast movement to target)
    → "precision" = fine-tuning (PID corrections)
    → "fire" = holding aim steady while firing
  
  pid_p_pan, pid_d_pan
    → P = Proportional (how much to correct per degree of error)
    → D = Derivative (damping to prevent overshoot)
    → If P is large but D is small → overshoot
    → If D is large but P is small → sluggish/slow-to-lock
  
  overshoot_pan, overshoot_tilt
    → True = turret is moving AWAY from target (bad!)
    → Count per engagement: High % = Kp too high or Kd too low
  
  lock_stable
    → True = target held within deadzone (good!)
    → Goal: High % during "fire" phase (>80%)
  
  within_deadzone
    → True = close enough to target (no more corrections needed)
    → Goal: Happen before "fire" phase

═══════════════════════════════════════════════════════════════════════════════
DIAGNOSE YOUR PROBLEM
═══════════════════════════════════════════════════════════════════════════════

SYMPTOM A: "OVERSHOOTS A LOT"
  Indicators in logs:
    - overshoot_pan / overshoot_tilt are True for many frames
    - overshoot_percent > 30%
    - error_pan_deg swings from -2° to +3° to -1° (oscillation)
  
  Root Causes & Fixes:
    1. Kp (precision_kp) is too high
       → Turret moves too aggressively for small errors
       → FIX: Reduce precision_kp from 0.035 to 0.025, retest
    
    2. Kd (precision_kd) is too low
       → Not enough damping to prevent overshoot
       → FIX: Increase precision_kd from 0.01 to 0.015, retest
    
    3. precision_max_step too high
       → Single frame movement is too large
       → FIX: Reduce precision_max_pan_step from 0.90 to 0.65
       → Or: precision_max_tilt_step from 0.75 to 0.55

SYMPTOM B: "MICRO-ADJUSTS PERFECTLY (BUT NOT ALWAYS)"
  Indicators in logs:
    - lock_stable = True for most frames
    - within_deadzone = True before firing
    - overshoots are rare but do happen occasionally
  
  Root Cause: Settings are mostly right, but servo has latency
    → Sometimes target moves before servo catches up
    → Sometimes servo overshoots because of inertia
  
  FIX: Add slight damping where missing
    - If only Tilt overshoots: increase precision_kd slightly (0.01 → 0.012)
    - If only Pan overshoots: adjust precision_reversal_brake (0.30 → 0.25)

═══════════════════════════════════════════════════════════════════════════════
STEP 3: ADJUSTING PARAMETERS
═══════════════════════════════════════════════════════════════════════════════

Location: UI Detection Tab → Advanced (scroll down)
           Or config file: app/config/sentry_v2_settings.json

Parameters (in order of tuning priority):

  1. precision_kp (proportional gain) — MOST IMPORTANT
     Default: 0.035
     Symptom → Fix:
       - Turret too slow to catch target
         → INCREASE Kp (try 0.045)
       - Turret overshoots/oscillates
         → DECREASE Kp (try 0.025)
     Range: 0.015 — 0.060
  
  2. precision_kd (derivative gain) — DAMPING
     Default: 0.01
     Symptom → Fix:
       - Lots of overshoot (swinging past target)
         → INCREASE Kd (try 0.015)
       - Micro-oscillations near target
         → INCREASE Kd (try 0.012)
     Range: 0.005 — 0.025
  
  3. precision_deadzone_pan_deg / precision_deadzone_tilt_deg
     Default: 0.18° (pan), 0.15° (tilt)
     Symptom → Fix:
       - Jitter near target (tiny back-and-forth)
         → INCREASE deadzone (try 0.22°, 0.18°)
       - Target drifts away from aim (not holding)
         → DECREASE deadzone (try 0.14°, 0.12°)
     Range: 0.08° — 0.30°
  
  4. precision_reversal_brake — PREVENTS OSCILLATION
     Default: 0.30
     Meaning: When direction reverses (overshoot detected), 
              reduce integral by 30%
     Symptom → Fix:
       - Oscillation after reaching target
         → INCREASE value (try 0.20, meaning 80% damping)
       - Target slips during micro-corrections
         → DECREASE value (try 0.35)
     Range: 0.15 — 0.50
  
  5. precision_max_pan_step / precision_max_tilt_step
     Default: 0.90° (pan), 0.75° (tilt)
     Symptom → Fix:
       - Overshoots wildly (big jumps past target)
         → DECREASE both (try 0.60, 0.50)
       - Creeps toward target too slowly
         → INCREASE both (try 1.0, 0.85)
     Range: 0.40° — 1.20°
  
  6. precision_ki (integral gain) — RARELY NEEDED
     Default: 0.0 (disabled)
     Only enable if error steadily drifts and never reaches zero
     Symptom → Fix:
       - Slight bias (always 0.5° off target)
         → Enable Ki: change from 0.0 to 0.002
     Caution: High Ki causes lag and oscillation!
       → Keep <= 0.005 if enabled

═══════════════════════════════════════════════════════════════════════════════
STEP 4: QUICK TUNING CHECKLIST
═══════════════════════════════════════════════════════════════════════════════

After each change:
  1. Test on target 3-5 times (same distance, lighting)
  2. Export logs (it's automatic)
  3. Check summary:
     - Are overshoots reduced? (aim for <10%)
     - Is lock time faster? (first deadzone hit should be ~50-150ms)
     - Do you fire more accurately? (test by hitting actual targets)

Target Thresholds for Good Precision:
  - Overshoot: <10% of frames
  - Lock stable: >75% during "fire" phase
  - Average error at lock: <0.3°
  - Lock time (enter deadzone): <200ms from phase start

═══════════════════════════════════════════════════════════════════════════════
STEP 5: DETECT-MODE-SPECIFIC TUNING
═══════════════════════════════════════════════════════════════════════════════

Different detection modes may need different precision settings because:
  - Mode 6 (Color) can drift in lighting changes → needs higher deadzone
  - Mode 9 (Color+YOLO) is more stable → can use tighter deadzone
  - Mode 10 (Motion-Locked) bounding boxes change size → may need Kp adjustment

If you notice precision is good in Mode 9 but bad in Mode 7:
  1. Run logs side-by-side for each mode
  2. Note which parameter differs most (e.g., error magnitude is 3x higher in Mode 7)
  3. Adjust precision settings BEFORE switching modes in UI
     → (Or use "Method Presets" to save mode-specific precision settings)

═══════════════════════════════════════════════════════════════════════════════
STEP 6: ADVANCED DEBUGGING
═══════════════════════════════════════════════════════════════════════════════

If tuning Kp/Kd doesn't help, check these:

A. Servo Lag / Response Time
   Indicators: Constant delay between command and actual movement
   Check: precision_settle_time (default 0.4s)
   → If servo takes 0.2s to respond, increase settle_time to 0.5s

B. Target Instability
   Indicators: error_magnitude swinging 0.5° → 1.5° → 0.2° randomly
   Check: Is detection stable?
   → Run same test in Mode 10 (motion-locked) vs Mode 9 (color+YOLO)
   → If Mode 10 is more stable, detector is noisy → tune detection mode first

C. Sensor Resolution
   Indicators: Error always a multiple of 0.25° (coarse quantization)
   Check: Camera resolution vs frame size
   → May need to increase engagement_speed to get finer control

═══════════════════════════════════════════════════════════════════════════════
EXAMPLE WORKFLOW
═══════════════════════════════════════════════════════════════════════════════

Session 1: Baseline
  1. Run app, 5 engagements on stationary 1-meter target
  2. Export: overshoot_percent = 35%, lock_stable = 65%
  3. Observation: Lots of oscillation
  
  Decision: Overshooting → reduce Kp and increase Kd
  Changes:
    - precision_kp: 0.035 → 0.028
    - precision_kd: 0.01 → 0.013
  
  Save, retest

Session 2: After first tuning
  1. Run app, 5 engagements on same target
  2. Export: overshoot_percent = 18%, lock_stable = 82%
  3. Observation: Much better, but still some jitter at end
  
  Decision: Deadzone too tight causing rapid back-and-forth
  Changes:
    - precision_deadzone_pan_deg: 0.18 → 0.20
  
  Save, retest

Session 3: Dial in
  1. Run app, 5 engagements
  2. Export: overshoot_percent = 8%, lock_stable = 88%
  3. Observation: Stable lock, precise aim
  
  ✓ DONE — Save this configuration as your baseline
     (You can now adjust per-mode if needed)

═══════════════════════════════════════════════════════════════════════════════
EXPORT & ANALYZE LOGS (PYTHON)
═══════════════════════════════════════════════════════════════════════════════

After running, open Python in the workspace:

    import pandas as pd
    
    # Load latest CSV
    df = pd.read_csv('logs/precision_tuning/precision_tuning_LATEST.csv')
    
    # Summary stats
    print("Overshoot %:", (df['overshoot_pan'] | df['overshoot_tilt']).sum() / len(df) * 100)
    print("Lock stable %:", df['lock_stable'].sum() / len(df) * 100)
    print("Avg error:", df['error_magnitude_deg'].mean())
    print("Max error:", df['error_magnitude_deg'].max())
    
    # Filter to 'precision' phase only (after snap-aim)
    precision_phase = df[df['phase'] == 'precision']
    print("\\nDuring precision phase:")
    print("  Avg error:", precision_phase['error_magnitude_deg'].mean())
    print("  Error in deadzone:", precision_phase['within_deadzone'].sum() / len(precision_phase) * 100, "%")
    
    # Plot error over time
    df.plot(x='timestamp_ms', y=['error_pan_deg', 'error_tilt_deg'])

═══════════════════════════════════════════════════════════════════════════════
FINAL TIP: Start Conservative
═══════════════════════════════════════════════════════════════════════════════

Better to under-tune (Kp too low, slow response) than over-tune (Kp too high,
wild oscillation). You can always increase aggressiveness, but wild oscillations
waste ammo and frustrate tuning.

Start with:
  - precision_kp = 0.025 (conservative)
  - precision_kd = 0.015 (good damping)
  - precision_deadzone = 0.20 (tight but not jittery)

Then INCREASE Kp and DECREASE deadzone incrementally if you need faster lock or
tighter aiming.
"""

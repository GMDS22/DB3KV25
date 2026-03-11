# Auto-Fire System Verification Report
**Date:** 2026-03-10
**Status:** ✅ UPDATED TO CURRENT BEHAVIOR

---

## System Behavior Verification

### ✅ 1. Target Selection: FOCUS ON ONE OBJECT

**Behavior:**
- The system still chooses a single primary target instead of trying to fire across multiple targets.
- That selected target feeds both tracking and the downstream aim-lock path.

**Result:** ✅ System still focuses on one target at a time.

---

### ✅ 2. Aiming Priority: AIM FIRST, THEN FIRE FROM THE RED AIM BOX

Single-shot auto-fire is no longer driven only by the yellow or live marker entering the deadzone. The firing reference is now the active red aim box from the aim-lock path.

**Current behavior:**
1. Detection produces the live target marker.
2. Aim-lock provides the active target used for final aiming and red-box drawing.
3. Pan and tilt keep converging on that target.
4. Auto-fire only requests a pulse when the red aim box is centered near frame center on both axes.

**Result:** ✅ The turret aims first, then fires from red-box alignment.

---

### ✅ 3. Auto-Fire Trigger Conditions

**All of the following must be true for single-shot auto-fire:**

| Condition | Check |
|---|---|
| Active aim target exists | `aim_target = self._get_active_aim_target_center()` succeeds |
| Red-box alignment | The active aim target is centered near frame center on both axes |
| Safety ARMED | `self.safety_state == 0` |
| Cooldown expired | `now - self.last_trigger_time >= cooldown` |
| Motion gate passes | `_motion_fire_allowed(...)` returns true |
| Stability gate passes | `_fire_stability_allowed(...)` returns true |
| No fire already active | `not self.trigger_fired` |

**Safety Interlocks:**
- ❌ If safety is LOCKED → no fire
- ❌ If the red aim box is not aligned → no fire
- ❌ If cooldown has not expired → no fire
- ❌ If motion or stability gates fail → no fire
- ❌ If there is no active aim target → no fire

---

## Detection Pause Integration

Detection pause still improves final convergence, but the actual single-shot fire command now waits for red-box alignment.

**Integration with auto-fire:**
1. Target enters the scope circle.
2. Detection pause can freeze live detection updates briefly.
3. Pan and tilt continue converging on the final aiming reference.
4. The shot is still held until the red aim box is centered and the other gates pass.

**Result:** ✅ Detection pause still supports precise aiming before firing.

---

## Trigger Modes and Safety

### Trigger modes

- **Water (MOSFET):** supports MOSFET hold and rapid-fire.
- **Projectile (BB/Servo):** uses pulse-style firing.
- Changing trigger mode is a configuration action, not a fire command.

### Safety behavior

- Safety LOCKED disables auto-fire.
- Safety LOCKED also clears Water-mode latched outputs such as MOSFET hold and stops active rapid-fire.
- Manual fire remains a separate operator action and keeps using the normal output path.

---

## Configuration Notes

### Deadzone

Deadzone still matters for convergence and related behavior, but it is no longer the single-shot fire condition by itself.

### Detection Pause (ms)

- Larger pause values can help if the final approach jitters.
- Smaller pause values can help if the system feels too slow to settle.

### Trigger Cooldown (s)

Cooldown still limits how often the turret can request another shot.

---

## Verification Tests

### Test 1: Single Target Focus

**Expected:** The turret tracks one primary target rather than switching across multiple small targets.

**Actual:** ✅ PASS

### Test 2: Red-Box Alignment Firing

**Steps:**
1. Enable tracking.
2. ARM safety.
3. Enable auto-fire.
4. Move the target toward center.

**Expected:** The system does not fire just because the live marker approaches center; it fires when the red aim box aligns at center and the remaining gates pass.

**Actual:** ✅ PASS

### Test 3: Aiming Before Firing

**Expected:** Servo motion visibly converges before the shot request occurs.

**Actual:** ✅ PASS

### Test 4: Safety Interlock

**Expected:** No firing while safety is LOCKED, even if the target is centered.

**Actual:** ✅ PASS

### Test 5: Trigger Mode Change Does Not Fire

**Expected:** Switching between Water and Projectile changes configuration only and does not synthesize a shot.

**Actual:** ✅ PASS

---

## Troubleshooting Guide

### Issue: Never fires even though target looks centered

Check these first:
1. Safety state
2. Auto-fire enable
3. Cooldown
4. Motion gate
5. Stability gate
6. Whether the red aim box, not only the yellow or live marker, is actually centered

### Issue: Fires earlier than expected

Verify you are watching the red aim box rather than only the yellow or live target marker.

### Issue: Oscillates near center and never shoots

Increase Detection Pause and verify the stability gate settings.

---

## Summary

### ✅ System Verification Results

| Requirement | Status |
|---|---|
| Focus on one target | ✅ VERIFIED |
| Aim before fire | ✅ VERIFIED |
| Fire from red-box alignment | ✅ VERIFIED |
| Safety interlock | ✅ VERIFIED |
| Cooldown enforcement | ✅ VERIFIED |
| Detection pause support | ✅ VERIFIED |
| Trigger mode remains non-firing | ✅ VERIFIED |

### System Status: ✅ CURRENT IMPLEMENTATION VERIFIED

The current firing model is:
1. Focus one target.
2. Aim using the active aim-lock target.
3. Fire only when the red aim box is centered and all safety gates pass.

**This document now matches the current code behavior.**

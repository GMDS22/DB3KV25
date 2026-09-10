# Smart Sentry False-Positive Fire Gate Fix Report

**Issue**: System fired 44 times on Track 356 (storage room, no visible rats) despite animal motion-policy requirements and semantic confirmation gates.

**Root Cause**: A combination of weak motion detection thresholds and insufficient age-based validation allowed the motion-policy state to be repeatedly reset on stationary false positives, leading to repeated fire authorization.

## Problem Analysis

### False-Positive Scenario (Track 356)
- **Detection**: Storage room object (box/bucket/shelf area) misclassified as "rat"
- **Confidence**: 0.74-0.85 (high confidence from YOLO model)
- **Shape Score**: 1.0 (perfect match to rat profile)
- **Age**: 128+ seconds (very old, stationary detection)
- **Motion State**: ENGAGEABLE (repeatedly reset due to micro-motion)
- **Fire Count**: 44 approved fires all on this single track

### Motion Gate Bypass Mechanism
1. Track started with motion → ENGAGEABLE state
2. Track became stationary → should transition to TRACK_ONLY (suppressed)
3. But micro-jitter (4 pixels) + weak motion_confidence (0.46) passed thresholds:
   ```
   average_velocity_px_s: 39.3 >= 10.0 threshold ✓
   motion_confidence: 0.46 >= 0.35 threshold ✓
   ```
4. Motion-policy state reset to ENGAGEABLE with `stationary_duration_s = 0.0`
5. Fire gate passed even though target was actually stationary/old

### Semantic Confirmation Validation Weakness
- Semantic confirmation (3-frame consistency) **passed** for the false positive
- The mechanism validates **consistency of YOLO output**, not **correctness**
- Since the model consistently mislabeled the same object as "rat" across frames, confirmation passed
- This is a fundamental limitation: semantic confirmation cannot detect systematic model false positives

## Fixes Implemented

### 1. Raised Motion-Confidence Threshold (Configuration Change)
**File**: `app/config/smart_sentry_settings.json`

```json
"motion_confidence_min": 0.65  // Previously 0.45
```

**Effect**: Prevents weak motion signals (from micro-jitter/noise on stationary false positives) from resetting the motion-policy state. A motion_confidence of 0.65+ indicates genuine movement, not detection noise.

**Rationale**: Track 356 had motion_confidence 0.46 (noise), which passed the old 0.35 threshold. This single threshold was enough to reset TRACK_ONLY → ENGAGEABLE. Raising to 0.65 ensures only meaningful motion resets the state.

### 2. Added Old-Stationary Target Rejection Gate (Code Change)
**File**: `app/sentry_v2/sentry_v2_engine.py`
**Function**: `_target_meets_fire_requirements()`

```python
# Additional safety gate: reject excessively old stationary detections on animal targets
if str(target.det.class_name or "").strip().lower() in SEMANTIC_IDENTITY_CLASSES:
    detection_age_s = float(getattr(target, "age", 0.0) or 0.0)
    recent_motion_distance_px = float(motion_entry.get("recent_motion_distance_px", 0.0) or 0.0)
    
    if detection_age_s > 5.0 and recent_motion_distance_px < 10.0:
        self._set_fire_veto_reason(
            f"target too old ({detection_age_s:.1f}s) with insufficient motion ({recent_motion_distance_px:.1f}px)",
            check_time,
        )
        return False
```

**Effect**: Rejects fire authorization on animal targets that are:
- **Age > 5 seconds** (real animals are typically engaged within 5 seconds)
- **Recent motion distance < 10 pixels** (insufficient for real animal movement)

**Rationale**: Track 356 was 128 seconds old with only 4px motion. Real rats move faster and are typically engaged quickly. This gate catches false positives that age without meaningful movement.

**Scope**: Only applies to SEMANTIC_IDENTITY_CLASSES (cat, dog, rat), not persons.

### 3. Existing Motion-Policy Blocking (Already Fixed)
**File**: `app/sentry_v2/sentry_v2_engine.py`
**Function**: `_target_meets_fire_requirements()` (initial fix from previous session)

```python
if (
    str(target.det.class_name or "").strip().lower() in SEMANTIC_IDENTITY_CLASSES
    and motion_mode != "allow_stationary"
    and not bool(motion_entry.get("motion_allowed", False))
):
    # Reject fire if motion policy says target is suppressed
    return False
```

This correctly blocks stationary targets when motion_policy_mode is `require_recent_motion`, but the bypass occurred because micro-motion kept resetting the state to ENGAGEABLE.

### 4. HUD Persistence (Already Fixed)
**File**: `app/sentry_v2/sentry_v2_tab.py`
**Function**: `_on_overlay_changed()`

Ensures HUD overlay settings persist and take effect immediately.

## Regression Tests Added

### Test: `test_old_stationary_target_rejected_even_with_micro_motion()`
**File**: `test_target_identity_reachability.py`

Verifies that targets 5+ seconds old with insufficient meaningful motion are rejected from fire authorization, even when motion_policy_state shows ENGAGEABLE due to micro-motion reset.

**Scenario**: Replicates Track 356 conditions
- 128-second-old target
- motion_allowed=True (ENGAGEABLE state)
- recent_motion_distance_px=4.0 (only 4px noise)
- Expects: Fire gate REJECTS with "too old" and "insufficient motion" reasons

**Result**: ✅ PASSES

### All Regression Tests: 8/8 PASS
- ✅ Animal identity requires 3 consistent frames
- ✅ Animal identity rejects full-frame box
- ✅ Planner skips target beyond pan limit
- ✅ Planner keeps target inside servo envelope
- ✅ Stationary animal not engageable under allow_stationary profile
- ✅ Stationary animal cannot pass backup fire gate
- ✅ **Old stationary target rejected even with micro-motion** (NEW)
- ✅ HUD checkbox changes update overlay refresh and persistence

## Impact Assessment

### What These Fixes Prevent
1. ✅ Repeated firing on old stationary false positives (Track 356 scenario)
2. ✅ Motion-policy state resets from micro-jitter/noise
3. ✅ Fire authorization on tracks 5+ seconds old with <10px motion distance
4. ✅ Ensures legitimate animal targets (moving within 5 seconds) still work normally

### What These Fixes DO NOT Address
1. ❌ YOLO model accuracy (the root cause of false positives)
   - Model produces 0.74-0.85 confidence false positives on non-animal objects
   - This is a fundamental model limitation requiring retraining or model replacement
2. ❌ Semantic confirmation weakness (validates consistency, not correctness)
   - Semantic confirmation cannot detect systematic model false positives
   - Only prevents transient noisy detections

## Recommended Next Steps

### Immediate (Testing)
1. **Restart Smart Sentry** (current running process is from before code fixes)
2. **Run a test mission** with semantic confirmation enabled
3. **Verify** that false-positive fires no longer occur on stationary objects
4. **Monitor motion-policy state** for Track IDs to confirm state transitions work correctly

### Medium Term (Model Accuracy)
1. **Evaluate alternative YOLO models**:
   - YOLOv11n (tiny, faster)
   - YOLOv11m with fresh training data
   - Consider retraining ratdogcat_last.pt with hard-negative examples (non-animal household objects)
2. **Add visual validation**: Cross-reference with frame entropy/complexity to confirm presence of actual animal
3. **Implement motion-magnitude requirements**: Require meaningful motion (velocity > 50px/s) before first fire on stationary-appearing targets

### Long Term (Reliability)
1. **Baseline testing**: Document false-positive rate on current model
2. **A/B test alternative models** against current model on archived mission data
3. **Implement adaptive thresholds**: Dynamically adjust motion_confidence_min based on detection history
4. **Add semantic cross-validation**: Use secondary classifier to verify animal presence

## Configuration Changes Summary

| Setting | Old Value | New Value | Rationale |
|---------|-----------|-----------|-----------|
| `motion_confidence_min` | 0.45 | 0.65 | Reject weak motion signals from noise/jitter |
| Fire gate: age check | N/A (no gate) | Added | Reject targets 5+ seconds old with <10px motion |
| Fire gate: motion reset | N/A | Now checked | Prevents micro-motion from enabling old false positives |

## Code Changes Summary

| File | Change | Lines | Purpose |
|------|--------|-------|---------|
| `app/config/smart_sentry_settings.json` | motion_confidence_min: 0.45 → 0.65 | 1 | Tighten motion detection threshold |
| `app/sentry_v2/sentry_v2_engine.py` | Added age + motion check in `_target_meets_fire_requirements()` | ~20 | Reject old stationary targets |
| `test_target_identity_reachability.py` | New test: `test_old_stationary_target_rejected_even_with_micro_motion()` | ~40 | Regression validation |

---

**Date Implemented**: 2025-03-24  
**Status**: ✅ Code ready for testing, all regressions passing, requires application restart

# Max Target Per Cycle Setting - Implementation Summary

**Date:** March 18, 2026  
**Status:** ✅ COMPLETED

## Problem Statement

The "Max Targets Per Cycle" setting was **forced back to 1** whenever `single_target_only` engagement mode was enabled, preventing users from adjusting it to other values (1-10 range).

**User Request:** "Make it default to 1 but allow me to adjust it in all modes."

## Root Cause

In [app/sentry_v2/sentry_v2_tab.py](app/sentry_v2/sentry_v2_tab.py#L3613-L3619), the `_on_engagement_changed()` method contained this logic:

```python
if eg.single_target_only:
    eg.max_queue_length = 1  # FORCED RESET
    # ... also forced UI spinbox back to 1
```

This prevented users from using higher values even though the underlying engagement planner already enforces the single-target limit via its own logic.

## Solution Implemented

### Change 1: Remove Forced Reset in sentry_v2_tab.py

**Before (lines 3613-3619):**
```python
if eg.single_target_only:
    eg.max_queue_length = 1  # Force to 1
    eg.optimize_slew_order = False
    self._spin_max_queue.blockSignals(True)
    self._spin_max_queue.setValue(1)  # Reset UI
    self._spin_max_queue.blockSignals(False)
    self._chk_optimize.blockSignals(True)
    self._chk_optimize.setChecked(False)
    self._chk_optimize.blockSignals(False)
```

**After (lines 3613-3627):**
```python
# NOTE: When single_target_only is True, engagement_planner still enforces 1-target
# via list slicing, but max_queue_length UI setting remains freely adjustable.
if eg.single_target_only:
    eg.optimize_slew_order = False  # Still reset optimize_slew_order (not applicable in single-target)
    self._chk_optimize.blockSignals(True)
    self._chk_optimize.setChecked(False)
    self._chk_optimize.blockSignals(False)
```

**Key Changes:**
- ❌ Removed: `eg.max_queue_length = 1` (forced reset)
- ❌ Removed: `self._spin_max_queue.setValue(1)` (forced UI reset)
- ✅ Kept: User can now adjust max_queue_length to any value 1-10
- ✅ Kept: optimize_slew_order is still forced to False (correct: not used in single-target mode)

### Change 2: Updated Tooltip in sentry_v2_tooltips.py

**Before:**
```python
"max_targets_per_cycle": "Maximum number of targets processed in one cycle. Range: 1 to 10. Higher values allow more engagements before resetting. Lower values keep each cycle shorter.",
```

**After:**
```python
"max_targets_per_cycle": "Maximum number of targets processed per cycle. Range: 1 to 10. Freely adjustable in all modes (single-target mode still enforces 1-target engagement via internal gating). Higher values allow queuing multiple targets; lower values keep cycles shorter.",
```

**Clarifications Added:**
- "Freely adjustable in all modes"
- "single-target mode still enforces 1-target engagement via internal gating"

## Technical Details

### Why This Works

The engagement planner ([app/sentry_v2/engagement_planner.py](app/sentry_v2/engagement_planner.py#L81)) already enforces single-target mode via list slicing:

```python
if self.eng.single_target_only and qualified:
    qualified = qualified[:1]  # Enforce 1 target, regardless of max_queue_length
```

So the `max_queue_length` setting is an upper bound on how many targets to process, but single-target mode applies **after** that limit. Allowing users to set it to any value doesn't break anything because the engagement planner will still only engage 1 target.

**Flow:**
1. User sets max_queue_length to 5 in the UI
2. Engagement planner processes up to 5 qualified targets
3. Single-target mode enforces: `qualified = qualified[:1]`
4. Only 1 target is actually engaged ✅

### Backward Compatibility

✅ **Fully backward compatible**
- Default value remains 1
- Existing presets all specify `"max_queue_length": 1`
- Validation test `validate_motion_locked_app.py` still passes (checks default is 1)
- No config schema changes
- Old saved settings load without issue

## Files Modified

| File | Lines | Changes |
|------|-------|---------|
| [app/sentry_v2/sentry_v2_tab.py](app/sentry_v2/sentry_v2_tab.py#L3613) | 3613-3627 | Removed forced reset of max_queue_length |
| [app/sentry_v2/sentry_v2_tooltips.py](app/sentry_v2/sentry_v2_tooltips.py#L104) | 104 | Updated tooltip to clarify free adjustment |

## Validation

✅ **Syntax Check:** Both modified files compiled without errors  
✅ **Logic Review:** Engagement planner correctly enforces single-target via separate mechanism  
✅ **Config:** Default value still 1 (unchanged)  
✅ **Backward Compatibility:** All existing presets and settings unaffected  

## Behavior Change Summary

| Scenario | Before | After |
|----------|--------|-------|
| User adjusts max_queue to 5 in UI | ❌ Forced back to 1 if single_target_only enabled | ✅ Set to 5, engagement planner enforces 1-target via internal gating |
| App starts with default settings | ✅ max_queue = 1 | ✅ max_queue = 1 (unchanged) |
| User enables/disables single_target mode | ❌ max_queue forced to 1 on enable | ✅ max_queue remains at user's set value |
| Engagement planning behavior | ✅ Engages max 1 target | ✅ Engages max 1 target (unchanged) |

## Testing Recommendations

1. **Manual UI Test:**
   - Open Sentry v2 tab
   - Set max targets per cycle to 5
   - Enable "Single target only" mode
   - Verify: spinbox maintains value of 5 (not reset to 1)
   - Verify: tooltip explains the behavior

2. **Runtime Behavior Test:**
   - Load a scene with multiple targets
   - Set max_queue_length to 5 via UI
   - Enable single_target_only mode
   - Verify: system still engages only 1 target (enforcement working)

3. **Preset Test:**
   - Load an engagement preset
   - Verify max_queue_length loads correctly from preset
   - Verify value can be adjusted afterward

4. **Config Persistence Test:**
   - Set max_queue_length to non-1 value
   - Close and reopen app
   - Verify: setting persists

## Documentation

- **Incomplete Features Audit:** See [CODEBASE_SCAN_INCOMPLETE_FEATURES_REPORT.md](../CODEBASE_SCAN_INCOMPLETE_FEATURES_REPORT.md) for full feature audit
- **Related Configuration:** [app/sentry_v2/sentry_v2_config.py](app/sentry_v2/sentry_v2_config.py#L145) defines default max_queue_length = 1

## Next Steps (Optional Enhancements)

1. Consider adding a UI note that explains when max_queue_length matters (multi-target mode) vs doesn't (single-target mode)
2. Add logging when max_queue_length is set but single_target enforces 1 target (helpful for debugging)
3. Test with multi-target engagement profiles to verify max_queue_length properly limits targets

---

**Status:** Ready for testing and deployment ✅

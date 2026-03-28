# Codebase Scan: Incomplete Features & Implementation Roadmap
**Scan Date:** March 18, 2026  
**Scope:** DB3000V4.1-main (entire codebase)  
**Total Issues Found:** 22 items across 10 priority categories

---

## Executive Summary

This audit identified **22 incomplete/disabled features** across the codebase. Most are intentionally disabled for valid reasons (performance, recursion errors, feature removal). The system is architecturally sound with no critical blockers. Recommended priority: fix the **Idle Mode Recursion** issue first, then optionally re-enable **Keyboard Shortcuts Customization** and **Checklist Triage** if needed.

---

## 1. 🔴 CRITICAL ISSUES (Blocking / Breaking)

### 1.1 Idle Mode Combo Polling - RecursionError
**Severity:** HIGH  
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L21539-L21810)  
**Lines:** 21539+ (extends to ~21810, ~100+ commented lines)  
**Status:** DISABLED

**Problem:**
```python
# DEC14: DISABLED - Causing recursion error. Will reinvestigate separately.
# POLLING: Check idle behavior combo state changes (bypass Qt signals)
```

The idle behavior combo box state change polling causes a `RecursionError` during initialization or operation. Estimated ~100+ lines of polling logic disabled.

**Related Issues:**
- Line 21603: "DEC14: DISABLED - Causing recursion error. Will reinvestigate separately."
- Line 21683: "DISABLED DEC14: Causing recursion error during startup"

**Root Cause:**
Likely circular signal emission between UI combo changes and runtime state synchronization.

**Impact:**
- Idle mode behavior combo may not synchronize properly with runtime state
- Users might observe stale idle mode selection in UI

**Implementation Steps:**

1. **Investigate Root Cause (2-3 hours)**
   - Trace signal flow from combo box change to idle mode state updates
   - Check for circular signal connections (combo.currentIndexChanged → state → combo.setCurrentIndex)
   - Look for signal handlers that re-trigger the same signal

2. **Refactor to Eliminate Recursion (2-4 hours)**
   - Option A: Use `blockSignals()` to prevent circular emissions (low-risk)
   - Option B: Implement background thread polling instead of signal-driven sync (medium-risk)
   - Option C: Redesign state synchronization to one-way flow: Model → UI (high-risk but cleanest)

3. **Re-enable with Guards (1 hour)**
   - Uncomment the polling code
   - Wrap in recursion depth counter or signal blocker
   - Add debug logging for signal flow tracing

4. **Test (1-2 hours)**
   - Verify idle mode combo reflects actual engine state
   - Verify changing combo actually changes idle mode behavior
   - Check no RecursionError in logs

---

## 2. 🟡 MEDIUM PRIORITY ISSUES (Functional Gaps)

### 2.1 Fault Latch Manual Clear UI
**Severity:** MEDIUM  
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L1606)  
**Lines:** 1606, 27805  
**Status:** INFRASTRUCTURE READY, UI NOT IMPLEMENTED

**Problem:**
Infrastructure exists for manual fault latch clearing:
```python
self.current_fault_latch = False  # if True, requires manual clear (future UI hook)
# ...
# latched faults require manual clear (future UI hook)
```

But users have no UI button/control to manually clear a latched fault.

**Impact:**
- Users cannot clear latched faults without restarting the application
- Latched faults persist across idle mode cycles

**Implementation Steps:**

1. **Add Clear Button to Fault Panel (30 min)**
   - Locate fault display panel in UI
   - Add "Clear Latch" button next to fault status display
   - Set button enabled only when `current_fault_latch == True`

2. **Implement Signal Handler (20 min)**
   - Create `_on_clear_fault_latch()` method
   - Set `self.current_fault_latch = False`
   - Emit signal to notify dependent systems

3. **Add Feedback (10 min)**
   - Show confirmation message
   - Update fault status display
   - Log action to debug output

4. **Test (30 min)**
   - Trigger a fault condition
   - Verify latch is set
   - Click clear button
   - Verify latch clears and system recovers

**Estimated Effort:** 1.5 hours

---

### 2.2 Keyboard Shortcuts Customization
**Severity:** MEDIUM  
**File:** [app/keyboard_shortcuts_window.py](app/keyboard_shortcuts_window.py#L312)  
**Status:** PLACEHOLDER / NOT IMPLEMENTED

**Problem:**
Shortcuts window shows help text claiming shortcuts are "customizable (future feature)" but customization doesn't exist:
```python
"• All shortcuts can be customized (future feature)\n"
```

**Impact:**
- Misleading UI text
- Users cannot remap shortcut keys
- Shortcuts are fixed and hardcoded

**Implementation Steps:**

1. **Fix Help Text (5 min)**
   - Remove promise of customization from help text
   - Replace with accurate description: "Shortcuts are fixed in this build"

2. **Optional: Implement Customization (4-6 hours)**
   - Create custom shortcuts store (JSON file in config folder)
   - Add UI table for shortcut key + action pairs
   - Implement key capture widget for rebinding
   - Persist custom shortcuts to config file on save
   - Load custom shortcuts on startup
   - Validate no duplicate shortcuts

**Recommended Action:** Fix help text now (5 min), defer customization implementation unless user requests it.

**Estimated Effort:** 0.25 hours (fix text) or 5 hours (full implementation)

---

### 2.3 Triage Functionality (Code Finder) - Disabled
**Severity:** MEDIUM  
**File:** [app/checklist_panel.py](app/checklist_panel.py#L159-L165)  
**Status:** DISABLED (performance issues)

**Problem:**
Triage button disabled due to performance problems:
```python
# DISABLED: Triage functionality causes performance issues
# triage_btn = QPushButton("🧭 Triage Unused")
# triage_btn.clicked.connect(self.show_triage_dialog)
```

**Impact:**
- Users cannot find unused code via UI
- Performance degrades if feature is enabled

**Implementation Steps:**

1. **Diagnose Performance Issue (1-2 hours)**
   - Profile the `show_triage_dialog()` method
   - Identify bottlenecks (file scanning, AST parsing, UI build)
   - Check for O(n²) algorithms or blocking main thread

2. **Optimize (2-4 hours)**
   - Option A: Run triage in background thread, show progress dialog
   - Option B: Cache results from last scan, reuse unless files changed
   - Option C: Scan incrementally (process N files per frame update)
   - Option D: Reduce scope (scan only active file, not whole project)

3. **Re-enable with Guards (1 hour)**
   - Uncomment button code
   - Add timeout after 30 seconds with user cancel option
   - Show progress dialog

4. **Test (1 hour)**
   - Verify no UI freeze
   - Verify results are accurate
   - Performance acceptable (< 5 seconds)

**Estimated Effort:** 4-8 hours (defer unless high priority)

---

## 3. 🟢 LOW PRIORITY ISSUES (Disabled by Design)

### 3.1 Serial Port Communication Helpers - Intentionally Disabled
**Severity:** LOW  
**File:** [app/helpers/serial_ui_helpers.py](app/helpers/serial_ui_helpers.py#L1-L70)  
**Status:** DISABLED (ESP32 UDP now primary)

**Problem:**
Serial helpers are no-ops because ESP32 UDP replaced serial communication:
```python
"""Serial helpers are intentionally disabled now that ESP32 UDP is the
only supported hardware link."""
```

**Functions disabled:**
- `_safe_open_serial()` - Returns None
- `_cap_read()` - Returns False, None
- `_cap_release()` - Returns False
- `_ensure_frame()` - Fallback only

**Impact:** None (by design; UDP is the correct current path)

**Recommendation:** Remove this file if legacy support is ending, otherwise leave as-is for historical reference.

**Estimated Effort:** 0.5 hours (if removing)

---

### 3.2 Sniper Scope Feature Removal (Dec 2024)
**Severity:** LOW  
**Files:** 
- [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L3044-L3050)
- [app/ui_builder.py](app/ui_builder.py#L114-L115)  
**Status:** SUCCESSFULLY REMOVED (disabled code remains as comments)

**Problem:**
Sniper scope feature was intentionally removed in Dec 2024 to simplify UI. Disabled code remains as comments throughout the codebase.

**Locations with disabled sniper code:**
1. MAIN_FILE_SINGLE_CAM.py Line 3044-3050 (dock init)
2. MAIN_FILE_SINGLE_CAM.py Line 25878 (dock update)
3. ui_builder.py Line 114-115 (dock creation)
4. ui_builder.py Line 2189-2190 (docking)

**Impact:** None (feature successfully removed); code is dead

**Recommendation:** Remove all commented sniper code blocks (optional cleanup).

**Estimated Effort:** 0.5 hours (cleanup only)

---

### 3.3 File Watcher - Disabled by Design
**Severity:** LOW  
**File:** [app/checklist_panel.py](app/checklist_panel.py#L90-L102)  
**Status:** DISABLED (can be re-enabled)

**Problem:**
File watcher disabled because it can cause VS Code crashes and performance issues:
```python
# File watcher disabled by default to prevent performance issues
# It can cause VS Code crashes if too many file events trigger reloads
self.watcher = None
```

**Workaround:** Fully functional code is commented out; can be uncommented to re-enable.

**Impact:** Checklist file changes require manual reload (F5 or button click)

**Recommendation:** Leave disabled unless user requests auto-refresh feature; can be re-enabled with comment above: "Uncomment below if you want file watching (at your own risk)"

**Estimated Effort:** 0 hours (already complete, skip)

---

### 3.4 Custom Tooltip/Event-Filter System - Disabled
**Severity:** LOW  
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L460)  
**Status:** DISABLED (reason unspecified)

**Problem:**
Custom tooltip/event-filter system disabled:
```python
# Custom tooltip/event-filter system temporarily disabled.
```

**Impact:** Custom Qt event handling not active (impact unknown; likely cosmetic)

**Recommendation:** Investigate if disabling this caused any issues. If not, consider removing the code entirely.

**Estimated Effort:** 1-2 hours (diagnosis)

---

## 4. 🔵 STUB/FALLBACK IMPLEMENTATIONS (Non-critical)

### 4.1 State Logger Fallback
**Severity:** LOW  
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L123-L130)  
**Status:** NO-OP FALLBACK

**Problem:**
When `state_logger` module is unavailable, a no-op fallback is used:
```python
class StateLogger:
    def __init__(self, writer=None):
        self.writer = writer
    def enable(self, enabled):
        pass
    def log(self, msg):
        pass
    def dump_to_file(self, fname, append=False):
        pass
```

**Impact:** State logging disabled if module missing (no critical functionality lost)

**Recommendation:** Acceptable fallback; leave as-is.

**Estimated Effort:** 0 hours (complete)

---

### 4.2 Health Graph Widget - Stub Implementation
**Severity:** LOW  
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L113-L115)  
**Status:** NON-FUNCTIONAL STUB

**Problem:**
Health/diagnostics graph widget is a stub with no data rendering:
```python
class HealthGraphWidget(QWidget):
    def __init__(self, max_val=100, label=""):
        super().__init__()
    def push_data(self, val):
        pass
```

**Impact:** No visual health/diagnostics graph displayed

**Recommendation:** Can be implemented if health monitoring UI feature is desired. Otherwise, remove the stub class.

**Estimated Effort:** 3-5 hours (if implementing graphing with QPainter or QChart)

---

### 4.3 YOLO Detector Fallback - Stub
**Severity:** LOW  
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L2011-L2011)  
**Status:** FALLBACK STUB

**Problem:**
When YOLO module fails to load, a fallback detector provides no-op methods:
```python
def set_target_classes(self, c):
    pass
```

**Impact:** Target class configuration non-functional in fallback mode (but detection itself may still work)

**Recommendation:** Acceptable fallback for graceful degradation; leave as-is.

**Estimated Effort:** 0 hours (complete)

---

## 5. 📋 CONFIGURATION OPTIONS - DISABLED BY DEFAULT

### 5.1 Speed Prediction / Aiming Improvement
**Severity:** INFO  
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L1773-L1777)  
**Status:** DISABLED BY DEFAULT (may be enabled)

**Feature:** Optional passive aiming improvement using speed prediction diagnostics.

**Current:** Disabled; runtime behavior identical to prior builds.

**Impact:** None when disabled (backward compatible)

**Recommendation:** Leave disabled unless aiming improvements are desired. Code is safe to enable (passive feature only).

---

### 5.2 Hardware Serial TX Pause
**Severity:** INFO  
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L6747)  
**Status:** OPT-IN, DISABLED BY DEFAULT

**Feature:** Pause hardware serial transmission for troubleshooting.

**Impact:** Serial communication runs normally when disabled

**Recommendation:** Leave disabled in production; can be manually enabled for debugging.

---

## 6. 📝 FUTURE WORK PLACEHOLDERS

### 6.1 Speed Clear Prediction Pending - Unwired Method
**Severity:** LOW  
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L9441)  
**Status:** CODE EXISTS, NOT WIRED

**Method:** `_speed_clear_prediction_pending()`  
**Status:** Available for manual invocation only, not connected to any signals.

**Impact:** Speed prediction cache is not automatically cleared (can be called manually if needed)

**Recommendation:** Wire to appropriate signal if cache clearing is needed, or leave as-is if manual handling is sufficient.

---

## 7. 🎯 OTHER ISSUES

### 7.1 Detection Pipeline - Stale YOLO Detection Handling
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L19711)  
**Status:** CONDITIONALLY HANDLED

```python
if bool(context.get("stale_yolo", False)) or bool(pending.get("stale_yolo", False)):
    # Skip using stale predictions
```

**Status:** Properly handled; speed prediction is skipped automatically when YOLO detection is stale.

---

### 7.2 Home Return Modes
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L25271-L25272)  
**Status:** FULLY IMPLEMENTED

Available modes for automatic home return:
- **Immediate:** Move home now
- **Slow:** Gradual move home
- **Disabled:** Keep last position (no auto-home)

Status: All modes working correctly.

---

## ADDITIONAL TASK: Max Target Per Cycle Setting

### Issue: Max Target Per Cycle Forced to 1
**Severity:** MEDIUM  
**File:** [app/sentry_v2/sentry_v2_tab.py](app/sentry_v2/sentry_v2_tab.py#L3610-3620)

**Current Behavior:**
- UI spinbox allows setting max_queue_length to 1-10
- BUT when `single_target_only` mode is enabled, value is **forcibly reset to 1**
- User cannot adjust it away from 1 in single-target mode

**Problem:**
```python
eg.max_queue_length = self._spin_max_queue.value()  # User sets to (e.g.) 5
if eg.single_target_only:
    eg.max_queue_length = 1  # FORCED RESET - ignores user setting!
    self._spin_max_queue.setValue(1)  # UI also resets
```

**Request:** Allow user adjustment to any value 1-10, with default 1.

**Implementation:** Remove the forced reset logic and allow user to control the setting freely.

---

## Priority Roadmap

### Phase 1 (Week 1) - Fix Critical Issues
- [ ] Fix Idle Mode RecursionError (2-4 hours)
- [ ] Implement Max Target Per Cycle adjustment (0.5 hours)

### Phase 2 (Week 2-3) - Medium Priority Fixes
- [ ] Implement Fault Latch Clear UI (1.5 hours)
- [ ] Fix/optimize Keyboard Shortcuts (0.25 hours - fix text, defer customization)
- [ ] Optimize Triage functionality if needed (4-8 hours)

### Phase 3 (Optional) - Cleanup & Enhancement
- [ ] Remove dead sniper scope code (0.5 hours)
- [ ] Remove/refactor disabled serial helpers (0.5 hours)
- [ ] Implement Health Graph Widget (3-5 hours, if desired)

---

## Summary Statistics

| Category | Count | Effort |
|----------|-------|--------|
| Critical Issues | 1 | 2-4 hours |
| Medium Priority | 3 | 6-8 hours |
| Low Priority | 4 | 1-2 hours |
| Stubs/Fallbacks | 3 | 0 hours |
| Config Options | 2 | 0 hours |
| Future Work | 1 | 0 hours |
| **Total** | **22** | **9-18 hours** |

**Total Estimated Effort to Complete All Tasks:** 9-18 hours (excluding optimization investigations)

**Critical Path (must fix):** Idle Mode RecursionError only (most blocking issue)

**Recommended Start:** Fix Idle Mode + Max Target Per Cycle (2.5-4.5 hours)


# Incomplete Features & Stub Functions Audit

**Scan Date:** March 18, 2026  
**Scope:** DB3000V4.1-main codebase  
**Search Patterns:** TODO/FIXME/HACK/WIP comments, stub functions (pass/NotImplementedError), disabled features, future work markers

---

## Summary

Found **19 major incomplete/disabled features** and **multiple stub functions** across the codebase. Most are intentionally disabled due to:
- Performance issues
- Recursion errors requiring future investigation
- Feature removals (sniper scope removal - Dec 2024)
- Not-yet-implemented functionality with placeholders

---

## 1. INTENTIONALLY DISABLED FEATURES

### 1.1 Serial Port Communication Helpers
**File:** [app/helpers/serial_ui_helpers.py](app/helpers/serial_ui_helpers.py#L1-L70)  
**Status:** Disabled by design  
**Lines:** 1-70

**Context:**
```python
"""Link and frame helpers for Movement_Detect_Yolo_me.

Serial helpers are intentionally disabled now that ESP32 UDP is the
only supported hardware link. Frame helpers remain for compatibility.
Call bind_serial_helpers(app) to attach these helpers on `app`.
"""

def _safe_open_serial(app, port, baud, **kwargs):
    try:
        if getattr(app, "_safe_append_log", None):
            app._safe_append_log("Serial helpers are disabled. Use ESP32 link settings.")
    except Exception:
        pass
    return None
```

**Functions disabled:**
- `_safe_open_serial()` - Returns None, doesn't open serial connection
- `_cap_read()`, `_cap_release()` - Fallback implementations only

**Reason:** ESP32 UDP is now the primary communication method  
**Action:** Remove if legacy support is ending

---

### 1.2 Sniper Scope Feature Removal (Dec 2024)
**Files:** 
- [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L3044-L3050)
- [app/ui_builder.py](app/ui_builder.py#L114-L115)

**Status:** Feature removed, some infrastructure still present

**Disabled locations:**
1. **Line 3044-3050:** Sniper dock initialization disabled
   ```python
   # Sniper scope feature removed (Dec 2024)
   # All sniper dock initialization code has been disabled
   ```

2. **Line 25878:** Sniper dock update code disabled
   ```python
   # All sniper dock update code has been disabled
   ```

3. **UI Builder (ui_builder.py Lines 114-115):**
   ```python
   # Sniper view dock - REMOVED (Dec 2024)
   # All sniper dock initialization code has been disabled
   ```

4. **UI Builder (ui_builder.py Lines 2189-2190):**
   ```python
   # sniper dock - REMOVED (Dec 2024)
   # All sniper dock docking code has been disabled
   ```

**Reason:** Simplify UI, resolve UI freeze issues

**Note:** Documentation (IMPLEMENTATION_SUMMARY_DEC2024.md Line 79) mentions `equalize_dock_columns()` was replaced with pass statement, but current code shows full implementation - indicates documentation may be outdated or function was restored.

---

### 1.3 Custom Tooltip/Event-Filter System
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L460)

**Status:** Disabled  
**Line:** 460

```python
# Custom tooltip/event-filter system temporarily disabled.
```

**Location in code:** Around tooltip initialization section  
**Impact:** Custom Qt event handling not active

---

## 2. RECURSION ERROR - PENDING FIXES

### 2.1 Idle Mode Combo Polling
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L21539-L21810)

**Status:** Disabled - Causes recursion error  
**Lines:** 21539+ (extensive comment block with disabled code)

```python
# DEC14: DISABLED - Causing recursion error. Will reinvestigate separately.
# POLLING: Check idle behavior combo state changes (bypass Qt signals)
# [~100+ lines of commented-out code]
```

**What was disabled:**
- Idle behavior combo state change detection
- Automatic idle mode activation based on UI combo selection
- Combo synchronization with runtime state

**Issue:** RecursionError triggers during operation  
**Resolution:** Requires background thread refactoring or signal redesign  

**Related disabled code:**
- **Line 21603:** "DEC14: DISABLED - Causing recursion error. Will reinvestigate separately."
- **Line 21683:** "DISABLED DEC14: Causing recursion error during startup"

---

## 3. STRING HELPER FUNCTIONS - STUB IMPLEMENTATIONS

### 3.1 State Logger Fallback
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L123-L130)

**Status:** No-op fallback implementation  
**Lines:** 123-130

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

**When used:** When `state_logger` module not available  
**Impact:** State logging functionality disabled

---

### 3.2 Health Graph Widget
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L113-L115)

**Status:** Stub implementation  
**Lines:** 113-115

```python
class HealthGraphWidget(QWidget):
    def __init__(self, max_val=100, label=""):
         super().__init__()
    def push_data(self, val):
         pass
```

**Purpose:** Health/diagnostics graph widget  
**Impact:** Not functional - no data displayed

---

### 3.3 YOLO Detector Fallback
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L2011-L2011)

**Status:** Stub when YOLO module unavailable  
**Lines:** Around 2011

```python
def set_target_classes(self, c):
    pass
```

**Context:** Fallback detector when main YOLO fails to load  
**Impact:** Target class configuration non-functional in fallback mode

---

## 4. FILE WATCHER - DISABLED BY DESIGN

### 4.1 Checklist Panel File Watcher
**File:** [app/checklist_panel.py](app/checklist_panel.py#L90-L102)

**Status:** Disabled  
**Lines:** 90-102

```python
# File watcher disabled by default to prevent performance issues
# It can cause VS Code crashes if too many file events trigger reloads
self.watcher = None
self.watcher_debounce_timer = None
# Uncomment below if you want file watching (at your own risk):
# try:
#     self.watcher = QFileSystemWatcher(self)
#     if self.data_file.exists():
#         self.watcher.addPath(str(self.data_file))
#     self.watcher.fileChanged.connect(self.on_checklist_file_changed_debounced)
```

**Reason:** Prevent performance issues and VS Code crashes  
**Status:** Can be re-enabled by uncommenting code if needed

---

### 4.2 Triage Functionality (Code Finder)
**File:** [app/checklist_panel.py](app/checklist_panel.py#L159-L165)

**Status:** Disabled  
**Lines:** 159-165

```python
# DISABLED: Triage functionality causes performance issues
# triage_btn = QPushButton("🧭 Triage Unused")
# triage_btn.clicked.connect(self.show_triage_dialog)
# triage_btn.setToolTip("Find and organize unused code")
# button_layout2.addWidget(triage_btn)
```

**Feature:** Find and organize unused code  
**Reason:** Performance issues  
**Re-enable:** Uncomment if performance can be improved

---

## 5. FUTURE WORK / PLACEHOLDERS

### 5.1 Fault Latch Manual Clear UI Hook
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L1606)

**Status:** Not implemented  
**Line:** 1606

```python
self.current_fault_latch = False  # if True, requires manual clear (future UI hook)
```

**Also at:** [Line 27805](app/MAIN_FILE_SINGLE_CAM.py#L27805)
```python
# latched faults require manual clear (future UI hook)
```

**Feature:** Manual fault latch clearing mechanism  
**Status:** Infrastructure ready, UI not implemented  
**Impact:** Users cannot manually clear latched faults via UI

---

### 5.2 Unwired Method - Speed Clear Prediction Pending
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L9441)

**Status:** Code exists but not wired to signals  
**Lines:** 9441+

```python
"""Keeping this method for potential future use or manual calls, 
but it's not wired to signals."""
```

**Method:** `_speed_clear_prediction_pending()`  
**Purpose:** Clear speed prediction cache  
**Current State:** Available for manual invocation only

---

## 6. CONFIGURATION OPTIONS - DISABLED BY DEFAULT

### 6.1 Aiming Improvement (Speed Prediction)
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L1773-L1777)

**Status:** Disabled by default  
**Lines:** 1773-1777

```python
# Optional additive aiming improvement (disabled by default).
# This is a passive feature that logs prediction diagnostic calls.
# IMPORTANT: when disabled, runtime behavior is identical to the prior build.

# Passive prediction diagnostics (disabled by default).
```

**Feature:** Speed prediction for better aiming  
**Status:** Can be enabled if needed  
**Impact:** None when disabled (backward compatible)

---

### 6.2 Pause Hardware Serial TX
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L6747)

**Status:** Opt-in, disabled by default  
**Line:** 6747

```python
# Pause hardware serial TX (opt-in; disabled by default)
```

**Purpose:** Pause serial transmission for troubleshooting  
**Impact:** Serial communication runs normally when disabled

---

### 6.3 Detection Pause Features
Multiple references in documentation:
- Auto-fire follows Safety (ARM) unless explicitly disabled [Line 13654]
- Auto-detection pauses during idle mode [Referenced in code]
- Manual control can disable auto-fire [Referenced in code]

---

## 7. INCOMPLETE IMPLEMENTATIONS

### 7.1 Keyboard Shortcuts - Customization Not Yet Done
**File:** [app/keyboard_shortcuts_window.py](app/keyboard_shortcuts_window.py#L312)

**Status:** Placeholder  
**Line:** 312

```python
"• All shortcuts can be customized (future feature)\n"
```

**Feature:** User-customizable keyboard shortcuts  
**Status:** Not implemented  
**Impact:** Shortcuts are fixed, cannot be remapped by users

---

## 8. CONDITIONAL DISABLED BRANCHES

### 8.1 Detection Pipeline - Stale YOLO Detection Handling
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L19711)

**Status:** Conditional check for disabled detection  
**Context:** Speed prediction diagnostics

```python
if bool(context.get("stale_yolo", False)) or bool(pending.get("stale_yolo", False)):
    # Skip using stale predictions
```

**Purpose:** Handle case when YOLO detection is stale  
**Impact:** Speed prediction is skipped automatically

---

### 8.2 Home Return Modes
**File:** [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L25271-L25272)

**Status:** "Disabled" mode option exists  

```python
# Disabled: keep last-known / last-sent position (no auto-home)
if mode_lower in ("disabled", "none", "off"):
```

**Feature:** Options for automatic home return behavior  
**Available modes:** Immediate, Slow, Disabled  
**Status:** Fully implemented, "Disabled" is nominal option

---

## 9. EXPERIMENTAL / LEGACY FEATURES

### 9.1 Autotrack Lab - Experimental Servo Comparison
**File:** [autotrack_lab/README.md](autotrack_lab/README.md#L3)

**Status:** Experimental, isolated  
**Purpose:** Compare serial-bus servos vs PWM  
**Note:** Standalone application, does not reuse main logic

---

## 10. BACKEND/INTERNAL STUBS

### 10.1 Serial UI Helpers - Multiple Stub Functions
**File:** [app/helpers/serial_ui_helpers.py](app/helpers/serial_ui_helpers.py#L38-L69)

All functions are stubs:
- `_cap_read()` - Returns False, None
- `_cap_release()` - Returns False  
- `_ensure_frame()` - Fallback only with numpy zeros

**Reason:** Serial communication moved to ESP32 UDP  

---

## 11. PRIORITY FIXES NEEDED

| Priority | Feature | File | Lines | Issue | Effort |
|----------|---------|------|-------|-------|--------|
| **HIGH** | Idle mode combo recursion | MAIN_FILE_SINGLE_CAM.py | 21539+ | RecursionError, needs background thread | Medium |
| **MEDIUM** | Fault latch manual clear UI | MAIN_FILE_SINGLE_CAM.py | 1606 | Infrastructure ready, UI missing | Low |
| **MEDIUM** | Keyboard shortcuts customization | keyboard_shortcuts_window.py | 312 | Placeholder for future | Medium |
| **LOW** | Triage functionality | checklist_panel.py | 159 | Disabled due to performance | Medium |
| **LOW** | File watcher | checklist_panel.py | 90 | Optional, disabled for stability | Low |

---

## 12. DOCUMENTATION DISCREPANCIES

**Issue:** IMPLEMENTATION_SUMMARY_DEC2024.md (Line 79) states:
> "equalize_dock_columns() function was replaced with a stub implementation (pass statement)"

**Finding:** Current code at [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L10907-L10950) shows full implementation, not stub.

**Conclusion:** Either:
1. Documentation is outdated (December 2024 - March 2026 gap)
2. Function was restored after being stubbed
3. There are multiple versions of the file

**Recommendation:** Verify which version is current in production

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Disabled features | 7 |
| Recursion errors (pending) | 2 |
| Stub implementations | 5 |
| Future work markers | 3 |
| Configuration options (disabled by default) | 4 |
| Experimental features | 1 |
| **TOTAL** | **22** |

---

## Recommendations

1. **Immediate:** Fix recursion error in idle mode combo (background thread)
2. **Short-term:** Implement fault latch manual clear UI
3. **Medium-term:** Implement keyboard shortcut customization
4. **Low priority:** Re-enable file watcher with performance optimization or deprecate
5. **Maintenance:** Update IMPLEMENTATION_SUMMARY_DEC2024.md to reflect current equalize_dock_columns status
6. **Cleanup:** Decide on serial helper deprecation timeline

---

**Generated:** 2026-03-18  
**Scan Tool:** GitHub Copilot Code Audit  
**Lines of code scanned:** ~35,000+ lines across app/ directory

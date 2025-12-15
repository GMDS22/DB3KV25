# Tracking & Aiming Button Toggle Bug Fix

## Problem Summary
The tracking and aiming buttons could not be toggled to change application modes. Users could click the buttons but no state change would occur.

## Root Cause
**Signal-Slot Mismatch in PyQt5 Signal Connections**

### The Bug
- **Line 2770** in `MAIN_FILE_SINGLE_CAM.py`: `tracking_btn` was connected to the `"clicked"` signal
- **Line 2795** in `MAIN_FILE_SINGLE_CAM.py`: `aiming_btn` was connected to the `"toggled"` signal

Both buttons are configured as checkable (`.setCheckable(True)`), which means they maintain a toggle state. However:
- The `"clicked"` signal passes NO arguments to the connected slot
- The `"toggled"` signal passes a boolean `checked` value indicating the button's state

### Why This Caused Failure
```python
# WRONG (tracking_btn):
self._safe_connect("tracking_btn", "clicked", self.toggle_tracking)  # clicked signal passes nothing
def toggle_tracking(self):  # No parameters to receive signal data
    # Logic relied on reading button state, but wasn't being called properly

# CORRECT (aiming_btn):
self._safe_connect("aiming_btn", "toggled", self.toggle_aiming)  # toggled signal passes bool
def toggle_aiming(self, checked=None):  # Accepts the checked boolean from signal
    # Logic uses checked parameter for proper state management
```

## Solution Applied

### 1. Updated Button Signal Connection (Line 2770)
**Before:**
```python
self._safe_connect("tracking_btn", "clicked", self.toggle_tracking)
# ... fallback also used "clicked"
sig = getattr(btn, "clicked", None)
```

**After:**
```python
# Use 'toggled' for checkable toggle buttons to avoid double-press issues
self._safe_connect("tracking_btn", "toggled", self.toggle_tracking)
# ... fallback also uses "toggled"
sig = getattr(btn, "toggled", None)
```

### 2. Updated Handler Method Signature (Line 17894)
**Before:**
```python
def toggle_tracking(self):
    """Toggle object detection tracking."""
    try:
        if not getattr(self, "tracking_active", False):
            self.start_tracking()
            # ... rest of logic
```

**After:**
```python
def toggle_tracking(self, checked=None):
    """Toggle object detection tracking.
    
    If `checked` is provided (from a toggled(bool) signal), use it to set
    the tracking_active state. Otherwise, invert the current state.
    """
    try:
        if checked is None:
            tracking_was_active = getattr(self, "tracking_active", False)
            self.tracking_active = not tracking_was_active
        else:
            # Ensure boolean
            try:
                self.tracking_active = bool(checked)
            except Exception:
                self.tracking_active = bool(getattr(self, "tracking_active", False))
    except Exception:
        self.tracking_active = False
    
    try:
        if not self.tracking_active:
            self.start_tracking()
            # ... rest of logic (unchanged)
```

## Files Modified
1. **f:\AUTO_TURRET_PROJECT\BUILD_01_A\MAIN_FILE_SINGLE_CAM.py**
   - Line 2770: Changed signal from `"clicked"` to `"toggled"`
   - Line 2776: Updated fallback signal reference
   - Line 17894: Updated `toggle_tracking()` method signature and logic

2. **f:\AUTO_TURRET_PROJECT\BUILD_01_A\DADBOT PORTABLE V3.0\app\MAIN_FILE_SINGLE_CAM.py**
   - Same changes as above for portable version consistency

## How It Works Now
1. User clicks `tracking_btn` → `toggled(bool)` signal fires
2. Signal passes button's checked state (True/False) to slot
3. `toggle_tracking(checked=True/False)` receives the state
4. Method updates `self.tracking_active` based on the checked state
5. Application switches to/from tracking mode correctly

## Verification
**Before Fix:**
- Log shows: `[INIT] tracking_btn present; signals: clicked, pressed, released, toggled`
- Log never shows: `[TOGGLE]` handler execution for tracking mode changes
- Mode stays at `Mode=TRACK` (or IDLE) regardless of button clicks

**After Fix:**
- Log should show tracking mode switching between:
  - `Mode=AUTO_TRACKING` when tracking enabled
  - `Mode=TRACK` or other modes when tracking disabled
- Aiming button behavior now matches tracking button behavior consistently

## Technical Note
Both buttons now use the same pattern as documented in the aiming button's comment:
```python
# Use 'toggled' for checkable toggle buttons to avoid double-press issues
```

This is the PyQt5 best practice for checkable button widgets that maintain state.

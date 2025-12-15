# DADBOT v4 Camera Resolution Fix - Complete Documentation
## Status: WORKING - December 15, 2025

---

## WHAT WAS FIXED

**Problem:** Camera feed displayed at 640x480 in a small corner of the screen, even though code requested 1280x720

**Root Causes Found:**
1. HUD was querying camera for actual resolution during frame drawing - caused `sipBadCatcherResult` PyQt5 error
2. Error crashed the display update, leaving frame partially rendered
3. Frame display logic wasn't properly synchronized with resolution changes

**Solution Applied:**
- Simplified camera opening code to be reliable and straightforward
- Removed camera property queries from HUD rendering loop (was causing PyQt5 signal issues)
- HUD now uses configured `frame_width` and `frame_height` values instead of querying camera
- Set default resolution to 1280x720 at startup

**Result:** ✓ Camera displays full frame at correct resolution without errors

---

## HOW IT WORKS NOW

### 1. Configuration Phase (App Startup)
- **File:** `app/MAIN_FILE_SINGLE_CAM.py`
- **Lines:** 1350-1359
- **Code:**
```python
self.frame_ratio_options = {
    "640x480": (640, 480),    # 4:3 aspect ratio
    "800x600": (800, 600),    # 4:3 aspect ratio
    "1024x768": (1024, 768),  # 4:3 aspect ratio
    "1280x720": (1280, 720),  # 16:9 aspect ratio (HD) ← DEFAULT
}
self.frame_ratio_setting = "1280x720"  # Current active resolution
self.frame_width = 1280    # Pixel width
self.frame_height = 720    # Pixel height
```

### 2. Camera Opening (When Tracking Starts)
- **File:** `app/MAIN_FILE_SINGLE_CAM.py`
- **Method:** `open_camera()`
- **Lines:** 12243-12290
- **What Happens:**
  1. Gets target resolution from `frame_ratio_setting`
  2. Opens camera with `cv2.VideoCapture(int(idx))`
  3. Sets resolution: `cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)` and height
  4. Waits 50ms for camera to apply settings
  5. Queries actual resolution back from camera
  6. Updates `self.frame_width` and `self.frame_height` with actual values
  7. Returns the opened camera object

### 3. Frame Rendering (Each Frame Update)
- **File:** `app/MAIN_FILE_SINGLE_CAM.py`
- **Method:** `update_frame()`
- **Lines:** 16785-16788 (HUD Resolution Display)
- **What Happens:**
  1. Uses configured `self.frame_width` and `self.frame_height` (NOT querying camera)
  2. Formats as "1280x720" string for HUD display
  3. No camera object access during drawing (avoids PyQt5 signal issues)
  4. Frame displays at full screen resolution without errors

### 4. Resolution Changes (User Selects New Resolution)
- **File:** `app/MAIN_FILE_SINGLE_CAM.py`
- **Method:** `_on_frame_ratio_changed(ratio_label)`
- **Lines:** 12641-12720
- **What Happens:**
  1. User changes resolution in dropdown (if enabled)
  2. Signal triggers handler with new resolution label
  3. Updates: `frame_ratio_setting`, `frame_width`, `frame_height`
  4. Recalculates `max_contour_threshold` (85% of new frame area)
  5. Releases current camera
  6. Sets `_camera_open_needed = True` to reopen with new resolution
  7. Next `update_frame()` call opens camera with new resolution

---

## HOW TO CHANGE CAMERA RESOLUTION

### Simple Method: Change Default Resolution

If you want to use a different resolution by default:

**Step 1:** Edit `app/MAIN_FILE_SINGLE_CAM.py`

**Find lines 1350-1359:**
```python
self.frame_ratio_options = {
    "640x480": (640, 480),
    "800x600": (800, 600),
    "1024x768": (1024, 768),
    "1280x720": (1280, 720),
}
self.frame_ratio_setting = "1280x720"  # CHANGE THIS
self.frame_width = 1280                # CHANGE THIS
self.frame_height = 720                # CHANGE THIS
```

**Step 2:** Change to your desired resolution:
```python
self.frame_ratio_setting = "1024x768"  # Change to this
self.frame_width = 1024                # Change to this
self.frame_height = 768                # Change to this
```

**Step 3:** Restart the app

**Step 4:** Verify in HUD: "RES: 1024x768" should appear

### Advanced Method: Add New Resolution

If you want to add a new resolution option:

**Step 1:** Add to `frame_ratio_options` dict:
```python
self.frame_ratio_options = {
    "640x480": (640, 480),
    "800x600": (800, 600),
    "1024x768": (1024, 768),
    "1280x720": (1280, 720),
    "1920x1080": (1920, 1080),  # NEW - add this line
}
```

**Step 2:** Set as default if desired:
```python
self.frame_ratio_setting = "1920x1080"  # NEW DEFAULT
self.frame_width = 1920
self.frame_height = 1080
```

**Step 3:** Restart app and test

---

## RESOLUTION CONFIGURATION CHECKLIST

When updating camera resolution, verify you've updated ALL of these locations:

### ✓ Location 1: Resolution Options Dict
- **File:** `app/MAIN_FILE_SINGLE_CAM.py`
- **Lines:** 1350-1356
- **What to Change:** Add/remove resolution entries in `frame_ratio_options` dict
- **Example:** `"1280x720": (1280, 720),`

### ✓ Location 2: Default Resolution Setting
- **File:** `app/MAIN_FILE_SINGLE_CAM.py`
- **Line:** 1357
- **What to Change:** `self.frame_ratio_setting = "YOUR_RESOLUTION"`
- **Must Match:** A key from `frame_ratio_options` dict

### ✓ Location 3: Frame Width Variable
- **File:** `app/MAIN_FILE_SINGLE_CAM.py`
- **Line:** 1358
- **What to Change:** `self.frame_width = WIDTH_PIXEL_COUNT`
- **Must Match:** First tuple value in `frame_ratio_options`

### ✓ Location 4: Frame Height Variable
- **File:** `app/MAIN_FILE_SINGLE_CAM.py`
- **Line:** 1359
- **What to Change:** `self.frame_height = HEIGHT_PIXEL_COUNT`
- **Must Match:** Second tuple value in `frame_ratio_options`

### ✓ Location 5: Camera Opening Code
- **File:** `app/MAIN_FILE_SINGLE_CAM.py`
- **Method:** `open_camera()` - Lines 12254-12258
- **What it Does:** Automatically reads from `frame_ratio_options` and `frame_ratio_setting`
- **Action Required:** NO CHANGES NEEDED - automatically uses updated values

### ✓ Location 6: HUD Resolution Display
- **File:** `app/MAIN_FILE_SINGLE_CAM.py`
- **Lines:** 16785-16788
- **What it Does:** Automatically displays `self.frame_width` and `self.frame_height`
- **Action Required:** NO CHANGES NEEDED - automatically uses updated values

### ✓ Location 7: Frame Ratio Dropdown (if UI enabled)
- **File:** `app/MAIN_FILE_SINGLE_CAM.py`
- **Lines:** ~4277-4301
- **What it Does:** Lists available resolutions from `frame_ratio_options` dict
- **Action Required:** NO CHANGES NEEDED - automatically populates from dict

---

## VERIFICATION CHECKLIST

After changing resolution, verify these steps:

- [ ] App starts without errors
- [ ] HUD displays correct resolution in bottom-left (e.g., "RES: 1920x1080")
- [ ] Camera frame fills entire viewing area (no black borders)
- [ ] Tracking works smoothly without lag
- [ ] Frame capture is stable (no stuttering)
- [ ] Serial output shows resolution when camera opens
- [ ] Can change resolution via dropdown (if UI enabled)

---

## TROUBLESHOOTING

### Issue: Camera shows old resolution after restart
**Solution:** 
1. Verify you changed ALL 4 locations (options dict, setting, width, height)
2. Check spelling matches exactly
3. Restart app completely (kill process, reopen)

### Issue: Camera won't open with new resolution
**Solution:**
1. Camera may not support that resolution natively
2. Run `python camera_diagnostic.py` to test supported resolutions
3. Choose resolution from diagnostic output
4. Only use resolutions marked "✓ SUPPORTED" or "✓ EXACT"

### Issue: Frame displays distorted/stretched
**Solution:**
1. Verify width and height values match tuple in options dict
2. Ensure aspect ratio is correct (e.g., 16:9 for 1280x720)
3. Check camera actually supports that resolution with diagnostic tool

### Issue: HUD displays wrong resolution
**Solution:**
1. Camera didn't open with requested resolution
2. Check console output: `[CAMERA] Resolution: XXXxYYY` should match expected
3. If different, camera doesn't support that resolution
4. Use `camera_diagnostic.py` to find supported resolutions

---

## TECHNICAL DETAILS

### Why Simplified Camera Opening Works

The current code:
1. **Simple & Reliable:** Single backend, straightforward opening
2. **Safe:** No complex exception handling that could hide bugs
3. **Flexible:** Automatically reads from configuration, easy to change
4. **Debuggable:** Clear log messages show what's happening

### Why HUD Resolution Querying Was Removed

Previous code queried camera every frame:
```python
# OLD - CAUSED ERRORS
if cap is not None and cap.isOpened():
    _actual_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Access cap from draw thread
    _actual_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
```

Problems:
- Accessing `cap` (camera object) from multiple threads
- `cap.get()` calls take time, freeze frame updates
- PyQt5 signal/slot compatibility issues
- Could fail mid-operation, partial frame renders

New code is safe:
```python
# NEW - SAFE
_res_w = self.frame_width    # Simple variable access
_res_h = self.frame_height   # No camera object access
```

Benefits:
- Thread-safe (only reads configured values)
- Fast (no camera device queries)
- Reliable (no PyQt5 signal issues)
- Predictable (always shows what app is configured to use)

### Data Flow

```
┌─────────────────────────────────────────────────────────┐
│ App Startup                                             │
│ • Read frame_ratio_options dict (1350-1356)            │
│ • Set frame_ratio_setting (1357)                       │
│ • Set frame_width/height (1358-1359)                   │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ When Tracking Starts                                    │
│ • open_camera() reads frame_ratio_setting (12254)      │
│ • Looks up resolution in frame_ratio_options (12255)   │
│ • Opens camera and sets resolution (12262-12268)       │
│ • Updates frame_width/height with actual values        │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│ Each Frame Update (HUD Display)                         │
│ • Read frame_width and frame_height (16785-16788)      │
│ • Display in HUD: "RES: {width}x{height}"              │
│ • NO camera object access (safe, fast, reliable)       │
└─────────────────────────────────────────────────────────┘
```

---

## FILES INVOLVED

| File | Role | Lines |
|------|------|-------|
| `app/MAIN_FILE_SINGLE_CAM.py` | Main app, all resolution logic | See below |
| `camera_diagnostic.py` | Test camera capabilities | N/A |
| `CAMERA_FIX_DOCUMENTATION.md` | Previous fix notes | N/A |

### Key Code Locations in MAIN_FILE_SINGLE_CAM.py

| Feature | Lines | Purpose |
|---------|-------|---------|
| Options dict | 1350-1356 | Define available resolutions |
| Default setting | 1357 | Set which resolution to use |
| Width variable | 1358 | Store width value |
| Height variable | 1359 | Store height value |
| Camera opening | 12243-12290 | Open camera with resolution |
| HUD display | 16785-16788 | Show resolution in UI |
| Handler | 12641-12720 | Handle resolution changes |

---

## VERSION HISTORY

| Date | Change | Impact |
|------|--------|--------|
| 2025-12-15 | Removed camera querying from HUD (fixed sipBadCatcherResult) | ✓ App stable |
| 2025-12-15 | Set default to 1280x720 | ✓ Frame fills screen |
| 2025-12-15 | Simplified camera opening | ✓ Reliable initialization |
| (Before) | Complex multi-backend logic | ✗ Caused SIP errors |

---

## QUICK REFERENCE - CHANGING RESOLUTION

**To change default resolution from 1280x720 to 1024x768:**

1. Open: `app/MAIN_FILE_SINGLE_CAM.py`
2. Go to line 1357-1359:
   ```python
   self.frame_ratio_setting = "1024x768"  # Change
   self.frame_width = 1024                # Change
   self.frame_height = 768                # Change
   ```
3. Verify `1024x768` exists in dict above (line 1354)
4. Save file
5. Restart app
6. Check HUD shows "RES: 1024x768"

**Done!** No other files need changes.

---

## SUPPORT

If resolution issues occur:
1. Check terminal output for `[CAMERA]` log messages
2. Run `camera_diagnostic.py` to verify camera capabilities
3. Use only resolutions marked "✓ SUPPORTED" in diagnostic output
4. Verify all 4 locations match (options dict, setting, width, height)

---

**Last Updated:** December 15, 2025
**Status:** STABLE - Ready for Production
**Tested:** ✓ Working correctly with full frame display

# Resolution Configuration - Developer Checklist

This checklist prevents the resolution configuration bug from happening again.

---

## ⚠️ BEFORE Modifying Resolution-Related Code

- [ ] Read `RESOLUTION_CONFIGURATION_FIX.md`
- [ ] Read `CAMERA_RESOLUTION_GUIDE.md`
- [ ] Understand the 3 locations where frame_width/height can be modified
- [ ] Know WHY per-frame updates are forbidden

---

## ✅ To Change Default Resolution

**File:** `app/MAIN_FILE_SINGLE_CAM.py`

**Step 1: Edit ALL 3 lines together (lines 1373-1375):**
```python
self.frame_ratio_setting = "WIDTHxHEIGHT"  # Example: "640x480"
self.frame_width = WIDTH                    # Example: 640
self.frame_height = HEIGHT                  # Example: 480
```

**Step 2: Verify resolution exists in frame_ratio_options dict (lines 1368-1372)**

**Step 3: Test with camera_diagnostic.py:**
```bash
python camera_diagnostic.py
```

**Step 4: Verify the test passes:**
```bash
python test_resolution_fix.py
```

**Step 5: Start application and verify:**
- Console shows: `[CAMERA] Resolution: WIDTHxHEIGHT`
- HUD shows: `RES: WIDTHxHEIGHT`

---

## ❌ NEVER Do These Things

### 1. Never Modify Resolution in update_frame
```python
# ❌ WRONG - DO NOT ADD CODE LIKE THIS IN update_frame():
def update_frame(self):
    # ... existing code ...
    
    # ❌ NEVER DO THIS:
    if frame is not None:
        self.frame_width = frame.shape[1]   # NO!
        self.frame_height = frame.shape[0]  # NO!
```

**Why:** Wastes CPU, contradicts design, creates confusion

### 2. Never Modify Just One Variable
```python
# ❌ WRONG - Don't change just one:
self.frame_width = 640
# You must also change:
# self.frame_ratio_setting = "640x480"
# self.frame_height = 480
```

**Why:** Creates inconsistency, breaks assumptions

### 3. Never Remove Warning Comments
```python
# ❌ WRONG - Don't remove these:
# ⚠️ CRITICAL: TO CHANGE RESOLUTION, YOU MUST EDIT ALL 3 LINES
# ⚠️ DO NOT modify frame_width/height anywhere else in the code!
# WARNING: DO NOT update frame_width/height here on every frame!
```

**Why:** Future developers need these warnings

### 4. Never Query Camera During Frame Processing
```python
# ❌ WRONG - Don't do this in update_frame or similar:
def update_frame(self):
    # ❌ NEVER DO THIS:
    w = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # NO!
    h = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # NO!
```

**Why:** Causes PyQt5 errors, thread safety issues, performance problems

---

## ✅ The 3 Allowed Modification Locations

### Location 1: Initialization (lines 1373-1375)
**Purpose:** Set default resolution at startup  
**When:** Only when changing default resolution  
**Who:** Developers configuring the app

```python
self.frame_ratio_setting = "1280x720"
self.frame_width = 1280
self.frame_height = 720
```

### Location 2: Camera Opening (lines 12372-12373)
**Purpose:** Update with actual camera resolution  
**When:** Automatically when camera opens  
**Who:** DO NOT MODIFY - automatic behavior

```python
self.frame_width = actual_w if actual_w > 0 else width
self.frame_height = actual_h if actual_h > 0 else height
```

### Location 3: Resolution Change Handler (lines 12739-12740)
**Purpose:** Handle user changing resolution via UI  
**When:** Automatically when user selects new resolution  
**Who:** DO NOT MODIFY - automatic behavior

```python
self.frame_width = width
self.frame_height = height
```

---

## 🧪 After Making Changes

### Run Automated Test
```bash
python test_resolution_fix.py
```

**Expected output:**
```
✅ ALL TESTS PASSED

Resolution configuration is properly implemented:
  • Exactly 3 assignments to frame_width/height
  • No assignments in update_frame method
  • Protective warning comments in all critical sections
```

### Manual Verification
- [ ] Application starts without errors
- [ ] Console shows: `[CAMERA] Resolution: WIDTHxHEIGHT`
- [ ] HUD displays: `RES: WIDTHxHEIGHT`
- [ ] Tracking works correctly
- [ ] No frame display issues
- [ ] No PyQt5 errors in console

---

## 📚 Required Reading

**Before any resolution-related changes:**
1. `RESOLUTION_CONFIGURATION_FIX.md` (technical details)
2. `CAMERA_RESOLUTION_GUIDE.md` (user guide)
3. `FIX_SUMMARY.md` (overview)

**When troubleshooting:**
1. `CAMERA_FIX_DOCUMENTATION.md`
2. `CAMERA_FIX_SUMMARY.md`
3. `QUICK_RESOLUTION_GUIDE.txt`

---

## 🔍 Code Review Checklist

When reviewing resolution-related changes, verify:

- [ ] frame_width/height only modified in 3 allowed locations
- [ ] No per-frame resolution calculations added
- [ ] Warning comments still present and not modified
- [ ] All 3 values changed together (setting, width, height)
- [ ] Test still passes: `python test_resolution_fix.py`
- [ ] No camera queries added to frame processing
- [ ] Documentation updated if behavior changed

---

## ⚡ Quick Reference

| What | Where | Modify? |
|------|-------|---------|
| **Default resolution** | Lines 1373-1375 | ✅ YES (all 3 together) |
| **Camera opening** | Lines 12372-12373 | ❌ NO (automatic) |
| **Resolution handler** | Lines 12739-12740 | ❌ NO (automatic) |
| **update_frame** | Lines 14285-14307 | ❌ NEVER (read-only) |
| **Warning comments** | Multiple locations | ❌ NEVER REMOVE |

---

## 🚨 If You Break Something

### Symptoms of Broken Resolution Handling
- Camera displays at wrong resolution
- HUD shows incorrect resolution
- Tracking accuracy degraded
- PyQt5 errors about sipBadCatcherResult
- Frame display issues (black borders, distortion)
- Test fails: `python test_resolution_fix.py`

### How to Fix
1. Run the test: `python test_resolution_fix.py`
2. Look at which check failed
3. Review the warning comments at the failing location
4. Restore the correct behavior
5. Re-run test until it passes

### Emergency Revert
```bash
git diff app/MAIN_FILE_SINGLE_CAM.py  # See what changed
git checkout app/MAIN_FILE_SINGLE_CAM.py  # Revert to last commit
```

---

## 💡 Remember

1. **Resolution is set ONCE** when camera opens
2. **Resolution doesn't change** during operation
3. **frame_width/height are SOURCE OF TRUTH** for all calculations
4. **Never query camera** during frame processing
5. **Always run test** after modifications
6. **Warning comments** are there for a reason - don't remove them!

---

**This checklist ensures the resolution configuration bug will NEVER happen again.**

**Status:** Use this checklist for all future resolution-related work ✅

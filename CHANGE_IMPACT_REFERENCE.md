
# PAN & TILT SERIAL BUS SERVO UPGRADE WITH CURRENT MONITORING (2026)

## OVERVIEW
This section documents the required steps, affected subsystems, and review checklist for the following upgrade:
- Upgrade both Pan and Tilt servos to serial bus servos (using debug board)
- Monitor each servo's current consumption separately in the monitor panel
- Monitor total turret current via a dedicated current sensor

**Servo information prerequisite (do before firmware/protocol work):**
Confirm and record the exact Pan/Tilt bus servo model + protocol details (half-duplex vs full-duplex, baud rate, packet framing, voltage/current specs). Reference images present in repo root:
- [ce27550c941036c537039cccbb3b8236.jpg_2200x2200q80.jpg](ce27550c941036c537039cccbb3b8236.jpg_2200x2200q80.jpg)
- [1efe7e1c372359451be7058f9abeda0e.jpg_2200x2200q80.jpg](1efe7e1c372359451be7058f9abeda0e.jpg_2200x2200q80.jpg)

Current working assumption (confirm against datasheet before wiring power):
- Yahboom **YB-SD35M** “35kg” serial bus servo
- Rotation range: **0–270°**
- Connectors: **3 × HY2.0-3Pin**

**MANDATORY AGENT INSTRUCTION:**
Whenever you see the instruction "INITIATE SERVO UPGRADE", you MUST review this section in full before making any code or documentation changes. Reference this section in all related PRs, commits, and agent-managed blocks.

---

## STEP-BY-STEP UPGRADE PROCESS

1. Update Nano/debug board firmware to:
        - Control both Pan and Tilt via serial bus servos (remove all PWM logic)
        - Report per-servo current (Pan, Tilt) and total current over serial
        - Document protocol and wiring in README.md and hardware setup docs
2. Update serial protocol documentation and Python serial parsing logic (MAIN_FILE_SINGLE_CAM.py, serial helpers) to:
        - Send/receive serial bus commands for both servos
        - Parse and handle per-servo and total current values
3. Update all servo control logic (MAIN_FILE_SINGLE_CAM.py, servo helpers) to:
        - Use serial bus protocol for both Pan and Tilt
        - Remove all PWM-based logic
4. Update the monitor panel UI (ui_builder.py, layout_manager.py) to:
        - Display Pan current, Tilt current, and Total current in real time
        - Ensure clear labeling and correct refresh logic
5. Update logging and diagnostics to:
        - Optionally log per-servo and total current readings
        - Update/add test scripts for serial bus servo control and current monitoring (SERIAL_CONNECTION_TEST.py, servo_fix_test.py)
6. Update presets/settings (turret_presets.py, preferred_defaults.json) to:
        - Add thresholds/alerts for Pan, Tilt, and Total current if needed
        - Document new settings
7. Update all documentation (CHANGE_IMPACT_REFERENCE.md, RECENT_UPDATES.json, README.md, hardware setup docs) to:
        - Reflect new protocol, UI, and settings
        - Reference this section in all related PRs, commits, and agent-managed blocks

---

## IMPACTED FILES/SUBSYSTEMS SUMMARY

| Area                | Files/Subsystems Impacted                                 |
|---------------------|----------------------------------------------------------|
| Firmware            | Nano/debug board firmware (external, must be documented) |
| Serial Protocol     | MAIN_FILE_SINGLE_CAM.py, serial helpers, docs            |
| Servo Logic         | MAIN_FILE_SINGLE_CAM.py, servo_fix_test.py, presets      |
| UI/Monitor Panel    | ui_builder.py, layout_manager.py, enhancements           |
| Settings/Presets    | turret_presets.py, preferred_defaults.json               |
| Logging             | serial_log_*.txt, logging helpers                        |
| Documentation       | CHANGE_IMPACT_REFERENCE.md, RECENT_UPDATES.json, README  |
| Testing             | SERIAL_CONNECTION_TEST.py, servo_fix_test.py             |

---

## AGENT/DEVELOPER CHECKLIST

- [ ] Review this section in full before making any changes.
- [ ] Confirm hardware/firmware and serial protocol changes.
- [ ] Update all affected code and documentation as listed above.
- [ ] Remove all PWM logic for both Pan and Tilt servos.
- [ ] Confirm per-servo and total current are parsed, displayed, and logged as required.
- [ ] Reference this section in all PRs, commits, and agent-managed blocks.

---
# CHANGE_IMPACT_REFERENCE.md

## AutoTracker System Change Impact Map

> **Document Version:** 1.0  
> **Last Updated:** 2025-12-20  
> **Maintainer:** AutoTracker Development Team

---

## 1. Overview

### Purpose

This document serves as the **single authoritative reference** for understanding cross-system dependencies and change impacts in the AutoTracker codebase. It exists to **prevent regressions** caused by incomplete modifications.

### Rules for Editors

1. **READ** the relevant section(s) **BEFORE** making any changes
2. **VERIFY** all listed dependencies and cross-effects after modifications
3. **UPDATE** this document when you discover new dependencies
4. **ADD** change warnings to sensitive files as specified in Section 10
5. **LOG** all functional changes in RECENT_UPDATES.json (app home tab) and optionally in the Change Log (Section 13)
6. **DOCUMENTATION WORKFLOW**: For traceability, update RECENT_UPDATES.json for every change. Create .md files only for complex changes (e.g., multi-file refactors). Avoid accumulating .md files by consolidating or archiving old ones quarterly.

### Critical Principles

- A "small change" in one subsystem **can and will** break another
- Never assume a change is isolated without checking this document
- If you modify hardcoded constants, **multiple subsystems WILL be affected**
- Test across ALL detection modes, not just the one you're debugging

---

## 2. Camera & Video Capture Pipeline

### Primary Responsibility
Captures video frames from USB camera/webcam, configures resolution, and provides frames to the detection/tracking pipeline.

### Primary Files
| File | Description |
|------|-------------|
| [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py) | Camera initialization (`open_camera`), frame reading (`_cap_read`), resolution config |
| [camera_diagnostic.py](camera_diagnostic.py) | Camera troubleshooting utilities |

### Supporting / Dependent Files
| File | Impact |
|------|--------|
| [app/ui_builder.py](app/ui_builder.py) | Video label widget sizing |
| [app/turret_presets.py](app/turret_presets.py) | Resolution-specific presets (Wide FOV, HD, Fast) |
| [app/sentry_mode/sentry_controller.py](app/sentry_mode/sentry_controller.py) | Frame dimensions for overlay calculations |
| [app/color_detection/color_detector.py](app/color_detection/color_detector.py) | Contour area calculations (resolution-dependent) |

### Direct Dependencies

| Constant/Config | Location | Current Value | Used By |
|-----------------|----------|---------------|---------|
| `frame_width` | MAIN_FILE_SINGLE_CAM.py:1645 | 1280 | Tracking math, deadzone, UI scaling, HUD positioning |
| `frame_height` | MAIN_FILE_SINGLE_CAM.py:1646 | 720 | Tracking math, deadzone, UI scaling, HUD positioning |
| `frame_ratio_setting` | MAIN_FILE_SINGLE_CAM.py:1644 | "1280x720" | Settings persistence, preset application |
| `frame_ratio_options` | MAIN_FILE_SINGLE_CAM.py:1638-1643 | dict | Resolution dropdown, camera configuration |
| Camera Index | settings.json:`camera_index` | 0 | Camera selection dropdown |

### If You Change ANY of the Following

#### Resolution (`frame_width`, `frame_height`)
You **MUST ALSO** check/update:
- [ ] `frame_ratio_setting` string (must match width×height)
- [ ] All 3 lines must be edited together (see CAMERA_RESOLUTION_GUIDE.md)
- [ ] `min_contour` / `max_contour` detection parameters (scale with area)
- [ ] `deadzone` value (pixel-based, does not auto-scale)
- [ ] `snap_threshold` value (pixel-based)
- [ ] HUD layout constants (`HUD_MARGIN`, `HUD_LINE_HEIGHT`)
- [ ] Crosshair rendering calculations in `_add_crosshair_and_scope()`
- [ ] Sentry overlay `frame_width`/`frame_height` 
- [ ] Coordinate mapping to servo angles (center calculation)
- [ ] Video label QLabel minimum sizes in UI builder

#### Camera Index
You **MUST ALSO** check/update:
- [ ] `camera_index_combo` UI dropdown selection
- [ ] Verify camera opens successfully before saving

### Hidden or Non-Obvious Dependencies

1. **Coordinate center calculation**: `cx = frame_width // 2` appears in multiple places - change one, miss others
2. **Background subtractor warmup**: Tied to frame count, indirectly affected by resolution (larger frames = more processing time)
3. **YOLO inference size**: Ultralytics may resize frames internally - resolution affects detection accuracy
4. **QLabel aspect ratio**: Video label uses `setScaledContents(False)` - resolution affects display scaling

### Common Failure Modes

| Symptom | Likely Cause |
|---------|--------------|
| Tracking drifts to edges | `frame_width`/`frame_height` mismatch with actual camera output |
| Crosshair off-center | Center calculation using old resolution values |
| Detections at wrong position | Coordinate mapping still using old frame size |
| Black video feed | Camera index changed but camera not available |
| Tiny video window | QLabel minimum size not updated |

### Required Verification Steps

1. Run app and verify video feed displays at expected size
2. Enable tracking with test target at frame center - servo should stay at home position
3. Move target to corners - verify full pan/tilt range is used
4. Check HUD text is readable and not overlapping
5. Test all detection modes (FrameDiff, BackSub, YOLO, Color)

---

## 3. Frame Processing & Detection Logic

### Primary Responsibility
Processes video frames to detect targets using multiple algorithms (YOLO, Frame Difference, Background Subtraction, Color Detection, Hybrid modes).

### Primary Files
| File | Description |
|------|-------------|
| [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py) | `update_frame()` main loop, detection mode switching |
| [app/yolo_detector.py](app/yolo_detector.py) | YOLO model loading and inference |
| [app/color_detection/color_detector.py](app/color_detection/color_detector.py) | HSV color-based detection |
| [app/color_detection/hybrid_fusion.py](app/color_detection/hybrid_fusion.py) | Multi-detector fusion logic |

### Supporting / Dependent Files
| File | Impact |
|------|--------|
| [app/turret_presets.py](app/turret_presets.py) | Detection parameters per preset |
| [app/sentry_mode/sentry_controller.py](app/sentry_mode/sentry_controller.py) | Uses detection boxes for ambush calculation |
| [app/tracking_enhancements.py](app/tracking_enhancements.py) | Centroid smoothing and tracking refinement |

### Direct Dependencies

**Important: which `settings.json` is actually used**
- When launched via [run.py](run.py), the process `chdir`s into [app](app), so the app will typically read/write [app/settings.json](app/settings.json) (not the repo-root [settings.json](settings.json)).
- There is also a template/default file at [app/config/settings.json](app/config/settings.json) that may be used by reset/restore flows.
- If detections suddenly look "ignored", confirm you are editing the *active* settings file (usually [app/settings.json](app/settings.json) when using [run.py](run.py)).

| Parameter | Location | Default | Affects |
|-----------|----------|---------|---------|
| `detection_mode_index` | settings.json | 3 | Which algorithm runs |
| `detection_show_advanced` | settings.json | false | UI compactness: shows/hides advanced detection controls |
| `threshold` | settings.json | 40 | Frame difference sensitivity |
| `min_contour` | settings.json | 300 | Minimum detection size (pixels<sup>2</sup>) |
| `max_contour` | settings.json | 1400000 | Maximum detection size (pixels<sup>2</sup>) |
| `blur_kernel` | settings.json | 7 | Noise reduction (must be odd) |
| `dilate_iter` | settings.json | 2 | Contour expansion iterations |
| `backsub_warmup` | settings.json | 30 | Frames before BackSub stabilizes |
| `yolo_confidence` | settings.json | 0.3 | YOLO detection threshold |
| `yolo_classes` | settings.json | "mouse, rodent" | YOLO target filter |
| `yolo_model` | settings.json | "yolov8n.pt" | Model file |

### Detection Mode Index Mapping
```
0 = Frame Difference (motion-only)
1 = Background Subtraction (MOG2)
2 = YOLO Object Detection
3 = BackSub + FrameDiff Hybrid
4 = Motion-Gated YOLO
5 = BackSub + YOLO Overlap
6 = Color Detection
7-9 = Color Hybrid modes
```

### If You Change ANY of the Following

#### Detection Thresholds (`threshold`, `min_contour`, `max_contour`)
You **MUST ALSO** check/update:
- [ ] Test at current resolution (values are pixel-based, not relative)
- [ ] Verify in ALL lighting conditions used by deployment
- [ ] Check preset values in `turret_presets.py` still make sense
- [ ] Test with actual target (not just hand waving)

**Code references (where these values come from / are applied)**
- UI widget defaults (SpinBoxes): [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L3775-L4003) and [app/ui_builder.py](app/ui_builder.py#L582-L623)
- Resolution-based `max_contour` helper: [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L2343-L2362)
- Settings load (JSON → UI widgets): [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L9960-L10112)
- Settings save (UI widgets → JSON): [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L10696-L10720)

**Resolution & contour scaling (why objects get "ignored")**
- `min_contour`/`max_contour` are **pixel area** filters. As resolution increases, the same real-world object occupies more pixels.
- If `max_contour` is accidentally set too low (example failure: `max_contour` in the low-thousands while running 1280×720), most real objects' contours exceed the cap and are discarded → **no boxes** → looks like detection is "ignoring objects".
- Safe baseline for 1280×720:
        - `threshold`: ~30–50
        - `blur_kernel`: 5–7
        - `min_contour`: 300–1000
        - `max_contour`: 200000–1400000 (choose higher if you see large targets being dropped)

#### Detection Mode Index
You **MUST ALSO** check/update:
- [ ] `detection_mode_combo` UI dropdown text must match index
- [ ] Verify YOLO model loaded if switching to YOLO-based mode
- [ ] Clear `backSub` if switching away from BackSub mode
- [ ] Reset `backsub_warmup` counter for fresh background model

#### YOLO Configuration
You **MUST ALSO** check/update:
- [ ] Model file exists in `YOLO_MODELS/` directory
- [ ] Class names are valid for loaded model (COCO classes vs custom)
- [ ] Confidence threshold is appropriate for model
- [ ] GPU/CPU mode environment variable (`TURRET_USE_GPU`)

### Hidden or Non-Obvious Dependencies

1. **BackSub warmup**: First 30 frames are unstable - don't test immediately after mode switch
2. **Frame difference requires motion**: Static targets invisible to mode 0
3. **YOLO class names are case-sensitive**: "Person" ≠ "person"
4. **Color detection HSV vs BGR**: OpenCV uses BGR, color presets expect HSV
5. **Hybrid mode order**: Some modes AND results, others OR - affects sensitivity

### Common Failure Modes

| Symptom | Likely Cause |
|---------|--------------|
| No detections at all | Mode switched but detector not initialized |
| Ghost detections | `backsub_warmup` not completed, or `threshold` too low |
| Misses small targets | `min_contour` too high for current resolution |
| Tracks entire frame | `max_contour` not scaled for resolution |
| YOLO detects wrong objects | `yolo_classes` filter misconfigured |
| Color detection fails | HSV values wrong (use color picker tool) |

### Required Verification Steps

1. Switch to each detection mode and verify detections appear
2. Test with stationary target (YOLO, Color) and moving target (FrameDiff)
3. Verify bounding boxes draw around correct objects
4. Check serial log for detection coordinates
5. Test detection loss behavior (target leaving frame)

### Hybrid Mode 4/5 Threshold Semantics (INTENDED)

Hybrid modes 4 and 5 intentionally treat their UI values as **percentages (0–100)** stored in settings, then convert to **fractions (0.0–1.0)** at runtime.

| Parameter | Settings Key | Units in UI/JSON | Runtime Units | Default | Where Applied |
|----------|--------------|------------------|--------------|---------|--------------|
| Motion gate threshold | `motion_gate_threshold` | % of frame pixels that must move | fraction of frame area | 1.0 | [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L15394) (Mode 4)
| Overlap threshold | `overlap_threshold` | % box overlap required | fraction of YOLO box area | 30.0 | [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L15462-L15545) (Mode 5)

**Code references (defaults, persistence, and conversion)**
- Defaults initialized: [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L1707-L1709)
- UI spinbox defaults/ranges (0–100): [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L4419-L4446)
- Settings load (JSON → UI): [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L10305-L10310)
- Settings save (UI → JSON): [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L10514-L10515)
- Percent → fraction conversion: [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L15394) and [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L15462)

#### If You Change ANY of the Following

##### `motion_gate_threshold` / `overlap_threshold`
You **MUST ALSO** check/update:
- [ ] UI defaults in `QDoubleSpinBox.setValue(...)` (must stay in **percent** units): [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L4422-L4440)
- [ ] JSON keys in `load_settings()` and `save_settings()` (must match exactly): [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L10305-L10310) and [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L10514-L10515)
- [ ] Runtime conversion (`/ 100.0`) remains correct for comparisons: [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L15394) and [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L15462)
- [ ] Hybrid mode 4 motion source: `threshold_input` still controls the FrameDiff gate sensitivity
- [ ] Debug print formatting uses `*100` (keep units consistent): [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L15448) and [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L15545)

---

## 4. UI / Widget Layout & Scaling

### Primary Responsibility
Creates and manages all PyQt5 widgets, dock panels, menus, and visual layout.

### Primary Files
| File | Description |
|------|-------------|
| [app/ui_builder.py](app/ui_builder.py) | Widget creation and layout logic |
| [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py) | `init_ui()`, dock configuration, tab setup |
| [app/theme_manager.py](app/theme_manager.py) | Dark/light theme stylesheets |
| [app/turret_enhancements.py](app/turret_enhancements.py) | Status bar, top ARM bar, serial console |

### Supporting / Dependent Files
| File | Impact |
|------|--------|
| [app/layout_manager.py](app/layout_manager.py) | Save/load dock positions |
| [app/keyboard_shortcuts_window.py](app/keyboard_shortcuts_window.py) | Keyboard shortcut UI |
| [app/idle_settings_window.py](app/idle_settings_window.py) | Idle mode configuration window |
| [app/calibration_panel.py](app/calibration_panel.py) | Servo calibration UI |
| [app/checklist_panel.py](app/checklist_panel.py) | Code validation checklist |

### Direct Dependencies

| Constant | Location | Default | Affects |
|----------|----------|---------|---------|
| `DEFAULT_DOCK_COLUMN_WIDTH` | MAIN_FILE_SINGLE_CAM.py:1286 | 320 | Left/right panel widths |
| Widget minimum sizes | ui_builder.py, various | varies | Layout constraints |
| Window geometry | settings.json:`window_geometry` | base64 | Saved window position |
| Window state | settings.json:`window_state` | base64 | Saved dock arrangement |

### Widget Signal Connections (CRITICAL)

The following widgets have signals that MUST be connected correctly:

| Widget | Signal | Handler | File |
|--------|--------|---------|------|
| `tracking_btn` | `toggled` | `toggle_tracking` | MAIN_FILE_SINGLE_CAM.py + ui_builder.py |
| `aiming_btn` | `toggled` | `toggle_aiming` | MAIN_FILE_SINGLE_CAM.py + ui_builder.py |
| `connect_button` | `clicked` | `handle_connect_sound` | MAIN_FILE_SINGLE_CAM.py + ui_builder.py |
| `connection_preset_combo` | `currentIndexChanged` | `apply_preset` | MAIN_FILE_SINGLE_CAM.py + ui_builder.py |
| `idle_mode_toggle_btn` | `clicked` | `toggle_idle_mode` | MAIN_FILE_SINGLE_CAM.py |
| `go_home_button` | `clicked` | `go_home` | MAIN_FILE_SINGLE_CAM.py + ui_builder.py |
| `sound_checkbox` | `stateChanged` | `set_sound_enabled` | MAIN_FILE_SINGLE_CAM.py + ui_builder.py |

### If You Change ANY of the Following

#### Target Detection Panel Visibility (Basic/Advanced + mode-aware)
You **MUST ALSO** check/update:
- [ ] `update_detection_settings_visibility()` rules match the Detection Mode Index mapping (modes 0–9)
- [ ] Settings key `detection_show_advanced` is loaded/saved consistently
- [ ] Color panel helpers used by the main UI remain in sync (advanced/custom/hybrid visibility)

**Code references**
- Main UI visibility logic: [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py) (`update_detection_settings_visibility`, `_on_show_advanced_detection_changed`, `on_detection_mode_change`)
- Color panel visibility helpers: [app/color_detection/ui_components.py](app/color_detection/ui_components.py) (`set_color_advanced_visible`, `set_color_custom_hsv_visible`, `set_color_hybrid_visible`)

#### Widget Names
You **MUST ALSO** check/update:
- [ ] `_safe_connect()` calls using that widget name
- [ ] `load_settings()` / `save_settings()` field mapping
- [ ] Tooltip assignments in `_apply_tooltip_styles_and_texts()`
- [ ] Any `getattr(self, "widget_name", None)` references

#### Dock Panel Layout
You **MUST ALSO** check/update:
- [ ] `window_state` base64 in settings becomes invalid - user needs reset
- [ ] Layout presets in `app/layouts/*.json`
- [ ] `layout_manager.py` dock registration

#### Signal Connections
You **MUST ALSO** check/update:
- [ ] Use `_safe_connect()` helper, not direct `.connect()`
- [ ] Verify signal signature matches handler parameters
- [ ] Check for duplicate connections (causes double-fire)
- [ ] Checkable buttons use `toggled`, not `clicked`

### Hidden or Non-Obvious Dependencies

1. **`_safe_connect()` pattern**: Wraps signal connections with error handling - don't bypass
2. **Qt threading**: UI updates must be on main thread - use `serial_text_signal.emit()`
3. **Widget existence**: Many widgets guarded by `getattr(self, "widget", None)` - None causes silent failures
4. **Tooltip filters**: Custom tooltip filters installed - modifying styles may not take effect
5. **Tab widget structure**: Video/Notes/Home are tabs, not docks - different lifecycle

### Common Failure Modes

| Symptom | Likely Cause |
|---------|--------------|
| Button does nothing when clicked | Signal not connected, or wrong signal type |
| UI freezes during operation | Blocking call on main thread (camera, serial) |
| Widget shows wrong value | `load_settings()` field name mismatch |
| Setting not persisted | `save_settings()` missing the field |
| Dock panels overlap | Invalid `window_state` from different version |

### Dock Equalize Freeze Risk (Tools Menu)

**Symptom**: App appears to freeze/hang when using Tools → "Auto Equalize Dock Columns" or "Force Exact Dock Widths".

**Root cause class**: Dock resizing triggers a burst of Qt layout/repaint events while the main frame timer is still running (`update_frame()`), which can starve the UI thread. Re-entrant equalize calls during `LayoutRequest` can also lock the event loop.

**Required safeguards (DO NOT REMOVE)**
- Pause the frame timer during layout operations using the RESIZE-FIX helper `_pause_frame_timer_for_layout()`.
- Re-entrancy guard in `equalize_dock_columns()` (skip if already in progress).
- Defer menu-triggered equalize work via `QTimer.singleShot(0, ...)` so it runs outside the menu event handler.

**Code references**
- Tools menu actions calling equalize (deferred): [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L6660-L6765)
- Dock equalize implementation + re-entrancy guard + updates pause: [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L8550-L8960)
- RESIZE-FIX timer pause helpers: [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L20555-L20605)

### Hardware Tests (Tools Menu)

**Feature**: Tools → “🧪 Pan/Tilt Range Check” runs a slow sweep to help separate software vs. hardware issues (especially “tilt not moving”).

**Design constraints (DO NOT BREAK)**
- Must be **non-blocking** (QTimer-driven), never sleeps/loops on the Qt main thread.
- Must **pause/cancel tracking** for the duration of the test so autotracking does not fight the sweep.
- Must **restore prior runtime state** (tracking/aiming/detection flags and target angles) on completion/cancel.
- Must be isolated under `app/hardware_tests/` to allow expansion to other diagnostics.

**Confirmation limitations**
- If encoder feedback is enabled, the tool can best-effort confirm tilt movement.
- Without encoder feedback, the tool can only report that commands were issued and prompt the user to verify wiring/power/firmware/mechanics.

**Code references**
- Tools menu action wiring: [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py)
- Test runner: [app/hardware_tests/pan_tilt_range_check.py](app/hardware_tests/pan_tilt_range_check.py)

### Required Verification Steps

1. Click every button and verify expected action occurs
2. Change every slider/spinbox and verify value persists after restart
3. Toggle checkboxes and verify state persists
4. Rearrange docks and verify layout loads correctly on restart
5. Test keyboard shortcuts activate correct functions

---

## 5. Coordinate Mapping (Frame → Servo)

### Primary Responsibility
Converts target pixel coordinates from camera frame to servo pan/tilt angles.

### Primary Files
| File | Description |
|------|-------------|
| [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py) | Error calculation, PID/smoothing, angle computation |
| [app/tracking_enhancements.py](app/tracking_enhancements.py) | Centroid smoothing algorithms |

### Direct Dependencies

| Parameter | Location | Default | Affects |
|-----------|----------|---------|---------|
| `frame_width` | MAIN_FILE_SINGLE_CAM.py | 1280 | Center X calculation |
| `frame_height` | MAIN_FILE_SINGLE_CAM.py | 720 | Center Y calculation |
| `PAN_MIN` / `PAN_MAX` | MAIN_FILE_SINGLE_CAM.py | 0 / 220 | Servo angle limits |
| `TILT_MIN` / `TILT_MAX` | MAIN_FILE_SINGLE_CAM.py | 0 / 70 | Servo angle limits |
| `deadzone` | settings.json | 53 | No-movement zone (pixels) |
| `snap_threshold` | settings.json | 377 | Distance for instant snap (pixels) |
| `smoothing_factor` | settings.json | 0.7 | IIR filter coefficient |
| `movement_sensitivity` | settings.json | 74 | Error-to-movement gain |
| `tracking_speed` | settings.json | 80 | Overall speed multiplier |
| `invert_pan` | settings.json | true | UI checkbox state persisted for pan inversion |
| `invert_tilt` | settings.json | false | UI checkbox state persisted for tilt inversion |
| `flip_pan_direction` | runtime variable | varies | Internal pan direction used by tracking math (`pan_dir`) |
| `flip_tilt_direction` | runtime variable | varies | Internal tilt direction used by tracking math (`tilt_dir`) |

### Coordinate Flow
```
Detection Box (x, y, w, h) in pixels
        ↓
Centroid Calculation: cx = x + w/2, cy = y + h/2
        ↓
Error from Center: err_x = cx - frame_width/2, err_y = cy - frame_height/2
        ↓
Deadzone Check: if |err_x| < deadzone and |err_y| < deadzone → no movement
        ↓
Scaling: scaled_err = err * movement_sensitivity * tracking_speed
        ↓
Smoothing: new_angle = old_angle * smoothing + target_angle * (1 - smoothing)
        ↓
Clamping: angle = clamp(angle, MIN, MAX)
        ↓
Servo Command: P{pan}T{tilt}F{fire}...
```

### If You Change ANY of the Following

#### Frame Dimensions
You **MUST ALSO** check/update:
- [ ] Center calculation: `frame_width // 2`, `frame_height // 2`
- [ ] Deadzone value (absolute pixels, not relative)
- [ ] Snap threshold (absolute pixels)
- [ ] Min/max contour areas

#### Servo Limits (PAN_MIN, PAN_MAX, TILT_MIN, TILT_MAX)
You **MUST ALSO** check/update:
- [ ] Home position (`HOME_PAN`, `HOME_TILT`) must be within limits
- [ ] Spinbox ranges in UI (`pan_min_input`, `pan_max_input`, etc.)
- [ ] UI defaults vs internal defaults MUST match (or Apply New Limits will re-introduce legacy/unsafe values)
- [ ] Guard mode patrol points (may be out of new range)
- [ ] Arduino firmware limits (must match or be wider)
- [ ] Preset values that specify explicit angles

**Critical code references (servo limits + apply button)**
- Reset/default widget values for Servo Limits (must match internal defaults): [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L9781-L9792)
- Apply button handler that reads the spinboxes and pushes limits to MCU: [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L13933)

#### Servo Calibration File (`servo_calibration.json`)

You **MUST ALSO** check/update:
- [ ] Main app calibration loader uses a **script-relative** `servo_calibration.json` (do not depend on process CWD)
- [ ] Tools → "📏 Servo Calibration" launches `app/servo_calibration_tool.py` reliably and reads/writes the same script-relative file

**Why this matters**
- If calibration paths are CWD-dependent, multiple calibration files can be created and the tool/app will disagree about what limits are active.

#### Inversion Flags (`flip_pan_direction`, `flip_tilt_direction`)
You **MUST ALSO** check/update:
- [ ] Manual control direction (arrow keys)
- [ ] Go Home movement direction
- [ ] Quick Strike snap direction
- [ ] Guard mode patrol point interpretation

**Split-brain state risk (common regression class)**
- UI persists `invert_pan` / `invert_tilt`, while tracking math uses internal `flip_pan_direction` / `flip_tilt_direction`.
- If init/load order changes or signals don’t fire, the UI checkbox can show one state while internal `flip_*` flags remain stale.
- Symptom pattern: **runaway pan toward limit**, **wrong-direction chase**, or **tilt appears dead** even though serial commands look valid.

**Required invariant (enforce in code reviews)**
- After settings load and after default UI init, the internal `flip_*` flags must be explicitly synced from the checkbox states (do not rely solely on Qt signals firing).

**Code references (source of truth + sync points)**
- UI checkboxes: [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L5425-L5635)
- Internal setters used by UI signals: [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L8740-L8860)
- Settings persistence keys: [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L11302-L11304)
- Load-time sync (must exist): [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L10040-L10110)

### Runbook: “Pan drifts to max / Tilt not moving”

Use this exact order to avoid chasing symptoms.

1) **Confirm active settings source (avoid config drift)**
- If running via [run.py](run.py), the process `chdir`s into [app](app) and uses [app/settings.json](app/settings.json).

2) **Check direction state (UI vs internal)**
- Verify `invert_pan` / `invert_tilt` in the active settings file.
- In a debug log, confirm internal `flip_pan_direction` / `flip_tilt_direction` match the checkbox states.

3) **Validate the command stream (hardware truth)**
- In serial logs, check `WILL SEND: P..T..` changes in both P and T while the target moves.
- If `T` never changes but target tilt changes, look for tilt suppression gates (tilt safety latch, command overrides).

4) **Rule out tilt-safety suppression**
- Confirm `_mcu_tilt_safety_locked` is not latched from generic status lines.
- Confirm optional hardware flags (`tilt_safety_hardware_installed`, `tilt_safety_switch_enabled`) are correct.

5) **Only then tune detection/tracking**
- Verify `err_x/err_y` signs and that deadzone/snap settings are appropriate for the current resolution.

### Hidden or Non-Obvious Dependencies

1. **Integer rounding**: `int()` truncates, `round()` is more accurate - see `send_serial_command()` fix
2. **Fractional accumulator**: Sub-degree movements accumulate until threshold crossed
3. **Smoothing creates lag**: High smoothing = smooth but slow response
4. **Deadzone is center-relative**: Not a percentage, absolute pixels from frame center
5. **Tilt safety override**: MCU can lock tilt axis - host calculations ignored

**Current hardware note (Dec 2025)**
- Tilt safety encoder/switch hardware is not installed yet.
- The app now treats tilt-safety as **optional hardware** and gates both MCU message parsing and tilt suppression behind `tilt_safety_hardware_installed` + `tilt_safety_switch_enabled`.
- With defaults (`tilt_safety_hardware_installed=False`, `tilt_safety_switch_enabled=False`), tilt safety will not affect motion logic.

**Tilt freeze investigation anchors (pan moves, tilt stuck)**
- Tilt suppression gate (forces tilt_angle to last sent): [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L18370-L18392)
- MCU response parsing that latches/clears `_mcu_tilt_safety_locked`: [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L18610-L18666)

**Important nuance (real-world failure mode)**
- Some firmware prints status lines like "TILT SAFETY: OK". If host parsing latches on any "TILT SAFETY" substring, tilt can become permanently suppressed even though safety is OK. Host parsing must only lock on explicit trigger/locked messages, and clear on OK/reset.

**Serial command correctness (easy-to-overlook ordering bug class)**
- Command string must be built after any pan/tilt overrides (micro-step, safety overrides): [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L18389-L18393)

### Common Failure Modes

| Symptom | Likely Cause |
|---------|--------------|
| Servo moves wrong direction | Inversion flag wrong, or cable swapped |
| Servo doesn't reach corners | MIN/MAX limits too restrictive |
| Servo oscillates around target | Smoothing too low, or gain too high |
| Servo barely moves | Deadzone too large, or sensitivity too low |
| Tilt unresponsive | `int()` truncation losing fractional degrees |
| Tilt not moving but pan moves | Host is suppressing tilt due to MCU tilt-safety latch (`_mcu_tilt_safety_locked`), sometimes caused by overly broad parsing of "TILT SAFETY" status lines |

### Required Verification Steps

1. Target at frame center → servo at home position (no movement)
2. Target at frame left edge → servo pans left
3. Target at frame right edge → servo pans right
4. Target at frame top → servo tilts up
5. Target at frame bottom → servo tilts down
6. Rapid target movement → servo tracks smoothly without overshoot

---

## 6. Serial Communication / Arduino Interface

### Primary Responsibility
Manages serial port connection to Arduino/MCU and sends control commands.

### Primary Files
| File | Description |
|------|-------------|
| [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py) | `toggle_serial_connection()`, `send_serial_command()` |
| [app/turret_enhancements.py](app/turret_enhancements.py) | Serial console formatting, logging |
| [app/helpers/serial_ui_helpers.py](app/helpers/serial_ui_helpers.py) | Serial UI utilities |
| [SERIAL_CONNECTION_TEST.py](SERIAL_CONNECTION_TEST.py) | Standalone serial testing |

### Direct Dependencies

| Parameter | Location | Default | Affects |
|-----------|----------|---------|---------|
| `com_port` | settings.json | "COM3" | Which port to connect |
| `baud_rate` | settings.json | 115200 | Connection speed |
| `serial_timeout` | MAIN_FILE_SINGLE_CAM.py | 0.1s | Read timeout |

### Serial Command Protocol

Command format: `P{pan}T{tilt}F{fire}L{led}R{laser}G{acc}S{safety}M{mode}\n`

| Token | Range | Description |
|-------|-------|-------------|
| P | 0-255 | Pan servo angle (degrees) |
| T | 0-180 | Tilt servo angle (degrees) |
| F | 0/1 | Fire relay (0=off, 1=fire) |
| L | 0/1 | LED relay state |
| R | 0/1 | Laser relay state |
| G | 0/1 | Accessory relay |
| S | 0/1 | Safety state (0=armed, 1=safe) |
| M | 0/1 | Trigger mode (0=single, 1=burst) |

### If You Change ANY of the Following

#### Serial Protocol
You **MUST ALSO** check/update:
- [ ] Arduino firmware command parser (must match exactly)
- [ ] Command string construction in `send_serial_command()`
- [ ] Redundant command filter comparison
- [ ] Any test scripts that send commands

#### Port/Baud Configuration
You **MUST ALSO** check/update:
- [ ] UI combo box selections
- [ ] `settings.json` defaults
- [ ] Connection status display
- [ ] Arduino firmware baud rate

#### Fire/Safety Logic
You **MUST ALSO** check/update:
- [ ] ARM button state sync
- [ ] Fire indicator pulse timing
- [ ] Auto-fire enable flag
- [ ] Rapid-fire duty cycle
- [ ] Safety interlock checks

### Hidden or Non-Obvious Dependencies

1. **Redundant command filter**: Same command won't resend - prevents jitter but can miss state recovery
2. **Background thread connection**: Serial connect runs in thread - don't block UI
3. **TX pause feature**: `serial_tx_paused` stops sending without disconnecting
4. **Fire timeout**: `_max_firing_duration` prevents stuck trigger (default 3s)
5. **Tilt safety interlock**: MCU can report tilt locked - host must respect

### Common Failure Modes

| Symptom | Likely Cause |
|---------|--------------|
| "Port not found" error | Wrong COM port, or device disconnected |
| Commands ignored by Arduino | Baud rate mismatch |
| Servo twitches on connection | First command sends immediately (sentinel values) |
| Fire doesn't stop | Fire timeout not enforced, or flag stuck |
| Commands appear in log but servo doesn't move | TX paused, or redundant filter blocking |

### Required Verification Steps

1. Connect and verify "Connected" status
2. Manual control moves servo (arrow keys)
3. Toggle ARM and verify Arduino responds
4. Fire trigger and verify it stops after timeout
5. Disconnect and verify clean state reset

---

## 7. Timing, FPS, and Performance Control

### Primary Responsibility
Manages frame update timing, FPS calculation, and performance monitoring.

### Primary Files
| File | Description |
|------|-------------|
| [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py) | `update_frame()` timing, timer intervals |
| [app/turret_enhancements.py](app/turret_enhancements.py) | FPS display updates |

### Direct Dependencies

| Timer | Interval | Purpose |
|-------|----------|---------|
| `main_timer` | 33ms (~30fps) | Frame update loop |
| `serial_timer` | 50ms (20Hz) | Serial command send |
| `rapid_fire_timer` | variable | Burst fire pulses |
| `_notes_autosave_timer` | 5000ms | Notes auto-save |

### If You Change ANY of the Following

#### Timer Intervals
You **MUST ALSO** check/update:
- [ ] FPS calculation expects main_timer interval
- [ ] Serial command rate must not exceed Arduino processing
- [ ] Rapid fire timing directly affects duty cycle
- [ ] Very fast timers (< 16ms) may not be accurate

#### Processing in Timer Callbacks
You **MUST ALSO** check/update:
- [ ] Long operations block UI - use background threads
- [ ] Don't call `update_frame()` recursively
- [ ] YOLO inference time can exceed timer interval

### Hidden or Non-Obvious Dependencies

1. **FPS includes processing time**: Displayed FPS = actual frame rate, not timer rate
2. **Serial send rate independent of frame rate**: Can send commands faster than frames
3. **BackSub warmup is frame-count based**: Faster FPS = faster warmup
4. **Recording FPS vs display FPS**: Recording uses separate setting

### Common Failure Modes

| Symptom | Likely Cause |
|---------|--------------|
| Low FPS (< 15) | Detection taking too long, or camera slow |
| UI freezes periodically | Blocking operation in timer callback |
| Servo jitters | Serial timer too fast, sending redundant commands |
| Recording stutters | Recording FPS mismatch with actual FPS |

### Required Verification Steps

1. FPS counter shows stable 25-30 fps
2. UI remains responsive during tracking
3. Servo movements are smooth, not jerky
4. No "QObject::timerEvent" warnings in console

---

## 8. Threading / Async Execution

### Primary Responsibility
Manages background operations that would otherwise block the UI.

### Primary Files
| File | Description |
|------|-------------|
| [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py) | Threading for camera open, serial connect |
| [app/helpers/logger.py](app/helpers/logger.py) | Thread-safe logging |

### Threaded Operations

| Operation | Location | Notes |
|-----------|----------|-------|
| Camera opening | `update_frame()` | Daemon thread, can timeout |
| Serial connection | `toggle_serial_connection()` | Signal-based result handling |
| YOLO model loading | `yolo_detector.py` | Can block 5-30 seconds |

### Thread Safety Rules

1. **Never update UI from background thread** - use `signal.emit()`
2. **Serial port access is single-threaded** - don't read/write from multiple threads
3. **OpenCV operations are not thread-safe** - frame access must be synchronized
4. **Qt widgets have thread affinity** - only modify from creating thread

### If You Change ANY of the Following

#### Background Thread Operations
You **MUST ALSO** check/update:
- [ ] Use `daemon=True` for threads that shouldn't block shutdown
- [ ] Use signals to communicate results back to main thread
- [ ] Don't access `self.cap` (camera) from multiple threads
- [ ] Don't modify widget properties from background thread

### Common Failure Modes

| Symptom | Likely Cause |
|---------|--------------|
| Random crashes | UI accessed from background thread |
| "QObject::setParent" errors | Widget created on wrong thread |
| Hung shutdown | Non-daemon thread still running |
| Corrupted frame | Multiple threads accessing camera |

---

## 9. Configuration, Constants, and Globals

### Primary Responsibility
Manages persistent settings, presets, and runtime configuration.

### Primary Files
| File | Description |
|------|-------------|
| [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py) | `load_settings()`, `save_settings()` |
| [app/config/settings.json](app/config/settings.json) | Runtime settings |
| [app/turret_presets.py](app/turret_presets.py) | Tracking presets |
| [app/behavior_presets.py](app/behavior_presets.py) | User-saved behavior presets |
| [app/config/idle_modes_config.json](app/config/idle_modes_config.json) | Idle mode configuration |

### Settings Persistence

Settings are saved to multiple locations:
- `app/config/settings.json` - Primary runtime settings
- `app/settings.json` - Legacy/backup location  
- `app/preferred_defaults.json` - User defaults
- `settings.json` (root) - Root-level backup

### Critical Constants (Hardcoded)

| Constant | Location | Value | Impact |
|----------|----------|-------|--------|
| `HOME_PAN` | MAIN_FILE_SINGLE_CAM.py | 90 | Default home position |
| `HOME_TILT` | MAIN_FILE_SINGLE_CAM.py | 40 | Default home position |
| `HOME_SPEED` | MAIN_FILE_SINGLE_CAM.py | 5 | Home movement speed % |
| `_max_firing_duration` | MAIN_FILE_SINGLE_CAM.py | 3.0 | Fire timeout seconds |
| `_frac_send_threshold` | MAIN_FILE_SINGLE_CAM.py | 0.25 | Micro-step threshold degrees |
| `HUD_*` colors | MAIN_FILE_SINGLE_CAM.py | BGR tuples | HUD rendering colors |

### If You Change ANY of the Following

#### Settings Field Names
You **MUST ALSO** check/update:
- [ ] Both `load_settings()` and `save_settings()` 
- [ ] Widget name that populates/reads the setting
- [ ] Preset definitions in `turret_presets.py`
- [ ] Default value in `__init__`

#### Preset Values
You **MUST ALSO** check/update:
- [ ] Test each affected preset
- [ ] Document change in preset docstring
- [ ] Consider resolution-specific presets

### Hidden or Non-Obvious Dependencies

1. **Settings load order matters**: Widget values set after load can override
2. **Preset application partial**: Not all settings in all presets
3. **window_state/geometry base64**: Encoded Qt layout state - version-sensitive
4. **Multiple settings files**: Check all locations for stale copies

### Common Failure Modes

| Symptom | Likely Cause |
|---------|--------------|
| Settings don't persist | save_settings() exception, or wrong path |
| Wrong default value | __init__ default differs from settings default |
| Preset has no effect | Setting name changed but preset not updated |
| "Key error" on load | New setting added but not in old settings file |

### Idle Auto-Resume & Guard Defaults (FRAGILE / LEGACY)

The idle system relies on a persisted setting key (`auto_tracking`) and several runtime guard defaults.

| Item | Location | Default | Impact |
|------|----------|---------|--------|
| Idle-to-tracking auto-resume flag | [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L1618) | `True` | Enables exiting idle modes when a target is detected (if UI/settings allow)
| Settings persistence key | [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L9735) and [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L10441) | `auto_tracking` | If renamed/mismatched, idle detection will appear "ignored"
| Guard dwell time | [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L1742) | `5.0` seconds | Time at each random guard point
| Guard speed (fallback sweep) | [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L1744) | `0.6` | Used in fallback guard sweep path
| Guard pan/tilt random ranges | [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L1745-L1746) | `(20,160)`, `(30,90)` | Random positions must stay within servo limits and physical safe range

**Runtime usage**
- Auto-resume gate (idle modes): [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L16161-L16172)
- Guard random-point behavior + fallback sweep: [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L17229-L17256)
- Guard speed UI callback exists (keep in sync with behavior expectations): [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L3510-L3519)

#### If You Change ANY of the Following

##### `auto_tracking` / `auto_tracking_enabled`
You **MUST ALSO** check/update:
- [ ] `load_settings()` and `save_settings()` key name stays `auto_tracking`: [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L9735) and [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L10441)
- [ ] Any idle-mode logic that reads it via `getattr(..., False)` still has the correct default: [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py#L16172)

##### Guard defaults (`_guard_*`)
You **MUST ALSO** check/update:
- [ ] Ranges remain within `PAN_MIN/PAN_MAX` and `TILT_MIN/TILT_MAX` (otherwise clamping/physical stops may occur)
- [ ] Guard dwell time works with `main_timer` cadence (too small = jittery, too large = looks frozen)

---

## 10. Hardware Control (Servo, Trigger, Relays)

### Primary Responsibility
Manages physical hardware outputs via Arduino/MCU.

### Primary Files
| File | Description |
|------|-------------|
| [app/MAIN_FILE_SINGLE_CAM.py](app/MAIN_FILE_SINGLE_CAM.py) | Hardware state, command encoding |
| [app/turret_enhancements.py](app/turret_enhancements.py) | Sound feedback for hardware events |
| [app/servo_calibration_tool.py](app/servo_calibration_tool.py) | Servo tuning utility |

### Hardware State Variables

| Variable | Type | Description |
|----------|------|-------------|
| `trigger_fired` | bool | Fire relay requested |
| `relay1_state` | int | LED relay state |
| `relay2_state` | int | Laser relay state |
| `safety_state` | int | Safety interlock (0=armed) |
| `trigger_mode_bb` | bool | Burst mode flag |
| `rapid_fire_enabled` | bool | Rapid fire active |
| `rapid_fire_rate_hz` | int | Pulses per second |
| `rapid_fire_duty` | float | On-time fraction |

### If You Change ANY of the Following

#### Safety Logic
You **MUST ALSO** check/update:
- [ ] ARM button visual state
- [ ] Fire command encoding (S token)
- [ ] Auto-fire enable checks
- [ ] Sound feedback (armed/disarmed sounds)

#### Servo Limits
You **MUST ALSO** check/update:
- [ ] Arduino firmware limits (must allow range)
- [ ] UI spinbox ranges
- [ ] Home position within limits
- [ ] Preset angle values

### Common Failure Modes

| Symptom | Likely Cause |
|---------|--------------|
| Won't fire when armed | safety_state check failed, or auto_fire disabled |
| Fires when should be safe | Safety token not sent, or Arduino ignoring |
| Servo hits physical stop | Limits wider than hardware allows |
| Rapid fire too fast/slow | rate_hz or duty calculation wrong |

---

## 11. Code-Level Change Enforcement

### Mandatory Warning Comments

When modifying sensitive files, add or verify the following comment block at the top of modified functions:

```python
# CHANGE WARNING:
# Modifications here affect [list affected subsystems].
# See CHANGE_IMPACT_REFERENCE.md → [Section Name]
# Last modified: [DATE] by [EDITOR]
```

### Files Requiring Mandatory Comments

| File | Sensitive Functions |
|------|---------------------|
| `MAIN_FILE_SINGLE_CAM.py` | `__init__`, `update_frame`, `send_serial_command`, `toggle_tracking`, `toggle_aiming` |
| `ui_builder.py` | `build_ui`, signal connections |
| `turret_presets.py` | Any preset modification |
| `yolo_detector.py` | `load_model`, `detect` |
| `turret_enhancements.py` | `play_sound`, `_create_top_bar` |

### AGENT-MANAGED BLOCKS

Some sections are managed by automated tools. Look for:
```python
# === AGENT-MANAGED BLOCK START ===
# [description]
# AgentChangeID: [ID]
# Date: [DATE]
# === AGENT-MANAGED BLOCK END ===
```

**Do not modify agent-managed blocks without updating the AgentChangeID.**

---

## 12. Sentry Mode Integration

### Overview

Sentry Mode is an intelligent guard turret system that learns target movement patterns, identifies optimal ambush points, and fires predictively based on trajectory analysis.

**Added:** December 2024  
**Status:** Active Integration

### Primary Files

| File | Description |
|------|-------------|
| [app/sentry_mode/sentry_tab_widget.py](app/sentry_mode/sentry_tab_widget.py) | PyQt5 tab widget for main app integration |
| [app/sentry_mode/sentry_controller.py](app/sentry_mode/sentry_controller.py) | Main orchestrator and state machine |
| [app/sentry_mode/sentry_config.py](app/sentry_mode/sentry_config.py) | Configuration dataclass |
| [app/sentry_mode/track_recorder.py](app/sentry_mode/track_recorder.py) | Records target trajectories |
| [app/sentry_mode/path_analyzer.py](app/sentry_mode/path_analyzer.py) | Identifies repeated patterns (Fréchet distance) |
| [app/sentry_mode/trajectory_predictor.py](app/sentry_mode/trajectory_predictor.py) | Kalman filter predictions |
| [app/sentry_mode/peripheral_sensor.py](app/sentry_mode/peripheral_sensor.py) | Kill zone detection |
| [app/sentry_mode/sentry_overlay.py](app/sentry_mode/sentry_overlay.py) | Visual overlay rendering |
| [app/sentry_mode/trackers/byte_tracker.py](app/sentry_mode/trackers/byte_tracker.py) | Multi-object tracking |

### Integration Points in MAIN_FILE_SINGLE_CAM.py

| Location | Code Block | Purpose |
|----------|------------|---------|
| Line ~145 | Import statement | Imports `SentryTabWidget` with fallback |
| Lines ~857-882 | Tab creation | Creates sentry tab, connects signals |
| Lines ~17937-17960 | Frame update | Passes frame/detections to sentry |
| Line ~18257 | send_serial_command | Blocks main commands when sentry active |
| Lines ~20070-20290 | Handler methods | Tab change, enable, turret move, fire |

### AGENT-MANAGED Blocks

The following blocks are managed by automated tools - do NOT modify without updating markers:

1. **Tab Creation** (Lines ~857-882): `AGENT-MANAGED BLOCK: SENTRY MODE TAB`
2. **Frame Update** (Lines ~17937-17960): `SENTRY MODE FRAME UPDATE`
3. **Serial Block** (Line ~18257): `SENTRY MODE BLOCK`
4. **Handlers** (Lines ~20070-20320): `AGENT-MANAGED BLOCK: SENTRY MODE INTEGRATION`
5. **Manual Control UI** (sentry_tab_widget.py): `AGENT-MANAGED BLOCK: Manual Turret Control`
6. **Manual Control Methods** (sentry_tab_widget.py): `AGENT-MANAGED BLOCK: Manual Control Methods`

### State Machine

```
IDLE → LEARNING → WATCHING → AIMING → FIRING → COOLDOWN → WATCHING
         ↓           ↑           ↓                         ↑
    (no patterns)   (paths confirmed)                  (repeat)
```

### Key Variables

| Variable | Type | Description |
|----------|------|-------------|
| `self.sentry_tab` | SentryTabWidget | The sentry tab widget (None if unavailable) |
| `self.sentry_mode_active` | bool | True when sentry tab is displayed |
| `self._sentry_previous_tracking_state` | bool | Saved tracking state for restoration |
| `self.manual_override` | bool | Allows manual control to bypass sentry block |

### Signal Flow

```
SentryTabWidget.turret_move_requested(pan, tilt) → _on_sentry_turret_move() → self.ser.write()
SentryTabWidget.fire_requested(burst_count) → _on_sentry_fire() → self.ser.write()
SentryTabWidget.sentry_enabled_changed(enabled) → _on_sentry_enabled_changed() → pause/resume tracking
SentryTabWidget.manual_move_requested(pan_delta, tilt_delta) → _on_sentry_manual_move() → move_manual()
main_tab_widget.currentChanged(index) → _on_tab_changed() → activate/deactivate sentry_mode_active
```

### Manual Control Features (Dec 2024)

| UI Element | Action | Signal/Method |
|------------|--------|---------------|
| ▲ Up button | Tilt up 5° | `manual_move_requested(0, 5)` |
| ▼ Down button | Tilt down 5° | `manual_move_requested(0, -5)` |
| ◀ Left button | Pan left 5° | `manual_move_requested(-5, 0)` |
| ▶ Right button | Pan right 5° | `manual_move_requested(5, 0)` |
| ● Center button | Home position | `turret_move_requested(90, 90)` |
| 💀 Set Ambush HERE | Save current position | `_set_ambush_at_current()` |
| 🎯 Aim at Ambush | Move to best ambush | `_aim_at_ambush()` |

**Manual Override Flow:**
1. User clicks direction button in Sentry tab
2. `manual_move_requested` signal emitted
3. Main app `_on_sentry_manual_move()` called
4. `move_manual()` sets `manual_override = True`
5. `send_serial_command()` checks `manual_override` and allows command through sentry block
6. Command sent to Arduino

### If You Change ANY of the Following

#### Sentry Tab
You **MUST ALSO** check/update:
- [ ] Signal connections in tab creation block
- [ ] `_on_tab_changed()` tab index comparison
- [ ] `_update_sentry_frame()` detection format conversion
- [ ] `send_serial_command()` sentry block guard
- [ ] `_on_sentry_manual_move()` handler

#### Detection Format
You **MUST ALSO** check/update:
- [ ] `boxes` format in update_frame() (main app uses x,y,w,h,score,class)
- [ ] `sentry_boxes` conversion in frame update block
- [ ] ByteTracker expects (x,y,w,h,score)
- [ ] SentryController.update() expects (track_id,x,y,w,h)

#### Serial Protocol
You **MUST ALSO** check/update:
- [ ] `_on_sentry_turret_move()` command format
- [ ] `_on_sentry_fire()` command format
- [ ] `_on_sentry_manual_move()` command format
- [ ] Arduino firmware compatibility

### Common Failure Modes

| Symptom | Likely Cause |
|---------|--------------|
| Sentry tab blank | `process_frame()` not receiving frames |
| Main tracking still runs | `sentry_mode_active` not blocking `send_serial_command()` |
| No overlays visible | Controller in IDLE state (enable checkbox not checked) |
| Turret doesn't move | Signal not connected or serial blocked |
| Sentry not detecting | Detection format mismatch (check box format) |
| Crash on manual track draw | Using wrong method `_analyze_pending_tracks()` - use `analyze_track()` |
| Manual control not working | `manual_override` flag not checked in sentry block |

### Required Verification Steps

1. **Tab Creation**: Start app, verify "🎯 Sentry" tab appears
2. **Video Display**: Click sentry tab, verify video feed visible
3. **Mode Switching**: Check main tracking pauses when sentry tab active
4. **Enable Toggle**: Check "Enable Sentry Mode" starts LEARNING state
5. **Overlay Rendering**: Verify state label and status updates
6. **Turret Control**: With sentry enabled, verify main servo commands blocked
7. **Guard Point**: Set guard point, verify turret moves (if sentry enabled)
8. **Manual Track**: Draw track path, verify no crash and track analyzed

### Sentry Mode Critical Constants & Couplings (INTENDED / FRAGILE)

This section documents the non-obvious constants and unit conventions that Sentry Mode logic assumes.

#### Configuration Source of Truth
- All tunables live in `SentryConfig`: [app/sentry_mode/sentry_config.py](app/sentry_mode/sentry_config.py#L16-L167)
- Several values have "paired" semantics across modules. If you change one, validate the coupled behavior.

#### Kalman / Prediction Timing (INTENDED)
- Kalman `dt` is clamped to a safe range: `dt = max(0.001, min(dt, 1.0))`: [app/sentry_mode/trajectory_predictor.py](app/sentry_mode/trajectory_predictor.py#L136)
- Fire scheduling uses `mechanical_lead_time` and `fire_window_before` to fire early: [app/sentry_mode/trajectory_predictor.py](app/sentry_mode/trajectory_predictor.py#L380-L387) and [app/sentry_mode/sentry_config.py](app/sentry_mode/sentry_config.py#L86-L99)
- Fire gating uses `fire_confidence_threshold` and "late fire" window `fire_window_after`: [app/sentry_mode/trajectory_predictor.py](app/sentry_mode/trajectory_predictor.py#L408-L418) and [app/sentry_mode/sentry_config.py](app/sentry_mode/sentry_config.py#L86-L99)

#### Track Lifecycle & Persistence (FRAGILE)
- Track completion uses a **500ms grace period** when a track is not seen: [app/sentry_mode/track_recorder.py](app/sentry_mode/track_recorder.py#L214)
- Velocity uses EMA smoothing factor `velocity_smoothing`: [app/sentry_mode/track_recorder.py](app/sentry_mode/track_recorder.py#L235) and [app/sentry_mode/sentry_config.py](app/sentry_mode/sentry_config.py#L55-L72)
- Completed tracks are only kept if `len(points) >= min_track_length`: [app/sentry_mode/track_recorder.py](app/sentry_mode/track_recorder.py#L287) and [app/sentry_mode/sentry_config.py](app/sentry_mode/sentry_config.py#L54)
- Expiry removes old completed tracks using `track_expiry_seconds`: [app/sentry_mode/track_recorder.py](app/sentry_mode/track_recorder.py#L295-L301) and [app/sentry_mode/sentry_config.py](app/sentry_mode/sentry_config.py#L60)
- Persistence path is relative to the sentry module folder via `Path(__file__).parent / tracks_save_path`: [app/sentry_mode/track_recorder.py](app/sentry_mode/track_recorder.py#L340-L362) and [app/sentry_mode/sentry_config.py](app/sentry_mode/sentry_config.py#L139-L149)

#### Path Similarity & Ambush Selection (INTENDED)
- Similarity check uses `similarity >= (1.0 - path_similarity_threshold)`: [app/sentry_mode/path_analyzer.py](app/sentry_mode/path_analyzer.py#L117-L133)
        - This means **smaller** `path_similarity_threshold` is **stricter** matching (it is not "minimum similarity").
- Confirmed-path pruning enforces `max_ambush_points` and `ambush_priority_method`: [app/sentry_mode/path_analyzer.py](app/sentry_mode/path_analyzer.py#L345-L365) and [app/sentry_mode/sentry_config.py](app/sentry_mode/sentry_config.py#L106-L114)
- Manual ambush points are ignored when `manual_ambush_enabled` is false and are capped to `max_ambush_points`: [app/sentry_mode/path_analyzer.py](app/sentry_mode/path_analyzer.py#L367-L381)

#### Normalized → Servo Mapping in SentryController (FRAGILE / LEGACY)
- `_aim_turret_at_ambush()` uses a simplified mapping and clamps to fixed ranges: [app/sentry_mode/sentry_controller.py](app/sentry_mode/sentry_controller.py#L442-L470)
        - `pan = 90 + (x - 0.5) * 180`, clamped to `5..185`
        - `tilt = 75 + (y - 0.5) * 110`, clamped to `20..130`
Markdown Preview EnhancedMarkdown Preview Enhanced
#### If You Change ANY of the Following

##### `SentryConfig` firing/prediction constants
You **MUST ALSO** check/update:
- [ ] The fire scheduling and gating logic remain consistent with units (seconds vs ms): [app/sentry_mode/trajectory_predictor.py](app/sentry_mode/trajectory_predictor.py#L380-L418)
- [ ] Burst timing values (ms) align with Arduino firmware expectations

##### Track persistence paths
You **MUST ALSO** check/update:
- [ ] Any relative-path assumption (module-relative vs repo-root) for `tracks_save_path`: [app/sentry_mode/track_recorder.py](app/sentry_mode/track_recorder.py#L340-L362)

##### Path similarity thresholds
You **MUST ALSO** check/update:
- [ ] Documentation/UI wording reflects the inverted threshold semantics: [app/sentry_mode/path_analyzer.py](app/sentry_mode/path_analyzer.py#L117-L133)
- [ ] Learning confirmation expectations (`min_passes_to_confirm`) remain realistic for your environment: [app/sentry_mode/sentry_config.py](app/sentry_mode/sentry_config.py#L40-L56)

---

## 13. Change Log (Required)

| Date | Editor | Description | Sections Updated |
|------|--------|-------------|------------------|
| 2025-12-19 | AutoTracker Team | Initial document creation | All |
| 2025-12-19 | Copilot Agent | Added Sentry Mode integration section | Section 12 |
| 2025-12-19 | Copilot Agent | Fixed manual track crash - wrong method call | Section 12 |
| 2025-12-19 | Copilot Agent | Added manual turret control for Sentry Mode | Section 12 |
| 2025-12-19 | Copilot Agent | Fixed false tilt-safety latch that could suppress tilt on "OK" status messages (host parsing + explicit init) | Sections 5, 6, 13 |
| 2025-12-20 | Copilot Agent | Documented Hybrid Mode 4/5 thresholds, idle auto-resume/guard defaults, and key Sentry constants/persistence couplings | Sections 3, 9, 12, Appendix A |
| 2026-01-09 | Copilot Agent | Updated documentation workflow to prevent .md file accumulation - mandate RECENT_UPDATES.json for all changes, .md files only for complex cases | Section 1 |

---

## Appendix A: Quick Reference Checklists

### Before Changing Resolution
- [ ] Edit all 3 lines together (frame_ratio_setting, frame_width, frame_height)
- [ ] Update deadzone (pixel-based)
- [ ] Update snap_threshold (pixel-based)
- [ ] Test coordinate mapping
- [ ] Test HUD rendering
- [ ] Test all detection modes

### Before Changing Detection Parameters
- [ ] Test at deployed resolution
- [ ] Test in actual lighting conditions
- [ ] Test with actual target
- [ ] Update presets if needed
- [ ] Document threshold rationale

### Before Changing Hybrid Mode 4/5 Thresholds
- [ ] Confirm UI/JSON values are in **percent** and runtime comparisons are in **fraction**
- [ ] Verify `/ 100.0` conversions still exist and match debug output
- [ ] Test Mode 4 gating under expected lighting + motion levels
- [ ] Test Mode 5 overlap filtering with real motion regions and detections

### Before Changing Idle Auto-Resume / Guard
- [ ] Keep `auto_tracking` key consistent across load/save
- [ ] Validate idle → tracking resume still triggers on detection
- [ ] Verify guard random ranges remain inside servo limits
- [ ] Verify guard dwell time and speed feel intentional (not jitter/freeze)

### Before Changing Serial Protocol
- [ ] Update Arduino firmware to match
- [ ] Update all test scripts
- [ ] Update redundant command filter
- [ ] Test connection and commands
- [ ] Document protocol change

### Before Changing UI Widgets
- [ ] Use _safe_connect() for signals
- [ ] Update load_settings() mapping
- [ ] Update save_settings() mapping
- [ ] Test persistence across restart
- [ ] Test keyboard shortcuts still work

### Before Changing Sentry Mode
- [ ] Review Section 12 of this document
- [ ] Check AGENT-MANAGED block markers
- [ ] Verify detection format conversion
- [ ] Test tab switching (main ↔ sentry)
- [ ] Test sentry enable/disable toggle
- [ ] Verify main tracking pauses correctly
- [ ] Test turret move signals work
- [ ] Verify overlays render correctly
- [ ] Check Arduino serial compatibility

---

*This document must be updated whenever system dependencies change.*

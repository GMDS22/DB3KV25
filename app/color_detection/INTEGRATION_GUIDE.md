# Color Detection Integration Guide

This document provides step-by-step instructions for integrating the color detection module into the main DADBOT application.

## Prerequisites

- Color detection module files in `app/color_detection/`
- All existing detection modes working (0-5)

## Integration Steps

### Step 1: Import the Color Detector

In `MAIN_FILE_SINGLE_CAM.py`, add the import near the top with other detector imports (around line 100-110):

```python
# Color detection import
try:
    from color_detection import ColorDetector, fuse_detections_and, fuse_detections_or
    COLOR_DETECTION_AVAILABLE = True
except ImportError as e:
    print(f"[COLOR] Import failed: {e}")
    ColorDetector = None
    COLOR_DETECTION_AVAILABLE = False
```

### Step 2: Initialize the Color Detector

In the `__init__` method of the main class (around line 1720, after yolo_detector):

```python
# Initialize color detector
self.color_detector = None
self.color_calibration_mode = False
self.show_color_mask = False

try:
    if COLOR_DETECTION_AVAILABLE and ColorDetector is not None:
        self.color_detector = ColorDetector(enhancer=self.enhancer)
        print("[COLOR] Color detector initialized")
except Exception as e:
    print(f"[COLOR] Failed to initialize: {e}")
    self.color_detector = None
```

### Step 3: Update Detection Mode Combo Box

In `ui_builder.py`, update the detection mode combo items (around line 633):

```python
app._safe_widget_call(
    "detection_mode_combo",
    "addItems",
    [
        "Frame Difference",           # 0
        "Background Subtraction",     # 1
        "YOLO Object Detection",      # 2
        "Hybrid: FD+BS",              # 3
        "Hybrid: FD+YOLO",            # 4
        "Hybrid: BS+YOLO",            # 5
        "Color Detection",            # 6  <-- NEW
        "Hybrid: Color+FD",           # 7  <-- NEW
        "Hybrid: Color+BS",           # 8  <-- NEW
        "Hybrid: Color+YOLO",         # 9  <-- NEW
    ],
)
```

### Step 4: Add Color Settings UI Panel

In `ui_builder.py`, import and call the color panel builder:

```python
# At top of file
from color_detection.ui_components import build_color_detection_panel, connect_color_signals

# In the appropriate build function (where other detection settings are):
build_color_detection_panel(app, detection_layout)
connect_color_signals(app)
```

### Step 5: Update on_detection_mode_change

In the `on_detection_mode_change` method, add visibility toggle for color settings:

```python
def on_detection_mode_change(self, index_or_text):
    # ... existing code ...
    
    mode_text = str(index_or_text).lower() if isinstance(index_or_text, str) else ""
    is_color_mode = "color" in mode_text or index_or_text in [6, 7, 8, 9]
    
    # Show/hide color settings panel
    try:
        from color_detection.ui_components import show_hide_color_panel
        show_hide_color_panel(self, is_color_mode)
    except Exception:
        pass
    
    # ... rest of existing code ...
```

### Step 6: Add Detection Logic for Modes 6-9

In the main detection pipeline (around line 15105), add color detection handling:

```python
elif detection_mode == 6:  # Color Detection
    try:
        if self.color_detector is not None:
            # Get color preset from UI
            color_name = self._safe_widget_method_return(
                "color_preset_combo", "currentText", "red"
            ) or "red"
            
            if color_name == "custom":
                # Use custom HSV sliders
                h_min = getattr(self.color_h_min, "value", lambda: 0)()
                h_max = getattr(self.color_h_max, "value", lambda: 10)()
                s_min = getattr(self.color_s_min, "value", lambda: 100)()
                s_max = getattr(self.color_s_max, "value", lambda: 255)()
                v_min = getattr(self.color_v_min, "value", lambda: 100)()
                v_max = getattr(self.color_v_max, "value", lambda: 255)()
                self.color_detector.set_custom_range(h_min, s_min, v_min, h_max, s_max, v_max)
                self.color_detector.set_active_colors("custom")
            else:
                self.color_detector.set_active_colors(color_name)
            
            # Update detection params from UI
            min_area = self._safe_int_widget_value("color_min_area_input", 300)
            max_area = self._safe_int_widget_value("color_max_area_input", 500000)
            blur = self._safe_int_widget_value("color_blur_input", 5)
            morph = self._safe_int_widget_value("color_morph_input", 2)
            self.color_detector.set_detection_params(
                min_area=min_area, max_area=max_area,
                blur_kernel=blur, morph_iterations=morph
            )
            
            # Run detection
            boxes = self.color_detector.detect(frame1)
            
            # Show mask if enabled
            if getattr(self, "show_color_mask", False) and self.color_detector.last_mask is not None:
                cv2.imshow("Color Mask", self.color_detector.last_mask)
            
    except Exception as e:
        boxes = []
        if hasattr(self, "enhancer"):
            self.enhancer.log_serial_output(f"Color Mode 6 error: {e}", fire=False)

elif detection_mode == 7:  # Hybrid: Color + FrameDiff
    try:
        # Get color detections
        color_boxes = []
        if self.color_detector is not None:
            color_name = self._safe_widget_method_return("color_preset_combo", "currentText", "red")
            self.color_detector.set_active_colors(color_name if color_name != "custom" else "custom")
            color_boxes = self.color_detector.detect(frame1)
        
        # Get frame diff detections (reuse existing logic)
        fd_boxes = []  # ... frame diff detection logic ...
        
        # Fuse detections
        fusion_strategy = self._safe_widget_method_return("color_fusion_strategy", "currentText", "AND")
        overlap = self._safe_int_widget_value("color_fusion_overlap", 30) / 100.0
        
        if fusion_strategy == "AND":
            boxes = fuse_detections_and(color_boxes, fd_boxes, overlap)
        else:
            boxes = fuse_detections_or(color_boxes, fd_boxes)
            
    except Exception as e:
        boxes = []

elif detection_mode == 8:  # Hybrid: Color + BackSub
    # Similar pattern to mode 7, but with background subtraction
    pass

elif detection_mode == 9:  # Hybrid: Color + YOLO
    # Similar pattern to mode 7, but with YOLO
    pass
```

### Step 7: Update Settings Save/Load

In `save_settings` method, add:

```python
# Color detection settings
"color_preset": val("color_preset_combo", "red", "text"),
"color_h_min": val("color_h_min", 0, "value"),
"color_h_max": val("color_h_max", 10, "value"),
"color_s_min": val("color_s_min", 100, "value"),
"color_s_max": val("color_s_max", 255, "value"),
"color_v_min": val("color_v_min", 100, "value"),
"color_v_max": val("color_v_max", 255, "value"),
"color_min_area": val("color_min_area_input", 300, "value"),
"color_max_area": val("color_max_area_input", 500000, "value"),
"color_blur": val("color_blur_input", 5, "value"),
"color_morph": val("color_morph_input", 2, "value"),
"color_fusion_strategy": val("color_fusion_strategy", "AND", "text"),
"color_fusion_overlap": val("color_fusion_overlap", 30, "value"),
```

In `load_settings` method, add corresponding restore logic.

### Step 8: Add Color Presets to turret_presets.py

Copy presets from `color_detection/color_presets.py` to the main `PRESETS` dict in `turret_presets.py`.

### Step 9: Handle ROI Calibration (Optional)

Add mouse callback for ROI color calibration:

```python
def on_video_mouse_callback(self, event, x, y, flags, param):
    if getattr(self, "color_calibration_mode", False):
        if event == cv2.EVENT_LBUTTONDOWN:
            self._calibration_start = (x, y)
        elif event == cv2.EVENT_LBUTTONUP and hasattr(self, "_calibration_start"):
            x1, y1 = self._calibration_start
            roi = (min(x1, x), min(y1, y), abs(x - x1), abs(y - y1))
            if self.color_detector and roi[2] > 5 and roi[3] > 5:
                self.color_detector.calibrate_from_roi(self.current_frame, roi)
                # Update UI sliders with calibrated values
                # ...
            self.color_calibration_mode = False
```

## Testing After Integration

1. Run the main application
2. Select "Color Detection" from detection mode dropdown
3. Choose a color preset (e.g., "red")
4. Hold a red object in front of camera
5. Verify bounding box appears
6. Test hybrid modes (7, 8, 9)
7. Test saving/loading settings

## Rollback

If issues occur, the color detection module is isolated and can be disabled by:

1. Removing the import in `MAIN_FILE_SINGLE_CAM.py`
2. Removing detection modes 6-9 from combo box
3. Hiding the color settings panel

The module files can remain in place without affecting other functionality.

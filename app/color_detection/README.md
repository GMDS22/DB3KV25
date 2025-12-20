# Color Detection Module for DADBOT v4

## Overview

This module provides HSV-based color detection and tracking capabilities for the DADBOT turret system. It can track objects by color, either using predefined color presets or custom HSV ranges.

## Features

- **12 Predefined Color Presets**: red, orange, yellow, green, cyan, blue, purple, pink, white, black, neon_green, laser_red
- **Custom HSV Ranges**: Define your own color ranges with sliders
- **Multi-Color Tracking**: Track multiple colors simultaneously
- **Hybrid Mode Support**: Combine with FrameDiff, BackSub, or YOLO for enhanced accuracy
- **ROI Calibration**: Sample colors directly from the video feed
- **No External Dependencies**: Uses only OpenCV (already required)

## Detection Mode Indices

| Index | Mode Name | Description |
|-------|-----------|-------------|
| 6 | Color Detection | Pure HSV color tracking |
| 7 | Hybrid: Color+FD | Color with frame difference motion gate |
| 8 | Hybrid: Color+BS | Color with background subtraction |
| 9 | Hybrid: Color+YOLO | Color with YOLO confirmation |

## Files

| File | Purpose |
|------|---------|
| `__init__.py` | Package initialization and exports |
| `color_detector.py` | Main ColorDetector class |
| `hybrid_fusion.py` | Fusion helpers for hybrid modes |
| `color_presets.py` | Turret presets for color tracking |
| `ui_components.py` | PyQt5 UI panel builders |
| `test_color_detection.py` | Standalone test script |
| `INTEGRATION_GUIDE.md` | Developer integration instructions |

## Quick Start

### Standalone Testing

```bash
# Activate virtual environment
cd D:\GM_REVIT_TOOLBOX\DB3000V4.1-main
.\.venv\Scripts\Activate.ps1

# Run standalone test
cd app\color_detection
python test_color_detection.py --color red

# Test with different colors
python test_color_detection.py --color neon_green
python test_color_detection.py --color laser_red

# Test with custom HSV range
python test_color_detection.py --custom --h-min 0 --h-max 10 --s-min 150 --s-max 255 --v-min 150 --v-max 255
```

### Basic Usage in Code

```python
from color_detection import ColorDetector

# Initialize
detector = ColorDetector()

# Set color to track
detector.set_active_colors("red")

# In your frame loop:
boxes = detector.detect(frame)
for (x, y, w, h) in boxes:
    # Do something with detection
    cx, cy = x + w//2, y + h//2
```

## Color Presets

### Standard Colors
- **red** - Bright red objects (wraps around hue spectrum)
- **orange** - Orange objects
- **yellow** - Yellow objects
- **green** - Green objects (general range)
- **cyan** - Cyan/Teal objects
- **blue** - Blue objects
- **purple** - Purple/Violet objects
- **pink** - Pink/Magenta objects

### Special Presets
- **neon_green** - High-visibility safety green, tennis balls
- **laser_red** - Optimized for laser pointer dots (very saturated red)
- **white** - Bright/white objects (low saturation)
- **black** - Dark objects (low value)

## Integration Status

**Current Status**: ⏳ Ready for Integration

The color detection module is fully implemented and tested. Integration with the main application requires:

1. Adding import in `MAIN_FILE_SINGLE_CAM.py`
2. Adding detection modes 6-9 to combo box
3. Adding UI panel from `ui_components.py`
4. Adding detection logic for modes 6-9
5. Adding presets from `color_presets.py`

See [INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md) for detailed steps.

## Performance

| Mode | Speed | Accuracy | Use Case |
|------|-------|----------|----------|
| Color (6) | ⚡⚡⚡ Fast | Medium | General color tracking |
| Color+FD (7) | ⚡⚡ Fast | Good | Moving colored objects |
| Color+BS (8) | ⚡ Medium | Good | Objects entering scene |
| Color+YOLO (9) | 🐢 Slower | Best | Maximum accuracy |

## Troubleshooting

### No Detections
- Check lighting conditions
- Lower the saturation/value minimums
- Verify camera is working

### Too Many False Positives
- Increase min_area parameter
- Narrow the HSV range
- Use a hybrid mode

### Color Not Matching
- Use the ROI calibration tool
- Adjust under actual operating conditions
- Check for colored lighting affecting perception

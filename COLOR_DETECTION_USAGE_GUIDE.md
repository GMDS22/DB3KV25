# Color Detection Usage Guide

## Overview
The DADBOT v4 application now includes HSV-based color detection as an alternative or complementary detection mode to YOLO and frame-difference based methods.

## Color Detection Modes

### Pure Color Detection
**Mode 6: Color Detection**
- Uses only HSV color-space detection
- Fastest for color-based targets
- Best for objects with distinct color signatures
- Does not require YOLO model loading

### Hybrid Color Detection Modes
Combine color detection with other detection methods for more robust tracking:

**Mode 7: Color + Frame Difference**
- Fuses color detection with motion detection
- Useful for colored objects that move
- Good for cluttered backgrounds with static colored elements

**Mode 8: Color + Background Subtraction**
- Combines color detection with background subtraction
- Excellent for stationary colored targets in changing lighting
- Requires background model building (~30 frames)

**Mode 9: Color + YOLO**
- Most robust: combines color detection with AI object detection
- Highest accuracy for colored objects
- Requires YOLO models to be available

## Color Presets

The color detection module includes pre-calibrated HSV ranges for common colors:

### Available Presets:
- **Red** - Bright red objects (wraps hue around 0°)
- **Orange** - Orange-colored objects
- **Yellow** - Yellow objects
- **Green** - Green objects and vegetation
- **Cyan** - Cyan/Teal colored objects
- **Blue** - Blue objects
- **Purple** - Purple/Violet objects
- **Pink** - Pink/Magenta objects
- **White** - Light/White objects
- **Black** - Dark/Black objects
- **Skin** - Flesh tones (human skin)
- **Custom** - User-defined color range

## Using Color Detection

### Basic Workflow

1. **Launch Application**
   - Run DADBOT v4 normally
   - Application loads with default detection mode

2. **Select Color Detection Mode**
   - Open detection mode dropdown (typically in Configuration panel)
   - Choose:
     - Mode 6 for simple color detection
     - Mode 7-9 for hybrid approaches
   
3. **Configure Color Settings**
   - Color detection panel appears automatically when a color mode is selected
   - Select a color preset OR define custom range

4. **Adjust HSV Parameters (if needed)**
   - **Hue** (0-179 in OpenCV): Main color selection
     - Red: 0-10 or 160-179
     - Orange: 10-25
     - Yellow: 25-35
     - Green: 35-85
     - Cyan: 85-100
     - Blue: 100-130
     - Purple: 130-160
   
   - **Saturation** (0-255): Color purity
     - Low (0-50): Washed out, grayish colors
     - Medium (50-150): Normal colors
     - High (150-255): Very pure, vivid colors
   
   - **Value** (0-255): Brightness
     - Low (0-50): Very dark
     - Medium (50-150): Normal
     - High (150-255): Very bright

5. **Enable Aiming/Tracking**
   - Toggle "Aiming" button to enable turret control
   - Toggle "Tracking" button to follow detected targets

### Hybrid Mode Tips

#### For Mode 7 (Color + Frame Diff):
- Use when tracking colored objects with motion
- Motion detection helps eliminate static colored distractions
- Good for fast-moving targets with distinct colors

#### For Mode 8 (Color + BackSub):
- Let background model build for 30+ frames first
- Use for targets in changing light conditions
- Better for outdoor use where sky color varies
- Excellent for indoor environments with stable lighting

#### For Mode 9 (Color + YOLO):
- Highest accuracy and robustness
- Most CPU intensive
- Best for critical applications
- Requires YOLO model files present

## Custom Color Calibration

### Method 1: Manual HSV Range Adjustment
1. Set target object in camera view
2. Open color detection settings
3. Select "Custom" preset
4. Adjust Hue, Saturation, Value sliders until target is highlighted
5. Refer to HSV color wheel for hue selection

### Method 2: Color Picker Tool (if available)
1. Click on target object in camera view
2. Tool samples pixel and suggests HSV range
3. Fine-tune sensitivity as needed

### Method 3: Test and Iterate
1. Enable display of detected objects (debug view if available)
2. Observe mask showing detected areas
3. Adjust HSV until only desired target is detected
4. Minimize false positives from background

## Detection Parameters

### Contour Settings
- **Min Contour Area**: Minimum pixel area to consider valid detection
  - Lower = detects smaller objects but more noise
  - Default: 50-500 depending on resolution

- **Max Contour Area**: Maximum pixel area to consider valid detection
  - Prevents large background areas from being detected

- **Morphological Operations**: Cleanup filters
  - Helps remove noise and fill small gaps
  - Improves detection stability

## Performance Considerations

### CPU Usage
- **Color Detection Alone**: ~5-10% CPU (very fast)
- **Color + BackSub**: ~15-20% CPU
- **Color + YOLO**: ~40-60% CPU

### Speed Ranking (fastest to slowest)
1. Color Detection (Mode 6) - Fastest
2. Frame Difference (Mode 0) - Fast
3. Color + Frame Diff (Mode 7) - Medium
4. Color + BackSub (Mode 8) - Medium-High
5. Color + YOLO (Mode 9) - Slowest
6. YOLO Alone (Mode 2) - Slowest

## Troubleshooting

### Issue: No detections in color mode
**Solutions:**
- Verify target color is within selected HSV range
- Increase saturation range if color is washed out
- Check lighting conditions (poor lighting affects color)
- Enable debug view to see color mask
- Try preset color closer to actual target

### Issue: False positive detections
**Solutions:**
- Narrow HSV range (reduce Saturation or Value range)
- Reduce maximum contour area to exclude large background regions
- Use hybrid mode to add motion/background filtering
- Adjust minimum contour area to filter noise

### Issue: Detection is jerky or unstable
**Solutions:**
- Increase minimum contour area to filter noise
- Enable morphological cleanup operations
- Switch to hybrid mode for stability
- Ensure sufficient lighting for color recognition

### Issue: FPS drops when using color detection
**Solutions:**
- Switch from Mode 9 (Color + YOLO) to Mode 6 (Color only)
- Use Mode 7 (Color + Frame Diff) as faster hybrid alternative
- Reduce camera resolution if possible
- Close unnecessary UI windows

## Serial Output / Debugging

When color detection is active, the serial console displays:
- `[COLOR] Detecting: <color_name>`
- `[HYBRID] Fusing Color + <other_method>`
- Detection statistics (area, center, contours found)
- Mode transitions and parameter changes

## Settings Persistence

Color detection configuration is saved to:
- `settings.json` - Detection mode selection
- Application state - HSV ranges and presets

Settings are automatically restored on next application launch.

## Advanced Usage

### Blob Detection Enhancement
Color detection can be combined with blob tracking for enhanced accuracy:
- Minimize noise using contour filters
- Use morphological operations (erode/dilate)
- Apply convex hull matching for shape consistency

### Multi-Color Tracking
In hybrid modes, you can theoretically track multiple color ranges by running multiple color detectors:
- Configure separate color presets
- Use OR fusion to combine detection results
- Prioritize by contour size or distance

### Integration with Idle Modes
Color detection works seamlessly with idle modes:
- When idle, target last detected color location
- Resume tracking when motion detected in that color
- Useful for returning to specific colored landmarks

---

**Last Updated**: December 2024
**Version**: DADBOT v4.1+
**Status**: Ready for Production Use

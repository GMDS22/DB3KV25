#!/usr/bin/env python3
"""
Color Detection Standalone Test
================================

This script tests the color detector independently without the main application.
Run this to verify color detection is working before integration.

Usage:
    python test_color_detection.py [--camera 0] [--color red] [--no-gui]

Arguments:
    --camera N      Camera index (default: 0)
    --color NAME    Color preset to track (default: red)
    --no-gui        Run without GUI (print detection counts only)
    --custom        Use custom HSV range
    --h-min N       Custom hue min (0-179)
    --h-max N       Custom hue max (0-179)
    --s-min N       Custom saturation min (0-255)
    --s-max N       Custom saturation max (0-255)
    --v-min N       Custom value min (0-255)
    --v-max N       Custom value max (0-255)

Controls (GUI mode):
    q - Quit
    r - Switch to red
    g - Switch to green
    b - Switch to blue
    y - Switch to yellow
    n - Switch to neon_green
    l - Switch to laser_red
    c - Cycle through all presets
    m - Toggle mask display
    + - Increase min area
    - - Decrease min area
"""

import sys
import os
import argparse
import time

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import cv2
import numpy as np

from color_detector import ColorDetector


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Test color detection")
    parser.add_argument("--camera", type=int, default=0, help="Camera index")
    parser.add_argument("--color", type=str, default="red", help="Color preset")
    parser.add_argument("--no-gui", action="store_true", help="Run without GUI")
    parser.add_argument("--custom", action="store_true", help="Use custom HSV range")
    parser.add_argument("--h-min", type=int, default=0, help="Custom hue min")
    parser.add_argument("--h-max", type=int, default=10, help="Custom hue max")
    parser.add_argument("--s-min", type=int, default=100, help="Custom saturation min")
    parser.add_argument("--s-max", type=int, default=255, help="Custom saturation max")
    parser.add_argument("--v-min", type=int, default=100, help="Custom value min")
    parser.add_argument("--v-max", type=int, default=255, help="Custom value max")
    return parser.parse_args()


def main():
    """Main test function."""
    args = parse_args()
    
    print("=" * 60)
    print("Color Detection Test")
    print("=" * 60)
    
    # Initialize detector
    detector = ColorDetector()
    
    # Show available presets
    print("\nAvailable color presets:")
    for color in detector.get_color_presets():
        info = detector.get_preset_info(color)
        print(f"  - {color}: {info['description']}")
    
    # Configure detector
    if args.custom:
        print(f"\nUsing custom HSV range:")
        print(f"  H: {args.h_min} - {args.h_max}")
        print(f"  S: {args.s_min} - {args.s_max}")
        print(f"  V: {args.v_min} - {args.v_max}")
        detector.set_custom_range(
            args.h_min, args.s_min, args.v_min,
            args.h_max, args.s_max, args.v_max
        )
        detector.set_active_colors("custom")
    else:
        print(f"\nUsing color preset: {args.color}")
        detector.set_active_colors(args.color)
    
    # Open camera
    print(f"\nOpening camera {args.camera}...")
    cap = cv2.VideoCapture(args.camera)
    
    if not cap.isOpened():
        print(f"ERROR: Could not open camera {args.camera}")
        return 1
    
    # Set camera resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f"Camera resolution: {width}x{height}")
    
    if args.no_gui:
        print("\nRunning in no-GUI mode. Press Ctrl+C to stop.")
        run_no_gui(detector, cap)
    else:
        print("\nControls:")
        print("  q - Quit")
        print("  r/g/b/y - Switch to red/green/blue/yellow")
        print("  n - Switch to neon_green")
        print("  l - Switch to laser_red")
        print("  c - Cycle through all presets")
        print("  m - Toggle mask display")
        print("  +/- - Increase/decrease min area")
        run_gui(detector, cap)
    
    cap.release()
    cv2.destroyAllWindows()
    print("\nTest complete.")
    return 0


def run_no_gui(detector, cap):
    """Run detection without GUI, just print stats."""
    frame_count = 0
    start_time = time.time()
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to read frame")
                break
            
            boxes = detector.detect(frame)
            frame_count += 1
            
            # Print stats every 30 frames
            if frame_count % 30 == 0:
                elapsed = time.time() - start_time
                fps = frame_count / elapsed
                print(f"Frame {frame_count}: {len(boxes)} detections, {fps:.1f} FPS")
                
    except KeyboardInterrupt:
        print("\nStopped by user")


def run_gui(detector, cap):
    """Run detection with GUI display."""
    show_mask = False
    preset_index = 0
    presets = detector.get_color_presets()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame")
            break
        
        # Run detection
        boxes, mask = detector.detect(frame, return_mask=True)
        
        # Draw detections
        display = detector.draw_detections(frame, boxes)
        
        # Add info overlay
        color_name = detector.active_colors[0] if detector.active_colors else "none"
        cv2.putText(display, f"Color: {color_name}", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(display, f"Detections: {len(boxes)}", (10, 60),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(display, f"Min Area: {detector.min_contour_area:.0f}", (10, 90),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Show main window
        cv2.imshow("Color Detection Test", display)
        
        # Show mask window if enabled
        if show_mask and mask is not None:
            # Colorize mask for better visibility
            mask_color = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
            mask_color[mask > 0] = detector.get_display_color()
            cv2.imshow("Color Mask", mask_color)
        else:
            cv2.destroyWindow("Color Mask")
        
        # Handle key presses
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q'):
            break
        elif key == ord('r'):
            detector.set_active_colors("red")
            print("Switched to: red")
        elif key == ord('g'):
            detector.set_active_colors("green")
            print("Switched to: green")
        elif key == ord('b'):
            detector.set_active_colors("blue")
            print("Switched to: blue")
        elif key == ord('y'):
            detector.set_active_colors("yellow")
            print("Switched to: yellow")
        elif key == ord('n'):
            detector.set_active_colors("neon_green")
            print("Switched to: neon_green")
        elif key == ord('l'):
            detector.set_active_colors("laser_red")
            print("Switched to: laser_red")
        elif key == ord('c'):
            # Cycle through presets
            preset_index = (preset_index + 1) % len(presets)
            detector.set_active_colors(presets[preset_index])
            print(f"Switched to: {presets[preset_index]}")
        elif key == ord('m'):
            show_mask = not show_mask
            print(f"Mask display: {'ON' if show_mask else 'OFF'}")
        elif key == ord('+') or key == ord('='):
            detector.min_contour_area = min(100000, detector.min_contour_area + 100)
            print(f"Min area: {detector.min_contour_area}")
        elif key == ord('-'):
            detector.min_contour_area = max(0, detector.min_contour_area - 100)
            print(f"Min area: {detector.min_contour_area}")


if __name__ == "__main__":
    sys.exit(main())

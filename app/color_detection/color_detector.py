"""
Color Detection Module for DADBOT v4
=====================================

Provides HSV-based color detection and tracking capabilities.
This module is designed to integrate with the existing detection modes
and can be used standalone or in hybrid configurations.

Detection Mode Index: 6 (Color Detection)
Hybrid Mode Indices: 7 (Color + FrameDiff), 8 (Color + BackSub), 9 (Color + YOLO)

Author: DADBOT Development Team
Date: December 2024
"""

import cv2
import numpy as np
import time
from typing import List, Tuple, Optional, Dict, Any


class ColorDetector:
    """
    A class to handle HSV color-based object detection.
    
    This detector finds objects matching specified color ranges in the HSV
    color space. Supports multiple color presets (red, green, blue, yellow, etc.)
    and custom color ranges defined by the user.
    
    Optionally accepts an `enhancer` object (TurretEnhancements) for playing
    detection sounds. Sound playback is debounced to avoid audio spam.
    """
    
    # =====================================================================
    # PREDEFINED COLOR PRESETS (HSV ranges)
    # HSV: Hue (0-179), Saturation (0-255), Value (0-255)
    # =====================================================================
    COLOR_PRESETS: Dict[str, Dict[str, Any]] = {
        "red": {
            # Red wraps around the hue spectrum, so we need two ranges
            "ranges": [
                {"lower": (0, 100, 100), "upper": (10, 255, 255)},
                {"lower": (160, 100, 100), "upper": (179, 255, 255)}
            ],
            "display_color": (0, 0, 255),  # BGR for drawing
            "description": "Bright red objects"
        },
        "orange": {
            "ranges": [{"lower": (10, 100, 100), "upper": (25, 255, 255)}],
            "display_color": (0, 165, 255),
            "description": "Orange objects"
        },
        "yellow": {
            "ranges": [{"lower": (25, 100, 100), "upper": (35, 255, 255)}],
            "display_color": (0, 255, 255),
            "description": "Yellow objects"
        },
        "green": {
            "ranges": [{"lower": (35, 100, 100), "upper": (85, 255, 255)}],
            "display_color": (0, 255, 0),
            "description": "Green objects"
        },
        "cyan": {
            "ranges": [{"lower": (85, 100, 100), "upper": (100, 255, 255)}],
            "display_color": (255, 255, 0),
            "description": "Cyan/Teal objects"
        },
        "blue": {
            "ranges": [{"lower": (100, 100, 100), "upper": (130, 255, 255)}],
            "display_color": (255, 0, 0),
            "description": "Blue objects"
        },
        "purple": {
            "ranges": [{"lower": (130, 100, 100), "upper": (160, 255, 255)}],
            "display_color": (255, 0, 128),
            "description": "Purple/Violet objects"
        },
        "pink": {
            "ranges": [{"lower": (140, 50, 100), "upper": (170, 255, 255)}],
            "display_color": (203, 192, 255),
            "description": "Pink/Magenta objects"
        },
        "white": {
            "ranges": [{"lower": (0, 0, 200), "upper": (179, 30, 255)}],
            "display_color": (255, 255, 255),
            "description": "White/Bright objects (low saturation)"
        },
        "black": {
            "ranges": [{"lower": (0, 0, 0), "upper": (179, 255, 50)}],
            "display_color": (50, 50, 50),
            "description": "Black/Dark objects (low value)"
        },
        "neon_green": {
            # High-vis safety green / tennis ball
            "ranges": [{"lower": (35, 150, 150), "upper": (75, 255, 255)}],
            "display_color": (0, 255, 127),
            "description": "Bright neon/safety green"
        },
        "laser_red": {
            # Laser pointer dot (very bright, saturated red)
            "ranges": [
                {"lower": (0, 200, 200), "upper": (10, 255, 255)},
                {"lower": (170, 200, 200), "upper": (179, 255, 255)}
            ],
            "display_color": (0, 0, 255),
            "description": "Laser pointer dots"
        },
    }
    
    def __init__(self, enhancer=None):
        """
        Initialize the color detector.
        
        Args:
            enhancer: Optional TurretEnhancements instance for sound playback.
        """
        self.enhancer = enhancer
        
        # Currently active color(s) to detect
        self.active_colors: List[str] = ["red"]
        
        # Custom color range (used when preset is "custom")
        self.custom_range: Dict[str, Tuple[int, int, int]] = {
            "lower": (0, 100, 100),
            "upper": (10, 255, 255)
        }
        
        # Detection parameters
        self.min_contour_area: float = 300.0
        self.max_contour_area: float = 500000.0
        self.blur_kernel: int = 5
        self.morph_iterations: int = 2
        
        # Tracking enhancement: centroid smoothing
        self.smoothing_enabled: bool = True
        self.smoothing_factor: float = 0.3  # Lower = more responsive
        self._last_centroids: Dict[str, Tuple[float, float]] = {}
        
        # Detection sound debounce
        self._last_detect_sound_time: float = 0.0
        self._detect_sound_debounce: float = 0.6
        
        # Loaded state (for consistency with YoloDetector interface)
        self.model_loaded: bool = True  # Always "loaded" - no model to load
        
        # Debug/diagnostic info
        self.last_mask: Optional[np.ndarray] = None
        self.last_detection_count: int = 0
    
    def set_active_colors(self, colors_str: str) -> None:
        """
        Set the colors to detect.
        
        Args:
            colors_str: Comma-separated color names (e.g., "red, green, blue")
                       or a single color name. Use "custom" to use custom_range.
        """
        if colors_str is None:
            self.active_colors = []
            return
        
        if isinstance(colors_str, (list, tuple, set)):
            self.active_colors = [str(c).strip().lower() for c in colors_str if str(c).strip()]
            return
        
        s = str(colors_str).strip()
        if not s:
            self.active_colors = []
        else:
            self.active_colors = [c.strip().lower() for c in s.split(",") if c.strip()]
    
    def set_custom_range(self, h_min: int, s_min: int, v_min: int,
                         h_max: int, s_max: int, v_max: int) -> None:
        """
        Set a custom HSV color range.
        
        Args:
            h_min, s_min, v_min: Lower bounds for Hue, Saturation, Value
            h_max, s_max, v_max: Upper bounds for Hue, Saturation, Value
        """
        self.custom_range = {
            "lower": (
                max(0, min(179, h_min)),
                max(0, min(255, s_min)),
                max(0, min(255, v_min))
            ),
            "upper": (
                max(0, min(179, h_max)),
                max(0, min(255, s_max)),
                max(0, min(255, v_max))
            )
        }
    
    def set_detection_params(self, min_area: float = None, max_area: float = None,
                             blur_kernel: int = None, morph_iterations: int = None) -> None:
        """
        Set detection filtering parameters.
        
        Args:
            min_area: Minimum contour area in pixels
            max_area: Maximum contour area in pixels
            blur_kernel: Gaussian blur kernel size (must be odd)
            morph_iterations: Morphological operation iterations
        """
        if min_area is not None:
            self.min_contour_area = max(0.0, float(min_area))
        if max_area is not None:
            self.max_contour_area = max(0.0, float(max_area))
        if blur_kernel is not None:
            k = int(blur_kernel)
            self.blur_kernel = k if k % 2 == 1 else max(1, k - 1)
        if morph_iterations is not None:
            self.morph_iterations = max(0, int(morph_iterations))
    
    def get_color_presets(self) -> List[str]:
        """Return list of available color preset names."""
        return list(self.COLOR_PRESETS.keys())
    
    def get_preset_info(self, color_name: str) -> Optional[Dict[str, Any]]:
        """Get information about a color preset."""
        return self.COLOR_PRESETS.get(color_name.lower())
    
    def _create_color_mask(self, hsv_frame: np.ndarray) -> np.ndarray:
        """
        Create a binary mask for all active colors.
        
        Args:
            hsv_frame: Frame in HSV color space
            
        Returns:
            Binary mask where detected colors are white (255)
        """
        combined_mask = np.zeros(hsv_frame.shape[:2], dtype=np.uint8)
        
        for color_name in self.active_colors:
            if color_name == "custom":
                # Use custom range
                lower = np.array(self.custom_range["lower"], dtype=np.uint8)
                upper = np.array(self.custom_range["upper"], dtype=np.uint8)
                mask = cv2.inRange(hsv_frame, lower, upper)
                combined_mask = cv2.bitwise_or(combined_mask, mask)
            elif color_name in self.COLOR_PRESETS:
                # Use preset range(s)
                preset = self.COLOR_PRESETS[color_name]
                for range_def in preset["ranges"]:
                    lower = np.array(range_def["lower"], dtype=np.uint8)
                    upper = np.array(range_def["upper"], dtype=np.uint8)
                    mask = cv2.inRange(hsv_frame, lower, upper)
                    combined_mask = cv2.bitwise_or(combined_mask, mask)
        
        return combined_mask
    
    def detect(self, frame: np.ndarray, return_mask: bool = False) -> List[Tuple[int, int, int, int]]:
        """
        Detect objects matching the active color(s).
        
        Args:
            frame: BGR image frame from camera
            return_mask: If True, also returns the detection mask
            
        Returns:
            List of bounding boxes as (x, y, w, h) tuples.
            If return_mask is True, returns (boxes, mask) tuple.
        """
        if frame is None or len(frame.shape) < 3:
            return ([], None) if return_mask else []
        
        if not self.active_colors:
            return ([], None) if return_mask else []
        
        try:
            # Apply Gaussian blur to reduce noise
            blurred = cv2.GaussianBlur(frame, (self.blur_kernel, self.blur_kernel), 0)
            
            # Convert to HSV color space
            hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
            
            # Create combined mask for all active colors
            mask = self._create_color_mask(hsv)
            
            # Morphological operations to clean up mask
            kernel = np.ones((5, 5), np.uint8)
            if self.morph_iterations > 0:
                # Opening to remove small noise
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, 
                                        iterations=self.morph_iterations)
                # Closing to fill small holes
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel,
                                        iterations=self.morph_iterations)
            
            # Store mask for debugging
            self.last_mask = mask.copy()
            
            # Find contours
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # Filter contours by area and create bounding boxes
            boxes = []
            for contour in contours:
                area = cv2.contourArea(contour)
                if self.min_contour_area <= area <= self.max_contour_area:
                    x, y, w, h = cv2.boundingRect(contour)
                    boxes.append((x, y, w, h))
            
            # Update detection count
            self.last_detection_count = len(boxes)
            
            # Play detection sound if detections found
            self._play_detect_sound_if_needed(len(boxes) > 0)
            
            if return_mask:
                return boxes, mask
            return boxes
            
        except Exception as e:
            print(f"[COLOR] Detection error: {e}")
            if return_mask:
                return [], None
            return []
    
    def detect_with_centroids(self, frame: np.ndarray) -> List[Dict[str, Any]]:
        """
        Detect objects and return detailed detection info including centroids.
        
        Args:
            frame: BGR image frame from camera
            
        Returns:
            List of detection dictionaries with keys:
            - 'box': (x, y, w, h) bounding box
            - 'centroid': (cx, cy) center point
            - 'area': contour area
            - 'color': detected color name (if single color) or "multi"
        """
        if frame is None or len(frame.shape) < 3:
            return []
        
        if not self.active_colors:
            return []
        
        try:
            blurred = cv2.GaussianBlur(frame, (self.blur_kernel, self.blur_kernel), 0)
            hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
            mask = self._create_color_mask(hsv)
            
            kernel = np.ones((5, 5), np.uint8)
            if self.morph_iterations > 0:
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel,
                                        iterations=self.morph_iterations)
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel,
                                        iterations=self.morph_iterations)
            
            self.last_mask = mask.copy()
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            detections = []
            color_name = self.active_colors[0] if len(self.active_colors) == 1 else "multi"
            
            for contour in contours:
                area = cv2.contourArea(contour)
                if self.min_contour_area <= area <= self.max_contour_area:
                    x, y, w, h = cv2.boundingRect(contour)
                    
                    # Calculate centroid
                    M = cv2.moments(contour)
                    if M["m00"] > 0:
                        cx = int(M["m10"] / M["m00"])
                        cy = int(M["m01"] / M["m00"])
                    else:
                        cx = x + w // 2
                        cy = y + h // 2
                    
                    detections.append({
                        'box': (x, y, w, h),
                        'centroid': (cx, cy),
                        'area': area,
                        'color': color_name
                    })
            
            self.last_detection_count = len(detections)
            self._play_detect_sound_if_needed(len(detections) > 0)
            
            return detections
            
        except Exception as e:
            print(f"[COLOR] Detection with centroids error: {e}")
            return []
    
    def _play_detect_sound_if_needed(self, detected: bool) -> None:
        """Play detection sound with debouncing."""
        if not detected:
            return
        
        now = time.time()
        if self.enhancer is not None and hasattr(self.enhancer, "play_detect"):
            if now - self._last_detect_sound_time >= self._detect_sound_debounce:
                try:
                    self.enhancer.play_detect()
                except Exception:
                    pass
                self._last_detect_sound_time = now
    
    def draw_detections(self, frame: np.ndarray, boxes: List[Tuple[int, int, int, int]],
                       color: Tuple[int, int, int] = None, thickness: int = 2) -> np.ndarray:
        """
        Draw bounding boxes on the frame.
        
        Args:
            frame: BGR image frame
            boxes: List of (x, y, w, h) bounding boxes
            color: BGR color for drawing (auto-selects based on active color if None)
            thickness: Line thickness
            
        Returns:
            Frame with drawn bounding boxes
        """
        result = frame.copy()
        
        # Determine draw color
        if color is None:
            if self.active_colors and self.active_colors[0] in self.COLOR_PRESETS:
                color = self.COLOR_PRESETS[self.active_colors[0]]["display_color"]
            else:
                color = (0, 255, 0)  # Default green
        
        for (x, y, w, h) in boxes:
            cv2.rectangle(result, (x, y), (x + w, y + h), color, thickness)
            # Draw centroid
            cx, cy = x + w // 2, y + h // 2
            cv2.circle(result, (cx, cy), 4, color, -1)
        
        return result
    
    def calibrate_from_roi(self, frame: np.ndarray, roi: Tuple[int, int, int, int],
                          tolerance: int = 20) -> Dict[str, Tuple[int, int, int]]:
        """
        Calibrate custom color range from a region of interest.
        
        Args:
            frame: BGR image frame
            roi: Region of interest as (x, y, w, h)
            tolerance: HSV tolerance to add around sampled values
            
        Returns:
            Dictionary with 'lower' and 'upper' HSV bounds
        """
        x, y, w, h = roi
        roi_region = frame[y:y+h, x:x+w]
        
        if roi_region.size == 0:
            return self.custom_range
        
        hsv_roi = cv2.cvtColor(roi_region, cv2.COLOR_BGR2HSV)
        
        # Calculate mean and std of HSV values in ROI
        h_mean = np.mean(hsv_roi[:, :, 0])
        s_mean = np.mean(hsv_roi[:, :, 1])
        v_mean = np.mean(hsv_roi[:, :, 2])
        
        # Create range with tolerance
        self.custom_range = {
            "lower": (
                max(0, int(h_mean - tolerance)),
                max(0, int(s_mean - tolerance * 2)),
                max(0, int(v_mean - tolerance * 2))
            ),
            "upper": (
                min(179, int(h_mean + tolerance)),
                min(255, int(s_mean + tolerance * 2)),
                min(255, int(v_mean + tolerance * 2))
            )
        }
        
        return self.custom_range
    
    def get_display_color(self) -> Tuple[int, int, int]:
        """Get the BGR display color for the current active color."""
        if self.active_colors and self.active_colors[0] in self.COLOR_PRESETS:
            return self.COLOR_PRESETS[self.active_colors[0]]["display_color"]
        return (0, 255, 0)  # Default green

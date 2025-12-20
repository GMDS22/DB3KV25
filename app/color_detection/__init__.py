"""
Color Detection Module for DADBOT v4
=====================================

HSV-based color detection and tracking capabilities.
Designed to integrate with existing detection modes and hybrid configurations.

Detection Mode Index: 6 (Color Detection)
Hybrid Mode Indices: 7 (Color + FrameDiff), 8 (Color + BackSub), 9 (Color + YOLO)

Usage:
    from color_detection import ColorDetector
    detector = ColorDetector()
    detector.set_active_colors("red")
    boxes = detector.detect(frame)
"""

from .color_detector import ColorDetector
from .hybrid_fusion import fuse_detections_and, fuse_detections_or

__all__ = [
    "ColorDetector",
    "fuse_detections_and",
    "fuse_detections_or",
]

__version__ = "1.0.0"

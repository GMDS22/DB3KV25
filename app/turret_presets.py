# turret_presets.py
# Preset profiles for turret tracking & YOLO detection behavior
#
# === TRACKING SETTINGS DOCUMENTATION ===
#
# GENERAL SETTINGS (applicable to all detection modes):
#   tracking_speed (1-100): Multiplier on servo movement speed. Higher = faster response.
#   movement_sensitivity (1-100): Base gain multiplier for error-to-movement conversion.
#   smoothing_factor (0.0-1.0): IIR filter blend. Lower = snappier, Higher = smoother.
#   deadzone (0-200 px): No-movement zone around frame center.
#   snap_threshold (0-400 px): Distance for instant snap vs gradual approach.
#
# NEW AIMING SETTINGS (added Dec 2024):
#   aim_aggression (0-100): Controls how aggressively the turret pursues center.
#       0 = conservative/lazy, 100 = maximum aggression with boosted final approach.
#   final_approach_boost (True/False): When True, applies 2-3x speed multiplier
#       and reduces smoothing when target is within 2x deadzone radius.
#
# YOLO-SPECIFIC SETTINGS (only for YOLO detection modes):
#   yolo_confidence (0.0-1.0): Minimum confidence threshold for detections.
#   yolo_classes (string): Comma-separated YOLO class names to detect.
#   yolo_model (string): YOLO model file to use (yolov8n/s/m/l/x.pt).
#
# DETECTION MODE:
#   detection_mode: ONLY included for target-specific presets that REQUIRE YOLO.
#       General performance presets do NOT set detection_mode, preserving user's
#       current detection mode selection.
#
# MOTION DETECTION SETTINGS (for BackgroundSub/FrameDiff modes):
#   threshold, blur_kernel, min_contour, max_contour, dilate_iter, backsub_warmup
#

PRESETS = {
    # ==========================================================================
    # BASE PERFORMANCE PROFILES
    # These presets control tracking aggressiveness WITHOUT changing detection mode.
    # Users can combine any of these with their preferred detection method.
    # ==========================================================================
    
    "Smooth / Conservative": {
        # Gentle, smooth tracking - ideal for slow-moving targets or demos
        "tracking_speed": 20,
        "movement_sensitivity": 15,
        "smoothing_factor": 0.98,
        "deadzone": 30,
        "snap_threshold": 50,
        "aim_aggression": 10,           # Very conservative aiming
        "final_approach_boost": False,  # No boost - smooth all the way
        # YOLO settings (applied if YOLO mode is active)
        "yolo_confidence": 0.6,
        "yolo_classes": "person",
        "yolo_model": "yolov8n.pt",
        # NOTE: No detection_mode - preserves user's current selection
    },
    
    "Balanced": {
        # Good all-around preset - recommended starting point
        "tracking_speed": 40,
        "movement_sensitivity": 30,
        "smoothing_factor": 0.95,
        "deadzone": 20,
        "snap_threshold": 80,
        "aim_aggression": 35,           # Moderate aggression
        "final_approach_boost": True,   # Boost for final centering
        "yolo_confidence": 0.5,
        "yolo_classes": "person",
        "yolo_model": "yolov8n.pt",
    },
    
    "Responsive": {
        # Quick response for moderately fast targets
        "tracking_speed": 60,
        "movement_sensitivity": 50,
        "smoothing_factor": 0.85,
        "deadzone": 12,
        "snap_threshold": 120,
        "aim_aggression": 55,           # Above average aggression
        "final_approach_boost": True,
        "yolo_confidence": 0.45,
        "yolo_classes": "person",
        "yolo_model": "yolov8s.pt",
    },
    
    "Aggressive": {
        # Fast tracking with strong centering force
        "tracking_speed": 80,
        "movement_sensitivity": 70,
        "smoothing_factor": 0.75,
        "deadzone": 8,
        "snap_threshold": 160,
        "aim_aggression": 75,           # High aggression
        "final_approach_boost": True,
        "yolo_confidence": 0.4,
        "yolo_classes": "person",
        "yolo_model": "yolov8m.pt",
    },
    
    "Very Aggressive": {
        # Maximum stock aggression - fast but may overshoot
        "tracking_speed": 95,
        "movement_sensitivity": 90,
        "smoothing_factor": 0.6,
        "deadzone": 4,
        "snap_threshold": 220,
        "aim_aggression": 90,           # Very high aggression
        "final_approach_boost": True,
        "yolo_confidence": 0.35,
        "yolo_classes": "person",
        "yolo_model": "yolov8m.pt",
    },
    
    "Maximum Aggression": {
        # NEW: Absolute maximum tracking aggression
        # Warning: May cause overshoot/oscillation on some servo setups
        "tracking_speed": 100,
        "movement_sensitivity": 100,
        "smoothing_factor": 0.3,        # Minimal smoothing for instant response
        "deadzone": 2,                  # Tiny deadzone - always correcting
        "snap_threshold": 300,
        "aim_aggression": 100,          # Maximum aggression
        "final_approach_boost": True,
        "yolo_confidence": 0.3,
        "yolo_classes": "person",
        "yolo_model": "yolov8m.pt",
    },
    
    "Precision Sniper": {
        # NEW: Optimized for accurate centering over speed
        # Moderate speed but very precise final approach
        "tracking_speed": 50,
        "movement_sensitivity": 45,
        "smoothing_factor": 0.7,
        "deadzone": 3,                  # Very small deadzone for precision
        "snap_threshold": 100,
        "aim_aggression": 85,           # High aggression for final centering
        "final_approach_boost": True,
        "yolo_confidence": 0.5,
        "yolo_classes": "person",
        "yolo_model": "yolov8s.pt",
    },
    
    # ==========================================================================
    # TARGET-SPECIFIC PRESETS
    # These presets ARE designed for specific YOLO classes, so they INCLUDE
    # detection_mode to ensure YOLO is active when selected.
    # ==========================================================================
    
    "Track Person": {
        # Optimized for human tracking
        "tracking_speed": 55,
        "movement_sensitivity": 40,
        "smoothing_factor": 0.9,
        "deadzone": 15,
        "snap_threshold": 100,
        "aim_aggression": 50,
        "final_approach_boost": True,
        "yolo_confidence": 0.5,
        "yolo_classes": "person",
        "yolo_model": "yolov8m.pt",
        "detection_mode": "YOLO Object Detection",  # REQUIRED: Needs YOLO for person class
    },
    
    "Track Mouse": {
        # Fast, aggressive tracking for small rodents
        "tracking_speed": 80,
        "movement_sensitivity": 85,
        "smoothing_factor": 0.7,
        "deadzone": 4,
        "snap_threshold": 160,
        "aim_aggression": 80,
        "final_approach_boost": True,
        "yolo_confidence": 0.3,
        "yolo_classes": "mouse, rodent",
        "yolo_model": "yolov8x.pt",  # Larger model for small object accuracy
        "detection_mode": "YOLO Object Detection",  # REQUIRED: Needs YOLO for mouse class
        # Motion detection fallback settings
        "threshold": 30,
        "blur_kernel": 7,
        "min_contour": 400,
        "dilate_iter": 3,
    },
    
    "Track Cats": {
        # Balanced tracking for cats - medium speed, good precision
        "tracking_speed": 65,
        "movement_sensitivity": 55,
        "smoothing_factor": 0.85,
        "deadzone": 10,
        "snap_threshold": 130,
        "aim_aggression": 60,
        "final_approach_boost": True,
        "yolo_confidence": 0.45,
        "yolo_classes": "cat",
        "yolo_model": "yolov8m.pt",
        "detection_mode": "YOLO Object Detection",  # REQUIRED: Needs YOLO for cat class
        "threshold": 40,
        "blur_kernel": 5,
        "min_contour": 800,
        "dilate_iter": 2,
    },
    
    "Track Dogs": {
        # Slightly slower than cats - dogs are generally larger/slower
        "tracking_speed": 60,
        "movement_sensitivity": 50,
        "smoothing_factor": 0.88,
        "deadzone": 12,
        "snap_threshold": 120,
        "aim_aggression": 55,
        "final_approach_boost": True,
        "yolo_confidence": 0.45,
        "yolo_classes": "dog",
        "yolo_model": "yolov8m.pt",
        "detection_mode": "YOLO Object Detection",  # REQUIRED: Needs YOLO for dog class
        "threshold": 45,
        "blur_kernel": 5,
        "min_contour": 1000,
        "dilate_iter": 2,
    },
    
    "Track Vehicles": {
        # Optimized for cars, trucks, motorcycles
        "tracking_speed": 70,
        "movement_sensitivity": 65,
        "smoothing_factor": 0.8,
        "deadzone": 20,
        "snap_threshold": 180,
        "aim_aggression": 65,
        "final_approach_boost": True,
        "yolo_confidence": 0.4,
        "yolo_classes": "car, truck, bus, motorcycle",
        "yolo_model": "yolov8l.pt",
        "detection_mode": "YOLO Object Detection",  # REQUIRED: Needs YOLO for vehicle classes
        "threshold": 50,
        "blur_kernel": 5,
        "min_contour": 1200,
        "dilate_iter": 2,
    },
    
    # ==========================================================================
    # RESOLUTION-OPTIMIZED PRESETS
    # These presets are optimized for specific camera resolutions and FOV.
    # They do NOT set detection_mode - user can choose their preferred method.
    # ==========================================================================
    
    "Wide FOV (1920x1080)": {
        # Full width capture for 170° wide-angle cameras
        "frame_ratio_setting": "1920x1080 (Full Wide FOV)",
        "tracking_speed": 35,
        "movement_sensitivity": 25,
        "smoothing_factor": 0.92,
        "deadzone": 25,
        "snap_threshold": 60,
        "aim_aggression": 40,
        "final_approach_boost": True,
        "yolo_confidence": 0.5,
        "yolo_classes": "person",
        "yolo_model": "yolov8n.pt",
        # NOTE: No detection_mode - user can use BackgroundSub, YOLO, or FrameDiff
        # Motion detection tuned for high resolution
        "threshold": 35,
        "blur_kernel": 5,
        "min_contour": 800,  # Adjusted for larger frame area
        "dilate_iter": 2,
        "backsub_warmup": 40,
    },
    
    "Balanced (1280x720)": {
        # Recommended default - good balance of FOV, processing speed, and accuracy
        "frame_ratio_setting": "1280x720 (HD)",
        "tracking_speed": 50,
        "movement_sensitivity": 35,
        "smoothing_factor": 0.90,
        "deadzone": 20,
        "snap_threshold": 90,
        "aim_aggression": 45,
        "final_approach_boost": True,
        "yolo_confidence": 0.5,
        "yolo_classes": "person",
        "yolo_model": "yolov8n.pt",
        "threshold": 32,
        "blur_kernel": 5,
        "min_contour": 600,
        "dilate_iter": 2,
        "backsub_warmup": 35,
    },
    
    "Fast (640x480)": {
        # Minimum processing for maximum speed - best for low-power systems
        "frame_ratio_setting": "640x480 (Fast)",
        "tracking_speed": 65,
        "movement_sensitivity": 45,
        "smoothing_factor": 0.85,
        "deadzone": 15,
        "snap_threshold": 110,
        "aim_aggression": 50,
        "final_approach_boost": True,
        "yolo_confidence": 0.55,
        "yolo_classes": "person",
        "yolo_model": "yolov8n.pt",
        "threshold": 28,
        "blur_kernel": 3,
        "min_contour": 200,  # Smaller min for lower resolution
        "dilate_iter": 1,
    },
}

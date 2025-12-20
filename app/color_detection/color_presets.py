"""
Color Detection Presets for DADBOT v4
=====================================

These presets are designed to be added to turret_presets.py PRESETS dict.
They configure the turret for color-based tracking scenarios.

Usage:
    Copy the COLOR_PRESETS dict contents into the main PRESETS dict
    in turret_presets.py during integration.
"""

# =============================================================================
# COLOR DETECTION PRESETS
# Add these to PRESETS dict in turret_presets.py
# =============================================================================

COLOR_PRESETS = {
    # =========================================================================
    # PURE COLOR DETECTION PRESETS (Mode 6)
    # =========================================================================
    
    "Track Laser Pointer": {
        # Optimized for tracking laser pointer dots
        "tracking_speed": 90,
        "movement_sensitivity": 85,
        "smoothing_factor": 0.5,        # Low smoothing for fast response
        "deadzone": 3,                   # Very small - laser dots are precise
        "snap_threshold": 200,
        "aim_aggression": 95,            # Maximum aggression for tiny targets
        "final_approach_boost": True,
        "detection_mode": "Color Detection",  # Mode 6
        # Color-specific settings
        "color_preset": "laser_red",
        "color_min_area": 5,             # Laser dots are tiny
        "color_max_area": 500,
        "color_blur": 3,
        "color_morph": 1,
    },
    
    "Track Red Objects": {
        # General red object tracking
        "tracking_speed": 60,
        "movement_sensitivity": 50,
        "smoothing_factor": 0.85,
        "deadzone": 15,
        "snap_threshold": 100,
        "aim_aggression": 55,
        "final_approach_boost": True,
        "detection_mode": "Color Detection",
        "color_preset": "red",
        "color_min_area": 300,
        "color_max_area": 200000,
        "color_blur": 5,
        "color_morph": 2,
    },
    
    "Track Green Objects": {
        # Green object tracking (tennis balls, safety items)
        "tracking_speed": 65,
        "movement_sensitivity": 55,
        "smoothing_factor": 0.82,
        "deadzone": 12,
        "snap_threshold": 110,
        "aim_aggression": 60,
        "final_approach_boost": True,
        "detection_mode": "Color Detection",
        "color_preset": "neon_green",
        "color_min_area": 400,
        "color_max_area": 150000,
        "color_blur": 5,
        "color_morph": 2,
    },
    
    "Track Blue Objects": {
        # Blue object tracking
        "tracking_speed": 55,
        "movement_sensitivity": 45,
        "smoothing_factor": 0.88,
        "deadzone": 15,
        "snap_threshold": 95,
        "aim_aggression": 50,
        "final_approach_boost": True,
        "detection_mode": "Color Detection",
        "color_preset": "blue",
        "color_min_area": 300,
        "color_max_area": 200000,
        "color_blur": 5,
        "color_morph": 2,
    },
    
    "Track Yellow Objects": {
        # Yellow object tracking
        "tracking_speed": 58,
        "movement_sensitivity": 48,
        "smoothing_factor": 0.85,
        "deadzone": 14,
        "snap_threshold": 100,
        "aim_aggression": 52,
        "final_approach_boost": True,
        "detection_mode": "Color Detection",
        "color_preset": "yellow",
        "color_min_area": 300,
        "color_max_area": 200000,
        "color_blur": 5,
        "color_morph": 2,
    },
    
    "Track Orange Objects": {
        # Orange object tracking
        "tracking_speed": 58,
        "movement_sensitivity": 48,
        "smoothing_factor": 0.85,
        "deadzone": 14,
        "snap_threshold": 100,
        "aim_aggression": 52,
        "final_approach_boost": True,
        "detection_mode": "Color Detection",
        "color_preset": "orange",
        "color_min_area": 300,
        "color_max_area": 200000,
        "color_blur": 5,
        "color_morph": 2,
    },
    
    "Track Safety Vest": {
        # High-visibility safety vest tracking (orange/neon)
        "tracking_speed": 50,
        "movement_sensitivity": 40,
        "smoothing_factor": 0.9,
        "deadzone": 20,
        "snap_threshold": 80,
        "aim_aggression": 45,
        "final_approach_boost": True,
        "detection_mode": "Color Detection",
        "color_preset": "neon_green",    # or "orange" for orange vests
        "color_min_area": 2000,          # Vests are large
        "color_max_area": 300000,
        "color_blur": 7,
        "color_morph": 2,
    },
    
    "Track Tennis Ball": {
        # Tennis ball / yellow-green ball tracking
        "tracking_speed": 70,
        "movement_sensitivity": 60,
        "smoothing_factor": 0.75,
        "deadzone": 10,
        "snap_threshold": 120,
        "aim_aggression": 65,
        "final_approach_boost": True,
        "detection_mode": "Color Detection",
        "color_preset": "neon_green",
        "color_min_area": 200,
        "color_max_area": 50000,
        "color_blur": 5,
        "color_morph": 2,
    },
    
    # =========================================================================
    # HYBRID COLOR PRESETS (Modes 7, 8, 9)
    # =========================================================================
    
    "Laser + Motion (Hybrid)": {
        # Laser tracking with motion confirmation (reduces static reflections)
        "tracking_speed": 85,
        "movement_sensitivity": 80,
        "smoothing_factor": 0.6,
        "deadzone": 4,
        "snap_threshold": 180,
        "aim_aggression": 90,
        "final_approach_boost": True,
        "detection_mode": "Hybrid: Color+FD",  # Mode 7
        "color_preset": "laser_red",
        "color_min_area": 5,
        "color_max_area": 500,
        "color_blur": 3,
        "color_morph": 1,
        # Frame diff settings for motion gate
        "threshold": 25,
        "blur_kernel": 3,
        # Fusion settings
        "fusion_strategy": "AND",
        "fusion_overlap": 0.2,
    },
    
    "Color + Background (Hybrid)": {
        # Color detection with background subtraction for moving targets
        "tracking_speed": 55,
        "movement_sensitivity": 50,
        "smoothing_factor": 0.85,
        "deadzone": 15,
        "snap_threshold": 95,
        "aim_aggression": 50,
        "final_approach_boost": True,
        "detection_mode": "Hybrid: Color+BS",  # Mode 8
        "color_preset": "red",
        "color_min_area": 300,
        "color_max_area": 150000,
        # Background sub settings
        "mog2_history": 500,
        "mog2_threshold": 16,
        # Fusion settings
        "fusion_strategy": "AND",
        "fusion_overlap": 0.3,
    },
    
    "Color + YOLO Confirm": {
        # Color detection with YOLO confirmation for maximum accuracy
        "tracking_speed": 55,
        "movement_sensitivity": 45,
        "smoothing_factor": 0.88,
        "deadzone": 15,
        "snap_threshold": 90,
        "aim_aggression": 50,
        "final_approach_boost": True,
        "detection_mode": "Hybrid: Color+YOLO",  # Mode 9
        "color_preset": "red",
        "color_min_area": 500,
        "color_max_area": 150000,
        # YOLO settings for confirmation
        "yolo_confidence": 0.4,
        "yolo_classes": "person, sports ball",
        "yolo_model": "yolov8n.pt",
        # Fusion settings
        "fusion_strategy": "AND",
        "fusion_overlap": 0.3,
    },
    
    "Multi-Color Tracking": {
        # Track multiple colors at once
        "tracking_speed": 55,
        "movement_sensitivity": 45,
        "smoothing_factor": 0.88,
        "deadzone": 15,
        "snap_threshold": 90,
        "aim_aggression": 50,
        "final_approach_boost": True,
        "detection_mode": "Color Detection",
        "color_preset": "red,green,blue",  # Multiple colors
        "color_min_area": 300,
        "color_max_area": 200000,
        "color_blur": 5,
        "color_morph": 2,
    },
}


# =============================================================================
# HELPER FUNCTION FOR INTEGRATION
# =============================================================================

def get_color_preset_names():
    """Return list of color preset names for UI dropdown."""
    return list(COLOR_PRESETS.keys())


def get_preset(name: str) -> dict:
    """Get a specific preset by name."""
    return COLOR_PRESETS.get(name, {})


# For testing
if __name__ == "__main__":
    print("Color Detection Presets:")
    print("=" * 50)
    for name in COLOR_PRESETS:
        preset = COLOR_PRESETS[name]
        mode = preset.get("detection_mode", "Unknown")
        color = preset.get("color_preset", "N/A")
        print(f"  {name}")
        print(f"    Mode: {mode}")
        print(f"    Color: {color}")
        print()

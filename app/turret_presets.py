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
#   detection_mode: If present, the preset will switch the detection mode dropdown.
#       (Most size-tier presets include it to ensure consistent behavior.)
#
# MOTION DETECTION SETTINGS (for BackgroundSub/FrameDiff modes):
#   threshold, blur_kernel, min_contour, max_contour, dilate_iter, backsub_warmup
#

# Precision Aim defaults (persisted + presettable). These are conservative for 1280x720.
PRECISION_DEFAULTS = {
    "precision_mode": False,
    "precision_roi": 48,
    "precision_kp": 0.02,
    "precision_ki": 0.001,
    "precision_kd": 0.005,
    "precision_hfov": 90.0,
    "precision_max_step": 1.0,
    "precision_frac_threshold": 0.25,
}

# Speed optimization presets (Feb 2026)
SPEED_BEHAVIOR_SMOOTH = {
    "speed_opt_enabled": True,
    "speed_serial_interval_ms": 20,
    "speed_bus_servo_time_ms": 18,
    "speed_predictive_lead_ms": 35,
    "speed_predictive_max_px": 80,
    "speed_roi_enabled": True,
    "speed_roi_scale": 0.75,
    "speed_roi_min_size": 220,
    "speed_roi_padding_px": 28,
    "speed_threaded_yolo": True,
    "speed_threaded_yolo_max_age_s": 0.7,
    "speed_prefer_light_yolo": True,
    "speed_disable_command_filter": False,
}

SPEED_BEHAVIOR_RESPONSIVE = {
    "speed_opt_enabled": True,
    "speed_serial_interval_ms": 16,
    "speed_bus_servo_time_ms": 14,
    "speed_predictive_lead_ms": 55,
    "speed_predictive_max_px": 110,
    "speed_roi_enabled": True,
    "speed_roi_scale": 0.65,
    "speed_roi_min_size": 200,
    "speed_roi_padding_px": 24,
    "speed_threaded_yolo": True,
    "speed_threaded_yolo_max_age_s": 0.6,
    "speed_prefer_light_yolo": True,
    "speed_disable_command_filter": True,
}

SPEED_BEHAVIOR_AGGRESSIVE = {
    "speed_opt_enabled": True,
    "speed_serial_interval_ms": 12,
    "speed_bus_servo_time_ms": 10,
    "speed_predictive_lead_ms": 85,
    "speed_predictive_max_px": 140,
    "speed_roi_enabled": True,
    "speed_roi_scale": 0.55,
    "speed_roi_min_size": 180,
    "speed_roi_padding_px": 20,
    "speed_threaded_yolo": True,
    "speed_threaded_yolo_max_age_s": 0.5,
    "speed_prefer_light_yolo": True,
    "speed_disable_command_filter": True,
}

SPEED_MOTION_BALANCED = {
    "speed_opt_enabled": True,
    "speed_serial_interval_ms": 18,
    "speed_bus_servo_time_ms": 16,
    "speed_predictive_lead_ms": 45,
    "speed_predictive_max_px": 90,
    "speed_roi_enabled": False,
    "speed_roi_scale": 0.7,
    "speed_roi_min_size": 220,
    "speed_roi_padding_px": 24,
    "speed_threaded_yolo": False,
    "speed_threaded_yolo_max_age_s": 0.6,
    "speed_prefer_light_yolo": False,
    "speed_disable_command_filter": False,
}

SPEED_YOLO_FAST = {
    "speed_opt_enabled": True,
    "speed_serial_interval_ms": 15,
    "speed_bus_servo_time_ms": 12,
    "speed_predictive_lead_ms": 70,
    "speed_predictive_max_px": 120,
    "speed_roi_enabled": True,
    "speed_roi_scale": 0.6,
    "speed_roi_min_size": 200,
    "speed_roi_padding_px": 24,
    "speed_threaded_yolo": True,
    "speed_threaded_yolo_max_age_s": 0.6,
    "speed_prefer_light_yolo": True,
    "speed_disable_command_filter": True,
}

PRESETS = {
    # ======================================================================
    # CONSISTENT PRESET NAMING (Dec 2025)
    # Format: "Target / <Detection Mode> / <Size Tier> / <Profile>"
    # Size tiers:
    #   Small  = rat-sized contour band
    #   Medium = dog-sized contour band
    #   Person = person/human-sized contour band
    #
    # Goal: while you learn the technical UI settings, these presets give you
    # predictable, size-gated behavior that prevents giant blobs from locking
    # and firing. All presets set BOTH min_contour and max_contour.
    # ======================================================================

    # ----------------------------------------------------------------------
    # Shared tracking behavior (applies across modes)
    # ----------------------------------------------------------------------

    "Behavior / Smooth": {
        "tracking_speed": 45,
        "movement_sensitivity": 35,
        "smoothing_factor": 0.75,
        "deadzone": 22,
        "snap_threshold": 90,
        "aim_aggression": 35,
        "final_approach_boost": True,
        "detection_pause_ms": 400,
        "motion_fire_frames_required": 2,
        "fire_stability_frames_required": 2,
        "speed_profile_mode": "Balanced",
        **PRECISION_DEFAULTS,
    },

    "Behavior / Responsive": {
        "tracking_speed": 65,
        "movement_sensitivity": 50,
        "smoothing_factor": 0.22,
        "deadzone": 10,
        "snap_threshold": 120,
        "aim_aggression": 90,
        "final_approach_boost": True,
        "detection_pause_ms": 300,
        "motion_fire_frames_required": 1,
        "fire_stability_frames_required": 1,
        "speed_profile_mode": "Aggressive",
        **PRECISION_DEFAULTS,
        "precision_mode": False,
        "precision_max_step": 1.8,
    },

    "Behavior / Aggressive": {
        "tracking_speed": 80,
        "movement_sensitivity": 65,
        "smoothing_factor": 0.18,
        "deadzone": 8,
        "snap_threshold": 160,
        "aim_aggression": 95,
        "final_approach_boost": True,
        "detection_pause_ms": 250,
        "motion_fire_frames_required": 1,
        "fire_stability_frames_required": 1,
        "speed_profile_mode": "Aggressive",
        **PRECISION_DEFAULTS,
        "precision_mode": False,
        "precision_max_step": 1.8,
        # Single-strike aiming: one decisive move then short hold (avoids many micro-steps)
        "auto_strike_enabled": True,
        "auto_strike_hold_ms": 320,
        "auto_strike_cooldown_ms": 260,
        "auto_strike_min_error_deg": 2.0,
    },

    # ----------------------------------------------------------------------
    # Target / Frame Difference (Mode 0)
    # ----------------------------------------------------------------------

    "Target / Frame Difference / Small / Balanced": {
        "detection_mode": "Frame Difference",
        "threshold": 30,
        "blur_kernel": 5,
        "dilate_iter": 1,
        "min_contour": 900,
        "max_contour": 25000,
        "backsub_warmup": 10,
        "tracking_speed": 60,
        "movement_sensitivity": 45,
        "smoothing_factor": 0.55,
        "deadzone": 22,
        "snap_threshold": 120,
        "aim_aggression": 50,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / Frame Difference / Small / Sensitive": {
        "detection_mode": "Frame Difference",
        "threshold": 24,
        "blur_kernel": 3,
        "dilate_iter": 2,
        "min_contour": 500,
        "max_contour": 22000,
        "backsub_warmup": 10,
        "tracking_speed": 65,
        "movement_sensitivity": 50,
        "smoothing_factor": 0.50,
        "deadzone": 22,
        "snap_threshold": 130,
        "aim_aggression": 55,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / Frame Difference / Medium / Balanced": {
        "detection_mode": "Frame Difference",
        "threshold": 26,
        "blur_kernel": 5,
        "dilate_iter": 2,
        "min_contour": 8000,
        "max_contour": 140000,
        "backsub_warmup": 10,
        "tracking_speed": 65,
        "movement_sensitivity": 50,
        "smoothing_factor": 0.50,
        "deadzone": 20,
        "snap_threshold": 130,
        "aim_aggression": 55,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / Frame Difference / Medium / Sensitive": {
        "detection_mode": "Frame Difference",
        "threshold": 24,
        "blur_kernel": 5,
        "dilate_iter": 2,
        "min_contour": 6000,
        "max_contour": 160000,
        "backsub_warmup": 10,
        "tracking_speed": 70,
        "movement_sensitivity": 55,
        "smoothing_factor": 0.45,
        "deadzone": 20,
        "snap_threshold": 150,
        "aim_aggression": 60,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / Frame Difference / Person / Precision Clamp": {
        "detection_mode": "Frame Difference",
        "threshold": 24,
        "blur_kernel": 3,
        "dilate_iter": 1,
        "min_contour": 60000,
        "max_contour": 450000,
        "backsub_warmup": 10,
        "tracking_speed": 70,
        "movement_sensitivity": 55,
        "smoothing_factor": 0.45,
        "deadzone": 16,
        "snap_threshold": 150,
        "aim_aggression": 60,
        "final_approach_boost": True,
        # Enable precision for large targets (helps final lock without overshoot)
        "precision_mode": True,
        "precision_roi": 64,
        "precision_kp": 0.018,
        "precision_ki": 0.001,
        "precision_kd": 0.006,
        "precision_hfov": 90.0,
        "precision_max_step": 0.9,
        "precision_frac_threshold": 0.25,
    },

    # ----------------------------------------------------------------------
    # Target / Background Subtraction (Mode 1)
    # ----------------------------------------------------------------------

    "Target / Background Subtraction / Small / Stable": {
        "detection_mode": "Background Subtraction",
        "threshold": 28,
        "blur_kernel": 5,
        "dilate_iter": 1,
        "min_contour": 900,
        "max_contour": 25000,
        "backsub_warmup": 25,
        "tracking_speed": 60,
        "movement_sensitivity": 45,
        "smoothing_factor": 0.55,
        "deadzone": 22,
        "snap_threshold": 120,
        "aim_aggression": 50,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / Background Subtraction / Small / Sensitive": {
        "detection_mode": "Background Subtraction",
        "threshold": 24,
        "blur_kernel": 3,
        "dilate_iter": 2,
        "min_contour": 500,
        "max_contour": 22000,
        "backsub_warmup": 18,
        "tracking_speed": 65,
        "movement_sensitivity": 50,
        "smoothing_factor": 0.50,
        "deadzone": 22,
        "snap_threshold": 130,
        "aim_aggression": 55,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / Background Subtraction / Medium / Balanced": {
        "detection_mode": "Background Subtraction",
        "threshold": 26,
        "blur_kernel": 5,
        "dilate_iter": 1,
        "min_contour": 8000,
        "max_contour": 140000,
        "backsub_warmup": 30,
        "tracking_speed": 65,
        "movement_sensitivity": 50,
        "smoothing_factor": 0.50,
        "deadzone": 20,
        "snap_threshold": 130,
        "aim_aggression": 55,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / Background Subtraction / Medium / Stable": {
        "detection_mode": "Background Subtraction",
        "threshold": 28,
        "blur_kernel": 5,
        "dilate_iter": 1,
        "min_contour": 8000,
        "max_contour": 140000,
        "backsub_warmup": 40,
        "tracking_speed": 65,
        "movement_sensitivity": 50,
        "smoothing_factor": 0.55,
        "deadzone": 20,
        "snap_threshold": 130,
        "aim_aggression": 55,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / Background Subtraction / Person / Precision Clamp": {
        "detection_mode": "Background Subtraction",
        "threshold": 24,
        "blur_kernel": 3,
        "dilate_iter": 1,
        "min_contour": 60000,
        "max_contour": 450000,
        "backsub_warmup": 35,
        "tracking_speed": 70,
        "movement_sensitivity": 55,
        "smoothing_factor": 0.45,
        "deadzone": 16,
        "snap_threshold": 150,
        "aim_aggression": 60,
        "final_approach_boost": True,
        "precision_mode": True,
        "precision_roi": 64,
        "precision_kp": 0.018,
        "precision_ki": 0.001,
        "precision_kd": 0.006,
        "precision_hfov": 90.0,
        "precision_max_step": 0.9,
        "precision_frac_threshold": 0.25,
    },

    # ----------------------------------------------------------------------
    # Target / Hybrid: Frame Diff + BackSub (Mode 3)
    # ----------------------------------------------------------------------

    "Target / Hybrid: Frame Diff + BackSub / Small / OR Lenient": {
        "detection_mode": "Hybrid: Frame Diff + BackSub",
        "fusion_strategy": 1,
        "threshold": 26,
        "blur_kernel": 5,
        "dilate_iter": 2,
        "min_contour": 900,
        "max_contour": 25000,
        "backsub_warmup": 20,
        "tracking_speed": 60,
        "movement_sensitivity": 45,
        "smoothing_factor": 0.55,
        "deadzone": 22,
        "snap_threshold": 120,
        "aim_aggression": 50,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / Hybrid: Frame Diff + BackSub / Small / AND Strict": {
        "detection_mode": "Hybrid: Frame Diff + BackSub",
        "fusion_strategy": 0,
        "threshold": 28,
        "blur_kernel": 5,
        "dilate_iter": 1,
        "min_contour": 1200,
        "max_contour": 25000,
        "backsub_warmup": 25,
        "tracking_speed": 60,
        "movement_sensitivity": 45,
        "smoothing_factor": 0.60,
        "deadzone": 22,
        "snap_threshold": 120,
        "aim_aggression": 50,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / Hybrid: Frame Diff + BackSub / Medium / AND Strict": {
        "detection_mode": "Hybrid: Frame Diff + BackSub",
        "fusion_strategy": 0,
        "threshold": 26,
        "blur_kernel": 5,
        "dilate_iter": 1,
        "min_contour": 8000,
        "max_contour": 140000,
        "backsub_warmup": 25,
        "tracking_speed": 65,
        "movement_sensitivity": 50,
        "smoothing_factor": 0.50,
        "deadzone": 20,
        "snap_threshold": 130,
        "aim_aggression": 55,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / Hybrid: Frame Diff + BackSub / Medium / OR Lenient": {
        "detection_mode": "Hybrid: Frame Diff + BackSub",
        "fusion_strategy": 1,
        "threshold": 26,
        "blur_kernel": 5,
        "dilate_iter": 2,
        "min_contour": 8000,
        "max_contour": 140000,
        "backsub_warmup": 20,
        "tracking_speed": 65,
        "movement_sensitivity": 50,
        "smoothing_factor": 0.50,
        "deadzone": 20,
        "snap_threshold": 130,
        "aim_aggression": 55,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / Hybrid: Frame Diff + BackSub / Person / Precision Clamp": {
        "detection_mode": "Hybrid: Frame Diff + BackSub",
        "fusion_strategy": 0,
        "threshold": 24,
        "blur_kernel": 3,
        "dilate_iter": 1,
        "min_contour": 60000,
        "max_contour": 450000,
        "backsub_warmup": 30,
        "tracking_speed": 70,
        "movement_sensitivity": 55,
        "smoothing_factor": 0.45,
        "deadzone": 16,
        "snap_threshold": 150,
        "aim_aggression": 60,
        "final_approach_boost": True,
        "precision_mode": True,
        "precision_roi": 64,
        "precision_kp": 0.018,
        "precision_ki": 0.001,
        "precision_kd": 0.006,
        "precision_hfov": 90.0,
        "precision_max_step": 0.9,
        "precision_frac_threshold": 0.25,
    },

    # ----------------------------------------------------------------------
    # Target / YOLO (Mode 2)
    # ----------------------------------------------------------------------

    "Target / YOLO / Small / Sensitive": {
        "detection_mode": "YOLO Object Detection",
        "yolo_classes": "person",
        "yolo_model": "yolov8s.pt",
        "yolo_confidence": 0.35,
        "yolo_min_area": 5000,
        "yolo_max_results": 5,
        "tracking_speed": 60,
        "movement_sensitivity": 45,
        "smoothing_factor": 0.55,
        "deadzone": 22,
        "snap_threshold": 120,
        "aim_aggression": 50,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / YOLO / Small / Balanced": {
        "detection_mode": "YOLO Object Detection",
        "yolo_classes": "person",
        "yolo_model": "yolov8s.pt",
        "yolo_confidence": 0.40,
        "yolo_min_area": 7000,
        "yolo_max_results": 5,
        "tracking_speed": 60,
        "movement_sensitivity": 45,
        "smoothing_factor": 0.55,
        "deadzone": 22,
        "snap_threshold": 120,
        "aim_aggression": 50,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / YOLO / Medium / Balanced": {
        "detection_mode": "YOLO Object Detection",
        "yolo_classes": "person",
        "yolo_model": "yolov8m.pt",
        "yolo_confidence": 0.45,
        "yolo_min_area": 15000,
        "yolo_max_results": 5,
        "tracking_speed": 65,
        "movement_sensitivity": 50,
        "smoothing_factor": 0.50,
        "deadzone": 20,
        "snap_threshold": 130,
        "aim_aggression": 55,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / YOLO / Medium / Sensitive": {
        "detection_mode": "YOLO Object Detection",
        "yolo_classes": "person",
        "yolo_model": "yolov8m.pt",
        "yolo_confidence": 0.40,
        "yolo_min_area": 12000,
        "yolo_max_results": 5,
        "tracking_speed": 70,
        "movement_sensitivity": 55,
        "smoothing_factor": 0.45,
        "deadzone": 20,
        "snap_threshold": 150,
        "aim_aggression": 60,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / YOLO / Person / Precision": {
        "detection_mode": "YOLO Object Detection",
        "yolo_classes": "person",
        "yolo_model": "yolov8m.pt",
        "yolo_confidence": 0.50,
        "yolo_min_area": 40000,
        "yolo_max_results": 5,
        "tracking_speed": 70,
        "movement_sensitivity": 55,
        "smoothing_factor": 0.45,
        "deadzone": 16,
        "snap_threshold": 150,
        "aim_aggression": 60,
        "final_approach_boost": True,
        "precision_mode": True,
        "precision_roi": 64,
        "precision_kp": 0.018,
        "precision_ki": 0.001,
        "precision_kd": 0.006,
        "precision_hfov": 90.0,
        "precision_max_step": 0.9,
        "precision_frac_threshold": 0.25,
    },

    # ----------------------------------------------------------------------
    # Target / Hybrid: Frame Diff + YOLO (Mode 4)
    # ----------------------------------------------------------------------

    "Target / Hybrid: Frame Diff + YOLO / Small / Motion Gate Lenient": {
        "detection_mode": "Hybrid: Frame Diff + YOLO",
        "motion_gate_threshold": 0.85,
        "threshold": 28,
        "blur_kernel": 5,
        "dilate_iter": 2,
        "min_contour": 900,
        "max_contour": 25000,
        "yolo_classes": "person",
        "yolo_model": "yolov8s.pt",
        "yolo_confidence": 0.35,
        "yolo_min_area": 5000,
        "yolo_max_results": 5,
        "tracking_speed": 60,
        "movement_sensitivity": 45,
        "smoothing_factor": 0.55,
        "deadzone": 22,
        "snap_threshold": 120,
        "aim_aggression": 50,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / Hybrid: Frame Diff + YOLO / Small / Motion Gate Balanced": {
        "detection_mode": "Hybrid: Frame Diff + YOLO",
        "motion_gate_threshold": 0.95,
        "threshold": 26,
        "blur_kernel": 5,
        "dilate_iter": 2,
        "min_contour": 900,
        "max_contour": 25000,
        "yolo_classes": "person",
        "yolo_model": "yolov8s.pt",
        "yolo_confidence": 0.40,
        "yolo_min_area": 7000,
        "yolo_max_results": 5,
        "tracking_speed": 60,
        "movement_sensitivity": 45,
        "smoothing_factor": 0.55,
        "deadzone": 22,
        "snap_threshold": 120,
        "aim_aggression": 50,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / Hybrid: Frame Diff + YOLO / Medium / Motion Gate Balanced": {
        "detection_mode": "Hybrid: Frame Diff + YOLO",
        "motion_gate_threshold": 1.0,
        "threshold": 26,
        "blur_kernel": 5,
        "dilate_iter": 1,
        "min_contour": 8000,
        "max_contour": 140000,
        "yolo_classes": "person",
        "yolo_model": "yolov8m.pt",
        "yolo_confidence": 0.45,
        "yolo_min_area": 15000,
        "yolo_max_results": 5,
        "tracking_speed": 65,
        "movement_sensitivity": 50,
        "smoothing_factor": 0.50,
        "deadzone": 20,
        "snap_threshold": 130,
        "aim_aggression": 55,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / Hybrid: Frame Diff + YOLO / Medium / Motion Gate Lenient": {
        "detection_mode": "Hybrid: Frame Diff + YOLO",
        "motion_gate_threshold": 0.9,
        "threshold": 26,
        "blur_kernel": 5,
        "dilate_iter": 2,
        "min_contour": 8000,
        "max_contour": 160000,
        "yolo_classes": "person",
        "yolo_model": "yolov8m.pt",
        "yolo_confidence": 0.40,
        "yolo_min_area": 12000,
        "yolo_max_results": 5,
        "tracking_speed": 65,
        "movement_sensitivity": 50,
        "smoothing_factor": 0.50,
        "deadzone": 20,
        "snap_threshold": 130,
        "aim_aggression": 55,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / Hybrid: Frame Diff + YOLO / Person / Motion Gate Strict": {
        "detection_mode": "Hybrid: Frame Diff + YOLO",
        "motion_gate_threshold": 1.15,
        "threshold": 24,
        "blur_kernel": 3,
        "dilate_iter": 1,
        "min_contour": 60000,
        "max_contour": 450000,
        "yolo_classes": "person",
        "yolo_model": "yolov8m.pt",
        "yolo_confidence": 0.50,
        "yolo_min_area": 40000,
        "yolo_max_results": 5,
        "tracking_speed": 70,
        "movement_sensitivity": 55,
        "smoothing_factor": 0.45,
        "deadzone": 16,
        "snap_threshold": 150,
        "aim_aggression": 60,
        "final_approach_boost": True,
        "precision_mode": True,
        "precision_roi": 64,
        "precision_kp": 0.018,
        "precision_ki": 0.001,
        "precision_kd": 0.006,
        "precision_hfov": 90.0,
        "precision_max_step": 0.9,
        "precision_frac_threshold": 0.25,
    },

    # ----------------------------------------------------------------------
    # Target / Hybrid: BackSub + YOLO (Best) (Mode 5)
    # ----------------------------------------------------------------------

    "Target / Hybrid: BackSub + YOLO (Best) / Small / Overlap Lenient": {
        "detection_mode": "Hybrid: BackSub + YOLO (Best)",
        "overlap_threshold": 22.0,
        "threshold": 28,
        "blur_kernel": 5,
        "dilate_iter": 1,
        "min_contour": 900,
        "max_contour": 25000,
        "backsub_warmup": 25,
        "yolo_classes": "person",
        "yolo_model": "yolov8s.pt",
        "yolo_confidence": 0.35,
        "yolo_min_area": 5000,
        "yolo_max_results": 5,
        "tracking_speed": 60,
        "movement_sensitivity": 45,
        "smoothing_factor": 0.55,
        "deadzone": 22,
        "snap_threshold": 120,
        "aim_aggression": 50,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / Hybrid: BackSub + YOLO (Best) / Small / Overlap Balanced": {
        "detection_mode": "Hybrid: BackSub + YOLO (Best)",
        "overlap_threshold": 26.0,
        "threshold": 28,
        "blur_kernel": 5,
        "dilate_iter": 1,
        "min_contour": 900,
        "max_contour": 25000,
        "backsub_warmup": 30,
        "yolo_classes": "person",
        "yolo_model": "yolov8s.pt",
        "yolo_confidence": 0.40,
        "yolo_min_area": 7000,
        "yolo_max_results": 5,
        "tracking_speed": 60,
        "movement_sensitivity": 45,
        "smoothing_factor": 0.55,
        "deadzone": 22,
        "snap_threshold": 120,
        "aim_aggression": 50,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / Hybrid: BackSub + YOLO (Best) / Medium / Overlap Balanced": {
        "detection_mode": "Hybrid: BackSub + YOLO (Best)",
        "overlap_threshold": 28.0,
        "threshold": 26,
        "blur_kernel": 5,
        "dilate_iter": 1,
        "min_contour": 8000,
        "max_contour": 140000,
        "backsub_warmup": 30,
        "yolo_classes": "person",
        "yolo_model": "yolov8m.pt",
        "yolo_confidence": 0.45,
        "yolo_min_area": 15000,
        "yolo_max_results": 5,
        "tracking_speed": 65,
        "movement_sensitivity": 50,
        "smoothing_factor": 0.50,
        "deadzone": 20,
        "snap_threshold": 130,
        "aim_aggression": 55,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / Hybrid: BackSub + YOLO (Best) / Medium / Overlap Lenient": {
        "detection_mode": "Hybrid: BackSub + YOLO (Best)",
        "overlap_threshold": 24.0,
        "threshold": 26,
        "blur_kernel": 5,
        "dilate_iter": 1,
        "min_contour": 8000,
        "max_contour": 160000,
        "backsub_warmup": 35,
        "yolo_classes": "person",
        "yolo_model": "yolov8m.pt",
        "yolo_confidence": 0.40,
        "yolo_min_area": 12000,
        "yolo_max_results": 5,
        "tracking_speed": 65,
        "movement_sensitivity": 50,
        "smoothing_factor": 0.50,
        "deadzone": 20,
        "snap_threshold": 130,
        "aim_aggression": 55,
        "final_approach_boost": True,
        **PRECISION_DEFAULTS,
    },

    "Target / Hybrid: BackSub + YOLO (Best) / Person / Overlap Strict": {
        "detection_mode": "Hybrid: BackSub + YOLO (Best)",
        "overlap_threshold": 32.0,
        "threshold": 24,
        "blur_kernel": 3,
        "dilate_iter": 1,
        "min_contour": 60000,
        "max_contour": 450000,
        "backsub_warmup": 35,
        "yolo_classes": "person",
        "yolo_model": "yolov8m.pt",
        "yolo_confidence": 0.50,
        "yolo_min_area": 40000,
        "yolo_max_results": 5,
        "tracking_speed": 70,
        "movement_sensitivity": 55,
        "smoothing_factor": 0.45,
        "deadzone": 16,
        "snap_threshold": 150,
        "aim_aggression": 60,
        "final_approach_boost": True,
        "precision_mode": True,
        "precision_roi": 64,
        "precision_kp": 0.018,
        "precision_ki": 0.001,
        "precision_kd": 0.006,
        "precision_hfov": 90.0,
        "precision_max_step": 0.9,
        "precision_frac_threshold": 0.25,
    },
}


def _apply_speed_profiles() -> None:
    """Inject speed optimization settings into presets based on preset type."""
    for name, preset in PRESETS.items():
        if not isinstance(preset, dict):
            continue

        # Decide profile by name
        profile = SPEED_MOTION_BALANCED

        name_l = name.lower()
        if name_l.startswith("behavior / smooth"):
            profile = SPEED_BEHAVIOR_SMOOTH
        elif name_l.startswith("behavior / responsive"):
            profile = SPEED_BEHAVIOR_RESPONSIVE
        elif name_l.startswith("behavior / aggressive"):
            profile = SPEED_BEHAVIOR_AGGRESSIVE
        elif "yolo" in name_l:
            profile = SPEED_YOLO_FAST
        elif "color" in name_l:
            profile = SPEED_MOTION_BALANCED
        elif "frame difference" in name_l or "background subtraction" in name_l:
            profile = SPEED_MOTION_BALANCED

        # Apply defaults without overwriting explicit values
        for k, v in profile.items():
            preset.setdefault(k, v)


def _apply_target_aggressive_baseline() -> None:
    """Propagate aggressive-centering tuning to all Target/* factory presets."""
    for name, preset in PRESETS.items():
        if not isinstance(preset, dict):
            continue
        if not str(name).startswith("Target /"):
            continue

        try:
            # Core centering responsiveness
            preset["final_approach_boost"] = True
            preset["aim_aggression"] = max(90, int(preset.get("aim_aggression", 90)))
            preset["smoothing_factor"] = min(0.22, float(preset.get("smoothing_factor", 0.22)))
            preset["deadzone"] = min(10, int(preset.get("deadzone", 10)))

            # Convergence behavior
            preset["detection_pause_ms"] = 300
            preset["speed_profile_mode"] = "Aggressive"

            # Fire gating responsiveness
            preset["motion_fire_frames_required"] = 1
            preset["fire_stability_frames_required"] = 1

            # Precision mode: keep disabled for fastest lock-in unless explicitly re-enabled later
            preset["precision_mode"] = False
            preset["precision_max_step"] = max(1.8, float(preset.get("precision_max_step", 1.8)))
        except Exception:
            continue


# Apply speed profiles on import
_apply_speed_profiles()
_apply_target_aggressive_baseline()

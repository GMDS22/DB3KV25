from __future__ import annotations

PRESETS = {
    "Precision": {
        "aim_gain": 0.65,
        "max_step_deg": 1.5,
        "detect_interval": 6,
        "lost_max": 18,
        "lead_time_ms": 180,
        "settle_speed_px": 10.0,
        "strike_cooldown_ms": 180,
        "bus_time_ms": 180,
        "pixels_per_degree_x": 9.0,
        "pixels_per_degree_y": 9.0,
    },
    "Balanced": {
        "aim_gain": 0.85,
        "max_step_deg": 2.5,
        "detect_interval": 4,
        "lost_max": 12,
        "lead_time_ms": 140,
        "settle_speed_px": 16.0,
        "strike_cooldown_ms": 140,
        "bus_time_ms": 140,
        "pixels_per_degree_x": 8.0,
        "pixels_per_degree_y": 8.0,
    },
    "Fast": {
        "aim_gain": 1.05,
        "max_step_deg": 3.5,
        "detect_interval": 3,
        "lost_max": 10,
        "lead_time_ms": 100,
        "settle_speed_px": 22.0,
        "strike_cooldown_ms": 120,
        "bus_time_ms": 110,
        "pixels_per_degree_x": 7.0,
        "pixels_per_degree_y": 7.0,
    },
}

SERIAL_DEFAULTS = {
    "nano_port": "COM8",
    "bus_port": "COM9",
    "nano_baud": 115200,
    "bus_baud": 115200,
    "mode": "dual",
}

BUS_SERVO_CONFIG = {
    "pan_id": 1,
    "tilt_id": 2,
    "ticks_max": 1000,
    "deg_max": 270.0,
    "goal_addr": 0x2A,
    "time_scale": 1,
    "invert_pan": False,
    "invert_tilt": False,
    "pan_min": 0.0,
    "pan_max": 220.0,
    "tilt_min": 0.0,
    "tilt_max": 70.0,
}

AIM_DEFAULTS = {
    "pan_center": 110.0,
    "tilt_center": 80.0,
    "manual_step_deg": 3.0,
}

TRACKING_DEFAULTS = {
    "yolo_model": "yolov8n.pt",
    "yolo_conf": 0.45,
    "tracker_type": "CSRT",
    "detector": "blob",
    "blob_min_area": 800,
    "blob_max_area_ratio": 0.4,
}

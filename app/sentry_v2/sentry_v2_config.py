"""
Smart Sentry v2 — Configuration

All tuneable parameters for the smart sentry system.
Designed as a dataclass for easy serialization / UI binding.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple


SENTRY_PAN_MIN = 0.0
SENTRY_PAN_MAX = 270.0
SENTRY_TILT_MIN = 0.0
SENTRY_TILT_MAX = 110.0
SENTRY_HOME_PAN = (SENTRY_PAN_MIN + SENTRY_PAN_MAX) / 2.0
SENTRY_HOME_TILT = (SENTRY_TILT_MIN + SENTRY_TILT_MAX) / 2.0
SENTRY_SWEEP_PAN_MIN = SENTRY_PAN_MIN
SENTRY_SWEEP_PAN_MAX = SENTRY_PAN_MAX
SENTRY_RANDOM_PAN_MIN = SENTRY_PAN_MIN
SENTRY_RANDOM_PAN_MAX = SENTRY_PAN_MAX
SENTRY_RANDOM_TILT_MIN = SENTRY_TILT_MIN
SENTRY_RANDOM_TILT_MAX = SENTRY_TILT_MAX


# Full COCO class list (80 classes) — same order as YOLOv8 default
YOLO_COCO_CLASSES: List[str] = [
    "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train",
    "truck", "boat", "traffic light", "fire hydrant", "stop sign",
    "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep",
    "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
    "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard",
    "sports ball", "kite", "baseball bat", "baseball glove", "skateboard",
    "surfboard", "tennis racket", "bottle", "wine glass", "cup", "fork",
    "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange",
    "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair",
    "couch", "potted plant", "bed", "dining table", "toilet", "tv",
    "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave",
    "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase",
    "scissors", "teddy bear", "hair drier", "toothbrush",
]


@dataclass
class DetectionModeConfig:
    """Detection method settings — mirrors main app detection modes."""
    # Detection mode index (same as main app):
    # 0=Frame Difference, 1=Background Subtraction, 2=YOLO Object Detection,
    # 3=Hybrid: Frame Diff+BackSub, 4=Hybrid: Frame Diff+YOLO,
    # 5=Hybrid: BackSub+YOLO (Best), 6=Color Detection,
    # 7=Hybrid: Color+Frame Diff, 8=Hybrid: Color+BackSub,
    # 9=Hybrid: Color+YOLO, 10=Filtered Target Mode
    detection_mode: int = 10
    # --- Contour filtering (modes 0,1,3,7,8) ---
    min_contour_area: float = 250.0
    max_contour_area: float = 250000.0
    # --- YOLO-specific (modes 2,4,5,9,10) ---
    yolo_model_name: str = "ratdogcat_last.pt"
    yolo_min_area: int = 0
    yolo_confidence: float = 0.45
    # --- Color detection (modes 6,7,8,9) ---
    color_preset: str = "any"
    color_min_area: int = 120
    color_max_area: int = 250000
    color_fusion_strategy: str = "AND"
    color_fusion_overlap: int = 15
    # Custom HSV (used when color_preset == "custom")
    custom_h_min: int = 0
    custom_s_min: int = 100
    custom_v_min: int = 100
    custom_h_max: int = 179
    custom_s_max: int = 255
    custom_v_max: int = 255
    # Ignore motion detections briefly after turret movement so the camera
    # does not engage its own scene shift.
    motion_ignore_after_move_s: float = 0.08
    # --- Motion gate threshold % (modes 4,5) ---
    motion_gate_threshold: float = 1.0


@dataclass
class TargetFilterConfig:
    """Criteria for which detections qualify as engageable targets."""
    # YOLO class whitelist (empty = allow all)
    allowed_classes: List[str] = field(default_factory=list)
    # Per-class priority (higher = engage first). Missing classes default to 1.0.
    class_priority: Dict[str, float] = field(default_factory=lambda: {
        "person": 5.0,
        "car": 3.0,
        "dog": 2.0,
        "cat": 2.0,
        "rat": 2.2,
    })
    # Minimum YOLO confidence to consider
    min_confidence: float = 0.45
    # Minimum bounding-box area (fraction of frame area, 0-1)
    min_size_ratio: float = 0.0025
    # Maximum bounding-box area (fraction of frame area, 0-1, 0=no limit)
    max_size_ratio: float = 0.18
    # Optional bbox aspect-ratio safety gate for class-specific targets.
    shape_filter_enabled: bool = False
    shape_profile_name: str = ""
    # Minimum consecutive tracked frames required before a semantic class is accepted.
    semantic_min_confirm_frames: int = 1
    # Minimum confidence required for a frame to count toward semantic confirmation.
    semantic_min_confirm_confidence: float = 0.0
    # Reset semantic confirmation if a track disappears longer than this.
    semantic_confirm_ttl_s: float = 0.8
    # Engagement zone: normalised rectangle [x1, y1, x2, y2]
    # (0,0)=top-left  (1,1)=bottom-right — only targets inside are engaged
    engagement_zone: Tuple[float, float, float, float] = (0.0, 0.0, 1.0, 1.0)


@dataclass
class ThreatScoringConfig:
    """Weights for the threat scoring formula."""
    # Weight: proximity to frame center (closer = higher threat)
    w_proximity: float = 0.25
    # Weight: object size (larger = higher threat)
    w_size: float = 0.15
    # Weight: YOLO confidence
    w_confidence: float = 0.10
    # Weight: class priority from TargetFilterConfig
    w_class_priority: float = 0.20
    # Weight: speed of movement (faster = higher threat)
    w_speed: float = 0.10
    # Weight: time-in-frame / persistence (longer = higher threat)
    w_persistence: float = 0.10
    # Weight: heading toward guard point (approaching = higher threat)
    w_approach: float = 0.10
    # Enable ML-based scoring refinement (requires sklearn)
    use_ml_model: bool = False
    # Path to saved ML model (pickle)
    ml_model_path: str = "config/sentry_v2_threat_model.pkl"


@dataclass
class EngagementConfig:
    """How the turret engages targets."""
    # Minimum threat score (0-1) to engage
    min_threat_score: float = 0.30
    # Burst count per target engagement
    burst_count: int = 3
    # Milliseconds between burst shots
    burst_interval_ms: int = 50
    # Seconds to wait after engaging one target before the next
    inter_target_cooldown: float = 0.8
    # Seconds to wait after full engagement cycle before re-scanning
    cycle_cooldown: float = 2.0
    # Maximum simultaneous engagement queue length
    max_queue_length: int = 1
    # Use minimum-slew ordering (nearest-neighbor) for multi-target
    optimize_slew_order: bool = False
    # Force Smart Sentry to work one target at a time.
    single_target_only: bool = True
    # Seconds before turret returns to guard position after last engagement
    return_delay: float = 1.5
    # Servo speed multiplier for engagement snap-aim (1-100)
    engagement_speed: int = 80
    # --- Auto-trigger ---
    auto_trigger_enabled: bool = False
    # --- Trigger mode (False = Water/MOSFET, True = Projectile/BB Servo) ---
    trigger_mode_bb: bool = False
    # --- Precision aiming for small / distant targets ---
    precision_aim_enabled: bool = True
    # Seconds to allow PID refinement after initial snap-aim
    precision_settle_time: float = 0.4
    # PID gains for precision refinement
    precision_kp: float = 0.035
    precision_ki: float = 0.0
    precision_kd: float = 0.01
    # Max correction step per frame (degrees)
    precision_max_step: float = 0.85
    precision_deadzone_pan_deg: float = 0.18
    precision_deadzone_tilt_deg: float = 0.15
    precision_error_ema: float = 0.40
    precision_max_pan_step: float = 0.90
    precision_max_tilt_step: float = 0.75
    precision_reversal_brake: float = 0.30
    fire_micro_adjust_enabled: bool = True
    fire_micro_adjust_max_pan_step: float = 0.25
    fire_micro_adjust_max_tilt_step: float = 0.20
    fire_recenter_pan_tolerance: float = 0.85
    fire_recenter_tilt_tolerance: float = 0.70
    fire_trigger_enter_pan_tolerance: float = 0.35
    fire_trigger_enter_tilt_tolerance: float = 0.28
    fire_trigger_exit_pan_tolerance: float = 0.55
    fire_trigger_exit_tilt_tolerance: float = 0.42
    fire_trigger_max_pan_rate: float = 2.0
    fire_trigger_max_tilt_rate: float = 1.7
    fire_trigger_hold_time: float = 0.10
    fire_trigger_refractory_time: float = 0.20
    fire_trigger_min_confidence: float = 0.45
    fire_trigger_min_persistence: float = 0.12
    # Auto-fire requires a stable aim lock in precision mode.
    fire_requires_lock: bool = True
    aim_lock_pan_tolerance: float = 0.65
    aim_lock_tilt_tolerance: float = 0.55
    aim_lock_required_frames: int = 5
    aim_lock_timeout: float = 1.3
    target_loss_timeout: float = 0.55
    # Keep engaging/holding last known target area when target is temporarily lost
    # instead of advancing queue and returning to guard.
    continuous_hunt_on_loss: bool = False


@dataclass
class GuardConfig:
    """Guard position and behaviour."""
    # Guard position — where turret rests (degrees)
    guard_pan: float = SENTRY_HOME_PAN
    guard_tilt: float = SENTRY_HOME_TILT
    pan_min: float = SENTRY_PAN_MIN
    pan_max: float = SENTRY_PAN_MAX
    tilt_min: float = SENTRY_TILT_MIN
    tilt_max: float = SENTRY_TILT_MAX
    # Horizontal field-of-view of camera (degrees) — used for px→° conversion
    camera_hfov: float = 78.0
    # Vertical field-of-view (degrees)
    camera_vfov: float = 44.0
    pan_center_bias_deg: float = 0.0
    tilt_center_bias_deg: float = 0.0
    # Frame dimensions (set at runtime)
    frame_width: int = 1280
    frame_height: int = 720
    # --- Guard patrol modes ---
    # 0=Static, 1=Slow Sweep, 2=Waypoint Patrol, 3=Random Scan
    guard_mode: int = 0
    # Sweep settings (mode 1)
    sweep_pan_min: float = SENTRY_SWEEP_PAN_MIN
    sweep_pan_max: float = SENTRY_SWEEP_PAN_MAX
    sweep_tilt: float = SENTRY_HOME_TILT
    sweep_speed: float = 8.0        # degrees per second (slow & smooth)
    # Waypoint patrol settings (mode 2)
    patrol_waypoints: List[Tuple[float, float]] = field(default_factory=list)
    patrol_dwell: float = 2.0       # seconds to pause at each waypoint
    patrol_speed: float = 10.0      # degrees per second between waypoints
    # Random scan settings (mode 3)
    random_pan_min: float = SENTRY_RANDOM_PAN_MIN
    random_pan_max: float = SENTRY_RANDOM_PAN_MAX
    random_tilt_min: float = SENTRY_RANDOM_TILT_MIN
    random_tilt_max: float = SENTRY_RANDOM_TILT_MAX
    random_dwell: float = 3.0       # seconds to pause at each random point
    random_speed: float = 8.0       # degrees per second


@dataclass
class NoFireMaskVertex:
    pan: float
    tilt: float


@dataclass
class NoFireMaskConfig:
    id: str = ""
    name: str = "No-Fire Mask"
    enabled: bool = True
    visible: bool = True
    vertices: List[NoFireMaskVertex] = field(default_factory=list)
    source_frame_width: int = 0
    source_frame_height: int = 0
    source_hfov: float = 0.0
    source_vfov: float = 0.0
    anchor_pan: float = 0.0
    anchor_tilt: float = 0.0
    notes: str = ""


@dataclass
class PIRSensorConfig:
    """Individual PIR sensor settings."""
    # GPIO index or identifier on ESP32
    pin_id: int = 0
    # Pan angle in degrees (0-270) to look when this sensor triggers
    cue_pan: float = 0.0
    # Tilt angle in degrees (0-110) to look when this sensor triggers
    cue_tilt: float = 55.0
    # Debounce time in milliseconds to avoid repeated triggers
    debounce_ms: int = 500
    # Enable/disable this particular sensor
    enabled: bool = False


@dataclass
class PIRGuardConfig:
    """PIR sensor integration for blind-spot detection."""
    # Master enable/disable for all PIR features
    pir_enabled: bool = False
    # Number of PIR sensors (typically 3)
    pir_count: int = 3
    # Individual sensor configs
    # Equal 90° spacing across the full 0–270° pan arc:
    #   S0 (GPIO35) covers right zone  0°– 90°  → cue_pan= 45°
    #   S1 (GPIO34) covers front zone  90°–180° → cue_pan=135°
    #   S2 (GPIO39) covers left zone  180°–270° → cue_pan=225°
    sensors: List[PIRSensorConfig] = field(default_factory=lambda: [
        PIRSensorConfig(pin_id=0, cue_pan=45.0,  cue_tilt=35.0, enabled=False),
        PIRSensorConfig(pin_id=1, cue_pan=135.0, cue_tilt=35.0, enabled=False),
        PIRSensorConfig(pin_id=2, cue_pan=225.0, cue_tilt=35.0, enabled=False),
    ])
    # Enable adaptive scan when PIR fires but camera doesn't detect
    scan_on_no_detect: bool = True
    # Pan sweep range (degrees left/right from cue point)
    # 45° covers the full 90° zone for each sensor (±45° from center)
    scan_pan_range: float = 45.0
    # Tilt sweep range (degrees up/down from cue point)
    scan_tilt_range: float = 15.0
    # Scan movement speed (degrees per second)
    scan_speed: float = 12.0
    # Time to wait for camera detection after initial slew (seconds)
    confirmation_timeout: float = 1.2
    # Number of points in scan grid per axis (3x3 = 9 points)
    scan_grid_resolution: int = 3
    # Data timeout: discard PIR data older than this (milliseconds)
    data_timeout_ms: int = 5000


@dataclass
class ConnectionConfig:
    """Connection settings for Smart Sentry v2.

    Modes:
        0  ESP32 USB only               (single COM)
        1  ESP32 USB + Debug Board USB  (2 COM ports)
        2  ESP32 WiFi + Debug Board USB (1 COM + UDP)
        3  ESP32 WiFi (fully wireless)  (UDP only)
    """
    connection_type: int = 3
    # ESP32 serial (modes 0, 1)
    esp32_port: str = ""
    esp32_baud: int = 115200
    # Debug board serial (modes 1, 2)
    debug_port: str = ""
    debug_baud: int = 115200
    # WiFi UDP (modes 2, 3)
    udp_host: str = "192.168.4.1"
    udp_port: int = 9000
    # Servo config
    pan_servo_id: int = 1
    tilt_servo_id: int = 2
    bus_servo_time_ms: int = 55
    # Inversion
    invert_pan: bool = False
    invert_tilt: bool = False
    # Camera
    camera_source: str = "0"       # Standalone default camera index; may also be a URL or file path
    camera_width: int = 1280
    camera_height: int = 720
    webcam_zoom_pct: int = 100
    test_source_zoom_pct: int = 100


@dataclass
class SentryV2Config:
    """Top-level configuration for Smart Sentry v2."""
    connection: ConnectionConfig = field(default_factory=ConnectionConfig)
    detection_mode: DetectionModeConfig = field(default_factory=DetectionModeConfig)
    target_filter: TargetFilterConfig = field(default_factory=TargetFilterConfig)
    threat_scoring: ThreatScoringConfig = field(default_factory=ThreatScoringConfig)
    engagement: EngagementConfig = field(default_factory=EngagementConfig)
    guard: GuardConfig = field(default_factory=GuardConfig)
    no_fire_masks: List[NoFireMaskConfig] = field(default_factory=list)
    pir_guard: PIRGuardConfig = field(default_factory=PIRGuardConfig)

    # --- Overlay / HUD ---
    show_overlay: bool = True
    show_threat_scores: bool = False
    show_engagement_zone: bool = False
    show_guard_crosshair: bool = True
    show_no_fire_masks: bool = True
    scope_view_enabled: bool = False
    scope_radius_pct: int = 35
    scope_vignette_opacity: int = 60
    settings_panel_width: int = 420
    prompted_targets_enabled: bool = False
    prompted_allow_auto_fire: bool = False
    prompted_library_path: str = "app/config/sentry_v2_prompted_targets.json"

    # --- Persistence ---
    config_path: str = "app/config/sentry_v2_settings.json"

    # ------------------------------------------------------------------ #
    # Serialization helpers
    # ------------------------------------------------------------------ #
    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def _sanitize_guard_config(guard: GuardConfig) -> GuardConfig:
        pan_min = float(min(SENTRY_PAN_MAX, max(SENTRY_PAN_MIN, guard.pan_min)))
        pan_max = float(min(SENTRY_PAN_MAX, max(SENTRY_PAN_MIN, guard.pan_max)))
        tilt_min = float(min(SENTRY_TILT_MAX, max(SENTRY_TILT_MIN, guard.tilt_min)))
        tilt_max = float(min(SENTRY_TILT_MAX, max(SENTRY_TILT_MIN, guard.tilt_max)))
        if pan_min > pan_max:
            pan_min, pan_max = pan_max, pan_min
        if tilt_min > tilt_max:
            tilt_min, tilt_max = tilt_max, tilt_min
        if pan_min == pan_max:
            pan_min, pan_max = SENTRY_PAN_MIN, SENTRY_PAN_MAX
        if tilt_min == tilt_max:
            tilt_min, tilt_max = SENTRY_TILT_MIN, SENTRY_TILT_MAX

        guard.pan_min = pan_min
        guard.pan_max = pan_max
        guard.tilt_min = tilt_min
        guard.tilt_max = tilt_max
        guard.guard_pan = float(min(pan_max, max(pan_min, guard.guard_pan)))
        guard.guard_tilt = float(min(tilt_max, max(tilt_min, guard.guard_tilt)))
        guard.sweep_pan_min = float(min(pan_max, max(pan_min, guard.sweep_pan_min)))
        guard.sweep_pan_max = float(min(pan_max, max(pan_min, guard.sweep_pan_max)))
        if guard.sweep_pan_min > guard.sweep_pan_max:
            guard.sweep_pan_min, guard.sweep_pan_max = guard.sweep_pan_max, guard.sweep_pan_min
        guard.sweep_tilt = float(min(tilt_max, max(tilt_min, guard.sweep_tilt)))
        guard.random_pan_min = float(min(pan_max, max(pan_min, guard.random_pan_min)))
        guard.random_pan_max = float(min(pan_max, max(pan_min, guard.random_pan_max)))
        if guard.random_pan_min > guard.random_pan_max:
            guard.random_pan_min, guard.random_pan_max = guard.random_pan_max, guard.random_pan_min
        guard.random_tilt_min = float(min(tilt_max, max(tilt_min, guard.random_tilt_min)))
        guard.random_tilt_max = float(min(tilt_max, max(tilt_min, guard.random_tilt_max)))
        if guard.random_tilt_min > guard.random_tilt_max:
            guard.random_tilt_min, guard.random_tilt_max = guard.random_tilt_max, guard.random_tilt_min
        return guard

    @classmethod
    def from_dict(cls, d: dict) -> "SentryV2Config":
        cn = ConnectionConfig(**d.get("connection", {}))
        if not str(cn.camera_source).strip():
            cn.camera_source = "0"
        dm = DetectionModeConfig(**d.get("detection_mode", {}))
        tf = TargetFilterConfig(**d.get("target_filter", {}))
        ts = ThreatScoringConfig(**d.get("threat_scoring", {}))
        eg = EngagementConfig(**d.get("engagement", {}))
        gd_raw = dict(d.get("guard", {}))
        # JSON stores tuples as lists — convert patrol_waypoints back
        if "patrol_waypoints" in gd_raw:
            gd_raw["patrol_waypoints"] = [
                (float(p[0]), float(p[1])) for p in gd_raw["patrol_waypoints"]
            ]
        gd = GuardConfig(**gd_raw)
        gd = cls._sanitize_guard_config(gd)
        masks_raw = list(d.get("no_fire_masks", []))
        masks: List[NoFireMaskConfig] = []
        for entry in masks_raw:
            mask_data = dict(entry or {})
            vertices_raw = list(mask_data.pop("vertices", []))
            vertices = [
                NoFireMaskVertex(
                    pan=float(v.get("pan", 0.0)),
                    tilt=float(v.get("tilt", 0.0)),
                )
                for v in vertices_raw
                if isinstance(v, dict)
            ]
            masks.append(NoFireMaskConfig(vertices=vertices, **mask_data))
        
        # Load PIR guard config
        pir_raw = dict(d.get("pir_guard", {}))
        sensors_raw = list(pir_raw.pop("sensors", []))
        sensors: List[PIRSensorConfig] = []
        for sensor_data in sensors_raw:
            if isinstance(sensor_data, dict):
                sensors.append(PIRSensorConfig(**sensor_data))
        pir_cfg = PIRGuardConfig(sensors=sensors, **pir_raw)
        
        return cls(
            connection=cn,
            detection_mode=dm,
            target_filter=tf,
            threat_scoring=ts,
            engagement=eg,
            guard=gd,
            no_fire_masks=masks,
            pir_guard=pir_cfg,
            show_overlay=d.get("show_overlay", True),
            show_threat_scores=d.get("show_threat_scores", False),
            show_engagement_zone=d.get("show_engagement_zone", False),
            show_guard_crosshair=d.get("show_guard_crosshair", True),
            show_no_fire_masks=d.get("show_no_fire_masks", True),
            scope_view_enabled=d.get("scope_view_enabled", False),
            scope_radius_pct=d.get("scope_radius_pct", 35),
            scope_vignette_opacity=d.get("scope_vignette_opacity", 60),
            settings_panel_width=d.get("settings_panel_width", 420),
            prompted_targets_enabled=d.get("prompted_targets_enabled", False),
            prompted_allow_auto_fire=d.get("prompted_allow_auto_fire", False),
            prompted_library_path=d.get("prompted_library_path", "app/config/sentry_v2_prompted_targets.json"),
            config_path=d.get("config_path", "app/config/sentry_v2_settings.json"),
        )

    def save(self, path: Optional[str] = None) -> None:
        p = Path(path or self.config_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(self.to_dict(), indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: str) -> "SentryV2Config":
        p = Path(path)
        if p.exists():
            return cls.from_dict(json.loads(p.read_text(encoding="utf-8")))
        return cls()

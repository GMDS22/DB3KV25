"""
SMART SENTRY V3 — Configuration

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
CANONICAL_FACE_LIBRARY_PATH = "app/config/smart_sentry_faces.json"
CANONICAL_PROMPTED_TARGETS_PATH = "app/config/smart_sentry_prompted_targets.json"
CANONICAL_SETTINGS_PATH = "app/config/smart_sentry_settings.json"

# Older shipped auto-trigger profiles used sub-2 degree gates that do not
# converge reliably enough for live firing.
AUTO_TRIGGER_MIN_AIM_LOCK_PAN_DEG = 2.0
AUTO_TRIGGER_MIN_AIM_LOCK_TILT_DEG = 2.0
AUTO_TRIGGER_MIN_FIRE_ENTER_PAN_DEG = 2.0
AUTO_TRIGGER_MIN_FIRE_ENTER_TILT_DEG = 2.0
AUTO_TRIGGER_MIN_FIRE_EXIT_PAN_DEG = 2.8
AUTO_TRIGGER_MIN_FIRE_EXIT_TILT_DEG = 2.4
AUTO_TRIGGER_MIN_PRECISION_DEADZONE_PAN_DEG = 0.18
AUTO_TRIGGER_MIN_PRECISION_DEADZONE_TILT_DEG = 0.16
AUTO_TRIGGER_MIN_FIRE_MICRO_ADJUST_PAN_STEP_DEG = 0.32
AUTO_TRIGGER_MIN_FIRE_MICRO_ADJUST_TILT_STEP_DEG = 0.25
AUTO_TRIGGER_MIN_TARGET_LOSS_TIMEOUT_S = 1.4
AUTO_TRIGGER_MAX_AIM_LOCK_REQUIRED_FRAMES = 4
AUTO_TRIGGER_MAX_AIM_LOCK_TIMEOUT_S = 2.0
NANO_USB_HOST_BAUD = 115200
NANO_USB_CONNECTION_TYPES = {0, 1}


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
    yolo_model_dir: str = ""
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
    ml_model_path: str = "config/smart_sentry_v3_threat_model.pkl"


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
    # Water/MOSFET trigger tuning pushed to the IO firmware at runtime.
    trigger_mosfet_pulse_ms: int = 120
    trigger_mosfet_cycle_count: int = 1
    trigger_mosfet_cycle_off_ms: int = 50
    # Projectile trigger-servo tuning pushed to the ESP32 at runtime.
    trigger_servo_rest_deg: int = 0
    trigger_servo_fire_deg: int = 45
    trigger_servo_speed_dps: int = 360
    # --- Precision aiming for small / distant targets ---
    precision_aim_enabled: bool = True
    # Seconds to allow PID refinement after initial snap-aim
    precision_settle_time: float = 0.4
    # PID gains for precision refinement
    precision_kp: float = 0.035
    precision_ki: float = 0.0
    precision_kd: float = 0.015
    # Max correction step per frame (degrees)
    precision_max_step: float = 0.85
    precision_deadzone_pan_deg: float = 0.4
    precision_deadzone_tilt_deg: float = 0.35
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
    # Simple fire gate: fire when aim error (degrees from center) is within this value.
    # Set this and precision_settle_time — no other settings required for auto-fire.
    # 0 = use legacy aim_lock / precision_deadzone system instead.
    fire_center_tolerance_deg: float = 3.5
    # Auto-fire requires a stable aim lock in precision mode.
    fire_requires_lock: bool = True
    aim_lock_pan_tolerance: float = 0.65
    aim_lock_tilt_tolerance: float = 0.55
    aim_lock_required_frames: int = 3
    aim_lock_timeout: float = 1.3
    target_loss_timeout: float = 0.55
    # Keep engaging/holding last known target area when target is temporarily lost
    # instead of advancing queue and returning to guard.
    continuous_hunt_on_loss: bool = False
    # Finite multi-stage loss recovery that runs before queue advance / return.
    loss_recovery_enabled: bool = True
    # Predict motion from recent track history to lead fast targets.
    predictive_aim_enabled: bool = True
    predictive_lead_time_s: float = 0.16
    predictive_fire_extra_lead_s: float = 0.05
    predictive_max_lead_pan_deg: float = 3.5
    predictive_max_lead_tilt_deg: float = 2.2
    predictive_min_persistence_s: float = 0.18
    # If a target drops out, first continue into its last direction, then
    # search locally around the loss point before giving up.
    loss_direction_pursuit_enabled: bool = True
    loss_direction_pursuit_s: float = 0.28
    loss_local_search_enabled: bool = True
    loss_local_search_pan_deg: float = 6.0
    loss_local_search_tilt_deg: float = 4.0
    loss_expanding_search_enabled: bool = True
    loss_expanding_search_rings: int = 2
    loss_expanding_search_pan_step_deg: float = 3.0
    loss_expanding_search_tilt_step_deg: float = 1.5
    loss_search_step_interval_s: float = 0.25
    # Adaptive after-loss search protocols.
    adaptive_loss_recovery_enabled: bool = True
    loss_recovery_protocol_new_target: str = "rapid_handoff_search"
    loss_recovery_protocol_no_detection: str = "persistent_reacquire_search"
    loss_handoff_pursuit_time_s: float = 0.14
    loss_handoff_backoff_pan_deg: float = 1.4
    loss_handoff_tilt_step_deg: float = 0.9
    loss_handoff_max_duration_s: float = 0.38
    loss_persistent_retry_passes_sparse: int = 2
    loss_persistent_retry_passes_crowded: int = 1
    loss_persistent_expand_scale: float = 1.18
    loss_switch_score_margin: float = 0.12
    loss_switch_persistence_bias: float = 0.05
    loss_scene_crowding_threshold: int = 3
    loss_personality_intensity: float = 0.35
    loss_personality_velocity_bias: float = 0.40
    loss_personality_order_variation: float = 0.30
    # Shared hunting style for both target-loss and PIR no-detect behavior.
    # "hunting" favors a careful local-area search, while
    # "fast_reacquire" trims dwell and broadens early coverage.
    loss_search_style: str = "hunting"
    # Shared hunt pass count for target-loss and PIR no-detect searches.
    loss_search_rounds: int = 1
    # Stationary-target release protocol: after repeated fire cycles on a
    # near-static target, temporarily suppress re-engaging that same track so
    # guard-mode PIR/acoustic workflows can run.
    stationary_release_enabled: bool = True
    stationary_release_min_fire_cycles: int = 3
    stationary_release_hold_s: float = 8.0
    stationary_release_suppress_s: float = 10.0
    stationary_release_motion_px: float = 36.0

    def __post_init__(self) -> None:
        normalize_auto_trigger_engagement(self)


def normalize_auto_trigger_engagement(engagement: "EngagementConfig") -> List[str]:
    """Clamp stale auto-trigger settings to values that can actually fire."""
    if not bool(getattr(engagement, "auto_trigger_enabled", False)):
        return []

    adjustments: List[str] = []

    def enforce_min(attr: str, minimum: float) -> None:
        current = float(getattr(engagement, attr, minimum))
        if current >= minimum:
            return
        setattr(engagement, attr, minimum)
        adjustments.append(f"{attr}={current:.2f}->{minimum:.2f}")

    def enforce_max(attr: str, maximum: float) -> None:
        current = float(getattr(engagement, attr, maximum))
        if current <= maximum:
            return
        setattr(engagement, attr, maximum)
        adjustments.append(f"{attr}={current:.2f}->{maximum:.2f}")

    enforce_min("aim_lock_pan_tolerance", AUTO_TRIGGER_MIN_AIM_LOCK_PAN_DEG)
    enforce_min("aim_lock_tilt_tolerance", AUTO_TRIGGER_MIN_AIM_LOCK_TILT_DEG)
    enforce_min("fire_trigger_enter_pan_tolerance", AUTO_TRIGGER_MIN_FIRE_ENTER_PAN_DEG)
    enforce_min("fire_trigger_enter_tilt_tolerance", AUTO_TRIGGER_MIN_FIRE_ENTER_TILT_DEG)
    enforce_min("fire_trigger_exit_pan_tolerance", AUTO_TRIGGER_MIN_FIRE_EXIT_PAN_DEG)
    enforce_min("fire_trigger_exit_tilt_tolerance", AUTO_TRIGGER_MIN_FIRE_EXIT_TILT_DEG)
    enforce_min("precision_deadzone_pan_deg", AUTO_TRIGGER_MIN_PRECISION_DEADZONE_PAN_DEG)
    enforce_min("precision_deadzone_tilt_deg", AUTO_TRIGGER_MIN_PRECISION_DEADZONE_TILT_DEG)
    enforce_min("fire_micro_adjust_max_pan_step", AUTO_TRIGGER_MIN_FIRE_MICRO_ADJUST_PAN_STEP_DEG)
    enforce_min("fire_micro_adjust_max_tilt_step", AUTO_TRIGGER_MIN_FIRE_MICRO_ADJUST_TILT_STEP_DEG)
    enforce_min("target_loss_timeout", AUTO_TRIGGER_MIN_TARGET_LOSS_TIMEOUT_S)
    enforce_max("aim_lock_required_frames", AUTO_TRIGGER_MAX_AIM_LOCK_REQUIRED_FRAMES)
    enforce_max("aim_lock_timeout", AUTO_TRIGGER_MAX_AIM_LOCK_TIMEOUT_S)

    enter_pan = float(getattr(engagement, "fire_trigger_enter_pan_tolerance", AUTO_TRIGGER_MIN_FIRE_ENTER_PAN_DEG))
    enter_tilt = float(getattr(engagement, "fire_trigger_enter_tilt_tolerance", AUTO_TRIGGER_MIN_FIRE_ENTER_TILT_DEG))
    exit_pan = float(getattr(engagement, "fire_trigger_exit_pan_tolerance", AUTO_TRIGGER_MIN_FIRE_EXIT_PAN_DEG))
    exit_tilt = float(getattr(engagement, "fire_trigger_exit_tilt_tolerance", AUTO_TRIGGER_MIN_FIRE_EXIT_TILT_DEG))

    if exit_pan < enter_pan:
        setattr(engagement, "fire_trigger_exit_pan_tolerance", enter_pan)
        adjustments.append(f"fire_trigger_exit_pan_tolerance={exit_pan:.2f}->{enter_pan:.2f}")
        exit_pan = enter_pan
    if exit_tilt < enter_tilt:
        setattr(engagement, "fire_trigger_exit_tilt_tolerance", enter_tilt)
        adjustments.append(f"fire_trigger_exit_tilt_tolerance={exit_tilt:.2f}->{enter_tilt:.2f}")
        exit_tilt = enter_tilt

    recenter_pan = float(getattr(engagement, "fire_recenter_pan_tolerance", exit_pan))
    recenter_tilt = float(getattr(engagement, "fire_recenter_tilt_tolerance", exit_tilt))
    if recenter_pan < exit_pan:
        setattr(engagement, "fire_recenter_pan_tolerance", exit_pan)
        adjustments.append(f"fire_recenter_pan_tolerance={recenter_pan:.2f}->{exit_pan:.2f}")
    if recenter_tilt < exit_tilt:
        setattr(engagement, "fire_recenter_tilt_tolerance", exit_tilt)
        adjustments.append(f"fire_recenter_tilt_tolerance={recenter_tilt:.2f}->{exit_tilt:.2f}")

    return adjustments


def normalize_target_filter_tracking(filter_cfg: "TargetFilterConfig") -> List[str]:
    """Clamp semantic confirmation gates so moving-camera reacquire remains possible."""
    adjustments: List[str] = []

    frames = int(getattr(filter_cfg, "semantic_min_confirm_frames", 1) or 1)
    if frames > 1:
        setattr(filter_cfg, "semantic_min_confirm_frames", 1)
        adjustments.append(f"semantic_min_confirm_frames={frames}->1")

    sem_conf = float(getattr(filter_cfg, "semantic_min_confirm_confidence", 0.0) or 0.0)
    conf_floor = float(getattr(filter_cfg, "min_confidence", 0.5) or 0.5)
    conf_cap = max(conf_floor, 0.52)
    if sem_conf > conf_cap:
        setattr(filter_cfg, "semantic_min_confirm_confidence", conf_cap)
        adjustments.append(f"semantic_min_confirm_confidence={sem_conf:.2f}->{conf_cap:.2f}")

    return adjustments


@dataclass
class GuardConfig:
    """Guard position and behaviour."""
    # Guard position — where turret rests (degrees)
    guard_pan: float = SENTRY_HOME_PAN
    guard_tilt: float = SENTRY_HOME_TILT
    rest_pan: float = SENTRY_HOME_PAN
    rest_tilt: float = SENTRY_HOME_TILT
    rest_on_startup_enabled: bool = True
    rest_on_close_enabled: bool = True
    rest_startup_delay_ms: int = 900
    rest_close_timeout_ms: int = 1600
    home_move_speed_dps: float = 24.0
    home_move_approach_speed_dps: float = 14.0
    rest_move_speed_dps: float = 14.0
    rest_move_approach_speed_dps: float = 10.0
    guided_move_approach_window_deg: float = 14.0
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
    # --- Sentry behaviour mode ---
    # 0=Watchful (tracks any mover, engages valid targets)
    # 1=Curious Guard (glances at movers, only engages valid targets)
    # 2=Strict (only moves/acts for fully-qualified valid targets)
    sentry_behaviour: int = 2
    # Curious Guard glance parameters
    curious_glance_interval_s: float = 7.0
    curious_glance_dwell_s: float = 1.3


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
    # Blink the ESP32 status LED / GPIO2 mirror when a PIR event is detected.
    pir_event_blink_enabled: bool = False
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
    # Short cue-center dwell before the local hunt begins.
    cue_hold_time_s: float = 0.18
    # Pan sweep range (degrees left/right from cue point)
    # 45° covers the full 90° zone for each sensor (±45° from center)
    scan_pan_range: float = 45.0
    # Tilt sweep range (degrees up/down from cue point)
    scan_tilt_range: float = 45.0
    # Scan movement speed (degrees per second)
    scan_speed: float = 12.0
    # Time to wait for camera detection after initial slew (seconds)
    confirmation_timeout: float = 1.2
    # Number of points in scan grid per axis (3x3 = 9 points)
    scan_grid_resolution: int = 3
    # Data timeout: discard PIR data older than this (milliseconds)
    data_timeout_ms: int = 5000
    # Ignore near-simultaneous events from different PIR sensors so one target
    # crossing overlapping sensor cones is treated as a single zone hit.
    cross_sensor_lockout_ms: int = 120
    # Shared hunting style for PIR no-detect search.
    search_style: str = "hunting"
    # Shared hunt pass count for target-loss and PIR no-detect searches.
    search_rounds: int = 1


@dataclass
class LightingConfig:
    """Automated LED brightness control settings."""
    auto_lighting_enabled: bool = False
    led_pwm_value: int = 255
    auto_brightness_threshold: int = 140
    auto_pwm_min: int = 60
    auto_pwm_max: int = 255
    auto_sample_interval_frames: int = 8


@dataclass
class SoundConfig:
    """Runtime sound cue settings."""
    enabled: bool = True
    volume_pct: int = 100
    personality: str = "sentinel"
    attitude_pct: int = 60
    rest_cue_enabled: bool = True
    robot_voice_enabled: bool = True
    human_voice_enabled: bool = False
    mute_buzzer_when_human_voice_enabled: bool = True
    human_voice_name: str = "Microsoft Zira Desktop"
    human_voice_style: str = "neutral"
    human_voice_rate_pct: int = 100
    human_voice_pitch_pct: int = 100
    human_voice_volume_pct: int = 85
    human_voice_cleanup_enabled: bool = True
    known_face_hello_once_per_session: bool = True
    name_announce_cooldown_s: float = 18.0
    autotracking_voice_reports_enabled: bool = False
    pir_voice_alerts_enabled: bool = False
    acoustic_voice_alerts_enabled: bool = False
    autotracking_voice_report_cooldown_s: float = 8.0
    voice_commands_enabled: bool = True
    voice_wake_word: str = "elion"
    voice_command_cooldown_s: float = 0.35
    voice_vosk_model_path: str = "models/vosk"
    voice_pre_generated_audio_dir: str = "sounds/voice"
    voice_input_device_name: str = ""
    neural_tts_enabled: bool = False
    neural_tts_voice_name: str = "en-US-JennyNeural"
    # Kokoro offline TTS (primary neural backend — no internet/key required)
    kokoro_model_path: str = "models/kokoro/kokoro-v1.0.onnx"
    kokoro_voices_path: str = "models/kokoro/voices-v1.0.bin"
    kokoro_voice_profile: str = "female_us"
    kokoro_voice_female_us: str = "af_sarah"
    kokoro_voice_male_us: str = "am_michael"
    kokoro_voice_female_uk: str = "bf_emma"
    kokoro_voice_male_uk: str = "bm_george"
    # Optional explicit override. Leave empty to use kokoro_voice_profile mapping.
    kokoro_voice_name: str = ""
    kokoro_speed: float = 1.0


@dataclass
class AcousticGuardConfig:
    """Adaptive USB microphone anomaly detection and alert-sweep behavior."""
    enabled: bool = False
    source: str = "usb_microphone"
    device_name: str = ""
    sample_rate_hz: int = 16000
    block_size: int = 1024
    warmup_seconds: float = 3.0
    baseline_adapt_rate: float = 0.035
    anomaly_threshold_db: float = 3.5
    anomaly_zscore_threshold: float = 1.6
    event_cooldown_s: float = 8.0
    queue_ttl_s: float = 14.0
    home_hold_s: float = 0.35
    pir_check_hold_s: float = 0.30
    quick_lr_hold_s: float = 0.26
    quick_lr_offset_deg: float = 22.0
    sweep_speed_dps: float = 12.0


@dataclass
class FaceRecognitionConfig:
    """Known-face identification and friendly-recognition behavior."""
    enabled: bool = True
    library_path: str = CANONICAL_FACE_LIBRARY_PATH
    backend: str = "opencv_sface"
    detector_model_path: str = "app/models/face/face_detection_yunet_2023mar.onnx"
    recognizer_model_path: str = "app/models/face/face_recognition_sface_2021dec.onnx"
    allow_legacy_fallback: bool = True
    recognition_threshold: float = 0.82
    min_face_size_px: int = 56
    suppress_known_faces_from_engagement: bool = True
    announce_known_faces: bool = True
    cute_gesture_enabled: bool = True
    gesture_cooldown_s: float = 30.0
    registration_samples_required: int = 1


@dataclass
class AIAssistantConfig:
    """Local assistant controls for Smart Sentry diagnostics and Ollama-backed reasoning."""
    enabled: bool = True
    mode: str = "conversational_voice"
    provider: str = "ollama"
    endpoint_url: str = "http://localhost:11434"
    preferred_model_tier: str = "fast"
    model: str = "llama3.2:latest"
    analyst_model: str = "gpt-oss:20b"
    request_timeout_s: float = 45.0
    include_recent_logs: bool = True
    allow_mode_switch: bool = True
    allow_setting_drafts: bool = True
    allow_runtime_analysis: bool = True
    allow_action_execution: bool = True
    auto_speak_responses: bool = False
    auto_speak_requires_cue_name: bool = True


@dataclass
class ShortcutConfig:
    """Global keyboard shortcut preferences."""
    enabled: bool = True
    manual_controls_enabled: bool = False
    quick_view_doc_path: str = "SMART_SENTRY_SHORTCUT_KEYS.md"


@dataclass
class ThemeConfig:
    """Runtime theme settings for the SMART SENTRY V3 UI."""
    preset: str = "ember"
    accent_strength_pct: int = 100
    surface_opacity_pct: int = 94
    video_panel_opacity_pct: int = 100
    window_opacity_pct: int = 100
    corner_radius_px: int = 14
    font_scale_pct: int = 100
    contrast_pct: int = 100


@dataclass
class ConnectionConfig:
    """Connection settings for SMART SENTRY V3.

    Modes:
        0  Arduino Nano USB IO only     (single COM; legacy ESP32 serial also supported)
        1  Arduino Nano + Debug Board   (2 COM ports; Nano IO + Debug Board USB)
        2  ESP32 WiFi + Debug Board USB (1 COM + UDP)
        3  ESP32 WiFi (fully wireless)  (UDP only)
        4  Dual ESP32 WiFi              (2 UDP endpoints)
    """
    connection_type: int = 3
    # Primary USB IO board serial (modes 0, 1) — legacy ESP32 or Nano replacement
    esp32_port: str = ""
    esp32_baud: int = 115200
    # Debug board serial (modes 1, 2)
    debug_port: str = ""
    debug_baud: int = 115200
    # Primary ESP32 WiFi (modes 2, 3, 4) - handles IO/accessories
    udp_host: str = "192.168.4.1"
    udp_port: int = 9000
    # Secondary ESP32 WiFi (mode 4) - handles servos
    servo_udp_host: str = "192.168.4.2"
    servo_udp_port: int = 9001
    # Servo config
    pan_servo_id: int = 1
    tilt_servo_id: int = 2
    bus_servo_time_ms: int = 55
    # Inversion
    invert_pan: bool = False
    invert_tilt: bool = False
    # WiFi adapter (Windows only) — name of the interface to use for ESP32 SSID
    # e.g. "SMART SENTRY CON"; leave empty to auto-select first available adapter
    wifi_interface: str = ""
    # Camera
    camera_source: str = "0"       # Standalone default camera index; may also be a URL or file path
    camera_width: int = 1280
    camera_height: int = 720
    webcam_zoom_pct: int = 100
    test_source_zoom_pct: int = 100


def normalize_connection_config(connection: "ConnectionConfig") -> List[str]:
    """Clamp Nano USB modes to the shipped host baud expected by the firmware."""
    updates: List[str] = []
    mode = int(getattr(connection, "connection_type", 3) or 3)
    # Always force Nano USB modes (0, 1) to 115200 baud, regardless of saved value
    if mode in NANO_USB_CONNECTION_TYPES:
        if int(getattr(connection, "esp32_baud", NANO_USB_HOST_BAUD) or NANO_USB_HOST_BAUD) != NANO_USB_HOST_BAUD:
            connection.esp32_baud = NANO_USB_HOST_BAUD
            updates.append("esp32_baud (forced to 115200 for Nano USB mode)")
    return updates


@dataclass
class SentryV2Config:
    """Top-level configuration for SMART SENTRY V3."""
    connection: ConnectionConfig = field(default_factory=ConnectionConfig)
    detection_mode: DetectionModeConfig = field(default_factory=DetectionModeConfig)
    target_filter: TargetFilterConfig = field(default_factory=TargetFilterConfig)
    threat_scoring: ThreatScoringConfig = field(default_factory=ThreatScoringConfig)
    engagement: EngagementConfig = field(default_factory=EngagementConfig)
    guard: GuardConfig = field(default_factory=GuardConfig)
    no_fire_masks: List[NoFireMaskConfig] = field(default_factory=list)
    pir_guard: PIRGuardConfig = field(default_factory=PIRGuardConfig)
    lighting: LightingConfig = field(default_factory=LightingConfig)
    sound: SoundConfig = field(default_factory=SoundConfig)
    acoustic_guard: AcousticGuardConfig = field(default_factory=AcousticGuardConfig)
    face_recognition: FaceRecognitionConfig = field(default_factory=FaceRecognitionConfig)
    ai_assistant: AIAssistantConfig = field(default_factory=AIAssistantConfig)
    shortcuts: ShortcutConfig = field(default_factory=ShortcutConfig)
    theme: ThemeConfig = field(default_factory=ThemeConfig)

    # --- Overlay / HUD ---
    show_overlay: bool = True
    overlay_display_mode: str = "show_all"
    show_threat_scores: bool = False
    show_engagement_zone: bool = False
    show_guard_crosshair: bool = True
    show_no_fire_masks: bool = True
    scope_view_enabled: bool = False
    scope_radius_pct: int = 35
    scope_vignette_opacity: int = 60
    settings_panel_width: int = 420
    main_splitter_sizes: List[int] = field(default_factory=list)
    layout_splitter_sizes: List[int] = field(default_factory=list)
    bottom_info_splitter_sizes: List[int] = field(default_factory=list)
    quick_access_expanded: bool = False
    quick_access_pinned: bool = False
    quick_access_panel_height: int = 156
    window_x: int = -1
    window_y: int = -1
    window_width: int = 1280
    window_height: int = 860
    window_maximized: bool = False
    prompted_targets_enabled: bool = False
    prompted_allow_auto_fire: bool = False
    prompted_library_path: str = CANONICAL_PROMPTED_TARGETS_PATH
    quick_startup_enabled: bool = True
    auto_export_logs_and_snapshot_on_close: bool = False

    # --- Persistence ---
    config_path: str = CANONICAL_SETTINGS_PATH

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
        guard.rest_pan = float(min(pan_max, max(pan_min, guard.rest_pan)))
        guard.rest_tilt = float(min(SENTRY_TILT_MAX, max(SENTRY_TILT_MIN, guard.rest_tilt)))
        guard.home_move_speed_dps = float(max(2.0, guard.home_move_speed_dps))
        guard.rest_move_speed_dps = float(max(2.0, guard.rest_move_speed_dps))
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
        normalize_connection_config(cn)
        if not str(cn.camera_source).strip():
            cn.camera_source = "0"
        dm = DetectionModeConfig(**d.get("detection_mode", {}))
        tf = TargetFilterConfig(**d.get("target_filter", {}))
        normalize_target_filter_tracking(tf)
        ts = ThreatScoringConfig(**d.get("threat_scoring", {}))
        eg = EngagementConfig(**d.get("engagement", {}))
        gd_raw = dict(d.get("guard", {}))
        if "rest_pan" not in gd_raw:
            gd_raw["rest_pan"] = gd_raw.get("guard_pan", SENTRY_HOME_PAN)
        if "rest_tilt" not in gd_raw:
            gd_raw["rest_tilt"] = gd_raw.get("guard_tilt", SENTRY_HOME_TILT)
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
        lighting_cfg = LightingConfig(**dict(d.get("lighting", {})))
        sound_cfg = SoundConfig(**dict(d.get("sound", {})))
        acoustic_cfg = AcousticGuardConfig(**dict(d.get("acoustic_guard", {})))
        face_cfg = FaceRecognitionConfig(**dict(d.get("face_recognition", {})))
        ai_cfg = AIAssistantConfig(**dict(d.get("ai_assistant", {})))
        shortcut_cfg = ShortcutConfig(**dict(d.get("shortcuts", {})))
        theme_cfg = ThemeConfig(**dict(d.get("theme", {})))
        
        return cls(
            connection=cn,
            detection_mode=dm,
            target_filter=tf,
            threat_scoring=ts,
            engagement=eg,
            guard=gd,
            no_fire_masks=masks,
            pir_guard=pir_cfg,
            lighting=lighting_cfg,
            sound=sound_cfg,
            acoustic_guard=acoustic_cfg,
            face_recognition=face_cfg,
            ai_assistant=ai_cfg,
            shortcuts=shortcut_cfg,
            theme=theme_cfg,
            show_overlay=d.get("show_overlay", True),
            overlay_display_mode=str(d.get("overlay_display_mode", "show_all") or "show_all"),
            show_threat_scores=d.get("show_threat_scores", False),
            show_engagement_zone=d.get("show_engagement_zone", False),
            show_guard_crosshair=d.get("show_guard_crosshair", True),
            show_no_fire_masks=d.get("show_no_fire_masks", True),
            scope_view_enabled=d.get("scope_view_enabled", False),
            scope_radius_pct=d.get("scope_radius_pct", 35),
            scope_vignette_opacity=d.get("scope_vignette_opacity", 60),
            settings_panel_width=d.get("settings_panel_width", 420),
            main_splitter_sizes=[int(v) for v in d.get("main_splitter_sizes", []) if isinstance(v, (int, float))],
            layout_splitter_sizes=[int(v) for v in d.get("layout_splitter_sizes", []) if isinstance(v, (int, float))],
            bottom_info_splitter_sizes=[int(v) for v in d.get("bottom_info_splitter_sizes", []) if isinstance(v, (int, float))],
            quick_access_expanded=bool(d.get("quick_access_expanded", False)),
            quick_access_pinned=bool(d.get("quick_access_pinned", False)),
            quick_access_panel_height=int(d.get("quick_access_panel_height", 156)),
            window_x=int(d.get("window_x", -1)),
            window_y=int(d.get("window_y", -1)),
            window_width=int(d.get("window_width", 1280)),
            window_height=int(d.get("window_height", 860)),
            window_maximized=bool(d.get("window_maximized", False)),
            prompted_targets_enabled=d.get("prompted_targets_enabled", False),
            prompted_allow_auto_fire=d.get("prompted_allow_auto_fire", False),
            prompted_library_path=d.get("prompted_library_path", CANONICAL_PROMPTED_TARGETS_PATH),
            quick_startup_enabled=d.get("quick_startup_enabled", True),
            auto_export_logs_and_snapshot_on_close=bool(d.get("auto_export_logs_and_snapshot_on_close", False)),
            config_path=d.get("config_path", CANONICAL_SETTINGS_PATH),
        )

    def save(self, path: Optional[str] = None) -> None:
        p = Path(path or self.config_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(self.to_dict(), indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: str) -> "SentryV2Config":
        p = Path(path)
        if p.exists():
            return cls.from_dict(json.loads(p.read_text(encoding="utf-8-sig")))
        return cls()

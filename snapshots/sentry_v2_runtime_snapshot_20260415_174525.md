# Smart Sentry V3.0.0 Runtime Snapshot

- Generated: 2026-04-15 17:45:25
- Engine state: GUARDING
- Connection: ✅ Debug Board: COM34 (sub checksum)
✅ ESP32 WiFi: 192.168.4.1:9000
- Camera: 0
- YOLO: [OK] Runtime ready: yolo11m.pt

## Exported Files

- JSON: snapshots/sentry_v2_runtime_snapshot_20260415_174525.json
- Markdown: snapshots/sentry_v2_runtime_snapshot_20260415_174525.md

## Engine

- Motion enabled: True
- Current pan/tilt: 140.37362637362637 / 87.23076923076924
- Guard pan/tilt: 140.0 / 87.0
- Queue length/index: 0 / 0
- Engage phase: precision
- Visible targets: 0
- Qualified count: 0
- Active no-fire mask: none
- Last reacquire note: none

## Active Target

- Track ID: none
- Class: none
- Score: none
- Aim pan/tilt: None / None
- Burst count: None

## Communications

- Connected: True
- Host managed: False
- Mode: ESP32 WiFi + Debug Board USB
- Trigger mode: Projectile (ESP32 GPIO13 Servo)
- Last command: UDP SOUND 685Hz 61ms @20%
- Last error: none

## Telemetry

- Servo feedback age (s): 0.5783743858337402
- Servo feedback pan/tilt: 140.37362637362637 / 87.23076923076924
- IO runtime source: esp32-state
- IO runtime age (s): 0.16886496543884277
- Safety/mode: 1 / 1
- Current fault: False
- Total current (mA): 0

## Camera

- Capture open: True
- Source kind: camera
- Source label: 0
- Requested resolution: 1280 x 720
- Raw frame: {'width': 1280, 'height': 720, 'channels': 3}
- Display frame: {'width': 1280, 'height': 720, 'channels': 3}
- Blackout frame count: 0
- Recovery attempts/in progress: 0 / False

## YOLO

- Selected model: yolo11m.pt
- Selected model path: YOLO_MODELS/yolo11m.pt
- Loaded model path: YOLO_MODELS/yolo11m.pt
- Detector loaded: True
- Allowed classes: person
- Confidence/min area: 0.72 / 1144

## External Files

- settings_json: app/config/smart_sentry_v3_0_0_settings.json (exists=True)
- legacy_settings_json: app/config/smart_sentry_v3_settings.json (exists=True)
- custom_master_presets: app/config/smart_sentry_v3_custom_presets.json (exists=True)
- prompted_target_library: app/config/smart_sentry_v2_3_2_prompted_targets.json (exists=True)
- snapshot_dir: snapshots (exists=True)
- selected_yolo_model: YOLO_MODELS/yolo11m.pt (exists=True)
- candidate_yolo_model_dirs: YOLO_MODELS, F:\SMART SENTRY V2\YOLO_MODELS

## Recent Log Lines

```text
[17:45:22] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=GUARDING
[17:45:22] [SYSTEM] [PREVIEW] render_mode=full
[17:45:22] [PIR] ESP32 UDP ACK safety=LOCKED mode=PROJECTILE pir=OFF fault=CLEAR ctrl=app
[17:45:22] [PIR] ESP32 UDP ACK safety=LOCKED mode=PROJECTILE pir=OFF fault=CLEAR ctrl=app
[17:45:22] [PIR] ESP32 UDP STATE safety=LOCKED mode=PROJECTILE pir=OFF fault=CLEAR ctrl=app
[17:45:22] [SYSTEM] [PREVIEW] render_mode=busy-lite
[17:45:22] [ACCESSORY] [PREVIEW] render_mode=throttled
[17:45:23] [SYSTEM] [PREVIEW] render_mode=busy-lite
[17:45:23] [PIR] ESP32 UDP ACK safety=LOCKED mode=PROJECTILE pir=OFF fault=CLEAR ctrl=app
[17:45:23] [PIR] ESP32 UDP ACK safety=LOCKED mode=PROJECTILE pir=OFF fault=CLEAR ctrl=app
[17:45:23] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=GUARDING
[17:45:23] [SYSTEM] [PREVIEW] render_mode=full
[17:45:23] [SYSTEM] [PREVIEW] render_mode=busy-lite
[17:45:23] [SYSTEM] [PREVIEW] render_mode=full
[17:45:24] [SYSTEM] [PREVIEW] render_mode=busy-lite
[17:45:24] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=GUARDING
[17:45:24] [ACCESSORY] [PREVIEW] render_mode=throttled
[17:45:24] [PIR] ESP32 UDP STATE safety=LOCKED mode=PROJECTILE pir=OFF fault=CLEAR ctrl=app
[17:45:24] [PIR] ESP32 UDP ACK safety=LOCKED mode=PROJECTILE pir=OFF fault=CLEAR ctrl=app
[17:45:24] [PIR] ESP32 UDP ACK safety=LOCKED mode=PROJECTILE pir=OFF fault=CLEAR ctrl=app
```

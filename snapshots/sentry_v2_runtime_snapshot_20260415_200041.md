# Smart Sentry V3.0.0 Runtime Snapshot

- Generated: 2026-04-15 20:00:41
- Engine state: GUARDING
- Connection: ✅ Debug Board: COM34 (sub checksum)
✅ ESP32 WiFi: 192.168.4.1:9000
- Camera: 0
- YOLO: [OK] Runtime ready: yolo11m.pt

## Exported Files

- JSON: snapshots/sentry_v2_runtime_snapshot_20260415_200041.json
- Markdown: snapshots/sentry_v2_runtime_snapshot_20260415_200041.md

## Engine

- Motion enabled: True
- Current pan/tilt: 139.97802197802199 / 86.43956043956044
- Guard pan/tilt: 140.0 / 87.0
- Queue length/index: 1 / 1
- Engage phase: precision
- Visible targets: 0
- Qualified count: 0
- Active no-fire mask: none
- Last reacquire note: loss local scan

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
- Trigger mode: Water (MOSFET)
- Last command: UDP SOUND 762Hz 64ms @20%
- Last error: none

## Telemetry

- Servo feedback age (s): 0.8073840141296387
- Servo feedback pan/tilt: 139.97802197802199 / 86.43956043956044
- IO runtime source: esp32-state
- IO runtime age (s): 0.26778531074523926
- Safety/mode: 1 / 0
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
- Confidence/min area: 0.6599999999999999 / 572

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
[20:00:37] [PIR] ESP32 UDP ACK safety=LOCKED mode=WATER pir=OFF fault=CLEAR ctrl=app
[20:00:37] [PIR] ESP32 UDP STATE safety=LOCKED mode=WATER pir=OFF fault=CLEAR ctrl=app
[20:00:37] [PIR] ESP32 UDP ACK safety=LOCKED mode=WATER pir=OFF fault=CLEAR ctrl=app
[20:00:38] [SYSTEM] [PREVIEW] render_mode=busy-lite
[20:00:38] [ACCESSORY] [PREVIEW] render_mode=throttled
[20:00:38] [SYSTEM] [PREVIEW] render_mode=busy-lite
[20:00:38] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=GUARDING
[20:00:38] [ACCESSORY] [PREVIEW] render_mode=throttled
[20:00:38] [PIR] ESP32 UDP ACK safety=LOCKED mode=WATER pir=OFF fault=CLEAR ctrl=app
[20:00:38] [PIR] ESP32 UDP ACK safety=LOCKED mode=WATER pir=OFF fault=CLEAR ctrl=app
[20:00:39] [SYSTEM] [PREVIEW] render_mode=busy-lite
[20:00:39] [SYSTEM] [PREVIEW] render_mode=full
[20:00:39] [PIR] ESP32 UDP STATE safety=LOCKED mode=WATER pir=OFF fault=CLEAR ctrl=app
[20:00:40] [SYSTEM] [PREVIEW] render_mode=busy-lite
[20:00:40] [PIR] ESP32 UDP ACK safety=LOCKED mode=WATER pir=OFF fault=CLEAR ctrl=app
[20:00:40] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=GUARDING
[20:00:40] [ACCESSORY] [PREVIEW] render_mode=throttled
[20:00:40] [PIR] ESP32 UDP ACK safety=LOCKED mode=WATER pir=OFF fault=CLEAR ctrl=app
[20:00:40] [SYSTEM] [PREVIEW] render_mode=busy-lite
[20:00:40] [ACCESSORY] [PREVIEW] render_mode=throttled
```

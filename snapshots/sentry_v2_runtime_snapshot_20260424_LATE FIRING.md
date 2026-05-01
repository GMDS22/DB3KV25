# Smart Sentry V3.0.0 Runtime Snapshot

- Generated: 2026-04-24 17:37:53
- Engine state: GUARDING
- Connection: ✅ Debug Board: COM31 (sub checksum)
✅ ESP32 WiFi: 192.168.4.1:9000
- Camera: 0
- YOLO: [OK] Runtime ready: yolov8n.pt

## Exported Files

- JSON: snapshots/sentry_v2_runtime_snapshot_20260424_173753.json
- Markdown: snapshots/sentry_v2_runtime_snapshot_20260424_173753.md

## Engine

- Motion enabled: True
- Current pan/tilt: 144.72527472527472 / 90.06593406593406
- Guard pan/tilt: 140.0 / 82.0
- Queue length/index: 1 / 1
- Engage phase: precision
- Visible targets: 0
- Qualified count: 0
- Active no-fire mask: none
- Last reacquire note: persistent reacquire

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
- Last command: UDP PIR P0
- Last error: none

## Telemetry

- Servo feedback age (s): 0.41782069206237793
- Servo feedback pan/tilt: 144.72527472527472 / 90.06593406593406
- IO runtime source: esp32-state
- IO runtime age (s): 6.6201276779174805
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

- Selected model: yolov8n.pt
- Selected model path: F:\SMART SENTRY V3.0.0\YOLO_MODELS\yolov8n.pt
- Loaded model path: F:\SMART SENTRY V3.0.0\YOLO_MODELS\yolov8n.pt
- Detector loaded: True
- Allowed classes: person
- Confidence/min area: 0.44 / 1200

## External Files

- settings_json: app/config/smart_sentry_v3_0_0_settings.json (exists=True)
- legacy_settings_json: app/config/sentry_v2_settings.json (exists=False)
- custom_master_presets: app/config/smart_sentry_v3_0_0_custom_presets.json (exists=True)
- prompted_target_library: app/config/smart_sentry_v3_0_0_prompted_targets.json (exists=True)
- snapshot_dir: snapshots (exists=True)
- selected_yolo_model: F:\SMART SENTRY V3.0.0\YOLO_MODELS\yolov8n.pt (exists=True)
- candidate_yolo_model_dirs: F:\SMART SENTRY V3.0.0\YOLO_MODELS, YOLO_MODELS, F:\SMART SENTRY V2\YOLO_MODELS

## Recent Log Lines

```text
[17:37:50] [SYSTEM] [PREVIEW] render_mode=busy-lite
[17:37:50] [SYSTEM] [PREVIEW] render_mode=full
[17:37:50] [SYSTEM] [PREVIEW] render_mode=busy-lite
[17:37:51] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=GUARDING
[17:37:51] [SYSTEM] [PREVIEW] render_mode=full
[17:37:51] [SYSTEM] [PREVIEW] render_mode=busy-lite
[17:37:51] [SYSTEM] [PREVIEW] render_mode=full
[17:37:51] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=GUARDING
[17:37:51] [ACCESSORY] [PREVIEW] render_mode=throttled
[17:37:52] [SYSTEM] [PREVIEW] render_mode=busy-lite
[17:37:52] [SYSTEM] [PREVIEW] render_mode=full
[17:37:52] [SYSTEM] [PREVIEW] render_mode=busy-lite
[17:37:52] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=GUARDING
[17:37:52] [SYSTEM] [PREVIEW] render_mode=full
[17:37:52] [SYSTEM] [PREVIEW] render_mode=busy-lite
[17:37:53] [SYSTEM] [PREVIEW] render_mode=full
[17:37:53] [SYSTEM] [PREVIEW] render_mode=busy-lite
[17:37:53] [ACCESSORY] [PREVIEW] render_mode=throttled
[17:37:53] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=GUARDING
[17:37:53] [SYSTEM] [PREVIEW] render_mode=full
```

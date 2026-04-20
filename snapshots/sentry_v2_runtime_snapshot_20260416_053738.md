# Smart Sentry V3.0.0 Runtime Snapshot

- Generated: 2026-04-16 05:37:38
- Engine state: GUARDING
- Connection: ✅ Debug Board: COM34 (sub checksum)
✅ ESP32 WiFi: 192.168.4.1:9000
- Camera: 0
- YOLO: [OK] Runtime ready: yolo11m.pt

## Exported Files

- JSON: snapshots/sentry_v2_runtime_snapshot_20260416_053738.json
- Markdown: snapshots/sentry_v2_runtime_snapshot_20260416_053738.md

## Engine

- Motion enabled: True
- Current pan/tilt: 139.78021978021977 / 86.96703296703298
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
- Last command: UDP PIR P0
- Last error: none

## Telemetry

- Servo feedback age (s): 0.5840692520141602
- Servo feedback pan/tilt: 139.78021978021977 / 86.96703296703298
- IO runtime source: esp32-state
- IO runtime age (s): 9.486186265945435
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
- Confidence/min area: 0.18 / 0

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
[05:37:35] [ACCESSORY] [PREVIEW] render_mode=throttled
[05:37:35] [SYSTEM] [PREVIEW] render_mode=busy-lite
[05:37:35] [ACCESSORY] [PREVIEW] render_mode=throttled
[05:37:36] [SYSTEM] [PREVIEW] render_mode=full
[05:37:36] [ACCESSORY] [PREVIEW] render_mode=throttled
[05:37:36] [SYSTEM] [PREVIEW] render_mode=busy-lite
[05:37:36] [ACCESSORY] [PREVIEW] render_mode=throttled
[05:37:36] [SYSTEM] [PREVIEW] render_mode=busy-lite
[05:37:36] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=GUARDING
[05:37:36] [ACCESSORY] [PREVIEW] render_mode=throttled
[05:37:36] [SYSTEM] [PREVIEW] render_mode=full
[05:37:36] [ACCESSORY] [PREVIEW] render_mode=throttled
[05:37:37] [SYSTEM] [PREVIEW] render_mode=busy-lite
[05:37:37] [SYSTEM] [PREVIEW] render_mode=full
[05:37:37] [ACCESSORY] [PREVIEW] render_mode=throttled
[05:37:37] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=GUARDING
[05:37:37] [SYSTEM] [PREVIEW] render_mode=full
[05:37:38] [SYSTEM] [PREVIEW] render_mode=busy-lite
[05:37:38] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=GUARDING
[05:37:38] [ACCESSORY] [PREVIEW] render_mode=throttled
```

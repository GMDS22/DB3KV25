# Smart Sentry V3.0.0 Runtime Snapshot

- Generated: 2026-04-16 18:41:57
- Engine state: ENGAGING
- Connection: ✅ Debug Board: COM34 (sub checksum)
✅ ESP32 WiFi: 192.168.4.1:9000
- Camera: 0
- YOLO: [OK] Runtime ready: yolo11m.pt

## Exported Files

- JSON: snapshots/sentry_v2_runtime_snapshot_20260416_184157.json
- Markdown: snapshots/sentry_v2_runtime_snapshot_20260416_184157.md

## Engine

- Motion enabled: True
- Current pan/tilt: 160.64669994743295 / 75.68997940574688
- Guard pan/tilt: 140.0 / 87.0
- Queue length/index: 1 / 0
- Engage phase: precision
- Visible targets: 1
- Qualified count: 1
- Active no-fire mask: none
- Last reacquire note: persistent reacquire

## Active Target

- Track ID: 118
- Class: person
- Score: 0.8335022156097563
- Aim pan/tilt: 169.80287603021975 / 83.56568986568986
- Burst count: 1

## Communications

- Connected: True
- Host managed: False
- Mode: ESP32 WiFi + Debug Board USB
- Trigger mode: Water (MOSFET)
- Last command: UDP IO F0L0R0S0M0A0P0 | UDP IO F0L0R0A0P0
- Last error: none

## Telemetry

- Servo feedback age (s): 0.9579896926879883
- Servo feedback pan/tilt: 160.6813186813187 / 75.62637362637362
- IO runtime source: esp32-ack
- IO runtime age (s): 0.19419503211975098
- Safety/mode: 0 / 0
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
- Recovery attempts/in progress: 2 / False

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
[18:35:23] [CAMERA] Scope view: OFF (normal video restored)
[18:35:30] [CAMERA] Scope view: OFF (normal video restored)
[18:36:24] [CAMERA] Scope view: OFF (normal video restored)
[18:36:31] [CAMERA] Scope view: OFF (normal video restored)
[18:36:37] [CAMERA] Scope view: OFF (normal video restored)
[18:37:12] [CAMERA] Scope view: OFF (normal video restored)
[18:39:21] [CAMERA] Scope view: OFF (normal video restored)
[18:39:28] [CAMERA] Scope view: OFF (normal video restored)
[18:39:35] [CAMERA] Scope view: OFF (normal video restored)
[18:39:43] [CAMERA] Scope view: OFF (normal video restored)
[18:39:51] [CAMERA] Scope view: OFF (normal video restored)
[18:40:01] [CAMERA] Scope view: OFF (normal video restored)
[18:40:12] [CAMERA] Scope view: OFF (normal video restored)
[18:40:18] [CAMERA] Scope view: OFF (normal video restored)
[18:40:24] [CAMERA] Scope view: OFF (normal video restored)
[18:40:38] [CAMERA] Scope view: OFF (normal video restored)
[18:40:43] [CAMERA] Scope view: OFF (normal video restored)
[18:41:29] [CAMERA] Scope view: OFF (normal video restored)
[18:41:38] [CAMERA] Scope view: OFF (normal video restored)
[18:41:46] [CAMERA] Scope view: OFF (normal video restored)
```

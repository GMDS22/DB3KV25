# SMART SENTRY V2.3.1 Runtime Snapshot

- Generated: 2026-04-07 01:29:45
- Engine state: ENGAGING
- Connection: ✅ Debug Board: COM34 (sub checksum)
✅ ESP32 USB: COM28
- Camera: 0
- YOLO: [OK] Runtime ready: yolov8l.pt

## Exported Files

- JSON: snapshots/sentry_v2_runtime_snapshot_20260407_012945.json
- Markdown: snapshots/sentry_v2_runtime_snapshot_20260407_012945.md

## Engine

- Motion enabled: True
- Current pan/tilt: 113.67032967032966 / 50.83516483516483
- Guard pan/tilt: 140.0 / 80.0
- Queue length/index: 1 / 0
- Engage phase: precision
- Visible targets: 0
- Qualified count: 0
- Active no-fire mask: none
- Last reacquire note: loss expanding scan

## Active Target

- Track ID: none
- Class: motion
- Score: 0.0
- Aim pan/tilt: 147.85992445054947 / 80.21656491656492
- Burst count: 0

## Communications

- Connected: True
- Host managed: False
- Mode: ESP32 USB + Debug Board USB
- Trigger mode uses BB servo: True
- Last command: SOUND:870:122
- Last error: none

## Telemetry

- Servo feedback age (s): 0.7229142189025879
- Servo feedback pan/tilt: 113.67032967032966 / 50.83516483516483
- IO runtime source: inactive
- IO runtime age (s): None
- Safety/mode: None / None
- Current fault: None
- Total current (mA): None

## Camera

- Capture open: True
- Source kind: camera
- Source label: 0
- Requested resolution: 1920 x 1080
- Raw frame: {'width': 1920, 'height': 1080, 'channels': 3}
- Display frame: {'width': 1920, 'height': 1080, 'channels': 3}
- Recovery attempts/in progress: 0 / False

## YOLO

- Selected model: yolov8l.pt
- Selected model path: YOLO_MODELS/yolov8l.pt
- Loaded model path: YOLO_MODELS/yolov8l.pt
- Detector loaded: True
- Allowed classes: all
- Confidence/min area: 0.62 / 936

## External Files

- settings_json: app/config/smart_sentry_v3_settings.json (exists=True)
- legacy_settings_json: app/app/config/sentry_v2_settings.json (exists=True)
- custom_master_presets: app/config/smart_sentry_v3_custom_presets.json (exists=True)
- prompted_target_library: app/config/smart_sentry_v3_prompted_targets.json (exists=True)
- snapshot_dir: snapshots (exists=True)
- selected_yolo_model: YOLO_MODELS/yolov8l.pt (exists=True)
- candidate_yolo_model_dirs: YOLO_MODELS, app/YOLO_MODELS, app/models, F:\SMART SENTRY V2\YOLO_MODELS

## Recent Log Lines

```text
[01:29:44] [PREVIEW] render_mode=throttled
[01:29:44] [PREVIEW] render_mode=full
[01:29:44] [PREVIEW] render_mode=throttled
[01:29:44] [PREVIEW] render_mode=full
[01:29:44] [PREVIEW] render_mode=throttled
[01:29:44] [PREVIEW] render_mode=full
[01:29:44] [PREVIEW] render_mode=throttled
[01:29:44] [PREVIEW] render_mode=full
[01:29:44] [PREVIEW] render_mode=throttled
[01:29:44] [PREVIEW] render_mode=full
[01:29:44] [PREVIEW] render_mode=throttled
[01:29:44] [PREVIEW] render_mode=full
[01:29:45] [PREVIEW] render_mode=throttled
[01:29:45] [PREVIEW] render_mode=full
[01:29:45] [PREVIEW] render_mode=throttled
[01:29:45] [PREVIEW] render_mode=full
[01:29:45] [PREVIEW] render_mode=throttled
[01:29:45] [PREVIEW] render_mode=full
[01:29:45] [PREVIEW] render_mode=throttled
[01:29:45] [PREVIEW] render_mode=full
```

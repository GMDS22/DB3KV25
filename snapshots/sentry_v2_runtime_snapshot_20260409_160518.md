# SMART SENTRY V2.3.2 Runtime Snapshot

- Generated: 2026-04-09 16:05:18
- Engine state: ENGAGING
- Connection: ✅ Debug Board: COM34 (sub checksum)
✅ ESP32 WiFi: 192.168.4.1:9000
- Camera: 0
- YOLO: [OK] Runtime ready: yolo11n.pt

## Exported Files

- JSON: snapshots/sentry_v2_runtime_snapshot_20260409_160518.json
- Markdown: snapshots/sentry_v2_runtime_snapshot_20260409_160518.md

## Engine

- Motion enabled: True
- Current pan/tilt: 149.5186813186817 / 80.95481479078802
- Guard pan/tilt: 140.0 / 87.0
- Queue length/index: 1 / 0
- Engage phase: precision
- Visible targets: 1
- Qualified count: 1
- Active no-fire mask: none
- Last reacquire note: persistent reacquire

## Active Target

- Track ID: none
- Class: person
- Score: 0.0
- Aim pan/tilt: 169.62493131868132 / 80.6055759055759
- Burst count: 0

## Communications

- Connected: True
- Host managed: False
- Mode: ESP32 WiFi + Debug Board USB
- Trigger mode uses BB servo: True
- Last command: UDP IO F0L0R0S1M1A1P0 | UDP IO F0L0R0A1P0
- Last error: none

## Telemetry

- Servo feedback age (s): 4.001549959182739
- Servo feedback pan/tilt: 139.3186813186813 / 87.09890109890111
- IO runtime source: waiting
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

- Selected model: yolo11n.pt
- Selected model path: YOLO_MODELS/yolo11n.pt
- Loaded model path: YOLO_MODELS/yolo11n.pt
- Detector loaded: True
- Allowed classes: person
- Confidence/min area: 0.72 / 1144

## External Files

- settings_json: app/config/smart_sentry_v2_3_2_settings.json (exists=True)
- legacy_settings_json: app/config/smart_sentry_v3_settings.json (exists=True)
- custom_master_presets: app/config/smart_sentry_v3_custom_presets.json (exists=True)
- prompted_target_library: app/config/smart_sentry_v2_3_2_prompted_targets.json (exists=True)
- snapshot_dir: snapshots (exists=True)
- selected_yolo_model: YOLO_MODELS/yolo11n.pt (exists=True)
- candidate_yolo_model_dirs: YOLO_MODELS, F:\SMART SENTRY V2\YOLO_MODELS

## Recent Log Lines

```text
[16:05:16] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=8 conf=0.87 active_track=8
[16:05:16] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=8 conf=0.86 active_track=8
[16:05:16] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=8 conf=0.88 active_track=8
[16:05:16] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=8 conf=0.87 active_track=8
[16:05:16] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=8 conf=0.88 active_track=8
[16:05:16] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=8 conf=0.87 active_track=8
[16:05:17] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=8 conf=0.86 active_track=8
[16:05:17] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=8 conf=0.87 active_track=8
[16:05:17] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=8 conf=0.86 active_track=8
[16:05:17] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=8 conf=0.88 active_track=8
[16:05:17] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=8 conf=0.89 active_track=8
[16:05:17] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=8 conf=0.88 active_track=8
[16:05:17] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=8 conf=0.88 active_track=8
[16:05:17] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=8 conf=0.90 active_track=8
[16:05:17] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=8 conf=0.88 active_track=8
[16:05:17] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=8 conf=0.83 active_track=8
[16:05:18] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=8 conf=0.78 active_track=8
[16:05:18] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=8 conf=0.81 active_track=8
[16:05:18] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=8 conf=0.85 active_track=8
[16:05:18] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=8 conf=0.85 active_track=8
```

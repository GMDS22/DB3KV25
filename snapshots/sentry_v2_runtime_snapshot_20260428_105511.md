# SMART SENTRY V3.5.0 Runtime Snapshot

- Generated: 2026-04-28 10:55:11
- Engine state: GUARDING
- Connection: ✅ Debug Board: COM31 (sub checksum)
✅ USB IO Board: COM27
- Camera: 0
- YOLO: [OK] Runtime ready: yolov8l.pt

## Exported Files

- JSON: snapshots/sentry_v2_runtime_snapshot_20260428_105511.json
- Markdown: snapshots/sentry_v2_runtime_snapshot_20260428_105511.md

## Engine

- Motion enabled: True
- Current pan/tilt: 139.09869402485103 / 71.92649958131427
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
- Mode: Arduino Nano USB + Debug Board USB
- Trigger mode: Water (MOSFET)
- Last command: BUS hold P131 T72 @91ms [sub] | IO F0L0R0G0A0
- Last error: none

## Telemetry

- Servo feedback age (s): 0.4000740051269531
- Servo feedback pan/tilt: 139.9120879120879 / 73.18681318681318
- IO runtime source: inactive
- IO runtime age (s): None
- Safety/mode: None / None
- Current fault: None
- Total current (mA): None

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

- Selected model: yolov8l.pt
- Selected model path: F:\SMART SENTRY V3.5.0\YOLO_MODELS\yolov8l.pt
- Loaded model path: F:\SMART SENTRY V3.5.0\YOLO_MODELS\yolov8l.pt
- Detector loaded: True
- Allowed classes: person
- Confidence/min area: 0.44 / 1200

## External Files

- settings_json: app/config/smart_sentry_v3_5_0_settings.json (exists=True)
- legacy_settings_json: app/config/sentry_v2_settings.json (exists=False)
- custom_master_presets: app/config/smart_sentry_v3_5_0_custom_presets.json (exists=True)
- prompted_target_library: app/config/smart_sentry_v3_5_0_prompted_targets.json (exists=True)
- snapshot_dir: snapshots (exists=True)
- selected_yolo_model: F:\SMART SENTRY V3.5.0\YOLO_MODELS\yolov8l.pt (exists=True)
- candidate_yolo_model_dirs: F:\SMART SENTRY V3.5.0\YOLO_MODELS, YOLO_MODELS, F:\SMART SENTRY_v2a\YOLO_MODELS

## Recent Log Lines

```text
[10:55:09] [SYSTEM] USB IO RX STAT S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[10:55:09] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=GUARDING
[10:55:09] [SYSTEM] [PREVIEW] render_mode=full
[10:55:10] [SYSTEM] [PREVIEW] render_mode=busy-lite
[10:55:10] [SYSTEM] USB IO RX RECV: SOUND:537:24:2
[10:55:10] [SYSTEM] USB IO RX ACK SOUND freq=537 duration=24 volume=2
[10:55:10] [SYSTEM] USB IO RX RECV: SOUND:719:22:2
[10:55:10] [SYSTEM] USB IO RX ACK SOUND freq=719 duration=22 volume=2
[10:55:10] [SYSTEM] USB IO RX RECV: SOUND:610:24:2
[10:55:10] [SYSTEM] USB IO RX ACK SOUND freq=610 duration=24 volume=2
[10:55:10] [SYSTEM] USB IO RX RECV: SOUND:871:116:2
[10:55:10] [SYSTEM] USB IO RX ACK SOUND freq=871 duration=116 volume=2
[10:55:10] [SYSTEM] USB IO RX RECV: S0
[10:55:10] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[10:55:10] [SYSTEM] USB IO RX RECV: M0
[10:55:10] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[10:55:10] [SYSTEM] USB IO RX RECV: F0L0R0G0A0
[10:55:10] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[10:55:10] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=GUARDING
[10:55:10] [SYSTEM] [PREVIEW] render_mode=full
```

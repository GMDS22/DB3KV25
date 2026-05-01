# SMART SENTRY V3.5.0 Runtime Snapshot

- Generated: 2026-04-27 18:12:32
- Engine state: GUARDING
- Connection: ✅ Debug Board: COM31 (sub checksum)
✅ USB IO Board: COM28
- Camera: 0
- YOLO: [OK] Runtime ready: yolov8l.pt

## Exported Files

- JSON: snapshots/sentry_v2_runtime_snapshot_20260427_181232.json
- Markdown: snapshots/sentry_v2_runtime_snapshot_20260427_181232.md

## Engine

- Motion enabled: True
- Current pan/tilt: 139.97802197802199 / 80.7032967032967
- Guard pan/tilt: 140.0 / 82.0
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
- Mode: Arduino Nano USB + Debug Board USB
- Trigger mode: Water (MOSFET)
- Last command: BUS hold P131 T79 @43ms [sub] | IO F0L0R0G0A0
- Last error: none

## Telemetry

- Servo feedback age (s): 0.2887237071990967
- Servo feedback pan/tilt: 139.97802197802199 / 80.7032967032967
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
- Confidence/min area: 0.24 / 1200

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
[18:12:31] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[18:12:31] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=GUARDING
[18:12:32] [SYSTEM] [PREVIEW] render_mode=full
[18:12:32] [SYSTEM] [PREVIEW] render_mode=busy-lite
[18:12:32] [SYSTEM] USB IO RX STAT S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[18:12:32] [SYSTEM] USB IO RX RECV: S0
[18:12:32] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[18:12:32] [SYSTEM] USB IO RX RECV: M0
[18:12:32] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[18:12:32] [SYSTEM] USB IO RX RECV: F0L0R0G0A0
[18:12:32] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[18:12:32] [SYSTEM] [PREVIEW] render_mode=full
[18:12:32] [SYSTEM] [PREVIEW] render_mode=busy-lite
[18:12:32] [SYSTEM] USB IO RX RECV: S0
[18:12:32] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[18:12:32] [SYSTEM] USB IO RX RECV: M0
[18:12:32] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[18:12:32] [SYSTEM] USB IO RX RECV: F0L0R0G0A0
[18:12:32] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[18:12:32] [SYSTEM] [PREVIEW] render_mode=full
```

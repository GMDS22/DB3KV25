# SMART SENTRY V3.5.0 Runtime Snapshot

- Generated: 2026-04-28 11:24:57
- Engine state: ENGAGING
- Connection: ✅ Debug Board: COM31 (sub checksum)
✅ USB IO Board: COM27
- Camera: 0
- YOLO: [OK] Runtime ready: yolov8l.pt

## Exported Files

- JSON: snapshots/sentry_v2_runtime_snapshot_20260428_112457.json
- Markdown: snapshots/sentry_v2_runtime_snapshot_20260428_112457.md

## Engine

- Motion enabled: True
- Current pan/tilt: 196.8131868131868 / 83.14285714285715
- Guard pan/tilt: 140.0 / 82.0
- Queue length/index: 1 / 0
- Engage phase: fire
- Visible targets: 1
- Qualified count: 1
- Active no-fire mask: none
- Last reacquire note: none

## Active Target

- Track ID: 1
- Class: person
- Score: 0.48441835552618134
- Aim pan/tilt: 222.09663222782603 / 83.74648237066769
- Burst count: 2

## Communications

- Connected: True
- Host managed: False
- Mode: Arduino Nano USB + Debug Board USB
- Trigger mode: Water (MOSFET)
- Last command: SOUND:1232:61:2
- Last error: none

## Telemetry

- Servo feedback age (s): 0.8388063907623291
- Servo feedback pan/tilt: 196.8131868131868 / 83.14285714285715
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
- Confidence/min area: 0.38 / 1200

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
[11:24:55] [SAFETY] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=1 conf=0.94 active_track=1
[11:24:55] [SYSTEM] [PREVIEW] render_mode=full
[11:24:55] [SYSTEM] USB IO RX STAT S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[11:24:56] [SYSTEM] [PREVIEW] render_mode=busy-lite
[11:24:56] [SYSTEM] USB IO RX RECV: S0
[11:24:56] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[11:24:56] [SYSTEM] USB IO RX RECV: M0
[11:24:56] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[11:24:56] [SYSTEM] USB IO RX RECV: F0L0R0G0A0
[11:24:56] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[11:24:56] [SYSTEM] USB IO RX RECV: S0
[11:24:56] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[11:24:56] [SYSTEM] USB IO RX RECV: M0
[11:24:56] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[11:24:56] [SYSTEM] USB IO RX RECV: F0L0R0G0A0
[11:24:56] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[11:24:56] [SAFETY] FIRE! Burst: 2
[11:24:56] [SAFETY] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=1 conf=0.93 active_track=1
[11:24:56] [SYSTEM] [PREVIEW] render_mode=full
[11:24:56] [SYSTEM] USB IO RX STAT S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
```

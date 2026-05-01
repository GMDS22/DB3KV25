# SMART SENTRY V3.5.0 Runtime Snapshot

- Generated: 2026-04-30 14:37:10
- Engine state: GUARDING
- Connection: ✅ Debug Board: COM31 (sub checksum)
✅ USB IO Board: COM27
- Camera: 0
- YOLO: [OK] Runtime ready: yolo11m.pt

## Exported Files

- JSON: snapshots/sentry_v2_runtime_snapshot_20260430_143710.json
- Markdown: snapshots/sentry_v2_runtime_snapshot_20260430_143710.md

## Engine

- Motion enabled: True
- Current pan/tilt: 135.4345093300798 / 65.26028916630258
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
- Last command: BUS hold P135 T65 @28ms [sub] | IO F0L0R0G0A0
- Last error: none

## Telemetry

- Servo feedback age (s): 0.6532220840454102
- Servo feedback pan/tilt: 136.54945054945054 / 66.26373626373626
- IO runtime source: inactive
- IO runtime age (s): None
- Safety/mode: None / None
- Current fault: None
- Total current (mA): None

## Camera

- Capture open: False
- Source kind: 
- Source label: 0
- Requested resolution: 1280 x 720
- Raw frame: {'width': 1280, 'height': 720, 'channels': 3}
- Display frame: None
- Blackout frame count: 0
- Recovery attempts/in progress: 0 / False

## YOLO

- Selected model: yolo11m.pt
- Selected model path: F:\SMART SENTRY V3.5.0\YOLO_MODELS\yolo11m.pt
- Loaded model path: F:\SMART SENTRY V3.5.0\YOLO_MODELS\yolo11m.pt
- Detector loaded: True
- Allowed classes: person
- Confidence/min area: 0.44 / 1200

## External Files

- settings_json: app/config/smart_sentry_v3_5_0_settings.json (exists=True)
- legacy_settings_json: app/config/sentry_v2_settings.json (exists=False)
- custom_master_presets: app/config/smart_sentry_v3_5_0_custom_presets.json (exists=True)
- prompted_target_library: app/config/smart_sentry_v3_5_0_prompted_targets.json (exists=True)
- snapshot_dir: snapshots (exists=True)
- selected_yolo_model: F:\SMART SENTRY V3.5.0\YOLO_MODELS\yolo11m.pt (exists=True)
- candidate_yolo_model_dirs: F:\SMART SENTRY V3.5.0\YOLO_MODELS, YOLO_MODELS, F:\SMART SENTRY_v2a\YOLO_MODELS

## Recent Log Lines

```text
[14:37:08] [SYSTEM] USB IO RX ACK S=1 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=10 U=0 V=45 H=360 B=0 P=0
[14:37:08] [SYSTEM] [PREVIEW] render_mode=full
[14:37:09] [SYSTEM] [PREVIEW] render_mode=busy-lite
[14:37:09] [SYSTEM] USB IO RX RECV: SOUND:622:24:2
[14:37:09] [SYSTEM] USB IO RX ACK SOUND freq=622 duration=24 volume=2
[14:37:09] [SYSTEM] USB IO RX RECV: SOUND:735:24:2
[14:37:09] [SYSTEM] USB IO RX ACK SOUND freq=735 duration=24 volume=2
[14:37:09] [SYSTEM] USB IO RX RECV: SOUND:894:39:2
[14:37:09] [SYSTEM] USB IO RX ACK SOUND freq=894 duration=39 volume=2
[14:37:09] [SYSTEM] USB IO RX RECV: SOUND:695:124:2
[14:37:09] [SYSTEM] USB IO RX ACK SOUND freq=695 duration=124 volume=2
[14:37:09] [SYSTEM] USB IO RX RECV: S1
[14:37:09] [SYSTEM] USB IO RX ACK S=1 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=10 U=0 V=45 H=360 B=0 P=0
[14:37:09] [SYSTEM] USB IO RX RECV: M0
[14:37:09] [SYSTEM] USB IO RX ACK S=1 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=10 U=0 V=45 H=360 B=0 P=0
[14:37:09] [SYSTEM] USB IO RX RECV: F0L0R0G0A0
[14:37:09] [SYSTEM] USB IO RX ACK S=1 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=10 U=0 V=45 H=360 B=0 P=0
[14:37:09] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=GUARDING
[14:37:09] [SYSTEM] [PREVIEW] render_mode=full
[14:37:10] [CAMERA] Serial log exported: snapshots/serial_log_exports/sentry_v2_serial_log_20260430_143710.txt
```

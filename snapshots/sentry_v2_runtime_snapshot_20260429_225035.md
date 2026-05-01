# SMART SENTRY V3.5.0 Runtime Snapshot

- Generated: 2026-04-29 22:50:35
- Engine state: ENGAGING
- Connection: ✅ Debug Board: COM31 (sub checksum)
✅ USB IO Board: COM27
- Camera: 0
- YOLO: [OK] Runtime ready: yolo11m.pt

## Exported Files

- JSON: snapshots/sentry_v2_runtime_snapshot_20260429_225035.json
- Markdown: snapshots/sentry_v2_runtime_snapshot_20260429_225035.md

## Engine

- Motion enabled: True
- Current pan/tilt: 187.1878925989655 / 81.33147882448183
- Guard pan/tilt: 140.0 / 82.0
- Queue length/index: 1 / 0
- Engage phase: precision
- Visible targets: 1
- Qualified count: 1
- Active no-fire mask: none
- Last reacquire note: fire stale pose -> precision

## Active Target

- Track ID: 1
- Class: person
- Score: 0.41091953594332514
- Aim pan/tilt: 197.79956429129265 / 83.04997919842106
- Burst count: 6

## Communications

- Connected: True
- Host managed: False
- Mode: Arduino Nano USB + Debug Board USB
- Trigger mode: Projectile (ESP32 GPIO13 Servo)
- Last command: BUS hold P83 T81 @28ms [sub] | IO F0L0R0G0A0
- Last error: none

## Telemetry

- Servo feedback age (s): 0.4448575973510742
- Servo feedback pan/tilt: 187.38461538461536 / 81.6923076923077
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
[22:50:34] [SYSTEM] USB IO RX RECV: M1
[22:50:34] [SYSTEM] USB IO RX ACK S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=200 K=2 N=10 U=0 V=45 H=360 B=1 P=0
[22:50:34] [SYSTEM] USB IO RX RECV: F0L0R0G0A0
[22:50:34] [SAFETY] FIRE! Burst: 6
[22:50:34] [SAFETY] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=1 conf=0.89 active_track=1
[22:50:34] [SYSTEM] [PREVIEW] render_mode=full
[22:50:35] [SYSTEM] [PREVIEW] render_mode=busy-lite
[22:50:35] [SYSTEM] USB IO RX ACK S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=200 K=2 N=10 U=0 V=45 H=360 B=1 P=0
[22:50:35] [SYSTEM] USB IO RX STAT S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=200 K=2 N=10 U=0 V=45 H=360 B=1 P=0
[22:50:35] [SYSTEM] USB IO RX RECV: S0
[22:50:35] [SYSTEM] USB IO RX ACK S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=200 K=2 N=10 U=0 V=45 H=360 B=1 P=0
[22:50:35] [SYSTEM] USB IO RX RECV: M1
[22:50:35] [SYSTEM] USB IO RX ACK S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=200 K=2 N=10 U=0 V=45 H=360 B=1 P=0
[22:50:35] [SYSTEM] USB IO RX RECV: F0L0R0G0A0
[22:50:35] [SYSTEM] USB IO RX ACK S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=200 K=2 N=10 U=0 V=45 H=360 B=1 P=0
[22:50:35] [SYSTEM] USB IO RX RECV: S0
[22:50:35] [SYSTEM] USB IO RX ACK S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=200 K=2 N=10 U=0 V=45 H=360 B=1 P=0
[22:50:35] [SYSTEM] USB IO RX RECV: M1
[22:50:35] [SYSTEM] [PREVIEW] render_mode=full
[22:50:35] [CAMERA] Serial log exported: snapshots/serial_log_exports/sentry_v2_serial_log_20260429_225035.txt
```

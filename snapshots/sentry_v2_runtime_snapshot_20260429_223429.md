# SMART SENTRY V3.5.0 Runtime Snapshot

- Generated: 2026-04-29 22:34:29
- Engine state: ENGAGING
- Connection: ✅ Debug Board: COM31 (sub checksum)
✅ USB IO Board: COM27
- Camera: 0
- YOLO: [OK] Runtime ready: yolo11m.pt

## Exported Files

- JSON: snapshots/sentry_v2_runtime_snapshot_20260429_223429.json
- Markdown: snapshots/sentry_v2_runtime_snapshot_20260429_223429.md

## Engine

- Motion enabled: True
- Current pan/tilt: 189.06956682310945 / 80.39989973331214
- Guard pan/tilt: 140.0 / 82.0
- Queue length/index: 1 / 0
- Engage phase: precision
- Visible targets: 1
- Qualified count: 1
- Active no-fire mask: none
- Last reacquire note: fire stale pose -> precision

## Active Target

- Track ID: 5
- Class: person
- Score: 0.8491221933606267
- Aim pan/tilt: 189.4391869848901 / 80.41059218559218
- Burst count: 6

## Communications

- Connected: True
- Host managed: False
- Mode: Arduino Nano USB + Debug Board USB
- Trigger mode: Water (MOSFET)
- Last command: BUS P81 T80 @28ms [sub] | IO F0L0R0G0A0
- Last error: none

## Telemetry

- Servo feedback age (s): 0.42292261123657227
- Servo feedback pan/tilt: 188.43956043956044 / 81.0989010989011
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
[22:34:27] [SAFETY] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=5 conf=0.87 active_track=5
[22:34:27] [SYSTEM] [PREVIEW] render_mode=full
[22:34:27] [SYSTEM] USB IO RX STAT S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=2 N=10 U=0 V=45 H=360 B=1 P=0
[22:34:27] [SYSTEM] USB IO RX RECV: S0
[22:34:27] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=2 N=10 U=0 V=45 H=360 B=1 P=0
[22:34:27] [SYSTEM] USB IO RX RECV: M0
[22:34:27] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=2 N=10 U=0 V=45 H=360 B=1 P=0
[22:34:27] [SYSTEM] USB IO RX RECV: F1L0R0G0A0
[22:34:27] [SYSTEM] USB IO RX ACK S=0 M=0 F=1 L=0 R=0 G=0 A=0 J=120 K=2 N=10 U=0 V=45 H=360 B=1 P=0
[22:34:28] [SYSTEM] [PREVIEW] render_mode=busy-lite
[22:34:28] [SYSTEM] USB IO RX RECV: S0
[22:34:28] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=2 N=10 U=0 V=45 H=360 B=1 P=0
[22:34:28] [SYSTEM] USB IO RX RECV: M0
[22:34:28] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=2 N=10 U=0 V=45 H=360 B=1 P=0
[22:34:28] [SYSTEM] USB IO RX RECV: F0L0R0G0A0
[22:34:28] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=2 N=10 U=0 V=45 H=360 B=1 P=0
[22:34:28] [SYSTEM] USB IO RX STAT S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=2 N=10 U=0 V=45 H=360 B=1 P=0
[22:34:28] [SAFETY] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=5 conf=0.88 active_track=5
[22:34:28] [SYSTEM] [PREVIEW] render_mode=full
[22:34:29] [CAMERA] Serial log exported: snapshots/serial_log_exports/sentry_v2_serial_log_20260429_223429.txt
```

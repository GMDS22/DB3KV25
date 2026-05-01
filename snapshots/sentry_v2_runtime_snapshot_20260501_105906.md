# SMART SENTRY V3.5.1 Runtime Snapshot

- Generated: 2026-05-01 10:59:06
- Engine state: ENGAGING
- Connection: ✅ Debug Board: COM31 (sub checksum)
✅ USB IO Board: COM27
- Camera: 0
- YOLO: [OK] Runtime ready: yolo11m.pt

## Exported Files

- JSON: snapshots/sentry_v2_runtime_snapshot_20260501_105906.json
- Markdown: snapshots/sentry_v2_runtime_snapshot_20260501_105906.md

## Engine

- Motion enabled: True
- Current pan/tilt: 193.12087912087912 / 79.45054945054946
- Guard pan/tilt: 140.0 / 82.0
- Queue length/index: 1 / 0
- Engage phase: fire
- Visible targets: 1
- Qualified count: 1
- Active no-fire mask: none
- Last reacquire note: fire stale pose -> precision

## Active Target

- Track ID: 2
- Class: person
- Score: 0.8488107548968187
- Aim pan/tilt: 194.32257326007326 / 79.67462352462353
- Burst count: 6

## Communications

- Connected: True
- Host managed: False
- Mode: Arduino Nano USB + Debug Board USB
- Trigger mode: Water (MOSFET)
- Last command: BUS P77 T79 @31ms [sub] | IO F0L0R0G0A0
- Last error: none

## Telemetry

- Servo feedback age (s): 0.4435904026031494
- Servo feedback pan/tilt: 193.05494505494505 / 79.45054945054946
- IO runtime source: inactive
- IO runtime age (s): None
- Safety/mode: None / None
- Current fault: None
- Total current (mA): None

## Camera

- Capture open: False
- Source kind: 
- Source label: 0
- Requested resolution: 1920 x 1080
- Raw frame: {'width': 1920, 'height': 1080, 'channels': 3}
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

- settings_json: app/config/smart_sentry_v3_5_1_settings.json (exists=True)
- legacy_settings_json: app/config/sentry_v2_settings.json (exists=False)
- custom_master_presets: app/config/smart_sentry_v3_5_1_custom_presets.json (exists=False)
- prompted_target_library: app/config/smart_sentry_v3_5_1_prompted_targets.json (exists=False)
- snapshot_dir: snapshots (exists=True)
- selected_yolo_model: F:\SMART SENTRY V3.5.0\YOLO_MODELS\yolo11m.pt (exists=True)
- candidate_yolo_model_dirs: F:\SMART SENTRY V3.5.0\YOLO_MODELS, YOLO_MODELS, F:\SMART SENTRY_v2a\YOLO_MODELS

## Recent Log Lines

```text
[10:59:05] [SYSTEM] USB IO RX RECV: F0L0R0G0A0
[10:59:05] [SYSTEM] USB IO RX ACK S=1 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[10:59:05] [SYSTEM] [PREVIEW] render_mode=busy-lite
[10:59:05] [SYSTEM] USB IO RX RECV: S1
[10:59:05] [SYSTEM] USB IO RX ACK S=1 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[10:59:05] [SYSTEM] USB IO RX RECV: M0
[10:59:05] [SYSTEM] USB IO RX ACK S=1 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[10:59:05] [SYSTEM] USB IO RX RECV: F0L0R0G0A0
[10:59:05] [SYSTEM] USB IO RX ACK S=1 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[10:59:05] [SYSTEM] USB IO RX RECV: S1
[10:59:05] [SYSTEM] USB IO RX ACK S=1 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[10:59:05] [SYSTEM] USB IO RX RECV: M0
[10:59:05] [SYSTEM] USB IO RX ACK S=1 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[10:59:05] [SYSTEM] USB IO RX RECV: F1L0R0G0A0
[10:59:05] [SAFETY] USB IO RX WARN FIRE_BLOCKED_SAFETY S=1 (send S0 to arm)
[10:59:05] [SYSTEM] USB IO RX ACK S=1 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[10:59:05] [SAFETY] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=2 conf=0.86 active_track=2
[10:59:06] [SYSTEM] [PREVIEW] render_mode=full
[10:59:06] [SYSTEM] USB IO RX STAT S=1 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[10:59:06] [CAMERA] Serial log exported: snapshots/serial_log_exports/sentry_v2_serial_log_20260501_105906.txt
```

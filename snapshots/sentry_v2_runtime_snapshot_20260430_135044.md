# SMART SENTRY V3.5.0 Runtime Snapshot

- Generated: 2026-04-30 13:50:44
- Engine state: GUARDING
- Connection: ✅ Debug Board: COM31 (sub checksum)
✅ USB IO Board: COM27
- Camera: 0
- YOLO: [OK] Runtime ready: yolo11m.pt

## Exported Files

- JSON: snapshots/sentry_v2_runtime_snapshot_20260430_135044.json
- Markdown: snapshots/sentry_v2_runtime_snapshot_20260430_135044.md

## Engine

- Motion enabled: True
- Current pan/tilt: 139.1392936316484 / 70.80351100307702
- Guard pan/tilt: 140.0 / 82.0
- Queue length/index: 0 / 0
- Engage phase: precision
- Visible targets: 0
- Qualified count: 0
- Active no-fire mask: none
- Last reacquire note: none

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
- Last command: BUS P131 @28ms [sub] | IO F0L0R0G0A0
- Last error: none

## Telemetry

- Servo feedback age (s): 0.6947917938232422
- Servo feedback pan/tilt: 140.17582417582418 / 72.06593406593406
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
[13:50:42] [SYSTEM] USB IO RX STAT S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[13:50:43] [SYSTEM] [PREVIEW] render_mode=busy-lite
[13:50:43] [SYSTEM] USB IO RX RECV: SOUND:646:24:2
[13:50:43] [SYSTEM] USB IO RX ACK SOUND freq=646 duration=24 volume=2
[13:50:43] [SYSTEM] USB IO RX RECV: SOUND:742:24:2
[13:50:43] [SYSTEM] USB IO RX ACK SOUND freq=742 duration=24 volume=2
[13:50:43] [SYSTEM] USB IO RX RECV: SOUND:955:39:2
[13:50:43] [SYSTEM] USB IO RX ACK SOUND freq=955 duration=39 volume=2
[13:50:43] [SYSTEM] USB IO RX RECV: SOUND:736:124:2
[13:50:43] [SYSTEM] USB IO RX ACK SOUND freq=736 duration=124 volume=2
[13:50:43] [SYSTEM] USB IO RX RECV: S0
[13:50:43] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[13:50:43] [SYSTEM] USB IO RX RECV: M0
[13:50:43] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[13:50:43] [SYSTEM] USB IO RX RECV: F0L0R0G0A0
[13:50:43] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[13:50:43] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=GUARDING
[13:50:43] [SYSTEM] [PREVIEW] render_mode=full
[13:50:43] [SYSTEM] USB IO RX STAT S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[13:50:44] [CAMERA] Serial log exported: snapshots/serial_log_exports/sentry_v2_serial_log_20260430_135044.txt
```

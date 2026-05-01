# SMART SENTRY V3.5.0 Runtime Snapshot

- Generated: 2026-04-30 22:09:41
- Engine state: ENGAGING
- Connection: ✅ Debug Board: COM31 (sub checksum)
✅ USB IO Board: COM27
- Camera: 0
- YOLO: [OK] Runtime ready: yolo11m.pt

## Exported Files

- JSON: snapshots/sentry_v2_runtime_snapshot_20260430_220941.json
- Markdown: snapshots/sentry_v2_runtime_snapshot_20260430_220941.md

## Engine

- Motion enabled: True
- Current pan/tilt: 146.12825100678478 / 76.75552635825825
- Guard pan/tilt: 140.0 / 82.0
- Queue length/index: 1 / 0
- Engage phase: precision
- Visible targets: 1
- Qualified count: 1
- Active no-fire mask: none
- Last reacquire note: fire stale pose -> precision

## Active Target

- Track ID: 162
- Class: Prompted Target 7
- Score: 0.47486848820325206
- Aim pan/tilt: 155.39466002747253 / 70.84973544973545
- Burst count: 6

## Communications

- Connected: True
- Host managed: False
- Mode: Arduino Nano USB + Debug Board USB
- Trigger mode: Water (MOSFET)
- Last command: BUS P124 @28ms [sub] | IO F0L0R0G0A0
- Last error: none

## Telemetry

- Servo feedback age (s): 0.30042243003845215
- Servo feedback pan/tilt: 146.17582417582418 / 76.94505494505493
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

- settings_json: app/config/smart_sentry_v3_5_0_settings.json (exists=True)
- legacy_settings_json: app/config/sentry_v2_settings.json (exists=False)
- custom_master_presets: app/config/smart_sentry_v3_5_0_custom_presets.json (exists=True)
- prompted_target_library: app/config/smart_sentry_v3_5_0_prompted_targets.json (exists=True)
- snapshot_dir: snapshots (exists=True)
- selected_yolo_model: F:\SMART SENTRY V3.5.0\YOLO_MODELS\yolo11m.pt (exists=True)
- candidate_yolo_model_dirs: F:\SMART SENTRY V3.5.0\YOLO_MODELS, YOLO_MODELS, F:\SMART SENTRY_v2a\YOLO_MODELS

## Recent Log Lines

```text
[22:09:38] [SAFETY] FIRE! Burst: 6
[22:09:38] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=ENGAGING
[22:09:38] [SYSTEM] [PREVIEW] render_mode=full
[22:09:39] [SYSTEM] [PREVIEW] render_mode=busy-lite
[22:09:39] [SYSTEM] USB IO RX RECV: S0
[22:09:39] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[22:09:39] [SYSTEM] USB IO RX RECV: M0
[22:09:39] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[22:09:39] [SYSTEM] USB IO RX RECV: F0L0R0G0A0
[22:09:39] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[22:09:39] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=ENGAGING
[22:09:40] [SYSTEM] [PREVIEW] render_mode=full
[22:09:40] [SYSTEM] USB IO RX STAT S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[22:09:40] [SYSTEM] USB IO RX RECV: S0
[22:09:40] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[22:09:40] [SYSTEM] USB IO RX RECV: M0
[22:09:40] [SYSTEM] USB IO RX ACK S=0 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[22:09:40] [SYSTEM] USB IO RX RECV: F1L0R0G0A0
[22:09:40] [SYSTEM] USB IO RX ACK S=0 M=0 F=1 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[22:09:41] [CAMERA] Serial log exported: snapshots/serial_log_exports/sentry_v2_serial_log_20260430_220941.txt
```

# SMART SENTRY V3.5.1 Runtime Snapshot

- Generated: 2026-05-01 13:17:53
- Engine state: ENGAGING
- Connection: ✅ Debug Board: COM31 (sub checksum)
✅ USB IO Board: COM27
- Camera: 0
- YOLO: [OK] Runtime ready: yolo11m.pt

## Exported Files

- JSON: snapshots/sentry_v2_runtime_snapshot_20260501_131753.json
- Markdown: snapshots/sentry_v2_runtime_snapshot_20260501_131753.md

## Engine

- Motion enabled: True
- Current pan/tilt: 195.6263736263736 / 85.25274725274726
- Guard pan/tilt: 140.0 / 82.0
- Queue length/index: 1 / 0
- Engage phase: precision
- Visible targets: 1
- Qualified count: 1
- Active no-fire mask: none
- Last reacquire note: reacquire 22->23

## Active Target

- Track ID: 23
- Class: person
- Score: 0.7176961996413515
- Aim pan/tilt: 197.19878663003664 / 81.26066341066341
- Burst count: 6

## Communications

- Connected: True
- Host managed: False
- Mode: Arduino Nano USB + Debug Board USB
- Trigger mode: Projectile (ESP32 GPIO13 Servo)
- Last command: SOUND:728:33:2
- Last error: none

## Telemetry

- Servo feedback age (s): 0.41416025161743164
- Servo feedback pan/tilt: 195.6263736263736 / 85.25274725274726
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
- custom_master_presets: app/config/smart_sentry_v3_5_1_custom_presets.json (exists=True)
- prompted_target_library: app/config/smart_sentry_v3_5_1_prompted_targets.json (exists=False)
- snapshot_dir: snapshots (exists=True)
- selected_yolo_model: F:\SMART SENTRY V3.5.0\YOLO_MODELS\yolo11m.pt (exists=True)
- candidate_yolo_model_dirs: F:\SMART SENTRY V3.5.0\YOLO_MODELS, YOLO_MODELS, F:\SMART SENTRY_v2a\YOLO_MODELS

## Recent Log Lines

```text
[13:17:50] [SYSTEM] USB IO RX ACK S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=200 K=2 N=1336 U=0 V=45 H=720 B=1 P=0
[13:17:50] [SYSTEM] USB IO RX RECV: SOUND:737:34:2
[13:17:50] [SYSTEM] USB IO RX ACK SOUND freq=737 duration=34 volume=2
[13:17:51] [SYSTEM] USB IO RX STAT S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=200 K=2 N=1336 U=0 V=45 H=720 B=1 P=0
[13:17:51] [SYSTEM] [PREVIEW] render_mode=busy-lite
[13:17:51] [SAFETY] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=23 conf=0.76 active_track=23
[13:17:51] [SYSTEM] [PREVIEW] render_mode=full
[13:17:51] [SYSTEM] USB IO RX STAT S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=200 K=2 N=1336 U=0 V=45 H=720 B=1 P=0
[13:17:51] [SYSTEM] USB IO RX RECV: SOUND:656:26:2
[13:17:51] [SYSTEM] USB IO RX ACK SOUND freq=656 duration=26 volume=2
[13:17:51] [SYSTEM] USB IO RX RECV: S0
[13:17:51] [SYSTEM] USB IO RX ACK S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=200 K=2 N=1336 U=0 V=45 H=720 B=1 P=0
[13:17:52] [SYSTEM] USB IO RX RECV: M1
[13:17:52] [SYSTEM] USB IO RX ACK S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=200 K=2 N=1336 U=0 V=45 H=720 B=1 P=0
[13:17:52] [SYSTEM] USB IO RX RECV: F0L0R0G0A0
[13:17:52] [SYSTEM] USB IO RX ACK S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=200 K=2 N=1336 U=0 V=45 H=720 B=1 P=0
[13:17:52] [SYSTEM] USB IO RX RECV: SOUND:791:37:2
[13:17:52] [SYSTEM] USB IO RX ACK SOUND freq=791 duration=37 volume=2
[13:17:52] [SYSTEM] USB IO RX STAT S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=200 K=2 N=1336 U=0 V=45 H=720 B=1 P=0
[13:17:53] [CAMERA] Serial log exported: snapshots/serial_log_exports/sentry_v2_serial_log_20260501_131753.txt
```

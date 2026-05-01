# SMART SENTRY V3.5.0 Runtime Snapshot

- Generated: 2026-04-29 22:04:09
- Engine state: ENGAGING
- Connection: ✅ Debug Board: COM31 (sub checksum)
✅ USB IO Board: COM27
- Camera: 0
- YOLO: [OK] Runtime ready: yolo11m.pt

## Exported Files

- JSON: snapshots/sentry_v2_runtime_snapshot_20260429_220409.json
- Markdown: snapshots/sentry_v2_runtime_snapshot_20260429_220409.md

## Engine

- Motion enabled: True
- Current pan/tilt: 188.30769230769232 / 84.0
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
- Score: 0.3894227315286682
- Aim pan/tilt: 203.43339170406657 / 83.63547296704073
- Burst count: 6

## Communications

- Connected: True
- Host managed: False
- Mode: Arduino Nano USB + Debug Board USB
- Trigger mode: Projectile (ESP32 GPIO13 Servo)
- Last command: BUS P81 T84 @20ms [sub] | IO F0L0R0G0A0
- Last error: none

## Telemetry

- Servo feedback age (s): 0.2678351402282715
- Servo feedback pan/tilt: 187.38461538461536 / 84.0
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
[22:04:08] [SYSTEM] USB IO RX ACK S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[22:04:08] [SYSTEM] [PREVIEW] render_mode=busy-lite
[22:04:08] [SYSTEM] USB IO RX STAT S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[22:04:08] [SYSTEM] USB IO RX RECV: S0
[22:04:08] [SYSTEM] USB IO RX ACK S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[22:04:08] [SYSTEM] USB IO RX RECV: M1
[22:04:08] [SYSTEM] USB IO RX ACK S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[22:04:08] [SYSTEM] USB IO RX RECV: F0L0R0G0A0
[22:04:08] [SYSTEM] USB IO RX ACK S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[22:04:08] [SAFETY] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=1 conf=0.91 active_track=1
[22:04:09] [SYSTEM] [PREVIEW] render_mode=full
[22:04:09] [SYSTEM] [PREVIEW] render_mode=busy-lite
[22:04:09] [ACCESSORY] [PREVIEW] render_mode=throttled
[22:04:09] [SYSTEM] USB IO RX RECV: S0
[22:04:09] [SYSTEM] USB IO RX ACK S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[22:04:09] [SYSTEM] USB IO RX RECV: M1
[22:04:09] [SYSTEM] USB IO RX ACK S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[22:04:09] [SYSTEM] USB IO RX RECV: F0L0R0G0A0
[22:04:09] [SYSTEM] USB IO RX ACK S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[22:04:09] [SYSTEM] USB IO RX STAT S=0 M=1 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
```

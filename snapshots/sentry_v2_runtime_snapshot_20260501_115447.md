# SMART SENTRY V3.5.1 Runtime Snapshot

- Generated: 2026-05-01 11:54:47
- Engine state: ENGAGING
- Connection: ✅ Debug Board: COM31 (sub checksum)
✅ USB IO Board: COM27
- Camera: 0
- YOLO: [OK] Runtime ready: yolo11m.pt

## Exported Files

- JSON: snapshots/sentry_v2_runtime_snapshot_20260501_115447.json
- Markdown: snapshots/sentry_v2_runtime_snapshot_20260501_115447.md

## Engine

- Motion enabled: True
- Current pan/tilt: 192.53004309156339 / 80.09261977002512
- Guard pan/tilt: 140.0 / 82.0
- Queue length/index: 1 / 0
- Engage phase: fire
- Visible targets: 1
- Qualified count: 1
- Active no-fire mask: none
- Last reacquire note: stationary release active t1 (2.4s)

## Active Target

- Track ID: 1
- Class: person
- Score: 0.8137968249197699
- Aim pan/tilt: 199.6847870879121 / 80.990638990639
- Burst count: 6

## Communications

- Connected: True
- Host managed: False
- Mode: Arduino Nano USB + Debug Board USB
- Trigger mode: Water (MOSFET)
- Last command: BUS P77 T80 @20ms [sub] | IO F1L0R0G0A0
- Last error: none

## Telemetry

- Servo feedback age (s): 0.33627843856811523
- Servo feedback pan/tilt: 193.31868131868134 / 80.17582417582418
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
[11:54:45] [SAFETY] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=1 conf=0.88 active_track=1
[11:54:45] [SYSTEM] [PREVIEW] render_mode=full
[11:54:45] [SYSTEM] USB IO RX ACK S=1 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[11:54:45] [SYSTEM] USB IO RX RECV: M0
[11:54:45] [SYSTEM] USB IO RX ACK S=1 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[11:54:46] [SYSTEM] USB IO RX RECV: F1L0R0G0A0
[11:54:46] [SAFETY] USB IO RX WARN FIRE_BLOCKED_SAFETY S=1 (send S0 to arm)
[11:54:46] [SYSTEM] USB IO RX ACK S=1 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[11:54:46] [SYSTEM] [PREVIEW] render_mode=busy-lite
[11:54:46] [SYSTEM] USB IO RX STAT S=1 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[11:54:46] [SYSTEM] USB IO RX RECV: S1
[11:54:46] [SYSTEM] USB IO RX ACK S=1 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[11:54:46] [SYSTEM] USB IO RX RECV: M0
[11:54:46] [SYSTEM] USB IO RX ACK S=1 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[11:54:46] [SYSTEM] USB IO RX RECV: F0L0R0G0A0
[11:54:46] [SYSTEM] USB IO RX ACK S=1 M=0 F=0 L=0 R=0 G=0 A=0 J=120 K=1 N=50 U=0 V=45 H=360 B=0 P=0
[11:54:46] [SAFETY] FIRE! Burst: 6
[11:54:46] [SAFETY] [TRACKDBG] person pipeline: visible=1 qualified=1 engaged=1 state=ENGAGING lead_track=1 conf=0.88 active_track=1
[11:54:46] [SYSTEM] [PREVIEW] render_mode=full
[11:54:47] [CAMERA] Serial log exported: snapshots/serial_log_exports/sentry_v2_serial_log_20260501_115447.txt
```

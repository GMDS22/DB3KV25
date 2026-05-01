# SMART SENTRY V3.5.0 Runtime Snapshot

- Generated: 2026-04-27 12:10:42
- Engine state: GUARDING
- Connection: ✅ Debug Board: COM31 (sub checksum)
✅ USB IO Board: COM28
- Camera: 0
- YOLO: [OK] Runtime ready: yolo11m.pt

## Exported Files

- JSON: snapshots/sentry_v2_runtime_snapshot_20260427_121042.json
- Markdown: snapshots/sentry_v2_runtime_snapshot_20260427_121042.md

## Engine

- Motion enabled: True
- Current pan/tilt: 139.84615384615384 / 71.14285714285714
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
- Last command: BUS hold P131 T70 @131ms [sub] | IO F0L0R0G0A0
- Last error: none

## Telemetry

- Servo feedback age (s): 0.8332254886627197
- Servo feedback pan/tilt: 139.84615384615384 / 71.14285714285714
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
[12:10:40] [SYSTEM] USB IO RX 5)1
%
[12:10:40] [SYSTEM] USB IO RX -s
5!l-
[12:10:40] [SYSTEM] [PREVIEW] render_mode=busy-lite
[12:10:40] [ACCESSORY] [PREVIEW] render_mode=throttled
[12:10:40] [SYSTEM] [PREVIEW] render_mode=busy-lite
[12:10:40] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=GUARDING
[12:10:40] [ACCESSORY] [PREVIEW] render_mode=throttled
[12:10:41] [SYSTEM] [PREVIEW] render_mode=busy-lite
[12:10:41] [ACCESSORY] [PREVIEW] render_mode=throttled
[12:10:41] [SYSTEM] [PREVIEW] render_mode=busy-lite
[12:10:41] [ACCESSORY] [PREVIEW] render_mode=throttled
[12:10:41] [SYSTEM] [PREVIEW] render_mode=busy-lite
[12:10:41] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=GUARDING
[12:10:41] [ACCESSORY] [PREVIEW] render_mode=throttled
[12:10:41] [SYSTEM] [PREVIEW] render_mode=busy-lite
[12:10:42] [ACCESSORY] [PREVIEW] render_mode=throttled
[12:10:42] [SYSTEM] [PREVIEW] render_mode=busy-lite
[12:10:42] [ACCESSORY] [PREVIEW] render_mode=throttled
```

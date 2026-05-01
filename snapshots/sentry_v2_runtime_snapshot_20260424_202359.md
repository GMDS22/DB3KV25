# Smart Sentry V3.0.0 Runtime Snapshot

- Generated: 2026-04-24 20:23:59
- Engine state: GUARDING
- Connection: ✅ Debug Board: COM31 (sub checksum)
✅ ESP32 WiFi: 192.168.4.1:9000
- Camera: 0
- YOLO: [OK] Runtime ready: yolo11m.pt

## Exported Files

- JSON: snapshots/sentry_v2_runtime_snapshot_20260424_202359.json
- Markdown: snapshots/sentry_v2_runtime_snapshot_20260424_202359.md

## Engine

- Motion enabled: True
- Current pan/tilt: 140.94792277009677 / 80.00904831146941
- Guard pan/tilt: 140.0 / 82.0
- Queue length/index: 1 / 1
- Engage phase: precision
- Visible targets: 0
- Qualified count: 0
- Active no-fire mask: none
- Last reacquire note: persistent pursuit

## Active Target

- Track ID: none
- Class: none
- Score: none
- Aim pan/tilt: None / None
- Burst count: None

## Communications

- Connected: True
- Host managed: False
- Mode: ESP32 WiFi + Debug Board USB
- Trigger mode: Water (MOSFET)
- Last command: UDP IO F0L255R0S0M0A0P0 | UDP IO F0L255R0A0P0
- Last error: none

## Telemetry

- Servo feedback age (s): 2.0081377029418945
- Servo feedback pan/tilt: 148.68131868131866 / 76.41758241758241
- IO runtime source: esp32-state
- IO runtime age (s): 0.021060466766357422
- Safety/mode: 0 / 0
- Current fault: False
- Total current (mA): 0

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
- Selected model path: F:\SMART SENTRY V3.0.0\YOLO_MODELS\yolo11m.pt
- Loaded model path: F:\SMART SENTRY V3.0.0\YOLO_MODELS\yolo11m.pt
- Detector loaded: True
- Allowed classes: person
- Confidence/min area: 0.44 / 1200

## External Files

- settings_json: app/config/smart_sentry_v3_0_0_settings.json (exists=True)
- legacy_settings_json: app/config/sentry_v2_settings.json (exists=False)
- custom_master_presets: app/config/smart_sentry_v3_0_0_custom_presets.json (exists=True)
- prompted_target_library: app/config/smart_sentry_v3_0_0_prompted_targets.json (exists=True)
- snapshot_dir: snapshots (exists=True)
- selected_yolo_model: F:\SMART SENTRY V3.0.0\YOLO_MODELS\yolo11m.pt (exists=True)
- candidate_yolo_model_dirs: F:\SMART SENTRY V3.0.0\YOLO_MODELS, YOLO_MODELS, F:\SMART SENTRY V2\YOLO_MODELS

## Recent Log Lines

```text
[20:23:54] [SYSTEM] [PREVIEW] render_mode=busy-lite
[20:23:54] [SAFETY] [TRACKDBG] person pipeline: visible=1 qualified=0 engaged=0 state=GUARDING lead_track=17 conf=0.57 reason=semantic_confirm_pending (confirm=1/2 conf=0.57)
[20:23:54] [SYSTEM] [PREVIEW] render_mode=full
[20:23:54] [PIR] ESP32 UDP ACK safety=ARMED mode=WATER pir=OFF fault=CLEAR ctrl=app
[20:23:55] [SYSTEM] [PREVIEW] render_mode=busy-lite
[20:23:55] [PIR] ESP32 UDP ACK safety=ARMED mode=WATER pir=OFF fault=CLEAR ctrl=app
[20:23:55] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=GUARDING
[20:23:56] [SYSTEM] [PREVIEW] render_mode=full
[20:23:56] [SYSTEM] [PREVIEW] render_mode=busy-lite
[20:23:56] [PIR] ESP32 UDP STATE safety=ARMED mode=WATER pir=OFF fault=CLEAR ctrl=app
[20:23:56] [PIR] ESP32 UDP ACK safety=ARMED mode=WATER pir=OFF fault=CLEAR ctrl=app
[20:23:57] [SAFETY] [TRACKDBG] person pipeline: visible=1 qualified=0 engaged=0 state=GUARDING lead_track=17 conf=0.58 reason=semantic_confirm_pending (confirm=1/2 conf=0.58)
[20:23:57] [ACCESSORY] [PREVIEW] render_mode=throttled
[20:23:57] [SYSTEM] [PREVIEW] render_mode=busy-lite
[20:23:58] [PIR] ESP32 UDP ACK safety=ARMED mode=WATER pir=OFF fault=CLEAR ctrl=app
[20:23:58] [SAFETY] [TRACKDBG] person pipeline: visible=1 qualified=0 engaged=0 state=GUARDING lead_track=17 conf=0.69 reason=semantic_confirm_pending (confirm=1/2 conf=0.69)
[20:23:58] [SYSTEM] [PREVIEW] render_mode=full
[20:23:58] [SYSTEM] [PREVIEW] render_mode=busy-lite
[20:23:59] [SAFETY] [TRACKDBG] person pipeline: visible=0 qualified=0 engaged=0 state=GUARDING
[20:23:59] [SYSTEM] [PREVIEW] render_mode=full
```

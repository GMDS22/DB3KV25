# SMART SENTRY V2 — COMPLETE REFERENCE MANUAL

> **Version:** 2.3.2  
> **Module Path:** `app/sentry_v2/`  
> **Last Updated:** 2026-04-08  
> **Status:** Verified against the current standalone Smart Sentry v2.3.2 implementation. The canonical runtime settings file is `app/config/smart_sentry_v2_3_2_settings.json`; older settings paths remain compatibility fallbacks only. The live UI now includes the rest-position workflow, visible `Wake Up` / `Go Rest` controls, smooth guided home/rest motion tuning, procedural sound with transport-aware status, read-only runtime/log export actions, adaptive after-target-loss recovery, hidden Shift+wheel panel zoom, and PIR cue confirmation that immediately advances into an offset search when no target is found at the cue point.

---

## TABLE OF CONTENTS

1. [Architecture Overview](#1-architecture-overview)
2. [File Reference](#2-file-reference)
3. [Connection System](#3-connection-system)
4. [Detection Pipeline](#4-detection-pipeline)
5. [Target Processing](#5-target-processing)
6. [Engine State Machine](#6-engine-state-machine)
7. [Overlay / HUD](#7-overlay--hud)
8. [Configuration Reference](#8-configuration-reference)
9. [UI Tab Layout](#9-ui-tab-layout)
10. [Protocol Reference](#10-protocol-reference)
11. [Data Flow Diagrams](#11-data-flow-diagrams)
12. [Change Impact Map](#12-change-impact-map)
13. [Copilot / AI Agent Instructions](#13-copilot--ai-agent-instructions)
14. [Troubleshooting](#14-troubleshooting)
15. [Verified Improvement Plan](#15-verified-improvement-plan)
16. [Developer Checklist](#16-developer-checklist)
17. [Documentation Workflow](#17-documentation-workflow)

---

## 1. ARCHITECTURE OVERVIEW

Smart Sentry v2 is a standalone turret control application launched from the DB3000 launcher. Its **detection logic**, **serial/UDP communication**, **camera ownership**, and **state machine** are self-contained inside `app/sentry_v2/`.

- **Standalone camera ownership:** Smart Sentry opens and owns its own camera or stream source
- **Separate runtime settings:** Smart Sentry persists to `app/config/smart_sentry_v2_3_2_settings.json` and mirrors older files only for compatibility
- **One-app-at-a-time workflow:** Smart Sentry and the main app may use the same COM values, but never at the same time

On single-camera systems, Smart Sentry should normally use camera index `0` unless the operator explicitly selects another camera or stream source.

### Recent Verified Standalone Upgrades

- **Quick startup policy:** launch defers auto camera open and auto-connect, then performs a later lazy YOLO auto-load so startup stays responsive without leaving YOLO permanently unloaded
- **Sound system:** procedural non-blocking buzzer cues now route through `sound_engine.py` and `SentryV2Comm` with transport-aware status and persisted volume
- **Voice output modes:** Smart Sentry now supports both robot buzzer cues and optional human-like local speech through Qt text-to-speech, so identity alerts and assistant replies can use either path or both together
- **Runtime diagnostics:** the status area now includes pinned hardware-monitor cards plus a live sound-link readout
- **Runtime data export:** the Controls page can write timestamped JSON and Markdown runtime captures under the repo snapshot folder and expose a direct open-folder action for the saved files
- **Operator expansion:** the live settings surface now includes Facial Recognition, Shortcut Keys, and AI Assistant tabs plus a pinned top-row `Quick Keys` action
- **Known-face support:** Smart Sentry can now load and persist a lightweight face library, register new identities from images or the current live frame, label recognized faces in the preview, and optionally keep friendly known faces out of the engagement path
- **Settings compatibility:** the canonical runtime settings file remains authoritative while the legacy nested settings file is kept synchronized for compatibility

### Verified Current Integration Notes

- **Current standalone implementation:** Smart Sentry v2 is no longer hosted inside the main app and no longer depends on pushed main-app frames.
- **Current own-camera implementation:** Smart Sentry opens its configured camera source itself and runs its full internal detector pipeline on that feed.
- **Current protected baseline:** the live visual-servo controller, precision refinement, motion suppression, and fire-gating behavior are the preserved baseline and should only change for measured improvement.

### Module Philosophy

- **Independent sentry logic:** No reliance on main app detection or serial ports
- **Single owned video source:** Smart Sentry owns one configured camera/stream source at a time
- **Self-contained pipeline:** Camera → Detection → Filter → Score → Plan → Engage → Fire
- **Pluggable connection modes:** 5 hardware topologies supported
- **11 detection modes:** From simple motion to YOLO + color hybrids
- **4 guard patrol modes:** Static, sweep, waypoint, random scan
- **Precision PID aiming:** Closed-loop refinement before firing

### Component Dependency Map

```
SentryV2TabWidget (UI host)
├── SentryV2Config        (all settings, persistence)
├── SentryV2Comm          (serial/UDP/bus-servo I/O)
├── SentryV2Detector      (frame analysis, 11 modes)
├── FaceIdentityRuntime   (Haar-based face detection + lightweight embeddings)
├── SentryV2Engine        (state machine, engagement logic)
│   ├── TargetFilter      (class/size/zone filtering)
│   ├── ThreatScorer      (multi-factor threat ranking)
│   └── EngagementPlanner (queue ordering, pixel→pan/tilt)
├── SentryV2SoundEngine   (non-blocking procedural tone scheduling)
├── SentryV2VideoCanvas   (interactive video/status display surface)
└── SentryV2Overlay       (HUD drawing on frame)
```

### Per-Frame Pipeline

```
Camera Timer (30fps)
    │
    ▼
_grab_frame()
    │  cap.read() → BGR frame
    │  detector.detect(frame, mode) → [(x,y,w,h,score,class_id), ...]
    │
    ▼
process_frame(frame, raw_boxes)
   │  _raw_detections_to_objects() → [DetectedObject, ...]
   │  _apply_face_identity_to_objects() → friendly labels + optional engagement suppression
   │  engine.update(det_objects, timestamp)
    │      │  TargetFilter.filter() → qualified
    │      │  ThreatScorer.score() → sorted TrackedTargets
    │      │  State-specific logic (guard/engage/return)
    │      │  → cb_move(pan, tilt) → SentryV2Comm.send_command()
    │      │  → cb_fire(burst)     → SentryV2Comm.send_fire_burst()
    │
    ▼
overlay.draw(frame, engine)
    │  Engagement zone, crosshair, targets, reticle, state badge
    │
    ▼
_show_frame(frame) → QLabel.setPixmap()
```

---

## 2. FILE REFERENCE

### `__init__.py` (16 lines)
Package root. Exports the primary Smart Sentry v2 runtime classes and defines `__version__ = "2.0.0"`.

**Exports:** `SentryV2Config`, `SentryV2Engine`, `SentryV2State`, `SentryV2Comm`, `SentryV2Detector`, `TargetFilter`, `DetectedObject`, `ThreatScorer`, `TrackedTarget`, `EngagementPlanner`, `EngagementOrder`, `SentryV2Overlay`, `SentryV2TabWidget`

---

### `sentry_v2_config.py` (~280 lines)
All configuration in `@dataclass` structures with JSON save/load.

**Classes:**
| Class | Purpose | Key Fields |
|---|---|---|
| `DetectionModeConfig` | Detection algorithm settings | `detection_mode`, contour area, YOLO area, color preset, custom HSV, motion gate |
| `TargetFilterConfig` | Class/size/zone filtering | `allowed_classes`, `class_priority`, `min_confidence`, `engagement_zone` |
| `ThreatScoringConfig` | Threat score weights | 7 weights (proximity, size, confidence, class, speed, persistence, approach) |
| `EngagementConfig` | Fire/trigger/timing | `min_threat_score`, burst settings, cooldowns, PID gains, auto-trigger, adaptive after-loss recovery tuning |
| `GuardConfig` | Guard, rest, patrol, and guided move behavior | `guard_pan/tilt`, `rest_pan/tilt`, startup/close rest timing, home/rest move speeds, FOV, 4 guard modes, sweep/waypoint/random params |
| `SoundConfig` | Procedural and spoken audio behavior | buzzer enable, human voice enable, voice selection, voice rate/pitch/volume, rest cues, identity announce cooldown |
| `FaceRecognitionConfig` | Known-face runtime rules | enable, library path, threshold, min size, friendly suppression, announce, gesture |
| `AIAssistantConfig` | In-app assistant controls | enable, mode, mode switching, runtime analysis, setting drafts |
| `ShortcutConfig` | Operator hotkey runtime | enabled flag and quick-reference document path |
| `ConnectionConfig` | Hardware topology | `connection_type`, ports/bauds, UDP host/port, servo IDs, camera, inversions |
| `SentryV2Config` | Top-level container | All sub-configs + overlay flags + `save()`/`load()` |

**Persistence:** `app/config/smart_sentry_v2_3_2_settings.json` (canonical runtime file, auto-created). Compatibility fallbacks and mirrors may also exist at `app/config/smart_sentry_v2_3_1_settings.json`, `app/config/smart_sentry_v3_settings.json`, and `app/config/sentry_v2_settings.json`, but those are not the authoritative live file.

---

### `sentry_v2_tab.py` (~10k+ lines)
The main QWidget that hosts all UI tabs and orchestrates the pipeline.

**Class:** `SentryV2TabWidget(QWidget)`

**Signals:**
| Signal | Type | When Emitted |
|---|---|---|
| `sentry_enabled_changed` | `pyqtSignal(bool)` | Enable checkbox toggled |
| `detection_mode_changed` | `pyqtSignal(int)` | Detection mode combo changed |
| `color_preset_changed` | `pyqtSignal(str)` | Color preset combo changed |

**Key Internal Objects:**
- `self.config` — `SentryV2Config`
- `self._comm` — `SentryV2Comm` (standalone communication)
- `self._detector` — `SentryV2Detector` (standalone detection)
- `self.engine` — `SentryV2Engine` (state machine)
- `self.overlay` — `SentryV2Overlay` (HUD)
- `self._cap` — `cv2.VideoCapture` (own camera)
- `self._cam_timer` — `QTimer` (frame grab at ~30fps)

**UI Tabs Built:**
1. **Connection** — Port selection, connection modes, camera controls, servo settings
2. **Master Profiles** — high-level preset families and profile application
3. **Detection** — Mode selector, YOLO model loader, contour/color/motion settings
4. **Prompted Targets** — prompted-target library and guided target matching tools
5. **Target Filter** — Class whitelist, confidence threshold, size filter, engagement zone
6. **Threat AI** — threat-weight tuning and optional ML refinement controls
7. **Engage** — Burst/cooldown/PID settings, auto-trigger, trigger mode, aim-lock presets, After Target Loss recovery tuning
8. **Guard** — Guard position, rest position, startup/close rest behavior, PIR guard controls, patrol mode, sweep/waypoint/random parameters, guided home/rest motion tuning
9. **Theme** — visual preset selection plus live accent, transparency, contrast, radius, and contrast tuning; panel font zoom remains supported through the hidden Shift+wheel shortcut rather than a visible slider
10. **Controls** — Manual pan/tilt matrix, visible `Wake Up` / `Go Rest` actions, sound controls, runtime data export and open-folder actions, LED/laser/safety toggles
11. **Facial Recognition** — known-face library controls, image and live-frame registration, friendly-face behavior, runtime thresholding, and recognition testing
12. **Shortcut Keys** — live shortcut status, assigned key summary, and quick-reference access
13. **AI Assistant** — rule-based diagnostics, request input, runtime analysis, and safe recommendation tools

**Verified current layout note:** the live UI currently renders 13 icon-forward settings tabs inside a full-height right-side panel, with a pinned header and top-row `Quick Keys` button above the tabs and compact Status/Log areas below the video rather than as separate tabs.

**Verified current runtime note:** the Controls page now includes persisted Sound ON/OFF and volume controls, visible `Wake Up` / `Go Rest` buttons, read-only runtime data export controls, and an open-folder shortcut for saved exports, while the Status area surfaces live sound-link transport state alongside the hardware monitor. The Serial Output panel now also supports timestamped log export plus a direct open-folder action for AI analysis and troubleshooting.

**Verified current identity note:** the Facial Recognition page persists its face library separately at `app/config/smart_sentry_v2_3_2_faces.json`, uses Haar-cascade face detection plus lightweight DCT and histogram embeddings, and can either label friendly known faces only or keep them out of the engagement stream entirely when that protection is enabled. Recognized names can be announced through the buzzer, the local human voice engine, or both, but the current Controls contract now also supports muting the ESP32 buzzer automatically while human voice mode is enabled so those outputs do not overlap.

**Verified current shortcut note:** the top-row `Quick Keys` button and the Shortcut Keys tab both point operators to `SMART_SENTRY_SHORTCUT_KEYS.md`, and the live shortcut runtime stays window-focused so hotkeys only fire while the Smart Sentry window is active.

**Verified current AI assistant note:** the AI Assistant tab is now a local rule-based assistant surface, not a cloud LLM client. It can summarize runtime state, draft simple recommendations, and apply a small set of safe operator actions from text requests, including home or rest moves, shortcut toggling, face-recognition toggling, and detection-mode changes. In `Conversational Voice` mode it can also speak replies through the local human voice engine, and the color-detection request path now maps to the real Color Detection mode instead of the older hybrid index.

**Verified current Threat AI note:** the Threat AI page now shows saved-data and model status text, exposes an `Open ML Folder` action only when real saved data or model artifacts exist, and includes an operator-facing description of how logged training examples and optional ML refinement interact with the weighted threat scorer.

**Verified current command-status note:** the Connection page still shows the latest manual or operator-scale command result, but automatic tracking moves no longer overwrite that label every frame, so status remains readable during active tracking.

**Verified current loss-recovery note:** when a tracked target drops out, Smart Sentry now captures loss context and chooses between two bounded recovery protocols. `rapid_handoff_search` favors quick transfer toward a stronger visible candidate in crowded scenes, while `persistent_reacquire_search` spends more effort searching around the last known position in sparse scenes. In fixed guard mode, recovery still remains bounded and ends in a return to the configured guard position instead of lingering off-home.

**Runtime export note:** the runtime data export path is intentionally observational only. It records the active runtime state for diagnostics and future AI analysis, but it must not alter the live detector, engine, transport, or firing logic. See `SMART_SENTRY_RUNTIME_DATA_EXPORT.md` for the export contract and guardrails.

---

### `sentry_v2_detector.py` (~280 lines)
Standalone multi-mode detector. No dependency on main app detection code.

**Class:** `SentryV2Detector`

**Input:** BGR `np.ndarray` frame + mode index  
**Output:** `List[Tuple[int, int, int, int, float, int]]` — `(x, y, w, h, score, class_id)`

**11 Detection Modes:**

| Index | Name | Algorithm |
|---|---|---|
| 0 | Frame Difference | `absdiff` → gray → blur → threshold → dilate → contours |
| 1 | Background Subtraction | `MOG2` (30-frame warmup) → threshold → contours |
| 2 | YOLO Object Detection | `ultralytics` YOLO model → filtered by class + confidence |
| 3 | Hybrid: Diff + BackSub | Union of modes 0 and 1 |
| 4 | Hybrid: Diff + YOLO | Frame diff motion gate → YOLO on motion frames only |
| 5 | Hybrid: BackSub + YOLO | BackSub motion gate → YOLO on motion frames only |
| 6 | Color Detection | HSV `inRange` → morphology → contours. Named presets retry with a small saturation/value tolerance so moderate shading still reads as the selected color. |
| 7 | Hybrid: Color + Diff | Color mask + frame diff. With a specific color preset, the motion box must overlap the selected color. |
| 8 | Hybrid: Color + BackSub | Color mask + foreground motion. With a specific color preset, the foreground box must overlap the selected color. |
| 9 | Hybrid: Color + YOLO | Color mask + YOLO. With a specific color preset, the YOLO box must overlap the selected color; `OR` fallback only applies when the preset is `any`. |
| 10 | Filtered Target Mode | Motion-locked filtered mode: merges frame diff + backsub motion, optionally gates on color, prefers overlapping YOLO boxes for aim stability, and falls back to `moving_object` when no class box is present. |

**Color Presets (HSV ranges):**

| Preset | H Range | S Range | V Range |
|---|---|---|---|
| red | 0–10 + 160–179 | 100–255 | 100–255 |
| orange | 10–25 | 100–255 | 100–255 |
| yellow | 25–35 | 100–255 | 100–255 |
| green | 35–85 | 100–255 | 100–255 |
| blue | 85–130 | 100–255 | 100–255 |
| purple | 130–160 | 100–255 | 100–255 |
| cyan | 80–100 | 100–255 | 100–255 |
| white | 0–179 | 0–40 | 200–255 |
| black | 0–179 | 0–255 | 0–40 |
| custom | User-defined | User-defined | User-defined |

---

### `sentry_v2_comm.py` (~450 lines)
Standalone 4-mode serial/UDP/bus-servo communication.

**Class:** `SentryV2Comm`

See [Section 3: Connection System](#3-connection-system) for full details.

---

### `sound_engine.py` (~230 lines)
Non-blocking procedural sound scheduler used by the standalone UI.

**Class:** `SentryV2SoundEngine`

**Responsibilities:**
- Queue short tone phrases without blocking the UI or comm worker
- Apply per-event cooldowns for settings, detection, lock, fire, guard, and PIR cues
- Encode short robotic identity phrases for recognized names on the same buzzer transport
- Keep transport details out of the UI by emitting abstract tone requests only

---

### `face_identity.py` (~250 lines)
Standalone known-face helper for the Smart Sentry runtime.

**Classes:**
- `FaceIdentityProfile` — persisted identity profile with embeddings and friendly-behavior flags
- `FaceMatchResult` — one recognition result for the current frame
- `FaceIdentityLibrary` — JSON-backed face-profile storage
- `FaceIdentityRuntime` — Haar-cascade face finder and embedding matcher

**Responsibilities:**
- Persist the face library independently of the main settings JSON
- Register known faces from imported images or a live frame snapshot
- Match faces without requiring the unavailable `cv2.face` contrib package
- Keep the recognition runtime light enough for the current portable environment

---

### `sentry_v2_video_canvas.py` (~200 lines)
Interactive video canvas used for the main preview and prompted-target workflows.

**Class:** `SentryV2VideoCanvas`

**Responsibilities:**
- Display scaled live or static pixmaps with consistent aspect handling
- Support placeholder imagery/text when the camera is closed
- Provide an interactive canvas surface for prompted-target selection flows

---

### `sentry_v2_engine.py` (~550 lines)
Core state machine driving the turret autonomously.

**Class:** `SentryV2Engine`

See [Section 6: Engine State Machine](#6-engine-state-machine) for full details.

---

### `sentry_v2_overlay.py` (~210 lines)
HUD rendering on the video frame.

**Class:** `SentryV2Overlay`

See [Section 7: Overlay / HUD](#7-overlay--hud) for full details.

---

### `target_filter.py` (~120 lines)
Filters raw detections by class, confidence, size, and engagement zone.

**Classes:**
- `DetectedObject` (`@dataclass`) — Standard detection format used throughout the pipeline
- `TargetFilter` — Applies all filter criteria, returns qualifying detections

**DetectedObject Fields:**
| Field | Type | Description |
|---|---|---|
| `track_id` | `int` | Sequential ID (from detector output order) |
| `class_name` | `str` | YOLO class name or "unknown" |
| `confidence` | `float` | 0.0–1.0 |
| `bbox` | `(x, y, w, h)` | Pixel bounding box |
| `center_x` | `float` | Pixel center X |
| `center_y` | `float` | Pixel center Y |
| `frame_width` | `int` | Frame width for normalization |
| `frame_height` | `int` | Frame height for normalization |
| `identity_label` | `str` | Recognized person name, if known |
| `identity_confidence` | `float` | Recognition confidence for the matched identity |
| `identity_profile_id` | `str` | Back-reference to the saved face profile |
| `friendly_identity` | `bool` | Whether this identity is marked friendly/family-safe |

**Computed Properties:** `area_ratio`, `norm_cx`, `norm_cy`

**Filter Criteria Applied (in order):**
1. Class name in `allowed_classes` list
2. Confidence ≥ `min_confidence`
3. Size ratio ≥ `min_size_ratio`
4. Size ratio ≤ `max_size_ratio` (if > 0)
5. Center inside `engagement_zone` rectangle

---

### `threat_scorer.py` (~200 lines)
Multi-factor threat scoring with temporal tracking.

**Classes:**
- `TrackedTarget` (`@dataclass`) — DetectedObject + threat metadata
- `ThreatScorer` — Scores and ranks detections

**TrackedTarget Extra Fields:**
| Field | Type | Description |
|---|---|---|
| `threat_score` | `float` | 0.0–1.0 composite score |
| `speed` | `float` | pixels/second |
| `heading_x` | `float` | Normalized velocity X |
| `heading_y` | `float` | Normalized velocity Y |
| `persistence` | `float` | Seconds since first seen |
| `approach_rate` | `float` | Closing speed (positive = approaching center) |

**Scoring Formula:**
```
threat = w_proximity × (1 - distance_from_center)
       + w_size       × area_ratio
       + w_confidence  × confidence
       + w_class       × class_priority_normalized
       + w_speed       × speed_normalized
       + w_persistence × persistence_normalized
       + w_approach    × approach_rate_normalized
```

Default weights: proximity=0.25, size=0.15, confidence=0.10, class=0.20, speed=0.10, persistence=0.10, approach=0.10

**History:** Maintains per-track position history (last 30 frames) for velocity/heading/persistence calculation. Stale tracks (>5s unseen) are pruned.

---

### `engagement_planner.py` (~200 lines)
Converts scored targets to an optimized engagement queue.

**Classes:**
- `EngagementOrder` (`@dataclass`) — `target`, `pan`, `tilt`, `rank`
- `EngagementPlanner` — Plans turret engagement sequence

**Key Methods:**
- `plan(targets, current_pan, current_tilt)` → `List[EngagementOrder]`
  - Filters by `min_threat_score`
   - Truncates to `max_queue_length`
   - When `single_target_only` is enabled, queue length is forced to `1` and slew-order optimisation is disabled
  - Converts pixel position → pan/tilt degrees via `_pixel_to_pantilt()`
  - Optionally optimizes order via nearest-neighbor TSP heuristic

**Pixel-to-Pan/Tilt Conversion:**
```python
offset_x = (norm_cx - 0.5) × camera_hfov  # horizontal degrees from center
offset_y = -(norm_cy - 0.5) × camera_vfov  # vertical degrees (inverted)
pan  = current_pan + offset_x
tilt = current_tilt + offset_y
```

---

## 3. CONNECTION SYSTEM

### 4 Connection Modes

| Mode | ID | Description | Hardware Required |
|---|---|---|---|
| ESP32 USB | 0 | Single USB cable, full ASCII protocol | ESP32 only |
| Dual USB | 1 | Bus servo to Debug Board + IO to ESP32 | ESP32 + Debug Board (separate USB) |
| WiFi + Debug USB | 2 | Bus servo to Debug Board, IO over WiFi | Debug Board USB + ESP32 WiFi |
| Full WiFi | 3 | Everything wireless | ESP32 WiFi (debug board wired to ESP32) |
| Dual ESP32 WiFi | 4 | Separate ESP32 boards for servos and IO | Primary ESP32 WiFi + Secondary ESP32 WiFi |

### Mode Details

**Mode 0 — ESP32 USB:**
- Single `serial.Serial` connection to ESP32
- All commands via ASCII protocol: `P{pan}T{tilt}F{fire}L{led}R{laser}G{acc3}S{safety}M{mode}\n`
- Simplest setup, no bus servos needed

**Mode 1 — Dual USB:**
- Two serial connections: ESP32 (IO tokens) + Debug Board (bus servo binary)
- Pan/tilt sent as 11-byte Yahboom bus servo packets to Debug Board
- LED/laser/fire/safety sent as ASCII IO tokens to ESP32
- Debug Board is connected directly to PC (NOT chained through ESP32)

**Mode 2 — WiFi + Debug USB:**
- Debug Board serial (bus servo pan/tilt) + ESP32 UDP (IO tokens)
- UDP packets contain JSON payload + CRC32 integrity check
- Best for reducing wire clutter while keeping precise servo control

**Mode 3 — Full WiFi:**
- Everything over UDP to ESP32
- Motion and IO are sent as JSON payloads with CRC32 integrity check
- Typical payload fields are `pan_cmd`, `tilt_cmd`, `fire`, `safety`, `mode`, `led`, `laser`, and optional `move_time_ms`
- ESP32 relays bus servo commands to debug board via UART2

**Mode 4 — Dual ESP32 WiFi:**
- Primary ESP32 handles IO (fire, safety, laser, LED, PIR)
- Secondary ESP32 (Yahboom board) handles pan/tilt servo control
- Both communicate over WiFi/UDP only
- No USB cables required at runtime
- Simplifies wiring by separating servo control from accessory control

### Per-Link Connection Status

The Connection tab shows individual link status with checkmarks:
- ✅ = link connected successfully
- ❌ = link failed to connect
- Each mode shows status for its relevant links (ESP32 serial, Debug Board serial, UDP)

### Bus Servo Protocol

Binary 11-byte packets for Yahboom YB-SD35M servos:
```
Header:  0xFF 0xFF
Payload: [servo_id, 0x07, 0x03, 0x2A, pos_hi, pos_lo, time_hi, time_lo]
Checksum: (subtraction mode) ~sum(payload) & 0xFF
```

- Position: 0–4095 ticks (mapping 0–270°)
- Time: Movement duration in milliseconds
- Default servo IDs: Pan=1, Tilt=2

### UDP Protocol (Modes 2, 3)

JSON payload sent via UDP datagram:
```json
{
   "v": 1,
   "t": "cmd",
  "seq": 42,
   "ts": 1700000000000,
   "p": {
      "pan_cmd": 135,
      "tilt_cmd": 55,
      "fire": 0,
      "safety": 1,
      "mode": 0,
      "led": 1,
      "laser": 0,
      "move_time_ms": 1200
   },
   "crc": "a1b2c3d4"
}
```

- Mode 2 typically sends IO-only payloads over UDP while pan/tilt still go to the Debug Board USB link.
- Mode 3 sends full motion plus IO over UDP; it does not send raw ASCII over UDP anymore.

---

## 4. DETECTION PIPELINE

### Mode Dispatch

The detector uses a dispatch table mapping mode index → detection method:

```python
_DISPATCH = {
    0:  _detect_frame_diff,
    1:  _detect_backsub,
    2:  _detect_yolo,
    3:  _detect_hybrid_diff_backsub,
    4:  _detect_hybrid_diff_yolo,
    5:  _detect_hybrid_backsub_yolo,
    6:  _detect_color,
    7:  _detect_hybrid_color_diff,
    8:  _detect_hybrid_color_backsub,
    9:  _detect_hybrid_color_yolo,
    10: _detect_yolo,  # Filtered Target Mode (same as YOLO)
}
```

### Algorithm Details

**Frame Difference (Mode 0):**
1. Convert current + previous frame to grayscale
2. `cv2.absdiff()` between frames
3. Gaussian blur (5×5 kernel)
4. Binary threshold (default 40)
5. Dilate (2 iterations)
6. `findContours()` → filter by min/max area → bounding boxes

**Background Subtraction (Mode 1):**
1. MOG2 background subtractor (30-frame warmup)
2. Apply to frame → foreground mask
3. Threshold at 200
4. Dilate (2 iterations)
5. `findContours()` → filter by area → bounding boxes

**YOLO (Mode 2):**
1. Load `.pt` model via `ultralytics.YOLO`
2. `model(frame, stream=True, verbose=False)`
3. Filter by confidence threshold
4. Filter by target class list
5. Filter by minimum area
6. Convert xyxy → xywh tuples

**Color Detection (Mode 6):**
1. Convert to HSV
2. Build combined mask from preset ranges (or custom HSV)
3. If a named preset finds nothing, retry once with a small saturation/value tolerance while preserving the same hue family
4. Gaussian blur + morphological close
5. `findContours()` → filter by min/max area → bounding boxes

Named presets are hue-anchored but shade-tolerant. Moderate darkening or desaturation of the selected target color is still treated as that selected color, while nearby families such as cyan versus blue remain separated.

**Hybrid Modes (3–5, 7–9):**
- **Union hybrids** (3, 7, 8): Run both algorithms, merge results via `_merge_boxes()`
- **Gated hybrids** (4, 5, 9): First algorithm acts as motion/color gate — if it detects anything, run second algorithm; otherwise skip expensive computation

### YOLO Model Management

- Source-side models are stored in `YOLO_MODELS/` at the workspace root
- Packaged-release operator model drop folder is `F:\SMART SENTRY V2.3.2\YOLO_MODELS`
- Packaged default fallback weights may also exist under `F:\SMART SENTRY V2.3.2\SMART_SENTRY_V2_3_2_FILES\YOLO_MODELS`
- Model selector combo box scans for `*.pt` files
- Load button calls `detector.load_yolo(path)`
- Class filter text input controls which YOLO classes are detected
- Confidence spinner controls minimum detection confidence

### Detector Reset

`detector.reset()` is called on:
- Sentry enable toggle
- Detection mode change
- Clears: previous frame, background subtractor, warmup counter

---

## 5. TARGET PROCESSING

### Pipeline: Raw Boxes → Engagement Orders

```
detector.detect(frame, mode)
    → [(x,y,w,h,score,class_id), ...]   6-tuples from detector
    
_raw_detections_to_objects(raw, frame_w, frame_h)
    → [DetectedObject, ...]               Structured objects with center/norm

_apply_face_identity_to_objects(frame, detections)
   → recognized labels + optional friendly suppression

TargetFilter.filter(detections)
    → qualified [DetectedObject, ...]      Class/confidence/size/zone filtered

ThreatScorer.score(qualified, timestamp)
    → sorted [TrackedTarget, ...]          Threat-ranked with velocity/persistence

EngagementPlanner.plan(targets, pan, tilt)
    → [EngagementOrder, ...]               Pan/tilt angles, ranked queue
```

### Class Mapping

Raw `class_id` (0–79) is mapped to YOLO COCO class names:
```
0=person, 1=bicycle, 2=car, 3=motorcycle, 4=airplane,
5=bus, 6=train, 7=truck, 8=boat, 9=traffic light,
10=fire hydrant, 11=stop sign, ... (80 total)
```

Non-YOLO detections (frame diff, backsub, color) always use `class_id=0` and map to class name based on context.

---

## 6. ENGINE STATE MACHINE

### States

```
┌───────────┐   enable    ┌───────────┐
│  PAUSED   │ ──────────► │ GUARDING  │ ◄─────────┐
└───────────┘             └─────┬─────┘           │
      ▲                         │ threats          │ timeout
      │ disable                 ▼                  │
      │                   ┌───────────┐    ┌───────┴─────┐
      └───────────────────│ ENGAGING  │───►│  RETURNING  │
                          └───────────┘    └─────────────┘
                            queue done
```

**PAUSED:** Sentry disabled. No processing, no turret movement.

**GUARDING:** Watching for threats. If no threats, runs patrol logic. If threats detected above `min_threat_score`, plans engagement queue and transitions to ENGAGING.

**ENGAGING:** Working through engagement queue in phases:
1. **aim** — Servo settling (350ms)
2. **precision** — continuous visual-servo refinement using the live target center, shared camera-model angle conversion, EMA-smoothed error, deadzone suppression, reversal braking, and bounded PD-style correction
3. **fire** — Burst fire if auto-trigger enabled, with bounded micro-correction allowed while drift remains inside fire tolerances
4. Advance to next target or transition to RETURNING

**RETURNING:** Wait `return_delay` seconds, then move to guard position and re-enter GUARDING.

### Guard Patrol Modes

| Mode | ID | Behavior |
|---|---|---|
| Static | 0 | Hold guard_pan/guard_tilt |
| Slow Sweep | 1 | Continuous pan between sweep_pan_min/max at sweep_speed deg/sec |
| Waypoint Patrol | 2 | Visit waypoints in order with dwell pauses |
| Random Scan | 3 | Move to random positions with dwell pauses |

### Engagement Flow Detail

1. `_update_guarding()` detects scoreable targets → calls `planner.plan()`
2. Queue created, sorted by nearest-neighbor TSP (if `optimize_slew_order`)
3. First target: `_move_turret(pan, tilt)` → state = ENGAGING
4. Phase "aim": Wait 350ms for servo settle
5. Phase "precision": live visual-servo refinement using the latest target position
   - Error = target center offset from frame center converted through the shared planner camera model
   - Error is smoothed before control output
   - Small error inside controller deadzone commands no correction
   - Correction uses proportional + derivative control with bounded step size and reversal braking
   - Aim-lock frames increase only while smoothed error remains inside lock tolerance
6. Phase "fire": `_begin_fire()` → callback `_cb_fire(burst_count)`
   - Only fires if `auto_trigger_enabled` is True
   - Small micro-corrections are still allowed while drift stays inside fire recenter tolerance
   - If drift exceeds fire recenter tolerance, the engine falls back to precision instead of finishing a bad burst
   - Logs engagement to `engagement_log`
7. Wait for burst duration + `inter_target_cooldown`
8. Advance to next target or → RETURNING

### Protected Aiming Baseline

The current Smart Sentry v2 aiming controller is now the protected baseline for this repository.

- It should not be rewritten, simplified, or behaviorally changed unless the replacement is demonstrably better on live hardware or measured replay tests.
- “Better” means at minimum: equal or better centering, equal or lower overshoot, no regression in reacquisition continuity, and no regression in fire gating behavior.
- Cosmetic HUD changes are allowed without changing controller behavior.
- Tuning or logic changes to the controller should be documented in this manual and logged in `SMART_SENTRY_ISSUE_LOG.md`.

### Adaptive After-Target-Loss Contract

The current target-loss behavior is no longer a single generic recovery sweep. It is an adaptive protocol with explicit context capture and two distinct operator-tunable behaviors. Treat this as a protected behavior contract, not incidental implementation detail.

When an active target is lost, the engine now captures all of the following before it begins recovery:

- the last tracked target id and threat score
- the last known pan and tilt solution for that target
- the recent motion direction implied by the target history
- whether other visible candidates are present at the loss moment
- whether the scene is sparse or crowded based on the configured crowding threshold

The engine then selects one of two named recovery protocols:

1. `rapid_handoff_search`
2. `persistent_reacquire_search`

`rapid_handoff_search` is intended for scenes where the original target was lost but another credible target is already visible or appears quickly after loss. Its contract is:

- keep the turret moving in the same general direction for a short pursuit window instead of stopping immediately
- bias the search just behind and around the loss vector using backoff pan and tilt steps so the turret feels purposeful instead of random
- allow an immediate handoff if a visible target is stronger than the lost target by at least the configured switch margin
- finish quickly; it is a handoff-oriented protocol, not a wide-area search

`persistent_reacquire_search` is intended for sparse scenes where nothing equally credible is visible after loss. Its contract is:

- preserve continuity with the lost target instead of immediately abandoning the area
- keep moving in the last credible motion direction first, then hunt tightly around the last known aim before widening further
- retry the local search for more passes in sparse scenes than in crowded scenes
- expand the search pattern outward gradually from the loss anchor rather than jumping to unrelated positions
- remain bounded; once retry limits are exhausted, the engine must fall through to the normal return behavior

The distinction between these protocols is deliberate and must not be collapsed back into one generic “scan around last target” routine unless the full behavioral contract is revalidated and the manual is updated in the same change.

### Visible-Target Handoff Rule

If a new visible target appears during loss recovery, the engine does not automatically switch every time. The switch contract is:

- the alternative target must be currently visible
- the alternative target must exceed the lost target context by the configured `loss_switch_score_margin`
- the persistence bias still matters; recovery should not thrash between short-lived weak detections
- when a switch is accepted, the recovery state is cleared and the new target becomes the active engagement target immediately

This means the engine now behaves differently in two operator-visible cases:

1. A new target appears and is materially stronger: hand off quickly.
2. No target appears or only weak candidates appear: keep searching around the last loss anchor for a bounded time.

### Personality Rule

The new recovery behavior includes “personality” controls. These are not cosmetic labels; they intentionally shape how recovery feels:

- `loss_personality_intensity` increases how assertively the search points deviate from a plain symmetric pattern
- `loss_personality_velocity_bias` biases recovery in the direction the target was already moving
- `loss_personality_order_variation` allows less rigid point ordering so recovery feels less robotic in a repetitive sense while still remaining deterministic enough for tuning

These controls may alter the path shape and movement feel, but they must not change the safety envelope, firing rules, or the requirement that recovery remains bounded.

### Search Style Rule

The `Search Style (loss + PIR)` control is now a shared runtime preference for both after-target-loss hunting and PIR no-detect behavior.

- `Hunting` keeps the turret near the loss or PIR cue area first, uses a denser near-field pattern, and feels more deliberate.
- `Fast Reacquire` reduces dwell and broadens early coverage sooner so the system can catch up faster when raw reacquisition speed matters more than movement feel.

This setting is intentionally shared so blind-spot PIR hunting and visual target-loss hunting do not feel like two unrelated movement personalities.

### Turret Movement

All movement goes through `_move_turret(pan, tilt)`:
- Updates `current_pan` / `current_tilt`
- Invokes `_cb_move` callback → `SentryV2Comm.send_command()`

---

## 7. OVERLAY / HUD

The overlay draws all visual elements onto the BGR frame before display.

### Drawn Elements

| Element | Condition | Visual |
|---|---|---|
| Guard Crosshair | `show_guard_crosshair` | Layered center reticle with segmented arms, center ring, accent ticks, and engage pulse |
| Primary Target Box | Primary tracked target visible | Single-target bracketed box with reticle-matched styling and label chip |
| State Badge | Always | Top-left dark panel with accent line and current state label |
| Tracking Diagnostics | Always | Bottom-left panel with error, lock, queue, and recent reacquire note |

### HUD Visual Rules

| State | Reticle / HUD Accent |
|---|---|
| PAUSED | gray |
| GUARDING | green |
| ENGAGING | red |
| RETURNING | yellow |

When the engine is ENGAGING, the center reticle adds a subtle pulse ring. This is a visual-only cue and must not alter aiming behavior.

---

## 8. CONFIGURATION REFERENCE

### DetectionModeConfig

| Field | Type | Default | Description |
|---|---|---|---|
| `detection_mode` | `int` | 2 | Active detection mode (0–10) |
| `min_contour_area` | `float` | 300.0 | Minimum contour area (pixels²) |
| `max_contour_area` | `float` | 1400000.0 | Maximum contour area (pixels²) |
| `yolo_min_area` | `int` | 0 | Minimum YOLO box area |
| `color_preset` | `str` | "red" | Color detection preset name |
| `color_min_area` | `int` | 300 | Minimum color blob area |
| `color_max_area` | `int` | 500000 | Maximum color blob area |
| `color_fusion_strategy` | `str` | "AND" | Hybrid fusion: "AND" or "OR" |
| `color_fusion_overlap` | `int` | 30 | Overlap threshold for fusion |
| `custom_h_min` | `int` | 0 | Custom HSV hue minimum |
| `custom_h_max` | `int` | 179 | Custom HSV hue maximum |
| `custom_s_min` | `int` | 100 | Custom HSV saturation minimum |
| `custom_s_max` | `int` | 255 | Custom HSV saturation maximum |
| `custom_v_min` | `int` | 100 | Custom HSV value minimum |
| `custom_v_max` | `int` | 255 | Custom HSV value maximum |
| `motion_gate_threshold` | `float` | 1.0 | Motion gate sensitivity for gated hybrids |

### TargetFilterConfig

| Field | Type | Default | Description |
|---|---|---|---|
| `allowed_classes` | `List[str]` | `["person"]` | Whitelist of YOLO class names |
| `class_priority` | `Dict[str,float]` | person=5, car=3, dog=2, cat=2 | Priority weights |
| `min_confidence` | `float` | 0.45 | Minimum detection confidence |
| `min_size_ratio` | `float` | 0.005 | Minimum bbox/frame area ratio |
| `max_size_ratio` | `float` | 0.0 | Maximum ratio (0=disabled) |
| `engagement_zone` | `Tuple[4×float]` | (0,0,1,1) | Normalized zone (x1,y1,x2,y2) |

### ThreatScoringConfig

| Field | Type | Default | Description |
|---|---|---|---|
| `w_proximity` | `float` | 0.25 | Weight: distance from center |
| `w_size` | `float` | 0.15 | Weight: object size |
| `w_confidence` | `float` | 0.10 | Weight: YOLO confidence |
| `w_class_priority` | `float` | 0.20 | Weight: class priority value |
| `w_speed` | `float` | 0.10 | Weight: movement speed |
| `w_persistence` | `float` | 0.10 | Weight: time in frame |
| `w_approach` | `float` | 0.10 | Weight: approach rate |
| `use_ml_model` | `bool` | False | Use ML model refinement |
| `ml_model_path` | `str` | config/sentry_v2_threat_model.pkl | ML model path |

### EngagementConfig

| Field | Type | Default | Description |
|---|---|---|---|
| `min_threat_score` | `float` | 0.30 | Minimum score to engage |
| `burst_count` | `int` | 3 | Shots per burst |
| `burst_interval_ms` | `int` | 50 | Milliseconds between shots |
| `inter_target_cooldown` | `float` | 0.8 | Seconds between targets |
| `cycle_cooldown` | `float` | 2.0 | Seconds between full cycles |
| `max_queue_length` | `int` | 1 | Max simultaneous targets; forced to `1` when `single_target_only` is enabled |
| `optimize_slew_order` | `bool` | False | TSP nearest-neighbor ordering; disabled in single-target mode |
| `return_delay` | `float` | 1.5 | Seconds before returning to guard |
| `engagement_speed` | `int` | 80 | Servo speed multiplier |
| `auto_trigger_enabled` | `bool` | False | Enable automatic firing |
| `trigger_mode_bb` | `bool` | False | False=Water, True=BB |
| `precision_aim_enabled` | `bool` | True | Enable PID refinement |
| `precision_settle_time` | `float` | 0.5 | Max PID refinement duration |
| `precision_kp` | `float` | 0.02 | PID proportional gain |
| `precision_ki` | `float` | 0.001 | PID integral gain |
| `precision_kd` | `float` | 0.005 | PID derivative gain |
| `precision_max_step` | `float` | 1.0 | Max PID correction per tick (degrees) |
| `adaptive_loss_recovery_enabled` | `bool` | True | Master gate for context-aware after-target-loss behavior |
| `loss_recovery_protocol_new_target` | `str` | `rapid_handoff_search` | Protocol used when a stronger candidate is visible during loss recovery |
| `loss_recovery_protocol_no_detection` | `str` | `persistent_reacquire_search` | Protocol used when no strong visible replacement is present |
| `loss_handoff_pursuit_time_s` | `float` | 0.55 | How long rapid handoff continues along the last target direction before local stepping |
| `loss_handoff_backoff_pan_deg` | `float` | 3.5 | Pan offset used to search just behind and around the loss vector |
| `loss_handoff_tilt_step_deg` | `float` | 2.0 | Tilt stepping used during rapid handoff search |
| `loss_handoff_max_duration_s` | `float` | 1.4 | Maximum total time rapid handoff recovery may spend before resolving |
| `loss_persistent_retry_passes_sparse` | `int` | 3 | Number of bounded retry passes when the scene is sparse |
| `loss_persistent_retry_passes_crowded` | `int` | 1 | Number of bounded retry passes when the scene is already crowded |
| `loss_persistent_expand_scale` | `float` | 1.3 | Multiplier that grows the local search radius on each persistent retry pass |
| `loss_switch_score_margin` | `float` | 0.08 | Minimum score advantage required before switching to a visible alternative target |
| `loss_switch_persistence_bias` | `float` | 0.15 | Extra continuity bias that reduces thrash toward brief weak alternatives |
| `loss_scene_crowding_threshold` | `int` | 3 | Number of credible visible targets considered “crowded” for recovery selection |
| `loss_personality_intensity` | `float` | 0.35 | Strength of path-shape variation during recovery |
| `loss_personality_velocity_bias` | `float` | 0.45 | Weight placed on the lost target's recent motion direction |
| `loss_personality_order_variation` | `float` | 0.2 | Allowed variation in the order recovery points are visited |

### GuardConfig

| Field | Type | Default | Description |
|---|---|---|---|
| `guard_pan` | `float` | 90.0 | Home pan position |
| `guard_tilt` | `float` | 50.0 | Home tilt position |
| `rest_pan` | `float` | 90.0 | Rest-position pan; defaults to the home pan when first created |
| `rest_tilt` | `float` | 50.0 | Rest-position tilt; may be saved below `guard_tilt`/`tilt_min` as long as it remains inside absolute sentry tilt limits |
| `rest_on_startup_enabled` | `bool` | True | Start in rest after launch once the configured startup delay expires |
| `rest_on_close_enabled` | `bool` | True | Send the turret to rest before final shutdown/close |
| `rest_startup_delay_ms` | `int` | 900 | Delay before startup rest begins |
| `rest_close_timeout_ms` | `int` | 1600 | Grace period allowed for close-time rest movement |
| `home_move_speed_dps` | `float` | 24.0 | Primary speed used for guided moves back to home or guard |
| `home_move_approach_speed_dps` | `float` | 11.0 | Slower final-approach speed used near the home target |
| `rest_move_speed_dps` | `float` | 14.0 | Primary speed used for guided moves into rest |
| `rest_move_approach_speed_dps` | `float` | 5.0 | Slower final-approach speed used near the rest target |
| `guided_move_approach_window_deg` | `float` | 18.0 | Distance from the destination where the guided move switches to its approach speed |
| `pan_min` | `float` | 0.0 | Absolute minimum allowed pan angle |
| `pan_max` | `float` | 270.0 | Absolute maximum allowed pan angle |
| `tilt_min` | `float` | 0.0 | Minimum allowed guard/manual tilt bound; rest moves may still use any tilt inside absolute sentry limits |
| `tilt_max` | `float` | 110.0 | Maximum allowed guard/manual tilt bound |
| `camera_hfov` | `float` | 78.0 | Horizontal FOV (degrees) |
| `camera_vfov` | `float` | 44.0 | Vertical FOV (degrees) |
| `pan_center_bias_deg` | `float` | 0.0 | Horizontal calibration offset applied to pixel-to-pan conversion |
| `tilt_center_bias_deg` | `float` | 0.0 | Vertical calibration offset applied to pixel-to-tilt conversion |
| `frame_width` | `int` | 1280 | Frame width (updated at runtime) |
| `frame_height` | `int` | 720 | Frame height (updated at runtime) |
| `guard_mode` | `int` | 0 | 0=Static, 1=Sweep, 2=Waypoint, 3=Random |
| `sweep_pan_min` | `float` | 45.0 | Sweep left limit |
| `sweep_pan_max` | `float` | 135.0 | Sweep right limit |
| `sweep_tilt` | `float` | 50.0 | Sweep fixed tilt |
| `sweep_speed` | `float` | 8.0 | Sweep speed (deg/sec) |
| `patrol_waypoints` | `List[Tuple]` | [] | Waypoint list (pan, tilt) |
| `patrol_dwell` | `float` | 2.0 | Dwell time per waypoint (sec) |
| `patrol_speed` | `float` | 10.0 | Waypoint move speed (deg/sec) |
| `random_pan_min` | `float` | 45.0 | Random scan pan minimum |
| `random_pan_max` | `float` | 135.0 | Random scan pan maximum |
| `random_tilt_min` | `float` | 30.0 | Random scan tilt minimum |
| `random_tilt_max` | `float` | 70.0 | Random scan tilt maximum |
| `random_dwell` | `float` | 3.0 | Random dwell time (sec) |
| `random_speed` | `float` | 8.0 | Random move speed (deg/sec) |

### ConnectionConfig

| Field | Type | Default | Description |
|---|---|---|---|
| `connection_type` | `int` | 0 | Connection mode (0–3) |
| `esp32_port` | `str` | "COM10" | ESP32 serial port |
| `esp32_baud` | `int` | 115200 | ESP32 baud rate |
| `debug_port` | `str` | "" | Debug board serial port |
| `debug_baud` | `int` | 115200 | Debug board baud rate |
| `udp_host` | `str` | "192.168.4.1" | ESP32 WiFi IP address |
| `udp_port` | `int` | 9000 | UDP port |
| `servo_udp_host` | `str` | "192.168.4.2" | Secondary ESP32 (Yahboom board) WiFi IP address |
| `servo_udp_port` | `int` | 9001 | Secondary ESP32 UDP port |
| `pan_servo_id` | `int` | 1 | Bus servo ID for pan |
| `tilt_servo_id` | `int` | 2 | Bus servo ID for tilt |
| `bus_servo_time_ms` | `int` | 20 | Servo movement time (ms) |
| `invert_pan` | `bool` | False | Invert pan direction |
| `invert_tilt` | `bool` | False | Invert tilt direction |
| `camera_source` | `str` | "0" | Camera index, URL, or file path. Blank input is normalized to camera `0`. |
| `camera_width` | `int` | 1280 | Requested camera width |
| `camera_height` | `int` | 720 | Requested camera height |
| `settings_panel_width` | `int` | 420 | Preferred width of the right-side settings panel |
| `webcam_zoom_pct` | `int` | 100 | Source zoom applied to live webcam frames before display and detection |
| `test_source_zoom_pct` | `int` | 100 | Source zoom applied to video-file or test-source frames |

---

## 9. UI TAB LAYOUT

### Connection Tab

```
┌─ Enable Sentry ────────────────────────────────────────┐
│ [✓] Enable Smart Sentry v2                             │
│ State: PAUSED                                          │
├─ Connection Mode ──────────────────────────────────────┤
│ [Combo: ESP32 USB ▼]                                   │
│ "Single USB cable — full ASCII protocol to ESP32."     │
├─ ESP32 Serial ─────────────────────────────────────────┤
│ Port: [Combo ▼] [Scan]    Baud: [115200]               │
├─ Debug Board Serial ───────────────────────────────────┤
│ Port: [Combo ▼] [Scan]    Baud: [115200]               │
├─ Bus Servo ────────────────────────────────────────────┤
│ Pan ID: [1]  Tilt ID: [2]  Time: [20ms]                │
│ [✓] Invert Pan  [✓] Invert Tilt                        │
├─ WiFi / UDP ───────────────────────────────────────────┤
│ Host: [192.168.4.1]  Port: [9000]                      │
├─ Secondary ESP32 WiFi ────────────────────────────────┤
│ Host: [192.168.4.2]  Port: [9001]                      │
├─ Connection ───────────────────────────────────────────┤
│ [Connect]                                               │
│ ESP32 Serial: ✅  Debug Board: ✅  UDP: —  Servo UDP: —  │
├─ Camera ───────────────────────────────────────────────┤
│ Source: [0 / URL / file path]   Width: [1280] Height: [720] │
│ [Open Camera]   Status: Owned Smart Sentry source             │
└────────────────────────────────────────────────────────┘
```

### Current Layout Constraints

- The settings side is currently a scroll area on the right side of the video feed.
- The settings side is now hosted in a horizontal splitter so operators can resize it against the video feed.
- The current implementation uses icon-first tabs, large previous/next navigation arrows, a stacked `Wake Up` / `Go Rest` header control, and a pinned `Quick Keys` utility action in the top strip.
- The earlier bottom `Panel Width` slider is no longer part of the current operator workflow; width is managed by the splitter and persisted settings.

### Guard Tab

The Guard tab now covers four linked operator responsibilities instead of only the original patrol setup:

- home or guard position definition
- rest-position storage and lifecycle behavior
- PIR blind-spot cueing and no-detect scanning
- patrol and random/sweep motion limits

The current live contract is:

- `guard_pan` / `guard_tilt` remain the primary guarded home position.
- `rest_pan` / `rest_tilt` define a separate parked pose used for startup rest, close-time rest, and manual `Go Rest`.
- `rest_tilt` is allowed to sit below the normal guard minimum tilt as long as it stays inside the absolute sentry tilt range; the live `Go Rest` path now honors that exception instead of clamping back up to `guard.tilt_min`.
- startup rest and close rest are optional and timed by `rest_startup_delay_ms` and `rest_close_timeout_ms`.
- home and rest moves use guided two-stage motion profiles rather than one abrupt speed, with a configurable approach window and separate cruise/approach speeds.

### PIR Guard Behavior

Current PIR guard behavior is cue-first and scan-second:

1. A valid PIR event queues or starts a cue for that sensor's configured pan/tilt.
2. Smart Sentry slews to the cue point and holds there only for the configured `Cue Hold` time while vision checks the exact cue center.
3. If no target is confirmed and `scan_on_no_detect` is enabled, the scan begins immediately from a nearby offset point and starts with a localized hunt around the triggered PIR zone.
4. The duplicated center scan point is intentionally removed when multiple scan points exist because the cue phase already visited the center.
5. Early PIR hunt points are biased toward the triggered sensor's zone before the wider scan mirrors across the rest of the configured search area.
6. If a target appears during confirmation or scan, normal engagement resumes. If not, the cue completes and current builds explicitly command the configured guard/home position instead of leaving the turret parked at the last hunt point.

This behavior matters operationally because the turret should no longer appear to sit at one PIR cue for too long, and it should not remain frozen after the PIR hunt finishes. `Cue Hold` is the only intentional pre-hunt dwell. A stationary pause after the hunt itself is not part of the intended contract.

### Theme and Panel Zoom

The Theme page still persists `font_scale_pct`, but the current UI does not expose it as a normal slider. Operators can adjust panel zoom with `Shift` + mouse wheel while the settings panel has focus, or with the dedicated shortcut keys documented in `SMART_SENTRY_SHORTCUT_KEYS.md`. The zoom is clamped to the live supported range and saved back into theme config.

### Controls and Header Actions

The pinned header and Controls page now share the operator workflow for explicit positioning commands:

- `Wake Up` moves from rest toward the configured home position and uses the waking-home sound cue when enabled.
- `Go Rest` moves to the configured rest position and uses the rest cue when enabled.
- both actions follow the guided move profile instead of the generic manual jump behavior.
- manual movement arrows and absolute-position helpers still operate independently of automatic tracking, subject to the live motion-enable gate and transport availability.
- `Quick Keys` stays visible in the top strip and opens the dedicated shortcut-reference document without changing the header sizing contract.
- The Controls page now also exposes local human voice controls for Smart Sentry speech output, including enable or disable, speech-style presets, voice choice, rate, pitch, volume, a direct test button, an option to mute the ESP32 buzzer while human voice mode is enabled, and a dedicated Voice Diagnostics group.
- The Voice Diagnostics group shows the active speech backend, selected voice, current speech state, route note, a one-click fallback phrase, a stop-voice action, a refresh action for logging the current human-voice diagnostic state, and a `Validate Voices` action that confirms each detected Qt voice can be selected and driven into a valid speech state.

### Facial Recognition Tab

The Facial Recognition tab is now a live runtime surface rather than a placeholder.

- It can register identities from imported still images or from the current live frame.
- The face library is stored separately from the main settings file in `app/config/smart_sentry_v2_3_2_faces.json`.
- Recognition uses a lightweight Haar-cascade and embedding approach so it works in the current environment where `cv2.face` is not available.
- Friendly known faces can be announced, greeted with a small friendly gesture, and optionally suppressed from the engagement pipeline.
- Recognized names are drawn directly on the preview, even when a friendly face is excluded from engagement.

### Shortcut Keys Tab

The Shortcut Keys tab is now the runtime status page for operator hotkeys.

- It exposes one master enable toggle for window-focused shortcuts.
- It shows the assigned key list inside the app.
- It mirrors the same quick-reference document opened by the top-row `Quick Keys` button.

### AI Assistant Tab

The AI Assistant tab is now a live local assistant surface.

- It accepts short operator text requests.
- It can summarize the current runtime state.
- It can draft safe recommendations.
- It can apply a small set of rule-based actions such as switching detection mode, moving to home or rest, toggling shortcuts, controlling face recognition, and speaking a live status summary when allowed by the assistant settings.
- It now includes a `Conversational Voice` mode plus an option to speak replies through the local Qt text-to-speech engine, giving the operator a normal human-style spoken response path without requiring a cloud service.
- The human voice path now supports speech-style presets such as quiet operator, alert guard, warm greeter, and neutral assistant. Each preset updates the local voice rate, pitch, and volume together so operators can shift the spoken character quickly without hand-tuning every slider.
- When human voice mode is enabled, the Controls tab can now mute the ESP32 buzzer path so AI speech does not collide with firmware-driven buzzer cues on the integrated board.
- The newer human-voice and assistant speech controls now carry explicit in-app tooltips so operators can see what each setting validates, changes, or suppresses without leaving the tab.

### Engage Tab

The Engage tab now includes an `After Target Loss` group in the advanced engagement area.

That group is the operator-facing contract for the adaptive recovery system. It currently exposes:

- adaptive loss recovery enable or disable
- rapid handoff pursuit time
- handoff backoff pan amount
- handoff tilt step amount
- sparse-scene retry count
- crowded-scene retry count
- visible-target switch margin
- scene crowding threshold
- recovery personality intensity
- recovery velocity bias

This section is intended to let operators tune how quickly Smart Sentry hands off in dense scenes versus how stubbornly it searches in sparse scenes. Any future UI simplification must preserve the scene-dependent behavior distinction rather than flattening it into one generic timeout control.

### Detection Tab

```
┌─ Detection Mode ───────────────────────────────────────┐
│ [Combo: YOLO Object Detection ▼]                       │
│ "YOLO: Deep learning object detection..."              │
├─ YOLO Settings ────────────────────────────────────────┤
│ Model: [yolo11n.pt ▼] [Load Model]                     │
│ Status: Loaded: yolo11n.pt                             │
│ Classes: [person,car,dog]   Confidence: [0.50]          │
│ Min Area: [0]                                          │
├─ Contour Settings ─────────────────────────────────────┤
│ Min Area: [300]   Max Area: [1400000]                   │
│ Motion Threshold: [1.0]                                 │
├─ Color Settings ───────────────────────────────────────┤
│ Preset: [red ▼]                                        │
│ Min Area: [300]   Max Area: [500000]                    │
└────────────────────────────────────────────────────────┘
```

### Verified UI/Config Gaps

- `engagement_zone` exists in config and overlay logic, but the current UI does not expose an editor for the zone rectangle.
- `show_guard_crosshair` exists in config and overlay logic, but the current UI does not expose a checkbox for it.
- Custom HSV fields exist in config and detector sync, but the current UI does not currently expose manual HSV controls.
- Precision PID gains and lock thresholds exist in config and engine logic, but the current UI exposes only settle time and max step.
- YOLO confidence and YOLO class text are live controls, but they are not currently persisted in `SentryV2Config`.
- The current Motion Gate Threshold slider is live for the active motion-gated hybrid paths. Performance shortcuts are intentionally limited so hybrid and motion-locked modes keep full-resolution gating while pure motion-only modes may use a lighter preprocessing path.

### Scope View

- The toggleable scope overlay is display-only; it does not change detector geometry or fire logic.
- The current reticle intentionally avoids a filled center marker so the aim point stays unobstructed during live tracking.
- Normal scope styling is monochrome for visibility: white outer ring, black inner ring, black crosshair arms, and black short tick marks. A temporary fire-flash accent may still appear during active firing feedback.

---

## 10. PROTOCOL REFERENCE

### ASCII Command Format (ESP32)

```
P{pan}T{tilt}F{fire}L{led}R{laser}G{acc3}S{safety}M{mode}\n
```

| Token | Values | Description |
|---|---|---|
| P | 0–220 | Pan angle (degrees) |
| T | 0–130 | Tilt angle (degrees) |
| F | 0 or 1 | Fire trigger (1=active) |
| L | 0 or 1 | LED relay (1=on) |
| R | 0 or 1 | Laser relay (1=on) |
| G | 0–3 | Accelerometer mode / aux |
| S | 0 or 1 | Safety (0=armed, 1=locked) |
| M | 0 or 1 | Trigger mode (0=water, 1=BB) |

**Example:** `P90T50F0L1R0G0S1M0\n`

### Bus Servo Packet Format

```
Byte: [0xFF] [0xFF] [ID] [0x07] [0x03] [0x2A] [POS_H] [POS_L] [TIME_H] [TIME_L] [CHK]
```

- **ID:** Servo address (1=pan, 2=tilt)
- **0x07:** Packet length
- **0x03:** Write command
- **0x2A:** Position register
- **POS_H/L:** Position in ticks (0–4095 for 0–270°)
- **TIME_H/L:** Movement time in milliseconds
- **CHK:** `~sum(payload_bytes) & 0xFF`

### UDP IO JSON Format

```json
{
  "led": 0,
  "laser": 0,
  "fire": 0,
  "safety": 1,
  "mode": 0,
  "seq": 0,
  "crc": 0
}
```

CRC32 computed over the JSON string (before adding `crc` field), using `zlib.crc32`.

---

## 11. DATA FLOW DIAGRAMS

### Detection-to-Fire Flow

```
[Camera]
   │ cv2.VideoCapture.read()
   ▼
[SentryV2Detector.detect()]
   │ (x,y,w,h,score,class_id) tuples
   ▼
[_convert_detections()]
   │ DetectedObject list
   ▼
[TargetFilter.filter()]
   │ class/confidence/size/zone check
   ▼
[ThreatScorer.score()]
   │ TrackedTarget list (sorted by threat)
   ▼
[EngagementPlanner.plan()]
   │ EngagementOrder queue (pan/tilt angles)
   ▼
[SentryV2Engine state machine]
   │ aim → precision PID → fire
   ├──► cb_move(pan, tilt)  →  SentryV2Comm.send_command()
   └──► cb_fire(burst)      →  SentryV2Comm.send_fire_burst()
                                    │
                                    ▼
                   [Serial/UDP/Bus Servo hardware]
```

### Configuration Data Flow

```
[UI Controls]
   │ QSpinBox.valueChanged / QComboBox.currentIndexChanged
   ▼
[_on_*_changed() handler]
   │ Writes to self.config.<section>.<field>
   ▼
[_push_config()]
   ├── engine.update_config(config)
   ├── overlay.update_config(config)
   └── _sync_detector_params()
           │ Copies config values to detector attributes
           ▼
       [SentryV2Detector instance]
```

### Connection Topology (Mode 1 — Dual USB)

```
       ┌──────────┐     USB Serial (ASCII IO)     ┌─────────────┐
       │   PC     │ ──────────────────────────────►│   ESP32     │
       │          │                                │ LED/Laser/  │
       │          │     USB Serial (Binary Bus)    │ Fire/Safety │
       │          │ ──────────────────────────────►├─────────────┤
       └──────────┘                                │ Debug Board │
                                                   │ Pan/Tilt    │
                                                   │ Bus Servos  │
                                                   └─────────────┘
```

---

## 12. CHANGE IMPACT MAP

Use this section to assess which files are affected by common modifications.

### Adding a New Detection Mode

| Action | Files Affected |
|---|---|
| Add algorithm method | `sentry_v2_detector.py` — new `_detect_*()` method |
| Register in dispatch | `sentry_v2_detector.py` — add to `_DISPATCH` dict |
| Add mode name | `sentry_v2_tab.py` — append to `DETECTION_MODES` list |
| Add mode description | `sentry_v2_tab.py` — append to `_MODE_DESCRIPTIONS` dict |
| UI panel visibility | `sentry_v2_tab.py` — update `_update_detection_panel_visibility()` |

### Adding a New Color Preset

| Action | Files Affected |
|---|---|
| Define HSV ranges | `sentry_v2_detector.py` — add to `COLOR_PRESETS` dict |
| Add to UI combo | `sentry_v2_tab.py` — append to `COLOR_PRESETS` list |

### Adding a New Connection Mode

| Action | Files Affected |
|---|---|
| Add mode constant | `sentry_v2_comm.py` — new `MODE_*` constant |
| Add mode label | `sentry_v2_comm.py` — append to `MODE_LABELS` |
| Implement connect logic | `sentry_v2_comm.py` — update `connect()` method |
| Implement send logic | `sentry_v2_comm.py` — update `send_command()` dispatch |
| Update UI panel visibility | `sentry_v2_tab.py` — update `_update_conn_panel_visibility()` |
| Update mode hint | `sentry_v2_tab.py` — append to `_MODE_HINTS` |

### Changing Threat Scoring

| Action | Files Affected |
|---|---|
| Add new scoring factor | `threat_scorer.py` — add to `_score_one()` |
| Add config field | `sentry_v2_config.py` — add to `ThreatScoringConfig` |
| Add UI slider | `sentry_v2_tab.py` — add to `_build_scoring_tab()` |
| Wire handler | `sentry_v2_tab.py` — update `_on_scoring_changed()` |

### Changing Engagement Behavior

| Action | Files Affected |
|---|---|
| Modify engagement phases | `sentry_v2_engine.py` — `_update_engaging()` |
| Change PID gains | `sentry_v2_config.py` — `EngagementConfig` |
| Change after-target-loss behavior | `sentry_v2_engine.py` — `_capture_loss_recovery_context()`, `_select_loss_recovery_protocol()`, `_update_rapid_handoff_recovery()`, `_update_persistent_recovery()` |
| Add trigger type | `sentry_v2_comm.py` — `send_fire_burst()` |
| Update burst UI | `sentry_v2_tab.py` — `_build_engagement_tab()` |

### Adding a New Guard Patrol Mode

| Action | Files Affected |
|---|---|
| Add mode constant | Document in `GuardConfig.guard_mode` comment |
| Add patrol method | `sentry_v2_engine.py` — new `_patrol_*()` method |
| Register in dispatch | `sentry_v2_engine.py` — update `_update_patrol()` if/elif |
| Add init logic | `sentry_v2_engine.py` — update `_patrol_init()` |
| Add config fields | `sentry_v2_config.py` — add to `GuardConfig` |
| Add UI controls | `sentry_v2_tab.py` — update `_build_guard_tab()` |

### Modifying Overlay Elements

| Action | Files Affected |
|---|---|
| Add/change drawing | `sentry_v2_overlay.py` — modify `draw()` or add `_draw_*()` |
| Add toggle | `sentry_v2_config.py` — add bool to `SentryV2Config` |
| Add UI checkbox | `sentry_v2_tab.py` — update overlay checkboxes |

---

## 13. COPILOT / AI AGENT INSTRUCTIONS

### MANDATORY PRE-WORK

Before making ANY changes to Smart Sentry v2 files:

1. **Read this manual** — understand the architecture and data flow
2. **Identify affected files** — use the Change Impact Map (Section 12)
3. **Check the pipeline** — understand where your change fits in the per-frame flow
4. **Test compile** — run `python -c "from app.sentry_v2 import *"` to verify imports

### CRITICAL INVARIANTS (Do Not Break)

1. **Independence from main app:** Sentry v2 must NEVER import from or depend on `MAIN_FILE_SINGLE_CAM.py` or any main app module. It uses its own camera, detector, and communication.

2. **Own camera priority:** When `self._cap is not None`, external `process_frame()` calls from the main app are ignored (`_from_own_camera` flag).

3. **Detector output format:** Always 6-tuples: `(x, y, w, h, score, class_id)`. The `_convert_detections()` method expects this.

4. **Engine callback pattern:** The engine communicates outward ONLY via callbacks (`_cb_move`, `_cb_fire`, `_cb_state`). Never call `SentryV2Comm` directly from the engine.

5. **Config push pattern:** After any config change, call `_push_config()` which syncs engine, overlay, AND detector.

6. **Bus servo protocol:** Debug Board traffic is BINARY. Never send ASCII to the debug board port. Never send binary to the ESP32 port.

7. **Thread safety:** `SentryV2Comm` uses `threading.Lock` for all serial/UDP operations. Never bypass the lock.

8. **Detector reset:** Always call `detector.reset()` when changing detection modes or re-enabling sentry. Failure to reset leaves stale state (previous frame, MOG2 model).

9. **Pan/tilt ranges:** Pan = 0–220°, Tilt = 0–130°. Always clamp in `_manual_move()`. Bus servo ticks are 0–4095 for 0–270° range.

10. **Safety gate:** The `safety_armed` flag maps to protocol token `S0` (armed) / `S1` (locked). Inverted from what you'd expect.

### FILE MODIFICATION RULES

**sentry_v2_config.py:**
- All new settings MUST be `@dataclass` field_factory with defaults
- MUST be included in `to_dict()` / `from_dict()` for persistence
- Backward-compatible: missing keys in saved JSON must use defaults

**sentry_v2_detector.py:**
- New detection modes: add method, add to `_DISPATCH` dict, increment mode count
- All methods must return `List[Tuple[int, int, int, int, float, int]]`
- Use `_contours_to_boxes()` for contour-based algorithms
- Use `_merge_boxes()` for hybrid unions

**sentry_v2_engine.py:**
- State transitions MUST go through `_change_state()` for callback notification
- All turret movement MUST go through `_move_turret()` for callback notification
- Never access `SentryV2Comm` or UI widgets from the engine

**sentry_v2_comm.py:**
- All send operations MUST acquire `self._lock`
- `connect()` must update `self._connect_details` dict for per-link status
- New IO tokens require updates to `_build_ascii()`, `_build_io_tokens()`, and `_send_io_udp()`

**sentry_v2_tab.py:**
- UI building goes in `_build_*_tab()` methods
- Settings changes go in `_on_*_changed()` handlers
- Always call `_push_config()` after modifying `self.config`
- The `_grab_frame()` timer runs at ~30fps — keep it fast

**sentry_v2_overlay.py:**
- All drawing methods receive `(frame, ...)` and mutate in place
- Colors are BGR (OpenCV convention)
- Access engine state via `engine.last_targets`, `engine.active_order`, etc.

### COMMON TASKS

**Adding a new UI control for an existing config field:**
1. Add widget in the appropriate `_build_*_tab()` method
2. Connect signal to a `_on_*_changed()` handler
3. In the handler, write to `self.config.<section>.<field>`
4. Call `self._push_config()`
5. If needed, add to `_save_config()` for persistence

**Adding a new detection algorithm:**
1. Add method `_detect_new_algo(self, frame)` in `sentry_v2_detector.py`
2. Add entry to `_DISPATCH` dict
3. Add mode name to `DETECTION_MODES` in `sentry_v2_tab.py`
4. Add to `_MODE_DESCRIPTIONS` in `sentry_v2_tab.py`
5. Update `_update_detection_panel_visibility()` if mode needs specific panels

**Testing detection without hardware:**
```python
import cv2, numpy as np
from app.sentry_v2.sentry_v2_detector import SentryV2Detector

d = SentryV2Detector()
frame = np.zeros((480, 640, 3), dtype=np.uint8)
cv2.rectangle(frame, (200, 100, 200, 200), (255, 255, 255), -1)

# Need two frames for frame diff
d.detect(frame, 0)  # First frame (sets prev)
boxes = d.detect(frame, 0)  # This should return boxes if there's motion
```

### WHAT NOT TO DO

- Do NOT add imports from `MAIN_FILE_SINGLE_CAM.py` into any sentry_v2 file
- Do NOT bypass `_push_config()` when changing settings
- Do NOT send commands directly from the engine (use callbacks)
- Do NOT assume camera is always available (check `self._cap is not None`)
- Do NOT add synchronous blocking calls in `_grab_frame()` (it runs on the UI thread timer)
- Do NOT modify the ASCII protocol format without updating all 4 connection modes
- Do NOT add new dataclass fields without defaults (breaks loading saved configs)

### VERIFIED BEHAVIORAL RISKS (2026-03-16)

These are current implementation risks verified during documentation review and runtime probing.

1. **Tuning gap:** the Motion Gate Threshold control is now live in the active motion-gated hybrid methods, but the best threshold still depends on scene noise, camera gain, and the selected detection stack.
2. **Hidden config gap:** `engagement_zone`, `show_guard_crosshair`, custom HSV, and several precision-aim settings exist in config and logic, but are still not fully surfaced in the operator UI.
3. **Persistence gap:** YOLO class text is still a live control rather than a persisted Smart Sentry config field.

---

## 14. TROUBLESHOOTING

### Detection Not Working

| Symptom | Likely Cause | Fix |
|---|---|---|
| No boxes drawn | Detector returns empty list | Check mode matches algorithm, verify camera is open |
| Boxes appear but no engagement | Filter rejects all detections | Check `allowed_classes`, `min_confidence`, `engagement_zone` |
| YOLO mode shows nothing | Model not loaded or wrong release folder used | Confirm the model appears in the selector, wait for the lazy startup load or click "Load Model", and check the release-root `YOLO_MODELS/` folder first |
| Frame diff always empty | No motion in scene | Need actual movement between frames |
| Color mode misses objects | Wrong preset or poor lighting | Try "custom" preset with manual HSV tuning |
| BackSub warmup delay | Normal — MOG2 needs 30 frames | Wait ~1 second for background model to stabilize |

### Connection Issues

| Symptom | Likely Cause | Fix |
|---|---|---|
| ❌ next to ESP32 | Wrong port or port in use | Scan ports, check no other app has the port open |
| ❌ next to Debug Board | Wrong baud rate | Verify 115200 baud, check USB cable |
| Servo doesn't move (Mode 1/2) | Wrong servo ID | Check pan_servo_id (default 1) and tilt_servo_id (default 2) |
| UDP timeout (Mode 2/3) | ESP32 not on WiFi network | Verify ESP32 AP mode, check IP address |
| Movement inverted | Invert flags not set | Toggle "Invert Pan" / "Invert Tilt" checkboxes |
| Camera 0 still opens while the main app already owns the same device | The main app did not provide camera ownership state or the device index is genuinely different | Verify the host app is passing its live main-window reference and that the main camera selector reflects the device actually in use |

### Engagement Issues

| Symptom | Likely Cause | Fix |
|---|---|---|
| Sentry detects but doesn't engage | `min_threat_score` too high | Lower from default 0.30 |
| Fires too fast | Cooldown too short | Increase `inter_target_cooldown` |
| Doesn't fire at all | Auto-trigger disabled | Enable auto-trigger in Engagement tab |
| Aims wrong spot | Camera FOV mismatch | Adjust `camera_hfov` / `camera_vfov` in Guard tab |
| PID oscillation | Gains too high | Lower `precision_kp`, increase `precision_kd` |
| `Go Rest` stops above the saved rest tilt | Rest tilt is below the normal guard minimum and the saved value or limits are inconsistent | Verify `rest_tilt` is inside the absolute sentry tilt range. The current app allows rest moves below `tilt_min`/guard minimum when executing a rest command. |
| `Wake Up` / `Go Rest` feels abrupt | Guided move speeds or approach window are too aggressive | Tune `home_move_speed_dps`, `home_move_approach_speed_dps`, `rest_move_speed_dps`, `rest_move_approach_speed_dps`, and `guided_move_approach_window_deg` in Guard settings. |
| Fire timing looks uneven under heavy load | UI timer jitter can still affect timer-driven burst cadence | Move burst sequencing to a worker or hardware-timed path if stricter cadence is required |

### PIR Guard Issues

| Symptom | Likely Cause | Fix |
|---|---|---|
| PIR cue happens but the scan looks like it instantly returned to patrol | The first scan point used to duplicate the already-visited cue center, so no visible offset move occurred | Current builds remove the duplicated center point. If you still see this, confirm you are running the updated build and that `scan_on_no_detect` is enabled. |
| PIR search starts too late or seems to sit on one cue | `Cue Hold` is too high for the behavior you want | Reduce `Cue Hold` first. Use `Fast Reacquire` if you want the turret to leave the cue earlier and widen sooner. |
| PIR hunt finishes but the turret stays parked at the last hunt point | Older builds could clear PIR state without issuing an explicit return-home command | Current builds command the configured guard/home position when a no-target PIR hunt completes. If you still see a post-hunt stall, update the build rather than trying to tune around it. |
| PIR events feel merged across two zones | Cross-sensor lockout is suppressing near-simultaneous overlaps | Reduce `cross_sensor_lockout_ms` only if your sensors are mounted far enough apart to avoid duplicate-trigger churn. |

### UI and Sound Issues

| Symptom | Likely Cause | Fix |
|---|---|---|
| Theme page has no visible font-size control | Panel zoom is intentionally hidden in the current UI | Use `Shift` + mouse wheel over the settings panel to change the saved panel zoom. |
| Sound toggle is on but no cue plays | Active transport does not currently expose the ESP32 buzzer sound path | Check the pinned sound-link status in the Status panel and verify the active WiFi firmware still supports the normal `sound` action path. |

---

## 15. VERIFIED IMPROVEMENT PLAN

### Highest-Priority Code Fixes

1. Bench-tune Motion Gate Threshold defaults per mode so low-light motion scenes do not force operators into repeated manual retuning.
2. Persist YOLO confidence and YOLO class text in `SentryV2Config`.
3. Expose engagement-zone editing and guard-crosshair toggles in the operator UI.
4. Expose custom HSV and precision lock/PID tuning controls in the operator UI.
5. Add quick-jump navigation between settings sections for faster operator access.

### Recommended UI Update Path

1. Add a compact section-jump strip for `Connection`, `Detection`, `Target Filter`, `Threat AI`, `Engage`, `Guard`, and `Controls`.
2. Keep `Enable`, connection status, camera controls, safety, and fire mode immediately visible without deep scrolling.
3. Collapse advanced tuning groups by default, especially PID, class priority, and future HSV fine-tuning controls.
4. Expose the currently hidden but active config surfaces: engagement zone, guard crosshair toggle, custom HSV, PID gains, and aim-lock thresholds.

### Documentation Update Scope

When code changes are made later, update this manual in the same pass for:

- standalone camera/data flow
- camera ownership behavior
- current UI layout and navigation model
- persisted settings surface
- any operator-facing safety or firing semantics

---

## 16. DEVELOPER CHECKLIST

Before changing Smart Sentry v2, review these Smart Sentry-specific references:

- `SMART_SENTRY_MANUAL.md` for architecture, UI layout, connection modes, and pipeline behavior
- `SMART_SENTRY_ISSUE_LOG.md` for concise issue history, attempted fixes, and what worked
- `app/sentry_v2/sentry_v2_tooltips.py` for the authoritative tooltip text used by the Smart Sentry UI

### Change Checklist

- Update `SMART_SENTRY_MANUAL.md` when Smart Sentry behavior, UI, config, or workflow changes
- Add or update an entry in `SMART_SENTRY_ISSUE_LOG.md` for each Smart Sentry issue investigated
- Record every Smart Sentry fix attempt in the issue log, including attempts that failed
- Mark each issue-log attempt as `Worked`, `Did Not Work`, or `Partial`
- Keep issue-log entries short: date, issue, fix tried, result
- Keep Smart Sentry documentation separate from main-app issue history

## 17. DOCUMENTATION WORKFLOW

Smart Sentry documentation is intentionally split into three layers so future changes stay traceable without turning the manual into a diary:

### Reference Manual

- File: `SMART_SENTRY_MANUAL.md`
- Purpose: architecture, configuration, UI behavior, protocol, and troubleshooting reference
- Update when Smart Sentry design or behavior changes

### Issue Log

- File: `SMART_SENTRY_ISSUE_LOG.md`
- Purpose: compact issue history for Smart Sentry only
- Each row should include:
   - Date
   - Issue summary
   - Fix tried
   - Result: `Worked`, `Did Not Work`, or `Partial`
- Do not add main-app issues to this file

### Tooltip Source

- File: `app/sentry_v2/sentry_v2_tooltips.py`
- Purpose: single source of truth for Smart Sentry tooltip text
- Every tooltip should explain:
   - what the setting controls
   - valid range or allowed values when applicable
   - what increasing or decreasing the value does when that concept applies

This split keeps the manual stable, the issue log concise, and the tooltip text maintainable.

Before submitting changes to Smart Sentry v2:

- [ ] Read this manual's Change Impact Map for affected files
- [ ] No imports from `MAIN_FILE_SINGLE_CAM.py` or other main app modules
- [ ] All new config fields have default values
- [ ] `to_dict()` / `from_dict()` updated for new config fields
- [ ] `_push_config()` called after all config mutations
- [ ] Detector methods return 6-tuples: `(x, y, w, h, score, class_id)`
- [ ] Engine uses callbacks only (no direct comm/UI access)
- [ ] Thread lock used for all serial/UDP operations
- [ ] Compile check: `python -c "from app.sentry_v2 import *"` passes
- [ ] New detection modes added to BOTH `_DISPATCH` and `DETECTION_MODES`
- [ ] Bus servo binary traffic never sent to ESP32 ASCII port
- [ ] All pan values clamped to 0–220, tilt to 0–130
- [ ] This manual updated with any new features, modes, or config fields

---

*End of Smart Sentry v2 Reference Manual*

# Smart Sentry App Change Impact Reference

This document replaces the older `CHANGE_IMPACT_REFERENCE.md` catch-all file.

Its purpose is narrower: when Smart Sentry runtime behavior, firmware paths, packaging, or operator-facing controls change, use this file as the app-specific impact map and review checklist.

## 1. Canonical Runtime Facts

### Pinned current firmware path

- Current Smart Sentry app topology: ESP32 WiFi + Debug Board USB
- Current Smart Sentry app firmware: `arduino/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR.ino`
- Waveshare single-board firmware files are on hold and are not part of the current app contract.

### App identity

- Active desktop app family: Smart Sentry v2.x
- Current documented desktop release target: Smart Sentry v3.0.0
- Main launcher from this repo: `run.py`

### Canonical settings path

- Canonical runtime settings file: `app/config/smart_sentry_v2_3_2_settings.json`
- Legacy compatibility fallbacks: `app/config/smart_sentry_v2_3_1_settings.json`, `app/config/smart_sentry_v3_settings.json`, `app/config/sentry_v2_settings.json`
- Rule: make runtime-setting changes against the canonical file only; if load/save sync logic changes, review the fallback chain in the same change.

### Transport authority

- `app/sentry_v2/sentry_v2_comm.py` is the transport authority.
- UI code may request movement, trigger, sound, or accessory actions, but transport selection logic must stay centralized in the comm layer.
- Do not duplicate transport-specific decision logic in tabs, tooltips, or helper panels.

### Current app-side release deltas

- Preview smoothness relief for busy motion-led modes now lives in `app/sentry_v2/sentry_v2_tab.py`; do not move that optimization into detector cadence without revalidating tracking sensitivity.
- Preview continuity now has a second contract in `app/sentry_v2/sentry_v2_tab.py`: when local detector callbacks lag, the tab may present live camera frames through a reduced-overlay fallback path, and sustained successful-but-near-black webcam frames must trigger recovery instead of silently leaving the operator with a black screen.
- Motion-frame resize acceleration in `app/sentry_v2/sentry_v2_detector.py` is intentionally limited to pure motion-only modes; hybrid and motion-locked paths keep their full-resolution gating unless they are explicitly re-benched.
- Fixed-guard target loss in `app/sentry_v2/sentry_v2_engine.py` now follows a finite recovery path and must end in a clean return-to-guard instead of indefinite hunt.
- Adaptive after-target-loss behavior in `app/sentry_v2/sentry_v2_engine.py` is now a two-protocol contract, not a single generic scan: `rapid_handoff_search` is for quick transfer toward a stronger visible candidate, while `persistent_reacquire_search` is for bounded sparse-scene searching around the last loss anchor.
- Automatic hunt movement now spans `app/sentry_v2/sentry_v2_engine.py` and `app/sentry_v2/sentry_v2_tab.py` together: if the tab defers an engine-requested move because debug-board feedback is stale or unsettled, the engine pose must be resynced to settled hardware state so target-loss and PIR hunts cannot continue from an optimistic unsent position.
- Known-face recognition now depends on `app/sentry_v2/face_identity.py`, `app/sentry_v2/target_filter.py`, `app/sentry_v2/sentry_v2_tab.py`, and `app/sentry_v2/sentry_v2_overlay.py` staying aligned: identity labels, friendly suppression, and preview annotations are intentionally split across those layers.
- The Smart Sentry buzzer is now used for short robotic identity-name cues in `app/sentry_v2/sound_engine.py`; do not fork that into a separate PC audio path without updating transport assumptions and docs together.
- Human-like local speech now depends on the PyQt5 QtTextToSpeech runtime and its Windows SAPI plugin path; if packaging changes, review voice-engine availability at the same time as assistant and sound UI changes.
- Human voice presets and assistant spoken tone are now coupled through `human_voice_style` plus the rate/pitch/volume sliders in `app/sentry_v2/sentry_v2_config.py` and `app/sentry_v2/sentry_v2_tab.py`; if one changes, review both the Controls tab preset behavior and the assistant reply path together.
- The Controls-tab human voice contract now also includes `mute_buzzer_when_human_voice_enabled` plus the Voice Diagnostics surface in `app/sentry_v2/sentry_v2_tab.py`; if buzzer or human voice behavior changes, review both the ESP32 sound path and the Windows speech path together so they do not overlap or misreport state.
- Operator shortcuts are now a documented runtime surface, not a hidden convenience: `app/sentry_v2/sentry_v2_tab.py`, `SMART_SENTRY_SHORTCUT_KEYS.md`, `SMART_SENTRY_MANUAL.md`, and `RECENT_UPDATES.json` must move together when the key map changes.
- The in-app AI Assistant is now a local Ollama-backed operator workflow surface inside `app/sentry_v2/sentry_v2_tab.py`, with deterministic runtime analysis and deterministic fallback behavior around it; treat it as an operator workflow surface, not a generic external-model integration point.
- The current v3.0.0 release target intentionally puts `Facial Recognition` and `AI Assistant` on release hold: the tab definitions stay in `SETTINGS_TAB_SPECS`, but `SETTINGS_TAB_RELEASE_HOLDS` filters them out of the active release UI so unfinished operator workflows do not affect normal release behavior. Restoring them should only require removing the hold entry.
- Guard and rest are now separate runtime contracts in `app/sentry_v2/sentry_v2_config.py` and `app/sentry_v2/sentry_v2_tab.py`: `guard_pan` / `guard_tilt` remain the defended home position, while `rest_pan` / `rest_tilt` plus startup/close rest timers drive the parked pose and the visible `Wake Up` / `Go Rest` actions.
- Rest execution is intentionally allowed to use a saved `rest_tilt` below the normal guard minimum as long as it remains inside the absolute sentry tilt limits; do not reintroduce generic guard/manual clamp logic into the rest move path.
- Guided home/rest motion in `app/sentry_v2/sentry_v2_tab.py` now uses separate cruise and approach speeds plus `guided_move_approach_window_deg`; if any home/rest command path changes, preserve the two-stage easing behavior and review the same tuning fields together.
- The left-pane quick-access deck in `app/sentry_v2/sentry_v2_tab.py` is a mirrored-control surface, not a second behavior source: it must keep reusing the existing handlers and control widgets for enable/video/link/camera/auto motion, movement, safety, fire, accessory outputs, and control-source state, and its expanded-plus-pinned persistence must stay aligned with the canonical settings file.
- PIR no-detect recovery in `app/sentry_v2/sentry_v2_engine.py` and `app/sentry_v2/sentry_v2_pir_manager.py` now starts from the first offset scan point after cue confirmation instead of reusing the already-visited cue center; this visible-search behavior is intentional and must stay aligned with the PIR docs.
- Threat AI status, saved-data visibility, and model-data summaries now depend on `app/sentry_v2/ml_training_logger.py`, `app/sentry_v2/sentry_v2_engine.py`, and `app/sentry_v2/sentry_v2_tab.py` staying aligned.
- The visible command-status surface in `app/sentry_v2/sentry_v2_tab.py` is intentionally human-scale now: automatic tracking moves should not overwrite the readable operator command line, while manual actions and failures still should.
- The toggleable scope reticle in `app/sentry_v2/sentry_v2_overlay.py` is now operator-biased for visibility: no center fill and neutral black/grey/white geometry unless fire flash is active.

## 2. Active Firmware Contracts

### DB3000 USB serial IO path

- Sketch: `arduino/DB3000_ESP32_IO_Telemetry_2026_w_PIR/DB3000_ESP32_IO_Telemetry_2026_w_PIR.ino`
- Used when ESP32 IO remains on direct serial tokens.

### DB3000 WiFi UDP baseline

- Sketch: `arduino/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR.ino`
- Used for the documented Smart Sentry v2.3.2 WiFi runtime.
- Rule: this firmware path remains valid across desktop app releases until the firmware contract itself changes.
- Current contract highlights:
  - GPIO0 stays reserved for ESP32 BOOT behavior.
  - Sweep is app-triggered over UDP, not a local GPIO0 runtime input.
  - Rest position is now a shared app-plus-firmware contract: desktop settings push a `rest` block to the active WiFi sketch, and the sketch exposes `{"action":"rest"}` plus `rest_pan` / `rest_tilt` in runtime replies.
  - Rest audio must stay on the existing buzzer transport by sending the normal `{"action":"sound"}` UDP tone payload, not a separate PC-local sound path.
  - SSID contract is `SMART-SENTRY-V2.3`.

### Waveshare single-board bridge archive

- Sketch: `arduino/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE.ino`
- Treat this as an archived, on-hold bench path, not the current Smart Sentry app runtime.
- Do not route app-default firmware, flashing, or release documentation through this path unless the user explicitly reactivates it.
- If this path is ever resumed, review the Waveshare helper scripts and docs in the same change.

## 3. Code Areas That Must Be Reviewed Together

When changing any one of the areas below, review the whole grouped set before considering the work complete.

### Firmware path changes

- `ESP32_CURRENT_SKETCH.md`
- `ESP32_UDP_FLASH.md`
- `SMART_SENTRY_MANUAL.md`
- `SMART_SENTRY_ISSUE_LOG.md`
- `RECENT_UPDATES.json`
- This file
- Any active release compilation protocol

### Connection mode or transport changes

- `app/sentry_v2/sentry_v2_tab.py`
- `app/sentry_v2/sentry_v2_comm.py`
- `app/sentry_v2/sentry_v2_tooltips.py`
- `app/sentry_v2/sentry_v2_overlay.py` when on-screen status or scope behavior changes
- Connection labels, status strings, and help text

### Runtime settings schema changes

- `app/config/smart_sentry_v2_3_2_settings.json`
- `app/config/smart_sentry_v2_3_1_settings.json`
- `app/config/smart_sentry_v3_settings.json`
- `app/config/sentry_v2_settings.json`
- Settings load and save logic in `app/sentry_v2/sentry_v2_tab.py`
- Any documentation that still names old settings files as canonical

### Engagement and loss-recovery behavior changes

- `app/sentry_v2/sentry_v2_engine.py`
- `app/sentry_v2/sentry_v2_config.py`
- `app/sentry_v2/sentry_v2_tab.py`
- `SMART_SENTRY_MANUAL.md`
- `SMART_SENTRY_ISSUE_LOG.md`
- `RECENT_UPDATES.json`
- Any active live-validation checklist for the current release

Rule: do not change after-target-loss behavior in only one of these places. Engine logic, config defaults, UI labels, and the written protocol contract must stay aligned.

### Face recognition, identity cues, or AI-assistant changes

- `app/sentry_v2/face_identity.py`
- `app/sentry_v2/target_filter.py`
- `app/sentry_v2/sentry_v2_tab.py`
- `app/sentry_v2/sentry_v2_overlay.py`
- `app/sentry_v2/sound_engine.py`
- `app/config/smart_sentry_v2_3_2_settings.json`
- `app/config/smart_sentry_v2_3_2_faces.json`
- `SMART_SENTRY_MANUAL.md`
- `SMART_SENTRY_SHORTCUT_KEYS.md` when shortcut-facing identity workflows change
- `SMART_SENTRY_ISSUE_LOG.md`
- `RECENT_UPDATES.json`

Rule: face registration, identity matching, friendly suppression, buzzer or human-voice announce behavior, and AI-assistant wording are one operator-facing feature family. Do not update only one part of that stack.

Additional rule: if human-like speech is changed, review Qt text-to-speech initialization, voice-selection UI, assistant auto-speak behavior, and packaging hooks in the same pass.

Additional release rule: if the feature is not release-ready, apply the release-hold workflow from `SMART_SENTRY_RELEASE_HOLD_CONVENTION.md` instead of removing the tab or leaving the runtime partially active.

### Guard, rest, and PIR workflow changes

- `app/sentry_v2/sentry_v2_tab.py`
- `app/sentry_v2/sentry_v2_config.py`
- `app/sentry_v2/sound_engine.py`
- `app/sentry_v2/sentry_v2_engine.py`
- `app/sentry_v2/sentry_v2_pir_manager.py`
- `SMART_SENTRY_AUTOTRACKING_BEHAVIOR_BLUEPRINT.md`
- `SMART_SENTRY_MANUAL.md`
- `PIR_GUARD_QUICK_START.md`
- `PIR_INTEGRATION_SUMMARY.md`
- `PIR_AT_A_GLANCE.md`
- `SMART_SENTRY_ISSUE_LOG.md`
- `RECENT_UPDATES.json`

Rule: treat guard-home behavior, rest-position behavior, PIR cue-confirm-scan behavior, and their operator wording as one coupled surface. If one changes, update the other code and documentation in the same pass.

- The current PIR contract now distinguishes a short `Cue Hold` from the subsequent local hunt. PIR no-detect behavior must not sit at the cue for too long; it should leave the cue quickly and search the triggered zone first.
- The current after-target-loss contract now includes a denser near-field local hunt ordered by recent motion direction before broader widening. Any future simplification must preserve that deliberate local hunting feel or revalidate the behavior.

### Packaging and release changes

- Version marker files
- Launcher text and window title metadata
- Packaging specs and generated output naming
- Release-root `YOLO_MODELS/` folder contract versus bundled support-folder defaults
- Release notes and compilation protocol docs
- `SMART_SENTRY_RELEASE_HOLD_CONVENTION.md` when unfinished tabs are intentionally kept visible but inactive

## 4. Workspace Canonical Vendor Folders

The workspace root intentionally keeps one canonical folder per vendor package after cleanup.

### Waveshare vendor bundles

- `Waveshare_Bus_Servo_Driver_HAT_A_Vendor`
- `Waveshare_BusServoDriverHAT_FACTORY`
- `WAVESHARE SERVO DRIVER HAT`

### Yahboom and servo libraries

- `YB-SD15MBus-servo-master`
- `YB-SD35MBus-servo-main`
- `SCSTServoLibrary`
- `STServo_Python`
- `ST_Servo`

### Vendor-folder rule

- Keep one canonical folder only.
- Do not keep wrapper folders that contain an inner folder with the same package again.
- If a tool script depends on a vendor path, update the script in the same change as any folder rename.

## 5. Waveshare Stock Flash Dependency

- Script: `tools/flash_waveshare_vendor_stock.ps1`
- Canonical stock-image root after cleanup: `Waveshare_Bus_Servo_Driver_HAT_A_Vendor`
- Required artifact path under that folder: `bin/`

If the vendor image bundle is moved again, update the script path immediately. Do not leave hard-coded references to removed wrapper folders.

## 6. Release Checklist

Before calling a firmware or runtime change complete, verify all of the following:

- The active sketch path is correct in `ESP32_CURRENT_SKETCH.md`.
- Flash examples in `ESP32_UDP_FLASH.md` still match the active firmware.
- Runtime settings still load from `app/config/smart_sentry_v2_3_2_settings.json`.
- UI wording matches the real connection topology.
- Version marker files and launcher text match the intended release.
- `RECENT_UPDATES.json` includes a concise summary entry when behavior or release identity changed.
- `SMART_SENTRY_ISSUE_LOG.md` records each Smart Sentry issue and fix attempt that materially changed runtime behavior.
- Any release-held unfinished tab is documented and still disabled before packaging.

## 7. Naming Standard

- New Smart Sentry release assets should use Smart Sentry naming, not legacy AutoTracker naming.
- Desktop app release numbers do not require a firmware sketch rename when firmware contents are unchanged.
- Prefer stable descriptive firmware names for future sketches instead of coupling them to every desktop app release.
- Vendor folders should be clear, single-level, and non-duplicated.
- New docs should be named for Smart Sentry directly when they describe the current app contract.

## 8. Short Rule Set

- One canonical runtime settings file.
- One transport authority.
- One canonical vendor folder per package.
- One app-facing change-impact reference.

## 9. Compile-Readiness Notes For v3.0.0

- App-side Smart Sentry Python should be treated as compile-ready only after `app/sentry_v2/sentry_v2_engine.py`, `app/sentry_v2/sentry_v2_overlay.py`, and `app/sentry_v2/sentry_v2_tab.py` pass diagnostics together.
- Release packaging should ignore generated bench churn under `platformio/**/.pio/**` and runtime exports under `snapshots/`; those are not desktop app release-source inputs.
- In frozen builds, treat the release-root `YOLO_MODELS/` folder as the public operator drop location and the versioned support-folder `YOLO_MODELS/` copy as bundled defaults only.
- Quick startup now defers camera open and auto-connect, but still schedules a later lazy YOLO auto-load so the packaged app can come up fast without staying permanently unloaded.
- Before a v3.0.0 package is signed off, verify one fixed-guard loss-recovery pass in Frame Difference mode so the turret returns to the configured guard position after its bounded recovery scan.
- Before an adaptive-loss-recovery change is signed off, verify both operator-visible branches: a quick handoff to a stronger visible target and a bounded persistent search when no such target appears.
- Before a v3.0.0 package is signed off, verify `Facial Recognition` and `AI Assistant` remain hidden by the release-hold convention and can be restored by removing their hold entries.

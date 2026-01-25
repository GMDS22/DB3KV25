# Copilot Instructions for DB3000V4.1-main

## Project Overview
- This is an automated turret control system with a PyQt5 UI, supporting multiple detection modes (YOLO, frame difference, background subtraction).
- **Architecture**: Supports Dual-Port operation (Nano for IO/Trigger on COM8, Debug Board for Servos on COM9).
- Main entry point: `app/MAIN_FILE_SINGLE_CAM.py` (creates UI, loads presets, manages tracking logic).
- Major components:
  - `turret_enhancements.py`: UI/status bar/sound helpers.
  - `turret_presets.py`: Preset profiles for tracking and detection.
  - `ui_builder.py`: Modular UI construction.
  - `theme_manager.py`: UI theming.
  - `serial_log*`, `SERIAL_CONNECTION_TEST.py`: Serial communication and diagnostics.

## Developer Workflows
- **Setup:**
  - Use a Python virtual environment (`python -m venv .venv; .\.venv\Scripts\Activate.ps1`).
  - Install dependencies: `pip install -r requirements.txt` (see also `requirements-main.txt`, `requirements-dev.txt`, `requirements-optional.txt`).
- **Run:**
  - Main app: `python app/MAIN_FILE_SINGLE_CAM.py` or use `run.py` for alternate entry.
- **Testing:**
  - Test scripts: `test_app_start.py`, `test_resolution_fix.py`, `test_nano_io.py`, `test_bus_servo_read.py`.
- **Debugging:**
  - Use log files (`serial_log_*.txt`, `tooltip_debug.txt`) and status bars in the UI.
  - For dependency issues, run `python scripts/check_dependencies.py`.
  - **Health Monitor**: Use the "System Health Monitor" dock (Widgets menu) to view real-time Graphs for FPS, Total Current, and Servo Load.

## Project-Specific Patterns
- **Presets:**
  - All tracking/detection tuning is centralized in `turret_presets.py` (`PRESETS` dict, with detailed docstrings).
- **Enhancements:**
  - UI/status/sound logic is always delegated to `TurretEnhancements` (do not duplicate in main file).
- **Agent Blocks:**
  - Some files contain `AGENT-MANAGED BLOCK` comments. Preserve these when editing.
- **Detection Modes:**
  - YOLO is optional; fallback modes require no torch/ultralytics.
- **Serial/Hardware:**
  - Serial communication is abstracted; `MAIN_FILE_SINGLE_CAM.py` handles Dual Port logic (`_serial_is_dual_port()`).
  - **Trigger Modes**: `Water Mode` (MOSFET, allows Rapid Fire) vs `Projectile Mode` (Servo).

## Integration & Dependencies
- Core: PyQt5, numpy, opencv-python, pyserial, ultralytics (YOLO, optional torch/pygame).
- Optional: torch, cx-Freeze (for packaging).
- Hardware: Arduino Nano (IO) + Debug Board (Servos).

## Conventions
- Do not copy logic between files; use helpers and enhancements.
- UI layout and logic are modularized for maintainability.
- Use the `sounds/` folder for all audio cues (referenced in `turret_enhancements.py`).
- **Widgets Menu**: All Dock Panels (including System Health Monitor) are toggled via the main `Widgets` menu.

## Change Safety Workflow (Required)

These rules exist to prevent recurring regressions (UI freezes, silent failures, settings drift, and cross-subsystem breakage).

### 1) Impact-map-first
- Before editing any behavior in `app/MAIN_FILE_SINGLE_CAM.py`, `app/ui_builder.py`, `app/turret_enhancements.py`, `app/turret_presets.py`, or any `app/sentry_mode/*` files, read `CHANGE_IMPACT_REFERENCE.md` and identify impacted subsystems.
- If a change touches a “Sensitive Function” (see `CHANGE_IMPACT_REFERENCE.md` → Code-Level Change Enforcement), add/refresh a short **CHANGE WARNING** comment at the top of the modified function.
- Preserve any `AGENT-MANAGED BLOCK` markers exactly; do not hand-edit inside those blocks unless you also update the AgentChangeID/date and validate all couplings in the impact map.

### 2) Single source of truth (no split-brain state)
- Avoid “multiple sources of truth” bugs:
  - **Camera resolution**: `frame_width`/`frame_height` must be set at init/camera-open/resolution-change only. Do not recompute per-frame in `update_frame()`.
  - **Tracking/aiming flags**: maintain invariant `tracking_active=True` implies `aiming_active=True` (use the existing sync helper patterns; do not reintroduce desync).
  - **Tilt safety**: treat as optional hardware unless explicitly enabled; do not latch “locked” on generic “OK” status lines.

### 3) Settings file location (avoid config drift)
- The app can read/write different settings depending on CWD (notably when using `run.py`).
- When modifying settings keys or defaults:
  - Ensure `load_settings()` and `save_settings()` both include the key.
  - Log (or otherwise make clear) which settings file is active at runtime.
  - Do not silently add new keys without documenting them in `CHANGE_IMPACT_REFERENCE.md` if they affect behavior.

### 4) PyQt signal/slot correctness
- Checkable buttons must use `toggled(bool)` and handlers must accept the boolean (or an optional `checked=None`), not `clicked`.
- Verify handler signature matches the signal payload.
- Prefer `_safe_connect()` instead of raw `.connect()` to keep failures visible and consistent.

### 5) UI thread safety / responsiveness
- Never run blocking operations on the main Qt thread:
  - Serial connect (`serial.Serial(...)`) must be async.
  - Model loading/inference setup must not freeze the UI.
  - Camera open/close and device probing must not be done inside the frame paint/update hot-path.
- Only update Qt widgets on the main thread.
- Avoid Qt marshaling patterns that capture non-trivial Qt objects through queued connections; prefer main-thread direct calls when already on the UI thread, or marshal minimal primitives back via `QTimer.singleShot(0, callback)`.

### 6) No silent exceptions
- Do not add `except Exception: pass` in production paths.
- If an exception is intentionally suppressed, it must be logged with context (use the centralized logger helpers if available).

### 7) Verification required for risky changes
- After changes in these areas, run the tightest applicable checks:
  - Resolution: `python test_resolution_fix.py`
  - Servo gating/flags: `python servo_fix_test.py`
  - Serial connect behavior: `python SERIAL_CONNECTION_TEST.py` (or verify async connect path)
  - Startup smoke: `python test_app_start.py` or `python run.py`
- If you change detection mode UI visibility or persistence (e.g., Basic/Advanced toggle), verify:
  - Mode 0–9 UI visibility logic is correct
  - `detection_show_advanced` loads/saves
  - Color detection panel visibility helpers remain consistent

### 8) Documentation and change logging
- When a functional change is made:
  - Add/adjust an entry in `RECENT_UPDATES.json`.
  - Update `CHANGE_IMPACT_REFERENCE.md` if you discovered a new coupling, hidden dependency, or common failure mode.
- Keep documentation dates consistent and avoid machine-specific absolute paths in docs (use repo-relative paths).

## Pre-Change / Pre-Merge Checklist (Do This Every Time)

- Read the relevant section(s) in `CHANGE_IMPACT_REFERENCE.md` for the subsystem you’re touching.
- Confirm “single source of truth” invariants (resolution, flags, optional hardware gating).
- Confirm signal/slot signatures: checkable buttons use `toggled(bool)`.
- Confirm no blocking calls on the Qt main thread (serial/camera/model).
- Run the narrowest applicable verification script(s): `test_resolution_fix.py`, `servo_fix_test.py`, `SERIAL_CONNECTION_TEST.py`, `test_app_start.py`.
- Update `RECENT_UPDATES.json` (and `CHANGE_IMPACT_REFERENCE.md` if new couplings were found).

## Quick Troubleshooting Workflow (Bug Finding)

Use this when a bug is reported and you need to locate the most likely recent cause and fix it in the correct place.

1) **Reproduce + classify**
- Reproduce the issue with the smallest steps possible.
- Classify the subsystem: Camera/Resolution, Detection (0–9), UI/Signals, Serial/Arduino, Servo gating, Tilt safety, Sentry Mode.

2) **Check the most recent changes first**
- Read `RECENT_UPDATES.json` and scan for entries touching the subsystem.
- Use `git log -n 20` (and `git show <sha>`) to inspect the most recent commits that touch the relevant files.
- Use `git blame` on the suspicious block (especially around “AgentChangeID” markers and recent FIX comments).

3) **Confirm the active configuration source**
- Verify which settings file is active at runtime (CWD-dependent when using `run.py`).
- If behavior differs between `python run.py` and `python app/MAIN_FILE_SINGLE_CAM.py`, assume settings drift until proven otherwise.

4) **Validate invariants (fast sanity checks)**
- Resolution: ensure `frame_width/frame_height` are not being recomputed per-frame.
- Flags: ensure `tracking_active=True` implies `aiming_active=True`.
- UI: checkable buttons use `toggled(bool)` and handler signature accepts `checked`.
- Threading: confirm no blocking work is executed on the Qt main thread.
- Tilt safety: confirm optional hardware gating is respected; avoid latching on generic “OK” status lines.
- If the symptom is **“Pan drifts to max / Tilt not moving”**, follow the dedicated runbook in `CHANGE_IMPACT_REFERENCE.md` before tuning gains or changing tracking math.

5) **Fix in the correct layer (don’t patch symptoms)**
- UI wiring bugs belong in signal connections and handler signatures (prefer `_safe_connect`).
- Settings persistence bugs require edits in BOTH `load_settings()` and `save_settings()`.
- Performance/freezes require moving blocking work off the UI thread (thread + main-thread callback).
- Cross-module couplings: update `CHANGE_IMPACT_REFERENCE.md` when you find a new one.

6) **Verify with the narrowest checks**
- Run the smallest applicable test: `test_resolution_fix.py`, `servo_fix_test.py`, `SERIAL_CONNECTION_TEST.py`, `test_app_start.py`.
- Smoke-test the affected modes (especially detection modes 0–9 and Sentry tab interactions if touched).

## References
- See `README.md` for setup, troubleshooting, and hardware requirements.
- See `CAMERA_FIX_*`, `SERVO_*`, and `TOOLTIPS.md` for targeted fixes and documentation.
- For new presets or detection modes, update `turret_presets.py` and document changes.

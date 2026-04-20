# Smart Sentry v3.0.0 Compilation Protocol

This document is the active release-prep checklist for the Smart Sentry v3.0.0 release.

## 1. Release Targets

- App version string: `v3.0.0`
- Active version marker: `SMART_SENTRY_V3_0_VERSION.txt`
- Primary ESP32 WiFi sketch: `arduino/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR.ino`
- Primary ESP32 WiFi SSID: `SMART-SENTRY-V2.3`
- Primary ESP32 WiFi password: `db3000pass`
- Primary UDP endpoint: `192.168.4.1:9000`
- Compiled app output drive: `F:`
- Compiled app output folder: `F:\SMART SENTRY V3.0.0`
- Final packaged executable: `F:\SMART SENTRY V3.0.0\SMART_SENTRY_V3.0.0.exe`
- Validated runtime interpreter: prefer `F:\SMART SENTRY V2\.venv311\Scripts\python.exe` when present; otherwise use the active repo/workspace `.venv` selected by the build helper
- Build-helper interpreter resolution order: `SMART_SENTRY_PYTHON_EXE` override, parent `.venv311`, repo `.venv311`, parent `.venv`, repo `.venv`

Pinned firmware note: the current release does not use the Waveshare single-board bridge files. Treat all Waveshare firmware and bridge docs as on hold unless this protocol is explicitly revised.

## 1A. Current Release Gate

Previous blocker summary for the v3.0.0 packaging path:

1. Qt VC runtime DLL drift caused silent packaged `APPCRASH` on launch.
2. Packaged YOLO failed when runtime DLL search paths or packaged settings pointed at the wrong model surface.
3. Packaged settings and sound/transport values could drift away from the live WiFi firmware contract.

The hold that paused packaging on 2026-04-10 is cleared only for an operator-authorized rebuild attempt. A new build attempt must still complete the post-build verification in sections `5A` and `5B` before the release is treated as good.

## 2. Active Packaging Path

Use the current version-aware portable build helper from repository root:

```powershell
& ".\build_smart_sentry_v2_3_2_portable.ps1"
```

Notes:

1. The helper script name is historical, but the script now resolves the active release from `SMART_SENTRY_V3_0_VERSION.txt` first.
2. `run.py` is the canonical launcher entrypoint and now resolves the active release launcher dynamically.
3. The release package must still keep the executable as the only root-level file in the release folder.
4. `YOLO_MODELS` at the release root remains the only public packaged-model drop folder.
5. Do not invoke this build helper until the gate in section `1A` is explicitly cleared.
6. The build helper must refresh the bundled Qt VC runtime DLLs in `PyQt5\Qt5\bin` from `C:\Windows\System32` before smoke-testing the staged build and again after copying into the final release folder.
7. The build helper replaces the existing `F:\SMART SENTRY V3.0.0` folder in place after the staged smoke test passes.

## 2A. Known Packaging Regressions To Block

The following failures already occurred on the v3.0.0 path and must be treated as release blockers if they reappear:

1. **Silent packaged APPCRASH on launch**
	- Symptom: `SMART_SENTRY_V3.0.0.exe` appears to do nothing.
	- Root cause: stale Qt-bundled VC runtime DLLs in `SMART_SENTRY_V3_0_0_FILES\PyQt5\Qt5\bin`, especially `MSVCP140.dll` / `MSVCP140_1.dll` version `14.26.28720.3`.
	- Required prevention: keep the build-helper VC runtime refresh in place and verify the packaged Qt runtime DLLs are current-system copies, not the stale Qt-bundled versions.

2. **YOLO fails to load in the packaged app**
	- Symptom: the packaged app launches but cannot find or load YOLO weights.
	- Root cause class: packaged settings can carry the wrong `yolo_model_dir`, including stale source-repo absolute paths or temporary staging paths.
	- Required prevention: verify the packaged active settings file points `detection_mode.yolo_model_dir` at the final release-root `YOLO_MODELS` folder, not the source tree and not `.pyinstaller-temp`.

3. **No buzzer output from the packaged app**
	- Symptom: the app launches and connects, but no audible firmware buzzer cue is produced.
	- Root cause class: the packaged runtime can load the wrong saved settings surface or carry connection/sound values that do not match the live WiFi firmware path.
	- Required prevention: verify the packaged active settings file still targets the live WiFi endpoint and preserves the intended sound settings before sign-off.

4. **Frozen exe crashes with `cannot load module more than once per process` on numpy**
	- Symptom: `SMART_SENTRY_V3.0.0.exe` crashes immediately at startup with a PyInstaller `cannot load module more than once per process` error pointing at `numpy._core.__init__`.
	- Root cause: any module-level torch or numpy import in `app/main.py` executes when `run.py` does `from app.main import main`. `sentry_v2_detector` then tries to import numpy again via cv2. PyInstaller's frozen importer raises on the second exec of the same module. See ISS-075.
	- Required prevention: do not call `_preload_torch_runtime()` or any torch-importing helper at module scope in `app/main.py`. All torch/numpy imports must occur inside functions called after the full frozen import graph is resolved.

5. **Frozen exe crashes with `ModuleNotFoundError: No module named 'numpy._core._exceptions'`**
	- Symptom: `SMART_SENTRY_V3.0.0.exe` crashes at startup with `ModuleNotFoundError: No module named 'numpy._core._exceptions'` in the cv2→numpy import chain.
	- Root cause: NumPy 2.x restructured C extensions into `numpy._core.*` submodules that PyInstaller's standard hook does not enumerate. They are absent from the bundle unless explicitly collected. See ISS-076.
	- Required prevention: `--collect-submodules numpy` must remain in the `$pyInstallerArgs` array in `build_smart_sentry_v2_3_2_portable.ps1`. Do not remove it. If numpy is upgraded and a new submodule is missing, this flag will already cover it.

6. **Frozen exe YOLO prepare fails with `ModuleNotFoundError: No module named 'asyncio.base_events'`**
	- Symptom: packaged app launches and UI appears, but every YOLO load attempt fails silently. `SMART_SENTRY_V3_0_0_FILES\logs\yolo_runtime_diag.log` shows `prepare-failed` entries with `ModuleNotFoundError: No module named 'asyncio.base_events'`.
	- Root cause: `_prepare_yolo_runtime()` triggers `import torch`. `torch/__init__.py` uses `typing_extensions._deprecated`, which causes `asyncio/__init__.py` to execute. In Python 3.11, `asyncio/__init__.py` eagerly imports all `asyncio.*` submodules (including `asyncio.base_events`) at package init time. PyInstaller does not auto-collect these stdlib submodules, so they are absent from the frozen bundle. See ISS-077.
	- Required prevention: `--collect-submodules asyncio` must remain in the `$pyInstallerArgs` array in `build_smart_sentry_v2_3_2_portable.ps1`, placed after `--collect-submodules numpy`. Do not remove it. This is a Python 3.11 + PyInstaller regression that affects any frozen app that imports torch.

## 3. Release-Hold Validation

Before packaging v3.0.0, confirm the unfinished operator tabs stay on release hold:

1. `Facial Recognition` is absent from the active settings tab strip while it remains in `SETTINGS_TAB_RELEASE_HOLDS`.
2. `AI Assistant` is absent from the active settings tab strip while it remains in `SETTINGS_TAB_RELEASE_HOLDS`.
3. Previous and next settings-tab navigation still works across the remaining visible tabs.
4. App startup does not trigger release-held tab runtime behavior.
5. Removing a hold entry is sufficient to restore the tab without restructuring the settings-tab build path.
6. The release-hold convention remains documented in `SMART_SENTRY_RELEASE_HOLD_CONVENTION.md`.

## 4. Documentation Sync

Sync these files before sign-off:

1. `SMART_SENTRY_MANUAL.md`
2. `SMART_SENTRY_APP_CHANGE_IMPACT.md`
3. `SMART_SENTRY_RELEASE_HOLD_CONVENTION.md`
4. `RECENT_UPDATES.json`
5. `SMART_SENTRY_ISSUE_LOG.md`
6. This file

## 5. Compile-Readiness Checks

1. Confirm `SMART_SENTRY_V3_0_VERSION.txt` contains `3.0.0`.
2. Confirm the app title resolves to Smart Sentry v3.0.0 at runtime.
3. Confirm `run.py` uses a direct `from app.main import main` import with no version-dispatch logic. The versioned launcher chain (`run_smart_sentry_v2_3_2.py`, `run_smart_sentry_v3_0_0.py`) has been deleted. `app/main.py` is now the single canonical entry point for both source-run and packaged modes.
4. Confirm the packaging preflight resolves the active launcher module for v3.0.0.
5. Run file diagnostics on `app/sentry_v2/sentry_v2_tab.py`, `run.py`, `app/smart_sentry_meta.py`, and the build helper path before packaging.
6. From repository root, run `& ".\.venv\Scripts\python.exe" .\tools\camera_open_smoke_test.py` and confirm the result reports `ok: true`, `actual: [1280, 720]`, and `recovery_attempts: 0`.
7. If camera startup regresses, run `& ".\.venv\Scripts\python.exe" .\tools\camera_backend_probe.py` and verify Windows still prefers a stable backend before packaging; on this validation machine the correct order is `MSMF -> DEFAULT -> DSHOW`.
8. Confirm no one resumes packaging from the broken parent `.venv311\Scripts\python.exe` launch path if that interpreter is missing on the active machine.
9. Confirm the source defaults and runtime path logic treat `app/config/smart_sentry_v3_0_0_settings.json` as the active canonical release file while still accepting older aliases only as migration fallbacks.

## 5A. Post-Build Artifact Verification

After every successful build, inspect the actual promoted release at `F:\SMART SENTRY V3.0.0` before calling the compile complete.

1. Confirm the release root contains exactly:
	- `SMART_SENTRY_V3.0.0.exe`
	- `SMART_SENTRY_V3_0_0_FILES\`
	- `YOLO_MODELS\`
2. Confirm the packaged Qt runtime folder `SMART_SENTRY_V3_0_0_FILES\PyQt5\Qt5\bin` contains refreshed current-system copies of:
	- `msvcp140.dll`
	- `msvcp140_1.dll`
	- `msvcp140_2.dll`
	- `vcruntime140.dll`
	- `vcruntime140_1.dll`
3. Confirm the packaged Qt runtime DLLs are not the stale `14.26.28720.3` copies that cause silent `APPCRASH` on launch.
4. Inspect the packaged config directory under `SMART_SENTRY_V3_0_0_FILES\app\config` and confirm the active v3.0.0 settings file exists.
5. Open the packaged active settings file and verify:
	- `connection.udp_host` is `192.168.4.1`
	- `connection.udp_port` is `9000`
	- the canonical packaged settings file is `app/config/smart_sentry_v3_0_0_settings.json`
	- `detection_mode.yolo_model_dir` points at the final release-root `YOLO_MODELS` folder
	- `detection_mode.yolo_model_dir` does not point at `F:\SMART SENTRY V2\SMART SENTRY\YOLO_MODELS`
	- `detection_mode.yolo_model_dir` does not point anywhere under `.pyinstaller-temp`
	- `sound.enabled` remains `true` unless the operator intentionally disabled it
	- `sound.mute_buzzer_when_human_voice_enabled` matches the intended operator contract
6. Launch the packaged executable once from the final release folder and confirm it creates a real top-level window instead of silently exiting.
7. While connected to the live WiFi firmware path, run one manual sound/buzzer validation from the packaged app before final sign-off.
8. While connected to the packaged app, confirm one YOLO model loads successfully from the release-root `YOLO_MODELS` folder before final sign-off.

## 5B. Release Sign-Off Rule

Do not mark the v3.0.0 compile complete unless all three are true on the final promoted release artifact:

1. The packaged app launches without the Qt VC runtime crash.
2. A YOLO model loads from the packaged release surface.
3. The firmware buzzer path produces sound from the packaged app on the live WiFi link.

## 6. Firmware Note

The desktop release target is now v3.0.0, but the documented WiFi firmware baseline remains the existing Smart Sentry v2.3.1 UDP sketch until the firmware contract itself changes. Do not rename that sketch only to mirror the desktop app version.

For the current release, editors must treat `arduino/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE.ino` and related Waveshare bridge documents as archived bench material, not as part of the live Smart Sentry app path.

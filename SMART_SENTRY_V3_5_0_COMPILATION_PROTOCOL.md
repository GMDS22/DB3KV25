# Smart Sentry v3.5.0 Compilation Protocol (Historical Snapshot)

This file is retained as a historical release snapshot only.

For all current and future releases, use `SMART_SENTRY_BUILD_RELEASE_STANDARD.md` as the single authoritative build and release workflow.

## 1. Release Targets

- App version string: `v3.5.0`
- Active version marker: `SMART_SENTRY_V3_5_0_VERSION.txt`
- Desktop topology label: `NANO BOARD USB + DEBUG BOARD USB`
- Current live Nano IO firmware: `arduino/SMART_SENTRY_V3_0_NANO_USB_IO_PIR/SMART_SENTRY_V3_0_NANO_USB_IO_PIR.ino`
- Compiled app output drive: `F:`
- Compiled app output folder: `F:\SMART SENTRY V3.5.0`
- Final packaged executable: `F:\SMART SENTRY V3.5.0\SMART_SENTRY_V3.5.0.exe`
- Canonical runtime settings file: `app/config/smart_sentry_settings.json`
- Canonical custom presets file: `app/config/smart_sentry_custom_presets.json`
- Canonical prompted-targets file: `app/config/smart_sentry_prompted_targets.json`
- Canonical face-library file: `app/config/smart_sentry_faces.json`

## 2. Active Packaging Path

Use the current version-aware portable build helper from repository root:

```powershell
& ".\build_smart_sentry_v2_3_2_portable.ps1"
```

Notes:

1. The helper script name is historical, and now resolves the active release from the highest-priority available version marker.
2. `run.py` remains the canonical launcher entrypoint.
3. The release package must still keep the executable as the only root-level file in the release folder.
4. `YOLO_MODELS` at the release root remains the operator-facing packaged-model drop folder.
5. The helper resolves Python from `SMART_SENTRY_PYTHON_EXE`, then parent or repo `.venv311`, then parent or repo `.venv`.
6. Output must stay on drive `F:`.

## 3. Release Deltas To Preserve

For v3.5.0, the packaged runtime must preserve these user-visible behaviors:

1. The hero title resolves to `SMART SENTRY V3.5.0` and the subtitle resolves to `NANO BOARD USB + DEBUG BOARD USB`.
2. Theme controls include the added font-scale and settings-panel-width controls.
3. Water or MOSFET trigger runtime settings remain available through the same release build.
4. Auto-lighting keeps the fixed dim-scene behavior and live threshold or PWM readout.
5. Graceful shutdown must switch off LED, laser, ACC, and spare outputs and lock safety before disconnecting transport.

## 4. Pre-Build Checks

Before packaging v3.5.0, confirm all of the following:

1. `SMART_SENTRY_V3_5_0_VERSION.txt` contains `3.5.0`.
2. `app.smart_sentry_meta.get_version()` resolves `3.5.0`.
3. The app title resolves to `SMART SENTRY V3.5.0` at runtime.
4. The canonical versionless settings, presets, prompted-targets, and face-library files all exist.
5. Confirm current saved operator settings and current saved custom profiles are present in source canonical files before running the build.
6. The close path still sends a real outputs-off state before disconnecting boards.
7. The build helper still points packaged `detection_mode.yolo_model_dir` at the final release-root `YOLO_MODELS` folder.

## 5. Post-Build Verification

After every successful build, inspect the promoted release at `F:\SMART SENTRY V3.5.0`.

1. Confirm the release root contains `SMART_SENTRY_V3.5.0.exe`, `SMART_SENTRY_V3_5_0_FILES\`, and `YOLO_MODELS\`.
2. Confirm the packaged config directory contains the active `smart_sentry_settings.json` file.
3. Confirm the packaged config directory contains the active `smart_sentry_custom_presets.json` file and it matches the current source custom profile file.
4. Confirm the packaged active settings file points at `app/config/smart_sentry_settings.json` and `F:\SMART SENTRY V3.5.0\YOLO_MODELS`.
5. Launch the packaged executable once from the final release folder and confirm the title panel shows the v3.5.0 release identity.
6. Verify one live shutdown pass closes accessories before transport disconnect.

## 6. Historical Packaging Blockers

Retain the PyInstaller, NumPy, Torch, asyncio, unittest, and Qt VC runtime mitigations documented in `SMART_SENTRY_V3_0_0_COMPILATION_PROTOCOL.md` unless they are explicitly replaced in the same change.
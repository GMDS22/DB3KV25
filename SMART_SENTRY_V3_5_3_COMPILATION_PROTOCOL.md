# Smart Sentry v3.5.3 Compilation Protocol

This file is a release snapshot for v3.5.3.

For all current and future releases, use SMART_SENTRY_BUILD_RELEASE_STANDARD.md as the single authoritative build and release workflow.

## 1. Release Targets

- App version string: v3.5.3
- Active version marker: SMART_SENTRY_V3_5_3_VERSION.txt
- Desktop topology label: NANO BOARD USB + DEBUG BOARD USB
- Current live Nano IO firmware: arduino/SMART_SENTRY_V3_0_NANO_USB_IO_PIR/SMART_SENTRY_V3_0_NANO_USB_IO_PIR.ino
- Compiled app output drive: F:
- Compiled app output folder: F:\SMART SENTRY V3.5.3
- Final packaged executable: F:\SMART SENTRY V3.5.3\SMART_SENTRY_V3.5.3.exe
- Canonical runtime settings file: app/config/smart_sentry_settings.json
- Canonical custom presets file: app/config/smart_sentry_custom_presets.json
- Canonical prompted-targets file: app/config/smart_sentry_prompted_targets.json
- Canonical face-library file: app/config/smart_sentry_faces.json

## 2. Active Packaging Path

Use the version-aware portable build helper from repository root:

```powershell
& ".\build_smart_sentry_v2_3_2_portable.ps1"
```

Notes:

1. The helper script name is historical and resolves the active release from the highest-priority available version marker.
2. run.py remains the canonical launcher entrypoint.
3. The release package keeps the executable as the primary root-level app artifact in the release folder.
4. YOLO_MODELS at release root remains the operator-facing packaged-model drop folder.
5. The helper resolves Python from SMART_SENTRY_PYTHON_EXE, then parent or repo .venv311, then parent or repo .venv.
6. Output remains on drive F: unless explicitly overridden.

## 3. Release Deltas To Preserve

For v3.5.3, the packaged runtime must preserve these user-visible behaviors:

1. The hero title resolves to SMART SENTRY V3.5.3 and the subtitle resolves to NANO BOARD USB + DEBUG BOARD USB.
2. Canonical versionless runtime config filenames remain unchanged.
3. Water or MOSFET trigger runtime settings remain available through the same release build.
4. Auto-lighting keeps the fixed dim-scene behavior and live threshold or PWM readout.
5. Graceful shutdown must switch off LED, laser, ACC, and spare outputs and lock safety before disconnecting transport.

## 4. Pre-Build Checks

Before packaging v3.5.3, confirm all of the following:

1. SMART_SENTRY_V3_5_3_VERSION.txt contains 3.5.3.
2. app.smart_sentry_meta.get_version() resolves 3.5.3.
3. The app title resolves to SMART SENTRY V3.5.3 at runtime.
4. Canonical versionless settings, presets, prompted-targets, and face-library files all exist.
5. Current saved operator settings and current saved custom profiles are present in source canonical files before running the build.
6. The close path still sends a real outputs-off state before disconnecting boards.
7. The build helper points packaged detection_mode.yolo_model_dir at the final release-root YOLO_MODELS folder.

## 5. Post-Build Verification

After every successful build, inspect the promoted release at F:\SMART SENTRY V3.5.3.

1. Confirm the release root contains SMART_SENTRY_V3.5.3.exe, SMART_SENTRY_V3_5_3_FILES\, and YOLO_MODELS\.
2. Confirm the packaged config directory contains smart_sentry_settings.json.
3. Confirm the packaged config directory contains smart_sentry_custom_presets.json and that it matches the current source custom profile file.
4. Confirm the packaged settings file points at app/config/smart_sentry_settings.json, app/config/smart_sentry_prompted_targets.json, app/config/smart_sentry_faces.json, and release-root YOLO_MODELS.
5. Launch the packaged executable once from the final release folder and confirm the title panel shows the v3.5.3 release identity.
6. Verify one live shutdown pass closes accessories before transport disconnect.

## 6. Historical Packaging Blockers

Retain the PyInstaller, NumPy, Torch, asyncio, unittest, and Qt VC runtime mitigations documented in SMART_SENTRY_V3_0_0_COMPILATION_PROTOCOL.md unless they are explicitly replaced in the same change.

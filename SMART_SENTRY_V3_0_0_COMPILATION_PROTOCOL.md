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
- Standard editor and build interpreter: `F:\SMART SENTRY V2\.venv311\Scripts\python.exe`

Pinned firmware note: the current release does not use the Waveshare single-board bridge files. Treat all Waveshare firmware and bridge docs as on hold unless this protocol is explicitly revised.

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
3. Confirm `run.py` resolves the active launcher without a hard-coded v2.3.2 import.
4. Confirm the packaging preflight resolves the active launcher module for v3.0.0.
5. Run file diagnostics on `app/sentry_v2/sentry_v2_tab.py`, `run.py`, `app/smart_sentry_meta.py`, and the build helper path before packaging.

## 6. Firmware Note

The desktop release target is now v3.0.0, but the documented WiFi firmware baseline remains the existing Smart Sentry v2.3.1 UDP sketch until the firmware contract itself changes. Do not rename that sketch only to mirror the desktop app version.

For the current release, editors must treat `arduino/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE.ino` and related Waveshare bridge documents as archived bench material, not as part of the live Smart Sentry app path.

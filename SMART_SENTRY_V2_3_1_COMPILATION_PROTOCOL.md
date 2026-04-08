# Smart Sentry v2.3.1 Compilation Protocol

This document is the release-prep checklist for Smart Sentry v2.3.1.

Use it before compiling firmware, packaging the app, or publishing release artifacts.

## 1. Release Targets

- App version string: `v2.3.1`
- Primary ESP32 WiFi sketch: `arduino/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR.ino`
- Primary ESP32 WiFi SSID: `SMART-SENTRY-V2.3`
- Primary ESP32 WiFi password: `db3000pass`
- Primary UDP endpoint: `192.168.4.1:9000`
- Compiled app output drive: `F:`
- Compiled app output folder rule: always create a folder named with the exact app version, for example `F:\SMART SENTRY V2.3.1`
- Standard editor/runtime interpreter: `F:\SMART SENTRY V2\.venv311\Scripts\python.exe`

## 2. Mandatory Output Rule

Before every compile or packaging run:

1. Save all compiled app outputs to drive `F:`.
2. Create a fresh folder that contains the exact app version in its name.
3. Do not mix outputs from different app versions in the same folder.
4. Keep source files and compiled outputs separate.
5. If a release is rebuilt, replace the contents of that exact version folder intentionally rather than dropping files into an older folder.
6. Keep a repo-tracked source marker for the release so the app title and packaging metadata resolve to the same version that is being built.
7. The final packaged executable for this release must be named `SMART_SENTRY_V2.3.1.exe` and must live directly inside `F:\SMART SENTRY V2.3.1`.
8. The packaged executable must use the repo icon file `smart_sentry_icon.ico`.
9. The release root must keep `SMART_SENTRY_V2.3.1.exe` as the only root-level file; every other packaged artifact must live inside subfolders such as `_internal`, `app`, `docs`, or `YOLO_MODELS`.
10. Use `F:\SMART SENTRY V2.3.1\YOLO_MODELS` as the only release-facing YOLO model drop folder.
11. Bundled default YOLO weights may still live under `F:\SMART SENTRY V2.3.1\SMART_SENTRY_V2_3_1_FILES\YOLO_MODELS`, but operators should add or replace release models only through the root-level `YOLO_MODELS` folder.
12. Treat Python `3.11` plus `.venv311` as the only supported editor/build environment for this release line.
13. Do not point VS Code, PyInstaller, or ad hoc terminal work at `.venv` or a system `3.12` interpreter unless you are intentionally doing compatibility triage.

Recommended example for this release:

```text
F:\SMART SENTRY V2.3.1
F:\SMART SENTRY V2.3.1\SMART_SENTRY_V2.3.1.exe
```

## 2B. Standard Python Environment

Use this environment contract for all future Smart Sentry v2.3.1 edits, builds, and validation:

1. Use `C:\Users\GM\AppData\Local\Programs\Python\Python311\python.exe` as the base interpreter.
2. Use `F:\SMART SENTRY V2\.venv311\Scripts\python.exe` as the active workspace interpreter.
3. Keep `.venv311` as the default VS Code interpreter.
4. Treat `.venv` as a legacy troubleshooting environment, not the default release environment.
5. If PyQt5 is reinstalled, remove the local Qt-bundled VC runtime override files from `PyQt5\Qt5\bin` so Windows uses the current system VC++ runtime.
6. Keep `lap` installed inside `.venv311` so Ultralytics does not try to satisfy that dependency from another Python installation during packaging.

## 2A. Active Desktop Packaging Path

Use the current PyInstaller portable build path for this release:

1. Build helper: `build_smart_sentry_v2_3_1_portable.ps1`
2. Packager: `python -m PyInstaller` (invoked by the build helper)
3. Launcher entrypoint: `run.py`

Legacy `setup_smart_sentry_v3_portable.py` and `.spec` files may remain in the repo for older packaging paths, but they are not the primary v2.3.1 release workflow unless you intentionally choose to revive and revalidate them.

## 3. Firmware Areas To Update Before Compile

Update these items every time the firmware version changes:

1. Sketch folder name and `.ino` filename must match the release version.
2. The top-of-sketch banner comment must match the real sketch name and target app version.
3. The boot banner in `setup()` must match the release version.
4. `caps["fw"]` must match the actual firmware identity string.
5. `WIFI_SSID` must match the release SSID standard.
6. Capability flags reported to the app must reflect real firmware behavior.
7. Manual action names such as `{"action":"sweep"}` must match the app transport code.
8. If any GPIO role changes, update the pin comments and `validate_pins()` output.

## 4. App Areas To Update Before Compile

Review these app-side areas before packaging:

1. WiFi credential constants and mode-routing logic.
2. Manual-control buttons and labels for firmware-owned actions.
3. Tooltips or explanatory notes that describe changed firmware behavior.
4. Packaging labels, launcher text, and versioned output folder names.
5. Any path that still points to an older release as the active build.
6. The active version marker file used by the app title resolver.

## 5. Documentation Areas To Update Before Compile

At minimum, sync these files when the release version changes:

1. `ESP32_CURRENT_SKETCH.md`
2. `ESP32_UDP_FLASH.md`
3. `SMART_SENTRY_APP_CHANGE_IMPACT.md`
4. `SMART_SENTRY_MANUAL.md`
5. `SMART_SENTRY_ISSUE_LOG.md`
6. `SMART_SENTRY_V2_3_1_LIVE_VALIDATION_CHECKLIST.md`
7. `RECENT_UPDATES.json`
8. This file

If topology, wiring, transport, or packaging changed, also review:

1. Pin reference docs
2. Quick-start docs
3. Bench or flash notes
4. Packaging or release logs

## 6. Naming Standard

Use these rules for future Smart Sentry releases:

1. The sketch folder and `.ino` filename must include the app version they are created for.
2. The top-of-sketch description must match the filename exactly.
3. The boot banner printed over serial must match the active release family.
4. The firmware capability string must identify the real release contract, not a legacy predecessor.
5. The compiled app output folder on `F:` must include the exact app version.
6. Each release must keep prior unreverted UI and behavior improvements unless they are intentionally removed and documented.
7. Each release should be traceable in the repo through a dedicated version file, commit, or clearly preserved release copy.

## 7. Verification Before Compile

Run this check sequence before release packaging:

1. Confirm the primary sketch path in `ESP32_CURRENT_SKETCH.md` matches the file you will flash.
2. Confirm the flash command in `ESP32_UDP_FLASH.md` points to the same sketch.
3. Confirm app WiFi credentials match the firmware SSID and password.
4. Confirm new manual actions work through the app transport.
5. Confirm docs no longer point to the previous release as the active baseline.
6. Confirm the destination output folder exists on `F:` and contains the exact version name.
7. Compile the sketch.
8. Run app error checks before packaging.
9. Save the packaged app into the versioned `F:` folder.
10. Confirm the packaged executable file name is exactly `SMART_SENTRY_V2.3.1.exe` inside that versioned `F:` folder.
11. Confirm the packaged executable uses the repo icon file `smart_sentry_icon.ico`.
12. Confirm the release root contains only the versioned executable as a file and that all other packaged content is grouped into subfolders.
13. Confirm the visible app header and launcher title match the active release version.
14. In fixed guard mode, verify target loss completes the recovery scan and returns to the configured guard position instead of drifting off-home.
15. Confirm the toggleable scope reticle uses the current operator-approved palette and does not draw a filled center marker.
16. Run the live checklist in `SMART_SENTRY_V2_3_1_LIVE_VALIDATION_CHECKLIST.md` against the packaged build in `F:`.
17. Confirm VS Code still points at `.venv311` before any package install, error check, or packaging run.

## 8. Flash Command For v2.3.1

From repository root:

```powershell
& ".\SMART SENTRY\tools\flash_esp32_udp.ps1" -Port COM28 -Sketch "arduino/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR.ino"
```

## 9. Desktop Build Command For v2.3.1

Use the version-aware portable build helper from repository root:

```powershell
& ".\build_smart_sentry_v2_3_1_portable.ps1"
```

Notes:

1. This is the active desktop packaging path for the current Smart Sentry release workflow.
2. The script reads `SMART_SENTRY_V2_3_1_VERSION.txt`, builds through `python -m PyInstaller`, reshapes the package so the exe is the only root-level file, and copies the result into the required `F:\SMART SENTRY V2.3.1` release folder.
3. The final exe contract for this release is `F:\SMART SENTRY V2.3.1\SMART_SENTRY_V2.3.1.exe`.
4. The exe icon must come from repo file `smart_sentry_icon.ico`.
5. `F:\SMART SENTRY V2.3.1\YOLO_MODELS` is the canonical packaged-model folder; do not treat `app\YOLO_MODELS` or `app\models` as release drop targets.
6. Bundled default models may also exist under `F:\SMART SENTRY V2.3.1\SMART_SENTRY_V2_3_1_FILES\YOLO_MODELS`; that support-folder copy is for packaged defaults, not operator drop-ins.
7. The release root should contain folders such as `_internal`, `app`, `docs`, and `YOLO_MODELS`, but the only root-level file should be `SMART_SENTRY_V2.3.1.exe`.
8. The default no-argument build now prefers `.venv311` when present, falls back to `.venv` only if needed, and can be explicitly pointed elsewhere with `SMART_SENTRY_PYTHON_EXE`.
9. The default no-argument build is now the full portable release: it bundles the local `YOLO_MODELS` tree, keeps scikit-learn enabled, keeps yt-dlp enabled, and patches the packaged settings to the bundled release model folder.
10. Use `-ExcludeModels`, `-ExcludeSklearn`, or `-ExcludeYtDlp` only when you intentionally want a smaller or reduced-capability portable package footprint.

Offline-safe packaging note:

1. The build helper is intended to run entirely from the already provisioned local venv at `F:\SMART SENTRY V2\.venv`.
2. The preferred local build environment is now `F:\SMART SENTRY V2\.venv311` on Python 3.11.
3. Do not rely on live package downloads during packaging.
4. If internet access drops during packaging, the build should still complete as long as the local venv already contains the required packages and the local `YOLO_MODELS` folder contains the models you want bundled.

## 10. Important Release Notes

These points should always be checked during release prep:

1. Do not trust old sketch banners alone; the documented sketch path is the source of truth.
2. Do not change SSID, password, port, or topology wording in one place only.
3. Do not rename a sketch without renaming its folder, docs, and flashing examples.
4. Do not leave old version numbers in UI labels, docs, or output folders.
5. Do not package a build until source and firmware documentation agree on the active release.
6. If the app depends on a firmware action, the firmware capability packet and the app UI must be updated together.
7. If the output is meant for delivery, verify the package in the `F:` version folder, not from an older build cache.
8. Do not treat generated bench artifacts under `platformio/**/.pio/**` or runtime exports under `snapshots/` as release-source files for the desktop package.

## 12. Future Traceability Hardening

Add these quality-of-life items in the next version so future failures are faster to isolate:

1. Add a build switch that writes the full PyInstaller output to a UTF-8 log file by default instead of relying on terminal scrollback.
2. Emit the selected Python interpreter, Python version, and resolved runtime DLL name at the top of every packaging run.
3. Add a post-build manifest file in the release root that records exe version, interpreter version, model folder contents, and canonical config names.
4. Add a packaging self-check that warns when VS Code or the terminal is using an interpreter outside `.venv311`.
5. Add a release smoke-test command that launches the packaged app with a short timeout and captures stdout or Windows event failures to a dedicated log file.
6. Add a one-command dependency snapshot export for `.venv311` so rebuilds can be compared quickly after environment drift.

## 11. v2.3.1-Specific Notes

This release changes the sweep contract:

1. GPIO0 is no longer used as a runtime sweep input.
2. GPIO0 remains reserved for ESP32 BOOT behavior only.
3. Sweep is now started by the app through a dedicated manual control button.
4. The firmware receives that request as `{"action":"sweep"}` over UDP.

Current Smart Sentry app-side prep notes for this release:

1. Motion-led preview smoothness is now handled by presentation throttling in `app/sentry_v2/sentry_v2_tab.py`; do not regress this by reintroducing detector-side cadence throttling without revalidation.
2. Target loss in fixed guard mode must end in a clean return to guard after the bounded recovery search in `app/sentry_v2/sentry_v2_engine.py`.
3. Threat AI status, ML folder access, and saved-data summaries now rely on `app/sentry_v2/ml_training_logger.py`, `app/sentry_v2/sentry_v2_engine.py`, and `app/sentry_v2/sentry_v2_tab.py` remaining aligned.
4. The current scope overlay contract is a no-center-fill reticle with neutral black/grey/white geometry unless temporary fire feedback is active.
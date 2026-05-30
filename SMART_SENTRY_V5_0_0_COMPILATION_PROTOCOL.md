# SMART SENTRY V5.0.0 COMPILATION PROTOCOL

Date: 2026-05-30
Status: Build-prep protocol for v5 release packaging
Output target: F:\\SMART SENTRY V5.0.0

This protocol prepares and validates the v5 release surface before executing the portable build helper.

## 1. Required release identity

- Version marker must exist: `SMART_SENTRY_V5_0_0_VERSION.txt`
- Marker content must be `5.0.0`
- Runtime title and packaged output names are derived from the active marker via `app/smart_sentry_meta.py`

## 2. Canonical runtime persistence contract (must preserve)

The build must include and preserve all four versionless canonical runtime files:

- `app/config/smart_sentry_settings.json`
- `app/config/smart_sentry_custom_presets.json`
- `app/config/smart_sentry_prompted_targets.json`
- `app/config/smart_sentry_faces.json`

These are authoritative runtime files. Legacy `smart_sentry_v*_*.json` files remain migration inputs only.

## 3. Preflight commands (mandatory before build)

Run from the `SMART SENTRY` folder:

```powershell
..\.venv\Scripts\python.exe tools\validate_packaging_entrypoints.py
```

```powershell
..\.venv\Scripts\python.exe tools\validate_build_surface_v5.py
```

Both commands must report success.

## 4. Dependency accountability surface

Dependency manifest (must stay current):

- `requirements-sentry-v2-portable.txt`

Required dependency groups:

- Core runtime: `numpy`, `opencv-python`, `pyserial`, `PyQt5`, `sounddevice`, `simpleaudio`, `requests`
- Detection/tracking: `ultralytics`, `torch`, `lap`
- Speech/voice: `vosk`, `edge-tts`, `kokoro-onnx`, `azure-cognitiveservices-speech`
- Optional packaged capabilities (included in standard helper checks): `scikit-learn`, `yt-dlp`
- Build tooling: `PyInstaller`, `cx-Freeze`

## 5. Required model and asset contract

Must exist before build:

- `YOLO_MODELS/` with at least one model file (`.pt`, `.onnx`, `.engine`, or `.torchscript`) for full model builds
- `models/kokoro/kokoro-v1.0.onnx`
- `models/kokoro/voices-v1.0.bin`
- `models/vosk/`
- `app/LOGO.png`
- `smart_sentry_icon.ico`

## 6. Build command

```powershell
& ".\build_smart_sentry_v2_3_2_portable.ps1"
```

Optional flags:

```powershell
& ".\build_smart_sentry_v2_3_2_portable.ps1" -IncludeModels -IncludeSklearn -IncludeYtDlp -Clean
```

## 7. Post-build verification

Verify in `F:\\SMART SENTRY V5.0.0`:

- `SMART_SENTRY_V5.0.0.exe` exists
- `SMART_SENTRY_V5_0_0_FILES/` exists
- Release-root `YOLO_MODELS/` exists
- Support-folder `models/` includes Kokoro assets
- `SMART_SENTRY_V5_0_0_FILES/app/config/` contains all four canonical runtime files
- Packaged hashes for canonical files match source hashes
- Launch smoke test passes (app remains running for at least the scripted smoke window)

## 8. Documentation and change log alignment

If any build flow, packaging include, or persistence contract changes, update all:

- `SMART_SENTRY_BUILD_RELEASE_STANDARD.md`
- `SENTRY_V2_PORTABLE_INCLUDE_LIST.md`
- `SMART_SENTRY_APP_CHANGE_IMPACT.md`
- `SMART_SENTRY_MANUAL.md`
- `RECENT_UPDATES.json`

## 9. Release safety notes

- Do not weaken transport or fire-gate safety contracts for build convenience.
- Do not rename canonical config files with version tokens.
- Keep large runtime models on Git LFS where appropriate.

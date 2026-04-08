# Smart Sentry v2 Portable Fix Log (2026-03-24)

## Scope

Finalize Smart Sentry v2 for standalone portable packaging preparation.
No major logic changes were introduced.

## Issues Found and Fixes Applied

1. Root launcher self-import ambiguity
- Issue: root run_sentry_v2.py could ambiguously import itself when loading app launcher.
- Fix: switched to explicit path-based import via importlib.util.spec_from_file_location.
- File: run_sentry_v2.py

2. Standalone launcher coupling to optional main-app helper modules
- Issue: app/run_sentry_v2.py required db3k_meta and theme_manager unconditionally.
- Fix: added safe fallbacks for get_app_title() and ThemeManager import failures.
- File: app/run_sentry_v2.py

3. Non-portable absolute settings paths persisted in Smart Sentry v2 config
- Issue: prompted_library_path and config_path could persist absolute machine paths.
- Fix: added repo-relative portable path normalization in save/load path handling.
- File: app/sentry_v2/sentry_v2_tab.py

4. YOLO discovery and release-folder contract drifted from the portable packaging protocol
- Issue: packaged builds exposed bundled default models only under the versioned support folder, while release docs told operators to use the release-root YOLO_MODELS folder.
- Fix: restored release-root `YOLO_MODELS` as the public drop folder, kept support-folder defaults as bundled fallbacks, and updated frozen model discovery to prefer the release-root folder while still seeing bundled defaults.
- File: app/sentry_v2/sentry_v2_tab.py, build_smart_sentry_v2_3_1_portable.ps1

5. Default model name not present in tracked model files
- Issue: default yolo_model_name was ratdogcat.pt (missing tracked file).
- Fix: changed default to ratdogcat_last.pt (tracked file).
- File: app/sentry_v2/sentry_v2_config.py

6. Portable dependency manifest was incomplete/ambiguous
- Issue: root requirements referenced missing optional requirements files and did not provide a dedicated Smart Sentry v2 portable manifest.
- Fix: created dedicated manifest with explicit runtime dependencies.
- File: requirements-sentry-v2-portable.txt

7. Portable build still depended on manual model copying and could inherit a machine-local YOLO path into the packaged release
- Issue: the standard build path did not bundle local models by default, the tracked config pointed at a temporary user-folder model path, and packaged settings could land on a dead machine-specific directory.
- Fix: changed the portable build helper so the default build is the full release, validates local package availability for offline-safe packaging, bundles the local YOLO model tree automatically, mirrors bundled models into the support-folder fallback location, and rewrites packaged configs to the bundled release model directory.
- File: build_smart_sentry_v2_3_1_portable.ps1, app/config/smart_sentry_v3_settings.json, app/config/sentry_v2_settings.json

8. Python 3.12 plus PyQt5 local runtime drift made source-run stability weaker than the packaged 3.11 path
- Issue: local PyQt5 installs could reintroduce stale VC runtime DLLs into `PyQt5\Qt5\bin`, and the workspace default editor/build path could drift back to Python 3.12.
- Fix: standardized the release workflow on Python 3.11 in `.venv311`, added interpreter override support plus 3.11 preference to the portable build helper, pinned VS Code to `.venv311`, and documented removal of the local Qt-bundled VC runtime override DLLs after PyQt reinstall.
- File: build_smart_sentry_v2_3_1_portable.ps1, .vscode/settings.json, SMART_SENTRY_V2_3_1_COMPILATION_PROTOCOL.md

## Portable Build Asset Tracking Docs Added

- SENTRY_V2_PORTABLE_INCLUDE_LIST.md
- SENTRY_V2_PORTABLE_FIX_LOG_2026-03-24.md

## Validation Performed

- Python compile validation of modified launch and Smart Sentry v2 modules.
- Import path validation for root and app launcher alignment.
- Static verification of model folder presence and tracked config assets.

## Notes

- Existing unrelated workspace changes were intentionally not modified.
- This change set is preparation for packaging only; compilation/build execution is not started in this log.

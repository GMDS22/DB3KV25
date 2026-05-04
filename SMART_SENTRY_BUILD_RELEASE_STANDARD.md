# Smart Sentry Build and Release Standard

This is the single authoritative build and release process for Smart Sentry desktop releases.

If any older protocol document conflicts with this file, this file wins.

## 1. Scope and non-negotiable rules

- One release version marker is authoritative for a build run: the highest-priority existing marker resolved by the app (`SMART_SENTRY_V3_5_3_VERSION.txt`, then older markers).
- Only the UI release identity changes per release (`SMART SENTRY V<version>` title and output folder/exe names).
- Runtime config filenames are versionless and must not be renamed per release:
  - `app/config/smart_sentry_settings.json`
  - `app/config/smart_sentry_custom_presets.json`
  - `app/config/smart_sentry_prompted_targets.json`
  - `app/config/smart_sentry_faces.json`
- Legacy `smart_sentry_v*_*.json` files are migration inputs only.
- Build output drive remains `F:` unless the build helper is intentionally changed.
- Every release build must include the current saved canonical runtime settings and current saved canonical custom profile file from source `app/config/`.

## 2. Source of truth files

- Build helper: `build_smart_sentry_v2_3_2_portable.ps1`
- Build config helper: `smart_sentry_build_config.py`
- Runtime version resolver: `app/smart_sentry_meta.py`
- Runtime config load/migration logic: `app/sentry_v2/sentry_v2_tab.py`
- Runtime config defaults/schema: `app/sentry_v2/sentry_v2_config.py`
- Release-hold policy: `SMART_SENTRY_RELEASE_HOLD_CONVENTION.md`

## 3. Standard build steps (all editors)

1. Open PowerShell at repo root (`SMART SENTRY`).
2. Ensure the intended version marker file exists and contains the correct version string.
3. Confirm canonical config files exist under `app/config/` with versionless names.
4. Run build helper:

```powershell
& ".\build_smart_sentry_v2_3_2_portable.ps1"
```

Optional flags:

```powershell
& ".\build_smart_sentry_v2_3_2_portable.ps1" -IncludeModels
& ".\build_smart_sentry_v2_3_2_portable.ps1" -IncludeSklearn
& ".\build_smart_sentry_v2_3_2_portable.ps1" -IncludeYtDlp
& ".\build_smart_sentry_v2_3_2_portable.ps1" -Clean
```

## 4. Mandatory post-build verification

Verify release folder `F:\SMART SENTRY V<version>`:

1. Root contains:
- `SMART_SENTRY_V<version>.exe`
- `SMART_SENTRY_V<version_token>_FILES\`
- `YOLO_MODELS\`

2. Packaged config folder contains versionless canonical files:
- `app/config/smart_sentry_settings.json`
- `app/config/smart_sentry_custom_presets.json`
- `app/config/smart_sentry_prompted_targets.json`
- `app/config/smart_sentry_faces.json`

2.1 Canonical profile parity rule:
- Packaged `app/config/smart_sentry_custom_presets.json` must match the source file byte-for-byte (same custom profiles/operators presets).

3. In packaged `smart_sentry_settings.json`, verify:
- `config_path` is `app/config/smart_sentry_settings.json`
- `prompted_library_path` is `app/config/smart_sentry_prompted_targets.json`
- `face_recognition.library_path` is `app/config/smart_sentry_faces.json`
- `detection_mode.yolo_model_dir` points to release-root `YOLO_MODELS`
- all operator-tuned values (guard/rest/waypoints and engagement tuning) remain present except intentional packaging overrides above

4. Launch packaged exe once and confirm title identity resolves to `SMART SENTRY V<version>`.
5. Verify one graceful shutdown pass switches outputs off and safety lock before transport disconnect.

## 5. Release bump process (version-independent structure)

When creating a new release:

1. Update only release identity inputs:
- active version marker file content
- user-facing release notes/changelog identity text

2. Do not introduce new versioned config filenames.
3. Do not change canonical config paths.
4. Keep fallback migration logic intact unless migration behavior itself is the target of change.

## 6. Documentation update contract

Any change to build/release flow or runtime config persistence must update all:

- This file (`SMART_SENTRY_BUILD_RELEASE_STANDARD.md`)
- `SMART_SENTRY_MANUAL.md` (runtime persistence text)
- `SMART_SENTRY_APP_CHANGE_IMPACT.md` (canonical runtime facts/checklists)
- `SENTRY_V2_PORTABLE_INCLUDE_LIST.md` (packaging include intent)
- `RECENT_UPDATES.json` (concise note when release process/contract changes)

## 7. Anti-regression guardrails

- Never use per-release canonical config names in new code.
- Never treat legacy versioned files as authoritative runtime outputs.
- Keep migration deterministic: read newest available legacy input only when canonical file is missing.
- Keep transport behavior centralized in `app/sentry_v2/sentry_v2_comm.py`.
- Keep release-hold tabs controlled only by `SETTINGS_TAB_RELEASE_HOLDS` policy.

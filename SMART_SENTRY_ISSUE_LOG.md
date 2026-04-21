# SMART SENTRY ISSUE LOG

> Comprehensive issue tracker and troubleshooting reference for Smart Sentry.
> All issues investigated, all fixes attempted — including failures.
> Smart Sentry issues **only** — do not add main-app-only issues.

---

## How to Use This Document

1. **Experiencing a problem?** Check the [Quick Troubleshooting Reference](#quick-troubleshooting-reference) first.
2. **Investigating a new issue?** Search this file by symptom keyword (`Ctrl+F`).
3. **Fixing something?** Add a new entry at the top of the [Issue Log](#issue-log) section using the format below.
4. **Retrying a past fix?** Check the [Known Unresolved Issues](#known-unresolved-issues) section before starting.

## Entry Format

```
### ISS-NNN | YYYY-MM-DD | vX.Y.Z | Category | Result
**Short Title**

- **Symptoms**: What the operator sees or experiences
- **Root Cause**: Technical reason for the failure
- **Fix/Solution**: Exact change made (include constant values, thresholds, logic)
- **Files Modified**: Source files changed
- **Notes**: Diagnostic tips, related issues, recurrence risk (optional)
```

| Field | Values |
|-------|--------|
| **Category** | `Camera`, `Engine`, `UI`, `Firmware`, `Detection`, `Build`, `Config` |
| **Result** | `Worked`, `Did Not Work`, `Partial` |

---

## Quick Troubleshooting Reference

### Camera Won't Open / Keeps Reopening
| Check | Reference |
|-------|-----------|
| Recovery counter resetting during recovery reopen | [ISS-001](#iss-001) |
| Resolution too high for webcam driver | [ISS-004](#iss-004) |
| Backend probe order (MSMF → DEFAULT → DSHOW) | [ISS-005](#iss-005) |
| Health grace window after open | [ISS-006](#iss-006) |
| Partial frames (tl_mean > 0 but br_max = 0) | [ISS-001](#iss-001), [ISS-008](#iss-008) |
| Cross-thread capture sharing (Windows unsafe) | [ISS-018](#iss-018) |

### Video Looks Blurry / Wrong Resolution
| Check | Reference |
|-------|-----------|
| Windows backend selected DSHOW instead of MSMF on this machine | [ISS-005](#iss-005) |
| `camera_width`/`camera_height` in config files | [ISS-004](#iss-004) |

### Video Has Artifacts / Black Corners
| Check | Reference |
|-------|-----------|
| `border-radius` on `QLabel#sentryV2Video` | [ISS-003](#iss-003) |
| Frame buffer not detached from OpenCV | [ISS-018](#iss-018) |

### YOLO/Detection Not Promoting to Engagement
| Check | Reference |
|-------|-----------|
| `min_threat_score` too high for YOLO person detections | [ISS-070](#iss-070) |
| Semantic-confirm frames requiring same `track_id` across search pans | [ISS-073](#iss-073) |

### Tracking Feels Off / Overshoots
| Check | Reference |
|-------|-----------|
| EMA cold-start seeding | [ISS-012](#iss-012) |
| Engagement response scale range | [ISS-013](#iss-013) |
| Aim settle time scaling | [ISS-011](#iss-011) |
| Stale loss-recovery anchor after target switch | [ISS-009](#iss-009) |
| PID derivative damping too low (`precision_kd`) | [ISS-070](#iss-070) |

### Turret Won't Return Home After Engagement
| Check | Reference |
|-------|-----------|
| `_update_returning()` handling non-static guard modes | [ISS-014](#iss-014) |
| PIR no-target return-home move | [ISS-025](#iss-025) |
| Target-loss recovery expiration | [ISS-046](#iss-046) |

### Loss Recovery Completes Without Re-detecting a Visible Target
| Check | Reference |
|-------|-----------|
| `semantic_min_confirm_frames ≥ 2` — ByteTrack ID resets after each search pan | [ISS-073](#iss-073) |
| `target_loss_timeout` too short; add more search time | [ISS-073](#iss-073) |
| `loss_local_search_pan/tilt_deg` too narrow; person is outside sweep | [ISS-072](#iss-072), [ISS-073](#iss-073) |

### PIR Sensors Seem One-Sided / Search Not Visible
| Check | Reference |
|-------|-----------|
| `cross_sensor_lockout_ms` too high or PIR logs hidden under `system` | [ISS-069](#iss-069) |
| PIR hunt moves deferred before the previous move finished settling | [ISS-069](#iss-069) |

### Fire Not Triggering / Triggering Too Fast
| Check | Reference |
|-------|-----------|
| Aim-lock timeout refractory guard | [ISS-010](#iss-010) |
| Early fire vs settle timer | [ISS-015](#iss-015) |
| Burst fire blocking UI thread | [ISS-037](#iss-037) |
| `fire_trigger_enter_pan/tilt_tolerance` tighter than YOLO natural jitter (auto-fire never fires) | [ISS-071](#iss-071) |
| Auto-trigger toggle enabled but stale fire-gate settings stayed loaded in memory | [ISS-074](#iss-074) |

### Detection Stalls After Changes
| Check | Reference |
|-------|-----------|
| `_last_engage_time` not cleared on runtime reset | [ISS-021](#iss-021) |
| Motion-locked fallback dropped by class filter | [ISS-055](#iss-055) |

### Key Files for Camera Issues
- `app/sentry_v2/sentry_v2_tab.py` — camera open/close, health checks, recovery, frame pipeline
- `app/config/smart_sentry_v3_settings.json` — `camera_width`, `camera_height`, `camera_source`
- `tools/camera_backend_probe.py` — direct backend comparison utility used during 1280×720 validation
- `tools/camera_open_smoke_test.py` — in-app camera-open validation used before release sign-off
- Health constants: `_MAX_CAMERA_BLACK_FRAMES=8`, `_MAX_CAMERA_PARTIAL_FRAMES=6`, `_MAX_GRAB_FAILS=90`, `_CAMERA_HEALTH_GRACE_AFTER_OPEN_S=2.0`, `_MAX_CAMERA_RECOVERY_ATTEMPTS=3`

### Key Files for Engine/Tracking Issues
- `app/sentry_v2/sentry_v2_engine.py` — aiming, engagement, loss recovery, guard return
- `app/sentry_v2/sentry_v2_config.py` — all persisted tuning fields

### Key Files for Overlay/Display Issues
- `app/sentry_v2/sentry_v2_overlay.py` — HUD rendering, `_font_scale()`, `_ui_scale()`
- `app/sentry_v2/sentry_v2_video_canvas.py` — QLabel video display with aspect-ratio scaling

---

## Issue Log

Issues numbered newest-first. Search by symptom, file name, or category with `Ctrl+F`.

---

### ISS-083 | 2026-04-21 | v3.0.0 | Build | Worked
**Frozen Exe YOLO Prepare Fails — `ImportError: cannot import name '_version' from partially initialized module 'PIL'`**

- **Symptoms**: After ISS-082 (torch.testing) was fixed, the EXE launched but YOLO prepare still failed. `yolo_runtime_diag.log` showed `prepare-failed` with `ImportError: cannot import name '_version' from partially initialized module 'PIL' (most likely due to a circular import)`. Traceback: `_prepare_yolo_runtime` → `import ultralytics` → `ultralytics/__init__.py:13` → `ultralytics.utils` → `ultralytics.utils.patches:15` → `from PIL import Image` → `PIL/__init__.py:18` → `from . import _version` → ImportError.
- **Root Cause**: `PIL/__init__.py` at line 18 does `from . import _version` to set `__version__`. In the frozen bundle, `_prepare_yolo_runtime` runs on a worker thread. If anything (e.g. cv2's data path) has already placed a partially-initialized `PIL` entry in `sys.modules` before PIL's `__init__` completed, the second access via the relative import `from . import _version` finds PIL in `sys.modules` as partially initialized and raises ImportError. This is a thread-safety/ordering issue in PyInstaller's frozen importer: relative imports inside a package's `__init__` can fail if the parent package is already in `sys.modules` as partially initialized from a concurrent import path.
- **Fix/Solution**: Added `import PIL` and `import PIL.Image` to `run.py` on the main thread, immediately after the `import torch.testing` pre-import. This fully initializes PIL in `sys.modules` before any worker thread can trigger a partial import. When `_prepare_yolo_runtime`'s `from PIL import Image` fires, PIL is already complete in `sys.modules` and the relative import of `_version` is never re-executed.
- **Files Modified**: `run.py`
- **Notes**: PIL 12.2.0 (`_version.__version__ = "12.2.0"`). PIL `__init__.py` line 18 does `from . import _version` then immediately `del _version` after extracting `__version__`. The `del _version` is fine at runtime but the partial-init race only affects the import step. The same pre-import pattern has been used for asyncio (ISS-077), unittest (ISS-078), torchgen (ISS-079), torch.testing (ISS-080/081/082). Related: ISS-082.

---

### ISS-082 | 2026-04-21 | v3.0.0 | Build | Worked
**Frozen Exe crash at startup — `ModuleNotFoundError: No module named 'torch.testing'` (ISS-081 fix ineffective)**

- **Symptoms**: Build 6 EXE (after ISS-081 explicit `collect_submodules("torch.testing")` fix) still crashes at startup with `Unhandled exception in script: No module named 'torch.testing'`. Build 6 log confirmed `custom hook-torch: explicitly added 95 torch.testing submodules (ISS-081)`, but ALL 95 were logged as `ERROR: Hidden import '...' not found` during analysis. The `torch/testing/` folder was absent from the bundle and `torch.testing` was absent from the PYZ.
- **Root Cause**: When PyInstaller processes hiddenimports, it analyzes each module by attempting to import it in a sandboxed AST walker. For `torch.testing`, this requires analyzing `torch.testing.__init__`, which imports `from torch._C import FileCheck`. `torch._C` is a compiled C extension (`.pyd`) — PyInstaller cannot statically analyze it, so the entire `torch.testing` package tree is reported as "not found" and excluded from the PYZ. Adding module names via `collect_submodules` only registers strings as hiddenimport candidates; the analysis step still fails. This is distinct from the `on_error="ignore"` path — `collect_submodules` itself succeeds, but the subsequent per-module analysis in PyInstaller's graph fails silently.
- **Fix/Solution**: Changed approach entirely — direct filesystem `glob.glob(torch/testing/**/*.py)` scan building `datas` tuples manually. `collect_data_files("torch.testing", includes=["**/*.py"])` was tried first but returns empty because PyInstaller internally strips `.py` files from data collection even with explicit `includes` (they are treated as module source files, not data). Direct glob bypasses both PyInstaller's C-ext analysis failure AND its data-file `.py` filter. At runtime, `torch._C.pyd` IS present in the bundle, so `torch.testing.__init__` executes correctly when Python loads the physical `.py` file.
- **Files Modified**: `pyinstaller_hooks/hook-torch.py`, `build_smart_sentry_v2_3_2_portable.ps1`
- **Additional root cause discovered**: `torch.testing` and `torch.testing._internal` were also listed in `$torchRuntimeExcludes` in the build script, which generated `--exclude-module torch.testing` PyInstaller flags. This would have overridden the datas-based inclusion even if the .py files were physically copied. Both entries removed from `$torchRuntimeExcludes`. The `--collect-submodules torch.testing` flag also removed (redundant; those hiddenimports all fail, datas handles it now).
- **Notes**: For any torch subpackage whose `__init__` imports a C extension, the correct bundling workaround is: (1) direct `glob.glob` scan of `torch/<subpkg>/**/*.py` → build `datas` tuples as `(src_path, dest_dir)` in hook-torch.py, AND (2) ensure the module is NOT in `$torchRuntimeExcludes` in the build script. Related: ISS-081 (hiddenimports — ineffective), ISS-082 v1 (collect_data_files — returned empty).

---

### ISS-081 | 2026-04-21 | v3.0.0 | Build | Failed (see ISS-082)
**Frozen Exe YOLO Prepare Fails — `ModuleNotFoundError: No module named 'torch.testing'` (recurrence after ISS-080 incomplete fix)**

- **Symptoms**: Build 5 EXE (after ISS-080) launched with `MainWindowTitle = "Unhandled exception in script"` — `Failed to execute script 'run' due to unhandled exception: No module named 'torch.testing'`. The `logs/yolo_runtime_diag.log` was never created because the crash happened before UI reached YOLO init. Confirmed: `torch.testing` absent from PYZ (not found in EXE binary string scan) and `torch/testing/` folder not present in `SMART_SENTRY_V3_0_0_FILES/`.
- **Root Cause**: ISS-080 fix removed `"torch.testing"` from `EXCLUDED_TORCH_PREFIXES` in `hook-torch.py`, but this was insufficient. `torch.testing.__init__` imports `from torch._C import FileCheck` — a C extension. During PyInstaller's static module graph analysis, importing `torch._C` fails (it's a `.pyd`), so the entire `torch.testing` package is silently dropped by `collect_submodules("torch", on_error="ignore")`. The package never appears in the build log at all, which confirms it was excluded by the `on_error="ignore"` path, not by the prefix filter. The physical `.py` file `torch/autograd/gradcheck.py` is collected to disk and imports `torch.testing` at runtime, but `torch.testing` itself was never bundled.
- **Fix/Solution**: Added an explicit separate `collect_submodules("torch.testing", on_error="ignore")` call in `hook-torch.py` after the main torch collect, with a hard-coded fallback list if that also fails. Added `--collect-submodules torch.testing` to `build_smart_sentry_v2_3_2_portable.ps1`. The `import torch.testing` pre-import in `run.py` was already in place from ISS-080.
- **Files Modified**: `pyinstaller_hooks/hook-torch.py`, `build_smart_sentry_v2_3_2_portable.ps1`
- **Notes**: When `collect_submodules("pkg")` runs with `on_error="ignore"` and the package's `__init__` imports a C extension that fails analysis, the entire package is silently dropped — even if the package itself is not in any exclusion list. The workaround is always to add an explicit separate `collect_submodules("pkg.subpackage")` call for known-problematic subpackages. Related: ISS-080.

---

### ISS-080 | 2026-04-21 | v3.0.0 | Build | Partial (see ISS-081)
**Frozen Exe YOLO Prepare Fails — `ModuleNotFoundError: No module named 'torch.testing'`**

- **Symptoms**: After ISS-079 fix (torchgen), YOLO still failed. `yolo_runtime_diag.log` showed `prepare-failed` with `ModuleNotFoundError: No module named 'torch.testing'`. Import chain: `import torch` → `torch.functional` → `torch.nn` → `torch.nn.modules` → `torch.nn.modules.batchnorm` → `torch.nn.modules._functions` → `torch.autograd` → `torch.autograd.gradcheck` → `import torch.testing` → failure.
- **Root Cause**: `torch.testing` was explicitly listed in `EXCLUDED_TORCH_PREFIXES` in `pyinstaller_hooks/hook-torch.py` as a size-optimization exclusion. However, `torch/autograd/gradcheck.py` imports `torch.testing` at module level. Because `torch` files are collected to disk as physical `.py` files in the one-dir build, PyInstaller does not trace imports within those files. `torch.testing` was therefore absent from the support folder. Unlike ISS-077/ISS-078, this is a true missing-package gap, not a timing issue — the package is simply not collected.
- **Fix/Solution**: Removed `"torch.testing"` from `EXCLUDED_TORCH_PREFIXES` in `pyinstaller_hooks/hook-torch.py` so the hook includes `torch.testing` in its `collect_submodules` pass. Added `import torch.testing` to `run.py` as a pre-import to document the dependency and ensure PyInstaller's static analysis traces it from the entry point.
- **Files Modified**: `pyinstaller_hooks/hook-torch.py`, `run.py`
- **Notes**: Recurrence risk: any `torch.*` package excluded from the hook that is imported at module level by another physical `.py` torch file will produce the same error. Review `EXCLUDED_TORCH_PREFIXES` if new `ModuleNotFoundError: No module named 'torch.*'` errors appear. Related: ISS-079 (torchgen), ISS-077/ISS-078 (timing).

---

### ISS-079 | 2026-04-20 | v3.0.0 | Build | Worked
**Title**: Frozen exe YOLO prepare fails � ModuleNotFoundError: No module named 'torchgen.model'
**Context**: Third PyInstaller build (exit 0) still fails YOLO prepare with 	orchgen.model not found.
**Root Cause**: 	orch/utils/_python_dispatch.py line 13-14 does import torchgen; import torchgen.model at module level. In the one-dir build, all torch .py files are collected to disk as physical files. PyInstaller's dependency analysis does not trace imports inside collected-to-disk files, so 	orchgen (a separate top-level package) is never discovered and not bundled into the support folder. Error is not a timing issue � the package is simply absent from the output directory.
**Fix**: Added --collect-submodules torchgen to uild_smart_sentry_v2_3_2_portable.ps1 (line 459). Added import torchgen; import torchgen.model to 
un.py as pre-import documentation and to ensure PyInstaller's static analysis sees the dependency from the entry point.
**Files Changed**: 
un.py, SMART SENTRY/build_smart_sentry_v2_3_2_portable.ps1
### ISS-078 | 2026-04-20 | v3.0.0 | Build | Worked
**Frozen Exe YOLO Prepare Failed With `ModuleNotFoundError: No module named 'unittest.result'`**

- **Symptoms**: After ISS-077 was fixed (asyncio preload), YOLO still failed to load. `yolo_runtime_diag.log` showed `prepare-failed` with `ModuleNotFoundError: No module named 'unittest.result'`. Import chain: `import torch` → `torch.utils._config_module` → `import unittest` → `unittest/__init__.py:60` → `from .result import *` → failure.
- **Root Cause**: Same initialization timing problem as ISS-077. `torch.utils._config_module` triggers `import unittest` for the first time **while torch is still mid-`exec_module`**. When `unittest/__init__.py` line 60 runs `from .result import *`, `unittest.__path__` is not yet established in the frozen importer context, so `unittest.result` cannot be resolved even though the module is present in the PYZ. `--collect-submodules unittest` was added to the build script but only collected `unittest.test.*` subpackages — `unittest.result`, `unittest.case` etc. are stdlib top-level modules within unittest and are already present in PYZ but cannot be loaded during mid-exec_module initialization.
- **Fix/Solution**: Added `import unittest` to `run.py` immediately after `import asyncio`, before `from app.main import main`. This pre-initializes unittest (and all its submodules including `unittest.result`) into `sys.modules` before any torch import occurs. The `--collect-submodules unittest` build flag was retained.
- **Files Modified**: `run.py`
- **Notes**: Third stdlib package initialization timing issue in v3.0.0 frozen bundle (asyncio → ISS-077, unittest → ISS-078). All follow the same pattern: torch's import chain triggers a stdlib `__init__.py` mid-exec_module, before `__path__` is established in the frozen importer. The consistent fix is to pre-import the affected stdlib package in `run.py`.

---

### ISS-077 | 2026-04-20 | v3.0.0 | Build | Worked
**Frozen Exe YOLO Prepare Failed With `ModuleNotFoundError: No module named 'asyncio.base_events'`**

- **Symptoms**: The packaged `SMART_SENTRY_V3.0.0.exe` launched and the UI appeared, but YOLO failed to load in every attempt. Checking `SMART_SENTRY_V3_0_0_FILES\logs\yolo_runtime_diag.log` showed multiple `prepare-failed` entries, all with the error `ModuleNotFoundError: No module named 'asyncio.base_events'`. The app was otherwise functional; only AI/YOLO detection was unavailable.
- **Root Cause**: Package initialization timing issue in the frozen bundle. `_prepare_yolo_runtime()` calls `import torch`. `torch/__init__.py:1756` applies a `@_deprecated` decorator from `typing_extensions`, which triggers execution of `asyncio/__init__.py` for the first time — **while `torch/__init__.py` is still mid-`exec_module`**. When `asyncio/__init__.py` line 8 runs `from .base_events import *`, it re-enters Python's import machinery from within an already-executing `exec_module`. At this point `asyncio.__path__` is not yet fully established in the frozen importer context (the package is still initializing), so PyInstaller's `pyimod02_importers.py` cannot resolve `asyncio.base_events` even though the module IS present in the PYZ archive. All asyncio submodules were confirmed present in the PYZ via `CArchiveReader`; the failure is purely an initialization ordering problem, not a missing-file problem. Traceback chain: `_prepare_yolo_runtime()` → `import torch` → `torch/__init__.py:1756` `@_deprecated` → `typing_extensions.py:2997` `__call__` → `asyncio/__init__.py:8` → `ModuleNotFoundError: No module named 'asyncio.base_events'`.
- **Fix/Solution**: Added `import asyncio` to `run.py` immediately after the environment variable setup block and before `from app.main import main`. This pre-initializes asyncio (and all its submodules) into `sys.modules` before any torch import can occur. When torch later triggers `asyncio/__init__.py`, Python finds asyncio already in `sys.modules` and skips re-execution, so `asyncio/__init__.py` line 8 is never reached again. The `--collect-submodules asyncio` build flag (added as part of earlier investigation) was retained as belt-and-suspenders since it has no negative effects.
- **Files Modified**: `run.py`
- **Notes**: Diagnosed by inspecting the EXE's embedded PYZ archive with `PyInstaller.archive.readers.CArchiveReader` — all 32 asyncio submodules were confirmed present. The error therefore cannot be a collection gap. This is a Python 3.11 + PyInstaller frozen import ordering issue specific to the `torch` → `typing_extensions` → `asyncio` import chain. The fix must remain in `run.py` for all future builds. Commit `c90ce74`. Related to ISS-076 (different mechanism — ISS-076 was a true missing-module gap, ISS-077 is an initialization ordering problem).

---

### ISS-076 | 2026-04-20 | v3.0.0 | Build | Worked
**Frozen Exe Crashed With `ModuleNotFoundError: No module named 'numpy._core._exceptions'`**

- **Symptoms**: `SMART_SENTRY_V3.0.0.exe` launched and immediately crashed with a full traceback ending in `ModuleNotFoundError: No module named 'numpy._core._exceptions'`. The crash happened before the app window appeared. Error surfaced through `cv2 → numpy → numpy._core → numpy._core._exceptions` import chain at startup.
- **Root Cause**: NumPy 2.x restructured its C extensions so that `numpy._core._exceptions` and other `numpy._core.*` submodules exist as separate importable modules. PyInstaller's standard `hook-numpy.py` (shipped with the installed `numpy._pyinstaller` package) does not enumerate all of these submodules, so they were silently absent from the frozen bundle even though the numpy package itself was included.
- **Fix/Solution**: Added `'--collect-submodules', 'numpy'` to the `$pyInstallerArgs` array in `build_smart_sentry_v2_3_2_portable.ps1`, placed immediately after the torchvision/sentry_v2_tab hidden-imports. This forces PyInstaller to walk and bundle every numpy submodule (including the `numpy._core.*` family). The `numpy.f2py.tests` collection emits a harmless `pytest` not-found warning at build time; this is expected and does not affect the runtime.
- **Files Modified**: `build_smart_sentry_v2_3_2_portable.ps1`
- **Notes**: This failure is specific to NumPy 2.x. NumPy 1.x packaged without this flag because the old `numpy.core` layout was picked up by the hook. Any upgrade to NumPy 2.x in the build venv requires this flag to remain. Related to ISS-075 (torch double-import in same session).

---

### ISS-075 | 2026-04-20 | v3.0.0 | Build | Worked
**Frozen Exe Crashed With `cannot load module more than once per process` on numpy**

- **Symptoms**: `SMART_SENTRY_V3.0.0.exe` crashed at startup with PyInstaller's internal error `cannot load module more than once per process`. Traceback showed `run.py → app/main.py → sentry_v2/__init__.py → sentry_v2_detector.py → cv2/__init__.py → import numpy` as the failing chain. The error was `numpy._core.__init__` failing the module-uniqueness guard inside PyInstaller's `pyimod02_importers.py`.
- **Root Cause**: `app/main.py` had two module-level calls — `_configure_ml_runtime_env()` and `_preload_torch_runtime()` — executed at import time (not inside `if __name__ == "__main__"`). `_preload_torch_runtime()` imported `torch`, which in turn imported `numpy`. Then `run.py`'s `from app.main import main` triggered that torch+numpy load. Immediately after, the frozen importer tried to load `sentry_v2_detector.py` which imports `cv2`, which imports `numpy` again. PyInstaller's frozen importer tracks module identity and raises `cannot load module more than once per process` on the second attempt to exec `numpy._core.__init__`.
- **Fix/Solution**: Removed the two bare module-level calls `_configure_ml_runtime_env()` and `_preload_torch_runtime()` from `app/main.py`. The function definitions were left in place but are no longer invoked at module scope. The environment variables they set (e.g. `KMP_DUPLICATE_LIB_OK`, `OMP_NUM_THREADS`) are already set unconditionally in `run.py` before any import, so they remain effective in both source-run and frozen modes without needing a preload call.
- **Files Modified**: `app/main.py`
- **Notes**: In a frozen PyInstaller exe, any import that happens at the top level of `app/main.py` executes the moment `run.py` does `from app.main import main`. Torch and numpy must not be imported before the frozen importer has finished resolving the sentry_v2 package tree. This is specific to the one-file-per-module frozen import model — source-run is unaffected. Commit `0de3912`.

---

### ISS-074 | 2026-04-16 | v3.0.0 | Config/UI | Worked
**Auto-Trigger Toggle Left Stale Fire-Gate Values Active**

- **Symptoms**: Operator enables auto-trigger and tracking looks active, but auto-fire still never happens even though the corrected fire-gate values exist on disk. Behavior still matches the old impossible sub-degree gate profile until the values are manually edited or reloaded.
- **Root Cause**: The auto-trigger checkbox only flipped `auto_trigger_enabled`; it did not normalize stale in-memory engagement settings already loaded from older configs or presets. Legacy sub-degree fire and aim-lock tolerances could therefore stay active in the engine even after the newer fix existed in the settings files.
- **Fix/Solution**: Added `normalize_auto_trigger_engagement()` in `app/sentry_v2/sentry_v2_config.py`, invoked it from `EngagementConfig.__post_init__`, from `_on_engagement_changed()`, and immediately when `_on_auto_trigger_toggled()` turns auto-trigger on. Also synced the active `smart_sentry_v3_0_0_settings.json` and legacy `smart_sentry_v2_3_2_settings.json` profiles to the fireable aim-lock / fire-gate values and added regression coverage in `tests/test_sentry_v2_engagement_config.py`.
- **Files Modified**: `app/sentry_v2/sentry_v2_config.py`, `app/sentry_v2/sentry_v2_tab.py`, `app/config/smart_sentry_v3_0_0_settings.json`, `app/config/smart_sentry_v2_3_2_settings.json`, `tests/test_sentry_v2_engagement_config.py`
- **Notes**: Related to ISS-071. This closes the stale-profile path where the UI could show auto-trigger ON while the engine still ran the old impossible gate values.

---

### ISS-073 | 2026-04-15 | v3.0.0 | Detection | Worked
**Loss Recovery Never Re-Detects Target During Search — ByteTrack ID Resets on Every Pan**

- **Symptoms**: After target loss, turret moves through its full search pattern but never re-detects the person even when they are standing directly in front of the turret. Engine completes the search window and returns to guard. Runtime snapshot shows `Visible targets: 0`, `Qualified: 0` at end of search.
- **Root Cause**: `semantic_min_confirm_frames: 2` required the same ByteTrack `track_id` to appear in at least 2 successive frames before a detection entered `last_targets`. After each pan step in the search pattern, ByteTrack assigns a new `track_id` to the person that reappears in the new frame (old track state ages out after ~1 second / ~30 frames). Every new search position resets semantic-confirm hits to 0, so a person detected in frame N gets `hits=1` (pending) → turret pans → fresh `track_id` → `hits=1` again. The 2-frame threshold is never reached, the detection never enters `last_targets`, and `_find_active_target()` (which reads from `last_targets`) always returns `None` throughout the entire search.
- **Fix/Solution**: Set `semantic_min_confirm_frames: 2 → 1` in `app/config/smart_sentry_v3_0_0_settings.json` so a single YOLO detection frame passes the semantic filter regardless of `track_id` continuity. Also expanded search coverage (`loss_local_search_pan_deg: 10 → 20°`, `loss_local_search_tilt_deg: 8 → 12°`), increased dwell time at each position (`loss_search_step_interval_s: 0.28 → 0.40s`) so the camera fully settles before YOLO evaluates, and raised the overall search window (`target_loss_timeout: 2.5 → 5.0s`).
- **Files Modified**: `app/config/smart_sentry_v3_0_0_settings.json`, `validate_settings.py`
- **Notes**: `semantic_min_confirm_frames ≥ 2` causes re-detection failure in any scenario that resets `track_id` (camera pan/tilt motion, ByteTrack age-out after ~1 s, brief occlusion). Setting it to 1 effectively turns off confirmation gating and lets a single high-confidence YOLO frame re-engage. If false-positive engagements increase after this change, raise `yolo_confidence` threshold or tighten `min_size_ratio` instead of reverting `semantic_min_confirm_frames`.

---

### ISS-072 | 2026-04-15 | v3.0.0 | Engine | Worked
**Target Loss Recovery Does Not Reacquire and Search Movement Feels Robotic**

- **Symptoms**: After target loss, turret moves past the lost position without reacquiring, then returns to guard. Search movement is not smooth, feels mechanical, and does not effectively hunt for the target.
- **Root Cause**: Default after-loss search spans were far too large, so the engine jumped through wide scan points instead of hunting locally. Search cadence was also too tight, which made movement feel robotic.
- **Fix/Solution**: Reduced default local search spans from 45° to 6° pan / 4° tilt, slowed loss search cadence to 0.25s, and tuned the runtime settings file to the same safer values. This preserves the adaptive quick-reacquire path while keeping search movement bounded and deliberate.
- **Files Modified**: app/sentry_v2/sentry_v2_config.py (loss search defaults), app/config/smart_sentry_v2_3_2_settings.json, app/config/smart_sentry_v3_0_0_settings.json (loss search tuning)
- **Notes**: Related to ISS-046 (target-loss recovery expiration), ISS-069 (PIR search visibility). This fix keeps the existing jitter profile but makes the commanded search points much smaller and more natural.

### ISS-071 | 2026-04-15 | v3.0.0 | Engine | Worked
**Auto Fire Not Triggering Despite `auto_trigger_enabled: true`**

- **Symptoms**: Manual fire works. With `auto_trigger_enabled: true` the turret tracks a person but never auto-fires, even when visually well-centered.
- **Root Cause**: Both the fire-trigger enter tolerances (`fire_trigger_enter_pan_tolerance: 0.08°`, `fire_trigger_enter_tilt_tolerance: 0.06°`) and the aim-lock tolerances (`aim_lock_pan_tolerance: 0.11°`, `aim_lock_tilt_tolerance: 0.10°`, `aim_lock_required_frames: 7`) were set impossibly tight for YOLO-based person tracking. A YOLO bounding-box center cannot reliably stay within 0.08° pan / 0.06° tilt across frames — those values are sub-pixel precision at 1280×720. Aim-lock was also configured to require 7 consecutive in-tolerance frames, which was never achieved before the lock timeout expired.
- **Fix/Solution**: Raised fire-trigger enter tolerances to realistic YOLO-tracking values (`fire_trigger_enter_pan_tolerance: 0.08 → 2.5°`, `fire_trigger_enter_tilt_tolerance: 0.06 → 2.0°`, exit `3.5°`/`3.0°`). Raised aim-lock tolerances to match (`aim_lock_pan_tolerance: 0.11 → 3.0°`, `aim_lock_tilt_tolerance: 0.10 → 2.5°`) and reduced required lock frames (`aim_lock_required_frames: 7 → 2`). Also tuned PID damping (`precision_kd: 0.014 → 0.018`) and settle time (`precision_settle_time: 0.88 → 0.55s`).
- **Files Modified**: `app/config/smart_sentry_v3_0_0_settings.json`, `validate_settings.py`
- **Notes**: The `fire_trigger_enter_pan/tilt_tolerance` values are the hard gate: if they are tighter than YOLO's natural center jitter (≈1–3°), auto-fire will never trigger regardless of aim quality. Related to ISS-070 (YOLO promotion), ISS-010 (aim-lock timeout).

### ISS-070 | 2026-04-15 | v3.0.0 | Engine | Worked
**YOLO Detection Not Promoting to Engagement / Overshooting When Target Moves**

- **Symptoms**: Using YOLO11m for person detection, system shows YOLO bounding box but turret does not move to engage. When engagement does trigger (usually after the target moves), the turret overshoots and oscillates.
- **Root Cause**: `min_threat_score: 0.5` was too high a bar for YOLO person detections — threat scoring for a live person in a typical indoor frame rarely exceeded 0.5, so the engine never entered ENGAGING state. Separately, `precision_kd: 0.014` provided insufficient derivative damping for the closed-loop visual-servo correction, causing overshoot on any non-trivial target motion.
- **Fix/Solution**: Lowered `min_threat_score: 0.5 → 0.25` so standard YOLO person detections reliably promote to engagement. Increased derivative damping `precision_kd: 0.014 → 0.018` and reduced settle time `precision_settle_time: 0.88 → 0.55s` to reduce overshoot and reach stable lock faster.
- **Files Modified**: `app/config/smart_sentry_v3_0_0_settings.json`, `validate_settings.py`
- **Notes**: `min_threat_score` is the primary engagement gate. If tracking regresses to not promoting again, check `threat_score` values in real-time snapshots (field: `threat_score`) and compare against `min_threat_score`. Related to ISS-071 (auto-fire tolerances too tight), ISS-012 (EMA cold-start seeding), ISS-013 (engagement response scale).

### ISS-069 | 2026-04-13 | v3.0.0 | UI | Worked
**PIR Events Looked One-Sided and PIR Search Was Missing From the Log Pane**

- **Symptoms**: Operators could see one PIR zone reacting while adjacent sensors appeared dead, PIR search/hunt movement often was not visible after a cue, and serial-log entries for PIR/search activity were easy to miss or appeared to vanish under the generic log stream.
- **Root Cause**: The live PIR runtime still used an `800 ms` cross-sensor lockout, which was long enough to suppress legitimate follow-on hits from a neighboring sensor. At the same time, PIR cue/search/return state was not surfaced through the UI log filter model, and tab-side auto-move deferral could hide the first visible PIR hunt step while another move was still settling.
- **Fix/Solution**: Reduced the PIR cross-sensor lockout default and live config surfaces to `120 ms`, capped cross-sensor suppression in `SentryV2PIRManager`, surfaced explicit PIR cue/search/confirm/return notes from the engine, added a dedicated `PIR` serial-log filter/category, logged PIR search movement and notes in the tab, and let active PIR hunt moves bypass the normal auto-move defer gate so the first search hop is visible.
- **Files Modified**: `app/sentry_v2/sentry_v2_config.py`, `app/sentry_v2/sentry_v2_pir_manager.py`, `app/sentry_v2/sentry_v2_engine.py`, `app/sentry_v2/sentry_v2_tab.py`, `app/config/smart_sentry_v2_3_2_settings.json`, `app/config/smart_sentry_v3_0_0_settings.json`, `test_pir_ui_config.py`
- **Notes**: If PIR coverage seems biased again, inspect the live `cross_sensor_lockout_ms` first and confirm the serial log is on `All` or `PIR` rather than `System`.

### ISS-068 | 2026-04-11 | v3.0.0 | Build | Worked
**Packaged OpenCV Face Cascade Data Was Missing From the Release**

- **Symptoms**: The packaged app launched with repeated OpenCV startup errors like `Can't open file ... cv2\\data\\haarcascade_frontalface_default.xml in read mode`, even before the operator touched face-recognition features.
- **Root Cause**: The portable build shipped `cv2\\data` as an almost-empty directory, so the packaged runtime resolved `cv2.data.haarcascades` into the release tree but did not actually have the cascade XML assets that `FaceIdentityRuntime` expected.
- **Fix/Solution**: Updated `app/sentry_v2/face_identity.py` so the face runtime resolves the cascade path from multiple valid locations and falls back to an empty classifier when the asset is absent instead of asking OpenCV to open a missing file path. Updated `SmartSentryV2.spec` and `build_smart_sentry_v2_3_2_portable.ps1` so `cv2\\data` is explicitly bundled into the packaged release. Also copied the missing cascade files into the current promoted `F:\SMART SENTRY V3.0.0` release so the operator-facing build stopped emitting the startup errors immediately.
- **Files Modified**: `app/sentry_v2/face_identity.py`, `SmartSentryV2.spec`, `build_smart_sentry_v2_3_2_portable.ps1`
- **Notes**: This cascade-data defect is separate from the YOLO runtime-prep recursion issue. If the same OpenCV startup error reappears, inspect `SMART_SENTRY_V3_0_0_FILES\\cv2\\data` first.

---

### ISS-067 | 2026-04-11 | v3.0.0 | Build | Worked
**Packaged YOLO Runtime Prep Recursed Before Torch Could Import**

- **Symptoms**: The packaged app repeatedly logged `YOLO runtime prepare failed: maximum recursion depth exceeded`, kept warning that YOLO detection was active with no model loaded, and never reached the actual model import/load phase even though the packaged weights and support files were present.
- **Root Cause**: The frozen-runtime DLL-path preparation path in `app/sentry_v2/sentry_v2_tab.py` used extra path resolution work while preparing the packaged support directories, which could recurse in the packaged environment before `torch` and `ultralytics` were imported. The helper also dropped `os.add_dll_directory()` handles immediately, which is not a stable way to hold those DLL search paths alive for the lifetime of the process.
- **Fix/Solution**: Simplified `_prepare_frozen_runtime_library_paths()` to use direct directory checks and absolute normalized paths instead of additional `resolve()` calls in the frozen path-prep flow, preserved `os.add_dll_directory()` handles on the tab instance, and upgraded `_prepare_yolo_runtime()` error reporting to include the exception type so future packaged import failures are diagnosable from the runtime log. A dedicated frozen-runtime reproduction script confirmed the helper now completes cleanly and `torch` / `ultralytics` import successfully under the simulated packaged path.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`, `tools/repro_yolo_prepare.py`
- **Notes**: If packaged YOLO fails again, run `tools/repro_yolo_prepare.py` first before rebuilding so the failure can be separated into path-prep vs actual torch/ultralytics import problems.

---

### ISS-065 | 2026-04-11 | v3.0.0 | Build | Worked
**Packaged YOLO Model Path Drifted to the Wrong Runtime Surface**

- **Symptoms**: `SMART_SENTRY_V3.0.0.exe` launched, but YOLO would not load from the packaged release and the packaged settings could still point at a source-tree or staging-model path instead of the final release-root `YOLO_MODELS` folder.
- **Root Cause**: The live runtime path selection in `app/sentry_v2/sentry_v2_tab.py` was still anchored to hard-coded `smart_sentry_v2_3_2_*` settings, prompted-target, preset, and face-library paths. That let the packaged v3.0.0 app boot against the wrong settings surface and carry stale `yolo_model_dir` values.
- **Fix/Solution**: Made the Smart Sentry runtime path layer version-aware so v3.0.0 now resolves its active canonical settings, presets, prompted-target, and face-library paths from the active release version while still falling back to older aliases for migration. Added release-protocol checks that require the packaged active settings file to point `detection_mode.yolo_model_dir` at the final release-root `YOLO_MODELS` folder and explicitly reject source-tree or `.pyinstaller-temp` paths.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`, `SMART_SENTRY_V3_0_0_COMPILATION_PROTOCOL.md`
- **Notes**: This regression can reappear whenever packaging works but the runtime still loads a stale compatibility settings file. Always inspect the packaged active settings file under `SMART_SENTRY_V3_0_0_FILES\app\config` before sign-off.

---

### ISS-066 | 2026-04-11 | v3.0.0 | Build | Worked
**Packaged App Loaded the Wrong Settings Surface and Silenced the Live Buzzer Path**

- **Symptoms**: The packaged app connected, but the ESP32 buzzer produced no audible cue and the live WiFi runtime behavior did not match the intended v3.0.0 operator settings.
- **Root Cause**: The packaged app was still capable of loading the stale `2.3.2` settings surface instead of the active v3.0.0 settings file, so sound and connection values could drift away from the live WiFi firmware contract even though the package itself launched.
- **Fix/Solution**: Redirected the live load/save path to the active release-version settings surface in `app/sentry_v2/sentry_v2_tab.py` instead of the hard-coded `2.3.2` file, kept compatibility fallbacks only for migration, and updated the v3.0.0 compilation protocol so release sign-off now requires a packaged buzzer validation on the live WiFi link plus inspection of the packaged active settings file for the intended sound and UDP values.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`, `SMART_SENTRY_V3_0_0_COMPILATION_PROTOCOL.md`
- **Notes**: This failure mode is easy to miss because the packaged app can look healthy while still using the wrong saved config. Treat buzzer silence in the packaged app as a config-surface bug first, not just a transport bug.

---

### ISS-001 | 2026-04-10 | v3.0.0 | Camera | Worked
**Partial-Frame Recovery Counter Could Loop Forever**

- **Symptoms**: Camera could appear to reopen forever after a partial-frame condition because recovery attempts never advanced past `0/3`, especially while testing 1280×720 on Windows.
- **Root Cause**: `_finish_camera_open()` reset `_camera_recovery_attempts = 0` on every reopen, including reopens triggered by `_attempt_camera_recovery()`. That made partial-frame recovery diagnostics misleading and could hide the true backend failure by restarting from attempt 1 on every cycle.
- **Fix/Solution**: Kept `_camera_recovery_attempts` intact while `_camera_recovery_in_progress` is true, so recovery escalates correctly across reopen attempts and only resets after a non-recovery open succeeds.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`
- **Notes**: This fix was necessary for correct recovery behavior, but it was not the full 1280×720 solution by itself. The final stable result came after the backend-order change in [ISS-005](#iss-005), which stopped Windows from selecting the degraded DSHOW path on this machine.

---

### ISS-002 | 2026-04-10 | v3.0.0 | Camera | Did Not Work
**Crop-And-Resize Partial-Frame Workaround Softened the Feed**

- **Symptoms**: Video could be kept visually alive by masking partial frames, but the resulting 1280×720 preview looked soft because only the upper-left content region was real image data.
- **Root Cause**: The temporary workaround path cropped partial frames to visible content and then resized them back to the requested camera dimensions. That hid the black area, but it did not fix the underlying camera path and made the image look worse.
- **Fix/Solution**: Removed the partial-frame acceptance and crop-and-resize masking path during the camera rollback, so persistent partial frames are no longer treated as a valid stable camera state. The real fix was to keep partial-frame detection as a health guard and then choose the correct backend as documented in [ISS-005](#iss-005).
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`
- **Notes**: If this workaround ever reappears, remove it again. It is useful only as a diagnostic experiment; it is not an acceptable release path for Smart Sentry camera quality.

---

### ISS-003 | 2026-04-10 | v3.0.0 | UI | Worked
**Scope View Corner Arc Artifact**

- **Symptoms**: Rounded arcs visible at corners of the video panel, especially noticeable in scope view mode with dark overlay.
- **Root Cause**: `QLabel#sentryV2Video` had `border-radius: 16px` in the static theme and `border-radius: {radius_large}px` in the dynamic theme block. Qt clips the QLabel pixmap at rounded corners, creating visible arc cutouts.
- **Fix/Solution**: Set `border-radius: 0px` in both the static stylesheet block (~line 2577) and the dynamic theme block (~line 4357) for `QLabel#sentryV2Video`.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`
- **Notes**: Any future theme change that adds `border-radius` to the video label will re-introduce this artifact. Video labels should always use `border-radius: 0px`.

---

### ISS-004 | 2026-04-10 | v3.0.0 | Config | Worked
**Camera Default Resolution Too High (1920×1080)**

- **Symptoms**: Camera opens at 1920×1080 causing driver instability, black frames, or partial frames on many USB webcams.
- **Root Cause**: Default `camera_width`/`camera_height` in all 3 config files was 1920×1080. Many USB webcams handle this poorly under Windows DSHOW/MSMF backends.
- **Fix/Solution**: Changed defaults to `camera_width: 1280`, `camera_height: 720` in all 3 settings files.
- **Files Modified**: `app/config/smart_sentry_v3_settings.json`, `app/config/sentry_v2_settings.json`, `app/config/smart_sentry_v2_3_2_settings.json`
- **Notes**: 1280×720 is the baseline resolution for Smart Sentry FOV calculations. Higher resolutions require better USB bandwidth and may cause driver-level issues.

---

### ISS-005 | 2026-04-10 | v3.0.0 | Camera | Worked
**Windows Backend Selection Was Choosing a Degraded 1280×720 Path**

- **Symptoms**: The app could request 1280×720 successfully, but the live source still auto-closed after repeated partial-frame recovery because Windows kept reopening the camera with DSHOW. In-app diagnostics showed `Camera opened: 0 (1280x720)` followed by repeated partial-frame detection and recovery.
- **Root Cause**: On this machine, DSHOW is the broken backend for camera `0` at 1280×720: it opens and reports the requested resolution, but the feed is mostly partial frames. Direct probing showed MSMF and DEFAULT hold stable full frames while DSHOW does not. The old Windows probe order preferred DSHOW first, so the runtime kept selecting the degraded path.
- **Fix/Solution**: Added `_is_usable_camera_probe_frame()` so the probe rejects startup frames that are black or partial, then changed the Windows backend probe order in `_open_bg()` to `MSMF -> DEFAULT -> DSHOW`. Kept the warm-up discard, health grace window, and delayed recovery reopen so the selected backend has time to settle before health checks start. Validated the fix with `tools/camera_backend_probe.py` and `tools/camera_open_smoke_test.py`, which confirmed a stable in-app open at 1280×720 with `recovery_attempts: 0`.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`, `tools/camera_backend_probe.py`, `tools/camera_open_smoke_test.py`
- **Notes**: This is the actual release-path fix for the 1280×720 camera issue on this Windows system. If the symptom returns, run the backend probe first and confirm the app still prefers MSMF before DSHOW.

---

### ISS-006 | 2026-04-10 | v3.0.0 | Camera | Worked
**Camera Recovery Loop After Successful Open (Startup Noise)**

- **Symptoms**: Camera appears to open successfully then immediately closes and reopens in a loop. Most noticeable on webcams that deliver unstable startup frames (first 1-2 seconds).
- **Root Cause**: Health checks started as soon as the grab timer began. Transient startup artifacts (black or partial frames in the first 1-2 seconds) tripped recovery almost immediately. Overlapping integer-camera open requests could also stack while no live `_cap` existed.
- **Fix/Solution**: Added `_CAMERA_HEALTH_GRACE_AFTER_OPEN_S = 2.0` — health checks ignore blackout and partial-frame triggers for 2 seconds after camera open. Added `_camera_open_in_progress` guard to prevent duplicate open requests.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`
- **Notes**: Grace window is separate from recovery counter ([ISS-001](#iss-001)). Both work together: grace window handles startup noise, recovery counter handles persistent failures.

---

### ISS-007 | 2026-04-10 | v3.0.0 | Firmware | Worked
**PWM Servo Motion Too Abrupt and Unsynchronized**

- **Symptoms**: Turret pan/tilt movements are jerky, snappy. Small target changes cause visible jitter. Pan and tilt settle at different times.
- **Root Cause**: ESP32 WiFi + Debug Board USB sketch wrote each new target angle directly to servos with only coarse 4-bucket timing estimates. No motion smoothing or axis synchronization.
- **Fix/Solution**: Added internal synchronized motion plan, fixed update interval, and settle deadband to ESP32 firmware. PWM outputs now ramp toward targets instead of snapping. Both axes use one synchronized plan time.
- **Files Modified**: `arduino/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR.ino`
- **Notes**: No changes to the desktop app UDP protocol. Firmware-only change.

---

### ISS-008 | 2026-04-10 | v3.0.0 | Camera | Worked
**Partial-Frame Driver Degradation**

- **Symptoms**: Video squished into upper-left corner with rest of frame black. Crosshair and HUD centered on full (mostly black) frame. Camera doesn't trigger blackout recovery because frame isn't entirely black.
- **Root Cause**: After prolonged runtime, USB webcam (MSMF/DSHOW) enters degraded state where driver fills buffer with video only in upper-left sub-rectangle; remainder is zero-filled black. Existing blackout detector missed this because `tl_mean` was above threshold.
- **Fix/Solution**: Added `_is_probable_partial_frame()` sampling top-left vs bottom-right quadrants (thresholds: `tl_mean > 8.0` AND `br_max <= 6` AND `br_mean <= 1.5`). Extended `_handle_camera_frame_health()` to count consecutive partial frames and trigger recovery after `_MAX_CAMERA_PARTIAL_FRAMES = 6`. The same partial-frame detector is now also used during backend probing so degraded startup frames are rejected before a backend is chosen.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`
- **Notes**: Persistent partial frames are now treated as a backend-selection or recovery failure, not as something the app should mask for the operator. See [ISS-001](#iss-001) for the recovery-counter guard and [ISS-005](#iss-005) for the final Windows backend-order fix.

---

### ISS-009 | 2026-04-10 | v3.0.0 | Engine | Worked
**Stale Loss-Recovery Anchor After Target Switch**

- **Symptoms**: After losing a target and switching to next in engagement queue, loss recovery searches near wrong location (previous target's position).
- **Root Cause**: `_start_order_engagement()` did not initialize `_active_target_last_aim_pan/tilt` to the new order's position. Values remained from previous target.
- **Fix/Solution**: Seeded `_active_target_last_aim_pan/tilt` to `_clamp_pan/tilt(order.pan/tilt)` in `_start_order_engagement()` after `_remember_active_target()`.
- **Files Modified**: `app/sentry_v2/sentry_v2_engine.py`

---

### ISS-010 | 2026-04-10 | v3.0.0 | Engine | Worked
**Refractory Bypass on Aim-Lock Timeout Fire Path**

- **Symptoms**: Rapid re-firing loops when `aim_lock_timeout` is low and `single_target_only=True`. Turret fires more frequently than refractory period should allow.
- **Root Cause**: The aim_lock_timeout fallback fire trigger did not check `_trigger_refractory_until`, bypassing the cooldown gate.
- **Fix/Solution**: Added `now >= self._trigger_refractory_until` guard to the aim_lock_timeout fire condition.
- **Files Modified**: `app/sentry_v2/sentry_v2_engine.py`

---

### ISS-011 | 2026-04-10 | v3.0.0 | Engine | Worked
**Hardcoded Aim Settle Time**

- **Symptoms**: Fast presets (speed 90–100) feel sluggish entering precision phase. Settle time doesn't scale with engagement speed.
- **Root Cause**: Aim settle time was fixed at 0.35 s regardless of `engagement_speed`.
- **Fix/Solution**: Scaled settle time inversely with `engagement_speed`: speed=100 → ~0.14 s, speed=50 → 0.35 s.
- **Files Modified**: `app/sentry_v2/sentry_v2_engine.py`

---

### ISS-012 | 2026-04-10 | v3.0.0 | Engine | Worked
**EMA Cold-Start Bias**

- **Symptoms**: Initial tracking corrections are softer than expected (~50% reduced authority). Takes several frames for the turret to correct at full authority.
- **Root Cause**: `_smoothed_err_pan/tilt` initialized at `0.0` instead of first real error value. EMA filter had to "catch up" from zero.
- **Fix/Solution**: Seeded smoothed error with first real measurement in `_compute_visual_servo_correction()` when stored value is `0.0` and new measurement is nonzero.
- **Files Modified**: `app/sentry_v2/sentry_v2_engine.py`

---

### ISS-013 | 2026-04-10 | v3.0.0 | Engine | Worked
**Narrow Engagement Response Scale**

- **Symptoms**: Speed 90 feels similar to speed 60. Higher speed settings don't feel proportionally faster.
- **Root Cause**: speed → authority mapping range (0.72–1.40) compressed fast presets into a narrow band.
- **Fix/Solution**: Widened scale to 0.65–1.50 and raised fire-phase ceiling to 1.15× in `_engagement_response_scale()`.
- **Files Modified**: `app/sentry_v2/sentry_v2_engine.py`

---

### ISS-014 | 2026-04-10 | v3.0.0 | Engine | Worked
**Guard Return Stranded for Non-Static Modes**

- **Symptoms**: Turret stays parked at last engagement position after target loss in sweep, waypoint, or random patrol modes. Only static guard (mode 0) returns home.
- **Root Cause**: `RETURNING` state only issued move-to-guard for mode 0.
- **Fix/Solution**: Updated `_update_returning()` to command move-to-guard for **all** guard modes.
- **Files Modified**: `app/sentry_v2/sentry_v2_engine.py`

---

### ISS-015 | 2026-04-10 | v3.0.0 | Engine | Worked
**Early Fire Blocked by Settle Timer**

- **Symptoms**: Turret achieves aim lock early but waits for full settle time before firing.
- **Root Cause**: No early-fire path — precision phase transition gated solely on settle time expiration.
- **Fix/Solution**: Added early-fire check: if `aim_lock_required_frames` met before settle time expires, transition to precision immediately.
- **Files Modified**: `app/sentry_v2/sentry_v2_engine.py`

---

### ISS-016 | 2026-04-10 | v3.0.0 | Engine | Worked
**Robotic Hunting Movement**

- **Symptoms**: Loss-recovery search and PIR scan moves look mechanical — exact grid points with no natural variation.
- **Root Cause**: Search targets were exact grid coordinates with no randomization.
- **Fix/Solution**: Added Gaussian micro-jitter (σ=0.35°/0.22° loss recovery, σ=0.40°/0.25° PIR scan) to all hunting movement targets.
- **Files Modified**: `app/sentry_v2/sentry_v2_engine.py`

---

### ISS-017 | 2026-04-10 | v3.0.0 | UI | Worked
**Firing Zone Label Clutter**

- **Symptoms**: "FIRE ZONE" / "LOCK ZONE" text below engagement zone rectangle clutters the crosshair area.
- **Fix/Solution**: Removed the text label render block; preserved the engagement zone rectangle.
- **Files Modified**: `app/sentry_v2/sentry_v2_overlay.py`

---

### ISS-018 | 2026-04-09 | v3.0.0 | Camera | Worked
**Black Screen and RGB Artifacts from Thread-Unsafe Camera Access**

- **Symptoms**: Live preview turns black after recovery, or shows giant RGB block artifacts. Happens intermittently during runtime.
- **Root Cause**: Windows camera path opened and test-read `cv2.VideoCapture` on background thread, then reused same capture on Qt thread. Successful reads handed downstream without detaching from OpenCV's reused frame buffer — corrupted buffers painted as artifacts.
- **Fix/Solution**: Background camera open now probes backend and reopens webcam on Qt thread. All frames detached into contiguous owned buffers before preview or detector handoff.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`
- **Notes**: Cross-thread OpenCV capture sharing is fundamentally unsafe on Windows. **Always** reopen on the consuming thread.

---

### ISS-019 | 2026-04-09 | v3.0.0 | UI | Worked
**No Quick-Access Panel for Runtime Actions**

- **Symptoms**: Operator had to switch to Controls tab for common runtime actions during live monitoring.
- **Fix/Solution**: Added retractable quick-access panel between video feed and serial/status splitter. Panel state (pinned, expanded, height) persisted via config.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`, `app/sentry_v2/sentry_v2_config.py`

---

### ISS-020 | 2026-04-09 | v3.0.0 | Camera/Engine | Worked
**Black Frame Stall and Stale Feedback Overshoot**

- **Symptoms**: Preview goes black or stale during runtime. Target-loss and PIR hunts overshoot because engine advances from commanded pose even when tab defers moves.
- **Root Cause**: Local preview depended too heavily on detector callbacks. Sustained black frames didn't trigger recovery. Engine advanced from commanded position even when moves were deferred by stale feedback.
- **Fix/Solution**: Live-preview fallback active when processed frames lag. Sustained near-black detection with auto-reopen. Resync engine pan/tilt to settled feedback or last confirmed command when moves deferred. Slowed loss-recovery search step cadence.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`, `app/sentry_v2/sentry_v2_engine.py`

---

### ISS-021 | 2026-04-10 | v3.0.0 | Engine | Worked
**Detection Stall After Preset/Mode Change**

- **Symptoms**: After changing master preset or detection method, turret sits idle until operator presses Home or manually moves servo.
- **Root Cause**: `_reset_runtime_state()` did not clear `_last_engage_time`. Stale timestamp kept `cycle_cooldown` blocking new engagements until cooldown expired.
- **Fix/Solution**: Added `self._last_engage_time = 0.0` to `_reset_runtime_state()`.
- **Files Modified**: `app/sentry_v2/sentry_v2_engine.py`

---

### ISS-022 | 2026-04-10 | v3.0.0 | UI | Worked
**Unsafe Default for Manual Keyboard Controls**

- **Symptoms**: WASD + Space keys could accidentally move turret or fire when Smart Sentry window had focus.
- **Root Cause**: No opt-in gate for keyboard manual controls.
- **Fix/Solution**: Added `manual_controls_enabled` (default `False`) in `sentry_v2_config.py`. WASD + Space + Ctrl+Shift+Arrow all gated behind opt-in checkbox. Keys ignored during text/numeric field editing. Keyboard fire auto-releases on focus loss.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`, `app/sentry_v2/sentry_v2_config.py`

---

### ISS-023 | 2026-04-09 | v3.0.0 | Config | Worked
**Firmware Docs Pointed to Wrong Active Sketch**

- **Symptoms**: Editor-facing docs made on-hold Waveshare bridge look like current firmware.
- **Fix/Solution**: Pinned `arduino/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR.ino` as current firmware. Marked Waveshare bridge files as archived/on-hold.
- **Files Modified**: `ESP32_CURRENT_SKETCH.md`, `ESP32_UDP_FLASH.md`, `SMART_SENTRY_MANUAL.md`, `SMART_SENTRY_APP_CHANGE_IMPACT.md`, `SMART_SENTRY_V3_0_0_COMPILATION_PROTOCOL.md`, `PHASE_0_FILES_REQUIRED.md`

---

### ISS-024 | 2026-04-09 | v3.0.0 | Build | Worked
**Release-Hold Tabs Still Visible at Runtime**

- **Symptoms**: Unfinished Facial Recognition and AI Assistant tabs were live runtime surfaces, blocking clean v3.0.0 release prep.
- **Fix/Solution**: Added release-hold convention, filtered held tabs from active tab strip, updated navigation to use visible tab set, added `app/run_smart_sentry_v3_0_0.py` launcher.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`, `run.py`, `app/smart_sentry_meta.py`, `smart_sentry_build_config.py`, `tools/validate_packaging_entrypoints.py`, `build_smart_sentry_v2_3_2_portable.ps1`

---

### ISS-025 | 2026-04-09 | v3.0.0 | Engine | Worked
**PIR No-Target Didn't Return Home**

- **Symptoms**: In static guard setups, turret stays parked at final PIR hunt point after no-target scan completes.
- **Root Cause**: PIR no-target completion cleared cue state without issuing explicit return-home move command.
- **Fix/Solution**: PIR no-target paths now explicitly command configured guard/home position.
- **Files Modified**: `app/sentry_v2/sentry_v2_engine.py`

---

### ISS-026 | 2026-04-09 | v3.0.0 | UI | Worked
**Voice Playback Overlapped ESP32 Buzzer**

- **Symptoms**: Human voice TTS and ESP32 buzzer cues play simultaneously, garbling audio.
- **Fix/Solution**: Added `mute_buzzer_when_human_voice_enabled` guard. Added Voice Diagnostics panel with validation actions.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`, `app/sentry_v2/sentry_v2_config.py`, `app/sentry_v2/sentry_v2_tooltips.py`

---

### ISS-027 | 2026-04-09 | v3.0.0 | Engine | Worked
**PIR Search and Loss Recovery Too Static**

- **Symptoms**: PIR scan sits at cue point doing nothing. Target loss recovery doesn't feel like a local hunt.
- **Fix/Solution**: Added `Hunting` vs `Fast Reacquire` search-style, PIR `Cue Hold` timing, denser directional local hunt for loss recovery, zone-biased local hunt for PIR scans.
- **Files Modified**: `app/sentry_v2/sentry_v2_engine.py`, `app/sentry_v2/sentry_v2_config.py`, `app/sentry_v2/sentry_v2_tab.py`, `app/sentry_v2/sentry_v2_pir_manager.py`

---

### ISS-028 | 2026-04-09 | v3.0.0 | UI | Worked
**AI Assistant Narrow Command Set and Wrong Color Detection Mode**

- **Symptoms**: Assistant couldn't handle home/rest/link/camera commands. Color detection requests activated wrong mode.
- **Fix/Solution**: Expanded assistant command handling, corrected color-detection mode index, added human-voice style presets.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`

---

### ISS-029 | 2026-04-09 | v3.0.0 | UI | Worked
**AI Assistant Had No Spoken Response Mode**

- **Symptoms**: Assistant communicated only through text and buzzer cues, no human-style voice.
- **Fix/Solution**: Added local human speech via PyQt5 `QtTextToSpeech`. Exposed voice selection, rate/pitch/volume controls, `Conversational Voice` mode with auto-speak.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`

---

### ISS-030 | 2026-04-09 | v3.0.0 | UI | Worked
**Placeholder Panels for Face Recognition, Shortcuts, AI Assistant**

- **Symptoms**: Face Recognition, Shortcut Keys, and AI Assistant tabs were non-functional placeholders.
- **Fix/Solution**: Added face-library runtime (`face_identity.py`), face matching with friendly suppression, identity name cues via sound engine, working UI for all three tabs, pinned Quick Keys action, live shortcut bindings.
- **Files Modified**: `app/sentry_v2/face_identity.py`, `app/sentry_v2/sentry_v2_tab.py`, `app/sentry_v2/sound_engine.py`

---

### ISS-031 | 2026-04-09 | v3.0.0 | UI | Worked
**Rigid UI Layout — No Responsive Scaling**

- **Symptoms**: Window shell, tab navigation, manual controls, and list surfaces used hard-coded sizes. Didn't adapt to panel-width changes.
- **Fix/Solution**: Horizontal splitter, responsive panel metrics, scaled icon tab bar, responsive manual controls, preset grids up to 3 columns, vertical flip for narrow panels.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`, `app/run_smart_sentry_v2_3_2.py`

---

### ISS-032 | 2026-04-09 | v3.0.0 | UI | Worked
**Window Size and Splitter Not Persisted**

- **Symptoms**: Window resets to default size on every launch. Settings-panel width and bottom-panel splitter lost.
- **Root Cause**: No geometry persistence. Early startup restore captured zero splitter sizes before widget had real layout.
- **Fix/Solution**: Persisted window and splitter geometry fields. Ignored pre-layout zero-size snapshots. Reapply restore on first show.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`, `app/sentry_v2/sentry_v2_config.py`, `app/run_smart_sentry_v2_3_2.py`

---

### ISS-033 | 2026-04-09 | v3.0.0 | UI | Worked
**AI Default Contract and Fallback Reply Confusion**

- **Symptoms**: Default AI mode didn't match conversational path. Fallback replies looked like normal model output. Spoken replies read full diagnostic blocks.
- **Fix/Solution**: Defaults set to `Conversational Voice` + `llama3.2:latest` with auto-speak. Expanded action parsing. Labeled deterministic fallback. Shortened spoken replies.
- **Files Modified**: `app/sentry_v2/sentry_v2_config.py`, `app/sentry_v2/assistant/service.py`, `app/sentry_v2/sentry_v2_tab.py`

---

### ISS-034 | 2026-04-08 | v3.0.0 | Engine | Worked
**Rest Tilt Clamped Above Guard Minimum**

- **Symptoms**: Rest tilt saved below Guard minimum, but `Go Rest` pulls turret up to guard minimum instead of saved position.
- **Root Cause**: Rest-move execution reused the generic manual clamp path which enforces guard minimum.
- **Fix/Solution**: Rest command now clamps against absolute sentry tilt limits instead of guard/manual minimum.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`

---

### ISS-035 | 2026-04-08 | v3.0.0 | Engine | Worked
**PIR Scan Started with Duplicate Center Point**

- **Symptoms**: PIR no-detect search appears to do nothing initially — turret stays at cue point before moving.
- **Root Cause**: Multi-point scan re-issued already-visited cue center as first scan point.
- **Fix/Solution**: Skip duplicated center; immediately move to first offset point after cue no-detect window.
- **Files Modified**: `app/sentry_v2/sentry_v2_pir_manager.py`

---

### ISS-036 | 2026-04-08 | v3.0.0 | Engine | Worked
**Adaptive Loss Recovery for Dense vs Sparse Scenes**

- **Symptoms**: Loss recovery behaved the same regardless of scene complexity.
- **Fix/Solution**: Added adaptive loss-context capture plus two named recovery protocols. Exposed `After Target Loss` tuning group.
- **Files Modified**: `app/sentry_v2/sentry_v2_engine.py`, `app/sentry_v2/sentry_v2_config.py`, `app/sentry_v2/sentry_v2_tab.py`

---

### ISS-037 | 2026-03-16 | v2.3.x | Engine | Worked
**Burst Fire Blocked UI Thread**

- **Symptoms**: Frame updates freeze during automatic fire sequences. UI becomes unresponsive during bursts.
- **Root Cause**: Burst loop used synchronous blocking sleeps on the UI thread.
- **Fix/Solution**: Replaced blocking burst loop with timer-driven nonblocking sequencer.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`

---

### ISS-038 | 2026-03-16 | v2.3.x | Engine | Worked
**Invert Pan/Tilt Inconsistent Across Motion Paths**

- **Symptoms**: Manual movement inverted correctly but autonomous movements not inverted.
- **Root Cause**: Inversion applied in manual button logic but not uniformly in autonomous send paths.
- **Fix/Solution**: Moved axis inversion into `sentry_v2_comm.py` so all command paths use same hardware-space transform.
- **Files Modified**: `app/sentry_v2/sentry_v2_comm.py`

---

### ISS-039 | 2026-03-16 | v2.3.x | Camera | Worked
**Shared-Feed Mode Depended on Main-App Detections**

- **Symptoms**: Smart Sentry didn't run its own detection in shared-feed mode.
- **Fix/Solution**: Updated `MAIN_FILE_SINGLE_CAM.py` to pass frames only and call `process_frame(..., use_internal_detector=True)`.
- **Files Modified**: `MAIN_FILE_SINGLE_CAM.py`

---

### ISS-040 | 2026-03-16 | v2.3.x | Camera | Worked
**Camera Conflict Detection Failed in Standalone Window**

- **Symptoms**: Smart Sentry couldn't identify main app camera owner in standalone-window setup.
- **Root Cause**: Parent-walking lookup returned `None` in standalone `QMainWindow` setup.
- **Fix/Solution**: Added `set_host_main_window()` for explicit host registration.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`

---

### ISS-041 | 2026-03-16 | v2.3.x | UI | Worked
**Fixed-Width Settings Panel**

- **Symptoms**: Settings panel cramped, hard to navigate.
- **Fix/Solution**: Replaced fixed-width panel with horizontal splitter. Added `Panel Width` slider.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`

---

### ISS-042 | 2026-03-16 | v2.3.x | Engine | Worked
**Aiming Overshoot and Self-Chasing**

- **Symptoms**: Live tracking moves too abrupt. Motion-locked detection suppresses itself after each correction, losing target.
- **Fix/Solution**: Wired engagement speed into per-move bus-servo timing, raised move-time defaults, shortened motion suppression windows, aligned FOV defaults with 1280×720 baseline.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`

---

### ISS-043 | 2026-03-16 | v2.3.x | Engine | Worked
**Target Lost During Brief Detection Flicker**

- **Symptoms**: Moving targets dropped after brief flicker or track-ID churn, then reacquired at wrong position.
- **Fix/Solution**: Added nearest-target reacquisition using last known position and bbox overlap. Extended target-loss timeout.
- **Files Modified**: `app/sentry_v2/sentry_v2_engine.py`

---

### ISS-044 | 2026-03-16 | v2.3.x | UI/Engine | Worked
**HUD Too Utilitarian, Visual Servo Not Documented**

- **Fix/Solution**: Documented live visual-servo aiming controller as protected baseline. Upgraded HUD with pulse reticle, bracketed target box, cleaner panels.
- **Files Modified**: `app/sentry_v2/sentry_v2_overlay.py`, `app/sentry_v2/sentry_v2_tab.py`

---

### ISS-045 | 2026-03-16 | v2.3.x | Build | Worked
**Shared-Feed Startup Assumptions After Architecture Change**

- **Symptoms**: Smart Sentry still carried shared-feed code after switching to standalone-only launch.
- **Fix/Solution**: Removed Smart Sentry v2 from `MAIN_FILE_SINGLE_CAM.py`, removed dead env flag, normalized blank `camera_source` to standalone camera `0`.
- **Files Modified**: `MAIN_FILE_SINGLE_CAM.py`, `app/config/sentry_v2_settings.json`

---

### ISS-046 | 2026-04-09 | v3.0.0 | Engine | Worked
**Target-Loss Recovery Drifts Off-Home (Fixed Guard)**

- **Symptoms**: After target loss in fixed guard mode, turret drifts into recovery search and stays off-home indefinitely.
- **Fix/Solution**: Finite pursuit/local-scan/expanding-scan sequence. Stops indefinite retry in static guard mode. Shared return helper commands guard position when recovery expires.
- **Files Modified**: `app/sentry_v2/sentry_v2_engine.py`

---

### ISS-047 | 2026-04-07 | v3.0.0 | Build | Worked
**YOLO Models Not Found in Portable Build**

- **Symptoms**: Portable release can't load YOLO models. Quick startup deferred YOLO initialization too aggressively.
- **Fix/Solution**: Frozen builds prefer release-root `YOLO_MODELS` folder. Lazy auto-load under quick startup. Build script creates public model folder.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`, `build_smart_sentry_v2_3_1_portable.ps1`

---

### ISS-048 | 2026-04-07 | v3.0.0 | Build | Worked
**Python 3.12 / 3.11 Environment Drift**

- **Symptoms**: Local editing drifts between Python versions. PyQt5 reinstalls introduce stale VC runtime DLLs.
- **Fix/Solution**: Standardized on `.venv311` (Python 3.11.8). Added interpreter override to build scripts. Documented VC runtime override removal after PyQt reinstalls.
- **Files Modified**: `build_smart_sentry_v2_3_1_portable.ps1`
- **Notes**: Always use `.venv311` for running and building. If PyQt5 is reinstalled, check for and remove Qt-bundled `msvcp140.dll` / `vcruntime140.dll` from `PyQt5\Qt5\bin`.

---

### ISS-049 | 2026-04-07 | v3.0.0 | UI | Worked
**Overlay Clutter — Stale Branding and Noisy Status**

- **Symptoms**: Stale overlay branding, forced `moving` prefix on labels, noisy per-command status churn during tracking.
- **Fix/Solution**: Removed upper-left overlay label and `moving` prefix. Suppressed tracking-move churn in status.
- **Files Modified**: `app/sentry_v2/sentry_v2_overlay.py`, `app/sentry_v2/sentry_v2_tab.py`, `app/sentry_v2/ml_training_logger.py`, `app/sentry_v2/sentry_v2_engine.py`

---

### ISS-050 | 2026-04-07 | v3.0.0 | UI | Worked
**No Log Export Feature**

- **Symptoms**: No way to save Serial Output panel for later AI analysis without manual copy.
- **Fix/Solution**: Added `Export Logs` and `Open Log Folder` actions to Serial Output panel.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`

---

### ISS-051 | 2026-04-07 | v3.0.0 | Camera/UI | Worked
**Preview Frozen in Motion-Led Modes**

- **Symptoms**: Preview feels frozen during busy motion-led detection modes.
- **Fix/Solution**: Moved smoothness relief to preview-side presentation throttling. Kept detector/engine cadence intact. Limited motion-frame resize to pure motion-only modes.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`, `app/sentry_v2/sentry_v2_detector.py`

---

### ISS-052 | 2026-04-06 | v3.0.0 | UI | Worked
**Theme Transparency Inconsistent Across Buttons**

- **Symptoms**: Some buttons/panels more opaque than others at same transparency setting.
- **Root Cause**: Only subset of button types derived RGBA from `surface_opacity_pct`.
- **Fix/Solution**: Reworked `_theme_tokens()` so all button types use same alpha model. Removed hard-coded dialog button styling.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`

---

### ISS-053 | 2026-03-22 | v2.3.x | Build | Worked
**Standalone Validators Used Wrong Working Directory**

- **Symptoms**: Validators resolved wrong config path because of wrong working directory.
- **Fix/Solution**: Added launcher-style torch preload and switched to repo-root working directory.
- **Files Modified**: Standalone validator scripts

---

### ISS-054 | 2026-03-22 | v2.3.x | Detection | Worked
**Color Presets Brittle Under Moderate Shading**

- **Symptoms**: Named color presets lose tracking under moderate shading or desaturation.
- **Fix/Solution**: Tightened blue/cyan separation, blocked black full-frame grabs, broadened dim-shade floors, added second-pass saturation/value tolerance retry.
- **Files Modified**: `app/sentry_v2/target_filter.py`

---

### ISS-055 | 2026-03-21 | v2.3.x | Detection | Worked
**Motion-Locked Fallback Dropped by Class Filter**

- **Symptoms**: Motion-only detections lost when YOLO has no overlapping class box.
- **Fix/Solution**: Treated `moving_object` as non-semantic fallback class, survives class whitelist and size filtering.
- **Files Modified**: `app/sentry_v2/target_filter.py`

---

### ISS-056 | 2026-03-21 | v2.3.x | Engine | Worked
**Engagement Presets Drifted / Single-Target UI Showed Unused Controls**

- **Symptoms**: Preset labels drift. Single-target UI shows queue/order controls the engine ignores.
- **Fix/Solution**: Resolved presets against full `EngagementConfig` defaults. Forced queue length 1 + no slew for single-target. Disabled queue/order UI when single-target active.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`, `app/sentry_v2/sentry_v2_engine.py`

---

### ISS-057 | 2026-03-21 | v2.3.x | Config | Worked
**Overlay Defaults Flipped On for Old Configs**

- **Symptoms**: Threat scores and engagement-zone overlays appear unexpectedly on older config files.
- **Root Cause**: `SentryV2Config.from_dict()` fallback values didn't match dataclass defaults.
- **Fix/Solution**: Aligned fallback values with live dataclass defaults.
- **Files Modified**: `app/sentry_v2/sentry_v2_config.py`

---

### ISS-058 | 2026-03-21 | v2.3.x | Build | Worked
**Standalone Validators Targeted Legacy Hosting Path**

- **Fix/Solution**: Rewrote validators to exercise `run_sentry_v2.py` / `SentryV2StandaloneWindow`.
- **Files Modified**: Standalone validator scripts

---

### ISS-059 | 2026-03-16 | v2.3.x | UI | Worked
**Overlay and Target Selection Too Cluttered**

- **Fix/Solution**: Simplified HUD to one moving target at a time. Repurposed Filtered Target Mode into motion-locked pipeline. Motion-first defaults.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`, `app/sentry_v2/sentry_v2_overlay.py`

---

### ISS-060 | 2026-03-12 | v2.3.x | Camera | Worked
**COM Port `Incorrect function` on High-Number Ports**

- **Symptoms**: Dual-USB connection fails on Windows with `Incorrect function` for COM ports ≥ 10.
- **Root Cause**: Windows requires `\\.\COMxx` extended form for ports ≥ 10.
- **Fix/Solution**: Normalized COM names to accept `20`, `COM20`, `\\.\COM20`. Auto-retry with extended form for ports ≥ 10.
- **Files Modified**: `app/sentry_v2/sentry_v2_comm.py`
- **Notes**: Classic Windows serial port issue. Always use `\\.\COMxx` form for any port number.

---

### ISS-061 | 2026-03-12 | v2.3.x | Camera | Worked
**Single-Camera System Conflict**

- **Symptoms**: Smart Sentry competes for camera ownership on single-camera system.
- **Fix/Solution**: Blank `camera_source` defaults to shared-feed path. Blocked opening camera `0` when main app already owns it.
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`

---

### ISS-062 | 2026-03-12 | v2.3.x | Camera | Partial
**Secondary Camera Frame-Grab Stall**

- **Symptoms**: Secondary camera starts then hits repeated frame-grab failures until feed stalls permanently.
- **Fix/Solution**: Auto-close after 30 consecutive grab failures so UI recovers. (Partial — doesn't prevent the stall, only recovers from it.)
- **Files Modified**: `app/sentry_v2/sentry_v2_tab.py`

---

### ISS-063 | 2026-03-12 | v2.3.x | UI | Worked
**Missing Tooltips Across Settings**

- **Fix/Solution**: Added centralized tooltip text in `sentry_v2_tooltips.py` and applied across all tabs.
- **Files Modified**: `app/sentry_v2/sentry_v2_tooltips.py`, `app/sentry_v2/sentry_v2_tab.py`

---

### ISS-064 | 2026-03-12 | v2.3.x | Engine | Worked
**Frame Difference Chasing Own Camera Motion**

- **Symptoms**: Frame difference detection chases its own camera motion, loses target identity, fires without verified lock.
- **Fix/Solution**: Added stable bbox tracking, movement-triggered motion suppression, shared pan/tilt soft limits, precision-phase fire gating requiring lock before auto-fire.
- **Files Modified**: `app/sentry_v2/sentry_v2_engine.py`, `app/sentry_v2/sentry_v2_tab.py`

---

## Known Unresolved Issues

Issues investigated but **not fixed**. Check before re-attempting the same approach.

---

### ISS-U1 | 2026-03-15 | v2.3.x | Camera | Did Not Work
**Camera Conflict Guard Weak in Standalone Window**

- **Issue**: `_get_main_window()` parent-walk returns `None` in standalone `QMainWindow` setup.
- **Fix Tried**: Runtime-probed parent walk. Confirmed `None`.
- **Resolution**: Later fixed by [ISS-040](#iss-040) (explicit host-window registration).

---

### ISS-U2 | 2026-03-15 | v2.3.x | Engine | Did Not Work
**Invert Pan/Tilt Inconsistent in Autonomous Paths**

- **Issue**: Inversion applied in manual button logic but not in autonomous send paths.
- **Fix Tried**: Investigated only.
- **Resolution**: Later fixed by [ISS-038](#iss-038) (moved inversion to comm layer).

---

### ISS-U3 | 2026-03-15 | v2.3.x | UI | Did Not Work
**Motion Gate Threshold is a Dead Control**

- **Issue**: Threshold helper not used by live hybrid detection modes. UI control does nothing.
- **Fix Tried**: Investigated only — documented as dead control.
- **Resolution**: **Still unresolved.** Either wire it to active detection modes or remove from UI.

---

### ISS-U4 | 2026-03-15 | v2.3.x | Engine | Did Not Work
**Burst Firing Uses Blocking Sleeps**

- **Issue**: Current burst path is synchronous and blocking on UI thread.
- **Fix Tried**: Investigated only.
- **Resolution**: Later fixed by [ISS-037](#iss-037) (timer-driven nonblocking sequencer).

---

### ISS-U5 | 2026-03-15 | v2.3.x | Camera | Did Not Work
**Shared-Feed Mode Depended on Main-App Detections**

- **Issue**: Smart Sentry did not run its own detector in shared-feed mode.
- **Fix Tried**: Investigated only.
- **Resolution**: Later fixed by [ISS-039](#iss-039) (internal detector flag).
| 2026-04-16 | Auto-trigger could still stay effectively broken after the earlier tolerance fix because enabling the UI toggle did not normalize stale fire-gate settings already loaded from older profiles. | Added `normalize_auto_trigger_engagement()` in `app/sentry_v2/sentry_v2_config.py`, applied it on config construction, live engagement edits, and the auto-trigger toggle path in `app/sentry_v2/sentry_v2_tab.py`, synced the active and legacy settings JSON files to the fireable gate values, and added a regression test in `tests/test_sentry_v2_engagement_config.py`. | Worked |
| 2026-04-09 | PIR no-target completion could clear cue state without issuing an explicit return-home move, which let static guard setups stay parked at the final PIR hunt point and made operators think there was a hidden post-hunt dwell timer. | Updated `app/sentry_v2/sentry_v2_engine.py` so PIR no-target paths explicitly command the configured guard/home position, filled in missing tooltip coverage for the newer loss-recovery and guard/rest controls in `app/sentry_v2/sentry_v2_tab.py` plus `app/sentry_v2/sentry_v2_tooltips.py`, extended `test_pir_ui_config.py`, and corrected the PIR docs to state that `Cue Hold` is the pre-hunt dwell while a post-hunt stall is a bug, not a feature. | Worked |
| 2026-04-09 | Human voice playback could overlap with the ESP32 buzzer path, and operators still lacked a focused in-app voice diagnostics surface while investigating why Windows speech might be inaudible on some setups. | Added a persisted `mute_buzzer_when_human_voice_enabled` guard in `app/sentry_v2/sentry_v2_config.py`, suppressed firmware buzzer cues from `app/sentry_v2/sentry_v2_tab.py` while human voice mode is enabled, added a dedicated Voice Diagnostics group with backend, selected voice, speech-state, route note, fallback phrase, stop, refresh, and `Validate Voices` actions, filled in explicit tooltip coverage for the newer human-voice and assistant speech controls via `app/sentry_v2/sentry_v2_tooltips.py`, and verified in `.venv311` that both `Microsoft Zira Desktop` and `Microsoft David Desktop` are accepted by Qt and enter a valid speech state under the real validation path. | Worked |
| 2026-04-09 | PIR no-detect behavior could still feel too static at the cue point, and after-target-loss recovery still did not feel like a careful local hunt around the loss area. | Added a shared `Hunting` vs `Fast Reacquire` search-style control, introduced explicit PIR `Cue Hold` timing in `app/sentry_v2/sentry_v2_config.py` and `app/sentry_v2/sentry_v2_tab.py`, updated `app/sentry_v2/sentry_v2_engine.py` so PIR confirmation now leaves the cue sooner and target-loss recovery uses a denser directional local hunt with shorter step cadence, updated `app/sentry_v2/sentry_v2_pir_manager.py` so PIR scans start with a zone-biased local hunt before wider coverage, and synced the PIR/manual docs to the new contract. | Worked |
| 2026-04-09 | The new local assistant still had a narrow command set, could switch to the wrong detection mode for color requests, and made human-voice tuning cumbersome because operators had to adjust rate, pitch, and volume manually. | Expanded `app/sentry_v2/sentry_v2_tab.py` so the assistant can handle home/rest, link, camera, shortcut, face-recognition, and auto-speak requests, corrected the color-detection request path to the real Color Detection mode index, added persisted human-voice style presets, and updated the manual plus recent-updates log to match the new operator contract. | Worked |
| 2026-04-09 | The new in-app assistant still lacked a normal human-style spoken response mode and could only communicate through text plus the existing buzzer-style cues. | Added optional local human speech support in `app/sentry_v2/sentry_v2_tab.py` using PyQt5 QtTextToSpeech, exposed voice selection plus rate/pitch/volume controls in the Controls tab, added a `Conversational Voice` assistant mode with auto-speak support, and updated docs to treat human speech and buzzer speech as compatible output paths. | Worked |
| 2026-04-09 | Smart Sentry only had placeholder panels for Facial Recognition, Shortcut Keys, and AI Assistant, so operators could not register faces, announce recognized names, use documented hotkeys, or run the planned in-app assistant workflow. | Added a lightweight face-library runtime in `app/sentry_v2/face_identity.py`, wired face matching and friendly suppression into `app/sentry_v2/sentry_v2_tab.py`, extended `app/sentry_v2/sound_engine.py` with robotic identity-name cues, replaced the placeholder tabs with working UI, added a pinned `Quick Keys` action plus live shortcut bindings, and synced the docs. | Worked |
| 2026-04-09 | Smart Sentry’s operator UI still felt rigid after earlier splitter work because the window shell, tab navigation, manual control matrix, and several list surfaces kept using hard-coded sizes that did not adapt cleanly to panel-width changes. | Updated `app/sentry_v2/sentry_v2_tab.py` and `app/run_smart_sentry_v2_3_2.py` to lower the shell and panel sizing floor, add shared responsive panel metrics, scale the icon tab bar and prev/next tab buttons from live panel width, make manual control buttons resize with the panel, let preset grids use up to three columns, scale list heights with the available settings-panel height, add responsive width handling for compact zoom and threat-weight labels, tighten group/button spacing, and let dense settings rows in Presets, Camera, Detection, and Prompted Targets flip vertical on narrower panel widths instead of only squeezing horizontally. | Worked |
| 2026-04-08 | Rest tilt could be saved below the Guard minimum, but executing `Go Rest` still reused the generic manual clamp path and pulled the turret back up instead of honoring the saved rest pose. | Updated the rest-move execution path in `app/sentry_v2/sentry_v2_tab.py` to allow the rest command to clamp against the absolute sentry tilt limits instead of the normal guard/manual minimum, preserving valid below-guard rest tilts. | Worked |
| 2026-04-08 | PIR no-detect search could appear invisible because the scan sequence re-issued the already-visited cue center as its first scan point, making the turret seem to do nothing before returning to guard/patrol. | Updated `app/sentry_v2/sentry_v2_pir_manager.py` and the engine-side PIR confirmation flow so multi-point scans skip the duplicated center and immediately move to the first offset point after the cue no-detect window expires. | Worked |
| 2026-03-12 | Smart Sentry dual-USB connection could fail on Windows with `Incorrect function` when opening higher-number COM ports. | Normalized Smart Sentry COM names in `app/sentry_v2/sentry_v2_comm.py` so it accepts `20`, `COM20`, and `\\.\\COM20`, and retries with the Windows extended COM form for ports `>= 10`. | Worked |
| 2026-03-12 | Smart Sentry could accidentally compete for camera ownership on single-camera systems when a secondary camera was opened instead of using the main app feed. | Kept blank `camera_source` behavior as the default shared-feed path and blocked opening camera `0` when the main app already owns that source. | Worked |
| 2026-03-12 | Smart Sentry secondary camera could start and then hit repeated frame-grab failures until the feed stalled. | Auto-close the optional Smart Sentry-owned camera after 30 consecutive grab failures so the UI recovers cleanly instead of hanging on a dead feed. | Partial |
| 2026-03-12 | Smart Sentry settings lacked consistent, explanatory tooltips across the UI. | Added centralized tooltip text in `app/sentry_v2/sentry_v2_tooltips.py` and applied those tooltips across Smart Sentry settings tabs and control widgets. | Worked |
| 2026-03-12 | Frame Difference aiming could chase its own camera motion, lose target identity, and fire without a verified lock. | Added stable bbox tracking, movement-triggered motion suppression, shared pan/tilt soft limits, and precision-phase fire gating that now requires lock before auto-fire. | Worked |
| 2026-03-15 | Smart Sentry shared-feed mode documentation claimed detector independence, but the live integration still forwards main-app detection boxes into Smart Sentry processing. | Re-reviewed `MAIN_FILE_SINGLE_CAM.py` and `sentry_v2_tab.py` against the manual and confirmed shared-feed mode currently depends on main-app detections instead of running `SentryV2Detector` as the primary source. No code fix applied yet; documented as a verified gap. | Did Not Work |
| 2026-03-15 | Smart Sentry camera conflict protection was expected to block reopening the same camera already owned by the main app, but the current standalone-window hosting model weakens that guard. | Runtime-probed `_get_main_window()` from the live Smart Sentry tab and confirmed the parent-walk lookup returns `None` in the standalone `QMainWindow` setup. No code fix applied yet; documented for follow-up. | Did Not Work |
| 2026-03-15 | `Invert Pan` and `Invert Tilt` do not consistently affect autonomous Smart Sentry movement paths. | Compared manual movement, engine move callbacks, and communication send paths. Verified inversion is applied in manual button logic but not uniformly in autonomous send paths. No code fix applied yet; documented for follow-up. | Did Not Work |
| 2026-03-15 | Motion Gate Threshold appears in the Smart Sentry UI but is not currently honored by the active hybrid detection methods. | Traced the detector call graph and verified the threshold helper is not used by the live hybrid modes that the UI suggests it controls. No code fix applied yet; documented as a dead control. | Did Not Work |
| 2026-03-15 | Smart Sentry burst firing can stall frame updates because firing uses blocking sleeps on the UI thread. | Traced engine fire callbacks into the communication burst loop and confirmed the current burst path is synchronous and blocking. No code fix applied yet; documented for follow-up. | Did Not Work |
| 2026-03-16 | `Invert Pan` and `Invert Tilt` were inconsistent across manual, guard, and autonomous Smart Sentry motion. | Moved axis inversion into `app/sentry_v2/sentry_v2_comm.py` so all Smart Sentry command paths use the same hardware-space transform, and removed the manual-only sign flip. | Worked |
| 2026-03-16 | Smart Sentry shared-feed mode depended on main-app detection boxes instead of running its own detector pipeline. | Updated `MAIN_FILE_SINGLE_CAM.py` to pass frames only and call `process_frame(..., use_internal_detector=True)`, restoring Smart Sentry-owned detection in shared-feed mode. | Worked |
| 2026-03-16 | Camera conflict protection in Smart Sentry could not reliably identify the main app camera owner in the standalone-window setup. | Added explicit host-window registration via `set_host_main_window()` and used that reference in Smart Sentry camera conflict checks instead of relying only on parent walking. | Worked |
| 2026-03-16 | Smart Sentry burst fire blocked the UI thread during automatic fire sequences. | Replaced the blocking burst loop in the Smart Sentry tab path with a timer-driven nonblocking sequencer that emits the same fire on/off command pattern without freezing frame updates. | Worked |
| 2026-03-16 | Smart Sentry settings panel was cramped and fixed-width, making dense settings harder to navigate. | Replaced the fixed-width right panel with a horizontal splitter and added a bottom `Panel Width` slider backed by Smart Sentry config state. | Worked |
| 2026-03-16 | Smart Sentry overlay and target selection were too cluttered for motion-only operation. | Simplified the HUD to one moving target at a time, repurposed Filtered Target Mode into a motion-locked moving-object pipeline, and shifted the saved defaults to motion-first size, color, and class filtering. | Worked |
| 2026-03-16 | Smart Sentry aiming overshot and lost centering because live tracking moves were too abrupt and motion-locked detection suppressed itself after each correction. | Wired engagement speed into per-move bus-servo timing, raised sentry move-time defaults, shortened motion suppression windows for fine tracking corrections, and aligned sentry FOV defaults with the 1280x720 camera baseline. | Worked |
| 2026-03-16 | Smart Sentry could drop a moving target after brief detection flicker or track-ID churn, then reacquire inaccurately. | Added engine-side nearest-target reacquisition using last known target position and bbox overlap, and extended target-loss timeout slightly so precision tracking can stay on the same moving object longer. | Worked |
| 2026-03-16 | Smart Sentry needed the improved visual-servo aiming behavior documented as the protected baseline and the simplified HUD still looked too utilitarian. | Documented the live visual-servo aiming controller as the baseline that should only change for measured improvement, then upgraded the HUD with a pulse reticle, bracketed target box, and cleaner state/diagnostic panels. | Worked |
| 2026-03-16 | Smart Sentry still carried shared-feed startup assumptions after the architecture changed to standalone-only launch from the DB3000 launcher. | Removed Smart Sentry v2 from `MAIN_FILE_SINGLE_CAM.py`, removed the dead embedded-v2 launcher env flag, normalized blank `camera_source` to standalone camera `0`, and kept Smart Sentry runtime settings isolated in `app/config/sentry_v2_settings.json`. | Worked |
| 2026-03-21 | Motion-locked fallback detections could be dropped by class or size filters when YOLO had no overlapping class box for a moving target. | Treated `moving_object` as a non-semantic fallback class in `app/sentry_v2/target_filter.py` so motion-locked fallback boxes survive class whitelist and size filtering. | Worked |
| 2026-03-21 | Engagement preset labels could drift because presets did not fully define all active controller fields, and the single-target UI still exposed controls the engine would never honor. | Resolved engagement presets against full `EngagementConfig` defaults before apply/match, forced single-target presets to queue length `1` with no slew optimisation, and disabled the queue/order controls in the UI when single-target mode is active. | Worked |
| 2026-03-21 | Standalone overlay defaults for threat scores and engagement-zone visibility could flip on when older config files omitted those keys. | Aligned `SentryV2Config.from_dict()` fallback values with the live dataclass defaults so both overlays stay off unless explicitly enabled. | Worked |
| 2026-03-21 | Standalone validation scripts still targeted the legacy main-app hosting path instead of the current standalone launcher. | Rewrote the motion-locked and window validators to exercise `run_sentry_v2.py` / `SentryV2StandaloneWindow` and verify standalone-only assumptions. | Worked |
| 2026-03-22 | Standalone validators could still produce misleading results because they bypassed launcher-style torch preload and changed into the wrong working directory, which made Smart Sentry resolve the wrong relative config path. | Added launcher-style torch preload to the standalone validators and switched them back to the repo-root working directory so `app/config/sentry_v2_settings.json` resolves the same way as the real app. | Worked |
| 2026-04-06 | Theme panel transparency only affected a subset of Smart Sentry buttons and panels, leaving accent-backed controls visually more opaque than the rest of the UI. | Reworked `app/sentry_v2/sentry_v2_tab.py::_theme_tokens()` so regular, primary, utility, dpad, mode, and danger buttons all derive RGBA backgrounds from the same `surface_opacity_pct` alpha model, and removed the remaining hard-coded dialog button styling. | Worked |
| 2026-04-07 | Smart Sentry preview could feel frozen in busy motion-led modes and the detector resize shortcut risked changing hybrid-mode sensitivity. | Moved the smoothness relief to preview-side presentation throttling in `app/sentry_v2/sentry_v2_tab.py`, kept detector and engine cadence intact, and limited motion-frame resize acceleration in `app/sentry_v2/sentry_v2_detector.py` to pure motion-only modes with safe path-switch recovery. | Worked |
| 2026-04-07 | Smart Sentry operator feedback still had too much clutter: stale overlay branding, forced `moving` prefixes, noisy per-command status churn during tracking, and incomplete Threat AI status visibility. | Removed the upper-left overlay label and `moving` prefix in `app/sentry_v2/sentry_v2_overlay.py`, restored a readable command-status surface in `app/sentry_v2/sentry_v2_tab.py` by suppressing automatic tracking-move churn while keeping manual actions and failures visible, and tightened ML status plus folder-access reporting across `app/sentry_v2/ml_training_logger.py`, `app/sentry_v2/sentry_v2_engine.py`, and `app/sentry_v2/sentry_v2_tab.py`. | Worked |
| 2026-04-07 | Smart Sentry needed a direct way to preserve the Serial Output panel for later AI analysis without copying log text by hand. | Added timestamped `Export Logs` and `Open Log Folder` actions to the Serial Output panel in `app/sentry_v2/sentry_v2_tab.py`, storing exports under the repo snapshot tree for later analysis. | Worked |
| 2026-04-07 | After target loss in fixed guard mode, Smart Sentry could drift into recovery search and stay off-home instead of finishing the loss protocol and returning to guard. | Updated `app/sentry_v2/sentry_v2_engine.py` so target loss now runs a finite pursuit/local-scan/expanding-scan sequence, stops indefinite retry in static guard mode, and uses a shared return helper that commands the configured guard position when recovery expires. | Worked |
| 2026-04-08 | After target loss, Smart Sentry needed different behavior for crowded scenes versus sparse scenes and needed to switch quickly to a stronger visible target instead of always running one generic search path. | Added adaptive loss-context capture plus two named recovery protocols in `app/sentry_v2/sentry_v2_engine.py`, added the new recovery fields in `app/sentry_v2/sentry_v2_config.py`, exposed the new `After Target Loss` tuning group in `app/sentry_v2/sentry_v2_tab.py`, and documented the protocol contract in the manual and validation checklist. | Worked |
| 2026-04-07 | The portable v2.3.1 release could appear unable to load YOLO models because the documented public drop folder and the packaged default-model location diverged, and quick startup deferred YOLO initialization too aggressively. | Updated `app/sentry_v2/sentry_v2_tab.py` so frozen builds prefer the release-root `YOLO_MODELS` folder while still discovering bundled default models and still perform a later lazy auto-load under quick startup, then updated `build_smart_sentry_v2_3_1_portable.ps1` to create the public release-root model folder alongside the bundled support-folder defaults. | Worked |
| 2026-04-07 | Local Smart Sentry editing and packaging could drift between Python 3.12 and Python 3.11, while PyQt5 reinstalls could reintroduce stale VC runtime DLLs that made source runs unstable. | Standardized the release workflow on `.venv311`, added interpreter override plus `.venv311` preference to `build_smart_sentry_v2_3_1_portable.ps1`, pinned the workspace interpreter to `.venv311`, moved the default release output to `F:`, and documented removal of local Qt-bundled VC runtime overrides after PyQt reinstalls. | Worked |
| 2026-03-22 | Named color presets were too brittle under moderate shading and desaturation, and some presets still had edge-case misclassification risk in real camera-like footage. | Tightened blue/cyan separation, blocked black full-frame background grabs, broadened dim-shade preset floors, and added a second-pass saturation/value tolerance retry so the selected hue family still tracks under moderate shading without collapsing nearby colors together. | Worked |

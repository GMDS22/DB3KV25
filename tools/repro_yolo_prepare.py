from __future__ import annotations

import sys
import traceback
from pathlib import Path


def main() -> int:
    repo_root = Path(r"F:\SMART SENTRY V2\SMART SENTRY")
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))
    app_root = repo_root / "app"
    if str(app_root) not in sys.path:
        sys.path.insert(0, str(app_root))

    had_frozen = hasattr(sys, "frozen")
    orig_frozen = getattr(sys, "frozen", None)
    orig_executable = sys.executable
    sys.frozen = True
    sys.executable = r"F:\SMART SENTRY V3.0.0\SMART_SENTRY_V3.0.0.exe"
    try:
        from app.sentry_v2.sentry_v2_tab import SentryV2TabWidget

        class Dummy:
            pass

        dummy = Dummy()
        dummy._yolo_runtime_prepared = False
        dummy._runtime_lib_paths_prepared = False
        dummy._runtime_dll_dir_handles = []
        dummy._prepare_frozen_runtime_library_paths = SentryV2TabWidget._prepare_frozen_runtime_library_paths.__get__(dummy, Dummy)
        dummy._prepare_yolo_runtime = SentryV2TabWidget._prepare_yolo_runtime.__get__(dummy, Dummy)

        print("about_to_prepare", flush=True)
        result = dummy._prepare_yolo_runtime()
        print(f"prepare_result: {result}", flush=True)
        print(f"runtime_prepared: {dummy._yolo_runtime_prepared}", flush=True)
        print(f"lib_paths_prepared: {dummy._runtime_lib_paths_prepared}", flush=True)
        print(f"dll_handles: {len(dummy._runtime_dll_dir_handles)}", flush=True)
        return 0
    except Exception:
        traceback.print_exc()
        return 1
    finally:
        if had_frozen:
            sys.frozen = orig_frozen
        else:
            delattr(sys, "frozen")
        sys.executable = orig_executable


if __name__ == "__main__":
    raise SystemExit(main())

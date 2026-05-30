from __future__ import annotations

import importlib
import sys
from pathlib import Path


def read_active_version(repo_root: Path, default: str = "2.3.2") -> str:
    for version_name in (
        "SMART_SENTRY_V5_0_0_VERSION.txt",
        "SMART_SENTRY_V4_0_0_VERSION.txt",
        "SMART_SENTRY_V3_5_3_VERSION.txt",
        "SMART_SENTRY_V3_5_2_VERSION.txt",
        "SMART_SENTRY_V3_5_1_VERSION.txt",
        "SMART_SENTRY_V3_5_0_VERSION.txt",
        "SMART_SENTRY_V3_0_VERSION.txt",
        "SMART_SENTRY_V2_3_2_VERSION.txt",
        "SMART_SENTRY_V2_3_1_VERSION.txt",
        "SMART_SENTRY_V2_0_VERSION.txt",
    ):
        version_path = repo_root / version_name
        try:
            raw = version_path.read_text(encoding="utf-8").strip().lstrip("vV").strip()
            if raw:
                return raw
        except Exception:
            continue
    return default


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    app_root = repo_root / "app"
    active_version = read_active_version(repo_root)

    for path_obj in (repo_root, app_root):
        path_str = str(path_obj)
        if path_str not in sys.path:
            sys.path.insert(0, path_str)

    required_paths = [
        repo_root / "run.py",
        app_root / "main.py",
        app_root / "smart_sentry_meta.py",
        app_root / "theme_manager.py",
        app_root / "runtime_paths.py",
        app_root / "sentry_v2" / "sentry_v2_tab.py",
    ]
    missing_paths = [str(path_obj) for path_obj in required_paths if not path_obj.exists()]

    required_modules = [
        "app.main",
        "app.runtime_paths",
        "smart_sentry_meta",
        "theme_manager",
        "sentry_v2.sentry_v2_tab",
    ]
    import_failures: list[str] = []
    for module_name in required_modules:
        try:
            importlib.import_module(module_name)
        except Exception as exc:
            import_failures.append(f"{module_name}: {exc}")

    if missing_paths or import_failures:
        if missing_paths:
            print("PACKAGING_PREFLIGHT_MISSING_PATHS")
            for path_text in missing_paths:
                print(path_text)
        if import_failures:
            print("PACKAGING_PREFLIGHT_IMPORT_FAILURES")
            for failure in import_failures:
                print(failure)
        return 1

    print("PACKAGING_PREFLIGHT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
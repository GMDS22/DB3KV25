#!/usr/bin/env python3
"""Canonical SMART SENTRY launcher for the current app in this codebase."""

from __future__ import annotations
 
import importlib.util
import os
import sys
from pathlib import Path


def _read_active_version(root_dir: Path) -> str:
    for version_name in (
        "SMART_SENTRY_V3_0_VERSION.txt",
        "SMART_SENTRY_V2_3_2_VERSION.txt",
        "SMART_SENTRY_V2_3_1_VERSION.txt",
        "SMART_SENTRY_V2_0_VERSION.txt",
    ):
        version_path = root_dir / version_name
        try:
            raw = version_path.read_text(encoding="utf-8-sig").strip().lstrip("vV").strip()
            if raw:
                return raw
        except Exception:
            continue
    return "2.3.2"


def _configure_ml_runtime_env() -> None:
    try:
        os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")
        os.environ.setdefault("OMP_NUM_THREADS", "1")
        os.environ.setdefault("MKL_NUM_THREADS", "1")
        os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")
        os.environ.setdefault("CUDA_VISIBLE_DEVICES", "")
    except Exception:
        pass


def _preload_torch_runtime() -> None:
    try:
        
        import torch  # noqa: F401
    except Exception:
        pass


def main() -> int:
    _configure_ml_runtime_env()
    _preload_torch_runtime()

    root_dir = Path(__file__).resolve().parent
    app_dir = root_dir / "app"
    app_dir_str = str(app_dir)
    if app_dir.is_dir() and app_dir_str not in sys.path:
        sys.path.insert(0, app_dir_str)

    active_version = _read_active_version(root_dir)
    active_version_token = active_version.replace(".", "_")
    import_errors: list[str] = []

    launcher_candidates = [f"run_smart_sentry_v{active_version_token}"]
    if active_version_token == "3_0_0":
        launcher_candidates.append("run_smart_sentry_v3")
    launcher_candidates.append("run_smart_sentry_v2_3_2")

    for launcher_basename in launcher_candidates:
        module_name = f"app.{launcher_basename}"
        try:
            sentry_main = getattr(__import__(module_name, fromlist=["main"]), "main")
            return int(sentry_main())
        except Exception as exc:
            import_errors.append(f"{module_name}: {exc}")

        app_launcher = app_dir / f"{launcher_basename}.py"
        if getattr(sys, "frozen", False) or not app_launcher.is_file():
            continue

        spec = importlib.util.spec_from_file_location("smart_sentry_current_launcher", str(app_launcher))
        if spec is None or spec.loader is None:
            import_errors.append(f"{app_launcher}: unable to load launcher spec")
            continue

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        sentry_main = getattr(module, "main", None)
        if sentry_main is None:
            import_errors.append(f"{app_launcher}: launcher has no main()")
            continue
        return int(sentry_main())

    error_text = "; ".join(import_errors) if import_errors else "no launcher import attempts succeeded"
    raise ImportError(
        f"Unable to import Smart Sentry launcher. Expected packaged module or source file under {app_dir}. "
        f"Attempts: {error_text}"
    )


if __name__ == "__main__":
    raise SystemExit(main())

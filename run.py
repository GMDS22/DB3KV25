#!/usr/bin/env python3
"""Canonical SMART SENTRY launcher for the current app in this codebase."""

from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path


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

    import_errors: list[str] = []

    try:
        from app.run_smart_sentry_v2_3_2 import main as sentry_main
        return int(sentry_main())
    except Exception as exc:
        import_errors.append(f"app.run_smart_sentry_v2_3_2: {exc}")

    app_launcher = app_dir / "run_smart_sentry_v2_3_2.py"
    if not getattr(sys, "frozen", False) and app_launcher.is_file():
        spec = importlib.util.spec_from_file_location("smart_sentry_current_launcher", str(app_launcher))
        if spec is None or spec.loader is None:
            raise ImportError(f"Unable to load launcher spec: {app_launcher}")

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        sentry_main = getattr(module, "main", None)
        if sentry_main is None:
            raise AttributeError(f"Launcher has no main(): {app_launcher}")
        return int(sentry_main())

    error_text = "; ".join(import_errors) if import_errors else "no launcher import attempts succeeded"
    raise ImportError(
        f"Unable to import Smart Sentry launcher. Expected packaged module or source file at {app_launcher}. "
        f"Attempts: {error_text}"
    )


if __name__ == "__main__":
    raise SystemExit(main())

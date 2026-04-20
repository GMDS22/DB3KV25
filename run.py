#!/usr/bin/env python3
"""Canonical SMART SENTRY launcher for the current app in this codebase."""

from __future__ import annotations

import importlib
import importlib.util
import os
import sys
from pathlib import Path
from typing import Any


CANONICAL_LAUNCHER_BASENAME = "run_smart_sentry_v2_3_2"
CANONICAL_FROZEN_LAUNCHER_MODULE = f"app.{CANONICAL_LAUNCHER_BASENAME}"


def _invoke_launcher_main(sentry_main: Any) -> int:
    if not callable(sentry_main):
        raise AttributeError("launcher has no callable main()")
    return int(sentry_main())


def _load_launcher_module_from_path(launcher_path: Path, module_name: str) -> Any:
    spec = importlib.util.spec_from_file_location(module_name, str(launcher_path))
    if spec is None or spec.loader is None:
        raise ImportError(f"unable to load launcher spec from {launcher_path}")

    existing_module = sys.modules.get(module_name)
    if existing_module is not None:
        return existing_module

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    except Exception:
        sys.modules.pop(module_name, None)
        raise

    return module


def _run_launcher_path(launcher_path: Path, run_name: str) -> int:
    launcher_module = _load_launcher_module_from_path(launcher_path, run_name)
    return _invoke_launcher_main(getattr(launcher_module, "main", None))


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
    frozen = bool(getattr(sys, "frozen", False))
    meipass = getattr(sys, "_MEIPASS", "")

    if frozen:
        # In frozen mode the canonical launcher is embedded in PYZ via --hidden-import.
        # Never use spec_from_file_location on a frozen module — PyInstaller's importer
        # intercepts exec_module and corrupts its internal loading state, causing every
        # subsequent importlib.import_module call to also fail with
        # "cannot load module more than once per process".
        module = sys.modules.get(CANONICAL_FROZEN_LAUNCHER_MODULE)
        if module is None:
            try:
                module = importlib.import_module(CANONICAL_FROZEN_LAUNCHER_MODULE)
            except Exception as exc:
                raise ImportError(
                    f"Unable to import frozen launcher {CANONICAL_FROZEN_LAUNCHER_MODULE}. "
                    f"Ensure --hidden-import {CANONICAL_FROZEN_LAUNCHER_MODULE} is present "
                    f"in the build spec. _MEIPASS={meipass!r}. Error: {exc}"
                ) from exc
        return _invoke_launcher_main(getattr(module, "main", None))

    # Source run: locate app dir and execute launcher file directly.
    app_dir = root_dir / "app"
    app_dir_str = str(app_dir)
    if app_dir.is_dir() and app_dir_str not in sys.path:
        sys.path.insert(0, app_dir_str)

    launcher_basename = CANONICAL_LAUNCHER_BASENAME
    app_launcher = app_dir / f"{launcher_basename}.py"
    import_errors: list[str] = []

    if app_launcher.is_file():
        try:
            return _run_launcher_path(
                app_launcher,
                f"smart_sentry_current_launcher_{launcher_basename}",
            )
        except Exception as exc:
            import_errors.append(f"{app_launcher}: {exc}")

    # Developer fallback: import as package module.
    try:
        module = importlib.import_module(CANONICAL_FROZEN_LAUNCHER_MODULE)
        return _invoke_launcher_main(getattr(module, "main", None))
    except Exception as exc:
        import_errors.append(f"{CANONICAL_FROZEN_LAUNCHER_MODULE}: {exc}")

    error_text = "; ".join(import_errors) if import_errors else "no launcher import attempts succeeded"
    raise ImportError(
        f"Unable to import Smart Sentry launcher. Expected {app_launcher} or "
        f"packaged module {CANONICAL_FROZEN_LAUNCHER_MODULE}. Attempts: {error_text}"
    )


if __name__ == "__main__":
    raise SystemExit(main())

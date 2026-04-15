#!/usr/bin/env python3
"""Canonical SMART SENTRY launcher for the current app in this codebase."""

from __future__ import annotations

import importlib
import importlib.util
import os
import sys
from pathlib import Path
from typing import Any, cast


FROZEN_TERMINAL_LAUNCHERS = {
    "3_0_0": "app.run_smart_sentry_v2_3_2",
    "3": "app.run_smart_sentry_v2_3_2",
    "2_3_2": "app.run_smart_sentry_v2_3_2",
    "2_3_1": "app.run_smart_sentry_v2_3_1",
}


def _invoke_launcher_main(sentry_main: Any) -> int:
    if not callable(sentry_main):
        raise AttributeError("launcher has no callable main()")
    return int(cast(Any, sentry_main)())


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
    runtime_roots: list[Path] = [root_dir]
    frozen = bool(getattr(sys, "frozen", False))
    meipass = getattr(sys, "_MEIPASS", "")
    if frozen and meipass:
        runtime_roots.insert(0, Path(meipass))

    runtime_roots = list(dict.fromkeys(runtime_roots))
    app_dir = root_dir / "app"
    for candidate_root in runtime_roots:
        candidate_app_dir = candidate_root / "app"
        if candidate_app_dir.is_dir():
            app_dir = candidate_app_dir
            break

    app_dir_str = str(app_dir)
    if not frozen and app_dir.is_dir() and app_dir_str not in sys.path:
        sys.path.insert(0, app_dir_str)

    active_version = _read_active_version(root_dir)
    active_version_token = active_version.replace(".", "_")
    import_errors: list[str] = []

    if frozen:
        frozen_launcher_module = FROZEN_TERMINAL_LAUNCHERS.get(
            active_version_token,
            f"app.run_smart_sentry_v{active_version_token}",
        )
        frozen_import_errors: list[str] = []

        candidate_module_names = [frozen_launcher_module]
        canonical_basename = frozen_launcher_module.rsplit(".", 1)[-1]
        for fallback_name in (canonical_basename, f"smart_sentry_frozen_launcher_{canonical_basename}"):
            if fallback_name not in candidate_module_names:
                candidate_module_names.append(fallback_name)

        for module_name in candidate_module_names:
            module = sys.modules.get(module_name)
            if module is not None:
                try:
                    return _invoke_launcher_main(getattr(module, "main", None))
                except Exception as exc:
                    frozen_import_errors.append(f"{module_name}: {exc}")
                    continue

        try:
            module = importlib.import_module(frozen_launcher_module)
            return _invoke_launcher_main(getattr(module, "main", None))
        except Exception as exc:
            frozen_import_errors.append(f"{frozen_launcher_module}: {exc}")

        frozen_error_text = "; ".join(frozen_import_errors) if frozen_import_errors else "no frozen launcher import attempts succeeded"
        raise ImportError(
            f"Unable to import Smart Sentry launcher for frozen runtime from {app_dir}. "
            f"Resolved terminal launcher: {frozen_launcher_module}. Attempts: {frozen_error_text}"
        )

    launcher_candidates = [f"run_smart_sentry_v{active_version_token}"]
    if active_version_token == "3_0_0":
        launcher_candidates.append("run_smart_sentry_v3")
    elif active_version_token != "2_3_2":
        # Keep legacy fallback only for source runs, not packaged builds.
        if not frozen:
            launcher_candidates.append("run_smart_sentry_v2_3_2")

    # Preserve order while removing duplicates.
    launcher_candidates = list(dict.fromkeys(launcher_candidates))

    for launcher_basename in launcher_candidates:
        app_launcher = app_dir / f"{launcher_basename}.py"

        # Deterministic path for packaged/frozen runtime: execute launcher file directly.
        if app_launcher.is_file():
            try:
                return _run_launcher_path(
                    app_launcher,
                    f"smart_sentry_current_launcher_{launcher_basename}",
                )
            except Exception as exc:
                import_errors.append(f"{app_launcher}: {exc}")
                if frozen:
                    # In packaged mode, never fall through to package imports.
                    continue

        # Source/developer fallback: import as package module when file execution is unavailable.
        module_name = f"app.{launcher_basename}"
        if frozen:
            import_errors.append(f"{module_name}: launcher file not found for frozen runtime")
            continue

        try:
            module = importlib.import_module(module_name)
            return _invoke_launcher_main(getattr(module, "main", None))
        except Exception as exc:
            if "cannot load module more than once per process" in str(exc).lower():
                # In frozen runtimes, the module may already be present in sys.modules.
                preloaded = sys.modules.get(module_name)
                if preloaded is not None:
                    return _invoke_launcher_main(getattr(preloaded, "main", None))
            import_errors.append(f"{module_name}: {exc}")

        if not app_launcher.is_file():
            continue

        try:
            module = _load_launcher_module_from_path(
                app_launcher,
                f"smart_sentry_current_launcher_{launcher_basename}",
            )
            return _invoke_launcher_main(getattr(module, "main", None))
        except Exception as exc:
            import_errors.append(f"{app_launcher}: {exc}")
            continue

    error_text = "; ".join(import_errors) if import_errors else "no launcher import attempts succeeded"
    raise ImportError(
        f"Unable to import Smart Sentry launcher. Expected packaged module or source file under {app_dir}. "
        f"Attempts: {error_text}"
    )


if __name__ == "__main__":
    raise SystemExit(main())

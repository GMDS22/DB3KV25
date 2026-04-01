#!/usr/bin/env python3
"""Root-level Smart Sentry v2 launcher wrapper."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def main() -> int:
    root_dir = Path(__file__).resolve().parent
    app_dir = root_dir / "app"
    app_launcher = root_dir / "app" / "run_sentry_v2.py"
    if not app_launcher.is_file():
        raise FileNotFoundError(f"Missing app launcher: {app_launcher}")

    # Ensure package imports like `sentry_v2.*` resolve when loading by spec.
    app_dir_str = str(app_dir)
    if app_dir_str not in sys.path:
        sys.path.insert(0, app_dir_str)

    # Load the app launcher by absolute path to avoid self-import ambiguity.
    spec = importlib.util.spec_from_file_location("db3000_sentry_v2_launcher", str(app_launcher))
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load launcher spec: {app_launcher}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    app_main = getattr(module, "main", None)
    if app_main is None:
        raise AttributeError(f"Launcher has no main(): {app_launcher}")
    return int(app_main())


if __name__ == "__main__":
    raise SystemExit(main())
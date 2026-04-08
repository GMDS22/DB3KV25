from __future__ import annotations

import sys
from pathlib import Path


def is_frozen_runtime() -> bool:
    return bool(getattr(sys, "frozen", False))


def runtime_root_path() -> Path:
    if is_frozen_runtime():
        meipass = getattr(sys, "_MEIPASS", None)
        if meipass:
            return Path(meipass).resolve()
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent.parent


def app_root_path() -> Path:
    runtime_root = runtime_root_path()
    runtime_app = runtime_root / "app"
    if runtime_app.is_dir():
        return runtime_app
    return Path(__file__).resolve().parent
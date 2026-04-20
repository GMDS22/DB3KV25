#!/usr/bin/env python3
"""SMART SENTRY entry point."""

import os
import sys
from pathlib import Path

os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")
os.environ.setdefault("CUDA_VISIBLE_DEVICES", "")

# Pre-initialize asyncio before any torch import occurs.
# torch/__init__.py triggers asyncio/__init__.py through typing_extensions._deprecated.
# If asyncio is only partially initialized when that happens (mid-exec_module), the
# relative import `from .base_events import *` in asyncio/__init__.py fails with
# ModuleNotFoundError in the frozen bundle. Importing asyncio here ensures it is
# fully initialized in sys.modules before torch is ever touched.
import asyncio  # noqa: E402

if not getattr(sys, "frozen", False):
    _app_dir = str(Path(__file__).resolve().parent / "app")
    if _app_dir not in sys.path:
        sys.path.insert(0, _app_dir)

from app.main import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())

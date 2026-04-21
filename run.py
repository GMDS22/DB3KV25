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

# Pre-initialize unittest before any torch import occurs.
# torch.utils._config_module imports unittest, which triggers unittest/__init__.py
# (via exec_module) while torch is still mid-import. unittest/__init__.py line 60
# does `from .result import *` — if unittest.__path__ is not yet established in the
# frozen importer context, this fails with ModuleNotFoundError: No module named
# 'unittest.result'. Importing unittest here pre-populates sys.modules so torch's
# import chain finds unittest already initialized and skips re-execution.
import unittest  # noqa: E402

# Pre-import torchgen before any torch import occurs.
# torch/utils/_python_dispatch.py line 13-14 does `import torchgen; import torchgen.model`
# at module level. In the frozen exe (one-dir build), torchgen must be physically present
# in the support folder. PyInstaller does not automatically discover torchgen from torch's
# transitive dependency analysis. The build script uses --collect-submodules torchgen to
# bundle it; this pre-import documents the dependency and ensures it appears in sys.modules
# before any sub-thread triggers torch.nn imports. (ISS-079)
import torchgen  # noqa: E402
import torchgen.model  # noqa: E402
import torch.testing  # noqa: E402  (ISS-080 fix — torch.autograd.gradcheck imports this at module level)

# Pre-import PIL on the main thread before any background threads start.
# PIL/__init__.py line 18 does `from . import _version` then `del _version`. In the
# frozen bundle, if PIL is first imported from a worker thread (_prepare_yolo_runtime),
# the relative import `from . import _version` fails with:
#   ImportError: cannot import name '_version' from partially initialized module 'PIL'
# because another import chain (e.g. cv2 data path) may have already placed a partially
# initialized PIL in sys.modules before __init__ finished. Importing PIL and PIL.Image
# here on the main thread ensures PIL is fully initialized before any thread uses it.
# (ISS-083)
import PIL  # noqa: E402
import PIL.Image  # noqa: E402

# Pre-import yaml on the main thread before any background threads start.
# ultralytics/utils/__init__.py line 562 does `import yaml` inside YAML.__init__,
# which fires on a worker thread. yaml/__init__.py line 2 does `from .error import *`;
# if yaml is partially initialized in sys.modules from a concurrent path, this raises
# ModuleNotFoundError: No module named 'yaml.error'. (ISS-084)
import yaml  # noqa: E402

# Pre-import ultralytics on the main thread — the definitive fix for the entire class
# of partial-init races in _prepare_yolo_runtime.
#
# ultralytics/__init__.py triggers a chain of third-party imports (yaml, PIL, requests,
# urllib3, etc.), each of which has relative imports in its own __init__.py. In the
# frozen bundle, if any of these packages are first imported from the worker thread
# (_prepare_yolo_runtime), PyInstaller's frozen importer may race: the relative import
# (e.g. `from .error import *` in yaml/__init__.py) runs before __path__ is fully
# established, causing ModuleNotFoundError for the sub-module.
#
# By importing ultralytics here, on the main thread, all of the above transitive
# dependencies are fully initialized in sys.modules. When the worker thread later calls
# `import ultralytics`, Python finds it already complete and skips re-execution entirely.
# (ISS-084, ISS-083 definitive fix)
import ultralytics  # noqa: E402

if not getattr(sys, "frozen", False):
    _app_dir = str(Path(__file__).resolve().parent / "app")
    if _app_dir not in sys.path:
        sys.path.insert(0, _app_dir)

from app.main import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())

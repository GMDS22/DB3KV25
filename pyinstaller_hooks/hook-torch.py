import sys

from PyInstaller.compat import is_win
from PyInstaller.utils.hooks import PY_DYLIB_PATTERNS
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import collect_dynamic_libs
from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.utils.hooks import is_module_satisfies
from PyInstaller.utils.hooks import logger


EXCLUDED_TORCH_PREFIXES = (
    "torch.utils.benchmark",
    "torch.distributed.algorithms",
    "torch.distributed.autograd",
    "torch.distributed.checkpoint",
    "torch.distributed.elastic",
    "torch.distributed.fsdp",
    "torch.distributed.launcher",
    "torch.distributed.nn",
    "torch.distributed.optim",
    "torch.distributed.pipeline",
    "torch.distributed.pipelining",
    "torch.distributed.rpc",
    "torch.distributed.run",
    "torch.distributed.tensor",
    "torch.distributed._composable",
    "torch.distributed._serialization",
    "torch.distributed._shard",
    "torch.distributed._sharded_tensor",
    "torch.distributed._sharding_spec",
    "torch.distributed._spmd",
    "torch.distributed._symmetric_memory",
    "torch.distributed.device_mesh",
    "torch.onnx._internal.exporter._testing",
    "torch.onnx._internal.exporter._verification",
    "torch.onnx.testing",
    "torch.onnx.verification",
)


def _include_torch_submodule(module_name):
    for prefix in EXCLUDED_TORCH_PREFIXES:
        if module_name == prefix or module_name.startswith(prefix + "."):
            return False
    return True


module_collection_mode = "pyz+py"
warn_on_missing_hiddenimports = False

datas = collect_data_files(
    "torch",
    excludes=[
        "**/*.h",
        "**/*.hpp",
        "**/*.cuh",
        "**/*.lib",
        "**/*.cpp",
        "**/*.pyi",
        "**/*.cmake",
    ],
)

# ISS-082 fix: torch.testing.__init__ imports torch._C.FileCheck (C extension).
# This causes PyInstaller's static analysis to fail for ALL torch.testing modules,
# so they cannot be included in PYZ via hiddenimports — even explicit collect_submodules
# calls (ISS-081) register names but all show "not found" in the build log.
# Fix: physically copy torch/testing/**/*.py files into bundle as data using a direct
# filesystem glob. collect_data_files(..., includes=["**/*.py"]) is ineffective because
# PyInstaller strips .py files from data collection (they are treated as module files).
# Using a direct glob to os.path/glob bypasses that filter entirely.
import glob as _glob
import os as _os
import torch as _torch_probe
_torch_root = _os.path.dirname(_torch_probe.__file__)
_testing_root = _os.path.join(_torch_root, "testing")
_testing_py_count = 0
if _os.path.isdir(_testing_root):
    for _py_src in _glob.glob(_os.path.join(_testing_root, "**", "*.py"), recursive=True):
        _rel_dir = _os.path.relpath(_os.path.dirname(_py_src), _torch_root)
        datas.append((_py_src, _os.path.join("torch", _rel_dir)))
        _testing_py_count += 1
if _testing_py_count:
    logger.info("custom hook-torch: added %d torch.testing .py files via direct glob datas (ISS-082)", _testing_py_count)
else:
    logger.warning("custom hook-torch: torch.testing direct glob found nothing — check torch install (ISS-082)")

hiddenimports = collect_submodules("torch", filter=_include_torch_submodule, on_error="ignore")

binaries = collect_dynamic_libs("torch", search_patterns=PY_DYLIB_PATTERNS + ["*.so.*"])

if is_win:
    logger.info("custom hook-torch: filtered torch hidden imports down to %d modules", len(hiddenimports))

if is_module_satisfies("torch >= 2.0.0") and sys.getrecursionlimit() < 5000:
    logger.info("custom hook-torch: raising recursion limit to 5000")
    sys.setrecursionlimit(5000)
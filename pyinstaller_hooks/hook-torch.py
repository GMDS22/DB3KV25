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

hiddenimports = collect_submodules("torch", filter=_include_torch_submodule, on_error="ignore")
binaries = collect_dynamic_libs("torch", search_patterns=PY_DYLIB_PATTERNS + ["*.so.*"])

if is_win:
    logger.info("custom hook-torch: filtered torch hidden imports down to %d modules", len(hiddenimports))

if is_module_satisfies("torch >= 2.0.0") and sys.getrecursionlimit() < 5000:
    logger.info("custom hook-torch: raising recursion limit to 5000")
    sys.setrecursionlimit(5000)
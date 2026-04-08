import sys
import os

from cx_Freeze import Executable, setup
from smart_sentry_build_config import build_exe_options, env_flag, read_active_version


sys.setrecursionlimit(max(10000, sys.getrecursionlimit()))


INCLUDE_MODELS = env_flag("SMART_SENTRY_INCLUDE_MODELS")
INCLUDE_SKLEARN = env_flag("SMART_SENTRY_INCLUDE_SKLEARN")
INCLUDE_YTDLP = not env_flag("SMART_SENTRY_EXCLUDE_YTDLP")
ACTIVE_VERSION = read_active_version()

build_exe_options = build_exe_options(
    include_models=INCLUDE_MODELS,
    include_sklearn=INCLUDE_SKLEARN,
    include_ytdlp=INCLUDE_YTDLP,
)
BUILD_EXE_DIR = str(os.environ.get("SMART_SENTRY_BUILD_EXE_DIR", "")).strip()
if BUILD_EXE_DIR:
    build_exe_options["build_exe"] = BUILD_EXE_DIR

executables = [
    Executable(
        script="run.py",
        target_name=f"SMART_SENTRY_V{ACTIVE_VERSION}.exe",
        base="Win32GUI",
        icon="smart_sentry_icon.ico",
    )
]

setup(
    name=f"SMART SENTRY V{ACTIVE_VERSION}",
    version=ACTIVE_VERSION,
    description=f"SMART SENTRY portable build for V{ACTIVE_VERSION}",
    options={"build_exe": build_exe_options},
    executables=executables,
)
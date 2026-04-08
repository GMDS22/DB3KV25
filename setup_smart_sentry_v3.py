import sys

from cx_Freeze import Executable, setup
from smart_sentry_build_config import build_exe_options, read_active_version


sys.setrecursionlimit(max(10000, sys.getrecursionlimit()))


ACTIVE_VERSION = read_active_version()

build_exe_options = build_exe_options(
    include_models=True,
    include_sklearn=True,
    include_ytdlp=True,
)


executables = [
    Executable(
        script="run.py",
        target_name="SMART_SENTRY.exe",
        base="Win32GUI",
    )
]

setup(
    name="SMART_SENTRY",
    version=ACTIVE_VERSION,
    description=f"SMART SENTRY build for V{ACTIVE_VERSION}",
    options={"build_exe": build_exe_options},
    executables=executables,
)
from cx_Freeze import Executable, setup

build_exe_options = {
    "include_msvcr": True,
    "optimize": 1,
    "packages": [
        "os",
        "sys",
        "cv2",
        "numpy",
        "serial",
        "ultralytics",
        "torch",
        "sklearn",
        "yt_dlp",
    ],
    "includes": [
        "PyQt5.QtCore",
        "PyQt5.QtGui",
        "PyQt5.QtWidgets",
    ],
    "excludes": [
        "tkinter",
        "pytest",
        "matplotlib.tests",
    ],
    "include_files": [
        ("app/sentry_v2", "app/sentry_v2"),
        ("app/config", "app/config"),
        ("app/models", "app/models"),
        ("app/YOLO_MODELS", "app/YOLO_MODELS"),
        ("app/LOGO.png", "app/LOGO.png"),
        ("requirements-sentry-v2-portable.txt", "requirements-sentry-v2-portable.txt"),
        ("SENTRY_V2_PORTABLE_INCLUDE_LIST.md", "SENTRY_V2_PORTABLE_INCLUDE_LIST.md"),
        ("SENTRY_V2_PORTABLE_FIX_LOG_2026-03-24.md", "SENTRY_V2_PORTABLE_FIX_LOG_2026-03-24.md"),
    ],
}

executables = [
    Executable(
        script="app/run_sentry_v2.py",
        target_name="SmartSentryV2.exe",
        base="Win32GUI",
    )
]

setup(
    name="SmartSentryV2Portable",
    version="1.0.0",
    description="Smart Sentry v2 portable build",
    options={"build_exe": build_exe_options},
    executables=executables,
)

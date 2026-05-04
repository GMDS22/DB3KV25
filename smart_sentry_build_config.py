import os
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent


def read_active_version(default: str = "2.3.2") -> str:
    for version_name in (
        "SMART_SENTRY_V3_5_3_VERSION.txt",
        "SMART_SENTRY_V3_5_2_VERSION.txt",
        "SMART_SENTRY_V3_5_1_VERSION.txt",
        "SMART_SENTRY_V3_5_0_VERSION.txt",
        "SMART_SENTRY_V3_0_VERSION.txt",
        "SMART_SENTRY_V2_3_2_VERSION.txt",
        "SMART_SENTRY_V2_3_1_VERSION.txt",
        "SMART_SENTRY_V2_0_VERSION.txt",
    ):
        version_path = REPO_ROOT / version_name
        try:
            raw = version_path.read_text(encoding="utf-8").strip().lstrip("vV").strip()
            if raw:
                return raw
        except Exception:
            continue
    return default


def env_flag(name: str) -> bool:
    value = str(os.environ.get(name, "")).strip().lower()
    return value in {"1", "true", "yes", "on"}


def existing_include_files(include_models: bool) -> list[tuple[str, str]]:
    include_files: list[tuple[str, str]] = []

    base_entries = [
        ("app/sentry_v2", "app/sentry_v2"),
        ("app/config", "app/config"),
        ("app/LOGO.png", "app/LOGO.png"),
        ("smart_sentry_icon.ico", "smart_sentry_icon.ico"),
        ("requirements-sentry-v2-portable.txt", "requirements-sentry-v2-portable.txt"),
        ("RECENT_UPDATES.json", "RECENT_UPDATES.json"),
        ("SMART_SENTRY_BUILD_RELEASE_STANDARD.md", "SMART_SENTRY_BUILD_RELEASE_STANDARD.md"),
        ("SMART_SENTRY_V3_5_3_COMPILATION_PROTOCOL.md", "SMART_SENTRY_V3_5_3_COMPILATION_PROTOCOL.md"),
        ("SMART_SENTRY_V3_5_0_COMPILATION_PROTOCOL.md", "SMART_SENTRY_V3_5_0_COMPILATION_PROTOCOL.md"),
        ("SMART_SENTRY_V3_0_0_COMPILATION_PROTOCOL.md", "SMART_SENTRY_V3_0_0_COMPILATION_PROTOCOL.md"),
        ("SMART_SENTRY_RELEASE_HOLD_CONVENTION.md", "SMART_SENTRY_RELEASE_HOLD_CONVENTION.md"),
        ("SMART_SENTRY_V2_3_2_COMPILATION_PROTOCOL.md", "SMART_SENTRY_V2_3_2_COMPILATION_PROTOCOL.md"),
        ("SMART_SENTRY_V2_3_1_COMPILATION_PROTOCOL.md", "SMART_SENTRY_V2_3_1_COMPILATION_PROTOCOL.md"),
        ("SMART_SENTRY_APP_CHANGE_IMPACT.md", "SMART_SENTRY_APP_CHANGE_IMPACT.md"),
        ("SENTRY_V2_PORTABLE_INCLUDE_LIST.md", "SENTRY_V2_PORTABLE_INCLUDE_LIST.md"),
        ("SENTRY_V2_PORTABLE_FIX_LOG_2026-03-24.md", "SENTRY_V2_PORTABLE_FIX_LOG_2026-03-24.md"),
    ]
    for version_marker in (
        "SMART_SENTRY_V3_5_3_VERSION.txt",
        "SMART_SENTRY_V3_5_2_VERSION.txt",
        "SMART_SENTRY_V3_5_1_VERSION.txt",
        "SMART_SENTRY_V3_5_0_VERSION.txt",
        "SMART_SENTRY_V2_3_2_VERSION.txt",
        "SMART_SENTRY_V2_3_1_VERSION.txt",
        "SMART_SENTRY_V3_0_VERSION.txt",
        "SMART_SENTRY_V2_0_VERSION.txt",
    ):
        if (REPO_ROOT / version_marker).exists():
            base_entries.append((version_marker, version_marker))

    if include_models:
        base_entries.extend(
            [
                ("YOLO_MODELS", "YOLO_MODELS"),
            ]
        )

    for source, destination in base_entries:
        if (REPO_ROOT / source).exists():
            include_files.append((source, destination))
    return include_files


def build_packages(include_sklearn: bool, include_ytdlp: bool) -> list[str]:
    packages = [
        "os",
        "sys",
        "cv2",
        "numpy",
        "serial",
        "ultralytics",
        "torch",
    ]
    if include_sklearn:
        packages.append("sklearn")
    if include_ytdlp:
        packages.append("yt_dlp")
    return packages


def build_exe_options(*, include_models: bool, include_sklearn: bool, include_ytdlp: bool) -> dict:
    return {
        "include_msvcr": True,
        "optimize": 1,
        "packages": build_packages(include_sklearn, include_ytdlp),
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
        "include_files": existing_include_files(include_models),
    }
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def _clean_requirement_name(raw: str) -> str:
    token = raw.strip()
    token = re.split(r"[<>=!~]", token, maxsplit=1)[0]
    return token.strip().lower().replace("_", "-")


def _load_requirement_names(requirements_path: Path) -> set[str]:
    names: set[str] = set()
    for line in requirements_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        names.add(_clean_requirement_name(stripped))
    return names


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent

    required_files = [
        repo_root / "run.py",
        repo_root / "build_smart_sentry_v2_3_2_portable.ps1",
        repo_root / "requirements-sentry-v2-portable.txt",
        repo_root / "SMART_SENTRY_BUILD_RELEASE_STANDARD.md",
        repo_root / "SENTRY_V2_PORTABLE_INCLUDE_LIST.md",
        repo_root / "SMART_SENTRY_V5_0_0_COMPILATION_PROTOCOL.md",
        repo_root / "SMART_SENTRY_V5_0_0_VERSION.txt",
        repo_root / "tools" / "validate_packaging_entrypoints.py",
    ]

    canonical_config_files = [
        repo_root / "app" / "config" / "smart_sentry_settings.json",
        repo_root / "app" / "config" / "smart_sentry_custom_presets.json",
        repo_root / "app" / "config" / "smart_sentry_prompted_targets.json",
        repo_root / "app" / "config" / "smart_sentry_faces.json",
    ]

    required_model_paths = [
        repo_root / "models" / "kokoro" / "kokoro-v1.0.onnx",
        repo_root / "models" / "kokoro" / "voices-v1.0.bin",
        repo_root / "models" / "vosk",
        repo_root / "YOLO_MODELS",
    ]

    required_dependencies = {
        "requests",
        "numpy",
        "opencv-python",
        "sounddevice",
        "vosk",
        "simpleaudio",
        "edge-tts",
        "kokoro-onnx",
        "azure-cognitiveservices-speech",
        "pyserial",
        "pyqt5",
        "ultralytics",
        "lap",
        "torch",
        "scikit-learn",
        "yt-dlp",
        "cx-freeze",
        "pyinstaller",
    }

    missing: list[str] = []

    for path in required_files:
        if not path.exists():
            missing.append(f"missing-required-file:{path}")

    for path in required_model_paths:
        if not path.exists():
            missing.append(f"missing-required-model-path:{path}")

    for path in canonical_config_files:
        if not path.exists():
            missing.append(f"missing-canonical-config:{path}")
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            missing.append(f"invalid-json:{path}:{exc}")

    requirements_path = repo_root / "requirements-sentry-v2-portable.txt"
    if requirements_path.exists():
        listed = _load_requirement_names(requirements_path)
        missing_requirements = sorted(req for req in required_dependencies if req not in listed)
        for req in missing_requirements:
            missing.append(f"missing-requirement-entry:{req}")

    print("SMART_SENTRY_V5_BUILD_SURFACE_AUDIT")
    print(f"repo_root={repo_root}")
    print("expected_release_marker=SMART_SENTRY_V5_0_0_VERSION.txt")
    print("canonical_configs=4")
    print("required_dependencies=18")

    if missing:
        print("BUILD_SURFACE_AUDIT_FAIL")
        for item in missing:
            print(item)
        return 1

    print("BUILD_SURFACE_AUDIT_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

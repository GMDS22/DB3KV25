from __future__ import annotations

from pathlib import Path
import re
import sys

BASE_DIR = Path(__file__).resolve().parent
MAIN_FILE = BASE_DIR / "app" / "MAIN_FILE_SINGLE_CAM.py"


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return path.read_text(encoding="utf-8", errors="ignore")


def _extract_func(text: str, name: str) -> str:
    marker = f"def {name}"
    start = text.find(marker)
    if start == -1:
        return ""
    # Use a fixed window to avoid stopping at nested defs.
    return text[start : start + 6000]


def main() -> int:
    text = _read_text(MAIN_FILE)

    # Guard 1: update_frame should avoid sync model loads in YOLO modes.
    if "ASYNC ONLY: model loads are never run in update_frame()." not in text:
        print("FAIL: Missing async-only guard comment for YOLO model loads.")
        return 1

    # Guard 2: threaded YOLO should be force-enabled in YOLO/Hybrid modes.
    if "Threaded inference forced ON" not in text:
        print("FAIL: Missing threaded YOLO responsiveness guard.")
        return 1

    # Guard 3: async YOLO should not be gated by speed_opt.
    func = _extract_func(text, "_speed_yolo_detect_async")
    if not func:
        print("FAIL: _speed_yolo_detect_async not found.")
        return 1
    if "_speed_opt_active" in func:
        print("FAIL: _speed_yolo_detect_async still gated by speed_opt.")
        return 1

    # Guard 4: async max-age default should be <= 0.35s for responsiveness.
    if "0.35" not in func:
        print("FAIL: _speed_yolo_detect_async max-age default not set to 0.35s.")
        return 1

    print("OK: YOLO responsiveness guards present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

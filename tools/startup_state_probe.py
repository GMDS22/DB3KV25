from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PyQt5.QtWidgets import QApplication

REPO_ROOT = Path(r"F:\SMART SENTRY V2\SMART SENTRY")
APP_ROOT = REPO_ROOT / "app"
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
if str(APP_ROOT) not in sys.path:
    sys.path.insert(0, str(APP_ROOT))

from app.sentry_v2.sentry_v2_tab import SentryV2TabWidget


def main() -> int:
    app = QApplication(sys.argv)
    widget = SentryV2TabWidget()
    widget.show()

    end = time.time() + 12.0
    while time.time() < end:
        app.processEvents()
        time.sleep(0.05)

    yolo_status = ""
    if hasattr(widget, "_lbl_yolo_status") and widget._lbl_yolo_status is not None:
        yolo_status = widget._lbl_yolo_status.text()

    result = {
        "yolo_status": yolo_status,
        "yolo_runtime_prepared": bool(getattr(widget, "_yolo_runtime_prepared", False)),
        "yolo_loading": bool(getattr(widget, "_yolo_loading", False)),
        "selected_yolo_model": str(getattr(widget.config.detection_mode, "yolo_model_name", "")),
        "selected_yolo_dir": str(getattr(widget.config.detection_mode, "yolo_model_dir", "")),
        "sound_transport_info": str(widget._comm.sound_transport_info()),
        "can_send_sound": bool(widget._comm.can_send_sound()),
        "log_tail": [
            f"[{ts}] [{category}] {message}"
            for ts, category, message in getattr(widget, "_log_entries", [])[-40:]
        ],
    }

    try:
        widget.close()
    finally:
        for _ in range(20):
            app.processEvents()
            time.sleep(0.01)

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

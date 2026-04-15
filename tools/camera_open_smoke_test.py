from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication

APP_DIR = Path(__file__).resolve().parents[1] / "app"
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from run_smart_sentry_v2_3_2 import SmartSentryV2_3_2StandaloneWindow


def _log_tail(tab: object, limit: int = 25) -> list[str]:
    entries = getattr(tab, "_log_entries", [])[-limit:]
    return [f"[{ts}] [{category}] {message}" for ts, category, message in entries]


def main() -> int:
    result: dict[str, object] = {
        "ok": False,
        "requested": [1280, 720],
        "actual": None,
        "source_kind": None,
        "recovery_attempts": None,
        "recovery_in_progress": None,
        "status": None,
        "log_tail": [],
    }

    app = QApplication(sys.argv)
    window = SmartSentryV2_3_2StandaloneWindow()
    window.show()
    tab = window.sentry_v2_tab

    try:
        tab._edit_cam_source.setText("0")
        tab._set_camera_dimensions(1280, 720)

        def _open_camera() -> None:
            if not tab._has_local_source():
                tab._toggle_camera()

        QTimer.singleShot(0, _open_camera)

        deadline = time.time() + 80.0
        open_since: float | None = None
        while time.time() < deadline:
            app.processEvents()
            time.sleep(0.05)

            if tab._cap is not None and tab._local_source_kind == "camera":
                if open_since is None:
                    open_since = time.time()
                actual_w = int(tab._cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                actual_h = int(tab._cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                result["actual"] = [actual_w, actual_h]
                result["source_kind"] = tab._local_source_kind
                result["recovery_attempts"] = int(getattr(tab, "_camera_recovery_attempts", -1))
                result["recovery_in_progress"] = bool(getattr(tab, "_camera_recovery_in_progress", False))
                result["status"] = str(tab._lbl_cam_status.text()) if hasattr(tab, "_lbl_cam_status") else ""
                if actual_w == 1280 and actual_h == 720 and (time.time() - open_since) >= 6.0:
                    if not bool(getattr(tab, "_camera_recovery_in_progress", False)):
                        result["ok"] = True
                        break
            else:
                open_since = None

        result["log_tail"] = _log_tail(tab)
    finally:
        try:
            tab._close_camera(log_close=False)
        except Exception:
            pass
        try:
            window.close()
        except Exception:
            pass
        for _ in range(20):
            app.processEvents()
            time.sleep(0.02)

    print(json.dumps(result, indent=2))
    return 0 if bool(result["ok"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
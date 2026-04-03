#!/usr/bin/env python3
"""Standalone Smart Sentry v2 launcher.

Runs Smart Sentry v2 without booting the full main app.
This is the direct test path for Sentry-only work.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path


def _configure_ml_runtime_env() -> None:
    """Stabilize torch/ultralytics startup on Windows before Qt imports."""
    try:
        os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")
        os.environ.setdefault("OMP_NUM_THREADS", "1")
        os.environ.setdefault("MKL_NUM_THREADS", "1")
        os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")
        os.environ.setdefault("CUDA_VISIBLE_DEVICES", "")
    except Exception:
        pass


def _preload_torch_runtime() -> None:
    """Preload torch before importing the Qt-heavy Sentry stack."""
    try:
        import torch  # noqa: F401
    except Exception:
        # Lazy-loading paths inside the Sentry stack handle optional ML runtime failures.
        return


_configure_ml_runtime_env()
_preload_torch_runtime()

APP_DIR = Path(__file__).resolve().parent
app_dir_str = str(APP_DIR)
if app_dir_str not in sys.path:
    sys.path.insert(0, app_dir_str)

from PyQt5.QtWidgets import QApplication, QMainWindow

try:
    from smart_sentry_meta import get_app_title
except Exception:
    def get_app_title() -> str:
        return "Smart Sentry v2"

try:
    from theme_manager import ThemeManager
except Exception:
    class ThemeManager:
        def apply_theme(self, _theme_name: str = "dark") -> None:
            return

from sentry_v2.sentry_v2_tab import (
    SENTRY_V2_PANEL_DEFAULT_WIDTH,
    SENTRY_V2_STANDALONE_THEME,
    SENTRY_V2_WIDGET_MIN_WIDTH,
    SentryV2TabWidget,
)


class SentryV2StandaloneWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(get_app_title())

        self.sentry_v2_tab = SentryV2TabWidget(self)
        self.sentry_v2_tab.set_host_main_window(None)
        self.setCentralWidget(self.sentry_v2_tab)
        self.setMinimumWidth(max(SENTRY_V2_WIDGET_MIN_WIDTH, self.minimumSizeHint().width()))
        self.resize(max(1460, SENTRY_V2_PANEL_DEFAULT_WIDTH + 840), 940)

    def closeEvent(self, event):
        try:
            self.sentry_v2_tab.cleanup()
        except Exception:
            pass
        super().closeEvent(event)


def main() -> int:
    app = QApplication(sys.argv)
    ThemeManager().apply_theme("dark")
    app.setStyleSheet(app.styleSheet() + SENTRY_V2_STANDALONE_THEME)
    window = SentryV2StandaloneWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    raise SystemExit(main())
#!/usr/bin/env python3
"""Standalone Smart Sentry v2 launcher.

Runs Smart Sentry v2 without booting the full main app.
This is the direct test path for Sentry-only work.
"""

from __future__ import annotations

import os
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

try:
    from db3k_meta import get_app_title
except Exception:
    def get_app_title() -> str:
        return "Smart Sentry"

try:
    from theme_manager import ThemeManager
except Exception:
    class ThemeManager:
        def apply_theme(self, _theme_name: str = "dark") -> None:
            return

from sentry_v2.sentry_v2_tab import SENTRY_V2_STANDALONE_THEME, SentryV2TabWidget


class SentryV2StandaloneWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(f"{get_app_title()} - Smart Sentry v2")
        self.resize(1460, 940)

        self.sentry_v2_tab = SentryV2TabWidget(self)
        self.sentry_v2_tab.set_host_main_window(None)
        self.setCentralWidget(self.sentry_v2_tab)

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
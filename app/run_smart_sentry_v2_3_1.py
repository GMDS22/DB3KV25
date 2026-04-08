#!/usr/bin/env python3
"""Standalone SMART SENTRY launcher for the v2.3.1 release."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any


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
        return


_configure_ml_runtime_env()
_preload_torch_runtime()

APP_DIR = Path(__file__).resolve().parent
app_dir_str = str(APP_DIR)
if app_dir_str not in sys.path:
    sys.path.insert(0, app_dir_str)

from PyQt5.QtCore import QEvent, QPoint, Qt
from PyQt5.QtGui import QCloseEvent, QIcon, QMouseEvent
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QStyle, QVBoxLayout, QWidget

try:
    from smart_sentry_meta import get_app_title
except Exception:
    def get_app_title() -> str:
        return "SMART SENTRY V2.3.1"


def _apply_theme(theme_name: str = "dark") -> None:
    try:
        from theme_manager import ThemeManager

        ThemeManager().apply_theme(theme_name)
    except Exception:
        return


from sentry_v2.sentry_v2_tab import (
    SENTRY_V2_PANEL_DEFAULT_WIDTH,
    SENTRY_V2_STANDALONE_THEME,
    SENTRY_V2_WIDGET_MIN_WIDTH,
    SentryV2TabWidget,
)


FRAMELESS_SMART_SENTRY_THEME = """
#smartSentryWindowRoot {
    background: #08131d;
}
#smartSentryWindowControls {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0d1924, stop:1 #142638);
    border-bottom: 1px solid rgba(173, 201, 226, 0.14);
}
#smartSentryWindowControls QPushButton {
    min-width: 28px;
    max-width: 28px;
    min-height: 24px;
    max-height: 24px;
    border: 1px solid rgba(173, 201, 226, 0.18);
    border-radius: 6px;
    background: rgba(9, 23, 35, 0.72);
}
#smartSentryWindowControls QPushButton:hover {
    background: rgba(38, 69, 97, 0.9);
}
#smartSentryWindowControls QPushButton:pressed {
    background: rgba(62, 108, 149, 0.92);
}
"""


def _qt_attr(namespace: Any, attr_name: str, fallback: Any = None) -> Any:
    value = getattr(namespace, attr_name, None)
    if value is not None:
        return value
    return fallback


def _style_icon(widget: QWidget, standard_pixmap_name: str) -> QIcon:
    style = widget.style() or QApplication.style()
    standard_pixmap = _qt_attr(QStyle, standard_pixmap_name)
    if style is None or standard_pixmap is None:
        return QIcon()
    return style.standardIcon(standard_pixmap)


QT_LEFT_BUTTON = _qt_attr(Qt, "LeftButton", _qt_attr(getattr(Qt, "MouseButton", None), "LeftButton", 0))
QT_WINDOW = _qt_attr(Qt, "Window", _qt_attr(getattr(Qt, "WindowType", None), "Window", 0))
QT_FRAMELESS_WINDOW_HINT = _qt_attr(
    Qt,
    "FramelessWindowHint",
    _qt_attr(getattr(Qt, "WindowType", None), "FramelessWindowHint", 0),
)
QT_WINDOW_MIN_MAX_BUTTONS_HINT = _qt_attr(
    Qt,
    "WindowMinMaxButtonsHint",
    _qt_attr(getattr(Qt, "WindowType", None), "WindowMinMaxButtonsHint", 0),
)
QT_WINDOW_CLOSE_BUTTON_HINT = _qt_attr(
    Qt,
    "WindowCloseButtonHint",
    _qt_attr(getattr(Qt, "WindowType", None), "WindowCloseButtonHint", 0),
)
QT_WA_TRANSLUCENT_BACKGROUND = _qt_attr(
    Qt,
    "WA_TranslucentBackground",
    _qt_attr(getattr(Qt, "WidgetAttribute", None), "WA_TranslucentBackground", 0),
)
QT_WA_STYLED_BACKGROUND = _qt_attr(
    Qt,
    "WA_StyledBackground",
    _qt_attr(getattr(Qt, "WidgetAttribute", None), "WA_StyledBackground", 0),
)
QT_EVENT_WINDOW_STATE_CHANGE = _qt_attr(
    QEvent,
    "WindowStateChange",
    _qt_attr(getattr(QEvent, "Type", None), "WindowStateChange", None),
)


class FramelessControlStrip(QWidget):
    def __init__(self, host_window: "SmartSentryV2_3_1StandaloneWindow") -> None:
        super().__init__(host_window)
        self._host_window = host_window
        self._drag_offset: QPoint | None = None
        self.setObjectName("smartSentryWindowControls")
        self.setFixedHeight(34)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)
        layout.setSpacing(6)
        layout.addStretch(1)

        self._btn_min = QPushButton()
        self._btn_min.setToolTip("Minimize window")
        self._btn_min.setIcon(_style_icon(self, "SP_TitleBarMinButton"))
        self._btn_min.clicked.connect(self._host_window.showMinimized)
        layout.addWidget(self._btn_min)

        self._btn_restore = QPushButton()
        self._btn_restore.clicked.connect(self._host_window.toggle_maximized)
        layout.addWidget(self._btn_restore)

        self._btn_close = QPushButton()
        self._btn_close.setToolTip("Close window")
        self._btn_close.setIcon(_style_icon(self, "SP_TitleBarCloseButton"))
        self._btn_close.clicked.connect(self._close_host_window)
        layout.addWidget(self._btn_close)

        self.sync_window_state()

    def _close_host_window(self) -> None:
        self._host_window.close()

    def sync_window_state(self) -> None:
        is_maximized = self._host_window.isMaximized()
        icon_name = "SP_TitleBarNormalButton" if is_maximized else "SP_TitleBarMaxButton"
        self._btn_restore.setIcon(_style_icon(self, icon_name))
        self._btn_restore.setToolTip("Restore window" if is_maximized else "Maximize window")

    def mouseDoubleClickEvent(self, a0: QMouseEvent | None) -> None:
        event = a0
        if event is not None and event.button() == QT_LEFT_BUTTON:
            self._host_window.toggle_maximized()
            event.accept()
            return
        super().mouseDoubleClickEvent(event)

    def mousePressEvent(self, a0: QMouseEvent | None) -> None:
        event = a0
        if event is not None and event.button() == QT_LEFT_BUTTON and not self._host_window.isMaximized():
            self._drag_offset = event.globalPos() - self._host_window.frameGeometry().topLeft()
            event.accept()
            return
        super().mousePressEvent(event)

    def mouseMoveEvent(self, a0: QMouseEvent | None) -> None:
        event = a0
        if event is not None and self._drag_offset is not None and event.buttons() & QT_LEFT_BUTTON:
            self._host_window.move(event.globalPos() - self._drag_offset)
            event.accept()
            return
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, a0: QMouseEvent | None) -> None:
        event = a0
        self._drag_offset = None
        super().mouseReleaseEvent(event)


class SmartSentryV2_3_1StandaloneWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(get_app_title())
        self.setWindowFlags(
            QT_WINDOW | QT_FRAMELESS_WINDOW_HINT | QT_WINDOW_MIN_MAX_BUTTONS_HINT | QT_WINDOW_CLOSE_BUTTON_HINT
        )
        self.setAttribute(QT_WA_TRANSLUCENT_BACKGROUND, True)

        self._window_root = QWidget(self)
        self._window_root.setObjectName("smartSentryWindowRoot")
        self._window_root.setAttribute(QT_WA_STYLED_BACKGROUND, True)
        self._window_layout = QVBoxLayout(self._window_root)
        self._window_layout.setContentsMargins(0, 0, 0, 0)
        self._window_layout.setSpacing(0)

        self._control_strip = FramelessControlStrip(self)
        self._window_layout.addWidget(self._control_strip)

        self.sentry_v2_tab = SentryV2TabWidget(self)
        self.sentry_v2_tab.set_host_main_window(None)
        self._window_layout.addWidget(self.sentry_v2_tab, 1)
        self.setCentralWidget(self._window_root)
        self.setMinimumWidth(max(SENTRY_V2_WIDGET_MIN_WIDTH, self.minimumSizeHint().width()))
        self.resize(max(1460, SENTRY_V2_PANEL_DEFAULT_WIDTH + 840), 940)

    def toggle_maximized(self) -> None:
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
        self._control_strip.sync_window_state()

    def changeEvent(self, a0: QEvent | None) -> None:
        event = a0
        if event is not None and event.type() == QT_EVENT_WINDOW_STATE_CHANGE and hasattr(self, "_control_strip"):
            self._control_strip.sync_window_state()
        super().changeEvent(event)

    def closeEvent(self, a0: QCloseEvent | None) -> None:
        event = a0
        if getattr(self.sentry_v2_tab, "_cleanup_started", False):
            super().closeEvent(event)
            return
        def _finish_close() -> None:
            self.close()
        try:
            if event is not None:
                event.ignore()
        except Exception:
            pass
        try:
            self.sentry_v2_tab.begin_graceful_shutdown(on_complete=_finish_close)
        except Exception:
            try:
                self.sentry_v2_tab.cleanup()
            except Exception:
                pass
            super().closeEvent(event)


def main() -> int:
    app = QApplication(sys.argv)
    _apply_theme("dark")
    app.setStyleSheet(app.styleSheet() + SENTRY_V2_STANDALONE_THEME + FRAMELESS_SMART_SENTRY_THEME)
    window = SmartSentryV2_3_1StandaloneWindow()
    window.show()
    return app.exec_()


SmartSentryV3StandaloneWindow = SmartSentryV2_3_1StandaloneWindow


if __name__ == "__main__":
    raise SystemExit(main())
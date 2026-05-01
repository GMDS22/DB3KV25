#!/usr/bin/env python3
"""Standalone SMART SENTRY launcher for the v2.3.2 release."""

from __future__ import annotations

import ctypes
import os
import sys
from pathlib import Path
from typing import Any

from ctypes import wintypes


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


APP_DIR = Path(__file__).resolve().parent
if not getattr(sys, "frozen", False):
    app_dir_str = str(APP_DIR)
    if app_dir_str not in sys.path:
        sys.path.insert(0, app_dir_str)

from PyQt5.QtCore import QEvent, QPoint, Qt, QTimer, pyqtSignal
from PyQt5.QtGui import QCloseEvent, QIcon, QMouseEvent, QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QStyle,
    QVBoxLayout,
    QWidget,
)

try:
    from smart_sentry_meta import get_app_title
except Exception:
    def get_app_title() -> str:
        return "SMART SENTRY V2.3.2"


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

WM_NCHITTEST = 0x0084
HTCLIENT = 1
HTLEFT = 10
HTRIGHT = 11
HTTOP = 12
HTTOPLEFT = 13
HTTOPRIGHT = 14
HTBOTTOM = 15
HTBOTTOMLEFT = 16
HTBOTTOMRIGHT = 17
FRAMELESS_RESIZE_BORDER = 8


class FramelessControlStrip(QWidget):
    def __init__(self, host_window: "SmartSentryV2_3_2StandaloneWindow") -> None:
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


_EXIT_OVERLAY_STYLE = """
#exitSplashRoot {
    background: #0a1828;
    border: 1px solid rgba(173, 201, 226, 0.18);
    border-radius: 10px;
}
#exitSplashStatus {
    color: rgba(173, 201, 226, 0.88);
    font-size: 15px;
    letter-spacing: 0.5px;
}
#exitSplashSep {
    background: rgba(173, 201, 226, 0.14);
    min-height: 1px;
    max-height: 1px;
}
QProgressBar#exitSplashBar {
    background: rgba(173, 201, 226, 0.07);
    border: none;
    border-radius: 2px;
    min-height: 5px;
    max-height: 5px;
}
QProgressBar#exitSplashBar::chunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #1a6fa8, stop:0.5 #26a6d1, stop:1 #3ecfef);
    border-radius: 2px;
}
"""

_EXIT_OVERLAY_W = 540
_EXIT_OVERLAY_H = 200

_EXIT_STATUS_STEPS = [
    (0,    "Closing camera feed",                 8),
    (450,  "Turning off accessories",             30),
    (1050, "Returning turret to rest position",   58),
    (1800, "Disconnecting from boards",           86),
]
_EXIT_DOTS_INTERVAL_MS = 380
_EXIT_BAR_TICK_MS = 40
_EXIT_GOODBYE_LINGER_MS = 900


class ExitSplashOverlay(QWidget):
    """Full-window overlay displayed during the graceful shutdown sequence."""

    close_ready = pyqtSignal()

    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.setObjectName("exitSplashRoot")
        self.setAttribute(QT_WA_STYLED_BACKGROUND, True)
        self.setFixedSize(_EXIT_OVERLAY_W, _EXIT_OVERLAY_H)
        self.setStyleSheet(_EXIT_OVERLAY_STYLE)

        root_layout = QVBoxLayout(self)
        root_layout.setContentsMargins(32, 28, 32, 28)
        root_layout.setSpacing(0)
        root_layout.addStretch(1)

        # Separator
        sep = QWidget()
        sep.setObjectName("exitSplashSep")
        sep.setFixedHeight(1)
        root_layout.addWidget(sep)

        root_layout.addSpacing(20)

        # Status label
        self._status_label = QLabel("", alignment=Qt.AlignCenter)  # type: ignore[call-overload]
        self._status_label.setObjectName("exitSplashStatus")
        root_layout.addWidget(self._status_label)

        root_layout.addSpacing(16)

        # Progress bar
        self._bar = QProgressBar()
        self._bar.setObjectName("exitSplashBar")
        self._bar.setRange(0, 100)
        self._bar.setValue(0)
        self._bar.setTextVisible(False)
        self._bar.setFixedHeight(5)
        root_layout.addWidget(self._bar)

        root_layout.addStretch(1)

        # Internal state
        self._dots_count = 0
        self._status_base = ""
        self._bar_target = 0
        self._shutdown_done = False

        # Dots animation timer
        self._dots_timer = QTimer(self)
        self._dots_timer.setInterval(_EXIT_DOTS_INTERVAL_MS)
        self._dots_timer.timeout.connect(self._tick_dots)

        # Bar easing timer
        self._bar_timer = QTimer(self)
        self._bar_timer.setInterval(_EXIT_BAR_TICK_MS)
        self._bar_timer.timeout.connect(self._tick_bar)

        # Schedule the status step sequence
        for delay_ms, text, bar_pct in _EXIT_STATUS_STEPS:
            QTimer.singleShot(delay_ms, lambda t=text, p=bar_pct: self._set_step(t, p))

        self._dots_timer.start()
        self._bar_timer.start()

    def _set_step(self, text: str, bar_pct: int) -> None:
        if self._shutdown_done:
            return
        self._status_base = text
        self._dots_count = 0
        self._bar_target = bar_pct
        self._update_status_label()

    def _tick_dots(self) -> None:
        if self._shutdown_done:
            return
        self._dots_count = (self._dots_count + 1) % 4
        self._update_status_label()

    def _update_status_label(self) -> None:
        dots = "." * self._dots_count
        self._status_label.setText(self._status_base + dots)

    def _tick_bar(self) -> None:
        current = self._bar.value()
        if current < self._bar_target:
            step = max(1, (self._bar_target - current) // 5)
            self._bar.setValue(min(current + step, self._bar_target))

    def on_shutdown_complete(self) -> None:
        """Call when the actual cleanup() has finished — shows 'Goodbye' then emits close_ready."""
        if self._shutdown_done:
            return
        self._shutdown_done = True
        self._dots_timer.stop()
        self._bar_timer.stop()
        self._bar_target = 100
        self._bar.setValue(100)
        self._status_label.setText("All systems safe\u2002\u2014\u2002Goodbye")
        QTimer.singleShot(_EXIT_GOODBYE_LINGER_MS, self.close_ready.emit)


class SmartSentryV2_3_2StandaloneWindow(QMainWindow):
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
        self.setMinimumSize(max(SENTRY_V2_WIDGET_MIN_WIDTH, self.minimumSizeHint().width()), 760)
        self.resize(max(1280, SENTRY_V2_PANEL_DEFAULT_WIDTH + 760), 860)
        self.sentry_v2_tab.restore_window_geometry(self)

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

    def nativeEvent(self, eventType, message):  # type: ignore[override]
        if sys.platform == "win32" and eventType == b"windows_generic_MSG" and not self.isMaximized():
            msg = wintypes.MSG.from_address(int(message))
            if msg.message == WM_NCHITTEST:
                hit = self._hit_test_resize_border(msg.lParam)
                if hit != HTCLIENT:
                    return True, hit
        return super().nativeEvent(eventType, message)

    def resizeEvent(self, a0) -> None:  # type: ignore[override]
        super().resizeEvent(a0)
        self._reposition_exit_overlay()

    def _hit_test_resize_border(self, l_param: int) -> int:
        x = ctypes.c_short(l_param & 0xFFFF).value
        y = ctypes.c_short((l_param >> 16) & 0xFFFF).value
        pos = self.mapFromGlobal(QPoint(x, y))
        rect = self.rect()
        border = FRAMELESS_RESIZE_BORDER
        left = pos.x() <= border
        right = pos.x() >= rect.width() - border
        top = pos.y() <= border
        bottom = pos.y() >= rect.height() - border

        if top and left:
            return HTTOPLEFT
        if top and right:
            return HTTOPRIGHT
        if bottom and left:
            return HTBOTTOMLEFT
        if bottom and right:
            return HTBOTTOMRIGHT
        if left:
            return HTLEFT
        if right:
            return HTRIGHT
        if top:
            return HTTOP
        if bottom:
            return HTBOTTOM
        return HTCLIENT

    def _reposition_exit_overlay(self) -> None:
        overlay = getattr(self, "_exit_overlay", None)
        if overlay is None:
            return
        parent = self.centralWidget() or self
        pw, ph = parent.width(), parent.height()
        ow, oh = overlay.width(), overlay.height()
        overlay.move((pw - ow) // 2, (ph - oh) // 2)

    def closeEvent(self, a0: QCloseEvent | None) -> None:
        event = a0
        # Second call after cleanup: allow the real close through.
        if getattr(self.sentry_v2_tab, "_cleanup_started", False):
            super().closeEvent(event)
            return
        # Overlay already shown — ignore duplicate close triggers until shutdown completes.
        if getattr(self, "_exit_overlay", None) is not None:
            try:
                if event is not None:
                    event.ignore()
            except Exception:
                pass
            return
        try:
            if event is not None:
                event.ignore()
        except Exception:
            pass
        try:
            self.sentry_v2_tab.persist_window_geometry(self, immediate=True)
        except Exception:
            pass
        # Stop the camera feed immediately so the overlay shows the logo cleanly.
        try:
            self.sentry_v2_tab.close_camera_for_exit()
        except Exception:
            pass
        # Create and show the exit overlay centered over the window.
        try:
            parent = self.centralWidget() or self
            overlay = ExitSplashOverlay(parent)
            pw, ph = parent.width(), parent.height()
            ow, oh = _EXIT_OVERLAY_W, _EXIT_OVERLAY_H
            overlay.move((pw - ow) // 2, (ph - oh) // 2)
            overlay.show()
            overlay.raise_()
            self._exit_overlay = overlay
        except Exception:
            self._exit_overlay = None
        def _on_shutdown_done() -> None:
            overlay_ref = getattr(self, "_exit_overlay", None)
            if overlay_ref is not None:
                overlay_ref.close_ready.connect(self.close)
                overlay_ref.on_shutdown_complete()
            else:
                self.close()
        try:
            self.sentry_v2_tab.begin_graceful_shutdown(on_complete=_on_shutdown_done)
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
    window = SmartSentryV2_3_2StandaloneWindow()
    window.show()
    return app.exec_()


SmartSentryV3StandaloneWindow = SmartSentryV2_3_2StandaloneWindow


if __name__ == "__main__":
    raise SystemExit(main())
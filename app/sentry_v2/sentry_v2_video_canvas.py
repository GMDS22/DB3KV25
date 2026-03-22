from __future__ import annotations

from typing import Optional, Tuple

from PyQt5.QtCore import QPoint, QRect, Qt, pyqtSignal
from PyQt5.QtGui import QMouseEvent, QPixmap
from PyQt5.QtWidgets import QLabel


class SentryV2VideoCanvas(QLabel):
    frameClicked = pyqtSignal(float, float)
    frameRightClicked = pyqtSignal(float, float)

    def __init__(self, text: str = "", parent=None):
        super().__init__(text, parent)
        self._raw_pixmap = QPixmap()
        self._frame_width = 0
        self._frame_height = 0
        self._display_rect = QRect()
        self.setAlignment(Qt.AlignCenter)

    def clear_frame(self, text: str = "Waiting for video...") -> None:
        self._raw_pixmap = QPixmap()
        self._frame_width = 0
        self._frame_height = 0
        self._display_rect = QRect()
        super().setPixmap(QPixmap())
        self.setText(text)

    def set_frame(self, pixmap: QPixmap, frame_width: int, frame_height: int) -> None:
        self._raw_pixmap = QPixmap(pixmap)
        self._frame_width = int(max(1, frame_width))
        self._frame_height = int(max(1, frame_height))
        self.setText("")
        self._apply_scaled_pixmap()

    def frame_point_from_widget_pos(self, pos: QPoint) -> Optional[Tuple[float, float]]:
        if self._display_rect.isNull() or self._frame_width <= 0 or self._frame_height <= 0:
            return None
        if not self._display_rect.contains(pos):
            return None

        rel_x = (pos.x() - self._display_rect.x()) / max(1.0, float(self._display_rect.width()))
        rel_y = (pos.y() - self._display_rect.y()) / max(1.0, float(self._display_rect.height()))
        frame_x = rel_x * float(self._frame_width)
        frame_y = rel_y * float(self._frame_height)
        return frame_x, frame_y

    def widget_point_from_frame_point(self, frame_x: float, frame_y: float) -> Optional[Tuple[float, float]]:
        if self._display_rect.isNull() or self._frame_width <= 0 or self._frame_height <= 0:
            return None
        rel_x = float(frame_x) / max(1.0, float(self._frame_width))
        rel_y = float(frame_y) / max(1.0, float(self._frame_height))
        x = self._display_rect.x() + (rel_x * float(self._display_rect.width()))
        y = self._display_rect.y() + (rel_y * float(self._display_rect.height()))
        return x, y

    def display_rect(self) -> QRect:
        return QRect(self._display_rect)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        if not self._raw_pixmap.isNull():
            self._apply_scaled_pixmap()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        mapped = self.frame_point_from_widget_pos(event.pos())
        if mapped is not None:
            if event.button() == Qt.RightButton:
                self.frameRightClicked.emit(float(mapped[0]), float(mapped[1]))
            else:
                self.frameClicked.emit(float(mapped[0]), float(mapped[1]))
        super().mousePressEvent(event)

    def _apply_scaled_pixmap(self) -> None:
        if self._raw_pixmap.isNull():
            self._display_rect = QRect()
            return

        target = self.size()
        if target.width() <= 0 or target.height() <= 0:
            return

        scaled = self._raw_pixmap.scaled(target, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        x = (target.width() - scaled.width()) // 2
        y = (target.height() - scaled.height()) // 2
        self._display_rect = QRect(x, y, scaled.width(), scaled.height())
        super().setPixmap(scaled)

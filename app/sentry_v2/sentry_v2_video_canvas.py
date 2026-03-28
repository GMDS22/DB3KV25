from __future__ import annotations

from typing import Optional, Tuple

from PyQt5.QtCore import QPoint, QRect, Qt, pyqtSignal
from PyQt5.QtGui import QColor, QMouseEvent, QPainter, QPen, QPixmap
from PyQt5.QtWidgets import QLabel


class SentryV2VideoCanvas(QLabel):
    frameClicked = pyqtSignal(float, float)
    frameRightClicked = pyqtSignal(float, float)
    roiSelected = pyqtSignal(float, float, float, float)

    def __init__(self, text: str = "", parent=None):
        super().__init__(text, parent)
        self._raw_pixmap = QPixmap()
        self._placeholder_pixmap = QPixmap()
        self._placeholder_text = text
        self._placeholder_enabled = False
        self._frame_width = 0
        self._frame_height = 0
        self._display_rect = QRect()
        self._roi_selection_enabled = False
        self._drag_start_pos: Optional[QPoint] = None
        self._drag_current_pos: Optional[QPoint] = None
        self.setAlignment(Qt.AlignCenter)

    def set_roi_selection_enabled(self, enabled: bool) -> None:
        self._roi_selection_enabled = bool(enabled)
        if not enabled:
            self._drag_start_pos = None
            self._drag_current_pos = None
            self.update()

    def set_placeholder_pixmap(self, pixmap: QPixmap) -> None:
        self._placeholder_pixmap = QPixmap(pixmap)
        if self._placeholder_enabled and self._raw_pixmap.isNull():
            self._apply_placeholder_pixmap()

    def set_placeholder_text(self, text: str) -> None:
        self._placeholder_text = str(text or "")
        if self._placeholder_enabled and self._raw_pixmap.isNull() and not self._placeholder_pixmap.isNull():
            self.update()

    def set_placeholder_enabled(self, enabled: bool) -> None:
        self._placeholder_enabled = bool(enabled)
        if self._raw_pixmap.isNull():
            if self._placeholder_enabled and not self._placeholder_pixmap.isNull():
                self.setText("")
                self._apply_placeholder_pixmap()
            else:
                super().setPixmap(QPixmap())
                self._display_rect = QRect()
                if self._placeholder_text:
                    self.setText(self._placeholder_text)

    def clear_frame(self, text: str = "Waiting for video...") -> None:
        self._raw_pixmap = QPixmap()
        self._frame_width = 0
        self._frame_height = 0
        self._display_rect = QRect()
        if self._placeholder_enabled and not self._placeholder_pixmap.isNull():
            if text:
                self._placeholder_text = str(text)
            self.setText("")
            self._apply_placeholder_pixmap()
            return
        super().setPixmap(QPixmap())
        self.setText(text)

    def set_frame(self, pixmap: QPixmap, frame_width: int, frame_height: int) -> None:
        self._placeholder_enabled = False
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
        elif self._placeholder_enabled and not self._placeholder_pixmap.isNull():
            self._apply_placeholder_pixmap()

    def paintEvent(self, event) -> None:
        super().paintEvent(event)
        if self._raw_pixmap.isNull() and self._placeholder_enabled and not self._placeholder_pixmap.isNull() and self._placeholder_text:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.TextAntialiasing, True)
            painter.setPen(QColor(111, 125, 138))
            text_rect = QRect(16, max(0, self.height() - 54), max(0, self.width() - 32), 38)
            painter.drawText(text_rect, Qt.AlignHCenter | Qt.AlignTop | Qt.TextWordWrap, self._placeholder_text)
        if not self._roi_selection_enabled or self._drag_start_pos is None or self._drag_current_pos is None:
            return
        rect = QRect(self._drag_start_pos, self._drag_current_pos).normalized()
        if rect.width() < 2 or rect.height() < 2:
            return
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(QPen(QColor(30, 220, 145), 2))
        painter.drawRect(rect)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if self._roi_selection_enabled and event.button() == Qt.LeftButton:
            mapped = self.frame_point_from_widget_pos(event.pos())
            if mapped is not None:
                self._drag_start_pos = QPoint(event.pos())
                self._drag_current_pos = QPoint(event.pos())
                self.update()
                event.accept()
                return
        mapped = self.frame_point_from_widget_pos(event.pos())
        if mapped is not None:
            if event.button() == Qt.RightButton:
                self.frameRightClicked.emit(float(mapped[0]), float(mapped[1]))
            else:
                self.frameClicked.emit(float(mapped[0]), float(mapped[1]))
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self._roi_selection_enabled and self._drag_start_pos is not None:
            self._drag_current_pos = QPoint(event.pos())
            self.update()
            event.accept()
            return
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if self._roi_selection_enabled and self._drag_start_pos is not None and event.button() == Qt.LeftButton:
            start = self.frame_point_from_widget_pos(self._drag_start_pos)
            end = self.frame_point_from_widget_pos(event.pos())
            self._drag_current_pos = QPoint(event.pos())
            if start is not None and end is not None:
                x1 = min(float(start[0]), float(end[0]))
                y1 = min(float(start[1]), float(end[1]))
                x2 = max(float(start[0]), float(end[0]))
                y2 = max(float(start[1]), float(end[1]))
                width = x2 - x1
                height = y2 - y1
                if width >= 6.0 and height >= 6.0:
                    self.roiSelected.emit(x1, y1, width, height)
            self._drag_start_pos = None
            self._drag_current_pos = None
            self.update()
            event.accept()
            return
        super().mouseReleaseEvent(event)

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

    def _apply_placeholder_pixmap(self) -> None:
        if self._placeholder_pixmap.isNull():
            super().setPixmap(QPixmap())
            return
        target = self.size()
        if target.width() <= 0 or target.height() <= 0:
            return
        pixmap = self._placeholder_pixmap
        if pixmap.width() > target.width() or pixmap.height() > max(1, target.height() - 48):
            scaled = pixmap.scaled(target.width(), max(1, target.height() - 48), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        else:
            scaled = pixmap
        x = (target.width() - scaled.width()) // 2
        y = max(0, ((target.height() - scaled.height()) // 2) - 12)
        self._display_rect = QRect(x, y, scaled.width(), scaled.height())
        super().setPixmap(scaled)

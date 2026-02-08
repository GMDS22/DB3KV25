"""
idle_zones_widget.py
====================
Graphical selector for idle watch zones based on current pan/tilt limits.
"""

from __future__ import annotations

from typing import List, Tuple

from PyQt5.QtCore import Qt, QRectF, pyqtSignal
from PyQt5.QtGui import QColor, QFont, QPainter, QPen
from PyQt5.QtWidgets import QWidget


class IdleZonesWidget(QWidget):
    """Interactive grid that maps pan/tilt limits into selectable zones."""

    zoneSelected = pyqtSignal(int, int, str, float, float)
    selectionChanged = pyqtSignal(list)

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self._pan_min = 0.0
        self._pan_max = 180.0
        self._tilt_min = 0.0
        self._tilt_max = 90.0
        self._pan_divs = 3
        self._tilt_divs = 3
        self._selected_pan = 1
        self._selected_tilt = 1
        self._selected_zones: list[tuple[int, int]] = [(1, 1)]
        self._multi_select_enabled = False
        self.setMinimumSize(280, 200)

    def set_limits(self, pan_min: float, pan_max: float, tilt_min: float, tilt_max: float) -> None:
        self._pan_min = float(pan_min)
        self._pan_max = float(pan_max)
        self._tilt_min = float(tilt_min)
        self._tilt_max = float(tilt_max)
        self.update()

    def set_divisions(self, pan_divs: int, tilt_divs: int) -> None:
        self._pan_divs = max(1, int(pan_divs))
        self._tilt_divs = max(1, int(tilt_divs))
        self._selected_pan = max(0, min(self._selected_pan, self._pan_divs - 1))
        self._selected_tilt = max(0, min(self._selected_tilt, self._tilt_divs - 1))
        self._selected_zones = [
            (p, t)
            for (p, t) in self._selected_zones
            if 0 <= p < self._pan_divs and 0 <= t < self._tilt_divs
        ]
        if not self._selected_zones:
            self._selected_zones = [(self._selected_pan, self._selected_tilt)]
        self.update()

    def set_multi_select(self, enabled: bool) -> None:
        self._multi_select_enabled = bool(enabled)

    def set_selected_zone(self, pan_index: int, tilt_index: int, emit: bool = False) -> None:
        self._selected_pan = max(0, min(int(pan_index), self._pan_divs - 1))
        self._selected_tilt = max(0, min(int(tilt_index), self._tilt_divs - 1))
        self._selected_zones = [(self._selected_pan, self._selected_tilt)]
        self.update()
        if emit:
            label = self.get_zone_label(self._selected_pan, self._selected_tilt)
            center_pan, center_tilt = self.get_zone_center(self._selected_pan, self._selected_tilt)
            self.zoneSelected.emit(self._selected_pan, self._selected_tilt, label, center_pan, center_tilt)
            self.selectionChanged.emit(list(self._selected_zones))

    def set_selected_zones(self, zones: list[tuple[int, int]], emit: bool = False) -> None:
        filtered = [
            (int(p), int(t))
            for (p, t) in zones
            if 0 <= int(p) < self._pan_divs and 0 <= int(t) < self._tilt_divs
        ]
        self._selected_zones = filtered or [(self._selected_pan, self._selected_tilt)]
        self._selected_pan, self._selected_tilt = self._selected_zones[-1]
        self.update()
        if emit:
            self.selectionChanged.emit(list(self._selected_zones))

    def get_selected_zone(self) -> Tuple[int, int]:
        return self._selected_pan, self._selected_tilt

    def get_selected_zones(self) -> List[Tuple[int, int]]:
        return list(self._selected_zones)

    def get_zone_center(self, pan_index: int, tilt_index: int) -> Tuple[float, float]:
        pan_step = (self._pan_max - self._pan_min) / float(max(1, self._pan_divs))
        tilt_step = (self._tilt_max - self._tilt_min) / float(max(1, self._tilt_divs))
        center_pan = self._pan_min + pan_step * (pan_index + 0.5)
        center_tilt = self._tilt_min + tilt_step * (tilt_index + 0.5)
        return center_pan, center_tilt

    def get_zone_label(self, pan_index: int, tilt_index: int) -> str:
        pan_labels = self._pan_labels()
        tilt_labels = self._tilt_labels()
        pan_label = pan_labels[pan_index] if pan_index < len(pan_labels) else f"P{pan_index + 1}"
        tilt_label = tilt_labels[tilt_index] if tilt_index < len(tilt_labels) else f"T{tilt_index + 1}"
        return f"{tilt_label} {pan_label}"

    def mousePressEvent(self, event):
        if event.button() != Qt.LeftButton:
            return
        rect = self._grid_rect()
        if rect.width() <= 0 or rect.height() <= 0:
            return
        if not rect.contains(event.pos()):
            return
        cell_w = rect.width() / float(max(1, self._pan_divs))
        cell_h = rect.height() / float(max(1, self._tilt_divs))
        pan_idx = int((event.x() - rect.left()) / cell_w)
        tilt_idx = int((event.y() - rect.top()) / cell_h)
        pan_idx = max(0, min(pan_idx, self._pan_divs - 1))
        tilt_idx = max(0, min(tilt_idx, self._tilt_divs - 1))
        multi = self._multi_select_enabled or bool(event.modifiers() & (Qt.ControlModifier | Qt.ShiftModifier))
        if multi:
            zone = (pan_idx, tilt_idx)
            if zone in self._selected_zones:
                self._selected_zones = [z for z in self._selected_zones if z != zone]
                if not self._selected_zones:
                    self._selected_zones = [(pan_idx, tilt_idx)]
            else:
                self._selected_zones.append(zone)
            self._selected_pan, self._selected_tilt = self._selected_zones[-1]
            self.update()
            label = self.get_zone_label(self._selected_pan, self._selected_tilt)
            center_pan, center_tilt = self.get_zone_center(self._selected_pan, self._selected_tilt)
            self.zoneSelected.emit(self._selected_pan, self._selected_tilt, label, center_pan, center_tilt)
            self.selectionChanged.emit(list(self._selected_zones))
        else:
            self.set_selected_zone(pan_idx, tilt_idx, emit=True)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), QColor(30, 30, 30))

        rect = self._grid_rect()
        if rect.width() <= 0 or rect.height() <= 0:
            return

        border_pen = QPen(QColor(90, 90, 90), 2)
        painter.setPen(border_pen)
        painter.drawRect(rect)

        cell_w = rect.width() / float(max(1, self._pan_divs))
        cell_h = rect.height() / float(max(1, self._tilt_divs))

        grid_pen = QPen(QColor(70, 70, 70), 1)
        painter.setPen(grid_pen)
        for i in range(1, self._pan_divs):
            x = rect.left() + cell_w * i
            painter.drawLine(int(x), int(rect.top()), int(x), int(rect.bottom()))
        for j in range(1, self._tilt_divs):
            y = rect.top() + cell_h * j
            painter.drawLine(int(rect.left()), int(y), int(rect.right()), int(y))

        # Highlight selected zone
        painter.setPen(QPen(QColor(0, 180, 255), 2))
        for pan_idx, tilt_idx in self._selected_zones:
            sel_rect = QRectF(
                rect.left() + cell_w * pan_idx,
                rect.top() + cell_h * tilt_idx,
                cell_w,
                cell_h,
            )
            painter.fillRect(sel_rect, QColor(0, 180, 255, 60))
            painter.drawRect(sel_rect)

        # Labels
        painter.setPen(QPen(QColor(220, 220, 220)))
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        painter.setFont(font)

        pan_labels = self._pan_labels()
        tilt_labels = self._tilt_labels()
        for row in range(self._tilt_divs):
            for col in range(self._pan_divs):
                label = f"{tilt_labels[row]}\n{pan_labels[col]}" if row < len(tilt_labels) and col < len(pan_labels) else f"{row + 1},{col + 1}"
                cell = QRectF(
                    rect.left() + cell_w * col,
                    rect.top() + cell_h * row,
                    cell_w,
                    cell_h,
                )
                painter.drawText(cell, Qt.AlignCenter, label)

        # Axis labels
        painter.setPen(QPen(QColor(150, 150, 150)))
        axis_font = QFont()
        axis_font.setPointSize(8)
        painter.setFont(axis_font)
        painter.drawText(
            QRectF(rect.left(), rect.bottom() + 4, rect.width(), 16),
            Qt.AlignCenter,
            f"PAN: {self._pan_min:.0f}° → {self._pan_max:.0f}°",
        )
        painter.save()
        painter.translate(10, rect.top() + rect.height() / 2)
        painter.rotate(-90)
        painter.drawText(
            QRectF(-rect.height() / 2, -20, rect.height(), 16),
            Qt.AlignCenter,
            f"TILT: {self._tilt_min:.0f}° → {self._tilt_max:.0f}°",
        )
        painter.restore()

    def _grid_rect(self) -> QRectF:
        margin = 30
        return QRectF(
            margin,
            margin,
            max(0.0, float(self.width() - margin * 2)),
            max(0.0, float(self.height() - margin * 2 - 18)),
        )

    def _pan_labels(self) -> List[str]:
        if self._pan_divs == 3:
            return ["Left", "Center", "Right"]
        if self._pan_divs == 4:
            return ["Far Left", "Left", "Right", "Far Right"]
        return [f"P{idx + 1}" for idx in range(self._pan_divs)]

    def _tilt_labels(self) -> List[str]:
        if self._tilt_divs == 2:
            return ["Top", "Bottom"]
        if self._tilt_divs == 3:
            return ["Top", "Mid", "Bottom"]
        return [f"T{idx + 1}" for idx in range(self._tilt_divs)]

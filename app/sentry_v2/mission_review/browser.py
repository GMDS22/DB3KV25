from __future__ import annotations

import json
import time
from pathlib import Path
from typing import List, Optional

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QComboBox,
    QHBoxLayout,
    QHeaderView,
    QInputDialog,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from .exporter import export_complete_package
from .repository import MissionRepository, MissionSummary
from .review_window import MissionReviewWindow


def _fmt_ts(value: float) -> str:
    if float(value or 0.0) <= 0.0:
        return ""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(value)))


def _fmt_size(size_bytes: int) -> str:
    size = float(size_bytes or 0)
    units = ["B", "KB", "MB", "GB"]
    idx = 0
    while size >= 1024.0 and idx < len(units) - 1:
        size /= 1024.0
        idx += 1
    return f"{size:.2f} {units[idx]}"


class MissionBrowserWindow(QWidget):
    def __init__(self, repo: Optional[MissionRepository] = None, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.repo = repo or MissionRepository()
        self.setWindowTitle("Mission Browser")
        self.setMinimumSize(1320, 760)
        self._missions: List[MissionSummary] = []
        self._review_windows: List[MissionReviewWindow] = []
        self._build_ui()
        self.refresh()

    def _build_ui(self) -> None:
        root = QVBoxLayout(self)

        controls = QHBoxLayout()
        controls.addWidget(QLabel("Search"))
        self._edit_search = QLineEdit()
        self._edit_search.setPlaceholderText("Search mission/profile/model/id")
        self._edit_search.textChanged.connect(self._render_table)
        controls.addWidget(self._edit_search, 1)

        self._combo_filter = QComboBox()
        self._combo_filter.addItems(["all", "bookmarked", "with_notes", "without_notes"])
        self._combo_filter.currentTextChanged.connect(self._render_table)
        controls.addWidget(self._combo_filter)

        self._btn_open = QPushButton("Open")
        self._btn_delete = QPushButton("Delete")
        self._btn_duplicate = QPushButton("Duplicate")
        self._btn_export = QPushButton("Export")
        self._btn_rename = QPushButton("Rename")
        self._btn_refresh = QPushButton("Refresh")
        self._btn_open.clicked.connect(self.open_selected)
        self._btn_delete.clicked.connect(self.delete_selected)
        self._btn_duplicate.clicked.connect(self.duplicate_selected)
        self._btn_export.clicked.connect(self.export_selected)
        self._btn_rename.clicked.connect(self.rename_selected)
        self._btn_refresh.clicked.connect(self.refresh)
        for btn in [self._btn_open, self._btn_delete, self._btn_duplicate, self._btn_export, self._btn_rename, self._btn_refresh]:
            controls.addWidget(btn)

        root.addLayout(controls)

        self._table = QTableWidget(0, 14)
        self._table.setHorizontalHeaderLabels(
            [
                "Mission Name",
                "Mission ID",
                "Start Time",
                "End Time",
                "Duration (s)",
                "Active Profile",
                "Detection Model",
                "Events",
                "Detections",
                "Engagements",
                "Shots",
                "Mission Size",
                "Notes",
                "Bookmark",
            ]
        )
        self._table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self._table.setSelectionMode(QAbstractItemView.SingleSelection)
        self._table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self._table.setSortingEnabled(True)
        self._table.doubleClicked.connect(lambda _idx: self.open_selected())
        header = self._table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        root.addWidget(self._table, 1)

    def refresh(self) -> None:
        self._missions = self.repo.load_missions()
        self._render_table()

    def _render_table(self) -> None:
        query = self._edit_search.text().strip().lower()
        filter_mode = self._combo_filter.currentText().strip().lower()
        rows = []
        for mission in self._missions:
            if filter_mode == "bookmarked" and not mission.bookmarked:
                continue
            if filter_mode == "with_notes" and not mission.has_notes:
                continue
            if filter_mode == "without_notes" and mission.has_notes:
                continue
            if query:
                blob = " ".join(
                    [
                        mission.mission_name,
                        mission.mission_id,
                        mission.active_profile,
                        mission.detection_model,
                    ]
                ).lower()
                if query not in blob:
                    continue
            rows.append(mission)

        self._table.setSortingEnabled(False)
        self._table.setRowCount(len(rows))
        for r, m in enumerate(rows):
            values = [
                m.mission_name,
                m.mission_id,
                _fmt_ts(m.start_time),
                _fmt_ts(m.end_time),
                f"{m.duration_s:.3f}",
                m.active_profile,
                m.detection_model,
                str(m.events_count),
                str(m.detections_count),
                str(m.engagements_count),
                str(m.shots_fired),
                _fmt_size(m.mission_size_bytes),
                "yes" if m.has_notes else "",
                "yes" if m.bookmarked else "",
            ]
            for c, value in enumerate(values):
                item = QTableWidgetItem(value)
                if c >= 7:
                    item.setTextAlignment(Qt.AlignCenter)
                self._table.setItem(r, c, item)
            self._table.item(r, 0).setData(Qt.UserRole, m.mission_id)
        self._table.setSortingEnabled(True)

    def _selected_mission_id(self) -> str:
        row = self._table.currentRow()
        if row < 0:
            return ""
        item = self._table.item(row, 0)
        if item is None:
            return ""
        return str(item.data(Qt.UserRole) or "")

    def open_selected(self) -> None:
        mission_id = self._selected_mission_id()
        if not mission_id:
            return
        review = MissionReviewWindow(self.repo, mission_id)
        review.setAttribute(Qt.WA_DeleteOnClose, True)
        review.show()
        self._review_windows.append(review)

    def delete_selected(self) -> None:
        mission_id = self._selected_mission_id()
        if not mission_id:
            return
        resp = QMessageBox.question(self, "Delete Mission", f"Delete mission {mission_id}? This cannot be undone.")
        if resp != QMessageBox.Yes:
            return
        self.repo.delete_mission(mission_id)
        self.refresh()

    def duplicate_selected(self) -> None:
        mission_id = self._selected_mission_id()
        if not mission_id:
            return
        try:
            new_id = self.repo.duplicate_mission(mission_id)
        except Exception as exc:
            QMessageBox.critical(self, "Duplicate Failed", str(exc))
            return
        QMessageBox.information(self, "Mission Duplicated", f"Created {new_id}")
        self.refresh()

    def rename_selected(self) -> None:
        mission_id = self._selected_mission_id()
        if not mission_id:
            return
        text, ok = QInputDialog.getText(self, "Rename Mission", "Mission name")
        if not ok:
            return
        self.repo.rename_mission(mission_id, str(text or ""))
        self.refresh()

    def export_selected(self) -> None:
        mission_id = self._selected_mission_id()
        if not mission_id:
            return
        output_dir = self.repo.archive_root / mission_id / "exports"
        try:
            result = export_complete_package(self.repo, mission_id, output_dir)
        except Exception as exc:
            QMessageBox.critical(self, "Export Failed", str(exc))
            return
        QMessageBox.information(self, "Export Complete", json.dumps(result, ensure_ascii=True, indent=2))

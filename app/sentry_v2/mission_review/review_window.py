from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import cv2
from PyQt5.QtCore import QAbstractListModel, QModelIndex, QPoint, QRectF, Qt, QSortFilterProxyModel
from PyQt5.QtGui import QColor, QImage, QPixmap
from PyQt5.QtWidgets import (
    QCheckBox,
    QComboBox,
    QFormLayout,
    QGraphicsPixmapItem,
    QGraphicsScene,
    QGraphicsView,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListView,
    QMessageBox,
    QPushButton,
    QPlainTextEdit,
    QSplitter,
    QTabWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from .annotations import event_annotation, normalize_annotations, set_event_annotation
from .exporter import export_complete_package
from .repository import MissionEvent, MissionRepository
from .statistics import compute_mission_statistics


class MissionEventListModel(QAbstractListModel):
    def __init__(self, archive_root: Path, events: Optional[List[MissionEvent]] = None):
        super().__init__()
        self._archive_root = Path(archive_root)
        self._events: List[MissionEvent] = list(events or [])
        self._thumb_cache: Dict[str, QPixmap] = {}

    def set_events(self, events: List[MissionEvent]) -> None:
        self.beginResetModel()
        self._events = list(events)
        self._thumb_cache = {}
        self.endResetModel()

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        if parent.isValid():
            return 0
        return len(self._events)

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):
        if not index.isValid() or index.row() < 0 or index.row() >= len(self._events):
            return None
        event = self._events[index.row()]
        if role == Qt.DisplayRole:
            return (
                f"{event.sequence:06d}  t={event.occurred_at:.3f}  frame={event.frame_number}  "
                f"{event.category}:{event.event_type}  id={event.tracker_id}  class={event.object_class}  "
                f"conf={event.confidence:.3f}  threat={event.threat_score:.3f}"
            )
        if role == Qt.DecorationRole:
            media_refs = list(event.media_refs or [])
            if not media_refs:
                return None
            rel = str(media_refs[0])
            if rel in self._thumb_cache:
                return self._thumb_cache[rel]
            path = self._archive_root / rel
            if not path.exists():
                return None
            pix = QPixmap(str(path))
            if pix.isNull():
                return None
            thumb = pix.scaled(84, 52, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self._thumb_cache[rel] = thumb
            return thumb
        if role == Qt.BackgroundRole:
            if event.severity in {"error", "critical"}:
                return QColor("#401010")
            if event.category == "engagement":
                return QColor("#203020")
            if event.category == "planner":
                return QColor("#202030")
            if event.category == "tracking":
                return QColor("#202020")
        if role == Qt.UserRole:
            return event
        return None


class MissionEventFilterProxy(QSortFilterProxyModel):
    def __init__(self):
        super().__init__()
        self._query = ""
        self._category = "all"
        self._event_type = "all"
        self._tracker = ""
        self._object_class = ""
        self._decision = ""
        self._planner_state = ""
        self._motion_policy_state = ""
        self._safety_state = ""

    def set_filters(
        self,
        *,
        query: str,
        category: str,
        event_type: str,
        tracker: str,
        object_class: str,
        decision: str,
        planner_state: str,
        motion_policy_state: str,
        safety_state: str,
    ) -> None:
        self._query = str(query or "").strip().lower()
        self._category = str(category or "all").strip().lower()
        self._event_type = str(event_type or "all").strip().lower()
        self._tracker = str(tracker or "").strip().lower()
        self._object_class = str(object_class or "").strip().lower()
        self._decision = str(decision or "").strip().lower()
        self._planner_state = str(planner_state or "").strip().lower()
        self._motion_policy_state = str(motion_policy_state or "").strip().lower()
        self._safety_state = str(safety_state or "").strip().lower()
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row: int, source_parent: QModelIndex) -> bool:
        index = self.sourceModel().index(source_row, 0, source_parent)
        event = self.sourceModel().data(index, Qt.UserRole)
        if event is None:
            return False

        if self._category != "all" and str(event.category).lower() != self._category:
            return False
        if self._event_type != "all" and str(event.event_type).lower() != self._event_type:
            return False
        if self._tracker and self._tracker not in str(event.tracker_id).lower():
            return False
        if self._object_class and self._object_class not in str(event.object_class).lower():
            return False
        if self._decision and self._decision not in str(event.decision).lower():
            return False
        if self._planner_state and self._planner_state not in str(event.planner_state).lower():
            return False
        if self._motion_policy_state and self._motion_policy_state not in str(event.motion_policy_state).lower():
            return False
        if self._safety_state and self._safety_state not in str(event.safety_state).lower():
            return False

        if self._query:
            blob = " ".join(
                [
                    str(event.event_type),
                    str(event.category),
                    str(event.source),
                    str(event.object_class),
                    str(event.decision),
                    str(event.planner_state),
                    str(event.motion_policy_state),
                    str(event.safety_state),
                    json.dumps(event.data, ensure_ascii=True),
                ]
            ).lower()
            if self._query not in blob:
                return False

        return True


class SnapshotViewer(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self._scene = QGraphicsScene(self)
        self.setScene(self._scene)
        self._pixmap_item = QGraphicsPixmapItem()
        self._scene.addItem(self._pixmap_item)
        self._scale = 1.0

    def set_pixmap(self, pixmap: QPixmap) -> None:
        self._pixmap_item.setPixmap(pixmap)
        self._scene.setSceneRect(QRectF(pixmap.rect()))

    def fit_to_window(self) -> None:
        if self._pixmap_item.pixmap().isNull():
            return
        self.fitInView(self._pixmap_item, Qt.KeepAspectRatio)
        self._scale = 1.0

    def original_size(self) -> None:
        self.resetTransform()
        self._scale = 1.0

    def zoom(self, factor: float) -> None:
        self._scale *= float(factor)
        self.scale(float(factor), float(factor))


class MissionReviewWindow(QWidget):
    def __init__(self, repo: MissionRepository, mission_id: str, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self.setWindowTitle(f"Mission Review - {mission_id}")
        self.setMinimumSize(1260, 820)
        self.repo = repo
        self.mission_id = mission_id
        self.manifest = self.repo.load_manifest(mission_id)
        self.annotations = normalize_annotations(self.repo.load_annotations(mission_id))
        self.events = self.repo.load_mission_events(mission_id)
        self.stats = compute_mission_statistics(self.events)
        self._current_event: Optional[MissionEvent] = None

        self._model = MissionEventListModel(self.repo.archive_root, self.events)
        self._proxy = MissionEventFilterProxy()
        self._proxy.setSourceModel(self._model)

        self._build_ui()
        self._refresh_stats_panel()
        self._reload_filter_options()

    def _build_ui(self) -> None:
        root = QVBoxLayout(self)

        actions = QHBoxLayout()
        self._btn_export = QPushButton("Export Complete Mission Package")
        self._btn_export.clicked.connect(self._export_mission)
        actions.addWidget(self._btn_export)
        actions.addStretch(1)
        root.addLayout(actions)

        split = QSplitter(Qt.Horizontal)
        root.addWidget(split, 1)

        # Left: timeline + filters
        left = QWidget()
        left_lay = QVBoxLayout(left)
        self._edit_search = QLineEdit()
        self._edit_search.setPlaceholderText("Search mission/timestamp/frame/tracker/class/decision/planner/motion/safety/keyword")
        self._edit_search.textChanged.connect(self._apply_event_filters)
        left_lay.addWidget(self._edit_search)

        filter_row1 = QHBoxLayout()
        self._combo_category = QComboBox()
        self._combo_event_type = QComboBox()
        self._combo_category.currentTextChanged.connect(self._apply_event_filters)
        self._combo_event_type.currentTextChanged.connect(self._apply_event_filters)
        filter_row1.addWidget(QLabel("Category"))
        filter_row1.addWidget(self._combo_category)
        filter_row1.addWidget(QLabel("Event Type"))
        filter_row1.addWidget(self._combo_event_type)
        left_lay.addLayout(filter_row1)

        filter_row2 = QHBoxLayout()
        self._edit_tracker = QLineEdit()
        self._edit_class = QLineEdit()
        self._edit_decision = QLineEdit()
        self._edit_tracker.setPlaceholderText("Tracker ID")
        self._edit_class.setPlaceholderText("Class")
        self._edit_decision.setPlaceholderText("Decision")
        self._edit_tracker.textChanged.connect(self._apply_event_filters)
        self._edit_class.textChanged.connect(self._apply_event_filters)
        self._edit_decision.textChanged.connect(self._apply_event_filters)
        filter_row2.addWidget(self._edit_tracker)
        filter_row2.addWidget(self._edit_class)
        filter_row2.addWidget(self._edit_decision)
        left_lay.addLayout(filter_row2)

        filter_row3 = QHBoxLayout()
        self._edit_planner_state = QLineEdit()
        self._edit_motion_state = QLineEdit()
        self._edit_safety_state = QLineEdit()
        self._edit_planner_state.setPlaceholderText("Planner state")
        self._edit_motion_state.setPlaceholderText("Motion policy state")
        self._edit_safety_state.setPlaceholderText("Safety state")
        self._edit_planner_state.textChanged.connect(self._apply_event_filters)
        self._edit_motion_state.textChanged.connect(self._apply_event_filters)
        self._edit_safety_state.textChanged.connect(self._apply_event_filters)
        filter_row3.addWidget(self._edit_planner_state)
        filter_row3.addWidget(self._edit_motion_state)
        filter_row3.addWidget(self._edit_safety_state)
        left_lay.addLayout(filter_row3)

        self._timeline = QListView()
        self._timeline.setModel(self._proxy)
        self._timeline.clicked.connect(self._on_event_selected)
        left_lay.addWidget(self._timeline, 1)

        split.addWidget(left)

        # Center: snapshot viewer
        center = QWidget()
        center_lay = QVBoxLayout(center)
        toolbar = QHBoxLayout()
        self._btn_zoom_in = QPushButton("+")
        self._btn_zoom_out = QPushButton("-")
        self._btn_fit = QPushButton("Fit")
        self._btn_orig = QPushButton("Original")
        self._combo_render = QComboBox()
        self._combo_render.addItems(["Annotated", "Raw"])
        self._viewer = SnapshotViewer()
        self._combo_render.currentTextChanged.connect(self._refresh_snapshot)
        self._btn_zoom_in.clicked.connect(lambda: self._viewer.zoom(1.2))
        self._btn_zoom_out.clicked.connect(lambda: self._viewer.zoom(1.0 / 1.2))
        self._btn_fit.clicked.connect(self._viewer.fit_to_window)
        self._btn_orig.clicked.connect(self._viewer.original_size)
        toolbar.addWidget(self._btn_zoom_in)
        toolbar.addWidget(self._btn_zoom_out)
        toolbar.addWidget(self._btn_fit)
        toolbar.addWidget(self._btn_orig)
        toolbar.addWidget(QLabel("Render"))
        toolbar.addWidget(self._combo_render)
        toolbar.addStretch(1)
        center_lay.addLayout(toolbar)

        overlay_row = QHBoxLayout()
        self._chk_bbox = QCheckBox("Bounding boxes")
        self._chk_labels = QCheckBox("Labels")
        self._chk_conf = QCheckBox("Confidence")
        self._chk_tid = QCheckBox("Tracker IDs")
        self._chk_vectors = QCheckBox("Motion vectors")
        self._chk_cross = QCheckBox("Crosshair")
        self._chk_zones = QCheckBox("Detection zones")
        self._chk_no_fire = QCheckBox("No-fire zones")
        self._chk_current = QCheckBox("Current target")
        self._chk_other = QCheckBox("Other tracked objects")
        for box in [
            self._chk_bbox,
            self._chk_labels,
            self._chk_conf,
            self._chk_tid,
            self._chk_vectors,
            self._chk_cross,
            self._chk_zones,
            self._chk_no_fire,
            self._chk_current,
            self._chk_other,
        ]:
            box.setChecked(True)
            box.stateChanged.connect(self._refresh_snapshot)
            overlay_row.addWidget(box)
        overlay_row.addStretch(1)
        center_lay.addLayout(overlay_row)

        center_lay.addWidget(self._viewer, 1)
        split.addWidget(center)

        # Right: inspector / stats / annotations
        right = QTabWidget()

        inspector_page = QWidget()
        inspector_lay = QVBoxLayout(inspector_page)
        self._txt_inspector = QTextEdit()
        self._txt_inspector.setReadOnly(True)
        inspector_lay.addWidget(self._txt_inspector)
        right.addTab(inspector_page, "Event Inspector")

        stats_page = QWidget()
        stats_lay = QVBoxLayout(stats_page)
        self._txt_stats = QTextEdit()
        self._txt_stats.setReadOnly(True)
        stats_lay.addWidget(self._txt_stats)
        right.addTab(stats_page, "Mission Statistics")

        annotate_page = QWidget()
        annotate_lay = QVBoxLayout(annotate_page)
        form = QFormLayout()
        self._chk_event_bookmark = QCheckBox("Bookmarked")
        self._edit_event_labels = QLineEdit()
        self._edit_event_labels.setPlaceholderText("false_engagement,false_positive,confirmed_engagement")
        self._edit_event_tags = QLineEdit()
        self._edit_event_tags.setPlaceholderText("custom tags comma separated")
        self._edit_event_flags = QLineEdit()
        self._edit_event_flags.setPlaceholderText("flags comma separated")
        self._edit_event_note = QPlainTextEdit()
        form.addRow("Bookmark", self._chk_event_bookmark)
        form.addRow("Labels", self._edit_event_labels)
        form.addRow("Tags", self._edit_event_tags)
        form.addRow("Flags", self._edit_event_flags)
        form.addRow("Note", self._edit_event_note)
        annotate_lay.addLayout(form)
        self._btn_save_annotation = QPushButton("Save Annotation")
        self._btn_save_annotation.clicked.connect(self._save_selected_event_annotation)
        annotate_lay.addWidget(self._btn_save_annotation)
        annotate_lay.addStretch(1)
        right.addTab(annotate_page, "Annotations")

        split.addWidget(right)
        split.setSizes([460, 520, 380])

    def _reload_filter_options(self) -> None:
        categories = sorted({e.category for e in self.events})
        types = sorted({e.event_type for e in self.events})
        self._combo_category.clear()
        self._combo_category.addItem("all")
        self._combo_category.addItems(categories)
        self._combo_event_type.clear()
        self._combo_event_type.addItem("all")
        self._combo_event_type.addItems(types)

    def _apply_event_filters(self) -> None:
        self._proxy.set_filters(
            query=self._edit_search.text(),
            category=self._combo_category.currentText(),
            event_type=self._combo_event_type.currentText(),
            tracker=self._edit_tracker.text(),
            object_class=self._edit_class.text(),
            decision=self._edit_decision.text(),
            planner_state=self._edit_planner_state.text(),
            motion_policy_state=self._edit_motion_state.text(),
            safety_state=self._edit_safety_state.text(),
        )

    def _on_event_selected(self, proxy_index: QModelIndex) -> None:
        source_index = self._proxy.mapToSource(proxy_index)
        event = self._model.data(source_index, Qt.UserRole)
        if event is None:
            return
        self._current_event = event
        self._refresh_inspector(event)
        self._refresh_snapshot()
        self._load_event_annotation(event)

    def _refresh_inspector(self, event: MissionEvent) -> None:
        data = dict(event.data or {})
        category = event.category
        details: Dict[str, Any] = {
            "event_id": event.event_id,
            "sequence": event.sequence,
            "timestamp": event.occurred_at,
            "frame_number": event.frame_number,
            "event_type": event.event_type,
            "category": event.category,
            "tracker_id": event.tracker_id,
            "object_class": event.object_class,
            "decision": event.decision,
            "confidence": event.confidence,
            "threat_score": event.threat_score,
            "planner_state": event.planner_state,
            "motion_policy_state": event.motion_policy_state,
            "safety_state": event.safety_state,
        }

        if category == "detection":
            details["detection_metrics"] = {
                "bbox": data.get("bbox"),
                "shape_profile": data.get("shape_profile_used", ""),
                "shape_score": data.get("shape_score", 0.0),
            }
        elif category == "tracking":
            details["tracking_metrics"] = {
                "motion_history": data.get("history", []),
                "velocity": data.get("target_velocity", {}),
                "motion_confidence": data.get("motion_confidence", 0.0),
                "stationary_duration_s": data.get("stationary_duration_s", 0.0),
            }
        elif category == "planner":
            details["planner_metrics"] = {
                "ranking": data.get("ranking", []),
                "selection_reason": data.get("selection_reason", ""),
                "suppression_reason": data.get("suppression_reason", ""),
            }
        elif category == "engagement":
            details["engagement_metrics"] = {
                "qualification_stages": data.get("qualification_stages", []),
                "fire_authorization": data.get("firing_approved", False),
                "rejection_reason": data.get("firing_rejected_reason", ""),
                "burst_count": data.get("burst_count", 1),
            }
        elif category == "fire":
            qualification_stages = list(data.get("qualification_stages", []) or [])
            hold_stage = next((s for s in qualification_stages if str(s.get("stage", "")) == "hold_time"), {})
            refractory_stage = next((s for s in qualification_stages if str(s.get("stage", "")) == "refractory_period"), {})
            fire_approved = bool(data.get("firing_approved", data.get("fire_approved", False)))
            details["fire_metrics"] = {
                "fire_timestamp": data.get("fire_timestamp", data.get("timestamp", event.occurred_at)),
                "burst_number": data.get("burst_number", data.get("burst_count", 1)),
                "burst_index": data.get("burst_index", data.get("burst_idx", 0)),
                "fire_mode": data.get("fire_mode", data.get("attempt_type", "")),
                "trigger_source": data.get("trigger_source", data.get("attempt_type", "")),
                "auto_manual_trigger_state": data.get(
                    "auto_manual_trigger_state",
                    "auto" if bool(data.get("auto_trigger_enabled", True)) else "manual",
                ),
                "authorization_chain": data.get("authorization_chain", qualification_stages),
                "hold_time_result": data.get("hold_time_result", hold_stage.get("reason", "")),
                "refractory_state": data.get(
                    "refractory_state",
                    {
                        "active": bool(not refractory_stage.get("pass", True)),
                        "reason": refractory_stage.get("reason", ""),
                    },
                ),
                "safety_state": data.get("safety_state", event.safety_state),
                "motion_policy_state": data.get("motion_policy_state", event.motion_policy_state),
                "final_fire_approval": fire_approved,
                "final_veto_reason": data.get("firing_rejected_reason", data.get("fire_veto_reason", "")),
                "actuator_command_issued": data.get("actuator_command_issued", fire_approved),
                "fire_completion_state": data.get(
                    "fire_completion_state",
                    "completed" if fire_approved else "rejected",
                ),
            }
        else:
            details["system"] = data

        self._txt_inspector.setPlainText(json.dumps(details, ensure_ascii=True, indent=2))

    def _refresh_stats_panel(self) -> None:
        self._txt_stats.setPlainText(json.dumps(self.stats, ensure_ascii=True, indent=2))

    def _load_event_annotation(self, event: MissionEvent) -> None:
        ann = event_annotation(self.annotations, event.event_id)
        self._chk_event_bookmark.setChecked(bool(ann.get("bookmarked", False)))
        self._edit_event_labels.setText(",".join(list(ann.get("labels") or [])))
        self._edit_event_tags.setText(",".join(list(ann.get("tags") or [])))
        self._edit_event_flags.setText(",".join(list(ann.get("flags") or [])))
        self._edit_event_note.setPlainText(str(ann.get("note", "") or ""))

    def _save_selected_event_annotation(self) -> None:
        event = self._current_event
        if event is None:
            return
        labels = [s.strip() for s in self._edit_event_labels.text().split(",") if s.strip()]
        tags = [s.strip() for s in self._edit_event_tags.text().split(",") if s.strip()]
        flags = [s.strip() for s in self._edit_event_flags.text().split(",") if s.strip()]
        self.annotations = set_event_annotation(
            self.annotations,
            event.event_id,
            note=self._edit_event_note.toPlainText(),
            bookmarked=bool(self._chk_event_bookmark.isChecked()),
            labels=labels,
            tags=tags,
            flags=flags,
        )
        self.repo.save_annotations(self.mission_id, self.annotations)

    def _event_snapshot_path(self, event: MissionEvent) -> Optional[Path]:
        media_refs = list(event.media_refs or [])
        if not media_refs:
            return None
        ref = media_refs[0]
        candidate = self.repo.archive_root / ref
        if candidate.exists():
            return candidate
        return None

    def _refresh_snapshot(self) -> None:
        event = self._current_event
        if event is None:
            self._viewer.set_pixmap(QPixmap())
            return

        path = self._event_snapshot_path(event)
        if path is None or not path.exists():
            self._viewer.set_pixmap(QPixmap())
            return

        raw = cv2.imread(str(path))
        if raw is None:
            self._viewer.set_pixmap(QPixmap())
            return

        use_annotated = self._combo_render.currentText().strip().lower() == "annotated"
        if use_annotated:
            frame = raw.copy()
            bbox = event.data.get("bbox")
            if isinstance(bbox, list) and len(bbox) == 4 and self._chk_bbox.isChecked():
                x, y, w, h = [int(v) for v in bbox]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (40, 220, 90), 2, cv2.LINE_AA)
                label_parts = []
                if self._chk_labels.isChecked():
                    label_parts.append(str(event.object_class or ""))
                if self._chk_tid.isChecked():
                    label_parts.append(f"id={event.tracker_id}")
                if self._chk_conf.isChecked():
                    label_parts.append(f"conf={event.confidence:.2f}")
                label = " ".join(part for part in label_parts if part)
                if label:
                    cv2.putText(frame, label, (x, max(18, y - 6)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (15, 15, 15), 2, cv2.LINE_AA)
                    cv2.putText(frame, label, (x, max(18, y - 6)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (230, 230, 230), 1, cv2.LINE_AA)
            if self._chk_cross.isChecked():
                h, w = frame.shape[:2]
                cv2.line(frame, (w // 2, 0), (w // 2, h), (180, 180, 180), 1, cv2.LINE_AA)
                cv2.line(frame, (0, h // 2), (w, h // 2), (180, 180, 180), 1, cv2.LINE_AA)
            if self._chk_vectors.isChecked():
                vel = event.data.get("target_velocity")
                if isinstance(vel, dict) and isinstance(bbox, list) and len(bbox) == 4:
                    vx = float(vel.get("vx", 0.0) or 0.0)
                    vy = float(vel.get("vy", 0.0) or 0.0)
                    x, y, w, h = [int(v) for v in bbox]
                    cx = x + w // 2
                    cy = y + h // 2
                    ex = int(cx + (vx * 120.0))
                    ey = int(cy + (vy * 120.0))
                    cv2.arrowedLine(frame, (cx, cy), (ex, ey), (255, 210, 80), 2, cv2.LINE_AA, tipLength=0.2)
            if self._chk_zones.isChecked():
                cv2.rectangle(frame, (int(frame.shape[1] * 0.05), int(frame.shape[0] * 0.05)), (int(frame.shape[1] * 0.95), int(frame.shape[0] * 0.95)), (90, 120, 220), 1, cv2.LINE_AA)
            if self._chk_no_fire.isChecked():
                cv2.putText(frame, "NO-FIRE ZONES", (16, frame.shape[0] - 38), cv2.FONT_HERSHEY_SIMPLEX, 0.52, (80, 120, 210), 1, cv2.LINE_AA)
            if self._chk_current.isChecked():
                cv2.putText(frame, "CURRENT TARGET", (16, frame.shape[0] - 22), cv2.FONT_HERSHEY_SIMPLEX, 0.52, (60, 220, 120), 1, cv2.LINE_AA)
            if self._chk_other.isChecked():
                cv2.putText(frame, "OTHER TRACKED OBJECTS", (16, frame.shape[0] - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.52, (220, 200, 80), 1, cv2.LINE_AA)
            raw = frame

        rgb = cv2.cvtColor(raw, cv2.COLOR_BGR2RGB)
        h, w = rgb.shape[:2]
        image = QImage(rgb.data, w, h, 3 * w, QImage.Format_RGB888).copy()
        self._viewer.set_pixmap(QPixmap.fromImage(image))
        self._viewer.fit_to_window()

    def _export_mission(self) -> None:
        output_dir = self.repo.archive_root / self.mission_id / "exports"
        try:
            result = export_complete_package(self.repo, self.mission_id, output_dir)
        except Exception as exc:
            QMessageBox.critical(self, "Export Failed", str(exc))
            return
        QMessageBox.information(self, "Export Complete", json.dumps(result, ensure_ascii=True, indent=2))

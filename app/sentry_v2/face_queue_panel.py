"""
Face Queue Panel — Auto-enrollment conveyor strip.

Shows detected-but-unrecognised faces as cards stacked in a vertical strip
to the right of the video canvas.  Each card stays pinned until the operator
renames it and clicks [Save], at which point it fades out and collapses
upward, making room for the next pending card.
"""

from __future__ import annotations

from typing import Dict, Optional, Set

import cv2
import numpy as np

from PyQt5.QtCore import (
    QByteArray, QEasingCurve, QPropertyAnimation, Qt, QTimer, pyqtSignal,
)
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (
    QFrame, QGraphicsOpacityEffect, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout, QWidget,
)

_CARD_WIDTH = 148
_PANEL_WIDTH = _CARD_WIDTH + 10
_COLLAPSED_PANEL_WIDTH = 28
_IMG_SIZE = 100


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _bgr_crop_to_pixmap(crop_bgr: Optional[np.ndarray], size: int = _IMG_SIZE) -> QPixmap:
    if crop_bgr is None or crop_bgr.size == 0:
        return QPixmap()
    h, w = crop_bgr.shape[:2]
    if h <= 0 or w <= 0:
        return QPixmap()
    # Square-crop from centre
    if w > h:
        off = (w - h) // 2
        crop_bgr = crop_bgr[:, off: off + h]
    elif h > w:
        off = (h - w) // 2
        crop_bgr = crop_bgr[off: off + w, :]
    try:
        crop_bgr = cv2.resize(crop_bgr, (size, size), interpolation=cv2.INTER_AREA)
        rgb = cv2.cvtColor(crop_bgr, cv2.COLOR_BGR2RGB)
    except Exception:
        return QPixmap()
    qimg = QImage(
        rgb.data,
        rgb.shape[1],
        rgb.shape[0],
        int(rgb.strides[0]),
        QImage.Format_RGB888,
    )
    return QPixmap.fromImage(qimg).copy()


# ---------------------------------------------------------------------------
# FaceQueueCard
# ---------------------------------------------------------------------------

class FaceQueueCard(QFrame):
    """
    A single pending-enrollment card.

    Stays visible and interactive until [Save] is clicked, then fades out
    and collapses so the item above it "shifts up" to fill the gap.

    Signals
    -------
    save_requested(temp_id, name, is_target, embedding)
    """

    save_requested = pyqtSignal(str, str, bool, object)

    def __init__(
        self,
        temp_id: str,
        crop_bgr: Optional[np.ndarray],
        embedding: Optional[np.ndarray],
        default_name: str,
        parent: Optional[QWidget] = None,
    ) -> None:
        super().__init__(parent)
        self._temp_id = temp_id
        self._embedding = embedding
        self._saved = False

        self.setObjectName("FaceQueueCard")
        self.setFrameShape(QFrame.StyledPanel)
        self.setFixedWidth(_CARD_WIDTH)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        self._apply_pending_style()

        lay = QVBoxLayout(self)
        lay.setContentsMargins(6, 8, 6, 8)
        lay.setSpacing(5)

        # ── Face thumbnail ──────────────────────────────────────────────────
        self._img_label = QLabel()
        self._img_label.setFixedSize(_IMG_SIZE, _IMG_SIZE)
        self._img_label.setAlignment(Qt.AlignCenter)
        self._img_label.setStyleSheet(
            "border: 1px solid #444; border-radius: 6px; background: #111122;"
        )
        pixmap = _bgr_crop_to_pixmap(crop_bgr, _IMG_SIZE)
        if not pixmap.isNull():
            self._img_label.setPixmap(
                pixmap.scaled(_IMG_SIZE, _IMG_SIZE, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            )
        else:
            self._img_label.setText("No Image")
            self._img_label.setStyleSheet(
                "color:#666; border:1px solid #333; border-radius:6px; background:#111;"
            )
        lay.addWidget(self._img_label, 0, Qt.AlignCenter)

        # ── Name field ───────────────────────────────────────────────────────
        self._name_edit = QLineEdit(default_name)
        self._name_edit.setPlaceholderText("Name…")
        self._name_edit.setMaximumWidth(_CARD_WIDTH - 12)
        self._name_edit.textChanged.connect(self._on_name_changed)
        lay.addWidget(self._name_edit)

        # ── Target / Friendly toggle ─────────────────────────────────────────
        self._btn_target = QPushButton("🟢 Friendly")
        self._btn_target.setCheckable(True)
        self._btn_target.setChecked(False)
        self._btn_target.setMaximumWidth(_CARD_WIDTH - 12)
        self._btn_target.setStyleSheet(
            "QPushButton { background:#1a3a1a; color:#88cc88; border:1px solid #336633;"
            " border-radius:4px; padding:2px 4px; font-size:11px; }"
            "QPushButton:checked { background:#3a1a1a; color:#cc8888; border:1px solid #663333; }"
        )
        self._btn_target.toggled.connect(self._on_target_toggled)
        lay.addWidget(self._btn_target)

        # ── Save button ───────────────────────────────────────────────────────
        self._btn_save = QPushButton("Save ✓")
        self._btn_save.setMaximumWidth(_CARD_WIDTH - 12)
        self._btn_save.setEnabled(bool(default_name.strip()))
        self._btn_save.setStyleSheet(
            "QPushButton { background:#1a2a4a; color:#aaccff; border:1px solid #2255aa;"
            " border-radius:4px; padding:3px 6px; font-size:11px; font-weight:bold; }"
            "QPushButton:hover { background:#223355; }"
            "QPushButton:disabled { color:#555; border-color:#333; background:#111; }"
        )
        self._btn_save.clicked.connect(self._on_save_clicked)
        lay.addWidget(self._btn_save)

    # ── Slots ────────────────────────────────────────────────────────────────

    def _on_name_changed(self, text: str) -> None:
        self._btn_save.setEnabled(bool(text.strip()) and not self._saved)

    def _on_target_toggled(self, checked: bool) -> None:
        self._btn_target.setText("🔴 Target" if checked else "🟢 Friendly")

    def _on_save_clicked(self) -> None:
        if self._saved:
            return
        self._saved = True
        self._name_edit.setEnabled(False)
        self._btn_target.setEnabled(False)
        self._btn_save.setEnabled(False)
        self._btn_save.setText("Saved ✓")
        self._apply_saved_style()

        name = self._name_edit.text().strip()
        is_target = self._btn_target.isChecked()
        self.save_requested.emit(self._temp_id, name, is_target, self._embedding)
        self._start_exit_animation()

    # ── Styles ───────────────────────────────────────────────────────────────

    def _apply_pending_style(self) -> None:
        self.setStyleSheet(
            "QFrame#FaceQueueCard {"
            "  background: #16162e;"
            "  border: 2px solid #e0a020;"
            "  border-radius: 8px;"
            "}"
        )

    def _apply_saved_style(self) -> None:
        self.setStyleSheet(
            "QFrame#FaceQueueCard {"
            "  background: #0f1a0f;"
            "  border: 2px solid #2a6a2a;"
            "  border-radius: 8px;"
            "}"
        )

    # ── Exit animation (fade + height-collapse) ───────────────────────────────

    def _start_exit_animation(self) -> None:
        # Opacity fade
        effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(effect)
        self._fade_anim = QPropertyAnimation(effect, QByteArray(b"opacity"), self)
        self._fade_anim.setDuration(800)
        self._fade_anim.setStartValue(1.0)
        self._fade_anim.setEndValue(0.0)
        self._fade_anim.setEasingCurve(QEasingCurve.InQuad)
        self._fade_anim.start()

        # Height collapse (starts 200 ms after fade begins → "slide upward" feel)
        self._height_anim = QPropertyAnimation(self, QByteArray(b"maximumHeight"), self)
        self._height_anim.setDuration(1100)
        self._height_anim.setStartValue(self.sizeHint().height())
        self._height_anim.setEndValue(0)
        self._height_anim.setEasingCurve(QEasingCurve.InCubic)
        self._height_anim.finished.connect(self._remove_self)
        QTimer.singleShot(200, self._height_anim.start)

    def _remove_self(self) -> None:
        parent_widget = self.parent()
        if parent_widget is not None:
            layout = parent_widget.layout()
            if layout is not None:
                layout.removeWidget(self)
        self.deleteLater()


# ---------------------------------------------------------------------------
# FaceQueuePanel
# ---------------------------------------------------------------------------

class FaceQueuePanel(QWidget):
    """
    Vertical strip docked to the right of the video canvas.

    New unrecognised faces are pushed to the bottom; saved cards fade and
    collapse upward, giving a natural conveyor/wheel feel.

    Signals
    -------
    face_saved(temp_id: str, name: str, is_target: bool, embedding: object)
    """

    face_saved = pyqtSignal(str, str, bool, object)

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)
        self._seen_temp_ids: Set[str] = set()
        self._cards: Dict[str, FaceQueueCard] = {}
        self._person_counter: int = 0
        self._collapsed: bool = False

        self.setMinimumWidth(_PANEL_WIDTH)
        self.setMaximumWidth(_PANEL_WIDTH)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setObjectName("FaceQueuePanel")
        self.setStyleSheet(
            "QWidget#FaceQueuePanel {"
            "  background: #0b0b1c;"
            "  border-left: 1px solid #252545;"
            "}"
        )

        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        # Header bar
        header = QWidget()
        header.setFixedHeight(24)
        header.setStyleSheet(
            "QWidget {"
            "  background: #12122a;"
            "  border-bottom: 1px solid #252545;"
            "}"
        )
        header_lay = QHBoxLayout(header)
        header_lay.setContentsMargins(4, 2, 4, 2)
        header_lay.setSpacing(4)

        self._header_label = QLabel("Detected Faces")
        self._header_label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self._header_label.setStyleSheet(
            "QLabel {"
            "  color: #9999cc;"
            "  font-size: 10px;"
            "  font-weight: bold;"
            "}"
        )
        header_lay.addWidget(self._header_label, 1)

        self._toggle_btn = QPushButton("<")
        self._toggle_btn.setFixedSize(18, 18)
        self._toggle_btn.setCursor(Qt.PointingHandCursor)
        self._toggle_btn.setStyleSheet(
            "QPushButton {"
            "  background: #1b1b36;"
            "  color: #ccd4ff;"
            "  border: 1px solid #30305a;"
            "  border-radius: 4px;"
            "  font-size: 11px;"
            "  font-weight: bold;"
            "  padding: 0;"
            "}"
            "QPushButton:hover { background: #242449; }"
        )
        self._toggle_btn.clicked.connect(self.toggle_collapsed)
        header_lay.addWidget(self._toggle_btn, 0, Qt.AlignRight)
        outer.addWidget(header)

        # Scroll area holds the card stack
        self._scroll = QScrollArea()
        self._scroll.setWidgetResizable(True)
        self._scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self._scroll.setStyleSheet(
            "QScrollArea { border: none; background: transparent; }"
            "QScrollBar:vertical { width: 6px; background: #0b0b1c; }"
            "QScrollBar::handle:vertical { background: #333355; border-radius: 3px; }"
        )
        outer.addWidget(self._scroll, 1)

        # Card container inside the scroll area
        self._cards_widget = QWidget()
        self._cards_widget.setStyleSheet("background: transparent;")
        self._cards_lay = QVBoxLayout(self._cards_widget)
        self._cards_lay.setContentsMargins(4, 4, 4, 4)
        self._cards_lay.setSpacing(6)
        self._cards_lay.addStretch(1)  # pushes cards to the bottom of empty space
        self._scroll.setWidget(self._cards_widget)
        self._update_header_text()

    # ── Public API ───────────────────────────────────────────────────────────

    def push_detection(
        self,
        temp_id: str,
        crop_bgr: Optional[np.ndarray],
        embedding: Optional[np.ndarray],
    ) -> None:
        """
        Called from the UI thread when a new unrecognised face is detected.
        Idempotent: duplicate temp_ids within the same session are ignored.
        """
        if temp_id in self._seen_temp_ids:
            return
        self._seen_temp_ids.add(temp_id)
        self._person_counter += 1
        default_name = f"Person {self._person_counter:02d}"

        card = FaceQueueCard(
            temp_id=temp_id,
            crop_bgr=crop_bgr,
            embedding=embedding,
            default_name=default_name,
            parent=self._cards_widget,
        )
        card.save_requested.connect(self._on_card_saved)
        self._cards[temp_id] = card

        # Insert before the trailing stretch so cards stack at the bottom
        insert_pos = self._cards_lay.count() - 1
        self._cards_lay.insertWidget(insert_pos, card)
        self._update_header_text()

        # Auto-scroll to show the newest card
        QTimer.singleShot(60, self._scroll_to_bottom)

    def set_collapsed(self, collapsed: bool) -> None:
        collapsed = bool(collapsed)
        if self._collapsed == collapsed:
            return
        self._collapsed = collapsed
        self._header_label.setVisible(not collapsed)
        self._scroll.setVisible(not collapsed)
        width = _COLLAPSED_PANEL_WIDTH if collapsed else _PANEL_WIDTH
        self.setMinimumWidth(width)
        self.setMaximumWidth(width)
        self._toggle_btn.setText(">" if collapsed else "<")
        self._update_header_text()

    def toggle_collapsed(self) -> None:
        self.set_collapsed(not self._collapsed)

    def is_collapsed(self) -> bool:
        return bool(self._collapsed)

    def _update_header_text(self) -> None:
        pending = len(self._cards)
        title = "Detected Faces"
        if pending > 0:
            title = f"Detected Faces ({pending})"
        self._header_label.setText(title)
        if self._collapsed:
            tooltip = "Show detected faces"
        else:
            tooltip = "Hide detected faces"
        if pending > 0:
            tooltip += f" ({pending} pending)"
        self._toggle_btn.setToolTip(tooltip)

    # ── Private slots ────────────────────────────────────────────────────────

    def _on_card_saved(
        self,
        temp_id: str,
        name: str,
        is_target: bool,
        embedding: object,
    ) -> None:
        self._cards.pop(temp_id, None)
        self._update_header_text()
        self.face_saved.emit(temp_id, name, is_target, embedding)

    def _scroll_to_bottom(self) -> None:
        self._scroll.verticalScrollBar().setValue(
            self._scroll.verticalScrollBar().maximum()
        )

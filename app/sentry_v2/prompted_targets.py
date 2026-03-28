from __future__ import annotations

import base64
import json
import time
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Tuple

import cv2
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (
    QDialog,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QSlider,
    QVBoxLayout,
    QWidget,
)

from .sentry_v2_video_canvas import SentryV2VideoCanvas
from .target_filter import DetectedObject


def _clamp_bbox(bbox: Tuple[int, int, int, int], frame_width: int, frame_height: int) -> Tuple[int, int, int, int]:
    x, y, w, h = [int(v) for v in bbox]
    x = max(0, min(int(frame_width) - 1, x))
    y = max(0, min(int(frame_height) - 1, y))
    w = max(1, min(int(frame_width) - x, w))
    h = max(1, min(int(frame_height) - y, h))
    return x, y, w, h


def _crop_frame(frame: np.ndarray, bbox: Tuple[int, int, int, int]) -> np.ndarray:
    frame_height, frame_width = frame.shape[:2]
    x, y, w, h = _clamp_bbox(bbox, frame_width, frame_height)
    return frame[y:y + h, x:x + w].copy()


def _encode_png(image: np.ndarray) -> str:
    ok, encoded = cv2.imencode('.png', image)
    if not ok:
        raise ValueError('failed to encode target crop')
    return base64.b64encode(encoded.tobytes()).decode('ascii')


def _decode_png(payload: str) -> np.ndarray:
    raw = base64.b64decode(payload.encode('ascii'))
    arr = np.frombuffer(raw, dtype=np.uint8)
    image = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError('failed to decode target crop')
    return image


def _compute_histogram(image: np.ndarray) -> np.ndarray:
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1], None, [24, 24], [0, 180, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    return hist.astype(np.float32)


def _hist_similarity(a: np.ndarray, b: np.ndarray) -> float:
    if a.size == 0 or b.size == 0:
        return 0.0
    score = cv2.compareHist(a.astype(np.float32), b.astype(np.float32), cv2.HISTCMP_CORREL)
    return float(max(0.0, min(1.0, (score + 1.0) * 0.5)))


def _resize_for_template(image: np.ndarray, max_dim: int = 96) -> np.ndarray:
    h, w = image.shape[:2]
    if h <= 0 or w <= 0:
        return image.copy()
    scale = min(1.0, float(max_dim) / float(max(h, w)))
    if scale >= 0.999:
        return image.copy()
    new_w = max(8, int(round(w * scale)))
    new_h = max(8, int(round(h * scale)))
    return cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)


@dataclass
class PromptedTargetExample:
    source_type: str
    bbox: Tuple[int, int, int, int]
    crop_b64: str
    source_path: str = ''
    frame_index: int = 0

    @classmethod
    def from_frame(
        cls,
        frame: np.ndarray,
        bbox: Tuple[int, int, int, int],
        *,
        source_type: str,
        source_path: str = '',
        frame_index: int = 0,
    ) -> 'PromptedTargetExample':
        crop = _crop_frame(frame, bbox)
        return cls(
            source_type=str(source_type),
            bbox=tuple(int(v) for v in bbox),
            crop_b64=_encode_png(crop),
            source_path=str(source_path or ''),
            frame_index=int(frame_index),
        )

    def crop_image(self) -> np.ndarray:
        return _decode_png(self.crop_b64)

    def to_dict(self) -> dict:
        return {
            'source_type': self.source_type,
            'bbox': [int(v) for v in self.bbox],
            'crop_b64': self.crop_b64,
            'source_path': self.source_path,
            'frame_index': int(self.frame_index),
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'PromptedTargetExample':
        bbox = tuple(int(v) for v in (data.get('bbox') or [0, 0, 1, 1])[:4])
        return cls(
            source_type=str(data.get('source_type', 'live') or 'live'),
            bbox=(bbox[0], bbox[1], max(1, bbox[2]), max(1, bbox[3])),
            crop_b64=str(data.get('crop_b64', '') or ''),
            source_path=str(data.get('source_path', '') or ''),
            frame_index=int(data.get('frame_index', 0) or 0),
        )


@dataclass
class PromptedTargetProfile:
    target_id: str
    name: str
    enabled: bool = True
    min_match_score: float = 0.58
    min_confirm_hits: int = 2
    lost_timeout_s: float = 1.2
    local_search_padding_px: int = 84
    full_frame_search_interval: int = 6
    examples: List[PromptedTargetExample] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            'target_id': self.target_id,
            'name': self.name,
            'enabled': bool(self.enabled),
            'min_match_score': float(self.min_match_score),
            'min_confirm_hits': int(self.min_confirm_hits),
            'lost_timeout_s': float(self.lost_timeout_s),
            'local_search_padding_px': int(self.local_search_padding_px),
            'full_frame_search_interval': int(self.full_frame_search_interval),
            'examples': [example.to_dict() for example in self.examples],
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'PromptedTargetProfile':
        return cls(
            target_id=str(data.get('target_id', '') or uuid.uuid4().hex),
            name=str(data.get('name', 'Target') or 'Target'),
            enabled=bool(data.get('enabled', True)),
            min_match_score=float(data.get('min_match_score', 0.58) or 0.58),
            min_confirm_hits=max(1, int(data.get('min_confirm_hits', 2) or 2)),
            lost_timeout_s=float(data.get('lost_timeout_s', 1.2) or 1.2),
            local_search_padding_px=int(data.get('local_search_padding_px', 84) or 84),
            full_frame_search_interval=max(1, int(data.get('full_frame_search_interval', 6) or 6)),
            examples=[PromptedTargetExample.from_dict(item) for item in list(data.get('examples', []))],
        )


class PromptedTargetLibrary:
    def __init__(self, profiles: Optional[List[PromptedTargetProfile]] = None):
        self.profiles: List[PromptedTargetProfile] = list(profiles or [])

    def to_dict(self) -> dict:
        return {
            'version': 1,
            'updated_at': time.time(),
            'targets': [profile.to_dict() for profile in self.profiles],
        }

    def save(self, path: str) -> None:
        target_path = Path(path)
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(json.dumps(self.to_dict(), indent=2), encoding='utf-8')

    @classmethod
    def load(cls, path: str) -> 'PromptedTargetLibrary':
        target_path = Path(path)
        if not target_path.exists():
            return cls()
        try:
            data = json.loads(target_path.read_text(encoding='utf-8'))
        except Exception:
            return cls()
        profiles = [PromptedTargetProfile.from_dict(item) for item in list(data.get('targets', []))]
        return cls(profiles)

    def get_profile(self, target_id: str) -> Optional[PromptedTargetProfile]:
        for profile in self.profiles:
            if profile.target_id == target_id:
                return profile
        return None

    def next_default_name(self, prefix: str = 'Prompted Target') -> str:
        existing = {profile.name for profile in self.profiles}
        index = 1
        while True:
            candidate = f'{prefix} {index}'
            if candidate not in existing:
                return candidate
            index += 1

    def add_new_target(self, name: str, selections: List['PromptedSelection']) -> Optional[PromptedTargetProfile]:
        if not selections:
            return None
        profile = PromptedTargetProfile(
            target_id=uuid.uuid4().hex,
            name=str(name or self.next_default_name()).strip() or self.next_default_name(),
            examples=[selection.to_example() for selection in selections],
        )
        self.profiles.append(profile)
        return profile

    def append_examples(self, target_id: str, selections: List['PromptedSelection']) -> Optional[PromptedTargetProfile]:
        profile = self.get_profile(target_id)
        if profile is None or not selections:
            return None
        profile.examples.extend(selection.to_example() for selection in selections)
        return profile

    def remove_target(self, target_id: str) -> None:
        self.profiles = [profile for profile in self.profiles if profile.target_id != target_id]

    def remove_last_example(self, target_id: str) -> Optional[PromptedTargetProfile]:
        profile = self.get_profile(target_id)
        if profile is None or not profile.examples:
            return None
        profile.examples.pop()
        return profile


@dataclass
class PromptedSelection:
    frame: np.ndarray
    bbox: Tuple[int, int, int, int]
    source_type: str
    source_path: str = ''
    frame_index: int = 0

    def to_example(self) -> PromptedTargetExample:
        return PromptedTargetExample.from_frame(
            self.frame,
            self.bbox,
            source_type=self.source_type,
            source_path=self.source_path,
            frame_index=self.frame_index,
        )


@dataclass
class _ExampleFeatures:
    template_gray: np.ndarray
    template_hist: np.ndarray
    aspect_ratio: float
    area: float


@dataclass
class _RuntimeState:
    last_bbox: Optional[Tuple[int, int, int, int]] = None
    last_seen: float = 0.0
    last_score: float = 0.0
    confirm_hits: int = 0
    missed_frames: int = 0
    frames_seen: int = 0


class PromptedTargetMatcher:
    def __init__(self, library: PromptedTargetLibrary):
        self.library = library
        self._runtime: dict[str, _RuntimeState] = {}
        self._feature_cache: dict[str, List[_ExampleFeatures]] = {}

    def reset(self) -> None:
        self._runtime.clear()

    def refresh_library_cache(self) -> None:
        self._runtime.clear()
        self._feature_cache.clear()

    def detect(
        self,
        frame: np.ndarray,
        base_detections: List[DetectedObject],
        timestamp: float,
    ) -> List[DetectedObject]:
        frame_height, frame_width = frame.shape[:2]
        results: List[DetectedObject] = []
        used_boxes: List[Tuple[int, int, int, int]] = []
        for profile in self.library.profiles:
            if not profile.enabled or not profile.examples:
                continue
            match = self._match_profile(frame, profile, base_detections, timestamp)
            if match is None:
                continue
            bbox, score = match
            if score < float(profile.min_match_score):
                continue
            if any(self._bbox_iou(bbox, other) > 0.70 for other in used_boxes):
                continue
            used_boxes.append(bbox)
            x, y, w, h = bbox
            results.append(
                DetectedObject(
                    track_id=0,
                    class_name=str(profile.name).strip() or 'prompted_target',
                    confidence=float(score),
                    bbox=(x, y, w, h),
                    center_x=x + (w / 2.0),
                    center_y=y + (h / 2.0),
                    source='prompted',
                    frame_width=frame_width,
                    frame_height=frame_height,
                )
            )
        return results

    def _match_profile(
        self,
        frame: np.ndarray,
        profile: PromptedTargetProfile,
        base_detections: List[DetectedObject],
        timestamp: float,
    ) -> Optional[Tuple[Tuple[int, int, int, int], float]]:
        state = self._runtime.setdefault(profile.target_id, _RuntimeState())
        state.frames_seen += 1
        features = self._features_for_profile(profile)
        best_bbox: Optional[Tuple[int, int, int, int]] = None
        best_score = 0.0

        if state.last_bbox is not None and (timestamp - state.last_seen) <= float(profile.lost_timeout_s):
            nearby = self._search_near_last_bbox(frame, state.last_bbox, features, int(profile.local_search_padding_px))
            if nearby is not None:
                best_bbox, best_score = nearby
        elif state.last_bbox is not None and (timestamp - state.last_seen) > float(profile.lost_timeout_s):
            state.last_bbox = None

        for det in sorted(base_detections, key=lambda item: float(item.confidence), reverse=True):
            candidate_score = self._score_bbox(frame, det.bbox, features)
            if candidate_score > best_score:
                best_score = candidate_score
                best_bbox = tuple(int(v) for v in det.bbox)

        should_try_global = (
            best_bbox is None
            or best_score < float(profile.min_match_score)
            or state.missed_frames > 0
            or (state.frames_seen % max(1, int(profile.full_frame_search_interval))) == 0
            or not base_detections
        )
        if should_try_global:
            global_match = self._search_full_frame(frame, features)
            if global_match is not None and global_match[1] > best_score:
                best_bbox, best_score = global_match

        if best_bbox is None or best_score < float(profile.min_match_score):
            state.confirm_hits = 0
            state.missed_frames += 1
            return None

        state.confirm_hits += 1
        state.missed_frames = 0
        state.last_bbox = best_bbox
        state.last_seen = float(timestamp)
        state.last_score = float(best_score)
        if state.confirm_hits < max(1, int(profile.min_confirm_hits)):
            return None
        return best_bbox, best_score

    def _features_for_profile(self, profile: PromptedTargetProfile) -> List[_ExampleFeatures]:
        cached = self._feature_cache.get(profile.target_id)
        if cached is not None and len(cached) == len(profile.examples):
            return cached
        features = [self._build_features(example.crop_image()) for example in profile.examples]
        self._feature_cache[profile.target_id] = features
        return features

    def _search_near_last_bbox(
        self,
        frame: np.ndarray,
        last_bbox: Tuple[int, int, int, int],
        features: List[_ExampleFeatures],
        padding_px: int,
    ) -> Optional[Tuple[Tuple[int, int, int, int], float]]:
        frame_height, frame_width = frame.shape[:2]
        x, y, w, h = last_bbox
        pad = max(24, int(padding_px))
        sx = max(0, x - pad)
        sy = max(0, y - pad)
        sw = min(frame_width - sx, w + (pad * 2))
        sh = min(frame_height - sy, h + (pad * 2))
        search = frame[sy:sy + sh, sx:sx + sw]
        if search.size == 0:
            return None
        local_match = self._search_region(search, features)
        if local_match is None:
            return None
        bbox, score = local_match
        return (sx + bbox[0], sy + bbox[1], bbox[2], bbox[3]), score

    def _search_full_frame(
        self,
        frame: np.ndarray,
        features: List[_ExampleFeatures],
    ) -> Optional[Tuple[Tuple[int, int, int, int], float]]:
        return self._search_region(frame, features)

    def _search_region(
        self,
        region: np.ndarray,
        features: List[_ExampleFeatures],
    ) -> Optional[Tuple[Tuple[int, int, int, int], float]]:
        if region.size == 0:
            return None
        gray_region = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
        best_bbox: Optional[Tuple[int, int, int, int]] = None
        best_score = 0.0
        for feature in features:
            template = feature.template_gray
            template_h, template_w = template.shape[:2]
            for scale in (0.70, 0.85, 1.0, 1.15, 1.35):
                scaled_w = max(8, int(round(template_w * scale)))
                scaled_h = max(8, int(round(template_h * scale)))
                if scaled_w >= gray_region.shape[1] or scaled_h >= gray_region.shape[0]:
                    continue
                scaled = cv2.resize(template, (scaled_w, scaled_h), interpolation=cv2.INTER_LINEAR)
                result = cv2.matchTemplate(gray_region, scaled, cv2.TM_CCOEFF_NORMED)
                _min_val, max_val, _min_loc, max_loc = cv2.minMaxLoc(result)
                bbox = (int(max_loc[0]), int(max_loc[1]), int(scaled_w), int(scaled_h))
                score = self._score_bbox(region, bbox, [feature], template_hint=float(max_val))
                if score > best_score:
                    best_score = score
                    best_bbox = bbox
        if best_bbox is None:
            return None
        return best_bbox, best_score

    def _score_bbox(
        self,
        frame: np.ndarray,
        bbox: Tuple[int, int, int, int],
        features: List[_ExampleFeatures],
        *,
        template_hint: Optional[float] = None,
    ) -> float:
        frame_height, frame_width = frame.shape[:2]
        x, y, w, h = _clamp_bbox(bbox, frame_width, frame_height)
        candidate = frame[y:y + h, x:x + w]
        if candidate.size == 0:
            return 0.0
        candidate_hist = _compute_histogram(candidate)
        candidate_gray = cv2.cvtColor(_resize_for_template(candidate), cv2.COLOR_BGR2GRAY)
        candidate_area = float(max(1, w * h))
        candidate_aspect = float(w) / float(max(1, h))

        best_score = 0.0
        for feature in features:
            resized_template = cv2.resize(feature.template_gray, (candidate_gray.shape[1], candidate_gray.shape[0]), interpolation=cv2.INTER_LINEAR)
            similarity_map = cv2.matchTemplate(candidate_gray, resized_template, cv2.TM_CCOEFF_NORMED)
            template_score = float(similarity_map[0][0]) if similarity_map.size else 0.0
            if template_hint is not None:
                template_score = max(template_score, float(template_hint))
            template_score = max(0.0, min(1.0, (template_score + 1.0) * 0.5))
            hist_score = _hist_similarity(candidate_hist, feature.template_hist)
            aspect_delta = abs(candidate_aspect - feature.aspect_ratio)
            aspect_score = max(0.0, 1.0 - min(1.0, aspect_delta / max(0.2, feature.aspect_ratio)))
            size_ratio = min(candidate_area, feature.area) / max(candidate_area, feature.area)
            score = (template_score * 0.58) + (hist_score * 0.27) + (aspect_score * 0.10) + (size_ratio * 0.05)
            best_score = max(best_score, float(score))
        return best_score

    @staticmethod
    def _build_features(crop: np.ndarray) -> _ExampleFeatures:
        templ = _resize_for_template(crop)
        gray = cv2.cvtColor(templ, cv2.COLOR_BGR2GRAY)
        hist = _compute_histogram(crop)
        h, w = crop.shape[:2]
        return _ExampleFeatures(
            template_gray=gray,
            template_hist=hist,
            aspect_ratio=float(w) / float(max(1, h)),
            area=float(max(1, w * h)),
        )

    @staticmethod
    def _bbox_iou(a: Tuple[int, int, int, int], b: Tuple[int, int, int, int]) -> float:
        ax, ay, aw, ah = a
        bx, by, bw, bh = b
        ax2, ay2 = ax + aw, ay + ah
        bx2, by2 = bx + bw, by + bh
        ix1 = max(ax, bx)
        iy1 = max(ay, by)
        ix2 = min(ax2, bx2)
        iy2 = min(ay2, by2)
        iw = max(0, ix2 - ix1)
        ih = max(0, iy2 - iy1)
        inter = iw * ih
        if inter <= 0:
            return 0.0
        union = max(1, (aw * ah) + (bw * bh) - inter)
        return float(inter) / float(union)


class PromptedMediaSelectionDialog(QDialog):
    def __init__(
        self,
        *,
        title: str,
        image: Optional[np.ndarray] = None,
        video_path: str = '',
        parent: Optional[QWidget] = None,
    ):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.resize(980, 720)
        self._video_path = str(video_path or '')
        self._video_cap: Optional[cv2.VideoCapture] = None
        self._frame_count = 1
        self._current_frame_index = 0
        self._current_frame: Optional[np.ndarray] = None
        self._base_image = image.copy() if image is not None else None
        self._selections: List[PromptedSelection] = []

        root = QVBoxLayout(self)
        self._canvas = SentryV2VideoCanvas('Load media to select targets')
        self._canvas.setMinimumSize(640, 420)
        self._canvas.set_roi_selection_enabled(True)
        self._canvas.roiSelected.connect(self._on_roi_selected)
        root.addWidget(self._canvas, 1)

        self._video_controls = QWidget()
        video_lay = QGridLayout(self._video_controls)
        self._btn_prev = QPushButton('Prev')
        self._btn_prev.clicked.connect(lambda: self._step_video(-1))
        video_lay.addWidget(self._btn_prev, 0, 0)
        self._btn_next = QPushButton('Next')
        self._btn_next.clicked.connect(lambda: self._step_video(1))
        video_lay.addWidget(self._btn_next, 0, 1)
        self._slider = QSlider(Qt.Horizontal)
        self._slider.valueChanged.connect(self._on_slider_changed)
        video_lay.addWidget(self._slider, 0, 2)
        self._lbl_frame = QLabel('Frame 0 / 0')
        video_lay.addWidget(self._lbl_frame, 0, 3)
        root.addWidget(self._video_controls)

        bottom = QHBoxLayout()
        self._selection_list = QListWidget()
        bottom.addWidget(self._selection_list, 1)

        right = QVBoxLayout()
        self._lbl_hint = QLabel('Drag a box on the preview to capture a target example.')
        self._lbl_hint.setWordWrap(True)
        right.addWidget(self._lbl_hint)
        btn_remove = QPushButton('Remove Last')
        btn_remove.clicked.connect(self._remove_last_selection)
        right.addWidget(btn_remove)
        btn_clear = QPushButton('Clear')
        btn_clear.clicked.connect(self._clear_selections)
        right.addWidget(btn_clear)
        btn_ok = QPushButton('Use Selections')
        btn_ok.clicked.connect(self.accept)
        right.addWidget(btn_ok)
        btn_cancel = QPushButton('Cancel')
        btn_cancel.clicked.connect(self.reject)
        right.addWidget(btn_cancel)
        right.addStretch()
        bottom.addLayout(right)
        root.addLayout(bottom, 1)

        if self._video_path:
            self._open_video(self._video_path)
        else:
            self._video_controls.setVisible(False)
            if self._base_image is not None:
                self._current_frame = self._base_image.copy()
                self._render_current_frame()

    def selections(self) -> List[PromptedSelection]:
        return list(self._selections)

    def accept(self) -> None:
        if not self._selections:
            self._lbl_hint.setText('Select at least one target region before continuing.')
            return
        super().accept()

    def closeEvent(self, event) -> None:
        self._close_video()
        super().closeEvent(event)

    def _open_video(self, path: str) -> None:
        self._close_video()
        cap = cv2.VideoCapture(path)
        if not cap.isOpened():
            self._lbl_hint.setText(f'Could not open video: {path}')
            return
        self._video_cap = cap
        self._frame_count = max(1, int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 1))
        self._slider.blockSignals(True)
        self._slider.setRange(0, max(0, self._frame_count - 1))
        self._slider.setValue(0)
        self._slider.blockSignals(False)
        self._load_video_frame(0)

    def _close_video(self) -> None:
        if self._video_cap is not None:
            try:
                self._video_cap.release()
            except Exception:
                pass
        self._video_cap = None

    def _on_slider_changed(self, value: int) -> None:
        if self._video_cap is None:
            return
        self._load_video_frame(int(value))

    def _step_video(self, delta: int) -> None:
        if self._video_cap is None:
            return
        target = max(0, min(self._frame_count - 1, self._current_frame_index + int(delta)))
        self._slider.setValue(target)

    def _load_video_frame(self, frame_index: int) -> None:
        if self._video_cap is None:
            return
        frame_index = max(0, min(self._frame_count - 1, int(frame_index)))
        self._video_cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ok, frame = self._video_cap.read()
        if not ok or frame is None:
            self._lbl_hint.setText(f'Could not read video frame {frame_index}.')
            return
        self._current_frame_index = frame_index
        self._current_frame = frame.copy()
        self._render_current_frame()

    def _on_roi_selected(self, frame_x: float, frame_y: float, width: float, height: float) -> None:
        if self._current_frame is None:
            return
        bbox = (
            int(round(frame_x)),
            int(round(frame_y)),
            max(1, int(round(width))),
            max(1, int(round(height))),
        )
        selection = PromptedSelection(
            frame=self._current_frame.copy(),
            bbox=bbox,
            source_type='video' if self._video_cap is not None else 'image',
            source_path=self._video_path,
            frame_index=int(self._current_frame_index),
        )
        self._selections.append(selection)
        label = (
            f'Frame {selection.frame_index}: x={bbox[0]} y={bbox[1]} w={bbox[2]} h={bbox[3]}'
            if selection.source_type == 'video'
            else f'x={bbox[0]} y={bbox[1]} w={bbox[2]} h={bbox[3]}'
        )
        self._selection_list.addItem(label)
        self._render_current_frame()

    def _remove_last_selection(self) -> None:
        if not self._selections:
            return
        self._selections.pop()
        self._selection_list.takeItem(self._selection_list.count() - 1)
        self._render_current_frame()

    def _clear_selections(self) -> None:
        self._selections.clear()
        self._selection_list.clear()
        self._render_current_frame()

    def _render_current_frame(self) -> None:
        if self._current_frame is None:
            return
        frame = self._current_frame.copy()
        for selection in self._selections:
            if self._video_cap is not None and selection.frame_index != self._current_frame_index:
                continue
            if self._video_cap is None and selection.source_type != 'image':
                continue
            x, y, w, h = selection.bbox
            cv2.rectangle(frame, (x, y), (x + w, y + h), (32, 214, 140), 2, cv2.LINE_AA)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb = np.ascontiguousarray(rgb)
        height, width, _channels = rgb.shape
        qimg = QImage(rgb.data, width, height, int(rgb.strides[0]), QImage.Format_RGB888).copy()
        self._canvas.set_frame(QPixmap.fromImage(qimg), width, height)
        if self._video_cap is not None:
            self._lbl_frame.setText(f'Frame {self._current_frame_index + 1} / {self._frame_count}')
        else:
            self._lbl_frame.setText('Image')

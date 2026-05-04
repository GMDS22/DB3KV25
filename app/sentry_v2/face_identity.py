from __future__ import annotations

import json
import time
import uuid
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

import cv2
import numpy as np

from app.runtime_paths import runtime_root_path


DEFAULT_FACE_DETECTOR_MODEL_RELATIVE_PATH = "app/models/face/face_detection_yunet_2023mar.onnx"
DEFAULT_FACE_RECOGNIZER_MODEL_RELATIVE_PATH = "app/models/face/face_recognition_sface_2021dec.onnx"

FACE_EMBEDDING_BACKEND_LEGACY = "legacy_dct"
FACE_EMBEDDING_BACKEND_SFACE = "opencv_sface"

_YUNET_INPUT_SIZE = (320, 320)
_YUNET_SCORE_THRESHOLD = 0.88
_YUNET_NMS_THRESHOLD = 0.3
_YUNET_TOP_K = 96
_LEGACY_EMBEDDING_SIZE = 160
_SFACE_MAX_DETECT_DIM = 640
_SFACE_EMBEDDING_SIZE = 128
_SFACE_RECOMMENDED_COSINE_THRESHOLD = 0.363
_SFACE_AMBIGUITY_MARGIN = 0.015


@dataclass
class FaceIdentityProfile:
    profile_id: str
    name: str
    embeddings: List[List[float]] = field(default_factory=list)
    embedding_backend: str = FACE_EMBEDDING_BACKEND_LEGACY
    friendly: bool = True
    announce_name: bool = True
    cute_gesture: bool = True
    notes: str = ""
    created_at: float = field(default_factory=time.time)
    updated_at: float = field(default_factory=time.time)


@dataclass
class FaceMatchResult:
    bbox: Tuple[int, int, int, int]
    profile_id: str = ""
    name: str = ""
    confidence: float = 0.0
    friendly: bool = False
    announce_name: bool = False
    cute_gesture: bool = False


@dataclass
class _DetectedFaceEntry:
    bbox: Tuple[int, int, int, int]
    landmarks: Optional[np.ndarray] = None
    score: float = 0.0


def expected_embedding_size_for_backend(backend: str) -> Optional[int]:
    normalized = str(backend or "").strip().lower()
    if normalized == FACE_EMBEDDING_BACKEND_LEGACY:
        return _LEGACY_EMBEDDING_SIZE
    if normalized == FACE_EMBEDDING_BACKEND_SFACE:
        return _SFACE_EMBEDDING_SIZE
    return None


def count_compatible_profile_embeddings(
    profile: FaceIdentityProfile,
    *,
    backend: Optional[str] = None,
) -> int:
    profile_backend = str(
        getattr(profile, "embedding_backend", FACE_EMBEDDING_BACKEND_LEGACY)
        or FACE_EMBEDDING_BACKEND_LEGACY
    ).strip().lower()
    if backend is not None and profile_backend != str(backend or "").strip().lower():
        return 0
    expected_size = expected_embedding_size_for_backend(profile_backend)
    compatible = 0
    for raw in getattr(profile, "embeddings", []) or []:
        candidate = np.asarray(raw, dtype=np.float32).flatten()
        if candidate.size <= 0:
            continue
        if expected_size is not None and candidate.size != expected_size:
            continue
        compatible += 1
    return compatible


class FaceIdentityLibrary:
    def __init__(self, profiles: Optional[List[FaceIdentityProfile]] = None):
        self.profiles: List[FaceIdentityProfile] = list(profiles or [])

    @classmethod
    def load(cls, path: str) -> "FaceIdentityLibrary":
        p = Path(path)
        if not p.exists():
            return cls()
        try:
            raw = json.loads(p.read_text(encoding="utf-8-sig"))
        except Exception:
            return cls()
        items = list(raw.get("profiles", [])) if isinstance(raw, dict) else []
        profiles: List[FaceIdentityProfile] = []
        for item in items:
            if not isinstance(item, dict):
                continue
            profiles.append(FaceIdentityProfile(**item))
        return cls(profiles)

    def save(self, path: str) -> None:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "schema": 1,
            "profiles": [asdict(profile) for profile in self.profiles],
        }
        p.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def upsert_profile(
        self,
        name: str,
        embeddings: Iterable[np.ndarray],
        *,
        embedding_backend: str = FACE_EMBEDDING_BACKEND_LEGACY,
        friendly: bool = True,
        announce_name: bool = True,
        cute_gesture: bool = True,
        notes: str = "",
    ) -> Optional[FaceIdentityProfile]:
        cleaned_name = str(name or "").strip()
        incoming_backend = str(embedding_backend or FACE_EMBEDDING_BACKEND_LEGACY).strip().lower()
        expected_size = expected_embedding_size_for_backend(incoming_backend)
        vectors = [np.asarray(vector, dtype=np.float32).flatten() for vector in embeddings if vector is not None]
        if expected_size is not None:
            vectors = [vector for vector in vectors if vector.size == expected_size]
        if not cleaned_name or not vectors:
            return None
        now = time.time()
        existing = self.find_by_name(cleaned_name)
        serialized = [vector.astype(float).tolist() for vector in vectors]
        if existing is None:
            profile = FaceIdentityProfile(
                profile_id=str(uuid.uuid4()),
                name=cleaned_name,
                embeddings=serialized,
                embedding_backend=incoming_backend,
                friendly=bool(friendly),
                announce_name=bool(announce_name),
                cute_gesture=bool(cute_gesture),
                notes=str(notes or ""),
                created_at=now,
                updated_at=now,
            )
            self.profiles.append(profile)
            return profile
        existing_backend = str(existing.embedding_backend or FACE_EMBEDDING_BACKEND_LEGACY)
        if existing_backend != incoming_backend:
            existing.embeddings = []
            existing.embedding_backend = incoming_backend
        elif expected_size is not None:
            existing.embeddings = [
                np.asarray(raw, dtype=np.float32).flatten().astype(float).tolist()
                for raw in existing.embeddings
                if np.asarray(raw, dtype=np.float32).flatten().size == expected_size
            ]
        existing.embeddings.extend(serialized)
        existing.friendly = bool(friendly)
        existing.announce_name = bool(announce_name)
        existing.cute_gesture = bool(cute_gesture)
        existing.notes = str(notes or existing.notes or "")
        existing.updated_at = now
        return existing

    def remove_profile(self, profile_id: str) -> bool:
        before = len(self.profiles)
        self.profiles = [profile for profile in self.profiles if str(profile.profile_id) != str(profile_id)]
        return len(self.profiles) != before

    def find_by_name(self, name: str) -> Optional[FaceIdentityProfile]:
        target = str(name or "").strip().lower()
        for profile in self.profiles:
            if str(profile.name or "").strip().lower() == target:
                return profile
        return None


class FaceIdentityRuntime:
    def __init__(
        self,
        library: FaceIdentityLibrary,
        *,
        preferred_backend: str = FACE_EMBEDDING_BACKEND_SFACE,
        detector_model_path: Optional[str] = None,
        recognizer_model_path: Optional[str] = None,
        allow_legacy_fallback: bool = True,
    ):
        self.library = library
        cascade_path = self._resolve_cascade_path()
        if cascade_path is None:
            self._cascade = cv2.CascadeClassifier()
        else:
            self._cascade = cv2.CascadeClassifier(str(cascade_path))
        self._preferred_backend = FACE_EMBEDDING_BACKEND_LEGACY
        self._active_backend = FACE_EMBEDDING_BACKEND_LEGACY
        self._backend_status = "legacy_dct ready"
        self._allow_legacy_fallback = bool(allow_legacy_fallback)
        self._detector_model_path: Optional[Path] = None
        self._recognizer_model_path: Optional[Path] = None
        self._face_detector = None
        self._face_recognizer = None
        self.configure_backend(
            preferred_backend=preferred_backend,
            detector_model_path=detector_model_path,
            recognizer_model_path=recognizer_model_path,
            allow_legacy_fallback=allow_legacy_fallback,
        )

    @staticmethod
    def _resolve_cascade_path() -> Optional[Path]:
        candidate_paths: List[Path] = []

        raw_haarcascades = str(getattr(cv2.data, "haarcascades", "") or "").strip()
        if raw_haarcascades:
            candidate_paths.append(Path(raw_haarcascades) / "haarcascade_frontalface_default.xml")

        try:
            cv2_root = Path(cv2.__file__).resolve().parent
            candidate_paths.append(cv2_root / "data" / "haarcascade_frontalface_default.xml")
        except Exception:
            pass

        try:
            candidate_paths.append(runtime_root_path() / "cv2" / "data" / "haarcascade_frontalface_default.xml")
        except Exception:
            pass

        seen: set[str] = set()
        for candidate in candidate_paths:
            candidate_text = str(candidate)
            if candidate_text in seen:
                continue
            seen.add(candidate_text)
            try:
                if candidate.is_file():
                    return candidate
            except Exception:
                continue
        return None

    def refresh_library(self, library: FaceIdentityLibrary) -> None:
        self.library = library

    @property
    def active_backend(self) -> str:
        return str(self._active_backend)

    @property
    def preferred_backend(self) -> str:
        return str(self._preferred_backend)

    def backend_status(self) -> str:
        return str(self._backend_status)

    def supported_profile_backends(self) -> Tuple[str, ...]:
        backends: List[str] = [str(self._active_backend or FACE_EMBEDDING_BACKEND_LEGACY)]
        if self._allow_legacy_fallback and self._active_backend == FACE_EMBEDDING_BACKEND_SFACE:
            backends.append(FACE_EMBEDDING_BACKEND_LEGACY)
        ordered: List[str] = []
        for backend in backends:
            normalized = str(backend or "").strip().lower()
            if not normalized or normalized in ordered:
                continue
            ordered.append(normalized)
        return tuple(ordered)

    def profile_backend_is_matchable(self, backend: str) -> bool:
        normalized = str(backend or FACE_EMBEDDING_BACKEND_LEGACY).strip().lower()
        return normalized in self.supported_profile_backends()

    def matchable_profile_embedding_count(self, profile: FaceIdentityProfile) -> int:
        profile_backend = str(
            getattr(profile, "embedding_backend", FACE_EMBEDDING_BACKEND_LEGACY)
            or FACE_EMBEDDING_BACKEND_LEGACY
        ).strip().lower()
        if not self.profile_backend_is_matchable(profile_backend):
            return 0
        return count_compatible_profile_embeddings(profile, backend=profile_backend)

    def detector_model_path(self) -> Optional[Path]:
        return self._detector_model_path

    def recognizer_model_path(self) -> Optional[Path]:
        return self._recognizer_model_path

    def configure_backend(
        self,
        *,
        preferred_backend: str = FACE_EMBEDDING_BACKEND_SFACE,
        detector_model_path: Optional[str] = None,
        recognizer_model_path: Optional[str] = None,
        allow_legacy_fallback: bool = True,
    ) -> None:
        preferred = str(preferred_backend or FACE_EMBEDDING_BACKEND_SFACE).strip().lower()
        if preferred not in {FACE_EMBEDDING_BACKEND_LEGACY, FACE_EMBEDDING_BACKEND_SFACE}:
            preferred = FACE_EMBEDDING_BACKEND_SFACE
        self._preferred_backend = preferred
        self._allow_legacy_fallback = bool(allow_legacy_fallback)
        self._detector_model_path = self._resolve_runtime_path(
            detector_model_path or DEFAULT_FACE_DETECTOR_MODEL_RELATIVE_PATH
        )
        self._recognizer_model_path = self._resolve_runtime_path(
            recognizer_model_path or DEFAULT_FACE_RECOGNIZER_MODEL_RELATIVE_PATH
        )
        self._face_detector = None
        self._face_recognizer = None

        if preferred == FACE_EMBEDDING_BACKEND_SFACE:
            self._configure_sface_backend()
            if self._active_backend == FACE_EMBEDDING_BACKEND_SFACE:
                return

        self._active_backend = FACE_EMBEDDING_BACKEND_LEGACY
        if self._allow_legacy_fallback:
            suffix = ""
            if preferred == FACE_EMBEDDING_BACKEND_SFACE and self._backend_status:
                suffix = f"; fallback to legacy_dct"
            self._backend_status = (self._backend_status or "legacy_dct ready") + suffix
        else:
            self._backend_status = self._backend_status or "legacy_dct forced"

    @staticmethod
    def _resolve_runtime_path(path_value: str) -> Path:
        candidate = Path(str(path_value or "")).expanduser()
        if candidate.is_absolute():
            return candidate
        return (runtime_root_path() / candidate).resolve()

    def _configure_sface_backend(self) -> None:
        self._backend_status = ""
        detector_path = self._detector_model_path
        recognizer_path = self._recognizer_model_path
        missing: List[str] = []
        if detector_path is None or not detector_path.is_file():
            missing.append(str(detector_path) if detector_path is not None else DEFAULT_FACE_DETECTOR_MODEL_RELATIVE_PATH)
        if recognizer_path is None or not recognizer_path.is_file():
            missing.append(str(recognizer_path) if recognizer_path is not None else DEFAULT_FACE_RECOGNIZER_MODEL_RELATIVE_PATH)
        if missing:
            self._backend_status = "opencv_sface unavailable: missing model file(s): " + ", ".join(missing)
            return
        try:
            self._face_detector = cv2.FaceDetectorYN.create(
                model=str(detector_path),
                config="",
                input_size=_YUNET_INPUT_SIZE,
                score_threshold=float(_YUNET_SCORE_THRESHOLD),
                nms_threshold=float(_YUNET_NMS_THRESHOLD),
                top_k=int(_YUNET_TOP_K),
            )
            self._face_recognizer = cv2.FaceRecognizerSF.create(
                model=str(recognizer_path),
                config="",
            )
        except Exception as exc:
            self._face_detector = None
            self._face_recognizer = None
            self._backend_status = f"opencv_sface unavailable: {exc}"
            return
        self._active_backend = FACE_EMBEDDING_BACKEND_SFACE
        self._backend_status = (
            f"opencv_sface ready ({detector_path.name}, {recognizer_path.name})"
        )

    def detect_faces(
        self,
        frame: np.ndarray,
        *,
        min_face_size_px: int = 56,
        roi_boxes: Optional[List[Tuple[int, int, int, int]]] = None,
    ) -> List[Tuple[int, int, int, int]]:
        entries = self._detect_face_entries(
            frame,
            min_face_size_px=min_face_size_px,
            roi_boxes=roi_boxes,
        )
        return [entry.bbox for entry in entries]

    def build_embeddings_from_images(self, image_paths: Iterable[str], *, min_face_size_px: int = 56) -> List[np.ndarray]:
        vectors: List[np.ndarray] = []
        for path in image_paths:
            frame = cv2.imread(str(path))
            if frame is None:
                continue
            vector = self.extract_primary_embedding(frame, min_face_size_px=min_face_size_px)
            if vector is not None:
                vectors.append(vector)
        return vectors

    def extract_embeddings_from_bboxes(
        self,
        frame: np.ndarray,
        bboxes: Iterable[Tuple[int, int, int, int]],
    ) -> List[Optional[np.ndarray]]:
        vectors: List[Optional[np.ndarray]] = []
        for bbox in bboxes:
            vectors.append(self._embedding_from_bbox(frame, tuple(int(v) for v in bbox)))
        return vectors

    def extract_primary_embedding(self, frame: np.ndarray, *, min_face_size_px: int = 56) -> Optional[np.ndarray]:
        faces = self._detect_face_entries(frame, min_face_size_px=min_face_size_px)
        if not faces:
            return None
        face = max(faces, key=lambda entry: entry.bbox[2] * entry.bbox[3])
        return self._embedding_from_face_entry(frame, face)

    def match_known_faces(
        self,
        frame: np.ndarray,
        *,
        min_face_size_px: int = 56,
        person_boxes: Optional[List[Tuple[int, int, int, int]]] = None,
        threshold: float = 0.82,
        min_profile_embeddings: int = 1,
    ) -> List[FaceMatchResult]:
        if frame is None or frame.size == 0:
            return []
        faces = self._detect_face_entries(frame, min_face_size_px=min_face_size_px, roi_boxes=person_boxes)
        results: List[FaceMatchResult] = []
        for face in faces:
            required_samples = max(1, int(min_profile_embeddings))
            profile: Optional[FaceIdentityProfile] = None
            confidence = 0.0

            embedding = self._embedding_from_face_entry(frame, face)
            if embedding is not None:
                profile, confidence = self._match_embedding(
                    embedding,
                    backend=self._active_backend,
                    min_profile_embeddings=required_samples,
                )

            if (
                (profile is None or confidence < float(threshold))
                and self._allow_legacy_fallback
                and self._active_backend == FACE_EMBEDDING_BACKEND_SFACE
            ):
                legacy_embedding = self._legacy_embedding_from_bbox(frame, face.bbox)
                if legacy_embedding is not None:
                    legacy_profile, legacy_confidence = self._match_embedding(
                        legacy_embedding,
                        backend=FACE_EMBEDDING_BACKEND_LEGACY,
                        min_profile_embeddings=required_samples,
                    )
                    if legacy_profile is not None and legacy_confidence > confidence:
                        profile = legacy_profile
                        confidence = legacy_confidence

            if profile is None or confidence < float(threshold):
                continue
            results.append(
                FaceMatchResult(
                    bbox=face.bbox,
                    profile_id=str(profile.profile_id),
                    name=str(profile.name),
                    confidence=float(confidence),
                    friendly=bool(profile.friendly),
                    announce_name=bool(profile.announce_name),
                    cute_gesture=bool(profile.cute_gesture),
                )
            )
        return results

    def _match_embedding(
        self,
        embedding: np.ndarray,
        *,
        backend: Optional[str] = None,
        min_profile_embeddings: int = 1,
    ) -> Tuple[Optional[FaceIdentityProfile], float]:
        best_profile: Optional[FaceIdentityProfile] = None
        best_score = -1.0
        runner_up_score = -1.0
        required_samples = max(1, int(min_profile_embeddings))
        match_backend = str(backend or self._active_backend or FACE_EMBEDDING_BACKEND_LEGACY).strip().lower()
        for profile in self.library.profiles:
            profile_backend = str(getattr(profile, "embedding_backend", FACE_EMBEDDING_BACKEND_LEGACY) or FACE_EMBEDDING_BACKEND_LEGACY)
            if profile_backend != match_backend:
                continue
            scores: List[float] = []
            for raw in profile.embeddings:
                candidate = np.asarray(raw, dtype=np.float32).flatten()
                if candidate.size != embedding.size:
                    continue
                denom = float(np.linalg.norm(embedding) * np.linalg.norm(candidate))
                if denom <= 1e-6:
                    continue
                score = float(np.dot(embedding, candidate) / denom)
                scores.append(score)
            if len(scores) < required_samples:
                continue
            scores.sort(reverse=True)
            support_count = min(max(1, required_samples), len(scores), 3)
            profile_score = sum(scores[:support_count]) / float(support_count)
            if profile_score > best_score:
                runner_up_score = best_score
                best_score = profile_score
                best_profile = profile
            elif profile_score > runner_up_score:
                runner_up_score = profile_score
        if (
            match_backend == FACE_EMBEDDING_BACKEND_SFACE
            and best_profile is not None
            and runner_up_score >= 0.0
            and (best_score - runner_up_score) < float(_SFACE_AMBIGUITY_MARGIN)
        ):
            return None, 0.0
        confidence = self._score_to_confidence(best_score, match_backend) if best_score >= 0.0 else 0.0
        return best_profile, max(0.0, min(1.0, confidence))

    def _score_to_confidence(self, score: float, backend: str) -> float:
        if backend == FACE_EMBEDDING_BACKEND_SFACE:
            clamped = max(0.0, min(1.0, float(score)))
            baseline = float(_SFACE_RECOMMENDED_COSINE_THRESHOLD)
            if clamped <= baseline:
                return 0.82 * (clamped / max(1e-6, baseline))
            return 0.82 + ((clamped - baseline) * (0.18 / max(1e-6, 1.0 - baseline)))
        return (float(score) + 1.0) * 0.5

    def _embedding_from_bbox(self, frame: np.ndarray, bbox: Tuple[int, int, int, int]) -> Optional[np.ndarray]:
        if self._active_backend == FACE_EMBEDDING_BACKEND_SFACE:
            face_entry = self._detect_best_face_entry_for_bbox(frame, bbox)
            if face_entry is not None:
                vector = self._embedding_from_face_entry(frame, face_entry)
                if vector is not None:
                    return vector
            return None
        return self._legacy_embedding_from_bbox(frame, bbox)

    def _embedding_from_face_entry(self, frame: np.ndarray, face: _DetectedFaceEntry) -> Optional[np.ndarray]:
        if self._active_backend == FACE_EMBEDDING_BACKEND_SFACE:
            if face.landmarks is None or self._face_recognizer is None:
                return None
            face_row = self._face_entry_to_sface_row(face)
            try:
                aligned = self._face_recognizer.alignCrop(frame, face_row[:-1])
                features = self._face_recognizer.feature(aligned)
            except Exception:
                features = None
            if features is None:
                return None
            vector = np.asarray(features, dtype=np.float32).flatten()
            if vector.size != _SFACE_EMBEDDING_SIZE:
                return None
            norm = float(np.linalg.norm(vector))
            if norm > 1e-6:
                return vector / norm
            return None
        return self._legacy_embedding_from_bbox(frame, face.bbox)

    def _legacy_embedding_from_bbox(self, frame: np.ndarray, bbox: Tuple[int, int, int, int]) -> Optional[np.ndarray]:
        x, y, w, h = bbox
        if w <= 0 or h <= 0:
            return None
        crop = frame[y:y + h, x:x + w]
        if crop.size == 0:
            return None
        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        resized = cv2.resize(gray, (32, 32), interpolation=cv2.INTER_AREA)
        normalized = resized.astype(np.float32) / 255.0
        dct = cv2.dct(normalized)
        low_freq = dct[:12, :12].flatten()
        histogram = cv2.calcHist([resized], [0], None, [16], [0, 256]).flatten().astype(np.float32)
        vector = np.concatenate([low_freq.astype(np.float32), histogram], axis=0)
        norm = float(np.linalg.norm(vector))
        if norm <= 1e-6:
            return None
        return vector / norm

    def _detect_face_entries(
        self,
        frame: np.ndarray,
        *,
        min_face_size_px: int = 56,
        roi_boxes: Optional[List[Tuple[int, int, int, int]]] = None,
    ) -> List[_DetectedFaceEntry]:
        if frame is None or frame.size == 0:
            return []
        if self._active_backend == FACE_EMBEDDING_BACKEND_SFACE and self._face_detector is not None:
            entries = self._detect_face_entries_sface(
                frame,
                min_face_size_px=min_face_size_px,
                roi_boxes=roi_boxes,
            )
            if entries:
                return entries
        return self._detect_face_entries_legacy(
            frame,
            min_face_size_px=min_face_size_px,
            roi_boxes=roi_boxes,
        )

    def _detect_face_entries_sface(
        self,
        frame: np.ndarray,
        *,
        min_face_size_px: int = 56,
        roi_boxes: Optional[List[Tuple[int, int, int, int]]] = None,
    ) -> List[_DetectedFaceEntry]:
        if self._face_detector is None:
            return []
        search_rois = roi_boxes or [(0, 0, frame.shape[1], frame.shape[0])]
        min_size = max(32, int(min_face_size_px))
        entries: List[_DetectedFaceEntry] = []
        for roi in search_rois:
            x, y, w, h = [int(max(0, v)) for v in roi]
            if w < min_size or h < min_size:
                continue
            sub = frame[y:y + h, x:x + w]
            if sub.size == 0:
                continue
            scale = 1.0
            detect_frame = sub
            longest_edge = max(int(sub.shape[1]), int(sub.shape[0]))
            if longest_edge > _SFACE_MAX_DETECT_DIM:
                scale = float(_SFACE_MAX_DETECT_DIM) / float(longest_edge)
                resized_w = max(1, int(round(float(sub.shape[1]) * scale)))
                resized_h = max(1, int(round(float(sub.shape[0]) * scale)))
                detect_frame = cv2.resize(sub, (resized_w, resized_h), interpolation=cv2.INTER_AREA)
            try:
                self._face_detector.setInputSize((int(detect_frame.shape[1]), int(detect_frame.shape[0])))
                _retval, faces = self._face_detector.detect(detect_frame)
            except Exception:
                continue
            if faces is None:
                continue
            inverse_scale = 1.0 / scale if scale > 0.0 else 1.0
            for row in np.asarray(faces, dtype=np.float32):
                fx, fy, fw, fh = row[:4] * inverse_scale
                if fw < min_size or fh < min_size:
                    continue
                bbox = (x + int(round(fx)), y + int(round(fy)), int(round(fw)), int(round(fh)))
                landmarks = (row[4:14].reshape(5, 2).astype(np.float32) * inverse_scale)
                landmarks[:, 0] += float(x)
                landmarks[:, 1] += float(y)
                score = float(row[14]) if row.size >= 15 else 0.0
                entries.append(
                    _DetectedFaceEntry(
                        bbox=bbox,
                        landmarks=landmarks,
                        score=score,
                    )
                )
        return self._dedupe_face_entries(entries)

    def _detect_face_entries_legacy(
        self,
        frame: np.ndarray,
        *,
        min_face_size_px: int = 56,
        roi_boxes: Optional[List[Tuple[int, int, int, int]]] = None,
    ) -> List[_DetectedFaceEntry]:
        if self._cascade.empty():
            return []
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        search_rois = roi_boxes or [(0, 0, frame.shape[1], frame.shape[0])]
        min_size = max(32, int(min_face_size_px))
        entries: List[_DetectedFaceEntry] = []
        for roi in search_rois:
            x, y, w, h = [int(max(0, v)) for v in roi]
            if w < min_size or h < min_size:
                continue
            sub = gray[y:y + h, x:x + w]
            if sub.size == 0:
                continue
            detected = self._cascade.detectMultiScale(
                sub,
                scaleFactor=1.08,
                minNeighbors=5,
                minSize=(min_size, min_size),
            )
            for fx, fy, fw, fh in detected:
                entries.append(
                    _DetectedFaceEntry(
                        bbox=(x + int(fx), y + int(fy), int(fw), int(fh)),
                        landmarks=None,
                        score=1.0,
                    )
                )
        return self._dedupe_face_entries(entries)

    def _detect_best_face_entry_for_bbox(
        self,
        frame: np.ndarray,
        bbox: Tuple[int, int, int, int],
    ) -> Optional[_DetectedFaceEntry]:
        candidates = self._detect_face_entries_sface(
            frame,
            min_face_size_px=max(32, int(min(bbox[2], bbox[3], 112))),
            roi_boxes=[bbox],
        )
        best_entry: Optional[_DetectedFaceEntry] = None
        best_score = 0.0
        for candidate in candidates:
            score = self._iou(candidate.bbox, bbox)
            if score > best_score:
                best_score = score
                best_entry = candidate
        return best_entry

    @staticmethod
    def _face_entry_to_sface_row(face: _DetectedFaceEntry) -> np.ndarray:
        x, y, w, h = face.bbox
        row = np.empty((15,), dtype=np.float32)
        row[0:4] = [float(x), float(y), float(w), float(h)]
        if face.landmarks is not None:
            row[4:14] = np.asarray(face.landmarks, dtype=np.float32).reshape(10)
        else:
            row[4:14] = 0.0
        row[14] = float(face.score)
        return row

    @staticmethod
    def _dedupe_face_entries(entries: List[_DetectedFaceEntry]) -> List[_DetectedFaceEntry]:
        deduped: List[_DetectedFaceEntry] = []
        for candidate in sorted(
            entries,
            key=lambda item: (float(item.score), item.bbox[2] * item.bbox[3]),
            reverse=True,
        ):
            keep = True
            for existing in deduped:
                if FaceIdentityRuntime._iou(candidate.bbox, existing.bbox) >= 0.35:
                    keep = False
                    break
            if keep:
                deduped.append(candidate)
        return deduped

    @staticmethod
    def _dedupe_boxes(boxes: List[Tuple[int, int, int, int]]) -> List[Tuple[int, int, int, int]]:
        deduped: List[Tuple[int, int, int, int]] = []
        for candidate in sorted(boxes, key=lambda item: item[2] * item[3], reverse=True):
            keep = True
            for existing in deduped:
                if FaceIdentityRuntime._iou(candidate, existing) >= 0.35:
                    keep = False
                    break
            if keep:
                deduped.append(candidate)
        return deduped

    @staticmethod
    def _iou(a: Tuple[int, int, int, int], b: Tuple[int, int, int, int]) -> float:
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
        return inter / union
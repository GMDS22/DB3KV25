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


@dataclass
class FaceIdentityProfile:
    profile_id: str
    name: str
    embeddings: List[List[float]] = field(default_factory=list)
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
        friendly: bool = True,
        announce_name: bool = True,
        cute_gesture: bool = True,
        notes: str = "",
    ) -> Optional[FaceIdentityProfile]:
        cleaned_name = str(name or "").strip()
        vectors = [np.asarray(vector, dtype=np.float32).flatten() for vector in embeddings if vector is not None]
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
                friendly=bool(friendly),
                announce_name=bool(announce_name),
                cute_gesture=bool(cute_gesture),
                notes=str(notes or ""),
                created_at=now,
                updated_at=now,
            )
            self.profiles.append(profile)
            return profile
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
    def __init__(self, library: FaceIdentityLibrary):
        self.library = library
        cascade_path = self._resolve_cascade_path()
        if cascade_path is None:
            self._cascade = cv2.CascadeClassifier()
        else:
            self._cascade = cv2.CascadeClassifier(str(cascade_path))

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

    def detect_faces(
        self,
        frame: np.ndarray,
        *,
        min_face_size_px: int = 56,
        roi_boxes: Optional[List[Tuple[int, int, int, int]]] = None,
    ) -> List[Tuple[int, int, int, int]]:
        if frame is None or frame.size == 0 or self._cascade.empty():
            return []
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        boxes: List[Tuple[int, int, int, int]] = []
        search_rois = roi_boxes or [(0, 0, frame.shape[1], frame.shape[0])]
        min_size = max(32, int(min_face_size_px))
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
                boxes.append((x + int(fx), y + int(fy), int(fw), int(fh)))
        return self._dedupe_boxes(boxes)

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
        faces = self.detect_faces(frame, min_face_size_px=min_face_size_px)
        if not faces:
            return None
        face = max(faces, key=lambda entry: entry[2] * entry[3])
        return self._embedding_from_bbox(frame, face)

    def match_known_faces(
        self,
        frame: np.ndarray,
        *,
        min_face_size_px: int = 56,
        person_boxes: Optional[List[Tuple[int, int, int, int]]] = None,
        threshold: float = 0.82,
    ) -> List[FaceMatchResult]:
        if frame is None or frame.size == 0:
            return []
        faces = self.detect_faces(frame, min_face_size_px=min_face_size_px, roi_boxes=person_boxes)
        results: List[FaceMatchResult] = []
        for bbox in faces:
            embedding = self._embedding_from_bbox(frame, bbox)
            if embedding is None:
                continue
            profile, confidence = self._match_embedding(embedding)
            if profile is None or confidence < float(threshold):
                continue
            results.append(
                FaceMatchResult(
                    bbox=bbox,
                    profile_id=str(profile.profile_id),
                    name=str(profile.name),
                    confidence=float(confidence),
                    friendly=bool(profile.friendly),
                    announce_name=bool(profile.announce_name),
                    cute_gesture=bool(profile.cute_gesture),
                )
            )
        return results

    def _match_embedding(self, embedding: np.ndarray) -> Tuple[Optional[FaceIdentityProfile], float]:
        best_profile: Optional[FaceIdentityProfile] = None
        best_score = -1.0
        for profile in self.library.profiles:
            for raw in profile.embeddings:
                candidate = np.asarray(raw, dtype=np.float32).flatten()
                if candidate.size != embedding.size:
                    continue
                denom = float(np.linalg.norm(embedding) * np.linalg.norm(candidate))
                if denom <= 1e-6:
                    continue
                score = float(np.dot(embedding, candidate) / denom)
                if score > best_score:
                    best_score = score
                    best_profile = profile
        confidence = (best_score + 1.0) * 0.5
        return best_profile, max(0.0, min(1.0, confidence))

    def _embedding_from_bbox(self, frame: np.ndarray, bbox: Tuple[int, int, int, int]) -> Optional[np.ndarray]:
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
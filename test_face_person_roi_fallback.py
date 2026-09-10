"""Regression checks for person-mode face ROI fallback."""

from types import SimpleNamespace
import json

import numpy as np

from app.sentry_v2.sentry_v2_tab import SentryV2TabWidget
from app.sentry_v2.face_identity import (
    FACE_EMBEDDING_BACKEND_LEGACY,
    FACE_EMBEDDING_BACKEND_SFACE,
    FaceIdentityLibrary,
    FaceIdentityRuntime,
)


class _FaceRuntime:
    active_backend = "legacy_dct"

    def __init__(self):
        self.person_boxes = "unset"

    def match_known_faces(self, frame, **kwargs):
        self.person_boxes = kwargs.get("person_boxes")
        return []


def _make_tab(face_runtime):
    tab = SentryV2TabWidget.__new__(SentryV2TabWidget)
    tab.config = SimpleNamespace(
        face_recognition=SimpleNamespace(
            enabled=True,
            min_face_size_px=56,
            recognition_threshold=0.82,
            suppress_known_faces_from_engagement=True,
        )
    )
    tab._face_library = SimpleNamespace(profiles=[object()])
    tab._face_runtime = face_runtime
    tab._last_face_match_eval_s = 0.0
    tab._last_face_person_boxes = []
    tab._last_face_matches = []
    tab._face_person_boxes = lambda objects: [det.bbox for det in objects]
    tab._face_match_refresh_interval_s = lambda frame: 0.0
    tab._face_person_boxes_similar = lambda current, previous: current == previous
    tab._face_identity_required_samples = lambda: 1
    tab._annotate_objects_with_face_matches = lambda objects, matches: list(objects)
    tab._maybe_announce_face_match = lambda match, now: None
    tab._maybe_run_friendly_identity_gesture = lambda match, now: None
    return tab


def test_face_matching_falls_back_to_full_frame_without_person_boxes():
    runtime = _FaceRuntime()
    tab = _make_tab(runtime)

    tab._apply_face_identity_to_objects(
        np.zeros((480, 640, 3), dtype=np.uint8),
        [],
        10.0,
    )

    assert runtime.person_boxes is None


def test_face_matching_keeps_person_roi_when_yolo_has_person_box():
    runtime = _FaceRuntime()
    tab = _make_tab(runtime)
    person = SimpleNamespace(bbox=(100, 60, 120, 240), class_name="person")

    tab._apply_face_identity_to_objects(
        np.zeros((480, 640, 3), dtype=np.uint8),
        [person],
        10.0,
    )

    assert runtime.person_boxes == [person.bbox]


def test_full_frame_sface_detection_scales_minimum_face_size(monkeypatch):
    runtime = FaceIdentityRuntime.__new__(FaceIdentityRuntime)
    runtime._active_backend = FACE_EMBEDDING_BACKEND_SFACE
    runtime._face_detector = SimpleNamespace()
    runtime._sface_candidate_is_plausible = lambda *args, **kwargs: True
    seen = {}

    def detect(_frame):
        seen["input_shape"] = _frame.shape[:2]
        # 30 px in the resized frame represents a 60 px original face.
        return 0, np.array([[100, 40, 30, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.95]], dtype=np.float32)

    runtime._face_detector.setInputSize = lambda size: seen.update(input_size=size)
    runtime._face_detector.detect = detect
    frame = np.zeros((720, 1280, 3), dtype=np.uint8)

    faces = runtime.detect_faces(frame, min_face_size_px=56)

    assert seen["input_shape"] == (360, 640)
    assert faces == [(200, 80, 60, 60)]


def test_face_library_normalizes_legacy_vectors_mislabeled_as_sface(tmp_path):
    path = tmp_path / "faces.json"
    path.write_text(json.dumps({
        "profiles": [{
            "profile_id": "p1",
            "name": "Legacy",
            "embeddings": [[0.0] * 160],
            "embedding_backend": "opencv_sface",
        }],
    }), encoding="utf-8")

    library = FaceIdentityLibrary.load(str(path))

    assert library.profiles[0].embedding_backend == FACE_EMBEDDING_BACKEND_LEGACY

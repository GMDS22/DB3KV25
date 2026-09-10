#!/usr/bin/env python3
"""
Simple test script to verify face detection is working
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from app.sentry_v2.face_identity import FaceIdentityLibrary, FaceIdentityRuntime

def test_face_detection():
    print("Testing face detection initialization...")

    # Initialize face runtime
    face_runtime = FaceIdentityRuntime(
        FaceIdentityLibrary(),
        preferred_backend="opencv_sface",
        detector_model_path="app/models/face/face_detection_yunet_2023mar.onnx",
        recognizer_model_path="app/models/face/face_recognition_sface_2021dec.onnx",
        allow_legacy_fallback=True,
    )

    # Check if backend is configured
    status = face_runtime.backend_status()
    print(f"Face runtime status: {status}")

    if face_runtime.active_backend == "opencv_sface":
        print("✓ Face detection backend is configured successfully!")
        print(f"  Backend: {face_runtime.active_backend}")
        return True
    else:
        print("✗ Face detection backend failed to configure")
        print(f"  Error: {status}")
        return False


def test_sface_confidence_mapping_is_not_overly_permissive():
    runtime = FaceIdentityRuntime(
        FaceIdentityLibrary(),
        preferred_backend="opencv_sface",
        detector_model_path="app/models/face/face_detection_yunet_2023mar.onnx",
        recognizer_model_path="app/models/face/face_recognition_sface_2021dec.onnx",
        allow_legacy_fallback=False,
    )

    # Near the OpenCV SFace recommendation boundary should not be treated as a
    # strong known-face match. The previous mapping inflated ~0.36 similarity
    # into ~0.82 confidence and caused false-positive recognized matches.
    assert runtime._score_to_confidence(0.36, "opencv_sface") < 0.5
    assert runtime._score_to_confidence(0.82, "opencv_sface") > 0.80


def test_sface_runtime_does_not_use_legacy_profiles_by_default():
    runtime = FaceIdentityRuntime(
        FaceIdentityLibrary(),
        preferred_backend="opencv_sface",
        detector_model_path="app/models/face/face_detection_yunet_2023mar.onnx",
        recognizer_model_path="app/models/face/face_recognition_sface_2021dec.onnx",
    )

    assert runtime.supported_profile_backends() == ("opencv_sface",)


def test_face_greeting_does_not_repeat_for_same_person():
    from types import SimpleNamespace

    from app.sentry_v2.face_identity import FaceMatchResult
    from app.sentry_v2.sentry_v2_tab import SentryV2TabWidget

    class DummyTab:
        pass

    tab = DummyTab()
    tab.config = SimpleNamespace(
        face_recognition=SimpleNamespace(announce_known_faces=True),
        sound=SimpleNamespace(
            known_face_hello_once_per_session=True,
            name_announce_cooldown_s=18.0,
            human_voice_enabled=False,
            robot_voice_enabled=True,
        ),
    )
    tab._announced_identity_session_keys = set()
    tab._last_announced_identity_at = {}
    tab._buzzer_suppressed_for_human_voice = lambda: False
    tab._log = lambda *args, **kwargs: None
    tab._speak_human_phrase = lambda phrase: True

    class DummySoundEngine:
        def __init__(self):
            self.calls = 0

        def note_identity_recognized(self, name, friendly=False):
            self.calls += 1

    tab._sound_engine = DummySoundEngine()
    tab._maybe_announce_face_match = SentryV2TabWidget._maybe_announce_face_match.__get__(tab, DummyTab)

    match = FaceMatchResult(
        bbox=(0, 0, 60, 60),
        profile_id="alice-42",
        name="Alice",
        confidence=0.97,
        friendly=True,
        announce_name=True,
        cute_gesture=True,
    )

    tab._maybe_announce_face_match(match, now=100.0)
    tab._maybe_announce_face_match(match, now=101.0)

    assert tab._sound_engine.calls == 1
    assert "alice-42" in tab._announced_identity_session_keys


if __name__ == "__main__":
    success = test_face_detection()
    sys.exit(0 if success else 1)
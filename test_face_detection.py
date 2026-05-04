#!/usr/bin/env python3
"""
Simple test script to verify face detection is working
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from app.sentry_v2.face_identity import FaceIdentityRuntime

def test_face_detection():
    print("Testing face detection initialization...")

    # Initialize face runtime
    face_runtime = FaceIdentityRuntime(
        runtime_root_path=os.path.dirname(__file__),
        config={
            "face_recognition": {
                "enabled": True,
                "backend": "opencv_sface",
                "detector_model_path": "app/models/face/face_detection_yunet_2023mar.onnx",
                "recognizer_model_path": "app/models/face/face_recognition_sface_2021dec.onnx",
                "min_face_size_px": 56
            }
        }
    )

    # Check if backend is configured
    status = face_runtime.get_status()
    print(f"Face runtime status: {status}")

    if status['backend_configured']:
        print("✓ Face detection backend is configured successfully!")
        print(f"  Backend: {status['backend']}")
        print(f"  Profiles loaded: {status['profiles_count']}")
        return True
    else:
        print("✗ Face detection backend failed to configure")
        print(f"  Error: {status.get('error', 'Unknown error')}")
        return False

if __name__ == "__main__":
    success = test_face_detection()
    sys.exit(0 if success else 1)
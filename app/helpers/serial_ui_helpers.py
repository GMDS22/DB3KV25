"""Serial and frame helpers and binder for Movement_Detect_Yolo_me.

This module contains safe wrappers for opening serial ports and
small capture/frame helpers. Call bind_serial_helpers(app) to attach
these as instance-level callables on `app`.
"""
from typing import Any


def _safe_open_serial(app, port, baud, **kwargs):
    try:
        p = str(port) if port is not None else ''
        b = int(baud)
    except Exception:
        try:
            p = str(port)
        except Exception:
            p = ''
        try:
            b = int(str(baud))
        except Exception:
            b = 115200
    try:
        import serial
        return serial.Serial(p, b, **kwargs)
    except Exception as e:
        try:
            # Best-effort log via app if available
            if getattr(app, '_safe_append_log', None):
                try:
                    app._safe_append_log(f"Serial open failed: {e}")
                except Exception:
                    pass
        except Exception:
            pass
        return None


def _cap_read(app):
    cap = getattr(app, 'cap', None)
    if cap is None:
        return False, None
    try:
        return cap.read()
    except Exception:
        return False, None


def _cap_release(app):
    cap = getattr(app, 'cap', None)
    if cap is None:
        return False
    try:
        if hasattr(cap, 'release'):
            cap.release()
            return True
    except Exception:
        pass
    return False


def _ensure_frame(app, frame, default_shape=(480, 640, 3)):
    try:
        import numpy as np
        if frame is None:
            return np.zeros(default_shape, dtype=np.uint8)
        if isinstance(frame, np.ndarray):
            return frame
        try:
            arr = np.asarray(frame)
            if arr is None:
                return np.zeros(default_shape, dtype=np.uint8)
            return arr
        except Exception:
            return np.zeros(default_shape, dtype=np.uint8)
    except Exception:
        # Fallback: return frame unchanged if numpy not available
        return frame


def bind_serial_helpers(app):
    app._safe_open_serial = lambda port, baud, **kwargs: _safe_open_serial(app, port, baud, **kwargs)
    app._cap_read = lambda: _cap_read(app)
    app._cap_release = lambda: _cap_release(app)
    app._ensure_frame = lambda frame, default_shape=(480, 640, 3): _ensure_frame(app, frame, default_shape)
    try:
        app._bound_serial_helpers = True
    except Exception:
        pass

"""UI safety helpers and binder for Movement_Detect_Yolo_me.

These functions are written to be lightweight and avoid heavy imports
at module import time. Call bind_ui_helpers(app) to attach the helpers
as instance-level callables on the provided `app` object.
"""
from typing import Any


def _safe_widget_call(app, attr_name: str, method_name: str, *args, **kwargs):
    w = getattr(app, attr_name, None)
    if w is None:
        return False
    try:
        m = getattr(w, method_name, None)
        if callable(m):
            m(*args, **kwargs)
            return True
    except Exception:
        try:
            setattr(w, method_name, args[0] if args else None)
            return True
        except Exception:
            return False
    return False


def _safe_widget_method_return(app, attr_name: str, method_name: str, default=None, *args, **kwargs):
    w = getattr(app, attr_name, None)
    if w is None:
        return default
    try:
        m = getattr(w, method_name, None)
        if callable(m):
            return m(*args, **kwargs)
    except Exception:
        pass
    return default


def _get_widget_value(app, attr_name: str, default=None):
    val = _safe_widget_method_return(app, attr_name, 'value', None)
    if val is not None:
        return val
    val = _safe_widget_method_return(app, attr_name, 'text', None)
    if val is not None:
        return val
    return default


def _safe_int_widget_value(app, attr_name: str, default=0):
    val = _safe_widget_method_return(app, attr_name, 'value', default)
    try:
        if isinstance(val, int):
            return val
        if isinstance(val, float):
            return int(val)
        if isinstance(val, str):
            try:
                return int(val)
            except Exception:
                try:
                    return int(float(val))
                except Exception:
                    return int(default)
        try:
            return int(str(val))
        except Exception:
            try:
                return int(float(str(val)))
            except Exception:
                return int(default)
    except Exception:
        return int(default)


def _safe_float_widget_value(app, attr_name: str, default=0.0):
    val = _safe_widget_method_return(app, attr_name, 'value', default)
    try:
        if isinstance(val, float):
            return val
        if isinstance(val, int):
            return float(val)
        if isinstance(val, str):
            try:
                return float(val)
            except Exception:
                return float(default)
        try:
            return float(str(val))
        except Exception:
            return float(default)
    except Exception:
        return float(default)


def _safe_append_log(app, text: str):
    try:
        if getattr(app, 'serial_output', None) is not None:
            try:
                _safe_widget_call(app, 'serial_output', 'append', text)
                return True
            except Exception:
                return False
    except Exception:
        pass
    try:
        # Fallback to console so developers can see messages when UI not ready
        print(f"[UI LOG] {text}")
    except Exception:
        pass
    return False


def _safe_connect(app, attr_name: str, signal_name: str, callback):
    w = getattr(app, attr_name, None)
    if w is None:
        try:
            cbname = getattr(callback, '__name__', repr(callback))
            _safe_append_log(app, f"CONNECT FAIL: widget '{attr_name}' missing for signal '{signal_name}' -> {cbname}")
        except Exception:
            pass
        return False
    try:
        sig = getattr(w, signal_name, None)
        if sig is None:
            return False
        try:
            conn = getattr(sig, 'connect', None)
            if callable(conn):
                conn(callback)
                return True
        except Exception:
            pass
        if callable(sig):
            try:
                maybe_sig = sig()
                conn2 = getattr(maybe_sig, 'connect', None)
                if callable(conn2):
                    conn2(callback)
                    return True
            except Exception:
                pass
    except Exception:
        pass
    try:
        cbname = getattr(callback, '__name__', repr(callback))
        _safe_append_log(app, f"CONNECT FAIL: '{attr_name}.{signal_name}' -> {cbname}")
    except Exception:
        pass
    return False


def _safe_connect_path(app, dotted_attr: str, signal_name: str, callback):
    try:
        parts = dotted_attr.split('.') if isinstance(dotted_attr, str) else [dotted_attr]
        obj = app
        for p in parts:
            obj = getattr(obj, p, None)
            if obj is None:
                try:
                    cbname = getattr(callback, '__name__', repr(callback))
                    _safe_append_log(app, f"CONNECT FAIL: path '{dotted_attr}' missing (failed at '{p}') for signal '{signal_name}' -> {cbname}")
                except Exception:
                    pass
                return False
        sig = getattr(obj, signal_name, None)
        if sig is None:
            return False
        try:
            conn = getattr(sig, 'connect', None)
            if callable(conn):
                conn(callback)
                return True
        except Exception:
            pass
        if callable(sig):
            try:
                maybe_sig = sig()
                conn2 = getattr(maybe_sig, 'connect', None)
                if callable(conn2):
                    conn2(callback)
                    return True
            except Exception:
                pass
    except Exception:
        pass
    try:
        cbname = getattr(callback, '__name__', repr(callback))
        _safe_append_log(app, f"CONNECT FAIL: path '{dotted_attr}.{signal_name}' -> {cbname}")
    except Exception:
        pass
    return False


def _safe_current_index(app, attr_name: str, default: int = 0):
    try:
        obj = getattr(app, attr_name, None)
        if obj is None:
            return default
        try:
            return int(obj.currentIndex())
        except Exception:
            try:
                return int(obj.currentIndex())
            except Exception:
                return default
    except Exception:
        return default


def _qt_enum(name: str, fallback: int):
    try:
        from PyQt5.QtCore import Qt
        return getattr(Qt, name, fallback)
    except Exception:
        return fallback


def _qt_dock_area(name: str, fallback):
    try:
        from PyQt5.QtCore import Qt as _Qt
        return getattr(_Qt, name, fallback)
    except Exception:
        return fallback


def _qt_orientation(name: str, fallback):
    try:
        from PyQt5.QtCore import Qt as _Qt
        return getattr(_Qt, name, fallback)
    except Exception:
        return fallback


def validate_required_widgets(app, widget_names):
    """
    Validate that all required widgets exist on the app instance.
    
    Args:
        app: The main application instance
        widget_names: List of widget attribute names to validate
    
    Returns:
        bool: True if all widgets exist, False otherwise
    """
    try:
        from helpers.logger import get_logger
        logger = get_logger()
    except ImportError:
        logger = None
    
    missing = []
    for name in widget_names:
        if not hasattr(app, name) or getattr(app, name, None) is None:
            missing.append(name)
    
    if missing:
        msg = f"Missing required widgets: {', '.join(missing)}"
        if logger:
            logger.critical(msg)
        else:
            print(f"CRITICAL: {msg}")
        try:
            _safe_append_log(app, f"CRITICAL: {msg}")
        except Exception:
            pass
        return False
    return True


def bind_ui_helpers(app):
    """Attach lightweight UI helper callables to the given app instance.

    After calling this, the app will expose the same names previously
    defined as instance methods (e.g. app._safe_widget_call(...)).
    """
    app._safe_widget_call = lambda attr_name, method_name, *args, **kwargs: _safe_widget_call(app, attr_name, method_name, *args, **kwargs)
    app._safe_widget_method_return = lambda attr_name, method_name, default=None, *args, **kwargs: _safe_widget_method_return(app, attr_name, method_name, default, *args, **kwargs)
    app._get_widget_value = lambda attr_name, default=None: _get_widget_value(app, attr_name, default)
    app._safe_int_widget_value = lambda attr_name, default=0: _safe_int_widget_value(app, attr_name, default)
    app._safe_float_widget_value = lambda attr_name, default=0.0: _safe_float_widget_value(app, attr_name, default)
    app._safe_append_log = lambda text: _safe_append_log(app, text)
    app._safe_connect = lambda attr_name, signal_name, callback: _safe_connect(app, attr_name, signal_name, callback)
    app._safe_connect_path = lambda dotted_attr, signal_name, callback: _safe_connect_path(app, dotted_attr, signal_name, callback)
    app._safe_current_index = lambda attr_name, default=0: _safe_current_index(app, attr_name, default)
    app._qt_enum = lambda name, fallback: _qt_enum(name, fallback)
    app._qt_dock_area = lambda name, fallback: _qt_dock_area(name, fallback)
    app._qt_orientation = lambda name, fallback: _qt_orientation(name, fallback)
    app.validate_required_widgets = lambda widget_names: validate_required_widgets(app, widget_names)
    try:
        app._bound_ui_helpers = True
    except Exception:
        pass

#!/usr/bin/env python3
"""
DADBOT v4 Portable - Application Entry Point
Launches the main turret control application with YOLO detection
"""

import sys
import os
import runpy
import warnings
import io
import traceback
from datetime import datetime

# Suppress PyQt5 warnings about unregistered signal types (non-critical)
warnings.filterwarnings('ignore', category=DeprecationWarning)
warnings.filterwarnings('ignore', message='.*QTextCursor.*')
warnings.filterwarnings('ignore', message='.*Cannot queue arguments.*')


def _configure_ml_runtime_env() -> None:
    """Configure a stable CPU-first ML runtime environment on Windows.

    Prevents common torch/ultralytics DLL init failures (WinError 1114) caused
    by OpenMP/MKL runtime conflicts in mixed Qt/OpenCV environments.
    """
    try:
        os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")
        os.environ.setdefault("OMP_NUM_THREADS", "1")
        os.environ.setdefault("MKL_NUM_THREADS", "1")
        os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")
        # CPU-first by default for maximum compatibility.
        os.environ.setdefault("CUDA_VISIBLE_DEVICES", "")
    except Exception:
        pass

# Redirect Qt debug output to suppress non-critical messages
class QuietIOWrapper(io.TextIOWrapper):
    """Suppresses Qt debug/warning messages but passes through real errors"""
    def __init__(self, original_stderr):
        self.original = original_stderr
        self.skip_patterns = [
            'QObject::connect',
            'Cannot queue arguments',
            'QTextCursor',
            'Could not find the requested feature',
            'QFontDatabase',
            'Could not load the Qt platform',
            'Unknown property in attribute'
        ]

    def write(self, s):
        if any(skip in s for skip in self.skip_patterns):
            return len(s)
        return self.original.write(s)

    def flush(self):
        self.original.flush()

# Apply stderr filter
sys.stderr = QuietIOWrapper(sys.stderr)


def _preload_torch_runtime() -> bool:
    """Preload torch before Qt/OpenCV-heavy app imports.

    On some Windows setups, importing torch after cv2/PyQt may fail with
    WinError 1114 (c10.dll init). Preloading torch early in the launcher
    stabilizes runtime loading without changing app logic.
    """
    try:
        import torch  # noqa: F401

        return True
    except Exception as e:
        try:
            err = getattr(sys.stderr, "original", sys.__stderr__)
            err.write(f"[BOOT] Torch preload failed: {e}\n")
        except Exception:
            pass
        return False


def _install_crash_logger() -> str:
    """Install a crash logger so PyQt slot exceptions produce a traceback."""
    repo_root = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(repo_root, "logs")
    try:
        os.makedirs(log_dir, exist_ok=True)
    except Exception:
        log_dir = repo_root

    log_path = os.path.join(
        log_dir, f"crash_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    )

    original_stderr = getattr(sys.stderr, "original", sys.__stderr__)

    def _excepthook(exc_type, exc, tb):
        try:
            header = (
                "\n" + "=" * 60 + "\n"
                "UNHANDLED PYTHON EXCEPTION\n"
                + "=" * 60 + "\n\n"
            )
            try:
                original_stderr.write(header)
                traceback.print_exception(exc_type, exc, tb, file=original_stderr)
            except Exception:
                pass
        finally:
            try:
                with open(log_path, "w", encoding="utf-8", errors="replace") as f:
                    f.write("UNHANDLED PYTHON EXCEPTION\n\n")
                    traceback.print_exception(exc_type, exc, tb, file=f)
            except Exception:
                pass

    sys.excepthook = _excepthook
    return log_path


# Add app directory to path
app_dir = os.path.join(os.path.dirname(__file__), 'app')
if app_dir not in sys.path:
    sys.path.insert(0, app_dir)

# Change to app directory so relative paths work
os.chdir(app_dir)

print("=" * 60)
try:
    from db3k_meta import get_app_title
    print(f"{get_app_title()} - Starting Application")
except Exception:
    print("DADBOT v4 Portable - Starting Application")
print("=" * 60)

# Install crash logger before running PyQt main
crash_log_path = _install_crash_logger()

# Configure runtime environment before any heavy ML imports.
_configure_ml_runtime_env()

# Preload torch runtime before app imports (import-order stability fix)
_preload_torch_runtime()

# Run main application
if __name__ == "__main__":
    
    try:
        runpy.run_path('MAIN_FILE_SINGLE_CAM.py', run_name='__main__')
    except SystemExit:
        raise
    except Exception:
        try:
            err = getattr(sys.stderr, "original", sys.__stderr__)
            err.write(f"\n[CRASH] Full traceback written to: {crash_log_path}\n")
            traceback.print_exc(file=err)
        except Exception:
            pass
        raise

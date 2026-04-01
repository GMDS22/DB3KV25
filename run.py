#!/usr/bin/env python3
"""
DADBOT v4 Portable - Application Entry Point
Launches the main turret control application with YOLO detection
"""

import sy
import runpy
import warnings
import io
import traceback
import subprocess
from datetime import datetime
import ctypes
from ctypes import wintypes

# Suppress PyQt5 warnings about unregistered signal types (non-critical)
warnings.filterwarnings('ignore', category=DeprecationWarning)
warnings.filterwarnings('ignore', message='.*QTextCursor.*')
warnings.filterwarnings('ignore', message='.*Cannot queue arguments.*')


_single_instance_mutex = None


def _is_child_of_same_launcher() -> bool:
    if os.name != "nt":
        return False
    try:
        parent_pid = int(os.getppid())
    except Exception:
        return False
    if parent_pid <= 0:
        return False

    try:
        current_path = os.path.normcase(os.path.abspath(__file__))
        current_name = os.path.basename(current_path)
        cmd = (
            f'Get-CimInstance Win32_Process -Filter "ProcessId = {parent_pid}" | '
            'Select-Object -ExpandProperty CommandLine | Out-String'
        )
        proc = subprocess.run(
            ["powershell", "-NoProfile", "-Command", cmd],
            capture_output=True,
            text=True,
            timeout=2.0,
        )
        parent_cmd = (proc.stdout or "").strip()
        if not parent_cmd:
            return False
        parent_norm = os.path.normcase(parent_cmd)
        return (current_path in parent_norm) or (current_name in parent_norm and "python" in parent_norm)
    except Exception:
        return False


def _enforce_single_instance() -> None:
    """Prevent duplicate Windows GUI instances from fighting over COM ports."""
    global _single_instance_mutex
    if os.name != "nt":
        return
    if _is_child_of_same_launcher():
        try:
            err = getattr(sys.stderr, "original", sys.__stderr__)
            err.write("[BOOT] Duplicate child launcher detected. Exiting child run.py process.\n")
        except Exception:
            pass
        raise SystemExit(0)
    try:
        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        kernel32.CreateMutexW.argtypes = [wintypes.LPVOID, wintypes.BOOL, wintypes.LPCWSTR]
        kernel32.CreateMutexW.restype = wintypes.HANDLE
        mutex_name = "Local\\DB3000V4_MAIN_APP_SINGLE_INSTANCE"
        ctypes.set_last_error(0)
        handle = kernel32.CreateMutexW(None, False, mutex_name)
        last_error = ctypes.get_last_error()
        if not handle:
            return
        _single_instance_mutex = handle
        if last_error == 183:
            try:
                err = getattr(sys.stderr, "original", sys.__stderr__)
                err.write("[BOOT] Another DB3000 app instance is already running. Exiting duplicate launcher.\n")
            except Exception:
                pass
            raise SystemExit(0)
    except SystemExit:
        raise
    except Exception:
        pass


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

# Run Smart Sentry v2
if __name__ == "__main__":
    try:
        import run_sentry_v2
        raise SystemExit(run_sentry_v2.main())
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

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
# QTextCursor cannot be queued through signals, but functionality still works
warnings.filterwarnings('ignore', category=DeprecationWarning)
warnings.filterwarnings('ignore', message='.*QTextCursor.*')
warnings.filterwarnings('ignore', message='.*Cannot queue arguments.*')

# Redirect Qt debug output to suppress non-critical messages
class QuietIOWrapper(io.TextIOWrapper):
    """Suppresses Qt debug/warning messages but passes through real errors"""
    def __init__(self, original_stderr):
        self.original = original_stderr
        # Comprehensive list of PyQt5/Qt warnings to suppress (cosmetic, non-functional)
        self.skip_patterns = [
            'QObject::connect',           # Signal connection warnings
            'Cannot queue arguments',     # Type queueing issues
            'QTextCursor',               # Text cursor signal issues
            'Could not find the requested feature',  # Qt feature warnings
            'QFontDatabase',             # Font database warnings
            'Could not load the Qt platform',  # Platform plugin warnings
            'Unknown property in attribute'  # Property warnings
        ]
    
    def write(self, s):
        # Only show actual errors, suppress Qt/PyQt5 cosmetic warnings
        if any(skip in s for skip in self.skip_patterns):
            return len(s)
        return self.original.write(s)
    
    def flush(self):
        self.original.flush()

# Apply the filter
sys.stderr = QuietIOWrapper(sys.stderr)


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
            msg = "\n".join(
                [
                    "\n" + "=" * 60,
                    "UNHANDLED PYTHON EXCEPTION (see traceback below)",
                    "=" * 60,
                    "",
                ]
            )
            try:
                original_stderr.write(msg)
            except Exception:
                pass
            try:
                traceback.print_exception(exc_type, exc, tb, file=original_stderr)
            except Exception:
                pass
        finally:
            # Always write to file too, even if stderr is filtered
            try:
                with open(log_path, "w", encoding="utf-8", errors="replace") as f:
                    f.write("UNHANDLED PYTHON EXCEPTION\n")
                    traceback.print_exception(exc_type, exc, tb, file=f)
            except Exception:
                pass

    sys.excepthook = _excepthook
    return log_path

# Add app directory to path so modules can be imported
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

# Install crash logger before running PyQt main.
crash_log_path = _install_crash_logger()

# Import and run the main application module
if __name__ == "__main__":
    # Execute the main file as a script to trigger its __main__ block
    try:
        runpy.run_path('MAIN_FILE_SINGLE_CAM.py', run_name='__main__')
    except SystemExit:
        raise
    except Exception:
        # Slot exceptions sometimes only show "Unhandled Python exception".
        # Ensure we emit a traceback and point to the crash log.
        try:
            err = getattr(sys.stderr, "original", sys.__stderr__)
            err.write(f"\n[CRASH] Full traceback written to: {crash_log_path}\n")
        except Exception:
            pass
        traceback.print_exc(file=getattr(sys.stderr, "original", sys.__stderr__))
        raise

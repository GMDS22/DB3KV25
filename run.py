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

# Import and run the main application module
if __name__ == "__main__":
    # Execute the main file as a script to trigger its __main__ block
    runpy.run_path('MAIN_FILE_SINGLE_CAM.py', run_name='__main__')

#!/usr/bin/env python3
"""
Quick test to verify the app starts without crashing
"""
import sys
import os

# Add app directory
app_dir = os.path.join(os.path.dirname(__file__), 'app')
sys.path.insert(0, app_dir)
os.chdir(app_dir)

print("[TEST] Importing PyQt5...")
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

print("[TEST] Creating QApplication...")
app = QApplication(sys.argv)

print("[TEST] Importing TrackingApp...")
from MAIN_FILE_SINGLE_CAM import TrackingApp

print("[TEST] Creating TrackingApp instance...")
try:
    ex = TrackingApp()
    print("[TEST] ✓ TrackingApp created successfully")
except Exception as e:
    print(f"[TEST] ✗ Failed to create TrackingApp: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("[TEST] Showing window...")
try:
    if not ex.isMaximized():
        ex.show()
    print("[TEST] ✓ Window shown")
except Exception as e:
    print(f"[TEST] ✗ Failed to show window: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Schedule app close after 2 seconds
print("[TEST] Scheduling app close in 2 seconds...")
QTimer.singleShot(2000, app.quit)

print("[TEST] Entering event loop...")
try:
    sys.exit(app.exec_())
except Exception as e:
    print(f"[TEST] ✗ Event loop error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

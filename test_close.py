
import sys
import os

# Bypass the quiet wrapper in run.py
import builtins
orig_print = builtins.print

import run
sys.stderr = sys.__stderr__

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

app = QApplication.instance()
if app is None:
    app = QApplication([])

window = run._create_minimal_sentry_window()
run._attach_reopen_handler(window, run._show_launcher)

print('Closing window...')
window.close()

def finalize():
    print('Current top level widgets:', [w.objectName() for w in QApplication.topLevelWidgets()])
    app.quit()

QTimer.singleShot(500, finalize)
sys.exit(app.exec_())

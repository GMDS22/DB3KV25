import sys
import time
import os
import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

# Ensure app/ is on sys.path so local imports inside MAIN_FILE_SINGLE_CAM work
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))
from MAIN_FILE_SINGLE_CAM import TrackingApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    print('[TEST] QApplication created')
    win = TrackingApp()
    win.show()
    print('[TEST] TrackingApp shown')

    # Set COM port and baud to simulate user selection
    try:
        if hasattr(win, 'com_port_input'):
            try:
                win.com_port_input.setText('COM3')
            except Exception:
                pass
        if hasattr(win, 'baud_rate_input'):
            try:
                win.baud_rate_input.setValue(115200)
            except Exception:
                pass
    except Exception:
        pass

    # Call connect_serial after 1 second
    QTimer.singleShot(1000, lambda: (print('[TEST] Calling connect_serial()'), win.connect_serial()))

    # Quit after 8 seconds
    QTimer.singleShot(8000, lambda: (print('[TEST] Quitting app'), app.quit()))

    sys.exit(app.exec_())


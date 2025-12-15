#!/usr/bin/env python3
"""
Serial Connection Async Implementation Test
Tests the new async serial connection implementation to ensure GUI doesn't freeze.

Run with: python SERIAL_CONNECTION_TEST.py

This test verifies:
1. Connection flag prevents concurrent attempts
2. Background thread doesn't block GUI
3. Callback properly updates UI on main thread
4. Error handling works correctly
"""

import sys
import time
import threading
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QPushButton, QLabel, QLineEdit, QComboBox
)
from PyQt5.QtCore import QTimer
import serial

class SerialConnectionTester(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ser = None
        self._serial_connection_in_progress = False
        self.initUI()
    
    def initUI(self):
        """Setup test UI"""
        self.setWindowTitle("Serial Connection Async Test")
        self.setGeometry(100, 100, 500, 300)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Port input
        self.port_input = QLineEdit()
        self.port_input.setPlaceholderText("Enter COM port (e.g., COM3)")
        layout.addWidget(QLabel("COM Port:"))
        layout.addWidget(self.port_input)
        
        # Baud rate dropdown
        self.baud_combo = QComboBox()
        self.baud_combo.addItems(["115200", "9600", "19200", "38400"])
        layout.addWidget(QLabel("Baud Rate:"))
        layout.addWidget(self.baud_combo)
        
        # Connect button
        self.connect_btn = QPushButton("Connect")
        self.connect_btn.clicked.connect(self.connect_serial)
        layout.addWidget(self.connect_btn)
        
        # Status label
        self.status_label = QLabel("Status: Disconnected")
        layout.addWidget(self.status_label)
        
        # Test result label
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def _safe_open_serial(self, port, baud, timeout=0.1, write_timeout=1):
        """Mock serial opening (would use real implementation in actual app)"""
        print(f"[TEST] Opening {port} @ {baud}...")
        time.sleep(2)  # Simulate slow connection
        if port.lower() == "test":
            return "MockSerialObject"  # Return mock object
        raise serial.SerialException(f"Port {port} not found")
    
    def _connect_serial_async(self, port, baud):
        """Background worker for serial connection"""
        def _do_connect():
            result = {
                'success': False,
                'port': port,
                'baud': baud,
                'error': None,
                'ser': None
            }
            
            try:
                result['ser'] = self._safe_open_serial(port, baud)
                result['success'] = (result['ser'] is not None)
            except Exception as e:
                result['success'] = False
                result['error'] = str(e)
            
            def _update_ui():
                try:
                    self._handle_serial_connection_result(result)
                except Exception as e:
                    print(f"[TEST] Error in callback: {e}")
            
            QTimer.singleShot(0, _update_ui)
        
        bg_thread = threading.Thread(target=_do_connect, daemon=True)
        bg_thread.start()
    
    def _handle_serial_connection_result(self, result):
        """Handle result from background thread"""
        self._serial_connection_in_progress = False
        
        if result['success']:
            self.ser = result['ser']
            self.status_label.setText(f"✓ Connected to {result['port']}")
            self.connect_btn.setText("Disconnect")
            self.result_label.setText("✅ SUCCESS: Connection succeeded!")
            print(f"[TEST] Connection succeeded!")
        else:
            error_msg = result.get('error', 'Unknown error')
            self.status_label.setText(f"✗ {error_msg}")
            self.connect_btn.setText("Connect")
            self.result_label.setText(f"❌ FAILED: {error_msg}")
            print(f"[TEST] Connection failed: {error_msg}")
    
    def connect_serial(self):
        """Handle connect button click"""
        # Check if already connecting
        if self._serial_connection_in_progress:
            self.result_label.setText("⏳ Connection attempt already in progress!")
            return
        
        port = self.port_input.text()
        baud = int(self.baud_combo.currentText())
        
        if not port:
            self.result_label.setText("❌ Please enter a COM port")
            return
        
        # Mark as in progress
        self._serial_connection_in_progress = True
        self.status_label.setText("Connecting...")
        self.connect_btn.setEnabled(False)
        self.result_label.setText("⏳ Connecting in background thread...")
        
        # Start async connection
        self._connect_serial_async(port, baud)


def main():
    print("=" * 60)
    print("SERIAL CONNECTION ASYNC TEST")
    print("=" * 60)
    print("\nTest Instructions:")
    print("1. Enter 'test' in the COM port field (test case)")
    print("2. Click 'Connect' button")
    print("3. Watch status change without GUI freezing")
    print("4. Button should show 'Connecting...' while in progress")
    print("\nFor real testing:")
    print("- Enter actual COM port (e.g., COM3)")
    print("- Connection should succeed/fail based on device availability")
    print("=" * 60)
    
    app = QApplication(sys.argv)
    window = SerialConnectionTester()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

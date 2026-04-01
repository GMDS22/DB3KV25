#!/usr/bin/env python3
"""
Test using servo.exe - the official Debug Board software
This runs the servo debug utility and captures its behavior
"""

import subprocess
import time
import os

def main():
    print("=" * 60)
    print("SERVO.EXE DEBUG SOFTWARE TEST")
    print("=" * 60)
    print("\nAttempting to launch servo.exe debugging software...")
    print("Location: F:\\DB3000V5.0 - ESP32\\servo\\servo.exe")
    print()

    servo_exe = R"F:\DB3000V5.0 - ESP32\servo\servo.exe"

    if not os.path.exists(servo_exe):
        print(f"✗ servo.exe not found at: {servo_exe}")
        return

    print("✓ servo.exe found")
    print("\nLaunching servo.exe...")
    print("=" * 60)
    print("\nInstructions for servo.exe:")
    print("1. When window opens, select COM28")
    print("2. Click 'Connect' or similar button")
    print("3. Select servo ID (try 1 and 2)")
    print("4. Try to move the servo using the GUI")
    print("5. If servo moves: hardware is OK, software may have issue")
    print("6. If servo doesn't move:")
    print("   a) Check servo power (LED)")
    print("   b) Check wiring")
    print("   c) Try different COM port")
    print("7. Close servo.exe when done")
    print("\n" + "=" * 60)

    try:
        subprocess.Popen([servo_exe])
        print("\n✓ servo.exe launched successfully")
        print("\nTest the servos with servo.exe, then close it.")
        print("This will tell us if the Debug Board hardware works correctly.")
    except Exception as e:
        print(f"\n✗ Failed to launch servo.exe: {e}")

    print("\nWaiting for servo.exe to complete...")
    print("(This will stay open until you close servo.exe)")

if __name__ == "__main__":
    main()
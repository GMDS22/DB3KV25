#!/usr/bin/env python3
"""
Test script to verify trigger/fire commands are being sent correctly.
This bypasses the UI and directly tests the serial command path.

Expected behavior (Projectile mode, Dual Port):
1. Connect to COM8 (Nano)
2. Send: F1L0R0G0S0M1\n  (fire=1, safety=armed, mode=projectile)
3. Arduino should move trigger servo from 90° to 120°
4. Send: F0L0R0G0S0M1\n  (fire=0)
5. Arduino should return servo to 90°
"""

import serial
import time
import sys

# Match user's settings
NANO_PORT = "COM8"
BAUD = 115200

def main():
    print("=" * 60)
    print("TRIGGER FIRE TEST - Direct Serial Command")
    print("=" * 60)
    
    try:
        ser = serial.Serial(NANO_PORT, BAUD, timeout=1)
        time.sleep(2)  # Wait for Arduino reset
        print(f"✓ Connected to {NANO_PORT}")
    except Exception as e:
        print(f"✗ FAILED to connect to {NANO_PORT}: {e}")
        sys.exit(1)
    
    # Drain any startup messages
    while ser.in_waiting:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line:
            print(f"  [ARDUINO] {line}")
    
    print()
    
    # Step 1: Ensure safety is ARMED (S0) and mode is Projectile (M1)
    print("Step 1: ARM safety and set Projectile mode...")
    cmd = "F0L0R0G0S0M1\n"
    print(f"  Sending: {cmd.strip()}")
    ser.write(cmd.encode())
    time.sleep(0.2)
    while ser.in_waiting:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line:
            print(f"  [ARDUINO] {line}")
    
    print()
    
    # Step 2: Send FIRE command
    print("Step 2: FIRE! (servo should move to 120°)")
    cmd = "F1L0R0G0S0M1\n"
    print(f"  Sending: {cmd.strip()}")
    ser.write(cmd.encode())
    time.sleep(0.5)  # Give servo time to move
    while ser.in_waiting:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line:
            print(f"  [ARDUINO] {line}")
    
    print()
    input(">>> Did the trigger servo move? Press ENTER to release fire...")
    
    # Step 3: Release fire
    print("Step 3: Release fire (servo should return to 90°)")
    cmd = "F0L0R0G0S0M1\n"
    print(f"  Sending: {cmd.strip()}")
    ser.write(cmd.encode())
    time.sleep(0.5)
    while ser.in_waiting:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line:
            print(f"  [ARDUINO] {line}")
    
    print()
    
    # Step 4: Test LED relay
    print("Step 4: Test LED relay (should turn ON)")
    cmd = "L1\n"
    print(f"  Sending: {cmd.strip()}")
    ser.write(cmd.encode())
    time.sleep(0.3)
    while ser.in_waiting:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line:
            print(f"  [ARDUINO] {line}")
    
    input(">>> LED relay should be ON. Press ENTER to turn OFF...")
    
    cmd = "L0\n"
    print(f"  Sending: {cmd.strip()}")
    ser.write(cmd.encode())
    time.sleep(0.2)
    while ser.in_waiting:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line:
            print(f"  [ARDUINO] {line}")
    
    print()
    
    # Step 5: Test LASER relay
    print("Step 5: Test LASER relay (should turn ON)")
    cmd = "R1\n"
    print(f"  Sending: {cmd.strip()}")
    ser.write(cmd.encode())
    time.sleep(0.3)
    while ser.in_waiting:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line:
            print(f"  [ARDUINO] {line}")
    
    input(">>> LASER relay should be ON. Press ENTER to turn OFF...")
    
    cmd = "R0\n"
    print(f"  Sending: {cmd.strip()}")
    ser.write(cmd.encode())
    time.sleep(0.2)
    while ser.in_waiting:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line:
            print(f"  [ARDUINO] {line}")
    
    print()
    print("=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)
    print()
    print("If the servo and relays responded correctly, the Arduino firmware is OK.")
    print("The problem is in the Python app's send_serial_command() function.")
    print()
    
    ser.close()

if __name__ == "__main__":
    main()

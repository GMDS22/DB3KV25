#!/usr/bin/env python3
"""
Comprehensive Servo Test for Debug Board
Tests servo connectivity, IDs, and movement on COM28
"""

import sys
import os
import time
import serial

# Add app directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from sentry_v2.sentry_v2_comm import SentryV2Comm

def test_servo_connectivity():
    """Test basic connectivity to Debug Board"""
    print("=== Testing Debug Board Connectivity ===")

    comm = SentryV2Comm()

    print("Connecting to Debug Board on COM28 (mode 2)...")
    connected = comm.connect(
        mode=2,  # ESP32 WiFi + Debug Board USB
        debug_port="COM28",
        esp32_port=""  # No ESP32 serial port
    )
    print(f"Connection result: {connected}")

    if not connected:
        print(f"Connection failed: {comm.get_last_error()}")
        return None

    print("Connection successful!")
    return comm

def test_servo_ids(comm):
    """Test different servo IDs to find which ones work"""
    print("\n=== Testing Servo IDs ===")

    # Test IDs 1-10
    for servo_id in range(1, 11):
        print(f"\nTesting Servo ID {servo_id}:")

        # Try to ping the servo
        try:
            comm.pan_servo_id = servo_id
            comm.tilt_servo_id = servo_id

            # Send a ping first
            ping_result = comm._try_ping(comm._bus_ser, servo_id, timeout_s=0.5)
            if ping_result:
                print(f"  ✓ Servo ID {servo_id} responded to ping!")
            else:
                print(f"  ✗ Servo ID {servo_id} no response to ping")

            # Try movement
            print(f"  Sending movement to ID {servo_id}...")
            result = comm.send_movement(0, 0)  # Center position
            time.sleep(0.5)
            result = comm.send_movement(45, 30)  # Move to 45°, 30°
            time.sleep(1.0)
            result = comm.send_movement(0, 0)  # Back to center
            time.sleep(0.5)

            print(f"  Movement commands sent (check if servo moved)")

        except Exception as e:
            print(f"  Error testing ID {servo_id}: {e}")

def test_large_movements(comm):
    """Test with large movements to make sure they're visible"""
    print("\n=== Testing Large Movements ===")

    # Assume default IDs 1 and 2, but test with large movements
    print("Testing with large movements (pan=1, tilt=2)...")

    positions = [
        (0, 0),      # Center
        (90, 45),    # Right/up
        (-90, -45),  # Left/down
        (0, 0),      # Back to center
    ]

    for i, (pan, tilt) in enumerate(positions):
        print(f"Position {i+1}: Pan={pan}°, Tilt={tilt}°")
        result = comm.send_movement(pan, tilt)
        print(f"  Send result: {result}")
        time.sleep(2.0)  # Wait longer to see movement

def main():
    print("Comprehensive Servo Test for Debug Board")
    print("=" * 50)

    # Create one comm instance and connect once
    comm = SentryV2Comm()

    # Test 1: Basic connectivity
    comm = test_servo_connectivity()
    if comm is None:
        print("Cannot proceed without Debug Board connection")
        return

    # Test 2: Try different servo IDs
    test_servo_ids(comm)

    # Test 3: Large movements
    test_large_movements(comm)

    # Clean up
    comm.disconnect()

    print("\n" + "=" * 50)
    print("Test complete. Check if you observed any servo movement.")
    print("If no movement was seen:")
    print("1. Check servo power (red LED should be on)")
    print("2. Check wiring (signal, power, ground)")
    print("3. Try different servo IDs")
    print("4. Check servo voltage (should be 6-8.4V)")

if __name__ == "__main__":
    main()
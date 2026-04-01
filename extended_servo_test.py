#!/usr/bin/env python3
"""
Extended Servo ID Test - Check wider range of IDs
Tests servo IDs 1-50 to find which ones respond
"""

import sys
import os
import time

# Add app directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from sentry_v2.sentry_v2_comm import SentryV2Comm

def test_extended_servo_ids():
    """Test servo IDs from 1-50 to find which ones work"""
    print("Extended Servo ID Test (1-50)")
    print("=" * 40)

    comm = SentryV2Comm()

    if not comm.connect(mode=2, debug_port="COM28", esp32_port=""):
        print("Failed to connect to Debug Board")
        return

    print("Testing servo IDs 1-50...")
    print("Watch the servos - any movement indicates a working ID")
    print()

    responsive_ids = []

    for servo_id in range(1, 51):
        print(f"Testing ID {servo_id:2d}: ", end="", flush=True)

        # Try to ping the servo
        try:
            ping_result = comm._try_ping(comm._bus_ser, servo_id, timeout_s=0.2)
            if ping_result and len(ping_result) > 0:
                print("✓ RESPONDS TO PING!")
                responsive_ids.append(servo_id)
            else:
                print("✗ no response")

            # Try movement anyway (sometimes servos respond to commands but not pings)
            comm.pan_servo_id = servo_id
            comm.tilt_servo_id = servo_id

            # Quick movement test
            result = comm.send_movement(30, 15)  # Small movement
            time.sleep(0.5)
            result = comm.send_movement(0, 0)   # Back to center
            time.sleep(0.3)

        except Exception as e:
            print(f"Error: {e}")

    print("\n" + "=" * 40)
    print("Summary:")
    if responsive_ids:
        print(f"Servos responded to ping: {responsive_ids}")
        print("These are likely your correct servo IDs!")
    else:
        print("No servos responded to ping commands.")
        print("But they might still respond to movement commands.")
        print("Try running the Sentry V2 app and use manual controls.")

    comm.disconnect()

def test_specific_ids(ids_to_test):
    """Test specific servo IDs with detailed feedback"""
    print(f"\nTesting specific IDs: {ids_to_test}")
    print("-" * 30)

    comm = SentryV2Comm()

    if not comm.connect(mode=2, debug_port="COM28", esp32_port=""):
        print("Failed to connect")
        return

    for servo_id in ids_to_test:
        print(f"\n--- Detailed test for Servo ID {servo_id} ---")

        comm.pan_servo_id = servo_id
        comm.tilt_servo_id = servo_id

        # Test ping
        print("Ping test: ", end="")
        ping_result = comm._try_ping(comm._bus_ser, servo_id, timeout_s=0.5)
        if ping_result:
            print("✓ Servo responds to ping")
        else:
            print("✗ No ping response")

        # Test movement sequence
        print("Movement test:")
        positions = [(0, 0), (45, 30), (-45, -30), (0, 0)]

        for i, (pan, tilt) in enumerate(positions):
            print(f"  Position {i+1}: Pan={pan:3d}°, Tilt={tilt:3d}° - ", end="")
            result = comm.send_movement(pan, tilt)
            print("Command sent")
            time.sleep(1.5)  # Wait to see movement

        print(f"ID {servo_id} test complete - did you see movement?")

    comm.disconnect()

def main():
    # First do extended scan
    test_extended_servo_ids()

    # Then test some common alternative IDs
    common_alternatives = [10, 11, 12, 20, 21, 22, 100, 101, 102]
    test_specific_ids(common_alternatives)

    print("\n" + "=" * 50)
    print("Extended servo test complete!")
    print("If you saw movement during any test:")
    print("1. Note the servo ID that caused movement")
    print("2. Update the servo IDs in the Sentry V2 settings")
    print("3. The servos should work with the main application")

if __name__ == "__main__":
    main()
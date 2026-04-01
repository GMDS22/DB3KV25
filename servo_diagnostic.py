#!/usr/bin/env python3
"""
Servo Diagnostic Test - Check actual servo responses
"""

import sys
import os
import time
import serial

# Add app directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from sentry_v2.sentry_v2_comm import SentryV2Comm

def test_servo_communication():
    """Test actual servo communication and responses"""
    print("Servo Communication Diagnostic Test")
    print("=" * 40)

    # Test direct serial communication
    print("Testing direct serial communication to COM28...")

    try:
        ser = serial.Serial('COM28', 115200, timeout=1)
        print("✓ Serial port opened successfully")

        # Test different checksum modes
        comm = SentryV2Comm()
        comm.pan_servo_id = 1
        comm.tilt_servo_id = 2

        checksum_modes = ["sub", "xor", "auto"]

        for mode in checksum_modes:
            print(f"\n--- Testing checksum mode: {mode} ---")
            comm._bus_checksum_mode = mode

            # Try to send a movement command
            print("Sending movement command (pan=45°, tilt=30°)...")
            packet = comm._build_servo_packet(1, 2048, 500)  # Pan servo, center position, 500ms
            print(f"Packet: {packet.hex()}")

            ser.write(packet)
            ser.flush()

            # Read response
            time.sleep(0.1)
            response = ser.read(10)
            if response:
                print(f"Response received: {response.hex()}")
            else:
                print("No response received")

            # Try tilt servo
            print("Sending tilt movement command...")
            packet = comm._build_servo_packet(2, 2048, 500)  # Tilt servo, center position, 500ms
            print(f"Packet: {packet.hex()}")

            ser.write(packet)
            ser.flush()

            time.sleep(0.1)
            response = ser.read(10)
            if response:
                print(f"Response received: {response.hex()}")
            else:
                print("No response received")

        ser.close()
        print("✓ Serial port closed")

    except Exception as e:
        print(f"✗ Serial communication failed: {e}")

def test_power_and_wiring():
    """Test basic power and wiring"""
    print("\nPower and Wiring Test")
    print("-" * 25)

    print("Please check:")
    print("1. Servo power LED is ON (red light)")
    print("2. Servo can be moved manually (feels resistance)")
    print("3. Wiring connections:")
    print("   - Signal wire (yellow/white) from Debug Board to servo")
    print("   - Power wires (red/black) connected and correct polarity")
    print("   - Ground connection secure")

    input("Press Enter when you've checked these...")

def test_servo_ids_manually():
    """Manual test of common servo ID combinations"""
    print("\nManual Servo ID Test")
    print("-" * 20)

    comm = SentryV2Comm()

    if not comm.connect(mode=2, debug_port="COM28", esp32_port=""):
        print("Failed to connect")
        return

    # Test common ID combinations
    test_combinations = [
        (1, 2),   # Default
        (10, 11), # Common alternative
        (20, 21), # Another common
        (100, 101), # Some systems use 100+
    ]

    for pan_id, tilt_id in test_combinations:
        print(f"\n--- Testing Pan ID {pan_id}, Tilt ID {tilt_id} ---")

        comm.pan_servo_id = pan_id
        comm.tilt_servo_id = tilt_id

        print("Moving to: Pan=45°, Tilt=30°")
        comm.send_movement(45, 30)
        time.sleep(2)

        print("Moving to: Pan=-45°, Tilt=-30°")
        comm.send_movement(-45, -30)
        time.sleep(2)

        print("Moving to: Pan=0°, Tilt=0° (center)")
        comm.send_movement(0, 0)
        time.sleep(2)

        print(f"DID YOU SEE MOVEMENT with IDs {pan_id}/{tilt_id}? (y/n): ", end="")
        response = input().strip().lower()
        if response == 'y':
            print(f"✓ SUCCESS! Servos are using IDs {pan_id}/{tilt_id}")
            return pan_id, tilt_id

    comm.disconnect()
    print("No movement detected with any tested ID combination")
    return None, None

def main():
    test_power_and_wiring()
    test_servo_communication()

    pan_id, tilt_id = test_servo_ids_manually()

    print("\n" + "=" * 50)
    if pan_id and tilt_id:
        print(f"SUCCESS! Servo IDs are: Pan={pan_id}, Tilt={tilt_id}")
        print("Update these IDs in your Sentry V2 settings.")
    else:
        print("SERVO ISSUE DIAGNOSIS:")
        print("1. Check servo power supply (6-8.4V DC)")
        print("2. Verify wiring connections")
        print("3. Try using the servo.exe debug software")
        print("4. Servos may need ID reprogramming")

if __name__ == "__main__":
    main()
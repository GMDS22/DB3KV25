#!/usr/bin/env python3
"""
Deep Servo Diagnostic Test
Comprehensive troubleshooting for servo movement issues
"""

import sys
import os
import time
import serial
import struct

# Add app directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from sentry_v2.sentry_v2_comm import SentryV2Comm

def test_serial_communication():
    """Test basic serial port communication"""
    print("=" * 60)
    print("TEST 1: Basic Serial Communication")
    print("=" * 60)

    try:
        ser = serial.Serial('COM28', 115200, timeout=1)
        print("✓ Serial port COM28 opened at 115200 baud")

        # Check port status
        print(f"  Port is open: {ser.is_open}")
        print(f"  Baudrate: {ser.baudrate}")
        print(f"  Timeout: {ser.timeout}")

        # Try to send and receive data
        print("\nTesting write/read...")
        test_data = b'\xFF\xFF\x01\x02\x02\xFB'  # Ping packet for ID 1
        print(f"  Sending: {test_data.hex().upper()}")

        ser.reset_input_buffer()
        ser.write(test_data)
        ser.flush()

        time.sleep(0.3)
        response = ser.read(100)

        if response:
            print(f"  Received: {response.hex().upper()} ({len(response)} bytes)")
        else:
            print(f"  No response received (timeout)")

        ser.close()
        print("✓ Serial communication test complete")
        return True

    except Exception as e:
        print(f"✗ Serial communication failed: {e}")
        return False

def test_checksum_calculation():
    """Test if checksum calculation is correct"""
    print("\n" + "=" * 60)
    print("TEST 2: Checksum Calculation")
    print("=" * 60)

    comm = SentryV2Comm()

    # Test different checksum modes
    modes = ["sub", "xor"]

    for mode in modes:
        print(f"\n--- Checksum Mode: {mode} ---")

        comm._bus_checksum_mode = mode

        # Build a simple movement packet for servo ID 1
        # Position: 2048 (center), Time: 500ms
        packet = comm._build_servo_packet(1, 2048, 500)

        print(f"Packet (hex): {packet.hex().upper()}")
        print(f"Packet (len): {len(packet)} bytes")

        # Break down packet
        if len(packet) >= 7:
            print(f"  Header: {packet[0:2].hex().upper()}")
            print(f"  ID: 0x{packet[2]:02X}")
            print(f"  Length: 0x{packet[3]:02X} ({packet[3]} bytes)")
            print(f"  Instruction: 0x{packet[4]:02X}")
            print(f"  Register: 0x{packet[5]:02X}")
            if len(packet) > 6:
                print(f"  Data: {packet[6:-1].hex().upper()}")
            if len(packet) > 0:
                print(f"  Checksum: 0x{packet[-1]:02X}")

def test_servo_movement_sequence():
    """Test actual servo movement with detailed feedback"""
    print("\n" + "=" * 60)
    print("TEST 3: Servo Movement Sequence")
    print("=" * 60)

    comm = SentryV2Comm()

    if not comm.connect(mode=2, debug_port="COM28", esp32_port=""):
        print("✗ Failed to connect to Debug Board")
        return False

    print("✓ Connected to Debug Board")

    # Test with default IDs
    print("\nTesting with Servo IDs: Pan=1, Tilt=2")

    comm.pan_servo_id = 1
    comm.tilt_servo_id = 2

    positions = [
        (0, 0, "Center"),
        (45, 0, "Pan Right 45°"),
        (-45, 0, "Pan Left 45°"),
        (0, 45, "Tilt Up 45°"),
        (0, -45, "Tilt Down 45°"),
        (45, 45, "Pan Right + Tilt Up"),
        (-45, -45, "Pan Left + Tilt Down"),
        (0, 0, "Back to Center"),
    ]

    for pan, tilt, description in positions:
        print(f"\nMove: {description} (Pan={pan:3d}°, Tilt={tilt:3d}°)")

        result = comm.send_movement(pan, tilt)
        print(f"  Command result: {result}")

        if result:
            print(f"  Last command: {comm._last_cmd}")
        else:
            print(f"  Last error: {comm._last_error}")

        time.sleep(1.5)

        print("  ⚠ DID YOU SEE MOVEMENT? (Watch the servo)")

    comm.disconnect()
    return True

def test_different_servo_ids():
    """Test different servo ID combinations"""
    print("\n" + "=" * 60)
    print("TEST 4: Different Servo ID Combinations")
    print("=" * 60)

    comm = SentryV2Comm()

    if not comm.connect(mode=2, debug_port="COM28", esp32_port=""):
        print("✗ Failed to connect")
        return

    # Test common ID combinations
    test_ids = [
        (1, 2, "Default (1, 2)"),
        (0, 1, "Zero-indexed (0, 1)"),
        (1, 1, "Same ID (1, 1)"),
        (2, 3, "Offset by 1 (2, 3)"),
        (10, 11, "High IDs (10, 11)"),
    ]

    for pan_id, tilt_id, description in test_ids:
        print(f"\n--- Testing {description} ---")

        comm.pan_servo_id = pan_id
        comm.tilt_servo_id = tilt_id

        print(f"Moving Pan servo (ID {pan_id}) to 45°")
        result = comm.send_movement(45, 0)
        print(f"  Result: {result}")
        time.sleep(1.5)

        print(f"Moving Tilt servo (ID {tilt_id}) to 30°")
        result = comm.send_movement(0, 30)
        print(f"  Result: {result}")
        time.sleep(1.5)

        print(f"Back to center")
        result = comm.send_movement(0, 0)
        time.sleep(1)

        print(f"⚠ Did {description} produce movement?")

    comm.disconnect()

def test_raw_servo_packets():
    """Test sending raw servo packets directly"""
    print("\n" + "=" * 60)
    print("TEST 5: Raw Servo Packets")
    print("=" * 60)

    try:
        ser = serial.Serial('COM28', 115200, timeout=1)
        print("✓ Opened COM28 directly")

        comm = SentryV2Comm()
        comm._bus_checksum_mode = "sub"

        # Test different positions
        positions = [
            (2048, "Center position"),
            (2548, "Right/Up 45°"),
            (1548, "Left/Down 45°"),
        ]

        for pos_ticks, description in positions:
            print(f"\n--- {description} (ticks={pos_ticks}) ---")

            # Build packet for servo ID 1 (pan)
            packet = comm._build_servo_packet(1, pos_ticks, 500)
            print(f"Sending packet: {packet.hex().upper()}")

            ser.reset_input_buffer()
            ser.write(packet)
            ser.flush()

            time.sleep(1.5)
            print("⚠ Did pan servo move?")

            # Reset to center
            packet = comm._build_servo_packet(1, 2048, 500)
            ser.write(packet)
            ser.flush()
            time.sleep(1)

        ser.close()

    except Exception as e:
        print(f"✗ Error: {e}")

def print_hardware_checklist():
    """Print hardware checklist"""
    print("\n" + "=" * 60)
    print("HARDWARE CHECKLIST")
    print("=" * 60)
    print("""
Please verify each item:

POWER:
  ☐ Servo power supply is turned ON
  ☐ Red LED visible on servo(s) (indicates power)
  ☐ Voltage measured: 6-8.4V DC (use multimeter)

WIRING:
  ☐ Signal wire connected (yellow/white to "S" pin)
  ☐ Power wire connected (red to "V+" or power rail)
  ☐ Ground wire connected (black to GND)
  ☐ All connections are secure (not loose)

DEBUG BOARD:
  ☐ Debug Board has power (USB or external)
  ☐ Debug Board COM28 is recognized by Windows
  ☐ No other program using COM28 (check Device Manager)

SERVO RESPONSE:
  ☐ Can manually move servo horn (should feel resistance)
  ☐ Servo horn moves freely when powered (not stuck)
""")

def main():
    print("\nDEEP SERVO DIAGNOSTIC TEST")
    print("=" * 60)
    print("This will help identify why servos aren't moving\n")

    # Show checklist first
    print_hardware_checklist()
    input("Press Enter once you've verified these items...")

    # Run tests
    test_serial_communication()
    test_checksum_calculation()
    test_servo_movement_sequence()
    test_different_servo_ids()
    test_raw_servo_packets()

    print("\n" + "=" * 60)
    print("DIAGNOSTIC TEST COMPLETE")
    print("=" * 60)
    print("""
NEXT STEPS:

If you saw movement:
  1. Note which servo IDs worked
  2. Update settings to use those IDs
  3. Run Sentry V2 app

If you did NOT see movement:
  1. Check POWER first (most likely issue)
  2. Verify WIRING connections
  3. Test servo with servo.exe software
  4. Check if servo is damaged
  5. Try different USB cable for Debug Board
""")

if __name__ == "__main__":
    main()
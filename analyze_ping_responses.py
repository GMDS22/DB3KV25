#!/usr/bin/env python3
"""
Servo Ping Response Analyzer
Checks if ping responses are real servo feedback or electrical noise
"""

import sys
import os
import time
import serial

# Add app directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from sentry_v2.sentry_v2_comm import SentryV2Comm

def analyze_ping_response():
    """Analyze raw ping responses to check for real servo feedback"""
    print("Servo Ping Response Analysis")
    print("=" * 50)

    comm = SentryV2Comm()

    # Open serial connection
    try:
        ser = serial.Serial('COM28', 115200, timeout=0.5)
        print("✓ Serial port COM28 opened")
    except Exception as e:
        print(f"✗ Failed to open COM28: {e}")
        return

    print("\nTesting ping responses with empty bus (no actual servos)...\n")

    # Build ping packets for different IDs
    servo_ids = [1, 2, 5, 10, 20, 50]

    for servo_id in servo_ids:
        print(f"--- Servo ID {servo_id} ---")

        # Build and send ping packet
        ping_packet = comm._build_ping_packet(servo_id)
        print(f"Sent ping packet: {ping_packet.hex().upper()}")
        print(f"  (0xFF 0xFF ID:{servo_id:02X} LEN:02 CMD:02)")

        # Clear buffer
        ser.reset_input_buffer()

        # Send ping
        ser.write(ping_packet)
        ser.flush()

        # Read response
        time.sleep(0.2)
        response = ser.read(100)

        if response:
            print(f"Response received: {response.hex().upper()} ({len(response)} bytes)")

            # Analyze response pattern
            print("Response analysis:")

            # Check for standard servo response header (0xFF 0xFF)
            if len(response) >= 2:
                if response[0] == 0xFF and response[1] == 0xFF:
                    print("  ✓ Header matches servo response (0xFF 0xFF)")
                    if len(response) >= 4:
                        servo_id_resp = response[2]
                        length = response[3]
                        print(f"  ID: {servo_id_resp:02X}, Length: {length}")
                else:
                    print(f"  ✗ No servo header (got 0x{response[0]:02X} 0x{response[1]:02X})")
                    print("  → This looks like electrical NOISE, not servo feedback")
            else:
                print(f"  ✗ Response too short ({len(response)} bytes)")

            # Show byte distribution (noise typically has random distribution)
            unique_bytes = len(set(response))
            print(f"  Unique byte values: {unique_bytes} out of {len(response)}")
            if unique_bytes == 1:
                print("  → Likely noise pattern (all same byte)")
            elif unique_bytes > len(response) * 0.7:
                print("  → Likely random noise (high variation)")
        else:
            print("No response received")

        print()

    ser.close()
    print("=" * 50)
    print("Analysis complete.")
    print("\nExpected servo response format:")
    print("  Header: 0xFF 0xFF")
    print("  ID: servo ID")
    print("  Length: packet length")
    print("  Error: error flags")
    print("  Parameters: response data")
    print("  Checksum: calculated checksum")

def test_with_actual_servo():
    """Test what a REAL servo response looks like"""
    print("\n\nReal Servo Response Test")
    print("=" * 50)
    print("Sending movement commands and checking for responses...\n")

    comm = SentryV2Comm()

    if not comm.connect(mode=2, debug_port="COM28", esp32_port=""):
        print("Failed to connect")
        return

    try:
        ser = comm._bus_ser

        # Send a movement command to a real servo
        print("Sending movement command to servo ID 1...")
        packet = comm._build_servo_packet(1, 2048, 500)
        print(f"Packet: {packet.hex().upper()}")

        ser.reset_input_buffer()
        ser.write(packet)
        ser.flush()

        time.sleep(0.3)
        response = ser.read(100)

        if response:
            print(f"Response: {response.hex().upper()} ({len(response)} bytes)")
            print("Note: Some servos don't send responses to position commands")
        else:
            print("No response (normal - many servos don't respond to move commands)")

        # Try to probe checksum mode which pings servos
        print("\n\nProbing checksum mode (sends pings to detect servos)...")
        checksum_mode = comm._probe_bus_servo_checksum(ser)
        print(f"Detected checksum mode: {checksum_mode}")

    except Exception as e:
        print(f"Error: {e}")

    comm.disconnect()

def main():
    analyze_ping_response()
    test_with_actual_servo()

if __name__ == "__main__":
    main()
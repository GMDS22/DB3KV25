#!/usr/bin/env python3
"""
Deep Servo & Debug Board Test
Direct USB communication test - no ESP32 involved
"""

import serial
import time
import sys

def test_debug_board_basic():
    """Test basic connectivity to Debug Board"""
    print("=" * 60)
    print("DEBUG BOARD BASIC CONNECTIVITY TEST")
    print("=" * 60)

    try:
        ser = serial.Serial('COM28', 115200, timeout=1)
        print("✓ COM28 opened at 115200 baud")
    except Exception as e:
        print(f"✗ Failed to open COM28: {e}")
        return False

    # Try to send a simple command and see if we get any response
    print("\nSending reset command (0xFF 0xFF 0xFF)...")
    ser.write(b'\xFF\xFF\xFF')
    ser.flush()
    time.sleep(0.5)

    response = ser.read(100)
    if response:
        print(f"Response: {response.hex().upper()}")
    else:
        print("No response")

    ser.close()
    return True

def test_servo_direct_control():
    """Direct test of servo control via Debug Board"""
    print("\n" + "=" * 60)
    print("DIRECT SERVO CONTROL TEST")
    print("=" * 60)

    try:
        ser = serial.Serial('COM28', 115200, timeout=1)
        print("✓ COM28 opened")
    except Exception as e:
        print(f"✗ Failed to open COM28: {e}")
        return

    print("\nTest 1: Send raw servo position commands")
    print("-" * 40)

    # Build servo commands manually
    # Format: 0xFF 0xFF ID LEN CMD REG DATA1 DATA2 DATA3... CHECKSUM

    # Servo ID 1, move to center position (2048 = 0x0800 in ticks)
    # Command format for YahBoom servo:
    # 0xFF 0xFF [ID] [LENGTH] [COMMAND] [REGISTER] [DATA_BYTE1] [DATA_BYTE2] ... [CHECKSUM]

    commands = [
        ("ID 1 -> 0°", b"\xFF\xFF\x01\x07\x03\x2A\x00\x00\x01\xF4", 0xCD),    # Pan to 0°
        ("ID 1 -> 90°", b"\xFF\xFF\x01\x07\x03\x2A\x08\x00\x01\xF4", 0xC5),   # Pan to 90°
        ("ID 1 -> 0°", b"\xFF\xFF\x01\x07\x03\x2A\x00\x00\x01\xF4", 0xCD),    # Pan back to 0°
        ("ID 2 -> 0°", b"\xFF\xFF\x02\x07\x03\x2A\x00\x00\x01\xF4", 0xCC),    # Tilt to 0°
        ("ID 2 -> 60°", b"\xFF\xFF\x02\x07\x03\x2A\x06\x00\x01\xF4", 0xC7),   # Tilt to 60°
        ("ID 2 -> 0°", b"\xFF\xFF\x02\x07\x03\x2A\x00\x00\x01\xF4", 0xCC),    # Tilt back to 0°
    ]

    for desc, packet, checksum in commands:
        print(f"\n{desc}")
        full_packet = packet + bytes([checksum])
        print(f"  Packet: {full_packet.hex().upper()}")
        print(f"  Sent: ", end="")

        ser.reset_input_buffer()
        ser.write(full_packet)
        ser.flush()

        time.sleep(0.5)

        response = ser.read(10)
        if response:
            print(f"✓ Response: {response.hex().upper()}")
        else:
            print("No response")

        print(f"  → DID SERVO MOVE? (Check manually)")
        time.sleep(1.5)

    ser.close()

def test_servo_positions():
    """Test reading servo positions to verify communication"""
    print("\n" + "=" * 60)
    print("SERVO POSITION READ TEST")
    print("=" * 60)

    try:
        ser = serial.Serial('COM28', 115200, timeout=1)
        print("✓ COM28 opened")
    except Exception as e:
        print(f"✗ Failed to open COM28: {e}")
        return

    print("\nAttempting to read servo positions...")
    print("-" * 40)

    # Ping packets to read position from servo
    # Format: 0xFF 0xFF ID 02 02 CHECKSUM (ping command)

    ping_commands = [
        (1, b"\xFF\xFF\x01\x02\x02\xFB"),      # Ping ID 1
        (2, b"\xFF\xFF\x02\x02\x02\xFA"),      # Ping ID 2
        (5, b"\xFF\xFF\x05\x02\x02\xF7"),      # Ping ID 5
    ]

    for servo_id, ping_packet in ping_commands:
        print(f"\nPinging Servo ID {servo_id}...")
        print(f"  Packet: {ping_packet.hex().upper()}")

        ser.reset_input_buffer()
        ser.write(ping_packet)
        ser.flush()

        time.sleep(0.3)

        response = ser.read(20)
        if response:
            print(f"  ✓ Response: {response.hex().upper()} ({len(response)} bytes)")

            # Analyze response
            if len(response) >= 4:
                if response[0] == 0xFF and response[1] == 0xFF:
                    resp_id = response[2]
                    resp_len = response[3]
                    print(f"    - Valid servo response header")
                    print(f"    - Response ID: {resp_id}")
                    print(f"    - Response Length: {resp_len}")
                else:
                    print(f"    - Invalid header (not 0xFF 0xFF)")
            else:
                print(f"    - Response too short")
        else:
            print(f"  ✗ No response")

    ser.close()

def test_servo_power():
    """Test if servo power is present"""
    print("\n" + "=" * 60)
    print("SERVO POWER & CONNECTIVITY TEST")
    print("=" * 60)

    print("\nManual checks:")
    print("1. LED on servo should be RED/ON")
    print("2. Servo should have resistance when manually moved")
    print("3. All wires connected to Debug Board:")
    print("   - Yellow/White (signal)")
    print("   - Red (power)")
    print("   - Black (ground)")
    print("\n4. Debug Board should be powered from USB")

    input("\nPress Enter when you've verified hardware...")

    print("\n✓ If LED is ON and servo has resistance, power is OK")
    print("✓ If no resistance, servo might not be connected properly")

def main():
    print("\nDEEP SERVO & DEBUG BOARD DIAGNOSTIC TEST")
    print("Testing Direct USB → Debug Board → Servos Connection")
    print()

    # Test 1: Basic connectivity
    if not test_debug_board_basic():
        print("\n✗ CRITICAL: Cannot connect to Debug Board on COM28")
        sys.exit(1)

    # Test 2: Check servo power
    test_servo_power()

    # Test 3: Direct servo commands
    test_servo_direct_control()

    # Test 4: Position verification
    test_servo_positions()

    print("\n" + "=" * 60)
    print("DIAGNOSTIC SUMMARY")
    print("=" * 60)
    print("\nIf servos DIDN'T move during any test:")
    print("1. ✓ Verify servo power LED is ON")
    print("2. ✓ Check all wiring connections (signal, power, ground)")
    print("3. ✓ Try using servo.exe to test Debug Board directly")
    print("4. ✓ Check servo voltage with multimeter (should be 6-8.4V)")
    print("\nIf servos MOVED during test:")
    print("1. Note which IDs work")
    print("2. Update settings with correct IDs")
    print("3. Run Sentry V2 app again")

if __name__ == "__main__":
    main()
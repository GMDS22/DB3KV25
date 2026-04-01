#!/usr/bin/env python3
"""
Advanced Debug Board Communication Test
Tests different communication protocols and baud rates
"""

import serial
import time
import sys

def test_baud_rates():
    """Test different baud rates with Debug Board"""
    print("=" * 60)
    print("TESTING DIFFERENT BAUD RATES")
    print("=" * 60)

    baud_rates = [9600, 115200, 230400, 460800]

    for baud in baud_rates:
        print(f"\nTesting baud rate: {baud}")
        try:
            ser = serial.Serial('COM28', baud, timeout=0.5)
            print(f"  ✓ Port opened at {baud} baud")

            # Send a reset command
            ser.write(b'\xFF\xFF\xFF')
            ser.flush()
            time.sleep(0.1)

            response = ser.read(20)
            if response:
                print(f"  Response: {response.hex().upper()}")
                # Check if it looks like valid data
                if response[0:1] != b'\x00':
                    print(f"  → Looks like valid response!")
                else:
                    print(f"  → Response is mostly zeros (may be buffer garbage)")
            else:
                print(f"  No response")

            ser.close()
        except Exception as e:
            print(f"  ✗ Failed: {e}")

def test_servo_protocol_variations():
    """Test different servo communication protocols"""
    print("\n" + "=" * 60)
    print("TESTING SERVO COMMUNICATION PROTOCOLS")
    print("=" * 60)

    try:
        ser = serial.Serial('COM28', 115200, timeout=0.5)
    except Exception as e:
        print(f"Cannot open COM28: {e}")
        return

    protocols = [
        ("Standard YahBoom Move (ID 1, 0°)", 
         b"\xFF\xFF\x01\x07\x03\x2A\x00\x00\x01\xF4\xCD"),

        ("Alternative Format (Test)", 
         b"\x55\xAA\x01\x00\x00\x00\x00\x00"),

        ("Simple Servo Command", 
         b"\xFF\x01\x00\x00\x00"),

        ("Ping Servo (Clean)", 
         b"\xFF\xFF\x01\x02\x02\xFB"),
    ]

    for desc, packet in protocols:
        print(f"\n{desc}")
        print(f"  Packet: {packet.hex().upper()}")

        ser.reset_input_buffer()
        ser.write(packet)
        ser.flush()

        time.sleep(0.2)

        response = ser.read(100)
        if response:
            print(f"  Response ({len(response)} bytes): {response.hex().upper()}")

            # Try to analyze
            if len(response) > 2:
                if response[0] == 0xFF and response[1] == 0xFF:
                    print(f"    ✓ Valid YahBoom response detected!")
                elif response[0] == 0x55 and response[1] == 0xAA:
                    print(f"    ✓ Different protocol response detected!")
                else:
                    print(f"    → Unrecognized response format")
        else:
            print(f"  No response")

        time.sleep(0.5)

    ser.close()

def test_buffer_flush():
    """Test clearing buffer garbage"""
    print("\n" + "=" * 60)
    print("TESTING BUFFER CLEANUP")
    print("=" * 60)

    try:
        ser = serial.Serial('COM28', 115200, timeout=0.5)
        print("✓ COM28 opened")
    except Exception as e:
        print(f"✗ Cannot open COM28: {e}")
        return

    print("\nClearing input buffer...")
    ser.reset_input_buffer()
    time.sleep(0.2)

    garbage = ser.read(100)
    if garbage:
        print(f"Found garbage in buffer: {garbage.hex().upper()}")
    else:
        print(f"Buffer is clean")

    print("\nSending clean servo command...")
    ser.write(b"\xFF\xFF\x01\x07\x03\x2A\x00\x00\x01\xF4\xCD")
    ser.flush()

    time.sleep(0.3)

    response = ser.read(100)
    if response:
        print(f"Response: {response.hex().upper()}")
    else:
        print(f"No response")

    ser.close()

def test_servo_direct_read():
    """Attempt to read servo position directly"""
    print("\n" + "=" * 60)
    print("READING SERVO POSITION")
    print("=" * 60)

    try:
        ser = serial.Serial('COM28', 115200, timeout=1)
    except Exception as e:
        print(f"Cannot open COM28: {e}")
        return

    # Read position command for servo ID 1
    # Format: 0xFF 0xFF 0x01 0x04 0x04 [ADDR_LO] [ADDR_HI] [CHECKSUM]
    # Address 0x2A+0x2B = current position

    read_commands = [
        ("Read Position (Reg 0x2A, ID 1)", 
         b"\xFF\xFF\x01\x04\x04\x2A\x00\x00\x00"),

        ("Read Position (Reg 0x30, ID 1)", 
         b"\xFF\xFF\x01\x04\x04\x30\x00\x00\x00"),

        ("Simple Position Query", 
         b"\xFF\xFF\x01\x03\x2A\x02\x00"),
    ]

    for desc, cmd in read_commands:
        print(f"\n{desc}")
        print(f"  Command: {cmd.hex().upper()}")

        ser.reset_input_buffer()
        ser.write(cmd)
        ser.flush()

        time.sleep(0.3)

        response = ser.read(20)
        if response:
            print(f"  Response: {response.hex().upper()}")

            # Look for position bytes
            if len(response) >= 4:
                pos_low = response[-2]
                pos_high = response[-1]
                position = (pos_high << 8) | pos_low
                print(f"  Position (raw): {position} ticks")
                print(f"  Position (degrees): {position * 0.2} °")  # Approximate
        else:
            print(f"  No response")

    ser.close()

def main():
    print("\nADVANCED DEBUG BOARD DIAGNOSTIC")
    print("Searching for communication issues\n")

    test_baud_rates()
    test_servo_protocol_variations()
    test_buffer_flush()
    test_servo_direct_read()

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
    print("\nPossible Issues Found:")
    print("1. If responses are mostly zeros: buffer garbage, not servo responses")
    print("2. If no responses at all: Debug Board not connected or powered")
    print("3. If valid responses but no movement: servo not powered or disconnected")
    print("4. If movement happens but inconsistent: timing or protocol issue")
    print("\nNext Steps:")
    print("1. Try servo.exe to test Debug Board independently")
    print("2. Check servo power supply (multimeter)")
    print("3. Check wiring: signal (yellow), power (red), ground (black)")
    print("4. Try different Debug Board USB cable")

if __name__ == "__main__":
    main()
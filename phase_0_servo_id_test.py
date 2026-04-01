#!/usr/bin/env python3
"""
Phase 0 - Servo ID Test (requires modified firmware)
Tests individual servo IDs to find which ones work
"""

import json
import socket
import time
import zlib
from typing import Dict, Any

def encode_with_crc(msg: Dict[str, Any]) -> bytes:
    """Encode message with CRC32 checksum"""
    payload = dict(msg)
    payload.pop("crc", None)
    raw = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    crc = zlib.crc32(raw) & 0xFFFFFFFF
    payload["crc"] = f"{crc:08x}"
    return json.dumps(payload, separators=(",", ":")).encode("utf-8")

def test_servo_id(sock: socket.socket, host: str, port: int, servo_id: int):
    """Test a specific servo ID by sending it to different positions"""
    print(f"\n--- Testing Servo ID {servo_id} ---")

    # Test command for this specific ID
    msg = {
        "t": "cmd",
        "action": "test_id",
        "id": servo_id,
        "deg": 0,  # Start at 0°
        "time": 1000,
        "ts": int(time.time() * 1000),
        "v": 1
    }
    data = encode_with_crc(msg)
    sock.sendto(data, (host, port))
    print(f"Sent ID {servo_id} to 0°")
    time.sleep(2)

    # Move to 90°
    msg["deg"] = 90
    msg["ts"] = int(time.time() * 1000)
    data = encode_with_crc(msg)
    sock.sendto(data, (host, port))
    print(f"Sent ID {servo_id} to 90°")
    time.sleep(2)

    # Move to 180°
    msg["deg"] = 180
    msg["ts"] = int(time.time() * 1000)
    data = encode_with_crc(msg)
    sock.sendto(data, (host, port))
    print(f"Sent ID {servo_id} to 180°")
    time.sleep(2)

    # Back to 0°
    msg["deg"] = 0
    msg["ts"] = int(time.time() * 1000)
    data = encode_with_crc(msg)
    sock.sendto(data, (host, port))
    print(f"Sent ID {servo_id} back to 0°")
    time.sleep(2)

def main():
    # ESP32 WiFi AP details
    ESP32_HOST = "192.168.4.2"
    ESP32_PORT = 9001

    print("Phase 0 - Servo ID Test (Modified Firmware Required)")
    print("This requires firmware with 'test_id' command support")
    print("Testing servo IDs 1-10 individually")
    print()

    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1.0)

    try:
        # Test each servo ID individually
        for servo_id in range(1, 11):  # Test IDs 1-10
            test_servo_id(sock, ESP32_HOST, ESP32_PORT, servo_id)
            print(f"ID {servo_id} test complete - did servo move?")

        print("\n✅ All ID tests complete!")
        print("Which servo ID made the servo move?")
        print("If none worked, the servos may not be Yahboom serial bus servos")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        sock.close()

if __name__ == "__main__":
    main()
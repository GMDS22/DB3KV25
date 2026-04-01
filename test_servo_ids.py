#!/usr/bin/env python3
"""
Test different servo IDs manually
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
    """Test a specific servo ID"""
    print(f"\n--- Testing Servo ID {servo_id} ---")

    # Send test command to this ID
    msg = {
        "t": "cmd",
        "action": "test_id",
        "id": servo_id,
        "deg": 90,  # Move to 90°
        "time": 1000,
        "ts": int(time.time() * 1000),
        "v": 1
    }
    data = encode_with_crc(msg)
    sock.sendto(data, (host, port))
    print(f"Sent test_id command to servo {servo_id}")

    time.sleep(2)  # Wait for movement

    # Send back to 0°
    msg["deg"] = 0
    msg["ts"] = int(time.time() * 1000)
    data = encode_with_crc(msg)
    sock.sendto(data, (host, port))
    print(f"Sent servo {servo_id} back to 0°")

    time.sleep(2)

def main():
    # ESP32 WiFi AP details
    ESP32_HOST = "192.168.4.2"
    ESP32_PORT = 9001

    print("Manual Servo ID Test")
    print("Testing different servo IDs to find which ones work")
    print()

    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1.0)

    try:
        # Test common servo IDs
        test_ids = [1, 2, 3, 4, 5, 10, 11, 12, 20, 21, 22]

        for servo_id in test_ids:
            test_servo_id(sock, ESP32_HOST, ESP32_PORT, servo_id)
            print(f"ID {servo_id} test complete - did servo move?")

        print("\n✅ All ID tests complete!")
        print("Which servo ID made the servo move?")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        sock.close()

if __name__ == "__main__":
    main()
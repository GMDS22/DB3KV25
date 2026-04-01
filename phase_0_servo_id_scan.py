#!/usr/bin/env python3
"""
Phase 0 - Servo ID Scan Test
Tests all possible servo IDs to find which ones respond
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

def send_servo_command(sock: socket.socket, host: str, port: int, servo_id: int, position_deg: float, move_time_ms: int = 1000):
    """Send servo position command to specific ID"""
    msg = {
        "t": "servo",
        "pan": position_deg if servo_id == 1 else 0,  # Only move the target servo
        "tilt": position_deg if servo_id == 2 else 0,
        "time": move_time_ms,
        "ts": int(time.time() * 1000),
        "v": 1
    }
    data = encode_with_crc(msg)
    sock.sendto(data, (host, port))
    print(f"Sent to ID {servo_id}: {position_deg}°")

def main():
    # ESP32 WiFi AP details
    ESP32_HOST = "192.168.4.2"
    ESP32_PORT = 9001

    print("Phase 0 - Servo ID Scan Test")
    print("Testing all servo IDs (1-10) to find which ones work")
    print("Watch the servos - any that move indicate their correct ID")
    print()

    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1.0)

    try:
        # Test each servo ID
        for servo_id in range(1, 11):  # Test IDs 1-10
            print(f"\n--- Testing Servo ID {servo_id} ---")

            # Move to 0°
            send_servo_command(sock, ESP32_HOST, ESP32_PORT, servo_id, 0, 1000)
            time.sleep(2)

            # Move to 90°
            send_servo_command(sock, ESP32_HOST, ESP32_PORT, servo_id, 90, 1000)
            time.sleep(2)

            # Move back to 0°
            send_servo_command(sock, ESP32_HOST, ESP32_PORT, servo_id, 0, 1000)
            time.sleep(2)

            print(f"ID {servo_id} test complete - did servo move?")

        print("\n✅ ID scan complete!")
        print("Which servo ID(s) made the servo(s) move?")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        sock.close()

if __name__ == "__main__":
    main()
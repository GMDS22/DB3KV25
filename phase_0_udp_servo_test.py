#!/usr/bin/env python3
"""
Phase 0 - Simple UDP Servo Test
Sends basic servo commands to Waveshare ESP32 over WiFi
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

def send_servo_command(sock: socket.socket, host: str, port: int, pan_deg: float, tilt_deg: float, move_time_ms: int = 1000):
    """Send servo position command"""
    msg = {
        "t": "servo",
        "pan": pan_deg,
        "tilt": tilt_deg,
        "time": move_time_ms,
        "ts": int(time.time() * 1000),
        "v": 1
    }
    data = encode_with_crc(msg)
    sock.sendto(data, (host, port))
    print(f"Sent: Pan={pan_deg}°, Tilt={tilt_deg}°, Time={move_time_ms}ms")

def main():
    # ESP32 WiFi AP details
    ESP32_HOST = "192.168.4.2"  # Default ESP32 AP IP
    ESP32_PORT = 9001           # UDP port from firmware

    print("Phase 0 - UDP Servo Test")
    print(f"Target: {ESP32_HOST}:{ESP32_PORT}")
    print("Make sure your PC is connected to 'DB3000-ESP32' WiFi network")
    print()

    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1.0)  # 1 second timeout

    try:
        # Test 1: Center position
        print("Test 1: Moving to center (0°, 0°)")
        send_servo_command(sock, ESP32_HOST, ESP32_PORT, 0, 0, 2000)
        time.sleep(3)

        # Test 2: Pan left
        print("Test 2: Panning left (-45°, 0°)")
        send_servo_command(sock, ESP32_HOST, ESP32_PORT, -45, 0, 2000)
        time.sleep(3)

        # Test 3: Pan right
        print("Test 3: Panning right (45°, 0°)")
        send_servo_command(sock, ESP32_HOST, ESP32_PORT, 45, 0, 2000)
        time.sleep(3)

        # Test 4: Tilt up
        print("Test 4: Tilting up (0°, -30°)")
        send_servo_command(sock, ESP32_HOST, ESP32_PORT, 0, -30, 2000)
        time.sleep(3)

        # Test 5: Tilt down
        print("Test 5: Tilting down (0°, 30°)")
        send_servo_command(sock, ESP32_HOST, ESP32_PORT, 0, 30, 2000)
        time.sleep(3)

        # Test 6: Back to center
        print("Test 6: Back to center (0°, 0°)")
        send_servo_command(sock, ESP32_HOST, ESP32_PORT, 0, 0, 2000)
        time.sleep(3)

        print("\n✅ All tests completed!")
        print("Check if servos actually moved. If yes, Phase 0 PASSED!")

    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure:")
        print("1. PC is connected to 'DB3000-ESP32' WiFi")
        print("2. ESP32 is powered and running")
        print("3. Servos are connected and powered")

    finally:
        sock.close()

if __name__ == "__main__":
    main()
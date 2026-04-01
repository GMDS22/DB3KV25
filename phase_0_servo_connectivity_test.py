#!/usr/bin/env python3
"""
Phase 0 - Servo Connectivity Test
Tests if servos are responding to bus commands
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

def send_bus_ping(sock: socket.socket, host: str, port: int):
    """Send bus ping command to test servo connectivity"""
    msg = {
        "t": "cmd",
        "action": "bus_ping",
        "ts": int(time.time() * 1000),
        "v": 1
    }
    data = encode_with_crc(msg)
    sock.sendto(data, (host, port))
    print("Sent bus_ping command to test servo connectivity")

def send_self_test(sock: socket.socket, host: str, port: int):
    """Send self-test command to move servos to home position"""
    msg = {
        "t": "cmd",
        "action": "test",
        "ts": int(time.time() * 1000),
        "v": 1
    }
    data = encode_with_crc(msg)
    sock.sendto(data, (host, port))
    print("Sent self-test command - servos should move to home position (Pan=90°, Tilt=40°)")

def main():
    # ESP32 WiFi AP details
    ESP32_HOST = "192.168.4.2"
    ESP32_PORT = 9001

    print("Phase 0 - Servo Connectivity Test")
    print(f"Target: {ESP32_HOST}:{ESP32_PORT}")
    print("Make sure your PC is connected to 'DB3000-ESP32' WiFi network")
    print()

    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2.0)

    try:
        print("Test 1: Bus Ping - Testing servo connectivity")
        send_bus_ping(sock, ESP32_HOST, ESP32_PORT)
        time.sleep(2)  # Wait for response

        print("\nTest 2: Self Test - Moving servos to home position")
        print("Watch the servos - they should move to Pan=90°, Tilt=40°")
        send_self_test(sock, ESP32_HOST, ESP32_PORT)
        time.sleep(3)  # Wait for movement

        print("\n✅ Tests completed!")
        print("Check the serial monitor for bus ping results")
        print("Did the servos move during the self-test?")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        sock.close()

if __name__ == "__main__":
    main()
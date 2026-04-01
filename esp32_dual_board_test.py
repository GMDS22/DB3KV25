#!/usr/bin/env python3
"""
ESP32 Dual Board Connectivity Test
===================================

Tests connectivity to both ESP32 boards in dual WiFi mode:
- Primary ESP32 (192.168.4.1:9000) - IO/accessories
- Secondary ESP32 (192.168.4.2:9001) - Yahboom servos

Usage:
    python esp32_dual_board_test.py

This script validates:
1. Primary ESP32 responds to IO commands
2. Secondary ESP32 responds to servo commands
3. Both boards maintain UDP connectivity
4. Command routing works correctly
"""

import socket
import json
import time
import sys
from typing import Dict, Any, Tuple

# Board configurations
PRIMARY_IP = "192.168.4.1"
PRIMARY_PORT = 9000
SECONDARY_IP = "192.168.4.2"
SECONDARY_PORT = 9001

UDP_TIMEOUT = 2.0  # seconds

def create_udp_socket() -> socket.socket:
    """Create and configure UDP socket."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(UDP_TIMEOUT)
    return sock

def send_command(sock: socket.socket, ip: str, port: int, payload: Dict[str, Any]) -> Tuple[bool, str]:
    """Send JSON command and return (success, response/error)."""
    try:
        # Create command packet
        packet = {
            "v": 1,
            "t": "cmd",
            "seq": int(time.time() * 1000) % 10000,
            "ts": int(time.time() * 1000),
            "p": payload
        }

        # Serialize and send
        msg = json.dumps(packet)
        sock.sendto(msg.encode(), (ip, port))

        # Wait for response
        data, addr = sock.recvfrom(2048)
        response = data.decode()

        # Validate response is JSON
        try:
            resp_json = json.loads(response)
            return True, f"OK: {resp_json.get('t', 'unknown')} from {addr}"
        except json.JSONDecodeError:
            return True, f"RAW: {response[:100]}... from {addr}"

    except socket.timeout:
        return False, f"TIMEOUT: No response from {ip}:{port}"
    except Exception as e:
        return False, f"ERROR: {str(e)}"

def test_primary_esp32(sock: socket.socket) -> Tuple[bool, str]:
    """Test primary ESP32 (IO/accessories)."""
    print("Testing Primary ESP32 (IO)...")

    # Test LED toggle
    success, response = send_command(sock, PRIMARY_IP, PRIMARY_PORT, {
        "led": 1,      # Turn LED on
        "laser": 0,    # Turn laser off
        "safety": 1,   # Stay safe
        "fire": 0      # Don't fire
    })

    if success:
        print(f"  ✓ Primary ESP32 responded: {response}")

        # Test another command
        time.sleep(0.5)
        success2, response2 = send_command(sock, PRIMARY_IP, PRIMARY_PORT, {
            "led": 0,      # Turn LED off
            "laser": 1,    # Turn laser on
            "safety": 1,   # Stay safe
            "fire": 0      # Don't fire
        })

        if success2:
            print(f"  ✓ Primary ESP32 command 2: {response2}")
            return True, "Primary ESP32 OK"
        else:
            return False, f"Primary ESP32 command 2 failed: {response2}"
    else:
        return False, f"Primary ESP32 failed: {response}"

def test_secondary_esp32(sock: socket.socket) -> Tuple[bool, str]:
    """Test secondary ESP32 (servos)."""
    print("Testing Secondary ESP32 (Servos)...")

    # Test pan/tilt command
    success, response = send_command(sock, SECONDARY_IP, SECONDARY_PORT, {
        "pan_cmd": 90.0,    # Center pan
        "tilt_cmd": 40.0,   # Center tilt
        "move_time_ms": 100
    })

    if success:
        print(f"  ✓ Secondary ESP32 responded: {response}")

        # Test another position
        time.sleep(0.5)
        success2, response2 = send_command(sock, SECONDARY_IP, SECONDARY_PORT, {
            "pan_cmd": 45.0,    # Left pan
            "tilt_cmd": 30.0,   # Lower tilt
            "move_time_ms": 200
        })

        if success2:
            print(f"  ✓ Secondary ESP32 command 2: {response2}")

            # Return to center
            time.sleep(0.5)
            send_command(sock, SECONDARY_IP, SECONDARY_PORT, {
                "pan_cmd": 90.0,
                "tilt_cmd": 40.0,
                "move_time_ms": 100
            })

            return True, "Secondary ESP32 OK"
        else:
            return False, f"Secondary ESP32 command 2 failed: {response2}"
    else:
        return False, f"Secondary ESP32 failed: {response}"

def test_dual_connectivity(sock: socket.socket) -> Tuple[bool, str]:
    """Test that both boards can be commanded simultaneously."""
    print("Testing Dual Board Connectivity...")

    # Send commands to both boards
    primary_success, primary_response = send_command(sock, PRIMARY_IP, PRIMARY_PORT, {
        "led": 1,
        "laser": 1,
        "safety": 1,
        "fire": 0
    })

    time.sleep(0.1)  # Small delay between commands

    secondary_success, secondary_response = send_command(sock, SECONDARY_IP, SECONDARY_PORT, {
        "pan_cmd": 135.0,   # Right pan
        "tilt_cmd": 50.0,   # Higher tilt
        "move_time_ms": 150
    })

    if primary_success and secondary_success:
        print(f"  ✓ Both boards responded simultaneously")
        print(f"    Primary: {primary_response}")
        print(f"    Secondary: {secondary_response}")

        # Return servos to center
        time.sleep(0.5)
        send_command(sock, SECONDARY_IP, SECONDARY_PORT, {
            "pan_cmd": 90.0,
            "tilt_cmd": 40.0,
            "move_time_ms": 100
        })

        return True, "Dual connectivity OK"
    else:
        failures = []
        if not primary_success:
            failures.append(f"Primary: {primary_response}")
        if not secondary_success:
            failures.append(f"Secondary: {secondary_response}")
        return False, f"Dual connectivity failed: {'; '.join(failures)}"

def main():
    """Main test function."""
    print("ESP32 Dual Board Connectivity Test")
    print("=" * 40)
    print(f"Primary ESP32:   {PRIMARY_IP}:{PRIMARY_PORT}")
    print(f"Secondary ESP32: {SECONDARY_IP}:{SECONDARY_PORT}")
    print()

    sock = create_udp_socket()

    try:
        # Test individual boards
        primary_ok, primary_msg = test_primary_esp32(sock)
        print(f"Primary result: {'PASS' if primary_ok else 'FAIL'} - {primary_msg}")
        print()

        secondary_ok, secondary_msg = test_secondary_esp32(sock)
        print(f"Secondary result: {'PASS' if secondary_ok else 'FAIL'} - {secondary_msg}")
        print()

        # Test dual connectivity
        dual_ok, dual_msg = test_dual_connectivity(sock)
        print(f"Dual result: {'PASS' if dual_ok else 'FAIL'} - {dual_msg}")
        print()

        # Summary
        all_pass = primary_ok and secondary_ok and dual_ok
        print("=" * 40)
        if all_pass:
            print("🎉 ALL TESTS PASSED - Dual ESP32 setup is working!")
            print("You can now use Smart Sentry v2 in Dual ESP32 WiFi mode.")
        else:
            print("❌ SOME TESTS FAILED")
            print("Check that both ESP32 boards are:")
            print("  - Powered on and connected to the same network")
            print("  - Running the correct firmware")
            print("  - Accessible at the expected IP addresses")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\nTest interrupted by user")
    except Exception as e:
        print(f"Test error: {e}")
        sys.exit(1)
    finally:
        sock.close()

if __name__ == "__main__":
    main()
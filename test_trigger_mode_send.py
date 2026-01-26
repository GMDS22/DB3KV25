"""
Test script to verify trigger mode (M token) is being sent correctly.
This script monitors the serial port to see what commands are actually transmitted.
"""

import serial
import time
import threading

PORT = "COM8"
BAUD = 115200

def monitor_serial(port, duration=30):
    """Monitor serial port for incoming data."""
    print(f"Monitoring {port} at {BAUD} baud for {duration} seconds...")
    print("Watching for M0 (Water) or M1 (BB/Projectile) tokens...\n")
    
    try:
        ser = serial.Serial(port, BAUD, timeout=0.1)
        time.sleep(2)  # Allow Arduino to reset
        
        start_time = time.time()
        received_lines = []
        
        while (time.time() - start_time) < duration:
            if ser.in_waiting > 0:
                try:
                    line = ser.readline().decode('utf-8', errors='ignore').strip()
                    if line:
                        print(f"[RX] {line}")
                        received_lines.append(line)
                except Exception as e:
                    print(f"Read error: {e}")
            time.sleep(0.05)
        
        ser.close()
        
        print(f"\n{'='*60}")
        print("SUMMARY:")
        print(f"{'='*60}")
        print(f"Total lines received: {len(received_lines)}")
        
        # Check for mode tokens
        mode_changes = [line for line in received_lines if 'M0' in line or 'M1' in line]
        if mode_changes:
            print(f"\nMode token commands found ({len(mode_changes)}):")
            for line in mode_changes:
                if 'M1' in line:
                    print(f"  ✓ {line} ← PROJECTILE MODE")
                elif 'M0' in line:
                    print(f"  ✓ {line} ← WATER MODE")
        else:
            print("\n⚠ WARNING: No mode tokens (M0/M1) detected in any commands!")
            print("   This explains why the servo on Pin 9 isn't responding.")
        
        # Check for fire commands
        fire_commands = [line for line in received_lines if 'F1' in line]
        if fire_commands:
            print(f"\nFire commands found ({len(fire_commands)}):")
            for line in fire_commands[:5]:  # Show first 5
                print(f"  {line}")
        
        # Check for safety tokens
        safety_commands = [line for line in received_lines if 'S0' in line or 'S1' in line]
        if safety_commands:
            print(f"\nSafety state changes ({len(safety_commands)}):")
            for line in safety_commands[:5]:
                if 'S0' in line:
                    print(f"  {line} ← ARMED")
                elif 'S1' in line:
                    print(f"  {line} ← SAFE")
        
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    print("="*60)
    print("TRIGGER MODE TOKEN DIAGNOSTIC")
    print("="*60)
    print("\nINSTRUCTIONS:")
    print("1. This script will monitor COM8 for 30 seconds")
    print("2. Start your main app (run.py)")
    print("3. In the UI:")
    print("   - Select 'Projectile (BB Servo)' from Trigger Mode dropdown")
    print("   - Click ARM button (Safety: ARMED)")
    print("   - Enable tracking and auto-fire")
    print("4. Watch the output below for M1 tokens")
    print("\nPress Ctrl+C to stop early\n")
    
    input("Press ENTER to start monitoring...")
    
    try:
        monitor_serial(PORT, duration=30)
    except KeyboardInterrupt:
        print("\n\nMonitoring stopped by user.")

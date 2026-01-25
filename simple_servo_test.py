import serial
import time
import struct

def build_packet(servo_id, pos_ticks, time_ms=1000, use_xor=False):
    sid = int(servo_id) & 0xFF
    pos = max(0, min(4095, int(pos_ticks)))
    t = max(0, min(30000, int(time_ms)))

    addr = 0x2A
    length = 0x07
    instruction = 0x03
    pos_h = (pos >> 8) & 0xFF
    pos_l = pos & 0xFF
    time_h = (t >> 8) & 0xFF
    time_l = t & 0xFF

    payload = bytes([sid, length, instruction, addr, pos_h, pos_l, time_h, time_l])
    s = sum(payload) & 0xFF
    if use_xor:
        chk = (0xFF ^ s) & 0xFF
    else:
        chk = (0xFF - s) & 0xFF
    
    return b"\xFF\xFF" + payload + bytes([chk])

def test_servos(port="COM9", baud=115200):
    print(f"Opening {port} at {baud}...")
    try:
        ser = serial.Serial(port, baud, timeout=1.0)
    except Exception as e:
        print(f"Failed to open {port}: {e}")
        return

    print("Port opened. Sending moves...")
    
    # Move Pan (ID 1)
    # 0 deg ~ 0 ticks, 135 deg ~ 2048 ticks, 270 deg ~ 4095 ticks
    center = 2048
    left = 1500
    right = 2500
    
    try:
        # Try SUB checksum first (standard)
        print("Moving ID 1 (Pan) to CENTER (using SUB checksum)...")
        pkt = build_packet(1, center, 1000, use_xor=False)
        ser.write(pkt)
        time.sleep(1.5)
        
        print("Moving ID 1 (Pan) to LEFT...")
        pkt = build_packet(1, left, 1000, use_xor=False)
        ser.write(pkt)
        time.sleep(1.5)
        
        print("Moving ID 1 (Pan) to RIGHT...")
        pkt = build_packet(1, right, 1000, use_xor=False)
        ser.write(pkt)
        time.sleep(1.5)
        
        print("Moving ID 1 (Pan) back to CENTER...")
        pkt = build_packet(1, center, 1000, use_xor=False)
        ser.write(pkt)
        time.sleep(1.5)
        
        # Test Tilt (ID 2)
        print("Moving ID 2 (Tilt) to CENTER...")
        pkt = build_packet(2, center, 1000, use_xor=False)
        ser.write(pkt)
        time.sleep(1.5)
        
        print("Moving ID 2 (Tilt) UP/DOWN check...")
        pkt = build_packet(2, center + 300, 1000, use_xor=False)
        ser.write(pkt)
        time.sleep(1.5)
        
        pkt = build_packet(2, center, 1000, use_xor=False)
        ser.write(pkt)
        time.sleep(1.5)
        
    except Exception as e:
        print(f"Error during write: {e}")
    finally:
        ser.close()
        print("Closed port.")

if __name__ == "__main__":
    test_servos(port="COM9")

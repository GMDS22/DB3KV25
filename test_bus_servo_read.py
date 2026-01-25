import serial
import time
import sys

# Protocol Config
PAN_ID = 1
TILT_ID = 2
BAUD = 115200
TIMEOUT = 0.1

def calculate_checksum(payload):
    # payload is [ID, LEN, INST, PARAM1, ... PARAM_N]
    # Checksum = ~ (ID + LEN + INST + PARAM_SUM)
    s = sum(payload)
    return (~s) & 0xFF

def build_read_packet(servo_id, addr, length):
    # Instruction 0x02 = READ
    # 0xFF 0xFF ID LEN INST ADDR READ_LEN CHK
    # LEN = 4 (INST + ADDR + READ_LEN + CHK) is wrong calculation in my head?
    # Protocol: 
    # Header: FF FF
    # ID: id
    # Len: 4 (Instruction(1) + Addr(1) + ReadLen(1) + Checksum(1)) ? No, Len is usually N+2
    # Let's check the doc reference:
    # "Read present position (ADDR=0x38, LEN=2): FF FF ID 04 02 38 02 CHK"
    # ID=ID, LEN=04, INST=02, P1=38(Addr), P2=02(Len)
    # Payload for checksum: ID, LEN, INST, P1, P2
    # No wait, checksum usually excludes ID? 
    # Doc says: "CHK = 0xFF ^ (sum(bytes[2..(N-3)]) & 0xFF)"
    # bytes indices: 0=FF, 1=FF, 2=ID, 3=LEN ... 
    # Packet: FF FF [ID LEN INST PARAMS] CHK
    # So sum includes ID, LEN, INST, PARAMS.
    
    inst = 0x02
    packet_len = 4 # (Inst + P1 + P2 + Chk) - Chk is part of length usually?
    # Wait, 04 in the example: Inst(1)+Addr(1)+Len(1)+Chk(1) = 4 bytes?  
    # Packet Structure is usually: FF FF ID LEN INST P1 P2 CHK
    # If LEN is "number of parameters + 2", then Inst(1) + P1(1) + P2(1) + CHK(1) = 4? No that's 4. 
    # Feetech doc says Length = N + 2 (Parameters + 2 [Inst + Chk])
    # Here parameters are ADDR and READ_LEN. So 2 parameters.
    # Length = 2 + 2 = 4. Correct.
    
    payload = [servo_id, 4, inst, addr, length]
    chk = calculate_checksum(payload) # ~sum
    
    # Docs say: CHK = 0xFF ^ (sum & 0xFF) which is the same as ~sum & 0xFF
    
    return bytes([0xFF, 0xFF] + payload + [chk])

def test_read(port, servo_id, reg_addr, reg_len, name):
    try:
        ser = serial.Serial(port, BAUD, timeout=TIMEOUT)
    except Exception as e:
        print(f"Failed to open {port}: {e}")
        return

    print(f"Opening {port} at {BAUD}...")
    
    pkt = build_read_packet(servo_id, reg_addr, reg_len)
    print(f"Sending Read {name} to ID {servo_id}: {pkt.hex().upper()}")
    
    ser.write(pkt)
    time.sleep(0.05)
    
    resp = ser.read(64)
    print(f"Response: {resp.hex().upper()}")
    
    if len(resp) > 0:
        # validate header
        if resp.startswith(b'\xFF\xFF'):
            # Parse return
            # FF FF ID LEN ERR P1... CHK
            # Len is num params + 2 (Error + Chk)
            try:
                rid = resp[2]
                rlen = resp[3]
                err = resp[4]
                params = resp[5:-1]
                chk = resp[-1]
                
                print(f"  ID: {rid}")
                print(f"  Error: {err:02X}")
                print(f"  Data: {params.hex().upper()}")
                
                if len(params) >= 2:
                    val = (params[0] << 8) | params[1]
                     # Convert to signed 16-bit if needed (Load is often signed)
                    if val > 32767:
                        val -= 65536
                    print(f"  Value (Int): {val}")
            except Exception as e:
                print(f"  Parse Error: {e}")
    else:
        print("  No response.")

    ser.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_bus_servo_read.py <COM_PORT>")
        sys.exit(1)
    
    port_name = sys.argv[1]
    
    # Try reading Position (Addr 0x38 / 56) - known to work
    print("\n--- TEST 1: READ POSITION (0x38) ---")
    test_read(port_name, PAN_ID, 0x38, 2, "Position")

    # Try reading Load/Current (Addr 0x3C / 60) - typical for SCS/Feetech
    print("\n--- TEST 2: READ LOAD (0x3C) ---")
    test_read(port_name, PAN_ID, 0x3C, 2, "Load/Current")
    
    # Try reading Voltage (Addr 0x3E / 62) - typical (1 byte)
    print("\n--- TEST 3: READ VOLTAGE (0x3E) ---")
    test_read(port_name, PAN_ID, 0x3E, 1, "Voltage")


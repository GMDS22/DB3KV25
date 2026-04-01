# Phase 0 - Minimal Servo Test
## Objective: Verify Waveshare ESP32 + Servos Work Wirelessly (NO APP NEEDED)

---

## What You Need
1. Waveshare ESP32 board
2. Pan/Tilt servos (or any 2 serial bus servos)
3. USB cable for Waveshare (power + serial)
4. Servo power supply (9-12V)
5. Windows PC on same network

---

## Step-by-Step Test (5 minutes)

### 1. Flash Firmware (One Time)
```powershell
cd F:\DB3000V5.0 - ESP32\DB3000V4.1-main
tools\arduino-cli\arduino-cli.exe upload -p COM31 --fqbn esp32:esp32:esp32 arduino\DB3000_ESP32_UDP_PIR\DB3000_ESP32_UDP_PIR.ino
```
*(Replace COM31 with your actual port)*

**Wait for message**: `Leaving... Hard resetting via RTS pin...`

---

### 2. Monitor Boot Messages
```powershell
python read_serial.py
```

**Look for these messages** (means it worked):
```
[BOOT] DB3000_ESP32_UDP_PIR  v1
[BOOT] Starting WiFi AP: "DB3000-Turret"
[BOOT] WiFi ready at IP: 192.168.4.2
[BOOT] UART2 baud=1000000 RX=GPIO16 TX=GPIO17
[UDP] Listening on port 9001
```

**Keep this terminal running** (shows real-time servo commands)

---

### 3. Connect PC to WiFi
- PC WiFi network list → Select `DB3000-Turret`
- (No password)

**Verify**: `ipconfig` should show you got an IP like `192.168.4.x`

---

### 4. Send Simple Servo Commands (Python)
Open **new terminal** (keep read_serial.py running):

```powershell
cd F:\DB3000V5.0 - ESP32\DB3000V4.1-main
python
```

Then paste this (one line at a time):

```python
import socket
import struct
import time

def crc32(data):
    import binascii
    return binascii.crc32(data) & 0xffffffff

# Connect to ESP32
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
esp32_addr = ("192.168.4.2", 9001)

# Pan servo to 90 degrees (ID=1)
cmd_json = '{"cmd":"pan","pan":90,"time":1000}'
msg = cmd_json.encode() + b'\x00' + struct.pack('<I', crc32(cmd_json.encode()))
sock.sendto(msg, esp32_addr)
print(">>> Sent: Pan 90°")

time.sleep(2)

# Tilt servo to 90 degrees (ID=2)
cmd_json = '{"cmd":"tilt","tilt":90,"time":1000}'
msg = cmd_json.encode() + b'\x00' + struct.pack('<I', crc32(cmd_json.encode()))
sock.sendto(msg, esp32_addr)
print(">>> Sent: Tilt 90°")

time.sleep(2)

# Pan back to 0 degrees
cmd_json = '{"cmd":"pan","pan":0,"time":1000}'
msg = cmd_json.encode() + b'\x00' + struct.pack('<I', crc32(cmd_json.encode()))
sock.sendto(msg, esp32_addr)
print(">>> Sent: Pan 0°")

time.sleep(2)

# Tilt back to 0 degrees
cmd_json = '{"cmd":"tilt","tilt":0,"time":1000}'
msg = cmd_json.encode() + b'\x00' + struct.pack('<I', crc32(cmd_json.encode()))
sock.sendto(msg, esp32_addr)
print(">>> Sent: Tilt 0°")

sock.close()
print("\nDone! Check servos.")
```

---

## Expected Results

### In read_serial.py terminal:
You'll see servo commands printed (example):
```
[UDP] RX: {"cmd":"pan","pan":90,"time":1000}
[BUS] TX: 0xFF 0xFF 0x01 0x04 0x03 0x68 0x00 0xXX
[BUS] Servo 1 position: 90 (1.5ms pulse)
```

### Physical:
- **Pan servo** spins to 90°, then back to 0° ✓
- **Tilt servo** spins to 90°, then back to 0° ✓

---

## Success Criteria (Phase 0 Complete)
- [ ] Firmware flashes without errors
- [ ] Boot messages visible in serial monitor
- [ ] WiFi AP "DB3000-Turret" visible and connectable
- [ ] PC gets IP from 192.168.4.x range
- [ ] Pan servo (ID=1) responds to commands
- [ ] Tilt servo (ID=2) responds to commands
- [ ] Servos move in response to Python commands

---

## If Something Fails

| Problem | Fix |
|---------|-----|
| **Board won't flash** | Check COM port correct, restart board in bootloader mode |
| **No WiFi AP visible** | Restart ESP32, check antenna, verify firmware flashed successfully |
| **"Connection refused" error** | Check PC is on 192.168.4.x network, firewall not blocking |
| **Servos don't move** | Check servo power cable, verify ID=1 and ID=2 in firmware |
| **read_serial.py shows nothing** | Install CH340 driver, try different USB port |

---

## That's It!
Once servos respond to wireless commands, **Phase 0 is DONE**.

Next: ID3 Nano integration (Phase 1+)

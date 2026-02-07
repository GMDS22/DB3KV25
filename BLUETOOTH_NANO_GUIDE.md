# Nano + Bluetooth Serial (HC-05/HC-06) Setup Guide

Goal: keep the Arduino Nano for IO/telemetry, but replace the USB cable to the PC with a Bluetooth SPP link (virtual COM port).

This works well with DB3000 **Dual Port** mode:
- Nano = IO + telemetry (Bluetooth virtual COM)
- Debug board = PAN/TILT bus-servo (USB COM)

## 1) Hardware (wiring + power)

Typical modules:
- **HC-05 / HC-06** (Classic Bluetooth SPP) ✅ recommended
- If you have a **BLE-only module** (HM-10, etc.) that is NOT SPP: Windows won’t give you a COM port; DB3000 would need a BLE client (different approach).

Wiring (3.3V logic on BT module):
- Nano **TX (D1)** → BT **RX** (through a divider/level shift)
- Nano **RX (D0)** ← BT **TX** (direct is usually fine)
- Nano **5V** → BT **VCC** (most HC-05 boards accept 5V; if yours says 3.3V only, power it at 3.3V)
- Nano **GND** ↔ BT **GND**

Level shifting for Nano TX → BT RX:
- Use a simple divider (example): Nano TX → **1k** → BT RX, and BT RX → **2k** → GND.

## 2) Baud rate (important)

DB3000 defaults to **115200** for the Nano (see settings.json).

- Many HC-05/HC-06 modules default to **9600** in DATA mode.
- Some can be configured to 115200 via AT commands.

Recommended options:
- Option A (best latency): set the BT module DATA baud to **115200**.
- Option B (most compatible): change DB3000 Nano baud to **9600** (both in DB3000 settings and in the Nano sketch).

## 3) Windows pairing (creates COM ports)

1. Pair the HC-05/HC-06 in Windows Bluetooth settings.
2. After pairing, Windows creates one or two COM ports:
   - “Standard Serial over Bluetooth link (COMxx)”
   - Sometimes both **Incoming** and **Outgoing** ports are created.

For DB3000, you usually want the **Outgoing** COM port.

## 4) DB3000 configuration

Edit `settings.json` (or set these in the UI Serial Settings):
- `serial_device_type_index`: `2` (Dual Port)
- `com_port`: set to the **Bluetooth COM** (example: `COM12`)
- `baud_rate`: match the BT module DATA baud (example: `115200` or `9600`)
- `debug_board_com_port`: keep your USB debug board (example: `COM9`)
- `debug_board_baud_rate`: `115200`

**Current Nano sketch (keep docs updated):**
- [arduino/DB3000_Nano_IO_Telemetry_2026/DB3000_Nano_IO_Telemetry_2026.ino](arduino/DB3000_Nano_IO_Telemetry_2026/DB3000_Nano_IO_Telemetry_2026.ino)

**UI tip (new):**
- The **Port Picker** in the Connection panel lists available COM ports and tags Bluetooth ports with **[BT]**.
- Use the refresh button (⟳) after pairing the module to re-scan ports.
- Selecting a port auto-fills the COM field.

## 5) Quick probe / troubleshooting

Run the probe to list COM ports and highlight Bluetooth ports:

- `python tools/bt_serial_probe.py`

Then run the Nano IO test against the Bluetooth COM:

- `python test_nano_io.py`

If the probe can’t open the Bluetooth COM:
- Close anything that might be holding it (Arduino Serial Monitor, PuTTY, DB3000 app)
- Remove the pairing and re-pair
- Try a different BT dongle / built-in BT

Notes:
- A Bluetooth COM port typically will **not** reset the Nano when opened (no DTR reset). If you need the Nano boot banner, tap Nano reset manually.

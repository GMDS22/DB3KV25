# ESP32 Flash Workflow

This guide flashes ESP32 firmware sketches using the included Arduino CLI.

Canonical sketch mapping is maintained in [ESP32_CURRENT_SKETCH.md](ESP32_CURRENT_SKETCH.md).

Selected runtime topology: dual ESP32 WiFi.

- Primary ESP32 (IO/accessories): WiFi/UDP only during normal operation
- Secondary ESP32 (servos): WiFi/UDP servo control with integrated Yahboom driver
- No runtime USB dependency for either board
- No ESP32 USB serial required at runtime

## Prereqs
- Board: ESP32 DevKit v1 (WROOM-32)
- Arduino CLI: tools/arduino-cli/arduino-cli.exe (already in repo)
- ESP32 core installed (see setup below)

## ESP32 Core Setup (one-time)
Use the ESP32 board manager URL:
https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json

Option A (Arduino IDE):
1) File -> Preferences -> Additional Boards Manager URLs
2) Add the URL above
3) Tools -> Board -> Boards Manager -> install "esp32"

Option B (Arduino CLI):
1) arduino-cli config init
2) arduino-cli config set board_manager.additional_urls https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
3) arduino-cli core update-index
4) arduino-cli core install esp32:esp32

## Flash (PowerShell)
From repo root:

```powershell
# Primary ESP32 (IO/accessories) - Full WiFi UDP sketch
.\tools\flash_esp32_udp.ps1 -Port COM5

# Secondary ESP32 (servos) - Yahboom Servo Driver UDP sketch
.\tools\flash_esp32_udp.ps1 -Port COM6 -Sketch "arduino/DB3000_ESP32_Yahboom_Servo/DB3000_ESP32_Yahboom_Servo.ino"
```

## Dual ESP32 WiFi Setup

For fully wireless operation with separate boards for IO and servos:

```powershell
# Primary ESP32 (IO/accessories/fire/safety/LED/laser/PIR)
.\tools\flash_esp32_udp.ps1 -Port COM5

# Secondary ESP32 (Yahboom servo driver board)
.\tools\flash_esp32_udp.ps1 -Port COM6 -Sketch "arduino/DB3000_ESP32_Yahboom_Servo/DB3000_ESP32_Yahboom_Servo.ino"
```

### Dual Board Testing

After flashing both boards, test connectivity:

```powershell
python esp32_dual_board_test.py
```

This validates:
- Primary ESP32 (192.168.4.1:9000) responds to IO commands
- Secondary ESP32 (192.168.4.2:9001) responds to servo commands
- Both boards maintain simultaneous UDP connectivity

## Yahboom Board Specific Notes
- The Yahboom ESP32 servo driver board has integrated serial bus servo control
- Supports up to 253 ST/RSBL series servos
- Accepts JSON commands over UDP: `{"pan_cmd": angle, "tilt_cmd": angle, "move_time_ms": time}`
- Default servo IDs: Pan=1, Tilt=2 (configurable in app settings)
- Power: 9-25V input, matches servo voltage requirements

Add -InstallCore if you want the script to attempt core install:

```powershell
.\tools\flash_esp32_udp.ps1 -Port COM5 -InstallCore
```

## Sketch Locations
- Full WiFi UDP runtime:
	- arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino
- USB Serial IO + PIR runtime (current serial/dual-port firmware):
	- arduino/DB3000_ESP32_IO_Telemetry_2026_w_PIR/DB3000_ESP32_IO_Telemetry_2026_w_PIR.ino

Upload USB Serial IO + PIR sketch:

```powershell
.\tools\flash_esp32_udp.ps1 -Port COM5 -Sketch "arduino/DB3000_ESP32_IO_Telemetry_2026_w_PIR/DB3000_ESP32_IO_Telemetry_2026_w_PIR.ino"
```

## Library Note
- The flash script will use a repo-local ArduinoJson library at `external/ArduinoJson` when present.
- This avoids dependency on the default Arduino user libraries folder during compile.

## Defaults
- WiFi AP SSID: DB3000-ESP32
- WiFi AP password: db3000pass
- UDP port: 9000

## Pin Assignments
- GPIO16: UART2 RX from Debug Board TX
- GPIO17: UART2 TX to Debug Board RX
- GPIO27: Trigger MOSFET (Water)
- GPIO13: Trigger Servo (Projectile)
- GPIO32: LED Relay
- GPIO33: Laser Relay
- GPIO36: Pan current sensor
- GPIO39: Tilt current sensor
- GPIO34: Total current sensor

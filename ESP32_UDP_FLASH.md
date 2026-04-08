# ESP32 Flash Workflow

This guide flashes ESP32 firmware sketches using the included Arduino CLI.

Canonical sketch mapping is maintained in [ESP32_CURRENT_SKETCH.md](ESP32_CURRENT_SKETCH.md).

Selected runtime topology: Smart Sentry WiFi baseline.

Firmware sketch names are treated as content-stable identifiers. An app release bump does not require a sketch rename unless the firmware itself changed or the team intentionally wants a new firmware identity.

- Primary baseline ESP32: WiFi/UDP control for motion, trigger, PIR, relays, and telemetry
- Optional secondary ESP32: separate WiFi servo board for Dual ESP32 WiFi mode
- ESP32 USB remains useful for flashing and diagnostics
- Current single-board WiFi baseline is the existing Smart Sentry WiFi UDP PIR sketch at the documented v2.3.1 path
- That active WiFi sketch now carries the rest-position firmware contract too: it accepts `rest` config, exposes `{"action":"rest"}`, and keeps buzzer playback on the existing `{"action":"sound"}` UDP action.
- Waveshare v3 single-board bring-up uses a separate UDP bus-bridge sketch

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
# Primary ESP32 (IO/accessories) - Full WiFi UDP baseline sketch
.\tools\flash_esp32_udp.ps1 -Port COM28 -Sketch "arduino/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR.ino"

# Waveshare Servo Driver HAT (v3 single-board bridge)
.\tools\flash_esp32_udp.ps1 -Port COM5 -Sketch "arduino/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE.ino"

# Secondary ESP32 (servos) - Yahboom Servo Driver UDP sketch
.\tools\flash_esp32_udp.ps1 -Port COM6 -Sketch "arduino/DB3000_ESP32_Yahboom_Servo/DB3000_ESP32_Yahboom_Servo.ino"
```

## Dual ESP32 WiFi Setup

For fully wireless operation with separate boards for IO and servos:

```powershell
# Primary ESP32 (IO/accessories/fire/safety/LED/laser/PIR)
.\tools\flash_esp32_udp.ps1 -Port COM28 -Sketch "arduino/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR.ino"

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
- Full WiFi UDP runtime for the current Smart Sentry WiFi baseline:
	- arduino/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR.ino
- Waveshare v3 single-board UDP bus bridge:
	- arduino/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE.ino
- USB Serial IO + PIR runtime (current serial/dual-port firmware):
	- arduino/DB3000_ESP32_IO_Telemetry_2026_w_PIR/DB3000_ESP32_IO_Telemetry_2026_w_PIR.ino

The current Smart Sentry WiFi baseline sketch currently adds:
- GPIO2 status LED / external blink mirror support
- Runtime projectile trigger-servo rest angle, fire angle, and speed settings
- Optional PIR-event blink suppression controlled by the app
- Periodic pan, tilt, and total current telemetry in `state` packets
- App-triggered sweep action over UDP instead of a GPIO0 runtime button
- GPIO0 reserved strictly for ESP32 BOOT strapping

Upload the Smart Sentry WiFi baseline sketch:

```powershell
.\tools\flash_esp32_udp.ps1 -Port COM28 -Sketch "arduino/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR.ino"
```

Upload the Waveshare v3 bridge sketch:

```powershell
.\tools\flash_esp32_udp.ps1 -Port COM5 -Sketch "arduino/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE.ino"
```

Upload USB Serial IO + PIR sketch:

```powershell
.\tools\flash_esp32_udp.ps1 -Port COM5 -Sketch "arduino/DB3000_ESP32_IO_Telemetry_2026_w_PIR/DB3000_ESP32_IO_Telemetry_2026_w_PIR.ino"
```

## Library Note
- The flash script will use a repo-local ArduinoJson library at `external/ArduinoJson` when present.
- This avoids dependency on the default Arduino user libraries folder during compile.

## Defaults
- WiFi AP SSID: SMART-SENTRY-V2.3
- WiFi AP password: db3000pass
- UDP port: 9000
- Default AP IP: 192.168.4.1

Waveshare v3 bridge defaults:
- WiFi AP SSID: SMART-SENTRY-V3
- WiFi AP password: smartv3pass
- UDP port: 9000
- Default AP IP: 192.168.4.1
- Bus UART RX/TX: GPIO18/GPIO19
- Bus baud: 1000000
- Confirmed active outputs: GPIO27 trigger MOSFET, GPIO25 accessory relay, GPIO26 spare relay, GPIO4 buzzer
- Intentionally unassigned outputs: LED relay, laser relay, trigger-servo PWM, buzzer volume ADC, speaker volume ADC

If normal upload does not enter bootloader automatically, use the manual helper:

```powershell
.\tools\flash_waveshare_bridge_manual_boot.ps1 -Port COM30
```

## Pin Assignments
- GPIO18 / GPIO19: Yahboom bus-servo UART RX / TX
- GPIO27: Trigger MOSFET
- GPIO25: Accessory relay
- GPIO26: Spare relay
- GPIO4: Buzzer
- GPIO14 / GPIO15: Reserved RC / telemetry serial path
- GPIO5: Speaker reserved only
- GPIO34: Total current sensor when PIR is disabled, otherwise PIR sensor 1

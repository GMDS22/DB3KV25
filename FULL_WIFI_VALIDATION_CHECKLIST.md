# Full WiFi Flash And Validation Checklist

## Goal

Validate the selected runtime topology:

- PC <-> ESP32 over WiFi/UDP
- ESP32 UART2 <-> Debug Board
- no runtime Debug Board USB dependency

This checklist is split into bring-up, firmware verification, UDP verification, and app smoke testing.

## Hardware Preconditions

- ESP32 DevKit v1 powered and flashable over USB
- Debug Board wired to ESP32 UART2
- common ground between ESP32 and Debug Board
- bus servos powered correctly
- expected UART2 wiring on DevKit v1:
  - GPIO16 = RX2 from Debug Board TX
  - GPIO17 = TX2 to Debug Board RX

## Firmware Target

Default firmware for this topology:

- [DB3000V4.1-main/arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino](DB3000V4.1-main/arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino)

## Phase 1: Flash Firmware

Reference doc:

- [DB3000V4.1-main/ESP32_UDP_FLASH.md](DB3000V4.1-main/ESP32_UDP_FLASH.md)

Flash commands from repo root:

```powershell
.\tools\arduino-cli\arduino-cli.exe board list
.\tools\flash_esp32_udp.ps1 -Port COM5
```

If ESP32 core is not installed:

```powershell
.\tools\flash_esp32_udp.ps1 -Port COM5 -InstallCore
```

Expected defaults after flash:

- SSID: `DB3000-ESP32`
- password: `db3000pass`
- ESP32 IP: `192.168.4.1`
- UDP port: `9000`

## Phase 2: Network Bring-Up

From the PC:

- join WiFi network `DB3000-ESP32`
- confirm the PC gets a `192.168.4.x` address
- verify basic route to `192.168.4.1`

Expected result:

- UDP scripts should report the local route IP on the `192.168.4.x` subnet

## Phase 3: Primary UDP Verification

Primary tool:

- [DB3000V4.1-main/esp32_udp_command_verify.py](DB3000V4.1-main/esp32_udp_command_verify.py)

Minimum verification command:

```powershell
python .\DB3000V4.1-main\esp32_udp_command_verify.py --settings .\DB3000V4.1-main\settings.json --bus-ping
```

Movement verification command:

```powershell
python .\DB3000V4.1-main\esp32_udp_command_verify.py --settings .\DB3000V4.1-main\settings.json --bus-ping --do-move --move-time-ms 1200
```

If servo IDs need to be forced explicitly:

```powershell
python .\DB3000V4.1-main\esp32_udp_command_verify.py --settings .\DB3000V4.1-main\settings.json --config-bus-pan-id 1 --config-bus-tilt-id 2 --bus-ping --do-move
```

Expected success signals:

- `hello` ACK received
- `encoder_request` ACK received
- `bus_ping` ACK received
- `state` packets received
- `state.bus` contains:
  - `send_count`
  - `baud`
  - `chk_mode`
  - `last_sent_pan`
  - `last_sent_tilt`

Acceptable outcomes:

- `pan_ok` or `tilt_ok` true
- or `bridge_rx_ok` true when the bridge path is healthy but strict ping signatures are not seen

## Phase 4: Firmware Log And Bus Diagnostic

Bring-up tool:

- [DB3000V4.1-main/esp32_current_setup_diagnostic.py](DB3000V4.1-main/esp32_current_setup_diagnostic.py)

Use this while ESP32 is still connected by USB for serial logs:

```powershell
python .\DB3000V4.1-main\esp32_current_setup_diagnostic.py --com COM5 --settings .\DB3000V4.1-main\settings.json
```

With movement request:

```powershell
python .\DB3000V4.1-main\esp32_current_setup_diagnostic.py --com COM5 --settings .\DB3000V4.1-main\settings.json --send-move --pan 130 --tilt 60 --move-time-ms 1200
```

Expected serial-log markers:

- boot banner
- WiFi AP started
- UDP port ready
- hello or command reception logs
- UART2 / bus diagnostics

Important note:

- this script is a bring-up tool, not a runtime requirement
- runtime success must not depend on keeping the ESP32 USB serial attached after deployment

## Phase 5: Main App Smoke Test

In the app configuration:

- select the future full-WiFi mode once implemented
- set host to `192.168.4.1`
- set UDP port to `9000`
- leave local port `0`
- do not require COM ports in this mode

Manual smoke checks:

- connect succeeds with WiFi fields only
- pan/tilt manual movement works
- safety toggle works
- LED toggle works
- laser toggle works
- trigger mode change propagates
- manual fire works when safety is armed

Tracking smoke checks:

- tracking starts without transport errors
- turret movement follows targets
- no tracking-code edits are needed to achieve this

## Optional Legacy / Lab Tools

These are not primary for full WiFi, but remain useful in lab bring-up:

- [DB3000V4.1-main/test_bus_servo_read.py](DB3000V4.1-main/test_bus_servo_read.py)
  - only useful when the Debug Board is directly exposed as a PC COM device
- [DB3000V4.1-main/test_nano_io.py](DB3000V4.1-main/test_nano_io.py)
  - USB IO-board check, not primary for the selected topology
- [DB3000V4.1-main/tools/servo_move_test_over_usb.py](DB3000V4.1-main/tools/servo_move_test_over_usb.py)
  - USB movement path check, not primary for the selected topology

## Failure Signatures

### No UDP ACK at all

Likely causes:

- PC is not connected to `DB3000-ESP32`
- wrong host or UDP port
- ESP32 firmware did not boot correctly

Primary checks:

- rerun the flash workflow
- confirm PC route IP is `192.168.4.x`
- rerun `esp32_udp_command_verify.py`

### UDP works but `bus_ping` shows zero RX bytes

Likely causes:

- UART2 wiring problem
- Debug Board not powered
- servo chain not powered
- wrong baud or no bus response path

Primary checks:

- inspect GPIO16/GPIO17 wiring
- inspect common ground
- inspect bus-servo power path

### UDP works and RX bytes exist, but no valid servo packet

Likely causes:

- checksum mismatch
- protocol variant mismatch
- noisy line-level behavior

Primary checks:

- inspect `chk_mode` in diagnostic output
- retest with the current firmware’s bus ping behavior

### App still asks for COM ports in the selected mode

Likely cause:

- main app connection mode semantics were not updated yet

Primary fix:

- implement the UI and validation changes described in [DB3000V4.1-main/FULL_WIFI_IMPLEMENTATION_PLAN.md](DB3000V4.1-main/FULL_WIFI_IMPLEMENTATION_PLAN.md)

## Acceptance Checklist

- firmware flashed successfully
- ESP32 AP visible and joinable
- UDP hello and state responses confirmed
- `bus_ping` confirms UART2 path health
- manual movement over UDP confirmed
- manual fire and accessory control over UDP confirmed
- app connects with WiFi settings only
- no runtime dependency on Debug Board USB remains

## Recommended Operator Flow

1. Flash ESP32 UDP firmware.
2. Join the ESP32 AP.
3. Run `esp32_udp_command_verify.py`.
4. Run `esp32_current_setup_diagnostic.py` during bring-up if needed.
5. Run the app in full-WiFi mode and perform manual smoke tests.
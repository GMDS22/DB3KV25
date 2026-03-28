# Full WiFi Implementation Plan

## Scope

Implement the selected topology:

- PC <-> ESP32 over WiFi/UDP only
- ESP32 UART2 <-> Debug Board RX/TX
- no runtime Debug Board USB dependency
- no changes to tracking, aiming, sentry target generation, or detection math

## Non-Goals

Do not modify:

- tracking PID logic
- target lock behavior
- sentry path planning or scoring
- detection pause behavior
- YOLO or camera pipeline

The transport layer changes must stay below the tracking stack.

## Implementation Order

1. Standardize the WiFi firmware target.
2. Make the main app expose a first-class full-WiFi mode.
3. Make the UDP path the primary validation path.
4. Update operator-facing docs and stale COM-centric wording.

## File-By-File Plan

### 1. Primary firmware

File: [DB3000V4.1-main/arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino](DB3000V4.1-main/arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino)

Changes to implement:

- Declare this as the canonical full-WiFi runtime firmware in the file header comments.
- Keep the existing UDP JSON+CRC32 protocol unchanged.
- Keep support for:
  - `pan_cmd`
  - `tilt_cmd`
  - `fire`
  - `safety`
  - `mode`
  - `led`
  - `laser`
  - `rapid_fire`
  - `move_time_ms`
  - `action=config`
  - `action=encoder_request`
  - `action=bus_ping`
  - `action=test`
- Preserve `ack`, `state`, and `cap` payload shape so the app does not need protocol changes beyond topology selection.
- Keep UART2 bus-servo ping and checksum locking logic intact.
- Confirm `state["bus"]` fields remain populated because the validation scripts depend on them.

Optional cleanup:

- Fold any missing behavior from the legacy direct-debugboard sketch into this one, then retire the duplicate firmware from operator docs.

### 2. Legacy duplicate firmware

File: [DB3000V4.1-main/arduino/DB3000_ESP32_DIRECT_DEBUGBOARD/DB3000_ESP32_DIRECT_DEBUGBOARD.ino](DB3000V4.1-main/arduino/DB3000_ESP32_DIRECT_DEBUGBOARD/DB3000_ESP32_DIRECT_DEBUGBOARD.ino)

Changes to implement:

- Decide whether to keep or retire it.
- If kept, mark it as legacy or experimental in header comments.
- If retired, update docs to stop recommending it as a primary deployment target.

Recommendation:

- keep one canonical WiFi runtime sketch only

### 3. Main app connection-mode model

File: [DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py](DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py)

Changes to implement:

- Add an explicit fourth connection mode for full WiFi, matching Smart Sentry v2.
- Keep old indices compatible where possible.

Recommended final mode model:

- `0` = ESP32 USB
- `1` = Debug Board USB direct
- `2` = Dual USB / legacy hybrid
- `3` = ESP32 WiFi, Debug Board on ESP32

Functions and areas to update:

- serial mode combo creation and tooltip text
- `_serial_device_type_index()` docstring and helper logic
- add helper such as `_serial_is_wifi_full()`
- `_update_connection_panel_visibility()`
- connect validation inside `connect_serial()`
- connect button wording and status label text
- startup auto-connect semantics when only WiFi settings are present

Exact behavior to implement:

- full-WiFi mode should require only `esp32_host` and `esp32_port`
- full-WiFi mode should not require `com_port`
- full-WiFi mode should not require `debug_board_com_port`
- full-WiFi mode should hide Debug Board COM fields
- full-WiFi mode should hide primary COM fields
- full-WiFi mode should show ESP32 UDP fields

### 4. Main app command routing

File: [DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py](DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py)

Function focus: `send_serial_command()`

Changes to implement:

- add a full-WiFi routing branch that sends motion and IO entirely through `esp32_link`
- do not attempt `_bus_servo_send_pan_tilt()` in that mode
- do not require `self.ser` or `self.bus_ser` in that mode
- keep existing payload keys unchanged to avoid protocol churn

Required routing outcome in full-WiFi mode:

- `pan_cmd` and `tilt_cmd` go over UDP
- `fire`, `safety`, `mode`, `led`, `laser` go over UDP
- `rapid_fire` stays in config or runtime UDP payloads as currently supported

Things to preserve:

- redundant-command filtering behavior
- last-sent state bookkeeping
- `esp32_link` event draining each control cycle
- current protection output gating
- tilt safety output gating

### 5. Main app settings persistence

Files:

- [DB3000V4.1-main/settings.json](DB3000V4.1-main/settings.json)
- [DB3000V4.1-main/preferred_defaults.json](DB3000V4.1-main/preferred_defaults.json)
- [DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py](DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py)

Changes to implement:

- persist the new full-WiFi mode index cleanly
- keep `esp32_host`, `esp32_port`, and `esp32_local_port`
- ensure old COM-based values do not block connection when full-WiFi mode is selected
- set sensible defaults for the new topology in the checked-in sample settings if desired

Recommended default values for full WiFi:

- `serial_device_type_index = 3`
- `esp32_host = 192.168.4.1`
- `esp32_port = 9000`
- `esp32_local_port = 0`

### 6. Help and UI wording

File: [DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py](DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py)

Changes to implement:

- update connection mode labels
- update tooltip text so operators understand that the Debug Board is behind ESP32 UART2 in full-WiFi mode
- update the ESP32 pin assignment help window to present the full-WiFi topology as a primary deployment path, not only “UDP link mode” wording

### 7. Smart Sentry v2 alignment

Files:

- [DB3000V4.1-main/app/sentry_v2/sentry_v2_comm.py](DB3000V4.1-main/app/sentry_v2/sentry_v2_comm.py)
- [DB3000V4.1-main/app/sentry_v2/sentry_v2_tab.py](DB3000V4.1-main/app/sentry_v2/sentry_v2_tab.py)
- [DB3000V4.1-main/SMART_SENTRY_MANUAL.md](DB3000V4.1-main/SMART_SENTRY_MANUAL.md)

Changes to implement:

- keep Smart Sentry v2’s mode naming as the model for the main app
- update the main app wording to match “Full WiFi” terminology already present in Sentry v2
- avoid having two conflicting mode taxonomies in the same repo

### 8. Flash workflow

Files:

- [DB3000V4.1-main/ESP32_UDP_FLASH.md](DB3000V4.1-main/ESP32_UDP_FLASH.md)
- [DB3000V4.1-main/tools/flash_esp32_udp.ps1](DB3000V4.1-main/tools/flash_esp32_udp.ps1)

Changes to implement:

- state clearly that this is the default flashing path for full-WiFi deployment
- keep the default sketch set to `DB3000_ESP32_UDP_Link`
- document the expected AP name, password, and UDP port as deployment defaults

### 9. Validation tools

Files:

- [DB3000V4.1-main/esp32_udp_command_verify.py](DB3000V4.1-main/esp32_udp_command_verify.py)
- [DB3000V4.1-main/esp32_current_setup_diagnostic.py](DB3000V4.1-main/esp32_current_setup_diagnostic.py)
- [DB3000V4.1-main/test_nano_io.py](DB3000V4.1-main/test_nano_io.py)
- [DB3000V4.1-main/tools/servo_move_test_over_usb.py](DB3000V4.1-main/tools/servo_move_test_over_usb.py)

Changes to implement:

- promote the UDP scripts as the primary validation path
- demote or relabel the USB serial scripts as bring-up or legacy tools
- optionally add one dedicated WiFi movement smoke test wrapper if you want one-command operator verification

### 10. Architecture docs

Files to update:

- [DB3000V4.1-main/README.md](DB3000V4.1-main/README.md)
- [DB3000V4.1-main/CHANGE_IMPACT_REFERENCE.md](DB3000V4.1-main/CHANGE_IMPACT_REFERENCE.md)
- [DB3000V4.1-main/BLUETOOTH_NANO_GUIDE.md](DB3000V4.1-main/BLUETOOTH_NANO_GUIDE.md)
- [DB3000V4.1-main/ARDUINO_SERIALBUS_SERVO_UPGRADE_2026.md](DB3000V4.1-main/ARDUINO_SERIALBUS_SERVO_UPGRADE_2026.md)
- [DB3000V4.1-main/.github/copilot-instructions.md](DB3000V4.1-main/.github/copilot-instructions.md)
- [DB3000V4.1-main/RECENT_UPDATES.json](DB3000V4.1-main/RECENT_UPDATES.json)

Changes to implement:

- replace COM-centric “Dual Port is primary” wording where appropriate
- describe full WiFi as the selected runtime topology
- clearly state that Debug Board USB is not required in that topology
- keep dual USB documented only as a legacy or alternate bring-up path if still supported

## Acceptance Criteria

- app can connect with WiFi settings only
- manual movement works through UDP
- fire, safety, LED, and laser work through UDP
- `bus_ping` confirms UART2 and Debug Board path through ESP32
- health/current state still updates from UDP state frames
- no part of the main app requires Debug Board USB for normal runtime in full-WiFi mode

## Recommended First Code Pass

If implementation starts now, the first pass should touch only:

- [DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py](DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py)
- [DB3000V4.1-main/ESP32_UDP_FLASH.md](DB3000V4.1-main/ESP32_UDP_FLASH.md)
- [DB3000V4.1-main/esp32_udp_command_verify.py](DB3000V4.1-main/esp32_udp_command_verify.py)
- [DB3000V4.1-main/README.md](DB3000V4.1-main/README.md)

Keep the firmware unchanged unless testing exposes a real protocol or state-reporting gap.
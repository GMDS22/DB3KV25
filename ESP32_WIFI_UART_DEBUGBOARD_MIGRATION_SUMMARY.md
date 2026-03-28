# ESP32 WiFi + UART Debug Board Migration Summary

Related planning documents:

- [DB3000V4.1-main/FULL_WIFI_IMPLEMENTATION_PLAN.md](DB3000V4.1-main/FULL_WIFI_IMPLEMENTATION_PLAN.md)
- [DB3000V4.1-main/FULL_WIFI_VALIDATION_CHECKLIST.md](DB3000V4.1-main/FULL_WIFI_VALIDATION_CHECKLIST.md)

## Goal

Retarget the app from a topology that depends on the Debug Board being visible to the PC over USB to a topology where:

- the PC talks to the ESP32 only, over either USB serial or WiFi/UDP
- the ESP32 talks to the Debug Board over UART2
- pan/tilt bus-servo control stays off the tracking stack and inside the transport/firmware layer
- existing tracking, aiming, sentry, and detection logic remain unchanged

## Selected Target Topology

You selected full WiFi.

The implementation target is:

- PC <-> ESP32 over WiFi/UDP only
- ESP32 UART2 <-> Debug Board RX/TX
- no Debug Board USB connection required at runtime
- no ESP32 USB serial required at runtime

What this means operationally:

- the PC sends all motion and IO over `esp32_link`
- the ESP32 firmware owns pan/tilt forwarding to the Debug Board
- the main app should treat this as the primary topology, not as a fallback special case

## Immediate Architecture Consequence

For full WiFi, the host-side packed ASCII command remains useful as an internal compatibility format, but it is no longer the operator-facing transport. The primary transport becomes the UDP JSON+CRC32 protocol already implemented by [DB3000V4.1-main/app/esp32_link.py](DB3000V4.1-main/app/esp32_link.py#L1).

## Current Codebase Status

### Main app transport layer

The main app currently supports three routing modes in [DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py](DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py#L10228):

- mode `0`: primary ESP32 ASCII/IO
- mode `1`: Debug Board bus-servo direct
- mode `2`: Dual Port, with ESP32 on one PC link and Debug Board on a second PC link

The actual command routing in [DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py](DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py#L26952) already separates three cases:

- bus-servo pan/tilt direct to a Debug Board COM port
- full ASCII command over primary serial
- full UDP JSON command over `esp32_link`

This means tracking code is already decoupled from the physical board topology. The migration should stay inside connection selection, firmware, and docs.

### Existing firmware candidates

There are already multiple firmware sketches in the repo:

- [DB3000V4.1-main/arduino/DB3000_ESP32_IO_Telemetry_2026/DB3000_ESP32_IO_Telemetry_2026.ino](DB3000V4.1-main/arduino/DB3000_ESP32_IO_Telemetry_2026/DB3000_ESP32_IO_Telemetry_2026.ino): USB serial IO-only firmware for Dual Port. No pan/tilt forwarding.
- [DB3000V4.1-main/arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino](DB3000V4.1-main/arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino): WiFi/UDP firmware for ESP32 DevKit v1 with Debug Board on UART2.
- [DB3000V4.1-main/arduino/DB3000_ESP32_DIRECT_DEBUGBOARD/DB3000_ESP32_DIRECT_DEBUGBOARD.ino](DB3000V4.1-main/arduino/DB3000_ESP32_DIRECT_DEBUGBOARD/DB3000_ESP32_DIRECT_DEBUGBOARD.ino): WiFi/UDP direct-to-Debug-Board topology for ESP32 DevKit v1.
- [DB3000V4.1-main/arduino/DB3000_ESP32CAM_SerialBus/DB3000_ESP32CAM_SerialBus.ino](DB3000V4.1-main/arduino/DB3000_ESP32CAM_SerialBus/DB3000_ESP32CAM_SerialBus.ino): host USB serial plus UART2 Debug Board forwarding, but targeted at ESP32-CAM pin mapping rather than the current ESP32 DevKit v1 wiring.

Key full-WiFi conclusion:

- the repo already has two relevant DevKit-v1 WiFi firmwares
- the migration does not require inventing a new transport protocol
- the main work is standardizing one firmware, then aligning the main app UI, settings semantics, scripts, and docs around that firmware

### Smart Sentry v2 is ahead of the main app here

[DB3000V4.1-main/app/sentry_v2/sentry_v2_comm.py](DB3000V4.1-main/app/sentry_v2/sentry_v2_comm.py#L1) already models four distinct connection modes:

- ESP32 USB only
- ESP32 USB + Debug Board USB
- ESP32 WiFi + Debug Board USB
- ESP32 WiFi with Debug Board on ESP32

The main app does not expose those same topology choices explicitly, even though parts of the runtime already support them.

## Commands and Protocol Surfaces That Matter

### ASCII host command that remains internal compatibility only

The main app still builds the packed ASCII command in [DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py](DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py#L26742):

`P{pan}T{tilt}F{fire}L{led}R{laser}G{acc}S{safety}M{mode}\n`

For the selected full-WiFi topology, this command should not be the primary operator-facing transport. It remains relevant only for:

- backward compatibility
- internal parity checks against the USB/ASCII path
- Smart Sentry v2 mode naming consistency, where mode `3` describes full wireless ASCII-equivalent control over UDP

### UDP command payloads that must remain supported

`esp32_link` sends JSON+CRC32 packets from [DB3000V4.1-main/app/esp32_link.py](DB3000V4.1-main/app/esp32_link.py#L88). The active payload shapes used by the main app are:

- motion and IO: `pan_cmd`, `tilt_cmd`, `fire`, `safety`, `mode`, `led`, `laser`
- IO-only hybrid packets: `fire`, `safety`, `mode`, `led`, `laser`
- config action: `action=config` plus limits, home, trigger, rapid_fire, current protection, tilt safety
- diagnostics: `action=encoder_request`, `action=bus_ping`, `action=test`
- motion visibility override: `move_time_ms`

These are already accepted by the UDP firmware in:

- [DB3000V4.1-main/arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino](DB3000V4.1-main/arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino#L1023)
- [DB3000V4.1-main/arduino/DB3000_ESP32_DIRECT_DEBUGBOARD/DB3000_ESP32_DIRECT_DEBUGBOARD.ino](DB3000V4.1-main/arduino/DB3000_ESP32_DIRECT_DEBUGBOARD/DB3000_ESP32_DIRECT_DEBUGBOARD.ino#L461)

### IO-only token path that becomes less central

Dual Port currently sends separate `S`, `M`, then packed `F/L/R/G` tokens in [DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py](DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py#L27108). This remains relevant only if a two-link fallback topology is still retained.

### PTEN compatibility

Existing serial-bus forwarding sketches include `PTEN` compatibility for disabling pan/tilt output in split topologies. If the chosen final topology is single-link ESP32-only, `PTEN` becomes optional compatibility behavior rather than a primary control surface.

## What Must Be Implemented

### 1. Standardize full WiFi as the primary transport topology

Implementation choice:

- standardize on ESP32 WiFi/UDP as the primary PC link
- connect the Debug Board only to ESP32 UART2
- retire any runtime assumption that the Debug Board must appear as a PC COM device

Practical outcome:

- the app must prefer `esp32_link` as the main command path for this topology
- the firmware, not the app, owns the forwarding from ESP32 to Debug Board
- the existing “COM blank = ESP32-only mode” behavior in [DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py](DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py#L17760) becomes the intended primary behavior, not an edge path

### 2. Standardize one ESP32 DevKit v1 WiFi firmware

For full WiFi, the preferred firmware candidates are:

- [DB3000V4.1-main/arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino](DB3000V4.1-main/arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino)
- [DB3000V4.1-main/arduino/DB3000_ESP32_DIRECT_DEBUGBOARD/DB3000_ESP32_DIRECT_DEBUGBOARD.ino](DB3000V4.1-main/arduino/DB3000_ESP32_DIRECT_DEBUGBOARD/DB3000_ESP32_DIRECT_DEBUGBOARD.ino)

Recommended choice:

- standardize on [DB3000V4.1-main/arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino](DB3000V4.1-main/arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino) as the primary full-WiFi firmware because it is the more complete diagnostic build and already accepts the active app payloads

Required firmware behavior:

- accept UDP JSON+CRC32 commands from `esp32_link`
- accept `pan_cmd`, `tilt_cmd`, `fire`, `safety`, `mode`, `led`, `laser`, `rapid_fire`, `move_time_ms`
- keep `action=config`, `action=encoder_request`, `action=bus_ping`, and `action=test`
- forward pan/tilt to the Debug Board over UART2
- drive local trigger and relay pins on the ESP32
- emit `ack`, `state`, and `cap` replies used by the app and diagnostics

Firmware decision still required:

- either make `DB3000_ESP32_UDP_Link` the only supported full-WiFi firmware
- or merge any missing compatibility behavior from `DB3000_ESP32_DIRECT_DEBUGBOARD` into it and retire the duplicate sketch

### 3. Main app connection UX must be made explicit for full WiFi

The runtime can already do more than the UI admits.

Required app-side cleanup in [DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py](DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py):

- rename the mode labels so they reflect topology, not only COM count
- make the “ESP32 WiFi with Debug Board on ESP32” path explicit in the UI
- stop implying that Debug Board mode requires Debug Board USB
- expose WiFi fields for the full-wireless path without forcing the operator through the current Debug Board COM semantics
- keep saved settings compatible, but add a clearer migration path from the current `serial_device_type_index`

Likely affected areas:

- connection mode labels and tooltip copy near [DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py](DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py#L3318)
- connection field visibility in [DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py](DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py#L10354)
- connect validation logic in [DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py](DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py#L17718)
- pin assignment help in [DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py](DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py#L8051)

Important current mismatch:

- the UI text around [DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py](DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py#L3318) still describes three COM-centric modes
- Smart Sentry v2 already names a full-wireless mode explicitly in [DB3000V4.1-main/app/sentry_v2/sentry_v2_comm.py](DB3000V4.1-main/app/sentry_v2/sentry_v2_comm.py#L8)

### 4. Preserve tracking by not editing the tracking stack

Do not modify:

- target generation
- sentry logic
- update_frame tracking math
- PID or precision logic
- detection pause behavior

The only safe host-side edits are in:

- connection mode selection
- transport opening and validation
- firmware selection documentation
- optional command routing labels or mode guards

### 5. Align Smart Sentry v2 and main app connection naming

Smart Sentry v2 already has the correct conceptual topology model. The main app should match it.

Files to align:

- [DB3000V4.1-main/app/sentry_v2/sentry_v2_comm.py](DB3000V4.1-main/app/sentry_v2/sentry_v2_comm.py)
- [DB3000V4.1-main/app/sentry_v2/sentry_v2_tab.py](DB3000V4.1-main/app/sentry_v2/sentry_v2_tab.py#L1125)
- [DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py](DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py)

This is mainly naming and operator UX consistency, not tracking logic.

### 6. Update operational scripts and validation tools for UDP-first runtime

These scripts currently still describe older assumptions and should be retargeted after the firmware choice is finalized:

- [DB3000V4.1-main/esp32_udp_command_verify.py](DB3000V4.1-main/esp32_udp_command_verify.py): this should become the primary command-path verification tool
- [DB3000V4.1-main/esp32_current_setup_diagnostic.py](DB3000V4.1-main/esp32_current_setup_diagnostic.py): this should become the primary runtime diagnostic tool
- [DB3000V4.1-main/tools/flash_esp32_udp.ps1](DB3000V4.1-main/tools/flash_esp32_udp.ps1): this should remain, but the docs should explicitly state it is the default flashing path for the chosen topology
- [DB3000V4.1-main/test_nano_io.py](DB3000V4.1-main/test_nano_io.py): likely demote or rename, since it validates USB IO-board behavior rather than the new UDP-first runtime
- [DB3000V4.1-main/tools/servo_move_test_over_usb.py](DB3000V4.1-main/tools/servo_move_test_over_usb.py): demote or replace with a UDP movement test for the chosen runtime topology

For full WiFi, there should be a single operator-facing validation flow:

- flash ESP32 UDP firmware
- join ESP32 AP
- run UDP command verification
- run current/bus diagnostic
- only use USB serial scripts for bring-up or recovery, not as the primary runtime test path

## Documentation That Must Be Updated

These files currently encode the old “Debug Board must be on PC USB” or older Dual Port assumptions and should be revised after implementation:

- [DB3000V4.1-main/README.md](DB3000V4.1-main/README.md#L122)
- [DB3000V4.1-main/CHANGE_IMPACT_REFERENCE.md](DB3000V4.1-main/CHANGE_IMPACT_REFERENCE.md#L12)
- [DB3000V4.1-main/SMART_SENTRY_MANUAL.md](DB3000V4.1-main/SMART_SENTRY_MANUAL.md#L327)
- [DB3000V4.1-main/ESP32_UDP_FLASH.md](DB3000V4.1-main/ESP32_UDP_FLASH.md)
- [DB3000V4.1-main/BLUETOOTH_NANO_GUIDE.md](DB3000V4.1-main/BLUETOOTH_NANO_GUIDE.md)
- [DB3000V4.1-main/ARDUINO_SERIALBUS_SERVO_UPGRADE_2026.md](DB3000V4.1-main/ARDUINO_SERIALBUS_SERVO_UPGRADE_2026.md)
- [DB3000V4.1-main/.github/copilot-instructions.md](DB3000V4.1-main/.github/copilot-instructions.md)

Also update [DB3000V4.1-main/RECENT_UPDATES.json](DB3000V4.1-main/RECENT_UPDATES.json) when the implementation lands.

## Minimal-Risk Implementation Plan

### Phase 1: Firmware standardization

- standardize `DB3000_ESP32_UDP_Link` as the chosen runtime firmware, or merge and retire the duplicate direct-debugboard sketch
- confirm UART2 pin mapping and Debug Board wiring on the actual ESP32 board you will deploy
- validate trigger, relays, safety, and pan/tilt outside the main app first

### Phase 2: Main app UX cleanup

- update connection mode labels and visibility logic around the selected full-WiFi topology
- keep `send_serial_command()` behavior functionally identical for target generation
- only change transport selection semantics and naming where needed

### Phase 3: Tests and scripts

- retarget quick hardware tests to the UDP-first topology
- ensure flashing docs point to the chosen UDP sketch
- make the UDP diagnostic scripts the primary validation path

### Phase 4: Documentation pass

- update operator docs
- update architecture references
- record the new default topology clearly so future work does not regress back to the old Dual Port assumption

## Verification Checklist

- manual pan/tilt still tracks correctly with no changes to tracking parameters
- manual fire, laser, LED, and safety still work
- current and state telemetry still populate the monitor path used by the chosen transport
- reconnect after app restart works with saved settings
- sentry v2 mode descriptions match the main app descriptions
- no code path falls back to direct Debug Board USB assumptions when that hardware is absent

## Final Recommendation

Implement the migration as a UDP-first transport and firmware retarget, not as a tracking refactor.

Chosen path:

- PC <-> ESP32 over WiFi/UDP
- Debug Board behind ESP32 UART2
- standardize the existing ESP32 UDP firmware as the runtime target
- update the main app and docs so full wireless is a first-class topology instead of an implicit side path

That keeps tracking untouched, removes the current dependency on Debug Board USB, and aligns the main app with the topology Smart Sentry v2 already models explicitly.

## Concrete File Priority For Full WiFi Implementation

### First priority

- [DB3000V4.1-main/arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino](DB3000V4.1-main/arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino)
- [DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py](DB3000V4.1-main/app/MAIN_FILE_SINGLE_CAM.py)

### Second priority

- [DB3000V4.1-main/ESP32_UDP_FLASH.md](DB3000V4.1-main/ESP32_UDP_FLASH.md)
- [DB3000V4.1-main/tools/flash_esp32_udp.ps1](DB3000V4.1-main/tools/flash_esp32_udp.ps1)
- [DB3000V4.1-main/esp32_udp_command_verify.py](DB3000V4.1-main/esp32_udp_command_verify.py)
- [DB3000V4.1-main/esp32_current_setup_diagnostic.py](DB3000V4.1-main/esp32_current_setup_diagnostic.py)

### Third priority

- [DB3000V4.1-main/README.md](DB3000V4.1-main/README.md)
- [DB3000V4.1-main/CHANGE_IMPACT_REFERENCE.md](DB3000V4.1-main/CHANGE_IMPACT_REFERENCE.md)
- [DB3000V4.1-main/SMART_SENTRY_MANUAL.md](DB3000V4.1-main/SMART_SENTRY_MANUAL.md)
- [DB3000V4.1-main/app/sentry_v2/sentry_v2_comm.py](DB3000V4.1-main/app/sentry_v2/sentry_v2_comm.py)
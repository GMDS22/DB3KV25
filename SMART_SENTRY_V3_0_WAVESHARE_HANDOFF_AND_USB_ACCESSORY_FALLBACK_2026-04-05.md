# Smart Sentry v3.0 Waveshare Handoff And USB Accessory Fallback

Date: 2026-04-05

## Final Decision For This Attempt

Stop the current single-board Waveshare WiFi bridge attempt here.

The board is still useful, but not in the originally targeted topology.

Approved fallback direction:

- keep the Waveshare on-board servo driver on USB for pan and tilt
- keep the on-board ESP32 only for accessory control
- do not rely on the Waveshare ESP32 SoftAP plus UDP bridge path for runtime motion control right now
- keep the physical setup to one board even though motion and accessories are no longer sharing the same WiFi bridge path

This preserves the key practical win:

- one physical board instead of the previous multi-board bench setup

## Original Goal

The attempted topology was:

- PC to Waveshare ESP32 over WiFi UDP only
- Waveshare ESP32 to Yahboom serial bus as the only bus master
- Waveshare ESP32 directly owning local accessories on the Pi-style 40-pin header
- no separate Debug Board in the runtime path

## What Was Successfully Fixed Or Verified

### Firmware And Repo Alignment Work

The following items were completed successfully in the repo.

- locked the Waveshare bridge bus path to:
  - bus UART RX `GPIO18`
  - bus UART TX `GPIO19`
  - bus baud `1000000`
- corrected Yahboom motion packet byte order to:
  - `POS_L POS_H TIME_L TIME_H`
- removed the dedicated hardware arm switch requirement from the bridge path
- updated capability reporting so the app no longer expects assigned LED, laser, or trigger-servo outputs
- aligned the app UI and documentation to the switchless bridge contract
- aligned the companion full-pin test sketch to the same bus assumptions

### Flashing And Build Outcomes

- the Waveshare bridge sketch compiled successfully multiple times
- manual flashing to `COM30` succeeded
- direct `esptool` flashing to `COM30` also succeeded once the board was in the correct bootloader state
- the flashed firmware booted correctly and printed expected serial boot logs

### Tooling And Bench Validation Outcomes

- the Waveshare UDP debugger launched and sent traffic correctly
- the standalone bench tool sent correctly formed `hello`, `hb`, `cmd`, and `bus_ping` packets
- serial logs confirmed that the flashed image actually changed when new revisions were flashed

## What Failed

The failures were not random anymore by the end. They narrowed down to one specific region.

### What Was Not The Problem

By the end of this attempt, the following were ruled out as the main blocker.

- not the repo documentation
- not the app packet format
- not the Waveshare debugger
- not the basic firmware boot process
- not the ability to compile the bridge
- not the ability to flash the board
- not the existence of the SoftAP configuration values in source

### What Still Failed

The remaining failure after the later retest is the full motion-capable single-board bridge path.

Observed behavior across the attempt:

- the Step 7 A3 single-board firmware reached a stable WiFi plus UDP state
- direct probing against `192.168.4.1:9000` succeeded for `bus_ping` and motion commands on the stable Step 7 A3 firmware
- the app-side movement failure at that stage was traced to `connection_type 4` instead of the correct single-board mode `3`
- the later Step 7.6 state-machine build stayed network-stable but could not test motion because servo writes are compiled only at `REINTRO_STEP >= 9`
- the later Step 9 state-machine build became unstable during direct motion-path validation after initial command acceptance
- no visible servo movement was observed by the user during the Step 9 validation attempt
- the staged reintroduction sketch was then found to still default to `250000` baud even though the vendor-aligned bridge path uses `1000000`
- a `1000000` baud Step 9 state-machine build was compiled, but bench validation of that build was not performed because testing was stopped

That means the unresolved problem is now specifically:

- the full single-board WiFi bridge becomes unreliable once the motion-capable Step 9 path is reintroduced
- physical servo actuation through the staged single-board bridge remains unproven

## Solutions Attempted In Order

This section records what was tried and what each attempt proved.

### 1. Bridge Contract Correction

Applied to the Waveshare bridge source:

- bus path fixed to `GPIO18/GPIO19`
- bus baud fixed to `1000000`
- motion packet byte order corrected
- capability packet made truthful
- hardware switch later removed from the bridge path

Result:

- success for source alignment and compile
- did not resolve live WiFi runtime failure

### 2. Repo-Wide Python And Documentation Alignment

Updated:

- app hints and tooltips
- flash docs
- current sketch docs
- prep report
- compatibility notes

Result:

- success for consistency
- not a runtime fix by itself

### 3. Manual Flash Workflow

Used:

- `tools/flash_waveshare_bridge_manual_boot.ps1`

Result:

- success when the board was manually put into bootloader mode
- proved the board could accept new firmware

### 4. Automatic Control-Line Flash Attempts

Tried:

- normal upload path
- direct `esptool`
- DTR and RTS pulse sequences

Result:

- mixed
- sometimes succeeded
- often failed with wrong boot mode or no serial data
- proved automatic bootloader entry is unreliable on this hardware path

### 5. First Network Diagnostics Pass

Checked:

- WiFi association state
- `ipconfig`
- route state
- ARP
- ping
- UDP `hello`
- serial boot output

Result:

- success in proving the board booted
- failure remained in live network reachability and UDP reply path

### 6. Diagnostic Firmware With Network Logging

Added:

- more explicit network boot logs
- periodic `[NET]` loop diagnostics
- explicit `udp.begin` status logging

Result:

- success in narrowing the problem
- the firmware said SoftAP and UDP were up
- real traffic still remained unreliable

### 7. Explicit UDP Bind Revision

Changed:

- UDP listener bound explicitly to `192.168.4.1:9000`

Result:

- compiled successfully
- that revision was flashed and confirmed by serial log
- did not resolve the no-reply condition by itself

### 8. Minimal SoftAP Rollback Revision

Changed:

- removed the more aggressive AP reset and power handling
- moved SoftAP startup back toward the simpler known-good v2 pattern

Result:

- compiled successfully
- prepared as the next best firmware candidate
- at the time this report was written, it had not been fully validated as a solved runtime fix

## Where We Succeeded

- source contract cleanup
- app and doc cleanup
- repeated clean builds
- manual flashing
- direct esptool flashing in at least one successful cycle
- confirming the actual flashed revision by serial output
- proving that Step 7 A3 could answer direct `bus_ping` and motion traffic on `192.168.4.1:9000`
- proving that the app-side movement failure on the stable Step 7 A3 firmware was caused by the wrong saved connection mode
- narrowing the remaining runtime failure down to the motion-capable Step 9 single-board path

## Where We Failed

- reliable unattended bootloader entry
- stable single-board WiFi motion-and-accessory runtime in the targeted v3 topology
- verified physical pan and tilt movement through the motion-capable staged bridge
- hardware validation of the prepared `1000000` baud Step 9 state-machine build before testing was stopped

## Practical Conclusion

The current Waveshare single-board WiFi bridge should be considered not runtime-ready for the intended v3 motion topology.

That does not mean the board is useless.

It means the useful next topology is:

- USB servo-driver control for pan and tilt
- on-board ESP32 used only for accessory outputs
- one physical Waveshare board instead of the previous separate servo and ESP32 boards

Operationally, this means Smart Sentry should run in hybrid mode `2`:

- Debug Board USB for movement
- ESP32 WiFi for IO and accessories

## Approved Fallback Topology

Use this as the next practical direction.

### Motion Path

- PC to Waveshare on-board servo driver over USB
- pan and tilt remain on the board's servo-driver side
- do not route runtime pan and tilt through the ESP32 SoftAP bridge for now

### Accessory Path

- use the on-board ESP32 only for accessories
- keep the accessory wiring on the confirmed Pi-style header pins below

## Confirmed Accessory Header Map

| Physical Header Pin | ESP32 GPIO | Accessory Function | Use In Fallback |
|---|---|---|---|
| `7` | `GPIO4` | Buzzer output | Use |
| `13` | `GPIO27` | Trigger MOSFET control | Use |
| `22` | `GPIO25` | Accessory relay control | Use |
| `29` | `GPIO5` | Speaker reserved only | Leave unused for now |
| `37` | `GPIO26` | Spare relay control | Use |
| `40` | `GPIO21` | Former switch input | Leave free |

Reserved pins that should remain untouched:

| Physical Header Pin | ESP32 GPIO | Status |
|---|---|---|
| `8` | `GPIO14` | Reserved UART TX |
| `10` | `GPIO15` | Reserved UART RX |

Useful power and ground pins on the same header:

- `Pin 2` = 5V
- `Pin 4` = 5V
- `Pin 6` = GND
- `Pin 9` = GND
- `Pin 14` = GND
- `Pin 20` = GND
- `Pin 25` = GND
- `Pin 30` = GND
- `Pin 34` = GND
- `Pin 39` = GND

## Pi-Style Header Diagram For Accessories

This is a simplified 40-pin header view using physical header numbering.

`[USE]` means active fallback accessory signal.
`[RSV]` means reserved, do not repurpose.
`[GND]` and `5V` are available support pins.
`[FREE]` means leave unused for now.

```text
Waveshare 40-pin header
Top of header, pin 1 at upper-left

Left column                              Right column
------------------------------------     ------------------------------------
( 1) 3V3                                 5V                       ( 2)
( 3) unused                              5V                       ( 4)
( 5) unused                              GND                      ( 6)
( 7) GPIO4   -> BUZZER        [USE]      GPIO14 -> UART TX [RSV] ( 8)
( 9) GND                                 GPIO15 -> UART RX [RSV] (10)
(11) unused                              unused                   (12)
(13) GPIO27  -> TRIGGER MOSFET [USE]     GND                      (14)
(15) unused                              unused                   (16)
(17) 3V3                                 unused                   (18)
(19) unused                              GND                      (20)
(21) unused                              GPIO25 -> ACC RELAY [USE](22)
(23) unused                              unused                   (24)
(25) GND                                 unused                   (26)
(27) unused                              unused                   (28)
(29) GPIO5   -> SPEAKER RSV   [FREE]     GND                      (30)
(31) unused                              unused                   (32)
(33) unused                              GND                      (34)
(35) unused                              unused                   (36)
(37) GPIO26  -> SPARE RELAY   [USE]      unused                   (38)
(39) GND                                 GPIO21 -> LEAVE FREE     (40)
```

## Wiring Notes For The Fallback Plan

### Buzzer

- signal -> `Pin 7` / `GPIO4`
- return -> any GND pin, for example `Pin 6` or `Pin 9`

### Trigger MOSFET Control

- control signal -> `Pin 13` / `GPIO27`
- ground reference -> any GND pin
- do not connect a raw high-current load directly to the GPIO pin

### Accessory Relay Module

- relay module `IN` -> `Pin 22` / `GPIO25`
- relay module `GND` -> any GND pin
- relay module `VCC` -> proper relay supply

### Spare Relay Module

- relay module `IN` -> `Pin 37` / `GPIO26`
- relay module `GND` -> any GND pin
- relay module `VCC` -> proper relay supply

### Speaker Pin

- `Pin 29` / `GPIO5` remains reserved only
- do not make it part of the first fallback build

### Leave These Free

- `Pin 8` / `GPIO14`
- `Pin 10` / `GPIO15`
- `Pin 40` / `GPIO21`

## Recommended Next Work

1. Stop spending time on the Waveshare ESP32 SoftAP bridge as the primary motion path.
2. Use the known-working Waveshare USB servo-driver path for pan and tilt.
3. Reuse the on-board ESP32 only for accessory output control.
4. Build the new single-board fallback around that simpler division of labor.

## Handoff Summary

The Waveshare v3 attempt was not wasted.

It produced:

- a corrected bridge source base
- consistent repo docs
- confirmed header accessory map
- repeatable flash procedures
- a narrowed failure domain

The unresolved blocker is specifically the on-board ESP32 WiFi SoftAP and IP/UDP service path under the attempted single-board WiFi bridge design.

The board remains useful through the fallback topology documented above.
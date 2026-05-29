# ESP32 Current Firmware Sketches (Single Source of Truth)

This document defines the sketch that must be uploaded to the ESP32 for each runtime topology.

Desktop app version numbers and firmware sketch names are not required to advance together. If the firmware payload, transport contract, and operator-facing behavior are unchanged, keep using the existing sketch path and document it here instead of forcing a rename.

If firmware is changed, this file MUST be updated in the same change.

## Pinned Current App Firmware

For the current Smart Sentry desktop app, treat the ESP32 WiFi plus Debug Board USB path as the live firmware contract unless a newer app-side release protocol explicitly says otherwise.

- Current app topology: ESP32 WiFi + Debug Board USB
- Current app firmware: [arduino/SMART_SENTRY_ESP32_UDP_PIR/SMART_SENTRY_ESP32_UDP_PIR.ino](arduino/SMART_SENTRY_ESP32_UDP_PIR/SMART_SENTRY_ESP32_UDP_PIR.ino)
- Current app note: Waveshare single-board files are on hold and are not part of the current Smart Sentry app runtime.

## Current Required Sketches

1. USB Serial IO / Dual-Port IO (debug board still owns pan/tilt)
- Current ESP32 sketch: [arduino/DB3000_ESP32_IO_Telemetry_PIR/DB3000_ESP32_IO_Telemetry_PIR.ino](arduino/DB3000_ESP32_IO_Telemetry_PIR/DB3000_ESP32_IO_Telemetry_PIR.ino)
- New Nano replacement sketch: [arduino/SMART_SENTRY_V3_0_NANO_USB_IO_PIR/SMART_SENTRY_V3_0_NANO_USB_IO_PIR.ino](arduino/SMART_SENTRY_V3_0_NANO_USB_IO_PIR/SMART_SENTRY_V3_0_NANO_USB_IO_PIR.ino)
- Why: Both sketches satisfy the current serial IO contract for Smart Sentry's dual-USB mode, while the Nano variant replaces only the USB accessory board and keeps the existing desktop transport logic unchanged.
- Used with: Smart Sentry v2 connection modes where the IO board is on serial tokens and the Debug Board remains on its own USB link.

2. Full WiFi UDP Runtime (ESP32 receives motion + IO over UDP JSON)
- Current sketch: [arduino/SMART_SENTRY_ESP32_UDP_PIR/SMART_SENTRY_ESP32_UDP_PIR.ino](arduino/SMART_SENTRY_ESP32_UDP_PIR/SMART_SENTRY_ESP32_UDP_PIR.ino)
- Why: This is the current content-stable Smart Sentry WiFi baseline for the DB3000 IO board. It keeps PIR support, GPIO2 status/blink output, runtime trigger-servo tuning, optional PIR-event blink suppression, periodic pan/tilt/total current telemetry, keeps GPIO0 reserved strictly for ESP32 BOOT behavior, moves sweep execution to an app-triggered UDP action instead of a local GPIO0 input, accepts an explicit UDP rest-position contract (`rest` config plus `{"action":"rest"}`) while continuing to drive buzzer tones through the existing `{"action":"sound"}` path, and now enters a link-loss safe mode that turns off relays, stops fire output, and suppresses PIR event emission when the app goes inactive.
- Used with: Smart Sentry v2 mode 3 Full WiFi runtime and as the current baseline for the primary ESP32 WiFi board, including desktop app releases that do not change the firmware contract.

3. Yahboom Servo Driver UDP Runtime (ESP32 with integrated serial bus servo driver)
- Current sketch: [arduino/DB3000_ESP32_Yahboom_Servo/DB3000_ESP32_Yahboom_Servo.ino](arduino/DB3000_ESP32_Yahboom_Servo/DB3000_ESP32_Yahboom_Servo.ino)
- Why: Accepts JSON servo commands over UDP, controls Yahboom YB-SD35M servos via integrated driver.
- Used with: Smart Sentry v2 Dual ESP32 WiFi mode (secondary ESP32 for servos).

4. Waveshare Single-Board UDP Bus Bridge (On Hold / Not Current App)
- On-hold sketch: [arduino/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE.ino](arduino/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE.ino)
- Status: Failed single-board attempt kept only for bench history and possible future reintroduction.
- Do not use this for the current Smart Sentry app unless a future release protocol explicitly restores the Waveshare path.
- Used with: Archived Waveshare bench validation only, not the live desktop app.

## Legacy Firmware Note

- Older docs may still reference [arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino](arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino) or [arduino/DB3000_ESP32_UDP_PIR/DB3000_ESP32_UDP_PIR.ino](arduino/DB3000_ESP32_UDP_PIR/DB3000_ESP32_UDP_PIR.ino) for the WiFi runtime.
- For current Smart Sentry v2 WiFi work, treat those as historical predecessors unless a specific recovery or comparison task explicitly calls for them.
- Older DB3000 WiFi baseline sketches remain in the repo for comparison and rollback, but the path above is now the documented default for current work.

## Accessory PWM Support (MOSFET driver — **ENABLED and flashed as of 2026-04-16**)

Both `SMART_SENTRY_ESP32_UDP_PIR` and `SMART_SENTRY_V2_3_DB3000_ESP32_UDP_PIR_FLYSKY` sketches now contain an optional 8-bit LEDC PWM driver for LED, Laser, ACC, and Spare outputs. **PWM is currently ACTIVE** (`#define ACCESSORY_PWM_ENABLED 1`). MOSFET driver hardware is installed on all four output channels (GPIO32/33/25/26). The firmware was compiled (951 792 bytes, 72% flash) and flashed to COM28 on 2026-04-16 with hash verified and hard reset confirmed.

To revert to relay/ON-OFF mode: set `#define ACCESSORY_PWM_ENABLED  0`, recompile, and re-flash.

**PWM parameters** (adjustable at the top of the sketch):
- `ACCESSORY_PWM_FREQ_HZ  5000` — 5 kHz carrier, silent and MOSFET-safe
- `ACCESSORY_PWM_BITS     8`    — 0-255 range (8-bit resolution)

App PWM values: 0=off, 1=full-on compat (backward compatible), 2-255=literal 8-bit duty cycle.

**All other sketch logic** (motion, fire, safety, PIR, buzzer, telemetry, link-loss safe mode) is completely unaffected by this flag.

## Upload Commands

From repository root:

```powershell
# Full WiFi UDP sketch (primary ESP32)
.\tools\flash_esp32_udp.ps1 -Port COM28 -Sketch "arduino/SMART_SENTRY_ESP32_UDP_PIR/SMART_SENTRY_ESP32_UDP_PIR.ino"

# USB Serial IO + PIR sketch
.\tools\flash_esp32_udp.ps1 -Port COM5 -Sketch "arduino/DB3000_ESP32_IO_Telemetry_PIR/DB3000_ESP32_IO_Telemetry_PIR.ino"

# Arduino Nano USB Serial IO + PIR sketch
.\tools\arduino-cli\arduino-cli.exe compile --fqbn arduino:avr:nano "arduino\SMART_SENTRY_V3_0_NANO_USB_IO_PIR"
.\tools\arduino-cli\arduino-cli.exe upload -p COM5 --fqbn arduino:avr:nano "arduino\SMART_SENTRY_V3_0_NANO_USB_IO_PIR"

# Yahboom Servo Driver UDP sketch (secondary ESP32)
.\tools\flash_esp32_udp.ps1 -Port COM6 -Sketch "arduino/DB3000_ESP32_Yahboom_Servo/DB3000_ESP32_Yahboom_Servo.ino"

# Waveshare single-board v3 bridge sketch (on hold, not current app)
.\tools\flash_esp32_udp.ps1 -Port COM5 -Sketch "arduino/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE.ino"
```

## Mandatory Firmware-Doc Update Policy

Whenever an ESP32 sketch is modified, renamed, replaced, or its canonical mapping changes:

1. Update this file with the new canonical sketch path(s).
2. Update [ESP32_UDP_FLASH.md](ESP32_UDP_FLASH.md) flashing examples and default workflow notes.
3. Update [SMART_SENTRY_APP_CHANGE_IMPACT.md](SMART_SENTRY_APP_CHANGE_IMPACT.md) firmware references.
4. Add a short entry to [RECENT_UPDATES.json](RECENT_UPDATES.json) summarizing the firmware swap.
5. Update the active release compilation protocol.
6. In the commit message, include: "firmware-doc-sync".

A firmware contract change is incomplete until all six items above are done.

# ESP32 Current Firmware Sketches (Single Source of Truth)

This document defines the sketch that must be uploaded to the ESP32 for each runtime topology.

If firmware is changed, this file MUST be updated in the same change.

## Current Required Sketches

1. USB Serial IO / Dual-Port IO (ESP32 handles fire/safety/relays over USB serial)
- Current sketch: [arduino/DB3000_ESP32_IO_Telemetry_2026_w_PIR/DB3000_ESP32_IO_Telemetry_2026_w_PIR.ino](arduino/DB3000_ESP32_IO_Telemetry_2026_w_PIR/DB3000_ESP32_IO_Telemetry_2026_w_PIR.ino)
- Why: Includes IO telemetry plus PIR event support and current command-token compatibility.
- Used with: Smart Sentry v2 connection modes where ESP32 IO is on serial tokens.

2. Full WiFi UDP Runtime (ESP32 receives motion + IO over UDP JSON)
- Current sketch: [arduino/SMART_SENTRY_V2_0_ESP32_UDP_PIR/SMART_SENTRY_V2_0_ESP32_UDP_PIR.ino](arduino/SMART_SENTRY_V2_0_ESP32_UDP_PIR/SMART_SENTRY_V2_0_ESP32_UDP_PIR.ino)
- Why: This is the current flashed Smart Sentry WiFi baseline. It includes PIR support, GPIO2 status/blink output, runtime trigger-servo tuning, optional PIR-event blink suppression, and periodic pan/tilt/total current telemetry in state packets.
- Used with: Smart Sentry v2 mode 3 Full WiFi runtime and as the current baseline for the primary ESP32 WiFi board.

3. Yahboom Servo Driver UDP Runtime (ESP32 with integrated serial bus servo driver)
- Current sketch: [arduino/DB3000_ESP32_Yahboom_Servo/DB3000_ESP32_Yahboom_Servo.ino](arduino/DB3000_ESP32_Yahboom_Servo/DB3000_ESP32_Yahboom_Servo.ino)
- Why: Accepts JSON servo commands over UDP, controls Yahboom YB-SD35M servos via integrated driver.
- Used with: Smart Sentry v2 Dual ESP32 WiFi mode (secondary ESP32 for servos).

## Legacy Firmware Note

- Older docs may still reference [arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino](arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino) or [arduino/DB3000_ESP32_UDP_PIR/DB3000_ESP32_UDP_PIR.ino](arduino/DB3000_ESP32_UDP_PIR/DB3000_ESP32_UDP_PIR.ino) for the WiFi runtime.
- For current Smart Sentry v2 WiFi work, treat those as historical predecessors unless a specific recovery or comparison task explicitly calls for them.
- The current WiFi baseline still prints the legacy boot banner `DB3000_ESP32_UDP_PIR  v1`, so rely on the sketch path in this document rather than the banner text alone.

## Upload Commands

From repository root:

```powershell
# Full WiFi UDP sketch (primary ESP32)
.\tools\flash_esp32_udp.ps1 -Port COM5 -Sketch "arduino/SMART_SENTRY_V2_0_ESP32_UDP_PIR/SMART_SENTRY_V2_0_ESP32_UDP_PIR.ino"

# USB Serial IO + PIR sketch
.\tools\flash_esp32_udp.ps1 -Port COM5 -Sketch "arduino/DB3000_ESP32_IO_Telemetry_2026_w_PIR/DB3000_ESP32_IO_Telemetry_2026_w_PIR.ino"

# Yahboom Servo Driver UDP sketch (secondary ESP32)
.\tools\flash_esp32_udp.ps1 -Port COM6 -Sketch "arduino/DB3000_ESP32_Yahboom_Servo/DB3000_ESP32_Yahboom_Servo.ino"
```

## Mandatory Firmware-Doc Update Policy

Whenever an ESP32 sketch is modified, renamed, or replaced:

1. Update this file with the new canonical sketch path(s).
2. Update [ESP32_UDP_FLASH.md](ESP32_UDP_FLASH.md) flashing examples and default workflow notes.
3. Update [CHANGE_IMPACT_REFERENCE.md](CHANGE_IMPACT_REFERENCE.md) firmware references.
4. Add a short entry to [RECENT_UPDATES.json](RECENT_UPDATES.json) summarizing the firmware swap.
5. In the commit message, include: "firmware-doc-sync".

A firmware change is incomplete until all five items above are done.

# ESP32 Current Firmware Sketches (Single Source of Truth)

This document defines the sketch that must be uploaded to the ESP32 for each runtime topology.

If firmware is changed, this file MUST be updated in the same change.

## Current Required Sketches

1. USB Serial IO / Dual-Port IO (ESP32 handles fire/safety/relays over USB serial)
- Current sketch: [arduino/DB3000_ESP32_IO_Telemetry_2026_w_PIR/DB3000_ESP32_IO_Telemetry_2026_w_PIR.ino](arduino/DB3000_ESP32_IO_Telemetry_2026_w_PIR/DB3000_ESP32_IO_Telemetry_2026_w_PIR.ino)
- Why: Includes IO telemetry plus PIR event support and current command-token compatibility.
- Used with: Smart Sentry v2 connection modes where ESP32 IO is on serial tokens.

2. Full WiFi UDP Runtime (ESP32 receives motion + IO over UDP JSON)
- Current sketch: [arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino](arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino)
- Used with: Smart Sentry v2 Full WiFi mode and Dual ESP32 WiFi mode (primary ESP32).

3. Yahboom Servo Driver UDP Runtime (ESP32 with integrated serial bus servo driver)
- Current sketch: [arduino/DB3000_ESP32_Yahboom_Servo/DB3000_ESP32_Yahboom_Servo.ino](arduino/DB3000_ESP32_Yahboom_Servo/DB3000_ESP32_Yahboom_Servo.ino)
- Why: Accepts JSON servo commands over UDP, controls Yahboom YB-SD35M servos via integrated driver.
- Used with: Smart Sentry v2 Dual ESP32 WiFi mode (secondary ESP32 for servos).

## Upload Commands

From repository root:

```powershell
# Full WiFi UDP sketch (primary ESP32)
.\tools\flash_esp32_udp.ps1 -Port COM5

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

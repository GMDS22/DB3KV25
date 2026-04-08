# Smart Sentry V3 Waveshare Prep Report

Date: 2026-04-05

## Goal

Prepare a flash-ready and bench-ready Smart Sentry v3 Waveshare firmware build,
sync all dependent repo files to the same hardware contract, and document any
remaining gaps before tomorrow's hardware test session.

## Firmware Work Completed

- Updated the canonical Waveshare bridge sketch:
  - [arduino/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE.ino](arduino/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE.ino)
- Locked the bus UART to the vendor-confirmed settings:
  - RX `GPIO18`
  - TX `GPIO19`
  - baud `1000000`
- Corrected the bus motion packet byte order to little-endian for both position
  and move time:
  - `POS_L POS_H TIME_L TIME_H`
- Removed the dedicated hardware-switch dependency from the current bridge:
  - no trigger interlock input is required
  - `switch_supported=false`
  - trigger output now respects software safety and fault state only
- Corrected capability reporting so the app sees only confirmed hardware:
  - `led_relay_assigned=false`
  - `laser_relay_assigned=false`
  - `trigger_servo_assigned=false`
  - confirmed pins exposed for trigger MOSFET, accessory relay, spare relay,
    buzzer, and reserved UART pins

## Additional Code Work Completed

- Synced the companion pin-test sketch to the same confirmed bus settings:
  - [arduino/SMART_SENTRY_V3_0_WAVESHARE_FULL_PIN_TEST/SMART_SENTRY_V3_0_WAVESHARE_FULL_PIN_TEST.ino](arduino/SMART_SENTRY_V3_0_WAVESHARE_FULL_PIN_TEST/SMART_SENTRY_V3_0_WAVESHARE_FULL_PIN_TEST.ino)
- That sketch now also sends little-endian motion payload bytes so it remains a
  valid diagnostic companion for the bridge.

## Files Audited And Updated

- [ESP32_CURRENT_SKETCH.md](ESP32_CURRENT_SKETCH.md)
- [ESP32_UDP_FLASH.md](ESP32_UDP_FLASH.md)
- [SMART_SENTRY_V3_0_WAVESHARE_NANO_UPGRADE_SPEC.md](SMART_SENTRY_V3_0_WAVESHARE_NANO_UPGRADE_SPEC.md)
- [SMART_SENTRY_APP_CHANGE_IMPACT.md](SMART_SENTRY_APP_CHANGE_IMPACT.md)
- [RECENT_UPDATES.json](RECENT_UPDATES.json)

## Files Audited But Not Requiring Code Changes

- [app/sentry_v2/sentry_v2_comm.py](app/sentry_v2/sentry_v2_comm.py)
  - Already parses bridge capability flags and tolerates absent switch metadata.
- [app/sentry_v2/sentry_v2_tab.py](app/sentry_v2/sentry_v2_tab.py)
  - Updated to fall back cleanly to software-safety-only status when the bridge
    reports no dedicated hardware switch.
- [tools/waveshare_udp_debugger.py](tools/waveshare_udp_debugger.py)
  - No protocol change needed; it already reads the bridge reply shape we kept.

## Remaining Gaps Or Risks

- Flash automation remains uncertain.
  - The board previously resisted bootloader entry without manual BOOT/RESET
    timing.
  - A final unattended flash attempt can still be tried tomorrow, but success is
    not guaranteed until the hardware confirms auto-reset behavior.
- Servo protocol is now better aligned with vendor references, but live Yahboom
  compatibility still depends on bench verification.
  - The most important tests are `hello`, `bus_ping`, motion, and software-
    safety-gated trigger behavior.

## Tomorrow's Recommended Validation Order

1. Build or flash the bridge sketch on `COM30`.
2. Confirm boot log shows bus UART on `GPIO18/GPIO19` at `1000000` baud.
3. Join `WAVESHARE-ESP32` and verify `hello` and `cap` replies.
4. Verify `cap` reports `switch_supported=false`.
5. Run `bus_ping`.
6. Run pan/tilt motion tests.
7. Validate trigger follows `safety=0` and is blocked when software safety is locked.
8. Validate buzzer, accessory relay, and spare relay.

## Summary

The repo is now internally consistent around one Waveshare v3 bridge contract:

- UART `GPIO18/GPIO19`
- bus baud `1000000`
- little-endian servo write payloads
- no dedicated hardware switch requirement in the bridge path
- only confirmed outputs exposed as supported

The remaining work is hardware validation and, if possible, a successful flash
without manual boot intervention.
# PIR Sensor Integration - At a Glance

Date: 2026-05-13
Status: Current contract audit for the live Smart Sentry PIR workflow
Audience: Developers, validators, integrators

## What Matches Right Now

Current active app firmware path:

`arduino/SMART_SENTRY_V3_0_NANO_USB_IO_PIR/SMART_SENTRY_V3_0_NANO_USB_IO_PIR.ino`

Current WiFi reference path:

`arduino/SMART_SENTRY_ESP32_UDP_PIR/SMART_SENTRY_ESP32_UDP_PIR.ino`

Current desktop runtime path:

- `app/sentry_v2/sentry_v2_comm.py`
- `app/sentry_v2/sentry_v2_engine.py`
- `app/sentry_v2/sentry_v2_pir_manager.py`
- `app/sentry_v2/sentry_v2_tab.py`

The firmware and desktop code currently match on these points:

- The active dual-USB app contract receives PIR events as `PIR_EVENT sensor_id=... timestamp=...` on the Nano serial IO path.
- The WiFi reference path can still emit `pir_event` over UDP for WiFi-specific builds, but it is not the primary current app path.
- PIR enable remains app-owned and is persisted through the canonical Smart Sentry settings file.
- Serial compatibility for `P0` and `P1` remains present in USB modes.
- PIR event LED blink is carried by the runtime config payload under `pir.event_blink`.
- The app receives PIR events in `sentry_v2_comm.py`, forwards them into the engine, and the engine converts them into cue, confirm, hunt, and return-home behavior.

## Current Behavior Contract

### PIR Motion Flow

1. A PIR sensor fires on the ESP32.
2. The firmware debounces the hit and sends the sensor id back to the app.
3. The desktop comm layer dispatches the PIR event into the sentry engine.
4. The engine slews to that sensor's configured cue angle.
5. The engine holds briefly at cue center.
6. If vision confirms a target, normal engagement starts.
7. If vision does not confirm and PIR scan is enabled, the engine runs a local hunt around that cue and then widens the search.
8. If the PIR hunt finishes with no target, the engine explicitly returns to the configured guard/home position.

### After Target Loss vs PIR

`target_loss_timeout` and `After Target Loss` are not in conflict in the current code.

- `target_loss_timeout` is the outer time budget for trying to recover a lost tracked target.
- Adaptive `After Target Loss` only decides which recovery protocol runs inside that time budget.
- While a PIR cue or PIR scan is active, normal target-loss recovery is suppressed so both systems do not fight each other.
- PIR cue hold is clamped against `confirmation_timeout`, so the center hold cannot outlive the confirmation window.
- The shared `Search style` and `Hunt rounds` controls are written into both engagement loss-recovery settings and PIR no-detect search settings.

## Firmware Pins

The current live firmware uses these PIR input pins:

| GPIO | Sensor | Firmware Role |
|------|--------|---------------|
| 35 | Sensor 0 | PIR input |
| 34 | Sensor 1 | PIR input |
| 39 | Sensor 2 | PIR input |

Important distinction:

- The firmware reports `sensor_id` values.
- The desktop app owns the cue pan and cue tilt used for that sensor id.
- Because of that, the physical mounting layout can differ from the default firmware comments without breaking the protocol.

## Cue Angle Ownership

There are two different truths to keep separate:

- Firmware transport contract: sensor ids `0`, `1`, and `2`.
- Desktop aiming contract: cue angles stored in `app/config/smart_sentry_settings.json`.

Default dataclass cue layout in code:

- Sensor 0 -> `45 deg`
- Sensor 1 -> `135 deg`
- Sensor 2 -> `225 deg`

Current saved operator profile in `app/config/smart_sentry_settings.json`:

- Sensor 0 -> `45.0 deg`, tilt `35.0 deg`
- Sensor 1 -> `135.0 deg`, tilt `35.0 deg`
- Sensor 2 -> `225.0 deg`, tilt `35.0 deg`

That saved profile is not a firmware mismatch. It is an operator-level cue map stored in the desktop config.

## Current Control Contract

### Active Dual-USB Serial Path

The current live app contract uses the Nano serial IO path.

Serial control compatibility remains:

```text
P0
P1
```

And PIR events appear as:

```text
PIR_EVENT sensor_id=0 timestamp=123456789
```

### WiFi / UDP Reference Path

In the WiFi reference path, the app does not depend on old single-letter PIR commands. It sends JSON payloads.

Enable PIR:

```json
{"pir_enabled":1}
```

Disable PIR:

```json
{"pir_enabled":0}
```

Update PIR event blink runtime config:

```json
{
  "action": "config",
  "pir": {
    "event_blink": 1
  }
}
```

Firmware PIR event back to app:

```json
{
  "v": 1,
  "t": "pir_event",
  "p": {
    "sensor_id": 0,
    "timestamp_ms": 123456789
  }
}
```

## Live Runtime Settings Seen In The Current Config

The current saved profile shows these relevant values:

- `pir_enabled = true`
- `pir_event_blink_enabled = false`
- per-sensor `enabled = false` until the operator activates the individual sensor rows
- `scan_on_no_detect = true`
- `cue_hold_time_s = 0.18`
- `confirmation_timeout = 1.2`
- `cross_sensor_lockout_ms = 120`
- `target_loss_timeout = 1.4`
- `adaptive_loss_recovery_enabled = true`
- `loss_search_style = hunting`
- `loss_search_rounds = 1`
- `pir_guard.search_style = hunting`
- `pir_guard.search_rounds = 1`

This is the expected aligned state for the shared loss/PIR hunt settings.

## Operator Checklist

1. Flash `arduino/SMART_SENTRY_V3_0_NANO_USB_IO_PIR/SMART_SENTRY_V3_0_NANO_USB_IO_PIR.ino` when running the current active dual-USB app path.
2. Keep PIR enable controlled from the Smart Sentry Guard tab in normal operation.
3. Treat `P0` and `P1` as serial compatibility controls for the dual-USB path, not a separate firmware family.
4. Use `SMART_SENTRY_ESP32_UDP_PIR.ino` only when you are intentionally validating the WiFi reference path.
5. If PIR cues look wrong, inspect the saved cue angles in `app/config/smart_sentry_settings.json` before changing firmware.
6. If after-loss behavior looks wrong, inspect `target_loss_timeout`, adaptive recovery, and shared hunt settings together because they are intentionally coupled.

## Source Of Truth

Use these files as the authoritative references:

- `arduino/SMART_SENTRY_V3_0_NANO_USB_IO_PIR/SMART_SENTRY_V3_0_NANO_USB_IO_PIR.ino`
- `ARDUINO_NANO_USB_IO_FIRMWARE_GUIDE.md`
- `arduino/SMART_SENTRY_ESP32_UDP_PIR/SMART_SENTRY_ESP32_UDP_PIR.ino` (WiFi reference path)
- `app/sentry_v2/sentry_v2_comm.py`
- `app/sentry_v2/sentry_v2_engine.py`
- `app/sentry_v2/sentry_v2_pir_manager.py`
- `app/sentry_v2/sentry_v2_tab.py`
- `app/config/smart_sentry_settings.json`
- `SMART_SENTRY_AUTOTRACKING_BEHAVIOR_BLUEPRINT.md`

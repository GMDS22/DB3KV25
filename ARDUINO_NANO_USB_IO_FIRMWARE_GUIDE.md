# Arduino Nano USB IO Firmware Guide

## Purpose

This guide documents the Smart Sentry hardware path where the ESP32 USB IO board
is replaced by an Arduino Nano while the servo debug board remains connected to
the PC over its own USB cable.

The desktop app transport stays unchanged. The new Nano sketch simply speaks the
serial contract that Smart Sentry already uses for its dual-USB mode, including
runtime trigger settings for both water/MOSFET and projectile/servo paths.

## How The App Works In This Topology

- `run.py` is the desktop entrypoint.
- `app/sentry_v2/sentry_v2_tab.py` owns the UI, camera, detector, and engine.
- `app/sentry_v2/sentry_v2_comm.py` is the transport authority.
- Use the `ESP32 USB + Debug Board USB` connection mode.
- In that mode, the `ESP32 Port` field may point to the Nano COM port because the
  app is sending plain serial IO commands, not ESP32-specific USB features.

Topology summary:

- PC USB -> Arduino Nano: fire, safety, water/MOSFET config, trigger-servo config, LED PWM, laser,
  PIR telemetry, and buzzer tones.
- PC USB -> Servo Debug Board: Yahboom pan/tilt bus servo movement.

## New Firmware

- Sketch: `arduino/SMART_SENTRY_V3_0_NANO_USB_IO_PIR/SMART_SENTRY_V3_0_NANO_USB_IO_PIR.ino`
- Board target: `arduino:avr:nano`
- Tool: `tools/arduino-cli/arduino-cli.exe`

## Serial Contract Implemented By The Nano Sketch

Packed or single-token lines accepted by the sketch:

- `F{0|1}`
- `L{0..255}`
- `R{0|1}`
- `G{0|1}`
- `A{0|1}`
- `S{0|1}`
- `M{0|1}`
- `J{10..2000}`
- `K{1..20}`
- `N{10..2000}`
- `U{0..180}`
- `V{0..180}`
- `H{10..5000}`
- `B{0|1}`
- `P{0|1}`

Sound line accepted by the sketch:

- `SOUND:<freq_hz>:<duration_ms>`
- `SOUND:<freq_hz>:<duration_ms>:<volume_pct>`

Telemetry lines emitted by the sketch:

- `ACK ...`
- `STAT ...`
- `PIR_EVENT sensor_id=<id> timestamp=<millis>`

LED PWM compatibility mapping:

- `0` = off
- `1` = full on compatibility value
- `2..255` = literal PWM duty

Water / MOSFET trigger runtime mapping:

- `J` = MOSFET pulse ON time in milliseconds
- `K` = number of ON pulses to fire for one water-mode fire request
- `N` = OFF gap between MOSFET pulses in milliseconds

In water mode, one fire request now runs the configured MOSFET pulse train on `D8`.
This is separate from the app's engagement burst count, which still controls how many
fire requests are issued per target engagement.

## Nano Pin Map

- `D4` -> passive buzzer tone output
- `D5` -> LED PWM output
- `D6` -> laser output
- `D7` -> accessory relay output
- `D8` -> trigger MOSFET output
- `D9` -> trigger servo PWM via `Servo` library
- `A3` -> spare relay output
- `A0` -> PIR sensor 0 input
- `A1` -> PIR sensor 1 input
- `A2` -> PIR sensor 2 input
- `D13 / LED_BUILTIN` -> status blink output

PIR note:

- A classic Nano does not provide internal pulldown inputs.
- Use PIR modules that idle LOW, or add external pulldown resistors.

## Compile And Upload

From `f:/SMART SENTRY_v2a/SMART SENTRY`:

```powershell
.\tools\arduino-cli\arduino-cli.exe compile --fqbn arduino:avr:nano "arduino\SMART_SENTRY_V3_0_NANO_USB_IO_PIR"
.\tools\arduino-cli\arduino-cli.exe upload -p COM5 --fqbn arduino:avr:nano "arduino\SMART_SENTRY_V3_0_NANO_USB_IO_PIR"
```

Replace `COM5` with the actual Nano port.

## Run The App

1. Connect the Arduino Nano to the PC over USB.
2. Connect the servo debug board to the PC over USB.
3. Launch Smart Sentry from `f:/SMART SENTRY_v2a/SMART SENTRY`:

```powershell
& "f:/SMART SENTRY_v2a/.venv/Scripts/python.exe" run.py
```

4. In the Connection tab select `Arduino Nano USB + Debug Board USB`.
5. Set `ESP32 Port` to the Nano COM port.
6. Set `Debug Board Port` to the servo debug board COM port.
7. Leave both baud rates at `115200`.
8. Connect and verify serial logs begin appearing.

## Validation Checklist

- Nano prints `[BOOT] SMART_SENTRY_V3_0_NANO_USB_IO_PIR ready`
- Safety toggle changes `ACK S=` state
- Fire command runs the configured MOSFET pulse train or trigger-servo pulse depending on `M`
- LED button and auto-lighting send `L0..255` and change brightness on `D5`
- Sound cues produce buzzer output on `D4`
- PIR hits emit `PIR_EVENT` lines and drive the existing app PIR workflow
- Trigger runtime config updates respond to `J`, `K`, `N`, `U`, `V`, `H`, and `B`

## Current App-Side Notes

- The current recurring mode-1 serial sender in `app/sentry_v2/sentry_v2_comm.py`
  actively transmits `S/M/F/L/R/G/A` and uses separate serial writes for `P`,
  `SOUND`, and `J/K/N/U/V/H/B`.
- The trigger settings panel now swaps by mode: Water/MOSFET shows pulse-train
  settings, while Projectile shows trigger-servo travel settings.
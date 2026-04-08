# Smart Sentry v3.0 Unassigned Output Tracker

This file tracks the remaining hardware-side outputs that are still intentionally
unassigned after the Waveshare header map was narrowed to only confirmed points.

## Current Confirmed Header-Backed Outputs

- Header pin `7` / `GPIO4`: buzzer
- Header pin `13` / `GPIO27`: trigger MOSFET
- Header pin `22` / `GPIO25`: accessory relay
- Header pin `37` / `GPIO26`: spare relay
- Header pin `40` / `GPIO21`: switch input
- Header pin `29` / `GPIO5`: speaker reserved only
- Header pin `8` / `GPIO14`: UART TX reserved
- Header pin `10` / `GPIO15`: UART RX reserved

## Still Unassigned

These functions are still part of the broader v3 upgrade direction, but they do
not yet have a trusted header-accessible pin assignment.

- LED relay output
- Laser relay output
- Trigger servo PWM output
- Buzzer volume ADC input
- Speaker volume ADC input

## Why They Are Still Unassigned

The current pinout evidence is strong enough to trust the confirmed header map
above, but not strong enough to claim additional ESP32 pins like `GPIO32`,
`GPIO33`, `GPIO34`, or `GPIO35` as safe accessory points from the exposed header.

That means the correct next move is validation, not guessing.

## Required Validation For Each Unassigned Function

### LED relay output

Need:
- a confirmed header pin or alternate exposed pad/header path
- proof that the pin is not shared with boot, UART, or bus-servo transport
- relay-drive compatibility check

### Laser relay output

Need:
- a confirmed header pin or alternate exposed pad/header path
- proof that the pin is not shared with boot, UART, or bus-servo transport
- relay-drive compatibility check

### Trigger servo PWM

Need:
- a confirmed PWM-capable, header-accessible output
- proof it does not collide with UART TX/RX
- pulse stability check under active WiFi and servo-bus traffic

### Buzzer volume ADC

Need:
- a confirmed ADC-capable, header-accessible input
- proof that the analog input stays stable in the intended wiring layout
- UI/firmware policy for whether the knob acts as hard max-volume or scaling input

### Speaker volume ADC

Need:
- a confirmed ADC-capable, header-accessible input
- proof that the analog input stays stable in the intended wiring layout
- amplifier/speaker path decision before knob integration

## Recommended Resolution Order

1. Trigger servo PWM
2. LED relay output
3. Laser relay output
4. Buzzer volume ADC
5. Speaker volume ADC

Reason:
- trigger PWM affects core fire-path hardware choices
- LED and laser outputs are useful but not safety-critical
- the analog knob inputs depend on later UX and speaker decisions

## Firmware Status

The bridge capability packet now explicitly advertises these fields as unassigned:

- `led_relay_assigned=false`
- `laser_relay_assigned=false`
- `trigger_servo_assigned=false`
- `buzzer_volume_assigned=false`
- `speaker_volume_assigned=false`
- `unassigned_outputs=[...]`

That keeps the unresolved hardware state visible to both bench tools and the app.

## Exit Condition

This tracker is complete when every currently unassigned function has:

1. a physically validated wiring point
2. a firmware pin assignment
3. a bench verification step
4. an app-facing capability update if needed

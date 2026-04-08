# Smart Sentry v3.0 Waveshare Header Wiring Guide

This is the plain-language wiring reference for the Waveshare Bus Servo Driver HAT
40-pin header using the same physical pin numbering shown in the Waveshare pinout
image.

Use this document when you want the exact answer to:

- which header pin number to use
- which GPIO that header pin maps to
- what that pin is for in Smart Sentry v3
- where the other wire goes

## Important Rule

This guide uses the Waveshare image's Raspberry Pi style physical header numbering.

That means:

- `Pin 7` means physical header pin 7 on the image
- `GPIO4` is the signal on that same physical pin

Do not confuse:

- physical header pin number
- ESP32 GPIO number

They are not the same thing.

## Confirmed Smart Sentry Header Assignments

| Waveshare Header Pin | GPIO | Smart Sentry Use | Status |
|---|---|---|---|
| `7` | `GPIO4` | Buzzer output | Use now |
| `8` | `GPIO14` | UART TX reserved | Keep free |
| `10` | `GPIO15` | UART RX reserved | Keep free |
| `13` | `GPIO27` | Trigger MOSFET output | Use now |
| `22` | `GPIO25` | Accessory relay control output | Use now |
| `29` | `GPIO5` | Speaker reserved | Do not wire active hardware yet |
| `37` | `GPIO26` | Spare relay control output | Use now |
| `40` | `GPIO21` | Switch input | Use now |

## Power And Ground Pins On The Same Header

Use these exactly as shown on the Waveshare image.

### 5V Pins

- `Pin 2`
- `Pin 4`

### Ground Pins

- `Pin 6`
- `Pin 9`
- `Pin 14`
- `Pin 20`
- `Pin 25`
- `Pin 30`
- `Pin 34`
- `Pin 39`

If a device needs:

- a signal wire and a ground wire: use the assigned signal pin plus any GND pin above
- signal, power, and ground: use the assigned signal pin, one GND pin, and one suitable power pin only if the device is safe to power that way

## Exact Wiring By Hardware

## 1. Buzzer

### Assigned Pin

- Signal pin: `Header pin 7`
- GPIO: `GPIO4`

### Simple Two-Wire Buzzer Wiring

If you are using a small buzzer with two terminals:

- buzzer positive or signal lead -> `Pin 7`
- buzzer negative lead -> any GND pin such as `Pin 6` or `Pin 9`

### If Your Buzzer Module Has `SIG`, `VCC`, `GND`

- `SIG` -> `Pin 7`
- `GND` -> any GND pin
- `VCC` -> only if the module actually requires a separate supply

### Important Buzzer Note

Do not assume every buzzer can be driven directly from the GPIO line.

Safe rule:

- small passive or logic-level buzzer: signal to `Pin 7`, return to GND
- larger or louder buzzer module: use a transistor or driver stage if the module draws meaningful current

If you are not sure, do not connect a high-current buzzer directly to the header GPIO.

## 2. Hardware Switch

### Assigned Pin

- Signal pin: `Header pin 40`
- GPIO: `GPIO21`

### Exact Wiring

Use a simple SPST switch.

- one switch terminal -> `Pin 40`
- other switch terminal -> any GND pin such as `Pin 39`

That is the whole switch circuit.

### Why The Second Wire Goes To Ground

The firmware uses the ESP32 internal pull-up on `GPIO21`.

That means:

- switch open = pin stays pulled high internally
- switch closed to GND = pin reads low

### Actual Smart Sentry Behavior

- switch open -> `switch_in=0` -> hardware arm disabled -> trigger output blocked
- switch closed to GND -> `switch_in=1` -> hardware arm enabled

Important:

- this switch gates the trigger path only
- it does not block motion testing
- it does not block buzzer testing
- it does not block accessory or spare relay testing

## 3. Trigger Output

### Assigned Pin

- Signal pin: `Header pin 13`
- GPIO: `GPIO27`

### What This Pin Is

This is the Smart Sentry v3 trigger control output.

Treat this as a control signal, not as a place to power a high-current load directly.

### If Your Trigger Hardware Uses `SIG` And `GND`

- trigger control input or `SIG` -> `Pin 13`
- trigger ground or reference ground -> any GND pin

### If Your Trigger Hardware Uses `SIG`, `VCC`, `GND`

- `SIG` -> `Pin 13`
- `GND` -> any GND pin
- `VCC` -> the proper supply for that trigger module

### What Not To Do

Do not connect the real load directly to `Pin 13`.

Use `Pin 13` only as the logic or gate control path into the actual trigger driver stage.

## 4. Accessory Relay Control

### Assigned Pin

- Signal pin: `Header pin 22`
- GPIO: `GPIO25`

### Typical Relay Module Wiring

If you are using an external relay module with `IN`, `VCC`, `GND`:

- relay module `IN` -> `Pin 22`
- relay module `GND` -> any GND pin
- relay module `VCC` -> appropriate relay-module power input

### Where The Other Wires Go

There are two separate sides here:

1. The relay control side:
- `IN`, `VCC`, `GND`

2. The relay contact side:
- `COM`, `NO`, `NC`

Your actual accessory load does not connect to the GPIO pin.
It connects to the relay contacts.

### Safe Rule

Do not wire the accessory load directly to `Pin 22`.

`Pin 22` is the control signal for the relay module, not the load power path.

## 5. Spare Relay Control

### Assigned Pin

- Signal pin: `Header pin 37`
- GPIO: `GPIO26`

### Typical Wiring

Same pattern as the accessory relay:

- spare relay module `IN` -> `Pin 37`
- spare relay module `GND` -> any GND pin
- spare relay module `VCC` -> appropriate relay-module power input

Again:

- the load goes on the relay contacts
- the GPIO pin only drives the relay control input

## 6. Speaker Reserved Pin

### Assigned Pin

- Signal pin: `Header pin 29`
- GPIO: `GPIO5`

### Current Status

Reserved only.

Do not wire active speaker hardware here yet.

This is intentionally held for future speaker work and is not part of the current
validated bench wiring.

## Pins You Must Leave Alone

These are reserved in the current Smart Sentry v3 Waveshare plan.

### `Pin 8 / GPIO14`

- reserved for UART TX use
- do not reuse for buzzer, switch, relay, or random accessories

### `Pin 10 / GPIO15`

- reserved for UART RX use
- do not reuse for buzzer, switch, relay, or random accessories

## Not Assigned Yet

These are not confirmed on the Waveshare header map and should not be wired from
this document.

- LED relay
- laser relay
- trigger-servo PWM output
- buzzer volume knob input
- speaker volume knob input
- GPIO32, GPIO33, GPIO34, GPIO35 header assumptions

## Quick Wiring Examples

## Example A: Two-Wire Buzzer

- buzzer `+` or `SIG` -> `Pin 7`
- buzzer `-` -> `Pin 6`

## Example B: Simple Arm Switch

- switch terminal 1 -> `Pin 40`
- switch terminal 2 -> `Pin 39`

## Example C: 3-Pin Relay Module For Accessory

- relay `IN` -> `Pin 22`
- relay `GND` -> `Pin 25` or any other GND pin
- relay `VCC` -> `Pin 2` or `Pin 4` only if that module's voltage and current are safe for the board power plan

Accessory load wiring then goes on the relay module's contact terminals, not on
the Waveshare GPIO header pin.

## Example D: 3-Pin Relay Module For Spare Output

- relay `IN` -> `Pin 37`
- relay `GND` -> `Pin 39` or any other GND pin
- relay `VCC` -> module-appropriate supply

## Quick Summary

If you only need the shortest answer:

- buzzer: `Pin 7` to buzzer signal, other buzzer wire to GND
- switch: `Pin 40` to one side of switch, other side of switch to GND
- trigger control: `Pin 13` to trigger control input, trigger ground to GND
- accessory relay control: `Pin 22` to relay `IN`, relay `GND` to GND, relay `VCC` to proper supply
- spare relay control: `Pin 37` to relay `IN`, relay `GND` to GND, relay `VCC` to proper supply
- speaker: `Pin 29` reserved, do not use yet
- UART pins: `Pin 8` and `Pin 10`, leave them alone

## Recommended Ground Pins For Convenience

Near the lower end of the header, these are convenient:

- `Pin 39` for the switch return
- `Pin 25` or `Pin 30` for nearby accessory ground

Near the top of the header, these are convenient:

- `Pin 6` or `Pin 9` for buzzer ground

## Final Safety Note

Do not power unknown loads directly from the GPIO pins.

GPIO pins are for:

- logic-level signal
- light control input
- relay-module input
- transistor or MOSFET driver input

They are not for directly feeding motors, solenoids, large buzzers, lamps, or
other heavier loads.
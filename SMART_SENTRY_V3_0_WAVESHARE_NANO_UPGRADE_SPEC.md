# Smart Sentry v3.0 Waveshare + Nano Upgrade Spec

## Purpose

This document locks the initial Smart Sentry v3.0 hardware and protocol contract
before deeper firmware or app integration begins.

The preserved Smart Sentry v2 baseline is:

- Branch: `backup/sentry2-v2-working-2026-04-04`
- Tag: `sentry2-v2-working-2026-04-04`
- Commit: `da430d9`

## Target Topology

- PC to Waveshare ESP32 over WiFi UDP only
- Waveshare ESP32 to Yahboom serial bus line as the only bus master
- Waveshare ESP32 directly owns the local accessory outputs
- Arduino Nano is optional fallback hardware only and is not required for the
  primary v3.0 topology
- Debug Board is removed from the runtime topology for v3.0

## Servo And Device ID Allocation

- ID 1: Pan bus servo
- ID 2: Tilt bus servo
- ID 3: Reserved for future trigger bus servo upgrade
- ID 4: Reserved only if an external accessory listener is ever restored

## Core Design Rules

- The Waveshare ESP32 owns all wireless motion and accessory command reception.
- The Waveshare ESP32 directly drives trigger, relays, switch input, and buzzer.
- The Nano is no longer part of the primary hardware path.
- The PC application should remain unchanged until the new firmware path is
  bench-validated.

## Yahboom Packet Assumptions

These assumptions are based on the Yahboom vendor examples already present in
the repository and must be re-validated against the exact live hardware.

- Motion write frame: `FF FF ID LEN 03 2A POS_L POS_H TIME_L TIME_H CHK`
- Register read frame: `FF FF ID 04 02 ADDR SIZE CHK`
- Broadcast ID: `0xFE`
- Position register: `0x2A`
- Checksum mode: inverse-sum is the working primary assumption

## Open Hardware Validation Gates

These are mandatory before final firmware wiring is considered stable.

1. Bench-validate the vendor-aligned 1000000 baud bus path against the actual live Yahboom setup.
2. Confirm the Waveshare HAT pin path from the ESP32 UART to the servo bus data line.
3. Confirm the exact Waveshare header net mapping for any future outputs that are
  not already covered by the Pi-style header reference image.
4. Confirm isolated power paths are correct for relays, buzzer, and any future
  speaker hardware.

## Confirmed Header-Based Wiring Map

These assignments are now anchored to the Pi-style 40-pin header reference image.
For the confirmed accessory points, the physical header pin and the GPIO number
align as follows.

- Header pin `7` / `GPIO4`: Buzzer output
- Header pin `13` / `GPIO27`: Trigger MOSFET output
- Header pin `22` / `GPIO25`: Accessory relay output
- Header pin `29` / `GPIO5`: Speaker output reserved, not implemented yet
- Header pin `37` / `GPIO26`: Spare relay output
- Header pin `40` / `GPIO21`: Switch input

Reserved system pins from the same header image:

- Header pin `8` / `GPIO14`: UART TX only, do not repurpose
- Header pin `10` / `GPIO15`: UART RX only, do not repurpose

## Unassigned Future Outputs

These functions remain part of the broader upgrade direction, but they no longer
have a claimed GPIO until a header-accessible path is confirmed.

- Trigger servo PWM output: unassigned
- LED relay output: unassigned
- Laser relay output: unassigned
- Buzzer volume analog input: unassigned
- Speaker volume analog input: unassigned

## Trigger Servo Direction

The trigger-servo PWM path should remain unassigned on the Waveshare header for
now.

Current decision:

- Do not guess a new on-board PWM pin from incomplete header evidence.
- Keep the confirmed trigger MOSFET path on header pin `13` / `GPIO27` as the
  primary fire hardware for v3.
- If a true trigger servo is restored later, prefer one of these paths:
  - Yahboom bus-servo trigger on reserved ID `3`
  - external PWM generator or small co-controller with a validated signal path

This avoids silently colliding with UART, boot, or undocumented board nets.

## Future RC Receiver Path

FlySky-style RC receiver support should be treated as a serial control input,
not as a bank of individual PWM wires.

See also:

- `SMART_SENTRY_V3_0_FLYSKY_FSIA6_INTEGRATION.md`

Working direction:

- With the exact FS-iA6 receiver in hand, the electrical decode path is still a
  validation item and should not be hard-claimed yet
- Header pin `10` / `GPIO15`: preferred future RC RX candidate if a safe summed
  or serial signal path is confirmed
- Header pin `8` / `GPIO14`: reserve only if a return UART or future telemetry
  path is needed
- Keep the WiFi/app control path as the primary supervisory layer unless RC
  override is explicitly enabled in firmware

If the available FlySky receiver exposes only separate PWM channels, that is not
the preferred direct integration path for this board because the pin budget is
already too constrained.

Current control-source contract added for FS-iA6 planning:

- FlySky CH6: APP vs RC mode select
- Existing header pin `40` / `GPIO21` switch: stays dedicated to hardware arm
  interlock
- Current assigned RC-side functions:
  - CH1 pan
  - CH2 tilt
  - CH3 fire request
  - CH4 accessory relay
  - CH5 spare relay
  - CH6 control-source select

LED and laser remain excluded from that map until their board outputs are
physically assigned.

## Sound Status For Phase 1

The buzzer is now part of the v3 upgrade scope.

- The current app-side sound engine design remains valid conceptually.
- Local buzzer playback is planned on header pin `7` / `GPIO4`.
- The three `D/V/G` bus-servo ports are not to be treated as buzzer outputs.
- Speaker playback and both volume knob inputs are only reserved for future use.

## Initial Bench Network Defaults

The single-board v3 bridge should start with conventional ESP32 SoftAP defaults:

- SoftAP IP: `192.168.4.1`
- UDP port: `9000`

These values keep the bench setup close to the current Smart Sentry network shape
and reduce unnecessary transport drift during early validation.

## Nano Listener Serial Assumption

The initial listener scaffold targets a classic Arduino Nano style board that does
not expose `Serial1`.

- USB `Serial` remains available for debug prints
- Passive bus sniffing uses `SoftwareSerial`

If the final hardware uses a different Nano-family board with a hardware UART,
the listener should be moved back to a real UART before any high-baud runtime use.

## v3 UDP Command Contract

The v3 bridge should stay as close as practical to the current Smart Sentry v2
UDP JSON command shape.

Primary fields:

- `pan_cmd`
- `tilt_cmd`
- `move_time_ms`
- `fire`
- `safety`
- `mode`
- `led`
- `laser`
- `acc`
- `spare`

For phase 1 bench work, the bridge may accept plain JSON while the final app
integration target remains the existing JSON plus CRC32 transport shape.

## ID 4 Accessory Register Map

ID 4 is retained only as a reserved future extension point. It is not required
for the primary single-controller v3 topology.

### Register `0x40` Accessory Flags

Single-byte bitfield:

- Bit 0: fire request
- Bit 1: safety armed
- Bit 2: projectile mode
- Bit 3: LED relay
- Bit 4: laser relay
- Bit 5: accessory relay
- Bit 6: spare relay
- Bit 7: reserved

### Register `0x41` Trigger Parameters

Four-byte payload:

- Byte 0: trigger rest angle in degrees
- Byte 1: trigger fire angle in degrees
- Byte 2: trigger pulse duration in 10 ms units
- Byte 3: reserved

### Register `0x42` Sequence And Heartbeat

Two-byte payload:

- Byte 0: sequence number
- Byte 1: heartbeat or watchdog timeout hint

## Phase 1 Firmware Responsibilities

### Waveshare ESP32 Bridge

- Host WiFi AP and UDP listener
- Parse motion and accessory JSON commands
- Emit Yahboom motion packets for ID 1 and ID 2
- Directly drive the confirmed trigger, relay, switch, and buzzer hardware
- Treat LED, laser, trigger-servo PWM, and knob inputs as unassigned until a
  confirmed header-accessible pin map is available
- Provide serial debug output for bench validation

### Nano Listener

- Optional contingency path only, not part of the primary v3 hardware plan

## Bench Validation Order

1. Verify Waveshare UDP receive and serial debug logs.
2. Verify Waveshare motion packet generation for IDs 1 and 2.
3. Verify direct Waveshare trigger, relay, switch, and buzzer outputs.
4. Confirm and assign the currently unassigned LED, laser, trigger-servo PWM,
   and knob input lines before implementing them.
5. Only after those pass, connect Smart Sentry app integration to the new path.

## Initial v3 Repository Artifacts

- `arduino/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE.ino`
- `arduino/SMART_SENTRY_V3_0_NANO_ID4_ACCESSORY_LISTENER/SMART_SENTRY_V3_0_NANO_ID4_ACCESSORY_LISTENER.ino`
- `sentry_v3_udp_bench_test.py`

The Nano listener scaffold remains in the repository only as a contingency path.

## Non-Goals For This First Step

- No modification of the current Smart Sentry v2 production sketch
- No replacement of current app transport logic yet
- No bus readback or telemetry return path from the Nano yet
- No use of ID 3 until the future trigger bus servo upgrade
- No implementation yet for speaker playback or volume knob inputs
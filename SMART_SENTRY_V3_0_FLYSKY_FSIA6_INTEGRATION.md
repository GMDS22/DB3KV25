# Smart Sentry v3.0 FlySky FS-iA6 Integration Direction

This note captures the clean way to add a FlySky hand controller path to the
current v3 Waveshare architecture.

## Bottom Line

Yes, FlySky control can fit into this setup, but with the exact FS-iA6 receiver
in hand the transport path must stay validation-driven rather than assumed.

## Recommended Receiver Strategy

Preferred when available:
- a FlySky receiver variant that exposes i-Bus or another summed serial output

Not preferred for direct Waveshare integration:
- a receiver that only exposes one PWM wire per channel without a decoder layer

Reason:
- the Waveshare header pin budget is already constrained
- the current v3 design only has a few confirmed header-backed pins left
- consuming 4 to 6 pins for discrete RC PWM channels is the wrong tradeoff

For the current FS-iA6 receiver, the correct fallback is either:
- use a supported summed RC output if that exact receiver provides one
- or add a tiny decoder layer that converts PWM channels into one serial/control stream

That is why the implementation now treats FS-iA6 control-source selection,
channel mapping, passive i-Bus runtime decoding, and live RC override as
first-class bridge state, while still leaving bench validation of the exact
receiver wiring path marked as validation-pending.

## Recommended Wiring Direction

Use the FlySky receiver as a local control source, but do not hard-claim the
final electrical path until the exact FS-iA6 signal behavior is bench-validated.

- Receiver power: header `5V` and `GND`
- Receiver signal path under validation: header pin `10` / `GPIO15` is now the implemented passive i-Bus RX path in firmware and remains the preferred bench-validation candidate for the exact receiver hardware in hand
- Header pin `8` / `GPIO14` stays reserved unless a return UART or telemetry path is needed later

This keeps the receiver off the already-claimed accessory outputs.

## Why Header Pin 10 Is The Best Candidate

- It is already treated as a reserved serial pin, not an accessory output
- It does not collide with the current bus-servo UART on GPIO18/GPIO19
- It preserves the confirmed accessory map on pins 7, 13, 22, 37, and 40

## Control Model

The FlySky path should be added as a local manual override input to the Waveshare bridge.

Recommended mapping for the current six-channel FlySky plan:
- CH1: pan manual command
- CH2: tilt manual command
- CH3: trigger intent
- CH4: accessory relay
- CH5: spare relay
- CH6: app-vs-RC source select

The existing hardware switch on header pin `40` / `GPIO21` remains the arm and
fire interlock, so CH5 does not need to be consumed for safety just to make the
FlySky path usable.

This is the best current mapping because it lets the receiver control all
currently assigned bridge-side functions without requiring an extra board switch
pin.

Current limitation:
- LED and laser are still unassigned at the board level, so they cannot be given
  trustworthy FS-iA6 channel claims yet

## Safety Model

The physical hardware switch on header pin `40` / `GPIO21` remains authoritative.

That means RC trigger input must still obey:

- hardware switch closed
- software safety armed
- no hardware fault condition

In other words, the FlySky path may request fire, but it must not bypass the
existing interlock chain.

## Recommended Source Arbitration

Use an explicit source-of-control policy inside the bridge.

Suggested order:
- App supervisory control remains default
- FlySky CH6 or the UI button can request RC mode without being near the computer
- RC input can override pan, tilt, trigger, accessory relay, and spare relay when receiver activity is present
- RC override should time out after inactivity and yield back to the app

This avoids fighting between the PC app and the hand controller.

## Separate Board Switch Question

A separate board-mounted RC mode switch is not required for the current plan.

Recommended answer:
- use FlySky CH6 as the local physical APP vs RC mode switch
- use the UI control-source button to command the same bridge mode remotely
- keep the existing hardware switch only as the arm and trigger interlock

Only add a second board switch input later if you specifically want a chassis
toggle that is independent of both the PC UI and the FlySky transmitter.

## Trigger Servo Implication

Do not combine FlySky receiver work with a guessed on-board trigger-servo PWM pin.

Current recommendation:
- keep the MOSFET trigger as the active v3 fire path
- if a physical trigger servo is added later, prefer:
  - Yahboom bus-servo trigger on reserved ID 3
  - or an external PWM source with a validated signal path

## Firmware Phases

### Phase RC-0

Document and reserve the serial input path only.

Done directionally by:
- reserving header pin `10` for future RC RX candidate validation
- keeping header pin `8` reserved for possible telemetry or return serial
- adding a bridge-side control-source mode that can be switched from the UI now

### Phase RC-1

Add passive RC decode in the Waveshare bridge.

Deliverables:
- decode receiver data
- publish RC active state in `state`
- advertise RC capability in `cap`
- no control override yet

Current status:
- implemented in firmware with a built-in i-Bus parser on header pin `10` / `GPIO15`
- publishes live channel telemetry when valid serial frames are present
- keeps RC override behavior out of scope for this phase

### Phase RC-2

Add manual pan and tilt override.

Deliverables:
- deadband around center sticks
- timeout when receiver signal stops updating
- explicit control-source state in `state`

Current status:
- implemented in firmware
- CH1 and CH2 now drive live pan and tilt override with a center deadband and direct source arbitration
- CH6 is honored when `control_source_mode="auto"`, while forced `app` and forced `rc` modes still obey the UI control-source request

### Phase RC-3

Add guarded trigger support.

Deliverables:
- RC trigger requests obey hardware switch, software safety, and fault state
- app and RC arbitration policy enforced in firmware

Current status:
- partially implemented in firmware
- CH3 now drives the existing MOSFET fire request path only when RC owns control, and the hardware switch plus software safety still gate the actual output
- CH4 and CH5 now drive the accessory and spare relays when RC owns control
- deeper no-fault integration still depends on future hardware fault wiring beyond the current bridge scaffold

## Bench Validation For RC Later

See also:

- `SMART_SENTRY_V3_0_FLYSKY_FSIA6_VALIDATION_CHECKLIST.md`

When receiver hardware is available, validate in this order:

1. receiver power and ground stability
2. serial receiver signal visibility on header pin `10`
3. stable RC frame decode while WiFi and bus-servo UART are both active
4. pan and tilt override only
5. trigger requests with interlocks enforced

## Current Decision

The FlySky path is feasible, and the current implementation now includes:

- a bridge control-source mode for APP vs RC
- a matching UI button for the same mode request
- a six-channel FS-iA6 mapping contract for the currently assigned bridge-side functions
- passive i-Bus receiver decode on header pin `10` / `GPIO15` with live RC telemetry fields in bridge `state`
- live RC override for pan, tilt, fire request, accessory relay, and spare relay with source arbitration enforced inside the bridge

The remaining open items are now:

- bench validation of the exact FS-iA6 electrical path in the real hardware setup
- guarded RC fire and relay actuation logic beyond passive telemetry

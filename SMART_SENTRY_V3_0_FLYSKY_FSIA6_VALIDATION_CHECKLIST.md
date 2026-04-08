# Smart Sentry v3.0 FlySky FS-iA6 Validation Checklist

This checklist is the next practical bench path for the FlySky control-source
mode, passive i-Bus decode path, RC runtime telemetry, and live override path.

It is intentionally split into two layers:

- bridge-mode and UI validation that can run now
- receiver electrical validation that starts once the exact FS-iA6 wiring path is ready

## Current Scope

This checklist validates the following already-implemented behavior:

- APP vs RC control-source mode
- bridge runtime reporting for RC link health and CH1 to CH6 values
- passive i-Bus decode support on header pin `10` / `GPIO15`
- FlySky channel map contract for currently assigned bridge outputs
- live RC override for pan, tilt, fire request, accessory relay, and spare relay
- UI visibility of RC mode and RC runtime health

It does not claim that the exact FS-iA6 receiver wiring on your physical bench is already validated.

## Current FlySky Channel Contract

- CH1: pan command
- CH2: tilt command
- CH3: fire request
- CH4: accessory relay
- CH5: spare relay
- CH6: APP vs RC source select

Still not assigned at board level:

- LED relay
- laser relay
- trigger-servo PWM

That means those functions are out of scope for this FlySky checklist.

## Safety Rules

- Keep the hardware interlock switch on header pin `40` / `GPIO21` in the loop for every fire-path test
- Treat CH3 as a fire request only, not as a safety bypass
- Keep a safe load or no live load connected during early trigger validation

## Phase A: Bridge Runtime Bring-Up

### A1. Capability Packet Check

Run:

```powershell
python .\sentry_v3_udp_bench_test.py --packet-type hello --listen-ms 1000
```

Expected result:

- one `ack`
- one `cap`
- `rc_mode_supported=true`
- `rc_input_supported=true`
- `rc_input_protocol="ibus_serial"`
- `rc_live_decode_enabled=true`
- `rc_receiver_model="flysky_fs_ia6"`
- `rc_source_switch_channel=6`
- `rc_runtime_stub_supported=true`
- `rc_channel_map` is present

### A2. APP Mode Command Check

Run:

```powershell
python .\sentry_v3_udp_bench_test.py --action rc_mode --rc-mode app --listen-ms 800
```

Expected result:

- `ack.ok=true`
- returned `state` shows `control_source_mode="app"`

### A3. RC Mode Command Check

Run:

```powershell
python .\sentry_v3_udp_bench_test.py --action rc_mode --rc-mode rc --listen-ms 800
```

Expected result:

- `ack.ok=true`
- returned `state` shows `control_source_mode="rc"`

### A4. RC Runtime Stub Injection Check

Run:

```powershell
python .\sentry_v3_udp_bench_test.py --action rc_stub --rc-mode rc --rc-link-active --rc-override-active --rc-frame-age-ms 22 --ch1-us 1520 --ch2-us 1460 --ch3-us 1000 --ch4-us 1880 --ch5-us 1120 --ch6-us 1900 --listen-ms 900
```

Expected result:

- `ack.ok=true`
- returned `state` shows:
  - `rc_link_active=1`
  - `rc_override_active=1`
  - `rc_frame_age_ms=22`
  - nested `rc` object with `ch1_us` through `ch6_us`

### A5. UI Reflection Check

With the Smart Sentry UI connected to the bridge, expected result:

- Control Source button changes to `FLYSKY` when RC mode is active
- bridge runtime line shows the active source
- FlySky status line shows:
  - mode
  - rc link state
  - override state
  - failsafe state if set
  - CH4, CH5, and CH6 values when present

## Phase B: UI and Local Mode-Switch Validation

### B1. UI Button Drives Bridge Mode

In the UI, toggle the Control Source button between `APP` and `FLYSKY`.

Expected result:

- bridge state changes between `control_source_mode="app"` and `control_source_mode="rc"`
- no app disconnect or command path stall occurs

### B2. CH6 Contract Check

Use the stub path first to simulate low and high CH6 values.

Low position example:

```powershell
python .\sentry_v3_udp_bench_test.py --action rc_stub --rc-mode app --rc-link-active --ch6-us 1000 --listen-ms 800
```

High position example:

```powershell
python .\sentry_v3_udp_bench_test.py --action rc_stub --rc-mode rc --rc-link-active --ch6-us 1900 --listen-ms 800
```

Expected result:

- UI and bridge state both reflect the intended source-selection contract for CH6
- when `control_source_mode="auto"`, low CH6 keeps app control and high CH6 transfers active control to RC

## Phase C: Accessory Mapping Validation

### C1. CH4 Accessory Relay Contract

Use stub input to represent CH4 high:

```powershell
python .\sentry_v3_udp_bench_test.py --action rc_stub --rc-mode rc --rc-link-active --rc-override-active --ch4-us 1900 --ch5-us 1000 --ch6-us 1900 --listen-ms 800
```

Expected result for this phase:

- bridge runtime reports CH4 high
- when RC owns the active source, the accessory relay output follows CH4 high and low transitions

### C2. CH5 Spare Relay Contract

Use stub input to represent CH5 high:

```powershell
python .\sentry_v3_udp_bench_test.py --action rc_stub --rc-mode rc --rc-link-active --rc-override-active --ch4-us 1000 --ch5-us 1900 --ch6-us 1900 --listen-ms 800
```

Expected result:

- bridge runtime reports CH5 high
- when RC owns the active source, the spare relay output follows CH5 high and low transitions

## Phase D: Real Receiver Electrical Validation

Start this phase only after the exact FS-iA6 wiring path is confirmed.

### D1. Receiver Power Check

Confirm:

- receiver powers correctly from the selected 5V and GND path
- no brownout occurs on the Waveshare side

### D2. Receiver Signal Path Check

Confirm:

- the implemented i-Bus path into header pin `10` / `GPIO15` is electrically valid for the exact receiver in use
- no conflict exists with servo-bus UART traffic

### D3. Live Channel Visibility Check

Expected result:

- bridge `state.rc` values change live with stick and switch movement
- CH6 movement can be observed directly in runtime telemetry

### D4. Fire Interlock Check Under RC Request

Expected result:

- CH3 may request fire only when:
  - hardware switch is closed
  - software safety is armed
  - no hardware fault is present

### D5. Live Pan And Tilt Override Check

Expected result:

- with RC active, CH1 and CH2 move the pan and tilt servos live
- center-stick deadband holds the last commanded position instead of dithering
- when RC times out or CH6 returns to APP in auto mode, motion authority yields back to the app cleanly

## Exit Condition

This FlySky checklist is complete when all of the following are true:

1. APP vs RC mode can be changed from both the UI and the bridge command path.
2. The bridge reports stable RC runtime health and CH1 to CH6 values.
3. CH6 is confirmed as the local APP vs RC selection contract.
4. CH4 and CH5 mapping are visible in runtime telemetry and verified against real output behavior when RC owns the active source.
5. Real receiver signal validation is complete for the exact FS-iA6 hardware path.
6. Live pan and tilt override behaves correctly under RC ownership and yields back cleanly when RC is no longer active.
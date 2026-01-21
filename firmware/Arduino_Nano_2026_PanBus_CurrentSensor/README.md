# Arduino Nano Firmware (2026) — Pan Serial-Bus + Current Sensor + PWM Tilt

Files:
- `Arduino_Nano_2026_PanBus_CurrentSensor.ino`

## Compatibility goals

This firmware is designed to be compatible with the existing host app serial protocol:

- Command line from host (newline terminated):
  - `P{pan}T{tilt}F{fire}L{led}R{laser}G{acc}S{safety}M{mode}`
- Encoder request from host:
  - `GET_ENCODER`
- Encoder response to host:
  - `ENCODER_TILT,<tilt_deg>,RAW_COUNT,<count>`

## Current monitoring

The firmware periodically reports **total turret current** from an analog current sensor.

Supported host telemetry formats:
- Legacy (this firmware family): `STAT I=<milliamps>`
- Serial-bus upgrade (Pan+Tilt+Total): `CUR PmA=<pan_mA> TmA=<tilt_mA> TOTmA=<total_mA>`

The app accepts both. For the full Pan+Tilt serial-bus upgrade sketch, see:
- `arduino/DB3000_SerialBus_Upgrade_2026/DB3000_SerialBus_Upgrade_2026.ino`

Tune calibration constants in the `.ino`:
- `SENSOR_ZERO_V`
- `SENSOR_SENS_V_PER_A`

## Tilt servo

Tilt remains PWM using `Servo.h`.
- Default limits in the `.ino` match the app defaults: `TILT_MIN=0`, `TILT_MAX=70`.

## Pan servo (serial-bus)

The repo does not specify the exact serial-bus servo family.

The `.ino` includes a selectable driver layer:
- `PAN_BUS_PROTOCOL_NONE` (default compile-safe stub)
- `PAN_BUS_PROTOCOL_YD_SD35M` (Yahboom YD-SD35M; 115200 UART via the driver/debug board)
- `PAN_BUS_PROTOCOL_LX16A` (alias for the same packet-based 0x55 0x55 family)

If your bus servo is not in the 0x55 0x55 family, do not enable it until you implement the correct protocol.

## Baud rate

- Host serial: `115200` (matches app defaults)

## Notes

- Tilt safety switch support is present but disabled by default (`TILT_SAFETY_SWITCH_INSTALLED=false`) to avoid host-side latch issues.

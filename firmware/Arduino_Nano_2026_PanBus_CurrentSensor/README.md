# Deprecated

The Arduino Nano current-sensor sketch that used to live in this folder was removed to reduce confusion.

For Dual Port (your setup: Nano COM8 + Debug Board COM9), use this Nano firmware:
- `arduino/DB3000_Nano_IO_Telemetry_2026/DB3000_Nano_IO_Telemetry_2026.ino`

For the legacy one-port topology (Nano drives the bus servos via the debug board), use:
- `arduino/DB3000_SerialBus_Upgrade_2026/DB3000_SerialBus_Upgrade_2026.ino`

Current telemetry formats accepted by the host:
- Total-only: `STAT I=<milliamps>`
- Pan+Tilt+Total (if enabled): `CUR PmA=<pan_mA> TmA=<tilt_mA> TOTmA=<total_mA>`


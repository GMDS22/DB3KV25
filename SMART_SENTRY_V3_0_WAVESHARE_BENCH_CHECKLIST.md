# Smart Sentry v3.0 Waveshare Bench Checklist

This checklist is the next practical step after locking the confirmed
header-based wiring map.

Use it to validate the narrowed v3 bridge before any app-side integration.

## Confirmed Header Map Under Test

- Header pin `7` / `GPIO4`: buzzer output
- Header pin `13` / `GPIO27`: trigger MOSFET output
- Header pin `22` / `GPIO25`: accessory relay output
- Header pin `37` / `GPIO26`: spare relay output
- Header pin `29` / `GPIO5`: speaker reserved only, do not wire active hardware yet
- Header pin `8` / `GPIO14`: UART TX reserved
- Header pin `10` / `GPIO15`: UART RX reserved

## Preconditions

1. Flash the bridge sketch:
   `arduino/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE.ino`
2. Power the Waveshare board safely.
3. Connect the test PC to WiFi SSID `WAVESHARE-ESP32`.
4. Confirm the PC can reach `192.168.4.1`.
5. Keep the trigger load physically safe before testing `fire` behavior.

## Session Bring-Up

Run from the repo root:

```powershell
python .\sentry_v3_udp_bench_test.py --packet-type hello --listen-ms 1000
```

Expected result:

- one `ack`
- one `cap`
- `sound_supported=true`
- `switch_supported=false`
- header pin references for trigger, accessory relay, spare relay, and buzzer
- `led_relay_assigned=false`
- `laser_relay_assigned=false`
- `trigger_servo_assigned=false`

## Bus Servo Path Check

```powershell
python .\sentry_v3_udp_bench_test.py --action bus_ping --listen-ms 1000
```

Expected result:

- `ack` and `state` replies
- at least one of the ping status fields for pan or tilt should report success if the bus wiring and servo path are live

## Motion Check

```powershell
python .\sentry_v3_udp_bench_test.py --pan 110 --tilt 40 --move-time-ms 200 --safety 1 --listen-ms 800
python .\sentry_v3_udp_bench_test.py --pan 70 --tilt 20 --move-time-ms 200 --safety 1 --listen-ms 800
```

Expected result:

- pan and tilt servos move
- returned `state` reflects the requested positions

## Buzzer Check

```powershell
python .\sentry_v3_udp_bench_test.py --action sound --sound-freq-hz 1500 --sound-duration-ms 200 --sound-volume-pct 100 --listen-ms 600
```

Expected result:

- audible tone on header pin `7` / `GPIO4`
- `ack` reply returns successfully

## Accessory Relay Check

Turn on accessory relay:

```powershell
python .\sentry_v3_udp_bench_test.py --acc --safety 1 --listen-ms 600
```

Turn it back off:

```powershell
python .\sentry_v3_udp_bench_test.py --safety 1 --listen-ms 600
```

Expected result:

- header pin `22` toggles with the `acc` field

## Spare Relay Check

Turn on spare relay:

```powershell
python .\sentry_v3_udp_bench_test.py --spare --safety 1 --listen-ms 600
```

Turn it back off:

```powershell
python .\sentry_v3_udp_bench_test.py --safety 1 --listen-ms 600
```

Expected result:

- header pin `37` toggles with the `spare` field

## Trigger MOSFET Check

Continuous mode:

```powershell
python .\sentry_v3_udp_bench_test.py --fire --mode 0 --safety 0 --listen-ms 600
python .\sentry_v3_udp_bench_test.py --safety 1 --listen-ms 600
```

Pulse mode:

```powershell
python .\sentry_v3_udp_bench_test.py --fire --mode 1 --safety 0 --trigger-pulse-ms 150 --listen-ms 800
```

Expected result:

- header pin `13` drives the trigger MOSFET
- continuous mode stays active until safety returns to `1`
- pulse mode asserts briefly, then self-clears

## Trigger Safety Check

Verify that software safety still blocks trigger output.

Safety locked:

```powershell
python .\sentry_v3_udp_bench_test.py --fire --mode 0 --safety 1 --listen-ms 600
```

Expected result:

- header pin `13` stays inactive

Safety armed:

```powershell
python .\sentry_v3_udp_bench_test.py --fire --mode 0 --safety 0 --listen-ms 600
python .\sentry_v3_udp_bench_test.py --safety 1 --listen-ms 600
```

Expected result:

- header pin `13` follows the trigger command path while `safety=0`

## Known Unassigned Items

Do not try to bench these yet from the v3 bridge:

- LED relay
- laser relay
- trigger servo PWM
- buzzer volume analog input
- speaker volume analog input
- active speaker output on header pin `29`

These remain intentionally unassigned until a confirmed header-accessible path is
validated from the hardware documentation.

## Exit Criteria

Bench validation is good enough to move toward app integration when all of the
following are true:

1. `hello` returns valid `ack` and `cap` packets.
2. `bus_ping` confirms at least one working readback path or the bus behavior is otherwise understood.
3. pan and tilt motion commands work repeatedly.
4. buzzer, accessory relay, spare relay, and trigger MOSFET all behave as expected.
5. no reserved UART pins are repurposed during testing.
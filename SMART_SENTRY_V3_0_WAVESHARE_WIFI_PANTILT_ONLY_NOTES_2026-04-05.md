# SMART SENTRY v3.0 Waveshare WiFi Pan/Tilt Only Notes

## Why this sketch exists

The closest previous success was the Step 7 A3 / Step 7.6 reintroduction path:

- WiFi SoftAP and UDP stayed stable.
- direct UDP probes to `192.168.4.1:9000` replied correctly.
- motion was not actually proven there because servo writes were still gated off until `REINTRO_STEP >= 9`.

The first motion-capable staged builds were Step 9 / Step 9.6, but those still carried broader bridge behavior and became unstable before any physical servo movement was confirmed.

This sketch is the simplified retry built from that history:

- keep the stable Waveshare SoftAP + UDP control path
- keep only UART2 bus-servo traffic on pins `18/19`
- force bus baud to `1000000`
- remove all accessory GPIO setup and output control
- accept only pan/tilt motion commands plus optional `bus_ping`

Sketch path:

- `arduino/SMART_SENTRY_V3_0_WAVESHARE_WIFI_PANTILT_ONLY/SMART_SENTRY_V3_0_WAVESHARE_WIFI_PANTILT_ONLY.ino`

## Bench intent

This is a motion-only wireless proof sketch. If pan and tilt still do not move with this firmware, the unresolved issue is in the Waveshare single-board ESP32-to-servo-bus path itself rather than in accessory logic or mixed bridge features.

## Expected runtime

- SSID: `WAVESHARE-ESP32`
- password: `smartv3pass`
- AP IP: `192.168.4.1`
- UDP port: `9000`
- pan servo ID: `1`
- tilt servo ID: `2`
- no accessory pins are initialized by this sketch

## Example UDP payloads

Pan only:

```json
{"seq":1,"p":{"pan_cmd":90}}
```

Tilt only:

```json
{"seq":2,"p":{"tilt_cmd":35}}
```

Pan + tilt:

```json
{"seq":3,"p":{"pan_cmd":120,"tilt_cmd":20,"move_time_ms":120}}
```

Asynchronous bus ping trigger:

```json
{"seq":4,"p":{"action":"bus_ping"}}
```

The reply reports whether motion or ping was queued and includes UART byte counters so serial activity can be checked without enabling any accessory behavior.
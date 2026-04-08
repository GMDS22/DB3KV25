# Smart Sentry v3.0 Waveshare Full Test Summary

Date: 2026-04-05

## Purpose

This document records the full Waveshare single-board bridge investigation, the staged firmware tests that were run, the exact pass and fail boundaries, the app-side issue discovered during live integration, and the current recommended operating point.

## Final Outcome

The highest stable single-board firmware found during this test chain is:

- Step 7 with A3 delayed UART init
- compile-time intent: `REINTRO_STEP=7` with `REINTRO_UART_INIT_DELAY_MS=2000`

Everything beyond that point regressed.

The current recommended live path is:

- flash Step 7 A3
- run the Smart Sentry app in single-board WiFi mode
- use the Waveshare bridge at `192.168.4.1:9000`

The critical app finding was:

- the app was still configured for dual-ESP32 WiFi mode `4`
- that mode sends movement to `192.168.4.2:9001`
- the live Waveshare single-board bridge responds on `192.168.4.1:9000`
- movement failures in the app were therefore caused by the wrong connection mode, not by an unresponsive board

## Original Goal

The target topology for this effort was:

- PC to Waveshare ESP32 over WiFi UDP only
- Waveshare ESP32 to the Yahboom bus-servo line as the motion bridge
- Waveshare on-board ESP32 also owning the local accessory GPIO pins
- no separate runtime servo board over USB

## Firmware And Repo Preparation Completed

The Waveshare bridge path was aligned to the confirmed contract before staged testing began.

Completed source and repo alignment:

- bus UART set to `GPIO18/GPIO19`
- target bus baud for the bridge set to `1000000`
- motion payload corrected to little-endian `POS_L POS_H TIME_L TIME_H`
- stale hardware-switch assumptions removed from the bridge contract
- bridge capability reporting made truthful
- UI and documentation updated to the switchless bridge contract
- pin-test and supporting docs aligned to the same assumptions

## Test Timeline

### Phase 1: Full Bridge Bring-Up

Primary file:

- `arduino/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE.ino`

Observed result:

- firmware built cleanly
- flashing succeeded
- serial reported SoftAP start and UDP begin success
- live ARP, ping, and UDP replies were not reliable

Meaning:

- basic boot and compile were not the blocker
- runtime SoftAP and UDP service behavior remained unstable

### Phase 2: Minimal Isolation Test

Isolation file:

- `arduino/SMART_SENTRY_V3_0_WAVESHARE_WIFI_UDP_ECHO_TEST/SMART_SENTRY_V3_0_WAVESHARE_WIFI_UDP_ECHO_TEST.ino`

Validated outcome:

- AP visible
- Windows connected successfully
- ARP resolved
- ping succeeded
- UDP echo succeeded
- serial reported `stations=1`

Meaning:

- the hardware ESP32 SoftAP and UDP stack are healthy in isolation
- the failure belongs to interactions introduced by bridge functionality, not to a dead WiFi board

### Phase 3: Controlled Reintroduction Harness

Primary staged file:

- `arduino/SMART_SENTRY_V3_0_WAVESHARE_BRIDGE_REINTRO_TEST/SMART_SENTRY_V3_0_WAVESHARE_BRIDGE_REINTRO_TEST.ino`

Runbook:

- `SMART_SENTRY_V3_0_WAVESHARE_BRIDGE_REINTRO_TEST_PLAN.md`

PlatformIO Step 1-4 project:

- `platformio/SMART_SENTRY_V3_0_WAVESHARE_STEP_1_4_TEST/`

### Step 1-4 Result

Validated outcome:

- AP stable
- ping stable
- structured UDP replies stable
- JSON parsing safe
- GPIO init safe

Meaning:

- WiFi, UDP, JSON, and GPIO init are not the failure point

### Step 5 Result

Step 5 contract:

- accessory GPIO control via direct payloads like `{"cmd":"set","pin":25,"value":1}`

Validated outcome:

- AP stable
- ping stable
- repeated UDP command and reply stable
- serial counters remained healthy

Meaning:

- live GPIO control is not the failure point

### Step 6A Base Result

Step 6A contract:

- UART init only
- no UART reads
- no UART writes
- no `available()` checks used to process data

Base configuration tested:

- `GPIO18/GPIO19`
- `250000` baud

Observed outcome:

- AP visible
- Windows connected
- ping stayed up
- UDP stalled after only a few packets
- serial showed `uart_rx=0` and `uart_parse=0`

Meaning:

- UART init alone is enough to destabilize network service on the original configuration

### Step 6A A1 Result

Variant:

- `REINTRO_UART_RX_PIN=16`
- `REINTRO_UART_TX_PIN=17`

Observed outcome:

- no real recovery
- alternate pins did not restore stable UDP behavior

Meaning:

- wrong pins were not the root cause

### Step 6A A2 Result

Variant:

- `REINTRO_UART_BAUD=115200`

Observed outcome:

- AP visible
- Windows associated
- ping failed at `95%` loss in the stress test
- UDP timed out immediately
- serial still showed no UART traffic

Meaning:

- lowering the UART init baud did not solve the regression

### Step 6A A3 Result

Variant:

- `REINTRO_UART_INIT_DELAY_MS=2000`

Observed outcome:

- startup was slower and the first scan looked bad
- after the settle window, the AP appeared and Windows re-associated
- steady-state ping passed `20/20`
- UDP replied successfully to repeated tests
- serial reported `stations=1`, with healthy UDP counters

Meaning:

- delayed UART init is the first configuration that stabilizes Step 6A on the original pins

### Step 7 Result

Configuration used:

- Step 7
- A3 delayed UART init retained

Observed outcome:

- first pass looked weak because Windows did not auto-reassociate cleanly
- after reconnect, ping passed `20/20`
- UDP replied successfully in repeated tests
- serial showed `stations=1`, `udp_rx=8`, `udp_tx=8`
- direct motion-related UDP packets also received valid state replies

Meaning:

- light UART RX is not the failure point
- Step 7 A3 is the highest stable single-board operating point found

### Step 8 Base Result

Configuration used:

- Step 8
- A3 delayed UART init retained
- bounded main-loop UART draining active

Observed outcome:

- AP visible
- Windows stayed associated
- ping ended at `45%` loss
- UDP returned only the first reply, then stalled

Meaning:

- bounded UART draining in the main loop breaks network stability

### Step 8 B2 Result

Configuration used:

- Step 8
- A3 delayed UART init retained
- `REINTRO_UART_TASK_MODE=1`
- bounded UART reads moved into a dedicated task

Observed outcome:

- AP visible
- Windows stayed associated
- ping ended at `40%` loss
- UDP again returned only the first reply, then stalled

Meaning:

- moving bounded reads into a dedicated task did not restore reliable runtime behavior

### Step 8 B3 Result

Configuration used:

- Step 8
- A3 delayed UART init retained
- `REINTRO_UART_TASK_MODE=1`
- `REINTRO_UART_RING_MODE=1`
- task-based ring buffering used to separate UART capture from processing

Observed outcome:

- AP visible
- Windows stayed associated
- ping failed `20/20`
- UDP produced no useful reply traffic

Meaning:

- B3 is a hard failure
- Step 8 remained unstable across all recovery variants tried

## App Integration Findings

### Waveshare Debugger Result

Tool used:

- `tools/waveshare_udp_debugger.py`

Direct verified probe result against the live Step 7 A3 board:

- `bus_ping` replied successfully
- center motion command replied successfully
- left motion command replied successfully
- right motion command replied successfully

Meaning:

- the live board responds correctly on `192.168.4.1:9000`
- the board is not the cause of the app-side movement failure once Step 7 A3 is flashed

### App Log Symptom

Observed app symptom:

- repeated `Move failed: movement command failed`
- repeated `Sound link unavailable`

### Root Cause In App Config

Saved settings before correction:

- `connection_type: 4`
- `udp_host: 192.168.4.1`
- `udp_port: 9000`
- `servo_udp_host: 192.168.4.2`
- `servo_udp_port: 9001`

Meaning of that config:

- mode `4` is dual-ESP32 WiFi mode
- movement is sent to the secondary servo endpoint `192.168.4.2:9001`
- the single-board Waveshare bridge does not use that second endpoint

Confirmed code path:

- mode `3` uses `_send_wifi_full(...)` to the primary UDP endpoint
- mode `4` uses `_send_servo_udp(...)` to the secondary endpoint

Files corrected:

- `app/config/smart_sentry_v3_settings.json`
- `app/app/config/sentry_v2_settings.json`

Applied correction:

- changed `connection_type` from `4` to `3`

Meaning:

- after restart, the app should send motion to the live Waveshare bridge on `192.168.4.1:9000`

## Final Retest After App Fix

Additional work after the app mode correction produced the following final validated status.

### Step 7.6 State-Machine Result

- a non-blocking UART state-machine variant was added and compiled successfully
- the Step 7.6 build flashed successfully
- WiFi and UDP behavior remained clean in the same way as the Step 7 A3 baseline
- this build could not prove motion because the staged sketch still compiles servo writes and `bus_ping` bridging only at `REINTRO_STEP >= 9`

Meaning:

- Step 7.6 validated scheduler behavior only
- it did not validate actual servo motion

### Step 9 State-Machine Result

- a Step 9 motion-capable state-machine build was compiled and flashed
- direct probing suggested the first motion-related packet was accepted at the network or protocol layer
- the board then dropped out of stable network service during the same direct test pass
- the user later confirmed that no visible servo movement had been observed

Meaning:

- the Step 9 test did not prove physical motion
- it only proved that the motion-capable single-board path was still unstable

### Baud Mismatch Candidate Identified

- the staged reintroduction sketch was still defaulting to `250000` baud
- the vendor-aligned bridge contract and earlier known-good assumptions used `1000000` baud on the bus path
- a new Step 9 state-machine build was compiled with `REINTRO_UART_BAUD=1000000`
- that build was prepared under `logs/precision_tuning/waveshare_reintro_step9_sm_1m`
- bench validation of that `1000000` baud Step 9 build was not performed because testing was stopped at the user's request

Meaning:

- a plausible remaining servo-path mismatch was identified
- it is not resolved in hardware-validated terms yet

## Final Recommended Live Setup

Firmware for motion:

- use the Debug Board USB path for pan and tilt

Firmware for accessories:

- keep the Waveshare ESP32 on WiFi for IO and accessory control only

App mode:

- use hybrid mode `2`

Expected runtime split:

- pan and tilt on Debug Board USB
- ESP32 WiFi accessories on `192.168.4.1:9000`

Recommended app launcher:

- `launch_smart_sentry.cmd`
- or `python run.py` from the repo root using the project virtual environment

## What Is Ruled Out

The following are no longer credible primary causes for the current movement issue when Step 7 A3 is active:

- broken WiFi board hardware
- broken basic UDP stack
- wrong basic packet shape for primary motion packets
- wrong primary endpoint for the single-board bridge
- inability of the Waveshare bridge to reply to valid UDP commands

## What Is Still Not Solved

The following remains unresolved for the single-board bridge path:

- stable motion-capable Step 9 behavior on the same hardware
- verified physical servo movement through the single-board WiFi bridge path
- hardware validation of the `1000000` baud Step 9 state-machine variant

## Practical Recommendation

Do not continue using the single-board WiFi bridge as the active runtime motion path.

Use the approved hybrid fallback instead:

- Debug Board USB for pan and tilt
- Waveshare ESP32 WiFi for IO and accessories

If later work resumes on the single-board bridge, resume from the current reintroduction sketch and test the prepared `1000000` baud Step 9 state-machine build before creating any new bridge branch.
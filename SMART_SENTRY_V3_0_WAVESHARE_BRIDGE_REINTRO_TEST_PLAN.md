# Smart Sentry v3.0 Waveshare Bridge Reintroduction Test Plan

This runbook starts from the known-good SoftAP plus UDP echo baseline and reintroduces one bridge feature at a time.

## Sketch

Use:

- `arduino/SMART_SENTRY_V3_0_WAVESHARE_BRIDGE_REINTRO_TEST/SMART_SENTRY_V3_0_WAVESHARE_BRIDGE_REINTRO_TEST.ino`

Set the active stage by changing:

- `#define REINTRO_STEP 6`

Or override it at compile time with a build flag when you want the next stage without editing the file.

UART test variants can also be changed at compile time:

- `REINTRO_UART_RX_PIN`
- `REINTRO_UART_TX_PIN`
- `REINTRO_UART_BAUD`
- `REINTRO_UART_INIT_DELAY_MS`
- `REINTRO_UART_STATE_MACHINE_MODE`
- `UART_RX_WINDOW_MS`
- `UART_RX_MAX_BYTES`
- `UART_RX_CHUNK_LIMIT`

## Hard Rule

- change only `REINTRO_STEP`
- flash
- test ARP, ping, UDP behavior, and station count
- stop immediately at the first regression

## Step Map

### Step 1

- UDP framework only
- raw echo behavior
- no JSON
- no GPIO
- no UART

Pass criteria:

- ARP OK
- ping OK
- UDP echo OK
- serial shows station count and stable heap

### Step 2

- adds JSON parsing only
- no actions taken from parsed content
- raw payload handling remains bounded

Pass criteria:

- no network regression from step 1

### Step 3

- replaces echo with structured JSON state reply
- still no GPIO and no UART

Pass criteria:

- consistent UDP replies
- no ARP or ping regression

### Step 4

- initializes accessory GPIO pins only
- no output toggling yet

Pass criteria:

- no WiFi degradation

### Step 5

- accepts UDP-driven accessory control
- direct command form: `{"cmd":"set","pin":25,"value":1}`
- supported pins:
	- `4` buzzer
	- `27` trigger
	- `25` relay1
	- `26` relay2
- direct `digitalWrite` only
- no loops and no extra delays beyond the existing `delay(1)`

Pass criteria:

- no ARP, ping, or UDP regression under repeated commands

### Step 6A

- initializes UART2 only
- `Serial2.begin(250000, SERIAL_8N1, 18, 19)` equivalent in the staged sketch
- no send or receive logic
- no `available()` checks
- no reads
- no writes

Pass criteria:

- WiFi remains stable after UART startup
- AP remains visible
- station count updates correctly
- ping and UDP remain stable for 60+ seconds

### Solution Path A

If Step 6A breaks WiFi immediately or within a few seconds, test these in order:

1. A1 alternate pins:
	- `REINTRO_UART_RX_PIN=16`
	- `REINTRO_UART_TX_PIN=17`
2. A2 lower baud:
	- `REINTRO_UART_BAUD=115200`
3. A3 delayed UART init:
	- `REINTRO_UART_INIT_DELAY_MS=2000`
4. A4 WiFi-first with settle delay:
	- already satisfied by sketch order
	- combine with `REINTRO_UART_INIT_DELAY_MS=1000`

If any of these restores WiFi stability, keep that configuration and move to Step 7.

If none of them work, treat UART plus WiFi on this board as unreliable and use the fallback architecture.

### Step 7

- light UART RX path
- reads at most one byte per loop
- no draining loop
- periodic `delay(0)` yield every ~1 ms

Pass criteria:

- WiFi remains stable

### Step 7.6

- non-blocking UART receive state machine variant for Step 7
- enabled with `REINTRO_UART_STATE_MACHINE_MODE=1`
- send path opens a short RX window after each servo write instead of blocking in place
- UART receive work is bounded three ways:
	- time window: `UART_RX_WINDOW_MS`
	- total bytes: `UART_RX_MAX_BYTES`
	- per-loop chunk: `UART_RX_CHUNK_LIMIT`
- default tuning:
	- `UART_RX_WINDOW_MS=15`
	- `UART_RX_MAX_BYTES=64`
	- `UART_RX_CHUNK_LIMIT=16`
- scope note: with `REINTRO_STEP=7`, this validates WiFi plus UART scheduling only; full servo motion and `bus_ping` bridging are still compiled in at Step 9

Pass criteria:

- WiFi remains as stable as the existing Step 7 A3 path
- UDP replies stay consistent under repeated motion-related traffic
- serial shows bounded UART completion logs without loop starvation

Example Step 7.6 compile override:

- `-DREINTRO_STEP=7 -DREINTRO_UART_INIT_DELAY_MS=2000 -DREINTRO_UART_STATE_MACHINE_MODE=1`

If Step 7.6 regresses, reduce in this order:

1. `UART_RX_CHUNK_LIMIT=8`
2. `UART_RX_WINDOW_MS=10`

### Step 9.6

- full-bridge motion-capable variant using the same non-blocking UART state machine
- use this build when the goal is to verify actual servo writes and `bus_ping` response handling under the Step 7.6 scheduler model

Example Step 9.6 compile override:

- `-DREINTRO_STEP=9 -DREINTRO_UART_INIT_DELAY_MS=2000 -DREINTRO_UART_STATE_MACHINE_MODE=1`

Latest campaign note:

- the `REINTRO_STEP=9` state-machine build was flashed and direct probing reached initial motion-path handling, but the board did not produce confirmed visible servo movement and network stability regressed during the same validation pass
- a follow-up build was compiled with `-DREINTRO_UART_BAUD=1000000` because the staged sketch was still defaulting to `250000` while the vendor-aligned bridge path uses `1000000`
- hardware validation of that `1000000` baud Step 9.6 follow-up did not occur because testing was stopped and the approved direction changed to the hybrid fallback topology

### Solution Path B

If Step 7 breaks WiFi, treat UART read behavior as the root cause and try these in order:

1. B1 bounded reads only:
	- keep the Step 8 limit of 16 bytes per loop
2. B2 separate UART task:
	- move UART polling to its own task with `vTaskDelay(1)`
3. B3 ring buffer only:
	- store bytes in a buffer and keep parsing out of the main loop

If WiFi still destabilizes, stop forcing the single-board WiFi bridge path.

### Step 8

- bounded UART buffer handling
- drains at most 16 bytes per loop
- lightweight marker counting only

Pass criteria:

- WiFi remains stable

Example B2 compile override:

- `-DREINTRO_STEP=8 -DREINTRO_UART_INIT_DELAY_MS=2000 -DREINTRO_UART_TASK_MODE=1`

Example B3 compile override:

- `-DREINTRO_STEP=8 -DREINTRO_UART_INIT_DELAY_MS=2000 -DREINTRO_UART_TASK_MODE=1 -DREINTRO_UART_RING_MODE=1`

### Step 9

- reintroduces targeted bridge behavior
- bus motion writes
- optional bus ping command handling

Pass criteria:

- full motion-related network stability remains intact

## Required Diagnostics

The staged sketch logs these every 5 seconds:

- `WiFi.softAPgetStationNum()`
- `ESP.getFreeHeap()`
- loop execution time in microseconds
- max loop execution time
- UDP RX and TX counters
- UART RX and lightweight parse counters

## Stop Condition

If a step causes any of the following, stop there:

- station count fails while Windows is connected
- ARP resolution fails
- ping fails
- UDP replies become inconsistent
- heap collapses abnormally
- loop timing spikes hard compared to the previous step

The last feature added at that step is the root-cause candidate.

## Final Fallback

If repeated Step 6A, Step 7, or Step 8 attempts fail:

- motion path:
	- PC to Waveshare servo driver over USB
- accessory path:
	- on-board ESP32 over WiFi for GPIO only

This preserves stable motion and stable WiFi by avoiding UART plus WiFi timing conflicts.

## Alternative Fallback

If WiFi transport is still required but SoftAP becomes undesirable, use STA mode instead of SoftAP.

## Last Resort

Split the system:

- Waveshare board for servo driver only
- separate ESP32 for WiFi bridge duties

## Immediate Next Commands

Step 5 test payload:

- `{"cmd":"set","pin":25,"value":1}`

Step 6A build override idea:

- compile with `REINTRO_STEP=6` and keep runtime checks identical to Step 5 before moving to any UART RX path.

Example A1 compile override:

- `-DREINTRO_STEP=6 -DREINTRO_UART_RX_PIN=16 -DREINTRO_UART_TX_PIN=17`

Example A2 compile override:

- `-DREINTRO_STEP=6 -DREINTRO_UART_BAUD=115200`

Example A3 or A4 delay override:

- `-DREINTRO_STEP=6 -DREINTRO_UART_INIT_DELAY_MS=2000`
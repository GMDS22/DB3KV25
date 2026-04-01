# Waveshare ESP32 + Arduino Nano Integration Plan
## Single Network Source Architecture with ID3 Accessory Control

**Document Version**: 1.0  
**Date**: March 29, 2026  
**Status**: Planning Phase (No Code Changes Yet)  
**Objective**: Replace dual-ESP32 system with single Waveshare ESP32 board + Arduino Nano for accessory control

---

## Executive Summary

### Problem Statement
Current dual-ESP32 architecture suffers from:
- WiFi deadlock when both boards initialize UART communication
- GPIO0 boot mode conflicts preventing reliable firmware flashing
- Complex packet routing across dual network bridges
- Unreliable servo control during high-frequency targeting cycles

### Proposed Solution
Single Waveshare ESP32-WROOM-32 board with integrated serial bus servo driver:
- **Single Network Source**: PC talks only to `192.168.4.2:9001` via UDP (WiFi)
- **Servo Control**: Pan/Tilt via ID1/ID2 (built-in on Waveshare)
- **Accessory Control**: Fire/Laser/PWM trigger via ID3 (Arduino Nano via wired UART)
- **Communication**: Yahboom bus protocol (`0xFF 0xFF ID LEN CMD PAYLOAD CHK`) at 1M baud
- **Wiring**: Nano UART1 connected to ESP32 GPIO16/GPIO17 (UART2)

### Validation Status
✅ **ARCHITECTURE VALIDATED** - GPIO16/GPIO17 UART2 already in production use for Debug Board
✅ **PROTOCOL CONFIRMED** - Yahboom bus supports up to 254 device IDs (ID1/ID2/ID3 proven pattern)
✅ **CODEBASE READY** - Existing patterns in sentry_v2_comm.py and DB3000_ESP32_UDP_PIR.ino can be extended

---

## Technical Specifications

### Hardware Components

#### Waveshare ESP32-WROOM-32 Servo Driver HAT
- **Model**: Waveshare ESP32-WROOM-32 with integrated serial bus servo driver
- **WiFi**: Built-in (802.11 b/g/n)
- **Servo Support**: Native ST/RSBL series (1,000,000 baud bus)
- **Power Input**: 9-25V (servo voltage compatible)
- **Key GPIO Pins**:
  - **GPIO16**: UART2 RX (from Debug Board / Nano TX)
  - **GPIO17**: UART2 TX (to Debug Board / Nano RX)
  - **GPIO25**: Current fire control (optional fallback)
  - Multiple GPIO available for PWM/relay control

#### Arduino Nano (Accessory Controller)
- **Model**: Arduino Nano (ATmega328P)
- **Role**: Dedicated accessory controller (no WiFi)
- **UART Connection**: TX → ESP32 GPIO16 (RX), RX ← ESP32 GPIO17 (TX)
- **Functions**:
  - Fire relay triggering via bus commands (ID3)
  - Laser enable/disable via bus commands
  - PWM servo control via bus commands (accessory servo)
  - Safety interlock logic

#### Servo Configuration
- **Pan Servo**: `ID = 1` (Yahboom bus address)
- **Tilt Servo**: `ID = 2` (Yahboom bus address)
- **Accessory Servo/Relay**: `ID = 3` (Yahboom bus address via Nano)

### Communication Protocol

#### Yahboom Serial Bus Format
```
Frame Structure: [0xFF][0xFF][ID][LENGTH][INSTRUCTION][PARAM1][PARAM2]...[CHECKSUM]

0xFF 0xFF     : Header (sync bytes)
ID            : Device ID (0-253, shown here as 0x01-0x03)
LENGTH        : Payload length (instruction + parameters)
INSTRUCTION   : Command byte (0x03=write position, 0x08=fire, etc.)
PARAMETERS    : Command-specific data
CHECKSUM      : XOR or subtraction based on mode
BAUD          : 1,000,000 bps (1M)
```

#### Example Packets
```
Pan Servo Move:    [0xFF][0xFF][0x01][0x04][0x03][0x68][0x29][0x40]  → ID1, move to position 0x2968
Tilt Servo Move:   [0xFF][0xFF][0x02][0x04][0x03][0x84][0x03][0x6B]  → ID2, move to position 0x0384
Fire Command (ID3): [0xFF][0xFF][0x03][0x02][0x08][0x01][0xF5]       → ID3, execute fire instruction
```

#### Network Layer (UDP)
- **Protocol**: JSON + CRC32 checksum
- **Endpoint**: `192.168.4.2:9001`
- **Source**: PC (application on Windows/Linux)
- **Transport**: Single WiFi connection (no dual AP/STA mode)

#### Wiring (Physical UART2)
```
ESP32 GPIO16 (UART2 RX) ← Nano TX (Pin 1)
ESP32 GPIO17 (UART2 TX) → Nano RX (Pin 0)
ESP32 GND              ↔ Nano GND (common ground)
```

### Software Architecture

#### Packet Flow
```
PC Application (Windows)
    ↓ UDP JSON + CRC32
    ↓ 192.168.4.2:9001
    ↓
ESP32 (WiFi Receiver)
    ├─ Parse JSON packet
    ├─ Extract target command (pan, tilt, fire)
    ├─ Build Yahboom packets
    ├─ Route by ID:
    │  ├─ ID1 → Pan Servo (internal bus)
    │  ├─ ID2 → Tilt Servo (internal bus)
    │  └─ ID3 → TX on GPIO17 → Nano RX
    ↓
Arduino Nano (Serial Receiver)
    ├─ UART1 RX at 1M baud (GPIO17 input)
    ├─ Parse Yahboom packet
    ├─ Detect ID3 address
    ├─ Execute command:
    │  ├─ 0x08 → Fire relay trigger
    │  ├─ 0x09 → Laser on/off
    │  ├─ 0x0A → Accessory servo PWM
    │  └─ 0x0B → Safety interlock
    ↓
Accessory Outputs
    ├─ Fire relay (GPIO 5)
    ├─ Laser control (GPIO 6)
    ├─ PWM servo (GPIO 9, 10MHz clock)
    └─ Safety indicator (GPIO 7)
```

#### Software Components

**[sentry_v2_tab.py](sentry_v2_tab.py)** (4000+ lines)
- Current: UI displays GPIO16/17 UART2 configuration for Debug Board
- Role: Unchanged for this integration (already supports ID1/ID2 configuration)
- Future: Add "ID3 Accessory Mode" toggle to fire control

**[sentry_v2_comm.py](sentry_v2_comm.py)** (1000+ lines)
- Current: Builds packets for ID1/ID2 servos
- Role: Core integration point for ID3 commands
- Methods to extend:
  - `send_id3_command(cmd, payload)` - Send Yahboom packet to ID3
  - `_build_id3_packet(cmd, payload)` - Format ID3 packet with checksum
  - Route fire button → ID3 command dispatch

**[DB3000_ESP32_UDP_PIR.ino](arduino/DB3000_ESP32_UDP_PIR/DB3000_ESP32_UDP_PIR.ino)** (1000+ lines)
- Current: Receives WiFi UDP, builds ID1/ID2 packets
- Role: Add ID3 packet routing on GPIO17
- Code to add:
  - Detect `0xFF 0xFF 0x03` headers in serialized commands
  - Format ID3 packet: `buildID3Packet(cmd, payload)`
  - TX on GPIO17 with 1M baud handoff

**Arduino Nano Firmware** (NEW - ~300 lines)
- Current: None (will be created)
- Role: Receive ID3 packets, execute accessory actions
- Implementation:
  - UART1 initialization at 1M baud (custom baud setting)
  - Yahboom packet parser
  - Relay/laser/servo dispatch logic
  - Safety interlock enforcement

---

## Implementation Phases

### Phase 0: Waveshare ESP32 + Servo Testing (BLOCKING)
**Objective**: Verify that the Waveshare ESP32 board can control pan/tilt servos via wireless connection from PC application.

**Rationale**: Before integrating the Nano and ID3 command layer, confirm that:
1. Waveshare board boots correctly and establishes WiFi
2. Existing servo control code (ID1/ID2) works with physical hardware
3. UDP packet flow PC → ESP32 → servos is functional
4. GPIO16/GPIO17 UART2 is accessible for Nano integration

**Deliverables**:
- ✅ Waveshare ESP32 flashed with current `DB3000_ESP32_UDP_PIR.ino`
- ✅ Pan/Tilt servos responding to PC application commands
- ✅ Boot message confirms: `UART2 baud=1000000 RX=GPIO16 TX=GPIO17`
- ✅ Wireless latency measured (<100ms target)
- ✅ Servo position repeatability verified (±5 degree tolerance)

**Tasks**:
1. Flash Waveshare board with `DB3000_ESP32_UDP_PIR.ino` firmware
   - Use arduino-cli or Arduino IDE
   - Verify boot messages via serial terminal (115,200 baud on USB)
   - Confirm WiFi SSID and IP address (192.168.4.2 target)
   
2. Wire pan/tilt servos to Waveshare board
   - Power: 9-12V to servo power connector
   - Data: Pan servo to port 1 (ID1), Tilt servo to port 2 (ID2)
   - Test with simple position commands
   
3. Run basic servo test via PC application
   - Start `run.py` application
   - Set connection mode to "WiFi Full" (MODE_WIFI_FULL = 3)
   - Send pan/tilt commands from UI
   - Observe servo movement and response timing
   
4. Measure wireless communication latency
   - Send 10 rapid pan commands (0° → 90° → 0°)
   - Record time from PC command to servo movement start
   - Target: <100ms average latency
   - Document any packet loss or retries
   
5. Log boot diagnostics
   - Capture serial output from ESP32 during startup
   - Confirm all initialization messages
   - Save to `PHASE_0_BOOT_LOG.txt`

**Success Criteria**:
- [ ] Waveshare boots successfully and prints UART2 configuration message
- [ ] WiFi connects and shows correct IP (192.168.4.2)
- [ ] Pan servo responds to PC application pan commands (live video pan follows target)
- [ ] Tilt servo responds to PC application tilt commands (live video tilt follows target)
- [ ] Round-trip latency ≤100ms for 90° pan movement
- [ ] 30-minute soak test with no packet loss or servo lock-ups
- [ ] GPIO16/GPIO17 visible on scope during UART2 communication (if scope available)

**Failure Modes & Recovery**:
| Issue | Symptom | Recovery |
|-------|---------|----------|
| Board won't flash | arduino-cli: permission denied | Run PowerShell as Admin, check COM port |
| No WiFi connection | Boot hangs at "WiFi init..." | Verify WiFi SSID in firmware, restart router |
| Servos unresponsive | Motors silent, no current draw | Check servo power connector voltage (9-12V) |
| Packet timeout | PC shows "no response" error | Verify UDP port 9001 not blocked by firewall |
| Servo jitter | Servo oscillates ±5° continuously | Check power supply ripple, reduce move time |
| GPIO16/17 conflict | "UART2 init failed" error | Ensure Debug Board not connected during test |

**Estimated Duration**: 2-3 hours (including servo calibration and latency testing)

**Exit Criteria**: All success criteria met AND `PHASE_0_RESULTS.txt` documents:
- Boot message timestamp
- WiFi connection status
- Latency measurements (min/max/avg)
- Servo position readback (confirm feedback working)
- Any anomalies encountered

---

### Phase 1: Physical Hardware Verification
**Objective**: Confirm GPIO16/GPIO17 accessibility on Waveshare board and verify Nano wiring compatibility.

**Rationale**: 
- GPIO16/GPIO17 UART2 is documented in firmware but physically unavailable on some board revisions
- Nano UART1 baud rate (1M) must be verified achievable
- Physical wiring and signal integrity must be confirmed before firmware development

**Deliverables**:
- ✅ Waveshare GPIO16/GPIO17 header location identified and accessible
- ✅ Nano UART1 successfully configured at 1M baud
- ✅ Oscilloscope verification of UART signals (if available)
- ✅ Test data: Packet sniffer logs showing ID1/ID2 traffic on GPIO17 TX

**Tasks**:
1. Identify GPIO16/GPIO17 header on Waveshare board
   - Consult physical pinout diagram in `WAVESHARE SERVO DRIVER HAT` folder
   - Locate GPIO16 and GPIO17 on header or debug interface
   - Test continuity with multimeter to confirm header is active
   
2. Configure Arduino Nano for 1M baud UART1
   - Write test sketch: `nano_uart_init_test.ino`
   - Initialize Serial (TX/RX pins) at 1,000,000 baud
   - Flash Nano and verify boot message
   
3. Wire Nano to Waveshare (temporary test connection)
   - Nano TX (pin 1) → ESP32 GPIO16 (with 4.7kΩ pullup to 3.3V)
   - Nano RX (pin 0) → ESP32 GPIO17 (no pullup needed, 3.3V tolerant)
   - Common ground between boards
   - Do NOT connect power between boards (each has own supply)
   
4. Run packet sniffer on Nano
   - Program Nano with `uart2_packet_sniffer.ino`
   - Nano listens on UART1 and logs all `0xFF 0xFF` headers
   - Forward packets via USB serial to PC for analysis
   
5. Send test commands from ESP32
   - Flash ESP32 with `DB3000_ESP32_UDP_PIR.ino`
   - Trigger pan/tilt via PC application
   - Observe ID1/ID2 packets appearing on Nano sniffer
   - Document packet timing and checksum validity

**Success Criteria**:
- [ ] GPIO16/GPIO17 header physically accessible (soldering iron test)
- [ ] Nano UART1 configured and verified at 1M baud
- [ ] Sniffer captures `0xFF 0xFF 0x01` (pan) and `0xFF 0xFF 0x02` (tilt) packets
- [ ] Packet timing consistent (within ±10% of expected interval)
- [ ] No corruption in packet payloads (checksums valid)
- [ ] Oscilloscope shows clean UART signals (if available: >2.5V high, <0.5V low)

**Estimated Duration**: 3-4 hours (plus soldering time if headers need attachment)

---

### Phase 2: Add ID3 Support to ESP32 Firmware
**Objective**: Extend `DB3000_ESP32_UDP_PIR.ino` to recognize ID3 command packets and route them to UART2 TX (GPIO17).

**Rationale**:
- ID1/ID2 packets are built but only sent to internal servo bus
- ID3 packets must be built AND transmitted on GPIO17 to reach Nano
- Existing packet-building code can be refactored into generic `buildYahboomPacket(id, cmd, payload)`

**Deliverables**:
- ✅ Modified firmware: `DB3000_ESP32_UDP_PIR_ID3.ino`
- ✅ New helper function: `sendID3Command(cmd, payload)`
- ✅ Routing logic: UDP → ID1/ID2/ID3 packet builder → correct TX channel
- ✅ Test results: ID3 packets captured on oscilloscope or Nano sniffer

**Code Patterns**:
```cpp
// Existing (ID1/ID2):
servoController.write(servo_position);  // Internal bus

// New (ID3):
uint8_t packet[] = buildYahboomPacket(0x03, 0x08, payload);
Serial2.write(packet, packet_length);   // GPIO17 TX
```

**Tasks**:
1. Analyze existing servo packet builder in `DB3000_ESP32_UDP_PIR.ino`
   - Locate position-building function
   - Identify checksum calculation (XOR vs subtraction)
   - Extract into reusable `buildYahboomPacket(id, cmd, params[])`
   
2. Create ID3 commands dispatcher
   - Add switch case: `if (servo_id == 3) { ... }`
   - Build Yahboom packet matching format: `0xFF 0xFF 0x03 LEN CMD PARAMS CHK`
   - Add delay for UART2 turnaround time (~10ms for 256-byte packet at 1M baud)
   
3. Route JSON commands to ID3
   - UDP packet parsing already handles "cmd": "fire", "cmd": "laser"
   - Add to switch: `case 3: sendID3Command(cmd, payload); break;`
   - Document command bytecodes (0x08=fire, 0x09=laser, 0x0A=pwm, 0x0B=safe)
   
4. Test with packet sniffer
   - Send fire command via PC application
   - Verify `0xFF 0xFF 0x03` packet appears on GPIO17
   - Confirm packet structure and checksum
   
5. Validate latency impact
   - Measure delay from UDP rx to UART2 tx
   - Target: <50ms for ID3 command transmission
   - Ensure pan/tilt commands still respond with <100ms latency

**Success Criteria**:
- [ ] Code compiles without warnings
- [ ] Firmware boots normally (no additional startup latency)
- [ ] Sniffer shows `0xFF 0xFF 0x03` packets in response to fire commands
- [ ] Packet checksum valid on all ID3 messages
- [ ] Pan/tilt latency unchanged (<100ms)
- [ ] 30-minute soak test with mixed ID1/ID2/ID3 commands

**Estimated Duration**: 4-6 hours (including testing and debugging)

---

### Phase 3: Python Integration (sentry_v2_comm.py)
**Objective**: Extend PC application to send ID3 commands via UDP when fire button is pressed.

**Rationale**:
- Current application sends ID1/ID2 commands via `send_servo_command()`
- Fire button currently triggers GPIO25 relay on ESP32
- New mode: Fire button → UDP ID3 packet → Nano relay (more reliable routing)

**Deliverables**:
- ✅ Modified `sentry_v2_comm.py` with `send_id3_command(cmd, payload)` method
- ✅ Fire button routing: toggle between GPIO25 and ID3 modes
- ✅ UI indicator in `sentry_v2_tab.py` showing active fire control mode
- ✅ Test results: Fire button triggers Nano relay via ID3 packets

**Tasks**:
1. Add ID3 command builder to `sentry_v2_comm.py`
   ```python
   def send_id3_command(self, cmd: int, payload: List[int]) -> bool:
       """Send fire/laser/safety command to Nano via ID3."""
       packet = self._build_id3_packet(cmd, payload)
       return self._send_packet(packet)
   ```
   
2. Implement `_build_id3_packet()` matching ESP32 format
   - Header: `[0xFF, 0xFF]`
   - ID: `0x03`
   - Length: `len(cmd_bytes) + payload`
   - Checksum: match ESP32 calculation (XOR or subtraction)
   
3. Route fire button to ID3 command
   - Locate fire button handler in `sentry_v2_tab.py`
   - Add mode check: if `USE_ID3_FIRE` → `send_id3_command(0x08, [duration])`
   - Else → existing GPIO25 relay trigger
   
4. Add UI toggle for fire mode
   - New checkbox: "Use Serial Bus Fire (ID3) → requires Nano"
   - Display indicator: green (ID3) or yellow (GPIO25 fallback)
   - Store preference in config
   
5. Test fire control
   - Nano wired and powered
   - Fire button toggle between GPIO25 and ID3 modes
   - Verify relay triggers in both modes
   - Measure response timing: target <50ms from button press to relay close

**Success Criteria**:
- [ ] Code compiles without errors in Python
- [ ] Fire button sends ID3 packet when mode enabled
- [ ] Relay triggers via Nano (audible click if relay present, LED if not)
- [ ] Fallback to GPIO25 works if Nano disconnected
- [ ] UI mode toggle functional and persistent
- [ ] No interference with pan/tilt command timing

**Estimated Duration**: 2-3 hours

---

### Phase 4: Arduino Nano Firmware Implementation
**Objective**: Create Nano firmware to parse ID3 packets and control fire relay, laser, and accessory servo.

**Rationale**:
- Nano will be dedicated accessory controller (no WiFi complexity)
- Must handle 1M baud UART and latency-sensitive relay triggering
- Safety interlock logic (don't fire if pointed at friendly) runs on Nano

**Deliverables**:
- ✅ Nano firmware: `DB3000_Nano_ID3_Accessory.ino` (~300 lines)
- ✅ Command handlers for: fire relay, laser, pwm servo, safety interlock
- ✅ Watchdog timer: disable relay if no heartbeat for 500ms
- ✅ Test results: all commands verified and timed

**Tasks**:
1. Create Nano UART1 parser
   - Initialize `Serial` (pins 0/1) at 1M baud
   - Circular buffer for incoming bytes
   - Detect `0xFF 0xFF 0x03` header
   - Parse length and extract payload
   
2. Implement command dispatch
   ```cpp
   0x08: Fire relay trigger (pulse 100-500ms based on payload)
   0x09: Laser toggle (payload[0] = 1 for on, 0 for off)
   0x0A: PWM servo (payload[0] = angle 0-180 or 0-255 PWM)
   0x0B: Safety interlock update (payload[0] = armed/disarmed)
   ```
   
3. Add relay control logic
   - Fire relay on GPIO pin 5 (configurable)
   - Pulse duration encoded in payload: `0x08 [duration_ms_high] [duration_ms_low]`
   - Maximum pulse: 500ms (safety limit)
   - Watchdog: if 500ms without any command, disable relay
   
4. Add laser control
   - Laser enable GPIO pin 6
   - Toggle on/off via 0x09 command
   - Can be tied to fire relay (fire + laser) or independent
   
5. Add accessory servo PWM
   - PWM on GPIO pin 9 (50Hz standard servo frequency)
   - Payload: 8-bit value → 1000-2000µs pulse (90° range)
   - Or full 16-bit override for fine control
   
6. Add safety interlock watchdog
   - Safety arm/disarm via 0x0B command
   - If disarmed, relay and laser forced off
   - If no command received for 500ms, force safe state
   - Heartbeat indicator: LED blink on GPIO 7

**Success Criteria**:
- [ ] Nano firmware compiles for ATmega328P
- [ ] UART1 boots at 1M baud (verify with terminal)
- [ ] Fire relay pulses in response to ID3 0x08 commands
- [ ] Laser toggles in response to 0x09
- [ ] Servo responds to 0x0A (move to commanded angle)
- [ ] Watchdog activates relay shutdown after 500ms no-command
- [ ] Safety interlock prevents fire when disarmed
- [ ] 1-hour soak test with rapid fire commands

**Estimated Duration**: 5-8 hours (including safety verification)

---

### Phase 5: End-to-End Integration Testing
**Objective**: Verify complete chain: PC application → ESP32 → Nano → relay/laser/servo with timing and reliability verification.

**Rationale**:
- Individual components tested; now verify system behavior under load
- Detect race conditions, packet loss, and latency cascade effects
- Validate safety interlocks and failsafe behavior
- Document performance baseline for future upgrades

**Deliverables**:
- ✅ Test plan: `WAVESHARE_ID3_INTEGRATION_TEST_PLAN.txt`
- ✅ Test results: `WAVESHARE_ID3_TEST_RESULTS.txt` (latency timings, error logs)
- ✅ Performance baseline: latency histogram, packet loss rate
- ✅ Safety verification: watchdog, interlock, failsafe all functioning
- ✅ Production readiness checklist completed

**Tests**:

**Test 5.1: Rapid Fire Sequence**
- Objective: Fire button pressed 10 times in 5 seconds (2 Hz)
- Expected: Relay closes/opens for each press, <500ms per pulse
- Measurement: Oscilloscope on relay GPIO or relay coil current
- Pass Criteria: All 10 pulses captured, no missed edges, consistent timing

**Test 5.2: Pan/Tilt + Fire Interference**
- Objective: Pan/tilt movement while fire button pressed continuously
- Expected: Servos track target while relay pulses, no servo jitter
- Measurement: Visual (video shows smooth pan) + UDP packet sniffer (no retries)
- Pass Criteria: Smooth motion, no packet loss, sub-100ms latency

**Test 5.3: Safety Interlock Lockout**
- Objective: Disarm safety via 0x0B command, attempt fire
- Expected: Fire command ignored, relay NOT triggered
- Measurement: Relay GPIO and command log
- Pass Criteria: Relay silent, log shows command rejected

**Test 5.4: Watchdog Timeout**
- Objective: Send fire command, wait 600ms with no heartbeat
- Expected: Relay forced off after 500ms timeout
- Measurement: Relay GPIO duration measurement
- Pass Criteria: Relay active for ~100-200ms (fire pulse) then idle, watchdog at 500ms mark

**Test 5.5: 30-Minute Soak Test**
- Objective: Continuous operation with mixed commands for 30 min
  - Pan/tilt commands every 500ms
  - Fire commands every 3 seconds
  - Laser toggle every 10 seconds
- Expected: No packet loss, no servo lock-ups, no relay failures
- Measurement: Command counter, error log, watchdog actuation count
- Pass Criteria: 0 errors logged, <1% packet loss, watchdog not triggered

**Test 5.6: Latency Measurement**
- Objective: Measure end-to-end delay: UDP tx → Nano GPIO change
- Expected: <50ms P95, <100ms P99
- Measurement: Hardware timing: fire GPIO toggled at exact time packet sent from PC, oscilloscope captures latency
- Pass Criteria: >95% commands <50ms, 100% commands <100ms

**Test 5.7: Failsafe Validation**
- Objective: Unplug Nano UART cable during fire command
- Expected: ESP32 continues responding to pan/tilt, fire command fails gracefully
- Measurement: UI error indication, log entry, servo motion continues
- Pass Criteria: Pan/tilt responsive within 100ms, fire error logged, no crash

**Test 5.8: WiFi Dropout Recovery**
- Objective: WiFi disconnect/reconnect cycle while system running
- Expected: All commands queued, resume after WiFi restore
- Measurement: WiFi disconnection log timestamp vs. reconnection vs. command response recovery
- Pass Criteria: <5 sec reconnection, all commands after reconnect successful

**Success Criteria**:
- [ ] All 8 tests pass (0 critical failures)
- [ ] Latency measurements: P95 <50ms, P99 <100ms
- [ ] Packet loss: <0.5% over 30-minute soak
- [ ] Relay pulse consistency: ±10% of commanded duration
- [ ] Safety interlock: 100% command rejection when disarmed
- [ ] Watchdog triggered: 0 times during normal operation
- [ ] WiFi stability: <1 dropout per hour

**Estimated Duration**: 6-8 hours (includes test execution and result documentation)

---

## Execution Timeline & Dependency Graph

```
Phase 0: Waveshare + Servo Test (BLOCKING)
    ↓ [Must complete before Phase 1]
    ├── GPIO16/GPIO17 confirmed accessible
    ├── Servo control verified wireless
    └── UART2 message visible in boot logs
    
Phase 1: Hardware Verification
    ↓ [Parallel: can start Phase 2]
    ├── GPIO16/GPIO17 header soldered/accessible
    ├── Nano UART at 1M baud verified
    └── Packet sniffer confirms ID1/ID2 traffic
    
Phase 2: ESP32 Firmware (ID3 Routing)
    ↓ [Depends on: Phase 1 completed]
    ├── ID3 packet builder added
    ├── GPIO17 TX routing implemented
    └── Sniffer shows ID3 packets
    
Phase 3: Python Integration
    ↓ [Parallel: can start Phase 4]
    ├── `send_id3_command()` method added
    ├── Fire button mode toggle working
    └── Testing with mock Nano works
    
Phase 4: Nano Firmware
    ↓ [Depends on: Phase 1 completed, parallel with Phase 3]
    ├── UART1 parser at 1M baud
    ├── Command handlers: fire/laser/servo/safety
    └── Watchdog timer active
    
Phase 5: Integration Testing
    ↓ [Depends on: Phases 2, 3, 4 completed]
    ├── All 8 tests executed
    ├── Results documented
    └── Production readiness validated
```

**Critical Path**:
1. Phase 0 (blocking all others) - **2-3 hours**
2. Phase 1 (parallel start) - **3-4 hours**
3. Phase 2 (after 1) - **4-6 hours**
4. Phase 3 & 4 (after 1, parallel) - **2-3 hrs + 5-8 hrs = 7-11 hour parallel block**
5. Phase 5 (after 2, 3, 4) - **6-8 hours**

**Total Estimated Duration**: 25-40 hours of development + testing
**Recommended Spread**: 1 week (5 working days) to include debugging and iteration

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| GPIO16/GPIO17 inaccessible on board | Medium | BLOCKING | Verify pinout diagram and physical board before Phase 1 |
| Nano UART1 won't run at 1M baud | Low | High | Pre-flash Nano with `uart_init_test.ino` before Phase 1 |
| Checksum mismatch between ESP32/Nano | Medium | High | Implement checksum in Python first, test with logging enabled |
| WiFi UDP packet loss under fire load | Low | Medium | Add packet retry logic with exponential backoff in Phase 3 |
| Relay coil spike damages GPIO output | Low | High | Add 1N4148 diode protection (flyback) on relay coil before Phase 4 |
| Watchdog prevents intended prolonged fire | Low | High | Document watchdog behavior in UI, allow 500ms+ pulse commands |
| Safety interlock breaks engagement mode | Medium | Medium | Test interlock disable sequence thoroughly in Phase 5 |

---

## File Manifest

**Files to Create**:
- `DB3000_ESP32_UDP_PIR_ID3.ino` (Phase 2 - modified firmware)
- `DB3000_Nano_ID3_Accessory.ino` (Phase 4 - new Nano firmware)
- `WAVESHARE_ID3_INTEGRATION_TEST_PLAN.txt` (Phase 5)
- `WAVESHARE_ID3_TEST_RESULTS.txt` (Phase 5 outcome)

**Files to Modify**:
- `sentry_v2_comm.py` - Add `send_id3_command()` and `_build_id3_packet()` (Phase 3)
- `sentry_v2_tab.py` - Add fire mode toggle UI (Phase 3)

**Files to Reference** (Read-Only):
- `DB3000_ESP32_UDP_PIR.ino` - Source pattern for ID3 routing
- `sentry_v2_comm.py` - Existing packet building patterns
- `sentry_v2_config.py` - Configuration storage (add ID3 mode flag)

**Reference Documentation**:
- Folder: `WAVESHARE SERVO DRIVER HAT` - Board pinout and schematics (PDFs)
- File: `CHANGE_IMPACT_REFERENCE.md` - GPIO mappings already documented
- Repository Memory: `/memories/repo/sentry-v2-integration.md` - Protocol details

---

## Success Metrics

Upon completion of all phases, the system will:

✅ **Single Network Source**: PC connects to 192.168.4.2:9001 only (no dual-board UDP chaos)  
✅ **Reliable Pan/Tilt**: Servo response <100ms latency, consistently  
✅ **Responsive Fire**: ID3 fire command <50ms latency, >99.5% success rate  
✅ **Safe Operation**: Watchdog + interlock prevent runaway relay  
✅ **WiFi Stability**: Maintains connection >99% uptime, recovers from brief outages  
✅ **Extensible Architecture**: up to 254 device IDs available for future expansions  

---

## Next Steps (User Decision Gate)

**Required Before Starting Phase 0**:
1. [ ] Verify Waveshare board is physically available
2. [ ] Confirm pan/tilt servos are available and powered
3. [ ] Ensure PC can reach 192.168.4.2:9001 on same WiFi network
4. [ ] Confirm Arduino Nano available for Phase 4+

**Approval Gate**:
- [ ] User confirms ready to proceed with Phase 0
- [ ] User confirms hardware availability
- [ ] User acknowledges this is a **NO EDITING** document (planning phase only)

---

**Document Status**: ✅ READY FOR REVIEW  
**Approval Required**: YES  
**Estimated Total Effort**: 25-40 hours across all phases  
**Blocking**: Phase 0 must complete before Phase 1-5 proceed

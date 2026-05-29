# ESP32 IO Telemetry Firmware with PIR Sensor Support

## Overview
Updated ESP32 firmware that adds 3 PIR motion sensor inputs while maintaining 100% backward compatibility with existing IO/trigger control logic.

This guide describes the DB3000 ESP32 IO firmware family, not the archived Waveshare single-board bridge path.

Current live Smart Sentry app topology note:

- Current live WiFi + Debug Board app firmware: `arduino/SMART_SENTRY_ESP32_UDP_PIR/SMART_SENTRY_ESP32_UDP_PIR.ino`
- Current DB3000 USB serial IO firmware covered by this guide: `arduino/DB3000_ESP32_IO_Telemetry_PIR/DB3000_ESP32_IO_Telemetry_PIR.ino`

**Original File**: `DB3000_ESP32_IO_Telemetry_2026.ino`  
**New File**: `DB3000_ESP32_IO_Telemetry_PIR.ino`  
**Status**: Original remains unchanged; new version is fully independent

## Key Features

### ✅ Backward Compatible
- All original token-based command parsing unchanged (S, M, F, L, R, G)
- Water/Projectile trigger modes work identically
- LED, Laser, Accessory relay logic unchanged
- PIR code is completely optional via compile-time configuration

Scope note:

- the identical water/projectile statement here applies to this DB3000 ESP32 firmware contract
- archived Waveshare single-board bridge docs use a different capability surface and may intentionally leave projectile trigger-servo PWM unassigned

### ✅ PIR Integration
- 3 independent motion sensor inputs with edge detection
- Per-sensor debounce (200ms default, configurable)
- Event-driven reporting to host (JSON-like telemetry)
- Master enable/disable via `P` token
- Non-blocking polling (event-based, not interrupt-driven)

### ✅ Toggleable Feature
- Set `#define ENABLE_PIR_SUPPORT 1` to compile with PIR
- Set `#define ENABLE_PIR_SUPPORT 0` to strip all PIR code
- All original functionality works identically when disabled
- Boot messages indicate PIR status

## Pin Assignments

### Output Control (Existing)
| Pin | Function | Purpose |
|-----|----------|---------|
| GPIO 27 | PIN_TRIGGER_MOSFET | Water trigger relay (latching) |
| GPIO 13 | PIN_TRIGGER_SERVO | Projectile servo trigger (PWM) |
| GPIO 32 | PIN_LED_RELAY | Accessory LED output |
| GPIO 33 | PIN_LASER_RELAY | Laser pointer output |
| GPIO 25 | PIN_ACC_RELAY | Secondary accessory relay |

### PIR Sensor Inputs (New)
| Pin | Constant | Transport Role | Cue Ownership |
|-----|----------|----------------|---------------|
| GPIO 35 | PIN_PIR_SENSOR_0 | Sensor 0 input | App-configured cue angles |
| GPIO 34 | PIN_PIR_SENSOR_1 | Sensor 1 input | App-configured cue angles |
| GPIO 39 | PIN_PIR_SENSOR_2 | Sensor 2 input | App-configured cue angles |

**Note**: All PIR pins use active-HIGH inputs with internal GPIO pull-down (ESP32 default).

Cue-angle note:

- The firmware only reports `sensor_id` values.
- Cue pan/tilt angles live in the Smart Sentry desktop config, not in the ESP32 transport contract.
- Older docs that tied sensor ids directly to 270° / 150° / 30° should now be treated as one example mounting layout, not a fixed protocol requirement.

## Command Protocol

### Original Tokens (Unchanged)
```
F1          → Fire enabled
F0          → Fire disabled
S1          → Safety ON (all outputs disabled)
S0          → Safety OFF (armed)
M0          → Water mode (MOSFET trigger)
M1          → Projectile mode (servo pulse trigger)
L1          → LED on
L0          → LED off
R1          → Laser on
R0          → Laser off
G1          → Accessory on
G0          → Accessory off
```

### New PIR Token
```
P1          → PIR monitoring enabled
P0          → PIR monitoring disabled
```

### Packed Command Example
```
F1L1R0G0S0M1P1    → Fire + LED on, disable laser/acc, unsafe mode, projectile, enable PIR (all at once)
```

### Response Format
```
ACK S=0 M=1 F=1 L=1 R=0 G=0 P=1     → Echo back full state including new P token
```

When enabled, original formats still work:
```
ACK S=0 M=1 F=1 L=1 R=0 G=0         → (PIR disabled, no P in response)
```

## PIR Event Telemetry

### Event Report (When Motion Detected)
```
PIR_EVENT sensor_id=0 timestamp=123456789
PIR_EVENT sensor_id=1 timestamp=123456890
PIR_EVENT sensor_id=2 timestamp=123456891
```

**Note**: 
- `sensor_id` = 0, 1, or 2 (sensor index)
- `timestamp` = milliseconds since ESP32 boot
- Events only sent if `pir_enabled = 1` (P1)
- Each sensor respects 200ms debounce minimum between reports

### Periodic Status Update (Every 1 Second)
```
STAT S=0 M=1 F=0 L=0 R=0 G=0 P=1    → Full state dump with PIR status
```

## Electrical Specifications

### PIR Sensor Interface
- **Voltage**: 3.3V (ESP32 GPIO level)
- **Input Type**: Active HIGH digital signal
- **Debounce**: 200ms (firmware, not hardware)
- **Expected Sensor Output**: 
  - Idle (no motion): LOW (0V)
  - Motion detected: HIGH (3.3V)
  - Duration: Typically 1-5 seconds per detection

### Wiring Diagram
```
PIR Sensor 0 (Left-Rear)
  [GND]  ←→  GPIO 35   ←→  [+3.3V]
         (Signal)            (Common)

PIR Sensor 1 (Front-Left)
  [GND]  ←→  GPIO 34   ←→  [+3.3V]
         (Signal)            (Common)

PIR Sensor 2 (Front-Right)
  [GND]  ←→  GPIO 39   ←→  [+3.3V]
         (Signal)            (Common)
```

**Typical 3-pin PIR Module**:
- GND (black) → ESP32 GND (common ground)
- Signal (white/yellow) → GPIO 35/34/39
- VCC (red) → +3.3V ESP32 power

## Firmware Configuration

### Compile-Time Settings
In the sketch, modify line ~30:
```cpp
#define ENABLE_PIR_SUPPORT 1      // 1 = compile PIR code, 0 = strip it
```

### Runtime Settings
Via serial from host:
```
P1          → Enable PIR monitoring at runtime
P0          → Disable PIR at runtime (does not affect other functions)
P1L1F1S0    → Combined example: enable PIR, LED, fire, unsafe arm
```

## Code Architecture

### File Structure
```
DB3000_ESP32_IO_Telemetry_PIR.ino
├── Configuration Section (lines 30-60)
│   ├── ENABLE_PIR_SUPPORT define
│   ├── Pin assignments (all outputs)
│   └── Pin assignments (PIR sensors)
│
├── PIR Configuration (lines 62-75)
│   ├── Sensor pin array
│   ├── Debounce timing
│   └── State tracking arrays
│
├── Utility Functions
│   ├── clampInt()
│   ├── degToDutyTicks()
│   ├── triggerServoSet()
│   └── parseTokenInt()
│
├── applyOutputs() - Unchanged, all relay control
│
├── updatePIRSensors() - NEW: Edge detection + debounce
├── reportPIREvent() - NEW: Serial telemetry output
│
├── handleLine() - MODIFIED: Added P token parsing
│
├── setup() - MODIFIED: Added PIR pin init + boot messages
│
└── loop() - MODIFIED: Added PIR polling call
```

### PIR Polling Logic (Non-Blocking)
```cpp
updatePIRSensors()
├── Check if PIR enabled
├── For each sensor (0, 1, 2):
│   ├── Read current GPIO state (HIGH/LOW)
│   ├── Detect rising edge (LOW → HIGH)
│   ├── Check debounce timer (≥200ms since last event)
│   └── If edge + debounce OK: reportPIREvent(sensor_id, timestamp)
└── Update state tracking for next cycle
```

## Integration with Smart Sentry v2

### Python Side (sentry_v2_comm.py)
Current status:

- `sentry_v2_comm.py` already supports PIR event callbacks.
- The serial path parses `PIR_EVENT sensor_id=... timestamp=...` lines.
- The live WiFi path parses UDP JSON `pir_event` packets from `SMART_SENTRY_ESP32_UDP_PIR.ino`.
- The app can still inject a manual PIR event for bench testing, but real parser support is no longer future work.

Current live WiFi event example:
```json
{
  "v": 1,
  "t": "pir_event",
  "p": {
    "sensor_id": 0,
    "timestamp_ms": 123456789
  }
}
```

### Configuration Mapping
| Smart Sentry Setting | ESP32 Implementation |
|----------------------|---------------------|
| pir_enabled (bool) | P token (0/1) |
| sensor[0].cue_pan | Used by turret PC app only |
| sensor[0].cue_tilt | Used by turret PC app only |
| scan_grid_resolution | Used by turret PC app only |
| debounce_ms | Fixed 200ms in sketch |

**Note**: Pan/tilt look angles and scanning logic live in the **Smart Sentry v2 Python engine** (sentry_v2_engine.py), not the ESP32. The ESP32 simply detects and reports motion; the PC app decides what to do with it.

Current contract split:

- Use this DB3000 sketch when validating direct serial IO / dual-port ESP32 behavior.
- Use `SMART_SENTRY_ESP32_UDP_PIR.ino` when validating the current live WiFi + Debug Board desktop app path.

## Testing & Validation

### Test 1: Verify Original Functionality (PIR Disabled)
```
1. Flash with ENABLE_PIR_SUPPORT = 0
2. Send: F1S0M0  (fire, safe off, water mode)
3. Verify: ACK S=0 M=0 F=1 (no P token)
4. Check: Fire MOSFET energizes as expected
5. Result: Identical to original sketch
```

### Test 2: PIR Enable/Disable Toggle
```
1. Flash with ENABLE_PIR_SUPPORT = 1
2. Send: P1  (enable PIR)
3. Verify: ACK S=... M=... ... P=1
4. Wave hand in front of GPIO 35 (sensor 0)
5. Should see: PIR_EVENT sensor_id=0 timestamp=...
6. Send: P0  (disable PIR)
7. Wave hand again
8. Should NOT see PIR_EVENT
```

### Test 3: Debounce Validation
```
1. Enable PIR (P1)
2. Trigger sensor 0 with rapid motions (< 200ms apart)
3. Should only see one PIR_EVENT per 200ms interval
4. Verify: Events spaced ≥200ms apart in logs
```

### Test 4: Multi-Sensor Independence
```
1. Enable PIR (P1)
2. Trigger sensor 0 → should see PIR_EVENT sensor_id=0
3. Trigger sensor 1 → should see PIR_EVENT sensor_id=1
4. Trigger sensor 2 → should see PIR_EVENT sensor_id=2
5. Simultaneous triggers: might see 1-3 events interleaved
```

## Build Instructions

### Arduino IDE
1. Open `DB3000_ESP32_IO_Telemetry_PIR.ino`
2. Select Board: **ESP32 Dev Module**
3. Set Baud: **115200**
4. Modify line 30 if needed:
   - `#define ENABLE_PIR_SUPPORT 1` (to include PIR)
   - `#define ENABLE_PIR_SUPPORT 0` (to exclude PIR, smaller binary)
5. **Sketch → Upload**
6. Open Serial Monitor (115200 baud, line feed)
7. Should see: `[BOOT] DB3000_ESP32_IO_Telemetry_PIR ready`

### PlatformIO
```ini
[env:esp32doit-devkit-v1]
platform = espressif32
board = esp32doit-devkit-v1
framework = arduino
build_flags = -DENABLE_PIR_SUPPORT=1
```

## Migration Path

### Option 1: Drop-in Replacement (Easiest)
1. Backup original: `DB3000_ESP32_IO_Telemetry_2026.ino`
2. Flash new: `DB3000_ESP32_IO_Telemetry_PIR.ino` (keep PIR disabled by default)
3. All original tokens work identically
4. Enable PIR later when ready: P1

### Option 2: Parallel Deployment
1. Keep original board with `DB3000_ESP32_IO_Telemetry_2026.ino`
2. Flash new board with `DB3000_ESP32_IO_Telemetry_PIR.ino` with `ENABLE_PIR_SUPPORT=0`
3. Gradually migrate to new firmware as PIR support matures

### Option 3: Gradual Integration
1. Flash new firmware with PIR disabled
2. Run all original tests to verify baseline
3. Enable PIR in software: P1
4. Test PIR in controlled environment
5. Final integration: enable hardware detection in Smart Sentry v2 UI

## Known Limitations

- **Max 3 PIR Sensors**: Hardcoded for physical layout (can extend to 5+ with more GPIO)
- **No Real-Time Sensor State**: Only reports on motion (rising edge), not continuous state
- **Fixed 200ms Debounce**: Hardcoded in sketch, change at line ~72 if needed
- **No Interrupt Mode**: Uses polling in loop (non-blocking but slightly delayed)
- **No Hysteresis**: Simple edge detection, no noise filtering

## Future Enhancements

- [ ] Configurable debounce via P token with parameter: `P1D300` (enable, 300ms debounce)
- [ ] Real-time sensor state query: `P?` → Response: `STAT_PIR 0=0 1=1 2=0` (which sensors active now)
- [ ] Per-sensor enable/disable: `P0_0` (disable sensor 0) vs `P1_2` (enable sensor 2)
- [ ] Signal strength reporting: `PIR_EVENT sensor_id=0 strength=85 timestamp=...`
- [ ] Interrupt-driven mode for lower latency
- [ ] Support for more than 3 sensors (limited GPU availability)

## Troubleshooting

### PIR Events Not Appearing
1. Check: Is firmware compiled with `ENABLE_PIR_SUPPORT=1`?
2. Check: Is platform telemetry listening for `PIR_EVENT` lines?
3. Check: Is Serial Monitor showing `PIR support enabled` at boot?
4. Check: Did you send `P1` to enable PIR monitoring?
5. Verify: GPIO pins 35/34/39 are physically connected to PIR sensors

### Events Too Frequent
- Adjust debounce timer: Change line ~72 from `200` to `500` (milliseconds)
- Verify: PIR sensor not stuck HIGH (hardware issue)
- Verify: No electromagnetic interference if sensors are near power traces

### Events With PIR Disabled
- Safety check: Verify `P0` was recognized in ACK response
- Verify: Firmware actually compiled with PIR code (check boot message)

### Backward Compatibility Issues
- Set `ENABLE_PIR_SUPPORT 0` and rebuild if old code is sensitive to `P` token
- Verify all other tokens (S/M/F/L/R/G) work as before
- Check ACK responses don't include `P=` field when PIR disabled

## Firmware Files

| File | Purpose | Status |
|------|---------|--------|
| `DB3000_ESP32_IO_Telemetry_2026.ino` | Original (no PIR) | Kept as-is |
| `DB3000_ESP32_IO_Telemetry_PIR.ino` | New (PIR support) | New feature branch |
| Directory | `arduino/DB3000_ESP32_IO_Telemetry_2026/` | Original sketch folder |
| Directory | `arduino/DB3000_ESP32_IO_Telemetry_PIR/` | New sketch folder |

---

**Last Updated**: April 2026  
**Compile Status**: ✓ Verified (Arduino IDE 2.x + ESP32-IDF 2.0.x+)  
**Test Status**: ✓ Ready for hardware validation  
**Integration**: ✓ Serial `PIR_EVENT` and live WiFi `pir_event` paths are documented and supported in `sentry_v2_comm.py`

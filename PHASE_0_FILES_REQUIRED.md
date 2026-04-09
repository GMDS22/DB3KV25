# Phase 0 Testing - File Requirements Checklist

**Objective**: Historical Waveshare ESP32 + Pan/Tilt Servo bench checklist

> Status note (2026-04-09): this checklist is historical only. The Waveshare single-board attempt is on hold and is not part of the current Smart Sentry app. For live app work, use the ESP32 WiFi + Debug Board USB path with `arduino/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR.ino` and treat this file as archive material only.

---

## Essential Files - Already Exist ✅

### 1. ESP32 Firmware
**File**: [arduino/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE.ino](arduino/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE/SMART_SENTRY_V3_0_WAVESHARE_UDP_BUS_BRIDGE.ino)
- **Purpose**: Archived Waveshare V3 single-board bridge firmware
- **Status**: On hold, not current app firmware
- **Key Features**:
  - WiFi AP mode (192.168.4.1 SSID: "SMART-SENTRY-V3")
  - UDP server on port 9000
  - JSON+CRC32 packet parsing
  - Pan/Tilt servo control (ID1/ID2)
  - Bus UART on GPIO18/GPIO19 at 1000000 baud
  - Hardware arm switch reporting on GPIO21 / header 40
  - Direct trigger MOSFET, accessory relay, spare relay, and buzzer support
  - Optional outputs left explicitly unassigned
  - Boot diagnostics printed to serial (115,200 baud)
- **Phase 0 Role**: Flash this to Waveshare board; verify boot messages and bridge replies

---

### 2. PC Application (Python GUI)
**File**: [run.py](run.py)
- **Entry point**: Launches Smart Sentry v2 application
- **Purpose**: Launch the current Smart Sentry app, which now targets the ESP32 WiFi + Debug Board USB path rather than the archived Waveshare bridge path
- **Startup**: `python run.py` (from DB3000V4.1-main directory)
- **Phase 0 Role**: Use this to send pan/tilt commands to Waveshare

---

### 3. Smart Sentry v2 Communication Module
**File**: [app/sentry_v2/sentry_v2_comm.py](app/sentry_v2/sentry_v2_comm.py)
- **Purpose**: Handles all WiFi UDP communication with ESP32
- **Key Classes**: `SentryV2Comm` (singleton pattern)
- **Methods Used in Phase 0**:
  - `connect()` - Establish UDP connection to 192.168.4.1:9000
  - `send_servo_command(pan, tilt, time)` - Send pan/tilt position (in degrees 0-180)
  - Supports "WiFi Full" mode (MODE_WIFI_FULL = 3)
- **Phase 0 Role**: Already handles UDP packet building; will use existing methods

---

### 4. Smart Sentry v2 Configuration
**File**: [app/sentry_v2/sentry_v2_config.py](app/sentry_v2/sentry_v2_config.py)
- **Purpose**: Configuration storage and defaults
- **Saved Location**: `app/config/sentry_v2_settings.json`
- **Key Settings for Phase 0**:
  - `connection_type: int` - Set to 3 (MODE_WIFI_FULL)
  - `udp_host: str` - Should be "192.168.4.1"
  - `udp_port: int` - Should be 9000
  - `pan_servo_id: int` - Should be 1 (default)
  - `tilt_servo_id: int` - Should be 2 (default)
- **Phase 0 Role**: Configure connection before testing

---

### 5. Serial Monitor Script
**File**: [read_serial.py](read_serial.py)
- **Purpose**: Real-time serial output from ESP32 (USB debugging)
- **Usage**: `python read_serial.py` (auto-detects COM port)
- **Phase 0 Role**: 
  - Monitor boot messages (confirm UART2 init)
  - Watch for WiFi connection status
  - Capture any error messages during servo control
- **Output To Capture**:
  - `[BOOT] DB3000_ESP32_UDP_PIR  v1`
  - `[BOOT] ap=OK ip=192.168.4.1`
  - `[BOOT] bus uart baud=1000000 rx=18 tx=19`
  - `[BOOT] switch input gpio=21 active_low=1 state=...`
  - `[BOOT] UDP port 9000 ready`

---

### 6. Arduino CLI Tool
**Location**: [tools/arduino-cli/arduino-cli.exe](tools/arduino-cli/)
- **Purpose**: Command-line tool to flash firmware to ESP32
- **Phase 0 Usage**:
  ```bash
  tools\arduino-cli\arduino-cli.exe upload -p COM31 --fqbn esp32:esp32:esp32 arduino\SMART_SENTRY_V2_0_ESP32_UDP_PIR\SMART_SENTRY_V2_0_ESP32_UDP_PIR.ino
  ```
- **Note**: Replace `COM31` with actual COM port of Waveshare board

---

### 7. Smart Sentry v2 UI Tab
**File**: [app/sentry_v2/sentry_v2_tab.py](app/sentry_v2/sentry_v2_tab.py)
- **Purpose**: Main UI for turret control (4000+ lines)
- **Phase 0 Sections Used**:
  - **Connection Tab**: Mode selection dropdown (set to "WiFi Full")
  - **Servo Control Panel**: Manual pan/tilt sliders or direct degree input
  - **Fire Button**: For GPIO25 relay test (optional)
  - **Diagnostics Panel**: Connection status indicator
- **Key Line References**:
    - Full WiFi mode now shows the Waveshare bridge bus path on GPIO18/GPIO19
    - The Waveshare pin assignment help now reflects the active hardware switch and unassigned optional outputs
- **Phase 0 Role**: Primary interface for sending pan/tilt commands

---

## Helper/Test Scripts - Optional but Recommended ✓

### 8. Servo Bus Test Script
**File**: [test_bus_servo_read.py](test_bus_servo_read.py)
- **Purpose**: Direct servo bus command testing (useful for debugging)
- **Usage**: `python test_bus_servo_read.py COM9` (or actual port)
- **Phase 0 Optional Use**: If UDP testing shows servo non-response, use this to verify servos are electrically OK
- **Status**: Standalone (doesn't require GUI)

---

### 9. Simple Servo Test
**File**: [simple_servo_test.py](simple_servo_test.py)
- **Purpose**: Direct servo position test via serial
- **Usage**: `python simple_servo_test.py`
- **Phase 0 Optional Use**: Quick servo validation before WiFi testing
- **Status**: Standalone

---

### 10. Latency Measurement Tool
**File**: [tools/run_detection_mode_sweep.py](tools/run_detection_mode_sweep.py)
- **Purpose**: Automated latency measurement for detection modes
- **Phase 0 Relevance**: Can be adapted to measure command→servo latency
- **Status**: May need customization for Phase 0 servo test
- **Key Measurement**: P95 latency target <100ms

---

## Configuration Files - Auto-Created on First Run

### 11. Smart Sentry v2 Settings
**File**: `app/config/sentry_v2_settings.json` (auto-created)
- **Purpose**: Persistent configuration storage
- **Will Be Created**: Automatically on first `run.py` launch
- **Important for Phase 0**:
  ```json
  {
    "connection_type": 3,
    "udp_host": "192.168.4.1",
    "udp_port": 9000,
    "pan_servo_id": 1,
    "tilt_servo_id": 2,
    "bus_servo_time_ms": 55
  }
  ```
- **Location**: `app/config/` (created automatically on first launch)

---

## Files to Capture as Artifacts

### 12. Phase 0 Boot Log
**File**: `PHASE_0_BOOT_LOG.txt` (to create during testing)
- **Purpose**: Capture ESP32 boot messages for validation
- **How to Capture**:
  1. Open `read_serial.py` in terminal
  2. Power ESP32 and let it boot
  3. Copy all output to `PHASE_0_BOOT_LOG.txt`
- **Expected Content**:
  ```
  [BOOT] ap=OK ip=192.168.4.1
  [BOOT] bus uart baud=1000000 rx=18 tx=19
  [BOOT] switch input gpio=21 active_low=1 state=...
  [BOOT] udp port=9000
  ```

---

### 13. Phase 0 Test Results
**File**: `PHASE_0_TEST_RESULTS.txt` (to create after testing)
- **Purpose**: Document test execution and outcomes
- **To Include**:
  - Date/time of test
  - Waveshare board model and revision
  - ESP32 port & baud rate settings
  - WiFi SSID/IP confirmation
  - Pan servo ID1 response test (✓ or ✗)
  - Tilt servo ID2 response test (✓ or ✗)
  - Latency measurements (min/avg/max)
  - Any errors or anomalies
  - 30-minute soak test result
  - Conclusion: PASS / FAIL

---

## Environment Setup - Before Phase 0

### Required Python Environment
- **Location**: `.venv` (virtual environment)
- **Activation**: 
  ```powershell
  & "f:\DB3000V5.0 - ESP32\.venv\Scripts\Activate.ps1"
  ```
- **Verify Installation**:
  ```bash
  pip list | findstr pyserial opencv-python PyQt5
  ```

---

### Required System Setup
1. **Arduino IDE** (optional, arduino-cli used instead)
2. **CH340 Driver** (for USB serial on Waveshare)
   - If `read_serial.py` fails to find COM port, install from: https://sparks.gogo.co.nz/ch340.html
3. **Python 3.8+**
4. **PySerial** (for serial communication)

---

## Summary Table - Phase 0 Files

| Category | File | Status | Phase 0 Role |
|----------|------|--------|-------------|
| **Firmware** | `arduino/SMART_SENTRY_V2_0_ESP32_UDP_PIR/SMART_SENTRY_V2_0_ESP32_UDP_PIR.ino` | ✅ Exists | Flash to Waveshare |
| **GUI** | `run.py` | ✅ Exists | Launch application |
| **Comm** | `app/sentry_v2/sentry_v2_comm.py` | ✅ Exists | Send pan/tilt commands |
| **Config** | `app/sentry_v2/sentry_v2_config.py` | ✅ Exists | Manage settings |
| **Config** | `app/config/sentry_v2_settings.json` | 🔄 Auto-created | Store connection params |
| **Monitor** | `read_serial.py` | ✅ Exists | Capture boot logs |
| **UI** | `app/sentry_v2/sentry_v2_tab.py` | ✅ Exists | Control pan/tilt |
| **Tool** | `tools/arduino-cli/arduino-cli.exe` | ✅ Exists | Flash firmware |
| **Test** | `test_bus_servo_read.py` | ✅ Exists | Optional: Debug servos |
| **Test** | `simple_servo_test.py` | ✅ Exists | Optional: Quick servo test |
| **Artifact** | `PHASE_0_BOOT_LOG.txt` | 📝 To Create | Capture boot diagnostics |
| **Artifact** | `PHASE_0_TEST_RESULTS.txt` | 📝 To Create | Document test outcomes |

---

## Quick Action Checklist for Phase 0

### Pre-Test Setup
- [ ] Waveshare ESP32 board available
- [ ] Pan/Tilt servos available (ID1=pan, ID2=tilt)
- [ ] USB cable for Waveshare (power + serial communication)
- [ ] Servo power supply (9-12V recommended)
- [ ] Python virtual environment activated (`.venv`)
- [ ] PySerial installed (`pip install pyserial`)

### Execution Steps
1. [ ] Identify ESP32 COM port (Device Manager or `python -m serial.tools.list_ports`)
2. [ ] Flash firmware: `arduino-cli upload -p COMXX --fqbn esp32:esp32:esp32 arduino\SMART_SENTRY_V2_0_ESP32_UDP_PIR\SMART_SENTRY_V2_0_ESP32_UDP_PIR.ino`
3. [ ] Monitor boot messages: `python read_serial.py` (verify UART2 message appears)
4. [ ] Connect PC to WiFi "DB3000-Turret" or ensure network routing works
5. [ ] Launch application: `python run.py`
6. [ ] Set connection mode to "WiFi Full" (mode 3)
7. [ ] Send pan command: 0° (home), 45°, 90° (verify servo response)
8. [ ] Send tilt command: 0° (home), 45°, 90° (verify servo response)
9. [ ] Measure latency: Record time from button press to servo movement start
10. [ ] Run 30-minute soak test: Continuous pan/tilt commands with timing
11. [ ] Document results in `PHASE_0_TEST_RESULTS.txt`
12. [ ] Archive boot log as `PHASE_0_BOOT_LOG.txt`

### Success Criteria
- [ ] ESP32 boots and prints UART2 message
- [ ] WiFi connects and responds to UDP packets
- [ ] Pan servo (ID1) responds to pan commands
- [ ] Tilt servo (ID2) responds to tilt commands
- [ ] Latency <100ms (average)
- [ ] 30-minute run with no hangups or servo lock
- [ ] All results documented

---

## Troubleshooting Guide

| Problem | Symptoms | Recovery |
|---------|----------|----------|
| Board won't flash | `arduino-cli: connection failed` | Check USB cable, COM port, drivers (CH340) |
| No WiFi connection | Boot hangs at "WiFi init", SSID not visible | Restart router, verify firmware has WiFi enabled |
| Servos unresponsive | Motors silent, no movement | Check servo power (9-12V), verify power connector |
| Packet timeout | PC app shows "ESP32 not responding" | Check firewall, verify UDP port 9000 open |
| Boot log not visible | `read_serial.py` can't open port | Install CH340 driver, verify correct COM port |
| Servo jitter | Servo oscillates ±10°, won't settle | Check power supply ripple, reduce bus servo time |
| Latency spikes | varies from 20ms to 500ms | WiFi interference, reduce YOLO detection workload |

---

## Next Actions (After Phase 0)

**If Phase 0 Passes → Proceed to Phase 1** (Hardware Verification)
- Verify the local bus-servo path on GPIO18/GPIO19
- Plan Nano wiring

**If Phase 0 Fails → Debug Before Proceeding**
- Capture detailed bus traces with `test_bus_servo_read.py`
- Verify servo wiring and power
- Check ESP32 EEPROM if servo IDs corrupt

---

**Document Status**: REFERENCE FOR PHASE 0 TESTING  
**Created**: March 29, 2026  
**Ready For Review**: YES  
**No Code Changes Required**: YES (all files pre-existing)

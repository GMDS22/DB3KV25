# Smart Sentry Trigger Setup & Auto-Fire Guide

**Last Updated:** May 2026  
**Version:** v3.5.2+

---

## Overview

Smart Sentry supports two independent trigger mechanisms:

1. **Water/MOSFET Mode** (M0) — Pulse-train solenoid/relay fire control
2. **Projectile/Servo Mode** (M1) — Electronic servo-based trigger linkage

Both modes support **automatic firing** when engagement constraints are met, controlled by the **Auto-Trigger toggle** in the Settings tab.

---

## Trigger Mode Selection

### Quick Switch
- Settings Tab → "Trigger Mode:" dropdown
  - "Water (MOSFET)" = M0 solenoid/relay path
  - "Projectile (GPIO13 Servo)" = M1 servo pulse path

The UI automatically shows/hides settings panels based on the selected mode.

### Fire Output Pins

| Hardware | Mode | Output Pin | Control | Default State |
|----------|------|-----------|---------|----------------|
| ESP32 DB3000 | Water (M0) | GPIO 27 | Digital ON/OFF | LOW (safe) |
| ESP32 DB3000 | Projectile (M1) | GPIO 13 | PWM pulse | REST position |
| Arduino Nano | Water (M0) | D8 | Digital ON/OFF | LOW (safe) |
| Arduino Nano | Projectile (M1) | D9 | PWM servo | REST position |

---

## Mode 0: Water / MOSFET Configuration

### Settings Panel: "Water / MOSFET Trigger"

| Setting | Range | Default | Description |
|---------|-------|---------|-------------|
| **Pulse ON (ms)** | 10–2000 | 120 | Duration each MOSFET ON pulse stays active |
| **Cycles per fire** | 1–20 | 1 | Number of ON/OFF pulse pairs in one fire request |
| **Cycle OFF (ms)** | 10–2000 | 50 | Gap between consecutive pulses |
| **Output Polarity** | Checkbox | OFF | Activates for active-LOW relay modules |

### Pulse Train Calculation

When you request one fire in Water mode, the firmware executes:
```
Total ON time  = Pulse ON × Cycles per fire
Total OFF time = Cycle OFF × (Cycles - 1)
Total duration = Total ON + Total OFF
```

**Example:** Pulse=120ms, Cycles=2, OFF=50ms
```
ON:  120 ms  (pulse 1)
OFF:  50 ms  (gap)
ON:  120 ms  (pulse 2)
---
Total: 290 ms
```

### Hardware Requirements

- **MOSFET Driver or Relay Module** on GPIO 27 (ESP32) or D8 (Nano)
- **Solenoid/pump load** wired to the relay/driver output
- **Active-LOW output polarity** checkbox: Check ONLY if using a latching relay module (most common)
- **Active-HIGH output polarity** (default): Use for direct MOSFET gate drivers

### Configuration Tips

- **Short pulses** (50–120 ms) suit quick solenoid clicks or servo trigger presses
- **Multi-cycle fire** (Cycles > 1) simulates burst behavior: fire, pause, fire again
- **Relay modules** often require active-LOW; MOSFET drivers typically active-HIGH
- **Total duration** should not exceed ~500 ms (firmware safety limit: 2 sec per cycle)

---

## Mode 1: Projectile / Servo Configuration

### Settings Panel: "Projectile Trigger Servo"

| Setting | Range | Default | Description |
|---------|-------|---------|-------------|
| **Rest angle** | 0–180° | 0° | Idle/safe servo position (no trigger pull) |
| **Fire angle** | 0–180° | 45° | Engaged servo position (trigger pulled) |
| **Speed (deg/s)** | 10–5000 | 360 | Servo travel speed |

### Fire Sequence

One fire request causes:
1. Servo moves from **Rest angle** to **Fire angle** at **Speed**
2. Holds fire position for ~40 ms (firmware minimum latch)
3. Auto-returns to **Rest angle**

### Calculation: Estimated Move Time

```
Travel degrees = |Fire angle - Rest angle|
Estimated ms   = (Travel degrees / Speed) × 1000 + 40 ms hold
```

**Example:** Rest=0°, Fire=45°, Speed=360°/s
```
Travel: 45°
Time:   (45 / 360) × 1000 + 40 = 165 ms
```

### Hardware Requirements

- **RC Servo or PWM-controlled valve solenoid** on GPIO 13 (ESP32) or D9 (Nano)
- **Mechanical linkage** connecting servo to trigger (lever, rod, or direct pull)
- **Servo connector:** PWM signal line (typically yellow/white) to GPIO pin
- **Power:** Servo supply *separate* from microcontroller (5V recommended)

### Configuration Tips

- **Rest angle** should be safe (no accidental fire)
- **Fire angle** should fully depress trigger but not strain servo
- **Speed** affects response time: 360°/s is moderate; higher speeds may jam linkage
- **Travel > 10°** is typical for mechanical reliability
- **Speed < 100°/s** may cause slow trigger response; **> 1000°/s** risks missed timing

---

## Auto-Trigger (Auto-Fire) Workflow

### Enable Auto-Trigger

1. Open **Settings Tab**
2. Locate **"Auto-Trigger"** checkbox (prominent near top of Engagement section)
3. **Check the box** to enable automatic firing when aim constraints are met
4. Log message: `Auto-trigger: ON`

### Prerequisites for Auto-Fire

For any single fire to happen, *all* of these must be true:

| Condition | Check Point | How to Fix |
|-----------|-------------|-----------|
| Auto-Trigger enabled | Settings → "Auto-Trigger" checkbox = ✓ | Enable if disabled |
| Safety armed | Connection Tab → Safety toggle = "ARMED" | Click safety toggle to arm |
| Hardware connected | Connection Tab → Connection status = green/connected | Connect hardware |
| Aim lock achieved | Video overlay → reticle color = RED (not yellow) | Hold steady aim for configured frames |
| Fire centering met | Error within fire tolerance (typically ±0.35° pan, ±0.28° tilt) | Tighten aim on target |
| Hold time satisfied | Maintain centered aim for fire_trigger_hold_time (typically 0.1 s) | Keep aim steady for 100 ms |
| No fire mask active | No-fire zones not blocking turret position | Reposition turret outside no-fire zone |
| No runtime fault | Connection Tab → Runtime status shows no fault | Restart hardware if fault persists |

### Manual Test Procedure

1. **Enable safety**: Safety toggle = ON (armed)
2. **Enable auto-trigger**: Auto-Trigger checkbox = ✓
3. **Detect a target**: Point camera at person/object YOLO can detect
4. **Watch overlay**: Reticle should turn RED (indicates lock) after brief aim lock (3+ frames @ ~30 fps ≈ 100 ms)
5. **Observe output**: Hardware should fire after hold time (typically 100–200 ms)

### If Auto-Fire Doesn't Happen

Check these in order:

1. **Check app log window:**
   ```
   "Auto-Trigger: ON"  → Enabled? ✓
   "AUTO-FIRE: Queuing fire burst ..."  → Trying to fire? ✓
   "AUTO-FIRE BLOCKED: ..." → Why blocked?
   ```

2. **Verify Safety:**
   - Connection Tab → Safety toggle must show "ARMED"
   - If showing "SAFE", click toggle to arm

3. **Verify Hardware Connection:**
   - Connection Tab → Should show connected state (green indicator)
   - Check COM port and baud rate (typically 115200)

4. **Verify Auto-Trigger Config:**
   - Settings Tab → Auto-Trigger checkbox should be ✓
   - Check fire_trigger_hold_time, fire_trigger_enter_pan_tolerance, fire_trigger_enter_tilt_tolerance

5. **Check Aim Lock:**
   - Video overlay → Reticle should turn RED when locked
   - If yellow: aim lock not yet achieved (needs more stable frames)

6. **Test Manual Fire:**
   - Connection Tab → Manual Fire button should work (test hardware connectivity)
   - If Manual Fire works but Auto-Fire doesn't: issue is in aim lock or centering logic

7. **Review Logs:**
   - Look for "AUTO-FIRE BLOCKED:" messages with reason
   - Common reasons:
     - `auto_trigger_enabled is FALSE` → Enable in Settings
     - `Safety is not armed` → Click safety toggle
     - `Hardware link disconnected` → Check connection
     - `Runtime safety is LOCKED` → Hardware safety switch active
     - `Runtime fault` → Hardware error code; restart/check voltage

---

## Trigger Settings Propagation

### How Settings Reach Hardware

1. **UI Change** → User modifies Pulse ON, Fire angle, etc. in Settings Tab
2. **Config Update** → App stores new values in `engagement` config object
3. **Comm Sync** → App queues `send_trigger_runtime_config()` if hardware is connected
4. **Serial/UDP** → App sends J, K, N, X, U, V, H, B tokens to firmware
5. **Firmware Parse** → Hardware updates internal trigger config variables
6. **Next Fire** → Hardware uses new settings on next fire request

### Command Tokens (Nano USB & ESP32 Routes)

| Token | Field | Example | Max |
|-------|-------|---------|-----|
| J | Pulse ON (ms) | J120 | 2000 |
| K | Cycle count | K2 | 20 |
| N | Cycle OFF (ms) | N50 | 2000 |
| X | Active-LOW polarity | X0 (HIGH) or X1 (LOW) | 1 |
| U | Servo rest deg | U0 | 180 |
| V | Servo fire deg | V45 | 180 |
| H | Servo speed dps | H360 | 5000 |
| B | PIR blink enable | B1 | 1 |

### Verifying Settings Reached Hardware

**On Nano (Serial Monitor):**
```
[RX] S0F1L1 ...
[TX] ACK S=0 M=0 F=1 ... J=120 K=1 N=50 U=0 V=45 H=360 ...
```

**On ESP32 (UDP State Packet):**
```json
{
  "trigger_mosfet_pulse_ms": 120,
  "trigger_mosfet_cycle_count": 1,
  "trigger_mosfet_cycle_off_ms": 50,
  "trigger_servo_rest_deg": 0,
  "trigger_servo_fire_deg": 45,
  "trigger_servo_speed_dps": 360
}
```

If values don't match UI settings → settings not propagated; check connection status.

---

## Troubleshooting Checklist

### Symptom: "Auto-Trigger" checkbox grayed out
- **Cause:** Feature not supported in this firmware build
- **Fix:** Update firmware to latest version (v3.5.0+)

### Symptom: Auto-Trigger enabled but no fire happens
- **Check #1:** Is safety armed? (Connection Tab)
- **Check #2:** Is hardware connected? (green indicator)
- **Check #3:** Do logs show "AUTO-FIRE BLOCKED:" ? (app log window)
- **Check #4:** Can you fire manually? (Manual Fire button in Connection Tab)
- **Check #5:** Does reticle turn RED? (Video overlay; RED=locked, YELLOW=searching)

### Symptom: Manual fire works, auto-fire doesn't
- **Cause:** Aim lock or centering requirements not met
- **Fix:** Keep aim steady on target for 3+ frames (~100 ms); ensure error < fire_trigger_enter tolerance
- **Verify:** Reticle should turn RED before fire triggers

### Symptom: Settings changed in UI but hardware doesn't execute
- **Check:** Is "send_trigger_runtime_config()" being queued? (app log)
- **Fix:** 
  - Verify hardware is connected (not host-control mode)
  - Wait for state packet from hardware confirming new settings
  - Try clicking Manual Fire to verify connection is live

### Symptom: Fire triggers randomly or too often
- **Check:** fire_trigger_hold_time is too short (default 0.1 s)
- **Fix:** Increase hold_time in config to 0.2+ seconds to require longer centering
- **Also check:** aim_lock_required_frames should be ≥ 3 (at 30 fps = 100+ ms)

### Symptom: Servo doesn't return to rest after fire
- **Cause:** Servo speed too slow or travel angle too large
- **Fix:** Increase Speed (deg/s) or verify servo power supply voltage
- **Note:** Firmware auto-returns after ~40 ms hold; if servo still moving, increase speed

### Symptom: MOSFET fires continuously
- **Cause:** Output polarity inverted (active-LOW checkbox wrong)
- **Fix:** Toggle "Active-LOW relay" checkbox; re-test
- **Note:** 
  - Check unchecked = Active-HIGH (MOSFET drivers)
  - Check checked = Active-LOW (relay modules)

---

## Advanced: Fine-Tuning Auto-Fire Responsiveness

### Aim Lock Behavior

| Parameter | Looser (Faster Fire) | Tighter (More Deliberate) | Notes |
|-----------|----------------------|--------------------------|-------|
| `aim_lock_required_frames` | 2 | 5 | Frames needed before lock achieved |
| `fire_trigger_hold_time` | 0.05 s | 0.20 s | Time aim must stay centered |
| `fire_trigger_enter_*_tolerance` | ±1.0° | ±0.2° | How far off-center before lock breaks |

### Trade-Offs

- **Faster (loose settings):** Fire quickly but risk misses or false targets
- **Slower (tight settings):** Precise but delayed fire when tracking fast targets

### Recommended Presets

**"Rapid"** (fast-moving targets):
```
aim_lock_required_frames: 2
fire_trigger_hold_time: 0.05
fire_trigger_enter_pan_tolerance: 0.65
fire_trigger_enter_tilt_tolerance: 0.55
```

**"Standard"** (default, balanced):
```
aim_lock_required_frames: 3
fire_trigger_hold_time: 0.10
fire_trigger_enter_pan_tolerance: 0.35
fire_trigger_enter_tilt_tolerance: 0.28
```

**"Precise"** (stationary targets):
```
aim_lock_required_frames: 5
fire_trigger_hold_time: 0.20
fire_trigger_enter_pan_tolerance: 0.20
fire_trigger_enter_tilt_tolerance: 0.15
```

---

## Summary

| Concept | Key Point |
|---------|-----------|
| **Trigger Modes** | Water (MOSFET) or Projectile (Servo) — choose one |
| **Fire Output** | Configured per mode in Settings → configure both modes even if using one |
| **Auto-Trigger** | Master gate: must be ✓ and settings must be configured for any auto-fire |
| **Prerequisites** | Safety armed + Hardware connected + Aim lock (RED reticle) + Centered within tolerance + Hold time met |
| **Propagation** | UI → Config → Comm queue → Serial/UDP tokens → Firmware → Hardware |
| **Testing** | Enable Auto-Trigger → Point at target → Watch reticle turn RED → Fire should happen within 100–300 ms |
| **Troubleshooting** | Check app logs for "AUTO-FIRE BLOCKED:" messages and follow hints |

---

## Firmware Compatibility

| Firmware | Mode 0 | Mode 1 | Auto-Fire | Notes |
|----------|--------|--------|-----------|-------|
| `SMART_SENTRY_ESP32_UDP_PIR` | ✓ | ✓ | ✓ | Current WiFi baseline |
| `SMART_SENTRY_V2_3_1_ESP32_UDP_PIR` | ✓ | ✓ | ✓ | Stable ESP32 USB route |
| `SMART_SENTRY_V3_0_NANO_USB_IO_PIR` | ✓ | ✓ | ✓ | Nano serial IO path |
| `DB3000_ESP32_IO_Telemetry_PIR` | ✓ | ✓ | ✓ | Direct ESP32 IO board |

All current firmware versions support both trigger modes and auto-fire logic.

---

## Contact & Support

- **Issue with auto-fire:** Check app log (Settings Tab → View Log) for "AUTO-FIRE" diagnostic messages
- **Firmware questions:** Verify installed sketch via serial monitor boot message
- **Hardware verification:** Use Connection Tab → Manual Fire to test connectivity before enabling Auto-Trigger

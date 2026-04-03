# ESP32 Pin Quick Reference - Smart Sentry ESP32 WiFi / PIR Baseline

## ESP32 GPIO Pin Map

```
ESP32 Development Board
┌─────────────────────────────────────────┐
│                                         │
│  GND   3V3   EN             TX0   RX0  │
│   │     │    │              │     │   │
│   0     ●     ●              2  ●  ●  │ ← UART0 (USB serial)
│   │            │                       │
│  GND   3V3   ADC           GPIO      USB
│   └─────────────┘           ↓
│                                         │
│  ┌─ UART2 Debug Board ────────────────┐ │
│  │ GPIO 16 (RX) → COM9 Debug Board    │ │
│  │ GPIO 17 (TX) → COM9 Debug Board    │ │
│  └────────────────────────────────────┘ │
│                                         │
└─────────────────────────────────────────┘
```

## Pinout Table

### Power & Ground
| Pin | Function | Notes |
|-----|----------|-------|
| GND | Ground | Common return for all circuits |
| 3V3 | +3.3V Supply | For PIR sensors, LED logic |
| 5V (if available) | +5V Supply | Not used in this design |

### Output Control (Relay/PWM)
| GPIO | Name | Function | Connector |
|------|------|----------|-----------|
| 27 | PIN_TRIGGER_MOSFET | Water trigger relay (latching) | Pin 27 |
| 13 | PIN_TRIGGER_SERVO | Projectile servo trigger (PWM 50Hz) | Pin 13 |
| 4 | PIN_BUZZER | Passive buzzer / tone output | Pin 4 |
| 2 | PIN_STATUS_LED | Status LED / external blink mirror | Pin 2 |
| 32 | PIN_LED_RELAY | LED on/off relay | Pin 32 |
| 33 | PIN_LASER_RELAY | Laser on/off relay | Pin 33 |
| 25 | PIN_ACC_RELAY | Accessory relay | Pin 25 |

### PIR Sensor Input (Motion Detection)
| GPIO | Name | Physical Location | Direction | Connector |
|------|------|-------------------|-----------|-----------|
| 35 | PIN_PIR_SENSOR_0 | Left-rear mount | ~270° | Pin 35 |
| 34 | PIN_PIR_SENSOR_1 | Front-left mount | ~150° | Pin 34 |
| 39 | PIN_PIR_SENSOR_2 | Front-right mount | ~30° | Pin 39 |

### Serial/Debug (Reserved)
| GPIO | Function | Purpose | Connector |
|------|----------|---------|-----------|
| 1 | TX0 | USB Serial (Host commands) | USB |
| 3 | RX0 | USB Serial (Responses) | USB |
| 16 | RX2 | Debug Board TX into ESP32 UART2 | Debug Board link |
| 17 | TX2 | ESP32 TX out to Debug Board UART2 | Debug Board link |

## Electrical Specifications

### Output Relays
```
GPIO Output Configuration:
┌─ GPIO 27/13/32/33/25 ──┐
│ (Output, Push-Pull)     │
├─────────────────────────┤
│ Low  (0V)  → OFF        │
│ High (3.3V) → ON        │
└─────────────────────────┘

External Connection Pattern:
GPIO Pin ──→ [Relay Coil / MOSFET Gate / LED] ──→ GND
     3.3V                                      COM
```

### PIR Sensor Inputs
```
PIR Sensor Wiring (3-pin module):
VCC (Red)    ──→ +3.3V ESP32 power
Signal (White/Yellow) ──→ GPIO 35/34/39
GND (Black)  ──→ GND (common with ESP32)

Signal Logic:
- No motion  → LOW  (0V)
- Motion detected → HIGH (3.3V) for 1-5 seconds
- Debounce in firmware: 200ms minimum between reports
- PIR-triggered GPIO2 blinking is firmware-configurable and can be disabled from Smart Sentry.
```

## Breadboard Layout Example

```
ESP32 Dev Board (top view):
        Left Side      Right Side
        ─────────      ──────────
    GND ●              ● 3V3
    3V3 ●              ● EN
    36  ●              ● GPIO 15
    39  ● PIR_2 ←──┐   ● GPIO 2
    34  ● PIR_1 ←──┤   ● GPIO 4
    35  ● PIR_0 ←──┤   ● GPIO 5
    32  ● LED ←────┤   ● GPIO 18
    33  ● LASER ←──┤   ● GPIO 19
    25  ● ACC ←────┤   ● GPIO 21
    26  ●         ↓    ● GPIO 22
    19  ●        (GND) ● GPIO 23
    18  ●              ● GPIO 1 (TX USB)
    17  ●              ● GPIO 3 (RX USB)
    16  ●              ● GND
    4   ●              ● GPIO 13 (SERVO)
    0   ●              ● GPIO 12
    2   ●              ● GPIO 14
    15  ●              ● GPIO 27 (MOSFET)
    13  ●              ● GPIO 26
    12  ●              ● GPIO 25
    14  ●              ● GND
    27  ● MOSFET ←─────┘
```

## Typical Connection Diagram

```
Smart Sentry v2 System Layout:

PC Running Smart Sentry
    ↓ (USB Serial / UDP WiFi)
┌─────────────────────────────┐
│   ESP32 Development Board   │
├─────────────────────────────┤
│                             │
│  Power Supply:              │
│  - GND ←─ Common Ground     │
│  - 3V3 ←─ +3.3V from USB   │
│                             │
│  Outputs:                   │
│  - GPIO 2  → [LED] Status   │
│  - GPIO 27 → [MOSFET] Water │
│  - GPIO 13 → [PWM] Servo    │
│  - GPIO 32 → [Relay] LED    │
│  - GPIO 33 → [Relay] Laser  │
│  - GPIO 25 → [Relay] Acc    │
│                             │
│  Inputs (PIR):              │
│  - GPIO 35 ← [Sensor 0]     │
│  - GPIO 34 ← [Sensor 1]     │
│  - GPIO 39 ← [Sensor 2]     │
│                             │
└─────────────────────────────┘
      ↓        ↓              ↓
    [GND]   [3.3V]       [Relays]
      ↓        ↓              ↓
    ●────●────────────●────────●
   GND  
   Bus

PIR Sensors (x3):
┌─────────────┐
│ VCC - 3.3V  │
│ SIG - GPIO  │ ← Active HIGH motion detection
│ GND - GND   │
└─────────────┘
```

## Connector Location Reference

### ESP32 Dev Board Pin Groups

**Left Column** (top to bottom):
```
GND, 3V3, 36, 39, 34, 35, 32, 33, 25, 26, 19, 18, 17, 16, 4, 0, 2, 15, 13, 12, 14, 27
```

**Right Column** (top to bottom):
```
3V3, EN, 15, 2, 4, 5, 18, 19, 21, 22, 23, 1, 3, GND, 12, 14, 26, 25
```

## Firmware Configuration Checklist

- Current WiFi baseline sketch: `arduino/SMART_SENTRY_V2_0_ESP32_UDP_PIR/SMART_SENTRY_V2_0_ESP32_UDP_PIR.ino`
- Current USB serial IO sketch: `arduino/DB3000_ESP32_IO_Telemetry_2026_w_PIR/DB3000_ESP32_IO_Telemetry_2026_w_PIR.ino`
- GPIO4 passive buzzer is required if Smart Sentry sound cues should play on-board.

### Before Flashing
- [ ] Arduino IDE or PlatformIO installed
- [ ] ESP32 board support installed (ESP32 2.0.x+)
- [ ] USB cable connected to ESP32
- [ ] Board selected: "ESP32 Dev Module"
- [ ] COM port detected (e.g., COM10)
- [ ] Baud rate set to 115200

### Firmware File
- [ ] Using: `DB3000_ESP32_IO_Telemetry_2026_w_PIR.ino`
- [ ] Original file `DB3000_ESP32_IO_Telemetry_2026.ino` backed up
- [ ] `#define ENABLE_PIR_SUPPORT 1` (or 0 if PIR not needed)

### Hardware Connected
- [ ] GND connected to common reference
- [ ] 3.3V power available
- [ ] Trigger MOSFET/Servo on GPIO 27/13
- [ ] Relay outputs on GPIO 32/33/25
- [ ] PIR sensors on GPIO 35/34/39 (if enabled)

### Post-Flash Verification
- [ ] Serial monitor shows boot message
- [ ] `[BOOT] DB3000_ESP32_IO_Telemetry_2026_w_PIR ready`
- [ ] Responds to test command: `S0` → ACK message
- [ ] LED/Laser/Acc relays engage on command
- [ ] Trigger (water/projectile) responds to F token

## Testing Commands (Serial Terminal)

```
# Test water trigger (mosfet)
M0S0F1          → Fire in water mode (unsafe)
Response: ACK S=0 M=0 F=1 ...

# Test projectile trigger (servo pulse)
M1S0F1          → Fire in projectile mode
Response: ACK S=0 M=1 F=1 ...

# Test LED
L1              → LED on
Response: ACK ... L=1 ...

# Test Laser
R1              → Laser on
Response: ACK ... R=1 ...

# Enable PIR (if compiled with ENABLE_PIR_SUPPORT=1)
P1              → Enable PIR monitoring
Response: ACK ... P=1

# Test PIR event (wave hand at sensor)
[Should see: PIR_EVENT sensor_id=0 timestamp=...]

# Status dump
S0M0F0L0R0G0P0  → All off, safe mode, PIR disabled
Response: ACK S=1 M=0 F=0 L=0 R=0 G=0 P=0
```

## Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| No ACK response | USB not connected | Check COM port, try different cable |
| PIR_EVENT not appearing | PIR support disabled | Compile with `ENABLE_PIR_SUPPORT=1` |
| Events every <200ms | Hardware debounce issue | Extend firmware debounce (line ~72) |
| Relay not actuating | GPIO pin shorted or not connected | Verify wiring, test with digitalWrite(pin, HIGH) |
| Servo not responding | Pin 13 PWM not initialized | Check `ledcAttach()` in setup(), verify board type |
| GND not common | Multiple power supplies | Connect all GND pins to single common point |

---

**Pin Map Version**: 2.0 (PIR Support)  
**Last Updated**: December 2024  
**Hardware**: ESP32 Dev Module (30-pin variant)  
**Firmware**: DB3000_ESP32_IO_Telemetry_2026_w_PIR.ino

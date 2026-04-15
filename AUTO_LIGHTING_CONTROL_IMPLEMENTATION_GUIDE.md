# Auto Lighting Control — Full Implementation Guide

This document describes the complete plan for the **Auto Lighting Control** feature in Smart Sentry V2. Infrastructure groundwork (PWM comm layer, config dataclass, firmware LEDC support) is already implemented. This guide covers what remains to reach a fully operational feature.

---

## Feature Summary

Automatically adjusts LED brightness based on live scene luminance so the LED turns on and ramps up only when the scene is too dark, and dims or turns off when the scene is bright. The feature is togglable from both the Controls tab and a quick-access chip on the video canvas. Manual PWM override is also available.

---

## Current Implementation Status (as of 2026-04-15)

### Already done

| Layer | Status | Notes |
|---|---|---|
| `LightingConfig` dataclass | ✅ Done | `app/sentry_v2/sentry_v2_config.py` — 6 fields, serialized to JSON |
| Comm layer PWM | ✅ Done | `app/sentry_v2/sentry_v2_comm.py` — `led_pwm: int`, `set_led_pwm()`, `set_led()` shim |
| UDP JSON (0-255) | ✅ Done | Firmware already accepted `int`; no JSON parse changes needed |
| Firmware `ACCESSORY_PWM_ENABLED` flag | ✅ Done | Both `.ino` files — default `0` (relay, unchanged); set to `1` after MOSFET hardware install |
| Firmware `update_accessories()` | ✅ Done | Conditional `#if` block: PWM path uses `ledcWrite`, else original `digitalWrite` |
| Firmware `setup()` `ledcAttach` | ✅ Done | Conditional block attaches all 4 channels when flag is `1` |
| DB3000 `validate_pins()` guard | ✅ Done | LED blink test also gated by `ACCESSORY_PWM_ENABLED` |
| Tab instance vars | ✅ Done | `_auto_led_pwm`, `_scene_luma`, `_auto_lighting_frame_counter` |
| Camera loop brightness hook | ✅ Done | Samples every N frames, calls `_update_auto_lighting(frame)` |
| `_update_auto_lighting()` method | ✅ Done | Computes luma, maps to PWM range, queues `set_led_pwm` |
| Controls tab UI group | ✅ Done | "Auto Lighting Control" group box — toggle, PWM slider, threshold, range spinners, readout |
| Video chip bar | ✅ Done | QCheckBox + live luma/PWM label under video canvas |
| `_on_led_toggled` PWM dispatch | ✅ Done | Respects auto vs manual mode when LED button is toggled |
| `set_led_pwm` comm task dispatcher | ✅ Done | Wired into `_execute_comm_task` |
| Settings persistence | ✅ Done | All `LightingConfig` fields serialized via `asdict()` / `from_dict()` |
| Keyboard shortcut `Ctrl+Alt+L` | ✅ Done | Toggles auto lighting |

### Still required before fully operational

> ✅ **All steps completed as of 2026-04-16.** MOSFET hardware is installed, firmware PWM flag is enabled in both sketches, compiled (951 792 bytes, 72% flash), flashed to COM28 (hash verified, hard reset), and confirmed operational on physical hardware.

| Step | What | Status |
|---|---|---|
| 1 | Install MOSFET driver hardware on GPIO32/33/25/26 | ✅ Done |
| 2 | Set `ACCESSORY_PWM_ENABLED 1` in both `.ino` sketches | ✅ Done |
| 3 | Recompile and re-flash | ✅ Done — flashed to COM28 |
| 4 | Verify PWM output on hardware | ✅ Done — LED ramps correctly |
| 5 | Tune threshold and PWM range via Controls tab | ✅ Done — defaults tuned |

---

## Hardware Requirements

### MOSFET Driver Circuit (per output channel)

```
ESP32 GPIO → 1kΩ gate resistor → MOSFET gate
                                   MOSFET source → GND
                                   MOSFET drain  → Load (LED / Laser / ACC / Spare) → VCC
```

- **MOSFET recommendation**: IRLZ44N (logic-level, 3.3 V gate compatible) or similar
- **Gate resistor**: 100–1000 Ω (limits gate current and reduces ringing)
- **Flyback diode**: Required if the load is inductive (relay coil, motor)
- **Pins**: GPIO32 = LED, GPIO33 = Laser, GPIO25 = ACC, GPIO26 = Spare

> ⚠ Do NOT enable `ACCESSORY_PWM_ENABLED 1` if relay hardware is still directly connected. PWM at 5 kHz will cause relay chatter and rapid wear.

---

## Firmware Enable Procedure

### 1. Edit the sketch

Open `arduino/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR.ino` and change:

```cpp
// Before:
#define ACCESSORY_PWM_ENABLED  0

// After:
#define ACCESSORY_PWM_ENABLED  1
```

Repeat for `arduino/SMART_SENTRY_V2_3_DB3000_ESP32_UDP_PIR_FLYSKY/SMART_SENTRY_V2_3_DB3000_ESP32_UDP_PIR_FLYSKY.ino` if using the FlySky variant.

### 2. Compile and flash

From `f:\SMART SENTRY V2\SMART SENTRY`:

```powershell
# Compile
.\tools\arduino-cli\arduino-cli.exe compile --fqbn esp32:esp32:esp32 "arduino\SMART_SENTRY_V2_3_1_ESP32_UDP_PIR"

# Flash (replace COM28 with your actual port)
.\tools\arduino-cli\arduino-cli.exe upload -p COM28 --fqbn esp32:esp32:esp32 "arduino\SMART_SENTRY_V2_3_1_ESP32_UDP_PIR"
```

---

## App-Side Protocol Reference

The app sends `led` as an integer 0-255 in the UDP JSON payload (and in the ASCII token `L{value}`). The firmware PWM mapping is:

| App value | Relay mode (`ENABLED 0`) | PWM mode (`ENABLED 1`) |
|---|---|---|
| `0` | OFF | Duty 0 (off) |
| `1` | ON | Duty 255 (full on — backward-compat) |
| `2–255` | ON | Literal 8-bit duty cycle |

The compat mapping ensures existing toggle-only usage (value `1`) continues to work at full brightness in PWM mode without any app-side update.

### Auto lighting PWM mapping

```
if scene_luma < threshold:
    dark_ratio = 1.0 - (luma / threshold)        # 0.0 (just below threshold) → 1.0 (pitch black)
    pwm = pwm_min + dark_ratio × (pwm_max - pwm_min)
else:
    pwm = 0   # scene is bright, LED off
```

Config fields (stored in `config.lighting`):

| Field | Default | Description |
|---|---|---|
| `auto_lighting_enabled` | `False` | Master toggle |
| `led_pwm_value` | `255` | Manual PWM when auto is off |
| `auto_brightness_threshold` | `80` | Luma value (0-255) below which LED activates |
| `auto_pwm_min` | `60` | Minimum PWM when scene is just below threshold |
| `auto_pwm_max` | `255` | Maximum PWM when scene is near black |
| `auto_sample_interval_frames` | `8` | Frame interval between luminance samples |

---

## UI Reference

### Controls tab → Auto Lighting Control group

- **Auto Lighting checkbox** — master enable/disable
- **Manual LED PWM slider** (0-255) — used when auto is off and LED button is ON
- **Dark threshold spinner** — luma level that triggers LED activation
- **Auto PWM min / max spinners** — output range for auto mode
- **Scene luma / PWM readout label** — live feedback from the camera analysis loop

### Video canvas chip bar

- **Auto Lighting checkbox** — mirrors the Controls tab checkbox (in sync, no double-dispatch)
- **Luma/PWM label** — compact live readout (`luma:42 pwm:180`)

### Keyboard shortcut

- `Ctrl+Alt+L` — toggle auto lighting on/off

---

## Testing Checklist

- [ ] MOSFET hardware installed on all active output channels
- [ ] `ACCESSORY_PWM_ENABLED 1` compiled and flashed
- [ ] Oscilloscope confirms 5 kHz PWM on GPIO32 at varying duty
- [ ] App LED button ON + auto OFF → slider drives PWM correctly
- [ ] App LED button ON + auto ON, cover camera → PWM ramps to max
- [ ] App LED button ON + auto ON, point at bright source → PWM drops to 0
- [ ] App LED button OFF → PWM always 0 regardless of auto flag
- [ ] `Ctrl+Alt+L` toggles feature; video chip bar mirrors Controls tab checkbox
- [ ] Settings survive app restart (check `config.lighting` in JSON)
- [ ] DB3000 FlySky variant behaves identically

---

## Files Changed

| File | Change |
|---|---|
| `app/sentry_v2/sentry_v2_config.py` | Added `LightingConfig` dataclass, wired into `SentryV2Config` and `from_dict` |
| `app/sentry_v2/sentry_v2_comm.py` | `led_on→led_pwm`, `set_led_pwm()`, `set_led()` shim, all 3 send methods updated |
| `app/sentry_v2/sentry_v2_tab.py` | Instance vars, camera loop hook, `_update_auto_lighting()`, Controls UI group, video chip bar, `_on_led_toggled`, dispatcher, shortcut, handlers |
| `arduino/SMART_SENTRY_V2_3_1_ESP32_UDP_PIR/…ino` | `ACCESSORY_PWM_ENABLED` define, conditional `ledcAttach` in `setup()`, conditional `ledcWrite` in `update_accessories()` |
| `arduino/SMART_SENTRY_V2_3_DB3000_ESP32_UDP_PIR_FLYSKY/…ino` | Same as above + `validate_pins()` blink guard |
| `SMART SENTRY/ESP32_CURRENT_SKETCH.md` | Accessory PWM Support section added |
| `SMART SENTRY/RECENT_UPDATES.json` | Entry logged |

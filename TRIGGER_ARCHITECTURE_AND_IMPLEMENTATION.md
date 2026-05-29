# Smart Sentry Trigger System Architecture & Implementation

**Version:** v3.5.2  
**Date:** May 2026  
**Component:** Trigger subsystem (water/MOSFET + projectile/servo)

---

## System Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         SMART SENTRY V2 TRIGGER                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  UI Layer (sentry_v2_tab.py)                                            │
│  ├─ Settings Panel: Trigger Mode selector                              │
│  ├─ MOSFET panel: Pulse ON, Cycles, Cycle OFF, Polarity                │
│  ├─ Servo panel: Rest angle, Fire angle, Speed                         │
│  └─ Auto-Trigger toggle                                                │
│                                                                           │
│  ↓                                                                       │
│                                                                           │
│  Configuration (sentry_v2_config.py)                                    │
│  ├─ trigger_mode_bb: bool (False=MOSFET, True=Servo)                   │
│  ├─ trigger_mosfet_pulse_ms: int (10-2000)                             │
│  ├─ trigger_mosfet_cycle_count: int (1-20)                             │
│  ├─ trigger_mosfet_cycle_off_ms: int (10-2000)                         │
│  ├─ trigger_output_active_low: bool                                    │
│  ├─ trigger_servo_rest_deg: int (0-180)                                │
│  ├─ trigger_servo_fire_deg: int (0-180)                                │
│  ├─ trigger_servo_speed_dps: int (10-5000)                             │
│  └─ auto_trigger_enabled: bool                                         │
│                                                                           │
│  ↓                                                                       │
│                                                                           │
│  Engine (sentry_v2_engine.py) — Auto-Fire Decision Logic               │
│  ├─ Engagement phase: aim → fire                                       │
│  ├─ _trigger_should_fire(): centering + hold time gate                 │
│  ├─ _begin_fire(): checks auto_trigger_enabled + no-fire masks         │
│  └─ _cb_fire(burst_count): callback to tab's _on_engine_fire()         │
│                                                                           │
│  ↓                                                                       │
│                                                                           │
│  Tab Fire Execution (sentry_v2_tab.py)                                  │
│  ├─ _on_engine_fire(burst_count): validates safety/connection/config   │
│  └─ _start_fire_burst(): queues comm tasks (F=1, F=0 pulses)           │
│                                                                           │
│  ↓                                                                       │
│                                                                           │
│  Communication Layer (sentry_v2_comm.py)                                │
│  ├─ send_trigger_runtime_config(): sends J, K, N, X, U, V, H, B tokens│
│  ├─ _build_ascii(): adds F token to motion command                     │
│  └─ send_command(): queues fire pulse via serial/UDP                   │
│                                                                           │
│  ↓                                                                       │
│                                                                           │
│  Hardware Firmware (Arduino/ESP32)                                      │
│  ├─ parseTokenInt(): extract J, K, N, U, V, H, X, B from serial       │
│  ├─ updateFireOutputs(): execute MOSFET or servo pulse                 │
│  └─ writeTriggerMosfet() / triggerServoSet(): GPIO control             │
│                                                                           │
│  ↓                                                                       │
│                                                                           │
│  Physical Outputs (GPIO pins)                                           │
│  ├─ ESP32 GPIO27 (MOSFET) or GPIO13 (Servo)                           │
│  └─ Nano D8 (MOSFET) or D9 (Servo)                                    │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Data Flow: Settings Change to Hardware Fire

### 1. User Changes Trigger Setting

**Location:** Settings Tab → "Pulse ON (ms)" spinbox

```python
# sentry_v2_tab.py line 9541
self._spin_trigger_mosfet_pulse_ms.valueChanged.connect(
    self._on_trigger_mosfet_settings_changed
)
```

### 2. Handler Updates Config

**Location:** sentry_v2_tab.py:_on_trigger_mosfet_settings_changed()

```python
def _on_trigger_mosfet_settings_changed(self) -> None:
    pulse_ms = int(self._spin_trigger_mosfet_pulse_ms.value())
    self.config.engagement.trigger_mosfet_pulse_ms = pulse_ms  # ← Store in config
    self._sync_comm_runtime_settings_from_config()             # ← Sync to comm
    self._queue_runtime_trigger_config_if_connected()          # ← Queue send
    self._push_config()                                         # ← Persist
    self._save_config_quietly()
```

### 3. Comm Layer Syncs

**Location:** sentry_v2_tab.py:_sync_comm_runtime_settings_from_config()

```python
def _sync_comm_runtime_settings_from_config(self) -> None:
    engagement = self.config.engagement
    self._comm.trigger_mosfet_pulse_ms = int(engagement.trigger_mosfet_pulse_ms)
    self._comm.trigger_mosfet_cycle_count = int(engagement.trigger_mosfet_cycle_count)
    # ... etc for all trigger fields
```

### 4. Settings Queued for Send

**Location:** sentry_v2_tab.py:_queue_runtime_trigger_config_if_connected()

```python
def _queue_runtime_trigger_config_if_connected(self) -> None:
    # Skip if host controls hardware or not connected
    if self._host_controls_hardware() or not self._comm.is_connected():
        return
    self._queue_comm_task("send_trigger_runtime_config")
```

### 5. Comm Builds & Sends Packet

**Location:** sentry_v2_comm.py:send_trigger_runtime_config()

```python
def send_trigger_runtime_config(self) -> bool:
    if self._mode in (self.MODE_ESP32_USB, self.MODE_DUAL_USB):
        # Serial path: send individual tokens
        return self._send_trigger_runtime_config_serial()
    # UDP path: send JSON config
    payload = {
        "action": "config",
        "trigger": {
            "mosfet_pulse_ms": int(self.trigger_mosfet_pulse_ms),
            ...
        }
    }
    return self._send_udp_payload(payload)
```

**Serial (Nano/USB):**
```
J120\n  → Set pulse ON to 120 ms
K1\n    → Set cycle count to 1
N50\n   → Set cycle OFF to 50 ms
X0\n    → Set active-HIGH output
U0\n    → Set servo rest to 0°
V45\n   → Set servo fire to 45°
H360\n  → Set servo speed to 360°/s
B0\n    → PIR blink disabled
```

### 6. Hardware Firmware Parses & Stores

**Location:** Arduino firmware (DB3000_ESP32_IO_Telemetry_PIR.ino:~line 370)

```cpp
int j = clampInt(parseTokenInt(line, 'J', (int)trigger_mosfet_pulse_ms), 10, 2000);
if (j > 0) trigger_mosfet_pulse_ms = (uint32_t)j;

int k = clampInt(parseTokenInt(line, 'K', trigger_mosfet_cycle_count), 1, 20);
if (k > 0) trigger_mosfet_cycle_count = k;
// ... etc
```

### 7. Hardware Acknowledges Receipt

**Serial ACK response:**
```
[RX] J120
[TX] ACK ... J=120 K=1 N=50 X=0 U=0 V=45 H=360 ...
```

---

## Data Flow: Auto-Fire Trigger

### 1. Engine Detects Target & Evaluates Aim Lock

**Location:** sentry_v2_engine.py:_update_engaging_phase() (line ~1250)

```python
elif self._engage_phase == "precision":
    # Accumulate aim lock frames
    if self._has_aim_lock(lock_pan, lock_tilt):
        self._aim_lock_frames += 1
    
    settle = float(self.cfg.engagement.precision_settle_time)  # e.g., 0.4 s
    elapsed = now - self._phase_start
    settle_met = elapsed >= settle
    early_lock = self._aim_lock_frames >= aim_lock_required_frames
```

### 2. Engine Checks Auto-Fire Gate

**Location:** sentry_v2_engine.py:_update_engaging_phase() (line ~1295)

```python
# PRIMARY AUTO-TRIGGER LOGIC
if (
    self.cfg.engagement.auto_trigger_enabled  # ← REQUIRED
    and (settle_met or early_lock)            # ← Timing met
    and self._ready_to_fire()                 # ← Aim lock frames satisfied
    and target is not None
    and self._trigger_should_fire(...)        # ← Centering & hold time met
):
    self._begin_fire(order, now)  # ← Call fire callback
    return
```

### 3. Engine Calls Fire Callback

**Location:** sentry_v2_engine.py:_begin_fire() (line ~1854)

```python
def _begin_fire(self, order: EngagementOrder, now: float) -> None:
    # AUTO-TRIGGER FIRE GATE (DO NOT MODIFY WITHOUT OWNER APPROVAL)
    fired = (
        self.cfg.engagement.auto_trigger_enabled  # ← Double-check
        and blocked_mask is None                  # ← No-fire zones
        and prompted_auto_fire_allowed            # ← Prompted target override
    )
    if fired:
        burst = self.cfg.engagement.burst_count
        if self._cb_fire:
            self._cb_fire(burst)  # ← Invoke tab's _on_engine_fire()
```

### 4. Tab Validates & Executes Fire

**Location:** sentry_v2_tab.py:_on_engine_fire() (line ~13937)

```python
def _on_engine_fire(self, burst_count: int) -> None:
    # VALIDATION GATES (check in order)
    if not self.config.engagement.auto_trigger_enabled:
        self._log("AUTO-FIRE BLOCKED: auto_trigger_enabled is FALSE")
        return
    if not self._safety_armed:
        self._log("AUTO-FIRE BLOCKED: Safety is not armed")
        return
    if not self._comm.is_connected():
        self._log("AUTO-FIRE BLOCKED: Hardware link disconnected")
        return
    # ... check runtime safety & faults ...
    
    # EXECUTE FIRE
    self._start_fire_burst(pan, tilt, burst_count, interval)
    self._log(f"AUTO-FIRE: Queuing fire burst (burst={burst_count})")
```

### 5. Tab Queues Fire Pulse Commands

**Location:** sentry_v2_tab.py:_start_fire_burst()

```python
def _start_fire_burst(self, pan: float, tilt: float, burst_count: int, interval_ms: int) -> None:
    self._burst_pan = pan
    self._burst_tilt = tilt
    self._burst_remaining = max(1, burst_count)
    self._burst_interval_ms = interval_ms
    self._burst_phase_on = True
    
    # Queue FIRST fire pulse
    self._queue_comm_task("send_command", pan, tilt, fire=1)
    self._burst_timer.start(self._fire_burst_phase_duration_ms())
```

### 6. Comm Sends Fire Command

**Location:** sentry_v2_comm.py:_build_ascii()

```python
def _build_ascii(self, pan: float, tilt: float, fire: int = 0) -> str:
    f = int(bool(fire))  # fire=1 or fire=0
    return f"P{p}T{t}F{f}L{led}R{laser}G{acc}A{spare}S{safety}M{mode}X{polarity}\n"
    # Example: P90T50F1L0R0G0A0S0M0X0\n
```

### 7. Hardware Receives & Executes

**Location:** Arduino firmware:updateFireOutputs() (line ~220+)

```cpp
if (!mode_projectile) {
    // Water mode (M0)
    if (fire_token && !last_fire_cmd && !mosfet_cycle_active) {
        mosfet_cycle_active = true;
        mosfet_cycle_on_phase = true;
        mosfet_cycle_phase_start_ms = now;
        mosfet_cycle_pulses_remaining = trigger_mosfet_cycle_count;
        writeTriggerMosfet(true);  // ← GPIO27 = HIGH (or LOW if active_low)
    }
    // ... manage pulse timing ...
} else {
    // Projectile mode (M1)
    if (fire_token && !projectile_pulse_active) {
        projectile_pulse_active = true;
        projectile_pulse_start_ms = millis();
        triggerServoSet(true);  // ← GPIO13 PWM to fire angle
    }
    // ... auto-return after pulse duration ...
}
```

---

## Key Design Principles

### 1. Separation of Concerns

| Layer | Responsibility |
|-------|-----------------|
| **UI** | Display settings, collect user input, manage visual state |
| **Config** | Store settings persistently, validate ranges |
| **Engine** | Decision logic (aim lock, centering, timing gates) |
| **Comm** | Transport-agnostic serialization (serial/UDP) |
| **Firmware** | Real-time GPIO control, timing, telemetry |

### 2. Fire Gate Redundancy

Fire is guarded by **three independent checks**:

1. **Engine level** (`_begin_fire()`):
   - `auto_trigger_enabled` flag check
   - No-fire mask check
   - Prompted target override check

2. **Tab level** (`_on_engine_fire()`):
   - Config consistency check
   - Safety armed check
   - Connection state check
   - Runtime safety state check
   - Runtime fault check

3. **Firmware level** (Arduino):
   - Safety token (S0=armed, S1=safe)
   - Fire token (F0=no fire, F1=fire)
   - Mode validation

**Why three layers?** Safety margin. No single software error can cause unintended fire.

### 3. Configuration Persistence

Settings flow:
```
UI widget
  ↓ valueChanged signal
Handler (_on_*_changed)
  ↓ .config.engagement.field = value
Config object
  ↓ _push_config()
YAML file (auto-loaded on next restart)
```

This ensures settings survive app restart.

### 4. Runtime vs. Boot Configuration

| Aspect | Runtime | Boot |
|--------|---------|------|
| **When sent** | After connection established OR on user change | On firmware boot (hardcoded defaults) |
| **Transport** | J, K, N, X, U, V, H, B tokens | Compiled constants |
| **Can change** | Yes, every fire cycle | No, requires reflash |
| **Use case** | Tune responsiveness live | Safety defaults if comm lost |

---

## Critical Conditional Logic

### Auto-Fire Unlock (Must ALL Be True)

```
    auto_trigger_enabled ✓
    AND
    (precision_settle_time OR early_aim_lock) ✓
    AND
    aim_lock_frames >= aim_lock_required_frames ✓
    AND
    target not None ✓
    AND
    NOT in refractory period ✓
    AND
    NOT blocked by no-fire mask ✓
    AND
    centered within fire_trigger_enter_tolerance ✓
    AND
    AND hold_time >= fire_trigger_hold_time ✓
    AND
    confidence >= fire_trigger_min_confidence ✓
    AND
    persistence >= fire_trigger_min_persistence ✓
    AND
    NOT (app-level safety checks)
    ──────────────────────────────────
    ==> FIRE EXECUTES
```

### Failure Diagnostics

Every `AND` condition that fails is logged:
```
AUTO-FIRE BLOCKED: [reason]
  - auto_trigger_enabled is FALSE
  - Safety is not armed
  - Hardware link disconnected
  - Runtime safety is LOCKED
  - Runtime fault active: [code]
  - Refractory period active
  - No-fire mask blocking aim
  - Aim not centered
  - Hold time not satisfied
```

---

## Testing & Validation Checklist

- [ ] **UI Panel Visibility:** MOSFET panel shows when M0; Servo panel when M1
- [ ] **Settings Persistence:** Change value, close/reopen app, value persists
- [ ] **Comm Sync:** Change setting, check serial monitor/logs for J/K/N/U/V tokens
- [ ] **Firmware Acknowledgment:** Check ACK response includes updated values
- [ ] **Manual Fire:** Verify manual fire button works before enabling auto-fire
- [ ] **Reticle Locking:** Reticle turns RED when aim lock achieved
- [ ] **Auto-Fire Trigger:** Target centered + hold time → fire happens within 100–300 ms
- [ ] **Fire Output:** GPIO fires in correct mode (M0 pulse train vs. M1 servo pulse)
- [ ] **Safety Gate:** Auto-fire blocks if safety not armed
- [ ] **Connection Gate:** Auto-fire blocks if comm disconnected
- [ ] **Mask Gate:** Auto-fire blocks if fire position in no-fire zone

---

## Known Issues & Mitigations

| Issue | Root Cause | Mitigation |
|-------|-----------|-----------|
| Fire not triggering despite all green | Settings not sent to firmware | Force reconnect or manually toggle trigger mode |
| MOSFET fires continuously | Active-LOW polarity incorrect | Toggle checkbox; verify hardware output voltage |
| Servo doesn't return to rest | Speed too slow for smooth motion | Increase speed or check servo power supply |
| Auto-fire enabled but won't fire | Aim lock or hold time gate not met | Check overlay reticle color (should be RED) |
| Settings appear in config but don't fire | Safety not armed in hardware | Toggle hardware safety switch or Connection Tab toggle |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 3.5.2 | May 2026 | Current: Full auto-fire support, dual trigger modes, runtime config tokens |
| 3.5.1 | Apr 2026 | Stable servo/MOSFET pulse train implementation |
| 3.5.0 | Mar 2026 | Initial trigger architecture refactor |
| 3.0.0 | 2025 | Waveshare bus servo era (archived) |

---

## References

- **Settings File:** `app/config/smart_sentry_settings.json` → `engagement` section
- **Firmware:** `arduino/DB3000_ESP32_IO_Telemetry_PIR/DB3000_ESP32_IO_Telemetry_PIR.ino`
- **Communication:** `app/sentry_v2/sentry_v2_comm.py` → `send_trigger_runtime_config()`
- **Engine Logic:** `app/sentry_v2/sentry_v2_engine.py` → `_trigger_should_fire()`, `_begin_fire()`
- **UI:** `app/sentry_v2/sentry_v2_tab.py` → Settings panel, fire execution

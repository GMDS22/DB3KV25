# INITIATE SERVO UPGRADE — Serial Bus Pan/Tilt + Per-Servo Current + Total Current (2026)

## Read-this-first (mandatory)
If a request says **“initiate servo upgrade”**, you must read this document end-to-end *before* touching code, firmware, or docs.

This upgrade changes the **motion hardware interface** (Pan/Tilt servos) and adds **power telemetry** (Pan current, Tilt current, Total current). It must be done in a way that **does not break the trigger system**.

**Hard invariant:** the turret still uses a **separate trigger actuator (servo or MOSFET)** and it must remain operational and unaffected by the Pan/Tilt servo migration.

---

## 0) Scope, non-scope, and hard requirements

### In-scope
1) Replace **Pan** and **Tilt** movement servos from PWM to **serial bus servos** driven via a **debug board**.
2) Add telemetry so the UI can display:
   - Pan servo current (serial bus / debug board)
   - Tilt servo current (serial bus / debug board)
   - Total turret current (dedicated current sensor wired to the Nano)
3) Update all aiming/movement/autotracking paths so they all use the new Pan/Tilt transport (no legacy PWM path for pan/tilt).

### Servo information requirement (do this before firmware work)
This upgrade cannot be implemented correctly without pinning down the **exact Pan/Tilt bus servo model and protocol**.

Reference images in repo root:
- [ce27550c941036c537039cccbb3b8236.jpg_2200x2200q80.jpg](ce27550c941036c537039cccbb3b8236.jpg_2200x2200q80.jpg)
- [1efe7e1c372359451be7058f9abeda0e.jpg_2200x2200q80.jpg](1efe7e1c372359451be7058f9abeda0e.jpg_2200x2200q80.jpg)

Required details to record (and keep consistent across firmware + docs):
- Exact model name + vendor series
- Bus type: TTL UART bus, half-duplex vs full-duplex
- Required baud rate and packet framing
- Servo ID plan (Pan=1, Tilt=2 unless changed)
- Voltage range and power requirements
- Current/torque/speed specs (for thresholds + PSU sizing)
- Supported feedback signals (position/temp/voltage/current)

Known baseline (from provided servo description / product link):
- Yahboom **YB-SD35M** serial bus servo
- Rotation range: **0–270°**
- “35kg” torque class (confirm units and voltage in datasheet)
- Connectors: **3 × HY2.0-3Pin**

Still TBD (must confirm before implementing bus packet framing): half/full duplex, baud rate, and exact pinout.

### Explicit non-scope
- Replacing or redesigning the **trigger actuator**. Trigger remains as-is.
- Changing detection algorithms (YOLO / frame diff / backsub) beyond what is required to keep aiming math stable.

### Hard requirements (must not regress)
1) **Trigger remains functional and unchanged**
   - The UI already supports “Water (MOSFET)” and “Projectile (BB Servo)” trigger modes.
   - The host uses an encoded command containing `F{fire_token}` and a trigger mode token.
   - The Pan/Tilt migration must not alter firing semantics, safety gating, cooldown logic, or trigger-mode selection.

2) **All aiming modes must remain supported and benefit from improved motion**
   - Manual D-pad movement.
   - Autotracking (all detection modes 0–9).
   - Precision Mode (host-side PID / micro-correction path).
   - Sentry mode control paths.
   - Idle modes (watch/search/rest) movement.

“Improved” here means: after the migration, every mode’s motion ultimately drives the serial bus Pan/Tilt servos and can take advantage of serial bus servo characteristics (better holding, speed/accel control, optional feedback), rather than being limited by PWM jitter and repeated command hunting.

---

## 1) Current codebase behavior (what exists today)

### Command encoding: one packed line to the MCU
The host currently formats a **single packed command line** that includes pan, tilt, firing, accessories, safety, and mode flags:

`P{pan}T{tilt}F{fire}L{led}R{laser}G{acc}S{safety}M{mode}`

This is built in:
- app/MAIN_FILE_SINGLE_CAM.py → `send_serial_command()`

This packed command is also parsed for UI display only in:
- app/turret_enhancements.py → `_format_serial_text()` (purely for display)

Important implication: You can change the underlying hardware (PWM → serial bus) **without changing the host command format**, as long as the MCU interprets `P` and `T` as the requested angles.

### Trigger system (must remain intact)
The UI exposes trigger mode and fire controls in:
- app/ui_builder.py (Manual Movement & Firing)

The host encodes trigger intent in `send_serial_command()` via:
- `fire_token` (derived from MOSFET hold and `trigger_fired`)
- `mode_token` (derived from `trigger_mode_bb`)

The **trigger actuator itself is not Pan/Tilt**. It is either:
- a MOSFET/relay (water mode), or
- a dedicated BB trigger servo (projectile mode).

Therefore:
- Upgrading **Pan/Tilt** to serial bus must not remove or alter `F`/trigger handling.
- Firmware must keep its trigger output path exactly compatible.

### Servo calibration today (likely becomes obsolete for Pan/Tilt)
The repo contains a PWM-oriented Pan/Tilt calibration tool:
- app/servo_calibration_tool.py

And the main app loads Pan/Tilt limits from:
- app/MAIN_FILE_SINGLE_CAM.py → `load_servo_calibration()` reading `servo_calibration.json`

This is tightly tied to PWM assumptions (“discover range by sweeping with PWM commands”). For serial bus servos, Pan/Tilt limits may still exist, but the calibration workflow and storage format will likely need to change.

---

## 2) Target architecture for the upgrade (high-level)

### Keep the host command stable unless there is a compelling reason
Best outcome for safety and backwards compatibility:
- The host keeps sending the same packed command.
- The MCU (Nano + debug board) converts requested `pan_angle`/`tilt_angle` into serial bus servo commands.
- Trigger remains controlled exactly as before using the same `F`/mode semantics.

**Note (2026-01): the codebase now supports multiple host connection topologies.**
- You can still run the original “host → Nano → servos” architecture (Arduino/Nano ASCII mode).
- You can also run “host → Debug Board” for PAN/TILT directly (Debug Board bus-servo mode).
- For best of both worlds (PAN/TILT direct + Nano IO), use **Dual Port** mode (two COM ports).

This matters because future changes must preserve correct routing/decoding rules (binary bus vs ASCII Nano). See `CHANGE_IMPACT_REFERENCE.md` → **Serial Communication / Arduino Interface**.

Why this is preferred:
- It minimizes change surface in app/MAIN_FILE_SINGLE_CAM.py where many safety and anti-jitter protections exist.
- It avoids breaking sentry mode tools and any external scripts that emit the same packed command.

### Add *telemetry messages* from MCU → host for current monitoring
Instead of encoding currents into the packed command, send **separate telemetry lines** from the MCU to the host at a modest rate (e.g., 5–10 Hz). The host parses them and updates the monitor panel.

Recommended telemetry line concept (example, final format is up to firmware but must be documented):

`CUR PmA={pan_mA} TmA={tilt_mA} TOTmA={total_mA}`

Optional additional telemetry (strongly recommended for better aiming):
- Actual Pan/Tilt position feedback (if available from servos):
  `POS Pdeg={pan_deg} Tdeg={tilt_deg}`
- Overcurrent/stall flags:
  `FAULT PAN_OVERCURRENT` / `FAULT TILT_STALL`

---

## 3) Detailed breakdown: what must be updated (and why)

### 3.1 Firmware (Nano + debug board)
This repo does not contain the firmware source, but the firmware contract must be treated as part of this upgrade.

Firmware must implement:
1) Serial bus control for Pan servo (bus ID, direction, limits).
2) Serial bus control for Tilt servo (bus ID, direction, limits).
3) Preserve trigger outputs:
   - MOSFET output logic must remain compatible.
   - BB trigger servo control (if used) must remain PWM or whatever it currently is.
4) Telemetry generation:
   - Pan current (from debug board / servo feedback)
   - Tilt current (from debug board / servo feedback)
   - Total current (from external current sensor on Nano)

Firmware must also keep the safety model consistent with the host:
- When `S{safety}` indicates safe/armed, the MCU must continue to enforce firing safety.
- If the MCU currently enforces tilt safety locking, that behavior must be preserved or explicitly redefined.

### 3.2 Serial protocol (host ↔ MCU)

#### Host → MCU
The simplest (and recommended) approach is to keep:
- The packed command format unchanged.

In that case, the upgrade requires only that the MCU changes its interpretation:
- `P{pan}` and `T{tilt}` now mean “target angle for serial bus servos” rather than “PWM angle.”

#### MCU → Host (new)
Add new telemetry lines.

Host-side parsing changes will be required in whichever component currently reads `self.ser.readline()` and processes MCU output (typically within app/MAIN_FILE_SINGLE_CAM.py). The parser must:
- Be resilient to partial lines and unexpected text.
- Never block the UI thread.
- Record the latest currents into `self` fields so UI panels can display them.

### 3.3 Aiming/motion logic (all modes must route to serial bus)

**Key observation:** most aiming logic ultimately sets `self.target_pan` / `self.target_tilt`, and motion delivery is centralized in `send_serial_command()`.

That is good news: if `send_serial_command()` continues to send a stable `P/T` request, and the MCU now drives serial bus servos, then:
- Manual movement
- Autotracking
- Precision Mode micro-corrections
- Sentry/idle movements

…all automatically drive the upgraded hardware without duplicating logic.

However, to ensure the upgrade truly “improves aiming,” we must revisit some behaviors that were built to compensate for PWM limitations:

1) Redundant command filtering
   - Today: host skips sending if rounded integers did not change.
   - With serial bus servos (often higher resolution), you may want optional higher-resolution steps (e.g., 0.1°) or a different anti-jitter strategy.
   - If the host remains integer-degree, improvement still comes from better servo control (less hunting), but you won’t get sub-degree commands.

2) Precision Mode micro-step accumulator
   - Today: host accumulates fractional error and occasionally emits a ±1° step.
   - Serial bus servos might allow:
     - smaller minimum steps, or
     - servo-side speed/accel limiting that makes 1° steps smoother.

3) Optional closed-loop improvement (recommended)
   - If servo feedback provides actual position, the host can compute error using actual pose instead of “last sent” pose.
   - This reduces overshoot and improves stability in all tracking modes.

These are improvements, but they should be staged behind a configuration flag so the first integration can be stable.

### 3.4 UI monitoring: Pan current / Tilt current / Total current

There are two relevant UI concepts in the repo:
- The main app’s docks and status areas (built by app/ui_builder.py).
- A lightweight overlay monitor (app/health_monitor.py) used for runtime performance/health.

For this upgrade, “monitor panel” should expose the three current values clearly.

Implementation approach (to be executed during the upgrade, not now):
- Create three fields in a monitor panel UI section:
  - Pan current
  - Tilt current
  - Total current
- Update them from main-window state fields that are updated by the serial read loop.

**Important:** current parsing and UI update must be non-blocking and main-thread safe.

### 3.5 Tools/features to remove or update

#### Pan/Tilt PWM calibration tooling
The PWM-focused Pan/Tilt calibration workflow is likely obsolete:
- app/servo_calibration_tool.py
- app/MAIN_FILE_SINGLE_CAM.py → menu entry that launches it
- app/MAIN_FILE_SINGLE_CAM.py → `load_servo_calibration()` reading `servo_calibration.json`

For serial bus servos, “calibration” becomes one or more of:
- Servo ID discovery
- Direction inversion
- Soft limits / end-stops
- Center offset
- Speed/accel presets

Therefore the step-by-step upgrade must include either:
- removing the old PWM calibration tool, or
- rewriting it into a serial bus configuration tool.

#### What must NOT be removed
- Trigger mode controls and fire/safety logic.
- Any logic that ensures firing is gated by safety.

---

## 4) Step-by-step procedure (the full to-do for “initiate servo upgrade”)

This is the authoritative sequence. The order matters because it minimizes downtime and preserves safety.

### Phase A — Preparation (no behavioral change yet)
1) Define the exact serial bus servo hardware interface:
   - Servo model(s)
   - Bus protocol (e.g., TTL half-duplex)
   - Servo IDs for Pan and Tilt
   - Expected angle range mapping (degrees ↔ servo units)

2) Define current measurement sources and units:
   - Pan current source (debug board) and unit (mA recommended)
   - Tilt current source (debug board) and unit
   - Total current sensor model (e.g., ACS712/INA219) and unit

3) Decide telemetry rate and message format.
   - Ensure it won’t flood the serial link.
   - Ensure it won’t spam the UI.

4) Declare acceptance criteria up-front:
   - Manual D-pad Pan/Tilt works.
   - Autotracking moves both axes.
   - Precision Mode still converges.
   - Sentry mode still moves and can trigger fire.
   - Trigger modes still function unchanged.
   - UI displays Pan current, Tilt current, Total current.

### Phase B — Firmware upgrade (Pan/Tilt only; trigger preserved)
1) Implement serial bus control for Pan and Tilt on the debug board.
2) Ensure the MCU still consumes the packed command line.
3) Confirm that `F` handling and trigger outputs behave exactly as before.
4) Add telemetry lines for currents (and optionally positions).
5) Add basic firmware-side protection:
   - overcurrent detection
   - stall detection
   - optional safe shutdown behavior for Pan/Tilt only

**Critical:** firmware protection must not disable trigger handling unless explicitly intended (safety model must be clear).

### Phase C — Host parsing and state plumbing (currents)
1) In the host’s serial input path, parse the new telemetry lines.
2) Store the latest values in main window fields, e.g.:
   - `pan_current_mA`
   - `tilt_current_mA`
   - `total_current_mA`

3) Ensure parsing failures are logged (no silent exceptions).

**Implementation status (host, 2026-01-06):**
- The host already parses telemetry lines in the form `CUR PmA=<...> TmA=<...> TOTmA=<...>`.
- Telemetry parsing is resilient to separator variations and ignores non-telemetry lines.
- Serial input is drained even when redundant outbound commands are skipped (prevents telemetry backlog).

### Phase D — UI monitor panel implementation
1) Add three UI labels for currents.
2) Refresh them on a timer or when new telemetry arrives.
3) Present units and “N/A” if missing.

**Implementation status (UI, 2026-01-06):**
- A **Current Monitor** dock shows Pan/Tilt/Total current in mA (shows “—” until telemetry is received).

### Phase E — Motion/aiming improvements (all modes)
This phase is where you ensure “all aiming modes are improved” in a concrete, testable way.

1) Confirm that every mode ultimately drives `send_serial_command()` and no mode writes PWM-specific commands.
2) Validate motion stability improvements:
   - Review redundant-command filtering behavior.
   - For serial bus servos, decide whether to keep integer-degree stepping or introduce higher-resolution commands.
3) (Optional but recommended) Integrate position feedback:
   - Use actual servo position to compute error.
   - Reduce overshoot in fast-moving targets.

### Phase F — Update or remove obsolete tools
1) Deprecate PWM Pan/Tilt calibration tool:
   - Remove menu entry that launches app/servo_calibration_tool.py, OR
   - Replace tool with serial bus servo config tool (IDs, direction, limits).

2) Decide what happens to `servo_calibration.json`:
   - If still needed for limits, redefine its meaning and update loader.
   - If replaced, create a new config file and migrate.

**Trigger tooling is not part of this removal.**

### Phase G — Tests and verification
Run the narrowest checks first, then broader smoke tests:
- `python test_app_start.py`
- `python SERIAL_CONNECTION_TEST.py` (verify serial link & telemetry)
- `python servo_fix_test.py` (update this test if it assumes PWM)

Manual verification checklist:
- Manual D-pad movement in both axes.
- Autotrack in at least one fast mode (FrameDiff) and one stable mode (BackSub/YOLO).
- Precision Mode enabled: check small corrections move both axes.
- Sentry mode enabled: confirm it can move and trigger fire.
- Trigger mode “Water (MOSFET)” still functions.
- Trigger mode “Projectile (BB Servo)” still functions.

### Phase H — Documentation updates (required)
When the actual implementation is done, update at minimum:
- CHANGE_IMPACT_REFERENCE.md (servo + current monitoring couplings)
- RECENT_UPDATES.json (entry for this upgrade)
- README.md (wiring, firmware requirements, telemetry description)

Also update or add:
- A short protocol spec section describing telemetry lines.
- A note that trigger servo remains separate and unchanged.

---

## 5) “Do not break trigger” guardrails (very explicit)

During implementation, apply these rules:

1) The `F{fire_token}` concept remains authoritative.
   - Do not reinterpret `F` as anything related to Pan/Tilt.

2) The trigger mode concept remains authoritative.
   - UI element `trigger_mode_combo` and state `trigger_mode_bb` must continue to work.

3) Do not change safety gating semantics.
   - If `Safety: LOCKED` prevents firing today, it must still prevent firing.

4) If Pan/Tilt are faulted (overcurrent), define the behavior explicitly.
   - Recommended: motion may be inhibited, but trigger safety model remains intact.

---

## 6) Known touchpoints in this repo (where changes will concentrate later)

These are the main files that will be impacted when “initiate servo upgrade” is executed:

- app/MAIN_FILE_SINGLE_CAM.py
  - `send_serial_command()` (motion delivery and command encoding)
  - serial read loop / parsing (telemetry)
  - `load_servo_calibration()` (Pan/Tilt calibration assumptions)
  - tools menu entry that launches servo calibration

- app/turret_enhancements.py
  - `_format_serial_text()` will need to understand any new telemetry messages if you want them human-friendly in the serial console.

- app/ui_builder.py
  - Monitor panel UI fields for Pan/Tilt/Total current.
  - Trigger UI must remain unchanged.

- app/servo_calibration_tool.py
  - Pan/Tilt PWM-specific; likely deprecated or repurposed.

- app/sentry_mode/*
  - Any emitter of packed commands must remain compatible.

---

## 7) Open decisions to resolve before coding

This upgrade will go faster if these are decided first:

1) Do we keep the host packed command format unchanged? (recommended: yes)
2) What is the exact telemetry format and units?
3) Does the debug board provide reliable per-servo current directly, or is it estimated?
4) Do we want to add actual position feedback to the host for better aiming, or keep the host “open loop” and rely on servo-side control?
5) What is the fault policy for overcurrent (warn only vs. inhibit motion vs. full stop)?

---

## 8) Reference artifacts created for this upgrade

- pan_tilt_serialbus_current_upgrade_diff.py (planning diff file)

This document is the **authoritative** step-by-step checklist and integration guide.

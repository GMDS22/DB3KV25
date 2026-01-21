"""pan_servo_current_sensor_upgrade_diff.py

Diff/Planning file for: PAN SERVO & CURRENT SENSOR UPGRADES (2026)

Scope:
- Add a turret **total current** sensor (measured on the Nano and reported over serial).
- Replace **Pan** servo control with a **serial-bus** servo (Tilt remains PWM for now).

This file is for review and planning only.
DO NOT apply these changes directly; use as a reference for implementation and code review.

Key improvement goals (monitoring-focused):
- Define a robust, backward-compatible serial message format for current.
- Clearly separate **total turret current** (sensor) vs **pan servo internal current** (serial-bus feedback, if available).
- Add a clear “what to display/log/alert on” plan (avg/peak, thresholds, debounce).
"""

# ---
# 1. CURRENT SENSOR INTEGRATION
# ---

# Firmware (Nano):
#   - Read current sensor (total turret current). Prefer reporting in **milliamps** (mA) to avoid float parsing.
#   - Calibrate conversion from ADC -> amps (offset + scale) and clamp negative noise to 0.
#   - Report at a controlled cadence (e.g., 10–20 Hz) independent of video FPS.
#
# Serial message format (recommended):
#   Keep messages parseable and forward/backward compatible.
#
#   Option A (key=value tokens):
#     "STAT V=12.1 I=850 T=..."  (I in mA)
#
#   Option B (CSV with fixed positions):
#     "STAT,12.1,850,..."  (document the exact index for current)
#
#   Notes:
#   - Include a message prefix (e.g., STAT) so the parser can ignore unrelated chatter.
#   - Consider an optional simple checksum when running long cables/noisy environments.
#   - Ensure the message still works when current is omitted (old firmware). In that case, Python sets current=None.

# Python Serial Parsing (MAIN_FILE_SINGLE_CAM.py, serial helpers):
#   - Parse and store:
#     - total_current_ma: int | None
#     - total_current_avg_ma: float (EMA / rolling mean)
#     - total_current_peak_ma: int (windowed max)
#   - Debounce/validate:
#     - Reject outliers (e.g., negative, > plausible max) or mark as invalid.
#     - Maintain last-known-good with timestamp so UI can show “stale” state.
#
#   Example conceptual diff:
#     - old: current_value = None
#     + new: total_current_ma = parsed_from_serial_or_none
#
#   Robustness suggestions:
#   - Do not crash on partial lines; ignore malformed tokens.
#   - When firmware doesn’t include I=..., keep behavior identical to current releases.

# UI/Monitor Panel (ui_builder.py, layout_manager.py):
#   - Display total current in a minimal, non-invasive way.
#   - Prefer showing:
#     - Current (mA) live
#     - Avg (mA) optional
#     - Peak (mA) optional (short window)
#   - Indicate signal quality:
#     - “stale” if last update > N ms
#     - “N/A” if firmware doesn’t support it
#
#   Example diff:
#     - old: self.monitor_panel.addRow('Voltage', self.voltage_label)
#     + new: self.monitor_panel.addRow('Current', self.current_label)

# Logging (optional):
#   - Log current at a lower rate than received (e.g., 1 Hz) to avoid huge logs.
#   - Log both instantaneous and averaged current.
#   - If overcurrent events occur, log an event line with threshold + duration.

# Presets/Settings:
#   - Add thresholds as optional safety/telemetry settings:
#     - current_warn_ma (UI warning)
#     - current_trip_ma (optional “stop firing / stop motion”)
#     - current_trip_hold_ms (debounce so a spike doesn’t instantly trip)
#     - current_stale_ms (marks UI stale)
#
#   Important: “trip” behavior must be explicitly opt-in if hardware differs across builds.

# Documentation:
#   - Update CHANGE_IMPACT_REFERENCE.md, RECENT_UPDATES.json, README.md.

# ---
# 2. PAN SERVO SERIAL BUS UPGRADE
# ---

# Firmware (Nano):
#   - Add serial-bus servo control for Pan.
#   - Maintain PWM for Tilt.
#   - Update serial protocol for new Pan commands.
#
# Monitoring note (serial-bus servo):
#   Many serial-bus servos can report internal telemetry (implementation depends on servo family):
#   - Present position
#   - Load
#   - Temperature
#   - Voltage
#   - **Motor current** (often available, units vary)
#
#   If telemetry is supported:
#   - Decide whether telemetry is read by Nano and forwarded to Python (recommended single serial link)
#     vs Python querying directly (usually not ideal if Nano owns the bus).
#   - Normalize units in Nano before forwarding (prefer mA).

# Python Serial Communication/Servo Logic (MAIN_FILE_SINGLE_CAM.py, servo helpers):
#   - Update Pan control logic to use serial-bus protocol.
#   - Ensure Tilt logic remains PWM-based.
#
#   Monitoring improvement suggestion:
#   - Keep total_current_ma (sensor) and pan_servo_current_ma (telemetry) as separate fields.
#     Total current is system-level truth; pan-servo current is component-level diagnostic.
#
#   Example conceptual diff:
#     - old: send_pwm_command('pan', angle)
#     + new: send_serial_bus_command('pan', angle)

# UI/Monitor Panel:
#   - If telemetry is available, optionally add:
#     - Pan Servo Current (mA)
#     - Pan Servo Temp (°C)
#   - Avoid “double counting” in the UI:
#     - total_current_ma is the sensor value
#     - pan_servo_current_ma is an internal component reading (may not match due to measurement points)

# Presets/Settings:
#   - Add/configure serial-bus servo parameters (ID, speed, acceleration).
#   - Add an opt-in flag for telemetry polling rate (so it doesn’t starve motion commands).

# Testing/Diagnostics:
#   - Update/add a focused diagnostic to validate:
#     - Serial message parsing for I= (total current)
#     - (Optional) telemetry fields for pan servo
#     - Stale detection and threshold alert logic
#   - Add a “simulated serial line” test vector file to exercise parsing without hardware.

# Documentation:
#   - Update CHANGE_IMPACT_REFERENCE.md, RECENT_UPDATES.json, README.md.
#   - Mark Tilt servo upgrade as pending.

# ---
# 3. PENDING: TILT SERVO SERIAL BUS UPGRADE
# ---
#   - Leave all PWM Tilt logic in place.
#   - Document as pending in code and docs.

# Monitoring note (tilt pending):
#   Total current sensor remains valuable even before tilt is upgraded.
#   Ensure any future tilt telemetry doesn’t override/replace the total current reading.

# ---
# 4. AGENT/DEVELOPER CHECKLIST
# ---
#   - Review this diff file and CHANGE_IMPACT_REFERENCE.md before making changes.
#   - Reference this file in all related PRs, commits, and agent-managed blocks.

# Additional checklist items (monitoring-specific):
#   - Decide and document: current units (mA recommended), update rate, stale timeout.
#   - Verify backwards compatibility when current field is missing.
#   - Define thresholds and confirm they are opt-in and hardware-specific.
#   - Confirm UI never blocks on serial reads/telemetry polling.

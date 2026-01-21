"""
Diff file for: PAN & TILT SERVO SERIAL BUS UPGRADE WITH CURRENT MONITORING (2026)
This file documents the code changes required for the following upgrades:
- Upgrade both Pan and Tilt servos to serial bus servos (using debug board)
- Monitor each servo's current consumption separately in the monitor panel
- Monitor total turret current via a dedicated current sensor

This file is for review and planning only. DO NOT apply these changes directly; use as a reference for implementation and code review.
"""

# ---
# 0. SERVO INFORMATION (REQUIRED INPUT)
# ---
# Before implementing the bus protocol or wiring, confirm the exact Pan/Tilt bus servo model/spec.
# Reference images in repo root:
#   - ce27550c941036c537039cccbb3b8236.jpg_2200x2200q80.jpg
#   - 1efe7e1c372359451be7058f9abeda0e.jpg_2200x2200q80.jpg
# Record:
#   - Vendor + exact model name
#   - Control protocol (TTL UART), half-duplex vs full-duplex, baud rate, packet format
#   - Voltage range + recommended PSU
#   - Stall/peak current, torque, speed
#   - Feedback capabilities (position/temp/voltage/current)
# These details determine the correct `setBusServoAngle()` implementation and safety thresholds.

# Known baseline from provided servo info:
#   - Yahboom YB-SD35M serial bus servo ("35kg" class)
#   - Rotation range 0–270°
#   - 3 × HY2.0-3Pin connectors

# ---
# 1. PAN & TILT SERIAL BUS SERVO UPGRADE
# ---

# Firmware (Nano/Debug Board):
#   - Add serial bus servo control for both Pan and Tilt.
#   - Remove all PWM servo control logic.
#   - Update serial protocol to support:
#       * Serial bus commands for both servos
#       * Per-servo current reporting (Pan, Tilt)
#       * Total current reporting
#   - Document new protocol in README.md and CHANGE_IMPACT_REFERENCE.md

# Python Serial Communication/Servo Logic (MAIN_FILE_SINGLE_CAM.py, servo helpers):
#   - Update all Pan and Tilt control logic to use serial bus protocol.
#   - Remove all PWM-based logic for both axes.
#   - Parse and handle per-servo current values and total current from serial messages.
#   - Example diff:
#     - old: send_pwm_command('tilt', angle)
#     + new: send_serial_bus_command('tilt', angle)
#     - old: parse only voltage from serial
#     + new: parse pan_current, tilt_current, total_current

# UI/Monitor Panel (ui_builder.py, layout_manager.py):
#   - Add fields to display Pan current, Tilt current, and Total current.
#   - Update UI refresh logic to show all three values in real time.
#   - Example diff:
#     - old: self.monitor_panel.addRow('Voltage', self.voltage_label)
#     + new: self.monitor_panel.addRow('Pan Current', self.pan_current_label)
#     + new: self.monitor_panel.addRow('Tilt Current', self.tilt_current_label)
#     + new: self.monitor_panel.addRow('Total Current', self.total_current_label)

# Logging (optional):
#   - Add per-servo and total current readings to log output if enabled.

# Presets/Settings:
#   - Add thresholds/alerts for Pan, Tilt, and Total current if needed.
#   - Document new settings in turret_presets.py and preferred_defaults.json

# Documentation:
#   - Update CHANGE_IMPACT_REFERENCE.md, RECENT_UPDATES.json, README.md, hardware setup docs.
#   - Document new serial protocol, UI changes, and settings.

# Testing/Diagnostics:
#   - Update/add test scripts for serial bus servo control and current monitoring (SERIAL_CONNECTION_TEST.py, servo_fix_test.py).
#   - Add/extend tests to verify correct current reporting and UI updates.

# ---
# 2. AGENT/DEVELOPER CHECKLIST
# ---
#   - Review this diff file and CHANGE_IMPACT_REFERENCE.md before making changes.
#   - Reference this file in all related PRs, commits, and agent-managed blocks.
#   - Confirm all PWM logic is removed and replaced with serial bus logic for both axes.
#   - Confirm per-servo and total current are parsed, displayed, and logged as required.
#   - Update all documentation and test scripts as listed above.

# ---
# 3. IMPACTED FILES/SUBSYSTEMS SUMMARY
# ---
# | Area                | Files/Subsystems Impacted                                 |
# |---------------------|----------------------------------------------------------|
# | Firmware            | Nano/debug board firmware (external, must be documented) |
# | Serial Protocol     | MAIN_FILE_SINGLE_CAM.py, serial helpers, docs            |
# | Servo Logic         | MAIN_FILE_SINGLE_CAM.py, servo_fix_test.py, presets      |
# | UI/Monitor Panel    | ui_builder.py, layout_manager.py, enhancements           |
# | Settings/Presets    | turret_presets.py, preferred_defaults.json               |
# | Logging             | serial_log_*.txt, logging helpers                        |
# | Documentation       | CHANGE_IMPACT_REFERENCE.md, RECENT_UPDATES.json, README  |
# | Testing             | SERIAL_CONNECTION_TEST.py, servo_fix_test.py             |

# ---
# 4. NOTES
# ---
#   - PWM logic for both Pan and Tilt is now obsolete and must be fully removed.
#   - All current monitoring (per-servo and total) must be visible in the monitor panel and available for logging/diagnostics.
#   - All protocol, UI, and settings changes must be fully documented and referenced in all related code and documentation.

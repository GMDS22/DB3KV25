# TOOLTIPS.md

This document centralizes tooltip text and guidance for updating tooltips in the Auto Turret UI.

Purpose
- Make all tooltips readable (light background + dark text) and concise.
- Keep tooltip copy consistent and actionable.
- Give maintainers a single place to update texts used by the runtime helper.

How the app applies tooltips
- `app/MAIN_FILE_SINGLE_CAM.py` contains a helper `_apply_tooltip_styles_and_texts()` which:
  - Sets `QToolTip` font and palette to ensure light background and dark text.
  - Applies a small mapping of common widget attribute-names -> tooltip text (applied at `init_ui`).
- Files like `app/ui_builder.py` and `app/turret_enhancements.py` also set tooltips inline for specific widgets.

Editing guidelines
- Prefer short, imperative sentences that explain:
  1. What the control is, and
  2. What the user should do or the effect (if not obvious).
- Keep length under ~120 characters. Longer explanations belong in documentation, not tooltips.
- Avoid implementation details (e.g., "calls serial.open()") in the tooltip.

Current important tooltip mappings
- `connect_button` / `serial_connect_button`: "Open or close the selected serial port connection."
- `serial_port_combo` / `serial_port_input`: "Select the serial (COM) port for the device."
- `serial_baud_combo` / `serial_baud_input`: "Select the baud rate for the serial connection."
- `serial_output`: "Serial console — incoming and outgoing serial messages appear here."
- `tracking_toggle`: "Enable or disable the autotracking system."
- `aiming_toggle`: "Enable or disable automatic aiming assistance."
- `fire_button`: "Manual fire control (use only when safe)."

Discovered tooltips (audit)

The following tooltips were discovered across the `app/` folder during the audit. Suggested normalized text is provided in the "suggested" column and has been added to `tooltips_changes.csv` for review.

- `sound_checkbox` (app/MAIN_FILE_SINGLE_CAM.py:2940)
  - current: "Toggle UI sound effects (notifications and alerts)."
  - suggested: "Toggle UI sound effects (notifications and alerts)."

- `overshoot_input` (app/MAIN_FILE_SINGLE_CAM.py:4525)
  - current: "Percentage overshoot applied to motion gain (positive -> more aggressive). Applies to all detection modes."
  - suggested: "Percent overshoot applied to motion gain; positive = more aggressive."

- `lost_hold_input` / `hold_infinite_checkbox` (app/MAIN_FILE_SINGLE_CAM.py)
  - current: "When target is lost, hold the last known pan/tilt for this many seconds. 0 = no timed hold." / "When checked, never timeout the held position after target loss. Useful to lock aim at last seen point."
  - suggested: "When target is lost, keep aiming at the last known position for this many seconds (0 = disable)." / "Hold the last known target position indefinitely after loss (no timeout)."

- `aim_aggression_slider` (app/MAIN_FILE_SINGLE_CAM.py:5012)
  - current: multi-line description indicating 0/50/100 values
  - suggested: "How aggressively the turret recenters on target: 0=conservative, 50=balanced, 100=very aggressive (may overshoot)."

- `final_approach_boost_checkbox` (app/MAIN_FILE_SINGLE_CAM.py:5045)
  - current: multi-line description about 2-3x boost
  - suggested: "Enable speed boost and reduced smoothing when the target is very close to improve final centering."

- `lock_target_btn` (app/MAIN_FILE_SINGLE_CAM.py:5636)
  - current: lengthy QUICK STRIKE description
  - suggested: "Snap to the last detected target at maximum speed. If armed, fires automatically when position is reached."

- `fire_indicator` (app/turret_enhancements.py:174)
  - current: "Fire indicator — pulses when a fire is requested (host) and extends when MCU confirms)"
  - suggested: "Indicates a requested fire event from the host. Pulses when a fire is requested and remains extended when the MCU confirms the action."

- Code Fixer tooltips (app/code_fixer.py)
  - apply_fix_btn: current "Load selected fix into the editor" → suggested "Load the selected fix into the editor for review and application."
  - view_full_file_btn: current "Open window showing complete file after fix" → suggested "Open a window showing the complete file after applying the selected fix."
  - refresh_scan_btn: current "Rescan MAIN_FILE.py to update issue list" → suggested "Rescan MAIN_FILE.py to refresh the issues list."
  - copy_btn/paste_btn/clear_edit_btn/format_btn/insert_btn/insert_any_btn: minor wording clarifications suggested; see `tooltips_changes.csv` for full list.

- Checklist Panel (app/checklist_panel.py:109)
  - title: current "Verify code elements and dependencies for app integrity" → suggested "Verify code elements and dependencies to ensure application integrity."

Action taken
- Added all discovered tooltip entries and suggested normalized texts to `tooltips_changes.csv` for review.
- Added app-level mappings to the central `tips` dict in `app/MAIN_FILE_SINGLE_CAM.py` so main window widgets receive consistent tooltip copy at startup.

If you'd like, I can now:
- Apply the suggested wording changes inline across the repo (replace `setToolTip` strings), or
- Keep inline strings as-is and rely on `TOOLTIPS.md` + the CSV as the canonical source for manual updates.


Files updated in this change
- `app/MAIN_FILE_SINGLE_CAM.py` — added `_apply_tooltip_styles_and_texts()` and applied it during `init_ui()`.
- `app/ui_builder.py` — clarified tooltips for sound, hold/hold-infinite controls, and overshoot.
- `app/turret_enhancements.py` — clarified `fire_indicator` tooltip.

How to add or modify a tooltip
1. If the widget is created in `ui_builder.py`, edit its `setToolTip(...)` there.
2. For common widgets that may be created dynamically or in other modules, update the `tips` dict in `_apply_tooltip_styles_and_texts()` in `app/MAIN_FILE_SINGLE_CAM.py`.
3. Run the app and verify the tooltip text is readable and not truncated.

Checklist when updating
- [ ] Keep text concise and informative
- [ ] Use sentence-case and avoid punctuation-heavy text
- [ ] Verify readability with the dark theme (tooltips use light yellow background)

Style suggestions (examples)
- "Toggle UI sound effects (notifications and alerts)."
- "Select the serial (COM) port for the device."
- "When target is lost, keep aiming at the last known position for this many seconds (0 = disable)."

If you want, I can:
- Run a repo-wide pass to replace short/ambiguous tooltips with these improved versions.
- Generate a CSV with (file, line, widget, old_text, new_text) for review before applying changes.

---
Generated on: 2025-12-16

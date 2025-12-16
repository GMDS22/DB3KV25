Precision Mode tooltip additions

These concise tooltip strings were added to the main tooltip mapping in `app/MAIN_FILE_SINGLE_CAM.py`.

- `precision_mode_checkbox`: Enable sub-pixel precision aiming (host-side PID and ROI refinement).
- `precision_roi_input`: ROI size in pixels used for contour/template refinement (larger = more stable, more CPU).
- `precision_kp_input`: Precision PID proportional gain (small values).
- `precision_ki_input`: Precision PID integral gain (helps remove steady-state error).
- `precision_kd_input`: Precision PID derivative gain (damps oscillation).
- `precision_hfov_input`: Approximate camera horizontal field-of-view in degrees (used to convert pixels → degrees).
- `precision_max_step_input`: Maximum degrees the precision PID may command per frame (safety clamp).

Notes:
- Tooltips use the app-wide light tooltip palette (light yellow background, dark text) for readability in dark theme.
- Keep tooltips short (<= ~120 chars). Longer explanations belong in the user manual.

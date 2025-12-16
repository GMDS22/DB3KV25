Precision Mode: Host-side refinement and PID

Overview

- New optional Precision Mode provides sub-pixel centering and a host-side final-stage PID to improve aiming accuracy.
- Components:
  - Contour-based centroid: already implemented (see CENTROID_CHANGE.md).
  - Precision Mode toggle: `Precision Mode (Enable Precision Mode)` in the `Tracking Behavior` panel.
  - ROI size (`ROI px`): size used to gate/refine the precision activation (default 48 px).
  - Precision PID (`Kp`, `Ki`, `Kd`): small-gain PID applied only when the target is near the center.
  - HFOV input (`HFOV°`): approximate horizontal field of view used to convert pixel error → degrees.
  - Max°/frame: clamps per-frame PID output to a safe small step (default 1.0°).

How it works

1. When Precision Mode is enabled and the detected target is within the activation radius
   (default: 3 × deadzone or ROI size), a pixel→degree conversion is computed from the
   configured HFOV and the current frame width.
2. A small PID controller (host-side) computes a corrective delta in degrees for both pan
   and tilt. Integral wind-up is clamped and derivative uses frame-time delta.
3. The PID outputs are clamped by `Max°/frame` to avoid aggressive micro-movements.
4. The PID correction replaces the micro-adjustment logic so the final convergence is
   smoother and reduces steady-state error even when the MCU accepts integer-degree commands.

Safety & Tuning

- Start with conservative PID gains (defaults: Kp=0.02 Ki=0.001 Kd=0.005) and `Max°/frame=1.0`.
- If oscillation occurs, reduce Kp or Kd and/or lower `Max°/frame`.
- `HFOV°` should approximate the camera lens HFOV for best conversion; if unknown start with 90°.
- Precision Mode is opt-in and off by default.

Next steps / Enhancements

- Add a UI diagnostic readout showing PID outputs and refined centroid (helpful for tuning).
- Implement ROI-based phase-correlation template refinement to further improve sub-pixel accuracy.
- If pan encoder is available, add symmetric encoder-based PID for true closed-loop on pan.

Files changed

- `app/MAIN_FILE_SINGLE_CAM.py` — centroid refinement, Precision Mode UI, and host-side PID logic.
- `app/CENTROID_CHANGE.md` — notes about centroid change.

Testing

- Launch the app, enable Precision Mode, and observe convergence to center on a static high-contrast target.
- Compare steady-state offset with Precision Mode on vs off and tune PID gains accordingly.

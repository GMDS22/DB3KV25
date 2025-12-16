Precision Mode — User Manual Update

Overview

Precision Mode is an opt-in feature that improves final centering accuracy by combining:
- Contour-based sub-pixel centroid refinement (uses image moments inside the detected box).
- Host-side, final-stage PID controller that converts pixel error to degrees and issues small-degree corrections.

How to use

1. Open the app and go to the Tracking Behavior panel.
2. Enable `Precision Mode` to allow the host-side PID and ROI refinement to run.
3. Tweak `ROI px` to control the refinement area size. Larger ROI may be more stable but uses more CPU.
4. Tune PID gains conservatively:
   - `Kp`: Start at 0.02. Increase slightly if convergence is slow.
   - `Ki`: Start at 0.001. Use sparingly to remove steady-state error.
   - `Kd`: Start at 0.005. Increase slightly to damp small oscillations.
5. Set `HFOV°` to the camera's approximate horizontal field-of-view; this converts pixels → degrees.
6. Set `Max°/frame` to limit how much the precision PID can move the turret per frame (default 1°).

Behavior and safeguards

- Precision Mode only runs when the target is near the center (within the activation radius), so CPU cost is limited.
- The PID uses anti-windup clamps and per-frame limits to avoid aggressive movements.
- Micro-step commands at the MCU level are not used by default; the host accumulates fractional corrections and sends integer-degree commands only when they change.

Tuning tips

- Start with conservative gains and increase Kp gradually while observing convergence.
- If oscillation occurs, reduce Kp and/or increase Kd.
- Increase `ROI px` if centroid is noisy; reduce it if CPU usage is too high.

Files changed

- `app/MAIN_FILE_SINGLE_CAM.py` — Precision Mode UI, centroid refinement, host-side PID.
- `app/CENTROID_CHANGE.md` — explanation of centroid refinement implementation.
- `app/PRECISION_MODE.md` — short guide on the feature and testing tips.
- `app/TOOLTIPS_ADDITIONS.md` — added tooltip text for precision widgets.

If you want, I can add an on-screen diagnostics widget showing refined centroid and PID outputs for live tuning.

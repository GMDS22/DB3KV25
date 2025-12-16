Centroid Refinement Change

Summary

- Implemented contour-moment based centroid extraction for detections in `MAIN_FILE_SINGLE_CAM.py`.
- The code attempts to compute a contour centroid inside the detected bounding box (ROI) using `cv2.moments` on an Otsu-thresholded ROI.
- If the contour/moment calculation fails (no contours, too small ROI, or any exception), the code safely falls back to the original box center (x + w/2, y + h/2).

Why

- Bounding-box center may be biased for asymmetric or occluded objects. Using contour moments provides a more accurate, sub-pixel centroid which reduces steady-state aiming error.

Notes & Behavior

- The change is low-risk and only runs when the ROI is at least 3×3 pixels and `frame1` is available.
- The ROI is clipped to frame bounds to avoid indexing errors.
- CPU cost is small since the operation is limited to the detected box; if performance issues appear, we can gate this behind a user toggle `precision_mode`.

Next steps (recommended)

1. Run the app and test with a static target to confirm reduced steady-state offset.
2. If desired, add a UI toggle to enable/disable centroid refinement and add ROI-based sub-pixel refinement (phase-correlation / template matching) as a further step.
3. Optionally implement a final-stage small-gain PID using the refined centroid to improve convergence.

File changed: `app/MAIN_FILE_SINGLE_CAM.py` (centroid computation near detection handling).
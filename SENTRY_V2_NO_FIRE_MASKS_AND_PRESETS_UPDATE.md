# Smart Sentry v2 Presets and No-Fire Mask Groundwork

## What Changed

- Detection presets in `app/sentry_v2/sentry_v2_tab.py` were retuned so each preset behaves more distinctly instead of clustering around similar thresholds.
- Target-filter presets now separate permissive, class-specific, small-target, and large-close use cases more clearly.
- Threat-AI presets now bias more aggressively toward their intended priority model such as centerline snapping, speed chasing, class-first ranking, or large-target preference.
- Engagement presets were spread further apart so `Demo Track Only`, `Indoor Precision`, `Balanced Response`, `Outdoor Chase`, and `Saturation Burst` each produce visibly different aim, settle, cooldown, and firing behavior.
- Bus-servo move-time presets were widened to make movement style differences easier to see.

## No-Fire Mask Groundwork

- Added persistent no-fire-mask config support in `app/sentry_v2/sentry_v2_config.py`.
- Added angular mask math helpers in `app/sentry_v2/sentry_v2_no_fire_masks.py`.
- Added planner-level gating in `app/sentry_v2/engagement_planner.py` so targets whose planned aim point falls inside a no-fire mask are skipped.
- Added engine-level gating in `app/sentry_v2/sentry_v2_engine.py` so auto-fire is blocked if the current aim is inside a no-fire mask.
- Added overlay rendering in `app/sentry_v2/sentry_v2_overlay.py` so visible projected masks can be drawn over the live video.
- Added `show_no_fire_masks` and `no_fire_masks` to the saved Sentry v2 settings file.
- Added a first usable Guard-tab editor flow in `app/sentry_v2/sentry_v2_tab.py`: operators can name a mask, enable capture, click the live video to place vertices, right-click to finish a polygon, and enable/disable or remove saved masks.
- Added explicit status feedback when a no-fire mask is actively blocking the current aim/fire path, plus log entries when a blocking mask becomes active or clears.
- Added a temporary `Trace mask diagnostics` toggle in the Guard tab. When enabled, the log records change-only snapshots of current pan/tilt, the active blocking mask, and per-mask projected visible-point counts so live projection and block behavior can be verified during runtime.
- Added a `Dump Mask Snapshot` button in the Guard tab to force one immediate mask trace entry on demand during testing, even if the state has not changed.

## Video Canvas Groundwork

- Added `app/sentry_v2/sentry_v2_video_canvas.py` as the new live-video widget foundation.
- `app/sentry_v2/sentry_v2_tab.py` now uses this canvas for frame display instead of writing scaled pixmaps directly into a plain `QLabel`.
- The canvas now supports the first interactive editing path for no-fire masks through live-frame click capture.
- Sentry v2 now includes an optional engaging-state scope-view mode with a round scope window and adjustable vignette opacity.
- Richer polygon editing is still not finished.

## Scope View

- Added persisted scope-view settings in `app/sentry_v2/sentry_v2_config.py`, `app/config/sentry_v2_settings.json`, and `app/sentry_v2/config/sentry_v2_defaults.json`.
- Added Guard-tab controls in `app/sentry_v2/sentry_v2_tab.py` for:
	- enabling scope view during `ENGAGING`
	- scope radius percentage
	- vignette opacity percentage
- Added display-only scope rendering in `app/sentry_v2/sentry_v2_overlay.py`.
- Scope view is applied only to the final display frame after detection and engagement logic already ran, so it should not alter tracking math.
- Entering and leaving scope view is logged from Sentry v2 state transitions to simplify live verification.

## Troubleshooting Notes

- No-fire masks are stored in angular space, not only frame pixels. If a projected mask appears misplaced, verify guard/home calibration, current pan/tilt telemetry, and camera HFOV/VFOV values first.
- A mask can block planning and also block firing at the current aim point. If auto-fire appears silent, check whether the current target is inside a projected mask.
- The status panel now reports the active blocking mask by name. If fire appears suppressed, check that line before assuming comms or trigger issues.
- `Trace mask diagnostics` is intended for live verification. It logs only when the mask snapshot changes, so it should be readable during testing without constant spam.
- `Dump Mask Snapshot` is useful when you want a single checkpoint in the log after moving the turret, changing camera view, or loading a saved mask.
- If scope view appears at the wrong size, check `Scope radius (%)` first before changing overlay or FOV settings.
- If scope view appears too dark or too bright outside the circular window, check `Vignette opacity (%)` before assuming the camera feed is failing.
- Scope view only activates in Sentry v2 when the engine enters `ENGAGING`. If the checkbox is enabled but the effect never appears, confirm the state log is actually reaching `ENGAGING`.
- Projected mask overlays depend on live frame size. If the camera source changes resolution, confirm the guard frame width and height match the active stream.
- Preset changes affect operator feel immediately, especially movement timing and fire lock tolerance. Re-test any previous tuning assumptions after changing presets.

## Current Scope Boundary

- Finished in this update: preset differentiation, no-fire-mask persistence/helpers/planner+fire blocking, overlay support, video-canvas foundation, a first live-click mask creation workflow, and engaging-state scope-view visuals with adjustable radius and vignette opacity.
- Not finished in this update: richer polygon editing tools, vertex dragging, polygon rename/edit dialogs, and any expanded scope-view variants beyond the current engaging-state round scope mode.
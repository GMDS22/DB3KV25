# Smart Sentry v2 Scope View Troubleshooting and Backtracking

## Feature Summary

Sentry v2 now supports an optional display-only scope mode that activates while the engine is in `ENGAGING`.

- Normal video remains unchanged while not engaging.
- During `ENGAGING`, the final display frame is transformed into a round scope view.
- The scope radius is adjustable.
- The outside vignette opacity is adjustable.
- Detection and engagement logic continue to run on the original frame data.

## Files Changed

- `app/sentry_v2/sentry_v2_config.py`
- `app/config/sentry_v2_settings.json`
- `app/sentry_v2/config/sentry_v2_defaults.json`
- `app/sentry_v2/sentry_v2_tab.py`
- `app/sentry_v2/sentry_v2_overlay.py`
- `SENTRY_V2_NO_FIRE_MASKS_AND_PRESETS_UPDATE.md`
- `RECENT_UPDATES.json`

## Config Keys

- `scope_view_enabled`
- `scope_radius_pct`
- `scope_vignette_opacity`

These live at the top level of Sentry v2 config beside other overlay flags.

## UI Location

Guard tab:

- `Enable scope view during ENGAGING`
- `Scope radius (%)`
- `Vignette opacity (%)`

## Runtime Behavior

- Scope view is applied only in the display path after `overlay.draw(...)`.
- The activation gate is the Sentry v2 engine state `ENGAGING`.
- State transitions log when scope view turns on and off.

## Troubleshooting

### Scope view never appears

- Confirm `Enable scope view during ENGAGING` is checked.
- Confirm the Sentry v2 status/log actually enters `ENGAGING`.
- If the system is only guarding or returning, scope view will not activate.

### Scope view appears too small or too large

- Adjust `Scope radius (%)`.
- The radius is relative to `min(frame_width, frame_height)` of the current display frame.

### Scope view looks too dark outside the circle

- Reduce `Vignette opacity (%)`.
- `100%` produces the strongest darkening outside the scope.

### Scope view seems to affect tracking

- It should not. The effect is display-only.
- Verify the display transform is still applied after `overlay.draw(...)` in `app/sentry_v2/sentry_v2_tab.py`.
- Verify detector and engine updates still occur before the scope-view transform.

### Scope view activates at the wrong time

- Check the state transition log entries.
- The intended behavior is `ENGAGING` only.
- If a different state should also use scope view later, that should be a separate change rather than modifying the current intent silently.

## Backtracking Guide

If this feature needs to be disabled or rolled back quickly:

### Soft disable only

- Uncheck `Enable scope view during ENGAGING` in the Guard tab.
- Or set `scope_view_enabled` to `false` in `app/config/sentry_v2_settings.json`.

### Code rollback points

1. Remove config keys from:
   - `app/sentry_v2/sentry_v2_config.py`
   - `app/config/sentry_v2_settings.json`
   - `app/sentry_v2/config/sentry_v2_defaults.json`
2. Remove Guard-tab controls and handlers from:
   - `app/sentry_v2/sentry_v2_tab.py`
3. Remove display-path activation call from:
   - `app/sentry_v2/sentry_v2_tab.py`
4. Remove `apply_scope_view(...)` from:
   - `app/sentry_v2/sentry_v2_overlay.py`

## Safe Verification Steps

1. Enable scope view in Guard tab.
2. Start a session that can enter `ENGAGING`.
3. Watch the log for:
   - `State: ... -> ENGAGING`
   - `Scope view: ON (ENGAGING display mode)`
4. Adjust radius and vignette while engaging.
5. Exit engagement and confirm:
   - `Scope view: OFF (normal video restored)`

## Current Limits

- This is not a zoom scope.
- This does not add alternate scope themes.
- This does not change targeting math, detection pause logic, or fire gating behavior.
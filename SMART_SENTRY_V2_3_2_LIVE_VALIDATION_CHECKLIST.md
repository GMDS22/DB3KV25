# Smart Sentry v2.3.2 Live Validation Checklist

Use this after packaging the desktop app and before treating the v2.3.2 build as release-ready.

## 1. Launch And Identity

1. Launch the packaged app from the v2.3.2 release folder on `F:`.
2. Confirm the window title reads `SMART SENTRY V2.3.2`.
3. Confirm the hero title in the app matches the same release family.
4. Confirm the app opens without import errors, missing-model crashes, or immediate status-panel exceptions.

## 2. Connection And Status Surface

1. Connect using the intended release topology.
2. Confirm connection status goes green for the expected live links.
3. Confirm the `Last:` command line stays readable while tracking is active.
4. Confirm automatic tracking movement does not spam or rapidly overwrite that command-status line.
5. Confirm manual actions such as Home, Move to Guard, Sweep, Sound, or safety changes still update the visible command-status line.

## 3. Scope View

1. Enable the toggleable scope view.
2. Force an ENGAGING state with a valid target.
3. Confirm the scope reticle has a white outer ring, black inner ring, black crosshair arms, and no filled center dot.
4. Confirm temporary firing feedback still flashes without permanently changing the neutral reticle styling.

## 4. Threat AI Status

1. Open the Threat AI page.
2. Confirm the saved-data and model-status text is visible.
3. Confirm `Open ML Folder` appears only when real saved data or model artifacts exist.
4. Confirm the explanatory text about weighted scoring and optional ML refinement is present.

## 5. Preview Smoothness

1. Use Frame Difference mode with scene motion.
2. Confirm the live preview continues updating smoothly during motion activity.
3. Confirm detection and tracking responsiveness remain intact while the smoother preview path is active.

## 6. Adaptive Loss Recovery

1. Set guard mode to fixed/static guard.
2. Save a known guard pan and tilt position.
3. Use Frame Difference mode and acquire a moving target away from guard home.
4. Let Smart Sentry enter tracking or engaging state.
5. Remove the target from view.
6. Confirm Smart Sentry performs a bounded recovery path rather than freezing at the last off-home position.
7. While recovery is active, introduce a clearly stronger visible target.
8. Confirm Smart Sentry can hand off quickly to that visible target instead of finishing the entire old recovery pattern first.
9. Repeat the test without introducing any new strong target.
10. Confirm Smart Sentry now performs the more persistent bounded reacquire search around the last loss area.
11. Confirm the turret returns to the configured guard position after the recovery sequence completes when fixed/static guard is active.
12. Repeat once more to ensure the behavior is stable across two consecutive target-loss events.

## 7. Manual Control Regression Check

1. Test Home.
2. Test Move to Guard.
3. Test one manual step in each axis.
4. Confirm manual movement still works even after an adaptive target-loss recovery cycle.
5. Confirm manual actions remain visible in the readable command-status surface.

## 8. Release Sign-Off

Treat the package as ready only if all of the following are true:

1. Release identity matches `2.3.2` in the window title and version markers.
2. Connection and status surfaces are readable under live tracking.
3. Scope view matches the approved monochrome contract.
4. Adaptive loss recovery can both hand off quickly and return to guard cleanly when no new target takes over.
5. No new runtime import, JSON, or UI errors were observed during the validation pass.
# Prediction Validation Test Guide

## Purpose

This guide describes how to validate prediction and tracking performance using the passive prediction diagnostics layer **without modifying turret behavior**.

## Safe test configuration

Before testing, confirm these settings:

- `speed_debug_prediction = true`
- `speed_adaptive_lead_enabled = false`

Keep all other aiming and tracking settings unchanged for the duration of the test.

## Safety rule

During testing:

- do **not** change PID settings
- do **not** change detection parameters
- do **not** enable adaptive lead yet

This keeps the test observational only and preserves baseline runtime behavior.

## Test scenarios

Run the following scenarios in order:

1. **Stationary target**
   - Hold a visible target still near the center of the frame.
   - Observe whether prediction error remains low and stable.

2. **Slow lateral motion**
   - Move the target slowly left-to-right or right-to-left.
   - Confirm samples accumulate and prediction error remains controlled.

3. **Fast lateral motion**
   - Move the target quickly across the frame.
   - Expect larger error than slow motion, but verify tracking remains stable.

4. **Target approaching camera**
   - Move the target toward the camera so apparent box size and centroid shift change rapidly.
   - Watch for higher prediction error due to scale and perspective change.

5. **Target leaving frame and reappearing**
   - Let the target exit the frame, then re-enter.
   - This helps reveal hold-window reuse behavior and detection reacquisition behavior.

## Data collection

Use the built-in shortcut:

- `Ctrl+Shift+P`

This prints a short prediction summary.

Record the following values for each scenario:

- sample count
- average prediction error
- median prediction error
- worst prediction error

Recommended practice:

- let each scenario run long enough to gather multiple samples
- record results separately for each scenario
- note whether detections were clearly fresh, reused, or reacquired after loss

## Expected baseline interpretation

These ranges are intended as a practical developer baseline, not a hard pass/fail threshold.

### Low error

Typically means prediction is closely matching the next processed aiming sample.

General interpretation:
- about `0-10 px`
- expected for stationary targets or slow smooth motion

### Moderate error

Typically means prediction is usable but target motion, detector latency, or reuse/caching effects are visible.

General interpretation:
- about `10-30 px`
- expected for moderate motion or partial detector lag

### High error

Typically means prediction is struggling to match the next processed aiming sample.

General interpretation:
- above `30 px`
- may occur during fast motion, depth changes, target loss/reacquisition, reused hold-window boxes, or cached YOLO results

## Important interpretation note

Prediction statistics measure:

- **previous prediction vs next processed aiming sample**

That sample may come from:

- fresh detector output
- reused hold-window detection
- cached YOLO detection

So a high error does **not** always mean prediction math is wrong. It may also indicate stale or reused detection input.

## Suggested test record format

For each scenario, record:

- scenario name
- detection mode in use
- sample count
- average error
- median error
- worst error
- notes about target loss, hold behavior, or cached detections

## Exit criteria

The test is complete when:

- all five scenarios have been run
- prediction statistics have been captured with `Ctrl+Shift+P`
- observations have been recorded without changing runtime control behavior

## Reminder

This guide is for **passive validation only**.

Do not tune PID, change detection thresholds, or enable adaptive lead until baseline diagnostics have been collected and reviewed.

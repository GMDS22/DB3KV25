# SMART SENTRY Runtime Data Export

## Purpose

Smart Sentry exposes a runtime data export from the Controls page so the current session can be captured as structured evidence for debugging, tuning, and future AI-assisted analysis.

This export path is intentionally read-only.

- It captures runtime state.
- It does not change detector behavior.
- It does not change engine decisions.
- It does not change transport selection.
- It does not change firing or motion logic.

Any future AI analyzer must consume these exported artifacts without becoming part of the live control loop unless a later change explicitly introduces a separate reviewed control path.

## Operator Controls

The Controls page exposes two related actions.

1. `Export Runtime Data`
   Writes a timestamped JSON payload plus a Markdown summary into the runtime snapshot folder.

2. `Open Export Folder`
   Opens the folder that contains the exported runtime data files so the operator can inspect, copy, or hand them to an external analyzer.

## Current Export Scope

The export is assembled from the existing live runtime state in `app/sentry_v2/sentry_v2_tab.py`.

Current payload coverage includes:

- Full config snapshot from the active Smart Sentry runtime config object
- Engine state including state name, queue state, active order, visible targets, qualified target count, no-fire-mask name, and loss-recovery state
- Communication telemetry including connection status, transport mode, servo feedback, IO runtime telemetry, and bridge capability telemetry
- Camera status including current source, requested and selected resolution, frame dimensions, and recovery counters
- YOLO status including selected model, loaded model path, classes, and thresholds
- External file references for the active settings, presets, prompted-target library, snapshot folder, and model directories
- Recent runtime log lines from the UI log surface

## Future AI Analyzer Guardrails

Future AI-related work should treat the runtime export as an evidence source, not a behavior source.

Required guardrails:

1. Export generation must remain side-effect free apart from writing files and UI log messages.
2. Export collection must only read existing runtime state or call snapshot-style helper methods.
3. The analyzer should operate on exported files or copied in-memory payloads, not mutate live config or engine state during capture.
4. Any future AI recommendation system should propose changes separately from the export path.
5. Any future AI auto-apply mechanism must be introduced as a separate reviewed feature, not piggy-backed onto export.

## Recommended Usage

Use runtime data export when you need a precise record of what the app was doing at a specific moment, especially for cases such as:

- Model-selection verification
- Transport or hardware mismatch diagnosis
- Camera recovery failures
- False positives or missed detections
- Precision aiming tuning review
- External AI or offline analysis workflows

## Output Location

Exports are written under the runtime snapshot folder used by Smart Sentry:

- JSON: `snapshots/sentry_v2_runtime_snapshot_YYYYMMDD_HHMMSS.json`
- Markdown: `snapshots/sentry_v2_runtime_snapshot_YYYYMMDD_HHMMSS.md`

The folder-open control exists so the operator can jump directly to this location after export.
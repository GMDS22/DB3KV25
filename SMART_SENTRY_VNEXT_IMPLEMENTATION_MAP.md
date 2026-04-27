# SMART SENTRY vNext Implementation Map

Purpose: convert the vNext tracking proposal into a concrete file-and-function implementation plan, with phase 1 focused on overshoot reduction and first-lock stability.

Status: planning document. This file maps future edits; it is not the live runtime contract.

---

## 1. Phase Order

### Phase 1: Pose Authority And First-Lock Stability

Goal:

- stop precision aiming from steering off optimistic commanded pose when measured feedback is still settling
- remove the immediate blind first correction on new engagements
- enforce a real coarse-acquire then settle then precision handoff

Primary files:

- `app/sentry_v2/sentry_v2_engine.py`
- `app/sentry_v2/sentry_v2_tab.py`
- `app/sentry_v2/sentry_v2_config.py`

### Phase 2: Prediction Maturity And Tracker Stability

Goal:

- make lead compensation depend on stable motion history
- reduce track-ID churn during follow and reacquire

Primary files:

- `app/sentry_v2/threat_scorer.py`
- `app/sentry_v2/simple_tracker.py`
- `app/sentry_v2/sentry_v2_engine.py`

### Phase 3: Scene Memory Collection And Diagnostics

Goal:

- collect class-specific scene priors without changing live authority rules

Primary files:

- `app/sentry_v2/scene_memory.py` (new)
- `app/sentry_v2/sentry_v2_engine.py`
- `app/sentry_v2/sentry_v2_tab.py`
- `app/sentry_v2/sentry_v2_config.py`
- `SMART_SENTRY_RUNTIME_DATA_EXPORT.md`

### Phase 4: Scene Memory Reacquire Bias

Goal:

- use bounded scene memory only to reorder persistent reacquire and candidate ranking

Primary files:

- `app/sentry_v2/sentry_v2_engine.py`
- `app/sentry_v2/threat_scorer.py`
- `app/sentry_v2/scene_memory.py`

---

## 2. Phase 1 File And Function Map

### `app/sentry_v2/sentry_v2_engine.py`

#### `__init__`

Add runtime state for:

- last commanded pan/tilt
- optional measured/control pose tracking
- acquire/settle timing for engagement startup

Reason:

- the engine currently has only one live pose reference, but real runtime behavior already distinguishes between commanded and measured position on the tab side

#### `_move_turret()`

Change responsibility to:

- always emit the commanded move
- store commanded pose separately
- stop blindly replacing the live control pose when measured feedback is active and the move has not settled yet

Reason:

- this is the main optimistic-pose write that feeds early overshoot

#### `_start_order_engagement()`

Change startup behavior to:

- always begin with a coarse acquire move
- stop jumping straight into precision phase on the first engagement frame

Reason:

- current direct precision entry allows a first correction before the turret has actually settled on the new target

#### `_update_engaging()`

Refactor startup phases into:

- acquire or coarse move phase
- settle gate before precision
- precision only after settle criteria are met

Reason:

- this is the controlling phase transition for first-lock behavior

#### `_enter_precision_phase()`

Change precision entry to:

- initialize precision state only
- avoid issuing an immediate blind correction on phase entry
- let the normal precision update loop own the first measured correction after settle

Reason:

- the current immediate correction is the second half of the first-lock overshoot path

#### `_record_active_target_solution()`

Audit to ensure:

- recorded aim anchors are based on the correct live control pose
- last-known aim points remain useful for loss recovery after the pose-authority change

### `app/sentry_v2/sentry_v2_tab.py`

#### `_on_engine_move()`

Audit command dispatch timing so the engine phase changes still match the real transport behavior after phase-1 edits.

#### `_queue_move_command()`

Keep existing deferred-move behavior, but verify it still works when the engine no longer assumes commanded pose equals settled pose.

#### `_sync_engine_pose_from_feedback()`

Change to:

- feed measured pose into an engine helper instead of mutating `engine.current_pan/current_tilt` directly

Reason:

- measured pose should become an explicit engine input, not an out-of-band variable overwrite

#### `_resync_engine_pose_after_deferred_move()`

Change to:

- use the same engine helper for measured or fallback pose resync

Reason:

- phase 1 should keep one consistent pose update path

### `app/sentry_v2/sentry_v2_config.py`

Phase-1-only config additions are optional. If needed, keep them minimal and bounded:

- acquisition settle delay
- startup settle tolerance

Do not add a large new tuning surface in phase 1.

---

## 3. First Validation Targets For Phase 1

After each phase-1 edit, prefer these checks in order:

1. narrow import smoke for `sentry_v2_engine.py` and `sentry_v2_tab.py`
2. targeted Python snippet that verifies a new engagement starts in coarse acquire instead of direct precision correction
3. targeted Python snippet that verifies feedback pose can update the engine without relying on `_move_turret()` to overwrite the live control pose

---

## 4. Phase 1 Done Criteria

Phase 1 is complete when all of the following are true:

- a new engagement no longer enters precision with an immediate blind correction
- the engine distinguishes commanded move output from live control pose when measured feedback is available
- tab feedback sync updates the engine through one explicit pose-update path
- import smoke passes for touched modules
- live docs still describe the current runtime accurately enough for the implemented subset
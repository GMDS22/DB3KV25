# SMART SENTRY vNext Tracking And Scene-Memory Proposal

Purpose: document the next-version tracking, aiming, and behavior improvements that were proposed during the v3.5.0 analysis pass, including the new scene-memory idea for smarter target reacquire.

Status: proposal only. Nothing in this file is the active runtime contract yet.

Primary rule: the current live behavior still remains owned by `SMART_SENTRY_AUTOTRACKING_BEHAVIOR_BLUEPRINT.md` and `SMART_SENTRY_MANUAL.md`. This file is for planned work, rollout order, and implementation guardrails.

---

## 1. Why This Proposal Exists

The current Smart Sentry stack already has a strong end-to-end chain:

`Detection -> Filter -> Score -> Plan -> Aim -> Precision Refine -> Fire Gate -> Return/Hunt`

But the current analysis found four recurring limits that reduce first-lock quality and reacquire intelligence:

1. first contact can overshoot because commanded pose and measured pose are not treated as the same thing
2. first-lock precision can still start too aggressively for immature tracks
3. predictive lead can react to very recent noisy motion instead of mature stable motion
4. after loss, the system knows the last target position and direction, but it does not yet remember longer-term scene habits for a class or route

This proposal fixes those limits without changing the core safety rule that detection, tracking, and firing must stay separate authorities.

---

## 2. Proposed vNext Tracking Improvements

### A. Single Pose Authority

Current issue:

- the engine can treat the commanded pan/tilt as if it is already the current pose
- the tab then tries to repair that with delayed feedback sync and deferred-move logic
- this creates a short window where the controller may steer from optimistic pose instead of settled pose

vNext change:

- separate `commanded_pose`, `estimated_pose`, and `measured_pose`
- make measured debug-board feedback the only authoritative control pose during live precision tracking whenever feedback is available
- keep commanded pose only for transport and move-settle decisions

Expected benefit:

- less first-lock overshoot
- less controller self-chasing during fast presets
- cleaner handoff between movement, settle, and refinement

### B. Explicit Acquire -> Settle -> Precision Staging

Current issue:

- first acquisition is still a direct center-to-angle snap plus immediate precision correction

vNext change:

- split engagement into three explicit tracking stages before fire
- `acquire`: bounded coarse move toward target center, predictive lead disabled
- `settle`: short hardware-confirmation window or remaining-error confirmation window
- `precision`: existing fine centering logic, only after the target and hardware state are mature enough

Expected benefit:

- removes the current overly eager first correction
- gives fast but more trustworthy opening lock-on

### C. Gain Scheduling Instead Of One Response Shape

Current issue:

- the same family of response rules is being asked to handle both large first-contact errors and small center-lock errors

vNext change:

- use coarse-response limits for large errors
- use damped proportional response for medium errors
- use the current precision loop only near center

Expected benefit:

- faster acquisition without the opening snap feeling reckless
- tighter near-center behavior without slowing overall response

### D. Prediction Only For Mature Tracks

Current issue:

- predictive lead is useful, but early velocity estimates are still noisy because they can be derived from only very recent history

vNext change:

- require minimum track maturity before prediction can affect aim
- compute direction from a short stable window instead of only the latest displacement
- lower prediction authority automatically when track confidence or history quality falls

Expected benefit:

- fewer wrong-direction opening moves
- less jumpiness on partial detections or brief flicker

### E. Tracker Stability Upgrade

Current issue:

- the current greedy bbox tracker is lightweight and useful, but track-ID churn still costs reacquire stability

vNext change:

- either strengthen the current tracker with short-horizon velocity and IoU continuity, or replace it with a stronger motion-model association path

Expected benefit:

- less false "new target" behavior for the same object
- smoother follow and better reacquire continuity

### F. UI Simplification For Safer Tuning

Current issue:

- too many low-level knobs can interact in ways that are hard to reason about quickly

vNext change:

- keep a simple operator layer with a few behavior personalities such as `Stable`, `Balanced`, and `Fast`
- keep the current advanced parameters behind an expert section
- surface live tracking health, not just offline export buttons

Expected benefit:

- fewer unstable combinations chosen by accident
- faster tuning cycles during live tests

---

## 3. New Scene-Memory Idea

### Goal

Make Smart Sentry behave more intelligently after loss by remembering where certain classes usually appear, where they are usually lost, and what direction they usually travel.

Examples:

- if birds usually enter from the upper-left and move rightward, loss recovery should bias that corridor first
- if rats usually stay near the lower edge and disappear into the same corner, persistent reacquire should search that area before widening elsewhere
- if people in a given camera setup usually cross a doorway left-to-right, reacquire should favor that doorway band and heading corridor

### What This Memory Is

This is a bounded scene prior, not a new detector and not a fire authority.

It should remember only patterns such as:

- class name
- source family when relevant
- normalized area-of-frame heatmap for where that class is usually seen
- loss heatmap for where it is usually lost
- heading histogram for common movement direction
- dwell or hold zones where the class often remains stable
- optional time-decayed route segments between seen and lost points

### What This Memory Must Not Do

- it must not create a target when nothing credible is detected
- it must not bypass filter, scoring, or fire gate rules
- it must not override a visible stronger target during rapid handoff
- it must not turn sparse historical noise into permanent bias
- it must not be allowed to expand search beyond the existing bounded-recovery rules

---

## 4. How Scene Memory Fits The Current Behavior

Yes, it can be implemented cleanly with the proposed updates above.

The best fit is as an advisory layer inside target-loss recovery and optional guard scanning, not inside fire gating.

### Best Integration Points

1. `app/sentry_v2/sentry_v2_engine.py`
   Use scene memory in `_capture_loss_recovery_context()`, `_find_reacquire_target()`, `_select_loss_recovery_protocol()`, and persistent recovery path generation.

2. `app/sentry_v2/threat_scorer.py`
   Keep the current threat score mostly unchanged. At most, add a very small non-firing scene familiarity factor for tie-breaking, not for authority.

3. `app/sentry_v2/sentry_v2_tab.py`
   Add operator toggles, reset/export tools, and a compact live diagnostics surface.

4. `app/sentry_v2/sentry_v2_config.py`
   Add explicit config gates so the feature can be enabled, bounded, tuned, or disabled without changing core tracking.

5. `SMART_SENTRY_RUNTIME_DATA_EXPORT.md`
   Export memory snapshots for analysis, but do not make runtime export the live memory store.

### Best Use Cases In Current Behavior

#### A. Persistent Reacquire Search

This is the strongest fit.

Current persistent reacquire already searches around the last known aim anchor. Scene memory should adjust the search order, not replace the anchor.

That means:

- first search the last live anchor
- then bias the next few search points toward historically strong zones for that class
- favor the historically common heading corridor when the recent heading and class memory agree
- if history is weak, fall back to current bounded search ordering

#### B. Reacquire Candidate Ranking

Current reacquire ranking already uses class, source, distance, IoU, area similarity, and threat score. Scene memory can contribute a small additional bias term.

That means:

- candidates appearing inside historically common zones for that class score slightly better
- candidates moving along historically common direction corridors score slightly better
- the bias stays smaller than live spatial continuity and class continuity

#### C. Guard / Patrol Bias

Optional later phase only.

The guard or patrol system can gently bias its watch direction toward historically active corridors for the currently selected profile. This should remain subtle so Smart Sentry does not stop behaving like a sentry and start staring at one old hotspot forever.

---

## 5. Conflict-Avoidance Rules

To avoid breaking existing behavior, scene memory should follow these rules.

1. Advisory only. It may reorder or bias search, but it cannot create engagement authority by itself.
2. Loss recovery only at first rollout. Do not mix it into fire logic, face suppression, prompted targets, or PIR cue confirmation initially.
3. Bounded search remains bounded. Memory bias may reorder the existing search budget, not enlarge it without limit.
4. Strong live evidence wins over old memory. Fresh visible targets, recent heading, and nearby continuity beat historical priors.
5. Class-scoped and profile-scoped. Person routes from one camera setup should not pollute rat routes from another setup.
6. Time decay required. Old habits must fade unless reconfirmed.
7. Resettable by operator. There must be a clear way to clear learned memory for a profile or camera.

If these rules are followed, the feature should not conflict with current filter, score, precision, no-fire mask, or transport behavior.

---

## 6. Recommended Data Model

Recommended new module:

- `app/sentry_v2/scene_memory.py`

Recommended runtime structures:

- `SceneMemoryStore`
- `ClassSceneProfile`
- `SceneHeatmap`
- `HeadingMemory`
- `LossPattern`

Recommended stored keys:

- active release or schema version
- camera source identity
- guard profile or master preset identity when relevant
- class name
- detection source family
- normalized seen heatmap
- normalized loss heatmap
- heading histogram
- total observations
- last updated timestamp
- decay metadata

Recommended persisted file:

- `app/config/smart_sentry_v3_5_0_scene_memory.json`

This should stay separate from the main settings JSON so scene memory can be reset or exported independently.

---

## 7. Recommended Config Additions

Recommended fields for `EngagementConfig` or a dedicated behavior-memory config surface:

- `scene_memory_enabled: bool`
- `scene_memory_loss_bias_enabled: bool`
- `scene_memory_guard_bias_enabled: bool`
- `scene_memory_min_samples: int`
- `scene_memory_decay_days: float`
- `scene_memory_zone_weight: float`
- `scene_memory_heading_weight: float`
- `scene_memory_max_reacquire_bias: float`
- `scene_memory_profile_scope: str`
- `scene_memory_persist_across_runs: bool`

Recommended operator actions:

- enable or disable scene memory
- clear all memory
- clear memory for current class
- clear memory for current profile
- export current memory snapshot

---

## 8. Implementation Order

Recommended rollout order:

1. fix control-side pose authority and acquire/settle/precision staging
2. harden prediction maturity gating and tracker stability
3. add scene-memory collection only, with export and diagnostics
4. add scene-memory bias to persistent reacquire search only
5. add small scene-memory bias to reacquire candidate ranking
6. optionally add subtle guard/patrol bias later if field testing proves useful

Reason:

If scene memory is added before the pose-authority and first-lock issues are cleaned up, it can amplify wrong reacquire moves instead of making the system feel smarter.

---

## 9. File-Level Modification Map

If this proposal is implemented later, the main code surfaces should be:

- `app/sentry_v2/sentry_v2_engine.py`
  - separate measured vs commanded pose usage
  - add acquire/settle/precision phase contract
  - capture scene-memory context during loss
  - bias persistent reacquire ordering and candidate selection

- `app/sentry_v2/engagement_planner.py`
  - keep target-center mapping as the baseline camera model
  - optionally add bounded acquisition-specific damping helpers

- `app/sentry_v2/threat_scorer.py`
  - improve heading stability for prediction maturity
  - optionally add tiny scene familiarity tie-breakers only

- `app/sentry_v2/simple_tracker.py`
  - improve track continuity or replace with a stronger tracker

- `app/sentry_v2/sentry_v2_tab.py`
  - add operator scene-memory controls and diagnostics
  - keep advanced behavior under expert tuning surfaces

- `app/sentry_v2/sentry_v2_config.py`
  - add persisted config for scene memory and staged acquisition behavior

- `SMART_SENTRY_MANUAL.md`
  - document the live contract once implemented

- `SMART_SENTRY_AUTOTRACKING_BEHAVIOR_BLUEPRINT.md`
  - promote scene memory into the live behavior contract only after rollout is verified

- `SMART_SENTRY_RUNTIME_DATA_EXPORT.md`
  - add scene-memory snapshot export fields without turning export into a control path

---

## 10. Bottom Line

The proposed tracking improvements and the new scene-memory idea are compatible.

The safe way to combine them is:

- first make first-lock and pose authority more trustworthy
- then let scene memory influence only bounded reacquire and search ordering
- keep scene memory advisory, decayed, resettable, and clearly lower authority than live evidence

If implemented that way, Smart Sentry should feel noticeably smarter after target loss without weakening the current safety, filter, or fire-gate behavior.
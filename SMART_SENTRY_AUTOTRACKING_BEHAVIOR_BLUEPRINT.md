# Smart Sentry Autotracking Behavior Blueprint

Date: 2026-05-13
Status: Live behavior-contract document for current Smart Sentry tracking, PIR cueing, target-loss recovery, center aim, and fire gating
Audience: Developers, validators, advanced tuners

Purpose: this is the primary behavior-contract file for Smart Sentry target tracking, PIR cueing, target-loss recovery, center-aim logic, and fire gating.

Use this file first whenever:

- tracking behavior feels wrong
- PIR cue or hunt behavior changes
- a target gets a red primary box but the turret does not respond correctly
- presets are being retuned
- an editor needs to understand what must stay true before modifying engine logic

This file is intentionally written as a behavioral spec, not just a feature summary. It describes the intended runtime logic, the real code ownership points, and the places where careless edits commonly cause regressions.

Future-design note: proposed next-version tracking and scene-memory work lives in `SMART_SENTRY_VNEXT_TRACKING_AND_SCENE_MEMORY_PROPOSAL.md`. Do not treat that file as active runtime behavior until the implementation is complete and this blueprint is updated to match.

---

## 1. Primary Runtime Rule

The Smart Sentry turret exists to do one thing reliably:

1. detect something
2. decide whether it is a valid target
3. move the turret so the object center is brought to frame center
4. keep the object centered while it remains valid
5. fire only if the firing gate is enabled and all fire conditions are satisfied
6. return to guard behavior if the object is rejected, lost, or the sequence ends

The aim point is the detected target center, not a guessed offset. In the current implementation this is owned by `app/sentry_v2/engagement_planner.py`, which converts the normalized detection center into pan and tilt error using the configured camera field of view and center-bias values.

If future edits change the aim point away from the target center, that is a behavior-contract change and must be documented here, in the manual, and in the preset descriptions.

---

## 2. Behavioral Chain In Plain Language

The live chain is:

`Detection -> Filter -> Score -> Plan -> Aim -> Precision Refine -> Fire Gate -> Return/Hunt`

The owning runtime files are:

- `app/sentry_v2/sentry_v2_engine.py`: state machine, active target handling, loss recovery, PIR confirmation and scan, fire gating
- `app/sentry_v2/sentry_v2_pir_manager.py`: PIR queueing, debounce, local hunt pattern generation, scan ordering
- `app/sentry_v2/engagement_planner.py`: conversion from target center to pan/tilt command
- `app/sentry_v2/sentry_v2_tab.py`: preset bundles, UI-applied settings, hidden engagement advanced overrides
- `app/sentry_v2/sentry_v2_config.py`: default behavior values and saved settings schema
- `app/sentry_v2/sentry_v2_overlay.py`: visual meaning of guard/engaging/returning colors and primary-target box drawing

The engine is frame-driven. Every camera frame, it filters detections, scores remaining targets, and then chooses state-specific behavior:

- `GUARDING`: watch, patrol, process PIR cues, and promote valid targets into engagement
- `ENGAGING`: aim, refine, optionally fire, recover from temporary loss, or advance queue
- `RETURNING`: go back to guard after an engagement cycle
- `PAUSED`: do nothing

---

## 3. Core Operational Rule

Simple rule:

1. **Detect** — camera sees something
2. **Validate** — check if it's a credible target (class, size, confidence rules)
3. **Track** — move turret to center it on frame
4. **Fire** — only if centered + auto-fire enabled + no safety mask blocks it

**That's it.** Do not block tracking with too many validation gates. Tracking IS validation. Once a target is centered:
- If `auto_trigger_enabled = true`, and the target is reasonably confident, fire.
- If the target disappears while tracking, look for it briefly, then return to guard.
- If the target appears again, switch back to it.
- In patrol guard modes, returning from engagement should resume patrol naturally (no forced home nudge each cycle).

The key principle: **Track first. Fire only if centered and enabled.** Remove unnecessary complexity.

---

## 4. What The Primary Box Color Means

The primary target box is drawn in the overlay and its color is state-driven.

- `GUARDING`: green primary box means the system sees a leading candidate but has not yet promoted it into active engagement
- `ENGAGING`: red primary box means the engine has promoted a target into the active engagement path
- `RETURNING`: yellow primary box means the system is exiting or holding a locked result while leaving engagement

Current source of truth: `app/sentry_v2/sentry_v2_overlay.py`.

### Red-Frame Protocol

If a target has reached the red primary-box state, the turret should already be in the active aiming path.

That means:

- it should not remain parked in the old guard position unless the target is already near-perfectly centered
- it should not wait for PIR logic to finish first
- it should not keep patrolling
- it should not treat the target as advisory only

A red primary box should produce one of two valid outcomes immediately:

1. visible corrective aiming toward the target center
2. no visible movement only because the target is already centered closely enough that the controller outputs near-zero correction

If a red box is present and the turret stays visibly off-target without attempting correction, treat that as a behavior regression and investigate:

- engagement promotion logic
- movement suppression or deferred move handling
- stale feedback gating
- over-strict deadzone or aim-lock tolerances
- preset merge logic

### Return/Home Stability Contract

The `RETURNING` state must complete cleanly into fresh `GUARDING` without re-engaging visible targets. This prevents bounce-back loops where the system returns to guard position, immediately sees a lingering target, and starts returning again.

**Return Completion Rules:**

1. `RETURNING` state finishes into `GUARDING` with cleared queue and cooldown state
2. No automatic re-engagement of visible targets after return completion
3. Direct `hold_guard` moves finalize only after commanded motion duration completes
4. Stale delayed-finalize callbacks are invalidated when newer moves start
5. Post-return detection starts fresh from `GUARDING` after normal cooldown period

**Implementation Points:**
- `app/sentry_v2/sentry_v2_engine.py`: `_update_returning()` clears state on arrival
- `app/sentry_v2/sentry_v2_tab.py`: Token-based callback invalidation for guard moves

---

## 5a. Acoustic Guard Protocol

Acoustic Guard is a sound-triggered non-visual cueing system. It is subordinate to both active visual engagement and active PIR cues.

### Acoustic Guard Contract

When the USB microphone anomaly detector fires:

1. An anomaly event is queued (not acted on immediately).
2. The queue is only consumed when the engine is in `GUARDING` state with no active visual target and no PIR cue in progress.
3. Once started, the acoustic alert executes a two-phase movement sequence while keeping visual detection active.
4. If a visual target is found **at any point** during acoustic movement, the sequence is immediately cancelled and normal engagement takes over.

### Phase 1 — Initial Quick Search

Quick smooth movement through three fixed pan waypoints at the current guard tilt level:

- **45°** → **135°** → **230°**

Movement is smooth and continuous (uses `_patrol_move_toward`, not snap/jump). Speed is high (approximately 2.8× normal guard sweep speed). The intent is a fast but controlled scan that gives the detector a chance to find a target at each zone.

### Phase 2 — Secondary Slow Sweep

If no target is found after the initial search:

- Full-range pan sweep from `pan_min` to `pan_max` at `sweep_speed_dps`.
- Tilt varies ±7° during the sweep to improve vertical coverage.
- This phase is deliberately slow to maximize detection opportunity.
- After the sweep completes, the turret returns to guard position and patrol resumes.

### Acoustic Guard Must Not Behave Like This

- It must not snap-jump to waypoints — movement must be smooth.
- It must not interrupt an active visual engagement.
- It must not interrupt an active PIR cue.
- It must not leave the turret parked at a search waypoint if the sequence ends without a target.
- It must not fire — acoustic events only trigger search movement, not fire gating.

### Acoustic Guard Settings That Matter Most

- `anomaly_threshold_db`: dB above baseline to flag (lower = more sensitive)
- `anomaly_zscore_threshold`: standard deviations above rolling mean (lower = more sensitive)
- `event_cooldown_s`: minimum gap between alert executions
- `sweep_speed_dps`: secondary sweep speed (lower = slower/more thorough)

### Implementation Ownership

- `app/sentry_v2/acoustic_guard.py`: background mic thread, EWMA baseline, anomaly firing
- `app/sentry_v2/sentry_v2_engine.py`: `on_sound_anomaly_detected()`, `_start_sound_alert_sequence()`, `_update_sound_alert_sequence()`, `_build_sound_initial_points()`
- `app/sentry_v2/sentry_v2_config.py`: `AcousticGuardConfig` schema
- `app/sentry_v2/sentry_v2_tab.py`: signal bridge, Guard tab UI group, QA bar toggle button

---

## 5. PIR Cue And Hunt Protocol

PIR is a blind-spot cueing system. It is not a higher-priority authority than a live camera-confirmed active target.

### PIR Contract

When a PIR sensor fires:

1. debounce the sensor event
2. queue the cue event
3. if the system is not already in active engagement, move to that sensor's configured cue pan and tilt
4. hold briefly at the cue center
5. check whether the camera now sees a credible target there
6. if yes, promote that target into the normal engagement path
7. if not, begin a local hunt around the triggered zone
8. if the hunt still finds nothing, explicitly return to guard/home behavior

### PIR Must Not Behave Like This

- it must not permanently park at the cue point after no-detect
- it must not start by re-visiting the same center point again when a multi-point hunt begins
- it must not override a live already-confirmed engagement
- it must not leave static-guard mode parked at the last hunt point when the search fails

### Live PIR Search Shape

The current intended shape is:

1. cue center confirmation
2. immediate first offset move if no target is confirmed
3. denser local hunt biased toward the triggered PIR zone
4. broader mirrored widening only after the local zone has been checked
5. explicit return to guard/home if still no target

This is owned jointly by:

- `app/sentry_v2/sentry_v2_engine.py`
- `app/sentry_v2/sentry_v2_pir_manager.py`

### PIR Settings That Matter Most

- `cue_hold_time_s`: brief pre-hunt dwell only
- `scan_on_no_detect`: whether local PIR hunt is allowed at all
- `scan_pan_range` and `scan_tilt_range`: how large the zone is
- `scan_grid_resolution`: how dense the grid is
- `scan_speed`: apparent hunt tempo
- `search_style`: `hunting` vs `fast_reacquire`
- `search_rounds`: repeated passes of the local-plus-expanding pattern

### Required PIR Feel

Movement should be smooth, deliberate, and obvious enough to see, but not lazy. The system should visibly leave the cue point once no target is confirmed. If it appears to freeze, the likely causes are too much `cue_hold_time_s`, disabled `scan_on_no_detect`, or a duplicated-center regression.

---

## 6. Target-Loss Reacquire Protocol

Target loss is not supposed to be a single generic scan anymore.

The current engine captures loss context and chooses between two protocols:

1. `rapid_handoff_search`
2. `persistent_reacquire_search`

### A. Rapid Handoff Search

Use this when another credible target is already visible or becomes visible quickly.

Behavior contract:

- continue briefly in the last known motion direction
- search just behind and around the loss vector
- allow immediate handoff to a stronger visible target
- finish quickly instead of becoming a wide search

This is the crowded-scene, fast-transfer behavior.

### B. Persistent Reacquire Search

Use this when the scene is sparse and no equally credible visible replacement exists.

Behavior contract:

- keep continuity with the lost target
- search tightly around the last known aim first
- widen only after the local area has been checked
- retry more in sparse scenes than in crowded scenes
- **stop immediately and switch to tracking any credible target that becomes visible during the search**
- in fixed/static guard, end in a clean return to guard position

This is the careful, bounded, "stay near where the target was lost" behavior, but prioritizes reacquiring any visible target over completing the full search pattern.

### Loss-Recovery Settings That Matter Most

- `target_loss_timeout`
- `adaptive_loss_recovery_enabled`
- `loss_recovery_protocol_new_target`
- `loss_recovery_protocol_no_detection`
- `loss_direction_pursuit_s`
- `loss_local_search_pan_deg` and `loss_local_search_tilt_deg`
- `loss_expanding_search_*`
- `loss_search_step_interval_s`
- `continuous_hunt_on_loss`
- `loss_search_style`
- `loss_search_rounds`

### Required Loss-Recovery Feel

Loss recovery should feel bounded and purposeful, not random and not frozen. In static guard mode it must never leave the turret stranded off-home when recovery ends.

Returning-state clarification:

- if a valid target becomes visible again during RETURNING, the engine should re-enter ENGAGING directly instead of forcing a home move first
- static guard keeps explicit home return behavior
- patrol guard modes (sweep/waypoint/random) resume patrol flow without mandatory home-pingpong moves

---

## 7. Aiming And Fire Protocol (Simplified)

### Fire Gate (Simplified)

Automatic firing happens when ALL of these are true:

1. `auto_trigger_enabled` is ON (user control)
2. Target is **centered** within firing tolerance (see `fire_trigger_enter_pan_tolerance`, `fire_trigger_enter_tilt_tolerance`)
3. Target has **minimum confidence** (`fire_trigger_min_confidence`) — typically 0.4+
4. Target has appeared for long enough (`fire_trigger_min_persistence`) — typically 0.08s+
5. **No no-fire mask** is blocking the aim point
6. Target stayed centered for **hold time** (`fire_trigger_hold_time`) — typically 0.05s+

That is the entire gate. Simple.

**Tuning:** 
- To fire more often: increase tolerances, lower confidence/persistence thresholds, reduce hold time
- To fire less often: do the opposite
- **Do not add new checks here.** If firing is blocked, check the settings above or a no-fire mask.

UI control note:

- trigger mode is available both in the full engagement settings panel and as a quick selector below the video panel
- both controls are mirrored (changing one updates the other): `MOSFET` (water path) vs `SERVO` (projectile trigger-servo path)

### Trigger Mode Note

`trigger_mode_bb` changes the trigger transport path, not the target-selection logic. Aiming, centering, and fire gating should remain logically identical regardless of water or BB mode.

Historical clarification:

- the current Smart Sentry app contract still supports both logical trigger modes on the DB3000 ESP32 path
- water mode is the MOSFET path and projectile mode is the ESP32 GPIO13 trigger-servo path
- the active firmware/docs contract carries that mode through serial `M0` and `M1` tokens or the WiFi JSON `mode` field
- archived Waveshare single-board bridge docs are different: that on-hold path explicitly leaves trigger-servo PWM unassigned and may report `trigger_servo_assigned=false`
- if projectile mode is selected while the active bridge has no assigned trigger-servo output, that is a topology or capability mismatch, not a target-selection or fire-gate failure
- keep trigger transport authority in `app/sentry_v2/sentry_v2_comm.py`; do not move mode-specific fire semantics into the engine

### Safety And Fire Sync Note

Current fire-path contract in `app/sentry_v2/sentry_v2_tab.py`:

- `auto` fire and `manual` fire both support a pre-arm synchronization path through `_apply_safety_arm_sync(...)`
- when runtime safety is reported as locked (`S1`) and a fire request is valid, software can arm (`S0`) and proceed without silently consuming the fire cycle
- this is intentionally a reliability behavior for active runtime operation, not a bypass of fire-gate conditions
- fire still obeys target centering/tolerance/hold/no-fire-mask rules for auto fire

---

## 8. Preset System: How To Think About It

A complete behavior stack is made from five layers:

1. detection preset
2. target-filter preset
3. threat preset
4. engagement preset
5. servo timing preset

The master profile is only a bundle that selects those five layers together.

This is a critical editor warning:

Changing one layer without understanding the others can make the preset description lie.

### What Each Layer Controls

#### Detection Preset

Controls what produces candidate boxes.

- motion-only families detect movement but have weaker semantic identity
- YOLO families trust class detection more and can keep tracking stationary valid targets
- color families depend on the chosen color behavior and fusion strategy
- filtered motion-locked families prefer a single credible mover over raw motion volume
- protocol addendum: when YOLO-family modes detect a `person` body without a face match, runtime should apply controlled upward tilt nudges until the face detector can evaluate known/unknown identity status

#### Target Filter Preset

Controls which candidate boxes survive.

- class-locked filters enforce species or object family rules
- size-only sniper motion filters define expected scale only
- confirmation fields decide how many strong frames are needed before the target becomes live

#### Threat Preset

Controls which surviving target becomes the winner.

- center-biased presets prefer on-axis targets
- speed-biased presets can prefer fast movers
- size-biased presets can prefer the largest or closest-looking target
- class-first presets let configured class priorities dominate

#### Engagement Preset

Controls how the turret behaves once the target is chosen.

- whether it tracks only or fires automatically
- how fast it corrects
- how strict the lock must be
- how long it tolerates temporary loss
- how aggressive or conservative the fire gate is

#### Servo Timing Preset

Controls movement feel at the transport level.

- `smooth`: visibly measured motion, appropriate for demo and sniper families
- `balanced`: default general-purpose motion
- `fast`: high-tempo, aggressive movement for fast targets

---

## 9. Preset Families And Intended Behavior

### Master Profiles

These are the operator-facing whole-behavior bundles.

#### `demo_observer`

- purpose: observe many movers without firing
- feel: slow, wide-net, non-aggressive
- rule: should track candidates visibly but never auto-fire

#### `indoor_precision`

- purpose: selective short-range indoor auto-fire
- feel: calm, strict, deliberate
- rule: should only fire after strong center confirmation

#### `balanced_sentry`

- purpose: middle-ground everyday sentry behavior
- feel: controlled but responsive
- rule: should neither look sluggish nor twitchy

#### `vehicle_intercept`

- purpose: larger fast movers
- feel: quicker handoff, wider tolerances
- rule: should not behave like a sniper preset

#### `aggressive_pursuit`

- purpose: fast, permissive pursuit with heavy action bias
- feel: fastest non-specialized family
- rule: should visibly snap harder than balanced families

#### `dog_tracker`

- purpose: dog-specific follow
- feel: responsive center-follow, no auto-fire by default

#### `cat_tracker`

- purpose: smaller agile target follow
- feel: tighter center lock and faster reacquire than dog tracking

#### `rat_like_tracker`

- purpose: very small agile targets
- feel: quickest small-target follow behavior in the non-sniper families
- rule: should not drift into slow demo-like motion

#### `color_follow_small`

- purpose: track small colored objects
- feel: permissive tracking, no auto-fire by default
- rule: color selection must still matter after applying the preset

#### `person_track_fire`

- purpose: person-only tracking plus auto-fire behavior
- feel: stable person-scale follow with longer loss tolerance
- rule: should keep tracking through brief human occlusion or body sway

#### `sniper_*`

- purpose: strict center-fire families by target scale and detection style
- feel: slow, calm, highly exact
- rule: should never feel like chase presets

### Detection Preset Intent

- `frame_diff`, `backsub`, `dual_motion`: conservative motion-led watchers
- `motion_yolo`, `best_hybrid`: faster hybrid candidate generation
- `color`, `color_motion`, `color_backsub`, `color_yolo`: color-centered behaviors
- `motion_locked`: stable single-mover sentry behavior
- `observer_motion_watch`: permissive observer for tiny and far movers
- `dog_follow`, `cat_follow`, `rat_like_follow`, `person_yolo`: target-specific detection families

### Filter Preset Intent

- `wide_net`: maximum candidate volume
- `observer_all_movers`: permissive observation
- `human_focus`, `person_focus_closest`, `sniper_large_person`: human-only families with increasing strictness
- `dog_focus`, `cat_focus`, `bird_focus`, `rat_like_motion`: class-specific animal filters
- `sniper_small_motion`, `sniper_medium_motion`, `sniper_large_motion`: size-only sniper filters for motion/color modes

### Threat Preset Intent

- `balanced_guard`: even weighting
- `crosshair_snap`: center-first
- `speed_hunter`: fast-mover-first
- `big_target_bias`: large-target-first
- `class_first`: configured-class-first
- `pet_center_lock`: strong center lock for pet tracking
- `small_target_follow`: tiny-target continuity
- `person_closest_center`: closest person wins
- `sniper_*_center_lock`: strongest center-first precision ranking by scale

### Engagement Preset Intent

- `demo_track`, `demo_track_multi`: track-only, no auto-fire, visibly slower
- `indoor_precision`: strict indoor auto-fire
- `balanced_response`: moderate auto-fire
- `outdoor_chase`: quick chase with wider tolerances
- `saturation_burst`: most aggressive burst profile
- `dog_follow_center`, `cat_follow_center`, `rat_follow_center`, `color_follow_track`: tracking-first center-follow families without auto-fire by default
- `person_track_fire`: person-scale auto-fire with extended loss tolerance
- `sniper_small_center`, `sniper_medium_center`, `sniper_large_center`: strict center-fire families with sustained lock requirement

---

## 10. Movement Rules For Preset Families

Movement should always be smooth enough to look intentional.

Movement should never be so slow that the target can visibly drift away while the turret is still catching up.

The motion feel is jointly created by:

- bus-servo timing preset
- `engagement_speed`
- `precision_max_step`
- per-axis precision limits
- error smoothing
- deadzone size
- reversal brake
- predictive lead settings

### Required Movement Character By Family

- demo and observer families: smooth and visibly measured
- balanced and person-track families: smooth but not hesitant
- dog/cat/color/rat follow families: responsive enough to feel alive without becoming jittery
- vehicle and aggressive pursuit families: visibly faster than balanced
- sniper families: always smooth and calm, never snap-happy

### Important Hidden Behavior

Engagement presets are not fully defined only by the visible preset tables. `app/sentry_v2/sentry_v2_tab.py` also merges `_ENGAGEMENT_PRESET_ADVANCED_OVERRIDES` into those presets.

This means a future editor can easily break preset behavior by changing only the main preset table and forgetting the hidden advanced override merge that adjusts things like:

- precision gains
- reversal braking
- predictive lead timing
- target-loss pursuit time
- persistent hunting behavior

If preset feel changes unexpectedly, check both places.

---

## 11. Non-Negotiable Behavior Contracts

These should remain true unless the project deliberately changes them and this file is updated in the same pass.

### Contract A: Guard Means Guard

- static guard returns to the configured guard position after a finished engagement or exhausted bounded recovery
- static guard must not remain stranded at the last search point after PIR or loss recovery

### Contract B: PIR Is Cue-First, Not Fire-First

- PIR initiates a look and a hunt, not blind firing
- PIR must not outrank a currently confirmed live engagement

### Contract C: Red Active Target Means Aiming Is Live

- red primary target box means the target is already in the engagement controller
- the turret should already be trying to center it unless it is already centered

### Contract D: Center Before Fire

- auto-fire requires centered, stable, trustworthy aim
- no-fire masks must block fire but must not corrupt target selection logic

### Contract E: Loss Recovery Is Bounded

- loss recovery should hunt deliberately
- loss recovery should not freeze
- loss recovery should not wander forever
- fixed/static guard must end back at guard/home

### Contract F: Preset Descriptions Must Match Runtime Feel

- demo presets must remain visibly slower than chase presets
- sniper presets must remain stricter than person or pet tracking presets
- person-track behavior must tolerate brief occlusion better than small-animal presets

---

## 12. Quick Troubleshooting

### "It won't auto-fire"

Check in this order:

1. Is `auto_trigger_enabled` ON in the UI? (literally a checkbox)
2. Is the target **centered on screen**? (red box at center means it's being aimed)
3. Are there any **no-fire masks** configured that block the center?
4. Check the **fire gate settings**:
   - `fire_trigger_enter_pan_tolerance` (degrees) — is it too tight?
   - `fire_trigger_enter_tilt_tolerance` (degrees) — is it too tight?
   - `fire_trigger_min_confidence` — is it too high? (try 0.35-0.4)
   - `fire_trigger_hold_time` — is it too long? (try 0.05s)

**Default fix:** Loosen `fire_trigger_enter_*_tolerance` by 20%, lower confidence to 0.35, reduce hold_time to 0.05.

### "It moves very slow"

Check in this order:

1. `engagement_speed` — higher = faster (try 80-90)
2. `bus_servo_time_ms` — lower = faster (try 40-50)
3. `precision_max_pan_step` / `precision_max_tilt_step` — increase these

**Default fix:** Set `engagement_speed` to 80+, `bus_servo_time_ms` to 48.

### "It overshoots (wobbles)"

Check in this order:

1. `precision_reversal_brake` — lower = less overshoot (try 0.1-0.15)
2. `precision_max_pan_step` — lower = less overshoot (try 0.4-0.5)
3. `precision_max_tilt_step` — lower = less overshoot (try 0.3-0.4)

**Default fix:** Reduce reversal_brake to 0.1, max_pan_step to 0.4.

### "It loses targets immediately"

Check in this order:

1. `target_loss_timeout` (seconds) — how long before giving up? (try 1.5-2.0)
2. `loss_search_rounds` — more rounds = longer search (try 5-6)
3. `loss_direction_pursuit_s` — how long to pursue in last direction? (try 0.3-0.4)

**Default fix:** Increase `target_loss_timeout` to 2.0, `loss_search_rounds` to 6.

### "Turret stays locked on one stationary person forever; PIR/acoustic guard never runs"

This happens in single-target mode when the only visible target stops moving. The ENGAGING loop cycles through aim→precision→fire repeatedly and never re-enters GUARDING, so PIR and acoustic guard workflows are unreachable.

Check in this order:

1. Is `stationary_release_enabled` ON in config? (must be true)
2. Is `Max stationary target hold (s)` set in the Engage tab? (default 8.0 s; try 4–6 s)
3. Has the target actually been visible and tracked continuously? (the timer only counts while the track is held and low-motion criteria pass)

**Default fix:** Enable stationary release, set `stationary_release_hold_s` to 5.0, leave `stationary_release_min_fire_cycles` at default (3). The turret will force a return/queue-advance after the criteria are met so GUARDING can re-enter and consume PIR/acoustic cues.

**Important:** `target_loss_timeout` is not the right setting for this — it applies only when the target has *disappeared* (no detection box), not when it is still visibly tracked and stationary.

---

## 13. Known Editor Trap Areas (Simplified)

These are the places most likely to produce accidental regressions.

### 1. Changing Preset Values In Only One Table

Risk:

- master profile description says one thing
- engagement preset does another
- advanced override silently changes the final result again

Required discipline:

- treat master profile, detection, filter, threat, engagement, servo timing, and advanced overrides as one behavior bundle

### 2. Regressing Offset-First PIR Hunt Behavior

Risk:

- PIR cue looks like a pause or false return
- first scan point duplicates the center

Required discipline:

- preserve the current offset-first multi-point hunt contract after cue confirmation

### 3. Breaking Fixed-Guard Return-To-Guard

Risk:

- after loss or PIR no-detect the turret stays off-home

Required discipline:

- any search completion path in static guard must explicitly restore guard/home behavior

### 4. Over-Slowing Smooth Motion

Risk:

- motion stays elegant but becomes useless for live targets

Required discipline:

- smooth is allowed to be calm, not lazy
- balanced should remain the default practical operating point
- fast should remain visibly faster than balanced

### 5. Misunderstanding The Red Box

Risk:

- an editor assumes a red primary box is just a visual suggestion

Required discipline:

- red means active engagement state, not idle observation

### 6. Stale Feedback And Deferred-Move Drift

Risk:

- the engine keeps planning from commanded pose instead of settled hardware pose
- loss or PIR hunts overshoot or feel disconnected from the actual turret

Required discipline:

- engine and tab-side deferred-move handling must stay aligned so pose is resynced when automatic movement is delayed

### 7. Duplicating Trigger Logic Outside The Communication Layer

Risk:

- UI labels, saved settings, and transport payloads drift apart
- projectile trigger-servo runtime tuning works on one path but silently stops updating on another
- docs incorrectly imply that every hardware topology exposes both physical trigger outputs the same way

Required discipline:

- keep `app/sentry_v2/sentry_v2_comm.py` as the single transport authority for trigger mode encoding and runtime trigger configuration
- keep `app/sentry_v2/sentry_v2_engine.py` mode-agnostic; it should decide whether firing is allowed, not how a specific transport energizes hardware
- when docs describe both trigger modes, distinguish the current DB3000 ESP32 contract from archived Waveshare bridge history

### 8. Reintroducing Blocking Burst Fire

Risk:

- automatic fire freezes preview updates or makes the app feel stalled during bursts

Required discipline:

- preserve the timer-driven burst sequencer in `app/sentry_v2/sentry_v2_tab.py` for live app firing
- treat the older blocking communication burst loop as historical context, not the preferred runtime path for the UI

### 9. Scope/Reticle Documentation Drift

Possible mismatch worth tracking:

- some docs describe the scope reticle contract as “no center fill”
- current overlay code still draws a center dot in the guard crosshair path

This does not change the tracking math, but it is an editor-facing documentation consistency risk and should be treated carefully if overlay documentation is revised again.

### 10. Overlay Display Mode Contract

The live video pane now has a 3-state display mode cycle button under the panel:

- `SHOW ALL`: full overlay rendering path (`overlay.draw(...)` + identity labels + optional scope view + mask/status overlays)
- `MINIMAL`: thin crosshair + thin target boxes only (no full HUD labels/panels/scope rendering)
- `NO OVERLAY`: raw video frame copy with all overlay drawing bypassed

Current ownership points:

- `app/sentry_v2/sentry_v2_tab.py`: mode constants, mode-cycle UI, render branch (`_build_display_frame`), minimal renderer (`_draw_minimal_overlay`)
- `app/sentry_v2/sentry_v2_config.py`: persisted `overlay_display_mode` with `show_all` default

Required rule:

- per-overlay settings toggles remain preserved in config and must not be destroyed when mode is switched; display mode is a runtime visibility layer, not a destructive settings rewrite

---

## 14. Practical Tuning Rules (Simplified)

### Auto-Trigger Not Working

1. Check `auto_trigger_enabled` is ON
2. Check target is centered (red box at center)
3. Increase `fire_trigger_enter_pan_tolerance` and `fire_trigger_enter_tilt_tolerance` by ~1 degree
4. Lower `fire_trigger_min_confidence` to 0.35-0.4
5. Reduce `fire_trigger_hold_time` to 0.05

### Movement Too Slow

1. Increase `engagement_speed` to 80+
2. Lower `bus_servo_time_ms` to 40-50
3. Increase `precision_max_pan_step` to 0.6+
4. Increase `precision_max_tilt_step` to 0.5+

### Movement Overshoots / Wobbles

1. Lower `precision_reversal_brake` to 0.1-0.15
2. Lower `precision_max_pan_step` to 0.4-0.5
3. Lower `precision_max_tilt_step` to 0.3-0.4

### Target Loss (Can't Reacquire)

1. Increase `target_loss_timeout` to 2.0+ seconds
2. Increase `loss_search_rounds` to 5-6
3. Increase `loss_direction_pursuit_s` to 0.4

---

## 15. Change Checklist For Future Editors

Before modifying tracking behavior, review all of these together:

- `app/sentry_v2/sentry_v2_engine.py`
- `app/sentry_v2/sentry_v2_pir_manager.py`
- `app/sentry_v2/engagement_planner.py`
- `app/sentry_v2/sentry_v2_tab.py`
- `app/sentry_v2/sentry_v2_config.py`
- `app/sentry_v2/sentry_v2_overlay.py`
- `SMART_SENTRY_MANUAL.md`
- `SMART_SENTRY_APP_CHANGE_IMPACT.md`
- `PIR_AT_A_GLANCE.md`
- `PIR_GUARD_QUICK_START.md`
- `PIR_DOCUMENTATION_INDEX.md`

If behavior changes are real, update this file in the same pass.

If this file is not updated, the change is not finished.

---

## 16. Bottom-Line Operational Summary

The intended Smart Sentry behavior is:

- stay in guard until a credible target exists
- when a credible target exists, start centering it immediately
- if PIR sees something first, use it as a cue to look and hunt, not as a reason to fire blindly
- if the target becomes the active primary target, the turret should already be aiming it
- only fire after centered, stable confirmation if auto-fire is enabled
- when the target is gone, use bounded reacquire logic
- when reacquire fails, return to guard cleanly

That is the behavior contract this repository should preserve.
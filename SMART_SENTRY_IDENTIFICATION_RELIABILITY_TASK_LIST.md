# Smart Sentry Identification Reliability Task List

Date: 2026-08-21
Status: Face fallback and first animal false-positive gates implemented; model-quality validation remains staged.

## Validated Findings

- [x] YOLO class labels are treated as authoritative after confidence, size, shape, and semantic-frame checks. There is no second classifier or class-ambiguity rejection stage.
- [x] Animal-profile evidence includes a mission where YOLO reported `rat` at high confidence but the active whitelist was still `person`; every detection was rejected as `class_rejected`.
- [x] The effective cat/dog/rat profile can be configured with multiple confirmation frames, but runtime evidence also shows sessions with `semantic_min_confirm_frames=1`; active profile application must be verified per session.
- [x] Face models and the OpenCV YuNet/SFace backend are present and reported ready.
- [x] Before this fix, live face matching returned zero matches across recent snapshots even when a live frame existed.
- [x] Before this fix, face matching returned early when YOLO supplied no person boxes, so YuNet could not scan the full frame.
- [x] Camera and YOLO runtime issues can independently prevent face work: recent logs include camera recovery and sessions with zero visible persons.

## Implemented Targeted Fix

- [x] Person-mode face matching now uses a full-frame scan when no YOLO person ROI exists.
- [x] Person-box ROI scanning remains active when YOLO provides person boxes.
- [x] Regression coverage verifies both paths in `test_face_person_roi_fallback.py`.
- [x] Animal classes require at least three consistent semantic confirmation frames, even when a stale profile requests one frame.
- [x] Animal classes require recent motion before engagement, even when a stale profile allows stationary engagement.
- [x] Planner orders outside the configured pan/tilt servo envelope are skipped instead of being silently clamped into a false reachable order.
- [x] Active engagements release an animal target when its current visual position moves outside the servo envelope and advance the queue.
- [x] Backup auto-trigger now honors animal motion-policy rejection instead of firing a blocked stationary target.
- [x] Focused identity and reachability regressions pass in `test_target_identity_reachability.py`.

## Immediate Next Work

- [ ] Add explicit face-stage telemetry: scan attempted, ROI source, candidate count, score rejects, landmark rejects, ROI-geometry rejects, embedding failures, and profile-match failures.
- [ ] Add a face diagnostic command or panel action that reports the above counters for the current frame.
- [ ] Add a full-frame YuNet test using a controlled known-face image and a controlled no-face image.
- [ ] Confirm the live camera frame is exposed at sufficient face size and frontal angle before lowering `min_face_size_px` or YuNet acceptance thresholds.
- [ ] Verify that `last_match_count=0` is distinguishable from `no face candidates` and `no profile match`.
- [ ] Re-enroll profiles only after confirming the active backend and valid 128-dimensional SFace embeddings.

## Animal Identification Work

- [ ] Add runtime profile-application telemetry showing active profile, model path, allowed classes, shape profile, confidence, and semantic confirmation requirement in every mission configuration snapshot.
- [ ] Add a profile-application regression test proving cat/dog/rat selection cannot leave `allowed_classes=person`.
- [ ] Normalize model class aliases at the detector/filter boundary (`cat`/`cats`, `dog`/`dogs`, and similar configured aliases) without changing canonical YOLO labels.
- [ ] Require class consistency across a configurable number of consecutive frames for cat/dog/rat targets.
- [ ] Reset semantic confirmation when class, track identity, or detection center changes materially.
- [ ] Capture top-class and runner-up class probabilities when the model exposes them.
- [ ] Reject ambiguous classifications when the top-two probability margin is below a configured threshold.
- [ ] Confirm the custom animal model itself is not producing persistent high-confidence false rat labels; runtime gates cannot correct a wrong model class.
- [ ] Build a labeled validation set containing cats, dogs, rats, empty scenes, toys, shadows, clothing, bags, furniture, and other common false positives.
- [ ] Measure per-class precision, recall, false-positive rate, and confusion matrix before changing thresholds.
- [ ] Tune confidence, minimum area, shape limits, and confirmation frames from validation results rather than live-fire behavior.

## Safety and Release Gates

- [ ] Keep auto-trigger disabled during identification validation.
- [ ] Require a clear no-fire mask and hardware-safe actuator for detector tests.
- [ ] Add a mission-level fire-attempt counter and distinguish fire request, hardware acknowledgement, cooldown suppression, and safety veto.
- [ ] Reject release candidates when a profile silently falls back to a different model or class whitelist.
- [ ] Require animal-profile and person-profile regression tests before enabling automatic engagement.
- [ ] Archive representative runtime exports with the model checksum and effective configuration snapshot.

## Acceptance Criteria

- [ ] A cat/dog/rat profile never reports `person` as an allowed class after profile application.
- [ ] A target class must remain consistent for the configured confirmation window before it becomes engageable.
- [ ] Ambiguous top-two classifications are rejected and visible in diagnostics.
- [ ] Person mode attempts face detection even when YOLO misses the person body.
- [ ] Face diagnostics identify whether failure occurred before detection, during candidate filtering, during embedding, or during profile matching.
- [ ] Known test faces are detected and matched from both a full frame and a YOLO person ROI.
- [ ] No identification validation test can actuate the firing hardware.

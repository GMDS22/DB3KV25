# Smart Sentry AI Conversation Expansion Task List

Date: 2026-05-13
Status: Requested voice and conversation expansion pass completed, extended, and validated.

This checklist separates work completed in this implementation pass from the broader backlog identified during the earlier codebase audit.

## Completed In This Pass

- [x] Add short-term social memory for the active voice session so Elion can remember recently recognized enrolled names across back-to-back conversational turns.
- [x] Add deterministic social follow-up replies for prompts such as `do you remember us`, `who did you just meet`, and `we are back`.
- [x] Expand playful mission coverage from a single splash prompt into multiple mini-game packs including splash, stealth, freeze, countdown, and joke-reward challenge styles.
- [x] Add follow-up playful prompts such as `give us another challenge`, `give us a freeze dance challenge`, and `what games can we play`.
- [x] Preserve full cue-driven prompt context through the fast conversational reply path so family and scenario details are not lost during early canonicalization.
- [x] Expand cue-only wake acknowledgements with a larger rotating phrase set and optional recognized-name greetings when enrolled friendly faces are currently in view.
- [x] Add deterministic family-introduction replies that greet recognized enrolled faces by name before introducing Elion and summarizing capabilities.
- [x] Add deterministic conversational coaching for prompts such as `how can I improve the aiming precision`, `how can I make it more playful`, and `what can we ask you`.
- [x] Add family-friendly playful scenario coverage for prompts such as `give us a splash mission` and related challenge/game requests.
- [x] Expand the Vosk admission gate and tab-side conversational intent gate for the new family-introduction, coaching, playful, and discovery phrases.
- [x] Expand the Vosk admission gate so identity prompts like `introduce yourself`, `describe yourself`, and `who created you` are accepted.
- [x] Expand the Vosk admission gate so short follow-up voice selections like `British female`, `male`, `female`, and `try another one` are accepted.
- [x] Expand the Vosk admission gate for direct utility commands: `current voice`, `voice options`, `test voice`, `scan voices`, `save settings`, `export snapshot`, `export conversation`, and `open folder`.
- [x] Expand assistant identity and capability conversation for introduction, purpose, creator, and origin prompts.
- [x] Expand assistant joke coverage and support follow-up joke requests such as `another one` and `one more` without repeating the previous joke when alternatives exist.
- [x] Expand conversational handling for compliments and small-talk variants already supported by the local assistant layer.
- [x] Expand runtime voice-family guidance so operators receive clearer voice-option prompts with concrete family examples.
- [x] Fix the broken voice-change conversation path so selecting a voice no longer dead-ends into silence when human voice was previously disabled.
- [x] Centralize voice-change acknowledgement and demo phrases so all voice-selection paths use the same behavior.
- [x] Add direct spoken handling for current voice summary, voice test, full voice scan, settings save, runtime snapshot export, runtime conversation export, and export-folder open actions.
- [x] Fix the shutdown speech leak so Smart Sentry stops active speech immediately and blocks delayed voice callbacks once app shutdown begins.
- [x] Add direct spoken face commands for face status, known-face profile summary, preview face detection, saving detected faces, and known-face testing with prompts like `who is in view`.
- [x] Tighten Acoustic Guard so it requires a short sustained anomaly window, uses stricter default sensitivity values, and pauses unless Smart Sentry is actively enabled.
- [x] Add direct spoken coordinated-profile commands for `current profile`, `list profiles`, and `load profile <name>` using the live master-profile store.
- [x] Add direct spoken face-library management commands for live-frame registration and removal using phrases like `register face as <name>`, `register target face <name>`, and `remove face <name>`.
- [x] Add direct spoken tuning-preset commands for current/list/load flows across detection, target filter, threat AI, engagement, and servo move-time preset groups.
- [x] Add direct spoken face-library maintenance commands for refreshing an existing face profile from the current frame and renaming a saved face profile by name.
- [x] Add direct spoken face disposition commands for marking a saved face profile as target or friendly by name.
- [x] Add voice-first face image import flows for loading the latest preview-inbox photo and importing per-profile face photo batches from fixed folders.
- [x] Add a searchable Smart Sentry document browser window with both a Quick Actions launcher and direct voice-open commands.
- [x] Add an embedded `Documentation` settings tab that reuses the same formatted document browser UI inside the main Smart Sentry runtime.

## Documentation Updated In This Pass

- [x] Update the operator docs so the new short-term social memory and the expanded mini-game prompt families are documented alongside the earlier family-introduction flow.
- [x] Update `SMART SENTRY — CONVERSATION & COMMAND.md` with family-introduction, playful mission, and conversational coaching examples for the new voice-first behavior.
- [x] Update `SMART_SENTRY_MANUAL.md` so the operator reference calls out the new name-aware greetings, playful prompts, and precision-coaching conversation layer.
- [x] Update `SMART SENTRY — CONVERSATION & COMMAND.md` with the implemented identity, joke, voice-change, direct voice-utility, coordinated-profile, and acoustic-guard runtime scenarios.
- [x] Update `SMART_SENTRY_MANUAL.md` with the new voice-first conversation coverage, coordinated-profile voice commands, repaired no-silence voice-change behavior, and tightened acoustic-guard runtime contract.
- [x] Add `SMART_SENTRY_FACE_IMPORT_VOICE_GUIDE.md` and `SMART_SENTRY_DOCUMENT_BROWSER_GUIDE.md` for the new folder-backed face import flows and the in-app document browser.
- [x] Update the manual, conversation contract, and document-browser guide so the new embedded `Documentation` tab is documented alongside the detached browser window.

## Validation Completed

- [x] Focused voice-gate probe passed for `do you remember us`, `give us another challenge`, `give us a freeze dance challenge`, and `what games can we play`.
- [x] Focused regression script passed for short-term social memory recall and non-repeating challenge follow-up replies.
- [x] `py_compile` passed for `assistant/service.py`, `sentry_v2_tab.py`, `voice_runtime.py`, and `test_voice_conversation_expansion.py` after the family/playful conversation expansion.
- [x] Focused assistant conversation probe passed for name-aware family introductions, aiming-precision coaching, playful-mode guidance, mission prompts, and `what can we ask you` discovery replies.
- [x] Focused regression script `test_voice_conversation_expansion.py` passed for deterministic family introduction, coaching, discovery, and playful mission replies.
- [x] `py_compile` passed for `voice_runtime.py`, `assistant/service.py`, and `sentry_v2_tab.py`.
- [x] Focused Vosk gate probe passed for `introduce yourself`, `who created you`, `what voice are you using`, `save settings`, `export snapshot`, `open folder`, and `scan voices`.
- [x] Focused assistant reply probe passed for immediate introduction reply, creator reply, and non-repeating joke follow-up behavior.
- [x] Focused shutdown probe passed: shutdown-state speech APIs and deferred voice actions return immediately instead of speaking after close.
- [x] Focused face-command probe passed for `face status`, `list known faces`, `detect faces`, `save detected faces`, `test face recognition`, and `who is in view`.
- [x] `py_compile` passed for `acoustic_guard.py`, `sentry_v2_config.py`, and `sentry_v2_tab.py` after the acoustic-guard runtime tightening.
- [x] Acoustic guard probe passed: runtime debounce now requires 3 anomaly blocks, legacy `3.5 dB / 1.6 z-score` defaults migrate to `8.0 / 2.8`, and the tab gate blocks runtime when Smart Sentry is disabled or closing.
- [x] Coordinated-profile probe passed: spoken profile resolution now maps to the live master-profile store and returns current/available profile summaries.
- [x] Face-management voice probe passed: `register face as alice johnson`, `register target face intruder`, and `remove face alice` all parse correctly and resolve against the live face library helpers.
- [x] Tuning-preset voice probe passed: the listener now admits `current detection preset` and `use balanced response engagement preset`, and the tab-side parser resolves current/list/load requests into the correct tuning groups.
- [x] Face-maintenance voice probe passed: the listener now admits `update face alice` and `rename face alice to alicia`, and the tab-side parser extracts the requested face names correctly.
- [x] Face-disposition voice probe passed: the listener now admits `mark face alice as target` and `set face alice to friendly`, and the tab-side parser resolves the requested profile name plus target/friendly intent correctly.
- [x] Face-photo-import voice probe passed: the listener now admits `load latest face import into preview` and `import target face photos for alice johnson`, and the tab-side parser resolves preview load and target/default batch-import requests correctly.
- [x] Document-browser validation passed: the browser indexes live Smart Sentry markdown and text docs in an offscreen probe, and the new `open document browser` voice request is admitted and matched.
- [x] Documentation-tab validation passed: the runtime now builds a live `Documentation` settings tab backed by the same browser widget, and the offscreen probe confirmed the tab indexed live Smart Sentry documents.

## Broader Backlog From The Earlier Audit

- [ ] Add more voice-first commands around deeper identity-library maintenance beyond the new live register/remove/update/rename/disposition/photo-import flows.
- [ ] Add more direct spoken tuning flows beyond preset groups, especially manual slider/value changes and grouped diagnostics for the deeper runtime tuning tabs.
- [ ] Expand voice-first queue management beyond the current direct command set.
- [ ] Add end-to-end spoken regression coverage for Qt local voice, Edge voice, Kokoro voice, and Azure voice routing.
- [ ] Extend documentation further if additional command families are promoted from the broader audit into live implementation.
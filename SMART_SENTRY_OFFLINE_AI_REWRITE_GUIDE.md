# Smart Sentry Offline AI Rewrite Guide

## Purpose

This document is the working implementation guide for improving the current local Smart Sentry assistant into a stronger offline AI stack while keeping live sentry control deterministic, reviewable, and safe.

The current app already has three valuable pieces that should be preserved:

1. A stable deterministic sentry pipeline for detection, targeting, movement, and fire control.
2. A rich runtime export and logging path that can feed diagnostics safely.
3. A local Windows speech path through Qt TextToSpeech that can remain the single text-to-speech authority.

The rewrite should build on those strengths instead of turning movement, firing, or safety logic into LLM-driven behavior.

## Current State Summary

Smart Sentry currently exposes an AI Assistant tab with a live Ollama-backed local assistant plus deterministic runtime analysis and deterministic fallback behavior inside the main UI widget.

Current characteristics:

- Ollama-backed local responses using `llama3.2:latest` as the current fast default.
- Deterministic runtime analysis and deterministic fallback guidance when the local model path is unavailable.
- Safe operator actions such as home, rest, bounded pan or tilt positioning, detection mode switching, auto-speak toggling, and voice-style changes.
- Optional local human speech through Qt TextToSpeech, with conversational replies spoken as short summaries.
- No real memory system beyond live widget state.
- No semantic understanding of code logic or multi-step reasoning.
- No dedicated runtime abnormal-behavior analysis engine.

This is now a usable first-pass local AI assistant, but it still needs deeper subsystem reasoning, stronger retrieval quality, and clearer deployment coverage to meet the full long-term design target.

## Goals

The new offline assistant should:

1. Understand the Smart Sentry app structure, runtime state, and operator workflow.
2. Analyze runtime behavior and identify unusual movement, likely faults, or repeated unhealthy patterns.
3. Inspect code files, logs, and exported runtime artifacts to suggest likely logic fixes.
4. Remember operator preferences, the current session context, and curated app knowledge.
5. Stay free to use, downloadable, and fully offline.
6. Never bypass existing movement, trigger, or safety gates.

## Non-Goals

The first rewrite does not attempt to:

- Make the model directly control firing logic.
- Let the model silently apply code changes from inside the runtime app.
- Replace the sentry engine, detector, comm layer, or safety rules with ML.
- Depend on a cloud provider.

## Design Principles

1. Deterministic control, model-assisted reasoning.
2. Read-only diagnostics by default.
3. All mutating actions must be approval-gated.
4. Runtime analysis should use structured telemetry first, LLM explanation second.
5. The assistant should be modular, not embedded in the main UI class.
6. Build and packaging should support fast local iteration.

## Recommended Offline Model Options

### Recommended Default: Ollama

Ollama is the recommended first backend because it is:

- Free.
- Downloadable and usable offline.
- Easy to install on Windows.
- Easy to test independently of the app.
- Flexible enough to swap models without rewriting the integration.

Recommended first-pass models:

- General assistant: `qwen2.5:7b-instruct` or `llama3.1:8b-instruct`
- Code reasoning: `qwen2.5-coder:7b`
- Lower-resource fallback: `phi3:mini`

### Strong Alternative: llama.cpp

Use llama.cpp only if Ollama proves too heavy or too opaque for deployment. It offers tighter control over bundling and inference options but requires more custom integration and runtime management.

### Lightweight Supporting Option: ONNX Intent Model

For very fast local intent parsing, a small ONNX or TorchScript classifier can be used for command routing even when the main assistant provider is unavailable. This is not a replacement for a reasoning model; it is a fast fallback.

## Recommended Architecture

Create a dedicated assistant package under `app/sentry_v2/assistant/`.

Suggested modules:

- `assistant_service.py`
- `assistant_provider.py`
- `assistant_provider_ollama.py`
- `assistant_provider_rule_fallback.py`
- `assistant_context.py`
- `assistant_memory.py`
- `assistant_actions.py`
- `assistant_runtime_analyzer.py`
- `assistant_prompts.py`
- `assistant_models.py`

### Assistant Service Responsibilities

The assistant service should:

- Orchestrate requests.
- Load provider status asynchronously.
- Assemble runtime and domain context.
- Dispatch read-only tools immediately.
- Route mutating requests into staged actions.
- Persist session and operator memory.
- Feed replies into the existing TTS path when enabled.

### Provider Abstraction

The provider abstraction should support these states cleanly:

- Provider unavailable.
- Provider available but no model installed.
- Provider available and ready.
- Provider timed out or faulted.

Every response should include metadata such as provider name, model, latency, and confidence or fallback reason when available.

## Runtime Analysis Architecture

The app already exposes useful telemetry. The first implementation should create a deterministic runtime health monitor that observes the sentry system and produces structured findings.

### Runtime Health Monitor

Add a new observational-only subsystem, for example:

- `RuntimeHealthMonitor`
- `MotionAnomalyDetector`
- `ServoHealthAnalyzer`
- `StateTransitionAuditor`
- `CameraHealthAnalyzer`
- `CommunicationHealthAnalyzer`

### Signals To Use Immediately

Use existing telemetry and logs where possible:

- Servo feedback pan and tilt.
- Servo feedback age and error state.
- IO runtime age, current, and fault state.
- Engine state, queue state, and active order.
- Loss recovery phase and reacquire notes.
- Recent log lines.
- Camera grab-failure counts and recovery attempts.
- Precision tuning logger data when enabled.
- ML training logger outputs when enabled.

### First Abnormal-Behavior Checks

The first release should detect and surface these conditions:

1. Repeated loss recovery cycles in a short period.
2. Servo position not following commanded movement closely enough.
3. Large jitter or oscillation during precision aiming.
4. Stale telemetry or stale feedback.
5. Camera grab-failure bursts.
6. Repeated no-fire-mask blocking during otherwise valid engagements.
7. Unusually long time spent in a state or sub-phase.
8. Repeated comm errors or transport resets.

These should produce structured findings with:

- title
- severity
- evidence
- likely causes
- suggested next checks

### LLM Use In Runtime Analysis

The LLM should explain health-monitor findings and generate operator-friendly summaries. It should not be the first or only detector of abnormal behavior.

## Context and Memory Model

The assistant should not be fed the whole repo on every request. Instead, build context from structured layers.

### Layer 1: Runtime Context

Use the full runtime snapshot and recent log tail.

Include:

- Engine state.
- Active config summary.
- Hardware and connection mode.
- Camera state.
- YOLO/model status.
- Recent alarms and findings.

### Layer 2: Domain Knowledge Context

Curate persistent summaries from project docs and architecture references.

Include:

- Manual summary.
- Change impact rules.
- Export guardrails.
- Detection mode reference.
- Hardware topology notes.
- Voice and assistant operating rules.

### Layer 3: Memory

Use three memory scopes inside the app runtime:

- Operator memory: preferred voice, preferred assistant style, hardware mode, preferred actions.
- Session memory: current conversation, recent findings, recent exports, active investigation thread.
- Knowledge memory: curated subsystem summaries and settings schema, not raw full-file dumps.

## Code Analysis Scope

The new assistant should support code analysis as a guided diagnostic feature.

### Supported Inputs

- Selected code files.
- Exported runtime snapshots.
- Exported serial logs.
- Recent issue log entries.
- Manual and change-impact docs.

### Expected Outputs

- Likely bug or logic mismatch.
- Evidence pointing to the relevant subsystem.
- Recommended fix strategy.
- Optional patch draft text.

### Safety Boundary

The runtime assistant must not silently edit source files. It can produce recommendations and staged patch text, but implementation should remain a reviewed developer workflow.

## UI Rewrite Plan

The current `AI Assistant` tab should be replaced or split.

### Recommended Tabs

#### Assistant

Purpose:

- Natural-language assistant interaction.
- Provider status.
- Memory summary.
- Conversation history.
- Speak last reply.

Features:

- Ask about current state.
- Ask how the app works.
- Ask for recommended next actions.
- Ask for explanations of recent anomalies.

#### Runtime Analyst

Purpose:

- Show live health findings.
- Show unusual movement or likely faults.
- Export evidence.
- Review recent anomaly timeline.

Features:

- Current findings panel.
- Severity badges.
- Trend indicators.
- Snapshot/export actions.

#### Draft Changes

Purpose:

- Stage assistant-proposed config changes.
- Show rationale and affected settings.
- Let the operator approve or reject.

Features:

- Proposed changes table.
- Risk note.
- Apply and revert actions.
- Audit trail entry.

### Current Controls Tab Role

Do not move human voice diagnostics out of Controls for now. Controls should remain the canonical home for:

- voice enable or disable
- selected Windows SAPI voice
- speech style preset
- rate, pitch, and volume
- voice diagnostics

The assistant should call into that existing TTS path rather than owning another speech engine.

## Voice Defaults

The current saved human voice settings are not ideal for a natural default voice.

Recommended defaults on this Windows environment:

### Male Natural

- Voice: `Microsoft David Desktop`
- Preset key: `male_natural`
- Rate: `96`
- Pitch: `92`
- Volume: `88`

### Female Natural

- Voice: `Microsoft Zira Desktop`
- Preset key: `female_natural`
- Rate: `98`
- Pitch: `104`
- Volume: `86`

### Spoken Behavior Defaults

- Keep `auto_speak_responses` off by default unless conversational mode is explicitly selected.
- Keep human voice speech separate from buzzer cues.
- Keep the existing buzzer mute guard when human voice mode is enabled.

## Build and Packaging Strategy

The rewrite should also make builds easier and faster.

### Packaging Variants

Add clear packaging modes:

1. `full`
   Includes the current full runtime plus standard bundled assets.

2. `lean`
   Excludes large optional assets that are not required for local assistant development.

3. `offline-ai`
   Intended for local assistant work. Keeps the assistant integration code, but avoids re-bundling heavyweight model payloads into the main app package when possible.

### Build Speed Improvements

Recommended improvements:

1. Faster preflight dependency checks before PyInstaller starts.
2. Stronger validation that `.venv311` is the active build interpreter.
3. Clear separation between packaged app files and mutable operator data.
4. Optional external model directories rather than bundling every large model into the package.
5. Better fast-fail behavior when required local AI components are missing.

### Deployment Recommendation For Offline AI

Prefer this deployment pattern:

- Main Smart Sentry app packaged normally.
- Ollama installed separately on the target PC.
- Models pulled once and stored outside the app package.
- App validates provider availability on startup or from the Assistant tab.

This avoids enormous packages and speeds up rebuilds significantly.

## Migration Phases

### Phase 1: Document and Freeze Boundaries

- Create this guide.
- Keep the current rule-based assistant as fallback.
- Define provider and safety boundaries.

### Phase 2: Extract Assistant Code

- Move AI logic out of the UI monolith.
- Add provider abstraction.
- Keep existing keyword routing as fallback.

### Phase 3: Add Runtime Health Monitor

- Implement deterministic abnormal-behavior checks.
- Surface findings in a new Runtime Analyst tab.

### Phase 4: Add Offline Provider

- Integrate Ollama.
- Add provider health and model availability checks.
- Add background request execution.

### Phase 5: Add Memory and Better Context

- Persist operator preferences.
- Add session memory.
- Add curated subsystem summaries.

### Phase 6: Add Drafted Actions

- Let the assistant propose config changes.
- Require explicit user approval.
- Log applied changes.

### Phase 7: Add Code Diagnosis Workflows

- Let the assistant analyze logs, snapshots, and selected files.
- Return findings and patch suggestions.

## Verification Checklist

Before considering the rewrite stable, verify these scenarios:

1. App starts with no AI provider installed.
2. App starts with provider installed but no model available.
3. App starts with provider ready.
4. Assistant fallback path still works without the model.
5. Runtime anomaly monitor detects simulated stale servo feedback.
6. Runtime anomaly monitor detects repeated camera failures.
7. Runtime anomaly monitor detects repeated loss-recovery behavior.
8. Voice still works when available and fails gracefully when unavailable.
9. Build variants complete successfully.
10. No assistant path can bypass existing movement, trigger, or safety gates.

## Safety Rules

The following rules are mandatory:

1. The assistant cannot directly fire or bypass fire gating.
2. The assistant cannot directly bypass movement clamping or safety locks.
3. The assistant cannot silently edit source files.
4. The assistant cannot mutate the live runtime during export capture.
5. All applied runtime-setting changes must be explicit, reviewable, and logged.

## Limitations

These constraints should remain explicit while building:

1. Free offline local models are slower and less reliable than strong cloud models on weaker hardware.
2. A local model can explain likely causes, but it cannot guarantee a root-cause diagnosis.
3. The assistant can become familiar with curated app structure and recent session evidence, but it cannot reliably hold the entire large repository in active context every turn.
4. Runtime anomaly detection is strongest when based on deterministic telemetry rules, not model intuition alone.
5. If local hardware telemetry is incomplete or stale, the assistant can only reason from partial evidence.

## Recommended First Implementation Scope

The first actual code pass should implement only these items:

1. Assistant package scaffold.
2. Provider abstraction.
3. Rule fallback provider.
4. Runtime health monitor scaffold with read-only findings.
5. Assistant UI split into `Assistant` and `Runtime Analyst`.
6. New natural male and female voice presets.

Do not attempt the full staged-actions workflow and code-diagnosis workflow in the same first pass unless the extraction work is already stable.

## Working Decision Summary

- Preferred backend: Ollama first.
- Preferred control model: deterministic engine plus model-assisted reasoning.
- Preferred safety stance: observational by default, approval-gated mutation.
- Preferred packaging stance: separate large model assets from the main app package when practical.
- Preferred rollout: keep the current keyword assistant as fallback during migration.

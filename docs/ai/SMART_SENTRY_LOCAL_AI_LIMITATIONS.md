# Smart Sentry Local AI Limitations

## Purpose

This note documents the current known limitations of Smart Sentry's local Ollama-based assistant, the likely impact of each limitation, and practical ways to reduce that impact.

The current default local model is `llama3.2:latest` for fast interaction. A stronger but slower option is `gpt-oss:20b` for deeper analysis.

## Core Rule

The local model is used for reasoning, explanation, and operator guidance.

It is not the safety authority.

Live sentry movement, trigger logic, clamping, safety lock behavior, and hardware control should remain deterministic and explicitly gated by the app.

## Known Limitations

### 1. Limited reasoning depth compared with larger cloud models

What happens:
The local model can miss subtle multi-step causes, especially when the problem spans several subsystems at once such as camera state, YOLO load state, transport state, and engine state transitions.

Impact:
The assistant may produce a plausible answer that is incomplete or too generic.

Mitigation:
- Use deterministic runtime findings first and treat the model as an interpreter of those findings.
- Switch analyst-style tasks to `gpt-oss:20b` when you need deeper reasoning.
- Keep prompts grounded in the runtime snapshot instead of asking broad abstract questions.

### 2. Smaller context window than a full codebase review would need

What happens:
The live assistant cannot ingest the entire project and all logs on every request without becoming slow or noisy.

Impact:
It may miss relevant context unless that context is selected or summarized first.

Mitigation:
- Feed the model structured runtime excerpts, recent logs, and selected subsystem summaries rather than the full repo.
- Export runtime snapshots for focused analysis.
- Keep curated docs for important subsystems and use those as compact context.

### 3. Variable output quality across prompts

What happens:
The same local model can answer well on one runtime question and weakly on the next depending on prompt shape and runtime evidence quality.

Impact:
Some replies can be too verbose, too shallow, or oddly phrased.

Mitigation:
- Use structured prompts with explicit sections such as Current State, Risks, and Next Steps.
- Keep the system prompt strict and safety-focused.
- Prefer deterministic summaries plus model explanation over open-ended chat.

### 4. Slow responses on heavier local models

What happens:
Stronger local models such as `gpt-oss:20b` take noticeably longer than `llama3.2:latest`.

Impact:
This can make the assistant feel sluggish during live operation.

Mitigation:
- Use `llama3.2:latest` for fast UI interaction.
- Reserve `gpt-oss:20b` for analyst mode, exported snapshot review, or slower operator coaching.
- Keep prompts concise and avoid dumping unnecessary logs.

### 5. Hallucination risk still exists

What happens:
Even local models can infer hardware state or claim certainty beyond the actual evidence.

Impact:
An operator may trust a confident but partially incorrect explanation.

Mitigation:
- Keep deterministic findings visible beside the model answer.
- Treat the model as advisory, not authoritative.
- Require the assistant to separate observations from suggested actions.
- Do not let the model directly bypass hardware or safety gates.

### 6. Local model availability is not guaranteed

What happens:
Ollama may be stopped, unreachable, misconfigured, or missing the selected model.

Impact:
The assistant can become unavailable or fall back to deterministic guidance only.

Mitigation:
- Show provider health clearly in the AI tab.
- Keep deterministic runtime analysis available as a fallback.
- Keep at least one verified local fast model installed at all times.

### 6a. Spoken replies still depend on the local Qt speech path

What happens:
Spoken assistant replies require the Qt text-to-speech backend to be available, human voice mode to be enabled, and assistant auto-speak to be enabled. On Windows, the current Smart Sentry runtime uses the classic SAPI backend exposed through `QTextToSpeech`.

Impact:
The assistant can still answer in text while spoken replies remain unavailable, which can make the feature look partially broken if the operator expects voice by default. Voice enumeration alone is not enough to prove that speech will actually play.

Confirmed failure modes in the live v3.5.2 runtime:
- Persisted `sound.enabled = false` mutes the board-sound path at startup.
- Non-zero Qt pitch offsets can cause Windows SAPI to drop speech silently even while voices still enumerate correctly.
- A stale interrupt-stop cycle can leave the runtime permanently "busy" and block all later speech until that stale state is released.
- Repeated paused-state autotracking chatter can hide the real failure and make startup behavior look random.

Mitigation:
- Surface voice readiness clearly in the AI tab.
- Use the in-app current-voice and scan-all-voices validation buttons before treating speech as broken.
- Keep SAPI pitch neutral and tune rate, volume, phrasing, and voice choice instead of Qt pitch on that backend.
- Keep spoken replies short and summary-focused so the voice path stays usable during live operation.
- If speech worked and then stopped, inspect stale speech-state / interrupt handling first; do not assume the backend disappeared.

### 6b. Additional voices are OS-level, not app-level

What happens:
Smart Sentry only sees the voices that `QTextToSpeech` can access through classic Windows SAPI. In the current environment that is `Microsoft Zira Desktop` and `Microsoft David Desktop`. Windows OneCore may have additional voices installed, but QtTextToSpeech does not automatically expose them to the app.

Impact:
Adding a new in-app preset does not add a new voice. The operating system must provide a voice that the Qt SAPI backend can enumerate.

Mitigation:
- Install additional Windows desktop SAPI voices, not just in-app presets.
- Or expose compatible OneCore voices to the classic SAPI layer with an admin-level Windows change.
- After any OS-level voice change, restart Smart Sentry and use the voice scan tools in the AI tab to confirm visibility.

### 7. Poor performance if runtime evidence is incomplete

What happens:
If the controller link is down, the camera is closed, or telemetry is stale, the model only sees partial truth.

Impact:
The answer may be technically reasonable but still not identify the real fault.

Mitigation:
- Surface missing evidence explicitly in deterministic findings.
- Encourage snapshot export and hardware reconnection before deeper analysis.
- Treat stale telemetry itself as a first-class finding.

### 8. Prompt-triggered actions can be misunderstood if phrasing is vague

What happens:
An operator request like "check color mode" versus "switch to color mode" can imply different intent.

Impact:
The assistant may parse a supported action when the operator only wanted explanation, or the reverse.

Mitigation:
- Keep action execution permission-gated.
- Restrict automatic action parsing to explicit phrases.
- Prefer confirmation or clear action/result labeling in assistant output.

### 9. The model cannot replace subsystem-specific diagnostics

What happens:
A language model cannot replace direct hardware telemetry, camera diagnostics, YOLO load checks, or serial and UDP health validation.

Impact:
If the underlying instrumentation is weak, the model cannot compensate.

Mitigation:
- Keep investing in deterministic runtime analyzers.
- Add more structured health checks over time for servo drift, stale telemetry, repeated loss recovery, and current faults.
- Use the model to explain analyzer findings, not invent them.

### 10. Packaging and deployment remain separate from the model itself

What happens:
The app can ship correctly while the target machine still lacks Ollama or the needed model pull.

Impact:
The assistant UI may load but the model backend may not be usable yet.

Mitigation:
- Treat Ollama availability as an environment prerequisite.
- Provide a clear startup/provider status check.
- Keep the app functional even when the assistant is running in fallback mode.

## Practical Model Guidance

### Best current fast model

`llama3.2:latest`

Why:
- Fast enough for live UI use on this machine.
- Produces normal text responses through `/api/generate`.
- Good fit for operator chat, runtime summaries, and short explanations.

### Best current analyst model

`gpt-oss:20b`

Why:
- Better reasoning depth than `llama3.2:latest`.
- Useful for slower analysis tasks and exported runtime snapshots.

Tradeoff:
- Slower and heavier.

### Model to avoid as default

`gpt-oss:120b-cloud`

Why:
- Cloud-tagged rather than a good local default for this build.
- Not a reliable fit for Smart Sentry's local-first UI workflow.

## Recommended Operating Pattern

1. Use deterministic runtime analysis first.
2. Use `llama3.2:latest` for live assistant interaction.
3. Use `gpt-oss:20b` only when you deliberately want slower deeper analysis.
4. Keep action execution explicit and permission-gated.
5. Export runtime data when you need a more complete offline diagnosis.

## Future Improvements

Possible solutions that can reduce current limitations:

- Add a dedicated Runtime Analyst tab that shows deterministic findings separately from chat output.
- Add more structured anomaly detectors for servo lag, telemetry staleness, repeated recovery loops, and transport instability.
- Add clearer action confirmation so the assistant distinguishes pending, suggested, and executed actions.
- Add model-specific presets so fast chat and analyst mode automatically choose the right model.
- Add selective context packs for subsystems such as comms, camera, YOLO, and engagement tuning.
- Add a lightweight local classifier for intent parsing so action detection is less dependent on freeform prompting.

## Bottom Line

The current local AI is useful and practical, but it is not a replacement for deterministic sentry logic or direct hardware diagnostics.

Its best use is:
- explaining runtime state
- summarizing likely issues
- drafting operator next steps
- translating structured telemetry into readable guidance

Its weakest use is:
- being treated as a single source of truth
- replacing live instrumentation
- being trusted to control safety-critical behavior on its own
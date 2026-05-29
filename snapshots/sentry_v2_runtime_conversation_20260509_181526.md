# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-09 18:15:26
- Entries: 50
- Roles: {'assistant': 4, 'system': 1, 'operator': 45}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 1, 'spoken_confirmation': 2, 'voice_transcript_partial': 38, 'voice_transcript_final': 6, 'voice_command': 1}
- Channels: {'text': 2, 'voice': 48}
- Latest operator request: pir on loss recovery buzzer mute on
- Latest assistant message: That does not match a known command. Please repeat.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-09 18:04:34] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-09 18:04:34] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-09 18:04:36] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778321076.6998339 | source=vosk
- [2026-05-09 18:05:10] assistant / spoken_confirmation / voice: The smart Sentry is online now. Say the command.
  meta: interrupt=True | assistant_output=False | spoken=False
- [2026-05-09 18:05:17] operator / voice_transcript_partial / voice: mode switching
  meta: kind=partial | timestamp=1778321117.7406125 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:05:18] operator / voice_transcript_partial / voice: system
  meta: kind=partial | timestamp=1778321118.237704 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:05:19] operator / voice_transcript_final / voice: system
  meta: kind=final | timestamp=1778321119.589317 | source=final | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:05:32] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1778321132.7367187 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:05:32] operator / voice_transcript_partial / voice: no detection
  meta: kind=partial | timestamp=1778321132.9884853 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:05:33] operator / voice_transcript_partial / voice: no fire
  meta: kind=partial | timestamp=1778321133.24056 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:05:33] operator / voice_transcript_partial / voice: no detection
  meta: kind=partial | timestamp=1778321133.489995 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:05:33] operator / voice_transcript_partial / voice: no greeting
  meta: kind=partial | timestamp=1778321133.740288 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:05:33] operator / voice_transcript_partial / voice: no cleanup on
  meta: kind=partial | timestamp=1778321133.9909263 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:05:34] operator / voice_transcript_partial / voice: no cleanup on the
  meta: kind=partial | timestamp=1778321134.2444608 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:05:34] operator / voice_transcript_partial / voice: no cleanup on the current
  meta: kind=partial | timestamp=1778321134.9889555 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:05:35] operator / voice_transcript_partial / voice: no cleanup on the hello
  meta: kind=partial | timestamp=1778321135.2389793 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:05:35] operator / voice_transcript_partial / voice: no cleanup on the hello run
  meta: kind=partial | timestamp=1778321135.7437243 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:05:35] operator / voice_transcript_partial / voice: no cleanup on the hello run face
  meta: kind=partial | timestamp=1778321135.9926715 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:05:36] operator / voice_transcript_partial / voice: no cleanup on the hello run the
  meta: kind=partial | timestamp=1778321136.2384753 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:05:36] operator / voice_transcript_partial / voice: no cleanup on the hello run the name
  meta: kind=partial | timestamp=1778321136.4899294 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:05:36] operator / voice_transcript_partial / voice: no cleanup on the hello run the name pir guard
  meta: kind=partial | timestamp=1778321136.9962602 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:05:37] operator / voice_transcript_partial / voice: no cleanup on the hello run the name diagnostics
  meta: kind=partial | timestamp=1778321137.2381697 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:05:37] operator / voice_transcript_partial / voice: no cleanup on the hello run the name for engaging adaptive
  meta: kind=partial | timestamp=1778321137.4865105 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:05:38] operator / voice_transcript_partial / voice: no cleanup on the hello run the name pir guard running
  meta: kind=partial | timestamp=1778321138.2458646 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:05:38] operator / voice_transcript_final / voice: no cleanup on the hello run the name pir guard running
  meta: kind=final | timestamp=1778321138.8927794 | source=final | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:05:58] operator / voice_transcript_partial / voice: ai
  meta: kind=partial | timestamp=1778321158.9768405 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:06:00] operator / voice_transcript_final / voice: ai
  meta: kind=final | timestamp=1778321160.3233535 | source=final | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:06:28] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778321188.2306755 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:06:54] operator / voice_transcript_partial / voice: on port the
  meta: kind=partial | timestamp=1778321214.987335 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:07:01] operator / voice_transcript_partial / voice: on port the guard
  meta: kind=partial | timestamp=1778321221.9824102 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:07:04] operator / voice_transcript_partial / voice: on port the go
  meta: kind=partial | timestamp=1778321224.480364 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:07:11] operator / voice_transcript_final / voice: aim on port the go model
  meta: kind=final | timestamp=1778321231.8719273 | source=final | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:07:12] operator / voice_transcript_partial / voice: use nano
  meta: kind=partial | timestamp=1778321232.4152703 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:07:25] operator / voice_transcript_partial / voice: use nano model
  meta: kind=partial | timestamp=1778321245.1708422 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:07:32] operator / voice_transcript_final / voice: use nano model
  meta: kind=final | timestamp=1778321252.4239967 | source=final | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:07:33] operator / voice_command / voice: use nano model
  meta: normalized=True
- [2026-05-09 18:07:33] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-09 18:13:17] operator / voice_transcript_partial / voice: pir on loss
  meta: kind=partial | timestamp=1778321597.2111812 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:13:25] operator / voice_transcript_partial / voice: pir on loss precision
  meta: kind=partial | timestamp=1778321605.4331355 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:13:25] operator / voice_transcript_partial / voice: pir on loss recovery
  meta: kind=partial | timestamp=1778321605.6873755 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:13:31] operator / voice_transcript_partial / voice: pir on loss recovery buzzer
  meta: kind=partial | timestamp=1778321611.683242 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:13:32] operator / voice_transcript_partial / voice: pir on loss recovery buzzer mute on
  meta: kind=partial | timestamp=1778321612.215944 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:13:32] operator / voice_transcript_partial / voice: pir on loss recovery buzzer mute
  meta: kind=partial | timestamp=1778321612.4357028 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:13:42] operator / voice_transcript_final / voice: pir on loss recovery buzzer mute on
  meta: kind=final | timestamp=1778321622.5958607 | source=final | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:13:43] operator / voice_transcript_partial / voice: auto
  meta: kind=partial | timestamp=1778321623.194943 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:13:43] operator / voice_transcript_partial / voice: requirement
  meta: kind=partial | timestamp=1778321623.4351246 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:13:46] operator / voice_transcript_partial / voice: requirement go rest
  meta: kind=partial | timestamp=1778321626.9532216 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:13:47] operator / voice_transcript_partial / voice: auto trigger greeting gesture
  meta: kind=partial | timestamp=1778321627.1850204 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:13:47] operator / voice_transcript_partial / voice: auto trigger running
  meta: kind=partial | timestamp=1778321627.4344482 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017
- [2026-05-09 18:13:47] operator / voice_transcript_partial / voice: auto trigger greeting gesture
  meta: kind=partial | timestamp=1778321627.6865594 | source=vosk | frequency_hz=391.1 | rms=301 | updated_at=1778321087.7300017

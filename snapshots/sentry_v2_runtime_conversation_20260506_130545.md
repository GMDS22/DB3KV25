# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-06 13:05:45
- Entries: 115
- Roles: {'assistant': 7, 'system': 1, 'operator': 107}
- Event types: {'assistant_prompt': 3, 'assistant_analysis': 1, 'voice_status': 1, 'voice_transcript_final': 19, 'spoken_confirmation': 3, 'voice_transcript_partial': 82, 'voice_command': 6}
- Channels: {'text': 4, 'voice': 111}
- Latest operator request: tracking no one targets in view
- Latest assistant message: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] Parsed Intent: - action=none confidence=1.00 clarification=False I am Elion Mosk, Elion for short, Smart Sentry's runtime assistant built by GM Labs as Gino's personal project. I handle live analysis, diagnostics, and supported runtime commands.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-06 13:02:35] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-06 13:02:35] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-06 13:02:37] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778043757.6656344 | source=vosk
- [2026-05-06 13:03:13] operator / voice_transcript_final / voice: hey
  meta: kind=final | timestamp=1778043793.5737948 | source=final | frequency_hz=306.0 | rms=294 | updated_at=1778043759.009161
- [2026-05-06 13:03:16] assistant / spoken_confirmation / voice: Smart Sentry AI is online. Ask a question or give a command when ready.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 13:03:22] operator / voice_transcript_final / voice: smart sentry ai is on light
  meta: kind=final | timestamp=1778043802.126252 | source=final | frequency_hz=286.0 | rms=491 | updated_at=1778043801.7014751
- [2026-05-06 13:03:22] operator / voice_transcript_partial / voice: mask
  meta: kind=partial | timestamp=1778043802.2170868 | source=vosk | frequency_hz=286.0 | rms=491 | updated_at=1778043801.7014751
- [2026-05-06 13:03:22] operator / voice_transcript_partial / voice: ask a question
  meta: kind=partial | timestamp=1778043802.459382 | source=vosk | frequency_hz=286.0 | rms=491 | updated_at=1778043801.7014751
- [2026-05-06 13:03:23] operator / voice_transcript_partial / voice: ask a question give acoustic
  meta: kind=partial | timestamp=1778043803.2097635 | source=vosk | frequency_hz=286.0 | rms=491 | updated_at=1778043801.7014751
- [2026-05-06 13:03:23] operator / voice_transcript_partial / voice: ask a question give
  meta: kind=partial | timestamp=1778043803.5328572 | source=vosk | frequency_hz=286.0 | rms=491 | updated_at=1778043801.7014751
- [2026-05-06 13:03:23] operator / voice_transcript_partial / voice: ask a question give command
  meta: kind=partial | timestamp=1778043803.710061 | source=vosk | frequency_hz=286.0 | rms=491 | updated_at=1778043801.7014751
- [2026-05-06 13:03:23] operator / voice_transcript_partial / voice: ask a question give command to rest
  meta: kind=partial | timestamp=1778043803.9603882 | source=vosk | frequency_hz=286.0 | rms=491 | updated_at=1778043801.7014751
- [2026-05-06 13:03:24] operator / voice_transcript_partial / voice: ask a question give command running
  meta: kind=partial | timestamp=1778043804.2108781 | source=vosk | frequency_hz=286.0 | rms=491 | updated_at=1778043801.7014751
- [2026-05-06 13:03:24] operator / voice_transcript_final / voice: mask a question give command running
  meta: kind=final | timestamp=1778043804.7335598 | source=final | frequency_hz=286.0 | rms=491 | updated_at=1778043801.7014751
- [2026-05-06 13:03:27] operator / voice_transcript_partial / voice: run the
  meta: kind=partial | timestamp=1778043807.7427113 | source=vosk | frequency_hz=286.0 | rms=491 | updated_at=1778043801.7014751
- [2026-05-06 13:03:29] operator / voice_transcript_final / voice: run the
  meta: kind=final | timestamp=1778043809.0948155 | source=final | frequency_hz=286.0 | rms=491 | updated_at=1778043801.7014751
- [2026-05-06 13:03:34] operator / voice_transcript_partial / voice: run smart
  meta: kind=partial | timestamp=1778043814.4909 | source=vosk | frequency_hz=286.0 | rms=491 | updated_at=1778043801.7014751
- [2026-05-06 13:03:34] operator / voice_transcript_partial / voice: run smart sentry
  meta: kind=partial | timestamp=1778043814.7405777 | source=vosk | frequency_hz=286.0 | rms=491 | updated_at=1778043801.7014751
- [2026-05-06 13:03:35] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1778043815.9961922 | source=final | frequency_hz=286.0 | rms=491 | updated_at=1778043801.7014751
- [2026-05-06 13:03:36] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-05-06 13:03:36] assistant / spoken_confirmation / voice: Connecting Smart Sentry boards now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 13:03:40] operator / voice_transcript_partial / voice: setting guard no active
  meta: kind=partial | timestamp=1778043820.0473819 | source=vosk | frequency_hz=286.0 | rms=491 | updated_at=1778043801.7014751
- [2026-05-06 13:03:40] operator / voice_transcript_partial / voice: setting guard no active target matching
  meta: kind=partial | timestamp=1778043820.5507207 | source=vosk | frequency_hz=286.0 | rms=491 | updated_at=1778043801.7014751
- [2026-05-06 13:03:40] operator / voice_transcript_partial / voice: setting guard no active target
  meta: kind=partial | timestamp=1778043820.7954628 | source=vosk | frequency_hz=286.0 | rms=491 | updated_at=1778043801.7014751
- [2026-05-06 13:03:41] operator / voice_transcript_partial / voice: setting guard no active target matching
  meta: kind=partial | timestamp=1778043821.0429816 | source=vosk | frequency_hz=286.0 | rms=491 | updated_at=1778043801.7014751
- [2026-05-06 13:03:41] operator / voice_transcript_partial / voice: setting guard no active target no
  meta: kind=partial | timestamp=1778043821.2924218 | source=vosk | frequency_hz=286.0 | rms=491 | updated_at=1778043801.7014751
- [2026-05-06 13:03:42] operator / voice_transcript_final / voice: setting guard no active target no
  meta: kind=final | timestamp=1778043822.917708 | source=final | frequency_hz=286.0 | rms=491 | updated_at=1778043801.7014751
- [2026-05-06 13:03:43] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778043823.99679 | source=vosk | frequency_hz=286.0 | rms=491 | updated_at=1778043801.7014751
- [2026-05-06 13:03:51] operator / voice_transcript_partial / voice: aiming on no fire
  meta: kind=partial | timestamp=1778043831.8294737 | source=vosk | frequency_hz=260.0 | rms=256 | updated_at=1778043828.0666745
- [2026-05-06 13:03:52] operator / voice_transcript_partial / voice: aiming on no fire no
  meta: kind=partial | timestamp=1778043832.0756867 | source=vosk | frequency_hz=260.0 | rms=256 | updated_at=1778043828.0666745
- [2026-05-06 13:03:52] operator / voice_transcript_final / voice: aiming guard no targets running no
  meta: kind=final | timestamp=1778043832.950312 | source=final | frequency_hz=260.0 | rms=256 | updated_at=1778043828.0666745
- [2026-05-06 13:03:54] operator / voice_transcript_partial / voice: overlay
  meta: kind=partial | timestamp=1778043834.7306082 | source=vosk | frequency_hz=260.0 | rms=256 | updated_at=1778043828.0666745
- [2026-05-06 13:03:55] operator / voice_transcript_partial / voice: overlay guard
  meta: kind=partial | timestamp=1778043835.2299619 | source=vosk | frequency_hz=260.0 | rms=256 | updated_at=1778043828.0666745
- [2026-05-06 13:03:55] operator / voice_transcript_partial / voice: overlay guard zone
  meta: kind=partial | timestamp=1778043835.4743948 | source=vosk | frequency_hz=260.0 | rms=256 | updated_at=1778043828.0666745
- [2026-05-06 13:03:55] operator / voice_transcript_partial / voice: overlay guard targets
  meta: kind=partial | timestamp=1778043835.7233217 | source=vosk | frequency_hz=260.0 | rms=256 | updated_at=1778043828.0666745
- [2026-05-06 13:03:56] operator / voice_transcript_partial / voice: overlay guard targets in view
  meta: kind=partial | timestamp=1778043836.2234893 | source=vosk | frequency_hz=260.0 | rms=256 | updated_at=1778043828.0666745
- [2026-05-06 13:03:57] operator / voice_transcript_final / voice: overlay guard targets in view
  meta: kind=final | timestamp=1778043837.5332103 | source=final | frequency_hz=260.0 | rms=256 | updated_at=1778043828.0666745
- [2026-05-06 13:04:01] operator / voice_transcript_partial / voice: open the
  meta: kind=partial | timestamp=1778043841.551641 | source=vosk | frequency_hz=260.0 | rms=256 | updated_at=1778043828.0666745
- [2026-05-06 13:04:01] operator / voice_transcript_partial / voice: open ai
  meta: kind=partial | timestamp=1778043841.7947228 | source=vosk | frequency_hz=260.0 | rms=256 | updated_at=1778043828.0666745
- [2026-05-06 13:04:02] operator / voice_transcript_partial / voice: open ai tab
  meta: kind=partial | timestamp=1778043842.312501 | source=vosk | frequency_hz=260.0 | rms=256 | updated_at=1778043828.0666745
- [2026-05-06 13:04:03] operator / voice_transcript_final / voice: open tab
  meta: kind=final | timestamp=1778043843.1395915 | source=final | frequency_hz=260.0 | rms=256 | updated_at=1778043828.0666745
- [2026-05-06 13:04:03] operator / voice_command / voice: open tab
  meta: normalized=True
- [2026-05-06 13:04:04] assistant / spoken_confirmation / voice: I could not map that to a command yet. Please say it again.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 13:04:09] operator / voice_transcript_partial / voice: the guard targets on
  meta: kind=partial | timestamp=1778043849.867942 | source=vosk | frequency_hz=153.2 | rms=456 | updated_at=1778043848.8328474
- [2026-05-06 13:04:10] operator / voice_transcript_partial / voice: the guard targets running
  meta: kind=partial | timestamp=1778043850.1203759 | source=vosk | frequency_hz=126.9 | rms=226 | updated_at=1778043850.1118643
- [2026-05-06 13:04:10] operator / voice_transcript_final / voice: the guard targets running
  meta: kind=final | timestamp=1778043850.7708027 | source=final | frequency_hz=126.9 | rms=226 | updated_at=1778043850.1118643
- [2026-05-06 13:04:12] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1778043852.060515 | source=vosk | frequency_hz=126.9 | rms=226 | updated_at=1778043850.1118643
- [2026-05-06 13:04:12] operator / voice_transcript_partial / voice: alion who are you
  meta: kind=partial | timestamp=1778043852.8680801 | source=vosk | frequency_hz=126.9 | rms=226 | updated_at=1778043850.1118643
- [2026-05-06 13:04:13] operator / voice_transcript_partial / voice: alion who are you checking
  meta: kind=partial | timestamp=1778043853.1263397 | source=vosk | frequency_hz=126.9 | rms=226 | updated_at=1778043850.1118643
- [2026-05-06 13:04:13] operator / voice_transcript_partial / voice: alion who are you guard
  meta: kind=partial | timestamp=1778043853.4830687 | source=vosk | frequency_hz=126.9 | rms=226 | updated_at=1778043850.1118643
- [2026-05-06 13:04:13] operator / voice_transcript_partial / voice: alion who are you guard detection
  meta: kind=partial | timestamp=1778043853.8760471 | source=vosk | frequency_hz=126.9 | rms=226 | updated_at=1778043850.1118643
- [2026-05-06 13:04:14] operator / voice_transcript_partial / voice: alion who are you guard detection on visual overlay
  meta: kind=partial | timestamp=1778043854.128831 | source=vosk | frequency_hz=126.9 | rms=226 | updated_at=1778043850.1118643
- [2026-05-06 13:04:14] operator / voice_transcript_partial / voice: alion who are you guard detection on visual sound
  meta: kind=partial | timestamp=1778043854.3723967 | source=vosk | frequency_hz=126.9 | rms=226 | updated_at=1778043850.1118643
- [2026-05-06 13:04:14] operator / voice_transcript_partial / voice: alion who are you guard detection on visual sound announcements
  meta: kind=partial | timestamp=1778043854.8668222 | source=vosk | frequency_hz=126.9 | rms=226 | updated_at=1778043850.1118643
- [2026-05-06 13:04:15] operator / voice_transcript_partial / voice: alion who are you guard detection on visual sound of threat
  meta: kind=partial | timestamp=1778043855.1230156 | source=vosk | frequency_hz=126.9 | rms=226 | updated_at=1778043850.1118643
- [2026-05-06 13:04:15] operator / voice_transcript_partial / voice: alion who are you guard detection on visual sound of threat scores
  meta: kind=partial | timestamp=1778043855.625552 | source=vosk | frequency_hz=126.9 | rms=226 | updated_at=1778043850.1118643
- [2026-05-06 13:04:16] operator / voice_transcript_partial / voice: alion who are you guard detection on visual sound of threat
  meta: kind=partial | timestamp=1778043856.3803475 | source=vosk | frequency_hz=126.9 | rms=226 | updated_at=1778043850.1118643
- [2026-05-06 13:04:16] operator / voice_transcript_partial / voice: alion who are you guard detection on visual sound of threat disable is
  meta: kind=partial | timestamp=1778043856.62597 | source=vosk | frequency_hz=126.9 | rms=226 | updated_at=1778043850.1118643
- [2026-05-06 13:04:16] operator / voice_transcript_partial / voice: alion who are you guard detection on visual sound of threat disable is event blink
  meta: kind=partial | timestamp=1778043856.8710315 | source=vosk | frequency_hz=126.9 | rms=226 | updated_at=1778043850.1118643
- [2026-05-06 13:04:17] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 13:04:17] operator / voice_transcript_partial / voice: alion who are you guard detection on visual sound of threat disable is of of face
  meta: kind=partial | timestamp=1778043857.1309083 | source=vosk | frequency_hz=126.9 | rms=226 | updated_at=1778043850.1118643
- [2026-05-06 13:04:17] operator / voice_transcript_partial / voice: alion who are you guard detection on visual sound of threat disable is of of face id
  meta: kind=partial | timestamp=1778043857.3680375 | source=vosk | frequency_hz=126.9 | rms=226 | updated_at=1778043850.1118643
- [2026-05-06 13:04:18] operator / voice_transcript_partial / voice: alion who are you guard detection on visual sound of threat disable is of of face id current
  meta: kind=partial | timestamp=1778043858.205319 | source=vosk | frequency_hz=126.9 | rms=226 | updated_at=1778043850.1118643
- [2026-05-06 13:04:18] operator / voice_transcript_partial / voice: alion who are you guard detection on visual sound of threat disable is of of face id current status
  meta: kind=partial | timestamp=1778043858.3740246 | source=vosk | frequency_hz=126.9 | rms=226 | updated_at=1778043850.1118643
- [2026-05-06 13:04:19] operator / voice_transcript_partial / voice: alion who are you guard detection on visual sound of threat disable is of of face id current status guarding mode
  meta: kind=partial | timestamp=1778043859.4081829 | source=vosk | frequency_hz=126.9 | rms=226 | updated_at=1778043850.1118643
- [2026-05-06 13:04:19] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 13:04:22] operator / voice_transcript_final / voice: elion who are you guard detection on visual sound of threat disable is of of face id current status guarding
  meta: kind=final | timestamp=1778043862.1554153 | source=final | frequency_hz=78.0 | rms=595 | updated_at=1778043859.9019544
- [2026-05-06 13:04:22] operator / voice_command / voice: elion who are you guard detection on visual sound of threat disable is of of face id current status guarding
  meta: normalized=True
- [2026-05-06 13:04:23] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] Parsed Intent: - action=none confidence=1.00 clarification=False I am Elion Mosk, or Elion for short, the AI runtime assistant for Smart Sentry. I was created by GM Labs as a personal project by Gino. Right now, I provide live runtime awareness and operator support inside the running app: I can analyze current behavior, explain what the system is doing, surface likely causes when something is not loading, handle supported local control commands, and apply supported setting updates while keeping replies grounded in real runtime state. I also assist with face, tracking, trigger, guard, and assistant-related diagnostics using the app's current telemetry and configuration. Some areas are still a work in progress, and this assistant is actively evolving. Planned future capabilities include deeper autonomous diagnostics, smarter cross-subsystem fault correlation, broader natural-language command coverage, more proactive safety checks, richer memory/context handling across longer sessions, improved multimodal understanding, and tighter integration with future Smart Sentry hardware and automation workflows. I stay grounded in the running app and its supported controls. I do not invent hardware state or pretend unsupported actions already happened. I am actively improving while remaining grounded in what the app is actually doing now.
  meta: task_kind=prompt | speak_requested=True
- [2026-05-06 13:04:23] operator / voice_transcript_final / voice: who are you
  meta: kind=final | timestamp=1778043863.2661147 | source=final | frequency_hz=78.0 | rms=595 | updated_at=1778043859.9019544
- [2026-05-06 13:04:23] operator / voice_command / voice: who are you
  meta: normalized=True
- [2026-05-06 13:04:23] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] Parsed Intent: - action=none confidence=1.00 clarification=False I am Elion Mosk, Elion for short, Smart Sentry's runtime assistant built by GM Labs as Gino's personal project. I handle live analysis, diagnostics, and supported runtime commands.
  meta: task_kind=prompt | speak_requested=True
- [2026-05-06 13:04:24] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778043864.7373388 | source=vosk | frequency_hz=78.0 | rms=595 | updated_at=1778043859.9019544
- [2026-05-06 13:04:24] operator / voice_transcript_partial / voice: the pan
  meta: kind=partial | timestamp=1778043864.761873 | source=vosk | frequency_hz=78.0 | rms=595 | updated_at=1778043859.9019544
- [2026-05-06 13:04:24] operator / voice_transcript_partial / voice: the pan commands
  meta: kind=partial | timestamp=1778043864.8372774 | source=vosk | frequency_hz=78.0 | rms=595 | updated_at=1778043859.9019544
- [2026-05-06 13:04:25] operator / voice_transcript_partial / voice: the pan command
  meta: kind=partial | timestamp=1778043865.060742 | source=vosk | frequency_hz=78.0 | rms=595 | updated_at=1778043859.9019544
- [2026-05-06 13:04:25] operator / voice_transcript_partial / voice: the pan command tuning
  meta: kind=partial | timestamp=1778043865.3121958 | source=vosk | frequency_hz=78.0 | rms=595 | updated_at=1778043859.9019544
- [2026-05-06 13:04:25] operator / voice_transcript_partial / voice: the pan command a joke
  meta: kind=partial | timestamp=1778043865.563989 | source=vosk | frequency_hz=78.0 | rms=595 | updated_at=1778043859.9019544
- [2026-05-06 13:04:37] operator / voice_transcript_partial / voice: inversion no confidence
  meta: kind=partial | timestamp=1778043877.833268 | source=vosk | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:04:38] operator / voice_transcript_partial / voice: inversion no confidence is the
  meta: kind=partial | timestamp=1778043878.5313752 | source=vosk | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:04:39] operator / voice_transcript_partial / voice: inversion no confidence is the one pir
  meta: kind=partial | timestamp=1778043879.054141 | source=vosk | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:04:39] operator / voice_transcript_partial / voice: inversion no confidence is the one pir sensors
  meta: kind=partial | timestamp=1778043879.0656607 | source=vosk | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:04:39] operator / voice_transcript_partial / voice: inversion no confidence is the one pir sensors lion
  meta: kind=partial | timestamp=1778043879.5301197 | source=vosk | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:04:39] operator / voice_transcript_partial / voice: inversion no confidence is the one pir sensors lighting of the
  meta: kind=partial | timestamp=1778043879.77903 | source=vosk | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:04:40] operator / voice_transcript_partial / voice: inversion no confidence is the one pir sensors lighting of the ai
  meta: kind=partial | timestamp=1778043880.2791677 | source=vosk | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:04:41] operator / voice_transcript_final / voice: inversion no confidence is the one pir sensors lighting of the aim
  meta: kind=final | timestamp=1778043881.0550044 | source=final | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:05:05] operator / voice_transcript_partial / voice: standby guard no active
  meta: kind=partial | timestamp=1778043905.537861 | source=vosk | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:05:06] operator / voice_transcript_partial / voice: standby guard no active targets running
  meta: kind=partial | timestamp=1778043906.0305884 | source=vosk | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:05:06] operator / voice_transcript_partial / voice: standby guard no active targets running known
  meta: kind=partial | timestamp=1778043906.2905772 | source=vosk | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:05:06] operator / voice_transcript_partial / voice: standby guard no active targets running no
  meta: kind=partial | timestamp=1778043906.530677 | source=vosk | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:05:07] operator / voice_transcript_final / voice: standby guard no active targets running no
  meta: kind=final | timestamp=1778043907.4127948 | source=final | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:05:09] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1778043909.533573 | source=vosk | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:05:11] operator / voice_transcript_partial / voice: tracking known one target
  meta: kind=partial | timestamp=1778043911.1226578 | source=vosk | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:05:11] operator / voice_transcript_partial / voice: tracking known one target view
  meta: kind=partial | timestamp=1778043911.6217668 | source=vosk | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:05:11] operator / voice_transcript_partial / voice: tracking known one target view keyboard
  meta: kind=partial | timestamp=1778043911.8825855 | source=vosk | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:05:12] operator / voice_transcript_partial / voice: tracking known one target view pir guard
  meta: kind=partial | timestamp=1778043912.1278198 | source=vosk | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:05:12] operator / voice_transcript_partial / voice: tracking known one target view pir guard hey
  meta: kind=partial | timestamp=1778043912.3759942 | source=vosk | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:05:12] operator / voice_transcript_partial / voice: tracking known one target view pir guard hey position
  meta: kind=partial | timestamp=1778043912.8716333 | source=vosk | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:05:13] operator / voice_transcript_partial / voice: tracking known one target view pir guard hey position no
  meta: kind=partial | timestamp=1778043913.3745031 | source=vosk | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:05:14] operator / voice_transcript_final / voice: tracking known one target in view pir guard hey position no
  meta: kind=final | timestamp=1778043914.8678365 | source=final | frequency_hz=128.9 | rms=458 | updated_at=1778043876.0229776
- [2026-05-06 13:05:17] operator / voice_transcript_partial / voice: human voice
  meta: kind=partial | timestamp=1778043917.9053729 | source=vosk | frequency_hz=74.0 | rms=282 | updated_at=1778043915.3938632
- [2026-05-06 13:05:19] operator / voice_transcript_partial / voice: for human voice
  meta: kind=partial | timestamp=1778043919.4254155 | source=vosk | frequency_hz=74.0 | rms=282 | updated_at=1778043915.3938632
- [2026-05-06 13:05:19] operator / voice_transcript_partial / voice: video loop running
  meta: kind=partial | timestamp=1778043919.6563342 | source=vosk | frequency_hz=74.0 | rms=282 | updated_at=1778043915.3938632
- [2026-05-06 13:05:20] operator / voice_transcript_final / voice: video loop running
  meta: kind=final | timestamp=1778043920.5565038 | source=final | frequency_hz=74.0 | rms=282 | updated_at=1778043915.3938632
- [2026-05-06 13:05:20] operator / voice_transcript_partial / voice: ml
  meta: kind=partial | timestamp=1778043920.6499367 | source=vosk | frequency_hz=74.0 | rms=282 | updated_at=1778043915.3938632
- [2026-05-06 13:05:20] operator / voice_transcript_partial / voice: ml scoring
  meta: kind=partial | timestamp=1778043920.905257 | source=vosk | frequency_hz=74.0 | rms=282 | updated_at=1778043915.3938632
- [2026-05-06 13:05:21] operator / voice_transcript_partial / voice: ml refinement
  meta: kind=partial | timestamp=1778043921.1583939 | source=vosk | frequency_hz=74.0 | rms=282 | updated_at=1778043915.3938632
- [2026-05-06 13:05:21] operator / voice_transcript_partial / voice: ml
  meta: kind=partial | timestamp=1778043921.407117 | source=vosk | frequency_hz=74.0 | rms=282 | updated_at=1778043915.3938632
- [2026-05-06 13:05:22] operator / voice_transcript_partial / voice: for human
  meta: kind=partial | timestamp=1778043922.4852042 | source=vosk | frequency_hz=74.0 | rms=282 | updated_at=1778043915.3938632
- [2026-05-06 13:05:22] operator / voice_transcript_partial / voice: for human voice
  meta: kind=partial | timestamp=1778043922.4958882 | source=vosk | frequency_hz=74.0 | rms=282 | updated_at=1778043915.3938632
- [2026-05-06 13:05:23] operator / voice_transcript_final / voice: ml human
  meta: kind=final | timestamp=1778043923.4625335 | source=final | frequency_hz=74.0 | rms=282 | updated_at=1778043915.3938632
- [2026-05-06 13:05:28] operator / voice_transcript_final / voice: logging
  meta: kind=final | timestamp=1778043928.1515858 | source=final | frequency_hz=74.0 | rms=282 | updated_at=1778043915.3938632
- [2026-05-06 13:05:34] operator / voice_transcript_partial / voice: tracking no one targets
  meta: kind=partial | timestamp=1778043934.0519757 | source=vosk | frequency_hz=74.0 | rms=282 | updated_at=1778043915.3938632
- [2026-05-06 13:05:34] operator / voice_transcript_partial / voice: tracking no one targets in view
  meta: kind=partial | timestamp=1778043934.575857 | source=vosk | frequency_hz=74.0 | rms=282 | updated_at=1778043915.3938632
- [2026-05-06 13:05:35] operator / voice_transcript_final / voice: tracking no one targets in view
  meta: kind=final | timestamp=1778043935.402905 | source=final | frequency_hz=74.0 | rms=282 | updated_at=1778043915.3938632

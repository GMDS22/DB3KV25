# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-06 12:41:52
- Entries: 134
- Roles: {'assistant': 15, 'system': 1, 'operator': 118}
- Event types: {'assistant_prompt': 2, 'assistant_analysis': 1, 'voice_status': 1, 'voice_transcript_partial': 77, 'spoken_confirmation': 12, 'voice_transcript_final': 26, 'voice_command': 15}
- Channels: {'text': 3, 'voice': 131}
- Latest operator request: what s
- Latest assistant message: I heard the request, but only the registered operator can change Smart Sentry settings.

## Timeline

- [2026-05-06 12:34:30] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-06 12:34:30] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-06 12:34:32] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778042072.3223264 | source=vosk
- [2026-05-06 12:34:49] operator / voice_transcript_partial / voice: hey
  meta: kind=partial | timestamp=1778042089.613714 | source=vosk
- [2026-05-06 12:35:11] assistant / spoken_confirmation / voice: Elion is ready. Tell me what you want checked, changed, or explained.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 12:35:18] operator / voice_transcript_final / voice: id
  meta: kind=final | timestamp=1778042118.7365563 | source=final | frequency_hz=211.9 | rms=609 | updated_at=1778042116.1170313
- [2026-05-06 12:35:19] operator / voice_transcript_partial / voice: leon
  meta: kind=partial | timestamp=1778042119.2633023 | source=vosk | frequency_hz=211.9 | rms=609 | updated_at=1778042116.1170313
- [2026-05-06 12:35:19] operator / voice_transcript_partial / voice: leon off
  meta: kind=partial | timestamp=1778042119.3763502 | source=vosk | frequency_hz=211.9 | rms=609 | updated_at=1778042116.1170313
- [2026-05-06 12:35:20] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 12:35:25] operator / voice_transcript_partial / voice: standby go
  meta: kind=partial | timestamp=1778042125.2052193 | source=vosk | frequency_hz=211.9 | rms=609 | updated_at=1778042116.1170313
- [2026-05-06 12:35:25] operator / voice_transcript_final / voice: standby guard
  meta: kind=final | timestamp=1778042125.3237045 | source=final | frequency_hz=211.9 | rms=609 | updated_at=1778042116.1170313
- [2026-05-06 12:35:28] operator / voice_transcript_partial / voice: who are
  meta: kind=partial | timestamp=1778042128.9545114 | source=vosk | frequency_hz=360.0 | rms=1184 | updated_at=1778042128.4476585
- [2026-05-06 12:35:29] operator / voice_transcript_partial / voice: who are you
  meta: kind=partial | timestamp=1778042129.204651 | source=vosk | frequency_hz=360.0 | rms=1184 | updated_at=1778042128.4476585
- [2026-05-06 12:35:30] operator / voice_transcript_final / voice: who are you
  meta: kind=final | timestamp=1778042130.3336732 | source=final | frequency_hz=350.9 | rms=1201 | updated_at=1778042129.6972032
- [2026-05-06 12:35:30] operator / voice_command / voice: who are you
  meta: normalized=True
- [2026-05-06 12:35:30] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] Parsed Intent: - action=none confidence=1.00 clarification=False I am Elion Mosk, or Elion for short, the AI runtime assistant for Smart Sentry. I was created by GM Labs as a personal project by Gino. Right now, I provide live runtime awareness and operator support inside the running app: I can analyze current behavior, explain what the system is doing, surface likely causes when something is not loading, handle supported local control commands, and apply supported setting updates while keeping replies grounded in real runtime state. I also assist with face, tracking, trigger, guard, and assistant-related diagnostics using the app's current telemetry and configuration. Some areas are still a work in progress, and this assistant is actively evolving. Planned future capabilities include deeper autonomous diagnostics, smarter cross-subsystem fault correlation, broader natural-language command coverage, more proactive safety checks, richer memory/context handling across longer sessions, improved multimodal understanding, and tighter integration with future Smart Sentry hardware and automation workflows. I stay grounded in the running app and its supported controls. I do not invent hardware state or pretend unsupported actions already happened. I stay focused on verified runtime state and supported controls.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-06 12:35:40] operator / voice_transcript_final / voice: standby guard no
  meta: kind=final | timestamp=1778042140.0701308 | source=final | frequency_hz=68.0 | rms=1201 | updated_at=1778042139.0393212
- [2026-05-06 12:38:36] operator / voice_transcript_partial / voice: run the
  meta: kind=partial | timestamp=1778042316.6330955 | source=vosk | frequency_hz=349.5 | rms=841 | updated_at=1778042147.368287
- [2026-05-06 12:38:37] operator / voice_transcript_final / voice: run the
  meta: kind=final | timestamp=1778042317.7310367 | source=final | frequency_hz=349.5 | rms=841 | updated_at=1778042147.368287
- [2026-05-06 12:38:44] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1778042324.313828 | source=vosk | frequency_hz=349.5 | rms=841 | updated_at=1778042147.368287
- [2026-05-06 12:38:44] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 12:38:44] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1778042324.5633645 | source=vosk | frequency_hz=349.5 | rms=841 | updated_at=1778042147.368287
- [2026-05-06 12:38:45] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1778042325.3916993 | source=final | frequency_hz=349.5 | rms=841 | updated_at=1778042147.368287
- [2026-05-06 12:38:45] operator / voice_transcript_partial / voice: run the
  meta: kind=partial | timestamp=1778042325.8076553 | source=vosk | frequency_hz=349.5 | rms=841 | updated_at=1778042147.368287
- [2026-05-06 12:38:46] operator / voice_transcript_partial / voice: run the app
  meta: kind=partial | timestamp=1778042326.3091075 | source=vosk | frequency_hz=349.5 | rms=841 | updated_at=1778042147.368287
- [2026-05-06 12:38:47] operator / voice_transcript_final / voice: run the app
  meta: kind=final | timestamp=1778042327.1984897 | source=final | frequency_hz=349.5 | rms=841 | updated_at=1778042147.368287
- [2026-05-06 12:38:48] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1778042328.059338 | source=vosk | frequency_hz=349.5 | rms=841 | updated_at=1778042147.368287
- [2026-05-06 12:38:48] operator / voice_transcript_partial / voice: tracking voice
  meta: kind=partial | timestamp=1778042328.3087525 | source=vosk | frequency_hz=349.5 | rms=841 | updated_at=1778042147.368287
- [2026-05-06 12:38:48] operator / voice_transcript_partial / voice: tracking paused
  meta: kind=partial | timestamp=1778042328.8080747 | source=vosk | frequency_hz=349.5 | rms=841 | updated_at=1778042147.368287
- [2026-05-06 12:38:49] operator / voice_transcript_partial / voice: tracking paused use large
  meta: kind=partial | timestamp=1778042329.3087366 | source=vosk | frequency_hz=349.5 | rms=841 | updated_at=1778042147.368287
- [2026-05-06 12:38:49] operator / voice_transcript_partial / voice: tracking paused use leon
  meta: kind=partial | timestamp=1778042329.5842724 | source=vosk | frequency_hz=349.5 | rms=841 | updated_at=1778042147.368287
- [2026-05-06 12:38:49] operator / voice_transcript_partial / voice: tracking paused use leon turn
  meta: kind=partial | timestamp=1778042329.8089411 | source=vosk | frequency_hz=349.5 | rms=841 | updated_at=1778042147.368287
- [2026-05-06 12:38:50] operator / voice_transcript_partial / voice: tracking paused use leon trigger turn
  meta: kind=partial | timestamp=1778042330.0697901 | source=vosk | frequency_hz=349.5 | rms=841 | updated_at=1778042147.368287
- [2026-05-06 12:38:51] operator / voice_transcript_partial / voice: tracking paused use leon trigger turn to guard
  meta: kind=partial | timestamp=1778042331.007114 | source=vosk | frequency_hz=349.5 | rms=841 | updated_at=1778042147.368287
- [2026-05-06 12:38:51] operator / voice_transcript_partial / voice: tracking paused use leon trigger turn to guard hey
  meta: kind=partial | timestamp=1778042331.0136223 | source=vosk | frequency_hz=349.5 | rms=841 | updated_at=1778042147.368287
- [2026-05-06 12:38:51] operator / voice_transcript_partial / voice: tracking paused use leon trigger turn to guard hold position
  meta: kind=partial | timestamp=1778042331.022644 | source=vosk | frequency_hz=349.5 | rms=841 | updated_at=1778042147.368287
- [2026-05-06 12:38:52] operator / voice_transcript_final / voice: elion tracking paused use trigger turn to guard hold position
  meta: kind=final | timestamp=1778042332.2813 | source=final | frequency_hz=349.5 | rms=841 | updated_at=1778042147.368287
- [2026-05-06 12:38:52] operator / voice_command / voice: elion tracking paused use trigger turn to guard hold position
  meta: normalized=True
- [2026-05-06 12:38:53] assistant / spoken_confirmation / voice: Understood. Holding position. Tell me when to resume guarding mode.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 12:38:57] operator / voice_transcript_partial / voice: hold position
  meta: kind=partial | timestamp=1778042337.643746 | source=vosk | frequency_hz=288.0 | rms=464 | updated_at=1778042336.887126
- [2026-05-06 12:38:58] operator / voice_transcript_final / voice: hold position
  meta: kind=final | timestamp=1778042338.9586039 | source=final | frequency_hz=288.0 | rms=464 | updated_at=1778042336.887126
- [2026-05-06 12:38:59] operator / voice_command / voice: hold position
  meta: normalized=True
- [2026-05-06 12:39:00] assistant / spoken_confirmation / voice: Understood. Holding position. Tell me when to resume guarding mode.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 12:39:06] operator / voice_transcript_partial / voice: hi set run the app make on the keyboard visual tell me why resume guarding mode
  meta: kind=partial | timestamp=1778042346.0581775 | source=vosk | frequency_hz=288.0 | rms=464 | updated_at=1778042336.887126
- [2026-05-06 12:39:07] operator / voice_transcript_final / voice: resume guarding mode
  meta: kind=final | timestamp=1778042347.1715508 | source=final | frequency_hz=288.0 | rms=464 | updated_at=1778042336.887126
- [2026-05-06 12:39:07] operator / voice_command / voice: resume guarding mode
  meta: normalized=True
- [2026-05-06 12:39:07] operator / voice_transcript_partial / voice: you
  meta: kind=partial | timestamp=1778042347.8162036 | source=vosk | frequency_hz=288.0 | rms=464 | updated_at=1778042336.887126
- [2026-05-06 12:39:08] operator / voice_transcript_partial / voice: e rest
  meta: kind=partial | timestamp=1778042348.0659592 | source=vosk | frequency_hz=288.0 | rms=464 | updated_at=1778042336.887126
- [2026-05-06 12:39:08] operator / voice_transcript_partial / voice: e rest to rest
  meta: kind=partial | timestamp=1778042348.3148203 | source=vosk | frequency_hz=288.0 | rms=464 | updated_at=1778042336.887126
- [2026-05-06 12:39:09] operator / voice_transcript_final / voice: e rest to rest
  meta: kind=final | timestamp=1778042349.1826546 | source=final | frequency_hz=288.0 | rms=464 | updated_at=1778042336.887126
- [2026-05-06 12:39:10] assistant / spoken_confirmation / voice: Resuming guarding mode now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 12:39:13] operator / voice_transcript_partial / voice: resume guarding mode no
  meta: kind=partial | timestamp=1778042353.121554 | source=vosk | frequency_hz=288.0 | rms=464 | updated_at=1778042336.887126
- [2026-05-06 12:39:13] operator / voice_transcript_final / voice: resume guarding mode
  meta: kind=final | timestamp=1778042353.6244833 | source=final | frequency_hz=288.0 | rms=464 | updated_at=1778042336.887126
- [2026-05-06 12:39:13] operator / voice_command / voice: resume guarding mode
  meta: normalized=True
- [2026-05-06 12:39:14] assistant / spoken_confirmation / voice: Resuming guarding mode now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 12:39:18] operator / voice_transcript_final / voice: resume guarding mode
  meta: kind=final | timestamp=1778042358.3569999 | source=final | frequency_hz=288.0 | rms=464 | updated_at=1778042336.887126
- [2026-05-06 12:39:18] operator / voice_command / voice: resume guarding mode
  meta: normalized=True
- [2026-05-06 12:39:19] operator / voice_transcript_partial / voice: deactivate
  meta: kind=partial | timestamp=1778042359.103422 | source=vosk | frequency_hz=276.0 | rms=682 | updated_at=1778042358.6004534
- [2026-05-06 12:39:19] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1778042359.6043243 | source=vosk | frequency_hz=276.0 | rms=682 | updated_at=1778042358.6004534
- [2026-05-06 12:39:19] operator / voice_transcript_partial / voice: connect boards
  meta: kind=partial | timestamp=1778042359.85422 | source=vosk | frequency_hz=276.0 | rms=682 | updated_at=1778042358.6004534
- [2026-05-06 12:39:20] operator / voice_transcript_final / voice: connect boards
  meta: kind=final | timestamp=1778042360.857212 | source=final | frequency_hz=276.0 | rms=682 | updated_at=1778042358.6004534
- [2026-05-06 12:39:21] operator / voice_command / voice: connect boards
  meta: normalized=True
- [2026-05-06 12:39:22] assistant / spoken_confirmation / voice: Connecting Smart Sentry boards now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 12:39:22] assistant / spoken_confirmation / voice: Resuming guarding mode now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 12:39:31] assistant / spoken_confirmation / voice: I am still guarding right now. Ask another question, give another command, or say pause guarding if you want me to hold position.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 12:39:40] operator / voice_transcript_partial / voice: export no tracking paused use leon turn guard hold position standby guard no
  meta: kind=partial | timestamp=1778042380.2027636 | source=vosk | frequency_hz=304.9 | rms=522 | updated_at=1778042373.69909
- [2026-05-06 12:39:40] operator / voice_transcript_partial / voice: export no tracking paused use leon turn guard hold position standby guard no active
  meta: kind=partial | timestamp=1778042380.464526 | source=vosk | frequency_hz=304.9 | rms=522 | updated_at=1778042373.69909
- [2026-05-06 12:39:40] operator / voice_transcript_partial / voice: export no tracking paused use leon turn guard hold position standby guard no active turn
  meta: kind=partial | timestamp=1778042380.7022066 | source=vosk | frequency_hz=304.9 | rms=522 | updated_at=1778042373.69909
- [2026-05-06 12:39:40] operator / voice_transcript_partial / voice: export no tracking paused use leon turn guard hold position standby guard no active targets running
  meta: kind=partial | timestamp=1778042380.9629118 | source=vosk | frequency_hz=304.9 | rms=522 | updated_at=1778042373.69909
- [2026-05-06 12:39:41] operator / voice_transcript_partial / voice: export no tracking paused use leon turn guard hold position standby guard no active targets running no
  meta: kind=partial | timestamp=1778042381.481846 | source=vosk | frequency_hz=304.9 | rms=522 | updated_at=1778042373.69909
- [2026-05-06 12:39:42] operator / voice_transcript_final / voice: elion export no tracking paused use turn guard hold position standby guard no active targets running
  meta: kind=final | timestamp=1778042382.786529 | source=final | frequency_hz=304.9 | rms=522 | updated_at=1778042373.69909
- [2026-05-06 12:39:43] operator / voice_command / voice: elion export no tracking paused use turn guard hold position standby guard no active targets running
  meta: normalized=True
- [2026-05-06 12:39:44] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 12:39:50] operator / voice_transcript_partial / voice: ai hey request zone activate assistant operator change smart sentry
  meta: kind=partial | timestamp=1778042390.795098 | source=vosk | frequency_hz=304.9 | rms=522 | updated_at=1778042373.69909
- [2026-05-06 12:39:51] operator / voice_transcript_partial / voice: ai hey request zone activate assistant operator change smart sentry setting
  meta: kind=partial | timestamp=1778042391.5456448 | source=vosk | frequency_hz=304.9 | rms=522 | updated_at=1778042373.69909
- [2026-05-06 12:39:51] operator / voice_transcript_partial / voice: ai hey request zone activate assistant operator change smart sentry setting drafts
  meta: kind=partial | timestamp=1778042391.793269 | source=vosk | frequency_hz=304.9 | rms=522 | updated_at=1778042373.69909
- [2026-05-06 12:39:52] operator / voice_transcript_final / voice: i hey request zone activate assistant operator change smart sentry setting
  meta: kind=final | timestamp=1778042392.5031493 | source=final | frequency_hz=304.9 | rms=522 | updated_at=1778042373.69909
- [2026-05-06 12:39:53] operator / voice_command / voice: i hey request zone activate assistant operator change smart sentry setting
  meta: normalized=True
- [2026-05-06 12:39:57] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 12:39:59] operator / voice_transcript_partial / voice: tracking no one
  meta: kind=partial | timestamp=1778042399.551338 | source=vosk | frequency_hz=304.9 | rms=522 | updated_at=1778042373.69909
- [2026-05-06 12:40:00] operator / voice_transcript_partial / voice: tracking no one targets enabled
  meta: kind=partial | timestamp=1778042400.0451403 | source=vosk | frequency_hz=304.9 | rms=522 | updated_at=1778042373.69909
- [2026-05-06 12:40:00] operator / voice_transcript_partial / voice: tracking no one targets
  meta: kind=partial | timestamp=1778042400.294194 | source=vosk | frequency_hz=304.9 | rms=522 | updated_at=1778042373.69909
- [2026-05-06 12:40:00] operator / voice_transcript_partial / voice: tracking no one targets in queue
  meta: kind=partial | timestamp=1778042400.5463698 | source=vosk | frequency_hz=304.9 | rms=522 | updated_at=1778042373.69909
- [2026-05-06 12:40:01] operator / voice_transcript_final / voice: tracking no one targets in queue
  meta: kind=final | timestamp=1778042401.1522825 | source=final | frequency_hz=304.9 | rms=522 | updated_at=1778042373.69909
- [2026-05-06 12:40:10] operator / voice_transcript_partial / voice: local that command changes
  meta: kind=partial | timestamp=1778042410.0143626 | source=vosk | frequency_hz=304.9 | rms=522 | updated_at=1778042373.69909
- [2026-05-06 12:40:10] operator / voice_transcript_partial / voice: local that command changes running
  meta: kind=partial | timestamp=1778042410.02188 | source=vosk | frequency_hz=304.9 | rms=522 | updated_at=1778042373.69909
- [2026-05-06 12:40:10] operator / voice_transcript_partial / voice: local that command changes is recognition
  meta: kind=partial | timestamp=1778042410.2732708 | source=vosk | frequency_hz=304.9 | rms=522 | updated_at=1778042373.69909
- [2026-05-06 12:40:11] operator / voice_transcript_final / voice: local that command changes is recognition
  meta: kind=final | timestamp=1778042411.2560248 | source=final | frequency_hz=304.9 | rms=522 | updated_at=1778042373.69909
- [2026-05-06 12:40:54] operator / voice_transcript_partial / voice: connect fire
  meta: kind=partial | timestamp=1778042454.2190816 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:40:54] operator / voice_transcript_final / voice: connect fire
  meta: kind=final | timestamp=1778042454.994823 | source=final | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:40:55] operator / voice_transcript_partial / voice: alerts
  meta: kind=partial | timestamp=1778042455.0046506 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:40:55] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778042455.2155752 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:40:56] operator / voice_transcript_final / voice: alert
  meta: kind=final | timestamp=1778042456.245938 | source=final | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:40:58] operator / voice_transcript_partial / voice: can output
  meta: kind=partial | timestamp=1778042458.464989 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:40:58] operator / voice_transcript_partial / voice: connect fire
  meta: kind=partial | timestamp=1778042458.7379484 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:40:58] operator / voice_transcript_partial / voice: connect fire safe zone
  meta: kind=partial | timestamp=1778042458.9681356 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:40:59] operator / voice_transcript_partial / voice: connect fire safe the is no detection
  meta: kind=partial | timestamp=1778042459.4704416 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:40:59] operator / voice_transcript_partial / voice: connect fire safe the is known
  meta: kind=partial | timestamp=1778042459.720767 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:40:59] operator / voice_transcript_partial / voice: connect fire safe zone
  meta: kind=partial | timestamp=1778042459.9633508 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:00] operator / voice_transcript_final / voice: connect fire safe is known zone
  meta: kind=final | timestamp=1778042460.5686424 | source=final | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:05] operator / voice_transcript_partial / voice: can auto fire safe the is no detection
  meta: kind=partial | timestamp=1778042465.9019222 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:05] operator / voice_transcript_partial / voice: can auto fire safe the is no tell me
  meta: kind=partial | timestamp=1778042465.9089413 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:06] operator / voice_transcript_partial / voice: can auto fire safe the is no target matching
  meta: kind=partial | timestamp=1778042466.1532502 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:07] operator / voice_transcript_final / voice: can alerts fire safe the is no sound
  meta: kind=final | timestamp=1778042467.1107185 | source=final | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:16] operator / voice_transcript_partial / voice: standby guard no active targets running
  meta: kind=partial | timestamp=1778042476.4023626 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:16] operator / voice_transcript_partial / voice: standby guard no active targets running app
  meta: kind=partial | timestamp=1778042476.903994 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:17] operator / voice_transcript_final / voice: standby guard no active targets running
  meta: kind=final | timestamp=1778042477.2954872 | source=final | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:19] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1778042479.420587 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:19] operator / voice_transcript_partial / voice: tracking of pir
  meta: kind=partial | timestamp=1778042479.6600199 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:19] operator / voice_transcript_partial / voice: tracking personality
  meta: kind=partial | timestamp=1778042479.904218 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:20] operator / voice_transcript_partial / voice: tracking personality confidence
  meta: kind=partial | timestamp=1778042480.9291945 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:21] operator / voice_transcript_partial / voice: tracking personality confidence alion
  meta: kind=partial | timestamp=1778042481.6530573 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:21] operator / voice_transcript_partial / voice: tracking personality confidence alion output
  meta: kind=partial | timestamp=1778042481.9030645 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:22] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 12:41:22] operator / voice_transcript_partial / voice: tracking personality confidence alion on pir sensors
  meta: kind=partial | timestamp=1778042482.1546664 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:22] operator / voice_transcript_partial / voice: tracking personality confidence alion ai assistant mode
  meta: kind=partial | timestamp=1778042482.6552472 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:22] operator / voice_transcript_partial / voice: tracking personality confidence alion ai assistant recognition
  meta: kind=partial | timestamp=1778042482.9100204 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:23] operator / voice_transcript_partial / voice: tracking personality confidence alion ai assistant make a lion
  meta: kind=partial | timestamp=1778042483.538788 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:23] operator / voice_transcript_partial / voice: tracking personality confidence alion ai assistant make a lion aim a joke
  meta: kind=partial | timestamp=1778042483.5490682 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:23] operator / voice_transcript_partial / voice: tracking personality confidence alion ai assistant make a lion aim gesture
  meta: kind=partial | timestamp=1778042483.7981434 | source=vosk | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:24] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 12:41:25] operator / voice_transcript_final / voice: elion tracking a personality confidence ai assistant make aim a gesture
  meta: kind=final | timestamp=1778042485.049479 | source=final | frequency_hz=238.0 | rms=489 | updated_at=1778042454.2110646
- [2026-05-06 12:41:25] operator / voice_command / voice: elion tracking a personality confidence ai assistant make aim a gesture
  meta: normalized=True
- [2026-05-06 12:41:27] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 12:41:34] operator / voice_transcript_partial / voice: ai hey the request the known e the rest can change the
  meta: kind=partial | timestamp=1778042494.1590374 | source=vosk | frequency_hz=297.6 | rms=399 | updated_at=1778042493.4266744
- [2026-05-06 12:41:34] operator / voice_transcript_partial / voice: ai hey the request the known e the rest can change theme to
  meta: kind=partial | timestamp=1778042494.1854014 | source=vosk | frequency_hz=297.6 | rms=399 | updated_at=1778042493.4266744
- [2026-05-06 12:41:34] operator / voice_transcript_partial / voice: ai hey the request the known e the rest can change theme to setting drafts
  meta: kind=partial | timestamp=1778042494.4339402 | source=vosk | frequency_hz=297.6 | rms=399 | updated_at=1778042493.4266744
- [2026-05-06 12:41:34] operator / voice_transcript_partial / voice: ai hey the request the known e the rest can change theme to setting is
  meta: kind=partial | timestamp=1778042494.6928415 | source=vosk | frequency_hz=297.6 | rms=399 | updated_at=1778042493.4266744
- [2026-05-06 12:41:35] operator / voice_transcript_final / voice: change theme
  meta: kind=final | timestamp=1778042495.5210204 | source=final | frequency_hz=297.6 | rms=399 | updated_at=1778042493.4266744
- [2026-05-06 12:41:36] operator / voice_command / voice: change theme
  meta: normalized=True
- [2026-05-06 12:41:37] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 12:41:46] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1778042506.8099828 | source=vosk | frequency_hz=398.0 | rms=529 | updated_at=1778042505.942684
- [2026-05-06 12:41:47] operator / voice_transcript_partial / voice: what's
  meta: kind=partial | timestamp=1778042507.0732906 | source=vosk | frequency_hz=398.0 | rms=529 | updated_at=1778042505.942684
- [2026-05-06 12:41:47] operator / voice_transcript_final / voice: what s
  meta: kind=final | timestamp=1778042507.8854718 | source=final | frequency_hz=398.0 | rms=529 | updated_at=1778042505.942684

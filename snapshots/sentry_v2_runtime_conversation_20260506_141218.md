# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-06 14:12:18
- Entries: 90
- Roles: {'assistant': 11, 'system': 1, 'operator': 78}
- Event types: {'assistant_prompt': 2, 'assistant_analysis': 1, 'voice_status': 1, 'spoken_confirmation': 8, 'voice_transcript_partial': 51, 'voice_transcript_final': 13, 'voice_command': 14}
- Channels: {'text': 3, 'voice': 87}
- Latest operator request: elion tracking voice use turn guard hold position
- Latest assistant message: Understood. Holding position. Tell me when to resume guarding mode.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.
- More normalized voice commands were dispatched than final transcript events were captured. Compare transcript text against command text to catch aggressive normalization or routing drift.

## Timeline

- [2026-05-06 14:09:58] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-06 14:09:58] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-06 14:09:59] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778047799.8448658 | source=vosk
- [2026-05-06 14:10:39] assistant / spoken_confirmation / voice: Good to go. Ask your question naturally, or say Elion first if you want a dedicated conversation window.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 14:10:47] operator / voice_transcript_partial / voice: go ask a question natural the voice alien face e
  meta: kind=partial | timestamp=1778047847.2492151 | source=vosk
- [2026-05-06 14:10:47] operator / voice_transcript_partial / voice: go ask a question natural the voice alien face e want to
  meta: kind=partial | timestamp=1778047847.258746 | source=vosk
- [2026-05-06 14:10:47] operator / voice_transcript_partial / voice: go ask a question natural the voice alien face e want the
  meta: kind=partial | timestamp=1778047847.4974732 | source=vosk
- [2026-05-06 14:10:48] operator / voice_transcript_final / voice: elion to go ask a question natural the voice face e want that
  meta: kind=final | timestamp=1778047848.6987612 | source=final | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:10:48] operator / voice_command / voice: elion to go ask a question natural the voice face e want that
  meta: normalized=True
- [2026-05-06 14:10:48] operator / voice_transcript_partial / voice: active
  meta: kind=partial | timestamp=1778047848.7510467 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:10:49] operator / voice_transcript_final / voice: active
  meta: kind=final | timestamp=1778047849.6064167 | source=final | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:10:54] operator / voice_transcript_partial / voice: standby guard no active targets recognition
  meta: kind=partial | timestamp=1778047854.003676 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:10:54] operator / voice_transcript_partial / voice: standby guard no active targets running no
  meta: kind=partial | timestamp=1778047854.2429125 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:10:55] operator / voice_transcript_final / voice: standby guard no active targets fire no
  meta: kind=final | timestamp=1778047855.1267152 | source=final | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:10:58] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1778047858.760284 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:10:58] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 14:10:59] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1778047859.8438246 | source=final | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:08] operator / voice_transcript_partial / voice: tracking voice use leon turn guard hold position standby guard no active targets
  meta: kind=partial | timestamp=1778047868.00463 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:08] operator / voice_transcript_partial / voice: tracking voice use leon turn guard hold position standby guard no active targets running
  meta: kind=partial | timestamp=1778047868.2548382 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:08] operator / voice_transcript_partial / voice: tracking voice use leon turn guard hold position standby guard no active targets for human
  meta: kind=partial | timestamp=1778047868.5126588 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:08] operator / voice_transcript_partial / voice: tracking voice use leon turn guard hold position standby guard no active targets running
  meta: kind=partial | timestamp=1778047868.7585368 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:09] operator / voice_transcript_final / voice: tracking voice use wait activate turn guard hold position standby guard no active targets running
  meta: kind=final | timestamp=1778047869.2038808 | source=final | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:09] operator / voice_command / voice: tracking voice use wait activate turn guard hold position standby guard no active targets running
  meta: normalized=True
- [2026-05-06 14:11:09] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1778047869.3826475 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:09] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 14:11:10] operator / voice_transcript_partial / voice: alion who are you
  meta: kind=partial | timestamp=1778047870.554446 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:11] operator / voice_transcript_final / voice: elion who are you
  meta: kind=final | timestamp=1778047871.415259 | source=final | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:11] operator / voice_command / voice: elion who are you
  meta: normalized=True
- [2026-05-06 14:11:11] assistant / assistant_prompt / text: I am Elion Mosk, or Elion for short, Smart Sentry's runtime AI assistant by GM Labs, a personal project by Gino. I provide live analysis, diagnostics, supported command handling, and supported runtime setting updates.
  meta: task_kind=prompt | speak_requested=True
- [2026-05-06 14:11:12] assistant / spoken_confirmation / voice: Understood. Holding position. Tell me when to resume guarding mode.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 14:11:15] operator / voice_transcript_partial / voice: tracking paused use leon turn guard hold position
  meta: kind=partial | timestamp=1778047875.5539417 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:15] operator / voice_transcript_partial / voice: tracking paused use leon turn guard hold position status
  meta: kind=partial | timestamp=1778047875.8036458 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:16] operator / voice_transcript_partial / voice: tracking paused use leon turn guard hold position standby
  meta: kind=partial | timestamp=1778047876.0534415 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:16] operator / voice_transcript_partial / voice: tracking paused use leon turn guard hold position standby guard
  meta: kind=partial | timestamp=1778047876.5549436 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:16] operator / voice_transcript_partial / voice: tracking paused use leon turn guard hold position standby guard no
  meta: kind=partial | timestamp=1778047876.8082428 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:17] operator / voice_transcript_partial / voice: tracking paused use leon turn guard hold position standby guard no active
  meta: kind=partial | timestamp=1778047877.0553184 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:17] operator / voice_transcript_partial / voice: tracking paused use leon turn guard hold position standby guard no active targets
  meta: kind=partial | timestamp=1778047877.5546093 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:17] operator / voice_transcript_partial / voice: tracking paused use leon turn guard hold position standby guard no active targets running
  meta: kind=partial | timestamp=1778047877.8036206 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:18] operator / voice_transcript_partial / voice: tracking paused use leon turn guard hold position standby guard no active targets on no
  meta: kind=partial | timestamp=1778047878.0551872 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:19] operator / voice_transcript_final / voice: tracking paused use wait activate turn guard hold position standby guard no active targets no
  meta: kind=final | timestamp=1778047879.197147 | source=final | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:19] operator / voice_command / voice: tracking paused use wait activate turn guard hold position standby guard no active targets no
  meta: normalized=True
- [2026-05-06 14:11:20] assistant / spoken_confirmation / voice: Understood. Holding position. Tell me when to resume guarding mode.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 14:11:25] operator / voice_transcript_partial / voice: on gesture hold tell me why resume guarding
  meta: kind=partial | timestamp=1778047885.1705503 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:25] operator / voice_transcript_partial / voice: on gesture hold tell me why resume guarding mode
  meta: kind=partial | timestamp=1778047885.2405863 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:26] operator / voice_transcript_partial / voice: on gesture hold tell me why resume guarding mode running
  meta: kind=partial | timestamp=1778047886.4898334 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:26] operator / voice_transcript_partial / voice: on gesture hold tell me why resume guarding mode run the
  meta: kind=partial | timestamp=1778047886.7410448 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:26] operator / voice_transcript_partial / voice: on gesture hold tell me why resume guarding mode run the smart
  meta: kind=partial | timestamp=1778047886.995737 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:27] operator / voice_transcript_partial / voice: on gesture hold tell me why resume guarding mode run the smart sentry
  meta: kind=partial | timestamp=1778047887.2425716 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:28] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1778047888.2454767 | source=final | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:28] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-05-06 14:11:29] assistant / spoken_confirmation / voice: Connecting Smart Sentry boards now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 14:11:32] operator / voice_transcript_partial / voice: setting guard no active
  meta: kind=partial | timestamp=1778047892.5140707 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:32] operator / voice_transcript_partial / voice: setting guard no active shortcuts
  meta: kind=partial | timestamp=1778047892.7539754 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:33] operator / voice_transcript_partial / voice: setting guard no active shortcuts for human
  meta: kind=partial | timestamp=1778047893.25115 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:33] operator / voice_transcript_partial / voice: setting guard no active shortcuts for human voice
  meta: kind=partial | timestamp=1778047893.5047214 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:34] operator / voice_transcript_final / voice: setting guard no active shortcuts for human
  meta: kind=final | timestamp=1778047894.3778942 | source=final | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:34] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778047894.5061147 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:34] operator / voice_transcript_partial / voice: the alion
  meta: kind=partial | timestamp=1778047894.7744539 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:35] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 14:11:35] operator / voice_transcript_partial / voice: the alion change your voice
  meta: kind=partial | timestamp=1778047895.2581406 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:44] operator / voice_transcript_partial / voice: tracking paused use leon turn guard hold position is alion guard no active targets for human
  meta: kind=partial | timestamp=1778047904.2261872 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:44] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 14:11:44] operator / voice_transcript_partial / voice: tracking paused use leon turn guard hold position is alion guard no active targets for human voice
  meta: kind=partial | timestamp=1778047904.4818242 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:46] operator / voice_transcript_final / voice: elion tracking paused use turn change guard hold position is guard no active targets for human
  meta: kind=final | timestamp=1778047906.151457 | source=final | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:46] operator / voice_command / voice: elion tracking paused use turn change guard hold position is guard no active targets for human
  meta: normalized=True
- [2026-05-06 14:11:47] assistant / spoken_confirmation / voice: Understood. Holding position. Tell me when to resume guarding mode.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 14:11:50] operator / voice_transcript_partial / voice: tracking voice use leon turn turn guard hey
  meta: kind=partial | timestamp=1778047910.6494138 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:50] operator / voice_transcript_partial / voice: tracking voice use leon turn turn guard home
  meta: kind=partial | timestamp=1778047910.9020886 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:51] operator / voice_transcript_partial / voice: tracking voice use leon turn turn guard hold position
  meta: kind=partial | timestamp=1778047911.149342 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:52] operator / voice_transcript_partial / voice: tracking voice use leon turn turn guard hold position who are you
  meta: kind=partial | timestamp=1778047912.148732 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:53] operator / voice_transcript_final / voice: tracking pause use make optimise turn guard hold position who are you
  meta: kind=final | timestamp=1778047913.0387053 | source=final | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:11:53] operator / voice_command / voice: tracking pause use make optimise turn guard hold position who are you
  meta: normalized=True
- [2026-05-06 14:11:54] assistant / spoken_confirmation / voice: Understood. Holding position. Tell me when to resume guarding mode.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 14:11:59] operator / voice_transcript_partial / voice: on the search hold position tell me why to resume guarding mode
  meta: kind=partial | timestamp=1778047919.1512914 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:12:00] operator / voice_transcript_final / voice: resume guarding mode
  meta: kind=final | timestamp=1778047920.159302 | source=final | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:12:00] operator / voice_command / voice: resume guarding mode
  meta: normalized=True
- [2026-05-06 14:12:01] assistant / spoken_confirmation / voice: Resuming guarding mode now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 14:12:04] operator / voice_transcript_partial / voice: standby guard no active
  meta: kind=partial | timestamp=1778047924.039339 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:12:04] operator / voice_transcript_partial / voice: standby guard no active target matching
  meta: kind=partial | timestamp=1778047924.3004622 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:12:05] operator / voice_transcript_partial / voice: standby guard no active target alion
  meta: kind=partial | timestamp=1778047925.0407436 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:12:05] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 14:12:05] operator / voice_transcript_partial / voice: standby guard no active target alion show
  meta: kind=partial | timestamp=1778047925.5401604 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:12:05] operator / voice_transcript_partial / voice: standby guard no active target alion show the
  meta: kind=partial | timestamp=1778047925.7971268 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:12:06] operator / voice_transcript_partial / voice: standby guard no active target alion tuning
  meta: kind=partial | timestamp=1778047926.1404169 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:12:10] operator / voice_transcript_partial / voice: tracking voice use leon turn guard hey
  meta: kind=partial | timestamp=1778047930.8476412 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:12:11] operator / voice_transcript_partial / voice: tracking voice use leon turn guard hold position
  meta: kind=partial | timestamp=1778047931.3556824 | source=vosk | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:12:12] operator / voice_transcript_final / voice: elion tracking voice use turn guard hold position
  meta: kind=final | timestamp=1778047932.7247996 | source=final | frequency_hz=302.0 | rms=492 | updated_at=1778047847.7378879
- [2026-05-06 14:12:13] operator / voice_command / voice: elion tracking voice use turn guard hold position
  meta: normalized=True
- [2026-05-06 14:12:14] assistant / spoken_confirmation / voice: Understood. Holding position. Tell me when to resume guarding mode.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-06 14:12:18] operator / voice_transcript_partial / voice: voice cleanup turn guard
  meta: kind=partial | timestamp=1778047938.3383968 | source=vosk | frequency_hz=149.6 | rms=495 | updated_at=1778047936.4325988

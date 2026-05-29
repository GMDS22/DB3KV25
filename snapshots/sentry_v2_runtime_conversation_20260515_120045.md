# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-15 12:00:45
- Entries: 131
- Roles: {'assistant': 6, 'system': 83, 'operator': 42}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 83, 'voice_transcript_partial': 29, 'voice_transcript_final': 9, 'voice_command': 4, 'spoken_confirmation': 4}
- Channels: {'text': 2, 'voice': 129}
- Latest operator request: changes
- Latest assistant message: I did not catch a supported command there. Please try again.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-15 11:47:23] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-15 11:47:23] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-15 11:47:26] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778816846.3827765 | source=vosk
- [2026-05-15 11:47:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816846.9130957 | source=vosk
- [2026-05-15 11:47:28] operator / voice_transcript_partial / voice: shortcuts
  meta: kind=partial | timestamp=1778816848.1749666 | source=vosk
- [2026-05-15 11:47:28] operator / voice_transcript_partial / voice: shortcuts control disabled
  meta: kind=partial | timestamp=1778816848.6714635 | source=vosk
- [2026-05-15 11:47:28] operator / voice_transcript_partial / voice: shortcuts control delete
  meta: kind=partial | timestamp=1778816848.9215791 | source=vosk
- [2026-05-15 11:47:29] operator / voice_transcript_partial / voice: shortcuts control the training
  meta: kind=partial | timestamp=1778816849.174059 | source=vosk
- [2026-05-15 11:47:29] operator / voice_transcript_partial / voice: shortcuts control trace
  meta: kind=partial | timestamp=1778816849.4206614 | source=vosk
- [2026-05-15 11:47:30] operator / voice_transcript_partial / voice: shortcuts control trace confirm
  meta: kind=partial | timestamp=1778816850.421537 | source=vosk
- [2026-05-15 11:47:30] operator / voice_transcript_partial / voice: shortcuts control trace confirm cleanup off
  meta: kind=partial | timestamp=1778816850.6820726 | source=vosk
- [2026-05-15 11:47:30] operator / voice_transcript_partial / voice: shortcuts control trace confirm cleanup refinement
  meta: kind=partial | timestamp=1778816850.9208739 | source=vosk
- [2026-05-15 11:47:31] operator / voice_transcript_partial / voice: shortcuts control trace confirm cleanup refinement want
  meta: kind=partial | timestamp=1778816851.6713111 | source=vosk
- [2026-05-15 11:47:31] operator / voice_transcript_partial / voice: shortcuts control trace confirm cleanup refinement logger
  meta: kind=partial | timestamp=1778816851.9203215 | source=vosk
- [2026-05-15 11:47:32] operator / voice_transcript_partial / voice: shortcuts control trace confirm cleanup refinement want servo
  meta: kind=partial | timestamp=1778816852.173141 | source=vosk
- [2026-05-15 11:47:33] operator / voice_transcript_final / voice: shortcuts control delete trace confirm cleanup refinement logger search
  meta: kind=final | timestamp=1778816853.214772 | source=final
- [2026-05-15 11:47:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816853.3324904 | source=vosk
- [2026-05-15 11:47:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816859.6650963 | source=vosk
- [2026-05-15 11:48:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816895.667566 | source=vosk
- [2026-05-15 11:48:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816896.1665437 | source=vosk
- [2026-05-15 11:48:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816910.6674626 | source=vosk
- [2026-05-15 11:48:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816911.1683922 | source=vosk
- [2026-05-15 11:48:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816912.167905 | source=vosk
- [2026-05-15 11:48:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816912.667663 | source=vosk
- [2026-05-15 11:48:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816913.1670375 | source=vosk
- [2026-05-15 11:48:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816913.6715524 | source=vosk
- [2026-05-15 11:48:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816914.6671257 | source=vosk
- [2026-05-15 11:48:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816915.1679378 | source=vosk
- [2026-05-15 11:48:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816916.1707323 | source=vosk
- [2026-05-15 11:48:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816916.6678398 | source=vosk
- [2026-05-15 11:48:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816922.1756535 | source=vosk
- [2026-05-15 11:48:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816922.9214494 | source=vosk
- [2026-05-15 11:48:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816924.6707041 | source=vosk
- [2026-05-15 11:48:44] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1778816924.6777039 | source=vosk
- [2026-05-15 11:48:45] operator / voice_transcript_partial / voice: alion run display
  meta: kind=partial | timestamp=1778816925.176454 | source=vosk
- [2026-05-15 11:48:46] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1778816926.3403769 | source=partial-timeout
- [2026-05-15 11:48:46] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-15 11:48:46] assistant / spoken_confirmation / voice: Hello. What would you like to talk about?
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-15 11:48:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816926.841581 | source=vosk
- [2026-05-15 11:48:47] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778816927.3475602 | source=vosk
- [2026-05-15 11:48:48] system / voice_status / voice: processing
  meta: kind=status | timestamp=1778816928.0911853 | source=state
- [2026-05-15 11:48:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816928.09269 | source=state
- [2026-05-15 11:48:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816928.8518243 | source=vosk
- [2026-05-15 11:48:49] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778816929.5340922 | source=state
- [2026-05-15 11:48:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816929.601988 | source=vosk
- [2026-05-15 11:48:50] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778816930.353876 | source=vosk
- [2026-05-15 11:48:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816933.1040695 | source=vosk
- [2026-05-15 11:48:53] operator / voice_transcript_partial / voice: alion run smart elian what you light
  meta: kind=partial | timestamp=1778816933.2152863 | source=vosk
- [2026-05-15 11:48:53] operator / voice_transcript_partial / voice: alion run smart elian what you light turn
  meta: kind=partial | timestamp=1778816933.360179 | source=vosk
- [2026-05-15 11:48:53] operator / voice_transcript_partial / voice: alion run smart elian what you light turn the smart sentry
  meta: kind=partial | timestamp=1778816933.6155934 | source=vosk
- [2026-05-15 11:48:54] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1778816934.424356 | source=final
- [2026-05-15 11:48:54] system / voice_status / voice: processing
  meta: kind=status | timestamp=1778816934.4692695 | source=state
- [2026-05-15 11:48:54] system / voice_status / voice: heard
  meta: kind=status | timestamp=1778816934.4692695 | source=state
- [2026-05-15 11:48:54] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-05-15 11:48:54] assistant / spoken_confirmation / voice: Connecting Smart Sentry boards now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-15 11:48:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816934.8881123 | source=vosk
- [2026-05-15 11:48:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816935.735713 | source=vosk
- [2026-05-15 11:48:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816936.2416499 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:48:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816936.9995484 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:48:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816936.9995484 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:48:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816937.511717 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:48:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816937.7605553 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:48:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816938.2635534 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816946.7596624 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:06] operator / voice_transcript_partial / voice: alion run smart elian what you light turn the smart sentry setting smart sentry
  meta: kind=partial | timestamp=1778816946.7731955 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:07] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1778816947.2719245 | source=final | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:07] system / voice_status / voice: processing
  meta: kind=status | timestamp=1778816947.3119996 | source=state | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:07] system / voice_status / voice: heard
  meta: kind=status | timestamp=1778816947.3140001 | source=state | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:07] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-05-15 11:49:07] assistant / spoken_confirmation / voice: Smart Sentry is already connected and enabled.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-15 11:49:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816947.760739 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816948.760919 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816949.2609143 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816951.0327477 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816951.5332832 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816952.2570245 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816952.759199 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816953.4547493 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816953.9564312 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816954.458175 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816954.9566667 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816956.206266 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816956.4565566 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:16] operator / voice_transcript_partial / voice: want active
  meta: kind=partial | timestamp=1778816956.4645631 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:16] operator / voice_transcript_partial / voice: want active guard zone
  meta: kind=partial | timestamp=1778816956.962997 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:17] operator / voice_transcript_partial / voice: want active guard system
  meta: kind=partial | timestamp=1778816957.2142253 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816957.72781 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816962.20615 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:22] operator / voice_transcript_partial / voice: want active guard system search
  meta: kind=partial | timestamp=1778816962.462808 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:22] operator / voice_transcript_partial / voice: want active guard system threat change your voice
  meta: kind=partial | timestamp=1778816962.7141173 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:23] operator / voice_transcript_partial / voice: want active guard system threat change your voice disabled
  meta: kind=partial | timestamp=1778816963.4634187 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816963.9570465 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816964.717278 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:24] operator / voice_transcript_partial / voice: want active guard system threat change your voice tuning
  meta: kind=partial | timestamp=1778816964.726791 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:24] operator / voice_transcript_partial / voice: want active guard system threat change your voice style neutral
  meta: kind=partial | timestamp=1778816964.9737697 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:25] operator / voice_transcript_final / voice: voice style alert
  meta: kind=final | timestamp=1778816965.622259 | source=final | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:25] system / voice_status / voice: processing
  meta: kind=status | timestamp=1778816965.6639004 | source=state | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:25] system / voice_status / voice: heard
  meta: kind=status | timestamp=1778816965.6649017 | source=state | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:25] operator / voice_command / voice: voice style alert
  meta: normalized=True
- [2026-05-15 11:49:25] assistant / spoken_confirmation / voice: I did not catch a supported command there. Please try again.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-15 11:49:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816965.9689984 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816967.4670281 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816967.7164078 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816968.471319 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816969.966981 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816970.4669561 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816970.9675517 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:30] operator / voice_transcript_partial / voice: want camera is tracking
  meta: kind=partial | timestamp=1778816970.9795825 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816971.7196283 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:32] operator / voice_transcript_final / voice: want camera is tracking
  meta: kind=final | timestamp=1778816972.02592 | source=final | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816972.1359417 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:32] operator / voice_transcript_partial / voice: want camera is tracking changes
  meta: kind=partial | timestamp=1778816972.1414628 | source=vosk | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:32] operator / voice_transcript_final / voice: want camera is tracking changes
  meta: kind=final | timestamp=1778816972.8245082 | source=final | frequency_hz=110.0 | rms=1262 | updated_at=1778816936.2416499
- [2026-05-15 11:49:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816973.5077019 | source=vosk | frequency_hz=240.0 | rms=1471 | updated_at=1778816973.5077019
- [2026-05-15 11:49:33] operator / voice_transcript_partial / voice: want camera is tracking status
  meta: kind=partial | timestamp=1778816973.5143604 | source=vosk | frequency_hz=240.0 | rms=1471 | updated_at=1778816973.5077019
- [2026-05-15 11:49:34] operator / voice_transcript_final / voice: want camera is tracking status
  meta: kind=final | timestamp=1778816974.3471498 | source=final | frequency_hz=240.0 | rms=1471 | updated_at=1778816973.5077019
- [2026-05-15 11:49:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816974.5150712 | source=vosk | frequency_hz=240.0 | rms=1471 | updated_at=1778816973.5077019
- [2026-05-15 11:49:35] system / voice_status / voice: heard
  meta: kind=status | timestamp=1778816975.0075588 | source=vosk | frequency_hz=240.0 | rms=1471 | updated_at=1778816973.5077019
- [2026-05-15 11:49:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816975.506992 | source=vosk | frequency_hz=240.0 | rms=1471 | updated_at=1778816973.5077019
- [2026-05-15 11:49:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816979.2578099 | source=vosk | frequency_hz=240.0 | rms=1471 | updated_at=1778816973.5077019
- [2026-05-15 11:49:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816979.50827 | source=vosk | frequency_hz=240.0 | rms=1471 | updated_at=1778816973.5077019
- [2026-05-15 11:49:40] operator / voice_transcript_partial / voice: changes
  meta: kind=partial | timestamp=1778816980.263521 | source=vosk | frequency_hz=240.0 | rms=1471 | updated_at=1778816973.5077019
- [2026-05-15 11:49:42] operator / voice_transcript_final / voice: changes
  meta: kind=final | timestamp=1778816982.3293355 | source=final | frequency_hz=240.0 | rms=1471 | updated_at=1778816973.5077019
- [2026-05-15 11:49:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816982.3713524 | source=vosk | frequency_hz=240.0 | rms=1471 | updated_at=1778816973.5077019
- [2026-05-15 11:49:42] system / voice_status / voice: heard
  meta: kind=status | timestamp=1778816982.8723774 | source=vosk | frequency_hz=240.0 | rms=1471 | updated_at=1778816973.5077019
- [2026-05-15 11:49:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816984.122322 | source=vosk | frequency_hz=240.0 | rms=1471 | updated_at=1778816973.5077019
- [2026-05-15 11:49:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816984.8727546 | source=vosk | frequency_hz=240.0 | rms=1471 | updated_at=1778816973.5077019
- [2026-05-15 11:49:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816986.1245835 | source=vosk | frequency_hz=240.0 | rms=1471 | updated_at=1778816973.5077019
- [2026-05-15 11:49:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816988.1224482 | source=vosk | frequency_hz=240.0 | rms=1471 | updated_at=1778816973.5077019
- [2026-05-15 11:49:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778816988.876994 | source=vosk | frequency_hz=240.0 | rms=1471 | updated_at=1778816973.5077019
- [2026-05-15 11:49:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778816990.3735192 | source=vosk | frequency_hz=240.0 | rms=1471 | updated_at=1778816973.5077019

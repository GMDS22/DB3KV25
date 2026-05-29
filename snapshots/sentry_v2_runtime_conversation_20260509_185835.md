# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-09 18:58:35
- Entries: 27
- Roles: {'assistant': 2, 'system': 1, 'operator': 24}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 1, 'voice_transcript_partial': 20, 'voice_transcript_final': 4}
- Channels: {'text': 2, 'voice': 25}
- Latest operator request: camera guard
- Latest assistant message: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.
- Assistant text replies were generated without matching spoken assistant lines. Inspect human voice availability or auto-speak configuration.

## Timeline

- [2026-05-09 18:22:04] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-09 18:22:04] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-09 18:22:05] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778322125.5977955 | source=vosk
- [2026-05-09 18:22:06] operator / voice_transcript_partial / voice: shortcuts
  meta: kind=partial | timestamp=1778322126.7130008 | source=vosk | frequency_hz=136.4 | rms=325 | updated_at=1778322126.6962771
- [2026-05-09 18:22:06] operator / voice_transcript_partial / voice: show
  meta: kind=partial | timestamp=1778322126.9492626 | source=vosk | frequency_hz=137.0 | rms=1002 | updated_at=1778322126.940252
- [2026-05-09 18:22:07] operator / voice_transcript_partial / voice: show shortcuts
  meta: kind=partial | timestamp=1778322127.6964533 | source=vosk | frequency_hz=137.0 | rms=1002 | updated_at=1778322126.940252
- [2026-05-09 18:22:07] operator / voice_transcript_partial / voice: show show
  meta: kind=partial | timestamp=1778322127.9623787 | source=vosk | frequency_hz=137.0 | rms=1002 | updated_at=1778322126.940252
- [2026-05-09 18:22:08] operator / voice_transcript_partial / voice: show show show
  meta: kind=partial | timestamp=1778322128.9464784 | source=vosk | frequency_hz=137.0 | rms=1002 | updated_at=1778322126.940252
- [2026-05-09 18:22:09] operator / voice_transcript_partial / voice: show show show mode
  meta: kind=partial | timestamp=1778322129.1971207 | source=vosk | frequency_hz=137.0 | rms=1002 | updated_at=1778322126.940252
- [2026-05-09 18:22:10] operator / voice_transcript_final / voice: show show on show mode
  meta: kind=final | timestamp=1778322130.0741036 | source=final | frequency_hz=137.0 | rms=1002 | updated_at=1778322126.940252
- [2026-05-09 18:22:11] operator / voice_transcript_partial / voice: on
  meta: kind=partial | timestamp=1778322131.126952 | source=vosk | frequency_hz=137.0 | rms=1002 | updated_at=1778322126.940252
- [2026-05-09 18:22:11] operator / voice_transcript_partial / voice: on show
  meta: kind=partial | timestamp=1778322131.1359704 | source=vosk | frequency_hz=137.0 | rms=1002 | updated_at=1778322126.940252
- [2026-05-09 18:22:11] operator / voice_transcript_partial / voice: on show on
  meta: kind=partial | timestamp=1778322131.949222 | source=vosk | frequency_hz=137.0 | rms=1002 | updated_at=1778322126.940252
- [2026-05-09 18:22:12] operator / voice_transcript_partial / voice: on show of window shortcuts
  meta: kind=partial | timestamp=1778322132.1971712 | source=vosk | frequency_hz=137.0 | rms=1002 | updated_at=1778322126.940252
- [2026-05-09 18:22:12] operator / voice_transcript_partial / voice: on show of window abort
  meta: kind=partial | timestamp=1778322132.4497252 | source=vosk | frequency_hz=137.0 | rms=1002 | updated_at=1778322126.940252
- [2026-05-09 18:22:12] operator / voice_transcript_partial / voice: on show of window abort current
  meta: kind=partial | timestamp=1778322132.696425 | source=vosk | frequency_hz=360.0 | rms=283 | updated_at=1778322132.6903768
- [2026-05-09 18:22:12] operator / voice_transcript_partial / voice: on show of window enable
  meta: kind=partial | timestamp=1778322132.9496925 | source=vosk | frequency_hz=341.8 | rms=292 | updated_at=1778322132.940163
- [2026-05-09 18:22:13] operator / voice_transcript_final / voice: on show of window abort
  meta: kind=final | timestamp=1778322133.8014991 | source=final | frequency_hz=311.1 | rms=280 | updated_at=1778322133.1902983
- [2026-05-09 18:22:13] operator / voice_transcript_partial / voice: on
  meta: kind=partial | timestamp=1778322133.9485366 | source=vosk | frequency_hz=311.1 | rms=280 | updated_at=1778322133.1902983
- [2026-05-09 18:22:14] operator / voice_transcript_partial / voice: on the status
  meta: kind=partial | timestamp=1778322134.199257 | source=vosk | frequency_hz=311.1 | rms=280 | updated_at=1778322133.1902983
- [2026-05-09 18:22:14] operator / voice_transcript_partial / voice: local actions
  meta: kind=partial | timestamp=1778322134.4503427 | source=vosk | frequency_hz=314.2 | rms=285 | updated_at=1778322134.4402134
- [2026-05-09 18:22:15] operator / voice_transcript_final / voice: local
  meta: kind=final | timestamp=1778322135.5300825 | source=final | frequency_hz=314.2 | rms=285 | updated_at=1778322134.4402134
- [2026-05-09 18:27:05] operator / voice_transcript_partial / voice: ml
  meta: kind=partial | timestamp=1778322425.0640647 | source=vosk | frequency_hz=296.0 | rms=281 | updated_at=1778322136.9406674
- [2026-05-09 18:27:05] operator / voice_transcript_partial / voice: camera
  meta: kind=partial | timestamp=1778322425.315087 | source=vosk | frequency_hz=296.0 | rms=281 | updated_at=1778322136.9406674
- [2026-05-09 18:27:07] operator / voice_transcript_partial / voice: camera pir guard
  meta: kind=partial | timestamp=1778322427.5703619 | source=vosk | frequency_hz=296.0 | rms=281 | updated_at=1778322136.9406674
- [2026-05-09 18:27:08] operator / voice_transcript_partial / voice: camera logger go
  meta: kind=partial | timestamp=1778322428.0624971 | source=vosk | frequency_hz=296.0 | rms=281 | updated_at=1778322136.9406674
- [2026-05-09 18:27:35] operator / voice_transcript_final / voice: camera guard
  meta: kind=final | timestamp=1778322455.912251 | source=final | frequency_hz=296.0 | rms=281 | updated_at=1778322136.9406674

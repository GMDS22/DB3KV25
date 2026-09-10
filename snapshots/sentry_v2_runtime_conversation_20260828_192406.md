# SMART SENTRY V5.0.0 Runtime Conversation Export

- Generated: 2026-08-28 19:24:06
- Entries: 2571
- Roles: {'assistant': 4, 'system': 1974, 'operator': 593}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 1974, 'voice_transcript_partial': 487, 'voice_transcript_final': 105, 'spoken_confirmation': 2, 'voice_command': 1}
- Channels: {'text': 2, 'voice': 2569}
- Latest operator request: to school
- Latest assistant message: Running Smart Sentry now. Connecting the Smart Sentry boards first.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-08-28 18:33:47] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-08-28 18:33:47] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-08-28 18:33:50] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787913230.388287 | source=vosk
- [2026-08-28 18:33:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913231.1463752 | source=vosk | rms=724 | updated_at=1787913231.1463752
- [2026-08-28 18:33:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913231.8966544 | source=vosk | rms=724 | updated_at=1787913231.1463752
- [2026-08-28 18:33:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913232.6463158 | source=vosk | rms=879 | updated_at=1787913232.6463158
- [2026-08-28 18:33:53] operator / voice_transcript_partial / voice: academic
  meta: kind=partial | timestamp=1787913233.676345 | source=vosk | rms=1200 | updated_at=1787913233.6463668
- [2026-08-28 18:33:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913233.897782 | source=vosk | rms=1204 | updated_at=1787913233.897782
- [2026-08-28 18:33:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913234.3963237 | source=vosk | rms=480 | updated_at=1787913234.3963237 | frequency_hz=300.0
- [2026-08-28 18:33:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913234.6461837 | source=vosk | rms=479 | updated_at=1787913234.6461837 | frequency_hz=244.0
- [2026-08-28 18:33:54] operator / voice_transcript_partial / voice: academic sama
  meta: kind=partial | timestamp=1787913234.6602046 | source=vosk | rms=479 | updated_at=1787913234.6461837 | frequency_hz=244.0
- [2026-08-28 18:33:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913234.8963091 | source=vosk | rms=479 | updated_at=1787913234.6461837 | frequency_hz=244.0
- [2026-08-28 18:33:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913235.146246 | source=vosk | rms=1200 | updated_at=1787913235.146246 | frequency_hz=297.2
- [2026-08-28 18:33:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913235.397145 | source=vosk | rms=1200 | updated_at=1787913235.3966243 | frequency_hz=297.2
- [2026-08-28 18:33:55] operator / voice_transcript_final / voice: academic sama
  meta: kind=final | timestamp=1787913235.707011 | source=final | rms=1200 | updated_at=1787913235.3966243 | frequency_hz=297.2
- [2026-08-28 18:33:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913235.806254 | source=vosk | rms=872 | updated_at=1787913235.806254 | frequency_hz=297.2
- [2026-08-28 18:33:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913238.8965087 | source=vosk | rms=122 | updated_at=1787913238.1461601 | frequency_hz=274.8
- [2026-08-28 18:33:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913239.146278 | source=vosk | rms=198 | updated_at=1787913239.146278 | frequency_hz=274.8
- [2026-08-28 18:34:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913240.146183 | source=vosk | rms=136 | updated_at=1787913239.3962026 | frequency_hz=242.3
- [2026-08-28 18:34:27] assistant / spoken_confirmation / voice: Smart Sentry is ready.
  meta: interrupt=True | assistant_output=False | spoken=True
- [2026-08-28 18:34:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913245.946655 | source=vosk | rms=1201 | updated_at=1787913245.946655 | frequency_hz=242.3
- [2026-08-28 18:34:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913246.447813 | source=vosk | rms=1201 | updated_at=1787913245.946655 | frequency_hz=242.3
- [2026-08-28 18:34:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913246.6967049 | source=vosk | rms=1043 | updated_at=1787913246.6967049 | frequency_hz=242.3
- [2026-08-28 18:34:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913254.0875716 | source=vosk | rms=416 | updated_at=1787913253.5869627 | frequency_hz=261.7
- [2026-08-28 18:34:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913255.33695 | source=vosk | rms=351 | updated_at=1787913255.33695 | frequency_hz=261.7
- [2026-08-28 18:34:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913258.0873852 | source=vosk | rms=458 | updated_at=1787913257.5874104 | frequency_hz=261.7
- [2026-08-28 18:34:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913259.337446 | source=vosk | rms=423 | updated_at=1787913259.337446 | frequency_hz=261.7
- [2026-08-28 18:34:20] operator / voice_transcript_partial / voice: hundred
  meta: kind=partial | timestamp=1787913260.1818972 | source=vosk | rms=442 | updated_at=1787913260.0881145 | frequency_hz=261.7
- [2026-08-28 18:34:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913260.3370981 | source=vosk | rms=478 | updated_at=1787913260.3370981 | frequency_hz=261.7
- [2026-08-28 18:34:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913260.5870228 | source=vosk | rms=478 | updated_at=1787913260.3370981 | frequency_hz=261.7
- [2026-08-28 18:34:20] operator / voice_transcript_partial / voice: that's
  meta: kind=partial | timestamp=1787913260.6733432 | source=vosk | rms=478 | updated_at=1787913260.3370981 | frequency_hz=261.7
- [2026-08-28 18:34:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913260.8373628 | source=vosk | rms=478 | updated_at=1787913260.3370981 | frequency_hz=261.7
- [2026-08-28 18:34:20] operator / voice_transcript_partial / voice: that's popular
  meta: kind=partial | timestamp=1787913260.9192302 | source=vosk | rms=478 | updated_at=1787913260.3370981 | frequency_hz=261.7
- [2026-08-28 18:34:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913261.5866683 | source=vosk | rms=803 | updated_at=1787913261.5866683 | frequency_hz=261.7
- [2026-08-28 18:34:21] operator / voice_transcript_partial / voice: you know at that spot
  meta: kind=partial | timestamp=1787913261.6587484 | source=vosk | rms=803 | updated_at=1787913261.5866683 | frequency_hz=261.7
- [2026-08-28 18:34:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913262.0866177 | source=vosk | rms=803 | updated_at=1787913261.5866683 | frequency_hz=261.7
- [2026-08-28 18:34:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913262.586815 | source=vosk | rms=566 | updated_at=1787913262.586815 | frequency_hz=261.7
- [2026-08-28 18:34:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913263.08779 | source=vosk | rms=566 | updated_at=1787913262.586815 | frequency_hz=261.7
- [2026-08-28 18:34:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913264.0871704 | source=vosk | rms=566 | updated_at=1787913262.586815 | frequency_hz=261.7
- [2026-08-28 18:34:24] operator / voice_transcript_final / voice: know at that spot
  meta: kind=final | timestamp=1787913264.3776639 | source=final | rms=566 | updated_at=1787913262.586815 | frequency_hz=261.7
- [2026-08-28 18:34:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913264.588333 | source=vosk | rms=566 | updated_at=1787913262.586815 | frequency_hz=261.7
- [2026-08-28 18:34:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913266.078105 | source=vosk | rms=566 | updated_at=1787913262.586815 | frequency_hz=261.7
- [2026-08-28 18:34:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913266.5772877 | source=vosk | rms=566 | updated_at=1787913262.586815 | frequency_hz=261.7
- [2026-08-28 18:34:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913266.826856 | source=vosk | rms=590 | updated_at=1787913266.826856 | frequency_hz=261.7
- [2026-08-28 18:34:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913267.5770626 | source=vosk | rms=409 | updated_at=1787913267.0772154 | frequency_hz=261.7
- [2026-08-28 18:34:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913269.838346 | source=vosk | rms=409 | updated_at=1787913267.0772154 | frequency_hz=261.7
- [2026-08-28 18:34:34] operator / voice_transcript_partial / voice: union
  meta: kind=partial | timestamp=1787913274.1608949 | source=vosk | rms=2963 | updated_at=1787913274.0871723 | frequency_hz=319.6
- [2026-08-28 18:34:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913274.337413 | source=vosk | rms=7391 | updated_at=1787913274.337413 | frequency_hz=319.6
- [2026-08-28 18:34:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913274.587739 | source=vosk | rms=4784 | updated_at=1787913274.587739 | frequency_hz=319.6
- [2026-08-28 18:34:34] operator / voice_transcript_partial / voice: can you run the
  meta: kind=partial | timestamp=1787913274.6342895 | source=vosk | rms=4784 | updated_at=1787913274.587739 | frequency_hz=319.6
- [2026-08-28 18:34:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913274.838776 | source=vosk | rms=3433 | updated_at=1787913274.838776 | frequency_hz=319.6
- [2026-08-28 18:34:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913275.0878372 | source=vosk | rms=4935 | updated_at=1787913275.0878372 | frequency_hz=319.6
- [2026-08-28 18:34:35] operator / voice_transcript_partial / voice: can you run the smart
  meta: kind=partial | timestamp=1787913275.1063619 | source=vosk | rms=4935 | updated_at=1787913275.0878372 | frequency_hz=319.6
- [2026-08-28 18:34:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913275.353045 | source=vosk | rms=1572 | updated_at=1787913275.3520436 | frequency_hz=314.8
- [2026-08-28 18:34:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913275.5871642 | source=vosk | rms=1201 | updated_at=1787913275.5871642 | frequency_hz=261.3
- [2026-08-28 18:34:35] operator / voice_transcript_partial / voice: can you run the smart sentry
  meta: kind=partial | timestamp=1787913275.6187396 | source=vosk | rms=1201 | updated_at=1787913275.5871642 | frequency_hz=261.3
- [2026-08-28 18:34:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913275.858506 | source=vosk | rms=1200 | updated_at=1787913275.858506 | frequency_hz=261.3
- [2026-08-28 18:34:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913276.086911 | source=vosk | rms=1200 | updated_at=1787913276.086911 | frequency_hz=261.3
- [2026-08-28 18:34:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913276.3464663 | source=vosk | rms=1202 | updated_at=1787913276.3464663 | frequency_hz=290.2
- [2026-08-28 18:34:36] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1787913276.3648307 | source=final | rms=1202 | updated_at=1787913276.3464663 | frequency_hz=290.2
- [2026-08-28 18:34:36] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787913276.393847 | source=state | rms=1202 | updated_at=1787913276.3464663 | frequency_hz=290.2
- [2026-08-28 18:34:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913276.393847 | source=state | rms=1202 | updated_at=1787913276.3464663 | frequency_hz=290.2
- [2026-08-28 18:34:36] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-08-28 18:34:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913276.5903318 | source=vosk | rms=397 | updated_at=1787913276.5903318 | frequency_hz=215.2
- [2026-08-28 18:34:36] assistant / spoken_confirmation / voice: Running Smart Sentry now. Connecting the Smart Sentry boards first.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-08-28 18:34:41] operator / voice_transcript_partial / voice: she
  meta: kind=partial | timestamp=1787913281.909783 | source=vosk | rms=1201 | updated_at=1787913281.89121 | frequency_hz=222.6
- [2026-08-28 18:34:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913282.088666 | source=vosk | rms=730 | updated_at=1787913282.088666 | frequency_hz=222.6
- [2026-08-28 18:34:42] operator / voice_transcript_partial / voice: she is
  meta: kind=partial | timestamp=1787913282.1377552 | source=vosk | rms=730 | updated_at=1787913282.088666 | frequency_hz=222.6
- [2026-08-28 18:34:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913282.4086568 | source=vosk | rms=1205 | updated_at=1787913282.4086568 | frequency_hz=260.9
- [2026-08-28 18:34:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913282.6134245 | source=vosk | rms=1205 | updated_at=1787913282.4086568 | frequency_hz=260.9
- [2026-08-28 18:34:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913282.8373802 | source=vosk | rms=1205 | updated_at=1787913282.8373802 | frequency_hz=260.9
- [2026-08-28 18:34:43] operator / voice_transcript_final / voice: she is
  meta: kind=final | timestamp=1787913283.122603 | source=final | rms=1205 | updated_at=1787913282.8373802 | frequency_hz=260.9
- [2026-08-28 18:34:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913283.1717935 | source=vosk | rms=1201 | updated_at=1787913283.1717935 | frequency_hz=260.9
- [2026-08-28 18:34:45] operator / voice_transcript_partial / voice: central
  meta: kind=partial | timestamp=1787913285.6555154 | source=vosk | rms=1203 | updated_at=1787913285.5886905 | frequency_hz=215.7
- [2026-08-28 18:34:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913285.8380997 | source=vosk | rms=1202 | updated_at=1787913285.8380997 | frequency_hz=215.7
- [2026-08-28 18:34:45] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1787913285.9072614 | source=vosk | rms=1202 | updated_at=1787913285.8380997 | frequency_hz=215.7
- [2026-08-28 18:34:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913286.0874512 | source=vosk | rms=1201 | updated_at=1787913286.0874512 | frequency_hz=283.0
- [2026-08-28 18:34:46] operator / voice_transcript_final / voice: century
  meta: kind=final | timestamp=1787913286.330167 | source=final | rms=1201 | updated_at=1787913286.0874512 | frequency_hz=283.0
- [2026-08-28 18:34:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913286.3697846 | source=vosk | rms=1205 | updated_at=1787913286.3697846 | frequency_hz=283.0
- [2026-08-28 18:34:48] operator / voice_transcript_partial / voice: i think
  meta: kind=partial | timestamp=1787913288.6290934 | source=vosk | rms=1306 | updated_at=1787913288.5875947 | frequency_hz=297.8
- [2026-08-28 18:34:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913288.8401098 | source=vosk | rms=1205 | updated_at=1787913288.8401098 | frequency_hz=297.8
- [2026-08-28 18:34:49] operator / voice_transcript_partial / voice: i think that's really
  meta: kind=partial | timestamp=1787913289.1299765 | source=vosk | rms=1205 | updated_at=1787913289.088122 | frequency_hz=297.8
- [2026-08-28 18:34:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913289.3380013 | source=vosk | rms=1200 | updated_at=1787913289.3380013 | frequency_hz=297.8
- [2026-08-28 18:34:49] operator / voice_transcript_partial / voice: i think that
  meta: kind=partial | timestamp=1787913289.4559395 | source=vosk | rms=1200 | updated_at=1787913289.3380013 | frequency_hz=297.8
- [2026-08-28 18:34:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913289.5881362 | source=vosk | rms=1164 | updated_at=1787913289.5881362 | frequency_hz=259.4
- [2026-08-28 18:34:49] operator / voice_transcript_partial / voice: regardless
  meta: kind=partial | timestamp=1787913289.6369576 | source=vosk | rms=1164 | updated_at=1787913289.5881362 | frequency_hz=259.4
- [2026-08-28 18:34:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913289.839014 | source=vosk | rms=1017 | updated_at=1787913289.839014 | frequency_hz=219.7
- [2026-08-28 18:34:49] operator / voice_transcript_partial / voice: i think that regard for
  meta: kind=partial | timestamp=1787913289.9211705 | source=vosk | rms=1017 | updated_at=1787913289.839014 | frequency_hz=219.7
- [2026-08-28 18:34:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913290.0882676 | source=vosk | rms=1203 | updated_at=1787913290.0882676 | frequency_hz=249.2
- [2026-08-28 18:34:50] operator / voice_transcript_partial / voice: i think about four or
  meta: kind=partial | timestamp=1787913290.153939 | source=vosk | rms=1203 | updated_at=1787913290.0882676 | frequency_hz=249.2
- [2026-08-28 18:34:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913290.5247445 | source=vosk | rms=1201 | updated_at=1787913290.5247445 | frequency_hz=249.2
- [2026-08-28 18:34:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913290.9053404 | source=vosk | rms=986 | updated_at=1787913290.9053404 | frequency_hz=249.2
- [2026-08-28 18:34:51] operator / voice_transcript_final / voice: i think that regard for or
  meta: kind=final | timestamp=1787913291.320247 | source=final | rms=986 | updated_at=1787913290.9053404 | frequency_hz=249.2
- [2026-08-28 18:34:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913291.4254873 | source=vosk | rms=986 | updated_at=1787913290.9053404 | frequency_hz=249.2
- [2026-08-28 18:34:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913291.4254873 | source=vosk | rms=986 | updated_at=1787913290.9053404 | frequency_hz=249.2
- [2026-08-28 18:34:51] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1787913291.4841142 | source=vosk | rms=990 | updated_at=1787913291.4400132 | frequency_hz=249.2
- [2026-08-28 18:34:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913291.6429937 | source=vosk | rms=990 | updated_at=1787913291.4400132 | frequency_hz=249.2
- [2026-08-28 18:34:51] operator / voice_transcript_partial / voice: the question
  meta: kind=partial | timestamp=1787913291.6590278 | source=vosk | rms=990 | updated_at=1787913291.4400132 | frequency_hz=249.2
- [2026-08-28 18:34:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913291.8724747 | source=vosk | rms=990 | updated_at=1787913291.4400132 | frequency_hz=249.2
- [2026-08-28 18:34:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913292.0877707 | source=vosk | rms=1005 | updated_at=1787913292.0877707 | frequency_hz=249.2
- [2026-08-28 18:34:52] operator / voice_transcript_partial / voice: the question working
  meta: kind=partial | timestamp=1787913292.143807 | source=vosk | rms=1005 | updated_at=1787913292.0877707 | frequency_hz=249.2
- [2026-08-28 18:34:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913292.3808846 | source=vosk | rms=1005 | updated_at=1787913292.0877707 | frequency_hz=249.2
- [2026-08-28 18:34:52] operator / voice_transcript_partial / voice: the question or given a
  meta: kind=partial | timestamp=1787913292.4230063 | source=vosk | rms=1005 | updated_at=1787913292.0877707 | frequency_hz=249.2
- [2026-08-28 18:34:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913292.837353 | source=vosk | rms=1005 | updated_at=1787913292.0877707 | frequency_hz=249.2
- [2026-08-28 18:34:52] operator / voice_transcript_partial / voice: the question or given access
  meta: kind=partial | timestamp=1787913292.8601906 | source=vosk | rms=1005 | updated_at=1787913292.0877707 | frequency_hz=249.2
- [2026-08-28 18:34:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913293.0880535 | source=vosk | rms=1005 | updated_at=1787913292.0877707 | frequency_hz=249.2
- [2026-08-28 18:34:53] operator / voice_transcript_partial / voice: the question or give an accurate
  meta: kind=partial | timestamp=1787913293.1279533 | source=vosk | rms=1005 | updated_at=1787913292.0877707 | frequency_hz=249.2
- [2026-08-28 18:34:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913293.3911967 | source=vosk | rms=1200 | updated_at=1787913293.3911967 | frequency_hz=209.6
- [2026-08-28 18:34:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913294.087473 | source=vosk | rms=1162 | updated_at=1787913294.087473 | frequency_hz=200.6
- [2026-08-28 18:34:54] operator / voice_transcript_final / voice: the question or give an accurate
  meta: kind=final | timestamp=1787913294.4709191 | source=final | rms=1162 | updated_at=1787913294.087473 | frequency_hz=200.6
- [2026-08-28 18:34:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913294.5719833 | source=vosk | rms=1162 | updated_at=1787913294.087473 | frequency_hz=200.6
- [2026-08-28 18:34:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913294.5719833 | source=vosk | rms=982 | updated_at=1787913294.5719833 | frequency_hz=151.4
- [2026-08-28 18:34:54] operator / voice_transcript_partial / voice: all
  meta: kind=partial | timestamp=1787913294.6352203 | source=vosk | rms=982 | updated_at=1787913294.5719833 | frequency_hz=151.4
- [2026-08-28 18:34:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913295.0890079 | source=vosk | rms=982 | updated_at=1787913294.5719833 | frequency_hz=151.4
- [2026-08-28 18:34:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913299.5900662 | source=vosk | rms=982 | updated_at=1787913294.5719833 | frequency_hz=151.4
- [2026-08-28 18:35:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913300.0880892 | source=vosk | rms=982 | updated_at=1787913294.5719833 | frequency_hz=151.4
- [2026-08-28 18:35:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913300.3392198 | source=vosk | rms=982 | updated_at=1787913294.5719833 | frequency_hz=151.4
- [2026-08-28 18:35:00] operator / voice_transcript_final / voice: wow
  meta: kind=final | timestamp=1787913300.5365205 | source=final | rms=982 | updated_at=1787913294.5719833 | frequency_hz=151.4
- [2026-08-28 18:35:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913300.5879173 | source=vosk | rms=982 | updated_at=1787913294.5719833 | frequency_hz=151.4
- [2026-08-28 18:35:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913302.8391862 | source=vosk | rms=982 | updated_at=1787913294.5719833 | frequency_hz=151.4
- [2026-08-28 18:35:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913307.3384676 | source=vosk | rms=982 | updated_at=1787913294.5719833 | frequency_hz=151.4
- [2026-08-28 18:35:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913307.83791 | source=vosk | rms=982 | updated_at=1787913294.5719833 | frequency_hz=151.4
- [2026-08-28 18:35:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913308.3395345 | source=vosk | rms=982 | updated_at=1787913294.5719833 | frequency_hz=151.4
- [2026-08-28 18:35:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913310.0881314 | source=vosk | rms=1203 | updated_at=1787913309.588149 | frequency_hz=175.1
- [2026-08-28 18:35:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913310.8384233 | source=vosk | rms=1178 | updated_at=1787913310.8384233 | frequency_hz=187.3
- [2026-08-28 18:35:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913313.8384507 | source=vosk | rms=998 | updated_at=1787913313.33791 | frequency_hz=158.6
- [2026-08-28 18:35:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913314.5892897 | source=vosk | rms=998 | updated_at=1787913313.33791 | frequency_hz=158.6
- [2026-08-28 18:35:15] operator / voice_transcript_partial / voice: what's wrong
  meta: kind=partial | timestamp=1787913315.3630543 | source=vosk | rms=1201 | updated_at=1787913315.3381555 | frequency_hz=131.4
- [2026-08-28 18:35:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913315.5883777 | source=vosk | rms=1201 | updated_at=1787913315.3381555 | frequency_hz=131.4
- [2026-08-28 18:35:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913315.838672 | source=vosk | rms=1165 | updated_at=1787913315.838672 | frequency_hz=195.3
- [2026-08-28 18:35:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913316.08805 | source=vosk | rms=1200 | updated_at=1787913316.08805 | frequency_hz=226.3
- [2026-08-28 18:35:17] operator / voice_transcript_final / voice: what's wrong
  meta: kind=final | timestamp=1787913317.1823652 | source=final | rms=1200 | updated_at=1787913316.08805 | frequency_hz=226.3
- [2026-08-28 18:35:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913317.399732 | source=vosk | rms=1200 | updated_at=1787913316.08805 | frequency_hz=226.3
- [2026-08-28 18:35:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913317.399732 | source=vosk | rms=1201 | updated_at=1787913317.399732 | frequency_hz=237.4
- [2026-08-28 18:35:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913318.8385105 | source=vosk | rms=1111 | updated_at=1787913318.3380594 | frequency_hz=298.5
- [2026-08-28 18:35:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913321.0879612 | source=vosk | rms=1111 | updated_at=1787913318.3380594 | frequency_hz=298.5
- [2026-08-28 18:35:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913321.5888839 | source=vosk | rms=1111 | updated_at=1787913318.3380594 | frequency_hz=298.5
- [2026-08-28 18:35:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913323.5891812 | source=vosk | rms=1111 | updated_at=1787913318.3380594 | frequency_hz=298.5
- [2026-08-28 18:35:24] operator / voice_transcript_partial / voice: it
  meta: kind=partial | timestamp=1787913324.8798716 | source=vosk | rms=987 | updated_at=1787913324.8390503 | frequency_hz=298.5
- [2026-08-28 18:35:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913325.08905 | source=vosk | rms=987 | updated_at=1787913324.8390503 | frequency_hz=298.5
- [2026-08-28 18:35:25] operator / voice_transcript_partial / voice: it was
  meta: kind=partial | timestamp=1787913325.1219327 | source=vosk | rms=987 | updated_at=1787913324.8390503 | frequency_hz=298.5
- [2026-08-28 18:35:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913325.5884411 | source=vosk | rms=987 | updated_at=1787913324.8390503 | frequency_hz=298.5
- [2026-08-28 18:35:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913327.3383803 | source=vosk | rms=987 | updated_at=1787913324.8390503 | frequency_hz=298.5
- [2026-08-28 18:35:27] operator / voice_transcript_partial / voice: it was another
  meta: kind=partial | timestamp=1787913327.364085 | source=vosk | rms=987 | updated_at=1787913324.8390503 | frequency_hz=298.5
- [2026-08-28 18:35:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913327.5890548 | source=vosk | rms=987 | updated_at=1787913324.8390503 | frequency_hz=298.5
- [2026-08-28 18:35:27] operator / voice_transcript_partial / voice: it was in other places
  meta: kind=partial | timestamp=1787913327.6259923 | source=vosk | rms=987 | updated_at=1787913324.8390503 | frequency_hz=298.5
- [2026-08-28 18:35:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913328.0889702 | source=vosk | rms=987 | updated_at=1787913324.8390503 | frequency_hz=298.5
- [2026-08-28 18:35:28] operator / voice_transcript_partial / voice: it was another place was in
  meta: kind=partial | timestamp=1787913328.1221092 | source=vosk | rms=987 | updated_at=1787913324.8390503 | frequency_hz=298.5
- [2026-08-28 18:35:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913328.338788 | source=vosk | rms=1203 | updated_at=1787913328.338788 | frequency_hz=298.5
- [2026-08-28 18:35:28] operator / voice_transcript_partial / voice: it was another place was a lot of
  meta: kind=partial | timestamp=1787913328.4157975 | source=vosk | rms=1203 | updated_at=1787913328.338788 | frequency_hz=298.5
- [2026-08-28 18:35:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913328.838197 | source=vosk | rms=1203 | updated_at=1787913328.338788 | frequency_hz=298.5
- [2026-08-28 18:35:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913332.8387249 | source=vosk | rms=708 | updated_at=1787913332.8387249 | frequency_hz=298.5
- [2026-08-28 18:35:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913333.088361 | source=vosk | rms=1202 | updated_at=1787913333.088361 | frequency_hz=298.5
- [2026-08-28 18:35:33] operator / voice_transcript_partial / voice: it was another place was a lot of that
  meta: kind=partial | timestamp=1787913333.124532 | source=vosk | rms=1202 | updated_at=1787913333.088361 | frequency_hz=298.5
- [2026-08-28 18:35:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913333.5885696 | source=vosk | rms=1202 | updated_at=1787913333.088361 | frequency_hz=298.5
- [2026-08-28 18:35:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913333.8386283 | source=vosk | rms=1202 | updated_at=1787913333.088361 | frequency_hz=298.5
- [2026-08-28 18:35:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913334.3381865 | source=vosk | rms=1202 | updated_at=1787913333.088361 | frequency_hz=298.5
- [2026-08-28 18:35:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913334.589201 | source=vosk | rms=1202 | updated_at=1787913334.589201 | frequency_hz=298.5
- [2026-08-28 18:35:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913334.8387754 | source=vosk | rms=1201 | updated_at=1787913334.8387754 | frequency_hz=298.5
- [2026-08-28 18:35:34] operator / voice_transcript_partial / voice: it was another place was a lot of the
  meta: kind=partial | timestamp=1787913334.8841474 | source=vosk | rms=1201 | updated_at=1787913334.8387754 | frequency_hz=298.5
- [2026-08-28 18:35:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913335.0885265 | source=vosk | rms=1201 | updated_at=1787913334.8387754 | frequency_hz=298.5
- [2026-08-28 18:35:35] operator / voice_transcript_final / voice: it was another place was a lot of that
  meta: kind=final | timestamp=1787913335.4401739 | source=final | rms=1201 | updated_at=1787913334.8387754 | frequency_hz=298.5
- [2026-08-28 18:35:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913335.5586762 | source=vosk | rms=1201 | updated_at=1787913334.8387754 | frequency_hz=298.5
- [2026-08-28 18:35:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913335.5586762 | source=vosk | rms=1043 | updated_at=1787913335.5586762 | frequency_hz=298.5
- [2026-08-28 18:35:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913337.8392448 | source=vosk | rms=908 | updated_at=1787913335.589503 | frequency_hz=298.5
- [2026-08-28 18:35:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913338.088626 | source=vosk | rms=1201 | updated_at=1787913338.088626 | frequency_hz=298.5
- [2026-08-28 18:35:39] operator / voice_transcript_partial / voice: wasn't
  meta: kind=partial | timestamp=1787913339.1183734 | source=vosk | rms=886 | updated_at=1787913339.088752 | frequency_hz=298.5
- [2026-08-28 18:35:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913339.3389628 | source=vosk | rms=1202 | updated_at=1787913339.3389628 | frequency_hz=298.5
- [2026-08-28 18:35:39] operator / voice_transcript_partial / voice: what are they could be
  meta: kind=partial | timestamp=1787913339.4319239 | source=vosk | rms=1202 | updated_at=1787913339.3389628 | frequency_hz=298.5
- [2026-08-28 18:35:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913339.83927 | source=vosk | rms=1202 | updated_at=1787913339.3389628 | frequency_hz=298.5
- [2026-08-28 18:35:39] operator / voice_transcript_partial / voice: what i think of your
  meta: kind=partial | timestamp=1787913339.917888 | source=vosk | rms=1202 | updated_at=1787913339.3389628 | frequency_hz=298.5
- [2026-08-28 18:35:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913340.3384132 | source=vosk | rms=1202 | updated_at=1787913340.3384132 | frequency_hz=298.5
- [2026-08-28 18:35:40] operator / voice_transcript_partial / voice: what i think of your read
  meta: kind=partial | timestamp=1787913340.431927 | source=vosk | rms=1202 | updated_at=1787913340.3384132 | frequency_hz=298.5
- [2026-08-28 18:35:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913340.5960424 | source=vosk | rms=1201 | updated_at=1787913340.5960424 | frequency_hz=298.5
- [2026-08-28 18:35:40] operator / voice_transcript_partial / voice: what are they going to regret what i
  meta: kind=partial | timestamp=1787913340.6288602 | source=vosk | rms=1201 | updated_at=1787913340.5960424 | frequency_hz=298.5
- [2026-08-28 18:35:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913340.8393805 | source=vosk | rms=1201 | updated_at=1787913340.8393805 | frequency_hz=298.5
- [2026-08-28 18:35:40] operator / voice_transcript_partial / voice: what are they going to regret what
  meta: kind=partial | timestamp=1787913340.8689284 | source=vosk | rms=1201 | updated_at=1787913340.8393805 | frequency_hz=298.5
- [2026-08-28 18:35:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913341.0890906 | source=vosk | rms=1201 | updated_at=1787913340.8393805 | frequency_hz=298.5
- [2026-08-28 18:35:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913341.5972095 | source=vosk | rms=728 | updated_at=1787913341.5972095 | frequency_hz=298.5
- [2026-08-28 18:35:41] operator / voice_transcript_final / voice: what i think of your read what
  meta: kind=final | timestamp=1787913341.96015 | source=final | rms=728 | updated_at=1787913341.5972095 | frequency_hz=298.5
- [2026-08-28 18:35:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913342.1285932 | source=vosk | rms=728 | updated_at=1787913341.5972095 | frequency_hz=298.5
- [2026-08-28 18:35:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913342.1285932 | source=vosk | rms=728 | updated_at=1787913341.5972095 | frequency_hz=298.5
- [2026-08-28 18:35:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913343.7278972 | source=vosk | rms=1206 | updated_at=1787913342.5895908 | frequency_hz=298.5
- [2026-08-28 18:35:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913344.4693341 | source=vosk | rms=1206 | updated_at=1787913342.5895908 | frequency_hz=298.5
- [2026-08-28 18:35:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913344.9685585 | source=vosk | rms=1206 | updated_at=1787913342.5895908 | frequency_hz=298.5
- [2026-08-28 18:35:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913345.2236712 | source=vosk | rms=832 | updated_at=1787913345.2236712 | frequency_hz=298.5
- [2026-08-28 18:35:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913346.473223 | source=vosk | rms=832 | updated_at=1787913345.2236712 | frequency_hz=298.5
- [2026-08-28 18:35:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913347.2192805 | source=vosk | rms=832 | updated_at=1787913345.2236712 | frequency_hz=298.5
- [2026-08-28 18:35:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913348.219386 | source=vosk | rms=553 | updated_at=1787913347.4702544 | frequency_hz=298.5
- [2026-08-28 18:35:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913349.4692261 | source=vosk | rms=557 | updated_at=1787913349.4692261 | frequency_hz=298.5
- [2026-08-28 18:35:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913350.7195015 | source=vosk | rms=1201 | updated_at=1787913350.2194583 | frequency_hz=298.5
- [2026-08-28 18:35:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913354.2191117 | source=vosk | rms=1201 | updated_at=1787913350.2194583 | frequency_hz=298.5
- [2026-08-28 18:35:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913354.718854 | source=vosk | rms=1201 | updated_at=1787913350.2194583 | frequency_hz=298.5
- [2026-08-28 18:35:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913355.2194366 | source=vosk | rms=1201 | updated_at=1787913350.2194583 | frequency_hz=298.5
- [2026-08-28 18:35:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913355.719196 | source=vosk | rms=1201 | updated_at=1787913350.2194583 | frequency_hz=298.5
- [2026-08-28 18:35:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913355.9689074 | source=vosk | rms=1201 | updated_at=1787913350.2194583 | frequency_hz=298.5
- [2026-08-28 18:35:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913356.9695234 | source=vosk | rms=776 | updated_at=1787913356.469896 | frequency_hz=298.5
- [2026-08-28 18:35:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913358.469738 | source=vosk | rms=585 | updated_at=1787913358.469738 | frequency_hz=298.5
- [2026-08-28 18:35:59] operator / voice_transcript_final / voice: so
  meta: kind=final | timestamp=1787913359.0006082 | source=final | rms=593 | updated_at=1787913358.7190332 | frequency_hz=298.5
- [2026-08-28 18:35:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913359.538778 | source=vosk | rms=443 | updated_at=1787913359.538778 | frequency_hz=298.5
- [2026-08-28 18:36:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913361.2799845 | source=vosk | rms=435 | updated_at=1787913360.7793229 | frequency_hz=298.5
- [2026-08-28 18:36:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913362.7791233 | source=vosk | rms=471 | updated_at=1787913362.7791233 | frequency_hz=298.5
- [2026-08-28 18:36:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913363.2789688 | source=vosk | rms=471 | updated_at=1787913362.7791233 | frequency_hz=298.5
- [2026-08-28 18:36:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913365.5292888 | source=vosk | rms=471 | updated_at=1787913362.7791233 | frequency_hz=298.5
- [2026-08-28 18:36:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913366.2789917 | source=vosk | rms=471 | updated_at=1787913362.7791233 | frequency_hz=298.5
- [2026-08-28 18:36:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913366.5291615 | source=vosk | rms=471 | updated_at=1787913362.7791233 | frequency_hz=298.5
- [2026-08-28 18:36:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913367.0308526 | source=vosk | rms=471 | updated_at=1787913362.7791233 | frequency_hz=298.5
- [2026-08-28 18:36:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913367.2801964 | source=vosk | rms=471 | updated_at=1787913362.7791233 | frequency_hz=298.5
- [2026-08-28 18:36:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913369.5294414 | source=vosk | rms=1158 | updated_at=1787913369.0295172 | frequency_hz=298.5
- [2026-08-28 18:36:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913369.7797146 | source=vosk | rms=501 | updated_at=1787913369.7797146 | frequency_hz=298.5
- [2026-08-28 18:36:10] operator / voice_transcript_final / voice: oh wow
  meta: kind=final | timestamp=1787913370.988125 | source=final | rms=343 | updated_at=1787913370.5295708 | frequency_hz=298.5
- [2026-08-28 18:36:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913371.0299394 | source=vosk | rms=343 | updated_at=1787913370.5295708 | frequency_hz=298.5
- [2026-08-28 18:36:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913373.2793465 | source=vosk | rms=434 | updated_at=1787913372.7788906 | frequency_hz=298.5
- [2026-08-28 18:36:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913377.2792544 | source=vosk | rms=618 | updated_at=1787913377.2792544 | frequency_hz=298.5
- [2026-08-28 18:36:20] operator / voice_transcript_final / voice: roma
  meta: kind=final | timestamp=1787913380.4756172 | source=final | rms=543 | updated_at=1787913380.0302699 | frequency_hz=298.5
- [2026-08-28 18:36:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913380.5295353 | source=vosk | rms=284 | updated_at=1787913380.5295353 | frequency_hz=298.5
- [2026-08-28 18:36:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913381.2797258 | source=vosk | rms=304 | updated_at=1787913380.779646 | frequency_hz=298.5
- [2026-08-28 18:36:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913381.530116 | source=vosk | rms=304 | updated_at=1787913380.779646 | frequency_hz=298.5
- [2026-08-28 18:36:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913382.2795732 | source=vosk | rms=384 | updated_at=1787913381.779887 | frequency_hz=298.5
- [2026-08-28 18:36:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913384.029747 | source=vosk | rms=388 | updated_at=1787913384.029747 | frequency_hz=298.5
- [2026-08-28 18:36:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913384.7799487 | source=vosk | rms=418 | updated_at=1787913384.2790847 | frequency_hz=298.5
- [2026-08-28 18:36:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913385.0308726 | source=vosk | rms=418 | updated_at=1787913384.2790847 | frequency_hz=298.5
- [2026-08-28 18:36:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913386.279754 | source=vosk | rms=418 | updated_at=1787913384.2790847 | frequency_hz=298.5
- [2026-08-28 18:36:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913387.0295117 | source=vosk | rms=368 | updated_at=1787913387.0295117 | frequency_hz=298.5
- [2026-08-28 18:36:30] operator / voice_transcript_final / voice: supper
  meta: kind=final | timestamp=1787913390.2324038 | source=final | rms=674 | updated_at=1787913390.0297282 | frequency_hz=298.5
- [2026-08-28 18:36:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913390.2801628 | source=vosk | rms=526 | updated_at=1787913390.2801628 | frequency_hz=298.5
- [2026-08-28 18:36:31] operator / voice_transcript_partial / voice: i don't
  meta: kind=partial | timestamp=1787913391.545379 | source=vosk | rms=1201 | updated_at=1787913391.5303621 | frequency_hz=298.5
- [2026-08-28 18:36:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913391.7796686 | source=vosk | rms=922 | updated_at=1787913391.7796686 | frequency_hz=298.5
- [2026-08-28 18:36:31] operator / voice_transcript_partial / voice: i don't believe
  meta: kind=partial | timestamp=1787913391.8276775 | source=vosk | rms=922 | updated_at=1787913391.7796686 | frequency_hz=298.5
- [2026-08-28 18:36:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913392.0300088 | source=vosk | rms=526 | updated_at=1787913392.0300088 | frequency_hz=298.5
- [2026-08-28 18:36:32] operator / voice_transcript_partial / voice: i love the record
  meta: kind=partial | timestamp=1787913392.1361837 | source=vosk | rms=526 | updated_at=1787913392.0300088 | frequency_hz=298.5
- [2026-08-28 18:36:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913392.280409 | source=vosk | rms=526 | updated_at=1787913392.0300088 | frequency_hz=298.5
- [2026-08-28 18:36:32] operator / voice_transcript_partial / voice: i love the record though
  meta: kind=partial | timestamp=1787913392.3264627 | source=vosk | rms=526 | updated_at=1787913392.0300088 | frequency_hz=298.5
- [2026-08-28 18:36:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913392.780101 | source=vosk | rms=526 | updated_at=1787913392.0300088 | frequency_hz=298.5
- [2026-08-28 18:36:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913393.0301366 | source=vosk | rms=526 | updated_at=1787913392.0300088 | frequency_hz=298.5
- [2026-08-28 18:36:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913393.2804592 | source=vosk | rms=615 | updated_at=1787913393.2804592 | frequency_hz=298.5
- [2026-08-28 18:36:33] operator / voice_transcript_final / voice: i love that either though
  meta: kind=final | timestamp=1787913393.5540943 | source=final | rms=615 | updated_at=1787913393.2804592 | frequency_hz=298.5
- [2026-08-28 18:36:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913393.6579852 | source=vosk | rms=637 | updated_at=1787913393.6579852 | frequency_hz=298.5
- [2026-08-28 18:36:33] operator / voice_transcript_partial / voice: where
  meta: kind=partial | timestamp=1787913393.6817393 | source=vosk | rms=637 | updated_at=1787913393.6579852 | frequency_hz=298.5
- [2026-08-28 18:36:33] operator / voice_transcript_partial / voice: were going into
  meta: kind=partial | timestamp=1787913393.837195 | source=vosk | rms=824 | updated_at=1787913393.7804534 | frequency_hz=298.5
- [2026-08-28 18:36:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913394.0315676 | source=vosk | rms=505 | updated_at=1787913394.0315676 | frequency_hz=298.5
- [2026-08-28 18:36:34] operator / voice_transcript_partial / voice: where but it was
  meta: kind=partial | timestamp=1787913394.07468 | source=vosk | rms=505 | updated_at=1787913394.0315676 | frequency_hz=298.5
- [2026-08-28 18:36:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913394.2803695 | source=vosk | rms=756 | updated_at=1787913394.2803695 | frequency_hz=298.5
- [2026-08-28 18:36:34] operator / voice_transcript_partial / voice: where but it was pretty
  meta: kind=partial | timestamp=1787913394.3268132 | source=vosk | rms=756 | updated_at=1787913394.2803695 | frequency_hz=298.5
- [2026-08-28 18:36:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913394.5307274 | source=vosk | rms=527 | updated_at=1787913394.529724 | frequency_hz=298.5
- [2026-08-28 18:36:34] operator / voice_transcript_partial / voice: where but it was
  meta: kind=partial | timestamp=1787913394.5693133 | source=vosk | rms=527 | updated_at=1787913394.529724 | frequency_hz=298.5
- [2026-08-28 18:36:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913394.7800822 | source=vosk | rms=355 | updated_at=1787913394.7800822 | frequency_hz=298.5
- [2026-08-28 18:36:34] operator / voice_transcript_partial / voice: whether that i was trying to think
  meta: kind=partial | timestamp=1787913394.8320277 | source=vosk | rms=355 | updated_at=1787913394.7800822 | frequency_hz=298.5
- [2026-08-28 18:36:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913395.279895 | source=vosk | rms=472 | updated_at=1787913395.279895 | frequency_hz=298.5
- [2026-08-28 18:36:35] operator / voice_transcript_partial / voice: whether that i was trying to figure
  meta: kind=partial | timestamp=1787913395.3436637 | source=vosk | rms=472 | updated_at=1787913395.279895 | frequency_hz=298.5
- [2026-08-28 18:36:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913395.5305378 | source=vosk | rms=768 | updated_at=1787913395.5305378 | frequency_hz=298.5
- [2026-08-28 18:36:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913395.7802656 | source=vosk | rms=582 | updated_at=1787913395.7802656 | frequency_hz=298.5
- [2026-08-28 18:36:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913396.0297158 | source=vosk | rms=984 | updated_at=1787913396.0297158 | frequency_hz=298.5
- [2026-08-28 18:36:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913396.280192 | source=vosk | rms=597 | updated_at=1787913396.280192 | frequency_hz=298.5
- [2026-08-28 18:36:36] operator / voice_transcript_partial / voice: whether that i was trying to figure out
  meta: kind=partial | timestamp=1787913396.3282917 | source=vosk | rms=597 | updated_at=1787913396.280192 | frequency_hz=298.5
- [2026-08-28 18:36:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913396.5301292 | source=vosk | rms=624 | updated_at=1787913396.5301292 | frequency_hz=298.5
- [2026-08-28 18:36:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913396.7799149 | source=vosk | rms=594 | updated_at=1787913396.7799149 | frequency_hz=298.5
- [2026-08-28 18:36:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913397.031663 | source=vosk | rms=465 | updated_at=1787913397.031663 | frequency_hz=298.5
- [2026-08-28 18:36:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913397.3157792 | source=vosk | rms=465 | updated_at=1787913397.031663 | frequency_hz=298.5
- [2026-08-28 18:36:37] operator / voice_transcript_final / voice: where but it i was trying to figure out
  meta: kind=final | timestamp=1787913397.94472 | source=final | rms=465 | updated_at=1787913397.031663 | frequency_hz=298.5
- [2026-08-28 18:36:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913398.0785084 | source=vosk | rms=465 | updated_at=1787913397.031663 | frequency_hz=298.5
- [2026-08-28 18:36:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913398.0795088 | source=vosk | rms=658 | updated_at=1787913398.0795088 | frequency_hz=298.5
- [2026-08-28 18:36:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913400.5301642 | source=vosk | rms=758 | updated_at=1787913400.0626268 | frequency_hz=298.5
- [2026-08-28 18:36:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913400.7877886 | source=vosk | rms=718 | updated_at=1787913400.7877886 | frequency_hz=298.5
- [2026-08-28 18:36:41] operator / voice_transcript_partial / voice: i'm around
  meta: kind=partial | timestamp=1787913401.8392446 | source=vosk | rms=719 | updated_at=1787913401.7800918 | frequency_hz=298.5
- [2026-08-28 18:36:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913402.0316682 | source=vosk | rms=621 | updated_at=1787913402.0316682 | frequency_hz=298.5
- [2026-08-28 18:36:42] operator / voice_transcript_partial / voice: i'm around eleven
  meta: kind=partial | timestamp=1787913402.076725 | source=vosk | rms=621 | updated_at=1787913402.0316682 | frequency_hz=298.5
- [2026-08-28 18:36:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913402.2800775 | source=vosk | rms=1201 | updated_at=1787913402.2800775 | frequency_hz=298.5
- [2026-08-28 18:36:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913402.7813406 | source=vosk | rms=1201 | updated_at=1787913402.2800775 | frequency_hz=298.5
- [2026-08-28 18:36:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913403.28016 | source=vosk | rms=578 | updated_at=1787913403.28016 | frequency_hz=298.5
- [2026-08-28 18:36:43] operator / voice_transcript_partial / voice: i'm around a level that
  meta: kind=partial | timestamp=1787913403.338688 | source=vosk | rms=578 | updated_at=1787913403.28016 | frequency_hz=298.5
- [2026-08-28 18:36:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913403.7804277 | source=vosk | rms=578 | updated_at=1787913403.28016 | frequency_hz=298.5
- [2026-08-28 18:36:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913404.530782 | source=vosk | rms=454 | updated_at=1787913404.530782 | frequency_hz=298.5
- [2026-08-28 18:36:44] operator / voice_transcript_partial / voice: i'm around a little annoyed
  meta: kind=partial | timestamp=1787913404.5781941 | source=vosk | rms=454 | updated_at=1787913404.530782 | frequency_hz=298.5
- [2026-08-28 18:36:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913404.7798848 | source=vosk | rms=426 | updated_at=1787913404.7798848 | frequency_hz=298.5
- [2026-08-28 18:36:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913405.0306463 | source=vosk | rms=450 | updated_at=1787913405.0306463 | frequency_hz=298.5
- [2026-08-28 18:36:45] operator / voice_transcript_final / voice: i m around a little annoyed
  meta: kind=final | timestamp=1787913405.3286703 | source=final | rms=450 | updated_at=1787913405.0306463 | frequency_hz=298.5
- [2026-08-28 18:36:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913405.4580586 | source=vosk | rms=450 | updated_at=1787913405.0306463 | frequency_hz=298.5
- [2026-08-28 18:36:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913405.4580586 | source=vosk | rms=450 | updated_at=1787913405.0306463 | frequency_hz=298.5
- [2026-08-28 18:36:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913408.0304081 | source=vosk | rms=429 | updated_at=1787913407.5305686 | frequency_hz=298.5
- [2026-08-28 18:36:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913414.0486577 | source=vosk | rms=429 | updated_at=1787913407.5305686 | frequency_hz=298.5
- [2026-08-28 18:36:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913416.5641358 | source=vosk | rms=429 | updated_at=1787913407.5305686 | frequency_hz=298.5
- [2026-08-28 18:37:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913423.530499 | source=vosk | rms=429 | updated_at=1787913407.5305686 | frequency_hz=298.5
- [2026-08-28 18:37:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913424.030438 | source=vosk | rms=429 | updated_at=1787913407.5305686 | frequency_hz=298.5
- [2026-08-28 18:37:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913425.0483403 | source=vosk | rms=429 | updated_at=1787913407.5305686 | frequency_hz=298.5
- [2026-08-28 18:37:07] operator / voice_transcript_partial / voice: it's
  meta: kind=partial | timestamp=1787913427.793254 | source=vosk | rms=590 | updated_at=1787913427.7814157 | frequency_hz=298.5
- [2026-08-28 18:37:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913428.290998 | source=vosk | rms=590 | updated_at=1787913427.7814157 | frequency_hz=298.5
- [2026-08-28 18:37:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913428.5307317 | source=vosk | rms=736 | updated_at=1787913428.5307317 | frequency_hz=298.5
- [2026-08-28 18:37:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913429.0306509 | source=vosk | rms=441 | updated_at=1787913429.0306509 | frequency_hz=298.5
- [2026-08-28 18:37:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913429.280723 | source=vosk | rms=696 | updated_at=1787913429.280723 | frequency_hz=298.5
- [2026-08-28 18:37:09] operator / voice_transcript_final / voice: it s
  meta: kind=final | timestamp=1787913429.6906705 | source=final | rms=696 | updated_at=1787913429.280723 | frequency_hz=298.5
- [2026-08-28 18:37:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913429.7323885 | source=vosk | rms=696 | updated_at=1787913429.280723 | frequency_hz=298.5
- [2026-08-28 18:37:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913429.7808895 | source=vosk | rms=642 | updated_at=1787913429.7808895 | frequency_hz=298.5
- [2026-08-28 18:37:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913430.2811306 | source=vosk | rms=642 | updated_at=1787913429.7808895 | frequency_hz=298.5
- [2026-08-28 18:37:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913430.7807016 | source=vosk | rms=660 | updated_at=1787913430.7807016 | frequency_hz=298.5
- [2026-08-28 18:37:10] operator / voice_transcript_partial / voice: at
  meta: kind=partial | timestamp=1787913430.7932894 | source=vosk | rms=660 | updated_at=1787913430.7807016 | frequency_hz=298.5
- [2026-08-28 18:37:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913431.031387 | source=vosk | rms=660 | updated_at=1787913430.7807016 | frequency_hz=298.5
- [2026-08-28 18:37:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913431.2807286 | source=vosk | rms=660 | updated_at=1787913430.7807016 | frequency_hz=298.5
- [2026-08-28 18:37:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913431.5531747 | source=vosk | rms=858 | updated_at=1787913431.5531747 | frequency_hz=298.5
- [2026-08-28 18:37:11] operator / voice_transcript_final / voice: at
  meta: kind=final | timestamp=1787913431.7352064 | source=final | rms=858 | updated_at=1787913431.5531747 | frequency_hz=298.5
- [2026-08-28 18:37:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913431.781221 | source=vosk | rms=858 | updated_at=1787913431.5531747 | frequency_hz=298.5
- [2026-08-28 18:37:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913432.5314217 | source=vosk | rms=858 | updated_at=1787913431.5531747 | frequency_hz=298.5
- [2026-08-28 18:37:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913432.7825935 | source=vosk | rms=522 | updated_at=1787913432.7825935 | frequency_hz=298.5
- [2026-08-28 18:37:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913433.2814 | source=vosk | rms=522 | updated_at=1787913432.7825935 | frequency_hz=298.5
- [2026-08-28 18:37:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913433.5323045 | source=vosk | rms=356 | updated_at=1787913433.5323045 | frequency_hz=298.5
- [2026-08-28 18:37:13] operator / voice_transcript_partial / voice: at
  meta: kind=partial | timestamp=1787913433.793522 | source=vosk | rms=237 | updated_at=1787913433.7809792 | frequency_hz=298.5
- [2026-08-28 18:37:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913434.2811902 | source=vosk | rms=577 | updated_at=1787913434.2811902 | frequency_hz=298.5
- [2026-08-28 18:37:14] operator / voice_transcript_partial / voice: at that
  meta: kind=partial | timestamp=1787913434.3052304 | source=vosk | rms=577 | updated_at=1787913434.2811902 | frequency_hz=298.5
- [2026-08-28 18:37:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913434.7812834 | source=vosk | rms=577 | updated_at=1787913434.2811902 | frequency_hz=298.5
- [2026-08-28 18:37:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913435.0352087 | source=vosk | rms=518 | updated_at=1787913435.0352087 | frequency_hz=298.5
- [2026-08-28 18:37:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913435.7810657 | source=vosk | rms=397 | updated_at=1787913435.7810657 | frequency_hz=298.5
- [2026-08-28 18:37:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913436.2816067 | source=vosk | rms=397 | updated_at=1787913435.7810657 | frequency_hz=298.5
- [2026-08-28 18:37:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913436.7814562 | source=vosk | rms=272 | updated_at=1787913436.7814562 | frequency_hz=298.5
- [2026-08-28 18:37:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913437.0313509 | source=vosk | rms=330 | updated_at=1787913437.0313509 | frequency_hz=298.5
- [2026-08-28 18:37:17] operator / voice_transcript_final / voice: at that
  meta: kind=final | timestamp=1787913437.3017142 | source=final | rms=330 | updated_at=1787913437.0313509 | frequency_hz=298.5
- [2026-08-28 18:37:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913437.555791 | source=vosk | rms=330 | updated_at=1787913437.0313509 | frequency_hz=298.5
- [2026-08-28 18:37:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913439.780682 | source=vosk | rms=573 | updated_at=1787913439.780682 | frequency_hz=298.5
- [2026-08-28 18:37:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913440.281125 | source=vosk | rms=573 | updated_at=1787913439.780682 | frequency_hz=298.5
- [2026-08-28 18:37:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913442.5352693 | source=vosk | rms=1200 | updated_at=1787913442.5352693 | frequency_hz=298.5
- [2026-08-28 18:37:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913443.0317764 | source=vosk | rms=1200 | updated_at=1787913442.5352693 | frequency_hz=298.5
- [2026-08-28 18:37:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913445.0355422 | source=vosk | rms=249 | updated_at=1787913445.0355422 | frequency_hz=298.5
- [2026-08-28 18:37:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913445.534423 | source=vosk | rms=249 | updated_at=1787913445.0355422 | frequency_hz=298.5
- [2026-08-28 18:37:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913445.8096743 | source=vosk | rms=249 | updated_at=1787913445.0355422 | frequency_hz=298.5
- [2026-08-28 18:37:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913447.0312614 | source=vosk | rms=262 | updated_at=1787913446.5435069 | frequency_hz=298.5
- [2026-08-28 18:37:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913448.0371282 | source=vosk | rms=259 | updated_at=1787913448.0371282 | frequency_hz=298.5
- [2026-08-28 18:37:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913448.5320787 | source=vosk | rms=259 | updated_at=1787913448.0371282 | frequency_hz=298.5
- [2026-08-28 18:37:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913449.5311115 | source=vosk | rms=259 | updated_at=1787913448.0371282 | frequency_hz=298.5
- [2026-08-28 18:37:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913450.2811093 | source=vosk | rms=833 | updated_at=1787913449.7810965 | frequency_hz=298.5
- [2026-08-28 18:37:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913452.0314999 | source=vosk | rms=833 | updated_at=1787913449.7810965 | frequency_hz=298.5
- [2026-08-28 18:37:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913452.531422 | source=vosk | rms=833 | updated_at=1787913449.7810965 | frequency_hz=298.5
- [2026-08-28 18:37:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913458.281861 | source=vosk | rms=172 | updated_at=1787913458.281861 | frequency_hz=298.5
- [2026-08-28 18:37:46] operator / voice_transcript_partial / voice: democrats
  meta: kind=partial | timestamp=1787913466.049222 | source=vosk | rms=724 | updated_at=1787913465.2821083 | frequency_hz=298.5
- [2026-08-28 18:37:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913466.28203 | source=vosk | rms=299 | updated_at=1787913466.28203 | frequency_hz=298.5
- [2026-08-28 18:37:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913466.5332277 | source=vosk | rms=170 | updated_at=1787913466.5332277 | frequency_hz=298.5
- [2026-08-28 18:37:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913466.7815 | source=vosk | rms=178 | updated_at=1787913466.7815 | frequency_hz=298.5
- [2026-08-28 18:37:46] operator / voice_transcript_final / voice: democrats
  meta: kind=final | timestamp=1787913466.9654331 | source=final | rms=178 | updated_at=1787913466.7815 | frequency_hz=298.5
- [2026-08-28 18:37:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913467.031869 | source=vosk | rms=123 | updated_at=1787913467.031869 | frequency_hz=298.5
- [2026-08-28 18:37:52] operator / voice_transcript_final / voice: it
  meta: kind=final | timestamp=1787913472.0950143 | source=final | rms=448 | updated_at=1787913471.5344281 | frequency_hz=298.5
- [2026-08-28 18:37:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913472.282112 | source=vosk | rms=381 | updated_at=1787913472.282112 | frequency_hz=298.5
- [2026-08-28 18:37:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913473.5321906 | source=vosk | rms=948 | updated_at=1787913473.0321507 | frequency_hz=298.5
- [2026-08-28 18:37:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913473.7819345 | source=vosk | rms=948 | updated_at=1787913473.0321507 | frequency_hz=298.5
- [2026-08-28 18:37:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913474.7821126 | source=vosk | rms=948 | updated_at=1787913473.0321507 | frequency_hz=298.5
- [2026-08-28 18:37:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913475.5344107 | source=vosk | rms=948 | updated_at=1787913473.0321507 | frequency_hz=298.5
- [2026-08-28 18:37:55] operator / voice_transcript_partial / voice: rather than
  meta: kind=partial | timestamp=1787913475.8031442 | source=vosk | rms=268 | updated_at=1787913475.7821114 | frequency_hz=298.5
- [2026-08-28 18:37:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913476.2821462 | source=vosk | rms=268 | updated_at=1787913475.7821114 | frequency_hz=298.5
- [2026-08-28 18:37:59] operator / voice_transcript_final / voice: rug
  meta: kind=final | timestamp=1787913479.4889505 | source=final | rms=700 | updated_at=1787913479.2818038 | frequency_hz=298.5
- [2026-08-28 18:37:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913479.6431434 | source=vosk | rms=745 | updated_at=1787913479.6431434 | frequency_hz=298.5
- [2026-08-28 18:38:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913482.7823606 | source=vosk | rms=634 | updated_at=1787913482.0319722 | frequency_hz=298.5
- [2026-08-28 18:38:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913485.6300285 | source=vosk | rms=556 | updated_at=1787913485.6300285 | frequency_hz=298.5
- [2026-08-28 18:38:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913487.0326073 | source=vosk | rms=1072 | updated_at=1787913486.541949 | frequency_hz=298.5
- [2026-08-28 18:38:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913490.2825744 | source=vosk | rms=1072 | updated_at=1787913486.541949 | frequency_hz=298.5
- [2026-08-28 18:38:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913491.2828934 | source=vosk | rms=892 | updated_at=1787913490.7826195 | frequency_hz=298.5
- [2026-08-28 18:38:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913494.032966 | source=vosk | rms=892 | updated_at=1787913490.7826195 | frequency_hz=298.5
- [2026-08-28 18:38:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913494.783272 | source=vosk | rms=892 | updated_at=1787913490.7826195 | frequency_hz=298.5
- [2026-08-28 18:38:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913508.3623667 | source=vosk | rms=1200 | updated_at=1787913508.3623667 | frequency_hz=398.0
- [2026-08-28 18:38:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913509.3640316 | source=vosk | rms=1201 | updated_at=1787913508.8621626 | frequency_hz=398.0
- [2026-08-28 18:38:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913518.1253407 | source=vosk | rms=132 | updated_at=1787913518.1253407 | frequency_hz=398.0
- [2026-08-28 18:38:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913518.6129267 | source=vosk | rms=132 | updated_at=1787913518.1253407 | frequency_hz=398.0
- [2026-08-28 18:39:06] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787913546.8493207 | source=vosk | rms=132 | updated_at=1787913518.1253407 | frequency_hz=398.0
- [2026-08-28 18:39:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913547.19193 | source=vosk | rms=132 | updated_at=1787913518.1253407 | frequency_hz=398.0
- [2026-08-28 18:39:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913547.647749 | source=vosk | rms=132 | updated_at=1787913518.1253407 | frequency_hz=398.0
- [2026-08-28 18:39:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913548.0941792 | source=vosk | rms=132 | updated_at=1787913518.1253407 | frequency_hz=398.0
- [2026-08-28 18:39:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913548.6257808 | source=vosk | rms=132 | updated_at=1787913518.1253407 | frequency_hz=398.0
- [2026-08-28 18:39:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913556.0935419 | source=vosk | rms=132 | updated_at=1787913518.1253407 | frequency_hz=398.0
- [2026-08-28 18:39:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913556.5937092 | source=vosk | rms=132 | updated_at=1787913518.1253407 | frequency_hz=398.0
- [2026-08-28 18:39:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913566.6447606 | source=vosk | rms=423 | updated_at=1787913566.6447606 | frequency_hz=398.0
- [2026-08-28 18:39:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913567.3946075 | source=vosk | rms=161 | updated_at=1787913566.9121332 | frequency_hz=398.0
- [2026-08-28 18:39:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913569.6439772 | source=vosk | rms=293 | updated_at=1787913569.6439772 | frequency_hz=398.0
- [2026-08-28 18:39:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913570.769128 | source=vosk | rms=437 | updated_at=1787913570.1442785 | frequency_hz=398.0
- [2026-08-28 18:39:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913575.3946128 | source=vosk | rms=441 | updated_at=1787913575.3946128 | frequency_hz=398.0
- [2026-08-28 18:39:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913576.3939013 | source=vosk | rms=411 | updated_at=1787913575.6445272 | frequency_hz=398.0
- [2026-08-28 18:39:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913590.1451643 | source=vosk | rms=411 | updated_at=1787913575.6445272 | frequency_hz=398.0
- [2026-08-28 18:39:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913591.894681 | source=vosk | rms=122 | updated_at=1787913591.3948922 | frequency_hz=398.0
- [2026-08-28 18:39:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913593.1454308 | source=vosk | rms=122 | updated_at=1787913591.3948922 | frequency_hz=398.0
- [2026-08-28 18:39:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913593.6447818 | source=vosk | rms=122 | updated_at=1787913591.3948922 | frequency_hz=398.0
- [2026-08-28 18:39:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913594.1442084 | source=vosk | rms=122 | updated_at=1787913591.3948922 | frequency_hz=398.0
- [2026-08-28 18:39:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913594.8944628 | source=vosk | rms=122 | updated_at=1787913591.3948922 | frequency_hz=398.0
- [2026-08-28 18:39:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913595.8959525 | source=vosk | rms=125 | updated_at=1787913595.8959525 | frequency_hz=398.0
- [2026-08-28 18:39:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913598.3947613 | source=vosk | rms=149 | updated_at=1787913597.8973389 | frequency_hz=398.0
- [2026-08-28 18:39:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913598.6452184 | source=vosk | rms=1158 | updated_at=1787913598.6452184 | frequency_hz=398.0
- [2026-08-28 18:39:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913599.145319 | source=vosk | rms=1158 | updated_at=1787913598.6452184 | frequency_hz=398.0
- [2026-08-28 18:39:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913599.6480842 | source=vosk | rms=1158 | updated_at=1787913598.6452184 | frequency_hz=398.0
- [2026-08-28 18:40:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913600.1456022 | source=vosk | rms=1158 | updated_at=1787913598.6452184 | frequency_hz=398.0
- [2026-08-28 18:40:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913605.8955116 | source=vosk | rms=1202 | updated_at=1787913605.8955116 | frequency_hz=398.0
- [2026-08-28 18:40:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913608.1452026 | source=vosk | rms=762 | updated_at=1787913607.65406 | frequency_hz=398.0
- [2026-08-28 18:40:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913608.3975449 | source=vosk | rms=608 | updated_at=1787913608.3975449 | frequency_hz=398.0
- [2026-08-28 18:40:08] operator / voice_transcript_partial / voice: at
  meta: kind=partial | timestamp=1787913608.4364743 | source=vosk | rms=608 | updated_at=1787913608.3975449 | frequency_hz=398.0
- [2026-08-28 18:40:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913608.647227 | source=vosk | rms=608 | updated_at=1787913608.3975449 | frequency_hz=398.0
- [2026-08-28 18:40:08] operator / voice_transcript_partial / voice: at at at
  meta: kind=partial | timestamp=1787913608.6775057 | source=vosk | rms=608 | updated_at=1787913608.3975449 | frequency_hz=398.0
- [2026-08-28 18:40:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913609.144827 | source=vosk | rms=608 | updated_at=1787913608.3975449 | frequency_hz=398.0
- [2026-08-28 18:40:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913609.395528 | source=vosk | rms=696 | updated_at=1787913609.395528 | frequency_hz=398.0
- [2026-08-28 18:40:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913609.645407 | source=vosk | rms=696 | updated_at=1787913609.395528 | frequency_hz=398.0
- [2026-08-28 18:40:09] operator / voice_transcript_partial / voice: at at at at
  meta: kind=partial | timestamp=1787913609.6565583 | source=vosk | rms=696 | updated_at=1787913609.395528 | frequency_hz=398.0
- [2026-08-28 18:40:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913610.1451635 | source=vosk | rms=696 | updated_at=1787913609.395528 | frequency_hz=398.0
- [2026-08-28 18:40:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913610.3953645 | source=vosk | rms=675 | updated_at=1787913610.3953645 | frequency_hz=398.0
- [2026-08-28 18:40:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913610.898299 | source=vosk | rms=675 | updated_at=1787913610.3953645 | frequency_hz=398.0
- [2026-08-28 18:40:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913611.6456664 | source=vosk | rms=604 | updated_at=1787913611.6456664 | frequency_hz=398.0
- [2026-08-28 18:40:11] operator / voice_transcript_partial / voice: at at at at at
  meta: kind=partial | timestamp=1787913611.6526768 | source=vosk | rms=604 | updated_at=1787913611.6456664 | frequency_hz=398.0
- [2026-08-28 18:40:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913611.895133 | source=vosk | rms=604 | updated_at=1787913611.6456664 | frequency_hz=398.0
- [2026-08-28 18:40:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913612.3949122 | source=vosk | rms=604 | updated_at=1787913611.6456664 | frequency_hz=398.0
- [2026-08-28 18:40:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913613.1414628 | source=vosk | rms=706 | updated_at=1787913613.1414628 | frequency_hz=398.0
- [2026-08-28 18:40:13] operator / voice_transcript_partial / voice: at at at at at at
  meta: kind=partial | timestamp=1787913613.1550014 | source=vosk | rms=706 | updated_at=1787913613.1414628 | frequency_hz=398.0
- [2026-08-28 18:40:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913613.6451304 | source=vosk | rms=706 | updated_at=1787913613.1414628 | frequency_hz=398.0
- [2026-08-28 18:40:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913614.6451008 | source=vosk | rms=988 | updated_at=1787913614.6451008 | frequency_hz=398.0
- [2026-08-28 18:40:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913614.895105 | source=vosk | rms=988 | updated_at=1787913614.6451008 | frequency_hz=398.0
- [2026-08-28 18:40:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913615.3950508 | source=vosk | rms=988 | updated_at=1787913614.6451008 | frequency_hz=398.0
- [2026-08-28 18:40:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913616.1451032 | source=vosk | rms=814 | updated_at=1787913616.1451032 | frequency_hz=398.0
- [2026-08-28 18:40:16] operator / voice_transcript_final / voice: at at at at at at
  meta: kind=final | timestamp=1787913616.7865832 | source=final | rms=814 | updated_at=1787913616.1451032 | frequency_hz=398.0
- [2026-08-28 18:40:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913616.8453941 | source=vosk | rms=814 | updated_at=1787913616.1451032 | frequency_hz=398.0
- [2026-08-28 18:40:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913616.8957636 | source=vosk | rms=859 | updated_at=1787913616.8957636 | frequency_hz=398.0
- [2026-08-28 18:40:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913617.3950841 | source=vosk | rms=859 | updated_at=1787913616.8957636 | frequency_hz=398.0
- [2026-08-28 18:40:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913617.6456504 | source=vosk | rms=151 | updated_at=1787913617.6456504 | frequency_hz=398.0
- [2026-08-28 18:40:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913618.3949032 | source=vosk | rms=252 | updated_at=1787913617.8953943 | frequency_hz=398.0
- [2026-08-28 18:40:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913619.8951626 | source=vosk | rms=252 | updated_at=1787913617.8953943 | frequency_hz=398.0
- [2026-08-28 18:40:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913620.645107 | source=vosk | rms=189 | updated_at=1787913620.1454268 | frequency_hz=398.0
- [2026-08-28 18:40:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913622.9049444 | source=vosk | rms=798 | updated_at=1787913622.9049444 | frequency_hz=398.0
- [2026-08-28 18:40:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913624.700095 | source=vosk | rms=1011 | updated_at=1787913624.145289 | frequency_hz=398.0
- [2026-08-28 18:40:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913624.8953028 | source=vosk | rms=320 | updated_at=1787913624.8953028 | frequency_hz=398.0
- [2026-08-28 18:40:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913625.6466277 | source=vosk | rms=429 | updated_at=1787913625.1459873 | frequency_hz=398.0
- [2026-08-28 18:40:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913627.1462212 | source=vosk | rms=484 | updated_at=1787913627.1447115 | frequency_hz=398.0
- [2026-08-28 18:40:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913627.8946908 | source=vosk | rms=484 | updated_at=1787913627.1447115 | frequency_hz=398.0
- [2026-08-28 18:40:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913629.8956478 | source=vosk | rms=653 | updated_at=1787913629.8956478 | frequency_hz=398.0
- [2026-08-28 18:40:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913630.3956456 | source=vosk | rms=653 | updated_at=1787913629.8956478 | frequency_hz=398.0
- [2026-08-28 18:40:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913636.8955753 | source=vosk | rms=172 | updated_at=1787913636.8955753 | frequency_hz=398.0
- [2026-08-28 18:40:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913637.895922 | source=vosk | rms=224 | updated_at=1787913637.3958728 | frequency_hz=398.0
- [2026-08-28 18:40:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913638.3956578 | source=vosk | rms=154 | updated_at=1787913638.3956578 | frequency_hz=398.0
- [2026-08-28 18:40:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913638.8990629 | source=vosk | rms=154 | updated_at=1787913638.3956578 | frequency_hz=398.0
- [2026-08-28 18:41:03] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787913663.1677997 | source=vosk | rms=154 | updated_at=1787913638.3956578 | frequency_hz=398.0
- [2026-08-28 18:41:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913674.0165372 | source=vosk | rms=131 | updated_at=1787913674.0165372 | frequency_hz=398.0
- [2026-08-28 18:41:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913674.4781208 | source=vosk | rms=131 | updated_at=1787913674.0165372 | frequency_hz=398.0
- [2026-08-28 18:41:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913685.4771495 | source=vosk | rms=131 | updated_at=1787913674.0165372 | frequency_hz=398.0
- [2026-08-28 18:41:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913685.9768157 | source=vosk | rms=131 | updated_at=1787913674.0165372 | frequency_hz=398.0
- [2026-08-28 18:41:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913688.7285225 | source=vosk | rms=131 | updated_at=1787913674.0165372 | frequency_hz=398.0
- [2026-08-28 18:41:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913689.2273037 | source=vosk | rms=131 | updated_at=1787913674.0165372 | frequency_hz=398.0
- [2026-08-28 18:41:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913691.7274582 | source=vosk | rms=131 | updated_at=1787913674.0165372 | frequency_hz=398.0
- [2026-08-28 18:41:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913692.7269328 | source=vosk | rms=132 | updated_at=1787913692.2274787 | frequency_hz=398.0
- [2026-08-28 18:41:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913692.9782596 | source=vosk | rms=132 | updated_at=1787913692.2274787 | frequency_hz=398.0
- [2026-08-28 18:41:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913705.7371392 | source=vosk | rms=153 | updated_at=1787913705.227103 | frequency_hz=398.0
- [2026-08-28 18:41:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913705.9773083 | source=vosk | rms=153 | updated_at=1787913705.227103 | frequency_hz=398.0
- [2026-08-28 18:41:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913719.9780896 | source=vosk | rms=120 | updated_at=1787913716.4772582 | frequency_hz=398.0
- [2026-08-28 18:42:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913720.2289262 | source=vosk | rms=120 | updated_at=1787913716.4772582 | frequency_hz=398.0
- [2026-08-28 18:42:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913721.6812346 | source=vosk | rms=120 | updated_at=1787913716.4772582 | frequency_hz=398.0
- [2026-08-28 18:42:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913721.7274542 | source=vosk | rms=120 | updated_at=1787913716.4772582 | frequency_hz=398.0
- [2026-08-28 18:42:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913722.477515 | source=vosk | rms=120 | updated_at=1787913716.4772582 | frequency_hz=398.0
- [2026-08-28 18:42:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913722.7467408 | source=vosk | rms=120 | updated_at=1787913716.4772582 | frequency_hz=398.0
- [2026-08-28 18:42:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913727.2274327 | source=vosk | rms=120 | updated_at=1787913716.4772582 | frequency_hz=398.0
- [2026-08-28 18:42:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913736.4784338 | source=vosk | rms=120 | updated_at=1787913716.4772582 | frequency_hz=398.0
- [2026-08-28 18:42:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913736.9783118 | source=vosk | rms=120 | updated_at=1787913716.4772582 | frequency_hz=398.0
- [2026-08-28 18:42:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913745.2283037 | source=vosk | rms=213 | updated_at=1787913745.2283037 | frequency_hz=398.0
- [2026-08-28 18:42:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913745.7485614 | source=vosk | rms=213 | updated_at=1787913745.2283037 | frequency_hz=398.0
- [2026-08-28 18:42:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913747.2281163 | source=vosk | rms=149 | updated_at=1787913747.2281163 | frequency_hz=398.0
- [2026-08-28 18:42:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913748.2288353 | source=vosk | rms=149 | updated_at=1787913747.2281163 | frequency_hz=398.0
- [2026-08-28 18:42:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913767.6029873 | source=vosk | rms=149 | updated_at=1787913747.2281163 | frequency_hz=398.0
- [2026-08-28 18:42:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913768.2295158 | source=vosk | rms=149 | updated_at=1787913747.2281163 | frequency_hz=398.0
- [2026-08-28 18:42:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913770.7352815 | source=vosk | rms=149 | updated_at=1787913747.2281163 | frequency_hz=398.0
- [2026-08-28 18:42:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913772.4788775 | source=vosk | rms=149 | updated_at=1787913747.2281163 | frequency_hz=398.0
- [2026-08-28 18:42:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913772.979292 | source=vosk | rms=206 | updated_at=1787913772.979292 | frequency_hz=398.0
- [2026-08-28 18:42:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913778.7595696 | source=vosk | rms=144 | updated_at=1787913778.2285533 | frequency_hz=398.0
- [2026-08-28 18:43:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913788.689814 | source=vosk | rms=132 | updated_at=1787913788.689814 | frequency_hz=398.0
- [2026-08-28 18:43:09] operator / voice_transcript_partial / voice: hello
  meta: kind=partial | timestamp=1787913789.7063625 | source=vosk | rms=686 | updated_at=1787913789.6898227 | frequency_hz=398.0
- [2026-08-28 18:43:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913789.9398963 | source=vosk | rms=348 | updated_at=1787913789.9398963 | frequency_hz=398.0
- [2026-08-28 18:43:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913790.4388297 | source=vosk | rms=348 | updated_at=1787913789.9398963 | frequency_hz=398.0
- [2026-08-28 18:43:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913796.439772 | source=vosk | rms=348 | updated_at=1787913789.9398963 | frequency_hz=398.0
- [2026-08-28 18:43:16] operator / voice_transcript_partial / voice: hello so my
  meta: kind=partial | timestamp=1787913796.4954526 | source=vosk | rms=348 | updated_at=1787913789.9398963 | frequency_hz=398.0
- [2026-08-28 18:43:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913796.9397998 | source=vosk | rms=144 | updated_at=1787913796.9397998 | frequency_hz=398.0
- [2026-08-28 18:43:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913797.4418898 | source=vosk | rms=144 | updated_at=1787913796.9397998 | frequency_hz=398.0
- [2026-08-28 18:43:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913799.689308 | source=vosk | rms=187 | updated_at=1787913799.689308 | frequency_hz=398.0
- [2026-08-28 18:43:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913799.9393816 | source=vosk | rms=164 | updated_at=1787913799.9393816 | frequency_hz=398.0
- [2026-08-28 18:43:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913800.1965342 | source=vosk | rms=164 | updated_at=1787913799.9393816 | frequency_hz=398.0
- [2026-08-28 18:43:20] operator / voice_transcript_final / voice: hello so by
  meta: kind=final | timestamp=1787913800.4817603 | source=final | rms=164 | updated_at=1787913799.9393816 | frequency_hz=398.0
- [2026-08-28 18:43:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913800.7778716 | source=vosk | rms=164 | updated_at=1787913799.9393816 | frequency_hz=398.0
- [2026-08-28 18:43:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913800.7778716 | source=vosk | rms=164 | updated_at=1787913799.9393816 | frequency_hz=398.0
- [2026-08-28 18:43:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913801.4399796 | source=vosk | rms=164 | updated_at=1787913799.9393816 | frequency_hz=398.0
- [2026-08-28 18:43:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913801.6911862 | source=vosk | rms=402 | updated_at=1787913801.6911862 | frequency_hz=398.0
- [2026-08-28 18:43:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913802.445844 | source=vosk | rms=233 | updated_at=1787913801.9422467 | frequency_hz=398.0
- [2026-08-28 18:43:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913806.6920226 | source=vosk | rms=183 | updated_at=1787913806.6920226 | frequency_hz=398.0
- [2026-08-28 18:43:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913807.4399943 | source=vosk | rms=183 | updated_at=1787913806.6920226 | frequency_hz=398.0
- [2026-08-28 18:43:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913811.200869 | source=vosk | rms=194 | updated_at=1787913811.200869 | frequency_hz=398.0
- [2026-08-28 18:43:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913812.6896985 | source=vosk | rms=194 | updated_at=1787913811.200869 | frequency_hz=398.0
- [2026-08-28 18:43:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913813.6899095 | source=vosk | rms=194 | updated_at=1787913811.200869 | frequency_hz=398.0
- [2026-08-28 18:43:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913814.1914225 | source=vosk | rms=194 | updated_at=1787913811.200869 | frequency_hz=398.0
- [2026-08-28 18:43:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913822.1901875 | source=vosk | rms=182 | updated_at=1787913822.1901875 | frequency_hz=264.0
- [2026-08-28 18:43:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913822.9407392 | source=vosk | rms=182 | updated_at=1787913822.1901875 | frequency_hz=264.0
- [2026-08-28 18:43:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913834.2268138 | source=vosk | rms=182 | updated_at=1787913822.1901875 | frequency_hz=264.0
- [2026-08-28 18:43:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913834.6899762 | source=vosk | rms=182 | updated_at=1787913822.1901875 | frequency_hz=264.0
- [2026-08-28 18:43:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913836.6906915 | source=vosk | rms=252 | updated_at=1787913836.6906915 | frequency_hz=264.0
- [2026-08-28 18:43:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913837.4408052 | source=vosk | rms=252 | updated_at=1787913836.6906915 | frequency_hz=264.0
- [2026-08-28 18:44:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913845.441203 | source=vosk | rms=252 | updated_at=1787913836.6906915 | frequency_hz=264.0
- [2026-08-28 18:44:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913847.9406047 | source=vosk | rms=160 | updated_at=1787913846.940552 | frequency_hz=264.0
- [2026-08-28 18:44:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913848.441131 | source=vosk | rms=160 | updated_at=1787913846.940552 | frequency_hz=264.0
- [2026-08-28 18:44:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913849.3122292 | source=vosk | rms=160 | updated_at=1787913846.940552 | frequency_hz=264.0
- [2026-08-28 18:44:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913849.441143 | source=vosk | rms=160 | updated_at=1787913846.940552 | frequency_hz=264.0
- [2026-08-28 18:44:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913857.4007516 | source=vosk | rms=139 | updated_at=1787913854.9014387 | frequency_hz=264.0
- [2026-08-28 18:44:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913857.942073 | source=vosk | rms=139 | updated_at=1787913854.9014387 | frequency_hz=264.0
- [2026-08-28 18:44:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913858.4412951 | source=vosk | rms=139 | updated_at=1787913854.9014387 | frequency_hz=264.0
- [2026-08-28 18:44:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913858.6914387 | source=vosk | rms=139 | updated_at=1787913854.9014387 | frequency_hz=264.0
- [2026-08-28 18:44:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913859.4412224 | source=vosk | rms=139 | updated_at=1787913854.9014387 | frequency_hz=264.0
- [2026-08-28 18:44:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913860.9432423 | source=vosk | rms=139 | updated_at=1787913854.9014387 | frequency_hz=264.0
- [2026-08-28 18:44:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913861.4412603 | source=vosk | rms=139 | updated_at=1787913854.9014387 | frequency_hz=264.0
- [2026-08-28 18:44:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913861.9407275 | source=vosk | rms=139 | updated_at=1787913854.9014387 | frequency_hz=264.0
- [2026-08-28 18:44:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913862.9413033 | source=vosk | rms=139 | updated_at=1787913854.9014387 | frequency_hz=264.0
- [2026-08-28 18:44:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913863.6907103 | source=vosk | rms=139 | updated_at=1787913854.9014387 | frequency_hz=264.0
- [2026-08-28 18:44:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913865.19156 | source=vosk | rms=139 | updated_at=1787913854.9014387 | frequency_hz=264.0
- [2026-08-28 18:44:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913865.691517 | source=vosk | rms=179 | updated_at=1787913865.691517 | frequency_hz=264.0
- [2026-08-28 18:44:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913866.9415886 | source=vosk | rms=179 | updated_at=1787913865.691517 | frequency_hz=264.0
- [2026-08-28 18:44:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913868.376013 | source=vosk | rms=179 | updated_at=1787913865.691517 | frequency_hz=264.0
- [2026-08-28 18:44:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913868.9407148 | source=vosk | rms=179 | updated_at=1787913865.691517 | frequency_hz=264.0
- [2026-08-28 18:44:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913870.4411345 | source=vosk | rms=179 | updated_at=1787913865.691517 | frequency_hz=264.0
- [2026-08-28 18:44:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913871.1938183 | source=vosk | rms=179 | updated_at=1787913865.691517 | frequency_hz=264.0
- [2026-08-28 18:44:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913871.4410357 | source=vosk | rms=179 | updated_at=1787913865.691517 | frequency_hz=264.0
- [2026-08-28 18:44:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913872.4413135 | source=vosk | rms=179 | updated_at=1787913865.691517 | frequency_hz=264.0
- [2026-08-28 18:44:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913872.9466772 | source=vosk | rms=179 | updated_at=1787913865.691517 | frequency_hz=264.0
- [2026-08-28 18:44:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913873.4414153 | source=vosk | rms=179 | updated_at=1787913865.691517 | frequency_hz=264.0
- [2026-08-28 18:44:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913876.6913395 | source=vosk | rms=179 | updated_at=1787913865.691517 | frequency_hz=264.0
- [2026-08-28 18:44:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913877.19284 | source=vosk | rms=179 | updated_at=1787913865.691517 | frequency_hz=264.0
- [2026-08-28 18:45:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913908.9426088 | source=vosk | rms=148 | updated_at=1787913908.9426088 | frequency_hz=264.0
- [2026-08-28 18:45:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913909.4423997 | source=vosk | rms=148 | updated_at=1787913908.9426088 | frequency_hz=264.0
- [2026-08-28 18:45:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913927.1920788 | source=vosk | rms=148 | updated_at=1787913908.9426088 | frequency_hz=264.0
- [2026-08-28 18:45:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913927.692726 | source=vosk | rms=148 | updated_at=1787913908.9426088 | frequency_hz=264.0
- [2026-08-28 18:45:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913928.4428167 | source=vosk | rms=122 | updated_at=1787913928.4428167 | frequency_hz=264.0
- [2026-08-28 18:45:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913928.942758 | source=vosk | rms=122 | updated_at=1787913928.4428167 | frequency_hz=264.0
- [2026-08-28 18:45:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913931.9448962 | source=vosk | rms=122 | updated_at=1787913928.4428167 | frequency_hz=264.0
- [2026-08-28 18:45:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913933.6974764 | source=vosk | rms=314 | updated_at=1787913932.702473 | frequency_hz=264.0
- [2026-08-28 18:45:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913935.4429545 | source=vosk | rms=314 | updated_at=1787913932.702473 | frequency_hz=264.0
- [2026-08-28 18:45:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913935.942866 | source=vosk | rms=314 | updated_at=1787913932.702473 | frequency_hz=264.0
- [2026-08-28 18:45:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913937.4432883 | source=vosk | rms=314 | updated_at=1787913932.702473 | frequency_hz=264.0
- [2026-08-28 18:45:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913937.9428878 | source=vosk | rms=314 | updated_at=1787913932.702473 | frequency_hz=264.0
- [2026-08-28 18:45:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913942.4431043 | source=vosk | rms=314 | updated_at=1787913932.702473 | frequency_hz=264.0
- [2026-08-28 18:45:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913942.9427235 | source=vosk | rms=314 | updated_at=1787913932.702473 | frequency_hz=264.0
- [2026-08-28 18:45:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913943.1960735 | source=vosk | rms=314 | updated_at=1787913932.702473 | frequency_hz=264.0
- [2026-08-28 18:45:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913943.6929023 | source=vosk | rms=314 | updated_at=1787913932.702473 | frequency_hz=264.0
- [2026-08-28 18:45:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913943.9427073 | source=vosk | rms=139 | updated_at=1787913943.9427073 | frequency_hz=264.0
- [2026-08-28 18:45:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913944.4487016 | source=vosk | rms=139 | updated_at=1787913943.9427073 | frequency_hz=264.0
- [2026-08-28 18:45:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913944.6926694 | source=vosk | rms=139 | updated_at=1787913943.9427073 | frequency_hz=264.0
- [2026-08-28 18:45:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913947.443414 | source=vosk | rms=140 | updated_at=1787913946.1941454 | frequency_hz=264.0
- [2026-08-28 18:45:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913947.9427102 | source=vosk | rms=220 | updated_at=1787913947.9427102 | frequency_hz=264.0
- [2026-08-28 18:45:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913948.4527252 | source=vosk | rms=220 | updated_at=1787913947.9427102 | frequency_hz=264.0
- [2026-08-28 18:45:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913948.692809 | source=vosk | rms=220 | updated_at=1787913947.9427102 | frequency_hz=264.0
- [2026-08-28 18:45:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913950.4442148 | source=vosk | rms=176 | updated_at=1787913949.942671 | frequency_hz=264.0
- [2026-08-28 18:45:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913951.4043264 | source=vosk | rms=151 | updated_at=1787913951.4043264 | frequency_hz=264.0
- [2026-08-28 18:45:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913951.9428847 | source=vosk | rms=151 | updated_at=1787913951.4043264 | frequency_hz=264.0
- [2026-08-28 18:45:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913955.4445355 | source=vosk | rms=151 | updated_at=1787913951.4043264 | frequency_hz=264.0
- [2026-08-28 18:45:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913956.443649 | source=vosk | rms=147 | updated_at=1787913955.692995 | frequency_hz=264.0
- [2026-08-28 18:45:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913959.443519 | source=vosk | rms=147 | updated_at=1787913955.692995 | frequency_hz=264.0
- [2026-08-28 18:46:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913960.1926653 | source=vosk | rms=147 | updated_at=1787913955.692995 | frequency_hz=264.0
- [2026-08-28 18:46:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913961.943192 | source=vosk | rms=167 | updated_at=1787913961.943192 | frequency_hz=264.0
- [2026-08-28 18:46:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913962.443718 | source=vosk | rms=167 | updated_at=1787913961.943192 | frequency_hz=264.0
- [2026-08-28 18:46:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913962.943551 | source=vosk | rms=167 | updated_at=1787913961.943192 | frequency_hz=264.0
- [2026-08-28 18:46:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913966.1994722 | source=vosk | rms=153 | updated_at=1787913964.943155 | frequency_hz=264.0
- [2026-08-28 18:46:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913966.878633 | source=vosk | rms=153 | updated_at=1787913964.943155 | frequency_hz=264.0
- [2026-08-28 18:46:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913967.9520023 | source=vosk | rms=153 | updated_at=1787913964.943155 | frequency_hz=264.0
- [2026-08-28 18:46:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913968.4437504 | source=vosk | rms=153 | updated_at=1787913964.943155 | frequency_hz=264.0
- [2026-08-28 18:46:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913968.942673 | source=vosk | rms=153 | updated_at=1787913964.943155 | frequency_hz=264.0
- [2026-08-28 18:46:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913971.45421 | source=vosk | rms=164 | updated_at=1787913971.45421 | frequency_hz=264.0
- [2026-08-28 18:46:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913971.9839718 | source=vosk | rms=164 | updated_at=1787913971.45421 | frequency_hz=264.0
- [2026-08-28 18:46:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913983.7039826 | source=vosk | rms=164 | updated_at=1787913971.45421 | frequency_hz=264.0
- [2026-08-28 18:46:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913984.4545453 | source=vosk | rms=164 | updated_at=1787913971.45421 | frequency_hz=264.0
- [2026-08-28 18:46:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913985.203765 | source=vosk | rms=181 | updated_at=1787913985.203765 | frequency_hz=264.0
- [2026-08-28 18:46:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913985.7040997 | source=vosk | rms=181 | updated_at=1787913985.203765 | frequency_hz=264.0
- [2026-08-28 18:46:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913987.2304287 | source=vosk | rms=181 | updated_at=1787913985.203765 | frequency_hz=264.0
- [2026-08-28 18:46:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913987.7041914 | source=vosk | rms=181 | updated_at=1787913985.203765 | frequency_hz=264.0
- [2026-08-28 18:46:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913988.9538388 | source=vosk | rms=181 | updated_at=1787913985.203765 | frequency_hz=264.0
- [2026-08-28 18:46:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913989.4534657 | source=vosk | rms=181 | updated_at=1787913985.203765 | frequency_hz=264.0
- [2026-08-28 18:46:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913991.4540286 | source=vosk | rms=181 | updated_at=1787913985.203765 | frequency_hz=264.0
- [2026-08-28 18:46:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913991.9699357 | source=vosk | rms=181 | updated_at=1787913985.203765 | frequency_hz=264.0
- [2026-08-28 18:46:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913997.2037706 | source=vosk | rms=181 | updated_at=1787913985.203765 | frequency_hz=264.0
- [2026-08-28 18:46:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913997.7039506 | source=vosk | rms=181 | updated_at=1787913985.203765 | frequency_hz=264.0
- [2026-08-28 18:47:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914024.8678057 | source=vosk | rms=181 | updated_at=1787913985.203765 | frequency_hz=264.0
- [2026-08-28 18:47:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914025.357066 | source=vosk | rms=181 | updated_at=1787913985.203765 | frequency_hz=264.0
- [2026-08-28 18:47:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914026.3555262 | source=vosk | rms=163 | updated_at=1787914026.3555262 | frequency_hz=264.0
- [2026-08-28 18:47:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914026.8551984 | source=vosk | rms=163 | updated_at=1787914026.3555262 | frequency_hz=264.0
- [2026-08-28 18:47:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914031.3752854 | source=vosk | rms=163 | updated_at=1787914026.3555262 | frequency_hz=264.0
- [2026-08-28 18:47:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914031.8751237 | source=vosk | rms=163 | updated_at=1787914026.3555262 | frequency_hz=264.0
- [2026-08-28 18:47:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914032.382365 | source=vosk | rms=163 | updated_at=1787914026.3555262 | frequency_hz=264.0
- [2026-08-28 18:47:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914039.1255126 | source=vosk | rms=136 | updated_at=1787914036.1252162 | frequency_hz=264.0
- [2026-08-28 18:47:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914046.8750384 | source=vosk | rms=212 | updated_at=1787914046.8750384 | frequency_hz=264.0
- [2026-08-28 18:47:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914047.3755558 | source=vosk | rms=212 | updated_at=1787914046.8750384 | frequency_hz=264.0
- [2026-08-28 18:47:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914048.1365879 | source=vosk | rms=212 | updated_at=1787914046.8750384 | frequency_hz=264.0
- [2026-08-28 18:47:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914048.635501 | source=vosk | rms=212 | updated_at=1787914046.8750384 | frequency_hz=264.0
- [2026-08-28 18:47:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914053.1358504 | source=vosk | rms=197 | updated_at=1787914053.1358504 | frequency_hz=264.0
- [2026-08-28 18:47:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914056.2070024 | source=vosk | rms=122 | updated_at=1787914054.956685 | frequency_hz=264.0
- [2026-08-28 18:47:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914057.2067065 | source=vosk | rms=303 | updated_at=1787914057.2067065 | frequency_hz=264.0
- [2026-08-28 18:47:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914058.705827 | source=vosk | rms=206 | updated_at=1787914057.4555733 | frequency_hz=264.0
- [2026-08-28 18:47:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914058.9688528 | source=vosk | rms=206 | updated_at=1787914057.4555733 | frequency_hz=264.0
- [2026-08-28 18:47:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914061.2622573 | source=vosk | rms=148 | updated_at=1787914060.4559917 | frequency_hz=264.0
- [2026-08-28 18:47:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914061.70528 | source=vosk | rms=148 | updated_at=1787914060.4559917 | frequency_hz=264.0
- [2026-08-28 18:47:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914062.229124 | source=vosk | rms=148 | updated_at=1787914060.4559917 | frequency_hz=264.0
- [2026-08-28 18:47:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914065.4562871 | source=vosk | rms=148 | updated_at=1787914060.4559917 | frequency_hz=264.0
- [2026-08-28 18:47:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914065.9554484 | source=vosk | rms=148 | updated_at=1787914060.4559917 | frequency_hz=264.0
- [2026-08-28 18:47:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914066.7057855 | source=vosk | rms=135 | updated_at=1787914066.7057855 | frequency_hz=264.0
- [2026-08-28 18:47:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914067.2055104 | source=vosk | rms=135 | updated_at=1787914066.7057855 | frequency_hz=264.0
- [2026-08-28 18:47:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914067.456102 | source=vosk | rms=189 | updated_at=1787914067.456102 | frequency_hz=264.0
- [2026-08-28 18:47:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914068.4555342 | source=vosk | rms=189 | updated_at=1787914067.456102 | frequency_hz=264.0
- [2026-08-28 18:47:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914070.9557111 | source=vosk | rms=207 | updated_at=1787914070.9557111 | frequency_hz=264.0
- [2026-08-28 18:47:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914071.455523 | source=vosk | rms=207 | updated_at=1787914070.9557111 | frequency_hz=264.0
- [2026-08-28 18:47:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914078.36559 | source=vosk | rms=207 | updated_at=1787914070.9557111 | frequency_hz=264.0
- [2026-08-28 18:47:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914078.866624 | source=vosk | rms=207 | updated_at=1787914070.9557111 | frequency_hz=264.0
- [2026-08-28 18:48:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914091.8812206 | source=vosk | rms=207 | updated_at=1787914070.9557111 | frequency_hz=264.0
- [2026-08-28 18:48:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914092.666859 | source=vosk | rms=207 | updated_at=1787914070.9557111 | frequency_hz=264.0
- [2026-08-28 18:48:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914096.6685748 | source=vosk | rms=207 | updated_at=1787914070.9557111 | frequency_hz=264.0
- [2026-08-28 18:48:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914097.1684873 | source=vosk | rms=207 | updated_at=1787914070.9557111 | frequency_hz=264.0
- [2026-08-28 18:48:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914097.418033 | source=vosk | rms=207 | updated_at=1787914070.9557111 | frequency_hz=264.0
- [2026-08-28 18:48:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914097.9181938 | source=vosk | rms=207 | updated_at=1787914070.9557111 | frequency_hz=264.0
- [2026-08-28 18:48:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914116.5762484 | source=vosk | rms=126 | updated_at=1787914116.5762484 | frequency_hz=236.0
- [2026-08-28 18:48:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914118.6052783 | source=vosk | rms=165 | updated_at=1787914118.1037202 | frequency_hz=262.8
- [2026-08-28 18:48:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914126.9650385 | source=vosk | rms=165 | updated_at=1787914118.1037202 | frequency_hz=262.8
- [2026-08-28 18:48:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914130.8277152 | source=vosk | rms=123 | updated_at=1787914129.7153723 | frequency_hz=101.2
- [2026-08-28 18:48:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914134.3476958 | source=vosk | rms=123 | updated_at=1787914129.7153723 | frequency_hz=101.2
- [2026-08-28 18:48:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914134.7995205 | source=vosk | rms=123 | updated_at=1787914129.7153723 | frequency_hz=101.2
- [2026-08-28 18:48:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914139.0978448 | source=vosk | rms=123 | updated_at=1787914129.7153723 | frequency_hz=101.2
- [2026-08-28 18:48:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914139.5977905 | source=vosk | rms=123 | updated_at=1787914129.7153723 | frequency_hz=101.2
- [2026-08-28 18:48:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914139.8475106 | source=vosk | rms=123 | updated_at=1787914129.7153723 | frequency_hz=101.2
- [2026-08-28 18:49:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914144.5980265 | source=vosk | rms=166 | updated_at=1787914140.097579 | frequency_hz=101.2
- [2026-08-28 18:49:34] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787914174.9438293 | source=vosk | rms=166 | updated_at=1787914140.097579 | frequency_hz=101.2
- [2026-08-28 18:49:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914193.287311 | source=vosk | rms=537 | updated_at=1787914193.287311 | frequency_hz=101.2
- [2026-08-28 18:49:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914196.0473733 | source=vosk | rms=205 | updated_at=1787914195.2870271 | frequency_hz=101.2
- [2026-08-28 18:49:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914198.3211105 | source=vosk | rms=205 | updated_at=1787914195.2870271 | frequency_hz=101.2
- [2026-08-28 18:49:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914198.8203216 | source=vosk | rms=205 | updated_at=1787914195.2870271 | frequency_hz=101.2
- [2026-08-28 18:49:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914199.0742147 | source=vosk | rms=205 | updated_at=1787914195.2870271 | frequency_hz=101.2
- [2026-08-28 18:50:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914200.4058142 | source=vosk | rms=205 | updated_at=1787914195.2870271 | frequency_hz=101.2
- [2026-08-28 18:50:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914207.1598535 | source=vosk | rms=207 | updated_at=1787914207.1598535 | frequency_hz=101.2
- [2026-08-28 18:50:09] operator / voice_transcript_final / voice: that
  meta: kind=final | timestamp=1787914209.1129332 | source=final | rms=132 | updated_at=1787914208.9035075 | frequency_hz=101.2
- [2026-08-28 18:50:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914209.155014 | source=vosk | rms=141 | updated_at=1787914209.155014 | frequency_hz=101.2
- [2026-08-28 18:50:14] operator / voice_transcript_partial / voice: and i
  meta: kind=partial | timestamp=1787914214.8236203 | source=vosk | rms=797 | updated_at=1787914214.5538135 | frequency_hz=101.2
- [2026-08-28 18:50:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914215.352823 | source=vosk | rms=797 | updated_at=1787914214.5538135 | frequency_hz=101.2
- [2026-08-28 18:50:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914216.8860254 | source=vosk | rms=797 | updated_at=1787914214.5538135 | frequency_hz=101.2
- [2026-08-28 18:50:17] operator / voice_transcript_final / voice: and now
  meta: kind=final | timestamp=1787914217.1556714 | source=final | rms=797 | updated_at=1787914214.5538135 | frequency_hz=101.2
- [2026-08-28 18:50:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914217.384776 | source=vosk | rms=465 | updated_at=1787914217.384776 | frequency_hz=101.2
- [2026-08-28 18:50:19] operator / voice_transcript_partial / voice: and i
  meta: kind=partial | timestamp=1787914219.4024434 | source=vosk | rms=517 | updated_at=1787914219.385424 | frequency_hz=101.2
- [2026-08-28 18:50:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914219.9020112 | source=vosk | rms=517 | updated_at=1787914219.385424 | frequency_hz=101.2
- [2026-08-28 18:50:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914220.1351678 | source=vosk | rms=902 | updated_at=1787914220.1351678 | frequency_hz=101.2
- [2026-08-28 18:50:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914220.3916106 | source=vosk | rms=965 | updated_at=1787914220.3916106 | frequency_hz=101.2
- [2026-08-28 18:50:20] operator / voice_transcript_partial / voice: and i am at
  meta: kind=partial | timestamp=1787914220.4332933 | source=vosk | rms=965 | updated_at=1787914220.3916106 | frequency_hz=101.2
- [2026-08-28 18:50:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914220.6352382 | source=vosk | rms=885 | updated_at=1787914220.6352382 | frequency_hz=101.2
- [2026-08-28 18:50:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914221.1367218 | source=vosk | rms=885 | updated_at=1787914220.6352382 | frequency_hz=101.2
- [2026-08-28 18:50:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914221.3858943 | source=vosk | rms=1076 | updated_at=1787914221.3858943 | frequency_hz=101.2
- [2026-08-28 18:50:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914221.8859756 | source=vosk | rms=1076 | updated_at=1787914221.3858943 | frequency_hz=101.2
- [2026-08-28 18:50:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914222.1357737 | source=vosk | rms=1205 | updated_at=1787914222.1357737 | frequency_hz=101.2
- [2026-08-28 18:50:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914222.697144 | source=vosk | rms=1206 | updated_at=1787914222.697144 | frequency_hz=101.2
- [2026-08-28 18:50:22] operator / voice_transcript_partial / voice: anti
  meta: kind=partial | timestamp=1787914222.742395 | source=vosk | rms=1206 | updated_at=1787914222.697144 | frequency_hz=101.2
- [2026-08-28 18:50:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914223.1958704 | source=vosk | rms=1206 | updated_at=1787914222.697144 | frequency_hz=101.2
- [2026-08-28 18:50:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914224.4455357 | source=vosk | rms=930 | updated_at=1787914224.4455357 | frequency_hz=101.2
- [2026-08-28 18:50:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914224.7317486 | source=vosk | rms=956 | updated_at=1787914224.7317486 | frequency_hz=101.2
- [2026-08-28 18:50:25] operator / voice_transcript_final / voice: and i at at
  meta: kind=final | timestamp=1787914225.0808637 | source=final | rms=956 | updated_at=1787914224.7317486 | frequency_hz=101.2
- [2026-08-28 18:50:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914225.2308538 | source=vosk | rms=956 | updated_at=1787914224.7317486 | frequency_hz=101.2
- [2026-08-28 18:50:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914225.2308538 | source=vosk | rms=978 | updated_at=1787914225.2308538 | frequency_hz=101.2
- [2026-08-28 18:50:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914226.764384 | source=vosk | rms=644 | updated_at=1787914226.256046 | frequency_hz=101.2
- [2026-08-28 18:50:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914227.505576 | source=vosk | rms=1069 | updated_at=1787914227.505576 | frequency_hz=101.2
- [2026-08-28 18:50:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914228.0057523 | source=vosk | rms=1069 | updated_at=1787914227.505576 | frequency_hz=101.2
- [2026-08-28 18:50:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914230.053889 | source=vosk | rms=937 | updated_at=1787914230.053889 | frequency_hz=101.2
- [2026-08-28 18:50:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914230.8127012 | source=vosk | rms=937 | updated_at=1787914230.053889 | frequency_hz=101.2
- [2026-08-28 18:50:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914232.057155 | source=vosk | rms=1082 | updated_at=1787914232.057155 | frequency_hz=101.2
- [2026-08-28 18:50:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914233.054456 | source=vosk | rms=844 | updated_at=1787914232.554115 | frequency_hz=101.2
- [2026-08-28 18:50:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914233.5535228 | source=vosk | rms=786 | updated_at=1787914233.5535228 | frequency_hz=101.2
- [2026-08-28 18:50:33] operator / voice_transcript_partial / voice: at
  meta: kind=partial | timestamp=1787914233.5691855 | source=vosk | rms=786 | updated_at=1787914233.5535228 | frequency_hz=101.2
- [2026-08-28 18:50:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914233.8042357 | source=vosk | rms=299 | updated_at=1787914233.8042357 | frequency_hz=101.2
- [2026-08-28 18:50:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914234.3035057 | source=vosk | rms=299 | updated_at=1787914233.8042357 | frequency_hz=101.2
- [2026-08-28 18:50:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914235.0538745 | source=vosk | rms=812 | updated_at=1787914235.0538745 | frequency_hz=101.2
- [2026-08-28 18:50:35] operator / voice_transcript_partial / voice: at at
  meta: kind=partial | timestamp=1787914235.0705435 | source=vosk | rms=812 | updated_at=1787914235.0538745 | frequency_hz=101.2
- [2026-08-28 18:50:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914235.5541103 | source=vosk | rms=812 | updated_at=1787914235.0538745 | frequency_hz=101.2
- [2026-08-28 18:50:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914235.807449 | source=vosk | rms=1131 | updated_at=1787914235.807449 | frequency_hz=101.2
- [2026-08-28 18:50:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914236.0535936 | source=vosk | rms=1131 | updated_at=1787914235.807449 | frequency_hz=101.2
- [2026-08-28 18:50:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914236.5538328 | source=vosk | rms=1027 | updated_at=1787914236.5538328 | frequency_hz=101.2
- [2026-08-28 18:50:36] operator / voice_transcript_final / voice: at at a pet
  meta: kind=final | timestamp=1787914236.8363705 | source=final | rms=1027 | updated_at=1787914236.5538328 | frequency_hz=101.2
- [2026-08-28 18:50:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914236.9452577 | source=vosk | rms=384 | updated_at=1787914236.9452577 | frequency_hz=101.2
- [2026-08-28 18:50:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914237.4337447 | source=vosk | rms=384 | updated_at=1787914236.9452577 | frequency_hz=101.2
- [2026-08-28 18:50:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914238.196089 | source=vosk | rms=348 | updated_at=1787914238.196089 | frequency_hz=101.2
- [2026-08-28 18:50:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914238.695962 | source=vosk | rms=348 | updated_at=1787914238.196089 | frequency_hz=101.2
- [2026-08-28 18:50:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914239.6959968 | source=vosk | rms=807 | updated_at=1787914239.6959968 | frequency_hz=101.2
- [2026-08-28 18:50:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914240.4458444 | source=vosk | rms=840 | updated_at=1787914239.946454 | frequency_hz=101.2
- [2026-08-28 18:50:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914241.2034326 | source=vosk | rms=322 | updated_at=1787914241.2034326 | frequency_hz=101.2
- [2026-08-28 18:50:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914241.946383 | source=vosk | rms=969 | updated_at=1787914241.4461093 | frequency_hz=101.2
- [2026-08-28 18:50:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914242.1960366 | source=vosk | rms=1058 | updated_at=1787914242.1960366 | frequency_hz=101.2
- [2026-08-28 18:50:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914243.1978927 | source=vosk | rms=345 | updated_at=1787914242.696456 | frequency_hz=101.2
- [2026-08-28 18:50:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914243.9738421 | source=vosk | rms=881 | updated_at=1787914243.9738421 | frequency_hz=101.2
- [2026-08-28 18:50:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914244.4506397 | source=vosk | rms=881 | updated_at=1787914243.9738421 | frequency_hz=101.2
- [2026-08-28 18:50:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914244.6971688 | source=vosk | rms=752 | updated_at=1787914244.6971688 | frequency_hz=101.2
- [2026-08-28 18:50:45] operator / voice_transcript_partial / voice: have had pet
  meta: kind=partial | timestamp=1787914245.4643426 | source=vosk | rms=352 | updated_at=1787914245.4462516 | frequency_hz=101.2
- [2026-08-28 18:50:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914245.9456375 | source=vosk | rms=352 | updated_at=1787914245.4462516 | frequency_hz=101.2
- [2026-08-28 18:50:47] operator / voice_transcript_final / voice: have had pet
  meta: kind=final | timestamp=1787914247.4883735 | source=final | rms=403 | updated_at=1787914246.9464872 | frequency_hz=101.2
- [2026-08-28 18:50:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914248.4386222 | source=vosk | rms=403 | updated_at=1787914246.9464872 | frequency_hz=101.2
- [2026-08-28 18:50:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914248.4386222 | source=vosk | rms=719 | updated_at=1787914248.4386222 | frequency_hz=101.2
- [2026-08-28 18:50:50] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1787914250.4885256 | source=vosk | rms=472 | updated_at=1787914250.447242 | frequency_hz=101.2
- [2026-08-28 18:50:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914250.697283 | source=vosk | rms=765 | updated_at=1787914250.697283 | frequency_hz=101.2
- [2026-08-28 18:50:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914250.9460042 | source=vosk | rms=632 | updated_at=1787914250.9460042 | frequency_hz=101.2
- [2026-08-28 18:50:51] operator / voice_transcript_final / voice: and perhaps
  meta: kind=final | timestamp=1787914251.142496 | source=final | rms=632 | updated_at=1787914250.9460042 | frequency_hz=101.2
- [2026-08-28 18:50:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914251.2314506 | source=vosk | rms=632 | updated_at=1787914250.9460042 | frequency_hz=101.2
- [2026-08-28 18:50:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914252.9466732 | source=vosk | rms=939 | updated_at=1787914252.4458108 | frequency_hz=101.2
- [2026-08-28 18:50:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914253.9594245 | source=vosk | rms=707 | updated_at=1787914253.9594245 | frequency_hz=101.2
- [2026-08-28 18:50:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914254.6964676 | source=vosk | rms=707 | updated_at=1787914253.9594245 | frequency_hz=101.2
- [2026-08-28 18:50:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914255.19577 | source=vosk | rms=841 | updated_at=1787914255.19577 | frequency_hz=101.2
- [2026-08-28 18:50:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914256.2613077 | source=vosk | rms=950 | updated_at=1787914255.4464128 | frequency_hz=101.2
- [2026-08-28 18:50:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914256.5139565 | source=vosk | rms=408 | updated_at=1787914256.5139565 | frequency_hz=147.0
- [2026-08-28 18:50:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914257.0145023 | source=vosk | rms=408 | updated_at=1787914256.5139565 | frequency_hz=147.0
- [2026-08-28 18:50:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914257.7647488 | source=vosk | rms=706 | updated_at=1787914257.7647488 | frequency_hz=147.0
- [2026-08-28 18:50:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914258.514332 | source=vosk | rms=547 | updated_at=1787914258.0147862 | frequency_hz=147.0
- [2026-08-28 18:51:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914260.0908654 | source=vosk | rms=547 | updated_at=1787914258.0147862 | frequency_hz=147.0
- [2026-08-28 18:51:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914260.5906198 | source=vosk | rms=547 | updated_at=1787914258.0147862 | frequency_hz=147.0
- [2026-08-28 18:51:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914263.8629045 | source=vosk | rms=1203 | updated_at=1787914263.8629045 | frequency_hz=147.0
- [2026-08-28 18:51:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914264.6107745 | source=vosk | rms=1203 | updated_at=1787914263.8629045 | frequency_hz=147.0
- [2026-08-28 18:51:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914273.9366515 | source=vosk | rms=847 | updated_at=1787914273.9366515 | frequency_hz=147.0
- [2026-08-28 18:51:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914275.4363606 | source=vosk | rms=753 | updated_at=1787914274.9363015 | frequency_hz=147.0
- [2026-08-28 18:51:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914275.936542 | source=vosk | rms=768 | updated_at=1787914275.936542 | frequency_hz=147.0
- [2026-08-28 18:51:16] operator / voice_transcript_final / voice: that
  meta: kind=final | timestamp=1787914276.1764975 | source=final | rms=768 | updated_at=1787914275.936542 | frequency_hz=147.0
- [2026-08-28 18:51:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914276.9103177 | source=vosk | rms=768 | updated_at=1787914275.936542 | frequency_hz=147.0
- [2026-08-28 18:51:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914276.9103177 | source=vosk | rms=324 | updated_at=1787914276.9103177 | frequency_hz=147.0
- [2026-08-28 18:51:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914277.4367907 | source=vosk | rms=324 | updated_at=1787914276.9103177 | frequency_hz=147.0
- [2026-08-28 18:51:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914280.2134397 | source=vosk | rms=962 | updated_at=1787914280.2134397 | frequency_hz=147.0
- [2026-08-28 18:51:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914280.714006 | source=vosk | rms=962 | updated_at=1787914280.2134397 | frequency_hz=147.0
- [2026-08-28 18:51:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914282.7141435 | source=vosk | rms=962 | updated_at=1787914280.2134397 | frequency_hz=147.0
- [2026-08-28 18:51:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914283.7144186 | source=vosk | rms=962 | updated_at=1787914280.2134397 | frequency_hz=147.0
- [2026-08-28 18:51:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914288.883265 | source=vosk | rms=962 | updated_at=1787914280.2134397 | frequency_hz=147.0
- [2026-08-28 18:51:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914289.3832183 | source=vosk | rms=962 | updated_at=1787914280.2134397 | frequency_hz=147.0
- [2026-08-28 18:51:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914289.633135 | source=vosk | rms=962 | updated_at=1787914280.2134397 | frequency_hz=147.0
- [2026-08-28 18:51:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914290.3419845 | source=vosk | rms=962 | updated_at=1787914280.2134397 | frequency_hz=147.0
- [2026-08-28 18:51:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914290.6330953 | source=vosk | rms=413 | updated_at=1787914290.6330953 | frequency_hz=147.0
- [2026-08-28 18:51:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914291.4007456 | source=vosk | rms=432 | updated_at=1787914290.8831728 | frequency_hz=147.0
- [2026-08-28 18:51:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914291.643151 | source=vosk | rms=1078 | updated_at=1787914291.643151 | frequency_hz=147.0
- [2026-08-28 18:51:32] operator / voice_transcript_partial / voice: that's
  meta: kind=partial | timestamp=1787914292.6917708 | source=vosk | rms=157 | updated_at=1787914292.404586 | frequency_hz=147.0
- [2026-08-28 18:51:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914293.1428978 | source=vosk | rms=157 | updated_at=1787914292.404586 | frequency_hz=147.0
- [2026-08-28 18:51:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914295.9134922 | source=vosk | rms=157 | updated_at=1787914292.404586 | frequency_hz=147.0
- [2026-08-28 18:51:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914296.4135373 | source=vosk | rms=157 | updated_at=1787914292.404586 | frequency_hz=147.0
- [2026-08-28 18:51:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914308.8089623 | source=vosk | rms=130 | updated_at=1787914308.8089623 | frequency_hz=147.0
- [2026-08-28 18:51:49] operator / voice_transcript_final / voice: had pets
  meta: kind=final | timestamp=1787914309.468642 | source=final | rms=130 | updated_at=1787914308.8089623 | frequency_hz=147.0
- [2026-08-28 18:51:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914309.5006924 | source=vosk | rms=130 | updated_at=1787914308.8089623 | frequency_hz=147.0
- [2026-08-28 18:51:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914309.5006924 | source=vosk | rms=130 | updated_at=1787914308.8089623 | frequency_hz=147.0
- [2026-08-28 18:51:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914310.0480406 | source=vosk | rms=130 | updated_at=1787914308.8089623 | frequency_hz=147.0
- [2026-08-28 18:51:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914310.7976947 | source=vosk | rms=130 | updated_at=1787914308.8089623 | frequency_hz=147.0
- [2026-08-28 18:51:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914311.7981188 | source=vosk | rms=130 | updated_at=1787914308.8089623 | frequency_hz=147.0
- [2026-08-28 18:51:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914315.0472946 | source=vosk | rms=130 | updated_at=1787914308.8089623 | frequency_hz=147.0
- [2026-08-28 18:51:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914317.0478098 | source=vosk | rms=169 | updated_at=1787914316.0480177 | frequency_hz=147.0
- [2026-08-28 18:52:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914323.1898124 | source=vosk | rms=188 | updated_at=1787914323.1898124 | frequency_hz=147.0
- [2026-08-28 18:52:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914324.1847506 | source=vosk | rms=268 | updated_at=1787914323.68234 | frequency_hz=147.0
- [2026-08-28 18:52:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914324.4317179 | source=vosk | rms=279 | updated_at=1787914324.4317179 | frequency_hz=147.0
- [2026-08-28 18:52:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914325.1233094 | source=vosk | rms=279 | updated_at=1787914324.4317179 | frequency_hz=147.0
- [2026-08-28 18:52:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914325.6815145 | source=vosk | rms=279 | updated_at=1787914324.4317179 | frequency_hz=147.0
- [2026-08-28 18:52:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914326.1819763 | source=vosk | rms=279 | updated_at=1787914324.4317179 | frequency_hz=147.0
- [2026-08-28 18:52:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914334.1465373 | source=vosk | rms=122 | updated_at=1787914334.1465373 | frequency_hz=147.0
- [2026-08-28 18:52:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914347.186326 | source=vosk | rms=132 | updated_at=1787914346.683361 | frequency_hz=229.2
- [2026-08-28 18:52:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914360.1080673 | source=vosk | rms=132 | updated_at=1787914346.683361 | frequency_hz=229.2
- [2026-08-28 18:52:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914360.5706148 | source=vosk | rms=132 | updated_at=1787914346.683361 | frequency_hz=229.2
- [2026-08-28 18:52:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914364.320454 | source=vosk | rms=127 | updated_at=1787914364.320454 | frequency_hz=229.2
- [2026-08-28 18:52:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914364.829045 | source=vosk | rms=127 | updated_at=1787914364.320454 | frequency_hz=229.2
- [2026-08-28 18:52:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914366.3206875 | source=vosk | rms=127 | updated_at=1787914364.320454 | frequency_hz=229.2
- [2026-08-28 18:52:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914366.948566 | source=vosk | rms=127 | updated_at=1787914364.320454 | frequency_hz=229.2
- [2026-08-28 18:52:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914367.9410155 | source=vosk | rms=148 | updated_at=1787914367.9410155 | frequency_hz=229.2
- [2026-08-28 18:52:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914368.4031262 | source=vosk | rms=148 | updated_at=1787914367.9410155 | frequency_hz=229.2
- [2026-08-28 18:53:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914388.3649693 | source=vosk | rms=152 | updated_at=1787914388.3649693 | frequency_hz=229.2
- [2026-08-28 18:53:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914388.8651295 | source=vosk | rms=152 | updated_at=1787914388.3649693 | frequency_hz=229.2
- [2026-08-28 18:53:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914391.866777 | source=vosk | rms=152 | updated_at=1787914388.3649693 | frequency_hz=229.2
- [2026-08-28 18:53:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914392.3656852 | source=vosk | rms=152 | updated_at=1787914388.3649693 | frequency_hz=229.2
- [2026-08-28 18:53:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914393.115833 | source=vosk | rms=152 | updated_at=1787914388.3649693 | frequency_hz=229.2
- [2026-08-28 18:53:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914393.8659794 | source=vosk | rms=152 | updated_at=1787914388.3649693 | frequency_hz=229.2
- [2026-08-28 18:53:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914395.365276 | source=vosk | rms=178 | updated_at=1787914395.365276 | frequency_hz=229.2
- [2026-08-28 18:53:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914398.775859 | source=vosk | rms=178 | updated_at=1787914395.365276 | frequency_hz=229.2
- [2026-08-28 18:53:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914405.5434844 | source=vosk | rms=178 | updated_at=1787914395.365276 | frequency_hz=229.2
- [2026-08-28 18:53:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914406.5442855 | source=vosk | rms=178 | updated_at=1787914395.365276 | frequency_hz=229.2
- [2026-08-28 18:53:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914427.4548855 | source=vosk | rms=178 | updated_at=1787914395.365276 | frequency_hz=229.2
- [2026-08-28 18:53:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914427.95487 | source=vosk | rms=178 | updated_at=1787914395.365276 | frequency_hz=229.2
- [2026-08-28 18:53:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914433.208103 | source=vosk | rms=178 | updated_at=1787914395.365276 | frequency_hz=229.2
- [2026-08-28 18:53:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914433.7056642 | source=vosk | rms=178 | updated_at=1787914395.365276 | frequency_hz=229.2
- [2026-08-28 18:53:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914434.955152 | source=vosk | rms=178 | updated_at=1787914395.365276 | frequency_hz=229.2
- [2026-08-28 18:53:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914438.2037454 | source=vosk | rms=178 | updated_at=1787914395.365276 | frequency_hz=229.2
- [2026-08-28 18:53:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914438.4553292 | source=vosk | rms=178 | updated_at=1787914395.365276 | frequency_hz=229.2
- [2026-08-28 18:53:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914439.7133687 | source=vosk | rms=178 | updated_at=1787914395.365276 | frequency_hz=229.2
- [2026-08-28 18:53:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914439.9552681 | source=vosk | rms=178 | updated_at=1787914395.365276 | frequency_hz=229.2
- [2026-08-28 18:54:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914447.2050326 | source=vosk | rms=144 | updated_at=1787914442.9554505 | frequency_hz=229.2
- [2026-08-28 18:54:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914447.462607 | source=vosk | rms=144 | updated_at=1787914442.9554505 | frequency_hz=229.2
- [2026-08-28 18:54:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914448.2052083 | source=vosk | rms=144 | updated_at=1787914442.9554505 | frequency_hz=229.2
- [2026-08-28 18:54:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914480.6139705 | source=vosk | rms=127 | updated_at=1787914480.6139705 | frequency_hz=229.2
- [2026-08-28 18:54:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914481.1118128 | source=vosk | rms=127 | updated_at=1787914480.6139705 | frequency_hz=229.2
- [2026-08-28 18:54:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914499.11228 | source=vosk | rms=127 | updated_at=1787914480.6139705 | frequency_hz=229.2
- [2026-08-28 18:54:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914499.6123924 | source=vosk | rms=127 | updated_at=1787914480.6139705 | frequency_hz=229.2
- [2026-08-28 18:55:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914517.13395 | source=vosk | rms=385 | updated_at=1787914517.13395 | frequency_hz=229.2
- [2026-08-28 18:55:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914520.6593306 | source=vosk | rms=331 | updated_at=1787914518.8847349 | frequency_hz=229.2
- [2026-08-28 18:55:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914522.4645832 | source=vosk | rms=197 | updated_at=1787914522.4645832 | frequency_hz=229.2
- [2026-08-28 18:55:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914525.6587048 | source=vosk | rms=121 | updated_at=1787914524.2145882 | frequency_hz=229.2
- [2026-08-28 18:55:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914526.9458606 | source=vosk | rms=171 | updated_at=1787914526.9458606 | frequency_hz=229.2
- [2026-08-28 18:55:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914527.517021 | source=vosk | rms=171 | updated_at=1787914526.9458606 | frequency_hz=229.2
- [2026-08-28 18:55:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914529.9665227 | source=vosk | rms=171 | updated_at=1787914526.9458606 | frequency_hz=229.2
- [2026-08-28 18:55:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914530.4691226 | source=vosk | rms=171 | updated_at=1787914526.9458606 | frequency_hz=229.2
- [2026-08-28 18:55:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914532.4849775 | source=vosk | rms=171 | updated_at=1787914526.9458606 | frequency_hz=229.2
- [2026-08-28 18:55:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914533.5115814 | source=vosk | rms=171 | updated_at=1787914526.9458606 | frequency_hz=229.2
- [2026-08-28 18:55:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914542.6447053 | source=vosk | rms=171 | updated_at=1787914526.9458606 | frequency_hz=229.2
- [2026-08-28 18:55:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914543.151917 | source=vosk | rms=171 | updated_at=1787914526.9458606 | frequency_hz=229.2
- [2026-08-28 18:56:03] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787914563.9859216 | source=vosk | rms=171 | updated_at=1787914526.9458606 | frequency_hz=229.2
- [2026-08-28 18:56:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914565.7301297 | source=vosk | rms=150 | updated_at=1787914565.7301297 | frequency_hz=358.0
- [2026-08-28 18:56:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914572.1634367 | source=vosk | rms=152 | updated_at=1787914568.2173734 | frequency_hz=126.2
- [2026-08-28 18:56:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914575.7087479 | source=vosk | rms=152 | updated_at=1787914568.2173734 | frequency_hz=126.2
- [2026-08-28 18:56:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914577.6915557 | source=vosk | rms=152 | updated_at=1787914568.2173734 | frequency_hz=126.2
- [2026-08-28 18:56:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914584.7856653 | source=vosk | rms=171 | updated_at=1787914584.7856653 | frequency_hz=126.2
- [2026-08-28 18:56:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914585.286307 | source=vosk | rms=171 | updated_at=1787914584.7856653 | frequency_hz=126.2
- [2026-08-28 18:56:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914586.7864664 | source=vosk | rms=171 | updated_at=1787914584.7856653 | frequency_hz=126.2
- [2026-08-28 18:56:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914587.2958102 | source=vosk | rms=171 | updated_at=1787914584.7856653 | frequency_hz=126.2
- [2026-08-28 18:56:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914588.5365043 | source=vosk | rms=171 | updated_at=1787914584.7856653 | frequency_hz=126.2
- [2026-08-28 18:56:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914589.5111065 | source=vosk | rms=171 | updated_at=1787914584.7856653 | frequency_hz=126.2
- [2026-08-28 18:56:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914594.552913 | source=vosk | rms=127 | updated_at=1787914594.552913 | frequency_hz=126.2
- [2026-08-28 18:56:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914595.053542 | source=vosk | rms=127 | updated_at=1787914594.552913 | frequency_hz=126.2
- [2026-08-28 18:56:56] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787914616.3461053 | source=vosk | rms=127 | updated_at=1787914594.552913 | frequency_hz=126.2
- [2026-08-28 18:57:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914644.1074479 | source=vosk | rms=169 | updated_at=1787914644.1074479 | frequency_hz=126.2
- [2026-08-28 18:57:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914644.6078346 | source=vosk | rms=169 | updated_at=1787914644.1074479 | frequency_hz=126.2
- [2026-08-28 18:57:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914645.6075513 | source=vosk | rms=169 | updated_at=1787914644.1074479 | frequency_hz=126.2
- [2026-08-28 18:57:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914646.1071281 | source=vosk | rms=169 | updated_at=1787914644.1074479 | frequency_hz=126.2
- [2026-08-28 18:57:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914649.1996512 | source=vosk | rms=120 | updated_at=1787914649.1996512 | frequency_hz=126.2
- [2026-08-28 18:57:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914649.6994135 | source=vosk | rms=120 | updated_at=1787914649.1996512 | frequency_hz=126.2
- [2026-08-28 18:57:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914650.1992197 | source=vosk | rms=120 | updated_at=1787914649.1996512 | frequency_hz=126.2
- [2026-08-28 18:57:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914651.7494707 | source=vosk | rms=228 | updated_at=1787914650.4486454 | frequency_hz=126.2
- [2026-08-28 18:57:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914651.999394 | source=vosk | rms=148 | updated_at=1787914651.999394 | frequency_hz=126.2
- [2026-08-28 18:57:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914654.0234153 | source=vosk | rms=167 | updated_at=1787914653.2489846 | frequency_hz=126.2
- [2026-08-28 18:57:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914654.7761629 | source=vosk | rms=167 | updated_at=1787914653.2489846 | frequency_hz=126.2
- [2026-08-28 18:57:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914655.2869084 | source=vosk | rms=167 | updated_at=1787914653.2489846 | frequency_hz=126.2
- [2026-08-28 18:57:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914662.5703163 | source=vosk | rms=226 | updated_at=1787914662.5703163 | frequency_hz=126.2
- [2026-08-28 18:57:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914663.6293662 | source=vosk | rms=226 | updated_at=1787914662.5703163 | frequency_hz=126.2
- [2026-08-28 18:57:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914668.4850962 | source=vosk | rms=150 | updated_at=1787914668.4850962 | frequency_hz=126.2
- [2026-08-28 18:57:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914669.6344817 | source=vosk | rms=150 | updated_at=1787914668.4850962 | frequency_hz=126.2
- [2026-08-28 18:58:11] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787914691.3575883 | source=vosk | rms=150 | updated_at=1787914668.4850962 | frequency_hz=126.2
- [2026-08-28 18:58:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914737.5980399 | source=vosk | rms=141 | updated_at=1787914737.5980399 | frequency_hz=126.2
- [2026-08-28 18:58:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914738.100954 | source=vosk | rms=141 | updated_at=1787914737.5980399 | frequency_hz=126.2
- [2026-08-28 18:59:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914757.6036103 | source=vosk | rms=149 | updated_at=1787914757.6036103 | frequency_hz=126.2
- [2026-08-28 18:59:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914758.098062 | source=vosk | rms=149 | updated_at=1787914757.6036103 | frequency_hz=126.2
- [2026-08-28 18:59:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914770.6088605 | source=vosk | rms=1200 | updated_at=1787914770.6088605 | frequency_hz=126.2
- [2026-08-28 18:59:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914771.358304 | source=vosk | rms=1200 | updated_at=1787914770.863619 | frequency_hz=126.2
- [2026-08-28 18:59:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914773.608705 | source=vosk | rms=1200 | updated_at=1787914770.863619 | frequency_hz=126.2
- [2026-08-28 18:59:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914774.108163 | source=vosk | rms=1200 | updated_at=1787914770.863619 | frequency_hz=126.2
- [2026-08-28 18:59:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914787.3988125 | source=vosk | rms=128 | updated_at=1787914787.3988125 | frequency_hz=126.2
- [2026-08-28 18:59:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914787.8990476 | source=vosk | rms=128 | updated_at=1787914787.3988125 | frequency_hz=126.2
- [2026-08-28 19:00:12] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787914812.27105 | source=vosk | rms=128 | updated_at=1787914787.3988125 | frequency_hz=126.2
- [2026-08-28 19:00:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914838.059963 | source=vosk | rms=479 | updated_at=1787914838.059963 | frequency_hz=126.2
- [2026-08-28 19:00:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914838.5632381 | source=vosk | rms=479 | updated_at=1787914838.059963 | frequency_hz=126.2
- [2026-08-28 19:00:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914850.0641723 | source=vosk | rms=1201 | updated_at=1787914850.0641723 | frequency_hz=126.2
- [2026-08-28 19:00:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914851.0633993 | source=vosk | rms=516 | updated_at=1787914850.5890262 | frequency_hz=126.2
- [2026-08-28 19:01:22] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787914882.5832028 | source=vosk | rms=516 | updated_at=1787914850.5890262 | frequency_hz=126.2
- [2026-08-28 19:02:58] system / voice_status / voice: mic_error
  meta: kind=status | timestamp=1787914978.8421319 | source=watchdog | rms=516 | updated_at=1787914850.5890262 | frequency_hz=126.2
- [2026-08-28 19:03:02] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787914982.4938376 | source=vosk
- [2026-08-28 19:03:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914984.770181 | source=vosk
- [2026-08-28 19:03:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914985.2435977 | source=vosk
- [2026-08-28 19:03:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914985.795835 | source=vosk | rms=960 | updated_at=1787914985.795835
- [2026-08-28 19:03:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914986.4937885 | source=vosk | rms=456 | updated_at=1787914985.9932384
- [2026-08-28 19:03:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787914990.99484 | source=vosk | rms=456 | updated_at=1787914985.9932384
- [2026-08-28 19:03:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787914991.4937592 | source=vosk | rms=456 | updated_at=1787914985.9932384
- [2026-08-28 19:03:35] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787915015.9884505 | source=vosk | rms=456 | updated_at=1787914985.9932384
- [2026-08-28 19:03:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915022.9943602 | source=vosk | rms=297 | updated_at=1787915022.9943602 | frequency_hz=342.0
- [2026-08-28 19:03:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915023.7457721 | source=vosk | rms=525 | updated_at=1787915023.244418 | frequency_hz=342.0
- [2026-08-28 19:03:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915024.9956036 | source=vosk | rms=262 | updated_at=1787915024.9956036 | frequency_hz=342.0
- [2026-08-28 19:03:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915025.7444081 | source=vosk | rms=262 | updated_at=1787915024.9956036 | frequency_hz=342.0
- [2026-08-28 19:03:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915026.4940917 | source=vosk | rms=126 | updated_at=1787915026.4940917 | frequency_hz=342.0
- [2026-08-28 19:03:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915027.2648463 | source=vosk | rms=126 | updated_at=1787915026.4940917 | frequency_hz=342.0
- [2026-08-28 19:03:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915029.2440252 | source=vosk | rms=126 | updated_at=1787915026.4940917 | frequency_hz=342.0
- [2026-08-28 19:03:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915030.4945545 | source=vosk | rms=340 | updated_at=1787915029.9955208 | frequency_hz=342.0
- [2026-08-28 19:03:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915037.2659771 | source=vosk | rms=945 | updated_at=1787915037.2654743 | frequency_hz=342.0
- [2026-08-28 19:03:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915039.995098 | source=vosk | rms=346 | updated_at=1787915039.2834008 | frequency_hz=342.0
- [2026-08-28 19:04:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915040.244583 | source=vosk | rms=346 | updated_at=1787915039.2834008 | frequency_hz=342.0
- [2026-08-28 19:04:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915045.4959154 | source=vosk | rms=204 | updated_at=1787915044.9956667 | frequency_hz=342.0
- [2026-08-28 19:04:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915045.7563782 | source=vosk | rms=131 | updated_at=1787915045.7563782 | frequency_hz=342.0
- [2026-08-28 19:04:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915047.7470572 | source=vosk | rms=301 | updated_at=1787915047.2471738 | frequency_hz=342.0
- [2026-08-28 19:04:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915054.495577 | source=vosk | rms=301 | updated_at=1787915047.2471738 | frequency_hz=342.0
- [2026-08-28 19:04:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915054.9964583 | source=vosk | rms=301 | updated_at=1787915047.2471738 | frequency_hz=342.0
- [2026-08-28 19:04:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915056.2447767 | source=vosk | rms=301 | updated_at=1787915047.2471738 | frequency_hz=342.0
- [2026-08-28 19:04:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915057.0018334 | source=vosk | rms=301 | updated_at=1787915047.2471738 | frequency_hz=342.0
- [2026-08-28 19:04:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915063.2457106 | source=vosk | rms=301 | updated_at=1787915047.2471738 | frequency_hz=342.0
- [2026-08-28 19:04:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915063.7575872 | source=vosk | rms=301 | updated_at=1787915047.2471738 | frequency_hz=342.0
- [2026-08-28 19:04:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915063.9956584 | source=vosk | rms=143 | updated_at=1787915063.9956584 | frequency_hz=342.0
- [2026-08-28 19:04:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915064.78766 | source=vosk | rms=143 | updated_at=1787915063.9956584 | frequency_hz=342.0
- [2026-08-28 19:04:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915070.7914822 | source=vosk | rms=148 | updated_at=1787915070.7914822 | frequency_hz=342.0
- [2026-08-28 19:04:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915076.3028636 | source=vosk | rms=202 | updated_at=1787915075.535732 | frequency_hz=342.0
- [2026-08-28 19:04:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915077.0433366 | source=vosk | rms=202 | updated_at=1787915075.535732 | frequency_hz=342.0
- [2026-08-28 19:04:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915079.2897632 | source=vosk | rms=139 | updated_at=1787915078.3350437 | frequency_hz=342.0
- [2026-08-28 19:04:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915079.535583 | source=vosk | rms=320 | updated_at=1787915079.535583 | frequency_hz=342.0
- [2026-08-28 19:04:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915080.8222067 | source=vosk | rms=297 | updated_at=1787915080.354947 | frequency_hz=342.0
- [2026-08-28 19:04:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915081.78975 | source=vosk | rms=297 | updated_at=1787915080.354947 | frequency_hz=342.0
- [2026-08-28 19:04:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915082.535969 | source=vosk | rms=297 | updated_at=1787915080.354947 | frequency_hz=342.0
- [2026-08-28 19:04:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915093.2859414 | source=vosk | rms=297 | updated_at=1787915080.354947 | frequency_hz=342.0
- [2026-08-28 19:04:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915093.7862585 | source=vosk | rms=297 | updated_at=1787915080.354947 | frequency_hz=342.0
- [2026-08-28 19:05:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915106.7867565 | source=vosk | rms=177 | updated_at=1787915106.7867565 | frequency_hz=342.0
- [2026-08-28 19:05:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915107.7866323 | source=vosk | rms=177 | updated_at=1787915106.7867565 | frequency_hz=342.0
- [2026-08-28 19:05:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915111.5392737 | source=vosk | rms=312 | updated_at=1787915111.5392737 | frequency_hz=342.0
- [2026-08-28 19:05:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915114.5374985 | source=vosk | rms=1015 | updated_at=1787915114.0618968 | frequency_hz=342.0
- [2026-08-28 19:05:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915118.7879415 | source=vosk | rms=1015 | updated_at=1787915114.0618968 | frequency_hz=342.0
- [2026-08-28 19:05:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915119.2870967 | source=vosk | rms=1015 | updated_at=1787915114.0618968 | frequency_hz=342.0
- [2026-08-28 19:05:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915121.0406659 | source=vosk | rms=132 | updated_at=1787915121.0406659 | frequency_hz=342.0
- [2026-08-28 19:05:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915121.7865 | source=vosk | rms=132 | updated_at=1787915121.0406659 | frequency_hz=342.0
- [2026-08-28 19:05:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915122.7987032 | source=vosk | rms=189 | updated_at=1787915122.7987032 | frequency_hz=342.0
- [2026-08-28 19:05:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915127.0463707 | source=vosk | rms=637 | updated_at=1787915125.036501 | frequency_hz=400.0
- [2026-08-28 19:05:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915127.5370467 | source=vosk | rms=637 | updated_at=1787915125.036501 | frequency_hz=400.0
- [2026-08-28 19:05:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915128.306631 | source=vosk | rms=637 | updated_at=1787915125.036501 | frequency_hz=400.0
- [2026-08-28 19:05:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915129.536968 | source=vosk | rms=135 | updated_at=1787915129.536968 | frequency_hz=400.0
- [2026-08-28 19:05:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915131.2872548 | source=vosk | rms=712 | updated_at=1787915130.7880664 | frequency_hz=400.0
- [2026-08-28 19:05:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915131.5369916 | source=vosk | rms=144 | updated_at=1787915131.5369916 | frequency_hz=400.0
- [2026-08-28 19:05:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915132.787162 | source=vosk | rms=144 | updated_at=1787915131.5369916 | frequency_hz=400.0
- [2026-08-28 19:05:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915141.3056948 | source=vosk | rms=144 | updated_at=1787915131.5369916 | frequency_hz=400.0
- [2026-08-28 19:05:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915141.7868097 | source=vosk | rms=144 | updated_at=1787915131.5369916 | frequency_hz=400.0
- [2026-08-28 19:05:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915142.568812 | source=vosk | rms=144 | updated_at=1787915131.5369916 | frequency_hz=400.0
- [2026-08-28 19:05:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915143.2872617 | source=vosk | rms=128 | updated_at=1787915142.7873588 | frequency_hz=400.0
- [2026-08-28 19:05:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915144.537374 | source=vosk | rms=128 | updated_at=1787915142.7873588 | frequency_hz=400.0
- [2026-08-28 19:05:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915145.5367897 | source=vosk | rms=128 | updated_at=1787915142.7873588 | frequency_hz=400.0
- [2026-08-28 19:05:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915145.7874906 | source=vosk | rms=128 | updated_at=1787915142.7873588 | frequency_hz=400.0
- [2026-08-28 19:05:56] operator / voice_transcript_final / voice: cash
  meta: kind=final | timestamp=1787915156.5006175 | source=final | rms=472 | updated_at=1787915156.2877154 | frequency_hz=400.0
- [2026-08-28 19:05:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915156.5378563 | source=vosk | rms=917 | updated_at=1787915156.5378563 | frequency_hz=400.0
- [2026-08-28 19:06:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915161.322391 | source=vosk | rms=932 | updated_at=1787915160.552362 | frequency_hz=400.0
- [2026-08-28 19:06:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915161.8329742 | source=vosk | rms=704 | updated_at=1787915161.8329742 | frequency_hz=400.0
- [2026-08-28 19:06:03] operator / voice_transcript_final / voice: hats
  meta: kind=final | timestamp=1787915163.755612 | source=final | rms=486 | updated_at=1787915163.351398 | frequency_hz=400.0
- [2026-08-28 19:06:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915163.833058 | source=vosk | rms=486 | updated_at=1787915163.351398 | frequency_hz=400.0
- [2026-08-28 19:06:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915164.083997 | source=vosk | rms=765 | updated_at=1787915164.083997 | frequency_hz=400.0
- [2026-08-28 19:06:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915165.3204522 | source=vosk | rms=916 | updated_at=1787915164.5704956 | frequency_hz=400.0
- [2026-08-28 19:06:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915166.3550174 | source=vosk | rms=938 | updated_at=1787915166.3550174 | frequency_hz=400.0
- [2026-08-28 19:06:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915167.068823 | source=vosk | rms=821 | updated_at=1787915166.5677977 | frequency_hz=400.0
- [2026-08-28 19:06:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915167.3188953 | source=vosk | rms=543 | updated_at=1787915167.3188953 | frequency_hz=400.0
- [2026-08-28 19:06:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915167.8238 | source=vosk | rms=543 | updated_at=1787915167.3188953 | frequency_hz=400.0
- [2026-08-28 19:06:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915168.5681365 | source=vosk | rms=1205 | updated_at=1787915168.5681365 | frequency_hz=400.0
- [2026-08-28 19:06:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915171.0973809 | source=vosk | rms=719 | updated_at=1787915170.5682135 | frequency_hz=400.0
- [2026-08-28 19:06:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915172.5678797 | source=vosk | rms=519 | updated_at=1787915172.5678797 | frequency_hz=400.0
- [2026-08-28 19:06:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915173.0858357 | source=vosk | rms=519 | updated_at=1787915172.5678797 | frequency_hz=400.0
- [2026-08-28 19:06:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915182.5683863 | source=vosk | rms=433 | updated_at=1787915182.5683863 | frequency_hz=400.0
- [2026-08-28 19:06:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915183.567571 | source=vosk | rms=433 | updated_at=1787915182.5683863 | frequency_hz=400.0
- [2026-08-28 19:06:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915188.8182063 | source=vosk | rms=185 | updated_at=1787915188.8182063 | frequency_hz=400.0
- [2026-08-28 19:06:29] operator / voice_transcript_final / voice: okay
  meta: kind=final | timestamp=1787915189.5828054 | source=final | rms=251 | updated_at=1787915189.3846173 | frequency_hz=400.0
- [2026-08-28 19:06:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915189.6142466 | source=vosk | rms=187 | updated_at=1787915189.6142466 | frequency_hz=400.0
- [2026-08-28 19:06:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915190.0747876 | source=vosk | rms=187 | updated_at=1787915189.6142466 | frequency_hz=400.0
- [2026-08-28 19:06:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915190.3246605 | source=vosk | rms=403 | updated_at=1787915190.3246605 | frequency_hz=400.0
- [2026-08-28 19:06:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915191.3213212 | source=vosk | rms=284 | updated_at=1787915190.8194847 | frequency_hz=400.0
- [2026-08-28 19:06:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915191.8180568 | source=vosk | rms=397 | updated_at=1787915191.8180568 | frequency_hz=400.0
- [2026-08-28 19:06:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915193.1563241 | source=vosk | rms=397 | updated_at=1787915191.8180568 | frequency_hz=400.0
- [2026-08-28 19:06:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915196.3985918 | source=vosk | rms=316 | updated_at=1787915196.3985918 | frequency_hz=400.0
- [2026-08-28 19:06:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915196.9035487 | source=vosk | rms=316 | updated_at=1787915196.3985918 | frequency_hz=400.0
- [2026-08-28 19:06:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915199.6486533 | source=vosk | rms=316 | updated_at=1787915196.3985918 | frequency_hz=400.0
- [2026-08-28 19:06:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915200.4081762 | source=vosk | rms=316 | updated_at=1787915196.3985918 | frequency_hz=400.0
- [2026-08-28 19:06:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915207.1498256 | source=vosk | rms=296 | updated_at=1787915207.1498256 | frequency_hz=400.0
- [2026-08-28 19:06:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915207.6489747 | source=vosk | rms=296 | updated_at=1787915207.1498256 | frequency_hz=400.0
- [2026-08-28 19:06:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915212.4005954 | source=vosk | rms=296 | updated_at=1787915207.1498256 | frequency_hz=400.0
- [2026-08-28 19:07:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915220.4252992 | source=vosk | rms=247 | updated_at=1787915219.9050107 | frequency_hz=400.0
- [2026-08-28 19:07:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915220.899451 | source=vosk | rms=809 | updated_at=1787915220.899451 | frequency_hz=400.0
- [2026-08-28 19:07:03] operator / voice_transcript_final / voice: six
  meta: kind=final | timestamp=1787915223.1070666 | source=final | rms=323 | updated_at=1787915222.902922 | frequency_hz=400.0
- [2026-08-28 19:07:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915223.3994176 | source=vosk | rms=323 | updated_at=1787915222.902922 | frequency_hz=400.0
- [2026-08-28 19:07:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915223.649028 | source=vosk | rms=122 | updated_at=1787915223.649028 | frequency_hz=400.0
- [2026-08-28 19:07:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915224.1485944 | source=vosk | rms=122 | updated_at=1787915223.649028 | frequency_hz=400.0
- [2026-08-28 19:07:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915224.9061928 | source=vosk | rms=136 | updated_at=1787915224.9061928 | frequency_hz=400.0
- [2026-08-28 19:07:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915225.398858 | source=vosk | rms=136 | updated_at=1787915224.9061928 | frequency_hz=400.0
- [2026-08-28 19:07:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915226.153652 | source=vosk | rms=232 | updated_at=1787915226.153652 | frequency_hz=400.0
- [2026-08-28 19:07:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915226.6487489 | source=vosk | rms=232 | updated_at=1787915226.153652 | frequency_hz=400.0
- [2026-08-28 19:07:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915227.1593587 | source=vosk | rms=554 | updated_at=1787915227.1593587 | frequency_hz=400.0
- [2026-08-28 19:07:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915227.8987355 | source=vosk | rms=568 | updated_at=1787915227.3988585 | frequency_hz=400.0
- [2026-08-28 19:07:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915229.4099767 | source=vosk | rms=405 | updated_at=1787915229.4099767 | frequency_hz=400.0
- [2026-08-28 19:07:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915231.905888 | source=vosk | rms=216 | updated_at=1787915230.9062672 | frequency_hz=400.0
- [2026-08-28 19:07:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915232.4493256 | source=vosk | rms=709 | updated_at=1787915232.4493256 | frequency_hz=400.0
- [2026-08-28 19:07:14] operator / voice_transcript_final / voice: ecuador
  meta: kind=final | timestamp=1787915234.425501 | source=final | rms=441 | updated_at=1787915234.1503925 | frequency_hz=400.0
- [2026-08-28 19:07:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915234.6669657 | source=vosk | rms=441 | updated_at=1787915234.1503925 | frequency_hz=400.0
- [2026-08-28 19:07:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915235.1498332 | source=vosk | rms=382 | updated_at=1787915235.1498332 | frequency_hz=400.0
- [2026-08-28 19:07:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915237.150455 | source=vosk | rms=231 | updated_at=1787915236.6551335 | frequency_hz=400.0
- [2026-08-28 19:07:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915238.152321 | source=vosk | rms=734 | updated_at=1787915238.152321 | frequency_hz=400.0
- [2026-08-28 19:07:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915240.3997877 | source=vosk | rms=228 | updated_at=1787915239.1492958 | frequency_hz=400.0
- [2026-08-28 19:07:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915241.4084508 | source=vosk | rms=805 | updated_at=1787915241.4084508 | frequency_hz=400.0
- [2026-08-28 19:07:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915242.155911 | source=vosk | rms=805 | updated_at=1787915241.4084508 | frequency_hz=400.0
- [2026-08-28 19:07:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915243.149808 | source=vosk | rms=779 | updated_at=1787915243.149808 | frequency_hz=400.0
- [2026-08-28 19:07:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915243.6516356 | source=vosk | rms=779 | updated_at=1787915243.149808 | frequency_hz=400.0
- [2026-08-28 19:07:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915244.899339 | source=vosk | rms=779 | updated_at=1787915243.149808 | frequency_hz=400.0
- [2026-08-28 19:07:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915245.403182 | source=vosk | rms=779 | updated_at=1787915243.149808 | frequency_hz=400.0
- [2026-08-28 19:07:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915245.6488814 | source=vosk | rms=421 | updated_at=1787915245.6488814 | frequency_hz=400.0
- [2026-08-28 19:07:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915246.650059 | source=vosk | rms=915 | updated_at=1787915246.1607625 | frequency_hz=400.0
- [2026-08-28 19:07:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915247.8995914 | source=vosk | rms=1207 | updated_at=1787915247.8995914 | frequency_hz=400.0
- [2026-08-28 19:07:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915248.3999152 | source=vosk | rms=1207 | updated_at=1787915247.8995914 | frequency_hz=400.0
- [2026-08-28 19:07:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915249.151602 | source=vosk | rms=856 | updated_at=1787915249.151602 | frequency_hz=400.0
- [2026-08-28 19:07:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915249.6498168 | source=vosk | rms=856 | updated_at=1787915249.151602 | frequency_hz=400.0
- [2026-08-28 19:07:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915250.1499224 | source=vosk | rms=1078 | updated_at=1787915250.1499224 | frequency_hz=400.0
- [2026-08-28 19:07:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915250.6500733 | source=vosk | rms=1078 | updated_at=1787915250.1499224 | frequency_hz=400.0
- [2026-08-28 19:07:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915250.8998363 | source=vosk | rms=706 | updated_at=1787915250.8998363 | frequency_hz=400.0
- [2026-08-28 19:07:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915251.8996682 | source=vosk | rms=1205 | updated_at=1787915251.399867 | frequency_hz=400.0
- [2026-08-28 19:07:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915252.65321 | source=vosk | rms=1205 | updated_at=1787915251.399867 | frequency_hz=400.0
- [2026-08-28 19:07:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915253.4018562 | source=vosk | rms=1205 | updated_at=1787915251.399867 | frequency_hz=400.0
- [2026-08-28 19:07:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915253.649429 | source=vosk | rms=1205 | updated_at=1787915251.399867 | frequency_hz=400.0
- [2026-08-28 19:07:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915254.9208467 | source=vosk | rms=478 | updated_at=1787915254.4006145 | frequency_hz=400.0
- [2026-08-28 19:07:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915255.1516924 | source=vosk | rms=478 | updated_at=1787915254.4006145 | frequency_hz=400.0
- [2026-08-28 19:07:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915256.649365 | source=vosk | rms=257 | updated_at=1787915256.1757565 | frequency_hz=400.0
- [2026-08-28 19:07:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915257.9272711 | source=vosk | rms=462 | updated_at=1787915257.9272711 | frequency_hz=400.0
- [2026-08-28 19:07:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915261.8997395 | source=vosk | rms=572 | updated_at=1787915261.4145718 | frequency_hz=400.0
- [2026-08-28 19:07:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915262.1497407 | source=vosk | rms=1088 | updated_at=1787915262.1497407 | frequency_hz=400.0
- [2026-08-28 19:07:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915263.3994973 | source=vosk | rms=1203 | updated_at=1787915262.6730382 | frequency_hz=400.0
- [2026-08-28 19:07:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915263.92747 | source=vosk | rms=1203 | updated_at=1787915262.6730382 | frequency_hz=400.0
- [2026-08-28 19:07:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915265.6501677 | source=vosk | rms=365 | updated_at=1787915264.6492693 | frequency_hz=400.0
- [2026-08-28 19:07:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915266.1690543 | source=vosk | rms=355 | updated_at=1787915266.1690543 | frequency_hz=400.0
- [2026-08-28 19:07:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915266.6496205 | source=vosk | rms=355 | updated_at=1787915266.1690543 | frequency_hz=400.0
- [2026-08-28 19:07:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915266.9007225 | source=vosk | rms=1206 | updated_at=1787915266.9007225 | frequency_hz=400.0
- [2026-08-28 19:07:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915267.4052918 | source=vosk | rms=1206 | updated_at=1787915266.9007225 | frequency_hz=400.0
- [2026-08-28 19:07:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915268.1623385 | source=vosk | rms=1202 | updated_at=1787915268.1623385 | frequency_hz=400.0
- [2026-08-28 19:07:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915268.925191 | source=vosk | rms=415 | updated_at=1787915268.40494 | frequency_hz=400.0
- [2026-08-28 19:07:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915269.400079 | source=vosk | rms=743 | updated_at=1787915269.400079 | frequency_hz=400.0
- [2026-08-28 19:07:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915270.1500542 | source=vosk | rms=743 | updated_at=1787915269.400079 | frequency_hz=400.0
- [2026-08-28 19:07:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915270.4010334 | source=vosk | rms=917 | updated_at=1787915270.4010334 | frequency_hz=400.0
- [2026-08-28 19:07:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915270.9200523 | source=vosk | rms=917 | updated_at=1787915270.4010334 | frequency_hz=400.0
- [2026-08-28 19:07:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915271.150658 | source=vosk | rms=917 | updated_at=1787915270.4010334 | frequency_hz=400.0
- [2026-08-28 19:07:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915272.6557186 | source=vosk | rms=339 | updated_at=1787915272.1499913 | frequency_hz=400.0
- [2026-08-28 19:07:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915274.9008243 | source=vosk | rms=744 | updated_at=1787915274.9008243 | frequency_hz=400.0
- [2026-08-28 19:07:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915275.400666 | source=vosk | rms=744 | updated_at=1787915274.9008243 | frequency_hz=400.0
- [2026-08-28 19:07:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915276.1507003 | source=vosk | rms=883 | updated_at=1787915276.1507003 | frequency_hz=400.0
- [2026-08-28 19:07:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915276.9032013 | source=vosk | rms=569 | updated_at=1787915276.4013042 | frequency_hz=400.0
- [2026-08-28 19:07:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915277.1510413 | source=vosk | rms=923 | updated_at=1787915277.1510413 | frequency_hz=400.0
- [2026-08-28 19:07:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915277.901418 | source=vosk | rms=923 | updated_at=1787915277.1510413 | frequency_hz=400.0
- [2026-08-28 19:07:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915278.9042714 | source=vosk | rms=834 | updated_at=1787915278.9042714 | frequency_hz=400.0
- [2026-08-28 19:07:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915279.4017942 | source=vosk | rms=834 | updated_at=1787915278.9042714 | frequency_hz=400.0
- [2026-08-28 19:07:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915279.6508963 | source=vosk | rms=1183 | updated_at=1787915279.6508963 | frequency_hz=400.0
- [2026-08-28 19:08:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915280.4007516 | source=vosk | rms=590 | updated_at=1787915279.9009042 | frequency_hz=400.0
- [2026-08-28 19:08:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915280.651941 | source=vosk | rms=1205 | updated_at=1787915280.651941 | frequency_hz=400.0
- [2026-08-28 19:08:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915281.900769 | source=vosk | rms=1206 | updated_at=1787915281.4007268 | frequency_hz=400.0
- [2026-08-28 19:08:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915282.6506774 | source=vosk | rms=1206 | updated_at=1787915281.4007268 | frequency_hz=400.0
- [2026-08-28 19:08:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915283.1741252 | source=vosk | rms=1206 | updated_at=1787915281.4007268 | frequency_hz=400.0
- [2026-08-28 19:08:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915283.65077 | source=vosk | rms=1206 | updated_at=1787915281.4007268 | frequency_hz=400.0
- [2026-08-28 19:08:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915284.1495218 | source=vosk | rms=1206 | updated_at=1787915281.4007268 | frequency_hz=400.0
- [2026-08-28 19:08:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915284.651065 | source=vosk | rms=1013 | updated_at=1787915284.651065 | frequency_hz=400.0
- [2026-08-28 19:08:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915285.4008756 | source=vosk | rms=1013 | updated_at=1787915284.651065 | frequency_hz=400.0
- [2026-08-28 19:08:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915285.6506708 | source=vosk | rms=440 | updated_at=1787915285.6506708 | frequency_hz=400.0
- [2026-08-28 19:08:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915286.1509898 | source=vosk | rms=440 | updated_at=1787915285.6506708 | frequency_hz=400.0
- [2026-08-28 19:08:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915286.659914 | source=vosk | rms=1079 | updated_at=1787915286.659914 | frequency_hz=400.0
- [2026-08-28 19:08:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915287.401238 | source=vosk | rms=1079 | updated_at=1787915286.659914 | frequency_hz=400.0
- [2026-08-28 19:08:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915289.401019 | source=vosk | rms=946 | updated_at=1787915289.401019 | frequency_hz=400.0
- [2026-08-28 19:08:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915290.155391 | source=vosk | rms=763 | updated_at=1787915289.6511102 | frequency_hz=400.0
- [2026-08-28 19:08:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915292.1507435 | source=vosk | rms=731 | updated_at=1787915292.1507435 | frequency_hz=400.0
- [2026-08-28 19:08:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915292.6530852 | source=vosk | rms=731 | updated_at=1787915292.1507435 | frequency_hz=400.0
- [2026-08-28 19:08:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915293.9031732 | source=vosk | rms=851 | updated_at=1787915293.9031732 | frequency_hz=400.0
- [2026-08-28 19:08:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915294.6510773 | source=vosk | rms=290 | updated_at=1787915294.150946 | frequency_hz=400.0
- [2026-08-28 19:08:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915296.4138517 | source=vosk | rms=667 | updated_at=1787915296.4138517 | frequency_hz=400.0
- [2026-08-28 19:08:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915297.158309 | source=vosk | rms=284 | updated_at=1787915296.6717956 | frequency_hz=400.0
- [2026-08-28 19:08:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915297.4174209 | source=vosk | rms=409 | updated_at=1787915297.4164207 | frequency_hz=400.0
- [2026-08-28 19:08:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915298.4206262 | source=vosk | rms=363 | updated_at=1787915297.9034874 | frequency_hz=400.0
- [2026-08-28 19:08:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915299.1803422 | source=vosk | rms=363 | updated_at=1787915297.9034874 | frequency_hz=400.0
- [2026-08-28 19:08:20] operator / voice_transcript_partial / voice: that's
  meta: kind=partial | timestamp=1787915300.4480987 | source=vosk | rms=1201 | updated_at=1787915300.402143 | frequency_hz=400.0
- [2026-08-28 19:08:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915300.654241 | source=vosk | rms=1200 | updated_at=1787915300.654241 | frequency_hz=400.0
- [2026-08-28 19:08:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915300.904508 | source=vosk | rms=1206 | updated_at=1787915300.904508 | frequency_hz=400.0
- [2026-08-28 19:08:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915301.1507611 | source=vosk | rms=1203 | updated_at=1787915301.1507611 | frequency_hz=400.0
- [2026-08-28 19:08:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915301.4019468 | source=vosk | rms=1206 | updated_at=1787915301.4019468 | frequency_hz=400.0
- [2026-08-28 19:08:21] operator / voice_transcript_final / voice: acts
  meta: kind=final | timestamp=1787915301.6530218 | source=final | rms=1206 | updated_at=1787915301.4019468 | frequency_hz=400.0
- [2026-08-28 19:08:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915301.6833127 | source=vosk | rms=1202 | updated_at=1787915301.6833127 | frequency_hz=400.0
- [2026-08-28 19:08:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915302.4141037 | source=vosk | rms=1201 | updated_at=1787915301.9154816 | frequency_hz=400.0
- [2026-08-28 19:08:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915303.4020817 | source=vosk | rms=740 | updated_at=1787915303.400925 | frequency_hz=400.0
- [2026-08-28 19:08:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915304.4008124 | source=vosk | rms=389 | updated_at=1787915303.9009721 | frequency_hz=400.0
- [2026-08-28 19:08:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915305.1515718 | source=vosk | rms=631 | updated_at=1787915305.1515718 | frequency_hz=400.0
- [2026-08-28 19:08:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915305.6515038 | source=vosk | rms=631 | updated_at=1787915305.1515718 | frequency_hz=400.0
- [2026-08-28 19:08:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915306.6661584 | source=vosk | rms=726 | updated_at=1787915306.6661584 | frequency_hz=400.0
- [2026-08-28 19:08:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915308.1515765 | source=vosk | rms=261 | updated_at=1787915307.6514816 | frequency_hz=400.0
- [2026-08-28 19:08:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915308.402266 | source=vosk | rms=261 | updated_at=1787915307.6514816 | frequency_hz=400.0
- [2026-08-28 19:08:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915308.9031925 | source=vosk | rms=261 | updated_at=1787915307.6514816 | frequency_hz=400.0
- [2026-08-28 19:08:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915309.4102843 | source=vosk | rms=261 | updated_at=1787915307.6514816 | frequency_hz=400.0
- [2026-08-28 19:08:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915310.1525562 | source=vosk | rms=261 | updated_at=1787915307.6514816 | frequency_hz=400.0
- [2026-08-28 19:08:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915310.4135795 | source=vosk | rms=1202 | updated_at=1787915310.4135795 | frequency_hz=400.0
- [2026-08-28 19:08:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915311.1506581 | source=vosk | rms=433 | updated_at=1787915310.652139 | frequency_hz=400.0
- [2026-08-28 19:08:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915311.4008842 | source=vosk | rms=213 | updated_at=1787915311.4008842 | frequency_hz=400.0
- [2026-08-28 19:08:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915312.4345875 | source=vosk | rms=1201 | updated_at=1787915311.9156334 | frequency_hz=400.0
- [2026-08-28 19:08:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915313.4010093 | source=vosk | rms=1201 | updated_at=1787915311.9156334 | frequency_hz=400.0
- [2026-08-28 19:08:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915317.150794 | source=vosk | rms=1069 | updated_at=1787915316.4009154 | frequency_hz=400.0
- [2026-08-28 19:08:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915318.1754718 | source=vosk | rms=1069 | updated_at=1787915316.4009154 | frequency_hz=400.0
- [2026-08-28 19:08:40] operator / voice_transcript_final / voice: to happen
  meta: kind=final | timestamp=1787915320.3796864 | source=final | rms=575 | updated_at=1787915320.1523259 | frequency_hz=400.0
- [2026-08-28 19:08:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915320.4493308 | source=vosk | rms=1200 | updated_at=1787915320.4493308 | frequency_hz=400.0
- [2026-08-28 19:08:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915321.651681 | source=vosk | rms=362 | updated_at=1787915321.1548083 | frequency_hz=400.0
- [2026-08-28 19:08:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915321.9018865 | source=vosk | rms=362 | updated_at=1787915321.1548083 | frequency_hz=400.0
- [2026-08-28 19:08:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915322.9114716 | source=vosk | rms=446 | updated_at=1787915322.4027328 | frequency_hz=400.0
- [2026-08-28 19:08:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915324.6763034 | source=vosk | rms=1156 | updated_at=1787915324.6763034 | frequency_hz=400.0
- [2026-08-28 19:08:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915325.401773 | source=vosk | rms=808 | updated_at=1787915324.9011774 | frequency_hz=400.0
- [2026-08-28 19:08:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915326.1509743 | source=vosk | rms=808 | updated_at=1787915324.9011774 | frequency_hz=400.0
- [2026-08-28 19:08:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915326.651773 | source=vosk | rms=808 | updated_at=1787915324.9011774 | frequency_hz=400.0
- [2026-08-28 19:08:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915327.4018784 | source=vosk | rms=808 | updated_at=1787915324.9011774 | frequency_hz=400.0
- [2026-08-28 19:08:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915329.4017134 | source=vosk | rms=673 | updated_at=1787915328.4019356 | frequency_hz=400.0
- [2026-08-28 19:08:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915330.658049 | source=vosk | rms=673 | updated_at=1787915328.4019356 | frequency_hz=400.0
- [2026-08-28 19:08:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915331.9018078 | source=vosk | rms=498 | updated_at=1787915331.4214914 | frequency_hz=400.0
- [2026-08-28 19:08:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915332.168313 | source=vosk | rms=498 | updated_at=1787915331.4214914 | frequency_hz=400.0
- [2026-08-28 19:08:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915332.6518567 | source=vosk | rms=498 | updated_at=1787915331.4214914 | frequency_hz=400.0
- [2026-08-28 19:08:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915333.9019024 | source=vosk | rms=498 | updated_at=1787915331.4214914 | frequency_hz=400.0
- [2026-08-28 19:08:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915334.4020386 | source=vosk | rms=498 | updated_at=1787915331.4214914 | frequency_hz=400.0
- [2026-08-28 19:08:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915334.6518724 | source=vosk | rms=500 | updated_at=1787915334.6518724 | frequency_hz=400.0
- [2026-08-28 19:08:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915336.4048233 | source=vosk | rms=413 | updated_at=1787915334.9064791 | frequency_hz=400.0
- [2026-08-28 19:08:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915337.4076486 | source=vosk | rms=413 | updated_at=1787915334.9064791 | frequency_hz=400.0
- [2026-08-28 19:08:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915337.9018142 | source=vosk | rms=413 | updated_at=1787915334.9064791 | frequency_hz=400.0
- [2026-08-28 19:08:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915338.6551375 | source=vosk | rms=413 | updated_at=1787915334.9064791 | frequency_hz=400.0
- [2026-08-28 19:08:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915339.6518242 | source=vosk | rms=530 | updated_at=1787915339.1666532 | frequency_hz=400.0
- [2026-08-28 19:09:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915341.906194 | source=vosk | rms=530 | updated_at=1787915339.1666532 | frequency_hz=400.0
- [2026-08-28 19:09:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915342.6516695 | source=vosk | rms=452 | updated_at=1787915342.151455 | frequency_hz=400.0
- [2026-08-28 19:09:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915343.173137 | source=vosk | rms=543 | updated_at=1787915343.173137 | frequency_hz=400.0
- [2026-08-28 19:09:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915344.152073 | source=vosk | rms=536 | updated_at=1787915343.651926 | frequency_hz=400.0
- [2026-08-28 19:09:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915344.6554992 | source=vosk | rms=536 | updated_at=1787915343.651926 | frequency_hz=400.0
- [2026-08-28 19:09:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915348.6518784 | source=vosk | rms=448 | updated_at=1787915348.1522415 | frequency_hz=400.0
- [2026-08-28 19:09:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915349.1519816 | source=vosk | rms=852 | updated_at=1787915349.1519816 | frequency_hz=400.0
- [2026-08-28 19:09:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915352.1520047 | source=vosk | rms=552 | updated_at=1787915351.6518426 | frequency_hz=400.0
- [2026-08-28 19:09:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915352.4015872 | source=vosk | rms=552 | updated_at=1787915351.6518426 | frequency_hz=400.0
- [2026-08-28 19:09:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915353.1556652 | source=vosk | rms=586 | updated_at=1787915352.7263691 | frequency_hz=400.0
- [2026-08-28 19:09:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915353.402537 | source=vosk | rms=285 | updated_at=1787915353.402537 | frequency_hz=400.0
- [2026-08-28 19:09:14] operator / voice_transcript_final / voice: so
  meta: kind=final | timestamp=1787915354.728281 | source=final | rms=360 | updated_at=1787915354.4162323 | frequency_hz=400.0
- [2026-08-28 19:09:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915354.7689736 | source=vosk | rms=574 | updated_at=1787915354.7689736 | frequency_hz=400.0
- [2026-08-28 19:09:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915355.6515539 | source=vosk | rms=379 | updated_at=1787915355.1522918 | frequency_hz=400.0
- [2026-08-28 19:09:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915356.439708 | source=vosk | rms=663 | updated_at=1787915356.439708 | frequency_hz=400.0
- [2026-08-28 19:09:17] operator / voice_transcript_partial / voice: six
  meta: kind=partial | timestamp=1787915357.1960201 | source=vosk | rms=561 | updated_at=1787915356.6941953 | frequency_hz=400.0
- [2026-08-28 19:09:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915357.68518 | source=vosk | rms=561 | updated_at=1787915356.6941953 | frequency_hz=400.0
- [2026-08-28 19:09:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915358.4379742 | source=vosk | rms=1202 | updated_at=1787915358.4379742 | frequency_hz=400.0
- [2026-08-28 19:09:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915358.6923678 | source=vosk | rms=1202 | updated_at=1787915358.6923678 | frequency_hz=400.0
- [2026-08-28 19:09:18] operator / voice_transcript_final / voice: six
  meta: kind=final | timestamp=1787915358.9312503 | source=final | rms=1202 | updated_at=1787915358.6923678 | frequency_hz=400.0
- [2026-08-28 19:09:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915358.9766097 | source=vosk | rms=1202 | updated_at=1787915358.6923678 | frequency_hz=400.0
- [2026-08-28 19:09:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915359.942129 | source=vosk | rms=317 | updated_at=1787915359.4427183 | frequency_hz=400.0
- [2026-08-28 19:09:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915360.4420462 | source=vosk | rms=317 | updated_at=1787915359.4427183 | frequency_hz=400.0
- [2026-08-28 19:09:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915360.943389 | source=vosk | rms=317 | updated_at=1787915359.4427183 | frequency_hz=400.0
- [2026-08-28 19:09:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915361.444441 | source=vosk | rms=317 | updated_at=1787915359.4427183 | frequency_hz=400.0
- [2026-08-28 19:09:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915361.9720926 | source=vosk | rms=317 | updated_at=1787915359.4427183 | frequency_hz=400.0
- [2026-08-28 19:09:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915363.203654 | source=vosk | rms=1200 | updated_at=1787915363.203654 | frequency_hz=400.0
- [2026-08-28 19:09:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915363.6923363 | source=vosk | rms=1200 | updated_at=1787915363.203654 | frequency_hz=400.0
- [2026-08-28 19:09:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915364.4428108 | source=vosk | rms=306 | updated_at=1787915364.4428108 | frequency_hz=400.0
- [2026-08-28 19:09:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915367.7103388 | source=vosk | rms=318 | updated_at=1787915367.192421 | frequency_hz=400.0
- [2026-08-28 19:09:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915368.9535472 | source=vosk | rms=318 | updated_at=1787915367.192421 | frequency_hz=400.0
- [2026-08-28 19:09:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915369.4423962 | source=vosk | rms=318 | updated_at=1787915367.192421 | frequency_hz=400.0
- [2026-08-28 19:09:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915369.943155 | source=vosk | rms=318 | updated_at=1787915367.192421 | frequency_hz=400.0
- [2026-08-28 19:09:30] operator / voice_transcript_partial / voice: he just
  meta: kind=partial | timestamp=1787915370.2281053 | source=vosk | rms=318 | updated_at=1787915367.192421 | frequency_hz=400.0
- [2026-08-28 19:09:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915370.448905 | source=vosk | rms=318 | updated_at=1787915367.192421 | frequency_hz=400.0
- [2026-08-28 19:09:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915370.6924262 | source=vosk | rms=318 | updated_at=1787915367.192421 | frequency_hz=400.0
- [2026-08-28 19:09:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915371.2029192 | source=vosk | rms=318 | updated_at=1787915367.192421 | frequency_hz=400.0
- [2026-08-28 19:09:31] operator / voice_transcript_final / voice: he just
  meta: kind=final | timestamp=1787915371.457757 | source=final | rms=318 | updated_at=1787915367.192421 | frequency_hz=400.0
- [2026-08-28 19:09:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915371.4878397 | source=vosk | rms=318 | updated_at=1787915367.192421 | frequency_hz=400.0
- [2026-08-28 19:09:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915374.4426737 | source=vosk | rms=305 | updated_at=1787915373.9420094 | frequency_hz=400.0
- [2026-08-28 19:09:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915374.7438216 | source=vosk | rms=305 | updated_at=1787915373.9420094 | frequency_hz=400.0
- [2026-08-28 19:09:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915377.6927707 | source=vosk | rms=494 | updated_at=1787915377.1960826 | frequency_hz=400.0
- [2026-08-28 19:09:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915378.2080245 | source=vosk | rms=494 | updated_at=1787915377.1960826 | frequency_hz=400.0
- [2026-08-28 19:09:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915380.1939251 | source=vosk | rms=663 | updated_at=1787915379.7023506 | frequency_hz=400.0
- [2026-08-28 19:09:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915382.4613614 | source=vosk | rms=663 | updated_at=1787915379.7023506 | frequency_hz=400.0
- [2026-08-28 19:09:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915382.960565 | source=vosk | rms=663 | updated_at=1787915379.7023506 | frequency_hz=400.0
- [2026-08-28 19:09:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915385.9428194 | source=vosk | rms=689 | updated_at=1787915385.9428194 | frequency_hz=400.0
- [2026-08-28 19:09:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915386.9741187 | source=vosk | rms=689 | updated_at=1787915385.9428194 | frequency_hz=400.0
- [2026-08-28 19:09:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915388.6933029 | source=vosk | rms=228 | updated_at=1787915388.6933029 | frequency_hz=400.0
- [2026-08-28 19:09:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915389.196161 | source=vosk | rms=228 | updated_at=1787915388.6933029 | frequency_hz=400.0
- [2026-08-28 19:09:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915389.7176576 | source=vosk | rms=228 | updated_at=1787915388.6933029 | frequency_hz=400.0
- [2026-08-28 19:09:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915390.4543757 | source=vosk | rms=228 | updated_at=1787915388.6933029 | frequency_hz=400.0
- [2026-08-28 19:09:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915391.6941507 | source=vosk | rms=448 | updated_at=1787915391.6941507 | frequency_hz=400.0
- [2026-08-28 19:09:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915392.1943738 | source=vosk | rms=448 | updated_at=1787915391.6941507 | frequency_hz=400.0
- [2026-08-28 19:09:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915394.214184 | source=vosk | rms=448 | updated_at=1787915391.6941507 | frequency_hz=400.0
- [2026-08-28 19:09:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915394.6935287 | source=vosk | rms=448 | updated_at=1787915391.6941507 | frequency_hz=400.0
- [2026-08-28 19:09:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915396.442749 | source=vosk | rms=448 | updated_at=1787915391.6941507 | frequency_hz=400.0
- [2026-08-28 19:09:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915396.9432726 | source=vosk | rms=448 | updated_at=1787915391.6941507 | frequency_hz=400.0
- [2026-08-28 19:09:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915398.6929367 | source=vosk | rms=281 | updated_at=1787915398.6929367 | frequency_hz=400.0
- [2026-08-28 19:10:00] operator / voice_transcript_final / voice: oh
  meta: kind=final | timestamp=1787915400.7180448 | source=final | rms=872 | updated_at=1787915400.4432142 | frequency_hz=400.0
- [2026-08-28 19:10:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915400.751414 | source=vosk | rms=1101 | updated_at=1787915400.751414 | frequency_hz=400.0
- [2026-08-28 19:10:01] operator / voice_transcript_partial / voice: a little
  meta: kind=partial | timestamp=1787915401.0190802 | source=vosk | rms=784 | updated_at=1787915400.9431813 | frequency_hz=400.0
- [2026-08-28 19:10:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915401.1944017 | source=vosk | rms=937 | updated_at=1787915401.1944017 | frequency_hz=400.0
- [2026-08-28 19:10:01] operator / voice_transcript_partial / voice: or
  meta: kind=partial | timestamp=1787915401.289153 | source=vosk | rms=937 | updated_at=1787915401.1944017 | frequency_hz=400.0
- [2026-08-28 19:10:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915401.4644766 | source=vosk | rms=1173 | updated_at=1787915401.4644766 | frequency_hz=400.0
- [2026-08-28 19:10:01] operator / voice_transcript_partial / voice: or maybe
  meta: kind=partial | timestamp=1787915401.5843256 | source=vosk | rms=1173 | updated_at=1787915401.4644766 | frequency_hz=400.0
- [2026-08-28 19:10:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915401.7049167 | source=vosk | rms=1036 | updated_at=1787915401.7049167 | frequency_hz=400.0
- [2026-08-28 19:10:01] operator / voice_transcript_partial / voice: or maybe maybe
  meta: kind=partial | timestamp=1787915401.804928 | source=vosk | rms=1036 | updated_at=1787915401.7049167 | frequency_hz=400.0
- [2026-08-28 19:10:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915401.9581583 | source=vosk | rms=1036 | updated_at=1787915401.7049167 | frequency_hz=400.0
- [2026-08-28 19:10:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915402.1934452 | source=vosk | rms=359 | updated_at=1787915402.1934452 | frequency_hz=400.0
- [2026-08-28 19:10:02] operator / voice_transcript_partial / voice: or maybe maybe we
  meta: kind=partial | timestamp=1787915402.2581193 | source=vosk | rms=359 | updated_at=1787915402.1934452 | frequency_hz=400.0
- [2026-08-28 19:10:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915402.4499078 | source=vosk | rms=1130 | updated_at=1787915402.4499078 | frequency_hz=400.0
- [2026-08-28 19:10:02] operator / voice_transcript_final / voice: a little are many men
  meta: kind=final | timestamp=1787915402.8381836 | source=final | rms=1130 | updated_at=1787915402.4499078 | frequency_hz=400.0
- [2026-08-28 19:10:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915403.0003986 | source=vosk | rms=1130 | updated_at=1787915402.4499078 | frequency_hz=400.0
- [2026-08-28 19:10:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915403.0003986 | source=vosk | rms=1200 | updated_at=1787915403.0003986 | frequency_hz=400.0
- [2026-08-28 19:10:05] operator / voice_transcript_partial / voice: around
  meta: kind=partial | timestamp=1787915405.4756658 | source=vosk | rms=877 | updated_at=1787915405.443191 | frequency_hz=400.0
- [2026-08-28 19:10:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915405.7120466 | source=vosk | rms=469 | updated_at=1787915405.7120466 | frequency_hz=400.0
- [2026-08-28 19:10:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915405.943628 | source=vosk | rms=782 | updated_at=1787915405.943628 | frequency_hz=400.0
- [2026-08-28 19:10:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915406.193301 | source=vosk | rms=484 | updated_at=1787915406.193301 | frequency_hz=400.0
- [2026-08-28 19:10:06] operator / voice_transcript_partial / voice: around or
  meta: kind=partial | timestamp=1787915406.2746089 | source=vosk | rms=484 | updated_at=1787915406.193301 | frequency_hz=400.0
- [2026-08-28 19:10:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915406.4435892 | source=vosk | rms=271 | updated_at=1787915406.4435892 | frequency_hz=400.0
- [2026-08-28 19:10:06] operator / voice_transcript_partial / voice: around or maybe
  meta: kind=partial | timestamp=1787915406.472337 | source=vosk | rms=271 | updated_at=1787915406.4435892 | frequency_hz=400.0
- [2026-08-28 19:10:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915406.6938634 | source=vosk | rms=220 | updated_at=1787915406.6938634 | frequency_hz=400.0
- [2026-08-28 19:10:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915406.9435203 | source=vosk | rms=917 | updated_at=1787915406.9435203 | frequency_hz=400.0
- [2026-08-28 19:10:07] operator / voice_transcript_partial / voice: around or maybe longer than
  meta: kind=partial | timestamp=1787915407.022461 | source=vosk | rms=917 | updated_at=1787915406.9435203 | frequency_hz=400.0
- [2026-08-28 19:10:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915407.194606 | source=vosk | rms=618 | updated_at=1787915407.194606 | frequency_hz=400.0
- [2026-08-28 19:10:07] operator / voice_transcript_partial / voice: around or maybe longer than it
  meta: kind=partial | timestamp=1787915407.3027875 | source=vosk | rms=618 | updated_at=1787915407.194606 | frequency_hz=400.0
- [2026-08-28 19:10:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915407.4488983 | source=vosk | rms=247 | updated_at=1787915407.4488983 | frequency_hz=400.0
- [2026-08-28 19:10:07] operator / voice_transcript_partial / voice: around or maybe longer than it was
  meta: kind=partial | timestamp=1787915407.531587 | source=vosk | rms=247 | updated_at=1787915407.4488983 | frequency_hz=400.0
- [2026-08-28 19:10:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915407.6935117 | source=vosk | rms=362 | updated_at=1787915407.6935117 | frequency_hz=400.0
- [2026-08-28 19:10:08] operator / voice_transcript_final / voice: around or maybe longer with the
  meta: kind=final | timestamp=1787915408.0374212 | source=final | rms=362 | updated_at=1787915407.6935117 | frequency_hz=400.0
- [2026-08-28 19:10:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915408.1403508 | source=vosk | rms=362 | updated_at=1787915407.6935117 | frequency_hz=400.0
- [2026-08-28 19:10:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915408.1403508 | source=vosk | rms=244 | updated_at=1787915408.1403508 | frequency_hz=400.0
- [2026-08-28 19:10:08] operator / voice_transcript_partial / voice: look
  meta: kind=partial | timestamp=1787915408.1645174 | source=vosk | rms=244 | updated_at=1787915408.1403508 | frequency_hz=400.0
- [2026-08-28 19:10:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915408.446849 | source=vosk | rms=1202 | updated_at=1787915408.446849 | frequency_hz=400.0
- [2026-08-28 19:10:08] operator / voice_transcript_partial / voice: i don't
  meta: kind=partial | timestamp=1787915408.6404028 | source=vosk | rms=1202 | updated_at=1787915408.446849 | frequency_hz=400.0
- [2026-08-28 19:10:08] operator / voice_transcript_partial / voice: don't feel
  meta: kind=partial | timestamp=1787915408.7884452 | source=vosk | rms=1201 | updated_at=1787915408.7035277 | frequency_hz=400.0
- [2026-08-28 19:10:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915409.6109502 | source=vosk | rms=950 | updated_at=1787915409.6109502 | frequency_hz=400.0
- [2026-08-28 19:10:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915410.1215405 | source=vosk | rms=950 | updated_at=1787915409.6109502 | frequency_hz=400.0
- [2026-08-28 19:10:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915410.6031704 | source=vosk | rms=125 | updated_at=1787915410.6031704 | frequency_hz=400.0
- [2026-08-28 19:10:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915410.8585484 | source=vosk | rms=285 | updated_at=1787915410.8585484 | frequency_hz=400.0
- [2026-08-28 19:10:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915411.1034856 | source=vosk | rms=1117 | updated_at=1787915411.1034856 | frequency_hz=400.0
- [2026-08-28 19:10:11] operator / voice_transcript_final / voice: look to for you
  meta: kind=final | timestamp=1787915411.4811397 | source=final | rms=1117 | updated_at=1787915411.1034856 | frequency_hz=400.0
- [2026-08-28 19:10:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915411.5930443 | source=vosk | rms=1117 | updated_at=1787915411.1034856 | frequency_hz=400.0
- [2026-08-28 19:10:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915418.3595922 | source=vosk | rms=372 | updated_at=1787915418.3595922 | frequency_hz=400.0
- [2026-08-28 19:10:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915420.3534102 | source=vosk | rms=551 | updated_at=1787915419.8653994 | frequency_hz=400.0
- [2026-08-28 19:10:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915421.1319816 | source=vosk | rms=829 | updated_at=1787915421.1319816 | frequency_hz=400.0
- [2026-08-28 19:10:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915421.8697083 | source=vosk | rms=429 | updated_at=1787915421.3550587 | frequency_hz=400.0
- [2026-08-28 19:10:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915425.8691902 | source=vosk | rms=429 | updated_at=1787915421.3550587 | frequency_hz=400.0
- [2026-08-28 19:10:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915426.3603296 | source=vosk | rms=429 | updated_at=1787915421.3550587 | frequency_hz=400.0
- [2026-08-28 19:10:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915428.1050785 | source=vosk | rms=429 | updated_at=1787915421.3550587 | frequency_hz=400.0
- [2026-08-28 19:10:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915428.6036215 | source=vosk | rms=429 | updated_at=1787915421.3550587 | frequency_hz=400.0
- [2026-08-28 19:10:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915433.354978 | source=vosk | rms=555 | updated_at=1787915433.354978 | frequency_hz=400.0
- [2026-08-28 19:10:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915434.1040146 | source=vosk | rms=485 | updated_at=1787915433.6041327 | frequency_hz=400.0
- [2026-08-28 19:10:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915435.103654 | source=vosk | rms=506 | updated_at=1787915435.103654 | frequency_hz=400.0
- [2026-08-28 19:10:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915435.8880432 | source=vosk | rms=506 | updated_at=1787915435.103654 | frequency_hz=400.0
- [2026-08-28 19:10:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915436.3538778 | source=vosk | rms=900 | updated_at=1787915436.3538778 | frequency_hz=400.0
- [2026-08-28 19:10:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915437.1098335 | source=vosk | rms=900 | updated_at=1787915436.3538778 | frequency_hz=400.0
- [2026-08-28 19:10:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915440.6042075 | source=vosk | rms=127 | updated_at=1787915440.6042075 | frequency_hz=400.0
- [2026-08-28 19:10:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915441.1039104 | source=vosk | rms=127 | updated_at=1787915440.6042075 | frequency_hz=400.0
- [2026-08-28 19:10:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915442.1047094 | source=vosk | rms=505 | updated_at=1787915442.1047094 | frequency_hz=400.0
- [2026-08-28 19:10:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915447.1047795 | source=vosk | rms=371 | updated_at=1787915446.3983262 | frequency_hz=400.0
- [2026-08-28 19:10:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915447.3541973 | source=vosk | rms=211 | updated_at=1787915447.3541973 | frequency_hz=400.0
- [2026-08-28 19:10:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915450.8795671 | source=vosk | rms=862 | updated_at=1787915450.3536146 | frequency_hz=400.0
- [2026-08-28 19:10:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915451.6042404 | source=vosk | rms=707 | updated_at=1787915451.6042404 | frequency_hz=400.0
- [2026-08-28 19:10:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915452.3574924 | source=vosk | rms=707 | updated_at=1787915451.6042404 | frequency_hz=400.0
- [2026-08-28 19:10:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915454.3550017 | source=vosk | rms=579 | updated_at=1787915454.3550017 | frequency_hz=400.0
- [2026-08-28 19:10:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915454.8758328 | source=vosk | rms=579 | updated_at=1787915454.3550017 | frequency_hz=400.0
- [2026-08-28 19:10:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915459.1049876 | source=vosk | rms=301 | updated_at=1787915459.1049876 | frequency_hz=400.0
- [2026-08-28 19:11:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915460.6051755 | source=vosk | rms=904 | updated_at=1787915460.104983 | frequency_hz=400.0
- [2026-08-28 19:11:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915461.1050558 | source=vosk | rms=959 | updated_at=1787915461.1050558 | frequency_hz=400.0
- [2026-08-28 19:11:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915462.6046464 | source=vosk | rms=819 | updated_at=1787915462.1040597 | frequency_hz=400.0
- [2026-08-28 19:11:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915464.1051674 | source=vosk | rms=403 | updated_at=1787915464.1051674 | frequency_hz=400.0
- [2026-08-28 19:11:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915464.8605425 | source=vosk | rms=601 | updated_at=1787915464.3647842 | frequency_hz=400.0
- [2026-08-28 19:11:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915466.3557172 | source=vosk | rms=402 | updated_at=1787915466.3557172 | frequency_hz=400.0
- [2026-08-28 19:11:06] operator / voice_transcript_final / voice: yeah
  meta: kind=final | timestamp=1787915466.6550345 | source=final | rms=402 | updated_at=1787915466.3557172 | frequency_hz=400.0
- [2026-08-28 19:11:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915466.6890385 | source=vosk | rms=402 | updated_at=1787915466.3557172 | frequency_hz=400.0
- [2026-08-28 19:11:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915469.6061387 | source=vosk | rms=1205 | updated_at=1787915469.1084275 | frequency_hz=400.0
- [2026-08-28 19:11:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915469.8548021 | source=vosk | rms=874 | updated_at=1787915469.8548021 | frequency_hz=400.0
- [2026-08-28 19:11:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915470.3586617 | source=vosk | rms=874 | updated_at=1787915469.8548021 | frequency_hz=400.0
- [2026-08-28 19:11:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915471.361981 | source=vosk | rms=614 | updated_at=1787915471.361981 | frequency_hz=400.0
- [2026-08-28 19:11:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915471.8553057 | source=vosk | rms=614 | updated_at=1787915471.361981 | frequency_hz=400.0
- [2026-08-28 19:11:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915472.1048727 | source=vosk | rms=614 | updated_at=1787915471.361981 | frequency_hz=400.0
- [2026-08-28 19:11:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915474.1208107 | source=vosk | rms=304 | updated_at=1787915473.3552458 | frequency_hz=400.0
- [2026-08-28 19:11:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915475.129258 | source=vosk | rms=304 | updated_at=1787915473.3552458 | frequency_hz=400.0
- [2026-08-28 19:11:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915477.3694272 | source=vosk | rms=273 | updated_at=1787915476.8632545 | frequency_hz=400.0
- [2026-08-28 19:11:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915477.6187828 | source=vosk | rms=482 | updated_at=1787915477.6187828 | frequency_hz=400.0
- [2026-08-28 19:11:18] operator / voice_transcript_partial / voice: we
  meta: kind=partial | timestamp=1787915478.180574 | source=vosk | rms=1048 | updated_at=1787915478.1225805 | frequency_hz=400.0
- [2026-08-28 19:11:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915478.3670805 | source=vosk | rms=478 | updated_at=1787915478.3670805 | frequency_hz=400.0
- [2026-08-28 19:11:18] operator / voice_transcript_partial / voice: blueberries or
  meta: kind=partial | timestamp=1787915478.491681 | source=vosk | rms=478 | updated_at=1787915478.3670805 | frequency_hz=400.0
- [2026-08-28 19:11:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915479.1051955 | source=vosk | rms=478 | updated_at=1787915478.3670805 | frequency_hz=400.0
- [2026-08-28 19:11:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915479.6074126 | source=vosk | rms=533 | updated_at=1787915479.6074126 | frequency_hz=400.0
- [2026-08-28 19:11:19] operator / voice_transcript_partial / voice: blueberries or know
  meta: kind=partial | timestamp=1787915479.6261473 | source=vosk | rms=533 | updated_at=1787915479.6074126 | frequency_hz=400.0
- [2026-08-28 19:11:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915479.863209 | source=vosk | rms=661 | updated_at=1787915479.863209 | frequency_hz=400.0
- [2026-08-28 19:11:19] operator / voice_transcript_partial / voice: blueberries are no one
  meta: kind=partial | timestamp=1787915479.9069197 | source=vosk | rms=661 | updated_at=1787915479.863209 | frequency_hz=400.0
- [2026-08-28 19:11:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915480.1052237 | source=vosk | rms=537 | updated_at=1787915480.1052237 | frequency_hz=400.0
- [2026-08-28 19:11:20] operator / voice_transcript_partial / voice: blueberries are no one will
  meta: kind=partial | timestamp=1787915480.120076 | source=vosk | rms=537 | updated_at=1787915480.1052237 | frequency_hz=400.0
- [2026-08-28 19:11:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915480.354878 | source=vosk | rms=550 | updated_at=1787915480.354878 | frequency_hz=400.0
- [2026-08-28 19:11:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915480.6050072 | source=vosk | rms=531 | updated_at=1787915480.6050072 | frequency_hz=400.0
- [2026-08-28 19:11:20] operator / voice_transcript_partial / voice: blueberries are no whoops a couple
  meta: kind=partial | timestamp=1787915480.6616788 | source=vosk | rms=531 | updated_at=1787915480.6050072 | frequency_hz=400.0
- [2026-08-28 19:11:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915480.9019551 | source=vosk | rms=1201 | updated_at=1787915480.9019551 | frequency_hz=400.0
- [2026-08-28 19:11:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915481.1223276 | source=vosk | rms=1204 | updated_at=1787915481.1223276 | frequency_hz=400.0
- [2026-08-28 19:11:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915481.3550212 | source=vosk | rms=698 | updated_at=1787915481.3550212 | frequency_hz=400.0
- [2026-08-28 19:11:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915481.8552365 | source=vosk | rms=698 | updated_at=1787915481.3550212 | frequency_hz=400.0
- [2026-08-28 19:11:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915482.8551326 | source=vosk | rms=613 | updated_at=1787915482.8551326 | frequency_hz=400.0
- [2026-08-28 19:11:23] operator / voice_transcript_final / voice: blueberries are no whoops a couple know
  meta: kind=final | timestamp=1787915483.1494982 | source=final | rms=613 | updated_at=1787915482.8551326 | frequency_hz=400.0
- [2026-08-28 19:11:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915483.2837179 | source=vosk | rms=613 | updated_at=1787915482.8551326 | frequency_hz=400.0
- [2026-08-28 19:11:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915483.2837179 | source=vosk | rms=845 | updated_at=1787915483.2837179 | frequency_hz=400.0
- [2026-08-28 19:11:23] operator / voice_transcript_partial / voice: so i
  meta: kind=partial | timestamp=1787915483.3195717 | source=vosk | rms=845 | updated_at=1787915483.2837179 | frequency_hz=400.0
- [2026-08-28 19:11:23] operator / voice_transcript_partial / voice: so i visited
  meta: kind=partial | timestamp=1787915483.4499924 | source=vosk | rms=322 | updated_at=1787915483.3608546 | frequency_hz=400.0
- [2026-08-28 19:11:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915483.6052966 | source=vosk | rms=631 | updated_at=1787915483.6052966 | frequency_hz=400.0
- [2026-08-28 19:11:23] operator / voice_transcript_partial / voice: so i visited me
  meta: kind=partial | timestamp=1787915483.6797724 | source=vosk | rms=631 | updated_at=1787915483.6052966 | frequency_hz=400.0
- [2026-08-28 19:11:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915483.9144456 | source=vosk | rms=353 | updated_at=1787915483.9144456 | frequency_hz=400.0
- [2026-08-28 19:11:24] operator / voice_transcript_partial / voice: so i was able to go
  meta: kind=partial | timestamp=1787915484.0076897 | source=vosk | rms=353 | updated_at=1787915483.9144456 | frequency_hz=400.0
- [2026-08-28 19:11:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915484.1054666 | source=vosk | rms=547 | updated_at=1787915484.1054666 | frequency_hz=400.0
- [2026-08-28 19:11:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915484.355422 | source=vosk | rms=408 | updated_at=1787915484.355422 | frequency_hz=400.0
- [2026-08-28 19:11:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915484.627139 | source=vosk | rms=400 | updated_at=1787915484.627139 | frequency_hz=400.0
- [2026-08-28 19:11:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915484.8740022 | source=vosk | rms=654 | updated_at=1787915484.8740022 | frequency_hz=400.0
- [2026-08-28 19:11:25] operator / voice_transcript_final / voice: so i visited me go
  meta: kind=final | timestamp=1787915485.1907847 | source=final | rms=654 | updated_at=1787915484.8740022 | frequency_hz=400.0
- [2026-08-28 19:11:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915485.5014558 | source=vosk | rms=654 | updated_at=1787915484.8740022 | frequency_hz=400.0
- [2026-08-28 19:11:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915485.5014558 | source=vosk | rms=550 | updated_at=1787915485.5014558 | frequency_hz=400.0
- [2026-08-28 19:11:27] operator / voice_transcript_partial / voice: mark saunders
  meta: kind=partial | timestamp=1787915487.8934917 | source=vosk | rms=688 | updated_at=1787915487.8554063 | frequency_hz=400.0
- [2026-08-28 19:11:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915488.1104057 | source=vosk | rms=618 | updated_at=1787915488.1104057 | frequency_hz=400.0
- [2026-08-28 19:11:28] operator / voice_transcript_partial / voice: sound gonna
  meta: kind=partial | timestamp=1787915488.2195666 | source=vosk | rms=618 | updated_at=1787915488.1104057 | frequency_hz=400.0
- [2026-08-28 19:11:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915488.3813741 | source=vosk | rms=618 | updated_at=1787915488.1104057 | frequency_hz=400.0
- [2026-08-28 19:11:28] operator / voice_transcript_partial / voice: sound condescending
  meta: kind=partial | timestamp=1787915488.4367871 | source=vosk | rms=618 | updated_at=1787915488.1104057 | frequency_hz=400.0
- [2026-08-28 19:11:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915488.6055057 | source=vosk | rms=618 | updated_at=1787915488.1104057 | frequency_hz=400.0
- [2026-08-28 19:11:28] operator / voice_transcript_partial / voice: sound condescending and
  meta: kind=partial | timestamp=1787915488.6693187 | source=vosk | rms=618 | updated_at=1787915488.1104057 | frequency_hz=400.0
- [2026-08-28 19:11:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915489.1094215 | source=vosk | rms=618 | updated_at=1787915488.1104057 | frequency_hz=400.0
- [2026-08-28 19:11:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915489.855229 | source=vosk | rms=721 | updated_at=1787915489.855229 | frequency_hz=400.0
- [2026-08-28 19:11:29] operator / voice_transcript_partial / voice: sound condescending
  meta: kind=partial | timestamp=1787915489.910188 | source=vosk | rms=721 | updated_at=1787915489.855229 | frequency_hz=400.0
- [2026-08-28 19:11:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915490.105609 | source=vosk | rms=1092 | updated_at=1787915490.105609 | frequency_hz=400.0
- [2026-08-28 19:11:30] operator / voice_transcript_partial / voice: sound condescending agreement between
  meta: kind=partial | timestamp=1787915490.1455524 | source=vosk | rms=1092 | updated_at=1787915490.105609 | frequency_hz=400.0
- [2026-08-28 19:11:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915490.6064975 | source=vosk | rms=1092 | updated_at=1787915490.105609 | frequency_hz=400.0
- [2026-08-28 19:11:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915491.1056678 | source=vosk | rms=554 | updated_at=1787915491.1056678 | frequency_hz=400.0
- [2026-08-28 19:11:31] operator / voice_transcript_partial / voice: sound condescending agreement
  meta: kind=partial | timestamp=1787915491.1239934 | source=vosk | rms=554 | updated_at=1787915491.1056678 | frequency_hz=400.0
- [2026-08-28 19:11:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915491.3551283 | source=vosk | rms=576 | updated_at=1787915491.3551283 | frequency_hz=400.0
- [2026-08-28 19:11:31] operator / voice_transcript_partial / voice: sound condescending agreement was
  meta: kind=partial | timestamp=1787915491.3776734 | source=vosk | rms=576 | updated_at=1787915491.3551283 | frequency_hz=400.0
- [2026-08-28 19:11:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915491.611963 | source=vosk | rms=633 | updated_at=1787915491.611963 | frequency_hz=400.0
- [2026-08-28 19:11:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915491.8554537 | source=vosk | rms=633 | updated_at=1787915491.611963 | frequency_hz=400.0
- [2026-08-28 19:11:31] operator / voice_transcript_partial / voice: sound condescending agreement with this new
  meta: kind=partial | timestamp=1787915491.8993788 | source=vosk | rms=633 | updated_at=1787915491.611963 | frequency_hz=400.0
- [2026-08-28 19:11:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915492.1087153 | source=vosk | rms=476 | updated_at=1787915492.1087153 | frequency_hz=400.0
- [2026-08-28 19:11:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915492.6054199 | source=vosk | rms=476 | updated_at=1787915492.1087153 | frequency_hz=400.0
- [2026-08-28 19:11:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915492.8566852 | source=vosk | rms=679 | updated_at=1787915492.8566852 | frequency_hz=400.0
- [2026-08-28 19:11:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915493.605364 | source=vosk | rms=1060 | updated_at=1787915493.605364 | frequency_hz=400.0
- [2026-08-28 19:11:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915493.854982 | source=vosk | rms=1060 | updated_at=1787915493.605364 | frequency_hz=400.0
- [2026-08-28 19:11:34] operator / voice_transcript_final / voice: mark sound condescending agreement was this new
  meta: kind=final | timestamp=1787915494.1544251 | source=final | rms=1060 | updated_at=1787915493.605364 | frequency_hz=400.0
- [2026-08-28 19:11:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915494.2699258 | source=vosk | rms=1060 | updated_at=1787915493.605364 | frequency_hz=400.0
- [2026-08-28 19:11:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915494.8606665 | source=vosk | rms=600 | updated_at=1787915494.3737335 | frequency_hz=400.0
- [2026-08-28 19:11:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915495.6126342 | source=vosk | rms=530 | updated_at=1787915495.6126342 | frequency_hz=400.0
- [2026-08-28 19:11:35] operator / voice_transcript_partial / voice: i don't
  meta: kind=partial | timestamp=1787915495.9214132 | source=vosk | rms=540 | updated_at=1787915495.8992875 | frequency_hz=400.0
- [2026-08-28 19:11:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915496.1055894 | source=vosk | rms=540 | updated_at=1787915495.8992875 | frequency_hz=400.0
- [2026-08-28 19:11:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915496.3554358 | source=vosk | rms=542 | updated_at=1787915496.3554358 | frequency_hz=400.0
- [2026-08-28 19:11:36] operator / voice_transcript_partial / voice: i don't know
  meta: kind=partial | timestamp=1787915496.3764834 | source=vosk | rms=542 | updated_at=1787915496.3554358 | frequency_hz=400.0
- [2026-08-28 19:11:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915496.8643646 | source=vosk | rms=542 | updated_at=1787915496.3554358 | frequency_hz=400.0
- [2026-08-28 19:11:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915497.1097858 | source=vosk | rms=698 | updated_at=1787915497.1097858 | frequency_hz=400.0
- [2026-08-28 19:11:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915497.3559859 | source=vosk | rms=1201 | updated_at=1787915497.3559859 | frequency_hz=400.0
- [2026-08-28 19:11:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915497.6058497 | source=vosk | rms=1201 | updated_at=1787915497.3559859 | frequency_hz=400.0
- [2026-08-28 19:11:37] operator / voice_transcript_final / voice: i don t know
  meta: kind=final | timestamp=1787915497.9941263 | source=final | rms=1201 | updated_at=1787915497.3559859 | frequency_hz=400.0
- [2026-08-28 19:11:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915498.0946047 | source=vosk | rms=1201 | updated_at=1787915497.3559859 | frequency_hz=400.0
- [2026-08-28 19:11:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915498.0946047 | source=vosk | rms=450 | updated_at=1787915498.0946047 | frequency_hz=400.0
- [2026-08-28 19:11:38] operator / voice_transcript_partial / voice: what he
  meta: kind=partial | timestamp=1787915498.7109213 | source=vosk | rms=935 | updated_at=1787915498.640554 | frequency_hz=400.0
- [2026-08-28 19:11:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915498.8558373 | source=vosk | rms=843 | updated_at=1787915498.8558373 | frequency_hz=400.0
- [2026-08-28 19:11:38] operator / voice_transcript_partial / voice: borderlands
  meta: kind=partial | timestamp=1787915498.9242744 | source=vosk | rms=843 | updated_at=1787915498.8558373 | frequency_hz=400.0
- [2026-08-28 19:11:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915499.1055126 | source=vosk | rms=600 | updated_at=1787915499.1055126 | frequency_hz=400.0
- [2026-08-28 19:11:39] operator / voice_transcript_partial / voice: what he wanted a good
  meta: kind=partial | timestamp=1787915499.1766667 | source=vosk | rms=600 | updated_at=1787915499.1055126 | frequency_hz=400.0
- [2026-08-28 19:11:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915499.363907 | source=vosk | rms=652 | updated_at=1787915499.363907 | frequency_hz=400.0
- [2026-08-28 19:11:39] operator / voice_transcript_partial / voice: what he wanted a good one
  meta: kind=partial | timestamp=1787915499.4179513 | source=vosk | rms=652 | updated_at=1787915499.363907 | frequency_hz=400.0
- [2026-08-28 19:11:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915499.6068888 | source=vosk | rms=706 | updated_at=1787915499.6068888 | frequency_hz=400.0
- [2026-08-28 19:11:39] operator / voice_transcript_partial / voice: what he wanted a good one only
  meta: kind=partial | timestamp=1787915499.6675923 | source=vosk | rms=706 | updated_at=1787915499.6068888 | frequency_hz=400.0
- [2026-08-28 19:11:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915500.0790472 | source=vosk | rms=458 | updated_at=1787915500.0790472 | frequency_hz=400.0
- [2026-08-28 19:11:40] operator / voice_transcript_partial / voice: what he wanted a good one only but
  meta: kind=partial | timestamp=1787915500.124074 | source=vosk | rms=458 | updated_at=1787915500.0790472 | frequency_hz=400.0
- [2026-08-28 19:11:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915500.6055205 | source=vosk | rms=458 | updated_at=1787915500.0790472 | frequency_hz=400.0
- [2026-08-28 19:11:40] operator / voice_transcript_partial / voice: what he wanted a good one only been more
  meta: kind=partial | timestamp=1787915500.6311443 | source=vosk | rms=458 | updated_at=1787915500.0790472 | frequency_hz=400.0
- [2026-08-28 19:11:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915500.8559606 | source=vosk | rms=634 | updated_at=1787915500.8559606 | frequency_hz=400.0
- [2026-08-28 19:11:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915501.360608 | source=vosk | rms=634 | updated_at=1787915500.8559606 | frequency_hz=400.0
- [2026-08-28 19:11:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915503.1349373 | source=vosk | rms=634 | updated_at=1787915500.8559606 | frequency_hz=400.0
- [2026-08-28 19:11:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915503.3557796 | source=vosk | rms=634 | updated_at=1787915500.8559606 | frequency_hz=400.0
- [2026-08-28 19:11:43] operator / voice_transcript_final / voice: what he wanted a good one only but more
  meta: kind=final | timestamp=1787915503.7648518 | source=final | rms=634 | updated_at=1787915500.8559606 | frequency_hz=400.0
- [2026-08-28 19:11:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915503.9307249 | source=vosk | rms=634 | updated_at=1787915500.8559606 | frequency_hz=400.0
- [2026-08-28 19:11:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915503.9307249 | source=vosk | rms=634 | updated_at=1787915500.8559606 | frequency_hz=400.0
- [2026-08-28 19:11:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915504.3607213 | source=vosk | rms=634 | updated_at=1787915500.8559606 | frequency_hz=400.0
- [2026-08-28 19:11:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915508.105557 | source=vosk | rms=634 | updated_at=1787915500.8559606 | frequency_hz=400.0
- [2026-08-28 19:11:49] operator / voice_transcript_partial / voice: it's
  meta: kind=partial | timestamp=1787915509.2100503 | source=vosk | rms=1201 | updated_at=1787915509.1417866 | frequency_hz=400.0
- [2026-08-28 19:11:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915509.8850043 | source=vosk | rms=1201 | updated_at=1787915509.1417866 | frequency_hz=400.0
- [2026-08-28 19:11:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915510.1054494 | source=vosk | rms=1201 | updated_at=1787915509.1417866 | frequency_hz=400.0
- [2026-08-28 19:11:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915510.358284 | source=vosk | rms=538 | updated_at=1787915510.358284 | frequency_hz=400.0
- [2026-08-28 19:11:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915510.883203 | source=vosk | rms=538 | updated_at=1787915510.358284 | frequency_hz=400.0
- [2026-08-28 19:11:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915512.10592 | source=vosk | rms=1202 | updated_at=1787915512.10592 | frequency_hz=400.0
- [2026-08-28 19:11:52] operator / voice_transcript_final / voice: thanks
  meta: kind=final | timestamp=1787915512.3951132 | source=final | rms=1202 | updated_at=1787915512.10592 | frequency_hz=400.0
- [2026-08-28 19:11:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915512.4247339 | source=vosk | rms=1202 | updated_at=1787915512.10592 | frequency_hz=400.0
- [2026-08-28 19:11:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915512.8557882 | source=vosk | rms=1202 | updated_at=1787915512.10592 | frequency_hz=400.0
- [2026-08-28 19:11:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915513.1062229 | source=vosk | rms=1202 | updated_at=1787915512.10592 | frequency_hz=400.0
- [2026-08-28 19:11:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915514.1063132 | source=vosk | rms=785 | updated_at=1787915513.6079063 | frequency_hz=400.0
- [2026-08-28 19:11:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915514.357263 | source=vosk | rms=1200 | updated_at=1787915514.356751 | frequency_hz=400.0
- [2026-08-28 19:11:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915515.6069071 | source=vosk | rms=406 | updated_at=1787915515.105908 | frequency_hz=400.0
- [2026-08-28 19:11:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915517.1054997 | source=vosk | rms=1206 | updated_at=1787915517.1054997 | frequency_hz=400.0
- [2026-08-28 19:11:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915517.8851712 | source=vosk | rms=1206 | updated_at=1787915517.1054997 | frequency_hz=400.0
- [2026-08-28 19:11:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915518.1058388 | source=vosk | rms=1201 | updated_at=1787915518.1058388 | frequency_hz=400.0
- [2026-08-28 19:11:59] operator / voice_transcript_partial / voice: so what are
  meta: kind=partial | timestamp=1787915519.4645853 | source=vosk | rms=401 | updated_at=1787915519.4116173 | frequency_hz=400.0
- [2026-08-28 19:11:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915519.605687 | source=vosk | rms=1088 | updated_at=1787915519.605687 | frequency_hz=400.0
- [2026-08-28 19:11:59] operator / voice_transcript_partial / voice: so when are we going
  meta: kind=partial | timestamp=1787915519.7102804 | source=vosk | rms=1088 | updated_at=1787915519.605687 | frequency_hz=400.0
- [2026-08-28 19:11:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915519.856134 | source=vosk | rms=1088 | updated_at=1787915519.605687 | frequency_hz=400.0
- [2026-08-28 19:11:59] operator / voice_transcript_partial / voice: so when are we going to
  meta: kind=partial | timestamp=1787915519.882461 | source=vosk | rms=1088 | updated_at=1787915519.605687 | frequency_hz=400.0
- [2026-08-28 19:12:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915520.358753 | source=vosk | rms=437 | updated_at=1787915520.358753 | frequency_hz=400.0
- [2026-08-28 19:12:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915520.8564284 | source=vosk | rms=437 | updated_at=1787915520.358753 | frequency_hz=400.0
- [2026-08-28 19:12:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915521.112173 | source=vosk | rms=437 | updated_at=1787915520.358753 | frequency_hz=400.0
- [2026-08-28 19:12:01] operator / voice_transcript_partial / voice: so when are we going to know
  meta: kind=partial | timestamp=1787915521.1537104 | source=vosk | rms=437 | updated_at=1787915520.358753 | frequency_hz=400.0
- [2026-08-28 19:12:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915521.3713865 | source=vosk | rms=363 | updated_at=1787915521.3713865 | frequency_hz=400.0
- [2026-08-28 19:12:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915521.6059034 | source=vosk | rms=363 | updated_at=1787915521.3713865 | frequency_hz=400.0
- [2026-08-28 19:12:01] operator / voice_transcript_partial / voice: so when are we going to no avail
  meta: kind=partial | timestamp=1787915521.6365964 | source=vosk | rms=363 | updated_at=1787915521.3713865 | frequency_hz=400.0
- [2026-08-28 19:12:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915521.8558755 | source=vosk | rms=1042 | updated_at=1787915521.8558755 | frequency_hz=400.0
- [2026-08-28 19:12:01] operator / voice_transcript_partial / voice: so when are we going to go over and over
  meta: kind=partial | timestamp=1787915521.8937225 | source=vosk | rms=1042 | updated_at=1787915521.8558755 | frequency_hz=400.0
- [2026-08-28 19:12:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915522.106692 | source=vosk | rms=564 | updated_at=1787915522.106692 | frequency_hz=400.0
- [2026-08-28 19:12:02] operator / voice_transcript_partial / voice: so when are we going to go over and over the
  meta: kind=partial | timestamp=1787915522.1329987 | source=vosk | rms=564 | updated_at=1787915522.106692 | frequency_hz=400.0
- [2026-08-28 19:12:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915522.3753276 | source=vosk | rms=564 | updated_at=1787915522.106692 | frequency_hz=400.0
- [2026-08-28 19:12:02] operator / voice_transcript_partial / voice: so when are we going to go over and over the logical of
  meta: kind=partial | timestamp=1787915522.484306 | source=vosk | rms=564 | updated_at=1787915522.106692 | frequency_hz=400.0
- [2026-08-28 19:12:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915522.6059122 | source=vosk | rms=377 | updated_at=1787915522.6059122 | frequency_hz=400.0
- [2026-08-28 19:12:02] operator / voice_transcript_partial / voice: so when are we going to go over and over the last coloccini
  meta: kind=partial | timestamp=1787915522.6516547 | source=vosk | rms=377 | updated_at=1787915522.6059122 | frequency_hz=400.0
- [2026-08-28 19:12:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915522.8558824 | source=vosk | rms=377 | updated_at=1787915522.6059122 | frequency_hz=400.0
- [2026-08-28 19:12:02] operator / voice_transcript_partial / voice: so when are we going to go over and over the last galaxy but the
  meta: kind=partial | timestamp=1787915522.8957345 | source=vosk | rms=377 | updated_at=1787915522.6059122 | frequency_hz=400.0
- [2026-08-28 19:12:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915523.1066086 | source=vosk | rms=629 | updated_at=1787915523.1056054 | frequency_hz=400.0
- [2026-08-28 19:12:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915523.6122212 | source=vosk | rms=629 | updated_at=1787915523.1056054 | frequency_hz=400.0
- [2026-08-28 19:12:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915523.8555026 | source=vosk | rms=629 | updated_at=1787915523.1056054 | frequency_hz=400.0
- [2026-08-28 19:12:03] operator / voice_transcript_partial / voice: so when are we going to go over and over the last galaxy but they
  meta: kind=partial | timestamp=1787915523.8810377 | source=vosk | rms=629 | updated_at=1787915523.1056054 | frequency_hz=400.0
- [2026-08-28 19:12:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915524.1058662 | source=vosk | rms=629 | updated_at=1787915523.1056054 | frequency_hz=400.0
- [2026-08-28 19:12:04] operator / voice_transcript_partial / voice: so when are we going to go over and over the last galaxy but the pay up
  meta: kind=partial | timestamp=1787915524.1493618 | source=vosk | rms=629 | updated_at=1787915523.1056054 | frequency_hz=400.0
- [2026-08-28 19:12:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915524.3558755 | source=vosk | rms=880 | updated_at=1787915524.3558755 | frequency_hz=400.0
- [2026-08-28 19:12:04] operator / voice_transcript_partial / voice: so when are we going to go over and over the last galaxy but the pay was
  meta: kind=partial | timestamp=1787915524.3819208 | source=vosk | rms=880 | updated_at=1787915524.3558755 | frequency_hz=400.0
- [2026-08-28 19:12:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915524.63597 | source=vosk | rms=880 | updated_at=1787915524.3558755 | frequency_hz=400.0
- [2026-08-28 19:12:04] operator / voice_transcript_partial / voice: so when are we going to go over and over the last galaxy but the pay was behind
  meta: kind=partial | timestamp=1787915524.6709065 | source=vosk | rms=880 | updated_at=1787915524.3558755 | frequency_hz=400.0
- [2026-08-28 19:12:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915524.9213946 | source=vosk | rms=1203 | updated_at=1787915524.9213946 | frequency_hz=400.0
- [2026-08-28 19:12:05] operator / voice_transcript_partial / voice: so when are we going to go over and over the last galaxy but the pay was be
  meta: kind=partial | timestamp=1787915525.0225804 | source=vosk | rms=1203 | updated_at=1787915524.9213946 | frequency_hz=400.0
- [2026-08-28 19:12:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915525.1271842 | source=vosk | rms=613 | updated_at=1787915525.1271842 | frequency_hz=400.0
- [2026-08-28 19:12:05] operator / voice_transcript_partial / voice: so when are we going to go over and over the last galaxy but the pay was be holding
  meta: kind=partial | timestamp=1787915525.2140145 | source=vosk | rms=613 | updated_at=1787915525.1271842 | frequency_hz=400.0
- [2026-08-28 19:12:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915525.3568096 | source=vosk | rms=613 | updated_at=1787915525.1271842 | frequency_hz=400.0
- [2026-08-28 19:12:05] operator / voice_transcript_partial / voice: so when are we going to go over and over the last galaxy but the day that was me how bout
  meta: kind=partial | timestamp=1787915525.424155 | source=vosk | rms=613 | updated_at=1787915525.1271842 | frequency_hz=400.0
- [2026-08-28 19:12:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915525.608313 | source=vosk | rms=368 | updated_at=1787915525.608313 | frequency_hz=400.0
- [2026-08-28 19:12:05] operator / voice_transcript_partial / voice: so when are we going to go over and over the last galaxy but the day that was me how bout you
  meta: kind=partial | timestamp=1787915525.6435103 | source=vosk | rms=368 | updated_at=1787915525.608313 | frequency_hz=400.0
- [2026-08-28 19:12:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915526.1273103 | source=vosk | rms=533 | updated_at=1787915526.1273103 | frequency_hz=400.0
- [2026-08-28 19:12:06] operator / voice_transcript_partial / voice: so when are we going to go over and over the last galaxy but the day that was me how bout you know
  meta: kind=partial | timestamp=1787915526.2082317 | source=vosk | rms=533 | updated_at=1787915526.1273103 | frequency_hz=400.0
- [2026-08-28 19:12:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915526.8601782 | source=vosk | rms=559 | updated_at=1787915526.8601782 | frequency_hz=400.0
- [2026-08-28 19:12:06] operator / voice_transcript_partial / voice: so when are we going to go over and over the last galaxy but the pay was be holding power unit on
  meta: kind=partial | timestamp=1787915526.9539287 | source=vosk | rms=559 | updated_at=1787915526.8601782 | frequency_hz=400.0
- [2026-08-28 19:12:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915527.1103177 | source=vosk | rms=357 | updated_at=1787915527.1103177 | frequency_hz=400.0
- [2026-08-28 19:12:07] operator / voice_transcript_partial / voice: so when are we going to go over and over the last galaxy but the day that was me how bout you know don't really
  meta: kind=partial | timestamp=1787915527.2076404 | source=vosk | rms=357 | updated_at=1787915527.1103177 | frequency_hz=400.0
- [2026-08-28 19:12:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915527.6648185 | source=vosk | rms=357 | updated_at=1787915527.1103177 | frequency_hz=400.0
- [2026-08-28 19:12:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915528.356235 | source=vosk | rms=357 | updated_at=1787915527.1103177 | frequency_hz=400.0
- [2026-08-28 19:12:08] operator / voice_transcript_partial / voice: so when are we going to go over and over the last galaxy but the day that was me how bout you know don't really know
  meta: kind=partial | timestamp=1787915528.4105165 | source=vosk | rms=357 | updated_at=1787915527.1103177 | frequency_hz=400.0
- [2026-08-28 19:12:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915528.6067104 | source=vosk | rms=357 | updated_at=1787915527.1103177 | frequency_hz=400.0
- [2026-08-28 19:12:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915528.856388 | source=vosk | rms=365 | updated_at=1787915528.856388 | frequency_hz=400.0
- [2026-08-28 19:12:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915529.1059518 | source=vosk | rms=365 | updated_at=1787915528.856388 | frequency_hz=400.0
- [2026-08-28 19:12:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915529.6083896 | source=vosk | rms=365 | updated_at=1787915528.856388 | frequency_hz=400.0
- [2026-08-28 19:12:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915530.6283667 | source=vosk | rms=403 | updated_at=1787915530.6283667 | frequency_hz=400.0
- [2026-08-28 19:12:10] operator / voice_transcript_final / voice: so when are we going to go over and over the last galaxy but the pay that was me how bout you know don t really know
  meta: kind=final | timestamp=1787915530.9284031 | source=final | rms=403 | updated_at=1787915530.6283667 | frequency_hz=400.0
- [2026-08-28 19:12:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915531.267684 | source=vosk | rms=403 | updated_at=1787915530.6283667 | frequency_hz=400.0
- [2026-08-28 19:12:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915531.267684 | source=vosk | rms=403 | updated_at=1787915530.6283667 | frequency_hz=400.0
- [2026-08-28 19:12:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915531.86436 | source=vosk | rms=387 | updated_at=1787915531.2786956 | frequency_hz=400.0
- [2026-08-28 19:12:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915533.60626 | source=vosk | rms=377 | updated_at=1787915533.60626 | frequency_hz=400.0
- [2026-08-28 19:12:13] operator / voice_transcript_partial / voice: when you're already
  meta: kind=partial | timestamp=1787915533.6413636 | source=vosk | rms=377 | updated_at=1787915533.60626 | frequency_hz=400.0
- [2026-08-28 19:12:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915534.10713 | source=vosk | rms=377 | updated_at=1787915533.60626 | frequency_hz=400.0
- [2026-08-28 19:12:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915534.4685402 | source=vosk | rms=596 | updated_at=1787915534.4685402 | frequency_hz=400.0
- [2026-08-28 19:12:14] operator / voice_transcript_partial / voice: when you're older a lot
  meta: kind=partial | timestamp=1787915534.520848 | source=vosk | rms=596 | updated_at=1787915534.4685402 | frequency_hz=400.0
- [2026-08-28 19:12:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915535.1066768 | source=vosk | rms=596 | updated_at=1787915534.4685402 | frequency_hz=400.0
- [2026-08-28 19:12:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915535.6068556 | source=vosk | rms=596 | updated_at=1787915534.4685402 | frequency_hz=400.0
- [2026-08-28 19:12:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915535.8558993 | source=vosk | rms=596 | updated_at=1787915534.4685402 | frequency_hz=400.0
- [2026-08-28 19:12:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915536.3565614 | source=vosk | rms=596 | updated_at=1787915534.4685402 | frequency_hz=400.0
- [2026-08-28 19:12:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915536.6067576 | source=vosk | rms=910 | updated_at=1787915536.6067576 | frequency_hz=400.0
- [2026-08-28 19:12:16] operator / voice_transcript_final / voice: when you re already lot
  meta: kind=final | timestamp=1787915536.9430285 | source=final | rms=910 | updated_at=1787915536.6067576 | frequency_hz=400.0
- [2026-08-28 19:12:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915537.0561678 | source=vosk | rms=910 | updated_at=1787915536.6067576 | frequency_hz=400.0
- [2026-08-28 19:12:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915537.87843 | source=vosk | rms=910 | updated_at=1787915536.6067576 | frequency_hz=400.0
- [2026-08-28 19:12:19] operator / voice_transcript_partial / voice: a wonderful relationship
  meta: kind=partial | timestamp=1787915539.193658 | source=vosk | rms=378 | updated_at=1787915538.8762538 | frequency_hz=400.0
- [2026-08-28 19:12:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915539.411405 | source=vosk | rms=378 | updated_at=1787915538.8762538 | frequency_hz=400.0
- [2026-08-28 19:12:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915539.876427 | source=vosk | rms=378 | updated_at=1787915538.8762538 | frequency_hz=400.0
- [2026-08-28 19:12:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915540.6310706 | source=vosk | rms=927 | updated_at=1787915540.6310706 | frequency_hz=400.0
- [2026-08-28 19:12:21] operator / voice_transcript_partial / voice: wonderful will return to work
  meta: kind=partial | timestamp=1787915541.9524632 | source=vosk | rms=743 | updated_at=1787915541.3767343 | frequency_hz=400.0
- [2026-08-28 19:12:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915542.137892 | source=vosk | rms=656 | updated_at=1787915542.137892 | frequency_hz=400.0
- [2026-08-28 19:12:22] operator / voice_transcript_partial / voice: where
  meta: kind=partial | timestamp=1787915542.1751184 | source=vosk | rms=656 | updated_at=1787915542.137892 | frequency_hz=400.0
- [2026-08-28 19:12:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915542.3962283 | source=vosk | rms=656 | updated_at=1787915542.137892 | frequency_hz=400.0
- [2026-08-28 19:12:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915542.631508 | source=vosk | rms=483 | updated_at=1787915542.631508 | frequency_hz=400.0
- [2026-08-28 19:12:22] operator / voice_transcript_final / voice: wonderful will really to
  meta: kind=final | timestamp=1787915542.987044 | source=final | rms=483 | updated_at=1787915542.631508 | frequency_hz=400.0
- [2026-08-28 19:12:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915543.0856526 | source=vosk | rms=483 | updated_at=1787915542.631508 | frequency_hz=400.0
- [2026-08-28 19:12:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915543.0856526 | source=vosk | rms=483 | updated_at=1787915542.631508 | frequency_hz=400.0
- [2026-08-28 19:12:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915543.6856883 | source=vosk | rms=471 | updated_at=1787915543.1462343 | frequency_hz=400.0
- [2026-08-28 19:12:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915543.927832 | source=vosk | rms=471 | updated_at=1787915543.1462343 | frequency_hz=400.0
- [2026-08-28 19:12:25] operator / voice_transcript_partial / voice: digital recorder and
  meta: kind=partial | timestamp=1787915545.0164962 | source=vosk | rms=903 | updated_at=1787915544.9120073 | frequency_hz=400.0
- [2026-08-28 19:12:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915545.1306884 | source=vosk | rms=1196 | updated_at=1787915545.129689 | frequency_hz=400.0
- [2026-08-28 19:12:25] operator / voice_transcript_partial / voice: the street journal about
  meta: kind=partial | timestamp=1787915545.1644819 | source=vosk | rms=1196 | updated_at=1787915545.129689 | frequency_hz=400.0
- [2026-08-28 19:12:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915545.3848553 | source=vosk | rms=1203 | updated_at=1787915545.3848553 | frequency_hz=400.0
- [2026-08-28 19:12:25] operator / voice_transcript_partial / voice: the street journal or not and
  meta: kind=partial | timestamp=1787915545.4508593 | source=vosk | rms=1203 | updated_at=1787915545.3848553 | frequency_hz=400.0
- [2026-08-28 19:12:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915545.626831 | source=vosk | rms=1202 | updated_at=1787915545.626831 | frequency_hz=400.0
- [2026-08-28 19:12:25] operator / voice_transcript_partial / voice: the street journal enough and
  meta: kind=partial | timestamp=1787915545.655361 | source=vosk | rms=1202 | updated_at=1787915545.626831 | frequency_hz=400.0
- [2026-08-28 19:12:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915545.8767676 | source=vosk | rms=789 | updated_at=1787915545.8767676 | frequency_hz=400.0
- [2026-08-28 19:12:25] operator / voice_transcript_partial / voice: the street journal enough and bowl but
  meta: kind=partial | timestamp=1787915545.9186943 | source=vosk | rms=789 | updated_at=1787915545.8767676 | frequency_hz=400.0
- [2026-08-28 19:12:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915546.1261258 | source=vosk | rms=789 | updated_at=1787915545.8767676 | frequency_hz=400.0
- [2026-08-28 19:12:26] operator / voice_transcript_partial / voice: the street journal or not an open
  meta: kind=partial | timestamp=1787915546.1690145 | source=vosk | rms=789 | updated_at=1787915545.8767676 | frequency_hz=400.0
- [2026-08-28 19:12:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915546.6271057 | source=vosk | rms=619 | updated_at=1787915546.6271057 | frequency_hz=400.0
- [2026-08-28 19:12:26] operator / voice_transcript_partial / voice: the street journal enough and bowling
  meta: kind=partial | timestamp=1787915546.6461487 | source=vosk | rms=619 | updated_at=1787915546.6271057 | frequency_hz=400.0
- [2026-08-28 19:12:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915546.8778207 | source=vosk | rms=619 | updated_at=1787915546.6271057 | frequency_hz=400.0
- [2026-08-28 19:12:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915547.1266294 | source=vosk | rms=684 | updated_at=1787915547.1266294 | frequency_hz=400.0
- [2026-08-28 19:12:27] operator / voice_transcript_partial / voice: the street journal enough and bowling now lives in
  meta: kind=partial | timestamp=1787915547.1726089 | source=vosk | rms=684 | updated_at=1787915547.1266294 | frequency_hz=400.0
- [2026-08-28 19:12:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915547.6408808 | source=vosk | rms=684 | updated_at=1787915547.1266294 | frequency_hz=400.0
- [2026-08-28 19:12:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915548.627118 | source=vosk | rms=402 | updated_at=1787915548.627118 | frequency_hz=400.0
- [2026-08-28 19:12:28] operator / voice_transcript_partial / voice: the street journal enough and bowling not lose yourself
  meta: kind=partial | timestamp=1787915548.7078857 | source=vosk | rms=402 | updated_at=1787915548.627118 | frequency_hz=400.0
- [2026-08-28 19:12:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915549.126753 | source=vosk | rms=402 | updated_at=1787915548.627118 | frequency_hz=400.0
- [2026-08-28 19:12:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915549.3927832 | source=vosk | rms=385 | updated_at=1787915549.3927832 | frequency_hz=400.0
- [2026-08-28 19:12:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915549.877967 | source=vosk | rms=385 | updated_at=1787915549.3927832 | frequency_hz=400.0
- [2026-08-28 19:12:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915550.6389017 | source=vosk | rms=385 | updated_at=1787915549.3927832 | frequency_hz=400.0
- [2026-08-28 19:12:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915550.8759623 | source=vosk | rms=519 | updated_at=1787915550.8759623 | frequency_hz=400.0
- [2026-08-28 19:12:30] operator / voice_transcript_partial / voice: the street journal enough and bowling not lose yourself in
  meta: kind=partial | timestamp=1787915550.9368997 | source=vosk | rms=519 | updated_at=1787915550.8759623 | frequency_hz=400.0
- [2026-08-28 19:12:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915551.128732 | source=vosk | rms=552 | updated_at=1787915551.128732 | frequency_hz=400.0
- [2026-08-28 19:12:31] operator / voice_transcript_partial / voice: the street journal enough and bowling not lose yourself in should
  meta: kind=partial | timestamp=1787915551.1767018 | source=vosk | rms=552 | updated_at=1787915551.128732 | frequency_hz=400.0
- [2026-08-28 19:12:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915551.631464 | source=vosk | rms=552 | updated_at=1787915551.128732 | frequency_hz=400.0
- [2026-08-28 19:12:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915553.1315086 | source=vosk | rms=552 | updated_at=1787915551.128732 | frequency_hz=400.0
- [2026-08-28 19:12:33] operator / voice_transcript_partial / voice: the street journal enough and bowling not lose yourself well
  meta: kind=partial | timestamp=1787915553.1848505 | source=vosk | rms=552 | updated_at=1787915551.128732 | frequency_hz=400.0
- [2026-08-28 19:12:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915553.3819418 | source=vosk | rms=552 | updated_at=1787915551.128732 | frequency_hz=400.0
- [2026-08-28 19:12:33] operator / voice_transcript_partial / voice: the street journal enough and bowling not lose yourself in should go
  meta: kind=partial | timestamp=1787915553.4541554 | source=vosk | rms=552 | updated_at=1787915551.128732 | frequency_hz=400.0
- [2026-08-28 19:12:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915553.6272087 | source=vosk | rms=839 | updated_at=1787915553.6272087 | frequency_hz=400.0
- [2026-08-28 19:12:33] operator / voice_transcript_partial / voice: the street journal enough and bowling not lose yourself in should go on and on
  meta: kind=partial | timestamp=1787915553.6807973 | source=vosk | rms=839 | updated_at=1787915553.6272087 | frequency_hz=400.0
- [2026-08-28 19:12:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915553.9082692 | source=vosk | rms=321 | updated_at=1787915553.9082692 | frequency_hz=400.0
- [2026-08-28 19:12:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915554.1342652 | source=vosk | rms=391 | updated_at=1787915554.1342652 | frequency_hz=400.0
- [2026-08-28 19:12:34] operator / voice_transcript_partial / voice: the street journal enough and bowling not lose yourself in should go on john doe or
  meta: kind=partial | timestamp=1787915554.1587927 | source=vosk | rms=391 | updated_at=1787915554.1342652 | frequency_hz=400.0
- [2026-08-28 19:12:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915554.3841462 | source=vosk | rms=541 | updated_at=1787915554.3841462 | frequency_hz=400.0
- [2026-08-28 19:12:34] operator / voice_transcript_partial / voice: the street journal enough and bowling not lose yourself in should go on john bolton wanderers
  meta: kind=partial | timestamp=1787915554.4400022 | source=vosk | rms=541 | updated_at=1787915554.3841462 | frequency_hz=400.0
- [2026-08-28 19:12:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915554.8764174 | source=vosk | rms=456 | updated_at=1787915554.8764174 | frequency_hz=400.0
- [2026-08-28 19:12:34] operator / voice_transcript_partial / voice: the street journal enough and bowling not lose yourself in should go on john bolton was
  meta: kind=partial | timestamp=1787915554.9500306 | source=vosk | rms=456 | updated_at=1787915554.8764174 | frequency_hz=400.0
- [2026-08-28 19:12:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915555.4216464 | source=vosk | rms=456 | updated_at=1787915554.8764174 | frequency_hz=400.0
- [2026-08-28 19:12:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915555.6391883 | source=vosk | rms=456 | updated_at=1787915554.8764174 | frequency_hz=400.0
- [2026-08-28 19:12:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915555.8839083 | source=vosk | rms=456 | updated_at=1787915554.8764174 | frequency_hz=400.0
- [2026-08-28 19:12:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915556.1382127 | source=vosk | rms=796 | updated_at=1787915556.1382127 | frequency_hz=400.0
- [2026-08-28 19:12:37] operator / voice_transcript_final / voice: and street journal or and bowling not close yourself in should go on john bolton was
  meta: kind=final | timestamp=1787915557.1878848 | source=final | rms=796 | updated_at=1787915556.1382127 | frequency_hz=400.0
- [2026-08-28 19:12:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915558.362138 | source=vosk | rms=796 | updated_at=1787915556.1382127 | frequency_hz=400.0
- [2026-08-28 19:12:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915558.362138 | source=vosk | rms=561 | updated_at=1787915558.362138 | frequency_hz=400.0
- [2026-08-28 19:12:38] operator / voice_transcript_partial / voice: former
  meta: kind=partial | timestamp=1787915558.4335086 | source=vosk | rms=490 | updated_at=1787915558.4059415 | frequency_hz=400.0
- [2026-08-28 19:12:38] operator / voice_transcript_partial / voice: former fsb
  meta: kind=partial | timestamp=1787915558.475135 | source=vosk | rms=944 | updated_at=1787915558.4335086 | frequency_hz=400.0
- [2026-08-28 19:12:38] operator / voice_transcript_partial / voice: former smokers
  meta: kind=partial | timestamp=1787915558.520256 | source=vosk | rms=753 | updated_at=1787915558.475135 | frequency_hz=400.0
- [2026-08-28 19:12:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915558.5647242 | source=vosk | rms=501 | updated_at=1787915558.520256 | frequency_hz=400.0
- [2026-08-28 19:12:38] operator / voice_transcript_partial / voice: former after school club
  meta: kind=partial | timestamp=1787915558.5647242 | source=vosk | rms=501 | updated_at=1787915558.520256 | frequency_hz=400.0
- [2026-08-28 19:12:38] operator / voice_transcript_final / voice: former smoker
  meta: kind=final | timestamp=1787915558.8716338 | source=final | rms=951 | updated_at=1787915558.5647242 | frequency_hz=400.0
- [2026-08-28 19:12:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915558.9059663 | source=vosk | rms=1098 | updated_at=1787915558.9059663 | frequency_hz=400.0
- [2026-08-28 19:12:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915563.6269345 | source=vosk | rms=828 | updated_at=1787915562.876508 | frequency_hz=400.0
- [2026-08-28 19:12:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915564.3800414 | source=vosk | rms=584 | updated_at=1787915564.3800414 | frequency_hz=400.0
- [2026-08-28 19:12:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915564.8777394 | source=vosk | rms=584 | updated_at=1787915564.3800414 | frequency_hz=400.0
- [2026-08-28 19:12:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915565.877472 | source=vosk | rms=901 | updated_at=1787915565.877472 | frequency_hz=400.0
- [2026-08-28 19:12:46] operator / voice_transcript_partial / voice: valuable to
  meta: kind=partial | timestamp=1787915566.1749017 | source=vosk | rms=801 | updated_at=1787915566.1352663 | frequency_hz=400.0
- [2026-08-28 19:12:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915566.4321444 | source=vosk | rms=801 | updated_at=1787915566.1352663 | frequency_hz=400.0
- [2026-08-28 19:12:46] operator / voice_transcript_partial / voice: look up on
  meta: kind=partial | timestamp=1787915566.4802911 | source=vosk | rms=801 | updated_at=1787915566.1352663 | frequency_hz=400.0
- [2026-08-28 19:12:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915566.62721 | source=vosk | rms=801 | updated_at=1787915566.1352663 | frequency_hz=400.0
- [2026-08-28 19:12:46] operator / voice_transcript_partial / voice: look up on you
  meta: kind=partial | timestamp=1787915566.7138834 | source=vosk | rms=801 | updated_at=1787915566.1352663 | frequency_hz=400.0
- [2026-08-28 19:12:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915566.9071543 | source=vosk | rms=801 | updated_at=1787915566.1352663 | frequency_hz=400.0
- [2026-08-28 19:12:46] operator / voice_transcript_partial / voice: look up on a new
  meta: kind=partial | timestamp=1787915566.9767332 | source=vosk | rms=801 | updated_at=1787915566.1352663 | frequency_hz=400.0
- [2026-08-28 19:12:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915567.4063563 | source=vosk | rms=801 | updated_at=1787915566.1352663 | frequency_hz=400.0
- [2026-08-28 19:12:47] operator / voice_transcript_partial / voice: look up on a nuclear
  meta: kind=partial | timestamp=1787915567.472763 | source=vosk | rms=801 | updated_at=1787915566.1352663 | frequency_hz=400.0
- [2026-08-28 19:12:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915568.1752138 | source=vosk | rms=801 | updated_at=1787915566.1352663 | frequency_hz=400.0
- [2026-08-28 19:12:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915568.3762891 | source=vosk | rms=801 | updated_at=1787915566.1352663 | frequency_hz=400.0
- [2026-08-28 19:12:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915568.6268106 | source=vosk | rms=517 | updated_at=1787915568.6268106 | frequency_hz=400.0
- [2026-08-28 19:12:48] operator / voice_transcript_partial / voice: look up on you get a proper
  meta: kind=partial | timestamp=1787915568.6574304 | source=vosk | rms=517 | updated_at=1787915568.6268106 | frequency_hz=400.0
- [2026-08-28 19:12:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915569.1268296 | source=vosk | rms=517 | updated_at=1787915568.6268106 | frequency_hz=400.0
- [2026-08-28 19:12:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915570.3774846 | source=vosk | rms=517 | updated_at=1787915568.6268106 | frequency_hz=400.0
- [2026-08-28 19:12:50] operator / voice_transcript_partial / voice: look up on you get a proper what's the
  meta: kind=partial | timestamp=1787915570.4071019 | source=vosk | rms=517 | updated_at=1787915568.6268106 | frequency_hz=400.0
- [2026-08-28 19:12:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915570.6339366 | source=vosk | rms=1120 | updated_at=1787915570.6339366 | frequency_hz=400.0
- [2026-08-28 19:12:50] operator / voice_transcript_partial / voice: look up on you get a proper won't stop your
  meta: kind=partial | timestamp=1787915570.6736624 | source=vosk | rms=1120 | updated_at=1787915570.6339366 | frequency_hz=400.0
- [2026-08-28 19:12:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915570.877677 | source=vosk | rms=1113 | updated_at=1787915570.877677 | frequency_hz=400.0
- [2026-08-28 19:12:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915571.1642516 | source=vosk | rms=1113 | updated_at=1787915570.877677 | frequency_hz=400.0
- [2026-08-28 19:12:51] operator / voice_transcript_partial / voice: look up on you get a proper what's stopping you don't
  meta: kind=partial | timestamp=1787915571.193377 | source=vosk | rms=1113 | updated_at=1787915570.877677 | frequency_hz=400.0
- [2026-08-28 19:12:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915571.6275225 | source=vosk | rms=847 | updated_at=1787915571.6275225 | frequency_hz=400.0
- [2026-08-28 19:12:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915571.876959 | source=vosk | rms=1206 | updated_at=1787915571.876959 | frequency_hz=400.0
- [2026-08-28 19:12:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915572.127584 | source=vosk | rms=1206 | updated_at=1787915571.876959 | frequency_hz=400.0
- [2026-08-28 19:12:52] operator / voice_transcript_final / voice: to look up on you get a proper won t stop you do don t
  meta: kind=final | timestamp=1787915572.4069228 | source=final | rms=1206 | updated_at=1787915571.876959 | frequency_hz=400.0
- [2026-08-28 19:12:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915573.10931 | source=vosk | rms=1206 | updated_at=1787915571.876959 | frequency_hz=400.0
- [2026-08-28 19:12:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915573.10931 | source=vosk | rms=1206 | updated_at=1787915571.876959 | frequency_hz=400.0
- [2026-08-28 19:12:53] operator / voice_transcript_partial / voice: oh
  meta: kind=partial | timestamp=1787915573.1257763 | source=vosk | rms=1206 | updated_at=1787915571.876959 | frequency_hz=400.0
- [2026-08-28 19:12:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915573.406544 | source=vosk | rms=1206 | updated_at=1787915571.876959 | frequency_hz=400.0
- [2026-08-28 19:12:53] operator / voice_transcript_partial / voice: open your
  meta: kind=partial | timestamp=1787915573.4301424 | source=vosk | rms=1206 | updated_at=1787915571.876959 | frequency_hz=400.0
- [2026-08-28 19:12:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915573.6273131 | source=vosk | rms=1206 | updated_at=1787915571.876959 | frequency_hz=400.0
- [2026-08-28 19:12:53] operator / voice_transcript_partial / voice: open your your
  meta: kind=partial | timestamp=1787915573.6474648 | source=vosk | rms=1206 | updated_at=1787915571.876959 | frequency_hz=400.0
- [2026-08-28 19:12:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915574.1284516 | source=vosk | rms=1206 | updated_at=1787915571.876959 | frequency_hz=400.0
- [2026-08-28 19:12:54] operator / voice_transcript_partial / voice: open your your there's not
  meta: kind=partial | timestamp=1787915574.2022066 | source=vosk | rms=1206 | updated_at=1787915571.876959 | frequency_hz=400.0
- [2026-08-28 19:12:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915574.403098 | source=vosk | rms=1204 | updated_at=1787915574.403098 | frequency_hz=400.0
- [2026-08-28 19:12:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915574.62867 | source=vosk | rms=808 | updated_at=1787915574.62867 | frequency_hz=400.0
- [2026-08-28 19:12:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915575.127154 | source=vosk | rms=808 | updated_at=1787915574.62867 | frequency_hz=400.0
- [2026-08-28 19:12:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915575.8769574 | source=vosk | rms=1200 | updated_at=1787915575.8769574 | frequency_hz=400.0
- [2026-08-28 19:12:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915576.1277394 | source=vosk | rms=1200 | updated_at=1787915576.1277394 | frequency_hz=400.0
- [2026-08-28 19:12:56] operator / voice_transcript_final / voice: open your your there s no
  meta: kind=final | timestamp=1787915576.42039 | source=final | rms=1200 | updated_at=1787915576.1277394 | frequency_hz=400.0
- [2026-08-28 19:12:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915576.7464027 | source=vosk | rms=1200 | updated_at=1787915576.1277394 | frequency_hz=400.0
- [2026-08-28 19:12:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915577.4141436 | source=vosk | rms=1200 | updated_at=1787915576.1277394 | frequency_hz=400.0
- [2026-08-28 19:12:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915577.8770967 | source=vosk | rms=1200 | updated_at=1787915576.1277394 | frequency_hz=400.0
- [2026-08-28 19:12:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915578.1436648 | source=vosk | rms=1200 | updated_at=1787915576.1277394 | frequency_hz=400.0
- [2026-08-28 19:12:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915578.6285076 | source=vosk | rms=1200 | updated_at=1787915576.1277394 | frequency_hz=400.0
- [2026-08-28 19:12:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915579.6279008 | source=vosk | rms=1171 | updated_at=1787915579.6279008 | frequency_hz=400.0
- [2026-08-28 19:13:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915580.1284664 | source=vosk | rms=1171 | updated_at=1787915579.6279008 | frequency_hz=400.0
- [2026-08-28 19:13:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915581.6272902 | source=vosk | rms=817 | updated_at=1787915581.6272902 | frequency_hz=400.0
- [2026-08-28 19:13:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915582.917547 | source=vosk | rms=1562 | updated_at=1787915581.882767 | frequency_hz=400.0
- [2026-08-28 19:13:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915585.1274252 | source=vosk | rms=1562 | updated_at=1787915581.882767 | frequency_hz=400.0
- [2026-08-28 19:13:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915585.6271384 | source=vosk | rms=1562 | updated_at=1787915581.882767 | frequency_hz=400.0
- [2026-08-28 19:13:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915588.1397705 | source=vosk | rms=633 | updated_at=1787915588.1397705 | frequency_hz=400.0
- [2026-08-28 19:13:08] operator / voice_transcript_partial / voice: on an
  meta: kind=partial | timestamp=1787915588.746443 | source=vosk | rms=656 | updated_at=1787915588.6562836 | frequency_hz=400.0
- [2026-08-28 19:13:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915588.9200938 | source=vosk | rms=656 | updated_at=1787915588.6562836 | frequency_hz=400.0
- [2026-08-28 19:13:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915589.6280942 | source=vosk | rms=656 | updated_at=1787915588.6562836 | frequency_hz=400.0
- [2026-08-28 19:13:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915591.656584 | source=vosk | rms=656 | updated_at=1787915588.6562836 | frequency_hz=400.0
- [2026-08-28 19:13:11] operator / voice_transcript_partial / voice: among us that are
  meta: kind=partial | timestamp=1787915591.8690624 | source=vosk | rms=656 | updated_at=1787915588.6562836 | frequency_hz=400.0
- [2026-08-28 19:13:12] operator / voice_transcript_partial / voice: about an hour and a nice little
  meta: kind=partial | timestamp=1787915592.0007706 | source=vosk | rms=1003 | updated_at=1787915591.8778465 | frequency_hz=400.0
- [2026-08-28 19:13:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915592.1275744 | source=vosk | rms=355 | updated_at=1787915592.1275744 | frequency_hz=400.0
- [2026-08-28 19:13:12] operator / voice_transcript_partial / voice: on an understanding of
  meta: kind=partial | timestamp=1787915592.177678 | source=vosk | rms=355 | updated_at=1787915592.1275744 | frequency_hz=400.0
- [2026-08-28 19:13:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915592.377302 | source=vosk | rms=373 | updated_at=1787915592.377302 | frequency_hz=400.0
- [2026-08-28 19:13:12] operator / voice_transcript_partial / voice: on an understanding of report
  meta: kind=partial | timestamp=1787915592.482543 | source=vosk | rms=373 | updated_at=1787915592.377302 | frequency_hz=400.0
- [2026-08-28 19:13:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915593.1282427 | source=vosk | rms=373 | updated_at=1787915592.377302 | frequency_hz=400.0
- [2026-08-28 19:13:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915594.1402686 | source=vosk | rms=373 | updated_at=1787915592.377302 | frequency_hz=400.0
- [2026-08-28 19:13:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915594.627787 | source=vosk | rms=373 | updated_at=1787915592.377302 | frequency_hz=400.0
- [2026-08-28 19:13:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915596.9061792 | source=vosk | rms=373 | updated_at=1787915592.377302 | frequency_hz=400.0
- [2026-08-28 19:13:16] operator / voice_transcript_partial / voice: on an understanding of report also
  meta: kind=partial | timestamp=1787915596.9655657 | source=vosk | rms=373 | updated_at=1787915592.377302 | frequency_hz=400.0
- [2026-08-28 19:13:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915597.146397 | source=vosk | rms=331 | updated_at=1787915597.146397 | frequency_hz=400.0
- [2026-08-28 19:13:17] operator / voice_transcript_final / voice: about an on an of report
  meta: kind=final | timestamp=1787915597.562008 | source=final | rms=331 | updated_at=1787915597.146397 | frequency_hz=400.0
- [2026-08-28 19:13:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915597.6988912 | source=vosk | rms=331 | updated_at=1787915597.146397 | frequency_hz=400.0
- [2026-08-28 19:13:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915597.6988912 | source=vosk | rms=331 | updated_at=1787915597.146397 | frequency_hz=400.0
- [2026-08-28 19:13:18] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1787915598.0369499 | source=vosk | rms=331 | updated_at=1787915597.146397 | frequency_hz=400.0
- [2026-08-28 19:13:18] operator / voice_transcript_partial / voice: you want
  meta: kind=partial | timestamp=1787915598.075697 | source=vosk | rms=331 | updated_at=1787915597.146397 | frequency_hz=400.0
- [2026-08-28 19:13:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915598.6283793 | source=vosk | rms=521 | updated_at=1787915598.6283793 | frequency_hz=400.0
- [2026-08-28 19:13:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915599.1352086 | source=vosk | rms=390 | updated_at=1787915599.1352086 | frequency_hz=400.0
- [2026-08-28 19:13:19] operator / voice_transcript_final / voice: you want
  meta: kind=final | timestamp=1787915599.4074082 | source=final | rms=390 | updated_at=1787915599.1352086 | frequency_hz=400.0
- [2026-08-28 19:13:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915599.628159 | source=vosk | rms=390 | updated_at=1787915599.1352086 | frequency_hz=400.0
- [2026-08-28 19:13:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915600.8863943 | source=vosk | rms=390 | updated_at=1787915599.1352086 | frequency_hz=400.0
- [2026-08-28 19:13:21] operator / voice_transcript_partial / voice: you
  meta: kind=partial | timestamp=1787915601.416395 | source=vosk | rms=403 | updated_at=1787915601.378166 | frequency_hz=400.0
- [2026-08-28 19:13:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915601.62772 | source=vosk | rms=249 | updated_at=1787915601.62772 | frequency_hz=400.0
- [2026-08-28 19:13:21] operator / voice_transcript_partial / voice: you know
  meta: kind=partial | timestamp=1787915601.6528032 | source=vosk | rms=249 | updated_at=1787915601.62772 | frequency_hz=400.0
- [2026-08-28 19:13:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915601.8783689 | source=vosk | rms=398 | updated_at=1787915601.8783689 | frequency_hz=400.0
- [2026-08-28 19:13:21] operator / voice_transcript_partial / voice: yeah but
  meta: kind=partial | timestamp=1787915601.9095302 | source=vosk | rms=398 | updated_at=1787915601.8783689 | frequency_hz=400.0
- [2026-08-28 19:13:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915602.128054 | source=vosk | rms=363 | updated_at=1787915602.128054 | frequency_hz=400.0
- [2026-08-28 19:13:22] operator / voice_transcript_partial / voice: yeah but because
  meta: kind=partial | timestamp=1787915602.1981466 | source=vosk | rms=363 | updated_at=1787915602.128054 | frequency_hz=400.0
- [2026-08-28 19:13:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915602.3812518 | source=vosk | rms=363 | updated_at=1787915602.128054 | frequency_hz=400.0
- [2026-08-28 19:13:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915602.6279705 | source=vosk | rms=385 | updated_at=1787915602.6279705 | frequency_hz=400.0
- [2026-08-28 19:13:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915602.8771198 | source=vosk | rms=385 | updated_at=1787915602.6279705 | frequency_hz=400.0
- [2026-08-28 19:13:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915603.3783915 | source=vosk | rms=385 | updated_at=1787915602.6279705 | frequency_hz=400.0
- [2026-08-28 19:13:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915603.8774545 | source=vosk | rms=385 | updated_at=1787915602.6279705 | frequency_hz=400.0
- [2026-08-28 19:13:23] operator / voice_transcript_partial / voice: yeah but because i didn't want
  meta: kind=partial | timestamp=1787915603.9219327 | source=vosk | rms=385 | updated_at=1787915602.6279705 | frequency_hz=400.0
- [2026-08-28 19:13:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915604.378524 | source=vosk | rms=630 | updated_at=1787915604.378524 | frequency_hz=400.0
- [2026-08-28 19:13:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915604.8784943 | source=vosk | rms=482 | updated_at=1787915604.8784943 | frequency_hz=400.0
- [2026-08-28 19:13:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915605.129183 | source=vosk | rms=442 | updated_at=1787915605.129183 | frequency_hz=400.0
- [2026-08-28 19:13:25] operator / voice_transcript_final / voice: yeah but because i didn t want
  meta: kind=final | timestamp=1787915605.6874845 | source=final | rms=442 | updated_at=1787915605.129183 | frequency_hz=400.0
- [2026-08-28 19:13:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915606.014966 | source=vosk | rms=442 | updated_at=1787915605.129183 | frequency_hz=400.0
- [2026-08-28 19:13:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915606.014966 | source=vosk | rms=364 | updated_at=1787915606.014966 | frequency_hz=400.0
- [2026-08-28 19:13:26] operator / voice_transcript_partial / voice: recipients
  meta: kind=partial | timestamp=1787915606.2535765 | source=vosk | rms=623 | updated_at=1787915606.1638765 | frequency_hz=400.0
- [2026-08-28 19:13:26] operator / voice_transcript_partial / voice: recent
  meta: kind=partial | timestamp=1787915606.3163316 | source=vosk | rms=481 | updated_at=1787915606.2535765 | frequency_hz=400.0
- [2026-08-28 19:13:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915606.4577672 | source=vosk | rms=508 | updated_at=1787915606.4037678 | frequency_hz=400.0
- [2026-08-28 19:13:26] operator / voice_transcript_partial / voice: i usually performed on
  meta: kind=partial | timestamp=1787915606.4577672 | source=vosk | rms=508 | updated_at=1787915606.4037678 | frequency_hz=400.0
- [2026-08-28 19:13:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915606.6666903 | source=vosk | rms=1138 | updated_at=1787915606.633403 | frequency_hz=400.0
- [2026-08-28 19:13:26] operator / voice_transcript_partial / voice: it therefore not
  meta: kind=partial | timestamp=1787915606.6666903 | source=vosk | rms=1138 | updated_at=1787915606.633403 | frequency_hz=400.0
- [2026-08-28 19:13:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915606.8783286 | source=vosk | rms=917 | updated_at=1787915606.8783286 | frequency_hz=400.0
- [2026-08-28 19:13:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915607.131505 | source=vosk | rms=1202 | updated_at=1787915607.131505 | frequency_hz=400.0
- [2026-08-28 19:13:27] operator / voice_transcript_partial / voice: it therefore not just
  meta: kind=partial | timestamp=1787915607.235052 | source=vosk | rms=1202 | updated_at=1787915607.131505 | frequency_hz=400.0
- [2026-08-28 19:13:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915607.404149 | source=vosk | rms=1200 | updated_at=1787915607.404149 | frequency_hz=400.0
- [2026-08-28 19:13:27] operator / voice_transcript_partial / voice: it therefore not just go
  meta: kind=partial | timestamp=1787915607.4506624 | source=vosk | rms=1200 | updated_at=1787915607.404149 | frequency_hz=400.0
- [2026-08-28 19:13:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915607.6393065 | source=vosk | rms=323 | updated_at=1787915607.6393065 | frequency_hz=400.0
- [2026-08-28 19:13:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915607.904922 | source=vosk | rms=1204 | updated_at=1787915607.904922 | frequency_hz=400.0
- [2026-08-28 19:13:27] operator / voice_transcript_partial / voice: it therefore not just go he was able
  meta: kind=partial | timestamp=1787915607.9746127 | source=vosk | rms=1204 | updated_at=1787915607.904922 | frequency_hz=400.0
- [2026-08-28 19:13:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915608.128539 | source=vosk | rms=528 | updated_at=1787915608.128539 | frequency_hz=400.0
- [2026-08-28 19:13:28] operator / voice_transcript_partial / voice: it therefore not just going as a group
  meta: kind=partial | timestamp=1787915608.2101269 | source=vosk | rms=528 | updated_at=1787915608.128539 | frequency_hz=400.0
- [2026-08-28 19:13:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915608.3774815 | source=vosk | rms=922 | updated_at=1787915608.3774815 | frequency_hz=400.0
- [2026-08-28 19:13:28] operator / voice_transcript_partial / voice: it therefore not just go he was a brilliant
  meta: kind=partial | timestamp=1787915608.4425728 | source=vosk | rms=922 | updated_at=1787915608.3774815 | frequency_hz=400.0
- [2026-08-28 19:13:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915608.647528 | source=vosk | rms=1200 | updated_at=1787915608.647528 | frequency_hz=400.0
- [2026-08-28 19:13:28] operator / voice_transcript_partial / voice: it therefore not just go he was a brilliant of
  meta: kind=partial | timestamp=1787915608.7136946 | source=vosk | rms=1200 | updated_at=1787915608.647528 | frequency_hz=400.0
- [2026-08-28 19:13:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915608.8777046 | source=vosk | rms=454 | updated_at=1787915608.8777046 | frequency_hz=400.0
- [2026-08-28 19:13:28] operator / voice_transcript_partial / voice: it therefore not just go he was a prisoner of war
  meta: kind=partial | timestamp=1787915608.9447732 | source=vosk | rms=454 | updated_at=1787915608.8777046 | frequency_hz=400.0
- [2026-08-28 19:13:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915609.1291175 | source=vosk | rms=317 | updated_at=1787915609.1291175 | frequency_hz=400.0
- [2026-08-28 19:13:29] operator / voice_transcript_partial / voice: it therefore not just go he was a brilliant of you know what about
  meta: kind=partial | timestamp=1787915609.1761935 | source=vosk | rms=317 | updated_at=1787915609.1291175 | frequency_hz=400.0
- [2026-08-28 19:13:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915609.3885028 | source=vosk | rms=519 | updated_at=1787915609.3885028 | frequency_hz=400.0
- [2026-08-28 19:13:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915609.8833265 | source=vosk | rms=519 | updated_at=1787915609.3885028 | frequency_hz=400.0
- [2026-08-28 19:13:29] operator / voice_transcript_partial / voice: it therefore not just go he was a brilliant of you know what i would love
  meta: kind=partial | timestamp=1787915609.9702082 | source=vosk | rms=519 | updated_at=1787915609.3885028 | frequency_hz=400.0
- [2026-08-28 19:13:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915610.133384 | source=vosk | rms=519 | updated_at=1787915609.3885028 | frequency_hz=400.0
- [2026-08-28 19:13:30] operator / voice_transcript_partial / voice: it therefore not just go he was a brilliant of you know what about
  meta: kind=partial | timestamp=1787915610.1832507 | source=vosk | rms=519 | updated_at=1787915609.3885028 | frequency_hz=400.0
- [2026-08-28 19:13:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915610.6282947 | source=vosk | rms=519 | updated_at=1787915609.3885028 | frequency_hz=400.0
- [2026-08-28 19:13:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915610.8784842 | source=vosk | rms=311 | updated_at=1787915610.8784842 | frequency_hz=400.0
- [2026-08-28 19:13:31] operator / voice_transcript_final / voice: it therefore not book they just go he was a brilliant of you know what about but level
  meta: kind=final | timestamp=1787915611.2841222 | source=final | rms=311 | updated_at=1787915610.8784842 | frequency_hz=400.0
- [2026-08-28 19:13:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915611.6554646 | source=vosk | rms=311 | updated_at=1787915610.8784842 | frequency_hz=400.0
- [2026-08-28 19:13:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915611.6554646 | source=vosk | rms=196 | updated_at=1787915611.6554646 | frequency_hz=400.0
- [2026-08-28 19:13:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915612.1286368 | source=vosk | rms=196 | updated_at=1787915611.6554646 | frequency_hz=400.0
- [2026-08-28 19:13:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915612.3783493 | source=vosk | rms=725 | updated_at=1787915612.3783493 | frequency_hz=400.0
- [2026-08-28 19:13:33] operator / voice_transcript_partial / voice: i can remember
  meta: kind=partial | timestamp=1787915613.913517 | source=vosk | rms=381 | updated_at=1787915613.8783627 | frequency_hz=400.0
- [2026-08-28 19:13:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915614.1299317 | source=vosk | rms=381 | updated_at=1787915613.8783627 | frequency_hz=400.0
- [2026-08-28 19:13:34] operator / voice_transcript_partial / voice: oh
  meta: kind=partial | timestamp=1787915614.483641 | source=vosk | rms=850 | updated_at=1787915614.377738 | frequency_hz=400.0
- [2026-08-28 19:13:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915614.6365583 | source=vosk | rms=685 | updated_at=1787915614.6365583 | frequency_hz=400.0
- [2026-08-28 19:13:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915614.8780015 | source=vosk | rms=536 | updated_at=1787915614.8780015 | frequency_hz=400.0
- [2026-08-28 19:13:34] operator / voice_transcript_partial / voice: i can remember when i
  meta: kind=partial | timestamp=1787915614.9797359 | source=vosk | rms=536 | updated_at=1787915614.8780015 | frequency_hz=400.0
- [2026-08-28 19:13:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915615.3781455 | source=vosk | rms=499 | updated_at=1787915615.3781455 | frequency_hz=400.0
- [2026-08-28 19:13:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915615.6336024 | source=vosk | rms=499 | updated_at=1787915615.3781455 | frequency_hz=400.0
- [2026-08-28 19:13:35] operator / voice_transcript_partial / voice: i can remember when i was still
  meta: kind=partial | timestamp=1787915615.7294629 | source=vosk | rms=499 | updated_at=1787915615.3781455 | frequency_hz=400.0
- [2026-08-28 19:13:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915616.3784707 | source=vosk | rms=499 | updated_at=1787915615.3781455 | frequency_hz=400.0
- [2026-08-28 19:13:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915620.1284513 | source=vosk | rms=502 | updated_at=1787915620.1284513 | frequency_hz=400.0
- [2026-08-28 19:13:40] operator / voice_transcript_partial / voice: i can remember when i was still in
  meta: kind=partial | timestamp=1787915620.217916 | source=vosk | rms=502 | updated_at=1787915620.1284513 | frequency_hz=400.0
- [2026-08-28 19:13:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915620.8941195 | source=vosk | rms=502 | updated_at=1787915620.1284513 | frequency_hz=400.0
- [2026-08-28 19:13:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915621.3797128 | source=vosk | rms=453 | updated_at=1787915621.3797128 | frequency_hz=400.0
- [2026-08-28 19:13:41] operator / voice_transcript_partial / voice: i can remember when i certainly didn't
  meta: kind=partial | timestamp=1787915621.4376755 | source=vosk | rms=453 | updated_at=1787915621.3797128 | frequency_hz=400.0
- [2026-08-28 19:13:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915621.6565259 | source=vosk | rms=453 | updated_at=1787915621.3797128 | frequency_hz=400.0
- [2026-08-28 19:13:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915621.8789575 | source=vosk | rms=362 | updated_at=1787915621.8789575 | frequency_hz=400.0
- [2026-08-28 19:13:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915622.1281698 | source=vosk | rms=330 | updated_at=1787915622.1281698 | frequency_hz=400.0
- [2026-08-28 19:13:42] operator / voice_transcript_final / voice: i can remember when i believe it
  meta: kind=final | timestamp=1787915622.5259235 | source=final | rms=330 | updated_at=1787915622.1281698 | frequency_hz=400.0
- [2026-08-28 19:13:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915622.6444576 | source=vosk | rms=330 | updated_at=1787915622.1281698 | frequency_hz=400.0
- [2026-08-28 19:13:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915622.6444576 | source=vosk | rms=972 | updated_at=1787915622.6444576 | frequency_hz=400.0
- [2026-08-28 19:13:42] operator / voice_transcript_partial / voice: people
  meta: kind=partial | timestamp=1787915622.6772273 | source=vosk | rms=972 | updated_at=1787915622.6444576 | frequency_hz=400.0
- [2026-08-28 19:13:42] operator / voice_transcript_partial / voice: people that the
  meta: kind=partial | timestamp=1787915622.757124 | source=vosk | rms=535 | updated_at=1787915622.6772273 | frequency_hz=400.0
- [2026-08-28 19:13:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915622.8883238 | source=vosk | rms=949 | updated_at=1787915622.8883238 | frequency_hz=400.0
- [2026-08-28 19:13:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915623.378354 | source=vosk | rms=949 | updated_at=1787915622.8883238 | frequency_hz=400.0
- [2026-08-28 19:13:43] operator / voice_transcript_partial / voice: people that the spot
  meta: kind=partial | timestamp=1787915623.4206123 | source=vosk | rms=949 | updated_at=1787915622.8883238 | frequency_hz=400.0
- [2026-08-28 19:13:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915623.6283557 | source=vosk | rms=765 | updated_at=1787915623.6283557 | frequency_hz=400.0
- [2026-08-28 19:13:43] operator / voice_transcript_partial / voice: people that the spoke of a
  meta: kind=partial | timestamp=1787915623.67303 | source=vosk | rms=765 | updated_at=1787915623.6283557 | frequency_hz=400.0
- [2026-08-28 19:13:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915623.885046 | source=vosk | rms=420 | updated_at=1787915623.885046 | frequency_hz=400.0
- [2026-08-28 19:13:43] operator / voice_transcript_partial / voice: people that the spoke of a good
  meta: kind=partial | timestamp=1787915623.9251835 | source=vosk | rms=420 | updated_at=1787915623.885046 | frequency_hz=400.0
- [2026-08-28 19:13:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915624.1291564 | source=vosk | rms=1201 | updated_at=1787915624.1291564 | frequency_hz=400.0
- [2026-08-28 19:13:44] operator / voice_transcript_partial / voice: people that the spoke of a break
  meta: kind=partial | timestamp=1787915624.1818037 | source=vosk | rms=1201 | updated_at=1787915624.1291564 | frequency_hz=400.0
- [2026-08-28 19:13:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915624.6327565 | source=vosk | rms=1201 | updated_at=1787915624.1291564 | frequency_hz=400.0
- [2026-08-28 19:13:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915624.8781989 | source=vosk | rms=1201 | updated_at=1787915624.1291564 | frequency_hz=400.0
- [2026-08-28 19:13:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915625.1291854 | source=vosk | rms=436 | updated_at=1787915625.1291854 | frequency_hz=400.0
- [2026-08-28 19:13:45] operator / voice_transcript_partial / voice: people that the spoke of a break out in
  meta: kind=partial | timestamp=1787915625.1845038 | source=vosk | rms=436 | updated_at=1787915625.1291854 | frequency_hz=400.0
- [2026-08-28 19:13:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915625.4152462 | source=vosk | rms=436 | updated_at=1787915625.1291854 | frequency_hz=400.0
- [2026-08-28 19:13:45] operator / voice_transcript_partial / voice: people that the spoke of a break out
  meta: kind=partial | timestamp=1787915625.468436 | source=vosk | rms=436 | updated_at=1787915625.1291854 | frequency_hz=400.0
- [2026-08-28 19:13:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915625.628955 | source=vosk | rms=391 | updated_at=1787915625.628955 | frequency_hz=400.0
- [2026-08-28 19:13:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915626.1282043 | source=vosk | rms=655 | updated_at=1787915626.1282043 | frequency_hz=400.0
- [2026-08-28 19:13:46] operator / voice_transcript_partial / voice: people that the spoke of a break out of nowhere
  meta: kind=partial | timestamp=1787915626.1676977 | source=vosk | rms=655 | updated_at=1787915626.1282043 | frequency_hz=400.0
- [2026-08-28 19:13:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915626.3786168 | source=vosk | rms=639 | updated_at=1787915626.3786168 | frequency_hz=400.0
- [2026-08-28 19:13:46] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lowest
  meta: kind=partial | timestamp=1787915626.4665403 | source=vosk | rms=639 | updated_at=1787915626.3786168 | frequency_hz=400.0
- [2026-08-28 19:13:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915626.6295247 | source=vosk | rms=1026 | updated_at=1787915626.6295247 | frequency_hz=400.0
- [2026-08-28 19:13:46] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social
  meta: kind=partial | timestamp=1787915626.6771922 | source=vosk | rms=1026 | updated_at=1787915626.6295247 | frequency_hz=400.0
- [2026-08-28 19:13:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915626.8785937 | source=vosk | rms=756 | updated_at=1787915626.8785937 | frequency_hz=400.0
- [2026-08-28 19:13:46] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet
  meta: kind=partial | timestamp=1787915626.9357734 | source=vosk | rms=756 | updated_at=1787915626.8785937 | frequency_hz=400.0
- [2026-08-28 19:13:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915627.13195 | source=vosk | rms=917 | updated_at=1787915627.13195 | frequency_hz=400.0
- [2026-08-28 19:13:47] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave
  meta: kind=partial | timestamp=1787915627.1746297 | source=vosk | rms=917 | updated_at=1787915627.13195 | frequency_hz=400.0
- [2026-08-28 19:13:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915627.3789294 | source=vosk | rms=614 | updated_at=1787915627.3789294 | frequency_hz=400.0
- [2026-08-28 19:13:47] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the
  meta: kind=partial | timestamp=1787915627.5097032 | source=vosk | rms=614 | updated_at=1787915627.3789294 | frequency_hz=400.0
- [2026-08-28 19:13:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915627.6596084 | source=vosk | rms=614 | updated_at=1787915627.3789294 | frequency_hz=400.0
- [2026-08-28 19:13:47] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the gun
  meta: kind=partial | timestamp=1787915627.7308147 | source=vosk | rms=614 | updated_at=1787915627.3789294 | frequency_hz=400.0
- [2026-08-28 19:13:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915628.3850281 | source=vosk | rms=614 | updated_at=1787915627.3789294 | frequency_hz=400.0
- [2026-08-28 19:13:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915629.1284888 | source=vosk | rms=605 | updated_at=1787915629.1284888 | frequency_hz=400.0
- [2026-08-28 19:13:49] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour
  meta: kind=partial | timestamp=1787915629.2117846 | source=vosk | rms=605 | updated_at=1787915629.1284888 | frequency_hz=400.0
- [2026-08-28 19:13:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915629.3790493 | source=vosk | rms=1007 | updated_at=1787915629.3790493 | frequency_hz=400.0
- [2026-08-28 19:13:49] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago
  meta: kind=partial | timestamp=1787915629.412398 | source=vosk | rms=1007 | updated_at=1787915629.3790493 | frequency_hz=400.0
- [2026-08-28 19:13:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915629.6284544 | source=vosk | rms=1203 | updated_at=1787915629.6284544 | frequency_hz=400.0
- [2026-08-28 19:13:49] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally
  meta: kind=partial | timestamp=1787915629.6876025 | source=vosk | rms=1203 | updated_at=1787915629.6284544 | frequency_hz=400.0
- [2026-08-28 19:13:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915629.8897533 | source=vosk | rms=1200 | updated_at=1787915629.8897533 | frequency_hz=400.0
- [2026-08-28 19:13:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915630.3796873 | source=vosk | rms=721 | updated_at=1787915630.3796873 | frequency_hz=400.0
- [2026-08-28 19:13:50] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about
  meta: kind=partial | timestamp=1787915630.4328597 | source=vosk | rms=721 | updated_at=1787915630.3796873 | frequency_hz=400.0
- [2026-08-28 19:13:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915630.6298184 | source=vosk | rms=1202 | updated_at=1787915630.6298184 | frequency_hz=400.0
- [2026-08-28 19:13:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915630.8795762 | source=vosk | rms=862 | updated_at=1787915630.8795762 | frequency_hz=400.0
- [2026-08-28 19:13:50] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about other
  meta: kind=partial | timestamp=1787915630.957139 | source=vosk | rms=862 | updated_at=1787915630.8795762 | frequency_hz=400.0
- [2026-08-28 19:13:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915631.1484637 | source=vosk | rms=1201 | updated_at=1787915631.1484637 | frequency_hz=400.0
- [2026-08-28 19:13:51] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred
  meta: kind=partial | timestamp=1787915631.213016 | source=vosk | rms=1201 | updated_at=1787915631.1484637 | frequency_hz=400.0
- [2026-08-28 19:13:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915631.3791242 | source=vosk | rms=1200 | updated_at=1787915631.3791242 | frequency_hz=400.0
- [2026-08-28 19:13:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915631.6283066 | source=vosk | rms=934 | updated_at=1787915631.6283066 | frequency_hz=400.0
- [2026-08-28 19:13:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915631.8783088 | source=vosk | rms=914 | updated_at=1787915631.8783088 | frequency_hz=400.0
- [2026-08-28 19:13:51] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred
  meta: kind=partial | timestamp=1787915631.9243836 | source=vosk | rms=914 | updated_at=1787915631.8783088 | frequency_hz=400.0
- [2026-08-28 19:13:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915632.1287916 | source=vosk | rms=1205 | updated_at=1787915632.1287916 | frequency_hz=400.0
- [2026-08-28 19:13:52] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and
  meta: kind=partial | timestamp=1787915632.154601 | source=vosk | rms=1205 | updated_at=1787915632.1287916 | frequency_hz=400.0
- [2026-08-28 19:13:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915632.628953 | source=vosk | rms=491 | updated_at=1787915632.628953 | frequency_hz=400.0
- [2026-08-28 19:13:52] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and eight
  meta: kind=partial | timestamp=1787915632.6682527 | source=vosk | rms=491 | updated_at=1787915632.628953 | frequency_hz=400.0
- [2026-08-28 19:13:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915633.1280863 | source=vosk | rms=491 | updated_at=1787915632.628953 | frequency_hz=400.0
- [2026-08-28 19:13:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915633.3869884 | source=vosk | rms=709 | updated_at=1787915633.3869884 | frequency_hz=400.0
- [2026-08-28 19:13:53] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred i don't know
  meta: kind=partial | timestamp=1787915633.4786572 | source=vosk | rms=709 | updated_at=1787915633.3869884 | frequency_hz=400.0
- [2026-08-28 19:13:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915633.6286461 | source=vosk | rms=709 | updated_at=1787915633.3869884 | frequency_hz=400.0
- [2026-08-28 19:13:53] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred on a home
  meta: kind=partial | timestamp=1787915633.697335 | source=vosk | rms=709 | updated_at=1787915633.3869884 | frequency_hz=400.0
- [2026-08-28 19:13:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915633.902958 | source=vosk | rms=1003 | updated_at=1787915633.902958 | frequency_hz=400.0
- [2026-08-28 19:13:53] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and all the
  meta: kind=partial | timestamp=1787915633.9735625 | source=vosk | rms=1003 | updated_at=1787915633.902958 | frequency_hz=400.0
- [2026-08-28 19:13:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915634.1632078 | source=vosk | rms=1200 | updated_at=1787915634.161691 | frequency_hz=400.0
- [2026-08-28 19:13:54] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and all the book
  meta: kind=partial | timestamp=1787915634.2109091 | source=vosk | rms=1200 | updated_at=1787915634.161691 | frequency_hz=400.0
- [2026-08-28 19:13:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915634.4033248 | source=vosk | rms=1067 | updated_at=1787915634.4033248 | frequency_hz=400.0
- [2026-08-28 19:13:54] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and all the book publishing
  meta: kind=partial | timestamp=1787915634.4571056 | source=vosk | rms=1067 | updated_at=1787915634.4033248 | frequency_hz=400.0
- [2026-08-28 19:13:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915634.6400204 | source=vosk | rms=771 | updated_at=1787915634.6400204 | frequency_hz=400.0
- [2026-08-28 19:13:54] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and eight open up a book published an
  meta: kind=partial | timestamp=1787915634.7139874 | source=vosk | rms=771 | updated_at=1787915634.6400204 | frequency_hz=400.0
- [2026-08-28 19:13:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915634.9044592 | source=vosk | rms=1201 | updated_at=1787915634.9044592 | frequency_hz=400.0
- [2026-08-28 19:13:55] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and eight open up a book published an adjustment
  meta: kind=partial | timestamp=1787915635.0077667 | source=vosk | rms=1201 | updated_at=1787915634.9044592 | frequency_hz=400.0
- [2026-08-28 19:13:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915635.128331 | source=vosk | rms=1201 | updated_at=1787915635.128331 | frequency_hz=400.0
- [2026-08-28 19:13:55] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and eight open up a book published an article just look at
  meta: kind=partial | timestamp=1787915635.202973 | source=vosk | rms=1201 | updated_at=1787915635.128331 | frequency_hz=400.0
- [2026-08-28 19:13:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915635.6334848 | source=vosk | rms=1201 | updated_at=1787915635.128331 | frequency_hz=400.0
- [2026-08-28 19:13:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915635.9083898 | source=vosk | rms=1201 | updated_at=1787915635.128331 | frequency_hz=400.0
- [2026-08-28 19:13:55] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and all the book publishing that looks like
  meta: kind=partial | timestamp=1787915635.968298 | source=vosk | rms=1201 | updated_at=1787915635.128331 | frequency_hz=400.0
- [2026-08-28 19:13:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915636.3859746 | source=vosk | rms=1201 | updated_at=1787915635.128331 | frequency_hz=400.0
- [2026-08-28 19:13:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915637.1299663 | source=vosk | rms=1201 | updated_at=1787915635.128331 | frequency_hz=400.0
- [2026-08-28 19:13:57] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and eight open up a book published an article just look at
  meta: kind=partial | timestamp=1787915637.197415 | source=vosk | rms=1201 | updated_at=1787915635.128331 | frequency_hz=400.0
- [2026-08-28 19:13:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915637.3790102 | source=vosk | rms=575 | updated_at=1787915637.3790102 | frequency_hz=400.0
- [2026-08-28 19:13:57] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and eight open up a book published not let us look i know
  meta: kind=partial | timestamp=1787915637.4115672 | source=vosk | rms=575 | updated_at=1787915637.3790102 | frequency_hz=400.0
- [2026-08-28 19:13:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915637.6287189 | source=vosk | rms=1202 | updated_at=1787915637.6287189 | frequency_hz=400.0
- [2026-08-28 19:13:57] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and eight open up a book published an article just walk out with no choice
  meta: kind=partial | timestamp=1787915637.7069461 | source=vosk | rms=1202 | updated_at=1787915637.6287189 | frequency_hz=400.0
- [2026-08-28 19:13:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915637.8788712 | source=vosk | rms=859 | updated_at=1787915637.8788712 | frequency_hz=400.0
- [2026-08-28 19:13:57] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and eight open up a book published an article just look at no charge
  meta: kind=partial | timestamp=1787915637.9074779 | source=vosk | rms=859 | updated_at=1787915637.8788712 | frequency_hz=400.0
- [2026-08-28 19:13:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915638.3790705 | source=vosk | rms=859 | updated_at=1787915637.8788712 | frequency_hz=400.0
- [2026-08-28 19:13:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915638.6286924 | source=vosk | rms=881 | updated_at=1787915638.6286924 | frequency_hz=400.0
- [2026-08-28 19:13:58] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and eight open up a book published an article just what i saw
  meta: kind=partial | timestamp=1787915638.6568096 | source=vosk | rms=881 | updated_at=1787915638.6286924 | frequency_hz=400.0
- [2026-08-28 19:13:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915638.8828964 | source=vosk | rms=1056 | updated_at=1787915638.8828964 | frequency_hz=400.0
- [2026-08-28 19:13:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915639.3812065 | source=vosk | rms=1056 | updated_at=1787915638.8828964 | frequency_hz=400.0
- [2026-08-28 19:14:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915640.878367 | source=vosk | rms=620 | updated_at=1787915640.878367 | frequency_hz=400.0
- [2026-08-28 19:14:00] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and eight open up a book published an article just walk out with no child died
  meta: kind=partial | timestamp=1787915640.9129179 | source=vosk | rms=620 | updated_at=1787915640.878367 | frequency_hz=400.0
- [2026-08-28 19:14:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915641.1519408 | source=vosk | rms=620 | updated_at=1787915640.878367 | frequency_hz=400.0
- [2026-08-28 19:14:01] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and eight open up a book published an article just walk out with no child died and
  meta: kind=partial | timestamp=1787915641.1986947 | source=vosk | rms=620 | updated_at=1787915640.878367 | frequency_hz=400.0
- [2026-08-28 19:14:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915641.379199 | source=vosk | rms=502 | updated_at=1787915641.379199 | frequency_hz=400.0
- [2026-08-28 19:14:01] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and eight open up a book published an article just walk out with no child died suddenly
  meta: kind=partial | timestamp=1787915641.4447088 | source=vosk | rms=502 | updated_at=1787915641.379199 | frequency_hz=400.0
- [2026-08-28 19:14:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915641.6311967 | source=vosk | rms=502 | updated_at=1787915641.379199 | frequency_hz=400.0
- [2026-08-28 19:14:01] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and eight open up a book published an article just walk out with no child died and civil
  meta: kind=partial | timestamp=1787915641.6909788 | source=vosk | rms=502 | updated_at=1787915641.379199 | frequency_hz=400.0
- [2026-08-28 19:14:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915641.9158523 | source=vosk | rms=885 | updated_at=1787915641.9158523 | frequency_hz=400.0
- [2026-08-28 19:14:01] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and eight open up a book published an article just what i saw guidance of literally
  meta: kind=partial | timestamp=1787915641.9941516 | source=vosk | rms=885 | updated_at=1787915641.9158523 | frequency_hz=400.0
- [2026-08-28 19:14:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915642.145388 | source=vosk | rms=1017 | updated_at=1787915642.145388 | frequency_hz=400.0
- [2026-08-28 19:14:02] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and eight open up a book published an article just walk out with no child died and simple little
  meta: kind=partial | timestamp=1787915642.180094 | source=vosk | rms=1017 | updated_at=1787915642.145388 | frequency_hz=400.0
- [2026-08-28 19:14:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915642.3790085 | source=vosk | rms=708 | updated_at=1787915642.3790085 | frequency_hz=400.0
- [2026-08-28 19:14:02] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and eight open up a book published an article just walk out with no child died and simple little girl for
  meta: kind=partial | timestamp=1787915642.4606667 | source=vosk | rms=708 | updated_at=1787915642.3790085 | frequency_hz=400.0
- [2026-08-28 19:14:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915642.6713839 | source=vosk | rms=1204 | updated_at=1787915642.6713839 | frequency_hz=400.0
- [2026-08-28 19:14:02] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and eight open up a book published an article just walk out with no child died and simple little girls button
  meta: kind=partial | timestamp=1787915642.7342966 | source=vosk | rms=1204 | updated_at=1787915642.6713839 | frequency_hz=400.0
- [2026-08-28 19:14:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915642.8941512 | source=vosk | rms=474 | updated_at=1787915642.8941512 | frequency_hz=400.0
- [2026-08-28 19:14:02] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and eight open up a book published an article just walk out with no child died and simple little girl for an
  meta: kind=partial | timestamp=1787915642.9900947 | source=vosk | rms=474 | updated_at=1787915642.8941512 | frequency_hz=400.0
- [2026-08-28 19:14:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915643.5824044 | source=vosk | rms=1204 | updated_at=1787915643.5824044 | frequency_hz=351.7
- [2026-08-28 19:14:03] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and eight open up a book published an article just walk out with no child died and simple little girls button on how
  meta: kind=partial | timestamp=1787915643.6338334 | source=vosk | rms=1204 | updated_at=1787915643.5824044 | frequency_hz=351.7
- [2026-08-28 19:14:03] operator / voice_transcript_partial / voice: people that the spoke of a break out of the lower social bullet gave it to the got an hour ago personally about a hundred eleven hundred and eight open up a book published an article just walk out with no child died and simple little girl for an ad hoc
  meta: kind=partial | timestamp=1787915643.6830242 | source=vosk | rms=1202 | updated_at=1787915643.6338334 | frequency_hz=351.7
- [2026-08-28 19:14:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915643.9022198 | source=vosk | rms=1203 | updated_at=1787915643.9022198 | frequency_hz=351.7
- [2026-08-28 19:14:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915644.1321769 | source=vosk | rms=1201 | updated_at=1787915644.1321769 | frequency_hz=351.7
- [2026-08-28 19:14:05] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787915645.427369 | source=state | rms=1201 | updated_at=1787915644.1321769 | frequency_hz=351.7
- [2026-08-28 19:14:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915645.8890438 | source=state | rms=1201 | updated_at=1787915644.1321769 | frequency_hz=351.7
- [2026-08-28 19:14:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915645.8900447 | source=vosk | rms=1202 | updated_at=1787915645.8890438 | frequency_hz=351.7
- [2026-08-28 19:14:05] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1787915645.9401891 | source=vosk | rms=1202 | updated_at=1787915645.8890438 | frequency_hz=351.7
- [2026-08-28 19:14:06] operator / voice_transcript_partial / voice: this
  meta: kind=partial | timestamp=1787915646.0561318 | source=vosk | rms=1202 | updated_at=1787915645.9881613 | frequency_hz=351.7
- [2026-08-28 19:14:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915646.0908887 | source=vosk | rms=1202 | updated_at=1787915646.0571318 | frequency_hz=351.7
- [2026-08-28 19:14:06] operator / voice_transcript_partial / voice: disc the
  meta: kind=partial | timestamp=1787915646.0908887 | source=vosk | rms=1202 | updated_at=1787915646.0571318 | frequency_hz=351.7
- [2026-08-28 19:14:06] operator / voice_transcript_partial / voice: disc the hundred
  meta: kind=partial | timestamp=1787915646.1498127 | source=vosk | rms=1044 | updated_at=1787915646.0908887 | frequency_hz=351.7
- [2026-08-28 19:14:06] operator / voice_transcript_partial / voice: disc the hundred dollar
  meta: kind=partial | timestamp=1787915646.2255175 | source=vosk | rms=1201 | updated_at=1787915646.1498127 | frequency_hz=351.7
- [2026-08-28 19:14:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915646.2771883 | source=vosk | rms=1201 | updated_at=1787915646.1498127 | frequency_hz=351.7
- [2026-08-28 19:14:06] operator / voice_transcript_partial / voice: disc the hundred another me how
  meta: kind=partial | timestamp=1787915646.2771883 | source=vosk | rms=1201 | updated_at=1787915646.1498127 | frequency_hz=351.7
- [2026-08-28 19:14:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915646.9026744 | source=vosk | rms=549 | updated_at=1787915646.9026744 | frequency_hz=351.7
- [2026-08-28 19:14:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915647.3789482 | source=vosk | rms=549 | updated_at=1787915646.9026744 | frequency_hz=351.7
- [2026-08-28 19:14:08] operator / voice_transcript_final / voice: disc the hundred another me how
  meta: kind=final | timestamp=1787915648.413698 | source=final | rms=549 | updated_at=1787915646.9026744 | frequency_hz=351.7
- [2026-08-28 19:14:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915648.5711799 | source=vosk | rms=1074 | updated_at=1787915648.5711799 | frequency_hz=351.7
- [2026-08-28 19:14:08] operator / voice_transcript_partial / voice: disc the hundred another me how
  meta: kind=partial | timestamp=1787915648.5826852 | source=vosk | rms=1074 | updated_at=1787915648.5711799 | frequency_hz=351.7
- [2026-08-28 19:14:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915649.1448333 | source=vosk | rms=1074 | updated_at=1787915648.5711799 | frequency_hz=351.7
- [2026-08-28 19:14:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915649.389427 | source=vosk | rms=642 | updated_at=1787915649.389427 | frequency_hz=351.7
- [2026-08-28 19:14:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915649.9217186 | source=vosk | rms=642 | updated_at=1787915649.389427 | frequency_hz=351.7
- [2026-08-28 19:14:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915650.3815362 | source=vosk | rms=632 | updated_at=1787915650.3815362 | frequency_hz=351.7
- [2026-08-28 19:14:10] operator / voice_transcript_final / voice: disc the hundred another me how
  meta: kind=final | timestamp=1787915650.875536 | source=final | rms=632 | updated_at=1787915650.3815362 | frequency_hz=351.7
- [2026-08-28 19:14:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915651.053764 | source=vosk | rms=632 | updated_at=1787915650.3815362 | frequency_hz=351.7
- [2026-08-28 19:14:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915651.1435428 | source=vosk | rms=632 | updated_at=1787915650.3815362 | frequency_hz=351.7
- [2026-08-28 19:14:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915651.6292512 | source=vosk | rms=632 | updated_at=1787915650.3815362 | frequency_hz=351.7
- [2026-08-28 19:14:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915652.6295543 | source=vosk | rms=729 | updated_at=1787915652.6295543 | frequency_hz=351.7
- [2026-08-28 19:14:12] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1787915652.9231741 | source=vosk | rms=729 | updated_at=1787915652.6295543 | frequency_hz=351.7
- [2026-08-28 19:14:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915653.128869 | source=vosk | rms=729 | updated_at=1787915652.6295543 | frequency_hz=351.7
- [2026-08-28 19:14:13] operator / voice_transcript_partial / voice: columbus
  meta: kind=partial | timestamp=1787915653.681323 | source=vosk | rms=695 | updated_at=1787915653.6296017 | frequency_hz=351.7
- [2026-08-28 19:14:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915653.8875399 | source=vosk | rms=1086 | updated_at=1787915653.8865397 | frequency_hz=351.7
- [2026-08-28 19:14:13] operator / voice_transcript_partial / voice: must read
  meta: kind=partial | timestamp=1787915653.9440193 | source=vosk | rms=1086 | updated_at=1787915653.8865397 | frequency_hz=351.7
- [2026-08-28 19:14:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915654.37944 | source=vosk | rms=1086 | updated_at=1787915653.8865397 | frequency_hz=351.7
- [2026-08-28 19:14:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915657.3797045 | source=vosk | rms=1204 | updated_at=1787915657.3797045 | frequency_hz=351.7
- [2026-08-28 19:14:17] operator / voice_transcript_partial / voice: what is what the lucas leiva
  meta: kind=partial | timestamp=1787915657.4521632 | source=vosk | rms=1204 | updated_at=1787915657.3797045 | frequency_hz=351.7
- [2026-08-28 19:14:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915657.878751 | source=vosk | rms=1204 | updated_at=1787915657.3797045 | frequency_hz=351.7
- [2026-08-28 19:14:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915685.8803043 | source=vosk | rms=1204 | updated_at=1787915657.3797045 | frequency_hz=351.7
- [2026-08-28 19:14:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915686.3802414 | source=vosk | rms=1204 | updated_at=1787915657.3797045 | frequency_hz=351.7
- [2026-08-28 19:14:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915687.129466 | source=vosk | rms=143 | updated_at=1787915687.129466 | frequency_hz=351.7
- [2026-08-28 19:14:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915687.3797336 | source=vosk | rms=140 | updated_at=1787915687.3797336 | frequency_hz=351.7
- [2026-08-28 19:14:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915687.8851416 | source=vosk | rms=140 | updated_at=1787915687.3797336 | frequency_hz=351.7
- [2026-08-28 19:14:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915688.143045 | source=vosk | rms=173 | updated_at=1787915688.143045 | frequency_hz=351.7
- [2026-08-28 19:14:48] operator / voice_transcript_final / voice: what is what the lucas leiva
  meta: kind=final | timestamp=1787915688.7739005 | source=final | rms=173 | updated_at=1787915688.143045 | frequency_hz=351.7
- [2026-08-28 19:14:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915689.0133805 | source=vosk | rms=173 | updated_at=1787915688.143045 | frequency_hz=351.7
- [2026-08-28 19:14:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915689.0133805 | source=vosk | rms=170 | updated_at=1787915689.0133805 | frequency_hz=351.7
- [2026-08-28 19:14:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915689.6342852 | source=vosk | rms=170 | updated_at=1787915689.0133805 | frequency_hz=351.7
- [2026-08-28 19:14:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915691.1350546 | source=vosk | rms=170 | updated_at=1787915689.0133805 | frequency_hz=351.7
- [2026-08-28 19:14:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915692.140481 | source=vosk | rms=172 | updated_at=1787915691.6333008 | frequency_hz=351.7
- [2026-08-28 19:14:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915692.402866 | source=vosk | rms=172 | updated_at=1787915691.6333008 | frequency_hz=351.7
- [2026-08-28 19:14:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915692.898614 | source=vosk | rms=172 | updated_at=1787915691.6333008 | frequency_hz=351.7
- [2026-08-28 19:14:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915694.6436794 | source=vosk | rms=172 | updated_at=1787915691.6333008 | frequency_hz=351.7
- [2026-08-28 19:14:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915695.655573 | source=vosk | rms=172 | updated_at=1787915691.6333008 | frequency_hz=351.7
- [2026-08-28 19:14:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915696.6309752 | source=vosk | rms=172 | updated_at=1787915691.6333008 | frequency_hz=351.7
- [2026-08-28 19:14:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915698.9010332 | source=vosk | rms=251 | updated_at=1787915697.6521664 | frequency_hz=351.7
- [2026-08-28 19:14:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915699.155069 | source=vosk | rms=251 | updated_at=1787915697.6521664 | frequency_hz=351.7
- [2026-08-28 19:15:01] operator / voice_transcript_final / voice: no
  meta: kind=final | timestamp=1787915701.2548285 | source=final | rms=251 | updated_at=1787915697.6521664 | frequency_hz=351.7
- [2026-08-28 19:15:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915701.4871469 | source=vosk | rms=251 | updated_at=1787915697.6521664 | frequency_hz=351.7
- [2026-08-28 19:15:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915701.4871469 | source=vosk | rms=251 | updated_at=1787915697.6521664 | frequency_hz=351.7
- [2026-08-28 19:15:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915702.1506526 | source=vosk | rms=251 | updated_at=1787915697.6521664 | frequency_hz=351.7
- [2026-08-28 19:15:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915702.401753 | source=vosk | rms=251 | updated_at=1787915697.6521664 | frequency_hz=351.7
- [2026-08-28 19:15:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915703.1511688 | source=vosk | rms=251 | updated_at=1787915697.6521664 | frequency_hz=351.7
- [2026-08-28 19:15:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915703.6783252 | source=vosk | rms=251 | updated_at=1787915697.6521664 | frequency_hz=351.7
- [2026-08-28 19:15:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915705.9006424 | source=vosk | rms=251 | updated_at=1787915697.6521664 | frequency_hz=351.7
- [2026-08-28 19:15:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915706.1734998 | source=vosk | rms=251 | updated_at=1787915697.6521664 | frequency_hz=351.7
- [2026-08-28 19:15:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915706.6548758 | source=vosk | rms=251 | updated_at=1787915697.6521664 | frequency_hz=351.7
- [2026-08-28 19:15:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915707.156342 | source=vosk | rms=251 | updated_at=1787915697.6521664 | frequency_hz=351.7
- [2026-08-28 19:15:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915707.6511428 | source=vosk | rms=251 | updated_at=1787915697.6521664 | frequency_hz=351.7
- [2026-08-28 19:15:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915720.9229078 | source=vosk | rms=338 | updated_at=1787915720.9229078 | frequency_hz=351.7
- [2026-08-28 19:15:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915721.969567 | source=vosk | rms=168 | updated_at=1787915721.1808095 | frequency_hz=351.7
- [2026-08-28 19:15:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915724.4008183 | source=vosk | rms=168 | updated_at=1787915724.4008183 | frequency_hz=351.7
- [2026-08-28 19:15:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915725.410055 | source=vosk | rms=282 | updated_at=1787915724.6524823 | frequency_hz=351.7
- [2026-08-28 19:15:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915728.9280539 | source=vosk | rms=282 | updated_at=1787915724.6524823 | frequency_hz=351.7
- [2026-08-28 19:15:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915729.4011915 | source=vosk | rms=282 | updated_at=1787915724.6524823 | frequency_hz=351.7
- [2026-08-28 19:15:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915731.9007633 | source=vosk | rms=285 | updated_at=1787915731.9007633 | frequency_hz=351.7
- [2026-08-28 19:15:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915732.920701 | source=vosk | rms=804 | updated_at=1787915732.4015496 | frequency_hz=351.7
- [2026-08-28 19:15:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915741.4014244 | source=vosk | rms=192 | updated_at=1787915741.4014244 | frequency_hz=351.7
- [2026-08-28 19:15:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915742.1511014 | source=vosk | rms=300 | updated_at=1787915741.6823123 | frequency_hz=351.7
- [2026-08-28 19:15:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915744.151047 | source=vosk | rms=300 | updated_at=1787915741.6823123 | frequency_hz=351.7
- [2026-08-28 19:15:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915744.651046 | source=vosk | rms=300 | updated_at=1787915741.6823123 | frequency_hz=351.7
- [2026-08-28 19:15:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915744.9008446 | source=vosk | rms=128 | updated_at=1787915744.9008446 | frequency_hz=351.7
- [2026-08-28 19:15:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915746.6804519 | source=vosk | rms=168 | updated_at=1787915746.151006 | frequency_hz=351.7
- [2026-08-28 19:15:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915747.4455426 | source=vosk | rms=315 | updated_at=1787915747.4455426 | frequency_hz=351.7
- [2026-08-28 19:15:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915747.9457958 | source=vosk | rms=315 | updated_at=1787915747.4455426 | frequency_hz=351.7
- [2026-08-28 19:15:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915749.9638896 | source=vosk | rms=315 | updated_at=1787915747.4455426 | frequency_hz=351.7
- [2026-08-28 19:15:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915750.4415169 | source=vosk | rms=315 | updated_at=1787915747.4455426 | frequency_hz=351.7
- [2026-08-28 19:15:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915752.6913517 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:15:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915753.1913073 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:15:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915756.1993716 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:15:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915756.6917136 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:15:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915758.6936092 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:15:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915759.6922255 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915760.216023 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915761.193669 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915761.6930041 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915765.1919723 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915765.4421268 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915774.94151 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915775.4518898 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915775.9422379 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915776.1925168 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915781.2192326 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915781.7019138 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915782.4517615 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915784.1924841 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915785.4418175 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915786.9700105 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915791.942177 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915792.19202 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915792.6924922 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915798.0329216 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915800.3134577 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915801.0339212 | source=vosk | rms=182 | updated_at=1787915752.6913517 | frequency_hz=351.7
- [2026-08-28 19:16:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915802.5369077 | source=vosk | rms=262 | updated_at=1787915802.0321238 | frequency_hz=351.7
- [2026-08-28 19:16:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915811.1460109 | source=vosk | rms=262 | updated_at=1787915802.0321238 | frequency_hz=351.7
- [2026-08-28 19:16:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915811.6800654 | source=vosk | rms=262 | updated_at=1787915802.0321238 | frequency_hz=351.7
- [2026-08-28 19:16:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915817.3973732 | source=vosk | rms=132 | updated_at=1787915817.3973732 | frequency_hz=351.7
- [2026-08-28 19:17:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915820.8929188 | source=vosk | rms=120 | updated_at=1787915818.420743 | frequency_hz=280.3
- [2026-08-28 19:17:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915821.1597202 | source=vosk | rms=120 | updated_at=1787915818.420743 | frequency_hz=280.3
- [2026-08-28 19:17:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915841.6744626 | source=vosk | rms=127 | updated_at=1787915827.3931022 | frequency_hz=294.0
- [2026-08-28 19:17:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915841.899357 | source=vosk | rms=127 | updated_at=1787915827.3931022 | frequency_hz=294.0
- [2026-08-28 19:17:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915842.411853 | source=vosk | rms=127 | updated_at=1787915827.3931022 | frequency_hz=294.0
- [2026-08-28 19:17:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915843.4248137 | source=vosk | rms=127 | updated_at=1787915827.3931022 | frequency_hz=294.0
- [2026-08-28 19:17:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915844.397688 | source=vosk | rms=127 | updated_at=1787915827.3931022 | frequency_hz=294.0
- [2026-08-28 19:17:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915844.6436124 | source=vosk | rms=127 | updated_at=1787915827.3931022 | frequency_hz=294.0
- [2026-08-28 19:17:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915845.4281147 | source=vosk | rms=127 | updated_at=1787915827.3931022 | frequency_hz=294.0
- [2026-08-28 19:17:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915847.1432133 | source=vosk | rms=188 | updated_at=1787915847.1432133 | frequency_hz=294.0
- [2026-08-28 19:17:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915848.14343 | source=vosk | rms=137 | updated_at=1787915847.4957416 | frequency_hz=294.0
- [2026-08-28 19:17:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915849.8947468 | source=vosk | rms=137 | updated_at=1787915847.4957416 | frequency_hz=294.0
- [2026-08-28 19:17:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915850.4182231 | source=vosk | rms=137 | updated_at=1787915847.4957416 | frequency_hz=294.0
- [2026-08-28 19:17:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915850.8943121 | source=vosk | rms=137 | updated_at=1787915847.4957416 | frequency_hz=294.0
- [2026-08-28 19:17:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915851.8935163 | source=vosk | rms=141 | updated_at=1787915851.1463225 | frequency_hz=294.0
- [2026-08-28 19:17:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915853.1441054 | source=vosk | rms=141 | updated_at=1787915851.1463225 | frequency_hz=294.0
- [2026-08-28 19:17:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915853.6434171 | source=vosk | rms=141 | updated_at=1787915851.1463225 | frequency_hz=294.0
- [2026-08-28 19:17:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915853.9120903 | source=vosk | rms=141 | updated_at=1787915851.1463225 | frequency_hz=294.0
- [2026-08-28 19:17:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915854.3939967 | source=vosk | rms=141 | updated_at=1787915851.1463225 | frequency_hz=294.0
- [2026-08-28 19:17:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915854.9168727 | source=vosk | rms=141 | updated_at=1787915851.1463225 | frequency_hz=294.0
- [2026-08-28 19:17:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915855.4238796 | source=vosk | rms=141 | updated_at=1787915851.1463225 | frequency_hz=294.0
- [2026-08-28 19:17:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915871.948352 | source=vosk | rms=141 | updated_at=1787915851.1463225 | frequency_hz=294.0
- [2026-08-28 19:17:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915876.8979216 | source=vosk | rms=141 | updated_at=1787915851.1463225 | frequency_hz=294.0
- [2026-08-28 19:17:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915877.3967493 | source=vosk | rms=554 | updated_at=1787915877.3967493 | frequency_hz=294.0
- [2026-08-28 19:17:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915878.6478162 | source=vosk | rms=554 | updated_at=1787915877.3967493 | frequency_hz=294.0
- [2026-08-28 19:18:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915882.8956304 | source=vosk | rms=904 | updated_at=1787915882.8956304 | frequency_hz=294.0
- [2026-08-28 19:18:07] operator / voice_transcript_partial / voice: since
  meta: kind=partial | timestamp=1787915887.4038405 | source=vosk | rms=176 | updated_at=1787915886.6447778 | frequency_hz=294.0
- [2026-08-28 19:18:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915887.644486 | source=vosk | rms=176 | updated_at=1787915886.6447778 | frequency_hz=294.0
- [2026-08-28 19:18:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915887.8944883 | source=vosk | rms=176 | updated_at=1787915886.6447778 | frequency_hz=294.0
- [2026-08-28 19:18:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915888.1447287 | source=vosk | rms=176 | updated_at=1787915886.6447778 | frequency_hz=294.0
- [2026-08-28 19:18:08] operator / voice_transcript_final / voice: since
  meta: kind=final | timestamp=1787915888.3357759 | source=final | rms=176 | updated_at=1787915886.6447778 | frequency_hz=294.0
- [2026-08-28 19:18:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915888.6442382 | source=vosk | rms=176 | updated_at=1787915886.6447778 | frequency_hz=294.0
- [2026-08-28 19:18:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915890.3943658 | source=vosk | rms=176 | updated_at=1787915886.6447778 | frequency_hz=294.0
- [2026-08-28 19:18:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915892.3977792 | source=vosk | rms=176 | updated_at=1787915886.6447778 | frequency_hz=294.0
- [2026-08-28 19:18:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915895.4007597 | source=vosk | rms=176 | updated_at=1787915886.6447778 | frequency_hz=294.0
- [2026-08-28 19:18:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915896.668633 | source=vosk | rms=176 | updated_at=1787915886.6447778 | frequency_hz=294.0
- [2026-08-28 19:18:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915897.1503162 | source=vosk | rms=176 | updated_at=1787915886.6447778 | frequency_hz=294.0
- [2026-08-28 19:18:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915897.4029195 | source=vosk | rms=176 | updated_at=1787915886.6447778 | frequency_hz=294.0
- [2026-08-28 19:18:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915897.8960469 | source=vosk | rms=176 | updated_at=1787915886.6447778 | frequency_hz=294.0
- [2026-08-28 19:18:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915900.6726816 | source=vosk | rms=176 | updated_at=1787915886.6447778 | frequency_hz=294.0
- [2026-08-28 19:18:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915901.3950748 | source=vosk | rms=176 | updated_at=1787915886.6447778 | frequency_hz=294.0
- [2026-08-28 19:18:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915905.3949943 | source=vosk | rms=176 | updated_at=1787915886.6447778 | frequency_hz=294.0
- [2026-08-28 19:18:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915906.6483388 | source=vosk | rms=176 | updated_at=1787915886.6447778 | frequency_hz=294.0
- [2026-08-28 19:18:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915906.9180772 | source=vosk | rms=594 | updated_at=1787915906.9180772 | frequency_hz=294.0
- [2026-08-28 19:18:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915907.662281 | source=vosk | rms=289 | updated_at=1787915907.1446831 | frequency_hz=294.0
- [2026-08-28 19:18:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915907.9026985 | source=vosk | rms=289 | updated_at=1787915907.1446831 | frequency_hz=294.0
- [2026-08-28 19:18:27] operator / voice_transcript_partial / voice: well
  meta: kind=partial | timestamp=1787915907.9455874 | source=vosk | rms=289 | updated_at=1787915907.1446831 | frequency_hz=294.0
- [2026-08-28 19:18:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915908.1862068 | source=vosk | rms=289 | updated_at=1787915907.1446831 | frequency_hz=294.0
- [2026-08-28 19:18:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915908.4103572 | source=vosk | rms=289 | updated_at=1787915907.1446831 | frequency_hz=294.0
- [2026-08-28 19:18:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915908.6498687 | source=vosk | rms=644 | updated_at=1787915908.6498687 | frequency_hz=294.0
- [2026-08-28 19:18:28] operator / voice_transcript_final / voice: well
  meta: kind=final | timestamp=1787915908.919489 | source=final | rms=644 | updated_at=1787915908.6498687 | frequency_hz=294.0
- [2026-08-28 19:18:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915909.1689625 | source=vosk | rms=644 | updated_at=1787915908.6498687 | frequency_hz=294.0
- [2026-08-28 19:18:29] operator / voice_transcript_partial / voice: when
  meta: kind=partial | timestamp=1787915909.4440348 | source=vosk | rms=644 | updated_at=1787915908.6498687 | frequency_hz=294.0
- [2026-08-28 19:18:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915909.6447337 | source=vosk | rms=192 | updated_at=1787915909.6447337 | frequency_hz=294.0
- [2026-08-28 19:18:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915909.895308 | source=vosk | rms=192 | updated_at=1787915909.6447337 | frequency_hz=294.0
- [2026-08-28 19:18:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915910.1451254 | source=vosk | rms=192 | updated_at=1787915909.6447337 | frequency_hz=294.0
- [2026-08-28 19:18:30] operator / voice_transcript_final / voice: when
  meta: kind=final | timestamp=1787915910.379008 | source=final | rms=192 | updated_at=1787915909.6447337 | frequency_hz=294.0
- [2026-08-28 19:18:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915910.4181223 | source=vosk | rms=192 | updated_at=1787915909.6447337 | frequency_hz=294.0
- [2026-08-28 19:18:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915914.895055 | source=vosk | rms=192 | updated_at=1787915909.6447337 | frequency_hz=294.0
- [2026-08-28 19:18:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915915.1699362 | source=vosk | rms=192 | updated_at=1787915909.6447337 | frequency_hz=294.0
- [2026-08-28 19:18:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915916.175774 | source=vosk | rms=192 | updated_at=1787915909.6447337 | frequency_hz=294.0
- [2026-08-28 19:18:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915918.898033 | source=vosk | rms=555 | updated_at=1787915918.898033 | frequency_hz=294.0
- [2026-08-28 19:18:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915919.4190464 | source=vosk | rms=555 | updated_at=1787915918.898033 | frequency_hz=294.0
- [2026-08-28 19:18:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915920.644928 | source=vosk | rms=555 | updated_at=1787915918.898033 | frequency_hz=294.0
- [2026-08-28 19:18:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915921.39862 | source=vosk | rms=710 | updated_at=1787915920.895592 | frequency_hz=294.0
- [2026-08-28 19:18:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915924.9131548 | source=vosk | rms=697 | updated_at=1787915924.9131548 | frequency_hz=294.0
- [2026-08-28 19:18:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915927.4026325 | source=vosk | rms=350 | updated_at=1787915926.8952074 | frequency_hz=294.0
- [2026-08-28 19:18:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915937.650638 | source=vosk | rms=1206 | updated_at=1787915937.650638 | frequency_hz=294.0
- [2026-08-28 19:18:58] operator / voice_transcript_partial / voice: from
  meta: kind=partial | timestamp=1787915938.2127995 | source=vosk | rms=208 | updated_at=1787915938.146976 | frequency_hz=294.0
- [2026-08-28 19:18:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915938.3962917 | source=vosk | rms=130 | updated_at=1787915938.3962917 | frequency_hz=294.0
- [2026-08-28 19:18:58] operator / voice_transcript_partial / voice: from atlanta
  meta: kind=partial | timestamp=1787915938.4251676 | source=vosk | rms=130 | updated_at=1787915938.3962917 | frequency_hz=294.0
- [2026-08-28 19:18:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915938.9212956 | source=vosk | rms=130 | updated_at=1787915938.3962917 | frequency_hz=294.0
- [2026-08-28 19:19:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915941.1470687 | source=vosk | rms=1063 | updated_at=1787915941.1470687 | frequency_hz=294.0
- [2026-08-28 19:19:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915941.4038508 | source=vosk | rms=458 | updated_at=1787915941.4038508 | frequency_hz=294.0
- [2026-08-28 19:19:01] operator / voice_transcript_final / voice: from atlanta
  meta: kind=final | timestamp=1787915941.6322174 | source=final | rms=458 | updated_at=1787915941.4038508 | frequency_hz=294.0
- [2026-08-28 19:19:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915941.6623895 | source=vosk | rms=226 | updated_at=1787915941.6623895 | frequency_hz=294.0
- [2026-08-28 19:19:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915942.395444 | source=vosk | rms=330 | updated_at=1787915941.9179356 | frequency_hz=294.0
- [2026-08-28 19:19:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915942.646077 | source=vosk | rms=330 | updated_at=1787915941.9179356 | frequency_hz=294.0
- [2026-08-28 19:19:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915943.3955736 | source=vosk | rms=330 | updated_at=1787915941.9179356 | frequency_hz=294.0
- [2026-08-28 19:19:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915943.6455753 | source=vosk | rms=330 | updated_at=1787915941.9179356 | frequency_hz=294.0
- [2026-08-28 19:19:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915944.6460133 | source=vosk | rms=1202 | updated_at=1787915944.2062533 | frequency_hz=294.0
- [2026-08-28 19:19:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915944.8962107 | source=vosk | rms=709 | updated_at=1787915944.8962107 | frequency_hz=294.0
- [2026-08-28 19:19:05] operator / voice_transcript_partial / voice: that's
  meta: kind=partial | timestamp=1787915945.5094562 | source=vosk | rms=661 | updated_at=1787915945.4393513 | frequency_hz=294.0
- [2026-08-28 19:19:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915945.6471353 | source=vosk | rms=624 | updated_at=1787915945.6471353 | frequency_hz=294.0
- [2026-08-28 19:19:08] operator / voice_transcript_final / voice: ah
  meta: kind=final | timestamp=1787915948.1268303 | source=final | rms=266 | updated_at=1787915947.4025464 | frequency_hz=294.0
- [2026-08-28 19:19:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915948.1573968 | source=vosk | rms=266 | updated_at=1787915947.4025464 | frequency_hz=294.0
- [2026-08-28 19:19:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915953.64635 | source=vosk | rms=1157 | updated_at=1787915953.1463845 | frequency_hz=276.5
- [2026-08-28 19:19:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915956.4076293 | source=vosk | rms=312 | updated_at=1787915956.4076293 | frequency_hz=276.5
- [2026-08-28 19:19:16] operator / voice_transcript_final / voice: go
  meta: kind=final | timestamp=1787915956.7244086 | source=final | rms=312 | updated_at=1787915956.4076293 | frequency_hz=276.5
- [2026-08-28 19:19:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915957.24402 | source=vosk | rms=312 | updated_at=1787915956.4076293 | frequency_hz=276.5
- [2026-08-28 19:19:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915957.24402 | source=vosk | rms=328 | updated_at=1787915957.24402 | frequency_hz=276.5
- [2026-08-28 19:19:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915957.8976622 | source=vosk | rms=335 | updated_at=1787915957.2577426 | frequency_hz=276.5
- [2026-08-28 19:19:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915958.1793926 | source=vosk | rms=581 | updated_at=1787915958.1793926 | frequency_hz=276.5
- [2026-08-28 19:19:18] operator / voice_transcript_partial / voice: at
  meta: kind=partial | timestamp=1787915958.7014358 | source=vosk | rms=855 | updated_at=1787915958.6633985 | frequency_hz=276.5
- [2026-08-28 19:19:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915958.8966558 | source=vosk | rms=431 | updated_at=1787915958.8966558 | frequency_hz=276.5
- [2026-08-28 19:19:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915959.8961663 | source=vosk | rms=483 | updated_at=1787915959.4249587 | frequency_hz=276.5
- [2026-08-28 19:19:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915961.1752634 | source=vosk | rms=678 | updated_at=1787915961.1752634 | frequency_hz=276.5
- [2026-08-28 19:19:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915963.4051304 | source=vosk | rms=476 | updated_at=1787915962.1519334 | frequency_hz=276.5
- [2026-08-28 19:19:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915964.668751 | source=vosk | rms=214 | updated_at=1787915964.668751 | frequency_hz=238.0
- [2026-08-28 19:19:25] operator / voice_transcript_final / voice: that
  meta: kind=final | timestamp=1787915965.8646934 | source=final | rms=342 | updated_at=1787915965.646866 | frequency_hz=238.0
- [2026-08-28 19:19:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915965.9020824 | source=vosk | rms=342 | updated_at=1787915965.646866 | frequency_hz=238.0
- [2026-08-28 19:19:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915966.6786427 | source=vosk | rms=342 | updated_at=1787915965.646866 | frequency_hz=238.0
- [2026-08-28 19:19:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915968.146699 | source=vosk | rms=446 | updated_at=1787915968.146699 | frequency_hz=238.0
- [2026-08-28 19:19:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915968.9264617 | source=vosk | rms=514 | updated_at=1787915968.4013114 | frequency_hz=238.0
- [2026-08-28 19:19:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915969.1463983 | source=vosk | rms=716 | updated_at=1787915969.1463983 | frequency_hz=238.0
- [2026-08-28 19:19:30] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1787915970.9195073 | source=vosk | rms=589 | updated_at=1787915970.8970692 | frequency_hz=238.0
- [2026-08-28 19:19:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915971.4030988 | source=vosk | rms=589 | updated_at=1787915970.8970692 | frequency_hz=238.0
- [2026-08-28 19:19:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915971.9430091 | source=vosk | rms=470 | updated_at=1787915971.9430091 | frequency_hz=238.0
- [2026-08-28 19:19:32] operator / voice_transcript_partial / voice: that said that
  meta: kind=partial | timestamp=1787915972.4380703 | source=vosk | rms=653 | updated_at=1787915972.405027 | frequency_hz=238.0
- [2026-08-28 19:19:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915972.6746445 | source=vosk | rms=383 | updated_at=1787915972.6746445 | frequency_hz=238.0
- [2026-08-28 19:19:32] operator / voice_transcript_partial / voice: other than that of
  meta: kind=partial | timestamp=1787915972.7289512 | source=vosk | rms=383 | updated_at=1787915972.6746445 | frequency_hz=238.0
- [2026-08-28 19:19:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915973.3977385 | source=vosk | rms=383 | updated_at=1787915972.6746445 | frequency_hz=238.0
- [2026-08-28 19:19:33] operator / voice_transcript_partial / voice: neither of us
  meta: kind=partial | timestamp=1787915973.4531884 | source=vosk | rms=383 | updated_at=1787915972.6746445 | frequency_hz=238.0
- [2026-08-28 19:19:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915973.8963678 | source=vosk | rms=383 | updated_at=1787915972.6746445 | frequency_hz=238.0
- [2026-08-28 19:19:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915976.3966534 | source=vosk | rms=372 | updated_at=1787915976.3966534 | frequency_hz=238.0
- [2026-08-28 19:19:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915976.6620345 | source=vosk | rms=795 | updated_at=1787915976.6620345 | frequency_hz=238.0
- [2026-08-28 19:19:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915976.9009018 | source=vosk | rms=358 | updated_at=1787915976.9009018 | frequency_hz=238.0
- [2026-08-28 19:19:37] operator / voice_transcript_final / voice: that last of us
  meta: kind=final | timestamp=1787915977.2461503 | source=final | rms=358 | updated_at=1787915976.9009018 | frequency_hz=238.0
- [2026-08-28 19:19:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915977.3628893 | source=vosk | rms=358 | updated_at=1787915976.9009018 | frequency_hz=238.0
- [2026-08-28 19:19:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915977.3628893 | source=vosk | rms=308 | updated_at=1787915977.3628893 | frequency_hz=238.0
- [2026-08-28 19:19:47] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1787915987.9111106 | source=vosk | rms=1137 | updated_at=1787915987.8980672 | frequency_hz=238.0
- [2026-08-28 19:19:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915988.1690097 | source=vosk | rms=301 | updated_at=1787915988.1690097 | frequency_hz=238.0
- [2026-08-28 19:19:48] operator / voice_transcript_partial / voice: that that's
  meta: kind=partial | timestamp=1787915988.1890385 | source=vosk | rms=301 | updated_at=1787915988.1690097 | frequency_hz=238.0
- [2026-08-28 19:19:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915988.3972359 | source=vosk | rms=297 | updated_at=1787915988.3972359 | frequency_hz=238.0
- [2026-08-28 19:19:48] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1787915988.4138765 | source=vosk | rms=297 | updated_at=1787915988.3972359 | frequency_hz=238.0
- [2026-08-28 19:19:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915988.6468062 | source=vosk | rms=321 | updated_at=1787915988.6468062 | frequency_hz=238.0
- [2026-08-28 19:19:48] operator / voice_transcript_final / voice: that that
  meta: kind=final | timestamp=1787915988.8594666 | source=final | rms=321 | updated_at=1787915988.6468062 | frequency_hz=238.0
- [2026-08-28 19:19:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915988.8982434 | source=vosk | rms=321 | updated_at=1787915988.6468062 | frequency_hz=238.0
- [2026-08-28 19:19:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915993.6482637 | source=vosk | rms=650 | updated_at=1787915990.6472783 | frequency_hz=238.0
- [2026-08-28 19:19:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915993.9147956 | source=vosk | rms=650 | updated_at=1787915990.6472783 | frequency_hz=238.0
- [2026-08-28 19:19:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915994.4197595 | source=vosk | rms=650 | updated_at=1787915990.6472783 | frequency_hz=238.0
- [2026-08-28 19:19:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787915994.8974643 | source=vosk | rms=650 | updated_at=1787915990.6472783 | frequency_hz=238.0
- [2026-08-28 19:19:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787915995.8973267 | source=vosk | rms=650 | updated_at=1787915990.6472783 | frequency_hz=238.0
- [2026-08-28 19:20:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916000.8970428 | source=vosk | rms=401 | updated_at=1787916000.8970428 | frequency_hz=238.0
- [2026-08-28 19:20:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916001.4021974 | source=vosk | rms=401 | updated_at=1787916000.8970428 | frequency_hz=238.0
- [2026-08-28 19:20:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916001.6476314 | source=vosk | rms=435 | updated_at=1787916001.6476314 | frequency_hz=238.0
- [2026-08-28 19:20:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916002.1831102 | source=vosk | rms=435 | updated_at=1787916001.6476314 | frequency_hz=238.0
- [2026-08-28 19:20:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916002.9466102 | source=vosk | rms=435 | updated_at=1787916001.6476314 | frequency_hz=238.0
- [2026-08-28 19:20:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916003.4277353 | source=vosk | rms=435 | updated_at=1787916001.6476314 | frequency_hz=238.0
- [2026-08-28 19:20:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916004.4032476 | source=vosk | rms=435 | updated_at=1787916001.6476314 | frequency_hz=238.0
- [2026-08-28 19:20:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916005.405551 | source=vosk | rms=435 | updated_at=1787916001.6476314 | frequency_hz=238.0
- [2026-08-28 19:20:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916006.1475666 | source=vosk | rms=435 | updated_at=1787916001.6476314 | frequency_hz=238.0
- [2026-08-28 19:20:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916007.432266 | source=vosk | rms=435 | updated_at=1787916001.6476314 | frequency_hz=238.0
- [2026-08-28 19:20:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916021.6591654 | source=vosk | rms=494 | updated_at=1787916021.6591654 | frequency_hz=238.0
- [2026-08-28 19:20:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916023.16942 | source=vosk | rms=448 | updated_at=1787916022.1529448 | frequency_hz=238.0
- [2026-08-28 19:20:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916024.4116392 | source=vosk | rms=448 | updated_at=1787916022.1529448 | frequency_hz=238.0
- [2026-08-28 19:20:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916026.1778777 | source=vosk | rms=448 | updated_at=1787916022.1529448 | frequency_hz=238.0
- [2026-08-28 19:20:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916028.2377722 | source=vosk | rms=448 | updated_at=1787916022.1529448 | frequency_hz=238.0
- [2026-08-28 19:20:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916029.8990395 | source=vosk | rms=448 | updated_at=1787916022.1529448 | frequency_hz=238.0
- [2026-08-28 19:20:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916031.6482723 | source=vosk | rms=448 | updated_at=1787916022.1529448 | frequency_hz=238.0
- [2026-08-28 19:20:38] operator / voice_transcript_partial / voice: without
  meta: kind=partial | timestamp=1787916038.4902403 | source=vosk | rms=144 | updated_at=1787916038.416754 | frequency_hz=238.0
- [2026-08-28 19:20:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916038.6607075 | source=vosk | rms=246 | updated_at=1787916038.6607075 | frequency_hz=238.0
- [2026-08-28 19:20:38] operator / voice_transcript_partial / voice: with all
  meta: kind=partial | timestamp=1787916038.687733 | source=vosk | rms=246 | updated_at=1787916038.6607075 | frequency_hz=238.0
- [2026-08-28 19:20:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916038.9323103 | source=vosk | rms=175 | updated_at=1787916038.9323103 | frequency_hz=238.0
- [2026-08-28 19:20:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916039.1687977 | source=vosk | rms=125 | updated_at=1787916039.1687977 | frequency_hz=238.0
- [2026-08-28 19:20:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916039.4088602 | source=vosk | rms=266 | updated_at=1787916039.4088602 | frequency_hz=238.0
- [2026-08-28 19:20:39] operator / voice_transcript_final / voice: with all
  meta: kind=final | timestamp=1787916039.6581275 | source=final | rms=266 | updated_at=1787916039.4088602 | frequency_hz=238.0
- [2026-08-28 19:20:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916039.6894133 | source=vosk | rms=554 | updated_at=1787916039.6894133 | frequency_hz=238.0
- [2026-08-28 19:20:42] operator / voice_transcript_partial / voice: just
  meta: kind=partial | timestamp=1787916042.6989312 | source=vosk | rms=180 | updated_at=1787916042.683427 | frequency_hz=238.0
- [2026-08-28 19:20:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916042.920771 | source=vosk | rms=437 | updated_at=1787916042.920771 | frequency_hz=238.0
- [2026-08-28 19:20:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916043.169662 | source=vosk | rms=586 | updated_at=1787916043.169662 | frequency_hz=238.0
- [2026-08-28 19:20:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916043.398123 | source=vosk | rms=469 | updated_at=1787916043.398123 | frequency_hz=238.0
- [2026-08-28 19:20:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916043.650802 | source=vosk | rms=597 | updated_at=1787916043.650802 | frequency_hz=238.0
- [2026-08-28 19:20:43] operator / voice_transcript_final / voice: just
  meta: kind=final | timestamp=1787916043.9200497 | source=final | rms=597 | updated_at=1787916043.650802 | frequency_hz=238.0
- [2026-08-28 19:20:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916043.952469 | source=vosk | rms=418 | updated_at=1787916043.952469 | frequency_hz=238.0
- [2026-08-28 19:20:47] operator / voice_transcript_partial / voice: how many
  meta: kind=partial | timestamp=1787916047.4370058 | source=vosk | rms=366 | updated_at=1787916047.1488416 | frequency_hz=238.0
- [2026-08-28 19:20:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916047.898887 | source=vosk | rms=223 | updated_at=1787916047.898887 | frequency_hz=238.0
- [2026-08-28 19:20:47] operator / voice_transcript_partial / voice: how will
  meta: kind=partial | timestamp=1787916047.94449 | source=vosk | rms=223 | updated_at=1787916047.898887 | frequency_hz=238.0
- [2026-08-28 19:20:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916048.1482263 | source=vosk | rms=1153 | updated_at=1787916048.1482263 | frequency_hz=238.0
- [2026-08-28 19:20:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916048.398407 | source=vosk | rms=288 | updated_at=1787916048.398407 | frequency_hz=238.0
- [2026-08-28 19:20:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916048.6486957 | source=vosk | rms=289 | updated_at=1787916048.6486957 | frequency_hz=238.0
- [2026-08-28 19:20:48] operator / voice_transcript_final / voice: hard mode
  meta: kind=final | timestamp=1787916048.920687 | source=final | rms=289 | updated_at=1787916048.6486957 | frequency_hz=238.0
- [2026-08-28 19:20:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916048.9526129 | source=vosk | rms=522 | updated_at=1787916048.9526129 | frequency_hz=238.0
- [2026-08-28 19:20:49] operator / voice_transcript_partial / voice: much
  meta: kind=partial | timestamp=1787916049.9083412 | source=vosk | rms=936 | updated_at=1787916049.8983057 | frequency_hz=238.0
- [2026-08-28 19:20:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916050.1486514 | source=vosk | rms=337 | updated_at=1787916050.1486514 | frequency_hz=238.0
- [2026-08-28 19:20:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916050.3984485 | source=vosk | rms=1205 | updated_at=1787916050.3984485 | frequency_hz=238.0
- [2026-08-28 19:20:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916050.6484027 | source=vosk | rms=1201 | updated_at=1787916050.6484027 | frequency_hz=238.0
- [2026-08-28 19:20:50] operator / voice_transcript_final / voice: much
  meta: kind=final | timestamp=1787916050.9933968 | source=final | rms=1201 | updated_at=1787916050.6484027 | frequency_hz=238.0
- [2026-08-28 19:20:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916051.1764238 | source=vosk | rms=1201 | updated_at=1787916050.6484027 | frequency_hz=238.0
- [2026-08-28 19:20:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916051.1764238 | source=vosk | rms=659 | updated_at=1787916051.1764238 | frequency_hz=238.0
- [2026-08-28 19:20:51] operator / voice_transcript_partial / voice: keep in
  meta: kind=partial | timestamp=1787916051.9607897 | source=vosk | rms=400 | updated_at=1787916051.9286573 | frequency_hz=238.0
- [2026-08-28 19:20:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916052.1595752 | source=vosk | rms=414 | updated_at=1787916052.1595752 | frequency_hz=238.0
- [2026-08-28 19:20:52] operator / voice_transcript_partial / voice: keep an eye out
  meta: kind=partial | timestamp=1787916052.210619 | source=vosk | rms=414 | updated_at=1787916052.1595752 | frequency_hz=238.0
- [2026-08-28 19:20:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916052.4056535 | source=vosk | rms=159 | updated_at=1787916052.4056535 | frequency_hz=238.0
- [2026-08-28 19:20:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916052.649395 | source=vosk | rms=159 | updated_at=1787916052.4056535 | frequency_hz=238.0
- [2026-08-28 19:20:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916052.9330812 | source=vosk | rms=159 | updated_at=1787916052.4056535 | frequency_hz=238.0
- [2026-08-28 19:20:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916053.181717 | source=vosk | rms=1191 | updated_at=1787916053.181717 | frequency_hz=238.0
- [2026-08-28 19:20:53] operator / voice_transcript_partial / voice: keep an eye out for
  meta: kind=partial | timestamp=1787916053.225705 | source=vosk | rms=1191 | updated_at=1787916053.181717 | frequency_hz=238.0
- [2026-08-28 19:20:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916053.492704 | source=vosk | rms=801 | updated_at=1787916053.492704 | frequency_hz=238.0
- [2026-08-28 19:20:53] operator / voice_transcript_final / voice: keep an eye out
  meta: kind=final | timestamp=1787916053.92983 | source=final | rms=801 | updated_at=1787916053.492704 | frequency_hz=238.0
- [2026-08-28 19:20:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916054.1375074 | source=vosk | rms=801 | updated_at=1787916053.492704 | frequency_hz=238.0
- [2026-08-28 19:20:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916054.1375074 | source=vosk | rms=801 | updated_at=1787916053.492704 | frequency_hz=238.0
- [2026-08-28 19:20:54] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1787916054.1696682 | source=vosk | rms=801 | updated_at=1787916053.492704 | frequency_hz=238.0
- [2026-08-28 19:20:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916054.4195795 | source=vosk | rms=1200 | updated_at=1787916054.4195795 | frequency_hz=238.0
- [2026-08-28 19:20:54] operator / voice_transcript_final / voice: yeah
  meta: kind=final | timestamp=1787916054.610577 | source=final | rms=1200 | updated_at=1787916054.4195795 | frequency_hz=238.0
- [2026-08-28 19:20:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916054.9062047 | source=vosk | rms=1200 | updated_at=1787916054.4195795 | frequency_hz=238.0
- [2026-08-28 19:20:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916055.1556075 | source=vosk | rms=1205 | updated_at=1787916055.1556075 | frequency_hz=238.0
- [2026-08-28 19:20:56] operator / voice_transcript_partial / voice: people were
  meta: kind=partial | timestamp=1787916056.25204 | source=vosk | rms=799 | updated_at=1787916056.1484845 | frequency_hz=238.0
- [2026-08-28 19:20:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916056.4126105 | source=vosk | rms=1203 | updated_at=1787916056.4126105 | frequency_hz=238.0
- [2026-08-28 19:20:56] operator / voice_transcript_partial / voice: very rare form of
  meta: kind=partial | timestamp=1787916056.5297413 | source=vosk | rms=1203 | updated_at=1787916056.4126105 | frequency_hz=238.0
- [2026-08-28 19:20:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916056.6499484 | source=vosk | rms=1201 | updated_at=1787916056.6499484 | frequency_hz=238.0
- [2026-08-28 19:20:56] operator / voice_transcript_partial / voice: very rare for i don't
  meta: kind=partial | timestamp=1787916056.7068496 | source=vosk | rms=1201 | updated_at=1787916056.6499484 | frequency_hz=238.0
- [2026-08-28 19:20:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916056.9185877 | source=vosk | rms=1708 | updated_at=1787916056.9185877 | frequency_hz=238.0
- [2026-08-28 19:20:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916057.2017055 | source=vosk | rms=2072 | updated_at=1787916057.2017055 | frequency_hz=238.0
- [2026-08-28 19:20:57] operator / voice_transcript_final / voice: people for it
  meta: kind=final | timestamp=1787916057.5888865 | source=final | rms=2072 | updated_at=1787916057.2017055 | frequency_hz=238.0
- [2026-08-28 19:20:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916057.7246733 | source=vosk | rms=2072 | updated_at=1787916057.2017055 | frequency_hz=238.0
- [2026-08-28 19:20:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916057.7246733 | source=vosk | rms=1484 | updated_at=1787916057.7246733 | frequency_hz=238.0
- [2026-08-28 19:21:01] operator / voice_transcript_partial / voice: twenty
  meta: kind=partial | timestamp=1787916061.5191138 | source=vosk | rms=637 | updated_at=1787916061.4411495 | frequency_hz=238.0
- [2026-08-28 19:21:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916061.6783054 | source=vosk | rms=810 | updated_at=1787916061.6783054 | frequency_hz=238.0
- [2026-08-28 19:21:01] operator / voice_transcript_partial / voice: tom reeves
  meta: kind=partial | timestamp=1787916061.9940853 | source=vosk | rms=564 | updated_at=1787916061.9282987 | frequency_hz=238.0
- [2026-08-28 19:21:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916062.178884 | source=vosk | rms=564 | updated_at=1787916061.9282987 | frequency_hz=238.0
- [2026-08-28 19:21:02] operator / voice_transcript_partial / voice: tom ridge
  meta: kind=partial | timestamp=1787916062.215942 | source=vosk | rms=564 | updated_at=1787916061.9282987 | frequency_hz=238.0
- [2026-08-28 19:21:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916062.4324036 | source=vosk | rms=605 | updated_at=1787916062.4324036 | frequency_hz=238.0
- [2026-08-28 19:21:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916062.771648 | source=vosk | rms=1203 | updated_at=1787916062.771648 | frequency_hz=238.0
- [2026-08-28 19:21:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916062.9608152 | source=vosk | rms=832 | updated_at=1787916062.9608152 | frequency_hz=238.0
- [2026-08-28 19:21:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916063.679065 | source=vosk | rms=832 | updated_at=1787916062.9608152 | frequency_hz=238.0
- [2026-08-28 19:21:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916065.203721 | source=vosk | rms=494 | updated_at=1787916065.203721 | frequency_hz=238.0
- [2026-08-28 19:21:05] operator / voice_transcript_final / voice: tom ridge
  meta: kind=final | timestamp=1787916065.53281 | source=final | rms=494 | updated_at=1787916065.203721 | frequency_hz=238.0
- [2026-08-28 19:21:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916065.5718782 | source=vosk | rms=1065 | updated_at=1787916065.5718782 | frequency_hz=238.0
- [2026-08-28 19:21:05] operator / voice_transcript_partial / voice: are
  meta: kind=partial | timestamp=1787916065.7194948 | source=vosk | rms=1065 | updated_at=1787916065.5718782 | frequency_hz=238.0
- [2026-08-28 19:21:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916065.9601157 | source=vosk | rms=1136 | updated_at=1787916065.9601157 | frequency_hz=238.0
- [2026-08-28 19:21:05] operator / voice_transcript_partial / voice: are you
  meta: kind=partial | timestamp=1787916065.972193 | source=vosk | rms=1136 | updated_at=1787916065.9601157 | frequency_hz=238.0
- [2026-08-28 19:21:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916066.1843696 | source=vosk | rms=1136 | updated_at=1787916065.9601157 | frequency_hz=238.0
- [2026-08-28 19:21:06] operator / voice_transcript_partial / voice: are you know
  meta: kind=partial | timestamp=1787916066.2398608 | source=vosk | rms=1136 | updated_at=1787916065.9601157 | frequency_hz=238.0
- [2026-08-28 19:21:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916066.4490466 | source=vosk | rms=1136 | updated_at=1787916065.9601157 | frequency_hz=238.0
- [2026-08-28 19:21:06] operator / voice_transcript_partial / voice: are you are one and
  meta: kind=partial | timestamp=1787916066.5027204 | source=vosk | rms=1136 | updated_at=1787916065.9601157 | frequency_hz=238.0
- [2026-08-28 19:21:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916066.6819997 | source=vosk | rms=1136 | updated_at=1787916065.9601157 | frequency_hz=238.0
- [2026-08-28 19:21:06] operator / voice_transcript_partial / voice: are you know when i'm not
  meta: kind=partial | timestamp=1787916066.7320123 | source=vosk | rms=1136 | updated_at=1787916065.9601157 | frequency_hz=238.0
- [2026-08-28 19:21:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916067.1792662 | source=vosk | rms=1136 | updated_at=1787916065.9601157 | frequency_hz=238.0
- [2026-08-28 19:21:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916067.4677076 | source=vosk | rms=1206 | updated_at=1787916067.4677076 | frequency_hz=238.0
- [2026-08-28 19:21:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916067.6993673 | source=vosk | rms=749 | updated_at=1787916067.6993673 | frequency_hz=238.0
- [2026-08-28 19:21:07] operator / voice_transcript_partial / voice: are you know when i'm hungry shoulder
  meta: kind=partial | timestamp=1787916067.741646 | source=vosk | rms=749 | updated_at=1787916067.6993673 | frequency_hz=238.0
- [2026-08-28 19:21:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916067.9289508 | source=vosk | rms=904 | updated_at=1787916067.9289508 | frequency_hz=238.0
- [2026-08-28 19:21:07] operator / voice_transcript_partial / voice: are you know when i'm hungry shoulder up remember
  meta: kind=partial | timestamp=1787916067.9675875 | source=vosk | rms=904 | updated_at=1787916067.9289508 | frequency_hz=238.0
- [2026-08-28 19:21:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916068.4379897 | source=vosk | rms=904 | updated_at=1787916067.9289508 | frequency_hz=238.0
- [2026-08-28 19:21:08] operator / voice_transcript_partial / voice: are you know when i'm hungry shoulder and
  meta: kind=partial | timestamp=1787916068.513406 | source=vosk | rms=904 | updated_at=1787916067.9289508 | frequency_hz=238.0
- [2026-08-28 19:21:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916068.957296 | source=vosk | rms=904 | updated_at=1787916067.9289508 | frequency_hz=238.0
- [2026-08-28 19:21:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916074.7487004 | source=vosk | rms=904 | updated_at=1787916067.9289508 | frequency_hz=238.0
- [2026-08-28 19:21:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916075.2735634 | source=vosk | rms=904 | updated_at=1787916067.9289508 | frequency_hz=238.0
- [2026-08-28 19:21:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916080.2488234 | source=vosk | rms=904 | updated_at=1787916067.9289508 | frequency_hz=238.0
- [2026-08-28 19:21:20] operator / voice_transcript_partial / voice: are you know when i'm hungry shoulder up a little
  meta: kind=partial | timestamp=1787916080.2765627 | source=vosk | rms=904 | updated_at=1787916067.9289508 | frequency_hz=238.0
- [2026-08-28 19:21:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916080.5008116 | source=vosk | rms=904 | updated_at=1787916067.9289508 | frequency_hz=238.0
- [2026-08-28 19:21:20] operator / voice_transcript_partial / voice: are you know when i'm hungry shoulder up
  meta: kind=partial | timestamp=1787916080.56134 | source=vosk | rms=904 | updated_at=1787916067.9289508 | frequency_hz=238.0
- [2026-08-28 19:21:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916081.0007873 | source=vosk | rms=904 | updated_at=1787916067.9289508 | frequency_hz=238.0
- [2026-08-28 19:21:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916081.8045235 | source=vosk | rms=904 | updated_at=1787916067.9289508 | frequency_hz=238.0
- [2026-08-28 19:21:22] operator / voice_transcript_final / voice: are you know when i m hungry shoulder up to lately
  meta: kind=final | timestamp=1787916082.1219943 | source=final | rms=904 | updated_at=1787916067.9289508 | frequency_hz=238.0
- [2026-08-28 19:21:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916082.2271657 | source=vosk | rms=904 | updated_at=1787916067.9289508 | frequency_hz=238.0
- [2026-08-28 19:21:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916082.2271657 | source=vosk | rms=904 | updated_at=1787916067.9289508 | frequency_hz=238.0
- [2026-08-28 19:21:22] operator / voice_transcript_partial / voice: we are
  meta: kind=partial | timestamp=1787916082.2683616 | source=vosk | rms=904 | updated_at=1787916067.9289508 | frequency_hz=238.0
- [2026-08-28 19:21:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916082.499456 | source=vosk | rms=904 | updated_at=1787916067.9289508 | frequency_hz=238.0
- [2026-08-28 19:21:22] operator / voice_transcript_partial / voice: we're on
  meta: kind=partial | timestamp=1787916082.5225022 | source=vosk | rms=904 | updated_at=1787916067.9289508 | frequency_hz=238.0
- [2026-08-28 19:21:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916083.0153553 | source=vosk | rms=904 | updated_at=1787916067.9289508 | frequency_hz=238.0
- [2026-08-28 19:21:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916083.273827 | source=vosk | rms=904 | updated_at=1787916067.9289508 | frequency_hz=238.0
- [2026-08-28 19:21:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916084.041728 | source=vosk | rms=1201 | updated_at=1787916084.041728 | frequency_hz=238.0
- [2026-08-28 19:21:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916084.2491224 | source=vosk | rms=634 | updated_at=1787916084.2491224 | frequency_hz=238.0
- [2026-08-28 19:21:24] operator / voice_transcript_partial / voice: we're on our
  meta: kind=partial | timestamp=1787916084.2806244 | source=vosk | rms=634 | updated_at=1787916084.2491224 | frequency_hz=238.0
- [2026-08-28 19:21:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916084.749572 | source=vosk | rms=634 | updated_at=1787916084.2491224 | frequency_hz=238.0
- [2026-08-28 19:21:24] operator / voice_transcript_partial / voice: we're on fossil fuels
  meta: kind=partial | timestamp=1787916084.8362548 | source=vosk | rms=634 | updated_at=1787916084.2491224 | frequency_hz=238.0
- [2026-08-28 19:21:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916085.2569878 | source=vosk | rms=1205 | updated_at=1787916085.2569878 | frequency_hz=238.0
- [2026-08-28 19:21:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916085.4995463 | source=vosk | rms=1204 | updated_at=1787916085.4995463 | frequency_hz=238.0
- [2026-08-28 19:21:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916085.7490616 | source=vosk | rms=1202 | updated_at=1787916085.7490616 | frequency_hz=238.0
- [2026-08-28 19:21:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916086.0234132 | source=vosk | rms=1201 | updated_at=1787916086.0234132 | frequency_hz=238.0
- [2026-08-28 19:21:26] operator / voice_transcript_final / voice: we on possible
  meta: kind=final | timestamp=1787916086.4404824 | source=final | rms=1201 | updated_at=1787916086.0234132 | frequency_hz=238.0
- [2026-08-28 19:21:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916086.750713 | source=vosk | rms=1201 | updated_at=1787916086.0234132 | frequency_hz=238.0
- [2026-08-28 19:21:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916086.750713 | source=vosk | rms=1203 | updated_at=1787916086.750713 | frequency_hz=238.0
- [2026-08-28 19:21:27] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1787916087.296702 | source=vosk | rms=1204 | updated_at=1787916087.2797022 | frequency_hz=238.0
- [2026-08-28 19:21:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916087.5163708 | source=vosk | rms=1201 | updated_at=1787916087.5163708 | frequency_hz=238.0
- [2026-08-28 19:21:27] operator / voice_transcript_partial / voice: the deal
  meta: kind=partial | timestamp=1787916087.5802565 | source=vosk | rms=1201 | updated_at=1787916087.5163708 | frequency_hz=238.0
- [2026-08-28 19:21:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916087.7494562 | source=vosk | rms=1201 | updated_at=1787916087.7494562 | frequency_hz=238.0
- [2026-08-28 19:21:27] operator / voice_transcript_partial / voice: the the old a lot
  meta: kind=partial | timestamp=1787916087.8509717 | source=vosk | rms=1201 | updated_at=1787916087.7494562 | frequency_hz=238.0
- [2026-08-28 19:21:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916088.0298254 | source=vosk | rms=1200 | updated_at=1787916088.0298254 | frequency_hz=238.0
- [2026-08-28 19:21:28] operator / voice_transcript_partial / voice: the deal that
  meta: kind=partial | timestamp=1787916088.0513253 | source=vosk | rms=1200 | updated_at=1787916088.0298254 | frequency_hz=238.0
- [2026-08-28 19:21:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916088.3316731 | source=vosk | rms=1202 | updated_at=1787916088.3316731 | frequency_hz=238.0
- [2026-08-28 19:21:28] operator / voice_transcript_final / voice: the folder
  meta: kind=final | timestamp=1787916088.7263925 | source=final | rms=1202 | updated_at=1787916088.3316731 | frequency_hz=238.0
- [2026-08-28 19:21:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916088.821635 | source=vosk | rms=1202 | updated_at=1787916088.3316731 | frequency_hz=238.0
- [2026-08-28 19:21:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916088.8226352 | source=vosk | rms=1200 | updated_at=1787916088.821635 | frequency_hz=238.0
- [2026-08-28 19:21:28] operator / voice_transcript_partial / voice: regarding the
  meta: kind=partial | timestamp=1787916088.9179358 | source=vosk | rms=1201 | updated_at=1787916088.8607366 | frequency_hz=238.0
- [2026-08-28 19:21:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916089.0304382 | source=vosk | rms=1201 | updated_at=1787916088.8607366 | frequency_hz=238.0
- [2026-08-28 19:21:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916089.250836 | source=vosk | rms=1206 | updated_at=1787916089.250836 | frequency_hz=238.0
- [2026-08-28 19:21:29] operator / voice_transcript_partial / voice: regarding the upper
  meta: kind=partial | timestamp=1787916089.3063934 | source=vosk | rms=1206 | updated_at=1787916089.250836 | frequency_hz=238.0
- [2026-08-28 19:21:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916089.4991016 | source=vosk | rms=1200 | updated_at=1787916089.4991016 | frequency_hz=238.0
- [2026-08-28 19:21:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916089.7496455 | source=vosk | rms=1202 | updated_at=1787916089.7496455 | frequency_hz=238.0
- [2026-08-28 19:21:29] operator / voice_transcript_partial / voice: regarding the upper i'm about
  meta: kind=partial | timestamp=1787916089.7913907 | source=vosk | rms=1202 | updated_at=1787916089.7496455 | frequency_hz=238.0
- [2026-08-28 19:21:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916090.0114818 | source=vosk | rms=1202 | updated_at=1787916090.0114818 | frequency_hz=238.0
- [2026-08-28 19:21:30] operator / voice_transcript_partial / voice: regarding the upper i'm
  meta: kind=partial | timestamp=1787916090.065006 | source=vosk | rms=1202 | updated_at=1787916090.0114818 | frequency_hz=238.0
- [2026-08-28 19:21:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916090.2584155 | source=vosk | rms=1200 | updated_at=1787916090.2584155 | frequency_hz=238.0
- [2026-08-28 19:21:30] operator / voice_transcript_partial / voice: regarding the upper i'm about an hour
  meta: kind=partial | timestamp=1787916090.3161323 | source=vosk | rms=1200 | updated_at=1787916090.2584155 | frequency_hz=238.0
- [2026-08-28 19:21:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916090.5536542 | source=vosk | rms=601 | updated_at=1787916090.5536542 | frequency_hz=238.0
- [2026-08-28 19:21:30] operator / voice_transcript_partial / voice: regarding the upper i've
  meta: kind=partial | timestamp=1787916090.5801501 | source=vosk | rms=601 | updated_at=1787916090.5536542 | frequency_hz=238.0
- [2026-08-28 19:21:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916090.998933 | source=vosk | rms=1202 | updated_at=1787916090.998933 | frequency_hz=238.0
- [2026-08-28 19:21:31] operator / voice_transcript_partial / voice: regarding the number of guns
  meta: kind=partial | timestamp=1787916091.027186 | source=vosk | rms=1202 | updated_at=1787916090.998933 | frequency_hz=238.0
- [2026-08-28 19:21:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916091.5338428 | source=vosk | rms=1202 | updated_at=1787916091.5338428 | frequency_hz=238.0
- [2026-08-28 19:21:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916091.799695 | source=vosk | rms=858 | updated_at=1787916091.799695 | frequency_hz=238.0
- [2026-08-28 19:21:32] operator / voice_transcript_final / voice: regarding the upper i m about know that guns
  meta: kind=final | timestamp=1787916092.7598116 | source=final | rms=858 | updated_at=1787916091.799695 | frequency_hz=238.0
- [2026-08-28 19:21:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916092.9160323 | source=vosk | rms=858 | updated_at=1787916091.799695 | frequency_hz=238.0
- [2026-08-28 19:21:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916092.9160323 | source=vosk | rms=851 | updated_at=1787916092.9160323 | frequency_hz=238.0
- [2026-08-28 19:21:33] operator / voice_transcript_partial / voice: don't forget
  meta: kind=partial | timestamp=1787916093.1014807 | source=vosk | rms=519 | updated_at=1787916093.0419376 | frequency_hz=238.0
- [2026-08-28 19:21:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916093.2988238 | source=vosk | rms=1203 | updated_at=1787916093.1014807 | frequency_hz=238.0
- [2026-08-28 19:21:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916093.5297246 | source=vosk | rms=1203 | updated_at=1787916093.1014807 | frequency_hz=238.0
- [2026-08-28 19:21:33] operator / voice_transcript_partial / voice: don't forget to
  meta: kind=partial | timestamp=1787916093.5635903 | source=vosk | rms=1203 | updated_at=1787916093.1014807 | frequency_hz=238.0
- [2026-08-28 19:21:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916093.7795634 | source=vosk | rms=985 | updated_at=1787916093.7795634 | frequency_hz=238.0
- [2026-08-28 19:21:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916094.0314198 | source=vosk | rms=985 | updated_at=1787916093.7795634 | frequency_hz=238.0
- [2026-08-28 19:21:34] operator / voice_transcript_partial / voice: don't forget to look
  meta: kind=partial | timestamp=1787916094.1084104 | source=vosk | rms=985 | updated_at=1787916093.7795634 | frequency_hz=238.0
- [2026-08-28 19:21:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916094.5328019 | source=vosk | rms=985 | updated_at=1787916093.7795634 | frequency_hz=238.0
- [2026-08-28 19:21:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916095.0299246 | source=vosk | rms=985 | updated_at=1787916093.7795634 | frequency_hz=238.0
- [2026-08-28 19:21:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916095.7815368 | source=vosk | rms=854 | updated_at=1787916095.7815368 | frequency_hz=238.0
- [2026-08-28 19:21:36] operator / voice_transcript_final / voice: don t forget to look
  meta: kind=final | timestamp=1787916096.094869 | source=final | rms=854 | updated_at=1787916095.7815368 | frequency_hz=238.0
- [2026-08-28 19:21:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916096.1994865 | source=vosk | rms=1051 | updated_at=1787916096.1994865 | frequency_hz=238.0
- [2026-08-28 19:21:36] operator / voice_transcript_partial / voice: i do this
  meta: kind=partial | timestamp=1787916096.3208551 | source=vosk | rms=845 | updated_at=1787916096.279168 | frequency_hz=238.0
- [2026-08-28 19:21:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916096.5686858 | source=vosk | rms=845 | updated_at=1787916096.279168 | frequency_hz=238.0
- [2026-08-28 19:21:36] operator / voice_transcript_partial / voice: i do
  meta: kind=partial | timestamp=1787916096.6272287 | source=vosk | rms=845 | updated_at=1787916096.279168 | frequency_hz=238.0
- [2026-08-28 19:21:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916096.7858558 | source=vosk | rms=504 | updated_at=1787916096.7858558 | frequency_hz=238.0
- [2026-08-28 19:21:36] operator / voice_transcript_partial / voice: i do some
  meta: kind=partial | timestamp=1787916096.855968 | source=vosk | rms=504 | updated_at=1787916096.7858558 | frequency_hz=238.0
- [2026-08-28 19:21:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916097.0682952 | source=vosk | rms=1197 | updated_at=1787916097.0682952 | frequency_hz=238.0
- [2026-08-28 19:21:37] operator / voice_transcript_partial / voice: i do those are just a little
  meta: kind=partial | timestamp=1787916097.1779578 | source=vosk | rms=1197 | updated_at=1787916097.0682952 | frequency_hz=238.0
- [2026-08-28 19:21:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916097.7792258 | source=vosk | rms=1197 | updated_at=1787916097.0682952 | frequency_hz=238.0
- [2026-08-28 19:21:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916099.7810292 | source=vosk | rms=1197 | updated_at=1787916097.0682952 | frequency_hz=238.0
- [2026-08-28 19:21:39] operator / voice_transcript_partial / voice: i do some people will go
  meta: kind=partial | timestamp=1787916099.8208265 | source=vosk | rms=1197 | updated_at=1787916097.0682952 | frequency_hz=238.0
- [2026-08-28 19:21:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916100.2797377 | source=vosk | rms=1083 | updated_at=1787916100.2797377 | frequency_hz=238.0
- [2026-08-28 19:21:40] operator / voice_transcript_partial / voice: i do those understanding what does not
  meta: kind=partial | timestamp=1787916100.371645 | source=vosk | rms=1083 | updated_at=1787916100.2797377 | frequency_hz=238.0
- [2026-08-28 19:21:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916100.5667984 | source=vosk | rms=1083 | updated_at=1787916100.2797377 | frequency_hz=238.0
- [2026-08-28 19:21:40] operator / voice_transcript_partial / voice: i do those are just a little doubt that are
  meta: kind=partial | timestamp=1787916100.6249926 | source=vosk | rms=1083 | updated_at=1787916100.2797377 | frequency_hz=238.0
- [2026-08-28 19:21:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916101.0338125 | source=vosk | rms=645 | updated_at=1787916101.0338125 | frequency_hz=238.0
- [2026-08-28 19:21:41] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on
  meta: kind=partial | timestamp=1787916101.0849056 | source=vosk | rms=645 | updated_at=1787916101.0338125 | frequency_hz=238.0
- [2026-08-28 19:21:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916101.5302508 | source=vosk | rms=645 | updated_at=1787916101.0338125 | frequency_hz=238.0
- [2026-08-28 19:21:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916101.7807329 | source=vosk | rms=582 | updated_at=1787916101.7807329 | frequency_hz=238.0
- [2026-08-28 19:21:41] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth
  meta: kind=partial | timestamp=1787916101.8309586 | source=vosk | rms=582 | updated_at=1787916101.7807329 | frequency_hz=238.0
- [2026-08-28 19:21:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916102.0572088 | source=vosk | rms=582 | updated_at=1787916101.7807329 | frequency_hz=238.0
- [2026-08-28 19:21:42] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth are
  meta: kind=partial | timestamp=1787916102.112751 | source=vosk | rms=582 | updated_at=1787916101.7807329 | frequency_hz=238.0
- [2026-08-28 19:21:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916102.2795858 | source=vosk | rms=582 | updated_at=1787916101.7807329 | frequency_hz=238.0
- [2026-08-28 19:21:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916102.77994 | source=vosk | rms=582 | updated_at=1787916101.7807329 | frequency_hz=238.0
- [2026-08-28 19:21:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916103.0538154 | source=vosk | rms=582 | updated_at=1787916101.7807329 | frequency_hz=238.0
- [2026-08-28 19:21:43] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or
  meta: kind=partial | timestamp=1787916103.1120107 | source=vosk | rms=582 | updated_at=1787916101.7807329 | frequency_hz=238.0
- [2026-08-28 19:21:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916103.2799973 | source=vosk | rms=582 | updated_at=1787916101.7807329 | frequency_hz=238.0
- [2026-08-28 19:21:43] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or or
  meta: kind=partial | timestamp=1787916103.3145304 | source=vosk | rms=582 | updated_at=1787916101.7807329 | frequency_hz=238.0
- [2026-08-28 19:21:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916103.529931 | source=vosk | rms=626 | updated_at=1787916103.529931 | frequency_hz=238.0
- [2026-08-28 19:21:43] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth are all good
  meta: kind=partial | timestamp=1787916103.5620096 | source=vosk | rms=626 | updated_at=1787916103.529931 | frequency_hz=238.0
- [2026-08-28 19:21:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916103.8305051 | source=vosk | rms=508 | updated_at=1787916103.8305051 | frequency_hz=238.0
- [2026-08-28 19:21:43] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or one hundred percent
  meta: kind=partial | timestamp=1787916103.9210775 | source=vosk | rms=508 | updated_at=1787916103.8305051 | frequency_hz=238.0
- [2026-08-28 19:21:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916104.5301235 | source=vosk | rms=508 | updated_at=1787916103.8305051 | frequency_hz=238.0
- [2026-08-28 19:21:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916106.0297885 | source=vosk | rms=508 | updated_at=1787916103.8305051 | frequency_hz=238.0
- [2026-08-28 19:21:46] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program
  meta: kind=partial | timestamp=1787916106.064138 | source=vosk | rms=508 | updated_at=1787916103.8305051 | frequency_hz=238.0
- [2026-08-28 19:21:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916106.3142958 | source=vosk | rms=596 | updated_at=1787916106.3142958 | frequency_hz=238.0
- [2026-08-28 19:21:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916106.5328577 | source=vosk | rms=603 | updated_at=1787916106.5328577 | frequency_hz=238.0
- [2026-08-28 19:21:46] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called
  meta: kind=partial | timestamp=1787916106.588797 | source=vosk | rms=603 | updated_at=1787916106.5328577 | frequency_hz=238.0
- [2026-08-28 19:21:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916106.7808042 | source=vosk | rms=603 | updated_at=1787916106.5328577 | frequency_hz=238.0
- [2026-08-28 19:21:46] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on the pokemon go
  meta: kind=partial | timestamp=1787916106.8259132 | source=vosk | rms=603 | updated_at=1787916106.5328577 | frequency_hz=238.0
- [2026-08-28 19:21:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916107.2799397 | source=vosk | rms=603 | updated_at=1787916106.5328577 | frequency_hz=238.0
- [2026-08-28 19:21:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916107.5294836 | source=vosk | rms=1200 | updated_at=1787916107.5294836 | frequency_hz=238.0
- [2026-08-28 19:21:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916107.7991996 | source=vosk | rms=1203 | updated_at=1787916107.7991996 | frequency_hz=238.0
- [2026-08-28 19:21:47] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on the pokemon go big or
  meta: kind=partial | timestamp=1787916107.8811088 | source=vosk | rms=1203 | updated_at=1787916107.7991996 | frequency_hz=238.0
- [2026-08-28 19:21:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916108.2825036 | source=vosk | rms=665 | updated_at=1787916108.2825036 | frequency_hz=238.0
- [2026-08-28 19:21:48] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program will do little bit
  meta: kind=partial | timestamp=1787916108.347709 | source=vosk | rms=665 | updated_at=1787916108.2825036 | frequency_hz=238.0
- [2026-08-28 19:21:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916108.5301805 | source=vosk | rms=1201 | updated_at=1787916108.5301805 | frequency_hz=238.0
- [2026-08-28 19:21:48] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on the pokemon go back
  meta: kind=partial | timestamp=1787916108.5578122 | source=vosk | rms=1201 | updated_at=1787916108.5301805 | frequency_hz=238.0
- [2026-08-28 19:21:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916108.779854 | source=vosk | rms=1201 | updated_at=1787916108.5301805 | frequency_hz=238.0
- [2026-08-28 19:21:48] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on the pokemon go back to
  meta: kind=partial | timestamp=1787916108.8460655 | source=vosk | rms=1201 | updated_at=1787916108.5301805 | frequency_hz=238.0
- [2026-08-28 19:21:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916109.0542383 | source=vosk | rms=735 | updated_at=1787916109.0542383 | frequency_hz=238.0
- [2026-08-28 19:21:49] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on the pokemon go been treated with respect
  meta: kind=partial | timestamp=1787916109.0990987 | source=vosk | rms=735 | updated_at=1787916109.0542383 | frequency_hz=238.0
- [2026-08-28 19:21:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916109.291001 | source=vosk | rms=735 | updated_at=1787916109.0542383 | frequency_hz=238.0
- [2026-08-28 19:21:49] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on the pokemon go back to when the looming
  meta: kind=partial | timestamp=1787916109.3911982 | source=vosk | rms=735 | updated_at=1787916109.0542383 | frequency_hz=238.0
- [2026-08-28 19:21:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916110.115941 | source=vosk | rms=735 | updated_at=1787916109.0542383 | frequency_hz=238.0
- [2026-08-28 19:21:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916110.2942705 | source=vosk | rms=1200 | updated_at=1787916110.2942705 | frequency_hz=238.0
- [2026-08-28 19:21:50] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it
  meta: kind=partial | timestamp=1787916110.3628254 | source=vosk | rms=1200 | updated_at=1787916110.2942705 | frequency_hz=238.0
- [2026-08-28 19:21:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916110.784901 | source=vosk | rms=1200 | updated_at=1787916110.2942705 | frequency_hz=238.0
- [2026-08-28 19:21:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916114.041291 | source=vosk | rms=1200 | updated_at=1787916110.2942705 | frequency_hz=238.0
- [2026-08-28 19:21:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916114.5483656 | source=vosk | rms=1200 | updated_at=1787916110.2942705 | frequency_hz=238.0
- [2026-08-28 19:21:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916115.0658195 | source=vosk | rms=1101 | updated_at=1787916115.0658195 | frequency_hz=238.0
- [2026-08-28 19:21:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916115.2801588 | source=vosk | rms=1101 | updated_at=1787916115.0658195 | frequency_hz=238.0
- [2026-08-28 19:21:55] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease
  meta: kind=partial | timestamp=1787916115.3769636 | source=vosk | rms=1101 | updated_at=1787916115.0658195 | frequency_hz=238.0
- [2026-08-28 19:21:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916116.0295599 | source=vosk | rms=1101 | updated_at=1787916115.0658195 | frequency_hz=238.0
- [2026-08-28 19:21:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916116.5614412 | source=vosk | rms=1101 | updated_at=1787916115.0658195 | frequency_hz=238.0
- [2026-08-28 19:21:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916116.7810416 | source=vosk | rms=1101 | updated_at=1787916115.0658195 | frequency_hz=238.0
- [2026-08-28 19:21:56] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it is a similar
  meta: kind=partial | timestamp=1787916116.83918 | source=vosk | rms=1101 | updated_at=1787916115.0658195 | frequency_hz=238.0
- [2026-08-28 19:21:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916117.2805452 | source=vosk | rms=1122 | updated_at=1787916117.2805452 | frequency_hz=238.0
- [2026-08-28 19:21:57] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden
  meta: kind=partial | timestamp=1787916117.3293455 | source=vosk | rms=1122 | updated_at=1787916117.2805452 | frequency_hz=238.0
- [2026-08-28 19:21:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916117.7800865 | source=vosk | rms=1122 | updated_at=1787916117.2805452 | frequency_hz=238.0
- [2026-08-28 19:21:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916119.5297055 | source=vosk | rms=566 | updated_at=1787916119.5297055 | frequency_hz=238.0
- [2026-08-28 19:21:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916119.8018637 | source=vosk | rms=699 | updated_at=1787916119.8018637 | frequency_hz=238.0
- [2026-08-28 19:21:59] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it is this movie would have been
  meta: kind=partial | timestamp=1787916119.8551393 | source=vosk | rms=699 | updated_at=1787916119.8018637 | frequency_hz=238.0
- [2026-08-28 19:22:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916120.0521116 | source=vosk | rms=599 | updated_at=1787916120.0521116 | frequency_hz=238.0
- [2026-08-28 19:22:00] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it is this movie would have been rumblings
  meta: kind=partial | timestamp=1787916120.121405 | source=vosk | rms=599 | updated_at=1787916120.0521116 | frequency_hz=238.0
- [2026-08-28 19:22:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916120.2871706 | source=vosk | rms=621 | updated_at=1787916120.2871706 | frequency_hz=238.0
- [2026-08-28 19:22:00] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it is this movie would have been romantically
  meta: kind=partial | timestamp=1787916120.3556333 | source=vosk | rms=621 | updated_at=1787916120.2871706 | frequency_hz=238.0
- [2026-08-28 19:22:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916120.5298178 | source=vosk | rms=621 | updated_at=1787916120.2871706 | frequency_hz=238.0
- [2026-08-28 19:22:00] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up and
  meta: kind=partial | timestamp=1787916120.6245394 | source=vosk | rms=621 | updated_at=1787916120.2871706 | frequency_hz=238.0
- [2026-08-28 19:22:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916120.7805536 | source=vosk | rms=1136 | updated_at=1787916120.7805536 | frequency_hz=238.0
- [2026-08-28 19:22:00] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the
  meta: kind=partial | timestamp=1787916120.8186636 | source=vosk | rms=1136 | updated_at=1787916120.7805536 | frequency_hz=238.0
- [2026-08-28 19:22:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916121.282822 | source=vosk | rms=1136 | updated_at=1787916120.7805536 | frequency_hz=238.0
- [2026-08-28 19:22:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916121.5414133 | source=vosk | rms=1206 | updated_at=1787916121.5414133 | frequency_hz=238.0
- [2026-08-28 19:22:01] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the know
  meta: kind=partial | timestamp=1787916121.5924609 | source=vosk | rms=1206 | updated_at=1787916121.5414133 | frequency_hz=238.0
- [2026-08-28 19:22:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916122.0303414 | source=vosk | rms=1206 | updated_at=1787916121.5414133 | frequency_hz=238.0
- [2026-08-28 19:22:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916125.2896872 | source=vosk | rms=467 | updated_at=1787916125.2896872 | frequency_hz=238.0
- [2026-08-28 19:22:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916125.5302482 | source=vosk | rms=467 | updated_at=1787916125.2896872 | frequency_hz=238.0
- [2026-08-28 19:22:05] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no
  meta: kind=partial | timestamp=1787916125.5773337 | source=vosk | rms=467 | updated_at=1787916125.2896872 | frequency_hz=238.0
- [2026-08-28 19:22:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916125.818353 | source=vosk | rms=748 | updated_at=1787916125.818353 | frequency_hz=238.0
- [2026-08-28 19:22:05] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more
  meta: kind=partial | timestamp=1787916125.8491871 | source=vosk | rms=748 | updated_at=1787916125.818353 | frequency_hz=238.0
- [2026-08-28 19:22:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916126.0305395 | source=vosk | rms=633 | updated_at=1787916126.0305395 | frequency_hz=238.0
- [2026-08-28 19:22:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916126.279966 | source=vosk | rms=1203 | updated_at=1787916126.279966 | frequency_hz=238.0
- [2026-08-28 19:22:06] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want
  meta: kind=partial | timestamp=1787916126.3378983 | source=vosk | rms=1203 | updated_at=1787916126.279966 | frequency_hz=238.0
- [2026-08-28 19:22:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916126.5299933 | source=vosk | rms=843 | updated_at=1787916126.5299933 | frequency_hz=238.0
- [2026-08-28 19:22:06] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go
  meta: kind=partial | timestamp=1787916126.5914922 | source=vosk | rms=843 | updated_at=1787916126.5299933 | frequency_hz=238.0
- [2026-08-28 19:22:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916126.7798321 | source=vosk | rms=698 | updated_at=1787916126.7798321 | frequency_hz=238.0
- [2026-08-28 19:22:06] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bonkers
  meta: kind=partial | timestamp=1787916126.8174655 | source=vosk | rms=698 | updated_at=1787916126.7798321 | frequency_hz=238.0
- [2026-08-28 19:22:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916127.0301847 | source=vosk | rms=1200 | updated_at=1787916127.0301847 | frequency_hz=238.0
- [2026-08-28 19:22:07] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling for
  meta: kind=partial | timestamp=1787916127.121601 | source=vosk | rms=1200 | updated_at=1787916127.0301847 | frequency_hz=238.0
- [2026-08-28 19:22:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916127.2846673 | source=vosk | rms=1038 | updated_at=1787916127.2846673 | frequency_hz=238.0
- [2026-08-28 19:22:07] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to the guy being promoted
  meta: kind=partial | timestamp=1787916127.3389502 | source=vosk | rms=1038 | updated_at=1787916127.2846673 | frequency_hz=238.0
- [2026-08-28 19:22:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916127.5540516 | source=vosk | rms=526 | updated_at=1787916127.5540516 | frequency_hz=238.0
- [2026-08-28 19:22:07] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling for a while but
  meta: kind=partial | timestamp=1787916127.611482 | source=vosk | rms=526 | updated_at=1787916127.5540516 | frequency_hz=238.0
- [2026-08-28 19:22:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916127.7804015 | source=vosk | rms=621 | updated_at=1787916127.7804015 | frequency_hz=238.0
- [2026-08-28 19:22:07] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about
  meta: kind=partial | timestamp=1787916127.8018806 | source=vosk | rms=621 | updated_at=1787916127.7804015 | frequency_hz=238.0
- [2026-08-28 19:22:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916128.3100405 | source=vosk | rms=621 | updated_at=1787916127.7804015 | frequency_hz=238.0
- [2026-08-28 19:22:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916128.546087 | source=vosk | rms=621 | updated_at=1787916127.7804015 | frequency_hz=238.0
- [2026-08-28 19:22:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916128.7814667 | source=vosk | rms=495 | updated_at=1787916128.780946 | frequency_hz=238.0
- [2026-08-28 19:22:08] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about three
  meta: kind=partial | timestamp=1787916128.8126519 | source=vosk | rms=495 | updated_at=1787916128.780946 | frequency_hz=238.0
- [2026-08-28 19:22:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916129.0314035 | source=vosk | rms=495 | updated_at=1787916128.780946 | frequency_hz=238.0
- [2026-08-28 19:22:09] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were
  meta: kind=partial | timestamp=1787916129.0677109 | source=vosk | rms=495 | updated_at=1787916128.780946 | frequency_hz=238.0
- [2026-08-28 19:22:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916129.544636 | source=vosk | rms=495 | updated_at=1787916128.780946 | frequency_hz=238.0
- [2026-08-28 19:22:09] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were no
  meta: kind=partial | timestamp=1787916129.5859554 | source=vosk | rms=495 | updated_at=1787916128.780946 | frequency_hz=238.0
- [2026-08-28 19:22:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916129.7799072 | source=vosk | rms=1201 | updated_at=1787916129.7799072 | frequency_hz=238.0
- [2026-08-28 19:22:09] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were know what
  meta: kind=partial | timestamp=1787916129.8460808 | source=vosk | rms=1201 | updated_at=1787916129.7799072 | frequency_hz=238.0
- [2026-08-28 19:22:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916130.033747 | source=vosk | rms=749 | updated_at=1787916130.033747 | frequency_hz=238.0
- [2026-08-28 19:22:10] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were know what was
  meta: kind=partial | timestamp=1787916130.0969012 | source=vosk | rms=749 | updated_at=1787916130.033747 | frequency_hz=238.0
- [2026-08-28 19:22:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916130.2800562 | source=vosk | rms=749 | updated_at=1787916130.033747 | frequency_hz=238.0
- [2026-08-28 19:22:10] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were new ballparks
  meta: kind=partial | timestamp=1787916130.337433 | source=vosk | rms=749 | updated_at=1787916130.033747 | frequency_hz=238.0
- [2026-08-28 19:22:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916130.5308175 | source=vosk | rms=749 | updated_at=1787916130.033747 | frequency_hz=238.0
- [2026-08-28 19:22:10] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were new ballparks when
  meta: kind=partial | timestamp=1787916130.5837767 | source=vosk | rms=749 | updated_at=1787916130.033747 | frequency_hz=238.0
- [2026-08-28 19:22:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916131.0299144 | source=vosk | rms=749 | updated_at=1787916130.033747 | frequency_hz=238.0
- [2026-08-28 19:22:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916131.2799315 | source=vosk | rms=452 | updated_at=1787916131.2799315 | frequency_hz=238.0
- [2026-08-28 19:22:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916131.5307484 | source=vosk | rms=624 | updated_at=1787916131.5307484 | frequency_hz=238.0
- [2026-08-28 19:22:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916131.7814755 | source=vosk | rms=1204 | updated_at=1787916131.7814755 | frequency_hz=238.0
- [2026-08-28 19:22:11] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were new ballparks when the only
  meta: kind=partial | timestamp=1787916131.8091981 | source=vosk | rms=1204 | updated_at=1787916131.7814755 | frequency_hz=238.0
- [2026-08-28 19:22:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916132.127167 | source=vosk | rms=854 | updated_at=1787916132.127167 | frequency_hz=238.0
- [2026-08-28 19:22:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916132.3691711 | source=vosk | rms=854 | updated_at=1787916132.127167 | frequency_hz=238.0
- [2026-08-28 19:22:12] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were new ballparks when the only lebanon
  meta: kind=partial | timestamp=1787916132.3691711 | source=vosk | rms=854 | updated_at=1787916132.127167 | frequency_hz=238.0
- [2026-08-28 19:22:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916132.5533295 | source=vosk | rms=533 | updated_at=1787916132.5297906 | frequency_hz=238.0
- [2026-08-28 19:22:12] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were new ballparks when the only lebanon during
  meta: kind=partial | timestamp=1787916132.5533295 | source=vosk | rms=533 | updated_at=1787916132.5297906 | frequency_hz=238.0
- [2026-08-28 19:22:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916132.780734 | source=vosk | rms=1102 | updated_at=1787916132.780734 | frequency_hz=238.0
- [2026-08-28 19:22:12] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were new ballparks when the only lebanon done
  meta: kind=partial | timestamp=1787916132.8630843 | source=vosk | rms=1102 | updated_at=1787916132.780734 | frequency_hz=238.0
- [2026-08-28 19:22:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916133.0337217 | source=vosk | rms=1102 | updated_at=1787916133.0337217 | frequency_hz=238.0
- [2026-08-28 19:22:13] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were new ballparks when the only lebanon done in missouri
  meta: kind=partial | timestamp=1787916133.1103446 | source=vosk | rms=1102 | updated_at=1787916133.0337217 | frequency_hz=238.0
- [2026-08-28 19:22:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916133.5358896 | source=vosk | rms=448 | updated_at=1787916133.5358896 | frequency_hz=238.0
- [2026-08-28 19:22:13] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were new ballparks when the only lebanon done in wasn't
  meta: kind=partial | timestamp=1787916133.6446636 | source=vosk | rms=448 | updated_at=1787916133.5358896 | frequency_hz=238.0
- [2026-08-28 19:22:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916133.7810404 | source=vosk | rms=448 | updated_at=1787916133.5358896 | frequency_hz=238.0
- [2026-08-28 19:22:13] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were new ballparks when the only lebanon done in wasn't enough
  meta: kind=partial | timestamp=1787916133.8745778 | source=vosk | rms=448 | updated_at=1787916133.5358896 | frequency_hz=238.0
- [2026-08-28 19:22:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916134.032654 | source=vosk | rms=448 | updated_at=1787916133.5358896 | frequency_hz=238.0
- [2026-08-28 19:22:14] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were new ballparks when the only lebanon done in wasn't enough to the report
  meta: kind=partial | timestamp=1787916134.1427937 | source=vosk | rms=448 | updated_at=1787916133.5358896 | frequency_hz=238.0
- [2026-08-28 19:22:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916134.2802055 | source=vosk | rms=448 | updated_at=1787916133.5358896 | frequency_hz=238.0
- [2026-08-28 19:22:14] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were new ballparks when the only lebanon done in wasn't enough to live in brooklyn
  meta: kind=partial | timestamp=1787916134.3140311 | source=vosk | rms=448 | updated_at=1787916133.5358896 | frequency_hz=238.0
- [2026-08-28 19:22:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916134.530208 | source=vosk | rms=448 | updated_at=1787916133.5358896 | frequency_hz=238.0
- [2026-08-28 19:22:14] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were new ballparks when the only lebanon done in wasn't enough to live in brooklyn is
  meta: kind=partial | timestamp=1787916134.6172268 | source=vosk | rms=448 | updated_at=1787916133.5358896 | frequency_hz=238.0
- [2026-08-28 19:22:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916134.8033242 | source=vosk | rms=448 | updated_at=1787916133.5358896 | frequency_hz=238.0
- [2026-08-28 19:22:14] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were new ballparks when the only lebanon done in wasn't enough to live in brooklyn is all
  meta: kind=partial | timestamp=1787916134.876415 | source=vosk | rms=448 | updated_at=1787916133.5358896 | frequency_hz=238.0
- [2026-08-28 19:22:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916135.0309148 | source=vosk | rms=448 | updated_at=1787916133.5358896 | frequency_hz=238.0
- [2026-08-28 19:22:15] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were new ballparks when the only lebanon done in wasn't enough to live in brooklyn is all the
  meta: kind=partial | timestamp=1787916135.107351 | source=vosk | rms=448 | updated_at=1787916133.5358896 | frequency_hz=238.0
- [2026-08-28 19:22:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916135.5637944 | source=vosk | rms=448 | updated_at=1787916133.5358896 | frequency_hz=238.0
- [2026-08-28 19:22:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916136.0496516 | source=vosk | rms=427 | updated_at=1787916136.0496516 | frequency_hz=238.0
- [2026-08-28 19:22:16] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were new ballparks when the only lebanon done in wasn't enough to live in brooklyn is what are
  meta: kind=partial | timestamp=1787916136.0926547 | source=vosk | rms=427 | updated_at=1787916136.0496516 | frequency_hz=238.0
- [2026-08-28 19:22:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916136.2800415 | source=vosk | rms=449 | updated_at=1787916136.2800415 | frequency_hz=238.0
- [2026-08-28 19:22:16] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were new ballparks when the only lebanon done in wasn't enough to live in brooklyn is promoting to
  meta: kind=partial | timestamp=1787916136.3415623 | source=vosk | rms=449 | updated_at=1787916136.2800415 | frequency_hz=238.0
- [2026-08-28 19:22:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916136.5647762 | source=vosk | rms=573 | updated_at=1787916136.5647762 | frequency_hz=238.0
- [2026-08-28 19:22:16] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were new ballparks when the only lebanon done in wasn't enough to live in brooklyn is promoting two people
  meta: kind=partial | timestamp=1787916136.6175888 | source=vosk | rms=573 | updated_at=1787916136.5647762 | frequency_hz=238.0
- [2026-08-28 19:22:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916136.7828171 | source=vosk | rms=512 | updated_at=1787916136.7828171 | frequency_hz=238.0
- [2026-08-28 19:22:16] operator / voice_transcript_partial / voice: i do those are just a little doubt that are on earth or or on that program called it will get into trouble believing it three disease burden on one of them up the no more you want to go bowling promo about we were new ballparks when the only lebanon done in wasn't enough to live in brooklyn is promoting two people put
  meta: kind=partial | timestamp=1787916136.8353088 | source=vosk | rms=512 | updated_at=1787916136.7828171 | frequency_hz=238.0
- [2026-08-28 19:22:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916137.0319612 | source=vosk | rms=560 | updated_at=1787916137.0319612 | frequency_hz=238.0
- [2026-08-28 19:22:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916137.2839804 | source=vosk | rms=560 | updated_at=1787916137.0319612 | frequency_hz=238.0
- [2026-08-28 19:22:19] operator / voice_transcript_final / voice: i do those on just a little the that are on earth or or on that pokemon go bit get into trouble believing it three disease movie would have been prominent theme up the no more you want to go bowling promo about we were new ballparks when the only lebanon done in wasn t enough to live in brooklyn wondering what are you two people put on monday
  meta: kind=final | timestamp=1787916139.2531867 | source=final | rms=560 | updated_at=1787916137.0319612 | frequency_hz=238.0
- [2026-08-28 19:22:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916141.8035395 | source=vosk | rms=560 | updated_at=1787916137.0319612 | frequency_hz=238.0
- [2026-08-28 19:22:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916141.8035395 | source=vosk | rms=1200 | updated_at=1787916141.8035395 | frequency_hz=238.0
- [2026-08-28 19:22:21] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1787916141.8184898 | source=vosk | rms=1200 | updated_at=1787916141.8035395 | frequency_hz=238.0
- [2026-08-28 19:22:21] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1787916141.8404076 | source=vosk | rms=1147 | updated_at=1787916141.8184898 | frequency_hz=238.0
- [2026-08-28 19:22:21] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1787916141.8843515 | source=vosk | rms=367 | updated_at=1787916141.8404076 | frequency_hz=238.0
- [2026-08-28 19:22:21] operator / voice_transcript_partial / voice: he removed
  meta: kind=partial | timestamp=1787916141.9074502 | source=vosk | rms=975 | updated_at=1787916141.8843515 | frequency_hz=238.0
- [2026-08-28 19:22:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916142.0147812 | source=vosk | rms=1201 | updated_at=1787916141.946792 | frequency_hz=238.0
- [2026-08-28 19:22:22] operator / voice_transcript_partial / voice: he removed probably
  meta: kind=partial | timestamp=1787916142.0847316 | source=vosk | rms=1202 | updated_at=1787916142.0147812 | frequency_hz=238.0
- [2026-08-28 19:22:22] operator / voice_transcript_partial / voice: he removed probably due to
  meta: kind=partial | timestamp=1787916142.1279213 | source=vosk | rms=1204 | updated_at=1787916142.0857315 | frequency_hz=238.0
- [2026-08-28 19:22:22] operator / voice_transcript_partial / voice: he removed probably due to the
  meta: kind=partial | timestamp=1787916142.161002 | source=vosk | rms=1203 | updated_at=1787916142.1279213 | frequency_hz=238.0
- [2026-08-28 19:22:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916142.2257006 | source=vosk | rms=704 | updated_at=1787916142.161002 | frequency_hz=238.0
- [2026-08-28 19:22:22] operator / voice_transcript_partial / voice: he removed probably due to the middle
  meta: kind=partial | timestamp=1787916142.2257006 | source=vosk | rms=704 | updated_at=1787916142.161002 | frequency_hz=238.0
- [2026-08-28 19:22:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916143.0803897 | source=vosk | rms=1202 | updated_at=1787916142.3270733 | frequency_hz=238.0
- [2026-08-28 19:22:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916143.8008745 | source=vosk | rms=1202 | updated_at=1787916142.3270733 | frequency_hz=238.0
- [2026-08-28 19:22:23] operator / voice_transcript_partial / voice: he removed probably due to the middle new
  meta: kind=partial | timestamp=1787916143.8118868 | source=vosk | rms=1202 | updated_at=1787916142.3270733 | frequency_hz=238.0
- [2026-08-28 19:22:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916144.050865 | source=vosk | rms=1202 | updated_at=1787916142.3270733 | frequency_hz=238.0
- [2026-08-28 19:22:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916144.3288205 | source=vosk | rms=551 | updated_at=1787916144.3288205 | frequency_hz=238.0
- [2026-08-28 19:22:24] operator / voice_transcript_final / voice: the removed probably build a middle new
  meta: kind=final | timestamp=1787916144.6717184 | source=final | rms=551 | updated_at=1787916144.3288205 | frequency_hz=238.0
- [2026-08-28 19:22:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916144.8421516 | source=vosk | rms=551 | updated_at=1787916144.3288205 | frequency_hz=238.0
- [2026-08-28 19:22:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916144.8421516 | source=vosk | rms=551 | updated_at=1787916144.3288205 | frequency_hz=238.0
- [2026-08-28 19:22:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916146.5894113 | source=vosk | rms=551 | updated_at=1787916144.3288205 | frequency_hz=238.0
- [2026-08-28 19:22:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916146.8265107 | source=vosk | rms=551 | updated_at=1787916144.3288205 | frequency_hz=238.0
- [2026-08-28 19:22:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916147.5658264 | source=vosk | rms=551 | updated_at=1787916144.3288205 | frequency_hz=238.0
- [2026-08-28 19:22:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916147.8147087 | source=vosk | rms=551 | updated_at=1787916144.3288205 | frequency_hz=238.0
- [2026-08-28 19:22:28] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1787916148.3721466 | source=vosk | rms=731 | updated_at=1787916148.3008246 | frequency_hz=238.0
- [2026-08-28 19:22:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916148.579356 | source=vosk | rms=652 | updated_at=1787916148.579356 | frequency_hz=238.0
- [2026-08-28 19:22:28] operator / voice_transcript_partial / voice: which
  meta: kind=partial | timestamp=1787916148.6778247 | source=vosk | rms=652 | updated_at=1787916148.579356 | frequency_hz=238.0
- [2026-08-28 19:22:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916149.3322396 | source=vosk | rms=652 | updated_at=1787916148.579356 | frequency_hz=238.0
- [2026-08-28 19:22:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916149.56213 | source=vosk | rms=685 | updated_at=1787916149.56213 | frequency_hz=238.0
- [2026-08-28 19:22:29] operator / voice_transcript_partial / voice: which were
  meta: kind=partial | timestamp=1787916149.5776484 | source=vosk | rms=685 | updated_at=1787916149.56213 | frequency_hz=238.0
- [2026-08-28 19:22:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916149.8020105 | source=vosk | rms=1202 | updated_at=1787916149.8020105 | frequency_hz=238.0
- [2026-08-28 19:22:29] operator / voice_transcript_partial / voice: richard where they can
  meta: kind=partial | timestamp=1787916149.8491666 | source=vosk | rms=1202 | updated_at=1787916149.8020105 | frequency_hz=238.0
- [2026-08-28 19:22:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916150.0778978 | source=vosk | rms=1071 | updated_at=1787916150.0778978 | frequency_hz=238.0
- [2026-08-28 19:22:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916150.3129482 | source=vosk | rms=1200 | updated_at=1787916150.3129482 | frequency_hz=238.0
- [2026-08-28 19:22:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916151.4432337 | source=vosk | rms=1200 | updated_at=1787916151.4432337 | frequency_hz=238.0
- [2026-08-28 19:22:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916151.735744 | source=vosk | rms=1200 | updated_at=1787916151.735744 | frequency_hz=238.0
- [2026-08-28 19:22:32] operator / voice_transcript_final / voice: reached where they can be reached
  meta: kind=final | timestamp=1787916152.5626493 | source=final | rms=1200 | updated_at=1787916151.735744 | frequency_hz=238.0
- [2026-08-28 19:22:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916152.7299578 | source=vosk | rms=1200 | updated_at=1787916151.735744 | frequency_hz=238.0
- [2026-08-28 19:22:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916152.7299578 | source=vosk | rms=1200 | updated_at=1787916151.735744 | frequency_hz=238.0
- [2026-08-28 19:22:32] operator / voice_transcript_partial / voice: but
  meta: kind=partial | timestamp=1787916152.9902012 | source=vosk | rms=1728 | updated_at=1787916152.9489622 | frequency_hz=238.0
- [2026-08-28 19:22:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916153.2022767 | source=vosk | rms=1202 | updated_at=1787916153.2022767 | frequency_hz=238.0
- [2026-08-28 19:22:33] operator / voice_transcript_partial / voice: but i
  meta: kind=partial | timestamp=1787916153.2634423 | source=vosk | rms=1202 | updated_at=1787916153.2022767 | frequency_hz=238.0
- [2026-08-28 19:22:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916153.4441676 | source=vosk | rms=1201 | updated_at=1787916153.4441676 | frequency_hz=238.0
- [2026-08-28 19:22:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916153.7114165 | source=vosk | rms=1202 | updated_at=1787916153.7114165 | frequency_hz=238.0
- [2026-08-28 19:22:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916153.942268 | source=vosk | rms=1200 | updated_at=1787916153.942268 | frequency_hz=238.0
- [2026-08-28 19:22:34] operator / voice_transcript_final / voice: but the
  meta: kind=final | timestamp=1787916154.3832989 | source=final | rms=1200 | updated_at=1787916153.942268 | frequency_hz=238.0
- [2026-08-28 19:22:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916154.4352295 | source=vosk | rms=1200 | updated_at=1787916153.942268 | frequency_hz=238.0
- [2026-08-28 19:22:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916154.4352295 | source=vosk | rms=1202 | updated_at=1787916154.4352295 | frequency_hz=238.0
- [2026-08-28 19:22:34] operator / voice_transcript_partial / voice: we're not expecting
  meta: kind=partial | timestamp=1787916154.724185 | source=vosk | rms=1200 | updated_at=1787916154.690686 | frequency_hz=238.0
- [2026-08-28 19:22:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916154.940789 | source=vosk | rms=1204 | updated_at=1787916154.940789 | frequency_hz=238.0
- [2026-08-28 19:22:34] operator / voice_transcript_partial / voice: that experience
  meta: kind=partial | timestamp=1787916154.9687164 | source=vosk | rms=1204 | updated_at=1787916154.940789 | frequency_hz=238.0
- [2026-08-28 19:22:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916155.227844 | source=vosk | rms=867 | updated_at=1787916155.227844 | frequency_hz=238.0
- [2026-08-28 19:22:35] operator / voice_transcript_partial / voice: experian
  meta: kind=partial | timestamp=1787916155.278024 | source=vosk | rms=867 | updated_at=1787916155.227844 | frequency_hz=238.0
- [2026-08-28 19:22:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916155.4421906 | source=vosk | rms=1201 | updated_at=1787916155.4406874 | frequency_hz=238.0
- [2026-08-28 19:22:35] operator / voice_transcript_partial / voice: experian up
  meta: kind=partial | timestamp=1787916155.4949572 | source=vosk | rms=1201 | updated_at=1787916155.4406874 | frequency_hz=238.0
- [2026-08-28 19:22:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916155.7249408 | source=vosk | rms=1200 | updated_at=1787916155.7249408 | frequency_hz=238.0
- [2026-08-28 19:22:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916155.9439523 | source=vosk | rms=1200 | updated_at=1787916155.7249408 | frequency_hz=238.0
- [2026-08-28 19:22:36] operator / voice_transcript_partial / voice: experian up but i don't
  meta: kind=partial | timestamp=1787916156.0151842 | source=vosk | rms=1200 | updated_at=1787916155.7249408 | frequency_hz=238.0
- [2026-08-28 19:22:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916156.1910183 | source=vosk | rms=1200 | updated_at=1787916155.7249408 | frequency_hz=238.0
- [2026-08-28 19:22:36] operator / voice_transcript_partial / voice: experian up but i don't believe
  meta: kind=partial | timestamp=1787916156.2258208 | source=vosk | rms=1200 | updated_at=1787916155.7249408 | frequency_hz=238.0
- [2026-08-28 19:22:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916156.4470165 | source=vosk | rms=1201 | updated_at=1787916156.4470165 | frequency_hz=238.0
- [2026-08-28 19:22:36] operator / voice_transcript_partial / voice: experian up but i don't build a new
  meta: kind=partial | timestamp=1787916156.4841619 | source=vosk | rms=1201 | updated_at=1787916156.4470165 | frequency_hz=238.0
- [2026-08-28 19:22:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916156.7922602 | source=vosk | rms=1201 | updated_at=1787916156.4470165 | frequency_hz=238.0
- [2026-08-28 19:22:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916157.4406812 | source=vosk | rms=1201 | updated_at=1787916156.4470165 | frequency_hz=238.0
- [2026-08-28 19:22:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916158.4406364 | source=vosk | rms=849 | updated_at=1787916158.4406364 | frequency_hz=238.0
- [2026-08-28 19:22:38] operator / voice_transcript_partial / voice: experian up but i don't build a new welcome
  meta: kind=partial | timestamp=1787916158.5195174 | source=vosk | rms=849 | updated_at=1787916158.4406364 | frequency_hz=238.0
- [2026-08-28 19:22:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916158.7276628 | source=vosk | rms=1202 | updated_at=1787916158.7276628 | frequency_hz=238.0
- [2026-08-28 19:22:38] operator / voice_transcript_partial / voice: experian up but i don't build a new government buildings
  meta: kind=partial | timestamp=1787916158.773951 | source=vosk | rms=1202 | updated_at=1787916158.7276628 | frequency_hz=238.0
- [2026-08-28 19:22:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916158.9442792 | source=vosk | rms=1201 | updated_at=1787916158.9442792 | frequency_hz=238.0
- [2026-08-28 19:22:38] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen political
  meta: kind=partial | timestamp=1787916158.970071 | source=vosk | rms=1201 | updated_at=1787916158.9442792 | frequency_hz=238.0
- [2026-08-28 19:22:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916159.1914983 | source=vosk | rms=1204 | updated_at=1787916159.1914983 | frequency_hz=238.0
- [2026-08-28 19:22:39] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy gonna go
  meta: kind=partial | timestamp=1787916159.250786 | source=vosk | rms=1204 | updated_at=1787916159.1914983 | frequency_hz=238.0
- [2026-08-28 19:22:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916159.440917 | source=vosk | rms=1201 | updated_at=1787916159.440917 | frequency_hz=238.0
- [2026-08-28 19:22:39] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gun be
  meta: kind=partial | timestamp=1787916159.500745 | source=vosk | rms=1201 | updated_at=1787916159.440917 | frequency_hz=238.0
- [2026-08-28 19:22:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916159.6913204 | source=vosk | rms=1201 | updated_at=1787916159.6913204 | frequency_hz=238.0
- [2026-08-28 19:22:39] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gun be burned
  meta: kind=partial | timestamp=1787916159.7333143 | source=vosk | rms=1201 | updated_at=1787916159.6913204 | frequency_hz=238.0
- [2026-08-28 19:22:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916160.0440874 | source=vosk | rms=1201 | updated_at=1787916160.0440874 | frequency_hz=238.0
- [2026-08-28 19:22:40] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambit i love a good
  meta: kind=partial | timestamp=1787916160.1635413 | source=vosk | rms=1201 | updated_at=1787916160.0440874 | frequency_hz=238.0
- [2026-08-28 19:22:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916160.2781396 | source=vosk | rms=1203 | updated_at=1787916160.2159011 | frequency_hz=238.0
- [2026-08-28 19:22:40] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get any opposition
  meta: kind=partial | timestamp=1787916160.2781396 | source=vosk | rms=1203 | updated_at=1787916160.2159011 | frequency_hz=238.0
- [2026-08-28 19:22:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916160.4745843 | source=vosk | rms=1200 | updated_at=1787916160.4413075 | frequency_hz=238.0
- [2026-08-28 19:22:40] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens
  meta: kind=partial | timestamp=1787916160.4745843 | source=vosk | rms=1200 | updated_at=1787916160.4413075 | frequency_hz=238.0
- [2026-08-28 19:22:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916160.6907463 | source=vosk | rms=1201 | updated_at=1787916160.6907463 | frequency_hz=238.0
- [2026-08-28 19:22:40] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens a
  meta: kind=partial | timestamp=1787916160.7092123 | source=vosk | rms=1201 | updated_at=1787916160.6907463 | frequency_hz=238.0
- [2026-08-28 19:22:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916160.940924 | source=vosk | rms=1202 | updated_at=1787916160.940924 | frequency_hz=238.0
- [2026-08-28 19:22:40] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens ugly and
  meta: kind=partial | timestamp=1787916160.9701195 | source=vosk | rms=1202 | updated_at=1787916160.940924 | frequency_hz=238.0
- [2026-08-28 19:22:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916161.1941047 | source=vosk | rms=1201 | updated_at=1787916161.1941047 | frequency_hz=238.0
- [2026-08-28 19:22:41] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can
  meta: kind=partial | timestamp=1787916161.243472 | source=vosk | rms=1201 | updated_at=1787916161.1941047 | frequency_hz=238.0
- [2026-08-28 19:22:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916161.4715414 | source=vosk | rms=1201 | updated_at=1787916161.4715414 | frequency_hz=238.0
- [2026-08-28 19:22:41] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go
  meta: kind=partial | timestamp=1787916161.490758 | source=vosk | rms=1201 | updated_at=1787916161.4715414 | frequency_hz=238.0
- [2026-08-28 19:22:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916161.691503 | source=vosk | rms=1205 | updated_at=1787916161.691503 | frequency_hz=238.0
- [2026-08-28 19:22:41] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get
  meta: kind=partial | timestamp=1787916161.7070806 | source=vosk | rms=1205 | updated_at=1787916161.691503 | frequency_hz=238.0
- [2026-08-28 19:22:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916161.9413702 | source=vosk | rms=1202 | updated_at=1787916161.9413702 | frequency_hz=238.0
- [2026-08-28 19:22:41] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get a degree
  meta: kind=partial | timestamp=1787916161.9725099 | source=vosk | rms=1202 | updated_at=1787916161.9413702 | frequency_hz=238.0
- [2026-08-28 19:22:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916162.1908808 | source=vosk | rms=1201 | updated_at=1787916162.1908808 | frequency_hz=238.0
- [2026-08-28 19:22:42] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get the
  meta: kind=partial | timestamp=1787916162.2821665 | source=vosk | rms=1201 | updated_at=1787916162.1908808 | frequency_hz=238.0
- [2026-08-28 19:22:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916162.44743 | source=vosk | rms=1201 | updated_at=1787916162.44743 | frequency_hz=238.0
- [2026-08-28 19:22:42] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly
  meta: kind=partial | timestamp=1787916162.554395 | source=vosk | rms=1201 | updated_at=1787916162.44743 | frequency_hz=238.0
- [2026-08-28 19:22:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916162.692141 | source=vosk | rms=1201 | updated_at=1787916162.692141 | frequency_hz=238.0
- [2026-08-28 19:22:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916162.9413037 | source=vosk | rms=1205 | updated_at=1787916162.9413037 | frequency_hz=238.0
- [2026-08-28 19:22:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916163.190656 | source=vosk | rms=1203 | updated_at=1787916163.190656 | frequency_hz=238.0
- [2026-08-28 19:22:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916163.441257 | source=vosk | rms=1204 | updated_at=1787916163.441257 | frequency_hz=238.0
- [2026-08-28 19:22:43] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high
  meta: kind=partial | timestamp=1787916163.493346 | source=vosk | rms=1204 | updated_at=1787916163.441257 | frequency_hz=238.0
- [2026-08-28 19:22:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916163.698789 | source=vosk | rms=1202 | updated_at=1787916163.698789 | frequency_hz=238.0
- [2026-08-28 19:22:43] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but the
  meta: kind=partial | timestamp=1787916163.740926 | source=vosk | rms=1202 | updated_at=1787916163.698789 | frequency_hz=238.0
- [2026-08-28 19:22:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916163.9421773 | source=vosk | rms=1203 | updated_at=1787916163.9421773 | frequency_hz=238.0
- [2026-08-28 19:22:44] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was
  meta: kind=partial | timestamp=1787916164.018879 | source=vosk | rms=1203 | updated_at=1787916163.9421773 | frequency_hz=238.0
- [2026-08-28 19:22:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916164.1995845 | source=vosk | rms=1201 | updated_at=1787916164.1995845 | frequency_hz=238.0
- [2026-08-28 19:22:44] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was a
  meta: kind=partial | timestamp=1787916164.26295 | source=vosk | rms=1201 | updated_at=1787916164.1995845 | frequency_hz=238.0
- [2026-08-28 19:22:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916164.4406216 | source=vosk | rms=1202 | updated_at=1787916164.4406216 | frequency_hz=238.0
- [2026-08-28 19:22:44] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was a as you can go
  meta: kind=partial | timestamp=1787916164.4936013 | source=vosk | rms=1202 | updated_at=1787916164.4406216 | frequency_hz=238.0
- [2026-08-28 19:22:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916164.6964428 | source=vosk | rms=1201 | updated_at=1787916164.6964428 | frequency_hz=238.0
- [2026-08-28 19:22:44] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was urging me to
  meta: kind=partial | timestamp=1787916164.7685857 | source=vosk | rms=1201 | updated_at=1787916164.6964428 | frequency_hz=238.0
- [2026-08-28 19:22:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916164.9453144 | source=vosk | rms=1063 | updated_at=1787916164.9453144 | frequency_hz=238.0
- [2026-08-28 19:22:45] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was urging me to put
  meta: kind=partial | timestamp=1787916165.0022573 | source=vosk | rms=1063 | updated_at=1787916164.9453144 | frequency_hz=238.0
- [2026-08-28 19:22:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916165.1934748 | source=vosk | rms=852 | updated_at=1787916165.1934748 | frequency_hz=238.0
- [2026-08-28 19:22:45] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was urging me to put a
  meta: kind=partial | timestamp=1787916165.293614 | source=vosk | rms=852 | updated_at=1787916165.1934748 | frequency_hz=238.0
- [2026-08-28 19:22:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916165.4424677 | source=vosk | rms=1200 | updated_at=1787916165.4424677 | frequency_hz=238.0
- [2026-08-28 19:22:45] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was urging me to put us with
  meta: kind=partial | timestamp=1787916165.495456 | source=vosk | rms=1200 | updated_at=1787916165.4424677 | frequency_hz=238.0
- [2026-08-28 19:22:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916165.691335 | source=vosk | rms=1200 | updated_at=1787916165.691335 | frequency_hz=238.0
- [2026-08-28 19:22:45] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was urging me to put us with my
  meta: kind=partial | timestamp=1787916165.7682152 | source=vosk | rms=1200 | updated_at=1787916165.691335 | frequency_hz=238.0
- [2026-08-28 19:22:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916165.9640348 | source=vosk | rms=1201 | updated_at=1787916165.9640348 | frequency_hz=238.0
- [2026-08-28 19:22:46] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was urging me to put us with know what
  meta: kind=partial | timestamp=1787916166.1194048 | source=vosk | rms=1201 | updated_at=1787916165.9640348 | frequency_hz=238.0
- [2026-08-28 19:22:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916166.2324028 | source=vosk | rms=1200 | updated_at=1787916166.2324028 | frequency_hz=238.0
- [2026-08-28 19:22:46] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was urging me to put us with no i would look
  meta: kind=partial | timestamp=1787916166.3124316 | source=vosk | rms=1200 | updated_at=1787916166.2324028 | frequency_hz=238.0
- [2026-08-28 19:22:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916166.4680734 | source=vosk | rms=1088 | updated_at=1787916166.4680734 | frequency_hz=238.0
- [2026-08-28 19:22:46] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was urging me to put us with know what the founders
  meta: kind=partial | timestamp=1787916166.5465631 | source=vosk | rms=1088 | updated_at=1787916166.4680734 | frequency_hz=238.0
- [2026-08-28 19:22:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916166.7026463 | source=vosk | rms=1202 | updated_at=1787916166.7026463 | frequency_hz=238.0
- [2026-08-28 19:22:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916166.9410493 | source=vosk | rms=1202 | updated_at=1787916166.9410493 | frequency_hz=238.0
- [2026-08-28 19:22:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916167.2033527 | source=vosk | rms=1201 | updated_at=1787916167.2033527 | frequency_hz=238.0
- [2026-08-28 19:22:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916167.4786425 | source=vosk | rms=1201 | updated_at=1787916167.4786425 | frequency_hz=238.0
- [2026-08-28 19:22:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916167.6913545 | source=vosk | rms=1202 | updated_at=1787916167.6913545 | frequency_hz=238.0
- [2026-08-28 19:22:47] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was urging me to put us with know what the founders of my
  meta: kind=partial | timestamp=1787916167.7716506 | source=vosk | rms=1202 | updated_at=1787916167.6913545 | frequency_hz=238.0
- [2026-08-28 19:22:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916167.940884 | source=vosk | rms=1205 | updated_at=1787916167.940884 | frequency_hz=238.0
- [2026-08-28 19:22:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916168.1910412 | source=vosk | rms=1202 | updated_at=1787916168.1910412 | frequency_hz=238.0
- [2026-08-28 19:22:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916168.7228818 | source=vosk | rms=1202 | updated_at=1787916168.1910412 | frequency_hz=238.0
- [2026-08-28 19:22:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916169.203467 | source=vosk | rms=1201 | updated_at=1787916169.203467 | frequency_hz=238.0
- [2026-08-28 19:22:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916169.4409127 | source=vosk | rms=1201 | updated_at=1787916169.4409127 | frequency_hz=238.0
- [2026-08-28 19:22:49] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was urging me to put us with know what the founders of my name is carl pettersson
  meta: kind=partial | timestamp=1787916169.5264397 | source=vosk | rms=1201 | updated_at=1787916169.4409127 | frequency_hz=238.0
- [2026-08-28 19:22:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916169.7112174 | source=vosk | rms=1202 | updated_at=1787916169.7112174 | frequency_hz=238.0
- [2026-08-28 19:22:49] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was urging me to put us with know what the founders of my computer screen
  meta: kind=partial | timestamp=1787916169.7343612 | source=vosk | rms=1202 | updated_at=1787916169.7112174 | frequency_hz=238.0
- [2026-08-28 19:22:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916170.20265 | source=vosk | rms=1202 | updated_at=1787916170.20265 | frequency_hz=238.0
- [2026-08-28 19:22:50] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was urging me to put us with know what the founders of i use computers
  meta: kind=partial | timestamp=1787916170.272581 | source=vosk | rms=1202 | updated_at=1787916170.20265 | frequency_hz=238.0
- [2026-08-28 19:22:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916170.444192 | source=vosk | rms=1200 | updated_at=1787916170.4431872 | frequency_hz=238.0
- [2026-08-28 19:22:50] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was urging me to put us with know what the founders of i use computers through
  meta: kind=partial | timestamp=1787916170.509123 | source=vosk | rms=1200 | updated_at=1787916170.4431872 | frequency_hz=238.0
- [2026-08-28 19:22:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916170.7039394 | source=vosk | rms=1201 | updated_at=1787916170.7039394 | frequency_hz=238.0
- [2026-08-28 19:22:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916170.9709728 | source=vosk | rms=1133 | updated_at=1787916170.9709728 | frequency_hz=238.0
- [2026-08-28 19:22:51] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was urging me to put us with know what the founders of i use computers through modeling
  meta: kind=partial | timestamp=1787916171.0626423 | source=vosk | rms=1133 | updated_at=1787916170.9709728 | frequency_hz=238.0
- [2026-08-28 19:22:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916171.1924324 | source=vosk | rms=1200 | updated_at=1787916171.1924324 | frequency_hz=238.0
- [2026-08-28 19:22:51] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was urging me to put us with know what the founders of i use computers through modeling underwear
  meta: kind=partial | timestamp=1787916171.231376 | source=vosk | rms=1200 | updated_at=1787916171.1924324 | frequency_hz=238.0
- [2026-08-28 19:22:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916171.69171 | source=vosk | rms=1200 | updated_at=1787916171.1924324 | frequency_hz=238.0
- [2026-08-28 19:22:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916174.1918545 | source=vosk | rms=1204 | updated_at=1787916174.1918545 | frequency_hz=238.0
- [2026-08-28 19:22:54] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was urging me to put us with know what the founders of i use computers through modeling i'm gonna
  meta: kind=partial | timestamp=1787916174.2477086 | source=vosk | rms=1204 | updated_at=1787916174.1918545 | frequency_hz=238.0
- [2026-08-28 19:22:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916174.4413118 | source=vosk | rms=1204 | updated_at=1787916174.1918545 | frequency_hz=238.0
- [2026-08-28 19:22:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916174.7064674 | source=vosk | rms=1204 | updated_at=1787916174.1918545 | frequency_hz=238.0
- [2026-08-28 19:22:54] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was urging me to put us with know what the founders of i use computers through modeling i'm gonna are
  meta: kind=partial | timestamp=1787916174.7726064 | source=vosk | rms=1204 | updated_at=1787916174.1918545 | frequency_hz=238.0
- [2026-08-28 19:22:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916175.19125 | source=vosk | rms=1204 | updated_at=1787916174.1918545 | frequency_hz=238.0
- [2026-08-28 19:22:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916175.4416873 | source=vosk | rms=1202 | updated_at=1787916175.4416873 | frequency_hz=238.0
- [2026-08-28 19:22:55] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was urging me to put us with know what the founders of i use computers through modeling i'm gonna are you
  meta: kind=partial | timestamp=1787916175.4817371 | source=vosk | rms=1202 | updated_at=1787916175.4416873 | frequency_hz=238.0
- [2026-08-28 19:22:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916175.694843 | source=vosk | rms=1200 | updated_at=1787916175.694843 | frequency_hz=238.0
- [2026-08-28 19:22:55] operator / voice_transcript_partial / voice: experian up but i don't build a new bergen polygamy get a gambino never get you know what happens or gluons you can go get bigger the monopoly this too high but there was urging me to put us with know what the founders of i use computers through modeling i'm gonna are you know
  meta: kind=partial | timestamp=1787916175.7560709 | source=vosk | rms=1200 | updated_at=1787916175.694843 | frequency_hz=238.0
- [2026-08-28 19:22:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916175.9426143 | source=vosk | rms=1201 | updated_at=1787916175.9426143 | frequency_hz=238.0
- [2026-08-28 19:22:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916176.193504 | source=vosk | rms=1201 | updated_at=1787916175.9426143 | frequency_hz=238.0
- [2026-08-28 19:22:57] operator / voice_transcript_final / voice: experian up but i don t build a new bergen polygamy get a be never get you know what happens or gluons you can go get bigger the monopoly this too high but the was urging me to put us with know what the founders of my news use computers through modeling i m gonna are you know
  meta: kind=final | timestamp=1787916177.0617406 | source=final | rms=1201 | updated_at=1787916175.9426143 | frequency_hz=238.0
- [2026-08-28 19:22:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916177.689292 | source=vosk | rms=1201 | updated_at=1787916175.9426143 | frequency_hz=238.0
- [2026-08-28 19:22:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916177.689292 | source=vosk | rms=1205 | updated_at=1787916177.689292 | frequency_hz=238.0
- [2026-08-28 19:22:57] operator / voice_transcript_partial / voice: job
  meta: kind=partial | timestamp=1787916177.7857945 | source=vosk | rms=1205 | updated_at=1787916177.689292 | frequency_hz=238.0
- [2026-08-28 19:22:57] operator / voice_transcript_partial / voice: job the
  meta: kind=partial | timestamp=1787916177.8399224 | source=vosk | rms=1200 | updated_at=1787916177.7857945 | frequency_hz=238.0
- [2026-08-28 19:22:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916177.874827 | source=vosk | rms=1202 | updated_at=1787916177.8399224 | frequency_hz=238.0
- [2026-08-28 19:22:57] operator / voice_transcript_partial / voice: job the glad we didn't
  meta: kind=partial | timestamp=1787916177.9112682 | source=vosk | rms=1202 | updated_at=1787916177.874827 | frequency_hz=238.0
- [2026-08-28 19:22:57] operator / voice_transcript_partial / voice: job to go with
  meta: kind=partial | timestamp=1787916177.9826338 | source=vosk | rms=1160 | updated_at=1787916177.9112682 | frequency_hz=238.0
- [2026-08-28 19:22:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916178.4411175 | source=vosk | rms=1160 | updated_at=1787916177.9112682 | frequency_hz=238.0
- [2026-08-28 19:22:58] operator / voice_transcript_partial / voice: job the going on
  meta: kind=partial | timestamp=1787916178.5182905 | source=vosk | rms=1160 | updated_at=1787916177.9112682 | frequency_hz=238.0
- [2026-08-28 19:22:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916178.696165 | source=vosk | rms=1160 | updated_at=1787916177.9112682 | frequency_hz=238.0
- [2026-08-28 19:22:59] operator / voice_transcript_final / voice: job the going on
  meta: kind=final | timestamp=1787916179.1025028 | source=final | rms=1160 | updated_at=1787916177.9112682 | frequency_hz=238.0
- [2026-08-28 19:22:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916179.358592 | source=vosk | rms=1160 | updated_at=1787916177.9112682 | frequency_hz=238.0
- [2026-08-28 19:22:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916179.358592 | source=vosk | rms=1160 | updated_at=1787916177.9112682 | frequency_hz=238.0
- [2026-08-28 19:23:02] operator / voice_transcript_partial / voice: modernization
  meta: kind=partial | timestamp=1787916182.5258207 | source=vosk | rms=1203 | updated_at=1787916181.953839 | frequency_hz=339.2
- [2026-08-28 19:23:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916182.6916919 | source=vosk | rms=1203 | updated_at=1787916181.953839 | frequency_hz=339.2
- [2026-08-28 19:23:02] operator / voice_transcript_partial / voice: mountain is a pool because
  meta: kind=partial | timestamp=1787916182.7714047 | source=vosk | rms=1203 | updated_at=1787916181.953839 | frequency_hz=339.2
- [2026-08-28 19:23:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916183.1950216 | source=vosk | rms=1203 | updated_at=1787916181.953839 | frequency_hz=339.2
- [2026-08-28 19:23:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916183.941526 | source=vosk | rms=1182 | updated_at=1787916183.941526 | frequency_hz=339.2
- [2026-08-28 19:23:03] operator / voice_transcript_partial / voice: mountain is it will be going
  meta: kind=partial | timestamp=1787916183.9601395 | source=vosk | rms=1182 | updated_at=1787916183.941526 | frequency_hz=339.2
- [2026-08-28 19:23:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916184.4413676 | source=vosk | rms=1182 | updated_at=1787916183.941526 | frequency_hz=339.2
- [2026-08-28 19:23:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916185.191651 | source=vosk | rms=1202 | updated_at=1787916185.191651 | frequency_hz=339.2
- [2026-08-28 19:23:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916185.6918314 | source=vosk | rms=1202 | updated_at=1787916185.191651 | frequency_hz=339.2
- [2026-08-28 19:23:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916185.9458857 | source=vosk | rms=1202 | updated_at=1787916185.191651 | frequency_hz=339.2
- [2026-08-28 19:23:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916186.4414587 | source=vosk | rms=1202 | updated_at=1787916185.191651 | frequency_hz=339.2
- [2026-08-28 19:23:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916186.9585078 | source=vosk | rms=1202 | updated_at=1787916185.191651 | frequency_hz=339.2
- [2026-08-28 19:23:07] operator / voice_transcript_final / voice: modeled is a pool begun
  meta: kind=final | timestamp=1787916187.2879684 | source=final | rms=1202 | updated_at=1787916185.191651 | frequency_hz=339.2
- [2026-08-28 19:23:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916187.799642 | source=vosk | rms=1202 | updated_at=1787916185.191651 | frequency_hz=339.2
- [2026-08-28 19:23:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916187.799642 | source=vosk | rms=1202 | updated_at=1787916185.191651 | frequency_hz=339.2
- [2026-08-28 19:23:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916190.7248359 | source=vosk | rms=1202 | updated_at=1787916185.191651 | frequency_hz=339.2
- [2026-08-28 19:23:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916191.2104402 | source=vosk | rms=1202 | updated_at=1787916185.191651 | frequency_hz=339.2
- [2026-08-28 19:23:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916194.486037 | source=vosk | rms=1049 | updated_at=1787916193.9442537 | frequency_hz=339.2
- [2026-08-28 19:23:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916205.6932933 | source=vosk | rms=598 | updated_at=1787916205.6932933 | frequency_hz=276.0
- [2026-08-28 19:23:25] operator / voice_transcript_partial / voice: tracking pause going to guard
  meta: kind=partial | timestamp=1787916205.7417934 | source=vosk | rms=598 | updated_at=1787916205.6932933 | frequency_hz=276.0
- [2026-08-28 19:23:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916205.9573696 | source=vosk | rms=543 | updated_at=1787916205.9573696 | frequency_hz=225.6
- [2026-08-28 19:23:25] operator / voice_transcript_partial / voice: tracking pause going to guard whole notion
  meta: kind=partial | timestamp=1787916205.9931986 | source=vosk | rms=543 | updated_at=1787916205.9573696 | frequency_hz=225.6
- [2026-08-28 19:23:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916206.225069 | source=vosk | rms=576 | updated_at=1787916206.225069 | frequency_hz=255.1
- [2026-08-28 19:23:26] operator / voice_transcript_partial / voice: tracking pause going to guard hornish
  meta: kind=partial | timestamp=1787916206.2507613 | source=vosk | rms=576 | updated_at=1787916206.225069 | frequency_hz=255.1
- [2026-08-28 19:23:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916206.4853506 | source=vosk | rms=531 | updated_at=1787916206.4853506 | frequency_hz=247.7
- [2026-08-28 19:23:26] operator / voice_transcript_final / voice: tracking pause going to guard hornish
  meta: kind=final | timestamp=1787916206.825585 | source=final | rms=531 | updated_at=1787916206.4853506 | frequency_hz=247.7
- [2026-08-28 19:23:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916207.1655657 | source=vosk | rms=531 | updated_at=1787916206.4853506 | frequency_hz=247.7
- [2026-08-28 19:23:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916207.1655657 | source=vosk | rms=531 | updated_at=1787916206.4853506 | frequency_hz=247.7
- [2026-08-28 19:23:29] operator / voice_transcript_partial / voice: mr
  meta: kind=partial | timestamp=1787916209.4914505 | source=vosk | rms=509 | updated_at=1787916209.4420187 | frequency_hz=166.1
- [2026-08-28 19:23:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916209.691954 | source=vosk | rms=506 | updated_at=1787916209.691954 | frequency_hz=172.4
- [2026-08-28 19:23:29] operator / voice_transcript_partial / voice: mr procure
  meta: kind=partial | timestamp=1787916209.7317765 | source=vosk | rms=506 | updated_at=1787916209.691954 | frequency_hz=172.4
- [2026-08-28 19:23:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916209.947509 | source=vosk | rms=506 | updated_at=1787916209.691954 | frequency_hz=172.4
- [2026-08-28 19:23:29] operator / voice_transcript_partial / voice: mr procure know
  meta: kind=partial | timestamp=1787916209.999412 | source=vosk | rms=506 | updated_at=1787916209.691954 | frequency_hz=172.4
- [2026-08-28 19:23:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916210.471097 | source=vosk | rms=506 | updated_at=1787916209.691954 | frequency_hz=172.4
- [2026-08-28 19:23:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916210.722459 | source=vosk | rms=506 | updated_at=1787916209.691954 | frequency_hz=172.4
- [2026-08-28 19:23:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916210.9423716 | source=vosk | rms=498 | updated_at=1787916210.9423716 | frequency_hz=144.3
- [2026-08-28 19:23:31] operator / voice_transcript_final / voice: mr procure know
  meta: kind=final | timestamp=1787916211.2252765 | source=final | rms=498 | updated_at=1787916210.9423716 | frequency_hz=144.3
- [2026-08-28 19:23:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916211.3510616 | source=vosk | rms=613 | updated_at=1787916211.3510616 | frequency_hz=133.0
- [2026-08-28 19:23:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916214.2146842 | source=vosk | rms=485 | updated_at=1787916213.2055178 | frequency_hz=175.5
- [2026-08-28 19:23:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916214.692205 | source=vosk | rms=485 | updated_at=1787916213.2055178 | frequency_hz=175.5
- [2026-08-28 19:23:36] operator / voice_transcript_partial / voice: snowboarders
  meta: kind=partial | timestamp=1787916216.9936302 | source=vosk | rms=834 | updated_at=1787916216.6949313 | frequency_hz=175.5
- [2026-08-28 19:23:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916217.1946108 | source=vosk | rms=1201 | updated_at=1787916217.1946108 | frequency_hz=175.5
- [2026-08-28 19:23:37] operator / voice_transcript_partial / voice: snowboard
  meta: kind=partial | timestamp=1787916217.2373772 | source=vosk | rms=1201 | updated_at=1787916217.1946108 | frequency_hz=175.5
- [2026-08-28 19:23:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916217.4456499 | source=vosk | rms=762 | updated_at=1787916217.4456499 | frequency_hz=175.5
- [2026-08-28 19:23:37] operator / voice_transcript_partial / voice: snowboarder
  meta: kind=partial | timestamp=1787916217.503805 | source=vosk | rms=762 | updated_at=1787916217.4456499 | frequency_hz=175.5
- [2026-08-28 19:23:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916217.9680164 | source=vosk | rms=762 | updated_at=1787916217.4456499 | frequency_hz=175.5
- [2026-08-28 19:23:37] operator / voice_transcript_partial / voice: snowboarder speech
  meta: kind=partial | timestamp=1787916217.9787722 | source=vosk | rms=762 | updated_at=1787916217.4456499 | frequency_hz=175.5
- [2026-08-28 19:23:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916218.2062678 | source=vosk | rms=762 | updated_at=1787916217.4456499 | frequency_hz=175.5
- [2026-08-28 19:23:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916218.700994 | source=vosk | rms=762 | updated_at=1787916217.4456499 | frequency_hz=175.5
- [2026-08-28 19:23:39] operator / voice_transcript_final / voice: snowboarder speech
  meta: kind=final | timestamp=1787916219.6077042 | source=final | rms=762 | updated_at=1787916217.4456499 | frequency_hz=175.5
- [2026-08-28 19:23:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916219.6646616 | source=vosk | rms=762 | updated_at=1787916217.4456499 | frequency_hz=175.5
- [2026-08-28 19:23:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916219.6646616 | source=vosk | rms=402 | updated_at=1787916219.6646616 | frequency_hz=175.5
- [2026-08-28 19:23:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916220.1526291 | source=vosk | rms=995 | updated_at=1787916219.724931 | frequency_hz=175.5
- [2026-08-28 19:23:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916220.4018328 | source=vosk | rms=931 | updated_at=1787916220.4018328 | frequency_hz=238.0
- [2026-08-28 19:23:40] operator / voice_transcript_partial / voice: lucy
  meta: kind=partial | timestamp=1787916220.6906025 | source=vosk | rms=931 | updated_at=1787916220.4018328 | frequency_hz=238.0
- [2026-08-28 19:23:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916220.9426072 | source=vosk | rms=495 | updated_at=1787916220.9426072 | frequency_hz=238.0
- [2026-08-28 19:23:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916221.16976 | source=vosk | rms=495 | updated_at=1787916220.9426072 | frequency_hz=238.0
- [2026-08-28 19:23:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916221.4022753 | source=vosk | rms=466 | updated_at=1787916221.4022753 | frequency_hz=238.0
- [2026-08-28 19:23:41] operator / voice_transcript_final / voice: lucy groups
  meta: kind=final | timestamp=1787916221.6131823 | source=final | rms=466 | updated_at=1787916221.4022753 | frequency_hz=238.0
- [2026-08-28 19:23:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916221.9026363 | source=vosk | rms=466 | updated_at=1787916221.4022753 | frequency_hz=238.0
- [2026-08-28 19:23:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916222.9176316 | source=vosk | rms=466 | updated_at=1787916221.4022753 | frequency_hz=238.0
- [2026-08-28 19:23:46] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1787916226.6748133 | source=vosk | rms=326 | updated_at=1787916226.6525817 | frequency_hz=251.1
- [2026-08-28 19:23:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916226.93136 | source=vosk | rms=326 | updated_at=1787916226.6525817 | frequency_hz=251.1
- [2026-08-28 19:23:46] operator / voice_transcript_partial / voice: to school
  meta: kind=partial | timestamp=1787916226.991674 | source=vosk | rms=326 | updated_at=1787916226.6525817 | frequency_hz=251.1
- [2026-08-28 19:23:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916227.184698 | source=vosk | rms=326 | updated_at=1787916226.6525817 | frequency_hz=251.1
- [2026-08-28 19:23:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916227.41915 | source=vosk | rms=589 | updated_at=1787916227.41915 | frequency_hz=297.6
- [2026-08-28 19:23:47] operator / voice_transcript_final / voice: to school
  meta: kind=final | timestamp=1787916227.6238713 | source=final | rms=589 | updated_at=1787916227.41915 | frequency_hz=297.6
- [2026-08-28 19:23:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916227.653908 | source=vosk | rms=330 | updated_at=1787916227.653908 | frequency_hz=214.4
- [2026-08-28 19:23:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916230.6529207 | source=vosk | rms=318 | updated_at=1787916229.9027164 | frequency_hz=117.9
- [2026-08-28 19:23:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916230.9074779 | source=vosk | rms=318 | updated_at=1787916229.9027164 | frequency_hz=117.9
- [2026-08-28 19:23:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787916234.769402 | source=vosk | rms=607 | updated_at=1787916234.2258985 | frequency_hz=172.4
- [2026-08-28 19:23:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787916235.7279294 | source=vosk | rms=607 | updated_at=1787916234.2258985 | frequency_hz=172.4

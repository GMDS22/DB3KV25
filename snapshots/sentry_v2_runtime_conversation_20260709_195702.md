# SMART SENTRY V5.0.0 Runtime Conversation Export

- Generated: 2026-07-09 19:57:02
- Entries: 1068
- Roles: {'assistant': 5, 'system': 902, 'operator': 161}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 902, 'spoken_confirmation': 3, 'voice_transcript_final': 32, 'voice_transcript_partial': 127, 'voice_command': 2}
- Channels: {'text': 2, 'voice': 1066}
- Latest operator request: so
- Latest assistant message: Smart Sentry is already connected and enabled.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-07-09 19:38:06] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-07-09 19:38:06] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-07-09 19:38:09] system / voice_status / voice: listening
  meta: kind=status | timestamp=1783597089.0249982 | source=vosk
- [2026-07-09 19:38:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597089.9007726 | source=vosk | rms=605 | updated_at=1783597089.9007726
- [2026-07-09 19:38:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597090.8917584 | source=vosk | rms=605 | updated_at=1783597089.9007726
- [2026-07-09 19:38:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597091.6420274 | source=vosk | rms=127 | updated_at=1783597091.6420274
- [2026-07-09 19:38:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597092.709717 | source=vosk | rms=158 | updated_at=1783597091.8918545
- [2026-07-09 19:38:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597096.4521298 | source=vosk | rms=356 | updated_at=1783597096.4521298
- [2026-07-09 19:38:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597097.4521935 | source=vosk | rms=283 | updated_at=1783597096.9533718
- [2026-07-09 19:38:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597097.952355 | source=vosk | rms=270 | updated_at=1783597097.952355
- [2026-07-09 19:38:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597098.9518657 | source=vosk | rms=268 | updated_at=1783597098.4554143
- [2026-07-09 19:38:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597099.2023888 | source=vosk | rms=204 | updated_at=1783597099.2023888 | frequency_hz=364.0
- [2026-07-09 19:38:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597099.7023132 | source=vosk | rms=204 | updated_at=1783597099.2023888 | frequency_hz=364.0
- [2026-07-09 19:38:43] assistant / spoken_confirmation / voice: Smart Sentry is ready.
  meta: interrupt=True | assistant_output=False | spoken=True
- [2026-07-09 19:38:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597100.4522092 | source=vosk | rms=125 | updated_at=1783597100.4522092 | frequency_hz=364.0
- [2026-07-09 19:38:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597101.2027626 | source=vosk | rms=141 | updated_at=1783597100.701731 | frequency_hz=364.0
- [2026-07-09 19:38:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597101.7020657 | source=vosk | rms=181 | updated_at=1783597101.7020657 | frequency_hz=364.0
- [2026-07-09 19:38:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597102.2022612 | source=vosk | rms=181 | updated_at=1783597101.7020657 | frequency_hz=364.0
- [2026-07-09 19:38:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597105.9526486 | source=vosk | rms=155 | updated_at=1783597105.9526486 | frequency_hz=364.0
- [2026-07-09 19:38:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597106.7015562 | source=vosk | rms=155 | updated_at=1783597105.9526486 | frequency_hz=364.0
- [2026-07-09 19:38:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597108.2024033 | source=vosk | rms=155 | updated_at=1783597105.9526486 | frequency_hz=364.0
- [2026-07-09 19:38:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597110.2027893 | source=vosk | rms=429 | updated_at=1783597109.7024717 | frequency_hz=364.0
- [2026-07-09 19:38:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597110.451881 | source=vosk | rms=123 | updated_at=1783597110.451881 | frequency_hz=364.0
- [2026-07-09 19:38:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597110.9534297 | source=vosk | rms=123 | updated_at=1783597110.451881 | frequency_hz=364.0
- [2026-07-09 19:38:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597112.4524584 | source=vosk | rms=258 | updated_at=1783597112.4524584 | frequency_hz=364.0
- [2026-07-09 19:38:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597113.7025328 | source=vosk | rms=827 | updated_at=1783597113.202329 | frequency_hz=364.0
- [2026-07-09 19:38:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597115.4527512 | source=vosk | rms=827 | updated_at=1783597113.202329 | frequency_hz=364.0
- [2026-07-09 19:38:39] operator / voice_transcript_final / voice: say something funny
  meta: kind=final | timestamp=1783597119.4273963 | source=final | rms=905 | updated_at=1783597119.2018654 | frequency_hz=364.0
- [2026-07-09 19:38:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597120.3526876 | source=vosk | rms=905 | updated_at=1783597119.2018654 | frequency_hz=364.0
- [2026-07-09 19:38:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597120.3526876 | source=vosk | rms=222 | updated_at=1783597120.3526876 | frequency_hz=364.0
- [2026-07-09 19:38:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597125.2028081 | source=vosk | rms=207 | updated_at=1783597124.7057903 | frequency_hz=324.8
- [2026-07-09 19:38:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597127.4528992 | source=vosk | rms=262 | updated_at=1783597127.4528992 | frequency_hz=324.8
- [2026-07-09 19:38:48] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1783597128.3087306 | source=vosk | rms=278 | updated_at=1783597128.2029247 | frequency_hz=324.8
- [2026-07-09 19:38:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597128.4526386 | source=vosk | rms=424 | updated_at=1783597128.4526386 | frequency_hz=324.8
- [2026-07-09 19:38:48] operator / voice_transcript_partial / voice: smart century is
  meta: kind=partial | timestamp=1783597128.497542 | source=vosk | rms=424 | updated_at=1783597128.4526386 | frequency_hz=324.8
- [2026-07-09 19:38:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597128.9527273 | source=vosk | rms=424 | updated_at=1783597128.4526386 | frequency_hz=324.8
- [2026-07-09 19:38:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597131.2026246 | source=vosk | rms=1200 | updated_at=1783597131.2026246 | frequency_hz=324.8
- [2026-07-09 19:38:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597131.4581141 | source=vosk | rms=433 | updated_at=1783597131.4581141 | frequency_hz=324.8
- [2026-07-09 19:38:51] operator / voice_transcript_partial / voice: smart century his reputation
  meta: kind=partial | timestamp=1783597131.5094593 | source=vosk | rms=433 | updated_at=1783597131.4581141 | frequency_hz=324.8
- [2026-07-09 19:38:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597131.9525936 | source=vosk | rms=433 | updated_at=1783597131.4581141 | frequency_hz=324.8
- [2026-07-09 19:38:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597132.2024226 | source=vosk | rms=1205 | updated_at=1783597132.2024226 | frequency_hz=324.8
- [2026-07-09 19:38:52] operator / voice_transcript_partial / voice: smart century is right billion
  meta: kind=partial | timestamp=1783597132.2706113 | source=vosk | rms=1205 | updated_at=1783597132.2024226 | frequency_hz=324.8
- [2026-07-09 19:38:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597132.452748 | source=vosk | rms=1206 | updated_at=1783597132.452748 | frequency_hz=324.8
- [2026-07-09 19:38:52] operator / voice_transcript_partial / voice: smart century is rarely a
  meta: kind=partial | timestamp=1783597132.531556 | source=vosk | rms=1206 | updated_at=1783597132.452748 | frequency_hz=324.8
- [2026-07-09 19:38:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597132.7026541 | source=vosk | rms=348 | updated_at=1783597132.7026541 | frequency_hz=324.8
- [2026-07-09 19:38:52] operator / voice_transcript_partial / voice: smart century is rarely i run
  meta: kind=partial | timestamp=1783597132.7565944 | source=vosk | rms=348 | updated_at=1783597132.7026541 | frequency_hz=324.8
- [2026-07-09 19:38:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597132.9539995 | source=vosk | rms=1034 | updated_at=1783597132.9539995 | frequency_hz=324.8
- [2026-07-09 19:38:52] operator / voice_transcript_partial / voice: smart century is rarely i run the
  meta: kind=partial | timestamp=1783597132.9872997 | source=vosk | rms=1034 | updated_at=1783597132.9539995 | frequency_hz=324.8
- [2026-07-09 19:38:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597133.202498 | source=vosk | rms=1021 | updated_at=1783597133.202498 | frequency_hz=324.8
- [2026-07-09 19:38:53] operator / voice_transcript_partial / voice: smart century is rarely i rubbed a smart
  meta: kind=partial | timestamp=1783597133.2148705 | source=vosk | rms=1021 | updated_at=1783597133.202498 | frequency_hz=324.8
- [2026-07-09 19:38:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597133.453803 | source=vosk | rms=645 | updated_at=1783597133.453803 | frequency_hz=324.8
- [2026-07-09 19:38:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597133.9539373 | source=vosk | rms=1114 | updated_at=1783597133.9539373 | frequency_hz=324.8
- [2026-07-09 19:38:53] operator / voice_transcript_partial / voice: smart century is rarely i rubbed a smart sentry
  meta: kind=partial | timestamp=1783597133.9818466 | source=vosk | rms=1114 | updated_at=1783597133.9539373 | frequency_hz=324.8
- [2026-07-09 19:38:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597134.4526231 | source=vosk | rms=1114 | updated_at=1783597133.9539373 | frequency_hz=324.8
- [2026-07-09 19:38:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597134.9538233 | source=vosk | rms=1114 | updated_at=1783597133.9539373 | frequency_hz=324.8
- [2026-07-09 19:38:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597135.458326 | source=vosk | rms=1114 | updated_at=1783597133.9539373 | frequency_hz=324.8
- [2026-07-09 19:38:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597136.702725 | source=vosk | rms=373 | updated_at=1783597136.702725 | frequency_hz=324.8
- [2026-07-09 19:38:56] operator / voice_transcript_partial / voice: smart century is rarely i rubbed a smart sentry i
  meta: kind=partial | timestamp=1783597136.7154176 | source=vosk | rms=373 | updated_at=1783597136.702725 | frequency_hz=324.8
- [2026-07-09 19:38:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597137.202414 | source=vosk | rms=373 | updated_at=1783597136.702725 | frequency_hz=324.8
- [2026-07-09 19:38:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597139.953523 | source=vosk | rms=874 | updated_at=1783597139.953523 | frequency_hz=324.8
- [2026-07-09 19:39:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597140.4532661 | source=vosk | rms=874 | updated_at=1783597139.953523 | frequency_hz=324.8
- [2026-07-09 19:39:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597140.7029104 | source=vosk | rms=1202 | updated_at=1783597140.7029104 | frequency_hz=324.8
- [2026-07-09 19:39:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597140.957749 | source=vosk | rms=436 | updated_at=1783597140.957749 | frequency_hz=324.8
- [2026-07-09 19:39:00] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1783597140.9790332 | source=final | rms=436 | updated_at=1783597140.957749 | frequency_hz=324.8
- [2026-07-09 19:39:01] system / voice_status / voice: processing
  meta: kind=status | timestamp=1783597141.018006 | source=state | rms=436 | updated_at=1783597140.957749 | frequency_hz=324.8
- [2026-07-09 19:39:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597141.018006 | source=state | rms=436 | updated_at=1783597140.957749 | frequency_hz=324.8
- [2026-07-09 19:39:01] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-07-09 19:39:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597141.2031798 | source=vosk | rms=444 | updated_at=1783597141.2031798 | frequency_hz=324.8
- [2026-07-09 19:39:01] assistant / spoken_confirmation / voice: Running Smart Sentry now. Connecting the Smart Sentry boards first.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-07-09 19:39:02] operator / voice_transcript_partial / voice: had he
  meta: kind=partial | timestamp=1783597142.7917619 | source=vosk | rms=667 | updated_at=1783597142.7025673 | frequency_hz=324.8
- [2026-07-09 19:39:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597142.953955 | source=vosk | rms=776 | updated_at=1783597142.953955 | frequency_hz=324.8
- [2026-07-09 19:39:03] operator / voice_transcript_partial / voice: opponents
  meta: kind=partial | timestamp=1783597143.433839 | source=vosk | rms=571 | updated_at=1783597143.2030325 | frequency_hz=324.8
- [2026-07-09 19:39:03] operator / voice_transcript_partial / voice: a lot of time and
  meta: kind=partial | timestamp=1783597143.481604 | source=vosk | rms=571 | updated_at=1783597143.2030325 | frequency_hz=324.8
- [2026-07-09 19:39:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597143.7030692 | source=vosk | rms=571 | updated_at=1783597143.2030325 | frequency_hz=324.8
- [2026-07-09 19:39:03] operator / voice_transcript_partial / voice: a lot of time and smart
  meta: kind=partial | timestamp=1783597143.72599 | source=vosk | rms=571 | updated_at=1783597143.2030325 | frequency_hz=324.8
- [2026-07-09 19:39:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597143.952963 | source=vosk | rms=1201 | updated_at=1783597143.952963 | frequency_hz=324.8
- [2026-07-09 19:39:03] operator / voice_transcript_partial / voice: a lot of time and smart centered
  meta: kind=partial | timestamp=1783597143.997716 | source=vosk | rms=1201 | updated_at=1783597143.952963 | frequency_hz=324.8
- [2026-07-09 19:39:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597144.452949 | source=vosk | rms=583 | updated_at=1783597144.452949 | frequency_hz=324.8
- [2026-07-09 19:39:04] operator / voice_transcript_partial / voice: a lot of time and smart centered not like
  meta: kind=partial | timestamp=1783597144.5449646 | source=vosk | rms=583 | updated_at=1783597144.452949 | frequency_hz=324.8
- [2026-07-09 19:39:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597144.7039123 | source=vosk | rms=639 | updated_at=1783597144.7039123 | frequency_hz=324.8
- [2026-07-09 19:39:04] operator / voice_transcript_partial / voice: a lot of time and smart centered not like if
  meta: kind=partial | timestamp=1783597144.7875426 | source=vosk | rms=639 | updated_at=1783597144.7039123 | frequency_hz=324.8
- [2026-07-09 19:39:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597144.9538796 | source=vosk | rms=489 | updated_at=1783597144.9538796 | frequency_hz=324.8
- [2026-07-09 19:39:05] operator / voice_transcript_partial / voice: a lot of time and smart centered not
  meta: kind=partial | timestamp=1783597145.0398288 | source=vosk | rms=489 | updated_at=1783597144.9538796 | frequency_hz=324.8
- [2026-07-09 19:39:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597145.2030878 | source=vosk | rms=726 | updated_at=1783597145.2030878 | frequency_hz=324.8
- [2026-07-09 19:39:05] operator / voice_transcript_partial / voice: a lot of time and smart centered not connecting with
  meta: kind=partial | timestamp=1783597145.2226431 | source=vosk | rms=726 | updated_at=1783597145.2030878 | frequency_hz=324.8
- [2026-07-09 19:39:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597145.4531207 | source=vosk | rms=726 | updated_at=1783597145.2030878 | frequency_hz=324.8
- [2026-07-09 19:39:05] operator / voice_transcript_partial / voice: a lot of time and smart centered not connecting the
  meta: kind=partial | timestamp=1783597145.495909 | source=vosk | rms=726 | updated_at=1783597145.2030878 | frequency_hz=324.8
- [2026-07-09 19:39:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597145.7032435 | source=vosk | rms=726 | updated_at=1783597145.2030878 | frequency_hz=324.8
- [2026-07-09 19:39:05] operator / voice_transcript_partial / voice: a lot of time and smart centered not connecting with smart
  meta: kind=partial | timestamp=1783597145.7148798 | source=vosk | rms=726 | updated_at=1783597145.2030878 | frequency_hz=324.8
- [2026-07-09 19:39:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597145.9524958 | source=vosk | rms=829 | updated_at=1783597145.9524958 | frequency_hz=324.8
- [2026-07-09 19:39:05] operator / voice_transcript_partial / voice: a lot of time and smart centered not connecting with smart such a
  meta: kind=partial | timestamp=1783597145.9862313 | source=vosk | rms=829 | updated_at=1783597145.9524958 | frequency_hz=324.8
- [2026-07-09 19:39:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597146.2026503 | source=vosk | rms=654 | updated_at=1783597146.2026503 | frequency_hz=324.8
- [2026-07-09 19:39:06] operator / voice_transcript_partial / voice: a lot of time and smart centered not connecting with smart such
  meta: kind=partial | timestamp=1783597146.2558694 | source=vosk | rms=654 | updated_at=1783597146.2026503 | frequency_hz=324.8
- [2026-07-09 19:39:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597146.4526525 | source=vosk | rms=787 | updated_at=1783597146.4526525 | frequency_hz=324.8
- [2026-07-09 19:39:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597146.7031405 | source=vosk | rms=787 | updated_at=1783597146.4526525 | frequency_hz=324.8
- [2026-07-09 19:39:06] operator / voice_transcript_partial / voice: a lot of time and smart centered not connecting with smart such as much
  meta: kind=partial | timestamp=1783597146.7515678 | source=vosk | rms=787 | updated_at=1783597146.4526525 | frequency_hz=324.8
- [2026-07-09 19:39:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597146.953086 | source=vosk | rms=1207 | updated_at=1783597146.953086 | frequency_hz=324.8
- [2026-07-09 19:39:08] operator / voice_transcript_final / voice: you know a lot of time and smart centered not connecting with smart such a nice
  meta: kind=final | timestamp=1783597148.1224318 | source=final | rms=1207 | updated_at=1783597146.953086 | frequency_hz=324.8
- [2026-07-09 19:39:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597148.266081 | source=vosk | rms=1207 | updated_at=1783597146.953086 | frequency_hz=324.8
- [2026-07-09 19:39:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597148.266081 | source=vosk | rms=1207 | updated_at=1783597146.953086 | frequency_hz=324.8
- [2026-07-09 19:39:08] operator / voice_transcript_partial / voice: it's
  meta: kind=partial | timestamp=1783597148.3161223 | source=vosk | rms=511 | updated_at=1783597148.2946777 | frequency_hz=324.8
- [2026-07-09 19:39:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597148.4528828 | source=vosk | rms=473 | updated_at=1783597148.4528828 | frequency_hz=324.8
- [2026-07-09 19:39:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597148.7049038 | source=vosk | rms=473 | updated_at=1783597148.4528828 | frequency_hz=324.8
- [2026-07-09 19:39:08] operator / voice_transcript_partial / voice: it's a
  meta: kind=partial | timestamp=1783597148.7396386 | source=vosk | rms=473 | updated_at=1783597148.4528828 | frequency_hz=324.8
- [2026-07-09 19:39:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597149.2404928 | source=vosk | rms=473 | updated_at=1783597148.4528828 | frequency_hz=324.8
- [2026-07-09 19:39:10] operator / voice_transcript_final / voice: it s a
  meta: kind=final | timestamp=1783597150.3920093 | source=final | rms=473 | updated_at=1783597148.4528828 | frequency_hz=324.8
- [2026-07-09 19:39:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597150.9543097 | source=vosk | rms=556 | updated_at=1783597150.9538007 | frequency_hz=324.8
- [2026-07-09 19:39:11] operator / voice_transcript_final / voice: it s
  meta: kind=final | timestamp=1783597151.2475562 | source=final | rms=556 | updated_at=1783597150.9538007 | frequency_hz=324.8
- [2026-07-09 19:39:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597151.2931995 | source=vosk | rms=758 | updated_at=1783597151.2931995 | frequency_hz=324.8
- [2026-07-09 19:39:11] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1783597151.7107286 | source=vosk | rms=360 | updated_at=1783597151.4530008 | frequency_hz=324.8
- [2026-07-09 19:39:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597151.9534266 | source=vosk | rms=337 | updated_at=1783597151.9534266 | frequency_hz=324.8
- [2026-07-09 19:39:11] operator / voice_transcript_partial / voice: smart century
  meta: kind=partial | timestamp=1783597151.9640713 | source=vosk | rms=337 | updated_at=1783597151.9534266 | frequency_hz=324.8
- [2026-07-09 19:39:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597152.2026718 | source=vosk | rms=337 | updated_at=1783597151.9534266 | frequency_hz=324.8
- [2026-07-09 19:39:12] operator / voice_transcript_partial / voice: smart century boards
  meta: kind=partial | timestamp=1783597152.2674916 | source=vosk | rms=337 | updated_at=1783597151.9534266 | frequency_hz=324.8
- [2026-07-09 19:39:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597152.453116 | source=vosk | rms=351 | updated_at=1783597152.453116 | frequency_hz=324.8
- [2026-07-09 19:39:12] operator / voice_transcript_partial / voice: smart century boards are
  meta: kind=partial | timestamp=1783597152.481893 | source=vosk | rms=351 | updated_at=1783597152.453116 | frequency_hz=324.8
- [2026-07-09 19:39:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597152.7025144 | source=vosk | rms=351 | updated_at=1783597152.453116 | frequency_hz=324.8
- [2026-07-09 19:39:12] operator / voice_transcript_partial / voice: smart century boards are connected
  meta: kind=partial | timestamp=1783597152.7309852 | source=vosk | rms=351 | updated_at=1783597152.453116 | frequency_hz=324.8
- [2026-07-09 19:39:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597152.953111 | source=vosk | rms=351 | updated_at=1783597152.453116 | frequency_hz=324.8
- [2026-07-09 19:39:12] operator / voice_transcript_partial / voice: smart century boards are connected on
  meta: kind=partial | timestamp=1783597152.9641519 | source=vosk | rms=351 | updated_at=1783597152.453116 | frequency_hz=324.8
- [2026-07-09 19:39:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597153.2025337 | source=vosk | rms=351 | updated_at=1783597152.453116 | frequency_hz=324.8
- [2026-07-09 19:39:13] operator / voice_transcript_partial / voice: smart century boards are connected on the
  meta: kind=partial | timestamp=1783597153.233372 | source=vosk | rms=351 | updated_at=1783597152.453116 | frequency_hz=324.8
- [2026-07-09 19:39:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597153.4527876 | source=vosk | rms=394 | updated_at=1783597153.4527876 | frequency_hz=324.8
- [2026-07-09 19:39:13] operator / voice_transcript_partial / voice: smart century boards are connected on the c o
  meta: kind=partial | timestamp=1783597153.4811916 | source=vosk | rms=394 | updated_at=1783597153.4527876 | frequency_hz=324.8
- [2026-07-09 19:39:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597153.954284 | source=vosk | rms=394 | updated_at=1783597153.4527876 | frequency_hz=324.8
- [2026-07-09 19:39:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597154.4531395 | source=vosk | rms=423 | updated_at=1783597154.4531395 | frequency_hz=324.8
- [2026-07-09 19:39:14] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m
  meta: kind=partial | timestamp=1783597154.4641256 | source=vosk | rms=423 | updated_at=1783597154.4531395 | frequency_hz=324.8
- [2026-07-09 19:39:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597154.7032175 | source=vosk | rms=610 | updated_at=1783597154.7032175 | frequency_hz=324.8
- [2026-07-09 19:39:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597154.9535134 | source=vosk | rms=610 | updated_at=1783597154.7032175 | frequency_hz=324.8
- [2026-07-09 19:39:14] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m smart
  meta: kind=partial | timestamp=1783597154.9642262 | source=vosk | rms=610 | updated_at=1783597154.7032175 | frequency_hz=324.8
- [2026-07-09 19:39:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597155.4541452 | source=vosk | rms=610 | updated_at=1783597154.7032175 | frequency_hz=324.8
- [2026-07-09 19:39:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597156.452924 | source=vosk | rms=915 | updated_at=1783597156.452924 | frequency_hz=324.8
- [2026-07-09 19:39:16] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m smart such
  meta: kind=partial | timestamp=1783597156.4629493 | source=vosk | rms=915 | updated_at=1783597156.452924 | frequency_hz=324.8
- [2026-07-09 19:39:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597156.7031028 | source=vosk | rms=455 | updated_at=1783597156.7031028 | frequency_hz=324.8
- [2026-07-09 19:39:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597156.954024 | source=vosk | rms=589 | updated_at=1783597156.954024 | frequency_hz=324.8
- [2026-07-09 19:39:16] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m smart such as
  meta: kind=partial | timestamp=1783597156.9640934 | source=vosk | rms=589 | updated_at=1783597156.954024 | frequency_hz=324.8
- [2026-07-09 19:39:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597157.20289 | source=vosk | rms=534 | updated_at=1783597157.20289 | frequency_hz=324.8
- [2026-07-09 19:39:17] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m smart such ask another
  meta: kind=partial | timestamp=1783597157.2255485 | source=vosk | rms=534 | updated_at=1783597157.20289 | frequency_hz=324.8
- [2026-07-09 19:39:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597157.4531336 | source=vosk | rms=567 | updated_at=1783597157.4531336 | frequency_hz=324.8
- [2026-07-09 19:39:17] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m smart such ask another question
  meta: kind=partial | timestamp=1783597157.479963 | source=vosk | rms=567 | updated_at=1783597157.4531336 | frequency_hz=324.8
- [2026-07-09 19:39:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597157.9584277 | source=vosk | rms=536 | updated_at=1783597157.9584277 | frequency_hz=324.8
- [2026-07-09 19:39:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597158.2030787 | source=vosk | rms=418 | updated_at=1783597158.2030787 | frequency_hz=324.8
- [2026-07-09 19:39:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597158.4542882 | source=vosk | rms=547 | updated_at=1783597158.4542882 | frequency_hz=324.8
- [2026-07-09 19:39:18] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m smart such ask another question or give
  meta: kind=partial | timestamp=1783597158.4745042 | source=vosk | rms=547 | updated_at=1783597158.4542882 | frequency_hz=324.8
- [2026-07-09 19:39:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597158.7035735 | source=vosk | rms=547 | updated_at=1783597158.4542882 | frequency_hz=324.8
- [2026-07-09 19:39:18] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m smart such ask another question or give another
  meta: kind=partial | timestamp=1783597158.7203033 | source=vosk | rms=547 | updated_at=1783597158.4542882 | frequency_hz=324.8
- [2026-07-09 19:39:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597158.9529643 | source=vosk | rms=547 | updated_at=1783597158.4542882 | frequency_hz=324.8
- [2026-07-09 19:39:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597159.203518 | source=vosk | rms=547 | updated_at=1783597158.4542882 | frequency_hz=324.8
- [2026-07-09 19:39:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597159.703049 | source=vosk | rms=547 | updated_at=1783597158.4542882 | frequency_hz=324.8
- [2026-07-09 19:39:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597162.4535146 | source=vosk | rms=1206 | updated_at=1783597162.4535146 | frequency_hz=324.8
- [2026-07-09 19:39:22] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m smart such ask another question or give another command
  meta: kind=partial | timestamp=1783597162.4731085 | source=vosk | rms=1206 | updated_at=1783597162.4535146 | frequency_hz=324.8
- [2026-07-09 19:39:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597162.7028432 | source=vosk | rms=1103 | updated_at=1783597162.7028432 | frequency_hz=324.8
- [2026-07-09 19:39:22] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m smart such ask another question or give another command when
  meta: kind=partial | timestamp=1783597162.7896464 | source=vosk | rms=1103 | updated_at=1783597162.7028432 | frequency_hz=324.8
- [2026-07-09 19:39:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597162.9543533 | source=vosk | rms=1203 | updated_at=1783597162.9543533 | frequency_hz=324.8
- [2026-07-09 19:39:23] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m smart such ask another question or give another command what do
  meta: kind=partial | timestamp=1783597163.0430522 | source=vosk | rms=1203 | updated_at=1783597162.9543533 | frequency_hz=324.8
- [2026-07-09 19:39:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597163.2035556 | source=vosk | rms=1203 | updated_at=1783597163.2035556 | frequency_hz=324.8
- [2026-07-09 19:39:23] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m smart such ask another question or give another command what do you
  meta: kind=partial | timestamp=1783597163.2262945 | source=vosk | rms=1203 | updated_at=1783597163.2035556 | frequency_hz=324.8
- [2026-07-09 19:39:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597163.4531062 | source=vosk | rms=546 | updated_at=1783597163.4531062 | frequency_hz=324.8
- [2026-07-09 19:39:23] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m smart such ask another question or give another command what do you chose to
  meta: kind=partial | timestamp=1783597163.5030837 | source=vosk | rms=546 | updated_at=1783597163.4531062 | frequency_hz=324.8
- [2026-07-09 19:39:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597163.7032723 | source=vosk | rms=680 | updated_at=1783597163.7032723 | frequency_hz=324.8
- [2026-07-09 19:39:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597163.953129 | source=vosk | rms=838 | updated_at=1783597163.953129 | frequency_hz=324.8
- [2026-07-09 19:39:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597164.20318 | source=vosk | rms=1201 | updated_at=1783597164.20318 | frequency_hz=324.8
- [2026-07-09 19:39:24] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m smart such ask another question or give another command what do you chose to prefer to
  meta: kind=partial | timestamp=1783597164.2608607 | source=vosk | rms=1201 | updated_at=1783597164.20318 | frequency_hz=324.8
- [2026-07-09 19:39:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597164.454299 | source=vosk | rms=717 | updated_at=1783597164.454299 | frequency_hz=324.8
- [2026-07-09 19:39:24] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m smart such ask another question or give another command what do you chose to prefer to spend
  meta: kind=partial | timestamp=1783597164.4855456 | source=vosk | rms=717 | updated_at=1783597164.454299 | frequency_hz=324.8
- [2026-07-09 19:39:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597164.7052178 | source=vosk | rms=1202 | updated_at=1783597164.7052178 | frequency_hz=324.8
- [2026-07-09 19:39:24] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m smart such ask another question or give another command what do you chose to prefer to
  meta: kind=partial | timestamp=1783597164.737931 | source=vosk | rms=1202 | updated_at=1783597164.7052178 | frequency_hz=324.8
- [2026-07-09 19:39:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597164.9530516 | source=vosk | rms=1147 | updated_at=1783597164.9530516 | frequency_hz=324.8
- [2026-07-09 19:39:24] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m smart such ask another question or give another command what do you chose to prefer to sports and
  meta: kind=partial | timestamp=1783597164.970898 | source=vosk | rms=1147 | updated_at=1783597164.9530516 | frequency_hz=324.8
- [2026-07-09 19:39:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597165.2032921 | source=vosk | rms=443 | updated_at=1783597165.2032921 | frequency_hz=324.8
- [2026-07-09 19:39:25] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m smart such ask another question or give another command what do you chose to prefer to sports
  meta: kind=partial | timestamp=1783597165.231938 | source=vosk | rms=443 | updated_at=1783597165.2032921 | frequency_hz=324.8
- [2026-07-09 19:39:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597165.4562435 | source=vosk | rms=443 | updated_at=1783597165.2032921 | frequency_hz=324.8
- [2026-07-09 19:39:25] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m smart such ask another question or give another command what do you chose to prefer to smart centrist
  meta: kind=partial | timestamp=1783597165.4768836 | source=vosk | rms=443 | updated_at=1783597165.2032921 | frequency_hz=324.8
- [2026-07-09 19:39:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597165.7027347 | source=vosk | rms=819 | updated_at=1783597165.7027347 | frequency_hz=324.8
- [2026-07-09 19:39:25] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m smart such ask another question or give another command what do you chose to prefer to smart centrist beat florida
  meta: kind=partial | timestamp=1783597165.7410073 | source=vosk | rms=819 | updated_at=1783597165.7027347 | frequency_hz=324.8
- [2026-07-09 19:39:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597166.2024002 | source=vosk | rms=819 | updated_at=1783597165.7027347 | frequency_hz=324.8
- [2026-07-09 19:39:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597166.953135 | source=vosk | rms=988 | updated_at=1783597166.953135 | frequency_hz=324.8
- [2026-07-09 19:39:26] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m smart such ask another question or give another command what do you chose to prefer to smart centrist beat
  meta: kind=partial | timestamp=1783597166.976256 | source=vosk | rms=988 | updated_at=1783597166.953135 | frequency_hz=324.8
- [2026-07-09 19:39:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597167.20325 | source=vosk | rms=544 | updated_at=1783597167.20325 | frequency_hz=324.8
- [2026-07-09 19:39:27] operator / voice_transcript_partial / voice: smart century boards are connected on the c o m smart such ask another question or give another command what do you chose to prefer to smart centrist beat flight
  meta: kind=partial | timestamp=1783597167.2299168 | source=vosk | rms=544 | updated_at=1783597167.20325 | frequency_hz=324.8
- [2026-07-09 19:39:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597167.4530797 | source=vosk | rms=518 | updated_at=1783597167.4530797 | frequency_hz=324.8
- [2026-07-09 19:39:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597167.9546623 | source=vosk | rms=518 | updated_at=1783597167.4530797 | frequency_hz=324.8
- [2026-07-09 19:39:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597168.7058473 | source=vosk | rms=566 | updated_at=1783597168.7058473 | frequency_hz=324.8
- [2026-07-09 19:39:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597168.9585052 | source=vosk | rms=517 | updated_at=1783597168.9585052 | frequency_hz=324.8
- [2026-07-09 19:39:28] operator / voice_transcript_final / voice: connect boards
  meta: kind=final | timestamp=1783597168.987917 | source=final | rms=517 | updated_at=1783597168.9585052 | frequency_hz=324.8
- [2026-07-09 19:39:29] system / voice_status / voice: processing
  meta: kind=status | timestamp=1783597169.0203462 | source=state | rms=517 | updated_at=1783597168.9585052 | frequency_hz=324.8
- [2026-07-09 19:39:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597169.0203462 | source=state | rms=517 | updated_at=1783597168.9585052 | frequency_hz=324.8
- [2026-07-09 19:39:29] operator / voice_command / voice: connect boards
  meta: normalized=True
- [2026-07-09 19:39:30] assistant / spoken_confirmation / voice: Smart Sentry is already connected and enabled.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-07-09 19:39:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597169.4536846 | source=vosk | rms=1198 | updated_at=1783597169.4536846 | frequency_hz=324.8
- [2026-07-09 19:39:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597169.9535618 | source=vosk | rms=1198 | updated_at=1783597169.4536846 | frequency_hz=324.8
- [2026-07-09 19:39:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597170.4605901 | source=vosk | rms=580 | updated_at=1783597170.4605901 | frequency_hz=324.8
- [2026-07-09 19:39:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597171.2029784 | source=vosk | rms=544 | updated_at=1783597170.7041106 | frequency_hz=324.8
- [2026-07-09 19:39:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597171.7036626 | source=vosk | rms=929 | updated_at=1783597171.7036626 | frequency_hz=324.8
- [2026-07-09 19:39:32] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1783597172.7127738 | source=vosk | rms=771 | updated_at=1783597172.7032151 | frequency_hz=324.8
- [2026-07-09 19:39:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597172.9544919 | source=vosk | rms=771 | updated_at=1783597172.7032151 | frequency_hz=324.8
- [2026-07-09 19:39:32] operator / voice_transcript_partial / voice: smart century is
  meta: kind=partial | timestamp=1783597172.9694111 | source=vosk | rms=771 | updated_at=1783597172.7032151 | frequency_hz=324.8
- [2026-07-09 19:39:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597173.203674 | source=vosk | rms=771 | updated_at=1783597172.7032151 | frequency_hz=324.8
- [2026-07-09 19:39:33] operator / voice_transcript_partial / voice: smart century is already
  meta: kind=partial | timestamp=1783597173.224719 | source=vosk | rms=771 | updated_at=1783597172.7032151 | frequency_hz=324.8
- [2026-07-09 19:39:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597173.703558 | source=vosk | rms=771 | updated_at=1783597172.7032151 | frequency_hz=324.8
- [2026-07-09 19:39:34] operator / voice_transcript_final / voice: smart sentry is already
  meta: kind=final | timestamp=1783597174.707207 | source=final | rms=771 | updated_at=1783597172.7032151 | frequency_hz=324.8
- [2026-07-09 19:39:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597175.703057 | source=vosk | rms=771 | updated_at=1783597172.7032151 | frequency_hz=324.8
- [2026-07-09 19:39:35] operator / voice_transcript_partial / voice: smart century is already connected
  meta: kind=partial | timestamp=1783597175.74632 | source=vosk | rms=771 | updated_at=1783597172.7032151 | frequency_hz=324.8
- [2026-07-09 19:39:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597175.9567869 | source=vosk | rms=587 | updated_at=1783597175.9567869 | frequency_hz=324.8
- [2026-07-09 19:39:35] operator / voice_transcript_partial / voice: smart century is already can i
  meta: kind=partial | timestamp=1783597175.9663541 | source=vosk | rms=587 | updated_at=1783597175.9567869 | frequency_hz=324.8
- [2026-07-09 19:39:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597176.4534733 | source=vosk | rms=587 | updated_at=1783597175.9567869 | frequency_hz=324.8
- [2026-07-09 19:39:37] operator / voice_transcript_final / voice: smart sentry is already can i
  meta: kind=final | timestamp=1783597177.4703243 | source=final | rms=587 | updated_at=1783597175.9567869 | frequency_hz=324.8
- [2026-07-09 19:39:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597177.9546323 | source=vosk | rms=705 | updated_at=1783597177.9546323 | frequency_hz=324.8
- [2026-07-09 19:39:37] operator / voice_transcript_partial / voice: smart century is already can i
  meta: kind=partial | timestamp=1783597177.966667 | source=vosk | rms=705 | updated_at=1783597177.9546323 | frequency_hz=324.8
- [2026-07-09 19:39:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597178.2040992 | source=vosk | rms=1200 | updated_at=1783597178.2040992 | frequency_hz=324.8
- [2026-07-09 19:39:38] operator / voice_transcript_partial / voice: smart century is already can i can you
  meta: kind=partial | timestamp=1783597178.2297974 | source=vosk | rms=1200 | updated_at=1783597178.2040992 | frequency_hz=324.8
- [2026-07-09 19:39:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597178.4532578 | source=vosk | rms=390 | updated_at=1783597178.4532578 | frequency_hz=324.8
- [2026-07-09 19:39:38] operator / voice_transcript_partial / voice: smart century is already can i can you change the
  meta: kind=partial | timestamp=1783597178.4690876 | source=vosk | rms=390 | updated_at=1783597178.4532578 | frequency_hz=324.8
- [2026-07-09 19:39:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597178.7034526 | source=vosk | rms=567 | updated_at=1783597178.7034526 | frequency_hz=324.8
- [2026-07-09 19:39:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597178.9535909 | source=vosk | rms=1205 | updated_at=1783597178.9535909 | frequency_hz=324.8
- [2026-07-09 19:39:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597179.4533303 | source=vosk | rms=1205 | updated_at=1783597178.9535909 | frequency_hz=324.8
- [2026-07-09 19:39:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597191.0428712 | source=vosk | rms=1205 | updated_at=1783597178.9535909 | frequency_hz=324.8
- [2026-07-09 19:39:51] operator / voice_transcript_partial / voice: smart century is already can i can you change the profile
  meta: kind=partial | timestamp=1783597191.0582232 | source=vosk | rms=1205 | updated_at=1783597178.9535909 | frequency_hz=324.8
- [2026-07-09 19:39:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597191.2934568 | source=vosk | rms=293 | updated_at=1783597191.2934568 | frequency_hz=324.8
- [2026-07-09 19:39:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597191.793469 | source=vosk | rms=293 | updated_at=1783597191.2934568 | frequency_hz=324.8
- [2026-07-09 19:39:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597196.0527878 | source=vosk | rms=549 | updated_at=1783597196.0527878 | frequency_hz=324.8
- [2026-07-09 19:39:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597196.2939706 | source=vosk | rms=549 | updated_at=1783597196.0527878 | frequency_hz=324.8
- [2026-07-09 19:39:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597196.794827 | source=vosk | rms=549 | updated_at=1783597196.0527878 | frequency_hz=324.8
- [2026-07-09 19:39:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597197.043376 | source=vosk | rms=595 | updated_at=1783597197.043376 | frequency_hz=324.8
- [2026-07-09 19:39:57] operator / voice_transcript_final / voice: smart sentry is already can i can you change the profile
  meta: kind=final | timestamp=1783597197.3505273 | source=final | rms=595 | updated_at=1783597197.043376 | frequency_hz=324.8
- [2026-07-09 19:39:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597197.7040193 | source=vosk | rms=595 | updated_at=1783597197.043376 | frequency_hz=324.8
- [2026-07-09 19:39:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597197.7040193 | source=vosk | rms=595 | updated_at=1783597197.043376 | frequency_hz=324.8
- [2026-07-09 19:39:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597198.294705 | source=vosk | rms=1029 | updated_at=1783597197.7935128 | frequency_hz=324.8
- [2026-07-09 19:39:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597199.0433395 | source=vosk | rms=1029 | updated_at=1783597197.7935128 | frequency_hz=324.8
- [2026-07-09 19:39:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597199.5435393 | source=vosk | rms=1029 | updated_at=1783597197.7935128 | frequency_hz=324.8
- [2026-07-09 19:39:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597199.7935915 | source=vosk | rms=558 | updated_at=1783597199.7935915 | frequency_hz=324.8
- [2026-07-09 19:40:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597201.0433872 | source=vosk | rms=619 | updated_at=1783597200.5439696 | frequency_hz=324.8
- [2026-07-09 19:40:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597201.7938464 | source=vosk | rms=292 | updated_at=1783597201.7938464 | frequency_hz=324.8
- [2026-07-09 19:40:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597204.0436947 | source=vosk | rms=186 | updated_at=1783597202.2946775 | frequency_hz=324.8
- [2026-07-09 19:40:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597204.2942252 | source=vosk | rms=127 | updated_at=1783597204.2942252 | frequency_hz=324.8
- [2026-07-09 19:40:07] operator / voice_transcript_partial / voice: we welcome back
  meta: kind=partial | timestamp=1783597207.3159733 | source=vosk | rms=640 | updated_at=1783597207.2935054 | frequency_hz=324.8
- [2026-07-09 19:40:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597207.5439844 | source=vosk | rms=743 | updated_at=1783597207.5439844 | frequency_hz=324.8
- [2026-07-09 19:40:07] operator / voice_transcript_partial / voice: we were comeback guard
  meta: kind=partial | timestamp=1783597207.5560157 | source=vosk | rms=743 | updated_at=1783597207.5439844 | frequency_hz=324.8
- [2026-07-09 19:40:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597207.7941244 | source=vosk | rms=395 | updated_at=1783597207.7941244 | frequency_hz=324.8
- [2026-07-09 19:40:07] operator / voice_transcript_partial / voice: we were comeback guard such as
  meta: kind=partial | timestamp=1783597207.8593938 | source=vosk | rms=395 | updated_at=1783597207.7941244 | frequency_hz=324.8
- [2026-07-09 19:40:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597208.0439305 | source=vosk | rms=383 | updated_at=1783597208.0439305 | frequency_hz=324.8
- [2026-07-09 19:40:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597208.2934623 | source=vosk | rms=530 | updated_at=1783597208.2934623 | frequency_hz=324.8
- [2026-07-09 19:40:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597208.5435832 | source=vosk | rms=289 | updated_at=1783597208.5435832 | frequency_hz=324.8
- [2026-07-09 19:40:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597208.793582 | source=vosk | rms=662 | updated_at=1783597208.793582 | frequency_hz=324.8
- [2026-07-09 19:40:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597209.0442064 | source=vosk | rms=171 | updated_at=1783597209.0442064 | frequency_hz=324.8
- [2026-07-09 19:40:09] operator / voice_transcript_partial / voice: we were comeback guard such as recognizable
  meta: kind=partial | timestamp=1783597209.0562503 | source=vosk | rms=171 | updated_at=1783597209.0442064 | frequency_hz=324.8
- [2026-07-09 19:40:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597209.2963808 | source=vosk | rms=161 | updated_at=1783597209.2963808 | frequency_hz=324.8
- [2026-07-09 19:40:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597209.5435243 | source=vosk | rms=188 | updated_at=1783597209.5435243 | frequency_hz=324.8
- [2026-07-09 19:40:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597209.7951803 | source=vosk | rms=127 | updated_at=1783597209.7951803 | frequency_hz=324.8
- [2026-07-09 19:40:09] operator / voice_transcript_partial / voice: we were comeback guard such as recognizable been under
  meta: kind=partial | timestamp=1783597209.8440158 | source=vosk | rms=127 | updated_at=1783597209.7951803 | frequency_hz=324.8
- [2026-07-09 19:40:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597210.2939765 | source=vosk | rms=127 | updated_at=1783597209.7951803 | frequency_hz=324.8
- [2026-07-09 19:40:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597210.54877 | source=vosk | rms=659 | updated_at=1783597210.54877 | frequency_hz=324.8
- [2026-07-09 19:40:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597210.7939346 | source=vosk | rms=604 | updated_at=1783597210.7939346 | frequency_hz=324.8
- [2026-07-09 19:40:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597211.2937443 | source=vosk | rms=604 | updated_at=1783597210.7939346 | frequency_hz=324.8
- [2026-07-09 19:40:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597212.5438092 | source=vosk | rms=272 | updated_at=1783597212.5438092 | frequency_hz=324.8
- [2026-07-09 19:40:12] operator / voice_transcript_partial / voice: we were comeback guard such as recognizable
  meta: kind=partial | timestamp=1783597212.5633712 | source=vosk | rms=272 | updated_at=1783597212.5438092 | frequency_hz=324.8
- [2026-07-09 19:40:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597212.7941234 | source=vosk | rms=193 | updated_at=1783597212.7941234 | frequency_hz=324.8
- [2026-07-09 19:40:12] operator / voice_transcript_partial / voice: we were comeback guard such as recognizable are you
  meta: kind=partial | timestamp=1783597212.8545842 | source=vosk | rms=193 | updated_at=1783597212.7941234 | frequency_hz=324.8
- [2026-07-09 19:40:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597213.0438051 | source=vosk | rms=298 | updated_at=1783597213.0438051 | frequency_hz=324.8
- [2026-07-09 19:40:13] operator / voice_transcript_partial / voice: we were comeback guard such as recognizable are you know but
  meta: kind=partial | timestamp=1783597213.1241329 | source=vosk | rms=298 | updated_at=1783597213.0438051 | frequency_hz=324.8
- [2026-07-09 19:40:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597213.2935865 | source=vosk | rms=294 | updated_at=1783597213.2935865 | frequency_hz=324.8
- [2026-07-09 19:40:13] operator / voice_transcript_partial / voice: we were comeback guard such as recognizable are you know about
  meta: kind=partial | timestamp=1783597213.3449357 | source=vosk | rms=294 | updated_at=1783597213.2935865 | frequency_hz=324.8
- [2026-07-09 19:40:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597213.544311 | source=vosk | rms=194 | updated_at=1783597213.544311 | frequency_hz=324.8
- [2026-07-09 19:40:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597214.0442688 | source=vosk | rms=194 | updated_at=1783597213.544311 | frequency_hz=324.8
- [2026-07-09 19:40:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597214.5448637 | source=vosk | rms=136 | updated_at=1783597214.5448637 | frequency_hz=324.8
- [2026-07-09 19:40:14] operator / voice_transcript_partial / voice: we were comeback guard such as recognizable are you know about more
  meta: kind=partial | timestamp=1783597214.5634136 | source=vosk | rms=136 | updated_at=1783597214.5448637 | frequency_hz=324.8
- [2026-07-09 19:40:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597215.0464466 | source=vosk | rms=136 | updated_at=1783597214.5448637 | frequency_hz=324.8
- [2026-07-09 19:40:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597219.5439882 | source=vosk | rms=136 | updated_at=1783597214.5448637 | frequency_hz=324.8
- [2026-07-09 19:40:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597219.7946625 | source=vosk | rms=217 | updated_at=1783597219.7946625 | frequency_hz=324.8
- [2026-07-09 19:40:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597220.043808 | source=vosk | rms=542 | updated_at=1783597220.043808 | frequency_hz=324.8
- [2026-07-09 19:40:20] operator / voice_transcript_final / voice: kentucky were comeback guard such as recognizable been under are you know about more
  meta: kind=final | timestamp=1783597220.337185 | source=final | rms=542 | updated_at=1783597220.043808 | frequency_hz=324.8
- [2026-07-09 19:40:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597220.4538102 | source=vosk | rms=542 | updated_at=1783597220.043808 | frequency_hz=324.8
- [2026-07-09 19:40:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597221.0468485 | source=vosk | rms=542 | updated_at=1783597220.043808 | frequency_hz=324.8
- [2026-07-09 19:40:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597223.5442095 | source=vosk | rms=619 | updated_at=1783597223.5442095 | frequency_hz=324.8
- [2026-07-09 19:40:23] operator / voice_transcript_partial / voice: was
  meta: kind=partial | timestamp=1783597223.5637374 | source=vosk | rms=619 | updated_at=1783597223.5442095 | frequency_hz=324.8
- [2026-07-09 19:40:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597223.7944655 | source=vosk | rms=589 | updated_at=1783597223.7944655 | frequency_hz=324.8
- [2026-07-09 19:40:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597224.0442286 | source=vosk | rms=589 | updated_at=1783597223.7944655 | frequency_hz=324.8
- [2026-07-09 19:40:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597224.2950113 | source=vosk | rms=445 | updated_at=1783597224.2950113 | frequency_hz=324.8
- [2026-07-09 19:40:24] operator / voice_transcript_final / voice: this
  meta: kind=final | timestamp=1783597224.4912674 | source=final | rms=445 | updated_at=1783597224.2950113 | frequency_hz=324.8
- [2026-07-09 19:40:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597224.5441685 | source=vosk | rms=348 | updated_at=1783597224.5441685 | frequency_hz=324.8
- [2026-07-09 19:40:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597225.0447795 | source=vosk | rms=348 | updated_at=1783597224.5441685 | frequency_hz=324.8
- [2026-07-09 19:40:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597226.7952008 | source=vosk | rms=348 | updated_at=1783597224.5441685 | frequency_hz=324.8
- [2026-07-09 19:40:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597227.2939599 | source=vosk | rms=348 | updated_at=1783597224.5441685 | frequency_hz=324.8
- [2026-07-09 19:40:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597229.2937775 | source=vosk | rms=555 | updated_at=1783597229.2937775 | frequency_hz=324.8
- [2026-07-09 19:40:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597233.2953093 | source=vosk | rms=337 | updated_at=1783597232.2942975 | frequency_hz=324.8
- [2026-07-09 19:40:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597234.565048 | source=vosk | rms=337 | updated_at=1783597232.2942975 | frequency_hz=324.8
- [2026-07-09 19:40:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597235.814584 | source=vosk | rms=337 | updated_at=1783597232.2942975 | frequency_hz=324.8
- [2026-07-09 19:40:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597236.314991 | source=vosk | rms=337 | updated_at=1783597232.2942975 | frequency_hz=324.8
- [2026-07-09 19:40:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597236.8152525 | source=vosk | rms=337 | updated_at=1783597232.2942975 | frequency_hz=324.8
- [2026-07-09 19:40:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597238.0642433 | source=vosk | rms=337 | updated_at=1783597232.2942975 | frequency_hz=324.8
- [2026-07-09 19:40:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597238.5641272 | source=vosk | rms=337 | updated_at=1783597232.2942975 | frequency_hz=324.8
- [2026-07-09 19:40:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597238.814614 | source=vosk | rms=337 | updated_at=1783597232.2942975 | frequency_hz=324.8
- [2026-07-09 19:40:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597239.3142176 | source=vosk | rms=337 | updated_at=1783597232.2942975 | frequency_hz=324.8
- [2026-07-09 19:40:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597240.8137963 | source=vosk | rms=337 | updated_at=1783597232.2942975 | frequency_hz=324.8
- [2026-07-09 19:40:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597241.3155165 | source=vosk | rms=337 | updated_at=1783597232.2942975 | frequency_hz=324.8
- [2026-07-09 19:40:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597241.8139753 | source=vosk | rms=337 | updated_at=1783597232.2942975 | frequency_hz=324.8
- [2026-07-09 19:40:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597243.8144221 | source=vosk | rms=355 | updated_at=1783597243.3141632 | frequency_hz=324.8
- [2026-07-09 19:40:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597244.064752 | source=vosk | rms=361 | updated_at=1783597244.064752 | frequency_hz=324.8
- [2026-07-09 19:40:45] operator / voice_transcript_partial / voice: i
  meta: kind=partial | timestamp=1783597245.5795164 | source=vosk | rms=130 | updated_at=1783597245.563979 | frequency_hz=324.8
- [2026-07-09 19:40:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597246.0642974 | source=vosk | rms=130 | updated_at=1783597245.563979 | frequency_hz=324.8
- [2026-07-09 19:40:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597247.063894 | source=vosk | rms=222 | updated_at=1783597247.063894 | frequency_hz=324.8
- [2026-07-09 19:40:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597247.3156278 | source=vosk | rms=222 | updated_at=1783597247.063894 | frequency_hz=324.8
- [2026-07-09 19:40:47] operator / voice_transcript_partial / voice: i just
  meta: kind=partial | timestamp=1783597247.3276484 | source=vosk | rms=222 | updated_at=1783597247.063894 | frequency_hz=324.8
- [2026-07-09 19:40:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597247.5691721 | source=vosk | rms=222 | updated_at=1783597247.063894 | frequency_hz=324.8
- [2026-07-09 19:40:47] operator / voice_transcript_partial / voice: a junior
  meta: kind=partial | timestamp=1783597247.585815 | source=vosk | rms=222 | updated_at=1783597247.063894 | frequency_hz=324.8
- [2026-07-09 19:40:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597248.0664258 | source=vosk | rms=222 | updated_at=1783597247.063894 | frequency_hz=324.8
- [2026-07-09 19:40:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597248.3149395 | source=vosk | rms=768 | updated_at=1783597248.3149395 | frequency_hz=324.8
- [2026-07-09 19:40:48] operator / voice_transcript_final / voice: a junior
  meta: kind=final | timestamp=1783597248.787314 | source=final | rms=768 | updated_at=1783597248.3149395 | frequency_hz=324.8
- [2026-07-09 19:40:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597248.8200233 | source=vosk | rms=768 | updated_at=1783597248.3149395 | frequency_hz=324.8
- [2026-07-09 19:40:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597248.8200233 | source=vosk | rms=601 | updated_at=1783597248.8200233 | frequency_hz=324.8
- [2026-07-09 19:40:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597249.3146741 | source=vosk | rms=556 | updated_at=1783597248.837634 | frequency_hz=324.8
- [2026-07-09 19:40:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597249.5678163 | source=vosk | rms=249 | updated_at=1783597249.5678163 | frequency_hz=324.8
- [2026-07-09 19:40:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597250.5648222 | source=vosk | rms=184 | updated_at=1783597249.8140707 | frequency_hz=324.8
- [2026-07-09 19:40:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597251.0648425 | source=vosk | rms=215 | updated_at=1783597251.0648425 | frequency_hz=324.8
- [2026-07-09 19:40:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597255.0648842 | source=vosk | rms=189 | updated_at=1783597254.564336 | frequency_hz=324.8
- [2026-07-09 19:40:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597255.3156521 | source=vosk | rms=546 | updated_at=1783597255.3156521 | frequency_hz=324.8
- [2026-07-09 19:40:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597256.5844464 | source=vosk | rms=528 | updated_at=1783597256.0855525 | frequency_hz=324.8
- [2026-07-09 19:40:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597256.834489 | source=vosk | rms=526 | updated_at=1783597256.834489 | frequency_hz=324.8
- [2026-07-09 19:40:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597257.5846481 | source=vosk | rms=505 | updated_at=1783597257.0842807 | frequency_hz=324.8
- [2026-07-09 19:40:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597258.0849166 | source=vosk | rms=1151 | updated_at=1783597258.0849166 | frequency_hz=324.8
- [2026-07-09 19:40:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597258.8358772 | source=vosk | rms=1151 | updated_at=1783597258.0849166 | frequency_hz=324.8
- [2026-07-09 19:40:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597259.0846808 | source=vosk | rms=377 | updated_at=1783597259.0846808 | frequency_hz=324.8
- [2026-07-09 19:41:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597262.8343883 | source=vosk | rms=173 | updated_at=1783597261.592281 | frequency_hz=324.8
- [2026-07-09 19:41:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597263.0836625 | source=vosk | rms=173 | updated_at=1783597261.592281 | frequency_hz=324.8
- [2026-07-09 19:41:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597263.5849974 | source=vosk | rms=173 | updated_at=1783597261.592281 | frequency_hz=324.8
- [2026-07-09 19:41:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597265.0848093 | source=vosk | rms=173 | updated_at=1783597261.592281 | frequency_hz=324.8
- [2026-07-09 19:41:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597267.334342 | source=vosk | rms=291 | updated_at=1783597266.8345513 | frequency_hz=324.8
- [2026-07-09 19:41:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597268.6656592 | source=vosk | rms=291 | updated_at=1783597266.8345513 | frequency_hz=324.8
- [2026-07-09 19:41:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597270.7655878 | source=vosk | rms=328 | updated_at=1783597269.4140444 | frequency_hz=324.8
- [2026-07-09 19:41:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597270.7655878 | source=vosk | rms=540 | updated_at=1783597270.7655878 | frequency_hz=324.8
- [2026-07-09 19:41:12] operator / voice_transcript_partial / voice: it's
  meta: kind=partial | timestamp=1783597272.6747277 | source=vosk | rms=388 | updated_at=1783597272.6649666 | frequency_hz=324.8
- [2026-07-09 19:41:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597272.9144466 | source=vosk | rms=232 | updated_at=1783597272.9144466 | frequency_hz=324.8
- [2026-07-09 19:41:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597273.1647875 | source=vosk | rms=299 | updated_at=1783597273.1647875 | frequency_hz=324.8
- [2026-07-09 19:41:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597273.6646814 | source=vosk | rms=299 | updated_at=1783597273.1647875 | frequency_hz=324.8
- [2026-07-09 19:41:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597274.6650746 | source=vosk | rms=470 | updated_at=1783597274.6650746 | frequency_hz=324.8
- [2026-07-09 19:41:14] operator / voice_transcript_final / voice: it s work
  meta: kind=final | timestamp=1783597274.9807396 | source=final | rms=470 | updated_at=1783597274.6650746 | frequency_hz=324.8
- [2026-07-09 19:41:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597275.0941875 | source=vosk | rms=470 | updated_at=1783597274.6650746 | frequency_hz=324.8
- [2026-07-09 19:41:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597275.0941875 | source=vosk | rms=578 | updated_at=1783597275.0941875 | frequency_hz=324.8
- [2026-07-09 19:41:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597275.6646433 | source=vosk | rms=578 | updated_at=1783597275.0941875 | frequency_hz=324.8
- [2026-07-09 19:41:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597275.915044 | source=vosk | rms=578 | updated_at=1783597275.0941875 | frequency_hz=324.8
- [2026-07-09 19:41:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597276.9152758 | source=vosk | rms=424 | updated_at=1783597276.414894 | frequency_hz=324.8
- [2026-07-09 19:41:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597282.9151516 | source=vosk | rms=424 | updated_at=1783597276.414894 | frequency_hz=324.8
- [2026-07-09 19:41:23] operator / voice_transcript_partial / voice: come
  meta: kind=partial | timestamp=1783597283.4402912 | source=vosk | rms=238 | updated_at=1783597283.4219854 | frequency_hz=324.8
- [2026-07-09 19:41:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597283.9152033 | source=vosk | rms=238 | updated_at=1783597283.4219854 | frequency_hz=324.8
- [2026-07-09 19:41:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597284.4151344 | source=vosk | rms=764 | updated_at=1783597284.4151344 | frequency_hz=324.8
- [2026-07-09 19:41:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597284.6652997 | source=vosk | rms=764 | updated_at=1783597284.4151344 | frequency_hz=324.8
- [2026-07-09 19:41:24] operator / voice_transcript_final / voice: come
  meta: kind=final | timestamp=1783597284.8436534 | source=final | rms=764 | updated_at=1783597284.4151344 | frequency_hz=324.8
- [2026-07-09 19:41:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597284.9149456 | source=vosk | rms=764 | updated_at=1783597284.4151344 | frequency_hz=324.8
- [2026-07-09 19:41:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597285.4148433 | source=vosk | rms=764 | updated_at=1783597284.4151344 | frequency_hz=324.8
- [2026-07-09 19:41:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597285.6651018 | source=vosk | rms=957 | updated_at=1783597285.6651018 | frequency_hz=324.8
- [2026-07-09 19:41:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597286.4161787 | source=vosk | rms=319 | updated_at=1783597285.916113 | frequency_hz=324.8
- [2026-07-09 19:41:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597286.666233 | source=vosk | rms=319 | updated_at=1783597285.916113 | frequency_hz=324.8
- [2026-07-09 19:41:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597287.665642 | source=vosk | rms=1178 | updated_at=1783597287.169787 | frequency_hz=324.8
- [2026-07-09 19:41:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597288.164879 | source=vosk | rms=561 | updated_at=1783597288.164879 | frequency_hz=324.8
- [2026-07-09 19:41:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597288.9150646 | source=vosk | rms=508 | updated_at=1783597288.4150953 | frequency_hz=324.8
- [2026-07-09 19:41:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597289.9151342 | source=vosk | rms=498 | updated_at=1783597289.9151342 | frequency_hz=324.8
- [2026-07-09 19:41:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597290.6651368 | source=vosk | rms=498 | updated_at=1783597289.9151342 | frequency_hz=324.8
- [2026-07-09 19:41:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597290.9150004 | source=vosk | rms=498 | updated_at=1783597289.9151342 | frequency_hz=324.8
- [2026-07-09 19:41:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597291.424743 | source=vosk | rms=498 | updated_at=1783597289.9151342 | frequency_hz=324.8
- [2026-07-09 19:41:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597292.9148126 | source=vosk | rms=498 | updated_at=1783597289.9151342 | frequency_hz=324.8
- [2026-07-09 19:41:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597294.4146762 | source=vosk | rms=250 | updated_at=1783597293.9149144 | frequency_hz=324.8
- [2026-07-09 19:41:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597294.9152215 | source=vosk | rms=220 | updated_at=1783597294.9152215 | frequency_hz=324.8
- [2026-07-09 19:41:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597297.1653972 | source=vosk | rms=526 | updated_at=1783597296.6650164 | frequency_hz=324.8
- [2026-07-09 19:41:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597297.9158645 | source=vosk | rms=346 | updated_at=1783597297.9158645 | frequency_hz=311.2
- [2026-07-09 19:41:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597298.9169352 | source=vosk | rms=341 | updated_at=1783597298.417383 | frequency_hz=311.2
- [2026-07-09 19:41:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597302.166313 | source=vosk | rms=341 | updated_at=1783597298.417383 | frequency_hz=311.2
- [2026-07-09 19:41:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597303.9158337 | source=vosk | rms=183 | updated_at=1783597303.4155788 | frequency_hz=311.2
- [2026-07-09 19:41:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597304.1653109 | source=vosk | rms=550 | updated_at=1783597304.1653109 | frequency_hz=311.2
- [2026-07-09 19:41:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597305.915376 | source=vosk | rms=490 | updated_at=1783597305.1656284 | frequency_hz=311.2
- [2026-07-09 19:41:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597307.165307 | source=vosk | rms=490 | updated_at=1783597305.1656284 | frequency_hz=311.2
- [2026-07-09 19:41:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597307.6649384 | source=vosk | rms=490 | updated_at=1783597305.1656284 | frequency_hz=311.2
- [2026-07-09 19:41:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597308.549927 | source=vosk | rms=490 | updated_at=1783597305.1656284 | frequency_hz=311.2
- [2026-07-09 19:41:48] operator / voice_transcript_final / voice: good person
  meta: kind=final | timestamp=1783597308.8737814 | source=final | rms=490 | updated_at=1783597305.1656284 | frequency_hz=311.2
- [2026-07-09 19:41:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597309.169825 | source=vosk | rms=490 | updated_at=1783597305.1656284 | frequency_hz=311.2
- [2026-07-09 19:41:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597310.9165099 | source=vosk | rms=513 | updated_at=1783597310.9165099 | frequency_hz=311.2
- [2026-07-09 19:41:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597311.665116 | source=vosk | rms=534 | updated_at=1783597311.165692 | frequency_hz=311.2
- [2026-07-09 19:41:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597313.4180787 | source=vosk | rms=534 | updated_at=1783597311.165692 | frequency_hz=311.2
- [2026-07-09 19:41:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597314.1650803 | source=vosk | rms=534 | updated_at=1783597311.165692 | frequency_hz=311.2
- [2026-07-09 19:41:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597314.9149694 | source=vosk | rms=517 | updated_at=1783597314.9149694 | frequency_hz=311.2
- [2026-07-09 19:41:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597317.054038 | source=vosk | rms=564 | updated_at=1783597315.1652226 | frequency_hz=311.2
- [2026-07-09 19:41:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597317.554553 | source=vosk | rms=564 | updated_at=1783597315.1652226 | frequency_hz=311.2
- [2026-07-09 19:41:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597318.0550306 | source=vosk | rms=564 | updated_at=1783597315.1652226 | frequency_hz=311.2
- [2026-07-09 19:41:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597319.804206 | source=vosk | rms=564 | updated_at=1783597315.1652226 | frequency_hz=311.2
- [2026-07-09 19:42:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597320.5540607 | source=vosk | rms=406 | updated_at=1783597320.0544398 | frequency_hz=311.2
- [2026-07-09 19:42:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597324.5758777 | source=vosk | rms=315 | updated_at=1783597324.5743747 | frequency_hz=311.2
- [2026-07-09 19:42:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597325.3249557 | source=vosk | rms=315 | updated_at=1783597324.5743747 | frequency_hz=311.2
- [2026-07-09 19:42:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597325.574873 | source=vosk | rms=222 | updated_at=1783597325.574873 | frequency_hz=311.2
- [2026-07-09 19:42:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597326.825024 | source=vosk | rms=222 | updated_at=1783597325.574873 | frequency_hz=311.2
- [2026-07-09 19:42:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597327.075624 | source=vosk | rms=222 | updated_at=1783597325.574873 | frequency_hz=311.2
- [2026-07-09 19:42:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597328.5777218 | source=vosk | rms=180 | updated_at=1783597327.8242571 | frequency_hz=311.2
- [2026-07-09 19:42:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597332.0744855 | source=vosk | rms=131 | updated_at=1783597332.0744855 | frequency_hz=311.2
- [2026-07-09 19:42:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597335.0748317 | source=vosk | rms=199 | updated_at=1783597333.0758772 | frequency_hz=311.2
- [2026-07-09 19:42:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597335.3242283 | source=vosk | rms=199 | updated_at=1783597333.0758772 | frequency_hz=311.2
- [2026-07-09 19:42:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597335.8245218 | source=vosk | rms=199 | updated_at=1783597333.0758772 | frequency_hz=311.2
- [2026-07-09 19:42:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597338.0747428 | source=vosk | rms=199 | updated_at=1783597333.0758772 | frequency_hz=311.2
- [2026-07-09 19:42:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597339.5750756 | source=vosk | rms=157 | updated_at=1783597339.0804794 | frequency_hz=311.2
- [2026-07-09 19:42:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597343.5746279 | source=vosk | rms=157 | updated_at=1783597339.0804794 | frequency_hz=311.2
- [2026-07-09 19:42:24] operator / voice_transcript_partial / voice: you
  meta: kind=partial | timestamp=1783597344.3431559 | source=vosk | rms=319 | updated_at=1783597344.3255537 | frequency_hz=311.2
- [2026-07-09 19:42:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597344.5749521 | source=vosk | rms=173 | updated_at=1783597344.5749521 | frequency_hz=311.2
- [2026-07-09 19:42:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597344.8247573 | source=vosk | rms=173 | updated_at=1783597344.5749521 | frequency_hz=311.2
- [2026-07-09 19:42:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597345.4016497 | source=vosk | rms=173 | updated_at=1783597344.5749521 | frequency_hz=311.2
- [2026-07-09 19:42:25] operator / voice_transcript_final / voice: you
  meta: kind=final | timestamp=1783597345.60042 | source=final | rms=173 | updated_at=1783597344.5749521 | frequency_hz=311.2
- [2026-07-09 19:42:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597345.8245559 | source=vosk | rms=173 | updated_at=1783597344.5749521 | frequency_hz=311.2
- [2026-07-09 19:42:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597346.0751324 | source=vosk | rms=173 | updated_at=1783597344.5749521 | frequency_hz=311.2
- [2026-07-09 19:42:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597361.6246145 | source=vosk | rms=217 | updated_at=1783597360.3749468 | frequency_hz=311.2
- [2026-07-09 19:42:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597364.127597 | source=vosk | rms=217 | updated_at=1783597360.3749468 | frequency_hz=311.2
- [2026-07-09 19:42:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597367.6251457 | source=vosk | rms=233 | updated_at=1783597366.8745084 | frequency_hz=311.2
- [2026-07-09 19:42:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597370.6257482 | source=vosk | rms=233 | updated_at=1783597366.8745084 | frequency_hz=311.2
- [2026-07-09 19:42:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597371.3764818 | source=vosk | rms=233 | updated_at=1783597366.8745084 | frequency_hz=311.2
- [2026-07-09 19:43:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597380.1296375 | source=vosk | rms=233 | updated_at=1783597366.8745084 | frequency_hz=311.2
- [2026-07-09 19:43:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597380.8754911 | source=vosk | rms=233 | updated_at=1783597366.8745084 | frequency_hz=311.2
- [2026-07-09 19:43:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597382.125514 | source=vosk | rms=170 | updated_at=1783597382.125514 | frequency_hz=311.2
- [2026-07-09 19:43:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597382.8765285 | source=vosk | rms=149 | updated_at=1783597382.375443 | frequency_hz=311.2
- [2026-07-09 19:43:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597383.1255348 | source=vosk | rms=505 | updated_at=1783597383.1255348 | frequency_hz=311.2
- [2026-07-09 19:43:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597384.3764167 | source=vosk | rms=164 | updated_at=1783597383.8767617 | frequency_hz=311.2
- [2026-07-09 19:43:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597386.3753374 | source=vosk | rms=164 | updated_at=1783597383.8767617 | frequency_hz=311.2
- [2026-07-09 19:43:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597386.8751338 | source=vosk | rms=164 | updated_at=1783597383.8767617 | frequency_hz=311.2
- [2026-07-09 19:43:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597387.6254823 | source=vosk | rms=164 | updated_at=1783597383.8767617 | frequency_hz=311.2
- [2026-07-09 19:43:08] operator / voice_transcript_final / voice: yeah
  meta: kind=final | timestamp=1783597388.2976904 | source=final | rms=164 | updated_at=1783597383.8767617 | frequency_hz=311.2
- [2026-07-09 19:43:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597388.332101 | source=vosk | rms=164 | updated_at=1783597383.8767617 | frequency_hz=311.2
- [2026-07-09 19:43:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597388.332101 | source=vosk | rms=164 | updated_at=1783597383.8767617 | frequency_hz=311.2
- [2026-07-09 19:43:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597388.8764253 | source=vosk | rms=164 | updated_at=1783597383.8767617 | frequency_hz=311.2
- [2026-07-09 19:43:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597393.1252398 | source=vosk | rms=164 | updated_at=1783597383.8767617 | frequency_hz=311.2
- [2026-07-09 19:43:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597393.6253228 | source=vosk | rms=164 | updated_at=1783597383.8767617 | frequency_hz=311.2
- [2026-07-09 19:43:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597394.3756964 | source=vosk | rms=318 | updated_at=1783597394.3756964 | frequency_hz=311.2
- [2026-07-09 19:43:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597394.8767545 | source=vosk | rms=318 | updated_at=1783597394.3756964 | frequency_hz=311.2
- [2026-07-09 19:43:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597395.125628 | source=vosk | rms=618 | updated_at=1783597395.125628 | frequency_hz=311.2
- [2026-07-09 19:43:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597397.625998 | source=vosk | rms=486 | updated_at=1783597397.1313121 | frequency_hz=311.2
- [2026-07-09 19:43:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597397.8759634 | source=vosk | rms=227 | updated_at=1783597397.8759634 | frequency_hz=311.2
- [2026-07-09 19:43:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597399.126009 | source=vosk | rms=271 | updated_at=1783597398.6253545 | frequency_hz=311.2
- [2026-07-09 19:43:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597404.1254756 | source=vosk | rms=267 | updated_at=1783597404.1254756 | frequency_hz=311.2
- [2026-07-09 19:43:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597404.8757834 | source=vosk | rms=299 | updated_at=1783597404.3758159 | frequency_hz=311.2
- [2026-07-09 19:43:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597405.8769357 | source=vosk | rms=299 | updated_at=1783597404.3758159 | frequency_hz=311.2
- [2026-07-09 19:43:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597406.8767624 | source=vosk | rms=299 | updated_at=1783597404.3758159 | frequency_hz=311.2
- [2026-07-09 19:43:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597408.3758864 | source=vosk | rms=299 | updated_at=1783597404.3758159 | frequency_hz=311.2
- [2026-07-09 19:43:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597409.1290388 | source=vosk | rms=351 | updated_at=1783597408.626143 | frequency_hz=311.2
- [2026-07-09 19:43:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597409.3814435 | source=vosk | rms=132 | updated_at=1783597409.3814435 | frequency_hz=311.2
- [2026-07-09 19:43:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597410.3754575 | source=vosk | rms=358 | updated_at=1783597409.8768728 | frequency_hz=311.2
- [2026-07-09 19:43:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597410.6313484 | source=vosk | rms=538 | updated_at=1783597410.6313484 | frequency_hz=311.2
- [2026-07-09 19:43:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597413.125259 | source=vosk | rms=399 | updated_at=1783597412.6266384 | frequency_hz=311.2
- [2026-07-09 19:43:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597415.7269077 | source=vosk | rms=171 | updated_at=1783597415.7269077 | frequency_hz=311.2
- [2026-07-09 19:43:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597416.385748 | source=vosk | rms=171 | updated_at=1783597415.7269077 | frequency_hz=311.2
- [2026-07-09 19:43:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597416.8756804 | source=vosk | rms=139 | updated_at=1783597416.8756804 | frequency_hz=311.2
- [2026-07-09 19:43:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597417.3763142 | source=vosk | rms=139 | updated_at=1783597416.8756804 | frequency_hz=311.2
- [2026-07-09 19:43:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597418.1256928 | source=vosk | rms=139 | updated_at=1783597416.8756804 | frequency_hz=311.2
- [2026-07-09 19:43:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597418.6257935 | source=vosk | rms=139 | updated_at=1783597416.8756804 | frequency_hz=311.2
- [2026-07-09 19:43:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597420.3758476 | source=vosk | rms=217 | updated_at=1783597420.3758476 | frequency_hz=311.2
- [2026-07-09 19:43:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597422.0799558 | source=vosk | rms=525 | updated_at=1783597420.8756678 | frequency_hz=311.2
- [2026-07-09 19:43:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597424.085834 | source=vosk | rms=525 | updated_at=1783597420.8756678 | frequency_hz=311.2
- [2026-07-09 19:43:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597424.5761218 | source=vosk | rms=525 | updated_at=1783597420.8756678 | frequency_hz=311.2
- [2026-07-09 19:43:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597426.8262575 | source=vosk | rms=525 | updated_at=1783597420.8756678 | frequency_hz=311.2
- [2026-07-09 19:43:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597428.325802 | source=vosk | rms=492 | updated_at=1783597427.5757391 | frequency_hz=311.2
- [2026-07-09 19:43:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597430.8258107 | source=vosk | rms=542 | updated_at=1783597430.8258107 | frequency_hz=311.2
- [2026-07-09 19:43:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597432.077472 | source=vosk | rms=356 | updated_at=1783597431.5759308 | frequency_hz=311.2
- [2026-07-09 19:43:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597432.5765622 | source=vosk | rms=129 | updated_at=1783597432.5765622 | frequency_hz=311.2
- [2026-07-09 19:43:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597433.8257453 | source=vosk | rms=210 | updated_at=1783597433.3305223 | frequency_hz=311.2
- [2026-07-09 19:43:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597434.5757837 | source=vosk | rms=210 | updated_at=1783597433.3305223 | frequency_hz=311.2
- [2026-07-09 19:43:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597436.326301 | source=vosk | rms=453 | updated_at=1783597435.8261504 | frequency_hz=311.2
- [2026-07-09 19:43:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597437.8266807 | source=vosk | rms=453 | updated_at=1783597435.8261504 | frequency_hz=311.2
- [2026-07-09 19:43:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597438.8265598 | source=vosk | rms=453 | updated_at=1783597435.8261504 | frequency_hz=311.2
- [2026-07-09 19:43:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597439.575848 | source=vosk | rms=453 | updated_at=1783597435.8261504 | frequency_hz=311.2
- [2026-07-09 19:44:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597440.8459034 | source=vosk | rms=453 | updated_at=1783597435.8261504 | frequency_hz=311.2
- [2026-07-09 19:44:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597442.346188 | source=vosk | rms=163 | updated_at=1783597442.346188 | frequency_hz=311.2
- [2026-07-09 19:44:02] operator / voice_transcript_final / voice: it kinda
  meta: kind=final | timestamp=1783597442.553749 | source=final | rms=163 | updated_at=1783597442.346188 | frequency_hz=311.2
- [2026-07-09 19:44:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597442.596563 | source=vosk | rms=122 | updated_at=1783597442.596563 | frequency_hz=311.2
- [2026-07-09 19:44:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597443.5964358 | source=vosk | rms=122 | updated_at=1783597442.596563 | frequency_hz=311.2
- [2026-07-09 19:44:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597444.3468 | source=vosk | rms=122 | updated_at=1783597442.596563 | frequency_hz=311.2
- [2026-07-09 19:44:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597445.595966 | source=vosk | rms=207 | updated_at=1783597444.59616 | frequency_hz=311.2
- [2026-07-09 19:44:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597446.5965543 | source=vosk | rms=207 | updated_at=1783597444.59616 | frequency_hz=311.2
- [2026-07-09 19:44:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597447.0968072 | source=vosk | rms=207 | updated_at=1783597444.59616 | frequency_hz=311.2
- [2026-07-09 19:44:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597449.0958805 | source=vosk | rms=207 | updated_at=1783597444.59616 | frequency_hz=311.2
- [2026-07-09 19:44:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597450.347552 | source=vosk | rms=177 | updated_at=1783597449.848689 | frequency_hz=311.2
- [2026-07-09 19:44:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597452.3477187 | source=vosk | rms=177 | updated_at=1783597449.848689 | frequency_hz=311.2
- [2026-07-09 19:44:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597452.8558574 | source=vosk | rms=177 | updated_at=1783597449.848689 | frequency_hz=311.2
- [2026-07-09 19:44:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597453.5965784 | source=vosk | rms=177 | updated_at=1783597449.848689 | frequency_hz=311.2
- [2026-07-09 19:44:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597454.0964522 | source=vosk | rms=177 | updated_at=1783597449.848689 | frequency_hz=311.2
- [2026-07-09 19:44:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597454.3460534 | source=vosk | rms=328 | updated_at=1783597454.3460534 | frequency_hz=311.2
- [2026-07-09 19:44:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597454.8483093 | source=vosk | rms=328 | updated_at=1783597454.3460534 | frequency_hz=311.2
- [2026-07-09 19:44:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597455.3463671 | source=vosk | rms=511 | updated_at=1783597455.3463671 | frequency_hz=311.2
- [2026-07-09 19:44:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597456.5964265 | source=vosk | rms=533 | updated_at=1783597456.096395 | frequency_hz=311.2
- [2026-07-09 19:44:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597456.8468423 | source=vosk | rms=533 | updated_at=1783597456.096395 | frequency_hz=311.2
- [2026-07-09 19:44:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597457.8466272 | source=vosk | rms=891 | updated_at=1783597457.3463058 | frequency_hz=311.2
- [2026-07-09 19:44:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597458.8463337 | source=vosk | rms=891 | updated_at=1783597457.3463058 | frequency_hz=311.2
- [2026-07-09 19:44:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597460.8457947 | source=vosk | rms=136 | updated_at=1783597460.0963092 | frequency_hz=311.2
- [2026-07-09 19:44:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597461.3461328 | source=vosk | rms=133 | updated_at=1783597461.3461328 | frequency_hz=311.2
- [2026-07-09 19:44:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597461.8463135 | source=vosk | rms=133 | updated_at=1783597461.3461328 | frequency_hz=311.2
- [2026-07-09 19:44:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597462.846648 | source=vosk | rms=1035 | updated_at=1783597462.846648 | frequency_hz=311.2
- [2026-07-09 19:44:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597463.5966861 | source=vosk | rms=527 | updated_at=1783597463.0965025 | frequency_hz=311.2
- [2026-07-09 19:44:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597467.3765829 | source=vosk | rms=279 | updated_at=1783597467.3765829 | frequency_hz=311.2
- [2026-07-09 19:44:27] operator / voice_transcript_partial / voice: killian
  meta: kind=partial | timestamp=1783597467.416736 | source=vosk | rms=279 | updated_at=1783597467.3765829 | frequency_hz=311.2
- [2026-07-09 19:44:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597467.616734 | source=vosk | rms=733 | updated_at=1783597467.616734 | frequency_hz=311.2
- [2026-07-09 19:44:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597467.869896 | source=vosk | rms=153 | updated_at=1783597467.869896 | frequency_hz=311.2
- [2026-07-09 19:44:27] operator / voice_transcript_partial / voice: julian edelman
  meta: kind=partial | timestamp=1783597467.9762094 | source=vosk | rms=153 | updated_at=1783597467.869896 | frequency_hz=311.2
- [2026-07-09 19:44:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597468.116756 | source=vosk | rms=261 | updated_at=1783597468.116756 | frequency_hz=311.2
- [2026-07-09 19:44:28] operator / voice_transcript_partial / voice: the alien alien
  meta: kind=partial | timestamp=1783597468.1453693 | source=vosk | rms=261 | updated_at=1783597468.116756 | frequency_hz=311.2
- [2026-07-09 19:44:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597468.3678646 | source=vosk | rms=373 | updated_at=1783597468.3678646 | frequency_hz=311.2
- [2026-07-09 19:44:28] operator / voice_transcript_partial / voice: the alien alien or
  meta: kind=partial | timestamp=1783597468.4141445 | source=vosk | rms=373 | updated_at=1783597468.3678646 | frequency_hz=311.2
- [2026-07-09 19:44:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597468.6161544 | source=vosk | rms=694 | updated_at=1783597468.6161544 | frequency_hz=311.2
- [2026-07-09 19:44:28] operator / voice_transcript_partial / voice: the alien alien are you
  meta: kind=partial | timestamp=1783597468.670697 | source=vosk | rms=694 | updated_at=1783597468.6161544 | frequency_hz=311.2
- [2026-07-09 19:44:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597468.8665564 | source=vosk | rms=322 | updated_at=1783597468.8665564 | frequency_hz=311.2
- [2026-07-09 19:44:28] operator / voice_transcript_partial / voice: the alien alien are you listening
  meta: kind=partial | timestamp=1783597468.8825157 | source=vosk | rms=322 | updated_at=1783597468.8665564 | frequency_hz=311.2
- [2026-07-09 19:44:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597469.11643 | source=vosk | rms=322 | updated_at=1783597468.8665564 | frequency_hz=311.2
- [2026-07-09 19:44:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597469.616779 | source=vosk | rms=322 | updated_at=1783597468.8665564 | frequency_hz=311.2
- [2026-07-09 19:44:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597470.1161792 | source=vosk | rms=339 | updated_at=1783597470.1161792 | frequency_hz=311.2
- [2026-07-09 19:44:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597470.616295 | source=vosk | rms=391 | updated_at=1783597470.616295 | frequency_hz=305.2
- [2026-07-09 19:44:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597470.8677084 | source=vosk | rms=375 | updated_at=1783597470.8677084 | frequency_hz=305.2
- [2026-07-09 19:44:31] system / voice_status / voice: listening
  meta: kind=status | timestamp=1783597471.6470518 | source=state | rms=375 | updated_at=1783597470.8677084 | frequency_hz=305.2
- [2026-07-09 19:44:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597471.780954 | source=state | rms=375 | updated_at=1783597470.8677084 | frequency_hz=305.2
- [2026-07-09 19:44:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597471.780954 | source=vosk | rms=375 | updated_at=1783597470.8677084 | frequency_hz=305.2
- [2026-07-09 19:44:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597472.3978465 | source=vosk | rms=375 | updated_at=1783597470.8677084 | frequency_hz=305.2
- [2026-07-09 19:44:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597472.896707 | source=vosk | rms=451 | updated_at=1783597472.896707 | frequency_hz=305.2
- [2026-07-09 19:44:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597473.4007003 | source=vosk | rms=451 | updated_at=1783597472.896707 | frequency_hz=305.2
- [2026-07-09 19:44:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597476.3966377 | source=vosk | rms=142 | updated_at=1783597476.3966377 | frequency_hz=305.2
- [2026-07-09 19:44:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597478.1465466 | source=vosk | rms=332 | updated_at=1783597477.6472466 | frequency_hz=305.2
- [2026-07-09 19:44:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597481.896728 | source=vosk | rms=243 | updated_at=1783597481.896728 | frequency_hz=305.2
- [2026-07-09 19:44:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597482.896423 | source=vosk | rms=203 | updated_at=1783597482.1471527 | frequency_hz=305.2
- [2026-07-09 19:44:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597483.1467392 | source=vosk | rms=163 | updated_at=1783597483.1467392 | frequency_hz=305.2
- [2026-07-09 19:44:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597485.8972392 | source=vosk | rms=323 | updated_at=1783597485.3971508 | frequency_hz=305.2
- [2026-07-09 19:44:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597486.3971672 | source=vosk | rms=199 | updated_at=1783597486.3971672 | frequency_hz=305.2
- [2026-07-09 19:44:46] operator / voice_transcript_final / voice: but
  meta: kind=final | timestamp=1783597486.6170826 | source=final | rms=199 | updated_at=1783597486.3971672 | frequency_hz=305.2
- [2026-07-09 19:44:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597486.8989956 | source=vosk | rms=199 | updated_at=1783597486.3971672 | frequency_hz=305.2
- [2026-07-09 19:44:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597488.1468806 | source=vosk | rms=464 | updated_at=1783597488.1468806 | frequency_hz=305.2
- [2026-07-09 19:44:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597489.1512346 | source=vosk | rms=457 | updated_at=1783597488.39681 | frequency_hz=305.2
- [2026-07-09 19:44:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597489.396307 | source=vosk | rms=457 | updated_at=1783597488.39681 | frequency_hz=305.2
- [2026-07-09 19:44:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597489.8971102 | source=vosk | rms=457 | updated_at=1783597488.39681 | frequency_hz=305.2
- [2026-07-09 19:44:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597490.6468751 | source=vosk | rms=140 | updated_at=1783597490.6468751 | frequency_hz=305.2
- [2026-07-09 19:44:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597491.1483257 | source=vosk | rms=140 | updated_at=1783597490.6468751 | frequency_hz=305.2
- [2026-07-09 19:44:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597499.1471877 | source=vosk | rms=443 | updated_at=1783597499.1471877 | frequency_hz=305.2
- [2026-07-09 19:44:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597499.8969734 | source=vosk | rms=375 | updated_at=1783597499.3966198 | frequency_hz=305.2
- [2026-07-09 19:45:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597504.6475005 | source=vosk | rms=323 | updated_at=1783597504.6475005 | frequency_hz=330.0
- [2026-07-09 19:45:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597505.6468084 | source=vosk | rms=240 | updated_at=1783597505.1467085 | frequency_hz=330.0
- [2026-07-09 19:45:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597516.6478457 | source=vosk | rms=198 | updated_at=1783597516.6478457 | frequency_hz=148.0
- [2026-07-09 19:45:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597517.647105 | source=vosk | rms=319 | updated_at=1783597517.147061 | frequency_hz=148.0
- [2026-07-09 19:45:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597518.1486642 | source=vosk | rms=319 | updated_at=1783597517.147061 | frequency_hz=148.0
- [2026-07-09 19:45:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597518.8732224 | source=vosk | rms=216 | updated_at=1783597518.39717 | frequency_hz=148.0
- [2026-07-09 19:45:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597523.397665 | source=vosk | rms=1189 | updated_at=1783597523.397665 | frequency_hz=148.0
- [2026-07-09 19:45:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597523.8973446 | source=vosk | rms=1189 | updated_at=1783597523.397665 | frequency_hz=148.0
- [2026-07-09 19:45:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597524.147847 | source=vosk | rms=1189 | updated_at=1783597523.397665 | frequency_hz=148.0
- [2026-07-09 19:45:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597524.6477304 | source=vosk | rms=1189 | updated_at=1783597523.397665 | frequency_hz=148.0
- [2026-07-09 19:45:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597527.6469917 | source=vosk | rms=659 | updated_at=1783597527.6469917 | frequency_hz=148.0
- [2026-07-09 19:45:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597528.3978136 | source=vosk | rms=647 | updated_at=1783597527.9022863 | frequency_hz=148.0
- [2026-07-09 19:45:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597529.1472347 | source=vosk | rms=647 | updated_at=1783597527.9022863 | frequency_hz=148.0
- [2026-07-09 19:45:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597529.647954 | source=vosk | rms=647 | updated_at=1783597527.9022863 | frequency_hz=148.0
- [2026-07-09 19:45:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597531.3973827 | source=vosk | rms=125 | updated_at=1783597531.3973827 | frequency_hz=386.0
- [2026-07-09 19:45:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597532.3977797 | source=vosk | rms=582 | updated_at=1783597531.8972688 | frequency_hz=386.0
- [2026-07-09 19:45:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597535.1473691 | source=vosk | rms=597 | updated_at=1783597535.1473691 | frequency_hz=386.0
- [2026-07-09 19:45:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597536.1489294 | source=vosk | rms=243 | updated_at=1783597535.648023 | frequency_hz=386.0
- [2026-07-09 19:45:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597538.6479158 | source=vosk | rms=395 | updated_at=1783597538.6479158 | frequency_hz=386.0
- [2026-07-09 19:45:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597540.8981414 | source=vosk | rms=437 | updated_at=1783597539.8972483 | frequency_hz=386.0
- [2026-07-09 19:45:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597541.2378697 | source=vosk | rms=218 | updated_at=1783597541.2378697 | frequency_hz=386.0
- [2026-07-09 19:45:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597542.1490366 | source=vosk | rms=248 | updated_at=1783597541.6480935 | frequency_hz=386.0
- [2026-07-09 19:45:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597542.398335 | source=vosk | rms=248 | updated_at=1783597541.6480935 | frequency_hz=386.0
- [2026-07-09 19:45:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597543.3975909 | source=vosk | rms=145 | updated_at=1783597542.9003775 | frequency_hz=386.0
- [2026-07-09 19:45:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597543.6482162 | source=vosk | rms=145 | updated_at=1783597542.9003775 | frequency_hz=386.0
- [2026-07-09 19:45:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597544.1478808 | source=vosk | rms=145 | updated_at=1783597542.9003775 | frequency_hz=386.0
- [2026-07-09 19:45:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597544.6660974 | source=vosk | rms=145 | updated_at=1783597542.9003775 | frequency_hz=386.0
- [2026-07-09 19:45:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597545.148997 | source=vosk | rms=145 | updated_at=1783597542.9003775 | frequency_hz=386.0
- [2026-07-09 19:45:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597546.6480618 | source=vosk | rms=124 | updated_at=1783597546.6480618 | frequency_hz=386.0
- [2026-07-09 19:45:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597548.3978364 | source=vosk | rms=462 | updated_at=1783597547.1472957 | frequency_hz=386.0
- [2026-07-09 19:45:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597551.3978143 | source=vosk | rms=462 | updated_at=1783597547.1472957 | frequency_hz=386.0
- [2026-07-09 19:45:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597551.8981435 | source=vosk | rms=462 | updated_at=1783597547.1472957 | frequency_hz=386.0
- [2026-07-09 19:45:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597554.8981977 | source=vosk | rms=462 | updated_at=1783597547.1472957 | frequency_hz=386.0
- [2026-07-09 19:45:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597556.1480184 | source=vosk | rms=242 | updated_at=1783597555.1478794 | frequency_hz=386.0
- [2026-07-09 19:45:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597557.1493976 | source=vosk | rms=242 | updated_at=1783597555.1478794 | frequency_hz=386.0
- [2026-07-09 19:45:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597558.65672 | source=vosk | rms=136 | updated_at=1783597557.8977664 | frequency_hz=386.0
- [2026-07-09 19:45:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597559.148266 | source=vosk | rms=136 | updated_at=1783597557.8977664 | frequency_hz=386.0
- [2026-07-09 19:45:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597559.897983 | source=vosk | rms=136 | updated_at=1783597557.8977664 | frequency_hz=386.0
- [2026-07-09 19:46:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597560.8977637 | source=vosk | rms=136 | updated_at=1783597560.8977637 | frequency_hz=386.0
- [2026-07-09 19:46:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597561.6479385 | source=vosk | rms=136 | updated_at=1783597560.8977637 | frequency_hz=386.0
- [2026-07-09 19:46:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597562.1484363 | source=vosk | rms=128 | updated_at=1783597562.1484363 | frequency_hz=386.0
- [2026-07-09 19:46:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597564.1483235 | source=vosk | rms=450 | updated_at=1783597563.6479747 | frequency_hz=386.0
- [2026-07-09 19:46:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597564.3980148 | source=vosk | rms=450 | updated_at=1783597563.6479747 | frequency_hz=386.0
- [2026-07-09 19:46:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597564.8981085 | source=vosk | rms=450 | updated_at=1783597563.6479747 | frequency_hz=386.0
- [2026-07-09 19:46:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597565.4038067 | source=vosk | rms=276 | updated_at=1783597565.4038067 | frequency_hz=386.0
- [2026-07-09 19:46:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597566.6486793 | source=vosk | rms=213 | updated_at=1783597566.1502056 | frequency_hz=386.0
- [2026-07-09 19:46:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597567.1485634 | source=vosk | rms=506 | updated_at=1783597567.1485634 | frequency_hz=386.0
- [2026-07-09 19:46:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597567.8984103 | source=vosk | rms=510 | updated_at=1783597567.3977728 | frequency_hz=386.0
- [2026-07-09 19:46:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597570.3978677 | source=vosk | rms=301 | updated_at=1783597570.3978677 | frequency_hz=386.0
- [2026-07-09 19:46:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597571.397711 | source=vosk | rms=286 | updated_at=1783597570.8985481 | frequency_hz=386.0
- [2026-07-09 19:46:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597572.9001951 | source=vosk | rms=552 | updated_at=1783597572.9001951 | frequency_hz=386.0
- [2026-07-09 19:46:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597573.898905 | source=vosk | rms=606 | updated_at=1783597573.1481626 | frequency_hz=386.0
- [2026-07-09 19:46:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597575.6481972 | source=vosk | rms=128 | updated_at=1783597575.6481972 | frequency_hz=386.0
- [2026-07-09 19:46:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597576.2491648 | source=vosk | rms=128 | updated_at=1783597575.6481972 | frequency_hz=386.0
- [2026-07-09 19:46:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597577.9982238 | source=vosk | rms=833 | updated_at=1783597577.9982238 | frequency_hz=386.0
- [2026-07-09 19:46:18] operator / voice_transcript_final / voice: such
  meta: kind=final | timestamp=1783597578.1850898 | source=final | rms=833 | updated_at=1783597577.9982238 | frequency_hz=386.0
- [2026-07-09 19:46:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597578.247998 | source=vosk | rms=564 | updated_at=1783597578.247998 | frequency_hz=386.0
- [2026-07-09 19:46:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597579.7484114 | source=vosk | rms=127 | updated_at=1783597579.2480881 | frequency_hz=386.0
- [2026-07-09 19:46:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597580.498357 | source=vosk | rms=127 | updated_at=1783597579.2480881 | frequency_hz=386.0
- [2026-07-09 19:46:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597580.998576 | source=vosk | rms=127 | updated_at=1783597579.2480881 | frequency_hz=386.0
- [2026-07-09 19:46:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597582.7481482 | source=vosk | rms=975 | updated_at=1783597582.7481482 | frequency_hz=386.0
- [2026-07-09 19:46:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597583.248151 | source=vosk | rms=975 | updated_at=1783597582.7481482 | frequency_hz=386.0
- [2026-07-09 19:46:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597583.7481542 | source=vosk | rms=558 | updated_at=1783597583.7481542 | frequency_hz=386.0
- [2026-07-09 19:46:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597584.7494693 | source=vosk | rms=222 | updated_at=1783597584.2478778 | frequency_hz=386.0
- [2026-07-09 19:46:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597595.1196246 | source=vosk | rms=401 | updated_at=1783597595.1196246 | frequency_hz=386.0
- [2026-07-09 19:46:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597596.1180863 | source=vosk | rms=392 | updated_at=1783597595.618488 | frequency_hz=386.0
- [2026-07-09 19:46:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597597.118826 | source=vosk | rms=599 | updated_at=1783597597.118826 | frequency_hz=386.0
- [2026-07-09 19:46:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597598.8687646 | source=vosk | rms=566 | updated_at=1783597598.1188521 | frequency_hz=386.0
- [2026-07-09 19:46:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597602.8690743 | source=vosk | rms=566 | updated_at=1783597598.1188521 | frequency_hz=386.0
- [2026-07-09 19:46:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597603.3689651 | source=vosk | rms=566 | updated_at=1783597598.1188521 | frequency_hz=386.0
- [2026-07-09 19:46:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597603.619058 | source=vosk | rms=566 | updated_at=1783597598.1188521 | frequency_hz=386.0
- [2026-07-09 19:46:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597604.118988 | source=vosk | rms=566 | updated_at=1783597598.1188521 | frequency_hz=386.0
- [2026-07-09 19:46:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597607.118492 | source=vosk | rms=566 | updated_at=1783597598.1188521 | frequency_hz=386.0
- [2026-07-09 19:46:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597608.8686595 | source=vosk | rms=490 | updated_at=1783597608.3688617 | frequency_hz=386.0
- [2026-07-09 19:46:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597609.6187932 | source=vosk | rms=498 | updated_at=1783597609.6187932 | frequency_hz=386.0
- [2026-07-09 19:46:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597610.3680868 | source=vosk | rms=498 | updated_at=1783597609.6187932 | frequency_hz=386.0
- [2026-07-09 19:46:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597610.6191876 | source=vosk | rms=498 | updated_at=1783597609.6187932 | frequency_hz=386.0
- [2026-07-09 19:46:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597612.11876 | source=vosk | rms=156 | updated_at=1783597611.6183658 | frequency_hz=386.0
- [2026-07-09 19:46:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597612.6184232 | source=vosk | rms=644 | updated_at=1783597612.6184232 | frequency_hz=386.0
- [2026-07-09 19:46:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597613.3692734 | source=vosk | rms=615 | updated_at=1783597612.8685555 | frequency_hz=386.0
- [2026-07-09 19:46:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597614.8690202 | source=vosk | rms=450 | updated_at=1783597614.8690202 | frequency_hz=386.0
- [2026-07-09 19:46:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597615.6186213 | source=vosk | rms=373 | updated_at=1783597615.1201234 | frequency_hz=386.0
- [2026-07-09 19:46:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597615.8689702 | source=vosk | rms=233 | updated_at=1783597615.8689702 | frequency_hz=386.0
- [2026-07-09 19:46:56] operator / voice_transcript_final / voice: it s
  meta: kind=final | timestamp=1783597616.8471267 | source=final | rms=672 | updated_at=1783597616.6184824 | frequency_hz=386.0
- [2026-07-09 19:46:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597616.8777635 | source=vosk | rms=257 | updated_at=1783597616.8777635 | frequency_hz=386.0
- [2026-07-09 19:46:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597617.3687599 | source=vosk | rms=257 | updated_at=1783597616.8777635 | frequency_hz=386.0
- [2026-07-09 19:46:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597618.368479 | source=vosk | rms=597 | updated_at=1783597618.368479 | frequency_hz=386.0
- [2026-07-09 19:46:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597619.3690495 | source=vosk | rms=148 | updated_at=1783597618.86919 | frequency_hz=386.0
- [2026-07-09 19:47:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597620.1254723 | source=vosk | rms=635 | updated_at=1783597620.1254723 | frequency_hz=386.0
- [2026-07-09 19:47:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597622.3694913 | source=vosk | rms=601 | updated_at=1783597621.8686564 | frequency_hz=386.0
- [2026-07-09 19:47:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597623.870768 | source=vosk | rms=628 | updated_at=1783597623.870768 | frequency_hz=386.0
- [2026-07-09 19:47:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597624.6191118 | source=vosk | rms=632 | updated_at=1783597624.120079 | frequency_hz=386.0
- [2026-07-09 19:47:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597624.8697546 | source=vosk | rms=188 | updated_at=1783597624.8697546 | frequency_hz=386.0
- [2026-07-09 19:47:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597627.6194165 | source=vosk | rms=407 | updated_at=1783597627.1234155 | frequency_hz=386.0
- [2026-07-09 19:47:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597627.8685725 | source=vosk | rms=407 | updated_at=1783597627.1234155 | frequency_hz=386.0
- [2026-07-09 19:47:09] operator / voice_transcript_partial / voice: come
  meta: kind=partial | timestamp=1783597629.6633513 | source=vosk | rms=690 | updated_at=1783597629.6186166 | frequency_hz=386.0
- [2026-07-09 19:47:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597629.870482 | source=vosk | rms=426 | updated_at=1783597629.870482 | frequency_hz=386.0
- [2026-07-09 19:47:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597630.8693511 | source=vosk | rms=426 | updated_at=1783597629.870482 | frequency_hz=386.0
- [2026-07-09 19:47:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597637.3695004 | source=vosk | rms=214 | updated_at=1783597637.3695004 | frequency_hz=386.0
- [2026-07-09 19:47:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597639.1202798 | source=vosk | rms=675 | updated_at=1783597638.3696203 | frequency_hz=386.0
- [2026-07-09 19:47:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597640.3686397 | source=vosk | rms=344 | updated_at=1783597640.3686397 | frequency_hz=386.0
- [2026-07-09 19:47:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597641.118795 | source=vosk | rms=287 | updated_at=1783597640.6195529 | frequency_hz=386.0
- [2026-07-09 19:47:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597642.3688972 | source=vosk | rms=287 | updated_at=1783597640.6195529 | frequency_hz=386.0
- [2026-07-09 19:47:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597643.1190362 | source=vosk | rms=287 | updated_at=1783597640.6195529 | frequency_hz=386.0
- [2026-07-09 19:47:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597656.4390779 | source=vosk | rms=512 | updated_at=1783597656.4390779 | frequency_hz=356.0
- [2026-07-09 19:47:37] operator / voice_transcript_final / voice: cowboy
  meta: kind=final | timestamp=1783597657.0051954 | source=final | rms=648 | updated_at=1783597656.6941082 | frequency_hz=356.0
- [2026-07-09 19:47:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597657.0405383 | source=vosk | rms=333 | updated_at=1783597657.0390348 | frequency_hz=356.0
- [2026-07-09 19:47:38] operator / voice_transcript_partial / voice: so
  meta: kind=partial | timestamp=1783597658.7293525 | source=vosk | rms=463 | updated_at=1783597658.6896553 | frequency_hz=356.0
- [2026-07-09 19:47:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597658.9397933 | source=vosk | rms=486 | updated_at=1783597658.9397933 | frequency_hz=356.0
- [2026-07-09 19:47:39] operator / voice_transcript_partial / voice: so the
  meta: kind=partial | timestamp=1783597659.001752 | source=vosk | rms=486 | updated_at=1783597658.9397933 | frequency_hz=356.0
- [2026-07-09 19:47:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597659.189285 | source=vosk | rms=530 | updated_at=1783597659.189285 | frequency_hz=356.0
- [2026-07-09 19:47:39] operator / voice_transcript_partial / voice: son of a
  meta: kind=partial | timestamp=1783597659.2239013 | source=vosk | rms=530 | updated_at=1783597659.189285 | frequency_hz=356.0
- [2026-07-09 19:47:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597659.444517 | source=vosk | rms=485 | updated_at=1783597659.444517 | frequency_hz=356.0
- [2026-07-09 19:47:39] operator / voice_transcript_partial / voice: son of a global
  meta: kind=partial | timestamp=1783597659.5078473 | source=vosk | rms=485 | updated_at=1783597659.444517 | frequency_hz=356.0
- [2026-07-09 19:47:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597659.6893854 | source=vosk | rms=663 | updated_at=1783597659.6893854 | frequency_hz=356.0
- [2026-07-09 19:47:39] operator / voice_transcript_partial / voice: so the local militia
  meta: kind=partial | timestamp=1783597659.7383614 | source=vosk | rms=663 | updated_at=1783597659.6893854 | frequency_hz=356.0
- [2026-07-09 19:47:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597659.9396453 | source=vosk | rms=272 | updated_at=1783597659.9396453 | frequency_hz=356.0
- [2026-07-09 19:47:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597660.1942601 | source=vosk | rms=219 | updated_at=1783597660.1942601 | frequency_hz=356.0
- [2026-07-09 19:47:40] operator / voice_transcript_partial / voice: so the local militia to
  meta: kind=partial | timestamp=1783597660.2277408 | source=vosk | rms=219 | updated_at=1783597660.1942601 | frequency_hz=356.0
- [2026-07-09 19:47:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597660.6973357 | source=vosk | rms=219 | updated_at=1783597660.1942601 | frequency_hz=356.0
- [2026-07-09 19:47:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597662.0600202 | source=vosk | rms=740 | updated_at=1783597662.0600202 | frequency_hz=356.0
- [2026-07-09 19:47:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597662.309941 | source=vosk | rms=733 | updated_at=1783597662.309941 | frequency_hz=356.0
- [2026-07-09 19:47:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597662.5590534 | source=vosk | rms=417 | updated_at=1783597662.5590534 | frequency_hz=356.0
- [2026-07-09 19:47:42] operator / voice_transcript_final / voice: of rumors are true
  meta: kind=final | timestamp=1783597662.84277 | source=final | rms=417 | updated_at=1783597662.5590534 | frequency_hz=356.0
- [2026-07-09 19:47:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597662.9608393 | source=vosk | rms=245 | updated_at=1783597662.9608393 | frequency_hz=356.0
- [2026-07-09 19:47:43] operator / voice_transcript_partial / voice: but
  meta: kind=partial | timestamp=1783597663.34965 | source=vosk | rms=525 | updated_at=1783597663.3097222 | frequency_hz=356.0
- [2026-07-09 19:47:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597663.5604205 | source=vosk | rms=1202 | updated_at=1783597663.5589032 | frequency_hz=356.0
- [2026-07-09 19:47:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597663.80971 | source=vosk | rms=633 | updated_at=1783597663.80971 | frequency_hz=356.0
- [2026-07-09 19:47:43] operator / voice_transcript_partial / voice: cooper how
  meta: kind=partial | timestamp=1783597663.854131 | source=vosk | rms=633 | updated_at=1783597663.80971 | frequency_hz=356.0
- [2026-07-09 19:47:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597664.0595243 | source=vosk | rms=745 | updated_at=1783597664.0595243 | frequency_hz=356.0
- [2026-07-09 19:47:44] operator / voice_transcript_partial / voice: october
  meta: kind=partial | timestamp=1783597664.1092052 | source=vosk | rms=745 | updated_at=1783597664.0595243 | frequency_hz=356.0
- [2026-07-09 19:47:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597664.3154929 | source=vosk | rms=443 | updated_at=1783597664.3154929 | frequency_hz=356.0
- [2026-07-09 19:47:44] operator / voice_transcript_partial / voice: cooper how dick
  meta: kind=partial | timestamp=1783597664.3674295 | source=vosk | rms=443 | updated_at=1783597664.3154929 | frequency_hz=356.0
- [2026-07-09 19:47:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597664.559531 | source=vosk | rms=489 | updated_at=1783597664.559531 | frequency_hz=356.0
- [2026-07-09 19:47:44] operator / voice_transcript_partial / voice: alberta canada gluten nuggets
  meta: kind=partial | timestamp=1783597664.6203845 | source=vosk | rms=489 | updated_at=1783597664.559531 | frequency_hz=356.0
- [2026-07-09 19:47:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597664.8106203 | source=vosk | rms=268 | updated_at=1783597664.8096201 | frequency_hz=356.0
- [2026-07-09 19:47:45] operator / voice_transcript_final / voice: comic book
  meta: kind=final | timestamp=1783597665.430979 | source=final | rms=268 | updated_at=1783597664.8096201 | frequency_hz=356.0
- [2026-07-09 19:47:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597665.4630442 | source=vosk | rms=268 | updated_at=1783597664.8096201 | frequency_hz=356.0
- [2026-07-09 19:47:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597665.4630442 | source=vosk | rms=760 | updated_at=1783597665.4630442 | frequency_hz=356.0
- [2026-07-09 19:47:45] operator / voice_transcript_partial / voice: i'll be
  meta: kind=partial | timestamp=1783597665.8425148 | source=vosk | rms=1200 | updated_at=1783597665.8091447 | frequency_hz=356.0
- [2026-07-09 19:47:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597666.0600111 | source=vosk | rms=285 | updated_at=1783597666.0600111 | frequency_hz=356.0
- [2026-07-09 19:47:46] operator / voice_transcript_partial / voice: amish
  meta: kind=partial | timestamp=1783597666.069529 | source=vosk | rms=285 | updated_at=1783597666.0600111 | frequency_hz=356.0
- [2026-07-09 19:47:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597666.309637 | source=vosk | rms=728 | updated_at=1783597666.309637 | frequency_hz=356.0
- [2026-07-09 19:47:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597666.5600173 | source=vosk | rms=582 | updated_at=1783597666.5600173 | frequency_hz=356.0
- [2026-07-09 19:47:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597666.809524 | source=vosk | rms=651 | updated_at=1783597666.809524 | frequency_hz=356.0
- [2026-07-09 19:47:46] operator / voice_transcript_partial / voice: amish the
  meta: kind=partial | timestamp=1783597666.825658 | source=vosk | rms=651 | updated_at=1783597666.809524 | frequency_hz=356.0
- [2026-07-09 19:47:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597667.0594125 | source=vosk | rms=1033 | updated_at=1783597667.0594125 | frequency_hz=356.0
- [2026-07-09 19:47:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597667.310028 | source=vosk | rms=633 | updated_at=1783597667.310028 | frequency_hz=356.0
- [2026-07-09 19:47:47] operator / voice_transcript_partial / voice: amish the phone
  meta: kind=partial | timestamp=1783597667.3407145 | source=vosk | rms=633 | updated_at=1783597667.310028 | frequency_hz=356.0
- [2026-07-09 19:47:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597667.5608017 | source=vosk | rms=1174 | updated_at=1783597667.5608017 | frequency_hz=356.0
- [2026-07-09 19:47:47] operator / voice_transcript_partial / voice: amish the phone a lot
  meta: kind=partial | timestamp=1783597667.621433 | source=vosk | rms=1174 | updated_at=1783597667.5608017 | frequency_hz=356.0
- [2026-07-09 19:47:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597667.8098333 | source=vosk | rms=656 | updated_at=1783597667.8098333 | frequency_hz=356.0
- [2026-07-09 19:47:47] operator / voice_transcript_partial / voice: amish the phone a lot of
  meta: kind=partial | timestamp=1783597667.8857503 | source=vosk | rms=656 | updated_at=1783597667.8098333 | frequency_hz=356.0
- [2026-07-09 19:47:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597668.0597224 | source=vosk | rms=646 | updated_at=1783597668.0597224 | frequency_hz=356.0
- [2026-07-09 19:47:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597668.3095093 | source=vosk | rms=615 | updated_at=1783597668.3095093 | frequency_hz=356.0
- [2026-07-09 19:47:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597668.5593588 | source=vosk | rms=511 | updated_at=1783597668.5593588 | frequency_hz=356.0
- [2026-07-09 19:47:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597668.8101516 | source=vosk | rms=955 | updated_at=1783597668.8101516 | frequency_hz=356.0
- [2026-07-09 19:47:49] operator / voice_transcript_final / voice: amish the phone a lot of
  meta: kind=final | timestamp=1783597669.091971 | source=final | rms=955 | updated_at=1783597668.8101516 | frequency_hz=356.0
- [2026-07-09 19:47:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597669.2011106 | source=vosk | rms=656 | updated_at=1783597669.2011106 | frequency_hz=356.0
- [2026-07-09 19:47:49] operator / voice_transcript_partial / voice: for
  meta: kind=partial | timestamp=1783597669.361232 | source=vosk | rms=406 | updated_at=1783597669.3102663 | frequency_hz=356.0
- [2026-07-09 19:47:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597669.559757 | source=vosk | rms=385 | updated_at=1783597669.559757 | frequency_hz=356.0
- [2026-07-09 19:47:49] operator / voice_transcript_partial / voice: for slower than
  meta: kind=partial | timestamp=1783597669.610891 | source=vosk | rms=385 | updated_at=1783597669.559757 | frequency_hz=356.0
- [2026-07-09 19:47:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597669.8100562 | source=vosk | rms=721 | updated_at=1783597669.8100562 | frequency_hz=356.0
- [2026-07-09 19:47:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597670.0593507 | source=vosk | rms=926 | updated_at=1783597670.0593507 | frequency_hz=356.0
- [2026-07-09 19:47:50] operator / voice_transcript_partial / voice: for slower than think that
  meta: kind=partial | timestamp=1783597670.0775907 | source=vosk | rms=926 | updated_at=1783597670.0593507 | frequency_hz=356.0
- [2026-07-09 19:47:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597670.3108451 | source=vosk | rms=855 | updated_at=1783597670.3098462 | frequency_hz=356.0
- [2026-07-09 19:47:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597670.809817 | source=vosk | rms=855 | updated_at=1783597670.3098462 | frequency_hz=356.0
- [2026-07-09 19:47:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597671.0604153 | source=vosk | rms=1046 | updated_at=1783597671.0604153 | frequency_hz=356.0
- [2026-07-09 19:47:51] operator / voice_transcript_partial / voice: for slower than think that this
  meta: kind=partial | timestamp=1783597671.1015668 | source=vosk | rms=1046 | updated_at=1783597671.0604153 | frequency_hz=356.0
- [2026-07-09 19:47:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597671.309562 | source=vosk | rms=423 | updated_at=1783597671.309562 | frequency_hz=356.0
- [2026-07-09 19:47:51] operator / voice_transcript_partial / voice: for slower than think that the six
  meta: kind=partial | timestamp=1783597671.3579388 | source=vosk | rms=423 | updated_at=1783597671.309562 | frequency_hz=356.0
- [2026-07-09 19:47:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597671.559475 | source=vosk | rms=257 | updated_at=1783597671.559475 | frequency_hz=356.0
- [2026-07-09 19:47:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597671.810034 | source=vosk | rms=168 | updated_at=1783597671.810034 | frequency_hz=356.0
- [2026-07-09 19:47:52] operator / voice_transcript_final / voice: for slower than think that the six he silently
  meta: kind=final | timestamp=1783597672.6616747 | source=final | rms=168 | updated_at=1783597671.810034 | frequency_hz=356.0
- [2026-07-09 19:47:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597672.7890074 | source=vosk | rms=168 | updated_at=1783597671.810034 | frequency_hz=356.0
- [2026-07-09 19:47:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597672.7890074 | source=vosk | rms=288 | updated_at=1783597672.7890074 | frequency_hz=356.0
- [2026-07-09 19:47:52] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1783597672.8087413 | source=vosk | rms=288 | updated_at=1783597672.7890074 | frequency_hz=356.0
- [2026-07-09 19:47:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597673.3098965 | source=vosk | rms=1178 | updated_at=1783597672.8392882 | frequency_hz=356.0
- [2026-07-09 19:48:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597683.9998176 | source=vosk | rms=1200 | updated_at=1783597683.9998176 | frequency_hz=356.0
- [2026-07-09 19:48:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597684.7498794 | source=vosk | rms=1200 | updated_at=1783597683.9998176 | frequency_hz=356.0
- [2026-07-09 19:48:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597687.5038457 | source=vosk | rms=1200 | updated_at=1783597683.9998176 | frequency_hz=356.0
- [2026-07-09 19:48:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597687.9999156 | source=vosk | rms=1200 | updated_at=1783597683.9998176 | frequency_hz=356.0
- [2026-07-09 19:48:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597688.2496483 | source=vosk | rms=1200 | updated_at=1783597683.9998176 | frequency_hz=356.0
- [2026-07-09 19:48:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597688.749663 | source=vosk | rms=1200 | updated_at=1783597683.9998176 | frequency_hz=356.0
- [2026-07-09 19:48:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597689.000284 | source=vosk | rms=346 | updated_at=1783597689.000284 | frequency_hz=356.0
- [2026-07-09 19:48:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597691.2503047 | source=vosk | rms=830 | updated_at=1783597690.750131 | frequency_hz=356.0
- [2026-07-09 19:48:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597693.3610797 | source=vosk | rms=406 | updated_at=1783597693.3600798 | frequency_hz=356.0
- [2026-07-09 19:48:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597693.860479 | source=vosk | rms=406 | updated_at=1783597693.3600798 | frequency_hz=356.0
- [2026-07-09 19:48:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597701.1100411 | source=vosk | rms=416 | updated_at=1783597701.1100411 | frequency_hz=356.0
- [2026-07-09 19:48:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597701.8783424 | source=vosk | rms=416 | updated_at=1783597701.1100411 | frequency_hz=356.0
- [2026-07-09 19:48:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597702.3598402 | source=vosk | rms=296 | updated_at=1783597702.3598402 | frequency_hz=356.0
- [2026-07-09 19:48:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597702.8605642 | source=vosk | rms=296 | updated_at=1783597702.3598402 | frequency_hz=356.0
- [2026-07-09 19:48:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597707.860242 | source=vosk | rms=296 | updated_at=1783597702.3598402 | frequency_hz=356.0
- [2026-07-09 19:48:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597708.3605714 | source=vosk | rms=296 | updated_at=1783597702.3598402 | frequency_hz=356.0
- [2026-07-09 19:48:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597708.6144905 | source=vosk | rms=470 | updated_at=1783597708.6144905 | frequency_hz=356.0
- [2026-07-09 19:48:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597709.1104958 | source=vosk | rms=470 | updated_at=1783597708.6144905 | frequency_hz=356.0
- [2026-07-09 19:48:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597712.4252577 | source=vosk | rms=1204 | updated_at=1783597712.4252577 | frequency_hz=356.0
- [2026-07-09 19:48:33] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1783597713.1361053 | source=final | rms=229 | updated_at=1783597712.9205635 | frequency_hz=356.0
- [2026-07-09 19:48:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597713.1701736 | source=vosk | rms=210 | updated_at=1783597713.1701736 | frequency_hz=356.0
- [2026-07-09 19:48:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597713.678185 | source=vosk | rms=210 | updated_at=1783597713.1701736 | frequency_hz=356.0
- [2026-07-09 19:48:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597714.9204085 | source=vosk | rms=343 | updated_at=1783597714.9204085 | frequency_hz=356.0
- [2026-07-09 19:48:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597715.9206924 | source=vosk | rms=1184 | updated_at=1783597715.1700401 | frequency_hz=356.0
- [2026-07-09 19:48:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597716.419766 | source=vosk | rms=1184 | updated_at=1783597715.1700401 | frequency_hz=356.0
- [2026-07-09 19:48:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597716.9218335 | source=vosk | rms=1184 | updated_at=1783597715.1700401 | frequency_hz=356.0
- [2026-07-09 19:48:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597717.1705804 | source=vosk | rms=1184 | updated_at=1783597715.1700401 | frequency_hz=356.0
- [2026-07-09 19:48:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597717.670247 | source=vosk | rms=1184 | updated_at=1783597715.1700401 | frequency_hz=356.0
- [2026-07-09 19:48:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597718.920396 | source=vosk | rms=1184 | updated_at=1783597715.1700401 | frequency_hz=356.0
- [2026-07-09 19:48:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597719.4205675 | source=vosk | rms=1184 | updated_at=1783597715.1700401 | frequency_hz=356.0
- [2026-07-09 19:48:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597721.670812 | source=vosk | rms=1184 | updated_at=1783597715.1700401 | frequency_hz=356.0
- [2026-07-09 19:48:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597722.1717427 | source=vosk | rms=1184 | updated_at=1783597715.1700401 | frequency_hz=356.0
- [2026-07-09 19:48:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597736.0010765 | source=vosk | rms=506 | updated_at=1783597736.0010765 | frequency_hz=356.0
- [2026-07-09 19:49:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597741.5004036 | source=vosk | rms=225 | updated_at=1783597740.0011475 | frequency_hz=356.0
- [2026-07-09 19:49:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597742.5008814 | source=vosk | rms=225 | updated_at=1783597740.0011475 | frequency_hz=356.0
- [2026-07-09 19:49:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597744.501193 | source=vosk | rms=401 | updated_at=1783597744.0007014 | frequency_hz=358.1
- [2026-07-09 19:49:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597745.5007083 | source=vosk | rms=401 | updated_at=1783597744.0007014 | frequency_hz=358.1
- [2026-07-09 19:49:07] operator / voice_transcript_final / voice: with
  meta: kind=final | timestamp=1783597747.4712923 | source=final | rms=204 | updated_at=1783597747.001249 | frequency_hz=358.1
- [2026-07-09 19:49:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597747.548413 | source=vosk | rms=204 | updated_at=1783597747.001249 | frequency_hz=358.1
- [2026-07-09 19:49:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597747.548413 | source=vosk | rms=281 | updated_at=1783597747.548413 | frequency_hz=358.1
- [2026-07-09 19:49:07] operator / voice_transcript_partial / voice: principal
  meta: kind=partial | timestamp=1783597747.7708826 | source=vosk | rms=235 | updated_at=1783597747.7504628 | frequency_hz=358.1
- [2026-07-09 19:49:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597748.0008783 | source=vosk | rms=187 | updated_at=1783597748.0008783 | frequency_hz=358.1
- [2026-07-09 19:49:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597748.2556229 | source=vosk | rms=221 | updated_at=1783597748.2556229 | frequency_hz=358.1
- [2026-07-09 19:49:08] operator / voice_transcript_partial / voice: principal going
  meta: kind=partial | timestamp=1783597748.3148534 | source=vosk | rms=221 | updated_at=1783597748.2556229 | frequency_hz=358.1
- [2026-07-09 19:49:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597748.750856 | source=vosk | rms=221 | updated_at=1783597748.2556229 | frequency_hz=358.1
- [2026-07-09 19:49:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597751.250783 | source=vosk | rms=169 | updated_at=1783597751.250783 | frequency_hz=358.1
- [2026-07-09 19:49:11] operator / voice_transcript_partial / voice: principal going to
  meta: kind=partial | timestamp=1783597751.2854733 | source=vosk | rms=169 | updated_at=1783597751.250783 | frequency_hz=358.1
- [2026-07-09 19:49:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597751.5688074 | source=vosk | rms=169 | updated_at=1783597751.250783 | frequency_hz=358.1
- [2026-07-09 19:49:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597752.0008059 | source=vosk | rms=169 | updated_at=1783597751.250783 | frequency_hz=358.1
- [2026-07-09 19:49:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597752.5019183 | source=vosk | rms=131 | updated_at=1783597752.5019183 | frequency_hz=358.1
- [2026-07-09 19:49:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597752.7519026 | source=vosk | rms=144 | updated_at=1783597752.7519026 | frequency_hz=358.1
- [2026-07-09 19:49:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597753.0007112 | source=vosk | rms=142 | updated_at=1783597753.0007112 | frequency_hz=358.1
- [2026-07-09 19:49:13] operator / voice_transcript_partial / voice: principal going to bring up
  meta: kind=partial | timestamp=1783597753.0480807 | source=vosk | rms=142 | updated_at=1783597753.0007112 | frequency_hz=358.1
- [2026-07-09 19:49:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597753.2521074 | source=vosk | rms=180 | updated_at=1783597753.2521074 | frequency_hz=358.1
- [2026-07-09 19:49:13] operator / voice_transcript_partial / voice: principal going to bring
  meta: kind=partial | timestamp=1783597753.2816858 | source=vosk | rms=180 | updated_at=1783597753.2521074 | frequency_hz=358.1
- [2026-07-09 19:49:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597753.500467 | source=vosk | rms=253 | updated_at=1783597753.500467 | frequency_hz=358.1
- [2026-07-09 19:49:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597753.9398234 | source=vosk | rms=182 | updated_at=1783597753.9398234 | frequency_hz=358.1
- [2026-07-09 19:49:13] operator / voice_transcript_partial / voice: principal going to bring a new
  meta: kind=partial | timestamp=1783597753.9689364 | source=vosk | rms=182 | updated_at=1783597753.9398234 | frequency_hz=358.1
- [2026-07-09 19:49:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597754.500624 | source=vosk | rms=182 | updated_at=1783597753.9398234 | frequency_hz=358.1
- [2026-07-09 19:49:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597756.252248 | source=vosk | rms=260 | updated_at=1783597756.252248 | frequency_hz=358.1
- [2026-07-09 19:49:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597756.501292 | source=vosk | rms=359 | updated_at=1783597756.501292 | frequency_hz=358.1
- [2026-07-09 19:49:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597756.750823 | source=vosk | rms=345 | updated_at=1783597756.750823 | frequency_hz=358.1
- [2026-07-09 19:49:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597757.0013468 | source=vosk | rms=964 | updated_at=1783597757.0013468 | frequency_hz=358.1
- [2026-07-09 19:49:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597757.2512674 | source=vosk | rms=486 | updated_at=1783597757.2512674 | frequency_hz=358.1
- [2026-07-09 19:49:17] operator / voice_transcript_partial / voice: principal going to bring a new superior to
  meta: kind=partial | timestamp=1783597757.2921543 | source=vosk | rms=486 | updated_at=1783597757.2512674 | frequency_hz=358.1
- [2026-07-09 19:49:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597757.5068557 | source=vosk | rms=329 | updated_at=1783597757.5068557 | frequency_hz=358.1
- [2026-07-09 19:49:17] operator / voice_transcript_partial / voice: principal going to bring a new secretary stitched
  meta: kind=partial | timestamp=1783597757.591363 | source=vosk | rms=329 | updated_at=1783597757.5068557 | frequency_hz=358.1
- [2026-07-09 19:49:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597757.7507472 | source=vosk | rms=193 | updated_at=1783597757.7507472 | frequency_hz=358.1
- [2026-07-09 19:49:17] operator / voice_transcript_partial / voice: principal going to bring a new superior teach their kids
  meta: kind=partial | timestamp=1783597757.7956567 | source=vosk | rms=193 | updated_at=1783597757.7507472 | frequency_hz=358.1
- [2026-07-09 19:49:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597758.000855 | source=vosk | rms=381 | updated_at=1783597758.000855 | frequency_hz=358.1
- [2026-07-09 19:49:18] operator / voice_transcript_partial / voice: principal going to bring a new secretary stitched reputable
  meta: kind=partial | timestamp=1783597758.042642 | source=vosk | rms=381 | updated_at=1783597758.000855 | frequency_hz=358.1
- [2026-07-09 19:49:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597758.2506413 | source=vosk | rms=152 | updated_at=1783597758.2506413 | frequency_hz=358.1
- [2026-07-09 19:49:18] operator / voice_transcript_partial / voice: principal going to bring a new secretary stitched get the
  meta: kind=partial | timestamp=1783597758.267262 | source=vosk | rms=152 | updated_at=1783597758.2506413 | frequency_hz=358.1
- [2026-07-09 19:49:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597758.9851658 | source=vosk | rms=152 | updated_at=1783597758.2506413 | frequency_hz=358.1
- [2026-07-09 19:49:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597761.0041668 | source=vosk | rms=163 | updated_at=1783597761.0041668 | frequency_hz=358.1
- [2026-07-09 19:49:21] operator / voice_transcript_partial / voice: principal going to bring a new secretary stitched get the boy
  meta: kind=partial | timestamp=1783597761.0184386 | source=vosk | rms=163 | updated_at=1783597761.0041668 | frequency_hz=358.1
- [2026-07-09 19:49:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597761.2510848 | source=vosk | rms=379 | updated_at=1783597761.2510848 | frequency_hz=358.1
- [2026-07-09 19:49:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597761.5011628 | source=vosk | rms=379 | updated_at=1783597761.2510848 | frequency_hz=358.1
- [2026-07-09 19:49:21] operator / voice_transcript_final / voice: principal going to bring a new secretary stitched get the boy
  meta: kind=final | timestamp=1783597761.7901478 | source=final | rms=379 | updated_at=1783597761.2510848 | frequency_hz=358.1
- [2026-07-09 19:49:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597761.910216 | source=vosk | rms=379 | updated_at=1783597761.2510848 | frequency_hz=358.1
- [2026-07-09 19:49:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597762.5037673 | source=vosk | rms=379 | updated_at=1783597761.2510848 | frequency_hz=358.1
- [2026-07-09 19:49:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597769.250939 | source=vosk | rms=346 | updated_at=1783597769.250939 | frequency_hz=358.1
- [2026-07-09 19:49:29] operator / voice_transcript_partial / voice: been
  meta: kind=partial | timestamp=1783597769.7761152 | source=vosk | rms=346 | updated_at=1783597769.250939 | frequency_hz=358.1
- [2026-07-09 19:49:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597770.0011616 | source=vosk | rms=168 | updated_at=1783597770.0011616 | frequency_hz=358.1
- [2026-07-09 19:49:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597770.5008392 | source=vosk | rms=168 | updated_at=1783597770.0011616 | frequency_hz=358.1
- [2026-07-09 19:49:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597782.7509139 | source=vosk | rms=145 | updated_at=1783597782.7509139 | frequency_hz=358.1
- [2026-07-09 19:49:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597783.7515955 | source=vosk | rms=124 | updated_at=1783597783.2526438 | frequency_hz=358.1
- [2026-07-09 19:49:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597795.0011077 | source=vosk | rms=253 | updated_at=1783597795.0011077 | frequency_hz=116.0
- [2026-07-09 19:49:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597796.2557423 | source=vosk | rms=437 | updated_at=1783597795.751434 | frequency_hz=116.0
- [2026-07-09 19:49:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597797.2519636 | source=vosk | rms=403 | updated_at=1783597797.2519636 | frequency_hz=116.0
- [2026-07-09 19:49:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597798.0014462 | source=vosk | rms=135 | updated_at=1783597797.5012665 | frequency_hz=116.0
- [2026-07-09 19:49:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597799.0012915 | source=vosk | rms=686 | updated_at=1783597799.0012915 | frequency_hz=116.0
- [2026-07-09 19:49:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597799.8928826 | source=vosk | rms=585 | updated_at=1783597799.251979 | frequency_hz=116.0
- [2026-07-09 19:50:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597800.003927 | source=vosk | rms=585 | updated_at=1783597799.251979 | frequency_hz=116.0
- [2026-07-09 19:50:00] operator / voice_transcript_final / voice: been
  meta: kind=final | timestamp=1783597800.9483652 | source=final | rms=557 | updated_at=1783597800.50612 | frequency_hz=116.0
- [2026-07-09 19:50:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597801.0040998 | source=vosk | rms=322 | updated_at=1783597801.0040998 | frequency_hz=116.0
- [2026-07-09 19:50:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597802.751368 | source=vosk | rms=310 | updated_at=1783597802.2520952 | frequency_hz=116.0
- [2026-07-09 19:50:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597803.002504 | source=vosk | rms=312 | updated_at=1783597803.002504 | frequency_hz=116.0
- [2026-07-09 19:50:03] operator / voice_transcript_partial / voice: a pretty good
  meta: kind=partial | timestamp=1783597803.0356972 | source=vosk | rms=312 | updated_at=1783597803.002504 | frequency_hz=116.0
- [2026-07-09 19:50:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597803.5018752 | source=vosk | rms=312 | updated_at=1783597803.002504 | frequency_hz=116.0
- [2026-07-09 19:50:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597804.0011983 | source=vosk | rms=312 | updated_at=1783597803.002504 | frequency_hz=116.0
- [2026-07-09 19:50:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597804.7515545 | source=vosk | rms=1200 | updated_at=1783597804.7515545 | frequency_hz=116.0
- [2026-07-09 19:50:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597805.001772 | source=vosk | rms=204 | updated_at=1783597805.001772 | frequency_hz=116.0
- [2026-07-09 19:50:05] operator / voice_transcript_final / voice: a pretty good
  meta: kind=final | timestamp=1783597805.278109 | source=final | rms=204 | updated_at=1783597805.001772 | frequency_hz=116.0
- [2026-07-09 19:50:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597805.4186916 | source=vosk | rms=345 | updated_at=1783597805.4186916 | frequency_hz=116.0
- [2026-07-09 19:50:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597806.7516592 | source=vosk | rms=236 | updated_at=1783597806.2520955 | frequency_hz=116.0
- [2026-07-09 19:50:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597807.751787 | source=vosk | rms=236 | updated_at=1783597806.2520955 | frequency_hz=116.0
- [2026-07-09 19:50:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597808.7509573 | source=vosk | rms=349 | updated_at=1783597808.2519958 | frequency_hz=116.0
- [2026-07-09 19:50:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597809.268886 | source=vosk | rms=205 | updated_at=1783597809.268886 | frequency_hz=116.0
- [2026-07-09 19:50:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597809.7518387 | source=vosk | rms=205 | updated_at=1783597809.268886 | frequency_hz=116.0
- [2026-07-09 19:50:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597812.2517142 | source=vosk | rms=205 | updated_at=1783597809.268886 | frequency_hz=116.0
- [2026-07-09 19:50:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597812.7519162 | source=vosk | rms=205 | updated_at=1783597809.268886 | frequency_hz=116.0
- [2026-07-09 19:50:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597814.252221 | source=vosk | rms=1201 | updated_at=1783597814.252221 | frequency_hz=116.0
- [2026-07-09 19:50:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597815.0016408 | source=vosk | rms=626 | updated_at=1783597814.5015907 | frequency_hz=116.0
- [2026-07-09 19:50:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597815.5029335 | source=vosk | rms=626 | updated_at=1783597814.5015907 | frequency_hz=116.0
- [2026-07-09 19:50:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597816.0022118 | source=vosk | rms=626 | updated_at=1783597814.5015907 | frequency_hz=116.0
- [2026-07-09 19:50:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597816.7515297 | source=vosk | rms=400 | updated_at=1783597816.7515297 | frequency_hz=116.0
- [2026-07-09 19:50:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597819.50227 | source=vosk | rms=508 | updated_at=1783597819.0015478 | frequency_hz=116.0
- [2026-07-09 19:50:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597819.754053 | source=vosk | rms=676 | updated_at=1783597819.754053 | frequency_hz=116.0
- [2026-07-09 19:50:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597820.752342 | source=vosk | rms=719 | updated_at=1783597820.2520459 | frequency_hz=116.0
- [2026-07-09 19:50:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597835.7577534 | source=vosk | rms=719 | updated_at=1783597820.2520459 | frequency_hz=116.0
- [2026-07-09 19:50:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597836.2522404 | source=vosk | rms=719 | updated_at=1783597820.2520459 | frequency_hz=116.0
- [2026-07-09 19:50:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597836.5022259 | source=vosk | rms=719 | updated_at=1783597820.2520459 | frequency_hz=116.0
- [2026-07-09 19:50:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597837.7522478 | source=vosk | rms=455 | updated_at=1783597837.252568 | frequency_hz=116.0
- [2026-07-09 19:50:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597839.2526464 | source=vosk | rms=455 | updated_at=1783597837.252568 | frequency_hz=116.0
- [2026-07-09 19:50:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597839.7525313 | source=vosk | rms=455 | updated_at=1783597837.252568 | frequency_hz=116.0
- [2026-07-09 19:50:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597841.0036309 | source=vosk | rms=417 | updated_at=1783597841.0036309 | frequency_hz=116.0
- [2026-07-09 19:50:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597841.5020726 | source=vosk | rms=417 | updated_at=1783597841.0036309 | frequency_hz=116.0
- [2026-07-09 19:50:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597842.5021138 | source=vosk | rms=291 | updated_at=1783597842.5021138 | frequency_hz=116.0
- [2026-07-09 19:50:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597843.253574 | source=vosk | rms=289 | updated_at=1783597842.7524145 | frequency_hz=116.0
- [2026-07-09 19:50:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597843.7529192 | source=vosk | rms=289 | updated_at=1783597842.7524145 | frequency_hz=116.0
- [2026-07-09 19:50:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597844.5021458 | source=vosk | rms=182 | updated_at=1783597844.0134225 | frequency_hz=116.0
- [2026-07-09 19:50:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597851.5026302 | source=vosk | rms=182 | updated_at=1783597844.0134225 | frequency_hz=116.0
- [2026-07-09 19:50:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597852.0027587 | source=vosk | rms=182 | updated_at=1783597844.0134225 | frequency_hz=116.0
- [2026-07-09 19:50:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597858.5029404 | source=vosk | rms=175 | updated_at=1783597858.5029404 | frequency_hz=116.0
- [2026-07-09 19:50:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597859.5028975 | source=vosk | rms=678 | updated_at=1783597858.7528 | frequency_hz=116.0
- [2026-07-09 19:50:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597859.753851 | source=vosk | rms=160 | updated_at=1783597859.753851 | frequency_hz=116.0
- [2026-07-09 19:51:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597861.5020885 | source=vosk | rms=386 | updated_at=1783597861.0026171 | frequency_hz=116.0
- [2026-07-09 19:51:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597861.7522185 | source=vosk | rms=168 | updated_at=1783597861.7522185 | frequency_hz=116.0
- [2026-07-09 19:51:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597862.5028493 | source=vosk | rms=567 | updated_at=1783597862.0016758 | frequency_hz=116.0
- [2026-07-09 19:51:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597863.002065 | source=vosk | rms=257 | updated_at=1783597863.002065 | frequency_hz=116.0
- [2026-07-09 19:51:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597867.2536132 | source=vosk | rms=266 | updated_at=1783597866.0029747 | frequency_hz=116.0
- [2026-07-09 19:51:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597867.5024576 | source=vosk | rms=266 | updated_at=1783597866.0029747 | frequency_hz=116.0
- [2026-07-09 19:51:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597868.2530103 | source=vosk | rms=216 | updated_at=1783597867.752223 | frequency_hz=116.0
- [2026-07-09 19:51:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597869.2602806 | source=vosk | rms=216 | updated_at=1783597867.752223 | frequency_hz=116.0
- [2026-07-09 19:51:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597870.5036328 | source=vosk | rms=127 | updated_at=1783597869.502145 | frequency_hz=116.0
- [2026-07-09 19:51:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597871.5020776 | source=vosk | rms=128 | updated_at=1783597871.5020776 | frequency_hz=116.0
- [2026-07-09 19:51:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597872.7155123 | source=vosk | rms=128 | updated_at=1783597871.5020776 | frequency_hz=116.0
- [2026-07-09 19:51:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597873.2118568 | source=vosk | rms=128 | updated_at=1783597871.5020776 | frequency_hz=116.0
- [2026-07-09 19:51:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597873.9767797 | source=vosk | rms=165 | updated_at=1783597873.4626124 | frequency_hz=116.0
- [2026-07-09 19:51:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597874.7129421 | source=vosk | rms=756 | updated_at=1783597874.7129421 | frequency_hz=116.0
- [2026-07-09 19:51:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597877.4629638 | source=vosk | rms=227 | updated_at=1783597876.9631686 | frequency_hz=116.0
- [2026-07-09 19:51:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597877.9630475 | source=vosk | rms=356 | updated_at=1783597877.9630475 | frequency_hz=116.0
- [2026-07-09 19:51:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597878.7138166 | source=vosk | rms=458 | updated_at=1783597878.2183888 | frequency_hz=116.0
- [2026-07-09 19:51:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597878.9625719 | source=vosk | rms=273 | updated_at=1783597878.9625719 | frequency_hz=116.0
- [2026-07-09 19:51:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597880.2139502 | source=vosk | rms=146 | updated_at=1783597879.4732182 | frequency_hz=116.0
- [2026-07-09 19:51:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597880.7148113 | source=vosk | rms=146 | updated_at=1783597879.4732182 | frequency_hz=116.0
- [2026-07-09 19:51:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597881.712195 | source=vosk | rms=146 | updated_at=1783597879.4732182 | frequency_hz=116.0
- [2026-07-09 19:51:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597887.0829146 | source=vosk | rms=908 | updated_at=1783597887.0829146 | frequency_hz=116.0
- [2026-07-09 19:51:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597887.5832186 | source=vosk | rms=908 | updated_at=1783597887.0829146 | frequency_hz=116.0
- [2026-07-09 19:51:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597889.5836403 | source=vosk | rms=264 | updated_at=1783597889.5836403 | frequency_hz=116.0
- [2026-07-09 19:51:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597890.083048 | source=vosk | rms=264 | updated_at=1783597889.5836403 | frequency_hz=116.0
- [2026-07-09 19:51:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597890.3324351 | source=vosk | rms=175 | updated_at=1783597890.3324351 | frequency_hz=116.0
- [2026-07-09 19:51:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597890.8359377 | source=vosk | rms=175 | updated_at=1783597890.3324351 | frequency_hz=116.0
- [2026-07-09 19:51:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597892.6939561 | source=vosk | rms=1203 | updated_at=1783597892.6939561 | frequency_hz=116.0
- [2026-07-09 19:51:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597894.1931355 | source=vosk | rms=1200 | updated_at=1783597893.6930513 | frequency_hz=116.0
- [2026-07-09 19:51:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597894.4428918 | source=vosk | rms=689 | updated_at=1783597894.4428918 | frequency_hz=116.0
- [2026-07-09 19:51:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597894.9466486 | source=vosk | rms=689 | updated_at=1783597894.4428918 | frequency_hz=116.0
- [2026-07-09 19:51:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597895.6943245 | source=vosk | rms=384 | updated_at=1783597895.6943245 | frequency_hz=116.0
- [2026-07-09 19:51:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597897.9456675 | source=vosk | rms=444 | updated_at=1783597897.4433906 | frequency_hz=116.0
- [2026-07-09 19:51:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597898.9425745 | source=vosk | rms=241 | updated_at=1783597898.9425745 | frequency_hz=116.0
- [2026-07-09 19:51:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597899.943431 | source=vosk | rms=617 | updated_at=1783597899.4429946 | frequency_hz=116.0
- [2026-07-09 19:51:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597900.193269 | source=vosk | rms=591 | updated_at=1783597900.193269 | frequency_hz=116.0
- [2026-07-09 19:51:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597902.303548 | source=vosk | rms=384 | updated_at=1783597901.8035119 | frequency_hz=116.0
- [2026-07-09 19:51:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597902.804457 | source=vosk | rms=384 | updated_at=1783597901.8035119 | frequency_hz=116.0
- [2026-07-09 19:51:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597904.304381 | source=vosk | rms=237 | updated_at=1783597903.8028984 | frequency_hz=116.0
- [2026-07-09 19:51:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597905.0542805 | source=vosk | rms=399 | updated_at=1783597905.0542805 | frequency_hz=116.0
- [2026-07-09 19:51:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597905.8033934 | source=vosk | rms=398 | updated_at=1783597905.3027265 | frequency_hz=116.0
- [2026-07-09 19:51:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597907.053643 | source=vosk | rms=366 | updated_at=1783597907.053643 | frequency_hz=116.0
- [2026-07-09 19:51:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597907.8031416 | source=vosk | rms=360 | updated_at=1783597907.3044667 | frequency_hz=116.0
- [2026-07-09 19:52:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597921.8034942 | source=vosk | rms=993 | updated_at=1783597921.8034942 | frequency_hz=116.0
- [2026-07-09 19:52:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597922.8043008 | source=vosk | rms=803 | updated_at=1783597922.303257 | frequency_hz=116.0
- [2026-07-09 19:52:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597923.0530915 | source=vosk | rms=625 | updated_at=1783597923.0530915 | frequency_hz=116.0
- [2026-07-09 19:52:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597924.052614 | source=vosk | rms=346 | updated_at=1783597923.5534422 | frequency_hz=116.0
- [2026-07-09 19:52:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597924.5535414 | source=vosk | rms=643 | updated_at=1783597924.5535414 | frequency_hz=116.0
- [2026-07-09 19:52:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597925.3036444 | source=vosk | rms=643 | updated_at=1783597924.5535414 | frequency_hz=116.0
- [2026-07-09 19:52:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597926.0533166 | source=vosk | rms=705 | updated_at=1783597926.0533166 | frequency_hz=116.0
- [2026-07-09 19:52:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597927.053215 | source=vosk | rms=607 | updated_at=1783597926.5554872 | frequency_hz=116.0
- [2026-07-09 19:52:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597928.0532963 | source=vosk | rms=237 | updated_at=1783597928.0532963 | frequency_hz=116.0
- [2026-07-09 19:52:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597929.055276 | source=vosk | rms=1075 | updated_at=1783597928.5531893 | frequency_hz=116.0
- [2026-07-09 19:52:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597929.305995 | source=vosk | rms=355 | updated_at=1783597929.305995 | frequency_hz=116.0
- [2026-07-09 19:52:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597930.0538118 | source=vosk | rms=355 | updated_at=1783597929.305995 | frequency_hz=116.0
- [2026-07-09 19:52:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597931.5533462 | source=vosk | rms=353 | updated_at=1783597931.5533462 | frequency_hz=116.0
- [2026-07-09 19:52:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597932.0547357 | source=vosk | rms=353 | updated_at=1783597931.5533462 | frequency_hz=116.0
- [2026-07-09 19:52:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597932.8032482 | source=vosk | rms=452 | updated_at=1783597932.8032482 | frequency_hz=182.5
- [2026-07-09 19:52:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597933.803862 | source=vosk | rms=390 | updated_at=1783597933.3032672 | frequency_hz=182.5
- [2026-07-09 19:52:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597935.5531797 | source=vosk | rms=390 | updated_at=1783597933.3032672 | frequency_hz=182.5
- [2026-07-09 19:52:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597936.0534406 | source=vosk | rms=390 | updated_at=1783597933.3032672 | frequency_hz=182.5
- [2026-07-09 19:52:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597947.303455 | source=vosk | rms=390 | updated_at=1783597933.3032672 | frequency_hz=182.5
- [2026-07-09 19:52:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597948.074228 | source=vosk | rms=597 | updated_at=1783597947.5538726 | frequency_hz=182.5
- [2026-07-09 19:52:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597949.0739486 | source=vosk | rms=263 | updated_at=1783597949.0739486 | frequency_hz=284.0
- [2026-07-09 19:52:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597951.3235316 | source=vosk | rms=134 | updated_at=1783597950.8245058 | frequency_hz=284.0
- [2026-07-09 19:52:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597952.5835752 | source=vosk | rms=134 | updated_at=1783597950.8245058 | frequency_hz=284.0
- [2026-07-09 19:52:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597953.3240716 | source=vosk | rms=134 | updated_at=1783597950.8245058 | frequency_hz=284.0
- [2026-07-09 19:52:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597953.8237562 | source=vosk | rms=134 | updated_at=1783597950.8245058 | frequency_hz=284.0
- [2026-07-09 19:52:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597954.5739498 | source=vosk | rms=134 | updated_at=1783597950.8245058 | frequency_hz=284.0
- [2026-07-09 19:52:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597955.0741706 | source=vosk | rms=382 | updated_at=1783597955.0741706 | frequency_hz=284.0
- [2026-07-09 19:52:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597955.5737045 | source=vosk | rms=382 | updated_at=1783597955.0741706 | frequency_hz=284.0
- [2026-07-09 19:52:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597955.8242419 | source=vosk | rms=382 | updated_at=1783597955.0741706 | frequency_hz=284.0
- [2026-07-09 19:52:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597957.0835874 | source=vosk | rms=382 | updated_at=1783597955.0741706 | frequency_hz=284.0
- [2026-07-09 19:52:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597957.5817726 | source=vosk | rms=382 | updated_at=1783597955.0741706 | frequency_hz=284.0
- [2026-07-09 19:52:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597958.9234192 | source=vosk | rms=382 | updated_at=1783597955.0741706 | frequency_hz=284.0
- [2026-07-09 19:52:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597960.6743507 | source=vosk | rms=382 | updated_at=1783597955.0741706 | frequency_hz=284.0
- [2026-07-09 19:52:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597962.9251623 | source=vosk | rms=146 | updated_at=1783597961.6737077 | frequency_hz=284.0
- [2026-07-09 19:52:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597963.1744194 | source=vosk | rms=146 | updated_at=1783597961.6737077 | frequency_hz=284.0
- [2026-07-09 19:52:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597963.6740124 | source=vosk | rms=146 | updated_at=1783597961.6737077 | frequency_hz=284.0
- [2026-07-09 19:52:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597964.1741617 | source=vosk | rms=146 | updated_at=1783597961.6737077 | frequency_hz=284.0
- [2026-07-09 19:52:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597965.174571 | source=vosk | rms=161 | updated_at=1783597964.6736453 | frequency_hz=284.0
- [2026-07-09 19:52:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597965.4359076 | source=vosk | rms=161 | updated_at=1783597964.6736453 | frequency_hz=284.0
- [2026-07-09 19:52:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597965.9252875 | source=vosk | rms=161 | updated_at=1783597964.6736453 | frequency_hz=284.0
- [2026-07-09 19:52:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597966.1742866 | source=vosk | rms=154 | updated_at=1783597966.1742866 | frequency_hz=284.0
- [2026-07-09 19:52:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597966.673818 | source=vosk | rms=154 | updated_at=1783597966.1742866 | frequency_hz=284.0
- [2026-07-09 19:52:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597967.6737015 | source=vosk | rms=139 | updated_at=1783597967.6737015 | frequency_hz=284.0
- [2026-07-09 19:52:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597973.9242096 | source=vosk | rms=142 | updated_at=1783597972.9264414 | frequency_hz=284.0
- [2026-07-09 19:52:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597974.1740167 | source=vosk | rms=142 | updated_at=1783597972.9264414 | frequency_hz=284.0
- [2026-07-09 19:52:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597975.425966 | source=vosk | rms=141 | updated_at=1783597974.924051 | frequency_hz=284.0
- [2026-07-09 19:52:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597975.673952 | source=vosk | rms=159 | updated_at=1783597975.673952 | frequency_hz=327.4
- [2026-07-09 19:53:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597980.9640863 | source=vosk | rms=189 | updated_at=1783597980.4643762 | frequency_hz=327.4
- [2026-07-09 19:53:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597982.4640064 | source=vosk | rms=339 | updated_at=1783597982.4640064 | frequency_hz=327.4
- [2026-07-09 19:53:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783597984.2138362 | source=vosk | rms=256 | updated_at=1783597983.7154908 | frequency_hz=327.4
- [2026-07-09 19:53:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783597999.7146 | source=vosk | rms=120 | updated_at=1783597999.7146 | frequency_hz=327.4
- [2026-07-09 19:53:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598000.9644272 | source=vosk | rms=147 | updated_at=1783598000.4754016 | frequency_hz=327.4
- [2026-07-09 19:53:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598002.2141545 | source=vosk | rms=147 | updated_at=1783598000.4754016 | frequency_hz=327.4
- [2026-07-09 19:53:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598003.2146823 | source=vosk | rms=424 | updated_at=1783598002.714748 | frequency_hz=327.4
- [2026-07-09 19:53:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598003.9643767 | source=vosk | rms=148 | updated_at=1783598003.9643767 | frequency_hz=327.4
- [2026-07-09 19:53:23] operator / voice_transcript_partial / voice: so
  meta: kind=partial | timestamp=1783598003.9920387 | source=vosk | rms=148 | updated_at=1783598003.9643767 | frequency_hz=327.4
- [2026-07-09 19:53:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598004.4649754 | source=vosk | rms=148 | updated_at=1783598003.9643767 | frequency_hz=327.4
- [2026-07-09 19:53:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598005.46483 | source=vosk | rms=148 | updated_at=1783598003.9643767 | frequency_hz=327.4
- [2026-07-09 19:53:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598005.7150836 | source=vosk | rms=148 | updated_at=1783598003.9643767 | frequency_hz=327.4
- [2026-07-09 19:53:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598006.2143502 | source=vosk | rms=148 | updated_at=1783598003.9643767 | frequency_hz=327.4
- [2026-07-09 19:53:26] operator / voice_transcript_final / voice: so
  meta: kind=final | timestamp=1783598006.4049733 | source=final | rms=148 | updated_at=1783598003.9643767 | frequency_hz=327.4
- [2026-07-09 19:53:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598006.7146823 | source=vosk | rms=148 | updated_at=1783598003.9643767 | frequency_hz=327.4
- [2026-07-09 19:53:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598006.9649677 | source=vosk | rms=148 | updated_at=1783598003.9643767 | frequency_hz=327.4
- [2026-07-09 19:53:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598008.468802 | source=vosk | rms=148 | updated_at=1783598003.9643767 | frequency_hz=327.4
- [2026-07-09 19:53:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598008.7150838 | source=vosk | rms=122 | updated_at=1783598008.7150838 | frequency_hz=327.4
- [2026-07-09 19:53:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598009.2148957 | source=vosk | rms=122 | updated_at=1783598008.7150838 | frequency_hz=327.4
- [2026-07-09 19:53:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598010.2154155 | source=vosk | rms=122 | updated_at=1783598008.7150838 | frequency_hz=327.4
- [2026-07-09 19:53:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598010.7145283 | source=vosk | rms=122 | updated_at=1783598008.7150838 | frequency_hz=327.4
- [2026-07-09 19:53:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598014.2647774 | source=vosk | rms=122 | updated_at=1783598008.7150838 | frequency_hz=327.4
- [2026-07-09 19:53:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598014.7650054 | source=vosk | rms=122 | updated_at=1783598008.7150838 | frequency_hz=327.4
- [2026-07-09 19:53:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598024.3552952 | source=vosk | rms=122 | updated_at=1783598008.7150838 | frequency_hz=327.4
- [2026-07-09 19:53:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598024.85536 | source=vosk | rms=122 | updated_at=1783598008.7150838 | frequency_hz=327.4
- [2026-07-09 19:53:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598028.3550525 | source=vosk | rms=532 | updated_at=1783598028.3550525 | frequency_hz=327.4
- [2026-07-09 19:53:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598029.3548098 | source=vosk | rms=639 | updated_at=1783598028.8644314 | frequency_hz=327.4
- [2026-07-09 19:53:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598030.604809 | source=vosk | rms=274 | updated_at=1783598030.604809 | frequency_hz=327.4
- [2026-07-09 19:53:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598031.1047802 | source=vosk | rms=274 | updated_at=1783598030.604809 | frequency_hz=327.4
- [2026-07-09 19:53:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598034.6063416 | source=vosk | rms=219 | updated_at=1783598034.6063416 | frequency_hz=327.4
- [2026-07-09 19:54:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598047.2125816 | source=vosk | rms=337 | updated_at=1783598046.712421 | frequency_hz=327.4
- [2026-07-09 19:54:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598049.4623957 | source=vosk | rms=337 | updated_at=1783598046.712421 | frequency_hz=327.4
- [2026-07-09 19:54:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598049.96201 | source=vosk | rms=337 | updated_at=1783598046.712421 | frequency_hz=327.4
- [2026-07-09 19:54:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598051.4620452 | source=vosk | rms=286 | updated_at=1783598051.4620452 | frequency_hz=327.4
- [2026-07-09 19:54:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598052.9625673 | source=vosk | rms=377 | updated_at=1783598051.7128143 | frequency_hz=327.4
- [2026-07-09 19:54:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598067.2122774 | source=vosk | rms=136 | updated_at=1783598067.2122774 | frequency_hz=327.4
- [2026-07-09 19:54:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598073.4626381 | source=vosk | rms=628 | updated_at=1783598072.9626637 | frequency_hz=327.4
- [2026-07-09 19:54:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598074.2123654 | source=vosk | rms=252 | updated_at=1783598074.2123654 | frequency_hz=327.4
- [2026-07-09 19:54:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598076.8664842 | source=vosk | rms=154 | updated_at=1783598076.212679 | frequency_hz=327.4
- [2026-07-09 19:54:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598076.96516 | source=vosk | rms=154 | updated_at=1783598076.212679 | frequency_hz=327.4
- [2026-07-09 19:54:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598083.31328 | source=vosk | rms=389 | updated_at=1783598082.813232 | frequency_hz=327.4
- [2026-07-09 19:54:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598083.8119888 | source=vosk | rms=249 | updated_at=1783598083.8119888 | frequency_hz=327.4
- [2026-07-09 19:54:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598085.33045 | source=vosk | rms=222 | updated_at=1783598084.5623746 | frequency_hz=327.4
- [2026-07-09 19:54:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598086.7928846 | source=vosk | rms=208 | updated_at=1783598086.7928846 | frequency_hz=327.4
- [2026-07-09 19:54:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598094.0426478 | source=vosk | rms=172 | updated_at=1783598093.542579 | frequency_hz=327.4
- [2026-07-09 19:54:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598095.0430784 | source=vosk | rms=172 | updated_at=1783598093.542579 | frequency_hz=327.4
- [2026-07-09 19:54:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598096.0425363 | source=vosk | rms=172 | updated_at=1783598093.542579 | frequency_hz=327.4
- [2026-07-09 19:54:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598096.5434284 | source=vosk | rms=427 | updated_at=1783598096.5434284 | frequency_hz=327.4
- [2026-07-09 19:54:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598097.043456 | source=vosk | rms=427 | updated_at=1783598096.5434284 | frequency_hz=327.4
- [2026-07-09 19:54:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598097.54284 | source=vosk | rms=427 | updated_at=1783598096.5434284 | frequency_hz=327.4
- [2026-07-09 19:54:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598098.2716258 | source=vosk | rms=427 | updated_at=1783598096.5434284 | frequency_hz=327.4
- [2026-07-09 19:55:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598111.6407585 | source=vosk | rms=232 | updated_at=1783598111.6407585 | frequency_hz=327.4
- [2026-07-09 19:55:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598112.139824 | source=vosk | rms=232 | updated_at=1783598111.6407585 | frequency_hz=327.4
- [2026-07-09 19:55:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598117.9521294 | source=vosk | rms=239 | updated_at=1783598117.9521294 | frequency_hz=327.4
- [2026-07-09 19:55:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598118.4048028 | source=vosk | rms=239 | updated_at=1783598117.9521294 | frequency_hz=327.4
- [2026-07-09 19:55:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598118.9046528 | source=vosk | rms=208 | updated_at=1783598118.9046528 | frequency_hz=327.4
- [2026-07-09 19:55:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598119.6565769 | source=vosk | rms=293 | updated_at=1783598119.155996 | frequency_hz=327.4
- [2026-07-09 19:55:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598120.4046986 | source=vosk | rms=293 | updated_at=1783598119.155996 | frequency_hz=327.4
- [2026-07-09 19:55:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598121.4050932 | source=vosk | rms=155 | updated_at=1783598120.9059517 | frequency_hz=327.4
- [2026-07-09 19:55:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598121.6541524 | source=vosk | rms=199 | updated_at=1783598121.6541524 | frequency_hz=327.4
- [2026-07-09 19:55:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598122.9043639 | source=vosk | rms=153 | updated_at=1783598121.9122791 | frequency_hz=327.4
- [2026-07-09 19:55:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598123.155309 | source=vosk | rms=153 | updated_at=1783598121.9122791 | frequency_hz=327.4
- [2026-07-09 19:55:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598124.1540437 | source=vosk | rms=153 | updated_at=1783598121.9122791 | frequency_hz=327.4
- [2026-07-09 19:55:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598127.4047897 | source=vosk | rms=400 | updated_at=1783598127.4047897 | frequency_hz=327.4
- [2026-07-09 19:55:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598128.6545377 | source=vosk | rms=158 | updated_at=1783598128.154967 | frequency_hz=327.4
- [2026-07-09 19:55:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598129.6546342 | source=vosk | rms=1200 | updated_at=1783598129.6546342 | frequency_hz=327.4
- [2026-07-09 19:55:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598131.4047081 | source=vosk | rms=467 | updated_at=1783598130.9045434 | frequency_hz=327.4
- [2026-07-09 19:55:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598132.1549149 | source=vosk | rms=514 | updated_at=1783598132.1549149 | frequency_hz=327.4
- [2026-07-09 19:55:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598133.654364 | source=vosk | rms=514 | updated_at=1783598132.1549149 | frequency_hz=327.4
- [2026-07-09 19:55:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598136.6756935 | source=vosk | rms=138 | updated_at=1783598136.6756935 | frequency_hz=327.4
- [2026-07-09 19:55:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598138.17608 | source=vosk | rms=233 | updated_at=1783598137.4254901 | frequency_hz=327.4
- [2026-07-09 19:55:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598139.675723 | source=vosk | rms=142 | updated_at=1783598139.675723 | frequency_hz=327.4
- [2026-07-09 19:55:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598140.28837 | source=vosk | rms=142 | updated_at=1783598139.675723 | frequency_hz=327.4
- [2026-07-09 19:55:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598141.0385985 | source=vosk | rms=137 | updated_at=1783598141.0385985 | frequency_hz=327.4
- [2026-07-09 19:55:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598141.7899528 | source=vosk | rms=139 | updated_at=1783598141.2887826 | frequency_hz=327.4
- [2026-07-09 19:55:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598144.0388324 | source=vosk | rms=139 | updated_at=1783598141.2887826 | frequency_hz=327.4
- [2026-07-09 19:55:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598144.5383735 | source=vosk | rms=139 | updated_at=1783598141.2887826 | frequency_hz=327.4
- [2026-07-09 19:55:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598148.5384696 | source=vosk | rms=274 | updated_at=1783598148.5384696 | frequency_hz=327.4
- [2026-07-09 19:55:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598149.2885678 | source=vosk | rms=228 | updated_at=1783598148.7886338 | frequency_hz=327.4
- [2026-07-09 19:55:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598149.7891936 | source=vosk | rms=228 | updated_at=1783598148.7886338 | frequency_hz=327.4
- [2026-07-09 19:55:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598150.7898679 | source=vosk | rms=141 | updated_at=1783598150.2890332 | frequency_hz=327.4
- [2026-07-09 19:55:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598151.2883906 | source=vosk | rms=221 | updated_at=1783598151.2883906 | frequency_hz=327.4
- [2026-07-09 19:55:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598152.5392091 | source=vosk | rms=305 | updated_at=1783598151.7888508 | frequency_hz=327.4
- [2026-07-09 19:55:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598152.7990737 | source=vosk | rms=424 | updated_at=1783598152.7990737 | frequency_hz=327.4
- [2026-07-09 19:55:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598153.538584 | source=vosk | rms=124 | updated_at=1783598153.038503 | frequency_hz=327.4
- [2026-07-09 19:55:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598153.7901833 | source=vosk | rms=124 | updated_at=1783598153.038503 | frequency_hz=327.4
- [2026-07-09 19:55:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598154.5386648 | source=vosk | rms=124 | updated_at=1783598153.038503 | frequency_hz=327.4
- [2026-07-09 19:55:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598155.2890317 | source=vosk | rms=256 | updated_at=1783598155.2890317 | frequency_hz=327.4
- [2026-07-09 19:55:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598156.0385087 | source=vosk | rms=256 | updated_at=1783598155.2890317 | frequency_hz=327.4
- [2026-07-09 19:55:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598157.0388463 | source=vosk | rms=256 | updated_at=1783598155.2890317 | frequency_hz=327.4
- [2026-07-09 19:55:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598157.539361 | source=vosk | rms=256 | updated_at=1783598155.2890317 | frequency_hz=327.4
- [2026-07-09 19:55:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598158.0386457 | source=vosk | rms=256 | updated_at=1783598155.2890317 | frequency_hz=327.4
- [2026-07-09 19:55:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598158.5386546 | source=vosk | rms=256 | updated_at=1783598155.2890317 | frequency_hz=327.4
- [2026-07-09 19:55:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598158.789239 | source=vosk | rms=256 | updated_at=1783598155.2890317 | frequency_hz=327.4
- [2026-07-09 19:56:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598163.2888663 | source=vosk | rms=1060 | updated_at=1783598162.788971 | frequency_hz=332.9
- [2026-07-09 19:56:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598166.789459 | source=vosk | rms=1060 | updated_at=1783598162.788971 | frequency_hz=332.9
- [2026-07-09 19:56:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598167.5387638 | source=vosk | rms=350 | updated_at=1783598167.044553 | frequency_hz=332.9
- [2026-07-09 19:56:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598167.7894156 | source=vosk | rms=350 | updated_at=1783598167.044553 | frequency_hz=332.9
- [2026-07-09 19:56:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598168.2889543 | source=vosk | rms=350 | updated_at=1783598167.044553 | frequency_hz=332.9
- [2026-07-09 19:56:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598168.7903423 | source=vosk | rms=156 | updated_at=1783598168.7903423 | frequency_hz=332.9
- [2026-07-09 19:56:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598169.2889438 | source=vosk | rms=156 | updated_at=1783598168.7903423 | frequency_hz=332.9
- [2026-07-09 19:56:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598169.7895849 | source=vosk | rms=178 | updated_at=1783598169.7895849 | frequency_hz=332.9
- [2026-07-09 19:56:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598170.5391738 | source=vosk | rms=278 | updated_at=1783598170.0389743 | frequency_hz=332.9
- [2026-07-09 19:56:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598172.5401998 | source=vosk | rms=278 | updated_at=1783598170.0389743 | frequency_hz=332.9
- [2026-07-09 19:56:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598173.0395632 | source=vosk | rms=278 | updated_at=1783598170.0389743 | frequency_hz=332.9
- [2026-07-09 19:56:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598174.0390782 | source=vosk | rms=278 | updated_at=1783598170.0389743 | frequency_hz=332.9
- [2026-07-09 19:56:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598174.7904778 | source=vosk | rms=275 | updated_at=1783598174.2895415 | frequency_hz=332.9
- [2026-07-09 19:56:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598175.300288 | source=vosk | rms=177 | updated_at=1783598175.300288 | frequency_hz=332.9
- [2026-07-09 19:56:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598176.039674 | source=vosk | rms=320 | updated_at=1783598175.5391216 | frequency_hz=332.9
- [2026-07-09 19:56:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598177.039446 | source=vosk | rms=320 | updated_at=1783598175.5391216 | frequency_hz=332.9
- [2026-07-09 19:56:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598177.7903636 | source=vosk | rms=320 | updated_at=1783598175.5391216 | frequency_hz=332.9
- [2026-07-09 19:56:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598178.2888412 | source=vosk | rms=320 | updated_at=1783598175.5391216 | frequency_hz=332.9
- [2026-07-09 19:56:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598180.7892308 | source=vosk | rms=145 | updated_at=1783598180.039487 | frequency_hz=332.9
- [2026-07-09 19:56:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598181.7891014 | source=vosk | rms=141 | updated_at=1783598181.7891014 | frequency_hz=332.9
- [2026-07-09 19:56:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598183.5394652 | source=vosk | rms=153 | updated_at=1783598183.039216 | frequency_hz=332.9
- [2026-07-09 19:56:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598184.5431192 | source=vosk | rms=251 | updated_at=1783598184.5431192 | frequency_hz=332.9
- [2026-07-09 19:56:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598186.0432796 | source=vosk | rms=464 | updated_at=1783598185.2898493 | frequency_hz=332.9
- [2026-07-09 19:56:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598186.5395713 | source=vosk | rms=464 | updated_at=1783598185.2898493 | frequency_hz=332.9
- [2026-07-09 19:56:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598187.5388472 | source=vosk | rms=464 | updated_at=1783598185.2898493 | frequency_hz=332.9
- [2026-07-09 19:56:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598188.038879 | source=vosk | rms=269 | updated_at=1783598188.038879 | frequency_hz=332.9
- [2026-07-09 19:56:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598189.7908463 | source=vosk | rms=146 | updated_at=1783598189.2916186 | frequency_hz=332.9
- [2026-07-09 19:56:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598191.7890012 | source=vosk | rms=146 | updated_at=1783598189.2916186 | frequency_hz=332.9
- [2026-07-09 19:56:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598197.8164499 | source=vosk | rms=125 | updated_at=1783598197.3176255 | frequency_hz=297.6
- [2026-07-09 19:56:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598198.0663795 | source=vosk | rms=348 | updated_at=1783598198.0663795 | frequency_hz=297.6
- [2026-07-09 19:56:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598198.816465 | source=vosk | rms=190 | updated_at=1783598198.3169687 | frequency_hz=297.6
- [2026-07-09 19:56:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598199.3161883 | source=vosk | rms=140 | updated_at=1783598199.3161883 | frequency_hz=297.6
- [2026-07-09 19:56:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598206.4118893 | source=vosk | rms=302 | updated_at=1783598205.6616938 | frequency_hz=297.6
- [2026-07-09 19:56:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598214.7971425 | source=vosk | rms=175 | updated_at=1783598214.7971425 | frequency_hz=297.6
- [2026-07-09 19:56:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598215.7976766 | source=vosk | rms=969 | updated_at=1783598215.297058 | frequency_hz=297.6
- [2026-07-09 19:56:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598217.046771 | source=vosk | rms=476 | updated_at=1783598217.046771 | frequency_hz=297.6
- [2026-07-09 19:56:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598217.5471046 | source=vosk | rms=476 | updated_at=1783598217.046771 | frequency_hz=297.6
- [2026-07-09 19:56:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598218.2989168 | source=vosk | rms=476 | updated_at=1783598217.046771 | frequency_hz=297.6
- [2026-07-09 19:56:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783598218.7963305 | source=vosk | rms=476 | updated_at=1783598217.046771 | frequency_hz=297.6
- [2026-07-09 19:57:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783598220.0471575 | source=vosk | rms=397 | updated_at=1783598220.0471575 | frequency_hz=297.6

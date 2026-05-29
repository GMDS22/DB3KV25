# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-14 19:35:29
- Entries: 124
- Roles: {'assistant': 2, 'system': 88, 'operator': 34}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 88, 'voice_transcript_partial': 30, 'voice_transcript_final': 4}
- Channels: {'text': 2, 'voice': 122}
- Latest operator request: thanks but no things
- Latest assistant message: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.
- Assistant text replies were generated without matching spoken assistant lines. Inspect human voice availability or auto-speak configuration.

## Timeline

- [2026-05-14 19:32:08] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-14 19:32:08] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-14 19:32:10] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778758330.300094 | source=vosk
- [2026-05-14 19:32:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758330.9204063 | source=vosk
- [2026-05-14 19:32:14] operator / voice_transcript_partial / voice: smarter eventually
  meta: kind=partial | timestamp=1778758334.6360862 | source=vosk | frequency_hz=98.0 | rms=137 | updated_at=1778758332.2699285
- [2026-05-14 19:32:15] operator / voice_transcript_partial / voice: smarter than before
  meta: kind=partial | timestamp=1778758335.0707815 | source=vosk | frequency_hz=98.0 | rms=137 | updated_at=1778758332.2699285
- [2026-05-14 19:32:15] operator / voice_transcript_final / voice: hello smarter than before
  meta: kind=final | timestamp=1778758335.7582939 | source=final | frequency_hz=98.0 | rms=137 | updated_at=1778758332.2699285
- [2026-05-14 19:32:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758336.6288364 | source=vosk | frequency_hz=98.0 | rms=137 | updated_at=1778758332.2699285
- [2026-05-14 19:32:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758337.8424554 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:32:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758337.8434558 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:32:17] operator / voice_transcript_partial / voice: so much
  meta: kind=partial | timestamp=1778758337.9695277 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:32:18] operator / voice_transcript_partial / voice: most central
  meta: kind=partial | timestamp=1778758338.0969 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:32:18] operator / voice_transcript_partial / voice: question three
  meta: kind=partial | timestamp=1778758338.1815958 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:32:19] operator / voice_transcript_final / voice: question three
  meta: kind=final | timestamp=1778758339.1588936 | source=final | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:32:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758339.193683 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:32:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758344.87922 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:32:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758347.3791804 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:32:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758347.879747 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:32:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758352.8800995 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:32:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758353.3792112 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:32:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758377.1312575 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:32:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758377.6303997 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:32:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758377.8796363 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:32:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758378.3799295 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:32:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758379.3805544 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:32:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758379.8805285 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758380.1315076 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758380.6303751 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758385.1303484 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758385.6298213 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758386.630518 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758387.1305146 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758392.3801186 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758392.8802996 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758395.8843153 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758396.711375 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758397.2186213 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758398.2124996 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758402.2129002 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758403.2127697 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758409.9625692 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758410.463044 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758414.2133462 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758414.963226 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758416.7170613 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758417.212939 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758420.7124972 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758421.2133014 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758424.2132828 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758424.7133782 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758428.4633312 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758429.962882 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758431.213504 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758431.7126052 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758432.9645019 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:33:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758433.463133 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758440.2190516 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758440.713713 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758445.7130108 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758446.212987 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758453.4631116 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758453.9637363 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758458.9634018 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758459.7134457 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758469.4637208 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758469.96369 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758471.9661837 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758472.4640722 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758478.4642687 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:39] operator / voice_transcript_partial / voice: run the smartest
  meta: kind=partial | timestamp=1778758479.2636044 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758479.7154086 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758489.9645672 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:49] operator / voice_transcript_partial / voice: run the smart city
  meta: kind=partial | timestamp=1778758489.9904695 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:50] operator / voice_transcript_partial / voice: run the smart said you need
  meta: kind=partial | timestamp=1778758490.2560441 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:50] operator / voice_transcript_partial / voice: run the smart said you need to be
  meta: kind=partial | timestamp=1778758490.5581257 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758491.2166853 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758493.714214 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:55] operator / voice_transcript_partial / voice: run the smart said you need to be not
  meta: kind=partial | timestamp=1778758495.2298808 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:55] operator / voice_transcript_partial / voice: run the smart said you need to be nice to meet
  meta: kind=partial | timestamp=1778758495.7435334 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758496.1813855 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758497.6804225 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:57] operator / voice_transcript_partial / voice: run the smart said you need to be nice to meet on
  meta: kind=partial | timestamp=1778758497.732821 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:58] operator / voice_transcript_partial / voice: run the smart said you needed me not to me learn anything
  meta: kind=partial | timestamp=1778758498.0369992 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:58] operator / voice_transcript_partial / voice: run the smart said you need to be nice to meet not immediately
  meta: kind=partial | timestamp=1778758498.2543879 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:58] operator / voice_transcript_partial / voice: run the smart said you need to be nice to meet up in unison
  meta: kind=partial | timestamp=1778758498.500314 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:59] operator / voice_transcript_partial / voice: run the smart said you need to be nice to meet up in unison me
  meta: kind=partial | timestamp=1778758499.209888 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:34:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758499.6800392 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758500.4306026 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:00] operator / voice_transcript_partial / voice: run the smart said you need to be nice to meet up in unison me right now
  meta: kind=partial | timestamp=1778758500.4708042 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758500.9309597 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758505.180849 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:05] operator / voice_transcript_partial / voice: run the smart said you need to be nice to meet up in unison me right now it
  meta: kind=partial | timestamp=1778758505.2078636 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:05] operator / voice_transcript_partial / voice: run the smart said you need to be nice to meet up in unison me right now it it
  meta: kind=partial | timestamp=1778758505.5736766 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:05] operator / voice_transcript_partial / voice: run the smart said you need to be nice to meet up in unison me right now i'm
  meta: kind=partial | timestamp=1778758505.7631323 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:05] operator / voice_transcript_partial / voice: run the smart said you need to be nice to meet up in unison me right now i'm noticing
  meta: kind=partial | timestamp=1778758505.9458516 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:06] operator / voice_transcript_partial / voice: run the smart said you need to be nice to meet up in unison me right now i'm not a few
  meta: kind=partial | timestamp=1778758506.2261057 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758506.6809196 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758509.4306858 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:09] operator / voice_transcript_partial / voice: run the smart said you need to be nice to meet up in unison me right now i'm not the police and
  meta: kind=partial | timestamp=1778758509.7086818 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:09] operator / voice_transcript_partial / voice: run the smart said you need to be nice to meet up in unison me right now i'm not the police and really
  meta: kind=partial | timestamp=1778758509.9629762 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:10] operator / voice_transcript_partial / voice: run the smart said you need to be nice to meet up in unison me right now i'm not the police and really know
  meta: kind=partial | timestamp=1778758510.4969923 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:10] operator / voice_transcript_partial / voice: run the smart said you need to be nice to meet up in unison me right now i'm not the police and really know much
  meta: kind=partial | timestamp=1778758510.7137382 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:11] operator / voice_transcript_final / voice: run the smart said you need me not to me learn in unison me right now it if i m not the police and really know
  meta: kind=final | timestamp=1778758511.9046185 | source=final | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758512.996522 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758512.996522 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:15] operator / voice_transcript_partial / voice: thanks but no
  meta: kind=partial | timestamp=1778758515.5237446 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:15] operator / voice_transcript_partial / voice: thanks but not
  meta: kind=partial | timestamp=1778758515.7942038 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:16] operator / voice_transcript_partial / voice: thanks but not the
  meta: kind=partial | timestamp=1778758516.0367105 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758516.501018 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758516.7477865 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:16] operator / voice_transcript_partial / voice: thanks but no things
  meta: kind=partial | timestamp=1778758516.762601 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758517.2477 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758518.746921 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758519.2472537 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758519.9978256 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758520.4990945 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758521.2478778 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:22] operator / voice_transcript_final / voice: thanks but no things
  meta: kind=final | timestamp=1778758522.449435 | source=final | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758522.6235623 | source=vosk | frequency_hz=100.0 | rms=127 | updated_at=1778758336.8794243
- [2026-05-14 19:35:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758523.80337 | source=vosk | frequency_hz=234.0 | rms=1602 | updated_at=1778758523.1242392
- [2026-05-14 19:35:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758523.80337 | source=vosk | frequency_hz=234.0 | rms=1602 | updated_at=1778758523.1242392
- [2026-05-14 19:35:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758524.3733659 | source=vosk | frequency_hz=234.0 | rms=1602 | updated_at=1778758523.1242392
- [2026-05-14 19:35:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1778758524.6237123 | source=vosk | frequency_hz=234.0 | rms=1602 | updated_at=1778758523.1242392
- [2026-05-14 19:35:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1778758528.123679 | source=vosk | frequency_hz=234.0 | rms=1602 | updated_at=1778758523.1242392

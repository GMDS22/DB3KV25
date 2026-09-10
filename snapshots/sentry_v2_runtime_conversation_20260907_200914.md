# SMART SENTRY V5.0.0 Runtime Conversation Export

- Generated: 2026-09-07 20:09:14
- Entries: 710
- Roles: {'assistant': 3, 'system': 530, 'operator': 177}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 530, 'spoken_confirmation': 1, 'voice_transcript_partial': 139, 'voice_transcript_final': 38}
- Channels: {'text': 2, 'voice': 708}
- Latest operator request: than that
- Latest assistant message: Smart Sentry is ready.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-09-07 20:01:05] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-09-07 20:01:05] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-09-07 20:01:07] system / voice_status / voice: listening
  meta: kind=status | timestamp=1788782467.38112 | source=vosk
- [2026-09-07 20:01:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782468.8401062 | source=vosk | rms=1201 | updated_at=1788782468.8401062
- [2026-09-07 20:01:45] assistant / spoken_confirmation / voice: Smart Sentry is ready.
  meta: interrupt=True | assistant_output=False | spoken=True
- [2026-09-07 20:01:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782482.0906582 | source=vosk | rms=392 | updated_at=1788782481.5906296
- [2026-09-07 20:01:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782482.5902576 | source=vosk | rms=392 | updated_at=1788782481.5906296
- [2026-09-07 20:01:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782484.59046 | source=vosk | rms=237 | updated_at=1788782483.3408387
- [2026-09-07 20:01:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782485.0907226 | source=vosk | rms=237 | updated_at=1788782483.3408387
- [2026-09-07 20:01:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782485.5903604 | source=vosk | rms=237 | updated_at=1788782483.3408387
- [2026-09-07 20:01:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782485.8402617 | source=vosk | rms=220 | updated_at=1788782485.8402617
- [2026-09-07 20:01:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782486.5908737 | source=vosk | rms=220 | updated_at=1788782485.8402617
- [2026-09-07 20:01:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782487.5913477 | source=vosk | rms=204 | updated_at=1788782487.5913477
- [2026-09-07 20:01:28] operator / voice_transcript_partial / voice: both
  meta: kind=partial | timestamp=1788782488.4068274 | source=vosk | rms=336 | updated_at=1788782488.3413956
- [2026-09-07 20:01:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782488.5905628 | source=vosk | rms=345 | updated_at=1788782488.5905628
- [2026-09-07 20:01:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782488.840971 | source=vosk | rms=264 | updated_at=1788782488.840971
- [2026-09-07 20:01:28] operator / voice_transcript_partial / voice: both to
  meta: kind=partial | timestamp=1788782488.8847775 | source=vosk | rms=264 | updated_at=1788782488.840971
- [2026-09-07 20:01:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782489.0909956 | source=vosk | rms=329 | updated_at=1788782489.0909956
- [2026-09-07 20:01:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782489.3410876 | source=vosk | rms=329 | updated_at=1788782489.0909956
- [2026-09-07 20:01:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782489.5913913 | source=vosk | rms=205 | updated_at=1788782489.5913913
- [2026-09-07 20:01:29] operator / voice_transcript_partial / voice: both to a contract
  meta: kind=partial | timestamp=1788782489.7209454 | source=vosk | rms=205 | updated_at=1788782489.5913913
- [2026-09-07 20:01:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782490.341265 | source=vosk | rms=205 | updated_at=1788782489.5913913
- [2026-09-07 20:01:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782490.8420596 | source=vosk | rms=205 | updated_at=1788782489.5913913
- [2026-09-07 20:01:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782491.340699 | source=vosk | rms=205 | updated_at=1788782489.5913913
- [2026-09-07 20:01:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782491.8406103 | source=vosk | rms=217 | updated_at=1788782491.8406103
- [2026-09-07 20:01:32] operator / voice_transcript_final / voice: both to theme a contract
  meta: kind=final | timestamp=1788782492.139856 | source=final | rms=217 | updated_at=1788782491.8406103
- [2026-09-07 20:01:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782493.0837877 | source=vosk | rms=217 | updated_at=1788782491.8406103
- [2026-09-07 20:01:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782493.0837877 | source=vosk | rms=217 | updated_at=1788782491.8406103
- [2026-09-07 20:01:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782494.8408375 | source=vosk | rms=217 | updated_at=1788782491.8406103
- [2026-09-07 20:01:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782495.0913718 | source=vosk | rms=280 | updated_at=1788782495.0913718
- [2026-09-07 20:01:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782500.091234 | source=vosk | rms=188 | updated_at=1788782499.5908544
- [2026-09-07 20:01:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782500.5914743 | source=vosk | rms=200 | updated_at=1788782500.5914743
- [2026-09-07 20:01:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782503.0913148 | source=vosk | rms=399 | updated_at=1788782501.0914779
- [2026-09-07 20:01:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782503.3415854 | source=vosk | rms=761 | updated_at=1788782503.3415854
- [2026-09-07 20:01:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782504.5916283 | source=vosk | rms=761 | updated_at=1788782503.3415854
- [2026-09-07 20:01:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782504.841462 | source=vosk | rms=297 | updated_at=1788782504.841462
- [2026-09-07 20:01:46] operator / voice_transcript_final / voice: commodity
  meta: kind=final | timestamp=1788782506.4649043 | source=final | rms=215 | updated_at=1788782505.0912325
- [2026-09-07 20:01:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782506.502783 | source=vosk | rms=207 | updated_at=1788782506.502783
- [2026-09-07 20:01:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782507.3410444 | source=vosk | rms=172 | updated_at=1788782506.629709
- [2026-09-07 20:01:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782507.5910287 | source=vosk | rms=195 | updated_at=1788782507.5910287
- [2026-09-07 20:01:48] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1788782508.382542 | source=vosk | rms=915 | updated_at=1788782508.3419993
- [2026-09-07 20:01:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782508.5925078 | source=vosk | rms=1205 | updated_at=1788782508.5925078
- [2026-09-07 20:01:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782508.8428397 | source=vosk | rms=1151 | updated_at=1788782508.8428397
- [2026-09-07 20:01:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782509.1271615 | source=vosk | rms=198 | updated_at=1788782509.1271615
- [2026-09-07 20:01:49] operator / voice_transcript_partial / voice: smart centralized
  meta: kind=partial | timestamp=1788782509.2287273 | source=vosk | rms=198 | updated_at=1788782509.1271615
- [2026-09-07 20:01:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782509.3418355 | source=vosk | rms=171 | updated_at=1788782509.3418355
- [2026-09-07 20:01:49] operator / voice_transcript_partial / voice: smart centralized branded with
  meta: kind=partial | timestamp=1788782509.4564364 | source=vosk | rms=171 | updated_at=1788782509.3418355
- [2026-09-07 20:01:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782509.5918503 | source=vosk | rms=173 | updated_at=1788782509.5918503
- [2026-09-07 20:01:49] operator / voice_transcript_partial / voice: smart centralized rounded
  meta: kind=partial | timestamp=1788782509.6802223 | source=vosk | rms=173 | updated_at=1788782509.5918503
- [2026-09-07 20:01:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782509.8424885 | source=vosk | rms=173 | updated_at=1788782509.5918503
- [2026-09-07 20:01:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782510.0917327 | source=vosk | rms=173 | updated_at=1788782509.5918503
- [2026-09-07 20:01:50] operator / voice_transcript_final / voice: smart centralized that
  meta: kind=final | timestamp=1788782510.805346 | source=final | rms=173 | updated_at=1788782509.5918503
- [2026-09-07 20:01:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782510.9110804 | source=vosk | rms=173 | updated_at=1788782509.5918503
- [2026-09-07 20:01:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782510.9110804 | source=vosk | rms=173 | updated_at=1788782509.5918503
- [2026-09-07 20:01:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782512.0926125 | source=vosk | rms=204 | updated_at=1788782510.9228563
- [2026-09-07 20:01:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782512.5917633 | source=vosk | rms=547 | updated_at=1788782512.5917633
- [2026-09-07 20:01:53] operator / voice_transcript_partial / voice: smart swear to
  meta: kind=partial | timestamp=1788782513.463779 | source=vosk | rms=783 | updated_at=1788782513.3427725
- [2026-09-07 20:01:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782513.59201 | source=vosk | rms=554 | updated_at=1788782513.59201
- [2026-09-07 20:01:53] operator / voice_transcript_partial / voice: smart for additional
  meta: kind=partial | timestamp=1788782513.7504506 | source=vosk | rms=554 | updated_at=1788782513.59201
- [2026-09-07 20:01:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782513.842714 | source=vosk | rms=350 | updated_at=1788782513.842714
- [2026-09-07 20:01:53] operator / voice_transcript_partial / voice: smart friday snowstorms
  meta: kind=partial | timestamp=1788782513.8908982 | source=vosk | rms=350 | updated_at=1788782513.842714
- [2026-09-07 20:01:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782514.0915356 | source=vosk | rms=350 | updated_at=1788782513.842714
- [2026-09-07 20:01:54] operator / voice_transcript_partial / voice: smart for additional
  meta: kind=partial | timestamp=1788782514.125391 | source=vosk | rms=350 | updated_at=1788782513.842714
- [2026-09-07 20:01:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782514.6030684 | source=vosk | rms=350 | updated_at=1788782513.842714
- [2026-09-07 20:01:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782515.092653 | source=vosk | rms=350 | updated_at=1788782513.842714
- [2026-09-07 20:01:55] operator / voice_transcript_partial / voice: smart for additional century
  meta: kind=partial | timestamp=1788782515.1440017 | source=vosk | rms=350 | updated_at=1788782513.842714
- [2026-09-07 20:01:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782515.3413427 | source=vosk | rms=350 | updated_at=1788782513.842714
- [2026-09-07 20:01:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782515.5914793 | source=vosk | rms=350 | updated_at=1788782513.842714
- [2026-09-07 20:01:55] operator / voice_transcript_final / voice: smart for additional century
  meta: kind=final | timestamp=1788782515.8518703 | source=final | rms=350 | updated_at=1788782513.842714
- [2026-09-07 20:01:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782515.9494295 | source=vosk | rms=520 | updated_at=1788782515.9494295
- [2026-09-07 20:01:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782516.5919402 | source=vosk | rms=520 | updated_at=1788782515.9494295
- [2026-09-07 20:02:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782520.841876 | source=vosk | rms=520 | updated_at=1788782515.9494295
- [2026-09-07 20:02:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782521.3415403 | source=vosk | rms=520 | updated_at=1788782515.9494295
- [2026-09-07 20:02:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782523.3423636 | source=vosk | rms=520 | updated_at=1788782515.9494295
- [2026-09-07 20:02:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782525.6017091 | source=vosk | rms=520 | updated_at=1788782515.9494295
- [2026-09-07 20:02:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782526.3429558 | source=vosk | rms=520 | updated_at=1788782515.9494295
- [2026-09-07 20:02:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782526.8417296 | source=vosk | rms=520 | updated_at=1788782515.9494295
- [2026-09-07 20:02:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782527.34363 | source=vosk | rms=520 | updated_at=1788782515.9494295
- [2026-09-07 20:02:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782529.6041272 | source=vosk | rms=272 | updated_at=1788782527.6272352
- [2026-09-07 20:02:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782530.6051862 | source=vosk | rms=272 | updated_at=1788782527.6272352
- [2026-09-07 20:02:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782531.0922186 | source=vosk | rms=272 | updated_at=1788782527.6272352
- [2026-09-07 20:02:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782531.8420372 | source=vosk | rms=243 | updated_at=1788782531.8420372
- [2026-09-07 20:02:12] operator / voice_transcript_final / voice: a of
  meta: kind=final | timestamp=1788782532.8707767 | source=final | rms=247 | updated_at=1788782532.6051822
- [2026-09-07 20:02:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782532.9019454 | source=vosk | rms=247 | updated_at=1788782532.6051822
- [2026-09-07 20:02:15] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1788782535.1573467 | source=vosk | rms=416 | updated_at=1788782535.0917432
- [2026-09-07 20:02:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782535.341723 | source=vosk | rms=416 | updated_at=1788782535.0917432
- [2026-09-07 20:02:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782536.0924988 | source=vosk | rms=416 | updated_at=1788782535.0917432
- [2026-09-07 20:02:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782536.3432178 | source=vosk | rms=416 | updated_at=1788782535.0917432
- [2026-09-07 20:02:16] operator / voice_transcript_partial / voice: i'm not going to
  meta: kind=partial | timestamp=1788782536.3987427 | source=vosk | rms=416 | updated_at=1788782535.0917432
- [2026-09-07 20:02:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782536.8434258 | source=vosk | rms=416 | updated_at=1788782535.0917432
- [2026-09-07 20:02:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782537.3429604 | source=vosk | rms=294 | updated_at=1788782537.3429604
- [2026-09-07 20:02:20] operator / voice_transcript_final / voice: the law
  meta: kind=final | timestamp=1788782540.2951312 | source=final | rms=228 | updated_at=1788782539.8419027
- [2026-09-07 20:02:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782540.3419328 | source=vosk | rms=318 | updated_at=1788782540.3419328
- [2026-09-07 20:02:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782546.8424592 | source=vosk | rms=392 | updated_at=1788782545.842624
- [2026-09-07 20:02:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782547.0927854 | source=vosk | rms=502 | updated_at=1788782547.0927854
- [2026-09-07 20:02:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782548.0926454 | source=vosk | rms=502 | updated_at=1788782547.0927854
- [2026-09-07 20:02:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782548.3435264 | source=vosk | rms=290 | updated_at=1788782548.3435264
- [2026-09-07 20:02:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782548.8423488 | source=vosk | rms=290 | updated_at=1788782548.3435264
- [2026-09-07 20:02:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782549.0919473 | source=vosk | rms=290 | updated_at=1788782548.3435264
- [2026-09-07 20:02:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782550.34232 | source=vosk | rms=276 | updated_at=1788782549.593553
- [2026-09-07 20:02:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782551.0924883 | source=vosk | rms=700 | updated_at=1788782551.0924883
- [2026-09-07 20:02:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782557.09314 | source=vosk | rms=356 | updated_at=1788782556.5917928
- [2026-09-07 20:02:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782557.5923626 | source=vosk | rms=356 | updated_at=1788782556.5917928
- [2026-09-07 20:02:38] operator / voice_transcript_partial / voice: it it
  meta: kind=partial | timestamp=1788782558.9210403 | source=vosk | rms=373 | updated_at=1788782558.8429615
- [2026-09-07 20:02:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782559.0935118 | source=vosk | rms=304 | updated_at=1788782559.0935118
- [2026-09-07 20:02:39] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1788782559.235269 | source=vosk | rms=304 | updated_at=1788782559.0935118
- [2026-09-07 20:02:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782559.3496833 | source=vosk | rms=336 | updated_at=1788782559.3496833
- [2026-09-07 20:02:39] operator / voice_transcript_partial / voice: did it but it didn't
  meta: kind=partial | timestamp=1788782559.4323602 | source=vosk | rms=336 | updated_at=1788782559.3496833
- [2026-09-07 20:02:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782559.5939126 | source=vosk | rms=239 | updated_at=1788782559.5939126
- [2026-09-07 20:02:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782560.092883 | source=vosk | rms=239 | updated_at=1788782559.5939126
- [2026-09-07 20:02:40] operator / voice_transcript_partial / voice: did it but it didn't have
  meta: kind=partial | timestamp=1788782560.115607 | source=vosk | rms=239 | updated_at=1788782559.5939126
- [2026-09-07 20:02:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782560.59244 | source=vosk | rms=239 | updated_at=1788782559.5939126
- [2026-09-07 20:02:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782560.8426976 | source=vosk | rms=239 | updated_at=1788782559.5939126
- [2026-09-07 20:02:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782561.093115 | source=vosk | rms=379 | updated_at=1788782561.093115
- [2026-09-07 20:02:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782561.3436992 | source=vosk | rms=557 | updated_at=1788782561.3436992
- [2026-09-07 20:02:41] operator / voice_transcript_final / voice: did it but it didn t have
  meta: kind=final | timestamp=1788782561.6638858 | source=final | rms=557 | updated_at=1788782561.3436992
- [2026-09-07 20:02:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782561.7664902 | source=vosk | rms=557 | updated_at=1788782561.3436992
- [2026-09-07 20:02:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782561.7664902 | source=vosk | rms=432 | updated_at=1788782561.7664902
- [2026-09-07 20:02:41] operator / voice_transcript_partial / voice: never thought
  meta: kind=partial | timestamp=1788782561.90423 | source=vosk | rms=265 | updated_at=1788782561.8423913
- [2026-09-07 20:02:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782562.3429139 | source=vosk | rms=279 | updated_at=1788782562.3429139
- [2026-09-07 20:02:42] operator / voice_transcript_partial / voice: never forget
  meta: kind=partial | timestamp=1788782562.3678327 | source=vosk | rms=279 | updated_at=1788782562.3429139
- [2026-09-07 20:02:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782562.8426867 | source=vosk | rms=279 | updated_at=1788782562.3429139
- [2026-09-07 20:02:42] operator / voice_transcript_partial / voice: never thought
  meta: kind=partial | timestamp=1788782562.8640149 | source=vosk | rms=279 | updated_at=1788782562.3429139
- [2026-09-07 20:02:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782563.3460329 | source=vosk | rms=279 | updated_at=1788782562.3429139
- [2026-09-07 20:02:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782563.5931828 | source=vosk | rms=279 | updated_at=1788782562.3429139
- [2026-09-07 20:02:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782563.8431015 | source=vosk | rms=279 | updated_at=1788782562.3429139
- [2026-09-07 20:02:44] operator / voice_transcript_final / voice: never thought
  meta: kind=final | timestamp=1788782564.025476 | source=final | rms=279 | updated_at=1788782562.3429139
- [2026-09-07 20:02:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782564.3427744 | source=vosk | rms=279 | updated_at=1788782562.3429139
- [2026-09-07 20:02:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782564.5926113 | source=vosk | rms=279 | updated_at=1788782562.3429139
- [2026-09-07 20:02:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782570.3438964 | source=vosk | rms=511 | updated_at=1788782569.8435974
- [2026-09-07 20:02:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782570.5927563 | source=vosk | rms=511 | updated_at=1788782569.8435974
- [2026-09-07 20:02:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782571.5933883 | source=vosk | rms=511 | updated_at=1788782569.8435974
- [2026-09-07 20:02:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782571.842245 | source=vosk | rms=373 | updated_at=1788782571.842245
- [2026-09-07 20:02:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782572.3441253 | source=vosk | rms=373 | updated_at=1788782571.842245
- [2026-09-07 20:02:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782572.5931199 | source=vosk | rms=373 | updated_at=1788782571.842245
- [2026-09-07 20:02:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782575.8432848 | source=vosk | rms=250 | updated_at=1788782574.8428223
- [2026-09-07 20:02:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782576.0934534 | source=vosk | rms=250 | updated_at=1788782574.8428223
- [2026-09-07 20:02:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782577.342839 | source=vosk | rms=293 | updated_at=1788782576.8428073
- [2026-09-07 20:02:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782577.8433516 | source=vosk | rms=406 | updated_at=1788782577.8433516
- [2026-09-07 20:02:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782578.3442264 | source=vosk | rms=406 | updated_at=1788782577.8433516
- [2026-09-07 20:02:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782579.0933886 | source=vosk | rms=313 | updated_at=1788782579.0933886
- [2026-09-07 20:02:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782579.8467302 | source=vosk | rms=254 | updated_at=1788782579.343371
- [2026-09-07 20:03:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782580.3431325 | source=vosk | rms=281 | updated_at=1788782580.3431325
- [2026-09-07 20:03:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782581.3432071 | source=vosk | rms=281 | updated_at=1788782580.3431325
- [2026-09-07 20:03:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782582.0932992 | source=vosk | rms=307 | updated_at=1788782582.0932992
- [2026-09-07 20:03:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782583.0938952 | source=vosk | rms=307 | updated_at=1788782582.0932992
- [2026-09-07 20:03:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782583.5937054 | source=vosk | rms=307 | updated_at=1788782582.0932992
- [2026-09-07 20:03:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782584.3445678 | source=vosk | rms=448 | updated_at=1788782583.8434076
- [2026-09-07 20:03:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782585.5935311 | source=vosk | rms=353 | updated_at=1788782585.5935311
- [2026-09-07 20:03:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782586.356929 | source=vosk | rms=353 | updated_at=1788782585.5935311
- [2026-09-07 20:03:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782588.3437388 | source=vosk | rms=353 | updated_at=1788782585.5935311
- [2026-09-07 20:03:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782589.8434834 | source=vosk | rms=353 | updated_at=1788782585.5935311
- [2026-09-07 20:03:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782590.5963717 | source=vosk | rms=353 | updated_at=1788782585.5935311
- [2026-09-07 20:03:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782591.0945933 | source=vosk | rms=353 | updated_at=1788782585.5935311
- [2026-09-07 20:03:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782591.3434696 | source=vosk | rms=353 | updated_at=1788782585.5935311
- [2026-09-07 20:03:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782592.8430758 | source=vosk | rms=295 | updated_at=1788782591.8438537
- [2026-09-07 20:03:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782593.093398 | source=vosk | rms=295 | updated_at=1788782591.8438537
- [2026-09-07 20:03:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782594.3437781 | source=vosk | rms=172 | updated_at=1788782593.843115
- [2026-09-07 20:03:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782594.5939844 | source=vosk | rms=172 | updated_at=1788782593.843115
- [2026-09-07 20:03:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782595.5936258 | source=vosk | rms=174 | updated_at=1788782595.0935478
- [2026-09-07 20:03:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782596.8432932 | source=vosk | rms=412 | updated_at=1788782596.8432932
- [2026-09-07 20:03:54] operator / voice_transcript_partial / voice: managers
  meta: kind=partial | timestamp=1788782634.3777587 | source=vosk | rms=511 | updated_at=1788782634.354299
- [2026-09-07 20:03:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782634.844572 | source=vosk | rms=511 | updated_at=1788782634.354299
- [2026-09-07 20:03:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782635.3445444 | source=vosk | rms=431 | updated_at=1788782635.3445444
- [2026-09-07 20:03:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782635.5954623 | source=vosk | rms=500 | updated_at=1788782635.5954623
- [2026-09-07 20:03:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782635.8810213 | source=vosk | rms=611 | updated_at=1788782635.8810213
- [2026-09-07 20:03:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782636.094325 | source=vosk | rms=611 | updated_at=1788782635.8810213
- [2026-09-07 20:03:56] operator / voice_transcript_final / voice: managers
  meta: kind=final | timestamp=1788782636.5368338 | source=final | rms=611 | updated_at=1788782635.8810213
- [2026-09-07 20:03:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782636.573376 | source=vosk | rms=611 | updated_at=1788782635.8810213
- [2026-09-07 20:03:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782636.573376 | source=vosk | rms=524 | updated_at=1788782636.573376
- [2026-09-07 20:03:57] operator / voice_transcript_partial / voice: each shot
  meta: kind=partial | timestamp=1788782637.989674 | source=vosk | rms=619 | updated_at=1788782637.3445778
- [2026-09-07 20:03:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782638.3754194 | source=vosk | rms=502 | updated_at=1788782638.37442
- [2026-09-07 20:04:00] operator / voice_transcript_partial / voice: english edition
  meta: kind=partial | timestamp=1788782640.9160373 | source=vosk | rms=806 | updated_at=1788782640.5953681
- [2026-09-07 20:04:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782641.0954578 | source=vosk | rms=387 | updated_at=1788782641.0954578
- [2026-09-07 20:04:01] operator / voice_transcript_partial / voice: finish
  meta: kind=partial | timestamp=1788782641.1906345 | source=vosk | rms=387 | updated_at=1788782641.0954578
- [2026-09-07 20:04:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782641.345345 | source=vosk | rms=387 | updated_at=1788782641.0954578
- [2026-09-07 20:04:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782641.596319 | source=vosk | rms=387 | updated_at=1788782641.0954578
- [2026-09-07 20:04:01] operator / voice_transcript_final / voice: each shot the finish
  meta: kind=final | timestamp=1788782641.8991337 | source=final | rms=387 | updated_at=1788782641.0954578
- [2026-09-07 20:04:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782642.001987 | source=vosk | rms=622 | updated_at=1788782642.001987
- [2026-09-07 20:04:04] operator / voice_transcript_partial / voice: you been to chicago
  meta: kind=partial | timestamp=1788782644.6352994 | source=vosk | rms=688 | updated_at=1788782644.5957716
- [2026-09-07 20:04:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782645.0952659 | source=vosk | rms=688 | updated_at=1788782644.5957716
- [2026-09-07 20:04:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782645.594119 | source=vosk | rms=548 | updated_at=1788782645.594119
- [2026-09-07 20:04:05] operator / voice_transcript_partial / voice: you been to church
  meta: kind=partial | timestamp=1788782645.637402 | source=vosk | rms=548 | updated_at=1788782645.594119
- [2026-09-07 20:04:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782645.8457198 | source=vosk | rms=548 | updated_at=1788782645.594119
- [2026-09-07 20:04:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782646.3790772 | source=vosk | rms=548 | updated_at=1788782645.594119
- [2026-09-07 20:04:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782646.5954103 | source=vosk | rms=448 | updated_at=1788782646.5954103
- [2026-09-07 20:04:06] operator / voice_transcript_partial / voice: you been to church and
  meta: kind=partial | timestamp=1788782646.6996887 | source=vosk | rms=448 | updated_at=1788782646.5954103
- [2026-09-07 20:04:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782646.8454893 | source=vosk | rms=667 | updated_at=1788782646.8454893
- [2026-09-07 20:04:06] operator / voice_transcript_partial / voice: you been to church
  meta: kind=partial | timestamp=1788782646.909724 | source=vosk | rms=667 | updated_at=1788782646.8454893
- [2026-09-07 20:04:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782647.0944915 | source=vosk | rms=526 | updated_at=1788782647.0944915
- [2026-09-07 20:04:07] operator / voice_transcript_partial / voice: you didn't change much
  meta: kind=partial | timestamp=1788782647.1291976 | source=vosk | rms=526 | updated_at=1788782647.0944915
- [2026-09-07 20:04:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782647.3445196 | source=vosk | rms=526 | updated_at=1788782647.0944915
- [2026-09-07 20:04:07] operator / voice_transcript_partial / voice: you been to church
  meta: kind=partial | timestamp=1788782647.3640215 | source=vosk | rms=526 | updated_at=1788782647.0944915
- [2026-09-07 20:04:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782647.5962121 | source=vosk | rms=526 | updated_at=1788782647.0944915
- [2026-09-07 20:04:07] operator / voice_transcript_partial / voice: you been to church child
  meta: kind=partial | timestamp=1788782647.637682 | source=vosk | rms=526 | updated_at=1788782647.0944915
- [2026-09-07 20:04:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782647.845182 | source=vosk | rms=483 | updated_at=1788782647.845182
- [2026-09-07 20:04:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782648.095344 | source=vosk | rms=778 | updated_at=1788782648.095344
- [2026-09-07 20:04:08] operator / voice_transcript_partial / voice: you been to church child after
  meta: kind=partial | timestamp=1788782648.1438944 | source=vosk | rms=778 | updated_at=1788782648.095344
- [2026-09-07 20:04:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782648.345578 | source=vosk | rms=438 | updated_at=1788782648.345578
- [2026-09-07 20:04:08] operator / voice_transcript_partial / voice: you been to church child after she
  meta: kind=partial | timestamp=1788782648.3728435 | source=vosk | rms=438 | updated_at=1788782648.345578
- [2026-09-07 20:04:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782648.5941317 | source=vosk | rms=438 | updated_at=1788782648.345578
- [2026-09-07 20:04:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782648.84555 | source=vosk | rms=576 | updated_at=1788782648.84555
- [2026-09-07 20:04:08] operator / voice_transcript_partial / voice: you been to church child after she coached
  meta: kind=partial | timestamp=1788782648.9013615 | source=vosk | rms=576 | updated_at=1788782648.84555
- [2026-09-07 20:04:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782649.095538 | source=vosk | rms=847 | updated_at=1788782649.095538
- [2026-09-07 20:04:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782649.3455155 | source=vosk | rms=847 | updated_at=1788782649.095538
- [2026-09-07 20:04:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782649.8454366 | source=vosk | rms=847 | updated_at=1788782649.095538
- [2026-09-07 20:04:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782650.3451762 | source=vosk | rms=580 | updated_at=1788782650.3451762
- [2026-09-07 20:04:10] operator / voice_transcript_final / voice: you been to church much a child after she coached
  meta: kind=final | timestamp=1788782650.6727092 | source=final | rms=580 | updated_at=1788782650.3451762
- [2026-09-07 20:04:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782650.8322747 | source=vosk | rms=580 | updated_at=1788782650.3451762
- [2026-09-07 20:04:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782650.8322747 | source=vosk | rms=937 | updated_at=1788782650.8322747
- [2026-09-07 20:04:11] operator / voice_transcript_partial / voice: catch
  meta: kind=partial | timestamp=1788782651.2180083 | source=vosk | rms=514 | updated_at=1788782651.1469097
- [2026-09-07 20:04:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782651.3454835 | source=vosk | rms=514 | updated_at=1788782651.1469097
- [2026-09-07 20:04:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782651.845406 | source=vosk | rms=514 | updated_at=1788782651.1469097
- [2026-09-07 20:04:12] operator / voice_transcript_final / voice: cats
  meta: kind=final | timestamp=1788782652.0653837 | source=final | rms=514 | updated_at=1788782651.1469097
- [2026-09-07 20:04:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782652.096477 | source=vosk | rms=514 | updated_at=1788782651.1469097
- [2026-09-07 20:04:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782652.5954802 | source=vosk | rms=514 | updated_at=1788782651.1469097
- [2026-09-07 20:04:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782653.345335 | source=vosk | rms=514 | updated_at=1788782651.1469097
- [2026-09-07 20:04:13] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1788782653.6595783 | source=vosk | rms=767 | updated_at=1788782653.5961835
- [2026-09-07 20:04:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782653.8460839 | source=vosk | rms=465 | updated_at=1788782653.8460839
- [2026-09-07 20:04:13] operator / voice_transcript_partial / voice: what the doctor
  meta: kind=partial | timestamp=1788782653.9035947 | source=vosk | rms=465 | updated_at=1788782653.8460839
- [2026-09-07 20:04:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782654.0955846 | source=vosk | rms=442 | updated_at=1788782654.0955846
- [2026-09-07 20:04:14] operator / voice_transcript_partial / voice: one perspective
  meta: kind=partial | timestamp=1788782654.1191757 | source=vosk | rms=442 | updated_at=1788782654.0955846
- [2026-09-07 20:04:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782654.3451486 | source=vosk | rms=832 | updated_at=1788782654.3451486
- [2026-09-07 20:04:14] operator / voice_transcript_partial / voice: what the doctor
  meta: kind=partial | timestamp=1788782654.3709424 | source=vosk | rms=832 | updated_at=1788782654.3451486
- [2026-09-07 20:04:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782654.5952177 | source=vosk | rms=442 | updated_at=1788782654.5952177
- [2026-09-07 20:04:14] operator / voice_transcript_partial / voice: what the doctor strange person
  meta: kind=partial | timestamp=1788782654.6439974 | source=vosk | rms=442 | updated_at=1788782654.5952177
- [2026-09-07 20:04:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782654.8482049 | source=vosk | rms=472 | updated_at=1788782654.8482049
- [2026-09-07 20:04:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782655.095301 | source=vosk | rms=472 | updated_at=1788782654.8482049
- [2026-09-07 20:04:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782655.345532 | source=vosk | rms=472 | updated_at=1788782654.8482049
- [2026-09-07 20:04:15] operator / voice_transcript_final / voice: what the doctor strange person
  meta: kind=final | timestamp=1788782655.6202302 | source=final | rms=472 | updated_at=1788782654.8482049
- [2026-09-07 20:04:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782655.8556874 | source=vosk | rms=557 | updated_at=1788782655.8556874
- [2026-09-07 20:04:16] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1788782656.8876724 | source=vosk | rms=461 | updated_at=1788782656.095241
- [2026-09-07 20:04:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782657.0954516 | source=vosk | rms=523 | updated_at=1788782657.0954516
- [2026-09-07 20:04:17] operator / voice_transcript_partial / voice: to get
  meta: kind=partial | timestamp=1788782657.188984 | source=vosk | rms=523 | updated_at=1788782657.0954516
- [2026-09-07 20:04:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782657.5955653 | source=vosk | rms=1179 | updated_at=1788782657.5955653
- [2026-09-07 20:04:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782657.8460355 | source=vosk | rms=1179 | updated_at=1788782657.5955653
- [2026-09-07 20:04:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782658.095576 | source=vosk | rms=1179 | updated_at=1788782657.5955653
- [2026-09-07 20:04:18] operator / voice_transcript_final / voice: the kids
  meta: kind=final | timestamp=1788782658.340021 | source=final | rms=1179 | updated_at=1788782657.5955653
- [2026-09-07 20:04:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782658.3700051 | source=vosk | rms=1179 | updated_at=1788782657.5955653
- [2026-09-07 20:04:21] operator / voice_transcript_partial / voice: like
  meta: kind=partial | timestamp=1788782661.746273 | source=vosk | rms=596 | updated_at=1788782661.3454585
- [2026-09-07 20:04:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782662.3456435 | source=vosk | rms=596 | updated_at=1788782661.3454585
- [2026-09-07 20:04:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782662.8454902 | source=vosk | rms=530 | updated_at=1788782662.8454902
- [2026-09-07 20:04:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782663.0953581 | source=vosk | rms=547 | updated_at=1788782663.0953581
- [2026-09-07 20:04:23] operator / voice_transcript_final / voice: to teach like
  meta: kind=final | timestamp=1788782663.7663934 | source=final | rms=547 | updated_at=1788782663.0953581
- [2026-09-07 20:04:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782663.8708963 | source=vosk | rms=547 | updated_at=1788782663.0953581
- [2026-09-07 20:04:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782663.8708963 | source=vosk | rms=815 | updated_at=1788782663.8708963
- [2026-09-07 20:04:23] operator / voice_transcript_partial / voice: he is
  meta: kind=partial | timestamp=1788782663.8894556 | source=vosk | rms=815 | updated_at=1788782663.8708963
- [2026-09-07 20:04:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782664.1153843 | source=vosk | rms=815 | updated_at=1788782663.8708963
- [2026-09-07 20:04:24] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1788782664.134555 | source=vosk | rms=815 | updated_at=1788782663.8708963
- [2026-09-07 20:04:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782664.3652794 | source=vosk | rms=768 | updated_at=1788782664.3652794
- [2026-09-07 20:04:24] operator / voice_transcript_partial / voice: he escaped me
  meta: kind=partial | timestamp=1788782664.3788548 | source=vosk | rms=768 | updated_at=1788782664.3652794
- [2026-09-07 20:04:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782664.865478 | source=vosk | rms=455 | updated_at=1788782664.865478
- [2026-09-07 20:04:24] operator / voice_transcript_partial / voice: he escaped people
  meta: kind=partial | timestamp=1788782664.9167976 | source=vosk | rms=455 | updated_at=1788782664.865478
- [2026-09-07 20:04:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782665.3663068 | source=vosk | rms=455 | updated_at=1788782664.865478
- [2026-09-07 20:04:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782665.6156206 | source=vosk | rms=455 | updated_at=1788782664.865478
- [2026-09-07 20:04:25] operator / voice_transcript_partial / voice: he escaped with
  meta: kind=partial | timestamp=1788782665.660767 | source=vosk | rms=455 | updated_at=1788782664.865478
- [2026-09-07 20:04:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782665.865524 | source=vosk | rms=490 | updated_at=1788782665.865524
- [2026-09-07 20:04:25] operator / voice_transcript_partial / voice: he is he was
  meta: kind=partial | timestamp=1788782665.899436 | source=vosk | rms=490 | updated_at=1788782665.865524
- [2026-09-07 20:04:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782666.115423 | source=vosk | rms=533 | updated_at=1788782666.115423
- [2026-09-07 20:04:26] operator / voice_transcript_final / voice: he escaped me bullshit
  meta: kind=final | timestamp=1788782666.41654 | source=final | rms=533 | updated_at=1788782666.115423
- [2026-09-07 20:04:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782666.5677614 | source=vosk | rms=533 | updated_at=1788782666.115423
- [2026-09-07 20:04:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782666.5677614 | source=vosk | rms=533 | updated_at=1788782666.115423
- [2026-09-07 20:04:28] operator / voice_transcript_partial / voice: stories
  meta: kind=partial | timestamp=1788782668.6352906 | source=vosk | rms=649 | updated_at=1788782668.6160824
- [2026-09-07 20:04:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782668.8656082 | source=vosk | rms=575 | updated_at=1788782668.8656082
- [2026-09-07 20:04:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782669.116161 | source=vosk | rms=575 | updated_at=1788782668.8656082
- [2026-09-07 20:04:29] operator / voice_transcript_partial / voice: stories and
  meta: kind=partial | timestamp=1788782669.1292944 | source=vosk | rms=575 | updated_at=1788782668.8656082
- [2026-09-07 20:04:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782669.3659854 | source=vosk | rms=575 | updated_at=1788782668.8656082
- [2026-09-07 20:04:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782669.6154747 | source=vosk | rms=575 | updated_at=1788782668.8656082
- [2026-09-07 20:04:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782669.8899958 | source=vosk | rms=487 | updated_at=1788782669.8899958
- [2026-09-07 20:04:30] operator / voice_transcript_final / voice: stories and
  meta: kind=final | timestamp=1788782670.8529768 | source=final | rms=487 | updated_at=1788782669.8899958
- [2026-09-07 20:04:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782670.889329 | source=vosk | rms=487 | updated_at=1788782669.8899958
- [2026-09-07 20:04:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782670.889329 | source=vosk | rms=487 | updated_at=1788782669.8899958
- [2026-09-07 20:04:31] operator / voice_transcript_partial / voice: the lead to operate
  meta: kind=partial | timestamp=1788782671.2059982 | source=vosk | rms=464 | updated_at=1788782671.1164043
- [2026-09-07 20:04:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782671.3662574 | source=vosk | rms=464 | updated_at=1788782671.1164043
- [2026-09-07 20:04:31] operator / voice_transcript_partial / voice: the lead to operating other
  meta: kind=partial | timestamp=1788782671.7086577 | source=vosk | rms=464 | updated_at=1788782671.1164043
- [2026-09-07 20:04:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782671.8664792 | source=vosk | rms=617 | updated_at=1788782671.8664792
- [2026-09-07 20:04:31] operator / voice_transcript_partial / voice: two older brothers
  meta: kind=partial | timestamp=1788782671.9166741 | source=vosk | rms=617 | updated_at=1788782671.8664792
- [2026-09-07 20:04:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782672.3653226 | source=vosk | rms=449 | updated_at=1788782672.3653226
- [2026-09-07 20:04:32] operator / voice_transcript_partial / voice: the lead to operating other you
  meta: kind=partial | timestamp=1788782672.4045188 | source=vosk | rms=449 | updated_at=1788782672.3653226
- [2026-09-07 20:04:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782672.8718357 | source=vosk | rms=449 | updated_at=1788782672.3653226
- [2026-09-07 20:04:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782673.365831 | source=vosk | rms=525 | updated_at=1788782673.365831
- [2026-09-07 20:04:33] operator / voice_transcript_partial / voice: the lead to operating under bush brought
  meta: kind=partial | timestamp=1788782673.3903804 | source=vosk | rms=525 | updated_at=1788782673.365831
- [2026-09-07 20:04:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782673.8683205 | source=vosk | rms=525 | updated_at=1788782673.365831
- [2026-09-07 20:04:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782674.6171784 | source=vosk | rms=804 | updated_at=1788782674.6171784
- [2026-09-07 20:04:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782674.865376 | source=vosk | rms=804 | updated_at=1788782674.6171784
- [2026-09-07 20:04:34] operator / voice_transcript_partial / voice: the lead to a restaurant association
  meta: kind=partial | timestamp=1788782674.9019282 | source=vosk | rms=804 | updated_at=1788782674.6171784
- [2026-09-07 20:04:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782675.115942 | source=vosk | rms=804 | updated_at=1788782674.6171784
- [2026-09-07 20:04:35] operator / voice_transcript_partial / voice: the lead to operating other you describe as your
  meta: kind=partial | timestamp=1788782675.1552799 | source=vosk | rms=804 | updated_at=1788782674.6171784
- [2026-09-07 20:04:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782675.6159837 | source=vosk | rms=804 | updated_at=1788782674.6171784
- [2026-09-07 20:04:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782676.1163726 | source=vosk | rms=804 | updated_at=1788782674.6171784
- [2026-09-07 20:04:36] operator / voice_transcript_partial / voice: the lead to operating other you describe as your post
  meta: kind=partial | timestamp=1788782676.1909661 | source=vosk | rms=804 | updated_at=1788782674.6171784
- [2026-09-07 20:04:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782676.3660553 | source=vosk | rms=530 | updated_at=1788782676.3660553
- [2026-09-07 20:04:36] operator / voice_transcript_partial / voice: the lead to operating under bush brought into
  meta: kind=partial | timestamp=1788782676.4079714 | source=vosk | rms=530 | updated_at=1788782676.3660553
- [2026-09-07 20:04:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782676.6161902 | source=vosk | rms=530 | updated_at=1788782676.3660553
- [2026-09-07 20:04:36] operator / voice_transcript_partial / voice: the lead to operating other you describe as your last
  meta: kind=partial | timestamp=1788782676.6466734 | source=vosk | rms=530 | updated_at=1788782676.3660553
- [2026-09-07 20:04:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782676.866043 | source=vosk | rms=530 | updated_at=1788782676.3660553
- [2026-09-07 20:04:36] operator / voice_transcript_partial / voice: the lead to operating other you describe as your entire
  meta: kind=partial | timestamp=1788782676.8980422 | source=vosk | rms=530 | updated_at=1788782676.3660553
- [2026-09-07 20:04:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782677.1155233 | source=vosk | rms=530 | updated_at=1788782676.3660553
- [2026-09-07 20:04:37] operator / voice_transcript_partial / voice: the lead to operating other you describe as your entire anthony
  meta: kind=partial | timestamp=1788782677.1508393 | source=vosk | rms=530 | updated_at=1788782676.3660553
- [2026-09-07 20:04:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782677.365467 | source=vosk | rms=530 | updated_at=1788782676.3660553
- [2026-09-07 20:04:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782677.6161923 | source=vosk | rms=530 | updated_at=1788782676.3660553
- [2026-09-07 20:04:37] operator / voice_transcript_partial / voice: the lead to operating other you describe as your entire anthony anthony
  meta: kind=partial | timestamp=1788782677.6575227 | source=vosk | rms=530 | updated_at=1788782676.3660553
- [2026-09-07 20:04:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782677.8663275 | source=vosk | rms=530 | updated_at=1788782676.3660553
- [2026-09-07 20:04:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782678.1160831 | source=vosk | rms=530 | updated_at=1788782676.3660553
- [2026-09-07 20:04:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782678.366042 | source=vosk | rms=530 | updated_at=1788782676.3660553
- [2026-09-07 20:04:38] operator / voice_transcript_final / voice: lead to operating other you brush brought your entire anthony anthony
  meta: kind=final | timestamp=1788782678.6305687 | source=final | rms=530 | updated_at=1788782676.3660553
- [2026-09-07 20:04:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782678.8654423 | source=vosk | rms=530 | updated_at=1788782676.3660553
- [2026-09-07 20:04:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782679.366341 | source=vosk | rms=530 | updated_at=1788782676.3660553
- [2026-09-07 20:04:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782679.6162827 | source=vosk | rms=554 | updated_at=1788782679.6162827
- [2026-09-07 20:04:39] operator / voice_transcript_partial / voice: so
  meta: kind=partial | timestamp=1788782679.6460376 | source=vosk | rms=554 | updated_at=1788782679.6162827
- [2026-09-07 20:04:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782679.8662007 | source=vosk | rms=891 | updated_at=1788782679.8662007
- [2026-09-07 20:04:40] operator / voice_transcript_partial / voice: so did that
  meta: kind=partial | timestamp=1788782680.1652646 | source=vosk | rms=534 | updated_at=1788782680.1161954
- [2026-09-07 20:04:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782680.616426 | source=vosk | rms=534 | updated_at=1788782680.1161954
- [2026-09-07 20:04:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782680.866216 | source=vosk | rms=534 | updated_at=1788782680.1161954
- [2026-09-07 20:04:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782681.1161308 | source=vosk | rms=481 | updated_at=1788782681.1161308
- [2026-09-07 20:04:41] operator / voice_transcript_partial / voice: so that people think
  meta: kind=partial | timestamp=1788782681.2261348 | source=vosk | rms=481 | updated_at=1788782681.1161308
- [2026-09-07 20:04:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782681.366051 | source=vosk | rms=537 | updated_at=1788782681.366051
- [2026-09-07 20:04:41] operator / voice_transcript_partial / voice: so that people
  meta: kind=partial | timestamp=1788782681.4351332 | source=vosk | rms=537 | updated_at=1788782681.366051
- [2026-09-07 20:04:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782681.8665051 | source=vosk | rms=478 | updated_at=1788782681.8665051
- [2026-09-07 20:04:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782682.366282 | source=vosk | rms=478 | updated_at=1788782681.8665051
- [2026-09-07 20:04:42] operator / voice_transcript_partial / voice: so that people should
  meta: kind=partial | timestamp=1788782682.399056 | source=vosk | rms=478 | updated_at=1788782681.8665051
- [2026-09-07 20:04:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782682.8662949 | source=vosk | rms=478 | updated_at=1788782681.8665051
- [2026-09-07 20:04:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782683.3667262 | source=vosk | rms=534 | updated_at=1788782683.3667262
- [2026-09-07 20:04:43] operator / voice_transcript_final / voice: so their own people
  meta: kind=final | timestamp=1788782683.7278645 | source=final | rms=534 | updated_at=1788782683.3667262
- [2026-09-07 20:04:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782683.8312364 | source=vosk | rms=534 | updated_at=1788782683.3667262
- [2026-09-07 20:04:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782683.8312364 | source=vosk | rms=477 | updated_at=1788782683.8312364
- [2026-09-07 20:04:44] operator / voice_transcript_partial / voice: so jealous
  meta: kind=partial | timestamp=1788782684.6610973 | source=vosk | rms=503 | updated_at=1788782684.616251
- [2026-09-07 20:04:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782684.8659492 | source=vosk | rms=558 | updated_at=1788782684.8659492
- [2026-09-07 20:04:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782685.1161942 | source=vosk | rms=668 | updated_at=1788782685.1161942
- [2026-09-07 20:04:45] operator / voice_transcript_final / voice: so jealous
  meta: kind=final | timestamp=1788782685.3361604 | source=final | rms=668 | updated_at=1788782685.1161942
- [2026-09-07 20:04:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782685.3709195 | source=vosk | rms=447 | updated_at=1788782685.3709195
- [2026-09-07 20:04:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782690.1165352 | source=vosk | rms=601 | updated_at=1788782689.6163836
- [2026-09-07 20:04:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782690.6165092 | source=vosk | rms=768 | updated_at=1788782690.6165092
- [2026-09-07 20:04:51] operator / voice_transcript_partial / voice: actually
  meta: kind=partial | timestamp=1788782691.1580422 | source=vosk | rms=498 | updated_at=1788782691.1162555
- [2026-09-07 20:04:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782691.3662739 | source=vosk | rms=509 | updated_at=1788782691.3662739
- [2026-09-07 20:04:51] operator / voice_transcript_partial / voice: actually i
  meta: kind=partial | timestamp=1788782691.4270964 | source=vosk | rms=509 | updated_at=1788782691.3662739
- [2026-09-07 20:04:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782691.866224 | source=vosk | rms=514 | updated_at=1788782691.866224
- [2026-09-07 20:04:51] operator / voice_transcript_partial / voice: he actually has
  meta: kind=partial | timestamp=1788782691.891509 | source=vosk | rms=514 | updated_at=1788782691.866224
- [2026-09-07 20:04:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782692.3668938 | source=vosk | rms=514 | updated_at=1788782691.866224
- [2026-09-07 20:04:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782692.8669968 | source=vosk | rms=514 | updated_at=1788782691.866224
- [2026-09-07 20:04:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782693.1178374 | source=vosk | rms=546 | updated_at=1788782693.1178374
- [2026-09-07 20:04:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782693.4460714 | source=vosk | rms=425 | updated_at=1788782693.4460714
- [2026-09-07 20:04:53] operator / voice_transcript_partial / voice: actually i
  meta: kind=partial | timestamp=1788782693.4614763 | source=vosk | rms=425 | updated_at=1788782693.4460714
- [2026-09-07 20:04:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782693.6430259 | source=vosk | rms=425 | updated_at=1788782693.4460714
- [2026-09-07 20:04:53] operator / voice_transcript_partial / voice: actually i think
  meta: kind=partial | timestamp=1788782693.6430259 | source=vosk | rms=425 | updated_at=1788782693.4460714
- [2026-09-07 20:04:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782693.866116 | source=vosk | rms=425 | updated_at=1788782693.4460714
- [2026-09-07 20:04:53] operator / voice_transcript_partial / voice: actually i got
  meta: kind=partial | timestamp=1788782693.9198353 | source=vosk | rms=425 | updated_at=1788782693.4460714
- [2026-09-07 20:04:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782694.1230812 | source=vosk | rms=425 | updated_at=1788782693.4460714
- [2026-09-07 20:04:54] operator / voice_transcript_partial / voice: actually i think
  meta: kind=partial | timestamp=1788782694.1710944 | source=vosk | rms=425 | updated_at=1788782693.4460714
- [2026-09-07 20:04:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782694.3668177 | source=vosk | rms=571 | updated_at=1788782694.3668177
- [2026-09-07 20:04:54] operator / voice_transcript_partial / voice: actually i think doctor
  meta: kind=partial | timestamp=1788782694.3925693 | source=vosk | rms=571 | updated_at=1788782694.3668177
- [2026-09-07 20:04:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782694.616027 | source=vosk | rms=753 | updated_at=1788782694.616027
- [2026-09-07 20:04:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782694.8661187 | source=vosk | rms=827 | updated_at=1788782694.8661187
- [2026-09-07 20:04:55] operator / voice_transcript_final / voice: he actually has i think doctor
  meta: kind=final | timestamp=1788782695.1617699 | source=final | rms=827 | updated_at=1788782694.8661187
- [2026-09-07 20:04:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782695.2599404 | source=vosk | rms=558 | updated_at=1788782695.2599404
- [2026-09-07 20:04:57] operator / voice_transcript_partial / voice: cheers
  meta: kind=partial | timestamp=1788782697.1336367 | source=vosk | rms=417 | updated_at=1788782697.1196184
- [2026-09-07 20:04:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782697.3664205 | source=vosk | rms=435 | updated_at=1788782697.3664205
- [2026-09-07 20:04:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782697.616463 | source=vosk | rms=435 | updated_at=1788782697.3664205
- [2026-09-07 20:04:57] operator / voice_transcript_final / voice: cheers
  meta: kind=final | timestamp=1788782697.8452244 | source=final | rms=435 | updated_at=1788782697.3664205
- [2026-09-07 20:04:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782697.877842 | source=vosk | rms=435 | updated_at=1788782697.3664205
- [2026-09-07 20:05:00] operator / voice_transcript_partial / voice: my
  meta: kind=partial | timestamp=1788782700.1362696 | source=vosk | rms=599 | updated_at=1788782699.871929
- [2026-09-07 20:05:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782700.3663106 | source=vosk | rms=417 | updated_at=1788782700.3663106
- [2026-09-07 20:05:00] operator / voice_transcript_partial / voice: my child
  meta: kind=partial | timestamp=1788782700.385446 | source=vosk | rms=417 | updated_at=1788782700.3663106
- [2026-09-07 20:05:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782700.6167426 | source=vosk | rms=417 | updated_at=1788782700.3663106
- [2026-09-07 20:05:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782700.8664246 | source=vosk | rms=498 | updated_at=1788782700.8664246
- [2026-09-07 20:05:00] operator / voice_transcript_partial / voice: trying to
  meta: kind=partial | timestamp=1788782700.901684 | source=vosk | rms=498 | updated_at=1788782700.8664246
- [2026-09-07 20:05:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782701.3669617 | source=vosk | rms=596 | updated_at=1788782701.3669617
- [2026-09-07 20:05:01] operator / voice_transcript_partial / voice: my child protection
  meta: kind=partial | timestamp=1788782701.3944547 | source=vosk | rms=596 | updated_at=1788782701.3669617
- [2026-09-07 20:05:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782701.6169925 | source=vosk | rms=472 | updated_at=1788782701.6169925
- [2026-09-07 20:05:01] operator / voice_transcript_final / voice: my child protection
  meta: kind=final | timestamp=1788782701.9238496 | source=final | rms=472 | updated_at=1788782701.6169925
- [2026-09-07 20:05:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782702.0337412 | source=vosk | rms=644 | updated_at=1788782702.0337412
- [2026-09-07 20:05:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782702.6167984 | source=vosk | rms=644 | updated_at=1788782702.0337412
- [2026-09-07 20:05:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782702.8667862 | source=vosk | rms=644 | updated_at=1788782702.0337412
- [2026-09-07 20:05:03] operator / voice_transcript_partial / voice: the scope of
  meta: kind=partial | timestamp=1788782703.7101972 | source=vosk | rms=763 | updated_at=1788782703.1162112
- [2026-09-07 20:05:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782703.8660603 | source=vosk | rms=763 | updated_at=1788782703.1162112
- [2026-09-07 20:05:03] operator / voice_transcript_partial / voice: disco
  meta: kind=partial | timestamp=1788782703.920385 | source=vosk | rms=763 | updated_at=1788782703.1162112
- [2026-09-07 20:05:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782704.1164317 | source=vosk | rms=763 | updated_at=1788782703.1162112
- [2026-09-07 20:05:04] operator / voice_transcript_partial / voice: fiscal and monetary
  meta: kind=partial | timestamp=1788782704.1895046 | source=vosk | rms=763 | updated_at=1788782703.1162112
- [2026-09-07 20:05:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782704.3677073 | source=vosk | rms=653 | updated_at=1788782704.3677073
- [2026-09-07 20:05:04] operator / voice_transcript_partial / voice: disco on
  meta: kind=partial | timestamp=1788782704.4116256 | source=vosk | rms=653 | updated_at=1788782704.3677073
- [2026-09-07 20:05:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782704.6215885 | source=vosk | rms=517 | updated_at=1788782704.6215885
- [2026-09-07 20:05:04] operator / voice_transcript_partial / voice: fiscal and monetary
  meta: kind=partial | timestamp=1788782704.6564417 | source=vosk | rms=517 | updated_at=1788782704.6215885
- [2026-09-07 20:05:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782704.8665292 | source=vosk | rms=433 | updated_at=1788782704.8665292
- [2026-09-07 20:05:04] operator / voice_transcript_partial / voice: to discover that
  meta: kind=partial | timestamp=1788782704.9035988 | source=vosk | rms=433 | updated_at=1788782704.8665292
- [2026-09-07 20:05:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782705.1216877 | source=vosk | rms=433 | updated_at=1788782704.8665292
- [2026-09-07 20:05:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782705.3669174 | source=vosk | rms=433 | updated_at=1788782704.8665292
- [2026-09-07 20:05:06] operator / voice_transcript_final / voice: discover on that
  meta: kind=final | timestamp=1788782706.3113925 | source=final | rms=433 | updated_at=1788782704.8665292
- [2026-09-07 20:05:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782706.4306257 | source=vosk | rms=433 | updated_at=1788782704.8665292
- [2026-09-07 20:05:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782706.4306257 | source=vosk | rms=433 | updated_at=1788782704.8665292
- [2026-09-07 20:05:07] operator / voice_transcript_partial / voice: exactly
  meta: kind=partial | timestamp=1788782707.13408 | source=vosk | rms=720 | updated_at=1788782707.1161737
- [2026-09-07 20:05:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782707.6167374 | source=vosk | rms=720 | updated_at=1788782707.1161737
- [2026-09-07 20:05:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782708.1166873 | source=vosk | rms=514 | updated_at=1788782708.1166873
- [2026-09-07 20:05:08] operator / voice_transcript_partial / voice: the exact same
  meta: kind=partial | timestamp=1788782708.144362 | source=vosk | rms=514 | updated_at=1788782708.1166873
- [2026-09-07 20:05:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782708.367041 | source=vosk | rms=514 | updated_at=1788782708.1166873
- [2026-09-07 20:05:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782708.8660815 | source=vosk | rms=514 | updated_at=1788782708.1166873
- [2026-09-07 20:05:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782709.1275468 | source=vosk | rms=514 | updated_at=1788782708.1166873
- [2026-09-07 20:05:09] operator / voice_transcript_partial / voice: the exact same thing
  meta: kind=partial | timestamp=1788782709.1909976 | source=vosk | rms=514 | updated_at=1788782708.1166873
- [2026-09-07 20:05:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782709.6176703 | source=vosk | rms=514 | updated_at=1788782708.1166873
- [2026-09-07 20:05:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782709.8670506 | source=vosk | rms=514 | updated_at=1788782708.1166873
- [2026-09-07 20:05:09] operator / voice_transcript_partial / voice: the exact same also
  meta: kind=partial | timestamp=1788782709.9063995 | source=vosk | rms=514 | updated_at=1788782708.1166873
- [2026-09-07 20:05:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782710.3696551 | source=vosk | rms=514 | updated_at=1788782708.1166873
- [2026-09-07 20:05:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782710.617033 | source=vosk | rms=514 | updated_at=1788782708.1166873
- [2026-09-07 20:05:10] operator / voice_transcript_partial / voice: the exact same also include
  meta: kind=partial | timestamp=1788782710.6919198 | source=vosk | rms=514 | updated_at=1788782708.1166873
- [2026-09-07 20:05:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782711.1165392 | source=vosk | rms=514 | updated_at=1788782708.1166873
- [2026-09-07 20:05:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782716.116379 | source=vosk | rms=514 | updated_at=1788782708.1166873
- [2026-09-07 20:05:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782716.3674598 | source=vosk | rms=514 | updated_at=1788782708.1166873
- [2026-09-07 20:05:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782716.616853 | source=vosk | rms=514 | updated_at=1788782708.1166873
- [2026-09-07 20:05:16] operator / voice_transcript_final / voice: the exact same the cute
  meta: kind=final | timestamp=1788782716.8730655 | source=final | rms=514 | updated_at=1788782708.1166873
- [2026-09-07 20:05:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782716.9807177 | source=vosk | rms=657 | updated_at=1788782716.9807177
- [2026-09-07 20:05:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782720.6166918 | source=vosk | rms=857 | updated_at=1788782720.1170866
- [2026-09-07 20:05:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782721.6231208 | source=vosk | rms=857 | updated_at=1788782720.1170866
- [2026-09-07 20:05:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782722.867139 | source=vosk | rms=418 | updated_at=1788782721.8672404
- [2026-09-07 20:05:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782723.1167135 | source=vosk | rms=418 | updated_at=1788782721.8672404
- [2026-09-07 20:05:23] operator / voice_transcript_final / voice: oh
  meta: kind=final | timestamp=1788782723.8229687 | source=final | rms=418 | updated_at=1788782723.616692
- [2026-09-07 20:05:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782723.866976 | source=vosk | rms=418 | updated_at=1788782723.616692
- [2026-09-07 20:05:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782727.8671749 | source=vosk | rms=439 | updated_at=1788782727.1170282
- [2026-09-07 20:05:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782730.1172628 | source=vosk | rms=439 | updated_at=1788782727.1170282
- [2026-09-07 20:05:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782730.6166093 | source=vosk | rms=439 | updated_at=1788782727.1170282
- [2026-09-07 20:05:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782731.6174428 | source=vosk | rms=439 | updated_at=1788782727.1170282
- [2026-09-07 20:05:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782734.3681936 | source=vosk | rms=368 | updated_at=1788782733.616616
- [2026-09-07 20:05:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782734.6170788 | source=vosk | rms=368 | updated_at=1788782733.616616
- [2026-09-07 20:05:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782736.1169388 | source=vosk | rms=351 | updated_at=1788782735.1175263
- [2026-09-07 20:05:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782736.388622 | source=vosk | rms=351 | updated_at=1788782735.1175263
- [2026-09-07 20:05:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782737.6174362 | source=vosk | rms=351 | updated_at=1788782735.1175263
- [2026-09-07 20:05:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782737.8676026 | source=vosk | rms=351 | updated_at=1788782735.1175263
- [2026-09-07 20:05:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782738.3684099 | source=vosk | rms=351 | updated_at=1788782735.1175263
- [2026-09-07 20:05:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782738.6174557 | source=vosk | rms=365 | updated_at=1788782738.6174557
- [2026-09-07 20:05:44] operator / voice_transcript_partial / voice: not
  meta: kind=partial | timestamp=1788782744.658684 | source=vosk | rms=622 | updated_at=1788782744.3676717
- [2026-09-07 20:05:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782744.8806982 | source=vosk | rms=482 | updated_at=1788782744.8806982
- [2026-09-07 20:05:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782745.1171618 | source=vosk | rms=520 | updated_at=1788782745.1171618
- [2026-09-07 20:05:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782745.3678894 | source=vosk | rms=520 | updated_at=1788782745.1171618
- [2026-09-07 20:05:45] operator / voice_transcript_final / voice: not properly
  meta: kind=final | timestamp=1788782745.6061778 | source=final | rms=520 | updated_at=1788782745.1171618
- [2026-09-07 20:05:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782745.637162 | source=vosk | rms=520 | updated_at=1788782745.1171618
- [2026-09-07 20:05:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782746.3676014 | source=vosk | rms=520 | updated_at=1788782745.1171618
- [2026-09-07 20:05:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782746.8674316 | source=vosk | rms=1202 | updated_at=1788782746.8674316
- [2026-09-07 20:05:52] operator / voice_transcript_partial / voice: i thought was
  meta: kind=partial | timestamp=1788782752.391618 | source=vosk | rms=374 | updated_at=1788782752.3674898
- [2026-09-07 20:05:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782752.6180053 | source=vosk | rms=391 | updated_at=1788782752.6180053
- [2026-09-07 20:05:57] operator / voice_transcript_final / voice: thought was
  meta: kind=final | timestamp=1788782757.0991867 | source=final | rms=428 | updated_at=1788782756.6174095
- [2026-09-07 20:05:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782758.0209515 | source=vosk | rms=428 | updated_at=1788782756.6174095
- [2026-09-07 20:05:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782758.0209515 | source=vosk | rms=428 | updated_at=1788782756.6174095
- [2026-09-07 20:05:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782758.7678878 | source=vosk | rms=428 | updated_at=1788782756.6174095
- [2026-09-07 20:05:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782759.0177834 | source=vosk | rms=428 | updated_at=1788782756.6174095
- [2026-09-07 20:06:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782761.0184984 | source=vosk | rms=554 | updated_at=1788782760.0182743
- [2026-09-07 20:06:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782762.0177581 | source=vosk | rms=554 | updated_at=1788782760.0182743
- [2026-09-07 20:06:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782762.5182228 | source=vosk | rms=554 | updated_at=1788782760.0182743
- [2026-09-07 20:06:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782763.01794 | source=vosk | rms=670 | updated_at=1788782763.01794
- [2026-09-07 20:06:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782766.2681897 | source=vosk | rms=385 | updated_at=1788782765.7679558
- [2026-09-07 20:06:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782766.7675574 | source=vosk | rms=445 | updated_at=1788782766.7675574
- [2026-09-07 20:06:07] operator / voice_transcript_final / voice: sweden
  meta: kind=final | timestamp=1788782767.45897 | source=final | rms=445 | updated_at=1788782766.7675574
- [2026-09-07 20:06:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782767.5181572 | source=vosk | rms=445 | updated_at=1788782766.7675574
- [2026-09-07 20:06:12] operator / voice_transcript_partial / voice: this
  meta: kind=partial | timestamp=1788782772.8377867 | source=vosk | rms=383 | updated_at=1788782772.7680228
- [2026-09-07 20:06:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782773.2686229 | source=vosk | rms=441 | updated_at=1788782773.2686229
- [2026-09-07 20:06:13] operator / voice_transcript_partial / voice: this was
  meta: kind=partial | timestamp=1788782773.3038948 | source=vosk | rms=441 | updated_at=1788782773.2686229
- [2026-09-07 20:06:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782773.5182805 | source=vosk | rms=441 | updated_at=1788782773.2686229
- [2026-09-07 20:06:13] operator / voice_transcript_partial / voice: this was an
  meta: kind=partial | timestamp=1788782773.574495 | source=vosk | rms=441 | updated_at=1788782773.2686229
- [2026-09-07 20:06:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782774.080394 | source=vosk | rms=441 | updated_at=1788782773.2686229
- [2026-09-07 20:06:14] operator / voice_transcript_partial / voice: this was
  meta: kind=partial | timestamp=1788782774.134368 | source=vosk | rms=441 | updated_at=1788782773.2686229
- [2026-09-07 20:06:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782774.7676368 | source=vosk | rms=441 | updated_at=1788782773.2686229
- [2026-09-07 20:06:14] operator / voice_transcript_final / voice: this was
  meta: kind=final | timestamp=1788782774.9731228 | source=final | rms=441 | updated_at=1788782773.2686229
- [2026-09-07 20:06:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782775.0180008 | source=vosk | rms=382 | updated_at=1788782775.0180008
- [2026-09-07 20:06:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782775.5496957 | source=vosk | rms=382 | updated_at=1788782775.0180008
- [2026-09-07 20:06:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782775.7693143 | source=vosk | rms=447 | updated_at=1788782775.7693143
- [2026-09-07 20:06:15] operator / voice_transcript_partial / voice: this
  meta: kind=partial | timestamp=1788782775.7806182 | source=vosk | rms=447 | updated_at=1788782775.7693143
- [2026-09-07 20:06:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782776.019303 | source=vosk | rms=447 | updated_at=1788782775.7693143
- [2026-09-07 20:06:16] operator / voice_transcript_partial / voice: this was
  meta: kind=partial | timestamp=1788782776.0380404 | source=vosk | rms=447 | updated_at=1788782775.7693143
- [2026-09-07 20:06:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782776.5203044 | source=vosk | rms=447 | updated_at=1788782775.7693143
- [2026-09-07 20:06:16] operator / voice_transcript_partial / voice: the school
  meta: kind=partial | timestamp=1788782776.5762587 | source=vosk | rms=447 | updated_at=1788782775.7693143
- [2026-09-07 20:06:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782777.0438964 | source=vosk | rms=447 | updated_at=1788782775.7693143
- [2026-09-07 20:06:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782777.5185025 | source=vosk | rms=504 | updated_at=1788782777.5185025
- [2026-09-07 20:06:17] operator / voice_transcript_partial / voice: this forces
  meta: kind=partial | timestamp=1788782777.551496 | source=vosk | rms=504 | updated_at=1788782777.5185025
- [2026-09-07 20:06:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782777.7681453 | source=vosk | rms=504 | updated_at=1788782777.5185025
- [2026-09-07 20:06:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782778.0370252 | source=vosk | rms=391 | updated_at=1788782778.0370252
- [2026-09-07 20:06:18] operator / voice_transcript_final / voice: this forces
  meta: kind=final | timestamp=1788782778.5073562 | source=final | rms=391 | updated_at=1788782778.0370252
- [2026-09-07 20:06:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782778.5463474 | source=vosk | rms=391 | updated_at=1788782778.0370252
- [2026-09-07 20:06:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782778.7693002 | source=vosk | rms=391 | updated_at=1788782778.0370252
- [2026-09-07 20:06:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782781.5186625 | source=vosk | rms=682 | updated_at=1788782780.5192363
- [2026-09-07 20:06:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782782.0213842 | source=vosk | rms=682 | updated_at=1788782780.5192363
- [2026-09-07 20:06:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782782.5195508 | source=vosk | rms=682 | updated_at=1788782780.5192363
- [2026-09-07 20:06:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782782.768833 | source=vosk | rms=682 | updated_at=1788782780.5192363
- [2026-09-07 20:06:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782783.7731225 | source=vosk | rms=682 | updated_at=1788782780.5192363
- [2026-09-07 20:06:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782784.0182424 | source=vosk | rms=376 | updated_at=1788782784.0182424
- [2026-09-07 20:06:26] operator / voice_transcript_final / voice: the truth
  meta: kind=final | timestamp=1788782786.738299 | source=final | rms=328 | updated_at=1788782786.5231302
- [2026-09-07 20:06:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782786.7698176 | source=vosk | rms=328 | updated_at=1788782786.5231302
- [2026-09-07 20:06:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782787.5197558 | source=vosk | rms=328 | updated_at=1788782786.5231302
- [2026-09-07 20:06:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782789.5214515 | source=vosk | rms=328 | updated_at=1788782786.5231302
- [2026-09-07 20:06:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782790.7724745 | source=vosk | rms=304 | updated_at=1788782790.268699
- [2026-09-07 20:06:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782791.268393 | source=vosk | rms=304 | updated_at=1788782790.268699
- [2026-09-07 20:06:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782792.0216017 | source=vosk | rms=304 | updated_at=1788782790.268699
- [2026-09-07 20:06:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782792.519029 | source=vosk | rms=355 | updated_at=1788782792.519029
- [2026-09-07 20:06:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782793.018969 | source=vosk | rms=355 | updated_at=1788782792.519029
- [2026-09-07 20:06:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782793.2690642 | source=vosk | rms=304 | updated_at=1788782793.2690642
- [2026-09-07 20:06:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782797.1294634 | source=vosk | rms=275 | updated_at=1788782796.6287045
- [2026-09-07 20:06:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782797.3788733 | source=vosk | rms=292 | updated_at=1788782797.3788733
- [2026-09-07 20:06:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782799.3784132 | source=vosk | rms=323 | updated_at=1788782798.128461
- [2026-09-07 20:06:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782799.6287072 | source=vosk | rms=410 | updated_at=1788782799.6287072
- [2026-09-07 20:06:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782800.1293921 | source=vosk | rms=410 | updated_at=1788782799.6287072
- [2026-09-07 20:06:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782801.6289823 | source=vosk | rms=410 | updated_at=1788782799.6287072
- [2026-09-07 20:06:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782802.1410367 | source=vosk | rms=410 | updated_at=1788782799.6287072
- [2026-09-07 20:06:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782802.3806667 | source=vosk | rms=410 | updated_at=1788782799.6287072
- [2026-09-07 20:06:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782803.3792737 | source=vosk | rms=1137 | updated_at=1788782802.878318
- [2026-09-07 20:06:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782805.129219 | source=vosk | rms=1137 | updated_at=1788782802.878318
- [2026-09-07 20:06:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782805.8795757 | source=vosk | rms=1137 | updated_at=1788782802.878318
- [2026-09-07 20:06:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782807.1487184 | source=vosk | rms=1079 | updated_at=1788782807.1487184
- [2026-09-07 20:06:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782807.6285381 | source=vosk | rms=1079 | updated_at=1788782807.1487184
- [2026-09-07 20:06:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782808.1296425 | source=vosk | rms=1079 | updated_at=1788782807.1487184
- [2026-09-07 20:06:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782815.644011 | source=vosk | rms=260 | updated_at=1788782814.6291637
- [2026-09-07 20:06:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782815.8801444 | source=vosk | rms=260 | updated_at=1788782814.6291637
- [2026-09-07 20:06:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782816.3789334 | source=vosk | rms=260 | updated_at=1788782814.6291637
- [2026-09-07 20:06:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782817.3794472 | source=vosk | rms=260 | updated_at=1788782814.6291637
- [2026-09-07 20:06:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782819.1292706 | source=vosk | rms=261 | updated_at=1788782818.3788927
- [2026-09-07 20:07:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782820.1291487 | source=vosk | rms=261 | updated_at=1788782818.3788927
- [2026-09-07 20:07:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782822.1294525 | source=vosk | rms=261 | updated_at=1788782818.3788927
- [2026-09-07 20:07:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782824.6291785 | source=vosk | rms=261 | updated_at=1788782818.3788927
- [2026-09-07 20:07:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782825.128975 | source=vosk | rms=261 | updated_at=1788782818.3788927
- [2026-09-07 20:07:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782825.8796608 | source=vosk | rms=779 | updated_at=1788782825.8796608
- [2026-09-07 20:07:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782828.6291611 | source=vosk | rms=296 | updated_at=1788782826.888003
- [2026-09-07 20:07:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782829.6299129 | source=vosk | rms=296 | updated_at=1788782826.888003
- [2026-09-07 20:07:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782830.1290987 | source=vosk | rms=296 | updated_at=1788782826.888003
- [2026-09-07 20:07:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782830.3800268 | source=vosk | rms=296 | updated_at=1788782826.888003
- [2026-09-07 20:07:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782831.3792548 | source=vosk | rms=445 | updated_at=1788782830.8797433
- [2026-09-07 20:07:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782832.879384 | source=vosk | rms=445 | updated_at=1788782830.8797433
- [2026-09-07 20:07:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782833.6299708 | source=vosk | rms=172 | updated_at=1788782833.1291869
- [2026-09-07 20:07:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782833.879869 | source=vosk | rms=219 | updated_at=1788782833.879869
- [2026-09-07 20:07:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782834.3791919 | source=vosk | rms=219 | updated_at=1788782833.879869
- [2026-09-07 20:07:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782835.629122 | source=vosk | rms=219 | updated_at=1788782833.879869
- [2026-09-07 20:07:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782836.8967986 | source=vosk | rms=219 | updated_at=1788782833.879869
- [2026-09-07 20:07:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782838.1294582 | source=vosk | rms=444 | updated_at=1788782838.1294582
- [2026-09-07 20:07:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782839.3792148 | source=vosk | rms=182 | updated_at=1788782838.630036
- [2026-09-07 20:07:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782840.6294634 | source=vosk | rms=1201 | updated_at=1788782840.6294634
- [2026-09-07 20:07:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782841.879869 | source=vosk | rms=788 | updated_at=1788782841.3792613
- [2026-09-07 20:07:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782842.3798673 | source=vosk | rms=788 | updated_at=1788782841.3792613
- [2026-09-07 20:07:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782842.8798592 | source=vosk | rms=788 | updated_at=1788782841.3792613
- [2026-09-07 20:07:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782843.6290908 | source=vosk | rms=788 | updated_at=1788782841.3792613
- [2026-09-07 20:07:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782845.1332548 | source=vosk | rms=270 | updated_at=1788782843.8805964
- [2026-09-07 20:07:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782845.4181604 | source=vosk | rms=270 | updated_at=1788782843.8805964
- [2026-09-07 20:07:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782847.1303828 | source=vosk | rms=277 | updated_at=1788782846.6303446
- [2026-09-07 20:07:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782847.630947 | source=vosk | rms=867 | updated_at=1788782847.6299484
- [2026-09-07 20:07:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782849.380157 | source=vosk | rms=210 | updated_at=1788782848.8800564
- [2026-09-07 20:07:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782850.8799474 | source=vosk | rms=210 | updated_at=1788782848.8800564
- [2026-09-07 20:07:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782858.1315525 | source=vosk | rms=266 | updated_at=1788782857.1304767
- [2026-09-07 20:07:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782858.3802536 | source=vosk | rms=266 | updated_at=1788782857.1304767
- [2026-09-07 20:07:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782858.8797228 | source=vosk | rms=266 | updated_at=1788782857.1304767
- [2026-09-07 20:07:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782859.3799608 | source=vosk | rms=266 | updated_at=1788782857.1304767
- [2026-09-07 20:07:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782859.8806112 | source=vosk | rms=266 | updated_at=1788782857.1304767
- [2026-09-07 20:07:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782860.3802972 | source=vosk | rms=266 | updated_at=1788782857.1304767
- [2026-09-07 20:07:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782860.8801925 | source=vosk | rms=266 | updated_at=1788782857.1304767
- [2026-09-07 20:07:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782861.1310668 | source=vosk | rms=266 | updated_at=1788782857.1304767
- [2026-09-07 20:07:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782861.6652467 | source=vosk | rms=266 | updated_at=1788782857.1304767
- [2026-09-07 20:07:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782862.1298692 | source=vosk | rms=319 | updated_at=1788782862.1298692
- [2026-09-07 20:07:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782862.8798773 | source=vosk | rms=319 | updated_at=1788782862.1298692
- [2026-09-07 20:07:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782863.6302748 | source=vosk | rms=319 | updated_at=1788782862.1298692
- [2026-09-07 20:07:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782864.1302226 | source=vosk | rms=319 | updated_at=1788782862.1298692
- [2026-09-07 20:07:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782864.6308107 | source=vosk | rms=319 | updated_at=1788782862.1298692
- [2026-09-07 20:07:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782865.130229 | source=vosk | rms=319 | updated_at=1788782862.1298692
- [2026-09-07 20:07:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782865.6304479 | source=vosk | rms=223 | updated_at=1788782865.6304479
- [2026-09-07 20:07:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782867.131848 | source=vosk | rms=221 | updated_at=1788782866.6309972
- [2026-09-07 20:07:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782867.6343138 | source=vosk | rms=230 | updated_at=1788782867.6343138
- [2026-09-07 20:07:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782868.881551 | source=vosk | rms=481 | updated_at=1788782868.380524
- [2026-09-07 20:07:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782869.1312993 | source=vosk | rms=481 | updated_at=1788782868.380524
- [2026-09-07 20:07:50] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1788782870.4660785 | source=vosk | rms=427 | updated_at=1788782869.631534
- [2026-09-07 20:07:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782870.630721 | source=vosk | rms=288 | updated_at=1788782870.630721
- [2026-09-07 20:07:50] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1788782870.9553444 | source=final | rms=288 | updated_at=1788782870.630721
- [2026-09-07 20:07:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782871.0115619 | source=vosk | rms=288 | updated_at=1788782870.630721
- [2026-09-07 20:07:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782877.136418 | source=vosk | rms=367 | updated_at=1788782876.3803961
- [2026-09-07 20:07:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782877.380806 | source=vosk | rms=367 | updated_at=1788782876.3803961
- [2026-09-07 20:07:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782879.881238 | source=vosk | rms=269 | updated_at=1788782878.3809676
- [2026-09-07 20:08:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782880.631995 | source=vosk | rms=269 | updated_at=1788782878.3809676
- [2026-09-07 20:08:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782881.8803136 | source=vosk | rms=269 | updated_at=1788782878.3809676
- [2026-09-07 20:08:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782882.131962 | source=vosk | rms=332 | updated_at=1788782882.131962
- [2026-09-07 20:08:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782882.8819747 | source=vosk | rms=332 | updated_at=1788782882.131962
- [2026-09-07 20:08:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782883.1308424 | source=vosk | rms=332 | updated_at=1788782882.131962
- [2026-09-07 20:08:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782884.6303885 | source=vosk | rms=332 | updated_at=1788782882.131962
- [2026-09-07 20:08:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782884.9338465 | source=vosk | rms=197 | updated_at=1788782884.9338465
- [2026-09-07 20:08:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782887.380601 | source=vosk | rms=298 | updated_at=1788782886.3804493
- [2026-09-07 20:08:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782887.8811436 | source=vosk | rms=298 | updated_at=1788782886.3804493
- [2026-09-07 20:08:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782888.8808255 | source=vosk | rms=166 | updated_at=1788782888.1322997
- [2026-09-07 20:08:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782889.1313057 | source=vosk | rms=185 | updated_at=1788782889.1313057
- [2026-09-07 20:08:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782890.8807786 | source=vosk | rms=434 | updated_at=1788782890.3812513
- [2026-09-07 20:08:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782891.1380625 | source=vosk | rms=181 | updated_at=1788782891.1380625
- [2026-09-07 20:08:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782891.6330378 | source=vosk | rms=181 | updated_at=1788782891.1380625
- [2026-09-07 20:08:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782891.8821306 | source=vosk | rms=210 | updated_at=1788782891.8821306
- [2026-09-07 20:08:13] operator / voice_transcript_partial / voice: hello can
  meta: kind=partial | timestamp=1788782893.906187 | source=vosk | rms=508 | updated_at=1788782893.3911722
- [2026-09-07 20:08:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782894.3915193 | source=vosk | rms=508 | updated_at=1788782893.3911722
- [2026-09-07 20:08:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782894.6472487 | source=vosk | rms=508 | updated_at=1788782893.3911722
- [2026-09-07 20:08:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782894.8908322 | source=vosk | rms=508 | updated_at=1788782893.3911722
- [2026-09-07 20:08:15] operator / voice_transcript_final / voice: hello kyle
  meta: kind=final | timestamp=1788782895.1751676 | source=final | rms=508 | updated_at=1788782893.3911722
- [2026-09-07 20:08:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782895.4970562 | source=vosk | rms=508 | updated_at=1788782893.3911722
- [2026-09-07 20:08:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782895.4970562 | source=vosk | rms=508 | updated_at=1788782893.3911722
- [2026-09-07 20:08:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782896.8961833 | source=vosk | rms=508 | updated_at=1788782893.3911722
- [2026-09-07 20:08:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782897.1421692 | source=vosk | rms=408 | updated_at=1788782897.140665
- [2026-09-07 20:08:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782899.1610768 | source=vosk | rms=272 | updated_at=1788782898.6610892
- [2026-09-07 20:08:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782899.4123561 | source=vosk | rms=272 | updated_at=1788782898.6610892
- [2026-09-07 20:08:20] operator / voice_transcript_partial / voice: hello current
  meta: kind=partial | timestamp=1788782900.080543 | source=vosk | rms=246 | updated_at=1788782899.6614444
- [2026-09-07 20:08:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782900.411417 | source=vosk | rms=511 | updated_at=1788782900.411417
- [2026-09-07 20:08:20] operator / voice_transcript_partial / voice: hello current all my
  meta: kind=partial | timestamp=1788782900.5379732 | source=vosk | rms=511 | updated_at=1788782900.411417
- [2026-09-07 20:08:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782900.6614952 | source=vosk | rms=912 | updated_at=1788782900.6614952
- [2026-09-07 20:08:20] operator / voice_transcript_partial / voice: hello current all longer
  meta: kind=partial | timestamp=1788782900.8558102 | source=vosk | rms=912 | updated_at=1788782900.6614952
- [2026-09-07 20:08:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782901.41243 | source=vosk | rms=1204 | updated_at=1788782900.965381
- [2026-09-07 20:08:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782901.9187279 | source=vosk | rms=1204 | updated_at=1788782900.965381
- [2026-09-07 20:08:22] operator / voice_transcript_partial / voice: hello current all about
  meta: kind=partial | timestamp=1788782902.040462 | source=vosk | rms=1204 | updated_at=1788782900.965381
- [2026-09-07 20:08:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782902.160825 | source=vosk | rms=979 | updated_at=1788782902.160825
- [2026-09-07 20:08:22] operator / voice_transcript_partial / voice: hello current obama obama
  meta: kind=partial | timestamp=1788782902.2582796 | source=vosk | rms=979 | updated_at=1788782902.160825
- [2026-09-07 20:08:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782902.4261131 | source=vosk | rms=1201 | updated_at=1788782902.4261131
- [2026-09-07 20:08:22] operator / voice_transcript_partial / voice: hello current obama obama hello
  meta: kind=partial | timestamp=1788782902.5301428 | source=vosk | rms=1201 | updated_at=1788782902.4261131
- [2026-09-07 20:08:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782902.6714115 | source=vosk | rms=455 | updated_at=1788782902.6714115
- [2026-09-07 20:08:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782902.9217267 | source=vosk | rms=455 | updated_at=1788782902.6714115
- [2026-09-07 20:08:23] operator / voice_transcript_partial / voice: hello current obama obama hello so
  meta: kind=partial | timestamp=1788782903.0606585 | source=vosk | rms=455 | updated_at=1788782902.6714115
- [2026-09-07 20:08:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782903.1723905 | source=vosk | rms=216 | updated_at=1788782903.1723905
- [2026-09-07 20:08:23] operator / voice_transcript_partial / voice: hello current obama obama hello so unless
  meta: kind=partial | timestamp=1788782903.2478852 | source=vosk | rms=216 | updated_at=1788782903.1723905
- [2026-09-07 20:08:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782903.4214926 | source=vosk | rms=1207 | updated_at=1788782903.4214926
- [2026-09-07 20:08:23] operator / voice_transcript_partial / voice: hello current obama obama hello solace or
  meta: kind=partial | timestamp=1788782903.4746203 | source=vosk | rms=1207 | updated_at=1788782903.4214926
- [2026-09-07 20:08:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782903.6719222 | source=vosk | rms=438 | updated_at=1788782903.6719222
- [2026-09-07 20:08:23] operator / voice_transcript_partial / voice: hello current obama obama had those are less likely
  meta: kind=partial | timestamp=1788782903.7407506 | source=vosk | rms=438 | updated_at=1788782903.6719222
- [2026-09-07 20:08:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782903.9216008 | source=vosk | rms=1126 | updated_at=1788782903.9216008
- [2026-09-07 20:08:24] operator / voice_transcript_partial / voice: hello current obama obama had those are less likely to
  meta: kind=partial | timestamp=1788782904.0084639 | source=vosk | rms=1126 | updated_at=1788782903.9216008
- [2026-09-07 20:08:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782904.1727674 | source=vosk | rms=1202 | updated_at=1788782904.172263
- [2026-09-07 20:08:24] operator / voice_transcript_partial / voice: hello current obama obama hello so unless they did
  meta: kind=partial | timestamp=1788782904.2923582 | source=vosk | rms=1202 | updated_at=1788782904.172263
- [2026-09-07 20:08:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782904.4709346 | source=vosk | rms=798 | updated_at=1788782904.4709346
- [2026-09-07 20:08:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782904.6717405 | source=vosk | rms=798 | updated_at=1788782904.4709346
- [2026-09-07 20:08:24] operator / voice_transcript_partial / voice: hello current obama obama hello so unless they did not
  meta: kind=partial | timestamp=1788782904.7604508 | source=vosk | rms=798 | updated_at=1788782904.4709346
- [2026-09-07 20:08:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782905.1878748 | source=vosk | rms=798 | updated_at=1788782904.4709346
- [2026-09-07 20:08:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782905.4220402 | source=vosk | rms=225 | updated_at=1788782905.4220402
- [2026-09-07 20:08:25] operator / voice_transcript_partial / voice: hello current obama obama had those or less not more
  meta: kind=partial | timestamp=1788782905.460667 | source=vosk | rms=225 | updated_at=1788782905.4220402
- [2026-09-07 20:08:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782905.9222 | source=vosk | rms=225 | updated_at=1788782905.4220402
- [2026-09-07 20:08:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782906.4217763 | source=vosk | rms=573 | updated_at=1788782906.4217763
- [2026-09-07 20:08:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782906.6757123 | source=vosk | rms=1051 | updated_at=1788782906.6757123
- [2026-09-07 20:08:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782906.9210277 | source=vosk | rms=567 | updated_at=1788782906.9210277
- [2026-09-07 20:08:26] operator / voice_transcript_partial / voice: hello current obama obama had those are less likely to normal type
  meta: kind=partial | timestamp=1788782906.9890645 | source=vosk | rms=567 | updated_at=1788782906.9210277
- [2026-09-07 20:08:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782907.1711729 | source=vosk | rms=1002 | updated_at=1788782907.1711729
- [2026-09-07 20:08:27] operator / voice_transcript_partial / voice: hello current obama obama had those or less not more a part
  meta: kind=partial | timestamp=1788782907.2423627 | source=vosk | rms=1002 | updated_at=1788782907.1711729
- [2026-09-07 20:08:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782907.8351161 | source=vosk | rms=1002 | updated_at=1788782907.1711729
- [2026-09-07 20:08:27] operator / voice_transcript_partial / voice: hello current obama obama had those or less not more a boss who
  meta: kind=partial | timestamp=1788782907.9368732 | source=vosk | rms=1002 | updated_at=1788782907.1711729
- [2026-09-07 20:08:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782908.3319194 | source=vosk | rms=1002 | updated_at=1788782907.1711729
- [2026-09-07 20:08:28] operator / voice_transcript_partial / voice: hello current obama obama had those or less not more a boss who aren't
  meta: kind=partial | timestamp=1788782908.3850918 | source=vosk | rms=1002 | updated_at=1788782907.1711729
- [2026-09-07 20:08:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782908.5830936 | source=vosk | rms=421 | updated_at=1788782908.5830936
- [2026-09-07 20:08:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782908.8318946 | source=vosk | rms=421 | updated_at=1788782908.5830936
- [2026-09-07 20:08:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782909.0873694 | source=vosk | rms=459 | updated_at=1788782909.0873694
- [2026-09-07 20:08:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782909.3313391 | source=vosk | rms=459 | updated_at=1788782909.0873694
- [2026-09-07 20:08:29] operator / voice_transcript_final / voice: hello current obama obama had hello so less not more a boss who aren t
  meta: kind=final | timestamp=1788782909.633622 | source=final | rms=459 | updated_at=1788782909.0873694
- [2026-09-07 20:08:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782909.9190965 | source=vosk | rms=459 | updated_at=1788782909.0873694
- [2026-09-07 20:08:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782914.6040125 | source=vosk | rms=933 | updated_at=1788782914.6040125
- [2026-09-07 20:08:34] operator / voice_transcript_partial / voice: report
  meta: kind=partial | timestamp=1788782914.9214537 | source=vosk | rms=1202 | updated_at=1788782914.831765
- [2026-09-07 20:08:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782915.0927706 | source=vosk | rms=1202 | updated_at=1788782915.0927706
- [2026-09-07 20:08:35] operator / voice_transcript_partial / voice: report and
  meta: kind=partial | timestamp=1788782915.1526108 | source=vosk | rms=1202 | updated_at=1788782915.0927706
- [2026-09-07 20:08:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782915.3318443 | source=vosk | rms=1083 | updated_at=1788782915.3318443
- [2026-09-07 20:08:35] operator / voice_transcript_partial / voice: lamont
  meta: kind=partial | timestamp=1788782915.3798497 | source=vosk | rms=1083 | updated_at=1788782915.3318443
- [2026-09-07 20:08:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782915.6298535 | source=vosk | rms=1052 | updated_at=1788782915.6288533
- [2026-09-07 20:08:35] operator / voice_transcript_partial / voice: lamont have any
  meta: kind=partial | timestamp=1788782915.6946356 | source=vosk | rms=1052 | updated_at=1788782915.6288533
- [2026-09-07 20:08:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782915.8311825 | source=vosk | rms=1204 | updated_at=1788782915.8311825
- [2026-09-07 20:08:35] operator / voice_transcript_partial / voice: lamar depending on
  meta: kind=partial | timestamp=1788782915.8846347 | source=vosk | rms=1204 | updated_at=1788782915.8311825
- [2026-09-07 20:08:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782916.081412 | source=vosk | rms=1204 | updated_at=1788782916.081412
- [2026-09-07 20:08:36] operator / voice_transcript_partial / voice: lamont of anyone that the
  meta: kind=partial | timestamp=1788782916.1327639 | source=vosk | rms=1204 | updated_at=1788782916.081412
- [2026-09-07 20:08:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782916.332907 | source=vosk | rms=889 | updated_at=1788782916.332907
- [2026-09-07 20:08:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782916.5955095 | source=vosk | rms=889 | updated_at=1788782916.332907
- [2026-09-07 20:08:36] operator / voice_transcript_partial / voice: lamont of anyone that the know and i'm
  meta: kind=partial | timestamp=1788782916.656812 | source=vosk | rms=889 | updated_at=1788782916.332907
- [2026-09-07 20:08:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782917.0820413 | source=vosk | rms=889 | updated_at=1788782916.332907
- [2026-09-07 20:08:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782918.3319333 | source=vosk | rms=889 | updated_at=1788782916.332907
- [2026-09-07 20:08:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782918.8314242 | source=vosk | rms=889 | updated_at=1788782916.332907
- [2026-09-07 20:08:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782919.3328106 | source=vosk | rms=889 | updated_at=1788782916.332907
- [2026-09-07 20:08:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782920.5820076 | source=vosk | rms=889 | updated_at=1788782916.332907
- [2026-09-07 20:08:40] operator / voice_transcript_final / voice: to lamont of one of the neuron
  meta: kind=final | timestamp=1788782920.9306076 | source=final | rms=889 | updated_at=1788782916.332907
- [2026-09-07 20:08:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782921.0367675 | source=vosk | rms=889 | updated_at=1788782916.332907
- [2026-09-07 20:08:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782921.5818725 | source=vosk | rms=889 | updated_at=1788782916.332907
- [2026-09-07 20:08:43] operator / voice_transcript_partial / voice: i still
  meta: kind=partial | timestamp=1788782923.3679757 | source=vosk | rms=414 | updated_at=1788782923.3316252
- [2026-09-07 20:08:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782923.8322392 | source=vosk | rms=414 | updated_at=1788782923.3316252
- [2026-09-07 20:08:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782927.0862503 | source=vosk | rms=414 | updated_at=1788782923.3316252
- [2026-09-07 20:08:47] operator / voice_transcript_partial / voice: i love
  meta: kind=partial | timestamp=1788782927.1480367 | source=vosk | rms=414 | updated_at=1788782923.3316252
- [2026-09-07 20:08:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782927.6493146 | source=vosk | rms=414 | updated_at=1788782923.3316252
- [2026-09-07 20:08:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782931.332271 | source=vosk | rms=414 | updated_at=1788782923.3316252
- [2026-09-07 20:08:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782931.5943754 | source=vosk | rms=616 | updated_at=1788782931.5943754
- [2026-09-07 20:08:51] operator / voice_transcript_partial / voice: i still have enough to not have
  meta: kind=partial | timestamp=1788782931.659919 | source=vosk | rms=616 | updated_at=1788782931.5943754
- [2026-09-07 20:08:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782931.8323305 | source=vosk | rms=424 | updated_at=1788782931.8323305
- [2026-09-07 20:08:51] operator / voice_transcript_partial / voice: i love the most of the
  meta: kind=partial | timestamp=1788782931.919689 | source=vosk | rms=424 | updated_at=1788782931.8323305
- [2026-09-07 20:08:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782932.6181831 | source=vosk | rms=424 | updated_at=1788782931.8323305
- [2026-09-07 20:08:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782933.8321805 | source=vosk | rms=357 | updated_at=1788782933.8321805
- [2026-09-07 20:08:53] operator / voice_transcript_partial / voice: i love the most of the thousand
  meta: kind=partial | timestamp=1788782933.8500142 | source=vosk | rms=357 | updated_at=1788782933.8321805
- [2026-09-07 20:08:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782934.126453 | source=vosk | rms=413 | updated_at=1788782934.126453
- [2026-09-07 20:08:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782934.3330324 | source=vosk | rms=413 | updated_at=1788782934.126453
- [2026-09-07 20:08:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782934.831919 | source=vosk | rms=413 | updated_at=1788782934.126453
- [2026-09-07 20:08:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782936.3386018 | source=vosk | rms=413 | updated_at=1788782934.126453
- [2026-09-07 20:08:56] operator / voice_transcript_final / voice: i still have enough to of the thousand a month
  meta: kind=final | timestamp=1788782936.7597964 | source=final | rms=413 | updated_at=1788782934.126453
- [2026-09-07 20:08:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782936.9058747 | source=vosk | rms=413 | updated_at=1788782934.126453
- [2026-09-07 20:08:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782936.906382 | source=vosk | rms=413 | updated_at=1788782934.126453
- [2026-09-07 20:08:58] operator / voice_transcript_partial / voice: look at the
  meta: kind=partial | timestamp=1788782938.146237 | source=vosk | rms=333 | updated_at=1788782937.583063
- [2026-09-07 20:08:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782938.3324788 | source=vosk | rms=333 | updated_at=1788782937.583063
- [2026-09-07 20:08:58] operator / voice_transcript_partial / voice: wouldn't that
  meta: kind=partial | timestamp=1788782938.4063237 | source=vosk | rms=333 | updated_at=1788782937.583063
- [2026-09-07 20:08:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782938.8318093 | source=vosk | rms=279 | updated_at=1788782938.8318093
- [2026-09-07 20:08:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782939.3319614 | source=vosk | rms=279 | updated_at=1788782938.8318093
- [2026-09-07 20:08:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782939.5826542 | source=vosk | rms=443 | updated_at=1788782939.5826542
- [2026-09-07 20:09:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782940.0825863 | source=vosk | rms=443 | updated_at=1788782939.5826542
- [2026-09-07 20:09:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782940.332481 | source=vosk | rms=443 | updated_at=1788782939.5826542
- [2026-09-07 20:09:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782940.8321161 | source=vosk | rms=443 | updated_at=1788782939.5826542
- [2026-09-07 20:09:01] operator / voice_transcript_final / voice: than that
  meta: kind=final | timestamp=1788782941.026067 | source=final | rms=443 | updated_at=1788782939.5826542
- [2026-09-07 20:09:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782941.3318741 | source=vosk | rms=443 | updated_at=1788782939.5826542
- [2026-09-07 20:09:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782943.582294 | source=vosk | rms=443 | updated_at=1788782939.5826542
- [2026-09-07 20:09:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782944.8372025 | source=vosk | rms=443 | updated_at=1788782939.5826542
- [2026-09-07 20:09:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782945.083098 | source=vosk | rms=443 | updated_at=1788782939.5826542
- [2026-09-07 20:09:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782946.4167316 | source=vosk | rms=197 | updated_at=1788782945.8585262
- [2026-09-07 20:09:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782947.082197 | source=vosk | rms=197 | updated_at=1788782945.8585262
- [2026-09-07 20:09:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782947.5855353 | source=vosk | rms=197 | updated_at=1788782945.8585262
- [2026-09-07 20:09:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782947.832722 | source=vosk | rms=197 | updated_at=1788782945.8585262
- [2026-09-07 20:09:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782948.342177 | source=vosk | rms=197 | updated_at=1788782945.8585262
- [2026-09-07 20:09:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782948.833547 | source=vosk | rms=197 | updated_at=1788782945.8585262
- [2026-09-07 20:09:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782950.0817232 | source=vosk | rms=679 | updated_at=1788782949.5823305
- [2026-09-07 20:09:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782950.3328626 | source=vosk | rms=679 | updated_at=1788782949.5823305
- [2026-09-07 20:09:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782950.8321695 | source=vosk | rms=679 | updated_at=1788782949.5823305
- [2026-09-07 20:09:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782951.102818 | source=vosk | rms=679 | updated_at=1788782949.5823305
- [2026-09-07 20:09:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782951.8327963 | source=vosk | rms=679 | updated_at=1788782949.5823305
- [2026-09-07 20:09:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788782952.5837452 | source=vosk | rms=217 | updated_at=1788782952.5837452
- [2026-09-07 20:09:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788782953.3321502 | source=vosk | rms=217 | updated_at=1788782952.5837452

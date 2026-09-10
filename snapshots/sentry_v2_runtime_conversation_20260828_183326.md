# SMART SENTRY V5.0.0 Runtime Conversation Export

- Generated: 2026-08-28 18:33:26
- Entries: 213
- Roles: {'assistant': 4, 'system': 146, 'operator': 63}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 146, 'spoken_confirmation': 2, 'voice_transcript_partial': 53, 'voice_transcript_final': 8, 'voice_command': 2}
- Channels: {'text': 2, 'voice': 211}
- Latest operator request: much to the lowdown on camera
- Latest assistant message: I could not open that tab.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-08-28 18:31:14] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-08-28 18:31:14] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-08-28 18:31:19] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787913079.1975043 | source=vosk
- [2026-08-28 18:31:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913079.7145617 | source=vosk | rms=1200 | updated_at=1787913079.7145617
- [2026-08-28 18:31:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913091.180796 | source=vosk | rms=570 | updated_at=1787913090.6818159 | frequency_hz=140.4
- [2026-08-28 18:31:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913091.4313416 | source=vosk | rms=1205 | updated_at=1787913091.4313416 | frequency_hz=140.4
- [2026-08-28 18:31:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913092.9309795 | source=vosk | rms=126 | updated_at=1787913092.4861286 | frequency_hz=140.4
- [2026-08-28 18:31:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913093.4313788 | source=vosk | rms=1201 | updated_at=1787913093.4313788 | frequency_hz=140.4
- [2026-08-28 18:31:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913099.6823454 | source=vosk | rms=1202 | updated_at=1787913098.9315014 | frequency_hz=214.5
- [2026-08-28 18:31:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913100.1806145 | source=vosk | rms=1200 | updated_at=1787913100.1806145 | frequency_hz=203.8
- [2026-08-28 18:31:40] assistant / spoken_confirmation / voice: Smart Sentry is ready.
  meta: interrupt=True | assistant_output=False | spoken=True
- [2026-08-28 18:31:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913100.6810284 | source=vosk | rms=1200 | updated_at=1787913100.1806145 | frequency_hz=203.8
- [2026-08-28 18:31:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913103.1819108 | source=vosk | rms=1206 | updated_at=1787913103.1819108 | frequency_hz=203.8
- [2026-08-28 18:31:45] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1787913105.0035794 | source=vosk | rms=1062 | updated_at=1787913104.9314344 | frequency_hz=250.8
- [2026-08-28 18:31:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913105.1817503 | source=vosk | rms=1036 | updated_at=1787913105.1817503 | frequency_hz=250.8
- [2026-08-28 18:31:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913105.431718 | source=vosk | rms=1036 | updated_at=1787913105.1817503 | frequency_hz=250.8
- [2026-08-28 18:31:45] operator / voice_transcript_partial / voice: smart century is
  meta: kind=partial | timestamp=1787913105.4943001 | source=vosk | rms=1036 | updated_at=1787913105.1817503 | frequency_hz=250.8
- [2026-08-28 18:31:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913105.9316356 | source=vosk | rms=1036 | updated_at=1787913105.1817503 | frequency_hz=250.8
- [2026-08-28 18:31:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913111.5195272 | source=vosk | rms=1036 | updated_at=1787913105.1817503 | frequency_hz=250.8
- [2026-08-28 18:31:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913111.7403686 | source=vosk | rms=1009 | updated_at=1787913111.6827276 | frequency_hz=92.0
- [2026-08-28 18:31:51] operator / voice_transcript_partial / voice: smart century is ready
  meta: kind=partial | timestamp=1787913111.7403686 | source=vosk | rms=1009 | updated_at=1787913111.6827276 | frequency_hz=92.0
- [2026-08-28 18:31:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913111.9317183 | source=vosk | rms=1009 | updated_at=1787913111.6827276 | frequency_hz=92.0
- [2026-08-28 18:31:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913112.1825435 | source=vosk | rms=1009 | updated_at=1787913111.6827276 | frequency_hz=92.0
- [2026-08-28 18:31:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913112.4320347 | source=vosk | rms=1007 | updated_at=1787913112.4320347 | frequency_hz=179.5
- [2026-08-28 18:31:52] operator / voice_transcript_final / voice: smart sentry is ready
  meta: kind=final | timestamp=1787913112.8447342 | source=final | rms=1007 | updated_at=1787913112.4320347 | frequency_hz=179.5
- [2026-08-28 18:31:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913113.053795 | source=vosk | rms=1007 | updated_at=1787913112.4320347 | frequency_hz=179.5
- [2026-08-28 18:31:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913113.053795 | source=vosk | rms=1007 | updated_at=1787913112.4320347 | frequency_hz=179.5
- [2026-08-28 18:31:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913113.68116 | source=vosk | rms=1007 | updated_at=1787913112.4320347 | frequency_hz=179.5
- [2026-08-28 18:31:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913116.1815171 | source=vosk | rms=1201 | updated_at=1787913116.1815171 | frequency_hz=272.0
- [2026-08-28 18:31:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913119.181125 | source=vosk | rms=836 | updated_at=1787913118.4318948 | frequency_hz=187.0
- [2026-08-28 18:31:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913119.4315834 | source=vosk | rms=1201 | updated_at=1787913119.4315834 | frequency_hz=248.9
- [2026-08-28 18:32:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913120.7575767 | source=vosk | rms=1200 | updated_at=1787913119.6815808 | frequency_hz=248.9
- [2026-08-28 18:32:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913121.0031257 | source=vosk | rms=1200 | updated_at=1787913121.0031257 | frequency_hz=230.4
- [2026-08-28 18:32:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913122.7523346 | source=vosk | rms=813 | updated_at=1787913122.2517552 | frequency_hz=249.4
- [2026-08-28 18:32:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913124.2522202 | source=vosk | rms=798 | updated_at=1787913124.2522202 | frequency_hz=192.0
- [2026-08-28 18:32:06] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1787913126.2988746 | source=vosk | rms=1201 | updated_at=1787913126.2521436 | frequency_hz=207.4
- [2026-08-28 18:32:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913126.751905 | source=vosk | rms=5616 | updated_at=1787913126.751905 | frequency_hz=241.9
- [2026-08-28 18:32:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913127.0024402 | source=vosk | rms=5471 | updated_at=1787913127.0024402 | frequency_hz=241.9
- [2026-08-28 18:32:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913127.2520664 | source=vosk | rms=4021 | updated_at=1787913127.2520664 | frequency_hz=241.9
- [2026-08-28 18:32:07] operator / voice_transcript_partial / voice: alien run the
  meta: kind=partial | timestamp=1787913127.277391 | source=vosk | rms=4021 | updated_at=1787913127.2520664 | frequency_hz=241.9
- [2026-08-28 18:32:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913127.5024314 | source=vosk | rms=3810 | updated_at=1787913127.5024314 | frequency_hz=241.9
- [2026-08-28 18:32:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913127.7522995 | source=vosk | rms=4795 | updated_at=1787913127.7522995 | frequency_hz=241.9
- [2026-08-28 18:32:07] operator / voice_transcript_partial / voice: alien run the smart
  meta: kind=partial | timestamp=1787913127.766899 | source=vosk | rms=4795 | updated_at=1787913127.7522995 | frequency_hz=241.9
- [2026-08-28 18:32:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913128.003049 | source=vosk | rms=2019 | updated_at=1787913128.003049 | frequency_hz=239.8
- [2026-08-28 18:32:08] operator / voice_transcript_partial / voice: alien run the smart century
  meta: kind=partial | timestamp=1787913128.0216308 | source=vosk | rms=2019 | updated_at=1787913128.003049 | frequency_hz=239.8
- [2026-08-28 18:32:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913128.2516923 | source=vosk | rms=1200 | updated_at=1787913128.2516923 | frequency_hz=185.3
- [2026-08-28 18:32:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913128.5015736 | source=vosk | rms=1201 | updated_at=1787913128.5015736 | frequency_hz=208.6
- [2026-08-28 18:32:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913128.751478 | source=vosk | rms=1200 | updated_at=1787913128.751478 | frequency_hz=197.2
- [2026-08-28 18:32:08] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1787913128.7645032 | source=final | rms=1200 | updated_at=1787913128.751478 | frequency_hz=197.2
- [2026-08-28 18:32:08] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787913128.7988615 | source=state | rms=1200 | updated_at=1787913128.751478 | frequency_hz=197.2
- [2026-08-28 18:32:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913128.7988615 | source=state | rms=1200 | updated_at=1787913128.751478 | frequency_hz=197.2
- [2026-08-28 18:32:31] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-08-28 18:32:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913129.0018299 | source=vosk | rms=886 | updated_at=1787913129.0018299 | frequency_hz=194.0
- [2026-08-28 18:32:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913130.7522707 | source=vosk | rms=928 | updated_at=1787913129.2518387 | frequency_hz=264.0
- [2026-08-28 18:32:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913135.2524865 | source=vosk | rms=928 | updated_at=1787913129.2518387 | frequency_hz=264.0
- [2026-08-28 18:32:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913136.751954 | source=vosk | rms=1204 | updated_at=1787913136.2528856 | frequency_hz=264.0
- [2026-08-28 18:32:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913138.5017169 | source=vosk | rms=1204 | updated_at=1787913136.2528856 | frequency_hz=264.0
- [2026-08-28 18:32:19] operator / voice_transcript_partial / voice: to my
  meta: kind=partial | timestamp=1787913139.3136268 | source=vosk | rms=965 | updated_at=1787913139.2522366 | frequency_hz=264.0
- [2026-08-28 18:32:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913139.7523677 | source=vosk | rms=1203 | updated_at=1787913139.7523677 | frequency_hz=304.6
- [2026-08-28 18:32:19] operator / voice_transcript_partial / voice: tomorrow saturday
  meta: kind=partial | timestamp=1787913139.8037522 | source=vosk | rms=1203 | updated_at=1787913139.7523677 | frequency_hz=304.6
- [2026-08-28 18:32:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913140.002101 | source=vosk | rms=1200 | updated_at=1787913140.002101 | frequency_hz=304.6
- [2026-08-28 18:32:20] operator / voice_transcript_partial / voice: the mindset
  meta: kind=partial | timestamp=1787913140.0479274 | source=vosk | rms=1200 | updated_at=1787913140.002101 | frequency_hz=304.6
- [2026-08-28 18:32:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913140.2522936 | source=vosk | rms=1201 | updated_at=1787913140.2522936 | frequency_hz=304.6
- [2026-08-28 18:32:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913140.5025566 | source=vosk | rms=3772 | updated_at=1787913140.5025566 | frequency_hz=304.6
- [2026-08-28 18:32:20] operator / voice_transcript_partial / voice: to mark such a
  meta: kind=partial | timestamp=1787913140.5431423 | source=vosk | rms=3772 | updated_at=1787913140.5025566 | frequency_hz=304.6
- [2026-08-28 18:32:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913140.7524517 | source=vosk | rms=2839 | updated_at=1787913140.7524517 | frequency_hz=304.6
- [2026-08-28 18:32:20] operator / voice_transcript_partial / voice: the mindset
  meta: kind=partial | timestamp=1787913140.837831 | source=vosk | rms=2839 | updated_at=1787913140.7524517 | frequency_hz=304.6
- [2026-08-28 18:32:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913141.002755 | source=vosk | rms=1007 | updated_at=1787913141.002755 | frequency_hz=304.6
- [2026-08-28 18:32:21] operator / voice_transcript_partial / voice: the marks an alien
  meta: kind=partial | timestamp=1787913141.0261583 | source=vosk | rms=1007 | updated_at=1787913141.002755 | frequency_hz=304.6
- [2026-08-28 18:32:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913141.2524467 | source=vosk | rms=973 | updated_at=1787913141.2524467 | frequency_hz=304.6
- [2026-08-28 18:32:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913141.5029836 | source=vosk | rms=973 | updated_at=1787913141.2524467 | frequency_hz=304.6
- [2026-08-28 18:32:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913141.752802 | source=vosk | rms=973 | updated_at=1787913141.2524467 | frequency_hz=304.6
- [2026-08-28 18:32:21] operator / voice_transcript_partial / voice: the mindset iliad by such
  meta: kind=partial | timestamp=1787913141.797038 | source=vosk | rms=973 | updated_at=1787913141.2524467 | frequency_hz=304.6
- [2026-08-28 18:32:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913142.0051928 | source=vosk | rms=973 | updated_at=1787913141.2524467 | frequency_hz=304.6
- [2026-08-28 18:32:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913142.2524211 | source=vosk | rms=1201 | updated_at=1787913142.2524211 | frequency_hz=311.4
- [2026-08-28 18:32:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913142.5034292 | source=vosk | rms=1201 | updated_at=1787913142.5034292 | frequency_hz=311.4
- [2026-08-28 18:32:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913142.7532513 | source=vosk | rms=1189 | updated_at=1787913142.7527487 | frequency_hz=311.4
- [2026-08-28 18:32:23] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787913143.472411 | source=state | rms=1189 | updated_at=1787913142.7527487 | frequency_hz=311.4
- [2026-08-28 18:32:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913144.0310752 | source=state | rms=1189 | updated_at=1787913142.7527487 | frequency_hz=311.4
- [2026-08-28 18:32:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913144.0310752 | source=vosk | rms=1203 | updated_at=1787913144.0310752 | frequency_hz=311.4
- [2026-08-28 18:32:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913146.751922 | source=vosk | rms=1202 | updated_at=1787913146.2531128 | frequency_hz=348.0
- [2026-08-28 18:32:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913148.2521443 | source=vosk | rms=1202 | updated_at=1787913146.2531128 | frequency_hz=348.0
- [2026-08-28 18:32:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913148.7526457 | source=vosk | rms=1202 | updated_at=1787913146.2531128 | frequency_hz=348.0
- [2026-08-28 18:32:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913149.0036323 | source=vosk | rms=1202 | updated_at=1787913146.2531128 | frequency_hz=348.0
- [2026-08-28 18:32:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913149.5019724 | source=vosk | rms=1202 | updated_at=1787913146.2531128 | frequency_hz=348.0
- [2026-08-28 18:32:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913150.252068 | source=vosk | rms=1202 | updated_at=1787913146.2531128 | frequency_hz=348.0
- [2026-08-28 18:32:30] operator / voice_transcript_partial / voice: as far as
  meta: kind=partial | timestamp=1787913150.826577 | source=vosk | rms=1202 | updated_at=1787913146.2531128 | frequency_hz=348.0
- [2026-08-28 18:32:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913151.2553558 | source=vosk | rms=1202 | updated_at=1787913146.2531128 | frequency_hz=348.0
- [2026-08-28 18:32:32] operator / voice_transcript_final / voice: as far as
  meta: kind=final | timestamp=1787913152.6590738 | source=final | rms=1202 | updated_at=1787913146.2531128 | frequency_hz=348.0
- [2026-08-28 18:32:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913154.753785 | source=vosk | rms=1202 | updated_at=1787913154.753785 | frequency_hz=348.0
- [2026-08-28 18:32:34] operator / voice_transcript_partial / voice: as far as other
  meta: kind=partial | timestamp=1787913154.8272595 | source=vosk | rms=1202 | updated_at=1787913154.753785 | frequency_hz=348.0
- [2026-08-28 18:32:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913155.2524745 | source=vosk | rms=1203 | updated_at=1787913155.2524745 | frequency_hz=348.0
- [2026-08-28 18:32:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913155.5066075 | source=vosk | rms=1203 | updated_at=1787913155.2524745 | frequency_hz=348.0
- [2026-08-28 18:32:36] operator / voice_transcript_final / voice: as far as other best
  meta: kind=final | timestamp=1787913156.2320793 | source=final | rms=1203 | updated_at=1787913155.2524745 | frequency_hz=348.0
- [2026-08-28 18:32:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913156.385957 | source=vosk | rms=1203 | updated_at=1787913155.2524745 | frequency_hz=348.0
- [2026-08-28 18:32:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913156.385957 | source=vosk | rms=962 | updated_at=1787913156.385957 | frequency_hz=348.0
- [2026-08-28 18:32:36] operator / voice_transcript_partial / voice: please
  meta: kind=partial | timestamp=1787913156.5772312 | source=vosk | rms=1056 | updated_at=1787913156.539998 | frequency_hz=348.0
- [2026-08-28 18:32:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913156.7531402 | source=vosk | rms=1204 | updated_at=1787913156.7531402 | frequency_hz=348.0
- [2026-08-28 18:32:36] operator / voice_transcript_partial / voice: please try to
  meta: kind=partial | timestamp=1787913156.7970762 | source=vosk | rms=1204 | updated_at=1787913156.7531402 | frequency_hz=348.0
- [2026-08-28 18:32:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913157.0425646 | source=vosk | rms=2861 | updated_at=1787913157.0425646 | frequency_hz=348.0
- [2026-08-28 18:32:37] operator / voice_transcript_partial / voice: please try again
  meta: kind=partial | timestamp=1787913157.0848534 | source=vosk | rms=2861 | updated_at=1787913157.0425646 | frequency_hz=348.0
- [2026-08-28 18:32:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913157.252456 | source=vosk | rms=4929 | updated_at=1787913157.252456 | frequency_hz=348.0
- [2026-08-28 18:32:37] operator / voice_transcript_partial / voice: please try to get
  meta: kind=partial | timestamp=1787913157.2710574 | source=vosk | rms=4929 | updated_at=1787913157.252456 | frequency_hz=348.0
- [2026-08-28 18:32:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913157.5404928 | source=vosk | rms=4812 | updated_at=1787913157.5404928 | frequency_hz=348.0
- [2026-08-28 18:32:37] operator / voice_transcript_partial / voice: please try to open
  meta: kind=partial | timestamp=1787913157.5761702 | source=vosk | rms=4812 | updated_at=1787913157.5404928 | frequency_hz=348.0
- [2026-08-28 18:32:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913157.75872 | source=vosk | rms=2953 | updated_at=1787913157.75872 | frequency_hz=348.0
- [2026-08-28 18:32:37] operator / voice_transcript_partial / voice: please try to open the
  meta: kind=partial | timestamp=1787913157.7964468 | source=vosk | rms=2953 | updated_at=1787913157.75872 | frequency_hz=348.0
- [2026-08-28 18:32:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913158.0440826 | source=vosk | rms=1310 | updated_at=1787913158.0440826 | frequency_hz=300.4
- [2026-08-28 18:32:38] operator / voice_transcript_partial / voice: please try to open the camera
  meta: kind=partial | timestamp=1787913158.0748441 | source=vosk | rms=1310 | updated_at=1787913158.0440826 | frequency_hz=300.4
- [2026-08-28 18:32:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913158.2530909 | source=vosk | rms=1200 | updated_at=1787913158.2530909 | frequency_hz=300.4
- [2026-08-28 18:32:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913158.761176 | source=vosk | rms=1200 | updated_at=1787913158.2530909 | frequency_hz=300.4
- [2026-08-28 18:32:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913159.0182307 | source=vosk | rms=1200 | updated_at=1787913159.0182307 | frequency_hz=300.4
- [2026-08-28 18:32:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913159.2530751 | source=vosk | rms=1202 | updated_at=1787913159.2530751 | frequency_hz=300.4
- [2026-08-28 18:32:39] operator / voice_transcript_final / voice: open camera
  meta: kind=final | timestamp=1787913159.2659621 | source=final | rms=1202 | updated_at=1787913159.2530751 | frequency_hz=300.4
- [2026-08-28 18:32:39] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787913159.3037288 | source=state | rms=1202 | updated_at=1787913159.2530751 | frequency_hz=300.4
- [2026-08-28 18:32:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913159.3037288 | source=state | rms=1202 | updated_at=1787913159.2530751 | frequency_hz=300.4
- [2026-08-28 18:32:39] operator / voice_command / voice: open camera
  meta: normalized=True
- [2026-08-28 18:32:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913159.5039797 | source=vosk | rms=1205 | updated_at=1787913159.5039797 | frequency_hz=300.4
- [2026-08-28 18:32:39] assistant / spoken_confirmation / voice: I could not open that tab.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-08-28 18:32:40] operator / voice_transcript_partial / voice: such reports
  meta: kind=partial | timestamp=1787913160.2797885 | source=vosk | rms=1205 | updated_at=1787913159.5039797 | frequency_hz=300.4
- [2026-08-28 18:32:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913160.5027885 | source=vosk | rms=1205 | updated_at=1787913159.5039797 | frequency_hz=300.4
- [2026-08-28 18:32:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913160.753101 | source=vosk | rms=1205 | updated_at=1787913159.5039797 | frequency_hz=300.4
- [2026-08-28 18:32:40] operator / voice_transcript_partial / voice: such reports are
  meta: kind=partial | timestamp=1787913160.772332 | source=vosk | rms=1205 | updated_at=1787913159.5039797 | frequency_hz=300.4
- [2026-08-28 18:32:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913161.010933 | source=vosk | rms=1205 | updated_at=1787913159.5039797 | frequency_hz=300.4
- [2026-08-28 18:32:41] operator / voice_transcript_partial / voice: such reports are connected on
  meta: kind=partial | timestamp=1787913161.0483186 | source=vosk | rms=1205 | updated_at=1787913159.5039797 | frequency_hz=300.4
- [2026-08-28 18:32:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913161.2522035 | source=vosk | rms=1153 | updated_at=1787913161.2522035 | frequency_hz=300.4
- [2026-08-28 18:32:41] operator / voice_transcript_partial / voice: such reports are connected on the
  meta: kind=partial | timestamp=1787913161.270762 | source=vosk | rms=1153 | updated_at=1787913161.2522035 | frequency_hz=300.4
- [2026-08-28 18:32:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913161.5049183 | source=vosk | rms=1203 | updated_at=1787913161.5049183 | frequency_hz=300.4
- [2026-08-28 18:32:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913161.7528012 | source=vosk | rms=1202 | updated_at=1787913161.7528012 | frequency_hz=300.4
- [2026-08-28 18:32:41] operator / voice_transcript_partial / voice: such reports are connected on this
  meta: kind=partial | timestamp=1787913161.793164 | source=vosk | rms=1202 | updated_at=1787913161.7528012 | frequency_hz=300.4
- [2026-08-28 18:32:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913162.013979 | source=vosk | rms=1205 | updated_at=1787913162.013979 | frequency_hz=300.4
- [2026-08-28 18:32:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913162.2528477 | source=vosk | rms=1204 | updated_at=1787913162.2528477 | frequency_hz=300.4
- [2026-08-28 18:32:43] operator / voice_transcript_final / voice: such reports are connect on the seal
  meta: kind=final | timestamp=1787913163.579548 | source=final | rms=1204 | updated_at=1787913162.2528477 | frequency_hz=300.4
- [2026-08-28 18:32:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913164.7370136 | source=vosk | rms=1204 | updated_at=1787913162.2528477 | frequency_hz=300.4
- [2026-08-28 18:32:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913164.7370136 | source=vosk | rms=1201 | updated_at=1787913164.7370136 | frequency_hz=300.4
- [2026-08-28 18:32:45] operator / voice_transcript_partial / voice: another
  meta: kind=partial | timestamp=1787913165.5538445 | source=vosk | rms=1121 | updated_at=1787913165.5153382 | frequency_hz=300.4
- [2026-08-28 18:32:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913165.7331371 | source=vosk | rms=1121 | updated_at=1787913165.5153382 | frequency_hz=300.4
- [2026-08-28 18:32:45] operator / voice_transcript_partial / voice: another question
  meta: kind=partial | timestamp=1787913165.7462497 | source=vosk | rms=1121 | updated_at=1787913165.5153382 | frequency_hz=300.4
- [2026-08-28 18:32:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913166.2332196 | source=vosk | rms=897 | updated_at=1787913166.2332196 | frequency_hz=300.4
- [2026-08-28 18:32:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913166.5280743 | source=vosk | rms=1193 | updated_at=1787913166.5280743 | frequency_hz=300.4
- [2026-08-28 18:32:46] operator / voice_transcript_partial / voice: another question or
  meta: kind=partial | timestamp=1787913166.5528338 | source=vosk | rms=1193 | updated_at=1787913166.5280743 | frequency_hz=300.4
- [2026-08-28 18:32:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913166.7331932 | source=vosk | rms=1193 | updated_at=1787913166.5280743 | frequency_hz=300.4
- [2026-08-28 18:32:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913167.2215772 | source=vosk | rms=1193 | updated_at=1787913166.5280743 | frequency_hz=300.4
- [2026-08-28 18:32:47] operator / voice_transcript_partial / voice: another question work in another
  meta: kind=partial | timestamp=1787913167.3421404 | source=vosk | rms=1193 | updated_at=1787913166.5280743 | frequency_hz=300.4
- [2026-08-28 18:32:47] operator / voice_transcript_partial / voice: another question work in another country
  meta: kind=partial | timestamp=1787913167.3741868 | source=vosk | rms=1193 | updated_at=1787913166.5280743 | frequency_hz=300.4
- [2026-08-28 18:32:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913167.5392413 | source=vosk | rms=1193 | updated_at=1787913166.5280743 | frequency_hz=300.4
- [2026-08-28 18:32:47] operator / voice_transcript_partial / voice: another question work in another country and
  meta: kind=partial | timestamp=1787913167.66214 | source=vosk | rms=1193 | updated_at=1787913166.5280743 | frequency_hz=300.4
- [2026-08-28 18:32:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913168.2327569 | source=vosk | rms=904 | updated_at=1787913168.2327569 | frequency_hz=300.4
- [2026-08-28 18:32:48] operator / voice_transcript_partial / voice: another question work in another country and around
  meta: kind=partial | timestamp=1787913168.2725112 | source=vosk | rms=904 | updated_at=1787913168.2327569 | frequency_hz=300.4
- [2026-08-28 18:32:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913168.5252767 | source=vosk | rms=904 | updated_at=1787913168.2327569 | frequency_hz=300.4
- [2026-08-28 18:32:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913168.7329898 | source=vosk | rms=904 | updated_at=1787913168.2327569 | frequency_hz=300.4
- [2026-08-28 18:32:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913169.0114958 | source=vosk | rms=1158 | updated_at=1787913169.0114958 | frequency_hz=300.4
- [2026-08-28 18:32:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913169.2328906 | source=vosk | rms=1158 | updated_at=1787913169.0114958 | frequency_hz=300.4
- [2026-08-28 18:32:49] operator / voice_transcript_partial / voice: another question work in another country and around smart
  meta: kind=partial | timestamp=1787913169.2462986 | source=vosk | rms=1158 | updated_at=1787913169.0114958 | frequency_hz=300.4
- [2026-08-28 18:32:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913169.7332733 | source=vosk | rms=1158 | updated_at=1787913169.0114958 | frequency_hz=300.4
- [2026-08-28 18:32:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913170.004052 | source=vosk | rms=1158 | updated_at=1787913169.0114958 | frequency_hz=300.4
- [2026-08-28 18:32:50] operator / voice_transcript_partial / voice: another question work in another country and around smart center
  meta: kind=partial | timestamp=1787913170.0427601 | source=vosk | rms=1158 | updated_at=1787913169.0114958 | frequency_hz=300.4
- [2026-08-28 18:32:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913170.2340677 | source=vosk | rms=1158 | updated_at=1787913169.0114958 | frequency_hz=300.4
- [2026-08-28 18:32:50] operator / voice_transcript_partial / voice: another question work in another country and around smart center it's actually
  meta: kind=partial | timestamp=1787913170.2690625 | source=vosk | rms=1158 | updated_at=1787913169.0114958 | frequency_hz=300.4
- [2026-08-28 18:32:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913170.73304 | source=vosk | rms=1158 | updated_at=1787913169.0114958 | frequency_hz=300.4
- [2026-08-28 18:32:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913170.9831243 | source=vosk | rms=1158 | updated_at=1787913169.0114958 | frequency_hz=300.4
- [2026-08-28 18:32:51] operator / voice_transcript_partial / voice: another question work in another country and around smart center it's actually necklace
  meta: kind=partial | timestamp=1787913171.0467188 | source=vosk | rms=1158 | updated_at=1787913169.0114958 | frequency_hz=300.4
- [2026-08-28 18:32:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913171.2325146 | source=vosk | rms=1201 | updated_at=1787913171.2325146 | frequency_hz=300.4
- [2026-08-28 18:32:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913171.4832318 | source=vosk | rms=1201 | updated_at=1787913171.2325146 | frequency_hz=300.4
- [2026-08-28 18:32:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913171.9831257 | source=vosk | rms=1129 | updated_at=1787913171.9831257 | frequency_hz=300.4
- [2026-08-28 18:32:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913172.2334437 | source=vosk | rms=1200 | updated_at=1787913172.2334437 | frequency_hz=300.4
- [2026-08-28 18:32:52] operator / voice_transcript_final / voice: another question work in another country and around smart center it s actually necklace
  meta: kind=final | timestamp=1787913172.6431549 | source=final | rms=1200 | updated_at=1787913172.2334437 | frequency_hz=300.4
- [2026-08-28 18:32:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913172.7517025 | source=vosk | rms=1200 | updated_at=1787913172.2334437 | frequency_hz=300.4
- [2026-08-28 18:32:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913172.7517025 | source=vosk | rms=1200 | updated_at=1787913172.7517025 | frequency_hz=300.4
- [2026-08-28 18:32:55] operator / voice_transcript_partial / voice: good
  meta: kind=partial | timestamp=1787913175.57218 | source=vosk | rms=2139 | updated_at=1787913175.4825807 | frequency_hz=300.4
- [2026-08-28 18:32:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913175.7327104 | source=vosk | rms=1200 | updated_at=1787913175.7327104 | frequency_hz=300.4
- [2026-08-28 18:32:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913177.2332613 | source=vosk | rms=1720 | updated_at=1787913176.4844384 | frequency_hz=300.4
- [2026-08-28 18:32:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913177.4832153 | source=vosk | rms=1720 | updated_at=1787913176.4844384 | frequency_hz=300.4
- [2026-08-28 18:32:57] operator / voice_transcript_partial / voice: much
  meta: kind=partial | timestamp=1787913177.80696 | source=vosk | rms=1720 | updated_at=1787913176.4844384 | frequency_hz=300.4
- [2026-08-28 18:32:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913178.2333143 | source=vosk | rms=1720 | updated_at=1787913176.4844384 | frequency_hz=300.4
- [2026-08-28 18:32:58] operator / voice_transcript_partial / voice: much to the
  meta: kind=partial | timestamp=1787913178.3487968 | source=vosk | rms=1720 | updated_at=1787913176.4844384 | frequency_hz=300.4
- [2026-08-28 18:32:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913178.4826427 | source=vosk | rms=985 | updated_at=1787913178.4826427 | frequency_hz=300.4
- [2026-08-28 18:32:58] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1787913178.573286 | source=vosk | rms=985 | updated_at=1787913178.4826427 | frequency_hz=300.4
- [2026-08-28 18:32:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913179.2335293 | source=vosk | rms=1061 | updated_at=1787913179.2335293 | frequency_hz=300.4
- [2026-08-28 18:32:59] operator / voice_transcript_partial / voice: much to the lowdown on
  meta: kind=partial | timestamp=1787913179.2674563 | source=vosk | rms=1061 | updated_at=1787913179.2335293 | frequency_hz=300.4
- [2026-08-28 18:32:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913179.4841027 | source=vosk | rms=1205 | updated_at=1787913179.4841027 | frequency_hz=300.4
- [2026-08-28 18:32:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913179.733414 | source=vosk | rms=1202 | updated_at=1787913179.733414 | frequency_hz=300.4
- [2026-08-28 18:32:59] operator / voice_transcript_partial / voice: much to the lowdown on camera
  meta: kind=partial | timestamp=1787913179.7722464 | source=vosk | rms=1202 | updated_at=1787913179.733414 | frequency_hz=300.4
- [2026-08-28 18:32:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913179.9834707 | source=vosk | rms=1202 | updated_at=1787913179.9834707 | frequency_hz=300.4
- [2026-08-28 18:33:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913180.2327554 | source=vosk | rms=1202 | updated_at=1787913180.2327554 | frequency_hz=300.4
- [2026-08-28 18:33:01] operator / voice_transcript_final / voice: much to the lowdown on camera
  meta: kind=final | timestamp=1787913181.0608413 | source=final | rms=1202 | updated_at=1787913180.2327554 | frequency_hz=300.4
- [2026-08-28 18:33:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913181.2087662 | source=vosk | rms=1202 | updated_at=1787913180.2327554 | frequency_hz=300.4
- [2026-08-28 18:33:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913181.2087662 | source=vosk | rms=1202 | updated_at=1787913180.2327554 | frequency_hz=300.4
- [2026-08-28 18:33:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913181.7337003 | source=vosk | rms=1202 | updated_at=1787913180.2327554 | frequency_hz=300.4
- [2026-08-28 18:33:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913185.2336462 | source=vosk | rms=1200 | updated_at=1787913185.2336462 | frequency_hz=300.4
- [2026-08-28 18:33:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913185.733436 | source=vosk | rms=1200 | updated_at=1787913185.2336462 | frequency_hz=300.4
- [2026-08-28 18:33:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913188.4844394 | source=vosk | rms=1200 | updated_at=1787913185.2336462 | frequency_hz=300.4
- [2026-08-28 18:33:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913189.232706 | source=vosk | rms=1200 | updated_at=1787913185.2336462 | frequency_hz=300.4
- [2026-08-28 18:33:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913190.232938 | source=vosk | rms=1200 | updated_at=1787913190.232938 | frequency_hz=300.4
- [2026-08-28 18:33:11] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1787913191.035475 | source=vosk | rms=1126 | updated_at=1787913190.9837084 | frequency_hz=300.4
- [2026-08-28 18:33:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913191.2338076 | source=vosk | rms=1200 | updated_at=1787913191.2338076 | frequency_hz=300.4
- [2026-08-28 18:33:11] operator / voice_transcript_partial / voice: better than
  meta: kind=partial | timestamp=1787913191.2917345 | source=vosk | rms=1200 | updated_at=1787913191.2338076 | frequency_hz=300.4
- [2026-08-28 18:33:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913191.484657 | source=vosk | rms=1200 | updated_at=1787913191.4836564 | frequency_hz=300.4
- [2026-08-28 18:33:13] operator / voice_transcript_partial / voice: and you're gonna make
  meta: kind=partial | timestamp=1787913193.0365589 | source=vosk | rms=1206 | updated_at=1787913192.140668 | frequency_hz=300.4
- [2026-08-28 18:33:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913193.233099 | source=vosk | rms=1206 | updated_at=1787913193.233099 | frequency_hz=300.4
- [2026-08-28 18:33:13] operator / voice_transcript_partial / voice: better than this guy making
  meta: kind=partial | timestamp=1787913193.2672381 | source=vosk | rms=1206 | updated_at=1787913193.233099 | frequency_hz=300.4
- [2026-08-28 18:33:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913193.7336512 | source=vosk | rms=1206 | updated_at=1787913193.233099 | frequency_hz=300.4
- [2026-08-28 18:33:13] operator / voice_transcript_partial / voice: better than this guy making a lot
  meta: kind=partial | timestamp=1787913193.7946248 | source=vosk | rms=1206 | updated_at=1787913193.233099 | frequency_hz=300.4
- [2026-08-28 18:33:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913194.233692 | source=vosk | rms=1206 | updated_at=1787913193.233099 | frequency_hz=300.4
- [2026-08-28 18:33:14] operator / voice_transcript_partial / voice: better than this guy making that allows a
  meta: kind=partial | timestamp=1787913194.2971551 | source=vosk | rms=1206 | updated_at=1787913193.233099 | frequency_hz=300.4
- [2026-08-28 18:33:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913194.4845638 | source=vosk | rms=1206 | updated_at=1787913193.233099 | frequency_hz=300.4
- [2026-08-28 18:33:14] operator / voice_transcript_partial / voice: better than this guy making a collapsing and
  meta: kind=partial | timestamp=1787913194.4975808 | source=vosk | rms=1206 | updated_at=1787913193.233099 | frequency_hz=300.4
- [2026-08-28 18:33:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913194.7335107 | source=vosk | rms=1054 | updated_at=1787913194.7335107 | frequency_hz=300.4
- [2026-08-28 18:33:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913195.2335374 | source=vosk | rms=1054 | updated_at=1787913194.7335107 | frequency_hz=300.4
- [2026-08-28 18:33:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913196.7335825 | source=vosk | rms=1200 | updated_at=1787913196.7335825 | frequency_hz=300.4
- [2026-08-28 18:33:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913196.9836564 | source=vosk | rms=1200 | updated_at=1787913196.7335825 | frequency_hz=300.4
- [2026-08-28 18:33:17] operator / voice_transcript_partial / voice: better than this guy making a collapsing and disconnected and
  meta: kind=partial | timestamp=1787913197.0107527 | source=vosk | rms=1200 | updated_at=1787913196.7335825 | frequency_hz=300.4
- [2026-08-28 18:33:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913197.4845917 | source=vosk | rms=1200 | updated_at=1787913196.7335825 | frequency_hz=300.4

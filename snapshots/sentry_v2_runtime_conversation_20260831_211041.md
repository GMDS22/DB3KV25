# SMART SENTRY V5.0.0 Runtime Conversation Export

- Generated: 2026-08-31 21:10:41
- Entries: 1492
- Roles: {'assistant': 3, 'system': 1353, 'operator': 136}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 1353, 'spoken_confirmation': 1, 'voice_transcript_partial': 105, 'voice_transcript_final': 31}
- Channels: {'text': 2, 'voice': 1490}
- Latest operator request: ha
- Latest assistant message: Smart Sentry is ready.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-08-31 20:41:09] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-08-31 20:41:09] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-08-31 20:41:12] system / voice_status / voice: listening
  meta: kind=status | timestamp=1788180072.8605475 | source=vosk
- [2026-08-31 20:41:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180074.5143132 | source=vosk | rms=397 | updated_at=1788180074.5143132 | frequency_hz=92.0
- [2026-08-31 20:41:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180075.0546598 | source=vosk | rms=397 | updated_at=1788180074.5143132 | frequency_hz=92.0
- [2026-08-31 20:41:49] assistant / spoken_confirmation / voice: Smart Sentry is ready.
  meta: interrupt=True | assistant_output=False | spoken=True
- [2026-08-31 20:41:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180088.512956 | source=vosk | rms=145 | updated_at=1788180088.512956 | frequency_hz=92.0
- [2026-08-31 20:41:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180089.0135813 | source=vosk | rms=145 | updated_at=1788180088.512956 | frequency_hz=92.0
- [2026-08-31 20:41:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180092.7629266 | source=vosk | rms=244 | updated_at=1788180092.7629266 | frequency_hz=92.0
- [2026-08-31 20:41:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180106.0131156 | source=vosk | rms=331 | updated_at=1788180105.5139132 | frequency_hz=92.0
- [2026-08-31 20:41:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180106.263735 | source=vosk | rms=181 | updated_at=1788180106.263735 | frequency_hz=92.0
- [2026-08-31 20:41:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180109.763261 | source=vosk | rms=245 | updated_at=1788180109.2849038 | frequency_hz=174.6
- [2026-08-31 20:41:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180110.0143638 | source=vosk | rms=131 | updated_at=1788180110.0143638 | frequency_hz=174.6
- [2026-08-31 20:41:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180111.0150423 | source=vosk | rms=315 | updated_at=1788180110.5141778 | frequency_hz=174.6
- [2026-08-31 20:41:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180111.785158 | source=vosk | rms=315 | updated_at=1788180110.5141778 | frequency_hz=174.6
- [2026-08-31 20:41:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180112.9520197 | source=vosk | rms=315 | updated_at=1788180110.5141778 | frequency_hz=174.6
- [2026-08-31 20:41:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180113.202304 | source=vosk | rms=1200 | updated_at=1788180113.202304 | frequency_hz=174.6
- [2026-08-31 20:41:55] operator / voice_transcript_partial / voice: close
  meta: kind=partial | timestamp=1788180115.1831696 | source=vosk | rms=1016 | updated_at=1788180115.1610186 | frequency_hz=174.6
- [2026-08-31 20:41:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180115.3717294 | source=vosk | rms=443 | updated_at=1788180115.3717294 | frequency_hz=174.6
- [2026-08-31 20:41:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180115.6288626 | source=vosk | rms=443 | updated_at=1788180115.3717294 | frequency_hz=174.6
- [2026-08-31 20:41:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180115.8717737 | source=vosk | rms=443 | updated_at=1788180115.3717294 | frequency_hz=174.6
- [2026-08-31 20:41:56] operator / voice_transcript_final / voice: close
  meta: kind=final | timestamp=1788180116.0812235 | source=final | rms=443 | updated_at=1788180115.3717294 | frequency_hz=174.6
- [2026-08-31 20:41:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180116.319569 | source=vosk | rms=443 | updated_at=1788180115.3717294 | frequency_hz=174.6
- [2026-08-31 20:41:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180116.319569 | source=vosk | rms=613 | updated_at=1788180116.319569 | frequency_hz=174.6
- [2026-08-31 20:41:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180117.8711395 | source=vosk | rms=1201 | updated_at=1788180117.373185 | frequency_hz=174.6
- [2026-08-31 20:41:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180118.371896 | source=vosk | rms=500 | updated_at=1788180118.371896 | frequency_hz=174.6
- [2026-08-31 20:42:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180123.1591575 | source=vosk | rms=401 | updated_at=1788180122.6243277 | frequency_hz=174.6
- [2026-08-31 20:42:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180123.3715634 | source=vosk | rms=401 | updated_at=1788180122.6243277 | frequency_hz=174.6
- [2026-08-31 20:42:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180124.6215177 | source=vosk | rms=480 | updated_at=1788180124.1221642 | frequency_hz=174.6
- [2026-08-31 20:42:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180126.3725371 | source=vosk | rms=693 | updated_at=1788180126.3725371 | frequency_hz=174.6
- [2026-08-31 20:42:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180126.8716862 | source=vosk | rms=693 | updated_at=1788180126.3725371 | frequency_hz=174.6
- [2026-08-31 20:42:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180127.3724315 | source=vosk | rms=693 | updated_at=1788180126.3725371 | frequency_hz=174.6
- [2026-08-31 20:42:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180128.3718793 | source=vosk | rms=689 | updated_at=1788180127.876302 | frequency_hz=174.6
- [2026-08-31 20:42:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180133.8723629 | source=vosk | rms=464 | updated_at=1788180133.8723629 | frequency_hz=174.6
- [2026-08-31 20:42:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180134.6221251 | source=vosk | rms=464 | updated_at=1788180133.8723629 | frequency_hz=174.6
- [2026-08-31 20:42:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180138.6221285 | source=vosk | rms=1201 | updated_at=1788180138.6221285 | frequency_hz=174.6
- [2026-08-31 20:42:19] operator / voice_transcript_partial / voice: hello
  meta: kind=partial | timestamp=1788180139.1518912 | source=vosk | rms=1200 | updated_at=1788180139.1220756 | frequency_hz=174.6
- [2026-08-31 20:42:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180139.3725345 | source=vosk | rms=408 | updated_at=1788180139.3725345 | frequency_hz=174.6
- [2026-08-31 20:42:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180139.8734932 | source=vosk | rms=408 | updated_at=1788180139.3725345 | frequency_hz=174.6
- [2026-08-31 20:42:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180140.3740528 | source=vosk | rms=408 | updated_at=1788180139.3725345 | frequency_hz=174.6
- [2026-08-31 20:42:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180149.8729024 | source=vosk | rms=122 | updated_at=1788180149.8729024 | frequency_hz=120.0
- [2026-08-31 20:42:29] operator / voice_transcript_partial / voice: hello kyle
  meta: kind=partial | timestamp=1788180149.8885114 | source=vosk | rms=122 | updated_at=1788180149.8729024 | frequency_hz=120.0
- [2026-08-31 20:42:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180150.3728716 | source=vosk | rms=122 | updated_at=1788180149.8729024 | frequency_hz=120.0
- [2026-08-31 20:42:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180152.8723397 | source=vosk | rms=122 | updated_at=1788180149.8729024 | frequency_hz=120.0
- [2026-08-31 20:42:33] operator / voice_transcript_final / voice: hello kyle
  meta: kind=final | timestamp=1788180153.0882585 | source=final | rms=122 | updated_at=1788180149.8729024 | frequency_hz=120.0
- [2026-08-31 20:42:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180153.3001788 | source=vosk | rms=122 | updated_at=1788180149.8729024 | frequency_hz=120.0
- [2026-08-31 20:42:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180153.3732224 | source=vosk | rms=658 | updated_at=1788180153.3732224 | frequency_hz=244.0
- [2026-08-31 20:42:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180153.8731844 | source=vosk | rms=658 | updated_at=1788180153.3732224 | frequency_hz=244.0
- [2026-08-31 20:42:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180155.8741262 | source=vosk | rms=790 | updated_at=1788180155.8741262 | frequency_hz=244.0
- [2026-08-31 20:42:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180156.3762035 | source=vosk | rms=790 | updated_at=1788180155.8741262 | frequency_hz=244.0
- [2026-08-31 20:42:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180156.876179 | source=vosk | rms=503 | updated_at=1788180156.876179 | frequency_hz=214.6
- [2026-08-31 20:42:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180158.6233525 | source=vosk | rms=279 | updated_at=1788180157.8727937 | frequency_hz=237.5
- [2026-08-31 20:42:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180159.622936 | source=vosk | rms=279 | updated_at=1788180157.8727937 | frequency_hz=237.5
- [2026-08-31 20:42:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180160.6229918 | source=vosk | rms=279 | updated_at=1788180157.8727937 | frequency_hz=237.5
- [2026-08-31 20:42:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180160.8728685 | source=vosk | rms=215 | updated_at=1788180160.8728685 | frequency_hz=237.5
- [2026-08-31 20:42:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180161.6233041 | source=vosk | rms=215 | updated_at=1788180160.8728685 | frequency_hz=237.5
- [2026-08-31 20:42:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180162.643141 | source=vosk | rms=215 | updated_at=1788180160.8728685 | frequency_hz=237.5
- [2026-08-31 20:42:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180163.123072 | source=vosk | rms=215 | updated_at=1788180160.8728685 | frequency_hz=237.5
- [2026-08-31 20:42:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180164.6238706 | source=vosk | rms=210 | updated_at=1788180164.6238706 | frequency_hz=278.0
- [2026-08-31 20:42:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180165.1227448 | source=vosk | rms=210 | updated_at=1788180164.6238706 | frequency_hz=278.0
- [2026-08-31 20:42:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180167.8728836 | source=vosk | rms=154 | updated_at=1788180167.8728836 | frequency_hz=278.0
- [2026-08-31 20:42:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180169.3908942 | source=vosk | rms=426 | updated_at=1788180168.8721254 | frequency_hz=278.0
- [2026-08-31 20:42:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180170.623278 | source=vosk | rms=426 | updated_at=1788180168.8721254 | frequency_hz=278.0
- [2026-08-31 20:42:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180171.122763 | source=vosk | rms=426 | updated_at=1788180168.8721254 | frequency_hz=278.0
- [2026-08-31 20:42:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180173.8731585 | source=vosk | rms=205 | updated_at=1788180173.8731585 | frequency_hz=278.0
- [2026-08-31 20:42:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180174.378065 | source=vosk | rms=205 | updated_at=1788180173.8731585 | frequency_hz=278.0
- [2026-08-31 20:42:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180176.123952 | source=vosk | rms=281 | updated_at=1788180176.1234477 | frequency_hz=150.0
- [2026-08-31 20:42:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180176.6511235 | source=vosk | rms=281 | updated_at=1788180176.1234477 | frequency_hz=150.0
- [2026-08-31 20:42:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180177.3732984 | source=vosk | rms=281 | updated_at=1788180176.1234477 | frequency_hz=150.0
- [2026-08-31 20:42:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180177.8727052 | source=vosk | rms=281 | updated_at=1788180176.1234477 | frequency_hz=150.0
- [2026-08-31 20:42:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180179.6234035 | source=vosk | rms=252 | updated_at=1788180179.6234035 | frequency_hz=150.0
- [2026-08-31 20:43:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180180.8731077 | source=vosk | rms=220 | updated_at=1788180180.3728232 | frequency_hz=131.1
- [2026-08-31 20:43:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180181.6231527 | source=vosk | rms=220 | updated_at=1788180180.3728232 | frequency_hz=131.1
- [2026-08-31 20:43:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180182.3728511 | source=vosk | rms=591 | updated_at=1788180181.8735752 | frequency_hz=364.0
- [2026-08-31 20:43:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180183.1313725 | source=vosk | rms=591 | updated_at=1788180181.8735752 | frequency_hz=364.0
- [2026-08-31 20:43:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180183.6225955 | source=vosk | rms=591 | updated_at=1788180181.8735752 | frequency_hz=364.0
- [2026-08-31 20:43:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180184.6552448 | source=vosk | rms=138 | updated_at=1788180184.6552448 | frequency_hz=364.0
- [2026-08-31 20:43:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180185.1456199 | source=vosk | rms=138 | updated_at=1788180184.6552448 | frequency_hz=364.0
- [2026-08-31 20:43:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180191.8744204 | source=vosk | rms=210 | updated_at=1788180191.8744204 | frequency_hz=364.0
- [2026-08-31 20:43:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180192.8733861 | source=vosk | rms=644 | updated_at=1788180192.373631 | frequency_hz=280.0
- [2026-08-31 20:43:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180196.8737752 | source=vosk | rms=216 | updated_at=1788180196.8737752 | frequency_hz=280.0
- [2026-08-31 20:43:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180198.1375148 | source=vosk | rms=132 | updated_at=1788180197.6614745 | frequency_hz=280.0
- [2026-08-31 20:43:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180199.373052 | source=vosk | rms=170 | updated_at=1788180199.373052 | frequency_hz=280.0
- [2026-08-31 20:43:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180200.1241193 | source=vosk | rms=170 | updated_at=1788180199.373052 | frequency_hz=280.0
- [2026-08-31 20:43:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180201.1267457 | source=vosk | rms=542 | updated_at=1788180201.1267457 | frequency_hz=280.0
- [2026-08-31 20:43:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180202.3735807 | source=vosk | rms=157 | updated_at=1788180201.873178 | frequency_hz=280.0
- [2026-08-31 20:43:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180204.62319 | source=vosk | rms=462 | updated_at=1788180204.62319 | frequency_hz=280.0
- [2026-08-31 20:43:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180205.3730364 | source=vosk | rms=142 | updated_at=1788180204.873617 | frequency_hz=280.0
- [2026-08-31 20:43:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180205.8745606 | source=vosk | rms=142 | updated_at=1788180204.873617 | frequency_hz=280.0
- [2026-08-31 20:43:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180206.8745728 | source=vosk | rms=337 | updated_at=1788180206.3731258 | frequency_hz=280.0
- [2026-08-31 20:43:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180207.123686 | source=vosk | rms=713 | updated_at=1788180207.123686 | frequency_hz=280.0
- [2026-08-31 20:43:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180208.3733158 | source=vosk | rms=713 | updated_at=1788180207.123686 | frequency_hz=280.0
- [2026-08-31 20:43:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180210.1236231 | source=vosk | rms=713 | updated_at=1788180207.123686 | frequency_hz=280.0
- [2026-08-31 20:43:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180211.1236274 | source=vosk | rms=349 | updated_at=1788180210.625004 | frequency_hz=280.0
- [2026-08-31 20:43:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180211.6233866 | source=vosk | rms=1200 | updated_at=1788180211.6233866 | frequency_hz=280.0
- [2026-08-31 20:43:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180214.8740964 | source=vosk | rms=1202 | updated_at=1788180214.3735912 | frequency_hz=280.0
- [2026-08-31 20:43:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180215.5822055 | source=vosk | rms=196 | updated_at=1788180215.5822055 | frequency_hz=280.0
- [2026-08-31 20:43:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180216.3741448 | source=vosk | rms=844 | updated_at=1788180215.8750036 | frequency_hz=277.2
- [2026-08-31 20:43:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180216.9051478 | source=vosk | rms=189 | updated_at=1788180216.9051478 | frequency_hz=277.2
- [2026-08-31 20:43:36] operator / voice_transcript_partial / voice: welcome back chino guard systems recognize
  meta: kind=partial | timestamp=1788180216.9138606 | source=vosk | rms=189 | updated_at=1788180216.9051478 | frequency_hz=277.2
- [2026-08-31 20:43:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180217.1234596 | source=vosk | rms=301 | updated_at=1788180217.1234596 | frequency_hz=277.2
- [2026-08-31 20:43:37] operator / voice_transcript_final / voice: welcome back chino guard systems recognize
  meta: kind=final | timestamp=1788180217.4341326 | source=final | rms=301 | updated_at=1788180217.1234596 | frequency_hz=277.2
- [2026-08-31 20:43:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180217.624123 | source=vosk | rms=301 | updated_at=1788180217.1234596 | frequency_hz=277.2
- [2026-08-31 20:43:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180217.874005 | source=vosk | rms=577 | updated_at=1788180217.874005 | frequency_hz=229.2
- [2026-08-31 20:43:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180218.3740194 | source=vosk | rms=577 | updated_at=1788180217.874005 | frequency_hz=229.2
- [2026-08-31 20:43:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180222.6240697 | source=vosk | rms=329 | updated_at=1788180222.6240697 | frequency_hz=229.2
- [2026-08-31 20:43:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180223.1236253 | source=vosk | rms=329 | updated_at=1788180222.6240697 | frequency_hz=229.2
- [2026-08-31 20:43:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180225.1411066 | source=vosk | rms=329 | updated_at=1788180222.6240697 | frequency_hz=229.2
- [2026-08-31 20:43:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180225.6236947 | source=vosk | rms=329 | updated_at=1788180222.6240697 | frequency_hz=229.2
- [2026-08-31 20:43:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180227.623477 | source=vosk | rms=329 | updated_at=1788180222.6240697 | frequency_hz=229.2
- [2026-08-31 20:43:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180228.123575 | source=vosk | rms=329 | updated_at=1788180222.6240697 | frequency_hz=229.2
- [2026-08-31 20:43:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180231.874644 | source=vosk | rms=488 | updated_at=1788180231.874644 | frequency_hz=229.2
- [2026-08-31 20:43:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180232.3745525 | source=vosk | rms=488 | updated_at=1788180231.874644 | frequency_hz=229.2
- [2026-08-31 20:43:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180233.3736167 | source=vosk | rms=800 | updated_at=1788180233.3736167 | frequency_hz=229.2
- [2026-08-31 20:43:54] operator / voice_transcript_partial / voice: sound volume set to thirty
  meta: kind=partial | timestamp=1788180234.9078808 | source=vosk | rms=678 | updated_at=1788180234.8742485 | frequency_hz=229.2
- [2026-08-31 20:43:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180235.125398 | source=vosk | rms=1201 | updated_at=1788180235.125398 | frequency_hz=229.2
- [2026-08-31 20:43:55] operator / voice_transcript_partial / voice: sound volume set to thirty nine
  meta: kind=partial | timestamp=1788180235.163547 | source=vosk | rms=1201 | updated_at=1788180235.125398 | frequency_hz=229.2
- [2026-08-31 20:43:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180235.3737872 | source=vosk | rms=528 | updated_at=1788180235.3737872 | frequency_hz=229.2
- [2026-08-31 20:43:55] operator / voice_transcript_partial / voice: sound volume set to thirty nine percent
  meta: kind=partial | timestamp=1788180235.4136343 | source=vosk | rms=528 | updated_at=1788180235.3737872 | frequency_hz=229.2
- [2026-08-31 20:43:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180235.6239114 | source=vosk | rms=528 | updated_at=1788180235.3737872 | frequency_hz=229.2
- [2026-08-31 20:43:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180236.1244266 | source=vosk | rms=528 | updated_at=1788180235.3737872 | frequency_hz=229.2
- [2026-08-31 20:44:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180241.3741806 | source=vosk | rms=528 | updated_at=1788180235.3737872 | frequency_hz=229.2
- [2026-08-31 20:44:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180241.874766 | source=vosk | rms=528 | updated_at=1788180235.3737872 | frequency_hz=229.2
- [2026-08-31 20:44:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180247.6239443 | source=vosk | rms=552 | updated_at=1788180247.6239443 | frequency_hz=229.2
- [2026-08-31 20:44:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180248.1582205 | source=vosk | rms=552 | updated_at=1788180247.6239443 | frequency_hz=229.2
- [2026-08-31 20:44:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180250.3743095 | source=vosk | rms=552 | updated_at=1788180247.6239443 | frequency_hz=229.2
- [2026-08-31 20:44:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180250.8750982 | source=vosk | rms=552 | updated_at=1788180247.6239443 | frequency_hz=229.2
- [2026-08-31 20:44:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180252.1242816 | source=vosk | rms=227 | updated_at=1788180252.1242816 | frequency_hz=229.2
- [2026-08-31 20:44:12] operator / voice_transcript_final / voice: sound volume set to thirty nine percent
  meta: kind=final | timestamp=1788180252.3929029 | source=final | rms=227 | updated_at=1788180252.1242816 | frequency_hz=229.2
- [2026-08-31 20:44:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180252.6949992 | source=vosk | rms=227 | updated_at=1788180252.1242816 | frequency_hz=229.2
- [2026-08-31 20:44:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180252.6949992 | source=vosk | rms=160 | updated_at=1788180252.6949992 | frequency_hz=229.2
- [2026-08-31 20:44:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180253.6504188 | source=vosk | rms=160 | updated_at=1788180252.6949992 | frequency_hz=229.2
- [2026-08-31 20:44:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180253.8943796 | source=vosk | rms=543 | updated_at=1788180253.8943796 | frequency_hz=229.2
- [2026-08-31 20:44:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180254.6453636 | source=vosk | rms=532 | updated_at=1788180254.1932526 | frequency_hz=229.2
- [2026-08-31 20:44:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180254.8936586 | source=vosk | rms=426 | updated_at=1788180254.8936586 | frequency_hz=293.2
- [2026-08-31 20:44:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180256.6444004 | source=vosk | rms=426 | updated_at=1788180254.8936586 | frequency_hz=293.2
- [2026-08-31 20:44:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180257.8948388 | source=vosk | rms=602 | updated_at=1788180257.8948388 | frequency_hz=293.2
- [2026-08-31 20:44:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180258.6444237 | source=vosk | rms=602 | updated_at=1788180257.8948388 | frequency_hz=293.2
- [2026-08-31 20:44:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180259.3951588 | source=vosk | rms=176 | updated_at=1788180259.3951588 | frequency_hz=240.0
- [2026-08-31 20:44:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180259.8977318 | source=vosk | rms=176 | updated_at=1788180259.3951588 | frequency_hz=240.0
- [2026-08-31 20:44:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180261.6445732 | source=vosk | rms=176 | updated_at=1788180259.3951588 | frequency_hz=240.0
- [2026-08-31 20:44:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180262.1444883 | source=vosk | rms=176 | updated_at=1788180259.3951588 | frequency_hz=240.0
- [2026-08-31 20:44:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180262.3967936 | source=vosk | rms=159 | updated_at=1788180262.39579 | frequency_hz=240.0
- [2026-08-31 20:44:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180263.144686 | source=vosk | rms=159 | updated_at=1788180262.39579 | frequency_hz=240.0
- [2026-08-31 20:44:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180266.3951044 | source=vosk | rms=159 | updated_at=1788180262.39579 | frequency_hz=240.0
- [2026-08-31 20:44:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180266.8946242 | source=vosk | rms=159 | updated_at=1788180262.39579 | frequency_hz=240.0
- [2026-08-31 20:44:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180268.3948534 | source=vosk | rms=125 | updated_at=1788180268.3948534 | frequency_hz=240.0
- [2026-08-31 20:44:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180269.3945117 | source=vosk | rms=281 | updated_at=1788180268.8945608 | frequency_hz=232.3
- [2026-08-31 20:44:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180270.1458848 | source=vosk | rms=281 | updated_at=1788180268.8945608 | frequency_hz=232.3
- [2026-08-31 20:44:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180271.3953083 | source=vosk | rms=139 | updated_at=1788180270.8950772 | frequency_hz=232.3
- [2026-08-31 20:44:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180271.8952081 | source=vosk | rms=1001 | updated_at=1788180271.8952081 | frequency_hz=232.3
- [2026-08-31 20:44:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180272.6455207 | source=vosk | rms=428 | updated_at=1788180272.1448488 | frequency_hz=242.7
- [2026-08-31 20:44:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180273.3944638 | source=vosk | rms=428 | updated_at=1788180272.1448488 | frequency_hz=242.7
- [2026-08-31 20:44:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180273.8949 | source=vosk | rms=428 | updated_at=1788180272.1448488 | frequency_hz=242.7
- [2026-08-31 20:44:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180274.1444721 | source=vosk | rms=428 | updated_at=1788180272.1448488 | frequency_hz=242.7
- [2026-08-31 20:44:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180274.644479 | source=vosk | rms=428 | updated_at=1788180272.1448488 | frequency_hz=242.7
- [2026-08-31 20:44:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180274.89593 | source=vosk | rms=428 | updated_at=1788180272.1448488 | frequency_hz=242.7
- [2026-08-31 20:44:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180275.3945062 | source=vosk | rms=428 | updated_at=1788180272.1448488 | frequency_hz=242.7
- [2026-08-31 20:44:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180275.644856 | source=vosk | rms=251 | updated_at=1788180275.644856 | frequency_hz=242.7
- [2026-08-31 20:44:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180276.3950799 | source=vosk | rms=155 | updated_at=1788180275.9008412 | frequency_hz=242.7
- [2026-08-31 20:44:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180276.6451702 | source=vosk | rms=155 | updated_at=1788180275.9008412 | frequency_hz=242.7
- [2026-08-31 20:44:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180278.1460276 | source=vosk | rms=763 | updated_at=1788180277.644633 | frequency_hz=321.1
- [2026-08-31 20:44:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180278.8961012 | source=vosk | rms=236 | updated_at=1788180278.8961012 | frequency_hz=321.1
- [2026-08-31 20:44:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180280.8948417 | source=vosk | rms=662 | updated_at=1788180280.394606 | frequency_hz=321.1
- [2026-08-31 20:44:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180281.3942008 | source=vosk | rms=1201 | updated_at=1788180281.3942008 | frequency_hz=321.1
- [2026-08-31 20:44:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180281.8960016 | source=vosk | rms=1201 | updated_at=1788180281.3942008 | frequency_hz=321.1
- [2026-08-31 20:44:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180285.154284 | source=vosk | rms=145 | updated_at=1788180285.154284 | frequency_hz=321.1
- [2026-08-31 20:44:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180286.145219 | source=vosk | rms=134 | updated_at=1788180285.6804347 | frequency_hz=233.9
- [2026-08-31 20:44:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180287.145171 | source=vosk | rms=753 | updated_at=1788180287.145171 | frequency_hz=334.0
- [2026-08-31 20:44:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180287.895835 | source=vosk | rms=753 | updated_at=1788180287.145171 | frequency_hz=334.0
- [2026-08-31 20:44:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180288.6456494 | source=vosk | rms=253 | updated_at=1788180288.6451464 | frequency_hz=334.0
- [2026-08-31 20:44:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180289.395404 | source=vosk | rms=133 | updated_at=1788180288.8953507 | frequency_hz=334.0
- [2026-08-31 20:44:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180292.1446943 | source=vosk | rms=205 | updated_at=1788180292.1446943 | frequency_hz=334.0
- [2026-08-31 20:44:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180292.6453414 | source=vosk | rms=205 | updated_at=1788180292.1446943 | frequency_hz=334.0
- [2026-08-31 20:44:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180297.9358554 | source=vosk | rms=733 | updated_at=1788180297.9358554 | frequency_hz=334.0
- [2026-08-31 20:44:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180298.6879945 | source=vosk | rms=184 | updated_at=1788180298.185678 | frequency_hz=299.0
- [2026-08-31 20:44:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180299.1864948 | source=vosk | rms=431 | updated_at=1788180299.1849928 | frequency_hz=299.0
- [2026-08-31 20:44:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180299.9535966 | source=vosk | rms=129 | updated_at=1788180299.435817 | frequency_hz=290.2
- [2026-08-31 20:45:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180300.685987 | source=vosk | rms=1004 | updated_at=1788180300.684479 | frequency_hz=219.4
- [2026-08-31 20:45:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180301.1855876 | source=vosk | rms=1004 | updated_at=1788180300.684479 | frequency_hz=219.4
- [2026-08-31 20:45:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180301.6853662 | source=vosk | rms=663 | updated_at=1788180301.6853662 | frequency_hz=191.6
- [2026-08-31 20:45:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180302.2164707 | source=vosk | rms=663 | updated_at=1788180301.6853662 | frequency_hz=191.6
- [2026-08-31 20:45:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180303.9351676 | source=vosk | rms=663 | updated_at=1788180301.6853662 | frequency_hz=191.6
- [2026-08-31 20:45:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180304.435804 | source=vosk | rms=663 | updated_at=1788180301.6853662 | frequency_hz=191.6
- [2026-08-31 20:45:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180310.4158278 | source=vosk | rms=663 | updated_at=1788180301.6853662 | frequency_hz=191.6
- [2026-08-31 20:45:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180310.9153745 | source=vosk | rms=663 | updated_at=1788180301.6853662 | frequency_hz=191.6
- [2026-08-31 20:45:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180312.1660132 | source=vosk | rms=126 | updated_at=1788180312.1660132 | frequency_hz=180.0
- [2026-08-31 20:45:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180312.6663058 | source=vosk | rms=126 | updated_at=1788180312.1660132 | frequency_hz=180.0
- [2026-08-31 20:45:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180313.1660533 | source=vosk | rms=935 | updated_at=1788180313.1660533 | frequency_hz=168.1
- [2026-08-31 20:45:16] operator / voice_transcript_partial / voice: low
  meta: kind=partial | timestamp=1788180316.2255888 | source=vosk | rms=228 | updated_at=1788180316.2053084 | frequency_hz=228.7
- [2026-08-31 20:45:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180316.4558036 | source=vosk | rms=662 | updated_at=1788180316.4558036 | frequency_hz=228.7
- [2026-08-31 20:45:16] operator / voice_transcript_partial / voice: low car
  meta: kind=partial | timestamp=1788180316.4708662 | source=vosk | rms=662 | updated_at=1788180316.4558036 | frequency_hz=228.7
- [2026-08-31 20:45:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180316.9554617 | source=vosk | rms=662 | updated_at=1788180316.4558036 | frequency_hz=228.7
- [2026-08-31 20:45:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180318.705327 | source=vosk | rms=1031 | updated_at=1788180318.705327 | frequency_hz=228.7
- [2026-08-31 20:45:18] operator / voice_transcript_partial / voice: low carla
  meta: kind=partial | timestamp=1788180318.71489 | source=vosk | rms=1031 | updated_at=1788180318.705327 | frequency_hz=228.7
- [2026-08-31 20:45:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180318.955442 | source=vosk | rms=1205 | updated_at=1788180318.955442 | frequency_hz=228.7
- [2026-08-31 20:45:19] operator / voice_transcript_final / voice: low carla
  meta: kind=final | timestamp=1788180319.1587732 | source=final | rms=1205 | updated_at=1788180318.955442 | frequency_hz=228.7
- [2026-08-31 20:45:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180319.4562826 | source=vosk | rms=1205 | updated_at=1788180318.955442 | frequency_hz=228.7
- [2026-08-31 20:45:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180319.7061164 | source=vosk | rms=1205 | updated_at=1788180318.955442 | frequency_hz=228.7
- [2026-08-31 20:45:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180320.4560833 | source=vosk | rms=1205 | updated_at=1788180318.955442 | frequency_hz=228.7
- [2026-08-31 20:45:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180320.7092886 | source=vosk | rms=622 | updated_at=1788180320.7092886 | frequency_hz=228.7
- [2026-08-31 20:45:21] operator / voice_transcript_partial / voice: below
  meta: kind=partial | timestamp=1788180321.221427 | source=vosk | rms=851 | updated_at=1788180321.20558 | frequency_hz=228.7
- [2026-08-31 20:45:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180321.455769 | source=vosk | rms=649 | updated_at=1788180321.455769 | frequency_hz=228.7
- [2026-08-31 20:45:21] operator / voice_transcript_partial / voice: below grade
  meta: kind=partial | timestamp=1788180321.4872065 | source=vosk | rms=649 | updated_at=1788180321.455769 | frequency_hz=228.7
- [2026-08-31 20:45:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180321.9659278 | source=vosk | rms=649 | updated_at=1788180321.455769 | frequency_hz=228.7
- [2026-08-31 20:45:21] operator / voice_transcript_partial / voice: below grace
  meta: kind=partial | timestamp=1788180321.984526 | source=vosk | rms=649 | updated_at=1788180321.455769 | frequency_hz=228.7
- [2026-08-31 20:45:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180322.4562314 | source=vosk | rms=649 | updated_at=1788180321.455769 | frequency_hz=228.7
- [2026-08-31 20:45:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180322.9559517 | source=vosk | rms=649 | updated_at=1788180321.455769 | frequency_hz=228.7
- [2026-08-31 20:45:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180323.455293 | source=vosk | rms=649 | updated_at=1788180321.455769 | frequency_hz=228.7
- [2026-08-31 20:45:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180323.7054656 | source=vosk | rms=178 | updated_at=1788180323.7054656 | frequency_hz=228.7
- [2026-08-31 20:45:23] operator / voice_transcript_final / voice: below grace
  meta: kind=final | timestamp=1788180323.88473 | source=final | rms=178 | updated_at=1788180323.7054656 | frequency_hz=228.7
- [2026-08-31 20:45:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180324.2063437 | source=vosk | rms=178 | updated_at=1788180323.7054656 | frequency_hz=228.7
- [2026-08-31 20:45:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180326.7053509 | source=vosk | rms=178 | updated_at=1788180323.7054656 | frequency_hz=228.7
- [2026-08-31 20:45:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180327.4562812 | source=vosk | rms=737 | updated_at=1788180326.9560254 | frequency_hz=228.7
- [2026-08-31 20:45:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180330.7064095 | source=vosk | rms=894 | updated_at=1788180330.7064095 | frequency_hz=356.0
- [2026-08-31 20:45:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180331.206438 | source=vosk | rms=894 | updated_at=1788180330.7064095 | frequency_hz=356.0
- [2026-08-31 20:45:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180332.955489 | source=vosk | rms=1203 | updated_at=1788180332.955489 | frequency_hz=254.0
- [2026-08-31 20:45:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180333.7057948 | source=vosk | rms=767 | updated_at=1788180333.2061803 | frequency_hz=254.0
- [2026-08-31 20:45:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180333.9562595 | source=vosk | rms=1204 | updated_at=1788180333.9562595 | frequency_hz=240.7
- [2026-08-31 20:45:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180334.710151 | source=vosk | rms=940 | updated_at=1788180334.2061598 | frequency_hz=240.7
- [2026-08-31 20:45:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180334.9559956 | source=vosk | rms=672 | updated_at=1788180334.9559956 | frequency_hz=240.7
- [2026-08-31 20:45:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180335.706252 | source=vosk | rms=278 | updated_at=1788180335.2073228 | frequency_hz=240.7
- [2026-08-31 20:45:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180336.206012 | source=vosk | rms=186 | updated_at=1788180336.206012 | frequency_hz=240.7
- [2026-08-31 20:45:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180336.7057495 | source=vosk | rms=186 | updated_at=1788180336.206012 | frequency_hz=240.7
- [2026-08-31 20:45:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180339.9556754 | source=vosk | rms=321 | updated_at=1788180339.9556754 | frequency_hz=240.7
- [2026-08-31 20:45:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180340.4555616 | source=vosk | rms=321 | updated_at=1788180339.9556754 | frequency_hz=240.7
- [2026-08-31 20:45:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180341.4561973 | source=vosk | rms=288 | updated_at=1788180341.4561973 | frequency_hz=240.7
- [2026-08-31 20:45:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180342.205739 | source=vosk | rms=288 | updated_at=1788180341.4561973 | frequency_hz=240.7
- [2026-08-31 20:45:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180351.2118564 | source=vosk | rms=157 | updated_at=1788180351.2118564 | frequency_hz=240.7
- [2026-08-31 20:45:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180351.9562354 | source=vosk | rms=157 | updated_at=1788180351.2118564 | frequency_hz=240.7
- [2026-08-31 20:45:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180355.7074082 | source=vosk | rms=157 | updated_at=1788180351.2118564 | frequency_hz=240.7
- [2026-08-31 20:45:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180356.9565396 | source=vosk | rms=138 | updated_at=1788180356.4567065 | frequency_hz=240.7
- [2026-08-31 20:46:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180364.45634 | source=vosk | rms=1200 | updated_at=1788180364.45634 | frequency_hz=240.0
- [2026-08-31 20:46:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180365.2066166 | source=vosk | rms=575 | updated_at=1788180364.7074242 | frequency_hz=240.0
- [2026-08-31 20:46:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180367.207617 | source=vosk | rms=990 | updated_at=1788180367.207617 | frequency_hz=240.0
- [2026-08-31 20:46:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180367.7076514 | source=vosk | rms=990 | updated_at=1788180367.207617 | frequency_hz=240.0
- [2026-08-31 20:46:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180367.9560885 | source=vosk | rms=990 | updated_at=1788180367.207617 | frequency_hz=240.0
- [2026-08-31 20:46:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180368.456245 | source=vosk | rms=990 | updated_at=1788180367.207617 | frequency_hz=240.0
- [2026-08-31 20:46:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180375.0466557 | source=vosk | rms=1205 | updated_at=1788180375.0466557 | frequency_hz=278.0
- [2026-08-31 20:46:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180375.838973 | source=vosk | rms=487 | updated_at=1788180375.2970488 | frequency_hz=278.0
- [2026-08-31 20:46:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180377.0466971 | source=vosk | rms=262 | updated_at=1788180377.0466971 | frequency_hz=312.0
- [2026-08-31 20:46:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180377.548277 | source=vosk | rms=262 | updated_at=1788180377.0466971 | frequency_hz=312.0
- [2026-08-31 20:46:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180377.80576 | source=vosk | rms=181 | updated_at=1788180377.80576 | frequency_hz=312.0
- [2026-08-31 20:46:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180378.2968307 | source=vosk | rms=181 | updated_at=1788180377.80576 | frequency_hz=312.0
- [2026-08-31 20:46:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180379.5832214 | source=vosk | rms=909 | updated_at=1788180379.5832214 | frequency_hz=312.0
- [2026-08-31 20:46:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180380.8267164 | source=vosk | rms=381 | updated_at=1788180379.8284712 | frequency_hz=253.9
- [2026-08-31 20:46:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180391.5772626 | source=vosk | rms=381 | updated_at=1788180379.8284712 | frequency_hz=253.9
- [2026-08-31 20:46:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180392.1059625 | source=vosk | rms=381 | updated_at=1788180379.8284712 | frequency_hz=253.9
- [2026-08-31 20:46:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180392.3267288 | source=vosk | rms=381 | updated_at=1788180379.8284712 | frequency_hz=253.9
- [2026-08-31 20:46:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180392.826602 | source=vosk | rms=381 | updated_at=1788180379.8284712 | frequency_hz=253.9
- [2026-08-31 20:46:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180394.0771217 | source=vosk | rms=124 | updated_at=1788180394.0771217 | frequency_hz=253.9
- [2026-08-31 20:46:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180395.5775867 | source=vosk | rms=192 | updated_at=1788180395.077075 | frequency_hz=253.9
- [2026-08-31 20:46:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180395.8516042 | source=vosk | rms=192 | updated_at=1788180395.077075 | frequency_hz=253.9
- [2026-08-31 20:46:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180396.327389 | source=vosk | rms=192 | updated_at=1788180395.077075 | frequency_hz=253.9
- [2026-08-31 20:46:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180397.5767896 | source=vosk | rms=192 | updated_at=1788180395.077075 | frequency_hz=253.9
- [2026-08-31 20:46:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180398.0791764 | source=vosk | rms=192 | updated_at=1788180395.077075 | frequency_hz=253.9
- [2026-08-31 20:46:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180398.5773873 | source=vosk | rms=192 | updated_at=1788180395.077075 | frequency_hz=253.9
- [2026-08-31 20:46:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180399.0773022 | source=vosk | rms=192 | updated_at=1788180395.077075 | frequency_hz=253.9
- [2026-08-31 20:46:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180409.8284652 | source=vosk | rms=215 | updated_at=1788180409.8284652 | frequency_hz=253.9
- [2026-08-31 20:46:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180412.5772817 | source=vosk | rms=169 | updated_at=1788180412.0771317 | frequency_hz=253.9
- [2026-08-31 20:46:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180414.3279927 | source=vosk | rms=369 | updated_at=1788180414.3279927 | frequency_hz=253.9
- [2026-08-31 20:46:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180415.3477268 | source=vosk | rms=287 | updated_at=1788180414.8288035 | frequency_hz=253.9
- [2026-08-31 20:46:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180418.5778131 | source=vosk | rms=121 | updated_at=1788180418.5778131 | frequency_hz=253.9
- [2026-08-31 20:47:00] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1788180420.3968482 | source=vosk | rms=278 | updated_at=1788180420.3278127 | frequency_hz=253.9
- [2026-08-31 20:47:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180420.577507 | source=vosk | rms=422 | updated_at=1788180420.577507 | frequency_hz=253.9
- [2026-08-31 20:47:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180421.0777864 | source=vosk | rms=228 | updated_at=1788180421.0777864 | frequency_hz=253.9
- [2026-08-31 20:47:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180421.3272192 | source=vosk | rms=420 | updated_at=1788180421.3272192 | frequency_hz=253.9
- [2026-08-31 20:47:01] operator / voice_transcript_final / voice: what
  meta: kind=final | timestamp=1788180421.7513125 | source=final | rms=420 | updated_at=1788180421.3272192 | frequency_hz=253.9
- [2026-08-31 20:47:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180421.8015406 | source=vosk | rms=420 | updated_at=1788180421.3272192 | frequency_hz=253.9
- [2026-08-31 20:47:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180421.8015406 | source=vosk | rms=305 | updated_at=1788180421.8015406 | frequency_hz=253.9
- [2026-08-31 20:47:03] operator / voice_transcript_partial / voice: rather than
  meta: kind=partial | timestamp=1788180423.421098 | source=vosk | rms=505 | updated_at=1788180423.3278008 | frequency_hz=253.9
- [2026-08-31 20:47:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180423.577235 | source=vosk | rms=299 | updated_at=1788180423.577235 | frequency_hz=253.9
- [2026-08-31 20:47:04] operator / voice_transcript_partial / voice: it would
  meta: kind=partial | timestamp=1788180424.87487 | source=vosk | rms=223 | updated_at=1788180424.5774431 | frequency_hz=253.9
- [2026-08-31 20:47:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180425.0776134 | source=vosk | rms=291 | updated_at=1788180425.0776134 | frequency_hz=253.9
- [2026-08-31 20:47:06] operator / voice_transcript_partial / voice: mother was
  meta: kind=partial | timestamp=1788180426.4017153 | source=vosk | rms=382 | updated_at=1788180426.3275354 | frequency_hz=253.9
- [2026-08-31 20:47:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180426.5773432 | source=vosk | rms=1203 | updated_at=1788180426.5773432 | frequency_hz=253.9
- [2026-08-31 20:47:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180426.826964 | source=vosk | rms=1201 | updated_at=1788180426.826964 | frequency_hz=253.9
- [2026-08-31 20:47:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180427.0777717 | source=vosk | rms=1201 | updated_at=1788180426.826964 | frequency_hz=253.9
- [2026-08-31 20:47:07] operator / voice_transcript_final / voice: mother was
  meta: kind=final | timestamp=1788180427.2991707 | source=final | rms=1201 | updated_at=1788180426.826964 | frequency_hz=253.9
- [2026-08-31 20:47:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180427.3780992 | source=vosk | rms=526 | updated_at=1788180427.3780992 | frequency_hz=253.9
- [2026-08-31 20:47:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180428.5782359 | source=vosk | rms=172 | updated_at=1788180427.578908 | frequency_hz=253.9
- [2026-08-31 20:47:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180429.3279562 | source=vosk | rms=172 | updated_at=1788180427.578908 | frequency_hz=253.9
- [2026-08-31 20:47:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180429.8278959 | source=vosk | rms=172 | updated_at=1788180427.578908 | frequency_hz=253.9
- [2026-08-31 20:47:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180431.0777304 | source=vosk | rms=259 | updated_at=1788180431.0777304 | frequency_hz=253.9
- [2026-08-31 20:47:12] operator / voice_transcript_partial / voice: part of
  meta: kind=partial | timestamp=1788180432.1068106 | source=vosk | rms=1015 | updated_at=1788180432.0777936 | frequency_hz=253.9
- [2026-08-31 20:47:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180432.3270543 | source=vosk | rms=364 | updated_at=1788180432.3270543 | frequency_hz=253.9
- [2026-08-31 20:47:12] operator / voice_transcript_partial / voice: part of a
  meta: kind=partial | timestamp=1788180432.8665998 | source=vosk | rms=364 | updated_at=1788180432.3270543 | frequency_hz=253.9
- [2026-08-31 20:47:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180433.0775125 | source=vosk | rms=187 | updated_at=1788180433.0775125 | frequency_hz=253.9
- [2026-08-31 20:47:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180433.3284416 | source=vosk | rms=239 | updated_at=1788180433.3284416 | frequency_hz=253.9
- [2026-08-31 20:47:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180433.57918 | source=vosk | rms=352 | updated_at=1788180433.57918 | frequency_hz=253.9
- [2026-08-31 20:47:13] operator / voice_transcript_final / voice: arch a
  meta: kind=final | timestamp=1788180433.8799813 | source=final | rms=352 | updated_at=1788180433.57918 | frequency_hz=253.9
- [2026-08-31 20:47:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180433.9319005 | source=vosk | rms=352 | updated_at=1788180433.57918 | frequency_hz=253.9
- [2026-08-31 20:47:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180435.0778606 | source=vosk | rms=849 | updated_at=1788180434.577894 | frequency_hz=206.3
- [2026-08-31 20:47:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180437.0782852 | source=vosk | rms=287 | updated_at=1788180437.0782852 | frequency_hz=206.3
- [2026-08-31 20:47:17] operator / voice_transcript_partial / voice: at the
  meta: kind=partial | timestamp=1788180437.6600325 | source=vosk | rms=452 | updated_at=1788180437.5783136 | frequency_hz=206.3
- [2026-08-31 20:47:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180437.827929 | source=vosk | rms=452 | updated_at=1788180437.5783136 | frequency_hz=206.3
- [2026-08-31 20:47:17] operator / voice_transcript_partial / voice: at the target of
  meta: kind=partial | timestamp=1788180437.9401548 | source=vosk | rms=452 | updated_at=1788180437.5783136 | frequency_hz=206.3
- [2026-08-31 20:47:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180438.0783818 | source=vosk | rms=452 | updated_at=1788180437.5783136 | frequency_hz=206.3
- [2026-08-31 20:47:18] operator / voice_transcript_partial / voice: attitude you don't
  meta: kind=partial | timestamp=1788180438.1339607 | source=vosk | rms=452 | updated_at=1788180437.5783136 | frequency_hz=206.3
- [2026-08-31 20:47:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180438.578108 | source=vosk | rms=172 | updated_at=1788180438.578108 | frequency_hz=206.3
- [2026-08-31 20:47:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180438.8282998 | source=vosk | rms=702 | updated_at=1788180438.8282998 | frequency_hz=206.3
- [2026-08-31 20:47:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180439.0782678 | source=vosk | rms=1105 | updated_at=1788180439.0782678 | frequency_hz=206.3
- [2026-08-31 20:47:19] operator / voice_transcript_partial / voice: attitude you don't know about
  meta: kind=partial | timestamp=1788180439.1439824 | source=vosk | rms=1105 | updated_at=1788180439.0782678 | frequency_hz=206.3
- [2026-08-31 20:47:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180439.328069 | source=vosk | rms=1105 | updated_at=1788180439.0782678 | frequency_hz=206.3
- [2026-08-31 20:47:19] operator / voice_transcript_partial / voice: as opposed to
  meta: kind=partial | timestamp=1788180439.3713665 | source=vosk | rms=1105 | updated_at=1788180439.0782678 | frequency_hz=206.3
- [2026-08-31 20:47:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180439.57901 | source=vosk | rms=706 | updated_at=1788180439.57901 | frequency_hz=206.3
- [2026-08-31 20:47:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180439.8285239 | source=vosk | rms=496 | updated_at=1788180439.8285239 | frequency_hz=206.3
- [2026-08-31 20:47:19] operator / voice_transcript_partial / voice: as opposed to a football
  meta: kind=partial | timestamp=1788180439.8816924 | source=vosk | rms=496 | updated_at=1788180439.8285239 | frequency_hz=206.3
- [2026-08-31 20:47:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180440.0780914 | source=vosk | rms=417 | updated_at=1788180440.0780914 | frequency_hz=206.3
- [2026-08-31 20:47:20] operator / voice_transcript_partial / voice: attitude you don't oppose abortion or
  meta: kind=partial | timestamp=1788180440.1261618 | source=vosk | rms=417 | updated_at=1788180440.0780914 | frequency_hz=206.3
- [2026-08-31 20:47:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180440.3279762 | source=vosk | rms=402 | updated_at=1788180440.3279762 | frequency_hz=206.3
- [2026-08-31 20:47:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180440.8280542 | source=vosk | rms=402 | updated_at=1788180440.3279762 | frequency_hz=206.3
- [2026-08-31 20:47:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180441.078343 | source=vosk | rms=976 | updated_at=1788180441.078343 | frequency_hz=206.3
- [2026-08-31 20:47:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180441.3282244 | source=vosk | rms=370 | updated_at=1788180441.3282244 | frequency_hz=206.3
- [2026-08-31 20:47:21] operator / voice_transcript_partial / voice: attitude you don't oppose abortion is also
  meta: kind=partial | timestamp=1788180441.3562865 | source=vosk | rms=370 | updated_at=1788180441.3282244 | frequency_hz=206.3
- [2026-08-31 20:47:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180441.828515 | source=vosk | rms=370 | updated_at=1788180441.3282244 | frequency_hz=206.3
- [2026-08-31 20:47:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180442.3280373 | source=vosk | rms=417 | updated_at=1788180442.3280373 | frequency_hz=206.3
- [2026-08-31 20:47:22] operator / voice_transcript_partial / voice: attitude you don't oppose abortion is also my
  meta: kind=partial | timestamp=1788180442.4068325 | source=vosk | rms=417 | updated_at=1788180442.3280373 | frequency_hz=206.3
- [2026-08-31 20:47:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180442.5785415 | source=vosk | rms=1121 | updated_at=1788180442.5785415 | frequency_hz=206.3
- [2026-08-31 20:47:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180442.8281846 | source=vosk | rms=677 | updated_at=1788180442.8281846 | frequency_hz=206.3
- [2026-08-31 20:47:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180443.078226 | source=vosk | rms=423 | updated_at=1788180443.078226 | frequency_hz=206.3
- [2026-08-31 20:47:23] operator / voice_transcript_final / voice: at the you don t oppose abortion or she is also one
  meta: kind=final | timestamp=1788180443.4559135 | source=final | rms=423 | updated_at=1788180443.078226 | frequency_hz=206.3
- [2026-08-31 20:47:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180443.5853946 | source=vosk | rms=423 | updated_at=1788180443.078226 | frequency_hz=206.3
- [2026-08-31 20:47:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180443.5853946 | source=vosk | rms=846 | updated_at=1788180443.5853946 | frequency_hz=206.3
- [2026-08-31 20:47:23] operator / voice_transcript_partial / voice: obama
  meta: kind=partial | timestamp=1788180443.6113513 | source=vosk | rms=973 | updated_at=1788180443.5946193 | frequency_hz=206.3
- [2026-08-31 20:47:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180443.8273792 | source=vosk | rms=900 | updated_at=1788180443.8273792 | frequency_hz=206.3
- [2026-08-31 20:47:23] operator / voice_transcript_partial / voice: up up up up
  meta: kind=partial | timestamp=1788180443.8549845 | source=vosk | rms=900 | updated_at=1788180443.8273792 | frequency_hz=206.3
- [2026-08-31 20:47:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180444.328339 | source=vosk | rms=900 | updated_at=1788180443.8273792 | frequency_hz=206.3
- [2026-08-31 20:47:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180447.328465 | source=vosk | rms=317 | updated_at=1788180447.328465 | frequency_hz=206.3
- [2026-08-31 20:47:27] operator / voice_transcript_partial / voice: up up up up up
  meta: kind=partial | timestamp=1788180447.347557 | source=vosk | rms=317 | updated_at=1788180447.328465 | frequency_hz=206.3
- [2026-08-31 20:47:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180447.5777264 | source=vosk | rms=317 | updated_at=1788180447.328465 | frequency_hz=206.3
- [2026-08-31 20:47:27] operator / voice_transcript_partial / voice: up up up up up up
  meta: kind=partial | timestamp=1788180447.5847423 | source=vosk | rms=317 | updated_at=1788180447.328465 | frequency_hz=206.3
- [2026-08-31 20:47:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180447.828483 | source=vosk | rms=604 | updated_at=1788180447.828483 | frequency_hz=206.3
- [2026-08-31 20:47:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180448.0793173 | source=vosk | rms=604 | updated_at=1788180447.828483 | frequency_hz=206.3
- [2026-08-31 20:47:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180448.3282661 | source=vosk | rms=604 | updated_at=1788180447.828483 | frequency_hz=206.3
- [2026-08-31 20:47:29] operator / voice_transcript_final / voice: up up up up up up
  meta: kind=final | timestamp=1788180449.4005883 | source=final | rms=604 | updated_at=1788180447.828483 | frequency_hz=206.3
- [2026-08-31 20:47:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180449.4406111 | source=vosk | rms=604 | updated_at=1788180447.828483 | frequency_hz=206.3
- [2026-08-31 20:47:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180451.5780756 | source=vosk | rms=604 | updated_at=1788180447.828483 | frequency_hz=206.3
- [2026-08-31 20:47:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180452.0782382 | source=vosk | rms=604 | updated_at=1788180447.828483 | frequency_hz=206.3
- [2026-08-31 20:47:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180454.0782092 | source=vosk | rms=604 | updated_at=1788180447.828483 | frequency_hz=206.3
- [2026-08-31 20:47:35] operator / voice_transcript_partial / voice: but it was
  meta: kind=partial | timestamp=1788180455.6204765 | source=vosk | rms=463 | updated_at=1788180455.5788646 | frequency_hz=206.3
- [2026-08-31 20:47:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180455.8283558 | source=vosk | rms=463 | updated_at=1788180455.5788646 | frequency_hz=206.3
- [2026-08-31 20:47:37] operator / voice_transcript_partial / voice: but it will go on
  meta: kind=partial | timestamp=1788180457.3560796 | source=vosk | rms=656 | updated_at=1788180457.3280365 | frequency_hz=206.3
- [2026-08-31 20:47:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180457.5796704 | source=vosk | rms=1085 | updated_at=1788180457.5796704 | frequency_hz=206.3
- [2026-08-31 20:47:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180457.8280973 | source=vosk | rms=734 | updated_at=1788180457.8280973 | frequency_hz=206.3
- [2026-08-31 20:47:37] operator / voice_transcript_partial / voice: but it will go on for another
  meta: kind=partial | timestamp=1788180457.8688536 | source=vosk | rms=734 | updated_at=1788180457.8280973 | frequency_hz=206.3
- [2026-08-31 20:47:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180458.0785768 | source=vosk | rms=645 | updated_at=1788180458.0785768 | frequency_hz=206.3
- [2026-08-31 20:47:38] operator / voice_transcript_partial / voice: but it will go on thrown out
  meta: kind=partial | timestamp=1788180458.141043 | source=vosk | rms=645 | updated_at=1788180458.0785768 | frequency_hz=206.3
- [2026-08-31 20:47:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180458.3285105 | source=vosk | rms=510 | updated_at=1788180458.3285105 | frequency_hz=206.3
- [2026-08-31 20:47:38] operator / voice_transcript_partial / voice: but it will go on for a non
  meta: kind=partial | timestamp=1788180458.3998232 | source=vosk | rms=510 | updated_at=1788180458.3285105 | frequency_hz=206.3
- [2026-08-31 20:47:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180458.5788538 | source=vosk | rms=510 | updated_at=1788180458.3285105 | frequency_hz=206.3
- [2026-08-31 20:47:38] operator / voice_transcript_partial / voice: but it will go on found out when i got
  meta: kind=partial | timestamp=1788180458.5988805 | source=vosk | rms=510 | updated_at=1788180458.3285105 | frequency_hz=206.3
- [2026-08-31 20:47:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180458.828507 | source=vosk | rms=510 | updated_at=1788180458.3285105 | frequency_hz=206.3
- [2026-08-31 20:47:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180459.0788364 | source=vosk | rms=545 | updated_at=1788180459.0788364 | frequency_hz=206.3
- [2026-08-31 20:47:39] operator / voice_transcript_partial / voice: but it will go on found out when i got out
  meta: kind=partial | timestamp=1788180459.1008604 | source=vosk | rms=545 | updated_at=1788180459.0788364 | frequency_hz=206.3
- [2026-08-31 20:47:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180459.328602 | source=vosk | rms=545 | updated_at=1788180459.0788364 | frequency_hz=206.3
- [2026-08-31 20:47:39] operator / voice_transcript_partial / voice: but it will go on found out when i got out of the
  meta: kind=partial | timestamp=1788180459.3807611 | source=vosk | rms=545 | updated_at=1788180459.0788364 | frequency_hz=206.3
- [2026-08-31 20:47:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180459.8280742 | source=vosk | rms=545 | updated_at=1788180459.0788364 | frequency_hz=206.3
- [2026-08-31 20:47:39] operator / voice_transcript_partial / voice: but it will go on found out when i got out of the to the
  meta: kind=partial | timestamp=1788180459.875581 | source=vosk | rms=545 | updated_at=1788180459.0788364 | frequency_hz=206.3
- [2026-08-31 20:47:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180460.0787835 | source=vosk | rms=545 | updated_at=1788180459.0788364 | frequency_hz=206.3
- [2026-08-31 20:47:40] operator / voice_transcript_partial / voice: but it will go on found out when i got out it was
  meta: kind=partial | timestamp=1788180460.129659 | source=vosk | rms=545 | updated_at=1788180459.0788364 | frequency_hz=206.3
- [2026-08-31 20:47:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180460.328801 | source=vosk | rms=332 | updated_at=1788180460.328801 | frequency_hz=206.3
- [2026-08-31 20:47:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180460.5796816 | source=vosk | rms=940 | updated_at=1788180460.5796816 | frequency_hz=206.3
- [2026-08-31 20:47:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180460.828272 | source=vosk | rms=296 | updated_at=1788180460.828272 | frequency_hz=206.3
- [2026-08-31 20:47:40] operator / voice_transcript_partial / voice: but it will go on found out when i got out it was going
  meta: kind=partial | timestamp=1788180460.863554 | source=vosk | rms=296 | updated_at=1788180460.828272 | frequency_hz=206.3
- [2026-08-31 20:47:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180461.0781584 | source=vosk | rms=268 | updated_at=1788180461.0781584 | frequency_hz=206.3
- [2026-08-31 20:47:41] operator / voice_transcript_partial / voice: but it will go on found out when i got out it was going to
  meta: kind=partial | timestamp=1788180461.1165824 | source=vosk | rms=268 | updated_at=1788180461.0781584 | frequency_hz=206.3
- [2026-08-31 20:47:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180461.3283405 | source=vosk | rms=268 | updated_at=1788180461.0781584 | frequency_hz=206.3
- [2026-08-31 20:47:41] operator / voice_transcript_partial / voice: but it will go on found out when i got out it was going to be
  meta: kind=partial | timestamp=1788180461.3800678 | source=vosk | rms=268 | updated_at=1788180461.0781584 | frequency_hz=206.3
- [2026-08-31 20:47:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180461.828272 | source=vosk | rms=268 | updated_at=1788180461.0781584 | frequency_hz=206.3
- [2026-08-31 20:47:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180463.3284242 | source=vosk | rms=268 | updated_at=1788180461.0781584 | frequency_hz=206.3
- [2026-08-31 20:47:43] operator / voice_transcript_partial / voice: but it will go on found out when i got out it was gonna go back
  meta: kind=partial | timestamp=1788180463.4085186 | source=vosk | rms=268 | updated_at=1788180461.0781584 | frequency_hz=206.3
- [2026-08-31 20:47:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180463.579735 | source=vosk | rms=268 | updated_at=1788180461.0781584 | frequency_hz=206.3
- [2026-08-31 20:47:43] operator / voice_transcript_partial / voice: but it will go on found out when i got out it was gonna get over
  meta: kind=partial | timestamp=1788180463.6341758 | source=vosk | rms=268 | updated_at=1788180461.0781584 | frequency_hz=206.3
- [2026-08-31 20:47:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180464.0785942 | source=vosk | rms=268 | updated_at=1788180461.0781584 | frequency_hz=206.3
- [2026-08-31 20:47:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180464.328841 | source=vosk | rms=268 | updated_at=1788180461.0781584 | frequency_hz=206.3
- [2026-08-31 20:47:44] operator / voice_transcript_final / voice: but it will go on find out when i got out of the was gonna to work
  meta: kind=final | timestamp=1788180464.6767337 | source=final | rms=268 | updated_at=1788180461.0781584 | frequency_hz=206.3
- [2026-08-31 20:47:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180465.1006014 | source=vosk | rms=268 | updated_at=1788180461.0781584 | frequency_hz=206.3
- [2026-08-31 20:47:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180465.1006014 | source=vosk | rms=268 | updated_at=1788180461.0781584 | frequency_hz=206.3
- [2026-08-31 20:47:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180466.0782664 | source=vosk | rms=268 | updated_at=1788180461.0781584 | frequency_hz=206.3
- [2026-08-31 20:47:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180466.8294663 | source=vosk | rms=268 | updated_at=1788180461.0781584 | frequency_hz=206.3
- [2026-08-31 20:47:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180467.5839708 | source=vosk | rms=268 | updated_at=1788180461.0781584 | frequency_hz=206.3
- [2026-08-31 20:47:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180469.8285742 | source=vosk | rms=1200 | updated_at=1788180469.8285742 | frequency_hz=206.3
- [2026-08-31 20:47:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180470.337615 | source=vosk | rms=1200 | updated_at=1788180469.8285742 | frequency_hz=206.3
- [2026-08-31 20:47:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180471.8282692 | source=vosk | rms=341 | updated_at=1788180471.8282692 | frequency_hz=206.3
- [2026-08-31 20:47:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180472.5799828 | source=vosk | rms=303 | updated_at=1788180472.0789807 | frequency_hz=206.3
- [2026-08-31 20:47:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180473.3289306 | source=vosk | rms=441 | updated_at=1788180473.3289306 | frequency_hz=206.3
- [2026-08-31 20:47:55] operator / voice_transcript_partial / voice: it was
  meta: kind=partial | timestamp=1788180475.0974712 | source=vosk | rms=324 | updated_at=1788180474.5793169 | frequency_hz=206.3
- [2026-08-31 20:47:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180475.3287604 | source=vosk | rms=324 | updated_at=1788180474.5793169 | frequency_hz=206.3
- [2026-08-31 20:47:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180475.8290293 | source=vosk | rms=324 | updated_at=1788180474.5793169 | frequency_hz=206.3
- [2026-08-31 20:47:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180477.0786655 | source=vosk | rms=324 | updated_at=1788180474.5793169 | frequency_hz=206.3
- [2026-08-31 20:47:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180477.5799623 | source=vosk | rms=324 | updated_at=1788180474.5793169 | frequency_hz=206.3
- [2026-08-31 20:47:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180479.8285422 | source=vosk | rms=324 | updated_at=1788180474.5793169 | frequency_hz=206.3
- [2026-08-31 20:48:00] operator / voice_transcript_final / voice: it was great
  meta: kind=final | timestamp=1788180480.1459782 | source=final | rms=324 | updated_at=1788180474.5793169 | frequency_hz=206.3
- [2026-08-31 20:48:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180480.2586002 | source=vosk | rms=324 | updated_at=1788180474.5793169 | frequency_hz=206.3
- [2026-08-31 20:48:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180481.0785372 | source=vosk | rms=264 | updated_at=1788180481.0785372 | frequency_hz=206.3
- [2026-08-31 20:48:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180481.827957 | source=vosk | rms=264 | updated_at=1788180481.0785372 | frequency_hz=206.3
- [2026-08-31 20:48:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180482.5787387 | source=vosk | rms=264 | updated_at=1788180481.0785372 | frequency_hz=206.3
- [2026-08-31 20:48:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180483.0790277 | source=vosk | rms=264 | updated_at=1788180481.0785372 | frequency_hz=206.3
- [2026-08-31 20:48:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180484.829192 | source=vosk | rms=264 | updated_at=1788180481.0785372 | frequency_hz=206.3
- [2026-08-31 20:48:04] operator / voice_transcript_partial / voice: look out
  meta: kind=partial | timestamp=1788180484.8665981 | source=vosk | rms=264 | updated_at=1788180481.0785372 | frequency_hz=206.3
- [2026-08-31 20:48:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180485.3285217 | source=vosk | rms=264 | updated_at=1788180481.0785372 | frequency_hz=206.3
- [2026-08-31 20:48:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180487.5801837 | source=vosk | rms=264 | updated_at=1788180481.0785372 | frequency_hz=206.3
- [2026-08-31 20:48:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180487.8286643 | source=vosk | rms=720 | updated_at=1788180487.8286643 | frequency_hz=206.3
- [2026-08-31 20:48:08] operator / voice_transcript_final / voice: look out
  meta: kind=final | timestamp=1788180488.0530457 | source=final | rms=720 | updated_at=1788180487.8286643 | frequency_hz=206.3
- [2026-08-31 20:48:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180488.3292994 | source=vosk | rms=720 | updated_at=1788180487.8286643 | frequency_hz=206.3
- [2026-08-31 20:48:08] operator / voice_transcript_partial / voice: jupiter jupiter
  meta: kind=partial | timestamp=1788180488.853003 | source=vosk | rms=299 | updated_at=1788180488.8289587 | frequency_hz=206.3
- [2026-08-31 20:48:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180489.0871482 | source=vosk | rms=455 | updated_at=1788180489.0871482 | frequency_hz=206.3
- [2026-08-31 20:48:09] operator / voice_transcript_partial / voice: jupiter to watch
  meta: kind=partial | timestamp=1788180489.626916 | source=vosk | rms=222 | updated_at=1788180489.5794287 | frequency_hz=206.3
- [2026-08-31 20:48:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180489.8291502 | source=vosk | rms=253 | updated_at=1788180489.8291502 | frequency_hz=206.3
- [2026-08-31 20:48:09] operator / voice_transcript_partial / voice: what's cool about
  meta: kind=partial | timestamp=1788180489.8900366 | source=vosk | rms=253 | updated_at=1788180489.8291502 | frequency_hz=206.3
- [2026-08-31 20:48:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180490.0791523 | source=vosk | rms=158 | updated_at=1788180490.0791523 | frequency_hz=206.3
- [2026-08-31 20:48:10] operator / voice_transcript_partial / voice: jupiter to watch global
  meta: kind=partial | timestamp=1788180490.1213274 | source=vosk | rms=158 | updated_at=1788180490.0791523 | frequency_hz=206.3
- [2026-08-31 20:48:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180490.329154 | source=vosk | rms=212 | updated_at=1788180490.329154 | frequency_hz=206.3
- [2026-08-31 20:48:10] operator / voice_transcript_partial / voice: what's cool about
  meta: kind=partial | timestamp=1788180490.3638217 | source=vosk | rms=212 | updated_at=1788180490.329154 | frequency_hz=206.3
- [2026-08-31 20:48:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180490.5794501 | source=vosk | rms=807 | updated_at=1788180490.5794501 | frequency_hz=206.3
- [2026-08-31 20:48:10] operator / voice_transcript_final / voice: jupiter to watch global market
  meta: kind=final | timestamp=1788180490.9280717 | source=final | rms=807 | updated_at=1788180490.5794501 | frequency_hz=206.3
- [2026-08-31 20:48:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180491.043718 | source=vosk | rms=807 | updated_at=1788180490.5794501 | frequency_hz=206.3
- [2026-08-31 20:48:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180491.043718 | source=vosk | rms=807 | updated_at=1788180490.5794501 | frequency_hz=206.3
- [2026-08-31 20:48:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180491.5785453 | source=vosk | rms=256 | updated_at=1788180491.0789156 | frequency_hz=206.3
- [2026-08-31 20:48:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180492.8287675 | source=vosk | rms=258 | updated_at=1788180492.8287675 | frequency_hz=206.3
- [2026-08-31 20:48:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180493.3295639 | source=vosk | rms=258 | updated_at=1788180492.8287675 | frequency_hz=206.3
- [2026-08-31 20:48:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180493.828204 | source=vosk | rms=623 | updated_at=1788180493.828204 | frequency_hz=206.3
- [2026-08-31 20:48:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180494.8287048 | source=vosk | rms=184 | updated_at=1788180494.3286808 | frequency_hz=206.3
- [2026-08-31 20:48:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180495.3290935 | source=vosk | rms=823 | updated_at=1788180495.3290935 | frequency_hz=206.3
- [2026-08-31 20:48:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180496.5800948 | source=vosk | rms=1201 | updated_at=1788180496.0791826 | frequency_hz=206.3
- [2026-08-31 20:48:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180497.5793948 | source=vosk | rms=254 | updated_at=1788180497.5793948 | frequency_hz=206.3
- [2026-08-31 20:48:18] operator / voice_transcript_partial / voice: album
  meta: kind=partial | timestamp=1788180498.6561801 | source=vosk | rms=567 | updated_at=1788180498.0791442 | frequency_hz=206.3
- [2026-08-31 20:48:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180498.8290899 | source=vosk | rms=372 | updated_at=1788180498.8290899 | frequency_hz=206.3
- [2026-08-31 20:48:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180499.329604 | source=vosk | rms=372 | updated_at=1788180498.8290899 | frequency_hz=206.3
- [2026-08-31 20:48:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180499.580204 | source=vosk | rms=372 | updated_at=1788180498.8290899 | frequency_hz=206.3
- [2026-08-31 20:48:20] operator / voice_transcript_final / voice: album
  meta: kind=final | timestamp=1788180500.821887 | source=final | rms=244 | updated_at=1788180500.0793216 | frequency_hz=206.3
- [2026-08-31 20:48:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180500.859715 | source=vosk | rms=259 | updated_at=1788180500.859715 | frequency_hz=206.3
- [2026-08-31 20:48:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180501.328825 | source=vosk | rms=259 | updated_at=1788180500.859715 | frequency_hz=206.3
- [2026-08-31 20:48:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180503.079515 | source=vosk | rms=402 | updated_at=1788180503.079515 | frequency_hz=206.3
- [2026-08-31 20:48:23] operator / voice_transcript_partial / voice: got
  meta: kind=partial | timestamp=1788180503.8588102 | source=vosk | rms=1205 | updated_at=1788180503.579273 | frequency_hz=206.3
- [2026-08-31 20:48:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180504.3296547 | source=vosk | rms=154 | updated_at=1788180504.3296547 | frequency_hz=206.3
- [2026-08-31 20:48:24] operator / voice_transcript_partial / voice: not knowing
  meta: kind=partial | timestamp=1788180504.3559678 | source=vosk | rms=154 | updated_at=1788180504.3296547 | frequency_hz=206.3
- [2026-08-31 20:48:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180504.5801787 | source=vosk | rms=290 | updated_at=1788180504.5801787 | frequency_hz=206.3
- [2026-08-31 20:48:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180505.0796783 | source=vosk | rms=290 | updated_at=1788180504.5801787 | frequency_hz=206.3
- [2026-08-31 20:48:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180507.8295133 | source=vosk | rms=172 | updated_at=1788180507.8295133 | frequency_hz=206.3
- [2026-08-31 20:48:27] operator / voice_transcript_partial / voice: got know when he got
  meta: kind=partial | timestamp=1788180507.8704474 | source=vosk | rms=172 | updated_at=1788180507.8295133 | frequency_hz=206.3
- [2026-08-31 20:48:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180508.329631 | source=vosk | rms=172 | updated_at=1788180507.8295133 | frequency_hz=206.3
- [2026-08-31 20:48:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180509.3294349 | source=vosk | rms=172 | updated_at=1788180507.8295133 | frequency_hz=206.3
- [2026-08-31 20:48:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180509.8296177 | source=vosk | rms=613 | updated_at=1788180509.8296177 | frequency_hz=206.3
- [2026-08-31 20:48:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180510.0790765 | source=vosk | rms=220 | updated_at=1788180510.0790765 | frequency_hz=206.3
- [2026-08-31 20:48:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180510.5796196 | source=vosk | rms=220 | updated_at=1788180510.0790765 | frequency_hz=206.3
- [2026-08-31 20:48:30] operator / voice_transcript_final / voice: got know when he got it
  meta: kind=final | timestamp=1788180510.8725872 | source=final | rms=220 | updated_at=1788180510.0790765 | frequency_hz=206.3
- [2026-08-31 20:48:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180511.0034328 | source=vosk | rms=220 | updated_at=1788180510.0790765 | frequency_hz=206.3
- [2026-08-31 20:48:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180512.5795882 | source=vosk | rms=220 | updated_at=1788180510.0790765 | frequency_hz=206.3
- [2026-08-31 20:48:33] operator / voice_transcript_partial / voice: it's
  meta: kind=partial | timestamp=1788180513.6114752 | source=vosk | rms=147 | updated_at=1788180512.8295465 | frequency_hz=206.3
- [2026-08-31 20:48:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180514.0795367 | source=vosk | rms=147 | updated_at=1788180512.8295465 | frequency_hz=206.3
- [2026-08-31 20:48:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180514.5805194 | source=vosk | rms=147 | updated_at=1788180512.8295465 | frequency_hz=206.3
- [2026-08-31 20:48:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180515.0800548 | source=vosk | rms=147 | updated_at=1788180512.8295465 | frequency_hz=206.3
- [2026-08-31 20:48:35] operator / voice_transcript_final / voice: it s
  meta: kind=final | timestamp=1788180515.9766593 | source=final | rms=147 | updated_at=1788180512.8295465 | frequency_hz=206.3
- [2026-08-31 20:48:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180516.0086987 | source=vosk | rms=147 | updated_at=1788180512.8295465 | frequency_hz=206.3
- [2026-08-31 20:48:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180516.0797517 | source=vosk | rms=302 | updated_at=1788180516.0797517 | frequency_hz=206.3
- [2026-08-31 20:48:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180519.5796719 | source=vosk | rms=190 | updated_at=1788180518.8296368 | frequency_hz=206.3
- [2026-08-31 20:48:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180519.829538 | source=vosk | rms=202 | updated_at=1788180519.829538 | frequency_hz=206.3
- [2026-08-31 20:48:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180521.0798454 | source=vosk | rms=359 | updated_at=1788180520.5806432 | frequency_hz=206.3
- [2026-08-31 20:48:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180521.329227 | source=vosk | rms=436 | updated_at=1788180521.329227 | frequency_hz=206.3
- [2026-08-31 20:48:41] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1788180521.613806 | source=vosk | rms=272 | updated_at=1788180521.5795288 | frequency_hz=206.3
- [2026-08-31 20:48:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180522.0792844 | source=vosk | rms=272 | updated_at=1788180521.5795288 | frequency_hz=206.3
- [2026-08-31 20:48:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180522.3291655 | source=vosk | rms=182 | updated_at=1788180522.3291655 | frequency_hz=206.3
- [2026-08-31 20:48:42] operator / voice_transcript_partial / voice: a representative
  meta: kind=partial | timestamp=1788180522.3866224 | source=vosk | rms=182 | updated_at=1788180522.3291655 | frequency_hz=206.3
- [2026-08-31 20:48:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180522.5796459 | source=vosk | rms=182 | updated_at=1788180522.3291655 | frequency_hz=206.3
- [2026-08-31 20:48:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180523.0797153 | source=vosk | rms=182 | updated_at=1788180522.3291655 | frequency_hz=206.3
- [2026-08-31 20:48:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180523.3294597 | source=vosk | rms=182 | updated_at=1788180522.3291655 | frequency_hz=206.3
- [2026-08-31 20:48:43] operator / voice_transcript_partial / voice: of representatives that
  meta: kind=partial | timestamp=1788180523.3499925 | source=vosk | rms=182 | updated_at=1788180522.3291655 | frequency_hz=206.3
- [2026-08-31 20:48:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180523.8291736 | source=vosk | rms=182 | updated_at=1788180522.3291655 | frequency_hz=206.3
- [2026-08-31 20:48:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180524.0793288 | source=vosk | rms=182 | updated_at=1788180522.3291655 | frequency_hz=206.3
- [2026-08-31 20:48:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180524.329322 | source=vosk | rms=182 | updated_at=1788180522.3291655 | frequency_hz=206.3
- [2026-08-31 20:48:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180524.5906746 | source=vosk | rms=182 | updated_at=1788180522.3291655 | frequency_hz=206.3
- [2026-08-31 20:48:45] operator / voice_transcript_final / voice: of representatives
  meta: kind=final | timestamp=1788180525.5798528 | source=final | rms=182 | updated_at=1788180522.3291655 | frequency_hz=206.3
- [2026-08-31 20:48:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180525.6294098 | source=vosk | rms=182 | updated_at=1788180522.3291655 | frequency_hz=206.3
- [2026-08-31 20:48:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180525.6294098 | source=vosk | rms=182 | updated_at=1788180522.3291655 | frequency_hz=206.3
- [2026-08-31 20:48:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180526.081121 | source=vosk | rms=154 | updated_at=1788180525.6407712 | frequency_hz=206.3
- [2026-08-31 20:48:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180526.3295352 | source=vosk | rms=154 | updated_at=1788180525.6407712 | frequency_hz=206.3
- [2026-08-31 20:48:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180528.3892684 | source=vosk | rms=143 | updated_at=1788180527.6399524 | frequency_hz=206.3
- [2026-08-31 20:48:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180529.1399167 | source=vosk | rms=180 | updated_at=1788180529.1399167 | frequency_hz=206.3
- [2026-08-31 20:48:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180530.3895042 | source=vosk | rms=283 | updated_at=1788180529.889674 | frequency_hz=206.3
- [2026-08-31 20:48:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180530.640203 | source=vosk | rms=283 | updated_at=1788180529.889674 | frequency_hz=206.3
- [2026-08-31 20:48:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180531.889367 | source=vosk | rms=283 | updated_at=1788180529.889674 | frequency_hz=206.3
- [2026-08-31 20:48:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180532.1402724 | source=vosk | rms=283 | updated_at=1788180529.889674 | frequency_hz=206.3
- [2026-08-31 20:48:53] operator / voice_transcript_partial / voice: you don't
  meta: kind=partial | timestamp=1788180533.176633 | source=vosk | rms=200 | updated_at=1788180533.1404855 | frequency_hz=206.3
- [2026-08-31 20:48:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180533.3931496 | source=vosk | rms=193 | updated_at=1788180533.3931496 | frequency_hz=206.3
- [2026-08-31 20:48:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180533.6395013 | source=vosk | rms=182 | updated_at=1788180533.6395013 | frequency_hz=206.3
- [2026-08-31 20:48:53] operator / voice_transcript_partial / voice: you don't on
  meta: kind=partial | timestamp=1788180533.673279 | source=vosk | rms=182 | updated_at=1788180533.6395013 | frequency_hz=206.3
- [2026-08-31 20:48:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180533.8899717 | source=vosk | rms=220 | updated_at=1788180533.8899717 | frequency_hz=206.3
- [2026-08-31 20:48:53] operator / voice_transcript_partial / voice: you don't on computers will
  meta: kind=partial | timestamp=1788180533.953263 | source=vosk | rms=220 | updated_at=1788180533.8899717 | frequency_hz=206.3
- [2026-08-31 20:48:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180534.141031 | source=vosk | rms=182 | updated_at=1788180534.141031 | frequency_hz=206.3
- [2026-08-31 20:48:54] operator / voice_transcript_partial / voice: you don't compete with
  meta: kind=partial | timestamp=1788180534.1873214 | source=vosk | rms=182 | updated_at=1788180534.141031 | frequency_hz=206.3
- [2026-08-31 20:48:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180534.4164054 | source=vosk | rms=420 | updated_at=1788180534.4164054 | frequency_hz=206.3
- [2026-08-31 20:48:54] operator / voice_transcript_partial / voice: you don't on computers will
  meta: kind=partial | timestamp=1788180534.4464517 | source=vosk | rms=420 | updated_at=1788180534.4164054 | frequency_hz=206.3
- [2026-08-31 20:48:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180534.6404903 | source=vosk | rms=346 | updated_at=1788180534.639933 | frequency_hz=206.3
- [2026-08-31 20:48:54] operator / voice_transcript_partial / voice: you don't on computers will determine
  meta: kind=partial | timestamp=1788180534.664602 | source=vosk | rms=346 | updated_at=1788180534.639933 | frequency_hz=206.3
- [2026-08-31 20:48:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180534.8892684 | source=vosk | rms=244 | updated_at=1788180534.8892684 | frequency_hz=206.3
- [2026-08-31 20:48:54] operator / voice_transcript_partial / voice: you don't on computers will deter you
  meta: kind=partial | timestamp=1788180534.9152143 | source=vosk | rms=244 | updated_at=1788180534.8892684 | frequency_hz=206.3
- [2026-08-31 20:48:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180535.3900578 | source=vosk | rms=235 | updated_at=1788180535.3900578 | frequency_hz=206.3
- [2026-08-31 20:48:55] operator / voice_transcript_partial / voice: you don't compete with did too young
  meta: kind=partial | timestamp=1788180535.4187305 | source=vosk | rms=235 | updated_at=1788180535.3900578 | frequency_hz=206.3
- [2026-08-31 20:48:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180535.8900523 | source=vosk | rms=235 | updated_at=1788180535.3900578 | frequency_hz=206.3
- [2026-08-31 20:48:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180536.140428 | source=vosk | rms=184 | updated_at=1788180536.140428 | frequency_hz=206.3
- [2026-08-31 20:48:56] operator / voice_transcript_partial / voice: you don't on computers will deter you don't
  meta: kind=partial | timestamp=1788180536.1593308 | source=vosk | rms=184 | updated_at=1788180536.140428 | frequency_hz=206.3
- [2026-08-31 20:48:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180536.6403863 | source=vosk | rms=184 | updated_at=1788180536.140428 | frequency_hz=206.3
- [2026-08-31 20:48:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180537.1396754 | source=vosk | rms=139 | updated_at=1788180537.1396754 | frequency_hz=206.3
- [2026-08-31 20:48:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180537.390517 | source=vosk | rms=358 | updated_at=1788180537.390517 | frequency_hz=206.3
- [2026-08-31 20:48:57] operator / voice_transcript_partial / voice: you don't on computers will deter you don't have
  meta: kind=partial | timestamp=1788180537.4116716 | source=vosk | rms=358 | updated_at=1788180537.390517 | frequency_hz=206.3
- [2026-08-31 20:48:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180537.63902 | source=vosk | rms=268 | updated_at=1788180537.63902 | frequency_hz=206.3
- [2026-08-31 20:48:57] operator / voice_transcript_final / voice: if you don t on computers when did too young
  meta: kind=final | timestamp=1788180537.9340887 | source=final | rms=268 | updated_at=1788180537.63902 | frequency_hz=206.3
- [2026-08-31 20:48:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180538.0606556 | source=vosk | rms=268 | updated_at=1788180537.63902 | frequency_hz=206.3
- [2026-08-31 20:48:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180538.0606556 | source=vosk | rms=246 | updated_at=1788180538.0606556 | frequency_hz=206.3
- [2026-08-31 20:49:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180541.3897092 | source=vosk | rms=270 | updated_at=1788180540.8959591 | frequency_hz=206.3
- [2026-08-31 20:49:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180541.8901486 | source=vosk | rms=227 | updated_at=1788180541.8901486 | frequency_hz=206.3
- [2026-08-31 20:49:05] operator / voice_transcript_partial / voice: my
  meta: kind=partial | timestamp=1788180545.6611876 | source=vosk | rms=629 | updated_at=1788180545.639513 | frequency_hz=206.3
- [2026-08-31 20:49:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180545.8898942 | source=vosk | rms=1110 | updated_at=1788180545.8898942 | frequency_hz=206.3
- [2026-08-31 20:49:05] operator / voice_transcript_partial / voice: metropolis
  meta: kind=partial | timestamp=1788180545.9256988 | source=vosk | rms=1110 | updated_at=1788180545.8898942 | frequency_hz=206.3
- [2026-08-31 20:49:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180546.1401427 | source=vosk | rms=1204 | updated_at=1788180546.1401427 | frequency_hz=206.3
- [2026-08-31 20:49:06] operator / voice_transcript_partial / voice: my political
  meta: kind=partial | timestamp=1788180546.1581674 | source=vosk | rms=1204 | updated_at=1788180546.1401427 | frequency_hz=206.3
- [2026-08-31 20:49:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180546.3938968 | source=vosk | rms=1204 | updated_at=1788180546.3938968 | frequency_hz=206.3
- [2026-08-31 20:49:06] operator / voice_transcript_partial / voice: my top a little
  meta: kind=partial | timestamp=1788180546.4363058 | source=vosk | rms=1204 | updated_at=1788180546.3938968 | frequency_hz=206.3
- [2026-08-31 20:49:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180546.6401596 | source=vosk | rms=186 | updated_at=1788180546.6401596 | frequency_hz=206.3
- [2026-08-31 20:49:06] operator / voice_transcript_partial / voice: my top a little luck
  meta: kind=partial | timestamp=1788180546.6901793 | source=vosk | rms=186 | updated_at=1788180546.6401596 | frequency_hz=206.3
- [2026-08-31 20:49:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180547.1402783 | source=vosk | rms=302 | updated_at=1788180547.1402783 | frequency_hz=206.3
- [2026-08-31 20:49:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180547.3904843 | source=vosk | rms=1061 | updated_at=1788180547.3904843 | frequency_hz=206.3
- [2026-08-31 20:49:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180547.6405685 | source=vosk | rms=655 | updated_at=1788180547.6405685 | frequency_hz=206.3
- [2026-08-31 20:49:07] operator / voice_transcript_partial / voice: my top a little luck it didn't
  meta: kind=partial | timestamp=1788180547.6733277 | source=vosk | rms=655 | updated_at=1788180547.6405685 | frequency_hz=206.3
- [2026-08-31 20:49:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180547.8902287 | source=vosk | rms=1136 | updated_at=1788180547.8902287 | frequency_hz=206.3
- [2026-08-31 20:49:07] operator / voice_transcript_partial / voice: my top a little luck
  meta: kind=partial | timestamp=1788180547.9793754 | source=vosk | rms=1136 | updated_at=1788180547.8902287 | frequency_hz=206.3
- [2026-08-31 20:49:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180548.1402938 | source=vosk | rms=712 | updated_at=1788180548.1402938 | frequency_hz=206.3
- [2026-08-31 20:49:08] operator / voice_transcript_partial / voice: my top a little luck to tell you the
  meta: kind=partial | timestamp=1788180548.1929076 | source=vosk | rms=712 | updated_at=1788180548.1402938 | frequency_hz=206.3
- [2026-08-31 20:49:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180548.3898857 | source=vosk | rms=320 | updated_at=1788180548.3898857 | frequency_hz=206.3
- [2026-08-31 20:49:08] operator / voice_transcript_partial / voice: my top a little luck the theory of gravity
  meta: kind=partial | timestamp=1788180548.4444351 | source=vosk | rms=320 | updated_at=1788180548.3898857 | frequency_hz=206.3
- [2026-08-31 20:49:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180548.6405911 | source=vosk | rms=281 | updated_at=1788180548.6405911 | frequency_hz=206.3
- [2026-08-31 20:49:08] operator / voice_transcript_partial / voice: my top a little luck the t v a graphic novel
  meta: kind=partial | timestamp=1788180548.6537426 | source=vosk | rms=281 | updated_at=1788180548.6405911 | frequency_hz=206.3
- [2026-08-31 20:49:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180548.8910244 | source=vosk | rms=281 | updated_at=1788180548.8910244 | frequency_hz=206.3
- [2026-08-31 20:49:08] operator / voice_transcript_partial / voice: my top a little luck to tell you the graphic novels
  meta: kind=partial | timestamp=1788180548.9023523 | source=vosk | rms=281 | updated_at=1788180548.8910244 | frequency_hz=206.3
- [2026-08-31 20:49:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180549.14037 | source=vosk | rms=176 | updated_at=1788180549.14037 | frequency_hz=206.3
- [2026-08-31 20:49:09] operator / voice_transcript_partial / voice: my top a little luck to tell you the graphic novels including
  meta: kind=partial | timestamp=1788180549.1796982 | source=vosk | rms=176 | updated_at=1788180549.14037 | frequency_hz=206.3
- [2026-08-31 20:49:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180549.3909755 | source=vosk | rms=710 | updated_at=1788180549.3899753 | frequency_hz=206.3
- [2026-08-31 20:49:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180549.640646 | source=vosk | rms=1206 | updated_at=1788180549.640646 | frequency_hz=206.3
- [2026-08-31 20:49:09] operator / voice_transcript_partial / voice: my top a little luck to tell you the graphic novels income was
  meta: kind=partial | timestamp=1788180549.6723945 | source=vosk | rms=1206 | updated_at=1788180549.640646 | frequency_hz=206.3
- [2026-08-31 20:49:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180549.8901315 | source=vosk | rms=1201 | updated_at=1788180549.8901315 | frequency_hz=206.3
- [2026-08-31 20:49:09] operator / voice_transcript_partial / voice: my top a little luck to tell you the graphic novels income or
  meta: kind=partial | timestamp=1788180549.9848785 | source=vosk | rms=1201 | updated_at=1788180549.8901315 | frequency_hz=206.3
- [2026-08-31 20:49:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180550.172396 | source=vosk | rms=1204 | updated_at=1788180550.172396 | frequency_hz=206.3
- [2026-08-31 20:49:10] operator / voice_transcript_partial / voice: my top a little luck to tell you the graphic novels income or problem
  meta: kind=partial | timestamp=1788180550.2199652 | source=vosk | rms=1204 | updated_at=1788180550.172396 | frequency_hz=206.3
- [2026-08-31 20:49:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180550.3896968 | source=vosk | rms=826 | updated_at=1788180550.3896968 | frequency_hz=206.3
- [2026-08-31 20:49:10] operator / voice_transcript_partial / voice: my top a little luck to tell you the graphic novels are probably going
  meta: kind=partial | timestamp=1788180550.445117 | source=vosk | rms=826 | updated_at=1788180550.3896968 | frequency_hz=206.3
- [2026-08-31 20:49:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180550.6404123 | source=vosk | rms=1202 | updated_at=1788180550.6404123 | frequency_hz=206.3
- [2026-08-31 20:49:10] operator / voice_transcript_partial / voice: my top a little luck to tell you the graphic novels income or probably
  meta: kind=partial | timestamp=1788180550.7014284 | source=vosk | rms=1202 | updated_at=1788180550.6404123 | frequency_hz=206.3
- [2026-08-31 20:49:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180550.8897495 | source=vosk | rms=1014 | updated_at=1788180550.8897495 | frequency_hz=206.3
- [2026-08-31 20:49:10] operator / voice_transcript_partial / voice: my top a little luck to tell you the graphic novels income or probably got
  meta: kind=partial | timestamp=1788180550.916075 | source=vosk | rms=1014 | updated_at=1788180550.8897495 | frequency_hz=206.3
- [2026-08-31 20:49:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180551.1401916 | source=vosk | rms=344 | updated_at=1788180551.1401916 | frequency_hz=206.3
- [2026-08-31 20:49:11] operator / voice_transcript_partial / voice: my top a little luck to tell you the graphic novels income or probably got no
  meta: kind=partial | timestamp=1788180551.1715198 | source=vosk | rms=344 | updated_at=1788180551.1401916 | frequency_hz=206.3
- [2026-08-31 20:49:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180551.6405253 | source=vosk | rms=344 | updated_at=1788180551.1401916 | frequency_hz=206.3
- [2026-08-31 20:49:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180554.3942752 | source=vosk | rms=529 | updated_at=1788180554.3942752 | frequency_hz=206.3
- [2026-08-31 20:49:14] operator / voice_transcript_partial / voice: my top a little luck to tell you the graphic novels income or problem is i'm gonna go
  meta: kind=partial | timestamp=1788180554.4224918 | source=vosk | rms=529 | updated_at=1788180554.3942752 | frequency_hz=206.3
- [2026-08-31 20:49:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180554.6405072 | source=vosk | rms=529 | updated_at=1788180554.3942752 | frequency_hz=206.3
- [2026-08-31 20:49:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180555.1406863 | source=vosk | rms=529 | updated_at=1788180554.3942752 | frequency_hz=206.3
- [2026-08-31 20:49:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180555.640576 | source=vosk | rms=529 | updated_at=1788180554.3942752 | frequency_hz=206.3
- [2026-08-31 20:49:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180556.6495512 | source=vosk | rms=579 | updated_at=1788180556.6495512 | frequency_hz=206.3
- [2026-08-31 20:49:16] operator / voice_transcript_final / voice: my top a little luck the a graphic novels income because problem probably got gonna go
  meta: kind=final | timestamp=1788180556.9437196 | source=final | rms=579 | updated_at=1788180556.6495512 | frequency_hz=206.3
- [2026-08-31 20:49:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180557.3127093 | source=vosk | rms=579 | updated_at=1788180556.6495512 | frequency_hz=206.3
- [2026-08-31 20:49:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180557.3127093 | source=vosk | rms=1205 | updated_at=1788180557.3127093 | frequency_hz=206.3
- [2026-08-31 20:49:17] operator / voice_transcript_partial / voice: from the
  meta: kind=partial | timestamp=1788180557.917451 | source=vosk | rms=398 | updated_at=1788180557.8914165 | frequency_hz=206.3
- [2026-08-31 20:49:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180558.1399202 | source=vosk | rms=433 | updated_at=1788180558.1399202 | frequency_hz=206.3
- [2026-08-31 20:49:18] operator / voice_transcript_partial / voice: from the get him
  meta: kind=partial | timestamp=1788180558.2007701 | source=vosk | rms=433 | updated_at=1788180558.1399202 | frequency_hz=206.3
- [2026-08-31 20:49:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180558.3929765 | source=vosk | rms=347 | updated_at=1788180558.3929765 | frequency_hz=206.3
- [2026-08-31 20:49:18] operator / voice_transcript_partial / voice: together these
  meta: kind=partial | timestamp=1788180558.4422743 | source=vosk | rms=347 | updated_at=1788180558.3929765 | frequency_hz=206.3
- [2026-08-31 20:49:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180558.6404314 | source=vosk | rms=347 | updated_at=1788180558.3929765 | frequency_hz=206.3
- [2026-08-31 20:49:18] operator / voice_transcript_partial / voice: together these insects
  meta: kind=partial | timestamp=1788180558.7215476 | source=vosk | rms=347 | updated_at=1788180558.3929765 | frequency_hz=206.3
- [2026-08-31 20:49:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180559.1407297 | source=vosk | rms=347 | updated_at=1788180558.3929765 | frequency_hz=206.3
- [2026-08-31 20:49:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180559.6408412 | source=vosk | rms=347 | updated_at=1788180558.3929765 | frequency_hz=206.3
- [2026-08-31 20:49:19] operator / voice_transcript_partial / voice: together with insect
  meta: kind=partial | timestamp=1788180559.689141 | source=vosk | rms=347 | updated_at=1788180558.3929765 | frequency_hz=206.3
- [2026-08-31 20:49:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180559.8963776 | source=vosk | rms=393 | updated_at=1788180559.8963776 | frequency_hz=206.3
- [2026-08-31 20:49:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180560.1445637 | source=vosk | rms=535 | updated_at=1788180560.1445637 | frequency_hz=206.3
- [2026-08-31 20:49:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180560.391077 | source=vosk | rms=1202 | updated_at=1788180560.390562 | frequency_hz=206.3
- [2026-08-31 20:49:20] operator / voice_transcript_final / voice: together with insect
  meta: kind=final | timestamp=1788180560.6795332 | source=final | rms=1202 | updated_at=1788180560.390562 | frequency_hz=206.3
- [2026-08-31 20:49:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180560.7863505 | source=vosk | rms=1202 | updated_at=1788180560.390562 | frequency_hz=206.3
- [2026-08-31 20:49:23] operator / voice_transcript_partial / voice: if
  meta: kind=partial | timestamp=1788180563.2060163 | source=vosk | rms=498 | updated_at=1788180563.1412616 | frequency_hz=206.3
- [2026-08-31 20:49:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180563.3904176 | source=vosk | rms=498 | updated_at=1788180563.1412616 | frequency_hz=206.3
- [2026-08-31 20:49:23] operator / voice_transcript_partial / voice: let me finish
  meta: kind=partial | timestamp=1788180563.443402 | source=vosk | rms=498 | updated_at=1788180563.1412616 | frequency_hz=206.3
- [2026-08-31 20:49:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180563.6461065 | source=vosk | rms=498 | updated_at=1788180563.1412616 | frequency_hz=206.3
- [2026-08-31 20:49:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180564.1408436 | source=vosk | rms=340 | updated_at=1788180564.1408436 | frequency_hz=206.3
- [2026-08-31 20:49:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180564.3906028 | source=vosk | rms=340 | updated_at=1788180564.1408436 | frequency_hz=206.3
- [2026-08-31 20:49:24] operator / voice_transcript_final / voice: let me finish
  meta: kind=final | timestamp=1788180564.7236316 | source=final | rms=340 | updated_at=1788180564.1408436 | frequency_hz=206.3
- [2026-08-31 20:49:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180564.8295178 | source=vosk | rms=340 | updated_at=1788180564.1408436 | frequency_hz=206.3
- [2026-08-31 20:49:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180564.8295178 | source=vosk | rms=340 | updated_at=1788180564.1408436 | frequency_hz=206.3
- [2026-08-31 20:49:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180567.1401207 | source=vosk | rms=424 | updated_at=1788180566.6410265 | frequency_hz=206.3
- [2026-08-31 20:49:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180567.640384 | source=vosk | rms=424 | updated_at=1788180566.6410265 | frequency_hz=206.3
- [2026-08-31 20:49:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180568.3902001 | source=vosk | rms=424 | updated_at=1788180566.6410265 | frequency_hz=206.3
- [2026-08-31 20:49:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180568.641006 | source=vosk | rms=424 | updated_at=1788180566.6410265 | frequency_hz=206.3
- [2026-08-31 20:49:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180569.3902578 | source=vosk | rms=465 | updated_at=1788180568.8907523 | frequency_hz=206.3
- [2026-08-31 20:49:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180569.6727428 | source=vosk | rms=465 | updated_at=1788180568.8907523 | frequency_hz=206.3
- [2026-08-31 20:49:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180572.3903384 | source=vosk | rms=773 | updated_at=1788180571.8907273 | frequency_hz=206.3
- [2026-08-31 20:49:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180572.640931 | source=vosk | rms=416 | updated_at=1788180572.640931 | frequency_hz=206.3
- [2026-08-31 20:49:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180573.890661 | source=vosk | rms=487 | updated_at=1788180573.4181812 | frequency_hz=206.3
- [2026-08-31 20:49:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180574.1403744 | source=vosk | rms=1203 | updated_at=1788180574.1403744 | frequency_hz=206.3
- [2026-08-31 20:49:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180575.1411612 | source=vosk | rms=444 | updated_at=1788180574.3987715 | frequency_hz=206.3
- [2026-08-31 20:49:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180584.390539 | source=vosk | rms=388 | updated_at=1788180584.390539 | frequency_hz=206.3
- [2026-08-31 20:49:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180584.9098349 | source=vosk | rms=388 | updated_at=1788180584.390539 | frequency_hz=206.3
- [2026-08-31 20:49:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180590.8908947 | source=vosk | rms=239 | updated_at=1788180590.8908947 | frequency_hz=206.3
- [2026-08-31 20:49:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180592.1407173 | source=vosk | rms=295 | updated_at=1788180591.6412432 | frequency_hz=206.3
- [2026-08-31 20:49:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180593.403048 | source=vosk | rms=295 | updated_at=1788180591.6412432 | frequency_hz=206.3
- [2026-08-31 20:49:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180593.8911374 | source=vosk | rms=295 | updated_at=1788180591.6412432 | frequency_hz=206.3
- [2026-08-31 20:49:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180594.391387 | source=vosk | rms=295 | updated_at=1788180591.6412432 | frequency_hz=206.3
- [2026-08-31 20:49:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180594.8922276 | source=vosk | rms=295 | updated_at=1788180591.6412432 | frequency_hz=206.3
- [2026-08-31 20:49:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180595.1405818 | source=vosk | rms=283 | updated_at=1788180595.1405818 | frequency_hz=206.3
- [2026-08-31 20:49:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180595.6413376 | source=vosk | rms=283 | updated_at=1788180595.1405818 | frequency_hz=206.3
- [2026-08-31 20:49:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180596.6414735 | source=vosk | rms=272 | updated_at=1788180596.6414735 | frequency_hz=310.0
- [2026-08-31 20:49:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180597.1410186 | source=vosk | rms=272 | updated_at=1788180596.6414735 | frequency_hz=310.0
- [2026-08-31 20:50:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180601.8942928 | source=vosk | rms=272 | updated_at=1788180596.6414735 | frequency_hz=310.0
- [2026-08-31 20:50:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180603.891604 | source=vosk | rms=185 | updated_at=1788180603.4014084 | frequency_hz=310.0
- [2026-08-31 20:50:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180605.6457484 | source=vosk | rms=477 | updated_at=1788180605.6457484 | frequency_hz=310.0
- [2026-08-31 20:50:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180606.8914626 | source=vosk | rms=221 | updated_at=1788180606.391521 | frequency_hz=310.0
- [2026-08-31 20:50:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180607.392313 | source=vosk | rms=267 | updated_at=1788180607.392313 | frequency_hz=310.0
- [2026-08-31 20:50:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180609.1416442 | source=vosk | rms=157 | updated_at=1788180608.6414797 | frequency_hz=310.0
- [2026-08-31 20:50:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180609.3911817 | source=vosk | rms=157 | updated_at=1788180608.6414797 | frequency_hz=310.0
- [2026-08-31 20:50:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180613.141514 | source=vosk | rms=232 | updated_at=1788180612.6683762 | frequency_hz=310.0
- [2026-08-31 20:50:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180613.3911543 | source=vosk | rms=232 | updated_at=1788180612.6683762 | frequency_hz=310.0
- [2026-08-31 20:50:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180614.4111702 | source=vosk | rms=154 | updated_at=1788180613.891614 | frequency_hz=310.0
- [2026-08-31 20:50:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180615.3916137 | source=vosk | rms=406 | updated_at=1788180615.3916137 | frequency_hz=310.0
- [2026-08-31 20:50:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180620.6413453 | source=vosk | rms=404 | updated_at=1788180620.1425636 | frequency_hz=287.6
- [2026-08-31 20:50:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180621.1410556 | source=vosk | rms=130 | updated_at=1788180621.1410556 | frequency_hz=287.6
- [2026-08-31 20:50:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180621.641649 | source=vosk | rms=130 | updated_at=1788180621.1410556 | frequency_hz=287.6
- [2026-08-31 20:50:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180622.8909338 | source=vosk | rms=554 | updated_at=1788180622.8909338 | frequency_hz=287.6
- [2026-08-31 20:50:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180623.6017034 | source=vosk | rms=554 | updated_at=1788180622.8909338 | frequency_hz=287.6
- [2026-08-31 20:50:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180624.3954294 | source=vosk | rms=554 | updated_at=1788180622.8909338 | frequency_hz=287.6
- [2026-08-31 20:50:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180624.891253 | source=vosk | rms=554 | updated_at=1788180622.8909338 | frequency_hz=287.6
- [2026-08-31 20:50:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180627.3129666 | source=vosk | rms=554 | updated_at=1788180622.8909338 | frequency_hz=287.6
- [2026-08-31 20:50:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180628.641147 | source=vosk | rms=493 | updated_at=1788180628.1423373 | frequency_hz=287.6
- [2026-08-31 20:50:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180628.8996842 | source=vosk | rms=335 | updated_at=1788180628.8996842 | frequency_hz=287.6
- [2026-08-31 20:50:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180630.8913336 | source=vosk | rms=256 | updated_at=1788180630.1413932 | frequency_hz=287.6
- [2026-08-31 20:50:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180631.3944378 | source=vosk | rms=256 | updated_at=1788180630.1413932 | frequency_hz=287.6
- [2026-08-31 20:50:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180632.392101 | source=vosk | rms=256 | updated_at=1788180630.1413932 | frequency_hz=287.6
- [2026-08-31 20:50:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180633.6411448 | source=vosk | rms=1151 | updated_at=1788180633.6411448 | frequency_hz=287.6
- [2026-08-31 20:50:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180634.6414168 | source=vosk | rms=173 | updated_at=1788180634.147766 | frequency_hz=287.6
- [2026-08-31 20:50:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180636.970934 | source=vosk | rms=256 | updated_at=1788180636.970934 | frequency_hz=287.6
- [2026-08-31 20:50:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180642.0015624 | source=vosk | rms=1022 | updated_at=1788180641.1422215 | frequency_hz=287.6
- [2026-08-31 20:50:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180642.0015624 | source=vosk | rms=1200 | updated_at=1788180642.0015624 | frequency_hz=287.6
- [2026-08-31 20:50:42] operator / voice_transcript_partial / voice: hello person feels
  meta: kind=partial | timestamp=1788180642.0242505 | source=vosk | rms=1200 | updated_at=1788180642.0015624 | frequency_hz=287.6
- [2026-08-31 20:50:42] operator / voice_transcript_partial / voice: hello person zero
  meta: kind=partial | timestamp=1788180642.043789 | source=vosk | rms=1200 | updated_at=1788180642.0015624 | frequency_hz=287.6
- [2026-08-31 20:50:42] operator / voice_transcript_partial / voice: hello person zero ticked
  meta: kind=partial | timestamp=1788180642.080524 | source=vosk | rms=230 | updated_at=1788180642.043789 | frequency_hz=287.6
- [2026-08-31 20:50:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180643.192279 | source=vosk | rms=206 | updated_at=1788180642.142257 | frequency_hz=287.6
- [2026-08-31 20:50:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180643.4321828 | source=vosk | rms=206 | updated_at=1788180642.142257 | frequency_hz=287.6
- [2026-08-31 20:50:43] operator / voice_transcript_final / voice: hello person zero it
  meta: kind=final | timestamp=1788180643.7133522 | source=final | rms=206 | updated_at=1788180642.142257 | frequency_hz=287.6
- [2026-08-31 20:50:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180644.392654 | source=vosk | rms=206 | updated_at=1788180642.142257 | frequency_hz=287.6
- [2026-08-31 20:50:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180644.392654 | source=vosk | rms=206 | updated_at=1788180642.142257 | frequency_hz=287.6
- [2026-08-31 20:50:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180644.9332619 | source=vosk | rms=317 | updated_at=1788180644.4131808 | frequency_hz=287.6
- [2026-08-31 20:50:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180645.4324436 | source=vosk | rms=317 | updated_at=1788180644.4131808 | frequency_hz=287.6
- [2026-08-31 20:50:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180645.9330385 | source=vosk | rms=317 | updated_at=1788180644.4131808 | frequency_hz=287.6
- [2026-08-31 20:50:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180653.6819327 | source=vosk | rms=302 | updated_at=1788180653.6819327 | frequency_hz=287.6
- [2026-08-31 20:50:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180654.4333842 | source=vosk | rms=415 | updated_at=1788180653.9335532 | frequency_hz=287.6
- [2026-08-31 20:50:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180659.9324708 | source=vosk | rms=543 | updated_at=1788180659.9324708 | frequency_hz=287.6
- [2026-08-31 20:51:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180660.6824825 | source=vosk | rms=224 | updated_at=1788180660.1820989 | frequency_hz=252.7
- [2026-08-31 20:51:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180660.932413 | source=vosk | rms=224 | updated_at=1788180660.1820989 | frequency_hz=252.7
- [2026-08-31 20:51:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180661.431844 | source=vosk | rms=224 | updated_at=1788180660.1820989 | frequency_hz=252.7
- [2026-08-31 20:51:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180661.6822238 | source=vosk | rms=273 | updated_at=1788180661.6822238 | frequency_hz=252.7
- [2026-08-31 20:51:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180662.1822846 | source=vosk | rms=273 | updated_at=1788180661.6822238 | frequency_hz=252.7
- [2026-08-31 20:51:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180663.9327693 | source=vosk | rms=273 | updated_at=1788180661.6822238 | frequency_hz=252.7
- [2026-08-31 20:51:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180664.4322984 | source=vosk | rms=273 | updated_at=1788180661.6822238 | frequency_hz=252.7
- [2026-08-31 20:51:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180664.6829364 | source=vosk | rms=211 | updated_at=1788180664.6829364 | frequency_hz=252.7
- [2026-08-31 20:51:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180665.432575 | source=vosk | rms=179 | updated_at=1788180664.9328244 | frequency_hz=251.8
- [2026-08-31 20:51:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180671.1826186 | source=vosk | rms=179 | updated_at=1788180664.9328244 | frequency_hz=251.8
- [2026-08-31 20:51:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180671.682675 | source=vosk | rms=179 | updated_at=1788180664.9328244 | frequency_hz=251.8
- [2026-08-31 20:51:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180672.9323392 | source=vosk | rms=212 | updated_at=1788180672.9323392 | frequency_hz=251.8
- [2026-08-31 20:51:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180674.1827104 | source=vosk | rms=466 | updated_at=1788180673.18212 | frequency_hz=251.8
- [2026-08-31 20:51:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180674.4359732 | source=vosk | rms=1201 | updated_at=1788180674.4359732 | frequency_hz=251.8
- [2026-08-31 20:51:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180676.4329195 | source=vosk | rms=226 | updated_at=1788180674.9322236 | frequency_hz=251.8
- [2026-08-31 20:51:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180676.9337134 | source=vosk | rms=145 | updated_at=1788180676.9337134 | frequency_hz=251.8
- [2026-08-31 20:51:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180682.4330392 | source=vosk | rms=175 | updated_at=1788180681.4329052 | frequency_hz=251.8
- [2026-08-31 20:51:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180682.7115612 | source=vosk | rms=467 | updated_at=1788180682.7115612 | frequency_hz=251.8
- [2026-08-31 20:51:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180685.6837711 | source=vosk | rms=1203 | updated_at=1788180685.044924 | frequency_hz=251.8
- [2026-08-31 20:51:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180686.1832743 | source=vosk | rms=1203 | updated_at=1788180685.044924 | frequency_hz=251.8
- [2026-08-31 20:51:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180688.182719 | source=vosk | rms=227 | updated_at=1788180687.6826417 | frequency_hz=251.8
- [2026-08-31 20:51:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180688.432454 | source=vosk | rms=156 | updated_at=1788180688.432454 | frequency_hz=251.8
- [2026-08-31 20:51:31] operator / voice_transcript_partial / voice: it
  meta: kind=partial | timestamp=1788180691.1975405 | source=vosk | rms=308 | updated_at=1788180691.1826453 | frequency_hz=251.8
- [2026-08-31 20:51:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180691.6830623 | source=vosk | rms=308 | updated_at=1788180691.1826453 | frequency_hz=251.8
- [2026-08-31 20:51:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180691.934832 | source=vosk | rms=381 | updated_at=1788180691.934832 | frequency_hz=251.8
- [2026-08-31 20:51:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180692.1829877 | source=vosk | rms=150 | updated_at=1788180692.1829877 | frequency_hz=251.8
- [2026-08-31 20:51:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180692.6826959 | source=vosk | rms=150 | updated_at=1788180692.1829877 | frequency_hz=251.8
- [2026-08-31 20:51:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180693.1827328 | source=vosk | rms=162 | updated_at=1788180693.1827328 | frequency_hz=251.8
- [2026-08-31 20:51:33] operator / voice_transcript_final / voice: it
  meta: kind=final | timestamp=1788180693.3901968 | source=final | rms=162 | updated_at=1788180693.1827328 | frequency_hz=251.8
- [2026-08-31 20:51:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180693.683464 | source=vosk | rms=162 | updated_at=1788180693.1827328 | frequency_hz=251.8
- [2026-08-31 20:51:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180697.6853788 | source=vosk | rms=275 | updated_at=1788180697.6853788 | frequency_hz=251.8
- [2026-08-31 20:51:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180699.185712 | source=vosk | rms=442 | updated_at=1788180698.452435 | frequency_hz=251.8
- [2026-08-31 20:51:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180699.4328985 | source=vosk | rms=189 | updated_at=1788180699.4328985 | frequency_hz=251.8
- [2026-08-31 20:51:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180701.9335737 | source=vosk | rms=583 | updated_at=1788180701.433364 | frequency_hz=251.8
- [2026-08-31 20:51:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180702.4328887 | source=vosk | rms=583 | updated_at=1788180701.433364 | frequency_hz=251.8
- [2026-08-31 20:51:42] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1788180702.9427793 | source=vosk | rms=179 | updated_at=1788180702.9327528 | frequency_hz=251.8
- [2026-08-31 20:51:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180703.1830103 | source=vosk | rms=167 | updated_at=1788180703.1830103 | frequency_hz=251.8
- [2026-08-31 20:51:44] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1788180704.396677 | source=final | rms=350 | updated_at=1788180703.9617677 | frequency_hz=251.8
- [2026-08-31 20:51:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180704.435198 | source=vosk | rms=350 | updated_at=1788180703.9617677 | frequency_hz=251.8
- [2026-08-31 20:51:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180704.4367 | source=vosk | rms=350 | updated_at=1788180703.9617677 | frequency_hz=251.8
- [2026-08-31 20:51:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180706.8846855 | source=vosk | rms=189 | updated_at=1788180706.433588 | frequency_hz=251.8
- [2026-08-31 20:51:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180706.9368284 | source=vosk | rms=203 | updated_at=1788180706.9368284 | frequency_hz=251.8
- [2026-08-31 20:51:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180707.6830783 | source=vosk | rms=203 | updated_at=1788180706.9368284 | frequency_hz=251.8
- [2026-08-31 20:51:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180709.1834779 | source=vosk | rms=277 | updated_at=1788180709.1834779 | frequency_hz=251.8
- [2026-08-31 20:51:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180710.3971882 | source=vosk | rms=475 | updated_at=1788180709.6830096 | frequency_hz=251.8
- [2026-08-31 20:51:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180711.683107 | source=vosk | rms=273 | updated_at=1788180711.683107 | frequency_hz=251.8
- [2026-08-31 20:52:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180725.2556279 | source=vosk | rms=289 | updated_at=1788180724.7534177 | frequency_hz=251.8
- [2026-08-31 20:52:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180725.7531533 | source=vosk | rms=249 | updated_at=1788180725.7531533 | frequency_hz=251.8
- [2026-08-31 20:52:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180727.503812 | source=vosk | rms=511 | updated_at=1788180726.753745 | frequency_hz=251.8
- [2026-08-31 20:52:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180732.2549076 | source=vosk | rms=511 | updated_at=1788180726.753745 | frequency_hz=251.8
- [2026-08-31 20:52:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180734.2537138 | source=vosk | rms=511 | updated_at=1788180726.753745 | frequency_hz=251.8
- [2026-08-31 20:52:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180742.754069 | source=vosk | rms=511 | updated_at=1788180726.753745 | frequency_hz=251.8
- [2026-08-31 20:52:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180743.2534232 | source=vosk | rms=511 | updated_at=1788180726.753745 | frequency_hz=251.8
- [2026-08-31 20:52:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180744.7543843 | source=vosk | rms=420 | updated_at=1788180744.7543843 | frequency_hz=251.8
- [2026-08-31 20:52:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180745.503456 | source=vosk | rms=406 | updated_at=1788180745.015215 | frequency_hz=251.8
- [2026-08-31 20:52:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180747.50511 | source=vosk | rms=361 | updated_at=1788180747.50511 | frequency_hz=251.8
- [2026-08-31 20:52:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180748.004065 | source=vosk | rms=361 | updated_at=1788180747.50511 | frequency_hz=251.8
- [2026-08-31 20:52:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180748.2543972 | source=vosk | rms=361 | updated_at=1788180747.50511 | frequency_hz=251.8
- [2026-08-31 20:52:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180748.7537613 | source=vosk | rms=361 | updated_at=1788180747.50511 | frequency_hz=251.8
- [2026-08-31 20:52:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180750.0043297 | source=vosk | rms=361 | updated_at=1788180747.50511 | frequency_hz=251.8
- [2026-08-31 20:52:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180750.754503 | source=vosk | rms=361 | updated_at=1788180747.50511 | frequency_hz=251.8
- [2026-08-31 20:52:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180751.7561197 | source=vosk | rms=643 | updated_at=1788180751.7561197 | frequency_hz=251.8
- [2026-08-31 20:52:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180752.254325 | source=vosk | rms=643 | updated_at=1788180751.7561197 | frequency_hz=251.8
- [2026-08-31 20:52:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180756.530057 | source=vosk | rms=643 | updated_at=1788180751.7561197 | frequency_hz=251.8
- [2026-08-31 20:52:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180757.2541907 | source=vosk | rms=643 | updated_at=1788180751.7561197 | frequency_hz=251.8
- [2026-08-31 20:52:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180762.2146425 | source=vosk | rms=220 | updated_at=1788180762.2146425 | frequency_hz=164.0
- [2026-08-31 20:52:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180763.214859 | source=vosk | rms=692 | updated_at=1788180762.7144349 | frequency_hz=183.6
- [2026-08-31 20:52:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180763.4640927 | source=vosk | rms=387 | updated_at=1788180763.4640927 | frequency_hz=183.6
- [2026-08-31 20:52:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180767.2142284 | source=vosk | rms=190 | updated_at=1788180766.2166185 | frequency_hz=183.6
- [2026-08-31 20:52:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180767.4964042 | source=vosk | rms=331 | updated_at=1788180767.4964042 | frequency_hz=183.6
- [2026-08-31 20:52:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180768.4645429 | source=vosk | rms=331 | updated_at=1788180767.4964042 | frequency_hz=183.6
- [2026-08-31 20:52:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180769.463945 | source=vosk | rms=331 | updated_at=1788180767.4964042 | frequency_hz=183.6
- [2026-08-31 20:52:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180772.0639892 | source=vosk | rms=185 | updated_at=1788180771.3242216 | frequency_hz=183.6
- [2026-08-31 20:52:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180772.3149784 | source=vosk | rms=185 | updated_at=1788180771.3242216 | frequency_hz=183.6
- [2026-08-31 20:52:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180774.3165562 | source=vosk | rms=191 | updated_at=1788180773.8147655 | frequency_hz=183.6
- [2026-08-31 20:52:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180775.0648885 | source=vosk | rms=175 | updated_at=1788180775.0648885 | frequency_hz=183.6
- [2026-08-31 20:52:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180776.0662277 | source=vosk | rms=175 | updated_at=1788180775.0648885 | frequency_hz=183.6
- [2026-08-31 20:53:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180780.0652425 | source=vosk | rms=175 | updated_at=1788180775.0648885 | frequency_hz=183.6
- [2026-08-31 20:53:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180780.5643375 | source=vosk | rms=175 | updated_at=1788180775.0648885 | frequency_hz=183.6
- [2026-08-31 20:53:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180781.72294 | source=vosk | rms=175 | updated_at=1788180775.0648885 | frequency_hz=183.6
- [2026-08-31 20:53:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180782.3160307 | source=vosk | rms=161 | updated_at=1788180781.8147094 | frequency_hz=183.6
- [2026-08-31 20:53:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180783.5657537 | source=vosk | rms=168 | updated_at=1788180783.5657537 | frequency_hz=183.6
- [2026-08-31 20:53:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180787.8142598 | source=vosk | rms=160 | updated_at=1788180787.363116 | frequency_hz=183.6
- [2026-08-31 20:53:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180788.3157873 | source=vosk | rms=160 | updated_at=1788180787.363116 | frequency_hz=183.6
- [2026-08-31 20:53:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180793.8151686 | source=vosk | rms=231 | updated_at=1788180793.3240178 | frequency_hz=183.6
- [2026-08-31 20:53:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180805.315069 | source=vosk | rms=158 | updated_at=1788180805.315069 | frequency_hz=183.6
- [2026-08-31 20:53:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180805.8149195 | source=vosk | rms=158 | updated_at=1788180805.315069 | frequency_hz=183.6
- [2026-08-31 20:53:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180807.0653148 | source=vosk | rms=158 | updated_at=1788180805.315069 | frequency_hz=183.6
- [2026-08-31 20:53:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180807.8152022 | source=vosk | rms=468 | updated_at=1788180807.3157942 | frequency_hz=183.6
- [2026-08-31 20:53:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180811.0655217 | source=vosk | rms=468 | updated_at=1788180807.3157942 | frequency_hz=183.6
- [2026-08-31 20:53:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180812.3151202 | source=vosk | rms=468 | updated_at=1788180807.3157942 | frequency_hz=183.6
- [2026-08-31 20:53:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180814.3154497 | source=vosk | rms=468 | updated_at=1788180807.3157942 | frequency_hz=183.6
- [2026-08-31 20:53:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180816.0655475 | source=vosk | rms=468 | updated_at=1788180807.3157942 | frequency_hz=183.6
- [2026-08-31 20:53:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180816.8315063 | source=vosk | rms=468 | updated_at=1788180807.3157942 | frequency_hz=183.6
- [2026-08-31 20:53:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180817.5654678 | source=vosk | rms=468 | updated_at=1788180807.3157942 | frequency_hz=183.6
- [2026-08-31 20:53:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180819.8153827 | source=vosk | rms=468 | updated_at=1788180807.3157942 | frequency_hz=183.6
- [2026-08-31 20:53:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180820.315638 | source=vosk | rms=468 | updated_at=1788180807.3157942 | frequency_hz=183.6
- [2026-08-31 20:53:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180821.0649083 | source=vosk | rms=149 | updated_at=1788180821.0649083 | frequency_hz=183.6
- [2026-08-31 20:53:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180822.315266 | source=vosk | rms=149 | updated_at=1788180821.0649083 | frequency_hz=183.6
- [2026-08-31 20:54:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180840.315583 | source=vosk | rms=303 | updated_at=1788180840.315583 | frequency_hz=183.6
- [2026-08-31 20:54:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180841.0748017 | source=vosk | rms=522 | updated_at=1788180840.5654836 | frequency_hz=183.6
- [2026-08-31 20:54:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180842.3162625 | source=vosk | rms=442 | updated_at=1788180842.3162625 | frequency_hz=292.0
- [2026-08-31 20:54:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180842.8155532 | source=vosk | rms=442 | updated_at=1788180842.3162625 | frequency_hz=292.0
- [2026-08-31 20:54:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180843.0700016 | source=vosk | rms=341 | updated_at=1788180843.0700016 | frequency_hz=292.0
- [2026-08-31 20:54:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180843.5655942 | source=vosk | rms=341 | updated_at=1788180843.0700016 | frequency_hz=292.0
- [2026-08-31 20:54:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180846.1282716 | source=vosk | rms=442 | updated_at=1788180846.1282716 | frequency_hz=292.0
- [2026-08-31 20:54:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180846.815418 | source=vosk | rms=442 | updated_at=1788180846.1282716 | frequency_hz=292.0
- [2026-08-31 20:54:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180847.3164065 | source=vosk | rms=548 | updated_at=1788180847.3164065 | frequency_hz=302.5
- [2026-08-31 20:54:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180851.5670686 | source=vosk | rms=425 | updated_at=1788180851.0657542 | frequency_hz=302.5
- [2026-08-31 20:54:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180854.8188689 | source=vosk | rms=125 | updated_at=1788180854.8188689 | frequency_hz=302.5
- [2026-08-31 20:54:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180855.316495 | source=vosk | rms=125 | updated_at=1788180854.8188689 | frequency_hz=302.5
- [2026-08-31 20:54:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180855.816341 | source=vosk | rms=168 | updated_at=1788180855.816341 | frequency_hz=302.5
- [2026-08-31 20:54:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180856.315787 | source=vosk | rms=168 | updated_at=1788180855.816341 | frequency_hz=302.5
- [2026-08-31 20:54:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180856.8159382 | source=vosk | rms=180 | updated_at=1788180856.8159382 | frequency_hz=302.5
- [2026-08-31 20:54:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180861.316349 | source=vosk | rms=429 | updated_at=1788180860.567205 | frequency_hz=268.7
- [2026-08-31 20:54:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180865.0766535 | source=vosk | rms=387 | updated_at=1788180865.0766535 | frequency_hz=268.7
- [2026-08-31 20:54:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180868.5660458 | source=vosk | rms=310 | updated_at=1788180867.8166995 | frequency_hz=268.7
- [2026-08-31 20:54:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180870.5667493 | source=vosk | rms=580 | updated_at=1788180870.5667493 | frequency_hz=60.0
- [2026-08-31 20:54:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180871.6548402 | source=vosk | rms=580 | updated_at=1788180870.5667493 | frequency_hz=60.0
- [2026-08-31 20:54:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180878.0667737 | source=vosk | rms=580 | updated_at=1788180870.5667493 | frequency_hz=60.0
- [2026-08-31 20:54:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180878.5666392 | source=vosk | rms=580 | updated_at=1788180870.5667493 | frequency_hz=60.0
- [2026-08-31 20:54:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180879.5735292 | source=vosk | rms=580 | updated_at=1788180870.5667493 | frequency_hz=60.0
- [2026-08-31 20:54:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180880.3167872 | source=vosk | rms=145 | updated_at=1788180879.8162193 | frequency_hz=60.0
- [2026-08-31 20:54:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180881.3249028 | source=vosk | rms=347 | updated_at=1788180881.3249028 | frequency_hz=60.0
- [2026-08-31 20:54:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180882.0660863 | source=vosk | rms=347 | updated_at=1788180881.3249028 | frequency_hz=60.0
- [2026-08-31 20:54:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180882.8165133 | source=vosk | rms=172 | updated_at=1788180882.8165133 | frequency_hz=60.0
- [2026-08-31 20:54:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180884.3196454 | source=vosk | rms=168 | updated_at=1788180883.0660977 | frequency_hz=60.0
- [2026-08-31 20:54:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180885.0663533 | source=vosk | rms=300 | updated_at=1788180885.0663533 | frequency_hz=60.0
- [2026-08-31 20:54:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180886.3163471 | source=vosk | rms=139 | updated_at=1788180885.8188977 | frequency_hz=81.0
- [2026-08-31 20:54:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180887.066856 | source=vosk | rms=139 | updated_at=1788180885.8188977 | frequency_hz=81.0
- [2026-08-31 20:54:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180889.3165786 | source=vosk | rms=126 | updated_at=1788180888.8163106 | frequency_hz=176.5
- [2026-08-31 20:54:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180891.4864798 | source=vosk | rms=128 | updated_at=1788180891.4864798 | frequency_hz=176.5
- [2026-08-31 20:54:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180891.9692278 | source=vosk | rms=128 | updated_at=1788180891.4864798 | frequency_hz=176.5
- [2026-08-31 20:54:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180892.456216 | source=vosk | rms=144 | updated_at=1788180892.456216 | frequency_hz=176.5
- [2026-08-31 20:54:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180896.4578788 | source=vosk | rms=404 | updated_at=1788180895.9580772 | frequency_hz=176.5
- [2026-08-31 20:54:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180896.7065902 | source=vosk | rms=404 | updated_at=1788180895.9580772 | frequency_hz=176.5
- [2026-08-31 20:54:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180898.4562662 | source=vosk | rms=306 | updated_at=1788180897.957262 | frequency_hz=176.5
- [2026-08-31 20:55:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180900.2079031 | source=vosk | rms=979 | updated_at=1788180900.2079031 | frequency_hz=176.5
- [2026-08-31 20:55:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180900.956675 | source=vosk | rms=1206 | updated_at=1788180900.456124 | frequency_hz=242.1
- [2026-08-31 20:55:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180901.9564726 | source=vosk | rms=775 | updated_at=1788180901.9564726 | frequency_hz=328.0
- [2026-08-31 20:55:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180903.1313553 | source=vosk | rms=120 | updated_at=1788180902.7068055 | frequency_hz=260.0
- [2026-08-31 20:55:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180903.2071536 | source=vosk | rms=120 | updated_at=1788180902.7068055 | frequency_hz=260.0
- [2026-08-31 20:55:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180904.4571493 | source=vosk | rms=120 | updated_at=1788180902.7068055 | frequency_hz=260.0
- [2026-08-31 20:55:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180904.957557 | source=vosk | rms=120 | updated_at=1788180902.7068055 | frequency_hz=260.0
- [2026-08-31 20:55:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180905.439061 | source=vosk | rms=120 | updated_at=1788180902.7068055 | frequency_hz=260.0
- [2026-08-31 20:55:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180905.7069588 | source=vosk | rms=160 | updated_at=1788180905.7069588 | frequency_hz=168.0
- [2026-08-31 20:55:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180906.2065973 | source=vosk | rms=160 | updated_at=1788180905.7069588 | frequency_hz=168.0
- [2026-08-31 20:55:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180907.4565291 | source=vosk | rms=339 | updated_at=1788180907.4565291 | frequency_hz=232.0
- [2026-08-31 20:55:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180908.7066658 | source=vosk | rms=138 | updated_at=1788180907.9576201 | frequency_hz=205.4
- [2026-08-31 20:55:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180909.7076883 | source=vosk | rms=311 | updated_at=1788180909.7061858 | frequency_hz=205.4
- [2026-08-31 20:55:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180910.4592323 | source=vosk | rms=149 | updated_at=1788180909.9577918 | frequency_hz=205.4
- [2026-08-31 20:55:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180912.4566538 | source=vosk | rms=270 | updated_at=1788180912.4566538 | frequency_hz=205.4
- [2026-08-31 20:55:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180912.9575243 | source=vosk | rms=270 | updated_at=1788180912.4566538 | frequency_hz=205.4
- [2026-08-31 20:55:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180913.2077339 | source=vosk | rms=270 | updated_at=1788180912.4566538 | frequency_hz=205.4
- [2026-08-31 20:55:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180914.7076077 | source=vosk | rms=583 | updated_at=1788180913.4575644 | frequency_hz=235.7
- [2026-08-31 20:55:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180917.206903 | source=vosk | rms=507 | updated_at=1788180917.206903 | frequency_hz=276.0
- [2026-08-31 20:55:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180918.2069476 | source=vosk | rms=507 | updated_at=1788180917.206903 | frequency_hz=276.0
- [2026-08-31 20:55:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180918.7075818 | source=vosk | rms=173 | updated_at=1788180918.7075818 | frequency_hz=296.0
- [2026-08-31 20:55:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180919.2070987 | source=vosk | rms=173 | updated_at=1788180918.7075818 | frequency_hz=296.0
- [2026-08-31 20:55:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180919.7080262 | source=vosk | rms=130 | updated_at=1788180919.7080262 | frequency_hz=296.0
- [2026-08-31 20:55:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180920.2086103 | source=vosk | rms=130 | updated_at=1788180919.7080262 | frequency_hz=296.0
- [2026-08-31 20:55:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180921.207621 | source=vosk | rms=239 | updated_at=1788180921.207621 | frequency_hz=280.0
- [2026-08-31 20:55:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180921.7072353 | source=vosk | rms=239 | updated_at=1788180921.207621 | frequency_hz=280.0
- [2026-08-31 20:55:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180922.4578578 | source=vosk | rms=136 | updated_at=1788180922.4578578 | frequency_hz=236.6
- [2026-08-31 20:55:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180922.957697 | source=vosk | rms=136 | updated_at=1788180922.4578578 | frequency_hz=236.6
- [2026-08-31 20:55:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180923.4574845 | source=vosk | rms=123 | updated_at=1788180923.4574845 | frequency_hz=236.6
- [2026-08-31 20:55:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180923.9578593 | source=vosk | rms=123 | updated_at=1788180923.4574845 | frequency_hz=236.6
- [2026-08-31 20:55:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180924.208115 | source=vosk | rms=297 | updated_at=1788180924.208115 | frequency_hz=236.6
- [2026-08-31 20:55:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180924.9579237 | source=vosk | rms=297 | updated_at=1788180924.208115 | frequency_hz=236.6
- [2026-08-31 20:55:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180925.2077348 | source=vosk | rms=536 | updated_at=1788180925.2077348 | frequency_hz=236.6
- [2026-08-31 20:55:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180926.46404 | source=vosk | rms=215 | updated_at=1788180925.9637237 | frequency_hz=236.6
- [2026-08-31 20:55:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180927.7066014 | source=vosk | rms=215 | updated_at=1788180925.9637237 | frequency_hz=236.6
- [2026-08-31 20:55:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180928.457835 | source=vosk | rms=215 | updated_at=1788180925.9637237 | frequency_hz=236.6
- [2026-08-31 20:55:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180928.7081926 | source=vosk | rms=215 | updated_at=1788180925.9637237 | frequency_hz=236.6
- [2026-08-31 20:55:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180929.2077825 | source=vosk | rms=215 | updated_at=1788180925.9637237 | frequency_hz=236.6
- [2026-08-31 20:55:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180930.7077725 | source=vosk | rms=573 | updated_at=1788180930.7077725 | frequency_hz=236.6
- [2026-08-31 20:55:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180933.7094932 | source=vosk | rms=292 | updated_at=1788180933.2080722 | frequency_hz=236.6
- [2026-08-31 20:55:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180933.9577603 | source=vosk | rms=292 | updated_at=1788180933.2080722 | frequency_hz=236.6
- [2026-08-31 20:55:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180935.707447 | source=vosk | rms=350 | updated_at=1788180935.2079942 | frequency_hz=236.6
- [2026-08-31 20:55:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180936.4587588 | source=vosk | rms=350 | updated_at=1788180935.2079942 | frequency_hz=236.6
- [2026-08-31 20:55:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180937.2081077 | source=vosk | rms=350 | updated_at=1788180935.2079942 | frequency_hz=236.6
- [2026-08-31 20:55:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180938.7075624 | source=vosk | rms=350 | updated_at=1788180935.2079942 | frequency_hz=236.6
- [2026-08-31 20:55:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180939.208199 | source=vosk | rms=350 | updated_at=1788180935.2079942 | frequency_hz=236.6
- [2026-08-31 20:55:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180939.7081175 | source=vosk | rms=128 | updated_at=1788180939.7081175 | frequency_hz=236.6
- [2026-08-31 20:55:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180940.4580126 | source=vosk | rms=183 | updated_at=1788180939.9574823 | frequency_hz=236.6
- [2026-08-31 20:55:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180941.967307 | source=vosk | rms=418 | updated_at=1788180941.967307 | frequency_hz=236.6
- [2026-08-31 20:55:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180942.707882 | source=vosk | rms=696 | updated_at=1788180942.2081394 | frequency_hz=236.6
- [2026-08-31 20:55:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180942.9579723 | source=vosk | rms=339 | updated_at=1788180942.9579723 | frequency_hz=236.6
- [2026-08-31 20:55:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180948.9577565 | source=vosk | rms=600 | updated_at=1788180947.457783 | frequency_hz=236.6
- [2026-08-31 20:55:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180949.4583192 | source=vosk | rms=211 | updated_at=1788180949.4583192 | frequency_hz=116.0
- [2026-08-31 20:55:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180949.9577816 | source=vosk | rms=211 | updated_at=1788180949.4583192 | frequency_hz=116.0
- [2026-08-31 20:55:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180950.7074814 | source=vosk | rms=275 | updated_at=1788180950.7074814 | frequency_hz=116.0
- [2026-08-31 20:55:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180951.4849799 | source=vosk | rms=284 | updated_at=1788180950.957599 | frequency_hz=116.0
- [2026-08-31 20:55:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180955.2081985 | source=vosk | rms=380 | updated_at=1788180955.2081985 | frequency_hz=196.0
- [2026-08-31 20:55:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180955.7085242 | source=vosk | rms=380 | updated_at=1788180955.2081985 | frequency_hz=196.0
- [2026-08-31 20:56:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180965.4588695 | source=vosk | rms=263 | updated_at=1788180965.4588695 | frequency_hz=196.0
- [2026-08-31 20:56:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180965.962683 | source=vosk | rms=263 | updated_at=1788180965.4588695 | frequency_hz=196.0
- [2026-08-31 20:56:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180966.9584723 | source=vosk | rms=242 | updated_at=1788180966.9584723 | frequency_hz=200.0
- [2026-08-31 20:56:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180967.708096 | source=vosk | rms=272 | updated_at=1788180967.208608 | frequency_hz=205.6
- [2026-08-31 20:56:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180967.9592516 | source=vosk | rms=272 | updated_at=1788180967.208608 | frequency_hz=205.6
- [2026-08-31 20:56:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180968.4582152 | source=vosk | rms=272 | updated_at=1788180967.208608 | frequency_hz=205.6
- [2026-08-31 20:56:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180969.708794 | source=vosk | rms=146 | updated_at=1788180969.708794 | frequency_hz=205.6
- [2026-08-31 20:56:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180971.4585257 | source=vosk | rms=851 | updated_at=1788180970.97228 | frequency_hz=205.6
- [2026-08-31 20:56:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180971.708445 | source=vosk | rms=750 | updated_at=1788180971.708445 | frequency_hz=205.6
- [2026-08-31 20:56:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180972.2081695 | source=vosk | rms=750 | updated_at=1788180971.708445 | frequency_hz=205.6
- [2026-08-31 20:56:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180975.4579391 | source=vosk | rms=640 | updated_at=1788180975.4579391 | frequency_hz=205.6
- [2026-08-31 20:56:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180978.2730172 | source=vosk | rms=285 | updated_at=1788180977.7778986 | frequency_hz=198.7
- [2026-08-31 20:56:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180980.3048549 | source=vosk | rms=1206 | updated_at=1788180980.3048549 | frequency_hz=198.7
- [2026-08-31 20:56:23] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1788180983.9437091 | source=final | rms=1204 | updated_at=1788180983.5529752 | frequency_hz=198.7
- [2026-08-31 20:56:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180983.9818292 | source=vosk | rms=1204 | updated_at=1788180983.5529752 | frequency_hz=198.7
- [2026-08-31 20:56:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180983.9818292 | source=vosk | rms=1204 | updated_at=1788180983.5529752 | frequency_hz=198.7
- [2026-08-31 20:56:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180985.3023615 | source=vosk | rms=608 | updated_at=1788180984.8026857 | frequency_hz=198.7
- [2026-08-31 20:56:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180985.8062854 | source=vosk | rms=1070 | updated_at=1788180985.8062854 | frequency_hz=198.7
- [2026-08-31 20:56:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180986.5539505 | source=vosk | rms=1070 | updated_at=1788180985.8062854 | frequency_hz=198.7
- [2026-08-31 20:56:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180994.344694 | source=vosk | rms=1070 | updated_at=1788180985.8062854 | frequency_hz=198.7
- [2026-08-31 20:56:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180994.847945 | source=vosk | rms=1070 | updated_at=1788180985.8062854 | frequency_hz=198.7
- [2026-08-31 20:56:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180995.7683911 | source=vosk | rms=273 | updated_at=1788180995.7683911 | frequency_hz=198.7
- [2026-08-31 20:56:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180996.8445537 | source=vosk | rms=225 | updated_at=1788180996.3453217 | frequency_hz=198.7
- [2026-08-31 20:56:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180997.345121 | source=vosk | rms=1152 | updated_at=1788180997.345121 | frequency_hz=198.7
- [2026-08-31 20:56:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788180998.0946295 | source=vosk | rms=893 | updated_at=1788180997.5952935 | frequency_hz=198.7
- [2026-08-31 20:56:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788180998.5953128 | source=vosk | rms=391 | updated_at=1788180998.5953128 | frequency_hz=198.7
- [2026-08-31 20:56:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181001.7225838 | source=vosk | rms=234 | updated_at=1788181000.76777 | frequency_hz=198.7
- [2026-08-31 20:56:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181002.2233775 | source=vosk | rms=294 | updated_at=1788181002.2233775 | frequency_hz=374.0
- [2026-08-31 20:56:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181002.7284675 | source=vosk | rms=294 | updated_at=1788181002.2233775 | frequency_hz=374.0
- [2026-08-31 20:56:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181004.9728081 | source=vosk | rms=248 | updated_at=1788181004.9728081 | frequency_hz=374.0
- [2026-08-31 20:56:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181006.7228055 | source=vosk | rms=304 | updated_at=1788181006.2232926 | frequency_hz=374.0
- [2026-08-31 20:56:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181007.473343 | source=vosk | rms=203 | updated_at=1788181007.473343 | frequency_hz=374.0
- [2026-08-31 20:56:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181008.2231243 | source=vosk | rms=357 | updated_at=1788181007.7225425 | frequency_hz=374.0
- [2026-08-31 20:56:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181008.473665 | source=vosk | rms=357 | updated_at=1788181007.7225425 | frequency_hz=374.0
- [2026-08-31 20:56:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181009.7231174 | source=vosk | rms=358 | updated_at=1788181008.9734168 | frequency_hz=374.0
- [2026-08-31 20:56:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181009.9734943 | source=vosk | rms=264 | updated_at=1788181009.9734943 | frequency_hz=374.0
- [2026-08-31 20:56:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181011.472952 | source=vosk | rms=248 | updated_at=1788181010.223273 | frequency_hz=374.0
- [2026-08-31 20:56:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181012.2231128 | source=vosk | rms=248 | updated_at=1788181010.223273 | frequency_hz=374.0
- [2026-08-31 20:56:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181012.7231476 | source=vosk | rms=248 | updated_at=1788181010.223273 | frequency_hz=374.0
- [2026-08-31 20:56:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181013.7234592 | source=vosk | rms=248 | updated_at=1788181010.223273 | frequency_hz=374.0
- [2026-08-31 20:56:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181014.7264564 | source=vosk | rms=1201 | updated_at=1788181014.2238264 | frequency_hz=374.0
- [2026-08-31 20:56:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181015.2228441 | source=vosk | rms=1201 | updated_at=1788181015.2228441 | frequency_hz=374.0
- [2026-08-31 20:56:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181016.973446 | source=vosk | rms=308 | updated_at=1788181016.4735053 | frequency_hz=374.0
- [2026-08-31 20:56:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181018.2455404 | source=vosk | rms=307 | updated_at=1788181018.2455404 | frequency_hz=374.0
- [2026-08-31 20:57:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181020.2438178 | source=vosk | rms=512 | updated_at=1788181018.9927988 | frequency_hz=374.0
- [2026-08-31 20:57:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181020.9932542 | source=vosk | rms=335 | updated_at=1788181020.9932542 | frequency_hz=374.0
- [2026-08-31 20:57:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181025.4937327 | source=vosk | rms=506 | updated_at=1788181024.9930577 | frequency_hz=374.0
- [2026-08-31 20:57:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181025.7438252 | source=vosk | rms=478 | updated_at=1788181025.7438252 | frequency_hz=374.0
- [2026-08-31 20:57:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181027.4458094 | source=vosk | rms=217 | updated_at=1788181026.7425897 | frequency_hz=374.0
- [2026-08-31 20:57:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181027.6939166 | source=vosk | rms=568 | updated_at=1788181027.6939166 | frequency_hz=374.0
- [2026-08-31 20:57:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181030.1945202 | source=vosk | rms=325 | updated_at=1788181029.7029443 | frequency_hz=374.0
- [2026-08-31 20:57:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181030.9429946 | source=vosk | rms=444 | updated_at=1788181030.9429946 | frequency_hz=374.0
- [2026-08-31 20:57:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181031.6938648 | source=vosk | rms=444 | updated_at=1788181030.9429946 | frequency_hz=374.0
- [2026-08-31 20:57:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181038.492697 | source=vosk | rms=444 | updated_at=1788181030.9429946 | frequency_hz=374.0
- [2026-08-31 20:57:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181038.9974296 | source=vosk | rms=444 | updated_at=1788181030.9429946 | frequency_hz=374.0
- [2026-08-31 20:57:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181039.5306916 | source=vosk | rms=444 | updated_at=1788181030.9429946 | frequency_hz=374.0
- [2026-08-31 20:57:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181039.9950552 | source=vosk | rms=444 | updated_at=1788181030.9429946 | frequency_hz=374.0
- [2026-08-31 20:57:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181040.493341 | source=vosk | rms=351 | updated_at=1788181040.493341 | frequency_hz=374.0
- [2026-08-31 20:57:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181045.4942265 | source=vosk | rms=297 | updated_at=1788181044.993741 | frequency_hz=374.0
- [2026-08-31 20:57:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181048.24359 | source=vosk | rms=280 | updated_at=1788181048.24359 | frequency_hz=184.0
- [2026-08-31 20:57:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181048.8622296 | source=vosk | rms=280 | updated_at=1788181048.24359 | frequency_hz=184.0
- [2026-08-31 20:57:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181049.2435246 | source=vosk | rms=309 | updated_at=1788181049.2435246 | frequency_hz=209.2
- [2026-08-31 20:57:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181049.7434964 | source=vosk | rms=309 | updated_at=1788181049.2435246 | frequency_hz=209.2
- [2026-08-31 20:57:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181052.7596195 | source=vosk | rms=214 | updated_at=1788181052.7596195 | frequency_hz=209.2
- [2026-08-31 20:57:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181053.2442894 | source=vosk | rms=214 | updated_at=1788181052.7596195 | frequency_hz=209.2
- [2026-08-31 20:57:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181056.2442863 | source=vosk | rms=214 | updated_at=1788181052.7596195 | frequency_hz=209.2
- [2026-08-31 20:57:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181056.7436411 | source=vosk | rms=214 | updated_at=1788181052.7596195 | frequency_hz=209.2
- [2026-08-31 20:57:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181056.993593 | source=vosk | rms=246 | updated_at=1788181056.993593 | frequency_hz=209.2
- [2026-08-31 20:57:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181060.7439392 | source=vosk | rms=1201 | updated_at=1788181060.244124 | frequency_hz=209.2
- [2026-08-31 20:57:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181061.745294 | source=vosk | rms=1201 | updated_at=1788181060.244124 | frequency_hz=209.2
- [2026-08-31 20:57:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181064.7451706 | source=vosk | rms=1202 | updated_at=1788181064.2441728 | frequency_hz=209.2
- [2026-08-31 20:57:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181065.494528 | source=vosk | rms=775 | updated_at=1788181065.494528 | frequency_hz=209.2
- [2026-08-31 20:57:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181066.494438 | source=vosk | rms=560 | updated_at=1788181066.009912 | frequency_hz=209.2
- [2026-08-31 20:57:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181067.24403 | source=vosk | rms=1203 | updated_at=1788181067.24403 | frequency_hz=209.2
- [2026-08-31 20:57:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181068.171861 | source=vosk | rms=375 | updated_at=1788181067.493889 | frequency_hz=209.2
- [2026-08-31 20:57:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181068.494611 | source=vosk | rms=188 | updated_at=1788181068.494611 | frequency_hz=209.2
- [2026-08-31 20:57:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181069.9946487 | source=vosk | rms=592 | updated_at=1788181069.4941585 | frequency_hz=229.1
- [2026-08-31 20:57:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181070.2445688 | source=vosk | rms=251 | updated_at=1788181070.2445688 | frequency_hz=229.1
- [2026-08-31 20:57:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181072.4937856 | source=vosk | rms=389 | updated_at=1788181071.994742 | frequency_hz=228.0
- [2026-08-31 20:57:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181073.2445889 | source=vosk | rms=271 | updated_at=1788181073.2445889 | frequency_hz=228.0
- [2026-08-31 20:57:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181074.2436638 | source=vosk | rms=780 | updated_at=1788181073.7454329 | frequency_hz=228.0
- [2026-08-31 20:57:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181074.5021386 | source=vosk | rms=609 | updated_at=1788181074.5021386 | frequency_hz=228.0
- [2026-08-31 20:57:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181075.0263774 | source=vosk | rms=609 | updated_at=1788181074.5021386 | frequency_hz=228.0
- [2026-08-31 20:57:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181075.7761924 | source=vosk | rms=609 | updated_at=1788181074.5021386 | frequency_hz=228.0
- [2026-08-31 20:57:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181076.2768693 | source=vosk | rms=609 | updated_at=1788181074.5021386 | frequency_hz=228.0
- [2026-08-31 20:57:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181076.5273693 | source=vosk | rms=447 | updated_at=1788181076.5273693 | frequency_hz=228.0
- [2026-08-31 20:57:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181077.5260577 | source=vosk | rms=447 | updated_at=1788181076.5273693 | frequency_hz=228.0
- [2026-08-31 20:57:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181078.5264146 | source=vosk | rms=426 | updated_at=1788181078.5264146 | frequency_hz=204.0
- [2026-08-31 20:58:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181080.0268965 | source=vosk | rms=338 | updated_at=1788181079.5263083 | frequency_hz=204.0
- [2026-08-31 20:58:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181083.3157609 | source=vosk | rms=1205 | updated_at=1788181083.3157609 | frequency_hz=204.0
- [2026-08-31 20:58:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181083.8076625 | source=vosk | rms=1205 | updated_at=1788181083.3157609 | frequency_hz=204.0
- [2026-08-31 20:58:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181085.0742261 | source=vosk | rms=516 | updated_at=1788181085.0742261 | frequency_hz=204.0
- [2026-08-31 20:58:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181086.5566733 | source=vosk | rms=356 | updated_at=1788181086.056397 | frequency_hz=204.0
- [2026-08-31 20:58:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181086.8071032 | source=vosk | rms=515 | updated_at=1788181086.8071032 | frequency_hz=204.0
- [2026-08-31 20:58:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181088.0557382 | source=vosk | rms=515 | updated_at=1788181086.8071032 | frequency_hz=204.0
- [2026-08-31 20:58:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181090.890608 | source=vosk | rms=320 | updated_at=1788181090.890608 | frequency_hz=136.0
- [2026-08-31 20:58:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181091.3906584 | source=vosk | rms=320 | updated_at=1788181090.890608 | frequency_hz=136.0
- [2026-08-31 20:58:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181093.2006 | source=vosk | rms=320 | updated_at=1788181090.890608 | frequency_hz=136.0
- [2026-08-31 20:58:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181093.695227 | source=vosk | rms=320 | updated_at=1788181090.890608 | frequency_hz=136.0
- [2026-08-31 20:58:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181094.444271 | source=vosk | rms=320 | updated_at=1788181090.890608 | frequency_hz=136.0
- [2026-08-31 20:58:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181094.9444897 | source=vosk | rms=320 | updated_at=1788181090.890608 | frequency_hz=136.0
- [2026-08-31 20:58:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181096.4448252 | source=vosk | rms=553 | updated_at=1788181096.4448252 | frequency_hz=136.0
- [2026-08-31 20:58:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181100.755455 | source=vosk | rms=938 | updated_at=1788181100.2746732 | frequency_hz=136.0
- [2026-08-31 20:58:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181101.5062008 | source=vosk | rms=938 | updated_at=1788181100.2746732 | frequency_hz=136.0
- [2026-08-31 20:58:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181102.0049462 | source=vosk | rms=938 | updated_at=1788181100.2746732 | frequency_hz=136.0
- [2026-08-31 20:58:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181102.5045152 | source=vosk | rms=198 | updated_at=1788181102.5045152 | frequency_hz=136.0
- [2026-08-31 20:58:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181107.754649 | source=vosk | rms=161 | updated_at=1788181106.264297 | frequency_hz=136.0
- [2026-08-31 20:58:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181111.504147 | source=vosk | rms=161 | updated_at=1788181106.264297 | frequency_hz=136.0
- [2026-08-31 20:58:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181112.0056398 | source=vosk | rms=161 | updated_at=1788181106.264297 | frequency_hz=136.0
- [2026-08-31 20:58:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181114.5051618 | source=vosk | rms=509 | updated_at=1788181114.5051618 | frequency_hz=136.0
- [2026-08-31 20:58:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181115.755281 | source=vosk | rms=528 | updated_at=1788181115.0062633 | frequency_hz=136.0
- [2026-08-31 20:58:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181117.7555084 | source=vosk | rms=452 | updated_at=1788181117.7555084 | frequency_hz=136.0
- [2026-08-31 20:58:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181118.5127344 | source=vosk | rms=452 | updated_at=1788181117.7555084 | frequency_hz=136.0
- [2026-08-31 20:58:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181119.256256 | source=vosk | rms=145 | updated_at=1788181119.256256 | frequency_hz=136.0
- [2026-08-31 20:58:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181119.7562947 | source=vosk | rms=145 | updated_at=1788181119.256256 | frequency_hz=136.0
- [2026-08-31 20:58:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181120.005035 | source=vosk | rms=503 | updated_at=1788181120.005035 | frequency_hz=136.0
- [2026-08-31 20:58:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181120.7551124 | source=vosk | rms=503 | updated_at=1788181120.005035 | frequency_hz=136.0
- [2026-08-31 20:58:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181121.5050695 | source=vosk | rms=129 | updated_at=1788181121.5050695 | frequency_hz=136.0
- [2026-08-31 20:58:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181123.0050523 | source=vosk | rms=172 | updated_at=1788181122.0054088 | frequency_hz=136.0
- [2026-08-31 20:58:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181126.0056045 | source=vosk | rms=225 | updated_at=1788181126.0056045 | frequency_hz=136.0
- [2026-08-31 20:58:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181126.5057914 | source=vosk | rms=225 | updated_at=1788181126.0056045 | frequency_hz=136.0
- [2026-08-31 20:58:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181129.5050602 | source=vosk | rms=295 | updated_at=1788181129.5050602 | frequency_hz=136.0
- [2026-08-31 20:58:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181130.005417 | source=vosk | rms=295 | updated_at=1788181129.5050602 | frequency_hz=136.0
- [2026-08-31 20:58:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181133.0058773 | source=vosk | rms=295 | updated_at=1788181129.5050602 | frequency_hz=136.0
- [2026-08-31 20:58:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181133.505611 | source=vosk | rms=295 | updated_at=1788181129.5050602 | frequency_hz=136.0
- [2026-08-31 20:58:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181134.0053425 | source=vosk | rms=409 | updated_at=1788181134.0053425 | frequency_hz=250.0
- [2026-08-31 20:58:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181136.0097156 | source=vosk | rms=218 | updated_at=1788181135.5056407 | frequency_hz=250.0
- [2026-08-31 20:58:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181137.2640572 | source=vosk | rms=289 | updated_at=1788181137.2640572 | frequency_hz=372.0
- [2026-08-31 20:58:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181137.7776535 | source=vosk | rms=289 | updated_at=1788181137.2640572 | frequency_hz=372.0
- [2026-08-31 20:58:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181138.7555158 | source=vosk | rms=287 | updated_at=1788181138.7555158 | frequency_hz=90.0
- [2026-08-31 20:58:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181139.255564 | source=vosk | rms=287 | updated_at=1788181138.7555158 | frequency_hz=90.0
- [2026-08-31 20:59:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181141.097811 | source=vosk | rms=270 | updated_at=1788181141.097811 | frequency_hz=390.0
- [2026-08-31 20:59:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181141.847262 | source=vosk | rms=675 | updated_at=1788181141.3474247 | frequency_hz=398.4
- [2026-08-31 20:59:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181142.0974128 | source=vosk | rms=346 | updated_at=1788181142.0974128 | frequency_hz=398.4
- [2026-08-31 20:59:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181144.5979788 | source=vosk | rms=163 | updated_at=1788181144.0978174 | frequency_hz=398.4
- [2026-08-31 20:59:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181144.8479314 | source=vosk | rms=145 | updated_at=1788181144.8479314 | frequency_hz=398.4
- [2026-08-31 20:59:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181147.347821 | source=vosk | rms=363 | updated_at=1788181146.8479733 | frequency_hz=372.4
- [2026-08-31 20:59:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181148.59757 | source=vosk | rms=363 | updated_at=1788181146.8479733 | frequency_hz=372.4
- [2026-08-31 20:59:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181149.0989265 | source=vosk | rms=363 | updated_at=1788181146.8479733 | frequency_hz=372.4
- [2026-08-31 20:59:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181149.8477087 | source=vosk | rms=151 | updated_at=1788181149.8477087 | frequency_hz=372.4
- [2026-08-31 20:59:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181150.3476975 | source=vosk | rms=151 | updated_at=1788181149.8477087 | frequency_hz=372.4
- [2026-08-31 20:59:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181155.5980434 | source=vosk | rms=242 | updated_at=1788181155.5980434 | frequency_hz=100.0
- [2026-08-31 20:59:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181156.0989056 | source=vosk | rms=242 | updated_at=1788181155.5980434 | frequency_hz=100.0
- [2026-08-31 20:59:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181157.0982594 | source=vosk | rms=293 | updated_at=1788181157.0982594 | frequency_hz=384.0
- [2026-08-31 20:59:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181157.6060202 | source=vosk | rms=293 | updated_at=1788181157.0982594 | frequency_hz=384.0
- [2026-08-31 20:59:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181157.8477604 | source=vosk | rms=498 | updated_at=1788181157.8477604 | frequency_hz=384.0
- [2026-08-31 20:59:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181159.5972867 | source=vosk | rms=280 | updated_at=1788181158.5976343 | frequency_hz=384.0
- [2026-08-31 20:59:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181159.848238 | source=vosk | rms=309 | updated_at=1788181159.848238 | frequency_hz=384.0
- [2026-08-31 20:59:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181161.225543 | source=vosk | rms=309 | updated_at=1788181159.848238 | frequency_hz=384.0
- [2026-08-31 20:59:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181162.4522336 | source=vosk | rms=1201 | updated_at=1788181162.4522336 | frequency_hz=384.0
- [2026-08-31 20:59:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181162.9519773 | source=vosk | rms=1201 | updated_at=1788181162.4522336 | frequency_hz=384.0
- [2026-08-31 20:59:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181164.2781527 | source=vosk | rms=145 | updated_at=1788181164.2781527 | frequency_hz=384.0
- [2026-08-31 20:59:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181165.4577386 | source=vosk | rms=145 | updated_at=1788181164.2781527 | frequency_hz=384.0
- [2026-08-31 20:59:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181166.2081535 | source=vosk | rms=145 | updated_at=1788181164.2781527 | frequency_hz=384.0
- [2026-08-31 20:59:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181167.2079146 | source=vosk | rms=205 | updated_at=1788181166.7226088 | frequency_hz=384.0
- [2026-08-31 20:59:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181167.458623 | source=vosk | rms=205 | updated_at=1788181166.7226088 | frequency_hz=384.0
- [2026-08-31 20:59:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181168.4584827 | source=vosk | rms=1201 | updated_at=1788181167.9582965 | frequency_hz=384.0
- [2026-08-31 20:59:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181168.8653007 | source=vosk | rms=176 | updated_at=1788181168.8653007 | frequency_hz=342.0
- [2026-08-31 20:59:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181169.4583244 | source=vosk | rms=167 | updated_at=1788181168.95791 | frequency_hz=265.7
- [2026-08-31 20:59:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181170.209444 | source=vosk | rms=130 | updated_at=1788181170.209444 | frequency_hz=265.7
- [2026-08-31 20:59:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181170.7092767 | source=vosk | rms=130 | updated_at=1788181170.209444 | frequency_hz=265.7
- [2026-08-31 20:59:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181170.963493 | source=vosk | rms=130 | updated_at=1788181170.209444 | frequency_hz=265.7
- [2026-08-31 20:59:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181171.7077088 | source=vosk | rms=130 | updated_at=1788181170.209444 | frequency_hz=265.7
- [2026-08-31 20:59:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181173.708341 | source=vosk | rms=967 | updated_at=1788181173.708341 | frequency_hz=265.7
- [2026-08-31 20:59:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181174.2104678 | source=vosk | rms=967 | updated_at=1788181173.708341 | frequency_hz=265.7
- [2026-08-31 20:59:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181177.7082756 | source=vosk | rms=391 | updated_at=1788181177.7082756 | frequency_hz=265.7
- [2026-08-31 20:59:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181178.7085354 | source=vosk | rms=183 | updated_at=1788181178.2087214 | frequency_hz=265.7
- [2026-08-31 20:59:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181181.7023437 | source=vosk | rms=188 | updated_at=1788181181.7023437 | frequency_hz=265.7
- [2026-08-31 20:59:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181183.452374 | source=vosk | rms=180 | updated_at=1788181182.4523745 | frequency_hz=265.7
- [2026-08-31 20:59:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181183.952346 | source=vosk | rms=405 | updated_at=1788181183.952346 | frequency_hz=274.0
- [2026-08-31 20:59:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181187.202895 | source=vosk | rms=163 | updated_at=1788181186.7028985 | frequency_hz=227.1
- [2026-08-31 20:59:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181187.7029166 | source=vosk | rms=361 | updated_at=1788181187.7029166 | frequency_hz=216.2
- [2026-08-31 20:59:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181188.202674 | source=vosk | rms=361 | updated_at=1788181187.7029166 | frequency_hz=216.2
- [2026-08-31 20:59:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181188.7027087 | source=vosk | rms=655 | updated_at=1788181188.7027087 | frequency_hz=216.2
- [2026-08-31 20:59:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181189.7021854 | source=vosk | rms=448 | updated_at=1788181189.2029357 | frequency_hz=220.3
- [2026-08-31 20:59:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181190.9639087 | source=vosk | rms=583 | updated_at=1788181190.9639087 | frequency_hz=220.3
- [2026-08-31 20:59:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181191.702773 | source=vosk | rms=484 | updated_at=1788181191.2023065 | frequency_hz=245.4
- [2026-08-31 20:59:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181191.9528916 | source=vosk | rms=614 | updated_at=1788181191.9528916 | frequency_hz=239.3
- [2026-08-31 20:59:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181193.4531434 | source=vosk | rms=478 | updated_at=1788181192.9527667 | frequency_hz=223.3
- [2026-08-31 20:59:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181194.4529643 | source=vosk | rms=146 | updated_at=1788181194.4529643 | frequency_hz=92.0
- [2026-08-31 20:59:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181196.7028904 | source=vosk | rms=1202 | updated_at=1788181195.9529965 | frequency_hz=92.0
- [2026-08-31 20:59:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181199.2028773 | source=vosk | rms=1202 | updated_at=1788181195.9529965 | frequency_hz=92.0
- [2026-08-31 20:59:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181199.7027855 | source=vosk | rms=1202 | updated_at=1788181195.9529965 | frequency_hz=92.0
- [2026-08-31 21:00:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181201.4527555 | source=vosk | rms=353 | updated_at=1788181201.4527555 | frequency_hz=344.0
- [2026-08-31 21:00:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181201.9532194 | source=vosk | rms=353 | updated_at=1788181201.4527555 | frequency_hz=344.0
- [2026-08-31 21:00:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181202.4534712 | source=vosk | rms=341 | updated_at=1788181202.4534712 | frequency_hz=344.0
- [2026-08-31 21:00:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181202.956246 | source=vosk | rms=341 | updated_at=1788181202.4534712 | frequency_hz=344.0
- [2026-08-31 21:00:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181204.204159 | source=vosk | rms=341 | updated_at=1788181202.4534712 | frequency_hz=344.0
- [2026-08-31 21:00:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181204.7031307 | source=vosk | rms=341 | updated_at=1788181202.4534712 | frequency_hz=344.0
- [2026-08-31 21:00:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181205.70253 | source=vosk | rms=165 | updated_at=1788181205.70253 | frequency_hz=344.0
- [2026-08-31 21:00:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181208.20337 | source=vosk | rms=588 | updated_at=1788181207.202975 | frequency_hz=344.0
- [2026-08-31 21:00:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181208.4639542 | source=vosk | rms=536 | updated_at=1788181208.4639542 | frequency_hz=344.0
- [2026-08-31 21:00:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181209.9530933 | source=vosk | rms=158 | updated_at=1788181209.453116 | frequency_hz=344.0
- [2026-08-31 21:00:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181210.2027123 | source=vosk | rms=158 | updated_at=1788181209.453116 | frequency_hz=344.0
- [2026-08-31 21:00:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181211.4561417 | source=vosk | rms=158 | updated_at=1788181209.453116 | frequency_hz=344.0
- [2026-08-31 21:00:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181211.727363 | source=vosk | rms=161 | updated_at=1788181211.727363 | frequency_hz=344.0
- [2026-08-31 21:00:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181212.9527042 | source=vosk | rms=147 | updated_at=1788181212.4528224 | frequency_hz=344.0
- [2026-08-31 21:00:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181213.906464 | source=vosk | rms=272 | updated_at=1788181213.906464 | frequency_hz=156.0
- [2026-08-31 21:00:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181214.4529614 | source=vosk | rms=699 | updated_at=1788181213.952677 | frequency_hz=156.0
- [2026-08-31 21:00:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181216.2034843 | source=vosk | rms=200 | updated_at=1788181216.2034843 | frequency_hz=156.0
- [2026-08-31 21:00:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181216.7042387 | source=vosk | rms=200 | updated_at=1788181216.2034843 | frequency_hz=156.0
- [2026-08-31 21:00:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181217.7026365 | source=vosk | rms=350 | updated_at=1788181217.7026365 | frequency_hz=156.0
- [2026-08-31 21:00:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181218.453349 | source=vosk | rms=133 | updated_at=1788181217.9530053 | frequency_hz=156.0
- [2026-08-31 21:00:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181219.2052898 | source=vosk | rms=133 | updated_at=1788181217.9530053 | frequency_hz=156.0
- [2026-08-31 21:00:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181220.703249 | source=vosk | rms=243 | updated_at=1788181220.2022285 | frequency_hz=240.0
- [2026-08-31 21:00:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181226.702955 | source=vosk | rms=205 | updated_at=1788181226.702955 | frequency_hz=240.0
- [2026-08-31 21:00:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181228.203005 | source=vosk | rms=464 | updated_at=1788181227.4530466 | frequency_hz=215.2
- [2026-08-31 21:00:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181229.9929342 | source=vosk | rms=865 | updated_at=1788181229.9929342 | frequency_hz=215.2
- [2026-08-31 21:00:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181230.4536994 | source=vosk | rms=865 | updated_at=1788181229.9929342 | frequency_hz=215.2
- [2026-08-31 21:00:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181230.9530647 | source=vosk | rms=245 | updated_at=1788181230.9530647 | frequency_hz=215.2
- [2026-08-31 21:00:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181231.745817 | source=vosk | rms=245 | updated_at=1788181230.9530647 | frequency_hz=215.2
- [2026-08-31 21:00:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181232.4967222 | source=vosk | rms=245 | updated_at=1788181230.9530647 | frequency_hz=215.2
- [2026-08-31 21:00:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181233.9956677 | source=vosk | rms=396 | updated_at=1788181233.4957006 | frequency_hz=215.2
- [2026-08-31 21:00:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181236.246485 | source=vosk | rms=217 | updated_at=1788181236.246485 | frequency_hz=215.2
- [2026-08-31 21:00:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181236.7458959 | source=vosk | rms=217 | updated_at=1788181236.246485 | frequency_hz=215.2
- [2026-08-31 21:00:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181241.7451887 | source=vosk | rms=217 | updated_at=1788181236.246485 | frequency_hz=215.2
- [2026-08-31 21:00:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181242.5169473 | source=vosk | rms=217 | updated_at=1788181236.246485 | frequency_hz=215.2
- [2026-08-31 21:00:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181242.7923543 | source=vosk | rms=341 | updated_at=1788181242.7913542 | frequency_hz=215.2
- [2026-08-31 21:00:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181244.8423722 | source=vosk | rms=288 | updated_at=1788181244.0166774 | frequency_hz=215.2
- [2026-08-31 21:00:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181245.0941458 | source=vosk | rms=288 | updated_at=1788181244.0166774 | frequency_hz=215.2
- [2026-08-31 21:00:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181245.6557512 | source=vosk | rms=288 | updated_at=1788181244.0166774 | frequency_hz=215.2
- [2026-08-31 21:00:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181246.342754 | source=vosk | rms=201 | updated_at=1788181246.342754 | frequency_hz=215.2
- [2026-08-31 21:00:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181247.3447933 | source=vosk | rms=201 | updated_at=1788181246.342754 | frequency_hz=215.2
- [2026-08-31 21:00:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181247.5921926 | source=vosk | rms=201 | updated_at=1788181246.342754 | frequency_hz=215.2
- [2026-08-31 21:00:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181251.2099292 | source=vosk | rms=474 | updated_at=1788181250.7063963 | frequency_hz=215.2
- [2026-08-31 21:00:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181252.0391972 | source=vosk | rms=525 | updated_at=1788181252.0391972 | frequency_hz=215.2
- [2026-08-31 21:00:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181252.9598534 | source=vosk | rms=258 | updated_at=1788181252.2097988 | frequency_hz=215.2
- [2026-08-31 21:00:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181253.209647 | source=vosk | rms=258 | updated_at=1788181252.2097988 | frequency_hz=215.2
- [2026-08-31 21:01:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181261.4801013 | source=vosk | rms=154 | updated_at=1788181260.7296898 | frequency_hz=198.0
- [2026-08-31 21:01:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181262.2298238 | source=vosk | rms=657 | updated_at=1788181262.2298238 | frequency_hz=198.0
- [2026-08-31 21:01:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181263.2300441 | source=vosk | rms=710 | updated_at=1788181262.7301412 | frequency_hz=198.0
- [2026-08-31 21:01:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181263.4803534 | source=vosk | rms=328 | updated_at=1788181263.4803534 | frequency_hz=198.0
- [2026-08-31 21:01:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181266.2211041 | source=vosk | rms=876 | updated_at=1788181264.7427266 | frequency_hz=198.0
- [2026-08-31 21:01:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181266.73104 | source=vosk | rms=281 | updated_at=1788181266.73104 | frequency_hz=198.0
- [2026-08-31 21:01:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181267.493567 | source=vosk | rms=205 | updated_at=1788181266.9797244 | frequency_hz=198.0
- [2026-08-31 21:01:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181268.2300305 | source=vosk | rms=205 | updated_at=1788181266.9797244 | frequency_hz=198.0
- [2026-08-31 21:01:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181268.7305162 | source=vosk | rms=205 | updated_at=1788181266.9797244 | frequency_hz=198.0
- [2026-08-31 21:01:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181269.229963 | source=vosk | rms=205 | updated_at=1788181266.9797244 | frequency_hz=198.0
- [2026-08-31 21:01:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181269.7302265 | source=vosk | rms=205 | updated_at=1788181266.9797244 | frequency_hz=198.0
- [2026-08-31 21:01:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181270.730768 | source=vosk | rms=735 | updated_at=1788181270.730768 | frequency_hz=198.0
- [2026-08-31 21:01:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181271.4797535 | source=vosk | rms=735 | updated_at=1788181270.730768 | frequency_hz=198.0
- [2026-08-31 21:01:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181272.9800935 | source=vosk | rms=735 | updated_at=1788181270.730768 | frequency_hz=198.0
- [2026-08-31 21:01:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181273.480611 | source=vosk | rms=735 | updated_at=1788181270.730768 | frequency_hz=198.0
- [2026-08-31 21:01:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181273.980491 | source=vosk | rms=302 | updated_at=1788181273.980491 | frequency_hz=198.0
- [2026-08-31 21:01:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181274.7820654 | source=vosk | rms=302 | updated_at=1788181273.980491 | frequency_hz=198.0
- [2026-08-31 21:01:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181275.5320828 | source=vosk | rms=323 | updated_at=1788181275.5320828 | frequency_hz=198.0
- [2026-08-31 21:01:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181277.497752 | source=vosk | rms=279 | updated_at=1788181276.5323832 | frequency_hz=198.0
- [2026-08-31 21:01:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181277.992686 | source=vosk | rms=563 | updated_at=1788181277.992686 | frequency_hz=262.0
- [2026-08-31 21:01:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181278.7436602 | source=vosk | rms=563 | updated_at=1788181277.992686 | frequency_hz=262.0
- [2026-08-31 21:01:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181279.2424924 | source=vosk | rms=696 | updated_at=1788181279.2424924 | frequency_hz=262.0
- [2026-08-31 21:01:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181279.7423842 | source=vosk | rms=696 | updated_at=1788181279.2424924 | frequency_hz=262.0
- [2026-08-31 21:01:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181285.0125802 | source=vosk | rms=696 | updated_at=1788181279.2424924 | frequency_hz=262.0
- [2026-08-31 21:01:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181285.492666 | source=vosk | rms=696 | updated_at=1788181279.2424924 | frequency_hz=262.0
- [2026-08-31 21:01:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181286.2435873 | source=vosk | rms=356 | updated_at=1788181286.2435873 | frequency_hz=262.0
- [2026-08-31 21:01:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181286.7411156 | source=vosk | rms=356 | updated_at=1788181286.2435873 | frequency_hz=262.0
- [2026-08-31 21:01:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181287.9926097 | source=vosk | rms=316 | updated_at=1788181287.9926097 | frequency_hz=262.0
- [2026-08-31 21:01:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181288.4929729 | source=vosk | rms=316 | updated_at=1788181287.9926097 | frequency_hz=262.0
- [2026-08-31 21:01:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181290.992684 | source=vosk | rms=432 | updated_at=1788181290.992684 | frequency_hz=156.0
- [2026-08-31 21:01:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181291.492816 | source=vosk | rms=432 | updated_at=1788181290.992684 | frequency_hz=156.0
- [2026-08-31 21:01:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181293.8782656 | source=vosk | rms=421 | updated_at=1788181293.8782656 | frequency_hz=156.0
- [2026-08-31 21:01:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181294.3785565 | source=vosk | rms=421 | updated_at=1788181293.8782656 | frequency_hz=156.0
- [2026-08-31 21:01:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181295.1280572 | source=vosk | rms=819 | updated_at=1788181295.1280572 | frequency_hz=156.0
- [2026-08-31 21:01:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181295.8787193 | source=vosk | rms=429 | updated_at=1788181295.3782935 | frequency_hz=156.0
- [2026-08-31 21:01:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181297.3796864 | source=vosk | rms=429 | updated_at=1788181295.3782935 | frequency_hz=156.0
- [2026-08-31 21:01:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181302.8784738 | source=vosk | rms=260 | updated_at=1788181300.8787758 | frequency_hz=156.0
- [2026-08-31 21:01:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181303.128932 | source=vosk | rms=260 | updated_at=1788181300.8787758 | frequency_hz=156.0
- [2026-08-31 21:01:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181304.1284266 | source=vosk | rms=260 | updated_at=1788181300.8787758 | frequency_hz=156.0
- [2026-08-31 21:01:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181305.3790905 | source=vosk | rms=306 | updated_at=1788181305.3790905 | frequency_hz=156.0
- [2026-08-31 21:01:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181307.5914993 | source=vosk | rms=192 | updated_at=1788181306.8787248 | frequency_hz=156.0
- [2026-08-31 21:01:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181307.8793604 | source=vosk | rms=296 | updated_at=1788181307.8793604 | frequency_hz=156.0
- [2026-08-31 21:01:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181308.6290066 | source=vosk | rms=544 | updated_at=1788181308.1325252 | frequency_hz=147.6
- [2026-08-31 21:01:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181309.129462 | source=vosk | rms=372 | updated_at=1788181309.129462 | frequency_hz=147.6
- [2026-08-31 21:01:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181309.9810834 | source=vosk | rms=372 | updated_at=1788181309.129462 | frequency_hz=147.6
- [2026-08-31 21:01:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181311.2075968 | source=vosk | rms=199 | updated_at=1788181311.2075968 | frequency_hz=147.6
- [2026-08-31 21:01:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181313.4929547 | source=vosk | rms=121 | updated_at=1788181312.9935086 | frequency_hz=147.6
- [2026-08-31 21:01:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181313.7440627 | source=vosk | rms=142 | updated_at=1788181313.7440627 | frequency_hz=147.6
- [2026-08-31 21:01:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181316.2426305 | source=vosk | rms=381 | updated_at=1788181315.7434285 | frequency_hz=147.6
- [2026-08-31 21:02:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181321.9934359 | source=vosk | rms=381 | updated_at=1788181315.7434285 | frequency_hz=147.6
- [2026-08-31 21:02:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181323.7433221 | source=vosk | rms=889 | updated_at=1788181323.2442083 | frequency_hz=147.6
- [2026-08-31 21:02:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181324.4982622 | source=vosk | rms=889 | updated_at=1788181323.2442083 | frequency_hz=147.6
- [2026-08-31 21:02:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181325.993535 | source=vosk | rms=380 | updated_at=1788181325.4935522 | frequency_hz=147.6
- [2026-08-31 21:02:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181327.2466383 | source=vosk | rms=380 | updated_at=1788181325.4935522 | frequency_hz=147.6
- [2026-08-31 21:02:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181328.9928288 | source=vosk | rms=261 | updated_at=1788181328.4937294 | frequency_hz=147.6
- [2026-08-31 21:02:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181330.4959598 | source=vosk | rms=541 | updated_at=1788181330.4959598 | frequency_hz=147.6
- [2026-08-31 21:02:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181332.247264 | source=vosk | rms=364 | updated_at=1788181331.782813 | frequency_hz=147.6
- [2026-08-31 21:02:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181332.7435403 | source=vosk | rms=348 | updated_at=1788181332.7435403 | frequency_hz=147.6
- [2026-08-31 21:02:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181334.243637 | source=vosk | rms=832 | updated_at=1788181333.5030413 | frequency_hz=147.6
- [2026-08-31 21:02:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181334.9924881 | source=vosk | rms=659 | updated_at=1788181334.9924881 | frequency_hz=147.6
- [2026-08-31 21:02:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181335.4961624 | source=vosk | rms=659 | updated_at=1788181334.9924881 | frequency_hz=147.6
- [2026-08-31 21:02:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181336.243888 | source=vosk | rms=217 | updated_at=1788181336.243888 | frequency_hz=147.6
- [2026-08-31 21:02:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181336.74338 | source=vosk | rms=217 | updated_at=1788181336.243888 | frequency_hz=147.6
- [2026-08-31 21:02:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181336.993357 | source=vosk | rms=140 | updated_at=1788181336.993357 | frequency_hz=193.9
- [2026-08-31 21:02:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181337.4927227 | source=vosk | rms=140 | updated_at=1788181336.993357 | frequency_hz=193.9
- [2026-08-31 21:02:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181337.9951255 | source=vosk | rms=140 | updated_at=1788181336.993357 | frequency_hz=193.9
- [2026-08-31 21:02:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181339.4935913 | source=vosk | rms=140 | updated_at=1788181336.993357 | frequency_hz=193.9
- [2026-08-31 21:02:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181342.2433298 | source=vosk | rms=140 | updated_at=1788181336.993357 | frequency_hz=193.9
- [2026-08-31 21:02:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181342.6850061 | source=vosk | rms=140 | updated_at=1788181336.993357 | frequency_hz=193.9
- [2026-08-31 21:02:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181345.7446103 | source=vosk | rms=140 | updated_at=1788181336.993357 | frequency_hz=193.9
- [2026-08-31 21:02:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181346.2437172 | source=vosk | rms=140 | updated_at=1788181336.993357 | frequency_hz=193.9
- [2026-08-31 21:02:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181349.2435853 | source=vosk | rms=270 | updated_at=1788181349.2435853 | frequency_hz=280.0
- [2026-08-31 21:02:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181350.4932172 | source=vosk | rms=621 | updated_at=1788181349.7437837 | frequency_hz=280.0
- [2026-08-31 21:02:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181354.9979765 | source=vosk | rms=144 | updated_at=1788181354.9979765 | frequency_hz=280.0
- [2026-08-31 21:02:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181355.7433817 | source=vosk | rms=510 | updated_at=1788181355.2493546 | frequency_hz=280.0
- [2026-08-31 21:02:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181356.7449784 | source=vosk | rms=302 | updated_at=1788181356.7449784 | frequency_hz=244.0
- [2026-08-31 21:02:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181357.4934556 | source=vosk | rms=172 | updated_at=1788181356.993844 | frequency_hz=277.6
- [2026-08-31 21:02:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181358.9939275 | source=vosk | rms=172 | updated_at=1788181356.993844 | frequency_hz=277.6
- [2026-08-31 21:02:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181359.504118 | source=vosk | rms=172 | updated_at=1788181356.993844 | frequency_hz=277.6
- [2026-08-31 21:02:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181359.9934685 | source=vosk | rms=172 | updated_at=1788181356.993844 | frequency_hz=277.6
- [2026-08-31 21:02:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181360.9934 | source=vosk | rms=578 | updated_at=1788181360.4935353 | frequency_hz=277.6
- [2026-08-31 21:02:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181362.2451289 | source=vosk | rms=188 | updated_at=1788181362.2451289 | frequency_hz=277.6
- [2026-08-31 21:02:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181362.7442396 | source=vosk | rms=188 | updated_at=1788181362.2451289 | frequency_hz=277.6
- [2026-08-31 21:02:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181362.9942179 | source=vosk | rms=446 | updated_at=1788181362.9942179 | frequency_hz=277.6
- [2026-08-31 21:02:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181363.7440593 | source=vosk | rms=143 | updated_at=1788181363.2438462 | frequency_hz=310.6
- [2026-08-31 21:02:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181366.2597837 | source=vosk | rms=556 | updated_at=1788181366.2597837 | frequency_hz=310.6
- [2026-08-31 21:02:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181367.9942095 | source=vosk | rms=131 | updated_at=1788181367.5170915 | frequency_hz=310.6
- [2026-08-31 21:02:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181368.2706816 | source=vosk | rms=381 | updated_at=1788181368.2706816 | frequency_hz=310.6
- [2026-08-31 21:02:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181368.7479963 | source=vosk | rms=381 | updated_at=1788181368.2706816 | frequency_hz=310.6
- [2026-08-31 21:02:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181369.243678 | source=vosk | rms=366 | updated_at=1788181369.243678 | frequency_hz=310.6
- [2026-08-31 21:02:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181373.2444887 | source=vosk | rms=140 | updated_at=1788181372.743667 | frequency_hz=310.6
- [2026-08-31 21:02:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181373.9961462 | source=vosk | rms=140 | updated_at=1788181372.743667 | frequency_hz=310.6
- [2026-08-31 21:02:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181374.9942744 | source=vosk | rms=288 | updated_at=1788181374.4941769 | frequency_hz=310.6
- [2026-08-31 21:02:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181375.9936912 | source=vosk | rms=374 | updated_at=1788181375.9936912 | frequency_hz=310.6
- [2026-08-31 21:02:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181377.0141723 | source=vosk | rms=374 | updated_at=1788181375.9936912 | frequency_hz=310.6
- [2026-08-31 21:02:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181377.2472978 | source=vosk | rms=272 | updated_at=1788181377.2472978 | frequency_hz=310.6
- [2026-08-31 21:02:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181378.2440243 | source=vosk | rms=287 | updated_at=1788181377.7438037 | frequency_hz=310.6
- [2026-08-31 21:02:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181378.5043187 | source=vosk | rms=287 | updated_at=1788181377.7438037 | frequency_hz=310.6
- [2026-08-31 21:03:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181380.2556815 | source=vosk | rms=190 | updated_at=1788181379.7442536 | frequency_hz=310.6
- [2026-08-31 21:03:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181383.5313537 | source=vosk | rms=224 | updated_at=1788181383.5313537 | frequency_hz=310.6
- [2026-08-31 21:03:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181384.994414 | source=vosk | rms=257 | updated_at=1788181384.244777 | frequency_hz=310.6
- [2026-08-31 21:03:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181385.2439232 | source=vosk | rms=308 | updated_at=1788181385.2439232 | frequency_hz=310.6
- [2026-08-31 21:03:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181385.7442808 | source=vosk | rms=308 | updated_at=1788181385.2439232 | frequency_hz=310.6
- [2026-08-31 21:03:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181388.756592 | source=vosk | rms=714 | updated_at=1788181388.756592 | frequency_hz=310.6
- [2026-08-31 21:03:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181389.2441542 | source=vosk | rms=714 | updated_at=1788181388.756592 | frequency_hz=310.6
- [2026-08-31 21:03:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181389.5073717 | source=vosk | rms=612 | updated_at=1788181389.5073717 | frequency_hz=310.6
- [2026-08-31 21:03:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181390.255857 | source=vosk | rms=612 | updated_at=1788181389.5073717 | frequency_hz=310.6
- [2026-08-31 21:03:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181390.9947977 | source=vosk | rms=201 | updated_at=1788181390.9947977 | frequency_hz=310.6
- [2026-08-31 21:03:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181397.2446349 | source=vosk | rms=341 | updated_at=1788181396.7445202 | frequency_hz=310.6
- [2026-08-31 21:03:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181397.9941795 | source=vosk | rms=344 | updated_at=1788181397.9941795 | frequency_hz=310.6
- [2026-08-31 21:03:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181398.5129359 | source=vosk | rms=344 | updated_at=1788181397.9941795 | frequency_hz=310.6
- [2026-08-31 21:03:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181400.2465217 | source=vosk | rms=344 | updated_at=1788181397.9941795 | frequency_hz=310.6
- [2026-08-31 21:03:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181400.7447743 | source=vosk | rms=344 | updated_at=1788181397.9941795 | frequency_hz=310.6
- [2026-08-31 21:03:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181401.506026 | source=vosk | rms=1200 | updated_at=1788181401.506026 | frequency_hz=310.6
- [2026-08-31 21:03:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181402.2703602 | source=vosk | rms=562 | updated_at=1788181401.7459893 | frequency_hz=310.6
- [2026-08-31 21:03:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181402.754818 | source=vosk | rms=562 | updated_at=1788181401.7459893 | frequency_hz=310.6
- [2026-08-31 21:03:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181403.2479932 | source=vosk | rms=562 | updated_at=1788181401.7459893 | frequency_hz=310.6
- [2026-08-31 21:03:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181404.0096538 | source=vosk | rms=1201 | updated_at=1788181404.0096538 | frequency_hz=310.6
- [2026-08-31 21:03:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181404.7502193 | source=vosk | rms=288 | updated_at=1788181404.2616303 | frequency_hz=310.6
- [2026-08-31 21:03:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181405.7451162 | source=vosk | rms=358 | updated_at=1788181405.7451162 | frequency_hz=370.0
- [2026-08-31 21:03:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181407.2451031 | source=vosk | rms=564 | updated_at=1788181406.744414 | frequency_hz=370.0
- [2026-08-31 21:03:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181407.745916 | source=vosk | rms=449 | updated_at=1788181407.7449098 | frequency_hz=370.0
- [2026-08-31 21:03:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181408.2782528 | source=vosk | rms=449 | updated_at=1788181407.7449098 | frequency_hz=370.0
- [2026-08-31 21:03:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181410.4959233 | source=vosk | rms=449 | updated_at=1788181407.7449098 | frequency_hz=370.0
- [2026-08-31 21:03:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181411.2449014 | source=vosk | rms=449 | updated_at=1788181407.7449098 | frequency_hz=370.0
- [2026-08-31 21:03:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181414.5019479 | source=vosk | rms=1203 | updated_at=1788181414.5019479 | frequency_hz=370.0
- [2026-08-31 21:03:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181415.1639197 | source=vosk | rms=1203 | updated_at=1788181414.5019479 | frequency_hz=370.0
- [2026-08-31 21:03:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181415.9954205 | source=vosk | rms=470 | updated_at=1788181415.9954205 | frequency_hz=370.0
- [2026-08-31 21:03:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181416.745398 | source=vosk | rms=266 | updated_at=1788181416.2446053 | frequency_hz=370.0
- [2026-08-31 21:03:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181416.994706 | source=vosk | rms=1205 | updated_at=1788181416.994706 | frequency_hz=370.0
- [2026-08-31 21:03:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181418.7452614 | source=vosk | rms=975 | updated_at=1788181418.2451136 | frequency_hz=370.0
- [2026-08-31 21:03:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181419.7451422 | source=vosk | rms=1201 | updated_at=1788181419.7451422 | frequency_hz=370.0
- [2026-08-31 21:03:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181420.2453077 | source=vosk | rms=1201 | updated_at=1788181419.7451422 | frequency_hz=370.0
- [2026-08-31 21:03:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181420.494694 | source=vosk | rms=1201 | updated_at=1788181419.7451422 | frequency_hz=370.0
- [2026-08-31 21:03:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181420.9954066 | source=vosk | rms=1201 | updated_at=1788181419.7451422 | frequency_hz=370.0
- [2026-08-31 21:03:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181426.7482932 | source=vosk | rms=904 | updated_at=1788181426.7482932 | frequency_hz=370.0
- [2026-08-31 21:03:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181427.24546 | source=vosk | rms=904 | updated_at=1788181426.7482932 | frequency_hz=370.0
- [2026-08-31 21:03:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181428.2591457 | source=vosk | rms=513 | updated_at=1788181428.2591457 | frequency_hz=364.0
- [2026-08-31 21:03:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181428.9956386 | source=vosk | rms=837 | updated_at=1788181428.495009 | frequency_hz=364.0
- [2026-08-31 21:03:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181429.2449372 | source=vosk | rms=465 | updated_at=1788181429.2449372 | frequency_hz=364.0
- [2026-08-31 21:03:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181429.745333 | source=vosk | rms=465 | updated_at=1788181429.2449372 | frequency_hz=364.0
- [2026-08-31 21:03:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181430.2488668 | source=vosk | rms=200 | updated_at=1788181430.2488668 | frequency_hz=364.0
- [2026-08-31 21:03:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181430.7453656 | source=vosk | rms=200 | updated_at=1788181430.2488668 | frequency_hz=364.0
- [2026-08-31 21:03:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181432.7451515 | source=vosk | rms=258 | updated_at=1788181432.7451515 | frequency_hz=364.0
- [2026-08-31 21:03:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181434.0412688 | source=vosk | rms=347 | updated_at=1788181433.495158 | frequency_hz=364.0
- [2026-08-31 21:03:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181436.245534 | source=vosk | rms=254 | updated_at=1788181436.245534 | frequency_hz=364.0
- [2026-08-31 21:04:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181441.9957962 | source=vosk | rms=1206 | updated_at=1788181441.4946647 | frequency_hz=364.0
- [2026-08-31 21:04:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181442.2478483 | source=vosk | rms=921 | updated_at=1788181442.2478483 | frequency_hz=364.0
- [2026-08-31 21:04:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181443.4963229 | source=vosk | rms=399 | updated_at=1788181442.9958975 | frequency_hz=364.0
- [2026-08-31 21:04:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181444.4954813 | source=vosk | rms=853 | updated_at=1788181444.4954813 | frequency_hz=364.0
- [2026-08-31 21:04:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181444.9953942 | source=vosk | rms=853 | updated_at=1788181444.4954813 | frequency_hz=364.0
- [2026-08-31 21:04:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181445.4952266 | source=vosk | rms=676 | updated_at=1788181445.4952266 | frequency_hz=364.0
- [2026-08-31 21:04:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181446.99654 | source=vosk | rms=1083 | updated_at=1788181446.4955451 | frequency_hz=364.0
- [2026-08-31 21:04:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181447.4953268 | source=vosk | rms=1083 | updated_at=1788181446.4955451 | frequency_hz=364.0
- [2026-08-31 21:04:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181447.9987583 | source=vosk | rms=1083 | updated_at=1788181446.4955451 | frequency_hz=364.0
- [2026-08-31 21:04:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181448.4955726 | source=vosk | rms=344 | updated_at=1788181448.4955726 | frequency_hz=364.0
- [2026-08-31 21:04:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181448.9953258 | source=vosk | rms=344 | updated_at=1788181448.4955726 | frequency_hz=364.0
- [2026-08-31 21:04:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181449.2475748 | source=vosk | rms=344 | updated_at=1788181448.4955726 | frequency_hz=364.0
- [2026-08-31 21:04:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181450.745535 | source=vosk | rms=273 | updated_at=1788181450.2460887 | frequency_hz=364.0
- [2026-08-31 21:04:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181450.99555 | source=vosk | rms=1180 | updated_at=1788181450.99555 | frequency_hz=364.0
- [2026-08-31 21:04:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181452.7459252 | source=vosk | rms=625 | updated_at=1788181451.9958231 | frequency_hz=364.0
- [2026-08-31 21:04:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181453.7454996 | source=vosk | rms=1203 | updated_at=1788181453.7454996 | frequency_hz=364.0
- [2026-08-31 21:04:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181454.495412 | source=vosk | rms=211 | updated_at=1788181453.9954464 | frequency_hz=364.0
- [2026-08-31 21:04:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181456.2454062 | source=vosk | rms=211 | updated_at=1788181453.9954464 | frequency_hz=364.0
- [2026-08-31 21:04:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181456.7474492 | source=vosk | rms=211 | updated_at=1788181453.9954464 | frequency_hz=364.0
- [2026-08-31 21:04:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181460.2454405 | source=vosk | rms=211 | updated_at=1788181453.9954464 | frequency_hz=364.0
- [2026-08-31 21:04:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181460.746023 | source=vosk | rms=211 | updated_at=1788181453.9954464 | frequency_hz=364.0
- [2026-08-31 21:04:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181460.995865 | source=vosk | rms=375 | updated_at=1788181460.995865 | frequency_hz=364.0
- [2026-08-31 21:04:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181461.506161 | source=vosk | rms=375 | updated_at=1788181460.995865 | frequency_hz=364.0
- [2026-08-31 21:04:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181461.7647998 | source=vosk | rms=283 | updated_at=1788181461.7647998 | frequency_hz=309.4
- [2026-08-31 21:04:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181462.4971945 | source=vosk | rms=422 | updated_at=1788181462.0099094 | frequency_hz=309.4
- [2026-08-31 21:04:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181463.2461345 | source=vosk | rms=251 | updated_at=1788181463.2461345 | frequency_hz=309.4
- [2026-08-31 21:04:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181463.7455835 | source=vosk | rms=251 | updated_at=1788181463.2461345 | frequency_hz=309.4
- [2026-08-31 21:04:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181463.9960315 | source=vosk | rms=251 | updated_at=1788181463.2461345 | frequency_hz=309.4
- [2026-08-31 21:04:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181465.2456725 | source=vosk | rms=828 | updated_at=1788181464.4953709 | frequency_hz=309.4
- [2026-08-31 21:04:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181465.6002307 | source=vosk | rms=828 | updated_at=1788181464.4953709 | frequency_hz=309.4
- [2026-08-31 21:04:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181466.4961147 | source=vosk | rms=828 | updated_at=1788181464.4953709 | frequency_hz=309.4
- [2026-08-31 21:04:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181467.9970844 | source=vosk | rms=369 | updated_at=1788181467.9970844 | frequency_hz=309.4
- [2026-08-31 21:04:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181469.7550554 | source=vosk | rms=437 | updated_at=1788181468.996256 | frequency_hz=309.4
- [2026-08-31 21:04:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181470.7461283 | source=vosk | rms=779 | updated_at=1788181470.7461283 | frequency_hz=309.4
- [2026-08-31 21:04:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181471.49615 | source=vosk | rms=1203 | updated_at=1788181470.9963021 | frequency_hz=309.4
- [2026-08-31 21:04:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181472.4964983 | source=vosk | rms=435 | updated_at=1788181472.4964983 | frequency_hz=309.4
- [2026-08-31 21:04:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181473.7464163 | source=vosk | rms=282 | updated_at=1788181473.0004096 | frequency_hz=309.4
- [2026-08-31 21:04:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181474.5036628 | source=vosk | rms=282 | updated_at=1788181473.0004096 | frequency_hz=309.4
- [2026-08-31 21:04:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181475.4960713 | source=vosk | rms=282 | updated_at=1788181473.0004096 | frequency_hz=309.4
- [2026-08-31 21:04:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181475.7552886 | source=vosk | rms=1204 | updated_at=1788181475.7552886 | frequency_hz=309.4
- [2026-08-31 21:04:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181477.4964929 | source=vosk | rms=678 | updated_at=1788181476.995748 | frequency_hz=309.4
- [2026-08-31 21:04:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181477.9972868 | source=vosk | rms=678 | updated_at=1788181476.995748 | frequency_hz=309.4
- [2026-08-31 21:04:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181479.2540083 | source=vosk | rms=231 | updated_at=1788181478.7458513 | frequency_hz=309.4
- [2026-08-31 21:04:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181479.7463317 | source=vosk | rms=1201 | updated_at=1788181479.7463317 | frequency_hz=309.4
- [2026-08-31 21:04:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181480.2465572 | source=vosk | rms=1201 | updated_at=1788181479.7463317 | frequency_hz=309.4
- [2026-08-31 21:04:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181480.9963274 | source=vosk | rms=672 | updated_at=1788181480.9963274 | frequency_hz=309.4
- [2026-08-31 21:04:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181481.764696 | source=vosk | rms=672 | updated_at=1788181480.9963274 | frequency_hz=309.4
- [2026-08-31 21:04:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181482.000224 | source=vosk | rms=224 | updated_at=1788181482.000224 | frequency_hz=309.4
- [2026-08-31 21:04:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181483.246401 | source=vosk | rms=563 | updated_at=1788181482.7461271 | frequency_hz=309.4
- [2026-08-31 21:04:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181483.99666 | source=vosk | rms=563 | updated_at=1788181482.7461271 | frequency_hz=309.4
- [2026-08-31 21:04:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181484.528497 | source=vosk | rms=563 | updated_at=1788181482.7461271 | frequency_hz=309.4
- [2026-08-31 21:04:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181484.995861 | source=vosk | rms=563 | updated_at=1788181482.7461271 | frequency_hz=309.4
- [2026-08-31 21:04:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181486.2468638 | source=vosk | rms=1205 | updated_at=1788181485.746292 | frequency_hz=309.4
- [2026-08-31 21:04:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181487.9962366 | source=vosk | rms=296 | updated_at=1788181487.9962366 | frequency_hz=309.4
- [2026-08-31 21:04:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181488.7459795 | source=vosk | rms=296 | updated_at=1788181487.9962366 | frequency_hz=309.4
- [2026-08-31 21:04:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181489.7462757 | source=vosk | rms=362 | updated_at=1788181489.7462757 | frequency_hz=309.4
- [2026-08-31 21:04:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181490.2581031 | source=vosk | rms=362 | updated_at=1788181489.7462757 | frequency_hz=309.4
- [2026-08-31 21:04:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181490.4965577 | source=vosk | rms=362 | updated_at=1788181489.7462757 | frequency_hz=309.4
- [2026-08-31 21:04:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181490.9965568 | source=vosk | rms=362 | updated_at=1788181489.7462757 | frequency_hz=309.4
- [2026-08-31 21:04:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181491.4961889 | source=vosk | rms=189 | updated_at=1788181491.4961889 | frequency_hz=309.4
- [2026-08-31 21:04:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181492.498397 | source=vosk | rms=260 | updated_at=1788181491.99654 | frequency_hz=309.4
- [2026-08-31 21:04:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181492.996614 | source=vosk | rms=507 | updated_at=1788181492.996614 | frequency_hz=309.4
- [2026-08-31 21:04:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181493.4965692 | source=vosk | rms=507 | updated_at=1788181492.996614 | frequency_hz=309.4
- [2026-08-31 21:04:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181494.0097823 | source=vosk | rms=507 | updated_at=1788181492.996614 | frequency_hz=309.4
- [2026-08-31 21:04:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181494.7483919 | source=vosk | rms=344 | updated_at=1788181494.2465832 | frequency_hz=309.4
- [2026-08-31 21:04:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181495.0016413 | source=vosk | rms=737 | updated_at=1788181495.0016413 | frequency_hz=309.4
- [2026-08-31 21:04:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181495.7470548 | source=vosk | rms=564 | updated_at=1788181495.246916 | frequency_hz=309.4
- [2026-08-31 21:04:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181496.0016558 | source=vosk | rms=1148 | updated_at=1788181496.0016558 | frequency_hz=309.4
- [2026-08-31 21:04:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181496.4964511 | source=vosk | rms=1148 | updated_at=1788181496.0016558 | frequency_hz=309.4
- [2026-08-31 21:04:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181496.7827294 | source=vosk | rms=248 | updated_at=1788181496.7827294 | frequency_hz=309.4
- [2026-08-31 21:04:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181497.2471278 | source=vosk | rms=248 | updated_at=1788181496.7827294 | frequency_hz=309.4
- [2026-08-31 21:04:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181497.496144 | source=vosk | rms=248 | updated_at=1788181496.7827294 | frequency_hz=309.4
- [2026-08-31 21:04:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181498.250685 | source=vosk | rms=248 | updated_at=1788181496.7827294 | frequency_hz=309.4
- [2026-08-31 21:04:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181498.7462814 | source=vosk | rms=431 | updated_at=1788181498.7462814 | frequency_hz=309.4
- [2026-08-31 21:05:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181500.5458446 | source=vosk | rms=1202 | updated_at=1788181499.5131547 | frequency_hz=309.4
- [2026-08-31 21:05:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181501.306068 | source=vosk | rms=289 | updated_at=1788181501.306068 | frequency_hz=309.4
- [2026-08-31 21:05:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181503.046737 | source=vosk | rms=277 | updated_at=1788181502.5566285 | frequency_hz=309.4
- [2026-08-31 21:05:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181503.5462759 | source=vosk | rms=277 | updated_at=1788181502.5566285 | frequency_hz=309.4
- [2026-08-31 21:05:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181504.3130188 | source=vosk | rms=1001 | updated_at=1788181503.7975273 | frequency_hz=309.4
- [2026-08-31 21:05:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181505.0478115 | source=vosk | rms=313 | updated_at=1788181505.0478115 | frequency_hz=309.4
- [2026-08-31 21:05:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181508.3165643 | source=vosk | rms=309 | updated_at=1788181507.8166988 | frequency_hz=309.4
- [2026-08-31 21:05:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181508.5665665 | source=vosk | rms=309 | updated_at=1788181507.8166988 | frequency_hz=309.4
- [2026-08-31 21:05:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181509.0666423 | source=vosk | rms=309 | updated_at=1788181507.8166988 | frequency_hz=309.4
- [2026-08-31 21:05:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181509.3165054 | source=vosk | rms=362 | updated_at=1788181509.3165054 | frequency_hz=309.4
- [2026-08-31 21:05:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181511.316914 | source=vosk | rms=1200 | updated_at=1788181510.0671525 | frequency_hz=309.4
- [2026-08-31 21:05:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181514.093541 | source=vosk | rms=1200 | updated_at=1788181510.0671525 | frequency_hz=309.4
- [2026-08-31 21:05:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181514.5870612 | source=vosk | rms=1200 | updated_at=1788181510.0671525 | frequency_hz=309.4
- [2026-08-31 21:05:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181515.3176281 | source=vosk | rms=1200 | updated_at=1788181510.0671525 | frequency_hz=309.4
- [2026-08-31 21:05:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181516.5670643 | source=vosk | rms=461 | updated_at=1788181516.0668278 | frequency_hz=309.4
- [2026-08-31 21:05:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181519.0662222 | source=vosk | rms=1204 | updated_at=1788181519.0662222 | frequency_hz=309.4
- [2026-08-31 21:05:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181519.8174338 | source=vosk | rms=340 | updated_at=1788181519.316978 | frequency_hz=309.4
- [2026-08-31 21:05:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181520.0871294 | source=vosk | rms=368 | updated_at=1788181520.0871294 | frequency_hz=309.4
- [2026-08-31 21:05:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181520.817414 | source=vosk | rms=368 | updated_at=1788181520.0871294 | frequency_hz=309.4
- [2026-08-31 21:05:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181521.572014 | source=vosk | rms=2014 | updated_at=1788181521.572014 | frequency_hz=309.4
- [2026-08-31 21:05:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181523.5665221 | source=vosk | rms=280 | updated_at=1788181523.0705256 | frequency_hz=309.4
- [2026-08-31 21:05:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181524.5666978 | source=vosk | rms=338 | updated_at=1788181524.5666978 | frequency_hz=309.4
- [2026-08-31 21:05:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181525.3171544 | source=vosk | rms=301 | updated_at=1788181524.824405 | frequency_hz=309.4
- [2026-08-31 21:05:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181525.8174386 | source=vosk | rms=301 | updated_at=1788181524.824405 | frequency_hz=309.4
- [2026-08-31 21:05:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181526.5671926 | source=vosk | rms=301 | updated_at=1788181524.824405 | frequency_hz=309.4
- [2026-08-31 21:05:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181530.5674741 | source=vosk | rms=301 | updated_at=1788181524.824405 | frequency_hz=309.4
- [2026-08-31 21:05:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181534.4892 | source=vosk | rms=1202 | updated_at=1788181534.0675051 | frequency_hz=309.4
- [2026-08-31 21:05:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181534.5738914 | source=vosk | rms=1200 | updated_at=1788181534.5738914 | frequency_hz=309.4
- [2026-08-31 21:05:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181535.0703342 | source=vosk | rms=1200 | updated_at=1788181534.5738914 | frequency_hz=309.4
- [2026-08-31 21:05:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181535.5671446 | source=vosk | rms=637 | updated_at=1788181535.5671446 | frequency_hz=309.4
- [2026-08-31 21:05:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181536.3169537 | source=vosk | rms=637 | updated_at=1788181535.5671446 | frequency_hz=309.4
- [2026-08-31 21:05:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181537.316877 | source=vosk | rms=509 | updated_at=1788181537.316877 | frequency_hz=309.4
- [2026-08-31 21:05:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181540.0669682 | source=vosk | rms=510 | updated_at=1788181538.8171782 | frequency_hz=309.4
- [2026-08-31 21:05:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181540.3171825 | source=vosk | rms=618 | updated_at=1788181540.3171825 | frequency_hz=309.4
- [2026-08-31 21:05:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181541.8253486 | source=vosk | rms=245 | updated_at=1788181540.5675125 | frequency_hz=309.4
- [2026-08-31 21:05:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181542.0771253 | source=vosk | rms=804 | updated_at=1788181542.0771253 | frequency_hz=309.4
- [2026-08-31 21:05:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181544.3119211 | source=vosk | rms=1204 | updated_at=1788181543.307756 | frequency_hz=309.4
- [2026-08-31 21:05:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181544.5581238 | source=vosk | rms=1204 | updated_at=1788181543.307756 | frequency_hz=309.4
- [2026-08-31 21:05:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181546.557984 | source=vosk | rms=648 | updated_at=1788181545.565445 | frequency_hz=309.4
- [2026-08-31 21:05:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181548.310074 | source=vosk | rms=1206 | updated_at=1788181548.310074 | frequency_hz=309.4
- [2026-08-31 21:05:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181549.074589 | source=vosk | rms=909 | updated_at=1788181548.5579786 | frequency_hz=309.4
- [2026-08-31 21:05:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181549.3082018 | source=vosk | rms=1203 | updated_at=1788181549.3082018 | frequency_hz=309.4
- [2026-08-31 21:05:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181550.0575113 | source=vosk | rms=1203 | updated_at=1788181549.3082018 | frequency_hz=309.4
- [2026-08-31 21:05:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181550.5579672 | source=vosk | rms=418 | updated_at=1788181550.5579672 | frequency_hz=309.4
- [2026-08-31 21:05:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181553.5574093 | source=vosk | rms=1200 | updated_at=1788181552.8081045 | frequency_hz=309.4
- [2026-08-31 21:05:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181553.8077366 | source=vosk | rms=642 | updated_at=1788181553.8077366 | frequency_hz=309.4
- [2026-08-31 21:06:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181560.808772 | source=vosk | rms=1098 | updated_at=1788181560.0609872 | frequency_hz=309.4
- [2026-08-31 21:06:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181570.5582647 | source=vosk | rms=523 | updated_at=1788181570.5582647 | frequency_hz=309.4
- [2026-08-31 21:06:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181572.3079882 | source=vosk | rms=1201 | updated_at=1788181571.8077211 | frequency_hz=309.4
- [2026-08-31 21:06:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181574.3076725 | source=vosk | rms=1201 | updated_at=1788181571.8077211 | frequency_hz=309.4
- [2026-08-31 21:06:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181575.0577037 | source=vosk | rms=965 | updated_at=1788181574.5577228 | frequency_hz=309.4
- [2026-08-31 21:06:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181575.5926943 | source=vosk | rms=559 | updated_at=1788181575.5926943 | frequency_hz=309.4
- [2026-08-31 21:06:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181576.5581753 | source=vosk | rms=675 | updated_at=1788181576.0627186 | frequency_hz=309.4
- [2026-08-31 21:06:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181578.8194826 | source=vosk | rms=1203 | updated_at=1788181578.8194826 | frequency_hz=309.4
- [2026-08-31 21:06:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181580.8085306 | source=vosk | rms=1202 | updated_at=1788181580.3092027 | frequency_hz=309.4
- [2026-08-31 21:06:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181581.067084 | source=vosk | rms=1116 | updated_at=1788181581.067084 | frequency_hz=266.9
- [2026-08-31 21:06:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181581.5612268 | source=vosk | rms=1116 | updated_at=1788181581.067084 | frequency_hz=266.9
- [2026-08-31 21:06:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181583.0577865 | source=vosk | rms=1116 | updated_at=1788181581.067084 | frequency_hz=266.9
- [2026-08-31 21:06:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181583.557931 | source=vosk | rms=1116 | updated_at=1788181581.067084 | frequency_hz=266.9
- [2026-08-31 21:06:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181586.3090804 | source=vosk | rms=808 | updated_at=1788181586.3090804 | frequency_hz=266.9
- [2026-08-31 21:06:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181586.8121102 | source=vosk | rms=808 | updated_at=1788181586.3090804 | frequency_hz=266.9
- [2026-08-31 21:06:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181588.8084137 | source=vosk | rms=808 | updated_at=1788181586.3090804 | frequency_hz=266.9
- [2026-08-31 21:06:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181589.3094802 | source=vosk | rms=808 | updated_at=1788181586.3090804 | frequency_hz=266.9
- [2026-08-31 21:06:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181593.5587702 | source=vosk | rms=500 | updated_at=1788181593.5587702 | frequency_hz=402.0
- [2026-08-31 21:06:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181594.3095303 | source=vosk | rms=500 | updated_at=1788181593.5587702 | frequency_hz=402.0
- [2026-08-31 21:06:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181600.5588462 | source=vosk | rms=239 | updated_at=1788181600.5588462 | frequency_hz=300.0
- [2026-08-31 21:06:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181601.3348157 | source=vosk | rms=239 | updated_at=1788181600.5588462 | frequency_hz=300.0
- [2026-08-31 21:06:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181601.5597703 | source=vosk | rms=239 | updated_at=1788181600.5588462 | frequency_hz=300.0
- [2026-08-31 21:06:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181602.0583978 | source=vosk | rms=239 | updated_at=1788181600.5588462 | frequency_hz=300.0
- [2026-08-31 21:06:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181604.0678964 | source=vosk | rms=317 | updated_at=1788181604.0678964 | frequency_hz=388.0
- [2026-08-31 21:06:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181604.5592206 | source=vosk | rms=317 | updated_at=1788181604.0678964 | frequency_hz=388.0
- [2026-08-31 21:06:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181605.8088212 | source=vosk | rms=317 | updated_at=1788181604.0678964 | frequency_hz=388.0
- [2026-08-31 21:06:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181606.5610204 | source=vosk | rms=317 | updated_at=1788181604.0678964 | frequency_hz=388.0
- [2026-08-31 21:06:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181607.3283374 | source=vosk | rms=317 | updated_at=1788181604.0678964 | frequency_hz=388.0
- [2026-08-31 21:06:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181607.8090444 | source=vosk | rms=317 | updated_at=1788181604.0678964 | frequency_hz=388.0
- [2026-08-31 21:06:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181609.808397 | source=vosk | rms=122 | updated_at=1788181609.808397 | frequency_hz=388.0
- [2026-08-31 21:06:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181610.3100486 | source=vosk | rms=122 | updated_at=1788181609.808397 | frequency_hz=388.0
- [2026-08-31 21:06:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181612.316351 | source=vosk | rms=212 | updated_at=1788181612.316351 | frequency_hz=388.0
- [2026-08-31 21:06:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181613.0591938 | source=vosk | rms=166 | updated_at=1788181612.5667167 | frequency_hz=388.0
- [2026-08-31 21:06:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181613.8085997 | source=vosk | rms=166 | updated_at=1788181612.5667167 | frequency_hz=388.0
- [2026-08-31 21:06:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181614.559135 | source=vosk | rms=165 | updated_at=1788181614.061611 | frequency_hz=388.0
- [2026-08-31 21:06:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181614.809102 | source=vosk | rms=260 | updated_at=1788181614.809102 | frequency_hz=388.0
- [2026-08-31 21:06:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181615.5637043 | source=vosk | rms=260 | updated_at=1788181614.809102 | frequency_hz=388.0
- [2026-08-31 21:06:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181618.0585053 | source=vosk | rms=657 | updated_at=1788181618.0585053 | frequency_hz=388.0
- [2026-08-31 21:06:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181618.5594985 | source=vosk | rms=657 | updated_at=1788181618.0585053 | frequency_hz=388.0
- [2026-08-31 21:06:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181619.0589974 | source=vosk | rms=290 | updated_at=1788181619.0589974 | frequency_hz=388.0
- [2026-08-31 21:07:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181620.5593073 | source=vosk | rms=793 | updated_at=1788181620.0590162 | frequency_hz=388.0
- [2026-08-31 21:07:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181620.8088229 | source=vosk | rms=138 | updated_at=1788181620.8088229 | frequency_hz=388.0
- [2026-08-31 21:07:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181621.3088837 | source=vosk | rms=138 | updated_at=1788181620.8088229 | frequency_hz=388.0
- [2026-08-31 21:07:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181621.561191 | source=vosk | rms=411 | updated_at=1788181621.561191 | frequency_hz=388.0
- [2026-08-31 21:07:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181623.570259 | source=vosk | rms=166 | updated_at=1788181623.080898 | frequency_hz=388.0
- [2026-08-31 21:07:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181623.8248186 | source=vosk | rms=135 | updated_at=1788181623.8248186 | frequency_hz=388.0
- [2026-08-31 21:07:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181624.8293517 | source=vosk | rms=350 | updated_at=1788181624.3186467 | frequency_hz=388.0
- [2026-08-31 21:07:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181625.0701492 | source=vosk | rms=350 | updated_at=1788181624.3186467 | frequency_hz=388.0
- [2026-08-31 21:07:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181626.8282957 | source=vosk | rms=958 | updated_at=1788181626.3193252 | frequency_hz=388.0
- [2026-08-31 21:07:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181627.323289 | source=vosk | rms=131 | updated_at=1788181627.323289 | frequency_hz=388.0
- [2026-08-31 21:07:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181628.0964067 | source=vosk | rms=285 | updated_at=1788181627.588385 | frequency_hz=388.0
- [2026-08-31 21:07:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181629.5692008 | source=vosk | rms=180 | updated_at=1788181629.5692008 | frequency_hz=388.0
- [2026-08-31 21:07:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181631.3186345 | source=vosk | rms=155 | updated_at=1788181630.0688617 | frequency_hz=388.0
- [2026-08-31 21:07:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181631.609224 | source=vosk | rms=155 | updated_at=1788181630.0688617 | frequency_hz=388.0
- [2026-08-31 21:07:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181633.8193302 | source=vosk | rms=153 | updated_at=1788181633.3345063 | frequency_hz=388.0
- [2026-08-31 21:07:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181634.0693278 | source=vosk | rms=1042 | updated_at=1788181634.0693278 | frequency_hz=388.0
- [2026-08-31 21:07:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181635.1404696 | source=vosk | rms=642 | updated_at=1788181634.3252552 | frequency_hz=388.0
- [2026-08-31 21:07:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181635.389693 | source=vosk | rms=642 | updated_at=1788181634.3252552 | frequency_hz=388.0
- [2026-08-31 21:07:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181636.6428008 | source=vosk | rms=1206 | updated_at=1788181636.1400034 | frequency_hz=388.0
- [2026-08-31 21:07:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181636.8893757 | source=vosk | rms=900 | updated_at=1788181636.8893757 | frequency_hz=388.0
- [2026-08-31 21:07:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181637.641331 | source=vosk | rms=900 | updated_at=1788181636.8893757 | frequency_hz=388.0
- [2026-08-31 21:07:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181638.1413918 | source=vosk | rms=405 | updated_at=1788181638.1413918 | frequency_hz=388.0
- [2026-08-31 21:07:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181638.6387973 | source=vosk | rms=405 | updated_at=1788181638.1413918 | frequency_hz=388.0
- [2026-08-31 21:07:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181641.1415951 | source=vosk | rms=157 | updated_at=1788181641.1405942 | frequency_hz=108.0
- [2026-08-31 21:07:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181641.6525965 | source=vosk | rms=157 | updated_at=1788181641.1405942 | frequency_hz=108.0
- [2026-08-31 21:07:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181643.3897796 | source=vosk | rms=317 | updated_at=1788181643.3897796 | frequency_hz=148.0
- [2026-08-31 21:07:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181643.8891664 | source=vosk | rms=317 | updated_at=1788181643.3897796 | frequency_hz=148.0
- [2026-08-31 21:07:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181646.1389902 | source=vosk | rms=279 | updated_at=1788181646.1389902 | frequency_hz=148.0
- [2026-08-31 21:07:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181646.639832 | source=vosk | rms=279 | updated_at=1788181646.1389902 | frequency_hz=148.0
- [2026-08-31 21:07:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181653.4039395 | source=vosk | rms=279 | updated_at=1788181646.1389902 | frequency_hz=148.0
- [2026-08-31 21:07:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181653.8897038 | source=vosk | rms=279 | updated_at=1788181646.1389902 | frequency_hz=148.0
- [2026-08-31 21:07:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181660.8896525 | source=vosk | rms=377 | updated_at=1788181660.8896525 | frequency_hz=148.0
- [2026-08-31 21:07:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181661.655344 | source=vosk | rms=810 | updated_at=1788181661.151947 | frequency_hz=148.0
- [2026-08-31 21:07:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181666.8894444 | source=vosk | rms=810 | updated_at=1788181661.151947 | frequency_hz=148.0
- [2026-08-31 21:07:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181667.3893187 | source=vosk | rms=810 | updated_at=1788181661.151947 | frequency_hz=148.0
- [2026-08-31 21:07:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181667.6453419 | source=vosk | rms=199 | updated_at=1788181667.6453419 | frequency_hz=180.0
- [2026-08-31 21:07:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181668.1408887 | source=vosk | rms=199 | updated_at=1788181667.6453419 | frequency_hz=180.0
- [2026-08-31 21:07:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181670.3926864 | source=vosk | rms=707 | updated_at=1788181670.3926864 | frequency_hz=180.0
- [2026-08-31 21:07:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181671.1401565 | source=vosk | rms=1206 | updated_at=1788181670.6399949 | frequency_hz=180.0
- [2026-08-31 21:07:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181671.6520023 | source=vosk | rms=515 | updated_at=1788181671.6520023 | frequency_hz=180.0
- [2026-08-31 21:07:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181672.63932 | source=vosk | rms=333 | updated_at=1788181672.1839142 | frequency_hz=180.0
- [2026-08-31 21:07:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181673.89573 | source=vosk | rms=1201 | updated_at=1788181673.89573 | frequency_hz=180.0
- [2026-08-31 21:07:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181674.390104 | source=vosk | rms=1201 | updated_at=1788181673.89573 | frequency_hz=180.0
- [2026-08-31 21:07:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181675.6403253 | source=vosk | rms=584 | updated_at=1788181675.6403253 | frequency_hz=180.0
- [2026-08-31 21:07:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181678.140716 | source=vosk | rms=129 | updated_at=1788181677.640394 | frequency_hz=180.0
- [2026-08-31 21:07:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181678.3898826 | source=vosk | rms=189 | updated_at=1788181678.3898826 | frequency_hz=180.0
- [2026-08-31 21:08:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181681.6398199 | source=vosk | rms=748 | updated_at=1788181681.1405504 | frequency_hz=180.0
- [2026-08-31 21:08:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181681.8996222 | source=vosk | rms=428 | updated_at=1788181681.8996222 | frequency_hz=180.0
- [2026-08-31 21:08:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181685.1522298 | source=vosk | rms=227 | updated_at=1788181684.639832 | frequency_hz=180.0
- [2026-08-31 21:08:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181685.3997407 | source=vosk | rms=629 | updated_at=1788181685.3997407 | frequency_hz=180.0
- [2026-08-31 21:08:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181687.640328 | source=vosk | rms=769 | updated_at=1788181686.8899825 | frequency_hz=180.0
- [2026-08-31 21:08:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181687.8922381 | source=vosk | rms=769 | updated_at=1788181686.8899825 | frequency_hz=180.0
- [2026-08-31 21:08:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181688.806496 | source=vosk | rms=769 | updated_at=1788181686.8899825 | frequency_hz=180.0
- [2026-08-31 21:08:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181689.050174 | source=vosk | rms=769 | updated_at=1788181686.8899825 | frequency_hz=180.0
- [2026-08-31 21:08:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181690.0504065 | source=vosk | rms=415 | updated_at=1788181689.5504248 | frequency_hz=180.0
- [2026-08-31 21:08:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181690.2997422 | source=vosk | rms=415 | updated_at=1788181689.5504248 | frequency_hz=180.0
- [2026-08-31 21:08:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181692.0499673 | source=vosk | rms=1079 | updated_at=1788181691.5505266 | frequency_hz=220.6
- [2026-08-31 21:08:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181692.300195 | source=vosk | rms=283 | updated_at=1788181692.300195 | frequency_hz=220.6
- [2026-08-31 21:08:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181695.55026 | source=vosk | rms=1202 | updated_at=1788181694.8006332 | frequency_hz=220.6
- [2026-08-31 21:08:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181701.0528443 | source=vosk | rms=596 | updated_at=1788181701.0528443 | frequency_hz=220.6
- [2026-08-31 21:08:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181702.3081007 | source=vosk | rms=527 | updated_at=1788181701.8014758 | frequency_hz=220.6
- [2026-08-31 21:08:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181702.563222 | source=vosk | rms=527 | updated_at=1788181701.8014758 | frequency_hz=220.6
- [2026-08-31 21:08:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181703.062477 | source=vosk | rms=527 | updated_at=1788181701.8014758 | frequency_hz=220.6
- [2026-08-31 21:08:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181710.5538635 | source=vosk | rms=297 | updated_at=1788181710.5538635 | frequency_hz=200.0
- [2026-08-31 21:08:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181711.0536995 | source=vosk | rms=297 | updated_at=1788181710.5538635 | frequency_hz=200.0
- [2026-08-31 21:08:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181713.075251 | source=vosk | rms=1201 | updated_at=1788181713.075251 | frequency_hz=200.0
- [2026-08-31 21:08:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181713.8010297 | source=vosk | rms=341 | updated_at=1788181713.3075044 | frequency_hz=200.0
- [2026-08-31 21:08:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181714.3145022 | source=vosk | rms=1201 | updated_at=1788181714.3145022 | frequency_hz=200.0
- [2026-08-31 21:08:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181717.5511606 | source=vosk | rms=685 | updated_at=1788181717.050578 | frequency_hz=200.0
- [2026-08-31 21:08:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181718.0661101 | source=vosk | rms=685 | updated_at=1788181717.050578 | frequency_hz=200.0
- [2026-08-31 21:08:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181719.3012877 | source=vosk | rms=1205 | updated_at=1788181718.8009267 | frequency_hz=200.0
- [2026-08-31 21:08:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181719.55129 | source=vosk | rms=1205 | updated_at=1788181718.8009267 | frequency_hz=200.0
- [2026-08-31 21:08:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181726.3105013 | source=vosk | rms=364 | updated_at=1788181725.8056033 | frequency_hz=200.0
- [2026-08-31 21:08:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181736.550651 | source=vosk | rms=1030 | updated_at=1788181736.550651 | frequency_hz=200.0
- [2026-08-31 21:08:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181737.0521855 | source=vosk | rms=1030 | updated_at=1788181736.550651 | frequency_hz=200.0
- [2026-08-31 21:08:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181737.5512962 | source=vosk | rms=305 | updated_at=1788181737.5512962 | frequency_hz=160.1
- [2026-08-31 21:08:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181738.0670717 | source=vosk | rms=305 | updated_at=1788181737.5512962 | frequency_hz=160.1
- [2026-08-31 21:09:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181744.5658774 | source=vosk | rms=640 | updated_at=1788181744.5658774 | frequency_hz=252.0
- [2026-08-31 21:09:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181745.8007872 | source=vosk | rms=151 | updated_at=1788181745.0520208 | frequency_hz=214.2
- [2026-08-31 21:09:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181747.0508552 | source=vosk | rms=380 | updated_at=1788181747.0508552 | frequency_hz=214.2
- [2026-08-31 21:09:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181748.0695076 | source=vosk | rms=380 | updated_at=1788181747.0508552 | frequency_hz=214.2
- [2026-08-31 21:09:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181754.3012664 | source=vosk | rms=149 | updated_at=1788181754.3012664 | frequency_hz=214.2
- [2026-08-31 21:09:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181754.8020263 | source=vosk | rms=149 | updated_at=1788181754.3012664 | frequency_hz=214.2
- [2026-08-31 21:09:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181755.8019137 | source=vosk | rms=1203 | updated_at=1788181755.8019137 | frequency_hz=214.2
- [2026-08-31 21:09:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181757.5518773 | source=vosk | rms=1202 | updated_at=1788181757.0515034 | frequency_hz=214.2
- [2026-08-31 21:09:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181758.05199 | source=vosk | rms=1202 | updated_at=1788181757.0515034 | frequency_hz=214.2
- [2026-08-31 21:09:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181758.5514684 | source=vosk | rms=1202 | updated_at=1788181757.0515034 | frequency_hz=214.2
- [2026-08-31 21:09:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181759.051837 | source=vosk | rms=122 | updated_at=1788181759.051837 | frequency_hz=214.2
- [2026-08-31 21:09:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181760.054559 | source=vosk | rms=122 | updated_at=1788181759.051837 | frequency_hz=214.2
- [2026-08-31 21:09:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181760.3017616 | source=vosk | rms=263 | updated_at=1788181760.3017616 | frequency_hz=214.2
- [2026-08-31 21:09:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181761.8016493 | source=vosk | rms=301 | updated_at=1788181761.3014693 | frequency_hz=214.2
- [2026-08-31 21:09:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181762.5640402 | source=vosk | rms=204 | updated_at=1788181762.5640402 | frequency_hz=214.2
- [2026-08-31 21:09:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181764.5520604 | source=vosk | rms=268 | updated_at=1788181764.0559065 | frequency_hz=214.2
- [2026-08-31 21:09:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181764.801797 | source=vosk | rms=751 | updated_at=1788181764.801797 | frequency_hz=214.2
- [2026-08-31 21:09:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181766.0515866 | source=vosk | rms=247 | updated_at=1788181765.3017342 | frequency_hz=214.2
- [2026-08-31 21:09:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181767.8021364 | source=vosk | rms=247 | updated_at=1788181765.3017342 | frequency_hz=214.2
- [2026-08-31 21:09:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788181768.802864 | source=vosk | rms=207 | updated_at=1788181768.3014252 | frequency_hz=214.2
- [2026-08-31 21:09:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181772.0707686 | source=vosk | rms=929 | updated_at=1788181772.0707686 | frequency_hz=214.2
- [2026-08-31 21:09:32] operator / voice_transcript_partial / voice: back
  meta: kind=partial | timestamp=1788181772.578212 | source=vosk | rms=1201 | updated_at=1788181772.5685956 | frequency_hz=214.2
- [2026-08-31 21:09:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181772.805402 | source=vosk | rms=1201 | updated_at=1788181772.805402 | frequency_hz=214.2
- [2026-08-31 21:09:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181773.0517304 | source=vosk | rms=1200 | updated_at=1788181773.0517304 | frequency_hz=214.2
- [2026-08-31 21:09:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181773.3205621 | source=vosk | rms=1441 | updated_at=1788181773.3205621 | frequency_hz=214.2
- [2026-08-31 21:09:33] operator / voice_transcript_final / voice: back
  meta: kind=final | timestamp=1788181773.5028267 | source=final | rms=1441 | updated_at=1788181773.3205621 | frequency_hz=214.2
- [2026-08-31 21:09:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181773.5514696 | source=vosk | rms=1491 | updated_at=1788181773.5514696 | frequency_hz=214.2
- [2026-08-31 21:09:43] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1788181783.5490537 | source=final | rms=1202 | updated_at=1788181783.3019505 | frequency_hz=214.2
- [2026-08-31 21:09:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181783.5812361 | source=vosk | rms=1200 | updated_at=1788181783.5812361 | frequency_hz=214.2
- [2026-08-31 21:10:03] operator / voice_transcript_final / voice: ha
  meta: kind=final | timestamp=1788181803.5974555 | source=final | rms=1200 | updated_at=1788181794.5578504 | frequency_hz=214.2
- [2026-08-31 21:10:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181803.6529896 | source=vosk | rms=1200 | updated_at=1788181794.5578504 | frequency_hz=214.2
- [2026-08-31 21:10:24] operator / voice_transcript_final / voice: ha
  meta: kind=final | timestamp=1788181824.6890972 | source=final | rms=1200 | updated_at=1788181794.5578504 | frequency_hz=214.2
- [2026-08-31 21:10:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788181824.7541814 | source=vosk | rms=1200 | updated_at=1788181794.5578504 | frequency_hz=214.2

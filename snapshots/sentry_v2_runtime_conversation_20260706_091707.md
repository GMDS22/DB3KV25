# SMART SENTRY V5.0.0 Runtime Conversation Export

- Generated: 2026-07-06 09:17:07
- Entries: 200
- Roles: {'assistant': 5, 'system': 147, 'operator': 48}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 147, 'spoken_confirmation': 3, 'voice_transcript_partial': 34, 'voice_transcript_final': 11, 'voice_command': 3}
- Channels: {'text': 2, 'voice': 198}
- Latest operator request: earlier restart the smart sentry
- Latest assistant message: Running Smart Sentry now. Connecting the Smart Sentry boards first.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-07-06 09:13:56] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-07-06 09:13:56] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-07-06 09:13:58] system / voice_status / voice: listening
  meta: kind=status | timestamp=1783300438.731529 | source=vosk
- [2026-07-06 09:14:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300440.468628 | source=vosk | rms=285 | updated_at=1783300440.468628
- [2026-07-06 09:14:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300441.9684627 | source=vosk | rms=120 | updated_at=1783300441.2189338 | frequency_hz=296.0
- [2026-07-06 09:14:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300442.221948 | source=vosk | rms=120 | updated_at=1783300441.2189338 | frequency_hz=296.0
- [2026-07-06 09:14:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300444.4681475 | source=vosk | rms=141 | updated_at=1783300443.9700541 | frequency_hz=296.0
- [2026-07-06 09:14:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300444.9691615 | source=vosk | rms=141 | updated_at=1783300443.9700541 | frequency_hz=296.0
- [2026-07-06 09:14:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300445.4689465 | source=vosk | rms=141 | updated_at=1783300443.9700541 | frequency_hz=296.0
- [2026-07-06 09:14:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300446.7191055 | source=vosk | rms=141 | updated_at=1783300443.9700541 | frequency_hz=296.0
- [2026-07-06 09:14:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300447.2201262 | source=vosk | rms=141 | updated_at=1783300443.9700541 | frequency_hz=296.0
- [2026-07-06 09:14:36] assistant / spoken_confirmation / voice: Smart Sentry is ready.
  meta: interrupt=True | assistant_output=False | spoken=True
- [2026-07-06 09:14:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300450.4689975 | source=vosk | rms=141 | updated_at=1783300443.9700541 | frequency_hz=296.0
- [2026-07-06 09:14:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300450.9695072 | source=vosk | rms=141 | updated_at=1783300443.9700541 | frequency_hz=296.0
- [2026-07-06 09:14:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300451.7201385 | source=vosk | rms=266 | updated_at=1783300451.7201385 | frequency_hz=296.0
- [2026-07-06 09:14:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300452.2193165 | source=vosk | rms=266 | updated_at=1783300451.7201385 | frequency_hz=296.0
- [2026-07-06 09:14:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300455.1944468 | source=vosk | rms=1057 | updated_at=1783300455.1944468 | frequency_hz=296.0
- [2026-07-06 09:14:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300455.6892 | source=vosk | rms=1057 | updated_at=1783300455.1944468 | frequency_hz=296.0
- [2026-07-06 09:14:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300457.1891315 | source=vosk | rms=1057 | updated_at=1783300455.1944468 | frequency_hz=296.0
- [2026-07-06 09:14:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300457.6892228 | source=vosk | rms=1057 | updated_at=1783300455.1944468 | frequency_hz=296.0
- [2026-07-06 09:14:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300478.4493291 | source=vosk | rms=1057 | updated_at=1783300455.1944468 | frequency_hz=296.0
- [2026-07-06 09:14:39] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1783300479.2518237 | source=vosk | rms=486 | updated_at=1783300479.200104 | frequency_hz=296.0
- [2026-07-06 09:14:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300479.4503524 | source=vosk | rms=1200 | updated_at=1783300479.4503524 | frequency_hz=296.0
- [2026-07-06 09:14:39] operator / voice_transcript_partial / voice: smart century
  meta: kind=partial | timestamp=1783300479.5094929 | source=vosk | rms=1200 | updated_at=1783300479.4503524 | frequency_hz=296.0
- [2026-07-06 09:14:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300479.6999893 | source=vosk | rms=378 | updated_at=1783300479.6999893 | frequency_hz=296.0
- [2026-07-06 09:14:39] operator / voice_transcript_partial / voice: smart century as
  meta: kind=partial | timestamp=1783300479.950899 | source=vosk | rms=378 | updated_at=1783300479.6999893 | frequency_hz=296.0
- [2026-07-06 09:14:40] operator / voice_transcript_partial / voice: smart century is ready
  meta: kind=partial | timestamp=1783300480.0294073 | source=vosk | rms=378 | updated_at=1783300479.6999893 | frequency_hz=296.0
- [2026-07-06 09:14:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300480.4503102 | source=vosk | rms=265 | updated_at=1783300480.4503102 | frequency_hz=296.0
- [2026-07-06 09:14:40] operator / voice_transcript_partial / voice: smart century erratic
  meta: kind=partial | timestamp=1783300480.462329 | source=vosk | rms=265 | updated_at=1783300480.4503102 | frequency_hz=296.0
- [2026-07-06 09:14:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300480.7009661 | source=vosk | rms=330 | updated_at=1783300480.7009661 | frequency_hz=296.0
- [2026-07-06 09:14:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300480.9507768 | source=vosk | rms=278 | updated_at=1783300480.9507768 | frequency_hz=296.0
- [2026-07-06 09:14:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300481.1998487 | source=vosk | rms=1200 | updated_at=1783300481.1998487 | frequency_hz=296.0
- [2026-07-06 09:14:41] operator / voice_transcript_final / voice: smart sentry as erratic
  meta: kind=final | timestamp=1783300481.4980726 | source=final | rms=1200 | updated_at=1783300481.1998487 | frequency_hz=296.0
- [2026-07-06 09:14:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300481.6386888 | source=vosk | rms=1200 | updated_at=1783300481.1998487 | frequency_hz=296.0
- [2026-07-06 09:14:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300481.6386888 | source=vosk | rms=1200 | updated_at=1783300481.6386888 | frequency_hz=317.0
- [2026-07-06 09:14:44] operator / voice_transcript_partial / voice: read the
  meta: kind=partial | timestamp=1783300484.3578737 | source=vosk | rms=2886 | updated_at=1783300484.1992223 | frequency_hz=305.4
- [2026-07-06 09:14:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300484.449915 | source=vosk | rms=2532 | updated_at=1783300484.449915 | frequency_hz=305.4
- [2026-07-06 09:14:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300484.7017705 | source=vosk | rms=2510 | updated_at=1783300484.7017705 | frequency_hz=342.0
- [2026-07-06 09:14:44] operator / voice_transcript_partial / voice: read the smart
  meta: kind=partial | timestamp=1783300484.7351067 | source=vosk | rms=2510 | updated_at=1783300484.7017705 | frequency_hz=342.0
- [2026-07-06 09:14:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300484.9495595 | source=vosk | rms=1302 | updated_at=1783300484.9495595 | frequency_hz=269.9
- [2026-07-06 09:14:44] operator / voice_transcript_partial / voice: read the smart century
  meta: kind=partial | timestamp=1783300484.9776862 | source=vosk | rms=1302 | updated_at=1783300484.9495595 | frequency_hz=269.9
- [2026-07-06 09:14:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300485.1998932 | source=vosk | rms=1204 | updated_at=1783300485.1998932 | frequency_hz=288.8
- [2026-07-06 09:14:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300485.451112 | source=vosk | rms=290 | updated_at=1783300485.451112 | frequency_hz=225.5
- [2026-07-06 09:14:45] operator / voice_transcript_final / voice: restart the smart sentry
  meta: kind=final | timestamp=1783300485.7558725 | source=final | rms=290 | updated_at=1783300485.451112 | frequency_hz=225.5
- [2026-07-06 09:14:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300485.9910736 | source=vosk | rms=290 | updated_at=1783300485.451112 | frequency_hz=225.5
- [2026-07-06 09:14:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300485.9910736 | source=vosk | rms=274 | updated_at=1783300485.9910736 | frequency_hz=192.8
- [2026-07-06 09:14:50] operator / voice_transcript_partial / voice: do you
  meta: kind=partial | timestamp=1783300490.2728786 | source=vosk | rms=1200 | updated_at=1783300490.199613 | frequency_hz=166.3
- [2026-07-06 09:14:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300490.450239 | source=vosk | rms=1202 | updated_at=1783300490.450239 | frequency_hz=143.8
- [2026-07-06 09:14:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300490.7000642 | source=vosk | rms=1205 | updated_at=1783300490.7000642 | frequency_hz=193.6
- [2026-07-06 09:14:50] operator / voice_transcript_final / voice: julia
  meta: kind=final | timestamp=1783300490.9401722 | source=final | rms=1205 | updated_at=1783300490.7000642 | frequency_hz=193.6
- [2026-07-06 09:14:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300490.9785392 | source=vosk | rms=4609 | updated_at=1783300490.9785392 | frequency_hz=193.6
- [2026-07-06 09:14:51] operator / voice_transcript_partial / voice: right
  meta: kind=partial | timestamp=1783300491.5047326 | source=vosk | rms=2864 | updated_at=1783300491.4521117 | frequency_hz=193.6
- [2026-07-06 09:14:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300491.7002509 | source=vosk | rms=2508 | updated_at=1783300491.7002509 | frequency_hz=193.6
- [2026-07-06 09:14:51] operator / voice_transcript_partial / voice: read the
  meta: kind=partial | timestamp=1783300491.7248724 | source=vosk | rms=2508 | updated_at=1783300491.7002509 | frequency_hz=193.6
- [2026-07-06 09:14:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300491.9506016 | source=vosk | rms=1774 | updated_at=1783300491.9506016 | frequency_hz=193.6
- [2026-07-06 09:14:51] operator / voice_transcript_partial / voice: read the sports
  meta: kind=partial | timestamp=1783300491.9616015 | source=vosk | rms=1774 | updated_at=1783300491.9506016 | frequency_hz=193.6
- [2026-07-06 09:14:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300492.2001462 | source=vosk | rms=1200 | updated_at=1783300492.2001462 | frequency_hz=208.4
- [2026-07-06 09:14:52] operator / voice_transcript_partial / voice: read the smart century
  meta: kind=partial | timestamp=1783300492.2262988 | source=vosk | rms=1200 | updated_at=1783300492.2001462 | frequency_hz=208.4
- [2026-07-06 09:14:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300492.4511213 | source=vosk | rms=1200 | updated_at=1783300492.2001462 | frequency_hz=208.4
- [2026-07-06 09:14:52] operator / voice_transcript_partial / voice: read the smart said during
  meta: kind=partial | timestamp=1783300492.4792924 | source=vosk | rms=1200 | updated_at=1783300492.2001462 | frequency_hz=208.4
- [2026-07-06 09:14:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300492.7011309 | source=vosk | rms=1201 | updated_at=1783300492.7011309 | frequency_hz=192.9
- [2026-07-06 09:14:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300492.9524202 | source=vosk | rms=1204 | updated_at=1783300492.9524202 | frequency_hz=177.2
- [2026-07-06 09:14:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300493.450514 | source=vosk | rms=1204 | updated_at=1783300492.9524202 | frequency_hz=177.2
- [2026-07-06 09:14:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300496.2040195 | source=vosk | rms=983 | updated_at=1783300496.2040195 | frequency_hz=124.0
- [2026-07-06 09:14:56] operator / voice_transcript_final / voice: restart the smart sentry
  meta: kind=final | timestamp=1783300496.5568693 | source=final | rms=983 | updated_at=1783300496.2040195 | frequency_hz=124.0
- [2026-07-06 09:14:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300496.7970278 | source=vosk | rms=983 | updated_at=1783300496.2040195 | frequency_hz=124.0
- [2026-07-06 09:14:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300496.7970278 | source=vosk | rms=1201 | updated_at=1783300496.7970278 | frequency_hz=219.2
- [2026-07-06 09:14:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300498.7013392 | source=vosk | rms=1200 | updated_at=1783300497.7031002 | frequency_hz=186.7
- [2026-07-06 09:15:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300501.201175 | source=vosk | rms=1200 | updated_at=1783300501.201175 | frequency_hz=70.0
- [2026-07-06 09:15:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300502.4497066 | source=vosk | rms=1203 | updated_at=1783300501.9504712 | frequency_hz=84.0
- [2026-07-06 09:15:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300503.7003317 | source=vosk | rms=1203 | updated_at=1783300501.9504712 | frequency_hz=84.0
- [2026-07-06 09:15:04] operator / voice_transcript_partial / voice: earlier
  meta: kind=partial | timestamp=1783300504.9767983 | source=vosk | rms=4456 | updated_at=1783300504.9512198 | frequency_hz=324.0
- [2026-07-06 09:15:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300505.2013607 | source=vosk | rms=3144 | updated_at=1783300505.2013607 | frequency_hz=281.3
- [2026-07-06 09:15:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300505.4498553 | source=vosk | rms=3144 | updated_at=1783300505.2013607 | frequency_hz=281.3
- [2026-07-06 09:15:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300505.9501634 | source=vosk | rms=3144 | updated_at=1783300505.2013607 | frequency_hz=281.3
- [2026-07-06 09:15:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300508.8501017 | source=vosk | rms=4222 | updated_at=1783300508.8501017 | frequency_hz=281.3
- [2026-07-06 09:15:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300509.1011326 | source=vosk | rms=4222 | updated_at=1783300508.8501017 | frequency_hz=281.3
- [2026-07-06 09:15:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300509.6016064 | source=vosk | rms=4222 | updated_at=1783300508.8501017 | frequency_hz=281.3
- [2026-07-06 09:15:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300511.1040044 | source=vosk | rms=2090 | updated_at=1783300511.1040044 | frequency_hz=281.3
- [2026-07-06 09:15:11] operator / voice_transcript_partial / voice: earlier a
  meta: kind=partial | timestamp=1783300511.1215835 | source=vosk | rms=2090 | updated_at=1783300511.1040044 | frequency_hz=281.3
- [2026-07-06 09:15:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300511.3499966 | source=vosk | rms=3245 | updated_at=1783300511.3499966 | frequency_hz=281.3
- [2026-07-06 09:15:11] operator / voice_transcript_partial / voice: earlier it
  meta: kind=partial | timestamp=1783300511.3714042 | source=vosk | rms=3245 | updated_at=1783300511.3499966 | frequency_hz=281.3
- [2026-07-06 09:15:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300511.6005218 | source=vosk | rms=3245 | updated_at=1783300511.3499966 | frequency_hz=281.3
- [2026-07-06 09:15:11] operator / voice_transcript_partial / voice: earlier ill ill utah
  meta: kind=partial | timestamp=1783300511.635649 | source=vosk | rms=3245 | updated_at=1783300511.3499966 | frequency_hz=281.3
- [2026-07-06 09:15:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300511.8524601 | source=vosk | rms=3245 | updated_at=1783300511.3499966 | frequency_hz=281.3
- [2026-07-06 09:15:11] operator / voice_transcript_partial / voice: earlier a earlier
  meta: kind=partial | timestamp=1783300511.8713048 | source=vosk | rms=3245 | updated_at=1783300511.3499966 | frequency_hz=281.3
- [2026-07-06 09:15:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300512.3536892 | source=vosk | rms=3245 | updated_at=1783300511.3499966 | frequency_hz=281.3
- [2026-07-06 09:15:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300513.8504045 | source=vosk | rms=3245 | updated_at=1783300511.3499966 | frequency_hz=281.3
- [2026-07-06 09:15:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300514.1000319 | source=vosk | rms=3245 | updated_at=1783300511.3499966 | frequency_hz=281.3
- [2026-07-06 09:15:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300514.3516803 | source=vosk | rms=3245 | updated_at=1783300511.3499966 | frequency_hz=281.3
- [2026-07-06 09:15:14] operator / voice_transcript_final / voice: earlier a lawyer
  meta: kind=final | timestamp=1783300514.6399562 | source=final | rms=3245 | updated_at=1783300511.3499966 | frequency_hz=281.3
- [2026-07-06 09:15:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300514.8524768 | source=vosk | rms=3245 | updated_at=1783300511.3499966 | frequency_hz=281.3
- [2026-07-06 09:15:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300518.8507316 | source=vosk | rms=1203 | updated_at=1783300518.8507316 | frequency_hz=402.0
- [2026-07-06 09:15:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300520.3501563 | source=vosk | rms=1201 | updated_at=1783300519.8504658 | frequency_hz=296.9
- [2026-07-06 09:15:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300521.8506875 | source=vosk | rms=1201 | updated_at=1783300519.8504658 | frequency_hz=296.9
- [2026-07-06 09:15:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300524.6016977 | source=vosk | rms=1202 | updated_at=1783300523.8507905 | frequency_hz=296.9
- [2026-07-06 09:15:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300533.8502295 | source=vosk | rms=1202 | updated_at=1783300523.8507905 | frequency_hz=296.9
- [2026-07-06 09:15:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300536.2333653 | source=vosk | rms=1202 | updated_at=1783300534.1005585 | frequency_hz=296.9
- [2026-07-06 09:15:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300538.8647356 | source=vosk | rms=1202 | updated_at=1783300534.1005585 | frequency_hz=296.9
- [2026-07-06 09:15:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300540.6283202 | source=vosk | rms=1202 | updated_at=1783300534.1005585 | frequency_hz=296.9
- [2026-07-06 09:15:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300541.6263888 | source=vosk | rms=1202 | updated_at=1783300534.1005585 | frequency_hz=296.9
- [2026-07-06 09:15:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300542.1266582 | source=vosk | rms=1202 | updated_at=1783300534.1005585 | frequency_hz=296.9
- [2026-07-06 09:15:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300543.376713 | source=vosk | rms=593 | updated_at=1783300543.376713 | frequency_hz=356.0
- [2026-07-06 09:15:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300546.1249087 | source=vosk | rms=554 | updated_at=1783300545.1265323 | frequency_hz=149.5
- [2026-07-06 09:15:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300547.1252165 | source=vosk | rms=554 | updated_at=1783300545.1265323 | frequency_hz=149.5
- [2026-07-06 09:15:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300548.1247253 | source=vosk | rms=554 | updated_at=1783300545.1265323 | frequency_hz=149.5
- [2026-07-06 09:15:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300548.625142 | source=vosk | rms=616 | updated_at=1783300548.625142 | frequency_hz=388.0
- [2026-07-06 09:15:56] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1783300556.8997846 | source=vosk | rms=723 | updated_at=1783300556.8755696 | frequency_hz=388.0
- [2026-07-06 09:15:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300557.1314538 | source=vosk | rms=562 | updated_at=1783300557.1314538 | frequency_hz=388.0
- [2026-07-06 09:15:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300557.378028 | source=vosk | rms=546 | updated_at=1783300557.378028 | frequency_hz=388.0
- [2026-07-06 09:15:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300557.6253614 | source=vosk | rms=714 | updated_at=1783300557.6253614 | frequency_hz=388.0
- [2026-07-06 09:15:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300557.875454 | source=vosk | rms=714 | updated_at=1783300557.6253614 | frequency_hz=388.0
- [2026-07-06 09:15:58] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1783300558.1070347 | source=final | rms=714 | updated_at=1783300557.6253614 | frequency_hz=388.0
- [2026-07-06 09:15:58] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-07-06 09:15:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300558.1247697 | source=vosk | rms=714 | updated_at=1783300557.6253614 | frequency_hz=388.0
- [2026-07-06 09:15:58] assistant / spoken_confirmation / voice: I am listening. Ask your question.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-07-06 09:16:00] operator / voice_transcript_partial / voice: run
  meta: kind=partial | timestamp=1783300560.7119455 | source=vosk | rms=3057 | updated_at=1783300559.8754096 | frequency_hz=388.0
- [2026-07-06 09:16:00] system / voice_status / voice: processing
  meta: kind=status | timestamp=1783300560.7125568 | source=state | rms=3057 | updated_at=1783300559.8754096 | frequency_hz=388.0
- [2026-07-06 09:16:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300560.714421 | source=state | rms=3057 | updated_at=1783300559.8754096 | frequency_hz=388.0
- [2026-07-06 09:16:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300560.714421 | source=vosk | rms=2337 | updated_at=1783300560.714421 | frequency_hz=388.0
- [2026-07-06 09:16:00] operator / voice_transcript_partial / voice: run smart
  meta: kind=partial | timestamp=1783300560.7616284 | source=vosk | rms=1741 | updated_at=1783300560.7535937 | frequency_hz=388.0
- [2026-07-06 09:16:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300560.8945594 | source=vosk | rms=1201 | updated_at=1783300560.8945594 | frequency_hz=308.9
- [2026-07-06 09:16:00] operator / voice_transcript_partial / voice: run smart century
  meta: kind=partial | timestamp=1783300560.9101071 | source=vosk | rms=1201 | updated_at=1783300560.8945594 | frequency_hz=308.9
- [2026-07-06 09:16:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300561.1450872 | source=vosk | rms=780 | updated_at=1783300561.1450872 | frequency_hz=308.9
- [2026-07-06 09:16:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300562.0846245 | source=vosk | rms=780 | updated_at=1783300561.1450872 | frequency_hz=308.9
- [2026-07-06 09:16:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300562.335251 | source=vosk | rms=909 | updated_at=1783300562.335251 | frequency_hz=308.9
- [2026-07-06 09:16:02] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1783300562.3533156 | source=final | rms=909 | updated_at=1783300562.335251 | frequency_hz=308.9
- [2026-07-06 09:16:02] system / voice_status / voice: processing
  meta: kind=status | timestamp=1783300562.4013307 | source=state | rms=909 | updated_at=1783300562.335251 | frequency_hz=308.9
- [2026-07-06 09:16:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300562.4013307 | source=state | rms=909 | updated_at=1783300562.335251 | frequency_hz=308.9
- [2026-07-06 09:16:02] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-07-06 09:16:02] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-07-06 09:16:02] assistant / spoken_confirmation / voice: Running Smart Sentry now. Connecting the Smart Sentry boards first.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-07-06 09:16:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300563.6284566 | source=vosk | rms=857 | updated_at=1783300563.6284566 | frequency_hz=308.9
- [2026-07-06 09:16:06] operator / voice_transcript_partial / voice: running
  meta: kind=partial | timestamp=1783300566.6855667 | source=vosk | rms=954 | updated_at=1783300566.6765468 | frequency_hz=308.9
- [2026-07-06 09:16:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300566.9257417 | source=vosk | rms=761 | updated_at=1783300566.9252388 | frequency_hz=308.9
- [2026-07-06 09:16:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300567.1749265 | source=vosk | rms=627 | updated_at=1783300567.1749265 | frequency_hz=308.9
- [2026-07-06 09:16:07] operator / voice_transcript_partial / voice: running some i
  meta: kind=partial | timestamp=1783300567.213631 | source=vosk | rms=627 | updated_at=1783300567.1749265 | frequency_hz=308.9
- [2026-07-06 09:16:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300567.4256444 | source=vosk | rms=897 | updated_at=1783300567.4256444 | frequency_hz=308.9
- [2026-07-06 09:16:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300567.6835396 | source=vosk | rms=926 | updated_at=1783300567.6835396 | frequency_hz=308.9
- [2026-07-06 09:16:07] operator / voice_transcript_final / voice: running smile
  meta: kind=final | timestamp=1783300567.9285684 | source=final | rms=926 | updated_at=1783300567.6835396 | frequency_hz=308.9
- [2026-07-06 09:16:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300568.240297 | source=vosk | rms=926 | updated_at=1783300567.6835396 | frequency_hz=308.9
- [2026-07-06 09:16:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300568.240297 | source=vosk | rms=741 | updated_at=1783300568.240297 | frequency_hz=308.9
- [2026-07-06 09:16:08] operator / voice_transcript_partial / voice: connecting a
  meta: kind=partial | timestamp=1783300568.7406254 | source=vosk | rms=777 | updated_at=1783300568.6755726 | frequency_hz=308.9
- [2026-07-06 09:16:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300568.925326 | source=vosk | rms=541 | updated_at=1783300568.925326 | frequency_hz=308.9
- [2026-07-06 09:16:08] operator / voice_transcript_partial / voice: connecting a smartphone
  meta: kind=partial | timestamp=1783300568.9683747 | source=vosk | rms=541 | updated_at=1783300568.925326 | frequency_hz=308.9
- [2026-07-06 09:16:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300569.1756735 | source=vosk | rms=541 | updated_at=1783300568.925326 | frequency_hz=308.9
- [2026-07-06 09:16:09] operator / voice_transcript_partial / voice: connecting a smart such
  meta: kind=partial | timestamp=1783300569.2183137 | source=vosk | rms=541 | updated_at=1783300568.925326 | frequency_hz=308.9
- [2026-07-06 09:16:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300569.4330916 | source=vosk | rms=538 | updated_at=1783300569.4330916 | frequency_hz=308.9
- [2026-07-06 09:16:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300569.6756046 | source=vosk | rms=538 | updated_at=1783300569.4330916 | frequency_hz=308.9
- [2026-07-06 09:16:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300570.1755238 | source=vosk | rms=538 | updated_at=1783300569.4330916 | frequency_hz=308.9
- [2026-07-06 09:16:11] operator / voice_transcript_final / voice: connecting a smart such
  meta: kind=final | timestamp=1783300571.2106907 | source=final | rms=538 | updated_at=1783300569.4330916 | frequency_hz=308.9
- [2026-07-06 09:16:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300571.674846 | source=vosk | rms=538 | updated_at=1783300569.4330916 | frequency_hz=308.9
- [2026-07-06 09:16:11] operator / voice_transcript_partial / voice: connecting a smart such as far as
  meta: kind=partial | timestamp=1783300571.7164805 | source=vosk | rms=538 | updated_at=1783300569.4330916 | frequency_hz=308.9
- [2026-07-06 09:16:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300571.9251785 | source=vosk | rms=538 | updated_at=1783300569.4330916 | frequency_hz=308.9
- [2026-07-06 09:16:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300572.4257684 | source=vosk | rms=538 | updated_at=1783300569.4330916 | frequency_hz=308.9
- [2026-07-06 09:16:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300572.92492 | source=vosk | rms=538 | updated_at=1783300569.4330916 | frequency_hz=308.9
- [2026-07-06 09:16:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300573.1764517 | source=vosk | rms=538 | updated_at=1783300569.4330916 | frequency_hz=308.9
- [2026-07-06 09:16:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300573.6753979 | source=vosk | rms=538 | updated_at=1783300569.4330916 | frequency_hz=308.9
- [2026-07-06 09:16:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300573.9252849 | source=vosk | rms=538 | updated_at=1783300569.4330916 | frequency_hz=308.9
- [2026-07-06 09:16:14] operator / voice_transcript_final / voice: connecting a smart such far as
  meta: kind=final | timestamp=1783300574.2348034 | source=final | rms=538 | updated_at=1783300569.4330916 | frequency_hz=308.9
- [2026-07-06 09:16:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300574.3442438 | source=vosk | rms=538 | updated_at=1783300569.4330916 | frequency_hz=308.9
- [2026-07-06 09:16:28] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1783300588.3800716 | source=vosk | rms=1202 | updated_at=1783300588.3560169 | frequency_hz=187.2
- [2026-07-06 09:16:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300588.824667 | source=vosk | rms=1102 | updated_at=1783300588.824667 | frequency_hz=187.2
- [2026-07-06 09:16:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300588.956314 | source=vosk | rms=14009 | updated_at=1783300588.956314 | frequency_hz=187.2
- [2026-07-06 09:16:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300589.6466591 | source=vosk | rms=14265 | updated_at=1783300589.6466591 | frequency_hz=187.2
- [2026-07-06 09:16:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300589.8960757 | source=vosk | rms=7467 | updated_at=1783300589.8960757 | frequency_hz=187.2
- [2026-07-06 09:16:29] operator / voice_transcript_partial / voice: alien we
  meta: kind=partial | timestamp=1783300589.9247713 | source=vosk | rms=7467 | updated_at=1783300589.8960757 | frequency_hz=187.2
- [2026-07-06 09:16:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300590.1459491 | source=vosk | rms=12481 | updated_at=1783300590.1459491 | frequency_hz=187.2
- [2026-07-06 09:16:30] operator / voice_transcript_partial / voice: alien restart
  meta: kind=partial | timestamp=1783300590.1670656 | source=vosk | rms=12481 | updated_at=1783300590.1459491 | frequency_hz=187.2
- [2026-07-06 09:16:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300590.3961756 | source=vosk | rms=5168 | updated_at=1783300590.394828 | frequency_hz=200.1
- [2026-07-06 09:16:30] operator / voice_transcript_partial / voice: alien restart simply
  meta: kind=partial | timestamp=1783300590.4316876 | source=vosk | rms=5168 | updated_at=1783300590.394828 | frequency_hz=200.1
- [2026-07-06 09:16:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300590.6459897 | source=vosk | rms=1542 | updated_at=1783300590.6459897 | frequency_hz=187.5
- [2026-07-06 09:16:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300590.8951418 | source=vosk | rms=1200 | updated_at=1783300590.8951418 | frequency_hz=187.5
- [2026-07-06 09:16:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300591.1454837 | source=vosk | rms=1244 | updated_at=1783300591.1454837 | frequency_hz=193.3
- [2026-07-06 09:16:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300591.4054494 | source=vosk | rms=1201 | updated_at=1783300591.4054494 | frequency_hz=244.6
- [2026-07-06 09:16:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300591.8340595 | source=state | rms=1201 | updated_at=1783300591.4054494 | frequency_hz=244.6
- [2026-07-06 09:16:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300591.8340595 | source=vosk | rms=3785 | updated_at=1783300591.8340595 | frequency_hz=244.6
- [2026-07-06 09:16:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300594.666505 | source=vosk | rms=1200 | updated_at=1783300593.916729 | frequency_hz=229.6
- [2026-07-06 09:16:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300595.1654353 | source=vosk | rms=1200 | updated_at=1783300593.916729 | frequency_hz=229.6
- [2026-07-06 09:16:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300596.4159126 | source=vosk | rms=963 | updated_at=1783300595.915475 | frequency_hz=96.0
- [2026-07-06 09:16:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300597.6657076 | source=vosk | rms=963 | updated_at=1783300597.6657076 | frequency_hz=96.0
- [2026-07-06 09:16:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300598.6660652 | source=vosk | rms=952 | updated_at=1783300598.1827104 | frequency_hz=96.0
- [2026-07-06 09:16:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300601.7096188 | source=vosk | rms=952 | updated_at=1783300598.1827104 | frequency_hz=96.0
- [2026-07-06 09:16:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300604.222675 | source=vosk | rms=952 | updated_at=1783300598.1827104 | frequency_hz=96.0
- [2026-07-06 09:16:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300604.4655333 | source=vosk | rms=2363 | updated_at=1783300604.4655333 | frequency_hz=96.0
- [2026-07-06 09:16:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300606.7753062 | source=vosk | rms=7742 | updated_at=1783300606.325956 | frequency_hz=96.0
- [2026-07-06 09:16:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300606.7753062 | source=vosk | rms=6056 | updated_at=1783300606.7753062 | frequency_hz=96.0
- [2026-07-06 09:16:47] operator / voice_transcript_final / voice: earlier restart the smart sentry
  meta: kind=final | timestamp=1783300607.9530478 | source=final | rms=3776 | updated_at=1783300607.6263096 | frequency_hz=215.0
- [2026-07-06 09:16:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300608.0999951 | source=vosk | rms=3776 | updated_at=1783300607.6263096 | frequency_hz=215.0
- [2026-07-06 09:16:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300608.0999951 | source=vosk | rms=3776 | updated_at=1783300607.6263096 | frequency_hz=215.0
- [2026-07-06 09:16:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300609.127203 | source=vosk | rms=3776 | updated_at=1783300607.6263096 | frequency_hz=215.0
- [2026-07-06 09:16:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300613.1800876 | source=vosk | rms=2701 | updated_at=1783300613.1800876 | frequency_hz=215.0
- [2026-07-06 09:16:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300613.696796 | source=vosk | rms=2701 | updated_at=1783300613.1800876 | frequency_hz=215.0
- [2026-07-06 09:16:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300613.9252055 | source=vosk | rms=2701 | updated_at=1783300613.1800876 | frequency_hz=215.0
- [2026-07-06 09:16:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300614.9258702 | source=vosk | rms=5269 | updated_at=1783300614.425762 | frequency_hz=215.0
- [2026-07-06 09:17:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300624.6666121 | source=vosk | rms=5269 | updated_at=1783300614.425762 | frequency_hz=215.0
- [2026-07-06 09:17:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300625.166107 | source=vosk | rms=5269 | updated_at=1783300614.425762 | frequency_hz=215.0
- [2026-07-06 09:17:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783300625.419442 | source=vosk | rms=5269 | updated_at=1783300614.425762 | frequency_hz=215.0
- [2026-07-06 09:17:05] operator / voice_transcript_partial / voice: but
  meta: kind=partial | timestamp=1783300625.485636 | source=vosk | rms=5269 | updated_at=1783300614.425762 | frequency_hz=215.0
- [2026-07-06 09:17:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783300625.9156656 | source=vosk | rms=5269 | updated_at=1783300614.425762 | frequency_hz=215.0

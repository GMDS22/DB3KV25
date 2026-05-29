# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-06 23:25:47
- Entries: 1151
- Roles: {'assistant': 21, 'system': 1, 'operator': 1129}
- Event types: {'assistant_prompt': 2, 'assistant_analysis': 1, 'voice_status': 1, 'spoken_confirmation': 16, 'voice_transcript_partial': 952, 'voice_transcript_final': 160, 'voice_command': 17, 'spoken_reply': 2}
- Channels: {'text': 3, 'voice': 1148}
- Latest operator request: slew order
- Latest assistant message: I heard the request, but only the registered operator can change Smart Sentry settings.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-06 22:57:58] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-06 22:57:58] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-06 22:58:00] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778079480.893543 | source=vosk
- [2026-05-06 22:58:35] assistant / spoken_confirmation / voice: The smart Sentry is now online. Say the command.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 22:58:39] operator / voice_transcript_partial / voice: what's the smart sentry is no
  meta: kind=partial | timestamp=1778079519.5647576 | source=vosk | frequency_hz=302.5 | rms=303 | updated_at=1778079517.691811
- [2026-05-06 22:58:39] operator / voice_transcript_partial / voice: what's the smart sentry is no on
  meta: kind=partial | timestamp=1778079519.8134563 | source=vosk | frequency_hz=302.5 | rms=303 | updated_at=1778079517.691811
- [2026-05-06 22:58:40] operator / voice_transcript_partial / voice: what's the smart sentry is no on lion
  meta: kind=partial | timestamp=1778079520.0649374 | source=vosk | frequency_hz=352.0 | rms=296 | updated_at=1778079520.0559156
- [2026-05-06 22:58:40] operator / voice_transcript_partial / voice: what's the smart sentry is no on lion say the
  meta: kind=partial | timestamp=1778079520.8135862 | source=vosk | frequency_hz=352.0 | rms=296 | updated_at=1778079520.0559156
- [2026-05-06 22:58:41] operator / voice_transcript_partial / voice: what's the smart sentry is no on lion say the command
  meta: kind=partial | timestamp=1778079521.3170831 | source=vosk | frequency_hz=347.8 | rms=319 | updated_at=1778079521.30553
- [2026-05-06 22:58:42] operator / voice_transcript_partial / voice: video
  meta: kind=partial | timestamp=1778079522.8327777 | source=vosk | frequency_hz=347.8 | rms=319 | updated_at=1778079521.30553
- [2026-05-06 22:58:43] operator / voice_transcript_partial / voice: video loop
  meta: kind=partial | timestamp=1778079523.575603 | source=vosk | frequency_hz=252.0 | rms=884 | updated_at=1778079523.5675883
- [2026-05-06 22:58:44] operator / voice_transcript_final / voice: video loop
  meta: kind=final | timestamp=1778079524.1772392 | source=final | frequency_hz=294.0 | rms=320 | updated_at=1778079524.066993
- [2026-05-06 22:58:45] operator / voice_transcript_partial / voice: run the smart
  meta: kind=partial | timestamp=1778079525.823241 | source=vosk | frequency_hz=348.1 | rms=433 | updated_at=1778079525.0671952
- [2026-05-06 22:58:46] operator / voice_transcript_partial / voice: run the smart sentry
  meta: kind=partial | timestamp=1778079526.0757716 | source=vosk | frequency_hz=348.1 | rms=433 | updated_at=1778079525.0671952
- [2026-05-06 22:58:47] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1778079527.3285146 | source=final | frequency_hz=329.8 | rms=308 | updated_at=1778079527.0673823
- [2026-05-06 22:58:47] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-05-06 22:58:47] assistant / spoken_confirmation / voice: Connecting Smart Sentry boards now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 22:58:59] operator / voice_transcript_partial / voice: off
  meta: kind=partial | timestamp=1778079539.9836822 | source=vosk | frequency_hz=258.6 | rms=1200 | updated_at=1778079539.7238777
- [2026-05-06 22:59:00] operator / voice_transcript_partial / voice: off gesture
  meta: kind=partial | timestamp=1778079540.2312531 | source=vosk | frequency_hz=258.6 | rms=1200 | updated_at=1778079539.7238777
- [2026-05-06 22:59:00] operator / voice_transcript_partial / voice: off
  meta: kind=partial | timestamp=1778079540.4861898 | source=vosk | frequency_hz=258.6 | rms=1200 | updated_at=1778079539.7238777
- [2026-05-06 22:59:00] operator / voice_transcript_partial / voice: off on keyboard
  meta: kind=partial | timestamp=1778079540.733778 | source=vosk | frequency_hz=258.6 | rms=1200 | updated_at=1778079539.7238777
- [2026-05-06 22:59:00] operator / voice_transcript_partial / voice: off on give another
  meta: kind=partial | timestamp=1778079540.9806454 | source=vosk | frequency_hz=258.6 | rms=1200 | updated_at=1778079539.7238777
- [2026-05-06 22:59:01] operator / voice_transcript_partial / voice: off on give another command
  meta: kind=partial | timestamp=1778079541.2588167 | source=vosk | frequency_hz=258.6 | rms=1200 | updated_at=1778079539.7238777
- [2026-05-06 22:59:01] operator / voice_transcript_partial / voice: off on give another command window shortcuts
  meta: kind=partial | timestamp=1778079541.979843 | source=vosk | frequency_hz=258.6 | rms=1200 | updated_at=1778079539.7238777
- [2026-05-06 22:59:02] operator / voice_transcript_final / voice: off on give another command window
  meta: kind=final | timestamp=1778079542.9470093 | source=final | frequency_hz=258.6 | rms=1200 | updated_at=1778079539.7238777
- [2026-05-06 22:59:04] operator / voice_transcript_partial / voice: changes
  meta: kind=partial | timestamp=1778079544.7365532 | source=vosk | frequency_hz=258.6 | rms=1200 | updated_at=1778079539.7238777
- [2026-05-06 22:59:04] operator / voice_transcript_partial / voice: change your voice
  meta: kind=partial | timestamp=1778079544.9852538 | source=vosk | frequency_hz=258.6 | rms=1200 | updated_at=1778079539.7238777
- [2026-05-06 22:59:05] operator / voice_transcript_partial / voice: change your voice buzzer
  meta: kind=partial | timestamp=1778079545.480526 | source=vosk | frequency_hz=258.6 | rms=1200 | updated_at=1778079539.7238777
- [2026-05-06 22:59:05] operator / voice_transcript_partial / voice: change your voice enabled
  meta: kind=partial | timestamp=1778079545.733936 | source=vosk | frequency_hz=258.6 | rms=1200 | updated_at=1778079539.7238777
- [2026-05-06 22:59:05] operator / voice_transcript_partial / voice: change your voice theme to
  meta: kind=partial | timestamp=1778079545.9890478 | source=vosk | frequency_hz=258.6 | rms=1200 | updated_at=1778079539.7238777
- [2026-05-06 22:59:06] operator / voice_transcript_partial / voice: change your voice theme to of
  meta: kind=partial | timestamp=1778079546.2299848 | source=vosk | frequency_hz=258.6 | rms=1200 | updated_at=1778079539.7238777
- [2026-05-06 22:59:06] operator / voice_transcript_partial / voice: change your voice theme to of hey leon
  meta: kind=partial | timestamp=1778079546.4925997 | source=vosk | frequency_hz=258.6 | rms=1200 | updated_at=1778079539.7238777
- [2026-05-06 22:59:06] operator / voice_transcript_partial / voice: change your voice theme to of hey leon enable
  meta: kind=partial | timestamp=1778079546.7315676 | source=vosk | frequency_hz=258.6 | rms=1200 | updated_at=1778079539.7238777
- [2026-05-06 22:59:06] operator / voice_transcript_partial / voice: change your voice theme to of hey leon
  meta: kind=partial | timestamp=1778079546.9903948 | source=vosk | frequency_hz=258.6 | rms=1200 | updated_at=1778079539.7238777
- [2026-05-06 22:59:07] operator / voice_transcript_partial / voice: change your voice theme to of hey leon engaging scope
  meta: kind=partial | timestamp=1778079547.2336066 | source=vosk | frequency_hz=258.6 | rms=1200 | updated_at=1778079539.7238777
- [2026-05-06 22:59:08] operator / voice_transcript_final / voice: change theme
  meta: kind=final | timestamp=1778079548.0814915 | source=final | frequency_hz=258.6 | rms=1200 | updated_at=1778079539.7238777
- [2026-05-06 22:59:08] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1778079548.7298915 | source=vosk | frequency_hz=258.6 | rms=1200 | updated_at=1778079539.7238777
- [2026-05-06 22:59:10] operator / voice_transcript_final / voice: voice
  meta: kind=final | timestamp=1778079550.2534688 | source=final | frequency_hz=258.6 | rms=1200 | updated_at=1778079539.7238777
- [2026-05-06 22:59:22] operator / voice_transcript_partial / voice: leon
  meta: kind=partial | timestamp=1778079562.4139757 | source=vosk | frequency_hz=344.7 | rms=320 | updated_at=1778079560.6592681
- [2026-05-06 22:59:22] operator / voice_transcript_partial / voice: leon increase
  meta: kind=partial | timestamp=1778079562.6644313 | source=vosk | frequency_hz=344.7 | rms=320 | updated_at=1778079560.6592681
- [2026-05-06 22:59:22] operator / voice_transcript_partial / voice: leon resume
  meta: kind=partial | timestamp=1778079562.9161487 | source=vosk | frequency_hz=344.7 | rms=320 | updated_at=1778079560.6592681
- [2026-05-06 22:59:23] operator / voice_transcript_partial / voice: leon is visual overlay
  meta: kind=partial | timestamp=1778079563.1671755 | source=vosk | frequency_hz=344.7 | rms=320 | updated_at=1778079560.6592681
- [2026-05-06 22:59:23] operator / voice_transcript_partial / voice: leon is visual greeting
  meta: kind=partial | timestamp=1778079563.422272 | source=vosk | frequency_hz=344.7 | rms=320 | updated_at=1778079560.6592681
- [2026-05-06 22:59:30] operator / voice_transcript_partial / voice: change your voice
  meta: kind=partial | timestamp=1778079570.9206164 | source=vosk | frequency_hz=350.1 | rms=307 | updated_at=1778079569.9086046
- [2026-05-06 22:59:32] operator / voice_transcript_final / voice: change your voice
  meta: kind=final | timestamp=1778079572.2763572 | source=final | frequency_hz=309.6 | rms=303 | updated_at=1778079571.661771
- [2026-05-06 22:59:32] operator / voice_command / voice: change your voice
  meta: normalized=True
- [2026-05-06 22:59:32] assistant / spoken_confirmation / voice: Absolutely. Tell me a voice style like British male or British female.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 22:59:40] operator / voice_transcript_partial / voice: give
  meta: kind=partial | timestamp=1778079580.1657586 | source=vosk | frequency_hz=396.0 | rms=340 | updated_at=1778079575.9096482
- [2026-05-06 22:59:40] operator / voice_transcript_partial / voice: give mute
  meta: kind=partial | timestamp=1778079580.4244833 | source=vosk | frequency_hz=396.0 | rms=340 | updated_at=1778079575.9096482
- [2026-05-06 22:59:40] operator / voice_transcript_partial / voice: give media loop
  meta: kind=partial | timestamp=1778079580.7087374 | source=vosk | frequency_hz=396.0 | rms=340 | updated_at=1778079575.9096482
- [2026-05-06 22:59:40] operator / voice_transcript_partial / voice: give media loop disabled
  meta: kind=partial | timestamp=1778079580.9562697 | source=vosk | frequency_hz=396.0 | rms=340 | updated_at=1778079575.9096482
- [2026-05-06 22:59:41] operator / voice_transcript_partial / voice: give mute slew order
  meta: kind=partial | timestamp=1778079581.4619024 | source=vosk | frequency_hz=384.8 | rms=303 | updated_at=1778079581.4498885
- [2026-05-06 22:59:42] operator / voice_transcript_final / voice: give me a slew
  meta: kind=final | timestamp=1778079582.7099562 | source=final | frequency_hz=384.8 | rms=303 | updated_at=1778079581.4498885
- [2026-05-06 22:59:44] operator / voice_transcript_partial / voice: guard
  meta: kind=partial | timestamp=1778079584.0390303 | source=vosk | frequency_hz=384.8 | rms=303 | updated_at=1778079581.4498885
- [2026-05-06 22:59:44] operator / voice_transcript_partial / voice: detection
  meta: kind=partial | timestamp=1778079584.2890708 | source=vosk | frequency_hz=384.8 | rms=303 | updated_at=1778079581.4498885
- [2026-05-06 22:59:44] operator / voice_transcript_partial / voice: detection alien
  meta: kind=partial | timestamp=1778079584.7860265 | source=vosk | frequency_hz=384.8 | rms=303 | updated_at=1778079581.4498885
- [2026-05-06 22:59:45] operator / voice_transcript_partial / voice: detection leon is
  meta: kind=partial | timestamp=1778079585.1388118 | source=vosk | frequency_hz=384.8 | rms=303 | updated_at=1778079581.4498885
- [2026-05-06 22:59:45] operator / voice_transcript_partial / voice: detection on
  meta: kind=partial | timestamp=1778079585.2908113 | source=vosk | frequency_hz=384.8 | rms=303 | updated_at=1778079581.4498885
- [2026-05-06 22:59:45] operator / voice_transcript_partial / voice: detection leon is runtime
  meta: kind=partial | timestamp=1778079585.5523424 | source=vosk | frequency_hz=384.8 | rms=303 | updated_at=1778079581.4498885
- [2026-05-06 22:59:46] operator / voice_transcript_final / voice: detection on
  meta: kind=final | timestamp=1778079586.242315 | source=final | frequency_hz=384.8 | rms=303 | updated_at=1778079581.4498885
- [2026-05-06 22:59:47] operator / voice_transcript_partial / voice: a lion
  meta: kind=partial | timestamp=1778079587.5360847 | source=vosk | frequency_hz=384.8 | rms=303 | updated_at=1778079581.4498885
- [2026-05-06 22:59:47] operator / voice_transcript_partial / voice: anomaly
  meta: kind=partial | timestamp=1778079587.810581 | source=vosk | frequency_hz=384.8 | rms=303 | updated_at=1778079581.4498885
- [2026-05-06 22:59:48] operator / voice_transcript_partial / voice: anomaly trigger
  meta: kind=partial | timestamp=1778079588.28773 | source=vosk | frequency_hz=384.8 | rms=303 | updated_at=1778079581.4498885
- [2026-05-06 22:59:48] operator / voice_transcript_final / voice: anomaly
  meta: kind=final | timestamp=1778079588.866085 | source=final | frequency_hz=384.8 | rms=303 | updated_at=1778079581.4498885
- [2026-05-06 22:59:49] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778079589.7847483 | source=vosk | frequency_hz=384.8 | rms=303 | updated_at=1778079581.4498885
- [2026-05-06 22:59:50] operator / voice_transcript_partial / voice: current status
  meta: kind=partial | timestamp=1778079590.077173 | source=vosk | frequency_hz=384.8 | rms=303 | updated_at=1778079581.4498885
- [2026-05-06 22:59:50] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778079590.2876487 | source=vosk | frequency_hz=384.8 | rms=303 | updated_at=1778079581.4498885
- [2026-05-06 22:59:50] operator / voice_transcript_partial / voice: current face hello
  meta: kind=partial | timestamp=1778079590.5383148 | source=vosk | frequency_hz=384.8 | rms=303 | updated_at=1778079581.4498885
- [2026-05-06 22:59:50] operator / voice_transcript_partial / voice: current face hello manual
  meta: kind=partial | timestamp=1778079590.7915723 | source=vosk | frequency_hz=384.8 | rms=303 | updated_at=1778079581.4498885
- [2026-05-06 22:59:51] operator / voice_transcript_partial / voice: current face hello manual human voice
  meta: kind=partial | timestamp=1778079591.301362 | source=vosk | frequency_hz=384.8 | rms=303 | updated_at=1778079581.4498885
- [2026-05-06 22:59:51] operator / voice_transcript_partial / voice: current face hello manual movement on the
  meta: kind=partial | timestamp=1778079591.5462816 | source=vosk | frequency_hz=384.8 | rms=303 | updated_at=1778079581.4498885
- [2026-05-06 22:59:52] operator / voice_transcript_partial / voice: current face hello manual movement on the leon
  meta: kind=partial | timestamp=1778079592.0364583 | source=vosk | frequency_hz=384.8 | rms=303 | updated_at=1778079581.4498885
- [2026-05-06 23:00:07] operator / voice_transcript_partial / voice: can you
  meta: kind=partial | timestamp=1778079607.8646233 | source=vosk | frequency_hz=408.0 | rms=312 | updated_at=1778079606.8562272
- [2026-05-06 23:00:08] operator / voice_transcript_partial / voice: can you greeting
  meta: kind=partial | timestamp=1778079608.3733711 | source=vosk | frequency_hz=408.0 | rms=312 | updated_at=1778079606.8562272
- [2026-05-06 23:00:08] operator / voice_transcript_partial / voice: can you increase
  meta: kind=partial | timestamp=1778079608.6108613 | source=vosk | frequency_hz=408.0 | rms=312 | updated_at=1778079606.8562272
- [2026-05-06 23:00:08] operator / voice_transcript_partial / voice: can you increase the automatic
  meta: kind=partial | timestamp=1778079608.8651829 | source=vosk | frequency_hz=408.0 | rms=312 | updated_at=1778079606.8562272
- [2026-05-06 23:00:09] operator / voice_transcript_partial / voice: can you increase the auto trigger
  meta: kind=partial | timestamp=1778079609.296939 | source=vosk | frequency_hz=408.0 | rms=312 | updated_at=1778079606.8562272
- [2026-05-06 23:00:09] operator / voice_transcript_partial / voice: can you increase the auto tracking
  meta: kind=partial | timestamp=1778079609.3607562 | source=vosk | frequency_hz=408.0 | rms=312 | updated_at=1778079606.8562272
- [2026-05-06 23:00:09] operator / voice_transcript_partial / voice: can you increase the auto tracking speed
  meta: kind=partial | timestamp=1778079609.8602796 | source=vosk | frequency_hz=408.0 | rms=312 | updated_at=1778079606.8562272
- [2026-05-06 23:00:10] operator / voice_transcript_final / voice: can you increase the autotracking speed
  meta: kind=final | timestamp=1778079610.4739516 | source=final | frequency_hz=408.0 | rms=312 | updated_at=1778079606.8562272
- [2026-05-06 23:00:10] operator / voice_command / voice: can you increase the autotracking speed
  meta: normalized=True
- [2026-05-06 23:00:11] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 23:00:17] operator / voice_transcript_partial / voice: operator change smart
  meta: kind=partial | timestamp=1778079617.6132143 | source=vosk | frequency_hz=334.4 | rms=319 | updated_at=1778079613.157252
- [2026-05-06 23:00:17] operator / voice_transcript_partial / voice: operator change smart sentry
  meta: kind=partial | timestamp=1778079617.862079 | source=vosk | frequency_hz=334.4 | rms=319 | updated_at=1778079613.157252
- [2026-05-06 23:00:18] operator / voice_transcript_final / voice: turn operator change smart sentry
  meta: kind=final | timestamp=1778079618.979648 | source=final | frequency_hz=376.1 | rms=318 | updated_at=1778079618.8558764
- [2026-05-06 23:00:19] operator / voice_command / voice: turn operator change smart sentry
  meta: normalized=True
- [2026-05-06 23:00:19] assistant / spoken_confirmation / voice: I can keep going with voice change. Tell me a voice family like Russian or Indian, ask what are the options, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 23:00:28] operator / voice_transcript_partial / voice: spare light russian dmitry
  meta: kind=partial | timestamp=1778079628.0101588 | source=vosk | frequency_hz=357.5 | rms=307 | updated_at=1778079622.10891
- [2026-05-06 23:00:28] operator / voice_transcript_partial / voice: spare light russian
  meta: kind=partial | timestamp=1778079628.5014012 | source=vosk | frequency_hz=357.5 | rms=307 | updated_at=1778079622.10891
- [2026-05-06 23:00:29] operator / voice_transcript_partial / voice: spare light russian ask what are the
  meta: kind=partial | timestamp=1778079629.004078 | source=vosk | frequency_hz=357.5 | rms=307 | updated_at=1778079622.10891
- [2026-05-06 23:00:30] operator / voice_transcript_partial / voice: spare light russian ask what are the voice
  meta: kind=partial | timestamp=1778079630.0043035 | source=vosk | frequency_hz=357.5 | rms=307 | updated_at=1778079622.10891
- [2026-05-06 23:00:31] operator / voice_transcript_final / voice: voice spare light russian ask what are the voice
  meta: kind=final | timestamp=1778079631.1962197 | source=final | frequency_hz=375.4 | rms=310 | updated_at=1778079630.99679
- [2026-05-06 23:00:32] operator / voice_transcript_partial / voice: changes
  meta: kind=partial | timestamp=1778079632.7712133 | source=vosk | frequency_hz=375.4 | rms=310 | updated_at=1778079630.99679
- [2026-05-06 23:00:33] operator / voice_transcript_partial / voice: changes to of
  meta: kind=partial | timestamp=1778079633.0134838 | source=vosk | frequency_hz=375.4 | rms=310 | updated_at=1778079630.99679
- [2026-05-06 23:00:33] operator / voice_transcript_partial / voice: changes to overlay
  meta: kind=partial | timestamp=1778079633.2523687 | source=vosk | frequency_hz=375.4 | rms=310 | updated_at=1778079630.99679
- [2026-05-06 23:00:33] operator / voice_transcript_partial / voice: changes to overlay name
  meta: kind=partial | timestamp=1778079633.7653039 | source=vosk | frequency_hz=375.4 | rms=310 | updated_at=1778079630.99679
- [2026-05-06 23:00:34] operator / voice_transcript_partial / voice: changes to overlay name in human voice
  meta: kind=partial | timestamp=1778079634.517306 | source=vosk | frequency_hz=375.4 | rms=310 | updated_at=1778079630.99679
- [2026-05-06 23:00:35] operator / voice_transcript_final / voice: changes to overlay name in human voice
  meta: kind=final | timestamp=1778079635.664963 | source=final | frequency_hz=347.4 | rms=301 | updated_at=1778079635.497416
- [2026-05-06 23:00:50] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1778079650.3733678 | source=vosk | frequency_hz=366.6 | rms=323 | updated_at=1778079645.2106645
- [2026-05-06 23:00:50] operator / voice_transcript_partial / voice: runtime
  meta: kind=partial | timestamp=1778079650.624363 | source=vosk | frequency_hz=366.6 | rms=323 | updated_at=1778079645.2106645
- [2026-05-06 23:00:50] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1778079650.8714952 | source=vosk | frequency_hz=366.6 | rms=323 | updated_at=1778079645.2106645
- [2026-05-06 23:00:51] operator / voice_transcript_partial / voice: e lion the hunting on
  meta: kind=partial | timestamp=1778079651.137623 | source=vosk | frequency_hz=366.6 | rms=323 | updated_at=1778079645.2106645
- [2026-05-06 23:00:51] operator / voice_transcript_partial / voice: runtime
  meta: kind=partial | timestamp=1778079651.514822 | source=vosk | frequency_hz=366.6 | rms=323 | updated_at=1778079645.2106645
- [2026-05-06 23:00:51] operator / voice_transcript_partial / voice: e lion the face
  meta: kind=partial | timestamp=1778079651.6220129 | source=vosk | frequency_hz=366.6 | rms=323 | updated_at=1778079645.2106645
- [2026-05-06 23:00:52] operator / voice_transcript_partial / voice: e lion the face hello
  meta: kind=partial | timestamp=1778079652.3703773 | source=vosk | frequency_hz=366.6 | rms=323 | updated_at=1778079645.2106645
- [2026-05-06 23:00:52] operator / voice_transcript_partial / voice: e lion the face current status
  meta: kind=partial | timestamp=1778079652.6243145 | source=vosk | frequency_hz=366.6 | rms=323 | updated_at=1778079645.2106645
- [2026-05-06 23:00:55] operator / voice_transcript_partial / voice: tell me a
  meta: kind=partial | timestamp=1778079655.6212041 | source=vosk | frequency_hz=366.6 | rms=323 | updated_at=1778079645.2106645
- [2026-05-06 23:00:55] operator / voice_transcript_partial / voice: tell me a joke
  meta: kind=partial | timestamp=1778079655.8864698 | source=vosk | frequency_hz=366.6 | rms=323 | updated_at=1778079645.2106645
- [2026-05-06 23:00:56] operator / voice_transcript_final / voice: tell me a joke
  meta: kind=final | timestamp=1778079656.7376156 | source=final | frequency_hz=388.0 | rms=299 | updated_at=1778079656.1152697
- [2026-05-06 23:00:56] operator / voice_command / voice: tell me a joke
  meta: normalized=True
- [2026-05-06 23:00:57] assistant / spoken_confirmation / voice: Alright, here is one. My favorite exercise is target practice. It is mostly core stability and tiny corrections. Want another one?
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 23:01:06] operator / voice_transcript_partial / voice: is motion control
  meta: kind=partial | timestamp=1778079666.1178386 | source=vosk | frequency_hz=334.0 | rms=335 | updated_at=1778079658.8718252
- [2026-05-06 23:01:06] operator / voice_transcript_partial / voice: is motion current
  meta: kind=partial | timestamp=1778079666.1238425 | source=vosk | frequency_hz=334.0 | rms=335 | updated_at=1778079658.8718252
- [2026-05-06 23:01:07] operator / voice_transcript_partial / voice: is last request
  meta: kind=partial | timestamp=1778079667.539604 | source=vosk | frequency_hz=334.0 | rms=335 | updated_at=1778079658.8718252
- [2026-05-06 23:01:07] operator / voice_transcript_partial / voice: is last request the current
  meta: kind=partial | timestamp=1778079667.8014057 | source=vosk | frequency_hz=284.0 | rms=279 | updated_at=1778079667.7913876
- [2026-05-06 23:01:08] operator / voice_transcript_partial / voice: is last request the current on adaptive
  meta: kind=partial | timestamp=1778079668.552053 | source=vosk | frequency_hz=284.0 | rms=279 | updated_at=1778079667.7913876
- [2026-05-06 23:01:09] operator / voice_transcript_final / voice: is last request the current on
  meta: kind=final | timestamp=1778079669.7275689 | source=final | frequency_hz=284.0 | rms=279 | updated_at=1778079667.7913876
- [2026-05-06 23:01:13] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1778079673.3211102 | source=vosk | frequency_hz=324.0 | rms=320 | updated_at=1778079672.3149996
- [2026-05-06 23:01:13] operator / voice_transcript_partial / voice: recent your
  meta: kind=partial | timestamp=1778079673.57568 | source=vosk | frequency_hz=324.0 | rms=320 | updated_at=1778079672.3149996
- [2026-05-06 23:01:14] operator / voice_transcript_final / voice: recent loop
  meta: kind=final | timestamp=1778079674.394592 | source=final | frequency_hz=324.0 | rms=320 | updated_at=1778079672.3149996
- [2026-05-06 23:01:23] operator / voice_transcript_partial / voice: alion
  meta: kind=partial | timestamp=1778079683.3201132 | source=vosk | frequency_hz=326.7 | rms=319 | updated_at=1778079682.5598955
- [2026-05-06 23:01:24] operator / voice_transcript_partial / voice: alion who are
  meta: kind=partial | timestamp=1778079684.1381652 | source=vosk | frequency_hz=326.7 | rms=319 | updated_at=1778079682.5598955
- [2026-05-06 23:01:24] operator / voice_transcript_partial / voice: alion who are you
  meta: kind=partial | timestamp=1778079684.1487384 | source=vosk | frequency_hz=326.7 | rms=319 | updated_at=1778079682.5598955
- [2026-05-06 23:01:25] operator / voice_transcript_final / voice: elion who are you
  meta: kind=final | timestamp=1778079685.0477614 | source=final | frequency_hz=326.7 | rms=319 | updated_at=1778079682.5598955
- [2026-05-06 23:01:25] operator / voice_command / voice: who are you
  meta: normalized=True
- [2026-05-06 23:01:25] assistant / assistant_prompt / text: Assistant is disabled.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-06 23:02:13] operator / voice_transcript_partial / voice: tuning
  meta: kind=partial | timestamp=1778079733.0813735 | source=vosk | frequency_hz=347.2 | rms=314 | updated_at=1778079731.0672014
- [2026-05-06 23:02:13] operator / voice_transcript_partial / voice: turn
  meta: kind=partial | timestamp=1778079733.3134794 | source=vosk | frequency_hz=347.2 | rms=314 | updated_at=1778079731.0672014
- [2026-05-06 23:02:14] operator / voice_transcript_final / voice: turn
  meta: kind=final | timestamp=1778079734.172118 | source=final | frequency_hz=412.0 | rms=289 | updated_at=1778079733.9901464
- [2026-05-06 23:02:17] operator / voice_transcript_partial / voice: acoustic
  meta: kind=partial | timestamp=1778079737.304543 | source=vosk | frequency_hz=397.9 | rms=329 | updated_at=1778079735.059267
- [2026-05-06 23:02:17] operator / voice_transcript_partial / voice: acoustic guard
  meta: kind=partial | timestamp=1778079737.5643353 | source=vosk | frequency_hz=397.9 | rms=329 | updated_at=1778079735.059267
- [2026-05-06 23:02:17] operator / voice_transcript_partial / voice: acoustic guard detection
  meta: kind=partial | timestamp=1778079737.8150694 | source=vosk | frequency_hz=397.9 | rms=329 | updated_at=1778079735.059267
- [2026-05-06 23:02:18] operator / voice_transcript_partial / voice: acoustic guard detection on e
  meta: kind=partial | timestamp=1778079738.3110473 | source=vosk | frequency_hz=397.9 | rms=329 | updated_at=1778079735.059267
- [2026-05-06 23:02:18] operator / voice_transcript_partial / voice: acoustic guard detection on event
  meta: kind=partial | timestamp=1778079738.7325716 | source=vosk | frequency_hz=397.9 | rms=329 | updated_at=1778079735.059267
- [2026-05-06 23:02:18] operator / voice_transcript_partial / voice: acoustic guard detection on e
  meta: kind=partial | timestamp=1778079738.8291314 | source=vosk | frequency_hz=397.9 | rms=329 | updated_at=1778079735.059267
- [2026-05-06 23:02:19] operator / voice_transcript_final / voice: acoustic guard detection on event
  meta: kind=final | timestamp=1778079739.4210563 | source=final | frequency_hz=397.9 | rms=329 | updated_at=1778079735.059267
- [2026-05-06 23:02:19] operator / voice_transcript_partial / voice: output
  meta: kind=partial | timestamp=1778079739.8256226 | source=vosk | frequency_hz=397.9 | rms=329 | updated_at=1778079735.059267
- [2026-05-06 23:02:20] operator / voice_transcript_partial / voice: hello
  meta: kind=partial | timestamp=1778079740.0635352 | source=vosk | frequency_hz=397.9 | rms=329 | updated_at=1778079735.059267
- [2026-05-06 23:02:21] operator / voice_transcript_final / voice: cleanup
  meta: kind=final | timestamp=1778079741.0138936 | source=final | frequency_hz=397.9 | rms=329 | updated_at=1778079735.059267
- [2026-05-06 23:02:21] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1778079741.0370572 | source=vosk | frequency_hz=397.9 | rms=329 | updated_at=1778079735.059267
- [2026-05-06 23:02:21] operator / voice_transcript_partial / voice: is the
  meta: kind=partial | timestamp=1778079741.5414157 | source=vosk | frequency_hz=397.9 | rms=329 | updated_at=1778079735.059267
- [2026-05-06 23:02:21] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1778079741.7835689 | source=vosk | frequency_hz=397.9 | rms=329 | updated_at=1778079735.059267
- [2026-05-06 23:02:22] operator / voice_transcript_partial / voice: is face
  meta: kind=partial | timestamp=1778079742.046401 | source=vosk | frequency_hz=397.9 | rms=329 | updated_at=1778079735.059267
- [2026-05-06 23:02:23] operator / voice_transcript_partial / voice: is face hello
  meta: kind=partial | timestamp=1778079743.0589929 | source=vosk | frequency_hz=397.9 | rms=329 | updated_at=1778079735.059267
- [2026-05-06 23:02:23] operator / voice_transcript_partial / voice: is the current status
  meta: kind=partial | timestamp=1778079743.281697 | source=vosk | frequency_hz=397.9 | rms=329 | updated_at=1778079735.059267
- [2026-05-06 23:02:24] operator / voice_transcript_partial / voice: is the current status engaging scope
  meta: kind=partial | timestamp=1778079744.298626 | source=vosk | frequency_hz=397.9 | rms=329 | updated_at=1778079735.059267
- [2026-05-06 23:02:24] operator / voice_transcript_final / voice: is the current status engaging
  meta: kind=final | timestamp=1778079744.908665 | source=final | frequency_hz=380.0 | rms=309 | updated_at=1778079744.7761426
- [2026-05-06 23:02:31] operator / voice_transcript_partial / voice: manual
  meta: kind=partial | timestamp=1778079751.033326 | source=vosk | frequency_hz=380.0 | rms=309 | updated_at=1778079744.7761426
- [2026-05-06 23:02:31] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1778079751.2827632 | source=vosk | frequency_hz=380.0 | rms=309 | updated_at=1778079744.7761426
- [2026-05-06 23:02:31] operator / voice_transcript_final / voice: model
  meta: kind=final | timestamp=1778079751.7470732 | source=final | frequency_hz=380.0 | rms=309 | updated_at=1778079744.7761426
- [2026-05-06 23:02:37] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778079757.5475488 | source=vosk | frequency_hz=412.0 | rms=303 | updated_at=1778079755.5271552
- [2026-05-06 23:02:37] operator / voice_transcript_partial / voice: human
  meta: kind=partial | timestamp=1778079757.7837272 | source=vosk | frequency_hz=412.0 | rms=303 | updated_at=1778079755.5271552
- [2026-05-06 23:02:38] operator / voice_transcript_partial / voice: window shortcuts
  meta: kind=partial | timestamp=1778079758.0378392 | source=vosk | frequency_hz=412.0 | rms=303 | updated_at=1778079755.5271552
- [2026-05-06 23:02:38] operator / voice_transcript_partial / voice: human voice reports
  meta: kind=partial | timestamp=1778079758.2833834 | source=vosk | frequency_hz=412.0 | rms=303 | updated_at=1778079755.5271552
- [2026-05-06 23:02:38] operator / voice_transcript_partial / voice: human loop
  meta: kind=partial | timestamp=1778079758.8237092 | source=vosk | frequency_hz=388.0 | rms=293 | updated_at=1778079758.8033845
- [2026-05-06 23:02:39] operator / voice_transcript_final / voice: human the loop
  meta: kind=final | timestamp=1778079759.128345 | source=final | frequency_hz=371.2 | rms=316 | updated_at=1778079759.0275738
- [2026-05-06 23:02:45] operator / voice_transcript_partial / voice: do you
  meta: kind=partial | timestamp=1778079765.7956743 | source=vosk | frequency_hz=369.6 | rms=314 | updated_at=1778079763.7769768
- [2026-05-06 23:02:46] operator / voice_transcript_final / voice: you
  meta: kind=final | timestamp=1778079766.6026258 | source=final | frequency_hz=369.6 | rms=314 | updated_at=1778079763.7769768
- [2026-05-06 23:02:55] operator / voice_transcript_partial / voice: acoustic guard detection on motion ml
  meta: kind=partial | timestamp=1778079775.0215268 | source=vosk | frequency_hz=369.6 | rms=314 | updated_at=1778079763.7769768
- [2026-05-06 23:02:55] operator / voice_transcript_partial / voice: acoustic guard detection on motion ml for
  meta: kind=partial | timestamp=1778079775.5365243 | source=vosk | frequency_hz=198.0 | rms=777 | updated_at=1778079775.022527
- [2026-05-06 23:02:55] operator / voice_transcript_partial / voice: acoustic guard detection on motion ml for prompted
  meta: kind=partial | timestamp=1778079775.779306 | source=vosk | frequency_hz=265.2 | rms=831 | updated_at=1778079775.7732973
- [2026-05-06 23:02:56] operator / voice_transcript_partial / voice: acoustic guard detection on motion ml for
  meta: kind=partial | timestamp=1778079776.0279393 | source=vosk | frequency_hz=265.2 | rms=831 | updated_at=1778079775.7732973
- [2026-05-06 23:02:56] operator / voice_transcript_partial / voice: acoustic guard detection on motion ml for face
  meta: kind=partial | timestamp=1778079776.2809148 | source=vosk | frequency_hz=265.2 | rms=831 | updated_at=1778079775.7732973
- [2026-05-06 23:02:56] operator / voice_transcript_partial / voice: acoustic guard detection on motion ml for face lion
  meta: kind=partial | timestamp=1778079776.529514 | source=vosk | frequency_hz=265.2 | rms=831 | updated_at=1778079775.7732973
- [2026-05-06 23:02:57] operator / voice_transcript_partial / voice: acoustic guard detection on motion ml for face lion current
  meta: kind=partial | timestamp=1778079777.2822282 | source=vosk | frequency_hz=265.2 | rms=831 | updated_at=1778079775.7732973
- [2026-05-06 23:02:57] operator / voice_transcript_partial / voice: acoustic guard detection on motion ml for face lion current status
  meta: kind=partial | timestamp=1778079777.5309756 | source=vosk | frequency_hz=265.2 | rms=831 | updated_at=1778079775.7732973
- [2026-05-06 23:02:58] operator / voice_transcript_partial / voice: acoustic guard detection on motion ml for face lion current status engaging scope
  meta: kind=partial | timestamp=1778079778.7093642 | source=vosk | frequency_hz=364.0 | rms=303 | updated_at=1778079778.6963594
- [2026-05-06 23:02:59] operator / voice_transcript_partial / voice: acoustic guard detection on motion ml for face lion current status engaging acoustic
  meta: kind=partial | timestamp=1778079779.279767 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:02:59] operator / voice_transcript_partial / voice: acoustic guard detection on motion ml for face lion current status engaging acoustic guard
  meta: kind=partial | timestamp=1778079779.778641 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:00] operator / voice_transcript_partial / voice: acoustic guard detection on motion ml for face lion current status engaging acoustic guard detection
  meta: kind=partial | timestamp=1778079780.2784452 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:00] operator / voice_transcript_partial / voice: acoustic guard detection on motion ml for face lion current status engaging acoustic guard detection on
  meta: kind=partial | timestamp=1778079780.9898107 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:01] operator / voice_transcript_partial / voice: acoustic guard detection on motion ml for face lion current status engaging acoustic guard detection on mute
  meta: kind=partial | timestamp=1778079781.0285428 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:01] operator / voice_transcript_partial / voice: acoustic guard detection on motion ml for face lion current status engaging acoustic guard detection on visual sound
  meta: kind=partial | timestamp=1778079781.7122982 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:02] operator / voice_transcript_partial / voice: acoustic guard detection on motion ml for face lion current status engaging acoustic guard detection on visual sound of
  meta: kind=partial | timestamp=1778079782.0294895 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:02] operator / voice_transcript_partial / voice: acoustic guard detection on motion ml for face lion current status engaging acoustic guard detection on visual sound of output
  meta: kind=partial | timestamp=1778079782.2805173 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:02] operator / voice_transcript_partial / voice: acoustic guard detection on motion ml for face lion current status engaging acoustic guard detection on visual sound of leon
  meta: kind=partial | timestamp=1778079782.5297568 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:04] operator / voice_transcript_partial / voice: system
  meta: kind=partial | timestamp=1778079784.5738027 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:05] operator / voice_transcript_partial / voice: system current
  meta: kind=partial | timestamp=1778079785.838909 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:06] operator / voice_transcript_partial / voice: system current status
  meta: kind=partial | timestamp=1778079786.011672 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:06] operator / voice_transcript_partial / voice: system current
  meta: kind=partial | timestamp=1778079786.253578 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:07] operator / voice_transcript_partial / voice: system current engaging scope
  meta: kind=partial | timestamp=1778079787.0647283 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:07] operator / voice_transcript_final / voice: system current engaging
  meta: kind=final | timestamp=1778079787.5932329 | source=final | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:08] operator / voice_transcript_partial / voice: acoustic
  meta: kind=partial | timestamp=1778079788.7527397 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:09] operator / voice_transcript_partial / voice: acoustic guard
  meta: kind=partial | timestamp=1778079789.251131 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:09] operator / voice_transcript_partial / voice: acoustic guard disabled
  meta: kind=partial | timestamp=1778079789.7654738 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:10] operator / voice_transcript_partial / voice: acoustic guard deactivate
  meta: kind=partial | timestamp=1778079790.017841 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:10] operator / voice_transcript_partial / voice: acoustic guard the prompted
  meta: kind=partial | timestamp=1778079790.250107 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:10] operator / voice_transcript_partial / voice: acoustic guard the prompted on visual
  meta: kind=partial | timestamp=1778079790.5045516 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:11] operator / voice_transcript_partial / voice: acoustic guard the prompted on visual sound cues
  meta: kind=partial | timestamp=1778079791.0023403 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:11] operator / voice_transcript_final / voice: acoustic guard the prompted on visual sound
  meta: kind=final | timestamp=1778079791.3589778 | source=final | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:11] operator / voice_transcript_partial / voice: of output
  meta: kind=partial | timestamp=1778079791.767898 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:12] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1778079792.0142293 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:12] operator / voice_transcript_partial / voice: a lion
  meta: kind=partial | timestamp=1778079792.5005636 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:13] operator / voice_transcript_partial / voice: a lion status
  meta: kind=partial | timestamp=1778079793.252344 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:13] operator / voice_transcript_partial / voice: a lion safe zone
  meta: kind=partial | timestamp=1778079793.58421 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:13] operator / voice_transcript_partial / voice: a lion safe
  meta: kind=partial | timestamp=1778079793.7641892 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:14] operator / voice_transcript_partial / voice: a lion safe deactivate
  meta: kind=partial | timestamp=1778079794.0032966 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:14] operator / voice_transcript_partial / voice: a lion safe deactivate adaptive
  meta: kind=partial | timestamp=1778079794.2782853 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:14] operator / voice_transcript_partial / voice: a lion safe deactivate the known
  meta: kind=partial | timestamp=1778079794.5129652 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:14] operator / voice_transcript_partial / voice: a lion safe deactivate the known face
  meta: kind=partial | timestamp=1778079794.7561193 | source=vosk | frequency_hz=383.6 | rms=312 | updated_at=1778079778.7733963
- [2026-05-06 23:03:15] operator / voice_transcript_partial / voice: a lion safe deactivate the known face current
  meta: kind=partial | timestamp=1778079795.5114164 | source=vosk | frequency_hz=356.0 | rms=325 | updated_at=1778079794.995862
- [2026-05-06 23:03:15] operator / voice_transcript_partial / voice: a lion safe deactivate the known face current status
  meta: kind=partial | timestamp=1778079795.7507951 | source=vosk | frequency_hz=356.0 | rms=325 | updated_at=1778079794.995862
- [2026-05-06 23:03:16] operator / voice_transcript_partial / voice: a lion safe deactivate the known face current
  meta: kind=partial | timestamp=1778079796.0173833 | source=vosk | frequency_hz=356.0 | rms=325 | updated_at=1778079794.995862
- [2026-05-06 23:03:27] operator / voice_transcript_partial / voice: the status
  meta: kind=partial | timestamp=1778079807.415122 | source=vosk | frequency_hz=197.0 | rms=1203 | updated_at=1778079806.6400266
- [2026-05-06 23:03:27] operator / voice_transcript_partial / voice: display deactivate
  meta: kind=partial | timestamp=1778079807.6478183 | source=vosk | frequency_hz=197.0 | rms=1203 | updated_at=1778079806.6400266
- [2026-05-06 23:03:27] operator / voice_transcript_partial / voice: the status of
  meta: kind=partial | timestamp=1778079807.9018269 | source=vosk | frequency_hz=197.0 | rms=1203 | updated_at=1778079806.6400266
- [2026-05-06 23:03:28] operator / voice_transcript_partial / voice: the status of is
  meta: kind=partial | timestamp=1778079808.560283 | source=vosk | frequency_hz=197.0 | rms=1203 | updated_at=1778079806.6400266
- [2026-05-06 23:03:28] operator / voice_transcript_partial / voice: the status of is learning
  meta: kind=partial | timestamp=1778079808.6488268 | source=vosk | frequency_hz=197.0 | rms=1203 | updated_at=1778079806.6400266
- [2026-05-06 23:03:28] operator / voice_transcript_partial / voice: the status of is learning scoring
  meta: kind=partial | timestamp=1778079808.896827 | source=vosk | frequency_hz=197.0 | rms=1203 | updated_at=1778079806.6400266
- [2026-05-06 23:03:29] operator / voice_transcript_partial / voice: the status of is logging
  meta: kind=partial | timestamp=1778079809.1833026 | source=vosk | frequency_hz=197.0 | rms=1203 | updated_at=1778079806.6400266
- [2026-05-06 23:03:29] operator / voice_transcript_partial / voice: the status of slew order
  meta: kind=partial | timestamp=1778079809.4004672 | source=vosk | frequency_hz=197.0 | rms=1203 | updated_at=1778079806.6400266
- [2026-05-06 23:03:30] operator / voice_transcript_final / voice: the status of is slew order
  meta: kind=final | timestamp=1778079810.212099 | source=final | frequency_hz=197.0 | rms=1203 | updated_at=1778079806.6400266
- [2026-05-06 23:03:30] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778079810.363165 | source=vosk | frequency_hz=197.0 | rms=1203 | updated_at=1778079806.6400266
- [2026-05-06 23:03:31] operator / voice_transcript_partial / voice: the acoustic
  meta: kind=partial | timestamp=1778079811.645633 | source=vosk | frequency_hz=352.0 | rms=307 | updated_at=1778079811.1459422
- [2026-05-06 23:03:32] operator / voice_transcript_partial / voice: the acoustic guard
  meta: kind=partial | timestamp=1778079812.146825 | source=vosk | frequency_hz=352.0 | rms=307 | updated_at=1778079811.1459422
- [2026-05-06 23:03:32] operator / voice_transcript_partial / voice: the acoustic guard detection
  meta: kind=partial | timestamp=1778079812.6741862 | source=vosk | frequency_hz=352.0 | rms=307 | updated_at=1778079811.1459422
- [2026-05-06 23:03:33] operator / voice_transcript_partial / voice: the acoustic guard detection on
  meta: kind=partial | timestamp=1778079813.148156 | source=vosk | frequency_hz=352.0 | rms=307 | updated_at=1778079811.1459422
- [2026-05-06 23:03:33] operator / voice_transcript_partial / voice: the acoustic guard detection on use
  meta: kind=partial | timestamp=1778079813.3955834 | source=vosk | frequency_hz=352.0 | rms=307 | updated_at=1778079811.1459422
- [2026-05-06 23:03:33] operator / voice_transcript_partial / voice: the acoustic guard detection on mute
  meta: kind=partial | timestamp=1778079813.6471267 | source=vosk | frequency_hz=352.0 | rms=307 | updated_at=1778079811.1459422
- [2026-05-06 23:03:33] operator / voice_transcript_partial / voice: the acoustic guard detection on mute window shortcuts
  meta: kind=partial | timestamp=1778079813.9386113 | source=vosk | frequency_hz=352.0 | rms=307 | updated_at=1778079811.1459422
- [2026-05-06 23:03:34] operator / voice_transcript_partial / voice: the acoustic guard detection on mute window
  meta: kind=partial | timestamp=1778079814.1472437 | source=vosk | frequency_hz=352.0 | rms=307 | updated_at=1778079811.1459422
- [2026-05-06 23:03:34] operator / voice_transcript_partial / voice: the acoustic guard detection on mute window shortcuts
  meta: kind=partial | timestamp=1778079814.517632 | source=vosk | frequency_hz=352.0 | rms=307 | updated_at=1778079811.1459422
- [2026-05-06 23:03:34] operator / voice_transcript_partial / voice: the acoustic guard detection on mute window guard
  meta: kind=partial | timestamp=1778079814.6482573 | source=vosk | frequency_hz=352.0 | rms=307 | updated_at=1778079811.1459422
- [2026-05-06 23:03:35] operator / voice_transcript_final / voice: the acoustic guard detection id on mute window guard
  meta: kind=final | timestamp=1778079815.7086694 | source=final | frequency_hz=394.8 | rms=314 | updated_at=1778079815.1411886
- [2026-05-06 23:03:35] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1778079815.7641437 | source=vosk | frequency_hz=394.8 | rms=314 | updated_at=1778079815.1411886
- [2026-05-06 23:03:35] operator / voice_transcript_partial / voice: one drafts
  meta: kind=partial | timestamp=1778079815.8951232 | source=vosk | frequency_hz=394.8 | rms=314 | updated_at=1778079815.1411886
- [2026-05-06 23:03:36] operator / voice_transcript_partial / voice: one disabled
  meta: kind=partial | timestamp=1778079816.1632478 | source=vosk | frequency_hz=394.8 | rms=314 | updated_at=1778079815.1411886
- [2026-05-06 23:03:36] operator / voice_transcript_partial / voice: lion disable of
  meta: kind=partial | timestamp=1778079816.4157162 | source=vosk | frequency_hz=394.8 | rms=314 | updated_at=1778079815.1411886
- [2026-05-06 23:03:36] operator / voice_transcript_partial / voice: lion disable of of face
  meta: kind=partial | timestamp=1778079816.9006653 | source=vosk | frequency_hz=394.8 | rms=314 | updated_at=1778079815.1411886
- [2026-05-06 23:03:37] operator / voice_transcript_partial / voice: lion disable of of face lion
  meta: kind=partial | timestamp=1778079817.1495245 | source=vosk | frequency_hz=394.8 | rms=314 | updated_at=1778079815.1411886
- [2026-05-06 23:03:37] operator / voice_transcript_partial / voice: lion disable of of face lion current
  meta: kind=partial | timestamp=1778079817.897177 | source=vosk | frequency_hz=394.8 | rms=314 | updated_at=1778079815.1411886
- [2026-05-06 23:03:38] operator / voice_transcript_partial / voice: lion disable of of face lion current status
  meta: kind=partial | timestamp=1778079818.14533 | source=vosk | frequency_hz=394.8 | rms=314 | updated_at=1778079815.1411886
- [2026-05-06 23:03:39] operator / voice_transcript_partial / voice: lion disable of of face lion current status engaging scope
  meta: kind=partial | timestamp=1778079819.1602952 | source=vosk | frequency_hz=392.0 | rms=302 | updated_at=1778079819.1542935
- [2026-05-06 23:03:40] operator / voice_transcript_final / voice: elion lion disable of of face lion current status engaging
  meta: kind=final | timestamp=1778079820.5483499 | source=final | frequency_hz=378.8 | rms=324 | updated_at=1778079819.8973186
- [2026-05-06 23:03:41] operator / voice_command / voice: lion disable of of face lion current status engaging
  meta: normalized=True
- [2026-05-06 23:03:42] assistant / spoken_confirmation / voice: I can keep going with voice change. Tell me a voice family like Russian or Indian, ask what are the options, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 23:03:51] operator / voice_transcript_partial / voice: e go e with voice change tell me a voice manual light russian order enabled
  meta: kind=partial | timestamp=1778079831.0425065 | source=vosk | frequency_hz=372.0 | rms=308 | updated_at=1778079827.4006715
- [2026-05-06 23:03:51] operator / voice_transcript_partial / voice: e go e with voice change tell me a voice manual light russian order in
  meta: kind=partial | timestamp=1778079831.048015 | source=vosk | frequency_hz=372.0 | rms=308 | updated_at=1778079827.4006715
- [2026-05-06 23:03:51] operator / voice_transcript_partial / voice: e go e with voice change tell me a voice manual light russian order in app
  meta: kind=partial | timestamp=1778079831.802727 | source=vosk | frequency_hz=372.0 | rms=308 | updated_at=1778079827.4006715
- [2026-05-06 23:03:52] operator / voice_transcript_final / voice: e go e with voice change tell me a voice manual light russian order it again app
  meta: kind=final | timestamp=1778079832.3904257 | source=final | frequency_hz=372.0 | rms=308 | updated_at=1778079827.4006715
- [2026-05-06 23:03:52] operator / voice_command / voice: e go e with voice change tell me a voice manual light russian order it again app
  meta: normalized=True
- [2026-05-06 23:03:53] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 23:03:52] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1778079832.5498295 | source=vosk | frequency_hz=372.0 | rms=308 | updated_at=1778079827.4006715
- [2026-05-06 23:03:52] operator / voice_transcript_partial / voice: for status
  meta: kind=partial | timestamp=1778079832.8016548 | source=vosk | frequency_hz=372.0 | rms=308 | updated_at=1778079827.4006715
- [2026-05-06 23:03:53] operator / voice_transcript_partial / voice: for safe cancel
  meta: kind=partial | timestamp=1778079833.4920878 | source=vosk | frequency_hz=372.0 | rms=308 | updated_at=1778079827.4006715
- [2026-05-06 23:03:54] operator / voice_transcript_partial / voice: for safe cancel what are
  meta: kind=partial | timestamp=1778079834.2909632 | source=vosk | frequency_hz=372.0 | rms=308 | updated_at=1778079827.4006715
- [2026-05-06 23:03:54] operator / voice_transcript_partial / voice: for safe cancel what are microphone
  meta: kind=partial | timestamp=1778079834.5641904 | source=vosk | frequency_hz=372.0 | rms=308 | updated_at=1778079827.4006715
- [2026-05-06 23:03:54] operator / voice_transcript_partial / voice: for safe cancel what are mode
  meta: kind=partial | timestamp=1778079834.806267 | source=vosk | frequency_hz=372.0 | rms=308 | updated_at=1778079827.4006715
- [2026-05-06 23:03:55] operator / voice_transcript_partial / voice: for safe cancel what are motion
  meta: kind=partial | timestamp=1778079835.0415196 | source=vosk | frequency_hz=372.0 | rms=308 | updated_at=1778079827.4006715
- [2026-05-06 23:03:55] operator / voice_transcript_partial / voice: for safe cancel what are mode off show no fire
  meta: kind=partial | timestamp=1778079835.547739 | source=vosk | frequency_hz=372.0 | rms=308 | updated_at=1778079827.4006715
- [2026-05-06 23:03:55] operator / voice_transcript_partial / voice: for safe cancel what are motion light window shortcuts
  meta: kind=partial | timestamp=1778079835.7899897 | source=vosk | frequency_hz=372.0 | rms=308 | updated_at=1778079827.4006715
- [2026-05-06 23:03:56] operator / voice_transcript_partial / voice: for safe cancel what are motion for human voice
  meta: kind=partial | timestamp=1778079836.055089 | source=vosk | frequency_hz=372.0 | rms=308 | updated_at=1778079827.4006715
- [2026-05-06 23:03:56] operator / voice_transcript_partial / voice: for safe cancel what are motion for human voice leon
  meta: kind=partial | timestamp=1778079836.5409343 | source=vosk | frequency_hz=372.0 | rms=308 | updated_at=1778079827.4006715
- [2026-05-06 23:03:57] operator / voice_transcript_partial / voice: for safe cancel what are motion for human voice leon is
  meta: kind=partial | timestamp=1778079837.7916894 | source=vosk | frequency_hz=372.0 | rms=308 | updated_at=1778079827.4006715
- [2026-05-06 23:03:59] operator / voice_transcript_partial / voice: auto speak
  meta: kind=partial | timestamp=1778079839.521519 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:03:59] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1778079839.7952006 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:00] operator / voice_transcript_partial / voice: auto export
  meta: kind=partial | timestamp=1778079840.055647 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:00] operator / voice_transcript_partial / voice: sentry
  meta: kind=partial | timestamp=1778079840.2843564 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:00] operator / voice_transcript_partial / voice: active voice reports
  meta: kind=partial | timestamp=1778079840.521255 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:00] operator / voice_transcript_partial / voice: sentry board
  meta: kind=partial | timestamp=1778079840.768112 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:01] operator / voice_transcript_final / voice: sentry default
  meta: kind=final | timestamp=1778079841.5273607 | source=final | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:01] operator / voice_transcript_partial / voice: acoustic
  meta: kind=partial | timestamp=1778079841.554052 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:02] operator / voice_transcript_partial / voice: acoustic detection
  meta: kind=partial | timestamp=1778079842.5546734 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:02] operator / voice_transcript_partial / voice: acoustic adaptive after
  meta: kind=partial | timestamp=1778079842.8109303 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:03] operator / voice_transcript_partial / voice: acoustic adaptive elliot
  meta: kind=partial | timestamp=1778079843.050126 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:03] operator / voice_transcript_partial / voice: acoustic adaptive alien is
  meta: kind=partial | timestamp=1778079843.2977738 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:03] operator / voice_transcript_partial / voice: acoustic adaptive elliot
  meta: kind=partial | timestamp=1778079843.5645103 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:04] operator / voice_transcript_partial / voice: of output
  meta: kind=partial | timestamp=1778079844.5478592 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:04] operator / voice_transcript_partial / voice: of hello per session
  meta: kind=partial | timestamp=1778079844.7974553 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:05] operator / voice_transcript_partial / voice: of output on
  meta: kind=partial | timestamp=1778079845.0689447 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:05] operator / voice_transcript_final / voice: of output on
  meta: kind=final | timestamp=1778079845.7518945 | source=final | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:06] operator / voice_transcript_partial / voice: enabled
  meta: kind=partial | timestamp=1778079846.0487382 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:06] operator / voice_transcript_partial / voice: enable
  meta: kind=partial | timestamp=1778079846.298809 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:06] operator / voice_transcript_partial / voice: a lion abort
  meta: kind=partial | timestamp=1778079846.7759018 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:06] operator / voice_transcript_partial / voice: enable the automatic
  meta: kind=partial | timestamp=1778079846.805796 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:07] operator / voice_transcript_partial / voice: a lion abort face
  meta: kind=partial | timestamp=1778079847.0716467 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:08] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778079848.081206 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:08] operator / voice_transcript_partial / voice: current status
  meta: kind=partial | timestamp=1778079848.3181603 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:08] operator / voice_transcript_partial / voice: current face in human
  meta: kind=partial | timestamp=1778079848.81356 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:09] operator / voice_transcript_partial / voice: current face
  meta: kind=partial | timestamp=1778079849.074778 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:09] operator / voice_transcript_partial / voice: current face engaging scope
  meta: kind=partial | timestamp=1778079849.3018088 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:10] operator / voice_transcript_final / voice: current face engaging
  meta: kind=final | timestamp=1778079850.3102028 | source=final | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:10] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1778079850.7967305 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:11] operator / voice_transcript_partial / voice: acoustic
  meta: kind=partial | timestamp=1778079851.069722 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:11] operator / voice_transcript_partial / voice: acoustic guard
  meta: kind=partial | timestamp=1778079851.3199832 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:11] operator / voice_transcript_partial / voice: acoustic guard disabled
  meta: kind=partial | timestamp=1778079851.5611625 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:11] operator / voice_transcript_partial / voice: acoustic guard detection
  meta: kind=partial | timestamp=1778079851.798342 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:12] operator / voice_transcript_partial / voice: acoustic guard detection on
  meta: kind=partial | timestamp=1778079852.0485718 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:12] operator / voice_transcript_partial / voice: acoustic guard detection on use
  meta: kind=partial | timestamp=1778079852.6317544 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:12] operator / voice_transcript_partial / voice: acoustic guard detection on neutral
  meta: kind=partial | timestamp=1778079852.6603973 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:13] operator / voice_transcript_final / voice: acoustic guard detection on neutral
  meta: kind=final | timestamp=1778079853.18406 | source=final | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:13] operator / voice_transcript_partial / voice: announcements
  meta: kind=partial | timestamp=1778079853.5559802 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:13] operator / voice_transcript_partial / voice: of output
  meta: kind=partial | timestamp=1778079853.824034 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:14] operator / voice_transcript_partial / voice: ml
  meta: kind=partial | timestamp=1778079854.0650048 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:15] operator / voice_transcript_final / voice: output
  meta: kind=final | timestamp=1778079855.1726704 | source=final | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:15] operator / voice_transcript_partial / voice: fire
  meta: kind=partial | timestamp=1778079855.188434 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:15] operator / voice_transcript_partial / voice: fire disabled
  meta: kind=partial | timestamp=1778079855.6932926 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:15] operator / voice_transcript_partial / voice: fire test
  meta: kind=partial | timestamp=1778079855.9299653 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:16] operator / voice_transcript_partial / voice: fire for
  meta: kind=partial | timestamp=1778079856.4925718 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:16] operator / voice_transcript_partial / voice: fire for you do
  meta: kind=partial | timestamp=1778079856.6891854 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:17] operator / voice_transcript_partial / voice: fire for you do it
  meta: kind=partial | timestamp=1778079857.4328272 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:17] operator / voice_transcript_partial / voice: fire for you do it status
  meta: kind=partial | timestamp=1778079857.6783662 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:17] operator / voice_transcript_partial / voice: fire for you do it status guarding mode
  meta: kind=partial | timestamp=1778079857.9813135 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:18] operator / voice_transcript_final / voice: fire for do it status guard
  meta: kind=final | timestamp=1778079858.6308959 | source=final | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:19] operator / voice_transcript_partial / voice: pan inversion
  meta: kind=partial | timestamp=1778079859.1781764 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:19] operator / voice_transcript_partial / voice: pan inversion running
  meta: kind=partial | timestamp=1778079859.4759762 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:20] operator / voice_transcript_partial / voice: pan inversion running detection
  meta: kind=partial | timestamp=1778079860.1953247 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:20] operator / voice_transcript_partial / voice: pan inversion running detection off
  meta: kind=partial | timestamp=1778079860.6772933 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:21] operator / voice_transcript_partial / voice: pan inversion running detection off visual
  meta: kind=partial | timestamp=1778079861.1630673 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:21] operator / voice_transcript_partial / voice: pan inversion running detection off neutral
  meta: kind=partial | timestamp=1778079861.1954966 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:21] operator / voice_transcript_partial / voice: pan inversion running detection off neutral turn on
  meta: kind=partial | timestamp=1778079861.4445937 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:21] operator / voice_transcript_partial / voice: pan inversion running detection off neutral turn
  meta: kind=partial | timestamp=1778079861.6810503 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:22] operator / voice_transcript_partial / voice: pan inversion running detection off neutral turn of actions
  meta: kind=partial | timestamp=1778079862.440989 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:22] operator / voice_transcript_partial / voice: pan inversion running detection off neutral turn of action execution
  meta: kind=partial | timestamp=1778079862.7007732 | source=vosk | frequency_hz=104.0 | rms=392 | updated_at=1778079839.0137188
- [2026-05-06 23:04:23] operator / voice_transcript_final / voice: pan inversion manual detection off neutral turn of actions
  meta: kind=final | timestamp=1778079863.7171671 | source=final | frequency_hz=340.0 | rms=324 | updated_at=1778079862.9235153
- [2026-05-06 23:04:23] operator / voice_transcript_partial / voice: known
  meta: kind=partial | timestamp=1778079863.8991568 | source=vosk | frequency_hz=340.0 | rms=324 | updated_at=1778079862.9235153
- [2026-05-06 23:04:23] operator / voice_transcript_partial / voice: name gesture
  meta: kind=partial | timestamp=1778079863.9503658 | source=vosk | frequency_hz=340.0 | rms=324 | updated_at=1778079862.9235153
- [2026-05-06 23:04:24] operator / voice_transcript_partial / voice: name disable
  meta: kind=partial | timestamp=1778079864.179382 | source=vosk | frequency_hz=340.0 | rms=324 | updated_at=1778079862.9235153
- [2026-05-06 23:04:24] operator / voice_transcript_partial / voice: name disable the led
  meta: kind=partial | timestamp=1778079864.42861 | source=vosk | frequency_hz=340.0 | rms=324 | updated_at=1778079862.9235153
- [2026-05-06 23:04:24] operator / voice_transcript_partial / voice: name disable face
  meta: kind=partial | timestamp=1778079864.6946151 | source=vosk | frequency_hz=340.0 | rms=324 | updated_at=1778079862.9235153
- [2026-05-06 23:04:25] operator / voice_transcript_final / voice: name disable face
  meta: kind=final | timestamp=1778079865.7754817 | source=final | frequency_hz=340.0 | rms=324 | updated_at=1778079862.9235153
- [2026-05-06 23:04:26] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778079866.2671058 | source=vosk | frequency_hz=340.0 | rms=324 | updated_at=1778079862.9235153
- [2026-05-06 23:04:26] operator / voice_transcript_partial / voice: current status
  meta: kind=partial | timestamp=1778079866.2931354 | source=vosk | frequency_hz=340.0 | rms=324 | updated_at=1778079862.9235153
- [2026-05-06 23:04:26] operator / voice_transcript_partial / voice: current status of
  meta: kind=partial | timestamp=1778079866.4404907 | source=vosk | frequency_hz=340.0 | rms=324 | updated_at=1778079862.9235153
- [2026-05-06 23:04:26] operator / voice_transcript_partial / voice: current status
  meta: kind=partial | timestamp=1778079866.6932633 | source=vosk | frequency_hz=340.0 | rms=324 | updated_at=1778079862.9235153
- [2026-05-06 23:04:27] operator / voice_transcript_final / voice: current status
  meta: kind=final | timestamp=1778079867.133033 | source=final | frequency_hz=340.0 | rms=324 | updated_at=1778079862.9235153
- [2026-05-06 23:04:29] operator / voice_transcript_partial / voice: fire mask leon
  meta: kind=partial | timestamp=1778079869.9507415 | source=vosk | frequency_hz=340.0 | rms=324 | updated_at=1778079862.9235153
- [2026-05-06 23:04:30] operator / voice_transcript_partial / voice: fire mask mute buzzer
  meta: kind=partial | timestamp=1778079870.2129118 | source=vosk | frequency_hz=340.0 | rms=324 | updated_at=1778079862.9235153
- [2026-05-06 23:04:30] operator / voice_transcript_partial / voice: fire mask the current
  meta: kind=partial | timestamp=1778079870.4302936 | source=vosk | frequency_hz=340.0 | rms=324 | updated_at=1778079862.9235153
- [2026-05-06 23:04:31] operator / voice_transcript_partial / voice: fire mask the current status
  meta: kind=partial | timestamp=1778079871.2950652 | source=vosk | frequency_hz=340.0 | rms=324 | updated_at=1778079862.9235153
- [2026-05-06 23:04:31] operator / voice_transcript_final / voice: fire mask loop on
  meta: kind=final | timestamp=1778079871.4973447 | source=final | frequency_hz=340.0 | rms=324 | updated_at=1778079862.9235153
- [2026-05-06 23:04:31] operator / voice_transcript_partial / voice: acoustic
  meta: kind=partial | timestamp=1778079871.6073582 | source=vosk | frequency_hz=340.0 | rms=324 | updated_at=1778079862.9235153
- [2026-05-06 23:04:32] operator / voice_transcript_partial / voice: detection
  meta: kind=partial | timestamp=1778079872.3224676 | source=vosk | frequency_hz=340.0 | rms=324 | updated_at=1778079862.9235153
- [2026-05-06 23:04:33] operator / voice_transcript_partial / voice: detection on
  meta: kind=partial | timestamp=1778079873.3338895 | source=vosk | frequency_hz=340.0 | rms=324 | updated_at=1778079862.9235153
- [2026-05-06 23:04:33] operator / voice_transcript_partial / voice: detection active
  meta: kind=partial | timestamp=1778079873.3405118 | source=vosk | frequency_hz=340.0 | rms=324 | updated_at=1778079862.9235153
- [2026-05-06 23:04:33] operator / voice_transcript_final / voice: detection active
  meta: kind=final | timestamp=1778079873.661382 | source=final | frequency_hz=190.0 | rms=224 | updated_at=1778079873.5841036
- [2026-05-06 23:04:35] operator / voice_transcript_partial / voice: pan inversion disabled
  meta: kind=partial | timestamp=1778079875.0938683 | source=vosk | frequency_hz=160.6 | rms=1063 | updated_at=1778079873.8404732
- [2026-05-06 23:04:36] operator / voice_transcript_partial / voice: pan inversion enabled
  meta: kind=partial | timestamp=1778079876.122051 | source=vosk | frequency_hz=160.6 | rms=1063 | updated_at=1778079873.8404732
- [2026-05-06 23:04:36] operator / voice_transcript_partial / voice: pan inversion enabled face
  meta: kind=partial | timestamp=1778079876.5993423 | source=vosk | frequency_hz=160.6 | rms=1063 | updated_at=1778079873.8404732
- [2026-05-06 23:04:37] operator / voice_transcript_final / voice: pan inversion enable face
  meta: kind=final | timestamp=1778079877.6978474 | source=final | frequency_hz=374.0 | rms=297 | updated_at=1778079877.0903618
- [2026-05-06 23:04:38] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778079878.1550817 | source=vosk | frequency_hz=374.0 | rms=297 | updated_at=1778079877.0903618
- [2026-05-06 23:04:38] operator / voice_transcript_partial / voice: current status
  meta: kind=partial | timestamp=1778079878.181002 | source=vosk | frequency_hz=374.0 | rms=297 | updated_at=1778079877.0903618
- [2026-05-06 23:04:38] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778079878.952815 | source=vosk | frequency_hz=374.0 | rms=297 | updated_at=1778079877.0903618
- [2026-05-06 23:04:39] operator / voice_transcript_final / voice: current
  meta: kind=final | timestamp=1778079879.3612564 | source=final | frequency_hz=374.0 | rms=297 | updated_at=1778079877.0903618
- [2026-05-06 23:04:42] operator / voice_transcript_partial / voice: acoustic
  meta: kind=partial | timestamp=1778079882.6501713 | source=vosk | frequency_hz=368.0 | rms=312 | updated_at=1778079880.3881934
- [2026-05-06 23:04:43] operator / voice_transcript_partial / voice: acoustic guard
  meta: kind=partial | timestamp=1778079883.3637893 | source=vosk | frequency_hz=368.0 | rms=312 | updated_at=1778079880.3881934
- [2026-05-06 23:04:43] operator / voice_transcript_partial / voice: acoustic guard enabled
  meta: kind=partial | timestamp=1778079883.417061 | source=vosk | frequency_hz=368.0 | rms=312 | updated_at=1778079880.3881934
- [2026-05-06 23:04:43] operator / voice_transcript_final / voice: acoustic guard
  meta: kind=final | timestamp=1778079883.7747416 | source=final | frequency_hz=368.0 | rms=312 | updated_at=1778079880.3881934
- [2026-05-06 23:04:45] operator / voice_transcript_partial / voice: of output
  meta: kind=partial | timestamp=1778079885.5620291 | source=vosk | frequency_hz=368.0 | rms=312 | updated_at=1778079880.3881934
- [2026-05-06 23:04:45] operator / voice_transcript_partial / voice: ml training
  meta: kind=partial | timestamp=1778079885.6441717 | source=vosk | frequency_hz=368.0 | rms=312 | updated_at=1778079880.3881934
- [2026-05-06 23:04:46] operator / voice_transcript_partial / voice: of output active
  meta: kind=partial | timestamp=1778079886.1467388 | source=vosk | frequency_hz=368.0 | rms=312 | updated_at=1778079880.3881934
- [2026-05-06 23:04:46] operator / voice_transcript_final / voice: of output hunting on
  meta: kind=final | timestamp=1778079886.7848988 | source=final | frequency_hz=368.0 | rms=312 | updated_at=1778079880.3881934
- [2026-05-06 23:04:46] operator / voice_transcript_partial / voice: hey
  meta: kind=partial | timestamp=1778079886.9206753 | source=vosk | frequency_hz=368.0 | rms=312 | updated_at=1778079880.3881934
- [2026-05-06 23:04:47] operator / voice_transcript_partial / voice: hey disable
  meta: kind=partial | timestamp=1778079887.1483135 | source=vosk | frequency_hz=368.0 | rms=312 | updated_at=1778079880.3881934
- [2026-05-06 23:04:48] operator / voice_transcript_partial / voice: hey disable the
  meta: kind=partial | timestamp=1778079888.0319643 | source=vosk | frequency_hz=368.0 | rms=312 | updated_at=1778079880.3881934
- [2026-05-06 23:04:48] operator / voice_transcript_partial / voice: hey disable the off
  meta: kind=partial | timestamp=1778079888.0595071 | source=vosk | frequency_hz=368.0 | rms=312 | updated_at=1778079880.3881934
- [2026-05-06 23:04:48] operator / voice_transcript_partial / voice: hey disable servo motion
  meta: kind=partial | timestamp=1778079888.076034 | source=vosk | frequency_hz=368.0 | rms=312 | updated_at=1778079880.3881934
- [2026-05-06 23:04:49] operator / voice_transcript_partial / voice: hey disable servo motion pir scan
  meta: kind=partial | timestamp=1778079889.0687928 | source=vosk | frequency_hz=110.0 | rms=1202 | updated_at=1778079888.5420868
- [2026-05-06 23:04:50] operator / voice_transcript_final / voice: hey disable servo motion pir scan
  meta: kind=final | timestamp=1778079890.4153209 | source=final | frequency_hz=110.0 | rms=1202 | updated_at=1778079888.5420868
- [2026-05-06 23:04:53] operator / voice_transcript_partial / voice: learning scoring
  meta: kind=partial | timestamp=1778079893.2987142 | source=vosk | frequency_hz=110.0 | rms=1202 | updated_at=1778079888.5420868
- [2026-05-06 23:04:53] operator / voice_transcript_partial / voice: learning is the
  meta: kind=partial | timestamp=1778079893.8608398 | source=vosk | frequency_hz=110.0 | rms=1202 | updated_at=1778079888.5420868
- [2026-05-06 23:04:54] operator / voice_transcript_partial / voice: learning is the the motion
  meta: kind=partial | timestamp=1778079894.0518122 | source=vosk | frequency_hz=110.0 | rms=1202 | updated_at=1778079888.5420868
- [2026-05-06 23:04:55] operator / voice_transcript_final / voice: learning is the the motion
  meta: kind=final | timestamp=1778079895.3780618 | source=final | frequency_hz=110.0 | rms=1202 | updated_at=1778079888.5420868
- [2026-05-06 23:05:06] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound output running
  meta: kind=partial | timestamp=1778079906.0899787 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:07] operator / voice_transcript_final / voice: acoustic guard detection on neutral sound of output running
  meta: kind=final | timestamp=1778079907.6792898 | source=final | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:08] operator / voice_transcript_partial / voice: known face
  meta: kind=partial | timestamp=1778079908.5654802 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:09] operator / voice_transcript_partial / voice: known face engagement zone
  meta: kind=partial | timestamp=1778079909.2766876 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:10] operator / voice_transcript_final / voice: face engagement
  meta: kind=final | timestamp=1778079910.1054802 | source=final | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:10] operator / voice_transcript_partial / voice: acoustic
  meta: kind=partial | timestamp=1778079910.3105764 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:10] operator / voice_transcript_partial / voice: acoustic guard
  meta: kind=partial | timestamp=1778079910.775622 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:11] operator / voice_transcript_partial / voice: acoustic guard detection
  meta: kind=partial | timestamp=1778079911.2797124 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:11] operator / voice_transcript_partial / voice: acoustic guard detection on
  meta: kind=partial | timestamp=1778079911.7761228 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:12] operator / voice_transcript_partial / voice: acoustic guard detection on mute
  meta: kind=partial | timestamp=1778079912.0435753 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:12] operator / voice_transcript_partial / voice: acoustic guard detection on visual
  meta: kind=partial | timestamp=1778079912.275577 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:12] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound cues
  meta: kind=partial | timestamp=1778079912.5263286 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:12] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound
  meta: kind=partial | timestamp=1778079912.79959 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:13] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound running
  meta: kind=partial | timestamp=1778079913.33265 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:13] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound
  meta: kind=partial | timestamp=1778079913.3389332 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:13] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound alerts
  meta: kind=partial | timestamp=1778079913.5606499 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:13] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound ml learning scoring
  meta: kind=partial | timestamp=1778079913.7985508 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:14] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound ml learning to
  meta: kind=partial | timestamp=1778079914.0270936 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:14] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound ml learning to a
  meta: kind=partial | timestamp=1778079914.7788265 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:15] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound ml learning to aim disabled
  meta: kind=partial | timestamp=1778079915.0260444 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:15] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound ml learning to a disable the motion
  meta: kind=partial | timestamp=1778079915.3372355 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:15] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound ml learning to a disable the off
  meta: kind=partial | timestamp=1778079915.5273004 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:15] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound ml learning to a disable servo face
  meta: kind=partial | timestamp=1778079915.7755616 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:16] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound ml learning to a disable servo face lion
  meta: kind=partial | timestamp=1778079916.0537765 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:16] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound ml learning to a disable servo face lion current
  meta: kind=partial | timestamp=1778079916.8029058 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:17] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound ml learning to a disable servo face lion current status
  meta: kind=partial | timestamp=1778079917.0419474 | source=vosk | frequency_hz=388.0 | rms=305 | updated_at=1778079906.076046
- [2026-05-06 23:05:18] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound ml learning to a disable servo face lion current status engaging
  meta: kind=partial | timestamp=1778079918.4159665 | source=vosk | frequency_hz=392.0 | rms=308 | updated_at=1778079918.374969
- [2026-05-06 23:05:18] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound ml learning to a disable servo face lion current status engaging scope
  meta: kind=partial | timestamp=1778079918.4580932 | source=vosk | frequency_hz=399.0 | rms=307 | updated_at=1778079918.416998
- [2026-05-06 23:05:20] operator / voice_transcript_final / voice: elion acoustic guard detection on visual sound ml learning to a disable servo face lion current status engaging
  meta: kind=final | timestamp=1778079920.9760067 | source=final | frequency_hz=372.4 | rms=315 | updated_at=1778079919.3744094
- [2026-05-06 23:05:22] operator / voice_command / voice: acoustic guard detection on visual sound ml learning to a disable servo face lion current status engaging
  meta: normalized=True
- [2026-05-06 23:05:22] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 23:05:21] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1778079921.3887546 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:22] operator / voice_transcript_partial / voice: of sound
  meta: kind=partial | timestamp=1778079922.3845923 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:22] operator / voice_transcript_partial / voice: event
  meta: kind=partial | timestamp=1778079922.887382 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:23] operator / voice_transcript_partial / voice: of threat
  meta: kind=partial | timestamp=1778079923.3358319 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:23] operator / voice_transcript_partial / voice: of precision
  meta: kind=partial | timestamp=1778079923.3864834 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:23] operator / voice_transcript_partial / voice: of threat scores
  meta: kind=partial | timestamp=1778079923.6397376 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:24] operator / voice_transcript_partial / voice: of threat fire
  meta: kind=partial | timestamp=1778079924.1458244 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:24] operator / voice_transcript_partial / voice: of threat fire disabled
  meta: kind=partial | timestamp=1778079924.657509 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:24] operator / voice_transcript_partial / voice: of threat fire disable the
  meta: kind=partial | timestamp=1778079924.8895557 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:25] operator / voice_transcript_partial / voice: of threat fire disable the on
  meta: kind=partial | timestamp=1778079925.13742 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:25] operator / voice_transcript_partial / voice: of threat fire disable the on commands
  meta: kind=partial | timestamp=1778079925.38686 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:25] operator / voice_transcript_partial / voice: of threat fire disable the on the movement
  meta: kind=partial | timestamp=1778079925.6386242 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:26] operator / voice_transcript_partial / voice: of threat fire disable the on the movement loop
  meta: kind=partial | timestamp=1778079926.161522 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:26] operator / voice_transcript_partial / voice: of threat fire disable the on the movement loop current
  meta: kind=partial | timestamp=1778079926.636581 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:26] operator / voice_transcript_partial / voice: of threat fire disable the on the movement loop current status
  meta: kind=partial | timestamp=1778079926.885711 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:27] operator / voice_transcript_partial / voice: of threat fire disable the on the movement loop current status engaging
  meta: kind=partial | timestamp=1778079927.6366162 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:27] operator / voice_transcript_partial / voice: of threat fire disable the on the movement loop current status engaging scope
  meta: kind=partial | timestamp=1778079927.8851137 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:28] operator / voice_transcript_final / voice: of threat fire disable the on the movement loop current status engaging
  meta: kind=final | timestamp=1778079928.7582963 | source=final | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:31] operator / voice_transcript_partial / voice: guard
  meta: kind=partial | timestamp=1778079931.9808912 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:32] operator / voice_transcript_partial / voice: guard detection
  meta: kind=partial | timestamp=1778079932.3633404 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:32] operator / voice_transcript_partial / voice: guard detection on
  meta: kind=partial | timestamp=1778079932.6105802 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:32] operator / voice_transcript_partial / voice: guard detection on mute
  meta: kind=partial | timestamp=1778079932.8830302 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:33] operator / voice_transcript_partial / voice: guard detection on visual overlay
  meta: kind=partial | timestamp=1778079933.1365936 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:34] operator / voice_transcript_partial / voice: guard detection on visual of ai
  meta: kind=partial | timestamp=1778079934.1785636 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:34] operator / voice_transcript_partial / voice: guard detection on visual of output
  meta: kind=partial | timestamp=1778079934.3618407 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:34] operator / voice_transcript_partial / voice: guard detection on visual of ai
  meta: kind=partial | timestamp=1778079934.6112785 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:35] operator / voice_transcript_final / voice: guard detection on visual of ai running
  meta: kind=final | timestamp=1778079935.4185803 | source=final | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:35] operator / voice_transcript_partial / voice: assistant
  meta: kind=partial | timestamp=1778079935.5771513 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:36] operator / voice_transcript_partial / voice: suggestions
  meta: kind=partial | timestamp=1778079936.0694952 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:36] operator / voice_transcript_partial / voice: acoustic is
  meta: kind=partial | timestamp=1778079936.5239615 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:36] operator / voice_transcript_partial / voice: acoustic is lion
  meta: kind=partial | timestamp=1778079936.8159595 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:37] operator / voice_transcript_partial / voice: is the current
  meta: kind=partial | timestamp=1778079937.5497227 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:37] operator / voice_transcript_partial / voice: is the current cleanup
  meta: kind=partial | timestamp=1778079937.7986624 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:38] operator / voice_transcript_partial / voice: is the current hey
  meta: kind=partial | timestamp=1778079938.0739875 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:38] operator / voice_transcript_partial / voice: is the current hey engaging scope
  meta: kind=partial | timestamp=1778079938.574786 | source=vosk | frequency_hz=420.0 | rms=301 | updated_at=1778079921.1295757
- [2026-05-06 23:05:48] operator / voice_transcript_partial / voice: acoustic guard detection on visual ml hey the
  meta: kind=partial | timestamp=1778079948.5766397 | source=vosk | frequency_hz=302.5 | rms=1065 | updated_at=1778079940.8692894
- [2026-05-06 23:05:48] operator / voice_transcript_partial / voice: acoustic guard detection on visual ml hey leon
  meta: kind=partial | timestamp=1778079948.63096 | source=vosk | frequency_hz=302.5 | rms=1065 | updated_at=1778079940.8692894
- [2026-05-06 23:05:48] operator / voice_transcript_partial / voice: acoustic guard detection on visual ml hey leon disable
  meta: kind=partial | timestamp=1778079948.864838 | source=vosk | frequency_hz=302.5 | rms=1065 | updated_at=1778079940.8692894
- [2026-05-06 23:05:49] operator / voice_transcript_partial / voice: acoustic guard detection on visual ml hey leon disable ml
  meta: kind=partial | timestamp=1778079949.7384255 | source=vosk | frequency_hz=302.5 | rms=1065 | updated_at=1778079940.8692894
- [2026-05-06 23:05:49] operator / voice_transcript_partial / voice: acoustic guard detection on visual ml hey leon disable enable assistant
  meta: kind=partial | timestamp=1778079949.771464 | source=vosk | frequency_hz=302.5 | rms=1065 | updated_at=1778079940.8692894
- [2026-05-06 23:05:51] operator / voice_transcript_partial / voice: pir led
  meta: kind=partial | timestamp=1778079951.0046113 | source=vosk | frequency_hz=302.5 | rms=1065 | updated_at=1778079940.8692894
- [2026-05-06 23:05:51] operator / voice_transcript_partial / voice: pir
  meta: kind=partial | timestamp=1778079951.2844021 | source=vosk | frequency_hz=284.0 | rms=485 | updated_at=1778079951.2256737
- [2026-05-06 23:05:51] operator / voice_transcript_partial / voice: pir logging
  meta: kind=partial | timestamp=1778079951.4865053 | source=vosk | frequency_hz=284.0 | rms=485 | updated_at=1778079951.2256737
- [2026-05-06 23:05:52] operator / voice_transcript_final / voice: pir logging
  meta: kind=final | timestamp=1778079952.092882 | source=final | frequency_hz=284.0 | rms=485 | updated_at=1778079951.2256737
- [2026-05-06 23:05:52] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1778079952.2483685 | source=vosk | frequency_hz=284.0 | rms=485 | updated_at=1778079951.2256737
- [2026-05-06 23:05:53] operator / voice_transcript_partial / voice: for
  meta: kind=partial | timestamp=1778079953.7433927 | source=vosk | frequency_hz=284.0 | rms=485 | updated_at=1778079951.2256737
- [2026-05-06 23:05:54] operator / voice_transcript_partial / voice: for shortcuts
  meta: kind=partial | timestamp=1778079954.022497 | source=vosk | frequency_hz=284.0 | rms=485 | updated_at=1778079951.2256737
- [2026-05-06 23:05:54] operator / voice_transcript_partial / voice: for zone masks
  meta: kind=partial | timestamp=1778079954.245821 | source=vosk | frequency_hz=284.0 | rms=485 | updated_at=1778079951.2256737
- [2026-05-06 23:05:54] operator / voice_transcript_partial / voice: loss order
  meta: kind=partial | timestamp=1778079954.4802854 | source=vosk | frequency_hz=284.0 | rms=485 | updated_at=1778079951.2256737
- [2026-05-06 23:05:54] operator / voice_transcript_partial / voice: fire for human voice
  meta: kind=partial | timestamp=1778079954.7310958 | source=vosk | frequency_hz=376.0 | rms=309 | updated_at=1778079954.7234979
- [2026-05-06 23:05:55] operator / voice_transcript_partial / voice: loss order local actions
  meta: kind=partial | timestamp=1778079955.0002089 | source=vosk | frequency_hz=381.6 | rms=306 | updated_at=1778079954.9907122
- [2026-05-06 23:05:55] operator / voice_transcript_final / voice: loss order local
  meta: kind=final | timestamp=1778079955.724804 | source=final | frequency_hz=382.2 | rms=318 | updated_at=1778079955.4743843
- [2026-05-06 23:05:57] operator / voice_transcript_partial / voice: report elian
  meta: kind=partial | timestamp=1778079957.7346547 | source=vosk | frequency_hz=379.8 | rms=320 | updated_at=1778079955.978893
- [2026-05-06 23:05:57] operator / voice_transcript_partial / voice: reporting enabled
  meta: kind=partial | timestamp=1778079957.9802308 | source=vosk | frequency_hz=379.8 | rms=320 | updated_at=1778079955.978893
- [2026-05-06 23:05:58] operator / voice_transcript_final / voice: reporting enable on
  meta: kind=final | timestamp=1778079958.3298404 | source=final | frequency_hz=379.8 | rms=320 | updated_at=1778079955.978893
- [2026-05-06 23:05:58] operator / voice_transcript_partial / voice: leon
  meta: kind=partial | timestamp=1778079958.4944048 | source=vosk | frequency_hz=379.8 | rms=320 | updated_at=1778079955.978893
- [2026-05-06 23:05:59] operator / voice_transcript_partial / voice: leon what on
  meta: kind=partial | timestamp=1778079959.2391145 | source=vosk | frequency_hz=379.8 | rms=320 | updated_at=1778079955.978893
- [2026-05-06 23:05:59] operator / voice_transcript_partial / voice: leon what on current
  meta: kind=partial | timestamp=1778079959.4790702 | source=vosk | frequency_hz=379.8 | rms=320 | updated_at=1778079955.978893
- [2026-05-06 23:05:59] operator / voice_transcript_partial / voice: leon what's pir name
  meta: kind=partial | timestamp=1778079959.729449 | source=vosk | frequency_hz=379.8 | rms=320 | updated_at=1778079955.978893
- [2026-05-06 23:06:01] operator / voice_transcript_final / voice: elion what s pir name
  meta: kind=final | timestamp=1778079961.781538 | source=final | frequency_hz=245.9 | rms=532 | updated_at=1778079960.8391027
- [2026-05-06 23:06:04] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778079964.1072435 | source=vosk | frequency_hz=304.1 | rms=317 | updated_at=1778079963.0990474
- [2026-05-06 23:06:04] operator / voice_transcript_partial / voice: running
  meta: kind=partial | timestamp=1778079964.3373332 | source=vosk | frequency_hz=304.1 | rms=317 | updated_at=1778079963.0990474
- [2026-05-06 23:06:04] operator / voice_transcript_partial / voice: running on
  meta: kind=partial | timestamp=1778079964.629016 | source=vosk | frequency_hz=304.1 | rms=317 | updated_at=1778079963.0990474
- [2026-05-06 23:06:05] operator / voice_transcript_partial / voice: running on loss
  meta: kind=partial | timestamp=1778079965.6093395 | source=vosk | frequency_hz=304.1 | rms=317 | updated_at=1778079963.0990474
- [2026-05-06 23:06:05] operator / voice_transcript_partial / voice: running on manual
  meta: kind=partial | timestamp=1778079965.8591564 | source=vosk | frequency_hz=304.1 | rms=317 | updated_at=1778079963.0990474
- [2026-05-06 23:06:06] operator / voice_transcript_partial / voice: running on learning scoring
  meta: kind=partial | timestamp=1778079966.09307 | source=vosk | frequency_hz=328.0 | rms=308 | updated_at=1778079966.0860627
- [2026-05-06 23:06:06] operator / voice_transcript_final / voice: running on running
  meta: kind=final | timestamp=1778079966.7257981 | source=final | frequency_hz=348.9 | rms=312 | updated_at=1778079966.593479
- [2026-05-06 23:06:16] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778079976.617339 | source=vosk | frequency_hz=341.7 | rms=303 | updated_at=1778079975.5835922
- [2026-05-06 23:06:16] operator / voice_transcript_partial / voice: camera
  meta: kind=partial | timestamp=1778079976.8428323 | source=vosk | frequency_hz=341.7 | rms=303 | updated_at=1778079975.5835922
- [2026-05-06 23:06:17] operator / voice_transcript_partial / voice: camera current
  meta: kind=partial | timestamp=1778079977.1194956 | source=vosk | frequency_hz=341.7 | rms=303 | updated_at=1778079975.5835922
- [2026-05-06 23:06:17] operator / voice_transcript_partial / voice: camera
  meta: kind=partial | timestamp=1778079977.3374052 | source=vosk | frequency_hz=341.7 | rms=303 | updated_at=1778079975.5835922
- [2026-05-06 23:06:17] operator / voice_transcript_partial / voice: camera view
  meta: kind=partial | timestamp=1778079977.6367543 | source=vosk | frequency_hz=341.7 | rms=303 | updated_at=1778079975.5835922
- [2026-05-06 23:06:19] operator / voice_transcript_final / voice: camera view
  meta: kind=final | timestamp=1778079979.0053818 | source=final | frequency_hz=192.0 | rms=501 | updated_at=1778079978.835975
- [2026-05-06 23:06:20] operator / voice_transcript_partial / voice: acoustic
  meta: kind=partial | timestamp=1778079980.8549612 | source=vosk | frequency_hz=234.2 | rms=324 | updated_at=1778079980.0910165
- [2026-05-06 23:06:21] operator / voice_transcript_partial / voice: acoustic guard
  meta: kind=partial | timestamp=1778079981.081986 | source=vosk | frequency_hz=234.2 | rms=324 | updated_at=1778079980.0910165
- [2026-05-06 23:06:21] operator / voice_transcript_partial / voice: acoustic guard active
  meta: kind=partial | timestamp=1778079981.85017 | source=vosk | frequency_hz=234.2 | rms=324 | updated_at=1778079980.0910165
- [2026-05-06 23:06:22] operator / voice_transcript_partial / voice: acoustic guard on mute
  meta: kind=partial | timestamp=1778079982.1642356 | source=vosk | frequency_hz=234.2 | rms=324 | updated_at=1778079980.0910165
- [2026-05-06 23:06:22] operator / voice_transcript_partial / voice: acoustic guard on use motion
  meta: kind=partial | timestamp=1778079982.607172 | source=vosk | frequency_hz=234.2 | rms=324 | updated_at=1778079980.0910165
- [2026-05-06 23:06:22] operator / voice_transcript_partial / voice: acoustic guard on use russian dmitry
  meta: kind=partial | timestamp=1778079982.8568494 | source=vosk | frequency_hz=234.2 | rms=324 | updated_at=1778079980.0910165
- [2026-05-06 23:06:23] operator / voice_transcript_partial / voice: acoustic guard on use motion
  meta: kind=partial | timestamp=1778079983.335416 | source=vosk | frequency_hz=234.2 | rms=324 | updated_at=1778079980.0910165
- [2026-05-06 23:06:23] operator / voice_transcript_partial / voice: acoustic guard on use motion of output
  meta: kind=partial | timestamp=1778079983.6079102 | source=vosk | frequency_hz=234.2 | rms=324 | updated_at=1778079980.0910165
- [2026-05-06 23:06:23] operator / voice_transcript_partial / voice: acoustic guard on use motion ml
  meta: kind=partial | timestamp=1778079983.8325527 | source=vosk | frequency_hz=234.2 | rms=324 | updated_at=1778079980.0910165
- [2026-05-06 23:06:24] operator / voice_transcript_partial / voice: acoustic guard on use motion of output window
  meta: kind=partial | timestamp=1778079984.082161 | source=vosk | frequency_hz=234.2 | rms=324 | updated_at=1778079980.0910165
- [2026-05-06 23:06:24] operator / voice_transcript_partial / voice: acoustic guard on use motion of output window shortcuts
  meta: kind=partial | timestamp=1778079984.4449456 | source=vosk | frequency_hz=234.2 | rms=324 | updated_at=1778079980.0910165
- [2026-05-06 23:06:24] operator / voice_transcript_partial / voice: acoustic guard on use motion ml training
  meta: kind=partial | timestamp=1778079984.8520534 | source=vosk | frequency_hz=234.2 | rms=324 | updated_at=1778079980.0910165
- [2026-05-06 23:06:25] operator / voice_transcript_partial / voice: acoustic guard on use motion of output window setting drafts
  meta: kind=partial | timestamp=1778079985.1046064 | source=vosk | frequency_hz=234.2 | rms=324 | updated_at=1778079980.0910165
- [2026-05-06 23:06:25] operator / voice_transcript_partial / voice: acoustic guard on use motion ml training disabled
  meta: kind=partial | timestamp=1778079985.346116 | source=vosk | frequency_hz=234.2 | rms=324 | updated_at=1778079980.0910165
- [2026-05-06 23:06:25] operator / voice_transcript_partial / voice: acoustic guard on use motion ml training disable the buzzer
  meta: kind=partial | timestamp=1778079985.6081328 | source=vosk | frequency_hz=234.2 | rms=324 | updated_at=1778079980.0910165
- [2026-05-06 23:06:25] operator / voice_transcript_partial / voice: acoustic guard on use motion ml training disable servo
  meta: kind=partial | timestamp=1778079985.844755 | source=vosk | frequency_hz=234.2 | rms=324 | updated_at=1778079980.0910165
- [2026-05-06 23:06:26] operator / voice_transcript_partial / voice: acoustic guard on use motion ml training disable the known faces
  meta: kind=partial | timestamp=1778079986.0896199 | source=vosk | frequency_hz=234.2 | rms=324 | updated_at=1778079980.0910165
- [2026-05-06 23:06:26] operator / voice_transcript_partial / voice: acoustic guard on use motion ml training disable servo motion
  meta: kind=partial | timestamp=1778079986.3909204 | source=vosk | frequency_hz=374.0 | rms=310 | updated_at=1778079986.3314793
- [2026-05-06 23:06:27] operator / voice_transcript_final / voice: acoustic guard on use motion ml training disable the face
  meta: kind=final | timestamp=1778079987.2400541 | source=final | frequency_hz=374.0 | rms=310 | updated_at=1778079986.3314793
- [2026-05-06 23:06:27] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778079987.3514082 | source=vosk | frequency_hz=374.0 | rms=310 | updated_at=1778079986.3314793
- [2026-05-06 23:06:27] operator / voice_transcript_partial / voice: current status
  meta: kind=partial | timestamp=1778079987.3764398 | source=vosk | frequency_hz=374.0 | rms=310 | updated_at=1778079986.3314793
- [2026-05-06 23:06:28] operator / voice_transcript_final / voice: current status
  meta: kind=final | timestamp=1778079988.6477802 | source=final | frequency_hz=374.0 | rms=310 | updated_at=1778079986.3314793
- [2026-05-06 23:06:39] operator / voice_transcript_partial / voice: acoustic
  meta: kind=partial | timestamp=1778079999.1806126 | source=vosk | frequency_hz=190.0 | rms=817 | updated_at=1778079996.4016194
- [2026-05-06 23:06:53] operator / voice_transcript_partial / voice: known
  meta: kind=partial | timestamp=1778080013.9112573 | source=vosk | frequency_hz=364.3 | rms=305 | updated_at=1778080012.1644845
- [2026-05-06 23:06:54] operator / voice_transcript_partial / voice: name is
  meta: kind=partial | timestamp=1778080014.1627457 | source=vosk | frequency_hz=364.3 | rms=305 | updated_at=1778080012.1644845
- [2026-05-06 23:06:54] operator / voice_transcript_partial / voice: name is the
  meta: kind=partial | timestamp=1778080014.4381738 | source=vosk | frequency_hz=364.3 | rms=305 | updated_at=1778080012.1644845
- [2026-05-06 23:06:55] operator / voice_transcript_final / voice: name is the
  meta: kind=final | timestamp=1778080015.300677 | source=final | frequency_hz=408.0 | rms=296 | updated_at=1778080015.1547444
- [2026-05-06 23:06:57] operator / voice_transcript_partial / voice: to rest
  meta: kind=partial | timestamp=1778080017.1593623 | source=vosk | frequency_hz=408.4 | rms=302 | updated_at=1778080016.1970978
- [2026-05-06 23:06:57] operator / voice_transcript_partial / voice: running
  meta: kind=partial | timestamp=1778080017.4077132 | source=vosk | frequency_hz=408.4 | rms=302 | updated_at=1778080016.1970978
- [2026-05-06 23:06:58] operator / voice_transcript_final / voice: running
  meta: kind=final | timestamp=1778080018.043734 | source=final | frequency_hz=372.0 | rms=305 | updated_at=1778080017.9024704
- [2026-05-06 23:06:59] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778080019.40901 | source=vosk | frequency_hz=371.1 | rms=302 | updated_at=1778080018.9224997
- [2026-05-06 23:06:59] operator / voice_transcript_partial / voice: the loop
  meta: kind=partial | timestamp=1778080019.6738665 | source=vosk | frequency_hz=371.1 | rms=302 | updated_at=1778080018.9224997
- [2026-05-06 23:06:59] operator / voice_transcript_partial / voice: the movement
  meta: kind=partial | timestamp=1778080019.910866 | source=vosk | frequency_hz=371.1 | rms=302 | updated_at=1778080018.9224997
- [2026-05-06 23:07:00] operator / voice_transcript_partial / voice: the loop
  meta: kind=partial | timestamp=1778080020.170696 | source=vosk | frequency_hz=371.1 | rms=302 | updated_at=1778080018.9224997
- [2026-05-06 23:07:00] operator / voice_transcript_final / voice: the loop
  meta: kind=final | timestamp=1778080020.7384403 | source=final | frequency_hz=356.0 | rms=316 | updated_at=1778080020.413908
- [2026-05-06 23:07:01] operator / voice_transcript_partial / voice: greeting
  meta: kind=partial | timestamp=1778080021.1765947 | source=vosk | frequency_hz=356.0 | rms=316 | updated_at=1778080020.413908
- [2026-05-06 23:07:01] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778080021.4168885 | source=vosk | frequency_hz=374.2 | rms=301 | updated_at=1778080021.4108872
- [2026-05-06 23:07:03] operator / voice_transcript_partial / voice: report
  meta: kind=partial | timestamp=1778080023.9195194 | source=vosk | frequency_hz=379.2 | rms=361 | updated_at=1778080023.9079075
- [2026-05-06 23:07:04] operator / voice_transcript_final / voice: reports
  meta: kind=final | timestamp=1778080024.5450435 | source=final | frequency_hz=378.6 | rms=318 | updated_at=1778080024.4250348
- [2026-05-06 23:07:05] operator / voice_transcript_partial / voice: human voice
  meta: kind=partial | timestamp=1778080025.1765845 | source=vosk | frequency_hz=378.6 | rms=318 | updated_at=1778080024.4250348
- [2026-05-06 23:07:06] operator / voice_transcript_final / voice: human
  meta: kind=final | timestamp=1778080026.5071955 | source=final | frequency_hz=374.9 | rms=886 | updated_at=1778080026.4028068
- [2026-05-06 23:07:21] operator / voice_transcript_partial / voice: shortcuts
  meta: kind=partial | timestamp=1778080041.262908 | source=vosk | frequency_hz=350.7 | rms=308 | updated_at=1778080037.507474
- [2026-05-06 23:07:21] operator / voice_transcript_partial / voice: summaries
  meta: kind=partial | timestamp=1778080041.4951398 | source=vosk | frequency_hz=350.7 | rms=308 | updated_at=1778080037.507474
- [2026-05-06 23:07:21] operator / voice_transcript_partial / voice: show
  meta: kind=partial | timestamp=1778080041.7518814 | source=vosk | frequency_hz=350.7 | rms=308 | updated_at=1778080037.507474
- [2026-05-06 23:07:22] operator / voice_transcript_partial / voice: show movement
  meta: kind=partial | timestamp=1778080042.0172076 | source=vosk | frequency_hz=350.7 | rms=308 | updated_at=1778080037.507474
- [2026-05-06 23:07:22] operator / voice_transcript_final / voice: summaries
  meta: kind=final | timestamp=1778080042.3800402 | source=final | frequency_hz=350.7 | rms=308 | updated_at=1778080037.507474
- [2026-05-06 23:07:40] operator / voice_transcript_partial / voice: acoustic guard detection on mute buzzer for
  meta: kind=partial | timestamp=1778080060.3424973 | source=vosk | frequency_hz=126.0 | rms=211 | updated_at=1778080058.8047705
- [2026-05-06 23:07:40] operator / voice_transcript_partial / voice: acoustic guard detection on mute buzzer for cue
  meta: kind=partial | timestamp=1778080060.9800029 | source=vosk | frequency_hz=126.0 | rms=211 | updated_at=1778080058.8047705
- [2026-05-06 23:07:41] operator / voice_transcript_partial / voice: acoustic guard detection on mute buzzer for cue disabled
  meta: kind=partial | timestamp=1778080061.0580046 | source=vosk | frequency_hz=126.0 | rms=211 | updated_at=1778080058.8047705
- [2026-05-06 23:07:41] operator / voice_transcript_partial / voice: acoustic guard detection on mute buzzer for cue disable disabled
  meta: kind=partial | timestamp=1778080061.3187582 | source=vosk | frequency_hz=126.0 | rms=211 | updated_at=1778080058.8047705
- [2026-05-06 23:07:41] operator / voice_transcript_partial / voice: acoustic guard detection on mute buzzer for cue disable disable
  meta: kind=partial | timestamp=1778080061.589054 | source=vosk | frequency_hz=126.0 | rms=211 | updated_at=1778080058.8047705
- [2026-05-06 23:07:42] operator / voice_transcript_final / voice: acoustic guard detection on e visual ml for cue disable disable
  meta: kind=final | timestamp=1778080062.2159088 | source=final | frequency_hz=126.0 | rms=211 | updated_at=1778080058.8047705
- [2026-05-06 23:07:42] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778080062.8029432 | source=vosk | frequency_hz=126.0 | rms=211 | updated_at=1778080058.8047705
- [2026-05-06 23:07:43] operator / voice_transcript_partial / voice: current status
  meta: kind=partial | timestamp=1778080063.1511097 | source=vosk | frequency_hz=126.0 | rms=211 | updated_at=1778080058.8047705
- [2026-05-06 23:07:43] operator / voice_transcript_partial / voice: current hey
  meta: kind=partial | timestamp=1778080063.323958 | source=vosk | frequency_hz=126.0 | rms=211 | updated_at=1778080058.8047705
- [2026-05-06 23:07:43] operator / voice_transcript_partial / voice: current hey guarding mode
  meta: kind=partial | timestamp=1778080063.5651245 | source=vosk | frequency_hz=334.0 | rms=318 | updated_at=1778080063.5585084
- [2026-05-06 23:07:44] operator / voice_transcript_final / voice: current hey guarding
  meta: kind=final | timestamp=1778080064.7349732 | source=final | frequency_hz=347.2 | rms=306 | updated_at=1778080064.5611439
- [2026-05-06 23:08:00] operator / voice_transcript_partial / voice: repeat
  meta: kind=partial | timestamp=1778080080.458918 | source=vosk | frequency_hz=412.0 | rms=367 | updated_at=1778080080.4454026
- [2026-05-06 23:08:01] operator / voice_transcript_final / voice: reporting
  meta: kind=final | timestamp=1778080081.3063743 | source=final | frequency_hz=389.6 | rms=305 | updated_at=1778080081.1998732
- [2026-05-06 23:08:16] operator / voice_transcript_partial / voice: acoustic guard detection id on the visual sound of output
  meta: kind=partial | timestamp=1778080096.0553606 | source=vosk | frequency_hz=381.3 | rms=315 | updated_at=1778080092.0406475
- [2026-05-06 23:08:16] operator / voice_transcript_partial / voice: acoustic guard detection id on the visual sound of output running
  meta: kind=partial | timestamp=1778080096.2862709 | source=vosk | frequency_hz=381.3 | rms=315 | updated_at=1778080092.0406475
- [2026-05-06 23:08:16] operator / voice_transcript_partial / voice: acoustic guard detection id on the visual sound of output running a
  meta: kind=partial | timestamp=1778080096.8168516 | source=vosk | frequency_hz=381.3 | rms=315 | updated_at=1778080092.0406475
- [2026-05-06 23:08:17] operator / voice_transcript_partial / voice: acoustic guard detection id on the visual sound of output running a disable the
  meta: kind=partial | timestamp=1778080097.3550453 | source=vosk | frequency_hz=381.3 | rms=315 | updated_at=1778080092.0406475
- [2026-05-06 23:08:17] operator / voice_transcript_partial / voice: acoustic guard detection id on the visual sound of output running a disable servo face
  meta: kind=partial | timestamp=1778080097.5632753 | source=vosk | frequency_hz=381.3 | rms=315 | updated_at=1778080092.0406475
- [2026-05-06 23:08:18] operator / voice_transcript_partial / voice: acoustic guard detection id on the visual sound of output running a disable servo face lion
  meta: kind=partial | timestamp=1778080098.0347073 | source=vosk | frequency_hz=400.0 | rms=315 | updated_at=1778080098.029204
- [2026-05-06 23:08:18] operator / voice_transcript_partial / voice: acoustic guard detection id on the visual sound of output running a disable servo face lion current
  meta: kind=partial | timestamp=1778080098.8214748 | source=vosk | frequency_hz=391.6 | rms=323 | updated_at=1778080098.2792068
- [2026-05-06 23:08:19] operator / voice_transcript_partial / voice: acoustic guard detection id on the visual sound of output running a disable servo face lion current status
  meta: kind=partial | timestamp=1778080099.0564694 | source=vosk | frequency_hz=391.6 | rms=323 | updated_at=1778080098.2792068
- [2026-05-06 23:08:20] operator / voice_transcript_partial / voice: acoustic guard detection id on the visual sound of output running a disable servo face lion current status engaging scope
  meta: kind=partial | timestamp=1778080100.0731263 | source=vosk | frequency_hz=391.6 | rms=323 | updated_at=1778080098.2792068
- [2026-05-06 23:08:21] operator / voice_transcript_final / voice: elion acoustic guard detection id on the visual sound of output running a disable servo face lion current status engaging
  meta: kind=final | timestamp=1778080101.9478505 | source=final | frequency_hz=352.0 | rms=304 | updated_at=1778080100.5401769
- [2026-05-06 23:08:22] operator / voice_command / voice: acoustic guard detection id on the visual sound of output running a disable servo face lion current status engaging
  meta: normalized=True
- [2026-05-06 23:08:23] assistant / spoken_confirmation / voice: I can keep going with voice change. Tell me a voice family like Russian or Indian, ask what are the options, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 23:08:23] operator / voice_transcript_partial / voice: detection
  meta: kind=partial | timestamp=1778080103.238198 | source=vosk | frequency_hz=382.0 | rms=311 | updated_at=1778080102.2093372
- [2026-05-06 23:08:23] operator / voice_transcript_partial / voice: detection on
  meta: kind=partial | timestamp=1778080103.7349434 | source=vosk | frequency_hz=382.0 | rms=311 | updated_at=1778080102.2093372
- [2026-05-06 23:08:24] operator / voice_transcript_partial / voice: detection on neutral
  meta: kind=partial | timestamp=1778080104.2640398 | source=vosk | frequency_hz=382.0 | rms=311 | updated_at=1778080102.2093372
- [2026-05-06 23:08:24] operator / voice_transcript_partial / voice: detection on neutral status
  meta: kind=partial | timestamp=1778080104.4751914 | source=vosk | frequency_hz=382.0 | rms=311 | updated_at=1778080102.2093372
- [2026-05-06 23:08:25] operator / voice_transcript_partial / voice: detection on neutral status of ai
  meta: kind=partial | timestamp=1778080105.0066264 | source=vosk | frequency_hz=382.0 | rms=311 | updated_at=1778080102.2093372
- [2026-05-06 23:08:25] operator / voice_transcript_partial / voice: detection on neutral status of accessory
  meta: kind=partial | timestamp=1778080105.2648227 | source=vosk | frequency_hz=382.0 | rms=311 | updated_at=1778080102.2093372
- [2026-05-06 23:08:25] operator / voice_transcript_partial / voice: detection on neutral status of
  meta: kind=partial | timestamp=1778080105.5125663 | source=vosk | frequency_hz=382.0 | rms=311 | updated_at=1778080102.2093372
- [2026-05-06 23:08:26] operator / voice_transcript_final / voice: detection id on neutral status of
  meta: kind=final | timestamp=1778080106.5607967 | source=final | frequency_hz=382.0 | rms=311 | updated_at=1778080102.2093372
- [2026-05-06 23:08:28] operator / voice_transcript_partial / voice: greeting gesture
  meta: kind=partial | timestamp=1778080108.30597 | source=vosk | frequency_hz=382.0 | rms=311 | updated_at=1778080102.2093372
- [2026-05-06 23:08:28] operator / voice_transcript_partial / voice: greeting
  meta: kind=partial | timestamp=1778080108.5443275 | source=vosk | frequency_hz=382.0 | rms=311 | updated_at=1778080102.2093372
- [2026-05-06 23:08:28] operator / voice_transcript_partial / voice: greeting status
  meta: kind=partial | timestamp=1778080108.9740915 | source=vosk | frequency_hz=382.0 | rms=311 | updated_at=1778080102.2093372
- [2026-05-06 23:08:29] operator / voice_transcript_partial / voice: feed off the
  meta: kind=partial | timestamp=1778080109.3159554 | source=vosk | frequency_hz=382.0 | rms=311 | updated_at=1778080102.2093372
- [2026-05-06 23:08:29] operator / voice_transcript_partial / voice: feed off the engaging
  meta: kind=partial | timestamp=1778080109.5480013 | source=vosk | frequency_hz=382.0 | rms=311 | updated_at=1778080102.2093372
- [2026-05-06 23:08:29] operator / voice_transcript_partial / voice: feed off the engaging scope
  meta: kind=partial | timestamp=1778080109.8028014 | source=vosk | frequency_hz=382.0 | rms=311 | updated_at=1778080102.2093372
- [2026-05-06 23:08:30] operator / voice_transcript_final / voice: feed off status
  meta: kind=final | timestamp=1778080110.5069027 | source=final | frequency_hz=382.0 | rms=311 | updated_at=1778080102.2093372
- [2026-05-06 23:08:41] operator / voice_transcript_partial / voice: acoustic guard tab the visual ml training
  meta: kind=partial | timestamp=1778080121.298155 | source=vosk | frequency_hz=220.0 | rms=342 | updated_at=1778080119.7954547
- [2026-05-06 23:08:41] operator / voice_transcript_final / voice: acoustic guard tab the visual output
  meta: kind=final | timestamp=1778080121.9483297 | source=final | frequency_hz=220.0 | rms=342 | updated_at=1778080119.7954547
- [2026-05-06 23:08:42] operator / voice_transcript_partial / voice: hey
  meta: kind=partial | timestamp=1778080122.0694842 | source=vosk | frequency_hz=220.0 | rms=342 | updated_at=1778080119.7954547
- [2026-05-06 23:08:42] operator / voice_transcript_partial / voice: hey disable
  meta: kind=partial | timestamp=1778080122.2951367 | source=vosk | frequency_hz=220.0 | rms=342 | updated_at=1778080119.7954547
- [2026-05-06 23:08:42] operator / voice_transcript_partial / voice: hey disable acoustic
  meta: kind=partial | timestamp=1778080122.8151698 | source=vosk | frequency_hz=220.0 | rms=342 | updated_at=1778080119.7954547
- [2026-05-06 23:08:43] operator / voice_transcript_partial / voice: hey disable assistant recent
  meta: kind=partial | timestamp=1778080123.0713298 | source=vosk | frequency_hz=220.0 | rms=342 | updated_at=1778080119.7954547
- [2026-05-06 23:08:43] operator / voice_transcript_partial / voice: hey disable servo face lion
  meta: kind=partial | timestamp=1778080123.327078 | source=vosk | frequency_hz=220.0 | rms=342 | updated_at=1778080119.7954547
- [2026-05-06 23:08:43] operator / voice_transcript_final / voice: hey disable servo trace on
  meta: kind=final | timestamp=1778080123.7715166 | source=final | frequency_hz=220.0 | rms=342 | updated_at=1778080119.7954547
- [2026-05-06 23:08:44] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778080124.1212573 | source=vosk | frequency_hz=220.0 | rms=342 | updated_at=1778080119.7954547
- [2026-05-06 23:08:44] operator / voice_transcript_partial / voice: current status
  meta: kind=partial | timestamp=1778080124.3281662 | source=vosk | frequency_hz=220.0 | rms=342 | updated_at=1778080119.7954547
- [2026-05-06 23:08:44] operator / voice_transcript_partial / voice: current feed
  meta: kind=partial | timestamp=1778080124.7976205 | source=vosk | frequency_hz=220.0 | rms=342 | updated_at=1778080119.7954547
- [2026-05-06 23:08:45] operator / voice_transcript_final / voice: current feed
  meta: kind=final | timestamp=1778080125.2349262 | source=final | frequency_hz=220.0 | rms=342 | updated_at=1778080119.7954547
- [2026-05-06 23:09:11] operator / voice_transcript_partial / voice: tuning
  meta: kind=partial | timestamp=1778080151.5795445 | source=vosk | frequency_hz=357.8 | rms=325 | updated_at=1778080150.0493681
- [2026-05-06 23:09:12] operator / voice_transcript_final / voice: tuning
  meta: kind=final | timestamp=1778080152.9036946 | source=final | frequency_hz=383.1 | rms=552 | updated_at=1778080152.3238175
- [2026-05-06 23:09:16] operator / voice_transcript_partial / voice: need
  meta: kind=partial | timestamp=1778080156.5880597 | source=vosk | frequency_hz=376.1 | rms=310 | updated_at=1778080153.5530324
- [2026-05-06 23:09:16] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1778080156.842969 | source=vosk | frequency_hz=376.1 | rms=310 | updated_at=1778080153.5530324
- [2026-05-06 23:09:17] operator / voice_transcript_final / voice: me
  meta: kind=final | timestamp=1778080157.452468 | source=final | frequency_hz=376.1 | rms=310 | updated_at=1778080153.5530324
- [2026-05-06 23:09:47] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound for a deactivate
  meta: kind=partial | timestamp=1778080187.2727268 | source=vosk | frequency_hz=349.8 | rms=306 | updated_at=1778080186.5037463
- [2026-05-06 23:09:47] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound for a diagnostics
  meta: kind=partial | timestamp=1778080187.4767869 | source=vosk | frequency_hz=349.8 | rms=306 | updated_at=1778080186.5037463
- [2026-05-06 23:09:47] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound for a deactivate
  meta: kind=partial | timestamp=1778080187.742693 | source=vosk | frequency_hz=349.8 | rms=306 | updated_at=1778080186.5037463
- [2026-05-06 23:09:48] operator / voice_transcript_partial / voice: acoustic guard detection on visual sound for a disable face
  meta: kind=partial | timestamp=1778080188.0299091 | source=vosk | frequency_hz=349.8 | rms=306 | updated_at=1778080186.5037463
- [2026-05-06 23:09:49] operator / voice_transcript_final / voice: acoustic guard detection on visual sound for a disable face
  meta: kind=final | timestamp=1778080189.2537634 | source=final | frequency_hz=349.8 | rms=306 | updated_at=1778080186.5037463
- [2026-05-06 23:09:49] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778080189.312791 | source=vosk | frequency_hz=349.8 | rms=306 | updated_at=1778080186.5037463
- [2026-05-06 23:09:49] assistant / spoken_reply / voice: Smart Sentry is engaging person target 71 in precision phase. Visible detections include 2 people. 2 people in view are not matched to known faces. The acoustic guard has also detected unusual sound recently. Latest AI note. Assistant is disabled. End of analysys report.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-06 23:09:49] operator / voice_transcript_partial / voice: current status
  meta: kind=partial | timestamp=1778080189.5059056 | source=vosk | frequency_hz=349.8 | rms=306 | updated_at=1778080186.5037463
- [2026-05-06 23:09:51] operator / voice_transcript_partial / voice: current status guarding mode
  meta: kind=partial | timestamp=1778080191.0666049 | source=vosk | frequency_hz=320.2 | rms=308 | updated_at=1778080190.9651284
- [2026-05-06 23:09:52] operator / voice_transcript_final / voice: current status guard
  meta: kind=final | timestamp=1778080192.1150734 | source=final | frequency_hz=310.3 | rms=824 | updated_at=1778080191.7171562
- [2026-05-06 23:09:55] assistant / spoken_reply / voice: Smart Sentry is engaging person target 71 in precision phase. Visible detections include 3 people. 3 people in view are not matched to known faces. Latest AI note. Smart Sentry is engaging person target 71 in precision phase. Visible detections include 2 people. 2 people in view are not matched to known faces. The acoustic guard has also detected unusual sound recently. End of analysys report.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-06 23:10:07] operator / voice_transcript_partial / voice: smart sentry is engaging pir scan targets running one in precision face disabled to to keyboard view are not mask to known faces
  meta: kind=partial | timestamp=1778080207.5936763 | source=vosk | frequency_hz=389.0 | rms=312 | updated_at=1778080194.0429964
- [2026-05-06 23:10:07] operator / voice_transcript_partial / voice: smart sentry is engaging pir scan targets running one in precision face disabled to to keyboard view are not mask to known faces acoustic
  meta: kind=partial | timestamp=1778080207.8044221 | source=vosk | frequency_hz=389.0 | rms=312 | updated_at=1778080194.0429964
- [2026-05-06 23:10:08] operator / voice_transcript_partial / voice: smart sentry is engaging pir scan targets running one in precision face disabled to to keyboard view are not mask to known faces the current
  meta: kind=partial | timestamp=1778080208.0941074 | source=vosk | frequency_hz=389.0 | rms=312 | updated_at=1778080194.0429964
- [2026-05-06 23:10:08] operator / voice_transcript_partial / voice: smart sentry is engaging pir scan targets running one in precision face disabled to to keyboard view are not mask to known faces acoustic guard off
  meta: kind=partial | timestamp=1778080208.300559 | source=vosk | frequency_hz=389.0 | rms=312 | updated_at=1778080194.0429964
- [2026-05-06 23:10:08] operator / voice_transcript_partial / voice: smart sentry is engaging pir scan targets running one in precision face disabled to to keyboard view are not mask to known faces acoustic guard is auto
  meta: kind=partial | timestamp=1778080208.4999669 | source=vosk | frequency_hz=389.0 | rms=312 | updated_at=1778080194.0429964
- [2026-05-06 23:10:08] operator / voice_transcript_partial / voice: smart sentry is engaging pir scan targets running one in precision face disabled to to keyboard view are not mask to known faces acoustic guard is auto detection
  meta: kind=partial | timestamp=1778080208.8345506 | source=vosk | frequency_hz=389.0 | rms=312 | updated_at=1778080194.0429964
- [2026-05-06 23:10:09] operator / voice_transcript_partial / voice: smart sentry is engaging pir scan targets running one in precision face disabled to to keyboard view are not mask to known faces acoustic guard is auto detection on mute
  meta: kind=partial | timestamp=1778080209.243642 | source=vosk | frequency_hz=389.0 | rms=312 | updated_at=1778080194.0429964
- [2026-05-06 23:10:09] operator / voice_transcript_partial / voice: smart sentry is engaging pir scan targets running one in precision face disabled to to keyboard view are not mask to known faces acoustic guard is auto detection on neutral sound
  meta: kind=partial | timestamp=1778080209.7582674 | source=vosk | frequency_hz=389.0 | rms=312 | updated_at=1778080194.0429964
- [2026-05-06 23:10:10] operator / voice_transcript_partial / voice: smart sentry is engaging pir scan targets running one in precision face disabled to to keyboard view are not mask to known faces acoustic guard is auto detection on neutral sound cues
  meta: kind=partial | timestamp=1778080210.2566078 | source=vosk | frequency_hz=389.0 | rms=312 | updated_at=1778080194.0429964
- [2026-05-06 23:10:10] operator / voice_transcript_partial / voice: smart sentry is engaging pir scan targets running one in precision face disabled to to keyboard view are not mask to known faces acoustic guard is auto detection on neutral sound
  meta: kind=partial | timestamp=1778080210.496377 | source=vosk | frequency_hz=389.0 | rms=312 | updated_at=1778080194.0429964
- [2026-05-06 23:10:11] operator / voice_transcript_final / voice: smart sentry is engaging pir scan targets setting one in precision face disable to to keyboard view are not mask to known faces acoustic guard is auto detection on neutral sound
  meta: kind=final | timestamp=1778080211.600668 | source=final | frequency_hz=389.0 | rms=312 | updated_at=1778080194.0429964
- [2026-05-06 23:10:13] operator / voice_transcript_partial / voice: leon
  meta: kind=partial | timestamp=1778080213.0618637 | source=vosk | frequency_hz=389.0 | rms=312 | updated_at=1778080194.0429964
- [2026-05-06 23:10:13] operator / voice_transcript_partial / voice: laser
  meta: kind=partial | timestamp=1778080213.2883327 | source=vosk | frequency_hz=389.0 | rms=312 | updated_at=1778080194.0429964
- [2026-05-06 23:10:13] operator / voice_transcript_partial / voice: blink disabled
  meta: kind=partial | timestamp=1778080213.5510113 | source=vosk | frequency_hz=389.0 | rms=312 | updated_at=1778080194.0429964
- [2026-05-06 23:10:13] operator / voice_transcript_partial / voice: laser assistant is
  meta: kind=partial | timestamp=1778080213.7742198 | source=vosk | frequency_hz=389.0 | rms=312 | updated_at=1778080194.0429964
- [2026-05-06 23:10:14] operator / voice_transcript_partial / voice: laser assistant is disable
  meta: kind=partial | timestamp=1778080214.587936 | source=vosk | frequency_hz=389.0 | rms=312 | updated_at=1778080194.0429964
- [2026-05-06 23:10:15] operator / voice_transcript_partial / voice: laser assistant is the status
  meta: kind=partial | timestamp=1778080215.1263156 | source=vosk | frequency_hz=389.0 | rms=312 | updated_at=1778080194.0429964
- [2026-05-06 23:10:15] operator / voice_transcript_partial / voice: laser assistant is the status of
  meta: kind=partial | timestamp=1778080215.2826483 | source=vosk | frequency_hz=389.0 | rms=312 | updated_at=1778080194.0429964
- [2026-05-06 23:10:15] operator / voice_transcript_partial / voice: laser assistant is the status of analyze
  meta: kind=partial | timestamp=1778080215.5368783 | source=vosk | frequency_hz=389.0 | rms=312 | updated_at=1778080194.0429964
- [2026-05-06 23:10:15] operator / voice_transcript_partial / voice: laser assistant is the status of analyze the shortcuts
  meta: kind=partial | timestamp=1778080215.7987018 | source=vosk | frequency_hz=389.0 | rms=312 | updated_at=1778080194.0429964
- [2026-05-06 23:10:16] operator / voice_transcript_partial / voice: laser assistant is the status of analyze the board
  meta: kind=partial | timestamp=1778080216.5318668 | source=vosk | frequency_hz=344.0 | rms=318 | updated_at=1778080216.5143492
- [2026-05-06 23:10:17] operator / voice_transcript_final / voice: laser assistant is the status of analyze the show port
  meta: kind=final | timestamp=1778080217.3829226 | source=final | frequency_hz=352.4 | rms=300 | updated_at=1778080217.0201344
- [2026-05-06 23:10:20] operator / voice_transcript_partial / voice: acoustic
  meta: kind=partial | timestamp=1778080220.4585354 | source=vosk | frequency_hz=367.2 | rms=377 | updated_at=1778080219.9685335
- [2026-05-06 23:10:20] operator / voice_transcript_partial / voice: acoustic guard
  meta: kind=partial | timestamp=1778080220.977375 | source=vosk | frequency_hz=367.2 | rms=377 | updated_at=1778080219.9685335
- [2026-05-06 23:10:21] operator / voice_transcript_partial / voice: acoustic guard detection
  meta: kind=partial | timestamp=1778080221.4677541 | source=vosk | frequency_hz=367.2 | rms=377 | updated_at=1778080219.9685335
- [2026-05-06 23:10:22] operator / voice_transcript_partial / voice: acoustic guard detection id
  meta: kind=partial | timestamp=1778080222.021211 | source=vosk | frequency_hz=367.2 | rms=377 | updated_at=1778080219.9685335
- [2026-05-06 23:10:22] operator / voice_transcript_partial / voice: acoustic guard detection id on neutral
  meta: kind=partial | timestamp=1778080222.221271 | source=vosk | frequency_hz=367.2 | rms=377 | updated_at=1778080219.9685335
- [2026-05-06 23:10:22] operator / voice_transcript_partial / voice: acoustic guard detection id on neutral sound
  meta: kind=partial | timestamp=1778080222.4459023 | source=vosk | frequency_hz=367.2 | rms=377 | updated_at=1778080219.9685335
- [2026-05-06 23:10:23] operator / voice_transcript_partial / voice: acoustic guard detection id on neutral sound of output
  meta: kind=partial | timestamp=1778080223.2123427 | source=vosk | frequency_hz=367.2 | rms=377 | updated_at=1778080219.9685335
- [2026-05-06 23:10:23] operator / voice_transcript_partial / voice: acoustic guard detection id on neutral sound ml
  meta: kind=partial | timestamp=1778080223.4690018 | source=vosk | frequency_hz=367.2 | rms=377 | updated_at=1778080219.9685335
- [2026-05-06 23:10:23] operator / voice_transcript_partial / voice: acoustic guard detection id on neutral sound ml threat scores
  meta: kind=partial | timestamp=1778080223.976199 | source=vosk | frequency_hz=370.0 | rms=296 | updated_at=1778080223.6958706
- [2026-05-06 23:10:24] operator / voice_transcript_partial / voice: acoustic guard detection id on neutral sound ml threat servo
  meta: kind=partial | timestamp=1778080224.4759145 | source=vosk | frequency_hz=370.0 | rms=296 | updated_at=1778080223.6958706
- [2026-05-06 23:10:24] operator / voice_transcript_partial / voice: acoustic guard detection id on neutral sound ml threat session disabled
  meta: kind=partial | timestamp=1778080224.713045 | source=vosk | frequency_hz=370.0 | rms=296 | updated_at=1778080223.6958706
- [2026-05-06 23:10:25] operator / voice_transcript_partial / voice: acoustic guard detection id on neutral sound ml threat servo disable suppress
  meta: kind=partial | timestamp=1778080225.2282588 | source=vosk | frequency_hz=370.0 | rms=296 | updated_at=1778080223.6958706
- [2026-05-06 23:10:25] operator / voice_transcript_partial / voice: acoustic guard detection id on neutral sound ml threat servo disable servo motion
  meta: kind=partial | timestamp=1778080225.516775 | source=vosk | frequency_hz=370.0 | rms=296 | updated_at=1778080223.6958706
- [2026-05-06 23:10:25] operator / voice_transcript_partial / voice: acoustic guard detection id on neutral sound ml threat servo disable servo face
  meta: kind=partial | timestamp=1778080225.7239738 | source=vosk | frequency_hz=370.0 | rms=296 | updated_at=1778080223.6958706
- [2026-05-06 23:10:26] operator / voice_transcript_partial / voice: acoustic guard detection id on neutral sound ml threat servo disable servo face lion
  meta: kind=partial | timestamp=1778080226.2295647 | source=vosk | frequency_hz=370.2 | rms=299 | updated_at=1778080226.218477
- [2026-05-06 23:10:27] operator / voice_transcript_partial / voice: acoustic guard detection id on neutral sound ml threat servo disable servo face lion current status
  meta: kind=partial | timestamp=1778080227.0078933 | source=vosk | frequency_hz=370.2 | rms=299 | updated_at=1778080226.218477
- [2026-05-06 23:10:27] operator / voice_transcript_partial / voice: acoustic guard detection id on neutral sound ml threat servo disable servo face lion current status engaging scope
  meta: kind=partial | timestamp=1778080227.9552903 | source=vosk | frequency_hz=372.0 | rms=314 | updated_at=1778080227.939244
- [2026-05-06 23:10:29] operator / voice_transcript_final / voice: elion acoustic guard detection id on neutral sound ml threat servo disable servo face lion current status engaging
  meta: kind=final | timestamp=1778080229.6365998 | source=final | frequency_hz=355.6 | rms=309 | updated_at=1778080228.4408574
- [2026-05-06 23:10:30] operator / voice_command / voice: acoustic guard detection id on neutral sound ml threat servo disable servo face lion current status engaging
  meta: normalized=True
- [2026-05-06 23:10:30] assistant / spoken_confirmation / voice: I can keep going with voice change. Tell me a voice family like Russian or Indian, ask what are the options, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 23:10:39] operator / voice_transcript_partial / voice: ai can keep go voice change tell me a voice disabled light on engagement
  meta: kind=partial | timestamp=1778080239.1408544 | source=vosk | frequency_hz=420.0 | rms=300 | updated_at=1778080235.4957473
- [2026-05-06 23:10:39] operator / voice_transcript_partial / voice: ai can keep go voice change tell me a voice disabled light on engagement after
  meta: kind=partial | timestamp=1778080239.3439672 | source=vosk | frequency_hz=420.0 | rms=300 | updated_at=1778080235.4957473
- [2026-05-06 23:10:39] operator / voice_transcript_partial / voice: ai can keep go voice change tell me a voice disabled light on engagement after the
  meta: kind=partial | timestamp=1778080239.5829706 | source=vosk | frequency_hz=420.0 | rms=300 | updated_at=1778080235.4957473
- [2026-05-06 23:10:40] operator / voice_transcript_partial / voice: ai can keep go voice change tell me a voice disabled light on engagement after the object detection
  meta: kind=partial | timestamp=1778080240.3511145 | source=vosk | frequency_hz=420.0 | rms=300 | updated_at=1778080235.4957473
- [2026-05-06 23:10:40] operator / voice_transcript_partial / voice: ai can keep go voice change tell me a voice disabled light on engagement after the off anomaly
  meta: kind=partial | timestamp=1778080240.5857966 | source=vosk | frequency_hz=420.0 | rms=300 | updated_at=1778080235.4957473
- [2026-05-06 23:10:41] operator / voice_transcript_final / voice: ai can keep go voice change tell me a voice disable light tracking on engagement after the off
  meta: kind=final | timestamp=1778080241.503107 | source=final | frequency_hz=420.0 | rms=300 | updated_at=1778080235.4957473
- [2026-05-06 23:10:44] operator / voice_command / voice: ai can keep go voice change tell me a voice disable light tracking on engagement after the off
  meta: normalized=True
- [2026-05-06 23:10:42] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778080242.847905 | source=vosk | frequency_hz=420.0 | rms=300 | updated_at=1778080235.4957473
- [2026-05-06 23:10:43] operator / voice_transcript_final / voice: the loop
  meta: kind=final | timestamp=1778080243.9370382 | source=final | frequency_hz=294.8 | rms=335 | updated_at=1778080243.7255886
- [2026-05-06 23:10:52] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1778080252.6054754 | source=vosk | frequency_hz=357.3 | rms=303 | updated_at=1778080251.8715115
- [2026-05-06 23:10:52] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1778080252.8576045 | source=vosk | frequency_hz=357.3 | rms=303 | updated_at=1778080251.8715115
- [2026-05-06 23:10:53] operator / voice_transcript_partial / voice: a joke
  meta: kind=partial | timestamp=1778080253.1300366 | source=vosk | frequency_hz=357.3 | rms=303 | updated_at=1778080251.8715115
- [2026-05-06 23:10:53] operator / voice_transcript_partial / voice: a joke on
  meta: kind=partial | timestamp=1778080253.754993 | source=vosk | frequency_hz=357.3 | rms=303 | updated_at=1778080251.8715115
- [2026-05-06 23:10:53] operator / voice_transcript_partial / voice: a joke on alerts
  meta: kind=partial | timestamp=1778080253.8646476 | source=vosk | frequency_hz=357.3 | rms=303 | updated_at=1778080251.8715115
- [2026-05-06 23:10:54] operator / voice_transcript_final / voice: a joke on alerts
  meta: kind=final | timestamp=1778080254.880457 | source=final | frequency_hz=357.3 | rms=303 | updated_at=1778080251.8715115
- [2026-05-06 23:11:07] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1778080267.1242218 | source=vosk | frequency_hz=373.9 | rms=292 | updated_at=1778080264.6201816
- [2026-05-06 23:11:07] operator / voice_transcript_partial / voice: on
  meta: kind=partial | timestamp=1778080267.357494 | source=vosk | frequency_hz=338.0 | rms=315 | updated_at=1778080267.3463254
- [2026-05-06 23:11:08] operator / voice_transcript_final / voice: on
  meta: kind=final | timestamp=1778080268.0542274 | source=final | frequency_hz=320.5 | rms=305 | updated_at=1778080267.5864108
- [2026-05-06 23:11:09] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1778080269.8796217 | source=vosk | frequency_hz=320.5 | rms=305 | updated_at=1778080267.5864108
- [2026-05-06 23:11:15] operator / voice_transcript_partial / voice: keyboard
  meta: kind=partial | timestamp=1778080275.3827813 | source=vosk | frequency_hz=335.5 | rms=303 | updated_at=1778080271.8404152
- [2026-05-06 23:11:15] operator / voice_transcript_partial / voice: greeting
  meta: kind=partial | timestamp=1778080275.5979412 | source=vosk | frequency_hz=335.5 | rms=303 | updated_at=1778080271.8404152
- [2026-05-06 23:11:15] operator / voice_transcript_partial / voice: engaging
  meta: kind=partial | timestamp=1778080275.8759267 | source=vosk | frequency_hz=335.5 | rms=303 | updated_at=1778080271.8404152
- [2026-05-06 23:11:16] operator / voice_transcript_partial / voice: engaging scope
  meta: kind=partial | timestamp=1778080276.1209605 | source=vosk | frequency_hz=335.5 | rms=303 | updated_at=1778080271.8404152
- [2026-05-06 23:11:17] operator / voice_transcript_final / voice: greeting
  meta: kind=final | timestamp=1778080277.1039557 | source=final | frequency_hz=354.7 | rms=316 | updated_at=1778080276.9079237
- [2026-05-06 23:11:19] operator / voice_transcript_partial / voice: inversion
  meta: kind=partial | timestamp=1778080279.8741205 | source=vosk | frequency_hz=332.0 | rms=316 | updated_at=1778080278.3420537
- [2026-05-06 23:11:20] operator / voice_transcript_partial / voice: include logs
  meta: kind=partial | timestamp=1778080280.102024 | source=vosk | frequency_hz=332.0 | rms=316 | updated_at=1778080278.3420537
- [2026-05-06 23:11:20] operator / voice_transcript_final / voice: inversion
  meta: kind=final | timestamp=1778080280.8660295 | source=final | frequency_hz=332.0 | rms=316 | updated_at=1778080278.3420537
- [2026-05-06 23:11:24] operator / voice_transcript_partial / voice: shortcuts
  meta: kind=partial | timestamp=1778080284.1074014 | source=vosk | frequency_hz=332.1 | rms=316 | updated_at=1778080281.3503904
- [2026-05-06 23:11:24] operator / voice_transcript_partial / voice: show
  meta: kind=partial | timestamp=1778080284.367076 | source=vosk | frequency_hz=332.1 | rms=316 | updated_at=1778080281.3503904
- [2026-05-06 23:11:24] operator / voice_transcript_partial / voice: show movement
  meta: kind=partial | timestamp=1778080284.7244027 | source=vosk | frequency_hz=332.1 | rms=316 | updated_at=1778080281.3503904
- [2026-05-06 23:11:25] operator / voice_transcript_partial / voice: show manual movement
  meta: kind=partial | timestamp=1778080285.1073956 | source=vosk | frequency_hz=332.1 | rms=316 | updated_at=1778080281.3503904
- [2026-05-06 23:11:25] operator / voice_transcript_partial / voice: show no
  meta: kind=partial | timestamp=1778080285.3872795 | source=vosk | frequency_hz=332.1 | rms=316 | updated_at=1778080281.3503904
- [2026-05-06 23:11:26] operator / voice_transcript_final / voice: show no
  meta: kind=final | timestamp=1778080286.0817842 | source=final | frequency_hz=332.1 | rms=316 | updated_at=1778080281.3503904
- [2026-05-06 23:11:28] operator / voice_transcript_partial / voice: human voice
  meta: kind=partial | timestamp=1778080288.6544235 | source=vosk | frequency_hz=363.3 | rms=407 | updated_at=1778080287.86995
- [2026-05-06 23:11:28] operator / voice_transcript_partial / voice: human off
  meta: kind=partial | timestamp=1778080288.977451 | source=vosk | frequency_hz=363.3 | rms=407 | updated_at=1778080287.86995
- [2026-05-06 23:11:29] operator / voice_transcript_partial / voice: human off the
  meta: kind=partial | timestamp=1778080289.1627076 | source=vosk | frequency_hz=363.3 | rms=407 | updated_at=1778080287.86995
- [2026-05-06 23:11:29] operator / voice_transcript_partial / voice: camera feed enabled
  meta: kind=partial | timestamp=1778080289.433708 | source=vosk | frequency_hz=363.3 | rms=407 | updated_at=1778080287.86995
- [2026-05-06 23:11:29] operator / voice_transcript_partial / voice: human off the alien
  meta: kind=partial | timestamp=1778080289.6673675 | source=vosk | frequency_hz=363.3 | rms=407 | updated_at=1778080287.86995
- [2026-05-06 23:11:29] operator / voice_transcript_partial / voice: human off the aiming
  meta: kind=partial | timestamp=1778080289.8798091 | source=vosk | frequency_hz=382.0 | rms=318 | updated_at=1778080289.8701348
- [2026-05-06 23:11:30] operator / voice_transcript_partial / voice: human off the aiming zone
  meta: kind=partial | timestamp=1778080290.1685765 | source=vosk | frequency_hz=382.0 | rms=318 | updated_at=1778080289.8701348
- [2026-05-06 23:11:30] operator / voice_transcript_final / voice: human off the aiming zone
  meta: kind=final | timestamp=1778080290.8675733 | source=final | frequency_hz=382.0 | rms=318 | updated_at=1778080289.8701348
- [2026-05-06 23:11:36] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1778080296.664694 | source=vosk | frequency_hz=355.1 | rms=318 | updated_at=1778080296.1516464
- [2026-05-06 23:11:38] operator / voice_transcript_partial / voice: scope view
  meta: kind=partial | timestamp=1778080298.8797343 | source=vosk | frequency_hz=351.4 | rms=302 | updated_at=1778080298.6238635
- [2026-05-06 23:11:39] operator / voice_transcript_partial / voice: you working
  meta: kind=partial | timestamp=1778080299.1953335 | source=vosk | frequency_hz=351.4 | rms=302 | updated_at=1778080298.6238635
- [2026-05-06 23:11:39] operator / voice_transcript_partial / voice: slew order
  meta: kind=partial | timestamp=1778080299.4231339 | source=vosk | frequency_hz=337.6 | rms=309 | updated_at=1778080299.3841186
- [2026-05-06 23:11:40] operator / voice_transcript_final / voice: slew order
  meta: kind=final | timestamp=1778080300.270282 | source=final | frequency_hz=344.5 | rms=284 | updated_at=1778080300.1249456
- [2026-05-06 23:11:41] operator / voice_transcript_partial / voice: pir
  meta: kind=partial | timestamp=1778080301.8972974 | source=vosk | frequency_hz=368.1 | rms=391 | updated_at=1778080301.880759
- [2026-05-06 23:11:42] operator / voice_transcript_partial / voice: prompted
  meta: kind=partial | timestamp=1778080302.1422849 | source=vosk | frequency_hz=356.9 | rms=329 | updated_at=1778080302.1342359
- [2026-05-06 23:11:43] operator / voice_transcript_final / voice: pir active
  meta: kind=final | timestamp=1778080303.0430324 | source=final | frequency_hz=338.1 | rms=315 | updated_at=1778080302.8787625
- [2026-05-06 23:11:44] operator / voice_transcript_partial / voice: detection
  meta: kind=partial | timestamp=1778080304.1698709 | source=vosk | frequency_hz=333.9 | rms=318 | updated_at=1778080303.3981955
- [2026-05-06 23:11:44] operator / voice_transcript_partial / voice: prompted target
  meta: kind=partial | timestamp=1778080304.4059837 | source=vosk | frequency_hz=333.9 | rms=318 | updated_at=1778080303.3981955
- [2026-05-06 23:11:44] operator / voice_transcript_partial / voice: turn
  meta: kind=partial | timestamp=1778080304.902185 | source=vosk | frequency_hz=333.9 | rms=318 | updated_at=1778080303.3981955
- [2026-05-06 23:11:45] operator / voice_transcript_partial / voice: turn on
  meta: kind=partial | timestamp=1778080305.1525497 | source=vosk | frequency_hz=333.9 | rms=318 | updated_at=1778080303.3981955
- [2026-05-06 23:11:51] operator / voice_transcript_partial / voice: on
  meta: kind=partial | timestamp=1778080311.2945285 | source=vosk | frequency_hz=316.8 | rms=321 | updated_at=1778080310.548922
- [2026-05-06 23:11:51] operator / voice_transcript_partial / voice: on lion voice
  meta: kind=partial | timestamp=1778080311.636594 | source=vosk | frequency_hz=316.8 | rms=321 | updated_at=1778080310.548922
- [2026-05-06 23:11:52] operator / voice_transcript_partial / voice: on lion voice face greeting
  meta: kind=partial | timestamp=1778080312.296801 | source=vosk | frequency_hz=316.8 | rms=321 | updated_at=1778080310.548922
- [2026-05-06 23:11:52] operator / voice_transcript_partial / voice: on lion voice safe
  meta: kind=partial | timestamp=1778080312.579084 | source=vosk | frequency_hz=316.8 | rms=321 | updated_at=1778080310.548922
- [2026-05-06 23:11:52] operator / voice_transcript_partial / voice: on lion voice to on
  meta: kind=partial | timestamp=1778080312.8088608 | source=vosk | frequency_hz=316.8 | rms=321 | updated_at=1778080310.548922
- [2026-05-06 23:11:53] operator / voice_transcript_partial / voice: on lion voice to on lion
  meta: kind=partial | timestamp=1778080313.0829802 | source=vosk | frequency_hz=316.8 | rms=321 | updated_at=1778080310.548922
- [2026-05-06 23:11:53] operator / voice_transcript_partial / voice: on lion voice to on lion enable
  meta: kind=partial | timestamp=1778080313.3218906 | source=vosk | frequency_hz=316.8 | rms=321 | updated_at=1778080310.548922
- [2026-05-06 23:11:53] operator / voice_transcript_partial / voice: on lion voice to on lion inversion
  meta: kind=partial | timestamp=1778080313.5467694 | source=vosk | frequency_hz=316.8 | rms=321 | updated_at=1778080310.548922
- [2026-05-06 23:11:53] operator / voice_transcript_partial / voice: on lion voice to on lion increase
  meta: kind=partial | timestamp=1778080313.8910036 | source=vosk | frequency_hz=316.8 | rms=321 | updated_at=1778080310.548922
- [2026-05-06 23:11:54] operator / voice_transcript_partial / voice: on lion voice to on lion increase alien
  meta: kind=partial | timestamp=1778080314.2917063 | source=vosk | frequency_hz=316.8 | rms=321 | updated_at=1778080310.548922
- [2026-05-06 23:11:54] operator / voice_transcript_partial / voice: on lion voice to on lion increase alien running
  meta: kind=partial | timestamp=1778080314.5599139 | source=vosk | frequency_hz=316.8 | rms=321 | updated_at=1778080310.548922
- [2026-05-06 23:11:54] operator / voice_transcript_partial / voice: on lion voice to on lion increase alien run
  meta: kind=partial | timestamp=1778080314.8367271 | source=vosk | frequency_hz=376.0 | rms=306 | updated_at=1778080314.7856367
- [2026-05-06 23:11:56] operator / voice_transcript_partial / voice: human voice
  meta: kind=partial | timestamp=1778080316.2066753 | source=vosk | frequency_hz=391.4 | rms=328 | updated_at=1778080315.6659596
- [2026-05-06 23:11:57] operator / voice_transcript_final / voice: human
  meta: kind=final | timestamp=1778080317.6627069 | source=final | frequency_hz=369.2 | rms=303 | updated_at=1778080316.9198651
- [2026-05-06 23:12:00] operator / voice_transcript_partial / voice: mute
  meta: kind=partial | timestamp=1778080320.906918 | source=vosk | frequency_hz=336.0 | rms=312 | updated_at=1778080320.3600318
- [2026-05-06 23:12:01] operator / voice_transcript_partial / voice: mute disabled
  meta: kind=partial | timestamp=1778080321.6219466 | source=vosk | frequency_hz=336.0 | rms=312 | updated_at=1778080320.3600318
- [2026-05-06 23:12:02] operator / voice_transcript_partial / voice: mute disabled tuning logger
  meta: kind=partial | timestamp=1778080322.1391344 | source=vosk | frequency_hz=336.0 | rms=312 | updated_at=1778080320.3600318
- [2026-05-06 23:12:02] operator / voice_transcript_final / voice: mute disable
  meta: kind=final | timestamp=1778080322.4892056 | source=final | frequency_hz=336.0 | rms=312 | updated_at=1778080320.3600318
- [2026-05-06 23:12:12] operator / voice_transcript_partial / voice: what's the pir scan
  meta: kind=partial | timestamp=1778080332.5858428 | source=vosk | frequency_hz=272.0 | rms=851 | updated_at=1778080330.5664186
- [2026-05-06 23:12:12] operator / voice_transcript_partial / voice: what's the visual
  meta: kind=partial | timestamp=1778080332.818063 | source=vosk | frequency_hz=272.0 | rms=851 | updated_at=1778080330.5664186
- [2026-05-06 23:12:13] operator / voice_transcript_partial / voice: what's the visual the
  meta: kind=partial | timestamp=1778080333.0726516 | source=vosk | frequency_hz=272.0 | rms=851 | updated_at=1778080330.5664186
- [2026-05-06 23:12:13] operator / voice_transcript_partial / voice: what's the visual the hello
  meta: kind=partial | timestamp=1778080333.3302448 | source=vosk | frequency_hz=272.0 | rms=851 | updated_at=1778080330.5664186
- [2026-05-06 23:12:14] operator / voice_transcript_final / voice: targets the visual the hello
  meta: kind=final | timestamp=1778080334.4664402 | source=final | frequency_hz=272.0 | rms=851 | updated_at=1778080330.5664186
- [2026-05-06 23:12:14] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1778080334.5716944 | source=vosk | frequency_hz=272.0 | rms=851 | updated_at=1778080330.5664186
- [2026-05-06 23:12:14] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1778080334.8751657 | source=vosk | frequency_hz=272.0 | rms=851 | updated_at=1778080330.5664186
- [2026-05-06 23:12:15] operator / voice_transcript_partial / voice: smart sentry hello
  meta: kind=partial | timestamp=1778080335.3228533 | source=vosk | frequency_hz=272.0 | rms=851 | updated_at=1778080330.5664186
- [2026-05-06 23:12:15] operator / voice_transcript_partial / voice: smart sentry hello activate
  meta: kind=partial | timestamp=1778080335.8163707 | source=vosk | frequency_hz=272.0 | rms=851 | updated_at=1778080330.5664186
- [2026-05-06 23:12:16] operator / voice_transcript_partial / voice: smart sentry hello targets
  meta: kind=partial | timestamp=1778080336.0873106 | source=vosk | frequency_hz=272.0 | rms=851 | updated_at=1778080330.5664186
- [2026-05-06 23:12:16] operator / voice_transcript_partial / voice: smart sentry hello targets mode
  meta: kind=partial | timestamp=1778080336.3138328 | source=vosk | frequency_hz=272.0 | rms=851 | updated_at=1778080330.5664186
- [2026-05-06 23:12:16] operator / voice_transcript_partial / voice: smart sentry hello targets mode is on
  meta: kind=partial | timestamp=1778080336.5726457 | source=vosk | frequency_hz=272.0 | rms=851 | updated_at=1778080330.5664186
- [2026-05-06 23:12:17] operator / voice_transcript_partial / voice: smart sentry hello targets mode is on light
  meta: kind=partial | timestamp=1778080337.0574174 | source=vosk | frequency_hz=272.0 | rms=851 | updated_at=1778080330.5664186
- [2026-05-06 23:12:17] operator / voice_transcript_final / voice: smart sentry hello targets mode is on light
  meta: kind=final | timestamp=1778080337.9076333 | source=final | frequency_hz=272.0 | rms=851 | updated_at=1778080330.5664186
- [2026-05-06 23:12:18] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1778080338.739484 | source=vosk | frequency_hz=292.8 | rms=1176 | updated_at=1778080338.7231894
- [2026-05-06 23:12:19] operator / voice_transcript_partial / voice: voice detection
  meta: kind=partial | timestamp=1778080339.5165462 | source=vosk | frequency_hz=292.8 | rms=1176 | updated_at=1778080338.7231894
- [2026-05-06 23:12:19] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1778080339.5378544 | source=vosk | frequency_hz=292.8 | rms=1176 | updated_at=1778080338.7231894
- [2026-05-06 23:12:20] operator / voice_transcript_final / voice: voice enable
  meta: kind=final | timestamp=1778080340.6035862 | source=final | frequency_hz=292.8 | rms=1176 | updated_at=1778080338.7231894
- [2026-05-06 23:12:21] operator / voice_transcript_partial / voice: machine
  meta: kind=partial | timestamp=1778080341.837461 | source=vosk | frequency_hz=74.0 | rms=1203 | updated_at=1778080341.204249
- [2026-05-06 23:12:22] operator / voice_transcript_partial / voice: leon
  meta: kind=partial | timestamp=1778080342.2731287 | source=vosk | frequency_hz=74.0 | rms=1203 | updated_at=1778080341.204249
- [2026-05-06 23:12:24] operator / voice_transcript_partial / voice: export
  meta: kind=partial | timestamp=1778080344.2809348 | source=vosk | frequency_hz=121.6 | rms=791 | updated_at=1778080342.5143447
- [2026-05-06 23:12:24] operator / voice_transcript_partial / voice: precision
  meta: kind=partial | timestamp=1778080344.7803562 | source=vosk | frequency_hz=121.6 | rms=791 | updated_at=1778080342.5143447
- [2026-05-06 23:12:25] operator / voice_transcript_partial / voice: suppress known
  meta: kind=partial | timestamp=1778080345.0634487 | source=vosk | frequency_hz=121.6 | rms=791 | updated_at=1778080342.5143447
- [2026-05-06 23:12:25] operator / voice_transcript_final / voice: suppress
  meta: kind=final | timestamp=1778080345.6979184 | source=final | frequency_hz=121.6 | rms=791 | updated_at=1778080342.5143447
- [2026-05-06 23:12:36] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1778080356.3284605 | source=vosk | frequency_hz=290.8 | rms=255 | updated_at=1778080355.353097
- [2026-05-06 23:12:37] operator / voice_transcript_final / voice: no
  meta: kind=final | timestamp=1778080357.2655761 | source=final | frequency_hz=290.8 | rms=255 | updated_at=1778080355.353097
- [2026-05-06 23:12:37] operator / voice_transcript_partial / voice: smart status
  meta: kind=partial | timestamp=1778080357.8525777 | source=vosk | frequency_hz=290.8 | rms=255 | updated_at=1778080355.353097
- [2026-05-06 23:12:38] operator / voice_transcript_partial / voice: smart sentry human
  meta: kind=partial | timestamp=1778080358.0953212 | source=vosk | frequency_hz=290.8 | rms=255 | updated_at=1778080355.353097
- [2026-05-06 23:12:38] operator / voice_transcript_partial / voice: smart sentry human voice
  meta: kind=partial | timestamp=1778080358.351998 | source=vosk | frequency_hz=290.8 | rms=255 | updated_at=1778080355.353097
- [2026-05-06 23:12:38] operator / voice_transcript_partial / voice: smart sentry human voice mode
  meta: kind=partial | timestamp=1778080358.8318505 | source=vosk | frequency_hz=290.8 | rms=255 | updated_at=1778080355.353097
- [2026-05-06 23:12:39] operator / voice_transcript_partial / voice: smart sentry human voice mode is
  meta: kind=partial | timestamp=1778080359.1128588 | source=vosk | frequency_hz=290.8 | rms=255 | updated_at=1778080355.353097
- [2026-05-06 23:12:39] operator / voice_transcript_partial / voice: smart sentry human voice mode is on no
  meta: kind=partial | timestamp=1778080359.347831 | source=vosk | frequency_hz=290.8 | rms=255 | updated_at=1778080355.353097
- [2026-05-06 23:12:41] operator / voice_transcript_final / voice: smart sentry human voice mode is on light
  meta: kind=final | timestamp=1778080361.1357775 | source=final | frequency_hz=349.0 | rms=494 | updated_at=1778080360.322867
- [2026-05-06 23:12:41] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1778080361.2603798 | source=vosk | frequency_hz=349.0 | rms=494 | updated_at=1778080360.322867
- [2026-05-06 23:12:42] operator / voice_transcript_final / voice: voice order
  meta: kind=final | timestamp=1778080362.7170043 | source=final | frequency_hz=349.0 | rms=494 | updated_at=1778080360.322867
- [2026-05-06 23:12:44] operator / voice_transcript_partial / voice: startup
  meta: kind=partial | timestamp=1778080364.0056853 | source=vosk | frequency_hz=356.0 | rms=320 | updated_at=1778080362.788421
- [2026-05-06 23:12:44] operator / voice_transcript_partial / voice: startup running
  meta: kind=partial | timestamp=1778080364.40467 | source=vosk | frequency_hz=356.0 | rms=320 | updated_at=1778080362.788421
- [2026-05-06 23:12:44] operator / voice_transcript_partial / voice: status wrong
  meta: kind=partial | timestamp=1778080364.5070086 | source=vosk | frequency_hz=356.0 | rms=320 | updated_at=1778080362.788421
- [2026-05-06 23:12:44] operator / voice_transcript_partial / voice: status wrong guard
  meta: kind=partial | timestamp=1778080364.7894785 | source=vosk | frequency_hz=356.0 | rms=320 | updated_at=1778080362.788421
- [2026-05-06 23:12:45] operator / voice_transcript_partial / voice: status wrong guard cue
  meta: kind=partial | timestamp=1778080365.0271976 | source=vosk | frequency_hz=356.0 | rms=320 | updated_at=1778080362.788421
- [2026-05-06 23:12:45] operator / voice_transcript_final / voice: startup wrong guard view
  meta: kind=final | timestamp=1778080365.9969492 | source=final | frequency_hz=374.0 | rms=289 | updated_at=1778080365.763061
- [2026-05-06 23:13:05] operator / voice_transcript_partial / voice: hello
  meta: kind=partial | timestamp=1778080385.0420992 | source=vosk | frequency_hz=395.7 | rms=314 | updated_at=1778080384.264971
- [2026-05-06 23:13:05] operator / voice_transcript_partial / voice: pir guard
  meta: kind=partial | timestamp=1778080385.277528 | source=vosk | frequency_hz=395.7 | rms=314 | updated_at=1778080384.264971
- [2026-05-06 23:13:06] operator / voice_transcript_final / voice: hello guard
  meta: kind=final | timestamp=1778080386.5489943 | source=final | frequency_hz=355.6 | rms=306 | updated_at=1778080386.0041356
- [2026-05-06 23:13:12] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1778080392.0135484 | source=vosk | frequency_hz=333.8 | rms=316 | updated_at=1778080389.5221004
- [2026-05-06 23:13:12] operator / voice_transcript_partial / voice: do board
  meta: kind=partial | timestamp=1778080392.2679398 | source=vosk | frequency_hz=333.8 | rms=316 | updated_at=1778080389.5221004
- [2026-05-06 23:13:13] operator / voice_transcript_final / voice: do board
  meta: kind=final | timestamp=1778080393.8290002 | source=final | frequency_hz=344.0 | rms=322 | updated_at=1778080393.0294375
- [2026-05-06 23:13:15] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1778080395.1305256 | source=vosk | frequency_hz=269.2 | rms=1027 | updated_at=1778080395.074478
- [2026-05-06 23:13:23] operator / voice_transcript_partial / voice: known
  meta: kind=partial | timestamp=1778080403.5961673 | source=vosk | frequency_hz=377.4 | rms=338 | updated_at=1778080402.8251493
- [2026-05-06 23:13:24] operator / voice_transcript_final / voice: known
  meta: kind=final | timestamp=1778080404.7167053 | source=final | frequency_hz=359.9 | rms=315 | updated_at=1778080404.3240676
- [2026-05-06 23:13:36] operator / voice_transcript_partial / voice: voice active
  meta: kind=partial | timestamp=1778080416.8658636 | source=vosk | frequency_hz=382.0 | rms=313 | updated_at=1778080412.848256
- [2026-05-06 23:13:37] operator / voice_transcript_partial / voice: voice style
  meta: kind=partial | timestamp=1778080417.879648 | source=vosk | frequency_hz=382.0 | rms=313 | updated_at=1778080412.848256
- [2026-05-06 23:13:38] operator / voice_transcript_partial / voice: voice style guard
  meta: kind=partial | timestamp=1778080418.110682 | source=vosk | frequency_hz=382.0 | rms=313 | updated_at=1778080412.848256
- [2026-05-06 23:13:38] operator / voice_transcript_final / voice: voice style alert
  meta: kind=final | timestamp=1778080418.5958729 | source=final | frequency_hz=396.0 | rms=301 | updated_at=1778080418.5855477
- [2026-05-06 23:13:39] operator / voice_command / voice: voice style alert
  meta: normalized=True
- [2026-05-06 23:13:39] assistant / spoken_confirmation / voice: I can keep going with voice change. Tell me a voice family like Russian or Indian, ask what are the options, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 23:13:48] operator / voice_transcript_partial / voice: let me ask
  meta: kind=partial | timestamp=1778080428.3259017 | source=vosk | frequency_hz=230.0 | rms=1201 | updated_at=1778080425.9163659
- [2026-05-06 23:13:48] operator / voice_transcript_partial / voice: let me ask what are the
  meta: kind=partial | timestamp=1778080428.5557299 | source=vosk | frequency_hz=230.0 | rms=1201 | updated_at=1778080425.9163659
- [2026-05-06 23:13:49] operator / voice_transcript_partial / voice: let me ask what are the off keys
  meta: kind=partial | timestamp=1778080429.3076642 | source=vosk | frequency_hz=230.0 | rms=1201 | updated_at=1778080425.9163659
- [2026-05-06 23:13:49] operator / voice_transcript_partial / voice: let me ask what are the machine
  meta: kind=partial | timestamp=1778080429.5959482 | source=vosk | frequency_hz=230.0 | rms=1201 | updated_at=1778080425.9163659
- [2026-05-06 23:13:50] operator / voice_transcript_final / voice: let me ask what are the off keys
  meta: kind=final | timestamp=1778080430.0369563 | source=final | frequency_hz=230.0 | rms=1201 | updated_at=1778080425.9163659
- [2026-05-06 23:13:52] operator / voice_transcript_partial / voice: change your voice
  meta: kind=partial | timestamp=1778080432.0766172 | source=vosk | frequency_hz=356.4 | rms=313 | updated_at=1778080431.0368497
- [2026-05-06 23:13:52] operator / voice_transcript_partial / voice: change your voice to
  meta: kind=partial | timestamp=1778080432.5785005 | source=vosk | frequency_hz=356.4 | rms=313 | updated_at=1778080431.0368497
- [2026-05-06 23:13:52] operator / voice_transcript_partial / voice: change your voice to anything
  meta: kind=partial | timestamp=1778080432.839735 | source=vosk | frequency_hz=356.4 | rms=313 | updated_at=1778080431.0368497
- [2026-05-06 23:13:53] operator / voice_transcript_partial / voice: change your voice doing
  meta: kind=partial | timestamp=1778080433.08416 | source=vosk | frequency_hz=356.4 | rms=313 | updated_at=1778080431.0368497
- [2026-05-06 23:13:53] operator / voice_transcript_partial / voice: change your voice doing in human voice
  meta: kind=partial | timestamp=1778080433.3022811 | source=vosk | frequency_hz=356.4 | rms=313 | updated_at=1778080431.0368497
- [2026-05-06 23:13:53] operator / voice_transcript_partial / voice: change your voice doing inversion
  meta: kind=partial | timestamp=1778080433.571802 | source=vosk | frequency_hz=356.4 | rms=313 | updated_at=1778080431.0368497
- [2026-05-06 23:13:53] operator / voice_transcript_partial / voice: change your voice doing in human voice
  meta: kind=partial | timestamp=1778080433.8158207 | source=vosk | frequency_hz=356.4 | rms=313 | updated_at=1778080431.0368497
- [2026-05-06 23:13:54] operator / voice_transcript_final / voice: change your voice doing in human guard
  meta: kind=final | timestamp=1778080434.6178706 | source=final | frequency_hz=328.0 | rms=304 | updated_at=1778080434.2904296
- [2026-05-06 23:13:56] operator / voice_command / voice: change your voice doing in human guard
  meta: normalized=True
- [2026-05-06 23:13:57] assistant / spoken_confirmation / voice: Sure. Ask for a voice accent such as British, and include male or female if you want.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 23:14:04] operator / voice_transcript_partial / voice: on
  meta: kind=partial | timestamp=1778080444.2236328 | source=vosk | frequency_hz=318.8 | rms=319 | updated_at=1778080438.6727362
- [2026-05-06 23:14:04] operator / voice_transcript_partial / voice: com alien
  meta: kind=partial | timestamp=1778080444.4665058 | source=vosk | frequency_hz=318.8 | rms=319 | updated_at=1778080438.6727362
- [2026-05-06 23:14:13] operator / voice_transcript_partial / voice: changes
  meta: kind=partial | timestamp=1778080453.6830812 | source=vosk | frequency_hz=332.0 | rms=297 | updated_at=1778080452.9202185
- [2026-05-06 23:14:13] operator / voice_transcript_partial / voice: change your voice
  meta: kind=partial | timestamp=1778080453.937282 | source=vosk | frequency_hz=332.0 | rms=297 | updated_at=1778080452.9202185
- [2026-05-06 23:14:14] operator / voice_transcript_partial / voice: change your voice to
  meta: kind=partial | timestamp=1778080454.7116716 | source=vosk | frequency_hz=332.0 | rms=297 | updated_at=1778080452.9202185
- [2026-05-06 23:14:14] operator / voice_transcript_partial / voice: change your voice to alien
  meta: kind=partial | timestamp=1778080454.9563549 | source=vosk | frequency_hz=332.0 | rms=297 | updated_at=1778080452.9202185
- [2026-05-06 23:14:15] operator / voice_transcript_partial / voice: change your voice to enable human
  meta: kind=partial | timestamp=1778080455.2202964 | source=vosk | frequency_hz=332.0 | rms=297 | updated_at=1778080452.9202185
- [2026-05-06 23:14:15] operator / voice_transcript_partial / voice: change your voice to on alion deactivate
  meta: kind=partial | timestamp=1778080455.457585 | source=vosk | frequency_hz=332.0 | rms=297 | updated_at=1778080452.9202185
- [2026-05-06 23:14:16] operator / voice_transcript_partial / voice: change your voice to on alion yes
  meta: kind=partial | timestamp=1778080456.9162607 | source=vosk | frequency_hz=372.3 | rms=290 | updated_at=1778080456.8525941
- [2026-05-06 23:14:20] operator / voice_transcript_partial / voice: manual
  meta: kind=partial | timestamp=1778080460.0414999 | source=vosk | frequency_hz=365.9 | rms=283 | updated_at=1778080457.080805
- [2026-05-06 23:14:20] operator / voice_transcript_partial / voice: manual alien
  meta: kind=partial | timestamp=1778080460.5373259 | source=vosk | frequency_hz=365.9 | rms=283 | updated_at=1778080457.080805
- [2026-05-06 23:14:31] operator / voice_transcript_partial / voice: change your
  meta: kind=partial | timestamp=1778080471.762733 | source=vosk | frequency_hz=343.5 | rms=295 | updated_at=1778080470.2516592
- [2026-05-06 23:14:32] operator / voice_transcript_partial / voice: change your voice
  meta: kind=partial | timestamp=1778080472.0115433 | source=vosk | frequency_hz=343.5 | rms=295 | updated_at=1778080470.2516592
- [2026-05-06 23:14:32] operator / voice_transcript_partial / voice: change your voice reports
  meta: kind=partial | timestamp=1778080472.2589269 | source=vosk | frequency_hz=343.5 | rms=295 | updated_at=1778080470.2516592
- [2026-05-06 23:14:32] operator / voice_transcript_partial / voice: change your voice reports the
  meta: kind=partial | timestamp=1778080472.7828786 | source=vosk | frequency_hz=343.5 | rms=295 | updated_at=1778080470.2516592
- [2026-05-06 23:14:33] operator / voice_transcript_partial / voice: change your voice reports acc output
  meta: kind=partial | timestamp=1778080473.0171082 | source=vosk | frequency_hz=343.5 | rms=295 | updated_at=1778080470.2516592
- [2026-05-06 23:14:33] operator / voice_transcript_partial / voice: change your voice reports guard to on media
  meta: kind=partial | timestamp=1778080473.2702904 | source=vosk | frequency_hz=343.5 | rms=295 | updated_at=1778080470.2516592
- [2026-05-06 23:14:33] operator / voice_transcript_partial / voice: change your voice reports guard to on alien
  meta: kind=partial | timestamp=1778080473.514712 | source=vosk | frequency_hz=343.5 | rms=295 | updated_at=1778080470.2516592
- [2026-05-06 23:14:33] operator / voice_transcript_partial / voice: change your voice reports guard to ml
  meta: kind=partial | timestamp=1778080473.860149 | source=vosk | frequency_hz=343.5 | rms=295 | updated_at=1778080470.2516592
- [2026-05-06 23:14:34] operator / voice_transcript_partial / voice: change your voice reports guard to on alien deactivate
  meta: kind=partial | timestamp=1778080474.039957 | source=vosk | frequency_hz=343.5 | rms=295 | updated_at=1778080470.2516592
- [2026-05-06 23:14:34] operator / voice_transcript_partial / voice: change your voice reports guard to on media loop
  meta: kind=partial | timestamp=1778080474.2870655 | source=vosk | frequency_hz=343.5 | rms=295 | updated_at=1778080470.2516592
- [2026-05-06 23:14:34] operator / voice_transcript_final / voice: change your voice reports guard to on media
  meta: kind=final | timestamp=1778080474.993356 | source=final | frequency_hz=320.0 | rms=296 | updated_at=1778080474.494288
- [2026-05-06 23:14:36] operator / voice_command / voice: change your voice reports guard to on media
  meta: normalized=True
- [2026-05-06 23:14:37] assistant / spoken_confirmation / voice: Absolutely. Tell me a voice style like British male or British female.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 23:14:37] operator / voice_transcript_partial / voice: changes
  meta: kind=partial | timestamp=1778080477.0612266 | source=vosk | frequency_hz=346.0 | rms=654 | updated_at=1778080476.0508468
- [2026-05-06 23:14:37] operator / voice_transcript_partial / voice: change your voice
  meta: kind=partial | timestamp=1778080477.3152337 | source=vosk | frequency_hz=346.0 | rms=654 | updated_at=1778080476.0508468
- [2026-05-06 23:14:38] operator / voice_transcript_partial / voice: change your voice to anything deactivate
  meta: kind=partial | timestamp=1778080478.558985 | source=vosk | frequency_hz=346.0 | rms=654 | updated_at=1778080476.0508468
- [2026-05-06 23:14:38] operator / voice_transcript_partial / voice: change your voice to anything alien
  meta: kind=partial | timestamp=1778080478.8115478 | source=vosk | frequency_hz=346.0 | rms=654 | updated_at=1778080476.0508468
- [2026-05-06 23:14:39] operator / voice_transcript_partial / voice: change your voice to anything alien mask
  meta: kind=partial | timestamp=1778080479.5889459 | source=vosk | frequency_hz=346.0 | rms=654 | updated_at=1778080476.0508468
- [2026-05-06 23:14:41] operator / voice_transcript_partial / voice: camera
  meta: kind=partial | timestamp=1778080481.1605844 | source=vosk | frequency_hz=346.0 | rms=654 | updated_at=1778080476.0508468
- [2026-05-06 23:14:41] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1778080481.5429144 | source=vosk | frequency_hz=346.0 | rms=654 | updated_at=1778080476.0508468
- [2026-05-06 23:14:42] operator / voice_transcript_final / voice: voice
  meta: kind=final | timestamp=1778080482.7309937 | source=final | frequency_hz=354.0 | rms=873 | updated_at=1778080481.749323
- [2026-05-06 23:14:44] operator / voice_transcript_partial / voice: engagement
  meta: kind=partial | timestamp=1778080484.7848668 | source=vosk | frequency_hz=352.0 | rms=312 | updated_at=1778080483.0204744
- [2026-05-06 23:14:45] operator / voice_transcript_partial / voice: engaging media loop
  meta: kind=partial | timestamp=1778080485.1138654 | source=vosk | frequency_hz=352.0 | rms=312 | updated_at=1778080483.0204744
- [2026-05-06 23:14:45] operator / voice_transcript_partial / voice: in the enabled
  meta: kind=partial | timestamp=1778080485.3424244 | source=vosk | frequency_hz=372.0 | rms=310 | updated_at=1778080485.2988365
- [2026-05-06 23:14:46] operator / voice_transcript_final / voice: in the enable
  meta: kind=final | timestamp=1778080486.0138333 | source=final | frequency_hz=346.7 | rms=293 | updated_at=1778080485.7576346
- [2026-05-06 23:14:50] operator / voice_transcript_partial / voice: changes
  meta: kind=partial | timestamp=1778080490.7649739 | source=vosk | frequency_hz=316.2 | rms=306 | updated_at=1778080489.274033
- [2026-05-06 23:14:51] operator / voice_transcript_partial / voice: change your voice
  meta: kind=partial | timestamp=1778080491.0150964 | source=vosk | frequency_hz=316.2 | rms=306 | updated_at=1778080489.274033
- [2026-05-06 23:14:51] operator / voice_transcript_partial / voice: change your voice to
  meta: kind=partial | timestamp=1778080491.279287 | source=vosk | frequency_hz=316.2 | rms=306 | updated_at=1778080489.274033
- [2026-05-06 23:14:51] operator / voice_transcript_partial / voice: change your voice to on
  meta: kind=partial | timestamp=1778080491.6077776 | source=vosk | frequency_hz=316.2 | rms=306 | updated_at=1778080489.274033
- [2026-05-06 23:14:52] operator / voice_transcript_partial / voice: change your voice to on alion
  meta: kind=partial | timestamp=1778080492.0408306 | source=vosk | frequency_hz=316.2 | rms=306 | updated_at=1778080489.274033
- [2026-05-06 23:14:52] operator / voice_transcript_partial / voice: change your voice to on alion manual
  meta: kind=partial | timestamp=1778080492.525988 | source=vosk | frequency_hz=384.0 | rms=304 | updated_at=1778080492.5189724
- [2026-05-06 23:14:55] operator / voice_transcript_partial / voice: pir guard
  meta: kind=partial | timestamp=1778080495.1644828 | source=vosk | frequency_hz=360.0 | rms=305 | updated_at=1778080493.987201
- [2026-05-06 23:14:55] operator / voice_transcript_final / voice: pir guard
  meta: kind=final | timestamp=1778080495.9066386 | source=final | frequency_hz=360.0 | rms=305 | updated_at=1778080493.987201
- [2026-05-06 23:15:04] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1778080504.1457112 | source=vosk | frequency_hz=366.8 | rms=296 | updated_at=1778080503.1393585
- [2026-05-06 23:15:07] operator / voice_transcript_partial / voice: change your
  meta: kind=partial | timestamp=1778080507.173216 | source=vosk | frequency_hz=363.8 | rms=312 | updated_at=1778080506.1715338
- [2026-05-06 23:15:07] operator / voice_transcript_partial / voice: change your voice
  meta: kind=partial | timestamp=1778080507.4195523 | source=vosk | frequency_hz=363.8 | rms=312 | updated_at=1778080506.1715338
- [2026-05-06 23:15:07] operator / voice_transcript_partial / voice: change your voice to
  meta: kind=partial | timestamp=1778080507.92942 | source=vosk | frequency_hz=363.8 | rms=312 | updated_at=1778080506.1715338
- [2026-05-06 23:15:08] operator / voice_transcript_partial / voice: change your voice to elliot
  meta: kind=partial | timestamp=1778080508.1738784 | source=vosk | frequency_hz=363.8 | rms=312 | updated_at=1778080506.1715338
- [2026-05-06 23:15:08] operator / voice_transcript_partial / voice: change your voice to anything
  meta: kind=partial | timestamp=1778080508.440775 | source=vosk | frequency_hz=363.8 | rms=312 | updated_at=1778080506.1715338
- [2026-05-06 23:15:08] operator / voice_transcript_partial / voice: change your voice to elliot
  meta: kind=partial | timestamp=1778080508.7448566 | source=vosk | frequency_hz=363.8 | rms=312 | updated_at=1778080506.1715338
- [2026-05-06 23:15:08] operator / voice_transcript_partial / voice: change your voice to alien
  meta: kind=partial | timestamp=1778080508.94526 | source=vosk | frequency_hz=363.8 | rms=312 | updated_at=1778080506.1715338
- [2026-05-06 23:15:09] operator / voice_transcript_partial / voice: change your voice to alien movement
  meta: kind=partial | timestamp=1778080509.1429484 | source=vosk | frequency_hz=363.8 | rms=312 | updated_at=1778080506.1715338
- [2026-05-06 23:15:09] operator / voice_transcript_partial / voice: change your voice to alien manual
  meta: kind=partial | timestamp=1778080509.3899016 | source=vosk | frequency_hz=363.8 | rms=312 | updated_at=1778080506.1715338
- [2026-05-06 23:15:12] operator / voice_transcript_partial / voice: greeting
  meta: kind=partial | timestamp=1778080512.0136967 | source=vosk | frequency_hz=363.8 | rms=312 | updated_at=1778080506.1715338
- [2026-05-06 23:15:12] operator / voice_transcript_partial / voice: what's the
  meta: kind=partial | timestamp=1778080512.5310178 | source=vosk | frequency_hz=363.8 | rms=312 | updated_at=1778080506.1715338
- [2026-05-06 23:15:12] operator / voice_transcript_partial / voice: video display
  meta: kind=partial | timestamp=1778080512.7392333 | source=vosk | frequency_hz=363.8 | rms=312 | updated_at=1778080506.1715338
- [2026-05-06 23:15:13] operator / voice_transcript_partial / voice: you do you do
  meta: kind=partial | timestamp=1778080513.0668921 | source=vosk | frequency_hz=222.0 | rms=12051 | updated_at=1778080512.9963083
- [2026-05-06 23:15:13] operator / voice_transcript_final / voice: you do you do
  meta: kind=final | timestamp=1778080513.7418597 | source=final | frequency_hz=222.0 | rms=12051 | updated_at=1778080512.9963083
- [2026-05-06 23:15:22] operator / voice_transcript_partial / voice: change your
  meta: kind=partial | timestamp=1778080522.0652297 | source=vosk | frequency_hz=262.4 | rms=1202 | updated_at=1778080520.33239
- [2026-05-06 23:15:22] operator / voice_transcript_partial / voice: change your voice
  meta: kind=partial | timestamp=1778080522.3052003 | source=vosk | frequency_hz=262.4 | rms=1202 | updated_at=1778080520.33239
- [2026-05-06 23:15:22] operator / voice_transcript_partial / voice: change your voice to
  meta: kind=partial | timestamp=1778080522.5632756 | source=vosk | frequency_hz=262.4 | rms=1202 | updated_at=1778080520.33239
- [2026-05-06 23:15:22] operator / voice_transcript_partial / voice: change your voice to anything
  meta: kind=partial | timestamp=1778080522.8175344 | source=vosk | frequency_hz=262.4 | rms=1202 | updated_at=1778080520.33239
- [2026-05-06 23:15:23] operator / voice_transcript_partial / voice: change your voice to on alion
  meta: kind=partial | timestamp=1778080523.3124838 | source=vosk | frequency_hz=262.4 | rms=1202 | updated_at=1778080520.33239
- [2026-05-06 23:15:23] operator / voice_transcript_partial / voice: change your voice to on alion manual
  meta: kind=partial | timestamp=1778080523.6136239 | source=vosk | frequency_hz=262.4 | rms=1202 | updated_at=1778080520.33239
- [2026-05-06 23:15:23] operator / voice_transcript_partial / voice: change your voice to on alion make a
  meta: kind=partial | timestamp=1778080523.8398275 | source=vosk | frequency_hz=262.4 | rms=1202 | updated_at=1778080520.33239
- [2026-05-06 23:15:29] operator / voice_transcript_partial / voice: changes
  meta: kind=partial | timestamp=1778080529.7222111 | source=vosk | frequency_hz=255.5 | rms=1200 | updated_at=1778080529.7146618
- [2026-05-06 23:15:29] operator / voice_transcript_partial / voice: change your voice
  meta: kind=partial | timestamp=1778080529.961743 | source=vosk | frequency_hz=255.5 | rms=1200 | updated_at=1778080529.7146618
- [2026-05-06 23:15:31] operator / voice_transcript_partial / voice: change your voice to
  meta: kind=partial | timestamp=1778080531.0140054 | source=vosk | frequency_hz=255.5 | rms=1200 | updated_at=1778080529.7146618
- [2026-05-06 23:15:31] operator / voice_transcript_partial / voice: change your voice to anything
  meta: kind=partial | timestamp=1778080531.241146 | source=vosk | frequency_hz=255.5 | rms=1200 | updated_at=1778080529.7146618
- [2026-05-06 23:15:31] operator / voice_transcript_partial / voice: change your voice to anything deactivate
  meta: kind=partial | timestamp=1778080531.5190122 | source=vosk | frequency_hz=255.5 | rms=1200 | updated_at=1778080529.7146618
- [2026-05-06 23:15:31] operator / voice_transcript_partial / voice: change your voice to on alion
  meta: kind=partial | timestamp=1778080531.7345347 | source=vosk | frequency_hz=255.5 | rms=1200 | updated_at=1778080529.7146618
- [2026-05-06 23:15:33] operator / voice_transcript_partial / voice: change your voice to on alion me
  meta: kind=partial | timestamp=1778080533.0185344 | source=vosk | frequency_hz=196.0 | rms=1487 | updated_at=1778080532.9661405
- [2026-05-06 23:15:33] operator / voice_transcript_partial / voice: change your voice to on alion me off
  meta: kind=partial | timestamp=1778080533.1747787 | source=vosk | frequency_hz=165.2 | rms=628 | updated_at=1778080533.1587627
- [2026-05-06 23:15:35] operator / voice_transcript_partial / voice: eileen
  meta: kind=partial | timestamp=1778080535.387862 | source=vosk | frequency_hz=101.1 | rms=1205 | updated_at=1778080534.6296284
- [2026-05-06 23:15:35] operator / voice_transcript_partial / voice: eileen the logger
  meta: kind=partial | timestamp=1778080535.6689901 | source=vosk | frequency_hz=101.1 | rms=1205 | updated_at=1778080534.6296284
- [2026-05-06 23:15:35] operator / voice_transcript_partial / voice: eileen the logger is
  meta: kind=partial | timestamp=1778080535.8964245 | source=vosk | frequency_hz=186.1 | rms=691 | updated_at=1778080535.8802986
- [2026-05-06 23:15:37] operator / voice_transcript_partial / voice: system
  meta: kind=partial | timestamp=1778080537.1334012 | source=vosk | frequency_hz=149.8 | rms=682 | updated_at=1778080536.3970056
- [2026-05-06 23:15:37] operator / voice_transcript_partial / voice: system scan
  meta: kind=partial | timestamp=1778080537.6653514 | source=vosk | frequency_hz=174.4 | rms=676 | updated_at=1778080537.6230977
- [2026-05-06 23:15:38] operator / voice_transcript_final / voice: session scan
  meta: kind=final | timestamp=1778080538.320367 | source=final | frequency_hz=167.3 | rms=666 | updated_at=1778080538.122183
- [2026-05-06 23:15:41] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1778080541.4093637 | source=vosk | frequency_hz=216.5 | rms=864 | updated_at=1778080540.884458
- [2026-05-06 23:15:41] operator / voice_transcript_partial / voice: is assistant
  meta: kind=partial | timestamp=1778080541.62983 | source=vosk | frequency_hz=216.5 | rms=864 | updated_at=1778080540.884458
- [2026-05-06 23:15:42] operator / voice_transcript_partial / voice: is is system
  meta: kind=partial | timestamp=1778080542.163438 | source=vosk | frequency_hz=216.5 | rms=864 | updated_at=1778080540.884458
- [2026-05-06 23:15:42] operator / voice_transcript_partial / voice: is assistant is
  meta: kind=partial | timestamp=1778080542.379055 | source=vosk | frequency_hz=216.5 | rms=864 | updated_at=1778080540.884458
- [2026-05-06 23:15:42] operator / voice_transcript_partial / voice: is assistant is slew
  meta: kind=partial | timestamp=1778080542.630691 | source=vosk | frequency_hz=316.0 | rms=1201 | updated_at=1778080542.622677
- [2026-05-06 23:15:42] operator / voice_transcript_partial / voice: is assistant is slew order
  meta: kind=partial | timestamp=1778080542.8795402 | source=vosk | frequency_hz=286.6 | rms=1202 | updated_at=1778080542.8725276
- [2026-05-06 23:15:43] operator / voice_transcript_partial / voice: is assistant is movement
  meta: kind=partial | timestamp=1778080543.393685 | source=vosk | frequency_hz=286.6 | rms=1202 | updated_at=1778080542.8725276
- [2026-05-06 23:15:43] operator / voice_transcript_partial / voice: is assistant is slew
  meta: kind=partial | timestamp=1778080543.6773884 | source=vosk | frequency_hz=286.6 | rms=1202 | updated_at=1778080542.8725276
- [2026-05-06 23:15:43] operator / voice_transcript_partial / voice: is assistant is slew is keep
  meta: kind=partial | timestamp=1778080543.9123528 | source=vosk | frequency_hz=286.6 | rms=1202 | updated_at=1778080542.8725276
- [2026-05-06 23:15:44] operator / voice_transcript_partial / voice: is assistant is slew scan
  meta: kind=partial | timestamp=1778080544.1715367 | source=vosk | frequency_hz=313.0 | rms=1200 | updated_at=1778080544.1237621
- [2026-05-06 23:15:44] operator / voice_transcript_final / voice: is assistant is slew scan
  meta: kind=final | timestamp=1778080544.9195735 | source=final | frequency_hz=302.9 | rms=1201 | updated_at=1778080544.408785
- [2026-05-06 23:15:45] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778080545.1820421 | source=vosk | frequency_hz=262.4 | rms=1202 | updated_at=1778080545.1294837
- [2026-05-06 23:15:46] operator / voice_transcript_final / voice: guard
  meta: kind=final | timestamp=1778080546.0111704 | source=final | frequency_hz=235.8 | rms=1202 | updated_at=1778080545.6545575
- [2026-05-06 23:15:48] operator / voice_transcript_partial / voice: movement
  meta: kind=partial | timestamp=1778080548.0816717 | source=vosk | frequency_hz=287.5 | rms=1204 | updated_at=1778080548.0706596
- [2026-05-06 23:15:48] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1778080548.5792413 | source=vosk | frequency_hz=298.2 | rms=1200 | updated_at=1778080548.0938563
- [2026-05-06 23:15:49] operator / voice_transcript_final / voice: to
  meta: kind=final | timestamp=1778080549.6588964 | source=final | frequency_hz=293.2 | rms=722 | updated_at=1778080549.060086
- [2026-05-06 23:15:50] operator / voice_transcript_partial / voice: ai
  meta: kind=partial | timestamp=1778080550.2942493 | source=vosk | frequency_hz=329.9 | rms=1082 | updated_at=1778080550.0440044
- [2026-05-06 23:15:50] operator / voice_transcript_partial / voice: ai is
  meta: kind=partial | timestamp=1778080550.5609283 | source=vosk | frequency_hz=329.9 | rms=1082 | updated_at=1778080550.0440044
- [2026-05-06 23:15:50] operator / voice_transcript_partial / voice: ai is assistant
  meta: kind=partial | timestamp=1778080550.8298783 | source=vosk | frequency_hz=360.0 | rms=937 | updated_at=1778080550.8146908
- [2026-05-06 23:15:51] operator / voice_transcript_partial / voice: ai is scan
  meta: kind=partial | timestamp=1778080551.0385957 | source=vosk | frequency_hz=360.0 | rms=937 | updated_at=1778080550.8146908
- [2026-05-06 23:15:52] operator / voice_transcript_partial / voice: ai is scan is
  meta: kind=partial | timestamp=1778080552.0355213 | source=vosk | frequency_hz=378.0 | rms=1202 | updated_at=1778080551.5453045
- [2026-05-06 23:15:53] operator / voice_transcript_partial / voice: ai is scan is scope
  meta: kind=partial | timestamp=1778080553.2942166 | source=vosk | frequency_hz=381.5 | rms=1201 | updated_at=1778080552.2879927
- [2026-05-06 23:15:53] operator / voice_transcript_partial / voice: ai is scan is scan on
  meta: kind=partial | timestamp=1778080553.605631 | source=vosk | frequency_hz=362.1 | rms=1203 | updated_at=1778080553.5261364
- [2026-05-06 23:15:53] operator / voice_transcript_partial / voice: ai is scan is scope view
  meta: kind=partial | timestamp=1778080553.7884347 | source=vosk | frequency_hz=338.3 | rms=1201 | updated_at=1778080553.7819319
- [2026-05-06 23:15:54] operator / voice_transcript_partial / voice: ai is scan is scope e
  meta: kind=partial | timestamp=1778080554.3238902 | source=vosk | frequency_hz=343.7 | rms=994 | updated_at=1778080554.3069973
- [2026-05-06 23:15:54] operator / voice_transcript_partial / voice: ai is scan is scope e lion
  meta: kind=partial | timestamp=1778080554.7980752 | source=vosk | frequency_hz=357.8 | rms=1204 | updated_at=1778080554.529095
- [2026-05-06 23:15:55] operator / voice_transcript_partial / voice: ai is scan is scope e lion one
  meta: kind=partial | timestamp=1778080555.8166876 | source=vosk | frequency_hz=357.8 | rms=1204 | updated_at=1778080554.529095
- [2026-05-06 23:15:56] operator / voice_transcript_partial / voice: ai is scan is scope e lion one hello
  meta: kind=partial | timestamp=1778080556.0379567 | source=vosk | frequency_hz=357.8 | rms=1204 | updated_at=1778080554.529095
- [2026-05-06 23:15:56] operator / voice_transcript_partial / voice: ai is scan is scope e lion one
  meta: kind=partial | timestamp=1778080556.5736074 | source=vosk | frequency_hz=392.0 | rms=1200 | updated_at=1778080556.5665958
- [2026-05-06 23:15:57] operator / voice_transcript_partial / voice: ai is scan is scope e lion one aileen deactivate
  meta: kind=partial | timestamp=1778080557.0359266 | source=vosk | frequency_hz=392.0 | rms=1200 | updated_at=1778080556.5665958
- [2026-05-06 23:16:02] operator / voice_transcript_partial / voice: what local leon turn on
  meta: kind=partial | timestamp=1778080562.86786 | source=vosk | frequency_hz=195.7 | rms=614 | updated_at=1778080560.7815256
- [2026-05-06 23:16:12] operator / voice_transcript_partial / voice: target motion on what is
  meta: kind=partial | timestamp=1778080572.928782 | source=vosk | frequency_hz=248.2 | rms=966 | updated_at=1778080572.9170754
- [2026-05-06 23:16:13] operator / voice_transcript_final / voice: target motion auto anomaly is
  meta: kind=final | timestamp=1778080573.508064 | source=final | frequency_hz=191.4 | rms=688 | updated_at=1778080573.170982
- [2026-05-06 23:16:15] operator / voice_transcript_partial / voice: human
  meta: kind=partial | timestamp=1778080575.213401 | source=vosk | frequency_hz=280.0 | rms=723 | updated_at=1778080575.1650338
- [2026-05-06 23:16:15] operator / voice_transcript_partial / voice: human voice
  meta: kind=partial | timestamp=1778080575.6880493 | source=vosk | frequency_hz=280.0 | rms=723 | updated_at=1778080575.1650338
- [2026-05-06 23:16:15] operator / voice_transcript_partial / voice: human voice mode
  meta: kind=partial | timestamp=1778080575.9618073 | source=vosk | frequency_hz=278.6 | rms=713 | updated_at=1778080575.9572973
- [2026-05-06 23:16:16] operator / voice_transcript_partial / voice: human voice mode is
  meta: kind=partial | timestamp=1778080576.429848 | source=vosk | frequency_hz=309.2 | rms=730 | updated_at=1778080576.4136584
- [2026-05-06 23:16:16] operator / voice_transcript_partial / voice: human voice mode is on
  meta: kind=partial | timestamp=1778080576.7220497 | source=vosk | frequency_hz=299.0 | rms=704 | updated_at=1778080576.7035174
- [2026-05-06 23:16:16] operator / voice_transcript_partial / voice: human voice mode is on lion
  meta: kind=partial | timestamp=1778080576.955296 | source=vosk | frequency_hz=227.2 | rms=691 | updated_at=1778080576.9387665
- [2026-05-06 23:16:18] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1778080578.4435325 | source=vosk | frequency_hz=198.1 | rms=706 | updated_at=1778080577.1842053
- [2026-05-06 23:16:18] operator / voice_transcript_partial / voice: voice enabled
  meta: kind=partial | timestamp=1778080578.7161288 | source=vosk | frequency_hz=198.1 | rms=706 | updated_at=1778080577.1842053
- [2026-05-06 23:16:18] operator / voice_transcript_partial / voice: voice reports
  meta: kind=partial | timestamp=1778080578.9303756 | source=vosk | frequency_hz=198.1 | rms=706 | updated_at=1778080577.1842053
- [2026-05-06 23:16:19] operator / voice_transcript_partial / voice: voice on human
  meta: kind=partial | timestamp=1778080579.5402932 | source=vosk | frequency_hz=332.0 | rms=716 | updated_at=1778080579.1824539
- [2026-05-06 23:16:20] operator / voice_transcript_final / voice: voice reports
  meta: kind=final | timestamp=1778080580.7169409 | source=final | frequency_hz=332.0 | rms=716 | updated_at=1778080579.1824539
- [2026-05-06 23:16:26] operator / voice_transcript_partial / voice: face id
  meta: kind=partial | timestamp=1778080586.1437142 | source=vosk | frequency_hz=336.0 | rms=724 | updated_at=1778080585.895465
- [2026-05-06 23:16:27] operator / voice_transcript_partial / voice: say it the setting buzzer
  meta: kind=partial | timestamp=1778080587.924747 | source=vosk | frequency_hz=150.6 | rms=673 | updated_at=1778080587.9087343
- [2026-05-06 23:16:28] operator / voice_transcript_final / voice: say it the setting buzzer
  meta: kind=final | timestamp=1778080588.4647787 | source=final | frequency_hz=174.2 | rms=668 | updated_at=1778080588.151736
- [2026-05-06 23:16:40] operator / voice_transcript_partial / voice: what's face
  meta: kind=partial | timestamp=1778080600.1625948 | source=vosk | frequency_hz=190.2 | rms=557 | updated_at=1778080599.1258118
- [2026-05-06 23:16:40] operator / voice_transcript_partial / voice: what's faces active
  meta: kind=partial | timestamp=1778080600.6781137 | source=vosk | frequency_hz=196.0 | rms=546 | updated_at=1778080600.6227124
- [2026-05-06 23:16:40] operator / voice_transcript_partial / voice: what's face
  meta: kind=partial | timestamp=1778080600.8776028 | source=vosk | frequency_hz=196.0 | rms=546 | updated_at=1778080600.6227124
- [2026-05-06 23:16:42] operator / voice_transcript_partial / voice: what's face the one
  meta: kind=partial | timestamp=1778080602.585438 | source=vosk | frequency_hz=257.6 | rms=571 | updated_at=1778080601.6569853
- [2026-05-06 23:16:42] operator / voice_transcript_partial / voice: what's face the one repeat
  meta: kind=partial | timestamp=1778080602.640182 | source=vosk | frequency_hz=257.6 | rms=571 | updated_at=1778080601.6569853
- [2026-05-06 23:16:44] operator / voice_transcript_final / voice: what s face the one greeting
  meta: kind=final | timestamp=1778080604.1509922 | source=final | frequency_hz=107.5 | rms=554 | updated_at=1778080603.8464015
- [2026-05-06 23:16:45] operator / voice_transcript_partial / voice: speech
  meta: kind=partial | timestamp=1778080605.6138544 | source=vosk | frequency_hz=94.9 | rms=1200 | updated_at=1778080604.7795298
- [2026-05-06 23:16:45] operator / voice_transcript_partial / voice: speech disabled
  meta: kind=partial | timestamp=1778080605.7521477 | source=vosk | frequency_hz=94.9 | rms=1200 | updated_at=1778080604.7795298
- [2026-05-06 23:16:46] operator / voice_transcript_partial / voice: speech status
  meta: kind=partial | timestamp=1778080606.0435808 | source=vosk | frequency_hz=94.9 | rms=1200 | updated_at=1778080604.7795298
- [2026-05-06 23:16:46] operator / voice_transcript_final / voice: speech
  meta: kind=final | timestamp=1778080606.5665216 | source=final | frequency_hz=94.9 | rms=1200 | updated_at=1778080604.7795298
- [2026-05-06 23:16:50] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1778080610.064189 | source=vosk | frequency_hz=290.1 | rms=574 | updated_at=1778080609.4954166
- [2026-05-06 23:16:50] operator / voice_transcript_partial / voice: voice speech
  meta: kind=partial | timestamp=1778080610.269194 | source=vosk | frequency_hz=290.1 | rms=574 | updated_at=1778080609.4954166
- [2026-05-06 23:16:50] operator / voice_transcript_partial / voice: voice speech face
  meta: kind=partial | timestamp=1778080610.7938886 | source=vosk | frequency_hz=290.1 | rms=574 | updated_at=1778080609.4954166
- [2026-05-06 23:16:51] operator / voice_transcript_partial / voice: voice speech face loop
  meta: kind=partial | timestamp=1778080611.0091836 | source=vosk | frequency_hz=290.1 | rms=574 | updated_at=1778080609.4954166
- [2026-05-06 23:16:51] operator / voice_transcript_partial / voice: voice speech hey
  meta: kind=partial | timestamp=1778080611.2945778 | source=vosk | frequency_hz=290.1 | rms=574 | updated_at=1778080609.4954166
- [2026-05-06 23:16:51] operator / voice_transcript_partial / voice: voice speech
  meta: kind=partial | timestamp=1778080611.541335 | source=vosk | frequency_hz=290.1 | rms=574 | updated_at=1778080609.4954166
- [2026-05-06 23:16:51] operator / voice_transcript_partial / voice: voice speech replies
  meta: kind=partial | timestamp=1778080611.7730258 | source=vosk | frequency_hz=290.1 | rms=574 | updated_at=1778080609.4954166
- [2026-05-06 23:16:52] operator / voice_transcript_partial / voice: voice speech face greeting
  meta: kind=partial | timestamp=1778080612.0403383 | source=vosk | frequency_hz=290.1 | rms=574 | updated_at=1778080609.4954166
- [2026-05-06 23:16:52] operator / voice_transcript_partial / voice: voice speech face greeting gesture
  meta: kind=partial | timestamp=1778080612.67205 | source=vosk | frequency_hz=290.1 | rms=574 | updated_at=1778080609.4954166
- [2026-05-06 23:16:52] operator / voice_transcript_partial / voice: voice speech face greeting buzzer
  meta: kind=partial | timestamp=1778080612.7571568 | source=vosk | frequency_hz=290.1 | rms=574 | updated_at=1778080609.4954166
- [2026-05-06 23:16:53] operator / voice_transcript_final / voice: voice speech face buzzer
  meta: kind=final | timestamp=1778080613.8102796 | source=final | frequency_hz=165.2 | rms=550 | updated_at=1778080613.4941847
- [2026-05-06 23:16:59] operator / voice_transcript_partial / voice: logs
  meta: kind=partial | timestamp=1778080619.7612627 | source=vosk | frequency_hz=177.0 | rms=567 | updated_at=1778080618.7523463
- [2026-05-06 23:17:00] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1778080620.0381756 | source=vosk | frequency_hz=177.0 | rms=567 | updated_at=1778080618.7523463
- [2026-05-06 23:17:00] operator / voice_transcript_partial / voice: smart sentry human
  meta: kind=partial | timestamp=1778080620.580215 | source=vosk | frequency_hz=177.0 | rms=567 | updated_at=1778080618.7523463
- [2026-05-06 23:17:00] operator / voice_transcript_partial / voice: smart sentry human voice
  meta: kind=partial | timestamp=1778080620.8059905 | source=vosk | frequency_hz=177.0 | rms=567 | updated_at=1778080618.7523463
- [2026-05-06 23:17:01] operator / voice_transcript_partial / voice: smart sentry human voice mode
  meta: kind=partial | timestamp=1778080621.282253 | source=vosk | frequency_hz=177.0 | rms=567 | updated_at=1778080618.7523463
- [2026-05-06 23:17:01] operator / voice_transcript_partial / voice: smart sentry human voice order is
  meta: kind=partial | timestamp=1778080621.7979248 | source=vosk | frequency_hz=177.0 | rms=567 | updated_at=1778080618.7523463
- [2026-05-06 23:17:02] operator / voice_transcript_partial / voice: smart sentry human voice mode on
  meta: kind=partial | timestamp=1778080622.056098 | source=vosk | frequency_hz=177.0 | rms=567 | updated_at=1778080618.7523463
- [2026-05-06 23:17:02] operator / voice_transcript_partial / voice: smart sentry human voice mode on loss
  meta: kind=partial | timestamp=1778080622.266774 | source=vosk | frequency_hz=177.0 | rms=567 | updated_at=1778080618.7523463
- [2026-05-06 23:17:03] operator / voice_transcript_final / voice: smart sentry human voice mode is on
  meta: kind=final | timestamp=1778080623.0961347 | source=final | frequency_hz=140.0 | rms=533 | updated_at=1778080622.7428656
- [2026-05-06 23:17:04] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1778080624.067438 | source=vosk | frequency_hz=115.2 | rms=541 | updated_at=1778080623.800058
- [2026-05-06 23:17:04] operator / voice_transcript_partial / voice: what report human
  meta: kind=partial | timestamp=1778080624.8576138 | source=vosk | frequency_hz=115.2 | rms=541 | updated_at=1778080623.800058
- [2026-05-06 23:17:05] operator / voice_transcript_partial / voice: what report human voice
  meta: kind=partial | timestamp=1778080625.028263 | source=vosk | frequency_hz=115.2 | rms=541 | updated_at=1778080623.800058
- [2026-05-06 23:17:05] operator / voice_transcript_final / voice: what pir guard
  meta: kind=final | timestamp=1778080625.6966345 | source=final | frequency_hz=297.4 | rms=596 | updated_at=1778080625.5196486
- [2026-05-06 23:17:06] operator / voice_transcript_partial / voice: startup
  meta: kind=partial | timestamp=1778080626.0457413 | source=vosk | frequency_hz=297.4 | rms=596 | updated_at=1778080625.5196486
- [2026-05-06 23:17:06] operator / voice_transcript_partial / voice: start e lion
  meta: kind=partial | timestamp=1778080626.3155565 | source=vosk | frequency_hz=297.4 | rms=596 | updated_at=1778080625.5196486
- [2026-05-06 23:17:07] operator / voice_transcript_partial / voice: style guard
  meta: kind=partial | timestamp=1778080627.3535526 | source=vosk | frequency_hz=297.4 | rms=596 | updated_at=1778080625.5196486
- [2026-05-06 23:17:07] operator / voice_transcript_partial / voice: startup on close to
  meta: kind=partial | timestamp=1778080627.3746803 | source=vosk | frequency_hz=297.4 | rms=596 | updated_at=1778080625.5196486
- [2026-05-06 23:17:07] operator / voice_transcript_partial / voice: start auto speak cue
  meta: kind=partial | timestamp=1778080627.807258 | source=vosk | frequency_hz=297.4 | rms=596 | updated_at=1778080625.5196486
- [2026-05-06 23:17:08] operator / voice_transcript_final / voice: start auto speak cue
  meta: kind=final | timestamp=1778080628.947783 | source=final | frequency_hz=149.8 | rms=537 | updated_at=1778080628.7955399
- [2026-05-06 23:18:05] operator / voice_transcript_partial / voice: acoustic guard zone announcements
  meta: kind=partial | timestamp=1778080685.6981473 | source=vosk | frequency_hz=271.6 | rms=348 | updated_at=1778080679.1277254
- [2026-05-06 23:18:05] operator / voice_transcript_partial / voice: acoustic guard zone ml
  meta: kind=partial | timestamp=1778080685.907556 | source=vosk | frequency_hz=271.6 | rms=348 | updated_at=1778080679.1277254
- [2026-05-06 23:18:06] operator / voice_transcript_final / voice: acoustic guard zone ml
  meta: kind=final | timestamp=1778080686.9474833 | source=final | frequency_hz=407.6 | rms=347 | updated_at=1778080686.4057236
- [2026-05-06 23:18:07] operator / voice_transcript_partial / voice: fire is
  meta: kind=partial | timestamp=1778080687.1853814 | source=vosk | frequency_hz=407.6 | rms=347 | updated_at=1778080686.4057236
- [2026-05-06 23:18:07] operator / voice_transcript_partial / voice: fire disabled
  meta: kind=partial | timestamp=1778080687.417194 | source=vosk | frequency_hz=407.6 | rms=347 | updated_at=1778080686.4057236
- [2026-05-06 23:18:07] operator / voice_transcript_partial / voice: fire disabled abort
  meta: kind=partial | timestamp=1778080687.9795053 | source=vosk | frequency_hz=407.6 | rms=347 | updated_at=1778080686.4057236
- [2026-05-06 23:18:08] operator / voice_transcript_partial / voice: fire disabled abort current
  meta: kind=partial | timestamp=1778080688.1760538 | source=vosk | frequency_hz=407.6 | rms=347 | updated_at=1778080686.4057236
- [2026-05-06 23:18:08] operator / voice_transcript_partial / voice: fire disabled abort trace
  meta: kind=partial | timestamp=1778080688.4113805 | source=vosk | frequency_hz=407.6 | rms=347 | updated_at=1778080686.4057236
- [2026-05-06 23:18:08] operator / voice_transcript_partial / voice: fire disabled abort trace lion
  meta: kind=partial | timestamp=1778080688.6526558 | source=vosk | frequency_hz=360.0 | rms=338 | updated_at=1778080688.6444776
- [2026-05-06 23:18:09] operator / voice_transcript_partial / voice: fire disabled abort trace logger
  meta: kind=partial | timestamp=1778080689.687021 | source=vosk | frequency_hz=369.1 | rms=347 | updated_at=1778080688.9219825
- [2026-05-06 23:18:10] operator / voice_transcript_partial / voice: hey
  meta: kind=partial | timestamp=1778080690.76827 | source=vosk | frequency_hz=287.6 | rms=289 | updated_at=1778080689.9366689
- [2026-05-06 23:18:11] operator / voice_transcript_partial / voice: engaging
  meta: kind=partial | timestamp=1778080691.0040834 | source=vosk | frequency_hz=294.7 | rms=325 | updated_at=1778080690.980785
- [2026-05-06 23:18:11] operator / voice_transcript_partial / voice: engaging scope
  meta: kind=partial | timestamp=1778080691.22069 | source=vosk | frequency_hz=317.6 | rms=331 | updated_at=1778080691.2045836
- [2026-05-06 23:18:12] operator / voice_transcript_final / voice: engaging
  meta: kind=final | timestamp=1778080692.206282 | source=final | frequency_hz=323.6 | rms=332 | updated_at=1778080691.963304
- [2026-05-06 23:18:13] operator / voice_transcript_partial / voice: acoustic
  meta: kind=partial | timestamp=1778080693.9596999 | source=vosk | frequency_hz=294.4 | rms=326 | updated_at=1778080693.4575496
- [2026-05-06 23:18:14] operator / voice_transcript_partial / voice: acoustic guard
  meta: kind=partial | timestamp=1778080694.4885783 | source=vosk | frequency_hz=294.4 | rms=326 | updated_at=1778080693.4575496
- [2026-05-06 23:18:15] operator / voice_transcript_partial / voice: acoustic guard recognition
  meta: kind=partial | timestamp=1778080695.2224185 | source=vosk | frequency_hz=294.4 | rms=326 | updated_at=1778080693.4575496
- [2026-05-06 23:18:15] operator / voice_transcript_partial / voice: acoustic guard active
  meta: kind=partial | timestamp=1778080695.4908113 | source=vosk | frequency_hz=294.4 | rms=326 | updated_at=1778080693.4575496
- [2026-05-06 23:18:15] operator / voice_transcript_partial / voice: acoustic guard active on human
  meta: kind=partial | timestamp=1778080695.6945662 | source=vosk | frequency_hz=294.4 | rms=326 | updated_at=1778080693.4575496
- [2026-05-06 23:18:15] operator / voice_transcript_partial / voice: acoustic guard active on use large
  meta: kind=partial | timestamp=1778080695.9608765 | source=vosk | frequency_hz=294.4 | rms=326 | updated_at=1778080693.4575496
- [2026-05-06 23:18:16] operator / voice_transcript_partial / voice: acoustic guard active manual fire
  meta: kind=partial | timestamp=1778080696.2167346 | source=vosk | frequency_hz=294.4 | rms=326 | updated_at=1778080693.4575496
- [2026-05-06 23:18:16] operator / voice_transcript_partial / voice: acoustic guard active on use sound
  meta: kind=partial | timestamp=1778080696.480948 | source=vosk | frequency_hz=294.4 | rms=326 | updated_at=1778080693.4575496
- [2026-05-06 23:18:16] operator / voice_transcript_partial / voice: acoustic guard active on use zone
  meta: kind=partial | timestamp=1778080696.7424521 | source=vosk | frequency_hz=294.4 | rms=326 | updated_at=1778080693.4575496
- [2026-05-06 23:18:16] operator / voice_transcript_partial / voice: acoustic guard active on use zone of
  meta: kind=partial | timestamp=1778080696.9839256 | source=vosk | frequency_hz=294.4 | rms=326 | updated_at=1778080693.4575496
- [2026-05-06 23:18:17] operator / voice_transcript_partial / voice: acoustic guard active on use zone of of precision
  meta: kind=partial | timestamp=1778080697.507635 | source=vosk | frequency_hz=252.0 | rms=313 | updated_at=1778080697.4375806
- [2026-05-06 23:18:17] operator / voice_transcript_partial / voice: acoustic guard active on use zone of output e lion
  meta: kind=partial | timestamp=1778080697.7110126 | source=vosk | frequency_hz=266.0 | rms=324 | updated_at=1778080697.6867933
- [2026-05-06 23:18:18] operator / voice_transcript_final / voice: acoustic guard active on use voice zone of output
  meta: kind=final | timestamp=1778080698.4078095 | source=final | frequency_hz=266.7 | rms=328 | updated_at=1778080697.941075
- [2026-05-06 23:18:20] operator / voice_command / voice: acoustic guard active on use voice zone of output
  meta: normalized=True
- [2026-05-06 23:18:21] assistant / spoken_confirmation / voice: Done, switching now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 23:18:19] operator / voice_transcript_partial / voice: setting
  meta: kind=partial | timestamp=1778080699.56673 | source=vosk | frequency_hz=266.7 | rms=328 | updated_at=1778080697.941075
- [2026-05-06 23:18:20] operator / voice_transcript_partial / voice: setting is
  meta: kind=partial | timestamp=1778080700.2586815 | source=vosk | frequency_hz=266.7 | rms=328 | updated_at=1778080697.941075
- [2026-05-06 23:18:34] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1778080714.000539 | source=vosk | frequency_hz=255.3 | rms=324 | updated_at=1778080713.4794629
- [2026-05-06 23:18:39] operator / voice_transcript_final / voice: is
  meta: kind=final | timestamp=1778080719.8837218 | source=final | frequency_hz=208.0 | rms=324 | updated_at=1778080718.985172
- [2026-05-06 23:18:58] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1778080738.1478338 | source=vosk | frequency_hz=408.0 | rms=336 | updated_at=1778080736.3577356
- [2026-05-06 23:19:00] operator / voice_transcript_partial / voice: voice mode is on
  meta: kind=partial | timestamp=1778080740.1989477 | source=vosk | frequency_hz=408.0 | rms=336 | updated_at=1778080736.3577356
- [2026-05-06 23:19:00] operator / voice_transcript_final / voice: voice mode is on
  meta: kind=final | timestamp=1778080740.5587182 | source=final | frequency_hz=408.0 | rms=336 | updated_at=1778080736.3577356
- [2026-05-06 23:19:01] operator / voice_transcript_partial / voice: camera
  meta: kind=partial | timestamp=1778080741.4196005 | source=vosk | frequency_hz=408.0 | rms=336 | updated_at=1778080736.3577356
- [2026-05-06 23:19:01] operator / voice_transcript_partial / voice: ml
  meta: kind=partial | timestamp=1778080741.9920647 | source=vosk | frequency_hz=408.0 | rms=336 | updated_at=1778080736.3577356
- [2026-05-06 23:19:03] operator / voice_transcript_final / voice: ml
  meta: kind=final | timestamp=1778080743.0998769 | source=final | frequency_hz=264.0 | rms=926 | updated_at=1778080742.154881
- [2026-05-06 23:19:14] operator / voice_transcript_partial / voice: recent
  meta: kind=partial | timestamp=1778080754.1620684 | source=vosk | frequency_hz=303.1 | rms=344 | updated_at=1778080752.4060335
- [2026-05-06 23:19:14] operator / voice_transcript_partial / voice: recent video
  meta: kind=partial | timestamp=1778080754.4740303 | source=vosk | frequency_hz=303.1 | rms=344 | updated_at=1778080752.4060335
- [2026-05-06 23:19:14] operator / voice_transcript_partial / voice: e summaries
  meta: kind=partial | timestamp=1778080754.74711 | source=vosk | frequency_hz=303.1 | rms=344 | updated_at=1778080752.4060335
- [2026-05-06 23:19:14] operator / voice_transcript_partial / voice: recent buzzer
  meta: kind=partial | timestamp=1778080754.9709525 | source=vosk | frequency_hz=303.1 | rms=344 | updated_at=1778080752.4060335
- [2026-05-06 23:19:15] operator / voice_transcript_final / voice: recent buzzer
  meta: kind=final | timestamp=1778080755.9024596 | source=final | frequency_hz=308.0 | rms=314 | updated_at=1778080755.657622
- [2026-05-06 23:19:20] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1778080760.486883 | source=vosk
- [2026-05-06 23:19:22] operator / voice_transcript_final / voice: spare voice
  meta: kind=final | timestamp=1778080762.0470407 | source=final
- [2026-05-06 23:19:22] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1778080762.0740736 | source=vosk
- [2026-05-06 23:19:23] operator / voice_transcript_partial / voice: keep hunting
  meta: kind=partial | timestamp=1778080763.3509037 | source=vosk | frequency_hz=186.0 | rms=912 | updated_at=1778080762.820678
- [2026-05-06 23:19:23] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778080763.6347666 | source=vosk | frequency_hz=186.0 | rms=912 | updated_at=1778080762.820678
- [2026-05-06 23:19:23] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1778080763.8712525 | source=vosk | frequency_hz=186.0 | rms=912 | updated_at=1778080762.820678
- [2026-05-06 23:19:24] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1778080764.1160178 | source=vosk | frequency_hz=186.0 | rms=912 | updated_at=1778080762.820678
- [2026-05-06 23:19:24] operator / voice_transcript_partial / voice: current laser fire
  meta: kind=partial | timestamp=1778080764.348281 | source=vosk | frequency_hz=186.0 | rms=912 | updated_at=1778080762.820678
- [2026-05-06 23:19:25] operator / voice_transcript_final / voice: current laser fire off
  meta: kind=final | timestamp=1778080765.7071147 | source=final | frequency_hz=186.0 | rms=912 | updated_at=1778080762.820678
- [2026-05-06 23:19:27] operator / voice_transcript_partial / voice: pir order
  meta: kind=partial | timestamp=1778080767.1538801 | source=vosk | frequency_hz=224.1 | rms=555 | updated_at=1778080766.349183
- [2026-05-06 23:19:27] operator / voice_transcript_partial / voice: pir do you
  meta: kind=partial | timestamp=1778080767.3745596 | source=vosk | frequency_hz=224.1 | rms=555 | updated_at=1778080766.349183
- [2026-05-06 23:19:27] operator / voice_transcript_partial / voice: pir do you do
  meta: kind=partial | timestamp=1778080767.618904 | source=vosk | frequency_hz=224.1 | rms=555 | updated_at=1778080766.349183
- [2026-05-06 23:19:28] operator / voice_transcript_final / voice: pir do you do
  meta: kind=final | timestamp=1778080768.3552272 | source=final | frequency_hz=224.1 | rms=555 | updated_at=1778080766.349183
- [2026-05-06 23:19:35] operator / voice_transcript_partial / voice: hello view pointer
  meta: kind=partial | timestamp=1778080775.310458 | source=vosk | frequency_hz=269.4 | rms=318 | updated_at=1778080774.261555
- [2026-05-06 23:19:35] operator / voice_transcript_partial / voice: hello view pointer in queue
  meta: kind=partial | timestamp=1778080775.7882335 | source=vosk | frequency_hz=269.4 | rms=318 | updated_at=1778080774.261555
- [2026-05-06 23:19:36] operator / voice_transcript_final / voice: hello view pointer in queue
  meta: kind=final | timestamp=1778080776.8480818 | source=final | frequency_hz=300.0 | rms=319 | updated_at=1778080776.5513139
- [2026-05-06 23:19:49] operator / voice_transcript_partial / voice: order
  meta: kind=partial | timestamp=1778080789.2711682 | source=vosk | frequency_hz=292.1 | rms=328 | updated_at=1778080788.5243595
- [2026-05-06 23:19:49] operator / voice_transcript_partial / voice: order no keep
  meta: kind=partial | timestamp=1778080789.7603612 | source=vosk | frequency_hz=292.1 | rms=328 | updated_at=1778080788.5243595
- [2026-05-06 23:19:50] operator / voice_transcript_partial / voice: order no blink running
  meta: kind=partial | timestamp=1778080790.0543902 | source=vosk | frequency_hz=292.1 | rms=328 | updated_at=1778080788.5243595
- [2026-05-06 23:19:50] operator / voice_transcript_partial / voice: order no blink run pan
  meta: kind=partial | timestamp=1778080790.3037574 | source=vosk | frequency_hz=292.1 | rms=328 | updated_at=1778080788.5243595
- [2026-05-06 23:19:50] operator / voice_transcript_partial / voice: order deactivate runtime export
  meta: kind=partial | timestamp=1778080790.519477 | source=vosk | frequency_hz=292.1 | rms=328 | updated_at=1778080788.5243595
- [2026-05-06 23:19:50] operator / voice_transcript_partial / voice: order no blink run pan joke
  meta: kind=partial | timestamp=1778080790.841325 | source=vosk | frequency_hz=292.1 | rms=328 | updated_at=1778080788.5243595
- [2026-05-06 23:19:51] operator / voice_transcript_partial / voice: order no blink run pan joke order
  meta: kind=partial | timestamp=1778080791.2571979 | source=vosk | frequency_hz=292.1 | rms=328 | updated_at=1778080788.5243595
- [2026-05-06 23:19:51] operator / voice_transcript_partial / voice: order no blink run pan joke overlay
  meta: kind=partial | timestamp=1778080791.526014 | source=vosk | frequency_hz=292.1 | rms=328 | updated_at=1778080788.5243595
- [2026-05-06 23:19:51] operator / voice_transcript_partial / voice: order no blink run pan joke overlay disabled
  meta: kind=partial | timestamp=1778080791.7671225 | source=vosk | frequency_hz=292.1 | rms=328 | updated_at=1778080788.5243595
- [2026-05-06 23:19:52] operator / voice_transcript_partial / voice: order no blink run pan joke overlay you do
  meta: kind=partial | timestamp=1778080792.0454707 | source=vosk | frequency_hz=292.1 | rms=328 | updated_at=1778080788.5243595
- [2026-05-06 23:19:52] operator / voice_transcript_final / voice: order no blink run pan joke overlay you do
  meta: kind=final | timestamp=1778080792.7561834 | source=final | frequency_hz=292.1 | rms=328 | updated_at=1778080788.5243595
- [2026-05-06 23:19:55] operator / voice_transcript_partial / voice: spare output
  meta: kind=partial | timestamp=1778080795.2768738 | source=vosk | frequency_hz=291.8 | rms=325 | updated_at=1778080793.9984825
- [2026-05-06 23:19:55] operator / voice_transcript_partial / voice: spare loss
  meta: kind=partial | timestamp=1778080795.5464413 | source=vosk | frequency_hz=291.8 | rms=325 | updated_at=1778080793.9984825
- [2026-05-06 23:19:56] operator / voice_transcript_final / voice: spare loss
  meta: kind=final | timestamp=1778080796.2246988 | source=final | frequency_hz=287.4 | rms=328 | updated_at=1778080795.9933352
- [2026-05-06 23:19:59] operator / voice_transcript_partial / voice: face
  meta: kind=partial | timestamp=1778080799.5057018 | source=vosk | frequency_hz=291.0 | rms=331 | updated_at=1778080797.9924254
- [2026-05-06 23:20:00] operator / voice_transcript_partial / voice: face machine
  meta: kind=partial | timestamp=1778080800.0486486 | source=vosk | frequency_hz=291.0 | rms=331 | updated_at=1778080797.9924254
- [2026-05-06 23:20:00] operator / voice_transcript_partial / voice: face mask overlay
  meta: kind=partial | timestamp=1778080800.2576976 | source=vosk | frequency_hz=291.0 | rms=331 | updated_at=1778080797.9924254
- [2026-05-06 23:20:00] operator / voice_transcript_partial / voice: face mask
  meta: kind=partial | timestamp=1778080800.5507615 | source=vosk | frequency_hz=291.0 | rms=331 | updated_at=1778080797.9924254
- [2026-05-06 23:20:01] operator / voice_transcript_final / voice: face mask
  meta: kind=final | timestamp=1778080801.2871003 | source=final | frequency_hz=291.0 | rms=331 | updated_at=1778080797.9924254
- [2026-05-06 23:20:04] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1778080804.5231278 | source=vosk | frequency_hz=291.0 | rms=331 | updated_at=1778080797.9924254
- [2026-05-06 23:20:06] operator / voice_transcript_final / voice: on
  meta: kind=final | timestamp=1778080806.8072248 | source=final | frequency_hz=260.5 | rms=329 | updated_at=1778080805.952958
- [2026-05-06 23:20:08] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1778080808.2118442 | source=vosk | frequency_hz=280.6 | rms=330 | updated_at=1778080806.818741
- [2026-05-06 23:20:08] operator / voice_transcript_partial / voice: e leon
  meta: kind=partial | timestamp=1778080808.452721 | source=vosk | frequency_hz=280.6 | rms=330 | updated_at=1778080806.818741
- [2026-05-06 23:20:08] operator / voice_transcript_partial / voice: e leon mask trace
  meta: kind=partial | timestamp=1778080808.9820507 | source=vosk | frequency_hz=280.6 | rms=330 | updated_at=1778080806.818741
- [2026-05-06 23:20:09] operator / voice_transcript_partial / voice: e leon mask can you
  meta: kind=partial | timestamp=1778080809.2126596 | source=vosk | frequency_hz=280.6 | rms=330 | updated_at=1778080806.818741
- [2026-05-06 23:20:09] operator / voice_transcript_partial / voice: e leon mask cue
  meta: kind=partial | timestamp=1778080809.4802566 | source=vosk | frequency_hz=280.6 | rms=330 | updated_at=1778080806.818741
- [2026-05-06 23:20:09] operator / voice_transcript_partial / voice: e leon mask can you me a
  meta: kind=partial | timestamp=1778080809.715204 | source=vosk | frequency_hz=280.6 | rms=330 | updated_at=1778080806.818741
- [2026-05-06 23:20:10] operator / voice_transcript_partial / voice: e leon mask can you me a test
  meta: kind=partial | timestamp=1778080810.5780606 | source=vosk | frequency_hz=280.6 | rms=330 | updated_at=1778080806.818741
- [2026-05-06 23:20:10] operator / voice_transcript_partial / voice: e leon mask video display
  meta: kind=partial | timestamp=1778080810.6401427 | source=vosk | frequency_hz=240.0 | rms=323 | updated_at=1778080810.583572
- [2026-05-06 23:20:35] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778080835.1714404 | source=vosk | frequency_hz=352.2 | rms=335 | updated_at=1778080834.2020702
- [2026-05-06 23:21:16] operator / voice_transcript_partial / voice: tuning
  meta: kind=partial | timestamp=1778080876.4229243 | source=vosk | frequency_hz=343.8 | rms=315 | updated_at=1778080873.2088437
- [2026-05-06 23:21:16] operator / voice_transcript_partial / voice: keyboard
  meta: kind=partial | timestamp=1778080876.593376 | source=vosk | frequency_hz=343.8 | rms=315 | updated_at=1778080873.2088437
- [2026-05-06 23:21:16] operator / voice_transcript_partial / voice: keyboard movement
  meta: kind=partial | timestamp=1778080876.8684413 | source=vosk | frequency_hz=343.8 | rms=315 | updated_at=1778080873.2088437
- [2026-05-06 23:21:17] operator / voice_transcript_partial / voice: to loop another command
  meta: kind=partial | timestamp=1778080877.1104183 | source=vosk | frequency_hz=343.8 | rms=315 | updated_at=1778080873.2088437
- [2026-05-06 23:21:17] operator / voice_transcript_partial / voice: keyboard automatic
  meta: kind=partial | timestamp=1778080877.3605433 | source=vosk | frequency_hz=343.8 | rms=315 | updated_at=1778080873.2088437
- [2026-05-06 23:21:17] operator / voice_transcript_partial / voice: keyboard buzzer for human voice
  meta: kind=partial | timestamp=1778080877.8443968 | source=vosk | frequency_hz=343.8 | rms=315 | updated_at=1778080873.2088437
- [2026-05-06 23:21:18] operator / voice_transcript_final / voice: keyboard buzzer for human
  meta: kind=final | timestamp=1778080878.924065 | source=final | frequency_hz=343.8 | rms=315 | updated_at=1778080873.2088437
- [2026-05-06 23:21:20] operator / voice_transcript_partial / voice: requirement enabled
  meta: kind=partial | timestamp=1778080880.9270947 | source=vosk | frequency_hz=343.8 | rms=315 | updated_at=1778080873.2088437
- [2026-05-06 23:21:20] operator / voice_transcript_partial / voice: requirement
  meta: kind=partial | timestamp=1778080880.9476354 | source=vosk | frequency_hz=343.8 | rms=315 | updated_at=1778080873.2088437
- [2026-05-06 23:21:21] operator / voice_transcript_partial / voice: requirement disabled
  meta: kind=partial | timestamp=1778080881.1004713 | source=vosk | frequency_hz=343.8 | rms=315 | updated_at=1778080873.2088437
- [2026-05-06 23:21:21] operator / voice_transcript_partial / voice: requirement disabled to
  meta: kind=partial | timestamp=1778080881.640901 | source=vosk | frequency_hz=343.8 | rms=315 | updated_at=1778080873.2088437
- [2026-05-06 23:21:21] operator / voice_transcript_partial / voice: requirement disabled
  meta: kind=partial | timestamp=1778080881.8848228 | source=vosk | frequency_hz=343.8 | rms=315 | updated_at=1778080873.2088437
- [2026-05-06 23:21:22] operator / voice_transcript_final / voice: requirement disable
  meta: kind=final | timestamp=1778080882.301823 | source=final | frequency_hz=343.8 | rms=315 | updated_at=1778080873.2088437
- [2026-05-06 23:21:23] operator / voice_transcript_partial / voice: the hi
  meta: kind=partial | timestamp=1778080883.3045738 | source=vosk | frequency_hz=343.8 | rms=315 | updated_at=1778080873.2088437
- [2026-05-06 23:21:24] operator / voice_transcript_final / voice: the hi
  meta: kind=final | timestamp=1778080884.4738054 | source=final | frequency_hz=343.8 | rms=315 | updated_at=1778080873.2088437
- [2026-05-06 23:21:24] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1778080884.569733 | source=vosk | frequency_hz=343.8 | rms=315 | updated_at=1778080873.2088437
- [2026-05-06 23:21:24] operator / voice_transcript_partial / voice: leon
  meta: kind=partial | timestamp=1778080884.8727856 | source=vosk | frequency_hz=343.8 | rms=315 | updated_at=1778080873.2088437
- [2026-05-06 23:21:25] operator / voice_transcript_partial / voice: camera
  meta: kind=partial | timestamp=1778080885.0393336 | source=vosk | frequency_hz=300.0 | rms=326 | updated_at=1778080885.027141
- [2026-05-06 23:21:25] operator / voice_transcript_partial / voice: camera view
  meta: kind=partial | timestamp=1778080885.7816339 | source=vosk | frequency_hz=300.0 | rms=326 | updated_at=1778080885.027141
- [2026-05-06 23:21:26] operator / voice_transcript_partial / voice: camera view enabled
  meta: kind=partial | timestamp=1778080886.2935522 | source=vosk | frequency_hz=300.0 | rms=326 | updated_at=1778080885.027141
- [2026-05-06 23:21:26] operator / voice_transcript_partial / voice: camera alien leon
  meta: kind=partial | timestamp=1778080886.54604 | source=vosk | frequency_hz=300.0 | rms=326 | updated_at=1778080885.027141
- [2026-05-06 23:21:26] operator / voice_transcript_partial / voice: camera alien loop
  meta: kind=partial | timestamp=1778080886.7435944 | source=vosk | frequency_hz=300.0 | rms=326 | updated_at=1778080885.027141
- [2026-05-06 23:21:28] operator / voice_transcript_partial / voice: the pir voice
  meta: kind=partial | timestamp=1778080888.7979538 | source=vosk | frequency_hz=247.7 | rms=925 | updated_at=1778080888.0143206
- [2026-05-06 23:21:29] operator / voice_transcript_final / voice: voice
  meta: kind=final | timestamp=1778080889.8454475 | source=final | frequency_hz=247.7 | rms=925 | updated_at=1778080888.0143206
- [2026-05-06 23:21:31] operator / voice_transcript_partial / voice: acoustic
  meta: kind=partial | timestamp=1778080891.3068476 | source=vosk | frequency_hz=350.4 | rms=334 | updated_at=1778080890.2849624
- [2026-05-06 23:21:31] operator / voice_transcript_partial / voice: acoustic guard
  meta: kind=partial | timestamp=1778080891.774171 | source=vosk | frequency_hz=350.4 | rms=334 | updated_at=1778080890.2849624
- [2026-05-06 23:21:33] operator / voice_transcript_partial / voice: acoustic guard detection
  meta: kind=partial | timestamp=1778080893.1448548 | source=vosk | frequency_hz=350.4 | rms=334 | updated_at=1778080890.2849624
- [2026-05-06 23:21:33] operator / voice_transcript_partial / voice: acoustic guard detection on
  meta: kind=partial | timestamp=1778080893.2213655 | source=vosk | frequency_hz=350.4 | rms=334 | updated_at=1778080890.2849624
- [2026-05-06 23:21:33] operator / voice_transcript_partial / voice: acoustic guard detection on neutral
  meta: kind=partial | timestamp=1778080893.6111073 | source=vosk | frequency_hz=350.4 | rms=334 | updated_at=1778080890.2849624
- [2026-05-06 23:21:34] operator / voice_transcript_final / voice: acoustic guard detection on neutral
  meta: kind=final | timestamp=1778080894.2819743 | source=final | frequency_hz=280.2 | rms=330 | updated_at=1778080894.058336
- [2026-05-06 23:21:34] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778080894.613452 | source=vosk | frequency_hz=280.2 | rms=330 | updated_at=1778080894.058336
- [2026-05-06 23:21:34] operator / voice_transcript_partial / voice: the adaptive
  meta: kind=partial | timestamp=1778080894.8554685 | source=vosk | frequency_hz=280.2 | rms=330 | updated_at=1778080894.058336
- [2026-05-06 23:21:35] operator / voice_transcript_partial / voice: the no detection
  meta: kind=partial | timestamp=1778080895.518103 | source=vosk | frequency_hz=280.2 | rms=330 | updated_at=1778080894.058336
- [2026-05-06 23:21:35] operator / voice_transcript_partial / voice: the runtime
  meta: kind=partial | timestamp=1778080895.5863776 | source=vosk | frequency_hz=280.2 | rms=330 | updated_at=1778080894.058336
- [2026-05-06 23:21:35] operator / voice_transcript_final / voice: the no detection
  meta: kind=final | timestamp=1778080895.848409 | source=final | frequency_hz=280.2 | rms=330 | updated_at=1778080894.058336
- [2026-05-06 23:21:36] operator / voice_transcript_partial / voice: face
  meta: kind=partial | timestamp=1778080896.1236749 | source=vosk | frequency_hz=280.2 | rms=330 | updated_at=1778080894.058336
- [2026-05-06 23:21:36] operator / voice_transcript_partial / voice: face hello
  meta: kind=partial | timestamp=1778080896.6155298 | source=vosk | frequency_hz=280.2 | rms=330 | updated_at=1778080894.058336
- [2026-05-06 23:21:36] operator / voice_transcript_partial / voice: face current
  meta: kind=partial | timestamp=1778080896.886664 | source=vosk | frequency_hz=280.2 | rms=330 | updated_at=1778080894.058336
- [2026-05-06 23:21:37] operator / voice_transcript_partial / voice: face current status
  meta: kind=partial | timestamp=1778080897.094226 | source=vosk | frequency_hz=280.2 | rms=330 | updated_at=1778080894.058336
- [2026-05-06 23:21:37] operator / voice_transcript_partial / voice: face current speak
  meta: kind=partial | timestamp=1778080897.7766771 | source=vosk | frequency_hz=280.2 | rms=330 | updated_at=1778080894.058336
- [2026-05-06 23:21:37] operator / voice_transcript_partial / voice: face current speak guarding mode
  meta: kind=partial | timestamp=1778080897.9632366 | source=vosk | frequency_hz=280.2 | rms=330 | updated_at=1778080894.058336
- [2026-05-06 23:21:39] operator / voice_transcript_final / voice: face current speak guarding
  meta: kind=final | timestamp=1778080899.2162688 | source=final | frequency_hz=266.8 | rms=317 | updated_at=1778080898.9360235
- [2026-05-06 23:21:47] operator / voice_transcript_partial / voice: cleanup running
  meta: kind=partial | timestamp=1778080907.1976616 | source=vosk | frequency_hz=318.1 | rms=327 | updated_at=1778080905.4445708
- [2026-05-06 23:21:47] operator / voice_transcript_partial / voice: run acoustic
  meta: kind=partial | timestamp=1778080907.4393241 | source=vosk | frequency_hz=318.1 | rms=327 | updated_at=1778080905.4445708
- [2026-05-06 23:21:47] operator / voice_transcript_partial / voice: recovery smart
  meta: kind=partial | timestamp=1778080907.686536 | source=vosk | frequency_hz=318.1 | rms=327 | updated_at=1778080905.4445708
- [2026-05-06 23:21:47] operator / voice_transcript_partial / voice: recent logs
  meta: kind=partial | timestamp=1778080907.9378612 | source=vosk | frequency_hz=318.1 | rms=327 | updated_at=1778080905.4445708
- [2026-05-06 23:21:48] operator / voice_transcript_final / voice: recent replies
  meta: kind=final | timestamp=1778080908.6781683 | source=final | frequency_hz=288.0 | rms=322 | updated_at=1778080908.1802661
- [2026-05-06 23:22:06] operator / voice_transcript_partial / voice: the trigger
  meta: kind=partial | timestamp=1778080926.0676148 | source=vosk | frequency_hz=353.6 | rms=331 | updated_at=1778080924.173718
- [2026-05-06 23:22:07] operator / voice_transcript_final / voice: the trigger
  meta: kind=final | timestamp=1778080927.0389519 | source=final | frequency_hz=353.6 | rms=331 | updated_at=1778080924.173718
- [2026-05-06 23:22:09] operator / voice_transcript_partial / voice: trigger
  meta: kind=partial | timestamp=1778080929.160906 | source=vosk | frequency_hz=287.5 | rms=330 | updated_at=1778080929.1443858
- [2026-05-06 23:22:09] operator / voice_transcript_final / voice: trigger
  meta: kind=final | timestamp=1778080929.7701714 | source=final | frequency_hz=287.5 | rms=330 | updated_at=1778080929.1443858
- [2026-05-06 23:22:11] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1778080931.395694 | source=vosk | frequency_hz=309.1 | rms=310 | updated_at=1778080931.129011
- [2026-05-06 23:22:11] operator / voice_transcript_partial / voice: manual
  meta: kind=partial | timestamp=1778080931.9236212 | source=vosk | frequency_hz=343.7 | rms=390 | updated_at=1778080931.9060102
- [2026-05-06 23:22:12] operator / voice_transcript_partial / voice: mute
  meta: kind=partial | timestamp=1778080932.1956108 | source=vosk | frequency_hz=350.1 | rms=344 | updated_at=1778080932.1833405
- [2026-05-06 23:22:12] operator / voice_transcript_final / voice: mute
  meta: kind=final | timestamp=1778080932.9899049 | source=final | frequency_hz=324.3 | rms=324 | updated_at=1778080932.6734724
- [2026-05-06 23:22:58] operator / voice_transcript_partial / voice: off
  meta: kind=partial | timestamp=1778080978.6750793 | source=vosk | frequency_hz=151.9 | rms=211 | updated_at=1778080977.7014186
- [2026-05-06 23:22:58] operator / voice_transcript_partial / voice: of face
  meta: kind=partial | timestamp=1778080978.9205365 | source=vosk | frequency_hz=151.9 | rms=211 | updated_at=1778080977.7014186
- [2026-05-06 23:22:59] operator / voice_transcript_partial / voice: of face id
  meta: kind=partial | timestamp=1778080979.1592493 | source=vosk | frequency_hz=292.0 | rms=330 | updated_at=1778080979.1511967
- [2026-05-06 23:22:59] operator / voice_transcript_partial / voice: of face lion
  meta: kind=partial | timestamp=1778080979.7836578 | source=vosk | frequency_hz=292.0 | rms=330 | updated_at=1778080979.1511967
- [2026-05-06 23:22:59] operator / voice_transcript_partial / voice: of face hello
  meta: kind=partial | timestamp=1778080979.8980458 | source=vosk | frequency_hz=292.0 | rms=330 | updated_at=1778080979.1511967
- [2026-05-06 23:23:00] operator / voice_transcript_partial / voice: of face lion current status
  meta: kind=partial | timestamp=1778080980.1799905 | source=vosk | frequency_hz=292.0 | rms=330 | updated_at=1778080979.1511967
- [2026-05-06 23:23:11] operator / voice_transcript_partial / voice: pir guard
  meta: kind=partial | timestamp=1778080991.775948 | source=vosk | frequency_hz=350.9 | rms=893 | updated_at=1778080991.508836
- [2026-05-06 23:23:12] operator / voice_transcript_final / voice: pir
  meta: kind=final | timestamp=1778080992.680907 | source=final | frequency_hz=349.9 | rms=328 | updated_at=1778080992.037604
- [2026-05-06 23:23:15] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778080995.8129215 | source=vosk | frequency_hz=295.4 | rms=332 | updated_at=1778080993.5669177
- [2026-05-06 23:23:16] operator / voice_transcript_partial / voice: acoustic
  meta: kind=partial | timestamp=1778080996.0301538 | source=vosk | frequency_hz=295.4 | rms=332 | updated_at=1778080993.5669177
- [2026-05-06 23:23:33] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1778081013.5426059 | source=vosk | frequency_hz=281.8 | rms=337 | updated_at=1778081013.5263941
- [2026-05-06 23:23:37] operator / voice_transcript_partial / voice: acoustic
  meta: kind=partial | timestamp=1778081017.5199347 | source=vosk | frequency_hz=251.5 | rms=311 | updated_at=1778081016.786252
- [2026-05-06 23:23:37] operator / voice_transcript_partial / voice: acoustic guard
  meta: kind=partial | timestamp=1778081017.828265 | source=vosk | frequency_hz=251.5 | rms=311 | updated_at=1778081016.786252
- [2026-05-06 23:23:38] operator / voice_transcript_partial / voice: acoustic guard detection
  meta: kind=partial | timestamp=1778081018.1694276 | source=vosk | frequency_hz=251.5 | rms=311 | updated_at=1778081016.786252
- [2026-05-06 23:23:38] operator / voice_transcript_partial / voice: acoustic guard detection on
  meta: kind=partial | timestamp=1778081018.5198655 | source=vosk | frequency_hz=251.5 | rms=311 | updated_at=1778081016.786252
- [2026-05-06 23:23:38] operator / voice_transcript_partial / voice: acoustic guard detection on use
  meta: kind=partial | timestamp=1778081018.777003 | source=vosk | frequency_hz=251.5 | rms=311 | updated_at=1778081016.786252
- [2026-05-06 23:23:39] operator / voice_transcript_partial / voice: acoustic guard detection on neutral
  meta: kind=partial | timestamp=1778081019.0232296 | source=vosk | frequency_hz=251.5 | rms=311 | updated_at=1778081016.786252
- [2026-05-06 23:23:39] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound
  meta: kind=partial | timestamp=1778081019.321054 | source=vosk | frequency_hz=251.5 | rms=311 | updated_at=1778081016.786252
- [2026-05-06 23:23:39] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound active
  meta: kind=partial | timestamp=1778081019.791889 | source=vosk | frequency_hz=251.5 | rms=311 | updated_at=1778081016.786252
- [2026-05-06 23:23:40] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound mask trace
  meta: kind=partial | timestamp=1778081020.0398152 | source=vosk | frequency_hz=251.5 | rms=311 | updated_at=1778081016.786252
- [2026-05-06 23:23:40] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of accessory
  meta: kind=partial | timestamp=1778081020.2751336 | source=vosk | frequency_hz=251.5 | rms=311 | updated_at=1778081016.786252
- [2026-05-06 23:23:40] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of accessory hey
  meta: kind=partial | timestamp=1778081020.7953105 | source=vosk | frequency_hz=251.5 | rms=311 | updated_at=1778081016.786252
- [2026-05-06 23:23:41] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of accessory disabled
  meta: kind=partial | timestamp=1778081021.0389898 | source=vosk | frequency_hz=251.5 | rms=311 | updated_at=1778081016.786252
- [2026-05-06 23:23:41] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of accessory hey disable
  meta: kind=partial | timestamp=1778081021.5609553 | source=vosk | frequency_hz=251.5 | rms=311 | updated_at=1778081016.786252
- [2026-05-06 23:23:41] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of accessory hey disable the current
  meta: kind=partial | timestamp=1778081021.8262277 | source=vosk | frequency_hz=251.5 | rms=311 | updated_at=1778081016.786252
- [2026-05-06 23:23:42] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of accessory hey disable the current operator
  meta: kind=partial | timestamp=1778081022.3465319 | source=vosk | frequency_hz=251.5 | rms=311 | updated_at=1778081016.786252
- [2026-05-06 23:23:42] operator / voice_transcript_partial / voice: acoustic guard detection on neutral sound of accessory hey disable the current are you
  meta: kind=partial | timestamp=1778081022.5431864 | source=vosk | frequency_hz=251.5 | rms=311 | updated_at=1778081016.786252
- [2026-05-06 23:23:43] operator / voice_transcript_final / voice: acoustic guard detection on neutral sound of accessory hey disable the current are you
  meta: kind=final | timestamp=1778081023.8613226 | source=final | frequency_hz=251.5 | rms=311 | updated_at=1778081016.786252
- [2026-05-06 23:23:44] operator / voice_transcript_partial / voice: greeting
  meta: kind=partial | timestamp=1778081024.2694016 | source=vosk | frequency_hz=251.5 | rms=311 | updated_at=1778081016.786252
- [2026-05-06 23:23:45] operator / voice_transcript_final / voice: greeting
  meta: kind=final | timestamp=1778081025.523342 | source=final | frequency_hz=319.2 | rms=915 | updated_at=1778081025.2652757
- [2026-05-06 23:23:47] operator / voice_transcript_partial / voice: on
  meta: kind=partial | timestamp=1778081027.005151 | source=vosk | frequency_hz=314.6 | rms=909 | updated_at=1778081026.0133488
- [2026-05-06 23:23:47] operator / voice_transcript_partial / voice: leon
  meta: kind=partial | timestamp=1778081027.530657 | source=vosk | frequency_hz=314.6 | rms=909 | updated_at=1778081026.0133488
- [2026-05-06 23:24:02] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778081042.3172812 | source=vosk | frequency_hz=316.1 | rms=768 | updated_at=1778081034.3193285
- [2026-05-06 23:25:06] operator / voice_transcript_partial / voice: guard detection on neutral sound off for one
  meta: kind=partial | timestamp=1778081106.4093828 | source=vosk | frequency_hz=288.2 | rms=352 | updated_at=1778081102.431613
- [2026-05-06 23:25:06] operator / voice_transcript_partial / voice: guard detection on neutral sound off for one disable the
  meta: kind=partial | timestamp=1778081106.863976 | source=vosk | frequency_hz=288.2 | rms=352 | updated_at=1778081102.431613
- [2026-05-06 23:25:07] operator / voice_transcript_partial / voice: guard detection on neutral sound off for one disabled off
  meta: kind=partial | timestamp=1778081107.1298025 | source=vosk | frequency_hz=288.2 | rms=352 | updated_at=1778081102.431613
- [2026-05-06 23:25:07] operator / voice_transcript_partial / voice: guard detection on neutral sound off for one disable the known faces
  meta: kind=partial | timestamp=1778081107.4090116 | source=vosk | frequency_hz=288.2 | rms=352 | updated_at=1778081102.431613
- [2026-05-06 23:25:07] operator / voice_transcript_partial / voice: guard detection on neutral sound off for one disable the known face
  meta: kind=partial | timestamp=1778081107.6491542 | source=vosk | frequency_hz=320.0 | rms=322 | updated_at=1778081107.64315
- [2026-05-06 23:25:07] operator / voice_transcript_partial / voice: guard detection on neutral sound off for one disable the known face lion
  meta: kind=partial | timestamp=1778081107.9131033 | source=vosk | frequency_hz=320.0 | rms=322 | updated_at=1778081107.64315
- [2026-05-06 23:25:08] operator / voice_transcript_partial / voice: guard detection on neutral sound off for one disable the known face lion turn
  meta: kind=partial | timestamp=1778081108.3833747 | source=vosk | frequency_hz=320.0 | rms=322 | updated_at=1778081107.64315
- [2026-05-06 23:25:08] operator / voice_transcript_partial / voice: guard detection on neutral sound off for one disable the known face lion current status
  meta: kind=partial | timestamp=1778081108.6670592 | source=vosk | frequency_hz=320.0 | rms=322 | updated_at=1778081107.64315
- [2026-05-06 23:25:09] operator / voice_transcript_partial / voice: guard detection on neutral sound off for one disable the known face lion current status engaging scope
  meta: kind=partial | timestamp=1778081109.8306623 | source=vosk | frequency_hz=418.0 | rms=324 | updated_at=1778081109.3564196
- [2026-05-06 23:25:11] operator / voice_transcript_final / voice: elion guard detection on neutral sound off for one disable the known face lion current status engaging
  meta: kind=final | timestamp=1778081111.9743457 | source=final | frequency_hz=418.0 | rms=324 | updated_at=1778081109.3564196
- [2026-05-06 23:25:14] operator / voice_command / voice: guard detection on neutral sound off for one disable the known face lion current status engaging
  meta: normalized=True
- [2026-05-06 23:25:16] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 23:25:22] operator / voice_transcript_partial / voice: face current status
  meta: kind=partial | timestamp=1778081122.5156178 | source=vosk | frequency_hz=328.0 | rms=331 | updated_at=1778081119.4842362
- [2026-05-06 23:25:23] operator / voice_transcript_partial / voice: face current status i have
  meta: kind=partial | timestamp=1778081123.2258472 | source=vosk | frequency_hz=328.0 | rms=331 | updated_at=1778081119.4842362
- [2026-05-06 23:25:23] operator / voice_transcript_partial / voice: face current status i have a
  meta: kind=partial | timestamp=1778081123.511585 | source=vosk | frequency_hz=328.0 | rms=331 | updated_at=1778081119.4842362
- [2026-05-06 23:25:23] operator / voice_transcript_partial / voice: face current status i have a question
  meta: kind=partial | timestamp=1778081123.7567315 | source=vosk | frequency_hz=328.0 | rms=331 | updated_at=1778081119.4842362
- [2026-05-06 23:25:24] operator / voice_transcript_partial / voice: face current status i have a question on
  meta: kind=partial | timestamp=1778081124.7339149 | source=vosk | frequency_hz=420.0 | rms=340 | updated_at=1778081124.0056856
- [2026-05-06 23:25:25] operator / voice_transcript_partial / voice: face current status i have a question overlay the
  meta: kind=partial | timestamp=1778081125.0741606 | source=vosk | frequency_hz=420.0 | rms=340 | updated_at=1778081124.0056856
- [2026-05-06 23:25:25] operator / voice_transcript_partial / voice: face current status i have a question overlay the recognition
  meta: kind=partial | timestamp=1778081125.2391179 | source=vosk | frequency_hz=420.0 | rms=340 | updated_at=1778081124.0056856
- [2026-05-06 23:25:25] operator / voice_transcript_partial / voice: face current status i have a question overlay the rest on
  meta: kind=partial | timestamp=1778081125.5309315 | source=vosk | frequency_hz=420.0 | rms=340 | updated_at=1778081124.0056856
- [2026-05-06 23:25:25] operator / voice_transcript_partial / voice: face current status i have a question overlay the rest on operator
  meta: kind=partial | timestamp=1778081125.991872 | source=vosk | frequency_hz=420.0 | rms=340 | updated_at=1778081124.0056856
- [2026-05-06 23:25:26] operator / voice_transcript_partial / voice: face current status i have a question overlay the rest on operator changes
  meta: kind=partial | timestamp=1778081126.5237842 | source=vosk | frequency_hz=420.0 | rms=340 | updated_at=1778081124.0056856
- [2026-05-06 23:25:26] operator / voice_transcript_partial / voice: face current status i have a question overlay the rest on operator changes model
  meta: kind=partial | timestamp=1778081126.7932618 | source=vosk | frequency_hz=420.0 | rms=340 | updated_at=1778081124.0056856
- [2026-05-06 23:25:27] operator / voice_transcript_partial / voice: face current status i have a question overlay the rest on operator changes on assistant
  meta: kind=partial | timestamp=1778081127.0059028 | source=vosk | frequency_hz=420.0 | rms=340 | updated_at=1778081124.0056856
- [2026-05-06 23:25:27] operator / voice_transcript_partial / voice: face current status i have a question overlay the rest on operator changes smart sentry
  meta: kind=partial | timestamp=1778081127.2954936 | source=vosk | frequency_hz=420.0 | rms=340 | updated_at=1778081124.0056856
- [2026-05-06 23:25:27] operator / voice_transcript_partial / voice: face current status i have a question overlay the rest on operator changes smart sentry setting
  meta: kind=partial | timestamp=1778081127.545027 | source=vosk | frequency_hz=420.0 | rms=340 | updated_at=1778081124.0056856
- [2026-05-06 23:25:27] operator / voice_transcript_partial / voice: face current status i have a question overlay the rest on operator changes smart sentry setting drafts
  meta: kind=partial | timestamp=1778081127.7910035 | source=vosk | frequency_hz=420.0 | rms=340 | updated_at=1778081124.0056856
- [2026-05-06 23:25:29] operator / voice_transcript_final / voice: face current status i have a question overlay the rest on operator changes smart sentry lighting
  meta: kind=final | timestamp=1778081129.0530834 | source=final | frequency_hz=339.1 | rms=330 | updated_at=1778081128.2225804
- [2026-05-06 23:25:29] operator / voice_transcript_partial / voice: movement
  meta: kind=partial | timestamp=1778081129.7643049 | source=vosk | frequency_hz=339.1 | rms=330 | updated_at=1778081128.2225804
- [2026-05-06 23:25:29] operator / voice_transcript_partial / voice: open
  meta: kind=partial | timestamp=1778081129.992402 | source=vosk | frequency_hz=339.1 | rms=330 | updated_at=1778081128.2225804
- [2026-05-06 23:25:30] operator / voice_transcript_final / voice: open
  meta: kind=final | timestamp=1778081130.9869797 | source=final | frequency_hz=339.1 | rms=330 | updated_at=1778081128.2225804
- [2026-05-06 23:25:32] operator / voice_transcript_partial / voice: anything else
  meta: kind=partial | timestamp=1778081132.7532444 | source=vosk | frequency_hz=263.4 | rms=332 | updated_at=1778081131.4717338
- [2026-05-06 23:25:33] operator / voice_transcript_partial / voice: anything current
  meta: kind=partial | timestamp=1778081133.0243714 | source=vosk | frequency_hz=380.0 | rms=359 | updated_at=1778081133.0183656
- [2026-05-06 23:25:33] operator / voice_transcript_partial / voice: anything are you
  meta: kind=partial | timestamp=1778081133.2556124 | source=vosk | frequency_hz=380.0 | rms=359 | updated_at=1778081133.0183656
- [2026-05-06 23:25:33] operator / voice_transcript_final / voice: anything guard
  meta: kind=final | timestamp=1778081133.9008708 | source=final | frequency_hz=380.0 | rms=359 | updated_at=1778081133.0183656
- [2026-05-06 23:25:35] operator / voice_transcript_partial / voice: recent
  meta: kind=partial | timestamp=1778081135.535351 | source=vosk | frequency_hz=276.6 | rms=308 | updated_at=1778081134.7280204
- [2026-05-06 23:25:36] operator / voice_transcript_partial / voice: slew order
  meta: kind=partial | timestamp=1778081136.8025835 | source=vosk | frequency_hz=276.6 | rms=308 | updated_at=1778081134.7280204
- [2026-05-06 23:25:36] operator / voice_transcript_partial / voice: slew what
  meta: kind=partial | timestamp=1778081136.8644185 | source=vosk | frequency_hz=276.6 | rms=308 | updated_at=1778081134.7280204
- [2026-05-06 23:25:37] operator / voice_transcript_partial / voice: resume guarding
  meta: kind=partial | timestamp=1778081137.3505075 | source=vosk | frequency_hz=276.6 | rms=308 | updated_at=1778081134.7280204
- [2026-05-06 23:25:37] operator / voice_transcript_partial / voice: slew order
  meta: kind=partial | timestamp=1778081137.6064267 | source=vosk | frequency_hz=242.0 | rms=892 | updated_at=1778081137.6004162
- [2026-05-06 23:25:38] operator / voice_transcript_final / voice: slew order
  meta: kind=final | timestamp=1778081138.275488 | source=final | frequency_hz=242.0 | rms=892 | updated_at=1778081137.6004162

# SMART SENTRY V5.0.0 Runtime Conversation Export

- Generated: 2026-08-22 13:42:55
- Entries: 400
- Roles: {'assistant': 4, 'system': 348, 'operator': 48}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 348, 'spoken_confirmation': 2, 'voice_transcript_partial': 39, 'voice_transcript_final': 8, 'voice_command': 1}
- Channels: {'text': 2, 'voice': 398}
- Latest operator request: show me the a tutti settings
- Latest assistant message: Running Smart Sentry now. Connecting the Smart Sentry boards first.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-08-22 13:34:56] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-08-22 13:34:56] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-08-22 13:35:01] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787376901.7548242 | source=vosk
- [2026-08-22 13:35:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376904.2283297 | source=vosk | rms=303 | updated_at=1787376904.2283297
- [2026-08-22 13:35:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376904.7166002 | source=vosk | rms=303 | updated_at=1787376904.2283297
- [2026-08-22 13:35:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376909.431458 | source=vosk | rms=303 | updated_at=1787376904.2283297
- [2026-08-22 13:35:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376909.928229 | source=vosk | rms=303 | updated_at=1787376904.2283297
- [2026-08-22 13:35:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376910.222787 | source=vosk | rms=303 | updated_at=1787376904.2283297
- [2026-08-22 13:35:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376910.677614 | source=vosk | rms=303 | updated_at=1787376904.2283297
- [2026-08-22 13:35:42] assistant / spoken_confirmation / voice: Smart Sentry is ready.
  meta: interrupt=True | assistant_output=False | spoken=True
- [2026-08-22 13:35:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376917.9282804 | source=vosk | rms=174 | updated_at=1787376917.9282804
- [2026-08-22 13:35:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376919.4269793 | source=vosk | rms=174 | updated_at=1787376917.9282804
- [2026-08-22 13:35:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376921.428257 | source=vosk | rms=278 | updated_at=1787376921.428257
- [2026-08-22 13:35:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376921.9277823 | source=vosk | rms=278 | updated_at=1787376921.428257
- [2026-08-22 13:35:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376933.17789 | source=vosk | rms=165 | updated_at=1787376933.17789
- [2026-08-22 13:35:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376933.9283025 | source=vosk | rms=165 | updated_at=1787376933.4289227
- [2026-08-22 13:35:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376936.9284265 | source=vosk | rms=165 | updated_at=1787376933.4289227
- [2026-08-22 13:35:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376938.4272747 | source=vosk | rms=161 | updated_at=1787376937.9283774
- [2026-08-22 13:35:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376942.7614708 | source=vosk | rms=161 | updated_at=1787376937.9283774
- [2026-08-22 13:35:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376943.2527943 | source=vosk | rms=161 | updated_at=1787376937.9283774
- [2026-08-22 13:35:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376944.181964 | source=vosk | rms=161 | updated_at=1787376937.9283774
- [2026-08-22 13:35:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376944.7490993 | source=vosk | rms=161 | updated_at=1787376937.9283774
- [2026-08-22 13:35:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376947.2500517 | source=vosk | rms=132 | updated_at=1787376947.2500517
- [2026-08-22 13:35:47] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1787376947.9592447 | source=vosk | rms=458 | updated_at=1787376947.928492
- [2026-08-22 13:35:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376948.1784344 | source=vosk | rms=650 | updated_at=1787376948.1784344
- [2026-08-22 13:35:48] operator / voice_transcript_partial / voice: smart century
  meta: kind=partial | timestamp=1787376948.2495298 | source=vosk | rms=650 | updated_at=1787376948.1784344
- [2026-08-22 13:35:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376948.4285197 | source=vosk | rms=580 | updated_at=1787376948.4285197
- [2026-08-22 13:35:48] operator / voice_transcript_partial / voice: smart century is
  meta: kind=partial | timestamp=1787376948.489673 | source=vosk | rms=580 | updated_at=1787376948.4285197
- [2026-08-22 13:35:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376949.4202063 | source=vosk | rms=580 | updated_at=1787376948.4285197
- [2026-08-22 13:35:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376950.9074926 | source=vosk | rms=580 | updated_at=1787376948.4285197
- [2026-08-22 13:35:50] operator / voice_transcript_partial / voice: smart century is ready
  meta: kind=partial | timestamp=1787376950.935813 | source=vosk | rms=580 | updated_at=1787376948.4285197
- [2026-08-22 13:35:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376951.163278 | source=vosk | rms=753 | updated_at=1787376951.163278
- [2026-08-22 13:35:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376951.4095109 | source=vosk | rms=336 | updated_at=1787376951.4095109
- [2026-08-22 13:35:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376951.6586027 | source=vosk | rms=661 | updated_at=1787376951.6586027
- [2026-08-22 13:35:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376951.912007 | source=vosk | rms=687 | updated_at=1787376951.912007
- [2026-08-22 13:35:52] operator / voice_transcript_final / voice: smart sentry is ready
  meta: kind=final | timestamp=1787376952.4078174 | source=final | rms=687 | updated_at=1787376951.912007
- [2026-08-22 13:35:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376952.5421333 | source=vosk | rms=687 | updated_at=1787376951.912007
- [2026-08-22 13:35:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376952.5421333 | source=vosk | rms=424 | updated_at=1787376952.5421333
- [2026-08-22 13:35:56] operator / voice_transcript_partial / voice: i couldn't
  meta: kind=partial | timestamp=1787376956.0431786 | source=vosk | rms=612 | updated_at=1787376955.4077685
- [2026-08-22 13:35:56] operator / voice_transcript_partial / voice: i could have been
  meta: kind=partial | timestamp=1787376956.2151446 | source=vosk | rms=458 | updated_at=1787376956.0431786
- [2026-08-22 13:35:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376956.3330083 | source=vosk | rms=319 | updated_at=1787376956.2151446
- [2026-08-22 13:35:56] operator / voice_transcript_partial / voice: i could have a box
  meta: kind=partial | timestamp=1787376956.3330083 | source=vosk | rms=319 | updated_at=1787376956.2151446
- [2026-08-22 13:35:56] operator / voice_transcript_partial / voice: i could have a box or
  meta: kind=partial | timestamp=1787376956.4595304 | source=vosk | rms=319 | updated_at=1787376956.2151446
- [2026-08-22 13:35:56] operator / voice_transcript_partial / voice: i could have a box or to
  meta: kind=partial | timestamp=1787376956.5017812 | source=vosk | rms=299 | updated_at=1787376956.4595304
- [2026-08-22 13:35:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376957.1272643 | source=vosk | rms=363 | updated_at=1787376957.1272643
- [2026-08-22 13:35:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376957.4641483 | source=vosk | rms=247 | updated_at=1787376957.4641483
- [2026-08-22 13:35:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376957.708159 | source=vosk | rms=230 | updated_at=1787376957.708159
- [2026-08-22 13:35:58] operator / voice_transcript_final / voice: i could have a box or two
  meta: kind=final | timestamp=1787376958.4227893 | source=final | rms=230 | updated_at=1787376957.708159
- [2026-08-22 13:35:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376958.5557172 | source=vosk | rms=230 | updated_at=1787376957.708159
- [2026-08-22 13:35:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376958.5557172 | source=vosk | rms=494 | updated_at=1787376958.5557172
- [2026-08-22 13:35:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376959.56097 | source=vosk | rms=1101 | updated_at=1787376958.7276483
- [2026-08-22 13:35:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376959.56097 | source=vosk | rms=743 | updated_at=1787376959.56097
- [2026-08-22 13:36:03] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1787376963.842388 | source=final | rms=1990 | updated_at=1787376963.4103336 | frequency_hz=213.0
- [2026-08-22 13:36:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376963.8880587 | source=vosk | rms=1990 | updated_at=1787376963.4103336 | frequency_hz=213.0
- [2026-08-22 13:36:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376963.8880587 | source=vosk | rms=3137 | updated_at=1787376963.8880587 | frequency_hz=213.0
- [2026-08-22 13:36:03] operator / voice_transcript_partial / voice: run the
  meta: kind=partial | timestamp=1787376963.9716659 | source=vosk | rms=3222 | updated_at=1787376963.9515104 | frequency_hz=213.0
- [2026-08-22 13:36:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376964.1603868 | source=vosk | rms=2638 | updated_at=1787376964.1603868 | frequency_hz=213.0
- [2026-08-22 13:36:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376964.4114695 | source=vosk | rms=2563 | updated_at=1787376964.4114695 | frequency_hz=213.0
- [2026-08-22 13:36:04] operator / voice_transcript_partial / voice: run the smart
  meta: kind=partial | timestamp=1787376964.4413416 | source=vosk | rms=2563 | updated_at=1787376964.4114695 | frequency_hz=213.0
- [2026-08-22 13:36:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376964.660491 | source=vosk | rms=2937 | updated_at=1787376964.660491 | frequency_hz=219.7
- [2026-08-22 13:36:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376964.910553 | source=vosk | rms=562 | updated_at=1787376964.910553 | frequency_hz=219.7
- [2026-08-22 13:36:04] operator / voice_transcript_partial / voice: run the smart century
  meta: kind=partial | timestamp=1787376964.9261491 | source=vosk | rms=562 | updated_at=1787376964.910553 | frequency_hz=219.7
- [2026-08-22 13:36:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376965.1623342 | source=vosk | rms=453 | updated_at=1787376965.1623342 | frequency_hz=219.7
- [2026-08-22 13:36:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376965.4101443 | source=vosk | rms=1038 | updated_at=1787376965.4101443 | frequency_hz=219.7
- [2026-08-22 13:36:05] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1787376965.4303837 | source=final | rms=1038 | updated_at=1787376965.4101443 | frequency_hz=219.7
- [2026-08-22 13:36:05] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787376965.474322 | source=state | rms=1038 | updated_at=1787376965.4101443 | frequency_hz=219.7
- [2026-08-22 13:36:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376965.4749038 | source=state | rms=1038 | updated_at=1787376965.4101443 | frequency_hz=219.7
- [2026-08-22 13:36:05] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-08-22 13:36:05] assistant / spoken_confirmation / voice: Running Smart Sentry now. Connecting the Smart Sentry boards first.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-08-22 13:36:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376966.346524 | source=vosk | rms=1200 | updated_at=1787376966.346524 | frequency_hz=219.7
- [2026-08-22 13:36:11] operator / voice_transcript_partial / voice: he definitely
  meta: kind=partial | timestamp=1787376971.0219154 | source=vosk | rms=766 | updated_at=1787376970.0796282 | frequency_hz=219.7
- [2026-08-22 13:36:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376971.0219154 | source=vosk | rms=766 | updated_at=1787376970.0796282 | frequency_hz=219.7
- [2026-08-22 13:36:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376971.0219154 | source=vosk | rms=981 | updated_at=1787376971.0219154 | frequency_hz=219.7
- [2026-08-22 13:36:11] operator / voice_transcript_partial / voice: connecting the smarts and
  meta: kind=partial | timestamp=1787376971.1655219 | source=vosk | rms=981 | updated_at=1787376971.0219154 | frequency_hz=219.7
- [2026-08-22 13:36:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376971.3297188 | source=vosk | rms=981 | updated_at=1787376971.0219154 | frequency_hz=219.7
- [2026-08-22 13:36:11] operator / voice_transcript_partial / voice: connecting the smart similar
  meta: kind=partial | timestamp=1787376971.436676 | source=vosk | rms=981 | updated_at=1787376971.0219154 | frequency_hz=219.7
- [2026-08-22 13:36:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376971.8313372 | source=vosk | rms=1203 | updated_at=1787376971.8313372 | frequency_hz=219.7
- [2026-08-22 13:36:11] operator / voice_transcript_partial / voice: connecting the smart similar it's
  meta: kind=partial | timestamp=1787376971.8789902 | source=vosk | rms=1203 | updated_at=1787376971.8313372 | frequency_hz=219.7
- [2026-08-22 13:36:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376972.0797546 | source=vosk | rms=1200 | updated_at=1787376972.0797546 | frequency_hz=219.7
- [2026-08-22 13:36:12] operator / voice_transcript_partial / voice: connecting the smart similar to earth
  meta: kind=partial | timestamp=1787376972.0978444 | source=vosk | rms=1200 | updated_at=1787376972.0797546 | frequency_hz=219.7
- [2026-08-22 13:36:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376972.3368564 | source=vosk | rms=1200 | updated_at=1787376972.3368564 | frequency_hz=219.7
- [2026-08-22 13:36:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376972.8305109 | source=vosk | rms=1200 | updated_at=1787376972.3368564 | frequency_hz=219.7
- [2026-08-22 13:36:13] operator / voice_transcript_final / voice: connecting the smart similar to earth
  meta: kind=final | timestamp=1787376973.9396012 | source=final | rms=1200 | updated_at=1787376972.3368564 | frequency_hz=219.7
- [2026-08-22 13:36:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376975.32997 | source=vosk | rms=1200 | updated_at=1787376972.3368564 | frequency_hz=219.7
- [2026-08-22 13:36:15] operator / voice_transcript_final / voice: connecting the smart similar to earth
  meta: kind=final | timestamp=1787376975.6159184 | source=final | rms=1200 | updated_at=1787376972.3368564 | frequency_hz=219.7
- [2026-08-22 13:36:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376975.732565 | source=vosk | rms=1205 | updated_at=1787376975.732565 | frequency_hz=219.7
- [2026-08-22 13:36:16] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1787376976.3435338 | source=vosk | rms=784 | updated_at=1787376975.835527 | frequency_hz=219.7
- [2026-08-22 13:36:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376976.5797882 | source=vosk | rms=784 | updated_at=1787376975.835527 | frequency_hz=219.7
- [2026-08-22 13:36:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376976.8359344 | source=vosk | rms=784 | updated_at=1787376975.835527 | frequency_hz=219.7
- [2026-08-22 13:36:16] operator / voice_transcript_partial / voice: smart central rates are
  meta: kind=partial | timestamp=1787376976.872619 | source=vosk | rms=784 | updated_at=1787376975.835527 | frequency_hz=219.7
- [2026-08-22 13:36:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376977.0805774 | source=vosk | rms=784 | updated_at=1787376975.835527 | frequency_hz=219.7
- [2026-08-22 13:36:17] operator / voice_transcript_partial / voice: smart central it's our connection
  meta: kind=partial | timestamp=1787376977.094521 | source=vosk | rms=784 | updated_at=1787376975.835527 | frequency_hz=219.7
- [2026-08-22 13:36:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376977.3302355 | source=vosk | rms=784 | updated_at=1787376975.835527 | frequency_hz=219.7
- [2026-08-22 13:36:17] operator / voice_transcript_partial / voice: smart central rates are connected
  meta: kind=partial | timestamp=1787376977.3615108 | source=vosk | rms=784 | updated_at=1787376975.835527 | frequency_hz=219.7
- [2026-08-22 13:36:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376977.5881 | source=vosk | rms=692 | updated_at=1787376977.5865977 | frequency_hz=219.7
- [2026-08-22 13:36:17] operator / voice_transcript_partial / voice: smart central rates are connected on
  meta: kind=partial | timestamp=1787376977.6066387 | source=vosk | rms=692 | updated_at=1787376977.5865977 | frequency_hz=219.7
- [2026-08-22 13:36:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376977.8335397 | source=vosk | rms=756 | updated_at=1787376977.8335397 | frequency_hz=219.7
- [2026-08-22 13:36:17] operator / voice_transcript_partial / voice: smart central rates are connected on the
  meta: kind=partial | timestamp=1787376977.863494 | source=vosk | rms=756 | updated_at=1787376977.8335397 | frequency_hz=219.7
- [2026-08-22 13:36:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376978.330451 | source=vosk | rms=756 | updated_at=1787376977.8335397 | frequency_hz=219.7
- [2026-08-22 13:36:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376978.8315606 | source=vosk | rms=820 | updated_at=1787376978.8315606 | frequency_hz=219.7
- [2026-08-22 13:36:18] operator / voice_transcript_partial / voice: smart central rates are connected on the c o
  meta: kind=partial | timestamp=1787376978.8667943 | source=vosk | rms=820 | updated_at=1787376978.8315606 | frequency_hz=219.7
- [2026-08-22 13:36:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376979.0803087 | source=vosk | rms=1081 | updated_at=1787376979.0803087 | frequency_hz=219.7
- [2026-08-22 13:36:19] operator / voice_transcript_partial / voice: smart central rates are connected on the c o and
  meta: kind=partial | timestamp=1787376979.1066203 | source=vosk | rms=1081 | updated_at=1787376979.0803087 | frequency_hz=219.7
- [2026-08-22 13:36:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376979.3299649 | source=vosk | rms=1009 | updated_at=1787376979.3299649 | frequency_hz=219.7
- [2026-08-22 13:36:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376979.581646 | source=vosk | rms=814 | updated_at=1787376979.581646 | frequency_hz=219.7
- [2026-08-22 13:36:19] operator / voice_transcript_partial / voice: smart central rates are connected on the c o and smart
  meta: kind=partial | timestamp=1787376979.6011899 | source=vosk | rms=814 | updated_at=1787376979.581646 | frequency_hz=219.7
- [2026-08-22 13:36:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376979.8309462 | source=vosk | rms=814 | updated_at=1787376979.581646 | frequency_hz=219.7
- [2026-08-22 13:36:19] operator / voice_transcript_partial / voice: smart central rates are connected on the c o and smart century
  meta: kind=partial | timestamp=1787376979.915932 | source=vosk | rms=814 | updated_at=1787376979.581646 | frequency_hz=219.7
- [2026-08-22 13:36:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376980.080214 | source=vosk | rms=814 | updated_at=1787376979.581646 | frequency_hz=219.7
- [2026-08-22 13:36:20] operator / voice_transcript_partial / voice: smart central rates are connected on the c o and smart century isn't a
  meta: kind=partial | timestamp=1787376980.1253014 | source=vosk | rms=814 | updated_at=1787376979.581646 | frequency_hz=219.7
- [2026-08-22 13:36:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376980.5801015 | source=vosk | rms=814 | updated_at=1787376979.581646 | frequency_hz=219.7
- [2026-08-22 13:36:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376981.0798383 | source=vosk | rms=1207 | updated_at=1787376981.0798383 | frequency_hz=219.7
- [2026-08-22 13:36:21] operator / voice_transcript_partial / voice: smart central rates are connected on the c o and smart century isn't a of
  meta: kind=partial | timestamp=1787376981.184454 | source=vosk | rms=1207 | updated_at=1787376981.0798383 | frequency_hz=219.7
- [2026-08-22 13:36:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376981.3336346 | source=vosk | rms=1207 | updated_at=1787376981.0798383 | frequency_hz=219.7
- [2026-08-22 13:36:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376981.5804026 | source=vosk | rms=926 | updated_at=1787376981.5804026 | frequency_hz=219.7
- [2026-08-22 13:36:21] operator / voice_transcript_partial / voice: smart central rates are connected on the c o and smart century isn't a of ask another
  meta: kind=partial | timestamp=1787376981.6201203 | source=vosk | rms=926 | updated_at=1787376981.5804026 | frequency_hz=219.7
- [2026-08-22 13:36:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376981.831608 | source=vosk | rms=960 | updated_at=1787376981.831608 | frequency_hz=219.7
- [2026-08-22 13:36:21] operator / voice_transcript_partial / voice: smart central rates are connected on the c o and smart century isn't a of ask another question
  meta: kind=partial | timestamp=1787376981.862503 | source=vosk | rms=960 | updated_at=1787376981.831608 | frequency_hz=219.7
- [2026-08-22 13:36:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376982.3300989 | source=vosk | rms=960 | updated_at=1787376981.831608 | frequency_hz=219.7
- [2026-08-22 13:36:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376982.5802174 | source=vosk | rms=960 | updated_at=1787376981.831608 | frequency_hz=219.7
- [2026-08-22 13:36:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376982.8299112 | source=vosk | rms=960 | updated_at=1787376981.831608 | frequency_hz=219.7
- [2026-08-22 13:36:22] operator / voice_transcript_partial / voice: smart central rates are connected on the c o and smart century isn't a of ask another question or
  meta: kind=partial | timestamp=1787376982.8465462 | source=vosk | rms=960 | updated_at=1787376981.831608 | frequency_hz=219.7
- [2026-08-22 13:36:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376983.3300548 | source=vosk | rms=960 | updated_at=1787376981.831608 | frequency_hz=219.7
- [2026-08-22 13:36:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376983.8316646 | source=vosk | rms=960 | updated_at=1787376981.831608 | frequency_hz=219.7
- [2026-08-22 13:36:23] operator / voice_transcript_partial / voice: smart central rates are connected on the c o and smart century isn't a of ask another question or given
  meta: kind=partial | timestamp=1787376983.8627539 | source=vosk | rms=960 | updated_at=1787376981.831608 | frequency_hz=219.7
- [2026-08-22 13:36:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376984.3306577 | source=vosk | rms=960 | updated_at=1787376981.831608 | frequency_hz=219.7
- [2026-08-22 13:36:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376988.3305287 | source=vosk | rms=1200 | updated_at=1787376988.3305287 | frequency_hz=219.7
- [2026-08-22 13:36:28] operator / voice_transcript_partial / voice: smart central rates are connected on the c o and smart century isn't a of ask another question or give another
  meta: kind=partial | timestamp=1787376988.3834906 | source=vosk | rms=1200 | updated_at=1787376988.3305287 | frequency_hz=219.7
- [2026-08-22 13:36:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376988.5807831 | source=vosk | rms=1203 | updated_at=1787376988.5807831 | frequency_hz=219.7
- [2026-08-22 13:36:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376988.8392842 | source=vosk | rms=1203 | updated_at=1787376988.8392842 | frequency_hz=219.7
- [2026-08-22 13:36:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376989.3306034 | source=vosk | rms=1202 | updated_at=1787376989.3306034 | frequency_hz=219.7
- [2026-08-22 13:36:30] operator / voice_transcript_final / voice: smart central rates are connect on the c o and smart sentry isn t a of ask another question or give another
  meta: kind=final | timestamp=1787376990.1302738 | source=final | rms=1202 | updated_at=1787376989.3306034 | frequency_hz=219.7
- [2026-08-22 13:36:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376990.482772 | source=vosk | rms=1202 | updated_at=1787376989.3306034 | frequency_hz=219.7
- [2026-08-22 13:36:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376990.482772 | source=vosk | rms=1200 | updated_at=1787376990.482772 | frequency_hz=219.7
- [2026-08-22 13:36:31] operator / voice_transcript_partial / voice: show me the
  meta: kind=partial | timestamp=1787376991.6362793 | source=vosk | rms=1533 | updated_at=1787376991.5804317 | frequency_hz=273.2
- [2026-08-22 13:36:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376991.8305697 | source=vosk | rms=2488 | updated_at=1787376991.8305697 | frequency_hz=273.2
- [2026-08-22 13:36:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376992.0800045 | source=vosk | rms=1590 | updated_at=1787376992.0800045 | frequency_hz=273.2
- [2026-08-22 13:36:32] operator / voice_transcript_partial / voice: show me the eight
  meta: kind=partial | timestamp=1787376992.095891 | source=vosk | rms=1590 | updated_at=1787376992.0800045 | frequency_hz=273.2
- [2026-08-22 13:36:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376992.3301797 | source=vosk | rms=2383 | updated_at=1787376992.3301797 | frequency_hz=273.2
- [2026-08-22 13:36:32] operator / voice_transcript_partial / voice: show me the a to
  meta: kind=partial | timestamp=1787376992.3584843 | source=vosk | rms=2383 | updated_at=1787376992.3301797 | frequency_hz=273.2
- [2026-08-22 13:36:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376992.5810823 | source=vosk | rms=1293 | updated_at=1787376992.5810823 | frequency_hz=273.2
- [2026-08-22 13:36:32] operator / voice_transcript_partial / voice: show me the a today he said
  meta: kind=partial | timestamp=1787376992.6154513 | source=vosk | rms=1293 | updated_at=1787376992.5810823 | frequency_hz=273.2
- [2026-08-22 13:36:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376992.8318136 | source=vosk | rms=1687 | updated_at=1787376992.8318136 | frequency_hz=273.2
- [2026-08-22 13:36:32] operator / voice_transcript_partial / voice: show me the a to the settings
  meta: kind=partial | timestamp=1787376992.8626313 | source=vosk | rms=1687 | updated_at=1787376992.8318136 | frequency_hz=273.2
- [2026-08-22 13:36:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376993.0808094 | source=vosk | rms=1687 | updated_at=1787376992.8318136 | frequency_hz=273.2
- [2026-08-22 13:36:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376993.5807116 | source=vosk | rms=1203 | updated_at=1787376993.5807116 | frequency_hz=273.2
- [2026-08-22 13:36:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376993.8308003 | source=vosk | rms=1167 | updated_at=1787376993.8308003 | frequency_hz=273.2
- [2026-08-22 13:36:34] operator / voice_transcript_final / voice: show me the a tutti settings
  meta: kind=final | timestamp=1787376994.2374563 | source=final | rms=1167 | updated_at=1787376993.8308003 | frequency_hz=273.2
- [2026-08-22 13:36:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376994.392811 | source=vosk | rms=1167 | updated_at=1787376993.8308003 | frequency_hz=273.2
- [2026-08-22 13:36:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376994.392811 | source=vosk | rms=1167 | updated_at=1787376993.8308003 | frequency_hz=273.2
- [2026-08-22 13:36:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376994.8308501 | source=vosk | rms=1167 | updated_at=1787376993.8308003 | frequency_hz=273.2
- [2026-08-22 13:36:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376995.3306715 | source=vosk | rms=1167 | updated_at=1787376993.8308003 | frequency_hz=273.2
- [2026-08-22 13:36:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376996.0808225 | source=vosk | rms=1167 | updated_at=1787376993.8308003 | frequency_hz=273.2
- [2026-08-22 13:36:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376998.4492946 | source=vosk | rms=1167 | updated_at=1787376993.8308003 | frequency_hz=273.2
- [2026-08-22 13:36:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787376999.4411013 | source=vosk | rms=1167 | updated_at=1787376993.8308003 | frequency_hz=273.2
- [2026-08-22 13:36:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787376999.690686 | source=vosk | rms=796 | updated_at=1787376999.690686 | frequency_hz=273.2
- [2026-08-22 13:36:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377001.190583 | source=vosk | rms=758 | updated_at=1787377000.6968043 | frequency_hz=273.2
- [2026-08-22 13:36:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377001.9402237 | source=vosk | rms=758 | updated_at=1787377000.6968043 | frequency_hz=273.2
- [2026-08-22 13:36:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377006.1895506 | source=vosk | rms=770 | updated_at=1787377004.4409883 | frequency_hz=273.2
- [2026-08-22 13:36:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377006.9803598 | source=vosk | rms=770 | updated_at=1787377004.4409883 | frequency_hz=273.2
- [2026-08-22 13:36:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377007.7308586 | source=vosk | rms=731 | updated_at=1787377007.2322211 | frequency_hz=273.2
- [2026-08-22 13:36:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377009.980772 | source=vosk | rms=731 | updated_at=1787377007.2322211 | frequency_hz=273.2
- [2026-08-22 13:36:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377011.2307427 | source=vosk | rms=731 | updated_at=1787377007.2322211 | frequency_hz=273.2
- [2026-08-22 13:36:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377013.352294 | source=vosk | rms=870 | updated_at=1787377013.352294 | frequency_hz=273.2
- [2026-08-22 13:36:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377016.8605928 | source=vosk | rms=931 | updated_at=1787377016.360629 | frequency_hz=313.4
- [2026-08-22 13:37:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377020.1104093 | source=vosk | rms=1202 | updated_at=1787377020.1104093 | frequency_hz=313.4
- [2026-08-22 13:37:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377021.360252 | source=vosk | rms=1202 | updated_at=1787377020.6153738 | frequency_hz=313.4
- [2026-08-22 13:37:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377022.6104841 | source=vosk | rms=1200 | updated_at=1787377022.6104841 | frequency_hz=313.4
- [2026-08-22 13:37:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377023.3769348 | source=vosk | rms=1200 | updated_at=1787377022.8617387 | frequency_hz=313.4
- [2026-08-22 13:37:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377028.3616536 | source=vosk | rms=1203 | updated_at=1787377028.3616536 | frequency_hz=313.4
- [2026-08-22 13:37:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377029.1101835 | source=vosk | rms=1201 | updated_at=1787377028.6102066 | frequency_hz=313.4
- [2026-08-22 13:37:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377030.8608873 | source=vosk | rms=1201 | updated_at=1787377028.6102066 | frequency_hz=313.4
- [2026-08-22 13:37:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377033.860315 | source=vosk | rms=1201 | updated_at=1787377028.6102066 | frequency_hz=313.4
- [2026-08-22 13:37:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377035.0154393 | source=vosk | rms=429 | updated_at=1787377035.0154393 | frequency_hz=313.4
- [2026-08-22 13:37:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377041.760701 | source=vosk | rms=750 | updated_at=1787377041.2612834 | frequency_hz=313.4
- [2026-08-22 13:37:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377042.0110226 | source=vosk | rms=750 | updated_at=1787377041.2612834 | frequency_hz=313.4
- [2026-08-22 13:37:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377043.7602441 | source=vosk | rms=370 | updated_at=1787377043.261067 | frequency_hz=313.4
- [2026-08-22 13:37:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377044.019277 | source=vosk | rms=370 | updated_at=1787377043.261067 | frequency_hz=313.4
- [2026-08-22 13:37:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377044.7598937 | source=vosk | rms=370 | updated_at=1787377043.261067 | frequency_hz=313.4
- [2026-08-22 13:37:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377045.760686 | source=vosk | rms=370 | updated_at=1787377043.261067 | frequency_hz=313.4
- [2026-08-22 13:37:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377047.7933605 | source=vosk | rms=485 | updated_at=1787377046.7604277 | frequency_hz=313.4
- [2026-08-22 13:37:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377048.0752401 | source=vosk | rms=485 | updated_at=1787377046.7604277 | frequency_hz=313.4
- [2026-08-22 13:37:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377048.5411055 | source=vosk | rms=485 | updated_at=1787377046.7604277 | frequency_hz=313.4
- [2026-08-22 13:37:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377049.7909906 | source=vosk | rms=480 | updated_at=1787377049.7909906 | frequency_hz=313.4
- [2026-08-22 13:37:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377051.2902684 | source=vosk | rms=1202 | updated_at=1787377050.8184652 | frequency_hz=313.4
- [2026-08-22 13:37:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377051.5405855 | source=vosk | rms=979 | updated_at=1787377051.5405855 | frequency_hz=313.4
- [2026-08-22 13:37:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377052.0406306 | source=vosk | rms=979 | updated_at=1787377051.5405855 | frequency_hz=313.4
- [2026-08-22 13:37:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377052.5430021 | source=vosk | rms=979 | updated_at=1787377051.5405855 | frequency_hz=313.4
- [2026-08-22 13:37:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377053.5420234 | source=vosk | rms=1205 | updated_at=1787377052.7940676 | frequency_hz=313.4
- [2026-08-22 13:37:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377054.7912169 | source=vosk | rms=1058 | updated_at=1787377054.7912169 | frequency_hz=313.4
- [2026-08-22 13:37:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377055.2905922 | source=vosk | rms=1058 | updated_at=1787377054.7912169 | frequency_hz=313.4
- [2026-08-22 13:37:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377055.5409338 | source=vosk | rms=1099 | updated_at=1787377055.5409338 | frequency_hz=313.4
- [2026-08-22 13:37:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377056.0550861 | source=vosk | rms=1099 | updated_at=1787377055.5409338 | frequency_hz=313.4
- [2026-08-22 13:37:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377056.8639634 | source=vosk | rms=1099 | updated_at=1787377055.5409338 | frequency_hz=313.4
- [2026-08-22 13:37:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377059.6112225 | source=vosk | rms=617 | updated_at=1787377058.8607404 | frequency_hz=313.4
- [2026-08-22 13:37:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377060.110772 | source=vosk | rms=525 | updated_at=1787377060.110772 | frequency_hz=313.4
- [2026-08-22 13:37:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377070.2909796 | source=vosk | rms=556 | updated_at=1787377068.38199 | frequency_hz=313.4
- [2026-08-22 13:37:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377070.5412624 | source=vosk | rms=594 | updated_at=1787377070.5412624 | frequency_hz=313.4
- [2026-08-22 13:37:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377072.7910552 | source=vosk | rms=1202 | updated_at=1787377071.2909067 | frequency_hz=313.4
- [2026-08-22 13:37:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377073.2959158 | source=vosk | rms=1202 | updated_at=1787377071.2909067 | frequency_hz=313.4
- [2026-08-22 13:37:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377074.2904823 | source=vosk | rms=801 | updated_at=1787377073.7906444 | frequency_hz=313.4
- [2026-08-22 13:37:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377076.041078 | source=vosk | rms=982 | updated_at=1787377076.041078 | frequency_hz=313.4
- [2026-08-22 13:37:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377076.5407643 | source=vosk | rms=982 | updated_at=1787377076.041078 | frequency_hz=313.4
- [2026-08-22 13:37:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377076.790917 | source=vosk | rms=987 | updated_at=1787377076.790917 | frequency_hz=313.4
- [2026-08-22 13:37:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377077.2907882 | source=vosk | rms=987 | updated_at=1787377076.790917 | frequency_hz=313.4
- [2026-08-22 13:37:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377077.7970002 | source=vosk | rms=1116 | updated_at=1787377077.7970002 | frequency_hz=313.4
- [2026-08-22 13:37:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377078.7908938 | source=vosk | rms=1205 | updated_at=1787377078.2910323 | frequency_hz=313.4
- [2026-08-22 13:37:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377079.0407932 | source=vosk | rms=1199 | updated_at=1787377079.0407932 | frequency_hz=313.4
- [2026-08-22 13:37:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377079.5406277 | source=vosk | rms=1199 | updated_at=1787377079.0407932 | frequency_hz=313.4
- [2026-08-22 13:38:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377081.2907293 | source=vosk | rms=775 | updated_at=1787377081.2907293 | frequency_hz=313.4
- [2026-08-22 13:38:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377082.2907155 | source=vosk | rms=1200 | updated_at=1787377081.7909224 | frequency_hz=313.4
- [2026-08-22 13:38:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377084.0423682 | source=vosk | rms=541 | updated_at=1787377084.0423682 | frequency_hz=313.4
- [2026-08-22 13:38:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377084.541102 | source=vosk | rms=541 | updated_at=1787377084.0423682 | frequency_hz=313.4
- [2026-08-22 13:38:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377085.0408444 | source=vosk | rms=1111 | updated_at=1787377085.0408444 | frequency_hz=313.4
- [2026-08-22 13:38:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377085.5414703 | source=vosk | rms=1111 | updated_at=1787377085.0408444 | frequency_hz=313.4
- [2026-08-22 13:38:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377087.2915456 | source=vosk | rms=1111 | updated_at=1787377085.0408444 | frequency_hz=313.4
- [2026-08-22 13:38:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377088.563839 | source=vosk | rms=1203 | updated_at=1787377087.960912 | frequency_hz=313.4
- [2026-08-22 13:38:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377090.8107865 | source=vosk | rms=847 | updated_at=1787377090.8107865 | frequency_hz=313.4
- [2026-08-22 13:38:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377091.3307889 | source=vosk | rms=847 | updated_at=1787377090.8107865 | frequency_hz=313.4
- [2026-08-22 13:38:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377092.5815449 | source=vosk | rms=568 | updated_at=1787377092.5815449 | frequency_hz=313.4
- [2026-08-22 13:38:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377093.0813775 | source=vosk | rms=568 | updated_at=1787377092.5815449 | frequency_hz=313.4
- [2026-08-22 13:38:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377094.3315032 | source=vosk | rms=1204 | updated_at=1787377094.3315032 | frequency_hz=313.4
- [2026-08-22 13:38:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377095.0823328 | source=vosk | rms=1203 | updated_at=1787377094.5812628 | frequency_hz=313.4
- [2026-08-22 13:38:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377095.3321376 | source=vosk | rms=1173 | updated_at=1787377095.3321376 | frequency_hz=313.4
- [2026-08-22 13:38:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377095.8315644 | source=vosk | rms=1173 | updated_at=1787377095.3321376 | frequency_hz=313.4
- [2026-08-22 13:38:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377096.8316598 | source=vosk | rms=1173 | updated_at=1787377095.3321376 | frequency_hz=313.4
- [2026-08-22 13:38:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377099.580737 | source=vosk | rms=609 | updated_at=1787377098.8309343 | frequency_hz=313.4
- [2026-08-22 13:38:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377099.8457398 | source=vosk | rms=369 | updated_at=1787377099.8457398 | frequency_hz=313.4
- [2026-08-22 13:38:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377101.3309112 | source=vosk | rms=790 | updated_at=1787377100.331321 | frequency_hz=313.4
- [2026-08-22 13:38:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377101.5816362 | source=vosk | rms=341 | updated_at=1787377101.5816362 | frequency_hz=313.4
- [2026-08-22 13:38:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377103.3362367 | source=vosk | rms=717 | updated_at=1787377102.8316154 | frequency_hz=313.4
- [2026-08-22 13:38:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377104.5903103 | source=vosk | rms=1012 | updated_at=1787377104.5903103 | frequency_hz=313.4
- [2026-08-22 13:38:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377106.8310182 | source=vosk | rms=645 | updated_at=1787377106.3314967 | frequency_hz=313.4
- [2026-08-22 13:38:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377107.8675637 | source=vosk | rms=1205 | updated_at=1787377107.8675637 | frequency_hz=313.4
- [2026-08-22 13:38:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377108.831012 | source=vosk | rms=1175 | updated_at=1787377108.3310246 | frequency_hz=313.4
- [2026-08-22 13:38:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377110.3316572 | source=vosk | rms=1175 | updated_at=1787377108.3310246 | frequency_hz=313.4
- [2026-08-22 13:38:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377114.1318986 | source=vosk | rms=1206 | updated_at=1787377113.3825772 | frequency_hz=313.4
- [2026-08-22 13:38:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377114.3807342 | source=vosk | rms=821 | updated_at=1787377114.3807342 | frequency_hz=313.4
- [2026-08-22 13:38:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377115.3817677 | source=vosk | rms=821 | updated_at=1787377114.3807342 | frequency_hz=313.4
- [2026-08-22 13:38:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377115.8816772 | source=vosk | rms=1201 | updated_at=1787377115.8816772 | frequency_hz=313.4
- [2026-08-22 13:38:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377120.13173 | source=vosk | rms=1202 | updated_at=1787377119.6307034 | frequency_hz=313.4
- [2026-08-22 13:38:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377120.631528 | source=vosk | rms=397 | updated_at=1787377120.631528 | frequency_hz=313.4
- [2026-08-22 13:38:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377125.566943 | source=vosk | rms=847 | updated_at=1787377125.1014142 | frequency_hz=313.4
- [2026-08-22 13:38:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377126.312697 | source=vosk | rms=1202 | updated_at=1787377126.312697 | frequency_hz=313.4
- [2026-08-22 13:38:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377126.8117468 | source=vosk | rms=1202 | updated_at=1787377126.312697 | frequency_hz=313.4
- [2026-08-22 13:38:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377131.06178 | source=vosk | rms=1204 | updated_at=1787377131.06178 | frequency_hz=313.4
- [2026-08-22 13:38:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377133.5611138 | source=vosk | rms=478 | updated_at=1787377131.8110034 | frequency_hz=313.4
- [2026-08-22 13:38:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377133.812649 | source=vosk | rms=1039 | updated_at=1787377133.812649 | frequency_hz=313.4
- [2026-08-22 13:38:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377135.0614538 | source=vosk | rms=1007 | updated_at=1787377134.311759 | frequency_hz=313.4
- [2026-08-22 13:38:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377135.3109744 | source=vosk | rms=953 | updated_at=1787377135.3109744 | frequency_hz=313.4
- [2026-08-22 13:38:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377138.5577013 | source=vosk | rms=1200 | updated_at=1787377137.791557 | frequency_hz=313.4
- [2026-08-22 13:38:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377138.5577013 | source=vosk | rms=1202 | updated_at=1787377138.5577013 | frequency_hz=313.4
- [2026-08-22 13:39:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377146.2915678 | source=vosk | rms=599 | updated_at=1787377145.790969 | frequency_hz=313.4
- [2026-08-22 13:39:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377146.8228953 | source=vosk | rms=651 | updated_at=1787377146.8228953 | frequency_hz=313.4
- [2026-08-22 13:39:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377149.2915108 | source=vosk | rms=1204 | updated_at=1787377148.5409794 | frequency_hz=313.4
- [2026-08-22 13:39:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377149.5415125 | source=vosk | rms=1204 | updated_at=1787377148.5409794 | frequency_hz=313.4
- [2026-08-22 13:39:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377151.0417674 | source=vosk | rms=1204 | updated_at=1787377148.5409794 | frequency_hz=313.4
- [2026-08-22 13:39:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377152.791351 | source=vosk | rms=1202 | updated_at=1787377152.791351 | frequency_hz=313.4
- [2026-08-22 13:39:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377153.541246 | source=vosk | rms=1201 | updated_at=1787377153.0467062 | frequency_hz=313.4
- [2026-08-22 13:39:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377155.087727 | source=vosk | rms=1204 | updated_at=1787377155.087727 | frequency_hz=313.4
- [2026-08-22 13:39:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377158.0611713 | source=vosk | rms=727 | updated_at=1787377155.8113368 | frequency_hz=313.4
- [2026-08-22 13:39:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377158.562976 | source=vosk | rms=727 | updated_at=1787377155.8113368 | frequency_hz=313.4
- [2026-08-22 13:39:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377159.8120184 | source=vosk | rms=591 | updated_at=1787377159.0994961 | frequency_hz=313.4
- [2026-08-22 13:39:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377161.319844 | source=vosk | rms=591 | updated_at=1787377159.0994961 | frequency_hz=313.4
- [2026-08-22 13:39:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377163.0614293 | source=vosk | rms=1201 | updated_at=1787377162.5619855 | frequency_hz=313.4
- [2026-08-22 13:39:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377163.8125882 | source=vosk | rms=1201 | updated_at=1787377162.5619855 | frequency_hz=313.4
- [2026-08-22 13:39:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377164.811281 | source=vosk | rms=1201 | updated_at=1787377162.5619855 | frequency_hz=313.4
- [2026-08-22 13:39:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377165.3119628 | source=vosk | rms=1201 | updated_at=1787377162.5619855 | frequency_hz=313.4
- [2026-08-22 13:39:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377166.0629385 | source=vosk | rms=1201 | updated_at=1787377162.5619855 | frequency_hz=313.4
- [2026-08-22 13:39:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377166.317306 | source=vosk | rms=1201 | updated_at=1787377162.5619855 | frequency_hz=313.4
- [2026-08-22 13:39:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377168.044051 | source=vosk | rms=1201 | updated_at=1787377162.5619855 | frequency_hz=313.4
- [2026-08-22 13:39:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377168.5229864 | source=vosk | rms=766 | updated_at=1787377168.5229864 | frequency_hz=313.4
- [2026-08-22 13:39:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377171.021723 | source=vosk | rms=656 | updated_at=1787377170.5216572 | frequency_hz=313.4
- [2026-08-22 13:39:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377171.2718832 | source=vosk | rms=656 | updated_at=1787377170.5216572 | frequency_hz=313.4
- [2026-08-22 13:39:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377173.5218012 | source=vosk | rms=710 | updated_at=1787377172.5301423 | frequency_hz=313.4
- [2026-08-22 13:39:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377174.0215352 | source=vosk | rms=714 | updated_at=1787377174.0215352 | frequency_hz=313.4
- [2026-08-22 13:39:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377177.2714324 | source=vosk | rms=563 | updated_at=1787377176.7727082 | frequency_hz=313.4
- [2026-08-22 13:39:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377177.5231228 | source=vosk | rms=1091 | updated_at=1787377177.5231228 | frequency_hz=313.4
- [2026-08-22 13:39:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377181.0216877 | source=vosk | rms=499 | updated_at=1787377180.5553498 | frequency_hz=258.3
- [2026-08-22 13:39:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377181.2715037 | source=vosk | rms=580 | updated_at=1787377181.2715037 | frequency_hz=258.3
- [2026-08-22 13:39:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377183.545082 | source=vosk | rms=504 | updated_at=1787377183.0494902 | frequency_hz=258.3
- [2026-08-22 13:39:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377183.772096 | source=vosk | rms=784 | updated_at=1787377183.772096 | frequency_hz=258.3
- [2026-08-22 13:39:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377185.0215902 | source=vosk | rms=463 | updated_at=1787377184.2730355 | frequency_hz=258.3
- [2026-08-22 13:39:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377186.522986 | source=vosk | rms=1201 | updated_at=1787377186.522986 | frequency_hz=258.3
- [2026-08-22 13:39:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377188.771618 | source=vosk | rms=754 | updated_at=1787377188.0220318 | frequency_hz=258.3
- [2026-08-22 13:39:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377189.0217597 | source=vosk | rms=754 | updated_at=1787377188.0220318 | frequency_hz=258.3
- [2026-08-22 13:39:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377194.6020248 | source=vosk | rms=558 | updated_at=1787377193.1062868 | frequency_hz=258.3
- [2026-08-22 13:39:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377195.1018481 | source=vosk | rms=558 | updated_at=1787377193.1062868 | frequency_hz=258.3
- [2026-08-22 13:39:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377196.351846 | source=vosk | rms=1200 | updated_at=1787377195.8523257 | frequency_hz=212.5
- [2026-08-22 13:40:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377201.8744812 | source=vosk | rms=1201 | updated_at=1787377201.8744812 | frequency_hz=212.5
- [2026-08-22 13:40:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377202.8573184 | source=vosk | rms=1201 | updated_at=1787377202.1026757 | frequency_hz=212.5
- [2026-08-22 13:40:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377204.3519676 | source=vosk | rms=596 | updated_at=1787377204.3519676 | frequency_hz=212.5
- [2026-08-22 13:40:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377207.6051588 | source=vosk | rms=589 | updated_at=1787377206.1061811 | frequency_hz=212.5
- [2026-08-22 13:40:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377207.8540514 | source=vosk | rms=589 | updated_at=1787377206.1061811 | frequency_hz=212.5
- [2026-08-22 13:40:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377209.372284 | source=vosk | rms=589 | updated_at=1787377206.1061811 | frequency_hz=212.5
- [2026-08-22 13:40:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377210.6221826 | source=vosk | rms=589 | updated_at=1787377206.1061811 | frequency_hz=212.5
- [2026-08-22 13:40:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377211.8721232 | source=vosk | rms=862 | updated_at=1787377211.3735778 | frequency_hz=212.5
- [2026-08-22 13:40:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377212.372113 | source=vosk | rms=862 | updated_at=1787377211.3735778 | frequency_hz=212.5
- [2026-08-22 13:40:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377213.9208214 | source=vosk | rms=1200 | updated_at=1787377213.3723767 | frequency_hz=212.5
- [2026-08-22 13:40:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377214.6222067 | source=vosk | rms=1200 | updated_at=1787377213.3723767 | frequency_hz=212.5
- [2026-08-22 13:40:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377215.1242127 | source=vosk | rms=1200 | updated_at=1787377213.3723767 | frequency_hz=212.5
- [2026-08-22 13:40:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377223.3722603 | source=vosk | rms=1200 | updated_at=1787377213.3723767 | frequency_hz=212.5
- [2026-08-22 13:40:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377223.8724058 | source=vosk | rms=1200 | updated_at=1787377213.3723767 | frequency_hz=212.5
- [2026-08-22 13:40:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377224.12345 | source=vosk | rms=688 | updated_at=1787377224.12345 | frequency_hz=212.5
- [2026-08-22 13:40:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377227.8723567 | source=vosk | rms=299 | updated_at=1787377227.1224244 | frequency_hz=212.5
- [2026-08-22 13:40:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377229.1254084 | source=vosk | rms=454 | updated_at=1787377229.1254084 | frequency_hz=212.5
- [2026-08-22 13:40:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377232.3727453 | source=vosk | rms=1200 | updated_at=1787377231.9133465 | frequency_hz=212.5
- [2026-08-22 13:40:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377232.6225133 | source=vosk | rms=400 | updated_at=1787377232.6225133 | frequency_hz=212.5
- [2026-08-22 13:40:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377239.3719914 | source=vosk | rms=1206 | updated_at=1787377238.8726485 | frequency_hz=212.5
- [2026-08-22 13:40:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377239.622926 | source=vosk | rms=1203 | updated_at=1787377239.622926 | frequency_hz=212.5
- [2026-08-22 13:40:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377240.3781996 | source=vosk | rms=1204 | updated_at=1787377239.872737 | frequency_hz=212.5
- [2026-08-22 13:40:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377242.122823 | source=vosk | rms=1204 | updated_at=1787377239.872737 | frequency_hz=212.5
- [2026-08-22 13:40:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377243.1232917 | source=vosk | rms=538 | updated_at=1787377242.6215703 | frequency_hz=212.5
- [2026-08-22 13:40:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377244.3732045 | source=vosk | rms=538 | updated_at=1787377242.6215703 | frequency_hz=212.5
- [2026-08-22 13:40:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377246.6284783 | source=vosk | rms=490 | updated_at=1787377246.1229398 | frequency_hz=212.5
- [2026-08-22 13:40:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377246.8811579 | source=vosk | rms=1203 | updated_at=1787377246.8811579 | frequency_hz=212.5
- [2026-08-22 13:40:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377250.3736422 | source=vosk | rms=525 | updated_at=1787377249.6307065 | frequency_hz=212.5
- [2026-08-22 13:40:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377250.872555 | source=vosk | rms=525 | updated_at=1787377249.6307065 | frequency_hz=212.5
- [2026-08-22 13:40:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377251.3728395 | source=vosk | rms=525 | updated_at=1787377249.6307065 | frequency_hz=212.5
- [2026-08-22 13:40:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377253.3734493 | source=vosk | rms=1201 | updated_at=1787377253.3734493 | frequency_hz=212.5
- [2026-08-22 13:40:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377254.1215909 | source=vosk | rms=1200 | updated_at=1787377253.6230805 | frequency_hz=212.5
- [2026-08-22 13:40:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377255.632891 | source=vosk | rms=1200 | updated_at=1787377255.632891 | frequency_hz=212.5
- [2026-08-22 13:40:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377257.5223317 | source=vosk | rms=1203 | updated_at=1787377257.022925 | frequency_hz=212.5
- [2026-08-22 13:41:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377260.2818491 | source=vosk | rms=1203 | updated_at=1787377257.022925 | frequency_hz=212.5
- [2026-08-22 13:41:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377260.7826376 | source=vosk | rms=1203 | updated_at=1787377257.022925 | frequency_hz=212.5
- [2026-08-22 13:41:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377264.2821507 | source=vosk | rms=1109 | updated_at=1787377264.2821507 | frequency_hz=224.0
- [2026-08-22 13:41:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377265.282254 | source=vosk | rms=1203 | updated_at=1787377264.783099 | frequency_hz=224.0
- [2026-08-22 13:41:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377265.550256 | source=vosk | rms=1204 | updated_at=1787377265.550256 | frequency_hz=224.0
- [2026-08-22 13:41:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377266.2820451 | source=vosk | rms=1203 | updated_at=1787377265.7824705 | frequency_hz=224.0
- [2026-08-22 13:41:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377269.5824049 | source=vosk | rms=453 | updated_at=1787377269.5824049 | frequency_hz=224.0
- [2026-08-22 13:41:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377270.1069417 | source=vosk | rms=453 | updated_at=1787377269.5824049 | frequency_hz=224.0
- [2026-08-22 13:41:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377272.5818617 | source=vosk | rms=708 | updated_at=1787377272.5818617 | frequency_hz=230.0
- [2026-08-22 13:41:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377273.5825 | source=vosk | rms=1204 | updated_at=1787377273.082449 | frequency_hz=230.0
- [2026-08-22 13:41:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377275.3333783 | source=vosk | rms=1201 | updated_at=1787377275.3333783 | frequency_hz=230.0
- [2026-08-22 13:41:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377276.3318448 | source=vosk | rms=669 | updated_at=1787377275.8318555 | frequency_hz=230.0
- [2026-08-22 13:41:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377277.1319098 | source=vosk | rms=669 | updated_at=1787377275.8318555 | frequency_hz=230.0
- [2026-08-22 13:41:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377277.832182 | source=vosk | rms=347 | updated_at=1787377277.3323948 | frequency_hz=230.0
- [2026-08-22 13:41:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377278.0859075 | source=vosk | rms=347 | updated_at=1787377277.3323948 | frequency_hz=230.0
- [2026-08-22 13:41:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377278.581857 | source=vosk | rms=347 | updated_at=1787377277.3323948 | frequency_hz=230.0
- [2026-08-22 13:41:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377279.3324869 | source=vosk | rms=347 | updated_at=1787377277.3323948 | frequency_hz=230.0
- [2026-08-22 13:41:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377280.0863318 | source=vosk | rms=640 | updated_at=1787377279.5847578 | frequency_hz=230.0
- [2026-08-22 13:41:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377280.5819976 | source=vosk | rms=1203 | updated_at=1787377280.5819976 | frequency_hz=230.0
- [2026-08-22 13:41:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377281.3337252 | source=vosk | rms=1204 | updated_at=1787377280.8326266 | frequency_hz=230.0
- [2026-08-22 13:41:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377285.3425055 | source=vosk | rms=1204 | updated_at=1787377280.8326266 | frequency_hz=230.0
- [2026-08-22 13:41:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377285.8321168 | source=vosk | rms=1204 | updated_at=1787377280.8326266 | frequency_hz=230.0
- [2026-08-22 13:41:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377286.0854807 | source=vosk | rms=322 | updated_at=1787377286.0854807 | frequency_hz=230.0
- [2026-08-22 13:41:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377288.3366117 | source=vosk | rms=1201 | updated_at=1787377287.8325264 | frequency_hz=230.0
- [2026-08-22 13:41:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377289.082811 | source=vosk | rms=509 | updated_at=1787377289.082811 | frequency_hz=230.0
- [2026-08-22 13:41:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377291.3320062 | source=vosk | rms=279 | updated_at=1787377290.5820625 | frequency_hz=230.0
- [2026-08-22 13:41:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377291.5822167 | source=vosk | rms=279 | updated_at=1787377290.5820625 | frequency_hz=230.0
- [2026-08-22 13:41:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377292.5828013 | source=vosk | rms=279 | updated_at=1787377290.5820625 | frequency_hz=230.0
- [2026-08-22 13:41:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377292.8425553 | source=vosk | rms=279 | updated_at=1787377290.5820625 | frequency_hz=230.0
- [2026-08-22 13:41:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377297.331958 | source=vosk | rms=275 | updated_at=1787377296.8329246 | frequency_hz=230.0
- [2026-08-22 13:41:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377298.0872142 | source=vosk | rms=1201 | updated_at=1787377298.0872142 | frequency_hz=230.0
- [2026-08-22 13:41:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377299.081986 | source=vosk | rms=281 | updated_at=1787377298.5819771 | frequency_hz=230.0
- [2026-08-22 13:41:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377300.202516 | source=vosk | rms=281 | updated_at=1787377298.5819771 | frequency_hz=230.0
- [2026-08-22 13:41:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377300.7027962 | source=vosk | rms=281 | updated_at=1787377298.5819771 | frequency_hz=230.0
- [2026-08-22 13:41:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377301.9923787 | source=vosk | rms=1201 | updated_at=1787377301.9923787 | frequency_hz=230.0
- [2026-08-22 13:41:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377302.952946 | source=vosk | rms=278 | updated_at=1787377302.4541364 | frequency_hz=230.0
- [2026-08-22 13:41:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377303.7019968 | source=vosk | rms=308 | updated_at=1787377303.7019968 | frequency_hz=185.2
- [2026-08-22 13:41:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377304.7033572 | source=vosk | rms=1201 | updated_at=1787377304.20265 | frequency_hz=185.2
- [2026-08-22 13:41:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377305.7426097 | source=vosk | rms=1203 | updated_at=1787377305.7426097 | frequency_hz=185.2
- [2026-08-22 13:41:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377306.452655 | source=vosk | rms=1201 | updated_at=1787377305.9526334 | frequency_hz=185.2
- [2026-08-22 13:41:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377312.4721353 | source=vosk | rms=1203 | updated_at=1787377312.4721353 | frequency_hz=185.2
- [2026-08-22 13:41:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377313.2227566 | source=vosk | rms=1202 | updated_at=1787377312.7230124 | frequency_hz=185.2
- [2026-08-22 13:41:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377314.4721377 | source=vosk | rms=1205 | updated_at=1787377314.4721377 | frequency_hz=302.0
- [2026-08-22 13:41:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377315.4722967 | source=vosk | rms=1205 | updated_at=1787377314.9721227 | frequency_hz=302.0
- [2026-08-22 13:41:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377316.4730268 | source=vosk | rms=1200 | updated_at=1787377316.4730268 | frequency_hz=286.0
- [2026-08-22 13:41:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377317.4724658 | source=vosk | rms=1204 | updated_at=1787377316.973789 | frequency_hz=286.0
- [2026-08-22 13:41:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377319.7222967 | source=vosk | rms=1202 | updated_at=1787377319.7222967 | frequency_hz=266.0
- [2026-08-22 13:42:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377320.7224245 | source=vosk | rms=1201 | updated_at=1787377320.2227068 | frequency_hz=266.0
- [2026-08-22 13:42:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377321.7227473 | source=vosk | rms=1203 | updated_at=1787377321.7227473 | frequency_hz=266.0
- [2026-08-22 13:42:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377322.7229638 | source=vosk | rms=892 | updated_at=1787377322.2227862 | frequency_hz=266.0
- [2026-08-22 13:42:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377324.9724424 | source=vosk | rms=1203 | updated_at=1787377324.9724424 | frequency_hz=266.0
- [2026-08-22 13:42:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377325.7232695 | source=vosk | rms=1202 | updated_at=1787377325.225314 | frequency_hz=266.0
- [2026-08-22 13:42:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377328.2565985 | source=vosk | rms=1203 | updated_at=1787377328.2565985 | frequency_hz=266.0
- [2026-08-22 13:42:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377328.974383 | source=vosk | rms=1203 | updated_at=1787377328.4726887 | frequency_hz=266.0
- [2026-08-22 13:42:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377331.7228253 | source=vosk | rms=653 | updated_at=1787377331.7228253 | frequency_hz=348.0
- [2026-08-22 13:42:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377332.7257073 | source=vosk | rms=1203 | updated_at=1787377332.2224524 | frequency_hz=348.0
- [2026-08-22 13:42:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377334.4744484 | source=vosk | rms=938 | updated_at=1787377334.4744484 | frequency_hz=174.0
- [2026-08-22 13:42:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377335.4726882 | source=vosk | rms=1202 | updated_at=1787377334.974299 | frequency_hz=174.0
- [2026-08-22 13:42:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377345.5113947 | source=vosk | rms=1205 | updated_at=1787377345.5113947 | frequency_hz=316.0
- [2026-08-22 13:42:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377346.494205 | source=vosk | rms=1202 | updated_at=1787377345.9932702 | frequency_hz=316.0
- [2026-08-22 13:42:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377350.3033001 | source=vosk | rms=1200 | updated_at=1787377350.3033001 | frequency_hz=316.0
- [2026-08-22 13:42:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377351.0541945 | source=vosk | rms=1200 | updated_at=1787377350.5526857 | frequency_hz=316.0
- [2026-08-22 13:42:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377351.8025675 | source=vosk | rms=1200 | updated_at=1787377350.5526857 | frequency_hz=316.0
- [2026-08-22 13:42:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377352.3045423 | source=vosk | rms=1200 | updated_at=1787377350.5526857 | frequency_hz=316.0
- [2026-08-22 13:42:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377353.8030493 | source=vosk | rms=412 | updated_at=1787377353.8030493 | frequency_hz=316.0
- [2026-08-22 13:42:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377354.302465 | source=vosk | rms=412 | updated_at=1787377353.8030493 | frequency_hz=316.0
- [2026-08-22 13:42:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377355.8024304 | source=vosk | rms=412 | updated_at=1787377353.8030493 | frequency_hz=316.0
- [2026-08-22 13:42:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377356.806989 | source=vosk | rms=200 | updated_at=1787377356.3030133 | frequency_hz=316.0
- [2026-08-22 13:42:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377357.054043 | source=vosk | rms=1204 | updated_at=1787377357.054043 | frequency_hz=316.0
- [2026-08-22 13:42:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377358.0528412 | source=vosk | rms=300 | updated_at=1787377357.553287 | frequency_hz=316.0
- [2026-08-22 13:42:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377365.5531747 | source=vosk | rms=1037 | updated_at=1787377365.5531747 | frequency_hz=192.0
- [2026-08-22 13:42:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377366.5527012 | source=vosk | rms=1201 | updated_at=1787377366.0541632 | frequency_hz=192.0
- [2026-08-22 13:42:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377369.8134122 | source=vosk | rms=1201 | updated_at=1787377366.0541632 | frequency_hz=192.0
- [2026-08-22 13:42:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377370.8134136 | source=vosk | rms=574 | updated_at=1787377370.302735 | frequency_hz=192.0
- [2026-08-22 13:42:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377371.0525203 | source=vosk | rms=574 | updated_at=1787377370.302735 | frequency_hz=192.0
- [2026-08-22 13:42:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787377373.5534139 | source=vosk | rms=261 | updated_at=1787377373.0534928 | frequency_hz=192.0
- [2026-08-22 13:42:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787377374.559722 | source=vosk | rms=1203 | updated_at=1787377374.559722 | frequency_hz=192.0

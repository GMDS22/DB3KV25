# SMART SENTRY V5.0.0 Runtime Conversation Export

- Generated: 2026-08-21 18:32:38
- Entries: 894
- Roles: {'assistant': 4, 'system': 828, 'operator': 62}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 828, 'spoken_confirmation': 2, 'voice_transcript_partial': 52, 'voice_transcript_final': 9, 'voice_command': 1}
- Channels: {'text': 2, 'voice': 892}
- Latest operator request: oh
- Latest assistant message: Running Smart Sentry now. Connecting the Smart Sentry boards first.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-08-21 18:16:41] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-08-21 18:16:41] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-08-21 18:16:43] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787307403.8329592 | source=vosk
- [2026-08-21 18:16:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307408.5040538 | source=vosk
- [2026-08-21 18:16:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307409.0032763 | source=vosk
- [2026-08-21 18:16:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307409.5047956 | source=vosk | rms=281 | updated_at=1787307409.5047956
- [2026-08-21 18:16:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307410.0032055 | source=vosk | rms=281 | updated_at=1787307409.5047956
- [2026-08-21 18:16:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307410.5041108 | source=vosk | rms=151 | updated_at=1787307410.5041108
- [2026-08-21 18:16:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307411.7541714 | source=vosk | rms=144 | updated_at=1787307411.2570846
- [2026-08-21 18:16:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307412.5047686 | source=vosk | rms=144 | updated_at=1787307411.2570846
- [2026-08-21 18:16:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307413.004281 | source=vosk | rms=144 | updated_at=1787307411.2570846
- [2026-08-21 18:16:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307413.5042045 | source=vosk | rms=159 | updated_at=1787307413.5042045
- [2026-08-21 18:16:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307414.2538223 | source=vosk | rms=201 | updated_at=1787307413.754108
- [2026-08-21 18:16:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307414.504391 | source=vosk | rms=134 | updated_at=1787307414.504391
- [2026-08-21 18:16:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307415.5053215 | source=vosk | rms=1200 | updated_at=1787307414.7526674
- [2026-08-21 18:17:20] assistant / spoken_confirmation / voice: Smart Sentry is ready.
  meta: interrupt=True | assistant_output=False | spoken=True
- [2026-08-21 18:16:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307417.0032203 | source=vosk | rms=1200 | updated_at=1787307414.7526674
- [2026-08-21 18:16:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307417.7527976 | source=vosk | rms=405 | updated_at=1787307417.2540493
- [2026-08-21 18:16:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307419.0039723 | source=vosk | rms=405 | updated_at=1787307417.2540493
- [2026-08-21 18:16:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307419.5035062 | source=vosk | rms=405 | updated_at=1787307417.2540493
- [2026-08-21 18:17:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307420.7541091 | source=vosk | rms=405 | updated_at=1787307417.2540493
- [2026-08-21 18:17:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307423.7530062 | source=vosk | rms=148 | updated_at=1787307423.2534537
- [2026-08-21 18:17:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307424.0044563 | source=vosk | rms=121 | updated_at=1787307424.0044563
- [2026-08-21 18:17:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307427.753535 | source=vosk | rms=143 | updated_at=1787307427.2536192
- [2026-08-21 18:17:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307429.253409 | source=vosk | rms=445 | updated_at=1787307429.253409
- [2026-08-21 18:17:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307430.5050826 | source=vosk | rms=319 | updated_at=1787307430.0028527
- [2026-08-21 18:17:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307431.2540286 | source=vosk | rms=319 | updated_at=1787307430.0028527
- [2026-08-21 18:17:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307432.5036495 | source=vosk | rms=195 | updated_at=1787307432.0043359
- [2026-08-21 18:17:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307434.0039268 | source=vosk | rms=138 | updated_at=1787307434.0039268
- [2026-08-21 18:17:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307434.5028882 | source=vosk | rms=138 | updated_at=1787307434.0039268
- [2026-08-21 18:17:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307434.753624 | source=vosk | rms=138 | updated_at=1787307434.0039268
- [2026-08-21 18:17:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307436.5050302 | source=vosk | rms=190 | updated_at=1787307436.0037189
- [2026-08-21 18:17:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307437.2535598 | source=vosk | rms=232 | updated_at=1787307437.2535598
- [2026-08-21 18:17:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307437.7538085 | source=vosk | rms=232 | updated_at=1787307437.2535598
- [2026-08-21 18:17:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307438.253272 | source=vosk | rms=232 | updated_at=1787307437.2535598
- [2026-08-21 18:17:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307439.5047793 | source=vosk | rms=161 | updated_at=1787307439.0037756
- [2026-08-21 18:17:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307439.7547417 | source=vosk | rms=366 | updated_at=1787307439.7547417
- [2026-08-21 18:17:23] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1787307443.3154974 | source=vosk | rms=1202 | updated_at=1787307443.2533054
- [2026-08-21 18:17:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307443.5060065 | source=vosk | rms=1200 | updated_at=1787307443.5060065
- [2026-08-21 18:17:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307443.7547228 | source=vosk | rms=1202 | updated_at=1787307443.7547228
- [2026-08-21 18:17:23] operator / voice_transcript_partial / voice: smart century as
  meta: kind=partial | timestamp=1787307443.8488224 | source=vosk | rms=1202 | updated_at=1787307443.7547228
- [2026-08-21 18:17:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307444.0047073 | source=vosk | rms=430 | updated_at=1787307444.0047073
- [2026-08-21 18:17:24] operator / voice_transcript_partial / voice: smart century is ready
  meta: kind=partial | timestamp=1787307444.0518658 | source=vosk | rms=430 | updated_at=1787307444.0047073
- [2026-08-21 18:17:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307444.254608 | source=vosk | rms=202 | updated_at=1787307444.254608
- [2026-08-21 18:17:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307444.509084 | source=vosk | rms=345 | updated_at=1787307444.509084
- [2026-08-21 18:17:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307444.754666 | source=vosk | rms=487 | updated_at=1787307444.754666
- [2026-08-21 18:17:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307445.0043287 | source=vosk | rms=627 | updated_at=1787307445.0043287
- [2026-08-21 18:17:25] operator / voice_transcript_final / voice: smart sentry is ready
  meta: kind=final | timestamp=1787307445.424667 | source=final | rms=627 | updated_at=1787307445.0043287
- [2026-08-21 18:17:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307445.5720832 | source=vosk | rms=627 | updated_at=1787307445.0043287
- [2026-08-21 18:17:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307445.5720832 | source=vosk | rms=407 | updated_at=1787307445.5720832
- [2026-08-21 18:17:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307449.0120575 | source=vosk | rms=381 | updated_at=1787307448.5099106
- [2026-08-21 18:17:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307449.260228 | source=vosk | rms=450 | updated_at=1787307449.260228
- [2026-08-21 18:17:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307453.2539012 | source=vosk | rms=168 | updated_at=1787307452.7535937
- [2026-08-21 18:17:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307453.5087402 | source=vosk | rms=492 | updated_at=1787307453.5087402
- [2026-08-21 18:17:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307455.0034037 | source=vosk | rms=274 | updated_at=1787307454.2547712
- [2026-08-21 18:17:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307455.5040317 | source=vosk | rms=274 | updated_at=1787307454.2547712
- [2026-08-21 18:17:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307458.50544 | source=vosk | rms=289 | updated_at=1787307457.7584114
- [2026-08-21 18:17:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307458.7541254 | source=vosk | rms=289 | updated_at=1787307457.7584114
- [2026-08-21 18:17:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307459.264072 | source=vosk | rms=289 | updated_at=1787307457.7584114
- [2026-08-21 18:17:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307459.5040698 | source=vosk | rms=380 | updated_at=1787307459.5040698
- [2026-08-21 18:17:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307460.5042467 | source=vosk | rms=380 | updated_at=1787307459.5040698
- [2026-08-21 18:17:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307461.0048041 | source=vosk | rms=373 | updated_at=1787307461.0048041
- [2026-08-21 18:17:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307462.7535663 | source=vosk | rms=373 | updated_at=1787307461.0048041
- [2026-08-21 18:17:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307463.5046773 | source=vosk | rms=257 | updated_at=1787307463.5046773
- [2026-08-21 18:17:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307464.7551365 | source=vosk | rms=363 | updated_at=1787307464.0038319
- [2026-08-21 18:17:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307473.7538733 | source=vosk | rms=398 | updated_at=1787307473.7538733
- [2026-08-21 18:17:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307475.00746 | source=vosk | rms=546 | updated_at=1787307474.0044205
- [2026-08-21 18:17:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307475.5054793 | source=vosk | rms=546 | updated_at=1787307474.0044205
- [2026-08-21 18:17:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307476.0056398 | source=vosk | rms=546 | updated_at=1787307474.0044205
- [2026-08-21 18:17:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307477.0085008 | source=vosk | rms=560 | updated_at=1787307477.0085008
- [2026-08-21 18:17:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307477.75888 | source=vosk | rms=1100 | updated_at=1787307477.293215
- [2026-08-21 18:17:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307478.0040166 | source=vosk | rms=286 | updated_at=1787307478.0040166
- [2026-08-21 18:18:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307482.7537167 | source=vosk | rms=745 | updated_at=1787307482.2765646
- [2026-08-21 18:18:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307483.2547555 | source=vosk | rms=181 | updated_at=1787307483.2547555
- [2026-08-21 18:18:04] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1787307484.5390253 | source=vosk | rms=526 | updated_at=1787307483.755032
- [2026-08-21 18:18:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307485.004157 | source=vosk | rms=526 | updated_at=1787307483.755032
- [2026-08-21 18:18:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307485.5039704 | source=vosk | rms=232 | updated_at=1787307485.5039704
- [2026-08-21 18:18:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307486.0040014 | source=vosk | rms=232 | updated_at=1787307485.5039704
- [2026-08-21 18:18:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307486.5045128 | source=vosk | rms=232 | updated_at=1787307485.5039704
- [2026-08-21 18:18:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307487.0045817 | source=vosk | rms=232 | updated_at=1787307485.5039704
- [2026-08-21 18:18:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307488.0050929 | source=vosk | rms=232 | updated_at=1787307485.5039704
- [2026-08-21 18:18:08] operator / voice_transcript_final / voice: a
  meta: kind=final | timestamp=1787307488.238681 | source=final | rms=232 | updated_at=1787307485.5039704
- [2026-08-21 18:18:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307488.268972 | source=vosk | rms=343 | updated_at=1787307488.268972
- [2026-08-21 18:18:08] operator / voice_transcript_partial / voice: because
  meta: kind=partial | timestamp=1787307488.5406072 | source=vosk | rms=740 | updated_at=1787307488.5076134
- [2026-08-21 18:18:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307488.758942 | source=vosk | rms=514 | updated_at=1787307488.758942
- [2026-08-21 18:18:08] operator / voice_transcript_partial / voice: because a
  meta: kind=partial | timestamp=1787307488.8913736 | source=vosk | rms=514 | updated_at=1787307488.758942
- [2026-08-21 18:18:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307489.005623 | source=vosk | rms=171 | updated_at=1787307489.005623
- [2026-08-21 18:18:09] operator / voice_transcript_partial / voice: because a brilliant
  meta: kind=partial | timestamp=1787307489.134321 | source=vosk | rms=171 | updated_at=1787307489.005623
- [2026-08-21 18:18:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307489.2545605 | source=vosk | rms=302 | updated_at=1787307489.2545605
- [2026-08-21 18:18:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307489.5042331 | source=vosk | rms=340 | updated_at=1787307489.5042331
- [2026-08-21 18:18:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307489.754092 | source=vosk | rms=195 | updated_at=1787307489.754092
- [2026-08-21 18:18:10] operator / voice_transcript_final / voice: because a brilliant
  meta: kind=final | timestamp=1787307490.0722718 | source=final | rms=195 | updated_at=1787307489.754092
- [2026-08-21 18:18:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307490.249622 | source=vosk | rms=195 | updated_at=1787307489.754092
- [2026-08-21 18:18:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307490.249622 | source=vosk | rms=262 | updated_at=1787307490.249622
- [2026-08-21 18:18:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307492.504128 | source=vosk | rms=206 | updated_at=1787307491.0070035
- [2026-08-21 18:18:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307496.8086112 | source=vosk | rms=315 | updated_at=1787307496.8086112
- [2026-08-21 18:18:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307497.2542694 | source=vosk | rms=315 | updated_at=1787307496.8086112
- [2026-08-21 18:18:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307502.3134832 | source=vosk | rms=947 | updated_at=1787307502.3134832
- [2026-08-21 18:18:22] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1787307502.8279378 | source=vosk | rms=670 | updated_at=1787307502.758604
- [2026-08-21 18:18:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307503.0053842 | source=vosk | rms=567 | updated_at=1787307503.0053842
- [2026-08-21 18:18:23] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1787307503.3176756 | source=vosk | rms=300 | updated_at=1787307503.2539594
- [2026-08-21 18:18:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307503.7552857 | source=vosk | rms=300 | updated_at=1787307503.2539594
- [2026-08-21 18:18:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307507.003865 | source=vosk | rms=282 | updated_at=1787307507.003865
- [2026-08-21 18:18:27] operator / voice_transcript_partial / voice: the smarts and
  meta: kind=partial | timestamp=1787307507.084516 | source=vosk | rms=282 | updated_at=1787307507.003865
- [2026-08-21 18:18:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307507.3066504 | source=vosk | rms=439 | updated_at=1787307507.3066504
- [2026-08-21 18:18:27] operator / voice_transcript_partial / voice: the smarts and to
  meta: kind=partial | timestamp=1787307507.3362017 | source=vosk | rms=439 | updated_at=1787307507.3066504
- [2026-08-21 18:18:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307507.755755 | source=vosk | rms=439 | updated_at=1787307507.3066504
- [2026-08-21 18:18:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307508.0046926 | source=vosk | rms=172 | updated_at=1787307508.0046926
- [2026-08-21 18:18:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307508.505956 | source=vosk | rms=172 | updated_at=1787307508.0046926
- [2026-08-21 18:18:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307508.7558963 | source=vosk | rms=172 | updated_at=1787307508.0046926
- [2026-08-21 18:18:29] operator / voice_transcript_final / voice: the smart center
  meta: kind=final | timestamp=1787307509.1184545 | source=final | rms=172 | updated_at=1787307508.0046926
- [2026-08-21 18:18:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307509.2638452 | source=vosk | rms=172 | updated_at=1787307508.0046926
- [2026-08-21 18:18:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307509.2653487 | source=vosk | rms=1204 | updated_at=1787307509.2638452
- [2026-08-21 18:18:31] operator / voice_transcript_partial / voice: billion
  meta: kind=partial | timestamp=1787307511.5227432 | source=vosk | rms=1202 | updated_at=1787307511.504059 | frequency_hz=366.0
- [2026-08-21 18:18:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307511.7558458 | source=vosk | rms=1200 | updated_at=1787307511.7558458 | frequency_hz=366.0
- [2026-08-21 18:18:31] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1787307511.7732956 | source=vosk | rms=1200 | updated_at=1787307511.7558458 | frequency_hz=366.0
- [2026-08-21 18:18:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307512.0100164 | source=vosk | rms=1201 | updated_at=1787307512.0100164 | frequency_hz=366.0
- [2026-08-21 18:18:32] operator / voice_transcript_partial / voice: alien run
  meta: kind=partial | timestamp=1787307512.0285616 | source=vosk | rms=1201 | updated_at=1787307512.0100164 | frequency_hz=366.0
- [2026-08-21 18:18:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307512.2555203 | source=vosk | rms=1200 | updated_at=1787307512.2555203 | frequency_hz=366.0
- [2026-08-21 18:18:32] operator / voice_transcript_partial / voice: alien run this
  meta: kind=partial | timestamp=1787307512.2994196 | source=vosk | rms=1200 | updated_at=1787307512.2555203 | frequency_hz=366.0
- [2026-08-21 18:18:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307512.504299 | source=vosk | rms=1201 | updated_at=1787307512.504299 | frequency_hz=366.0
- [2026-08-21 18:18:32] operator / voice_transcript_partial / voice: alien run the smarts and
  meta: kind=partial | timestamp=1787307512.5210414 | source=vosk | rms=1201 | updated_at=1787307512.504299 | frequency_hz=366.0
- [2026-08-21 18:18:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307513.0048072 | source=vosk | rms=1201 | updated_at=1787307512.504299 | frequency_hz=366.0
- [2026-08-21 18:18:33] operator / voice_transcript_partial / voice: alien run the smarts and three
  meta: kind=partial | timestamp=1787307513.025928 | source=vosk | rms=1201 | updated_at=1787307512.504299 | frequency_hz=366.0
- [2026-08-21 18:18:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307513.2544322 | source=vosk | rms=1202 | updated_at=1787307513.2544322 | frequency_hz=366.0
- [2026-08-21 18:18:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307513.5041273 | source=vosk | rms=1203 | updated_at=1787307513.5041273 | frequency_hz=366.0
- [2026-08-21 18:18:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307513.7557974 | source=vosk | rms=1203 | updated_at=1787307513.7557974 | frequency_hz=366.0
- [2026-08-21 18:18:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307514.004153 | source=vosk | rms=1201 | updated_at=1787307514.004153 | frequency_hz=366.0
- [2026-08-21 18:18:34] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1787307514.0178118 | source=final | rms=1201 | updated_at=1787307514.004153 | frequency_hz=366.0
- [2026-08-21 18:18:34] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787307514.0539799 | source=state | rms=1201 | updated_at=1787307514.004153 | frequency_hz=366.0
- [2026-08-21 18:18:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307514.0539799 | source=state | rms=1201 | updated_at=1787307514.004153 | frequency_hz=366.0
- [2026-08-21 18:18:34] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-08-21 18:18:34] assistant / spoken_confirmation / voice: Running Smart Sentry now. Connecting the Smart Sentry boards first.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-08-21 18:18:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307514.2577875 | source=vosk | rms=711 | updated_at=1787307514.2577875 | frequency_hz=366.0
- [2026-08-21 18:18:37] operator / voice_transcript_partial / voice: thanks
  meta: kind=partial | timestamp=1787307517.3220253 | source=vosk | rms=482 | updated_at=1787307517.253778 | frequency_hz=304.4
- [2026-08-21 18:18:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307517.5046337 | source=vosk | rms=482 | updated_at=1787307517.253778 | frequency_hz=304.4
- [2026-08-21 18:18:37] operator / voice_transcript_partial / voice: makes
  meta: kind=partial | timestamp=1787307517.5382981 | source=vosk | rms=482 | updated_at=1787307517.253778 | frequency_hz=304.4
- [2026-08-21 18:18:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307518.0042462 | source=vosk | rms=482 | updated_at=1787307517.253778 | frequency_hz=304.4
- [2026-08-21 18:18:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307518.253809 | source=vosk | rms=734 | updated_at=1787307518.253809 | frequency_hz=304.4
- [2026-08-21 18:18:38] operator / voice_transcript_partial / voice: thanks centric
  meta: kind=partial | timestamp=1787307518.5270066 | source=vosk | rms=734 | updated_at=1787307518.253809 | frequency_hz=304.4
- [2026-08-21 18:18:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307518.5275111 | source=vosk | rms=603 | updated_at=1787307518.5275111 | frequency_hz=304.4
- [2026-08-21 18:18:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307518.7547708 | source=vosk | rms=605 | updated_at=1787307518.7547708 | frequency_hz=304.4
- [2026-08-21 18:18:38] operator / voice_transcript_partial / voice: thanks centric not
  meta: kind=partial | timestamp=1787307518.7784863 | source=vosk | rms=605 | updated_at=1787307518.7547708 | frequency_hz=304.4
- [2026-08-21 18:18:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307519.0048187 | source=vosk | rms=623 | updated_at=1787307519.0048187 | frequency_hz=304.4
- [2026-08-21 18:18:39] operator / voice_transcript_partial / voice: thanks centric not connecting the
  meta: kind=partial | timestamp=1787307519.0228662 | source=vosk | rms=623 | updated_at=1787307519.0048187 | frequency_hz=304.4
- [2026-08-21 18:18:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307519.2546194 | source=vosk | rms=623 | updated_at=1787307519.0048187 | frequency_hz=304.4
- [2026-08-21 18:18:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307519.5039206 | source=vosk | rms=623 | updated_at=1787307519.0048187 | frequency_hz=304.4
- [2026-08-21 18:18:39] operator / voice_transcript_partial / voice: thanks centric not connecting the smart
  meta: kind=partial | timestamp=1787307519.5159576 | source=vosk | rms=623 | updated_at=1787307519.0048187 | frequency_hz=304.4
- [2026-08-21 18:18:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307519.7540407 | source=vosk | rms=456 | updated_at=1787307519.7540407 | frequency_hz=304.4
- [2026-08-21 18:18:39] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century
  meta: kind=partial | timestamp=1787307519.7730358 | source=vosk | rms=456 | updated_at=1787307519.7540407 | frequency_hz=304.4
- [2026-08-21 18:18:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307520.0738251 | source=vosk | rms=429 | updated_at=1787307520.0738251 | frequency_hz=304.4
- [2026-08-21 18:18:40] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for
  meta: kind=partial | timestamp=1787307520.1176512 | source=vosk | rms=429 | updated_at=1787307520.0738251 | frequency_hz=304.4
- [2026-08-21 18:18:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307520.5039585 | source=vosk | rms=1003 | updated_at=1787307520.5039585 | frequency_hz=304.4
- [2026-08-21 18:18:40] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's
  meta: kind=partial | timestamp=1787307520.576333 | source=vosk | rms=1003 | updated_at=1787307520.5039585 | frequency_hz=304.4
- [2026-08-21 18:18:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307520.7559135 | source=vosk | rms=939 | updated_at=1787307520.7553978 | frequency_hz=304.4
- [2026-08-21 18:18:40] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first
  meta: kind=partial | timestamp=1787307520.7759752 | source=vosk | rms=939 | updated_at=1787307520.7553978 | frequency_hz=304.4
- [2026-08-21 18:18:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307521.2552357 | source=vosk | rms=939 | updated_at=1787307520.7553978 | frequency_hz=304.4
- [2026-08-21 18:18:42] operator / voice_transcript_final / voice: thanks centric not connecting the smart sentry for it s first
  meta: kind=final | timestamp=1787307522.5720427 | source=final | rms=939 | updated_at=1787307520.7553978 | frequency_hz=304.4
- [2026-08-21 18:18:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307524.0038702 | source=vosk | rms=565 | updated_at=1787307524.0038702 | frequency_hz=304.4
- [2026-08-21 18:18:44] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first
  meta: kind=partial | timestamp=1787307524.0225832 | source=vosk | rms=565 | updated_at=1787307524.0038702 | frequency_hz=304.4
- [2026-08-21 18:18:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307524.2545106 | source=vosk | rms=795 | updated_at=1787307524.2545106 | frequency_hz=304.4
- [2026-08-21 18:18:44] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first smartphone
  meta: kind=partial | timestamp=1787307524.3296342 | source=vosk | rms=795 | updated_at=1787307524.2545106 | frequency_hz=304.4
- [2026-08-21 18:18:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307524.5045736 | source=vosk | rms=505 | updated_at=1787307524.5045736 | frequency_hz=304.4
- [2026-08-21 18:18:44] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first smart
  meta: kind=partial | timestamp=1787307524.5178618 | source=vosk | rms=505 | updated_at=1787307524.5045736 | frequency_hz=304.4
- [2026-08-21 18:18:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307525.004438 | source=vosk | rms=443 | updated_at=1787307525.004438 | frequency_hz=304.4
- [2026-08-21 18:18:45] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first smart century
  meta: kind=partial | timestamp=1787307525.026995 | source=vosk | rms=443 | updated_at=1787307525.004438 | frequency_hz=304.4
- [2026-08-21 18:18:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307525.2538621 | source=vosk | rms=443 | updated_at=1787307525.004438 | frequency_hz=304.4
- [2026-08-21 18:18:45] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first smart century rates are
  meta: kind=partial | timestamp=1787307525.3143694 | source=vosk | rms=443 | updated_at=1787307525.004438 | frequency_hz=304.4
- [2026-08-21 18:18:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307525.5046005 | source=vosk | rms=498 | updated_at=1787307525.5046005 | frequency_hz=304.4
- [2026-08-21 18:18:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307525.7540023 | source=vosk | rms=498 | updated_at=1787307525.5046005 | frequency_hz=304.4
- [2026-08-21 18:18:45] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first smart century rates are connected
  meta: kind=partial | timestamp=1787307525.7745943 | source=vosk | rms=498 | updated_at=1787307525.5046005 | frequency_hz=304.4
- [2026-08-21 18:18:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307526.0045302 | source=vosk | rms=577 | updated_at=1787307526.0045302 | frequency_hz=304.4
- [2026-08-21 18:18:46] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first smart century rates are connected on
  meta: kind=partial | timestamp=1787307526.0234613 | source=vosk | rms=577 | updated_at=1787307526.0045302 | frequency_hz=304.4
- [2026-08-21 18:18:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307526.2546492 | source=vosk | rms=410 | updated_at=1787307526.2546492 | frequency_hz=304.4
- [2026-08-21 18:18:46] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first smart century rates are connected on the
  meta: kind=partial | timestamp=1787307526.281259 | source=vosk | rms=410 | updated_at=1787307526.2546492 | frequency_hz=304.4
- [2026-08-21 18:18:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307526.5117207 | source=vosk | rms=428 | updated_at=1787307526.5117207 | frequency_hz=304.4
- [2026-08-21 18:18:46] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first smart century rates are connected on the see
  meta: kind=partial | timestamp=1787307526.5338433 | source=vosk | rms=428 | updated_at=1787307526.5117207 | frequency_hz=304.4
- [2026-08-21 18:18:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307527.0041187 | source=vosk | rms=428 | updated_at=1787307526.5117207 | frequency_hz=304.4
- [2026-08-21 18:18:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307527.5042439 | source=vosk | rms=486 | updated_at=1787307527.5042439 | frequency_hz=304.4
- [2026-08-21 18:18:47] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first smart century rates are connected on the c o
  meta: kind=partial | timestamp=1787307527.5178468 | source=vosk | rms=486 | updated_at=1787307527.5042439 | frequency_hz=304.4
- [2026-08-21 18:18:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307527.774606 | source=vosk | rms=611 | updated_at=1787307527.774606 | frequency_hz=304.4
- [2026-08-21 18:18:47] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first smart century rates are connected on the ceo and
  meta: kind=partial | timestamp=1787307527.7972865 | source=vosk | rms=611 | updated_at=1787307527.774606 | frequency_hz=304.4
- [2026-08-21 18:18:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307528.006212 | source=vosk | rms=393 | updated_at=1787307528.006212 | frequency_hz=304.4
- [2026-08-21 18:18:48] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first smart century rates are connected on the ceo and smart
  meta: kind=partial | timestamp=1787307528.0300095 | source=vosk | rms=393 | updated_at=1787307528.006212 | frequency_hz=304.4
- [2026-08-21 18:18:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307528.2554197 | source=vosk | rms=393 | updated_at=1787307528.006212 | frequency_hz=304.4
- [2026-08-21 18:18:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307528.507294 | source=vosk | rms=393 | updated_at=1787307528.006212 | frequency_hz=304.4
- [2026-08-21 18:18:48] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first smart century rates are connected on the ceo and smart century
  meta: kind=partial | timestamp=1787307528.526975 | source=vosk | rms=393 | updated_at=1787307528.006212 | frequency_hz=304.4
- [2026-08-21 18:18:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307529.0049148 | source=vosk | rms=393 | updated_at=1787307528.006212 | frequency_hz=304.4
- [2026-08-21 18:18:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307529.5049496 | source=vosk | rms=785 | updated_at=1787307529.5049496 | frequency_hz=304.4
- [2026-08-21 18:18:49] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first smart century rates are connected on the ceo and smart century is an
  meta: kind=partial | timestamp=1787307529.5261478 | source=vosk | rms=785 | updated_at=1787307529.5049496 | frequency_hz=304.4
- [2026-08-21 18:18:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307529.756335 | source=vosk | rms=596 | updated_at=1787307529.756335 | frequency_hz=304.4
- [2026-08-21 18:18:49] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first smart century rates are connected on the ceo and smart century is any
  meta: kind=partial | timestamp=1787307529.7889466 | source=vosk | rms=596 | updated_at=1787307529.756335 | frequency_hz=304.4
- [2026-08-21 18:18:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307530.005109 | source=vosk | rms=580 | updated_at=1787307530.005109 | frequency_hz=304.4
- [2026-08-21 18:18:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307530.2549942 | source=vosk | rms=580 | updated_at=1787307530.005109 | frequency_hz=304.4
- [2026-08-21 18:18:50] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first smart century rates are connected on the ceo and smart century is any ask another
  meta: kind=partial | timestamp=1787307530.2856553 | source=vosk | rms=580 | updated_at=1787307530.005109 | frequency_hz=304.4
- [2026-08-21 18:18:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307530.5038261 | source=vosk | rms=717 | updated_at=1787307530.5038261 | frequency_hz=304.4
- [2026-08-21 18:18:50] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first smart century rates are connected on the ceo and smart century is any ask another question
  meta: kind=partial | timestamp=1787307530.5315516 | source=vosk | rms=717 | updated_at=1787307530.5038261 | frequency_hz=304.4
- [2026-08-21 18:18:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307531.0142627 | source=vosk | rms=717 | updated_at=1787307530.5038261 | frequency_hz=304.4
- [2026-08-21 18:18:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307531.2963572 | source=vosk | rms=717 | updated_at=1787307530.5038261 | frequency_hz=304.4
- [2026-08-21 18:18:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307531.504092 | source=vosk | rms=717 | updated_at=1787307530.5038261 | frequency_hz=304.4
- [2026-08-21 18:18:51] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first smart century rates are connected on the ceo and smart century is any ask another question or
  meta: kind=partial | timestamp=1787307531.525428 | source=vosk | rms=717 | updated_at=1787307530.5038261 | frequency_hz=304.4
- [2026-08-21 18:18:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307531.7540522 | source=vosk | rms=717 | updated_at=1787307530.5038261 | frequency_hz=304.4
- [2026-08-21 18:18:51] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first smart century rates are connected on the ceo and smart century is any ask another question or given
  meta: kind=partial | timestamp=1787307531.788396 | source=vosk | rms=717 | updated_at=1787307530.5038261 | frequency_hz=304.4
- [2026-08-21 18:18:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307532.2549233 | source=vosk | rms=717 | updated_at=1787307530.5038261 | frequency_hz=304.4
- [2026-08-21 18:18:52] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first smart century rates are connected on the ceo and smart century is any ask another question or give another
  meta: kind=partial | timestamp=1787307532.2772317 | source=vosk | rms=717 | updated_at=1787307530.5038261 | frequency_hz=304.4
- [2026-08-21 18:18:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307532.7727168 | source=vosk | rms=717 | updated_at=1787307530.5038261 | frequency_hz=304.4
- [2026-08-21 18:19:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307545.254135 | source=vosk | rms=1200 | updated_at=1787307545.254135 | frequency_hz=304.4
- [2026-08-21 18:19:05] operator / voice_transcript_partial / voice: thanks centric not connecting the smart century for it's first smart century rates are connected on the ceo and smart century is any ask another question or give another coming right
  meta: kind=partial | timestamp=1787307545.3232298 | source=vosk | rms=1200 | updated_at=1787307545.254135 | frequency_hz=304.4
- [2026-08-21 18:19:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307545.5039597 | source=vosk | rms=1200 | updated_at=1787307545.5039597 | frequency_hz=311.3
- [2026-08-21 18:19:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307545.7556717 | source=vosk | rms=1206 | updated_at=1787307545.7556717 | frequency_hz=264.6
- [2026-08-21 18:19:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307546.004139 | source=vosk | rms=1204 | updated_at=1787307546.004139 | frequency_hz=289.6
- [2026-08-21 18:19:06] operator / voice_transcript_final / voice: thanks centric not connecting the smart sentry for it s first smart sentry rates are connect on the c o and smart sentry is any ask another question or give another coming right
  meta: kind=final | timestamp=1787307546.4437284 | source=final | rms=1204 | updated_at=1787307546.004139 | frequency_hz=289.6
- [2026-08-21 18:19:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307546.9086745 | source=vosk | rms=1204 | updated_at=1787307546.004139 | frequency_hz=289.6
- [2026-08-21 18:19:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307546.9086745 | source=vosk | rms=1203 | updated_at=1787307546.9086745 | frequency_hz=289.6
- [2026-08-21 18:19:08] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1787307548.3234556 | source=vosk | rms=3577 | updated_at=1787307548.3088062 | frequency_hz=212.7
- [2026-08-21 18:19:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307548.5102327 | source=vosk | rms=3053 | updated_at=1787307548.5102327 | frequency_hz=212.7
- [2026-08-21 18:19:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307548.8086572 | source=vosk | rms=1481 | updated_at=1787307548.8086572 | frequency_hz=212.7
- [2026-08-21 18:19:08] operator / voice_transcript_partial / voice: alien show me the
  meta: kind=partial | timestamp=1787307548.9063587 | source=vosk | rms=1481 | updated_at=1787307548.8086572 | frequency_hz=212.7
- [2026-08-21 18:19:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307549.0047734 | source=vosk | rms=2410 | updated_at=1787307549.0047734 | frequency_hz=212.7
- [2026-08-21 18:19:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307549.2620306 | source=vosk | rms=1230 | updated_at=1787307549.2620306 | frequency_hz=274.8
- [2026-08-21 18:19:09] operator / voice_transcript_partial / voice: alien show me the said
  meta: kind=partial | timestamp=1787307549.3281295 | source=vosk | rms=1230 | updated_at=1787307549.2620306 | frequency_hz=274.8
- [2026-08-21 18:19:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307549.5046456 | source=vosk | rms=1442 | updated_at=1787307549.5046456 | frequency_hz=273.8
- [2026-08-21 18:19:09] operator / voice_transcript_partial / voice: alien show me the settings tab
  meta: kind=partial | timestamp=1787307549.54075 | source=vosk | rms=1442 | updated_at=1787307549.5046456 | frequency_hz=273.8
- [2026-08-21 18:19:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307549.753823 | source=vosk | rms=1437 | updated_at=1787307549.753823 | frequency_hz=218.6
- [2026-08-21 18:19:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307550.0049913 | source=vosk | rms=621 | updated_at=1787307550.0049913 | frequency_hz=252.7
- [2026-08-21 18:19:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307550.3074548 | source=vosk | rms=1200 | updated_at=1787307550.3074548 | frequency_hz=270.7
- [2026-08-21 18:19:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307550.84692 | source=state | rms=1200 | updated_at=1787307550.3074548 | frequency_hz=270.7
- [2026-08-21 18:19:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307550.84692 | source=vosk | rms=922 | updated_at=1787307550.84692 | frequency_hz=270.7
- [2026-08-21 18:19:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307551.5050058 | source=vosk | rms=922 | updated_at=1787307550.84692 | frequency_hz=270.7
- [2026-08-21 18:19:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307552.2557566 | source=vosk | rms=289 | updated_at=1787307552.2557566 | frequency_hz=270.7
- [2026-08-21 18:19:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307552.7558923 | source=vosk | rms=289 | updated_at=1787307552.2557566 | frequency_hz=270.7
- [2026-08-21 18:19:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307554.3486774 | source=vosk | rms=289 | updated_at=1787307552.2557566 | frequency_hz=270.7
- [2026-08-21 18:19:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307554.8594937 | source=vosk | rms=289 | updated_at=1787307552.2557566 | frequency_hz=270.7
- [2026-08-21 18:19:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307555.6058347 | source=vosk | rms=289 | updated_at=1787307552.2557566 | frequency_hz=270.7
- [2026-08-21 18:19:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307556.094863 | source=vosk | rms=289 | updated_at=1787307552.2557566 | frequency_hz=270.7
- [2026-08-21 18:19:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307556.3449361 | source=vosk | rms=289 | updated_at=1787307552.2557566 | frequency_hz=270.7
- [2026-08-21 18:19:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307559.6008635 | source=vosk | rms=1205 | updated_at=1787307559.0945995 | frequency_hz=281.0
- [2026-08-21 18:19:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307563.5959356 | source=vosk | rms=716 | updated_at=1787307563.5959356 | frequency_hz=281.0
- [2026-08-21 18:19:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307564.3449936 | source=vosk | rms=615 | updated_at=1787307563.8466492 | frequency_hz=281.0
- [2026-08-21 18:19:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307569.349013 | source=vosk | rms=615 | updated_at=1787307563.8466492 | frequency_hz=281.0
- [2026-08-21 18:19:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307570.595132 | source=vosk | rms=856 | updated_at=1787307570.098024 | frequency_hz=281.0
- [2026-08-21 18:19:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307570.8691483 | source=vosk | rms=856 | updated_at=1787307570.098024 | frequency_hz=281.0
- [2026-08-21 18:19:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307572.3460836 | source=vosk | rms=856 | updated_at=1787307570.098024 | frequency_hz=281.0
- [2026-08-21 18:19:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307572.5961266 | source=vosk | rms=856 | updated_at=1787307570.098024 | frequency_hz=281.0
- [2026-08-21 18:19:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307573.3451405 | source=vosk | rms=728 | updated_at=1787307572.8528097 | frequency_hz=281.0
- [2026-08-21 18:19:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307573.8448026 | source=vosk | rms=1203 | updated_at=1787307573.8448026 | frequency_hz=281.0
- [2026-08-21 18:19:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307575.0949447 | source=vosk | rms=1203 | updated_at=1787307573.8448026 | frequency_hz=281.0
- [2026-08-21 18:19:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307575.3445947 | source=vosk | rms=1203 | updated_at=1787307573.8448026 | frequency_hz=281.0
- [2026-08-21 18:19:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307576.0946016 | source=vosk | rms=1203 | updated_at=1787307573.8448026 | frequency_hz=281.0
- [2026-08-21 18:19:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307578.0943446 | source=vosk | rms=522 | updated_at=1787307578.0943446 | frequency_hz=281.0
- [2026-08-21 18:19:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307578.5960383 | source=vosk | rms=522 | updated_at=1787307578.0943446 | frequency_hz=281.0
- [2026-08-21 18:19:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307578.8443892 | source=vosk | rms=522 | updated_at=1787307578.0943446 | frequency_hz=281.0
- [2026-08-21 18:19:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307579.3447983 | source=vosk | rms=522 | updated_at=1787307578.0943446 | frequency_hz=281.0
- [2026-08-21 18:19:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307581.3448637 | source=vosk | rms=450 | updated_at=1787307581.3448637 | frequency_hz=281.0
- [2026-08-21 18:19:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307581.8450372 | source=vosk | rms=450 | updated_at=1787307581.3448637 | frequency_hz=281.0
- [2026-08-21 18:19:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307582.8700035 | source=vosk | rms=450 | updated_at=1787307581.3448637 | frequency_hz=281.0
- [2026-08-21 18:19:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307583.3445647 | source=vosk | rms=450 | updated_at=1787307581.3448637 | frequency_hz=281.0
- [2026-08-21 18:19:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307586.84403 | source=vosk | rms=548 | updated_at=1787307586.84403 | frequency_hz=281.0
- [2026-08-21 18:19:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307587.3458295 | source=vosk | rms=548 | updated_at=1787307586.84403 | frequency_hz=281.0
- [2026-08-21 18:19:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307587.5960338 | source=vosk | rms=914 | updated_at=1787307587.5960338 | frequency_hz=281.0
- [2026-08-21 18:19:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307588.0942974 | source=vosk | rms=914 | updated_at=1787307587.5960338 | frequency_hz=281.0
- [2026-08-21 18:19:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307588.3450668 | source=vosk | rms=567 | updated_at=1787307588.3450668 | frequency_hz=281.0
- [2026-08-21 18:19:48] operator / voice_transcript_final / voice: oh fuck
  meta: kind=final | timestamp=1787307588.7975576 | source=final | rms=567 | updated_at=1787307588.3450668 | frequency_hz=281.0
- [2026-08-21 18:19:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307589.6049604 | source=vosk | rms=567 | updated_at=1787307588.3450668 | frequency_hz=281.0
- [2026-08-21 18:19:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307589.6049604 | source=vosk | rms=638 | updated_at=1787307589.6049604 | frequency_hz=281.0
- [2026-08-21 18:19:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307590.5961528 | source=vosk | rms=638 | updated_at=1787307589.6049604 | frequency_hz=281.0
- [2026-08-21 18:19:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307590.8458495 | source=vosk | rms=336 | updated_at=1787307590.8458495 | frequency_hz=281.0
- [2026-08-21 18:19:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307596.5959954 | source=vosk | rms=561 | updated_at=1787307596.0973895 | frequency_hz=281.0
- [2026-08-21 18:19:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307598.4948611 | source=vosk | rms=387 | updated_at=1787307598.4948611 | frequency_hz=281.0
- [2026-08-21 18:19:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307599.4943929 | source=vosk | rms=306 | updated_at=1787307598.9959517 | frequency_hz=281.0
- [2026-08-21 18:20:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307600.4270349 | source=vosk | rms=306 | updated_at=1787307598.9959517 | frequency_hz=281.0
- [2026-08-21 18:20:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307601.2452006 | source=vosk | rms=306 | updated_at=1787307598.9959517 | frequency_hz=281.0
- [2026-08-21 18:20:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307601.7460706 | source=vosk | rms=335 | updated_at=1787307601.7460706 | frequency_hz=281.0
- [2026-08-21 18:20:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307602.9947581 | source=vosk | rms=358 | updated_at=1787307602.4949913 | frequency_hz=281.0
- [2026-08-21 18:20:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307603.4948926 | source=vosk | rms=358 | updated_at=1787307602.4949913 | frequency_hz=281.0
- [2026-08-21 18:20:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307607.2445717 | source=vosk | rms=538 | updated_at=1787307606.7443967 | frequency_hz=281.0
- [2026-08-21 18:20:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307607.4947052 | source=vosk | rms=538 | updated_at=1787307606.7443967 | frequency_hz=281.0
- [2026-08-21 18:20:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307608.2443874 | source=vosk | rms=538 | updated_at=1787307606.7443967 | frequency_hz=281.0
- [2026-08-21 18:20:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307608.4947677 | source=vosk | rms=927 | updated_at=1787307608.4947677 | frequency_hz=281.0
- [2026-08-21 18:20:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307609.0189347 | source=vosk | rms=927 | updated_at=1787307608.4947677 | frequency_hz=281.0
- [2026-08-21 18:20:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307609.244737 | source=vosk | rms=927 | updated_at=1787307608.4947677 | frequency_hz=281.0
- [2026-08-21 18:20:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307611.2448485 | source=vosk | rms=1202 | updated_at=1787307610.7445316 | frequency_hz=281.0
- [2026-08-21 18:20:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307611.9951835 | source=vosk | rms=1202 | updated_at=1787307610.7445316 | frequency_hz=281.0
- [2026-08-21 18:20:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307614.7455037 | source=vosk | rms=1201 | updated_at=1787307614.2503805 | frequency_hz=281.0
- [2026-08-21 18:20:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307615.245641 | source=vosk | rms=1201 | updated_at=1787307614.2503805 | frequency_hz=281.0
- [2026-08-21 18:20:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307616.2460613 | source=vosk | rms=926 | updated_at=1787307615.7454147 | frequency_hz=281.0
- [2026-08-21 18:20:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307617.5046055 | source=vosk | rms=478 | updated_at=1787307617.5046055 | frequency_hz=281.0
- [2026-08-21 18:20:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307618.5046287 | source=vosk | rms=1202 | updated_at=1787307618.005167 | frequency_hz=281.0
- [2026-08-21 18:20:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307619.5049598 | source=vosk | rms=1037 | updated_at=1787307619.5049598 | frequency_hz=281.0
- [2026-08-21 18:20:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307620.0047169 | source=vosk | rms=1037 | updated_at=1787307619.5049598 | frequency_hz=281.0
- [2026-08-21 18:20:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307621.007739 | source=vosk | rms=1202 | updated_at=1787307621.007739 | frequency_hz=281.0
- [2026-08-21 18:20:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307621.9789767 | source=vosk | rms=1200 | updated_at=1787307621.5051594 | frequency_hz=281.0
- [2026-08-21 18:20:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307622.2690294 | source=vosk | rms=636 | updated_at=1787307622.2690294 | frequency_hz=281.0
- [2026-08-21 18:20:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307623.5076985 | source=vosk | rms=1200 | updated_at=1787307623.0051596 | frequency_hz=281.0
- [2026-08-21 18:20:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307624.0046089 | source=vosk | rms=498 | updated_at=1787307624.0046089 | frequency_hz=281.0
- [2026-08-21 18:20:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307625.5090013 | source=vosk | rms=1200 | updated_at=1787307625.0050845 | frequency_hz=281.0
- [2026-08-21 18:20:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307626.004604 | source=vosk | rms=1201 | updated_at=1787307626.004604 | frequency_hz=281.0
- [2026-08-21 18:20:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307627.0042 | source=vosk | rms=473 | updated_at=1787307626.5048394 | frequency_hz=281.0
- [2026-08-21 18:20:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307628.2546668 | source=vosk | rms=697 | updated_at=1787307628.2546668 | frequency_hz=281.0
- [2026-08-21 18:20:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307628.7562609 | source=vosk | rms=697 | updated_at=1787307628.2546668 | frequency_hz=281.0
- [2026-08-21 18:20:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307630.7544785 | source=vosk | rms=871 | updated_at=1787307630.7544785 | frequency_hz=281.0
- [2026-08-21 18:20:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307631.7566414 | source=vosk | rms=1201 | updated_at=1787307631.2548022 | frequency_hz=281.0
- [2026-08-21 18:20:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307632.75506 | source=vosk | rms=885 | updated_at=1787307632.75506 | frequency_hz=281.0
- [2026-08-21 18:20:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307633.2546892 | source=vosk | rms=885 | updated_at=1787307632.75506 | frequency_hz=281.0
- [2026-08-21 18:20:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307636.255502 | source=vosk | rms=927 | updated_at=1787307636.255502 | frequency_hz=281.0
- [2026-08-21 18:20:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307637.0064516 | source=vosk | rms=671 | updated_at=1787307636.5054195 | frequency_hz=281.0
- [2026-08-21 18:20:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307637.7563648 | source=vosk | rms=671 | updated_at=1787307636.5054195 | frequency_hz=281.0
- [2026-08-21 18:20:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307638.254608 | source=vosk | rms=671 | updated_at=1787307636.5054195 | frequency_hz=281.0
- [2026-08-21 18:20:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307638.7550538 | source=vosk | rms=671 | updated_at=1787307636.5054195 | frequency_hz=281.0
- [2026-08-21 18:20:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307639.2550042 | source=vosk | rms=671 | updated_at=1787307636.5054195 | frequency_hz=281.0
- [2026-08-21 18:20:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307640.265308 | source=vosk | rms=671 | updated_at=1787307636.5054195 | frequency_hz=281.0
- [2026-08-21 18:20:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307642.2550569 | source=vosk | rms=518 | updated_at=1787307641.2544792 | frequency_hz=281.0
- [2026-08-21 18:20:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307642.7553484 | source=vosk | rms=1207 | updated_at=1787307642.7553484 | frequency_hz=281.0
- [2026-08-21 18:20:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307652.1448414 | source=vosk | rms=831 | updated_at=1787307651.644859 | frequency_hz=281.0
- [2026-08-21 18:20:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307652.3967068 | source=vosk | rms=449 | updated_at=1787307652.3967068 | frequency_hz=281.0
- [2026-08-21 18:20:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307656.8962486 | source=vosk | rms=469 | updated_at=1787307656.145063 | frequency_hz=281.0
- [2026-08-21 18:20:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307657.645019 | source=vosk | rms=469 | updated_at=1787307656.145063 | frequency_hz=281.0
- [2026-08-21 18:20:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307658.1447852 | source=vosk | rms=469 | updated_at=1787307656.145063 | frequency_hz=281.0
- [2026-08-21 18:20:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307658.408202 | source=vosk | rms=469 | updated_at=1787307656.145063 | frequency_hz=281.0
- [2026-08-21 18:20:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307659.6504288 | source=vosk | rms=613 | updated_at=1787307658.8949637 | frequency_hz=281.0
- [2026-08-21 18:20:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307659.8958452 | source=vosk | rms=1201 | updated_at=1787307659.8958452 | frequency_hz=281.0
- [2026-08-21 18:21:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307660.6455572 | source=vosk | rms=1202 | updated_at=1787307660.1461656 | frequency_hz=281.0
- [2026-08-21 18:21:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307662.395523 | source=vosk | rms=1202 | updated_at=1787307660.1461656 | frequency_hz=281.0
- [2026-08-21 18:21:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307663.897319 | source=vosk | rms=588 | updated_at=1787307663.4377182 | frequency_hz=281.0
- [2026-08-21 18:21:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307674.4174113 | source=vosk | rms=1201 | updated_at=1787307674.4174113 | frequency_hz=281.0
- [2026-08-21 18:21:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307675.3956785 | source=vosk | rms=1205 | updated_at=1787307674.8949184 | frequency_hz=281.0
- [2026-08-21 18:21:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307676.1453497 | source=vosk | rms=1205 | updated_at=1787307674.8949184 | frequency_hz=281.0
- [2026-08-21 18:21:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307677.6455505 | source=vosk | rms=1201 | updated_at=1787307677.145262 | frequency_hz=281.0
- [2026-08-21 18:21:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307684.1464527 | source=vosk | rms=1202 | updated_at=1787307684.1464527 | frequency_hz=281.0
- [2026-08-21 18:21:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307685.1454349 | source=vosk | rms=767 | updated_at=1787307684.645487 | frequency_hz=281.0
- [2026-08-21 18:21:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307687.8957877 | source=vosk | rms=1201 | updated_at=1787307687.8957877 | frequency_hz=281.0
- [2026-08-21 18:21:28] operator / voice_transcript_final / voice: oh
  meta: kind=final | timestamp=1787307688.186923 | source=final | rms=1201 | updated_at=1787307687.8957877 | frequency_hz=281.0
- [2026-08-21 18:21:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307688.2338681 | source=vosk | rms=1200 | updated_at=1787307688.2338681 | frequency_hz=281.0
- [2026-08-21 18:21:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307688.8953745 | source=vosk | rms=1200 | updated_at=1787307688.2338681 | frequency_hz=281.0
- [2026-08-21 18:21:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307689.395798 | source=vosk | rms=1200 | updated_at=1787307689.395798 | frequency_hz=254.1
- [2026-08-21 18:21:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307690.3957431 | source=vosk | rms=1202 | updated_at=1787307689.8954792 | frequency_hz=254.1
- [2026-08-21 18:21:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307696.1459 | source=vosk | rms=1203 | updated_at=1787307696.1459 | frequency_hz=274.0
- [2026-08-21 18:21:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307697.1457586 | source=vosk | rms=1201 | updated_at=1787307696.6451879 | frequency_hz=274.0
- [2026-08-21 18:21:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307699.8964443 | source=vosk | rms=1201 | updated_at=1787307699.8949406 | frequency_hz=274.0
- [2026-08-21 18:21:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307700.6468275 | source=vosk | rms=1200 | updated_at=1787307700.1481729 | frequency_hz=274.0
- [2026-08-21 18:21:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307702.1456215 | source=vosk | rms=1200 | updated_at=1787307700.1481729 | frequency_hz=274.0
- [2026-08-21 18:21:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307702.9052773 | source=vosk | rms=1200 | updated_at=1787307700.1481729 | frequency_hz=274.0
- [2026-08-21 18:21:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307703.6470258 | source=vosk | rms=1201 | updated_at=1787307703.6470258 | frequency_hz=246.0
- [2026-08-21 18:21:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307704.6452646 | source=vosk | rms=1201 | updated_at=1787307704.1452615 | frequency_hz=246.0
- [2026-08-21 18:21:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307705.1453824 | source=vosk | rms=557 | updated_at=1787307705.1453824 | frequency_hz=246.0
- [2026-08-21 18:21:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307705.651093 | source=vosk | rms=557 | updated_at=1787307705.1453824 | frequency_hz=246.0
- [2026-08-21 18:21:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307707.5557868 | source=vosk | rms=1200 | updated_at=1787307707.5557868 | frequency_hz=246.0
- [2026-08-21 18:21:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307708.305173 | source=vosk | rms=1200 | updated_at=1787307707.8056896 | frequency_hz=246.0
- [2026-08-21 18:21:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307708.555848 | source=vosk | rms=381 | updated_at=1787307708.555848 | frequency_hz=246.0
- [2026-08-21 18:21:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307709.0558586 | source=vosk | rms=381 | updated_at=1787307708.555848 | frequency_hz=246.0
- [2026-08-21 18:21:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307709.306756 | source=vosk | rms=262 | updated_at=1787307709.306756 | frequency_hz=246.0
- [2026-08-21 18:21:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307711.555131 | source=vosk | rms=1202 | updated_at=1787307711.0560882 | frequency_hz=246.0
- [2026-08-21 18:21:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307712.557004 | source=vosk | rms=1202 | updated_at=1787307711.0560882 | frequency_hz=246.0
- [2026-08-21 18:21:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307713.0561612 | source=vosk | rms=1202 | updated_at=1787307711.0560882 | frequency_hz=246.0
- [2026-08-21 18:21:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307714.3087397 | source=vosk | rms=303 | updated_at=1787307714.3087397 | frequency_hz=246.0
- [2026-08-21 18:21:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307714.8070512 | source=vosk | rms=303 | updated_at=1787307714.3087397 | frequency_hz=246.0
- [2026-08-21 18:21:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307715.0560725 | source=vosk | rms=303 | updated_at=1787307714.3087397 | frequency_hz=246.0
- [2026-08-21 18:21:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307715.8053758 | source=vosk | rms=371 | updated_at=1787307715.3059943 | frequency_hz=246.0
- [2026-08-21 18:21:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307716.0558646 | source=vosk | rms=271 | updated_at=1787307716.0558646 | frequency_hz=246.0
- [2026-08-21 18:21:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307716.805555 | source=vosk | rms=271 | updated_at=1787307716.0558646 | frequency_hz=246.0
- [2026-08-21 18:21:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307717.0554042 | source=vosk | rms=358 | updated_at=1787307717.0554042 | frequency_hz=246.0
- [2026-08-21 18:21:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307719.3060513 | source=vosk | rms=435 | updated_at=1787307718.8060176 | frequency_hz=246.0
- [2026-08-21 18:21:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307719.5598605 | source=vosk | rms=437 | updated_at=1787307719.5598605 | frequency_hz=246.0
- [2026-08-21 18:22:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307720.0559874 | source=vosk | rms=437 | updated_at=1787307719.5598605 | frequency_hz=246.0
- [2026-08-21 18:22:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307720.306006 | source=vosk | rms=437 | updated_at=1787307719.5598605 | frequency_hz=246.0
- [2026-08-21 18:22:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307721.8054 | source=vosk | rms=898 | updated_at=1787307721.305995 | frequency_hz=246.0
- [2026-08-21 18:22:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307722.0567122 | source=vosk | rms=459 | updated_at=1787307722.0567122 | frequency_hz=246.0
- [2026-08-21 18:22:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307722.5553718 | source=vosk | rms=459 | updated_at=1787307722.0567122 | frequency_hz=246.0
- [2026-08-21 18:22:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307722.8057213 | source=vosk | rms=317 | updated_at=1787307722.8057213 | frequency_hz=246.0
- [2026-08-21 18:22:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307723.3053684 | source=vosk | rms=317 | updated_at=1787307722.8057213 | frequency_hz=246.0
- [2026-08-21 18:22:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307723.8070107 | source=vosk | rms=498 | updated_at=1787307723.8070107 | frequency_hz=246.0
- [2026-08-21 18:22:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307724.3055031 | source=vosk | rms=498 | updated_at=1787307723.8070107 | frequency_hz=246.0
- [2026-08-21 18:22:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307724.5555894 | source=vosk | rms=498 | updated_at=1787307723.8070107 | frequency_hz=246.0
- [2026-08-21 18:22:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307725.0568936 | source=vosk | rms=498 | updated_at=1787307723.8070107 | frequency_hz=246.0
- [2026-08-21 18:22:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307725.3058877 | source=vosk | rms=283 | updated_at=1787307725.3058877 | frequency_hz=246.0
- [2026-08-21 18:22:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307726.054923 | source=vosk | rms=283 | updated_at=1787307725.3058877 | frequency_hz=246.0
- [2026-08-21 18:22:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307726.3108175 | source=vosk | rms=341 | updated_at=1787307726.3108175 | frequency_hz=246.0
- [2026-08-21 18:22:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307727.5606472 | source=vosk | rms=426 | updated_at=1787307727.05519 | frequency_hz=246.0
- [2026-08-21 18:22:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307727.8060672 | source=vosk | rms=292 | updated_at=1787307727.8060672 | frequency_hz=246.0
- [2026-08-21 18:22:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307729.5586529 | source=vosk | rms=1203 | updated_at=1787307729.06553 | frequency_hz=296.4
- [2026-08-21 18:22:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307730.0551298 | source=vosk | rms=1203 | updated_at=1787307729.06553 | frequency_hz=296.4
- [2026-08-21 18:22:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307730.590525 | source=vosk | rms=1203 | updated_at=1787307729.06553 | frequency_hz=296.4
- [2026-08-21 18:22:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307730.80645 | source=vosk | rms=408 | updated_at=1787307730.80645 | frequency_hz=296.4
- [2026-08-21 18:22:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307731.3220758 | source=vosk | rms=408 | updated_at=1787307730.80645 | frequency_hz=296.4
- [2026-08-21 18:22:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307731.556113 | source=vosk | rms=414 | updated_at=1787307731.556113 | frequency_hz=296.4
- [2026-08-21 18:22:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307732.0559244 | source=vosk | rms=414 | updated_at=1787307731.556113 | frequency_hz=296.4
- [2026-08-21 18:22:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307732.3066738 | source=vosk | rms=357 | updated_at=1787307732.306157 | frequency_hz=296.4
- [2026-08-21 18:22:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307732.807081 | source=vosk | rms=357 | updated_at=1787307732.306157 | frequency_hz=296.4
- [2026-08-21 18:22:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307733.0563178 | source=vosk | rms=371 | updated_at=1787307733.0563178 | frequency_hz=296.4
- [2026-08-21 18:22:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307733.5558395 | source=vosk | rms=371 | updated_at=1787307733.0563178 | frequency_hz=296.4
- [2026-08-21 18:22:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307733.8057017 | source=vosk | rms=388 | updated_at=1787307733.8057017 | frequency_hz=296.4
- [2026-08-21 18:22:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307734.3189435 | source=vosk | rms=388 | updated_at=1787307733.8057017 | frequency_hz=296.4
- [2026-08-21 18:22:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307734.555295 | source=vosk | rms=344 | updated_at=1787307734.555295 | frequency_hz=296.4
- [2026-08-21 18:22:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307735.0554578 | source=vosk | rms=344 | updated_at=1787307734.555295 | frequency_hz=296.4
- [2026-08-21 18:22:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307735.3058798 | source=vosk | rms=346 | updated_at=1787307735.3058798 | frequency_hz=296.4
- [2026-08-21 18:22:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307735.806903 | source=vosk | rms=346 | updated_at=1787307735.3058798 | frequency_hz=296.4
- [2026-08-21 18:22:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307736.2398062 | source=vosk | rms=376 | updated_at=1787307736.2398062 | frequency_hz=296.4
- [2026-08-21 18:22:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307736.8059857 | source=vosk | rms=376 | updated_at=1787307736.2398062 | frequency_hz=296.4
- [2026-08-21 18:22:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307737.0556974 | source=vosk | rms=419 | updated_at=1787307737.0556974 | frequency_hz=296.4
- [2026-08-21 18:22:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307739.256186 | source=vosk | rms=1200 | updated_at=1787307738.756026 | frequency_hz=296.4
- [2026-08-21 18:22:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307739.7560003 | source=vosk | rms=1200 | updated_at=1787307738.756026 | frequency_hz=296.4
- [2026-08-21 18:22:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307740.2552807 | source=vosk | rms=1200 | updated_at=1787307738.756026 | frequency_hz=296.4
- [2026-08-21 18:22:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307740.7854385 | source=vosk | rms=1201 | updated_at=1787307740.7854385 | frequency_hz=296.4
- [2026-08-21 18:22:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307748.8555722 | source=vosk | rms=1200 | updated_at=1787307748.3573732 | frequency_hz=296.4
- [2026-08-21 18:22:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307749.3553684 | source=vosk | rms=1200 | updated_at=1787307748.3573732 | frequency_hz=296.4
- [2026-08-21 18:22:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307751.8556235 | source=vosk | rms=1206 | updated_at=1787307751.3560627 | frequency_hz=296.4
- [2026-08-21 18:22:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307752.1054044 | source=vosk | rms=391 | updated_at=1787307752.1054044 | frequency_hz=296.4
- [2026-08-21 18:22:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307752.6380897 | source=vosk | rms=391 | updated_at=1787307752.1054044 | frequency_hz=296.4
- [2026-08-21 18:22:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307752.8560107 | source=vosk | rms=468 | updated_at=1787307752.8560107 | frequency_hz=296.4
- [2026-08-21 18:22:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307753.356098 | source=vosk | rms=468 | updated_at=1787307752.8560107 | frequency_hz=296.4
- [2026-08-21 18:22:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307753.605945 | source=vosk | rms=403 | updated_at=1787307753.605945 | frequency_hz=296.4
- [2026-08-21 18:22:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307755.6062808 | source=vosk | rms=384 | updated_at=1787307755.106259 | frequency_hz=296.4
- [2026-08-21 18:22:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307755.8560948 | source=vosk | rms=384 | updated_at=1787307755.106259 | frequency_hz=296.4
- [2026-08-21 18:22:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307758.6052175 | source=vosk | rms=518 | updated_at=1787307758.1065204 | frequency_hz=296.4
- [2026-08-21 18:22:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307758.8593378 | source=vosk | rms=518 | updated_at=1787307758.1065204 | frequency_hz=296.4
- [2026-08-21 18:22:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307759.5712664 | source=vosk | rms=518 | updated_at=1787307758.1065204 | frequency_hz=296.4
- [2026-08-21 18:22:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307759.6063836 | source=vosk | rms=518 | updated_at=1787307758.1065204 | frequency_hz=296.4
- [2026-08-21 18:22:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307760.1057932 | source=vosk | rms=518 | updated_at=1787307758.1065204 | frequency_hz=296.4
- [2026-08-21 18:22:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307761.6060379 | source=vosk | rms=518 | updated_at=1787307758.1065204 | frequency_hz=296.4
- [2026-08-21 18:22:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307762.1055012 | source=vosk | rms=518 | updated_at=1787307758.1065204 | frequency_hz=296.4
- [2026-08-21 18:22:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307764.3570445 | source=vosk | rms=518 | updated_at=1787307758.1065204 | frequency_hz=296.4
- [2026-08-21 18:22:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307764.855913 | source=vosk | rms=518 | updated_at=1787307758.1065204 | frequency_hz=296.4
- [2026-08-21 18:22:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307766.1059222 | source=vosk | rms=518 | updated_at=1787307758.1065204 | frequency_hz=296.4
- [2026-08-21 18:22:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307766.6057184 | source=vosk | rms=518 | updated_at=1787307758.1065204 | frequency_hz=296.4
- [2026-08-21 18:22:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307767.1061392 | source=vosk | rms=1201 | updated_at=1787307767.1061392 | frequency_hz=296.4
- [2026-08-21 18:22:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307767.8560302 | source=vosk | rms=1202 | updated_at=1787307767.3635683 | frequency_hz=296.4
- [2026-08-21 18:22:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307768.856206 | source=vosk | rms=1202 | updated_at=1787307767.3635683 | frequency_hz=296.4
- [2026-08-21 18:22:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307769.356201 | source=vosk | rms=1202 | updated_at=1787307767.3635683 | frequency_hz=296.4
- [2026-08-21 18:22:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307769.6057646 | source=vosk | rms=1202 | updated_at=1787307767.3635683 | frequency_hz=296.4
- [2026-08-21 18:22:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307770.860599 | source=vosk | rms=1200 | updated_at=1787307770.1062727 | frequency_hz=296.4
- [2026-08-21 18:22:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307771.6063879 | source=vosk | rms=457 | updated_at=1787307771.6063879 | frequency_hz=296.4
- [2026-08-21 18:22:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307772.1076927 | source=vosk | rms=457 | updated_at=1787307771.6063879 | frequency_hz=296.4
- [2026-08-21 18:22:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307773.1062613 | source=vosk | rms=457 | updated_at=1787307771.6063879 | frequency_hz=296.4
- [2026-08-21 18:22:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307774.1057162 | source=vosk | rms=686 | updated_at=1787307773.6074953 | frequency_hz=296.4
- [2026-08-21 18:22:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307774.856009 | source=vosk | rms=540 | updated_at=1787307774.856009 | frequency_hz=296.4
- [2026-08-21 18:22:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307775.356261 | source=vosk | rms=540 | updated_at=1787307774.856009 | frequency_hz=296.4
- [2026-08-21 18:22:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307775.6064584 | source=vosk | rms=540 | updated_at=1787307774.856009 | frequency_hz=296.4
- [2026-08-21 18:22:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307778.8558567 | source=vosk | rms=1202 | updated_at=1787307778.3560052 | frequency_hz=296.4
- [2026-08-21 18:22:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307779.8564653 | source=vosk | rms=1202 | updated_at=1787307778.3560052 | frequency_hz=296.4
- [2026-08-21 18:23:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307781.357015 | source=vosk | rms=455 | updated_at=1787307780.85574 | frequency_hz=296.4
- [2026-08-21 18:23:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307781.8599136 | source=vosk | rms=398 | updated_at=1787307781.8599136 | frequency_hz=296.4
- [2026-08-21 18:23:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307782.4916954 | source=vosk | rms=398 | updated_at=1787307781.8599136 | frequency_hz=296.4
- [2026-08-21 18:23:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307785.1066718 | source=vosk | rms=326 | updated_at=1787307785.1066718 | frequency_hz=296.4
- [2026-08-21 18:23:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307785.607328 | source=vosk | rms=326 | updated_at=1787307785.1066718 | frequency_hz=296.4
- [2026-08-21 18:23:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307785.857506 | source=vosk | rms=326 | updated_at=1787307785.1066718 | frequency_hz=296.4
- [2026-08-21 18:23:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307786.3565774 | source=vosk | rms=326 | updated_at=1787307785.1066718 | frequency_hz=296.4
- [2026-08-21 18:23:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307786.606233 | source=vosk | rms=401 | updated_at=1787307786.606233 | frequency_hz=296.4
- [2026-08-21 18:23:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307787.1060877 | source=vosk | rms=401 | updated_at=1787307786.606233 | frequency_hz=296.4
- [2026-08-21 18:23:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307788.3567734 | source=vosk | rms=322 | updated_at=1787307788.3557725 | frequency_hz=296.4
- [2026-08-21 18:23:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307788.8561897 | source=vosk | rms=322 | updated_at=1787307788.3557725 | frequency_hz=296.4
- [2026-08-21 18:23:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307789.1057627 | source=vosk | rms=1201 | updated_at=1787307789.1057627 | frequency_hz=296.4
- [2026-08-21 18:23:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307790.1059945 | source=vosk | rms=1200 | updated_at=1787307789.605695 | frequency_hz=296.4
- [2026-08-21 18:23:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307790.356248 | source=vosk | rms=1200 | updated_at=1787307789.605695 | frequency_hz=296.4
- [2026-08-21 18:23:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307791.6074665 | source=vosk | rms=1201 | updated_at=1787307791.1062033 | frequency_hz=296.4
- [2026-08-21 18:23:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307792.615771 | source=vosk | rms=1201 | updated_at=1787307791.1062033 | frequency_hz=296.4
- [2026-08-21 18:23:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307793.1061 | source=vosk | rms=1201 | updated_at=1787307791.1062033 | frequency_hz=296.4
- [2026-08-21 18:23:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307793.8559415 | source=vosk | rms=1200 | updated_at=1787307793.8559415 | frequency_hz=296.4
- [2026-08-21 18:23:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307794.89955 | source=vosk | rms=1202 | updated_at=1787307794.3574147 | frequency_hz=296.4
- [2026-08-21 18:23:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307795.1061265 | source=vosk | rms=1202 | updated_at=1787307794.3574147 | frequency_hz=296.4
- [2026-08-21 18:23:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307795.606492 | source=vosk | rms=1202 | updated_at=1787307794.3574147 | frequency_hz=296.4
- [2026-08-21 18:23:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307798.3557522 | source=vosk | rms=1202 | updated_at=1787307794.3574147 | frequency_hz=296.4
- [2026-08-21 18:23:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307799.1065245 | source=vosk | rms=1202 | updated_at=1787307794.3574147 | frequency_hz=296.4
- [2026-08-21 18:23:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307800.8565543 | source=vosk | rms=1202 | updated_at=1787307794.3574147 | frequency_hz=296.4
- [2026-08-21 18:23:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307801.856337 | source=vosk | rms=318 | updated_at=1787307801.3564076 | frequency_hz=296.4
- [2026-08-21 18:23:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307802.356213 | source=vosk | rms=318 | updated_at=1787307801.3564076 | frequency_hz=296.4
- [2026-08-21 18:23:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307803.3566067 | source=vosk | rms=591 | updated_at=1787307802.8556905 | frequency_hz=296.4
- [2026-08-21 18:23:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307804.1085477 | source=vosk | rms=591 | updated_at=1787307802.8556905 | frequency_hz=296.4
- [2026-08-21 18:23:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307804.856138 | source=vosk | rms=447 | updated_at=1787307804.3565907 | frequency_hz=296.4
- [2026-08-21 18:23:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307806.105708 | source=vosk | rms=411 | updated_at=1787307806.105708 | frequency_hz=296.4
- [2026-08-21 18:23:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307809.6074317 | source=vosk | rms=356 | updated_at=1787307808.6067443 | frequency_hz=296.4
- [2026-08-21 18:23:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307810.6066532 | source=vosk | rms=273 | updated_at=1787307810.6066532 | frequency_hz=296.4
- [2026-08-21 18:23:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307814.1151094 | source=vosk | rms=477 | updated_at=1787307813.6058216 | frequency_hz=296.4
- [2026-08-21 18:23:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307815.1070125 | source=vosk | rms=477 | updated_at=1787307813.6058216 | frequency_hz=296.4
- [2026-08-21 18:23:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307816.0228202 | source=vosk | rms=477 | updated_at=1787307813.6058216 | frequency_hz=296.4
- [2026-08-21 18:23:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307816.1098576 | source=vosk | rms=284 | updated_at=1787307816.1098576 | frequency_hz=296.4
- [2026-08-21 18:23:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307817.106416 | source=vosk | rms=492 | updated_at=1787307816.6356554 | frequency_hz=296.4
- [2026-08-21 18:23:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307817.6064801 | source=vosk | rms=999 | updated_at=1787307817.6064801 | frequency_hz=296.4
- [2026-08-21 18:23:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307818.5479674 | source=vosk | rms=999 | updated_at=1787307817.6064801 | frequency_hz=296.4
- [2026-08-21 18:23:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307819.8617153 | source=vosk | rms=563 | updated_at=1787307819.8617153 | frequency_hz=296.4
- [2026-08-21 18:23:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307821.6106358 | source=vosk | rms=625 | updated_at=1787307821.110102 | frequency_hz=296.4
- [2026-08-21 18:23:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307822.129079 | source=vosk | rms=293 | updated_at=1787307822.129079 | frequency_hz=296.4
- [2026-08-21 18:23:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307823.8598547 | source=vosk | rms=293 | updated_at=1787307823.3600323 | frequency_hz=296.4
- [2026-08-21 18:23:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307824.3600461 | source=vosk | rms=1200 | updated_at=1787307824.3600461 | frequency_hz=296.4
- [2026-08-21 18:23:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307825.8616748 | source=vosk | rms=440 | updated_at=1787307825.3604748 | frequency_hz=296.4
- [2026-08-21 18:23:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307826.8603318 | source=vosk | rms=440 | updated_at=1787307825.3604748 | frequency_hz=296.4
- [2026-08-21 18:23:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307827.8599946 | source=vosk | rms=440 | updated_at=1787307825.3604748 | frequency_hz=296.4
- [2026-08-21 18:23:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307830.1114569 | source=vosk | rms=1200 | updated_at=1787307830.110451 | frequency_hz=296.4
- [2026-08-21 18:23:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307831.1104057 | source=vosk | rms=1200 | updated_at=1787307830.6101065 | frequency_hz=296.4
- [2026-08-21 18:23:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307831.8622208 | source=vosk | rms=486 | updated_at=1787307831.8622208 | frequency_hz=296.4
- [2026-08-21 18:23:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307832.8599105 | source=vosk | rms=1200 | updated_at=1787307832.3602102 | frequency_hz=296.4
- [2026-08-21 18:23:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307834.1103199 | source=vosk | rms=1200 | updated_at=1787307832.3602102 | frequency_hz=296.4
- [2026-08-21 18:23:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307834.6106656 | source=vosk | rms=1200 | updated_at=1787307832.3602102 | frequency_hz=296.4
- [2026-08-21 18:23:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307835.111896 | source=vosk | rms=1200 | updated_at=1787307832.3602102 | frequency_hz=296.4
- [2026-08-21 18:23:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307836.3601294 | source=vosk | rms=404 | updated_at=1787307835.6117022 | frequency_hz=296.4
- [2026-08-21 18:23:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307838.3614733 | source=vosk | rms=333 | updated_at=1787307838.3614733 | frequency_hz=296.4
- [2026-08-21 18:23:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307838.8603737 | source=vosk | rms=333 | updated_at=1787307838.3614733 | frequency_hz=296.4
- [2026-08-21 18:23:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307839.3621964 | source=vosk | rms=1149 | updated_at=1787307839.3621964 | frequency_hz=296.4
- [2026-08-21 18:24:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307840.3603153 | source=vosk | rms=906 | updated_at=1787307839.8857238 | frequency_hz=296.4
- [2026-08-21 18:24:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307840.861493 | source=vosk | rms=1201 | updated_at=1787307840.861493 | frequency_hz=296.4
- [2026-08-21 18:24:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307841.6108544 | source=vosk | rms=1201 | updated_at=1787307841.1104286 | frequency_hz=296.4
- [2026-08-21 18:24:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307843.3604646 | source=vosk | rms=1201 | updated_at=1787307843.3604646 | frequency_hz=296.4
- [2026-08-21 18:24:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307844.1101153 | source=vosk | rms=1200 | updated_at=1787307843.6100104 | frequency_hz=296.4
- [2026-08-21 18:24:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307848.360671 | source=vosk | rms=1200 | updated_at=1787307848.360671 | frequency_hz=296.4
- [2026-08-21 18:24:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307850.1107893 | source=vosk | rms=1201 | updated_at=1787307849.1101174 | frequency_hz=296.4
- [2026-08-21 18:24:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307851.8605092 | source=vosk | rms=1200 | updated_at=1787307851.8605092 | frequency_hz=296.4
- [2026-08-21 18:24:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307852.6108289 | source=vosk | rms=1200 | updated_at=1787307852.1100554 | frequency_hz=296.4
- [2026-08-21 18:24:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307853.860901 | source=vosk | rms=1201 | updated_at=1787307853.860901 | frequency_hz=296.4
- [2026-08-21 18:24:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307854.610444 | source=vosk | rms=1201 | updated_at=1787307854.1116202 | frequency_hz=296.4
- [2026-08-21 18:24:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307858.8620842 | source=vosk | rms=1202 | updated_at=1787307858.8620842 | frequency_hz=296.4
- [2026-08-21 18:24:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307859.6103952 | source=vosk | rms=1200 | updated_at=1787307859.11009 | frequency_hz=296.4
- [2026-08-21 18:24:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307863.8610568 | source=vosk | rms=1200 | updated_at=1787307863.8610568 | frequency_hz=296.4
- [2026-08-21 18:24:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307864.6108863 | source=vosk | rms=1200 | updated_at=1787307864.1108553 | frequency_hz=296.4
- [2026-08-21 18:24:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307869.1160336 | source=vosk | rms=1201 | updated_at=1787307869.1160336 | frequency_hz=296.4
- [2026-08-21 18:24:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307869.8606899 | source=vosk | rms=1202 | updated_at=1787307869.3601809 | frequency_hz=296.4
- [2026-08-21 18:24:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307870.6102986 | source=vosk | rms=1201 | updated_at=1787307870.6102986 | frequency_hz=280.2
- [2026-08-21 18:24:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307871.6107097 | source=vosk | rms=1201 | updated_at=1787307871.1106098 | frequency_hz=280.2
- [2026-08-21 18:24:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307873.3685012 | source=vosk | rms=1201 | updated_at=1787307871.1106098 | frequency_hz=280.2
- [2026-08-21 18:24:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307874.3608162 | source=vosk | rms=367 | updated_at=1787307873.6107419 | frequency_hz=280.2
- [2026-08-21 18:24:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307875.1142507 | source=vosk | rms=1202 | updated_at=1787307875.1142507 | frequency_hz=280.2
- [2026-08-21 18:24:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307877.6669683 | source=vosk | rms=1171 | updated_at=1787307877.110577 | frequency_hz=280.2
- [2026-08-21 18:24:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307878.860502 | source=vosk | rms=1200 | updated_at=1787307878.860502 | frequency_hz=280.2
- [2026-08-21 18:24:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307879.8618088 | source=vosk | rms=680 | updated_at=1787307879.3607113 | frequency_hz=280.2
- [2026-08-21 18:24:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307880.1105475 | source=vosk | rms=316 | updated_at=1787307880.1105475 | frequency_hz=280.2
- [2026-08-21 18:24:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307881.3671334 | source=vosk | rms=786 | updated_at=1787307880.8754988 | frequency_hz=280.2
- [2026-08-21 18:24:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307883.8603697 | source=vosk | rms=786 | updated_at=1787307880.8754988 | frequency_hz=280.2
- [2026-08-21 18:24:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307884.3610713 | source=vosk | rms=786 | updated_at=1787307880.8754988 | frequency_hz=280.2
- [2026-08-21 18:24:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307886.3611166 | source=vosk | rms=295 | updated_at=1787307886.3611166 | frequency_hz=280.2
- [2026-08-21 18:24:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307891.862769 | source=vosk | rms=1205 | updated_at=1787307891.3603747 | frequency_hz=280.2
- [2026-08-21 18:24:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307892.1153138 | source=vosk | rms=1205 | updated_at=1787307891.3603747 | frequency_hz=280.2
- [2026-08-21 18:24:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307892.610416 | source=vosk | rms=1205 | updated_at=1787307891.3603747 | frequency_hz=280.2
- [2026-08-21 18:24:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307892.8604612 | source=vosk | rms=1205 | updated_at=1787307891.3603747 | frequency_hz=280.2
- [2026-08-21 18:24:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307893.6115482 | source=vosk | rms=1205 | updated_at=1787307891.3603747 | frequency_hz=280.2
- [2026-08-21 18:24:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307893.869541 | source=vosk | rms=653 | updated_at=1787307893.869541 | frequency_hz=280.2
- [2026-08-21 18:24:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307896.8603375 | source=vosk | rms=1204 | updated_at=1787307896.361074 | frequency_hz=280.2
- [2026-08-21 18:24:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307897.8627803 | source=vosk | rms=599 | updated_at=1787307897.8627803 | frequency_hz=280.2
- [2026-08-21 18:24:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307898.3627715 | source=vosk | rms=599 | updated_at=1787307897.8627803 | frequency_hz=280.2
- [2026-08-21 18:24:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307898.6108956 | source=vosk | rms=1201 | updated_at=1787307898.6108956 | frequency_hz=280.2
- [2026-08-21 18:25:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307900.3606522 | source=vosk | rms=1202 | updated_at=1787307899.361932 | frequency_hz=280.2
- [2026-08-21 18:25:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307900.6111577 | source=vosk | rms=1202 | updated_at=1787307899.361932 | frequency_hz=280.2
- [2026-08-21 18:25:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307901.1109416 | source=vosk | rms=1202 | updated_at=1787307899.361932 | frequency_hz=280.2
- [2026-08-21 18:25:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307902.6111574 | source=vosk | rms=435 | updated_at=1787307902.6111574 | frequency_hz=280.2
- [2026-08-21 18:25:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307903.1106973 | source=vosk | rms=435 | updated_at=1787307902.6111574 | frequency_hz=280.2
- [2026-08-21 18:25:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307904.110756 | source=vosk | rms=1200 | updated_at=1787307904.110756 | frequency_hz=280.2
- [2026-08-21 18:25:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307910.610581 | source=vosk | rms=546 | updated_at=1787307909.862307 | frequency_hz=280.2
- [2026-08-21 18:25:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307911.6107233 | source=vosk | rms=1202 | updated_at=1787307911.6107233 | frequency_hz=280.2
- [2026-08-21 18:25:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307912.1108303 | source=vosk | rms=1202 | updated_at=1787307911.6107233 | frequency_hz=280.2
- [2026-08-21 18:25:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307912.6113725 | source=vosk | rms=715 | updated_at=1787307912.6113725 | frequency_hz=280.2
- [2026-08-21 18:25:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307914.6143084 | source=vosk | rms=1038 | updated_at=1787307914.110593 | frequency_hz=280.2
- [2026-08-21 18:25:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307915.8629696 | source=vosk | rms=1038 | updated_at=1787307914.110593 | frequency_hz=280.2
- [2026-08-21 18:25:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307917.8646495 | source=vosk | rms=1203 | updated_at=1787307917.3616297 | frequency_hz=280.2
- [2026-08-21 18:25:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307918.1104524 | source=vosk | rms=439 | updated_at=1787307918.1104524 | frequency_hz=280.2
- [2026-08-21 18:25:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307918.6111193 | source=vosk | rms=439 | updated_at=1787307918.1104524 | frequency_hz=280.2
- [2026-08-21 18:25:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307919.1178763 | source=vosk | rms=439 | updated_at=1787307918.1104524 | frequency_hz=280.2
- [2026-08-21 18:25:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307920.111253 | source=vosk | rms=1202 | updated_at=1787307919.6120832 | frequency_hz=280.2
- [2026-08-21 18:25:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307920.3623972 | source=vosk | rms=611 | updated_at=1787307920.3623972 | frequency_hz=280.2
- [2026-08-21 18:25:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307921.862566 | source=vosk | rms=674 | updated_at=1787307921.3612719 | frequency_hz=280.2
- [2026-08-21 18:25:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307922.6134794 | source=vosk | rms=755 | updated_at=1787307922.6134794 | frequency_hz=280.2
- [2026-08-21 18:25:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307923.224907 | source=vosk | rms=755 | updated_at=1787307922.6134794 | frequency_hz=280.2
- [2026-08-21 18:25:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307923.768874 | source=vosk | rms=888 | updated_at=1787307923.768874 | frequency_hz=280.2
- [2026-08-21 18:25:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307924.3610775 | source=vosk | rms=888 | updated_at=1787307923.768874 | frequency_hz=280.2
- [2026-08-21 18:25:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307924.6106143 | source=vosk | rms=813 | updated_at=1787307924.6106143 | frequency_hz=280.2
- [2026-08-21 18:25:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307925.1116018 | source=vosk | rms=813 | updated_at=1787307924.6106143 | frequency_hz=280.2
- [2026-08-21 18:25:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307925.380923 | source=vosk | rms=1200 | updated_at=1787307925.380923 | frequency_hz=280.2
- [2026-08-21 18:25:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307926.6114929 | source=vosk | rms=1200 | updated_at=1787307925.6112967 | frequency_hz=280.2
- [2026-08-21 18:25:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307926.8611262 | source=vosk | rms=1203 | updated_at=1787307926.8611262 | frequency_hz=280.2
- [2026-08-21 18:25:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307927.3610566 | source=vosk | rms=1203 | updated_at=1787307926.8611262 | frequency_hz=280.2
- [2026-08-21 18:25:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307928.1114886 | source=vosk | rms=1203 | updated_at=1787307926.8611262 | frequency_hz=280.2
- [2026-08-21 18:25:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307929.6106308 | source=vosk | rms=909 | updated_at=1787307929.1114135 | frequency_hz=280.2
- [2026-08-21 18:25:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307929.8620493 | source=vosk | rms=808 | updated_at=1787307929.8620493 | frequency_hz=280.2
- [2026-08-21 18:25:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307933.8310118 | source=vosk | rms=462 | updated_at=1787307932.61567 | frequency_hz=280.2
- [2026-08-21 18:25:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307934.331189 | source=vosk | rms=462 | updated_at=1787307932.61567 | frequency_hz=280.2
- [2026-08-21 18:25:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307934.830425 | source=vosk | rms=462 | updated_at=1787307932.61567 | frequency_hz=280.2
- [2026-08-21 18:25:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307935.5814142 | source=vosk | rms=462 | updated_at=1787307932.61567 | frequency_hz=280.2
- [2026-08-21 18:25:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307938.581283 | source=vosk | rms=524 | updated_at=1787307938.0814595 | frequency_hz=280.2
- [2026-08-21 18:25:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307938.8348691 | source=vosk | rms=623 | updated_at=1787307938.8348691 | frequency_hz=280.2
- [2026-08-21 18:25:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307940.2304623 | source=vosk | rms=1201 | updated_at=1787307939.7091637 | frequency_hz=280.2
- [2026-08-21 18:25:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307940.4516537 | source=vosk | rms=784 | updated_at=1787307940.4516537 | frequency_hz=280.2
- [2026-08-21 18:25:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307940.9506693 | source=vosk | rms=784 | updated_at=1787307940.4516537 | frequency_hz=280.2
- [2026-08-21 18:25:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307941.4510033 | source=vosk | rms=784 | updated_at=1787307940.4516537 | frequency_hz=280.2
- [2026-08-21 18:25:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307942.450985 | source=vosk | rms=784 | updated_at=1787307940.4516537 | frequency_hz=280.2
- [2026-08-21 18:25:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307942.9510746 | source=vosk | rms=807 | updated_at=1787307942.9510746 | frequency_hz=280.2
- [2026-08-21 18:25:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307943.451249 | source=vosk | rms=807 | updated_at=1787307942.9510746 | frequency_hz=280.2
- [2026-08-21 18:25:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307943.9509118 | source=vosk | rms=1200 | updated_at=1787307943.9509118 | frequency_hz=280.2
- [2026-08-21 18:25:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307944.9558506 | source=vosk | rms=1202 | updated_at=1787307944.452367 | frequency_hz=280.2
- [2026-08-21 18:25:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307948.2013905 | source=vosk | rms=1202 | updated_at=1787307948.2013905 | frequency_hz=280.2
- [2026-08-21 18:25:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307949.45094 | source=vosk | rms=1202 | updated_at=1787307948.7009614 | frequency_hz=280.2
- [2026-08-21 18:25:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307949.7027843 | source=vosk | rms=1200 | updated_at=1787307949.7027843 | frequency_hz=280.2
- [2026-08-21 18:25:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307950.4513059 | source=vosk | rms=1200 | updated_at=1787307949.9515307 | frequency_hz=280.2
- [2026-08-21 18:25:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307950.72086 | source=vosk | rms=1200 | updated_at=1787307949.9515307 | frequency_hz=280.2
- [2026-08-21 18:25:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307953.2010033 | source=vosk | rms=646 | updated_at=1787307952.450818 | frequency_hz=280.2
- [2026-08-21 18:25:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307953.4515972 | source=vosk | rms=641 | updated_at=1787307953.4515972 | frequency_hz=280.2
- [2026-08-21 18:25:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307954.2008843 | source=vosk | rms=1203 | updated_at=1787307953.701143 | frequency_hz=280.2
- [2026-08-21 18:25:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307954.4515085 | source=vosk | rms=1204 | updated_at=1787307954.4515085 | frequency_hz=280.2
- [2026-08-21 18:25:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307954.9514701 | source=vosk | rms=1204 | updated_at=1787307954.4515085 | frequency_hz=280.2
- [2026-08-21 18:25:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307955.45251 | source=vosk | rms=1204 | updated_at=1787307954.4515085 | frequency_hz=280.2
- [2026-08-21 18:25:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307958.2010033 | source=vosk | rms=1200 | updated_at=1787307957.2010407 | frequency_hz=280.2
- [2026-08-21 18:25:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307958.9509265 | source=vosk | rms=918 | updated_at=1787307958.9509265 | frequency_hz=280.2
- [2026-08-21 18:26:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307961.2013292 | source=vosk | rms=1200 | updated_at=1787307960.7008452 | frequency_hz=280.2
- [2026-08-21 18:26:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307961.702453 | source=vosk | rms=1200 | updated_at=1787307960.7008452 | frequency_hz=280.2
- [2026-08-21 18:26:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307962.2015405 | source=vosk | rms=1200 | updated_at=1787307960.7008452 | frequency_hz=280.2
- [2026-08-21 18:26:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307962.707485 | source=vosk | rms=1201 | updated_at=1787307962.707485 | frequency_hz=280.2
- [2026-08-21 18:26:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307963.4509501 | source=vosk | rms=1200 | updated_at=1787307962.95329 | frequency_hz=280.2
- [2026-08-21 18:26:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307963.9509773 | source=vosk | rms=1057 | updated_at=1787307963.9509773 | frequency_hz=280.2
- [2026-08-21 18:26:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307964.9509792 | source=vosk | rms=1169 | updated_at=1787307964.4515731 | frequency_hz=280.2
- [2026-08-21 18:26:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307965.4507682 | source=vosk | rms=1143 | updated_at=1787307965.4507682 | frequency_hz=280.2
- [2026-08-21 18:26:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307965.951417 | source=vosk | rms=1143 | updated_at=1787307965.4507682 | frequency_hz=280.2
- [2026-08-21 18:26:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307966.9825656 | source=vosk | rms=1143 | updated_at=1787307965.4507682 | frequency_hz=280.2
- [2026-08-21 18:26:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307968.9516828 | source=vosk | rms=1202 | updated_at=1787307968.4515617 | frequency_hz=280.2
- [2026-08-21 18:26:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307971.2009385 | source=vosk | rms=1201 | updated_at=1787307971.2009385 | frequency_hz=280.2
- [2026-08-21 18:26:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307973.9661822 | source=vosk | rms=1204 | updated_at=1787307973.2014515 | frequency_hz=280.2
- [2026-08-21 18:26:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307974.2013502 | source=vosk | rms=1204 | updated_at=1787307973.2014515 | frequency_hz=280.2
- [2026-08-21 18:26:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307974.7008042 | source=vosk | rms=1204 | updated_at=1787307973.2014515 | frequency_hz=280.2
- [2026-08-21 18:26:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307976.4516876 | source=vosk | rms=1204 | updated_at=1787307973.2014515 | frequency_hz=280.2
- [2026-08-21 18:26:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307978.201224 | source=vosk | rms=1204 | updated_at=1787307973.2014515 | frequency_hz=280.2
- [2026-08-21 18:26:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307978.723673 | source=vosk | rms=1203 | updated_at=1787307978.723673 | frequency_hz=280.2
- [2026-08-21 18:26:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307979.2016287 | source=vosk | rms=1203 | updated_at=1787307978.723673 | frequency_hz=280.2
- [2026-08-21 18:26:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307979.9512017 | source=vosk | rms=1200 | updated_at=1787307979.9512017 | frequency_hz=280.2
- [2026-08-21 18:26:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307981.201487 | source=vosk | rms=799 | updated_at=1787307980.7174032 | frequency_hz=280.2
- [2026-08-21 18:26:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307982.4515848 | source=vosk | rms=1200 | updated_at=1787307982.4515848 | frequency_hz=280.2
- [2026-08-21 18:26:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307983.2019897 | source=vosk | rms=1200 | updated_at=1787307982.7027223 | frequency_hz=280.2
- [2026-08-21 18:26:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307985.769158 | source=vosk | rms=1200 | updated_at=1787307982.7027223 | frequency_hz=280.2
- [2026-08-21 18:26:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307987.5198116 | source=vosk | rms=1200 | updated_at=1787307987.0192306 | frequency_hz=280.2
- [2026-08-21 18:26:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307988.5192945 | source=vosk | rms=1202 | updated_at=1787307988.5192945 | frequency_hz=280.2
- [2026-08-21 18:26:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307989.0191617 | source=vosk | rms=1202 | updated_at=1787307988.5192945 | frequency_hz=280.2
- [2026-08-21 18:26:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307989.2706814 | source=vosk | rms=1202 | updated_at=1787307988.5192945 | frequency_hz=280.2
- [2026-08-21 18:26:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307990.8193867 | source=vosk | rms=886 | updated_at=1787307990.3077424 | frequency_hz=280.2
- [2026-08-21 18:26:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307991.5507128 | source=vosk | rms=498 | updated_at=1787307991.5507128 | frequency_hz=280.2
- [2026-08-21 18:26:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307992.0514843 | source=vosk | rms=498 | updated_at=1787307991.5507128 | frequency_hz=280.2
- [2026-08-21 18:26:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307993.0605376 | source=vosk | rms=1202 | updated_at=1787307993.0605376 | frequency_hz=280.2
- [2026-08-21 18:26:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307993.8028243 | source=vosk | rms=1201 | updated_at=1787307993.299203 | frequency_hz=280.2
- [2026-08-21 18:26:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307996.3229234 | source=vosk | rms=571 | updated_at=1787307996.3229234 | frequency_hz=280.2
- [2026-08-21 18:26:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307997.799217 | source=vosk | rms=688 | updated_at=1787307996.799805 | frequency_hz=280.2
- [2026-08-21 18:26:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307998.0496566 | source=vosk | rms=688 | updated_at=1787307996.799805 | frequency_hz=280.2
- [2026-08-21 18:26:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787307998.5496173 | source=vosk | rms=688 | updated_at=1787307996.799805 | frequency_hz=280.2
- [2026-08-21 18:26:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787307999.049819 | source=vosk | rms=378 | updated_at=1787307999.049819 | frequency_hz=280.2
- [2026-08-21 18:26:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308004.2308109 | source=vosk | rms=324 | updated_at=1787308003.7300625 | frequency_hz=280.2
- [2026-08-21 18:26:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308004.9791057 | source=vosk | rms=1200 | updated_at=1787308004.9791057 | frequency_hz=280.2
- [2026-08-21 18:26:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308005.7318628 | source=vosk | rms=1202 | updated_at=1787308005.231687 | frequency_hz=280.2
- [2026-08-21 18:26:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308005.9800005 | source=vosk | rms=1202 | updated_at=1787308005.231687 | frequency_hz=280.2
- [2026-08-21 18:26:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308007.481938 | source=vosk | rms=351 | updated_at=1787308006.229685 | frequency_hz=280.2
- [2026-08-21 18:26:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308008.4795644 | source=vosk | rms=351 | updated_at=1787308006.229685 | frequency_hz=280.2
- [2026-08-21 18:26:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308008.9799185 | source=vosk | rms=351 | updated_at=1787308006.229685 | frequency_hz=280.2
- [2026-08-21 18:26:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308010.7391603 | source=vosk | rms=446 | updated_at=1787308010.7391603 | frequency_hz=280.2
- [2026-08-21 18:26:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308011.2395728 | source=vosk | rms=446 | updated_at=1787308010.7391603 | frequency_hz=280.2
- [2026-08-21 18:26:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308011.73931 | source=vosk | rms=812 | updated_at=1787308011.73931 | frequency_hz=280.2
- [2026-08-21 18:26:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308012.2398746 | source=vosk | rms=812 | updated_at=1787308011.73931 | frequency_hz=280.2
- [2026-08-21 18:26:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308012.489147 | source=vosk | rms=1203 | updated_at=1787308012.489147 | frequency_hz=280.2
- [2026-08-21 18:26:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308012.989986 | source=vosk | rms=1203 | updated_at=1787308012.489147 | frequency_hz=280.2
- [2026-08-21 18:26:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308013.739618 | source=vosk | rms=1202 | updated_at=1787308013.739618 | frequency_hz=280.2
- [2026-08-21 18:26:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308014.7407098 | source=vosk | rms=1201 | updated_at=1787308014.2447958 | frequency_hz=280.2
- [2026-08-21 18:26:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308014.989229 | source=vosk | rms=1201 | updated_at=1787308014.2447958 | frequency_hz=280.2
- [2026-08-21 18:26:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308015.9973202 | source=vosk | rms=1020 | updated_at=1787308015.489011 | frequency_hz=280.2
- [2026-08-21 18:26:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308016.9910688 | source=vosk | rms=903 | updated_at=1787308016.9910688 | frequency_hz=280.2
- [2026-08-21 18:26:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308017.4899945 | source=vosk | rms=903 | updated_at=1787308016.9910688 | frequency_hz=280.2
- [2026-08-21 18:26:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308017.989755 | source=vosk | rms=1202 | updated_at=1787308017.989755 | frequency_hz=280.2
- [2026-08-21 18:26:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308018.9898262 | source=vosk | rms=745 | updated_at=1787308018.4914007 | frequency_hz=280.2
- [2026-08-21 18:26:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308019.991015 | source=vosk | rms=1201 | updated_at=1787308019.991015 | frequency_hz=280.2
- [2026-08-21 18:27:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308021.239339 | source=vosk | rms=1204 | updated_at=1787308020.739621 | frequency_hz=280.2
- [2026-08-21 18:27:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308023.7397585 | source=vosk | rms=1204 | updated_at=1787308020.739621 | frequency_hz=280.2
- [2026-08-21 18:27:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308024.2400074 | source=vosk | rms=1204 | updated_at=1787308020.739621 | frequency_hz=280.2
- [2026-08-21 18:27:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308024.7542949 | source=vosk | rms=962 | updated_at=1787308024.7542949 | frequency_hz=280.2
- [2026-08-21 18:27:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308026.7398014 | source=vosk | rms=1201 | updated_at=1787308026.2394803 | frequency_hz=280.2
- [2026-08-21 18:27:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308027.9891849 | source=vosk | rms=1201 | updated_at=1787308027.9891849 | frequency_hz=280.2
- [2026-08-21 18:27:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308028.990778 | source=vosk | rms=1200 | updated_at=1787308028.4895632 | frequency_hz=280.2
- [2026-08-21 18:27:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308029.489784 | source=vosk | rms=383 | updated_at=1787308029.489784 | frequency_hz=280.2
- [2026-08-21 18:27:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308030.239851 | source=vosk | rms=1129 | updated_at=1787308029.740766 | frequency_hz=280.2
- [2026-08-21 18:27:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308030.4900882 | source=vosk | rms=904 | updated_at=1787308030.4900882 | frequency_hz=280.2
- [2026-08-21 18:27:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308030.995346 | source=vosk | rms=904 | updated_at=1787308030.4900882 | frequency_hz=280.2
- [2026-08-21 18:27:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308031.489577 | source=vosk | rms=827 | updated_at=1787308031.489577 | frequency_hz=280.2
- [2026-08-21 18:27:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308031.990824 | source=vosk | rms=827 | updated_at=1787308031.489577 | frequency_hz=280.2
- [2026-08-21 18:27:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308032.9894407 | source=vosk | rms=827 | updated_at=1787308031.489577 | frequency_hz=280.2
- [2026-08-21 18:27:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308033.489583 | source=vosk | rms=827 | updated_at=1787308031.489577 | frequency_hz=280.2
- [2026-08-21 18:27:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308033.9892998 | source=vosk | rms=827 | updated_at=1787308031.489577 | frequency_hz=280.2
- [2026-08-21 18:27:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308034.4897985 | source=vosk | rms=827 | updated_at=1787308031.489577 | frequency_hz=280.2
- [2026-08-21 18:27:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308035.4895816 | source=vosk | rms=440 | updated_at=1787308035.4895816 | frequency_hz=280.2
- [2026-08-21 18:27:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308037.491166 | source=vosk | rms=1206 | updated_at=1787308037.007834 | frequency_hz=280.2
- [2026-08-21 18:27:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308038.2398012 | source=vosk | rms=615 | updated_at=1787308038.2398012 | frequency_hz=280.2
- [2026-08-21 18:27:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308039.7393827 | source=vosk | rms=744 | updated_at=1787308039.239862 | frequency_hz=280.2
- [2026-08-21 18:27:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308040.9611332 | source=vosk | rms=619 | updated_at=1787308040.9611332 | frequency_hz=280.2
- [2026-08-21 18:27:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308042.2100923 | source=vosk | rms=1201 | updated_at=1787308041.7121902 | frequency_hz=280.2
- [2026-08-21 18:27:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308042.7101412 | source=vosk | rms=1202 | updated_at=1787308042.7101412 | frequency_hz=280.2
- [2026-08-21 18:27:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308043.7093694 | source=vosk | rms=427 | updated_at=1787308043.2137601 | frequency_hz=280.2
- [2026-08-21 18:27:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308043.9596138 | source=vosk | rms=541 | updated_at=1787308043.9596138 | frequency_hz=280.2
- [2026-08-21 18:27:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308044.4596114 | source=vosk | rms=541 | updated_at=1787308043.9596138 | frequency_hz=280.2
- [2026-08-21 18:27:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308044.960235 | source=vosk | rms=393 | updated_at=1787308044.960235 | frequency_hz=280.2
- [2026-08-21 18:27:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308045.4708853 | source=vosk | rms=393 | updated_at=1787308044.960235 | frequency_hz=280.2
- [2026-08-21 18:27:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308045.9594932 | source=vosk | rms=1135 | updated_at=1787308045.9594932 | frequency_hz=280.2
- [2026-08-21 18:27:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308046.4608753 | source=vosk | rms=1135 | updated_at=1787308045.9594932 | frequency_hz=280.2
- [2026-08-21 18:27:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308046.9599442 | source=vosk | rms=1200 | updated_at=1787308046.9599442 | frequency_hz=280.2
- [2026-08-21 18:27:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308048.9598293 | source=vosk | rms=1201 | updated_at=1787308048.4603083 | frequency_hz=280.2
- [2026-08-21 18:27:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308049.7096303 | source=vosk | rms=1203 | updated_at=1787308049.7096303 | frequency_hz=280.2
- [2026-08-21 18:27:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308050.21003 | source=vosk | rms=1203 | updated_at=1787308049.7096303 | frequency_hz=280.2
- [2026-08-21 18:27:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308050.959935 | source=vosk | rms=1204 | updated_at=1787308050.959935 | frequency_hz=250.7
- [2026-08-21 18:27:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308052.459567 | source=vosk | rms=745 | updated_at=1787308051.9632518 | frequency_hz=250.7
- [2026-08-21 18:27:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308053.4602365 | source=vosk | rms=421 | updated_at=1787308053.4602365 | frequency_hz=250.7
- [2026-08-21 18:27:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308053.959691 | source=vosk | rms=421 | updated_at=1787308053.4602365 | frequency_hz=250.7
- [2026-08-21 18:27:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308055.9596746 | source=vosk | rms=1202 | updated_at=1787308055.9596746 | frequency_hz=250.7
- [2026-08-21 18:27:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308056.961022 | source=vosk | rms=1200 | updated_at=1787308056.2103176 | frequency_hz=250.7
- [2026-08-21 18:27:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308057.2178087 | source=vosk | rms=1202 | updated_at=1787308057.2178087 | frequency_hz=250.7
- [2026-08-21 18:27:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308058.9610164 | source=vosk | rms=1201 | updated_at=1787308058.4597077 | frequency_hz=250.7
- [2026-08-21 18:27:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308059.9601195 | source=vosk | rms=1201 | updated_at=1787308058.4597077 | frequency_hz=250.7
- [2026-08-21 18:27:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308060.7096124 | source=vosk | rms=632 | updated_at=1787308060.212306 | frequency_hz=250.7
- [2026-08-21 18:27:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308062.2104049 | source=vosk | rms=632 | updated_at=1787308060.212306 | frequency_hz=250.7
- [2026-08-21 18:27:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308062.7113917 | source=vosk | rms=632 | updated_at=1787308060.212306 | frequency_hz=250.7
- [2026-08-21 18:27:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308064.2095454 | source=vosk | rms=1200 | updated_at=1787308064.2095454 | frequency_hz=250.7
- [2026-08-21 18:27:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308064.9600065 | source=vosk | rms=1201 | updated_at=1787308064.459441 | frequency_hz=250.7
- [2026-08-21 18:27:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308065.4605656 | source=vosk | rms=1201 | updated_at=1787308065.4605656 | frequency_hz=250.7
- [2026-08-21 18:27:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308065.959702 | source=vosk | rms=1201 | updated_at=1787308065.4605656 | frequency_hz=250.7
- [2026-08-21 18:27:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308067.9603188 | source=vosk | rms=1201 | updated_at=1787308067.9603188 | frequency_hz=250.7
- [2026-08-21 18:27:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308068.9605322 | source=vosk | rms=1201 | updated_at=1787308068.2097726 | frequency_hz=250.7
- [2026-08-21 18:27:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308078.2101889 | source=vosk | rms=1200 | updated_at=1787308078.2101889 | frequency_hz=250.7
- [2026-08-21 18:27:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308079.2097886 | source=vosk | rms=780 | updated_at=1787308078.7109904 | frequency_hz=250.7
- [2026-08-21 18:28:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308089.0795755 | source=vosk | rms=1202 | updated_at=1787308089.0795755 | frequency_hz=312.0
- [2026-08-21 18:28:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308090.0815818 | source=vosk | rms=1200 | updated_at=1787308089.5821588 | frequency_hz=312.0
- [2026-08-21 18:28:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308091.829781 | source=vosk | rms=306 | updated_at=1787308091.829781 | frequency_hz=94.0
- [2026-08-21 18:28:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308092.8446774 | source=vosk | rms=1202 | updated_at=1787308092.3399394 | frequency_hz=94.0
- [2026-08-21 18:28:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308093.3403416 | source=vosk | rms=1202 | updated_at=1787308092.3399394 | frequency_hz=94.0
- [2026-08-21 18:28:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308093.841692 | source=vosk | rms=1202 | updated_at=1787308092.3399394 | frequency_hz=94.0
- [2026-08-21 18:28:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308094.8396778 | source=vosk | rms=173 | updated_at=1787308094.8396778 | frequency_hz=94.0
- [2026-08-21 18:28:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308098.1000338 | source=vosk | rms=206 | updated_at=1787308097.340121 | frequency_hz=94.0
- [2026-08-21 18:28:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308099.0906358 | source=vosk | rms=249 | updated_at=1787308099.0906358 | frequency_hz=94.0
- [2026-08-21 18:28:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308100.0901732 | source=vosk | rms=209 | updated_at=1787308099.3442042 | frequency_hz=94.0
- [2026-08-21 18:28:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308102.840447 | source=vosk | rms=1201 | updated_at=1787308102.840447 | frequency_hz=94.0
- [2026-08-21 18:28:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308103.8397827 | source=vosk | rms=1203 | updated_at=1787308103.3412914 | frequency_hz=94.0
- [2026-08-21 18:28:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308104.340776 | source=vosk | rms=1203 | updated_at=1787308103.3412914 | frequency_hz=94.0
- [2026-08-21 18:28:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308105.0916924 | source=vosk | rms=1203 | updated_at=1787308103.3412914 | frequency_hz=94.0
- [2026-08-21 18:28:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308105.5913467 | source=vosk | rms=1201 | updated_at=1787308105.5913467 | frequency_hz=94.0
- [2026-08-21 18:28:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308106.8401742 | source=vosk | rms=226 | updated_at=1787308106.3399074 | frequency_hz=94.0
- [2026-08-21 18:28:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308108.3397608 | source=vosk | rms=1202 | updated_at=1787308108.3397608 | frequency_hz=94.0
- [2026-08-21 18:28:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308109.340349 | source=vosk | rms=1206 | updated_at=1787308108.8400068 | frequency_hz=94.0
- [2026-08-21 18:28:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308112.3399808 | source=vosk | rms=1202 | updated_at=1787308112.3399808 | frequency_hz=94.0
- [2026-08-21 18:28:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308113.0905478 | source=vosk | rms=1201 | updated_at=1787308112.606559 | frequency_hz=94.0
- [2026-08-21 18:28:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308119.841458 | source=vosk | rms=1203 | updated_at=1787308119.841458 | frequency_hz=302.0
- [2026-08-21 18:28:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308120.8406675 | source=vosk | rms=1201 | updated_at=1787308120.339891 | frequency_hz=302.0
- [2026-08-21 18:28:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308122.0901937 | source=vosk | rms=1201 | updated_at=1787308122.0901937 | frequency_hz=284.0
- [2026-08-21 18:28:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308123.1097932 | source=vosk | rms=1200 | updated_at=1787308122.5907295 | frequency_hz=284.0
- [2026-08-21 18:28:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308124.5895884 | source=vosk | rms=1202 | updated_at=1787308124.5895884 | frequency_hz=284.0
- [2026-08-21 18:28:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308125.594565 | source=vosk | rms=1206 | updated_at=1787308125.09063 | frequency_hz=284.0
- [2026-08-21 18:28:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308126.3404946 | source=vosk | rms=523 | updated_at=1787308126.3404946 | frequency_hz=284.0
- [2026-08-21 18:28:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308128.8204646 | source=vosk | rms=277 | updated_at=1787308128.3207428 | frequency_hz=284.0
- [2026-08-21 18:28:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308129.3213835 | source=vosk | rms=316 | updated_at=1787308129.3213835 | frequency_hz=284.0
- [2026-08-21 18:28:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308130.5700192 | source=vosk | rms=1202 | updated_at=1787308130.0701203 | frequency_hz=284.0
- [2026-08-21 18:28:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308133.070048 | source=vosk | rms=310 | updated_at=1787308133.070048 | frequency_hz=284.0
- [2026-08-21 18:28:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308133.8203123 | source=vosk | rms=310 | updated_at=1787308133.070048 | frequency_hz=284.0
- [2026-08-21 18:28:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308134.3199086 | source=vosk | rms=335 | updated_at=1787308134.3199086 | frequency_hz=284.0
- [2026-08-21 18:28:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308138.0707395 | source=vosk | rms=359 | updated_at=1787308137.570652 | frequency_hz=284.0
- [2026-08-21 18:28:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308138.820389 | source=vosk | rms=359 | updated_at=1787308137.570652 | frequency_hz=284.0
- [2026-08-21 18:28:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308139.320514 | source=vosk | rms=359 | updated_at=1787308137.570652 | frequency_hz=284.0
- [2026-08-21 18:28:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308139.57 | source=vosk | rms=359 | updated_at=1787308137.570652 | frequency_hz=284.0
- [2026-08-21 18:29:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308141.070255 | source=vosk | rms=1202 | updated_at=1787308140.5884898 | frequency_hz=284.0
- [2026-08-21 18:29:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308144.0701084 | source=vosk | rms=1201 | updated_at=1787308144.0701084 | frequency_hz=284.0
- [2026-08-21 18:29:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308145.0717962 | source=vosk | rms=1200 | updated_at=1787308144.5705078 | frequency_hz=284.0
- [2026-08-21 18:29:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308145.825818 | source=vosk | rms=745 | updated_at=1787308145.825818 | frequency_hz=284.0
- [2026-08-21 18:29:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308149.9301302 | source=vosk | rms=405 | updated_at=1787308149.1805074 | frequency_hz=284.0
- [2026-08-21 18:29:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308150.9304624 | source=vosk | rms=283 | updated_at=1787308150.9304624 | frequency_hz=284.0
- [2026-08-21 18:29:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308151.6806788 | source=vosk | rms=283 | updated_at=1787308150.9304624 | frequency_hz=284.0
- [2026-08-21 18:29:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308156.3103738 | source=vosk | rms=1200 | updated_at=1787308156.3103738 | frequency_hz=284.0
- [2026-08-21 18:29:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308157.3110971 | source=vosk | rms=419 | updated_at=1787308156.8103955 | frequency_hz=284.0
- [2026-08-21 18:29:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308160.061559 | source=vosk | rms=1202 | updated_at=1787308160.061559 | frequency_hz=284.0
- [2026-08-21 18:29:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308161.0655682 | source=vosk | rms=382 | updated_at=1787308160.560059 | frequency_hz=284.0
- [2026-08-21 18:29:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308166.8117545 | source=vosk | rms=339 | updated_at=1787308166.8117545 | frequency_hz=284.0
- [2026-08-21 18:29:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308168.0614274 | source=vosk | rms=305 | updated_at=1787308167.0608819 | frequency_hz=284.0
- [2026-08-21 18:29:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308168.5616693 | source=vosk | rms=350 | updated_at=1787308168.5616693 | frequency_hz=284.0
- [2026-08-21 18:29:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308169.5608833 | source=vosk | rms=523 | updated_at=1787308169.0609334 | frequency_hz=284.0
- [2026-08-21 18:29:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308172.3106885 | source=vosk | rms=1202 | updated_at=1787308172.3106885 | frequency_hz=284.0
- [2026-08-21 18:29:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308173.0605 | source=vosk | rms=1201 | updated_at=1787308172.574905 | frequency_hz=284.0
- [2026-08-21 18:29:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308176.060356 | source=vosk | rms=1201 | updated_at=1787308176.060356 | frequency_hz=284.0
- [2026-08-21 18:29:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308177.3107328 | source=vosk | rms=507 | updated_at=1787308176.810386 | frequency_hz=284.0
- [2026-08-21 18:29:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308177.561734 | source=vosk | rms=507 | updated_at=1787308176.810386 | frequency_hz=284.0
- [2026-08-21 18:29:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308179.3103921 | source=vosk | rms=1201 | updated_at=1787308178.5610569 | frequency_hz=284.0
- [2026-08-21 18:29:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308181.570247 | source=vosk | rms=1201 | updated_at=1787308178.5610569 | frequency_hz=284.0
- [2026-08-21 18:29:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308182.560865 | source=vosk | rms=451 | updated_at=1787308182.0602481 | frequency_hz=284.0
- [2026-08-21 18:29:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308183.561874 | source=vosk | rms=290 | updated_at=1787308183.561874 | frequency_hz=284.0
- [2026-08-21 18:29:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308185.3110478 | source=vosk | rms=258 | updated_at=1787308184.31137 | frequency_hz=284.0
- [2026-08-21 18:29:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308185.5606225 | source=vosk | rms=1203 | updated_at=1787308185.5606225 | frequency_hz=284.0
- [2026-08-21 18:29:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308186.56293 | source=vosk | rms=1201 | updated_at=1787308186.0609653 | frequency_hz=284.0
- [2026-08-21 18:29:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308186.8107777 | source=vosk | rms=1201 | updated_at=1787308186.0609653 | frequency_hz=284.0
- [2026-08-21 18:29:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308187.3281806 | source=vosk | rms=1201 | updated_at=1787308186.0609653 | frequency_hz=284.0
- [2026-08-21 18:29:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308187.5610716 | source=vosk | rms=1201 | updated_at=1787308187.5610716 | frequency_hz=284.0
- [2026-08-21 18:29:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308188.5607176 | source=vosk | rms=1200 | updated_at=1787308188.0607064 | frequency_hz=284.0
- [2026-08-21 18:29:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308197.810839 | source=vosk | rms=1200 | updated_at=1787308197.810839 | frequency_hz=284.0
- [2026-08-21 18:29:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308198.5687122 | source=vosk | rms=1201 | updated_at=1787308198.0671716 | frequency_hz=284.0
- [2026-08-21 18:30:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308200.5607827 | source=vosk | rms=1201 | updated_at=1787308200.5607827 | frequency_hz=284.0
- [2026-08-21 18:30:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308201.3103838 | source=vosk | rms=1200 | updated_at=1787308200.8118691 | frequency_hz=284.0
- [2026-08-21 18:30:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308207.3864794 | source=vosk | rms=259 | updated_at=1787308207.3864794 | frequency_hz=284.0
- [2026-08-21 18:30:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308208.387571 | source=vosk | rms=259 | updated_at=1787308207.3864794 | frequency_hz=284.0
- [2026-08-21 18:30:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308209.1370916 | source=vosk | rms=369 | updated_at=1787308209.1370916 | frequency_hz=284.0
- [2026-08-21 18:30:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308217.1372247 | source=vosk | rms=1202 | updated_at=1787308216.6369233 | frequency_hz=284.0
- [2026-08-21 18:30:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308218.1376202 | source=vosk | rms=634 | updated_at=1787308218.1376202 | frequency_hz=284.0
- [2026-08-21 18:30:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308219.1641567 | source=vosk | rms=1200 | updated_at=1787308218.6373901 | frequency_hz=284.0
- [2026-08-21 18:30:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308220.1369298 | source=vosk | rms=1200 | updated_at=1787308218.6373901 | frequency_hz=284.0
- [2026-08-21 18:30:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308220.6372595 | source=vosk | rms=1200 | updated_at=1787308218.6373901 | frequency_hz=284.0
- [2026-08-21 18:30:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308227.8874419 | source=vosk | rms=1200 | updated_at=1787308227.8874419 | frequency_hz=284.0
- [2026-08-21 18:30:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308228.6469283 | source=vosk | rms=1202 | updated_at=1787308228.136672 | frequency_hz=284.0
- [2026-08-21 18:30:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308229.888924 | source=vosk | rms=1202 | updated_at=1787308229.888924 | frequency_hz=284.0
- [2026-08-21 18:30:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308230.6375332 | source=vosk | rms=1200 | updated_at=1787308230.1373987 | frequency_hz=284.0
- [2026-08-21 18:30:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308232.6373491 | source=vosk | rms=1201 | updated_at=1787308232.6373491 | frequency_hz=284.0
- [2026-08-21 18:30:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308233.3868067 | source=vosk | rms=1201 | updated_at=1787308232.8884144 | frequency_hz=284.0
- [2026-08-21 18:30:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308235.8883576 | source=vosk | rms=989 | updated_at=1787308235.8883576 | frequency_hz=284.0
- [2026-08-21 18:30:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308236.38681 | source=vosk | rms=989 | updated_at=1787308235.8883576 | frequency_hz=284.0
- [2026-08-21 18:30:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308240.8873966 | source=vosk | rms=989 | updated_at=1787308235.8883576 | frequency_hz=284.0
- [2026-08-21 18:30:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308241.3866432 | source=vosk | rms=989 | updated_at=1787308235.8883576 | frequency_hz=284.0
- [2026-08-21 18:30:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308242.137432 | source=vosk | rms=1203 | updated_at=1787308242.137432 | frequency_hz=394.0
- [2026-08-21 18:30:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308243.387139 | source=vosk | rms=1200 | updated_at=1787308242.6521084 | frequency_hz=394.0
- [2026-08-21 18:30:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308243.6372526 | source=vosk | rms=1200 | updated_at=1787308242.6521084 | frequency_hz=394.0
- [2026-08-21 18:30:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308246.6368935 | source=vosk | rms=1200 | updated_at=1787308246.136705 | frequency_hz=394.0
- [2026-08-21 18:30:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308248.6366925 | source=vosk | rms=1204 | updated_at=1787308248.6366925 | frequency_hz=394.0
- [2026-08-21 18:30:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308249.6767528 | source=vosk | rms=1200 | updated_at=1787308249.1370971 | frequency_hz=394.0
- [2026-08-21 18:30:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308252.3879378 | source=vosk | rms=1200 | updated_at=1787308252.3879378 | frequency_hz=394.0
- [2026-08-21 18:30:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308253.1373408 | source=vosk | rms=1200 | updated_at=1787308252.6366856 | frequency_hz=394.0
- [2026-08-21 18:30:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308254.8876688 | source=vosk | rms=1202 | updated_at=1787308254.8876688 | frequency_hz=394.0
- [2026-08-21 18:30:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308255.8876002 | source=vosk | rms=1202 | updated_at=1787308255.4109206 | frequency_hz=394.0
- [2026-08-21 18:30:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308257.6377435 | source=vosk | rms=1201 | updated_at=1787308257.6377435 | frequency_hz=394.0
- [2026-08-21 18:30:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308258.6367836 | source=vosk | rms=1202 | updated_at=1787308258.1375215 | frequency_hz=394.0
- [2026-08-21 18:30:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308259.3867342 | source=vosk | rms=450 | updated_at=1787308259.3867342 | frequency_hz=394.0
- [2026-08-21 18:30:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308259.8884964 | source=vosk | rms=450 | updated_at=1787308259.3867342 | frequency_hz=394.0
- [2026-08-21 18:31:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308263.1374888 | source=vosk | rms=1200 | updated_at=1787308263.1374888 | frequency_hz=394.0
- [2026-08-21 18:31:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308264.136964 | source=vosk | rms=1204 | updated_at=1787308263.637349 | frequency_hz=394.0
- [2026-08-21 18:31:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308264.3873692 | source=vosk | rms=762 | updated_at=1787308264.3873692 | frequency_hz=394.0
- [2026-08-21 18:31:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308264.8872898 | source=vosk | rms=762 | updated_at=1787308264.3873692 | frequency_hz=394.0
- [2026-08-21 18:31:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308271.3310165 | source=vosk | rms=589 | updated_at=1787308271.3310165 | frequency_hz=394.0
- [2026-08-21 18:31:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308272.0837884 | source=vosk | rms=589 | updated_at=1787308271.3310165 | frequency_hz=394.0
- [2026-08-21 18:31:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308274.3316019 | source=vosk | rms=1201 | updated_at=1787308274.3316019 | frequency_hz=394.0
- [2026-08-21 18:31:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308275.104474 | source=vosk | rms=1200 | updated_at=1787308274.5808985 | frequency_hz=394.0
- [2026-08-21 18:31:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308275.3313293 | source=vosk | rms=1200 | updated_at=1787308274.5808985 | frequency_hz=394.0
- [2026-08-21 18:31:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308275.8312378 | source=vosk | rms=1200 | updated_at=1787308274.5808985 | frequency_hz=394.0
- [2026-08-21 18:31:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308276.831749 | source=vosk | rms=1200 | updated_at=1787308274.5808985 | frequency_hz=394.0
- [2026-08-21 18:31:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308277.581294 | source=vosk | rms=503 | updated_at=1787308277.0812392 | frequency_hz=394.0
- [2026-08-21 18:31:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308278.83166 | source=vosk | rms=388 | updated_at=1787308278.83166 | frequency_hz=394.0
- [2026-08-21 18:31:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308281.0872307 | source=vosk | rms=503 | updated_at=1787308280.3316412 | frequency_hz=394.0
- [2026-08-21 18:31:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308283.5815935 | source=vosk | rms=332 | updated_at=1787308283.5815935 | frequency_hz=394.0
- [2026-08-21 18:31:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308284.082477 | source=vosk | rms=332 | updated_at=1787308283.5815935 | frequency_hz=394.0
- [2026-08-21 18:31:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308286.0863304 | source=vosk | rms=589 | updated_at=1787308286.0863304 | frequency_hz=394.0
- [2026-08-21 18:31:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308286.5810194 | source=vosk | rms=589 | updated_at=1787308286.0863304 | frequency_hz=394.0
- [2026-08-21 18:31:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308286.831051 | source=vosk | rms=589 | updated_at=1787308286.0863304 | frequency_hz=394.0
- [2026-08-21 18:31:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308287.831926 | source=vosk | rms=589 | updated_at=1787308286.0863304 | frequency_hz=394.0
- [2026-08-21 18:31:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308288.5816538 | source=vosk | rms=589 | updated_at=1787308286.0863304 | frequency_hz=394.0
- [2026-08-21 18:31:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308290.082825 | source=vosk | rms=1200 | updated_at=1787308289.5815766 | frequency_hz=394.0
- [2026-08-21 18:31:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308297.3311858 | source=vosk | rms=1200 | updated_at=1787308297.3311858 | frequency_hz=394.0
- [2026-08-21 18:31:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308298.981911 | source=vosk | rms=463 | updated_at=1787308298.140953 | frequency_hz=394.0
- [2026-08-21 18:31:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308299.2185526 | source=vosk | rms=397 | updated_at=1787308299.2185526 | frequency_hz=394.0
- [2026-08-21 18:31:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308299.7325788 | source=vosk | rms=397 | updated_at=1787308299.2185526 | frequency_hz=394.0
- [2026-08-21 18:31:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308299.9699707 | source=vosk | rms=495 | updated_at=1787308299.9699707 | frequency_hz=394.0
- [2026-08-21 18:31:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308303.2186913 | source=vosk | rms=1201 | updated_at=1787308302.4689014 | frequency_hz=394.0
- [2026-08-21 18:31:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308303.4689007 | source=vosk | rms=191 | updated_at=1787308303.4689007 | frequency_hz=394.0
- [2026-08-21 18:31:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308304.2186768 | source=vosk | rms=191 | updated_at=1787308303.4689007 | frequency_hz=394.0
- [2026-08-21 18:31:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308304.96825 | source=vosk | rms=191 | updated_at=1787308303.4689007 | frequency_hz=394.0
- [2026-08-21 18:31:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308306.9684916 | source=vosk | rms=1203 | updated_at=1787308306.4680643 | frequency_hz=394.0
- [2026-08-21 18:31:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308308.4907963 | source=vosk | rms=1203 | updated_at=1787308306.4680643 | frequency_hz=394.0
- [2026-08-21 18:31:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308308.9893622 | source=vosk | rms=1203 | updated_at=1787308306.4680643 | frequency_hz=394.0
- [2026-08-21 18:31:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308309.490328 | source=vosk | rms=1203 | updated_at=1787308306.4680643 | frequency_hz=394.0
- [2026-08-21 18:31:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308309.9891894 | source=vosk | rms=1203 | updated_at=1787308306.4680643 | frequency_hz=394.0
- [2026-08-21 18:31:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308310.2381294 | source=vosk | rms=441 | updated_at=1787308310.2381294 | frequency_hz=394.0
- [2026-08-21 18:31:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308311.7386782 | source=vosk | rms=672 | updated_at=1787308310.7542725 | frequency_hz=394.0
- [2026-08-21 18:31:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308313.2390387 | source=vosk | rms=273 | updated_at=1787308313.2390387 | frequency_hz=394.0
- [2026-08-21 18:31:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308314.7381425 | source=vosk | rms=294 | updated_at=1787308314.2390006 | frequency_hz=394.0
- [2026-08-21 18:31:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308314.988677 | source=vosk | rms=294 | updated_at=1787308314.2390006 | frequency_hz=394.0
- [2026-08-21 18:31:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308315.48814 | source=vosk | rms=294 | updated_at=1787308314.2390006 | frequency_hz=394.0
- [2026-08-21 18:31:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308315.988996 | source=vosk | rms=298 | updated_at=1787308315.988996 | frequency_hz=394.0
- [2026-08-21 18:31:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308316.988852 | source=vosk | rms=1201 | updated_at=1787308316.488189 | frequency_hz=394.0
- [2026-08-21 18:31:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308317.4898586 | source=vosk | rms=251 | updated_at=1787308317.4898586 | frequency_hz=394.0
- [2026-08-21 18:31:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308319.2383895 | source=vosk | rms=394 | updated_at=1787308318.5132337 | frequency_hz=394.0
- [2026-08-21 18:31:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308319.7388651 | source=vosk | rms=1200 | updated_at=1787308319.7388651 | frequency_hz=394.0
- [2026-08-21 18:32:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308320.557522 | source=vosk | rms=1201 | updated_at=1787308319.9888453 | frequency_hz=394.0
- [2026-08-21 18:32:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308321.4888098 | source=vosk | rms=394 | updated_at=1787308321.4888098 | frequency_hz=394.0
- [2026-08-21 18:32:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308322.738818 | source=vosk | rms=298 | updated_at=1787308322.2390249 | frequency_hz=394.0
- [2026-08-21 18:32:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308324.488901 | source=vosk | rms=1202 | updated_at=1787308324.488901 | frequency_hz=394.0
- [2026-08-21 18:32:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308325.48952 | source=vosk | rms=1202 | updated_at=1787308324.9888318 | frequency_hz=394.0
- [2026-08-21 18:32:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308325.7388582 | source=vosk | rms=286 | updated_at=1787308325.7388582 | frequency_hz=394.0
- [2026-08-21 18:32:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308326.2382796 | source=vosk | rms=286 | updated_at=1787308325.7388582 | frequency_hz=394.0
- [2026-08-21 18:32:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308327.988946 | source=vosk | rms=1202 | updated_at=1787308327.988946 | frequency_hz=394.0
- [2026-08-21 18:32:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308329.2380886 | source=vosk | rms=635 | updated_at=1787308328.7782762 | frequency_hz=394.0
- [2026-08-21 18:32:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308329.7398903 | source=vosk | rms=844 | updated_at=1787308329.7398903 | frequency_hz=394.0
- [2026-08-21 18:32:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308330.2440062 | source=vosk | rms=844 | updated_at=1787308329.7398903 | frequency_hz=394.0
- [2026-08-21 18:32:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308330.4883273 | source=vosk | rms=1200 | updated_at=1787308330.4883273 | frequency_hz=394.0
- [2026-08-21 18:32:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308331.489818 | source=vosk | rms=1200 | updated_at=1787308330.9886732 | frequency_hz=394.0
- [2026-08-21 18:32:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308332.9882467 | source=vosk | rms=1200 | updated_at=1787308330.9886732 | frequency_hz=394.0
- [2026-08-21 18:32:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308333.4887834 | source=vosk | rms=1200 | updated_at=1787308330.9886732 | frequency_hz=394.0
- [2026-08-21 18:32:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308333.9889636 | source=vosk | rms=1200 | updated_at=1787308333.9889636 | frequency_hz=394.0
- [2026-08-21 18:32:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308334.7526102 | source=vosk | rms=1200 | updated_at=1787308334.2459924 | frequency_hz=394.0
- [2026-08-21 18:32:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308336.0427032 | source=vosk | rms=1200 | updated_at=1787308336.0427032 | frequency_hz=394.0
- [2026-08-21 18:32:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308336.989372 | source=vosk | rms=436 | updated_at=1787308336.4885728 | frequency_hz=394.0
- [2026-08-21 18:32:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308337.988286 | source=vosk | rms=896 | updated_at=1787308337.988286 | frequency_hz=394.0
- [2026-08-21 18:32:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308339.6198409 | source=vosk | rms=1201 | updated_at=1787308338.988245 | frequency_hz=394.0
- [2026-08-21 18:32:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308339.8688593 | source=vosk | rms=1201 | updated_at=1787308338.988245 | frequency_hz=394.0
- [2026-08-21 18:32:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308340.3688846 | source=vosk | rms=1201 | updated_at=1787308338.988245 | frequency_hz=394.0
- [2026-08-21 18:32:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308341.3719988 | source=vosk | rms=1201 | updated_at=1787308338.988245 | frequency_hz=394.0
- [2026-08-21 18:32:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308343.6183279 | source=vosk | rms=589 | updated_at=1787308343.1187162 | frequency_hz=394.0
- [2026-08-21 18:32:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308346.1194868 | source=vosk | rms=1200 | updated_at=1787308346.1189592 | frequency_hz=394.0
- [2026-08-21 18:32:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308346.8692575 | source=vosk | rms=1202 | updated_at=1787308346.3728714 | frequency_hz=394.0
- [2026-08-21 18:32:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308352.369279 | source=vosk | rms=1201 | updated_at=1787308352.369279 | frequency_hz=394.0
- [2026-08-21 18:32:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308353.3740737 | source=vosk | rms=932 | updated_at=1787308352.8686988 | frequency_hz=394.0
- [2026-08-21 18:32:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787308353.6192062 | source=vosk | rms=932 | updated_at=1787308352.8686988 | frequency_hz=394.0
- [2026-08-21 18:32:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787308354.1185262 | source=vosk | rms=932 | updated_at=1787308352.8686988 | frequency_hz=394.0

# SMART SENTRY V5.0.0 Runtime Conversation Export

- Generated: 2026-07-06 09:03:42
- Entries: 511
- Roles: {'assistant': 4, 'system': 370, 'operator': 137}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 370, 'spoken_confirmation': 2, 'voice_transcript_partial': 115, 'voice_transcript_final': 21, 'voice_command': 1}
- Channels: {'text': 2, 'voice': 509}
- Latest operator request: cannot fire safety is
- Latest assistant message: Running Smart Sentry now. Connecting the Smart Sentry boards first.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-07-06 08:58:03] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-07-06 08:58:03] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-07-06 08:58:05] system / voice_status / voice: listening
  meta: kind=status | timestamp=1783299485.3913863 | source=vosk
- [2026-07-06 08:58:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299485.8997166 | source=vosk | rms=493 | updated_at=1783299485.8997166
- [2026-07-06 08:58:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299486.400794 | source=vosk | rms=493 | updated_at=1783299485.8997166
- [2026-07-06 08:58:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299492.900022 | source=vosk | rms=760 | updated_at=1783299492.900022
- [2026-07-06 08:58:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299493.3995507 | source=vosk | rms=760 | updated_at=1783299492.900022
- [2026-07-06 08:58:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299493.899595 | source=vosk | rms=243 | updated_at=1783299493.899595
- [2026-07-06 08:58:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299494.3991573 | source=vosk | rms=243 | updated_at=1783299493.899595
- [2026-07-06 08:58:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299494.8995194 | source=vosk | rms=162 | updated_at=1783299494.8995194
- [2026-07-06 08:58:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299495.4006748 | source=vosk | rms=162 | updated_at=1783299494.8995194
- [2026-07-06 08:58:42] assistant / spoken_confirmation / voice: Smart Sentry is ready.
  meta: interrupt=True | assistant_output=False | spoken=True
- [2026-07-06 08:58:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299506.5607212 | source=vosk | rms=162 | updated_at=1783299494.8995194
- [2026-07-06 08:58:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299507.0593073 | source=vosk | rms=162 | updated_at=1783299494.8995194
- [2026-07-06 08:58:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299512.3090484 | source=vosk | rms=876 | updated_at=1783299512.3090484
- [2026-07-06 08:58:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299513.05978 | source=vosk | rms=175 | updated_at=1783299512.5600502
- [2026-07-06 08:58:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299513.5597506 | source=vosk | rms=175 | updated_at=1783299512.5600502
- [2026-07-06 08:58:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299514.3100142 | source=vosk | rms=175 | updated_at=1783299512.5600502
- [2026-07-06 08:58:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299515.8096159 | source=vosk | rms=314 | updated_at=1783299515.8096159
- [2026-07-06 08:58:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299516.8099391 | source=vosk | rms=427 | updated_at=1783299516.3100507
- [2026-07-06 08:58:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299517.0608296 | source=vosk | rms=127 | updated_at=1783299517.0593262
- [2026-07-06 08:58:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299518.560482 | source=vosk | rms=181 | updated_at=1783299518.0603092
- [2026-07-06 08:58:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299519.0597467 | source=vosk | rms=1203 | updated_at=1783299519.0597467
- [2026-07-06 08:58:45] operator / voice_transcript_partial / voice: smart such
  meta: kind=partial | timestamp=1783299525.8051255 | source=vosk | rms=1202 | updated_at=1783299525.7099428
- [2026-07-06 08:58:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299525.9603603 | source=vosk | rms=666 | updated_at=1783299525.9603603
- [2026-07-06 08:58:46] operator / voice_transcript_partial / voice: smart fact
  meta: kind=partial | timestamp=1783299526.0815718 | source=vosk | rms=666 | updated_at=1783299525.9603603
- [2026-07-06 08:58:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299526.2104607 | source=vosk | rms=309 | updated_at=1783299526.2104607
- [2026-07-06 08:58:46] operator / voice_transcript_partial / voice: smart such threats
  meta: kind=partial | timestamp=1783299526.2706678 | source=vosk | rms=309 | updated_at=1783299526.2104607
- [2026-07-06 08:58:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299526.4612482 | source=vosk | rms=346 | updated_at=1783299526.4612482
- [2026-07-06 08:58:46] operator / voice_transcript_partial / voice: smart fact
  meta: kind=partial | timestamp=1783299526.4914627 | source=vosk | rms=346 | updated_at=1783299526.4612482
- [2026-07-06 08:58:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299526.7110128 | source=vosk | rms=346 | updated_at=1783299526.4612482
- [2026-07-06 08:58:46] operator / voice_transcript_partial / voice: smart fact ready
  meta: kind=partial | timestamp=1783299526.7197144 | source=vosk | rms=346 | updated_at=1783299526.4612482
- [2026-07-06 08:58:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299526.9610348 | source=vosk | rms=346 | updated_at=1783299526.4612482
- [2026-07-06 08:58:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299527.2108169 | source=vosk | rms=346 | updated_at=1783299526.4612482
- [2026-07-06 08:58:47] operator / voice_transcript_final / voice: smart fact ready
  meta: kind=final | timestamp=1783299527.5171077 | source=final | rms=346 | updated_at=1783299526.4612482
- [2026-07-06 08:58:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299527.6380374 | source=vosk | rms=346 | updated_at=1783299526.4612482
- [2026-07-06 08:58:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299527.7103505 | source=vosk | rms=143 | updated_at=1783299527.7103505
- [2026-07-06 08:58:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299528.4622288 | source=vosk | rms=274 | updated_at=1783299527.960361
- [2026-07-06 08:58:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299528.7096965 | source=vosk | rms=173 | updated_at=1783299528.7096965
- [2026-07-06 08:58:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299529.21106 | source=vosk | rms=173 | updated_at=1783299528.7096965
- [2026-07-06 08:58:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299529.4595392 | source=vosk | rms=1201 | updated_at=1783299529.4595392
- [2026-07-06 08:58:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299530.4624894 | source=vosk | rms=1205 | updated_at=1783299529.9614773
- [2026-07-06 08:58:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299533.2137198 | source=vosk | rms=249 | updated_at=1783299533.2137198
- [2026-07-06 08:58:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299534.4600878 | source=vosk | rms=239 | updated_at=1783299533.710329
- [2026-07-06 08:58:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299535.209877 | source=vosk | rms=239 | updated_at=1783299533.710329
- [2026-07-06 08:58:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299537.714367 | source=vosk | rms=294 | updated_at=1783299536.9601183
- [2026-07-06 08:58:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299538.2104645 | source=vosk | rms=523 | updated_at=1783299538.2104645
- [2026-07-06 08:58:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299538.712296 | source=vosk | rms=523 | updated_at=1783299538.2104645
- [2026-07-06 08:59:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299540.460349 | source=vosk | rms=362 | updated_at=1783299540.460349
- [2026-07-06 08:59:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299541.461555 | source=vosk | rms=994 | updated_at=1783299540.9625115
- [2026-07-06 08:59:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299544.210898 | source=vosk | rms=828 | updated_at=1783299544.210898
- [2026-07-06 08:59:07] operator / voice_transcript_partial / voice: you
  meta: kind=partial | timestamp=1783299547.0466263 | source=vosk | rms=1988 | updated_at=1783299546.9605513 | frequency_hz=312.5
- [2026-07-06 08:59:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299547.210773 | source=vosk | rms=3238 | updated_at=1783299547.210773 | frequency_hz=312.5
- [2026-07-06 08:59:07] operator / voice_transcript_partial / voice: you you
  meta: kind=partial | timestamp=1783299547.5038228 | source=vosk | rms=2292 | updated_at=1783299547.460666 | frequency_hz=312.5
- [2026-07-06 08:59:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299547.7106724 | source=vosk | rms=2072 | updated_at=1783299547.7106724 | frequency_hz=312.5
- [2026-07-06 08:59:07] operator / voice_transcript_partial / voice: you you run the
  meta: kind=partial | timestamp=1783299547.7346966 | source=vosk | rms=2072 | updated_at=1783299547.7106724 | frequency_hz=312.5
- [2026-07-06 08:59:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299547.9619682 | source=vosk | rms=1207 | updated_at=1783299547.9614522 | frequency_hz=312.5
- [2026-07-06 08:59:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299548.2101443 | source=vosk | rms=2326 | updated_at=1783299548.2101443 | frequency_hz=279.4
- [2026-07-06 08:59:08] operator / voice_transcript_partial / voice: you you run the smarts
  meta: kind=partial | timestamp=1783299548.2825747 | source=vosk | rms=2326 | updated_at=1783299548.2101443 | frequency_hz=279.4
- [2026-07-06 08:59:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299548.4601805 | source=vosk | rms=1201 | updated_at=1783299548.4601805 | frequency_hz=232.7
- [2026-07-06 08:59:08] operator / voice_transcript_partial / voice: you you run the smart century
  meta: kind=partial | timestamp=1783299548.4813893 | source=vosk | rms=1201 | updated_at=1783299548.4601805 | frequency_hz=232.7
- [2026-07-06 08:59:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299548.710572 | source=vosk | rms=1202 | updated_at=1783299548.710572 | frequency_hz=224.1
- [2026-07-06 08:59:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299548.9614797 | source=vosk | rms=1200 | updated_at=1783299548.9604793 | frequency_hz=224.1
- [2026-07-06 08:59:08] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1783299548.9796908 | source=final | rms=1200 | updated_at=1783299548.9604793 | frequency_hz=224.1
- [2026-07-06 08:59:09] system / voice_status / voice: processing
  meta: kind=status | timestamp=1783299549.0234387 | source=state | rms=1200 | updated_at=1783299548.9604793 | frequency_hz=224.1
- [2026-07-06 08:59:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299549.0234387 | source=state | rms=1200 | updated_at=1783299548.9604793 | frequency_hz=224.1
- [2026-07-06 08:59:09] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-07-06 08:59:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299549.2103195 | source=vosk | rms=1104 | updated_at=1783299549.2103195 | frequency_hz=187.7
- [2026-07-06 08:59:09] assistant / spoken_confirmation / voice: Running Smart Sentry now. Connecting the Smart Sentry boards first.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-07-06 08:59:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299550.7117684 | source=vosk | rms=920 | updated_at=1783299549.7103765 | frequency_hz=249.4
- [2026-07-06 08:59:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299550.961742 | source=vosk | rms=522 | updated_at=1783299550.961742 | frequency_hz=249.4
- [2026-07-06 08:59:13] operator / voice_transcript_partial / voice: my sense
  meta: kind=partial | timestamp=1783299553.2038345 | source=vosk | rms=700 | updated_at=1783299552.2318182 | frequency_hz=249.4
- [2026-07-06 08:59:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299553.2038345 | source=vosk | rms=700 | updated_at=1783299552.2318182 | frequency_hz=249.4
- [2026-07-06 08:59:13] operator / voice_transcript_partial / voice: mark century
  meta: kind=partial | timestamp=1783299553.24257 | source=vosk | rms=700 | updated_at=1783299552.2318182 | frequency_hz=249.4
- [2026-07-06 08:59:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299553.4814858 | source=vosk | rms=1018 | updated_at=1783299553.4814858 | frequency_hz=249.4
- [2026-07-06 08:59:13] operator / voice_transcript_partial / voice: mark century now
  meta: kind=partial | timestamp=1783299553.4909897 | source=vosk | rms=1018 | updated_at=1783299553.4814858 | frequency_hz=249.4
- [2026-07-06 08:59:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299553.7335892 | source=vosk | rms=679 | updated_at=1783299553.7335892 | frequency_hz=249.4
- [2026-07-06 08:59:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299553.9803634 | source=vosk | rms=679 | updated_at=1783299553.7335892 | frequency_hz=249.4
- [2026-07-06 08:59:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299554.2303464 | source=vosk | rms=702 | updated_at=1783299554.2303464 | frequency_hz=249.4
- [2026-07-06 08:59:14] operator / voice_transcript_partial / voice: mark century now connecting the
  meta: kind=partial | timestamp=1783299554.2448912 | source=vosk | rms=702 | updated_at=1783299554.2303464 | frequency_hz=249.4
- [2026-07-06 08:59:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299554.481781 | source=vosk | rms=702 | updated_at=1783299554.2303464 | frequency_hz=249.4
- [2026-07-06 08:59:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299554.731011 | source=vosk | rms=702 | updated_at=1783299554.2303464 | frequency_hz=249.4
- [2026-07-06 08:59:14] operator / voice_transcript_partial / voice: mark century now connecting the smart
  meta: kind=partial | timestamp=1783299554.7508109 | source=vosk | rms=702 | updated_at=1783299554.2303464 | frequency_hz=249.4
- [2026-07-06 08:59:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299554.98081 | source=vosk | rms=702 | updated_at=1783299554.2303464 | frequency_hz=249.4
- [2026-07-06 08:59:14] operator / voice_transcript_partial / voice: mark century now connecting the smart century
  meta: kind=partial | timestamp=1783299554.9938385 | source=vosk | rms=702 | updated_at=1783299554.2303464 | frequency_hz=249.4
- [2026-07-06 08:59:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299555.231698 | source=vosk | rms=1200 | updated_at=1783299555.231698 | frequency_hz=249.4
- [2026-07-06 08:59:15] operator / voice_transcript_partial / voice: mark century now connecting the smart such reports from
  meta: kind=partial | timestamp=1783299555.3709438 | source=vosk | rms=1200 | updated_at=1783299555.231698 | frequency_hz=249.4
- [2026-07-06 08:59:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299555.4815543 | source=vosk | rms=1201 | updated_at=1783299555.4815543 | frequency_hz=249.4
- [2026-07-06 08:59:15] operator / voice_transcript_partial / voice: mark century now connecting the smart century for it's first
  meta: kind=partial | timestamp=1783299555.5041826 | source=vosk | rms=1201 | updated_at=1783299555.4815543 | frequency_hz=249.4
- [2026-07-06 08:59:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299555.7306988 | source=vosk | rms=1201 | updated_at=1783299555.7306988 | frequency_hz=249.4
- [2026-07-06 08:59:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299555.994411 | source=vosk | rms=1203 | updated_at=1783299555.994411 | frequency_hz=249.4
- [2026-07-06 08:59:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299556.2300115 | source=vosk | rms=1200 | updated_at=1783299556.2300115 | frequency_hz=249.4
- [2026-07-06 08:59:16] operator / voice_transcript_final / voice: mark century now connecting the smart sentry for first
  meta: kind=final | timestamp=1783299556.5344906 | source=final | rms=1200 | updated_at=1783299556.2300115 | frequency_hz=249.4
- [2026-07-06 08:59:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299556.6752937 | source=vosk | rms=1200 | updated_at=1783299556.2300115 | frequency_hz=249.4
- [2026-07-06 08:59:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299556.6752937 | source=vosk | rms=1203 | updated_at=1783299556.6752937 | frequency_hz=249.4
- [2026-07-06 08:59:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299557.482431 | source=vosk | rms=884 | updated_at=1783299556.7315774 | frequency_hz=262.2
- [2026-07-06 08:59:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299557.7333686 | source=vosk | rms=498 | updated_at=1783299557.7333686 | frequency_hz=234.8
- [2026-07-06 08:59:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299560.4807117 | source=vosk | rms=621 | updated_at=1783299559.4816012 | frequency_hz=187.2
- [2026-07-06 08:59:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299561.7316918 | source=vosk | rms=621 | updated_at=1783299559.4816012 | frequency_hz=187.2
- [2026-07-06 08:59:23] operator / voice_transcript_partial / voice: cannot fire hd is not
  meta: kind=partial | timestamp=1783299563.8666878 | source=vosk | rms=1088 | updated_at=1783299563.8220518 | frequency_hz=187.2
- [2026-07-06 08:59:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299564.0091155 | source=vosk | rms=1212 | updated_at=1783299563.9817524 | frequency_hz=187.2
- [2026-07-06 08:59:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299564.2298982 | source=vosk | rms=829 | updated_at=1783299564.2298982 | frequency_hz=187.2
- [2026-07-06 08:59:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299564.4803286 | source=vosk | rms=1032 | updated_at=1783299564.4803286 | frequency_hz=187.2
- [2026-07-06 08:59:25] operator / voice_transcript_final / voice: cannot fire hd is not off
  meta: kind=final | timestamp=1783299565.0267472 | source=final | rms=1032 | updated_at=1783299564.4803286 | frequency_hz=187.2
- [2026-07-06 08:59:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299565.1969728 | source=vosk | rms=1032 | updated_at=1783299564.4803286 | frequency_hz=187.2
- [2026-07-06 08:59:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299565.1969728 | source=vosk | rms=1032 | updated_at=1783299564.4803286 | frequency_hz=187.2
- [2026-07-06 08:59:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299567.4806871 | source=vosk | rms=870 | updated_at=1783299565.732175 | frequency_hz=240.9
- [2026-07-06 08:59:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299568.480668 | source=vosk | rms=870 | updated_at=1783299565.732175 | frequency_hz=240.9
- [2026-07-06 08:59:35] operator / voice_transcript_partial / voice: ilya
  meta: kind=partial | timestamp=1783299575.0007572 | source=vosk | rms=1233 | updated_at=1783299574.9807267 | frequency_hz=286.1
- [2026-07-06 08:59:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299575.4808125 | source=vosk | rms=891 | updated_at=1783299575.4808125 | frequency_hz=286.1
- [2026-07-06 08:59:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299575.7339356 | source=vosk | rms=1054 | updated_at=1783299575.7339356 | frequency_hz=249.0
- [2026-07-06 08:59:35] operator / voice_transcript_final / voice: ilya
  meta: kind=final | timestamp=1783299575.9559014 | source=final | rms=1054 | updated_at=1783299575.7339356 | frequency_hz=249.0
- [2026-07-06 08:59:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299575.996293 | source=vosk | rms=8289 | updated_at=1783299575.996293 | frequency_hz=249.0
- [2026-07-06 08:59:36] operator / voice_transcript_partial / voice: jade the
  meta: kind=partial | timestamp=1783299576.8247213 | source=vosk | rms=14803 | updated_at=1783299576.7312653 | frequency_hz=249.0
- [2026-07-06 08:59:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299576.981119 | source=vosk | rms=8193 | updated_at=1783299576.981119 | frequency_hz=249.0
- [2026-07-06 08:59:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299577.2310317 | source=vosk | rms=8640 | updated_at=1783299577.2310317 | frequency_hz=249.0
- [2026-07-06 08:59:37] operator / voice_transcript_partial / voice: jade the profile to
  meta: kind=partial | timestamp=1783299577.3048906 | source=vosk | rms=8640 | updated_at=1783299577.2310317 | frequency_hz=249.0
- [2026-07-06 08:59:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299577.4807134 | source=vosk | rms=7228 | updated_at=1783299577.4807134 | frequency_hz=249.0
- [2026-07-06 08:59:37] operator / voice_transcript_partial / voice: jade the profile the
  meta: kind=partial | timestamp=1783299577.5203345 | source=vosk | rms=7228 | updated_at=1783299577.4807134 | frequency_hz=249.0
- [2026-07-06 08:59:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299577.7326763 | source=vosk | rms=5270 | updated_at=1783299577.7326763 | frequency_hz=249.0
- [2026-07-06 08:59:37] operator / voice_transcript_partial / voice: jade the profile too smart
  meta: kind=partial | timestamp=1783299577.7426896 | source=vosk | rms=5270 | updated_at=1783299577.7326763 | frequency_hz=249.0
- [2026-07-06 08:59:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299577.9807851 | source=vosk | rms=5656 | updated_at=1783299577.9807851 | frequency_hz=249.0
- [2026-07-06 08:59:37] operator / voice_transcript_partial / voice: jade the profile too smart sentries
  meta: kind=partial | timestamp=1783299577.997812 | source=vosk | rms=5656 | updated_at=1783299577.9807851 | frequency_hz=249.0
- [2026-07-06 08:59:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299578.230748 | source=vosk | rms=8427 | updated_at=1783299578.230748 | frequency_hz=249.0
- [2026-07-06 08:59:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299578.4811826 | source=vosk | rms=10585 | updated_at=1783299578.4811826 | frequency_hz=249.0
- [2026-07-06 08:59:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299578.730484 | source=vosk | rms=2150 | updated_at=1783299578.730484 | frequency_hz=249.0
- [2026-07-06 08:59:38] operator / voice_transcript_partial / voice: jade the profile too smart sentry speed
  meta: kind=partial | timestamp=1783299578.7605176 | source=vosk | rms=2150 | updated_at=1783299578.730484 | frequency_hz=249.0
- [2026-07-06 08:59:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299578.981458 | source=vosk | rms=1201 | updated_at=1783299578.981458 | frequency_hz=259.9
- [2026-07-06 08:59:39] operator / voice_transcript_partial / voice: jade the profile too smart sentry speed ripe
  meta: kind=partial | timestamp=1783299579.0432215 | source=vosk | rms=1201 | updated_at=1783299578.981458 | frequency_hz=259.9
- [2026-07-06 08:59:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299579.2320473 | source=vosk | rms=1201 | updated_at=1783299579.2320473 | frequency_hz=313.1
- [2026-07-06 08:59:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299579.4805202 | source=vosk | rms=1039 | updated_at=1783299579.4805202 | frequency_hz=259.5
- [2026-07-06 08:59:39] operator / voice_transcript_final / voice: jade the profile too smart sentry speed vibe
  meta: kind=final | timestamp=1783299579.797531 | source=final | rms=1039 | updated_at=1783299579.4805202 | frequency_hz=259.5
- [2026-07-06 08:59:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299579.9261384 | source=vosk | rms=1039 | updated_at=1783299579.4805202 | frequency_hz=259.5
- [2026-07-06 08:59:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299579.9261384 | source=vosk | rms=1201 | updated_at=1783299579.9261384 | frequency_hz=314.3
- [2026-07-06 08:59:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299580.9807785 | source=vosk | rms=1201 | updated_at=1783299579.9261384 | frequency_hz=314.3
- [2026-07-06 08:59:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299581.7314017 | source=vosk | rms=996 | updated_at=1783299581.7314017 | frequency_hz=314.3
- [2026-07-06 08:59:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299583.4841535 | source=vosk | rms=1202 | updated_at=1783299582.9814196 | frequency_hz=268.7
- [2026-07-06 08:59:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299583.732336 | source=vosk | rms=11215 | updated_at=1783299583.732336 | frequency_hz=268.7
- [2026-07-06 08:59:43] operator / voice_transcript_partial / voice: cannot save the
  meta: kind=partial | timestamp=1783299583.794469 | source=vosk | rms=11215 | updated_at=1783299583.732336 | frequency_hz=268.7
- [2026-07-06 08:59:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299583.981431 | source=vosk | rms=9122 | updated_at=1783299583.981431 | frequency_hz=268.7
- [2026-07-06 08:59:44] operator / voice_transcript_partial / voice: cannot fire safety
  meta: kind=partial | timestamp=1783299584.0110116 | source=vosk | rms=9122 | updated_at=1783299583.981431 | frequency_hz=268.7
- [2026-07-06 08:59:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299584.2309294 | source=vosk | rms=11251 | updated_at=1783299584.2309294 | frequency_hz=268.7
- [2026-07-06 08:59:44] operator / voice_transcript_partial / voice: cannot fly safely
  meta: kind=partial | timestamp=1783299584.287754 | source=vosk | rms=11251 | updated_at=1783299584.2309294 | frequency_hz=268.7
- [2026-07-06 08:59:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299584.4813652 | source=vosk | rms=13806 | updated_at=1783299584.4813652 | frequency_hz=268.7
- [2026-07-06 08:59:44] operator / voice_transcript_partial / voice: cannot save the change to
  meta: kind=partial | timestamp=1783299584.5333014 | source=vosk | rms=13806 | updated_at=1783299584.4813652 | frequency_hz=268.7
- [2026-07-06 08:59:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299584.7308679 | source=vosk | rms=7541 | updated_at=1783299584.7308679 | frequency_hz=268.7
- [2026-07-06 08:59:44] operator / voice_transcript_partial / voice: cannot fly safely changed
  meta: kind=partial | timestamp=1783299584.7750666 | source=vosk | rms=7541 | updated_at=1783299584.7308679 | frequency_hz=268.7
- [2026-07-06 08:59:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299584.9812179 | source=vosk | rms=5689 | updated_at=1783299584.9812179 | frequency_hz=268.7
- [2026-07-06 08:59:45] operator / voice_transcript_partial / voice: cannot fly safely change the perfect
  meta: kind=partial | timestamp=1783299585.067547 | source=vosk | rms=5689 | updated_at=1783299584.9812179 | frequency_hz=268.7
- [2026-07-06 08:59:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299585.2310994 | source=vosk | rms=4195 | updated_at=1783299585.2310994 | frequency_hz=268.7
- [2026-07-06 08:59:45] operator / voice_transcript_partial / voice: cannot save the change to pay for this
  meta: kind=partial | timestamp=1783299585.3199852 | source=vosk | rms=4195 | updated_at=1783299585.2310994 | frequency_hz=268.7
- [2026-07-06 08:59:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299585.487438 | source=vosk | rms=4244 | updated_at=1783299585.487438 | frequency_hz=268.7
- [2026-07-06 08:59:45] operator / voice_transcript_partial / voice: cannot save the change to provide the smart
  meta: kind=partial | timestamp=1783299585.523839 | source=vosk | rms=4244 | updated_at=1783299585.487438 | frequency_hz=268.7
- [2026-07-06 08:59:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299585.7312372 | source=vosk | rms=6172 | updated_at=1783299585.7312372 | frequency_hz=268.7
- [2026-07-06 08:59:45] operator / voice_transcript_partial / voice: cannot save the change to provide the smart center is
  meta: kind=partial | timestamp=1783299585.753282 | source=vosk | rms=6172 | updated_at=1783299585.7312372 | frequency_hz=268.7
- [2026-07-06 08:59:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299585.981476 | source=vosk | rms=9052 | updated_at=1783299585.981476 | frequency_hz=268.7
- [2026-07-06 08:59:46] operator / voice_transcript_partial / voice: cannot save the change to provide the smart century speed
  meta: kind=partial | timestamp=1783299586.01008 | source=vosk | rms=9052 | updated_at=1783299585.981476 | frequency_hz=268.7
- [2026-07-06 08:59:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299586.2313433 | source=vosk | rms=2405 | updated_at=1783299586.2313433 | frequency_hz=295.8
- [2026-07-06 08:59:46] operator / voice_transcript_partial / voice: cannot save the change to provide the smart century
  meta: kind=partial | timestamp=1783299586.2595305 | source=vosk | rms=2405 | updated_at=1783299586.2313433 | frequency_hz=295.8
- [2026-07-06 08:59:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299586.732232 | source=vosk | rms=2405 | updated_at=1783299586.2313433 | frequency_hz=295.8
- [2026-07-06 08:59:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299598.6016076 | source=vosk | rms=2988 | updated_at=1783299598.6016076 | frequency_hz=364.0
- [2026-07-06 08:59:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299599.5297182 | source=vosk | rms=4678 | updated_at=1783299598.852652 | frequency_hz=364.0
- [2026-07-06 09:00:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299613.5328934 | source=vosk | rms=833 | updated_at=1783299613.5328934 | frequency_hz=364.0
- [2026-07-06 09:00:13] operator / voice_transcript_partial / voice: cannot save the change to provide the smart century speed five
  meta: kind=partial | timestamp=1783299613.5556765 | source=vosk | rms=833 | updated_at=1783299613.5328934 | frequency_hz=364.0
- [2026-07-06 09:00:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299613.7812355 | source=vosk | rms=833 | updated_at=1783299613.5328934 | frequency_hz=364.0
- [2026-07-06 09:00:14] operator / voice_transcript_final / voice: cannot fly safety change to provide the smart sentry speed five
  meta: kind=final | timestamp=1783299614.3826826 | source=final | rms=833 | updated_at=1783299613.5328934 | frequency_hz=364.0
- [2026-07-06 09:00:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299614.6836343 | source=vosk | rms=833 | updated_at=1783299613.5328934 | frequency_hz=364.0
- [2026-07-06 09:00:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299616.0314224 | source=vosk | rms=833 | updated_at=1783299613.5328934 | frequency_hz=364.0
- [2026-07-06 09:00:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299618.0315433 | source=vosk | rms=833 | updated_at=1783299613.5328934 | frequency_hz=364.0
- [2026-07-06 09:00:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299619.7826483 | source=vosk | rms=833 | updated_at=1783299613.5328934 | frequency_hz=364.0
- [2026-07-06 09:00:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299620.782239 | source=vosk | rms=833 | updated_at=1783299613.5328934 | frequency_hz=364.0
- [2026-07-06 09:00:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299622.031895 | source=vosk | rms=833 | updated_at=1783299613.5328934 | frequency_hz=364.0
- [2026-07-06 09:00:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299622.7914786 | source=vosk | rms=833 | updated_at=1783299613.5328934 | frequency_hz=364.0
- [2026-07-06 09:00:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299623.0319796 | source=vosk | rms=833 | updated_at=1783299613.5328934 | frequency_hz=364.0
- [2026-07-06 09:00:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299624.0897467 | source=vosk | rms=833 | updated_at=1783299613.5328934 | frequency_hz=364.0
- [2026-07-06 09:00:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299628.0326216 | source=vosk | rms=432 | updated_at=1783299628.0326216 | frequency_hz=364.0
- [2026-07-06 09:00:29] operator / voice_transcript_partial / voice: cannot fire safety as cannot safety is no cannot fire safety
  meta: kind=partial | timestamp=1783299629.5459626 | source=vosk | rms=553 | updated_at=1783299629.5319257 | frequency_hz=364.0
- [2026-07-06 09:00:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299629.7828865 | source=vosk | rms=349 | updated_at=1783299629.7828865 | frequency_hz=364.0
- [2026-07-06 09:00:29] operator / voice_transcript_partial / voice: cannot fire safety as cannot safety is no cannot fire safety is
  meta: kind=partial | timestamp=1783299629.7974086 | source=vosk | rms=349 | updated_at=1783299629.7828865 | frequency_hz=364.0
- [2026-07-06 09:00:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299630.0320542 | source=vosk | rms=349 | updated_at=1783299629.7828865 | frequency_hz=364.0
- [2026-07-06 09:00:30] operator / voice_transcript_partial / voice: cannot fire safety as cannot safety is no cannot fire safety is not
  meta: kind=partial | timestamp=1783299630.048499 | source=vosk | rms=349 | updated_at=1783299629.7828865 | frequency_hz=364.0
- [2026-07-06 09:00:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299630.2814033 | source=vosk | rms=349 | updated_at=1783299629.7828865 | frequency_hz=364.0
- [2026-07-06 09:00:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299630.781386 | source=vosk | rms=349 | updated_at=1783299629.7828865 | frequency_hz=364.0
- [2026-07-06 09:00:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299631.7821028 | source=vosk | rms=761 | updated_at=1783299631.7821028 | frequency_hz=364.0
- [2026-07-06 09:00:31] operator / voice_transcript_partial / voice: cannot fire safety as cannot safety is no cannot fire safety is not aren't
  meta: kind=partial | timestamp=1783299631.8022616 | source=vosk | rms=761 | updated_at=1783299631.7821028 | frequency_hz=364.0
- [2026-07-06 09:00:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299632.0324972 | source=vosk | rms=384 | updated_at=1783299632.0324972 | frequency_hz=364.0
- [2026-07-06 09:00:32] operator / voice_transcript_partial / voice: cannot fire safety as cannot safety is no cannot fire safety is not aren't present
  meta: kind=partial | timestamp=1783299632.0590787 | source=vosk | rms=384 | updated_at=1783299632.0324972 | frequency_hz=364.0
- [2026-07-06 09:00:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299632.3398473 | source=vosk | rms=378 | updated_at=1783299632.3398473 | frequency_hz=364.0
- [2026-07-06 09:00:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299632.531509 | source=vosk | rms=381 | updated_at=1783299632.531509 | frequency_hz=364.0
- [2026-07-06 09:00:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299632.7817335 | source=vosk | rms=482 | updated_at=1783299632.7817335 | frequency_hz=364.0
- [2026-07-06 09:00:32] operator / voice_transcript_partial / voice: cannot fire safety as cannot safety is no cannot fire safety is not aren't present profile
  meta: kind=partial | timestamp=1783299632.8002949 | source=vosk | rms=482 | updated_at=1783299632.7817335 | frequency_hz=364.0
- [2026-07-06 09:00:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299633.031844 | source=vosk | rms=543 | updated_at=1783299633.031844 | frequency_hz=364.0
- [2026-07-06 09:00:33] operator / voice_transcript_partial / voice: cannot fire safety as cannot safety is no cannot fire safety is not aren't present profiles that to
  meta: kind=partial | timestamp=1783299633.0584273 | source=vosk | rms=543 | updated_at=1783299633.031844 | frequency_hz=364.0
- [2026-07-06 09:00:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299633.5329971 | source=vosk | rms=543 | updated_at=1783299633.031844 | frequency_hz=364.0
- [2026-07-06 09:00:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299633.7820055 | source=vosk | rms=565 | updated_at=1783299633.7820055 | frequency_hz=364.0
- [2026-07-06 09:00:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299634.0317776 | source=vosk | rms=566 | updated_at=1783299634.0317776 | frequency_hz=364.0
- [2026-07-06 09:00:34] operator / voice_transcript_partial / voice: cannot fire safety as cannot safety is no cannot fire safety is not aren't present profiles that to cast
  meta: kind=partial | timestamp=1783299634.061468 | source=vosk | rms=566 | updated_at=1783299634.0317776 | frequency_hz=364.0
- [2026-07-06 09:00:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299634.2819138 | source=vosk | rms=353 | updated_at=1783299634.2819138 | frequency_hz=364.0
- [2026-07-06 09:00:34] operator / voice_transcript_partial / voice: cannot fire safety as cannot safety is no cannot fire safety is not aren't present profiles that to cast speed
  meta: kind=partial | timestamp=1783299634.3080292 | source=vosk | rms=353 | updated_at=1783299634.2819138 | frequency_hz=364.0
- [2026-07-06 09:00:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299634.531719 | source=vosk | rms=433 | updated_at=1783299634.531719 | frequency_hz=364.0
- [2026-07-06 09:00:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299634.7819712 | source=vosk | rms=406 | updated_at=1783299634.7819712 | frequency_hz=364.0
- [2026-07-06 09:00:34] operator / voice_transcript_partial / voice: cannot fire safety as cannot safety is no cannot fire safety is not aren't present profiles that to cast speed five
  meta: kind=partial | timestamp=1783299634.7974966 | source=vosk | rms=406 | updated_at=1783299634.7819712 | frequency_hz=364.0
- [2026-07-06 09:00:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299635.0326545 | source=vosk | rms=381 | updated_at=1783299635.0326545 | frequency_hz=364.0
- [2026-07-06 09:00:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299635.2816808 | source=vosk | rms=493 | updated_at=1783299635.2816808 | frequency_hz=364.0
- [2026-07-06 09:00:35] operator / voice_transcript_partial / voice: cannot fire safety as cannot safety is no cannot fire safety is not aren't present profiles that to cast speed five cat dog
  meta: kind=partial | timestamp=1783299635.303224 | source=vosk | rms=493 | updated_at=1783299635.2816808 | frequency_hz=364.0
- [2026-07-06 09:00:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299635.5328605 | source=vosk | rms=310 | updated_at=1783299635.5318606 | frequency_hz=364.0
- [2026-07-06 09:00:35] operator / voice_transcript_partial / voice: cannot fire safety as cannot safety is no cannot fire safety is not aren't present profiles that to cast speed five cat dog ran
  meta: kind=partial | timestamp=1783299635.585807 | source=vosk | rms=310 | updated_at=1783299635.5318606 | frequency_hz=364.0
- [2026-07-06 09:00:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299636.0331774 | source=vosk | rms=310 | updated_at=1783299635.5318606 | frequency_hz=364.0
- [2026-07-06 09:00:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299638.032241 | source=vosk | rms=946 | updated_at=1783299638.032241 | frequency_hz=364.0
- [2026-07-06 09:00:38] operator / voice_transcript_partial / voice: cannot fire safety as cannot safety is no cannot fire safety is not aren't present profiles that to cast speed five cat dog rat
  meta: kind=partial | timestamp=1783299638.0688703 | source=vosk | rms=946 | updated_at=1783299638.032241 | frequency_hz=364.0
- [2026-07-06 09:00:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299638.5316525 | source=vosk | rms=946 | updated_at=1783299638.032241 | frequency_hz=364.0
- [2026-07-06 09:00:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299643.7830055 | source=vosk | rms=302 | updated_at=1783299643.7830055 | frequency_hz=364.0
- [2026-07-06 09:00:43] operator / voice_transcript_partial / voice: cannot fire safety as cannot safety is no cannot fire safety is not aren't present profiles that to cast speed five cat dog right track
  meta: kind=partial | timestamp=1783299643.8116214 | source=vosk | rms=302 | updated_at=1783299643.7830055 | frequency_hz=364.0
- [2026-07-06 09:00:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299644.0323856 | source=vosk | rms=723 | updated_at=1783299644.0323856 | frequency_hz=364.0
- [2026-07-06 09:00:44] operator / voice_transcript_partial / voice: cannot fire safety as cannot safety is no cannot fire safety is not aren't present profiles that to cast speed five cat dog ran track
  meta: kind=partial | timestamp=1783299644.0484989 | source=vosk | rms=723 | updated_at=1783299644.0323856 | frequency_hz=364.0
- [2026-07-06 09:00:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299644.2819595 | source=vosk | rms=735 | updated_at=1783299644.2819595 | frequency_hz=364.0
- [2026-07-06 09:00:44] operator / voice_transcript_final / voice: cannot fire safety as cannot safety is no cannot fire safety is not aren t rest profile that to cast speed five cat dog right track
  meta: kind=final | timestamp=1783299644.6760736 | source=final | rms=735 | updated_at=1783299644.2819595 | frequency_hz=364.0
- [2026-07-06 09:00:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299644.890903 | source=vosk | rms=735 | updated_at=1783299644.2819595 | frequency_hz=364.0
- [2026-07-06 09:00:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299646.022209 | source=vosk | rms=617 | updated_at=1783299646.022209 | frequency_hz=364.0
- [2026-07-06 09:00:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299648.0317848 | source=vosk | rms=667 | updated_at=1783299647.2827892 | frequency_hz=364.0
- [2026-07-06 09:00:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299648.5333755 | source=vosk | rms=462 | updated_at=1783299648.5333755 | frequency_hz=364.0
- [2026-07-06 09:00:51] operator / voice_transcript_partial / voice: cannot fire safety is not aren't
  meta: kind=partial | timestamp=1783299651.0525343 | source=vosk | rms=775 | updated_at=1783299651.0329225 | frequency_hz=364.0
- [2026-07-06 09:00:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299651.282047 | source=vosk | rms=679 | updated_at=1783299651.282047 | frequency_hz=364.0
- [2026-07-06 09:00:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299651.5335498 | source=vosk | rms=731 | updated_at=1783299651.5335498 | frequency_hz=364.0
- [2026-07-06 09:00:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299651.7952833 | source=vosk | rms=1205 | updated_at=1783299651.7952833 | frequency_hz=364.0
- [2026-07-06 09:00:52] operator / voice_transcript_final / voice: cannot fire safety is not art
  meta: kind=final | timestamp=1783299652.1453874 | source=final | rms=1205 | updated_at=1783299651.7952833 | frequency_hz=364.0
- [2026-07-06 09:00:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299652.279381 | source=vosk | rms=1205 | updated_at=1783299651.7952833 | frequency_hz=364.0
- [2026-07-06 09:00:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299652.279381 | source=vosk | rms=534 | updated_at=1783299652.279381 | frequency_hz=364.0
- [2026-07-06 09:00:56] operator / voice_transcript_partial / voice: cannot fight safety is not aren't
  meta: kind=partial | timestamp=1783299656.7448094 | source=vosk | rms=688 | updated_at=1783299656.7322936 | frequency_hz=364.0
- [2026-07-06 09:00:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299656.9889915 | source=vosk | rms=704 | updated_at=1783299656.9889915 | frequency_hz=364.0
- [2026-07-06 09:00:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299657.4821186 | source=vosk | rms=683 | updated_at=1783299657.4821186 | frequency_hz=364.0
- [2026-07-06 09:00:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299657.7322948 | source=vosk | rms=711 | updated_at=1783299657.7322948 | frequency_hz=364.0
- [2026-07-06 09:00:58] operator / voice_transcript_final / voice: cannot fight safety is not aren t
  meta: kind=final | timestamp=1783299658.3489673 | source=final | rms=711 | updated_at=1783299657.7322948 | frequency_hz=364.0
- [2026-07-06 09:00:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299658.4874852 | source=vosk | rms=711 | updated_at=1783299657.7322948 | frequency_hz=364.0
- [2026-07-06 09:00:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299658.9620235 | source=vosk | rms=683 | updated_at=1783299658.9620235 | frequency_hz=364.0
- [2026-07-06 09:01:00] operator / voice_transcript_partial / voice: cannot
  meta: kind=partial | timestamp=1783299660.734735 | source=vosk | rms=413 | updated_at=1783299660.712672 | frequency_hz=364.0
- [2026-07-06 09:01:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299660.962185 | source=vosk | rms=413 | updated_at=1783299660.712672 | frequency_hz=364.0
- [2026-07-06 09:01:00] operator / voice_transcript_partial / voice: cannot five
  meta: kind=partial | timestamp=1783299660.9765706 | source=vosk | rms=413 | updated_at=1783299660.712672 | frequency_hz=364.0
- [2026-07-06 09:01:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299661.2154715 | source=vosk | rms=657 | updated_at=1783299661.2154715 | frequency_hz=364.0
- [2026-07-06 09:01:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299661.462266 | source=vosk | rms=506 | updated_at=1783299661.462266 | frequency_hz=364.0
- [2026-07-06 09:01:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299661.7124193 | source=vosk | rms=534 | updated_at=1783299661.7124193 | frequency_hz=364.0
- [2026-07-06 09:01:01] operator / voice_transcript_partial / voice: cannot five safety is
  meta: kind=partial | timestamp=1783299661.7296875 | source=vosk | rms=534 | updated_at=1783299661.7124193 | frequency_hz=364.0
- [2026-07-06 09:01:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299661.9627547 | source=vosk | rms=534 | updated_at=1783299661.7124193 | frequency_hz=364.0
- [2026-07-06 09:01:01] operator / voice_transcript_partial / voice: cannot five safety is not
  meta: kind=partial | timestamp=1783299661.9810896 | source=vosk | rms=534 | updated_at=1783299661.7124193 | frequency_hz=364.0
- [2026-07-06 09:01:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299662.2156327 | source=vosk | rms=534 | updated_at=1783299661.7124193 | frequency_hz=364.0
- [2026-07-06 09:01:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299662.7145112 | source=vosk | rms=534 | updated_at=1783299661.7124193 | frequency_hz=364.0
- [2026-07-06 09:01:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299664.4806077 | source=vosk | rms=629 | updated_at=1783299664.4806077 | frequency_hz=364.0
- [2026-07-06 09:01:04] operator / voice_transcript_partial / voice: cannot five safety is not aren't
  meta: kind=partial | timestamp=1783299664.4920316 | source=vosk | rms=629 | updated_at=1783299664.4806077 | frequency_hz=364.0
- [2026-07-06 09:01:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299664.97393 | source=vosk | rms=629 | updated_at=1783299664.4806077 | frequency_hz=364.0
- [2026-07-06 09:01:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299665.973824 | source=vosk | rms=356 | updated_at=1783299665.973824 | frequency_hz=364.0
- [2026-07-06 09:01:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299666.22239 | source=vosk | rms=607 | updated_at=1783299666.22239 | frequency_hz=364.0
- [2026-07-06 09:01:06] operator / voice_transcript_partial / voice: cannot five safety is not art
  meta: kind=partial | timestamp=1783299666.2324283 | source=vosk | rms=607 | updated_at=1783299666.22239 | frequency_hz=364.0
- [2026-07-06 09:01:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299666.4722786 | source=vosk | rms=387 | updated_at=1783299666.4722786 | frequency_hz=364.0
- [2026-07-06 09:01:06] operator / voice_transcript_partial / voice: cannot five safety is not aren't
  meta: kind=partial | timestamp=1783299666.4858003 | source=vosk | rms=387 | updated_at=1783299666.4722786 | frequency_hz=364.0
- [2026-07-06 09:01:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299666.9724405 | source=vosk | rms=387 | updated_at=1783299666.4722786 | frequency_hz=364.0
- [2026-07-06 09:01:06] operator / voice_transcript_partial / voice: cannot five safety is not aren't cannot
  meta: kind=partial | timestamp=1783299666.9824557 | source=vosk | rms=387 | updated_at=1783299666.4722786 | frequency_hz=364.0
- [2026-07-06 09:01:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299667.2247267 | source=vosk | rms=647 | updated_at=1783299667.2247267 | frequency_hz=364.0
- [2026-07-06 09:01:07] operator / voice_transcript_partial / voice: cannot five safety is not aren't cannot fight for
  meta: kind=partial | timestamp=1783299667.2367933 | source=vosk | rms=647 | updated_at=1783299667.2247267 | frequency_hz=364.0
- [2026-07-06 09:01:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299667.4721196 | source=vosk | rms=623 | updated_at=1783299667.4721196 | frequency_hz=364.0
- [2026-07-06 09:01:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299667.7223835 | source=vosk | rms=407 | updated_at=1783299667.7223835 | frequency_hz=364.0
- [2026-07-06 09:01:07] operator / voice_transcript_partial / voice: cannot five safety is not aren't cannot fight for safety
  meta: kind=partial | timestamp=1783299667.738235 | source=vosk | rms=407 | updated_at=1783299667.7223835 | frequency_hz=364.0
- [2026-07-06 09:01:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299667.9735367 | source=vosk | rms=407 | updated_at=1783299667.7223835 | frequency_hz=364.0
- [2026-07-06 09:01:07] operator / voice_transcript_partial / voice: cannot five safety is not aren't cannot fight for safety is
  meta: kind=partial | timestamp=1783299667.9845698 | source=vosk | rms=407 | updated_at=1783299667.7223835 | frequency_hz=364.0
- [2026-07-06 09:01:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299668.2222126 | source=vosk | rms=407 | updated_at=1783299667.7223835 | frequency_hz=364.0
- [2026-07-06 09:01:08] operator / voice_transcript_partial / voice: cannot five safety is not aren't cannot fight for safety is not
  meta: kind=partial | timestamp=1783299668.2382715 | source=vosk | rms=407 | updated_at=1783299667.7223835 | frequency_hz=364.0
- [2026-07-06 09:01:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299668.722197 | source=vosk | rms=472 | updated_at=1783299668.722197 | frequency_hz=364.0
- [2026-07-06 09:01:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299668.9720714 | source=vosk | rms=681 | updated_at=1783299668.9720714 | frequency_hz=364.0
- [2026-07-06 09:01:08] operator / voice_transcript_partial / voice: cannot five safety is not aren't cannot fight for safety is not art
  meta: kind=partial | timestamp=1783299668.9820855 | source=vosk | rms=681 | updated_at=1783299668.9720714 | frequency_hz=364.0
- [2026-07-06 09:01:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299669.472451 | source=vosk | rms=392 | updated_at=1783299669.472451 | frequency_hz=364.0
- [2026-07-06 09:01:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299669.7222228 | source=vosk | rms=392 | updated_at=1783299669.472451 | frequency_hz=364.0
- [2026-07-06 09:01:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299670.2228582 | source=vosk | rms=460 | updated_at=1783299670.2228582 | frequency_hz=364.0
- [2026-07-06 09:01:10] operator / voice_transcript_final / voice: cannot five safety is not aren t cannot fight for safety is not art
  meta: kind=final | timestamp=1783299670.832841 | source=final | rms=460 | updated_at=1783299670.2228582 | frequency_hz=364.0
- [2026-07-06 09:01:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299670.9793468 | source=vosk | rms=460 | updated_at=1783299670.2228582 | frequency_hz=364.0
- [2026-07-06 09:01:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299670.9802663 | source=vosk | rms=707 | updated_at=1783299670.9802663 | frequency_hz=364.0
- [2026-07-06 09:01:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299672.52206 | source=vosk | rms=546 | updated_at=1783299672.0279346 | frequency_hz=364.0
- [2026-07-06 09:01:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299673.0232804 | source=vosk | rms=354 | updated_at=1783299673.0232804 | frequency_hz=364.0
- [2026-07-06 09:01:20] operator / voice_transcript_partial / voice: i cannot fire safety
  meta: kind=partial | timestamp=1783299680.5344753 | source=vosk | rms=814 | updated_at=1783299680.5227973 | frequency_hz=364.0
- [2026-07-06 09:01:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299680.7725475 | source=vosk | rms=439 | updated_at=1783299680.7725475 | frequency_hz=364.0
- [2026-07-06 09:01:20] operator / voice_transcript_partial / voice: i cannot fire safety is
  meta: kind=partial | timestamp=1783299680.7805727 | source=vosk | rms=439 | updated_at=1783299680.7725475 | frequency_hz=364.0
- [2026-07-06 09:01:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299681.2730503 | source=vosk | rms=439 | updated_at=1783299680.7725475 | frequency_hz=364.0
- [2026-07-06 09:01:21] operator / voice_transcript_partial / voice: i cannot fire safety is not always
  meta: kind=partial | timestamp=1783299681.30107 | source=vosk | rms=439 | updated_at=1783299680.7725475 | frequency_hz=364.0
- [2026-07-06 09:01:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299681.5253117 | source=vosk | rms=439 | updated_at=1783299680.7725475 | frequency_hz=364.0
- [2026-07-06 09:01:21] operator / voice_transcript_partial / voice: i cannot fire safety is not
  meta: kind=partial | timestamp=1783299681.5651598 | source=vosk | rms=439 | updated_at=1783299680.7725475 | frequency_hz=364.0
- [2026-07-06 09:01:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299681.7738419 | source=vosk | rms=471 | updated_at=1783299681.7738419 | frequency_hz=364.0
- [2026-07-06 09:01:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299682.0227966 | source=vosk | rms=430 | updated_at=1783299682.0227966 | frequency_hz=364.0
- [2026-07-06 09:01:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299682.532494 | source=vosk | rms=544 | updated_at=1783299682.532494 | frequency_hz=364.0
- [2026-07-06 09:01:22] operator / voice_transcript_final / voice: i cannot fire safety is not
  meta: kind=final | timestamp=1783299682.8200061 | source=final | rms=544 | updated_at=1783299682.532494 | frequency_hz=364.0
- [2026-07-06 09:01:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299682.946041 | source=vosk | rms=493 | updated_at=1783299682.946041 | frequency_hz=364.0
- [2026-07-06 09:01:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299683.5329385 | source=vosk | rms=493 | updated_at=1783299682.946041 | frequency_hz=364.0
- [2026-07-06 09:01:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299684.533807 | source=vosk | rms=547 | updated_at=1783299684.533807 | frequency_hz=364.0
- [2026-07-06 09:01:27] operator / voice_transcript_partial / voice: cannot fire safety is not aren't
  meta: kind=partial | timestamp=1783299687.073885 | source=vosk | rms=597 | updated_at=1783299687.032546 | frequency_hz=364.0
- [2026-07-06 09:01:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299687.2829518 | source=vosk | rms=456 | updated_at=1783299687.2829518 | frequency_hz=364.0
- [2026-07-06 09:01:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299687.5341384 | source=vosk | rms=490 | updated_at=1783299687.5341384 | frequency_hz=364.0
- [2026-07-06 09:01:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299687.78232 | source=vosk | rms=490 | updated_at=1783299687.5341384 | frequency_hz=364.0
- [2026-07-06 09:01:28] operator / voice_transcript_final / voice: cannot fire safety is not aren t
  meta: kind=final | timestamp=1783299688.091013 | source=final | rms=490 | updated_at=1783299687.5341384 | frequency_hz=364.0
- [2026-07-06 09:01:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299688.2175167 | source=vosk | rms=490 | updated_at=1783299687.5341384 | frequency_hz=364.0
- [2026-07-06 09:01:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299688.532316 | source=vosk | rms=490 | updated_at=1783299687.5341384 | frequency_hz=364.0
- [2026-07-06 09:01:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299689.535925 | source=vosk | rms=490 | updated_at=1783299687.5341384 | frequency_hz=364.0
- [2026-07-06 09:01:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299689.784246 | source=vosk | rms=490 | updated_at=1783299687.5341384 | frequency_hz=364.0
- [2026-07-06 09:01:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299693.797242 | source=vosk | rms=616 | updated_at=1783299693.0339196 | frequency_hz=364.0
- [2026-07-06 09:01:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299693.797242 | source=vosk | rms=502 | updated_at=1783299693.797242 | frequency_hz=364.0
- [2026-07-06 09:01:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299695.0330117 | source=vosk | rms=529 | updated_at=1783299694.5331547 | frequency_hz=364.0
- [2026-07-06 09:01:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299695.5326447 | source=vosk | rms=529 | updated_at=1783299694.5331547 | frequency_hz=364.0
- [2026-07-06 09:01:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299697.4853282 | source=vosk | rms=566 | updated_at=1783299696.7882705 | frequency_hz=364.0
- [2026-07-06 09:01:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299697.5330093 | source=vosk | rms=566 | updated_at=1783299696.7882705 | frequency_hz=364.0
- [2026-07-06 09:01:38] operator / voice_transcript_partial / voice: cannot fire safety is not worth
  meta: kind=partial | timestamp=1783299698.8162887 | source=vosk | rms=449 | updated_at=1783299698.5333674 | frequency_hz=364.0
- [2026-07-06 09:01:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299699.03293 | source=vosk | rms=449 | updated_at=1783299698.5333674 | frequency_hz=364.0
- [2026-07-06 09:01:39] operator / voice_transcript_partial / voice: cannot fire safety has not worked
  meta: kind=partial | timestamp=1783299699.0554862 | source=vosk | rms=449 | updated_at=1783299698.5333674 | frequency_hz=364.0
- [2026-07-06 09:01:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299699.532679 | source=vosk | rms=449 | updated_at=1783299698.5333674 | frequency_hz=364.0
- [2026-07-06 09:01:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299699.7845948 | source=vosk | rms=449 | updated_at=1783299698.5333674 | frequency_hz=364.0
- [2026-07-06 09:01:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299700.0351713 | source=vosk | rms=449 | updated_at=1783299698.5333674 | frequency_hz=364.0
- [2026-07-06 09:01:40] operator / voice_transcript_final / voice: cannot fight safety as not worked
  meta: kind=final | timestamp=1783299700.3561723 | source=final | rms=449 | updated_at=1783299698.5333674 | frequency_hz=364.0
- [2026-07-06 09:01:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299700.4829576 | source=vosk | rms=449 | updated_at=1783299698.5333674 | frequency_hz=364.0
- [2026-07-06 09:01:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299701.0328896 | source=vosk | rms=449 | updated_at=1783299698.5333674 | frequency_hz=364.0
- [2026-07-06 09:01:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299701.5329144 | source=vosk | rms=449 | updated_at=1783299698.5333674 | frequency_hz=364.0
- [2026-07-06 09:01:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299702.2842546 | source=vosk | rms=423 | updated_at=1783299702.2842546 | frequency_hz=364.0
- [2026-07-06 09:01:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299704.680723 | source=vosk | rms=667 | updated_at=1783299703.7820916 | frequency_hz=364.0
- [2026-07-06 09:01:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299704.680723 | source=vosk | rms=565 | updated_at=1783299704.680723 | frequency_hz=364.0
- [2026-07-06 09:01:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299705.2826781 | source=vosk | rms=718 | updated_at=1783299704.7063093 | frequency_hz=364.0
- [2026-07-06 09:01:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299707.1643271 | source=vosk | rms=718 | updated_at=1783299704.7063093 | frequency_hz=364.0
- [2026-07-06 09:01:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299711.9553967 | source=vosk | rms=456 | updated_at=1783299711.4133508 | frequency_hz=364.0
- [2026-07-06 09:01:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299711.955911 | source=vosk | rms=456 | updated_at=1783299711.955911 | frequency_hz=364.0
- [2026-07-06 09:01:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299712.955475 | source=vosk | rms=422 | updated_at=1783299712.2182841 | frequency_hz=364.0
- [2026-07-06 09:01:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299713.209625 | source=vosk | rms=423 | updated_at=1783299713.209625 | frequency_hz=364.0
- [2026-07-06 09:01:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299716.6400967 | source=vosk | rms=572 | updated_at=1783299716.2135496 | frequency_hz=364.0
- [2026-07-06 09:01:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299716.6400967 | source=vosk | rms=572 | updated_at=1783299716.2135496 | frequency_hz=364.0
- [2026-07-06 09:01:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299717.213244 | source=vosk | rms=572 | updated_at=1783299716.2135496 | frequency_hz=364.0
- [2026-07-06 09:01:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299718.7130976 | source=vosk | rms=572 | updated_at=1783299716.2135496 | frequency_hz=364.0
- [2026-07-06 09:01:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299719.4632645 | source=vosk | rms=438 | updated_at=1783299718.9633713 | frequency_hz=364.0
- [2026-07-06 09:01:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299719.9628866 | source=vosk | rms=438 | updated_at=1783299718.9633713 | frequency_hz=364.0
- [2026-07-06 09:02:02] operator / voice_transcript_partial / voice: cannot fire safety is not armed cannot fire safety is
  meta: kind=partial | timestamp=1783299722.4769099 | source=vosk | rms=560 | updated_at=1783299722.2129672 | frequency_hz=364.0
- [2026-07-06 09:02:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299722.7138493 | source=vosk | rms=560 | updated_at=1783299722.2129672 | frequency_hz=364.0
- [2026-07-06 09:02:02] operator / voice_transcript_partial / voice: cannot fire safety is not armed cannot fire safety is not
  meta: kind=partial | timestamp=1783299722.725891 | source=vosk | rms=560 | updated_at=1783299722.2129672 | frequency_hz=364.0
- [2026-07-06 09:02:03] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299723.2138486 | source=vosk | rms=560 | updated_at=1783299722.2129672 | frequency_hz=364.0
- [2026-07-06 09:02:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299723.463002 | source=vosk | rms=560 | updated_at=1783299722.2129672 | frequency_hz=364.0
- [2026-07-06 09:02:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299723.7147746 | source=vosk | rms=560 | updated_at=1783299722.2129672 | frequency_hz=364.0
- [2026-07-06 09:02:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299724.215086 | source=vosk | rms=464 | updated_at=1783299724.215086 | frequency_hz=364.0
- [2026-07-06 09:02:05] operator / voice_transcript_final / voice: cannot fire safety is not armed cannot fire safety is not
  meta: kind=final | timestamp=1783299725.13111 | source=final | rms=464 | updated_at=1783299724.215086 | frequency_hz=364.0
- [2026-07-06 09:02:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299725.27388 | source=vosk | rms=464 | updated_at=1783299724.215086 | frequency_hz=364.0
- [2026-07-06 09:02:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299725.27388 | source=vosk | rms=563 | updated_at=1783299725.27388 | frequency_hz=364.0
- [2026-07-06 09:02:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299726.2130067 | source=vosk | rms=490 | updated_at=1783299725.7145243 | frequency_hz=364.0
- [2026-07-06 09:02:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299726.7135735 | source=vosk | rms=783 | updated_at=1783299726.7135735 | frequency_hz=364.0
- [2026-07-06 09:02:07] operator / voice_transcript_partial / voice: cannot
  meta: kind=partial | timestamp=1783299727.2271676 | source=vosk | rms=474 | updated_at=1783299726.963266 | frequency_hz=364.0
- [2026-07-06 09:02:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299727.7135093 | source=vosk | rms=640 | updated_at=1783299727.7135093 | frequency_hz=364.0
- [2026-07-06 09:02:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299727.9639304 | source=vosk | rms=479 | updated_at=1783299727.9639304 | frequency_hz=364.0
- [2026-07-06 09:02:07] operator / voice_transcript_partial / voice: cannot fire
  meta: kind=partial | timestamp=1783299727.9790425 | source=vosk | rms=479 | updated_at=1783299727.9639304 | frequency_hz=364.0
- [2026-07-06 09:02:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299728.213831 | source=vosk | rms=562 | updated_at=1783299728.213831 | frequency_hz=364.0
- [2026-07-06 09:02:08] operator / voice_transcript_partial / voice: cannot fire safety
  meta: kind=partial | timestamp=1783299728.22239 | source=vosk | rms=562 | updated_at=1783299728.213831 | frequency_hz=364.0
- [2026-07-06 09:02:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299728.4634876 | source=vosk | rms=562 | updated_at=1783299728.213831 | frequency_hz=364.0
- [2026-07-06 09:02:08] operator / voice_transcript_partial / voice: cannot fire safety is
  meta: kind=partial | timestamp=1783299728.4704962 | source=vosk | rms=562 | updated_at=1783299728.213831 | frequency_hz=364.0
- [2026-07-06 09:02:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299728.96303 | source=vosk | rms=562 | updated_at=1783299728.213831 | frequency_hz=364.0
- [2026-07-06 09:02:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299730.463766 | source=vosk | rms=562 | updated_at=1783299728.213831 | frequency_hz=364.0
- [2026-07-06 09:02:10] operator / voice_transcript_partial / voice: cannot fire safety is not
  meta: kind=partial | timestamp=1783299730.4737816 | source=vosk | rms=562 | updated_at=1783299728.213831 | frequency_hz=364.0
- [2026-07-06 09:02:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299730.9639592 | source=vosk | rms=392 | updated_at=1783299730.9639592 | frequency_hz=364.0
- [2026-07-06 09:02:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299731.4638844 | source=vosk | rms=392 | updated_at=1783299730.9639592 | frequency_hz=364.0
- [2026-07-06 09:02:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299731.7147071 | source=vosk | rms=391 | updated_at=1783299731.7147071 | frequency_hz=364.0
- [2026-07-06 09:02:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299732.4632611 | source=vosk | rms=606 | updated_at=1783299731.9631245 | frequency_hz=364.0
- [2026-07-06 09:02:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299732.7139146 | source=vosk | rms=564 | updated_at=1783299732.7139146 | frequency_hz=364.0
- [2026-07-06 09:02:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299734.701739 | source=vosk | rms=507 | updated_at=1783299733.9634566 | frequency_hz=364.0
- [2026-07-06 09:02:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299734.701739 | source=vosk | rms=573 | updated_at=1783299734.701739 | frequency_hz=364.0
- [2026-07-06 09:02:14] operator / voice_transcript_partial / voice: cannot fire safety is not only
  meta: kind=partial | timestamp=1783299734.974917 | source=vosk | rms=510 | updated_at=1783299734.9639013 | frequency_hz=364.0
- [2026-07-06 09:02:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299735.2139697 | source=vosk | rms=574 | updated_at=1783299735.2139697 | frequency_hz=364.0
- [2026-07-06 09:02:15] operator / voice_transcript_partial / voice: cannot fire safety is not on
  meta: kind=partial | timestamp=1783299735.2843254 | source=vosk | rms=574 | updated_at=1783299735.2139697 | frequency_hz=364.0
- [2026-07-06 09:02:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299735.463315 | source=vosk | rms=563 | updated_at=1783299735.463315 | frequency_hz=364.0
- [2026-07-06 09:02:15] operator / voice_transcript_final / voice: cannot fire safety is not art
  meta: kind=final | timestamp=1783299735.9115574 | source=final | rms=563 | updated_at=1783299735.463315 | frequency_hz=364.0
- [2026-07-06 09:02:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299736.0586915 | source=vosk | rms=563 | updated_at=1783299735.463315 | frequency_hz=364.0
- [2026-07-06 09:02:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299736.0586915 | source=vosk | rms=555 | updated_at=1783299736.0586915 | frequency_hz=364.0
- [2026-07-06 09:02:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299737.1218889 | source=vosk | rms=555 | updated_at=1783299736.0586915 | frequency_hz=364.0
- [2026-07-06 09:02:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299737.3549654 | source=vosk | rms=536 | updated_at=1783299737.3549654 | frequency_hz=364.0
- [2026-07-06 09:02:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299742.1102817 | source=vosk | rms=394 | updated_at=1783299741.606789 | frequency_hz=364.0
- [2026-07-06 09:02:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299743.1033835 | source=vosk | rms=394 | updated_at=1783299741.606789 | frequency_hz=364.0
- [2026-07-06 09:02:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299745.6080854 | source=vosk | rms=484 | updated_at=1783299744.8533335 | frequency_hz=364.0
- [2026-07-06 09:02:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299745.6080854 | source=vosk | rms=550 | updated_at=1783299745.6080854 | frequency_hz=364.0
- [2026-07-06 09:02:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299746.7797058 | source=vosk | rms=537 | updated_at=1783299746.1035788 | frequency_hz=364.0
- [2026-07-06 09:02:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299746.7807088 | source=vosk | rms=456 | updated_at=1783299746.7807088 | frequency_hz=364.0
- [2026-07-06 09:02:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299747.353942 | source=vosk | rms=571 | updated_at=1783299746.7932196 | frequency_hz=364.0
- [2026-07-06 09:02:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299747.6043177 | source=vosk | rms=494 | updated_at=1783299747.6043177 | frequency_hz=364.0
- [2026-07-06 09:02:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299749.1578712 | source=vosk | rms=533 | updated_at=1783299747.9510064 | frequency_hz=364.0
- [2026-07-06 09:02:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299749.4041061 | source=vosk | rms=533 | updated_at=1783299747.9510064 | frequency_hz=364.0
- [2026-07-06 09:02:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299750.4044776 | source=vosk | rms=483 | updated_at=1783299749.9039533 | frequency_hz=364.0
- [2026-07-06 09:02:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299750.65422 | source=vosk | rms=665 | updated_at=1783299750.65422 | frequency_hz=364.0
- [2026-07-06 09:02:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299753.153622 | source=vosk | rms=626 | updated_at=1783299752.6534286 | frequency_hz=364.0
- [2026-07-06 09:02:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299753.9040816 | source=vosk | rms=495 | updated_at=1783299753.9040816 | frequency_hz=364.0
- [2026-07-06 09:02:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299754.6553237 | source=vosk | rms=542 | updated_at=1783299754.1537528 | frequency_hz=364.0
- [2026-07-06 09:02:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299754.9043438 | source=vosk | rms=602 | updated_at=1783299754.9043438 | frequency_hz=364.0
- [2026-07-06 09:02:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299757.6261966 | source=vosk | rms=553 | updated_at=1783299757.1547315 | frequency_hz=364.0
- [2026-07-06 09:02:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299757.6261966 | source=vosk | rms=553 | updated_at=1783299757.1547315 | frequency_hz=364.0
- [2026-07-06 09:02:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299758.1607716 | source=vosk | rms=553 | updated_at=1783299757.1547315 | frequency_hz=364.0
- [2026-07-06 09:02:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299758.4040117 | source=vosk | rms=553 | updated_at=1783299757.1547315 | frequency_hz=364.0
- [2026-07-06 09:02:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299758.9201517 | source=vosk | rms=553 | updated_at=1783299757.1547315 | frequency_hz=364.0
- [2026-07-06 09:02:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299758.9201517 | source=vosk | rms=530 | updated_at=1783299758.9201517 | frequency_hz=364.0
- [2026-07-06 09:02:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299759.4042714 | source=vosk | rms=530 | updated_at=1783299758.9201517 | frequency_hz=364.0
- [2026-07-06 09:02:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299759.9038455 | source=vosk | rms=530 | updated_at=1783299758.9201517 | frequency_hz=364.0
- [2026-07-06 09:02:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299760.9035811 | source=vosk | rms=567 | updated_at=1783299760.153729 | frequency_hz=364.0
- [2026-07-06 09:02:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299761.653659 | source=vosk | rms=449 | updated_at=1783299761.653659 | frequency_hz=364.0
- [2026-07-06 09:02:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299764.9084067 | source=vosk | rms=551 | updated_at=1783299764.15458 | frequency_hz=364.0
- [2026-07-06 09:02:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299766.4051788 | source=vosk | rms=532 | updated_at=1783299766.4051788 | frequency_hz=364.0
- [2026-07-06 09:02:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299770.9042413 | source=vosk | rms=585 | updated_at=1783299770.1543372 | frequency_hz=364.0
- [2026-07-06 09:02:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299771.1545246 | source=vosk | rms=472 | updated_at=1783299771.1545246 | frequency_hz=364.0
- [2026-07-06 09:02:55] operator / voice_transcript_partial / voice: i cannot buy safety is not
  meta: kind=partial | timestamp=1783299775.6709828 | source=vosk | rms=654 | updated_at=1783299775.1540563 | frequency_hz=364.0
- [2026-07-06 09:02:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299775.9041033 | source=vosk | rms=654 | updated_at=1783299775.1540563 | frequency_hz=364.0
- [2026-07-06 09:02:55] operator / voice_transcript_partial / voice: i cannot buy safety is not our
  meta: kind=partial | timestamp=1783299775.9136317 | source=vosk | rms=654 | updated_at=1783299775.1540563 | frequency_hz=364.0
- [2026-07-06 09:02:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299776.1542366 | source=vosk | rms=531 | updated_at=1783299776.1542366 | frequency_hz=364.0
- [2026-07-06 09:02:56] operator / voice_transcript_partial / voice: i cannot buy safety is not
  meta: kind=partial | timestamp=1783299776.1768556 | source=vosk | rms=531 | updated_at=1783299776.1542366 | frequency_hz=364.0
- [2026-07-06 09:02:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299776.4092348 | source=vosk | rms=496 | updated_at=1783299776.4092348 | frequency_hz=364.0
- [2026-07-06 09:02:56] operator / voice_transcript_partial / voice: i cannot buy safety is not or
  meta: kind=partial | timestamp=1783299776.4207838 | source=vosk | rms=496 | updated_at=1783299776.4092348 | frequency_hz=364.0
- [2026-07-06 09:02:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299776.991149 | source=vosk | rms=496 | updated_at=1783299776.4092348 | frequency_hz=364.0
- [2026-07-06 09:02:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299777.2355032 | source=vosk | rms=449 | updated_at=1783299777.2355032 | frequency_hz=364.0
- [2026-07-06 09:02:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299777.7363563 | source=vosk | rms=449 | updated_at=1783299777.2355032 | frequency_hz=364.0
- [2026-07-06 09:02:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299778.733897 | source=vosk | rms=492 | updated_at=1783299778.733897 | frequency_hz=364.0
- [2026-07-06 09:03:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299784.9859169 | source=vosk | rms=525 | updated_at=1783299784.4860268 | frequency_hz=364.0
- [2026-07-06 09:03:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299785.2359698 | source=vosk | rms=525 | updated_at=1783299784.4860268 | frequency_hz=364.0
- [2026-07-06 09:03:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299787.8728058 | source=vosk | rms=690 | updated_at=1783299786.9844675 | frequency_hz=364.0
- [2026-07-06 09:03:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299787.8728058 | source=vosk | rms=511 | updated_at=1783299787.8728058 | frequency_hz=364.0
- [2026-07-06 09:03:07] operator / voice_transcript_partial / voice: i cannot find
  meta: kind=partial | timestamp=1783299787.8903906 | source=vosk | rms=511 | updated_at=1783299787.8728058 | frequency_hz=364.0
- [2026-07-06 09:03:07] operator / voice_transcript_partial / voice: i cannot fire safety
  meta: kind=partial | timestamp=1783299787.901414 | source=vosk | rms=538 | updated_at=1783299787.8903906 | frequency_hz=364.0
- [2026-07-06 09:03:07] operator / voice_transcript_partial / voice: i cannot fire safety is
  meta: kind=partial | timestamp=1783299787.9140637 | source=vosk | rms=538 | updated_at=1783299787.8903906 | frequency_hz=364.0
- [2026-07-06 09:03:08] operator / voice_transcript_partial / voice: i cannot fire safety is not
  meta: kind=partial | timestamp=1783299788.0190237 | source=vosk | rms=538 | updated_at=1783299787.8903906 | frequency_hz=364.0
- [2026-07-06 09:03:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299788.2346308 | source=vosk | rms=409 | updated_at=1783299788.2346308 | frequency_hz=364.0
- [2026-07-06 09:03:08] operator / voice_transcript_partial / voice: i cannot fire safety is not aren't
  meta: kind=partial | timestamp=1783299788.2556672 | source=vosk | rms=409 | updated_at=1783299788.2346308 | frequency_hz=364.0
- [2026-07-06 09:03:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299788.4856515 | source=vosk | rms=558 | updated_at=1783299788.4856515 | frequency_hz=364.0
- [2026-07-06 09:03:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299788.7342036 | source=vosk | rms=558 | updated_at=1783299788.4856515 | frequency_hz=364.0
- [2026-07-06 09:03:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299789.2343824 | source=vosk | rms=558 | updated_at=1783299788.4856515 | frequency_hz=364.0
- [2026-07-06 09:03:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299790.4841914 | source=vosk | rms=522 | updated_at=1783299790.4841914 | frequency_hz=364.0
- [2026-07-06 09:03:10] operator / voice_transcript_final / voice: i cannot fire safety is not ours
  meta: kind=final | timestamp=1783299790.8019307 | source=final | rms=522 | updated_at=1783299790.4841914 | frequency_hz=364.0
- [2026-07-06 09:03:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299790.9518852 | source=vosk | rms=522 | updated_at=1783299790.4841914 | frequency_hz=364.0
- [2026-07-06 09:03:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299790.9518852 | source=vosk | rms=560 | updated_at=1783299790.9518852 | frequency_hz=364.0
- [2026-07-06 09:03:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299791.485778 | source=vosk | rms=560 | updated_at=1783299790.9518852 | frequency_hz=364.0
- [2026-07-06 09:03:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299791.734169 | source=vosk | rms=1017 | updated_at=1783299791.734169 | frequency_hz=364.0
- [2026-07-06 09:03:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299793.2341747 | source=vosk | rms=401 | updated_at=1783299792.734365 | frequency_hz=364.0
- [2026-07-06 09:03:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299793.4851208 | source=vosk | rms=665 | updated_at=1783299793.4851208 | frequency_hz=364.0
- [2026-07-06 09:03:13] operator / voice_transcript_partial / voice: cannot
  meta: kind=partial | timestamp=1783299793.4956357 | source=vosk | rms=665 | updated_at=1783299793.4851208 | frequency_hz=364.0
- [2026-07-06 09:03:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299793.7347383 | source=vosk | rms=492 | updated_at=1783299793.7347383 | frequency_hz=364.0
- [2026-07-06 09:03:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299793.9850652 | source=vosk | rms=548 | updated_at=1783299793.9850652 | frequency_hz=364.0
- [2026-07-06 09:03:13] operator / voice_transcript_partial / voice: cannot for safety
  meta: kind=partial | timestamp=1783299793.994076 | source=vosk | rms=548 | updated_at=1783299793.9850652 | frequency_hz=364.0
- [2026-07-06 09:03:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299794.235142 | source=vosk | rms=548 | updated_at=1783299793.9850652 | frequency_hz=364.0
- [2026-07-06 09:03:14] operator / voice_transcript_partial / voice: cannot for safety is
  meta: kind=partial | timestamp=1783299794.2437284 | source=vosk | rms=548 | updated_at=1783299793.9850652 | frequency_hz=364.0
- [2026-07-06 09:03:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299794.7345119 | source=vosk | rms=548 | updated_at=1783299793.9850652 | frequency_hz=364.0
- [2026-07-06 09:03:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299796.234408 | source=vosk | rms=548 | updated_at=1783299793.9850652 | frequency_hz=364.0
- [2026-07-06 09:03:16] operator / voice_transcript_partial / voice: cannot for safety is not
  meta: kind=partial | timestamp=1783299796.2444189 | source=vosk | rms=548 | updated_at=1783299793.9850652 | frequency_hz=364.0
- [2026-07-06 09:03:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299796.7346537 | source=vosk | rms=503 | updated_at=1783299796.7346537 | frequency_hz=364.0
- [2026-07-06 09:03:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299797.4846005 | source=vosk | rms=669 | updated_at=1783299796.9850233 | frequency_hz=364.0
- [2026-07-06 09:03:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299797.7346916 | source=vosk | rms=560 | updated_at=1783299797.7346916 | frequency_hz=364.0
- [2026-07-06 09:03:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299798.7971916 | source=vosk | rms=443 | updated_at=1783299797.984567 | frequency_hz=364.0
- [2026-07-06 09:03:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299798.7971916 | source=vosk | rms=642 | updated_at=1783299798.7971916 | frequency_hz=364.0
- [2026-07-06 09:03:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299799.9509501 | source=vosk | rms=580 | updated_at=1783299799.2349205 | frequency_hz=364.0
- [2026-07-06 09:03:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299799.9509501 | source=vosk | rms=591 | updated_at=1783299799.9509501 | frequency_hz=364.0
- [2026-07-06 09:03:19] operator / voice_transcript_partial / voice: i cannot fight
  meta: kind=partial | timestamp=1783299799.9615037 | source=vosk | rms=591 | updated_at=1783299799.9509501 | frequency_hz=364.0
- [2026-07-06 09:03:19] operator / voice_transcript_partial / voice: i cannot fire safety is
  meta: kind=partial | timestamp=1783299799.9750185 | source=vosk | rms=591 | updated_at=1783299799.9509501 | frequency_hz=364.0
- [2026-07-06 09:03:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299800.235277 | source=vosk | rms=434 | updated_at=1783299800.235277 | frequency_hz=364.0
- [2026-07-06 09:03:20] operator / voice_transcript_partial / voice: i cannot fire safety is not
  meta: kind=partial | timestamp=1783299800.253266 | source=vosk | rms=434 | updated_at=1783299800.235277 | frequency_hz=364.0
- [2026-07-06 09:03:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299800.4860177 | source=vosk | rms=898 | updated_at=1783299800.4860177 | frequency_hz=364.0
- [2026-07-06 09:03:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299800.7352407 | source=vosk | rms=519 | updated_at=1783299800.7352407 | frequency_hz=364.0
- [2026-07-06 09:03:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299800.9850469 | source=vosk | rms=519 | updated_at=1783299800.7352407 | frequency_hz=364.0
- [2026-07-06 09:03:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299801.4845316 | source=vosk | rms=519 | updated_at=1783299800.7352407 | frequency_hz=364.0
- [2026-07-06 09:03:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299801.734642 | source=vosk | rms=1202 | updated_at=1783299801.734642 | frequency_hz=364.0
- [2026-07-06 09:03:22] operator / voice_transcript_final / voice: i cannot fire safety is not
  meta: kind=final | timestamp=1783299802.36757 | source=final | rms=1202 | updated_at=1783299801.734642 | frequency_hz=364.0
- [2026-07-06 09:03:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299802.5734272 | source=vosk | rms=1202 | updated_at=1783299801.734642 | frequency_hz=364.0
- [2026-07-06 09:03:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299802.5734272 | source=vosk | rms=1201 | updated_at=1783299802.5734272 | frequency_hz=364.0
- [2026-07-06 09:03:23] operator / voice_transcript_partial / voice: earlier
  meta: kind=partial | timestamp=1783299803.7763646 | source=vosk | rms=3438 | updated_at=1783299803.7413914 | frequency_hz=246.4
- [2026-07-06 09:03:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299803.9857612 | source=vosk | rms=1201 | updated_at=1783299803.9842372 | frequency_hz=205.7
- [2026-07-06 09:03:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299804.2345145 | source=vosk | rms=1200 | updated_at=1783299804.2345145 | frequency_hz=177.8
- [2026-07-06 09:03:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299804.484693 | source=vosk | rms=1147 | updated_at=1783299804.484693 | frequency_hz=244.4
- [2026-07-06 09:03:24] operator / voice_transcript_final / voice: earlier
  meta: kind=final | timestamp=1783299804.7079773 | source=final | rms=1147 | updated_at=1783299804.484693 | frequency_hz=244.4
- [2026-07-06 09:03:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299804.7797012 | source=vosk | rms=508 | updated_at=1783299804.7797012 | frequency_hz=244.4
- [2026-07-06 09:03:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299805.2346008 | source=vosk | rms=508 | updated_at=1783299804.7797012 | frequency_hz=244.4
- [2026-07-06 09:03:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299806.7345836 | source=vosk | rms=508 | updated_at=1783299804.7797012 | frequency_hz=244.4
- [2026-07-06 09:03:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299807.2349849 | source=vosk | rms=508 | updated_at=1783299804.7797012 | frequency_hz=244.4
- [2026-07-06 09:03:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299808.234507 | source=vosk | rms=1108 | updated_at=1783299808.234507 | frequency_hz=144.0
- [2026-07-06 09:03:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299810.8712175 | source=vosk | rms=551 | updated_at=1783299809.9851575 | frequency_hz=141.9
- [2026-07-06 09:03:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299810.8712175 | source=vosk | rms=551 | updated_at=1783299809.9851575 | frequency_hz=141.9
- [2026-07-06 09:03:30] operator / voice_transcript_partial / voice: cannot safety is
  meta: kind=partial | timestamp=1783299810.8863347 | source=vosk | rms=551 | updated_at=1783299809.9851575 | frequency_hz=141.9
- [2026-07-06 09:03:30] operator / voice_transcript_partial / voice: cannot safety is not
  meta: kind=partial | timestamp=1783299810.8963556 | source=vosk | rms=551 | updated_at=1783299809.9851575 | frequency_hz=141.9
- [2026-07-06 09:03:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299811.48529 | source=vosk | rms=551 | updated_at=1783299809.9851575 | frequency_hz=141.9
- [2026-07-06 09:03:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299811.7342927 | source=vosk | rms=4933 | updated_at=1783299811.7342927 | frequency_hz=141.9
- [2026-07-06 09:03:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299811.9849117 | source=vosk | rms=9948 | updated_at=1783299811.9849117 | frequency_hz=141.9
- [2026-07-06 09:03:31] operator / voice_transcript_partial / voice: cannot safety is not be
  meta: kind=partial | timestamp=1783299811.997431 | source=vosk | rms=9948 | updated_at=1783299811.9849117 | frequency_hz=141.9
- [2026-07-06 09:03:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299812.2349558 | source=vosk | rms=1201 | updated_at=1783299812.2349558 | frequency_hz=209.8
- [2026-07-06 09:03:32] operator / voice_transcript_partial / voice: cannot safety is not
  meta: kind=partial | timestamp=1783299812.2685897 | source=vosk | rms=1201 | updated_at=1783299812.2349558 | frequency_hz=209.8
- [2026-07-06 09:03:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299812.4860253 | source=vosk | rms=7073 | updated_at=1783299812.4860253 | frequency_hz=209.8
- [2026-07-06 09:03:32] operator / voice_transcript_partial / voice: cannot safety is not on you you
  meta: kind=partial | timestamp=1783299812.50238 | source=vosk | rms=7073 | updated_at=1783299812.4860253 | frequency_hz=209.8
- [2026-07-06 09:03:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299812.7349064 | source=vosk | rms=11804 | updated_at=1783299812.7349064 | frequency_hz=209.8
- [2026-07-06 09:03:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299812.9847 | source=vosk | rms=7212 | updated_at=1783299812.9847 | frequency_hz=209.8
- [2026-07-06 09:03:33] operator / voice_transcript_partial / voice: cannot safety is not believe in ghosts
  meta: kind=partial | timestamp=1783299813.059009 | source=vosk | rms=7212 | updated_at=1783299812.9847 | frequency_hz=209.8
- [2026-07-06 09:03:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299813.235296 | source=vosk | rms=6874 | updated_at=1783299813.235296 | frequency_hz=209.8
- [2026-07-06 09:03:33] operator / voice_transcript_partial / voice: cannot safety is not on you you go smoke
  meta: kind=partial | timestamp=1783299813.2678573 | source=vosk | rms=6874 | updated_at=1783299813.235296 | frequency_hz=209.8
- [2026-07-06 09:03:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299813.4850588 | source=vosk | rms=4920 | updated_at=1783299813.4850588 | frequency_hz=209.8
- [2026-07-06 09:03:33] operator / voice_transcript_partial / voice: cannot safety is not believe in ghosts watch it
  meta: kind=partial | timestamp=1783299813.5696557 | source=vosk | rms=4920 | updated_at=1783299813.4850588 | frequency_hz=209.8
- [2026-07-06 09:03:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299813.7351024 | source=vosk | rms=1408 | updated_at=1783299813.7351024 | frequency_hz=205.7
- [2026-07-06 09:03:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299813.9850292 | source=vosk | rms=774 | updated_at=1783299813.9850292 | frequency_hz=252.0
- [2026-07-06 09:03:34] operator / voice_transcript_partial / voice: cannot safety is not believe in ghosts watched it three
  meta: kind=partial | timestamp=1783299814.0316415 | source=vosk | rms=774 | updated_at=1783299813.9850292 | frequency_hz=252.0
- [2026-07-06 09:03:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299814.2364836 | source=vosk | rms=819 | updated_at=1783299814.2364836 | frequency_hz=214.2
- [2026-07-06 09:03:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299814.484682 | source=vosk | rms=1200 | updated_at=1783299814.484682 | frequency_hz=214.2
- [2026-07-06 09:03:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299814.7354949 | source=vosk | rms=1201 | updated_at=1783299814.7354949 | frequency_hz=214.2
- [2026-07-06 09:03:35] operator / voice_transcript_final / voice: cannot safety is not you you ghosts ports it three
  meta: kind=final | timestamp=1783299815.03548 | source=final | rms=1201 | updated_at=1783299814.7354949 | frequency_hz=214.2
- [2026-07-06 09:03:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299815.1440983 | source=vosk | rms=1201 | updated_at=1783299815.1440983 | frequency_hz=214.2
- [2026-07-06 09:03:36] operator / voice_transcript_partial / voice: cannot
  meta: kind=partial | timestamp=1783299816.494955 | source=vosk | rms=710 | updated_at=1783299816.2354739 | frequency_hz=214.2
- [2026-07-06 09:03:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299816.734957 | source=vosk | rms=789 | updated_at=1783299816.734957 | frequency_hz=214.2
- [2026-07-06 09:03:36] operator / voice_transcript_partial / voice: cannot fire
  meta: kind=partial | timestamp=1783299816.7524853 | source=vosk | rms=789 | updated_at=1783299816.734957 | frequency_hz=214.2
- [2026-07-06 09:03:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299816.9851174 | source=vosk | rms=598 | updated_at=1783299816.9851174 | frequency_hz=214.2
- [2026-07-06 09:03:36] operator / voice_transcript_partial / voice: cannot fire safety
  meta: kind=partial | timestamp=1783299816.9971316 | source=vosk | rms=598 | updated_at=1783299816.9851174 | frequency_hz=214.2
- [2026-07-06 09:03:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299817.2350671 | source=vosk | rms=1202 | updated_at=1783299817.2350671 | frequency_hz=214.2
- [2026-07-06 09:03:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299817.486337 | source=vosk | rms=1200 | updated_at=1783299817.486337 | frequency_hz=286.2
- [2026-07-06 09:03:37] operator / voice_transcript_partial / voice: cannot fire safety is
  meta: kind=partial | timestamp=1783299817.495348 | source=vosk | rms=1200 | updated_at=1783299817.486337 | frequency_hz=286.2
- [2026-07-06 09:03:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299817.735478 | source=vosk | rms=1199 | updated_at=1783299817.735478 | frequency_hz=326.7
- [2026-07-06 09:03:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299817.9902797 | source=vosk | rms=1199 | updated_at=1783299817.735478 | frequency_hz=326.7
- [2026-07-06 09:03:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299818.2414289 | source=vosk | rms=4532 | updated_at=1783299818.2409146 | frequency_hz=326.7
- [2026-07-06 09:03:38] operator / voice_transcript_final / voice: cannot fire safety is
  meta: kind=final | timestamp=1783299818.6132836 | source=final | rms=4532 | updated_at=1783299818.2409146 | frequency_hz=326.7
- [2026-07-06 09:03:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299818.7743132 | source=vosk | rms=4532 | updated_at=1783299818.2409146 | frequency_hz=326.7
- [2026-07-06 09:03:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783299818.7743132 | source=vosk | rms=3353 | updated_at=1783299818.7743132 | frequency_hz=326.7
- [2026-07-06 09:03:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783299820.234623 | source=vosk | rms=3353 | updated_at=1783299818.7743132 | frequency_hz=326.7

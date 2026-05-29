# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-06 20:32:27
- Entries: 285
- Roles: {'assistant': 10, 'system': 1, 'operator': 274}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 1, 'voice_transcript_final': 42, 'voice_transcript_partial': 220, 'voice_command': 12, 'spoken_confirmation': 8}
- Channels: {'text': 2, 'voice': 283}
- Latest operator request: give on stay what
- Latest assistant message: I am here. Ask your question.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-06 20:20:22] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-06 20:20:22] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-06 20:20:24] system / voice_status / voice: listening
  meta: kind=status | timestamp=1778070024.4837334 | source=vosk
- [2026-05-06 20:20:34] operator / voice_transcript_final / voice: hey
  meta: kind=final | timestamp=1778070034.3490555 | source=final | frequency_hz=416.0 | rms=310 | updated_at=1778070032.7644858
- [2026-05-06 20:21:19] operator / voice_transcript_final / voice: hey
  meta: kind=final | timestamp=1778070079.6813195 | source=final | frequency_hz=302.2 | rms=292 | updated_at=1778070079.5780702
- [2026-05-06 20:21:50] operator / voice_transcript_final / voice: be
  meta: kind=final | timestamp=1778070110.935238 | source=final | frequency_hz=314.9 | rms=289 | updated_at=1778070110.8296387
- [2026-05-06 20:24:00] operator / voice_transcript_partial / voice: pir
  meta: kind=partial | timestamp=1778070240.2910945 | source=vosk | frequency_hz=340.0 | rms=309 | updated_at=1778070240.2845895
- [2026-05-06 20:24:01] operator / voice_transcript_final / voice: pir
  meta: kind=final | timestamp=1778070241.2764783 | source=final | frequency_hz=357.6 | rms=297 | updated_at=1778070241.0363495
- [2026-05-06 20:24:02] operator / voice_transcript_partial / voice: greeting
  meta: kind=partial | timestamp=1778070242.2936807 | source=vosk | frequency_hz=358.4 | rms=288 | updated_at=1778070241.28964
- [2026-05-06 20:24:03] operator / voice_transcript_partial / voice: reporting
  meta: kind=partial | timestamp=1778070243.5524495 | source=vosk | frequency_hz=380.0 | rms=301 | updated_at=1778070243.5349252
- [2026-05-06 20:24:05] operator / voice_transcript_partial / voice: window shortcuts
  meta: kind=partial | timestamp=1778070245.2917411 | source=vosk | frequency_hz=380.0 | rms=301 | updated_at=1778070243.5349252
- [2026-05-06 20:24:05] operator / voice_transcript_partial / voice: window what is
  meta: kind=partial | timestamp=1778070245.546129 | source=vosk | frequency_hz=380.0 | rms=301 | updated_at=1778070243.5349252
- [2026-05-06 20:24:05] operator / voice_transcript_partial / voice: window what video
  meta: kind=partial | timestamp=1778070245.7921124 | source=vosk | frequency_hz=380.0 | rms=301 | updated_at=1778070243.5349252
- [2026-05-06 20:24:06] operator / voice_transcript_partial / voice: window what video loop
  meta: kind=partial | timestamp=1778070246.0423703 | source=vosk | frequency_hz=380.0 | rms=301 | updated_at=1778070243.5349252
- [2026-05-06 20:24:06] operator / voice_transcript_partial / voice: window what video
  meta: kind=partial | timestamp=1778070246.295232 | source=vosk | frequency_hz=372.0 | rms=294 | updated_at=1778070246.2852182
- [2026-05-06 20:24:06] operator / voice_transcript_final / voice: window what video logger
  meta: kind=final | timestamp=1778070246.6653242 | source=final | frequency_hz=372.0 | rms=294 | updated_at=1778070246.2852182
- [2026-05-06 20:24:07] operator / voice_transcript_partial / voice: microphone
  meta: kind=partial | timestamp=1778070247.290953 | source=vosk | frequency_hz=372.0 | rms=294 | updated_at=1778070246.2852182
- [2026-05-06 20:24:07] operator / voice_transcript_partial / voice: blink enabled
  meta: kind=partial | timestamp=1778070247.546193 | source=vosk | frequency_hz=372.0 | rms=294 | updated_at=1778070246.2852182
- [2026-05-06 20:24:07] operator / voice_transcript_partial / voice: blink
  meta: kind=partial | timestamp=1778070247.7921574 | source=vosk | frequency_hz=372.0 | rms=294 | updated_at=1778070246.2852182
- [2026-05-06 20:24:08] operator / voice_transcript_partial / voice: blink reporting
  meta: kind=partial | timestamp=1778070248.0405304 | source=vosk | frequency_hz=358.0 | rms=288 | updated_at=1778070248.0345185
- [2026-05-06 20:24:08] operator / voice_transcript_final / voice: blink reporting
  meta: kind=final | timestamp=1778070248.6393511 | source=final | frequency_hz=344.7 | rms=305 | updated_at=1778070248.5359652
- [2026-05-06 20:24:10] operator / voice_transcript_partial / voice: what's the
  meta: kind=partial | timestamp=1778070250.5422137 | source=vosk | frequency_hz=373.5 | rms=286 | updated_at=1778070249.7872314
- [2026-05-06 20:24:11] operator / voice_transcript_partial / voice: what's the what's the
  meta: kind=partial | timestamp=1778070251.0472968 | source=vosk | frequency_hz=373.5 | rms=286 | updated_at=1778070249.7872314
- [2026-05-06 20:24:11] operator / voice_transcript_partial / voice: what's the video loop
  meta: kind=partial | timestamp=1778070251.2928205 | source=vosk | frequency_hz=373.5 | rms=286 | updated_at=1778070249.7872314
- [2026-05-06 20:24:11] operator / voice_transcript_partial / voice: what's the what's the invert
  meta: kind=partial | timestamp=1778070251.5449097 | source=vosk | frequency_hz=380.0 | rms=297 | updated_at=1778070251.5354009
- [2026-05-06 20:24:12] operator / voice_transcript_final / voice: what s the what s the auto logger
  meta: kind=final | timestamp=1778070252.452981 | source=final | frequency_hz=364.9 | rms=309 | updated_at=1778070252.2853837
- [2026-05-06 20:25:47] operator / voice_transcript_partial / voice: video
  meta: kind=partial | timestamp=1778070347.5519373 | source=vosk | frequency_hz=360.4 | rms=297 | updated_at=1778070342.7894542
- [2026-05-06 20:25:53] operator / voice_transcript_partial / voice: hey
  meta: kind=partial | timestamp=1778070353.0501702 | source=vosk | frequency_hz=412.0 | rms=292 | updated_at=1778070348.0395765
- [2026-05-06 20:25:53] operator / voice_transcript_final / voice: blink
  meta: kind=final | timestamp=1778070353.878047 | source=final | frequency_hz=412.0 | rms=292 | updated_at=1778070348.0395765
- [2026-05-06 20:26:14] operator / voice_transcript_partial / voice: known
  meta: kind=partial | timestamp=1778070374.0469315 | source=vosk | frequency_hz=377.2 | rms=287 | updated_at=1778070372.5407617
- [2026-05-06 20:26:14] operator / voice_transcript_partial / voice: loop
  meta: kind=partial | timestamp=1778070374.5481112 | source=vosk | frequency_hz=377.2 | rms=287 | updated_at=1778070372.5407617
- [2026-05-06 20:26:14] operator / voice_transcript_partial / voice: logging
  meta: kind=partial | timestamp=1778070374.8103437 | source=vosk | frequency_hz=377.2 | rms=287 | updated_at=1778070372.5407617
- [2026-05-06 20:26:15] operator / voice_transcript_partial / voice: logging is the
  meta: kind=partial | timestamp=1778070375.2998857 | source=vosk | frequency_hz=377.2 | rms=287 | updated_at=1778070372.5407617
- [2026-05-06 20:26:15] operator / voice_transcript_partial / voice: logging recent logs
  meta: kind=partial | timestamp=1778070375.5493307 | source=vosk | frequency_hz=377.2 | rms=287 | updated_at=1778070372.5407617
- [2026-05-06 20:26:15] operator / voice_transcript_partial / voice: logging is the microphone
  meta: kind=partial | timestamp=1778070375.8004682 | source=vosk | frequency_hz=377.2 | rms=287 | updated_at=1778070372.5407617
- [2026-05-06 20:26:16] operator / voice_transcript_partial / voice: logging is the microphone anomaly
  meta: kind=partial | timestamp=1778070376.0485952 | source=vosk | frequency_hz=377.2 | rms=287 | updated_at=1778070372.5407617
- [2026-05-06 20:26:16] operator / voice_transcript_partial / voice: logging is the microphone logger
  meta: kind=partial | timestamp=1778070376.2986104 | source=vosk | frequency_hz=377.2 | rms=287 | updated_at=1778070372.5407617
- [2026-05-06 20:26:16] operator / voice_transcript_partial / voice: logging is the microphone anomaly
  meta: kind=partial | timestamp=1778070376.816225 | source=vosk | frequency_hz=377.2 | rms=287 | updated_at=1778070372.5407617
- [2026-05-06 20:26:17] operator / voice_transcript_partial / voice: logging is the microphone event blink
  meta: kind=partial | timestamp=1778070377.056465 | source=vosk | frequency_hz=377.2 | rms=287 | updated_at=1778070372.5407617
- [2026-05-06 20:26:17] operator / voice_transcript_partial / voice: logging is the microphone event blink the
  meta: kind=partial | timestamp=1778070377.5499423 | source=vosk | frequency_hz=377.2 | rms=287 | updated_at=1778070372.5407617
- [2026-05-06 20:26:17] operator / voice_transcript_partial / voice: logging is the microphone anomaly
  meta: kind=partial | timestamp=1778070377.7971172 | source=vosk | frequency_hz=377.2 | rms=287 | updated_at=1778070372.5407617
- [2026-05-06 20:26:18] operator / voice_transcript_partial / voice: logging is the microphone anomaly trigger
  meta: kind=partial | timestamp=1778070378.30136 | source=vosk | frequency_hz=377.2 | rms=287 | updated_at=1778070372.5407617
- [2026-05-06 20:26:18] operator / voice_transcript_partial / voice: logging is the microphone anomaly trigger on
  meta: kind=partial | timestamp=1778070378.546605 | source=vosk | frequency_hz=377.2 | rms=287 | updated_at=1778070372.5407617
- [2026-05-06 20:26:18] operator / voice_transcript_partial / voice: logging is the microphone anomaly trigger
  meta: kind=partial | timestamp=1778070378.7967918 | source=vosk | frequency_hz=348.0 | rms=288 | updated_at=1778070378.7907758
- [2026-05-06 20:26:19] operator / voice_transcript_final / voice: logging recent logger microphone event blink human anomaly trigger logger
  meta: kind=final | timestamp=1778070379.4055996 | source=final | frequency_hz=343.8 | rms=291 | updated_at=1778070379.040021
- [2026-05-06 20:26:20] operator / voice_transcript_partial / voice: greeting
  meta: kind=partial | timestamp=1778070380.047018 | source=vosk | frequency_hz=343.8 | rms=291 | updated_at=1778070379.040021
- [2026-05-06 20:26:20] operator / voice_transcript_partial / voice: greeting the face
  meta: kind=partial | timestamp=1778070380.298113 | source=vosk | frequency_hz=343.8 | rms=291 | updated_at=1778070379.040021
- [2026-05-06 20:26:20] operator / voice_transcript_partial / voice: trigger enabled
  meta: kind=partial | timestamp=1778070380.556306 | source=vosk | frequency_hz=343.8 | rms=291 | updated_at=1778070379.040021
- [2026-05-06 20:26:20] operator / voice_transcript_partial / voice: video enable
  meta: kind=partial | timestamp=1778070380.8145566 | source=vosk | frequency_hz=343.8 | rms=291 | updated_at=1778070379.040021
- [2026-05-06 20:26:21] operator / voice_transcript_final / voice: greeting enable
  meta: kind=final | timestamp=1778070381.1523101 | source=final | frequency_hz=343.8 | rms=291 | updated_at=1778070379.040021
- [2026-05-06 20:26:22] operator / voice_transcript_partial / voice: the microphone
  meta: kind=partial | timestamp=1778070382.297333 | source=vosk | frequency_hz=343.8 | rms=291 | updated_at=1778070379.040021
- [2026-05-06 20:26:22] operator / voice_transcript_partial / voice: the microphone anomaly
  meta: kind=partial | timestamp=1778070382.8006864 | source=vosk | frequency_hz=343.8 | rms=291 | updated_at=1778070379.040021
- [2026-05-06 20:26:23] operator / voice_transcript_final / voice: the microphone trigger
  meta: kind=final | timestamp=1778070383.325714 | source=final | frequency_hz=402.0 | rms=295 | updated_at=1778070383.0420802
- [2026-05-06 20:26:30] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778070390.547686 | source=vosk | frequency_hz=375.0 | rms=294 | updated_at=1778070389.791738
- [2026-05-06 20:26:30] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1778070390.7965147 | source=vosk | frequency_hz=375.0 | rms=294 | updated_at=1778070389.791738
- [2026-05-06 20:26:30] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 20:26:31] operator / voice_transcript_partial / voice: motion
  meta: kind=partial | timestamp=1778070391.0482433 | source=vosk | frequency_hz=375.0 | rms=294 | updated_at=1778070389.791738
- [2026-05-06 20:26:31] operator / voice_transcript_partial / voice: enable machine learning
  meta: kind=partial | timestamp=1778070391.2985518 | source=vosk | frequency_hz=375.0 | rms=294 | updated_at=1778070389.791738
- [2026-05-06 20:26:31] operator / voice_transcript_partial / voice: e lion what is the
  meta: kind=partial | timestamp=1778070391.5497804 | source=vosk | frequency_hz=375.0 | rms=294 | updated_at=1778070389.791738
- [2026-05-06 20:26:31] operator / voice_transcript_partial / voice: e lion what is the visual
  meta: kind=partial | timestamp=1778070391.7981377 | source=vosk | frequency_hz=375.0 | rms=294 | updated_at=1778070389.791738
- [2026-05-06 20:26:32] operator / voice_transcript_partial / voice: e lion what is the recent logs
  meta: kind=partial | timestamp=1778070392.051068 | source=vosk | frequency_hz=375.0 | rms=294 | updated_at=1778070389.791738
- [2026-05-06 20:26:32] operator / voice_transcript_partial / voice: e buzzer mute buzzer sound
  meta: kind=partial | timestamp=1778070392.2991803 | source=vosk | frequency_hz=375.0 | rms=294 | updated_at=1778070389.791738
- [2026-05-06 20:26:32] operator / voice_transcript_partial / voice: e buzzer mute buzzer sound is
  meta: kind=partial | timestamp=1778070392.8021328 | source=vosk | frequency_hz=375.0 | rms=294 | updated_at=1778070389.791738
- [2026-05-06 20:26:34] operator / voice_transcript_final / voice: e buzzer mute buzzer sound
  meta: kind=final | timestamp=1778070394.1383219 | source=final | frequency_hz=365.3 | rms=289 | updated_at=1778070393.2918386
- [2026-05-06 20:26:37] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1778070397.213204 | source=vosk | frequency_hz=388.4 | rms=742 | updated_at=1778070394.9542284
- [2026-05-06 20:26:37] operator / voice_transcript_partial / voice: is the
  meta: kind=partial | timestamp=1778070397.4615412 | source=vosk | frequency_hz=388.4 | rms=742 | updated_at=1778070394.9542284
- [2026-05-06 20:26:37] operator / voice_transcript_partial / voice: pir event
  meta: kind=partial | timestamp=1778070397.7109928 | source=vosk | frequency_hz=388.4 | rms=742 | updated_at=1778070394.9542284
- [2026-05-06 20:26:38] operator / voice_transcript_partial / voice: enabled
  meta: kind=partial | timestamp=1778070398.2110658 | source=vosk | frequency_hz=388.4 | rms=742 | updated_at=1778070394.9542284
- [2026-05-06 20:26:38] operator / voice_transcript_partial / voice: enable adaptive
  meta: kind=partial | timestamp=1778070398.4678576 | source=vosk | frequency_hz=388.4 | rms=742 | updated_at=1778070394.9542284
- [2026-05-06 20:26:38] operator / voice_transcript_partial / voice: is the
  meta: kind=partial | timestamp=1778070398.7087266 | source=vosk | frequency_hz=388.4 | rms=742 | updated_at=1778070394.9542284
- [2026-05-06 20:26:38] operator / voice_transcript_partial / voice: pir event blink
  meta: kind=partial | timestamp=1778070398.9876554 | source=vosk | frequency_hz=388.4 | rms=742 | updated_at=1778070394.9542284
- [2026-05-06 20:26:39] operator / voice_transcript_partial / voice: pir guard
  meta: kind=partial | timestamp=1778070399.2233062 | source=vosk | frequency_hz=388.4 | rms=742 | updated_at=1778070394.9542284
- [2026-05-06 20:26:39] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778070399.4603324 | source=vosk | frequency_hz=388.4 | rms=742 | updated_at=1778070394.9542284
- [2026-05-06 20:26:39] operator / voice_transcript_partial / voice: output enabled
  meta: kind=partial | timestamp=1778070399.7250578 | source=vosk | frequency_hz=388.4 | rms=742 | updated_at=1778070394.9542284
- [2026-05-06 20:26:40] operator / voice_transcript_final / voice: human output enable
  meta: kind=final | timestamp=1778070400.33315 | source=final | frequency_hz=388.4 | rms=742 | updated_at=1778070394.9542284
- [2026-05-06 20:26:41] operator / voice_transcript_partial / voice: elian
  meta: kind=partial | timestamp=1778070401.464602 | source=vosk | frequency_hz=388.4 | rms=742 | updated_at=1778070394.9542284
- [2026-05-06 20:26:41] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 20:26:42] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1778070402.5794704 | source=final | frequency_hz=388.4 | rms=742 | updated_at=1778070394.9542284
- [2026-05-06 20:26:44] operator / voice_transcript_partial / voice: buzzer for
  meta: kind=partial | timestamp=1778070404.7122629 | source=vosk | frequency_hz=387.2 | rms=300 | updated_at=1778070403.7037063
- [2026-05-06 20:26:47] operator / voice_transcript_partial / voice: buzzer for human voice
  meta: kind=partial | timestamp=1778070407.4663272 | source=vosk | frequency_hz=370.6 | rms=295 | updated_at=1778070407.4553292
- [2026-05-06 20:26:48] operator / voice_transcript_partial / voice: buzzer for human the
  meta: kind=partial | timestamp=1778070408.4756184 | source=vosk | frequency_hz=371.8 | rms=295 | updated_at=1778070407.7038083
- [2026-05-06 20:26:48] operator / voice_transcript_final / voice: buzzer for human
  meta: kind=final | timestamp=1778070408.8775644 | source=final | frequency_hz=371.8 | rms=295 | updated_at=1778070407.7038083
- [2026-05-06 20:26:49] operator / voice_transcript_partial / voice: buzzer
  meta: kind=partial | timestamp=1778070409.4679718 | source=vosk | frequency_hz=371.8 | rms=295 | updated_at=1778070407.7038083
- [2026-05-06 20:26:50] operator / voice_transcript_partial / voice: window shortcuts
  meta: kind=partial | timestamp=1778070410.4615912 | source=vosk | frequency_hz=371.8 | rms=295 | updated_at=1778070407.7038083
- [2026-05-06 20:26:51] operator / voice_transcript_partial / voice: window movement
  meta: kind=partial | timestamp=1778070411.0339444 | source=vosk | frequency_hz=371.8 | rms=295 | updated_at=1778070407.7038083
- [2026-05-06 20:26:51] operator / voice_transcript_partial / voice: window shortcuts
  meta: kind=partial | timestamp=1778070411.2119126 | source=vosk | frequency_hz=371.8 | rms=295 | updated_at=1778070407.7038083
- [2026-05-06 20:26:51] operator / voice_transcript_final / voice: window
  meta: kind=final | timestamp=1778070411.5501204 | source=final | frequency_hz=336.0 | rms=299 | updated_at=1778070411.454832
- [2026-05-06 20:26:53] operator / voice_transcript_partial / voice: video display
  meta: kind=partial | timestamp=1778070413.4755383 | source=vosk | frequency_hz=336.6 | rms=286 | updated_at=1778070412.454154
- [2026-05-06 20:26:53] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778070413.7105718 | source=vosk | frequency_hz=336.6 | rms=286 | updated_at=1778070412.454154
- [2026-05-06 20:26:53] operator / voice_transcript_partial / voice: the acoustic
  meta: kind=partial | timestamp=1778070413.9621382 | source=vosk | frequency_hz=336.6 | rms=286 | updated_at=1778070412.454154
- [2026-05-06 20:26:54] operator / voice_transcript_partial / voice: the acoustic voice
  meta: kind=partial | timestamp=1778070414.210252 | source=vosk | frequency_hz=336.6 | rms=286 | updated_at=1778070412.454154
- [2026-05-06 20:26:54] operator / voice_transcript_partial / voice: the acoustic leon
  meta: kind=partial | timestamp=1778070414.463249 | source=vosk | frequency_hz=336.6 | rms=286 | updated_at=1778070412.454154
- [2026-05-06 20:26:55] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 20:26:56] assistant / spoken_confirmation / voice: Yes. What do you want to know?
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:26:59] operator / voice_transcript_partial / voice: ml training
  meta: kind=partial | timestamp=1778070419.2172096 | source=vosk | frequency_hz=357.7 | rms=281 | updated_at=1778070417.0872731
- [2026-05-06 20:26:59] operator / voice_transcript_partial / voice: ml training is
  meta: kind=partial | timestamp=1778070419.5720186 | source=vosk | frequency_hz=357.7 | rms=281 | updated_at=1778070417.0872731
- [2026-05-06 20:27:00] operator / voice_transcript_final / voice: ml training is loop
  meta: kind=final | timestamp=1778070420.6982887 | source=final | frequency_hz=357.7 | rms=281 | updated_at=1778070417.0872731
- [2026-05-06 20:27:01] operator / voice_transcript_partial / voice: once
  meta: kind=partial | timestamp=1778070421.7100904 | source=vosk | frequency_hz=394.0 | rms=291 | updated_at=1778070420.7673314
- [2026-05-06 20:27:01] operator / voice_transcript_partial / voice: mode switching
  meta: kind=partial | timestamp=1778070421.9620564 | source=vosk | frequency_hz=394.0 | rms=291 | updated_at=1778070420.7673314
- [2026-05-06 20:27:02] operator / voice_transcript_partial / voice: once reporting
  meta: kind=partial | timestamp=1778070422.2132974 | source=vosk | frequency_hz=394.0 | rms=291 | updated_at=1778070420.7673314
- [2026-05-06 20:27:03] operator / voice_transcript_final / voice: once reporting
  meta: kind=final | timestamp=1778070423.3090606 | source=final | frequency_hz=394.0 | rms=291 | updated_at=1778070420.7673314
- [2026-05-06 20:27:03] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1778070423.4598327 | source=vosk | frequency_hz=394.0 | rms=291 | updated_at=1778070420.7673314
- [2026-05-06 20:27:03] operator / voice_transcript_partial / voice: is the
  meta: kind=partial | timestamp=1778070423.9608157 | source=vosk | frequency_hz=394.0 | rms=291 | updated_at=1778070420.7673314
- [2026-05-06 20:27:04] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1778070424.2842953 | source=vosk | frequency_hz=394.0 | rms=291 | updated_at=1778070420.7673314
- [2026-05-06 20:27:04] operator / voice_transcript_partial / voice: is the greeting
  meta: kind=partial | timestamp=1778070424.4611943 | source=vosk | frequency_hz=394.0 | rms=291 | updated_at=1778070420.7673314
- [2026-05-06 20:27:05] operator / voice_transcript_final / voice: is greeting
  meta: kind=final | timestamp=1778070425.5226543 | source=final | frequency_hz=394.0 | rms=291 | updated_at=1778070420.7673314
- [2026-05-06 20:27:23] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1778070443.2592828 | source=vosk | frequency_hz=384.0 | rms=299 | updated_at=1778070442.9567719
- [2026-05-06 20:27:23] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1778070443.7143211 | source=vosk | frequency_hz=384.0 | rms=299 | updated_at=1778070442.9567719
- [2026-05-06 20:27:24] operator / voice_transcript_partial / voice: detection
  meta: kind=partial | timestamp=1778070444.9631991 | source=vosk | frequency_hz=388.6 | rms=284 | updated_at=1778070444.2122927
- [2026-05-06 20:27:26] operator / voice_transcript_final / voice: do it again
  meta: kind=final | timestamp=1778070446.0045757 | source=final | frequency_hz=388.6 | rms=284 | updated_at=1778070444.2122927
- [2026-05-06 20:27:26] operator / voice_command / voice: do it again
  meta: normalized=True
- [2026-05-06 20:27:26] assistant / spoken_confirmation / voice: There is no recent command to repeat yet.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:27:30] operator / voice_transcript_partial / voice: is no recent logs
  meta: kind=partial | timestamp=1778070450.2851353 | source=vosk | frequency_hz=362.9 | rms=308 | updated_at=1778070448.0153549
- [2026-05-06 20:27:30] operator / voice_transcript_partial / voice: is no recent current
  meta: kind=partial | timestamp=1778070450.524415 | source=vosk | frequency_hz=362.9 | rms=308 | updated_at=1778070448.0153549
- [2026-05-06 20:27:30] operator / voice_transcript_partial / voice: is no recent movement
  meta: kind=partial | timestamp=1778070450.7858844 | source=vosk | frequency_hz=362.9 | rms=308 | updated_at=1778070448.0153549
- [2026-05-06 20:27:31] operator / voice_transcript_final / voice: is no recent loop
  meta: kind=final | timestamp=1778070451.4124234 | source=final | frequency_hz=362.9 | rms=308 | updated_at=1778070448.0153549
- [2026-05-06 20:27:31] operator / voice_transcript_partial / voice: video
  meta: kind=partial | timestamp=1778070451.5262127 | source=vosk | frequency_hz=362.9 | rms=308 | updated_at=1778070448.0153549
- [2026-05-06 20:27:31] operator / voice_transcript_partial / voice: media loop
  meta: kind=partial | timestamp=1778070451.7716079 | source=vosk | frequency_hz=362.9 | rms=308 | updated_at=1778070448.0153549
- [2026-05-06 20:27:32] operator / voice_transcript_final / voice: media
  meta: kind=final | timestamp=1778070452.6198344 | source=final | frequency_hz=362.9 | rms=308 | updated_at=1778070448.0153549
- [2026-05-06 20:27:33] operator / voice_transcript_partial / voice: repeat
  meta: kind=partial | timestamp=1778070453.0214436 | source=vosk | frequency_hz=362.9 | rms=308 | updated_at=1778070448.0153549
- [2026-05-06 20:27:33] operator / voice_transcript_partial / voice: tuning
  meta: kind=partial | timestamp=1778070453.2816203 | source=vosk | frequency_hz=362.9 | rms=308 | updated_at=1778070448.0153549
- [2026-05-06 20:27:33] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1778070453.5247319 | source=vosk | frequency_hz=362.9 | rms=308 | updated_at=1778070448.0153549
- [2026-05-06 20:27:34] operator / voice_transcript_final / voice: repeat it
  meta: kind=final | timestamp=1778070454.1369436 | source=final | frequency_hz=362.9 | rms=308 | updated_at=1778070448.0153549
- [2026-05-06 20:27:34] operator / voice_command / voice: repeat it
  meta: normalized=True
- [2026-05-06 20:27:34] assistant / spoken_confirmation / voice: I did not catch a supported command there. Please try again.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:27:34] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1778070454.7715409 | source=vosk | frequency_hz=362.9 | rms=308 | updated_at=1778070448.0153549
- [2026-05-06 20:27:35] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1778070455.8749053 | source=final | frequency_hz=362.9 | rms=308 | updated_at=1778070448.0153549
- [2026-05-06 20:27:36] operator / voice_transcript_partial / voice: greeting
  meta: kind=partial | timestamp=1778070456.0201304 | source=vosk | frequency_hz=362.9 | rms=308 | updated_at=1778070448.0153549
- [2026-05-06 20:27:36] operator / voice_transcript_partial / voice: run the
  meta: kind=partial | timestamp=1778070456.9526994 | source=vosk | frequency_hz=362.9 | rms=308 | updated_at=1778070448.0153549
- [2026-05-06 20:27:36] operator / voice_transcript_partial / voice: run the smart
  meta: kind=partial | timestamp=1778070456.9597154 | source=vosk | frequency_hz=362.9 | rms=308 | updated_at=1778070448.0153549
- [2026-05-06 20:27:36] operator / voice_transcript_partial / voice: run the smart sentry
  meta: kind=partial | timestamp=1778070456.9677281 | source=vosk | frequency_hz=362.9 | rms=308 | updated_at=1778070448.0153549
- [2026-05-06 20:27:38] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1778070458.1441126 | source=final | frequency_hz=330.0 | rms=700 | updated_at=1778070457.7137752
- [2026-05-06 20:27:38] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-05-06 20:27:38] assistant / spoken_confirmation / voice: Connecting Smart Sentry boards now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:27:51] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1778070471.2228818 | source=vosk | frequency_hz=390.0 | rms=287 | updated_at=1778070468.964705
- [2026-05-06 20:27:51] operator / voice_transcript_partial / voice: e no
  meta: kind=partial | timestamp=1778070471.667848 | source=vosk | frequency_hz=390.0 | rms=287 | updated_at=1778070468.964705
- [2026-05-06 20:27:51] operator / voice_transcript_partial / voice: e no detection
  meta: kind=partial | timestamp=1778070471.7277248 | source=vosk | frequency_hz=390.0 | rms=287 | updated_at=1778070468.964705
- [2026-05-06 20:27:52] operator / voice_transcript_partial / voice: e not cues enabled
  meta: kind=partial | timestamp=1778070472.2203202 | source=vosk | frequency_hz=390.0 | rms=287 | updated_at=1778070468.964705
- [2026-05-06 20:27:52] operator / voice_transcript_partial / voice: e not cues disabled
  meta: kind=partial | timestamp=1778070472.4731777 | source=vosk | frequency_hz=390.0 | rms=287 | updated_at=1778070468.964705
- [2026-05-06 20:27:52] operator / voice_transcript_partial / voice: e not cues is servo motion
  meta: kind=partial | timestamp=1778070472.7218897 | source=vosk | frequency_hz=390.0 | rms=287 | updated_at=1778070468.964705
- [2026-05-06 20:27:52] operator / voice_transcript_partial / voice: e not cues disabled keyboard
  meta: kind=partial | timestamp=1778070472.9785275 | source=vosk | frequency_hz=390.0 | rms=287 | updated_at=1778070468.964705
- [2026-05-06 20:27:53] operator / voice_transcript_partial / voice: e not cues disabled keep current
  meta: kind=partial | timestamp=1778070473.2213635 | source=vosk | frequency_hz=390.0 | rms=287 | updated_at=1778070468.964705
- [2026-05-06 20:27:53] operator / voice_transcript_partial / voice: e not cues disabled keep current zone
  meta: kind=partial | timestamp=1778070473.7187827 | source=vosk | frequency_hz=390.0 | rms=287 | updated_at=1778070468.964705
- [2026-05-06 20:27:54] operator / voice_transcript_final / voice: e not cues disable keep current zone
  meta: kind=final | timestamp=1778070474.4217334 | source=final | frequency_hz=390.0 | rms=287 | updated_at=1778070468.964705
- [2026-05-06 20:27:55] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1778070475.4870048 | source=vosk | frequency_hz=390.0 | rms=287 | updated_at=1778070468.964705
- [2026-05-06 20:27:55] operator / voice_transcript_partial / voice: status elliot
  meta: kind=partial | timestamp=1778070475.9716074 | source=vosk | frequency_hz=390.0 | rms=287 | updated_at=1778070468.964705
- [2026-05-06 20:27:57] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 20:27:58] assistant / spoken_confirmation / voice: Yes? I am listening.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:28:07] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1778070487.9516573 | source=vosk | frequency_hz=348.1 | rms=298 | updated_at=1778070483.1898785
- [2026-05-06 20:28:08] operator / voice_transcript_partial / voice: e assistant
  meta: kind=partial | timestamp=1778070488.1940784 | source=vosk | frequency_hz=348.1 | rms=298 | updated_at=1778070483.1898785
- [2026-05-06 20:28:08] operator / voice_transcript_partial / voice: e rest
  meta: kind=partial | timestamp=1778070488.458248 | source=vosk | frequency_hz=348.1 | rms=298 | updated_at=1778070483.1898785
- [2026-05-06 20:28:09] operator / voice_transcript_final / voice: e rest
  meta: kind=final | timestamp=1778070489.3716972 | source=final | frequency_hz=348.1 | rms=298 | updated_at=1778070483.1898785
- [2026-05-06 20:28:09] operator / voice_transcript_partial / voice: hey
  meta: kind=partial | timestamp=1778070489.4574234 | source=vosk | frequency_hz=348.1 | rms=298 | updated_at=1778070483.1898785
- [2026-05-06 20:28:09] operator / voice_transcript_partial / voice: hey leon
  meta: kind=partial | timestamp=1778070489.9642007 | source=vosk | frequency_hz=348.1 | rms=298 | updated_at=1778070483.1898785
- [2026-05-06 20:28:10] operator / voice_transcript_partial / voice: hey precision
  meta: kind=partial | timestamp=1778070490.1963 | source=vosk | frequency_hz=348.1 | rms=298 | updated_at=1778070483.1898785
- [2026-05-06 20:28:10] operator / voice_transcript_partial / voice: hey is the
  meta: kind=partial | timestamp=1778070490.457403 | source=vosk | frequency_hz=348.1 | rms=298 | updated_at=1778070483.1898785
- [2026-05-06 20:28:11] operator / voice_transcript_final / voice: hey is the
  meta: kind=final | timestamp=1778070491.3906543 | source=final | frequency_hz=348.1 | rms=298 | updated_at=1778070483.1898785
- [2026-05-06 20:28:12] operator / voice_transcript_partial / voice: changes
  meta: kind=partial | timestamp=1778070492.7127907 | source=vosk | frequency_hz=348.1 | rms=298 | updated_at=1778070483.1898785
- [2026-05-06 20:28:12] operator / voice_transcript_partial / voice: change your voice
  meta: kind=partial | timestamp=1778070492.947703 | source=vosk | frequency_hz=348.1 | rms=298 | updated_at=1778070483.1898785
- [2026-05-06 20:28:13] operator / voice_transcript_partial / voice: change your voice to
  meta: kind=partial | timestamp=1778070493.4472032 | source=vosk | frequency_hz=348.1 | rms=298 | updated_at=1778070483.1898785
- [2026-05-06 20:28:13] operator / voice_transcript_partial / voice: change your voice to rest
  meta: kind=partial | timestamp=1778070493.7107272 | source=vosk | frequency_hz=348.1 | rms=298 | updated_at=1778070483.1898785
- [2026-05-06 20:28:13] operator / voice_transcript_partial / voice: change your voice to anything
  meta: kind=partial | timestamp=1778070493.9467692 | source=vosk | frequency_hz=348.1 | rms=298 | updated_at=1778070483.1898785
- [2026-05-06 20:28:14] operator / voice_transcript_partial / voice: change your voice to eileen the
  meta: kind=partial | timestamp=1778070494.447533 | source=vosk | frequency_hz=348.1 | rms=298 | updated_at=1778070483.1898785
- [2026-05-06 20:28:14] operator / voice_transcript_partial / voice: change your voice to alion hey
  meta: kind=partial | timestamp=1778070494.6977677 | source=vosk | frequency_hz=324.0 | rms=297 | updated_at=1778070494.692767
- [2026-05-06 20:28:15] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 20:28:15] operator / voice_transcript_final / voice: elion change your voice
  meta: kind=final | timestamp=1778070495.8397114 | source=final | frequency_hz=324.0 | rms=297 | updated_at=1778070494.692767
- [2026-05-06 20:28:16] operator / voice_command / voice: elion change your voice
  meta: normalized=True
- [2026-05-06 20:28:17] assistant / spoken_confirmation / voice: I can speak in 69 voices across 18 voice families, including Microsoft Zira Desktop, Microsoft Mark, Microsoft David Desktop, American English, and 14 more. Tell me what voice you want, or ask what are the options.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:28:35] operator / voice_transcript_partial / voice: hey current status
  meta: kind=partial | timestamp=1778070515.979239 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:36] operator / voice_transcript_partial / voice: hey go speak
  meta: kind=partial | timestamp=1778070516.2352464 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:36] operator / voice_transcript_partial / voice: hey go speak increase
  meta: kind=partial | timestamp=1778070516.4495037 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:36] operator / voice_transcript_partial / voice: hey go speak controls disabled
  meta: kind=partial | timestamp=1778070516.6993892 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:36] operator / voice_transcript_partial / voice: hey go speech is the system
  meta: kind=partial | timestamp=1778070516.947547 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:37] operator / voice_transcript_partial / voice: hey go speak increase is the precision
  meta: kind=partial | timestamp=1778070517.1999385 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:37] operator / voice_transcript_partial / voice: hey go speak increase is the recent logs
  meta: kind=partial | timestamp=1778070517.4467788 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:37] operator / voice_transcript_partial / voice: hey go speak increase is the recent greeting
  meta: kind=partial | timestamp=1778070517.6973364 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:37] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision
  meta: kind=partial | timestamp=1778070517.985277 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:38] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision natural
  meta: kind=partial | timestamp=1778070518.1991215 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:38] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision not working
  meta: kind=partial | timestamp=1778070518.4660347 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:38] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic
  meta: kind=partial | timestamp=1778070518.6962578 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:38] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision acoustic voice cleanup
  meta: kind=partial | timestamp=1778070518.9487774 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:39] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is
  meta: kind=partial | timestamp=1778070519.1999068 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:39] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is the
  meta: kind=partial | timestamp=1778070519.4483032 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:39] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is include
  meta: kind=partial | timestamp=1778070519.7282174 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:39] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is e greeting
  meta: kind=partial | timestamp=1778070519.9502606 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:40] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is include include
  meta: kind=partial | timestamp=1778070520.20787 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:40] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is include include cancel
  meta: kind=partial | timestamp=1778070520.4482327 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:40] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is include include cancel the
  meta: kind=partial | timestamp=1778070520.708127 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:41] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is include include cancel zone is the
  meta: kind=partial | timestamp=1778070521.3742847 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:41] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is include include cancel zone is the current
  meta: kind=partial | timestamp=1778070521.9788709 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:42] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is include include cancel zone is the keyboard movement
  meta: kind=partial | timestamp=1778070522.2044835 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:42] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is include include cancel zone is the of microphone
  meta: kind=partial | timestamp=1778070522.447298 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:42] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is include include cancel zone is the microphone
  meta: kind=partial | timestamp=1778070522.9486623 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:43] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is include include cancel zone is the microphone anomaly
  meta: kind=partial | timestamp=1778070523.2092087 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:43] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is include include cancel zone is the of microphone updates
  meta: kind=partial | timestamp=1778070523.4493382 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:43] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is include include cancel zone is the microphone hey is
  meta: kind=partial | timestamp=1778070523.7111845 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:43] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is include include cancel zone is the microphone hey is the
  meta: kind=partial | timestamp=1778070523.948106 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:44] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is include include cancel zone is the microphone hey is the ml
  meta: kind=partial | timestamp=1778070524.4499881 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:44] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is include include cancel zone is the microphone hey is the
  meta: kind=partial | timestamp=1778070524.7024543 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:44] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is include include cancel zone is the microphone hey is the continuous
  meta: kind=partial | timestamp=1778070524.9483154 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:45] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is include include cancel zone is the microphone hey is the continuous hunt
  meta: kind=partial | timestamp=1778070525.4488804 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:45] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is include include cancel zone is the microphone hey is the continuous
  meta: kind=partial | timestamp=1778070525.6974497 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:46] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is include include cancel zone is the microphone hey is the continuous in tuning
  meta: kind=partial | timestamp=1778070526.2272377 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:46] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is include include cancel zone is the microphone hey is the continuous in human
  meta: kind=partial | timestamp=1778070526.4481134 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:46] operator / voice_transcript_partial / voice: hey go speak increase is the recent precision what's acoustic is include include cancel zone is the microphone hey is the continuous in trigger once
  meta: kind=partial | timestamp=1778070526.6990328 | source=vosk | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:47] operator / voice_transcript_final / voice: hey go speak increase recent the recent precision what s acoustic is include include cancel zone is the of microphone close the is the continuous in trigger once
  meta: kind=final | timestamp=1778070527.4827933 | source=final | frequency_hz=358.7 | rms=290 | updated_at=1778070513.1912398
- [2026-05-06 20:28:49] operator / voice_transcript_partial / voice: cue
  meta: kind=partial | timestamp=1778070529.132138 | source=vosk | frequency_hz=246.0 | rms=428 | updated_at=1778070527.735967
- [2026-05-06 20:28:49] operator / voice_transcript_partial / voice: cue voice
  meta: kind=partial | timestamp=1778070529.138156 | source=vosk | frequency_hz=246.0 | rms=428 | updated_at=1778070527.735967
- [2026-05-06 20:28:49] operator / voice_transcript_partial / voice: cue voice your
  meta: kind=partial | timestamp=1778070529.390408 | source=vosk | frequency_hz=246.0 | rms=428 | updated_at=1778070527.735967
- [2026-05-06 20:28:50] operator / voice_transcript_partial / voice: cue voice your buzzer
  meta: kind=partial | timestamp=1778070530.1392324 | source=vosk | frequency_hz=246.0 | rms=428 | updated_at=1778070527.735967
- [2026-05-06 20:28:50] operator / voice_transcript_partial / voice: cue voice you doing
  meta: kind=partial | timestamp=1778070530.4075787 | source=vosk | frequency_hz=246.0 | rms=428 | updated_at=1778070527.735967
- [2026-05-06 20:28:50] operator / voice_transcript_partial / voice: cue voice your is updates
  meta: kind=partial | timestamp=1778070530.6395974 | source=vosk | frequency_hz=246.0 | rms=428 | updated_at=1778070527.735967
- [2026-05-06 20:28:51] operator / voice_transcript_final / voice: cue voice your is updates
  meta: kind=final | timestamp=1778070531.535268 | source=final | frequency_hz=376.0 | rms=296 | updated_at=1778070530.8857677
- [2026-05-06 20:28:52] operator / voice_transcript_partial / voice: change theme
  meta: kind=partial | timestamp=1778070532.1654305 | source=vosk | frequency_hz=376.0 | rms=296 | updated_at=1778070530.8857677
- [2026-05-06 20:28:52] operator / voice_transcript_partial / voice: change to
  meta: kind=partial | timestamp=1778070532.1784453 | source=vosk | frequency_hz=376.0 | rms=296 | updated_at=1778070530.8857677
- [2026-05-06 20:28:52] operator / voice_transcript_partial / voice: change to of invert
  meta: kind=partial | timestamp=1778070532.3886247 | source=vosk | frequency_hz=376.0 | rms=296 | updated_at=1778070530.8857677
- [2026-05-06 20:28:52] operator / voice_transcript_partial / voice: change to alien deactivate
  meta: kind=partial | timestamp=1778070532.77847 | source=vosk | frequency_hz=376.0 | rms=296 | updated_at=1778070530.8857677
- [2026-05-06 20:28:52] operator / voice_transcript_partial / voice: change to of in human voice
  meta: kind=partial | timestamp=1778070532.8891418 | source=vosk | frequency_hz=376.0 | rms=296 | updated_at=1778070530.8857677
- [2026-05-06 20:28:53] operator / voice_transcript_partial / voice: change to of in human voice the media
  meta: kind=partial | timestamp=1778070533.6389282 | source=vosk | frequency_hz=376.0 | rms=296 | updated_at=1778070530.8857677
- [2026-05-06 20:28:53] operator / voice_transcript_partial / voice: change to of in human voice the manual
  meta: kind=partial | timestamp=1778070533.8902442 | source=vosk | frequency_hz=376.0 | rms=296 | updated_at=1778070530.8857677
- [2026-05-06 20:28:54] operator / voice_transcript_partial / voice: change to of in human voice the mask diagnostics
  meta: kind=partial | timestamp=1778070534.1408253 | source=vosk | frequency_hz=376.0 | rms=296 | updated_at=1778070530.8857677
- [2026-05-06 20:28:54] operator / voice_transcript_partial / voice: change to of in human voice the manual hey
  meta: kind=partial | timestamp=1778070534.3895113 | source=vosk | frequency_hz=376.0 | rms=296 | updated_at=1778070530.8857677
- [2026-05-06 20:28:55] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 20:28:56] assistant / spoken_confirmation / voice: Yes? I am listening.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:28:58] operator / voice_transcript_partial / voice: e is
  meta: kind=partial | timestamp=1778070538.8989913 | source=vosk | frequency_hz=340.1 | rms=287 | updated_at=1778070538.1336222
- [2026-05-06 20:28:59] operator / voice_transcript_partial / voice: use
  meta: kind=partial | timestamp=1778070539.1532881 | source=vosk | frequency_hz=340.1 | rms=287 | updated_at=1778070538.1336222
- [2026-05-06 20:29:00] operator / voice_transcript_final / voice: yes
  meta: kind=final | timestamp=1778070540.0069108 | source=final | frequency_hz=351.3 | rms=280 | updated_at=1778070539.3834596
- [2026-05-06 20:29:00] operator / voice_command / voice: yes
  meta: normalized=True
- [2026-05-06 20:29:00] operator / voice_transcript_partial / voice: hey
  meta: kind=partial | timestamp=1778070540.4037368 | source=vosk | frequency_hz=351.3 | rms=280 | updated_at=1778070539.3834596
- [2026-05-06 20:29:00] operator / voice_transcript_partial / voice: hey leon
  meta: kind=partial | timestamp=1778070540.642979 | source=vosk | frequency_hz=351.3 | rms=280 | updated_at=1778070539.3834596
- [2026-05-06 20:29:01] operator / voice_transcript_partial / voice: hey the status
  meta: kind=partial | timestamp=1778070541.3303168 | source=vosk | frequency_hz=351.3 | rms=280 | updated_at=1778070539.3834596
- [2026-05-06 20:29:01] operator / voice_transcript_final / voice: hey the status
  meta: kind=final | timestamp=1778070541.7989514 | source=final | frequency_hz=398.0 | rms=283 | updated_at=1778070541.639944
- [2026-05-06 20:29:26] operator / voice_transcript_partial / voice: video
  meta: kind=partial | timestamp=1778070566.2156572 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:26] operator / voice_transcript_partial / voice: the acoustic
  meta: kind=partial | timestamp=1778070566.4588647 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:27] operator / voice_transcript_partial / voice: the acoustic what is
  meta: kind=partial | timestamp=1778070567.2279751 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:27] operator / voice_transcript_partial / voice: the acoustic want to
  meta: kind=partial | timestamp=1778070567.7048821 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:27] operator / voice_transcript_partial / voice: the acoustic want to acoustic
  meta: kind=partial | timestamp=1778070567.9554935 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:28] operator / voice_transcript_partial / voice: the acoustic what is shortcuts
  meta: kind=partial | timestamp=1778070568.2273424 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:28] operator / voice_transcript_partial / voice: the acoustic want to show zone
  meta: kind=partial | timestamp=1778070568.459996 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:29] operator / voice_transcript_partial / voice: the acoustic want to show zone tilt motion
  meta: kind=partial | timestamp=1778070569.2050867 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:29] operator / voice_transcript_partial / voice: the acoustic want to show zone mode
  meta: kind=partial | timestamp=1778070569.4572153 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:29] operator / voice_transcript_partial / voice: the acoustic want to show zone mode trigger
  meta: kind=partial | timestamp=1778070569.9561052 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:30] operator / voice_transcript_final / voice: the acoustic want to show zone mode travel trigger
  meta: kind=final | timestamp=1778070570.8248184 | source=final | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:30] operator / voice_transcript_partial / voice: human
  meta: kind=partial | timestamp=1778070570.955781 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:31] operator / voice_transcript_partial / voice: human use
  meta: kind=partial | timestamp=1778070571.2034197 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:31] operator / voice_transcript_partial / voice: summaries acoustic
  meta: kind=partial | timestamp=1778070571.7040355 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:32] operator / voice_transcript_final / voice: summaries
  meta: kind=final | timestamp=1778070572.8209398 | source=final | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:32] operator / voice_transcript_partial / voice: is led
  meta: kind=partial | timestamp=1778070572.9071462 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:33] operator / voice_transcript_partial / voice: slew order
  meta: kind=partial | timestamp=1778070573.1023138 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:34] operator / voice_transcript_partial / voice: slew cues
  meta: kind=partial | timestamp=1778070574.0197754 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:34] operator / voice_transcript_partial / voice: slew human
  meta: kind=partial | timestamp=1778070574.241963 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:34] operator / voice_transcript_partial / voice: slew cues
  meta: kind=partial | timestamp=1778070574.5092893 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:34] operator / voice_transcript_partial / voice: slew human voice
  meta: kind=partial | timestamp=1778070574.7410753 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:35] operator / voice_transcript_final / voice: slew cues
  meta: kind=final | timestamp=1778070575.1520789 | source=final | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:35] operator / voice_transcript_partial / voice: keyboard
  meta: kind=partial | timestamp=1778070575.4920268 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:35] operator / voice_transcript_partial / voice: cue blink
  meta: kind=partial | timestamp=1778070575.7513154 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:35] operator / voice_transcript_partial / voice: cue loop
  meta: kind=partial | timestamp=1778070575.990438 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:36] operator / voice_transcript_partial / voice: cue loop report the
  meta: kind=partial | timestamp=1778070576.492379 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:36] operator / voice_transcript_partial / voice: cue loop reporting
  meta: kind=partial | timestamp=1778070576.7388654 | source=vosk | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:29:37] operator / voice_transcript_final / voice: cue loop report theme
  meta: kind=final | timestamp=1778070577.3587267 | source=final | frequency_hz=298.0 | rms=285 | updated_at=1778070565.7049792
- [2026-05-06 20:30:43] operator / voice_transcript_partial / voice: aileen disable scope of be slew order
  meta: kind=partial | timestamp=1778070643.272077 | source=vosk | frequency_hz=132.0 | rms=222 | updated_at=1778070638.455081
- [2026-05-06 20:30:44] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-06 20:30:45] assistant / spoken_confirmation / voice: I am here. Ask your question.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-06 20:30:44] operator / voice_transcript_partial / voice: current status
  meta: kind=partial | timestamp=1778070644.7729528 | source=vosk | frequency_hz=336.1 | rms=282 | updated_at=1778070644.1864665
- [2026-05-06 20:30:45] operator / voice_transcript_partial / voice: cue is the
  meta: kind=partial | timestamp=1778070645.522679 | source=vosk | frequency_hz=336.1 | rms=282 | updated_at=1778070644.1864665
- [2026-05-06 20:30:45] operator / voice_transcript_partial / voice: cue is the engaging
  meta: kind=partial | timestamp=1778070645.7688253 | source=vosk | frequency_hz=336.1 | rms=282 | updated_at=1778070644.1864665
- [2026-05-06 20:30:46] operator / voice_transcript_partial / voice: cue is the engaging scope
  meta: kind=partial | timestamp=1778070646.0204055 | source=vosk | frequency_hz=336.1 | rms=282 | updated_at=1778070644.1864665
- [2026-05-06 20:30:46] operator / voice_transcript_final / voice: cue is the engaging
  meta: kind=final | timestamp=1778070646.982437 | source=final | frequency_hz=380.0 | rms=297 | updated_at=1778070646.7715993
- [2026-05-06 20:30:56] operator / voice_transcript_partial / voice: acoustic what e the keep hunting show zone ml
  meta: kind=partial | timestamp=1778070656.5208848 | source=vosk | frequency_hz=338.0 | rms=278 | updated_at=1778070652.513675
- [2026-05-06 20:30:56] operator / voice_transcript_partial / voice: acoustic what e the keyboard shortcuts on no mode suggestions
  meta: kind=partial | timestamp=1778070656.7708905 | source=vosk | frequency_hz=338.0 | rms=278 | updated_at=1778070652.513675
- [2026-05-06 20:30:57] operator / voice_transcript_partial / voice: acoustic what e the keep hunting show zone ml face greeting
  meta: kind=partial | timestamp=1778070657.0345488 | source=vosk | frequency_hz=338.0 | rms=278 | updated_at=1778070652.513675
- [2026-05-06 20:30:58] operator / voice_transcript_final / voice: acoustic what e the keep on show zone ml face greeting
  meta: kind=final | timestamp=1778070658.5682673 | source=final | frequency_hz=340.0 | rms=293 | updated_at=1778070657.770528
- [2026-05-06 20:30:58] operator / voice_transcript_partial / voice: trigger
  meta: kind=partial | timestamp=1778070658.6598418 | source=vosk | frequency_hz=340.0 | rms=293 | updated_at=1778070657.770528
- [2026-05-06 20:30:58] operator / voice_transcript_partial / voice: trigger enabled
  meta: kind=partial | timestamp=1778070658.9206843 | source=vosk | frequency_hz=340.0 | rms=293 | updated_at=1778070657.770528
- [2026-05-06 20:30:59] operator / voice_transcript_partial / voice: trigger
  meta: kind=partial | timestamp=1778070659.8036761 | source=vosk | frequency_hz=294.5 | rms=1065 | updated_at=1778070659.1524036
- [2026-05-06 20:30:59] operator / voice_transcript_final / voice: trigger
  meta: kind=final | timestamp=1778070659.977819 | source=final | frequency_hz=294.5 | rms=1065 | updated_at=1778070659.1524036
- [2026-05-06 20:31:00] operator / voice_transcript_partial / voice: camera feed
  meta: kind=partial | timestamp=1778070660.0744483 | source=vosk | frequency_hz=308.3 | rms=348 | updated_at=1778070660.066926
- [2026-05-06 20:31:00] operator / voice_transcript_partial / voice: camera is
  meta: kind=partial | timestamp=1778070660.5189867 | source=vosk | frequency_hz=308.3 | rms=348 | updated_at=1778070660.066926
- [2026-05-06 20:31:01] operator / voice_transcript_final / voice: camera rest
  meta: kind=final | timestamp=1778070661.2261896 | source=final | frequency_hz=330.2 | rms=286 | updated_at=1778070660.8041594
- [2026-05-06 20:31:01] operator / voice_transcript_partial / voice: give another
  meta: kind=partial | timestamp=1778070661.5608695 | source=vosk | frequency_hz=330.2 | rms=286 | updated_at=1778070660.8041594
- [2026-05-06 20:31:01] operator / voice_transcript_partial / voice: give on
  meta: kind=partial | timestamp=1778070661.8216624 | source=vosk | frequency_hz=330.2 | rms=286 | updated_at=1778070660.8041594
- [2026-05-06 20:31:02] operator / voice_transcript_partial / voice: give on status
  meta: kind=partial | timestamp=1778070662.0792089 | source=vosk | frequency_hz=330.2 | rms=286 | updated_at=1778070660.8041594
- [2026-05-06 20:31:02] operator / voice_transcript_partial / voice: give on stay
  meta: kind=partial | timestamp=1778070662.3126051 | source=vosk | frequency_hz=330.2 | rms=286 | updated_at=1778070660.8041594
- [2026-05-06 20:31:02] operator / voice_transcript_partial / voice: give on stay what
  meta: kind=partial | timestamp=1778070662.5799725 | source=vosk | frequency_hz=330.2 | rms=286 | updated_at=1778070660.8041594
- [2026-05-06 20:31:03] operator / voice_transcript_final / voice: give on stay what
  meta: kind=final | timestamp=1778070663.4094884 | source=final | frequency_hz=333.0 | rms=307 | updated_at=1778070663.3045652

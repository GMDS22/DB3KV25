# SMART SENTRY V5.0.0 Runtime Conversation Export

- Generated: 2026-07-09 08:39:53
- Entries: 360
- Roles: {'assistant': 6, 'system': 257, 'operator': 97}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 257, 'spoken_confirmation': 4, 'voice_transcript_partial': 85, 'voice_transcript_final': 8, 'voice_command': 4}
- Channels: {'text': 2, 'voice': 358}
- Latest operator request: turns the profile to look got speeds five
- Latest assistant message: Verification accepted. Executing now.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-07-09 08:34:47] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-07-09 08:34:47] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-07-09 08:34:50] system / voice_status / voice: listening
  meta: kind=status | timestamp=1783557290.0789082 | source=vosk
- [2026-07-09 08:34:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557299.8318279 | source=vosk | rms=1205 | updated_at=1783557299.8318279
- [2026-07-09 08:35:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557300.3317513 | source=vosk | rms=1205 | updated_at=1783557299.8318279
- [2026-07-09 08:35:25] assistant / spoken_confirmation / voice: Smart Sentry is ready.
  meta: interrupt=True | assistant_output=False | spoken=True
- [2026-07-09 08:35:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557306.5824878 | source=vosk | rms=405 | updated_at=1783557306.5824878
- [2026-07-09 08:35:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557307.333297 | source=vosk | rms=405 | updated_at=1783557306.5824878
- [2026-07-09 08:35:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557307.831648 | source=vosk | rms=965 | updated_at=1783557307.831648
- [2026-07-09 08:35:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557308.5825386 | source=vosk | rms=965 | updated_at=1783557307.831648
- [2026-07-09 08:35:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557309.08164 | source=vosk | rms=965 | updated_at=1783557307.831648
- [2026-07-09 08:35:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557309.584205 | source=vosk | rms=965 | updated_at=1783557307.831648
- [2026-07-09 08:35:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557309.832418 | source=vosk | rms=965 | updated_at=1783557307.831648
- [2026-07-09 08:35:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557310.3332844 | source=vosk | rms=965 | updated_at=1783557307.831648
- [2026-07-09 08:35:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557314.081711 | source=vosk | rms=289 | updated_at=1783557314.081711
- [2026-07-09 08:35:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557314.8334022 | source=vosk | rms=289 | updated_at=1783557314.081711
- [2026-07-09 08:35:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557321.337309 | source=vosk | rms=289 | updated_at=1783557314.081711
- [2026-07-09 08:35:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557321.8323252 | source=vosk | rms=289 | updated_at=1783557314.081711
- [2026-07-09 08:35:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557327.5843794 | source=vosk | rms=289 | updated_at=1783557314.081711
- [2026-07-09 08:35:28] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1783557328.4087691 | source=vosk | rms=499 | updated_at=1783557328.3323636
- [2026-07-09 08:35:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557328.584052 | source=vosk | rms=511 | updated_at=1783557328.584052
- [2026-07-09 08:35:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557328.837377 | source=vosk | rms=337 | updated_at=1783557328.837377
- [2026-07-09 08:35:28] operator / voice_transcript_partial / voice: smart century is
  meta: kind=partial | timestamp=1783557328.9624302 | source=vosk | rms=337 | updated_at=1783557328.837377
- [2026-07-09 08:35:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557329.5822196 | source=vosk | rms=337 | updated_at=1783557328.837377
- [2026-07-09 08:35:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557332.3331301 | source=vosk | rms=127 | updated_at=1783557332.3331301
- [2026-07-09 08:35:32] operator / voice_transcript_partial / voice: smart century is ready
  meta: kind=partial | timestamp=1783557332.367231 | source=vosk | rms=127 | updated_at=1783557332.3331301
- [2026-07-09 08:35:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557332.8321633 | source=vosk | rms=440 | updated_at=1783557332.8321633
- [2026-07-09 08:35:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557333.0822442 | source=vosk | rms=614 | updated_at=1783557333.0822442
- [2026-07-09 08:35:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557333.33229 | source=vosk | rms=226 | updated_at=1783557333.33229
- [2026-07-09 08:35:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557333.5828493 | source=vosk | rms=290 | updated_at=1783557333.5828493 | frequency_hz=208.0
- [2026-07-09 08:35:33] operator / voice_transcript_partial / voice: smart century is ready billion
  meta: kind=partial | timestamp=1783557333.6230004 | source=vosk | rms=290 | updated_at=1783557333.5828493 | frequency_hz=208.0
- [2026-07-09 08:35:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557333.8337016 | source=vosk | rms=1206 | updated_at=1783557333.8337016 | frequency_hz=208.0
- [2026-07-09 08:35:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557334.0824122 | source=vosk | rms=846 | updated_at=1783557334.0824122 | frequency_hz=208.0
- [2026-07-09 08:35:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557334.3338094 | source=vosk | rms=811 | updated_at=1783557334.3338094 | frequency_hz=208.0
- [2026-07-09 08:35:34] operator / voice_transcript_partial / voice: smart century is ready billion run the
  meta: kind=partial | timestamp=1783557334.4667428 | source=vosk | rms=811 | updated_at=1783557334.3338094 | frequency_hz=208.0
- [2026-07-09 08:35:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557334.5836496 | source=vosk | rms=373 | updated_at=1783557334.5836496 | frequency_hz=208.0
- [2026-07-09 08:35:34] operator / voice_transcript_partial / voice: smart century is ready billion run the slots and
  meta: kind=partial | timestamp=1783557334.7254972 | source=vosk | rms=373 | updated_at=1783557334.5836496 | frequency_hz=208.0
- [2026-07-09 08:35:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557335.3324473 | source=vosk | rms=373 | updated_at=1783557334.5836496 | frequency_hz=208.0
- [2026-07-09 08:35:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557340.583635 | source=vosk | rms=176 | updated_at=1783557340.583635 | frequency_hz=360.0
- [2026-07-09 08:35:40] operator / voice_transcript_partial / voice: smart century is ready billion run the stewart
  meta: kind=partial | timestamp=1783557340.6559534 | source=vosk | rms=176 | updated_at=1783557340.583635 | frequency_hz=360.0
- [2026-07-09 08:35:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557341.0839233 | source=vosk | rms=176 | updated_at=1783557340.583635 | frequency_hz=360.0
- [2026-07-09 08:35:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557342.333066 | source=vosk | rms=476 | updated_at=1783557342.333066 | frequency_hz=360.0
- [2026-07-09 08:35:42] operator / voice_transcript_partial / voice: smart century is ready billion run the slots and three
  meta: kind=partial | timestamp=1783557342.3583584 | source=vosk | rms=476 | updated_at=1783557342.333066 | frequency_hz=360.0
- [2026-07-09 08:35:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557342.5895565 | source=vosk | rms=652 | updated_at=1783557342.5895565 | frequency_hz=360.0
- [2026-07-09 08:35:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557342.8334162 | source=vosk | rms=171 | updated_at=1783557342.8329134 | frequency_hz=360.0
- [2026-07-09 08:35:42] operator / voice_transcript_partial / voice: smart century is ready billion run the slots and three billion
  meta: kind=partial | timestamp=1783557342.8724282 | source=vosk | rms=171 | updated_at=1783557342.8329134 | frequency_hz=360.0
- [2026-07-09 08:35:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557343.336715 | source=vosk | rms=171 | updated_at=1783557342.8329134 | frequency_hz=360.0
- [2026-07-09 08:35:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557346.0826068 | source=vosk | rms=1140 | updated_at=1783557346.0826068 | frequency_hz=360.0
- [2026-07-09 08:35:46] operator / voice_transcript_partial / voice: smart century is ready billion run the slots and three bill you
  meta: kind=partial | timestamp=1783557346.0931282 | source=vosk | rms=1140 | updated_at=1783557346.0826068 | frequency_hz=360.0
- [2026-07-09 08:35:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557346.333871 | source=vosk | rms=917 | updated_at=1783557346.333871 | frequency_hz=360.0
- [2026-07-09 08:35:46] operator / voice_transcript_partial / voice: smart century is ready billion run the slots and three billion
  meta: kind=partial | timestamp=1783557346.356137 | source=vosk | rms=917 | updated_at=1783557346.333871 | frequency_hz=360.0
- [2026-07-09 08:35:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557346.583734 | source=vosk | rms=917 | updated_at=1783557346.333871 | frequency_hz=360.0
- [2026-07-09 08:35:46] operator / voice_transcript_partial / voice: smart century is ready billion run the slots and three billion billion
  meta: kind=partial | timestamp=1783557346.6430085 | source=vosk | rms=917 | updated_at=1783557346.333871 | frequency_hz=360.0
- [2026-07-09 08:35:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557347.0833428 | source=vosk | rms=917 | updated_at=1783557346.333871 | frequency_hz=360.0
- [2026-07-09 08:35:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557350.5829115 | source=vosk | rms=742 | updated_at=1783557350.5829115 | frequency_hz=360.0
- [2026-07-09 08:35:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557350.8327315 | source=vosk | rms=634 | updated_at=1783557350.8327315 | frequency_hz=360.0
- [2026-07-09 08:35:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557351.3324728 | source=vosk | rms=634 | updated_at=1783557350.8327315 | frequency_hz=360.0
- [2026-07-09 08:35:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557353.8340514 | source=vosk | rms=894 | updated_at=1783557353.8340514 | frequency_hz=360.0
- [2026-07-09 08:35:53] operator / voice_transcript_partial / voice: smart century is ready billion run the slots and three billion billion billion
  meta: kind=partial | timestamp=1783557353.8531098 | source=vosk | rms=894 | updated_at=1783557353.8340514 | frequency_hz=360.0
- [2026-07-09 08:35:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557354.0826612 | source=vosk | rms=494 | updated_at=1783557354.0826612 | frequency_hz=360.0
- [2026-07-09 08:35:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557354.3322494 | source=vosk | rms=357 | updated_at=1783557354.3322494 | frequency_hz=360.0
- [2026-07-09 08:35:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557354.5861096 | source=vosk | rms=854 | updated_at=1783557354.5861096 | frequency_hz=360.0
- [2026-07-09 08:35:54] operator / voice_transcript_partial / voice: smart century is ready billion run the slots and three billion billion billion run the
  meta: kind=partial | timestamp=1783557354.6330743 | source=vosk | rms=854 | updated_at=1783557354.5861096 | frequency_hz=360.0
- [2026-07-09 08:35:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557354.833279 | source=vosk | rms=264 | updated_at=1783557354.833279 | frequency_hz=360.0
- [2026-07-09 08:35:54] operator / voice_transcript_partial / voice: smart century is ready billion run the slots and three billion billion billion run the smart
  meta: kind=partial | timestamp=1783557354.8503716 | source=vosk | rms=264 | updated_at=1783557354.833279 | frequency_hz=360.0
- [2026-07-09 08:35:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557355.082432 | source=vosk | rms=264 | updated_at=1783557354.833279 | frequency_hz=360.0
- [2026-07-09 08:35:55] operator / voice_transcript_partial / voice: smart century is ready billion run the slots and three billion billion billion run the smart century
  meta: kind=partial | timestamp=1783557355.1530485 | source=vosk | rms=264 | updated_at=1783557354.833279 | frequency_hz=360.0
- [2026-07-09 08:35:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557355.5828443 | source=vosk | rms=264 | updated_at=1783557354.833279 | frequency_hz=360.0
- [2026-07-09 08:35:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557356.8345225 | source=vosk | rms=264 | updated_at=1783557354.833279 | frequency_hz=360.0
- [2026-07-09 08:35:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557357.3326125 | source=vosk | rms=264 | updated_at=1783557354.833279 | frequency_hz=360.0
- [2026-07-09 08:36:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557371.084296 | source=vosk | rms=437 | updated_at=1783557371.084296 | frequency_hz=360.0
- [2026-07-09 08:36:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557371.5827801 | source=vosk | rms=437 | updated_at=1783557371.084296 | frequency_hz=360.0
- [2026-07-09 08:36:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557372.3362415 | source=vosk | rms=514 | updated_at=1783557372.3362415 | frequency_hz=360.0
- [2026-07-09 08:36:13] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1783557373.1899207 | source=final | rms=514 | updated_at=1783557372.3362415 | frequency_hz=360.0
- [2026-07-09 08:36:13] system / voice_status / voice: processing
  meta: kind=status | timestamp=1783557373.2300007 | source=state | rms=514 | updated_at=1783557372.3362415 | frequency_hz=360.0
- [2026-07-09 08:36:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557373.2300007 | source=state | rms=514 | updated_at=1783557372.3362415 | frequency_hz=360.0
- [2026-07-09 08:36:13] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-07-09 08:36:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557373.231002 | source=vosk | rms=514 | updated_at=1783557372.3362415 | frequency_hz=360.0
- [2026-07-09 08:36:13] assistant / spoken_confirmation / voice: Running Smart Sentry now. Connecting the Smart Sentry boards first.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-07-09 08:36:16] operator / voice_transcript_partial / voice: running
  meta: kind=partial | timestamp=1783557376.8381493 | source=vosk | rms=570 | updated_at=1783557376.5842633 | frequency_hz=360.0
- [2026-07-09 08:36:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557376.8381493 | source=vosk | rms=446 | updated_at=1783557376.8381493 | frequency_hz=360.0
- [2026-07-09 08:36:17] operator / voice_transcript_partial / voice: running smart such
  meta: kind=partial | timestamp=1783557377.11529 | source=vosk | rms=443 | updated_at=1783557377.08308 | frequency_hz=360.0
- [2026-07-09 08:36:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557377.5835164 | source=vosk | rms=265 | updated_at=1783557377.5835164 | frequency_hz=360.0
- [2026-07-09 08:36:17] operator / voice_transcript_partial / voice: running smart century
  meta: kind=partial | timestamp=1783557377.6708372 | source=vosk | rms=265 | updated_at=1783557377.5835164 | frequency_hz=360.0
- [2026-07-09 08:36:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557377.8331766 | source=vosk | rms=1159 | updated_at=1783557377.8331766 | frequency_hz=360.0
- [2026-07-09 08:36:17] operator / voice_transcript_partial / voice: running smart century now
  meta: kind=partial | timestamp=1783557377.8654273 | source=vosk | rms=1159 | updated_at=1783557377.8331766 | frequency_hz=360.0
- [2026-07-09 08:36:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557378.0829992 | source=vosk | rms=597 | updated_at=1783557378.0829992 | frequency_hz=360.0
- [2026-07-09 08:36:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557378.3430676 | source=vosk | rms=748 | updated_at=1783557378.3430676 | frequency_hz=360.0
- [2026-07-09 08:36:18] operator / voice_transcript_partial / voice: running smart century now connecting the
  meta: kind=partial | timestamp=1783557378.3894737 | source=vosk | rms=748 | updated_at=1783557378.3430676 | frequency_hz=360.0
- [2026-07-09 08:36:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557378.5852091 | source=vosk | rms=907 | updated_at=1783557378.5852091 | frequency_hz=360.0
- [2026-07-09 08:36:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557378.8341978 | source=vosk | rms=368 | updated_at=1783557378.8341978 | frequency_hz=360.0
- [2026-07-09 08:36:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557379.0855982 | source=vosk | rms=307 | updated_at=1783557379.0855982 | frequency_hz=360.0
- [2026-07-09 08:36:19] operator / voice_transcript_partial / voice: running smart century now connecting the market
  meta: kind=partial | timestamp=1783557379.1577911 | source=vosk | rms=307 | updated_at=1783557379.0855982 | frequency_hz=360.0
- [2026-07-09 08:36:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557379.3335924 | source=vosk | rms=496 | updated_at=1783557379.3335924 | frequency_hz=360.0
- [2026-07-09 08:36:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557379.5854895 | source=vosk | rms=308 | updated_at=1783557379.5854895 | frequency_hz=360.0
- [2026-07-09 08:36:19] operator / voice_transcript_partial / voice: running smart century now connecting the market reports
  meta: kind=partial | timestamp=1783557379.617343 | source=vosk | rms=308 | updated_at=1783557379.5854895 | frequency_hz=360.0
- [2026-07-09 08:36:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557379.8335562 | source=vosk | rms=145 | updated_at=1783557379.8335562 | frequency_hz=360.0
- [2026-07-09 08:36:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557380.0856323 | source=vosk | rms=238 | updated_at=1783557380.0846226 | frequency_hz=360.0
- [2026-07-09 08:36:20] operator / voice_transcript_partial / voice: running smart century now connecting the market reports first
  meta: kind=partial | timestamp=1783557380.1066973 | source=vosk | rms=238 | updated_at=1783557380.0846226 | frequency_hz=360.0
- [2026-07-09 08:36:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557380.336346 | source=vosk | rms=373 | updated_at=1783557380.336346 | frequency_hz=360.0
- [2026-07-09 08:36:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557380.5834317 | source=vosk | rms=340 | updated_at=1783557380.5834317 | frequency_hz=360.0
- [2026-07-09 08:36:20] operator / voice_transcript_final / voice: running smart sentry now connecting this market reports first
  meta: kind=final | timestamp=1783557380.9944727 | source=final | rms=340 | updated_at=1783557380.5834317 | frequency_hz=360.0
- [2026-07-09 08:36:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557381.1480055 | source=vosk | rms=340 | updated_at=1783557380.5834317 | frequency_hz=360.0
- [2026-07-09 08:36:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557381.1480055 | source=vosk | rms=169 | updated_at=1783557381.1480055 | frequency_hz=360.0
- [2026-07-09 08:36:22] operator / voice_transcript_partial / voice: smart century
  meta: kind=partial | timestamp=1783557382.092962 | source=vosk | rms=993 | updated_at=1783557382.0833738 | frequency_hz=360.0
- [2026-07-09 08:36:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557382.3337889 | source=vosk | rms=463 | updated_at=1783557382.3337889 | frequency_hz=360.0
- [2026-07-09 08:36:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557382.5880432 | source=vosk | rms=618 | updated_at=1783557382.5880432 | frequency_hz=360.0
- [2026-07-09 08:36:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557382.8327408 | source=vosk | rms=333 | updated_at=1783557382.8327408 | frequency_hz=360.0
- [2026-07-09 08:36:22] operator / voice_transcript_partial / voice: smart century or
  meta: kind=partial | timestamp=1783557382.8590066 | source=vosk | rms=333 | updated_at=1783557382.8327408 | frequency_hz=360.0
- [2026-07-09 08:36:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557383.083355 | source=vosk | rms=274 | updated_at=1783557383.083355 | frequency_hz=360.0
- [2026-07-09 08:36:23] operator / voice_transcript_partial / voice: smart century parts are
  meta: kind=partial | timestamp=1783557383.1035218 | source=vosk | rms=274 | updated_at=1783557383.083355 | frequency_hz=360.0
- [2026-07-09 08:36:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557383.333612 | source=vosk | rms=501 | updated_at=1783557383.333612 | frequency_hz=360.0
- [2026-07-09 08:36:23] operator / voice_transcript_partial / voice: smart century parts are connected on
  meta: kind=partial | timestamp=1783557383.3506665 | source=vosk | rms=501 | updated_at=1783557383.333612 | frequency_hz=360.0
- [2026-07-09 08:36:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557383.5831935 | source=vosk | rms=599 | updated_at=1783557383.5831935 | frequency_hz=360.0
- [2026-07-09 08:36:23] operator / voice_transcript_partial / voice: smart century parts are connected
  meta: kind=partial | timestamp=1783557383.6286225 | source=vosk | rms=599 | updated_at=1783557383.5831935 | frequency_hz=360.0
- [2026-07-09 08:36:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557383.832992 | source=vosk | rms=562 | updated_at=1783557383.832992 | frequency_hz=360.0
- [2026-07-09 08:36:23] operator / voice_transcript_partial / voice: smart century parts are connected on the
  meta: kind=partial | timestamp=1783557383.8517997 | source=vosk | rms=562 | updated_at=1783557383.832992 | frequency_hz=360.0
- [2026-07-09 08:36:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557384.0836313 | source=vosk | rms=266 | updated_at=1783557384.0836313 | frequency_hz=360.0
- [2026-07-09 08:36:24] operator / voice_transcript_partial / voice: smart century parts are connected on the ceo
  meta: kind=partial | timestamp=1783557384.1388192 | source=vosk | rms=266 | updated_at=1783557384.0836313 | frequency_hz=360.0
- [2026-07-09 08:36:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557384.3329487 | source=vosk | rms=235 | updated_at=1783557384.3329487 | frequency_hz=360.0
- [2026-07-09 08:36:24] operator / voice_transcript_partial / voice: smart century parts are connected on the c o m
  meta: kind=partial | timestamp=1783557384.463694 | source=vosk | rms=235 | updated_at=1783557384.3329487 | frequency_hz=360.0
- [2026-07-09 08:36:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557384.5829744 | source=vosk | rms=644 | updated_at=1783557384.5829744 | frequency_hz=360.0
- [2026-07-09 08:36:24] operator / voice_transcript_partial / voice: smart century parts are connected on the c o m link
  meta: kind=partial | timestamp=1783557384.5990076 | source=vosk | rms=644 | updated_at=1783557384.5829744 | frequency_hz=360.0
- [2026-07-09 08:36:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557384.834375 | source=vosk | rms=695 | updated_at=1783557384.834375 | frequency_hz=360.0
- [2026-07-09 08:36:24] operator / voice_transcript_partial / voice: smart century parts are connected on the c o m like i
  meta: kind=partial | timestamp=1783557384.8797035 | source=vosk | rms=695 | updated_at=1783557384.834375 | frequency_hz=360.0
- [2026-07-09 08:36:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557385.0832849 | source=vosk | rms=517 | updated_at=1783557385.0832849 | frequency_hz=360.0
- [2026-07-09 08:36:25] operator / voice_transcript_partial / voice: smart century parts are connected on the c o m link
  meta: kind=partial | timestamp=1783557385.1263607 | source=vosk | rms=517 | updated_at=1783557385.0832849 | frequency_hz=360.0
- [2026-07-09 08:36:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557385.3335552 | source=vosk | rms=513 | updated_at=1783557385.3335552 | frequency_hz=360.0
- [2026-07-09 08:36:25] operator / voice_transcript_partial / voice: smart century parts are connected on the c o m link smart
  meta: kind=partial | timestamp=1783557385.3410642 | source=vosk | rms=513 | updated_at=1783557385.3335552 | frequency_hz=360.0
- [2026-07-09 08:36:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557385.584476 | source=vosk | rms=484 | updated_at=1783557385.584476 | frequency_hz=360.0
- [2026-07-09 08:36:25] operator / voice_transcript_partial / voice: smart century parts are connected on the c o m link smart centric
  meta: kind=partial | timestamp=1783557385.603039 | source=vosk | rms=484 | updated_at=1783557385.584476 | frequency_hz=360.0
- [2026-07-09 08:36:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557385.8379009 | source=vosk | rms=237 | updated_at=1783557385.8379009 | frequency_hz=360.0
- [2026-07-09 08:36:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557386.0839584 | source=vosk | rms=237 | updated_at=1783557385.8379009 | frequency_hz=360.0
- [2026-07-09 08:36:26] operator / voice_transcript_partial / voice: smart century parts are connected on the c o m link smart centric is unable
  meta: kind=partial | timestamp=1783557386.11103 | source=vosk | rms=237 | updated_at=1783557385.8379009 | frequency_hz=360.0
- [2026-07-09 08:36:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557386.3333845 | source=vosk | rms=182 | updated_at=1783557386.3333845 | frequency_hz=360.0
- [2026-07-09 08:36:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557386.583036 | source=vosk | rms=322 | updated_at=1783557386.583036 | frequency_hz=360.0
- [2026-07-09 08:36:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557386.8331604 | source=vosk | rms=1204 | updated_at=1783557386.8331604 | frequency_hz=360.0
- [2026-07-09 08:36:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557387.0840127 | source=vosk | rms=597 | updated_at=1783557387.0840127 | frequency_hz=360.0
- [2026-07-09 08:36:27] operator / voice_transcript_partial / voice: smart century parts are connected on the c o m link smart centric is an evil
  meta: kind=partial | timestamp=1783557387.1725764 | source=vosk | rms=597 | updated_at=1783557387.0840127 | frequency_hz=360.0
- [2026-07-09 08:36:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557387.336423 | source=vosk | rms=721 | updated_at=1783557387.336423 | frequency_hz=360.0
- [2026-07-09 08:36:27] operator / voice_transcript_partial / voice: smart century parts are connected on the c o m link smart centric is unable to ask
  meta: kind=partial | timestamp=1783557387.3582156 | source=vosk | rms=721 | updated_at=1783557387.336423 | frequency_hz=360.0
- [2026-07-09 08:36:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557387.5829985 | source=vosk | rms=642 | updated_at=1783557387.5829985 | frequency_hz=360.0
- [2026-07-09 08:36:27] operator / voice_transcript_partial / voice: smart century parts are connected on the c o m link smart centric is unable to ask another
  meta: kind=partial | timestamp=1783557387.604555 | source=vosk | rms=642 | updated_at=1783557387.5829985 | frequency_hz=360.0
- [2026-07-09 08:36:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557387.8336701 | source=vosk | rms=531 | updated_at=1783557387.8336701 | frequency_hz=360.0
- [2026-07-09 08:36:27] operator / voice_transcript_partial / voice: smart century parts are connected on the c o m link smart centric is unable to ask another question
  meta: kind=partial | timestamp=1783557387.8770523 | source=vosk | rms=531 | updated_at=1783557387.8336701 | frequency_hz=360.0
- [2026-07-09 08:36:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557388.0888886 | source=vosk | rms=137 | updated_at=1783557388.0888886 | frequency_hz=360.0
- [2026-07-09 08:36:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557388.3411217 | source=vosk | rms=597 | updated_at=1783557388.3411217 | frequency_hz=360.0
- [2026-07-09 08:36:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557388.584837 | source=vosk | rms=971 | updated_at=1783557388.584837 | frequency_hz=360.0
- [2026-07-09 08:36:28] operator / voice_transcript_partial / voice: smart century parts are connected on the c o m link smart centric is unable to ask another question or
  meta: kind=partial | timestamp=1783557388.5953522 | source=vosk | rms=971 | updated_at=1783557388.584837 | frequency_hz=360.0
- [2026-07-09 08:36:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557388.833561 | source=vosk | rms=587 | updated_at=1783557388.833561 | frequency_hz=360.0
- [2026-07-09 08:36:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557389.0834427 | source=vosk | rms=560 | updated_at=1783557389.0834427 | frequency_hz=360.0
- [2026-07-09 08:36:29] operator / voice_transcript_partial / voice: smart century parts are connected on the c o m link smart centric is unable to ask another question or give another
  meta: kind=partial | timestamp=1783557389.109982 | source=vosk | rms=560 | updated_at=1783557389.0834427 | frequency_hz=360.0
- [2026-07-09 08:36:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557389.3333023 | source=vosk | rms=323 | updated_at=1783557389.3333023 | frequency_hz=360.0
- [2026-07-09 08:36:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557389.5916862 | source=vosk | rms=535 | updated_at=1783557389.5916862 | frequency_hz=360.0
- [2026-07-09 08:36:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557389.8328764 | source=vosk | rms=238 | updated_at=1783557389.8328764 | frequency_hz=360.0
- [2026-07-09 08:36:29] operator / voice_transcript_partial / voice: smart century parts are connected on the c o m link smart centric is unable to ask another question or give another command would
  meta: kind=partial | timestamp=1783557389.8912115 | source=vosk | rms=238 | updated_at=1783557389.8328764 | frequency_hz=360.0
- [2026-07-09 08:36:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557390.3337107 | source=vosk | rms=687 | updated_at=1783557390.3337107 | frequency_hz=360.0
- [2026-07-09 08:36:30] operator / voice_transcript_partial / voice: smart century parts are connected on the c o m link smart centric is unable to ask another question or give another command with
  meta: kind=partial | timestamp=1783557390.3835676 | source=vosk | rms=687 | updated_at=1783557390.3337107 | frequency_hz=360.0
- [2026-07-09 08:36:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557390.5917192 | source=vosk | rms=485 | updated_at=1783557390.5917192 | frequency_hz=360.0
- [2026-07-09 08:36:30] operator / voice_transcript_partial / voice: smart century parts are connected on the c o m link smart centric is unable to ask another question or give another command with ready
  meta: kind=partial | timestamp=1783557390.6217792 | source=vosk | rms=485 | updated_at=1783557390.5917192 | frequency_hz=360.0
- [2026-07-09 08:36:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557390.8335688 | source=vosk | rms=748 | updated_at=1783557390.8335688 | frequency_hz=360.0
- [2026-07-09 08:36:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557391.0840542 | source=vosk | rms=402 | updated_at=1783557391.0840542 | frequency_hz=360.0
- [2026-07-09 08:36:31] operator / voice_transcript_final / voice: connect boards
  meta: kind=final | timestamp=1783557391.1117666 | source=final | rms=402 | updated_at=1783557391.0840542 | frequency_hz=360.0
- [2026-07-09 08:36:31] system / voice_status / voice: processing
  meta: kind=status | timestamp=1783557391.1553836 | source=state | rms=402 | updated_at=1783557391.0840542 | frequency_hz=360.0
- [2026-07-09 08:36:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557391.1553836 | source=state | rms=402 | updated_at=1783557391.0840542 | frequency_hz=360.0
- [2026-07-09 08:36:31] operator / voice_command / voice: connect boards
  meta: normalized=True
- [2026-07-09 08:36:31] assistant / spoken_confirmation / voice: Smart Sentry is already connected and enabled.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-07-09 08:36:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557391.584562 | source=vosk | rms=630 | updated_at=1783557391.584562 | frequency_hz=360.0
- [2026-07-09 08:36:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557392.0829456 | source=vosk | rms=630 | updated_at=1783557391.584562 | frequency_hz=360.0
- [2026-07-09 08:36:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557392.3335626 | source=vosk | rms=630 | updated_at=1783557391.584562 | frequency_hz=360.0
- [2026-07-09 08:36:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557392.8340383 | source=vosk | rms=630 | updated_at=1783557391.584562 | frequency_hz=360.0
- [2026-07-09 08:36:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557393.3338308 | source=vosk | rms=371 | updated_at=1783557393.3338308 | frequency_hz=360.0
- [2026-07-09 08:36:34] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1783557394.3436186 | source=vosk | rms=443 | updated_at=1783557394.334605 | frequency_hz=360.0
- [2026-07-09 08:36:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557394.5845957 | source=vosk | rms=814 | updated_at=1783557394.5845957 | frequency_hz=360.0
- [2026-07-09 08:36:34] operator / voice_transcript_partial / voice: smart center is
  meta: kind=partial | timestamp=1783557394.6066768 | source=vosk | rms=814 | updated_at=1783557394.5845957 | frequency_hz=360.0
- [2026-07-09 08:36:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557394.8333762 | source=vosk | rms=371 | updated_at=1783557394.8333762 | frequency_hz=360.0
- [2026-07-09 08:36:34] operator / voice_transcript_partial / voice: smart center is already
  meta: kind=partial | timestamp=1783557394.8616102 | source=vosk | rms=371 | updated_at=1783557394.8333762 | frequency_hz=360.0
- [2026-07-09 08:36:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557395.0836806 | source=vosk | rms=496 | updated_at=1783557395.0836806 | frequency_hz=360.0
- [2026-07-09 08:36:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557395.333892 | source=vosk | rms=496 | updated_at=1783557395.0836806 | frequency_hz=360.0
- [2026-07-09 08:36:35] operator / voice_transcript_partial / voice: smart center is already connected
  meta: kind=partial | timestamp=1783557395.34692 | source=vosk | rms=496 | updated_at=1783557395.0836806 | frequency_hz=360.0
- [2026-07-09 08:36:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557395.586523 | source=vosk | rms=496 | updated_at=1783557395.0836806 | frequency_hz=360.0
- [2026-07-09 08:36:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557396.0837271 | source=vosk | rms=496 | updated_at=1783557395.0836806 | frequency_hz=360.0
- [2026-07-09 08:36:37] operator / voice_transcript_final / voice: smart center is already connect
  meta: kind=final | timestamp=1783557397.8406765 | source=final | rms=496 | updated_at=1783557395.0836806 | frequency_hz=360.0
- [2026-07-09 08:36:38] system / voice_status / voice: processing
  meta: kind=status | timestamp=1783557398.9946048 | source=state | rms=496 | updated_at=1783557395.0836806 | frequency_hz=360.0
- [2026-07-09 08:36:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557398.9961085 | source=state | rms=496 | updated_at=1783557395.0836806 | frequency_hz=360.0
- [2026-07-09 08:36:39] operator / voice_command / voice: smart center is already connect
  meta: normalized=True
- [2026-07-09 08:36:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557398.9961085 | source=vosk | rms=496 | updated_at=1783557395.0836806 | frequency_hz=360.0
- [2026-07-09 08:36:39] operator / voice_transcript_partial / voice: smart center is already connected and
  meta: kind=partial | timestamp=1783557399.0326614 | source=vosk | rms=496 | updated_at=1783557395.0836806 | frequency_hz=360.0
- [2026-07-09 08:36:39] operator / voice_transcript_partial / voice: smart center is already connected and an eight
  meta: kind=partial | timestamp=1783557399.1056569 | source=vosk | rms=785 | updated_at=1783557399.0336623 | frequency_hz=360.0
- [2026-07-09 08:36:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557399.593728 | source=vosk | rms=550 | updated_at=1783557399.593728 | frequency_hz=360.0
- [2026-07-09 08:36:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557399.8431637 | source=vosk | rms=550 | updated_at=1783557399.593728 | frequency_hz=360.0
- [2026-07-09 08:36:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557400.3458767 | source=vosk | rms=415 | updated_at=1783557400.3458767 | frequency_hz=360.0
- [2026-07-09 08:36:40] operator / voice_transcript_final / voice: smart center is already connect and an eight
  meta: kind=final | timestamp=1783557400.6934905 | source=final | rms=415 | updated_at=1783557400.3458767 | frequency_hz=360.0
- [2026-07-09 08:36:41] system / voice_status / voice: processing
  meta: kind=status | timestamp=1783557401.4420052 | source=state | rms=415 | updated_at=1783557400.3458767 | frequency_hz=360.0
- [2026-07-09 08:36:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557401.4507952 | source=state | rms=415 | updated_at=1783557400.3458767 | frequency_hz=360.0
- [2026-07-09 08:36:41] operator / voice_command / voice: smart center is already connect and an eight
  meta: normalized=True
- [2026-07-09 08:36:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557401.4517958 | source=vosk | rms=754 | updated_at=1783557401.4517958 | frequency_hz=360.0
- [2026-07-09 08:36:41] assistant / spoken_confirmation / voice: Verification accepted. Executing now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-07-09 08:36:41] system / voice_status / voice: listening
  meta: kind=status | timestamp=1783557401.891965 | source=state | rms=478 | updated_at=1783557401.8431103 | frequency_hz=360.0
- [2026-07-09 08:36:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557401.8431103 | source=vosk | rms=478 | updated_at=1783557401.8431103 | frequency_hz=360.0
- [2026-07-09 08:36:43] operator / voice_transcript_partial / voice: verification
  meta: kind=partial | timestamp=1783557403.6249135 | source=vosk | rms=741 | updated_at=1783557403.5933874 | frequency_hz=360.0
- [2026-07-09 08:36:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557403.8434663 | source=vosk | rms=741 | updated_at=1783557403.5933874 | frequency_hz=360.0
- [2026-07-09 08:36:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557404.0937939 | source=vosk | rms=522 | updated_at=1783557404.0937939 | frequency_hz=360.0
- [2026-07-09 08:36:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557404.3442607 | source=vosk | rms=522 | updated_at=1783557404.0937939 | frequency_hz=360.0
- [2026-07-09 08:36:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557404.593967 | source=vosk | rms=1040 | updated_at=1783557404.593967 | frequency_hz=360.0
- [2026-07-09 08:36:44] operator / voice_transcript_partial / voice: verification except
  meta: kind=partial | timestamp=1783557404.613492 | source=vosk | rms=1040 | updated_at=1783557404.593967 | frequency_hz=360.0
- [2026-07-09 08:36:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557404.8494878 | source=vosk | rms=474 | updated_at=1783557404.8494878 | frequency_hz=360.0
- [2026-07-09 08:36:44] operator / voice_transcript_partial / voice: verification accepted
  meta: kind=partial | timestamp=1783557404.8605072 | source=vosk | rms=474 | updated_at=1783557404.8494878 | frequency_hz=360.0
- [2026-07-09 08:36:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557405.0934887 | source=vosk | rms=474 | updated_at=1783557404.8494878 | frequency_hz=360.0
- [2026-07-09 08:36:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557405.3431182 | source=vosk | rms=607 | updated_at=1783557405.3431182 | frequency_hz=360.0
- [2026-07-09 08:36:45] operator / voice_transcript_partial / voice: verification accepted execute
  meta: kind=partial | timestamp=1783557405.360811 | source=vosk | rms=607 | updated_at=1783557405.3431182 | frequency_hz=360.0
- [2026-07-09 08:36:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557406.0934744 | source=vosk | rms=607 | updated_at=1783557405.3431182 | frequency_hz=360.0
- [2026-07-09 08:36:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557406.5947194 | source=vosk | rms=727 | updated_at=1783557406.5947194 | frequency_hz=360.0
- [2026-07-09 08:36:46] operator / voice_transcript_partial / voice: verification accepted execute now
  meta: kind=partial | timestamp=1783557406.6102521 | source=vosk | rms=727 | updated_at=1783557406.5947194 | frequency_hz=360.0
- [2026-07-09 08:36:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557406.844906 | source=vosk | rms=760 | updated_at=1783557406.844906 | frequency_hz=360.0
- [2026-07-09 08:36:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557407.0936632 | source=vosk | rms=626 | updated_at=1783557407.0936632 | frequency_hz=360.0
- [2026-07-09 08:36:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557407.5933883 | source=vosk | rms=626 | updated_at=1783557407.0936632 | frequency_hz=360.0
- [2026-07-09 08:36:48] operator / voice_transcript_final / voice: verification accepted execute now
  meta: kind=final | timestamp=1783557408.750085 | source=final | rms=626 | updated_at=1783557407.0936632 | frequency_hz=360.0
- [2026-07-09 08:36:51] system / voice_status / voice: processing
  meta: kind=status | timestamp=1783557411.5943117 | source=state | rms=626 | updated_at=1783557407.0936632 | frequency_hz=360.0
- [2026-07-09 08:36:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557411.5953164 | source=state | rms=626 | updated_at=1783557407.0936632 | frequency_hz=360.0
- [2026-07-09 08:36:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557413.8446717 | source=vosk | rms=626 | updated_at=1783557407.0936632 | frequency_hz=360.0
- [2026-07-09 08:36:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557415.3441908 | source=vosk | rms=626 | updated_at=1783557407.0936632 | frequency_hz=360.0
- [2026-07-09 08:37:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557423.0936582 | source=vosk | rms=564 | updated_at=1783557423.0936582 | frequency_hz=360.0
- [2026-07-09 08:37:03] operator / voice_transcript_partial / voice: can you
  meta: kind=partial | timestamp=1783557423.685279 | source=vosk | rms=610 | updated_at=1783557423.5936246 | frequency_hz=360.0
- [2026-07-09 08:37:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557424.0941687 | source=vosk | rms=610 | updated_at=1783557423.5936246 | frequency_hz=360.0
- [2026-07-09 08:37:04] operator / voice_transcript_partial / voice: can you teach
  meta: kind=partial | timestamp=1783557424.3735542 | source=vosk | rms=875 | updated_at=1783557424.3438823 | frequency_hz=360.0
- [2026-07-09 08:37:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557424.5987606 | source=vosk | rms=619 | updated_at=1783557424.5987606 | frequency_hz=360.0
- [2026-07-09 08:37:04] operator / voice_transcript_partial / voice: can you teach the
  meta: kind=partial | timestamp=1783557424.6152902 | source=vosk | rms=619 | updated_at=1783557424.5987606 | frequency_hz=360.0
- [2026-07-09 08:37:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557424.8441622 | source=vosk | rms=619 | updated_at=1783557424.5987606 | frequency_hz=360.0
- [2026-07-09 08:37:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557425.0933354 | source=vosk | rms=695 | updated_at=1783557425.0933354 | frequency_hz=360.0
- [2026-07-09 08:37:05] operator / voice_transcript_partial / voice: can you teach the profile to
  meta: kind=partial | timestamp=1783557425.1053557 | source=vosk | rms=695 | updated_at=1783557425.0933354 | frequency_hz=360.0
- [2026-07-09 08:37:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557425.343563 | source=vosk | rms=695 | updated_at=1783557425.0933354 | frequency_hz=360.0
- [2026-07-09 08:37:05] operator / voice_transcript_partial / voice: can you teach the profile to cut
  meta: kind=partial | timestamp=1783557425.3592856 | source=vosk | rms=695 | updated_at=1783557425.0933354 | frequency_hz=360.0
- [2026-07-09 08:37:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557425.5940762 | source=vosk | rms=341 | updated_at=1783557425.5940762 | frequency_hz=360.0
- [2026-07-09 08:37:05] operator / voice_transcript_partial / voice: can you teach the profile took up golf
  meta: kind=partial | timestamp=1783557425.650295 | source=vosk | rms=341 | updated_at=1783557425.5940762 | frequency_hz=360.0
- [2026-07-09 08:37:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557425.8436592 | source=vosk | rms=535 | updated_at=1783557425.8436592 | frequency_hz=360.0
- [2026-07-09 08:37:05] operator / voice_transcript_partial / voice: can you teach the profile to cut programs
  meta: kind=partial | timestamp=1783557425.902622 | source=vosk | rms=535 | updated_at=1783557425.8436592 | frequency_hz=360.0
- [2026-07-09 08:37:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557426.0973961 | source=vosk | rms=784 | updated_at=1783557426.0973961 | frequency_hz=360.0
- [2026-07-09 08:37:06] operator / voice_transcript_partial / voice: can you teach the profile took up bro bro
  meta: kind=partial | timestamp=1783557426.1349876 | source=vosk | rms=784 | updated_at=1783557426.0973961 | frequency_hz=360.0
- [2026-07-09 08:37:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557426.3441448 | source=vosk | rms=1089 | updated_at=1783557426.3441448 | frequency_hz=360.0
- [2026-07-09 08:37:06] operator / voice_transcript_partial / voice: can you teach the profile to curb corporate
  meta: kind=partial | timestamp=1783557426.372071 | source=vosk | rms=1089 | updated_at=1783557426.3441448 | frequency_hz=360.0
- [2026-07-09 08:37:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557426.5942497 | source=vosk | rms=511 | updated_at=1783557426.5942497 | frequency_hz=360.0
- [2026-07-09 08:37:06] operator / voice_transcript_partial / voice: can you teach the profile to cut pro growth
  meta: kind=partial | timestamp=1783557426.610271 | source=vosk | rms=511 | updated_at=1783557426.5942497 | frequency_hz=360.0
- [2026-07-09 08:37:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557426.8435361 | source=vosk | rms=361 | updated_at=1783557426.8435361 | frequency_hz=360.0
- [2026-07-09 08:37:06] operator / voice_transcript_partial / voice: can you teach the profile took up the word spread
  meta: kind=partial | timestamp=1783557426.8692293 | source=vosk | rms=361 | updated_at=1783557426.8435361 | frequency_hz=360.0
- [2026-07-09 08:37:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557427.343975 | source=vosk | rms=361 | updated_at=1783557426.8435361 | frequency_hz=360.0
- [2026-07-09 08:37:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557435.8489215 | source=vosk | rms=338 | updated_at=1783557435.8489215 | frequency_hz=354.0
- [2026-07-09 08:37:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557436.0936546 | source=vosk | rms=688 | updated_at=1783557436.0936546 | frequency_hz=354.0
- [2026-07-09 08:37:16] operator / voice_transcript_partial / voice: can you teach the profile took up the word spread vibe
  meta: kind=partial | timestamp=1783557436.1101851 | source=vosk | rms=688 | updated_at=1783557436.0936546 | frequency_hz=354.0
- [2026-07-09 08:37:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557436.3445194 | source=vosk | rms=469 | updated_at=1783557436.3445194 | frequency_hz=354.0
- [2026-07-09 08:37:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557436.8437204 | source=vosk | rms=469 | updated_at=1783557436.3445194 | frequency_hz=354.0
- [2026-07-09 08:37:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557438.8439817 | source=vosk | rms=504 | updated_at=1783557438.8439817 | frequency_hz=354.0
- [2026-07-09 08:37:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557439.3454876 | source=vosk | rms=327 | updated_at=1783557439.3454876 | frequency_hz=354.0
- [2026-07-09 08:37:19] operator / voice_transcript_partial / voice: can you teach the profile took up the word spread five billion
  meta: kind=partial | timestamp=1783557439.4010973 | source=vosk | rms=327 | updated_at=1783557439.3454876 | frequency_hz=354.0
- [2026-07-09 08:37:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557439.5951002 | source=vosk | rms=1201 | updated_at=1783557439.5951002 | frequency_hz=354.0
- [2026-07-09 08:37:19] operator / voice_transcript_partial / voice: can you teach the profile took up the word spread vibe you
  meta: kind=partial | timestamp=1783557439.6171443 | source=vosk | rms=1201 | updated_at=1783557439.5951002 | frequency_hz=354.0
- [2026-07-09 08:37:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557439.8438337 | source=vosk | rms=402 | updated_at=1783557439.8438337 | frequency_hz=354.0
- [2026-07-09 08:37:19] operator / voice_transcript_partial / voice: can you teach the profile took up the word spread vibe to it
  meta: kind=partial | timestamp=1783557439.8964653 | source=vosk | rms=402 | updated_at=1783557439.8438337 | frequency_hz=354.0
- [2026-07-09 08:37:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557440.0936918 | source=vosk | rms=377 | updated_at=1783557440.0936918 | frequency_hz=354.0
- [2026-07-09 08:37:20] operator / voice_transcript_partial / voice: can you teach the profile took up the word spread vibe you change the
  meta: kind=partial | timestamp=1783557440.1890182 | source=vosk | rms=377 | updated_at=1783557440.0936918 | frequency_hz=354.0
- [2026-07-09 08:37:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557440.3445582 | source=vosk | rms=496 | updated_at=1783557440.3445582 | frequency_hz=354.0
- [2026-07-09 08:37:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557440.5950978 | source=vosk | rms=538 | updated_at=1783557440.5950978 | frequency_hz=354.0
- [2026-07-09 08:37:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557440.8453395 | source=vosk | rms=626 | updated_at=1783557440.8453395 | frequency_hz=354.0
- [2026-07-09 08:37:20] operator / voice_transcript_partial / voice: can you teach the profile took up the word spread vibe you change the profile
  meta: kind=partial | timestamp=1783557440.8664916 | source=vosk | rms=626 | updated_at=1783557440.8453395 | frequency_hz=354.0
- [2026-07-09 08:37:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557441.0945878 | source=vosk | rms=254 | updated_at=1783557441.0945878 | frequency_hz=354.0
- [2026-07-09 08:37:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557441.593979 | source=vosk | rms=254 | updated_at=1783557441.0945878 | frequency_hz=354.0
- [2026-07-09 08:37:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557451.1339302 | source=vosk | rms=333 | updated_at=1783557451.1339302 | frequency_hz=354.0
- [2026-07-09 08:37:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557451.634663 | source=vosk | rms=333 | updated_at=1783557451.1339302 | frequency_hz=354.0
- [2026-07-09 08:37:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557452.8839061 | source=vosk | rms=596 | updated_at=1783557452.8839061 | frequency_hz=354.0
- [2026-07-09 08:37:33] operator / voice_transcript_final / voice: can you judge the profile took up the word spread vibe you change the profile
  meta: kind=final | timestamp=1783557453.2025886 | source=final | rms=596 | updated_at=1783557452.8839061 | frequency_hz=354.0
- [2026-07-09 08:37:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557453.482972 | source=vosk | rms=596 | updated_at=1783557452.8839061 | frequency_hz=354.0
- [2026-07-09 08:37:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557453.482972 | source=vosk | rms=1010 | updated_at=1783557453.482972 | frequency_hz=354.0
- [2026-07-09 08:37:33] operator / voice_transcript_partial / voice: during the
  meta: kind=partial | timestamp=1783557453.5103455 | source=vosk | rms=282 | updated_at=1783557453.4889793 | frequency_hz=354.0
- [2026-07-09 08:37:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557453.8859324 | source=vosk | rms=168 | updated_at=1783557453.8859324 | frequency_hz=354.0
- [2026-07-09 08:37:33] operator / voice_transcript_partial / voice: turns the
  meta: kind=partial | timestamp=1783557453.8995628 | source=vosk | rms=168 | updated_at=1783557453.8859324 | frequency_hz=354.0
- [2026-07-09 08:37:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557454.1392388 | source=vosk | rms=168 | updated_at=1783557453.8859324 | frequency_hz=354.0
- [2026-07-09 08:37:34] operator / voice_transcript_partial / voice: turns the profile
  meta: kind=partial | timestamp=1783557454.14942 | source=vosk | rms=168 | updated_at=1783557453.8859324 | frequency_hz=354.0
- [2026-07-09 08:37:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557454.384421 | source=vosk | rms=328 | updated_at=1783557454.384421 | frequency_hz=354.0
- [2026-07-09 08:37:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557454.6347158 | source=vosk | rms=319 | updated_at=1783557454.6347158 | frequency_hz=354.0
- [2026-07-09 08:37:34] operator / voice_transcript_partial / voice: turns the profile to work
  meta: kind=partial | timestamp=1783557454.648265 | source=vosk | rms=319 | updated_at=1783557454.6347158 | frequency_hz=354.0
- [2026-07-09 08:37:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557454.8848507 | source=vosk | rms=323 | updated_at=1783557454.8848507 | frequency_hz=354.0
- [2026-07-09 08:37:34] operator / voice_transcript_partial / voice: turns the profile to work though
  meta: kind=partial | timestamp=1783557454.9397876 | source=vosk | rms=323 | updated_at=1783557454.8848507 | frequency_hz=354.0
- [2026-07-09 08:37:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557455.134293 | source=vosk | rms=255 | updated_at=1783557455.134293 | frequency_hz=354.0
- [2026-07-09 08:37:35] operator / voice_transcript_partial / voice: turns the profile to rock the
  meta: kind=partial | timestamp=1783557455.1912415 | source=vosk | rms=255 | updated_at=1783557455.134293 | frequency_hz=354.0
- [2026-07-09 08:37:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557455.384491 | source=vosk | rms=607 | updated_at=1783557455.384491 | frequency_hz=354.0
- [2026-07-09 08:37:35] operator / voice_transcript_partial / voice: turns the profile to work dog got
  meta: kind=partial | timestamp=1783557455.4055657 | source=vosk | rms=607 | updated_at=1783557455.384491 | frequency_hz=354.0
- [2026-07-09 08:37:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557455.6338646 | source=vosk | rms=121 | updated_at=1783557455.6338646 | frequency_hz=354.0
- [2026-07-09 08:37:35] operator / voice_transcript_partial / voice: turns the profile rock dot gov spitzer
  meta: kind=partial | timestamp=1783557455.662006 | source=vosk | rms=121 | updated_at=1783557455.6338646 | frequency_hz=354.0
- [2026-07-09 08:37:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557455.8840523 | source=vosk | rms=439 | updated_at=1783557455.8840523 | frequency_hz=354.0
- [2026-07-09 08:37:35] operator / voice_transcript_partial / voice: turns the profile to run docker street
  meta: kind=partial | timestamp=1783557455.9041672 | source=vosk | rms=439 | updated_at=1783557455.8840523 | frequency_hz=354.0
- [2026-07-09 08:37:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557456.1345518 | source=vosk | rms=160 | updated_at=1783557456.1345518 | frequency_hz=354.0
- [2026-07-09 08:37:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557456.6353912 | source=vosk | rms=160 | updated_at=1783557456.1345518 | frequency_hz=354.0
- [2026-07-09 08:37:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557466.1349099 | source=vosk | rms=160 | updated_at=1783557456.1345518 | frequency_hz=354.0
- [2026-07-09 08:37:46] operator / voice_transcript_partial / voice: turns the profile to run docker street fight
  meta: kind=partial | timestamp=1783557466.1533399 | source=vosk | rms=160 | updated_at=1783557456.1345518 | frequency_hz=354.0
- [2026-07-09 08:37:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557466.385642 | source=vosk | rms=211 | updated_at=1783557466.385642 | frequency_hz=354.0
- [2026-07-09 08:37:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557466.90441 | source=vosk | rms=211 | updated_at=1783557466.385642 | frequency_hz=354.0
- [2026-07-09 08:37:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557467.1395373 | source=vosk | rms=296 | updated_at=1783557467.1395373 | frequency_hz=354.0
- [2026-07-09 08:37:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557467.384938 | source=vosk | rms=237 | updated_at=1783557467.384938 | frequency_hz=354.0
- [2026-07-09 08:37:47] operator / voice_transcript_final / voice: turns the profile to look got speeds five
  meta: kind=final | timestamp=1783557467.7216647 | source=final | rms=237 | updated_at=1783557467.384938 | frequency_hz=354.0
- [2026-07-09 08:37:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557468.0713844 | source=vosk | rms=237 | updated_at=1783557467.384938 | frequency_hz=354.0
- [2026-07-09 08:37:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557468.0713844 | source=vosk | rms=416 | updated_at=1783557468.0713844 | frequency_hz=354.0
- [2026-07-09 08:37:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557468.6361194 | source=vosk | rms=142 | updated_at=1783557468.134026 | frequency_hz=354.0
- [2026-07-09 08:37:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557468.8845325 | source=vosk | rms=424 | updated_at=1783557468.8845325 | frequency_hz=354.0
- [2026-07-09 08:37:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557469.3867388 | source=vosk | rms=424 | updated_at=1783557468.8845325 | frequency_hz=354.0
- [2026-07-09 08:37:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557470.134163 | source=vosk | rms=429 | updated_at=1783557470.134163 | frequency_hz=354.0
- [2026-07-09 08:37:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557470.6349864 | source=vosk | rms=429 | updated_at=1783557470.134163 | frequency_hz=354.0
- [2026-07-09 08:37:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557470.8856077 | source=vosk | rms=429 | updated_at=1783557470.134163 | frequency_hz=354.0
- [2026-07-09 08:37:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557473.6343043 | source=vosk | rms=233 | updated_at=1783557472.3841116 | frequency_hz=354.0
- [2026-07-09 08:37:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557474.3861635 | source=vosk | rms=233 | updated_at=1783557472.3841116 | frequency_hz=354.0
- [2026-07-09 08:37:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557475.8861902 | source=vosk | rms=198 | updated_at=1783557474.8849988 | frequency_hz=354.0
- [2026-07-09 08:37:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557476.1350784 | source=vosk | rms=315 | updated_at=1783557476.1350784 | frequency_hz=354.0
- [2026-07-09 08:37:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557478.6383293 | source=vosk | rms=123 | updated_at=1783557478.1339421 | frequency_hz=354.0
- [2026-07-09 08:38:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557484.1343613 | source=vosk | rms=229 | updated_at=1783557484.1343613 | frequency_hz=354.0
- [2026-07-09 08:38:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557484.634365 | source=vosk | rms=229 | updated_at=1783557484.1343613 | frequency_hz=354.0
- [2026-07-09 08:38:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557486.216183 | source=vosk | rms=585 | updated_at=1783557486.216183 | frequency_hz=354.0
- [2026-07-09 08:38:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557486.715228 | source=vosk | rms=585 | updated_at=1783557486.216183 | frequency_hz=354.0
- [2026-07-09 08:38:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557487.9648652 | source=vosk | rms=585 | updated_at=1783557486.216183 | frequency_hz=354.0
- [2026-07-09 08:38:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557488.4660149 | source=vosk | rms=585 | updated_at=1783557486.216183 | frequency_hz=354.0
- [2026-07-09 08:38:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557490.21492 | source=vosk | rms=128 | updated_at=1783557490.21492 | frequency_hz=354.0
- [2026-07-09 08:38:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557492.4653988 | source=vosk | rms=227 | updated_at=1783557491.9643915 | frequency_hz=354.0
- [2026-07-09 08:38:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557504.4660816 | source=vosk | rms=727 | updated_at=1783557504.4660816 | frequency_hz=354.0
- [2026-07-09 08:38:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557505.4663723 | source=vosk | rms=719 | updated_at=1783557504.7147279 | frequency_hz=354.0
- [2026-07-09 08:38:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557511.8552334 | source=vosk | rms=514 | updated_at=1783557511.8552334 | frequency_hz=354.0
- [2026-07-09 08:38:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557513.3557446 | source=vosk | rms=470 | updated_at=1783557512.8553581 | frequency_hz=354.0
- [2026-07-09 08:38:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557514.1065903 | source=vosk | rms=225 | updated_at=1783557514.1065903 | frequency_hz=348.4
- [2026-07-09 08:38:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557515.1055043 | source=vosk | rms=643 | updated_at=1783557514.6074798 | frequency_hz=348.4
- [2026-07-09 08:38:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557516.6049964 | source=vosk | rms=188 | updated_at=1783557516.6049964 | frequency_hz=348.4
- [2026-07-09 08:38:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557517.6056786 | source=vosk | rms=674 | updated_at=1783557517.1052167 | frequency_hz=348.4
- [2026-07-09 08:38:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557518.3557312 | source=vosk | rms=738 | updated_at=1783557518.3557312 | frequency_hz=348.4
- [2026-07-09 08:38:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557519.1049938 | source=vosk | rms=717 | updated_at=1783557518.6051712 | frequency_hz=348.4
- [2026-07-09 08:38:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557520.1067107 | source=vosk | rms=455 | updated_at=1783557520.1067107 | frequency_hz=348.4
- [2026-07-09 08:38:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557521.1055968 | source=vosk | rms=495 | updated_at=1783557520.6053486 | frequency_hz=348.4
- [2026-07-09 08:38:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557521.8547368 | source=vosk | rms=750 | updated_at=1783557521.8547368 | frequency_hz=348.4
- [2026-07-09 08:38:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557522.611981 | source=vosk | rms=717 | updated_at=1783557522.1077476 | frequency_hz=348.4
- [2026-07-09 08:38:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557522.8557842 | source=vosk | rms=717 | updated_at=1783557522.1077476 | frequency_hz=348.4
- [2026-07-09 08:38:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557524.1057084 | source=vosk | rms=247 | updated_at=1783557523.6050153 | frequency_hz=348.4
- [2026-07-09 08:38:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557525.3555996 | source=vosk | rms=247 | updated_at=1783557523.6050153 | frequency_hz=348.4
- [2026-07-09 08:38:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557527.1050339 | source=vosk | rms=654 | updated_at=1783557526.6049767 | frequency_hz=348.4
- [2026-07-09 08:38:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557535.9112663 | source=vosk | rms=497 | updated_at=1783557535.9112663 | frequency_hz=302.0
- [2026-07-09 08:38:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557537.1563435 | source=vosk | rms=375 | updated_at=1783557536.65584 | frequency_hz=302.0
- [2026-07-09 08:38:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557538.1551554 | source=vosk | rms=375 | updated_at=1783557536.65584 | frequency_hz=302.0
- [2026-07-09 08:38:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557539.155498 | source=vosk | rms=690 | updated_at=1783557538.6556447 | frequency_hz=302.0
- [2026-07-09 08:39:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557541.405397 | source=vosk | rms=690 | updated_at=1783557538.6556447 | frequency_hz=302.0
- [2026-07-09 08:39:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557542.156247 | source=vosk | rms=348 | updated_at=1783557541.6556487 | frequency_hz=302.0
- [2026-07-09 08:39:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557563.4080644 | source=vosk | rms=421 | updated_at=1783557563.4080644 | frequency_hz=302.0
- [2026-07-09 08:39:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557563.9062989 | source=vosk | rms=421 | updated_at=1783557563.4080644 | frequency_hz=302.0
- [2026-07-09 08:39:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557566.1557431 | source=vosk | rms=153 | updated_at=1783557566.1557431 | frequency_hz=302.0
- [2026-07-09 08:39:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557567.186995 | source=vosk | rms=179 | updated_at=1783557566.6556747 | frequency_hz=302.0
- [2026-07-09 08:39:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557567.482186 | source=vosk | rms=179 | updated_at=1783557566.6556747 | frequency_hz=302.0
- [2026-07-09 08:39:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557568.40645 | source=vosk | rms=211 | updated_at=1783557567.9057398 | frequency_hz=302.0
- [2026-07-09 08:39:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557569.6559181 | source=vosk | rms=211 | updated_at=1783557567.9057398 | frequency_hz=302.0
- [2026-07-09 08:39:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557570.1558523 | source=vosk | rms=211 | updated_at=1783557567.9057398 | frequency_hz=302.0
- [2026-07-09 08:39:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557571.1560147 | source=vosk | rms=211 | updated_at=1783557567.9057398 | frequency_hz=302.0
- [2026-07-09 08:39:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557572.155675 | source=vosk | rms=211 | updated_at=1783557567.9057398 | frequency_hz=302.0
- [2026-07-09 08:39:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557579.6657891 | source=vosk | rms=612 | updated_at=1783557579.6657891 | frequency_hz=368.0
- [2026-07-09 08:39:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557580.906403 | source=vosk | rms=367 | updated_at=1783557580.4074967 | frequency_hz=368.0
- [2026-07-09 08:39:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557581.6559947 | source=vosk | rms=314 | updated_at=1783557581.6559947 | frequency_hz=368.0
- [2026-07-09 08:39:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557583.1564393 | source=vosk | rms=512 | updated_at=1783557582.6566222 | frequency_hz=368.0
- [2026-07-09 08:39:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783557585.4074292 | source=vosk | rms=229 | updated_at=1783557585.4074292 | frequency_hz=368.0
- [2026-07-09 08:39:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783557585.9186296 | source=vosk | rms=229 | updated_at=1783557585.4074292 | frequency_hz=368.0

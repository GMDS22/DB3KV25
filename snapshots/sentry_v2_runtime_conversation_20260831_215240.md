# SMART SENTRY V5.0.0 Runtime Conversation Export

- Generated: 2026-08-31 21:52:40
- Entries: 209
- Roles: {'assistant': 3, 'system': 191, 'operator': 15}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 191, 'spoken_confirmation': 1, 'voice_transcript_partial': 12, 'voice_transcript_final': 3}
- Channels: {'text': 2, 'voice': 207}
- Latest operator request: so
- Latest assistant message: Smart Sentry is ready.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-08-31 21:47:27] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-08-31 21:47:27] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-08-31 21:47:33] system / voice_status / voice: listening
  meta: kind=status | timestamp=1788184053.0017 | source=vosk
- [2026-08-31 21:47:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184053.758566 | source=vosk | rms=242 | updated_at=1788184053.758566
- [2026-08-31 21:47:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184054.2593758 | source=vosk | rms=242 | updated_at=1788184053.758566
- [2026-08-31 21:47:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184059.1085987 | source=vosk | rms=124 | updated_at=1788184059.1085987 | frequency_hz=386.0
- [2026-08-31 21:47:42] assistant / spoken_confirmation / voice: Smart Sentry is ready.
  meta: interrupt=True | assistant_output=False | spoken=True
- [2026-08-31 21:47:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184059.8577042 | source=vosk | rms=124 | updated_at=1788184059.1085987 | frequency_hz=386.0
- [2026-08-31 21:47:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184070.10814 | source=vosk | rms=124 | updated_at=1788184059.1085987 | frequency_hz=386.0
- [2026-08-31 21:47:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184070.6085157 | source=vosk | rms=124 | updated_at=1788184059.1085987 | frequency_hz=386.0
- [2026-08-31 21:48:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184082.1086519 | source=vosk | rms=247 | updated_at=1788184082.1086519 | frequency_hz=386.0
- [2026-08-31 21:48:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184082.6086023 | source=vosk | rms=247 | updated_at=1788184082.1086519 | frequency_hz=386.0
- [2026-08-31 21:48:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184083.3583467 | source=vosk | rms=1180 | updated_at=1788184083.3583467 | frequency_hz=386.0
- [2026-08-31 21:48:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184084.1087759 | source=vosk | rms=1180 | updated_at=1788184083.3583467 | frequency_hz=386.0
- [2026-08-31 21:48:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184085.858336 | source=vosk | rms=1180 | updated_at=1788184083.3583467 | frequency_hz=386.0
- [2026-08-31 21:48:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184086.3589396 | source=vosk | rms=1180 | updated_at=1788184083.3583467 | frequency_hz=386.0
- [2026-08-31 21:48:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184086.6089354 | source=vosk | rms=505 | updated_at=1788184086.6089354 | frequency_hz=184.0
- [2026-08-31 21:48:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184087.1084127 | source=vosk | rms=505 | updated_at=1788184086.6089354 | frequency_hz=184.0
- [2026-08-31 21:48:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184087.8592014 | source=vosk | rms=942 | updated_at=1788184087.8592014 | frequency_hz=184.0
- [2026-08-31 21:48:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184088.3596613 | source=vosk | rms=942 | updated_at=1788184087.8592014 | frequency_hz=184.0
- [2026-08-31 21:48:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184093.1092553 | source=vosk | rms=359 | updated_at=1788184093.1092553 | frequency_hz=184.0
- [2026-08-31 21:48:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184093.608528 | source=vosk | rms=359 | updated_at=1788184093.1092553 | frequency_hz=184.0
- [2026-08-31 21:48:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184096.6091151 | source=vosk | rms=359 | updated_at=1788184093.1092553 | frequency_hz=184.0
- [2026-08-31 21:48:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184097.109932 | source=vosk | rms=359 | updated_at=1788184093.1092553 | frequency_hz=184.0
- [2026-08-31 21:48:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184098.110187 | source=vosk | rms=359 | updated_at=1788184093.1092553 | frequency_hz=184.0
- [2026-08-31 21:48:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184098.6211805 | source=vosk | rms=359 | updated_at=1788184093.1092553 | frequency_hz=184.0
- [2026-08-31 21:48:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184101.859648 | source=vosk | rms=153 | updated_at=1788184101.859648 | frequency_hz=184.0
- [2026-08-31 21:48:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184102.358905 | source=vosk | rms=153 | updated_at=1788184101.859648 | frequency_hz=184.0
- [2026-08-31 21:48:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184104.359277 | source=vosk | rms=222 | updated_at=1788184104.359277 | frequency_hz=188.0
- [2026-08-31 21:48:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184104.8588593 | source=vosk | rms=222 | updated_at=1788184104.359277 | frequency_hz=188.0
- [2026-08-31 21:48:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184112.3591912 | source=vosk | rms=364 | updated_at=1788184112.3591912 | frequency_hz=126.0
- [2026-08-31 21:48:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184113.1104453 | source=vosk | rms=389 | updated_at=1788184112.6091957 | frequency_hz=126.0
- [2026-08-31 21:48:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184117.111612 | source=vosk | rms=389 | updated_at=1788184112.6091957 | frequency_hz=126.0
- [2026-08-31 21:48:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184117.6096048 | source=vosk | rms=389 | updated_at=1788184112.6091957 | frequency_hz=126.0
- [2026-08-31 21:48:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184130.859531 | source=vosk | rms=382 | updated_at=1788184130.859531 | frequency_hz=126.0
- [2026-08-31 21:48:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184131.3602657 | source=vosk | rms=382 | updated_at=1788184130.859531 | frequency_hz=126.0
- [2026-08-31 21:48:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184137.8605287 | source=vosk | rms=382 | updated_at=1788184130.859531 | frequency_hz=126.0
- [2026-08-31 21:48:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184138.3604474 | source=vosk | rms=382 | updated_at=1788184130.859531 | frequency_hz=126.0
- [2026-08-31 21:48:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184138.860187 | source=vosk | rms=382 | updated_at=1788184130.859531 | frequency_hz=126.0
- [2026-08-31 21:48:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184139.3601315 | source=vosk | rms=382 | updated_at=1788184130.859531 | frequency_hz=126.0
- [2026-08-31 21:49:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184144.610418 | source=vosk | rms=382 | updated_at=1788184130.859531 | frequency_hz=126.0
- [2026-08-31 21:49:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184145.1100998 | source=vosk | rms=382 | updated_at=1788184130.859531 | frequency_hz=126.0
- [2026-08-31 21:49:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184146.1101272 | source=vosk | rms=325 | updated_at=1788184146.1101272 | frequency_hz=414.0
- [2026-08-31 21:49:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184146.8605962 | source=vosk | rms=192 | updated_at=1788184146.3624878 | frequency_hz=414.0
- [2026-08-31 21:49:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184148.8604438 | source=vosk | rms=238 | updated_at=1788184148.8604438 | frequency_hz=414.0
- [2026-08-31 21:49:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184149.3603444 | source=vosk | rms=238 | updated_at=1788184148.8604438 | frequency_hz=414.0
- [2026-08-31 21:49:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184149.6101704 | source=vosk | rms=238 | updated_at=1788184148.8604438 | frequency_hz=414.0
- [2026-08-31 21:49:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184150.6103797 | source=vosk | rms=343 | updated_at=1788184150.1106396 | frequency_hz=414.0
- [2026-08-31 21:49:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184154.360783 | source=vosk | rms=343 | updated_at=1788184150.1106396 | frequency_hz=414.0
- [2026-08-31 21:49:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184155.361166 | source=vosk | rms=343 | updated_at=1788184150.1106396 | frequency_hz=414.0
- [2026-08-31 21:49:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184155.6097615 | source=vosk | rms=343 | updated_at=1788184150.1106396 | frequency_hz=414.0
- [2026-08-31 21:49:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184156.1104815 | source=vosk | rms=343 | updated_at=1788184150.1106396 | frequency_hz=414.0
- [2026-08-31 21:49:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184156.6101956 | source=vosk | rms=343 | updated_at=1788184150.1106396 | frequency_hz=414.0
- [2026-08-31 21:49:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184157.1107426 | source=vosk | rms=343 | updated_at=1788184150.1106396 | frequency_hz=414.0
- [2026-08-31 21:49:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184157.8607798 | source=vosk | rms=343 | updated_at=1788184150.1106396 | frequency_hz=414.0
- [2026-08-31 21:49:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184158.3604882 | source=vosk | rms=343 | updated_at=1788184150.1106396 | frequency_hz=414.0
- [2026-08-31 21:49:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184160.3601382 | source=vosk | rms=266 | updated_at=1788184160.3601382 | frequency_hz=414.0
- [2026-08-31 21:49:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184160.861005 | source=vosk | rms=266 | updated_at=1788184160.3601382 | frequency_hz=414.0
- [2026-08-31 21:49:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184178.864268 | source=vosk | rms=196 | updated_at=1788184178.864268 | frequency_hz=414.0
- [2026-08-31 21:49:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184181.861537 | source=vosk | rms=937 | updated_at=1788184181.3610609 | frequency_hz=414.0
- [2026-08-31 21:49:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184182.610951 | source=vosk | rms=937 | updated_at=1788184181.3610609 | frequency_hz=414.0
- [2026-08-31 21:49:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184183.1109662 | source=vosk | rms=937 | updated_at=1788184181.3610609 | frequency_hz=414.0
- [2026-08-31 21:49:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184185.8616252 | source=vosk | rms=302 | updated_at=1788184185.8616252 | frequency_hz=414.0
- [2026-08-31 21:49:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184186.8613214 | source=vosk | rms=126 | updated_at=1788184186.3614016 | frequency_hz=414.0
- [2026-08-31 21:49:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184187.1152833 | source=vosk | rms=331 | updated_at=1788184187.1152833 | frequency_hz=414.0
- [2026-08-31 21:49:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184190.1118648 | source=vosk | rms=375 | updated_at=1788184189.6113763 | frequency_hz=414.0
- [2026-08-31 21:49:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184190.3612094 | source=vosk | rms=166 | updated_at=1788184190.3612094 | frequency_hz=414.0
- [2026-08-31 21:49:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184191.8615615 | source=vosk | rms=1204 | updated_at=1788184191.1116378 | frequency_hz=414.0
- [2026-08-31 21:49:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184192.3611338 | source=vosk | rms=1204 | updated_at=1788184191.1116378 | frequency_hz=414.0
- [2026-08-31 21:49:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184192.8616314 | source=vosk | rms=1204 | updated_at=1788184191.1116378 | frequency_hz=414.0
- [2026-08-31 21:49:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184194.865024 | source=vosk | rms=1203 | updated_at=1788184194.865024 | frequency_hz=414.0
- [2026-08-31 21:49:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184195.611363 | source=vosk | rms=1203 | updated_at=1788184194.865024 | frequency_hz=414.0
- [2026-08-31 21:49:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184195.8611224 | source=vosk | rms=142 | updated_at=1788184195.8611224 | frequency_hz=414.0
- [2026-08-31 21:49:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184196.3612556 | source=vosk | rms=142 | updated_at=1788184195.8611224 | frequency_hz=414.0
- [2026-08-31 21:49:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184196.8622732 | source=vosk | rms=125 | updated_at=1788184196.8622732 | frequency_hz=414.0
- [2026-08-31 21:49:57] operator / voice_transcript_partial / voice: fluid pills
  meta: kind=partial | timestamp=1788184197.715126 | source=vosk | rms=1203 | updated_at=1788184197.6118772 | frequency_hz=414.0
- [2026-08-31 21:49:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184197.861232 | source=vosk | rms=1204 | updated_at=1788184197.861232 | frequency_hz=414.0
- [2026-08-31 21:49:58] operator / voice_transcript_partial / voice: bluetooth mouse
  meta: kind=partial | timestamp=1788184198.2060237 | source=vosk | rms=352 | updated_at=1788184198.1111758 | frequency_hz=414.0
- [2026-08-31 21:49:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184198.6130106 | source=vosk | rms=279 | updated_at=1788184198.6130106 | frequency_hz=414.0
- [2026-08-31 21:49:58] operator / voice_transcript_partial / voice: bluetooth left
  meta: kind=partial | timestamp=1788184198.6774378 | source=vosk | rms=279 | updated_at=1788184198.6130106 | frequency_hz=414.0
- [2026-08-31 21:49:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184198.8620582 | source=vosk | rms=448 | updated_at=1788184198.8620582 | frequency_hz=414.0
- [2026-08-31 21:49:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184199.1112046 | source=vosk | rms=230 | updated_at=1788184199.1112046 | frequency_hz=414.0
- [2026-08-31 21:49:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184199.3613353 | source=vosk | rms=124 | updated_at=1788184199.3613353 | frequency_hz=414.0
- [2026-08-31 21:49:59] operator / voice_transcript_final / voice: bluetooth left
  meta: kind=final | timestamp=1788184199.631466 | source=final | rms=124 | updated_at=1788184199.3613353 | frequency_hz=414.0
- [2026-08-31 21:49:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184199.6665387 | source=vosk | rms=1202 | updated_at=1788184199.6665387 | frequency_hz=414.0
- [2026-08-31 21:50:00] operator / voice_transcript_partial / voice: purple shirt
  meta: kind=partial | timestamp=1788184200.6494517 | source=vosk | rms=1201 | updated_at=1788184200.6120782 | frequency_hz=414.0
- [2026-08-31 21:50:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184200.8616521 | source=vosk | rms=1201 | updated_at=1788184200.8616521 | frequency_hz=414.0
- [2026-08-31 21:50:00] operator / voice_transcript_partial / voice: people should be
  meta: kind=partial | timestamp=1788184200.932604 | source=vosk | rms=1201 | updated_at=1788184200.8616521 | frequency_hz=414.0
- [2026-08-31 21:50:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184201.111917 | source=vosk | rms=973 | updated_at=1788184201.111917 | frequency_hz=414.0
- [2026-08-31 21:50:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184201.362121 | source=vosk | rms=1201 | updated_at=1788184201.362121 | frequency_hz=414.0
- [2026-08-31 21:50:01] operator / voice_transcript_partial / voice: people should be like
  meta: kind=partial | timestamp=1788184201.4294026 | source=vosk | rms=1201 | updated_at=1788184201.362121 | frequency_hz=414.0
- [2026-08-31 21:50:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184201.6120896 | source=vosk | rms=1200 | updated_at=1788184201.6120896 | frequency_hz=414.0
- [2026-08-31 21:50:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184201.8614926 | source=vosk | rms=1200 | updated_at=1788184201.8614926 | frequency_hz=414.0
- [2026-08-31 21:50:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184202.1114814 | source=vosk | rms=1200 | updated_at=1788184202.1114814 | frequency_hz=414.0
- [2026-08-31 21:50:02] operator / voice_transcript_partial / voice: people should be white
  meta: kind=partial | timestamp=1788184202.1570537 | source=vosk | rms=1200 | updated_at=1788184202.1114814 | frequency_hz=414.0
- [2026-08-31 21:50:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184202.3620942 | source=vosk | rms=1200 | updated_at=1788184202.3620942 | frequency_hz=414.0
- [2026-08-31 21:50:02] operator / voice_transcript_partial / voice: people should be like a lot
  meta: kind=partial | timestamp=1788184202.4318287 | source=vosk | rms=1200 | updated_at=1788184202.3620942 | frequency_hz=414.0
- [2026-08-31 21:50:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184202.6134796 | source=vosk | rms=1201 | updated_at=1788184202.6134796 | frequency_hz=414.0
- [2026-08-31 21:50:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184202.8618414 | source=vosk | rms=1200 | updated_at=1788184202.8618414 | frequency_hz=414.0
- [2026-08-31 21:50:03] operator / voice_transcript_partial / voice: people should be wide open that kinda sucks
  meta: kind=partial | timestamp=1788184203.030977 | source=vosk | rms=1200 | updated_at=1788184202.8618414 | frequency_hz=414.0
- [2026-08-31 21:50:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184203.112119 | source=vosk | rms=1200 | updated_at=1788184203.112119 | frequency_hz=414.0
- [2026-08-31 21:50:03] operator / voice_transcript_partial / voice: people should be like a connection garlic extract
  meta: kind=partial | timestamp=1788184203.1863165 | source=vosk | rms=1200 | updated_at=1788184203.112119 | frequency_hz=414.0
- [2026-08-31 21:50:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184203.3616726 | source=vosk | rms=1201 | updated_at=1788184203.3616726 | frequency_hz=414.0
- [2026-08-31 21:50:03] operator / voice_transcript_partial / voice: people should be like a lot to go fuck fuck fuck
  meta: kind=partial | timestamp=1788184203.4290764 | source=vosk | rms=1201 | updated_at=1788184203.3616726 | frequency_hz=414.0
- [2026-08-31 21:50:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184203.6119328 | source=vosk | rms=254 | updated_at=1788184203.6119328 | frequency_hz=414.0
- [2026-08-31 21:50:03] operator / voice_transcript_partial / voice: people should be like a connection garlic extract followed
  meta: kind=partial | timestamp=1788184203.6474178 | source=vosk | rms=254 | updated_at=1788184203.6119328 | frequency_hz=414.0
- [2026-08-31 21:50:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184204.1114087 | source=vosk | rms=254 | updated_at=1788184203.6119328 | frequency_hz=414.0
- [2026-08-31 21:50:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184209.8615355 | source=vosk | rms=254 | updated_at=1788184203.6119328 | frequency_hz=414.0
- [2026-08-31 21:50:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184210.3614578 | source=vosk | rms=254 | updated_at=1788184203.6119328 | frequency_hz=414.0
- [2026-08-31 21:50:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184210.6112034 | source=vosk | rms=429 | updated_at=1788184210.6112034 | frequency_hz=286.0
- [2026-08-31 21:50:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184211.111428 | source=vosk | rms=429 | updated_at=1788184210.6112034 | frequency_hz=286.0
- [2026-08-31 21:50:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184213.863592 | source=vosk | rms=412 | updated_at=1788184213.863592 | frequency_hz=140.0
- [2026-08-31 21:50:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184214.36238 | source=vosk | rms=412 | updated_at=1788184213.863592 | frequency_hz=140.0
- [2026-08-31 21:50:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184219.3627174 | source=vosk | rms=412 | updated_at=1788184213.863592 | frequency_hz=140.0
- [2026-08-31 21:50:19] operator / voice_transcript_final / voice: purple should be like a to garlic extract followed
  meta: kind=final | timestamp=1788184219.6777136 | source=final | rms=412 | updated_at=1788184213.863592 | frequency_hz=140.0
- [2026-08-31 21:50:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184219.796353 | source=vosk | rms=412 | updated_at=1788184213.863592 | frequency_hz=140.0
- [2026-08-31 21:50:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184219.796353 | source=vosk | rms=412 | updated_at=1788184213.863592 | frequency_hz=140.0
- [2026-08-31 21:50:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184220.362817 | source=vosk | rms=394 | updated_at=1788184219.864513 | frequency_hz=140.0
- [2026-08-31 21:50:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184222.362946 | source=vosk | rms=660 | updated_at=1788184222.362946 | frequency_hz=256.0
- [2026-08-31 21:50:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184222.8622296 | source=vosk | rms=660 | updated_at=1788184222.362946 | frequency_hz=256.0
- [2026-08-31 21:50:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184223.6114862 | source=vosk | rms=379 | updated_at=1788184223.6114862 | frequency_hz=263.0
- [2026-08-31 21:50:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184224.6117737 | source=vosk | rms=315 | updated_at=1788184223.8667035 | frequency_hz=263.0
- [2026-08-31 21:50:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184231.6142867 | source=vosk | rms=263 | updated_at=1788184231.6142867 | frequency_hz=234.0
- [2026-08-31 21:50:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184232.1130862 | source=vosk | rms=263 | updated_at=1788184231.6142867 | frequency_hz=234.0
- [2026-08-31 21:50:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184232.8684623 | source=vosk | rms=556 | updated_at=1788184232.8684623 | frequency_hz=244.5
- [2026-08-31 21:50:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184233.6144373 | source=vosk | rms=556 | updated_at=1788184232.8684623 | frequency_hz=244.5
- [2026-08-31 21:50:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184234.611699 | source=vosk | rms=556 | updated_at=1788184232.8684623 | frequency_hz=244.5
- [2026-08-31 21:50:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184236.8626878 | source=vosk | rms=439 | updated_at=1788184236.1130373 | frequency_hz=230.4
- [2026-08-31 21:50:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184239.1129491 | source=vosk | rms=137 | updated_at=1788184239.1129491 | frequency_hz=230.4
- [2026-08-31 21:50:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184239.612913 | source=vosk | rms=137 | updated_at=1788184239.1129491 | frequency_hz=230.4
- [2026-08-31 21:50:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184245.3667948 | source=vosk | rms=138 | updated_at=1788184245.3667948 | frequency_hz=230.4
- [2026-08-31 21:50:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184245.863315 | source=vosk | rms=138 | updated_at=1788184245.3667948 | frequency_hz=230.4
- [2026-08-31 21:50:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184247.1132522 | source=vosk | rms=476 | updated_at=1788184247.1132522 | frequency_hz=230.4
- [2026-08-31 21:50:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184248.364878 | source=vosk | rms=197 | updated_at=1788184247.6130958 | frequency_hz=230.4
- [2026-08-31 21:50:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184255.3632512 | source=vosk | rms=483 | updated_at=1788184255.3632512 | frequency_hz=230.4
- [2026-08-31 21:50:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184255.8631363 | source=vosk | rms=483 | updated_at=1788184255.3632512 | frequency_hz=230.4
- [2026-08-31 21:50:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184259.6134136 | source=vosk | rms=311 | updated_at=1788184259.6134136 | frequency_hz=144.0
- [2026-08-31 21:51:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184260.11431 | source=vosk | rms=311 | updated_at=1788184259.6134136 | frequency_hz=144.0
- [2026-08-31 21:51:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184262.113563 | source=vosk | rms=120 | updated_at=1788184262.113563 | frequency_hz=150.0
- [2026-08-31 21:51:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184262.6138368 | source=vosk | rms=120 | updated_at=1788184262.113563 | frequency_hz=150.0
- [2026-08-31 21:51:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184264.8633893 | source=vosk | rms=377 | updated_at=1788184264.8633893 | frequency_hz=150.0
- [2026-08-31 21:51:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184265.3633378 | source=vosk | rms=377 | updated_at=1788184264.8633893 | frequency_hz=150.0
- [2026-08-31 21:51:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184266.6129591 | source=vosk | rms=172 | updated_at=1788184266.6129591 | frequency_hz=196.0
- [2026-08-31 21:51:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184267.1134255 | source=vosk | rms=172 | updated_at=1788184266.6129591 | frequency_hz=196.0
- [2026-08-31 21:51:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184267.3676953 | source=vosk | rms=404 | updated_at=1788184267.3676953 | frequency_hz=196.0
- [2026-08-31 21:51:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184267.8630805 | source=vosk | rms=404 | updated_at=1788184267.3676953 | frequency_hz=196.0
- [2026-08-31 21:51:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184274.1156633 | source=vosk | rms=404 | updated_at=1788184267.3676953 | frequency_hz=196.0
- [2026-08-31 21:51:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184274.613703 | source=vosk | rms=404 | updated_at=1788184267.3676953 | frequency_hz=196.0
- [2026-08-31 21:51:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184275.863232 | source=vosk | rms=134 | updated_at=1788184275.863232 | frequency_hz=196.0
- [2026-08-31 21:51:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184277.8650281 | source=vosk | rms=134 | updated_at=1788184277.3632467 | frequency_hz=223.7
- [2026-08-31 21:51:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184279.6136618 | source=vosk | rms=585 | updated_at=1788184279.6136618 | frequency_hz=82.0
- [2026-08-31 21:51:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184280.1141012 | source=vosk | rms=585 | updated_at=1788184279.6136618 | frequency_hz=82.0
- [2026-08-31 21:51:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184280.8634317 | source=vosk | rms=124 | updated_at=1788184280.8634317 | frequency_hz=82.0
- [2026-08-31 21:51:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184281.363175 | source=vosk | rms=124 | updated_at=1788184280.8634317 | frequency_hz=82.0
- [2026-08-31 21:51:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184281.8651323 | source=vosk | rms=617 | updated_at=1788184281.8651323 | frequency_hz=170.9
- [2026-08-31 21:51:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184282.3636837 | source=vosk | rms=617 | updated_at=1788184281.8651323 | frequency_hz=170.9
- [2026-08-31 21:51:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184285.364127 | source=vosk | rms=208 | updated_at=1788184285.364127 | frequency_hz=170.9
- [2026-08-31 21:51:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184285.8641999 | source=vosk | rms=208 | updated_at=1788184285.364127 | frequency_hz=170.9
- [2026-08-31 21:51:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184288.6142638 | source=vosk | rms=398 | updated_at=1788184288.6142638 | frequency_hz=170.9
- [2026-08-31 21:51:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184289.113409 | source=vosk | rms=398 | updated_at=1788184288.6142638 | frequency_hz=170.9
- [2026-08-31 21:51:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184290.364028 | source=vosk | rms=144 | updated_at=1788184290.364028 | frequency_hz=170.9
- [2026-08-31 21:51:31] operator / voice_transcript_final / voice: so
  meta: kind=final | timestamp=1788184291.411078 | source=final | rms=218 | updated_at=1788184290.864241 | frequency_hz=170.9
- [2026-08-31 21:51:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184291.4501731 | source=vosk | rms=218 | updated_at=1788184290.864241 | frequency_hz=170.9
- [2026-08-31 21:51:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184291.8643992 | source=vosk | rms=218 | updated_at=1788184290.864241 | frequency_hz=170.9
- [2026-08-31 21:51:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184292.3642764 | source=vosk | rms=218 | updated_at=1788184290.864241 | frequency_hz=170.9
- [2026-08-31 21:51:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184292.6143503 | source=vosk | rms=129 | updated_at=1788184292.6143503 | frequency_hz=170.9
- [2026-08-31 21:51:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184293.6136901 | source=vosk | rms=454 | updated_at=1788184293.1256793 | frequency_hz=167.8
- [2026-08-31 21:51:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184294.3642457 | source=vosk | rms=153 | updated_at=1788184294.3642457 | frequency_hz=207.8
- [2026-08-31 21:51:34] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184294.8639653 | source=vosk | rms=153 | updated_at=1788184294.3642457 | frequency_hz=207.8
- [2026-08-31 21:51:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184296.1171458 | source=vosk | rms=153 | updated_at=1788184294.3642457 | frequency_hz=207.8
- [2026-08-31 21:51:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184297.3644762 | source=vosk | rms=201 | updated_at=1788184296.8644383 | frequency_hz=203.7
- [2026-08-31 21:51:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184297.8635602 | source=vosk | rms=201 | updated_at=1788184296.8644383 | frequency_hz=203.7
- [2026-08-31 21:51:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184298.6151 | source=vosk | rms=201 | updated_at=1788184296.8644383 | frequency_hz=203.7
- [2026-08-31 21:51:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184300.8642907 | source=vosk | rms=201 | updated_at=1788184296.8644383 | frequency_hz=203.7
- [2026-08-31 21:51:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184301.364309 | source=vosk | rms=201 | updated_at=1788184296.8644383 | frequency_hz=203.7
- [2026-08-31 21:51:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184304.6153123 | source=vosk | rms=524 | updated_at=1788184304.6153123 | frequency_hz=236.0
- [2026-08-31 21:51:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184305.1142576 | source=vosk | rms=524 | updated_at=1788184304.6153123 | frequency_hz=236.0
- [2026-08-31 21:51:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184305.3647969 | source=vosk | rms=533 | updated_at=1788184305.3647969 | frequency_hz=236.0
- [2026-08-31 21:51:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184307.364483 | source=vosk | rms=431 | updated_at=1788184306.8667576 | frequency_hz=238.1
- [2026-08-31 21:51:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184308.3647788 | source=vosk | rms=384 | updated_at=1788184308.3647788 | frequency_hz=238.1
- [2026-08-31 21:51:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184308.8644354 | source=vosk | rms=384 | updated_at=1788184308.3647788 | frequency_hz=238.1
- [2026-08-31 21:51:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184310.1147847 | source=vosk | rms=230 | updated_at=1788184310.1147847 | frequency_hz=352.0
- [2026-08-31 21:51:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184310.6150053 | source=vosk | rms=230 | updated_at=1788184310.1147847 | frequency_hz=352.0
- [2026-08-31 21:51:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184312.1142306 | source=vosk | rms=257 | updated_at=1788184312.1142306 | frequency_hz=352.0
- [2026-08-31 21:51:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184313.8641505 | source=vosk | rms=1203 | updated_at=1788184313.3703222 | frequency_hz=352.0
- [2026-08-31 21:51:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184314.1144452 | source=vosk | rms=150 | updated_at=1788184314.1144452 | frequency_hz=352.0
- [2026-08-31 21:51:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184315.3640141 | source=vosk | rms=171 | updated_at=1788184314.8641937 | frequency_hz=352.0
- [2026-08-31 21:51:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184316.364323 | source=vosk | rms=171 | updated_at=1788184314.8641937 | frequency_hz=352.0
- [2026-08-31 21:51:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184316.864656 | source=vosk | rms=171 | updated_at=1788184314.8641937 | frequency_hz=352.0
- [2026-08-31 21:51:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184317.1144085 | source=vosk | rms=171 | updated_at=1788184314.8641937 | frequency_hz=352.0
- [2026-08-31 21:51:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184317.614711 | source=vosk | rms=171 | updated_at=1788184314.8641937 | frequency_hz=352.0
- [2026-08-31 21:52:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184323.364275 | source=vosk | rms=1206 | updated_at=1788184323.364275 | frequency_hz=352.0
- [2026-08-31 21:52:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184324.8646698 | source=vosk | rms=1185 | updated_at=1788184323.6148598 | frequency_hz=352.0
- [2026-08-31 21:52:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184325.3649886 | source=vosk | rms=1201 | updated_at=1788184325.3649886 | frequency_hz=352.0
- [2026-08-31 21:52:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184326.365066 | source=vosk | rms=199 | updated_at=1788184325.8649518 | frequency_hz=352.0
- [2026-08-31 21:52:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184327.6150625 | source=vosk | rms=179 | updated_at=1788184327.6150625 | frequency_hz=318.0
- [2026-08-31 21:52:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184328.3653655 | source=vosk | rms=179 | updated_at=1788184327.6150625 | frequency_hz=318.0
- [2026-08-31 21:52:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184329.614457 | source=vosk | rms=195 | updated_at=1788184329.614457 | frequency_hz=318.0
- [2026-08-31 21:52:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184330.1161628 | source=vosk | rms=195 | updated_at=1788184329.614457 | frequency_hz=318.0
- [2026-08-31 21:52:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184330.3668854 | source=vosk | rms=497 | updated_at=1788184330.3658786 | frequency_hz=318.0
- [2026-08-31 21:52:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184330.8649063 | source=vosk | rms=497 | updated_at=1788184330.3658786 | frequency_hz=318.0
- [2026-08-31 21:52:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184332.3646355 | source=vosk | rms=497 | updated_at=1788184330.3658786 | frequency_hz=318.0
- [2026-08-31 21:52:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184332.8644893 | source=vosk | rms=497 | updated_at=1788184330.3658786 | frequency_hz=318.0
- [2026-08-31 21:52:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184354.6356616 | source=vosk | rms=120 | updated_at=1788184354.6356616 | frequency_hz=172.0
- [2026-08-31 21:52:35] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184355.141913 | source=vosk | rms=120 | updated_at=1788184354.6356616 | frequency_hz=172.0
- [2026-08-31 21:52:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184357.3853369 | source=vosk | rms=266 | updated_at=1788184357.3853369 | frequency_hz=192.0
- [2026-08-31 21:52:37] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184357.8866086 | source=vosk | rms=266 | updated_at=1788184357.3853369 | frequency_hz=192.0
- [2026-08-31 21:52:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1788184359.135089 | source=vosk | rms=266 | updated_at=1788184357.3853369 | frequency_hz=192.0
- [2026-08-31 21:52:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1788184359.6351461 | source=vosk | rms=266 | updated_at=1788184357.3853369 | frequency_hz=192.0

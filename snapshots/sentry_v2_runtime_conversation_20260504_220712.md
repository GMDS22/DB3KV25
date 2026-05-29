# SMART SENTRY V3.5.3 Runtime Conversation Export

- Generated: 2026-05-04 22:07:12
- Entries: 1203
- Roles: {'assistant': 23, 'system': 1, 'operator': 1179}
- Event types: {'assistant_prompt': 14, 'assistant_analysis': 1, 'voice_status': 1, 'voice_transcript_partial': 1032, 'voice_transcript_final': 133, 'voice_command': 14, 'spoken_confirmation': 8}
- Channels: {'text': 15, 'voice': 1188}
- Latest operator request: and one was known as
- Latest assistant message: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-04 21:53:22] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 21:53:22] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-04 21:53:23] system / voice_status / voice: listening
  meta: kind=status | timestamp=1777902803.6256456 | source=windows
- [2026-05-04 21:53:28] operator / voice_transcript_partial / voice: why
  meta: kind=partial | timestamp=1777902808.5083323 | source=windows
- [2026-05-04 21:53:28] operator / voice_transcript_partial / voice: late
  meta: kind=partial | timestamp=1777902808.7207668 | source=windows
- [2026-05-04 21:53:28] operator / voice_transcript_partial / voice: later
  meta: kind=partial | timestamp=1777902808.9381025 | source=windows
- [2026-05-04 21:53:29] operator / voice_transcript_partial / voice: what you are the
  meta: kind=partial | timestamp=1777902809.1400437 | source=windows
- [2026-05-04 21:53:29] operator / voice_transcript_partial / voice: later he is
  meta: kind=partial | timestamp=1777902809.3420157 | source=windows
- [2026-05-04 21:53:29] operator / voice_transcript_partial / voice: later he is a
  meta: kind=partial | timestamp=1777902809.543881 | source=windows
- [2026-05-04 21:53:30] operator / voice_transcript_partial / voice: while you're a setting in
  meta: kind=partial | timestamp=1777902810.1521535 | source=windows
- [2026-05-04 21:53:30] operator / voice_transcript_partial / voice: later he has any number
  meta: kind=partial | timestamp=1777902810.3544142 | source=windows
- [2026-05-04 21:53:30] operator / voice_transcript_partial / voice: later he is adding them over and
  meta: kind=partial | timestamp=1777902810.5554612 | source=windows
- [2026-05-04 21:53:30] operator / voice_transcript_partial / voice: what you are the setting and one half
  meta: kind=partial | timestamp=1777902810.9608483 | source=windows
- [2026-05-04 21:53:31] operator / voice_transcript_partial / voice: while you're a setting where and when
  meta: kind=partial | timestamp=1777902811.3676035 | source=windows
- [2026-05-04 21:53:31] operator / voice_transcript_partial / voice: while you're a setting where and when you
  meta: kind=partial | timestamp=1777902811.5835345 | source=windows
- [2026-05-04 21:53:31] operator / voice_transcript_partial / voice: while you're a setting where and when you add
  meta: kind=partial | timestamp=1777902811.9887514 | source=windows
- [2026-05-04 21:53:32] operator / voice_transcript_partial / voice: while you're a setting where and when you activate
  meta: kind=partial | timestamp=1777902812.1899736 | source=windows
- [2026-05-04 21:53:32] operator / voice_transcript_partial / voice: while you're a setting where and when was the
  meta: kind=partial | timestamp=1777902812.3920515 | source=windows
- [2026-05-04 21:53:32] operator / voice_transcript_partial / voice: while you're a setting where and when that has
  meta: kind=partial | timestamp=1777902812.6372948 | source=windows
- [2026-05-04 21:53:33] operator / voice_transcript_partial / voice: while you're a setting where and when you act as if
  meta: kind=partial | timestamp=1777902813.250953 | source=windows
- [2026-05-04 21:53:33] operator / voice_transcript_partial / voice: while you're a setting where and when that has
  meta: kind=partial | timestamp=1777902813.4681652 | source=windows
- [2026-05-04 21:53:34] operator / voice_transcript_partial / voice: while you're a setting where and when that has as many as
  meta: kind=partial | timestamp=1777902814.076569 | source=windows
- [2026-05-04 21:53:35] operator / voice_transcript_final / voice: while you re a setting where and when that has as many as
  meta: kind=final | timestamp=1777902815.1229575 | source=final | confidence=0.06
- [2026-05-04 21:53:35] operator / voice_transcript_partial / voice: two
  meta: kind=partial | timestamp=1777902815.3175592 | source=windows
- [2026-05-04 21:53:35] operator / voice_transcript_partial / voice: ten
  meta: kind=partial | timestamp=1777902815.3175592 | source=windows
- [2026-05-04 21:53:35] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777902815.7217743 | source=windows
- [2026-05-04 21:53:35] operator / voice_transcript_partial / voice: connect smart
  meta: kind=partial | timestamp=1777902815.924014 | source=windows
- [2026-05-04 21:53:36] operator / voice_transcript_partial / voice: two sets
  meta: kind=partial | timestamp=1777902816.1408763 | source=windows
- [2026-05-04 21:53:36] operator / voice_transcript_partial / voice: connect smart sentry
  meta: kind=partial | timestamp=1777902816.3437994 | source=windows
- [2026-05-04 21:53:36] operator / voice_transcript_partial / voice: two cents and see at least
  meta: kind=partial | timestamp=1777902816.9535403 | source=windows
- [2026-05-04 21:53:37] operator / voice_transcript_partial / voice: two assassins at these
  meta: kind=partial | timestamp=1777902817.157981 | source=windows
- [2026-05-04 21:53:37] operator / voice_transcript_final / voice: two assassins at these
  meta: kind=final | timestamp=1777902817.9831872 | source=final | confidence=0.33
- [2026-05-04 21:53:44] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777902824.1429827 | source=windows
- [2026-05-04 21:53:44] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777902824.550507 | source=windows
- [2026-05-04 21:54:01] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 21:53:44] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777902824.9597917 | source=final | confidence=0.8
- [2026-05-04 21:53:46] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777902826.7923727 | source=windows
- [2026-05-04 21:53:47] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777902827.2030418 | source=windows
- [2026-05-04 21:54:01] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 21:53:47] operator / voice_transcript_partial / voice: era and the
  meta: kind=partial | timestamp=1777902827.4051034 | source=windows
- [2026-05-04 21:53:48] operator / voice_transcript_partial / voice: era and i have
  meta: kind=partial | timestamp=1777902828.2320182 | source=windows
- [2026-05-04 21:53:48] operator / voice_transcript_partial / voice: era and the day
  meta: kind=partial | timestamp=1777902828.4359932 | source=windows
- [2026-05-04 21:53:49] operator / voice_transcript_final / voice: era and the day
  meta: kind=final | timestamp=1777902829.8563561 | source=final | confidence=0.48
- [2026-05-04 21:54:01] operator / voice_command / voice: era and the day
  meta: normalized=True
- [2026-05-04 21:53:54] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777902834.9604702 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:53:55] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777902835.1621342 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:53:55] operator / voice_transcript_partial / voice: in london
  meta: kind=partial | timestamp=1777902835.3626647 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:53:55] operator / voice_transcript_partial / voice: you run out of
  meta: kind=partial | timestamp=1777902835.5668776 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:53:55] operator / voice_transcript_partial / voice: he ran away
  meta: kind=partial | timestamp=1777902835.9714222 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:53:56] operator / voice_transcript_partial / voice: he ran away you
  meta: kind=partial | timestamp=1777902836.379178 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:53:56] operator / voice_transcript_partial / voice: he ran away you ever
  meta: kind=partial | timestamp=1777902836.7978535 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:53:57] operator / voice_transcript_partial / voice: he ran away you and
  meta: kind=partial | timestamp=1777902837.0014539 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:53:57] operator / voice_transcript_partial / voice: he ran away you anyway
  meta: kind=partial | timestamp=1777902837.2188807 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:53:58] operator / voice_transcript_final / voice: he ran away you anyway
  meta: kind=final | timestamp=1777902838.0491478 | source=final | confidence=0.26 | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:54:01] operator / voice_command / voice: he ran away you anyway
  meta: normalized=True
- [2026-05-04 21:54:01] assistant / assistant_prompt / text: Assistant request queued: assistant request about he ran away you anyway (position 1).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 21:53:58] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777902838.6582472 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:53:58] operator / voice_transcript_partial / voice: they
  meta: kind=partial | timestamp=1777902838.6582472 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:53:59] operator / voice_transcript_partial / voice: day
  meta: kind=partial | timestamp=1777902839.0780225 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:53:59] operator / voice_transcript_partial / voice: .
  meta: kind=partial | timestamp=1777902839.2815151 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:53:59] operator / voice_transcript_partial / voice: deja vu
  meta: kind=partial | timestamp=1777902839.4847064 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:53:59] operator / voice_transcript_partial / voice: is being
  meta: kind=partial | timestamp=1777902839.6879404 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:54:00] operator / voice_transcript_partial / voice: is being of
  meta: kind=partial | timestamp=1777902840.3106248 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:54:00] operator / voice_transcript_partial / voice: is being used to say
  meta: kind=partial | timestamp=1777902840.721675 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:54:00] operator / voice_transcript_partial / voice: is being you've seen
  meta: kind=partial | timestamp=1777902840.9357781 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:54:01] operator / voice_transcript_partial / voice: is being you've seen the
  meta: kind=partial | timestamp=1777902841.150791 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:54:01] operator / voice_transcript_partial / voice: is being you've seen in the
  meta: kind=partial | timestamp=1777902841.5681791 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:54:01] operator / voice_transcript_partial / voice: is being used to seeing you in
  meta: kind=partial | timestamp=1777902841.7708611 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:54:01] operator / voice_transcript_partial / voice: is being used to seeing you can see
  meta: kind=partial | timestamp=1777902841.973462 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:54:02] operator / voice_transcript_partial / voice: is being used to seeing you can see the
  meta: kind=partial | timestamp=1777902842.395133 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:54:02] operator / voice_transcript_partial / voice: is being used to seeing you can see in the
  meta: kind=partial | timestamp=1777902842.8096066 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:54:03] operator / voice_transcript_partial / voice: is being used to seeing you can see the kids
  meta: kind=partial | timestamp=1777902843.062684 | source=windows | frequency_hz=267.0 | rms=248 | updated_at=1777902832.1488078
- [2026-05-04 21:54:03] operator / voice_transcript_partial / voice: is being used to seeing you can see and do you see
  meta: kind=partial | timestamp=1777902843.5290892 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:03] operator / voice_transcript_partial / voice: is being used to seeing you can see and do you see in
  meta: kind=partial | timestamp=1777902843.5301785 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:03] operator / voice_transcript_partial / voice: is being used to seeing you can see the kids who
  meta: kind=partial | timestamp=1777902843.9931564 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:04] operator / voice_transcript_partial / voice: is being used to seeing you can see and do you see you in
  meta: kind=partial | timestamp=1777902844.2082345 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:04] assistant / spoken_confirmation / voice: Received. I started your assistant request about era and the day in the background.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 21:54:04] assistant / spoken_confirmation / voice: I am still finishing assistant request about era and the day. I queued your assistant request about he ran away you anyway. It is number 1 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 21:54:04] operator / voice_transcript_partial / voice: is being used to seeing you can see and do you see you in an
  meta: kind=partial | timestamp=1777902844.9195962 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:05] operator / voice_transcript_partial / voice: is being used to seeing you can see and do you see you in the
  meta: kind=partial | timestamp=1777902845.1779108 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:06] operator / voice_transcript_partial / voice: is being used to seeing you can see and do you see you doing things
  meta: kind=partial | timestamp=1777902846.0034547 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:06] operator / voice_transcript_partial / voice: is being used to seeing you can see and do you see you and you can see and
  meta: kind=partial | timestamp=1777902846.6364229 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:06] operator / voice_transcript_partial / voice: is being used to seeing you can see and do you see you doing things in the
  meta: kind=partial | timestamp=1777902846.6394715 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:06] operator / voice_transcript_partial / voice: is being used to seeing you can see and do you see you doing things in an
  meta: kind=partial | timestamp=1777902846.8619318 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:07] operator / voice_transcript_partial / voice: is being used to seeing you can see and do you see you doing things in the city
  meta: kind=partial | timestamp=1777902847.0763805 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:07] operator / voice_transcript_partial / voice: is being used to seeing you can see and do you see you doing things in the city say
  meta: kind=partial | timestamp=1777902847.2923026 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:07] operator / voice_transcript_partial / voice: is being used to seeing you can see and do you see you doing things in the sixteen
  meta: kind=partial | timestamp=1777902847.5082903 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:07] operator / voice_transcript_partial / voice: is being used to seeing you can see and do you see you doing things in the space and a
  meta: kind=partial | timestamp=1777902847.7202692 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:07] operator / voice_transcript_partial / voice: is being used to seeing you can see and do you see you doing things in the space and has
  meta: kind=partial | timestamp=1777902847.9377348 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:08] operator / voice_transcript_partial / voice: is being used to seeing you can see and do you see you doing things in the space and has the
  meta: kind=partial | timestamp=1777902848.1491675 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:08] operator / voice_transcript_partial / voice: is being used to seeing you can see and do you see you doing things in the space and has left
  meta: kind=partial | timestamp=1777902848.781509 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:08] operator / voice_transcript_partial / voice: is being used to seeing you can see and do you see you doing things in the space and whose last
  meta: kind=partial | timestamp=1777902848.99623 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:09] operator / voice_transcript_partial / voice: is being used to seeing you can see and do you see you doing things in the space and has the whose
  meta: kind=partial | timestamp=1777902849.1961966 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:10] operator / voice_transcript_final / voice: is being used to seeing you can see and do you see you doing things in the space and has the whose
  meta: kind=final | timestamp=1777902850.244534 | source=final | confidence=0.29 | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:10] operator / voice_command / voice: is being used to seeing you can see and do you see you doing things in the space and has the whose
  meta: normalized=True
- [2026-05-04 21:54:10] assistant / assistant_prompt / text: Assistant request queued: assistant request about is being used to seeing you can see and do you see yo... (position 2).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 21:54:10] assistant / spoken_confirmation / voice: I am still finishing assistant request about era and the day. I queued your assistant request about is being used to seeing you can see and do you see yo. It is number 2 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 21:54:11] operator / voice_transcript_partial / voice: we
  meta: kind=partial | timestamp=1777902851.996228 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:12] operator / voice_transcript_partial / voice: lead to
  meta: kind=partial | timestamp=1777902852.415565 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:12] operator / voice_transcript_partial / voice: only internet
  meta: kind=partial | timestamp=1777902852.6192021 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:12] operator / voice_transcript_partial / voice: maintaining the
  meta: kind=partial | timestamp=1777902852.8336015 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:13] operator / voice_transcript_partial / voice: we're seeing more
  meta: kind=partial | timestamp=1777902853.0498953 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:13] operator / voice_transcript_partial / voice: we're seeing more it's
  meta: kind=partial | timestamp=1777902853.4711232 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:13] operator / voice_transcript_partial / voice: lead singer of lords
  meta: kind=partial | timestamp=1777902853.6752853 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:14] operator / voice_transcript_final / voice: lead singer of lords
  meta: kind=final | timestamp=1777902854.753344 | source=final | confidence=0.46 | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:14] operator / voice_command / voice: lead singer of lords
  meta: normalized=True
- [2026-05-04 21:54:14] assistant / assistant_prompt / text: Assistant request queued: assistant request about lead singer of lords (position 3).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 21:54:15] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1777902855.1731834 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:15] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777902855.1731834 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:15] assistant / spoken_confirmation / voice: I am still finishing assistant request about era and the day. I queued your assistant request about lead singer of lords. It is number 3 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 21:54:16] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777902856.2401154 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:16] operator / voice_transcript_partial / voice: these
  meta: kind=partial | timestamp=1777902856.4516275 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:16] operator / voice_transcript_partial / voice: beside
  meta: kind=partial | timestamp=1777902856.858418 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:17] operator / voice_transcript_final / voice: beside
  meta: kind=final | timestamp=1777902857.6718466 | source=final | confidence=0.45 | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:17] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777902857.6728463 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:18] operator / voice_transcript_partial / voice: his
  meta: kind=partial | timestamp=1777902858.0901115 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:18] operator / voice_transcript_partial / voice: using the
  meta: kind=partial | timestamp=1777902858.2991474 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:18] operator / voice_transcript_partial / voice: using these
  meta: kind=partial | timestamp=1777902858.5133843 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:19] operator / voice_transcript_final / voice: using these
  meta: kind=final | timestamp=1777902859.429373 | source=final | confidence=0.37 | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:20] operator / voice_transcript_partial / voice: are
  meta: kind=partial | timestamp=1777902860.6571822 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:21] operator / voice_transcript_partial / voice: costs are
  meta: kind=partial | timestamp=1777902861.0583045 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:21] operator / voice_transcript_partial / voice: costs are a
  meta: kind=partial | timestamp=1777902861.263254 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:22] operator / voice_transcript_final / voice: costs are a
  meta: kind=final | timestamp=1777902862.5429146 | source=final | confidence=0.2 | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:22] operator / voice_transcript_partial / voice: day
  meta: kind=partial | timestamp=1777902862.7568371 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:22] operator / voice_transcript_partial / voice: ac
  meta: kind=partial | timestamp=1777902862.959516 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:23] operator / voice_transcript_partial / voice: pc or
  meta: kind=partial | timestamp=1777902863.363706 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:23] operator / voice_transcript_partial / voice: base eleven
  meta: kind=partial | timestamp=1777902863.5680745 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:23] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 21:54:24] operator / voice_transcript_final / voice: base 11
  meta: kind=final | timestamp=1777902864.5971391 | source=final | confidence=0.31 | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:29] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777902869.2056503 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:29] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777902869.2056503 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:30] operator / voice_transcript_final / voice: and
  meta: kind=final | timestamp=1777902870.5221972 | source=final | confidence=0.35 | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:30] operator / voice_command / voice: and
  meta: normalized=True
- [2026-05-04 21:54:30] assistant / assistant_prompt / text: Assistant request queued: assistant request about and (position 4).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 21:54:30] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777902870.7224333 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:30] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777902870.940809 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:31] assistant / spoken_confirmation / voice: I am still finishing assistant request about era and the day. I queued your assistant request about and. It is number 4 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 21:54:31] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777902871.5918174 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:31] operator / voice_transcript_partial / voice: that an
  meta: kind=partial | timestamp=1777902871.5925684 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:34] operator / voice_transcript_partial / voice: the pan out
  meta: kind=partial | timestamp=1777902874.3161151 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:38] operator / voice_transcript_partial / voice: that an out-
  meta: kind=partial | timestamp=1777902878.1564562 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:39] operator / voice_transcript_partial / voice: that hang out at night
  meta: kind=partial | timestamp=1777902879.4876103 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:43] operator / voice_transcript_final / voice: that hang out at night
  meta: kind=final | timestamp=1777902883.6564693 | source=final | confidence=0.3 | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:44] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1777902884.534591 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:45] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777902885.567163 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:46] operator / voice_transcript_partial / voice: and is
  meta: kind=partial | timestamp=1777902886.414459 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:49] operator / voice_transcript_final / voice: and is
  meta: kind=final | timestamp=1777902889.2199955 | source=final | confidence=0.27 | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:50] operator / voice_transcript_partial / voice: its
  meta: kind=partial | timestamp=1777902890.5771968 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:50] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777902890.7861395 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:51] operator / voice_transcript_partial / voice: second
  meta: kind=partial | timestamp=1777902891.170903 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:51] operator / voice_transcript_partial / voice: it has
  meta: kind=partial | timestamp=1777902891.5872948 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:51] operator / voice_transcript_partial / voice: it has a
  meta: kind=partial | timestamp=1777902891.951423 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:51] operator / voice_transcript_partial / voice: it has an
  meta: kind=partial | timestamp=1777902891.9519267 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:52] operator / voice_transcript_partial / voice: it has been a while
  meta: kind=partial | timestamp=1777902892.6745138 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:53] operator / voice_transcript_partial / voice: saying that while the
  meta: kind=partial | timestamp=1777902893.5281749 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:53] operator / voice_transcript_partial / voice: saying that while he
  meta: kind=partial | timestamp=1777902893.5286849 | source=windows | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:54] operator / voice_transcript_final / voice: saying that while he
  meta: kind=final | timestamp=1777902894.1301765 | source=final | confidence=0.02 | frequency_hz=418.0 | rms=162 | updated_at=1777902843.3265054
- [2026-05-04 21:54:56] operator / voice_transcript_partial / voice: did
  meta: kind=partial | timestamp=1777902896.2473717 | source=windows | frequency_hz=183.2 | rms=202 | updated_at=1777902896.2423594
- [2026-05-04 21:54:57] operator / voice_transcript_partial / voice: did in
  meta: kind=partial | timestamp=1777902897.1679442 | source=windows | frequency_hz=183.2 | rms=202 | updated_at=1777902896.2423594
- [2026-05-04 21:54:58] operator / voice_transcript_final / voice: did in
  meta: kind=final | timestamp=1777902898.0235975 | source=final | confidence=0.55 | frequency_hz=183.2 | rms=202 | updated_at=1777902896.2423594
- [2026-05-04 21:54:59] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777902899.7405841 | source=windows | frequency_hz=183.2 | rms=202 | updated_at=1777902896.2423594
- [2026-05-04 21:54:59] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777902899.96393 | source=windows | frequency_hz=183.2 | rms=202 | updated_at=1777902896.2423594
- [2026-05-04 21:55:00] operator / voice_transcript_partial / voice: enable
  meta: kind=partial | timestamp=1777902900.227972 | source=windows | frequency_hz=183.2 | rms=202 | updated_at=1777902896.2423594
- [2026-05-04 21:55:00] operator / voice_transcript_partial / voice: enable the
  meta: kind=partial | timestamp=1777902900.9034147 | source=windows | frequency_hz=183.2 | rms=202 | updated_at=1777902896.2423594
- [2026-05-04 21:55:01] operator / voice_transcript_final / voice: the enabler
  meta: kind=final | timestamp=1777902901.1298807 | source=final | confidence=0.21 | frequency_hz=183.2 | rms=202 | updated_at=1777902896.2423594
- [2026-05-04 21:55:06] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 21:55:09] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777902909.5808506 | source=windows | frequency_hz=183.2 | rms=202 | updated_at=1777902896.2423594
- [2026-05-04 21:55:17] operator / voice_transcript_final / voice: to
  meta: kind=final | timestamp=1777902917.9030974 | source=final | confidence=0.77 | frequency_hz=183.2 | rms=202 | updated_at=1777902896.2423594
- [2026-05-04 21:55:18] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777902918.701919 | source=windows | frequency_hz=273.4 | rms=193 | updated_at=1777902918.6609461
- [2026-05-04 21:55:19] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777902919.1172273 | source=windows | frequency_hz=273.4 | rms=193 | updated_at=1777902918.6609461
- [2026-05-04 21:55:19] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777902919.3339152 | source=windows | frequency_hz=273.4 | rms=193 | updated_at=1777902918.6609461
- [2026-05-04 21:55:19] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777902919.7384474 | source=windows | frequency_hz=273.4 | rms=193 | updated_at=1777902918.6609461
- [2026-05-04 21:55:21] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777902921.570759 | source=windows | frequency_hz=277.3 | rms=120 | updated_at=1777902921.0903027
- [2026-05-04 21:55:21] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777902921.9796255 | source=windows | frequency_hz=277.3 | rms=120 | updated_at=1777902921.0903027
- [2026-05-04 21:55:23] operator / voice_transcript_final / voice: fifth
  meta: kind=final | timestamp=1777902923.4593015 | source=final | confidence=0.24 | frequency_hz=277.3 | rms=120 | updated_at=1777902921.0903027
- [2026-05-04 21:55:24] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777902924.9045033 | source=windows | frequency_hz=277.3 | rms=120 | updated_at=1777902921.0903027
- [2026-05-04 21:55:25] operator / voice_transcript_partial / voice: to keep
  meta: kind=partial | timestamp=1777902925.530674 | source=windows | frequency_hz=277.3 | rms=120 | updated_at=1777902921.0903027
- [2026-05-04 21:55:26] operator / voice_transcript_partial / voice: to eighth
  meta: kind=partial | timestamp=1777902926.3436737 | source=windows | frequency_hz=277.3 | rms=120 | updated_at=1777902921.0903027
- [2026-05-04 21:55:26] operator / voice_transcript_partial / voice: to eighth to
  meta: kind=partial | timestamp=1777902926.7536047 | source=windows | frequency_hz=277.3 | rms=120 | updated_at=1777902921.0903027
- [2026-05-04 21:55:26] operator / voice_transcript_partial / voice: to keep up
  meta: kind=partial | timestamp=1777902926.956482 | source=windows | frequency_hz=277.3 | rms=120 | updated_at=1777902921.0903027
- [2026-05-04 21:55:27] operator / voice_transcript_partial / voice: to keep up with
  meta: kind=partial | timestamp=1777902927.375132 | source=windows | frequency_hz=277.3 | rms=120 | updated_at=1777902921.0903027
- [2026-05-04 21:55:27] operator / voice_transcript_partial / voice: to keep up to fifty
  meta: kind=partial | timestamp=1777902927.7845285 | source=windows | frequency_hz=277.3 | rms=120 | updated_at=1777902921.0903027
- [2026-05-04 21:55:27] operator / voice_transcript_partial / voice: to keep up
  meta: kind=partial | timestamp=1777902927.9985514 | source=windows | frequency_hz=277.3 | rms=120 | updated_at=1777902921.0903027
- [2026-05-04 21:55:28] operator / voice_transcript_partial / voice: to keep fifth
  meta: kind=partial | timestamp=1777902928.4022968 | source=windows | frequency_hz=277.3 | rms=120 | updated_at=1777902921.0903027
- [2026-05-04 21:55:29] operator / voice_transcript_partial / voice: to keep fifth to
  meta: kind=partial | timestamp=1777902929.0119634 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:29] operator / voice_transcript_partial / voice: to keep fifth to eighth
  meta: kind=partial | timestamp=1777902929.2111514 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:29] operator / voice_transcript_partial / voice: to keep fifth to eighth to
  meta: kind=partial | timestamp=1777902929.415171 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:29] operator / voice_transcript_partial / voice: to keep fifth to eighth up to
  meta: kind=partial | timestamp=1777902929.834151 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:30] operator / voice_transcript_partial / voice: to keep fifth to eighth up
  meta: kind=partial | timestamp=1777902930.2410603 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:30] operator / voice_transcript_partial / voice: to keep fifth to eighth up to
  meta: kind=partial | timestamp=1777902930.4486766 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:30] operator / voice_transcript_final / voice: to keep fifth to eighth up to
  meta: kind=final | timestamp=1777902930.8551064 | source=final | confidence=0.31 | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:31] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777902931.6642706 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:31] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777902931.8653686 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:32] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777902932.0810034 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:32] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777902932.2866714 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:32] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777902932.694349 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:32] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777902932.898037 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:33] operator / voice_transcript_partial / voice: fifty to fifty
  meta: kind=partial | timestamp=1777902933.1037564 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:33] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777902933.8153644 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:34] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777902934.8132362 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:34] operator / voice_transcript_partial / voice: fifth to sixth
  meta: kind=partial | timestamp=1777902934.8142369 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:35] operator / voice_transcript_final / voice: fifth to sixth
  meta: kind=final | timestamp=1777902935.4526584 | source=final | confidence=0.26 | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:35] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777902935.8587573 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:36] operator / voice_transcript_partial / voice: fifteen to
  meta: kind=partial | timestamp=1777902936.6705818 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:36] operator / voice_transcript_partial / voice: to keep
  meta: kind=partial | timestamp=1777902936.875174 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:37] operator / voice_transcript_partial / voice: to keep to
  meta: kind=partial | timestamp=1777902937.4844673 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:37] operator / voice_transcript_partial / voice: to keep up to
  meta: kind=partial | timestamp=1777902937.6862607 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:38] operator / voice_transcript_partial / voice: to keep up to keep
  meta: kind=partial | timestamp=1777902938.7476037 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:38] operator / voice_transcript_partial / voice: to keep up to fifth
  meta: kind=partial | timestamp=1777902938.965926 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:39] operator / voice_transcript_partial / voice: to keep up to fifth to eighth
  meta: kind=partial | timestamp=1777902939.8173504 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:40] operator / voice_transcript_partial / voice: to keep up to fifth to eighth to
  meta: kind=partial | timestamp=1777902940.257734 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:41] operator / voice_transcript_partial / voice: to keep up to fifth to eighth to tenth
  meta: kind=partial | timestamp=1777902941.0951545 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:42] operator / voice_transcript_final / voice: to keep up to fifth to eighth to 10th
  meta: kind=final | timestamp=1777902942.1348457 | source=final | confidence=0.57 | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:42] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777902942.1358461 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:42] operator / voice_transcript_partial / voice: to keep
  meta: kind=partial | timestamp=1777902942.3254101 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:42] operator / voice_transcript_partial / voice: to fifteen
  meta: kind=partial | timestamp=1777902942.528756 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:43] operator / voice_transcript_partial / voice: to fifth
  meta: kind=partial | timestamp=1777902943.7453368 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:44] operator / voice_transcript_partial / voice: to fifth to
  meta: kind=partial | timestamp=1777902944.977457 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:45] operator / voice_transcript_partial / voice: to fifth to eighth
  meta: kind=partial | timestamp=1777902945.4166923 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:46] operator / voice_transcript_partial / voice: to fifth to eighth to
  meta: kind=partial | timestamp=1777902946.4572885 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:46] operator / voice_transcript_partial / voice: to fifth to eighth fifth
  meta: kind=partial | timestamp=1777902946.6610155 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:47] operator / voice_transcript_final / voice: to fifth to eighth 5th
  meta: kind=final | timestamp=1777902947.0649807 | source=final | confidence=0.39 | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:47] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777902947.6730971 | source=windows | frequency_hz=339.8 | rms=141 | updated_at=1777902928.907809
- [2026-05-04 21:55:48] operator / voice_transcript_partial / voice: up
  meta: kind=partial | timestamp=1777902948.7125847 | source=windows | frequency_hz=365.5 | rms=134 | updated_at=1777902948.6433773
- [2026-05-04 21:55:49] operator / voice_transcript_partial / voice: to eighth
  meta: kind=partial | timestamp=1777902949.5195794 | source=windows | frequency_hz=365.5 | rms=134 | updated_at=1777902948.6433773
- [2026-05-04 21:55:50] operator / voice_transcript_partial / voice: to eighth to
  meta: kind=partial | timestamp=1777902950.1276517 | source=windows | frequency_hz=365.5 | rms=134 | updated_at=1777902948.6433773
- [2026-05-04 21:55:50] operator / voice_transcript_final / voice: to eighth to
  meta: kind=final | timestamp=1777902950.7392216 | source=final | confidence=0.22 | frequency_hz=365.5 | rms=134 | updated_at=1777902948.6433773
- [2026-05-04 21:55:51] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777902951.1416519 | source=windows | frequency_hz=365.5 | rms=134 | updated_at=1777902948.6433773
- [2026-05-04 21:55:51] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777902951.1416519 | source=windows | frequency_hz=365.5 | rms=134 | updated_at=1777902948.6433773
- [2026-05-04 21:55:51] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777902951.5632453 | source=windows | frequency_hz=365.5 | rms=134 | updated_at=1777902948.6433773
- [2026-05-04 21:55:52] operator / voice_transcript_partial / voice: fifty to
  meta: kind=partial | timestamp=1777902952.377045 | source=windows | frequency_hz=282.8 | rms=244 | updated_at=1777902952.2024543
- [2026-05-04 21:55:52] operator / voice_transcript_partial / voice: fifty two to
  meta: kind=partial | timestamp=1777902952.7835822 | source=windows | frequency_hz=282.8 | rms=244 | updated_at=1777902952.2024543
- [2026-05-04 21:55:52] operator / voice_transcript_partial / voice: fifty to keep
  meta: kind=partial | timestamp=1777902952.99847 | source=windows | frequency_hz=276.8 | rms=120 | updated_at=1777902952.8442752
- [2026-05-04 21:55:53] operator / voice_transcript_partial / voice: fifty to keep to
  meta: kind=partial | timestamp=1777902953.419956 | source=windows | frequency_hz=276.8 | rms=120 | updated_at=1777902952.8442752
- [2026-05-04 21:55:53] operator / voice_transcript_partial / voice: fifty to fifty to fifty
  meta: kind=partial | timestamp=1777902953.622921 | source=windows | frequency_hz=276.8 | rms=120 | updated_at=1777902952.8442752
- [2026-05-04 21:55:54] operator / voice_transcript_partial / voice: fifty to keep fifth
  meta: kind=partial | timestamp=1777902954.2300751 | source=windows | frequency_hz=267.3 | rms=144 | updated_at=1777902954.1227245
- [2026-05-04 21:55:54] operator / voice_transcript_partial / voice: fifty to keep fifth to
  meta: kind=partial | timestamp=1777902954.6426852 | source=windows | frequency_hz=267.3 | rms=144 | updated_at=1777902954.1227245
- [2026-05-04 21:55:55] operator / voice_transcript_partial / voice: fifty to fifty to fifty to fifty
  meta: kind=partial | timestamp=1777902955.0401335 | source=windows | frequency_hz=267.3 | rms=144 | updated_at=1777902954.1227245
- [2026-05-04 21:55:55] operator / voice_transcript_partial / voice: fifty to keep fifth to eighth
  meta: kind=partial | timestamp=1777902955.2414587 | source=windows | frequency_hz=267.3 | rms=144 | updated_at=1777902954.1227245
- [2026-05-04 21:55:56] operator / voice_transcript_final / voice: 50 to keep fifth to eighth
  meta: kind=final | timestamp=1777902956.068192 | source=final | confidence=0.53 | frequency_hz=267.3 | rms=144 | updated_at=1777902954.1227245
- [2026-05-04 21:55:57] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777902957.4759564 | source=windows | frequency_hz=267.3 | rms=144 | updated_at=1777902954.1227245
- [2026-05-04 21:55:58] operator / voice_transcript_partial / voice: to fifty
  meta: kind=partial | timestamp=1777902958.0887878 | source=windows | frequency_hz=267.3 | rms=144 | updated_at=1777902954.1227245
- [2026-05-04 21:55:58] operator / voice_transcript_partial / voice: to fifty to
  meta: kind=partial | timestamp=1777902958.5072093 | source=windows | frequency_hz=267.3 | rms=144 | updated_at=1777902954.1227245
- [2026-05-04 21:55:59] operator / voice_transcript_partial / voice: to fifty fifths
  meta: kind=partial | timestamp=1777902959.1182263 | source=windows | frequency_hz=267.3 | rms=144 | updated_at=1777902954.1227245
- [2026-05-04 21:55:59] operator / voice_transcript_partial / voice: to fifty fifths to
  meta: kind=partial | timestamp=1777902959.529616 | source=windows | frequency_hz=267.3 | rms=144 | updated_at=1777902954.1227245
- [2026-05-04 21:55:59] operator / voice_transcript_partial / voice: to fifty to its fifth
  meta: kind=partial | timestamp=1777902959.9367409 | source=windows | frequency_hz=267.3 | rms=144 | updated_at=1777902954.1227245
- [2026-05-04 21:56:00] operator / voice_transcript_final / voice: to 50 to its fifth
  meta: kind=final | timestamp=1777902960.184617 | source=final | confidence=0.75 | frequency_hz=267.3 | rms=144 | updated_at=1777902954.1227245
- [2026-05-04 21:56:01] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777902961.0524862 | source=windows | frequency_hz=267.3 | rms=144 | updated_at=1777902954.1227245
- [2026-05-04 21:56:01] operator / voice_transcript_partial / voice: to eighth
  meta: kind=partial | timestamp=1777902961.254847 | source=windows | frequency_hz=267.3 | rms=144 | updated_at=1777902954.1227245
- [2026-05-04 21:56:01] operator / voice_transcript_partial / voice: to fifty
  meta: kind=partial | timestamp=1777902961.4571414 | source=windows | frequency_hz=267.3 | rms=144 | updated_at=1777902954.1227245
- [2026-05-04 21:56:02] operator / voice_transcript_partial / voice: to eighth
  meta: kind=partial | timestamp=1777902962.0665154 | source=windows | frequency_hz=267.3 | rms=144 | updated_at=1777902954.1227245
- [2026-05-04 21:56:04] operator / voice_transcript_partial / voice: to eighth to
  meta: kind=partial | timestamp=1777902964.564069 | source=windows | frequency_hz=418.0 | rms=182 | updated_at=1777902964.2320888
- [2026-05-04 21:56:04] operator / voice_transcript_partial / voice: to eighth to to
  meta: kind=partial | timestamp=1777902964.7899358 | source=windows | frequency_hz=418.0 | rms=182 | updated_at=1777902964.2320888
- [2026-05-04 21:56:04] operator / voice_transcript_partial / voice: to eighth to ten
  meta: kind=partial | timestamp=1777902964.9927528 | source=windows | frequency_hz=418.0 | rms=182 | updated_at=1777902964.2320888
- [2026-05-04 21:56:05] operator / voice_transcript_final / voice: to eighth to 10
  meta: kind=final | timestamp=1777902965.4060009 | source=final | confidence=0.2 | frequency_hz=418.0 | rms=182 | updated_at=1777902964.2320888
- [2026-05-04 21:56:07] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777902967.8912961 | source=windows | frequency_hz=418.0 | rms=182 | updated_at=1777902964.2320888
- [2026-05-04 21:56:08] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777902968.0939212 | source=windows | frequency_hz=418.0 | rms=182 | updated_at=1777902964.2320888
- [2026-05-04 21:56:08] operator / voice_transcript_partial / voice: fifteen to
  meta: kind=partial | timestamp=1777902968.3083825 | source=windows | frequency_hz=418.0 | rms=182 | updated_at=1777902964.2320888
- [2026-05-04 21:56:08] operator / voice_transcript_final / voice: 15 to
  meta: kind=final | timestamp=1777902968.9428577 | source=final | confidence=0.29 | frequency_hz=418.0 | rms=182 | updated_at=1777902964.2320888
- [2026-05-04 21:56:09] operator / voice_transcript_partial / voice: two
  meta: kind=partial | timestamp=1777902969.3864784 | source=windows | frequency_hz=418.0 | rms=182 | updated_at=1777902964.2320888
- [2026-05-04 21:56:09] operator / voice_transcript_partial / voice: ten
  meta: kind=partial | timestamp=1777902969.600474 | source=windows | frequency_hz=418.0 | rms=182 | updated_at=1777902964.2320888
- [2026-05-04 21:56:09] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777902969.600474 | source=windows | frequency_hz=418.0 | rms=182 | updated_at=1777902964.2320888
- [2026-05-04 21:56:10] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777902970.241447 | source=windows | frequency_hz=418.0 | rms=182 | updated_at=1777902964.2320888
- [2026-05-04 21:56:10] operator / voice_transcript_final / voice: fifth
  meta: kind=final | timestamp=1777902970.6439178 | source=final | confidence=0.84 | frequency_hz=418.0 | rms=182 | updated_at=1777902964.2320888
- [2026-05-04 21:56:11] operator / voice_transcript_partial / voice: up
  meta: kind=partial | timestamp=1777902971.9035132 | source=windows | frequency_hz=418.0 | rms=182 | updated_at=1777902964.2320888
- [2026-05-04 21:56:12] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 21:56:12] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777902972.1092248 | source=windows | frequency_hz=418.0 | rms=182 | updated_at=1777902964.2320888
- [2026-05-04 21:56:12] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777902972.7368708 | source=windows | frequency_hz=418.0 | rms=182 | updated_at=1777902964.2320888
- [2026-05-04 21:56:13] operator / voice_transcript_partial / voice: fifth to sixth
  meta: kind=partial | timestamp=1777902973.156237 | source=windows | frequency_hz=371.1 | rms=147 | updated_at=1777902972.8022964
- [2026-05-04 21:56:13] operator / voice_transcript_partial / voice: fifth to sixth to
  meta: kind=partial | timestamp=1777902973.3607197 | source=windows | frequency_hz=371.1 | rms=147 | updated_at=1777902972.8022964
- [2026-05-04 21:56:14] operator / voice_transcript_partial / voice: fifth fifth to
  meta: kind=partial | timestamp=1777902974.1816337 | source=windows | frequency_hz=371.1 | rms=147 | updated_at=1777902972.8022964
- [2026-05-04 21:56:14] operator / voice_transcript_partial / voice: up fifty to fifty
  meta: kind=partial | timestamp=1777902974.3868492 | source=windows | frequency_hz=371.1 | rms=147 | updated_at=1777902972.8022964
- [2026-05-04 21:56:14] operator / voice_transcript_partial / voice: fifth fifth to eighth
  meta: kind=partial | timestamp=1777902974.7930694 | source=windows | frequency_hz=371.1 | rms=147 | updated_at=1777902972.8022964
- [2026-05-04 21:56:15] operator / voice_transcript_partial / voice: fifth fifth to eighth up
  meta: kind=partial | timestamp=1777902975.8058026 | source=windows | frequency_hz=168.0 | rms=202 | updated_at=1777902975.1181126
- [2026-05-04 21:56:16] operator / voice_transcript_partial / voice: fifth fifth to eighth
  meta: kind=partial | timestamp=1777902976.4272907 | source=windows | frequency_hz=168.0 | rms=202 | updated_at=1777902975.1181126
- [2026-05-04 21:56:18] operator / voice_transcript_partial / voice: fifth fifth to eighth to
  meta: kind=partial | timestamp=1777902978.3766801 | source=windows | frequency_hz=168.0 | rms=202 | updated_at=1777902975.1181126
- [2026-05-04 21:56:18] operator / voice_transcript_partial / voice: fifth fifth to eighth up to
  meta: kind=partial | timestamp=1777902978.793078 | source=windows | frequency_hz=168.0 | rms=202 | updated_at=1777902975.1181126
- [2026-05-04 21:56:19] operator / voice_transcript_partial / voice: fifth fifth to eighth up to the
  meta: kind=partial | timestamp=1777902979.4029372 | source=windows | frequency_hz=355.5 | rms=363 | updated_at=1777902978.9519546
- [2026-05-04 21:56:20] operator / voice_transcript_partial / voice: fifth fifth to eighth up to that of
  meta: kind=partial | timestamp=1777902980.028461 | source=windows | frequency_hz=355.5 | rms=363 | updated_at=1777902978.9519546
- [2026-05-04 21:56:20] operator / voice_transcript_partial / voice: fifth fifth to eighth up to the fifth
  meta: kind=partial | timestamp=1777902980.2720559 | source=windows | frequency_hz=355.5 | rms=363 | updated_at=1777902978.9519546
- [2026-05-04 21:56:20] operator / voice_transcript_final / voice: fifth 5th to eighth up to the fifth
  meta: kind=final | timestamp=1777902980.876475 | source=final | confidence=0.37 | frequency_hz=355.5 | rms=363 | updated_at=1777902978.9519546
- [2026-05-04 21:56:28] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777902988.7970798 | source=windows | frequency_hz=402.3 | rms=122 | updated_at=1777902981.005438
- [2026-05-04 21:56:29] operator / voice_transcript_partial / voice: to eighth
  meta: kind=partial | timestamp=1777902989.2042856 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:29] operator / voice_transcript_partial / voice: to eighth to
  meta: kind=partial | timestamp=1777902989.6154115 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:30] operator / voice_transcript_partial / voice: to eighth to tenth
  meta: kind=partial | timestamp=1777902990.0632057 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:30] operator / voice_transcript_partial / voice: to eighth
  meta: kind=partial | timestamp=1777902990.274847 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:31] operator / voice_transcript_final / voice: to eighth
  meta: kind=final | timestamp=1777902991.5640097 | source=final | confidence=0.14 | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:32] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777902992.1647403 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:32] operator / voice_transcript_partial / voice: to ten
  meta: kind=partial | timestamp=1777902992.3678935 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:32] operator / voice_transcript_partial / voice: to tenth
  meta: kind=partial | timestamp=1777902992.5689244 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:33] operator / voice_transcript_partial / voice: to tenth to
  meta: kind=partial | timestamp=1777902993.4162543 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:33] operator / voice_transcript_partial / voice: to keep
  meta: kind=partial | timestamp=1777902993.622096 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:33] operator / voice_transcript_partial / voice: to ten fifth
  meta: kind=partial | timestamp=1777902993.8421733 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:34] operator / voice_transcript_partial / voice: to ten fifth to
  meta: kind=partial | timestamp=1777902994.7902346 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:34] operator / voice_transcript_partial / voice: to ten fifth
  meta: kind=partial | timestamp=1777902994.9944413 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:36] operator / voice_transcript_partial / voice: to ten fifth to
  meta: kind=partial | timestamp=1777902996.1298358 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:36] operator / voice_transcript_partial / voice: to ten fifth to eighth
  meta: kind=partial | timestamp=1777902996.3366985 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:36] operator / voice_transcript_partial / voice: to ten fifth to eighth to
  meta: kind=partial | timestamp=1777902996.7469363 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:37] operator / voice_transcript_partial / voice: to ten fifth to sixth to eighth
  meta: kind=partial | timestamp=1777902997.15642 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:37] operator / voice_transcript_partial / voice: to ten fifth to eighth to fifty
  meta: kind=partial | timestamp=1777902997.3593335 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:37] operator / voice_transcript_partial / voice: to ten fifth to sixth to eighth
  meta: kind=partial | timestamp=1777902997.5590131 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:38] operator / voice_transcript_partial / voice: to ten fifth to sixth to eighth up
  meta: kind=partial | timestamp=1777902998.1701806 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:38] operator / voice_transcript_partial / voice: to ten fifth to sixth to eighth uptick
  meta: kind=partial | timestamp=1777902998.3768532 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:38] operator / voice_transcript_partial / voice: to ten fifth to eighth to fifth to eighth
  meta: kind=partial | timestamp=1777902998.592214 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:39] operator / voice_transcript_partial / voice: to ten fifth to eighth to fifth to eighth to
  meta: kind=partial | timestamp=1777902999.509758 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:39] operator / voice_transcript_partial / voice: to ten fifth to eighth to fifth to eighth up
  meta: kind=partial | timestamp=1777902999.7137578 | source=windows | frequency_hz=375.0 | rms=328 | updated_at=1777902989.1919997
- [2026-05-04 21:56:40] operator / voice_transcript_partial / voice: to ten fifth to sixth to eighth fifth to eighth
  meta: kind=partial | timestamp=1777903000.1209273 | source=windows | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:40] operator / voice_transcript_final / voice: to 10 5th to sixth to eighth 5th to eighth
  meta: kind=final | timestamp=1777903000.9387617 | source=final | confidence=0.43 | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:42] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903002.3718488 | source=windows | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:42] operator / voice_transcript_partial / voice: up
  meta: kind=partial | timestamp=1777903002.5768106 | source=windows | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:42] operator / voice_transcript_partial / voice: to fifty
  meta: kind=partial | timestamp=1777903002.8077703 | source=windows | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:43] operator / voice_transcript_partial / voice: up
  meta: kind=partial | timestamp=1777903003.2250197 | source=windows | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:44] operator / voice_transcript_partial / voice: up to
  meta: kind=partial | timestamp=1777903004.0368602 | source=windows | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:44] operator / voice_transcript_partial / voice: up to death
  meta: kind=partial | timestamp=1777903004.4437387 | source=windows | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:45] operator / voice_transcript_final / voice: up to death
  meta: kind=final | timestamp=1777903005.1056616 | source=final | confidence=0.46 | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:45] operator / voice_transcript_partial / voice: if
  meta: kind=partial | timestamp=1777903005.921345 | source=windows | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:46] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777903006.3459103 | source=windows | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:46] operator / voice_transcript_partial / voice: up
  meta: kind=partial | timestamp=1777903006.5491643 | source=windows | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:47] operator / voice_transcript_partial / voice: up to
  meta: kind=partial | timestamp=1777903007.159286 | source=windows | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:47] operator / voice_transcript_final / voice: up to
  meta: kind=final | timestamp=1777903007.7804956 | source=final | confidence=0.37 | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:49] operator / voice_transcript_partial / voice: two
  meta: kind=partial | timestamp=1777903009.0158794 | source=windows | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:49] operator / voice_transcript_partial / voice: death
  meta: kind=partial | timestamp=1777903009.2211618 | source=windows | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:50] operator / voice_transcript_partial / voice: fifty fifth
  meta: kind=partial | timestamp=1777903010.0445719 | source=windows | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:50] operator / voice_transcript_partial / voice: fifty fifth to
  meta: kind=partial | timestamp=1777903010.6543887 | source=windows | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:50] operator / voice_transcript_partial / voice: fifty fifth to keep
  meta: kind=partial | timestamp=1777903010.867422 | source=windows | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:51] operator / voice_transcript_partial / voice: fifty fifth up to
  meta: kind=partial | timestamp=1777903011.2754931 | source=windows | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:51] operator / voice_transcript_partial / voice: fifty fifth to keep
  meta: kind=partial | timestamp=1777903011.5010712 | source=windows | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:51] operator / voice_transcript_partial / voice: fifty fifth to eighth
  meta: kind=partial | timestamp=1777903011.7162552 | source=windows | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:52] operator / voice_transcript_partial / voice: fifty fifth to eighth to
  meta: kind=partial | timestamp=1777903012.527065 | source=windows | frequency_hz=410.2 | rms=120 | updated_at=1777903000.0720522
- [2026-05-04 21:56:52] operator / voice_transcript_partial / voice: fifty fifth to eighth
  meta: kind=partial | timestamp=1777903012.7660644 | source=windows | frequency_hz=328.1 | rms=411 | updated_at=1777903012.615807
- [2026-05-04 21:56:53] operator / voice_transcript_partial / voice: fifty fifth to keep
  meta: kind=partial | timestamp=1777903013.0187411 | source=windows | frequency_hz=328.1 | rms=411 | updated_at=1777903012.615807
- [2026-05-04 21:56:53] operator / voice_transcript_partial / voice: fifty fifth to eighth
  meta: kind=partial | timestamp=1777903013.2576182 | source=windows | frequency_hz=328.1 | rms=411 | updated_at=1777903012.615807
- [2026-05-04 21:56:54] operator / voice_transcript_partial / voice: fifty fifth to eighth to
  meta: kind=partial | timestamp=1777903014.3083 | source=windows | frequency_hz=283.0 | rms=121 | updated_at=1777903013.38296
- [2026-05-04 21:56:54] operator / voice_transcript_partial / voice: fifty fifth to eighth to fifty
  meta: kind=partial | timestamp=1777903014.5236402 | source=windows | frequency_hz=283.0 | rms=121 | updated_at=1777903013.38296
- [2026-05-04 21:56:54] operator / voice_transcript_partial / voice: fifty fifth to eighth fifteen to
  meta: kind=partial | timestamp=1777903014.7268798 | source=windows | frequency_hz=283.0 | rms=121 | updated_at=1777903013.38296
- [2026-05-04 21:56:54] operator / voice_transcript_partial / voice: fifty fifth to eighth fifth
  meta: kind=partial | timestamp=1777903014.9313421 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:56:55] operator / voice_transcript_partial / voice: fifty fifth to eighth fifth to
  meta: kind=partial | timestamp=1777903015.5585685 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:56:55] operator / voice_transcript_partial / voice: fifty fifth to eighth fifth to eighth
  meta: kind=partial | timestamp=1777903015.7601166 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:56:56] operator / voice_transcript_final / voice: 55th to eighth 5th to eighth
  meta: kind=final | timestamp=1777903016.3693194 | source=final | confidence=0.31 | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:56:58] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903018.2385852 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:56:59] operator / voice_transcript_partial / voice: to keep
  meta: kind=partial | timestamp=1777903019.054534 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:56:59] operator / voice_transcript_partial / voice: up to
  meta: kind=partial | timestamp=1777903019.5631902 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:00] operator / voice_transcript_partial / voice: to keep to keep
  meta: kind=partial | timestamp=1777903020.674661 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:01] operator / voice_transcript_partial / voice: up to up to
  meta: kind=partial | timestamp=1777903021.3150516 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:01] operator / voice_transcript_partial / voice: up to up to fifth
  meta: kind=partial | timestamp=1777903021.9674926 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:02] operator / voice_transcript_final / voice: up to up to fifth
  meta: kind=final | timestamp=1777903022.5755353 | source=final | confidence=0.66 | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:03] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903023.8386347 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:04] operator / voice_transcript_partial / voice: to eighth
  meta: kind=partial | timestamp=1777903024.0417745 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:04] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777903024.5217102 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:05] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777903025.7530382 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:05] operator / voice_transcript_partial / voice: fifth up
  meta: kind=partial | timestamp=1777903025.9887083 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:06] operator / voice_transcript_partial / voice: fifth to eighth
  meta: kind=partial | timestamp=1777903026.4326947 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:06] operator / voice_transcript_partial / voice: fifth to eighth to
  meta: kind=partial | timestamp=1777903026.6951187 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:06] operator / voice_transcript_partial / voice: fifth to eighth
  meta: kind=partial | timestamp=1777903026.9065175 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:07] operator / voice_transcript_partial / voice: fifth to eighth to
  meta: kind=partial | timestamp=1777903027.117191 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:07] operator / voice_transcript_partial / voice: fifth to eighth to tenth to
  meta: kind=partial | timestamp=1777903027.3185296 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:07] operator / voice_transcript_partial / voice: fifth to eighth to ten
  meta: kind=partial | timestamp=1777903027.521109 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:08] operator / voice_transcript_partial / voice: fifth to eighth to tenth to
  meta: kind=partial | timestamp=1777903028.130506 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:08] operator / voice_transcript_partial / voice: fifth to eighth to ten to five
  meta: kind=partial | timestamp=1777903028.6998708 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:09] operator / voice_transcript_partial / voice: fifth to eighth to fifty to fifty
  meta: kind=partial | timestamp=1777903029.3520007 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:09] operator / voice_transcript_final / voice: fifth to eighth to 50 to 50
  meta: kind=final | timestamp=1777903029.9673066 | source=final | confidence=0.36 | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:10] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777903030.5751815 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:10] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777903030.9943993 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:11] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777903031.413432 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:11] operator / voice_transcript_partial / voice: up to
  meta: kind=partial | timestamp=1777903031.6232743 | source=windows | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:12] operator / voice_transcript_final / voice: up to
  meta: kind=final | timestamp=1777903032.427235 | source=final | confidence=0.52 | frequency_hz=347.7 | rms=146 | updated_at=1777903014.7926965
- [2026-05-04 21:57:14] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777903034.2679849 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:14] operator / voice_transcript_partial / voice: up to
  meta: kind=partial | timestamp=1777903034.4838488 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:14] operator / voice_transcript_partial / voice: to to to
  meta: kind=partial | timestamp=1777903034.8888607 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:15] operator / voice_transcript_partial / voice: up to fifth
  meta: kind=partial | timestamp=1777903035.104461 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:15] operator / voice_transcript_partial / voice: to to to to
  meta: kind=partial | timestamp=1777903035.3118296 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:15] operator / voice_transcript_final / voice: to to to to
  meta: kind=final | timestamp=1777903035.5288687 | source=final | confidence=0.69 | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:15] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777903035.9334722 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:16] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777903036.7951868 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:17] operator / voice_transcript_partial / voice: keep up to
  meta: kind=partial | timestamp=1777903037.0149107 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:17] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 21:57:17] operator / voice_transcript_final / voice: keep up to
  meta: kind=final | timestamp=1777903037.6537616 | source=final | confidence=0.29 | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:18] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777903038.0507617 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:18] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777903038.2553818 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:18] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777903038.6745887 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:19] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777903039.092391 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:19] operator / voice_transcript_partial / voice: fifty fifth
  meta: kind=partial | timestamp=1777903039.2954357 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:19] operator / voice_transcript_partial / voice: fifty fifth to
  meta: kind=partial | timestamp=1777903039.9237676 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:20] operator / voice_transcript_partial / voice: fifty fifth to eighth
  meta: kind=partial | timestamp=1777903040.1365962 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:21] operator / voice_transcript_final / voice: 55th to eighth
  meta: kind=final | timestamp=1777903041.0111306 | source=final | confidence=0.68 | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:21] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903041.400382 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:22] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777903042.0091717 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:22] operator / voice_transcript_partial / voice: to fifty
  meta: kind=partial | timestamp=1777903042.212519 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:23] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777903043.2291365 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:23] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777903043.4346497 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:24] operator / voice_transcript_partial / voice: fifth to to
  meta: kind=partial | timestamp=1777903044.4473877 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:24] operator / voice_transcript_partial / voice: to fifty to fifty
  meta: kind=partial | timestamp=1777903044.7088873 | source=windows | frequency_hz=347.7 | rms=129 | updated_at=1777903034.123165
- [2026-05-04 21:57:25] operator / voice_transcript_partial / voice: fifth to to keep
  meta: kind=partial | timestamp=1777903045.1373916 | source=windows | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:26] operator / voice_transcript_partial / voice: fifth to to keep up to
  meta: kind=partial | timestamp=1777903046.1699555 | source=windows | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:26] operator / voice_transcript_partial / voice: to fifty to fifty to fifty to fifty
  meta: kind=partial | timestamp=1777903046.3719575 | source=windows | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:27] operator / voice_transcript_final / voice: to 50 to 50 to 50 to 50
  meta: kind=final | timestamp=1777903047.1814413 | source=final | confidence=0.42 | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:27] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903047.3819678 | source=windows | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:27] operator / voice_transcript_partial / voice: to fifty
  meta: kind=partial | timestamp=1777903047.7828822 | source=windows | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:28] operator / voice_transcript_partial / voice: to fifty to
  meta: kind=partial | timestamp=1777903048.2033315 | source=windows | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:28] operator / voice_transcript_partial / voice: to fifty fifth
  meta: kind=partial | timestamp=1777903048.6122296 | source=windows | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:28] operator / voice_transcript_partial / voice: to fifty fifth to
  meta: kind=partial | timestamp=1777903048.8273938 | source=windows | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:29] operator / voice_transcript_partial / voice: to fifty fifth
  meta: kind=partial | timestamp=1777903049.0602593 | source=windows | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:29] operator / voice_transcript_partial / voice: to fifty fifth to
  meta: kind=partial | timestamp=1777903049.4632492 | source=windows | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:29] operator / voice_transcript_partial / voice: to fifty fifth to sixth
  meta: kind=partial | timestamp=1777903049.6671329 | source=windows | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:30] operator / voice_transcript_partial / voice: to fifty fifth to sixth in
  meta: kind=partial | timestamp=1777903050.3637948 | source=windows | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:31] operator / voice_transcript_final / voice: to 55th to sixth in
  meta: kind=final | timestamp=1777903051.1901233 | source=final | confidence=0.43 | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:39] operator / voice_transcript_partial / voice: deep
  meta: kind=partial | timestamp=1777903059.0779054 | source=windows | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:41] operator / voice_transcript_partial / voice: up to
  meta: kind=partial | timestamp=1777903061.1667445 | source=windows | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:41] operator / voice_transcript_final / voice: up to
  meta: kind=final | timestamp=1777903061.4308639 | source=final | confidence=0.47 | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:42] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777903062.6649926 | source=windows | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:42] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777903062.866645 | source=windows | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:43] operator / voice_transcript_final / voice: fifth
  meta: kind=final | timestamp=1777903063.6978753 | source=final | confidence=0.81 | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:46] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903066.767609 | source=windows | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:48] operator / voice_transcript_partial / voice: to eighth
  meta: kind=partial | timestamp=1777903068.8719985 | source=windows | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:50] operator / voice_transcript_final / voice: to eighth
  meta: kind=final | timestamp=1777903070.2959478 | source=final | confidence=0.36 | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:50] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903070.4972956 | source=windows | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:50] operator / voice_transcript_partial / voice: to fifty
  meta: kind=partial | timestamp=1777903070.9052474 | source=windows | frequency_hz=339.8 | rms=134 | updated_at=1777903044.8734655
- [2026-05-04 21:57:51] operator / voice_transcript_partial / voice: up
  meta: kind=partial | timestamp=1777903071.9150622 | source=windows | frequency_hz=253.9 | rms=163 | updated_at=1777903071.4938648
- [2026-05-04 21:57:52] operator / voice_transcript_partial / voice: to fifth
  meta: kind=partial | timestamp=1777903072.129756 | source=windows | frequency_hz=253.9 | rms=163 | updated_at=1777903071.4938648
- [2026-05-04 21:57:52] operator / voice_transcript_final / voice: to fifth
  meta: kind=final | timestamp=1777903072.7512617 | source=final | confidence=0.44 | frequency_hz=253.9 | rms=163 | updated_at=1777903071.4938648
- [2026-05-04 21:57:54] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903074.60314 | source=windows | frequency_hz=253.9 | rms=163 | updated_at=1777903071.4938648
- [2026-05-04 21:57:55] operator / voice_transcript_partial / voice: to keep
  meta: kind=partial | timestamp=1777903075.025944 | source=windows | frequency_hz=238.3 | rms=180 | updated_at=1777903074.7008896
- [2026-05-04 21:57:55] operator / voice_transcript_partial / voice: to keep a
  meta: kind=partial | timestamp=1777903075.24077 | source=windows | frequency_hz=238.3 | rms=180 | updated_at=1777903074.7008896
- [2026-05-04 21:57:55] operator / voice_transcript_partial / voice: to keep to
  meta: kind=partial | timestamp=1777903075.4422727 | source=windows | frequency_hz=238.3 | rms=180 | updated_at=1777903074.7008896
- [2026-05-04 21:57:55] operator / voice_transcript_partial / voice: to fifty to fifty
  meta: kind=partial | timestamp=1777903075.647364 | source=windows | frequency_hz=238.3 | rms=180 | updated_at=1777903074.7008896
- [2026-05-04 21:57:56] operator / voice_transcript_partial / voice: to to to to to to
  meta: kind=partial | timestamp=1777903076.0831928 | source=windows | frequency_hz=238.3 | rms=180 | updated_at=1777903074.7008896
- [2026-05-04 21:57:56] operator / voice_transcript_partial / voice: to to to to to keep
  meta: kind=partial | timestamp=1777903076.2860763 | source=windows | frequency_hz=238.3 | rms=180 | updated_at=1777903074.7008896
- [2026-05-04 21:57:56] operator / voice_transcript_partial / voice: to up to fifth to eighth
  meta: kind=partial | timestamp=1777903076.4899359 | source=windows | frequency_hz=238.3 | rms=180 | updated_at=1777903074.7008896
- [2026-05-04 21:57:56] operator / voice_transcript_partial / voice: to up to fifth to eighth to
  meta: kind=partial | timestamp=1777903076.691137 | source=windows | frequency_hz=238.3 | rms=180 | updated_at=1777903074.7008896
- [2026-05-04 21:57:56] operator / voice_transcript_partial / voice: to up to fifth to eighth to fifty
  meta: kind=partial | timestamp=1777903076.895621 | source=windows | frequency_hz=238.3 | rms=180 | updated_at=1777903074.7008896
- [2026-05-04 21:57:57] operator / voice_transcript_partial / voice: to to to to to keep up
  meta: kind=partial | timestamp=1777903077.299685 | source=windows | frequency_hz=238.3 | rms=180 | updated_at=1777903074.7008896
- [2026-05-04 21:57:57] operator / voice_transcript_partial / voice: to up to fifth to eighth up to
  meta: kind=partial | timestamp=1777903077.5024362 | source=windows | frequency_hz=238.3 | rms=180 | updated_at=1777903074.7008896
- [2026-05-04 21:57:57] operator / voice_transcript_partial / voice: to up to fifth to eighth up fifth
  meta: kind=partial | timestamp=1777903077.9078543 | source=windows | frequency_hz=238.3 | rms=180 | updated_at=1777903074.7008896
- [2026-05-04 21:57:58] operator / voice_transcript_partial / voice: to up to fifth to eighth up fifth to
  meta: kind=partial | timestamp=1777903078.7353485 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:57:59] operator / voice_transcript_partial / voice: to up to fifth to eighth up fifth to eighth
  meta: kind=partial | timestamp=1777903079.3908925 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:57:59] operator / voice_transcript_partial / voice: to up to fifth to eighth up fifth to keep
  meta: kind=partial | timestamp=1777903079.5926275 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:00] operator / voice_transcript_partial / voice: to up to fifth to eighth up fifth to keep up
  meta: kind=partial | timestamp=1777903080.200471 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:01] operator / voice_transcript_partial / voice: to up to fifth to eighth up fifth to eighth
  meta: kind=partial | timestamp=1777903081.2149465 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:02] operator / voice_transcript_partial / voice: to up to fifth to eighth up fifth to eighth up
  meta: kind=partial | timestamp=1777903082.0724542 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:02] operator / voice_transcript_partial / voice: to up to fifth to eighth up fifth to eighth up to
  meta: kind=partial | timestamp=1777903082.490069 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:03] operator / voice_transcript_partial / voice: to up to fifth to eighth up fifth to eighth up to fifty
  meta: kind=partial | timestamp=1777903083.098336 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:03] operator / voice_transcript_partial / voice: to up to fifth to eighth up fifth to eighth up fifth
  meta: kind=partial | timestamp=1777903083.3079062 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:03] operator / voice_transcript_final / voice: to up to fifth to eighth up fifth to eighth up fifth
  meta: kind=final | timestamp=1777903083.965616 | source=final | confidence=0.54 | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:05] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903085.8515463 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:06] operator / voice_transcript_partial / voice: to sixth
  meta: kind=partial | timestamp=1777903086.2567172 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:06] operator / voice_transcript_partial / voice: to sixth to
  meta: kind=partial | timestamp=1777903086.868571 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:07] operator / voice_transcript_partial / voice: to sixth
  meta: kind=partial | timestamp=1777903087.284241 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:08] operator / voice_transcript_partial / voice: to sixth to
  meta: kind=partial | timestamp=1777903088.719407 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:09] operator / voice_transcript_partial / voice: to sixth
  meta: kind=partial | timestamp=1777903089.1120965 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:09] operator / voice_transcript_partial / voice: to sixth to
  meta: kind=partial | timestamp=1777903089.7384732 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:10] operator / voice_transcript_final / voice: to sixth to
  meta: kind=final | timestamp=1777903090.5774486 | source=final | confidence=0.18 | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:15] operator / voice_transcript_partial / voice: ten
  meta: kind=partial | timestamp=1777903095.3656445 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:15] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777903095.5597992 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:15] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777903095.9634922 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:16] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777903096.569054 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:16] operator / voice_transcript_partial / voice: eighth to tenth
  meta: kind=partial | timestamp=1777903096.771702 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:17] operator / voice_transcript_partial / voice: eighth to tenth to
  meta: kind=partial | timestamp=1777903097.0084944 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:17] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777903097.3085253 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:17] operator / voice_transcript_partial / voice: fifty to fifty to fifty
  meta: kind=partial | timestamp=1777903097.5125732 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:18] operator / voice_transcript_partial / voice: fifty to fifty to fifty to
  meta: kind=partial | timestamp=1777903098.3331249 | source=windows | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:18] operator / voice_transcript_final / voice: 50 to 50 to 50 to
  meta: kind=final | timestamp=1777903098.958799 | source=final | confidence=0.56 | frequency_hz=378.9 | rms=157 | updated_at=1777903078.0240836
- [2026-05-04 21:58:21] operator / voice_transcript_partial / voice: two
  meta: kind=partial | timestamp=1777903101.9059532 | source=windows | frequency_hz=308.6 | rms=175 | updated_at=1777903101.1945264
- [2026-05-04 21:58:22] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777903102.30988 | source=windows | frequency_hz=308.6 | rms=175 | updated_at=1777903101.1945264
- [2026-05-04 21:58:22] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 21:58:22] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777903102.5132816 | source=windows | frequency_hz=308.6 | rms=175 | updated_at=1777903101.1945264
- [2026-05-04 21:58:23] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777903103.3246112 | source=windows | frequency_hz=308.6 | rms=175 | updated_at=1777903101.1945264
- [2026-05-04 21:58:23] operator / voice_transcript_partial / voice: keep to death
  meta: kind=partial | timestamp=1777903103.527232 | source=windows | frequency_hz=308.6 | rms=175 | updated_at=1777903101.1945264
- [2026-05-04 21:58:24] operator / voice_transcript_final / voice: keep to death
  meta: kind=final | timestamp=1777903104.1392446 | source=final | confidence=0.5 | frequency_hz=308.6 | rms=175 | updated_at=1777903101.1945264
- [2026-05-04 21:58:24] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903104.3532526 | source=windows | frequency_hz=308.6 | rms=175 | updated_at=1777903101.1945264
- [2026-05-04 21:58:24] operator / voice_transcript_partial / voice: up
  meta: kind=partial | timestamp=1777903104.9766338 | source=windows | frequency_hz=308.6 | rms=175 | updated_at=1777903101.1945264
- [2026-05-04 21:58:25] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777903105.8075526 | source=windows | frequency_hz=308.6 | rms=175 | updated_at=1777903101.1945264
- [2026-05-04 21:58:26] operator / voice_transcript_partial / voice: up
  meta: kind=partial | timestamp=1777903106.2153487 | source=windows | frequency_hz=308.6 | rms=175 | updated_at=1777903101.1945264
- [2026-05-04 21:58:27] operator / voice_transcript_partial / voice: up to
  meta: kind=partial | timestamp=1777903107.1593773 | source=windows | frequency_hz=308.6 | rms=175 | updated_at=1777903101.1945264
- [2026-05-04 21:58:27] operator / voice_transcript_partial / voice: to keep up
  meta: kind=partial | timestamp=1777903107.7709835 | source=windows | frequency_hz=308.6 | rms=175 | updated_at=1777903101.1945264
- [2026-05-04 21:58:27] operator / voice_transcript_partial / voice: up to fifth
  meta: kind=partial | timestamp=1777903107.974556 | source=windows | frequency_hz=308.6 | rms=175 | updated_at=1777903101.1945264
- [2026-05-04 21:58:28] operator / voice_transcript_partial / voice: up to fifth to
  meta: kind=partial | timestamp=1777903108.3924632 | source=windows | frequency_hz=308.6 | rms=175 | updated_at=1777903101.1945264
- [2026-05-04 21:58:28] operator / voice_transcript_partial / voice: up to fifth up
  meta: kind=partial | timestamp=1777903108.608144 | source=windows | frequency_hz=386.7 | rms=142 | updated_at=1777903108.4838274
- [2026-05-04 21:58:28] operator / voice_transcript_partial / voice: up to fifth to eighth
  meta: kind=partial | timestamp=1777903108.8122902 | source=windows | frequency_hz=386.7 | rms=142 | updated_at=1777903108.4838274
- [2026-05-04 21:58:29] operator / voice_transcript_partial / voice: up to fifth up
  meta: kind=partial | timestamp=1777903109.2352817 | source=windows | frequency_hz=386.7 | rms=142 | updated_at=1777903108.4838274
- [2026-05-04 21:58:29] operator / voice_transcript_partial / voice: up to fifth to eighth
  meta: kind=partial | timestamp=1777903109.452853 | source=windows | frequency_hz=386.7 | rms=142 | updated_at=1777903108.4838274
- [2026-05-04 21:58:30] operator / voice_transcript_final / voice: up to fifth to eighth
  meta: kind=final | timestamp=1777903110.2939103 | source=final | confidence=0.39 | frequency_hz=386.7 | rms=142 | updated_at=1777903108.4838274
- [2026-05-04 21:58:30] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903110.8992927 | source=windows | frequency_hz=386.7 | rms=142 | updated_at=1777903108.4838274
- [2026-05-04 21:58:31] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777903111.1388695 | source=windows | frequency_hz=386.7 | rms=142 | updated_at=1777903108.4838274
- [2026-05-04 21:58:31] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777903111.5703404 | source=windows | frequency_hz=386.7 | rms=142 | updated_at=1777903108.4838274
- [2026-05-04 21:58:31] operator / voice_transcript_partial / voice: fifth to eighth
  meta: kind=partial | timestamp=1777903111.7722776 | source=windows | frequency_hz=386.7 | rms=142 | updated_at=1777903108.4838274
- [2026-05-04 21:58:31] operator / voice_transcript_partial / voice: fifth to eighth to
  meta: kind=partial | timestamp=1777903111.9804072 | source=windows | frequency_hz=386.7 | rms=142 | updated_at=1777903108.4838274
- [2026-05-04 21:58:32] operator / voice_transcript_partial / voice: fifth to eighth
  meta: kind=partial | timestamp=1777903112.1741242 | source=windows | frequency_hz=386.7 | rms=142 | updated_at=1777903108.4838274
- [2026-05-04 21:58:33] operator / voice_transcript_partial / voice: fifth to eighth to
  meta: kind=partial | timestamp=1777903113.8258727 | source=windows | frequency_hz=386.7 | rms=142 | updated_at=1777903108.4838274
- [2026-05-04 21:58:34] operator / voice_transcript_partial / voice: fifth to eighth up
  meta: kind=partial | timestamp=1777903114.0417476 | source=windows | frequency_hz=386.7 | rms=142 | updated_at=1777903108.4838274
- [2026-05-04 21:58:34] operator / voice_transcript_partial / voice: fifth to eighth to fifty
  meta: kind=partial | timestamp=1777903114.2361343 | source=windows | frequency_hz=386.7 | rms=142 | updated_at=1777903108.4838274
- [2026-05-04 21:58:34] operator / voice_transcript_partial / voice: fifth to eighth to fifth
  meta: kind=partial | timestamp=1777903114.4993012 | source=windows | frequency_hz=386.7 | rms=142 | updated_at=1777903108.4838274
- [2026-05-04 21:58:34] operator / voice_transcript_partial / voice: fifth to eighth to fifty
  meta: kind=partial | timestamp=1777903114.7609766 | source=windows | frequency_hz=386.7 | rms=142 | updated_at=1777903108.4838274
- [2026-05-04 21:58:35] operator / voice_transcript_partial / voice: fifth to eighth to fifty to
  meta: kind=partial | timestamp=1777903115.019649 | source=windows | frequency_hz=210.9 | rms=129 | updated_at=1777903114.7647104
- [2026-05-04 21:58:35] operator / voice_transcript_partial / voice: fifth to eighth to fifty to two
  meta: kind=partial | timestamp=1777903115.2252285 | source=windows | frequency_hz=210.9 | rms=129 | updated_at=1777903114.7647104
- [2026-05-04 21:58:35] operator / voice_transcript_partial / voice: fifth to eighth to fifty to fifty
  meta: kind=partial | timestamp=1777903115.4394202 | source=windows | frequency_hz=210.9 | rms=129 | updated_at=1777903114.7647104
- [2026-05-04 21:58:35] operator / voice_transcript_partial / voice: fifth to eighth to fifth to sixth
  meta: kind=partial | timestamp=1777903115.641837 | source=windows | frequency_hz=210.9 | rms=129 | updated_at=1777903114.7647104
- [2026-05-04 21:58:36] operator / voice_transcript_partial / voice: fifth to eighth to fifth to sixth to
  meta: kind=partial | timestamp=1777903116.26736 | source=windows | frequency_hz=210.9 | rms=129 | updated_at=1777903114.7647104
- [2026-05-04 21:58:36] operator / voice_transcript_partial / voice: fifth to eighth to fifty to fifty to fifty
  meta: kind=partial | timestamp=1777903116.470695 | source=windows | frequency_hz=210.9 | rms=129 | updated_at=1777903114.7647104
- [2026-05-04 21:58:36] operator / voice_transcript_partial / voice: fifth to eighth to fifty to fifty to fifty to
  meta: kind=partial | timestamp=1777903116.673139 | source=windows | frequency_hz=210.9 | rms=129 | updated_at=1777903114.7647104
- [2026-05-04 21:58:37] operator / voice_transcript_partial / voice: fifth to eighth to fifth to sixth to
  meta: kind=partial | timestamp=1777903117.5362372 | source=windows | frequency_hz=210.9 | rms=129 | updated_at=1777903114.7647104
- [2026-05-04 21:58:37] operator / voice_transcript_partial / voice: fifth to eighth to fifty to fifty to fifty to fifty
  meta: kind=partial | timestamp=1777903117.7514849 | source=windows | frequency_hz=210.9 | rms=129 | updated_at=1777903114.7647104
- [2026-05-04 21:58:37] operator / voice_transcript_partial / voice: fifth to eighth to fifth to sixth to eighth
  meta: kind=partial | timestamp=1777903117.9629142 | source=windows | frequency_hz=210.9 | rms=129 | updated_at=1777903114.7647104
- [2026-05-04 21:58:38] operator / voice_transcript_partial / voice: fifth to eighth to fifth to sixth to eighth to
  meta: kind=partial | timestamp=1777903118.7739265 | source=windows | frequency_hz=210.9 | rms=129 | updated_at=1777903114.7647104
- [2026-05-04 21:58:39] operator / voice_transcript_partial / voice: fifth to eighth to fifth to sixth to eighth to fifteenth
  meta: kind=partial | timestamp=1777903119.3916936 | source=windows | frequency_hz=210.9 | rms=129 | updated_at=1777903114.7647104
- [2026-05-04 21:58:39] operator / voice_transcript_partial / voice: fifth to eighth to fifth to sixth to eighth to fifteenth to
  meta: kind=partial | timestamp=1777903119.6079984 | source=windows | frequency_hz=210.9 | rms=129 | updated_at=1777903114.7647104
- [2026-05-04 21:58:39] operator / voice_transcript_partial / voice: fifth to eighth to fifth to sixth to eighth to fifth
  meta: kind=partial | timestamp=1777903119.8108995 | source=windows | frequency_hz=210.9 | rms=129 | updated_at=1777903114.7647104
- [2026-05-04 21:58:40] operator / voice_transcript_partial / voice: fifth to eighth to fifth to sixth to eighth to fifteenth to keep
  meta: kind=partial | timestamp=1777903120.2259555 | source=windows | frequency_hz=210.9 | rms=129 | updated_at=1777903114.7647104
- [2026-05-04 21:58:41] operator / voice_transcript_final / voice: fifth to eighth to fifth to sixth to eighth to 15th to keep
  meta: kind=final | timestamp=1777903121.8889956 | source=final | confidence=0.34 | frequency_hz=410.2 | rms=122 | updated_at=1777903120.9051573
- [2026-05-04 21:58:41] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777903121.8980193 | source=windows | frequency_hz=410.2 | rms=122 | updated_at=1777903120.9051573
- [2026-05-04 21:58:42] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903122.2863219 | source=windows | frequency_hz=410.2 | rms=122 | updated_at=1777903120.9051573
- [2026-05-04 21:58:42] operator / voice_transcript_partial / voice: to fifty
  meta: kind=partial | timestamp=1777903122.6942897 | source=windows | frequency_hz=410.2 | rms=122 | updated_at=1777903120.9051573
- [2026-05-04 21:58:43] operator / voice_transcript_partial / voice: to fifth
  meta: kind=partial | timestamp=1777903123.514872 | source=windows | frequency_hz=410.2 | rms=122 | updated_at=1777903120.9051573
- [2026-05-04 21:58:44] operator / voice_transcript_partial / voice: to fifth to
  meta: kind=partial | timestamp=1777903124.6348553 | source=windows | frequency_hz=410.2 | rms=122 | updated_at=1777903120.9051573
- [2026-05-04 21:58:44] operator / voice_transcript_partial / voice: to fifth
  meta: kind=partial | timestamp=1777903124.8415582 | source=windows | frequency_hz=410.2 | rms=122 | updated_at=1777903120.9051573
- [2026-05-04 21:58:45] operator / voice_transcript_partial / voice: to fifth to
  meta: kind=partial | timestamp=1777903125.0393581 | source=windows | frequency_hz=410.2 | rms=122 | updated_at=1777903120.9051573
- [2026-05-04 21:58:45] operator / voice_transcript_partial / voice: to fifth to eighth to fifty
  meta: kind=partial | timestamp=1777903125.244949 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:45] operator / voice_transcript_partial / voice: to fifth to eighth to fifty to
  meta: kind=partial | timestamp=1777903125.8592703 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:46] operator / voice_transcript_partial / voice: to fifth to eighth
  meta: kind=partial | timestamp=1777903126.059824 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:46] operator / voice_transcript_partial / voice: to fifth to eighth to
  meta: kind=partial | timestamp=1777903126.7605784 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:47] operator / voice_transcript_partial / voice: to fifth to eighth
  meta: kind=partial | timestamp=1777903127.009266 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:49] operator / voice_transcript_partial / voice: to fifth to eighth to
  meta: kind=partial | timestamp=1777903129.3324678 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:49] operator / voice_transcript_partial / voice: to fifth to eighth to ten
  meta: kind=partial | timestamp=1777903129.7540915 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:49] operator / voice_transcript_partial / voice: to fifth to eighth to fifty
  meta: kind=partial | timestamp=1777903129.9704978 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:50] operator / voice_transcript_partial / voice: to fifth to eighth up to keep
  meta: kind=partial | timestamp=1777903130.5962288 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:51] operator / voice_transcript_partial / voice: to fifth to eighth up to up to
  meta: kind=partial | timestamp=1777903131.3243523 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:51] operator / voice_transcript_partial / voice: to fifth to eighth up to up to fifth
  meta: kind=partial | timestamp=1777903131.7392616 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:52] operator / voice_transcript_partial / voice: to fifth to eighth up to up to fifth to the
  meta: kind=partial | timestamp=1777903132.3744144 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:52] operator / voice_transcript_partial / voice: to fifth to eighth up to up to fifth to keep
  meta: kind=partial | timestamp=1777903132.3759718 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:53] operator / voice_transcript_partial / voice: to fifth to eighth up to up to fifth to sixth
  meta: kind=partial | timestamp=1777903133.062099 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:53] operator / voice_transcript_partial / voice: to fifth to eighth up to up to fifth to sixth to
  meta: kind=partial | timestamp=1777903133.476879 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:54] operator / voice_transcript_final / voice: to fifth to eighth up to up to fifth to sixth to
  meta: kind=final | timestamp=1777903134.3037195 | source=final | confidence=0.32 | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:55] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777903135.344935 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:55] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903135.344935 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:55] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777903135.578232 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:56] operator / voice_transcript_final / voice: keep
  meta: kind=final | timestamp=1777903136.2392745 | source=final | confidence=0.08 | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:57] operator / voice_transcript_partial / voice: up
  meta: kind=partial | timestamp=1777903137.9541283 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:58] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777903138.971123 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:59] operator / voice_transcript_partial / voice: up
  meta: kind=partial | timestamp=1777903139.1709201 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:59] operator / voice_transcript_partial / voice: up to
  meta: kind=partial | timestamp=1777903139.3753624 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:59] operator / voice_transcript_partial / voice: up
  meta: kind=partial | timestamp=1777903139.6147223 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:58:59] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777903139.8261752 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:00] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777903140.858464 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:01] operator / voice_transcript_partial / voice: fifth to keep
  meta: kind=partial | timestamp=1777903141.465559 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:03] operator / voice_transcript_partial / voice: fifth to sixth
  meta: kind=partial | timestamp=1777903143.1032712 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:03] operator / voice_transcript_partial / voice: fifth to keep up
  meta: kind=partial | timestamp=1777903143.7594814 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:04] operator / voice_transcript_partial / voice: fifth to keep fifth
  meta: kind=partial | timestamp=1777903144.1602054 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:04] operator / voice_transcript_partial / voice: fifth to keep fifth to
  meta: kind=partial | timestamp=1777903144.9728408 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:05] operator / voice_transcript_partial / voice: fifth to keep fifth up
  meta: kind=partial | timestamp=1777903145.1763303 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:05] operator / voice_transcript_partial / voice: fifth to keep fifth up to
  meta: kind=partial | timestamp=1777903145.3795087 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:05] operator / voice_transcript_partial / voice: fifth to keep fifth up to a
  meta: kind=partial | timestamp=1777903145.9896638 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:06] operator / voice_transcript_partial / voice: fifth to keep fifth to eighth to
  meta: kind=partial | timestamp=1777903146.2049236 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:06] operator / voice_transcript_partial / voice: fifth to keep fifth to eighth to fifty
  meta: kind=partial | timestamp=1777903146.407617 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:06] operator / voice_transcript_partial / voice: fifth to keep fifth to eighth to tenth
  meta: kind=partial | timestamp=1777903146.8264923 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:07] operator / voice_transcript_partial / voice: fifth to keep fifth to eighth to tenth to
  meta: kind=partial | timestamp=1777903147.0290768 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:07] operator / voice_transcript_partial / voice: fifth to keep fifth to sixth to eighth
  meta: kind=partial | timestamp=1777903147.2642167 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:07] operator / voice_transcript_partial / voice: fifth to keep fifth to sixth to eighth to
  meta: kind=partial | timestamp=1777903147.477407 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:07] operator / voice_transcript_partial / voice: fifth to keep fifth to sixth to eighth to fifty
  meta: kind=partial | timestamp=1777903147.6837885 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:07] operator / voice_transcript_partial / voice: fifth to keep fifth up to fifth to eighth
  meta: kind=partial | timestamp=1777903147.8897433 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:08] operator / voice_transcript_partial / voice: fifth to keep fifth up to fifth to eighth to
  meta: kind=partial | timestamp=1777903148.2896895 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:08] operator / voice_transcript_partial / voice: fifth to keep fifth up to fifth to eighth to keep
  meta: kind=partial | timestamp=1777903148.4946213 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:08] operator / voice_transcript_partial / voice: fifth to keep fifth to sixth to eighth to fifty to fifty
  meta: kind=partial | timestamp=1777903148.6947298 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:08] operator / voice_transcript_partial / voice: fifth to keep fifth up to fifth to sixth to eighth
  meta: kind=partial | timestamp=1777903148.9411573 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:09] operator / voice_transcript_final / voice: fifth to keep fifth up to fifth to sixth to eighth
  meta: kind=final | timestamp=1777903149.557146 | source=final | confidence=0.32 | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:10] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903150.1647573 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:11] operator / voice_transcript_partial / voice: to tenth to
  meta: kind=partial | timestamp=1777903151.3847582 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:11] operator / voice_transcript_partial / voice: to fifty
  meta: kind=partial | timestamp=1777903151.6026795 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:12] operator / voice_transcript_partial / voice: to ten to fifteen
  meta: kind=partial | timestamp=1777903152.0057826 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:12] operator / voice_transcript_partial / voice: to ten fifth
  meta: kind=partial | timestamp=1777903152.20657 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:13] operator / voice_transcript_final / voice: to 10 5th
  meta: kind=final | timestamp=1777903153.0356526 | source=final | confidence=0.57 | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:14] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903154.2545688 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:14] operator / voice_transcript_partial / voice: up
  meta: kind=partial | timestamp=1777903154.6642573 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:14] operator / voice_transcript_partial / voice: to eighth
  meta: kind=partial | timestamp=1777903154.8686662 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:15] operator / voice_transcript_partial / voice: to eighth to
  meta: kind=partial | timestamp=1777903155.680158 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:15] operator / voice_transcript_partial / voice: to eighth
  meta: kind=partial | timestamp=1777903155.918975 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:16] operator / voice_transcript_final / voice: to eighth
  meta: kind=final | timestamp=1777903156.3343823 | source=final | confidence=0.14 | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:17] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903157.0014882 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:17] operator / voice_transcript_partial / voice: to fifty
  meta: kind=partial | timestamp=1777903157.4075427 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:18] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777903158.431228 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:19] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777903159.6853378 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:19] operator / voice_transcript_partial / voice: fifth to keep
  meta: kind=partial | timestamp=1777903159.8879552 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:20] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777903160.515252 | source=windows | frequency_hz=402.3 | rms=293 | updated_at=1777903125.1282666
- [2026-05-04 21:59:21] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777903161.3296764 | source=windows | frequency_hz=152.3 | rms=183 | updated_at=1777903161.225481
- [2026-05-04 21:59:21] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777903161.7469084 | source=windows | frequency_hz=152.3 | rms=183 | updated_at=1777903161.225481
- [2026-05-04 21:59:21] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777903161.9679987 | source=windows | frequency_hz=152.3 | rms=183 | updated_at=1777903161.225481
- [2026-05-04 21:59:22] operator / voice_transcript_partial / voice: fifth to eighth
  meta: kind=partial | timestamp=1777903162.3948457 | source=windows | frequency_hz=152.3 | rms=183 | updated_at=1777903161.225481
- [2026-05-04 21:59:23] operator / voice_transcript_final / voice: fifth to eighth
  meta: kind=final | timestamp=1777903163.0241666 | source=final | confidence=0.24 | frequency_hz=152.3 | rms=183 | updated_at=1777903161.225481
- [2026-05-04 21:59:23] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903163.844886 | source=windows | frequency_hz=152.3 | rms=183 | updated_at=1777903161.225481
- [2026-05-04 21:59:24] operator / voice_transcript_partial / voice: to ten
  meta: kind=partial | timestamp=1777903164.4830062 | source=windows | frequency_hz=152.3 | rms=183 | updated_at=1777903161.225481
- [2026-05-04 21:59:24] operator / voice_transcript_partial / voice: to fifty
  meta: kind=partial | timestamp=1777903164.6900768 | source=windows | frequency_hz=152.3 | rms=183 | updated_at=1777903161.225481
- [2026-05-04 21:59:24] operator / voice_transcript_partial / voice: to keep
  meta: kind=partial | timestamp=1777903164.9025898 | source=windows | frequency_hz=152.3 | rms=183 | updated_at=1777903161.225481
- [2026-05-04 21:59:25] operator / voice_transcript_partial / voice: to keep the
  meta: kind=partial | timestamp=1777903165.134239 | source=windows | frequency_hz=152.3 | rms=183 | updated_at=1777903161.225481
- [2026-05-04 21:59:25] operator / voice_transcript_partial / voice: to keep up
  meta: kind=partial | timestamp=1777903165.541261 | source=windows | frequency_hz=152.3 | rms=183 | updated_at=1777903161.225481
- [2026-05-04 21:59:26] operator / voice_transcript_partial / voice: to keep up to
  meta: kind=partial | timestamp=1777903166.9560778 | source=windows | frequency_hz=152.3 | rms=183 | updated_at=1777903161.225481
- [2026-05-04 21:59:27] operator / voice_transcript_partial / voice: to fifty eighth
  meta: kind=partial | timestamp=1777903167.363609 | source=windows | frequency_hz=152.3 | rms=183 | updated_at=1777903161.225481
- [2026-05-04 21:59:27] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 21:59:27] operator / voice_transcript_partial / voice: to fifty eighth to
  meta: kind=partial | timestamp=1777903167.9902136 | source=windows | frequency_hz=152.3 | rms=183 | updated_at=1777903161.225481
- [2026-05-04 21:59:28] operator / voice_transcript_partial / voice: to fifty eighth to fifty
  meta: kind=partial | timestamp=1777903168.4486158 | source=windows | frequency_hz=152.3 | rms=183 | updated_at=1777903161.225481
- [2026-05-04 21:59:28] operator / voice_transcript_partial / voice: to fifty eighth to fifty to
  meta: kind=partial | timestamp=1777903168.653029 | source=windows | frequency_hz=152.3 | rms=183 | updated_at=1777903161.225481
- [2026-05-04 21:59:28] operator / voice_transcript_partial / voice: to keep up fifth to eighth to
  meta: kind=partial | timestamp=1777903168.8873014 | source=windows | frequency_hz=152.3 | rms=183 | updated_at=1777903161.225481
- [2026-05-04 21:59:29] operator / voice_transcript_partial / voice: to fifty eighth to fifty to fifty
  meta: kind=partial | timestamp=1777903169.1197844 | source=windows | frequency_hz=152.3 | rms=183 | updated_at=1777903161.225481
- [2026-05-04 21:59:29] operator / voice_transcript_partial / voice: to fifty eighth to fifty fifth
  meta: kind=partial | timestamp=1777903169.325791 | source=windows | frequency_hz=355.5 | rms=216 | updated_at=1777903169.169469
- [2026-05-04 21:59:29] operator / voice_transcript_partial / voice: to fifty eighth to fifty fifth to the
  meta: kind=partial | timestamp=1777903169.982458 | source=windows | frequency_hz=355.5 | rms=216 | updated_at=1777903169.169469
- [2026-05-04 21:59:30] operator / voice_transcript_partial / voice: to fifty eighth to fifty fifth
  meta: kind=partial | timestamp=1777903170.187222 | source=windows | frequency_hz=355.5 | rms=216 | updated_at=1777903169.169469
- [2026-05-04 21:59:30] operator / voice_transcript_partial / voice: to fifty eighth to fifty fifth to
  meta: kind=partial | timestamp=1777903170.605621 | source=windows | frequency_hz=355.5 | rms=216 | updated_at=1777903169.169469
- [2026-05-04 21:59:30] operator / voice_transcript_partial / voice: to fifty eighth to fifty fifth to eighth
  meta: kind=partial | timestamp=1777903170.8060703 | source=windows | frequency_hz=355.5 | rms=216 | updated_at=1777903169.169469
- [2026-05-04 21:59:32] operator / voice_transcript_partial / voice: to fifty eighth to fifty fifth up to
  meta: kind=partial | timestamp=1777903172.2233968 | source=windows | frequency_hz=355.5 | rms=216 | updated_at=1777903169.169469
- [2026-05-04 21:59:32] operator / voice_transcript_partial / voice: to fifty eighth to fifty fifth to eighth
  meta: kind=partial | timestamp=1777903172.4427288 | source=windows | frequency_hz=355.5 | rms=216 | updated_at=1777903169.169469
- [2026-05-04 21:59:32] operator / voice_transcript_partial / voice: to fifty eighth to fifty fifth to eighth to
  meta: kind=partial | timestamp=1777903172.6432889 | source=windows | frequency_hz=355.5 | rms=216 | updated_at=1777903169.169469
- [2026-05-04 21:59:32] operator / voice_transcript_partial / voice: to fifty eighth to fifty fifth to eighth
  meta: kind=partial | timestamp=1777903172.8514874 | source=windows | frequency_hz=355.5 | rms=216 | updated_at=1777903169.169469
- [2026-05-04 21:59:34] operator / voice_transcript_partial / voice: to fifty eighth to fifty fifth to eighth to
  meta: kind=partial | timestamp=1777903174.5724866 | source=windows | frequency_hz=355.5 | rms=216 | updated_at=1777903169.169469
- [2026-05-04 21:59:34] operator / voice_transcript_partial / voice: to fifty eighth to fifty fifth to eighth
  meta: kind=partial | timestamp=1777903174.573249 | source=windows | frequency_hz=355.5 | rms=216 | updated_at=1777903169.169469
- [2026-05-04 21:59:35] operator / voice_transcript_final / voice: to 58th to 55th to eighth
  meta: kind=final | timestamp=1777903175.8530765 | source=final | confidence=0.17 | frequency_hz=355.5 | rms=216 | updated_at=1777903169.169469
- [2026-05-04 21:59:36] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903176.4664068 | source=windows | frequency_hz=363.3 | rms=204 | updated_at=1777903176.3273861
- [2026-05-04 21:59:37] operator / voice_transcript_final / voice: to
  meta: kind=final | timestamp=1777903177.0709813 | source=final | confidence=0.86 | frequency_hz=363.3 | rms=204 | updated_at=1777903176.3273861
- [2026-05-04 21:59:37] operator / voice_transcript_partial / voice: see
  meta: kind=partial | timestamp=1777903177.6763105 | source=windows | frequency_hz=363.3 | rms=204 | updated_at=1777903176.3273861
- [2026-05-04 21:59:40] operator / voice_transcript_partial / voice: its
  meta: kind=partial | timestamp=1777903180.3545504 | source=windows | frequency_hz=363.3 | rms=204 | updated_at=1777903176.3273861
- [2026-05-04 21:59:40] operator / voice_transcript_final / voice: its
  meta: kind=final | timestamp=1777903180.763394 | source=final | confidence=0.37 | frequency_hz=363.3 | rms=204 | updated_at=1777903176.3273861
- [2026-05-04 21:59:42] operator / voice_transcript_partial / voice: own
  meta: kind=partial | timestamp=1777903182.1916304 | source=windows | frequency_hz=363.3 | rms=204 | updated_at=1777903176.3273861
- [2026-05-04 21:59:42] operator / voice_transcript_partial / voice: way
  meta: kind=partial | timestamp=1777903182.394119 | source=windows | frequency_hz=363.3 | rms=204 | updated_at=1777903176.3273861
- [2026-05-04 21:59:42] operator / voice_transcript_partial / voice: way into
  meta: kind=partial | timestamp=1777903182.6000395 | source=windows | frequency_hz=363.3 | rms=204 | updated_at=1777903176.3273861
- [2026-05-04 21:59:42] operator / voice_transcript_partial / voice: way into the
  meta: kind=partial | timestamp=1777903182.8139641 | source=windows | frequency_hz=363.3 | rms=204 | updated_at=1777903176.3273861
- [2026-05-04 21:59:45] operator / voice_transcript_final / voice: way into the
  meta: kind=final | timestamp=1777903185.4016511 | source=final | confidence=0.17 | frequency_hz=363.3 | rms=204 | updated_at=1777903176.3273861
- [2026-05-04 21:59:49] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777903189.689466 | source=windows | frequency_hz=363.3 | rms=204 | updated_at=1777903176.3273861
- [2026-05-04 21:59:50] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777903190.3396888 | source=windows | frequency_hz=222.7 | rms=222 | updated_at=1777903190.0261166
- [2026-05-04 21:59:50] operator / voice_transcript_partial / voice: fifth to to
  meta: kind=partial | timestamp=1777903190.7617476 | source=windows | frequency_hz=211.7 | rms=151 | updated_at=1777903190.6665118
- [2026-05-04 21:59:50] operator / voice_transcript_partial / voice: fifth to to the
  meta: kind=partial | timestamp=1777903190.9627461 | source=windows | frequency_hz=211.7 | rms=151 | updated_at=1777903190.6665118
- [2026-05-04 21:59:51] operator / voice_transcript_final / voice: fifth to to the
  meta: kind=final | timestamp=1777903191.583084 | source=final | confidence=0.62 | frequency_hz=211.7 | rms=151 | updated_at=1777903190.6665118
- [2026-05-04 21:59:55] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903195.912803 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 21:59:57] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777903197.1619787 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 21:59:57] operator / voice_transcript_final / voice: fifth
  meta: kind=final | timestamp=1777903197.7814665 | source=final | confidence=0.72 | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 21:59:57] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903197.9795866 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 21:59:58] operator / voice_transcript_partial / voice: to keep
  meta: kind=partial | timestamp=1777903198.394222 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 21:59:58] operator / voice_transcript_partial / voice: to eighth
  meta: kind=partial | timestamp=1777903198.7948463 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 21:59:59] operator / voice_transcript_final / voice: to eighth
  meta: kind=final | timestamp=1777903199.8267994 | source=final | confidence=0.41 | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 21:59:59] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903199.8327937 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:00] operator / voice_transcript_partial / voice: to fifty
  meta: kind=partial | timestamp=1777903200.503727 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:00] operator / voice_transcript_partial / voice: to keep
  meta: kind=partial | timestamp=1777903200.7131495 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:00] operator / voice_transcript_partial / voice: to fifth
  meta: kind=partial | timestamp=1777903200.9276664 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:01] operator / voice_transcript_partial / voice: to fifth to
  meta: kind=partial | timestamp=1777903201.334551 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:01] operator / voice_transcript_partial / voice: to fifth to eighth
  meta: kind=partial | timestamp=1777903201.9465928 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:02] operator / voice_transcript_final / voice: to fifth to eighth
  meta: kind=final | timestamp=1777903202.568025 | source=final | confidence=0.59 | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:04] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903204.8921854 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:05] operator / voice_transcript_partial / voice: up
  meta: kind=partial | timestamp=1777903205.3276038 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:06] operator / voice_transcript_partial / voice: up to
  meta: kind=partial | timestamp=1777903206.3574388 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:06] operator / voice_transcript_partial / voice: up
  meta: kind=partial | timestamp=1777903206.7609909 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:07] operator / voice_transcript_final / voice: up
  meta: kind=final | timestamp=1777903207.569937 | source=final | confidence=0.3 | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:11] operator / voice_transcript_partial / voice: and up
  meta: kind=partial | timestamp=1777903211.1469069 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:11] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777903211.7652621 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:11] operator / voice_transcript_partial / voice: and up
  meta: kind=partial | timestamp=1777903211.9678128 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:12] operator / voice_transcript_partial / voice: and up to
  meta: kind=partial | timestamp=1777903212.8223948 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:13] operator / voice_transcript_partial / voice: and up to fifty
  meta: kind=partial | timestamp=1777903213.227802 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:13] operator / voice_transcript_final / voice: and up to 50
  meta: kind=final | timestamp=1777903213.668222 | source=final | confidence=0.34 | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:15] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903215.0889938 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:15] operator / voice_transcript_partial / voice: two to
  meta: kind=partial | timestamp=1777903215.6942773 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:15] operator / voice_transcript_partial / voice: to fifty to
  meta: kind=partial | timestamp=1777903215.9005373 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:16] operator / voice_transcript_partial / voice: to to to to
  meta: kind=partial | timestamp=1777903216.549848 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:16] operator / voice_transcript_partial / voice: to fifty to fifty
  meta: kind=partial | timestamp=1777903216.7749512 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:17] operator / voice_transcript_partial / voice: to fifty to fifty to
  meta: kind=partial | timestamp=1777903217.2032368 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:17] operator / voice_transcript_partial / voice: to to to to to to to
  meta: kind=partial | timestamp=1777903217.828188 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:18] operator / voice_transcript_final / voice: to to to to to to to
  meta: kind=final | timestamp=1777903218.4400399 | source=final | confidence=0.79 | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:18] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903218.844249 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:19] operator / voice_transcript_partial / voice: to to
  meta: kind=partial | timestamp=1777903219.051481 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:19] operator / voice_transcript_partial / voice: to fifty
  meta: kind=partial | timestamp=1777903219.6692429 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:20] operator / voice_transcript_partial / voice: to fifth to
  meta: kind=partial | timestamp=1777903220.0759208 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:20] operator / voice_transcript_partial / voice: keep up
  meta: kind=partial | timestamp=1777903220.2765775 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:20] operator / voice_transcript_partial / voice: to fifth to eighth
  meta: kind=partial | timestamp=1777903220.6843755 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:21] operator / voice_transcript_partial / voice: to fifth to eighth up
  meta: kind=partial | timestamp=1777903221.9326696 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:22] operator / voice_transcript_final / voice: to fifth to eighth up
  meta: kind=final | timestamp=1777903222.1367815 | source=final | confidence=0.57 | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:22] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903222.552921 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:22] operator / voice_transcript_partial / voice: if
  meta: kind=partial | timestamp=1777903222.9604075 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:23] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777903223.1630957 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:23] operator / voice_transcript_final / voice: 50
  meta: kind=final | timestamp=1777903223.9748092 | source=final | confidence=0.7 | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:24] operator / voice_transcript_partial / voice: two
  meta: kind=partial | timestamp=1777903224.1809187 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:24] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903224.1809187 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:24] operator / voice_transcript_final / voice: to
  meta: kind=final | timestamp=1777903224.7988305 | source=final | confidence=0.85 | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:25] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777903225.4310255 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:26] operator / voice_transcript_partial / voice: fifty to
  meta: kind=partial | timestamp=1777903226.4969609 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:27] operator / voice_transcript_partial / voice: fifty to fifty
  meta: kind=partial | timestamp=1777903227.1187665 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:27] operator / voice_transcript_partial / voice: fifty fifth
  meta: kind=partial | timestamp=1777903227.3264575 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:28] operator / voice_transcript_final / voice: 55th
  meta: kind=final | timestamp=1777903228.4183545 | source=final | confidence=0.31 | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:28] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903228.8142145 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:29] operator / voice_transcript_partial / voice: to eighth
  meta: kind=partial | timestamp=1777903229.0183504 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:29] operator / voice_transcript_partial / voice: to eighth to
  meta: kind=partial | timestamp=1777903229.8466218 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:30] operator / voice_transcript_partial / voice: to eighth to keep
  meta: kind=partial | timestamp=1777903230.0605602 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:30] operator / voice_transcript_final / voice: to eighth to keep
  meta: kind=final | timestamp=1777903230.4754887 | source=final | confidence=0.55 | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:31] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777903231.5187757 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:31] operator / voice_transcript_partial / voice: the fifth
  meta: kind=partial | timestamp=1777903231.721208 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:32] operator / voice_transcript_final / voice: the fifth
  meta: kind=final | timestamp=1777903232.547464 | source=final | confidence=0.61 | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:33] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903233.5781102 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:34] operator / voice_transcript_final / voice: to
  meta: kind=final | timestamp=1777903234.278317 | source=final | confidence=0.8 | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:37] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777903237.5412846 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:38] operator / voice_transcript_partial / voice: eighth to
  meta: kind=partial | timestamp=1777903238.1514952 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:38] operator / voice_transcript_partial / voice: fifty to fifty
  meta: kind=partial | timestamp=1777903238.3540456 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:38] operator / voice_transcript_partial / voice: fifty to fifty to
  meta: kind=partial | timestamp=1777903238.976135 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:39] operator / voice_transcript_final / voice: 50 to 50 to
  meta: kind=final | timestamp=1777903239.7858224 | source=final | confidence=0.45 | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:00:40] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777903240.6112192 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:16] operator / voice_transcript_partial / voice: two
  meta: kind=partial | timestamp=1777903276.0894325 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:16] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777903276.4973238 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:17] operator / voice_transcript_partial / voice: fifty to fifty
  meta: kind=partial | timestamp=1777903277.3159811 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:19] operator / voice_transcript_partial / voice: fifty to fifty to fifty
  meta: kind=partial | timestamp=1777903279.3498013 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:19] operator / voice_transcript_partial / voice: fifty fifth to keep
  meta: kind=partial | timestamp=1777903279.551142 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:20] operator / voice_transcript_final / voice: 55th to keep
  meta: kind=final | timestamp=1777903280.365786 | source=final | confidence=0.39 | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:20] operator / voice_transcript_partial / voice: up
  meta: kind=partial | timestamp=1777903280.9810634 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:21] operator / voice_transcript_partial / voice: safe
  meta: kind=partial | timestamp=1777903281.185985 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:21] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777903281.5904622 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:21] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777903281.797332 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:22] operator / voice_transcript_partial / voice: fifth to eighth
  meta: kind=partial | timestamp=1777903282.2004492 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:22] operator / voice_transcript_partial / voice: fifth to keep
  meta: kind=partial | timestamp=1777903282.6048717 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:23] operator / voice_transcript_partial / voice: fifth to eighth
  meta: kind=partial | timestamp=1777903283.0114124 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:23] operator / voice_transcript_partial / voice: fifth to keep
  meta: kind=partial | timestamp=1777903283.2120986 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:25] operator / voice_transcript_partial / voice: fifth up to
  meta: kind=partial | timestamp=1777903285.265391 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:26] operator / voice_transcript_partial / voice: fifth up to keep
  meta: kind=partial | timestamp=1777903286.0738125 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:26] operator / voice_transcript_partial / voice: fifth up to fifth
  meta: kind=partial | timestamp=1777903286.28222 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:27] operator / voice_transcript_partial / voice: fifth up to fifth to
  meta: kind=partial | timestamp=1777903287.2949262 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:27] operator / voice_transcript_partial / voice: fifth up to fifth to a
  meta: kind=partial | timestamp=1777903287.5251734 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:27] operator / voice_transcript_partial / voice: fifth up to fifth to ten
  meta: kind=partial | timestamp=1777903287.7302558 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:27] operator / voice_transcript_partial / voice: fifth up to fifth to ten to
  meta: kind=partial | timestamp=1777903287.9334557 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:28] operator / voice_transcript_partial / voice: fifth up to fifth to ten fifty
  meta: kind=partial | timestamp=1777903288.3455172 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:28] operator / voice_transcript_partial / voice: fifth up to fifth to ten fifth
  meta: kind=partial | timestamp=1777903288.7492616 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:29] operator / voice_transcript_final / voice: fifth up to fifth to 10 5th
  meta: kind=final | timestamp=1777903289.3595653 | source=final | confidence=0.47 | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:29] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903289.964924 | source=windows | frequency_hz=312.5 | rms=272 | updated_at=1777903192.846251
- [2026-05-04 22:01:30] operator / voice_transcript_partial / voice: up
  meta: kind=partial | timestamp=1777903290.1685712 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:30] operator / voice_transcript_partial / voice: up to
  meta: kind=partial | timestamp=1777903290.7768576 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:30] operator / voice_transcript_partial / voice: up to fifty
  meta: kind=partial | timestamp=1777903290.9782853 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:31] operator / voice_transcript_partial / voice: up to fifth
  meta: kind=partial | timestamp=1777903291.6003492 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:32] operator / voice_transcript_partial / voice: up to fifth to
  meta: kind=partial | timestamp=1777903292.6157382 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:33] operator / voice_transcript_partial / voice: up to fifth to keep
  meta: kind=partial | timestamp=1777903293.0226438 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:33] operator / voice_transcript_partial / voice: up to fifth to eighth
  meta: kind=partial | timestamp=1777903293.6269803 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:33] operator / voice_transcript_partial / voice: up to fifth to eighth to
  meta: kind=partial | timestamp=1777903293.8318956 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:34] operator / voice_transcript_final / voice: up to fifth to eighth to
  meta: kind=final | timestamp=1777903294.2380178 | source=final | confidence=0.48 | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:38] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777903298.915827 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:40] operator / voice_transcript_partial / voice: keep up to
  meta: kind=partial | timestamp=1777903300.541459 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:40] operator / voice_transcript_partial / voice: keep fifth
  meta: kind=partial | timestamp=1777903300.747608 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:41] operator / voice_transcript_partial / voice: keep up
  meta: kind=partial | timestamp=1777903301.350201 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:41] operator / voice_transcript_partial / voice: keep up to fifth
  meta: kind=partial | timestamp=1777903301.554072 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:41] operator / voice_transcript_partial / voice: keep up to fifth to
  meta: kind=partial | timestamp=1777903301.965417 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:42] operator / voice_transcript_final / voice: keep up to fifth to
  meta: kind=final | timestamp=1777903302.5744908 | source=final | confidence=0.55 | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:42] operator / voice_transcript_partial / voice: tie
  meta: kind=partial | timestamp=1777903302.7740648 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:42] operator / voice_transcript_partial / voice: ten
  meta: kind=partial | timestamp=1777903302.9781027 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:43] operator / voice_transcript_final / voice: 10
  meta: kind=final | timestamp=1777903303.3879375 | source=final | confidence=0.58 | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:43] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903303.7916791 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:43] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777903303.7916791 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:45] operator / voice_transcript_final / voice: in
  meta: kind=final | timestamp=1777903305.0525477 | source=final | confidence=0.65 | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:45] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903305.0535536 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:45] operator / voice_transcript_final / voice: to
  meta: kind=final | timestamp=1777903305.858604 | source=final | confidence=0.57 | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:48] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777903308.8953342 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:49] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777903309.0996284 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:49] operator / voice_transcript_partial / voice: happen
  meta: kind=partial | timestamp=1777903309.304543 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:49] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777903309.7065897 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:50] operator / voice_transcript_partial / voice: a man with
  meta: kind=partial | timestamp=1777903310.111636 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:50] operator / voice_transcript_partial / voice: one of my
  meta: kind=partial | timestamp=1777903310.314418 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:50] operator / voice_transcript_partial / voice: one lead
  meta: kind=partial | timestamp=1777903310.734606 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:50] operator / voice_transcript_partial / voice: one lead the
  meta: kind=partial | timestamp=1777903310.936536 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:51] operator / voice_transcript_partial / voice: cnn mobile and one
  meta: kind=partial | timestamp=1777903311.1418378 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:51] operator / voice_transcript_partial / voice: one lead someone who
  meta: kind=partial | timestamp=1777903311.3467786 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:51] operator / voice_transcript_partial / voice: one lead not only
  meta: kind=partial | timestamp=1777903311.551134 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:51] operator / voice_transcript_partial / voice: one lead not only in the
  meta: kind=partial | timestamp=1777903311.9599404 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:52] operator / voice_transcript_partial / voice: one lead to one late
  meta: kind=partial | timestamp=1777903312.160141 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:52] operator / voice_transcript_partial / voice: one lead to one one eight zero
  meta: kind=partial | timestamp=1777903312.36083 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:52] operator / voice_transcript_partial / voice: one lead not only has one
  meta: kind=partial | timestamp=1777903312.564497 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:53] operator / voice_transcript_partial / voice: one lead to one one eight one eight
  meta: kind=partial | timestamp=1777903313.1930163 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:53] operator / voice_transcript_final / voice: one lead to 11818
  meta: kind=final | timestamp=1777903313.9991841 | source=final | confidence=0.09 | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:54] operator / voice_transcript_partial / voice: nine
  meta: kind=partial | timestamp=1777903314.6353471 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:55] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777903315.0403993 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:55] operator / voice_transcript_partial / voice: and we'll
  meta: kind=partial | timestamp=1777903315.2411585 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:55] operator / voice_transcript_partial / voice: and we'll be
  meta: kind=partial | timestamp=1777903315.4454892 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:55] operator / voice_transcript_partial / voice: and we'll be a
  meta: kind=partial | timestamp=1777903315.6474354 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:56] operator / voice_transcript_final / voice: and we ll be a
  meta: kind=final | timestamp=1777903316.261959 | source=final | confidence=0.18 | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:56] operator / voice_transcript_partial / voice: pause
  meta: kind=partial | timestamp=1777903316.8684754 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:57] operator / voice_transcript_partial / voice: sixth
  meta: kind=partial | timestamp=1777903317.0728636 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:57] operator / voice_transcript_partial / voice: seat on the
  meta: kind=partial | timestamp=1777903317.4863677 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:01:58] operator / voice_transcript_final / voice: seat on the
  meta: kind=final | timestamp=1777903318.3300955 | source=final | confidence=0.07 | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:02:01] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777903321.799145 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:02:01] operator / voice_transcript_partial / voice: tv
  meta: kind=partial | timestamp=1777903321.799145 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:02:02] operator / voice_transcript_partial / voice: radar
  meta: kind=partial | timestamp=1777903322.0164087 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:02:02] operator / voice_transcript_partial / voice: inherent
  meta: kind=partial | timestamp=1777903322.4353886 | source=windows | frequency_hz=316.4 | rms=161 | updated_at=1777903289.99828
- [2026-05-04 22:02:02] operator / voice_transcript_partial / voice: tv and movie
  meta: kind=partial | timestamp=1777903322.641641 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:02] operator / voice_transcript_partial / voice: tv and believes in
  meta: kind=partial | timestamp=1777903322.8573089 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:03] operator / voice_transcript_partial / voice: inevitable digital
  meta: kind=partial | timestamp=1777903323.0616698 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:03] operator / voice_transcript_partial / voice: tv and believes in la
  meta: kind=partial | timestamp=1777903323.265687 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:03] operator / voice_transcript_partial / voice: inevitable that some of
  meta: kind=partial | timestamp=1777903323.6889427 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:03] operator / voice_transcript_partial / voice: inevitable that some of the
  meta: kind=partial | timestamp=1777903323.8923583 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:04] operator / voice_transcript_partial / voice: inevitable that some of the al
  meta: kind=partial | timestamp=1777903324.1030753 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:04] operator / voice_transcript_partial / voice: inevitable that some of the young
  meta: kind=partial | timestamp=1777903324.3101537 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:04] operator / voice_transcript_partial / voice: inevitable that some of the younger
  meta: kind=partial | timestamp=1777903324.5122998 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:04] operator / voice_transcript_partial / voice: inevitable that some of the unknowns
  meta: kind=partial | timestamp=1777903324.7143178 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:05] operator / voice_transcript_partial / voice: inevitable that some of the unknowns in a
  meta: kind=partial | timestamp=1777903325.1286352 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:05] operator / voice_transcript_partial / voice: inevitable that some of the unknowns and am
  meta: kind=partial | timestamp=1777903325.3253272 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:05] operator / voice_transcript_final / voice: inevitable that some of the unknowns and am
  meta: kind=final | timestamp=1777903325.9340034 | source=final | confidence=0.13 | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:06] operator / voice_transcript_partial / voice: i
  meta: kind=partial | timestamp=1777903326.3362734 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:06] operator / voice_transcript_partial / voice: less
  meta: kind=partial | timestamp=1777903326.5413494 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:06] operator / voice_transcript_partial / voice: i missing
  meta: kind=partial | timestamp=1777903326.9566588 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:07] operator / voice_transcript_partial / voice: receiving my
  meta: kind=partial | timestamp=1777903327.1665666 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:07] operator / voice_transcript_partial / voice: receiving money
  meta: kind=partial | timestamp=1777903327.3687975 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:08] operator / voice_transcript_partial / voice: receiving money in the
  meta: kind=partial | timestamp=1777903328.380462 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:09] operator / voice_transcript_final / voice: receiving money in the
  meta: kind=final | timestamp=1777903329.410785 | source=final | confidence=0.18 | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:12] operator / voice_transcript_partial / voice: scene
  meta: kind=partial | timestamp=1777903332.2590826 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:12] operator / voice_transcript_partial / voice: season
  meta: kind=partial | timestamp=1777903332.6660721 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:13] operator / voice_transcript_final / voice: season
  meta: kind=final | timestamp=1777903333.3182156 | source=final | confidence=0.42 | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:15] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903335.30119 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:15] operator / voice_transcript_partial / voice: see
  meta: kind=partial | timestamp=1777903335.5036318 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:16] operator / voice_transcript_final / voice: see
  meta: kind=final | timestamp=1777903336.3167808 | source=final | confidence=0.66 | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:17] operator / voice_transcript_partial / voice: on
  meta: kind=partial | timestamp=1777903337.1412578 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:17] operator / voice_transcript_partial / voice: on the
  meta: kind=partial | timestamp=1777903337.3334107 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:17] operator / voice_transcript_final / voice: on the
  meta: kind=final | timestamp=1777903337.9424438 | source=final | confidence=0.31 | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:22] operator / voice_transcript_partial / voice: who
  meta: kind=partial | timestamp=1777903342.4394631 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:22] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777903342.6475277 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:22] operator / voice_transcript_partial / voice: one oh
  meta: kind=partial | timestamp=1777903342.8594835 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:23] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777903343.0637493 | source=windows | frequency_hz=410.2 | rms=708 | updated_at=1777903322.6385708
- [2026-05-04 22:02:23] operator / voice_transcript_partial / voice: one that
  meta: kind=partial | timestamp=1777903343.6837225 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:23] operator / voice_transcript_partial / voice: one hundred
  meta: kind=partial | timestamp=1777903343.887242 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:24] operator / voice_transcript_partial / voice: one hand and
  meta: kind=partial | timestamp=1777903344.102687 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:24] operator / voice_transcript_partial / voice: one and one of
  meta: kind=partial | timestamp=1777903344.3064623 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:24] operator / voice_transcript_partial / voice: one hand and a home
  meta: kind=partial | timestamp=1777903344.5092177 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:24] operator / voice_transcript_partial / voice: one hand and a home,
  meta: kind=partial | timestamp=1777903344.9161122 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:25] operator / voice_transcript_partial / voice: one hand and a homeland in
  meta: kind=partial | timestamp=1777903345.3272724 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:25] operator / voice_transcript_partial / voice: one hand and a homeland
  meta: kind=partial | timestamp=1777903345.5267904 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:25] operator / voice_transcript_partial / voice: one hand and a homeland,
  meta: kind=partial | timestamp=1777903345.9317827 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:26] operator / voice_transcript_partial / voice: one hand and a homeland goes to
  meta: kind=partial | timestamp=1777903346.1352513 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:26] operator / voice_transcript_partial / voice: one hand and a home, and has died
  meta: kind=partial | timestamp=1777903346.3379478 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:26] operator / voice_transcript_partial / voice: one hand and a homeland, stanley
  meta: kind=partial | timestamp=1777903346.542589 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:26] operator / voice_transcript_partial / voice: one hand and a homeland, stanley who
  meta: kind=partial | timestamp=1777903346.9474578 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:27] operator / voice_transcript_partial / voice: one hand and a homeland, stanley has
  meta: kind=partial | timestamp=1777903347.1540227 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:27] operator / voice_transcript_partial / voice: one hand and a homeland in the last time i have had
  meta: kind=partial | timestamp=1777903347.5598183 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:27] operator / voice_transcript_partial / voice: one hand and a homeland, stanley has we can
  meta: kind=partial | timestamp=1777903347.760462 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:28] operator / voice_transcript_partial / voice: one hand and a homeland, stanley has put an end
  meta: kind=partial | timestamp=1777903348.1625946 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:28] operator / voice_transcript_partial / voice: one hand and a homeland, stanley has put an unknown
  meta: kind=partial | timestamp=1777903348.3668668 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:28] operator / voice_transcript_partial / voice: one hand and a homeland, stanley has been an ongoing
  meta: kind=partial | timestamp=1777903348.7759314 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:29] operator / voice_transcript_partial / voice: one hand and a homeland, stanley has been an ongoing my
  meta: kind=partial | timestamp=1777903349.1788206 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:29] operator / voice_transcript_partial / voice: one hand and a homeland, stanley has been an ongoing labor
  meta: kind=partial | timestamp=1777903349.3806477 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:29] operator / voice_transcript_partial / voice: one hand and a homeland, stanley has been an ongoing might have
  meta: kind=partial | timestamp=1777903349.5818598 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:30] operator / voice_transcript_partial / voice: one hand and a homeland, stanley has been an ongoing might have been
  meta: kind=partial | timestamp=1777903350.3927016 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:30] operator / voice_transcript_partial / voice: one hand and a homeland, stanley has been an ongoing might have
  meta: kind=partial | timestamp=1777903350.597887 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:30] operator / voice_transcript_partial / voice: one hand and a homeland, stanley has been an ongoing might have a
  meta: kind=partial | timestamp=1777903350.7994087 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:31] operator / voice_transcript_partial / voice: one hand and a homeland, stanley has been an ongoing might have a two
  meta: kind=partial | timestamp=1777903351.4217052 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:31] operator / voice_transcript_partial / voice: one hand and a homeland, stanley has been an ongoing might have a sea of
  meta: kind=partial | timestamp=1777903351.6249666 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:31] operator / voice_transcript_partial / voice: one hand and a homeland, stanley has been an ongoing might have a say in
  meta: kind=partial | timestamp=1777903351.8290355 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:32] operator / voice_transcript_partial / voice: one hand and a homeland, stanley has been an ongoing might have a say in the
  meta: kind=partial | timestamp=1777903352.842745 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:33] operator / voice_transcript_partial / voice: one hand and a homeland, stanley has been an ongoing might have a say in one
  meta: kind=partial | timestamp=1777903353.2503035 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:33] operator / voice_transcript_partial / voice: one hand and a homeland, stanley has been an ongoing might have a say in one of the
  meta: kind=partial | timestamp=1777903353.8737042 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:34] operator / voice_transcript_partial / voice: one hand and a homeland, stanley has been an ongoing might have a say in nineteen eighty one
  meta: kind=partial | timestamp=1777903354.0779324 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:34] operator / voice_transcript_partial / voice: one hand and a homeland, stanley has been an ongoing might have a say in nineteen eighty one one
  meta: kind=partial | timestamp=1777903354.4826937 | source=windows | frequency_hz=398.4 | rms=486 | updated_at=1777903343.2494533
- [2026-05-04 22:02:35] operator / voice_transcript_final / voice: one hand and a homeland stanley has been an ongoing might have a say in 19811
  meta: kind=final | timestamp=1777903355.942782 | source=final | confidence=0.04 | frequency_hz=351.6 | rms=155 | updated_at=1777903355.1495275
- [2026-05-04 22:02:38] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777903358.8008492 | source=windows | frequency_hz=406.2 | rms=576 | updated_at=1777903358.7303452
- [2026-05-04 22:02:39] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777903359.2093377 | source=windows | frequency_hz=406.2 | rms=576 | updated_at=1777903358.7303452
- [2026-05-04 22:02:39] operator / voice_transcript_partial / voice: to arrange a
  meta: kind=partial | timestamp=1777903359.4113166 | source=windows | frequency_hz=406.2 | rms=576 | updated_at=1777903358.7303452
- [2026-05-04 22:02:39] operator / voice_transcript_partial / voice: and then
  meta: kind=partial | timestamp=1777903359.615538 | source=windows | frequency_hz=406.2 | rms=576 | updated_at=1777903358.7303452
- [2026-05-04 22:02:40] operator / voice_transcript_partial / voice: and general
  meta: kind=partial | timestamp=1777903360.0198362 | source=windows | frequency_hz=406.2 | rms=576 | updated_at=1777903358.7303452
- [2026-05-04 22:02:40] operator / voice_transcript_partial / voice: and general news
  meta: kind=partial | timestamp=1777903360.222906 | source=windows | frequency_hz=406.2 | rms=576 | updated_at=1777903358.7303452
- [2026-05-04 22:02:40] operator / voice_transcript_partial / voice: and general news and
  meta: kind=partial | timestamp=1777903360.4260945 | source=windows | frequency_hz=406.2 | rms=576 | updated_at=1777903358.7303452
- [2026-05-04 22:02:40] operator / voice_transcript_partial / voice: billion gentleman's agreement
  meta: kind=partial | timestamp=1777903360.6267617 | source=windows | frequency_hz=406.2 | rms=576 | updated_at=1777903358.7303452
- [2026-05-04 22:02:41] operator / voice_transcript_partial / voice: and gentleness and then
  meta: kind=partial | timestamp=1777903361.032244 | source=windows | frequency_hz=406.2 | rms=576 | updated_at=1777903358.7303452
- [2026-05-04 22:02:41] operator / voice_transcript_partial / voice: and gentleness and then lying
  meta: kind=partial | timestamp=1777903361.2497787 | source=windows | frequency_hz=406.2 | rms=576 | updated_at=1777903358.7303452
- [2026-05-04 22:02:41] operator / voice_transcript_partial / voice: and gentleness and then won the
  meta: kind=partial | timestamp=1777903361.453664 | source=windows | frequency_hz=406.2 | rms=576 | updated_at=1777903358.7303452
- [2026-05-04 22:02:42] operator / voice_transcript_final / voice: and gentleness and then won the
  meta: kind=final | timestamp=1777903362.2886546 | source=final | confidence=0.1 | frequency_hz=406.2 | rms=576 | updated_at=1777903358.7303452
- [2026-05-04 22:02:47] operator / voice_transcript_partial / voice: run
  meta: kind=partial | timestamp=1777903367.5354304 | source=windows | frequency_hz=406.2 | rms=576 | updated_at=1777903358.7303452
- [2026-05-04 22:02:49] operator / voice_transcript_final / voice: one
  meta: kind=final | timestamp=1777903369.378748 | source=final | confidence=0.4 | frequency_hz=406.2 | rms=576 | updated_at=1777903358.7303452
- [2026-05-04 22:02:51] operator / voice_transcript_partial / voice: who
  meta: kind=partial | timestamp=1777903371.8468235 | source=windows | frequency_hz=406.2 | rms=576 | updated_at=1777903358.7303452
- [2026-05-04 22:02:52] operator / voice_transcript_partial / voice: more
  meta: kind=partial | timestamp=1777903372.0498607 | source=windows | frequency_hz=406.2 | rms=576 | updated_at=1777903358.7303452
- [2026-05-04 22:02:52] operator / voice_transcript_partial / voice: who
  meta: kind=partial | timestamp=1777903372.252655 | source=windows | frequency_hz=406.2 | rms=576 | updated_at=1777903358.7303452
- [2026-05-04 22:02:52] operator / voice_transcript_partial / voice: only
  meta: kind=partial | timestamp=1777903372.454692 | source=windows | frequency_hz=406.2 | rms=576 | updated_at=1777903358.7303452
- [2026-05-04 22:02:52] operator / voice_transcript_partial / voice: only the
  meta: kind=partial | timestamp=1777903372.6577816 | source=windows | frequency_hz=406.2 | rms=576 | updated_at=1777903358.7303452
- [2026-05-04 22:02:53] operator / voice_transcript_partial / voice: only be a
  meta: kind=partial | timestamp=1777903373.2854545 | source=windows | frequency_hz=406.2 | rms=576 | updated_at=1777903358.7303452
- [2026-05-04 22:02:53] operator / voice_transcript_partial / voice: only be a loss
  meta: kind=partial | timestamp=1777903373.4885514 | source=windows | frequency_hz=418.0 | rms=750 | updated_at=1777903373.3303003
- [2026-05-04 22:02:53] operator / voice_transcript_partial / voice: only be a lesson
  meta: kind=partial | timestamp=1777903373.69108 | source=windows | frequency_hz=418.0 | rms=750 | updated_at=1777903373.3303003
- [2026-05-04 22:02:53] operator / voice_transcript_partial / voice: only be a lesson in the
  meta: kind=partial | timestamp=1777903373.893622 | source=windows | frequency_hz=418.0 | rms=750 | updated_at=1777903373.3303003
- [2026-05-04 22:02:54] operator / voice_transcript_partial / voice: only be a lesson in the not
  meta: kind=partial | timestamp=1777903374.5078459 | source=windows | frequency_hz=418.0 | rms=750 | updated_at=1777903373.3303003
- [2026-05-04 22:02:54] operator / voice_transcript_partial / voice: only be a lesson in the night was
  meta: kind=partial | timestamp=1777903374.7092962 | source=windows | frequency_hz=418.0 | rms=750 | updated_at=1777903373.3303003
- [2026-05-04 22:02:54] operator / voice_transcript_partial / voice: only be a lesson in the night was a
  meta: kind=partial | timestamp=1777903374.911419 | source=windows | frequency_hz=418.0 | rms=750 | updated_at=1777903373.3303003
- [2026-05-04 22:02:55] operator / voice_transcript_partial / voice: only be a lesson in the cause of
  meta: kind=partial | timestamp=1777903375.3232768 | source=windows | frequency_hz=418.0 | rms=750 | updated_at=1777903373.3303003
- [2026-05-04 22:02:55] operator / voice_transcript_partial / voice: only be a lesson in the cause of my
  meta: kind=partial | timestamp=1777903375.5287035 | source=windows | frequency_hz=418.0 | rms=750 | updated_at=1777903373.3303003
- [2026-05-04 22:02:55] operator / voice_transcript_partial / voice: only be a lesson in the cause of money
  meta: kind=partial | timestamp=1777903375.7313063 | source=windows | frequency_hz=418.0 | rms=750 | updated_at=1777903373.3303003
- [2026-05-04 22:02:55] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the
  meta: kind=partial | timestamp=1777903375.9361231 | source=windows | frequency_hz=418.0 | rms=750 | updated_at=1777903373.3303003
- [2026-05-04 22:02:56] operator / voice_transcript_partial / voice: only be a lesson in the cause of money while
  meta: kind=partial | timestamp=1777903376.3429005 | source=windows | frequency_hz=418.0 | rms=750 | updated_at=1777903373.3303003
- [2026-05-04 22:02:56] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on a large
  meta: kind=partial | timestamp=1777903376.5468373 | source=windows | frequency_hz=418.0 | rms=750 | updated_at=1777903373.3303003
- [2026-05-04 22:02:56] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of
  meta: kind=partial | timestamp=1777903376.7477324 | source=windows | frequency_hz=418.0 | rms=750 | updated_at=1777903373.3303003
- [2026-05-04 22:02:57] operator / voice_transcript_partial / voice: only be a lesson in the cause of money while jim muir
  meta: kind=partial | timestamp=1777903377.5633442 | source=windows | frequency_hz=394.5 | rms=377 | updated_at=1777903377.550321
- [2026-05-04 22:02:57] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of one
  meta: kind=partial | timestamp=1777903377.768028 | source=windows | frequency_hz=394.5 | rms=377 | updated_at=1777903377.550321
- [2026-05-04 22:02:58] operator / voice_transcript_partial / voice: only be a lesson in the cause of money while she's a knee and missed
  meta: kind=partial | timestamp=1777903378.1769943 | source=windows | frequency_hz=394.5 | rms=377 | updated_at=1777903377.550321
- [2026-05-04 22:02:58] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco
  meta: kind=partial | timestamp=1777903378.5811653 | source=windows | frequency_hz=394.5 | rms=377 | updated_at=1777903377.550321
- [2026-05-04 22:02:58] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the assailant
  meta: kind=partial | timestamp=1777903378.7842033 | source=windows | frequency_hz=394.5 | rms=377 | updated_at=1777903377.550321
- [2026-05-04 22:02:58] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco the only
  meta: kind=partial | timestamp=1777903378.9865048 | source=windows | frequency_hz=394.5 | rms=377 | updated_at=1777903377.550321
- [2026-05-04 22:02:59] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco every day
  meta: kind=partial | timestamp=1777903379.1890893 | source=windows | frequency_hz=394.5 | rms=377 | updated_at=1777903377.550321
- [2026-05-04 22:02:59] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco the retail
  meta: kind=partial | timestamp=1777903379.61132 | source=windows | frequency_hz=394.5 | rms=377 | updated_at=1777903377.550321
- [2026-05-04 22:02:59] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco every day and
  meta: kind=partial | timestamp=1777903379.8310342 | source=windows | frequency_hz=394.5 | rms=377 | updated_at=1777903377.550321
- [2026-05-04 22:03:00] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco every day and some
  meta: kind=partial | timestamp=1777903380.0322 | source=windows | frequency_hz=394.5 | rms=377 | updated_at=1777903377.550321
- [2026-05-04 22:03:00] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco every day and has no
  meta: kind=partial | timestamp=1777903380.236464 | source=windows | frequency_hz=394.5 | rms=377 | updated_at=1777903377.550321
- [2026-05-04 22:03:00] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco every day and isabelle
  meta: kind=partial | timestamp=1777903380.4532983 | source=windows | frequency_hz=394.5 | rms=377 | updated_at=1777903377.550321
- [2026-05-04 22:03:00] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco every day and isabelle what
  meta: kind=partial | timestamp=1777903380.8585236 | source=windows | frequency_hz=367.2 | rms=923 | updated_at=1777903380.619795
- [2026-05-04 22:03:01] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco every day and isabel montero
  meta: kind=partial | timestamp=1777903381.2625973 | source=windows | frequency_hz=367.2 | rms=923 | updated_at=1777903380.619795
- [2026-05-04 22:03:01] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco every day and has no longer
  meta: kind=partial | timestamp=1777903381.4685938 | source=windows | frequency_hz=367.2 | rms=923 | updated_at=1777903380.619795
- [2026-05-04 22:03:01] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco every day and has no longer have
  meta: kind=partial | timestamp=1777903381.668499 | source=windows | frequency_hz=367.2 | rms=923 | updated_at=1777903380.619795
- [2026-05-04 22:03:02] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco every day and has no longer have been
  meta: kind=partial | timestamp=1777903382.8896303 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:03] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco every day and has no longer have been in
  meta: kind=partial | timestamp=1777903383.295868 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:03] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco every day and has no longer have been in the
  meta: kind=partial | timestamp=1777903383.497129 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:03] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco every day and has no longer have seen enough of
  meta: kind=partial | timestamp=1777903383.7121837 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:03] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco every day and has no longer have been inundated
  meta: kind=partial | timestamp=1777903383.914991 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:04] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco every day and has no longer have been inundated in
  meta: kind=partial | timestamp=1777903384.1168952 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:04] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco every day and has no longer have been inundated in a
  meta: kind=partial | timestamp=1777903384.7225397 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:04] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco every day and has no longer have been inundated in an
  meta: kind=partial | timestamp=1777903384.9323626 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:05] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco every day and has no longer have been inundated in a native of
  meta: kind=partial | timestamp=1777903385.129564 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:05] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco every day and has no longer have seen enough of an innocent man
  meta: kind=partial | timestamp=1777903385.5382173 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:05] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco every day and has no longer have been inundated in an amendment
  meta: kind=partial | timestamp=1777903385.7483246 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:06] operator / voice_transcript_partial / voice: only be a lesson in the cause of money on the object of me and the sco every day and has no longer have been inundated in an amendment to
  meta: kind=partial | timestamp=1777903386.7699776 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:07] operator / voice_transcript_final / voice: only be a lesson in the cause of money on the object of me and the sco every day and has no longer have been inundated in an amendment to
  meta: kind=final | timestamp=1777903387.196427 | source=final | confidence=0.15 | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:08] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777903388.1891313 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:08] operator / voice_transcript_partial / voice: ban on
  meta: kind=partial | timestamp=1777903388.6097932 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:09] operator / voice_transcript_partial / voice: one of the
  meta: kind=partial | timestamp=1777903389.223528 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:09] operator / voice_transcript_partial / voice: ban on guns
  meta: kind=partial | timestamp=1777903389.437906 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:09] operator / voice_transcript_partial / voice: ban on currency
  meta: kind=partial | timestamp=1777903389.6436949 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:10] operator / voice_transcript_partial / voice: ban on currency that
  meta: kind=partial | timestamp=1777903390.0681396 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:10] operator / voice_transcript_partial / voice: ban on currency that has an
  meta: kind=partial | timestamp=1777903390.2667599 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:10] operator / voice_transcript_partial / voice: ban on currency thousand
  meta: kind=partial | timestamp=1777903390.4685535 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:10] operator / voice_transcript_partial / voice: ban on currency that has an all
  meta: kind=partial | timestamp=1777903390.669798 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:11] operator / voice_transcript_partial / voice: ban on currency that has and will be
  meta: kind=partial | timestamp=1777903391.0760593 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:11] operator / voice_transcript_partial / voice: ban on currency balance among all these
  meta: kind=partial | timestamp=1777903391.277002 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:11] operator / voice_transcript_partial / voice: ban on currency balance among all these young
  meta: kind=partial | timestamp=1777903391.479713 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:11] operator / voice_transcript_partial / voice: ban on currency that has and will be some reason
  meta: kind=partial | timestamp=1777903391.6814406 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:12] operator / voice_transcript_partial / voice: ban on currency balance among all the things about
  meta: kind=partial | timestamp=1777903392.0861208 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:12] operator / voice_transcript_partial / voice: ban on currency balance among all the things about one
  meta: kind=partial | timestamp=1777903392.491634 | source=windows | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:12] operator / voice_transcript_final / voice: ban on currency balance among all the things about one
  meta: kind=final | timestamp=1777903392.8977528 | source=final | confidence=0.17 | frequency_hz=383.9 | rms=280 | updated_at=1777903382.030604
- [2026-05-04 22:03:13] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777903393.7104363 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:13] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777903393.9145722 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:15] operator / voice_transcript_partial / voice: and one
  meta: kind=partial | timestamp=1777903395.33506 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:15] operator / voice_transcript_partial / voice: and one that
  meta: kind=partial | timestamp=1777903395.538706 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:15] operator / voice_transcript_partial / voice: movie and liane
  meta: kind=partial | timestamp=1777903395.744995 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:16] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 22:03:16] operator / voice_transcript_partial / voice: movie and liane and
  meta: kind=partial | timestamp=1777903396.1499777 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:16] operator / voice_transcript_partial / voice: movie and liane and what
  meta: kind=partial | timestamp=1777903396.5537827 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:16] operator / voice_transcript_partial / voice: and one man and little
  meta: kind=partial | timestamp=1777903396.760128 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:16] operator / voice_transcript_partial / voice: movie and liane and what level
  meta: kind=partial | timestamp=1777903396.9590435 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:17] operator / voice_transcript_partial / voice: movie and liane and leslie aloha
  meta: kind=partial | timestamp=1777903397.5662425 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:17] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 22:03:17] operator / voice_transcript_partial / voice: movie and liane and leslie, who
  meta: kind=partial | timestamp=1777903397.772596 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:17] operator / voice_transcript_partial / voice: in unpaid leave an indelible ink one hundred
  meta: kind=partial | timestamp=1777903397.9726963 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:18] operator / voice_transcript_partial / voice: in unpaid leave an indelible ink one half to lead and
  meta: kind=partial | timestamp=1777903398.1748984 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:18] operator / voice_transcript_partial / voice: in unpaid leave an indelible ink one half million tons
  meta: kind=partial | timestamp=1777903398.5917597 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:18] operator / voice_transcript_partial / voice: in unpaid leave an indelible ink one half million guns in the
  meta: kind=partial | timestamp=1777903398.7830968 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:19] operator / voice_transcript_partial / voice: in unpaid leave an indelible ink one half million guns in the end
  meta: kind=partial | timestamp=1777903399.0005803 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:19] operator / voice_transcript_partial / voice: in unpaid leave an indelible ink one half million tons of u.n. is
  meta: kind=partial | timestamp=1777903399.2019472 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:19] operator / voice_transcript_partial / voice: in unpaid leave an indelible ink one half million tons of u.n. is an
  meta: kind=partial | timestamp=1777903399.404961 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:19] operator / voice_transcript_partial / voice: in unpaid leave an indelible ink one half million guns in the ins and
  meta: kind=partial | timestamp=1777903399.60852 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:20] operator / voice_transcript_partial / voice: in unpaid leave an indelible ink one half million tons of u.n. is undefeated
  meta: kind=partial | timestamp=1777903400.0115752 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:20] operator / voice_transcript_partial / voice: in unpaid leave an indelible ink one half million tons of u.n. is undefeated in
  meta: kind=partial | timestamp=1777903400.2149954 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:22] operator / voice_transcript_partial / voice: in unpaid leave an indelible ink one half million guns in the ins and he's in his
  meta: kind=partial | timestamp=1777903402.2631986 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:22] operator / voice_transcript_partial / voice: in unpaid leave an indelible ink one half million tons of u.n. is undefeated in
  meta: kind=partial | timestamp=1777903402.464876 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:22] operator / voice_transcript_partial / voice: in unpaid leave an indelible ink one half million guns in the ins and he's in his own
  meta: kind=partial | timestamp=1777903402.669769 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:23] operator / voice_transcript_partial / voice: in unpaid leave an indelible ink one half million tons of u.n. is undefeated in reason for
  meta: kind=partial | timestamp=1777903403.2966695 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:23] operator / voice_transcript_partial / voice: in unpaid leave an indelible ink one half million guns in the ins and he's in his own phone
  meta: kind=partial | timestamp=1777903403.5122075 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:24] operator / voice_transcript_partial / voice: in unpaid leave an indelible ink one half million guns in the ins and he's in his own phone in
  meta: kind=partial | timestamp=1777903404.1229491 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:24] operator / voice_transcript_partial / voice: in unpaid leave an indelible ink one half million guns in the ins and he's in his own and the
  meta: kind=partial | timestamp=1777903404.5334895 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:25] operator / voice_transcript_partial / voice: in unpaid leave an indelible ink one half million tons of u.n. is undefeated in reason than the ones
  meta: kind=partial | timestamp=1777903405.147027 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:25] operator / voice_transcript_final / voice: in unpaid leave an indelible ink 1 2 million tons of u n is undefeated in reason than the ones
  meta: kind=final | timestamp=1777903405.7589612 | source=final | confidence=0.13 | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:25] operator / voice_command / voice: in unpaid leave an indelible ink 1 2 million tons of u n is undefeated in reason than the ones
  meta: normalized=True
- [2026-05-04 22:03:26] assistant / spoken_confirmation / voice: Received. I started your assistant request about in unpaid leave an indelible ink 1 2 million tons of. in the background.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:03:30] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777903410.3520951 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:30] operator / voice_transcript_partial / voice: in a
  meta: kind=partial | timestamp=1777903410.7743745 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:30] operator / voice_transcript_partial / voice: in as
  meta: kind=partial | timestamp=1777903410.986032 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:31] operator / voice_transcript_final / voice: in as
  meta: kind=final | timestamp=1777903411.6177094 | source=final | confidence=0.19 | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:34] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777903414.6133149 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:34] operator / voice_transcript_partial / voice: an
  meta: kind=partial | timestamp=1777903414.8264046 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:35] operator / voice_transcript_partial / voice: an in
  meta: kind=partial | timestamp=1777903415.7401729 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:36] operator / voice_transcript_partial / voice: an indian
  meta: kind=partial | timestamp=1777903416.36206 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:37] operator / voice_transcript_partial / voice: an indian and
  meta: kind=partial | timestamp=1777903417.1896267 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:40] operator / voice_transcript_final / voice: an indian and
  meta: kind=final | timestamp=1777903420.7169778 | source=final | confidence=0.2 | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:40] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777903420.931028 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:41] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777903421.1351593 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:41] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777903421.5406048 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:41] operator / voice_transcript_partial / voice: indian war
  meta: kind=partial | timestamp=1777903421.9453998 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:42] operator / voice_transcript_partial / voice: you want to
  meta: kind=partial | timestamp=1777903422.1642258 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:42] operator / voice_transcript_partial / voice: a blocked and
  meta: kind=partial | timestamp=1777903422.5708613 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:42] operator / voice_transcript_partial / voice: you want to move
  meta: kind=partial | timestamp=1777903422.7750452 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:43] operator / voice_transcript_partial / voice: you want to move in
  meta: kind=partial | timestamp=1777903423.394502 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:43] operator / voice_transcript_partial / voice: you want to move and
  meta: kind=partial | timestamp=1777903423.8006382 | source=windows | frequency_hz=414.1 | rms=154 | updated_at=1777903393.291345
- [2026-05-04 22:03:45] operator / voice_transcript_final / voice: you want to move and
  meta: kind=final | timestamp=1777903425.4286458 | source=final | confidence=0.29 | frequency_hz=293.0 | rms=266 | updated_at=1777903424.260393
- [2026-05-04 22:03:46] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777903426.7084432 | source=windows | frequency_hz=378.9 | rms=291 | updated_at=1777903426.1834404
- [2026-05-04 22:03:46] operator / voice_transcript_partial / voice: miz
  meta: kind=partial | timestamp=1777903426.7084432 | source=windows | frequency_hz=378.9 | rms=291 | updated_at=1777903426.1834404
- [2026-05-04 22:03:46] operator / voice_transcript_partial / voice: this
  meta: kind=partial | timestamp=1777903426.9104915 | source=windows | frequency_hz=378.9 | rms=291 | updated_at=1777903426.1834404
- [2026-05-04 22:03:47] operator / voice_transcript_final / voice: this
  meta: kind=final | timestamp=1777903427.3208253 | source=final | confidence=0.08 | frequency_hz=378.9 | rms=291 | updated_at=1777903426.1834404
- [2026-05-04 22:03:51] operator / voice_transcript_partial / voice: would
  meta: kind=partial | timestamp=1777903431.4183521 | source=windows | frequency_hz=378.9 | rms=291 | updated_at=1777903426.1834404
- [2026-05-04 22:03:51] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777903431.620829 | source=windows | frequency_hz=378.9 | rms=291 | updated_at=1777903426.1834404
- [2026-05-04 22:03:52] operator / voice_transcript_partial / voice: and some
  meta: kind=partial | timestamp=1777903432.039658 | source=windows | frequency_hz=418.0 | rms=132 | updated_at=1777903431.691006
- [2026-05-04 22:03:52] operator / voice_transcript_partial / voice: is an
  meta: kind=partial | timestamp=1777903432.247649 | source=windows | frequency_hz=418.0 | rms=132 | updated_at=1777903431.691006
- [2026-05-04 22:03:53] operator / voice_transcript_final / voice: is an
  meta: kind=final | timestamp=1777903433.1151478 | source=final | confidence=0.27 | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:03:56] operator / voice_transcript_partial / voice: online
  meta: kind=partial | timestamp=1777903436.3959436 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:03:57] operator / voice_transcript_final / voice: online
  meta: kind=final | timestamp=1777903437.4335463 | source=final | confidence=0.49 | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:01] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777903441.4625764 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:02] operator / voice_transcript_partial / voice: more than
  meta: kind=partial | timestamp=1777903442.1228628 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:02] operator / voice_transcript_partial / voice: one and see
  meta: kind=partial | timestamp=1777903442.390053 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:02] operator / voice_transcript_partial / voice: more than his seat
  meta: kind=partial | timestamp=1777903442.6000466 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:02] operator / voice_transcript_partial / voice: one and seeing what the
  meta: kind=partial | timestamp=1777903442.804556 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:03] operator / voice_transcript_partial / voice: one and seeing what these
  meta: kind=partial | timestamp=1777903443.0083826 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:03] operator / voice_transcript_partial / voice: one and seeing what do you see
  meta: kind=partial | timestamp=1777903443.2292008 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:03] operator / voice_transcript_partial / voice: one and seeing what they're seeing
  meta: kind=partial | timestamp=1777903443.6444535 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:03] operator / voice_transcript_partial / voice: one and seeing what they're seeing me
  meta: kind=partial | timestamp=1777903443.8456445 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:05] operator / voice_transcript_final / voice: one and seeing what they re seeing me
  meta: kind=final | timestamp=1777903445.320809 | source=final | confidence=0.46 | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:05] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777903445.320809 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:05] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777903445.3218148 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:05] operator / voice_transcript_partial / voice: that the
  meta: kind=partial | timestamp=1777903445.5236554 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:06] operator / voice_transcript_final / voice: that the
  meta: kind=final | timestamp=1777903446.1581633 | source=final | confidence=0.12 | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:08] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777903448.4370582 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:09] operator / voice_transcript_partial / voice: one on
  meta: kind=partial | timestamp=1777903449.088231 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:10] operator / voice_transcript_final / voice: one on
  meta: kind=final | timestamp=1777903450.13797 | source=final | confidence=0.56 | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:11] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777903451.1825175 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:11] operator / voice_transcript_partial / voice: youth
  meta: kind=partial | timestamp=1777903451.5780196 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:11] operator / voice_transcript_partial / voice: in the thing
  meta: kind=partial | timestamp=1777903451.794362 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:12] operator / voice_transcript_partial / voice: in the thing that has
  meta: kind=partial | timestamp=1777903452.6073813 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:13] operator / voice_transcript_partial / voice: in the thing that has been
  meta: kind=partial | timestamp=1777903453.6314692 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:13] operator / voice_transcript_partial / voice: in the thing that has an
  meta: kind=partial | timestamp=1777903453.8356092 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:15] operator / voice_transcript_final / voice: in the thing that has an
  meta: kind=final | timestamp=1777903455.1191034 | source=final | confidence=0.38 | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:15] operator / voice_transcript_partial / voice: eight
  meta: kind=partial | timestamp=1777903455.120608 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:15] operator / voice_transcript_partial / voice: immense
  meta: kind=partial | timestamp=1777903455.120608 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:15] operator / voice_transcript_partial / voice: insane
  meta: kind=partial | timestamp=1777903455.505009 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:15] operator / voice_transcript_partial / voice: immense as a
  meta: kind=partial | timestamp=1777903455.7061257 | source=windows | frequency_hz=392.0 | rms=219 | updated_at=1777903432.581094
- [2026-05-04 22:04:15] operator / voice_transcript_partial / voice: insane thing you
  meta: kind=partial | timestamp=1777903455.9106717 | source=windows | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:16] operator / voice_transcript_partial / voice: insane thing you say
  meta: kind=partial | timestamp=1777903456.9399526 | source=windows | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:17] operator / voice_transcript_partial / voice: insane thing you see
  meta: kind=partial | timestamp=1777903457.141694 | source=windows | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:17] operator / voice_transcript_final / voice: insane thing you see
  meta: kind=final | timestamp=1777903457.7631278 | source=final | confidence=0.44 | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:24] operator / voice_transcript_partial / voice: its
  meta: kind=partial | timestamp=1777903464.141651 | source=windows | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:24] operator / voice_transcript_partial / voice: see
  meta: kind=partial | timestamp=1777903464.3461637 | source=windows | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:24] operator / voice_transcript_partial / voice: a few
  meta: kind=partial | timestamp=1777903464.778973 | source=windows | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:24] operator / voice_transcript_partial / voice: fewer
  meta: kind=partial | timestamp=1777903464.9876447 | source=windows | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:25] operator / voice_transcript_final / voice: fewer
  meta: kind=final | timestamp=1777903465.203278 | source=final | confidence=0.03 | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:28] operator / voice_transcript_partial / voice: than
  meta: kind=partial | timestamp=1777903468.691546 | source=windows | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:29] operator / voice_transcript_partial / voice: than six
  meta: kind=partial | timestamp=1777903469.1017995 | source=windows | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:29] operator / voice_transcript_partial / voice: resources and
  meta: kind=partial | timestamp=1777903469.5116186 | source=windows | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:29] operator / voice_transcript_partial / voice: resources and was
  meta: kind=partial | timestamp=1777903469.7176266 | source=windows | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:30] operator / voice_transcript_partial / voice: resources and was one
  meta: kind=partial | timestamp=1777903470.3258615 | source=windows | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:31] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 22:04:31] operator / voice_transcript_final / voice: resources and was one
  meta: kind=final | timestamp=1777903471.5775113 | source=final | confidence=0.22 | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:34] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777903474.0617175 | source=windows | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:34] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777903474.2658393 | source=windows | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:34] operator / voice_transcript_partial / voice: one one
  meta: kind=partial | timestamp=1777903474.8831604 | source=windows | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:35] operator / voice_transcript_partial / voice: one one six
  meta: kind=partial | timestamp=1777903475.5017993 | source=windows | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:35] operator / voice_transcript_partial / voice: one one six in
  meta: kind=partial | timestamp=1777903475.8975635 | source=windows | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:36] operator / voice_transcript_partial / voice: one one six in the
  meta: kind=partial | timestamp=1777903476.3050427 | source=windows | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:36] operator / voice_transcript_partial / voice: one one six eight one
  meta: kind=partial | timestamp=1777903476.5107353 | source=windows | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:37] operator / voice_transcript_partial / voice: one one six eight one nine
  meta: kind=partial | timestamp=1777903477.1114695 | source=windows | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:37] operator / voice_transcript_partial / voice: one one six eight one one
  meta: kind=partial | timestamp=1777903477.3251123 | source=windows | frequency_hz=253.3 | rms=125 | updated_at=1777903455.8814156
- [2026-05-04 22:04:38] operator / voice_transcript_final / voice: 116811
  meta: kind=final | timestamp=1777903478.1303427 | source=final | confidence=0.23 | frequency_hz=394.5 | rms=230 | updated_at=1777903477.3824651
- [2026-05-04 22:04:42] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777903482.8781996 | source=windows | frequency_hz=363.3 | rms=315 | updated_at=1777903482.6339474
- [2026-05-04 22:04:42] operator / voice_transcript_partial / voice: eight
  meta: kind=partial | timestamp=1777903482.8781996 | source=windows | frequency_hz=363.3 | rms=315 | updated_at=1777903482.6339474
- [2026-05-04 22:04:43] operator / voice_transcript_partial / voice: eight and
  meta: kind=partial | timestamp=1777903483.2851055 | source=windows | frequency_hz=363.3 | rms=315 | updated_at=1777903482.6339474
- [2026-05-04 22:04:43] operator / voice_transcript_partial / voice: eight oh
  meta: kind=partial | timestamp=1777903483.4889119 | source=windows | frequency_hz=363.3 | rms=315 | updated_at=1777903482.6339474
- [2026-05-04 22:04:43] operator / voice_transcript_partial / voice: one oh
  meta: kind=partial | timestamp=1777903483.699864 | source=windows | frequency_hz=363.3 | rms=315 | updated_at=1777903482.6339474
- [2026-05-04 22:04:44] operator / voice_transcript_final / voice: 10
  meta: kind=final | timestamp=1777903484.34209 | source=final | confidence=0.11 | frequency_hz=363.3 | rms=315 | updated_at=1777903482.6339474
- [2026-05-04 22:04:44] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777903484.7854733 | source=windows | frequency_hz=363.3 | rms=315 | updated_at=1777903482.6339474
- [2026-05-04 22:04:46] operator / voice_transcript_partial / voice: one dollars
  meta: kind=partial | timestamp=1777903486.253241 | source=windows | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:04:46] operator / voice_transcript_partial / voice: one dollars and
  meta: kind=partial | timestamp=1777903486.253241 | source=windows | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:04:46] operator / voice_transcript_partial / voice: million dollars round
  meta: kind=partial | timestamp=1777903486.253241 | source=windows | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:04:46] operator / voice_transcript_partial / voice: yen or
  meta: kind=partial | timestamp=1777903486.2542465 | source=windows | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:04:46] operator / voice_transcript_partial / voice: one dollars and ninety
  meta: kind=partial | timestamp=1777903486.2542465 | source=windows | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:04:46] operator / voice_transcript_partial / voice: million dollars round one in
  meta: kind=partial | timestamp=1777903486.8981378 | source=windows | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:04:47] operator / voice_transcript_final / voice: 1 000 000 round one in
  meta: kind=final | timestamp=1777903487.5547652 | source=final | confidence=0.2 | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:04:48] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777903488.4556673 | source=windows | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:04:48] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777903488.9285367 | source=windows | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:04:49] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 22:04:49] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777903489.4542031 | source=final | confidence=0.81 | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:04:52] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777903492.7451663 | source=windows | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:04:53] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777903493.0558574 | source=windows | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:04:53] operator / voice_transcript_final / voice: e
  meta: kind=final | timestamp=1777903493.0563624 | source=final | confidence=0.52 | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:04:53] operator / voice_command / voice: e
  meta: normalized=True
- [2026-05-04 22:04:53] assistant / spoken_confirmation / voice: Received. I started your assistant request about e in the background.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:04:55] operator / voice_transcript_partial / voice: c.
  meta: kind=partial | timestamp=1777903495.132417 | source=windows | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:04:55] operator / voice_transcript_partial / voice: scene
  meta: kind=partial | timestamp=1777903495.1334174 | source=windows | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:04:55] operator / voice_transcript_partial / voice: seen in
  meta: kind=partial | timestamp=1777903495.3537116 | source=windows | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:04:55] operator / voice_transcript_partial / voice: scene and
  meta: kind=partial | timestamp=1777903495.3547158 | source=windows | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:04:57] operator / voice_transcript_partial / voice: scene and an
  meta: kind=partial | timestamp=1777903497.6513374 | source=windows | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:04:58] operator / voice_transcript_final / voice: scene and an
  meta: kind=final | timestamp=1777903498.4872737 | source=final | confidence=0.46 | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:04:58] operator / voice_command / voice: scene and an
  meta: normalized=True
- [2026-05-04 22:04:58] assistant / assistant_prompt / text: Assistant request queued: assistant request about scene and an (position 1).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 22:04:58] operator / voice_transcript_partial / voice: who
  meta: kind=partial | timestamp=1777903498.4872737 | source=windows | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:04:58] operator / voice_transcript_partial / voice: who are you
  meta: kind=partial | timestamp=1777903498.4872737 | source=windows | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:04:59] assistant / spoken_confirmation / voice: I am still finishing assistant request about e. I queued your assistant request about scene and an. It is number 1 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:04:59] operator / voice_transcript_partial / voice: who are you an
  meta: kind=partial | timestamp=1777903499.3700664 | source=windows | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:05:00] operator / voice_transcript_partial / voice: korea and in
  meta: kind=partial | timestamp=1777903500.484889 | source=windows | frequency_hz=359.4 | rms=294 | updated_at=1777903485.5724401
- [2026-05-04 22:05:02] operator / voice_transcript_partial / voice: korean and
  meta: kind=partial | timestamp=1777903502.0749342 | source=windows | frequency_hz=339.9 | rms=541 | updated_at=1777903501.8628092
- [2026-05-04 22:05:04] operator / voice_transcript_partial / voice: warrior and you've seen
  meta: kind=partial | timestamp=1777903504.4060447 | source=windows | frequency_hz=339.9 | rms=541 | updated_at=1777903501.8628092
- [2026-05-04 22:05:06] operator / voice_transcript_partial / voice: warrior and you've seen the
  meta: kind=partial | timestamp=1777903506.309014 | source=windows | frequency_hz=341.0 | rms=501 | updated_at=1777903505.396825
- [2026-05-04 22:05:07] operator / voice_transcript_partial / voice: warrior and you've seen the suit
  meta: kind=partial | timestamp=1777903507.770334 | source=windows | frequency_hz=341.0 | rms=501 | updated_at=1777903505.396825
- [2026-05-04 22:05:07] operator / voice_transcript_partial / voice: warrior and you've seen the suit which
  meta: kind=partial | timestamp=1777903507.9718966 | source=windows | frequency_hz=341.0 | rms=501 | updated_at=1777903505.396825
- [2026-05-04 22:05:08] operator / voice_transcript_partial / voice: warrior and you've seen the same stuff
  meta: kind=partial | timestamp=1777903508.4839969 | source=windows | frequency_hz=208.5 | rms=228 | updated_at=1777903508.3256884
- [2026-05-04 22:05:08] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have
  meta: kind=partial | timestamp=1777903508.4839969 | source=windows | frequency_hz=208.5 | rms=228 | updated_at=1777903508.3256884
- [2026-05-04 22:05:09] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have a
  meta: kind=partial | timestamp=1777903509.354047 | source=windows | frequency_hz=208.5 | rms=228 | updated_at=1777903508.3256884
- [2026-05-04 22:05:09] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as
  meta: kind=partial | timestamp=1777903509.55999 | source=windows | frequency_hz=208.5 | rms=228 | updated_at=1777903508.3256884
- [2026-05-04 22:05:10] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the
  meta: kind=partial | timestamp=1777903510.8007054 | source=windows | frequency_hz=151.9 | rms=225 | updated_at=1777903509.7327106
- [2026-05-04 22:05:11] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have realized that he
  meta: kind=partial | timestamp=1777903511.0239072 | source=windows | frequency_hz=151.9 | rms=225 | updated_at=1777903509.7327106
- [2026-05-04 22:05:11] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the heat
  meta: kind=partial | timestamp=1777903511.240598 | source=windows | frequency_hz=151.9 | rms=225 | updated_at=1777903509.7327106
- [2026-05-04 22:05:12] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the heat last
  meta: kind=partial | timestamp=1777903512.1638482 | source=windows | frequency_hz=315.0 | rms=2674 | updated_at=1777903511.902679
- [2026-05-04 22:05:12] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the heat last seen
  meta: kind=partial | timestamp=1777903512.414044 | source=windows | frequency_hz=315.0 | rms=2674 | updated_at=1777903511.902679
- [2026-05-04 22:05:13] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the heat has seen a
  meta: kind=partial | timestamp=1777903513.4719157 | source=windows | frequency_hz=301.8 | rms=181 | updated_at=1777903513.0627937
- [2026-05-04 22:05:13] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the heat last seen in the
  meta: kind=partial | timestamp=1777903513.6893394 | source=windows | frequency_hz=301.8 | rms=181 | updated_at=1777903513.0627937
- [2026-05-04 22:05:14] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the heat last seen in the one
  meta: kind=partial | timestamp=1777903514.4509752 | source=windows | frequency_hz=301.8 | rms=181 | updated_at=1777903513.0627937
- [2026-05-04 22:05:15] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the heat last seen in the one that
  meta: kind=partial | timestamp=1777903515.365741 | source=windows | frequency_hz=153.3 | rms=207 | updated_at=1777903515.3627343
- [2026-05-04 22:05:15] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the heat last seen in the one now the
  meta: kind=partial | timestamp=1777903515.5771186 | source=windows | frequency_hz=136.6 | rms=261 | updated_at=1777903515.4929316
- [2026-05-04 22:05:15] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the heat last seen in the one who now heads a
  meta: kind=partial | timestamp=1777903515.9720926 | source=windows | frequency_hz=156.2 | rms=190 | updated_at=1777903515.872994
- [2026-05-04 22:05:15] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the heat last seen in the one now the single
  meta: kind=partial | timestamp=1777903515.9741116 | source=windows | frequency_hz=156.2 | rms=190 | updated_at=1777903515.872994
- [2026-05-04 22:05:16] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the heat last seen in the one who now heads of those rare
  meta: kind=partial | timestamp=1777903516.1759558 | source=windows | frequency_hz=151.0 | rms=192 | updated_at=1777903516.1335104
- [2026-05-04 22:05:16] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the heat last seen in the one now the singles gas
  meta: kind=partial | timestamp=1777903516.1781235 | source=windows | frequency_hz=151.0 | rms=192 | updated_at=1777903516.1335104
- [2026-05-04 22:05:16] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the heat last seen in the one now the singles gas and
  meta: kind=partial | timestamp=1777903516.685786 | source=windows | frequency_hz=116.0 | rms=186 | updated_at=1777903516.6427226
- [2026-05-04 22:05:16] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the heat last seen in the one now the singles gas and it's
  meta: kind=partial | timestamp=1777903516.6884105 | source=windows | frequency_hz=116.0 | rms=186 | updated_at=1777903516.6427226
- [2026-05-04 22:05:16] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the heat last seen in the one now the singles gas and since
  meta: kind=partial | timestamp=1777903516.8910599 | source=windows | frequency_hz=106.8 | rms=193 | updated_at=1777903516.772221
- [2026-05-04 22:05:17] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the heat last seen in the one now the singles gas and since the
  meta: kind=partial | timestamp=1777903517.6118686 | source=windows | frequency_hz=95.7 | rms=193 | updated_at=1777903517.5428762
- [2026-05-04 22:05:17] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the heat last seen in the one now the singles gas and its cousin
  meta: kind=partial | timestamp=1777903517.869948 | source=windows | frequency_hz=103.9 | rms=197 | updated_at=1777903517.7968922
- [2026-05-04 22:05:17] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the heat last seen in the one now the singles gas and since tesoro's
  meta: kind=partial | timestamp=1777903517.8719506 | source=windows | frequency_hz=103.9 | rms=197 | updated_at=1777903517.7968922
- [2026-05-04 22:05:17] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the heat last seen in the one now the singles gas and since tesoro's last
  meta: kind=partial | timestamp=1777903517.874955 | source=windows | frequency_hz=103.9 | rms=197 | updated_at=1777903517.7968922
- [2026-05-04 22:05:17] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the heat last seen in the one now the singles gas and since tesoro's last as
  meta: kind=partial | timestamp=1777903517.8769577 | source=windows | frequency_hz=103.9 | rms=197 | updated_at=1777903517.7968922
- [2026-05-04 22:05:18] operator / voice_transcript_partial / voice: warrior and you've seen the things that should have seen as the heat last seen in the one now the singles gas and since tesoro's last as an
  meta: kind=partial | timestamp=1777903518.2959275 | source=windows | frequency_hz=89.8 | rms=205 | updated_at=1777903518.1831036
- [2026-05-04 22:05:18] operator / voice_transcript_final / voice: warrior and you ve seen the things that should have seen as the heat last seen in the one now the singles gas and since tesoro s last as
  meta: kind=final | timestamp=1777903518.502568 | source=final | confidence=0.14 | frequency_hz=131.3 | rms=199 | updated_at=1777903518.4331698
- [2026-05-04 22:05:20] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777903520.8209827 | source=windows | frequency_hz=222.0 | rms=658 | updated_at=1777903520.2230046
- [2026-05-04 22:05:21] operator / voice_transcript_partial / voice: that the
  meta: kind=partial | timestamp=1777903521.8612874 | source=windows | frequency_hz=312.4 | rms=1333 | updated_at=1777903521.7632167
- [2026-05-04 22:05:22] operator / voice_transcript_partial / voice: that a
  meta: kind=partial | timestamp=1777903522.0639155 | source=windows | frequency_hz=322.0 | rms=386 | updated_at=1777903521.903187
- [2026-05-04 22:05:22] operator / voice_transcript_partial / voice: the third
  meta: kind=partial | timestamp=1777903522.2716658 | source=windows | frequency_hz=322.0 | rms=386 | updated_at=1777903521.903187
- [2026-05-04 22:05:23] operator / voice_transcript_partial / voice: the thought
  meta: kind=partial | timestamp=1777903523.2917342 | source=windows | frequency_hz=310.5 | rms=866 | updated_at=1777903523.043317
- [2026-05-04 22:05:23] operator / voice_transcript_partial / voice: the third thing
  meta: kind=partial | timestamp=1777903523.2917342 | source=windows | frequency_hz=310.5 | rms=866 | updated_at=1777903523.043317
- [2026-05-04 22:05:23] operator / voice_transcript_partial / voice: the thought of
  meta: kind=partial | timestamp=1777903523.5059094 | source=windows | frequency_hz=310.5 | rms=866 | updated_at=1777903523.043317
- [2026-05-04 22:05:23] operator / voice_transcript_partial / voice: that that is the
  meta: kind=partial | timestamp=1777903523.7988486 | source=windows | frequency_hz=301.6 | rms=271 | updated_at=1777903523.5533767
- [2026-05-04 22:05:24] operator / voice_transcript_partial / voice: the third thing is
  meta: kind=partial | timestamp=1777903524.2844105 | source=windows | frequency_hz=301.6 | rms=271 | updated_at=1777903523.5533767
- [2026-05-04 22:05:24] operator / voice_transcript_partial / voice: the third thing is to
  meta: kind=partial | timestamp=1777903524.4860115 | source=windows | frequency_hz=336.9 | rms=757 | updated_at=1777903524.3231466
- [2026-05-04 22:05:24] operator / voice_transcript_partial / voice: the thought of as a
  meta: kind=partial | timestamp=1777903524.9332635 | source=windows | frequency_hz=336.9 | rms=757 | updated_at=1777903524.3231466
- [2026-05-04 22:05:28] operator / voice_transcript_final / voice: the thought of as a
  meta: kind=final | timestamp=1777903528.1786811 | source=final | confidence=0.03 | frequency_hz=238.0 | rms=122 | updated_at=1777903527.2629287
- [2026-05-04 22:05:28] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777903528.179192 | source=windows | frequency_hz=238.0 | rms=122 | updated_at=1777903527.2629287
- [2026-05-04 22:05:28] operator / voice_transcript_partial / voice: part
  meta: kind=partial | timestamp=1777903528.179192 | source=windows | frequency_hz=238.0 | rms=122 | updated_at=1777903527.2629287
- [2026-05-04 22:05:28] operator / voice_transcript_partial / voice: kid who
  meta: kind=partial | timestamp=1777903528.179192 | source=windows | frequency_hz=238.0 | rms=122 | updated_at=1777903527.2629287
- [2026-05-04 22:05:28] operator / voice_transcript_partial / voice: third
  meta: kind=partial | timestamp=1777903528.179192 | source=windows | frequency_hz=238.0 | rms=122 | updated_at=1777903527.2629287
- [2026-05-04 22:05:28] operator / voice_transcript_partial / voice: third to
  meta: kind=partial | timestamp=1777903528.179192 | source=windows | frequency_hz=238.0 | rms=122 | updated_at=1777903527.2629287
- [2026-05-04 22:05:28] operator / voice_transcript_final / voice: third to
  meta: kind=final | timestamp=1777903528.179192 | source=final | confidence=0.16 | frequency_hz=238.0 | rms=122 | updated_at=1777903527.2629287
- [2026-05-04 22:05:58] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 22:06:01] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777903561.3449461 | source=windows | frequency_hz=238.0 | rms=122 | updated_at=1777903527.2629287
- [2026-05-04 22:06:01] operator / voice_transcript_final / voice: one
  meta: kind=final | timestamp=1777903561.752959 | source=final | confidence=0.1 | frequency_hz=238.0 | rms=122 | updated_at=1777903527.2629287
- [2026-05-04 22:06:03] operator / voice_transcript_partial / voice: of the
  meta: kind=partial | timestamp=1777903563.5881212 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:03] operator / voice_transcript_partial / voice: on
  meta: kind=partial | timestamp=1777903563.9955163 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:04] operator / voice_transcript_final / voice: on
  meta: kind=final | timestamp=1777903564.6895046 | source=final | confidence=0.83 | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:08] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777903568.8276587 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:09] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777903569.4380949 | source=final | confidence=0.75 | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:19] operator / voice_transcript_partial / voice: things
  meta: kind=partial | timestamp=1777903579.8702972 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:20] operator / voice_transcript_partial / voice: king's men
  meta: kind=partial | timestamp=1777903580.477754 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:20] operator / voice_transcript_partial / voice: new
  meta: kind=partial | timestamp=1777903580.6790156 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:21] operator / voice_transcript_partial / voice: menu has
  meta: kind=partial | timestamp=1777903581.0861998 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:21] operator / voice_transcript_partial / voice: menu was in
  meta: kind=partial | timestamp=1777903581.3012495 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:21] operator / voice_transcript_partial / voice: things as long as it was in
  meta: kind=partial | timestamp=1777903581.705515 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:22] operator / voice_transcript_final / voice: things as long as it was in
  meta: kind=final | timestamp=1777903582.7487562 | source=final | confidence=0.26 | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:25] operator / voice_transcript_partial / voice: my
  meta: kind=partial | timestamp=1777903585.1942372 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:25] operator / voice_transcript_partial / voice: was
  meta: kind=partial | timestamp=1777903585.3874242 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:25] operator / voice_transcript_partial / voice: what was in
  meta: kind=partial | timestamp=1777903585.5919418 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:26] operator / voice_transcript_partial / voice: one thousand one
  meta: kind=partial | timestamp=1777903586.207379 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:26] operator / voice_transcript_partial / voice: what was the one on
  meta: kind=partial | timestamp=1777903586.6135511 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:27] operator / voice_transcript_partial / voice: what was the one on one
  meta: kind=partial | timestamp=1777903587.0317328 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:27] operator / voice_transcript_partial / voice: what was going on while
  meta: kind=partial | timestamp=1777903587.2375205 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:27] operator / voice_transcript_partial / voice: what was the one on one of
  meta: kind=partial | timestamp=1777903587.4355443 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:27] operator / voice_transcript_partial / voice: what was the one on one one eight
  meta: kind=partial | timestamp=1777903587.6386662 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:28] operator / voice_transcript_partial / voice: what was the one on one one eight oh
  meta: kind=partial | timestamp=1777903588.6676095 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:29] operator / voice_transcript_final / voice: what was the one on 1180
  meta: kind=final | timestamp=1777903589.0734026 | source=final | confidence=0.21 | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:32] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777903592.3737087 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:32] operator / voice_transcript_partial / voice: was
  meta: kind=partial | timestamp=1777903592.3747103 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:32] operator / voice_transcript_partial / voice: was in the
  meta: kind=partial | timestamp=1777903592.5897264 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:32] operator / voice_transcript_partial / voice: nazi-
  meta: kind=partial | timestamp=1777903592.7973492 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:33] operator / voice_transcript_partial / voice: minus one
  meta: kind=partial | timestamp=1777903593.2283401 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:33] operator / voice_transcript_partial / voice: minus one one
  meta: kind=partial | timestamp=1777903593.6329403 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:33] operator / voice_transcript_partial / voice: last one on the
  meta: kind=partial | timestamp=1777903593.837459 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:34] operator / voice_transcript_partial / voice: was in on our behalf
  meta: kind=partial | timestamp=1777903594.0380936 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:34] operator / voice_transcript_partial / voice: minus one one yen
  meta: kind=partial | timestamp=1777903594.4518204 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:34] operator / voice_transcript_partial / voice: last one on behalf of the
  meta: kind=partial | timestamp=1777903594.6471972 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:35] operator / voice_transcript_partial / voice: last one on behalf of
  meta: kind=partial | timestamp=1777903595.0513973 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:36] operator / voice_transcript_final / voice: last one on behalf of
  meta: kind=final | timestamp=1777903596.270251 | source=final | confidence=0.11 | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:36] operator / voice_transcript_partial / voice: an
  meta: kind=partial | timestamp=1777903596.476453 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:37] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777903597.0964167 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:37] operator / voice_transcript_partial / voice: an easy
  meta: kind=partial | timestamp=1777903597.5100408 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:38] operator / voice_transcript_partial / voice: an easy one
  meta: kind=partial | timestamp=1777903598.3254197 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:39] operator / voice_transcript_partial / voice: an easy one of
  meta: kind=partial | timestamp=1777903599.078158 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:39] operator / voice_transcript_partial / voice: an easy on our
  meta: kind=partial | timestamp=1777903599.3559172 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:39] operator / voice_transcript_final / voice: an easy one of
  meta: kind=final | timestamp=1777903599.9632118 | source=final | confidence=0.24 | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:40] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777903600.2038014 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:40] operator / voice_transcript_partial / voice: these
  meta: kind=partial | timestamp=1777903600.4376526 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:40] operator / voice_transcript_partial / voice: the sea
  meta: kind=partial | timestamp=1777903600.883702 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:41] operator / voice_transcript_partial / voice: the season
  meta: kind=partial | timestamp=1777903601.1013968 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:41] operator / voice_transcript_partial / voice: the season at
  meta: kind=partial | timestamp=1777903601.5481422 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:42] operator / voice_transcript_partial / voice: the season at all
  meta: kind=partial | timestamp=1777903602.368615 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:42] operator / voice_transcript_partial / voice: the season at all on
  meta: kind=partial | timestamp=1777903602.7689154 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:43] operator / voice_transcript_final / voice: the season at all on
  meta: kind=final | timestamp=1777903603.7968197 | source=final | confidence=0.3 | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:47] operator / voice_transcript_partial / voice: it
  meta: kind=partial | timestamp=1777903607.133023 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:47] operator / voice_transcript_partial / voice: its
  meta: kind=partial | timestamp=1777903607.33875 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:47] operator / voice_transcript_partial / voice: its own
  meta: kind=partial | timestamp=1777903607.5404346 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:47] operator / voice_transcript_partial / voice: its way to
  meta: kind=partial | timestamp=1777903607.9447837 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:48] operator / voice_transcript_partial / voice: its way to see
  meta: kind=partial | timestamp=1777903608.3541846 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:48] operator / voice_transcript_partial / voice: its way to see on
  meta: kind=partial | timestamp=1777903608.771022 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:48] operator / voice_transcript_partial / voice: its way to see
  meta: kind=partial | timestamp=1777903608.9758954 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:49] operator / voice_transcript_partial / voice: its way to see on the
  meta: kind=partial | timestamp=1777903609.4290457 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:49] operator / voice_transcript_partial / voice: its way to see on the one
  meta: kind=partial | timestamp=1777903609.86166 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:50] operator / voice_transcript_final / voice: its way to see on the one
  meta: kind=final | timestamp=1777903610.4191062 | source=final | confidence=0.55 | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:50] operator / voice_transcript_partial / voice: on
  meta: kind=partial | timestamp=1777903610.725608 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:51] operator / voice_transcript_partial / voice: on which
  meta: kind=partial | timestamp=1777903611.1302056 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:51] operator / voice_transcript_partial / voice: on wednesday
  meta: kind=partial | timestamp=1777903611.3335881 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:51] operator / voice_transcript_final / voice: on wednesday
  meta: kind=final | timestamp=1777903611.9460523 | source=final | confidence=0.13 | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:57] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777903617.076479 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:57] operator / voice_transcript_partial / voice: as its
  meta: kind=partial | timestamp=1777903617.484597 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:06:58] operator / voice_transcript_final / voice: as its
  meta: kind=final | timestamp=1777903618.3377533 | source=final | confidence=0.5 | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:07:01] operator / voice_transcript_partial / voice: high
  meta: kind=partial | timestamp=1777903621.3271573 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:07:01] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777903621.527273 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:07:02] operator / voice_transcript_partial / voice: and one one one
  meta: kind=partial | timestamp=1777903622.3408668 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:07:02] operator / voice_transcript_partial / voice: and one was known as
  meta: kind=partial | timestamp=1777903622.5452106 | source=windows | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651
- [2026-05-04 22:07:04] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 22:07:05] operator / voice_transcript_final / voice: and one was known as
  meta: kind=final | timestamp=1777903625.0194674 | source=final | confidence=0.36 | frequency_hz=320.3 | rms=140 | updated_at=1777903561.8422651

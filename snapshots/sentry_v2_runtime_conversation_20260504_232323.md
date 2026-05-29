# SMART SENTRY V3.5.3 Runtime Conversation Export

- Generated: 2026-05-04 23:23:23
- Entries: 620
- Roles: {'assistant': 95, 'system': 1, 'operator': 524}
- Event types: {'assistant_prompt': 32, 'assistant_analysis': 4, 'voice_status': 1, 'voice_transcript_partial': 353, 'voice_transcript_final': 76, 'voice_command': 95, 'spoken_confirmation': 57, 'spoken_reply': 2}
- Channels: {'text': 36, 'voice': 584}
- Latest operator request: go rest
- Latest assistant message: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.
- More normalized voice commands were dispatched than final transcript events were captured. Compare transcript text against command text to catch aggressive normalization or routing drift.

## Timeline

- [2026-05-04 23:17:44] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:17:44] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-04 23:17:46] system / voice_status / voice: listening
  meta: kind=status | timestamp=1777907866.1307893 | source=vosk
- [2026-05-04 23:17:53] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777907873.381839 | source=vosk | frequency_hz=308.0 | rms=1201 | updated_at=1777907872.87547
- [2026-05-04 23:17:54] operator / voice_transcript_final / voice: do
  meta: kind=final | timestamp=1777907874.5472736 | source=final | frequency_hz=308.0 | rms=1201 | updated_at=1777907872.87547
- [2026-05-04 23:17:54] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777907874.5587106 | source=vosk | frequency_hz=308.0 | rms=1201 | updated_at=1777907872.87547
- [2026-05-04 23:17:57] operator / voice_transcript_partial / voice: task
  meta: kind=partial | timestamp=1777907877.0683758 | source=vosk | frequency_hz=308.0 | rms=1201 | updated_at=1777907872.87547
- [2026-05-04 23:17:58] operator / voice_transcript_final / voice: task
  meta: kind=final | timestamp=1777907878.0578885 | source=final | frequency_hz=308.0 | rms=1201 | updated_at=1777907872.87547
- [2026-05-04 23:18:00] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777907880.0693238 | source=vosk | frequency_hz=308.0 | rms=1201 | updated_at=1777907872.87547
- [2026-05-04 23:18:00] operator / voice_transcript_final / voice: say that
  meta: kind=final | timestamp=1777907880.5709248 | source=final | frequency_hz=308.0 | rms=1201 | updated_at=1777907872.87547
- [2026-05-04 23:18:16] operator / voice_transcript_final / voice: no
  meta: kind=final | timestamp=1777907896.071877 | source=final | frequency_hz=308.0 | rms=1201 | updated_at=1777907872.87547
- [2026-05-04 23:18:24] operator / voice_transcript_partial / voice: elliot
  meta: kind=partial | timestamp=1777907904.822131 | source=vosk | frequency_hz=308.0 | rms=1201 | updated_at=1777907872.87547
- [2026-05-04 23:18:25] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:18:25] operator / voice_transcript_partial / voice: enable smart
  meta: kind=partial | timestamp=1777907905.6915777 | source=vosk | frequency_hz=308.0 | rms=1201 | updated_at=1777907872.87547
- [2026-05-04 23:18:25] operator / voice_transcript_partial / voice: elliot what do
  meta: kind=partial | timestamp=1777907905.9382114 | source=vosk | frequency_hz=262.0 | rms=777 | updated_at=1777907905.9291904
- [2026-05-04 23:18:26] operator / voice_transcript_final / voice: what do
  meta: kind=final | timestamp=1777907906.8789322 | source=final | frequency_hz=191.3 | rms=1202 | updated_at=1777907906.178878
- [2026-05-04 23:18:26] operator / voice_command / voice: what do
  meta: normalized=True
- [2026-05-04 23:18:27] assistant / spoken_confirmation / voice: Received. I started your assistant request about what do in the background.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:18:29] operator / voice_transcript_partial / voice: repeat
  meta: kind=partial | timestamp=1777907909.8972108 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:30] operator / voice_transcript_partial / voice: repeat that
  meta: kind=partial | timestamp=1777907910.6429482 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:30] operator / voice_transcript_partial / voice: repeat it
  meta: kind=partial | timestamp=1777907910.889754 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:31] operator / voice_transcript_final / voice: repeat that
  meta: kind=final | timestamp=1777907911.4016569 | source=final | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:31] operator / voice_command / voice: repeat that
  meta: normalized=True
- [2026-05-04 23:18:31] operator / voice_command / voice: what do
  meta: normalized=True
- [2026-05-04 23:18:31] assistant / assistant_prompt / text: Assistant request queued: assistant request about what do (position 1).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:18:32] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do. I queued your assistant request about what do. It is number 1 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:18:33] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777907913.156519 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:34] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:18:44] operator / voice_transcript_partial / voice: what do
  meta: kind=partial | timestamp=1777907924.7682807 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:45] operator / voice_transcript_partial / voice: what do app to
  meta: kind=partial | timestamp=1777907925.268387 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:45] operator / voice_transcript_partial / voice: what do app to talk
  meta: kind=partial | timestamp=1777907925.5157795 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:45] operator / voice_transcript_partial / voice: what do app to
  meta: kind=partial | timestamp=1777907925.772339 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:46] operator / voice_transcript_partial / voice: what do app to smart sentry
  meta: kind=partial | timestamp=1777907926.018537 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:46] operator / voice_transcript_final / voice: what do app to talk smart
  meta: kind=final | timestamp=1777907926.902148 | source=final | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:47] operator / voice_command / voice: what do app to talk smart
  meta: normalized=True
- [2026-05-04 23:18:47] assistant / assistant_prompt / text: Assistant request queued: assistant request about what do app to talk smart (position 2).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:18:47] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do. I queued your assistant request about what do app to talk smart. It is number 2 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:18:48] operator / voice_transcript_partial / voice: yes
  meta: kind=partial | timestamp=1777907928.0745707 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:48] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777907928.5864124 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:49] operator / voice_transcript_partial / voice: override
  meta: kind=partial | timestamp=1777907929.8439074 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:50] operator / voice_transcript_partial / voice: board
  meta: kind=partial | timestamp=1777907930.083033 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:51] operator / voice_transcript_partial / voice: never mind
  meta: kind=partial | timestamp=1777907931.132396 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:51] operator / voice_transcript_partial / voice: a lion
  meta: kind=partial | timestamp=1777907931.3668869 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:51] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:18:51] operator / voice_transcript_partial / voice: a lion delay
  meta: kind=partial | timestamp=1777907931.616309 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:51] operator / voice_transcript_partial / voice: a lion do it again
  meta: kind=partial | timestamp=1777907931.8710697 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:53] operator / voice_transcript_final / voice: do it
  meta: kind=final | timestamp=1777907933.0441947 | source=final | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:53] operator / voice_command / voice: do it
  meta: normalized=True
- [2026-05-04 23:18:53] assistant / assistant_prompt / text: Assistant request queued: assistant request about do it (position 3).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:18:53] operator / voice_transcript_partial / voice: clear
  meta: kind=partial | timestamp=1777907933.0792775 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:53] operator / voice_transcript_partial / voice: the last
  meta: kind=partial | timestamp=1777907933.5665321 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:54] operator / voice_transcript_final / voice: the last
  meta: kind=final | timestamp=1777907934.300081 | source=final | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:54] operator / voice_command / voice: the last
  meta: normalized=True
- [2026-05-04 23:18:54] assistant / assistant_prompt / text: Assistant request queued: assistant request about the last (position 4).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:18:54] operator / voice_transcript_partial / voice: disconnect
  meta: kind=partial | timestamp=1777907934.8001838 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:55] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do. I queued your assistant request about do it. It is number 3 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:18:55] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do. I queued your assistant request about the last. It is number 4 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:18:55] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1777907935.6760983 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:55] operator / voice_transcript_partial / voice: rest
  meta: kind=partial | timestamp=1777907935.9406507 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:56] operator / voice_transcript_final / voice: rest
  meta: kind=final | timestamp=1777907936.43653 | source=final | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:56] operator / voice_command / voice: rest
  meta: normalized=True
- [2026-05-04 23:18:56] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777907936.9277263 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:57] operator / voice_transcript_partial / voice: it again
  meta: kind=partial | timestamp=1777907937.6854942 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:57] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777907937.9452538 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:58] operator / voice_transcript_partial / voice: never
  meta: kind=partial | timestamp=1777907938.214414 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:58] assistant / spoken_confirmation / voice: I think I heard rest. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:18:59] operator / voice_transcript_partial / voice: never to anything
  meta: kind=partial | timestamp=1777907939.035732 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:18:59] operator / voice_transcript_partial / voice: never to and current
  meta: kind=partial | timestamp=1777907939.049247 | source=vosk | frequency_hz=208.9 | rms=1203 | updated_at=1777907907.380909
- [2026-05-04 23:19:00] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777907940.7004414 | source=vosk | frequency_hz=126.0 | rms=265 | updated_at=1777907940.6874113
- [2026-05-04 23:19:01] operator / voice_transcript_partial / voice: [unk] be
  meta: kind=partial | timestamp=1777907941.0249026 | source=vosk | frequency_hz=126.0 | rms=265 | updated_at=1777907940.6874113
- [2026-05-04 23:19:01] operator / voice_transcript_partial / voice: [unk] be no
  meta: kind=partial | timestamp=1777907941.5262306 | source=vosk | frequency_hz=124.6 | rms=461 | updated_at=1777907941.2632809
- [2026-05-04 23:19:02] operator / voice_transcript_partial / voice: [unk] be no app to
  meta: kind=partial | timestamp=1777907942.0215955 | source=vosk | frequency_hz=124.6 | rms=461 | updated_at=1777907941.2632809
- [2026-05-04 23:19:02] operator / voice_transcript_partial / voice: [unk] be no app to talk
  meta: kind=partial | timestamp=1777907942.259895 | source=vosk | frequency_hz=124.6 | rms=461 | updated_at=1777907941.2632809
- [2026-05-04 23:19:02] operator / voice_transcript_partial / voice: [unk] be no app to talk it
  meta: kind=partial | timestamp=1777907942.5103962 | source=vosk | frequency_hz=124.6 | rms=461 | updated_at=1777907941.2632809
- [2026-05-04 23:19:02] operator / voice_transcript_final / voice: unk be no app to unk
  meta: kind=final | timestamp=1777907942.7630553 | source=final | frequency_hz=124.6 | rms=461 | updated_at=1777907941.2632809
- [2026-05-04 23:19:02] operator / voice_command / voice: unk be no app to unk
  meta: normalized=True
- [2026-05-04 23:19:02] assistant / assistant_prompt / text: Assistant request queued: assistant request about unk be no app to unk (position 5).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:19:03] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777907943.0151353 | source=vosk | frequency_hz=124.6 | rms=461 | updated_at=1777907941.2632809
- [2026-05-04 23:19:03] operator / voice_transcript_partial / voice: no enable
  meta: kind=partial | timestamp=1777907943.509658 | source=vosk | frequency_hz=124.6 | rms=461 | updated_at=1777907941.2632809
- [2026-05-04 23:19:03] operator / voice_transcript_partial / voice: no alien
  meta: kind=partial | timestamp=1777907943.7616317 | source=vosk | frequency_hz=380.0 | rms=280 | updated_at=1777907943.7541213
- [2026-05-04 23:19:03] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:19:04] operator / voice_transcript_final / voice: no
  meta: kind=final | timestamp=1777907944.8898761 | source=final | frequency_hz=378.6 | rms=285 | updated_at=1777907944.0031958
- [2026-05-04 23:19:05] operator / voice_command / voice: no
  meta: normalized=True
- [2026-05-04 23:19:05] assistant / assistant_prompt / text: Assistant request queued: assistant request about no (position 6).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:19:05] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do. I queued your assistant request about no. It is number 6 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:19:05] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do. I queued your assistant request about unk be no app to unk. It is number 5 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:19:09] operator / voice_transcript_partial / voice: are you
  meta: kind=partial | timestamp=1777907949.2604609 | source=vosk | frequency_hz=384.0 | rms=301 | updated_at=1777907947.2551012
- [2026-05-04 23:19:09] operator / voice_transcript_partial / voice: lion stop
  meta: kind=partial | timestamp=1777907949.5209868 | source=vosk | frequency_hz=384.0 | rms=301 | updated_at=1777907947.2551012
- [2026-05-04 23:19:09] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:19:09] operator / voice_transcript_partial / voice: lion stop enable
  meta: kind=partial | timestamp=1777907949.7705693 | source=vosk | frequency_hz=384.0 | rms=301 | updated_at=1777907947.2551012
- [2026-05-04 23:19:10] operator / voice_transcript_partial / voice: lion stop anything else
  meta: kind=partial | timestamp=1777907950.0197182 | source=vosk | frequency_hz=384.0 | rms=301 | updated_at=1777907947.2551012
- [2026-05-04 23:19:10] operator / voice_transcript_partial / voice: lion stop anything response
  meta: kind=partial | timestamp=1777907950.27324 | source=vosk | frequency_hz=384.0 | rms=301 | updated_at=1777907947.2551012
- [2026-05-04 23:19:10] operator / voice_transcript_partial / voice: lion stop check status report
  meta: kind=partial | timestamp=1777907950.521895 | source=vosk | frequency_hz=384.0 | rms=301 | updated_at=1777907947.2551012
- [2026-05-04 23:19:12] operator / voice_transcript_final / voice: check status
  meta: kind=final | timestamp=1777907952.0485399 | source=final | frequency_hz=384.0 | rms=301 | updated_at=1777907947.2551012
- [2026-05-04 23:19:12] operator / voice_command / voice: check status
  meta: normalized=True
- [2026-05-04 23:19:12] operator / voice_transcript_partial / voice: cancel
  meta: kind=partial | timestamp=1777907952.0650163 | source=vosk | frequency_hz=384.0 | rms=301 | updated_at=1777907947.2551012
- [2026-05-04 23:19:12] operator / voice_transcript_partial / voice: cancel it
  meta: kind=partial | timestamp=1777907952.078624 | source=vosk | frequency_hz=384.0 | rms=301 | updated_at=1777907947.2551012
- [2026-05-04 23:19:12] operator / voice_transcript_partial / voice: cancel that
  meta: kind=partial | timestamp=1777907952.3379376 | source=vosk | frequency_hz=230.0 | rms=368 | updated_at=1777907952.3254173
- [2026-05-04 23:19:12] operator / voice_transcript_partial / voice: cancel that a lion
  meta: kind=partial | timestamp=1777907952.6428595 | source=vosk | frequency_hz=230.0 | rms=368 | updated_at=1777907952.3254173
- [2026-05-04 23:19:13] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:19:13] operator / voice_transcript_partial / voice: cancel that a
  meta: kind=partial | timestamp=1777907953.953321 | source=vosk | frequency_hz=374.0 | rms=265 | updated_at=1777907953.9465883
- [2026-05-04 23:19:14] assistant / spoken_reply / voice: Smart Sentry is paused right now. Latest AI note. Assistant request queued: assistant request about no (position 6). End of analysys report.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-04 23:19:14] operator / voice_transcript_partial / voice: cancel that a eileen
  meta: kind=partial | timestamp=1777907954.7362678 | source=vosk | frequency_hz=374.0 | rms=265 | updated_at=1777907953.9465883
- [2026-05-04 23:19:14] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:19:16] operator / voice_transcript_final / voice: cancel that a
  meta: kind=final | timestamp=1777907956.0519617 | source=final | frequency_hz=374.0 | rms=265 | updated_at=1777907953.9465883
- [2026-05-04 23:19:16] operator / voice_command / voice: cancel that a
  meta: normalized=True
- [2026-05-04 23:19:16] assistant / assistant_prompt / text: Assistant request queued: assistant request about cancel that a (position 7).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:19:16] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do. I queued your assistant request about cancel that a. It is number 7 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:19:16] operator / voice_transcript_partial / voice: less
  meta: kind=partial | timestamp=1777907956.9533665 | source=vosk | frequency_hz=196.0 | rms=236 | updated_at=1777907956.943842
- [2026-05-04 23:19:18] operator / voice_transcript_final / voice: less
  meta: kind=final | timestamp=1777907958.3084671 | source=final | frequency_hz=196.0 | rms=236 | updated_at=1777907956.943842
- [2026-05-04 23:19:18] operator / voice_command / voice: less
  meta: normalized=True
- [2026-05-04 23:19:18] assistant / assistant_prompt / text: Assistant request queued: assistant request about less (position 8).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:19:18] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777907958.815747 | source=vosk | frequency_hz=196.0 | rms=236 | updated_at=1777907956.943842
- [2026-05-04 23:19:19] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777907959.0547671 | source=vosk | frequency_hz=196.0 | rms=236 | updated_at=1777907956.943842
- [2026-05-04 23:19:19] operator / voice_transcript_partial / voice: smart sentry a
  meta: kind=partial | timestamp=1777907959.5443957 | source=vosk | frequency_hz=196.0 | rms=236 | updated_at=1777907956.943842
- [2026-05-04 23:19:19] operator / voice_transcript_partial / voice: smart sentry it
  meta: kind=partial | timestamp=1777907959.794067 | source=vosk | frequency_hz=196.0 | rms=236 | updated_at=1777907956.943842
- [2026-05-04 23:19:20] operator / voice_transcript_partial / voice: smart sentry it pause
  meta: kind=partial | timestamp=1777907960.0495226 | source=vosk | frequency_hz=196.0 | rms=236 | updated_at=1777907956.943842
- [2026-05-04 23:19:20] operator / voice_transcript_partial / voice: smart sentry it pause brightness
  meta: kind=partial | timestamp=1777907960.2943592 | source=vosk | frequency_hz=196.0 | rms=236 | updated_at=1777907956.943842
- [2026-05-04 23:19:21] operator / voice_transcript_partial / voice: smart sentry it pause brightness lion
  meta: kind=partial | timestamp=1777907961.0440023 | source=vosk | frequency_hz=196.0 | rms=236 | updated_at=1777907956.943842
- [2026-05-04 23:19:21] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:19:21] operator / voice_transcript_partial / voice: smart sentry it pause brightness last
  meta: kind=partial | timestamp=1777907961.3022451 | source=vosk | frequency_hz=196.0 | rms=236 | updated_at=1777907956.943842
- [2026-05-04 23:19:21] operator / voice_transcript_partial / voice: smart sentry it pause brightness last a
  meta: kind=partial | timestamp=1777907961.7979226 | source=vosk | frequency_hz=196.0 | rms=236 | updated_at=1777907956.943842
- [2026-05-04 23:19:22] operator / voice_transcript_partial / voice: smart sentry it pause brightness last alion no
  meta: kind=partial | timestamp=1777907962.0439858 | source=vosk | frequency_hz=196.0 | rms=236 | updated_at=1777907956.943842
- [2026-05-04 23:19:22] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do. I queued your assistant request about less. It is number 8 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:19:23] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:19:22] operator / voice_transcript_partial / voice: smart sentry it pause brightness last alion no a
  meta: kind=partial | timestamp=1777907962.9524233 | source=vosk | frequency_hz=196.0 | rms=236 | updated_at=1777907956.943842
- [2026-05-04 23:19:23] operator / voice_transcript_partial / voice: smart sentry it pause brightness last alion no response
  meta: kind=partial | timestamp=1777907963.1994414 | source=vosk | frequency_hz=196.0 | rms=236 | updated_at=1777907956.943842
- [2026-05-04 23:19:23] operator / voice_transcript_partial / voice: smart sentry it pause brightness last alion no to the theme to
  meta: kind=partial | timestamp=1777907963.4609795 | source=vosk | frequency_hz=196.0 | rms=236 | updated_at=1777907956.943842
- [2026-05-04 23:19:24] operator / voice_transcript_final / voice: smart sentry it pause brightness last no to the theme unk
  meta: kind=final | timestamp=1777907964.2240124 | source=final | frequency_hz=212.0 | rms=1203 | updated_at=1777907964.206105
- [2026-05-04 23:19:24] operator / voice_command / voice: smart sentry it pause brightness last no to the theme unk
  meta: normalized=True
- [2026-05-04 23:19:25] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:19:25] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777907965.4675446 | source=vosk | frequency_hz=212.0 | rms=1203 | updated_at=1777907964.206105
- [2026-05-04 23:19:25] operator / voice_transcript_partial / voice: no resume
  meta: kind=partial | timestamp=1777907965.7156494 | source=vosk | frequency_hz=212.0 | rms=1203 | updated_at=1777907964.206105
- [2026-05-04 23:19:26] operator / voice_transcript_partial / voice: no resume say
  meta: kind=partial | timestamp=1777907966.220533 | source=vosk | frequency_hz=212.0 | rms=1203 | updated_at=1777907964.206105
- [2026-05-04 23:19:26] operator / voice_transcript_final / voice: no resume say it
  meta: kind=final | timestamp=1777907966.721936 | source=final | frequency_hz=212.0 | rms=1203 | updated_at=1777907964.206105
- [2026-05-04 23:19:26] operator / voice_command / voice: no resume say it
  meta: normalized=True
- [2026-05-04 23:19:26] operator / voice_transcript_partial / voice: and enable
  meta: kind=partial | timestamp=1777907966.964531 | source=vosk | frequency_hz=212.0 | rms=1203 | updated_at=1777907964.206105
- [2026-05-04 23:19:27] operator / voice_transcript_partial / voice: and app
  meta: kind=partial | timestamp=1777907967.2128003 | source=vosk | frequency_hz=212.0 | rms=1203 | updated_at=1777907964.206105
- [2026-05-04 23:19:27] operator / voice_transcript_partial / voice: and analyze the
  meta: kind=partial | timestamp=1777907967.4652152 | source=vosk | frequency_hz=212.0 | rms=1203 | updated_at=1777907964.206105
- [2026-05-04 23:19:27] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777907967.714894 | source=vosk | frequency_hz=212.0 | rms=1203 | updated_at=1777907964.206105
- [2026-05-04 23:19:27] operator / voice_transcript_partial / voice: [unk] report
  meta: kind=partial | timestamp=1777907967.9627125 | source=vosk | frequency_hz=212.0 | rms=1203 | updated_at=1777907964.206105
- [2026-05-04 23:19:28] operator / voice_transcript_partial / voice: [unk] report go
  meta: kind=partial | timestamp=1777907968.968626 | source=vosk | frequency_hz=212.0 | rms=1203 | updated_at=1777907964.206105
- [2026-05-04 23:19:29] operator / voice_transcript_final / voice: unk report
  meta: kind=final | timestamp=1777907969.4669363 | source=final | frequency_hz=212.0 | rms=1203 | updated_at=1777907964.206105
- [2026-05-04 23:19:29] operator / voice_command / voice: unk report
  meta: normalized=True
- [2026-05-04 23:19:29] assistant / assistant_analysis / text: Assistant request queued: background analysis about unk report (position 9).
  meta: task_kind=analysis | speak_requested=False
- [2026-05-04 23:19:30] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do. I queued your background analysis about unk report. It is number 9 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:19:30] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:19:30] operator / voice_transcript_partial / voice: guarding
  meta: kind=partial | timestamp=1777907970.9699688 | source=vosk | frequency_hz=212.0 | rms=1203 | updated_at=1777907964.206105
- [2026-05-04 23:19:31] operator / voice_transcript_partial / voice: guarding smart
  meta: kind=partial | timestamp=1777907971.2156618 | source=vosk | frequency_hz=212.0 | rms=1203 | updated_at=1777907964.206105
- [2026-05-04 23:19:31] operator / voice_transcript_partial / voice: guarding mode
  meta: kind=partial | timestamp=1777907971.7152343 | source=vosk | frequency_hz=212.0 | rms=1203 | updated_at=1777907964.206105
- [2026-05-04 23:19:31] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:19:32] operator / voice_transcript_partial / voice: guarding mode com
  meta: kind=partial | timestamp=1777907972.7181504 | source=vosk | frequency_hz=212.0 | rms=1203 | updated_at=1777907964.206105
- [2026-05-04 23:19:33] operator / voice_transcript_final / voice: guarding mode com
  meta: kind=final | timestamp=1777907973.4769874 | source=final | frequency_hz=212.0 | rms=1203 | updated_at=1777907964.206105
- [2026-05-04 23:19:33] operator / voice_command / voice: guarding mode com
  meta: normalized=True
- [2026-05-04 23:19:33] assistant / assistant_prompt / text: Assistant request queued: assistant request about guarding mode com (position 9).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:19:34] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do. I queued your assistant request about guarding mode com. It is number 9 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:19:34] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777907974.8875315 | source=vosk | frequency_hz=212.0 | rms=1203 | updated_at=1777907964.206105
- [2026-05-04 23:19:34] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:19:35] operator / voice_transcript_partial / voice: lion do
  meta: kind=partial | timestamp=1777907975.0984693 | source=vosk | frequency_hz=94.0 | rms=215 | updated_at=1777907975.0911677
- [2026-05-04 23:19:35] operator / voice_transcript_partial / voice: lion do the status report
  meta: kind=partial | timestamp=1777907975.9715977 | source=vosk | frequency_hz=94.0 | rms=215 | updated_at=1777907975.0911677
- [2026-05-04 23:19:37] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:19:37] operator / voice_transcript_final / voice: lion do the stop report
  meta: kind=final | timestamp=1777907977.5536847 | source=final | frequency_hz=94.0 | rms=215 | updated_at=1777907975.0911677
- [2026-05-04 23:19:37] operator / voice_command / voice: lion do the stop report
  meta: normalized=True
- [2026-05-04 23:19:37] assistant / assistant_analysis / text: Assistant request queued: background analysis about lion do the stop report (position 10).
  meta: task_kind=analysis | speak_requested=False
- [2026-05-04 23:19:38] operator / voice_transcript_partial / voice: aileen run diagnostics
  meta: kind=partial | timestamp=1777907978.2176661 | source=vosk | frequency_hz=94.0 | rms=215 | updated_at=1777907975.0911677
- [2026-05-04 23:19:38] operator / voice_transcript_partial / voice: and enable
  meta: kind=partial | timestamp=1777907978.4820602 | source=vosk | frequency_hz=94.0 | rms=215 | updated_at=1777907975.0911677
- [2026-05-04 23:19:38] operator / voice_transcript_partial / voice: aileen run diagnostics
  meta: kind=partial | timestamp=1777907978.7213418 | source=vosk | frequency_hz=94.0 | rms=215 | updated_at=1777907975.0911677
- [2026-05-04 23:19:38] operator / voice_transcript_partial / voice: aileen run diagnostics abort
  meta: kind=partial | timestamp=1777907978.967654 | source=vosk | frequency_hz=94.0 | rms=215 | updated_at=1777907975.0911677
- [2026-05-04 23:19:39] operator / voice_transcript_partial / voice: aileen run diagnostics
  meta: kind=partial | timestamp=1777907979.221281 | source=vosk | frequency_hz=94.0 | rms=215 | updated_at=1777907975.0911677
- [2026-05-04 23:19:39] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:19:39] operator / voice_transcript_partial / voice: aileen run diagnostics on commands
  meta: kind=partial | timestamp=1777907979.4667816 | source=vosk | frequency_hz=94.0 | rms=215 | updated_at=1777907975.0911677
- [2026-05-04 23:19:39] operator / voice_transcript_partial / voice: aileen run diagnostics on report
  meta: kind=partial | timestamp=1777907979.7187777 | source=vosk | frequency_hz=94.0 | rms=215 | updated_at=1777907975.0911677
- [2026-05-04 23:19:40] operator / voice_transcript_partial / voice: aileen run diagnostics on report on less
  meta: kind=partial | timestamp=1777907980.716905 | source=vosk | frequency_hz=94.0 | rms=215 | updated_at=1777907975.0911677
- [2026-05-04 23:19:40] operator / voice_transcript_partial / voice: aileen run diagnostics on report on less confidence
  meta: kind=partial | timestamp=1777907980.98023 | source=vosk | frequency_hz=94.0 | rms=215 | updated_at=1777907975.0911677
- [2026-05-04 23:19:41] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:19:42] operator / voice_transcript_final / voice: run diagnostics
  meta: kind=final | timestamp=1777907982.0283666 | source=final | frequency_hz=94.0 | rms=215 | updated_at=1777907975.0911677
- [2026-05-04 23:19:42] operator / voice_command / voice: run diagnostics
  meta: normalized=True
- [2026-05-04 23:19:42] operator / voice_transcript_partial / voice: diagnostics
  meta: kind=partial | timestamp=1777907982.0675433 | source=vosk | frequency_hz=94.0 | rms=215 | updated_at=1777907975.0911677
- [2026-05-04 23:19:42] operator / voice_transcript_partial / voice: identify yourself
  meta: kind=partial | timestamp=1777907982.5957456 | source=vosk | frequency_hz=94.0 | rms=215 | updated_at=1777907975.0911677
- [2026-05-04 23:19:43] operator / voice_transcript_partial / voice: lion decrease
  meta: kind=partial | timestamp=1777907983.095608 | source=vosk | frequency_hz=94.0 | rms=215 | updated_at=1777907975.0911677
- [2026-05-04 23:19:43] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:19:43] operator / voice_transcript_partial / voice: identify current
  meta: kind=partial | timestamp=1777907983.4614198 | source=vosk | frequency_hz=94.0 | rms=215 | updated_at=1777907975.0911677
- [2026-05-04 23:19:43] operator / voice_transcript_partial / voice: lion cancel last
  meta: kind=partial | timestamp=1777907983.59583 | source=vosk | frequency_hz=94.0 | rms=215 | updated_at=1777907975.0911677
- [2026-05-04 23:19:44] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do. I queued your background analysis about lion do the stop report. It is number 10 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:19:44] assistant / spoken_reply / voice: Smart Sentry is paused right now. Latest AI note. Assistant request queued: background analysis about lion do the stop report (position 10). End of analysys report.
  meta: interrupt=False | assistant_output=True | spoken=False
- [2026-05-04 23:19:44] operator / voice_transcript_partial / voice: lion cancel all tasks
  meta: kind=partial | timestamp=1777907984.682141 | source=vosk | frequency_hz=94.0 | rms=215 | updated_at=1777907975.0911677
- [2026-05-04 23:19:44] operator / voice_transcript_partial / voice: lion cancel all talk it
  meta: kind=partial | timestamp=1777907984.8825886 | source=vosk | frequency_hz=406.0 | rms=502 | updated_at=1777907984.8680549
- [2026-05-04 23:19:45] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:19:47] operator / voice_transcript_final / voice: identify cancel all talk it
  meta: kind=final | timestamp=1777907987.30288 | source=final | frequency_hz=406.0 | rms=502 | updated_at=1777907984.8680549
- [2026-05-04 23:19:47] operator / voice_command / voice: identify cancel all talk it
  meta: normalized=True
- [2026-05-04 23:19:48] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:19:50] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777907990.760733 | source=vosk | frequency_hz=156.0 | rms=215 | updated_at=1777907990.0343401
- [2026-05-04 23:19:51] operator / voice_transcript_partial / voice: app
  meta: kind=partial | timestamp=1777907991.518504 | source=vosk | frequency_hz=156.0 | rms=215 | updated_at=1777907990.0343401
- [2026-05-04 23:19:51] operator / voice_transcript_partial / voice: a who are
  meta: kind=partial | timestamp=1777907991.7614849 | source=vosk | frequency_hz=156.0 | rms=215 | updated_at=1777907990.0343401
- [2026-05-04 23:19:52] operator / voice_transcript_partial / voice: aileen decrease
  meta: kind=partial | timestamp=1777907992.0114427 | source=vosk | frequency_hz=156.0 | rms=215 | updated_at=1777907990.0343401
- [2026-05-04 23:19:52] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:19:52] operator / voice_transcript_partial / voice: a who the report
  meta: kind=partial | timestamp=1777907992.969859 | source=vosk | frequency_hz=156.0 | rms=215 | updated_at=1777907990.0343401
- [2026-05-04 23:19:52] operator / voice_transcript_partial / voice: a who the resume last
  meta: kind=partial | timestamp=1777907992.986396 | source=vosk | frequency_hz=156.0 | rms=215 | updated_at=1777907990.0343401
- [2026-05-04 23:19:53] operator / voice_transcript_partial / voice: a who the resume last but all
  meta: kind=partial | timestamp=1777907993.2328012 | source=vosk | frequency_hz=156.0 | rms=215 | updated_at=1777907990.0343401
- [2026-05-04 23:19:54] operator / voice_transcript_partial / voice: a who the resume last but all queued
  meta: kind=partial | timestamp=1777907994.2435284 | source=vosk | frequency_hz=364.0 | rms=1203 | updated_at=1777907993.721586
- [2026-05-04 23:19:54] operator / voice_transcript_partial / voice: a who the resume last but all queued change
  meta: kind=partial | timestamp=1777907994.4913683 | source=vosk | frequency_hz=364.0 | rms=1203 | updated_at=1777907993.721586
- [2026-05-04 23:19:54] operator / voice_transcript_partial / voice: a who the resume last but all queued change smart
  meta: kind=partial | timestamp=1777907994.9782965 | source=vosk | frequency_hz=364.0 | rms=1203 | updated_at=1777907993.721586
- [2026-05-04 23:19:55] operator / voice_transcript_partial / voice: a who the resume last but all queued change smart sentry
  meta: kind=partial | timestamp=1777907995.2271032 | source=vosk | frequency_hz=364.0 | rms=1203 | updated_at=1777907993.721586
- [2026-05-04 23:19:55] operator / voice_transcript_partial / voice: a who the resume last but all queued change smart sentry sentry
  meta: kind=partial | timestamp=1777907995.9778216 | source=vosk | frequency_hz=364.0 | rms=1203 | updated_at=1777907993.721586
- [2026-05-04 23:19:56] operator / voice_transcript_final / voice: resume guarding mode
  meta: kind=final | timestamp=1777907996.481386 | source=final | frequency_hz=336.0 | rms=335 | updated_at=1777907996.4713726
- [2026-05-04 23:19:56] operator / voice_command / voice: resume guarding mode
  meta: normalized=True
- [2026-05-04 23:19:57] assistant / spoken_confirmation / voice: Resuming guarding mode now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:19:58] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1777907998.238363 | source=vosk | frequency_hz=320.6 | rms=340 | updated_at=1777907996.7215827
- [2026-05-04 23:19:58] operator / voice_transcript_partial / voice: what do
  meta: kind=partial | timestamp=1777907998.479488 | source=vosk | frequency_hz=320.6 | rms=340 | updated_at=1777907996.7215827
- [2026-05-04 23:19:59] operator / voice_transcript_partial / voice: elian
  meta: kind=partial | timestamp=1777907999.2370358 | source=vosk | frequency_hz=320.6 | rms=340 | updated_at=1777907996.7215827
- [2026-05-04 23:19:59] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:19:59] operator / voice_transcript_partial / voice: elian resume
  meta: kind=partial | timestamp=1777907999.7341354 | source=vosk | frequency_hz=320.6 | rms=340 | updated_at=1777907996.7215827
- [2026-05-04 23:20:00] operator / voice_transcript_partial / voice: elian resume guarding
  meta: kind=partial | timestamp=1777908000.228792 | source=vosk | frequency_hz=320.6 | rms=340 | updated_at=1777907996.7215827
- [2026-05-04 23:20:00] operator / voice_transcript_partial / voice: elian resume guarding mode
  meta: kind=partial | timestamp=1777908000.4807897 | source=vosk | frequency_hz=320.6 | rms=340 | updated_at=1777907996.7215827
- [2026-05-04 23:20:01] operator / voice_transcript_partial / voice: elian resume guarding mode silence
  meta: kind=partial | timestamp=1777908001.2511616 | source=vosk | frequency_hz=320.6 | rms=340 | updated_at=1777907996.7215827
- [2026-05-04 23:20:01] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:20:01] operator / voice_transcript_final / voice: resume guarding mode
  meta: kind=final | timestamp=1777908001.480719 | source=final | frequency_hz=320.6 | rms=340 | updated_at=1777907996.7215827
- [2026-05-04 23:20:01] operator / voice_command / voice: resume guarding mode
  meta: normalized=True
- [2026-05-04 23:20:02] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:20:04] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777908004.9201882 | source=vosk | frequency_hz=335.6 | rms=335 | updated_at=1777908003.2217126
- [2026-05-04 23:20:05] operator / voice_transcript_partial / voice: standby guarding mode
  meta: kind=partial | timestamp=1777908005.4228375 | source=vosk | frequency_hz=335.6 | rms=335 | updated_at=1777908003.2217126
- [2026-05-04 23:20:05] operator / voice_transcript_partial / voice: standby guarding no
  meta: kind=partial | timestamp=1777908005.6736197 | source=vosk | frequency_hz=335.6 | rms=335 | updated_at=1777908003.2217126
- [2026-05-04 23:20:05] operator / voice_transcript_partial / voice: standby guarding no app to
  meta: kind=partial | timestamp=1777908005.918182 | source=vosk | frequency_hz=335.6 | rms=335 | updated_at=1777908003.2217126
- [2026-05-04 23:20:06] operator / voice_transcript_partial / voice: standby guarding no app to talk
  meta: kind=partial | timestamp=1777908006.4179251 | source=vosk | frequency_hz=335.6 | rms=335 | updated_at=1777908003.2217126
- [2026-05-04 23:20:06] operator / voice_transcript_partial / voice: standby guarding no app to talk it smart
  meta: kind=partial | timestamp=1777908006.6675699 | source=vosk | frequency_hz=335.6 | rms=335 | updated_at=1777908003.2217126
- [2026-05-04 23:20:06] operator / voice_transcript_final / voice: standby go it no app to unk
  meta: kind=final | timestamp=1777908006.9233973 | source=final | frequency_hz=335.6 | rms=335 | updated_at=1777908003.2217126
- [2026-05-04 23:20:07] operator / voice_command / voice: standby go it no app to unk
  meta: normalized=True
- [2026-05-04 23:20:07] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777908007.547881 | source=vosk | frequency_hz=335.6 | rms=335 | updated_at=1777908003.2217126
- [2026-05-04 23:20:08] operator / voice_transcript_final / voice: no
  meta: kind=final | timestamp=1777908008.0654354 | source=final | frequency_hz=335.6 | rms=335 | updated_at=1777908003.2217126
- [2026-05-04 23:20:08] operator / voice_command / voice: no
  meta: normalized=True
- [2026-05-04 23:20:08] assistant / assistant_prompt / text: Assistant request queued: assistant request about no (position 11).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:20:08] operator / voice_transcript_partial / voice: enable
  meta: kind=partial | timestamp=1777908008.801514 | source=vosk | frequency_hz=335.6 | rms=335 | updated_at=1777908003.2217126
- [2026-05-04 23:20:09] operator / voice_transcript_partial / voice: enable the smart
  meta: kind=partial | timestamp=1777908009.302726 | source=vosk | frequency_hz=335.6 | rms=335 | updated_at=1777908003.2217126
- [2026-05-04 23:20:09] operator / voice_transcript_partial / voice: enable the smart sentry
  meta: kind=partial | timestamp=1777908009.6318684 | source=vosk | frequency_hz=335.6 | rms=335 | updated_at=1777908003.2217126
- [2026-05-04 23:20:10] operator / voice_transcript_final / voice: enable smart sentry
  meta: kind=final | timestamp=1777908010.8056936 | source=final | frequency_hz=335.6 | rms=335 | updated_at=1777908003.2217126
- [2026-05-04 23:20:11] operator / voice_command / voice: enable smart sentry
  meta: normalized=True
- [2026-05-04 23:20:11] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777908011.2983987 | source=vosk | frequency_hz=335.6 | rms=335 | updated_at=1777908003.2217126
- [2026-05-04 23:20:11] operator / voice_transcript_partial / voice: e the
  meta: kind=partial | timestamp=1777908011.5528488 | source=vosk | frequency_hz=335.6 | rms=335 | updated_at=1777908003.2217126
- [2026-05-04 23:20:11] operator / voice_transcript_partial / voice: you do it
  meta: kind=partial | timestamp=1777908011.7988985 | source=vosk | frequency_hz=335.6 | rms=335 | updated_at=1777908003.2217126
- [2026-05-04 23:20:13] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do. I queued your assistant request about no. It is number 11 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:20:13] assistant / spoken_confirmation / voice: Going to rest position now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:20:13] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:20:13] operator / voice_transcript_final / voice: you do it
  meta: kind=final | timestamp=1777908013.4191432 | source=final | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:13] operator / voice_command / voice: you do it
  meta: normalized=True
- [2026-05-04 23:20:13] assistant / assistant_prompt / text: Assistant request queued: assistant request about you do it (position 12).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:20:13] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777908013.4321594 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:13] operator / voice_transcript_partial / voice: standby guarding
  meta: kind=partial | timestamp=1777908013.81296 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:14] operator / voice_transcript_partial / voice: standby go
  meta: kind=partial | timestamp=1777908014.3672216 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:15] operator / voice_transcript_final / voice: standby go
  meta: kind=final | timestamp=1777908015.3059394 | source=final | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:15] operator / voice_command / voice: standby go
  meta: normalized=True
- [2026-05-04 23:20:16] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777908016.1374042 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:16] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1777908016.6412027 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:17] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:20:16] operator / voice_transcript_partial / voice: e lion do
  meta: kind=partial | timestamp=1777908016.9284956 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:17] operator / voice_transcript_partial / voice: e lion stop
  meta: kind=partial | timestamp=1777908017.1426578 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:17] operator / voice_transcript_partial / voice: e lion stop e lion
  meta: kind=partial | timestamp=1777908017.391218 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:17] operator / voice_transcript_partial / voice: e lion stop e lion go
  meta: kind=partial | timestamp=1777908017.901075 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:18] operator / voice_transcript_partial / voice: e lion stop e lion decrease
  meta: kind=partial | timestamp=1777908018.138655 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:18] operator / voice_transcript_partial / voice: e lion stop e lion go rest
  meta: kind=partial | timestamp=1777908018.387057 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:18] operator / voice_transcript_partial / voice: e lion stop e lion go rest what do
  meta: kind=partial | timestamp=1777908018.6421762 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:18] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:20:19] operator / voice_transcript_partial / voice: e lion stop e lion go rest what do elian
  meta: kind=partial | timestamp=1777908019.1379602 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:19] operator / voice_transcript_partial / voice: e lion stop e lion go rest what do on commands
  meta: kind=partial | timestamp=1777908019.6391475 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:20] operator / voice_transcript_partial / voice: e lion stop e lion go rest what do com ports connect
  meta: kind=partial | timestamp=1777908020.1402535 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:20] operator / voice_transcript_final / voice: go rest
  meta: kind=final | timestamp=1777908020.4214866 | source=final | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:20] operator / voice_command / voice: go rest
  meta: normalized=True
- [2026-05-04 23:20:21] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777908021.4208472 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:21] operator / voice_transcript_partial / voice: no it again
  meta: kind=partial | timestamp=1777908021.887343 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:22] operator / voice_transcript_partial / voice: no it no
  meta: kind=partial | timestamp=1777908022.1460671 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:22] operator / voice_transcript_final / voice: no it unk
  meta: kind=final | timestamp=1777908022.3888273 | source=final | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:22] operator / voice_command / voice: no it unk
  meta: normalized=True
- [2026-05-04 23:20:22] assistant / assistant_prompt / text: Assistant request queued: assistant request about no it unk (position 13).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:20:22] operator / voice_transcript_partial / voice: never
  meta: kind=partial | timestamp=1777908022.6373723 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:23] operator / voice_transcript_partial / voice: never mind
  meta: kind=partial | timestamp=1777908023.145645 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:23] operator / voice_transcript_final / voice: never mind
  meta: kind=final | timestamp=1777908023.9026518 | source=final | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:24] operator / voice_command / voice: never mind
  meta: normalized=True
- [2026-05-04 23:20:24] assistant / assistant_prompt / text: Assistant request queued: assistant request about never mind (position 14).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:20:25] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:20:25] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do. I queued your assistant request about you do it. It is number 12 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:20:25] assistant / spoken_confirmation / voice: Going to rest position now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:20:25] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do. I queued your assistant request about no it unk. It is number 13 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:20:25] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do. I queued your assistant request about never mind. It is number 14 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:20:27] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777908027.006075 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:28] operator / voice_transcript_final / voice: standby
  meta: kind=final | timestamp=1777908028.2863894 | source=final | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:28] operator / voice_command / voice: standby
  meta: normalized=True
- [2026-05-04 23:20:28] operator / voice_transcript_partial / voice: to anything
  meta: kind=partial | timestamp=1777908028.3039222 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:28] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777908028.6751235 | source=vosk | frequency_hz=306.1 | rms=333 | updated_at=1777908012.3031516
- [2026-05-04 23:20:32] operator / voice_transcript_partial / voice: [unk] standby
  meta: kind=partial | timestamp=1777908032.817615 | source=vosk | frequency_hz=396.0 | rms=612 | updated_at=1777908030.3114438
- [2026-05-04 23:20:33] operator / voice_transcript_partial / voice: [unk] standby go
  meta: kind=partial | timestamp=1777908033.0687537 | source=vosk | frequency_hz=396.0 | rms=612 | updated_at=1777908030.3114438
- [2026-05-04 23:20:33] operator / voice_transcript_partial / voice: [unk] standby guarding
  meta: kind=partial | timestamp=1777908033.3188708 | source=vosk | frequency_hz=396.0 | rms=612 | updated_at=1777908030.3114438
- [2026-05-04 23:20:33] operator / voice_transcript_partial / voice: [unk] standby guarding mode
  meta: kind=partial | timestamp=1777908033.567609 | source=vosk | frequency_hz=396.0 | rms=612 | updated_at=1777908030.3114438
- [2026-05-04 23:20:33] operator / voice_transcript_partial / voice: [unk] standby guarding no
  meta: kind=partial | timestamp=1777908033.8288348 | source=vosk | frequency_hz=396.0 | rms=612 | updated_at=1777908030.3114438
- [2026-05-04 23:20:34] operator / voice_transcript_partial / voice: [unk] standby guarding no app to
  meta: kind=partial | timestamp=1777908034.0730171 | source=vosk | frequency_hz=396.0 | rms=612 | updated_at=1777908030.3114438
- [2026-05-04 23:20:34] operator / voice_transcript_partial / voice: [unk] standby guarding no app to talk
  meta: kind=partial | timestamp=1777908034.3175128 | source=vosk | frequency_hz=396.0 | rms=612 | updated_at=1777908030.3114438
- [2026-05-04 23:20:34] operator / voice_transcript_partial / voice: [unk] standby guarding no app to talk it smart
  meta: kind=partial | timestamp=1777908034.818249 | source=vosk | frequency_hz=396.0 | rms=612 | updated_at=1777908030.3114438
- [2026-05-04 23:20:35] operator / voice_transcript_partial / voice: [unk] standby guarding no app to talk it smart no
  meta: kind=partial | timestamp=1777908035.0702016 | source=vosk | frequency_hz=396.0 | rms=612 | updated_at=1777908030.3114438
- [2026-05-04 23:20:35] operator / voice_transcript_final / voice: unk standby go it no app to unk
  meta: kind=final | timestamp=1777908035.3233972 | source=final | frequency_hz=396.0 | rms=612 | updated_at=1777908030.3114438
- [2026-05-04 23:20:35] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777908035.8192065 | source=vosk | frequency_hz=396.0 | rms=612 | updated_at=1777908030.3114438
- [2026-05-04 23:20:36] assistant / spoken_confirmation / voice: Going to rest position now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:20:36] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:20:36] operator / voice_transcript_partial / voice: the current app
  meta: kind=partial | timestamp=1777908036.6570165 | source=vosk | frequency_hz=396.0 | rms=612 | updated_at=1777908030.3114438
- [2026-05-04 23:20:37] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:20:39] operator / voice_transcript_partial / voice: alien who are you
  meta: kind=partial | timestamp=1777908039.5751417 | source=vosk | frequency_hz=258.0 | rms=1114 | updated_at=1777908037.402543
- [2026-05-04 23:20:39] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:20:40] operator / voice_transcript_final / voice: who are you
  meta: kind=final | timestamp=1777908040.3294861 | source=final | frequency_hz=258.0 | rms=1114 | updated_at=1777908037.402543
- [2026-05-04 23:20:40] operator / voice_command / voice: who are you
  meta: normalized=True
- [2026-05-04 23:20:40] assistant / assistant_prompt / text: Assistant request queued: assistant request about who are you (position 14).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:20:41] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777908041.0516174 | source=vosk | frequency_hz=258.0 | rms=1114 | updated_at=1777908037.402543
- [2026-05-04 23:20:41] operator / voice_transcript_partial / voice: standby to
  meta: kind=partial | timestamp=1777908041.83297 | source=vosk | frequency_hz=258.0 | rms=1114 | updated_at=1777908037.402543
- [2026-05-04 23:20:42] operator / voice_transcript_partial / voice: standby no
  meta: kind=partial | timestamp=1777908042.051165 | source=vosk | frequency_hz=258.0 | rms=1114 | updated_at=1777908037.402543
- [2026-05-04 23:20:42] operator / voice_transcript_partial / voice: standby no app to
  meta: kind=partial | timestamp=1777908042.30677 | source=vosk | frequency_hz=258.0 | rms=1114 | updated_at=1777908037.402543
- [2026-05-04 23:20:42] operator / voice_transcript_partial / voice: standby no app to anything
  meta: kind=partial | timestamp=1777908042.8001776 | source=vosk | frequency_hz=258.0 | rms=1114 | updated_at=1777908037.402543
- [2026-05-04 23:20:43] operator / voice_transcript_partial / voice: standby no app to
  meta: kind=partial | timestamp=1777908043.0674047 | source=vosk | frequency_hz=258.0 | rms=1114 | updated_at=1777908037.402543
- [2026-05-04 23:20:43] operator / voice_transcript_partial / voice: standby no app to report
  meta: kind=partial | timestamp=1777908043.549401 | source=vosk | frequency_hz=258.0 | rms=1114 | updated_at=1777908037.402543
- [2026-05-04 23:20:44] operator / voice_transcript_partial / voice: standby no app to report standby
  meta: kind=partial | timestamp=1777908044.576496 | source=vosk | frequency_hz=258.0 | rms=1114 | updated_at=1777908037.402543
- [2026-05-04 23:20:44] operator / voice_transcript_partial / voice: standby no app to report standby to com
  meta: kind=partial | timestamp=1777908044.8299198 | source=vosk | frequency_hz=258.0 | rms=1114 | updated_at=1777908037.402543
- [2026-05-04 23:20:45] operator / voice_transcript_final / voice: standby no app to to report standby
  meta: kind=final | timestamp=1777908045.0855422 | source=final | frequency_hz=258.0 | rms=1114 | updated_at=1777908037.402543
- [2026-05-04 23:20:45] operator / voice_command / voice: standby no app to to report standby
  meta: normalized=True
- [2026-05-04 23:20:45] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777908045.421837 | source=vosk | frequency_hz=258.0 | rms=1114 | updated_at=1777908037.402543
- [2026-05-04 23:20:45] operator / voice_transcript_partial / voice: no app to
  meta: kind=partial | timestamp=1777908045.56749 | source=vosk | frequency_hz=258.0 | rms=1114 | updated_at=1777908037.402543
- [2026-05-04 23:20:46] operator / voice_transcript_partial / voice: no app to talk less
  meta: kind=partial | timestamp=1777908046.197309 | source=vosk | frequency_hz=258.0 | rms=1114 | updated_at=1777908037.402543
- [2026-05-04 23:20:47] operator / voice_transcript_final / voice: no app to talk
  meta: kind=final | timestamp=1777908047.3977377 | source=final | frequency_hz=258.0 | rms=1114 | updated_at=1777908037.402543
- [2026-05-04 23:20:47] operator / voice_command / voice: no app to talk
  meta: normalized=True
- [2026-05-04 23:20:47] assistant / assistant_prompt / text: Assistant request queued: assistant request about no app to talk (position 15).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:20:48] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do app to talk smart. I queued your assistant request about no app to talk. It is number 15 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:20:48] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do app to talk smart. I queued your assistant request about who are you. It is number 14 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:20:48] assistant / spoken_confirmation / voice: Going to rest position now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:20:48] operator / voice_transcript_partial / voice: home
  meta: kind=partial | timestamp=1777908048.692859 | source=vosk | frequency_hz=258.0 | rms=1114 | updated_at=1777908037.402543
- [2026-05-04 23:20:50] operator / voice_transcript_partial / voice: strict on
  meta: kind=partial | timestamp=1777908050.7896998 | source=vosk | frequency_hz=224.5 | rms=410 | updated_at=1777908050.781686
- [2026-05-04 23:20:51] operator / voice_transcript_partial / voice: same but
  meta: kind=partial | timestamp=1777908051.2940974 | source=vosk | frequency_hz=224.5 | rms=410 | updated_at=1777908050.781686
- [2026-05-04 23:20:51] operator / voice_transcript_partial / voice: same but no
  meta: kind=partial | timestamp=1777908051.5364323 | source=vosk | frequency_hz=224.5 | rms=410 | updated_at=1777908050.781686
- [2026-05-04 23:20:51] operator / voice_transcript_partial / voice: same but no app to
  meta: kind=partial | timestamp=1777908051.7874591 | source=vosk | frequency_hz=224.5 | rms=410 | updated_at=1777908050.781686
- [2026-05-04 23:20:52] operator / voice_transcript_partial / voice: same but no app to talk
  meta: kind=partial | timestamp=1777908052.0382838 | source=vosk | frequency_hz=224.5 | rms=410 | updated_at=1777908050.781686
- [2026-05-04 23:20:52] operator / voice_transcript_partial / voice: same but no app to talk elliot
  meta: kind=partial | timestamp=1777908052.2865007 | source=vosk | frequency_hz=224.5 | rms=410 | updated_at=1777908050.781686
- [2026-05-04 23:20:52] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:20:52] operator / voice_transcript_final / voice: lion same but no app to unk
  meta: kind=final | timestamp=1777908052.541415 | source=final | frequency_hz=224.5 | rms=410 | updated_at=1777908050.781686
- [2026-05-04 23:20:52] operator / voice_command / voice: lion same but no app to unk
  meta: normalized=True
- [2026-05-04 23:20:52] assistant / assistant_prompt / text: Assistant request queued: assistant request about lion same but no app to unk (position 16).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:20:53] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777908053.0372038 | source=vosk | frequency_hz=364.0 | rms=273 | updated_at=1777908053.0301855
- [2026-05-04 23:20:54] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do app to talk smart. I queued your assistant request about lion same but no app to unk. It is number 16 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:20:54] operator / voice_transcript_final / voice: no
  meta: kind=final | timestamp=1777908054.2596672 | source=final | frequency_hz=379.4 | rms=273 | updated_at=1777908053.2808685
- [2026-05-04 23:20:54] operator / voice_command / voice: no
  meta: normalized=True
- [2026-05-04 23:20:54] assistant / assistant_prompt / text: Assistant request queued: assistant request about no (position 17).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:20:55] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do app to talk smart. I queued your assistant request about no. It is number 17 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:20:59] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777908059.294787 | source=vosk | frequency_hz=86.0 | rms=1032 | updated_at=1777908055.6541097
- [2026-05-04 23:20:59] operator / voice_transcript_partial / voice: standby go
  meta: kind=partial | timestamp=1777908059.795556 | source=vosk | frequency_hz=86.0 | rms=1032 | updated_at=1777908055.6541097
- [2026-05-04 23:21:00] operator / voice_transcript_final / voice: go home
  meta: kind=final | timestamp=1777908060.9568338 | source=final | frequency_hz=316.0 | rms=469 | updated_at=1777908060.2909813
- [2026-05-04 23:21:01] operator / voice_command / voice: go home
  meta: normalized=True
- [2026-05-04 23:21:01] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777908061.5700576 | source=vosk | frequency_hz=316.0 | rms=469 | updated_at=1777908060.2909813
- [2026-05-04 23:21:01] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:21:02] operator / voice_transcript_final / voice: lion
  meta: kind=final | timestamp=1777908062.332362 | source=final | frequency_hz=316.0 | rms=469 | updated_at=1777908060.2909813
- [2026-05-04 23:21:02] operator / voice_command / voice: lion
  meta: normalized=True
- [2026-05-04 23:21:02] assistant / assistant_prompt / text: Assistant request queued: assistant request about lion (position 18).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:21:02] operator / voice_transcript_partial / voice: report
  meta: kind=partial | timestamp=1777908062.8257134 | source=vosk | frequency_hz=316.0 | rms=469 | updated_at=1777908060.2909813
- [2026-05-04 23:21:03] operator / voice_transcript_partial / voice: resume last
  meta: kind=partial | timestamp=1777908063.069885 | source=vosk | frequency_hz=316.0 | rms=469 | updated_at=1777908060.2909813
- [2026-05-04 23:21:03] operator / voice_transcript_partial / voice: resume last what do
  meta: kind=partial | timestamp=1777908063.5768461 | source=vosk | frequency_hz=316.0 | rms=469 | updated_at=1777908060.2909813
- [2026-05-04 23:21:04] operator / voice_transcript_partial / voice: resume last what do app
  meta: kind=partial | timestamp=1777908064.092039 | source=vosk | frequency_hz=316.0 | rms=469 | updated_at=1777908060.2909813
- [2026-05-04 23:21:04] operator / voice_transcript_partial / voice: resume last what do disable
  meta: kind=partial | timestamp=1777908064.3237522 | source=vosk | frequency_hz=316.0 | rms=469 | updated_at=1777908060.2909813
- [2026-05-04 23:21:04] operator / voice_transcript_partial / voice: resume last what do elliot resume
  meta: kind=partial | timestamp=1777908064.58985 | source=vosk | frequency_hz=316.0 | rms=469 | updated_at=1777908060.2909813
- [2026-05-04 23:21:05] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:21:05] operator / voice_transcript_final / voice: resume last abort what do no
  meta: kind=final | timestamp=1777908065.29063 | source=final | frequency_hz=316.0 | rms=469 | updated_at=1777908060.2909813
- [2026-05-04 23:21:05] operator / voice_command / voice: resume last abort what do no
  meta: normalized=True
- [2026-05-04 23:21:06] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:21:06] assistant / spoken_confirmation / voice: Going to guard home position now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:21:06] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do app to talk smart. I queued your assistant request about lion. It is number 18 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:21:06] operator / voice_transcript_partial / voice: never mind
  meta: kind=partial | timestamp=1777908066.444023 | source=vosk | frequency_hz=262.0 | rms=363 | updated_at=1777908065.485455
- [2026-05-04 23:21:06] operator / voice_transcript_final / voice: never mind
  meta: kind=final | timestamp=1777908066.4876227 | source=final | frequency_hz=262.0 | rms=363 | updated_at=1777908065.485455
- [2026-05-04 23:21:06] operator / voice_command / voice: never mind
  meta: normalized=True
- [2026-05-04 23:21:06] assistant / assistant_prompt / text: Assistant request queued: assistant request about never mind (position 19).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:21:06] operator / voice_transcript_partial / voice: report
  meta: kind=partial | timestamp=1777908066.957045 | source=vosk | frequency_hz=262.0 | rms=363 | updated_at=1777908065.485455
- [2026-05-04 23:21:07] operator / voice_transcript_final / voice: report
  meta: kind=final | timestamp=1777908067.6012812 | source=final | frequency_hz=262.0 | rms=363 | updated_at=1777908065.485455
- [2026-05-04 23:21:07] operator / voice_command / voice: report
  meta: normalized=True
- [2026-05-04 23:21:07] assistant / assistant_analysis / text: Assistant request queued: background analysis about report (position 20).
  meta: task_kind=analysis | speak_requested=False
- [2026-05-04 23:21:07] operator / voice_transcript_partial / voice: app
  meta: kind=partial | timestamp=1777908067.6077948 | source=vosk | frequency_hz=262.0 | rms=363 | updated_at=1777908065.485455
- [2026-05-04 23:21:07] operator / voice_transcript_partial / voice: app it again
  meta: kind=partial | timestamp=1777908067.7023032 | source=vosk | frequency_hz=262.0 | rms=363 | updated_at=1777908065.485455
- [2026-05-04 23:21:07] operator / voice_transcript_partial / voice: app it no
  meta: kind=partial | timestamp=1777908067.9536543 | source=vosk | frequency_hz=262.0 | rms=363 | updated_at=1777908065.485455
- [2026-05-04 23:21:08] operator / voice_transcript_partial / voice: app it [unk]
  meta: kind=partial | timestamp=1777908068.2036853 | source=vosk | frequency_hz=262.0 | rms=363 | updated_at=1777908065.485455
- [2026-05-04 23:21:08] operator / voice_transcript_final / voice: app it unk
  meta: kind=final | timestamp=1777908068.7222347 | source=final | frequency_hz=262.0 | rms=363 | updated_at=1777908065.485455
- [2026-05-04 23:21:08] operator / voice_command / voice: app it unk
  meta: normalized=True
- [2026-05-04 23:21:08] assistant / assistant_prompt / text: Assistant request queued: assistant request about app it unk (position 21).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:21:08] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777908068.7287478 | source=vosk | frequency_hz=262.0 | rms=363 | updated_at=1777908065.485455
- [2026-05-04 23:21:08] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777908068.955823 | source=vosk | frequency_hz=262.0 | rms=363 | updated_at=1777908065.485455
- [2026-05-04 23:21:09] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1777908069.2063425 | source=vosk | frequency_hz=262.0 | rms=363 | updated_at=1777908065.485455
- [2026-05-04 23:21:09] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:21:09] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777908069.4689376 | source=vosk | frequency_hz=262.0 | rms=363 | updated_at=1777908065.485455
- [2026-05-04 23:21:10] operator / voice_transcript_partial / voice: [unk] to the
  meta: kind=partial | timestamp=1777908070.2045193 | source=vosk | frequency_hz=262.0 | rms=363 | updated_at=1777908065.485455
- [2026-05-04 23:21:10] operator / voice_transcript_partial / voice: [unk] to the priority
  meta: kind=partial | timestamp=1777908070.4616005 | source=vosk | frequency_hz=262.0 | rms=363 | updated_at=1777908065.485455
- [2026-05-04 23:21:10] operator / voice_transcript_partial / voice: [unk] to the com override
  meta: kind=partial | timestamp=1777908070.7113993 | source=vosk | frequency_hz=262.0 | rms=363 | updated_at=1777908065.485455
- [2026-05-04 23:21:11] operator / voice_transcript_final / voice: lion go to the com override
  meta: kind=final | timestamp=1777908071.2182388 | source=final | frequency_hz=262.0 | rms=363 | updated_at=1777908065.485455
- [2026-05-04 23:21:11] operator / voice_command / voice: lion go to the com override
  meta: normalized=True
- [2026-05-04 23:21:12] assistant / spoken_confirmation / voice: Received. I started your assistant request about lion go to the com in the background.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:21:12] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do app to talk smart. I queued your assistant request about app it unk. It is number 21 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:21:12] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do app to talk smart. I queued your background analysis about report. It is number 20 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:21:12] assistant / spoken_confirmation / voice: I am still finishing assistant request about what do app to talk smart. I queued your assistant request about never mind. It is number 19 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:21:12] operator / voice_transcript_partial / voice: resume
  meta: kind=partial | timestamp=1777908072.8052425 | source=vosk | frequency_hz=262.0 | rms=363 | updated_at=1777908065.485455
- [2026-05-04 23:21:13] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777908073.5409138 | source=vosk | frequency_hz=262.0 | rms=363 | updated_at=1777908065.485455
- [2026-05-04 23:21:14] operator / voice_transcript_partial / voice: standby go
  meta: kind=partial | timestamp=1777908074.6960459 | source=vosk | frequency_hz=262.0 | rms=363 | updated_at=1777908065.485455
- [2026-05-04 23:21:15] operator / voice_transcript_final / voice: standby go
  meta: kind=final | timestamp=1777908075.9893084 | source=final | frequency_hz=248.0 | rms=388 | updated_at=1777908075.3921378
- [2026-05-04 23:21:16] operator / voice_command / voice: standby go
  meta: normalized=True
- [2026-05-04 23:21:17] assistant / spoken_confirmation / voice: Going to rest position now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:21:18] operator / voice_transcript_partial / voice: current task
  meta: kind=partial | timestamp=1777908078.6862895 | source=vosk | frequency_hz=248.0 | rms=388 | updated_at=1777908075.3921378
- [2026-05-04 23:21:18] operator / voice_transcript_partial / voice: current home
  meta: kind=partial | timestamp=1777908078.9412258 | source=vosk | frequency_hz=248.0 | rms=388 | updated_at=1777908075.3921378
- [2026-05-04 23:21:19] operator / voice_transcript_partial / voice: current home decrease
  meta: kind=partial | timestamp=1777908079.1877942 | source=vosk | frequency_hz=248.0 | rms=388 | updated_at=1777908075.3921378
- [2026-05-04 23:21:19] operator / voice_transcript_partial / voice: to disable the guarding
  meta: kind=partial | timestamp=1777908079.438584 | source=vosk | frequency_hz=248.0 | rms=388 | updated_at=1777908075.3921378
- [2026-05-04 23:21:19] operator / voice_transcript_partial / voice: to disable the go home
  meta: kind=partial | timestamp=1777908079.6937892 | source=vosk | frequency_hz=248.0 | rms=388 | updated_at=1777908075.3921378
- [2026-05-04 23:21:20] operator / voice_transcript_partial / voice: to disable the go home sensitivity
  meta: kind=partial | timestamp=1777908080.2012997 | source=vosk | frequency_hz=248.0 | rms=388 | updated_at=1777908075.3921378
- [2026-05-04 23:21:20] operator / voice_transcript_partial / voice: to disable the go home resume
  meta: kind=partial | timestamp=1777908080.4393265 | source=vosk | frequency_hz=248.0 | rms=388 | updated_at=1777908075.3921378
- [2026-05-04 23:21:21] operator / voice_transcript_final / voice: go home
  meta: kind=final | timestamp=1777908081.5031765 | source=final | frequency_hz=248.0 | rms=388 | updated_at=1777908075.3921378
- [2026-05-04 23:21:21] operator / voice_command / voice: go home
  meta: normalized=True
- [2026-05-04 23:21:21] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777908081.5091798 | source=vosk | frequency_hz=248.0 | rms=388 | updated_at=1777908075.3921378
- [2026-05-04 23:21:21] operator / voice_transcript_partial / voice: that strict
  meta: kind=partial | timestamp=1777908081.515193 | source=vosk | frequency_hz=248.0 | rms=388 | updated_at=1777908075.3921378
- [2026-05-04 23:21:21] operator / voice_transcript_partial / voice: else
  meta: kind=partial | timestamp=1777908081.7959783 | source=vosk | frequency_hz=248.0 | rms=388 | updated_at=1777908075.3921378
- [2026-05-04 23:21:22] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:21:22] operator / voice_transcript_final / voice: else
  meta: kind=final | timestamp=1777908082.6451595 | source=final | frequency_hz=248.0 | rms=388 | updated_at=1777908075.3921378
- [2026-05-04 23:21:22] operator / voice_command / voice: else
  meta: normalized=True
- [2026-05-04 23:21:22] assistant / assistant_prompt / text: Assistant request queued: assistant request about else (position 22).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:21:23] assistant / spoken_confirmation / voice: I am still finishing assistant request about lion go to the com. I queued your assistant request about else. It is number 22 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:21:26] operator / voice_transcript_partial / voice: aileen
  meta: kind=partial | timestamp=1777908086.390078 | source=vosk | frequency_hz=386.0 | rms=884 | updated_at=1777908082.6456728
- [2026-05-04 23:21:26] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:21:26] operator / voice_transcript_partial / voice: eileen current
  meta: kind=partial | timestamp=1777908086.7054002 | source=vosk | frequency_hz=386.0 | rms=884 | updated_at=1777908082.6456728
- [2026-05-04 23:21:26] operator / voice_transcript_partial / voice: eileen go rest
  meta: kind=partial | timestamp=1777908086.9307902 | source=vosk | frequency_hz=386.0 | rms=884 | updated_at=1777908082.6456728
- [2026-05-04 23:21:28] operator / voice_transcript_final / voice: go rest
  meta: kind=final | timestamp=1777908088.4388132 | source=final | frequency_hz=386.0 | rms=884 | updated_at=1777908082.6456728
- [2026-05-04 23:21:28] operator / voice_command / voice: go rest
  meta: normalized=True
- [2026-05-04 23:21:29] operator / voice_transcript_partial / voice: change
  meta: kind=partial | timestamp=1777908089.2023475 | source=vosk | frequency_hz=386.0 | rms=884 | updated_at=1777908082.6456728
- [2026-05-04 23:21:30] operator / voice_transcript_final / voice: change
  meta: kind=final | timestamp=1777908090.7008886 | source=final | frequency_hz=360.7 | rms=275 | updated_at=1777908090.673531
- [2026-05-04 23:21:31] operator / voice_command / voice: change
  meta: normalized=True
- [2026-05-04 23:21:31] assistant / assistant_prompt / text: Assistant request queued: assistant request about change (position 23).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:21:31] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777908091.539067 | source=vosk | frequency_hz=360.7 | rms=275 | updated_at=1777908090.673531
- [2026-05-04 23:21:31] operator / voice_transcript_partial / voice: standby guarding
  meta: kind=partial | timestamp=1777908091.7809706 | source=vosk | frequency_hz=360.7 | rms=275 | updated_at=1777908090.673531
- [2026-05-04 23:21:32] operator / voice_transcript_partial / voice: standby current
  meta: kind=partial | timestamp=1777908092.030068 | source=vosk | frequency_hz=360.7 | rms=275 | updated_at=1777908090.673531
- [2026-05-04 23:21:32] operator / voice_transcript_partial / voice: standby current no
  meta: kind=partial | timestamp=1777908092.529807 | source=vosk | frequency_hz=360.7 | rms=275 | updated_at=1777908090.673531
- [2026-05-04 23:21:32] operator / voice_transcript_partial / voice: standby current no app to
  meta: kind=partial | timestamp=1777908092.7821043 | source=vosk | frequency_hz=360.7 | rms=275 | updated_at=1777908090.673531
- [2026-05-04 23:21:33] operator / voice_transcript_partial / voice: standby current no app to talk
  meta: kind=partial | timestamp=1777908093.0376308 | source=vosk | frequency_hz=360.7 | rms=275 | updated_at=1777908090.673531
- [2026-05-04 23:21:33] operator / voice_transcript_partial / voice: standby current no app to talk it smart
  meta: kind=partial | timestamp=1777908093.5402277 | source=vosk | frequency_hz=360.7 | rms=275 | updated_at=1777908090.673531
- [2026-05-04 23:21:33] operator / voice_transcript_final / voice: standby current no app to unk
  meta: kind=final | timestamp=1777908093.8054788 | source=final | frequency_hz=360.7 | rms=275 | updated_at=1777908090.673531
- [2026-05-04 23:21:34] operator / voice_command / voice: standby current no app to unk
  meta: normalized=True
- [2026-05-04 23:21:35] assistant / spoken_confirmation / voice: Going to rest position now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:21:35] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:21:35] assistant / spoken_confirmation / voice: I am still finishing assistant request about lion go to the com. I queued your assistant request about change. It is number 23 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:21:35] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777908095.2895713 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:35] operator / voice_transcript_partial / voice: standby go
  meta: kind=partial | timestamp=1777908095.5730345 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:35] operator / voice_transcript_partial / voice: standby go it
  meta: kind=partial | timestamp=1777908095.8052583 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:36] operator / voice_transcript_partial / voice: standby go it no
  meta: kind=partial | timestamp=1777908096.044998 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:36] operator / voice_transcript_partial / voice: standby go it no talk
  meta: kind=partial | timestamp=1777908096.5412297 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:36] operator / voice_transcript_partial / voice: standby go it no to anything
  meta: kind=partial | timestamp=1777908096.7923975 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:37] operator / voice_transcript_partial / voice: standby go it no talk it are you
  meta: kind=partial | timestamp=1777908097.0929248 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:37] operator / voice_transcript_partial / voice: standby go it no to anything else
  meta: kind=partial | timestamp=1777908097.3035374 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:38] operator / voice_transcript_final / voice: standby go it no talk it are you
  meta: kind=final | timestamp=1777908098.2980607 | source=final | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:38] operator / voice_command / voice: standby go it no talk it are you
  meta: normalized=True
- [2026-05-04 23:21:39] assistant / spoken_confirmation / voice: Going to rest position now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:21:40] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777908100.3653092 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:40] operator / voice_transcript_partial / voice: standby go
  meta: kind=partial | timestamp=1777908100.6163704 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:40] operator / voice_transcript_partial / voice: standby go sentry
  meta: kind=partial | timestamp=1777908100.8636193 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:41] operator / voice_transcript_partial / voice: standby go no
  meta: kind=partial | timestamp=1777908101.1097708 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:41] operator / voice_transcript_partial / voice: standby go no app to
  meta: kind=partial | timestamp=1777908101.6152558 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:41] operator / voice_transcript_partial / voice: standby go no app to talk
  meta: kind=partial | timestamp=1777908101.8694794 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:42] operator / voice_transcript_final / voice: standby go no unk
  meta: kind=final | timestamp=1777908102.1293015 | source=final | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:42] operator / voice_command / voice: standby go no unk
  meta: normalized=True
- [2026-05-04 23:21:42] operator / voice_transcript_partial / voice: never
  meta: kind=partial | timestamp=1777908102.4555364 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:43] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777908103.159465 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:43] operator / voice_transcript_final / voice: no
  meta: kind=final | timestamp=1777908103.9214923 | source=final | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:44] operator / voice_transcript_partial / voice: standby
  meta: kind=partial | timestamp=1777908104.4246747 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:44] operator / voice_transcript_partial / voice: standby guarding
  meta: kind=partial | timestamp=1777908104.9565475 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:45] operator / voice_transcript_partial / voice: standby go ahead
  meta: kind=partial | timestamp=1777908105.3169103 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:46] operator / voice_transcript_partial / voice: standby go ahead no
  meta: kind=partial | timestamp=1777908106.1297302 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:46] operator / voice_transcript_final / voice: standby go it no
  meta: kind=final | timestamp=1777908106.4370854 | source=final | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:47] assistant / spoken_confirmation / voice: Going to rest position now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:21:48] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777908108.52285 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:48] operator / voice_transcript_partial / voice: tracking priority
  meta: kind=partial | timestamp=1777908108.909529 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:49] operator / voice_transcript_partial / voice: tracking port
  meta: kind=partial | timestamp=1777908109.2715065 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:50] operator / voice_transcript_final / voice: tracking port
  meta: kind=final | timestamp=1777908110.0807571 | source=final | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:50] operator / voice_transcript_partial / voice: board
  meta: kind=partial | timestamp=1777908110.0927749 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:50] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777908110.3374689 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:51] operator / voice_transcript_partial / voice: go home
  meta: kind=partial | timestamp=1777908111.0872939 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:51] operator / voice_transcript_partial / voice: go resume
  meta: kind=partial | timestamp=1777908111.338497 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:51] operator / voice_transcript_final / voice: go home
  meta: kind=final | timestamp=1777908111.8418472 | source=final | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:54] operator / voice_transcript_partial / voice: port
  meta: kind=partial | timestamp=1777908114.8437145 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:55] operator / voice_transcript_final / voice: port
  meta: kind=final | timestamp=1777908115.6787353 | source=final | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:55] operator / voice_transcript_partial / voice: are you
  meta: kind=partial | timestamp=1777908115.837698 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:59] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777908119.7019358 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:21:59] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777908119.9496768 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:22:01] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777908121.4674752 | source=final | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:22:01] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777908121.704841 | source=vosk | frequency_hz=368.0 | rms=270 | updated_at=1777908094.315569
- [2026-05-04 23:22:02] operator / voice_transcript_final / voice: that no
  meta: kind=final | timestamp=1777908122.4555333 | source=final | frequency_hz=316.0 | rms=274 | updated_at=1777908122.1935515
- [2026-05-04 23:22:03] operator / voice_transcript_partial / voice: you do
  meta: kind=partial | timestamp=1777908123.2013352 | source=vosk | frequency_hz=316.0 | rms=274 | updated_at=1777908122.1935515
- [2026-05-04 23:22:03] operator / voice_transcript_partial / voice: talk less
  meta: kind=partial | timestamp=1777908123.9510963 | source=vosk | frequency_hz=316.0 | rms=274 | updated_at=1777908122.1935515
- [2026-05-04 23:22:04] operator / voice_transcript_partial / voice: to com port
  meta: kind=partial | timestamp=1777908124.20511 | source=vosk | frequency_hz=316.0 | rms=274 | updated_at=1777908122.1935515
- [2026-05-04 23:22:04] operator / voice_transcript_final / voice: to com port
  meta: kind=final | timestamp=1777908124.7150784 | source=final | frequency_hz=316.0 | rms=274 | updated_at=1777908122.1935515
- [2026-05-04 23:22:09] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777908129.2007942 | source=vosk | frequency_hz=316.0 | rms=274 | updated_at=1777908122.1935515
- [2026-05-04 23:22:10] operator / voice_transcript_final / voice: do
  meta: kind=final | timestamp=1777908130.4051974 | source=final | frequency_hz=316.0 | rms=274 | updated_at=1777908122.1935515
- [2026-05-04 23:22:10] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777908130.921149 | source=vosk | frequency_hz=316.0 | rms=274 | updated_at=1777908122.1935515
- [2026-05-04 23:22:11] operator / voice_transcript_final / voice: go
  meta: kind=final | timestamp=1777908131.664836 | source=final | frequency_hz=316.0 | rms=274 | updated_at=1777908122.1935515
- [2026-05-04 23:22:13] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777908133.0499551 | source=vosk | frequency_hz=316.0 | rms=274 | updated_at=1777908122.1935515
- [2026-05-04 23:22:13] operator / voice_transcript_partial / voice: the guarding
  meta: kind=partial | timestamp=1777908133.547754 | source=vosk | frequency_hz=316.0 | rms=274 | updated_at=1777908122.1935515
- [2026-05-04 23:22:13] operator / voice_transcript_partial / voice: the go
  meta: kind=partial | timestamp=1777908133.7878082 | source=vosk | frequency_hz=316.0 | rms=274 | updated_at=1777908122.1935515
- [2026-05-04 23:22:14] operator / voice_transcript_final / voice: the guarding mode
  meta: kind=final | timestamp=1777908134.1578405 | source=final | frequency_hz=316.0 | rms=274 | updated_at=1777908122.1935515
- [2026-05-04 23:22:14] operator / voice_transcript_partial / voice: abort
  meta: kind=partial | timestamp=1777908134.2974994 | source=vosk | frequency_hz=316.0 | rms=274 | updated_at=1777908122.1935515
- [2026-05-04 23:22:14] operator / voice_transcript_partial / voice: elian
  meta: kind=partial | timestamp=1777908134.53872 | source=vosk | frequency_hz=316.0 | rms=274 | updated_at=1777908122.1935515
- [2026-05-04 23:22:14] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:22:14] operator / voice_transcript_partial / voice: on commands
  meta: kind=partial | timestamp=1777908134.7919865 | source=vosk | frequency_hz=316.0 | rms=274 | updated_at=1777908122.1935515
- [2026-05-04 23:22:15] operator / voice_transcript_partial / voice: elian
  meta: kind=partial | timestamp=1777908135.2876434 | source=vosk | frequency_hz=316.0 | rms=274 | updated_at=1777908122.1935515
- [2026-05-04 23:22:15] operator / voice_transcript_final / voice: no
  meta: kind=final | timestamp=1777908135.557317 | source=final | frequency_hz=316.0 | rms=274 | updated_at=1777908122.1935515
- [2026-05-04 23:22:15] operator / voice_command / voice: no
  meta: normalized=True
- [2026-05-04 23:22:15] assistant / assistant_prompt / text: Assistant request queued: assistant request about no (position 24).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:22:15] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777908135.7933521 | source=vosk | frequency_hz=316.0 | rms=274 | updated_at=1777908122.1935515
- [2026-05-04 23:22:16] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:22:17] assistant / spoken_confirmation / voice: I am still finishing assistant request about lion go to the com. I queued your assistant request about no. It is number 24 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:22:17] operator / voice_transcript_partial / voice: resume
  meta: kind=partial | timestamp=1777908137.0414758 | source=vosk | frequency_hz=376.0 | rms=302 | updated_at=1777908136.0306828
- [2026-05-04 23:22:17] operator / voice_transcript_partial / voice: response delay
  meta: kind=partial | timestamp=1777908137.3223886 | source=vosk | frequency_hz=376.0 | rms=302 | updated_at=1777908136.0306828
- [2026-05-04 23:22:17] operator / voice_transcript_partial / voice: enable
  meta: kind=partial | timestamp=1777908137.5663557 | source=vosk | frequency_hz=376.0 | rms=302 | updated_at=1777908136.0306828
- [2026-05-04 23:22:18] operator / voice_transcript_final / voice: enable
  meta: kind=final | timestamp=1777908138.801868 | source=final | frequency_hz=376.0 | rms=302 | updated_at=1777908136.0306828
- [2026-05-04 23:22:18] operator / voice_command / voice: enable
  meta: normalized=True
- [2026-05-04 23:22:19] assistant / spoken_confirmation / voice: I think I heard enable. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:22:23] operator / voice_transcript_partial / voice: be more strict
  meta: kind=partial | timestamp=1777908143.0136771 | source=vosk | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:23] operator / voice_transcript_partial / voice: boards lion
  meta: kind=partial | timestamp=1777908143.253551 | source=vosk | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:23] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:22:23] operator / voice_transcript_partial / voice: boards lion go to
  meta: kind=partial | timestamp=1777908143.502613 | source=vosk | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:24] operator / voice_transcript_partial / voice: boards lion go to the
  meta: kind=partial | timestamp=1777908144.125792 | source=vosk | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:24] operator / voice_transcript_partial / voice: boards lion go to the current
  meta: kind=partial | timestamp=1777908144.1341891 | source=vosk | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:24] operator / voice_transcript_partial / voice: boards lion go to the com
  meta: kind=partial | timestamp=1777908144.38053 | source=vosk | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:25] operator / voice_transcript_partial / voice: boards lion go to the com do tracking
  meta: kind=partial | timestamp=1777908145.2584763 | source=vosk | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:25] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:22:25] operator / voice_transcript_partial / voice: boards lion go to the com do to resume
  meta: kind=partial | timestamp=1777908145.3838243 | source=vosk | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:25] operator / voice_transcript_partial / voice: boards lion go to the com do to response delay
  meta: kind=partial | timestamp=1777908145.6393964 | source=vosk | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:25] operator / voice_transcript_partial / voice: boards lion go to the com do to resume last
  meta: kind=partial | timestamp=1777908145.8948565 | source=vosk | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:26] operator / voice_transcript_partial / voice: boards lion go to the com do to resume last aileen override
  meta: kind=partial | timestamp=1777908146.6248684 | source=vosk | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:26] operator / voice_transcript_partial / voice: boards lion go to the com do to resume last alien
  meta: kind=partial | timestamp=1777908146.8766854 | source=vosk | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:27] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:22:27] operator / voice_transcript_partial / voice: boards lion go to the com do to resume last alien never to anything
  meta: kind=partial | timestamp=1777908147.6333685 | source=vosk | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:28] operator / voice_transcript_partial / voice: boards lion go to the com do to resume last alien never connect boards
  meta: kind=partial | timestamp=1777908148.1266646 | source=vosk | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:28] operator / voice_transcript_partial / voice: boards lion go to the com do to resume last alien never connect board lion
  meta: kind=partial | timestamp=1777908148.477096 | source=vosk | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:29] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:22:29] operator / voice_transcript_final / voice: connect boards
  meta: kind=final | timestamp=1777908149.936512 | source=final | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:30] operator / voice_command / voice: connect boards
  meta: normalized=True
- [2026-05-04 23:22:31] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:22:31] operator / voice_transcript_partial / voice: and enable
  meta: kind=partial | timestamp=1777908151.8859546 | source=vosk | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:32] operator / voice_transcript_partial / voice: and to com
  meta: kind=partial | timestamp=1777908152.1342742 | source=vosk | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:32] operator / voice_transcript_partial / voice: and to com no
  meta: kind=partial | timestamp=1777908152.6535401 | source=vosk | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:33] operator / voice_transcript_partial / voice: and to com no talk
  meta: kind=partial | timestamp=1777908153.3886008 | source=vosk | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:33] operator / voice_transcript_final / voice: and to com no unk
  meta: kind=final | timestamp=1777908153.6349962 | source=final | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:33] operator / voice_command / voice: and to com no unk
  meta: normalized=True
- [2026-05-04 23:22:33] assistant / assistant_prompt / text: Assistant request queued: assistant request about and to com no unk (position 24).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:22:33] operator / voice_transcript_partial / voice: brightness
  meta: kind=partial | timestamp=1777908153.90871 | source=vosk | frequency_hz=403.4 | rms=267 | updated_at=1777908139.991615
- [2026-05-04 23:22:34] operator / voice_transcript_final / voice: no
  meta: kind=final | timestamp=1777908154.6406398 | source=final | frequency_hz=320.4 | rms=331 | updated_at=1777908154.6266177
- [2026-05-04 23:22:34] operator / voice_command / voice: no
  meta: normalized=True
- [2026-05-04 23:22:34] assistant / assistant_prompt / text: Assistant request queued: assistant request about no (position 25).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:22:35] assistant / spoken_confirmation / voice: I am still finishing assistant request about do it. I queued your assistant request about and to com no unk. It is number 24 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:22:35] assistant / spoken_confirmation / voice: I am still finishing assistant request about do it. I queued your assistant request about no. It is number 25 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:22:38] operator / voice_transcript_partial / voice: board
  meta: kind=partial | timestamp=1777908158.6704185 | source=vosk | frequency_hz=307.5 | rms=244 | updated_at=1777908156.6428282
- [2026-05-04 23:22:38] operator / voice_transcript_partial / voice: board home
  meta: kind=partial | timestamp=1777908158.9046166 | source=vosk | frequency_hz=307.5 | rms=244 | updated_at=1777908156.6428282
- [2026-05-04 23:22:39] operator / voice_transcript_partial / voice: board home the smart
  meta: kind=partial | timestamp=1777908159.1621819 | source=vosk | frequency_hz=307.5 | rms=244 | updated_at=1777908156.6428282
- [2026-05-04 23:22:39] operator / voice_transcript_partial / voice: board home resume
  meta: kind=partial | timestamp=1777908159.4039063 | source=vosk | frequency_hz=260.0 | rms=337 | updated_at=1777908159.397695
- [2026-05-04 23:22:40] operator / voice_transcript_partial / voice: board home resume lion
  meta: kind=partial | timestamp=1777908160.152144 | source=vosk | frequency_hz=260.0 | rms=337 | updated_at=1777908159.397695
- [2026-05-04 23:22:40] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:22:40] operator / voice_transcript_partial / voice: board home resume lion status
  meta: kind=partial | timestamp=1777908160.4651392 | source=vosk | frequency_hz=260.0 | rms=337 | updated_at=1777908159.397695
- [2026-05-04 23:22:40] operator / voice_transcript_partial / voice: board home resume lion stop
  meta: kind=partial | timestamp=1777908160.6947296 | source=vosk | frequency_hz=260.0 | rms=337 | updated_at=1777908159.397695
- [2026-05-04 23:22:40] operator / voice_transcript_partial / voice: board home resume lion to anything else
  meta: kind=partial | timestamp=1777908160.9622195 | source=vosk | frequency_hz=260.0 | rms=337 | updated_at=1777908159.397695
- [2026-05-04 23:22:41] operator / voice_transcript_partial / voice: board home resume lion to anything a serial
  meta: kind=partial | timestamp=1777908161.1567776 | source=vosk | frequency_hz=260.0 | rms=337 | updated_at=1777908159.397695
- [2026-05-04 23:22:42] operator / voice_transcript_partial / voice: board home resume lion to anything a sensitivity
  meta: kind=partial | timestamp=1777908162.0216787 | source=vosk | frequency_hz=260.0 | rms=337 | updated_at=1777908159.397695
- [2026-05-04 23:22:42] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:22:42] operator / voice_transcript_partial / voice: board home resume lion to anything a theme to com
  meta: kind=partial | timestamp=1777908162.030702 | source=vosk | frequency_hz=260.0 | rms=337 | updated_at=1777908159.397695
- [2026-05-04 23:22:42] operator / voice_transcript_partial / voice: board home resume lion to anything a faster current app
  meta: kind=partial | timestamp=1777908162.2194474 | source=vosk | frequency_hz=260.0 | rms=337 | updated_at=1777908159.397695
- [2026-05-04 23:22:43] operator / voice_transcript_final / voice: board home resume lion to anything a faster report
  meta: kind=final | timestamp=1777908163.151459 | source=final | frequency_hz=260.0 | rms=337 | updated_at=1777908159.397695
- [2026-05-04 23:22:43] operator / voice_command / voice: board home resume lion to anything a faster report
  meta: normalized=True
- [2026-05-04 23:22:43] operator / voice_transcript_partial / voice: increase
  meta: kind=partial | timestamp=1777908163.1657715 | source=vosk | frequency_hz=260.0 | rms=337 | updated_at=1777908159.397695
- [2026-05-04 23:22:43] operator / voice_transcript_partial / voice: in queue
  meta: kind=partial | timestamp=1777908163.33712 | source=vosk | frequency_hz=300.0 | rms=430 | updated_at=1777908163.3300557
- [2026-05-04 23:22:43] operator / voice_transcript_partial / voice: queued tasks
  meta: kind=partial | timestamp=1777908163.5869656 | source=vosk | frequency_hz=300.0 | rms=430 | updated_at=1777908163.3300557
- [2026-05-04 23:22:44] operator / voice_transcript_partial / voice: queued rest
  meta: kind=partial | timestamp=1777908164.2927904 | source=vosk | frequency_hz=300.0 | rms=430 | updated_at=1777908163.3300557
- [2026-05-04 23:22:44] operator / voice_transcript_partial / voice: queued last abort
  meta: kind=partial | timestamp=1777908164.365016 | source=vosk | frequency_hz=300.0 | rms=430 | updated_at=1777908163.3300557
- [2026-05-04 23:22:44] operator / voice_transcript_partial / voice: queued last app to anything
  meta: kind=partial | timestamp=1777908164.589644 | source=vosk | frequency_hz=300.0 | rms=430 | updated_at=1777908163.3300557
- [2026-05-04 23:22:44] operator / voice_transcript_partial / voice: queued last app to com
  meta: kind=partial | timestamp=1777908164.8454452 | source=vosk | frequency_hz=300.0 | rms=430 | updated_at=1777908163.3300557
- [2026-05-04 23:22:45] operator / voice_transcript_partial / voice: queued last app to com no
  meta: kind=partial | timestamp=1777908165.3518045 | source=vosk | frequency_hz=300.0 | rms=430 | updated_at=1777908163.3300557
- [2026-05-04 23:22:45] operator / voice_transcript_partial / voice: queued last app to com no on commands
  meta: kind=partial | timestamp=1777908165.6089494 | source=vosk | frequency_hz=264.0 | rms=333 | updated_at=1777908165.5792804
- [2026-05-04 23:22:45] operator / voice_transcript_partial / voice: queued last app to com no app
  meta: kind=partial | timestamp=1777908165.8412666 | source=vosk | frequency_hz=264.0 | rms=333 | updated_at=1777908165.5792804
- [2026-05-04 23:22:46] operator / voice_transcript_partial / voice: queued last app to com no app it
  meta: kind=partial | timestamp=1777908166.339722 | source=vosk | frequency_hz=264.0 | rms=333 | updated_at=1777908165.5792804
- [2026-05-04 23:22:46] operator / voice_transcript_partial / voice: queued last app to com no app it [unk]
  meta: kind=partial | timestamp=1777908166.6009786 | source=vosk | frequency_hz=264.0 | rms=333 | updated_at=1777908165.5792804
- [2026-05-04 23:22:46] operator / voice_transcript_final / voice: a queue last app to com no app it unk
  meta: kind=final | timestamp=1777908166.8565853 | source=final | frequency_hz=264.0 | rms=333 | updated_at=1777908165.5792804
- [2026-05-04 23:22:47] operator / voice_command / voice: a queue last app to com no app it unk
  meta: normalized=True
- [2026-05-04 23:22:47] assistant / assistant_prompt / text: Assistant request queued: assistant request about a queue last app to com no app it unk (position 26).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:22:47] operator / voice_transcript_partial / voice: boards
  meta: kind=partial | timestamp=1777908167.355503 | source=vosk | frequency_hz=264.0 | rms=333 | updated_at=1777908165.5792804
- [2026-05-04 23:22:47] operator / voice_transcript_partial / voice: board lion
  meta: kind=partial | timestamp=1777908167.5867763 | source=vosk | frequency_hz=296.0 | rms=319 | updated_at=1777908167.5807662
- [2026-05-04 23:22:47] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 23:22:49] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:22:48] operator / voice_transcript_final / voice: board lion
  meta: kind=final | timestamp=1777908168.343098 | source=final | frequency_hz=298.6 | rms=324 | updated_at=1777908168.330517
- [2026-05-04 23:22:50] operator / voice_command / voice: board lion
  meta: normalized=True
- [2026-05-04 23:22:50] assistant / assistant_prompt / text: Assistant request queued: assistant request about board lion (position 27).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 23:22:51] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777908171.3501987 | source=vosk | frequency_hz=342.7 | rms=336 | updated_at=1777908170.5811973
- [2026-05-04 23:22:51] operator / voice_transcript_partial / voice: tracking priority
  meta: kind=partial | timestamp=1777908171.5913877 | source=vosk | frequency_hz=342.7 | rms=336 | updated_at=1777908170.5811973
- [2026-05-04 23:22:51] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777908171.8370192 | source=vosk | frequency_hz=342.7 | rms=336 | updated_at=1777908170.5811973
- [2026-05-04 23:22:52] operator / voice_transcript_partial / voice: tracking pause
  meta: kind=partial | timestamp=1777908172.1113312 | source=vosk | frequency_hz=342.7 | rms=336 | updated_at=1777908170.5811973
- [2026-05-04 23:22:52] operator / voice_transcript_partial / voice: tracking pause current
  meta: kind=partial | timestamp=1777908172.6873527 | source=vosk | frequency_hz=342.7 | rms=336 | updated_at=1777908170.5811973
- [2026-05-04 23:22:52] operator / voice_transcript_final / voice: tracking pause unk
  meta: kind=final | timestamp=1777908172.9044704 | source=final | frequency_hz=342.7 | rms=336 | updated_at=1777908170.5811973
- [2026-05-04 23:22:53] operator / voice_command / voice: tracking pause unk
  meta: normalized=True
- [2026-05-04 23:22:53] operator / voice_transcript_partial / voice: boards
  meta: kind=partial | timestamp=1777908173.1049511 | source=vosk | frequency_hz=342.7 | rms=336 | updated_at=1777908170.5811973
- [2026-05-04 23:22:53] operator / voice_transcript_partial / voice: board increase
  meta: kind=partial | timestamp=1777908173.3357675 | source=vosk | frequency_hz=342.7 | rms=336 | updated_at=1777908170.5811973
- [2026-05-04 23:22:53] operator / voice_transcript_partial / voice: boards and guarding
  meta: kind=partial | timestamp=1777908173.5869162 | source=vosk | frequency_hz=342.7 | rms=336 | updated_at=1777908170.5811973
- [2026-05-04 23:22:53] operator / voice_transcript_partial / voice: boards and go home
  meta: kind=partial | timestamp=1777908173.8403032 | source=vosk | frequency_hz=342.7 | rms=336 | updated_at=1777908170.5811973
- [2026-05-04 23:22:54] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777908174.0969477 | source=vosk | frequency_hz=342.7 | rms=336 | updated_at=1777908170.5811973
- [2026-05-04 23:22:55] operator / voice_transcript_partial / voice: [unk] standby
  meta: kind=partial | timestamp=1777908175.1629145 | source=vosk | frequency_hz=342.7 | rms=336 | updated_at=1777908170.5811973
- [2026-05-04 23:22:56] assistant / spoken_confirmation / voice: I am still finishing assistant request about do it. I queued your assistant request about board lion. It is number 27 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:22:56] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:22:56] assistant / spoken_confirmation / voice: I am still finishing assistant request about do it. I queued your assistant request about a queue last app to com no app it unk. It is number 26 in line.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 23:22:55] operator / voice_transcript_partial / voice: [unk] standby current
  meta: kind=partial | timestamp=1777908175.5862029 | source=vosk | frequency_hz=342.7 | rms=336 | updated_at=1777908170.5811973
- [2026-05-04 23:22:55] operator / voice_transcript_partial / voice: [unk] standby current no
  meta: kind=partial | timestamp=1777908175.8377576 | source=vosk | frequency_hz=342.7 | rms=336 | updated_at=1777908170.5811973
- [2026-05-04 23:22:56] operator / voice_transcript_partial / voice: [unk] standby current no app to
  meta: kind=partial | timestamp=1777908176.3387465 | source=vosk | frequency_hz=342.7 | rms=336 | updated_at=1777908170.5811973
- [2026-05-04 23:22:56] operator / voice_transcript_partial / voice: [unk] standby current no app to talk
  meta: kind=partial | timestamp=1777908176.6380703 | source=vosk | frequency_hz=342.7 | rms=336 | updated_at=1777908170.5811973
- [2026-05-04 23:22:56] operator / voice_transcript_partial / voice: [unk] standby current no app to talk it
  meta: kind=partial | timestamp=1777908176.8366354 | source=vosk | frequency_hz=342.7 | rms=336 | updated_at=1777908170.5811973
- [2026-05-04 23:22:57] operator / voice_transcript_partial / voice: [unk] standby current no app to talk it smart
  meta: kind=partial | timestamp=1777908177.1003492 | source=vosk | frequency_hz=342.7 | rms=336 | updated_at=1777908170.5811973
- [2026-05-04 23:22:57] operator / voice_transcript_partial / voice: [unk] standby current no app to talk it brightness
  meta: kind=partial | timestamp=1777908177.3368373 | source=vosk | frequency_hz=372.0 | rms=324 | updated_at=1777908177.3298159
- [2026-05-04 23:22:57] operator / voice_transcript_partial / voice: [unk] standby current no app to talk it smart no
  meta: kind=partial | timestamp=1777908177.58617 | source=vosk | frequency_hz=331.4 | rms=308 | updated_at=1777908177.5801165
- [2026-05-04 23:22:58] operator / voice_transcript_final / voice: unk standby current no app to talk it smart no
  meta: kind=final | timestamp=1777908178.0893598 | source=final | frequency_hz=298.5 | rms=314 | updated_at=1777908178.079849
- [2026-05-04 23:22:58] operator / voice_command / voice: unk standby current no app to talk it smart no
  meta: normalized=True
- [2026-05-04 23:22:59] assistant / spoken_confirmation / voice: Going to rest position now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 23:23:02] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777908182.1072962 | source=vosk | frequency_hz=345.4 | rms=310 | updated_at=1777908180.5814745
- [2026-05-04 23:23:02] operator / voice_transcript_partial / voice: go rest
  meta: kind=partial | timestamp=1777908182.6084492 | source=vosk | frequency_hz=345.4 | rms=310 | updated_at=1777908180.5814745
- [2026-05-04 23:23:03] operator / voice_transcript_partial / voice: go rest resume
  meta: kind=partial | timestamp=1777908183.1068563 | source=vosk | frequency_hz=345.4 | rms=310 | updated_at=1777908180.5814745
- [2026-05-04 23:23:03] operator / voice_transcript_partial / voice: go rest resume diagnostics
  meta: kind=partial | timestamp=1777908183.3832052 | source=vosk | frequency_hz=345.4 | rms=310 | updated_at=1777908180.5814745
- [2026-05-04 23:23:03] operator / voice_transcript_partial / voice: go rest resume
  meta: kind=partial | timestamp=1777908183.64827 | source=vosk | frequency_hz=345.4 | rms=310 | updated_at=1777908180.5814745
- [2026-05-04 23:23:04] operator / voice_transcript_final / voice: go rest
  meta: kind=final | timestamp=1777908184.1071916 | source=final | frequency_hz=345.4 | rms=310 | updated_at=1777908180.5814745
- [2026-05-04 23:23:22] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False

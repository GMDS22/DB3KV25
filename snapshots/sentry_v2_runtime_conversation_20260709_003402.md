# SMART SENTRY V5.0.0 Runtime Conversation Export

- Generated: 2026-07-09 00:34:02
- Entries: 160
- Roles: {'assistant': 4, 'system': 122, 'operator': 34}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 122, 'spoken_confirmation': 2, 'voice_transcript_partial': 28, 'voice_transcript_final': 5, 'voice_command': 1}
- Channels: {'text': 2, 'voice': 158}
- Latest operator request: elion tell me what you can see from the camera
- Latest assistant message: Running Smart Sentry now. Connecting the Smart Sentry boards first.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-07-09 00:29:08] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-07-09 00:29:08] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-07-09 00:29:14] system / voice_status / voice: listening
  meta: kind=status | timestamp=1783528154.0893984 | source=vosk
- [2026-07-09 00:29:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528155.8473866 | source=vosk | rms=932 | updated_at=1783528155.8473866
- [2026-07-09 00:29:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528157.2206962 | source=vosk | rms=985 | updated_at=1783528156.1908944
- [2026-07-09 00:29:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528159.0634925 | source=vosk | rms=985 | updated_at=1783528156.1908944
- [2026-07-09 00:29:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528159.8135834 | source=vosk | rms=139 | updated_at=1783528159.3131247
- [2026-07-09 00:29:58] assistant / spoken_confirmation / voice: Smart Sentry is ready.
  meta: interrupt=True | assistant_output=False | spoken=True
- [2026-07-09 00:29:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528170.5648549 | source=vosk | rms=162 | updated_at=1783528170.5648549
- [2026-07-09 00:29:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528171.0631013 | source=vosk | rms=162 | updated_at=1783528170.5648549
- [2026-07-09 00:29:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528183.3139827 | source=vosk | rms=147 | updated_at=1783528183.3139827
- [2026-07-09 00:29:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528183.813159 | source=vosk | rms=147 | updated_at=1783528183.3139827
- [2026-07-09 00:29:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528185.5632198 | source=vosk | rms=128 | updated_at=1783528185.5632198
- [2026-07-09 00:29:46] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528186.0632656 | source=vosk | rms=128 | updated_at=1783528185.5632198
- [2026-07-09 00:30:02] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528202.0640655 | source=vosk | rms=367 | updated_at=1783528202.0640655 | frequency_hz=222.0
- [2026-07-09 00:30:03] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1783528203.386667 | source=vosk | rms=1201 | updated_at=1783528203.3248487 | frequency_hz=222.0
- [2026-07-09 00:30:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528203.573661 | source=vosk | rms=1204 | updated_at=1783528203.573661 | frequency_hz=222.0
- [2026-07-09 00:30:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528203.8245604 | source=vosk | rms=1202 | updated_at=1783528203.8245604 | frequency_hz=222.0
- [2026-07-09 00:30:03] operator / voice_transcript_partial / voice: smart century
  meta: kind=partial | timestamp=1783528203.9023557 | source=vosk | rms=1202 | updated_at=1783528203.8245604 | frequency_hz=222.0
- [2026-07-09 00:30:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528204.0754497 | source=vosk | rms=216 | updated_at=1783528204.0754497 | frequency_hz=222.0
- [2026-07-09 00:30:04] operator / voice_transcript_partial / voice: smart century is ready
  meta: kind=partial | timestamp=1783528204.1632762 | source=vosk | rms=216 | updated_at=1783528204.0754497 | frequency_hz=222.0
- [2026-07-09 00:30:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528204.3239076 | source=vosk | rms=190 | updated_at=1783528204.3239076 | frequency_hz=222.0
- [2026-07-09 00:30:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528204.5737784 | source=vosk | rms=601 | updated_at=1783528204.5737784 | frequency_hz=222.0
- [2026-07-09 00:30:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528204.824445 | source=vosk | rms=679 | updated_at=1783528204.824445 | frequency_hz=222.0
- [2026-07-09 00:30:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528205.075301 | source=vosk | rms=295 | updated_at=1783528205.075301 | frequency_hz=222.0
- [2026-07-09 00:30:06] operator / voice_transcript_final / voice: smart sentry is ready
  meta: kind=final | timestamp=1783528206.0176933 | source=final | rms=295 | updated_at=1783528205.075301 | frequency_hz=222.0
- [2026-07-09 00:30:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528206.1480317 | source=vosk | rms=295 | updated_at=1783528205.075301 | frequency_hz=222.0
- [2026-07-09 00:30:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528206.1480317 | source=vosk | rms=999 | updated_at=1783528206.1480317 | frequency_hz=222.0
- [2026-07-09 00:30:10] operator / voice_transcript_partial / voice: ilya
  meta: kind=partial | timestamp=1783528210.6201334 | source=vosk | rms=5114 | updated_at=1783528210.5770304 | frequency_hz=314.7
- [2026-07-09 00:30:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528210.8254712 | source=vosk | rms=9282 | updated_at=1783528210.8254712 | frequency_hz=314.7
- [2026-07-09 00:30:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528211.0762177 | source=vosk | rms=6216 | updated_at=1783528211.0762177 | frequency_hz=314.7
- [2026-07-09 00:30:11] operator / voice_transcript_partial / voice: ill you run the
  meta: kind=partial | timestamp=1783528211.1022584 | source=vosk | rms=6216 | updated_at=1783528211.0762177 | frequency_hz=314.7
- [2026-07-09 00:30:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528211.3243895 | source=vosk | rms=4323 | updated_at=1783528211.3243895 | frequency_hz=314.7
- [2026-07-09 00:30:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528211.5740979 | source=vosk | rms=4571 | updated_at=1783528211.5740979 | frequency_hz=314.7
- [2026-07-09 00:30:11] operator / voice_transcript_partial / voice: ill you run the smart
  meta: kind=partial | timestamp=1783528211.5920994 | source=vosk | rms=4571 | updated_at=1783528211.5740979 | frequency_hz=314.7
- [2026-07-09 00:30:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528211.823789 | source=vosk | rms=1966 | updated_at=1783528211.823789 | frequency_hz=269.7
- [2026-07-09 00:30:11] operator / voice_transcript_partial / voice: ill you run the smart century
  meta: kind=partial | timestamp=1783528211.8598876 | source=vosk | rms=1966 | updated_at=1783528211.823789 | frequency_hz=269.7
- [2026-07-09 00:30:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528212.0753994 | source=vosk | rms=1349 | updated_at=1783528212.0753994 | frequency_hz=257.2
- [2026-07-09 00:30:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528212.324396 | source=vosk | rms=1203 | updated_at=1783528212.324396 | frequency_hz=257.2
- [2026-07-09 00:30:12] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1783528212.352013 | source=final | rms=1203 | updated_at=1783528212.324396 | frequency_hz=257.2
- [2026-07-09 00:30:12] system / voice_status / voice: processing
  meta: kind=status | timestamp=1783528212.3954308 | source=state | rms=1203 | updated_at=1783528212.324396 | frequency_hz=257.2
- [2026-07-09 00:30:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528212.3954308 | source=state | rms=1203 | updated_at=1783528212.324396 | frequency_hz=257.2
- [2026-07-09 00:30:12] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-07-09 00:30:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528212.5743275 | source=vosk | rms=1201 | updated_at=1783528212.5743275 | frequency_hz=257.2
- [2026-07-09 00:30:12] assistant / spoken_confirmation / voice: Running Smart Sentry now. Connecting the Smart Sentry boards first.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-07-09 00:30:15] operator / voice_transcript_partial / voice: running
  meta: kind=partial | timestamp=1783528215.437638 | source=vosk | rms=856 | updated_at=1783528214.9739702 | frequency_hz=240.0
- [2026-07-09 00:30:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528215.437638 | source=vosk | rms=856 | updated_at=1783528214.9739702 | frequency_hz=240.0
- [2026-07-09 00:30:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528215.437638 | source=vosk | rms=890 | updated_at=1783528215.437638 | frequency_hz=240.0
- [2026-07-09 00:30:15] operator / voice_transcript_partial / voice: running smart
  meta: kind=partial | timestamp=1783528215.5144265 | source=vosk | rms=785 | updated_at=1783528215.4772398 | frequency_hz=240.0
- [2026-07-09 00:30:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528215.7249553 | source=vosk | rms=529 | updated_at=1783528215.7249553 | frequency_hz=240.0
- [2026-07-09 00:30:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528216.2244682 | source=vosk | rms=243 | updated_at=1783528216.2244682 | frequency_hz=240.0
- [2026-07-09 00:30:16] operator / voice_transcript_partial / voice: running smart century
  meta: kind=partial | timestamp=1783528216.2439919 | source=vosk | rms=243 | updated_at=1783528216.2244682 | frequency_hz=240.0
- [2026-07-09 00:30:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528216.478198 | source=vosk | rms=1206 | updated_at=1783528216.478198 | frequency_hz=240.0
- [2026-07-09 00:30:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528216.7256317 | source=vosk | rms=863 | updated_at=1783528216.7256317 | frequency_hz=240.0
- [2026-07-09 00:30:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528216.9778588 | source=vosk | rms=981 | updated_at=1783528216.9778588 | frequency_hz=240.0
- [2026-07-09 00:30:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528217.2246716 | source=vosk | rms=957 | updated_at=1783528217.2246716 | frequency_hz=240.0
- [2026-07-09 00:30:17] operator / voice_transcript_partial / voice: running smart century connecting the
  meta: kind=partial | timestamp=1783528217.2462363 | source=vosk | rms=957 | updated_at=1783528217.2246716 | frequency_hz=240.0
- [2026-07-09 00:30:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528217.8555846 | source=vosk | rms=746 | updated_at=1783528217.8555846 | frequency_hz=240.0
- [2026-07-09 00:30:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528218.1065822 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:18] operator / voice_transcript_partial / voice: running smart century connecting the smart such as
  meta: kind=partial | timestamp=1783528218.2103076 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528218.856122 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528219.1096673 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528219.6058686 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:20] operator / voice_transcript_final / voice: running smart sentry connecting the smart such as
  meta: kind=final | timestamp=1783528220.723655 | source=final | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528220.8814929 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:20] operator / voice_transcript_partial / voice: running smart century connecting the smart such as
  meta: kind=partial | timestamp=1783528220.911375 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528221.108788 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:21] operator / voice_transcript_partial / voice: running smart century connecting the smart such as smart
  meta: kind=partial | timestamp=1783528221.1360078 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528221.3566575 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528221.8590496 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528223.1074834 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528223.356692 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:23] operator / voice_transcript_partial / voice: running smart century connecting the smart such as smart saturday
  meta: kind=partial | timestamp=1783528223.371732 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528223.8558707 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528224.606471 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:24] operator / voice_transcript_partial / voice: running smart century connecting the smart such as smart saturday oh
  meta: kind=partial | timestamp=1783528224.637507 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528225.1072512 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528226.35987 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:26] operator / voice_transcript_partial / voice: running smart century connecting the smart such as smart saturday
  meta: kind=partial | timestamp=1783528226.3958108 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528226.8596876 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528228.6063342 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:28] operator / voice_transcript_partial / voice: running smart century connecting the smart such as smart saturday of arts and
  meta: kind=partial | timestamp=1783528228.6264353 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528228.8561566 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528229.106419 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:29] operator / voice_transcript_partial / voice: running smart century connecting the smart such as smart saturday oh arts
  meta: kind=partial | timestamp=1783528229.1199589 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528229.3577697 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:30] operator / voice_transcript_final / voice: running smart sentry connecting the smart such as smart saturday oh arts
  meta: kind=final | timestamp=1783528230.148495 | source=final | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528230.2850485 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528230.2850485 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528230.8563597 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528232.3564487 | source=vosk | rms=606 | updated_at=1783528218.1065822 | frequency_hz=240.0
- [2026-07-09 00:30:34] operator / voice_transcript_partial / voice: but it
  meta: kind=partial | timestamp=1783528234.1537597 | source=vosk | rms=10893 | updated_at=1783528234.1069875 | frequency_hz=348.6
- [2026-07-09 00:30:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528234.356882 | source=vosk | rms=3601 | updated_at=1783528234.356882 | frequency_hz=302.9
- [2026-07-09 00:30:34] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1783528234.4030838 | source=vosk | rms=3601 | updated_at=1783528234.356882 | frequency_hz=302.9
- [2026-07-09 00:30:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528234.6061375 | source=vosk | rms=3601 | updated_at=1783528234.356882 | frequency_hz=302.9
- [2026-07-09 00:30:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528234.8574255 | source=vosk | rms=11615 | updated_at=1783528234.8574255 | frequency_hz=302.9
- [2026-07-09 00:30:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528235.1064456 | source=vosk | rms=11160 | updated_at=1783528235.1064456 | frequency_hz=343.2
- [2026-07-09 00:30:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528235.3561594 | source=vosk | rms=8345 | updated_at=1783528235.3561594 | frequency_hz=343.2
- [2026-07-09 00:30:35] operator / voice_transcript_partial / voice: alien tell me
  meta: kind=partial | timestamp=1783528235.4767036 | source=vosk | rms=8345 | updated_at=1783528235.3561594 | frequency_hz=343.2
- [2026-07-09 00:30:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528235.612056 | source=vosk | rms=6888 | updated_at=1783528235.612056 | frequency_hz=343.2
- [2026-07-09 00:30:35] operator / voice_transcript_partial / voice: alien tell me what you
  meta: kind=partial | timestamp=1783528235.6506286 | source=vosk | rms=6888 | updated_at=1783528235.612056 | frequency_hz=343.2
- [2026-07-09 00:30:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528235.8561873 | source=vosk | rms=6610 | updated_at=1783528235.8561873 | frequency_hz=343.2
- [2026-07-09 00:30:35] operator / voice_transcript_partial / voice: alien tell me what you can
  meta: kind=partial | timestamp=1783528235.8797286 | source=vosk | rms=6610 | updated_at=1783528235.8561873 | frequency_hz=343.2
- [2026-07-09 00:30:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528236.1070166 | source=vosk | rms=4107 | updated_at=1783528236.1070166 | frequency_hz=343.2
- [2026-07-09 00:30:36] operator / voice_transcript_partial / voice: alien tell me what you can see from
  meta: kind=partial | timestamp=1783528236.1286848 | source=vosk | rms=4107 | updated_at=1783528236.1070166 | frequency_hz=343.2
- [2026-07-09 00:30:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528236.3579028 | source=vosk | rms=6857 | updated_at=1783528236.3579028 | frequency_hz=343.2
- [2026-07-09 00:30:36] operator / voice_transcript_partial / voice: alien tell me what you can see from the
  meta: kind=partial | timestamp=1783528236.4003615 | source=vosk | rms=6857 | updated_at=1783528236.3579028 | frequency_hz=343.2
- [2026-07-09 00:30:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528236.6063564 | source=vosk | rms=3306 | updated_at=1783528236.6063564 | frequency_hz=344.9
- [2026-07-09 00:30:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528236.8567708 | source=vosk | rms=1443 | updated_at=1783528236.8567708 | frequency_hz=291.4
- [2026-07-09 00:30:36] operator / voice_transcript_partial / voice: alien tell me what you can see from the camera
  meta: kind=partial | timestamp=1783528236.8732955 | source=vosk | rms=1443 | updated_at=1783528236.8567708 | frequency_hz=291.4
- [2026-07-09 00:30:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528237.108539 | source=vosk | rms=1443 | updated_at=1783528236.8567708 | frequency_hz=291.4
- [2026-07-09 00:30:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528237.356965 | source=vosk | rms=1443 | updated_at=1783528236.8567708 | frequency_hz=291.4
- [2026-07-09 00:30:37] operator / voice_transcript_final / voice: elion tell me what you can see from the camera
  meta: kind=final | timestamp=1783528237.9593544 | source=final | rms=1443 | updated_at=1783528236.8567708 | frequency_hz=291.4
- [2026-07-09 00:30:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528238.0682442 | source=state | rms=1443 | updated_at=1783528236.8567708 | frequency_hz=291.4
- [2026-07-09 00:30:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528238.0682442 | source=vosk | rms=1443 | updated_at=1783528236.8567708 | frequency_hz=291.4
- [2026-07-09 00:30:41] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528241.867458 | source=vosk | rms=2271 | updated_at=1783528238.356729 | frequency_hz=291.4
- [2026-07-09 00:31:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528261.1298492 | source=vosk | rms=2271 | updated_at=1783528238.356729 | frequency_hz=291.4
- [2026-07-09 00:31:01] operator / voice_transcript_partial / voice: if
  meta: kind=partial | timestamp=1783528261.393762 | source=vosk | rms=2271 | updated_at=1783528238.356729 | frequency_hz=291.4
- [2026-07-09 00:31:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528261.626652 | source=vosk | rms=3452 | updated_at=1783528261.626652 | frequency_hz=291.4
- [2026-07-09 00:31:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528264.8806736 | source=vosk | rms=7708 | updated_at=1783528264.1302445 | frequency_hz=244.6
- [2026-07-09 00:31:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528269.6879094 | source=vosk | rms=7708 | updated_at=1783528264.1302445 | frequency_hz=244.6
- [2026-07-09 00:31:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528270.1877413 | source=vosk | rms=7708 | updated_at=1783528264.1302445 | frequency_hz=244.6
- [2026-07-09 00:31:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528301.6870997 | source=vosk | rms=205 | updated_at=1783528301.6870997 | frequency_hz=244.6
- [2026-07-09 00:31:42] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528302.939857 | source=vosk | rms=197 | updated_at=1783528301.9426594 | frequency_hz=244.6
- [2026-07-09 00:31:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528303.6878197 | source=vosk | rms=2607 | updated_at=1783528303.6878197 | frequency_hz=410.0
- [2026-07-09 00:31:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528311.8672552 | source=vosk | rms=121 | updated_at=1783528309.36794 | frequency_hz=319.6
- [2026-07-09 00:31:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528316.6173482 | source=vosk | rms=873 | updated_at=1783528316.6173482 | frequency_hz=319.6
- [2026-07-09 00:31:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528317.3679285 | source=vosk | rms=157 | updated_at=1783528316.8684962 | frequency_hz=319.6
- [2026-07-09 00:31:58] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528318.8677137 | source=vosk | rms=157 | updated_at=1783528316.8684962 | frequency_hz=319.6
- [2026-07-09 00:31:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528319.618034 | source=vosk | rms=123 | updated_at=1783528319.117713 | frequency_hz=192.0
- [2026-07-09 00:32:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528333.6171136 | source=vosk | rms=201 | updated_at=1783528333.6171136 | frequency_hz=192.0
- [2026-07-09 00:32:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528335.1182942 | source=vosk | rms=255 | updated_at=1783528334.3678331 | frequency_hz=169.6
- [2026-07-09 00:32:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528342.8686864 | source=vosk | rms=1012 | updated_at=1783528342.8686864 | frequency_hz=169.6
- [2026-07-09 00:32:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528345.8694577 | source=vosk | rms=130 | updated_at=1783528345.1211793 | frequency_hz=116.5
- [2026-07-09 00:32:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528346.1176054 | source=vosk | rms=130 | updated_at=1783528345.1211793 | frequency_hz=116.5
- [2026-07-09 00:32:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528346.8681784 | source=vosk | rms=130 | updated_at=1783528345.1211793 | frequency_hz=116.5
- [2026-07-09 00:32:27] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528347.367808 | source=vosk | rms=130 | updated_at=1783528345.1211793 | frequency_hz=116.5
- [2026-07-09 00:32:27] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528347.8677537 | source=vosk | rms=130 | updated_at=1783528345.1211793 | frequency_hz=116.5
- [2026-07-09 00:32:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528359.618755 | source=vosk | rms=237 | updated_at=1783528359.618755 | frequency_hz=116.5
- [2026-07-09 00:32:47] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528367.1178727 | source=vosk | rms=120 | updated_at=1783528363.8693898 | frequency_hz=78.4
- [2026-07-09 00:32:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528372.3688684 | source=vosk | rms=486 | updated_at=1783528372.3688684 | frequency_hz=100.0
- [2026-07-09 00:33:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528386.758617 | source=vosk | rms=224 | updated_at=1783528383.5083506 | frequency_hz=141.5
- [2026-07-09 00:33:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528389.7591689 | source=vosk | rms=550 | updated_at=1783528389.7591689 | frequency_hz=141.5
- [2026-07-09 00:33:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528390.5090058 | source=vosk | rms=549 | updated_at=1783528390.0085392 | frequency_hz=141.5
- [2026-07-09 00:33:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528390.7632174 | source=vosk | rms=549 | updated_at=1783528390.0085392 | frequency_hz=141.5
- [2026-07-09 00:33:17] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528397.259075 | source=vosk | rms=240 | updated_at=1783528396.7587378 | frequency_hz=81.1
- [2026-07-09 00:33:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528399.7580469 | source=vosk | rms=383 | updated_at=1783528399.7580469 | frequency_hz=81.1
- [2026-07-09 00:33:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528400.5085511 | source=vosk | rms=401 | updated_at=1783528400.008453 | frequency_hz=81.1
- [2026-07-09 00:33:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528409.5094032 | source=vosk | rms=163 | updated_at=1783528409.5094032 | frequency_hz=120.0
- [2026-07-09 00:33:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528433.509296 | source=vosk | rms=613 | updated_at=1783528432.5090828 | frequency_hz=181.6
- [2026-07-09 00:33:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528434.0088992 | source=vosk | rms=613 | updated_at=1783528432.5090828 | frequency_hz=181.6
- [2026-07-09 00:33:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528434.7594564 | source=vosk | rms=613 | updated_at=1783528432.5090828 | frequency_hz=181.6
- [2026-07-09 00:33:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528435.0108547 | source=vosk | rms=613 | updated_at=1783528432.5090828 | frequency_hz=181.6
- [2026-07-09 00:33:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528436.4570343 | source=vosk | rms=613 | updated_at=1783528432.5090828 | frequency_hz=181.6
- [2026-07-09 00:33:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528436.7010822 | source=vosk | rms=613 | updated_at=1783528432.5090828 | frequency_hz=181.6
- [2026-07-09 00:33:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528437.1996713 | source=vosk | rms=613 | updated_at=1783528432.5090828 | frequency_hz=181.6
- [2026-07-09 00:33:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528437.9496841 | source=vosk | rms=613 | updated_at=1783528432.5090828 | frequency_hz=181.6
- [2026-07-09 00:34:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528440.1997476 | source=vosk | rms=613 | updated_at=1783528432.5090828 | frequency_hz=181.6
- [2026-07-09 00:34:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783528440.4497728 | source=vosk | rms=613 | updated_at=1783528432.5090828 | frequency_hz=181.6
- [2026-07-09 00:34:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783528440.9497871 | source=vosk | rms=613 | updated_at=1783528432.5090828 | frequency_hz=181.6

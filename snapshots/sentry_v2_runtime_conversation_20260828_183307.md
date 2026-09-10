# SMART SENTRY V5.0.0 Runtime Conversation Export

- Generated: 2026-08-28 18:33:07
- Entries: 201
- Roles: {'assistant': 7, 'system': 141, 'operator': 53}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 141, 'voice_transcript_partial': 39, 'voice_transcript_final': 10, 'spoken_confirmation': 5, 'voice_command': 4}
- Channels: {'text': 2, 'voice': 199}
- Latest operator request: something down our camera
- Latest assistant message: Listening window closed. Smart Sentry is not actively guarding right now.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-08-28 18:31:14] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-08-28 18:31:14] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-08-28 18:31:19] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787913079.1805317 | source=vosk
- [2026-08-28 18:31:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913079.7111654 | source=vosk | rms=1200 | updated_at=1787913079.7111654
- [2026-08-28 18:31:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913080.9423647 | source=vosk | rms=1200 | updated_at=1787913079.7111654
- [2026-08-28 18:31:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913080.9433637 | source=vosk | rms=1200 | updated_at=1787913080.9433637
- [2026-08-28 18:31:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913091.2714927 | source=vosk | rms=555 | updated_at=1787913090.7716842 | frequency_hz=175.2
- [2026-08-28 18:31:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913091.5220542 | source=vosk | rms=1201 | updated_at=1787913091.5220542 | frequency_hz=180.4
- [2026-08-28 18:31:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913093.020921 | source=vosk | rms=141 | updated_at=1787913092.2710083 | frequency_hz=180.4
- [2026-08-28 18:31:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913093.2712193 | source=vosk | rms=141 | updated_at=1787913092.2710083 | frequency_hz=180.4
- [2026-08-28 18:31:34] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1787913094.3974535 | source=vosk | rms=1200 | updated_at=1787913094.271426 | frequency_hz=218.1
- [2026-08-28 18:31:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913094.5224876 | source=vosk | rms=1202 | updated_at=1787913094.5214193 | frequency_hz=254.5
- [2026-08-28 18:31:34] operator / voice_transcript_partial / voice: that would
  meta: kind=partial | timestamp=1787913094.6136477 | source=vosk | rms=1202 | updated_at=1787913094.5214193 | frequency_hz=254.5
- [2026-08-28 18:31:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913094.7717755 | source=vosk | rms=1203 | updated_at=1787913094.7717755 | frequency_hz=219.3
- [2026-08-28 18:31:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913095.021475 | source=vosk | rms=1958 | updated_at=1787913095.021475 | frequency_hz=204.8
- [2026-08-28 18:31:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913095.271454 | source=vosk | rms=1137 | updated_at=1787913095.271454 | frequency_hz=204.8
- [2026-08-28 18:31:35] operator / voice_transcript_final / voice: that with
  meta: kind=final | timestamp=1787913095.4784184 | source=final | rms=1137 | updated_at=1787913095.271454 | frequency_hz=204.8
- [2026-08-28 18:31:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913095.5736744 | source=vosk | rms=1200 | updated_at=1787913095.5736744 | frequency_hz=204.8
- [2026-08-28 18:31:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913099.5217006 | source=vosk | rms=1202 | updated_at=1787913099.0213854 | frequency_hz=236.3
- [2026-08-28 18:32:15] assistant / spoken_confirmation / voice: Smart Sentry is ready.
  meta: interrupt=True | assistant_output=False | spoken=True
- [2026-08-28 18:31:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913100.0212371 | source=vosk | rms=1069 | updated_at=1787913100.0212371 | frequency_hz=240.4
- [2026-08-28 18:31:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913100.7707758 | source=vosk | rms=1069 | updated_at=1787913100.0212371 | frequency_hz=240.4
- [2026-08-28 18:31:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913103.0216727 | source=vosk | rms=1201 | updated_at=1787913103.0216727 | frequency_hz=240.4
- [2026-08-28 18:31:45] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1787913105.0612965 | source=vosk | rms=1184 | updated_at=1787913105.02137 | frequency_hz=259.9
- [2026-08-28 18:31:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913105.2717383 | source=vosk | rms=1184 | updated_at=1787913105.02137 | frequency_hz=259.9
- [2026-08-28 18:31:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913105.771567 | source=vosk | rms=1184 | updated_at=1787913105.02137 | frequency_hz=259.9
- [2026-08-28 18:31:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913111.5225275 | source=vosk | rms=1184 | updated_at=1787913105.02137 | frequency_hz=259.9
- [2026-08-28 18:31:51] operator / voice_transcript_partial / voice: smart century is
  meta: kind=partial | timestamp=1787913111.5601523 | source=vosk | rms=1184 | updated_at=1787913105.02137 | frequency_hz=259.9
- [2026-08-28 18:31:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913111.7713733 | source=vosk | rms=1022 | updated_at=1787913111.7713733 | frequency_hz=88.0
- [2026-08-28 18:31:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913112.0215085 | source=vosk | rms=1022 | updated_at=1787913111.7713733 | frequency_hz=88.0
- [2026-08-28 18:31:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913112.2726073 | source=vosk | rms=944 | updated_at=1787913112.2726073 | frequency_hz=124.4
- [2026-08-28 18:31:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913112.5230021 | source=vosk | rms=944 | updated_at=1787913112.2726073 | frequency_hz=124.4
- [2026-08-28 18:31:52] operator / voice_transcript_final / voice: smart sentry is record
  meta: kind=final | timestamp=1787913112.8679776 | source=final | rms=944 | updated_at=1787913112.2726073 | frequency_hz=124.4
- [2026-08-28 18:31:52] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913112.9948764 | source=vosk | rms=944 | updated_at=1787913112.2726073 | frequency_hz=124.4
- [2026-08-28 18:31:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913113.0217502 | source=vosk | rms=944 | updated_at=1787913112.2726073 | frequency_hz=124.4
- [2026-08-28 18:31:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913113.5221748 | source=vosk | rms=944 | updated_at=1787913112.2726073 | frequency_hz=124.4
- [2026-08-28 18:31:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913116.0222423 | source=vosk | rms=1142 | updated_at=1787913116.0222423 | frequency_hz=180.0
- [2026-08-28 18:31:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913119.0223155 | source=vosk | rms=888 | updated_at=1787913118.5215232 | frequency_hz=137.2
- [2026-08-28 18:31:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913119.2711146 | source=vosk | rms=888 | updated_at=1787913118.5215232 | frequency_hz=137.2
- [2026-08-28 18:32:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913120.7585778 | source=vosk | rms=1202 | updated_at=1787913119.7715452 | frequency_hz=199.1
- [2026-08-28 18:32:01] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913121.021382 | source=vosk | rms=1200 | updated_at=1787913121.021382 | frequency_hz=203.6
- [2026-08-28 18:32:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913122.7712984 | source=vosk | rms=800 | updated_at=1787913122.271505 | frequency_hz=238.4
- [2026-08-28 18:32:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913124.2725983 | source=vosk | rms=991 | updated_at=1787913124.2725983 | frequency_hz=198.0
- [2026-08-28 18:32:06] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1787913126.0752575 | source=vosk | rms=1148 | updated_at=1787913126.0220861 | frequency_hz=237.6
- [2026-08-28 18:32:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913126.2726233 | source=vosk | rms=1121 | updated_at=1787913126.27212 | frequency_hz=183.8
- [2026-08-28 18:32:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913126.7722323 | source=vosk | rms=6153 | updated_at=1787913126.7722323 | frequency_hz=242.0
- [2026-08-28 18:32:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913127.0225894 | source=vosk | rms=4919 | updated_at=1787913127.0225894 | frequency_hz=242.0
- [2026-08-28 18:32:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913127.2713728 | source=vosk | rms=3956 | updated_at=1787913127.2713728 | frequency_hz=242.0
- [2026-08-28 18:32:07] operator / voice_transcript_partial / voice: alien run the
  meta: kind=partial | timestamp=1787913127.2869303 | source=vosk | rms=3956 | updated_at=1787913127.2713728 | frequency_hz=242.0
- [2026-08-28 18:32:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913127.5216844 | source=vosk | rms=3802 | updated_at=1787913127.5216844 | frequency_hz=242.0
- [2026-08-28 18:32:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913127.7710316 | source=vosk | rms=4803 | updated_at=1787913127.7710316 | frequency_hz=242.0
- [2026-08-28 18:32:07] operator / voice_transcript_partial / voice: alien run the smart
  meta: kind=partial | timestamp=1787913127.7807634 | source=vosk | rms=4803 | updated_at=1787913127.7710316 | frequency_hz=242.0
- [2026-08-28 18:32:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913128.0216308 | source=vosk | rms=2028 | updated_at=1787913128.0216308 | frequency_hz=232.2
- [2026-08-28 18:32:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913128.272305 | source=vosk | rms=1202 | updated_at=1787913128.272305 | frequency_hz=177.5
- [2026-08-28 18:32:08] operator / voice_transcript_partial / voice: alien run the smart sentry
  meta: kind=partial | timestamp=1787913128.2828865 | source=vosk | rms=1202 | updated_at=1787913128.272305 | frequency_hz=177.5
- [2026-08-28 18:32:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913128.5218415 | source=vosk | rms=1200 | updated_at=1787913128.5218415 | frequency_hz=212.7
- [2026-08-28 18:32:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913128.7720866 | source=vosk | rms=1023 | updated_at=1787913128.7720866 | frequency_hz=192.2
- [2026-08-28 18:32:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913129.022356 | source=vosk | rms=1055 | updated_at=1787913129.022356 | frequency_hz=196.3
- [2026-08-28 18:32:09] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1787913129.0363376 | source=final | rms=1055 | updated_at=1787913129.022356 | frequency_hz=196.3
- [2026-08-28 18:32:09] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787913129.0755954 | source=state | rms=1055 | updated_at=1787913129.022356 | frequency_hz=196.3
- [2026-08-28 18:32:09] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913129.0755954 | source=state | rms=1055 | updated_at=1787913129.022356 | frequency_hz=196.3
- [2026-08-28 18:32:15] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-08-28 18:32:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913129.2717047 | source=vosk | rms=721 | updated_at=1787913129.2717047 | frequency_hz=263.4
- [2026-08-28 18:32:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913130.5393677 | source=vosk | rms=739 | updated_at=1787913129.5220037 | frequency_hz=220.2
- [2026-08-28 18:32:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913135.032018 | source=vosk | rms=739 | updated_at=1787913129.5220037 | frequency_hz=220.2
- [2026-08-28 18:32:16] assistant / spoken_confirmation / voice: Running Smart Sentry now. Connecting the Smart Sentry boards first.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-08-28 18:32:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913136.7833679 | source=vosk | rms=1206 | updated_at=1787913136.2830975 | frequency_hz=220.2
- [2026-08-28 18:32:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913138.5485108 | source=vosk | rms=1206 | updated_at=1787913136.2830975 | frequency_hz=220.2
- [2026-08-28 18:32:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913140.3104653 | source=vosk | rms=1203 | updated_at=1787913139.7919512 | frequency_hz=220.2
- [2026-08-28 18:32:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913140.3104653 | source=vosk | rms=1201 | updated_at=1787913140.3104653 | frequency_hz=220.2
- [2026-08-28 18:32:21] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1787913141.4952242 | source=vosk | rms=1496 | updated_at=1787913140.7925487 | frequency_hz=236.9
- [2026-08-28 18:32:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913141.49623 | source=vosk | rms=1496 | updated_at=1787913140.7925487 | frequency_hz=236.9
- [2026-08-28 18:32:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913141.49623 | source=vosk | rms=1496 | updated_at=1787913140.7925487 | frequency_hz=236.9
- [2026-08-28 18:32:21] operator / voice_transcript_partial / voice: eliot spitzer
  meta: kind=partial | timestamp=1787913141.5134451 | source=vosk | rms=1496 | updated_at=1787913140.7925487 | frequency_hz=236.9
- [2026-08-28 18:32:21] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1787913141.6744463 | source=vosk | rms=1496 | updated_at=1787913140.7925487 | frequency_hz=236.9
- [2026-08-28 18:32:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913141.7926717 | source=vosk | rms=1496 | updated_at=1787913140.7925487 | frequency_hz=236.9
- [2026-08-28 18:32:21] operator / voice_transcript_partial / voice: alien such
  meta: kind=partial | timestamp=1787913141.8442414 | source=vosk | rms=1496 | updated_at=1787913140.7925487 | frequency_hz=236.9
- [2026-08-28 18:32:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913142.0441449 | source=vosk | rms=1496 | updated_at=1787913140.7925487 | frequency_hz=236.9
- [2026-08-28 18:32:22] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1787913142.7963614 | source=final | rms=1496 | updated_at=1787913140.7925487 | frequency_hz=236.9
- [2026-08-28 18:32:22] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-08-28 18:32:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913142.7963614 | source=vosk | rms=1201 | updated_at=1787913142.7963614 | frequency_hz=236.9
- [2026-08-28 18:32:23] assistant / spoken_confirmation / voice: I am listening. Ask your question.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-08-28 18:32:24] operator / voice_transcript_partial / voice: it's
  meta: kind=partial | timestamp=1787913144.3198092 | source=vosk | rms=1206 | updated_at=1787913144.0427074 | frequency_hz=336.2
- [2026-08-28 18:32:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913144.5434198 | source=vosk | rms=1206 | updated_at=1787913144.0427074 | frequency_hz=336.2
- [2026-08-28 18:32:24] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787913144.6446118 | source=state | rms=1206 | updated_at=1787913144.0427074 | frequency_hz=336.2
- [2026-08-28 18:32:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913144.6446118 | source=state | rms=1206 | updated_at=1787913144.0427074 | frequency_hz=336.2
- [2026-08-28 18:32:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913144.7922268 | source=vosk | rms=1206 | updated_at=1787913144.0427074 | frequency_hz=336.2
- [2026-08-28 18:32:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913145.043474 | source=vosk | rms=1206 | updated_at=1787913144.0427074 | frequency_hz=336.2
- [2026-08-28 18:32:25] operator / voice_transcript_final / voice: it s
  meta: kind=final | timestamp=1787913145.307788 | source=final | rms=1206 | updated_at=1787913144.0427074 | frequency_hz=336.2
- [2026-08-28 18:32:25] operator / voice_command / voice: it s
  meta: normalized=True
- [2026-08-28 18:32:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913145.5426726 | source=vosk | rms=1200 | updated_at=1787913145.5426726 | frequency_hz=336.2
- [2026-08-28 18:32:25] assistant / spoken_confirmation / voice: I did not catch a clear question or command. Please try again.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-08-28 18:32:25] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787913145.6035469 | source=state | rms=1200 | updated_at=1787913145.5426726 | frequency_hz=336.2
- [2026-08-28 18:32:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913145.793105 | source=vosk | rms=1201 | updated_at=1787913145.793105 | frequency_hz=336.2
- [2026-08-28 18:32:26] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787913146.7921941 | source=vosk | rms=1202 | updated_at=1787913146.2929883 | frequency_hz=336.2
- [2026-08-28 18:32:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913148.2926252 | source=vosk | rms=1202 | updated_at=1787913146.2929883 | frequency_hz=336.2
- [2026-08-28 18:32:28] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787913148.7932656 | source=vosk | rms=1202 | updated_at=1787913146.2929883 | frequency_hz=336.2
- [2026-08-28 18:32:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913149.0420778 | source=vosk | rms=1202 | updated_at=1787913146.2929883 | frequency_hz=336.2
- [2026-08-28 18:32:29] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787913149.5429256 | source=vosk | rms=1202 | updated_at=1787913146.2929883 | frequency_hz=336.2
- [2026-08-28 18:32:30] assistant / spoken_confirmation / voice: Listening window closed. Smart Sentry is not actively guarding right now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-08-28 18:32:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913150.2954614 | source=vosk | rms=1202 | updated_at=1787913146.2929883 | frequency_hz=336.2
- [2026-08-28 18:32:31] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787913151.5436862 | source=vosk | rms=1202 | updated_at=1787913146.2929883 | frequency_hz=336.2
- [2026-08-28 18:32:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913154.903094 | source=vosk | rms=1202 | updated_at=1787913154.903094 | frequency_hz=336.2
- [2026-08-28 18:32:34] operator / voice_transcript_partial / voice: last
  meta: kind=partial | timestamp=1787913154.9540946 | source=vosk | rms=1202 | updated_at=1787913154.903094 | frequency_hz=336.2
- [2026-08-28 18:32:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913155.1529691 | source=vosk | rms=1204 | updated_at=1787913155.1529691 | frequency_hz=336.2
- [2026-08-28 18:32:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913156.1529582 | source=vosk | rms=1200 | updated_at=1787913156.1529582 | frequency_hz=336.2
- [2026-08-28 18:32:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913156.40359 | source=vosk | rms=1200 | updated_at=1787913156.1529582 | frequency_hz=336.2
- [2026-08-28 18:32:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913156.6528 | source=vosk | rms=1200 | updated_at=1787913156.6528 | frequency_hz=336.2
- [2026-08-28 18:32:36] operator / voice_transcript_partial / voice: last please try
  meta: kind=partial | timestamp=1787913156.691543 | source=vosk | rms=1200 | updated_at=1787913156.6528 | frequency_hz=336.2
- [2026-08-28 18:32:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913156.9029133 | source=vosk | rms=1245 | updated_at=1787913156.9029133 | frequency_hz=336.2
- [2026-08-28 18:32:36] operator / voice_transcript_partial / voice: last please try again
  meta: kind=partial | timestamp=1787913156.9326923 | source=vosk | rms=1245 | updated_at=1787913156.9029133 | frequency_hz=336.2
- [2026-08-28 18:32:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913157.1533334 | source=vosk | rms=4835 | updated_at=1787913157.1533334 | frequency_hz=364.1
- [2026-08-28 18:32:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913157.403866 | source=vosk | rms=5326 | updated_at=1787913157.403866 | frequency_hz=364.1
- [2026-08-28 18:32:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913157.6526234 | source=vosk | rms=3122 | updated_at=1787913157.6526234 | frequency_hz=364.1
- [2026-08-28 18:32:37] operator / voice_transcript_partial / voice: last please try again open the
  meta: kind=partial | timestamp=1787913157.6992426 | source=vosk | rms=3122 | updated_at=1787913157.6526234 | frequency_hz=364.1
- [2026-08-28 18:32:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913157.902909 | source=vosk | rms=1700 | updated_at=1787913157.902909 | frequency_hz=302.5
- [2026-08-28 18:32:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913158.153844 | source=vosk | rms=1200 | updated_at=1787913158.153844 | frequency_hz=337.3
- [2026-08-28 18:32:38] operator / voice_transcript_partial / voice: last please try again open the camera
  meta: kind=partial | timestamp=1787913158.1774633 | source=vosk | rms=1200 | updated_at=1787913158.153844 | frequency_hz=337.3
- [2026-08-28 18:32:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913158.9028544 | source=vosk | rms=1202 | updated_at=1787913158.9028544 | frequency_hz=337.3
- [2026-08-28 18:32:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913159.1529317 | source=vosk | rms=1202 | updated_at=1787913159.1529317 | frequency_hz=337.3
- [2026-08-28 18:32:39] operator / voice_transcript_final / voice: open camera
  meta: kind=final | timestamp=1787913159.165459 | source=final | rms=1202 | updated_at=1787913159.1529317 | frequency_hz=337.3
- [2026-08-28 18:32:39] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787913159.1986053 | source=state | rms=1202 | updated_at=1787913159.1529317 | frequency_hz=337.3
- [2026-08-28 18:32:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913159.1986053 | source=state | rms=1202 | updated_at=1787913159.1529317 | frequency_hz=337.3
- [2026-08-28 18:33:07] operator / voice_command / voice: open camera
  meta: normalized=True
- [2026-08-28 18:32:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913159.402845 | source=vosk | rms=1202 | updated_at=1787913159.402845 | frequency_hz=337.3
- [2026-08-28 18:32:39] operator / voice_transcript_partial / voice: the mindset
  meta: kind=partial | timestamp=1787913159.8091152 | source=vosk | rms=878 | updated_at=1787913159.6550243 | frequency_hz=337.3
- [2026-08-28 18:32:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913159.9028077 | source=vosk | rms=878 | updated_at=1787913159.6550243 | frequency_hz=337.3
- [2026-08-28 18:32:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913160.1527734 | source=vosk | rms=878 | updated_at=1787913159.6550243 | frequency_hz=337.3
- [2026-08-28 18:32:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913160.403888 | source=vosk | rms=878 | updated_at=1787913159.6550243 | frequency_hz=337.3
- [2026-08-28 18:32:40] operator / voice_transcript_partial / voice: the mindset reports are
  meta: kind=partial | timestamp=1787913160.4144258 | source=vosk | rms=878 | updated_at=1787913159.6550243 | frequency_hz=337.3
- [2026-08-28 18:32:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913160.6528904 | source=vosk | rms=878 | updated_at=1787913159.6550243 | frequency_hz=337.3
- [2026-08-28 18:32:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913160.9023314 | source=vosk | rms=878 | updated_at=1787913159.6550243 | frequency_hz=337.3
- [2026-08-28 18:32:40] operator / voice_transcript_partial / voice: the mindset reports are connected
  meta: kind=partial | timestamp=1787913160.9256582 | source=vosk | rms=878 | updated_at=1787913159.6550243 | frequency_hz=337.3
- [2026-08-28 18:32:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913161.1531217 | source=vosk | rms=878 | updated_at=1787913159.6550243 | frequency_hz=337.3
- [2026-08-28 18:32:41] operator / voice_transcript_partial / voice: the mindset reports are connected on
  meta: kind=partial | timestamp=1787913161.162421 | source=vosk | rms=878 | updated_at=1787913159.6550243 | frequency_hz=337.3
- [2026-08-28 18:32:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913161.4030375 | source=vosk | rms=1204 | updated_at=1787913161.4030375 | frequency_hz=337.3
- [2026-08-28 18:32:41] operator / voice_transcript_partial / voice: the mindset reports are connected on the
  meta: kind=partial | timestamp=1787913161.4240842 | source=vosk | rms=1204 | updated_at=1787913161.4030375 | frequency_hz=337.3
- [2026-08-28 18:32:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913161.6521888 | source=vosk | rms=1205 | updated_at=1787913161.6521888 | frequency_hz=337.3
- [2026-08-28 18:32:41] operator / voice_transcript_partial / voice: the mindset reports are connected on this
  meta: kind=partial | timestamp=1787913161.6910968 | source=vosk | rms=1205 | updated_at=1787913161.6521888 | frequency_hz=337.3
- [2026-08-28 18:32:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913161.9029765 | source=vosk | rms=1204 | updated_at=1787913161.9029765 | frequency_hz=337.3
- [2026-08-28 18:32:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913162.1526873 | source=vosk | rms=1201 | updated_at=1787913162.1526873 | frequency_hz=337.3
- [2026-08-28 18:32:42] operator / voice_transcript_final / voice: the mindset reports are connect on this
  meta: kind=final | timestamp=1787913162.508561 | source=final | rms=1201 | updated_at=1787913162.1526873 | frequency_hz=337.3
- [2026-08-28 18:32:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913163.579548 | source=vosk | rms=1201 | updated_at=1787913162.1526873 | frequency_hz=337.3
- [2026-08-28 18:32:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913163.579548 | source=vosk | rms=1203 | updated_at=1787913163.579548 | frequency_hz=337.3
- [2026-08-28 18:32:44] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913164.1528468 | source=vosk | rms=1010 | updated_at=1787913163.624892 | frequency_hz=337.3
- [2026-08-28 18:32:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913164.7360117 | source=vosk | rms=1141 | updated_at=1787913164.7360117 | frequency_hz=337.3
- [2026-08-28 18:32:45] operator / voice_transcript_partial / voice: ask another
  meta: kind=partial | timestamp=1787913165.437906 | source=vosk | rms=968 | updated_at=1787913165.4032633 | frequency_hz=337.3
- [2026-08-28 18:32:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913165.6527581 | source=vosk | rms=968 | updated_at=1787913165.4032633 | frequency_hz=337.3
- [2026-08-28 18:32:45] operator / voice_transcript_partial / voice: ask another question
  meta: kind=partial | timestamp=1787913165.68103 | source=vosk | rms=968 | updated_at=1787913165.4032633 | frequency_hz=337.3
- [2026-08-28 18:32:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913166.1535392 | source=vosk | rms=855 | updated_at=1787913166.1535392 | frequency_hz=337.3
- [2026-08-28 18:32:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913166.4040203 | source=vosk | rms=1020 | updated_at=1787913166.4040203 | frequency_hz=337.3
- [2026-08-28 18:32:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913166.6529233 | source=vosk | rms=927 | updated_at=1787913166.6529233 | frequency_hz=337.3
- [2026-08-28 18:32:46] operator / voice_transcript_partial / voice: ask another question or
  meta: kind=partial | timestamp=1787913166.6895597 | source=vosk | rms=927 | updated_at=1787913166.6529233 | frequency_hz=337.3
- [2026-08-28 18:32:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913166.902817 | source=vosk | rms=927 | updated_at=1787913166.6529233 | frequency_hz=337.3
- [2026-08-28 18:32:47] operator / voice_transcript_partial / voice: ask another question or get another
  meta: kind=partial | timestamp=1787913167.0712538 | source=vosk | rms=927 | updated_at=1787913166.6529233 | frequency_hz=337.3
- [2026-08-28 18:32:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913167.1526623 | source=vosk | rms=927 | updated_at=1787913166.6529233 | frequency_hz=337.3
- [2026-08-28 18:32:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913167.402943 | source=vosk | rms=927 | updated_at=1787913166.6529233 | frequency_hz=337.3
- [2026-08-28 18:32:47] operator / voice_transcript_partial / voice: ask another question or get another coming out
  meta: kind=partial | timestamp=1787913167.4927545 | source=vosk | rms=927 | updated_at=1787913166.6529233 | frequency_hz=337.3
- [2026-08-28 18:32:48] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913168.1534283 | source=vosk | rms=927 | updated_at=1787913166.6529233 | frequency_hz=337.3
- [2026-08-28 18:32:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913168.4030254 | source=vosk | rms=1107 | updated_at=1787913168.4030254 | frequency_hz=337.3
- [2026-08-28 18:32:48] operator / voice_transcript_partial / voice: ask another question or get another country and around
  meta: kind=partial | timestamp=1787913168.437536 | source=vosk | rms=1107 | updated_at=1787913168.4030254 | frequency_hz=337.3
- [2026-08-28 18:32:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913168.9028158 | source=vosk | rms=1124 | updated_at=1787913168.9028158 | frequency_hz=337.3
- [2026-08-28 18:32:48] operator / voice_transcript_partial / voice: ask another question or get another coming out
  meta: kind=partial | timestamp=1787913168.961223 | source=vosk | rms=1124 | updated_at=1787913168.9028158 | frequency_hz=337.3
- [2026-08-28 18:32:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913169.1532075 | source=vosk | rms=911 | updated_at=1787913169.1532075 | frequency_hz=337.3
- [2026-08-28 18:32:49] operator / voice_transcript_partial / voice: ask another question or get another command
  meta: kind=partial | timestamp=1787913169.1851306 | source=vosk | rms=911 | updated_at=1787913169.1532075 | frequency_hz=337.3
- [2026-08-28 18:32:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913169.4041374 | source=vosk | rms=911 | updated_at=1787913169.1532075 | frequency_hz=337.3
- [2026-08-28 18:32:49] operator / voice_transcript_partial / voice: ask another question or get another command smart
  meta: kind=partial | timestamp=1787913169.4133403 | source=vosk | rms=911 | updated_at=1787913169.1532075 | frequency_hz=337.3
- [2026-08-28 18:32:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913169.6524785 | source=vosk | rms=911 | updated_at=1787913169.1532075 | frequency_hz=337.3
- [2026-08-28 18:32:49] operator / voice_transcript_partial / voice: ask another question or get another command smart century
  meta: kind=partial | timestamp=1787913169.674251 | source=vosk | rms=911 | updated_at=1787913169.1532075 | frequency_hz=337.3
- [2026-08-28 18:32:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913169.9035578 | source=vosk | rms=911 | updated_at=1787913169.1532075 | frequency_hz=337.3
- [2026-08-28 18:32:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913170.1526573 | source=vosk | rms=911 | updated_at=1787913169.1532075 | frequency_hz=337.3
- [2026-08-28 18:32:50] operator / voice_transcript_partial / voice: ask another question or get another command smart century parts
  meta: kind=partial | timestamp=1787913170.1788936 | source=vosk | rms=911 | updated_at=1787913169.1532075 | frequency_hz=337.3
- [2026-08-28 18:32:50] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913170.6533825 | source=vosk | rms=911 | updated_at=1787913169.1532075 | frequency_hz=337.3
- [2026-08-28 18:32:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913170.9027808 | source=vosk | rms=911 | updated_at=1787913169.1532075 | frequency_hz=337.3
- [2026-08-28 18:32:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913171.1533208 | source=vosk | rms=911 | updated_at=1787913169.1532075 | frequency_hz=337.3
- [2026-08-28 18:32:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913171.4030812 | source=vosk | rms=1205 | updated_at=1787913171.4030812 | frequency_hz=337.3
- [2026-08-28 18:32:51] operator / voice_transcript_final / voice: ask another question or get another command smart sentry parts
  meta: kind=final | timestamp=1787913171.8191319 | source=final | rms=1205 | updated_at=1787913171.4030812 | frequency_hz=337.3
- [2026-08-28 18:32:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913171.9967797 | source=vosk | rms=1205 | updated_at=1787913171.4030812 | frequency_hz=337.3
- [2026-08-28 18:32:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913171.9967797 | source=vosk | rms=1205 | updated_at=1787913171.4030812 | frequency_hz=337.3
- [2026-08-28 18:32:55] operator / voice_transcript_partial / voice: much
  meta: kind=partial | timestamp=1787913175.4654565 | source=vosk | rms=1201 | updated_at=1787913175.403222 | frequency_hz=337.3
- [2026-08-28 18:32:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913175.6526752 | source=vosk | rms=2146 | updated_at=1787913175.6526752 | frequency_hz=337.3
- [2026-08-28 18:32:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913175.9030716 | source=vosk | rms=1200 | updated_at=1787913175.9030716 | frequency_hz=337.3
- [2026-08-28 18:32:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913176.1531858 | source=vosk | rms=3969 | updated_at=1787913176.1531858 | frequency_hz=337.3
- [2026-08-28 18:32:56] operator / voice_transcript_final / voice: much
  meta: kind=final | timestamp=1787913176.416377 | source=final | rms=3969 | updated_at=1787913176.1531858 | frequency_hz=337.3
- [2026-08-28 18:32:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913176.4504123 | source=vosk | rms=1797 | updated_at=1787913176.4504123 | frequency_hz=337.3
- [2026-08-28 18:32:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913176.9033422 | source=vosk | rms=1797 | updated_at=1787913176.4504123 | frequency_hz=337.3
- [2026-08-28 18:32:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913177.4036489 | source=vosk | rms=1797 | updated_at=1787913176.4504123 | frequency_hz=337.3
- [2026-08-28 18:32:58] operator / voice_transcript_partial / voice: something down
  meta: kind=partial | timestamp=1787913178.4485142 | source=vosk | rms=1062 | updated_at=1787913178.4035242 | frequency_hz=337.3
- [2026-08-28 18:32:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913178.903416 | source=vosk | rms=1062 | updated_at=1787913178.4035242 | frequency_hz=337.3
- [2026-08-28 18:32:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913179.152896 | source=vosk | rms=976 | updated_at=1787913179.152896 | frequency_hz=337.3
- [2026-08-28 18:32:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913179.402963 | source=vosk | rms=1141 | updated_at=1787913179.402963 | frequency_hz=337.3
- [2026-08-28 18:32:59] operator / voice_transcript_partial / voice: something down our
  meta: kind=partial | timestamp=1787913179.4537523 | source=vosk | rms=1141 | updated_at=1787913179.402963 | frequency_hz=337.3
- [2026-08-28 18:32:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913179.6533992 | source=vosk | rms=1200 | updated_at=1787913179.6533992 | frequency_hz=337.3
- [2026-08-28 18:32:59] operator / voice_transcript_partial / voice: something down our cameras
  meta: kind=partial | timestamp=1787913179.6741145 | source=vosk | rms=1200 | updated_at=1787913179.6533992 | frequency_hz=337.3
- [2026-08-28 18:32:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913179.9027123 | source=vosk | rms=1200 | updated_at=1787913179.9027123 | frequency_hz=337.3
- [2026-08-28 18:33:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913180.1539288 | source=vosk | rms=1201 | updated_at=1787913180.1539288 | frequency_hz=337.3
- [2026-08-28 18:33:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913180.4030733 | source=vosk | rms=1202 | updated_at=1787913180.4030733 | frequency_hz=337.3
- [2026-08-28 18:33:01] operator / voice_transcript_final / voice: something down our camera
  meta: kind=final | timestamp=1787913181.059836 | source=final | rms=1202 | updated_at=1787913180.4030733 | frequency_hz=337.3
- [2026-08-28 18:33:01] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913181.2102864 | source=vosk | rms=1202 | updated_at=1787913180.4030733 | frequency_hz=337.3
- [2026-08-28 18:33:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913185.153126 | source=vosk | rms=1201 | updated_at=1787913185.153126 | frequency_hz=337.3
- [2026-08-28 18:33:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913185.653546 | source=vosk | rms=1201 | updated_at=1787913185.153126 | frequency_hz=337.3

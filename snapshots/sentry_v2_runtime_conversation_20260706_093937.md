# SMART SENTRY V5.0.0 Runtime Conversation Export

- Generated: 2026-07-06 09:39:37
- Entries: 265
- Roles: {'assistant': 6, 'system': 189, 'operator': 70}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 189, 'spoken_confirmation': 4, 'voice_transcript_partial': 54, 'voice_transcript_final': 13, 'voice_command': 3}
- Channels: {'text': 2, 'voice': 263}
- Latest operator request: earlier
- Latest assistant message: I did not catch a clear question or command. Please try again.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-07-06 09:37:09] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-07-06 09:37:09] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-07-06 09:37:10] system / voice_status / voice: listening
  meta: kind=status | timestamp=1783301830.983376 | source=vosk
- [2026-07-06 09:37:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301832.9286442 | source=vosk | rms=381 | updated_at=1783301832.9286442
- [2026-07-06 09:37:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301833.678601 | source=vosk | rms=276 | updated_at=1783301833.1782758
- [2026-07-06 09:37:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301834.6783895 | source=vosk | rms=202 | updated_at=1783301834.6783895
- [2026-07-06 09:37:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301835.9284105 | source=vosk | rms=218 | updated_at=1783301835.428784
- [2026-07-06 09:37:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301836.42825 | source=vosk | rms=218 | updated_at=1783301835.428784
- [2026-07-06 09:37:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301836.9279847 | source=vosk | rms=218 | updated_at=1783301835.428784
- [2026-07-06 09:37:17] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301837.179485 | source=vosk | rms=152 | updated_at=1783301837.179485
- [2026-07-06 09:37:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301839.1787784 | source=vosk | rms=272 | updated_at=1783301838.6794386
- [2026-07-06 09:37:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301839.9286933 | source=vosk | rms=272 | updated_at=1783301838.6794386
- [2026-07-06 09:37:20] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301840.4280026 | source=vosk | rms=272 | updated_at=1783301838.6794386
- [2026-07-06 09:37:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301840.6786566 | source=vosk | rms=272 | updated_at=1783301838.6794386
- [2026-07-06 09:37:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301841.1786578 | source=vosk | rms=272 | updated_at=1783301838.6794386
- [2026-07-06 09:37:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301841.928515 | source=vosk | rms=141 | updated_at=1783301841.928515
- [2026-07-06 09:37:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301842.9282014 | source=vosk | rms=291 | updated_at=1783301842.4304795
- [2026-07-06 09:37:49] assistant / spoken_confirmation / voice: Smart Sentry is ready.
  meta: interrupt=True | assistant_output=False | spoken=True
- [2026-07-06 09:37:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301845.1774817 | source=vosk | rms=291 | updated_at=1783301842.4304795
- [2026-07-06 09:37:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301845.6783283 | source=vosk | rms=291 | updated_at=1783301842.4304795
- [2026-07-06 09:37:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301845.9283993 | source=vosk | rms=120 | updated_at=1783301845.9283993
- [2026-07-06 09:37:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301848.6779854 | source=vosk | rms=130 | updated_at=1783301848.1787071
- [2026-07-06 09:37:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301848.9282541 | source=vosk | rms=130 | updated_at=1783301848.1787071
- [2026-07-06 09:37:30] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301850.1789503 | source=vosk | rms=130 | updated_at=1783301848.1787071
- [2026-07-06 09:37:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301850.4291022 | source=vosk | rms=121 | updated_at=1783301850.4291022
- [2026-07-06 09:37:34] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1783301854.7006385 | source=vosk | rms=236 | updated_at=1783301854.6784644
- [2026-07-06 09:37:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301854.9282076 | source=vosk | rms=691 | updated_at=1783301854.9282076
- [2026-07-06 09:37:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301855.1799757 | source=vosk | rms=161 | updated_at=1783301855.1784725
- [2026-07-06 09:37:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301855.6783245 | source=vosk | rms=130 | updated_at=1783301855.6783245
- [2026-07-06 09:37:35] operator / voice_transcript_final / voice: and
  meta: kind=final | timestamp=1783301855.922678 | source=final | rms=130 | updated_at=1783301855.6783245
- [2026-07-06 09:37:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301855.9572084 | source=vosk | rms=155 | updated_at=1783301855.9557042
- [2026-07-06 09:37:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301859.9284477 | source=vosk | rms=257 | updated_at=1783301859.179142
- [2026-07-06 09:37:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301860.6790545 | source=vosk | rms=257 | updated_at=1783301859.179142
- [2026-07-06 09:37:54] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1783301874.6688318 | source=vosk | rms=922 | updated_at=1783301874.6201851
- [2026-07-06 09:37:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301874.8688047 | source=vosk | rms=1038 | updated_at=1783301874.8688047
- [2026-07-06 09:37:54] operator / voice_transcript_partial / voice: smart century is
  meta: kind=partial | timestamp=1783301874.940033 | source=vosk | rms=1038 | updated_at=1783301874.8688047
- [2026-07-06 09:37:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301875.1192892 | source=vosk | rms=697 | updated_at=1783301875.1192892
- [2026-07-06 09:37:55] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301875.619664 | source=vosk | rms=687 | updated_at=1783301875.619664
- [2026-07-06 09:37:55] operator / voice_transcript_partial / voice: smart century is ready
  meta: kind=partial | timestamp=1783301875.654218 | source=vosk | rms=687 | updated_at=1783301875.619664
- [2026-07-06 09:37:56] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301876.1194053 | source=vosk | rms=687 | updated_at=1783301875.619664
- [2026-07-06 09:37:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301876.3721595 | source=vosk | rms=391 | updated_at=1783301876.3721595
- [2026-07-06 09:37:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301876.6195486 | source=vosk | rms=727 | updated_at=1783301876.6195486
- [2026-07-06 09:37:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301877.1185029 | source=vosk | rms=218 | updated_at=1783301877.1185029
- [2026-07-06 09:37:57] operator / voice_transcript_partial / voice: smart century is ready to
  meta: kind=partial | timestamp=1783301877.1272879 | source=vosk | rms=218 | updated_at=1783301877.1185029
- [2026-07-06 09:37:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301877.3686144 | source=vosk | rms=218 | updated_at=1783301877.1185029
- [2026-07-06 09:37:57] operator / voice_transcript_final / voice: smart sentry is ready
  meta: kind=final | timestamp=1783301877.6942904 | source=final | rms=218 | updated_at=1783301877.1185029
- [2026-07-06 09:37:57] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301877.825777 | source=vosk | rms=218 | updated_at=1783301877.1185029
- [2026-07-06 09:37:57] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301877.8710117 | source=vosk | rms=201 | updated_at=1783301877.8710117
- [2026-07-06 09:37:58] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301878.368705 | source=vosk | rms=201 | updated_at=1783301877.8710117
- [2026-07-06 09:38:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301880.6204371 | source=vosk | rms=238 | updated_at=1783301880.6204371
- [2026-07-06 09:38:03] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1783301883.4612827 | source=vosk | rms=4930 | updated_at=1783301883.3691816 | frequency_hz=310.9
- [2026-07-06 09:38:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301883.6201742 | source=vosk | rms=1053 | updated_at=1783301883.6201742 | frequency_hz=246.9
- [2026-07-06 09:38:03] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301883.8686676 | source=vosk | rms=5447 | updated_at=1783301883.8686676 | frequency_hz=246.9
- [2026-07-06 09:38:03] operator / voice_transcript_partial / voice: do you
  meta: kind=partial | timestamp=1783301883.886921 | source=vosk | rms=5447 | updated_at=1783301883.8686676 | frequency_hz=246.9
- [2026-07-06 09:38:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301884.11873 | source=vosk | rms=4328 | updated_at=1783301884.11873 | frequency_hz=246.9
- [2026-07-06 09:38:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301884.3695788 | source=vosk | rms=3289 | updated_at=1783301884.3695788 | frequency_hz=246.9
- [2026-07-06 09:38:04] operator / voice_transcript_partial / voice: do you run
  meta: kind=partial | timestamp=1783301884.381686 | source=vosk | rms=3289 | updated_at=1783301884.3695788 | frequency_hz=246.9
- [2026-07-06 09:38:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301884.6188054 | source=vosk | rms=2780 | updated_at=1783301884.6188054 | frequency_hz=246.9
- [2026-07-06 09:38:04] operator / voice_transcript_partial / voice: do you run the smart
  meta: kind=partial | timestamp=1783301884.681429 | source=vosk | rms=2780 | updated_at=1783301884.6188054 | frequency_hz=246.9
- [2026-07-06 09:38:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301884.869622 | source=vosk | rms=4746 | updated_at=1783301884.869622 | frequency_hz=282.3
- [2026-07-06 09:38:04] operator / voice_transcript_partial / voice: do you run the smarts and three
  meta: kind=partial | timestamp=1783301884.9152372 | source=vosk | rms=4746 | updated_at=1783301884.869622 | frequency_hz=282.3
- [2026-07-06 09:38:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301885.1250696 | source=vosk | rms=1168 | updated_at=1783301885.1250696 | frequency_hz=282.3
- [2026-07-06 09:38:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301885.6188745 | source=vosk | rms=1168 | updated_at=1783301885.1250696 | frequency_hz=282.3
- [2026-07-06 09:38:06] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301886.1190183 | source=vosk | rms=1168 | updated_at=1783301885.1250696 | frequency_hz=282.3
- [2026-07-06 09:38:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301886.369027 | source=vosk | rms=1168 | updated_at=1783301885.1250696 | frequency_hz=282.3
- [2026-07-06 09:38:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301886.6190803 | source=vosk | rms=984 | updated_at=1783301886.6190803 | frequency_hz=282.3
- [2026-07-06 09:38:07] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1783301887.146078 | source=final | rms=984 | updated_at=1783301886.6190803 | frequency_hz=282.3
- [2026-07-06 09:38:07] system / voice_status / voice: processing
  meta: kind=status | timestamp=1783301887.1790013 | source=state | rms=984 | updated_at=1783301886.6190803 | frequency_hz=282.3
- [2026-07-06 09:38:07] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301887.1790013 | source=state | rms=984 | updated_at=1783301886.6190803 | frequency_hz=282.3
- [2026-07-06 09:38:07] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-07-06 09:38:07] assistant / spoken_confirmation / voice: Running Smart Sentry now. Connecting the Smart Sentry boards first.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-07-06 09:38:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301887.6493902 | source=vosk | rms=1205 | updated_at=1783301887.6493902 | frequency_hz=282.3
- [2026-07-06 09:38:09] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1783301889.8075807 | source=vosk | rms=611 | updated_at=1783301888.998984 | frequency_hz=282.3
- [2026-07-06 09:38:09] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301889.8080926 | source=vosk | rms=611 | updated_at=1783301888.998984 | frequency_hz=282.3
- [2026-07-06 09:38:09] operator / voice_transcript_partial / voice: exploring
  meta: kind=partial | timestamp=1783301889.8653154 | source=vosk | rms=611 | updated_at=1783301888.998984 | frequency_hz=282.3
- [2026-07-06 09:38:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301890.4988716 | source=vosk | rms=611 | updated_at=1783301888.998984 | frequency_hz=282.3
- [2026-07-06 09:38:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301890.7491918 | source=vosk | rms=729 | updated_at=1783301890.7491918 | frequency_hz=282.3
- [2026-07-06 09:38:10] operator / voice_transcript_partial / voice: he starts at
  meta: kind=partial | timestamp=1783301890.798958 | source=vosk | rms=729 | updated_at=1783301890.7491918 | frequency_hz=282.3
- [2026-07-06 09:38:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301891.002423 | source=vosk | rms=464 | updated_at=1783301891.002423 | frequency_hz=282.3
- [2026-07-06 09:38:11] operator / voice_transcript_partial / voice: he starts at you can
  meta: kind=partial | timestamp=1783301891.1162136 | source=vosk | rms=464 | updated_at=1783301891.002423 | frequency_hz=282.3
- [2026-07-06 09:38:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301891.2522664 | source=vosk | rms=464 | updated_at=1783301891.002423 | frequency_hz=282.3
- [2026-07-06 09:38:11] operator / voice_transcript_partial / voice: smart such
  meta: kind=partial | timestamp=1783301891.2825053 | source=vosk | rms=464 | updated_at=1783301891.002423 | frequency_hz=282.3
- [2026-07-06 09:38:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301891.50049 | source=vosk | rms=584 | updated_at=1783301891.49949 | frequency_hz=282.3
- [2026-07-06 09:38:11] operator / voice_transcript_partial / voice: smart such connecting the
  meta: kind=partial | timestamp=1783301891.519124 | source=vosk | rms=584 | updated_at=1783301891.49949 | frequency_hz=282.3
- [2026-07-06 09:38:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301891.749551 | source=vosk | rms=1351 | updated_at=1783301891.749551 | frequency_hz=282.3
- [2026-07-06 09:38:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301891.9990213 | source=vosk | rms=1200 | updated_at=1783301891.9990213 | frequency_hz=282.3
- [2026-07-06 09:38:12] operator / voice_transcript_partial / voice: smart such connecting the sports
  meta: kind=partial | timestamp=1783301892.0492373 | source=vosk | rms=1200 | updated_at=1783301891.9990213 | frequency_hz=282.3
- [2026-07-06 09:38:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301892.249721 | source=vosk | rms=1324 | updated_at=1783301892.249721 | frequency_hz=320.0
- [2026-07-06 09:38:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301892.500722 | source=vosk | rms=1205 | updated_at=1783301892.500722 | frequency_hz=320.0
- [2026-07-06 09:38:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301893.0020576 | source=vosk | rms=1205 | updated_at=1783301892.500722 | frequency_hz=320.0
- [2026-07-06 09:38:13] operator / voice_transcript_final / voice: running smart such connecting the ports
  meta: kind=final | timestamp=1783301893.3759706 | source=final | rms=1205 | updated_at=1783301892.500722 | frequency_hz=320.0
- [2026-07-06 09:38:13] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301893.5507383 | source=vosk | rms=1205 | updated_at=1783301892.500722 | frequency_hz=320.0
- [2026-07-06 09:38:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301893.5507383 | source=vosk | rms=1205 | updated_at=1783301892.500722 | frequency_hz=320.0
- [2026-07-06 09:38:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301895.2505782 | source=vosk | rms=468 | updated_at=1783301894.2494702 | frequency_hz=320.0
- [2026-07-06 09:38:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301895.498952 | source=vosk | rms=541 | updated_at=1783301895.498952 | frequency_hz=320.0
- [2026-07-06 09:38:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301896.4993672 | source=vosk | rms=548 | updated_at=1783301895.7490852 | frequency_hz=320.0
- [2026-07-06 09:38:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301896.7491786 | source=vosk | rms=548 | updated_at=1783301895.7490852 | frequency_hz=320.0
- [2026-07-06 09:38:18] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301898.0025702 | source=vosk | rms=548 | updated_at=1783301895.7490852 | frequency_hz=320.0
- [2026-07-06 09:38:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301900.7504926 | source=vosk | rms=548 | updated_at=1783301895.7490852 | frequency_hz=320.0
- [2026-07-06 09:38:24] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301904.0007818 | source=vosk | rms=875 | updated_at=1783301900.9998417 | frequency_hz=320.0
- [2026-07-06 09:38:26] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301906.7500253 | source=vosk | rms=875 | updated_at=1783301900.9998417 | frequency_hz=320.0
- [2026-07-06 09:38:29] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1783301909.2639885 | source=vosk | rms=1200 | updated_at=1783301909.2499297 | frequency_hz=247.9
- [2026-07-06 09:38:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301909.4993854 | source=vosk | rms=1200 | updated_at=1783301909.2499297 | frequency_hz=247.9
- [2026-07-06 09:38:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301910.7497172 | source=vosk | rms=1201 | updated_at=1783301910.7497172 | frequency_hz=218.0
- [2026-07-06 09:38:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301911.0000772 | source=vosk | rms=1205 | updated_at=1783301911.0000772 | frequency_hz=218.0
- [2026-07-06 09:38:31] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1783301911.3828866 | source=final | rms=1205 | updated_at=1783301911.0000772 | frequency_hz=218.0
- [2026-07-06 09:38:31] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-07-06 09:38:31] assistant / spoken_confirmation / voice: I am listening. Ask your question.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-07-06 09:38:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301912.0006356 | source=vosk | rms=827 | updated_at=1783301912.0006356 | frequency_hz=218.0
- [2026-07-06 09:38:32] operator / voice_transcript_partial / voice: stick
  meta: kind=partial | timestamp=1783301912.5459387 | source=vosk | rms=1323 | updated_at=1783301912.4995947 | frequency_hz=213.7
- [2026-07-06 09:38:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301912.7497947 | source=vosk | rms=1698 | updated_at=1783301912.7497947 | frequency_hz=201.2
- [2026-07-06 09:38:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301912.999989 | source=vosk | rms=1201 | updated_at=1783301912.999989 | frequency_hz=193.1
- [2026-07-06 09:38:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301913.2569182 | source=vosk | rms=1200 | updated_at=1783301913.2569182 | frequency_hz=226.3
- [2026-07-06 09:38:33] operator / voice_transcript_final / voice: stick
  meta: kind=final | timestamp=1783301913.4720814 | source=final | rms=1200 | updated_at=1783301913.2569182 | frequency_hz=226.3
- [2026-07-06 09:38:33] system / voice_status / voice: processing
  meta: kind=status | timestamp=1783301913.5096927 | source=state | rms=1200 | updated_at=1783301913.2569182 | frequency_hz=226.3
- [2026-07-06 09:38:33] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301913.5096927 | source=state | rms=1200 | updated_at=1783301913.2569182 | frequency_hz=226.3
- [2026-07-06 09:38:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301913.5096927 | source=vosk | rms=861 | updated_at=1783301913.5096927 | frequency_hz=226.3
- [2026-07-06 09:38:33] operator / voice_command / voice: stick
  meta: normalized=True
- [2026-07-06 09:38:33] assistant / spoken_confirmation / voice: I did not catch a clear question or command. Please try again.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-07-06 09:38:34] system / voice_status / voice: listening
  meta: kind=status | timestamp=1783301914.212749 | source=state | rms=861 | updated_at=1783301913.5096927 | frequency_hz=226.3
- [2026-07-06 09:38:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301914.499843 | source=vosk | rms=861 | updated_at=1783301913.5096927 | frequency_hz=226.3
- [2026-07-06 09:38:35] operator / voice_transcript_partial / voice: south
  meta: kind=partial | timestamp=1783301915.0217655 | source=vosk | rms=861 | updated_at=1783301913.5096927 | frequency_hz=226.3
- [2026-07-06 09:38:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301915.24947 | source=vosk | rms=861 | updated_at=1783301913.5096927 | frequency_hz=226.3
- [2026-07-06 09:38:35] operator / voice_transcript_partial / voice: about thirty
  meta: kind=partial | timestamp=1783301915.2928996 | source=vosk | rms=861 | updated_at=1783301913.5096927 | frequency_hz=226.3
- [2026-07-06 09:38:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301915.4993 | source=vosk | rms=1013 | updated_at=1783301915.4993 | frequency_hz=226.3
- [2026-07-06 09:38:35] operator / voice_transcript_partial / voice: about thirty four
  meta: kind=partial | timestamp=1783301915.5168977 | source=vosk | rms=1013 | updated_at=1783301915.4993 | frequency_hz=226.3
- [2026-07-06 09:38:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301915.7492876 | source=vosk | rms=1013 | updated_at=1783301915.4993 | frequency_hz=226.3
- [2026-07-06 09:38:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301915.9994059 | source=vosk | rms=1203 | updated_at=1783301915.9994059 | frequency_hz=226.3
- [2026-07-06 09:38:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301916.2509413 | source=vosk | rms=1250 | updated_at=1783301916.2509413 | frequency_hz=196.8
- [2026-07-06 09:38:36] operator / voice_transcript_partial / voice: about thirty four eight
  meta: kind=partial | timestamp=1783301916.2646003 | source=vosk | rms=1250 | updated_at=1783301916.2509413 | frequency_hz=196.8
- [2026-07-06 09:38:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301916.5007217 | source=vosk | rms=1403 | updated_at=1783301916.5007217 | frequency_hz=179.7
- [2026-07-06 09:38:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301916.749449 | source=vosk | rms=1219 | updated_at=1783301916.749449 | frequency_hz=159.5
- [2026-07-06 09:38:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301916.9997325 | source=vosk | rms=1203 | updated_at=1783301916.9997325 | frequency_hz=159.5
- [2026-07-06 09:38:37] operator / voice_transcript_final / voice: about thirty four eight
  meta: kind=final | timestamp=1783301917.2992327 | source=final | rms=1203 | updated_at=1783301916.9997325 | frequency_hz=159.5
- [2026-07-06 09:38:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301917.429043 | source=vosk | rms=914 | updated_at=1783301917.429043 | frequency_hz=222.7
- [2026-07-06 09:38:37] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1783301917.4865828 | source=vosk | rms=914 | updated_at=1783301917.429043 | frequency_hz=222.7
- [2026-07-06 09:38:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301918.0000362 | source=vosk | rms=830 | updated_at=1783301918.0000362 | frequency_hz=222.7
- [2026-07-06 09:38:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301918.250036 | source=vosk | rms=830 | updated_at=1783301918.0000362 | frequency_hz=222.7
- [2026-07-06 09:38:38] operator / voice_transcript_partial / voice: baseline
  meta: kind=partial | timestamp=1783301918.3006904 | source=vosk | rms=830 | updated_at=1783301918.0000362 | frequency_hz=222.7
- [2026-07-06 09:38:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301918.4995072 | source=vosk | rms=830 | updated_at=1783301918.0000362 | frequency_hz=222.7
- [2026-07-06 09:38:38] operator / voice_transcript_partial / voice: baseline current
  meta: kind=partial | timestamp=1783301918.5221143 | source=vosk | rms=830 | updated_at=1783301918.0000362 | frequency_hz=222.7
- [2026-07-06 09:38:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301918.749977 | source=vosk | rms=830 | updated_at=1783301918.0000362 | frequency_hz=222.7
- [2026-07-06 09:38:38] operator / voice_transcript_partial / voice: baseline current state of
  meta: kind=partial | timestamp=1783301918.7732174 | source=vosk | rms=830 | updated_at=1783301918.0000362 | frequency_hz=222.7
- [2026-07-06 09:38:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301918.9996011 | source=vosk | rms=830 | updated_at=1783301918.0000362 | frequency_hz=222.7
- [2026-07-06 09:38:39] operator / voice_transcript_partial / voice: baseline current state and
  meta: kind=partial | timestamp=1783301919.014154 | source=vosk | rms=830 | updated_at=1783301918.0000362 | frequency_hz=222.7
- [2026-07-06 09:38:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301919.2511714 | source=vosk | rms=830 | updated_at=1783301918.0000362 | frequency_hz=222.7
- [2026-07-06 09:38:39] operator / voice_transcript_partial / voice: baseline current state
  meta: kind=partial | timestamp=1783301919.2753465 | source=vosk | rms=830 | updated_at=1783301918.0000362 | frequency_hz=222.7
- [2026-07-06 09:38:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301919.4992454 | source=vosk | rms=830 | updated_at=1783301918.0000362 | frequency_hz=222.7
- [2026-07-06 09:38:39] operator / voice_transcript_partial / voice: baseline current state engaging
  meta: kind=partial | timestamp=1783301919.5107777 | source=vosk | rms=830 | updated_at=1783301918.0000362 | frequency_hz=222.7
- [2026-07-06 09:38:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301919.7514224 | source=vosk | rms=1200 | updated_at=1783301919.7514224 | frequency_hz=96.0
- [2026-07-06 09:38:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301919.9998565 | source=vosk | rms=925 | updated_at=1783301919.9998565 | frequency_hz=201.7
- [2026-07-06 09:38:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301920.253227 | source=vosk | rms=3027 | updated_at=1783301920.253227 | frequency_hz=201.7
- [2026-07-06 09:38:40] operator / voice_transcript_final / voice: baseline current state engaging
  meta: kind=final | timestamp=1783301920.9650848 | source=final | rms=3027 | updated_at=1783301920.253227 | frequency_hz=201.7
- [2026-07-06 09:38:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301921.1126928 | source=vosk | rms=1210 | updated_at=1783301921.1126928 | frequency_hz=201.7
- [2026-07-06 09:38:41] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1783301921.165467 | source=vosk | rms=1874 | updated_at=1783301921.1499174 | frequency_hz=175.2
- [2026-07-06 09:38:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301921.500023 | source=vosk | rms=1927 | updated_at=1783301921.500023 | frequency_hz=175.2
- [2026-07-06 09:38:41] operator / voice_transcript_partial / voice: alien changed
  meta: kind=partial | timestamp=1783301921.5477104 | source=vosk | rms=1927 | updated_at=1783301921.500023 | frequency_hz=175.2
- [2026-07-06 09:38:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301921.7501261 | source=vosk | rms=3094 | updated_at=1783301921.7501261 | frequency_hz=175.2
- [2026-07-06 09:38:41] operator / voice_transcript_partial / voice: alien changed the
  meta: kind=partial | timestamp=1783301921.7928789 | source=vosk | rms=3094 | updated_at=1783301921.7501261 | frequency_hz=175.2
- [2026-07-06 09:38:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301922.0001032 | source=vosk | rms=1878 | updated_at=1783301922.0001032 | frequency_hz=175.2
- [2026-07-06 09:38:42] operator / voice_transcript_partial / voice: alien changed the profile
  meta: kind=partial | timestamp=1783301922.0182898 | source=vosk | rms=1878 | updated_at=1783301922.0001032 | frequency_hz=175.2
- [2026-07-06 09:38:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301922.2511072 | source=vosk | rms=1890 | updated_at=1783301922.2511072 | frequency_hz=175.2
- [2026-07-06 09:38:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301922.499963 | source=vosk | rms=1294 | updated_at=1783301922.499963 | frequency_hz=175.2
- [2026-07-06 09:38:42] operator / voice_transcript_partial / voice: alien changed the profile to smart
  meta: kind=partial | timestamp=1783301922.508483 | source=vosk | rms=1294 | updated_at=1783301922.499963 | frequency_hz=175.2
- [2026-07-06 09:38:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301922.7499182 | source=vosk | rms=1439 | updated_at=1783301922.7499182 | frequency_hz=175.2
- [2026-07-06 09:38:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301923.0000162 | source=vosk | rms=1330 | updated_at=1783301923.0000162 | frequency_hz=175.2
- [2026-07-06 09:38:43] operator / voice_transcript_partial / voice: alien changed the profile to smart cent respectively
  meta: kind=partial | timestamp=1783301923.0174901 | source=vosk | rms=1330 | updated_at=1783301923.0000162 | frequency_hz=175.2
- [2026-07-06 09:38:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301923.251919 | source=vosk | rms=2573 | updated_at=1783301923.251919 | frequency_hz=175.2
- [2026-07-06 09:38:43] operator / voice_transcript_partial / voice: alien changed the profile to smart century speed
  meta: kind=partial | timestamp=1783301923.2628286 | source=vosk | rms=2573 | updated_at=1783301923.251919 | frequency_hz=175.2
- [2026-07-06 09:38:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301923.5007484 | source=vosk | rms=1205 | updated_at=1783301923.5002458 | frequency_hz=175.2
- [2026-07-06 09:38:43] operator / voice_transcript_partial / voice: alien changed the profile to smart century speed five
  meta: kind=partial | timestamp=1783301923.5269532 | source=vosk | rms=1205 | updated_at=1783301923.5002458 | frequency_hz=175.2
- [2026-07-06 09:38:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301923.7496083 | source=vosk | rms=1202 | updated_at=1783301923.7496083 | frequency_hz=191.6
- [2026-07-06 09:38:43] system / voice_status / voice: processing
  meta: kind=status | timestamp=1783301923.7834792 | source=state | rms=1202 | updated_at=1783301923.7496083 | frequency_hz=191.6
- [2026-07-06 09:38:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301923.7894819 | source=state | rms=1202 | updated_at=1783301923.7496083 | frequency_hz=191.6
- [2026-07-06 09:38:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301924.0011363 | source=vosk | rms=886 | updated_at=1783301924.0011363 | frequency_hz=191.7
- [2026-07-06 09:38:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301924.249587 | source=vosk | rms=1202 | updated_at=1783301924.249587 | frequency_hz=205.8
- [2026-07-06 09:38:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301924.4994338 | source=vosk | rms=1201 | updated_at=1783301924.4994338 | frequency_hz=196.8
- [2026-07-06 09:38:45] system / voice_status / voice: listening
  meta: kind=status | timestamp=1783301925.0311527 | source=state | rms=1201 | updated_at=1783301924.4994338 | frequency_hz=196.8
- [2026-07-06 09:38:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301925.1531994 | source=state | rms=1201 | updated_at=1783301924.4994338 | frequency_hz=196.8
- [2026-07-06 09:38:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301927.5031905 | source=vosk | rms=1201 | updated_at=1783301924.4994338 | frequency_hz=196.8
- [2026-07-06 09:38:48] operator / voice_transcript_partial / voice: cannot
  meta: kind=partial | timestamp=1783301928.017906 | source=vosk | rms=1201 | updated_at=1783301924.4994338 | frequency_hz=196.8
- [2026-07-06 09:38:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301928.500826 | source=vosk | rms=1201 | updated_at=1783301924.4994338 | frequency_hz=196.8
- [2026-07-06 09:38:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301929.4658341 | source=vosk | rms=1201 | updated_at=1783301924.4994338 | frequency_hz=196.8
- [2026-07-06 09:38:49] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301929.959612 | source=vosk | rms=1201 | updated_at=1783301924.4994338 | frequency_hz=196.8
- [2026-07-06 09:38:50] operator / voice_transcript_final / voice: cannot
  meta: kind=final | timestamp=1783301930.8985546 | source=final | rms=1201 | updated_at=1783301924.4994338 | frequency_hz=196.8
- [2026-07-06 09:38:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301930.962136 | source=vosk | rms=1201 | updated_at=1783301930.962136 | frequency_hz=196.8
- [2026-07-06 09:38:50] operator / voice_transcript_partial / voice: cannot fire safety
  meta: kind=partial | timestamp=1783301930.979658 | source=vosk | rms=1201 | updated_at=1783301930.962136 | frequency_hz=196.8
- [2026-07-06 09:38:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301931.210724 | source=vosk | rms=1205 | updated_at=1783301931.210724 | frequency_hz=196.8
- [2026-07-06 09:38:51] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301931.7097251 | source=vosk | rms=1205 | updated_at=1783301931.210724 | frequency_hz=196.8
- [2026-07-06 09:38:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301933.7101352 | source=vosk | rms=1205 | updated_at=1783301931.210724 | frequency_hz=196.8
- [2026-07-06 09:38:54] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301934.2099986 | source=vosk | rms=1205 | updated_at=1783301931.210724 | frequency_hz=196.8
- [2026-07-06 09:38:54] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301934.710495 | source=vosk | rms=1205 | updated_at=1783301931.210724 | frequency_hz=196.8
- [2026-07-06 09:38:55] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301935.2110548 | source=vosk | rms=1205 | updated_at=1783301931.210724 | frequency_hz=196.8
- [2026-07-06 09:39:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301944.4623244 | source=vosk | rms=1205 | updated_at=1783301931.210724 | frequency_hz=196.8
- [2026-07-06 09:39:04] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301944.9607747 | source=vosk | rms=1205 | updated_at=1783301931.210724 | frequency_hz=196.8
- [2026-07-06 09:39:05] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301945.4603434 | source=vosk | rms=1205 | updated_at=1783301931.210724 | frequency_hz=196.8
- [2026-07-06 09:39:05] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301945.9602673 | source=vosk | rms=1205 | updated_at=1783301931.210724 | frequency_hz=196.8
- [2026-07-06 09:39:10] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301950.210035 | source=vosk | rms=1205 | updated_at=1783301931.210724 | frequency_hz=196.8
- [2026-07-06 09:39:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301951.1481013 | source=vosk | rms=619 | updated_at=1783301950.4608622 | frequency_hz=196.8
- [2026-07-06 09:39:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301951.1481013 | source=vosk | rms=619 | updated_at=1783301950.4608622 | frequency_hz=196.8
- [2026-07-06 09:39:12] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301952.3636906 | source=vosk | rms=491 | updated_at=1783301951.8903618 | frequency_hz=196.8
- [2026-07-06 09:39:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301952.3636906 | source=vosk | rms=491 | updated_at=1783301951.8903618 | frequency_hz=196.8
- [2026-07-06 09:39:12] operator / voice_transcript_partial / voice: cannot fire safety not fifty not a cannot fire safety is not
  meta: kind=partial | timestamp=1783301952.3780818 | source=vosk | rms=491 | updated_at=1783301951.8903618 | frequency_hz=196.8
- [2026-07-06 09:39:12] operator / voice_transcript_partial / voice: cannot fire safety not fifty not a cannot fire safety is not hard
  meta: kind=partial | timestamp=1783301952.4162283 | source=vosk | rms=491 | updated_at=1783301951.8903618 | frequency_hz=196.8
- [2026-07-06 09:39:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301952.6398478 | source=vosk | rms=491 | updated_at=1783301951.8903618 | frequency_hz=196.8
- [2026-07-06 09:39:12] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301952.8904626 | source=vosk | rms=491 | updated_at=1783301951.8903618 | frequency_hz=196.8
- [2026-07-06 09:39:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301953.1399884 | source=vosk | rms=491 | updated_at=1783301951.8903618 | frequency_hz=196.8
- [2026-07-06 09:39:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301953.3899486 | source=vosk | rms=491 | updated_at=1783301951.8903618 | frequency_hz=196.8
- [2026-07-06 09:39:13] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301953.64004 | source=vosk | rms=491 | updated_at=1783301951.8903618 | frequency_hz=196.8
- [2026-07-06 09:39:13] operator / voice_transcript_final / voice: cannot fire safety not fifty not a cannot fire safety is not hard
  meta: kind=final | timestamp=1783301953.9708018 | source=final | rms=491 | updated_at=1783301951.8903618 | frequency_hz=196.8
- [2026-07-06 09:39:14] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301954.1118011 | source=vosk | rms=491 | updated_at=1783301951.8903618 | frequency_hz=196.8
- [2026-07-06 09:39:14] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301954.1118011 | source=vosk | rms=491 | updated_at=1783301951.8903618 | frequency_hz=196.8
- [2026-07-06 09:39:15] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301955.6403933 | source=vosk | rms=491 | updated_at=1783301951.8903618 | frequency_hz=196.8
- [2026-07-06 09:39:16] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301956.3902268 | source=vosk | rms=543 | updated_at=1783301956.3902268 | frequency_hz=196.8
- [2026-07-06 09:39:18] operator / voice_transcript_partial / voice: cannot fire safety is not aren't
  meta: kind=partial | timestamp=1783301958.6964412 | source=vosk | rms=599 | updated_at=1783301958.640769 | frequency_hz=272.6
- [2026-07-06 09:39:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301958.8900342 | source=vosk | rms=545 | updated_at=1783301958.8900342 | frequency_hz=221.3
- [2026-07-06 09:39:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301959.1404004 | source=vosk | rms=502 | updated_at=1783301959.1404004 | frequency_hz=232.0
- [2026-07-06 09:39:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301959.3904786 | source=vosk | rms=502 | updated_at=1783301959.1404004 | frequency_hz=232.0
- [2026-07-06 09:39:19] operator / voice_transcript_final / voice: cannot fire safety is not aren t
  meta: kind=final | timestamp=1783301959.7391171 | source=final | rms=502 | updated_at=1783301959.1404004 | frequency_hz=232.0
- [2026-07-06 09:39:19] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301959.8894072 | source=vosk | rms=502 | updated_at=1783301959.1404004 | frequency_hz=232.0
- [2026-07-06 09:39:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301959.89044 | source=vosk | rms=466 | updated_at=1783301959.8894072 | frequency_hz=285.2
- [2026-07-06 09:39:22] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301962.18655 | source=vosk | rms=802 | updated_at=1783301961.7206867 | frequency_hz=285.2
- [2026-07-06 09:39:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301962.18655 | source=vosk | rms=739 | updated_at=1783301962.18655 | frequency_hz=285.2
- [2026-07-06 09:39:23] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301963.391254 | source=vosk | rms=792 | updated_at=1783301962.9711921 | frequency_hz=284.8
- [2026-07-06 09:39:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301963.391254 | source=vosk | rms=675 | updated_at=1783301963.391254 | frequency_hz=292.9
- [2026-07-06 09:39:23] operator / voice_transcript_partial / voice: scan on fire safety is
  meta: kind=partial | timestamp=1783301963.4052794 | source=vosk | rms=675 | updated_at=1783301963.391254 | frequency_hz=292.9
- [2026-07-06 09:39:23] operator / voice_transcript_partial / voice: scan on fire safety is not
  meta: kind=partial | timestamp=1783301963.4814756 | source=vosk | rms=572 | updated_at=1783301963.4709277 | frequency_hz=292.9
- [2026-07-06 09:39:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301963.7235785 | source=vosk | rms=561 | updated_at=1783301963.7235785 | frequency_hz=217.0
- [2026-07-06 09:39:23] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301963.970175 | source=vosk | rms=561 | updated_at=1783301963.970175 | frequency_hz=164.9
- [2026-07-06 09:39:23] operator / voice_transcript_partial / voice: scan on fire safety is not aren't
  meta: kind=partial | timestamp=1783301963.9821837 | source=vosk | rms=561 | updated_at=1783301963.970175 | frequency_hz=164.9
- [2026-07-06 09:39:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301964.2203958 | source=vosk | rms=553 | updated_at=1783301964.2203958 | frequency_hz=161.8
- [2026-07-06 09:39:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301964.4709628 | source=vosk | rms=511 | updated_at=1783301964.4709628 | frequency_hz=224.2
- [2026-07-06 09:39:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301964.7199032 | source=vosk | rms=478 | updated_at=1783301964.7199032 | frequency_hz=273.1
- [2026-07-06 09:39:24] operator / voice_transcript_final / voice: his cannot buy his safety is not aren t
  meta: kind=final | timestamp=1783301964.9972684 | source=final | rms=478 | updated_at=1783301964.7199032 | frequency_hz=273.1
- [2026-07-06 09:39:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301965.099915 | source=vosk | rms=420 | updated_at=1783301965.099915 | frequency_hz=303.5
- [2026-07-06 09:39:29] operator / voice_transcript_partial / voice: earlier
  meta: kind=partial | timestamp=1783301969.979846 | source=vosk | rms=2867 | updated_at=1783301969.9709241 | frequency_hz=241.7
- [2026-07-06 09:39:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301970.2209156 | source=vosk | rms=1201 | updated_at=1783301970.2209156 | frequency_hz=208.9
- [2026-07-06 09:39:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301970.4702768 | source=vosk | rms=1201 | updated_at=1783301970.4702768 | frequency_hz=214.2
- [2026-07-06 09:39:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301970.7212074 | source=vosk | rms=555 | updated_at=1783301970.7212074 | frequency_hz=266.6
- [2026-07-06 09:39:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301970.970763 | source=vosk | rms=4822 | updated_at=1783301970.970763 | frequency_hz=266.6
- [2026-07-06 09:39:31] operator / voice_transcript_final / voice: earlier
  meta: kind=final | timestamp=1783301971.8102603 | source=final | rms=4822 | updated_at=1783301970.970763 | frequency_hz=266.6
- [2026-07-06 09:39:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1783301971.8629742 | source=vosk | rms=4822 | updated_at=1783301970.970763 | frequency_hz=266.6
- [2026-07-06 09:39:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301971.8629742 | source=vosk | rms=8454 | updated_at=1783301971.8629742 | frequency_hz=266.6
- [2026-07-06 09:39:32] operator / voice_transcript_partial / voice: close the smart century up
  meta: kind=partial | timestamp=1783301972.24061 | source=vosk | rms=6667 | updated_at=1783301972.2205696 | frequency_hz=316.1
- [2026-07-06 09:39:32] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301972.984549 | source=vosk | rms=1086 | updated_at=1783301972.984549 | frequency_hz=244.7
- [2026-07-06 09:39:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301973.2319956 | source=vosk | rms=699 | updated_at=1783301973.2319956 | frequency_hz=250.1
- [2026-07-06 09:39:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301973.4809294 | source=vosk | rms=1177 | updated_at=1783301973.4809294 | frequency_hz=250.1
- [2026-07-06 09:39:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301973.730872 | source=vosk | rms=1177 | updated_at=1783301973.4809294 | frequency_hz=250.1
- [2026-07-06 09:39:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301973.9846828 | source=vosk | rms=1177 | updated_at=1783301973.4809294 | frequency_hz=250.1
- [2026-07-06 09:39:33] operator / voice_transcript_partial / voice: close the smart century up cannot
  meta: kind=partial | timestamp=1783301973.9962244 | source=vosk | rms=1177 | updated_at=1783301973.4809294 | frequency_hz=250.1
- [2026-07-06 09:39:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301974.2316935 | source=vosk | rms=1177 | updated_at=1783301973.4809294 | frequency_hz=250.1
- [2026-07-06 09:39:34] operator / voice_transcript_partial / voice: close the smart century up cannot fire
  meta: kind=partial | timestamp=1783301974.2398598 | source=vosk | rms=1177 | updated_at=1783301973.4809294 | frequency_hz=250.1
- [2026-07-06 09:39:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301974.4809024 | source=vosk | rms=1177 | updated_at=1783301973.4809294 | frequency_hz=250.1
- [2026-07-06 09:39:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301974.7309082 | source=vosk | rms=1177 | updated_at=1783301973.4809294 | frequency_hz=250.1
- [2026-07-06 09:39:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301974.9811132 | source=vosk | rms=1177 | updated_at=1783301973.4809294 | frequency_hz=250.1
- [2026-07-06 09:39:34] operator / voice_transcript_partial / voice: close the smart century up cannot fire safety
  meta: kind=partial | timestamp=1783301974.9966464 | source=vosk | rms=1177 | updated_at=1783301973.4809294 | frequency_hz=250.1
- [2026-07-06 09:39:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301975.2329192 | source=vosk | rms=1177 | updated_at=1783301973.4809294 | frequency_hz=250.1
- [2026-07-06 09:39:35] operator / voice_transcript_partial / voice: close the smart century up cannot fire safety is
  meta: kind=partial | timestamp=1783301975.2429438 | source=vosk | rms=1177 | updated_at=1783301973.4809294 | frequency_hz=250.1
- [2026-07-06 09:39:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301975.4818227 | source=vosk | rms=1177 | updated_at=1783301973.4809294 | frequency_hz=250.1
- [2026-07-06 09:39:35] operator / voice_transcript_partial / voice: close the smart century up cannot fire safety is not
  meta: kind=partial | timestamp=1783301975.493838 | source=vosk | rms=1177 | updated_at=1783301973.4809294 | frequency_hz=250.1
- [2026-07-06 09:39:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301975.7303476 | source=vosk | rms=1177 | updated_at=1783301973.4809294 | frequency_hz=250.1
- [2026-07-06 09:39:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301975.9805174 | source=vosk | rms=1177 | updated_at=1783301973.4809294 | frequency_hz=250.1
- [2026-07-06 09:39:35] operator / voice_transcript_partial / voice: close the smart century up cannot fire safety is not aren't
  meta: kind=partial | timestamp=1783301975.9920285 | source=vosk | rms=1177 | updated_at=1783301973.4809294 | frequency_hz=250.1
- [2026-07-06 09:39:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301976.4840758 | source=vosk | rms=1177 | updated_at=1783301973.4809294 | frequency_hz=250.1
- [2026-07-06 09:39:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1783301976.985395 | source=vosk | rms=1177 | updated_at=1783301973.4809294 | frequency_hz=250.1

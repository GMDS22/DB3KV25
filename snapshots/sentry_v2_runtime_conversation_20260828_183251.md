# SMART SENTRY V5.0.0 Runtime Conversation Export

- Generated: 2026-08-28 18:32:51
- Entries: 178
- Roles: {'assistant': 3, 'system': 121, 'operator': 54}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 121, 'spoken_confirmation': 1, 'voice_transcript_partial': 42, 'voice_transcript_final': 8, 'voice_command': 4}
- Channels: {'text': 2, 'voice': 176}
- Latest operator request: such reports are connect on the seal
- Latest assistant message: Smart Sentry is ready.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-08-28 18:31:14] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-08-28 18:31:14] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-08-28 18:31:19] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787913079.1872396 | source=vosk
- [2026-08-28 18:31:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913079.7361119 | source=vosk | rms=1200 | updated_at=1787913079.7361119
- [2026-08-28 18:31:21] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913081.1501648 | source=vosk | rms=1200 | updated_at=1787913080.0742605
- [2026-08-28 18:31:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913081.1501648 | source=vosk | rms=1202 | updated_at=1787913081.1501648
- [2026-08-28 18:31:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913091.1621046 | source=vosk | rms=573 | updated_at=1787913090.6610823 | frequency_hz=109.0
- [2026-08-28 18:31:31] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913091.4108994 | source=vosk | rms=1204 | updated_at=1787913091.4108994 | frequency_hz=109.0
- [2026-08-28 18:31:32] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913092.910829 | source=vosk | rms=128 | updated_at=1787913092.41135 | frequency_hz=109.0
- [2026-08-28 18:31:33] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913093.4111001 | source=vosk | rms=1200 | updated_at=1787913093.4111001 | frequency_hz=109.0
- [2026-08-28 18:31:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913099.6608994 | source=vosk | rms=851 | updated_at=1787913099.160735 | frequency_hz=161.9
- [2026-08-28 18:31:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913100.1624706 | source=vosk | rms=1205 | updated_at=1787913100.1624706 | frequency_hz=171.0
- [2026-08-28 18:31:40] assistant / spoken_confirmation / voice: Smart Sentry is ready.
  meta: interrupt=True | assistant_output=False | spoken=True
- [2026-08-28 18:31:40] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913100.6614628 | source=vosk | rms=1205 | updated_at=1787913100.1624706 | frequency_hz=171.0
- [2026-08-28 18:31:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913103.162485 | source=vosk | rms=1200 | updated_at=1787913103.162485 | frequency_hz=171.0
- [2026-08-28 18:31:45] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1787913105.0010653 | source=vosk | rms=1065 | updated_at=1787913104.9214153 | frequency_hz=240.7
- [2026-08-28 18:31:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913105.1716666 | source=vosk | rms=1053 | updated_at=1787913105.1716666 | frequency_hz=240.7
- [2026-08-28 18:31:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913105.4208508 | source=vosk | rms=1053 | updated_at=1787913105.1716666 | frequency_hz=240.7
- [2026-08-28 18:31:45] operator / voice_transcript_partial / voice: smart century is
  meta: kind=partial | timestamp=1787913105.4973001 | source=vosk | rms=1053 | updated_at=1787913105.1716666 | frequency_hz=240.7
- [2026-08-28 18:31:45] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913105.9226162 | source=vosk | rms=1053 | updated_at=1787913105.1716666 | frequency_hz=240.7
- [2026-08-28 18:31:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913111.4214506 | source=vosk | rms=1053 | updated_at=1787913105.1716666 | frequency_hz=240.7
- [2026-08-28 18:31:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913111.6720645 | source=vosk | rms=1009 | updated_at=1787913111.6720645 | frequency_hz=92.0
- [2026-08-28 18:31:51] operator / voice_transcript_partial / voice: smart century is reading
  meta: kind=partial | timestamp=1787913111.722389 | source=vosk | rms=1009 | updated_at=1787913111.6720645 | frequency_hz=92.0
- [2026-08-28 18:31:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913111.9226916 | source=vosk | rms=1009 | updated_at=1787913111.6720645 | frequency_hz=92.0
- [2026-08-28 18:31:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913112.171797 | source=vosk | rms=1009 | updated_at=1787913111.6720645 | frequency_hz=92.0
- [2026-08-28 18:31:52] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913112.4214048 | source=vosk | rms=1037 | updated_at=1787913112.4214048 | frequency_hz=183.0
- [2026-08-28 18:31:52] operator / voice_transcript_final / voice: smart sentry is reading
  meta: kind=final | timestamp=1787913112.8253376 | source=final | rms=1037 | updated_at=1787913112.4214048 | frequency_hz=183.0
- [2026-08-28 18:31:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913113.0438588 | source=vosk | rms=1037 | updated_at=1787913112.4214048 | frequency_hz=183.0
- [2026-08-28 18:31:53] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913113.0438588 | source=vosk | rms=1037 | updated_at=1787913112.4214048 | frequency_hz=183.0
- [2026-08-28 18:31:53] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913113.6725175 | source=vosk | rms=1037 | updated_at=1787913112.4214048 | frequency_hz=183.0
- [2026-08-28 18:31:56] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913116.1723304 | source=vosk | rms=1201 | updated_at=1787913116.1723304 | frequency_hz=274.0
- [2026-08-28 18:31:59] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913119.1715534 | source=vosk | rms=737 | updated_at=1787913118.4215705 | frequency_hz=169.1
- [2026-08-28 18:31:59] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913119.4219997 | source=vosk | rms=1200 | updated_at=1787913119.4219997 | frequency_hz=248.5
- [2026-08-28 18:32:00] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913120.422122 | source=vosk | rms=1201 | updated_at=1787913119.671555 | frequency_hz=248.5
- [2026-08-28 18:32:00] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913120.9230099 | source=vosk | rms=1202 | updated_at=1787913120.9230099 | frequency_hz=241.3
- [2026-08-28 18:32:02] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913122.67147 | source=vosk | rms=1018 | updated_at=1787913122.1716807 | frequency_hz=279.5
- [2026-08-28 18:32:04] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913124.1722085 | source=vosk | rms=740 | updated_at=1787913124.1722085 | frequency_hz=188.0
- [2026-08-28 18:32:06] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1787913126.2350495 | source=vosk | rms=1200 | updated_at=1787913126.1714165 | frequency_hz=219.3
- [2026-08-28 18:32:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913126.4232283 | source=vosk | rms=1200 | updated_at=1787913126.1714165 | frequency_hz=219.3
- [2026-08-28 18:32:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913126.6720092 | source=vosk | rms=1200 | updated_at=1787913126.6720092 | frequency_hz=188.7
- [2026-08-28 18:32:06] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913126.9217055 | source=vosk | rms=6759 | updated_at=1787913126.9217055 | frequency_hz=188.7
- [2026-08-28 18:32:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913127.1720083 | source=vosk | rms=5578 | updated_at=1787913127.1720083 | frequency_hz=188.7
- [2026-08-28 18:32:07] operator / voice_transcript_partial / voice: everyone runs
  meta: kind=partial | timestamp=1787913127.199863 | source=vosk | rms=5578 | updated_at=1787913127.1720083 | frequency_hz=188.7
- [2026-08-28 18:32:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913127.4219084 | source=vosk | rms=3774 | updated_at=1787913127.4219084 | frequency_hz=188.7
- [2026-08-28 18:32:07] operator / voice_transcript_partial / voice: alien run the
  meta: kind=partial | timestamp=1787913127.4964802 | source=vosk | rms=3774 | updated_at=1787913127.4219084 | frequency_hz=188.7
- [2026-08-28 18:32:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913127.6721551 | source=vosk | rms=4327 | updated_at=1787913127.6721551 | frequency_hz=188.7
- [2026-08-28 18:32:07] operator / voice_transcript_partial / voice: alien run the smart
  meta: kind=partial | timestamp=1787913127.6922042 | source=vosk | rms=4327 | updated_at=1787913127.6721551 | frequency_hz=188.7
- [2026-08-28 18:32:07] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913127.9220252 | source=vosk | rms=2814 | updated_at=1787913127.9220252 | frequency_hz=188.7
- [2026-08-28 18:32:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913128.172322 | source=vosk | rms=1200 | updated_at=1787913128.172322 | frequency_hz=168.9
- [2026-08-28 18:32:08] operator / voice_transcript_partial / voice: alien run the smart century
  meta: kind=partial | timestamp=1787913128.1878538 | source=vosk | rms=1200 | updated_at=1787913128.172322 | frequency_hz=168.9
- [2026-08-28 18:32:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913128.4214199 | source=vosk | rms=1200 | updated_at=1787913128.4214199 | frequency_hz=170.0
- [2026-08-28 18:32:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913128.6723363 | source=vosk | rms=1201 | updated_at=1787913128.6723363 | frequency_hz=179.1
- [2026-08-28 18:32:08] operator / voice_transcript_final / voice: connect boards and enable smart sentry
  meta: kind=final | timestamp=1787913128.6833646 | source=final | rms=1201 | updated_at=1787913128.6723363 | frequency_hz=179.1
- [2026-08-28 18:32:08] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787913128.7159746 | source=state | rms=1201 | updated_at=1787913128.6723363 | frequency_hz=179.1
- [2026-08-28 18:32:08] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913128.7159746 | source=state | rms=1201 | updated_at=1787913128.6723363 | frequency_hz=179.1
- [2026-08-28 18:32:41] operator / voice_command / voice: connect boards and enable smart sentry
  meta: normalized=True
- [2026-08-28 18:32:08] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913128.9220557 | source=vosk | rms=1201 | updated_at=1787913128.6723363 | frequency_hz=179.1
- [2026-08-28 18:32:10] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913130.1720436 | source=vosk | rms=1204 | updated_at=1787913129.1719306 | frequency_hz=179.1
- [2026-08-28 18:32:11] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913131.1716638 | source=vosk | rms=1204 | updated_at=1787913129.1719306 | frequency_hz=179.1
- [2026-08-28 18:32:11] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913131.6721315 | source=vosk | rms=1204 | updated_at=1787913129.1719306 | frequency_hz=179.1
- [2026-08-28 18:32:15] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913135.1717885 | source=vosk | rms=1204 | updated_at=1787913129.1719306 | frequency_hz=179.1
- [2026-08-28 18:32:16] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913136.9227011 | source=vosk | rms=1182 | updated_at=1787913136.4225502 | frequency_hz=179.1
- [2026-08-28 18:32:18] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913138.4221044 | source=vosk | rms=1001 | updated_at=1787913138.4221044 | frequency_hz=179.1
- [2026-08-28 18:32:19] operator / voice_transcript_partial / voice: my sense
  meta: kind=partial | timestamp=1787913139.4530773 | source=vosk | rms=1001 | updated_at=1787913138.4221044 | frequency_hz=179.1
- [2026-08-28 18:32:19] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913139.9223175 | source=vosk | rms=1200 | updated_at=1787913139.9223175 | frequency_hz=179.1
- [2026-08-28 18:32:20] operator / voice_transcript_partial / voice: smart such
  meta: kind=partial | timestamp=1787913140.0199318 | source=vosk | rms=1200 | updated_at=1787913139.9223175 | frequency_hz=179.1
- [2026-08-28 18:32:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913140.1722932 | source=vosk | rms=1200 | updated_at=1787913140.1722932 | frequency_hz=179.1
- [2026-08-28 18:32:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913140.4223437 | source=vosk | rms=2648 | updated_at=1787913140.4223437 | frequency_hz=179.1
- [2026-08-28 18:32:20] operator / voice_transcript_final / voice: smart sense
  meta: kind=final | timestamp=1787913140.6345413 | source=final | rms=2648 | updated_at=1787913140.4223437 | frequency_hz=179.1
- [2026-08-28 18:32:20] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913140.6726825 | source=vosk | rms=3881 | updated_at=1787913140.6726825 | frequency_hz=179.1
- [2026-08-28 18:32:21] operator / voice_transcript_partial / voice: elliott
  meta: kind=partial | timestamp=1787913141.1826794 | source=vosk | rms=1200 | updated_at=1787913140.922988 | frequency_hz=179.1
- [2026-08-28 18:32:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913141.422745 | source=vosk | rms=1200 | updated_at=1787913140.922988 | frequency_hz=179.1
- [2026-08-28 18:32:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913141.6724374 | source=vosk | rms=1200 | updated_at=1787913140.922988 | frequency_hz=179.1
- [2026-08-28 18:32:21] operator / voice_transcript_partial / voice: elliott said
  meta: kind=partial | timestamp=1787913141.7129483 | source=vosk | rms=1200 | updated_at=1787913140.922988 | frequency_hz=179.1
- [2026-08-28 18:32:21] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913141.923947 | source=vosk | rms=1200 | updated_at=1787913140.922988 | frequency_hz=179.1
- [2026-08-28 18:32:21] operator / voice_transcript_partial / voice: elliott such
  meta: kind=partial | timestamp=1787913141.94816 | source=vosk | rms=1200 | updated_at=1787913140.922988 | frequency_hz=179.1
- [2026-08-28 18:32:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913142.1730306 | source=vosk | rms=1200 | updated_at=1787913142.1730306 | frequency_hz=223.5
- [2026-08-28 18:32:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913142.4229865 | source=vosk | rms=1200 | updated_at=1787913142.4229865 | frequency_hz=223.5
- [2026-08-28 18:32:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913142.6738918 | source=vosk | rms=1201 | updated_at=1787913142.6738918 | frequency_hz=223.5
- [2026-08-28 18:32:22] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787913142.9860687 | source=state | rms=1201 | updated_at=1787913142.6738918 | frequency_hz=223.5
- [2026-08-28 18:32:22] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1787913142.9875717 | source=final | rms=1201 | updated_at=1787913142.6738918 | frequency_hz=223.5
- [2026-08-28 18:32:41] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-08-28 18:32:22] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913142.9875717 | source=vosk | rms=1204 | updated_at=1787913142.9875717 | frequency_hz=223.5
- [2026-08-28 18:32:24] operator / voice_transcript_partial / voice: that's probably
  meta: kind=partial | timestamp=1787913144.4909222 | source=vosk | rms=1205 | updated_at=1787913144.172904 | frequency_hz=223.5
- [2026-08-28 18:32:24] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913144.6725013 | source=vosk | rms=1205 | updated_at=1787913144.172904 | frequency_hz=223.5
- [2026-08-28 18:32:25] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787913145.2856002 | source=state | rms=1202 | updated_at=1787913145.2409403 | frequency_hz=223.5
- [2026-08-28 18:32:25] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913145.2856002 | source=state | rms=1202 | updated_at=1787913145.2409403 | frequency_hz=223.5
- [2026-08-28 18:32:25] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913145.422355 | source=vosk | rms=1201 | updated_at=1787913145.422355 | frequency_hz=223.5
- [2026-08-28 18:32:26] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913146.6723526 | source=vosk | rms=1202 | updated_at=1787913146.172969 | frequency_hz=223.5
- [2026-08-28 18:32:28] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913148.4233906 | source=vosk | rms=1202 | updated_at=1787913146.172969 | frequency_hz=223.5
- [2026-08-28 18:32:28] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913148.9225042 | source=vosk | rms=1202 | updated_at=1787913146.172969 | frequency_hz=223.5
- [2026-08-28 18:32:29] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913149.1727834 | source=vosk | rms=1202 | updated_at=1787913146.172969 | frequency_hz=223.5
- [2026-08-28 18:32:29] operator / voice_transcript_partial / voice: arts
  meta: kind=partial | timestamp=1787913149.2346554 | source=vosk | rms=1202 | updated_at=1787913146.172969 | frequency_hz=223.5
- [2026-08-28 18:32:29] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913149.6727643 | source=vosk | rms=1202 | updated_at=1787913146.172969 | frequency_hz=223.5
- [2026-08-28 18:32:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913150.1727488 | source=vosk | rms=1202 | updated_at=1787913146.172969 | frequency_hz=223.5
- [2026-08-28 18:32:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913150.4223564 | source=vosk | rms=1202 | updated_at=1787913146.172969 | frequency_hz=223.5
- [2026-08-28 18:32:30] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913150.6722996 | source=vosk | rms=1202 | updated_at=1787913146.172969 | frequency_hz=223.5
- [2026-08-28 18:32:30] operator / voice_transcript_partial / voice: as far as
  meta: kind=partial | timestamp=1787913150.7297466 | source=vosk | rms=1202 | updated_at=1787913146.172969 | frequency_hz=223.5
- [2026-08-28 18:32:31] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913151.1737237 | source=vosk | rms=1202 | updated_at=1787913146.172969 | frequency_hz=223.5
- [2026-08-28 18:32:32] operator / voice_transcript_final / voice: as far as
  meta: kind=final | timestamp=1787913152.6590738 | source=final | rms=1202 | updated_at=1787913146.172969 | frequency_hz=223.5
- [2026-08-28 18:32:34] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913154.9223523 | source=vosk | rms=1201 | updated_at=1787913154.9223523 | frequency_hz=223.5
- [2026-08-28 18:32:35] operator / voice_transcript_partial / voice: arts ask another
  meta: kind=partial | timestamp=1787913155.0484543 | source=vosk | rms=1201 | updated_at=1787913154.9223523 | frequency_hz=223.5
- [2026-08-28 18:32:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913155.1730778 | source=vosk | rms=1202 | updated_at=1787913155.1730778 | frequency_hz=223.5
- [2026-08-28 18:32:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913155.4229228 | source=vosk | rms=1202 | updated_at=1787913155.1730778 | frequency_hz=223.5
- [2026-08-28 18:32:35] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913155.9222481 | source=vosk | rms=1202 | updated_at=1787913155.1730778 | frequency_hz=223.5
- [2026-08-28 18:32:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913156.1728342 | source=vosk | rms=1204 | updated_at=1787913156.1728342 | frequency_hz=223.5
- [2026-08-28 18:32:36] operator / voice_transcript_final / voice: as far as arts ask others
  meta: kind=final | timestamp=1787913156.5359588 | source=final | rms=1204 | updated_at=1787913156.1728342 | frequency_hz=223.5
- [2026-08-28 18:32:36] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913156.698552 | source=vosk | rms=1204 | updated_at=1787913156.1728342 | frequency_hz=223.5
- [2026-08-28 18:32:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913156.698552 | source=vosk | rms=1120 | updated_at=1787913156.698552 | frequency_hz=223.5
- [2026-08-28 18:32:36] operator / voice_transcript_partial / voice: please
  meta: kind=partial | timestamp=1787913156.7324858 | source=vosk | rms=1120 | updated_at=1787913156.698552 | frequency_hz=223.5
- [2026-08-28 18:32:36] operator / voice_transcript_partial / voice: please try
  meta: kind=partial | timestamp=1787913156.7526305 | source=vosk | rms=1206 | updated_at=1787913156.7324858 | frequency_hz=223.5
- [2026-08-28 18:32:36] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913156.9239109 | source=vosk | rms=1886 | updated_at=1787913156.9239109 | frequency_hz=223.5
- [2026-08-28 18:32:36] operator / voice_transcript_partial / voice: please try again
  meta: kind=partial | timestamp=1787913156.9603863 | source=vosk | rms=1886 | updated_at=1787913156.9239109 | frequency_hz=223.5
- [2026-08-28 18:32:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913157.1732125 | source=vosk | rms=4636 | updated_at=1787913157.1732125 | frequency_hz=223.5
- [2026-08-28 18:32:37] operator / voice_transcript_partial / voice: please try to get
  meta: kind=partial | timestamp=1787913157.196341 | source=vosk | rms=4636 | updated_at=1787913157.1732125 | frequency_hz=223.5
- [2026-08-28 18:32:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913157.4240031 | source=vosk | rms=5342 | updated_at=1787913157.4240031 | frequency_hz=223.5
- [2026-08-28 18:32:37] operator / voice_transcript_partial / voice: please try to open
  meta: kind=partial | timestamp=1787913157.4725046 | source=vosk | rms=5342 | updated_at=1787913157.4240031 | frequency_hz=223.5
- [2026-08-28 18:32:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913157.6739328 | source=vosk | rms=3079 | updated_at=1787913157.6739328 | frequency_hz=223.5
- [2026-08-28 18:32:37] operator / voice_transcript_partial / voice: please try to open the
  meta: kind=partial | timestamp=1787913157.6981459 | source=vosk | rms=3079 | updated_at=1787913157.6739328 | frequency_hz=223.5
- [2026-08-28 18:32:37] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913157.9227118 | source=vosk | rms=1721 | updated_at=1787913157.9227118 | frequency_hz=209.0
- [2026-08-28 18:32:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913158.173442 | source=vosk | rms=1200 | updated_at=1787913158.173442 | frequency_hz=209.0
- [2026-08-28 18:32:38] operator / voice_transcript_partial / voice: please try to open the camera
  meta: kind=partial | timestamp=1787913158.1921685 | source=vosk | rms=1200 | updated_at=1787913158.173442 | frequency_hz=209.0
- [2026-08-28 18:32:38] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913158.6727848 | source=vosk | rms=1200 | updated_at=1787913158.173442 | frequency_hz=209.0
- [2026-08-28 18:32:38] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913158.9222884 | source=vosk | rms=1201 | updated_at=1787913158.9222884 | frequency_hz=209.0
- [2026-08-28 18:32:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913159.1725383 | source=vosk | rms=1200 | updated_at=1787913159.1725383 | frequency_hz=209.0
- [2026-08-28 18:32:39] operator / voice_transcript_final / voice: open camera
  meta: kind=final | timestamp=1787913159.187074 | source=final | rms=1200 | updated_at=1787913159.1725383 | frequency_hz=209.0
- [2026-08-28 18:32:39] system / voice_status / voice: processing
  meta: kind=status | timestamp=1787913159.219007 | source=state | rms=1200 | updated_at=1787913159.1725383 | frequency_hz=209.0
- [2026-08-28 18:32:39] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913159.219007 | source=state | rms=1200 | updated_at=1787913159.1725383 | frequency_hz=209.0
- [2026-08-28 18:32:41] operator / voice_command / voice: open camera
  meta: normalized=True
- [2026-08-28 18:32:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913159.4231498 | source=vosk | rms=1200 | updated_at=1787913159.4231498 | frequency_hz=209.0
- [2026-08-28 18:32:39] operator / voice_transcript_partial / voice: why
  meta: kind=partial | timestamp=1787913159.7012715 | source=vosk | rms=1200 | updated_at=1787913159.4231498 | frequency_hz=209.0
- [2026-08-28 18:32:39] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913159.9239445 | source=vosk | rms=1200 | updated_at=1787913159.4231498 | frequency_hz=209.0
- [2026-08-28 18:32:40] operator / voice_transcript_partial / voice: sentry
  meta: kind=partial | timestamp=1787913160.02761 | source=vosk | rms=1200 | updated_at=1787913159.4231498 | frequency_hz=209.0
- [2026-08-28 18:32:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913160.1731029 | source=vosk | rms=1200 | updated_at=1787913159.4231498 | frequency_hz=209.0
- [2026-08-28 18:32:40] operator / voice_transcript_partial / voice: such reports
  meta: kind=partial | timestamp=1787913160.189253 | source=vosk | rms=1200 | updated_at=1787913159.4231498 | frequency_hz=209.0
- [2026-08-28 18:32:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913160.4230945 | source=vosk | rms=1200 | updated_at=1787913159.4231498 | frequency_hz=209.0
- [2026-08-28 18:32:40] operator / voice_transcript_partial / voice: such reports are
  meta: kind=partial | timestamp=1787913160.4411075 | source=vosk | rms=1200 | updated_at=1787913159.4231498 | frequency_hz=209.0
- [2026-08-28 18:32:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913160.6733487 | source=vosk | rms=1200 | updated_at=1787913159.4231498 | frequency_hz=209.0
- [2026-08-28 18:32:40] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913160.9234526 | source=vosk | rms=1200 | updated_at=1787913159.4231498 | frequency_hz=209.0
- [2026-08-28 18:32:40] operator / voice_transcript_partial / voice: such reports are connected
  meta: kind=partial | timestamp=1787913160.9485376 | source=vosk | rms=1200 | updated_at=1787913159.4231498 | frequency_hz=209.0
- [2026-08-28 18:32:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913161.1757038 | source=vosk | rms=1200 | updated_at=1787913159.4231498 | frequency_hz=209.0
- [2026-08-28 18:32:41] operator / voice_transcript_partial / voice: such reports are connected on the
  meta: kind=partial | timestamp=1787913161.1883247 | source=vosk | rms=1200 | updated_at=1787913159.4231498 | frequency_hz=209.0
- [2026-08-28 18:32:41] operator / voice_command / voice: as far as
  meta: normalized=True
- [2026-08-28 18:32:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913161.4225812 | source=vosk | rms=1202 | updated_at=1787913161.4225812 | frequency_hz=209.0
- [2026-08-28 18:32:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913161.6719038 | source=vosk | rms=1203 | updated_at=1787913161.6719038 | frequency_hz=209.0
- [2026-08-28 18:32:41] operator / voice_transcript_partial / voice: such reports are connected on this
  meta: kind=partial | timestamp=1787913161.7157753 | source=vosk | rms=1203 | updated_at=1787913161.6719038 | frequency_hz=209.0
- [2026-08-28 18:32:41] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913161.9231281 | source=vosk | rms=1201 | updated_at=1787913161.9231281 | frequency_hz=209.0
- [2026-08-28 18:32:42] operator / voice_transcript_partial / voice: such reports are connected on the ceo and
  meta: kind=partial | timestamp=1787913162.0028188 | source=vosk | rms=1201 | updated_at=1787913161.9231281 | frequency_hz=209.0
- [2026-08-28 18:32:42] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913162.1730142 | source=vosk | rms=1200 | updated_at=1787913162.1730142 | frequency_hz=209.0
- [2026-08-28 18:32:42] operator / voice_transcript_final / voice: such reports are connect on the seal
  meta: kind=final | timestamp=1787913162.5437908 | source=final | rms=1200 | updated_at=1787913162.1730142 | frequency_hz=209.0
- [2026-08-28 18:32:43] system / voice_status / voice: idle
  meta: kind=status | timestamp=1787913163.579548 | source=vosk | rms=1200 | updated_at=1787913162.1730142 | frequency_hz=209.0
- [2026-08-28 18:32:43] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913163.579548 | source=vosk | rms=1200 | updated_at=1787913163.579548 | frequency_hz=209.0
- [2026-08-28 18:32:43] system / voice_status / voice: listening
  meta: kind=status | timestamp=1787913163.8685179 | source=state | rms=914 | updated_at=1787913163.6440413 | frequency_hz=209.0
- [2026-08-28 18:32:44] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913164.6726964 | source=vosk | rms=1153 | updated_at=1787913164.6726964 | frequency_hz=209.0
- [2026-08-28 18:32:45] operator / voice_transcript_partial / voice: ask another
  meta: kind=partial | timestamp=1787913165.4419305 | source=vosk | rms=981 | updated_at=1787913165.4228308 | frequency_hz=209.0
- [2026-08-28 18:32:45] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913165.6774724 | source=vosk | rms=764 | updated_at=1787913165.6774724 | frequency_hz=209.0
- [2026-08-28 18:32:45] operator / voice_transcript_partial / voice: ask another question
  meta: kind=partial | timestamp=1787913165.6965451 | source=vosk | rms=764 | updated_at=1787913165.6774724 | frequency_hz=209.0
- [2026-08-28 18:32:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913166.172789 | source=vosk | rms=887 | updated_at=1787913166.172789 | frequency_hz=209.0
- [2026-08-28 18:32:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913166.422741 | source=vosk | rms=1053 | updated_at=1787913166.422741 | frequency_hz=209.0
- [2026-08-28 18:32:46] operator / voice_transcript_partial / voice: ask another question was
  meta: kind=partial | timestamp=1787913166.4438362 | source=vosk | rms=1053 | updated_at=1787913166.422741 | frequency_hz=209.0
- [2026-08-28 18:32:46] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913166.673981 | source=vosk | rms=884 | updated_at=1787913166.673981 | frequency_hz=209.0
- [2026-08-28 18:32:46] operator / voice_transcript_partial / voice: ask another question work in
  meta: kind=partial | timestamp=1787913166.7190495 | source=vosk | rms=884 | updated_at=1787913166.673981 | frequency_hz=209.0
- [2026-08-28 18:32:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913167.2215772 | source=vosk | rms=884 | updated_at=1787913166.673981 | frequency_hz=209.0
- [2026-08-28 18:32:47] operator / voice_transcript_partial / voice: ask another question work in another country
  meta: kind=partial | timestamp=1787913167.4145973 | source=vosk | rms=884 | updated_at=1787913166.673981 | frequency_hz=209.0
- [2026-08-28 18:32:47] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913167.6953351 | source=vosk | rms=884 | updated_at=1787913166.673981 | frequency_hz=209.0
- [2026-08-28 18:32:47] operator / voice_transcript_partial / voice: ask another question work in another country and
  meta: kind=partial | timestamp=1787913167.6953351 | source=vosk | rms=884 | updated_at=1787913166.673981 | frequency_hz=209.0
- [2026-08-28 18:32:48] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913168.5262768 | source=vosk | rms=1029 | updated_at=1787913168.5262768 | frequency_hz=209.0
- [2026-08-28 18:32:48] operator / voice_transcript_partial / voice: ask another question or get another coming around
  meta: kind=partial | timestamp=1787913168.585501 | source=vosk | rms=1029 | updated_at=1787913168.5262768 | frequency_hz=209.0
- [2026-08-28 18:32:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913169.0260181 | source=vosk | rms=1201 | updated_at=1787913169.0260181 | frequency_hz=209.0
- [2026-08-28 18:32:49] operator / voice_transcript_partial / voice: ask another question or get another camaro
  meta: kind=partial | timestamp=1787913169.0896497 | source=vosk | rms=1201 | updated_at=1787913169.0260181 | frequency_hz=209.0
- [2026-08-28 18:32:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913169.2126062 | source=vosk | rms=1201 | updated_at=1787913169.0260181 | frequency_hz=209.0
- [2026-08-28 18:32:49] operator / voice_transcript_partial / voice: ask another question or get another camaro smart
  meta: kind=partial | timestamp=1787913169.2468073 | source=vosk | rms=1201 | updated_at=1787913169.0260181 | frequency_hz=209.0
- [2026-08-28 18:32:49] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913169.71292 | source=vosk | rms=1201 | updated_at=1787913169.0260181 | frequency_hz=209.0
- [2026-08-28 18:32:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913170.0186744 | source=vosk | rms=1201 | updated_at=1787913169.0260181 | frequency_hz=209.0
- [2026-08-28 18:32:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913170.213095 | source=vosk | rms=1201 | updated_at=1787913169.0260181 | frequency_hz=209.0
- [2026-08-28 18:32:50] operator / voice_transcript_partial / voice: ask another question or get another camaro smart separates
  meta: kind=partial | timestamp=1787913170.2405882 | source=vosk | rms=1201 | updated_at=1787913169.0260181 | frequency_hz=209.0
- [2026-08-28 18:32:50] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913170.7126954 | source=vosk | rms=1201 | updated_at=1787913169.0260181 | frequency_hz=209.0
- [2026-08-28 18:32:51] system / voice_status / voice: hearing
  meta: kind=status | timestamp=1787913171.0316656 | source=vosk | rms=1201 | updated_at=1787913169.0260181 | frequency_hz=209.0

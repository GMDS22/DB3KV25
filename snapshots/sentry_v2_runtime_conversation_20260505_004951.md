# SMART SENTRY V3.5.3 Runtime Conversation Export

- Generated: 2026-05-05 00:49:51
- Entries: 1194
- Roles: {'assistant': 89, 'system': 1, 'operator': 1104}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 7, 'voice_status': 1, 'spoken_confirmation': 78, 'voice_transcript_partial': 806, 'voice_transcript_final': 165, 'voice_command': 133, 'spoken_reply': 3}
- Channels: {'text': 8, 'voice': 1186}
- Latest operator request: what do unk
- Latest assistant message: Received. I started your background analysis about the board same status what in the background.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-05 00:34:40] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 00:34:40] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-05 00:34:41] system / voice_status / voice: listening
  meta: kind=status | timestamp=1777912481.7184353 | source=vosk
- [2026-05-05 00:34:43] assistant / spoken_confirmation / voice: System online and listening. Do you want me to connect boards, enable sentry, or run another task?
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:34:51] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777912491.7509992 | source=vosk | frequency_hz=301.5 | rms=247 | updated_at=1777912488.490931
- [2026-05-05 00:34:52] operator / voice_transcript_final / voice: do
  meta: kind=final | timestamp=1777912492.6458895 | source=final | frequency_hz=301.5 | rms=247 | updated_at=1777912488.490931
- [2026-05-05 00:34:52] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777912492.6527421 | source=vosk | frequency_hz=301.5 | rms=247 | updated_at=1777912488.490931
- [2026-05-05 00:34:52] operator / voice_transcript_partial / voice: do response
  meta: kind=partial | timestamp=1777912492.659255 | source=vosk | frequency_hz=301.5 | rms=247 | updated_at=1777912488.490931
- [2026-05-05 00:34:52] operator / voice_transcript_partial / voice: do you status
  meta: kind=partial | timestamp=1777912492.9043407 | source=vosk | frequency_hz=301.5 | rms=247 | updated_at=1777912488.490931
- [2026-05-05 00:34:53] operator / voice_transcript_partial / voice: do it
  meta: kind=partial | timestamp=1777912493.1541715 | source=vosk | frequency_hz=301.5 | rms=247 | updated_at=1777912488.490931
- [2026-05-05 00:34:53] operator / voice_transcript_final / voice: do it
  meta: kind=final | timestamp=1777912493.8012028 | source=final | frequency_hz=348.0 | rms=858 | updated_at=1777912493.3977716
- [2026-05-05 00:34:54] operator / voice_transcript_partial / voice: again
  meta: kind=partial | timestamp=1777912494.9034274 | source=vosk | frequency_hz=348.0 | rms=858 | updated_at=1777912493.3977716
- [2026-05-05 00:34:55] operator / voice_transcript_partial / voice: eileen decrease
  meta: kind=partial | timestamp=1777912495.1542187 | source=vosk | frequency_hz=348.0 | rms=858 | updated_at=1777912493.3977716
- [2026-05-05 00:34:55] operator / voice_transcript_partial / voice: eileen connect
  meta: kind=partial | timestamp=1777912495.4040236 | source=vosk | frequency_hz=348.0 | rms=858 | updated_at=1777912493.3977716
- [2026-05-05 00:34:55] operator / voice_transcript_partial / voice: eileen connect the
  meta: kind=partial | timestamp=1777912495.6542757 | source=vosk | frequency_hz=348.0 | rms=858 | updated_at=1777912493.3977716
- [2026-05-05 00:34:55] operator / voice_transcript_partial / voice: eileen connect the boards
  meta: kind=partial | timestamp=1777912495.9042351 | source=vosk | frequency_hz=348.0 | rms=858 | updated_at=1777912493.3977716
- [2026-05-05 00:34:56] operator / voice_transcript_partial / voice: eileen connect the boards enable
  meta: kind=partial | timestamp=1777912496.4030144 | source=vosk | frequency_hz=348.0 | rms=858 | updated_at=1777912493.3977716
- [2026-05-05 00:34:56] operator / voice_transcript_partial / voice: eileen connect the boards enable smart
  meta: kind=partial | timestamp=1777912496.6529038 | source=vosk | frequency_hz=348.0 | rms=858 | updated_at=1777912493.3977716
- [2026-05-05 00:34:56] operator / voice_transcript_partial / voice: eileen connect the boards enable sentry
  meta: kind=partial | timestamp=1777912496.9023747 | source=vosk | frequency_hz=372.0 | rms=265 | updated_at=1777912496.8978605
- [2026-05-05 00:34:57] operator / voice_transcript_partial / voice: eileen connect the boards enable sentry run diagnostics
  meta: kind=partial | timestamp=1777912497.9065526 | source=vosk | frequency_hz=372.0 | rms=265 | updated_at=1777912496.8978605
- [2026-05-05 00:34:58] operator / voice_transcript_partial / voice: eileen connect the boards enable sentry run connect
  meta: kind=partial | timestamp=1777912498.1540968 | source=vosk | frequency_hz=372.0 | rms=265 | updated_at=1777912496.8978605
- [2026-05-05 00:34:58] operator / voice_transcript_partial / voice: eileen connect the boards enable sentry run disconnect
  meta: kind=partial | timestamp=1777912498.4042356 | source=vosk | frequency_hz=372.0 | rms=265 | updated_at=1777912496.8978605
- [2026-05-05 00:34:58] operator / voice_transcript_partial / voice: eileen connect the boards enable sentry run who are you do
  meta: kind=partial | timestamp=1777912498.6563344 | source=vosk | frequency_hz=372.0 | rms=265 | updated_at=1777912496.8978605
- [2026-05-05 00:34:58] operator / voice_transcript_partial / voice: eileen connect the boards enable sentry run alion
  meta: kind=partial | timestamp=1777912498.9037852 | source=vosk | frequency_hz=372.0 | rms=265 | updated_at=1777912496.8978605
- [2026-05-05 00:35:16] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:34:59] operator / voice_transcript_partial / voice: eileen connect the boards enable sentry run alion e lion
  meta: kind=partial | timestamp=1777912499.1536915 | source=vosk | frequency_hz=372.0 | rms=265 | updated_at=1777912496.8978605
- [2026-05-05 00:34:59] operator / voice_transcript_partial / voice: eileen connect the boards enable sentry run who are you do
  meta: kind=partial | timestamp=1777912499.4023175 | source=vosk | frequency_hz=372.0 | rms=265 | updated_at=1777912496.8978605
- [2026-05-05 00:34:59] operator / voice_transcript_partial / voice: eileen connect the boards enable sentry run who are you do it
  meta: kind=partial | timestamp=1777912499.9040132 | source=vosk | frequency_hz=372.0 | rms=265 | updated_at=1777912496.8978605
- [2026-05-05 00:35:00] operator / voice_transcript_final / voice: connect boards
  meta: kind=final | timestamp=1777912500.4057212 | source=final | frequency_hz=372.0 | rms=265 | updated_at=1777912496.8978605
- [2026-05-05 00:35:16] operator / voice_command / voice: connect boards
  meta: normalized=True
- [2026-05-05 00:35:00] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777912500.652127 | source=vosk | frequency_hz=372.0 | rms=265 | updated_at=1777912496.8978605
- [2026-05-05 00:35:00] operator / voice_transcript_partial / voice: be
  meta: kind=partial | timestamp=1777912500.9020529 | source=vosk | frequency_hz=372.0 | rms=265 | updated_at=1777912496.8978605
- [2026-05-05 00:35:02] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777912502.239642 | source=vosk | frequency_hz=372.0 | rms=265 | updated_at=1777912496.8978605
- [2026-05-05 00:35:03] operator / voice_transcript_partial / voice: [unk] e
  meta: kind=partial | timestamp=1777912503.244888 | source=vosk | frequency_hz=372.0 | rms=265 | updated_at=1777912496.8978605
- [2026-05-05 00:35:03] operator / voice_transcript_partial / voice: [unk] e last
  meta: kind=partial | timestamp=1777912503.4966524 | source=vosk | frequency_hz=372.0 | rms=265 | updated_at=1777912496.8978605
- [2026-05-05 00:35:03] operator / voice_transcript_partial / voice: [unk] e lion brightness
  meta: kind=partial | timestamp=1777912503.7466934 | source=vosk | frequency_hz=372.0 | rms=265 | updated_at=1777912496.8978605
- [2026-05-05 00:35:16] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:35:03] operator / voice_transcript_partial / voice: [unk] e lion enable
  meta: kind=partial | timestamp=1777912503.9979212 | source=vosk | frequency_hz=308.0 | rms=255 | updated_at=1777912503.9900305
- [2026-05-05 00:35:04] operator / voice_transcript_partial / voice: [unk] e lion behavior
  meta: kind=partial | timestamp=1777912504.2498324 | source=vosk | frequency_hz=292.6 | rms=253 | updated_at=1777912504.2402961
- [2026-05-05 00:35:04] operator / voice_transcript_final / voice: unk behavior
  meta: kind=final | timestamp=1777912504.6597407 | source=final | frequency_hz=292.6 | rms=253 | updated_at=1777912504.2402961
- [2026-05-05 00:35:16] operator / voice_command / voice: unk behavior
  meta: normalized=True
- [2026-05-05 00:35:04] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777912504.994122 | source=vosk | frequency_hz=292.6 | rms=253 | updated_at=1777912504.2402961
- [2026-05-05 00:35:05] operator / voice_transcript_partial / voice: connect anything
  meta: kind=partial | timestamp=1777912505.4967616 | source=vosk | frequency_hz=310.6 | rms=271 | updated_at=1777912505.489742
- [2026-05-05 00:35:05] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777912505.8600123 | source=vosk | frequency_hz=292.9 | rms=255 | updated_at=1777912505.7399807
- [2026-05-05 00:35:06] operator / voice_transcript_partial / voice: connect alien connect
  meta: kind=partial | timestamp=1777912506.7467566 | source=vosk | frequency_hz=294.4 | rms=261 | updated_at=1777912506.2396586
- [2026-05-05 00:35:06] operator / voice_transcript_partial / voice: anything be e
  meta: kind=partial | timestamp=1777912506.996476 | source=vosk | frequency_hz=294.4 | rms=261 | updated_at=1777912506.2396586
- [2026-05-05 00:35:07] operator / voice_transcript_partial / voice: anything be more
  meta: kind=partial | timestamp=1777912507.246065 | source=vosk | frequency_hz=294.4 | rms=261 | updated_at=1777912506.2396586
- [2026-05-05 00:35:07] operator / voice_transcript_partial / voice: anything be enable
  meta: kind=partial | timestamp=1777912507.494528 | source=vosk | frequency_hz=294.4 | rms=261 | updated_at=1777912506.2396586
- [2026-05-05 00:35:07] operator / voice_transcript_partial / voice: anything be enable and enable
  meta: kind=partial | timestamp=1777912507.7478862 | source=vosk | frequency_hz=294.4 | rms=261 | updated_at=1777912506.2396586
- [2026-05-05 00:35:08] operator / voice_transcript_final / voice: connect be enable and enable
  meta: kind=final | timestamp=1777912508.7505586 | source=final | frequency_hz=240.1 | rms=262 | updated_at=1777912508.7405388
- [2026-05-05 00:35:16] operator / voice_command / voice: connect be enable and enable
  meta: normalized=True
- [2026-05-05 00:35:09] operator / voice_transcript_partial / voice: anything
  meta: kind=partial | timestamp=1777912509.9951963 | source=vosk | frequency_hz=240.1 | rms=262 | updated_at=1777912508.7405388
- [2026-05-05 00:35:10] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777912510.2495782 | source=vosk | frequency_hz=260.0 | rms=259 | updated_at=1777912510.2399652
- [2026-05-05 00:35:13] operator / voice_transcript_partial / voice: behavior more
  meta: kind=partial | timestamp=1777912513.24601 | source=vosk | frequency_hz=295.9 | rms=263 | updated_at=1777912512.49036
- [2026-05-05 00:35:13] operator / voice_transcript_partial / voice: behavior more enable
  meta: kind=partial | timestamp=1777912513.4958587 | source=vosk | frequency_hz=295.9 | rms=263 | updated_at=1777912512.49036
- [2026-05-05 00:35:14] operator / voice_transcript_partial / voice: behavior more enable override
  meta: kind=partial | timestamp=1777912514.2498136 | source=vosk | frequency_hz=295.9 | rms=263 | updated_at=1777912512.49036
- [2026-05-05 00:35:14] operator / voice_transcript_partial / voice: behavior more enable board elliot
  meta: kind=partial | timestamp=1777912514.4965062 | source=vosk | frequency_hz=295.9 | rms=263 | updated_at=1777912512.49036
- [2026-05-05 00:35:14] operator / voice_transcript_partial / voice: behavior more enable board alien resume
  meta: kind=partial | timestamp=1777912514.7452602 | source=vosk | frequency_hz=295.9 | rms=263 | updated_at=1777912512.49036
- [2026-05-05 00:35:14] operator / voice_transcript_partial / voice: behavior more enable board elliot serial
  meta: kind=partial | timestamp=1777912514.997046 | source=vosk | frequency_hz=295.9 | rms=263 | updated_at=1777912512.49036
- [2026-05-05 00:35:15] operator / voice_transcript_partial / voice: behavior more enable board elliot silence
  meta: kind=partial | timestamp=1777912515.2460816 | source=vosk | frequency_hz=295.9 | rms=263 | updated_at=1777912512.49036
- [2026-05-05 00:35:15] operator / voice_transcript_partial / voice: behavior more enable board elliot say alien speed
  meta: kind=partial | timestamp=1777912515.4962313 | source=vosk | frequency_hz=294.0 | rms=256 | updated_at=1777912515.4907234
- [2026-05-05 00:35:16] operator / voice_transcript_final / voice: more enable board elliot say alien speed
  meta: kind=final | timestamp=1777912516.2714128 | source=final | frequency_hz=265.4 | rms=251 | updated_at=1777912516.2407107
- [2026-05-05 00:35:17] operator / voice_command / voice: more enable board elliot say alien speed
  meta: normalized=True
- [2026-05-05 00:35:16] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777912516.7484183 | source=vosk | frequency_hz=277.5 | rms=258 | updated_at=1777912516.4908466
- [2026-05-05 00:35:17] operator / voice_transcript_partial / voice: do you
  meta: kind=partial | timestamp=1777912517.002777 | source=vosk | frequency_hz=277.5 | rms=258 | updated_at=1777912516.4908466
- [2026-05-05 00:35:17] operator / voice_transcript_partial / voice: do you what
  meta: kind=partial | timestamp=1777912517.2491653 | source=vosk | frequency_hz=277.5 | rms=258 | updated_at=1777912516.4908466
- [2026-05-05 00:35:17] operator / voice_transcript_partial / voice: do you what do
  meta: kind=partial | timestamp=1777912517.497504 | source=vosk | frequency_hz=277.5 | rms=258 | updated_at=1777912516.4908466
- [2026-05-05 00:35:17] operator / voice_transcript_partial / voice: do you what do brightness
  meta: kind=partial | timestamp=1777912517.7566454 | source=vosk | frequency_hz=277.5 | rms=258 | updated_at=1777912516.4908466
- [2026-05-05 00:35:18] operator / voice_transcript_partial / voice: do you what do
  meta: kind=partial | timestamp=1777912518.005409 | source=vosk | frequency_hz=277.5 | rms=258 | updated_at=1777912516.4908466
- [2026-05-05 00:35:18] operator / voice_transcript_partial / voice: do you what do delay
  meta: kind=partial | timestamp=1777912518.253038 | source=vosk | frequency_hz=312.0 | rms=243 | updated_at=1777912518.2411633
- [2026-05-05 00:35:18] operator / voice_transcript_final / voice: do you what do delay
  meta: kind=final | timestamp=1777912518.7531235 | source=final | frequency_hz=280.3 | rms=252 | updated_at=1777912518.7430851
- [2026-05-05 00:35:18] operator / voice_command / voice: do you what do delay
  meta: normalized=True
- [2026-05-05 00:35:19] assistant / spoken_confirmation / voice: Connecting Smart Sentry boards now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:35:19] assistant / spoken_confirmation / voice: Received. I started your background analysis about unk behavior in the background.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:35:21] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777912521.7496583 | source=vosk | frequency_hz=277.8 | rms=255 | updated_at=1777912521.2405334
- [2026-05-05 00:35:22] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1777912522.002635 | source=vosk | frequency_hz=277.8 | rms=255 | updated_at=1777912521.2405334
- [2026-05-05 00:35:22] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:35:22] operator / voice_transcript_partial / voice: e lion enable
  meta: kind=partial | timestamp=1777912522.2577162 | source=vosk | frequency_hz=277.8 | rms=255 | updated_at=1777912521.2405334
- [2026-05-05 00:35:24] operator / voice_transcript_final / voice: lion it
  meta: kind=final | timestamp=1777912524.1686683 | source=final | frequency_hz=309.1 | rms=261 | updated_at=1777912522.9911401
- [2026-05-05 00:35:24] operator / voice_command / voice: lion it
  meta: normalized=True
- [2026-05-05 00:35:25] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777912525.4296827 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:25] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777912525.6774294 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:26] operator / voice_transcript_partial / voice: smart sentry boards
  meta: kind=partial | timestamp=1777912526.4377728 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:26] operator / voice_transcript_partial / voice: smart sentry status
  meta: kind=partial | timestamp=1777912526.926621 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:27] operator / voice_transcript_partial / voice: smart sentry boards
  meta: kind=partial | timestamp=1777912527.181962 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:27] operator / voice_transcript_partial / voice: smart sentry boards decrease
  meta: kind=partial | timestamp=1777912527.4276032 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:27] operator / voice_transcript_partial / voice: smart sentry boards it boards
  meta: kind=partial | timestamp=1777912527.6839058 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:27] operator / voice_transcript_partial / voice: smart sentry boards it boards a
  meta: kind=partial | timestamp=1777912527.9312437 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:28] operator / voice_transcript_partial / voice: smart sentry boards it boards a serial
  meta: kind=partial | timestamp=1777912528.1821733 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:28] operator / voice_transcript_partial / voice: smart sentry boards it boards disable
  meta: kind=partial | timestamp=1777912528.4300463 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:28] operator / voice_transcript_partial / voice: smart sentry boards it boards disable the alien
  meta: kind=partial | timestamp=1777912528.6896105 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:29] operator / voice_transcript_partial / voice: smart sentry boards it boards disable the app
  meta: kind=partial | timestamp=1777912529.4317544 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:30] operator / voice_transcript_partial / voice: smart sentry boards it boards disable the app e
  meta: kind=partial | timestamp=1777912530.4379373 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:30] operator / voice_transcript_partial / voice: smart sentry boards it boards disable the app e smart
  meta: kind=partial | timestamp=1777912530.6817763 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:30] operator / voice_transcript_partial / voice: smart sentry boards it boards disable the app e silence threshold
  meta: kind=partial | timestamp=1777912530.931041 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:31] operator / voice_transcript_partial / voice: smart sentry boards it boards disable the app e silence
  meta: kind=partial | timestamp=1777912531.6776245 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:31] operator / voice_transcript_final / voice: smart sentry boards it boards a serial who e silence
  meta: kind=final | timestamp=1777912531.9426787 | source=final | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:32] operator / voice_command / voice: smart sentry boards it boards a serial who e silence
  meta: normalized=True
- [2026-05-05 00:35:32] operator / voice_transcript_partial / voice: resume
  meta: kind=partial | timestamp=1777912532.1811962 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:32] operator / voice_transcript_partial / voice: resume e
  meta: kind=partial | timestamp=1777912532.9331193 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:33] operator / voice_transcript_partial / voice: resume last
  meta: kind=partial | timestamp=1777912533.1778555 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:33] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777912533.426913 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:33] operator / voice_transcript_partial / voice: resume e lion decrease
  meta: kind=partial | timestamp=1777912533.6806948 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:33] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:35:34] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777912534.1801639 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:34] operator / voice_transcript_partial / voice: [unk] the
  meta: kind=partial | timestamp=1777912534.4316375 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:34] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777912534.6989834 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:36] operator / voice_transcript_partial / voice: [unk] a lion
  meta: kind=partial | timestamp=1777912536.1782346 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:36] operator / voice_transcript_final / voice: unk unk
  meta: kind=final | timestamp=1777912536.9320445 | source=final | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:36] operator / voice_command / voice: unk unk
  meta: normalized=True
- [2026-05-05 00:35:37] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777912537.189341 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:37] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1777912537.4270551 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:37] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:35:37] operator / voice_transcript_partial / voice: e the resume
  meta: kind=partial | timestamp=1777912537.9303172 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:38] operator / voice_transcript_partial / voice: e the resume and
  meta: kind=partial | timestamp=1777912538.1857913 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:38] operator / voice_transcript_partial / voice: e the resume and go
  meta: kind=partial | timestamp=1777912538.4272225 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:38] operator / voice_transcript_partial / voice: e the resume and go more
  meta: kind=partial | timestamp=1777912538.677961 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:39] operator / voice_transcript_partial / voice: e the resume and go more guarding
  meta: kind=partial | timestamp=1777912539.1841295 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:39] operator / voice_transcript_partial / voice: e the resume and go more current
  meta: kind=partial | timestamp=1777912539.4280007 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:39] operator / voice_transcript_partial / voice: e the resume and go more guarding mode
  meta: kind=partial | timestamp=1777912539.6776285 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:39] operator / voice_transcript_final / voice: e the resume and go more unk
  meta: kind=final | timestamp=1777912539.9302156 | source=final | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:40] operator / voice_command / voice: e the resume and go more unk
  meta: normalized=True
- [2026-05-05 00:35:40] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777912540.425546 | source=vosk | frequency_hz=232.0 | rms=893 | updated_at=1777912524.9196913
- [2026-05-05 00:35:41] operator / voice_transcript_final / voice: go
  meta: kind=final | timestamp=1777912541.1833446 | source=final | frequency_hz=372.0 | rms=270 | updated_at=1777912540.9204018
- [2026-05-05 00:35:41] operator / voice_command / voice: go
  meta: normalized=True
- [2026-05-05 00:35:42] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:35:42] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:35:42] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777912542.4348202 | source=vosk | frequency_hz=342.6 | rms=281 | updated_at=1777912541.673502
- [2026-05-05 00:35:42] operator / voice_transcript_partial / voice: status report
  meta: kind=partial | timestamp=1777912542.685301 | source=vosk | frequency_hz=342.6 | rms=281 | updated_at=1777912541.673502
- [2026-05-05 00:35:42] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777912542.9282243 | source=vosk | frequency_hz=342.6 | rms=281 | updated_at=1777912541.673502
- [2026-05-05 00:35:43] operator / voice_transcript_final / voice: status
  meta: kind=final | timestamp=1777912543.5671585 | source=final | frequency_hz=342.6 | rms=281 | updated_at=1777912541.673502
- [2026-05-05 00:35:43] operator / voice_command / voice: status
  meta: normalized=True
- [2026-05-05 00:35:43] assistant / assistant_analysis / text: Assistant request queued: background analysis about status (position 1).
  meta: task_kind=analysis | speak_requested=False
- [2026-05-05 00:35:44] assistant / spoken_confirmation / voice: I am still finishing background analysis about unk behavior. I queued your background analysis about status. It is number 1 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:35:45] operator / voice_transcript_partial / voice: that again
  meta: kind=partial | timestamp=1777912545.1977735 | source=vosk | frequency_hz=342.6 | rms=281 | updated_at=1777912541.673502
- [2026-05-05 00:35:45] operator / voice_transcript_partial / voice: that again say
  meta: kind=partial | timestamp=1777912545.680017 | source=vosk | frequency_hz=342.6 | rms=281 | updated_at=1777912541.673502
- [2026-05-05 00:35:46] operator / voice_transcript_final / voice: that again
  meta: kind=final | timestamp=1777912546.179925 | source=final | frequency_hz=342.6 | rms=281 | updated_at=1777912541.673502
- [2026-05-05 00:35:46] operator / voice_command / voice: that again
  meta: normalized=True
- [2026-05-05 00:35:46] operator / voice_transcript_partial / voice: cancel
  meta: kind=partial | timestamp=1777912546.6847115 | source=vosk | frequency_hz=342.6 | rms=281 | updated_at=1777912541.673502
- [2026-05-05 00:35:46] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777912546.9289944 | source=vosk | frequency_hz=342.6 | rms=281 | updated_at=1777912541.673502
- [2026-05-05 00:35:49] operator / voice_transcript_partial / voice: [unk] status
  meta: kind=partial | timestamp=1777912549.9293616 | source=vosk | frequency_hz=282.0 | rms=652 | updated_at=1777912548.6710932
- [2026-05-05 00:35:50] operator / voice_transcript_partial / voice: [unk] theme to
  meta: kind=partial | timestamp=1777912550.178417 | source=vosk | frequency_hz=282.0 | rms=652 | updated_at=1777912548.6710932
- [2026-05-05 00:35:50] operator / voice_transcript_partial / voice: [unk] theme to what
  meta: kind=partial | timestamp=1777912550.6792758 | source=vosk | frequency_hz=320.0 | rms=293 | updated_at=1777912550.6697571
- [2026-05-05 00:35:50] operator / voice_transcript_partial / voice: [unk] theme to what do
  meta: kind=partial | timestamp=1777912550.9323711 | source=vosk | frequency_hz=293.4 | rms=302 | updated_at=1777912550.9198492
- [2026-05-05 00:35:52] operator / voice_transcript_final / voice: change theme
  meta: kind=final | timestamp=1777912552.2997775 | source=final | frequency_hz=297.7 | rms=298 | updated_at=1777912551.4204423
- [2026-05-05 00:35:52] operator / voice_command / voice: change theme
  meta: normalized=True
- [2026-05-05 00:35:52] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777912552.3123024 | source=vosk | frequency_hz=297.7 | rms=298 | updated_at=1777912551.4204423
- [2026-05-05 00:35:52] operator / voice_transcript_partial / voice: to the
  meta: kind=partial | timestamp=1777912552.8133962 | source=vosk | frequency_hz=297.7 | rms=298 | updated_at=1777912551.4204423
- [2026-05-05 00:35:53] operator / voice_transcript_final / voice: to the
  meta: kind=final | timestamp=1777912553.5646143 | source=final | frequency_hz=297.7 | rms=298 | updated_at=1777912551.4204423
- [2026-05-05 00:35:53] operator / voice_command / voice: to the
  meta: normalized=True
- [2026-05-05 00:35:57] operator / voice_transcript_partial / voice: be
  meta: kind=partial | timestamp=1777912557.629291 | source=vosk
- [2026-05-05 00:35:58] operator / voice_transcript_partial / voice: be no
  meta: kind=partial | timestamp=1777912558.1238565 | source=vosk | frequency_hz=356.0 | rms=308 | updated_at=1777912558.1173441
- [2026-05-05 00:35:58] operator / voice_transcript_partial / voice: be no status
  meta: kind=partial | timestamp=1777912558.8752756 | source=vosk | frequency_hz=356.0 | rms=308 | updated_at=1777912558.1173441
- [2026-05-05 00:35:59] operator / voice_transcript_partial / voice: be no same but
  meta: kind=partial | timestamp=1777912559.1254194 | source=vosk | frequency_hz=356.0 | rms=308 | updated_at=1777912558.1173441
- [2026-05-05 00:35:59] operator / voice_transcript_partial / voice: be no status report
  meta: kind=partial | timestamp=1777912559.376165 | source=vosk | frequency_hz=356.0 | rms=308 | updated_at=1777912558.1173441
- [2026-05-05 00:35:59] operator / voice_transcript_partial / voice: be no status on
  meta: kind=partial | timestamp=1777912559.6251516 | source=vosk | frequency_hz=356.0 | rms=308 | updated_at=1777912558.1173441
- [2026-05-05 00:35:59] operator / voice_transcript_partial / voice: be no status on lion
  meta: kind=partial | timestamp=1777912559.8758736 | source=vosk | frequency_hz=356.0 | rms=308 | updated_at=1777912558.1173441
- [2026-05-05 00:36:00] operator / voice_transcript_partial / voice: be no status on lion go
  meta: kind=partial | timestamp=1777912560.1262963 | source=vosk | frequency_hz=356.0 | rms=308 | updated_at=1777912558.1173441
- [2026-05-05 00:36:00] operator / voice_transcript_partial / voice: be no status on lion go sentry
  meta: kind=partial | timestamp=1777912560.3755605 | source=vosk | frequency_hz=356.0 | rms=308 | updated_at=1777912558.1173441
- [2026-05-05 00:36:00] operator / voice_transcript_partial / voice: be no status on lion go sentry run diagnostics
  meta: kind=partial | timestamp=1777912560.62864 | source=vosk | frequency_hz=356.0 | rms=308 | updated_at=1777912558.1173441
- [2026-05-05 00:36:01] operator / voice_transcript_partial / voice: be no status on lion go sentry lion identify
  meta: kind=partial | timestamp=1777912561.1373794 | source=vosk | frequency_hz=356.0 | rms=308 | updated_at=1777912558.1173441
- [2026-05-05 00:36:01] operator / voice_transcript_final / voice: be no status on mind go sentry unk
  meta: kind=final | timestamp=1777912561.391666 | source=final | frequency_hz=356.0 | rms=308 | updated_at=1777912558.1173441
- [2026-05-05 00:36:02] assistant / assistant_analysis / text: Assistant update. Analysis [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Local runtime analysis fallback: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Runtime facts: state=PAUSED | camera_open=True | yolo_loaded=True | mode=2 | tracking_scope=person | loss_protocols=rapid_handoff_search/persistent_reacquire_search | speed=100 trigger=water burst=6@70ms | return_delay=1.5 | guard_mode=2 guard_pan_tilt=140.0/83.0. Next step: Reconnect the controller link before expecting movement, trigger commands, or live bridge telemetry. Supporting Findings: - [low] Active behavior profile: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. - [high] Controller link offline: The sentry is not currently connected to its controller link. - [medium] PIR guard enabled without active sensors: PIR guard is ON but no PIR sensor entries are enabled. - [low] Conversational mode is text-only: Conversational Voice mode is selected, but assistant auto-speak is turned off. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=analysis | speak_requested=False
- [2026-05-05 00:36:04] operator / voice_transcript_partial / voice: say that
  meta: kind=partial | timestamp=1777912564.6239502 | source=vosk | frequency_hz=307.8 | rms=298 | updated_at=1777912564.1168919
- [2026-05-05 00:36:06] operator / voice_transcript_final / voice: say that
  meta: kind=final | timestamp=1777912566.6336215 | source=final | frequency_hz=289.3 | rms=301 | updated_at=1777912566.368613
- [2026-05-05 00:36:06] operator / voice_transcript_partial / voice: cancel
  meta: kind=partial | timestamp=1777912566.8759844 | source=vosk | frequency_hz=289.3 | rms=301 | updated_at=1777912566.368613
- [2026-05-05 00:36:07] operator / voice_transcript_final / voice: cancel
  meta: kind=final | timestamp=1777912567.8740757 | source=final | frequency_hz=278.3 | rms=311 | updated_at=1777912567.3671162
- [2026-05-05 00:36:08] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777912568.3784797 | source=vosk | frequency_hz=278.3 | rms=311 | updated_at=1777912567.3671162
- [2026-05-05 00:36:08] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777912568.6236575 | source=vosk | frequency_hz=278.3 | rms=311 | updated_at=1777912567.3671162
- [2026-05-05 00:36:09] operator / voice_transcript_partial / voice: smart sentry home
  meta: kind=partial | timestamp=1777912569.123598 | source=vosk | frequency_hz=278.3 | rms=311 | updated_at=1777912567.3671162
- [2026-05-05 00:36:09] operator / voice_transcript_partial / voice: smart sentry home and
  meta: kind=partial | timestamp=1777912569.374923 | source=vosk | frequency_hz=278.3 | rms=311 | updated_at=1777912567.3671162
- [2026-05-05 00:36:09] operator / voice_transcript_partial / voice: smart sentry home and boards smart
  meta: kind=partial | timestamp=1777912569.625113 | source=vosk | frequency_hz=278.3 | rms=311 | updated_at=1777912567.3671162
- [2026-05-05 00:36:09] operator / voice_transcript_partial / voice: smart sentry home and boards mode
  meta: kind=partial | timestamp=1777912569.881984 | source=vosk | frequency_hz=278.3 | rms=311 | updated_at=1777912567.3671162
- [2026-05-05 00:36:10] operator / voice_transcript_final / voice: smart sentry home and boards mode
  meta: kind=final | timestamp=1777912570.3784945 | source=final | frequency_hz=278.3 | rms=311 | updated_at=1777912567.3671162
- [2026-05-05 00:36:11] operator / voice_transcript_partial / voice: go speed
  meta: kind=partial | timestamp=1777912571.873938 | source=vosk | frequency_hz=278.3 | rms=311 | updated_at=1777912567.3671162
- [2026-05-05 00:36:12] operator / voice_transcript_partial / voice: boards and
  meta: kind=partial | timestamp=1777912572.1331856 | source=vosk | frequency_hz=278.3 | rms=311 | updated_at=1777912567.3671162
- [2026-05-05 00:36:12] operator / voice_transcript_partial / voice: boards and enable
  meta: kind=partial | timestamp=1777912572.376037 | source=vosk | frequency_hz=316.0 | rms=332 | updated_at=1777912572.3675184
- [2026-05-05 00:36:12] operator / voice_transcript_partial / voice: boards and do you
  meta: kind=partial | timestamp=1777912572.6312103 | source=vosk | frequency_hz=343.3 | rms=332 | updated_at=1777912572.61767
- [2026-05-05 00:36:22] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777912582.47706 | source=vosk | frequency_hz=313.9 | rms=288 | updated_at=1777912581.715907
- [2026-05-05 00:36:22] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777912582.7227983 | source=vosk | frequency_hz=313.9 | rms=288 | updated_at=1777912581.715907
- [2026-05-05 00:36:23] operator / voice_transcript_partial / voice: smart sentry queue
  meta: kind=partial | timestamp=1777912583.221403 | source=vosk | frequency_hz=313.9 | rms=288 | updated_at=1777912581.715907
- [2026-05-05 00:36:23] operator / voice_transcript_partial / voice: smart sentry e lion
  meta: kind=partial | timestamp=1777912583.4790623 | source=vosk | frequency_hz=313.9 | rms=288 | updated_at=1777912581.715907
- [2026-05-05 00:36:23] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:36:23] operator / voice_transcript_partial / voice: smart sentry boards smart
  meta: kind=partial | timestamp=1777912583.739314 | source=vosk | frequency_hz=308.0 | rms=310 | updated_at=1777912583.7161841
- [2026-05-05 00:36:23] operator / voice_transcript_partial / voice: smart sentry boards
  meta: kind=partial | timestamp=1777912583.9727354 | source=vosk | frequency_hz=308.0 | rms=310 | updated_at=1777912583.7161841
- [2026-05-05 00:36:24] operator / voice_transcript_final / voice: smart sentry boards
  meta: kind=final | timestamp=1777912584.236797 | source=final | frequency_hz=308.0 | rms=310 | updated_at=1777912583.7161841
- [2026-05-05 00:36:24] operator / voice_command / voice: smart sentry boards
  meta: normalized=True
- [2026-05-05 00:36:25] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777912585.7114093 | source=vosk
- [2026-05-05 00:36:42] operator / voice_transcript_partial / voice: elliot
  meta: kind=partial | timestamp=1777912602.7118979 | source=vosk | frequency_hz=299.4 | rms=298 | updated_at=1777912602.203289
- [2026-05-05 00:36:47] assistant / assistant_analysis / text: Assistant update. Analysis [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Local runtime analysis fallback: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Runtime facts: state=PAUSED | camera_open=True | yolo_loaded=True | mode=2 | tracking_scope=person | loss_protocols=rapid_handoff_search/persistent_reacquire_search | speed=100 trigger=water burst=6@70ms | return_delay=1.5 | guard_mode=2 guard_pan_tilt=140.0/83.0. Next step: Enable at least one PIR sensor or disable PIR guard to match actual intent. Supporting Findings: - [low] Active behavior profile: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. - [medium] PIR guard enabled without active sensors: PIR guard is ON but no PIR sensor entries are enabled. - [low] Conversational mode is text-only: Conversational Voice mode is selected, but assistant auto-speak is turned off. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=analysis | speak_requested=False
- [2026-05-05 00:36:49] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777912609.4773216 | source=vosk | frequency_hz=281.6 | rms=626 | updated_at=1777912608.9561448
- [2026-05-05 00:36:49] operator / voice_transcript_partial / voice: alien analyze
  meta: kind=partial | timestamp=1777912609.9632332 | source=vosk | frequency_hz=281.6 | rms=626 | updated_at=1777912608.9561448
- [2026-05-05 00:36:50] operator / voice_transcript_partial / voice: alien enable the
  meta: kind=partial | timestamp=1777912610.2132323 | source=vosk | frequency_hz=281.6 | rms=626 | updated_at=1777912608.9561448
- [2026-05-05 00:36:51] operator / voice_transcript_final / voice: enable the
  meta: kind=final | timestamp=1777912611.215123 | source=final | frequency_hz=324.3 | rms=309 | updated_at=1777912611.2050705
- [2026-05-05 00:36:51] operator / voice_command / voice: enable the
  meta: normalized=True
- [2026-05-05 00:36:52] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:36:54] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777912614.2115712 | source=vosk | frequency_hz=258.8 | rms=315 | updated_at=1777912613.7104719
- [2026-05-05 00:36:54] operator / voice_transcript_partial / voice: be more
  meta: kind=partial | timestamp=1777912614.4636931 | source=vosk | frequency_hz=258.8 | rms=315 | updated_at=1777912613.7104719
- [2026-05-05 00:36:54] operator / voice_transcript_partial / voice: be more strict
  meta: kind=partial | timestamp=1777912614.7178338 | source=vosk | frequency_hz=258.8 | rms=315 | updated_at=1777912613.7104719
- [2026-05-05 00:36:55] operator / voice_transcript_final / voice: more
  meta: kind=final | timestamp=1777912615.8123198 | source=final | frequency_hz=258.8 | rms=315 | updated_at=1777912613.7104719
- [2026-05-05 00:36:55] operator / voice_command / voice: more
  meta: normalized=True
- [2026-05-05 00:36:56] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:36:58] operator / voice_transcript_partial / voice: repeat
  meta: kind=partial | timestamp=1777912618.0803995 | source=vosk | frequency_hz=400.0 | rms=336 | updated_at=1777912615.820337
- [2026-05-05 00:36:58] operator / voice_transcript_final / voice: decrease repeat
  meta: kind=final | timestamp=1777912618.822714 | source=final | frequency_hz=400.0 | rms=336 | updated_at=1777912615.820337
- [2026-05-05 00:36:59] operator / voice_command / voice: decrease repeat
  meta: normalized=True
- [2026-05-05 00:36:59] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:37:03] operator / voice_transcript_partial / voice: rest
  meta: kind=partial | timestamp=1777912623.571601 | source=vosk | frequency_hz=296.2 | rms=312 | updated_at=1777912621.814027
- [2026-05-05 00:37:04] operator / voice_transcript_final / voice: rest
  meta: kind=final | timestamp=1777912624.3265762 | source=final | frequency_hz=296.2 | rms=312 | updated_at=1777912621.814027
- [2026-05-05 00:37:04] operator / voice_command / voice: rest
  meta: normalized=True
- [2026-05-05 00:37:05] operator / voice_transcript_partial / voice: on
  meta: kind=partial | timestamp=1777912625.3271785 | source=vosk | frequency_hz=296.2 | rms=312 | updated_at=1777912621.814027
- [2026-05-05 00:37:07] assistant / spoken_confirmation / voice: I think I heard rest. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:37:13] operator / voice_transcript_partial / voice: strict
  meta: kind=partial | timestamp=1777912633.2393744 | source=vosk | frequency_hz=349.4 | rms=299 | updated_at=1777912632.231429
- [2026-05-05 00:37:13] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777912633.491705 | source=vosk | frequency_hz=349.4 | rms=299 | updated_at=1777912632.231429
- [2026-05-05 00:37:13] operator / voice_transcript_partial / voice: alien that it
  meta: kind=partial | timestamp=1777912633.7447312 | source=vosk | frequency_hz=349.4 | rms=299 | updated_at=1777912632.231429
- [2026-05-05 00:37:13] operator / voice_transcript_partial / voice: alien that it the
  meta: kind=partial | timestamp=1777912633.9889812 | source=vosk | frequency_hz=349.4 | rms=299 | updated_at=1777912632.231429
- [2026-05-05 00:37:14] operator / voice_transcript_partial / voice: alien that it the never
  meta: kind=partial | timestamp=1777912634.238702 | source=vosk | frequency_hz=349.4 | rms=299 | updated_at=1777912632.231429
- [2026-05-05 00:37:14] operator / voice_transcript_partial / voice: alien that it the never mind
  meta: kind=partial | timestamp=1777912634.4918346 | source=vosk | frequency_hz=349.4 | rms=299 | updated_at=1777912632.231429
- [2026-05-05 00:37:15] operator / voice_transcript_final / voice: that it the never mind
  meta: kind=final | timestamp=1777912635.7200801 | source=final | frequency_hz=346.9 | rms=270 | updated_at=1777912635.2371218
- [2026-05-05 00:37:15] operator / voice_command / voice: that it the never mind
  meta: normalized=True
- [2026-05-05 00:37:16] operator / voice_transcript_partial / voice: the more
  meta: kind=partial | timestamp=1777912636.4908829 | source=vosk | frequency_hz=346.9 | rms=270 | updated_at=1777912635.2371218
- [2026-05-05 00:37:16] operator / voice_transcript_partial / voice: the more board
  meta: kind=partial | timestamp=1777912636.9911625 | source=vosk | frequency_hz=346.9 | rms=270 | updated_at=1777912635.2371218
- [2026-05-05 00:37:17] operator / voice_transcript_final / voice: the more board
  meta: kind=final | timestamp=1777912637.4920459 | source=final | frequency_hz=317.2 | rms=266 | updated_at=1777912637.4840403
- [2026-05-05 00:37:17] operator / voice_command / voice: the more board
  meta: normalized=True
- [2026-05-05 00:37:18] assistant / spoken_confirmation / voice: Cancelled. I will not run rest. What do you want me to do next?
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:37:18] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:37:18] operator / voice_transcript_partial / voice: on
  meta: kind=partial | timestamp=1777912638.9876153 | source=vosk | frequency_hz=314.1 | rms=272 | updated_at=1777912638.4814255
- [2026-05-05 00:37:19] operator / voice_transcript_partial / voice: on lion
  meta: kind=partial | timestamp=1777912639.249302 | source=vosk | frequency_hz=314.1 | rms=272 | updated_at=1777912638.4814255
- [2026-05-05 00:37:19] operator / voice_transcript_partial / voice: on lion resume
  meta: kind=partial | timestamp=1777912639.9897203 | source=vosk | frequency_hz=314.1 | rms=272 | updated_at=1777912638.4814255
- [2026-05-05 00:37:20] operator / voice_transcript_partial / voice: on lion resume you do
  meta: kind=partial | timestamp=1777912640.4880779 | source=vosk | frequency_hz=314.1 | rms=272 | updated_at=1777912638.4814255
- [2026-05-05 00:37:20] operator / voice_transcript_partial / voice: on lion resume alien
  meta: kind=partial | timestamp=1777912640.7464948 | source=vosk | frequency_hz=314.1 | rms=272 | updated_at=1777912638.4814255
- [2026-05-05 00:37:20] operator / voice_transcript_partial / voice: on lion resume that again
  meta: kind=partial | timestamp=1777912640.9870136 | source=vosk | frequency_hz=348.0 | rms=285 | updated_at=1777912640.9824686
- [2026-05-05 00:37:21] operator / voice_transcript_partial / voice: on lion resume alien repeat
  meta: kind=partial | timestamp=1777912641.4909394 | source=vosk | frequency_hz=348.0 | rms=285 | updated_at=1777912640.9824686
- [2026-05-05 00:37:21] operator / voice_transcript_partial / voice: on lion resume alien resume guarding
  meta: kind=partial | timestamp=1777912641.7397673 | source=vosk | frequency_hz=348.0 | rms=285 | updated_at=1777912640.9824686
- [2026-05-05 00:37:21] operator / voice_transcript_partial / voice: on lion resume alien repeat
  meta: kind=partial | timestamp=1777912641.9967597 | source=vosk | frequency_hz=348.0 | rms=285 | updated_at=1777912640.9824686
- [2026-05-05 00:37:23] operator / voice_transcript_final / voice: on lion no you that again be less
  meta: kind=final | timestamp=1777912643.0869548 | source=final | frequency_hz=365.7 | rms=722 | updated_at=1777912642.481875
- [2026-05-05 00:37:23] operator / voice_command / voice: on lion no you that again be less
  meta: normalized=True
- [2026-05-05 00:37:24] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:37:27] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777912647.1502137 | source=vosk | frequency_hz=248.0 | rms=836 | updated_at=1777912645.146466
- [2026-05-05 00:37:27] operator / voice_transcript_partial / voice: be less
  meta: kind=partial | timestamp=1777912647.3974 | source=vosk | frequency_hz=248.0 | rms=836 | updated_at=1777912645.146466
- [2026-05-05 00:37:27] operator / voice_transcript_partial / voice: be less strict
  meta: kind=partial | timestamp=1777912647.898614 | source=vosk | frequency_hz=248.0 | rms=836 | updated_at=1777912645.146466
- [2026-05-05 00:37:28] operator / voice_transcript_partial / voice: be less the serial
  meta: kind=partial | timestamp=1777912648.149843 | source=vosk | frequency_hz=248.0 | rms=836 | updated_at=1777912645.146466
- [2026-05-05 00:37:28] operator / voice_transcript_partial / voice: be less the serial decrease
  meta: kind=partial | timestamp=1777912648.4000704 | source=vosk | frequency_hz=248.0 | rms=836 | updated_at=1777912645.146466
- [2026-05-05 00:37:28] operator / voice_transcript_partial / voice: be less disable the
  meta: kind=partial | timestamp=1777912648.6571088 | source=vosk | frequency_hz=248.0 | rms=836 | updated_at=1777912645.146466
- [2026-05-05 00:37:28] operator / voice_transcript_partial / voice: be less disable the board theme
  meta: kind=partial | timestamp=1777912648.8992743 | source=vosk | frequency_hz=248.0 | rms=836 | updated_at=1777912645.146466
- [2026-05-05 00:37:29] operator / voice_transcript_final / voice: be less disable the board theme
  meta: kind=final | timestamp=1777912649.6605117 | source=final | frequency_hz=248.0 | rms=836 | updated_at=1777912645.146466
- [2026-05-05 00:37:29] operator / voice_command / voice: be less disable the board theme
  meta: normalized=True
- [2026-05-05 00:37:30] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:37:33] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777912653.3987725 | source=vosk | frequency_hz=352.0 | rms=315 | updated_at=1777912652.8923187
- [2026-05-05 00:37:33] operator / voice_transcript_partial / voice: that again
  meta: kind=partial | timestamp=1777912653.6482198 | source=vosk | frequency_hz=352.0 | rms=315 | updated_at=1777912652.8923187
- [2026-05-05 00:37:33] operator / voice_transcript_partial / voice: that again it
  meta: kind=partial | timestamp=1777912653.8982675 | source=vosk | frequency_hz=352.0 | rms=315 | updated_at=1777912652.8923187
- [2026-05-05 00:37:34] operator / voice_transcript_partial / voice: that again
  meta: kind=partial | timestamp=1777912654.149295 | source=vosk | frequency_hz=352.0 | rms=315 | updated_at=1777912652.8923187
- [2026-05-05 00:37:34] operator / voice_transcript_final / voice: that again
  meta: kind=final | timestamp=1777912654.413503 | source=final | frequency_hz=352.0 | rms=315 | updated_at=1777912652.8923187
- [2026-05-05 00:37:34] operator / voice_command / voice: that again
  meta: normalized=True
- [2026-05-05 00:37:35] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:37:42] operator / voice_transcript_partial / voice: less
  meta: kind=partial | timestamp=1777912662.717657 | source=vosk | frequency_hz=268.6 | rms=308 | updated_at=1777912661.705333
- [2026-05-05 00:37:42] operator / voice_transcript_partial / voice: last
  meta: kind=partial | timestamp=1777912662.970872 | source=vosk | frequency_hz=268.6 | rms=308 | updated_at=1777912661.705333
- [2026-05-05 00:37:43] operator / voice_transcript_partial / voice: last mind
  meta: kind=partial | timestamp=1777912663.211622 | source=vosk | frequency_hz=268.6 | rms=308 | updated_at=1777912661.705333
- [2026-05-05 00:37:43] operator / voice_transcript_partial / voice: last change
  meta: kind=partial | timestamp=1777912663.462272 | source=vosk | frequency_hz=268.6 | rms=308 | updated_at=1777912661.705333
- [2026-05-05 00:37:43] operator / voice_transcript_partial / voice: last change on commands
  meta: kind=partial | timestamp=1777912663.9639122 | source=vosk | frequency_hz=268.6 | rms=308 | updated_at=1777912661.705333
- [2026-05-05 00:37:44] operator / voice_transcript_partial / voice: last change on current
  meta: kind=partial | timestamp=1777912664.2111979 | source=vosk | frequency_hz=268.6 | rms=308 | updated_at=1777912661.705333
- [2026-05-05 00:37:44] operator / voice_transcript_partial / voice: last change on current task
  meta: kind=partial | timestamp=1777912664.9624088 | source=vosk | frequency_hz=304.8 | rms=327 | updated_at=1777912664.9554002
- [2026-05-05 00:37:45] operator / voice_transcript_final / voice: last change on current
  meta: kind=final | timestamp=1777912665.2137365 | source=final | frequency_hz=275.1 | rms=307 | updated_at=1777912665.2057228
- [2026-05-05 00:37:45] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777912665.960574 | source=vosk | frequency_hz=275.1 | rms=307 | updated_at=1777912665.2057228
- [2026-05-05 00:37:46] operator / voice_transcript_partial / voice: resume
  meta: kind=partial | timestamp=1777912666.2137647 | source=vosk | frequency_hz=275.1 | rms=307 | updated_at=1777912665.2057228
- [2026-05-05 00:37:46] operator / voice_transcript_partial / voice: decrease repeat
  meta: kind=partial | timestamp=1777912666.4639857 | source=vosk | frequency_hz=275.1 | rms=307 | updated_at=1777912665.2057228
- [2026-05-05 00:37:47] operator / voice_transcript_final / voice: decrease repeat
  meta: kind=final | timestamp=1777912667.211978 | source=final | frequency_hz=336.4 | rms=311 | updated_at=1777912667.2054582
- [2026-05-05 00:37:49] operator / voice_transcript_partial / voice: queue
  meta: kind=partial | timestamp=1777912669.7139885 | source=vosk | frequency_hz=330.1 | rms=337 | updated_at=1777912669.706951
- [2026-05-05 00:37:50] operator / voice_transcript_final / voice: queue
  meta: kind=final | timestamp=1777912670.4627357 | source=final | frequency_hz=240.8 | rms=307 | updated_at=1777912670.4557347
- [2026-05-05 00:37:51] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777912671.2106762 | source=vosk | frequency_hz=240.8 | rms=307 | updated_at=1777912670.4557347
- [2026-05-05 00:37:51] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777912671.4678686 | source=vosk | frequency_hz=240.8 | rms=307 | updated_at=1777912670.4557347
- [2026-05-05 00:37:52] operator / voice_transcript_partial / voice: smart sentry queue
  meta: kind=partial | timestamp=1777912672.2113461 | source=vosk | frequency_hz=240.8 | rms=307 | updated_at=1777912670.4557347
- [2026-05-05 00:37:52] operator / voice_transcript_final / voice: smart sentry unk
  meta: kind=final | timestamp=1777912672.464141 | source=final | frequency_hz=240.8 | rms=307 | updated_at=1777912670.4557347
- [2026-05-05 00:37:52] operator / voice_transcript_partial / voice: smart the
  meta: kind=partial | timestamp=1777912672.7142892 | source=vosk | frequency_hz=240.8 | rms=307 | updated_at=1777912670.4557347
- [2026-05-05 00:37:52] operator / voice_transcript_partial / voice: smart the e
  meta: kind=partial | timestamp=1777912672.9613824 | source=vosk | frequency_hz=240.8 | rms=307 | updated_at=1777912670.4557347
- [2026-05-05 00:37:53] operator / voice_transcript_partial / voice: smart the resume last
  meta: kind=partial | timestamp=1777912673.2117825 | source=vosk | frequency_hz=240.8 | rms=307 | updated_at=1777912670.4557347
- [2026-05-05 00:37:53] operator / voice_transcript_partial / voice: smart the e sentry
  meta: kind=partial | timestamp=1777912673.4616675 | source=vosk | frequency_hz=240.8 | rms=307 | updated_at=1777912670.4557347
- [2026-05-05 00:37:53] operator / voice_transcript_final / voice: smart the e sentry
  meta: kind=final | timestamp=1777912673.7280188 | source=final | frequency_hz=240.8 | rms=307 | updated_at=1777912670.4557347
- [2026-05-05 00:37:54] operator / voice_transcript_partial / voice: boards
  meta: kind=partial | timestamp=1777912674.9618542 | source=vosk | frequency_hz=400.4 | rms=519 | updated_at=1777912674.2096977
- [2026-05-05 00:37:55] operator / voice_transcript_final / voice: boards
  meta: kind=final | timestamp=1777912675.7140667 | source=final | frequency_hz=400.4 | rms=519 | updated_at=1777912674.2096977
- [2026-05-05 00:37:56] operator / voice_transcript_partial / voice: yourself
  meta: kind=partial | timestamp=1777912676.2115014 | source=vosk | frequency_hz=400.4 | rms=519 | updated_at=1777912674.2096977
- [2026-05-05 00:37:56] operator / voice_transcript_final / voice: yourself
  meta: kind=final | timestamp=1777912676.9642003 | source=final | frequency_hz=400.4 | rms=519 | updated_at=1777912674.2096977
- [2026-05-05 00:37:57] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777912677.7134411 | source=vosk | frequency_hz=400.4 | rms=519 | updated_at=1777912674.2096977
- [2026-05-05 00:37:57] operator / voice_transcript_partial / voice: status report
  meta: kind=partial | timestamp=1777912677.962945 | source=vosk | frequency_hz=400.4 | rms=519 | updated_at=1777912674.2096977
- [2026-05-05 00:37:58] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777912678.521893 | source=vosk | frequency_hz=400.4 | rms=519 | updated_at=1777912674.2096977
- [2026-05-05 00:37:58] operator / voice_transcript_partial / voice: status go
  meta: kind=partial | timestamp=1777912678.5368829 | source=vosk | frequency_hz=400.4 | rms=519 | updated_at=1777912674.2096977
- [2026-05-05 00:37:58] operator / voice_transcript_partial / voice: status go clear the
  meta: kind=partial | timestamp=1777912678.7165802 | source=vosk | frequency_hz=400.4 | rms=519 | updated_at=1777912674.2096977
- [2026-05-05 00:37:59] operator / voice_transcript_partial / voice: status go clear override
  meta: kind=partial | timestamp=1777912679.4646423 | source=vosk | frequency_hz=400.4 | rms=519 | updated_at=1777912674.2096977
- [2026-05-05 00:37:59] operator / voice_transcript_final / voice: status go clear
  meta: kind=final | timestamp=1777912679.740131 | source=final | frequency_hz=400.4 | rms=519 | updated_at=1777912674.2096977
- [2026-05-05 00:38:05] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777912685.723909 | source=vosk | frequency_hz=374.0 | rms=692 | updated_at=1777912683.955815
- [2026-05-05 00:38:06] operator / voice_transcript_partial / voice: say go
  meta: kind=partial | timestamp=1777912686.4621117 | source=vosk | frequency_hz=374.0 | rms=692 | updated_at=1777912683.955815
- [2026-05-05 00:38:07] operator / voice_transcript_final / voice: say go
  meta: kind=final | timestamp=1777912687.214056 | source=final | frequency_hz=352.0 | rms=716 | updated_at=1777912686.7061148
- [2026-05-05 00:38:08] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777912688.2124326 | source=vosk | frequency_hz=352.0 | rms=716 | updated_at=1777912686.7061148
- [2026-05-05 00:38:09] operator / voice_transcript_final / voice: say
  meta: kind=final | timestamp=1777912689.4436347 | source=final | frequency_hz=352.0 | rms=716 | updated_at=1777912686.7061148
- [2026-05-05 00:38:11] operator / voice_transcript_partial / voice: be
  meta: kind=partial | timestamp=1777912691.4268317 | source=vosk | frequency_hz=258.0 | rms=491 | updated_at=1777912689.677762
- [2026-05-05 00:38:12] operator / voice_transcript_final / voice: be
  meta: kind=final | timestamp=1777912692.4303606 | source=final | frequency_hz=258.0 | rms=491 | updated_at=1777912689.677762
- [2026-05-05 00:38:16] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777912696.6892178 | source=vosk | frequency_hz=258.0 | rms=491 | updated_at=1777912689.677762
- [2026-05-05 00:38:17] operator / voice_transcript_final / voice: say
  meta: kind=final | timestamp=1777912697.4315012 | source=final | frequency_hz=258.0 | rms=491 | updated_at=1777912689.677762
- [2026-05-05 00:39:33] operator / voice_transcript_partial / voice: enable smart
  meta: kind=partial | timestamp=1777912773.1950727 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:33] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777912773.4295065 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:34] operator / voice_transcript_partial / voice: status port
  meta: kind=partial | timestamp=1777912774.1796968 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:34] operator / voice_transcript_partial / voice: status report
  meta: kind=partial | timestamp=1777912774.4314702 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:34] operator / voice_transcript_final / voice: status report
  meta: kind=final | timestamp=1777912774.96591 | source=final | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:35] operator / voice_transcript_partial / voice: disconnect
  meta: kind=partial | timestamp=1777912775.9308994 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:36] operator / voice_transcript_partial / voice: do that again
  meta: kind=partial | timestamp=1777912776.18988 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:36] operator / voice_transcript_partial / voice: do that again silence
  meta: kind=partial | timestamp=1777912776.4329338 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:36] operator / voice_transcript_partial / voice: do that again say
  meta: kind=partial | timestamp=1777912776.7492743 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:37] operator / voice_transcript_final / voice: do it again
  meta: kind=final | timestamp=1777912777.2198436 | source=final | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:37] operator / voice_command / voice: do it again
  meta: normalized=True
- [2026-05-05 00:39:37] operator / voice_transcript_partial / voice: it
  meta: kind=partial | timestamp=1777912777.6893044 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:38] operator / voice_transcript_partial / voice: it again
  meta: kind=partial | timestamp=1777912778.1801987 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:38] operator / voice_transcript_partial / voice: it
  meta: kind=partial | timestamp=1777912778.436672 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:38] operator / voice_transcript_partial / voice: it anything cancel
  meta: kind=partial | timestamp=1777912778.6806848 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:39] assistant / spoken_confirmation / voice: There is no recent command to repeat yet.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:39:38] operator / voice_transcript_partial / voice: it sentry
  meta: kind=partial | timestamp=1777912778.9609857 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:39] operator / voice_transcript_partial / voice: it tracking port connect
  meta: kind=partial | timestamp=1777912779.1825151 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:39] operator / voice_transcript_partial / voice: it tracking port connect to
  meta: kind=partial | timestamp=1777912779.4299426 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:39] operator / voice_transcript_partial / voice: it tracking port connect
  meta: kind=partial | timestamp=1777912779.6830094 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:39] operator / voice_transcript_partial / voice: it tracking port connect connect
  meta: kind=partial | timestamp=1777912779.9360142 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:41] operator / voice_transcript_partial / voice: it tracking port connect connect say it
  meta: kind=partial | timestamp=1777912781.1813283 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:41] operator / voice_transcript_partial / voice: it tracking port connect connect say it again
  meta: kind=partial | timestamp=1777912781.6874797 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:42] operator / voice_transcript_partial / voice: it tracking port connect connect say it again the
  meta: kind=partial | timestamp=1777912782.180439 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:42] operator / voice_transcript_partial / voice: it tracking port connect connect say it again you
  meta: kind=partial | timestamp=1777912782.4305305 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:43] operator / voice_transcript_final / voice: it change to port connect connect say it again you
  meta: kind=final | timestamp=1777912783.4347265 | source=final | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:43] operator / voice_command / voice: it change to port connect connect say it again you
  meta: normalized=True
- [2026-05-05 00:39:44] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:39:46] operator / voice_transcript_partial / voice: you smart
  meta: kind=partial | timestamp=1777912786.9898124 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:47] operator / voice_transcript_partial / voice: you smart sentry
  meta: kind=partial | timestamp=1777912787.4857538 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:47] operator / voice_transcript_partial / voice: you smart resume guarding
  meta: kind=partial | timestamp=1777912787.764884 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:47] operator / voice_transcript_partial / voice: you smart resume current
  meta: kind=partial | timestamp=1777912787.9831257 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:48] operator / voice_transcript_partial / voice: you smart resume current yes
  meta: kind=partial | timestamp=1777912788.9848273 | source=vosk | frequency_hz=316.0 | rms=259 | updated_at=1777912772.1747284
- [2026-05-05 00:39:49] operator / voice_transcript_partial / voice: you smart resume current app behavior
  meta: kind=partial | timestamp=1777912789.240556 | source=vosk | frequency_hz=256.0 | rms=272 | updated_at=1777912789.2289824
- [2026-05-05 00:39:49] operator / voice_transcript_final / voice: do you smart resume current app behavior
  meta: kind=final | timestamp=1777912789.7932959 | source=final | frequency_hz=256.0 | rms=272 | updated_at=1777912789.2289824
- [2026-05-05 00:39:50] operator / voice_command / voice: do you smart resume current app behavior
  meta: normalized=True
- [2026-05-05 00:39:52] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:39:52] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777912792.0316477 | source=vosk | frequency_hz=256.0 | rms=272 | updated_at=1777912789.2289824
- [2026-05-05 00:39:52] operator / voice_transcript_partial / voice: repeat
  meta: kind=partial | timestamp=1777912792.236276 | source=vosk | frequency_hz=256.0 | rms=272 | updated_at=1777912789.2289824
- [2026-05-05 00:39:52] operator / voice_transcript_partial / voice: repeat it
  meta: kind=partial | timestamp=1777912792.484321 | source=vosk | frequency_hz=352.0 | rms=296 | updated_at=1777912792.478318
- [2026-05-05 00:39:52] operator / voice_transcript_final / voice: repeat it
  meta: kind=final | timestamp=1777912792.9970534 | source=final | frequency_hz=357.6 | rms=290 | updated_at=1777912792.7275624
- [2026-05-05 00:39:53] operator / voice_transcript_partial / voice: repeat
  meta: kind=partial | timestamp=1777912793.7479138 | source=vosk | frequency_hz=357.6 | rms=290 | updated_at=1777912792.7275624
- [2026-05-05 00:39:53] operator / voice_transcript_partial / voice: repeat it
  meta: kind=partial | timestamp=1777912793.9834826 | source=vosk | frequency_hz=357.6 | rms=290 | updated_at=1777912792.7275624
- [2026-05-05 00:39:54] operator / voice_transcript_partial / voice: repeat the elliot
  meta: kind=partial | timestamp=1777912794.4884288 | source=vosk | frequency_hz=357.6 | rms=290 | updated_at=1777912792.7275624
- [2026-05-05 00:39:54] operator / voice_transcript_partial / voice: repeat the elliot change
  meta: kind=partial | timestamp=1777912794.7349238 | source=vosk | frequency_hz=357.6 | rms=290 | updated_at=1777912792.7275624
- [2026-05-05 00:39:55] operator / voice_transcript_partial / voice: repeat it again
  meta: kind=partial | timestamp=1777912795.2338629 | source=vosk | frequency_hz=357.6 | rms=290 | updated_at=1777912792.7275624
- [2026-05-05 00:39:55] operator / voice_transcript_final / voice: repeat e
  meta: kind=final | timestamp=1777912795.555148 | source=final | frequency_hz=357.6 | rms=290 | updated_at=1777912792.7275624
- [2026-05-05 00:39:56] operator / voice_command / voice: repeat e
  meta: normalized=True
- [2026-05-05 00:39:56] operator / voice_transcript_partial / voice: repeat
  meta: kind=partial | timestamp=1777912796.7344515 | source=vosk | frequency_hz=368.0 | rms=303 | updated_at=1777912795.9780104
- [2026-05-05 00:39:56] operator / voice_transcript_partial / voice: repeat it
  meta: kind=partial | timestamp=1777912796.9825773 | source=vosk | frequency_hz=368.0 | rms=303 | updated_at=1777912795.9780104
- [2026-05-05 00:39:57] operator / voice_transcript_partial / voice: repeat it again
  meta: kind=partial | timestamp=1777912797.2328804 | source=vosk | frequency_hz=368.0 | rms=303 | updated_at=1777912795.9780104
- [2026-05-05 00:39:57] operator / voice_transcript_partial / voice: repeat it decrease
  meta: kind=partial | timestamp=1777912797.4834754 | source=vosk | frequency_hz=368.0 | rms=303 | updated_at=1777912795.9780104
- [2026-05-05 00:39:58] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:39:58] operator / voice_transcript_final / voice: repeat it decrease speed
  meta: kind=final | timestamp=1777912798.7451804 | source=final | frequency_hz=332.0 | rms=286 | updated_at=1777912797.9770746
- [2026-05-05 00:39:59] operator / voice_command / voice: repeat it decrease speed
  meta: normalized=True
- [2026-05-05 00:39:58] operator / voice_transcript_partial / voice: repeat it
  meta: kind=partial | timestamp=1777912798.9937525 | source=vosk | frequency_hz=332.0 | rms=286 | updated_at=1777912797.9770746
- [2026-05-05 00:39:59] operator / voice_transcript_partial / voice: repeat it decrease
  meta: kind=partial | timestamp=1777912799.233695 | source=vosk | frequency_hz=332.0 | rms=286 | updated_at=1777912797.9770746
- [2026-05-05 00:39:59] operator / voice_transcript_partial / voice: repeat it commands
  meta: kind=partial | timestamp=1777912799.4927833 | source=vosk | frequency_hz=332.0 | rms=286 | updated_at=1777912797.9770746
- [2026-05-05 00:39:59] operator / voice_transcript_partial / voice: repeat it to com alien
  meta: kind=partial | timestamp=1777912799.9900644 | source=vosk | frequency_hz=332.0 | rms=286 | updated_at=1777912797.9770746
- [2026-05-05 00:40:01] operator / voice_transcript_final / voice: repeat it to com
  meta: kind=final | timestamp=1777912801.0073688 | source=final | frequency_hz=332.0 | rms=286 | updated_at=1777912797.9770746
- [2026-05-05 00:40:01] operator / voice_command / voice: repeat it to com
  meta: normalized=True
- [2026-05-05 00:40:01] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777912801.4905198 | source=vosk | frequency_hz=332.0 | rms=286 | updated_at=1777912797.9770746
- [2026-05-05 00:40:01] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777912801.7324953 | source=vosk | frequency_hz=332.0 | rms=286 | updated_at=1777912797.9770746
- [2026-05-05 00:40:01] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777912801.9922833 | source=vosk | frequency_hz=332.0 | rms=286 | updated_at=1777912797.9770746
- [2026-05-05 00:40:02] operator / voice_transcript_partial / voice: smart change
  meta: kind=partial | timestamp=1777912802.2342002 | source=vosk | frequency_hz=332.0 | rms=286 | updated_at=1777912797.9770746
- [2026-05-05 00:40:02] operator / voice_transcript_partial / voice: smart resume guarding
  meta: kind=partial | timestamp=1777912802.738276 | source=vosk | frequency_hz=332.0 | rms=286 | updated_at=1777912797.9770746
- [2026-05-05 00:40:03] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:40:03] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:40:02] operator / voice_transcript_partial / voice: smart resume guarding mode
  meta: kind=partial | timestamp=1777912802.9864297 | source=vosk | frequency_hz=410.0 | rms=289 | updated_at=1777912802.9793272
- [2026-05-05 00:40:03] operator / voice_transcript_partial / voice: smart sentry current
  meta: kind=partial | timestamp=1777912803.232534 | source=vosk | frequency_hz=398.8 | rms=280 | updated_at=1777912803.2275207
- [2026-05-05 00:40:03] operator / voice_transcript_final / voice: resume guarding mode
  meta: kind=final | timestamp=1777912803.7491674 | source=final | frequency_hz=398.8 | rms=280 | updated_at=1777912803.2275207
- [2026-05-05 00:40:04] operator / voice_command / voice: resume guarding mode
  meta: normalized=True
- [2026-05-05 00:40:04] operator / voice_transcript_partial / voice: resume
  meta: kind=partial | timestamp=1777912804.7341921 | source=vosk | frequency_hz=398.8 | rms=280 | updated_at=1777912803.2275207
- [2026-05-05 00:40:05] operator / voice_transcript_partial / voice: decrease speed
  meta: kind=partial | timestamp=1777912805.015539 | source=vosk | frequency_hz=398.8 | rms=280 | updated_at=1777912803.2275207
- [2026-05-05 00:40:05] operator / voice_transcript_final / voice: decrease speed
  meta: kind=final | timestamp=1777912805.5286605 | source=final | frequency_hz=398.8 | rms=280 | updated_at=1777912803.2275207
- [2026-05-05 00:40:05] operator / voice_command / voice: decrease speed
  meta: normalized=True
- [2026-05-05 00:40:05] operator / voice_transcript_partial / voice: elliot
  meta: kind=partial | timestamp=1777912805.7334578 | source=vosk | frequency_hz=398.8 | rms=280 | updated_at=1777912803.2275207
- [2026-05-05 00:40:05] operator / voice_transcript_partial / voice: elliot be
  meta: kind=partial | timestamp=1777912805.9911945 | source=vosk | frequency_hz=398.8 | rms=280 | updated_at=1777912803.2275207
- [2026-05-05 00:40:06] operator / voice_transcript_partial / voice: repeat
  meta: kind=partial | timestamp=1777912806.2329652 | source=vosk | frequency_hz=398.8 | rms=280 | updated_at=1777912803.2275207
- [2026-05-05 00:40:07] operator / voice_transcript_final / voice: repeat
  meta: kind=final | timestamp=1777912807.2572217 | source=final | frequency_hz=332.0 | rms=278 | updated_at=1777912806.478822
- [2026-05-05 00:40:07] operator / voice_command / voice: repeat
  meta: normalized=True
- [2026-05-05 00:40:08] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777912808.4936042 | source=vosk | frequency_hz=332.0 | rms=283 | updated_at=1777912807.7285466
- [2026-05-05 00:40:08] operator / voice_transcript_partial / voice: queue
  meta: kind=partial | timestamp=1777912808.7496202 | source=vosk | frequency_hz=333.4 | rms=253 | updated_at=1777912808.7307026
- [2026-05-05 00:40:09] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:40:09] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:40:09] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:40:09] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777912809.7494392 | source=vosk | frequency_hz=333.4 | rms=253 | updated_at=1777912808.7307026
- [2026-05-05 00:40:09] operator / voice_transcript_partial / voice: resume
  meta: kind=partial | timestamp=1777912809.9943478 | source=vosk | frequency_hz=333.4 | rms=253 | updated_at=1777912808.7307026
- [2026-05-05 00:40:10] operator / voice_transcript_partial / voice: be
  meta: kind=partial | timestamp=1777912810.2340662 | source=vosk | frequency_hz=333.4 | rms=253 | updated_at=1777912808.7307026
- [2026-05-05 00:40:10] operator / voice_transcript_partial / voice: be repeat
  meta: kind=partial | timestamp=1777912810.4836915 | source=vosk | frequency_hz=333.4 | rms=253 | updated_at=1777912808.7307026
- [2026-05-05 00:40:10] operator / voice_transcript_partial / voice: be repeat that be
  meta: kind=partial | timestamp=1777912810.9924965 | source=vosk | frequency_hz=333.4 | rms=253 | updated_at=1777912808.7307026
- [2026-05-05 00:40:11] operator / voice_transcript_partial / voice: be repeat that be a
  meta: kind=partial | timestamp=1777912811.7474716 | source=vosk | frequency_hz=292.0 | rms=273 | updated_at=1777912811.2285383
- [2026-05-05 00:40:11] operator / voice_transcript_partial / voice: be repeat that be e
  meta: kind=partial | timestamp=1777912811.9837637 | source=vosk | frequency_hz=292.0 | rms=273 | updated_at=1777912811.2285383
- [2026-05-05 00:40:12] operator / voice_transcript_partial / voice: be repeat that be e lion
  meta: kind=partial | timestamp=1777912812.2538393 | source=vosk | frequency_hz=292.0 | rms=273 | updated_at=1777912811.2285383
- [2026-05-05 00:40:12] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:40:13] operator / voice_transcript_partial / voice: be repeat that be alien clear
  meta: kind=partial | timestamp=1777912813.6970532 | source=vosk | frequency_hz=292.0 | rms=273 | updated_at=1777912811.2285383
- [2026-05-05 00:40:13] operator / voice_transcript_partial / voice: be repeat that be e resume last
  meta: kind=partial | timestamp=1777912813.723115 | source=vosk | frequency_hz=292.0 | rms=273 | updated_at=1777912811.2285383
- [2026-05-05 00:40:14] operator / voice_transcript_final / voice: be repeat that be a e resume last
  meta: kind=final | timestamp=1777912814.6623912 | source=final | frequency_hz=292.0 | rms=273 | updated_at=1777912811.2285383
- [2026-05-05 00:40:15] operator / voice_command / voice: be repeat that be a e resume last
  meta: normalized=True
- [2026-05-05 00:40:15] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777912815.681266 | source=vosk | frequency_hz=292.0 | rms=273 | updated_at=1777912811.2285383
- [2026-05-05 00:40:15] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777912815.9198003 | source=vosk | frequency_hz=292.0 | rms=273 | updated_at=1777912811.2285383
- [2026-05-05 00:40:16] operator / voice_transcript_partial / voice: smart sentry say
  meta: kind=partial | timestamp=1777912816.6856735 | source=vosk | frequency_hz=292.0 | rms=273 | updated_at=1777912811.2285383
- [2026-05-05 00:40:16] operator / voice_transcript_partial / voice: smart sentry silence threshold
  meta: kind=partial | timestamp=1777912816.920011 | source=vosk | frequency_hz=268.0 | rms=264 | updated_at=1777912816.9135013
- [2026-05-05 00:40:17] operator / voice_transcript_final / voice: smart sentry say tasks
  meta: kind=final | timestamp=1777912817.4553888 | source=final | frequency_hz=262.4 | rms=276 | updated_at=1777912817.3176565
- [2026-05-05 00:40:17] operator / voice_command / voice: smart sentry say tasks
  meta: normalized=True
- [2026-05-05 00:40:18] operator / voice_transcript_partial / voice: threshold
  meta: kind=partial | timestamp=1777912818.9182217 | source=vosk | frequency_hz=327.4 | rms=278 | updated_at=1777912818.6636662
- [2026-05-05 00:40:19] operator / voice_transcript_partial / voice: tracking priority
  meta: kind=partial | timestamp=1777912819.418449 | source=vosk | frequency_hz=327.4 | rms=278 | updated_at=1777912818.6636662
- [2026-05-05 00:40:19] operator / voice_transcript_partial / voice: tracking
  meta: kind=partial | timestamp=1777912819.739485 | source=vosk | frequency_hz=327.4 | rms=278 | updated_at=1777912818.6636662
- [2026-05-05 00:40:19] operator / voice_transcript_partial / voice: tracking boards
  meta: kind=partial | timestamp=1777912819.9526196 | source=vosk | frequency_hz=298.2 | rms=282 | updated_at=1777912819.9202533
- [2026-05-05 00:40:20] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777912820.1706583 | source=vosk | frequency_hz=276.4 | rms=277 | updated_at=1777912820.1646547
- [2026-05-05 00:40:20] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:40:21] operator / voice_transcript_partial / voice: tracking boards who serial
  meta: kind=partial | timestamp=1777912821.418527 | source=vosk | frequency_hz=296.3 | rms=278 | updated_at=1777912820.6710446
- [2026-05-05 00:40:21] operator / voice_transcript_partial / voice: tracking boards who serial app
  meta: kind=partial | timestamp=1777912821.9188673 | source=vosk | frequency_hz=296.3 | rms=278 | updated_at=1777912820.6710446
- [2026-05-05 00:40:22] operator / voice_transcript_partial / voice: tracking boards who serial app to the
  meta: kind=partial | timestamp=1777912822.1982167 | source=vosk | frequency_hz=296.3 | rms=278 | updated_at=1777912820.6710446
- [2026-05-05 00:40:22] operator / voice_transcript_partial / voice: tracking boards who serial app to anything
  meta: kind=partial | timestamp=1777912822.5158222 | source=vosk | frequency_hz=296.3 | rms=278 | updated_at=1777912820.6710446
- [2026-05-05 00:40:22] operator / voice_transcript_partial / voice: tracking boards who serial app to the theme to
  meta: kind=partial | timestamp=1777912822.6704404 | source=vosk | frequency_hz=296.3 | rms=278 | updated_at=1777912820.6710446
- [2026-05-05 00:40:23] operator / voice_transcript_partial / voice: tracking boards who serial app to the theme to board
  meta: kind=partial | timestamp=1777912823.3113117 | source=vosk | frequency_hz=296.3 | rms=278 | updated_at=1777912820.6710446
- [2026-05-05 00:40:23] operator / voice_transcript_partial / voice: tracking boards who serial app to the theme to board ports
  meta: kind=partial | timestamp=1777912823.4185712 | source=vosk | frequency_hz=296.3 | rms=278 | updated_at=1777912820.6710446
- [2026-05-05 00:40:23] operator / voice_transcript_partial / voice: tracking boards who serial app to the theme to board ports in queue
  meta: kind=partial | timestamp=1777912823.683762 | source=vosk | frequency_hz=312.0 | rms=282 | updated_at=1777912823.6676118
- [2026-05-05 00:40:24] operator / voice_transcript_final / voice: tracking boards who serial app to the theme to board ports in queue
  meta: kind=final | timestamp=1777912824.1720293 | source=final | frequency_hz=316.5 | rms=281 | updated_at=1777912824.1633523
- [2026-05-05 00:40:27] operator / voice_command / voice: tracking boards who serial app to the theme to board ports in queue
  meta: normalized=True
- [2026-05-05 00:40:27] operator / voice_transcript_partial / voice: check status
  meta: kind=partial | timestamp=1777912827.176791 | source=vosk | frequency_hz=344.8 | rms=259 | updated_at=1777912825.6638644
- [2026-05-05 00:40:27] operator / voice_transcript_partial / voice: check app
  meta: kind=partial | timestamp=1777912827.424352 | source=vosk | frequency_hz=344.8 | rms=259 | updated_at=1777912825.6638644
- [2026-05-05 00:40:27] operator / voice_transcript_partial / voice: check app brightness
  meta: kind=partial | timestamp=1777912827.6679766 | source=vosk | frequency_hz=344.8 | rms=259 | updated_at=1777912825.6638644
- [2026-05-05 00:40:28] operator / voice_transcript_final / voice: check app brightness
  meta: kind=final | timestamp=1777912828.7357342 | source=final | frequency_hz=400.0 | rms=316 | updated_at=1777912828.6648273
- [2026-05-05 00:40:29] operator / voice_command / voice: check app brightness
  meta: normalized=True
- [2026-05-05 00:40:30] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:40:30] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:40:30] operator / voice_transcript_partial / voice: check status
  meta: kind=partial | timestamp=1777912830.1711173 | source=vosk | frequency_hz=358.0 | rms=299 | updated_at=1777912829.421942
- [2026-05-05 00:40:30] operator / voice_transcript_partial / voice: check brightness
  meta: kind=partial | timestamp=1777912830.4299474 | source=vosk | frequency_hz=358.0 | rms=299 | updated_at=1777912829.421942
- [2026-05-05 00:40:30] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777912830.6686077 | source=vosk | frequency_hz=358.0 | rms=299 | updated_at=1777912829.421942
- [2026-05-05 00:40:33] operator / voice_transcript_partial / voice: check app behavior elliot decrease
  meta: kind=partial | timestamp=1777912833.420331 | source=vosk | frequency_hz=256.0 | rms=267 | updated_at=1777912833.4133213
- [2026-05-05 00:40:33] operator / voice_transcript_partial / voice: check app behavior elliot decrease but
  meta: kind=partial | timestamp=1777912833.919435 | source=vosk | frequency_hz=256.0 | rms=267 | updated_at=1777912833.4133213
- [2026-05-05 00:40:34] operator / voice_transcript_partial / voice: check app behavior elliot decrease but faster
  meta: kind=partial | timestamp=1777912834.170937 | source=vosk | frequency_hz=256.0 | rms=267 | updated_at=1777912833.4133213
- [2026-05-05 00:40:34] operator / voice_transcript_partial / voice: check app behavior elliot decrease but resume
  meta: kind=partial | timestamp=1777912834.4187596 | source=vosk | frequency_hz=256.0 | rms=267 | updated_at=1777912833.4133213
- [2026-05-05 00:40:34] operator / voice_transcript_partial / voice: check app behavior elliot decrease but resume last
  meta: kind=partial | timestamp=1777912834.6722503 | source=vosk | frequency_hz=256.0 | rms=267 | updated_at=1777912833.4133213
- [2026-05-05 00:40:34] operator / voice_transcript_partial / voice: check app behavior elliot decrease but resume status
  meta: kind=partial | timestamp=1777912834.9206567 | source=vosk | frequency_hz=256.0 | rms=267 | updated_at=1777912833.4133213
- [2026-05-05 00:40:35] operator / voice_transcript_partial / voice: check app behavior elliot decrease but disable the current
  meta: kind=partial | timestamp=1777912835.1736717 | source=vosk | frequency_hz=256.0 | rms=267 | updated_at=1777912833.4133213
- [2026-05-05 00:40:35] operator / voice_transcript_partial / voice: check app behavior elliot decrease but disable the
  meta: kind=partial | timestamp=1777912835.421126 | source=vosk | frequency_hz=256.0 | rms=267 | updated_at=1777912833.4133213
- [2026-05-05 00:40:35] operator / voice_transcript_partial / voice: check app behavior elliot decrease but disable the current change
  meta: kind=partial | timestamp=1777912835.678271 | source=vosk | frequency_hz=256.0 | rms=267 | updated_at=1777912833.4133213
- [2026-05-05 00:40:36] operator / voice_transcript_partial / voice: check app behavior elliot decrease but disable the current change smart
  meta: kind=partial | timestamp=1777912836.1693888 | source=vosk | frequency_hz=256.0 | rms=267 | updated_at=1777912833.4133213
- [2026-05-05 00:40:36] operator / voice_transcript_partial / voice: check app behavior elliot decrease but disable the current change smart sentry
  meta: kind=partial | timestamp=1777912836.4226942 | source=vosk | frequency_hz=256.0 | rms=267 | updated_at=1777912833.4133213
- [2026-05-05 00:40:36] operator / voice_transcript_partial / voice: check app behavior elliot decrease but disable the current change smart sensitivity
  meta: kind=partial | timestamp=1777912836.9206529 | source=vosk | frequency_hz=256.0 | rms=267 | updated_at=1777912833.4133213
- [2026-05-05 00:40:37] operator / voice_transcript_partial / voice: check app behavior elliot decrease but disable the current change smart sentry status
  meta: kind=partial | timestamp=1777912837.170474 | source=vosk | frequency_hz=256.0 | rms=267 | updated_at=1777912833.4133213
- [2026-05-05 00:40:37] operator / voice_transcript_final / voice: disable smart sentry
  meta: kind=final | timestamp=1777912837.9218085 | source=final | frequency_hz=305.8 | rms=265 | updated_at=1777912837.91428
- [2026-05-05 00:40:38] operator / voice_command / voice: disable smart sentry
  meta: normalized=True
- [2026-05-05 00:40:39] assistant / spoken_confirmation / voice: Pausing Smart Sentry now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:40:43] operator / voice_transcript_partial / voice: brightness
  meta: kind=partial | timestamp=1777912843.1691678 | source=vosk | frequency_hz=256.4 | rms=269 | updated_at=1777912842.4141898
- [2026-05-05 00:40:43] operator / voice_transcript_partial / voice: repeat
  meta: kind=partial | timestamp=1777912843.419095 | source=vosk | frequency_hz=256.4 | rms=269 | updated_at=1777912842.4141898
- [2026-05-05 00:40:44] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777912844.421681 | source=final | frequency_hz=372.0 | rms=250 | updated_at=1777912844.1646087
- [2026-05-05 00:40:44] operator / voice_command / voice: unk
  meta: normalized=True
- [2026-05-05 00:40:45] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:40:46] operator / voice_transcript_partial / voice: queued tasks
  meta: kind=partial | timestamp=1777912846.679311 | source=vosk | frequency_hz=354.4 | rms=244 | updated_at=1777912844.9136934
- [2026-05-05 00:40:46] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777912846.9245872 | source=vosk | frequency_hz=354.4 | rms=244 | updated_at=1777912844.9136934
- [2026-05-05 00:40:47] operator / voice_transcript_partial / voice: serial
  meta: kind=partial | timestamp=1777912847.1705503 | source=vosk | frequency_hz=354.4 | rms=244 | updated_at=1777912844.9136934
- [2026-05-05 00:40:47] operator / voice_transcript_final / voice: port serial
  meta: kind=final | timestamp=1777912847.7014716 | source=final | frequency_hz=291.0 | rms=272 | updated_at=1777912847.6639302
- [2026-05-05 00:40:48] operator / voice_command / voice: port serial
  meta: normalized=True
- [2026-05-05 00:40:49] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:40:50] operator / voice_transcript_partial / voice: the smart
  meta: kind=partial | timestamp=1777912850.4195964 | source=vosk | frequency_hz=306.0 | rms=276 | updated_at=1777912849.9144006
- [2026-05-05 00:40:50] operator / voice_transcript_partial / voice: last
  meta: kind=partial | timestamp=1777912850.9344757 | source=vosk | frequency_hz=306.0 | rms=276 | updated_at=1777912849.9144006
- [2026-05-05 00:40:51] operator / voice_transcript_partial / voice: last change
  meta: kind=partial | timestamp=1777912851.6712005 | source=vosk | frequency_hz=306.0 | rms=276 | updated_at=1777912849.9144006
- [2026-05-05 00:40:51] operator / voice_transcript_partial / voice: less strict on
  meta: kind=partial | timestamp=1777912851.919291 | source=vosk | frequency_hz=306.0 | rms=276 | updated_at=1777912849.9144006
- [2026-05-05 00:40:52] operator / voice_transcript_partial / voice: less strict on commands
  meta: kind=partial | timestamp=1777912852.1697743 | source=vosk | frequency_hz=306.0 | rms=276 | updated_at=1777912849.9144006
- [2026-05-05 00:40:52] operator / voice_transcript_partial / voice: less strict on current
  meta: kind=partial | timestamp=1777912852.422457 | source=vosk | frequency_hz=306.0 | rms=276 | updated_at=1777912849.9144006
- [2026-05-05 00:40:53] operator / voice_transcript_final / voice: last change on current
  meta: kind=final | timestamp=1777912853.4243844 | source=final | frequency_hz=312.0 | rms=260 | updated_at=1777912853.1642468
- [2026-05-05 00:40:56] operator / voice_transcript_partial / voice: repeat
  meta: kind=partial | timestamp=1777912856.6691692 | source=vosk | frequency_hz=335.9 | rms=269 | updated_at=1777912855.6638446
- [2026-05-05 00:40:57] operator / voice_transcript_partial / voice: repeat do you
  meta: kind=partial | timestamp=1777912857.1692958 | source=vosk | frequency_hz=280.0 | rms=261 | updated_at=1777912857.1637838
- [2026-05-05 00:40:58] operator / voice_transcript_final / voice: repeat do you
  meta: kind=final | timestamp=1777912858.4283442 | source=final | frequency_hz=266.0 | rms=251 | updated_at=1777912857.414654
- [2026-05-05 00:40:59] operator / voice_transcript_partial / voice: again
  meta: kind=partial | timestamp=1777912859.8792715 | source=vosk | frequency_hz=293.4 | rms=892 | updated_at=1777912859.6225147
- [2026-05-05 00:41:00] operator / voice_transcript_partial / voice: to com
  meta: kind=partial | timestamp=1777912860.1337247 | source=vosk | frequency_hz=293.4 | rms=892 | updated_at=1777912859.6225147
- [2026-05-05 00:41:00] operator / voice_transcript_final / voice: com mode
  meta: kind=final | timestamp=1777912860.8144202 | source=final | frequency_hz=276.1 | rms=803 | updated_at=1777912860.372792
- [2026-05-05 00:41:06] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777912866.3773842 | source=vosk | frequency_hz=288.6 | rms=265 | updated_at=1777912865.872003
- [2026-05-05 00:41:06] operator / voice_transcript_partial / voice: do it again
  meta: kind=partial | timestamp=1777912866.6284833 | source=vosk | frequency_hz=288.6 | rms=265 | updated_at=1777912865.872003
- [2026-05-05 00:41:07] operator / voice_transcript_final / voice: do it again
  meta: kind=final | timestamp=1777912867.1317682 | source=final | frequency_hz=315.7 | rms=293 | updated_at=1777912867.1222389
- [2026-05-05 00:41:27] operator / voice_command / voice: do it again
  meta: normalized=True
- [2026-05-05 00:41:10] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777912870.6293116 | source=vosk | frequency_hz=299.1 | rms=271 | updated_at=1777912869.3722048
- [2026-05-05 00:41:11] operator / voice_transcript_final / voice: go
  meta: kind=final | timestamp=1777912871.3776443 | source=final | frequency_hz=282.0 | rms=256 | updated_at=1777912871.121719
- [2026-05-05 00:41:27] operator / voice_command / voice: go
  meta: normalized=True
- [2026-05-05 00:41:11] operator / voice_transcript_partial / voice: queue
  meta: kind=partial | timestamp=1777912871.8786447 | source=vosk | frequency_hz=282.0 | rms=256 | updated_at=1777912871.121719
- [2026-05-05 00:41:12] operator / voice_transcript_partial / voice: queue queue
  meta: kind=partial | timestamp=1777912872.1306489 | source=vosk | frequency_hz=282.0 | rms=256 | updated_at=1777912871.121719
- [2026-05-05 00:41:12] operator / voice_transcript_final / voice: queue queue
  meta: kind=final | timestamp=1777912872.9651763 | source=final | frequency_hz=282.0 | rms=256 | updated_at=1777912871.121719
- [2026-05-05 00:41:27] operator / voice_command / voice: queue queue
  meta: normalized=True
- [2026-05-05 00:41:13] operator / voice_transcript_partial / voice: board
  meta: kind=partial | timestamp=1777912873.6292143 | source=vosk | frequency_hz=366.0 | rms=298 | updated_at=1777912873.12378
- [2026-05-05 00:41:14] operator / voice_transcript_final / voice: board
  meta: kind=final | timestamp=1777912874.2086504 | source=final | frequency_hz=366.0 | rms=298 | updated_at=1777912873.12378
- [2026-05-05 00:41:27] operator / voice_command / voice: board
  meta: normalized=True
- [2026-05-05 00:41:25] operator / voice_transcript_partial / voice: last
  meta: kind=partial | timestamp=1777912885.628148 | source=vosk | frequency_hz=351.8 | rms=258 | updated_at=1777912885.1230688
- [2026-05-05 00:41:26] operator / voice_transcript_partial / voice: last what
  meta: kind=partial | timestamp=1777912886.1286607 | source=vosk | frequency_hz=360.3 | rms=298 | updated_at=1777912885.8732297
- [2026-05-05 00:41:26] operator / voice_transcript_partial / voice: last what do
  meta: kind=partial | timestamp=1777912886.3787436 | source=vosk | frequency_hz=360.3 | rms=298 | updated_at=1777912885.8732297
- [2026-05-05 00:41:28] operator / voice_command / voice: disable smart sentry
  meta: normalized=True
- [2026-05-05 00:41:27] operator / voice_transcript_final / voice: last what
  meta: kind=final | timestamp=1777912887.1702592 | source=final | frequency_hz=360.3 | rms=298 | updated_at=1777912885.8732297
- [2026-05-05 00:41:28] operator / voice_transcript_partial / voice: less
  meta: kind=partial | timestamp=1777912888.1301398 | source=vosk | frequency_hz=286.0 | rms=283 | updated_at=1777912887.6239917
- [2026-05-05 00:41:28] operator / voice_transcript_partial / voice: last
  meta: kind=partial | timestamp=1777912888.3791704 | source=vosk | frequency_hz=286.0 | rms=283 | updated_at=1777912887.6239917
- [2026-05-05 00:41:28] operator / voice_transcript_partial / voice: last last
  meta: kind=partial | timestamp=1777912888.6286893 | source=vosk | frequency_hz=289.5 | rms=268 | updated_at=1777912888.6228795
- [2026-05-05 00:41:29] operator / voice_transcript_final / voice: last last
  meta: kind=final | timestamp=1777912889.8118348 | source=final | frequency_hz=289.5 | rms=268 | updated_at=1777912888.6228795
- [2026-05-05 00:41:29] operator / voice_transcript_partial / voice: task
  meta: kind=partial | timestamp=1777912889.9011233 | source=vosk | frequency_hz=289.5 | rms=268 | updated_at=1777912888.6228795
- [2026-05-05 00:41:29] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777912889.9206803 | source=vosk | frequency_hz=289.5 | rms=268 | updated_at=1777912888.6228795
- [2026-05-05 00:41:30] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:41:31] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:41:31] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:41:31] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:41:32] operator / voice_transcript_partial / voice: less strict
  meta: kind=partial | timestamp=1777912892.847058 | source=vosk | frequency_hz=298.1 | rms=264 | updated_at=1777912892.841944
- [2026-05-05 00:41:34] operator / voice_transcript_final / voice: less
  meta: kind=final | timestamp=1777912894.6692007 | source=final | frequency_hz=261.9 | rms=274 | updated_at=1777912894.0929816
- [2026-05-05 00:41:34] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777912894.6758628 | source=vosk | frequency_hz=317.2 | rms=253 | updated_at=1777912894.669901
- [2026-05-05 00:41:35] operator / voice_transcript_partial / voice: lion who are
  meta: kind=partial | timestamp=1777912895.5981905 | source=vosk | frequency_hz=318.1 | rms=267 | updated_at=1777912895.094104
- [2026-05-05 00:41:35] operator / voice_transcript_partial / voice: lion who again
  meta: kind=partial | timestamp=1777912895.8492093 | source=vosk | frequency_hz=318.1 | rms=267 | updated_at=1777912895.094104
- [2026-05-05 00:41:36] operator / voice_transcript_partial / voice: lion who are you
  meta: kind=partial | timestamp=1777912896.1087277 | source=vosk | frequency_hz=318.1 | rms=267 | updated_at=1777912895.094104
- [2026-05-05 00:41:36] operator / voice_transcript_partial / voice: lion who are go
  meta: kind=partial | timestamp=1777912896.602448 | source=vosk | frequency_hz=318.1 | rms=267 | updated_at=1777912895.094104
- [2026-05-05 00:41:36] operator / voice_transcript_partial / voice: lion who are go rest
  meta: kind=partial | timestamp=1777912896.8593245 | source=vosk | frequency_hz=318.1 | rms=267 | updated_at=1777912895.094104
- [2026-05-05 00:41:37] operator / voice_transcript_partial / voice: lion who are go rest that again
  meta: kind=partial | timestamp=1777912897.101054 | source=vosk | frequency_hz=318.1 | rms=267 | updated_at=1777912895.094104
- [2026-05-05 00:41:37] operator / voice_transcript_partial / voice: lion who are go rest
  meta: kind=partial | timestamp=1777912897.3480115 | source=vosk | frequency_hz=224.0 | rms=262 | updated_at=1777912897.3422866
- [2026-05-05 00:41:37] operator / voice_transcript_final / voice: go rest
  meta: kind=final | timestamp=1777912897.6061423 | source=final | frequency_hz=236.6 | rms=264 | updated_at=1777912897.595535
- [2026-05-05 00:41:39] operator / voice_transcript_partial / voice: board
  meta: kind=partial | timestamp=1777912899.098619 | source=vosk | frequency_hz=236.6 | rms=264 | updated_at=1777912897.595535
- [2026-05-05 00:41:39] operator / voice_transcript_partial / voice: more strict
  meta: kind=partial | timestamp=1777912899.3522828 | source=vosk | frequency_hz=236.6 | rms=264 | updated_at=1777912897.595535
- [2026-05-05 00:41:39] operator / voice_transcript_partial / voice: boards you do
  meta: kind=partial | timestamp=1777912899.598462 | source=vosk | frequency_hz=236.6 | rms=264 | updated_at=1777912897.595535
- [2026-05-05 00:41:39] operator / voice_transcript_partial / voice: board sensitivity
  meta: kind=partial | timestamp=1777912899.8483424 | source=vosk | frequency_hz=236.6 | rms=264 | updated_at=1777912897.595535
- [2026-05-05 00:41:40] operator / voice_transcript_partial / voice: board sensitivity no
  meta: kind=partial | timestamp=1777912900.3491518 | source=vosk | frequency_hz=236.6 | rms=264 | updated_at=1777912897.595535
- [2026-05-05 00:41:40] operator / voice_transcript_partial / voice: board sensitivity less you
  meta: kind=partial | timestamp=1777912900.5981443 | source=vosk | frequency_hz=268.0 | rms=259 | updated_at=1777912900.5931306
- [2026-05-05 00:41:41] operator / voice_transcript_final / voice: board sensitivity less you
  meta: kind=final | timestamp=1777912901.929057 | source=final | frequency_hz=273.6 | rms=247 | updated_at=1777912900.8418636
- [2026-05-05 00:41:43] operator / voice_transcript_partial / voice: go home
  meta: kind=partial | timestamp=1777912903.9384532 | source=vosk | frequency_hz=247.8 | rms=265 | updated_at=1777912902.9313598
- [2026-05-05 00:41:44] operator / voice_transcript_partial / voice: go home and
  meta: kind=partial | timestamp=1777912904.1871817 | source=vosk | frequency_hz=247.8 | rms=265 | updated_at=1777912902.9313598
- [2026-05-05 00:41:44] operator / voice_transcript_partial / voice: go home and enable
  meta: kind=partial | timestamp=1777912904.4389133 | source=vosk | frequency_hz=247.8 | rms=265 | updated_at=1777912902.9313598
- [2026-05-05 00:41:44] operator / voice_transcript_partial / voice: go home and again app
  meta: kind=partial | timestamp=1777912904.9354732 | source=vosk | frequency_hz=247.8 | rms=265 | updated_at=1777912902.9313598
- [2026-05-05 00:41:45] operator / voice_transcript_final / voice: go home
  meta: kind=final | timestamp=1777912905.9378018 | source=final | frequency_hz=247.8 | rms=265 | updated_at=1777912902.9313598
- [2026-05-05 00:41:47] operator / voice_transcript_partial / voice: but that
  meta: kind=partial | timestamp=1777912907.9441462 | source=vosk | frequency_hz=412.0 | rms=274 | updated_at=1777912906.1808562
- [2026-05-05 00:41:48] operator / voice_transcript_partial / voice: but the last
  meta: kind=partial | timestamp=1777912908.1884112 | source=vosk | frequency_hz=412.0 | rms=274 | updated_at=1777912906.1808562
- [2026-05-05 00:41:48] operator / voice_transcript_partial / voice: but the go brightness
  meta: kind=partial | timestamp=1777912908.4473333 | source=vosk | frequency_hz=412.0 | rms=274 | updated_at=1777912906.1808562
- [2026-05-05 00:41:48] operator / voice_transcript_partial / voice: but the theme
  meta: kind=partial | timestamp=1777912908.6875546 | source=vosk | frequency_hz=412.0 | rms=274 | updated_at=1777912906.1808562
- [2026-05-05 00:41:48] operator / voice_transcript_partial / voice: but the theme alien
  meta: kind=partial | timestamp=1777912908.943477 | source=vosk | frequency_hz=396.0 | rms=273 | updated_at=1777912908.9314473
- [2026-05-05 00:41:49] operator / voice_transcript_partial / voice: but the theme anything else
  meta: kind=partial | timestamp=1777912909.1864722 | source=vosk | frequency_hz=373.6 | rms=262 | updated_at=1777912909.1814902
- [2026-05-05 00:41:49] operator / voice_transcript_final / voice: but the theme anything
  meta: kind=final | timestamp=1777912909.9375372 | source=final | frequency_hz=327.7 | rms=260 | updated_at=1777912909.688243
- [2026-05-05 00:41:50] operator / voice_command / voice: but the theme anything
  meta: normalized=True
- [2026-05-05 00:41:50] operator / voice_transcript_partial / voice: a lion
  meta: kind=partial | timestamp=1777912910.4409945 | source=vosk | frequency_hz=327.7 | rms=260 | updated_at=1777912909.688243
- [2026-05-05 00:41:50] operator / voice_transcript_partial / voice: enable
  meta: kind=partial | timestamp=1777912910.6875055 | source=vosk | frequency_hz=327.7 | rms=260 | updated_at=1777912909.688243
- [2026-05-05 00:41:51] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:41:51] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777912911.621227 | source=vosk | frequency_hz=339.0 | rms=277 | updated_at=1777912910.9315166
- [2026-05-05 00:41:53] operator / voice_transcript_partial / voice: [unk] resume last
  meta: kind=partial | timestamp=1777912913.883849 | source=vosk | frequency_hz=314.4 | rms=252 | updated_at=1777912913.1275928
- [2026-05-05 00:41:54] operator / voice_transcript_partial / voice: [unk] resume last no
  meta: kind=partial | timestamp=1777912914.3809578 | source=vosk | frequency_hz=314.4 | rms=252 | updated_at=1777912913.1275928
- [2026-05-05 00:41:54] operator / voice_transcript_partial / voice: [unk] resume last no change
  meta: kind=partial | timestamp=1777912914.8841038 | source=vosk | frequency_hz=314.4 | rms=252 | updated_at=1777912913.1275928
- [2026-05-05 00:41:55] operator / voice_transcript_final / voice: a unk resume last no change
  meta: kind=final | timestamp=1777912915.633252 | source=final | frequency_hz=356.0 | rms=259 | updated_at=1777912915.6267393
- [2026-05-05 00:41:55] operator / voice_command / voice: a unk resume last no change
  meta: normalized=True
- [2026-05-05 00:41:56] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:41:57] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777912917.132521 | source=vosk | frequency_hz=301.3 | rms=264 | updated_at=1777912916.3758361
- [2026-05-05 00:41:57] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777912917.3825505 | source=vosk | frequency_hz=301.3 | rms=264 | updated_at=1777912916.3758361
- [2026-05-05 00:41:57] operator / voice_transcript_partial / voice: decrease repeat
  meta: kind=partial | timestamp=1777912917.6333063 | source=vosk | frequency_hz=297.3 | rms=251 | updated_at=1777912917.6267328
- [2026-05-05 00:41:58] operator / voice_transcript_final / voice: decrease repeat
  meta: kind=final | timestamp=1777912918.3822157 | source=final | frequency_hz=299.5 | rms=266 | updated_at=1777912918.3761988
- [2026-05-05 00:41:58] operator / voice_command / voice: decrease repeat
  meta: normalized=True
- [2026-05-05 00:41:59] operator / voice_transcript_partial / voice: and enable
  meta: kind=partial | timestamp=1777912919.1323586 | source=vosk | frequency_hz=300.4 | rms=263 | updated_at=1777912918.6266384
- [2026-05-05 00:42:00] operator / voice_transcript_partial / voice: and to elliot
  meta: kind=partial | timestamp=1777912920.135811 | source=vosk | frequency_hz=316.0 | rms=265 | updated_at=1777912920.1303039
- [2026-05-05 00:42:00] operator / voice_transcript_final / voice: and to
  meta: kind=final | timestamp=1777912920.8823159 | source=final | frequency_hz=327.2 | rms=263 | updated_at=1777912920.3789265
- [2026-05-05 00:42:00] operator / voice_command / voice: and to
  meta: normalized=True
- [2026-05-05 00:42:01] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:42:01] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:42:04] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777912924.2668686 | source=vosk | frequency_hz=372.9 | rms=858 | updated_at=1777912923.261245
- [2026-05-05 00:42:04] operator / voice_transcript_partial / voice: and enable
  meta: kind=partial | timestamp=1777912924.516259 | source=vosk | frequency_hz=372.9 | rms=858 | updated_at=1777912923.261245
- [2026-05-05 00:42:04] operator / voice_transcript_partial / voice: a lion
  meta: kind=partial | timestamp=1777912924.7666695 | source=vosk | frequency_hz=372.9 | rms=858 | updated_at=1777912923.261245
- [2026-05-05 00:42:05] operator / voice_transcript_partial / voice: less
  meta: kind=partial | timestamp=1777912925.0190487 | source=vosk | frequency_hz=372.9 | rms=858 | updated_at=1777912923.261245
- [2026-05-05 00:42:05] operator / voice_transcript_final / voice: less
  meta: kind=final | timestamp=1777912925.518671 | source=final | frequency_hz=372.9 | rms=858 | updated_at=1777912923.261245
- [2026-05-05 00:42:29] operator / voice_command / voice: less
  meta: normalized=True
- [2026-05-05 00:42:06] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777912926.1074662 | source=vosk | frequency_hz=372.9 | rms=858 | updated_at=1777912923.261245
- [2026-05-05 00:42:06] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1777912926.1136787 | source=vosk | frequency_hz=372.9 | rms=858 | updated_at=1777912923.261245
- [2026-05-05 00:42:29] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:42:06] operator / voice_transcript_final / voice: e
  meta: kind=final | timestamp=1777912926.7685916 | source=final | frequency_hz=372.9 | rms=858 | updated_at=1777912923.261245
- [2026-05-05 00:42:30] operator / voice_command / voice: e
  meta: normalized=True
- [2026-05-05 00:42:08] operator / voice_transcript_partial / voice: speed
  meta: kind=partial | timestamp=1777912928.2680316 | source=vosk | frequency_hz=372.9 | rms=858 | updated_at=1777912923.261245
- [2026-05-05 00:42:08] operator / voice_transcript_partial / voice: repeat
  meta: kind=partial | timestamp=1777912928.5181608 | source=vosk | frequency_hz=372.9 | rms=858 | updated_at=1777912923.261245
- [2026-05-05 00:42:09] operator / voice_transcript_partial / voice: speed be more
  meta: kind=partial | timestamp=1777912929.017972 | source=vosk | frequency_hz=372.9 | rms=858 | updated_at=1777912923.261245
- [2026-05-05 00:42:09] operator / voice_transcript_partial / voice: repeat never
  meta: kind=partial | timestamp=1777912929.5177643 | source=vosk | frequency_hz=372.9 | rms=858 | updated_at=1777912923.261245
- [2026-05-05 00:42:09] operator / voice_transcript_partial / voice: repeat never mind
  meta: kind=partial | timestamp=1777912929.7680588 | source=vosk | frequency_hz=372.9 | rms=858 | updated_at=1777912923.261245
- [2026-05-05 00:42:10] operator / voice_transcript_final / voice: be repeat that
  meta: kind=final | timestamp=1777912930.0189734 | source=final | frequency_hz=372.9 | rms=858 | updated_at=1777912923.261245
- [2026-05-05 00:42:30] operator / voice_command / voice: be repeat that
  meta: normalized=True
- [2026-05-05 00:42:15] operator / voice_transcript_partial / voice: be
  meta: kind=partial | timestamp=1777912935.016241 | source=vosk | frequency_hz=364.4 | rms=518 | updated_at=1777912932.7612457
- [2026-05-05 00:42:15] operator / voice_transcript_partial / voice: and enable
  meta: kind=partial | timestamp=1777912935.2694058 | source=vosk | frequency_hz=364.4 | rms=518 | updated_at=1777912932.7612457
- [2026-05-05 00:42:15] operator / voice_transcript_partial / voice: repeat it again
  meta: kind=partial | timestamp=1777912935.7695694 | source=vosk | frequency_hz=364.4 | rms=518 | updated_at=1777912932.7612457
- [2026-05-05 00:42:16] operator / voice_transcript_partial / voice: abort current app
  meta: kind=partial | timestamp=1777912936.0188618 | source=vosk | frequency_hz=364.4 | rms=518 | updated_at=1777912932.7612457
- [2026-05-05 00:42:16] operator / voice_transcript_partial / voice: repeat it again
  meta: kind=partial | timestamp=1777912936.2678292 | source=vosk | frequency_hz=364.4 | rms=518 | updated_at=1777912932.7612457
- [2026-05-05 00:42:16] operator / voice_transcript_partial / voice: repeat it again do it
  meta: kind=partial | timestamp=1777912936.7669454 | source=vosk | frequency_hz=364.4 | rms=518 | updated_at=1777912932.7612457
- [2026-05-05 00:42:17] operator / voice_transcript_partial / voice: repeat it again do it boards
  meta: kind=partial | timestamp=1777912937.2701318 | source=vosk | frequency_hz=364.4 | rms=518 | updated_at=1777912932.7612457
- [2026-05-05 00:42:17] operator / voice_transcript_partial / voice: repeat it again do it boards and
  meta: kind=partial | timestamp=1777912937.51682 | source=vosk | frequency_hz=364.4 | rms=518 | updated_at=1777912932.7612457
- [2026-05-05 00:42:17] operator / voice_transcript_partial / voice: repeat it again do it boards tracking priority
  meta: kind=partial | timestamp=1777912937.7671614 | source=vosk | frequency_hz=364.4 | rms=518 | updated_at=1777912932.7612457
- [2026-05-05 00:42:18] operator / voice_transcript_partial / voice: repeat it again do it boards and enable
  meta: kind=partial | timestamp=1777912938.0179014 | source=vosk | frequency_hz=364.4 | rms=518 | updated_at=1777912932.7612457
- [2026-05-05 00:42:18] operator / voice_transcript_partial / voice: repeat it again do it boards tracking elian analyze
  meta: kind=partial | timestamp=1777912938.5182316 | source=vosk | frequency_hz=337.8 | rms=292 | updated_at=1777912938.511515
- [2026-05-05 00:42:30] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:42:19] operator / voice_transcript_final / voice: repeat it again again in boards tracking analyze com delay that
  meta: kind=final | timestamp=1777912939.5322678 | source=final | frequency_hz=337.8 | rms=292 | updated_at=1777912938.511515
- [2026-05-05 00:42:31] operator / voice_command / voice: repeat it again again in boards tracking analyze com delay that
  meta: normalized=True
- [2026-05-05 00:42:20] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777912940.0167851 | source=vosk | frequency_hz=337.8 | rms=292 | updated_at=1777912938.511515
- [2026-05-05 00:42:20] operator / voice_transcript_partial / voice: connect to
  meta: kind=partial | timestamp=1777912940.2665622 | source=vosk | frequency_hz=337.8 | rms=292 | updated_at=1777912938.511515
- [2026-05-05 00:42:20] operator / voice_transcript_partial / voice: connect to com
  meta: kind=partial | timestamp=1777912940.5163083 | source=vosk | frequency_hz=337.8 | rms=292 | updated_at=1777912938.511515
- [2026-05-05 00:42:20] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777912940.7692363 | source=final | frequency_hz=414.0 | rms=953 | updated_at=1777912940.7614937
- [2026-05-05 00:42:31] operator / voice_command / voice: unk
  meta: normalized=True
- [2026-05-05 00:42:30] operator / voice_transcript_partial / voice: identify
  meta: kind=partial | timestamp=1777912950.269393 | source=vosk | frequency_hz=326.8 | rms=277 | updated_at=1777912948.2625897
- [2026-05-05 00:42:31] operator / voice_command / voice: disable smart sentry
  meta: normalized=True
- [2026-05-05 00:42:30] operator / voice_transcript_partial / voice: aileen decrease
  meta: kind=partial | timestamp=1777912950.786267 | source=vosk | frequency_hz=326.8 | rms=277 | updated_at=1777912948.2625897
- [2026-05-05 00:42:31] operator / voice_transcript_partial / voice: aileen disconnect
  meta: kind=partial | timestamp=1777912951.0683274 | source=vosk | frequency_hz=326.8 | rms=277 | updated_at=1777912948.2625897
- [2026-05-05 00:42:31] operator / voice_transcript_final / voice: disconnect
  meta: kind=final | timestamp=1777912951.6041431 | source=final | frequency_hz=288.0 | rms=262 | updated_at=1777912951.264715
- [2026-05-05 00:42:32] operator / voice_command / voice: disconnect
  meta: normalized=True
- [2026-05-05 00:42:32] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777912952.7679775 | source=vosk | frequency_hz=329.5 | rms=237 | updated_at=1777912952.2623684
- [2026-05-05 00:42:33] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:42:33] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:42:34] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:42:33] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777912953.8634326 | source=vosk | frequency_hz=329.5 | rms=237 | updated_at=1777912952.2623684
- [2026-05-05 00:42:33] operator / voice_transcript_partial / voice: the current
  meta: kind=partial | timestamp=1777912953.8862212 | source=vosk | frequency_hz=329.5 | rms=237 | updated_at=1777912952.2623684
- [2026-05-05 00:42:33] operator / voice_transcript_partial / voice: check status
  meta: kind=partial | timestamp=1777912953.9124415 | source=vosk | frequency_hz=329.5 | rms=237 | updated_at=1777912952.2623684
- [2026-05-05 00:42:35] operator / voice_transcript_final / voice: check status
  meta: kind=final | timestamp=1777912955.0384145 | source=final | frequency_hz=92.0 | rms=891 | updated_at=1777912954.6201642
- [2026-05-05 00:42:35] operator / voice_command / voice: check status
  meta: normalized=True
- [2026-05-05 00:42:35] operator / voice_transcript_partial / voice: but
  meta: kind=partial | timestamp=1777912955.1523943 | source=vosk | frequency_hz=92.0 | rms=891 | updated_at=1777912954.6201642
- [2026-05-05 00:42:35] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777912955.3706799 | source=vosk | frequency_hz=92.0 | rms=891 | updated_at=1777912954.6201642
- [2026-05-05 00:42:35] operator / voice_transcript_partial / voice: [unk] go
  meta: kind=partial | timestamp=1777912955.872272 | source=vosk | frequency_hz=92.0 | rms=891 | updated_at=1777912954.6201642
- [2026-05-05 00:42:36] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777912956.1209738 | source=vosk | frequency_hz=92.0 | rms=891 | updated_at=1777912954.6201642
- [2026-05-05 00:42:39] operator / voice_transcript_partial / voice: [unk] change
  meta: kind=partial | timestamp=1777912959.372603 | source=vosk | frequency_hz=340.0 | rms=811 | updated_at=1777912958.615462
- [2026-05-05 00:42:39] operator / voice_transcript_partial / voice: [unk] change smart
  meta: kind=partial | timestamp=1777912959.6334684 | source=vosk | frequency_hz=340.0 | rms=811 | updated_at=1777912958.615462
- [2026-05-05 00:42:39] operator / voice_transcript_partial / voice: [unk] change smart sentry
  meta: kind=partial | timestamp=1777912959.8739638 | source=vosk | frequency_hz=340.0 | rms=811 | updated_at=1777912958.615462
- [2026-05-05 00:42:40] operator / voice_transcript_partial / voice: [unk] change smart sentry status
  meta: kind=partial | timestamp=1777912960.626049 | source=vosk | frequency_hz=340.0 | rms=811 | updated_at=1777912958.615462
- [2026-05-05 00:42:40] operator / voice_transcript_partial / voice: [unk] change smart sentry status report
  meta: kind=partial | timestamp=1777912960.870258 | source=vosk | frequency_hz=340.0 | rms=811 | updated_at=1777912958.615462
- [2026-05-05 00:42:41] operator / voice_transcript_partial / voice: [unk] change smart sentry status app
  meta: kind=partial | timestamp=1777912961.1214633 | source=vosk | frequency_hz=340.0 | rms=811 | updated_at=1777912958.615462
- [2026-05-05 00:42:41] operator / voice_transcript_final / voice: unk change smart sentry status app
  meta: kind=final | timestamp=1777912961.8795018 | source=final | frequency_hz=334.8 | rms=288 | updated_at=1777912961.6153908
- [2026-05-05 00:42:42] operator / voice_command / voice: unk change smart sentry status app
  meta: normalized=True
- [2026-05-05 00:42:43] operator / voice_transcript_partial / voice: yourself
  meta: kind=partial | timestamp=1777912963.1225395 | source=vosk | frequency_hz=334.8 | rms=288 | updated_at=1777912961.6153908
- [2026-05-05 00:42:43] operator / voice_transcript_partial / voice: yourself decrease
  meta: kind=partial | timestamp=1777912963.375783 | source=vosk | frequency_hz=334.8 | rms=288 | updated_at=1777912961.6153908
- [2026-05-05 00:42:43] operator / voice_transcript_partial / voice: you status report
  meta: kind=partial | timestamp=1777912963.627696 | source=vosk | frequency_hz=334.8 | rms=288 | updated_at=1777912961.6153908
- [2026-05-05 00:42:43] operator / voice_transcript_partial / voice: you status report theme it the
  meta: kind=partial | timestamp=1777912963.886852 | source=vosk | frequency_hz=334.8 | rms=288 | updated_at=1777912961.6153908
- [2026-05-05 00:42:44] operator / voice_transcript_partial / voice: you status report theme to anything
  meta: kind=partial | timestamp=1777912964.1261215 | source=vosk | frequency_hz=334.8 | rms=288 | updated_at=1777912961.6153908
- [2026-05-05 00:42:44] assistant / spoken_reply / voice: Smart Sentry is paused right now. Latest AI note. Analysis complete. Detection=Yolo Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1. 50s; face=off; pir=on. Enable at least one PIR sensor or disable PIR guard to match actual intent. End of analysys report.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-05 00:42:44] assistant / spoken_confirmation / voice: Received. I started your background analysis about unk change smart sentry status app in the background.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:42:44] operator / voice_transcript_partial / voice: you status report theme it the be
  meta: kind=partial | timestamp=1777912964.3857536 | source=vosk | frequency_hz=334.8 | rms=288 | updated_at=1777912961.6153908
- [2026-05-05 00:42:45] operator / voice_transcript_final / voice: you status app theme it the be
  meta: kind=final | timestamp=1777912965.1243303 | source=final | frequency_hz=334.8 | rms=288 | updated_at=1777912961.6153908
- [2026-05-05 00:42:45] operator / voice_command / voice: you status app theme it the be
  meta: normalized=True
- [2026-05-05 00:42:45] assistant / assistant_analysis / text: Assistant request queued: background analysis about you status app theme it the be (position 1).
  meta: task_kind=analysis | speak_requested=False
- [2026-05-05 00:42:46] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777912966.006079 | source=vosk | frequency_hz=334.8 | rms=288 | updated_at=1777912961.6153908
- [2026-05-05 00:42:46] operator / voice_transcript_partial / voice: same do
  meta: kind=partial | timestamp=1777912966.2510748 | source=vosk | frequency_hz=334.8 | rms=288 | updated_at=1777912961.6153908
- [2026-05-05 00:42:47] assistant / spoken_confirmation / voice: I am still finishing background analysis about unk change smart sentry status app. I queued your background analysis about you status app theme it the be. It is number 1 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:42:47] operator / voice_transcript_final / voice: same do
  meta: kind=final | timestamp=1777912967.160168 | source=final | frequency_hz=334.8 | rms=288 | updated_at=1777912961.6153908
- [2026-05-05 00:42:47] operator / voice_command / voice: same do
  meta: normalized=True
- [2026-05-05 00:42:49] operator / voice_transcript_partial / voice: silence
  meta: kind=partial | timestamp=1777912969.0000873 | source=vosk | frequency_hz=384.0 | rms=243 | updated_at=1777912967.1611674
- [2026-05-05 00:42:49] operator / voice_transcript_partial / voice: brightness
  meta: kind=partial | timestamp=1777912969.2601674 | source=vosk | frequency_hz=384.0 | rms=243 | updated_at=1777912967.1611674
- [2026-05-05 00:42:49] operator / voice_transcript_partial / voice: say no
  meta: kind=partial | timestamp=1777912969.4993696 | source=vosk | frequency_hz=384.0 | rms=243 | updated_at=1777912967.1611674
- [2026-05-05 00:42:49] operator / voice_transcript_partial / voice: brightness
  meta: kind=partial | timestamp=1777912969.7597046 | source=vosk | frequency_hz=384.0 | rms=243 | updated_at=1777912967.1611674
- [2026-05-05 00:42:50] operator / voice_transcript_final / voice: say no
  meta: kind=final | timestamp=1777912970.0417318 | source=final | frequency_hz=384.0 | rms=243 | updated_at=1777912967.1611674
- [2026-05-05 00:42:51] assistant / spoken_confirmation / voice: I think I heard disconnect. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:42:54] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777912974.3451056 | source=vosk | frequency_hz=340.9 | rms=235 | updated_at=1777912973.4937193
- [2026-05-05 00:42:54] operator / voice_transcript_partial / voice: status report
  meta: kind=partial | timestamp=1777912974.75374 | source=vosk | frequency_hz=340.9 | rms=235 | updated_at=1777912973.4937193
- [2026-05-05 00:42:54] operator / voice_transcript_partial / voice: status what
  meta: kind=partial | timestamp=1777912974.998919 | source=vosk | frequency_hz=340.9 | rms=235 | updated_at=1777912973.4937193
- [2026-05-05 00:42:55] operator / voice_transcript_partial / voice: status what do
  meta: kind=partial | timestamp=1777912975.248957 | source=vosk | frequency_hz=408.0 | rms=245 | updated_at=1777912975.2439516
- [2026-05-05 00:42:55] operator / voice_transcript_final / voice: status report
  meta: kind=final | timestamp=1777912975.7534723 | source=final | frequency_hz=405.2 | rms=250 | updated_at=1777912975.4938974
- [2026-05-05 00:42:56] operator / voice_transcript_partial / voice: elliot
  meta: kind=partial | timestamp=1777912976.2491224 | source=vosk | frequency_hz=405.2 | rms=250 | updated_at=1777912975.4938974
- [2026-05-05 00:42:56] operator / voice_transcript_partial / voice: elliot decrease
  meta: kind=partial | timestamp=1777912976.818468 | source=vosk | frequency_hz=405.2 | rms=250 | updated_at=1777912975.4938974
- [2026-05-05 00:42:56] operator / voice_transcript_partial / voice: elliot disconnect
  meta: kind=partial | timestamp=1777912976.8249855 | source=vosk | frequency_hz=405.2 | rms=250 | updated_at=1777912975.4938974
- [2026-05-05 00:42:57] operator / voice_transcript_partial / voice: elliot do you
  meta: kind=partial | timestamp=1777912977.011964 | source=vosk | frequency_hz=405.2 | rms=250 | updated_at=1777912975.4938974
- [2026-05-05 00:42:57] operator / voice_transcript_partial / voice: elliot decrease silence
  meta: kind=partial | timestamp=1777912977.2520106 | source=vosk | frequency_hz=405.2 | rms=250 | updated_at=1777912975.4938974
- [2026-05-05 00:42:57] operator / voice_transcript_partial / voice: elliot say
  meta: kind=partial | timestamp=1777912977.5093138 | source=vosk | frequency_hz=405.2 | rms=250 | updated_at=1777912975.4938974
- [2026-05-05 00:42:58] operator / voice_transcript_final / voice: do you sentry
  meta: kind=final | timestamp=1777912978.0366774 | source=final | frequency_hz=358.0 | rms=243 | updated_at=1777912977.9979944
- [2026-05-05 00:42:58] operator / voice_command / voice: do you sentry
  meta: normalized=True
- [2026-05-05 00:42:59] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:43:00] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777912980.750714 | source=vosk | frequency_hz=358.0 | rms=243 | updated_at=1777912977.9979944
- [2026-05-05 00:43:01] operator / voice_transcript_partial / voice: go queue
  meta: kind=partial | timestamp=1777912981.0030813 | source=vosk | frequency_hz=358.0 | rms=243 | updated_at=1777912977.9979944
- [2026-05-05 00:43:01] operator / voice_transcript_partial / voice: go queue disconnect
  meta: kind=partial | timestamp=1777912981.2604454 | source=vosk | frequency_hz=358.0 | rms=243 | updated_at=1777912977.9979944
- [2026-05-05 00:43:02] operator / voice_transcript_final / voice: go queue disconnect
  meta: kind=final | timestamp=1777912982.008333 | source=final | frequency_hz=358.0 | rms=243 | updated_at=1777912977.9979944
- [2026-05-05 00:43:02] operator / voice_command / voice: go queue disconnect
  meta: normalized=True
- [2026-05-05 00:43:03] operator / voice_transcript_partial / voice: sentry
  meta: kind=partial | timestamp=1777912983.0026364 | source=vosk | frequency_hz=358.0 | rms=243 | updated_at=1777912977.9979944
- [2026-05-05 00:43:03] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777912983.2501976 | source=vosk | frequency_hz=358.0 | rms=243 | updated_at=1777912977.9979944
- [2026-05-05 00:43:03] operator / voice_transcript_partial / voice: decrease response
  meta: kind=partial | timestamp=1777912983.753707 | source=vosk | frequency_hz=358.0 | rms=243 | updated_at=1777912977.9979944
- [2026-05-05 00:43:04] operator / voice_transcript_final / voice: theme
  meta: kind=final | timestamp=1777912984.0051422 | source=final | frequency_hz=358.0 | rms=243 | updated_at=1777912977.9979944
- [2026-05-05 00:43:04] operator / voice_command / voice: theme
  meta: normalized=True
- [2026-05-05 00:43:04] operator / voice_transcript_partial / voice: theme to
  meta: kind=partial | timestamp=1777912984.5013683 | source=vosk | frequency_hz=358.0 | rms=243 | updated_at=1777912977.9979944
- [2026-05-05 00:43:04] operator / voice_transcript_partial / voice: theme
  meta: kind=partial | timestamp=1777912984.7504785 | source=vosk | frequency_hz=358.0 | rms=243 | updated_at=1777912977.9979944
- [2026-05-05 00:43:05] operator / voice_transcript_final / voice: theme
  meta: kind=final | timestamp=1777912985.0037045 | source=final | frequency_hz=358.0 | rms=243 | updated_at=1777912977.9979944
- [2026-05-05 00:43:05] operator / voice_command / voice: theme
  meta: normalized=True
- [2026-05-05 00:43:05] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:43:05] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:43:06] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:43:10] operator / voice_transcript_final / voice: no
  meta: kind=final | timestamp=1777912990.3108022 | source=final | frequency_hz=358.0 | rms=243 | updated_at=1777912977.9979944
- [2026-05-05 00:43:10] operator / voice_command / voice: no
  meta: normalized=True
- [2026-05-05 00:43:12] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:43:15] operator / voice_transcript_partial / voice: less
  meta: kind=partial | timestamp=1777912995.3377054 | source=vosk | frequency_hz=400.0 | rms=247 | updated_at=1777912993.052488
- [2026-05-05 00:43:15] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777912995.5617313 | source=vosk | frequency_hz=400.0 | rms=247 | updated_at=1777912993.052488
- [2026-05-05 00:43:15] operator / voice_transcript_partial / voice: decrease response
  meta: kind=partial | timestamp=1777912995.8129852 | source=vosk | frequency_hz=400.0 | rms=247 | updated_at=1777912993.052488
- [2026-05-05 00:43:16] operator / voice_transcript_final / voice: decrease speed
  meta: kind=final | timestamp=1777912996.321891 | source=final | frequency_hz=400.0 | rms=247 | updated_at=1777912993.052488
- [2026-05-05 00:43:19] operator / voice_transcript_partial / voice: repeat
  meta: kind=partial | timestamp=1777912999.0586908 | source=vosk | frequency_hz=400.0 | rms=247 | updated_at=1777912993.052488
- [2026-05-05 00:43:20] operator / voice_transcript_final / voice: repeat
  meta: kind=final | timestamp=1777913000.0590084 | source=final | frequency_hz=400.0 | rms=247 | updated_at=1777912993.052488
- [2026-05-05 00:43:27] assistant / assistant_analysis / text: Assistant update. Analysis [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Local runtime analysis fallback: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=on; pir=on. Runtime facts: state=PAUSED | camera_open=True | yolo_loaded=True | mode=2 | tracking_scope=person | loss_protocols=rapid_handoff_search/persistent_reacquire_search | speed=100 trigger=water burst=6@70ms | return_delay=1.5 | guard_mode=2 guard_pan_tilt=140.0/83.0. Next step: Enable at least one PIR sensor or disable PIR guard to match actual intent. Supporting Findings: - [low] Active behavior profile: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=on; pir=on. - [medium] PIR guard enabled without active sensors: PIR guard is ON but no PIR sensor entries are enabled. - [low] Conversational mode is text-only: Conversational Voice mode is selected, but assistant auto-speak is turned off. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=analysis | speak_requested=False
- [2026-05-05 00:43:50] operator / voice_transcript_final / voice: that
  meta: kind=final | timestamp=1777913030.315844 | source=final | frequency_hz=290.0 | rms=289 | updated_at=1777913030.3025877
- [2026-05-05 00:43:55] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777913035.0628982 | source=vosk | frequency_hz=282.2 | rms=305 | updated_at=1777913034.05145
- [2026-05-05 00:43:58] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777913038.0592432 | source=vosk | frequency_hz=384.0 | rms=336 | updated_at=1777913035.5521562
- [2026-05-05 00:43:58] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777913038.311269 | source=vosk | frequency_hz=384.0 | rms=336 | updated_at=1777913035.5521562
- [2026-05-05 00:43:58] operator / voice_transcript_final / voice: do
  meta: kind=final | timestamp=1777913038.5661545 | source=final | frequency_hz=384.0 | rms=336 | updated_at=1777913035.5521562
- [2026-05-05 00:44:02] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777913042.057794 | source=vosk | frequency_hz=339.9 | rms=297 | updated_at=1777913040.3035507
- [2026-05-05 00:44:02] operator / voice_transcript_final / voice: do
  meta: kind=final | timestamp=1777913042.5620134 | source=final | frequency_hz=339.9 | rms=297 | updated_at=1777913040.3035507
- [2026-05-05 00:44:03] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777913043.5759044 | source=vosk | frequency_hz=339.9 | rms=297 | updated_at=1777913040.3035507
- [2026-05-05 00:44:04] operator / voice_transcript_partial / voice: to to
  meta: kind=partial | timestamp=1777913044.0619671 | source=vosk | frequency_hz=339.9 | rms=297 | updated_at=1777913040.3035507
- [2026-05-05 00:44:04] operator / voice_transcript_partial / voice: to queue
  meta: kind=partial | timestamp=1777913044.564654 | source=vosk | frequency_hz=339.9 | rms=297 | updated_at=1777913040.3035507
- [2026-05-05 00:44:05] operator / voice_transcript_partial / voice: do you do
  meta: kind=partial | timestamp=1777913045.0591593 | source=vosk | frequency_hz=339.9 | rms=297 | updated_at=1777913040.3035507
- [2026-05-05 00:44:05] operator / voice_transcript_final / voice: do you do
  meta: kind=final | timestamp=1777913045.8387148 | source=final | frequency_hz=339.9 | rms=297 | updated_at=1777913040.3035507
- [2026-05-05 00:44:10] operator / voice_transcript_final / voice: you
  meta: kind=final | timestamp=1777913050.8114836 | source=final | frequency_hz=350.9 | rms=1201 | updated_at=1777913049.3046339
- [2026-05-05 00:44:11] operator / voice_transcript_partial / voice: speed
  meta: kind=partial | timestamp=1777913051.309267 | source=vosk | frequency_hz=350.9 | rms=1201 | updated_at=1777913049.3046339
- [2026-05-05 00:44:11] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777913051.5618541 | source=vosk | frequency_hz=350.9 | rms=1201 | updated_at=1777913049.3046339
- [2026-05-05 00:44:12] operator / voice_transcript_partial / voice: response boards
  meta: kind=partial | timestamp=1777913052.0845778 | source=vosk | frequency_hz=350.9 | rms=1201 | updated_at=1777913049.3046339
- [2026-05-05 00:44:12] operator / voice_transcript_partial / voice: response boards current
  meta: kind=partial | timestamp=1777913052.30993 | source=vosk | frequency_hz=350.9 | rms=1201 | updated_at=1777913049.3046339
- [2026-05-05 00:44:12] operator / voice_transcript_final / voice: response unk
  meta: kind=final | timestamp=1777913052.8511405 | source=final | frequency_hz=350.9 | rms=1201 | updated_at=1777913049.3046339
- [2026-05-05 00:44:13] operator / voice_transcript_partial / voice: are
  meta: kind=partial | timestamp=1777913053.0691671 | source=vosk | frequency_hz=350.9 | rms=1201 | updated_at=1777913049.3046339
- [2026-05-05 00:44:13] assistant / assistant_analysis / text: Assistant update. Analysis [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Local runtime analysis fallback: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=on; pir=on. Runtime facts: state=PAUSED | camera_open=True | yolo_loaded=True | mode=2 | tracking_scope=person | loss_protocols=rapid_handoff_search/persistent_reacquire_search | speed=100 trigger=water burst=6@70ms | return_delay=1.5 | guard_mode=2 guard_pan_tilt=140.0/83.0. Next step: Enable at least one PIR sensor or disable PIR guard to match actual intent. Supporting Findings: - [low] Active behavior profile: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=on; pir=on. - [medium] PIR guard enabled without active sensors: PIR guard is ON but no PIR sensor entries are enabled. - [low] Conversational mode is text-only: Conversational Voice mode is selected, but assistant auto-speak is turned off. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=analysis | speak_requested=False
- [2026-05-05 00:44:13] operator / voice_transcript_partial / voice: yourself
  meta: kind=partial | timestamp=1777913053.3082733 | source=vosk | frequency_hz=350.9 | rms=1201 | updated_at=1777913049.3046339
- [2026-05-05 00:44:13] operator / voice_transcript_partial / voice: are smart
  meta: kind=partial | timestamp=1777913053.559076 | source=vosk | frequency_hz=350.9 | rms=1201 | updated_at=1777913049.3046339
- [2026-05-05 00:44:14] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777913054.1033995 | source=vosk | frequency_hz=350.9 | rms=1201 | updated_at=1777913049.3046339
- [2026-05-05 00:44:17] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777913057.8184137 | source=final | frequency_hz=264.4 | rms=292 | updated_at=1777913057.3021808
- [2026-05-05 00:44:39] operator / voice_transcript_partial / voice: resume
  meta: kind=partial | timestamp=1777913079.351819 | source=vosk | frequency_hz=392.0 | rms=708 | updated_at=1777913078.3507025
- [2026-05-05 00:44:39] operator / voice_transcript_partial / voice: boards yourself
  meta: kind=partial | timestamp=1777913079.6036408 | source=vosk | frequency_hz=392.0 | rms=708 | updated_at=1777913078.3507025
- [2026-05-05 00:44:39] operator / voice_transcript_partial / voice: resume threshold
  meta: kind=partial | timestamp=1777913079.8876693 | source=vosk | frequency_hz=392.0 | rms=708 | updated_at=1777913078.3507025
- [2026-05-05 00:44:40] operator / voice_transcript_partial / voice: resume
  meta: kind=partial | timestamp=1777913080.1094627 | source=vosk | frequency_hz=392.0 | rms=708 | updated_at=1777913078.3507025
- [2026-05-05 00:44:40] operator / voice_transcript_partial / voice: resume the
  meta: kind=partial | timestamp=1777913080.3559349 | source=vosk | frequency_hz=392.0 | rms=708 | updated_at=1777913078.3507025
- [2026-05-05 00:44:40] operator / voice_transcript_partial / voice: resume theme
  meta: kind=partial | timestamp=1777913080.610645 | source=vosk | frequency_hz=338.0 | rms=270 | updated_at=1777913080.5951245
- [2026-05-05 00:44:40] operator / voice_transcript_partial / voice: resume theme app
  meta: kind=partial | timestamp=1777913080.8609374 | source=vosk | frequency_hz=338.0 | rms=270 | updated_at=1777913080.5951245
- [2026-05-05 00:44:41] operator / voice_transcript_final / voice: resume theme it
  meta: kind=final | timestamp=1777913081.3781781 | source=final | frequency_hz=324.0 | rms=274 | updated_at=1777913081.3526347
- [2026-05-05 00:44:42] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777913082.6010866 | source=vosk | frequency_hz=295.3 | rms=257 | updated_at=1777913081.5946624
- [2026-05-05 00:44:43] operator / voice_transcript_partial / voice: resume
  meta: kind=partial | timestamp=1777913083.1159196 | source=vosk | frequency_hz=295.3 | rms=257 | updated_at=1777913081.5946624
- [2026-05-05 00:44:43] operator / voice_transcript_final / voice: resume
  meta: kind=final | timestamp=1777913083.867935 | source=final | frequency_hz=260.0 | rms=264 | updated_at=1777913083.5942976
- [2026-05-05 00:44:47] operator / voice_transcript_partial / voice: mind
  meta: kind=partial | timestamp=1777913087.8597934 | source=vosk | frequency_hz=304.7 | rms=281 | updated_at=1777913086.595186
- [2026-05-05 00:44:48] operator / voice_transcript_partial / voice: more strict
  meta: kind=partial | timestamp=1777913088.1000278 | source=vosk | frequency_hz=304.7 | rms=281 | updated_at=1777913086.595186
- [2026-05-05 00:44:48] operator / voice_transcript_final / voice: mind
  meta: kind=final | timestamp=1777913088.6014707 | source=final | frequency_hz=308.0 | rms=274 | updated_at=1777913088.3575683
- [2026-05-05 00:44:52] operator / voice_transcript_partial / voice: are you do
  meta: kind=partial | timestamp=1777913092.1002235 | source=vosk | frequency_hz=356.3 | rms=342 | updated_at=1777913091.5947397
- [2026-05-05 00:44:53] operator / voice_transcript_partial / voice: are you do but
  meta: kind=partial | timestamp=1777913093.1092725 | source=vosk | frequency_hz=312.0 | rms=272 | updated_at=1777913093.0954173
- [2026-05-05 00:44:53] operator / voice_transcript_partial / voice: are you do but faster
  meta: kind=partial | timestamp=1777913093.3521795 | source=vosk | frequency_hz=312.0 | rms=272 | updated_at=1777913093.0954173
- [2026-05-05 00:44:53] operator / voice_transcript_partial / voice: are you do but the
  meta: kind=partial | timestamp=1777913093.6044972 | source=vosk | frequency_hz=312.0 | rms=272 | updated_at=1777913093.0954173
- [2026-05-05 00:44:54] operator / voice_transcript_final / voice: are you do but the
  meta: kind=final | timestamp=1777913094.6040752 | source=final | frequency_hz=336.9 | rms=274 | updated_at=1777913094.5959582
- [2026-05-05 00:44:56] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1777913096.351115 | source=vosk | frequency_hz=318.4 | rms=275 | updated_at=1777913095.8449152
- [2026-05-05 00:44:56] operator / voice_transcript_partial / voice: what do
  meta: kind=partial | timestamp=1777913096.6040914 | source=vosk | frequency_hz=318.4 | rms=275 | updated_at=1777913095.8449152
- [2026-05-05 00:44:57] operator / voice_transcript_final / voice: what
  meta: kind=final | timestamp=1777913097.1021025 | source=final | frequency_hz=321.6 | rms=276 | updated_at=1777913097.0950425
- [2026-05-05 00:44:59] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777913099.8497047 | source=vosk | frequency_hz=291.1 | rms=318 | updated_at=1777913098.845139
- [2026-05-05 00:45:00] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777913100.8514926 | source=final | frequency_hz=271.7 | rms=266 | updated_at=1777913100.845141
- [2026-05-05 00:45:03] operator / voice_transcript_partial / voice: current
  meta: kind=partial | timestamp=1777913103.114577 | source=vosk | frequency_hz=327.0 | rms=289 | updated_at=1777913103.1065757
- [2026-05-05 00:45:03] operator / voice_transcript_final / voice: again
  meta: kind=final | timestamp=1777913103.8425558 | source=final | frequency_hz=328.8 | rms=339 | updated_at=1777913103.3450754
- [2026-05-05 00:45:09] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777913109.1007524 | source=vosk | frequency_hz=336.2 | rms=311 | updated_at=1777913109.0952344
- [2026-05-05 00:45:10] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777913110.1283817 | source=final | frequency_hz=336.2 | rms=311 | updated_at=1777913109.0952344
- [2026-05-05 00:45:16] operator / voice_transcript_partial / voice: delay
  meta: kind=partial | timestamp=1777913116.3607283 | source=vosk | frequency_hz=280.0 | rms=292 | updated_at=1777913115.3465676
- [2026-05-05 00:45:16] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777913116.6024344 | source=vosk | frequency_hz=280.0 | rms=292 | updated_at=1777913115.3465676
- [2026-05-05 00:45:16] operator / voice_transcript_partial / voice: the last
  meta: kind=partial | timestamp=1777913116.8514676 | source=vosk | frequency_hz=280.0 | rms=292 | updated_at=1777913115.3465676
- [2026-05-05 00:45:17] operator / voice_transcript_final / voice: delay
  meta: kind=final | timestamp=1777913117.1178746 | source=final | frequency_hz=280.0 | rms=292 | updated_at=1777913115.3465676
- [2026-05-05 00:45:17] operator / voice_transcript_partial / voice: enable
  meta: kind=partial | timestamp=1777913117.6016176 | source=vosk | frequency_hz=280.0 | rms=292 | updated_at=1777913115.3465676
- [2026-05-05 00:45:18] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777913118.7889135 | source=vosk | frequency_hz=280.0 | rms=292 | updated_at=1777913115.3465676
- [2026-05-05 00:45:18] operator / voice_transcript_partial / voice: you
  meta: kind=partial | timestamp=1777913118.7969706 | source=vosk | frequency_hz=272.0 | rms=305 | updated_at=1777913118.7889135
- [2026-05-05 00:45:19] operator / voice_transcript_final / voice: you
  meta: kind=final | timestamp=1777913119.966431 | source=final | frequency_hz=272.0 | rms=305 | updated_at=1777913118.7889135
- [2026-05-05 00:45:21] operator / voice_transcript_partial / voice: do it
  meta: kind=partial | timestamp=1777913121.722615 | source=vosk | frequency_hz=279.4 | rms=277 | updated_at=1777913121.2175925
- [2026-05-05 00:45:21] operator / voice_transcript_partial / voice: do it the
  meta: kind=partial | timestamp=1777913121.9727607 | source=vosk | frequency_hz=279.4 | rms=277 | updated_at=1777913121.2175925
- [2026-05-05 00:45:22] operator / voice_transcript_partial / voice: do it the boards and
  meta: kind=partial | timestamp=1777913122.237725 | source=vosk | frequency_hz=279.4 | rms=277 | updated_at=1777913121.2175925
- [2026-05-05 00:45:22] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777913122.4734738 | source=vosk | frequency_hz=279.4 | rms=277 | updated_at=1777913121.2175925
- [2026-05-05 00:45:24] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777913124.51541 | source=final | frequency_hz=320.1 | rms=275 | updated_at=1777913124.4806573
- [2026-05-05 00:45:33] operator / voice_transcript_partial / voice: the again
  meta: kind=partial | timestamp=1777913133.9782088 | source=vosk | frequency_hz=251.5 | rms=276 | updated_at=1777913133.4671576
- [2026-05-05 00:45:34] operator / voice_transcript_partial / voice: diagnostics
  meta: kind=partial | timestamp=1777913134.2221916 | source=vosk | frequency_hz=251.5 | rms=276 | updated_at=1777913133.4671576
- [2026-05-05 00:45:34] operator / voice_transcript_final / voice: the again
  meta: kind=final | timestamp=1777913134.4945443 | source=final | frequency_hz=251.5 | rms=276 | updated_at=1777913133.4671576
- [2026-05-05 00:45:36] operator / voice_transcript_partial / voice: mind
  meta: kind=partial | timestamp=1777913136.7251801 | source=vosk | frequency_hz=362.6 | rms=318 | updated_at=1777913136.2181964
- [2026-05-05 00:45:36] operator / voice_transcript_partial / voice: mind analyze
  meta: kind=partial | timestamp=1777913136.9758961 | source=vosk | frequency_hz=362.6 | rms=318 | updated_at=1777913136.2181964
- [2026-05-05 00:45:37] operator / voice_transcript_partial / voice: mind the never mind
  meta: kind=partial | timestamp=1777913137.2229168 | source=vosk | frequency_hz=362.6 | rms=318 | updated_at=1777913136.2181964
- [2026-05-05 00:45:37] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777913137.4806943 | source=vosk | frequency_hz=362.6 | rms=318 | updated_at=1777913136.2181964
- [2026-05-05 00:45:39] operator / voice_transcript_partial / voice: mind anything resume guarding less
  meta: kind=partial | timestamp=1777913139.4923863 | source=vosk | frequency_hz=371.8 | rms=320 | updated_at=1777913138.7176745
- [2026-05-05 00:45:39] operator / voice_transcript_partial / voice: mind anything resume guarding enable to anything
  meta: kind=partial | timestamp=1777913139.7289445 | source=vosk | frequency_hz=371.8 | rms=320 | updated_at=1777913138.7176745
- [2026-05-05 00:45:39] operator / voice_transcript_partial / voice: mind anything resume guarding and enable
  meta: kind=partial | timestamp=1777913139.9805617 | source=vosk | frequency_hz=371.8 | rms=320 | updated_at=1777913138.7176745
- [2026-05-05 00:45:40] operator / voice_transcript_partial / voice: mind anything resume guarding mode and eileen
  meta: kind=partial | timestamp=1777913140.2310276 | source=vosk | frequency_hz=371.8 | rms=320 | updated_at=1777913138.7176745
- [2026-05-05 00:45:40] operator / voice_transcript_partial / voice: mind anything resume guarding and enable
  meta: kind=partial | timestamp=1777913140.474098 | source=vosk | frequency_hz=356.0 | rms=301 | updated_at=1777913140.468089
- [2026-05-05 00:45:40] operator / voice_transcript_final / voice: resume guarding mode
  meta: kind=final | timestamp=1777913140.7389967 | source=final | frequency_hz=336.4 | rms=281 | updated_at=1777913140.7202113
- [2026-05-05 00:45:41] operator / voice_command / voice: resume guarding mode
  meta: normalized=True
- [2026-05-05 00:45:42] assistant / spoken_confirmation / voice: Resuming guarding mode now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:45:46] operator / voice_transcript_partial / voice: the resume
  meta: kind=partial | timestamp=1777913146.4922593 | source=vosk | frequency_hz=335.7 | rms=823 | updated_at=1777913142.736311
- [2026-05-05 00:45:46] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1777913146.9935703 | source=vosk | frequency_hz=335.7 | rms=823 | updated_at=1777913142.736311
- [2026-05-05 00:45:47] operator / voice_transcript_partial / voice: what do
  meta: kind=partial | timestamp=1777913147.2421803 | source=vosk | frequency_hz=335.7 | rms=823 | updated_at=1777913142.736311
- [2026-05-05 00:45:47] operator / voice_transcript_partial / voice: in commands
  meta: kind=partial | timestamp=1777913147.4913754 | source=vosk | frequency_hz=335.7 | rms=823 | updated_at=1777913142.736311
- [2026-05-05 00:45:47] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777913147.7447777 | source=vosk | frequency_hz=335.7 | rms=823 | updated_at=1777913142.736311
- [2026-05-05 00:45:50] operator / voice_transcript_partial / voice: increase the no you
  meta: kind=partial | timestamp=1777913150.492325 | source=vosk | frequency_hz=342.9 | rms=274 | updated_at=1777913149.4860883
- [2026-05-05 00:45:50] operator / voice_transcript_partial / voice: increase the no you more
  meta: kind=partial | timestamp=1777913150.7451656 | source=vosk | frequency_hz=342.9 | rms=274 | updated_at=1777913149.4860883
- [2026-05-05 00:45:51] operator / voice_transcript_partial / voice: increase the no you more the
  meta: kind=partial | timestamp=1777913151.24128 | source=vosk | frequency_hz=342.9 | rms=274 | updated_at=1777913149.4860883
- [2026-05-05 00:45:51] operator / voice_transcript_partial / voice: increase the no you mode a abort current
  meta: kind=partial | timestamp=1777913151.4962935 | source=vosk | frequency_hz=342.9 | rms=274 | updated_at=1777913149.4860883
- [2026-05-05 00:45:51] operator / voice_transcript_partial / voice: increase the no you more the board go
  meta: kind=partial | timestamp=1777913151.7497816 | source=vosk | frequency_hz=342.9 | rms=274 | updated_at=1777913149.4860883
- [2026-05-05 00:45:52] operator / voice_transcript_final / voice: lion increase the no you more the board go
  meta: kind=final | timestamp=1777913152.515305 | source=final | frequency_hz=342.9 | rms=274 | updated_at=1777913149.4860883
- [2026-05-05 00:45:52] operator / voice_command / voice: lion increase the no you more the board go
  meta: normalized=True
- [2026-05-05 00:45:54] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:45:54] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777913154.492863 | source=vosk | frequency_hz=296.8 | rms=279 | updated_at=1777913153.486634
- [2026-05-05 00:45:54] operator / voice_transcript_partial / voice: lion do you
  meta: kind=partial | timestamp=1777913154.7438173 | source=vosk | frequency_hz=296.8 | rms=279 | updated_at=1777913153.486634
- [2026-05-05 00:45:54] operator / voice_transcript_partial / voice: lion do you mind
  meta: kind=partial | timestamp=1777913154.9922545 | source=vosk | frequency_hz=296.8 | rms=279 | updated_at=1777913153.486634
- [2026-05-05 00:45:55] operator / voice_transcript_partial / voice: lion do you mode
  meta: kind=partial | timestamp=1777913155.2436206 | source=vosk | frequency_hz=296.8 | rms=279 | updated_at=1777913153.486634
- [2026-05-05 00:45:55] operator / voice_transcript_partial / voice: lion resume identify
  meta: kind=partial | timestamp=1777913155.495065 | source=vosk | frequency_hz=296.8 | rms=279 | updated_at=1777913153.486634
- [2026-05-05 00:45:55] operator / voice_transcript_partial / voice: lion resume identify board be more
  meta: kind=partial | timestamp=1777913155.7452304 | source=vosk | frequency_hz=296.8 | rms=279 | updated_at=1777913153.486634
- [2026-05-05 00:45:55] operator / voice_transcript_partial / voice: lion resume identify the theme to
  meta: kind=partial | timestamp=1777913155.9937053 | source=vosk | frequency_hz=296.8 | rms=279 | updated_at=1777913153.486634
- [2026-05-05 00:45:56] operator / voice_transcript_partial / voice: lion resume identify the theme to the
  meta: kind=partial | timestamp=1777913156.242652 | source=vosk | frequency_hz=296.8 | rms=279 | updated_at=1777913153.486634
- [2026-05-05 00:45:56] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue
  meta: kind=partial | timestamp=1777913156.5013232 | source=vosk | frequency_hz=296.8 | rms=279 | updated_at=1777913153.486634
- [2026-05-05 00:45:57] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue response
  meta: kind=partial | timestamp=1777913157.2454357 | source=vosk | frequency_hz=368.0 | rms=289 | updated_at=1777913157.2364116
- [2026-05-05 00:45:57] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease
  meta: kind=partial | timestamp=1777913157.4977076 | source=vosk | frequency_hz=368.0 | rms=289 | updated_at=1777913157.2364116
- [2026-05-05 00:45:57] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease what do
  meta: kind=partial | timestamp=1777913157.7515228 | source=vosk | frequency_hz=368.0 | rms=289 | updated_at=1777913157.2364116
- [2026-05-05 00:45:57] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease response
  meta: kind=partial | timestamp=1777913157.993595 | source=vosk | frequency_hz=368.0 | rms=289 | updated_at=1777913157.2364116
- [2026-05-05 00:45:58] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease what do disable
  meta: kind=partial | timestamp=1777913158.2423022 | source=vosk | frequency_hz=368.0 | rms=289 | updated_at=1777913157.2364116
- [2026-05-05 00:45:58] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease what do disable status
  meta: kind=partial | timestamp=1777913158.4909592 | source=vosk | frequency_hz=368.0 | rms=289 | updated_at=1777913157.2364116
- [2026-05-05 00:45:58] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease what do disable the
  meta: kind=partial | timestamp=1777913158.746237 | source=vosk | frequency_hz=368.0 | rms=289 | updated_at=1777913157.2364116
- [2026-05-05 00:45:58] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease what do disable status report
  meta: kind=partial | timestamp=1777913158.9923 | source=vosk | frequency_hz=368.0 | rms=289 | updated_at=1777913157.2364116
- [2026-05-05 00:45:59] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease what do disable the current
  meta: kind=partial | timestamp=1777913159.2458725 | source=vosk | frequency_hz=368.0 | rms=289 | updated_at=1777913157.2364116
- [2026-05-05 00:45:59] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease what do disable the current change
  meta: kind=partial | timestamp=1777913159.7408676 | source=vosk | frequency_hz=368.0 | rms=289 | updated_at=1777913157.2364116
- [2026-05-05 00:45:59] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease what do disable the current change smart
  meta: kind=partial | timestamp=1777913159.9934285 | source=vosk | frequency_hz=368.0 | rms=289 | updated_at=1777913157.2364116
- [2026-05-05 00:46:00] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease what do disable the current change smart sentry
  meta: kind=partial | timestamp=1777913160.241947 | source=vosk | frequency_hz=368.0 | rms=289 | updated_at=1777913157.2364116
- [2026-05-05 00:46:00] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease what do disable the current change smart sentry say last
  meta: kind=partial | timestamp=1777913160.9917314 | source=vosk | frequency_hz=368.0 | rms=289 | updated_at=1777913157.2364116
- [2026-05-05 00:46:01] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease what do disable the current change smart sentry say last that
  meta: kind=partial | timestamp=1777913161.501652 | source=vosk | frequency_hz=368.0 | rms=289 | updated_at=1777913157.2364116
- [2026-05-05 00:46:01] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease what do disable the current change smart sentry say last that again
  meta: kind=partial | timestamp=1777913161.7438335 | source=vosk | frequency_hz=404.0 | rms=332 | updated_at=1777913161.7368214
- [2026-05-05 00:46:02] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease what do disable the current change smart sentry say last that again less
  meta: kind=partial | timestamp=1777913162.2467682 | source=vosk | frequency_hz=404.0 | rms=332 | updated_at=1777913161.7368214
- [2026-05-05 00:46:02] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease what do disable the current change smart sentry say last that again rest the
  meta: kind=partial | timestamp=1777913162.4941962 | source=vosk | frequency_hz=404.0 | rms=332 | updated_at=1777913161.7368214
- [2026-05-05 00:46:02] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease what do disable the current change smart sentry say last that again less theme it
  meta: kind=partial | timestamp=1777913162.7435243 | source=vosk | frequency_hz=404.0 | rms=332 | updated_at=1777913161.7368214
- [2026-05-05 00:46:02] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease what do disable the current change smart sentry say last that again less theme increase
  meta: kind=partial | timestamp=1777913162.9925194 | source=vosk | frequency_hz=404.0 | rms=332 | updated_at=1777913161.7368214
- [2026-05-05 00:46:03] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease what do disable the current change smart sentry say last that again less theme increase it what
  meta: kind=partial | timestamp=1777913163.5137844 | source=vosk | frequency_hz=404.0 | rms=332 | updated_at=1777913161.7368214
- [2026-05-05 00:46:03] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease what do disable the current change smart sentry say last that again less theme increase it what and enable
  meta: kind=partial | timestamp=1777913163.7439113 | source=vosk | frequency_hz=404.0 | rms=332 | updated_at=1777913161.7368214
- [2026-05-05 00:46:03] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease what do disable the current change smart sentry say last that again less theme increase it what in
  meta: kind=partial | timestamp=1777913163.992503 | source=vosk | frequency_hz=404.0 | rms=332 | updated_at=1777913161.7368214
- [2026-05-05 00:46:04] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease what do disable the current change smart sentry say last that again less theme increase it what in serial
  meta: kind=partial | timestamp=1777913164.2435267 | source=vosk | frequency_hz=404.0 | rms=332 | updated_at=1777913161.7368214
- [2026-05-05 00:46:04] operator / voice_transcript_partial / voice: lion resume identify the theme to the queue decrease what do disable the current change smart sentry say last that again less theme increase it what in smart sentry
  meta: kind=partial | timestamp=1777913164.4923756 | source=vosk | frequency_hz=404.0 | rms=332 | updated_at=1777913161.7368214
- [2026-05-05 00:46:05] operator / voice_transcript_final / voice: do it again
  meta: kind=final | timestamp=1777913165.245526 | source=final | frequency_hz=316.2 | rms=273 | updated_at=1777913165.2365139
- [2026-05-05 00:46:05] operator / voice_command / voice: do it again
  meta: normalized=True
- [2026-05-05 00:46:06] operator / voice_command / voice: check status
  meta: normalized=True
- [2026-05-05 00:46:06] assistant / spoken_reply / voice: Smart Sentry is paused right now. Latest AI note. Analysis complete. Detection=Yolo Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1. 50s; face=on; pir=on. Enable at least one PIR sensor or disable PIR guard to match actual intent. End of analysys report.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-05 00:46:06] operator / voice_transcript_partial / voice: again you
  meta: kind=partial | timestamp=1777913166.9939823 | source=vosk | frequency_hz=298.4 | rms=279 | updated_at=1777913166.23568
- [2026-05-05 00:46:07] operator / voice_transcript_partial / voice: anything
  meta: kind=partial | timestamp=1777913167.4324932 | source=vosk | frequency_hz=298.4 | rms=279 | updated_at=1777913166.23568
- [2026-05-05 00:46:07] operator / voice_transcript_partial / voice: anything else
  meta: kind=partial | timestamp=1777913167.4913034 | source=vosk | frequency_hz=298.4 | rms=279 | updated_at=1777913166.23568
- [2026-05-05 00:46:08] operator / voice_transcript_final / voice: anything else
  meta: kind=final | timestamp=1777913168.5807178 | source=final | frequency_hz=298.4 | rms=279 | updated_at=1777913166.23568
- [2026-05-05 00:46:08] operator / voice_command / voice: anything else
  meta: normalized=True
- [2026-05-05 00:46:08] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777913168.7426455 | source=vosk | frequency_hz=298.4 | rms=279 | updated_at=1777913166.23568
- [2026-05-05 00:46:09] operator / voice_transcript_partial / voice: delay go
  meta: kind=partial | timestamp=1777913169.2438235 | source=vosk | frequency_hz=298.4 | rms=279 | updated_at=1777913166.23568
- [2026-05-05 00:46:09] operator / voice_transcript_final / voice: delay go
  meta: kind=final | timestamp=1777913169.8807642 | source=final | frequency_hz=298.4 | rms=279 | updated_at=1777913166.23568
- [2026-05-05 00:46:10] operator / voice_command / voice: delay go
  meta: normalized=True
- [2026-05-05 00:46:11] operator / voice_transcript_partial / voice: theme to
  meta: kind=partial | timestamp=1777913171.2424693 | source=vosk | frequency_hz=298.4 | rms=279 | updated_at=1777913166.23568
- [2026-05-05 00:46:11] operator / voice_transcript_partial / voice: theme it do it
  meta: kind=partial | timestamp=1777913171.7425525 | source=vosk | frequency_hz=298.4 | rms=279 | updated_at=1777913166.23568
- [2026-05-05 00:46:11] operator / voice_transcript_partial / voice: theme it repeat
  meta: kind=partial | timestamp=1777913171.9954777 | source=vosk | frequency_hz=360.0 | rms=282 | updated_at=1777913171.989968
- [2026-05-05 00:46:12] operator / voice_transcript_final / voice: theme it do it
  meta: kind=final | timestamp=1777913172.4938533 | source=final | frequency_hz=352.4 | rms=271 | updated_at=1777913172.4868371
- [2026-05-05 00:46:12] operator / voice_command / voice: theme it do it
  meta: normalized=True
- [2026-05-05 00:46:14] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:46:14] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:46:14] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:46:15] operator / voice_transcript_partial / voice: say decrease
  meta: kind=partial | timestamp=1777913175.7425647 | source=vosk | frequency_hz=312.5 | rms=285 | updated_at=1777913174.4869823
- [2026-05-05 00:46:15] operator / voice_transcript_partial / voice: say do it
  meta: kind=partial | timestamp=1777913175.9936063 | source=vosk | frequency_hz=312.5 | rms=285 | updated_at=1777913174.4869823
- [2026-05-05 00:46:16] operator / voice_transcript_partial / voice: say theme to
  meta: kind=partial | timestamp=1777913176.2428682 | source=vosk | frequency_hz=312.5 | rms=285 | updated_at=1777913174.4869823
- [2026-05-05 00:46:16] operator / voice_transcript_partial / voice: say theme to com
  meta: kind=partial | timestamp=1777913176.993009 | source=vosk | frequency_hz=268.0 | rms=261 | updated_at=1777913176.4864173
- [2026-05-05 00:46:17] operator / voice_transcript_partial / voice: say theme to com mind
  meta: kind=partial | timestamp=1777913177.2428663 | source=vosk | frequency_hz=268.0 | rms=261 | updated_at=1777913176.4864173
- [2026-05-05 00:46:17] operator / voice_transcript_partial / voice: say theme to confirm on commands
  meta: kind=partial | timestamp=1777913177.50163 | source=vosk | frequency_hz=289.0 | rms=389 | updated_at=1777913177.4935286
- [2026-05-05 00:46:17] operator / voice_transcript_partial / voice: say theme to confirm all queued tasks
  meta: kind=partial | timestamp=1777913177.743587 | source=vosk | frequency_hz=289.0 | rms=389 | updated_at=1777913177.4935286
- [2026-05-05 00:46:17] operator / voice_transcript_final / voice: say theme to com unk
  meta: kind=final | timestamp=1777913177.996115 | source=final | frequency_hz=281.6 | rms=271 | updated_at=1777913177.9871023
- [2026-05-05 00:46:18] operator / voice_command / voice: say theme to com unk
  meta: normalized=True
- [2026-05-05 00:46:19] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:46:20] operator / voice_transcript_partial / voice: sentry
  meta: kind=partial | timestamp=1777913180.2437193 | source=vosk | frequency_hz=317.0 | rms=270 | updated_at=1777913179.2381566
- [2026-05-05 00:46:20] operator / voice_transcript_partial / voice: say e
  meta: kind=partial | timestamp=1777913180.5091932 | source=vosk | frequency_hz=317.0 | rms=270 | updated_at=1777913179.2381566
- [2026-05-05 00:46:20] operator / voice_transcript_partial / voice: say it
  meta: kind=partial | timestamp=1777913180.7436004 | source=vosk | frequency_hz=317.0 | rms=270 | updated_at=1777913179.2381566
- [2026-05-05 00:46:20] operator / voice_transcript_partial / voice: sentry theme
  meta: kind=partial | timestamp=1777913180.9990437 | source=vosk | frequency_hz=317.0 | rms=270 | updated_at=1777913179.2381566
- [2026-05-05 00:46:21] operator / voice_transcript_partial / voice: sentry theme a
  meta: kind=partial | timestamp=1777913181.242715 | source=vosk | frequency_hz=317.0 | rms=270 | updated_at=1777913179.2381566
- [2026-05-05 00:46:21] operator / voice_transcript_partial / voice: say it do
  meta: kind=partial | timestamp=1777913181.4979625 | source=vosk | frequency_hz=372.0 | rms=265 | updated_at=1777913181.4869432
- [2026-05-05 00:46:21] operator / voice_transcript_final / voice: say theme a do
  meta: kind=final | timestamp=1777913181.9955897 | source=final | frequency_hz=328.2 | rms=290 | updated_at=1777913181.9865723
- [2026-05-05 00:46:23] operator / voice_transcript_partial / voice: do it
  meta: kind=partial | timestamp=1777913183.7419853 | source=vosk | frequency_hz=328.2 | rms=290 | updated_at=1777913181.9865723
- [2026-05-05 00:46:23] operator / voice_transcript_partial / voice: do it delay
  meta: kind=partial | timestamp=1777913183.9937892 | source=vosk | frequency_hz=328.2 | rms=290 | updated_at=1777913181.9865723
- [2026-05-05 00:46:25] operator / voice_transcript_final / voice: do it delay
  meta: kind=final | timestamp=1777913185.1155095 | source=final | frequency_hz=328.2 | rms=290 | updated_at=1777913181.9865723
- [2026-05-05 00:46:25] operator / voice_transcript_partial / voice: yourself
  meta: kind=partial | timestamp=1777913185.9922583 | source=vosk | frequency_hz=400.0 | rms=249 | updated_at=1777913185.2381046
- [2026-05-05 00:46:26] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777913186.257327 | source=vosk | frequency_hz=400.0 | rms=249 | updated_at=1777913185.2381046
- [2026-05-05 00:46:26] operator / voice_transcript_partial / voice: resume
  meta: kind=partial | timestamp=1777913186.4928901 | source=vosk | frequency_hz=400.0 | rms=249 | updated_at=1777913185.2381046
- [2026-05-05 00:46:26] operator / voice_transcript_partial / voice: priority sentry
  meta: kind=partial | timestamp=1777913186.7459493 | source=vosk | frequency_hz=400.0 | rms=249 | updated_at=1777913185.2381046
- [2026-05-05 00:46:26] operator / voice_transcript_partial / voice: resume anything
  meta: kind=partial | timestamp=1777913186.992433 | source=vosk | frequency_hz=400.0 | rms=249 | updated_at=1777913185.2381046
- [2026-05-05 00:46:27] operator / voice_transcript_partial / voice: resume alion increase
  meta: kind=partial | timestamp=1777913187.2442212 | source=vosk | frequency_hz=400.0 | rms=249 | updated_at=1777913185.2381046
- [2026-05-05 00:46:27] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:46:27] operator / voice_transcript_final / voice: do you resume increase
  meta: kind=final | timestamp=1777913187.9979117 | source=final | frequency_hz=357.4 | rms=242 | updated_at=1777913187.9868972
- [2026-05-05 00:46:28] operator / voice_command / voice: do you resume increase
  meta: normalized=True
- [2026-05-05 00:46:31] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777913191.2510622 | source=vosk | frequency_hz=349.2 | rms=246 | updated_at=1777913189.2379677
- [2026-05-05 00:46:31] operator / voice_transcript_partial / voice: smart sentry
  meta: kind=partial | timestamp=1777913191.4938982 | source=vosk | frequency_hz=349.2 | rms=246 | updated_at=1777913189.2379677
- [2026-05-05 00:46:32] operator / voice_transcript_partial / voice: smart sentry response
  meta: kind=partial | timestamp=1777913192.2416573 | source=vosk | frequency_hz=349.2 | rms=246 | updated_at=1777913189.2379677
- [2026-05-05 00:46:32] operator / voice_transcript_partial / voice: smart sentry response delay
  meta: kind=partial | timestamp=1777913192.4916992 | source=vosk | frequency_hz=349.2 | rms=246 | updated_at=1777913189.2379677
- [2026-05-05 00:46:32] operator / voice_transcript_partial / voice: smart sentry response threshold
  meta: kind=partial | timestamp=1777913192.7435887 | source=vosk | frequency_hz=349.2 | rms=246 | updated_at=1777913189.2379677
- [2026-05-05 00:46:32] operator / voice_transcript_partial / voice: smart sentry response brightness
  meta: kind=partial | timestamp=1777913192.9937348 | source=vosk | frequency_hz=362.0 | rms=242 | updated_at=1777913192.9867234
- [2026-05-05 00:46:33] operator / voice_transcript_partial / voice: smart sentry response delay
  meta: kind=partial | timestamp=1777913193.2412584 | source=vosk | frequency_hz=358.5 | rms=239 | updated_at=1777913193.2362468
- [2026-05-05 00:46:33] operator / voice_transcript_final / voice: smart sentry response delay
  meta: kind=final | timestamp=1777913193.7804449 | source=final | frequency_hz=345.0 | rms=235 | updated_at=1777913193.495869
- [2026-05-05 00:46:34] operator / voice_command / voice: smart sentry response delay
  meta: normalized=True
- [2026-05-05 00:46:34] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777913194.2444572 | source=vosk | frequency_hz=351.6 | rms=230 | updated_at=1777913193.7814467
- [2026-05-05 00:46:34] operator / voice_transcript_partial / voice: eileen to
  meta: kind=partial | timestamp=1777913194.4937267 | source=vosk | frequency_hz=351.6 | rms=230 | updated_at=1777913193.7814467
- [2026-05-05 00:46:35] operator / voice_transcript_partial / voice: aileen status
  meta: kind=partial | timestamp=1777913195.0796442 | source=vosk | frequency_hz=351.6 | rms=230 | updated_at=1777913193.7814467
- [2026-05-05 00:46:35] operator / voice_transcript_partial / voice: eileen say no
  meta: kind=partial | timestamp=1777913195.2795246 | source=vosk | frequency_hz=351.6 | rms=230 | updated_at=1777913193.7814467
- [2026-05-05 00:46:36] operator / voice_transcript_final / voice: say no
  meta: kind=final | timestamp=1777913196.2160146 | source=final | frequency_hz=351.6 | rms=230 | updated_at=1777913193.7814467
- [2026-05-05 00:46:36] operator / voice_command / voice: say no
  meta: normalized=True
- [2026-05-05 00:46:36] operator / voice_transcript_partial / voice: enable
  meta: kind=partial | timestamp=1777913196.253126 | source=vosk | frequency_hz=351.6 | rms=230 | updated_at=1777913193.7814467
- [2026-05-05 00:46:37] operator / voice_transcript_partial / voice: enable e lion
  meta: kind=partial | timestamp=1777913197.0130248 | source=vosk | frequency_hz=351.6 | rms=230 | updated_at=1777913193.7814467
- [2026-05-05 00:46:37] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:46:37] operator / voice_transcript_partial / voice: enable e less
  meta: kind=partial | timestamp=1777913197.3975606 | source=vosk | frequency_hz=351.6 | rms=230 | updated_at=1777913193.7814467
- [2026-05-05 00:46:37] operator / voice_transcript_partial / voice: enable the smart
  meta: kind=partial | timestamp=1777913197.4932013 | source=vosk | frequency_hz=351.6 | rms=230 | updated_at=1777913193.7814467
- [2026-05-05 00:46:37] operator / voice_transcript_partial / voice: enable the smart sentry
  meta: kind=partial | timestamp=1777913197.7500467 | source=vosk | frequency_hz=351.6 | rms=230 | updated_at=1777913193.7814467
- [2026-05-05 00:46:39] operator / voice_transcript_final / voice: enable smart sentry
  meta: kind=final | timestamp=1777913199.0406811 | source=final | frequency_hz=346.6 | rms=243 | updated_at=1777913198.737888
- [2026-05-05 00:46:39] operator / voice_command / voice: enable smart sentry
  meta: normalized=True
- [2026-05-05 00:46:39] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777913199.243592 | source=vosk | frequency_hz=346.6 | rms=243 | updated_at=1777913198.737888
- [2026-05-05 00:46:39] operator / voice_transcript_partial / voice: e the current
  meta: kind=partial | timestamp=1777913199.5199676 | source=vosk | frequency_hz=346.6 | rms=243 | updated_at=1777913198.737888
- [2026-05-05 00:46:39] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777913199.752113 | source=vosk | frequency_hz=346.6 | rms=243 | updated_at=1777913198.737888
- [2026-05-05 00:46:40] operator / voice_transcript_partial / voice: go ahead
  meta: kind=partial | timestamp=1777913200.2427528 | source=vosk | frequency_hz=346.6 | rms=243 | updated_at=1777913198.737888
- [2026-05-05 00:46:40] operator / voice_transcript_partial / voice: go ahead decrease
  meta: kind=partial | timestamp=1777913200.9931927 | source=vosk | frequency_hz=346.6 | rms=243 | updated_at=1777913198.737888
- [2026-05-05 00:46:41] operator / voice_transcript_final / voice: e the current go ahead do confirm
  meta: kind=final | timestamp=1777913201.5116942 | source=final | frequency_hz=348.0 | rms=228 | updated_at=1777913201.2377846
- [2026-05-05 00:46:42] operator / voice_command / voice: e the current go ahead do confirm
  meta: normalized=True
- [2026-05-05 00:46:42] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777913202.0034046 | source=vosk | frequency_hz=348.0 | rms=228 | updated_at=1777913201.2377846
- [2026-05-05 00:46:42] operator / voice_transcript_partial / voice: check
  meta: kind=partial | timestamp=1777913202.4012413 | source=vosk | frequency_hz=348.0 | rms=228 | updated_at=1777913201.2377846
- [2026-05-05 00:46:43] assistant / spoken_confirmation / voice: Enabling Smart Sentry now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:46:43] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777913203.004113 | source=vosk | frequency_hz=328.0 | rms=242 | updated_at=1777913202.989522
- [2026-05-05 00:46:45] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:46:45] operator / voice_transcript_partial / voice: [unk] but
  meta: kind=partial | timestamp=1777913205.0650468 | source=vosk | frequency_hz=328.0 | rms=242 | updated_at=1777913202.989522
- [2026-05-05 00:46:45] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777913205.0735962 | source=vosk | frequency_hz=328.0 | rms=242 | updated_at=1777913202.989522
- [2026-05-05 00:46:45] operator / voice_transcript_partial / voice: [unk] speed
  meta: kind=partial | timestamp=1777913205.5093248 | source=vosk | frequency_hz=328.0 | rms=242 | updated_at=1777913202.989522
- [2026-05-05 00:46:45] operator / voice_transcript_partial / voice: [unk] speed speed
  meta: kind=partial | timestamp=1777913205.7423801 | source=vosk | frequency_hz=328.0 | rms=242 | updated_at=1777913202.989522
- [2026-05-05 00:46:46] operator / voice_transcript_final / voice: unk abort speed
  meta: kind=final | timestamp=1777913206.0370355 | source=final | frequency_hz=328.0 | rms=242 | updated_at=1777913202.989522
- [2026-05-05 00:46:47] operator / voice_command / voice: unk abort speed
  meta: normalized=True
- [2026-05-05 00:46:46] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777913206.5092998 | source=vosk | frequency_hz=328.0 | rms=242 | updated_at=1777913202.989522
- [2026-05-05 00:46:46] operator / voice_transcript_partial / voice: serial
  meta: kind=partial | timestamp=1777913206.743467 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:46] operator / voice_transcript_partial / voice: and e lion
  meta: kind=partial | timestamp=1777913206.9947913 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:48] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:46:47] operator / voice_transcript_partial / voice: and e response
  meta: kind=partial | timestamp=1777913207.758225 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:48] operator / voice_transcript_partial / voice: a disable smart
  meta: kind=partial | timestamp=1777913208.012554 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:48] operator / voice_transcript_partial / voice: a disable smart no it
  meta: kind=partial | timestamp=1777913208.4922674 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:49] operator / voice_transcript_partial / voice: a disable smart no it else threshold
  meta: kind=partial | timestamp=1777913209.281808 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:49] operator / voice_transcript_partial / voice: a disable smart no it resume last
  meta: kind=partial | timestamp=1777913209.5119705 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:49] operator / voice_transcript_partial / voice: a disable smart no it go rest
  meta: kind=partial | timestamp=1777913209.8134918 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:50] operator / voice_transcript_partial / voice: a disable smart no it last decrease abort
  meta: kind=partial | timestamp=1777913210.0145211 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:50] operator / voice_transcript_partial / voice: a disable smart no it last decrease response
  meta: kind=partial | timestamp=1777913210.2439218 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:51] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:46:50] operator / voice_transcript_partial / voice: a disable smart no it last decrease sensitivity
  meta: kind=partial | timestamp=1777913210.4924645 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:51] operator / voice_transcript_final / voice: decrease sensitivity
  meta: kind=final | timestamp=1777913211.499344 | source=final | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:51] operator / voice_command / voice: decrease sensitivity
  meta: normalized=True
- [2026-05-05 00:46:51] operator / voice_transcript_partial / voice: elian
  meta: kind=partial | timestamp=1777913211.9936886 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:52] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:46:53] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777913213.0468867 | source=final | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:53] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:46:53] operator / voice_transcript_partial / voice: be
  meta: kind=partial | timestamp=1777913213.5023267 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:53] operator / voice_transcript_partial / voice: be sentry
  meta: kind=partial | timestamp=1777913213.749669 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:53] operator / voice_transcript_partial / voice: be status
  meta: kind=partial | timestamp=1777913213.9950762 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:54] operator / voice_transcript_partial / voice: be status report
  meta: kind=partial | timestamp=1777913214.4928505 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:54] operator / voice_transcript_partial / voice: be status response
  meta: kind=partial | timestamp=1777913214.7441127 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:55] operator / voice_transcript_partial / voice: be status resume last
  meta: kind=partial | timestamp=1777913215.0083444 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:55] operator / voice_transcript_partial / voice: be status resume no
  meta: kind=partial | timestamp=1777913215.2508557 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:56] operator / voice_transcript_partial / voice: be status resume no are you
  meta: kind=partial | timestamp=1777913216.0046396 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:56] operator / voice_transcript_partial / voice: be status resume no are you run diagnostics
  meta: kind=partial | timestamp=1777913216.245986 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:56] operator / voice_transcript_partial / voice: be status resume no are you run no
  meta: kind=partial | timestamp=1777913216.7173715 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:56] operator / voice_transcript_partial / voice: be status resume no are you current a
  meta: kind=partial | timestamp=1777913216.7504284 | source=vosk | frequency_hz=408.0 | rms=239 | updated_at=1777913206.7379582
- [2026-05-05 00:46:57] operator / voice_transcript_partial / voice: be status resume no are you current a elian
  meta: kind=partial | timestamp=1777913217.0156887 | source=vosk | frequency_hz=292.0 | rms=234 | updated_at=1777913216.9890223
- [2026-05-05 00:46:57] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:46:57] operator / voice_transcript_partial / voice: be status resume no are you current a elian alien
  meta: kind=partial | timestamp=1777913217.9396944 | source=vosk | frequency_hz=299.0 | rms=231 | updated_at=1777913217.2382197
- [2026-05-05 00:46:58] operator / voice_transcript_partial / voice: be status resume no are you current a elian enable
  meta: kind=partial | timestamp=1777913218.0129075 | source=vosk | frequency_hz=299.0 | rms=231 | updated_at=1777913217.2382197
- [2026-05-05 00:46:58] operator / voice_transcript_partial / voice: be status resume no are you current a elian enable smart
  meta: kind=partial | timestamp=1777913218.2455099 | source=vosk | frequency_hz=299.0 | rms=231 | updated_at=1777913217.2382197
- [2026-05-05 00:46:59] operator / voice_transcript_partial / voice: be status resume no are you current a elian enable smart sentry
  meta: kind=partial | timestamp=1777913219.113192 | source=vosk | frequency_hz=299.0 | rms=231 | updated_at=1777913217.2382197
- [2026-05-05 00:46:59] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:46:59] operator / voice_transcript_partial / voice: be status resume no are you current a elian enable smart sentry boards
  meta: kind=partial | timestamp=1777913219.7471695 | source=vosk | frequency_hz=299.0 | rms=231 | updated_at=1777913217.2382197
- [2026-05-05 00:46:59] operator / voice_transcript_partial / voice: be status resume no are you current a elian enable smart sentry port disable
  meta: kind=partial | timestamp=1777913219.9942873 | source=vosk | frequency_hz=299.0 | rms=231 | updated_at=1777913217.2382197
- [2026-05-05 00:47:00] operator / voice_transcript_partial / voice: be status resume no are you current a elian enable smart sentry port disable go home
  meta: kind=partial | timestamp=1777913220.545295 | source=vosk | frequency_hz=299.0 | rms=231 | updated_at=1777913217.2382197
- [2026-05-05 00:47:01] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:47:01] operator / voice_transcript_final / voice: enable smart sentry
  meta: kind=final | timestamp=1777913221.2473874 | source=final | frequency_hz=299.0 | rms=231 | updated_at=1777913217.2382197
- [2026-05-05 00:47:02] operator / voice_command / voice: enable smart sentry
  meta: normalized=True
- [2026-05-05 00:47:01] operator / voice_transcript_partial / voice: repeat that
  meta: kind=partial | timestamp=1777913221.9989398 | source=vosk | frequency_hz=299.0 | rms=231 | updated_at=1777913217.2382197
- [2026-05-05 00:47:02] operator / voice_transcript_final / voice: repeat that
  meta: kind=final | timestamp=1777913222.8003652 | source=final | frequency_hz=299.0 | rms=231 | updated_at=1777913217.2382197
- [2026-05-05 00:47:04] operator / voice_command / voice: repeat that
  meta: normalized=True
- [2026-05-05 00:47:03] operator / voice_transcript_partial / voice: app to
  meta: kind=partial | timestamp=1777913223.512979 | source=vosk | frequency_hz=299.0 | rms=231 | updated_at=1777913217.2382197
- [2026-05-05 00:47:05] operator / voice_command / voice: enable smart sentry
  meta: normalized=True
- [2026-05-05 00:47:04] operator / voice_transcript_partial / voice: app to sensitivity
  meta: kind=partial | timestamp=1777913224.4936814 | source=vosk | frequency_hz=299.0 | rms=231 | updated_at=1777913217.2382197
- [2026-05-05 00:47:05] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:47:05] operator / voice_transcript_final / voice: app to sensitivity
  meta: kind=final | timestamp=1777913225.4937906 | source=final | frequency_hz=299.0 | rms=231 | updated_at=1777913217.2382197
- [2026-05-05 00:47:06] operator / voice_command / voice: app to sensitivity
  meta: normalized=True
- [2026-05-05 00:47:07] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:47:07] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777913227.4955177 | source=vosk | frequency_hz=341.6 | rms=246 | updated_at=1777913225.996746
- [2026-05-05 00:47:08] operator / voice_transcript_partial / voice: same do
  meta: kind=partial | timestamp=1777913228.0027976 | source=vosk | frequency_hz=341.6 | rms=246 | updated_at=1777913225.996746
- [2026-05-05 00:47:08] operator / voice_transcript_partial / voice: same do it
  meta: kind=partial | timestamp=1777913228.2438323 | source=vosk | frequency_hz=341.6 | rms=246 | updated_at=1777913225.996746
- [2026-05-05 00:47:08] operator / voice_transcript_partial / voice: same do what do
  meta: kind=partial | timestamp=1777913228.5028074 | source=vosk | frequency_hz=348.0 | rms=284 | updated_at=1777913228.4957278
- [2026-05-05 00:47:09] operator / voice_transcript_final / voice: same do board
  meta: kind=final | timestamp=1777913229.057406 | source=final | frequency_hz=342.4 | rms=275 | updated_at=1777913228.9890757
- [2026-05-05 00:47:09] operator / voice_command / voice: same do board
  meta: normalized=True
- [2026-05-05 00:47:10] operator / voice_transcript_partial / voice: do it
  meta: kind=partial | timestamp=1777913230.2461805 | source=vosk | frequency_hz=342.4 | rms=275 | updated_at=1777913228.9890757
- [2026-05-05 00:47:10] operator / voice_transcript_partial / voice: do it say
  meta: kind=partial | timestamp=1777913230.744007 | source=vosk | frequency_hz=342.4 | rms=275 | updated_at=1777913228.9890757
- [2026-05-05 00:47:10] operator / voice_transcript_partial / voice: do it say it no
  meta: kind=partial | timestamp=1777913230.994389 | source=vosk | frequency_hz=342.4 | rms=275 | updated_at=1777913228.9890757
- [2026-05-05 00:47:11] operator / voice_transcript_final / voice: do it say it no
  meta: kind=final | timestamp=1777913231.745026 | source=final | frequency_hz=342.4 | rms=275 | updated_at=1777913228.9890757
- [2026-05-05 00:47:12] operator / voice_command / voice: do it say it no
  meta: normalized=True
- [2026-05-05 00:47:12] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777913232.9929862 | source=vosk | frequency_hz=342.4 | rms=275 | updated_at=1777913228.9890757
- [2026-05-05 00:47:13] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1777913233.2531645 | source=vosk | frequency_hz=342.4 | rms=275 | updated_at=1777913228.9890757
- [2026-05-05 00:47:13] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:47:13] operator / voice_transcript_partial / voice: e guarding
  meta: kind=partial | timestamp=1777913233.7480717 | source=vosk | frequency_hz=342.4 | rms=275 | updated_at=1777913228.9890757
- [2026-05-05 00:47:13] operator / voice_transcript_partial / voice: e tracking
  meta: kind=partial | timestamp=1777913233.997259 | source=vosk | frequency_hz=342.4 | rms=275 | updated_at=1777913228.9890757
- [2026-05-05 00:47:14] operator / voice_transcript_partial / voice: e tracking it
  meta: kind=partial | timestamp=1777913234.2437289 | source=vosk | frequency_hz=342.4 | rms=275 | updated_at=1777913228.9890757
- [2026-05-05 00:47:14] operator / voice_transcript_partial / voice: e tracking it the
  meta: kind=partial | timestamp=1777913234.7478466 | source=vosk | frequency_hz=342.4 | rms=275 | updated_at=1777913228.9890757
- [2026-05-05 00:47:15] operator / voice_transcript_partial / voice: e tracking it the what do
  meta: kind=partial | timestamp=1777913235.5030482 | source=vosk | frequency_hz=342.4 | rms=275 | updated_at=1777913228.9890757
- [2026-05-05 00:47:16] operator / voice_transcript_final / voice: e guarding it the board
  meta: kind=final | timestamp=1777913236.0631354 | source=final | frequency_hz=368.0 | rms=274 | updated_at=1777913236.0001187
- [2026-05-05 00:47:17] operator / voice_command / voice: e guarding it the board
  meta: normalized=True
- [2026-05-05 00:47:17] operator / voice_transcript_partial / voice: the smart
  meta: kind=partial | timestamp=1777913237.7452097 | source=vosk | frequency_hz=322.5 | rms=287 | updated_at=1777913236.2426198
- [2026-05-05 00:47:17] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777913237.9942255 | source=vosk | frequency_hz=322.5 | rms=287 | updated_at=1777913236.2426198
- [2026-05-05 00:47:18] operator / voice_transcript_partial / voice: say it no
  meta: kind=partial | timestamp=1777913238.2461698 | source=vosk | frequency_hz=296.0 | rms=277 | updated_at=1777913238.2381413
- [2026-05-05 00:47:18] operator / voice_transcript_final / voice: say it no
  meta: kind=final | timestamp=1777913238.9951499 | source=final | frequency_hz=336.4 | rms=276 | updated_at=1777913238.7421713
- [2026-05-05 00:47:19] operator / voice_command / voice: say it no
  meta: normalized=True
- [2026-05-05 00:47:20] operator / voice_transcript_partial / voice: that again
  meta: kind=partial | timestamp=1777913240.5208685 | source=vosk | frequency_hz=336.4 | rms=276 | updated_at=1777913238.7421713
- [2026-05-05 00:47:20] operator / voice_transcript_partial / voice: the repeat
  meta: kind=partial | timestamp=1777913240.762172 | source=vosk | frequency_hz=336.4 | rms=276 | updated_at=1777913238.7421713
- [2026-05-05 00:47:21] operator / voice_transcript_partial / voice: the repeat delay
  meta: kind=partial | timestamp=1777913241.0144436 | source=vosk | frequency_hz=336.4 | rms=276 | updated_at=1777913238.7421713
- [2026-05-05 00:47:21] operator / voice_transcript_partial / voice: the repeat that again
  meta: kind=partial | timestamp=1777913241.2439435 | source=vosk | frequency_hz=336.4 | rms=276 | updated_at=1777913238.7421713
- [2026-05-05 00:47:21] operator / voice_transcript_partial / voice: the repeat that again status
  meta: kind=partial | timestamp=1777913241.7904425 | source=vosk | frequency_hz=336.4 | rms=276 | updated_at=1777913238.7421713
- [2026-05-05 00:47:22] operator / voice_transcript_partial / voice: the repeat that again theme to anything
  meta: kind=partial | timestamp=1777913242.254143 | source=vosk | frequency_hz=336.4 | rms=276 | updated_at=1777913238.7421713
- [2026-05-05 00:47:22] operator / voice_transcript_partial / voice: the repeat that again status do it
  meta: kind=partial | timestamp=1777913242.49297 | source=vosk | frequency_hz=336.4 | rms=276 | updated_at=1777913238.7421713
- [2026-05-05 00:47:22] operator / voice_transcript_partial / voice: the repeat that again status commands
  meta: kind=partial | timestamp=1777913242.7438803 | source=vosk | frequency_hz=336.4 | rms=276 | updated_at=1777913238.7421713
- [2026-05-05 00:47:23] operator / voice_transcript_final / voice: the repeat that again status it
  meta: kind=final | timestamp=1777913243.3177106 | source=final | frequency_hz=336.4 | rms=276 | updated_at=1777913238.7421713
- [2026-05-05 00:47:23] operator / voice_command / voice: the repeat that again status it
  meta: normalized=True
- [2026-05-05 00:47:24] operator / voice_command / voice: enable smart sentry
  meta: normalized=True
- [2026-05-05 00:47:24] operator / voice_transcript_partial / voice: do you
  meta: kind=partial | timestamp=1777913244.4941337 | source=vosk | frequency_hz=336.4 | rms=276 | updated_at=1777913238.7421713
- [2026-05-05 00:47:24] operator / voice_transcript_partial / voice: serial
  meta: kind=partial | timestamp=1777913244.9943452 | source=vosk | frequency_hz=336.4 | rms=276 | updated_at=1777913238.7421713
- [2026-05-05 00:47:25] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777913245.2665596 | source=vosk | frequency_hz=336.4 | rms=276 | updated_at=1777913238.7421713
- [2026-05-05 00:47:25] operator / voice_transcript_partial / voice: say no
  meta: kind=partial | timestamp=1777913245.4929268 | source=vosk | frequency_hz=336.0 | rms=278 | updated_at=1777913245.4884198
- [2026-05-05 00:47:26] operator / voice_transcript_final / voice: do say no
  meta: kind=final | timestamp=1777913246.0009177 | source=final | frequency_hz=350.7 | rms=279 | updated_at=1777913245.9883888
- [2026-05-05 00:47:26] operator / voice_command / voice: do say no
  meta: normalized=True
- [2026-05-05 00:47:27] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:47:28] operator / voice_transcript_partial / voice: sensitivity
  meta: kind=partial | timestamp=1777913248.9945233 | source=vosk | frequency_hz=326.8 | rms=296 | updated_at=1777913246.988506
- [2026-05-05 00:47:29] operator / voice_transcript_partial / voice: say it
  meta: kind=partial | timestamp=1777913249.2680004 | source=vosk | frequency_hz=326.8 | rms=296 | updated_at=1777913246.988506
- [2026-05-05 00:47:29] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777913249.521066 | source=vosk | frequency_hz=326.8 | rms=296 | updated_at=1777913246.988506
- [2026-05-05 00:47:29] operator / voice_transcript_partial / voice: same but
  meta: kind=partial | timestamp=1777913249.99426 | source=vosk | frequency_hz=326.8 | rms=296 | updated_at=1777913246.988506
- [2026-05-05 00:47:30] operator / voice_transcript_partial / voice: same but faster
  meta: kind=partial | timestamp=1777913250.2442844 | source=vosk | frequency_hz=326.8 | rms=296 | updated_at=1777913246.988506
- [2026-05-05 00:47:30] operator / voice_transcript_partial / voice: same but on disable
  meta: kind=partial | timestamp=1777913250.4953759 | source=vosk | frequency_hz=326.8 | rms=296 | updated_at=1777913246.988506
- [2026-05-05 00:47:30] operator / voice_transcript_partial / voice: same but status
  meta: kind=partial | timestamp=1777913250.7445889 | source=vosk | frequency_hz=326.8 | rms=296 | updated_at=1777913246.988506
- [2026-05-05 00:47:30] operator / voice_transcript_partial / voice: same but do you do it again
  meta: kind=partial | timestamp=1777913250.9948785 | source=vosk | frequency_hz=326.8 | rms=296 | updated_at=1777913246.988506
- [2026-05-05 00:47:31] operator / voice_transcript_partial / voice: same but on disable the current
  meta: kind=partial | timestamp=1777913251.2446969 | source=vosk | frequency_hz=326.8 | rms=296 | updated_at=1777913246.988506
- [2026-05-05 00:47:31] operator / voice_transcript_partial / voice: same but strict on disconnect
  meta: kind=partial | timestamp=1777913251.4979358 | source=vosk | frequency_hz=326.8 | rms=296 | updated_at=1777913246.988506
- [2026-05-05 00:47:32] operator / voice_transcript_partial / voice: same but on disable the current change
  meta: kind=partial | timestamp=1777913252.0107858 | source=vosk | frequency_hz=326.8 | rms=296 | updated_at=1777913246.988506
- [2026-05-05 00:47:32] operator / voice_transcript_partial / voice: same but on disable the current change smart
  meta: kind=partial | timestamp=1777913252.2472641 | source=vosk | frequency_hz=326.8 | rms=296 | updated_at=1777913246.988506
- [2026-05-05 00:47:32] operator / voice_transcript_partial / voice: same but on disable the current change smart sentry
  meta: kind=partial | timestamp=1777913252.4935617 | source=vosk | frequency_hz=326.8 | rms=296 | updated_at=1777913246.988506
- [2026-05-05 00:47:33] operator / voice_transcript_partial / voice: same but on disable the current change smart sentry say
  meta: kind=partial | timestamp=1777913253.259238 | source=vosk | frequency_hz=326.8 | rms=296 | updated_at=1777913246.988506
- [2026-05-05 00:47:33] operator / voice_transcript_partial / voice: same but on disable the current change smart sentry silence threshold
  meta: kind=partial | timestamp=1777913253.4995317 | source=vosk | frequency_hz=326.8 | rms=296 | updated_at=1777913246.988506
- [2026-05-05 00:47:33] operator / voice_transcript_final / voice: disable smart sentry
  meta: kind=final | timestamp=1777913253.757429 | source=final | frequency_hz=408.0 | rms=286 | updated_at=1777913253.749306
- [2026-05-05 00:47:34] operator / voice_command / voice: disable smart sentry
  meta: normalized=True
- [2026-05-05 00:47:35] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:47:40] operator / voice_transcript_partial / voice: resume
  meta: kind=partial | timestamp=1777913260.496647 | source=vosk | frequency_hz=284.2 | rms=291 | updated_at=1777913257.2437224
- [2026-05-05 00:47:41] operator / voice_transcript_final / voice: resume
  meta: kind=final | timestamp=1777913261.2449484 | source=final | frequency_hz=284.2 | rms=291 | updated_at=1777913257.2437224
- [2026-05-05 00:47:41] operator / voice_command / voice: resume
  meta: normalized=True
- [2026-05-05 00:47:42] operator / voice_transcript_partial / voice: change
  meta: kind=partial | timestamp=1777913262.25223 | source=vosk | frequency_hz=284.2 | rms=291 | updated_at=1777913257.2437224
- [2026-05-05 00:47:42] operator / voice_transcript_partial / voice: change smart
  meta: kind=partial | timestamp=1777913262.4939332 | source=vosk | frequency_hz=284.2 | rms=291 | updated_at=1777913257.2437224
- [2026-05-05 00:47:42] operator / voice_transcript_partial / voice: change smart sentry
  meta: kind=partial | timestamp=1777913262.7438614 | source=vosk | frequency_hz=284.2 | rms=291 | updated_at=1777913257.2437224
- [2026-05-05 00:47:43] operator / voice_transcript_final / voice: change smart
  meta: kind=final | timestamp=1777913263.5416257 | source=final | frequency_hz=284.2 | rms=291 | updated_at=1777913257.2437224
- [2026-05-05 00:47:44] operator / voice_command / voice: change smart
  meta: normalized=True
- [2026-05-05 00:47:47] assistant / spoken_confirmation / voice: I think I heard resume. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:47:47] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:47:54] operator / voice_transcript_partial / voice: disconnect
  meta: kind=partial | timestamp=1777913274.5460813 | source=vosk | frequency_hz=400.0 | rms=263 | updated_at=1777913266.7377243
- [2026-05-05 00:47:55] operator / voice_transcript_partial / voice: what do
  meta: kind=partial | timestamp=1777913275.2444174 | source=vosk | frequency_hz=400.0 | rms=263 | updated_at=1777913266.7377243
- [2026-05-05 00:47:55] operator / voice_transcript_final / voice: what do
  meta: kind=final | timestamp=1777913275.9961596 | source=final | frequency_hz=400.0 | rms=263 | updated_at=1777913266.7377243
- [2026-05-05 00:47:56] operator / voice_command / voice: what do
  meta: normalized=True
- [2026-05-05 00:47:59] assistant / spoken_confirmation / voice: No confirmation received. I did not run resume.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:48:17] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777913297.244249 | source=vosk | frequency_hz=335.8 | rms=267 | updated_at=1777913295.4890301
- [2026-05-05 00:48:35] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777913315.7457995 | source=vosk | frequency_hz=408.0 | rms=283 | updated_at=1777913313.9898758
- [2026-05-05 00:48:36] operator / voice_transcript_partial / voice: smart ahead
  meta: kind=partial | timestamp=1777913316.0482268 | source=vosk | frequency_hz=408.0 | rms=283 | updated_at=1777913313.9898758
- [2026-05-05 00:48:36] operator / voice_transcript_final / voice: unk
  meta: kind=final | timestamp=1777913316.245662 | source=final | frequency_hz=408.0 | rms=283 | updated_at=1777913313.9898758
- [2026-05-05 00:48:38] operator / voice_transcript_partial / voice: lion
  meta: kind=partial | timestamp=1777913318.52947 | source=vosk | frequency_hz=408.0 | rms=283 | updated_at=1777913313.9898758
- [2026-05-05 00:48:39] operator / voice_transcript_final / voice: lion
  meta: kind=final | timestamp=1777913319.2474985 | source=final | frequency_hz=408.0 | rms=283 | updated_at=1777913313.9898758
- [2026-05-05 00:48:39] operator / voice_command / voice: lion
  meta: normalized=True
- [2026-05-05 00:48:41] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:48:41] operator / voice_transcript_partial / voice: delay
  meta: kind=partial | timestamp=1777913321.7654376 | source=vosk | frequency_hz=326.2 | rms=321 | updated_at=1777913321.239762
- [2026-05-05 00:48:42] operator / voice_transcript_final / voice: delay
  meta: kind=final | timestamp=1777913322.2457967 | source=final | frequency_hz=352.0 | rms=273 | updated_at=1777913321.9908628
- [2026-05-05 00:48:42] operator / voice_command / voice: delay
  meta: normalized=True
- [2026-05-05 00:48:43] operator / voice_transcript_partial / voice: less
  meta: kind=partial | timestamp=1777913323.495281 | source=vosk | frequency_hz=352.0 | rms=273 | updated_at=1777913321.9908628
- [2026-05-05 00:48:43] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777913323.7448587 | source=vosk | frequency_hz=352.0 | rms=273 | updated_at=1777913321.9908628
- [2026-05-05 00:48:43] operator / voice_transcript_partial / voice: decrease response
  meta: kind=partial | timestamp=1777913323.9962394 | source=vosk | frequency_hz=352.0 | rms=273 | updated_at=1777913321.9908628
- [2026-05-05 00:48:44] operator / voice_transcript_partial / voice: change
  meta: kind=partial | timestamp=1777913324.4958918 | source=vosk | frequency_hz=352.0 | rms=273 | updated_at=1777913321.9908628
- [2026-05-05 00:48:45] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:48:44] operator / voice_transcript_partial / voice: change on commands
  meta: kind=partial | timestamp=1777913324.7470307 | source=vosk | frequency_hz=352.0 | rms=273 | updated_at=1777913321.9908628
- [2026-05-05 00:48:45] operator / voice_transcript_partial / voice: change the current
  meta: kind=partial | timestamp=1777913325.0091991 | source=vosk | frequency_hz=352.0 | rms=273 | updated_at=1777913321.9908628
- [2026-05-05 00:48:46] operator / voice_transcript_final / voice: change on current
  meta: kind=final | timestamp=1777913326.2528503 | source=final | frequency_hz=322.5 | rms=250 | updated_at=1777913325.9893904
- [2026-05-05 00:48:46] operator / voice_command / voice: change on current
  meta: normalized=True
- [2026-05-05 00:48:47] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777913327.292964 | source=vosk | frequency_hz=322.5 | rms=250 | updated_at=1777913325.9893904
- [2026-05-05 00:48:47] operator / voice_transcript_partial / voice: serial
  meta: kind=partial | timestamp=1777913327.2990735 | source=vosk | frequency_hz=322.5 | rms=250 | updated_at=1777913325.9893904
- [2026-05-05 00:48:47] operator / voice_transcript_partial / voice: decrease repeat
  meta: kind=partial | timestamp=1777913327.3055873 | source=vosk | frequency_hz=316.0 | rms=257 | updated_at=1777913327.3000734
- [2026-05-05 00:48:48] operator / voice_transcript_final / voice: decrease repeat
  meta: kind=final | timestamp=1777913328.6878748 | source=final | frequency_hz=260.0 | rms=692 | updated_at=1777913328.0435984
- [2026-05-05 00:48:49] operator / voice_command / voice: decrease repeat
  meta: normalized=True
- [2026-05-05 00:48:50] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:48:50] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:48:51] operator / voice_transcript_partial / voice: what do
  meta: kind=partial | timestamp=1777913331.69674 | source=vosk | frequency_hz=309.7 | rms=252 | updated_at=1777913330.939771
- [2026-05-05 00:48:51] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1777913331.9631376 | source=vosk | frequency_hz=309.7 | rms=252 | updated_at=1777913330.939771
- [2026-05-05 00:48:52] operator / voice_transcript_partial / voice: what e speed
  meta: kind=partial | timestamp=1777913332.1980567 | source=vosk | frequency_hz=309.7 | rms=252 | updated_at=1777913330.939771
- [2026-05-05 00:48:52] operator / voice_transcript_partial / voice: what e you
  meta: kind=partial | timestamp=1777913332.4742131 | source=vosk | frequency_hz=309.7 | rms=252 | updated_at=1777913330.939771
- [2026-05-05 00:48:52] operator / voice_transcript_partial / voice: what e you a lion
  meta: kind=partial | timestamp=1777913332.697647 | source=vosk | frequency_hz=309.7 | rms=252 | updated_at=1777913330.939771
- [2026-05-05 00:48:52] operator / voice_transcript_partial / voice: what e you enable
  meta: kind=partial | timestamp=1777913332.9462843 | source=vosk | frequency_hz=309.7 | rms=252 | updated_at=1777913330.939771
- [2026-05-05 00:48:53] operator / voice_transcript_partial / voice: what e you enable e abort
  meta: kind=partial | timestamp=1777913333.4466832 | source=vosk | frequency_hz=309.7 | rms=252 | updated_at=1777913330.939771
- [2026-05-05 00:48:53] operator / voice_transcript_final / voice: what e you enable unk
  meta: kind=final | timestamp=1777913333.725119 | source=final | frequency_hz=309.7 | rms=252 | updated_at=1777913330.939771
- [2026-05-05 00:48:53] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777913333.945546 | source=vosk | frequency_hz=309.7 | rms=252 | updated_at=1777913330.939771
- [2026-05-05 00:48:54] operator / voice_transcript_partial / voice: rest
  meta: kind=partial | timestamp=1777913334.1959054 | source=vosk | frequency_hz=310.0 | rms=259 | updated_at=1777913334.1893876
- [2026-05-05 00:48:54] operator / voice_transcript_partial / voice: rest what do
  meta: kind=partial | timestamp=1777913334.6952078 | source=vosk | frequency_hz=310.0 | rms=259 | updated_at=1777913334.1893876
- [2026-05-05 00:48:54] operator / voice_transcript_partial / voice: rest what do it
  meta: kind=partial | timestamp=1777913334.9736054 | source=vosk | frequency_hz=310.0 | rms=259 | updated_at=1777913334.1893876
- [2026-05-05 00:48:55] operator / voice_transcript_partial / voice: rest what do it again
  meta: kind=partial | timestamp=1777913335.1943083 | source=vosk | frequency_hz=310.0 | rms=259 | updated_at=1777913334.1893876
- [2026-05-05 00:48:55] operator / voice_transcript_partial / voice: rest disable status
  meta: kind=partial | timestamp=1777913335.4651825 | source=vosk | frequency_hz=310.0 | rms=259 | updated_at=1777913334.1893876
- [2026-05-05 00:48:55] operator / voice_transcript_partial / voice: rest disable the
  meta: kind=partial | timestamp=1777913335.697346 | source=vosk | frequency_hz=310.0 | rms=259 | updated_at=1777913334.1893876
- [2026-05-05 00:48:55] operator / voice_transcript_partial / voice: rest disable the current app
  meta: kind=partial | timestamp=1777913335.9451098 | source=vosk | frequency_hz=310.0 | rms=259 | updated_at=1777913334.1893876
- [2026-05-05 00:48:56] operator / voice_transcript_partial / voice: rest disable the current that again
  meta: kind=partial | timestamp=1777913336.1982405 | source=vosk | frequency_hz=310.0 | rms=259 | updated_at=1777913334.1893876
- [2026-05-05 00:48:56] operator / voice_transcript_partial / voice: rest disable the current that again change
  meta: kind=partial | timestamp=1777913336.4451618 | source=vosk | frequency_hz=310.0 | rms=259 | updated_at=1777913334.1893876
- [2026-05-05 00:48:56] operator / voice_transcript_partial / voice: rest disable the current that again change smart
  meta: kind=partial | timestamp=1777913336.9457204 | source=vosk | frequency_hz=310.0 | rms=259 | updated_at=1777913334.1893876
- [2026-05-05 00:48:57] operator / voice_transcript_partial / voice: rest disable the current that again change smart sentry
  meta: kind=partial | timestamp=1777913337.2287946 | source=vosk | frequency_hz=310.0 | rms=259 | updated_at=1777913334.1893876
- [2026-05-05 00:48:57] operator / voice_transcript_partial / voice: rest disable the current that again change smart sentry lion
  meta: kind=partial | timestamp=1777913337.7194097 | source=vosk | frequency_hz=310.0 | rms=259 | updated_at=1777913334.1893876
- [2026-05-05 00:48:57] operator / voice_transcript_partial / voice: rest disable the current that again change smart sentry what
  meta: kind=partial | timestamp=1777913337.9453838 | source=vosk | frequency_hz=310.0 | rms=259 | updated_at=1777913334.1893876
- [2026-05-05 00:48:58] operator / voice_transcript_final / voice: do it again
  meta: kind=final | timestamp=1777913338.2829225 | source=final | frequency_hz=310.0 | rms=259 | updated_at=1777913334.1893876
- [2026-05-05 00:48:58] operator / voice_command / voice: do it again
  meta: normalized=True
- [2026-05-05 00:48:58] operator / voice_transcript_partial / voice: enable
  meta: kind=partial | timestamp=1777913338.4465263 | source=vosk | frequency_hz=232.0 | rms=248 | updated_at=1777913338.4400227
- [2026-05-05 00:48:58] operator / voice_transcript_partial / voice: same but
  meta: kind=partial | timestamp=1777913338.6944096 | source=vosk | frequency_hz=241.8 | rms=258 | updated_at=1777913338.690783
- [2026-05-05 00:48:59] operator / voice_command / voice: enable smart sentry
  meta: normalized=True
- [2026-05-05 00:48:59] operator / voice_transcript_final / voice: same
  meta: kind=final | timestamp=1777913339.550904 | source=final | frequency_hz=256.9 | rms=266 | updated_at=1777913339.4409657
- [2026-05-05 00:49:00] operator / voice_command / voice: same
  meta: normalized=True
- [2026-05-05 00:49:01] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:49:01] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:49:03] operator / voice_transcript_partial / voice: the smart
  meta: kind=partial | timestamp=1777913343.4450638 | source=vosk | frequency_hz=317.8 | rms=402 | updated_at=1777913342.4402418
- [2026-05-05 00:49:03] operator / voice_transcript_partial / voice: less no
  meta: kind=partial | timestamp=1777913343.714418 | source=vosk | frequency_hz=317.8 | rms=402 | updated_at=1777913342.4402418
- [2026-05-05 00:49:04] operator / voice_transcript_partial / voice: less no change
  meta: kind=partial | timestamp=1777913344.2098556 | source=vosk | frequency_hz=317.8 | rms=402 | updated_at=1777913342.4402418
- [2026-05-05 00:49:04] operator / voice_transcript_partial / voice: less no repeat
  meta: kind=partial | timestamp=1777913344.4459777 | source=vosk | frequency_hz=317.8 | rms=402 | updated_at=1777913342.4402418
- [2026-05-05 00:49:04] operator / voice_transcript_partial / voice: less no do it again on commands
  meta: kind=partial | timestamp=1777913344.6961446 | source=vosk | frequency_hz=317.8 | rms=402 | updated_at=1777913342.4402418
- [2026-05-05 00:49:04] operator / voice_transcript_partial / voice: less no repeat go home
  meta: kind=partial | timestamp=1777913344.9466226 | source=vosk | frequency_hz=317.8 | rms=402 | updated_at=1777913342.4402418
- [2026-05-05 00:49:05] operator / voice_transcript_partial / voice: less no do it again on current
  meta: kind=partial | timestamp=1777913345.1981232 | source=vosk | frequency_hz=317.8 | rms=402 | updated_at=1777913342.4402418
- [2026-05-05 00:49:05] operator / voice_transcript_partial / voice: less no do it again on current app override
  meta: kind=partial | timestamp=1777913345.7009838 | source=vosk | frequency_hz=317.8 | rms=402 | updated_at=1777913342.4402418
- [2026-05-05 00:49:06] operator / voice_transcript_partial / voice: less no do it again on current app override same but
  meta: kind=partial | timestamp=1777913346.6948647 | source=vosk | frequency_hz=317.8 | rms=402 | updated_at=1777913342.4402418
- [2026-05-05 00:49:06] operator / voice_transcript_partial / voice: less no do it again on current app override say be
  meta: kind=partial | timestamp=1777913346.9511588 | source=vosk | frequency_hz=317.8 | rms=402 | updated_at=1777913342.4402418
- [2026-05-05 00:49:07] operator / voice_transcript_partial / voice: less no do it again on current app behavior
  meta: kind=partial | timestamp=1777913347.4476256 | source=vosk | frequency_hz=344.0 | rms=257 | updated_at=1777913347.4401093
- [2026-05-05 00:49:08] operator / voice_transcript_final / voice: less no do on current app behavior
  meta: kind=final | timestamp=1777913348.20007 | source=final | frequency_hz=306.5 | rms=255 | updated_at=1777913348.191476
- [2026-05-05 00:49:08] operator / voice_command / voice: less no do on current app behavior
  meta: normalized=True
- [2026-05-05 00:49:09] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:49:09] operator / voice_transcript_partial / voice: a all
  meta: kind=partial | timestamp=1777913349.6950402 | source=vosk | frequency_hz=344.8 | rms=270 | updated_at=1777913348.6993332
- [2026-05-05 00:49:10] operator / voice_transcript_partial / voice: a all repeat
  meta: kind=partial | timestamp=1777913350.6955106 | source=vosk | frequency_hz=288.0 | rms=250 | updated_at=1777913350.6903749
- [2026-05-05 00:49:11] operator / voice_transcript_final / voice: a all repeat
  meta: kind=final | timestamp=1777913351.717431 | source=final | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:12] operator / voice_command / voice: a all repeat
  meta: normalized=True
- [2026-05-05 00:49:12] operator / voice_transcript_partial / voice: home
  meta: kind=partial | timestamp=1777913352.198503 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:12] operator / voice_transcript_partial / voice: home anything
  meta: kind=partial | timestamp=1777913352.4456534 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:12] operator / voice_transcript_partial / voice: home sentry
  meta: kind=partial | timestamp=1777913352.7081585 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:12] operator / voice_transcript_partial / voice: home anything to
  meta: kind=partial | timestamp=1777913352.9460812 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:13] operator / voice_transcript_partial / voice: home sentry do you
  meta: kind=partial | timestamp=1777913353.1978705 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:13] operator / voice_transcript_partial / voice: home sentry do you lion
  meta: kind=partial | timestamp=1777913353.4498565 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:14] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:49:13] operator / voice_transcript_partial / voice: home sentry do you lion change
  meta: kind=partial | timestamp=1777913353.7030149 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:13] operator / voice_transcript_partial / voice: home sentry do you lion repeat
  meta: kind=partial | timestamp=1777913353.946163 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:14] operator / voice_transcript_partial / voice: home sentry do you lion change theme
  meta: kind=partial | timestamp=1777913354.1985064 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:14] operator / voice_transcript_partial / voice: home sentry do you lion connect the
  meta: kind=partial | timestamp=1777913354.4492347 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:15] operator / voice_transcript_final / voice: home sentry do you lion to repeat
  meta: kind=final | timestamp=1777913355.4485977 | source=final | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:15] operator / voice_command / voice: home sentry do you lion to repeat
  meta: normalized=True
- [2026-05-05 00:49:16] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777913356.1960673 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:16] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777913356.5334563 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:16] operator / voice_transcript_partial / voice: decrease repeat it
  meta: kind=partial | timestamp=1777913356.6961238 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:17] operator / voice_transcript_partial / voice: decrease repeat e
  meta: kind=partial | timestamp=1777913357.1969078 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:17] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:49:17] operator / voice_transcript_partial / voice: decrease repeat e you
  meta: kind=partial | timestamp=1777913357.4476109 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:17] operator / voice_transcript_partial / voice: decrease repeat e you less
  meta: kind=partial | timestamp=1777913357.9454126 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:18] operator / voice_transcript_partial / voice: decrease repeat e you resume to
  meta: kind=partial | timestamp=1777913358.1964142 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:18] operator / voice_transcript_partial / voice: decrease repeat e you resume to be
  meta: kind=partial | timestamp=1777913358.4456806 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:18] operator / voice_transcript_partial / voice: decrease repeat e you resume to be more
  meta: kind=partial | timestamp=1777913358.9463627 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:19] operator / voice_transcript_partial / voice: decrease repeat e you resume to be more brightness
  meta: kind=partial | timestamp=1777913359.1975405 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:19] operator / voice_transcript_partial / voice: decrease repeat e you resume to be more be
  meta: kind=partial | timestamp=1777913359.4449382 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:19] operator / voice_transcript_partial / voice: decrease repeat e you resume to be more be less
  meta: kind=partial | timestamp=1777913359.9461935 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:20] operator / voice_transcript_partial / voice: decrease repeat e you resume to be more be less change
  meta: kind=partial | timestamp=1777913360.9605494 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:21] operator / voice_transcript_partial / voice: decrease repeat e you resume to be more be less change on commands
  meta: kind=partial | timestamp=1777913361.4472365 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:21] operator / voice_transcript_partial / voice: decrease repeat e you resume to be more be less change on current
  meta: kind=partial | timestamp=1777913361.6966102 | source=vosk | frequency_hz=315.2 | rms=262 | updated_at=1777913351.6913655
- [2026-05-05 00:49:22] operator / voice_transcript_final / voice: decrease repeat e you resume to be more be less change on current
  meta: kind=final | timestamp=1777913362.7337723 | source=final | frequency_hz=249.4 | rms=256 | updated_at=1777913362.6901603
- [2026-05-05 00:49:23] operator / voice_command / voice: decrease repeat e you resume to be more be less change on current
  meta: normalized=True
- [2026-05-05 00:49:23] operator / voice_transcript_partial / voice: response
  meta: kind=partial | timestamp=1777913363.6606538 | source=vosk | frequency_hz=249.4 | rms=256 | updated_at=1777913362.6901603
- [2026-05-05 00:49:23] operator / voice_transcript_partial / voice: increase repeat
  meta: kind=partial | timestamp=1777913363.6982756 | source=vosk | frequency_hz=249.4 | rms=256 | updated_at=1777913362.6901603
- [2026-05-05 00:49:24] operator / voice_transcript_final / voice: increase repeat
  meta: kind=final | timestamp=1777913364.4715283 | source=final | frequency_hz=296.2 | rms=256 | updated_at=1777913364.4399693
- [2026-05-05 00:49:25] operator / voice_command / voice: increase repeat
  meta: normalized=True
- [2026-05-05 00:49:25] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1777913365.4472 | source=vosk | frequency_hz=266.5 | rms=267 | updated_at=1777913364.940254
- [2026-05-05 00:49:25] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:49:25] operator / voice_transcript_partial / voice: e what
  meta: kind=partial | timestamp=1777913365.963095 | source=vosk | frequency_hz=266.5 | rms=267 | updated_at=1777913364.940254
- [2026-05-05 00:49:26] operator / voice_transcript_partial / voice: e what do it
  meta: kind=partial | timestamp=1777913366.1982896 | source=vosk | frequency_hz=266.5 | rms=267 | updated_at=1777913364.940254
- [2026-05-05 00:49:26] operator / voice_transcript_partial / voice: e what theme elian
  meta: kind=partial | timestamp=1777913366.4476545 | source=vosk | frequency_hz=266.5 | rms=267 | updated_at=1777913364.940254
- [2026-05-05 00:49:26] operator / voice_transcript_partial / voice: e lion talk less strict
  meta: kind=partial | timestamp=1777913366.6994543 | source=vosk | frequency_hz=266.5 | rms=267 | updated_at=1777913364.940254
- [2026-05-05 00:49:26] operator / voice_transcript_partial / voice: e lion talk less connect go
  meta: kind=partial | timestamp=1777913366.9472265 | source=vosk | frequency_hz=372.0 | rms=266 | updated_at=1777913366.9402869
- [2026-05-05 00:49:28] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:49:29] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:49:29] assistant / spoken_confirmation / voice: I heard the request, but only the registered operator can change Smart Sentry settings.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 00:49:27] operator / voice_transcript_final / voice: e what theme less connect go
  meta: kind=final | timestamp=1777913367.94716 | source=final | frequency_hz=323.0 | rms=259 | updated_at=1777913367.1903389
- [2026-05-05 00:49:29] operator / voice_command / voice: e what theme less connect go
  meta: normalized=True
- [2026-05-05 00:49:30] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777913370.9476893 | source=vosk | frequency_hz=306.9 | rms=251 | updated_at=1777913370.19003
- [2026-05-05 00:49:31] operator / voice_transcript_partial / voice: status report
  meta: kind=partial | timestamp=1777913371.4702306 | source=vosk | frequency_hz=340.9 | rms=260 | updated_at=1777913371.4456005
- [2026-05-05 00:49:31] operator / voice_transcript_partial / voice: status what do
  meta: kind=partial | timestamp=1777913371.7388055 | source=vosk | frequency_hz=311.2 | rms=258 | updated_at=1777913371.7051706
- [2026-05-05 00:49:32] operator / voice_transcript_final / voice: status report
  meta: kind=final | timestamp=1777913372.1967561 | source=final | frequency_hz=311.2 | rms=258 | updated_at=1777913371.7051706
- [2026-05-05 00:49:32] operator / voice_command / voice: status report
  meta: normalized=True
- [2026-05-05 00:49:33] operator / voice_transcript_partial / voice: a check status
  meta: kind=partial | timestamp=1777913373.19695 | source=vosk | frequency_hz=311.2 | rms=258 | updated_at=1777913371.7051706
- [2026-05-05 00:49:33] operator / voice_transcript_partial / voice: decrease
  meta: kind=partial | timestamp=1777913373.4457493 | source=vosk | frequency_hz=311.2 | rms=258 | updated_at=1777913371.7051706
- [2026-05-05 00:49:33] operator / voice_transcript_partial / voice: are you
  meta: kind=partial | timestamp=1777913373.6974201 | source=vosk | frequency_hz=311.2 | rms=258 | updated_at=1777913371.7051706
- [2026-05-05 00:49:33] operator / voice_transcript_partial / voice: a check status
  meta: kind=partial | timestamp=1777913373.9476223 | source=vosk | frequency_hz=311.2 | rms=258 | updated_at=1777913371.7051706
- [2026-05-05 00:49:34] operator / voice_transcript_partial / voice: decrease silence
  meta: kind=partial | timestamp=1777913374.2147987 | source=vosk | frequency_hz=311.2 | rms=258 | updated_at=1777913371.7051706
- [2026-05-05 00:49:34] operator / voice_transcript_partial / voice: decrease brightness
  meta: kind=partial | timestamp=1777913374.4466443 | source=vosk | frequency_hz=311.2 | rms=258 | updated_at=1777913371.7051706
- [2026-05-05 00:49:35] assistant / spoken_reply / voice: Smart Sentry is paused right now. Latest AI note. Smart Sentry is paused right now. Latest AI note. Analysis complete. Detection=Yolo Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1. End of analysys report.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-05 00:49:34] operator / voice_transcript_final / voice: a check sentry
  meta: kind=final | timestamp=1777913374.8129528 | source=final | frequency_hz=311.2 | rms=258 | updated_at=1777913371.7051706
- [2026-05-05 00:49:35] operator / voice_command / voice: a check sentry
  meta: normalized=True
- [2026-05-05 00:49:36] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777913376.014434 | source=vosk | frequency_hz=404.0 | rms=259 | updated_at=1777913375.1952927
- [2026-05-05 00:49:36] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777913376.2048712 | source=vosk | frequency_hz=387.2 | rms=796 | updated_at=1777913376.1902633
- [2026-05-05 00:49:36] operator / voice_transcript_partial / voice: the boards
  meta: kind=partial | timestamp=1777913376.4619443 | source=vosk | frequency_hz=387.2 | rms=796 | updated_at=1777913376.1902633
- [2026-05-05 00:49:36] operator / voice_transcript_partial / voice: the board that
  meta: kind=partial | timestamp=1777913376.6967456 | source=vosk | frequency_hz=387.2 | rms=796 | updated_at=1777913376.1902633
- [2026-05-05 00:49:36] operator / voice_transcript_partial / voice: the board status
  meta: kind=partial | timestamp=1777913376.9466143 | source=vosk | frequency_hz=387.2 | rms=796 | updated_at=1777913376.1902633
- [2026-05-05 00:49:37] operator / voice_transcript_partial / voice: the board status report
  meta: kind=partial | timestamp=1777913377.4478877 | source=vosk | frequency_hz=387.2 | rms=796 | updated_at=1777913376.1902633
- [2026-05-05 00:49:37] operator / voice_transcript_partial / voice: the board same alien what
  meta: kind=partial | timestamp=1777913377.7144365 | source=vosk | frequency_hz=387.2 | rms=796 | updated_at=1777913376.1902633
- [2026-05-05 00:49:37] operator / voice_transcript_partial / voice: the board same alien what do
  meta: kind=partial | timestamp=1777913377.9463925 | source=vosk | frequency_hz=387.2 | rms=796 | updated_at=1777913376.1902633
- [2026-05-05 00:49:38] operator / voice_transcript_final / voice: the board same status what
  meta: kind=final | timestamp=1777913378.7279587 | source=final | frequency_hz=272.0 | rms=256 | updated_at=1777913378.4566085
- [2026-05-05 00:49:39] operator / voice_command / voice: the board same status what
  meta: normalized=True
- [2026-05-05 00:49:39] operator / voice_transcript_partial / voice: less strict on
  meta: kind=partial | timestamp=1777913379.7031455 | source=vosk | frequency_hz=272.0 | rms=256 | updated_at=1777913378.4566085
- [2026-05-05 00:49:39] operator / voice_transcript_partial / voice: less strict on you
  meta: kind=partial | timestamp=1777913379.9679644 | source=vosk | frequency_hz=272.0 | rms=256 | updated_at=1777913378.4566085
- [2026-05-05 00:49:40] operator / voice_transcript_partial / voice: less strict on smart
  meta: kind=partial | timestamp=1777913380.204259 | source=vosk | frequency_hz=272.0 | rms=256 | updated_at=1777913378.4566085
- [2026-05-05 00:49:40] operator / voice_transcript_partial / voice: less strict on say
  meta: kind=partial | timestamp=1777913380.450296 | source=vosk | frequency_hz=272.0 | rms=256 | updated_at=1777913378.4566085
- [2026-05-05 00:49:42] assistant / spoken_confirmation / voice: Received. I started your background analysis about the board same status what in the background.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 00:49:41] operator / voice_transcript_final / voice: less strict on say that
  meta: kind=final | timestamp=1777913381.9621816 | source=final | frequency_hz=272.0 | rms=256 | updated_at=1777913378.4566085
- [2026-05-05 00:49:43] operator / voice_command / voice: less strict on say that
  meta: normalized=True
- [2026-05-05 00:49:43] operator / voice_transcript_partial / voice: a lion
  meta: kind=partial | timestamp=1777913383.1273117 | source=vosk | frequency_hz=134.0 | rms=406 | updated_at=1777913382.2727652
- [2026-05-05 00:49:43] operator / voice_transcript_partial / voice: app
  meta: kind=partial | timestamp=1777913383.133821 | source=vosk | frequency_hz=134.0 | rms=406 | updated_at=1777913382.2727652
- [2026-05-05 00:49:43] operator / voice_transcript_partial / voice: a disconnect
  meta: kind=partial | timestamp=1777913383.3971956 | source=vosk | frequency_hz=150.1 | rms=423 | updated_at=1777913383.3806086
- [2026-05-05 00:49:44] operator / voice_transcript_partial / voice: a disconnect speed
  meta: kind=partial | timestamp=1777913384.1293812 | source=vosk | frequency_hz=150.1 | rms=423 | updated_at=1777913383.3806086
- [2026-05-05 00:49:44] operator / voice_transcript_final / voice: a queue speed
  meta: kind=final | timestamp=1777913384.9506376 | source=final | frequency_hz=150.1 | rms=423 | updated_at=1777913383.3806086
- [2026-05-05 00:49:45] operator / voice_transcript_partial / voice: it
  meta: kind=partial | timestamp=1777913385.1286242 | source=vosk | frequency_hz=150.1 | rms=423 | updated_at=1777913383.3806086
- [2026-05-05 00:49:45] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777913385.3787909 | source=vosk | frequency_hz=150.1 | rms=423 | updated_at=1777913383.3806086
- [2026-05-05 00:49:45] operator / voice_transcript_partial / voice: alion what
  meta: kind=partial | timestamp=1777913385.9078484 | source=vosk | frequency_hz=150.1 | rms=423 | updated_at=1777913383.3806086
- [2026-05-05 00:49:47] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 00:49:46] operator / voice_transcript_partial / voice: alion what do
  meta: kind=partial | timestamp=1777913386.1551538 | source=vosk | frequency_hz=150.1 | rms=423 | updated_at=1777913383.3806086
- [2026-05-05 00:49:47] operator / voice_transcript_partial / voice: alion what do and
  meta: kind=partial | timestamp=1777913387.4001124 | source=vosk | frequency_hz=150.1 | rms=423 | updated_at=1777913383.3806086
- [2026-05-05 00:49:47] operator / voice_transcript_final / voice: what do unk
  meta: kind=final | timestamp=1777913387.7372973 | source=final | frequency_hz=150.1 | rms=423 | updated_at=1777913383.3806086
- [2026-05-05 00:49:49] operator / voice_command / voice: what do unk
  meta: normalized=True
- [2026-05-05 00:49:47] operator / voice_transcript_partial / voice: cancel
  meta: kind=partial | timestamp=1777913387.88789 | source=vosk | frequency_hz=150.1 | rms=423 | updated_at=1777913383.3806086
- [2026-05-05 00:49:48] operator / voice_transcript_partial / voice: speed
  meta: kind=partial | timestamp=1777913388.1381834 | source=vosk | frequency_hz=150.1 | rms=423 | updated_at=1777913383.3806086
- [2026-05-05 00:49:48] operator / voice_transcript_partial / voice: [unk]
  meta: kind=partial | timestamp=1777913388.3830967 | source=vosk | frequency_hz=150.1 | rms=423 | updated_at=1777913383.3806086

# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-05 13:31:01
- Entries: 265
- Roles: {'assistant': 11, 'system': 1, 'operator': 253}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 1, 'spoken_confirmation': 9, 'voice_transcript_partial': 204, 'voice_transcript_final': 43, 'voice_command': 6}
- Channels: {'text': 2, 'voice': 263}
- Latest operator request: line the
- Latest assistant message: No confirmation received. I did not run can you tell a joke.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-05 13:16:53] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 13:16:53] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-05 13:16:55] system / voice_status / voice: listening
  meta: kind=status | timestamp=1777958215.3285644 | source=windows
- [2026-05-05 13:16:59] assistant / spoken_confirmation / voice: Smart Sentry AI is online. What do you want me to do first?
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 13:17:06] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777958226.734094 | source=windows
- [2026-05-05 13:17:07] operator / voice_transcript_final / voice: as
  meta: kind=final | timestamp=1777958227.160487 | source=final | confidence=0.81
- [2026-05-05 13:17:07] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777958227.3554268 | source=windows
- [2026-05-05 13:17:07] operator / voice_transcript_partial / voice: some
  meta: kind=partial | timestamp=1777958227.3554268 | source=windows
- [2026-05-05 13:17:07] operator / voice_transcript_partial / voice: smart
  meta: kind=partial | timestamp=1777958227.5591757 | source=windows
- [2026-05-05 13:17:07] operator / voice_transcript_partial / voice: smart as
  meta: kind=partial | timestamp=1777958227.7613668 | source=windows
- [2026-05-05 13:17:08] operator / voice_transcript_partial / voice: he was
  meta: kind=partial | timestamp=1777958228.1690001 | source=windows
- [2026-05-05 13:17:08] operator / voice_transcript_final / voice: he was
  meta: kind=final | timestamp=1777958228.5768821 | source=final | confidence=0.06
- [2026-05-05 13:17:09] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777958229.9089906 | source=windows
- [2026-05-05 13:17:11] operator / voice_transcript_final / voice: he
  meta: kind=final | timestamp=1777958231.3427393 | source=final | confidence=0.48
- [2026-05-05 13:17:15] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777958235.4144313 | source=windows
- [2026-05-05 13:17:15] operator / voice_transcript_partial / voice: able
  meta: kind=partial | timestamp=1777958235.4144313 | source=windows
- [2026-05-05 13:17:15] operator / voice_transcript_partial / voice: the late
  meta: kind=partial | timestamp=1777958235.6212215 | source=windows
- [2026-05-05 13:17:15] operator / voice_transcript_partial / voice: the united
  meta: kind=partial | timestamp=1777958235.825366 | source=windows
- [2026-05-05 13:17:16] operator / voice_transcript_partial / voice: a boy who are
  meta: kind=partial | timestamp=1777958236.033245 | source=windows
- [2026-05-05 13:17:16] operator / voice_transcript_partial / voice: a blatantly
  meta: kind=partial | timestamp=1777958236.4387867 | source=windows
- [2026-05-05 13:17:17] operator / voice_transcript_final / voice: a blatantly
  meta: kind=final | timestamp=1777958237.052947 | source=final | confidence=0.03
- [2026-05-05 13:17:23] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777958243.1445813 | source=windows
- [2026-05-05 13:17:24] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777958244.161535 | source=final | confidence=0.18
- [2026-05-05 13:17:26] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777958246.0074697 | source=windows
- [2026-05-05 13:17:26] operator / voice_transcript_partial / voice: eighty
  meta: kind=partial | timestamp=1777958246.8512824 | source=windows
- [2026-05-05 13:17:27] operator / voice_transcript_partial / voice: eighty one
  meta: kind=partial | timestamp=1777958247.0556252 | source=windows
- [2026-05-05 13:17:27] operator / voice_transcript_partial / voice: eighty one on
  meta: kind=partial | timestamp=1777958247.2585065 | source=windows
- [2026-05-05 13:17:27] operator / voice_transcript_partial / voice: eighty one on one
  meta: kind=partial | timestamp=1777958247.4631534 | source=windows
- [2026-05-05 13:17:27] operator / voice_transcript_partial / voice: eighty one one one one
  meta: kind=partial | timestamp=1777958247.667708 | source=windows
- [2026-05-05 13:17:29] operator / voice_transcript_final / voice: 81111
  meta: kind=final | timestamp=1777958249.9102554 | source=final | confidence=0.3
- [2026-05-05 13:17:29] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777958249.910759 | source=windows
- [2026-05-05 13:17:30] operator / voice_transcript_partial / voice: one or
  meta: kind=partial | timestamp=1777958250.5165515 | source=windows
- [2026-05-05 13:17:30] operator / voice_transcript_partial / voice: one lonely
  meta: kind=partial | timestamp=1777958250.7188125 | source=windows
- [2026-05-05 13:17:30] operator / voice_transcript_partial / voice: one lonely nowhere
  meta: kind=partial | timestamp=1777958250.9223824 | source=windows
- [2026-05-05 13:17:31] operator / voice_transcript_partial / voice: one lonely when a
  meta: kind=partial | timestamp=1777958251.3284445 | source=windows
- [2026-05-05 13:17:31] operator / voice_transcript_final / voice: one lonely when a
  meta: kind=final | timestamp=1777958251.7377887 | source=final | confidence=0.56
- [2026-05-05 13:17:37] operator / voice_transcript_partial / voice: witch
  meta: kind=partial | timestamp=1777958257.010703 | source=windows
- [2026-05-05 13:17:37] operator / voice_transcript_partial / voice: which each
  meta: kind=partial | timestamp=1777958257.010703 | source=windows
- [2026-05-05 13:17:37] operator / voice_transcript_partial / voice: pitch to
  meta: kind=partial | timestamp=1777958257.5718634 | source=windows
- [2026-05-05 13:17:37] operator / voice_transcript_partial / voice: niche as soon as
  meta: kind=partial | timestamp=1777958257.9846907 | source=windows
- [2026-05-05 13:17:38] operator / voice_transcript_partial / voice: niche as soon as he has
  meta: kind=partial | timestamp=1777958258.1883044 | source=windows
- [2026-05-05 13:17:39] operator / voice_transcript_final / voice: niche as soon as he has
  meta: kind=final | timestamp=1777958259.4040012 | source=final | confidence=0.1
- [2026-05-05 13:17:42] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777958262.0294116 | source=windows
- [2026-05-05 13:17:42] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777958262.228803 | source=windows
- [2026-05-05 13:17:42] operator / voice_transcript_partial / voice: in the
  meta: kind=partial | timestamp=1777958262.4308045 | source=windows
- [2026-05-05 13:17:42] operator / voice_transcript_partial / voice: a u.s.
  meta: kind=partial | timestamp=1777958262.648868 | source=windows
- [2026-05-05 13:17:43] operator / voice_transcript_partial / voice: in the rest of the
  meta: kind=partial | timestamp=1777958263.2595682 | source=windows
- [2026-05-05 13:17:43] operator / voice_transcript_partial / voice: a u.s.
  meta: kind=partial | timestamp=1777958263.464207 | source=windows
- [2026-05-05 13:17:43] operator / voice_transcript_final / voice: a u s
  meta: kind=final | timestamp=1777958263.4873698 | source=final | confidence=0.13
- [2026-05-05 13:17:44] operator / voice_transcript_partial / voice: team
  meta: kind=partial | timestamp=1777958264.1414516 | source=windows
- [2026-05-05 13:17:45] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777958265.1516485 | source=windows
- [2026-05-05 13:17:45] operator / voice_transcript_partial / voice: be
  meta: kind=partial | timestamp=1777958265.1516485 | source=windows
- [2026-05-05 13:17:45] operator / voice_transcript_partial / voice: guy and the
  meta: kind=partial | timestamp=1777958265.557585 | source=windows
- [2026-05-05 13:17:45] operator / voice_transcript_partial / voice: is not
  meta: kind=partial | timestamp=1777958265.761587 | source=windows
- [2026-05-05 13:17:45] operator / voice_transcript_partial / voice: guy and the rest
  meta: kind=partial | timestamp=1777958265.9685032 | source=windows
- [2026-05-05 13:17:46] operator / voice_transcript_final / voice: guy and the rest
  meta: kind=final | timestamp=1777958266.810856 | source=final | confidence=0.41
- [2026-05-05 13:17:47] operator / voice_transcript_partial / voice: of the
  meta: kind=partial | timestamp=1777958267.8192883 | source=windows
- [2026-05-05 13:17:48] operator / voice_transcript_partial / voice: we
  meta: kind=partial | timestamp=1777958268.0208204 | source=windows
- [2026-05-05 13:17:48] operator / voice_transcript_partial / voice: we are
  meta: kind=partial | timestamp=1777958268.2270167 | source=windows
- [2026-05-05 13:17:48] operator / voice_transcript_partial / voice: leon
  meta: kind=partial | timestamp=1777958268.424603 | source=windows
- [2026-05-05 13:17:48] operator / voice_transcript_partial / voice: leon i
  meta: kind=partial | timestamp=1777958268.8630567 | source=windows
- [2026-05-05 13:17:49] operator / voice_transcript_final / voice: leon
  meta: kind=final | timestamp=1777958269.0665672 | source=final | confidence=0.65
- [2026-05-05 13:17:50] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777958270.0874267 | source=windows
- [2026-05-05 13:17:50] operator / voice_transcript_partial / voice: were
  meta: kind=partial | timestamp=1777958270.2898118 | source=windows
- [2026-05-05 13:17:50] operator / voice_transcript_partial / voice: was in
  meta: kind=partial | timestamp=1777958270.4930854 | source=windows
- [2026-05-05 13:17:50] operator / voice_transcript_partial / voice: was in a
  meta: kind=partial | timestamp=1777958270.6977746 | source=windows
- [2026-05-05 13:17:50] operator / voice_transcript_partial / voice: was india
  meta: kind=partial | timestamp=1777958270.9145741 | source=windows
- [2026-05-05 13:17:51] operator / voice_transcript_partial / voice: was india's
  meta: kind=partial | timestamp=1777958271.3353674 | source=windows
- [2026-05-05 13:17:52] operator / voice_transcript_final / voice: was india s
  meta: kind=final | timestamp=1777958272.5516536 | source=final | confidence=0.4
- [2026-05-05 13:17:55] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777958275.0178888 | source=windows
- [2026-05-05 13:17:55] operator / voice_transcript_partial / voice: he has
  meta: kind=partial | timestamp=1777958275.419839 | source=windows
- [2026-05-05 13:17:56] operator / voice_transcript_partial / voice: eighty when
  meta: kind=partial | timestamp=1777958276.0313377 | source=windows
- [2026-05-05 13:17:56] operator / voice_transcript_partial / voice: he has
  meta: kind=partial | timestamp=1777958276.234503 | source=windows
- [2026-05-05 13:17:56] operator / voice_transcript_partial / voice: he has earned
  meta: kind=partial | timestamp=1777958276.8457625 | source=windows
- [2026-05-05 13:17:57] operator / voice_transcript_final / voice: he has earned
  meta: kind=final | timestamp=1777958277.2962198 | source=final | confidence=0.25
- [2026-05-05 13:18:04] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777958284.5038962 | source=windows
- [2026-05-05 13:18:04] operator / voice_transcript_partial / voice: a while
  meta: kind=partial | timestamp=1777958284.7054758 | source=windows
- [2026-05-05 13:18:04] operator / voice_transcript_partial / voice: the white
  meta: kind=partial | timestamp=1777958284.914964 | source=windows
- [2026-05-05 13:18:05] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777958285.3368688 | source=windows
- [2026-05-05 13:18:05] operator / voice_transcript_partial / voice: the white
  meta: kind=partial | timestamp=1777958285.7389023 | source=windows
- [2026-05-05 13:18:05] operator / voice_transcript_partial / voice: it has
  meta: kind=partial | timestamp=1777958285.943264 | source=windows
- [2026-05-05 13:18:06] operator / voice_transcript_final / voice: it has
  meta: kind=final | timestamp=1777958286.76837 | source=final | confidence=0.02
- [2026-05-05 13:18:07] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777958287.1775887 | source=windows
- [2026-05-05 13:18:07] operator / voice_transcript_partial / voice: long
  meta: kind=partial | timestamp=1777958287.5821574 | source=windows
- [2026-05-05 13:18:07] operator / voice_transcript_partial / voice: only one
  meta: kind=partial | timestamp=1777958287.7824316 | source=windows
- [2026-05-05 13:18:08] operator / voice_transcript_final / voice: only one
  meta: kind=final | timestamp=1777958288.6519318 | source=final | confidence=0.11
- [2026-05-05 13:18:15] operator / voice_transcript_partial / voice: see
  meta: kind=partial | timestamp=1777958295.4592183 | source=windows
- [2026-05-05 13:18:15] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777958295.68111 | source=windows
- [2026-05-05 13:18:27] operator / voice_transcript_partial / voice: day
  meta: kind=partial | timestamp=1777958307.0226462 | source=windows
- [2026-05-05 13:18:27] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777958307.0226462 | source=windows
- [2026-05-05 13:18:27] operator / voice_transcript_partial / voice: here
  meta: kind=partial | timestamp=1777958307.2235372 | source=windows
- [2026-05-05 13:18:27] operator / voice_transcript_partial / voice: to believe
  meta: kind=partial | timestamp=1777958307.6280384 | source=windows
- [2026-05-05 13:18:27] operator / voice_transcript_partial / voice: to believe in
  meta: kind=partial | timestamp=1777958307.829387 | source=windows
- [2026-05-05 13:18:28] operator / voice_transcript_partial / voice: to believe he
  meta: kind=partial | timestamp=1777958308.239946 | source=windows
- [2026-05-05 13:18:29] operator / voice_transcript_final / voice: to believe he
  meta: kind=final | timestamp=1777958309.2795808 | source=final | confidence=0.26
- [2026-05-05 13:18:30] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1777958310.7628138 | source=windows
- [2026-05-05 13:18:30] operator / voice_transcript_partial / voice: has
  meta: kind=partial | timestamp=1777958310.7689774 | source=windows
- [2026-05-05 13:18:31] operator / voice_transcript_final / voice: has
  meta: kind=final | timestamp=1777958311.5825806 | source=final | confidence=0.21
- [2026-05-05 13:18:36] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777958316.496484 | source=windows
- [2026-05-05 13:18:36] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777958316.496484 | source=windows
- [2026-05-05 13:18:36] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777958316.6999547 | source=windows
- [2026-05-05 13:18:37] operator / voice_transcript_partial / voice: a clear
  meta: kind=partial | timestamp=1777958317.1076043 | source=windows
- [2026-05-05 13:18:37] operator / voice_transcript_partial / voice: a hero
  meta: kind=partial | timestamp=1777958317.310312 | source=windows
- [2026-05-05 13:18:37] operator / voice_transcript_partial / voice: a clear
  meta: kind=partial | timestamp=1777958317.518034 | source=windows
- [2026-05-05 13:18:37] operator / voice_transcript_partial / voice: made clear he
  meta: kind=partial | timestamp=1777958317.7173352 | source=windows
- [2026-05-05 13:18:38] operator / voice_transcript_final / voice: made clear he
  meta: kind=final | timestamp=1777958318.751154 | source=final | confidence=0.3
- [2026-05-05 13:18:41] operator / voice_transcript_partial / voice: may
  meta: kind=partial | timestamp=1777958321.1922367 | source=windows
- [2026-05-05 13:18:53] operator / voice_transcript_partial / voice: was fifty
  meta: kind=partial | timestamp=1777958333.680453 | source=windows
- [2026-05-05 13:19:00] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777958340.035408 | source=windows
- [2026-05-05 13:19:03] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777958343.5553448 | source=windows
- [2026-05-05 13:19:05] operator / voice_transcript_partial / voice: have a fifth
  meta: kind=partial | timestamp=1777958345.4332378 | source=windows
- [2026-05-05 13:19:06] operator / voice_transcript_partial / voice: have a fifth of
  meta: kind=partial | timestamp=1777958346.046318 | source=windows
- [2026-05-05 13:19:06] operator / voice_transcript_final / voice: have a fifth of
  meta: kind=final | timestamp=1777958346.9091032 | source=final | confidence=0.3
- [2026-05-05 13:19:11] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777958351.3712666 | source=windows | frequency_hz=308.6 | rms=175 | updated_at=1777958350.0638568
- [2026-05-05 13:19:19] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777958359.3985116 | source=final | confidence=0.08 | frequency_hz=308.6 | rms=175 | updated_at=1777958350.0638568
- [2026-05-05 13:19:27] operator / voice_transcript_partial / voice: scene
  meta: kind=partial | timestamp=1777958367.7326474 | source=windows | frequency_hz=308.6 | rms=175 | updated_at=1777958350.0638568
- [2026-05-05 13:19:27] operator / voice_transcript_partial / voice: game
  meta: kind=partial | timestamp=1777958367.9347577 | source=windows | frequency_hz=308.6 | rms=175 | updated_at=1777958350.0638568
- [2026-05-05 13:19:28] operator / voice_transcript_partial / voice: game and
  meta: kind=partial | timestamp=1777958368.341445 | source=windows | frequency_hz=308.6 | rms=175 | updated_at=1777958350.0638568
- [2026-05-05 13:19:28] operator / voice_transcript_partial / voice: be more
  meta: kind=partial | timestamp=1777958368.7512228 | source=windows | frequency_hz=308.6 | rms=175 | updated_at=1777958350.0638568
- [2026-05-05 13:19:28] operator / voice_transcript_final / voice: game and
  meta: kind=final | timestamp=1777958368.9546626 | source=final | confidence=0.57 | frequency_hz=308.6 | rms=175 | updated_at=1777958350.0638568
- [2026-05-05 13:19:30] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777958370.3724566 | source=windows | frequency_hz=308.6 | rms=175 | updated_at=1777958350.0638568
- [2026-05-05 13:19:30] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777958370.9828382 | source=final | confidence=0.82 | frequency_hz=308.6 | rms=175 | updated_at=1777958350.0638568
- [2026-05-05 13:19:37] operator / voice_transcript_partial / voice: main
  meta: kind=partial | timestamp=1777958377.0208085 | source=windows | frequency_hz=308.6 | rms=175 | updated_at=1777958350.0638568
- [2026-05-05 13:19:37] operator / voice_transcript_final / voice: main
  meta: kind=final | timestamp=1777958377.6323547 | source=final | confidence=0.03 | frequency_hz=308.6 | rms=175 | updated_at=1777958350.0638568
- [2026-05-05 13:19:42] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777958382.3498197 | source=windows | frequency_hz=367.2 | rms=195 | updated_at=1777958381.2197862
- [2026-05-05 13:19:43] operator / voice_transcript_partial / voice: the thing
  meta: kind=partial | timestamp=1777958383.5707812 | source=windows | frequency_hz=367.2 | rms=195 | updated_at=1777958381.2197862
- [2026-05-05 13:19:43] operator / voice_transcript_partial / voice: the thought
  meta: kind=partial | timestamp=1777958383.9743748 | source=windows | frequency_hz=367.2 | rms=195 | updated_at=1777958381.2197862
- [2026-05-05 13:19:44] operator / voice_transcript_partial / voice: the things
  meta: kind=partial | timestamp=1777958384.1768413 | source=windows | frequency_hz=367.2 | rms=195 | updated_at=1777958381.2197862
- [2026-05-05 13:19:44] operator / voice_transcript_partial / voice: the thing
  meta: kind=partial | timestamp=1777958384.3786905 | source=windows | frequency_hz=367.2 | rms=195 | updated_at=1777958381.2197862
- [2026-05-05 13:19:44] operator / voice_transcript_partial / voice: the thought
  meta: kind=partial | timestamp=1777958384.989685 | source=windows | frequency_hz=367.2 | rms=195 | updated_at=1777958381.2197862
- [2026-05-05 13:19:45] operator / voice_transcript_partial / voice: the thing
  meta: kind=partial | timestamp=1777958385.190968 | source=windows | frequency_hz=367.2 | rms=195 | updated_at=1777958381.2197862
- [2026-05-05 13:19:45] operator / voice_transcript_partial / voice: the th
  meta: kind=partial | timestamp=1777958385.3962102 | source=windows | frequency_hz=367.2 | rms=195 | updated_at=1777958381.2197862
- [2026-05-05 13:19:45] operator / voice_transcript_partial / voice: the thought
  meta: kind=partial | timestamp=1777958385.6006527 | source=windows | frequency_hz=367.2 | rms=195 | updated_at=1777958381.2197862
- [2026-05-05 13:19:46] operator / voice_transcript_partial / voice: the thing
  meta: kind=partial | timestamp=1777958386.016423 | source=windows | frequency_hz=261.7 | rms=4960 | updated_at=1777958385.6550593
- [2026-05-05 13:19:46] operator / voice_transcript_partial / voice: the th
  meta: kind=partial | timestamp=1777958386.4260066 | source=windows | frequency_hz=261.7 | rms=4960 | updated_at=1777958385.6550593
- [2026-05-05 13:19:46] operator / voice_transcript_partial / voice: the thick
  meta: kind=partial | timestamp=1777958386.6267014 | source=windows | frequency_hz=261.7 | rms=4960 | updated_at=1777958385.6550593
- [2026-05-05 13:19:46] operator / voice_transcript_partial / voice: the thing he
  meta: kind=partial | timestamp=1777958386.8308718 | source=windows | frequency_hz=261.7 | rms=4960 | updated_at=1777958385.6550593
- [2026-05-05 13:19:47] operator / voice_transcript_partial / voice: the things that
  meta: kind=partial | timestamp=1777958387.2400038 | source=windows | frequency_hz=261.7 | rms=4960 | updated_at=1777958385.6550593
- [2026-05-05 13:19:47] operator / voice_transcript_partial / voice: the things that if
  meta: kind=partial | timestamp=1777958387.6602454 | source=windows | frequency_hz=414.1 | rms=592 | updated_at=1777958387.3174899
- [2026-05-05 13:19:47] operator / voice_transcript_partial / voice: the thirty th
  meta: kind=partial | timestamp=1777958387.8562393 | source=windows | frequency_hz=401.8 | rms=376 | updated_at=1777958387.8255
- [2026-05-05 13:19:49] operator / voice_transcript_partial / voice: the thirty th of a
  meta: kind=partial | timestamp=1777958389.7166064 | source=windows | frequency_hz=401.8 | rms=376 | updated_at=1777958387.8255
- [2026-05-05 13:19:50] operator / voice_transcript_partial / voice: the thirty th of a deal
  meta: kind=partial | timestamp=1777958390.1204975 | source=windows | frequency_hz=401.8 | rms=376 | updated_at=1777958387.8255
- [2026-05-05 13:19:50] operator / voice_transcript_partial / voice: the thirty th of a deal yet
  meta: kind=partial | timestamp=1777958390.3234196 | source=windows | frequency_hz=156.2 | rms=2352 | updated_at=1777958390.2556028
- [2026-05-05 13:19:50] operator / voice_transcript_partial / voice: the thirty th of a deal yet more
  meta: kind=partial | timestamp=1777958390.9886491 | source=windows | frequency_hz=167.5 | rms=720 | updated_at=1777958390.6450284
- [2026-05-05 13:19:51] operator / voice_transcript_partial / voice: the thirty th of a ely and will
  meta: kind=partial | timestamp=1777958391.135616 | source=windows | frequency_hz=167.5 | rms=720 | updated_at=1777958390.6450284
- [2026-05-05 13:19:51] operator / voice_transcript_final / voice: the 30 th of a ely and will
  meta: kind=final | timestamp=1777958391.7641096 | source=final | confidence=0.22 | frequency_hz=167.5 | rms=720 | updated_at=1777958390.6450284
- [2026-05-05 13:19:52] operator / voice_transcript_partial / voice: be
  meta: kind=partial | timestamp=1777958392.5676706 | source=windows | frequency_hz=167.5 | rms=720 | updated_at=1777958390.6450284
- [2026-05-05 13:19:53] operator / voice_transcript_partial / voice: be an
  meta: kind=partial | timestamp=1777958393.1752608 | source=windows | frequency_hz=320.3 | rms=2448 | updated_at=1777958392.5676706
- [2026-05-05 13:19:53] operator / voice_transcript_partial / voice: be a mass
  meta: kind=partial | timestamp=1777958393.3793504 | source=windows | frequency_hz=250.4 | rms=242 | updated_at=1777958393.33684
- [2026-05-05 13:19:53] operator / voice_transcript_partial / voice: be a mask or
  meta: kind=partial | timestamp=1777958393.5839732 | source=windows | frequency_hz=250.4 | rms=242 | updated_at=1777958393.33684
- [2026-05-05 13:19:53] operator / voice_transcript_partial / voice: be a nice home
  meta: kind=partial | timestamp=1777958393.785724 | source=windows | frequency_hz=250.4 | rms=242 | updated_at=1777958393.33684
- [2026-05-05 13:19:54] operator / voice_transcript_final / voice: be amassed who
  meta: kind=final | timestamp=1777958394.2366283 | source=final | confidence=0.56 | frequency_hz=250.4 | rms=242 | updated_at=1777958393.33684
- [2026-05-05 13:19:57] operator / voice_transcript_partial / voice: we
  meta: kind=partial | timestamp=1777958397.0324545 | source=windows | frequency_hz=250.4 | rms=242 | updated_at=1777958393.33684
- [2026-05-05 13:19:57] operator / voice_transcript_partial / voice: played the
  meta: kind=partial | timestamp=1777958397.4388416 | source=windows | frequency_hz=250.4 | rms=242 | updated_at=1777958393.33684
- [2026-05-05 13:19:57] operator / voice_transcript_partial / voice: reduced by
  meta: kind=partial | timestamp=1777958397.641528 | source=windows | frequency_hz=250.4 | rms=242 | updated_at=1777958393.33684
- [2026-05-05 13:19:57] operator / voice_transcript_partial / voice: played the spicy
  meta: kind=partial | timestamp=1777958397.8440218 | source=windows | frequency_hz=250.4 | rms=242 | updated_at=1777958393.33684
- [2026-05-05 13:19:58] operator / voice_transcript_partial / voice: radius besieged
  meta: kind=partial | timestamp=1777958398.2519758 | source=windows | frequency_hz=250.4 | rms=242 | updated_at=1777958393.33684
- [2026-05-05 13:19:58] operator / voice_transcript_partial / voice: radius proceeds go
  meta: kind=partial | timestamp=1777958398.4573033 | source=windows | frequency_hz=164.1 | rms=161 | updated_at=1777958398.4558015
- [2026-05-05 13:19:58] operator / voice_transcript_partial / voice: played the spicy coat
  meta: kind=partial | timestamp=1777958398.6618729 | source=windows | frequency_hz=168.2 | rms=156 | updated_at=1777958398.5755134
- [2026-05-05 13:19:59] operator / voice_transcript_final / voice: played the spicy coat
  meta: kind=final | timestamp=1777958399.0706036 | source=final | confidence=0.49 | frequency_hz=168.2 | rms=156 | updated_at=1777958398.5755134
- [2026-05-05 13:20:03] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777958403.6371515 | source=windows | frequency_hz=326.6 | rms=202 | updated_at=1777958402.2973287
- [2026-05-05 13:20:04] operator / voice_transcript_final / voice: of
  meta: kind=final | timestamp=1777958404.4869423 | source=final | confidence=0.44 | frequency_hz=371.1 | rms=136 | updated_at=1777958404.3356898
- [2026-05-05 13:20:05] operator / voice_transcript_partial / voice: sea
  meta: kind=partial | timestamp=1777958405.0992336 | source=windows | frequency_hz=371.1 | rms=136 | updated_at=1777958404.3356898
- [2026-05-05 13:20:06] operator / voice_transcript_partial / voice: sea and
  meta: kind=partial | timestamp=1777958406.3472872 | source=windows | frequency_hz=414.1 | rms=137 | updated_at=1777958405.7465165
- [2026-05-05 13:20:07] operator / voice_transcript_final / voice: sea and
  meta: kind=final | timestamp=1777958407.1976385 | source=final | confidence=0.47 | frequency_hz=401.8 | rms=344 | updated_at=1777958406.3859382
- [2026-05-05 13:20:10] operator / voice_transcript_partial / voice: it's
  meta: kind=partial | timestamp=1777958410.8386905 | source=windows | frequency_hz=401.8 | rms=344 | updated_at=1777958406.3859382
- [2026-05-05 13:20:11] operator / voice_transcript_partial / voice: it's it's
  meta: kind=partial | timestamp=1777958411.6550741 | source=windows | frequency_hz=401.8 | rms=344 | updated_at=1777958406.3859382
- [2026-05-05 13:20:12] operator / voice_transcript_partial / voice: it's it's the
  meta: kind=partial | timestamp=1777958412.435919 | source=windows | frequency_hz=401.8 | rms=344 | updated_at=1777958406.3859382
- [2026-05-05 13:20:12] operator / voice_transcript_final / voice: it s it s the
  meta: kind=final | timestamp=1777958412.8979843 | source=final | confidence=0.52 | frequency_hz=401.8 | rms=344 | updated_at=1777958406.3859382
- [2026-05-05 13:20:15] operator / voice_transcript_partial / voice: true
  meta: kind=partial | timestamp=1777958415.319381 | source=windows | frequency_hz=358.0 | rms=219 | updated_at=1777958415.097078
- [2026-05-05 13:20:15] operator / voice_transcript_partial / voice: route
  meta: kind=partial | timestamp=1777958415.5299444 | source=windows | frequency_hz=358.0 | rms=219 | updated_at=1777958415.097078
- [2026-05-05 13:20:15] operator / voice_transcript_partial / voice: way through the
  meta: kind=partial | timestamp=1777958415.72802 | source=windows | frequency_hz=358.0 | rms=219 | updated_at=1777958415.097078
- [2026-05-05 13:20:16] operator / voice_transcript_partial / voice: true believer
  meta: kind=partial | timestamp=1777958416.138724 | source=windows | frequency_hz=376.3 | rms=347 | updated_at=1777958415.8563097
- [2026-05-05 13:20:16] operator / voice_transcript_partial / voice: way through the lyons
  meta: kind=partial | timestamp=1777958416.5467277 | source=windows | frequency_hz=376.3 | rms=347 | updated_at=1777958415.8563097
- [2026-05-05 13:20:16] operator / voice_transcript_final / voice: elion way through the lyons
  meta: kind=final | timestamp=1777958416.956775 | source=final | confidence=0.41 | frequency_hz=376.3 | rms=347 | updated_at=1777958415.8563097
- [2026-05-05 13:20:17] operator / voice_command / voice: elion way through the lyons
  meta: normalized=True
- [2026-05-05 13:20:18] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777958418.7913277 | source=windows | frequency_hz=376.3 | rms=347 | updated_at=1777958415.8563097
- [2026-05-05 13:20:19] operator / voice_transcript_final / voice: he
  meta: kind=final | timestamp=1777958419.6790824 | source=final | confidence=0.78 | frequency_hz=297.3 | rms=148 | updated_at=1777958419.1945512
- [2026-05-05 13:20:22] assistant / spoken_confirmation / voice: I think I heard elion way through the lyons. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 13:20:31] assistant / spoken_confirmation / voice: No confirmation received. I did not run elion way through the lyons.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 13:20:32] operator / voice_transcript_partial / voice: was
  meta: kind=partial | timestamp=1777958432.7588937 | source=windows | frequency_hz=187.5 | rms=151 | updated_at=1777958431.7376337
- [2026-05-05 13:20:40] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777958440.5274265 | source=windows | frequency_hz=187.5 | rms=151 | updated_at=1777958431.7376337
- [2026-05-05 13:20:40] operator / voice_transcript_partial / voice: hey
  meta: kind=partial | timestamp=1777958440.7298331 | source=windows | frequency_hz=187.5 | rms=151 | updated_at=1777958431.7376337
- [2026-05-05 13:20:40] operator / voice_transcript_partial / voice: ate the
  meta: kind=partial | timestamp=1777958440.9343762 | source=windows | frequency_hz=187.5 | rms=151 | updated_at=1777958431.7376337
- [2026-05-05 13:20:41] operator / voice_transcript_partial / voice: ate the lee
  meta: kind=partial | timestamp=1777958441.1388497 | source=windows | frequency_hz=187.5 | rms=151 | updated_at=1777958431.7376337
- [2026-05-05 13:20:41] operator / voice_transcript_partial / voice: ate the lyons
  meta: kind=partial | timestamp=1777958441.345102 | source=windows | frequency_hz=156.2 | rms=146 | updated_at=1777958441.3380847
- [2026-05-05 13:20:41] operator / voice_transcript_partial / voice: ate the liane
  meta: kind=partial | timestamp=1777958441.7502363 | source=windows | frequency_hz=156.2 | rms=146 | updated_at=1777958441.3380847
- [2026-05-05 13:20:42] operator / voice_transcript_final / voice: elion ate the liane
  meta: kind=final | timestamp=1777958442.013845 | source=final | confidence=0.44 | frequency_hz=156.2 | rms=146 | updated_at=1777958441.3380847
- [2026-05-05 13:20:42] operator / voice_command / voice: elion ate the liane
  meta: normalized=True
- [2026-05-05 13:20:44] assistant / spoken_confirmation / voice: I think I heard elion ate the liane. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 13:20:47] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777958447.7812226 | source=windows | frequency_hz=199.2 | rms=129 | updated_at=1777958444.787848
- [2026-05-05 13:20:51] operator / voice_transcript_partial / voice: its
  meta: kind=partial | timestamp=1777958451.4929254 | source=windows | frequency_hz=199.2 | rms=129 | updated_at=1777958444.787848
- [2026-05-05 13:20:52] operator / voice_transcript_partial / voice: it's it's
  meta: kind=partial | timestamp=1777958452.5279813 | source=windows | frequency_hz=199.2 | rms=129 | updated_at=1777958444.787848
- [2026-05-05 13:20:53] operator / voice_transcript_final / voice: it s it s
  meta: kind=final | timestamp=1777958453.346821 | source=final | confidence=0.75 | frequency_hz=199.2 | rms=129 | updated_at=1777958444.787848
- [2026-05-05 13:20:53] operator / voice_command / voice: it s it s
  meta: normalized=True
- [2026-05-05 13:20:54] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777958454.9715886 | source=windows | frequency_hz=199.2 | rms=129 | updated_at=1777958444.787848
- [2026-05-05 13:20:55] operator / voice_transcript_partial / voice: i
  meta: kind=partial | timestamp=1777958455.1758847 | source=windows | frequency_hz=199.2 | rms=129 | updated_at=1777958444.787848
- [2026-05-05 13:20:55] operator / voice_transcript_partial / voice: i have
  meta: kind=partial | timestamp=1777958455.3804314 | source=windows | frequency_hz=402.3 | rms=557 | updated_at=1777958455.2877462
- [2026-05-05 13:20:55] operator / voice_transcript_partial / voice: i have a
  meta: kind=partial | timestamp=1777958455.582275 | source=windows | frequency_hz=402.3 | rms=557 | updated_at=1777958455.2877462
- [2026-05-05 13:20:56] operator / voice_transcript_partial / voice: a head request
  meta: kind=partial | timestamp=1777958456.0008943 | source=windows | frequency_hz=396.8 | rms=144 | updated_at=1777958455.929571
- [2026-05-05 13:20:56] operator / voice_transcript_partial / voice: i have a question
  meta: kind=partial | timestamp=1777958456.1958497 | source=windows | frequency_hz=344.1 | rms=137 | updated_at=1777958456.1784618
- [2026-05-05 13:20:56] operator / voice_transcript_final / voice: i have a question
  meta: kind=final | timestamp=1777958456.6584768 | source=final | confidence=0.85 | frequency_hz=300.2 | rms=186 | updated_at=1777958456.3088543
- [2026-05-05 13:20:57] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777958457.2179213 | source=windows | frequency_hz=300.2 | rms=186 | updated_at=1777958456.3088543
- [2026-05-05 13:20:59] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 13:21:01] operator / voice_transcript_partial / voice: it's
  meta: kind=partial | timestamp=1777958461.5569956 | source=windows | frequency_hz=300.2 | rms=186 | updated_at=1777958456.3088543
- [2026-05-05 13:21:02] operator / voice_transcript_final / voice: it s
  meta: kind=final | timestamp=1777958462.1599436 | source=final | confidence=0.86 | frequency_hz=300.2 | rms=186 | updated_at=1777958456.3088543
- [2026-05-05 13:21:02] operator / voice_command / voice: it s
  meta: normalized=True
- [2026-05-05 13:21:05] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 13:21:06] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777958466.7240157 | source=windows | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:07] operator / voice_transcript_partial / voice: a huge
  meta: kind=partial | timestamp=1777958467.1272807 | source=windows | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:07] operator / voice_transcript_partial / voice: a new dell
  meta: kind=partial | timestamp=1777958467.3332336 | source=windows | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:07] operator / voice_transcript_partial / voice: a villager
  meta: kind=partial | timestamp=1777958467.537928 | source=windows | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:07] operator / voice_transcript_partial / voice: can you tell a joke
  meta: kind=partial | timestamp=1777958467.745127 | source=windows | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:09] operator / voice_transcript_final / voice: can you tell a joke
  meta: kind=final | timestamp=1777958469.012412 | source=final | confidence=0.28 | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:09] operator / voice_command / voice: can you tell a joke
  meta: normalized=True
- [2026-05-05 13:21:10] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777958470.6139746 | source=windows | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:10] operator / voice_transcript_partial / voice: there
  meta: kind=partial | timestamp=1777958470.825489 | source=windows | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:11] operator / voice_transcript_partial / voice: down the age
  meta: kind=partial | timestamp=1777958471.0202508 | source=windows | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:11] operator / voice_transcript_partial / voice: down the ager
  meta: kind=partial | timestamp=1777958471.2234223 | source=windows | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:11] operator / voice_transcript_partial / voice: tell me a joke
  meta: kind=partial | timestamp=1777958471.6282482 | source=windows | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:13] assistant / spoken_confirmation / voice: I think I heard can you tell a joke. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 13:21:18] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777958478.452754 | source=windows | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:19] operator / voice_transcript_partial / voice: that you
  meta: kind=partial | timestamp=1777958479.6866033 | source=windows | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:19] operator / voice_transcript_partial / voice: and the
  meta: kind=partial | timestamp=1777958479.88055 | source=windows | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:20] operator / voice_transcript_partial / voice: and the u.s.
  meta: kind=partial | timestamp=1777958480.0927224 | source=windows | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:20] operator / voice_transcript_final / voice: and the u s
  meta: kind=final | timestamp=1777958480.9243844 | source=final | confidence=0.18 | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:21] operator / voice_command / voice: and the u s
  meta: normalized=True
- [2026-05-05 13:21:22] operator / voice_transcript_partial / voice: be
  meta: kind=partial | timestamp=1777958482.538973 | source=windows | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:22] operator / voice_transcript_partial / voice: year
  meta: kind=partial | timestamp=1777958482.7444544 | source=windows | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:22] operator / voice_transcript_partial / voice: u.s.
  meta: kind=partial | timestamp=1777958482.947423 | source=windows | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:23] operator / voice_transcript_partial / voice: yes
  meta: kind=partial | timestamp=1777958483.1521788 | source=windows | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:23] operator / voice_transcript_final / voice: yes
  meta: kind=final | timestamp=1777958483.5603678 | source=final | confidence=0.89 | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:25] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 13:21:33] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777958493.6751537 | source=windows | frequency_hz=339.8 | rms=162 | updated_at=1777958466.168555
- [2026-05-05 13:21:34] operator / voice_transcript_partial / voice: and the
  meta: kind=partial | timestamp=1777958494.8331153 | source=windows | frequency_hz=324.4 | rms=431 | updated_at=1777958494.0741625
- [2026-05-05 13:21:35] operator / voice_transcript_partial / voice: and the thing that
  meta: kind=partial | timestamp=1777958495.7891195 | source=windows | frequency_hz=293.0 | rms=245 | updated_at=1777958495.4829192
- [2026-05-05 13:21:35] operator / voice_transcript_partial / voice: and the thing
  meta: kind=partial | timestamp=1777958495.9927845 | source=windows | frequency_hz=292.9 | rms=342 | updated_at=1777958495.9907794
- [2026-05-05 13:21:36] operator / voice_transcript_partial / voice: and the three
  meta: kind=partial | timestamp=1777958496.4138076 | source=windows | frequency_hz=331.2 | rms=459 | updated_at=1777958496.1291118
- [2026-05-05 13:21:36] operator / voice_transcript_partial / voice: and the thing that
  meta: kind=partial | timestamp=1777958496.625038 | source=windows | frequency_hz=331.2 | rms=459 | updated_at=1777958496.1291118
- [2026-05-05 13:21:36] operator / voice_transcript_partial / voice: and the things we're
  meta: kind=partial | timestamp=1777958496.8438067 | source=windows | frequency_hz=331.2 | rms=459 | updated_at=1777958496.1291118
- [2026-05-05 13:21:37] operator / voice_transcript_partial / voice: and the threat of
  meta: kind=partial | timestamp=1777958497.2678568 | source=windows | frequency_hz=331.2 | rms=459 | updated_at=1777958496.1291118
- [2026-05-05 13:21:37] operator / voice_transcript_partial / voice: and the threat of an
  meta: kind=partial | timestamp=1777958497.4659555 | source=windows | frequency_hz=331.2 | rms=459 | updated_at=1777958496.1291118
- [2026-05-05 13:21:37] operator / voice_transcript_partial / voice: and the thing that has
  meta: kind=partial | timestamp=1777958497.6660147 | source=windows | frequency_hz=331.2 | rms=459 | updated_at=1777958496.1291118
- [2026-05-05 13:21:38] operator / voice_transcript_partial / voice: and the thing that has the
  meta: kind=partial | timestamp=1777958498.0752082 | source=windows | frequency_hz=331.2 | rms=459 | updated_at=1777958496.1291118
- [2026-05-05 13:21:38] operator / voice_transcript_partial / voice: and the thing and that the
  meta: kind=partial | timestamp=1777958498.6828184 | source=windows | frequency_hz=331.2 | rms=459 | updated_at=1777958496.1291118
- [2026-05-05 13:21:39] operator / voice_transcript_partial / voice: and the thing and that the high
  meta: kind=partial | timestamp=1777958499.497507 | source=windows | frequency_hz=331.2 | rms=459 | updated_at=1777958496.1291118
- [2026-05-05 13:21:39] operator / voice_transcript_partial / voice: and the thing that has a ten-one
  meta: kind=partial | timestamp=1777958499.7030153 | source=windows | frequency_hz=331.2 | rms=459 | updated_at=1777958496.1291118
- [2026-05-05 13:21:39] operator / voice_transcript_partial / voice: and the thing and that the one thousand
  meta: kind=partial | timestamp=1777958499.9107952 | source=windows | frequency_hz=331.2 | rms=459 | updated_at=1777958496.1291118
- [2026-05-05 13:21:40] operator / voice_transcript_partial / voice: and the thing that has that that wasn't aware
  meta: kind=partial | timestamp=1777958500.3126738 | source=windows | frequency_hz=331.2 | rms=459 | updated_at=1777958496.1291118
- [2026-05-05 13:21:40] operator / voice_transcript_partial / voice: and the thing that has that that wasn't aware of the
  meta: kind=partial | timestamp=1777958500.5259008 | source=windows | frequency_hz=331.2 | rms=459 | updated_at=1777958496.1291118
- [2026-05-05 13:21:40] operator / voice_transcript_partial / voice: and the thing and that the house where he owns
  meta: kind=partial | timestamp=1777958500.9252586 | source=windows | frequency_hz=331.2 | rms=459 | updated_at=1777958496.1291118
- [2026-05-05 13:21:41] operator / voice_transcript_partial / voice: and the thing that has that that wasn't aware of the only
  meta: kind=partial | timestamp=1777958501.3395739 | source=windows | frequency_hz=331.2 | rms=459 | updated_at=1777958496.1291118
- [2026-05-05 13:21:42] operator / voice_transcript_final / voice: and the thing that has that that wasn t aware of the only
  meta: kind=final | timestamp=1777958502.1812556 | source=final | confidence=0.08 | frequency_hz=331.2 | rms=459 | updated_at=1777958496.1291118
- [2026-05-05 13:21:44] assistant / spoken_confirmation / voice: No confirmation received. I did not run can you tell a joke.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 13:24:13] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777958653.6200416 | source=windows | frequency_hz=331.2 | rms=459 | updated_at=1777958496.1291118
- [2026-05-05 13:25:30] operator / voice_transcript_partial / voice: if
  meta: kind=partial | timestamp=1777958730.013524 | source=windows | frequency_hz=331.2 | rms=459 | updated_at=1777958496.1291118
- [2026-05-05 13:25:30] operator / voice_transcript_final / voice: if
  meta: kind=final | timestamp=1777958730.2392778 | source=final | confidence=0.73 | frequency_hz=331.2 | rms=459 | updated_at=1777958496.1291118
- [2026-05-05 13:25:34] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777958734.5116963 | source=windows | frequency_hz=331.2 | rms=459 | updated_at=1777958496.1291118
- [2026-05-05 13:25:55] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777958755.5484738 | source=final | confidence=0.02 | frequency_hz=331.2 | rms=459 | updated_at=1777958496.1291118
- [2026-05-05 13:27:21] operator / voice_transcript_partial / voice: house
  meta: kind=partial | timestamp=1777958841.152654 | source=windows | frequency_hz=339.8 | rms=3351 | updated_at=1777958841.055816
- [2026-05-05 13:27:21] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777958841.5798032 | source=windows | frequency_hz=339.8 | rms=3351 | updated_at=1777958841.055816
- [2026-05-05 13:27:22] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777958842.0680556 | source=final | confidence=0.22 | frequency_hz=339.8 | rms=3351 | updated_at=1777958841.055816
- [2026-05-05 13:27:28] operator / voice_transcript_partial / voice: line
  meta: kind=partial | timestamp=1777958848.448307 | source=windows | frequency_hz=339.8 | rms=3351 | updated_at=1777958841.055816
- [2026-05-05 13:27:28] operator / voice_transcript_partial / voice: line the
  meta: kind=partial | timestamp=1777958848.652704 | source=windows | frequency_hz=339.8 | rms=3351 | updated_at=1777958841.055816
- [2026-05-05 13:27:29] operator / voice_transcript_final / voice: line the
  meta: kind=final | timestamp=1777958849.48373 | source=final | confidence=0.63 | frequency_hz=339.8 | rms=3351 | updated_at=1777958841.055816

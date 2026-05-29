# SMART SENTRY V3.5.3 Runtime Conversation Export

- Generated: 2026-05-05 01:19:22
- Entries: 367
- Roles: {'assistant': 6, 'system': 1, 'operator': 360}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 1, 'spoken_confirmation': 4, 'voice_transcript_partial': 292, 'voice_transcript_final': 62, 'voice_command': 6}
- Channels: {'text': 2, 'voice': 365}
- Latest operator request: its own name on the
- Latest assistant message: That does not match a known command. Please repeat.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-05 01:12:45] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 01:12:45] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-05 01:12:47] system / voice_status / voice: listening
  meta: kind=status | timestamp=1777914767.7893429 | source=windows
- [2026-05-05 01:12:48] assistant / spoken_confirmation / voice: Good to go. Tell me your first command when ready.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 01:12:55] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777914775.128367 | source=windows
- [2026-05-05 01:13:01] operator / voice_transcript_partial / voice: the dc
  meta: kind=partial | timestamp=1777914781.4459648 | source=windows
- [2026-05-05 01:13:01] operator / voice_transcript_partial / voice: the cd
  meta: kind=partial | timestamp=1777914781.6498508 | source=windows
- [2026-05-05 01:13:01] operator / voice_transcript_partial / voice: the same
  meta: kind=partial | timestamp=1777914781.852951 | source=windows
- [2026-05-05 01:13:02] operator / voice_transcript_final / voice: the same
  meta: kind=final | timestamp=1777914782.4841259 | source=final | confidence=0.01
- [2026-05-05 01:13:04] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777914784.9366603 | source=windows
- [2026-05-05 01:13:05] operator / voice_transcript_partial / voice: piece
  meta: kind=partial | timestamp=1777914785.1418114 | source=windows
- [2026-05-05 01:13:05] operator / voice_transcript_partial / voice: pcs
  meta: kind=partial | timestamp=1777914785.344727 | source=windows
- [2026-05-05 01:13:05] operator / voice_transcript_partial / voice: the season
  meta: kind=partial | timestamp=1777914785.561098 | source=windows
- [2026-05-05 01:13:05] operator / voice_transcript_partial / voice: pcs and the
  meta: kind=partial | timestamp=1777914785.7635486 | source=windows
- [2026-05-05 01:13:05] operator / voice_transcript_partial / voice: the season in the
  meta: kind=partial | timestamp=1777914785.9646897 | source=windows
- [2026-05-05 01:13:06] operator / voice_transcript_partial / voice: the season in the sea
  meta: kind=partial | timestamp=1777914786.1693802 | source=windows
- [2026-05-05 01:13:07] operator / voice_transcript_final / voice: the season in the sea
  meta: kind=final | timestamp=1777914787.1844356 | source=final | confidence=0.48
- [2026-05-05 01:13:07] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777914787.3851702 | source=windows
- [2026-05-05 01:13:07] operator / voice_transcript_partial / voice: use
  meta: kind=partial | timestamp=1777914787.587969 | source=windows
- [2026-05-05 01:13:07] operator / voice_transcript_partial / voice: in the people
  meta: kind=partial | timestamp=1777914787.7896302 | source=windows
- [2026-05-05 01:13:08] operator / voice_transcript_partial / voice: in its own
  meta: kind=partial | timestamp=1777914788.1965723 | source=windows
- [2026-05-05 01:13:08] operator / voice_transcript_final / voice: in its own
  meta: kind=final | timestamp=1777914788.8029058 | source=final | confidence=0.54
- [2026-05-05 01:13:16] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777914796.7386043 | source=windows
- [2026-05-05 01:13:17] operator / voice_transcript_partial / voice: ego
  meta: kind=partial | timestamp=1777914797.1470015 | source=windows
- [2026-05-05 01:13:17] operator / voice_transcript_partial / voice: ego eight
  meta: kind=partial | timestamp=1777914797.553796 | source=windows
- [2026-05-05 01:13:17] operator / voice_transcript_partial / voice: ego a close
  meta: kind=partial | timestamp=1777914797.7562408 | source=windows
- [2026-05-05 01:13:18] operator / voice_transcript_partial / voice: ego a close the
  meta: kind=partial | timestamp=1777914798.1622121 | source=windows
- [2026-05-05 01:13:18] operator / voice_transcript_partial / voice: ego a close the gap
  meta: kind=partial | timestamp=1777914798.5683458 | source=windows
- [2026-05-05 01:13:18] operator / voice_transcript_partial / voice: ego a close the nba
  meta: kind=partial | timestamp=1777914798.77135 | source=windows
- [2026-05-05 01:13:18] operator / voice_transcript_partial / voice: ego a close the eighty eight
  meta: kind=partial | timestamp=1777914798.9728792 | source=windows
- [2026-05-05 01:13:19] operator / voice_transcript_partial / voice: ego egos feed the people
  meta: kind=partial | timestamp=1777914799.3792076 | source=windows
- [2026-05-05 01:13:19] operator / voice_transcript_partial / voice: ego a close the nba to hopes
  meta: kind=partial | timestamp=1777914799.581754 | source=windows
- [2026-05-05 01:13:20] operator / voice_transcript_final / voice: ego a close the nba to hopes
  meta: kind=final | timestamp=1777914800.3960304 | source=final | confidence=0.44
- [2026-05-05 01:13:22] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777914802.4328902 | source=windows
- [2026-05-05 01:13:23] operator / voice_transcript_partial / voice: the move
  meta: kind=partial | timestamp=1777914803.0424366 | source=windows
- [2026-05-05 01:13:23] operator / voice_transcript_partial / voice: he moves
  meta: kind=partial | timestamp=1777914803.248999 | source=windows
- [2026-05-05 01:13:23] operator / voice_transcript_partial / voice: the scene
  meta: kind=partial | timestamp=1777914803.4522963 | source=windows
- [2026-05-05 01:13:24] operator / voice_transcript_partial / voice: he moves in los
  meta: kind=partial | timestamp=1777914804.273349 | source=windows
- [2026-05-05 01:13:25] operator / voice_transcript_final / voice: he moves in los
  meta: kind=final | timestamp=1777914805.0934858 | source=final | confidence=0.67
- [2026-05-05 01:13:27] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777914807.5366144 | source=windows
- [2026-05-05 01:13:27] operator / voice_transcript_partial / voice: yes
  meta: kind=partial | timestamp=1777914807.5371172 | source=windows
- [2026-05-05 01:13:27] operator / voice_transcript_partial / voice: whats
  meta: kind=partial | timestamp=1777914807.7428687 | source=windows
- [2026-05-05 01:13:28] operator / voice_transcript_final / voice: its
  meta: kind=final | timestamp=1777914808.5635083 | source=final | confidence=0.85
- [2026-05-05 01:13:30] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777914810.187201 | source=windows
- [2026-05-05 01:13:30] operator / voice_transcript_partial / voice: fifth in the
  meta: kind=partial | timestamp=1777914810.3931935 | source=windows
- [2026-05-05 01:13:30] operator / voice_transcript_partial / voice: been able
  meta: kind=partial | timestamp=1777914810.5946634 | source=windows
- [2026-05-05 01:13:30] operator / voice_transcript_partial / voice: enabled this
  meta: kind=partial | timestamp=1777914810.8022635 | source=windows
- [2026-05-05 01:13:31] operator / voice_transcript_partial / voice: enable the smart
  meta: kind=partial | timestamp=1777914811.003813 | source=windows
- [2026-05-05 01:13:31] operator / voice_transcript_partial / voice: enabled the smarts
  meta: kind=partial | timestamp=1777914811.4081829 | source=windows
- [2026-05-05 01:13:31] operator / voice_transcript_partial / voice: enabled the smarts to
  meta: kind=partial | timestamp=1777914811.6138353 | source=windows
- [2026-05-05 01:13:31] operator / voice_transcript_partial / voice: enable the smart sentry
  meta: kind=partial | timestamp=1777914811.818952 | source=windows
- [2026-05-05 01:13:32] operator / voice_transcript_final / voice: enable smart sentry
  meta: kind=final | timestamp=1777914812.0252612 | source=final | confidence=0.81
- [2026-05-05 01:13:32] operator / voice_command / voice: enable smart sentry
  meta: normalized=True
- [2026-05-05 01:13:32] assistant / spoken_confirmation / voice: Enabling Smart Sentry now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 01:13:34] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777914814.4692998 | source=windows
- [2026-05-05 01:13:34] operator / voice_transcript_partial / voice: scene
  meta: kind=partial | timestamp=1777914814.6773038 | source=windows
- [2026-05-05 01:13:35] operator / voice_transcript_final / voice: scene
  meta: kind=final | timestamp=1777914815.9076755 | source=final | confidence=0.73
- [2026-05-05 01:13:35] operator / voice_command / voice: scene
  meta: normalized=True
- [2026-05-05 01:13:36] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 01:13:37] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1777914817.7264874 | source=windows
- [2026-05-05 01:13:38] operator / voice_transcript_final / voice: is
  meta: kind=final | timestamp=1777914818.5561254 | source=final | confidence=0.55
- [2026-05-05 01:13:38] operator / voice_command / voice: is
  meta: normalized=True
- [2026-05-05 01:13:39] assistant / spoken_confirmation / voice: That does not match a known command. Please repeat.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 01:13:48] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777914828.1351144 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:48] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777914828.3393333 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:49] operator / voice_transcript_partial / voice: in its
  meta: kind=partial | timestamp=1777914829.1501212 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:49] operator / voice_transcript_partial / voice: in these
  meta: kind=partial | timestamp=1777914829.3536167 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:49] operator / voice_transcript_partial / voice: in its three
  meta: kind=partial | timestamp=1777914829.5561712 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:49] operator / voice_transcript_partial / voice: in its lead the
  meta: kind=partial | timestamp=1777914829.961317 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:50] operator / voice_transcript_partial / voice: in its lead the speed
  meta: kind=partial | timestamp=1777914830.1710684 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:50] operator / voice_transcript_partial / voice: in its only be seen as
  meta: kind=partial | timestamp=1777914830.3675282 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:50] operator / voice_transcript_partial / voice: in its only be seen as a
  meta: kind=partial | timestamp=1777914830.5696325 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:51] operator / voice_transcript_partial / voice: in its only be seen this is
  meta: kind=partial | timestamp=1777914831.381558 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:51] operator / voice_transcript_partial / voice: in its only be seen this is done
  meta: kind=partial | timestamp=1777914831.7910488 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:52] operator / voice_transcript_partial / voice: in its only be seen this is what
  meta: kind=partial | timestamp=1777914832.198995 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:52] operator / voice_transcript_partial / voice: in its only be seen this is what gives
  meta: kind=partial | timestamp=1777914832.4040759 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:52] operator / voice_transcript_partial / voice: in its only be seen this is what gives you
  meta: kind=partial | timestamp=1777914832.811757 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:53] operator / voice_transcript_final / voice: in its only be seen this is what gives you
  meta: kind=final | timestamp=1777914833.6260395 | source=final | confidence=0.27 | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:56] operator / voice_transcript_partial / voice: an
  meta: kind=partial | timestamp=1777914836.0737545 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:56] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777914836.4791636 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:56] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777914836.8870375 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:57] operator / voice_transcript_partial / voice: a lot in
  meta: kind=partial | timestamp=1777914837.0905623 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:57] operator / voice_transcript_partial / voice: one in the
  meta: kind=partial | timestamp=1777914837.908347 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:58] operator / voice_transcript_final / voice: one in the
  meta: kind=final | timestamp=1777914838.519573 | source=final | confidence=0.47 | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:59] operator / voice_transcript_partial / voice: ie
  meta: kind=partial | timestamp=1777914839.3376415 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:59] operator / voice_transcript_partial / voice: eileen
  meta: kind=partial | timestamp=1777914839.338645 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:59] operator / voice_transcript_partial / voice: name of
  meta: kind=partial | timestamp=1777914839.5363944 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:59] operator / voice_transcript_partial / voice: name of the
  meta: kind=partial | timestamp=1777914839.7389655 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:13:59] operator / voice_transcript_partial / voice: body of people
  meta: kind=partial | timestamp=1777914839.9441507 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:14:00] operator / voice_transcript_partial / voice: way of king of the
  meta: kind=partial | timestamp=1777914840.3524437 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:14:00] operator / voice_transcript_partial / voice: body of people in
  meta: kind=partial | timestamp=1777914840.5542808 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:14:01] operator / voice_transcript_final / voice: body of people in
  meta: kind=final | timestamp=1777914841.5707917 | source=final | confidence=0.06 | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:14:02] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777914842.3854413 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:14:03] operator / voice_transcript_partial / voice: the movie
  meta: kind=partial | timestamp=1777914843.0015182 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:14:04] operator / voice_transcript_final / voice: the movie
  meta: kind=final | timestamp=1777914844.0249307 | source=final | confidence=0.08 | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:14:06] operator / voice_transcript_partial / voice: on
  meta: kind=partial | timestamp=1777914846.4725692 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:14:07] operator / voice_transcript_final / voice: on
  meta: kind=final | timestamp=1777914847.4917974 | source=final | confidence=0.67 | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:14:07] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777914847.8967133 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:14:08] operator / voice_transcript_partial / voice: monday
  meta: kind=partial | timestamp=1777914848.306497 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:14:08] operator / voice_transcript_partial / voice: the idea of
  meta: kind=partial | timestamp=1777914848.715798 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:14:08] operator / voice_transcript_partial / voice: wonderful
  meta: kind=partial | timestamp=1777914848.916596 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:14:09] operator / voice_transcript_partial / voice: wonderful and
  meta: kind=partial | timestamp=1777914849.119741 | source=windows | frequency_hz=386.7 | rms=136 | updated_at=1777914818.8232489
- [2026-05-05 01:14:17] operator / voice_transcript_partial / voice: my
  meta: kind=partial | timestamp=1777914857.3109982 | source=windows | frequency_hz=121.1 | rms=234 | updated_at=1777914849.763673
- [2026-05-05 01:14:17] operator / voice_transcript_partial / voice: mine
  meta: kind=partial | timestamp=1777914857.724753 | source=windows | frequency_hz=121.1 | rms=234 | updated_at=1777914849.763673
- [2026-05-05 01:14:18] operator / voice_transcript_partial / voice: mining one of
  meta: kind=partial | timestamp=1777914858.541538 | source=windows | frequency_hz=121.1 | rms=234 | updated_at=1777914849.763673
- [2026-05-05 01:14:18] operator / voice_transcript_partial / voice: mining
  meta: kind=partial | timestamp=1777914858.7401342 | source=windows | frequency_hz=121.1 | rms=234 | updated_at=1777914849.763673
- [2026-05-05 01:14:19] operator / voice_transcript_partial / voice: mining one of the
  meta: kind=partial | timestamp=1777914859.3574314 | source=windows | frequency_hz=121.1 | rms=234 | updated_at=1777914849.763673
- [2026-05-05 01:14:19] operator / voice_transcript_final / voice: mining one of the
  meta: kind=final | timestamp=1777914859.981178 | source=final | confidence=0.5 | frequency_hz=121.1 | rms=234 | updated_at=1777914849.763673
- [2026-05-05 01:14:28] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777914868.2326937 | source=windows | frequency_hz=250.0 | rms=158 | updated_at=1777914861.3915136
- [2026-05-05 01:14:28] operator / voice_transcript_partial / voice: only
  meta: kind=partial | timestamp=1777914868.2326937 | source=windows | frequency_hz=250.0 | rms=158 | updated_at=1777914861.3915136
- [2026-05-05 01:14:29] operator / voice_transcript_final / voice: only
  meta: kind=final | timestamp=1777914869.2679677 | source=final | confidence=0.69 | frequency_hz=250.0 | rms=158 | updated_at=1777914861.3915136
- [2026-05-05 01:14:30] operator / voice_transcript_partial / voice: his
  meta: kind=partial | timestamp=1777914870.9098654 | source=windows | frequency_hz=250.0 | rms=158 | updated_at=1777914861.3915136
- [2026-05-05 01:14:31] operator / voice_transcript_final / voice: his
  meta: kind=final | timestamp=1777914871.7258856 | source=final | confidence=0.57 | frequency_hz=250.0 | rms=158 | updated_at=1777914861.3915136
- [2026-05-05 01:14:37] operator / voice_transcript_partial / voice: own
  meta: kind=partial | timestamp=1777914877.6586506 | source=windows | frequency_hz=250.0 | rms=158 | updated_at=1777914861.3915136
- [2026-05-05 01:14:57] operator / voice_transcript_partial / voice: own and
  meta: kind=partial | timestamp=1777914897.6863143 | source=windows | frequency_hz=250.0 | rms=158 | updated_at=1777914861.3915136
- [2026-05-05 01:14:57] operator / voice_transcript_partial / voice: own one
  meta: kind=partial | timestamp=1777914897.8913646 | source=windows | frequency_hz=250.0 | rms=158 | updated_at=1777914861.3915136
- [2026-05-05 01:14:58] operator / voice_transcript_partial / voice: was the
  meta: kind=partial | timestamp=1777914898.1097405 | source=windows | frequency_hz=250.0 | rms=158 | updated_at=1777914861.3915136
- [2026-05-05 01:14:58] operator / voice_transcript_partial / voice: own money into some
  meta: kind=partial | timestamp=1777914898.5163574 | source=windows | frequency_hz=367.2 | rms=243 | updated_at=1777914898.2523096
- [2026-05-05 01:14:58] operator / voice_transcript_partial / voice: own one thousand
  meta: kind=partial | timestamp=1777914898.735376 | source=windows | frequency_hz=367.2 | rms=243 | updated_at=1777914898.2523096
- [2026-05-05 01:14:58] operator / voice_transcript_partial / voice: own interests and those
  meta: kind=partial | timestamp=1777914898.93892 | source=windows | frequency_hz=367.2 | rms=243 | updated_at=1777914898.2523096
- [2026-05-05 01:14:59] operator / voice_transcript_partial / voice: own one thousand one
  meta: kind=partial | timestamp=1777914899.3487043 | source=windows | frequency_hz=367.2 | rms=243 | updated_at=1777914898.2523096
- [2026-05-05 01:15:00] operator / voice_transcript_final / voice: own 1001
  meta: kind=final | timestamp=1777914900.3793972 | source=final | confidence=0.08 | frequency_hz=367.2 | rms=243 | updated_at=1777914898.2523096
- [2026-05-05 01:15:01] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777914901.8045564 | source=windows | frequency_hz=367.2 | rms=243 | updated_at=1777914898.2523096
- [2026-05-05 01:15:02] operator / voice_transcript_partial / voice: and one
  meta: kind=partial | timestamp=1777914902.2137675 | source=windows | frequency_hz=367.2 | rms=243 | updated_at=1777914898.2523096
- [2026-05-05 01:15:03] operator / voice_transcript_final / voice: and one
  meta: kind=final | timestamp=1777914903.0362294 | source=final | confidence=0.53 | frequency_hz=367.2 | rms=243 | updated_at=1777914898.2523096
- [2026-05-05 01:15:03] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777914903.646097 | source=windows | frequency_hz=367.2 | rms=243 | updated_at=1777914898.2523096
- [2026-05-05 01:15:04] operator / voice_transcript_partial / voice: and see how
  meta: kind=partial | timestamp=1777914904.051283 | source=windows | frequency_hz=367.2 | rms=243 | updated_at=1777914898.2523096
- [2026-05-05 01:15:04] operator / voice_transcript_partial / voice: and two of the
  meta: kind=partial | timestamp=1777914904.2563503 | source=windows | frequency_hz=367.2 | rms=243 | updated_at=1777914898.2523096
- [2026-05-05 01:15:06] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777914906.240766 | source=windows
- [2026-05-05 01:15:06] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777914906.45195 | source=windows
- [2026-05-05 01:15:07] operator / voice_transcript_partial / voice: in his
  meta: kind=partial | timestamp=1777914907.0650434 | source=windows
- [2026-05-05 01:15:07] operator / voice_transcript_final / voice: in his
  meta: kind=final | timestamp=1777914907.8912525 | source=final | confidence=0.17
- [2026-05-05 01:15:08] operator / voice_transcript_partial / voice: eyes
  meta: kind=partial | timestamp=1777914908.9192407 | source=windows
- [2026-05-05 01:15:12] operator / voice_transcript_partial / voice: house
  meta: kind=partial | timestamp=1777914912.6190405 | source=windows
- [2026-05-05 01:15:13] operator / voice_transcript_final / voice: house
  meta: kind=final | timestamp=1777914913.6558487 | source=final | confidence=0.51
- [2026-05-05 01:15:15] operator / voice_transcript_partial / voice: will
  meta: kind=partial | timestamp=1777914915.4858074 | source=windows
- [2026-05-05 01:15:15] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1777914915.6890378 | source=windows
- [2026-05-05 01:15:15] operator / voice_transcript_partial / voice: while the
  meta: kind=partial | timestamp=1777914915.8916354 | source=windows
- [2026-05-05 01:15:16] operator / voice_transcript_partial / voice: while that of
  meta: kind=partial | timestamp=1777914916.709874 | source=windows
- [2026-05-05 01:15:17] operator / voice_transcript_final / voice: while that of
  meta: kind=final | timestamp=1777914917.942953 | source=final | confidence=0.34
- [2026-05-05 01:15:19] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777914919.1624198 | source=windows
- [2026-05-05 01:15:19] operator / voice_transcript_partial / voice: small
  meta: kind=partial | timestamp=1777914919.364984 | source=windows
- [2026-05-05 01:15:19] operator / voice_transcript_partial / voice: story
  meta: kind=partial | timestamp=1777914919.5683007 | source=windows
- [2026-05-05 01:15:19] operator / voice_transcript_partial / voice: :-)
  meta: kind=partial | timestamp=1777914919.770409 | source=windows
- [2026-05-05 01:15:20] operator / voice_transcript_partial / voice: :-) what
  meta: kind=partial | timestamp=1777914920.796676 | source=windows
- [2026-05-05 01:15:21] operator / voice_transcript_partial / voice: :-) the
  meta: kind=partial | timestamp=1777914921.00319 | source=windows
- [2026-05-05 01:15:21] operator / voice_transcript_partial / voice: :-) the things
  meta: kind=partial | timestamp=1777914921.6178071 | source=windows
- [2026-05-05 01:15:21] operator / voice_transcript_partial / voice: :-) the inquiry
  meta: kind=partial | timestamp=1777914921.8182275 | source=windows
- [2026-05-05 01:15:22] operator / voice_transcript_partial / voice: :-) lighting by e. coli
  meta: kind=partial | timestamp=1777914922.2351837 | source=windows
- [2026-05-05 01:15:23] operator / voice_transcript_final / voice: lighting by e coli
  meta: kind=final | timestamp=1777914923.257945 | source=final | confidence=0.06
- [2026-05-05 01:15:26] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777914926.3163326 | source=windows
- [2026-05-05 01:15:26] operator / voice_transcript_partial / voice: il
  meta: kind=partial | timestamp=1777914926.7243457 | source=windows
- [2026-05-05 01:15:26] operator / voice_transcript_partial / voice: elian
  meta: kind=partial | timestamp=1777914926.9298823 | source=windows
- [2026-05-05 01:15:27] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 01:15:27] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777914927.337919 | source=final | confidence=0.82
- [2026-05-05 01:15:28] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777914928.4155743 | source=windows
- [2026-05-05 01:15:28] operator / voice_transcript_partial / voice: eighty
  meta: kind=partial | timestamp=1777914928.5617514 | source=windows
- [2026-05-05 01:15:28] operator / voice_transcript_partial / voice: pdt at
  meta: kind=partial | timestamp=1777914928.7694051 | source=windows
- [2026-05-05 01:15:29] operator / voice_transcript_partial / voice: eighty and
  meta: kind=partial | timestamp=1777914929.1761532 | source=windows
- [2026-05-05 01:15:29] operator / voice_transcript_partial / voice: pdt and the
  meta: kind=partial | timestamp=1777914929.380021 | source=windows
- [2026-05-05 01:15:29] operator / voice_transcript_partial / voice: tv and movies
  meta: kind=partial | timestamp=1777914929.5841877 | source=windows
- [2026-05-05 01:15:30] operator / voice_transcript_final / voice: tv and movies
  meta: kind=final | timestamp=1777914930.4010956 | source=final | confidence=0.07
- [2026-05-05 01:15:30] operator / voice_command / voice: tv and movies
  meta: normalized=True
- [2026-05-05 01:15:38] operator / voice_transcript_partial / voice: are
  meta: kind=partial | timestamp=1777914938.566261 | source=windows
- [2026-05-05 01:15:40] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777914940.3970568 | source=windows
- [2026-05-05 01:15:40] operator / voice_transcript_partial / voice: these
  meta: kind=partial | timestamp=1777914940.6028779 | source=windows
- [2026-05-05 01:15:41] operator / voice_transcript_partial / voice: these days
  meta: kind=partial | timestamp=1777914941.2145932 | source=windows
- [2026-05-05 01:15:41] operator / voice_transcript_final / voice: these days
  meta: kind=final | timestamp=1777914941.8310938 | source=final | confidence=0.57
- [2026-05-05 01:15:42] operator / voice_command / voice: these days
  meta: normalized=True
- [2026-05-05 01:15:43] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777914943.2557707 | source=windows
- [2026-05-05 01:15:43] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777914943.4586432 | source=windows
- [2026-05-05 01:15:43] operator / voice_transcript_partial / voice: he has
  meta: kind=partial | timestamp=1777914943.6615524 | source=windows
- [2026-05-05 01:15:43] operator / voice_transcript_partial / voice: he has any
  meta: kind=partial | timestamp=1777914943.8663049 | source=windows
- [2026-05-05 01:15:44] operator / voice_transcript_partial / voice: he has an
  meta: kind=partial | timestamp=1777914944.06755 | source=windows
- [2026-05-05 01:15:44] operator / voice_transcript_partial / voice: he has
  meta: kind=partial | timestamp=1777914944.8801172 | source=windows
- [2026-05-05 01:15:45] operator / voice_transcript_partial / voice: they have
  meta: kind=partial | timestamp=1777914945.081694 | source=windows
- [2026-05-05 01:15:45] operator / voice_transcript_partial / voice: he has online
  meta: kind=partial | timestamp=1777914945.286589 | source=windows
- [2026-05-05 01:15:45] operator / voice_transcript_partial / voice: the day when
  meta: kind=partial | timestamp=1777914945.6957152 | source=windows
- [2026-05-05 01:15:45] operator / voice_transcript_partial / voice: he has
  meta: kind=partial | timestamp=1777914945.9009583 | source=windows
- [2026-05-05 01:15:46] operator / voice_transcript_partial / voice: he has an
  meta: kind=partial | timestamp=1777914946.1096199 | source=windows
- [2026-05-05 01:15:46] operator / voice_transcript_final / voice: he has an
  meta: kind=final | timestamp=1777914946.930559 | source=final | confidence=0.03
- [2026-05-05 01:15:50] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777914950.408575 | source=windows
- [2026-05-05 01:15:50] operator / voice_transcript_partial / voice: use
  meta: kind=partial | timestamp=1777914950.820028 | source=windows
- [2026-05-05 01:15:51] operator / voice_transcript_partial / voice: abc
  meta: kind=partial | timestamp=1777914951.0250878 | source=windows
- [2026-05-05 01:15:51] operator / voice_transcript_partial / voice: pc tag
  meta: kind=partial | timestamp=1777914951.4365075 | source=windows
- [2026-05-05 01:15:51] operator / voice_transcript_partial / voice: pc tag a
  meta: kind=partial | timestamp=1777914951.6415517 | source=windows
- [2026-05-05 01:15:52] operator / voice_transcript_partial / voice: pc tag of
  meta: kind=partial | timestamp=1777914952.0508945 | source=windows
- [2026-05-05 01:15:52] operator / voice_transcript_final / voice: pc tag of
  meta: kind=final | timestamp=1777914952.6632423 | source=final | confidence=0.36
- [2026-05-05 01:15:56] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777914956.34703 | source=windows
- [2026-05-05 01:15:56] operator / voice_transcript_partial / voice: an
  meta: kind=partial | timestamp=1777914956.557585 | source=windows
- [2026-05-05 01:15:56] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777914956.9590828 | source=windows
- [2026-05-05 01:16:01] operator / voice_transcript_partial / voice: an
  meta: kind=partial | timestamp=1777914961.871444 | source=windows
- [2026-05-05 01:16:02] operator / voice_transcript_partial / voice: an issue
  meta: kind=partial | timestamp=1777914962.279889 | source=windows
- [2026-05-05 01:16:02] operator / voice_transcript_partial / voice: an scenes
  meta: kind=partial | timestamp=1777914962.4846904 | source=windows
- [2026-05-05 01:16:02] operator / voice_transcript_partial / voice: an issue since
  meta: kind=partial | timestamp=1777914962.8975666 | source=windows
- [2026-05-05 01:16:03] operator / voice_transcript_partial / voice: an scene sees
  meta: kind=partial | timestamp=1777914963.1048205 | source=windows
- [2026-05-05 01:16:03] operator / voice_transcript_partial / voice: an scene sees as
  meta: kind=partial | timestamp=1777914963.308697 | source=windows
- [2026-05-05 01:16:03] operator / voice_transcript_partial / voice: an scene sees this as
  meta: kind=partial | timestamp=1777914963.5161512 | source=windows
- [2026-05-05 01:16:04] operator / voice_transcript_partial / voice: an scene sees these scenes
  meta: kind=partial | timestamp=1777914964.1277633 | source=windows
- [2026-05-05 01:16:04] operator / voice_transcript_final / voice: an scene sees these scenes
  meta: kind=final | timestamp=1777914964.7419899 | source=final | confidence=0.7
- [2026-05-05 01:16:05] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777914965.1531875 | source=windows
- [2026-05-05 01:16:05] operator / voice_transcript_partial / voice: seem
  meta: kind=partial | timestamp=1777914965.5633237 | source=windows
- [2026-05-05 01:16:05] operator / voice_transcript_partial / voice: seems
  meta: kind=partial | timestamp=1777914965.7676058 | source=windows
- [2026-05-05 01:16:05] operator / voice_transcript_partial / voice: seasons
  meta: kind=partial | timestamp=1777914965.9734368 | source=windows
- [2026-05-05 01:16:06] operator / voice_transcript_final / voice: seasons
  meta: kind=final | timestamp=1777914966.585049 | source=final | confidence=0.57
- [2026-05-05 01:16:07] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777914967.3995633 | source=windows
- [2026-05-05 01:16:08] operator / voice_transcript_partial / voice: since the
  meta: kind=partial | timestamp=1777914968.2136621 | source=windows
- [2026-05-05 01:16:08] operator / voice_transcript_partial / voice: as to
  meta: kind=partial | timestamp=1777914968.417894 | source=windows
- [2026-05-05 01:16:08] operator / voice_transcript_partial / voice: as he
  meta: kind=partial | timestamp=1777914968.8287466 | source=windows
- [2026-05-05 01:16:09] operator / voice_transcript_final / voice: as he
  meta: kind=final | timestamp=1777914969.4443393 | source=final | confidence=0.27
- [2026-05-05 01:16:10] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777914970.2611887 | source=windows
- [2026-05-05 01:16:10] operator / voice_transcript_partial / voice: being
  meta: kind=partial | timestamp=1777914970.6770194 | source=windows
- [2026-05-05 01:16:11] operator / voice_transcript_final / voice: being
  meta: kind=final | timestamp=1777914971.5049074 | source=final | confidence=0.64
- [2026-05-05 01:16:13] operator / voice_transcript_partial / voice: an
  meta: kind=partial | timestamp=1777914973.738132 | source=windows
- [2026-05-05 01:16:17] operator / voice_transcript_partial / voice: seen as
  meta: kind=partial | timestamp=1777914977.6471324 | source=windows
- [2026-05-05 01:16:18] operator / voice_transcript_partial / voice: seen as an
  meta: kind=partial | timestamp=1777914978.2592282 | source=windows
- [2026-05-05 01:16:18] operator / voice_transcript_final / voice: seen as an
  meta: kind=final | timestamp=1777914978.8764439 | source=final | confidence=0.32
- [2026-05-05 01:16:19] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777914979.6899896 | source=windows
- [2026-05-05 01:16:19] operator / voice_transcript_partial / voice: same
  meta: kind=partial | timestamp=1777914979.897328 | source=windows
- [2026-05-05 01:16:20] operator / voice_transcript_final / voice: aging
  meta: kind=final | timestamp=1777914980.3102493 | source=final | confidence=0.58
- [2026-05-05 01:16:21] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777914981.7452672 | source=windows
- [2026-05-05 01:16:22] operator / voice_transcript_final / voice: and
  meta: kind=final | timestamp=1777914982.765316 | source=final | confidence=0.73
- [2026-05-05 01:16:22] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777914982.7658935 | source=windows
- [2026-05-05 01:16:23] operator / voice_transcript_partial / voice: the two
  meta: kind=partial | timestamp=1777914983.173989 | source=windows
- [2026-05-05 01:16:24] operator / voice_transcript_final / voice: the two
  meta: kind=final | timestamp=1777914984.2318988 | source=final | confidence=0.49
- [2026-05-05 01:16:26] operator / voice_transcript_partial / voice: new
  meta: kind=partial | timestamp=1777914986.649153 | source=windows
- [2026-05-05 01:16:26] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777914986.853934 | source=windows
- [2026-05-05 01:16:27] operator / voice_transcript_final / voice: and
  meta: kind=final | timestamp=1777914987.679302 | source=final | confidence=0.31
- [2026-05-05 01:16:31] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777914991.7684293 | source=windows
- [2026-05-05 01:16:32] operator / voice_transcript_final / voice: he
  meta: kind=final | timestamp=1777914992.789907 | source=final | confidence=0.84
- [2026-05-05 01:16:36] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777914996.0667725 | source=windows
- [2026-05-05 01:16:37] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1777914997.5039616 | source=windows
- [2026-05-05 01:16:38] operator / voice_transcript_final / voice: is
  meta: kind=final | timestamp=1777914998.3194373 | source=final | confidence=0.24
- [2026-05-05 01:16:39] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777914999.7569635 | source=windows
- [2026-05-05 01:16:40] operator / voice_transcript_final / voice: as
  meta: kind=final | timestamp=1777915000.5763986 | source=final | confidence=0.69
- [2026-05-05 01:16:42] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777915002.012684 | source=windows
- [2026-05-05 01:16:42] operator / voice_transcript_final / voice: he
  meta: kind=final | timestamp=1777915002.6264236 | source=final | confidence=0.79
- [2026-05-05 01:16:49] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777915009.574516 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:16:50] operator / voice_transcript_final / voice: and
  meta: kind=final | timestamp=1777915010.3941538 | source=final | confidence=0.63 | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:16:58] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777915018.7859044 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:16:59] operator / voice_transcript_partial / voice: he is
  meta: kind=partial | timestamp=1777915019.3997586 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:16:59] operator / voice_transcript_partial / voice: the sea
  meta: kind=partial | timestamp=1777915019.6062791 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:00] operator / voice_transcript_partial / voice: the scene
  meta: kind=partial | timestamp=1777915020.0143726 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:00] operator / voice_transcript_final / voice: the scene
  meta: kind=final | timestamp=1777915020.4223895 | source=final | confidence=0.54 | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:04] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777915024.9278538 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:05] operator / voice_transcript_partial / voice: of the
  meta: kind=partial | timestamp=1777915025.1333709 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:05] operator / voice_transcript_partial / voice: that we
  meta: kind=partial | timestamp=1777915025.3373835 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:05] operator / voice_transcript_partial / voice: between you and
  meta: kind=partial | timestamp=1777915025.5421999 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:06] operator / voice_transcript_partial / voice: between the ie:
  meta: kind=partial | timestamp=1777915026.1591995 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:06] operator / voice_transcript_partial / voice: between the ie: a
  meta: kind=partial | timestamp=1777915026.9767463 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:07] operator / voice_transcript_partial / voice: between you and loan in the
  meta: kind=partial | timestamp=1777915027.1818051 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:07] operator / voice_transcript_partial / voice: between you and loan in their
  meta: kind=partial | timestamp=1777915027.3848362 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:07] operator / voice_transcript_partial / voice: between you and loan in the ravens
  meta: kind=partial | timestamp=1777915027.588316 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:07] operator / voice_transcript_partial / voice: between you and loan in the ravens in
  meta: kind=partial | timestamp=1777915027.7949054 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:08] operator / voice_transcript_partial / voice: between you and loan in the ravens in the
  meta: kind=partial | timestamp=1777915028.4101763 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:08] operator / voice_transcript_final / voice: between you and loan in the ravens in the
  meta: kind=final | timestamp=1777915028.821082 | source=final | confidence=0.37 | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:09] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777915029.4321449 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:09] operator / voice_transcript_partial / voice: lungs
  meta: kind=partial | timestamp=1777915029.631973 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:09] operator / voice_transcript_partial / voice: lungs to
  meta: kind=partial | timestamp=1777915029.8343544 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:10] operator / voice_transcript_partial / voice: lungs as
  meta: kind=partial | timestamp=1777915030.2382705 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:10] operator / voice_transcript_partial / voice: long as the
  meta: kind=partial | timestamp=1777915030.4425416 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:10] operator / voice_transcript_partial / voice: lungs as in the
  meta: kind=partial | timestamp=1777915030.6460469 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:10] operator / voice_transcript_partial / voice: lungs as including the
  meta: kind=partial | timestamp=1777915030.847371 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:11] operator / voice_transcript_partial / voice: long as the man is
  meta: kind=partial | timestamp=1777915031.051979 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:11] operator / voice_transcript_partial / voice: long as the man is any
  meta: kind=partial | timestamp=1777915031.4626727 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:11] operator / voice_transcript_partial / voice: long as the man is a need
  meta: kind=partial | timestamp=1777915031.6751862 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:11] operator / voice_transcript_partial / voice: long as the man is a need on
  meta: kind=partial | timestamp=1777915031.8703296 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:12] operator / voice_transcript_partial / voice: long as the man is a need and
  meta: kind=partial | timestamp=1777915032.0748923 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:12] operator / voice_transcript_final / voice: long as the man is a need and
  meta: kind=final | timestamp=1777915032.6920874 | source=final | confidence=0.39 | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:14] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777915034.937234 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:15] operator / voice_transcript_partial / voice: eight to
  meta: kind=partial | timestamp=1777915035.141455 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:15] operator / voice_transcript_partial / voice: a student at
  meta: kind=partial | timestamp=1777915035.5611918 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:15] operator / voice_transcript_partial / voice: eighteen and
  meta: kind=partial | timestamp=1777915035.9691393 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:16] operator / voice_transcript_partial / voice: eighteen and then
  meta: kind=partial | timestamp=1777915036.1723046 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:16] operator / voice_transcript_partial / voice: eighteen and then the
  meta: kind=partial | timestamp=1777915036.3771877 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:16] operator / voice_transcript_partial / voice: eighteen and then the man
  meta: kind=partial | timestamp=1777915036.9914596 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:17] operator / voice_transcript_partial / voice: eighteen and then the american
  meta: kind=partial | timestamp=1777915037.4072957 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:17] operator / voice_transcript_partial / voice: eighteen and then the manhattan to
  meta: kind=partial | timestamp=1777915037.8121593 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:18] operator / voice_transcript_partial / voice: eighteen and then the american city
  meta: kind=partial | timestamp=1777915038.2203588 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:18] operator / voice_transcript_partial / voice: eighteen and then the american season
  meta: kind=partial | timestamp=1777915038.643537 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:19] operator / voice_transcript_final / voice: 18 and then the american season
  meta: kind=final | timestamp=1777915039.2621632 | source=final | confidence=0.3 | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:20] operator / voice_transcript_partial / voice: see
  meta: kind=partial | timestamp=1777915040.104901 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:20] operator / voice_transcript_partial / voice: see the
  meta: kind=partial | timestamp=1777915040.5148156 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:20] operator / voice_transcript_partial / voice: seasons
  meta: kind=partial | timestamp=1777915040.7177913 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:20] operator / voice_transcript_partial / voice: see these
  meta: kind=partial | timestamp=1777915040.924926 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:21] operator / voice_transcript_final / voice: see these
  meta: kind=final | timestamp=1777915041.3339846 | source=final | confidence=0.49 | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:24] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777915044.1892369 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:24] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777915044.611456 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:24] operator / voice_transcript_partial / voice: in the
  meta: kind=partial | timestamp=1777915044.816754 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:25] operator / voice_transcript_final / voice: in the
  meta: kind=final | timestamp=1777915045.4290738 | source=final | confidence=0.3 | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:27] operator / voice_transcript_partial / voice: house
  meta: kind=partial | timestamp=1777915047.269193 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:27] operator / voice_transcript_partial / voice: last
  meta: kind=partial | timestamp=1777915047.4727807 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:27] operator / voice_transcript_partial / voice: last few
  meta: kind=partial | timestamp=1777915047.6775634 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:28] operator / voice_transcript_partial / voice: house and
  meta: kind=partial | timestamp=1777915048.0877364 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:28] operator / voice_transcript_final / voice: house and
  meta: kind=final | timestamp=1777915048.5016053 | source=final | confidence=0.28 | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:30] operator / voice_transcript_partial / voice: its
  meta: kind=partial | timestamp=1777915050.5364454 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:30] operator / voice_transcript_partial / voice: see
  meta: kind=partial | timestamp=1777915050.7393203 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:30] operator / voice_transcript_partial / voice: seen
  meta: kind=partial | timestamp=1777915050.940549 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:31] operator / voice_transcript_partial / voice: seen since
  meta: kind=partial | timestamp=1777915051.7559159 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:32] operator / voice_transcript_final / voice: seen since
  meta: kind=final | timestamp=1777915052.370838 | source=final | confidence=0.48 | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:33] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777915053.7978852 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:34] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777915054.2067418 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:34] operator / voice_transcript_partial / voice: one nine
  meta: kind=partial | timestamp=1777915054.4108188 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:34] operator / voice_transcript_partial / voice: one ninety
  meta: kind=partial | timestamp=1777915054.616378 | source=windows | frequency_hz=343.8 | rms=122 | updated_at=1777915009.154517
- [2026-05-05 01:17:40] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777915060.3202891 | source=windows
- [2026-05-05 01:17:40] operator / voice_transcript_partial / voice: we'll
  meta: kind=partial | timestamp=1777915060.3209221 | source=windows
- [2026-05-05 01:17:40] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1777915060.5227654 | source=windows
- [2026-05-05 01:17:40] operator / voice_transcript_partial / voice: wilson
  meta: kind=partial | timestamp=1777915060.964955 | source=windows
- [2026-05-05 01:17:40] operator / voice_transcript_partial / voice: more than one
  meta: kind=partial | timestamp=1777915060.964955 | source=windows
- [2026-05-05 01:17:41] operator / voice_transcript_partial / voice: more than one of
  meta: kind=partial | timestamp=1777915061.5694244 | source=windows
- [2026-05-05 01:17:41] operator / voice_transcript_partial / voice: more than one of the
  meta: kind=partial | timestamp=1777915061.9739556 | source=windows
- [2026-05-05 01:17:42] operator / voice_transcript_partial / voice: more than one of
  meta: kind=partial | timestamp=1777915062.1773777 | source=windows
- [2026-05-05 01:17:43] operator / voice_transcript_final / voice: more than one of
  meta: kind=final | timestamp=1777915063.2013826 | source=final | confidence=0.19
- [2026-05-05 01:17:44] operator / voice_transcript_partial / voice: its
  meta: kind=partial | timestamp=1777915064.022753 | source=windows
- [2026-05-05 01:17:47] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777915067.2705338 | source=windows
- [2026-05-05 01:17:47] operator / voice_transcript_partial / voice: them
  meta: kind=partial | timestamp=1777915067.8829145 | source=windows
- [2026-05-05 01:17:50] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777915070.7242315 | source=windows
- [2026-05-05 01:17:50] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1777915070.9371564 | source=windows
- [2026-05-05 01:17:51] operator / voice_transcript_final / voice: those
  meta: kind=final | timestamp=1777915071.9814224 | source=final | confidence=0.2
- [2026-05-05 01:18:02] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777915082.0133042 | source=windows
- [2026-05-05 01:18:02] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777915082.0133042 | source=windows
- [2026-05-05 01:18:02] operator / voice_transcript_partial / voice: and the
  meta: kind=partial | timestamp=1777915082.9186618 | source=windows
- [2026-05-05 01:18:03] operator / voice_transcript_partial / voice: and the north
  meta: kind=partial | timestamp=1777915083.311028 | source=windows
- [2026-05-05 01:18:03] operator / voice_transcript_partial / voice: and it was
  meta: kind=partial | timestamp=1777915083.541418 | source=windows
- [2026-05-05 01:18:04] operator / voice_transcript_final / voice: and it was
  meta: kind=final | timestamp=1777915084.1602223 | source=final | confidence=0.21
- [2026-05-05 01:18:18] operator / voice_transcript_partial / voice: it's
  meta: kind=partial | timestamp=1777915098.638017 | source=windows | frequency_hz=344.3 | rms=176 | updated_at=1777915098.232812
- [2026-05-05 01:18:18] operator / voice_transcript_partial / voice: if
  meta: kind=partial | timestamp=1777915098.846358 | source=windows | frequency_hz=344.3 | rms=176 | updated_at=1777915098.232812
- [2026-05-05 01:18:19] operator / voice_transcript_partial / voice: status
  meta: kind=partial | timestamp=1777915099.0500467 | source=windows | frequency_hz=344.3 | rms=176 | updated_at=1777915098.232812
- [2026-05-05 01:18:19] operator / voice_transcript_final / voice: does this
  meta: kind=final | timestamp=1777915099.8834705 | source=final | confidence=0.4 | frequency_hz=344.3 | rms=176 | updated_at=1777915098.232812
- [2026-05-05 01:18:19] operator / voice_transcript_partial / voice: mean
  meta: kind=partial | timestamp=1777915099.8844702 | source=windows | frequency_hz=344.3 | rms=176 | updated_at=1777915098.232812
- [2026-05-05 01:18:20] operator / voice_transcript_partial / voice: as a
  meta: kind=partial | timestamp=1777915100.2845879 | source=windows | frequency_hz=344.3 | rms=176 | updated_at=1777915098.232812
- [2026-05-05 01:18:20] operator / voice_transcript_partial / voice: was the
  meta: kind=partial | timestamp=1777915100.4896414 | source=windows | frequency_hz=344.3 | rms=176 | updated_at=1777915098.232812
- [2026-05-05 01:18:21] operator / voice_transcript_final / voice: was the
  meta: kind=final | timestamp=1777915101.3032212 | source=final | confidence=0.19 | frequency_hz=344.3 | rms=176 | updated_at=1777915098.232812
- [2026-05-05 01:18:30] operator / voice_transcript_partial / voice: only
  meta: kind=partial | timestamp=1777915110.2880425 | source=windows | frequency_hz=344.3 | rms=176 | updated_at=1777915098.232812
- [2026-05-05 01:18:30] operator / voice_transcript_partial / voice: way i
  meta: kind=partial | timestamp=1777915110.4903488 | source=windows | frequency_hz=344.3 | rms=176 | updated_at=1777915098.232812
- [2026-05-05 01:18:31] operator / voice_transcript_partial / voice: way home
  meta: kind=partial | timestamp=1777915111.098922 | source=windows | frequency_hz=344.3 | rms=176 | updated_at=1777915098.232812
- [2026-05-05 01:18:31] operator / voice_transcript_partial / voice: only have the
  meta: kind=partial | timestamp=1777915111.9136968 | source=windows | frequency_hz=344.3 | rms=176 | updated_at=1777915098.232812
- [2026-05-05 01:18:32] operator / voice_transcript_partial / voice: only an i am
  meta: kind=partial | timestamp=1777915112.1256301 | source=windows | frequency_hz=344.3 | rms=176 | updated_at=1777915098.232812
- [2026-05-05 01:18:32] operator / voice_transcript_final / voice: only an i am
  meta: kind=final | timestamp=1777915112.928196 | source=final | confidence=0.15 | frequency_hz=344.3 | rms=176 | updated_at=1777915098.232812
- [2026-05-05 01:18:34] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777915114.3476381 | source=windows | frequency_hz=344.3 | rms=176 | updated_at=1777915098.232812
- [2026-05-05 01:18:39] operator / voice_transcript_partial / voice: set
  meta: kind=partial | timestamp=1777915119.777191 | source=windows
- [2026-05-05 01:18:39] operator / voice_transcript_partial / voice: as soon as
  meta: kind=partial | timestamp=1777915119.777191 | source=windows
- [2026-05-05 01:18:41] operator / voice_transcript_partial / voice: as soon as the
  meta: kind=partial | timestamp=1777915121.834658 | source=windows
- [2026-05-05 01:18:42] operator / voice_transcript_partial / voice: as soon as his
  meta: kind=partial | timestamp=1777915122.0332198 | source=windows
- [2026-05-05 01:18:42] operator / voice_transcript_final / voice: as soon as his
  meta: kind=final | timestamp=1777915122.8658829 | source=final | confidence=0.45
- [2026-05-05 01:18:46] operator / voice_transcript_partial / voice: own
  meta: kind=partial | timestamp=1777915126.8972714 | source=windows
- [2026-05-05 01:18:47] operator / voice_transcript_partial / voice: voice
  meta: kind=partial | timestamp=1777915127.2982366 | source=windows
- [2026-05-05 01:18:48] operator / voice_transcript_final / voice: voice
  meta: kind=final | timestamp=1777915128.3813868 | source=final | confidence=0.31
- [2026-05-05 01:18:48] operator / voice_transcript_partial / voice: was
  meta: kind=partial | timestamp=1777915128.3813868 | source=windows
- [2026-05-05 01:18:50] operator / voice_transcript_final / voice: was
  meta: kind=final | timestamp=1777915130.358041 | source=final | confidence=0.45
- [2026-05-05 01:18:51] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777915131.7832499 | source=windows
- [2026-05-05 01:18:52] operator / voice_transcript_partial / voice: less
  meta: kind=partial | timestamp=1777915132.1961772 | source=windows
- [2026-05-05 01:18:52] operator / voice_transcript_partial / voice: voice style
  meta: kind=partial | timestamp=1777915132.806268 | source=windows
- [2026-05-05 01:18:53] operator / voice_transcript_final / voice: less so
  meta: kind=final | timestamp=1777915133.630332 | source=final | confidence=0.69
- [2026-05-05 01:18:59] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777915139.9344716 | source=windows
- [2026-05-05 01:19:00] operator / voice_transcript_final / voice: as
  meta: kind=final | timestamp=1777915140.7552555 | source=final | confidence=0.41
- [2026-05-05 01:19:01] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777915141.7809298 | source=windows
- [2026-05-05 01:19:07] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777915147.9119232 | source=windows
- [2026-05-05 01:19:08] operator / voice_transcript_partial / voice: yes
  meta: kind=partial | timestamp=1777915148.1158075 | source=windows
- [2026-05-05 01:19:08] operator / voice_transcript_partial / voice: this one
  meta: kind=partial | timestamp=1777915148.5209622 | source=windows
- [2026-05-05 01:19:09] operator / voice_transcript_partial / voice: its own name
  meta: kind=partial | timestamp=1777915149.334468 | source=windows
- [2026-05-05 01:19:09] operator / voice_transcript_partial / voice: its own name,
  meta: kind=partial | timestamp=1777915149.535932 | source=windows
- [2026-05-05 01:19:09] operator / voice_transcript_partial / voice: its own name on
  meta: kind=partial | timestamp=1777915149.7446601 | source=windows
- [2026-05-05 01:19:09] operator / voice_transcript_partial / voice: its own name on the
  meta: kind=partial | timestamp=1777915149.943583 | source=windows
- [2026-05-05 01:19:10] operator / voice_transcript_partial / voice: its own name on a
  meta: kind=partial | timestamp=1777915150.5525644 | source=windows
- [2026-05-05 01:19:10] operator / voice_transcript_partial / voice: its own name on the
  meta: kind=partial | timestamp=1777915150.7556524 | source=windows
- [2026-05-05 01:19:11] operator / voice_transcript_final / voice: its own name on the
  meta: kind=final | timestamp=1777915151.5727196 | source=final | confidence=0.3

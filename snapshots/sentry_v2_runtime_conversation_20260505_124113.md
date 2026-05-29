# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-05 12:41:13
- Entries: 178
- Roles: {'assistant': 15, 'system': 1, 'operator': 162}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 1, 'spoken_confirmation': 13, 'voice_transcript_partial': 116, 'voice_transcript_final': 31, 'voice_command': 15}
- Channels: {'text': 2, 'voice': 176}
- Latest operator request: the thought
- Latest assistant message: I think I heard is and that s as. Say yes if that is correct, say it again, or say cancel.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-05 12:38:02] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 12:38:02] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-05 12:38:03] system / voice_status / voice: listening
  meta: kind=status | timestamp=1777955883.1042464 | source=windows
- [2026-05-05 12:38:04] assistant / spoken_confirmation / voice: Smart Sentry AI is online. What do you want me to do first?
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 12:38:07] operator / voice_transcript_partial / voice: some
  meta: kind=partial | timestamp=1777955887.24474 | source=windows
- [2026-05-05 12:38:07] operator / voice_transcript_partial / voice: some of
  meta: kind=partial | timestamp=1777955887.6710966 | source=windows
- [2026-05-05 12:38:07] operator / voice_transcript_partial / voice: some of the
  meta: kind=partial | timestamp=1777955887.8757796 | source=windows
- [2026-05-05 12:38:08] operator / voice_transcript_partial / voice: some of
  meta: kind=partial | timestamp=1777955888.2926128 | source=windows
- [2026-05-05 12:38:09] operator / voice_transcript_final / voice: some of
  meta: kind=final | timestamp=1777955889.1155674 | source=final | confidence=0.16
- [2026-05-05 12:38:09] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777955889.9312832 | source=windows
- [2026-05-05 12:38:11] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777955891.5627403 | source=final | confidence=0.02
- [2026-05-05 12:38:30] operator / voice_transcript_partial / voice: six
  meta: kind=partial | timestamp=1777955910.698981 | source=windows
- [2026-05-05 12:38:31] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777955911.106864 | source=windows
- [2026-05-05 12:38:31] operator / voice_transcript_final / voice: fifth
  meta: kind=final | timestamp=1777955911.722107 | source=final | confidence=0.22
- [2026-05-05 12:38:37] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777955917.8632436 | source=windows
- [2026-05-05 12:38:39] operator / voice_transcript_final / voice: of
  meta: kind=final | timestamp=1777955919.08773 | source=final | confidence=0.46
- [2026-05-05 12:38:40] operator / voice_transcript_partial / voice: each
  meta: kind=partial | timestamp=1777955920.514611 | source=windows
- [2026-05-05 12:38:41] operator / voice_transcript_final / voice: each
  meta: kind=final | timestamp=1777955921.5322244 | source=final | confidence=0.65
- [2026-05-05 12:38:43] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777955923.3729243 | source=windows
- [2026-05-05 12:38:44] operator / voice_transcript_final / voice: of
  meta: kind=final | timestamp=1777955924.6252575 | source=final | confidence=0.23
- [2026-05-05 12:39:02] operator / voice_transcript_partial / voice: us
  meta: kind=partial | timestamp=1777955942.8247554 | source=windows
- [2026-05-05 12:39:04] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777955944.062234 | source=windows
- [2026-05-05 12:39:04] operator / voice_transcript_partial / voice: each of
  meta: kind=partial | timestamp=1777955944.4689865 | source=windows
- [2026-05-05 12:39:05] operator / voice_transcript_final / voice: each of
  meta: kind=final | timestamp=1777955945.4903104 | source=final | confidence=0.53
- [2026-05-05 12:39:06] operator / voice_transcript_partial / voice: us
  meta: kind=partial | timestamp=1777955946.4967241 | source=windows
- [2026-05-05 12:39:06] operator / voice_transcript_partial / voice: six
  meta: kind=partial | timestamp=1777955946.9040098 | source=windows
- [2026-05-05 12:39:07] operator / voice_transcript_final / voice: six
  meta: kind=final | timestamp=1777955947.5167809 | source=final | confidence=0.11
- [2026-05-05 12:39:16] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1777955956.4339736 | source=windows
- [2026-05-05 12:39:17] operator / voice_transcript_final / voice: is
  meta: kind=final | timestamp=1777955957.0483894 | source=final | confidence=0.76
- [2026-05-05 12:39:18] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777955958.4805896 | source=windows
- [2026-05-05 12:39:19] operator / voice_transcript_final / voice: he
  meta: kind=final | timestamp=1777955959.8258026 | source=final | confidence=0.63
- [2026-05-05 12:39:21] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777955961.3468769 | source=windows
- [2026-05-05 12:39:21] operator / voice_transcript_partial / voice: here
  meta: kind=partial | timestamp=1777955961.5580683 | source=windows
- [2026-05-05 12:39:22] operator / voice_transcript_partial / voice: he he
  meta: kind=partial | timestamp=1777955962.3741515 | source=windows
- [2026-05-05 12:39:23] operator / voice_transcript_partial / voice: he he may
  meta: kind=partial | timestamp=1777955963.1323898 | source=windows
- [2026-05-05 12:39:23] operator / voice_transcript_partial / voice: he he gained
  meta: kind=partial | timestamp=1777955963.5747292 | source=windows
- [2026-05-05 12:39:24] operator / voice_transcript_final / voice: he he gained
  meta: kind=final | timestamp=1777955964.615465 | source=final | confidence=0.78
- [2026-05-05 12:39:27] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777955967.0738037 | source=windows
- [2026-05-05 12:39:27] operator / voice_transcript_partial / voice: eighty
  meta: kind=partial | timestamp=1777955967.2818582 | source=windows
- [2026-05-05 12:39:27] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777955967.4996974 | source=windows
- [2026-05-05 12:39:28] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777955968.6998026 | source=final | confidence=0.89
- [2026-05-05 12:39:28] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 12:39:28] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777955968.862798 | source=windows
- [2026-05-05 12:39:29] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777955969.174173 | source=windows | frequency_hz=320.3 | rms=347 | updated_at=1777955969.0608494
- [2026-05-05 12:39:29] operator / voice_transcript_partial / voice: that has
  meta: kind=partial | timestamp=1777955969.625382 | source=windows | frequency_hz=324.4 | rms=256 | updated_at=1777955969.1918955
- [2026-05-05 12:39:30] operator / voice_transcript_final / voice: that has
  meta: kind=final | timestamp=1777955970.965148 | source=final | confidence=0.21 | frequency_hz=309.3 | rms=383 | updated_at=1777955970.8517156
- [2026-05-05 12:39:30] operator / voice_transcript_partial / voice: been
  meta: kind=partial | timestamp=1777955970.966683 | source=windows | frequency_hz=309.3 | rms=383 | updated_at=1777955970.8517156
- [2026-05-05 12:39:30] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777955970.966683 | source=windows | frequency_hz=309.3 | rms=383 | updated_at=1777955970.8517156
- [2026-05-05 12:39:31] operator / voice_transcript_partial / voice: that has
  meta: kind=partial | timestamp=1777955971.2127125 | source=windows | frequency_hz=309.3 | rms=383 | updated_at=1777955970.8517156
- [2026-05-05 12:39:31] operator / voice_transcript_partial / voice: the gift of
  meta: kind=partial | timestamp=1777955971.2127125 | source=windows | frequency_hz=309.3 | rms=383 | updated_at=1777955970.8517156
- [2026-05-05 12:39:31] operator / voice_transcript_partial / voice: that has the
  meta: kind=partial | timestamp=1777955971.4165914 | source=windows | frequency_hz=309.3 | rms=383 | updated_at=1777955970.8517156
- [2026-05-05 12:39:32] operator / voice_transcript_partial / voice: the gift that is
  meta: kind=partial | timestamp=1777955972.0290272 | source=windows | frequency_hz=309.3 | rms=383 | updated_at=1777955970.8517156
- [2026-05-05 12:39:32] operator / voice_transcript_partial / voice: the gift that is the
  meta: kind=partial | timestamp=1777955972.2417355 | source=windows | frequency_hz=286.7 | rms=417 | updated_at=1777955972.201225
- [2026-05-05 12:39:33] operator / voice_transcript_partial / voice: that has the same thing
  meta: kind=partial | timestamp=1777955973.0969772 | source=windows | frequency_hz=306.1 | rms=369 | updated_at=1777955972.5808718
- [2026-05-05 12:39:33] operator / voice_transcript_partial / voice: the gift that is three
  meta: kind=partial | timestamp=1777955973.8623135 | source=windows | frequency_hz=339.8 | rms=1103 | updated_at=1777955973.861768
- [2026-05-05 12:39:34] operator / voice_transcript_partial / voice: that has the same thing if
  meta: kind=partial | timestamp=1777955974.2699118 | source=windows | frequency_hz=352.1 | rms=2277 | updated_at=1777955974.2513597
- [2026-05-05 12:39:34] operator / voice_transcript_partial / voice: the gift that is thought
  meta: kind=partial | timestamp=1777955974.4744284 | source=windows | frequency_hz=352.1 | rms=2277 | updated_at=1777955974.2513597
- [2026-05-05 12:39:34] operator / voice_transcript_partial / voice: that has the same thing
  meta: kind=partial | timestamp=1777955974.6786547 | source=windows | frequency_hz=352.1 | rms=2277 | updated_at=1777955974.2513597
- [2026-05-05 12:39:35] operator / voice_transcript_partial / voice: the gift that is the thea
  meta: kind=partial | timestamp=1777955975.2869534 | source=windows | frequency_hz=371.1 | rms=125 | updated_at=1777955975.2718983
- [2026-05-05 12:39:35] operator / voice_transcript_partial / voice: the gift that is the theater
  meta: kind=partial | timestamp=1777955975.4921246 | source=windows | frequency_hz=371.1 | rms=125 | updated_at=1777955975.2718983
- [2026-05-05 12:39:36] operator / voice_transcript_partial / voice: the gift that is the theater of the
  meta: kind=partial | timestamp=1777955976.3511648 | source=windows | frequency_hz=371.1 | rms=125 | updated_at=1777955975.2718983
- [2026-05-05 12:39:36] operator / voice_transcript_partial / voice: the gift that is the theater-
  meta: kind=partial | timestamp=1777955976.8980644 | source=windows | frequency_hz=371.1 | rms=125 | updated_at=1777955975.2718983
- [2026-05-05 12:39:36] operator / voice_transcript_partial / voice: the gift that is the theater has a
  meta: kind=partial | timestamp=1777955976.8980644 | source=windows | frequency_hz=371.1 | rms=125 | updated_at=1777955975.2718983
- [2026-05-05 12:39:37] operator / voice_transcript_partial / voice: the gift that is the theater hyatt has
  meta: kind=partial | timestamp=1777955977.1012113 | source=windows | frequency_hz=304.7 | rms=333 | updated_at=1777955976.9413455
- [2026-05-05 12:39:37] operator / voice_transcript_partial / voice: the gift that is the theater in the third of the
  meta: kind=partial | timestamp=1777955977.710126 | source=windows | frequency_hz=304.7 | rms=333 | updated_at=1777955976.9413455
- [2026-05-05 12:39:37] operator / voice_transcript_partial / voice: the gift that is the theater hyatt has a
  meta: kind=partial | timestamp=1777955977.9147055 | source=windows | frequency_hz=295.1 | rms=1399 | updated_at=1777955977.831987
- [2026-05-05 12:39:38] operator / voice_transcript_partial / voice: the gift that is the theater that he could have to be an added
  meta: kind=partial | timestamp=1777955978.1176121 | source=windows | frequency_hz=295.1 | rms=1399 | updated_at=1777955977.831987
- [2026-05-05 12:39:38] operator / voice_transcript_partial / voice: the gift that is the theater that he could have to be an adequate
  meta: kind=partial | timestamp=1777955978.5245748 | source=windows | frequency_hz=316.2 | rms=345 | updated_at=1777955978.4722562
- [2026-05-05 12:39:38] operator / voice_transcript_partial / voice: the gift that is the theater that he could have to be another question
  meta: kind=partial | timestamp=1777955978.7264755 | source=windows | frequency_hz=282.1 | rms=173 | updated_at=1777955978.6020403
- [2026-05-05 12:39:41] operator / voice_transcript_final / voice: the gift that is the theater that he could have to be another question
  meta: kind=final | timestamp=1777955981.9846535 | source=final | confidence=0.19 | frequency_hz=282.1 | rms=173 | updated_at=1777955978.6020403
- [2026-05-05 12:39:42] operator / voice_command / voice: the gift that is the theater that he could have to be another question
  meta: normalized=True
- [2026-05-05 12:39:42] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1777955982.1836555 | source=windows | frequency_hz=282.1 | rms=173 | updated_at=1777955978.6020403
- [2026-05-05 12:39:42] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777955982.3900366 | source=windows | frequency_hz=282.1 | rms=173 | updated_at=1777955978.6020403
- [2026-05-05 12:39:42] operator / voice_transcript_final / voice: is
  meta: kind=final | timestamp=1777955982.7965212 | source=final | confidence=0.16 | frequency_hz=282.1 | rms=173 | updated_at=1777955978.6020403
- [2026-05-05 12:39:44] assistant / spoken_confirmation / voice: I think I heard the gift that is the theater that he could have to be another question. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 12:39:56] assistant / spoken_confirmation / voice: No confirmation received. I did not run the gift that is the theater that he could have to be another question.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 12:40:07] operator / voice_transcript_partial / voice: how
  meta: kind=partial | timestamp=1777956007.5641778 | source=windows | frequency_hz=343.8 | rms=133 | updated_at=1777956006.8925548
- [2026-05-05 12:40:07] operator / voice_transcript_partial / voice: hell
  meta: kind=partial | timestamp=1777956007.9677422 | source=windows | frequency_hz=361.6 | rms=154 | updated_at=1777956007.912875
- [2026-05-05 12:40:08] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777956008.1724527 | source=windows | frequency_hz=284.3 | rms=249 | updated_at=1777956008.0427396
- [2026-05-05 12:40:08] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777956008.3752315 | source=final | confidence=0.75 | frequency_hz=235.4 | rms=213 | updated_at=1777956008.1724527
- [2026-05-05 12:40:08] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 12:40:12] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777956012.3808813 | source=windows | frequency_hz=235.4 | rms=213 | updated_at=1777956008.1724527
- [2026-05-05 12:40:12] operator / voice_transcript_final / voice: seen
  meta: kind=final | timestamp=1777956012.9987078 | source=final | confidence=0.61 | frequency_hz=235.4 | rms=213 | updated_at=1777956008.1724527
- [2026-05-05 12:40:13] operator / voice_command / voice: seen
  meta: normalized=True
- [2026-05-05 12:40:15] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777956015.2320316 | source=windows | frequency_hz=269.5 | rms=127 | updated_at=1777956014.9525177
- [2026-05-05 12:40:15] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777956015.4352856 | source=windows | frequency_hz=269.5 | rms=127 | updated_at=1777956014.9525177
- [2026-05-05 12:40:15] operator / voice_transcript_partial / voice: aileen
  meta: kind=partial | timestamp=1777956015.6400087 | source=windows | frequency_hz=317.4 | rms=1279 | updated_at=1777956015.4620986
- [2026-05-05 12:40:15] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777956015.8428307 | source=windows | frequency_hz=317.4 | rms=1279 | updated_at=1777956015.4620986
- [2026-05-05 12:40:16] operator / voice_transcript_partial / voice: that ely and the
  meta: kind=partial | timestamp=1777956016.8881447 | source=windows | frequency_hz=317.4 | rms=1279 | updated_at=1777956015.4620986
- [2026-05-05 12:40:16] operator / voice_transcript_partial / voice: that ely and the navy
  meta: kind=partial | timestamp=1777956016.888649 | source=windows | frequency_hz=317.4 | rms=1279 | updated_at=1777956015.4620986
- [2026-05-05 12:40:17] operator / voice_transcript_final / voice: that ely and the navy
  meta: kind=final | timestamp=1777956017.7005546 | source=final | confidence=0.42 | frequency_hz=317.4 | rms=1279 | updated_at=1777956015.4620986
- [2026-05-05 12:40:17] operator / voice_command / voice: that ely and the navy
  meta: normalized=True
- [2026-05-05 12:40:18] operator / voice_transcript_partial / voice: it's
  meta: kind=partial | timestamp=1777956018.3110201 | source=windows | frequency_hz=317.4 | rms=1279 | updated_at=1777956015.4620986
- [2026-05-05 12:40:18] operator / voice_transcript_partial / voice: sea
  meta: kind=partial | timestamp=1777956018.5134177 | source=windows | frequency_hz=317.4 | rms=1279 | updated_at=1777956015.4620986
- [2026-05-05 12:40:18] operator / voice_transcript_final / voice: sea
  meta: kind=final | timestamp=1777956018.9403176 | source=final | confidence=0.65 | frequency_hz=175.8 | rms=204 | updated_at=1777956018.7919836
- [2026-05-05 12:40:19] operator / voice_command / voice: sea
  meta: normalized=True
- [2026-05-05 12:40:19] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777956019.5536714 | source=windows | frequency_hz=273.4 | rms=508 | updated_at=1777956019.3029718
- [2026-05-05 12:40:19] operator / voice_transcript_partial / voice: that the
  meta: kind=partial | timestamp=1777956019.5536714 | source=windows | frequency_hz=273.4 | rms=508 | updated_at=1777956019.3029718
- [2026-05-05 12:40:20] operator / voice_transcript_partial / voice: of the things
  meta: kind=partial | timestamp=1777956020.5765696 | source=windows | frequency_hz=298.0 | rms=577 | updated_at=1777956019.5626945
- [2026-05-05 12:40:21] operator / voice_transcript_final / voice: of the things
  meta: kind=final | timestamp=1777956021.9064791 | source=final | confidence=0.27 | frequency_hz=298.0 | rms=577 | updated_at=1777956019.5626945
- [2026-05-05 12:40:22] operator / voice_command / voice: of the things
  meta: normalized=True
- [2026-05-05 12:40:23] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777956023.1185687 | source=windows | frequency_hz=298.0 | rms=577 | updated_at=1777956019.5626945
- [2026-05-05 12:40:23] operator / voice_transcript_final / voice: as
  meta: kind=final | timestamp=1777956023.7331822 | source=final | confidence=0.37 | frequency_hz=298.0 | rms=577 | updated_at=1777956019.5626945
- [2026-05-05 12:40:23] operator / voice_command / voice: as
  meta: normalized=True
- [2026-05-05 12:40:25] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 12:40:25] assistant / spoken_confirmation / voice: I think I heard that ely and the navy. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 12:40:25] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 12:40:25] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 12:40:27] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777956027.598979 | source=windows | frequency_hz=298.0 | rms=577 | updated_at=1777956019.5626945
- [2026-05-05 12:40:27] operator / voice_transcript_partial / voice: you
  meta: kind=partial | timestamp=1777956027.8059556 | source=windows | frequency_hz=298.0 | rms=577 | updated_at=1777956019.5626945
- [2026-05-05 12:40:28] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777956028.0087216 | source=windows | frequency_hz=298.0 | rms=577 | updated_at=1777956019.5626945
- [2026-05-05 12:40:29] operator / voice_transcript_partial / voice: alien has a
  meta: kind=partial | timestamp=1777956029.4835513 | source=windows | frequency_hz=298.0 | rms=577 | updated_at=1777956019.5626945
- [2026-05-05 12:40:29] operator / voice_transcript_partial / voice: alien has the
  meta: kind=partial | timestamp=1777956029.6902587 | source=windows | frequency_hz=298.0 | rms=577 | updated_at=1777956019.5626945
- [2026-05-05 12:40:30] operator / voice_transcript_partial / voice: alien if he could see
  meta: kind=partial | timestamp=1777956030.5180304 | source=windows | frequency_hz=298.0 | rms=577 | updated_at=1777956019.5626945
- [2026-05-05 12:40:31] operator / voice_transcript_partial / voice: alien if he could see the
  meta: kind=partial | timestamp=1777956031.1305547 | source=windows | frequency_hz=298.0 | rms=577 | updated_at=1777956019.5626945
- [2026-05-05 12:40:31] operator / voice_transcript_final / voice: elion if he could see the
  meta: kind=final | timestamp=1777956031.5366213 | source=final | confidence=0.46 | frequency_hz=298.0 | rms=577 | updated_at=1777956019.5626945
- [2026-05-05 12:40:31] operator / voice_command / voice: elion if he could see the
  meta: normalized=True
- [2026-05-05 12:40:32] operator / voice_transcript_partial / voice: hell
  meta: kind=partial | timestamp=1777956032.3474455 | source=windows | frequency_hz=298.0 | rms=577 | updated_at=1777956019.5626945
- [2026-05-05 12:40:32] operator / voice_transcript_partial / voice: halle
  meta: kind=partial | timestamp=1777956032.76074 | source=windows | frequency_hz=298.0 | rms=577 | updated_at=1777956019.5626945
- [2026-05-05 12:40:32] operator / voice_transcript_partial / voice: elion
  meta: kind=partial | timestamp=1777956032.9619083 | source=windows | frequency_hz=298.0 | rms=577 | updated_at=1777956019.5626945
- [2026-05-05 12:40:33] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-05 12:40:33] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777956033.2129278 | source=final | confidence=0.92 | frequency_hz=298.0 | rms=577 | updated_at=1777956019.5626945
- [2026-05-05 12:40:34] assistant / spoken_confirmation / voice: I think I heard elion if he could see the. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 12:40:35] operator / voice_transcript_partial / voice: two
  meta: kind=partial | timestamp=1777956035.0004458 | source=windows | frequency_hz=406.2 | rms=987 | updated_at=1777956034.922949
- [2026-05-05 12:40:35] operator / voice_transcript_partial / voice: guy
  meta: kind=partial | timestamp=1777956035.2131488 | source=windows | frequency_hz=406.2 | rms=987 | updated_at=1777956034.922949
- [2026-05-05 12:40:35] operator / voice_transcript_partial / voice: guy image
  meta: kind=partial | timestamp=1777956035.6606197 | source=windows | frequency_hz=406.2 | rms=987 | updated_at=1777956034.922949
- [2026-05-05 12:40:36] operator / voice_transcript_final / voice: guy image
  meta: kind=final | timestamp=1777956036.5598495 | source=final | confidence=0.19 | frequency_hz=406.2 | rms=987 | updated_at=1777956034.922949
- [2026-05-05 12:40:39] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777956039.8532195 | source=windows | frequency_hz=406.2 | rms=987 | updated_at=1777956034.922949
- [2026-05-05 12:40:40] operator / voice_transcript_partial / voice: year
  meta: kind=partial | timestamp=1777956040.058103 | source=windows | frequency_hz=406.2 | rms=987 | updated_at=1777956034.922949
- [2026-05-05 12:40:40] operator / voice_transcript_final / voice: year
  meta: kind=final | timestamp=1777956040.6703742 | source=final | confidence=0.87 | frequency_hz=406.2 | rms=987 | updated_at=1777956034.922949
- [2026-05-05 12:40:40] operator / voice_command / voice: year
  meta: normalized=True
- [2026-05-05 12:40:41] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777956041.5043938 | source=windows | frequency_hz=406.2 | rms=987 | updated_at=1777956034.922949
- [2026-05-05 12:40:41] operator / voice_transcript_partial / voice: use
  meta: kind=partial | timestamp=1777956041.7060406 | source=windows | frequency_hz=406.2 | rms=987 | updated_at=1777956034.922949
- [2026-05-05 12:40:43] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 12:40:44] operator / voice_transcript_final / voice: use the
  meta: kind=final | timestamp=1777956044.1176658 | source=final | confidence=0.52 | frequency_hz=406.2 | rms=987 | updated_at=1777956034.922949
- [2026-05-05 12:40:44] operator / voice_command / voice: use the
  meta: normalized=True
- [2026-05-05 12:40:45] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777956045.312208 | source=windows | frequency_hz=277.3 | rms=566 | updated_at=1777956045.1632943
- [2026-05-05 12:40:45] operator / voice_transcript_partial / voice: th
  meta: kind=partial | timestamp=1777956045.5156617 | source=windows | frequency_hz=277.3 | rms=566 | updated_at=1777956045.1632943
- [2026-05-05 12:40:45] operator / voice_transcript_partial / voice: third
  meta: kind=partial | timestamp=1777956045.7202072 | source=windows | frequency_hz=277.3 | rms=566 | updated_at=1777956045.1632943
- [2026-05-05 12:40:46] operator / voice_transcript_partial / voice: thirty th
  meta: kind=partial | timestamp=1777956046.7762125 | source=windows | frequency_hz=277.3 | rms=566 | updated_at=1777956045.1632943
- [2026-05-05 12:40:46] operator / voice_transcript_partial / voice: thirty three
  meta: kind=partial | timestamp=1777956046.7762125 | source=windows | frequency_hz=277.3 | rms=566 | updated_at=1777956045.1632943
- [2026-05-05 12:40:46] operator / voice_transcript_partial / voice: thirty th hell
  meta: kind=partial | timestamp=1777956046.9910986 | source=windows | frequency_hz=277.3 | rms=566 | updated_at=1777956045.1632943
- [2026-05-05 12:40:47] operator / voice_transcript_partial / voice: third thallium
  meta: kind=partial | timestamp=1777956047.3998082 | source=windows | frequency_hz=277.3 | rms=566 | updated_at=1777956045.1632943
- [2026-05-05 12:40:47] operator / voice_transcript_partial / voice: third thallium the
  meta: kind=partial | timestamp=1777956047.808111 | source=windows | frequency_hz=277.3 | rms=566 | updated_at=1777956045.1632943
- [2026-05-05 12:40:48] operator / voice_transcript_partial / voice: third thallium they have
  meta: kind=partial | timestamp=1777956048.0234997 | source=windows | frequency_hz=277.3 | rms=566 | updated_at=1777956045.1632943
- [2026-05-05 12:40:48] operator / voice_transcript_partial / voice: third thallium to have a question
  meta: kind=partial | timestamp=1777956048.2301004 | source=windows | frequency_hz=277.3 | rms=566 | updated_at=1777956045.1632943
- [2026-05-05 12:40:48] operator / voice_transcript_final / voice: third thallium to have a question
  meta: kind=final | timestamp=1777956048.8605015 | source=final | confidence=0.43 | frequency_hz=277.3 | rms=566 | updated_at=1777956045.1632943
- [2026-05-05 12:40:48] operator / voice_command / voice: third thallium to have a question
  meta: normalized=True
- [2026-05-05 12:40:50] assistant / spoken_confirmation / voice: I think I heard third thallium to have a question. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 12:40:50] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 12:40:52] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777956052.6625285 | source=windows | frequency_hz=277.3 | rms=566 | updated_at=1777956045.1632943
- [2026-05-05 12:40:52] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777956052.6625285 | source=windows | frequency_hz=277.3 | rms=566 | updated_at=1777956045.1632943
- [2026-05-05 12:40:52] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777956052.6625285 | source=windows | frequency_hz=277.3 | rms=566 | updated_at=1777956045.1632943
- [2026-05-05 12:40:52] operator / voice_transcript_final / voice: he
  meta: kind=final | timestamp=1777956052.8775103 | source=final | confidence=0.18 | frequency_hz=277.3 | rms=566 | updated_at=1777956045.1632943
- [2026-05-05 12:40:56] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1777956056.7903092 | source=windows | frequency_hz=277.3 | rms=566 | updated_at=1777956045.1632943
- [2026-05-05 12:40:57] operator / voice_transcript_partial / voice: is the
  meta: kind=partial | timestamp=1777956057.196652 | source=windows | frequency_hz=288.7 | rms=344 | updated_at=1777956057.1936402
- [2026-05-05 12:40:58] operator / voice_transcript_partial / voice: is and that's
  meta: kind=partial | timestamp=1777956058.0070696 | source=windows | frequency_hz=262.3 | rms=254 | updated_at=1777956057.9636977
- [2026-05-05 12:40:58] operator / voice_transcript_partial / voice: is and that's the
  meta: kind=partial | timestamp=1777956058.6289816 | source=windows | frequency_hz=336.1 | rms=386 | updated_at=1777956058.607292
- [2026-05-05 12:40:58] operator / voice_transcript_partial / voice: is and that's as
  meta: kind=partial | timestamp=1777956058.8437986 | source=windows | frequency_hz=360.7 | rms=318 | updated_at=1777956058.7334158
- [2026-05-05 12:40:59] operator / voice_transcript_final / voice: is and that s as
  meta: kind=final | timestamp=1777956059.9246726 | source=final | confidence=0.27 | frequency_hz=296.0 | rms=222 | updated_at=1777956059.243009
- [2026-05-05 12:41:00] operator / voice_command / voice: is and that s as
  meta: normalized=True
- [2026-05-05 12:40:59] operator / voice_transcript_partial / voice: its
  meta: kind=partial | timestamp=1777956059.9361997 | source=windows | frequency_hz=296.0 | rms=222 | updated_at=1777956059.243009
- [2026-05-05 12:41:00] operator / voice_transcript_partial / voice: soon as
  meta: kind=partial | timestamp=1777956060.6436458 | source=windows | frequency_hz=296.0 | rms=222 | updated_at=1777956059.243009
- [2026-05-05 12:41:00] operator / voice_transcript_partial / voice: soon as the
  meta: kind=partial | timestamp=1777956060.8493328 | source=windows | frequency_hz=296.0 | rms=222 | updated_at=1777956059.243009
- [2026-05-05 12:41:01] operator / voice_transcript_partial / voice: soon as yes
  meta: kind=partial | timestamp=1777956061.0497987 | source=windows | frequency_hz=214.8 | rms=7792 | updated_at=1777956061.0332263
- [2026-05-05 12:41:01] operator / voice_transcript_partial / voice: soon as the u.s. and
  meta: kind=partial | timestamp=1777956061.6613944 | source=windows | frequency_hz=252.6 | rms=186 | updated_at=1777956061.2935934
- [2026-05-05 12:41:02] operator / voice_transcript_final / voice: soon as the u s and
  meta: kind=final | timestamp=1777956062.0663106 | source=final | confidence=0.12 | frequency_hz=252.6 | rms=186 | updated_at=1777956061.2935934
- [2026-05-05 12:41:02] operator / voice_command / voice: soon as the u s and
  meta: normalized=True
- [2026-05-05 12:41:04] assistant / spoken_confirmation / voice: I think I heard soon as the u s and. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 12:41:04] assistant / spoken_confirmation / voice: I think I heard is and that s as. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 12:41:07] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777956067.1583388 | source=windows | frequency_hz=390.6 | rms=229 | updated_at=1777956067.0572813
- [2026-05-05 12:41:08] operator / voice_transcript_partial / voice: the thing
  meta: kind=partial | timestamp=1777956068.3828435 | source=windows | frequency_hz=347.7 | rms=1708 | updated_at=1777956068.0736144
- [2026-05-05 12:41:08] operator / voice_transcript_partial / voice: the thing that
  meta: kind=partial | timestamp=1777956068.7892761 | source=windows | frequency_hz=347.7 | rms=1708 | updated_at=1777956068.0736144
- [2026-05-05 12:41:08] operator / voice_transcript_partial / voice: the thing
  meta: kind=partial | timestamp=1777956068.9995663 | source=windows | frequency_hz=347.7 | rms=1708 | updated_at=1777956068.0736144
- [2026-05-05 12:41:09] operator / voice_transcript_partial / voice: the thick
  meta: kind=partial | timestamp=1777956069.636595 | source=windows | frequency_hz=320.3 | rms=417 | updated_at=1777956069.613996
- [2026-05-05 12:41:09] operator / voice_transcript_partial / voice: the thought that the
  meta: kind=partial | timestamp=1777956069.8426046 | source=windows | frequency_hz=320.3 | rms=417 | updated_at=1777956069.613996
- [2026-05-05 12:41:10] operator / voice_transcript_partial / voice: the thought
  meta: kind=partial | timestamp=1777956070.046409 | source=windows | frequency_hz=320.3 | rms=417 | updated_at=1777956069.613996
- [2026-05-05 12:41:10] operator / voice_transcript_final / voice: the thought
  meta: kind=final | timestamp=1777956070.7113106 | source=final | confidence=0.06 | frequency_hz=320.3 | rms=417 | updated_at=1777956069.613996

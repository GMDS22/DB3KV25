# SMART SENTRY V3.5.3 Runtime Conversation Export

- Generated: 2026-05-05 02:29:31
- Entries: 206
- Roles: {'assistant': 7, 'system': 1, 'operator': 198}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 1, 'voice_transcript_partial': 163, 'voice_transcript_final': 32, 'spoken_confirmation': 5, 'voice_command': 3}
- Channels: {'text': 2, 'voice': 204}
- Latest operator request: fifth to eighth to fifth to to
- Latest assistant message: No confirmation received. I did not run fifth seed fifth to eighth up 50 to 50 fifth.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-05 02:24:41] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 02:24:41] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-05 02:24:42] system / voice_status / voice: listening
  meta: kind=status | timestamp=1777919082.949883 | source=windows
- [2026-05-05 02:24:43] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777919083.9244623 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:44] operator / voice_transcript_partial / voice: they see
  meta: kind=partial | timestamp=1777919084.1951158 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:44] operator / voice_transcript_partial / voice: they say
  meta: kind=partial | timestamp=1777919084.4000585 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:44] operator / voice_transcript_partial / voice: they say in
  meta: kind=partial | timestamp=1777919084.6152976 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:45] operator / voice_transcript_partial / voice: they say no
  meta: kind=partial | timestamp=1777919085.02155 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:45] operator / voice_transcript_final / voice: they say no
  meta: kind=final | timestamp=1777919085.8551803 | source=final | confidence=0.05 | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:47] assistant / spoken_confirmation / voice: System online and listening. Do you want me to connect boards, enable sentry, or run another task?
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 02:24:50] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777919090.1747947 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:50] operator / voice_transcript_partial / voice: to a
  meta: kind=partial | timestamp=1777919090.3777812 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:50] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777919090.5942059 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:51] operator / voice_transcript_partial / voice: one can
  meta: kind=partial | timestamp=1777919091.2053056 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:51] operator / voice_transcript_partial / voice: to one and one
  meta: kind=partial | timestamp=1777919091.4085655 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:51] operator / voice_transcript_partial / voice: to see where
  meta: kind=partial | timestamp=1777919091.6102383 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:51] operator / voice_transcript_partial / voice: to one and one
  meta: kind=partial | timestamp=1777919091.8273413 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:53] operator / voice_transcript_partial / voice: to one and one more
  meta: kind=partial | timestamp=1777919093.2489824 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:53] operator / voice_transcript_partial / voice: one says one one
  meta: kind=partial | timestamp=1777919093.464475 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:54] operator / voice_transcript_partial / voice: one says one and one of
  meta: kind=partial | timestamp=1777919094.0888062 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:54] operator / voice_transcript_partial / voice: one says one and one half
  meta: kind=partial | timestamp=1777919094.699646 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:55] operator / voice_transcript_final / voice: one says 1 1 2
  meta: kind=final | timestamp=1777919095.7247226 | source=final | confidence=0.25 | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:56] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777919096.95304 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:58] operator / voice_transcript_partial / voice: its
  meta: kind=partial | timestamp=1777919098.591028 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:59] operator / voice_transcript_final / voice: its
  meta: kind=final | timestamp=1777919099.4031293 | source=final | confidence=0.81 | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:59] operator / voice_transcript_partial / voice: two
  meta: kind=partial | timestamp=1777919099.6033342 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:24:59] operator / voice_transcript_partial / voice: its
  meta: kind=partial | timestamp=1777919099.8051329 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:25:01] operator / voice_transcript_final / voice: its
  meta: kind=final | timestamp=1777919101.0515614 | source=final | confidence=0.73 | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:25:04] operator / voice_transcript_partial / voice: plea
  meta: kind=partial | timestamp=1777919104.2935326 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:25:04] operator / voice_transcript_partial / voice: cleo
  meta: kind=partial | timestamp=1777919104.4956722 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:25:04] operator / voice_transcript_partial / voice: wheel of
  meta: kind=partial | timestamp=1777919104.6963606 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:25:05] operator / voice_transcript_partial / voice: way along
  meta: kind=partial | timestamp=1777919105.1043837 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:25:05] operator / voice_transcript_partial / voice: way along the
  meta: kind=partial | timestamp=1777919105.3192658 | source=windows | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:25:05] operator / voice_transcript_final / voice: elion way along the
  meta: kind=final | timestamp=1777919105.9445517 | source=final | confidence=0.36 | frequency_hz=261.7 | rms=453 | updated_at=1777919083.2471094
- [2026-05-05 02:25:20] operator / voice_command / voice: elion way along the
  meta: normalized=True
- [2026-05-05 02:25:09] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777919109.21283 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:09] operator / voice_transcript_partial / voice: beach
  meta: kind=partial | timestamp=1777919109.4167922 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:17] operator / voice_transcript_partial / voice: east
  meta: kind=partial | timestamp=1777919117.173745 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:17] operator / voice_transcript_partial / voice: sea
  meta: kind=partial | timestamp=1777919117.5806434 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:18] operator / voice_transcript_final / voice: sea
  meta: kind=final | timestamp=1777919118.1901448 | source=final | confidence=0.09 | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:21] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1777919121.0725834 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:21] operator / voice_transcript_partial / voice: is a
  meta: kind=partial | timestamp=1777919121.4803834 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:22] operator / voice_transcript_final / voice: is a
  meta: kind=final | timestamp=1777919122.2931874 | source=final | confidence=0.4 | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:23] operator / voice_transcript_partial / voice: two
  meta: kind=partial | timestamp=1777919123.1020865 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:23] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777919123.3058586 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:23] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777919123.91112 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:24] operator / voice_transcript_partial / voice: fifth to see
  meta: kind=partial | timestamp=1777919124.3206987 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:24] operator / voice_transcript_partial / voice: fifth season
  meta: kind=partial | timestamp=1777919124.520929 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:24] operator / voice_transcript_partial / voice: fifth seed
  meta: kind=partial | timestamp=1777919124.7225122 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:24] operator / voice_transcript_partial / voice: fifth seed to
  meta: kind=partial | timestamp=1777919124.9273016 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:25] operator / voice_transcript_partial / voice: fifth to see if
  meta: kind=partial | timestamp=1777919125.3313384 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:25] operator / voice_transcript_partial / voice: fifth seed fifty
  meta: kind=partial | timestamp=1777919125.9383693 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:26] operator / voice_transcript_partial / voice: fifth seed fifty to fifty
  meta: kind=partial | timestamp=1777919126.9811785 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:27] operator / voice_transcript_partial / voice: fifth seed fifty fifth
  meta: kind=partial | timestamp=1777919127.590421 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:27] operator / voice_transcript_partial / voice: fifth seed fifty fifth to
  meta: kind=partial | timestamp=1777919127.7939775 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:27] operator / voice_transcript_partial / voice: fifth seed fifty fifth
  meta: kind=partial | timestamp=1777919127.995018 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:29] operator / voice_transcript_partial / voice: fifth seed fifty fifth to
  meta: kind=partial | timestamp=1777919129.2139933 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:29] operator / voice_transcript_partial / voice: fifth seed fifty fifth fifteen to
  meta: kind=partial | timestamp=1777919129.819644 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:30] operator / voice_transcript_partial / voice: fifth seed fifth to eighth up fifty to fifty
  meta: kind=partial | timestamp=1777919130.228366 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:31] operator / voice_transcript_partial / voice: fifth seed fifth to eighth up fifty to fifty fifth
  meta: kind=partial | timestamp=1777919131.250895 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:31] operator / voice_transcript_partial / voice: fifth seed fifth to eighth up fifty to fifty to fifty
  meta: kind=partial | timestamp=1777919131.4675913 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:31] operator / voice_transcript_partial / voice: fifth seed fifth to eighth up fifty to fifty fifth
  meta: kind=partial | timestamp=1777919131.668159 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:32] operator / voice_transcript_final / voice: fifth seed fifth to eighth up 50 to 50 fifth
  meta: kind=final | timestamp=1777919132.5092835 | source=final | confidence=0.56 | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:32] operator / voice_command / voice: fifth seed fifth to eighth up 50 to 50 fifth
  meta: normalized=True
- [2026-05-05 02:25:33] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777919133.7359223 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:33] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777919133.9535444 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:34] operator / voice_transcript_partial / voice: to eighth
  meta: kind=partial | timestamp=1777919134.7643082 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:34] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777919134.969183 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:35] operator / voice_transcript_partial / voice: to eighth to
  meta: kind=partial | timestamp=1777919135.3784328 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:35] operator / voice_transcript_partial / voice: fifth in
  meta: kind=partial | timestamp=1777919135.7801375 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:36] operator / voice_transcript_final / voice: fifth in
  meta: kind=final | timestamp=1777919136.8012502 | source=final | confidence=0.35 | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:38] assistant / spoken_confirmation / voice: I think I heard fifth seed fifth to eighth up 50 to 50 fifth. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 02:25:38] assistant / spoken_confirmation / voice: I think I heard elion way along the. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 02:25:40] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777919140.095034 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:41] operator / voice_transcript_partial / voice: the fifth
  meta: kind=partial | timestamp=1777919141.3215811 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:43] operator / voice_transcript_final / voice: the fifth
  meta: kind=final | timestamp=1777919143.8568397 | source=final | confidence=0.18 | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:43] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777919143.971456 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:45] operator / voice_transcript_final / voice: to
  meta: kind=final | timestamp=1777919145.0272803 | source=final | confidence=0.83 | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:45] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777919145.0272803 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:45] operator / voice_transcript_partial / voice: death
  meta: kind=partial | timestamp=1777919145.192691 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:45] operator / voice_transcript_final / voice: death
  meta: kind=final | timestamp=1777919145.5990264 | source=final | confidence=0.79 | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:45] operator / voice_command / voice: death
  meta: normalized=True
- [2026-05-05 02:25:46] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777919146.813748 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:47] operator / voice_transcript_final / voice: to
  meta: kind=final | timestamp=1777919147.4286246 | source=final | confidence=0.89 | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:48] operator / voice_transcript_partial / voice: its
  meta: kind=partial | timestamp=1777919148.0406532 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:49] operator / voice_transcript_partial / voice: my
  meta: kind=partial | timestamp=1777919149.055114 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:49] operator / voice_transcript_partial / voice: live
  meta: kind=partial | timestamp=1777919149.2612038 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:49] operator / voice_transcript_partial / voice: life
  meta: kind=partial | timestamp=1777919149.4610074 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:49] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777919149.6621327 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:51] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 02:25:55] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777919155.992485 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:56] operator / voice_transcript_partial / voice: the guest
  meta: kind=partial | timestamp=1777919156.204114 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:56] operator / voice_transcript_partial / voice: the guests at
  meta: kind=partial | timestamp=1777919156.6292858 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:56] operator / voice_transcript_partial / voice: the vest said
  meta: kind=partial | timestamp=1777919156.8439815 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:57] operator / voice_transcript_partial / voice: the guests at
  meta: kind=partial | timestamp=1777919157.0466402 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:57] operator / voice_transcript_partial / voice: the guests as you
  meta: kind=partial | timestamp=1777919157.469661 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:25:58] operator / voice_transcript_final / voice: the guests as you
  meta: kind=final | timestamp=1777919158.5064726 | source=final | confidence=0.55 | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:00] assistant / spoken_confirmation / voice: No confirmation received. I did not run fifth seed fifth to eighth up 50 to 50 fifth.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 02:26:01] operator / voice_transcript_partial / voice: may
  meta: kind=partial | timestamp=1777919161.1056926 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:01] operator / voice_transcript_partial / voice: gain
  meta: kind=partial | timestamp=1777919161.7188659 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:02] operator / voice_transcript_partial / voice: gain the
  meta: kind=partial | timestamp=1777919162.1415367 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:03] operator / voice_transcript_final / voice: gain the
  meta: kind=final | timestamp=1777919163.5179038 | source=final | confidence=0.58 | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:04] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777919164.1288013 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:04] operator / voice_transcript_partial / voice: own
  meta: kind=partial | timestamp=1777919164.1298046 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:05] operator / voice_transcript_final / voice: own
  meta: kind=final | timestamp=1777919165.361593 | source=final | confidence=0.42 | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:09] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777919169.7192788 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:10] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777919170.0144017 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:10] operator / voice_transcript_final / voice: as
  meta: kind=final | timestamp=1777919170.6947823 | source=final | confidence=0.69 | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:22] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777919182.1979356 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:28] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777919188.7519212 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:29] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777919189.3767595 | source=final | confidence=0.79 | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:32] operator / voice_transcript_partial / voice: two
  meta: kind=partial | timestamp=1777919192.4514332 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:32] operator / voice_transcript_partial / voice: city
  meta: kind=partial | timestamp=1777919192.8521726 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:33] operator / voice_transcript_partial / voice: city he
  meta: kind=partial | timestamp=1777919193.4571595 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:34] operator / voice_transcript_final / voice: city he
  meta: kind=final | timestamp=1777919194.2838962 | source=final | confidence=0.29 | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:39] operator / voice_transcript_partial / voice: may
  meta: kind=partial | timestamp=1777919199.2269666 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:39] operator / voice_transcript_partial / voice: is the main
  meta: kind=partial | timestamp=1777919199.430225 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:39] operator / voice_transcript_final / voice: is the main
  meta: kind=final | timestamp=1777919199.6334434 | source=final | confidence=0.59 | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:43] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777919203.7020404 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:44] operator / voice_transcript_partial / voice: file a
  meta: kind=partial | timestamp=1777919204.30524 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:44] operator / voice_transcript_partial / voice: say they are
  meta: kind=partial | timestamp=1777919204.7285674 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:44] operator / voice_transcript_partial / voice: say they are on
  meta: kind=partial | timestamp=1777919204.944638 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:45] operator / voice_transcript_partial / voice: say they are on the
  meta: kind=partial | timestamp=1777919205.56304 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:26:46] operator / voice_transcript_final / voice: say they are on the
  meta: kind=final | timestamp=1777919206.3752985 | source=final | confidence=0.32 | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:27:12] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777919232.888052 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:27:13] operator / voice_transcript_final / voice: as
  meta: kind=final | timestamp=1777919233.3006482 | source=final | confidence=0.16 | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:27:20] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777919240.7074034 | source=windows | frequency_hz=359.4 | rms=200 | updated_at=1777919108.763626
- [2026-05-05 02:27:21] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777919241.1101425 | source=windows | frequency_hz=390.6 | rms=161 | updated_at=1777919240.90618
- [2026-05-05 02:27:22] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777919242.138012 | source=final | confidence=0.6 | frequency_hz=390.6 | rms=161 | updated_at=1777919240.90618
- [2026-05-05 02:27:41] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777919261.1978393 | source=windows | frequency_hz=390.6 | rms=161 | updated_at=1777919240.90618
- [2026-05-05 02:27:42] operator / voice_transcript_final / voice: as
  meta: kind=final | timestamp=1777919262.2629793 | source=final | confidence=0.62 | frequency_hz=390.6 | rms=161 | updated_at=1777919240.90618
- [2026-05-05 02:27:49] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777919269.25329 | source=windows | frequency_hz=390.6 | rms=161 | updated_at=1777919240.90618
- [2026-05-05 02:27:50] operator / voice_transcript_partial / voice: may
  meta: kind=partial | timestamp=1777919270.9232576 | source=windows | frequency_hz=390.6 | rms=161 | updated_at=1777919240.90618
- [2026-05-05 02:27:53] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777919273.8427908 | source=windows | frequency_hz=390.6 | rms=161 | updated_at=1777919240.90618
- [2026-05-05 02:27:54] operator / voice_transcript_partial / voice: he has
  meta: kind=partial | timestamp=1777919274.4511156 | source=windows | frequency_hz=390.6 | rms=161 | updated_at=1777919240.90618
- [2026-05-05 02:27:55] operator / voice_transcript_partial / voice: he have
  meta: kind=partial | timestamp=1777919275.063092 | source=windows | frequency_hz=390.6 | rms=161 | updated_at=1777919240.90618
- [2026-05-05 02:27:55] operator / voice_transcript_final / voice: he have
  meta: kind=final | timestamp=1777919275.505025 | source=final | confidence=0.24 | frequency_hz=390.6 | rms=161 | updated_at=1777919240.90618
- [2026-05-05 02:28:09] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777919289.7436867 | source=windows | frequency_hz=390.6 | rms=161 | updated_at=1777919240.90618
- [2026-05-05 02:28:13] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777919293.799208 | source=windows | frequency_hz=390.6 | rms=161 | updated_at=1777919240.90618
- [2026-05-05 02:28:15] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777919295.4364865 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:28:24] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777919304.809235 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:28:25] operator / voice_transcript_partial / voice: an
  meta: kind=partial | timestamp=1777919305.4199328 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:28:25] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777919305.716405 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:28:26] operator / voice_transcript_partial / voice: a name and the
  meta: kind=partial | timestamp=1777919306.174546 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:28:26] operator / voice_transcript_final / voice: a name and the
  meta: kind=final | timestamp=1777919306.6710498 | source=final | confidence=0.66 | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:28:31] operator / voice_transcript_partial / voice: main
  meta: kind=partial | timestamp=1777919311.6565108 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:28:41] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777919321.0708904 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:28:47] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777919327.6112435 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:28:49] operator / voice_transcript_final / voice: fifth
  meta: kind=final | timestamp=1777919329.0822344 | source=final | confidence=0.3 | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:28:49] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777919329.457851 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:28:50] operator / voice_transcript_partial / voice: and sixth
  meta: kind=partial | timestamp=1777919330.0794697 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:28:50] operator / voice_transcript_partial / voice: and sixth to
  meta: kind=partial | timestamp=1777919330.5955727 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:28:50] operator / voice_transcript_partial / voice: and sixth
  meta: kind=partial | timestamp=1777919330.7159815 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:28:53] operator / voice_transcript_partial / voice: and sixth to
  meta: kind=partial | timestamp=1777919333.96457 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:28:54] operator / voice_transcript_partial / voice: and sixth to eighth to fifty
  meta: kind=partial | timestamp=1777919334.9868238 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:28:55] operator / voice_transcript_final / voice: and sixth to eighth to 50
  meta: kind=final | timestamp=1777919335.393352 | source=final | confidence=0.19 | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:28:58] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777919338.4754488 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:28:58] operator / voice_transcript_partial / voice: to the
  meta: kind=partial | timestamp=1777919338.8760762 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:28:59] operator / voice_transcript_partial / voice: to gain
  meta: kind=partial | timestamp=1777919339.4989605 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:28:59] operator / voice_transcript_partial / voice: to gain to
  meta: kind=partial | timestamp=1777919339.705136 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:28:59] operator / voice_transcript_partial / voice: to fifty
  meta: kind=partial | timestamp=1777919339.9033768 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:00] operator / voice_transcript_partial / voice: to gain fifth
  meta: kind=partial | timestamp=1777919340.1069937 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:01] operator / voice_transcript_partial / voice: to gain fifth to
  meta: kind=partial | timestamp=1777919341.1249979 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:01] operator / voice_transcript_partial / voice: to gain fifth
  meta: kind=partial | timestamp=1777919341.9374943 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:02] operator / voice_transcript_partial / voice: to gain fifth to eighth
  meta: kind=partial | timestamp=1777919342.549171 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:02] operator / voice_transcript_final / voice: to gain fifth to eighth
  meta: kind=final | timestamp=1777919342.9525192 | source=final | confidence=0.61 | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:03] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777919343.3562858 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:04] operator / voice_transcript_partial / voice: to shift
  meta: kind=partial | timestamp=1777919344.1685507 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:04] operator / voice_transcript_partial / voice: to shift to
  meta: kind=partial | timestamp=1777919344.5779326 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:04] operator / voice_transcript_partial / voice: to fifty
  meta: kind=partial | timestamp=1777919344.7771049 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:05] operator / voice_transcript_partial / voice: to heat up
  meta: kind=partial | timestamp=1777919345.4281688 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:05] operator / voice_transcript_partial / voice: to fifty fifth
  meta: kind=partial | timestamp=1777919345.4281688 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:05] operator / voice_transcript_partial / voice: to keep up
  meta: kind=partial | timestamp=1777919345.7957861 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:05] operator / voice_transcript_partial / voice: to fifty fifth
  meta: kind=partial | timestamp=1777919345.996142 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:07] operator / voice_transcript_final / voice: to 55th
  meta: kind=final | timestamp=1777919347.008486 | source=final | confidence=0.41 | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:07] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777919347.6195004 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:08] operator / voice_transcript_partial / voice: to eighth
  meta: kind=partial | timestamp=1777919348.3088942 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:09] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777919349.047412 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:09] operator / voice_transcript_partial / voice: to eighth
  meta: kind=partial | timestamp=1777919349.047412 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:10] operator / voice_transcript_partial / voice: to eighth to
  meta: kind=partial | timestamp=1777919350.090282 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:10] operator / voice_transcript_partial / voice: to eighth up
  meta: kind=partial | timestamp=1777919350.2696857 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:10] operator / voice_transcript_partial / voice: to eighth up to
  meta: kind=partial | timestamp=1777919350.4629595 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:10] operator / voice_transcript_partial / voice: to sixth to eighth
  meta: kind=partial | timestamp=1777919350.877784 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:11] operator / voice_transcript_partial / voice: to eighth up to
  meta: kind=partial | timestamp=1777919351.080262 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:11] operator / voice_transcript_final / voice: to eighth up to
  meta: kind=final | timestamp=1777919351.6985207 | source=final | confidence=0.41 | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:12] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777919352.2348382 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:12] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777919352.245637 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:12] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777919352.5538435 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:12] operator / voice_transcript_partial / voice: fifth to keep
  meta: kind=partial | timestamp=1777919352.7650862 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:13] operator / voice_transcript_partial / voice: fifth to eighth
  meta: kind=partial | timestamp=1777919353.1806335 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:14] operator / voice_transcript_partial / voice: fifth to eighth to
  meta: kind=partial | timestamp=1777919354.4246724 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:15] operator / voice_transcript_partial / voice: fifth to eighth to fifty
  meta: kind=partial | timestamp=1777919355.2226388 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:15] operator / voice_transcript_partial / voice: fifth to eighth to fifth
  meta: kind=partial | timestamp=1777919355.5117004 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:15] operator / voice_transcript_partial / voice: fifth to eighth to fifty
  meta: kind=partial | timestamp=1777919355.6311414 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:16] operator / voice_transcript_partial / voice: fifth to eighth to fifth to
  meta: kind=partial | timestamp=1777919356.4515047 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:16] operator / voice_transcript_partial / voice: fifth to eighth to fifth to to
  meta: kind=partial | timestamp=1777919356.6527562 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:17] operator / voice_transcript_partial / voice: fifth to eighth to fifty to fifty
  meta: kind=partial | timestamp=1777919357.0576928 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:17] operator / voice_transcript_partial / voice: fifth to eighth to fifth to to
  meta: kind=partial | timestamp=1777919357.4297254 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:17] operator / voice_transcript_final / voice: fifth to eighth to fifth to to
  meta: kind=final | timestamp=1777919357.8714638 | source=final | confidence=0.64 | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:28] operator / voice_transcript_partial / voice: see
  meta: kind=partial | timestamp=1777919368.13022 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:28] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777919368.33663 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:28] operator / voice_transcript_partial / voice: hear
  meta: kind=partial | timestamp=1777919368.5432982 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:28] operator / voice_transcript_partial / voice: hear a
  meta: kind=partial | timestamp=1777919368.9417799 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:29] operator / voice_transcript_partial / voice: hear one
  meta: kind=partial | timestamp=1777919369.14979 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:29] operator / voice_transcript_partial / voice: he won the
  meta: kind=partial | timestamp=1777919369.3510127 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009
- [2026-05-05 02:29:29] operator / voice_transcript_partial / voice: hear only one
  meta: kind=partial | timestamp=1777919369.694512 | source=windows | frequency_hz=320.3 | rms=166 | updated_at=1777919294.1892009

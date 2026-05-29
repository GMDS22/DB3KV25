# SMART SENTRY V3.5.3 Runtime Conversation Export

- Generated: 2026-05-05 02:13:05
- Entries: 634
- Roles: {'assistant': 13, 'system': 1, 'operator': 620}
- Event types: {'assistant_prompt': 2, 'assistant_analysis': 1, 'voice_status': 1, 'spoken_confirmation': 9, 'voice_transcript_partial': 485, 'voice_transcript_final': 128, 'voice_command': 6, 'typed_request': 1, 'spoken_reply': 1}
- Channels: {'text': 4, 'voice': 630}
- Latest operator request: as
- Latest assistant message: Assistant update. Here is a sentry joke. I asked the turret for small talk, and it said it was still calibrating the punchline.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-05 01:55:55] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 01:55:55] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-05 01:55:56] system / voice_status / voice: listening
  meta: kind=status | timestamp=1777917356.817896 | source=windows
- [2026-05-05 01:55:57] assistant / spoken_confirmation / voice: Smart Sentry AI is online. What do you want me to do first?
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 01:55:59] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917359.49009 | source=windows
- [2026-05-05 01:55:59] operator / voice_transcript_partial / voice: this
  meta: kind=partial | timestamp=1777917359.9211226 | source=windows
- [2026-05-05 01:56:00] operator / voice_transcript_partial / voice: this is a
  meta: kind=partial | timestamp=1777917360.1227515 | source=windows
- [2026-05-05 01:56:01] operator / voice_transcript_partial / voice: this is the one
  meta: kind=partial | timestamp=1777917361.1347964 | source=windows
- [2026-05-05 01:56:01] operator / voice_transcript_partial / voice: this is the ones
  meta: kind=partial | timestamp=1777917361.3383222 | source=windows
- [2026-05-05 01:56:01] operator / voice_transcript_partial / voice: this is the one his own
  meta: kind=partial | timestamp=1777917361.5393374 | source=windows
- [2026-05-05 01:56:02] operator / voice_transcript_partial / voice: this is the one zone was
  meta: kind=partial | timestamp=1777917362.3508246 | source=windows
- [2026-05-05 01:56:02] operator / voice_transcript_partial / voice: this is the ones along with
  meta: kind=partial | timestamp=1777917362.5530415 | source=windows
- [2026-05-05 01:56:02] operator / voice_transcript_partial / voice: this is the one zone was one
  meta: kind=partial | timestamp=1777917362.7593977 | source=windows
- [2026-05-05 01:56:03] operator / voice_transcript_partial / voice: this is the one zone was one of
  meta: kind=partial | timestamp=1777917363.5638635 | source=windows
- [2026-05-05 01:56:04] operator / voice_transcript_final / voice: this is the one zone was one of
  meta: kind=final | timestamp=1777917364.3920891 | source=final | confidence=0.32
- [2026-05-05 01:56:05] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917365.8268645 | source=windows
- [2026-05-05 01:56:06] operator / voice_transcript_partial / voice: my
  meta: kind=partial | timestamp=1777917366.030158 | source=windows
- [2026-05-05 01:56:06] operator / voice_transcript_partial / voice: my need
  meta: kind=partial | timestamp=1777917366.4364097 | source=windows
- [2026-05-05 01:56:06] operator / voice_transcript_partial / voice: hiding in the
  meta: kind=partial | timestamp=1777917366.843152 | source=windows
- [2026-05-05 01:56:07] operator / voice_transcript_partial / voice: my need to
  meta: kind=partial | timestamp=1777917367.0450244 | source=windows
- [2026-05-05 01:56:07] operator / voice_transcript_final / voice: my need to
  meta: kind=final | timestamp=1777917367.8575263 | source=final | confidence=0.03
- [2026-05-05 01:56:08] operator / voice_transcript_partial / voice: come
  meta: kind=partial | timestamp=1777917368.2606375 | source=windows
- [2026-05-05 01:56:08] operator / voice_transcript_partial / voice: clean
  meta: kind=partial | timestamp=1777917368.261182 | source=windows
- [2026-05-05 01:56:08] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777917368.6659877 | source=windows
- [2026-05-05 01:56:09] operator / voice_transcript_partial / voice: connect boards
  meta: kind=partial | timestamp=1777917369.0768225 | source=windows
- [2026-05-05 01:56:09] operator / voice_transcript_final / voice: connect boards
  meta: kind=final | timestamp=1777917369.6836615 | source=final | confidence=0.85
- [2026-05-05 01:56:31] operator / voice_command / voice: connect boards
  meta: normalized=True
- [2026-05-05 01:56:13] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777917373.9667008 | source=windows
- [2026-05-05 01:56:14] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777917374.1701572 | source=windows
- [2026-05-05 01:56:14] operator / voice_transcript_partial / voice: continue to
  meta: kind=partial | timestamp=1777917374.3733184 | source=windows
- [2026-05-05 01:56:14] operator / voice_transcript_partial / voice: continue to ignore
  meta: kind=partial | timestamp=1777917374.9795234 | source=windows
- [2026-05-05 01:56:15] operator / voice_transcript_partial / voice: connect boards
  meta: kind=partial | timestamp=1777917375.1829448 | source=windows
- [2026-05-05 01:56:16] operator / voice_transcript_partial / voice: see
  meta: kind=partial | timestamp=1777917376.8232493 | source=windows
- [2026-05-05 01:56:17] operator / voice_transcript_final / voice: see
  meta: kind=final | timestamp=1777917377.636512 | source=final | confidence=0.34
- [2026-05-05 01:56:18] operator / voice_transcript_partial / voice: for
  meta: kind=partial | timestamp=1777917378.0396965 | source=windows
- [2026-05-05 01:56:18] operator / voice_transcript_partial / voice: three
  meta: kind=partial | timestamp=1777917378.244575 | source=windows
- [2026-05-05 01:56:18] operator / voice_transcript_partial / voice: three to
  meta: kind=partial | timestamp=1777917378.4471176 | source=windows
- [2026-05-05 01:56:18] operator / voice_transcript_partial / voice: three g.
  meta: kind=partial | timestamp=1777917378.6481526 | source=windows
- [2026-05-05 01:56:18] operator / voice_transcript_partial / voice: three g. and the
  meta: kind=partial | timestamp=1777917378.8495004 | source=windows
- [2026-05-05 01:56:19] operator / voice_transcript_partial / voice: three g. protein
  meta: kind=partial | timestamp=1777917379.2530735 | source=windows
- [2026-05-05 01:56:19] operator / voice_transcript_partial / voice: three g. and these
  meta: kind=partial | timestamp=1777917379.4557953 | source=windows
- [2026-05-05 01:56:19] operator / voice_transcript_partial / voice: three g. davies is
  meta: kind=partial | timestamp=1777917379.6575959 | source=windows
- [2026-05-05 01:56:20] operator / voice_transcript_partial / voice: three g. davies is sees
  meta: kind=partial | timestamp=1777917380.4881592 | source=windows
- [2026-05-05 01:56:20] operator / voice_transcript_partial / voice: three g. davies is sees its
  meta: kind=partial | timestamp=1777917380.8941386 | source=windows
- [2026-05-05 01:56:21] operator / voice_transcript_partial / voice: three g. davies is sees see
  meta: kind=partial | timestamp=1777917381.3007627 | source=windows
- [2026-05-05 01:56:21] operator / voice_transcript_partial / voice: three g. davies has since he's
  meta: kind=partial | timestamp=1777917381.5021026 | source=windows
- [2026-05-05 01:56:21] operator / voice_transcript_partial / voice: three g. davies is sees sees he
  meta: kind=partial | timestamp=1777917381.7191591 | source=windows
- [2026-05-05 01:56:21] operator / voice_transcript_partial / voice: three g. davies has since he's he's
  meta: kind=partial | timestamp=1777917381.9240425 | source=windows
- [2026-05-05 01:56:22] operator / voice_transcript_partial / voice: three g. davies is sees sees few of
  meta: kind=partial | timestamp=1777917382.533302 | source=windows
- [2026-05-05 01:56:22] operator / voice_transcript_partial / voice: three g. davies is sees sees few of them
  meta: kind=partial | timestamp=1777917382.737561 | source=windows
- [2026-05-05 01:56:22] operator / voice_transcript_partial / voice: three g. davies is sees sees the fans
  meta: kind=partial | timestamp=1777917382.9425445 | source=windows
- [2026-05-05 01:56:23] operator / voice_transcript_partial / voice: three g. davies is sees sees few of its
  meta: kind=partial | timestamp=1777917383.1454163 | source=windows
- [2026-05-05 01:56:23] operator / voice_transcript_partial / voice: three g. davies is sees sees few of them since
  meta: kind=partial | timestamp=1777917383.5498874 | source=windows
- [2026-05-05 01:56:23] operator / voice_transcript_partial / voice: three g. davies is sees sees few of them since the
  meta: kind=partial | timestamp=1777917383.969074 | source=windows
- [2026-05-05 01:56:24] operator / voice_transcript_partial / voice: three g. davies is sees sees few of them since they have
  meta: kind=partial | timestamp=1777917384.3742104 | source=windows
- [2026-05-05 01:56:24] operator / voice_transcript_partial / voice: three g. davies is sees sees few of them since they have been
  meta: kind=partial | timestamp=1777917384.778785 | source=windows
- [2026-05-05 01:56:24] operator / voice_transcript_partial / voice: three g. davies is sees sees few of the sins of these
  meta: kind=partial | timestamp=1777917384.9836252 | source=windows
- [2026-05-05 01:56:25] operator / voice_transcript_partial / voice: three g. davies is sees sees few of the safest thing to
  meta: kind=partial | timestamp=1777917385.1848514 | source=windows
- [2026-05-05 01:56:25] operator / voice_transcript_partial / voice: three g. davies is sees sees few of the sins of these cities
  meta: kind=partial | timestamp=1777917385.3890076 | source=windows
- [2026-05-05 01:56:26] operator / voice_transcript_partial / voice: three g. davies is sees sees few of the sins of these six six
  meta: kind=partial | timestamp=1777917386.1999948 | source=windows
- [2026-05-05 01:56:27] operator / voice_transcript_partial / voice: three g. davies is sees sees few of the sins of these cities since the
  meta: kind=partial | timestamp=1777917387.2231555 | source=windows
- [2026-05-05 01:56:28] operator / voice_transcript_partial / voice: three g. davies is sees sees few of the sins of these cities since the things that have
  meta: kind=partial | timestamp=1777917388.2364419 | source=windows
- [2026-05-05 01:56:29] operator / voice_transcript_partial / voice: three g. davies is sees sees few of the sins of these cities since the fifteenth
  meta: kind=partial | timestamp=1777917389.060641 | source=windows
- [2026-05-05 01:56:29] operator / voice_transcript_partial / voice: three g. davies is sees sees few of the sins of these cities since the fifth
  meta: kind=partial | timestamp=1777917389.4694788 | source=windows
- [2026-05-05 01:56:30] operator / voice_transcript_final / voice: three g davies is sees sees few of the sins of these cities since the fifth
  meta: kind=final | timestamp=1777917390.5037591 | source=final | confidence=0.36
- [2026-05-05 01:56:31] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777917391.5300832 | source=windows
- [2026-05-05 01:56:32] operator / voice_transcript_partial / voice: off
  meta: kind=partial | timestamp=1777917392.1424 | source=windows
- [2026-05-05 01:56:33] operator / voice_transcript_partial / voice: off the
  meta: kind=partial | timestamp=1777917393.0006993 | source=windows
- [2026-05-05 01:56:33] operator / voice_transcript_final / voice: off the
  meta: kind=final | timestamp=1777917393.4086418 | source=final | confidence=0.08
- [2026-05-05 01:56:34] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917394.0183604 | source=windows
- [2026-05-05 01:56:34] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777917394.4384382 | source=windows
- [2026-05-05 01:56:34] operator / voice_transcript_partial / voice: fifth and march
  meta: kind=partial | timestamp=1777917394.8780034 | source=windows
- [2026-05-05 01:56:35] operator / voice_transcript_partial / voice: fifth and market
  meta: kind=partial | timestamp=1777917395.0814347 | source=windows
- [2026-05-05 01:56:35] operator / voice_transcript_partial / voice: death of martin
  meta: kind=partial | timestamp=1777917395.4996786 | source=windows
- [2026-05-05 01:56:36] assistant / spoken_confirmation / voice: Connecting Smart Sentry boards now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 01:56:36] operator / voice_transcript_partial / voice: fifth and market the
  meta: kind=partial | timestamp=1777917396.527498 | source=windows
- [2026-05-05 01:56:36] operator / voice_transcript_partial / voice: fifth and market the old
  meta: kind=partial | timestamp=1777917396.9417775 | source=windows
- [2026-05-05 01:56:37] operator / voice_transcript_partial / voice: fifth and market the old of
  meta: kind=partial | timestamp=1777917397.5609548 | source=windows
- [2026-05-05 01:56:37] operator / voice_transcript_partial / voice: fifth and market the old fifth
  meta: kind=partial | timestamp=1777917397.5609548 | source=windows
- [2026-05-05 01:56:38] operator / voice_transcript_final / voice: fifth and market the old fifth
  meta: kind=final | timestamp=1777917398.5792012 | source=final | confidence=0.37
- [2026-05-05 01:56:42] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777917402.0570552 | source=windows
- [2026-05-05 01:56:42] operator / voice_transcript_partial / voice: in a
  meta: kind=partial | timestamp=1777917402.0570552 | source=windows
- [2026-05-05 01:56:42] operator / voice_transcript_partial / voice: enable
  meta: kind=partial | timestamp=1777917402.2620199 | source=windows
- [2026-05-05 01:56:42] operator / voice_transcript_partial / voice: enable smart
  meta: kind=partial | timestamp=1777917402.6655757 | source=windows
- [2026-05-05 01:56:42] operator / voice_transcript_partial / voice: enables marks
  meta: kind=partial | timestamp=1777917402.8709707 | source=windows
- [2026-05-05 01:56:43] operator / voice_transcript_partial / voice: enable smart sentry
  meta: kind=partial | timestamp=1777917403.087374 | source=windows
- [2026-05-05 01:56:43] operator / voice_transcript_final / voice: enable smart sentry
  meta: kind=final | timestamp=1777917403.9179125 | source=final | confidence=0.76
- [2026-05-05 01:56:43] operator / voice_command / voice: enable smart sentry
  meta: normalized=True
- [2026-05-05 01:56:45] assistant / spoken_confirmation / voice: I think I heard enable smart sentry. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 01:56:46] operator / voice_transcript_partial / voice: in the
  meta: kind=partial | timestamp=1777917406.3674698 | source=windows
- [2026-05-05 01:56:46] operator / voice_transcript_partial / voice: that if
  meta: kind=partial | timestamp=1777917406.9809604 | source=windows
- [2026-05-05 01:56:47] operator / voice_transcript_partial / voice: -
  meta: kind=partial | timestamp=1777917407.1826706 | source=windows
- [2026-05-05 01:56:48] operator / voice_transcript_final / voice: -
  meta: kind=final | timestamp=1777917408.200259 | source=final | confidence=0.04
- [2026-05-05 01:56:52] operator / voice_transcript_partial / voice: more
  meta: kind=partial | timestamp=1777917412.4805267 | source=windows
- [2026-05-05 01:56:52] operator / voice_transcript_partial / voice: wise
  meta: kind=partial | timestamp=1777917412.6805596 | source=windows
- [2026-05-05 01:56:53] operator / voice_transcript_partial / voice: wife show
  meta: kind=partial | timestamp=1777917413.2915037 | source=windows
- [2026-05-05 01:56:53] operator / voice_transcript_partial / voice: wives shall we
  meta: kind=partial | timestamp=1777917413.4947937 | source=windows
- [2026-05-05 01:56:53] operator / voice_transcript_partial / voice: wise chiles
  meta: kind=partial | timestamp=1777917413.6970186 | source=windows
- [2026-05-05 01:56:54] operator / voice_transcript_partial / voice: wife shown these are
  meta: kind=partial | timestamp=1777917414.3104405 | source=windows
- [2026-05-05 01:56:54] operator / voice_transcript_partial / voice: wise chiles what's
  meta: kind=partial | timestamp=1777917414.512962 | source=windows
- [2026-05-05 01:56:54] operator / voice_transcript_partial / voice: wise chiles was
  meta: kind=partial | timestamp=1777917414.7157316 | source=windows
- [2026-05-05 01:56:54] operator / voice_transcript_partial / voice: wise chiles what's
  meta: kind=partial | timestamp=1777917414.9189332 | source=windows
- [2026-05-05 01:56:55] operator / voice_transcript_final / voice: wise chiles what s
  meta: kind=final | timestamp=1777917415.5281904 | source=final | confidence=0.43
- [2026-05-05 01:56:55] operator / voice_command / voice: wise chiles what s
  meta: normalized=True
- [2026-05-05 01:56:57] assistant / spoken_confirmation / voice: I think I heard wise chiles what s. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 01:57:09] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777917429.267871 | source=windows
- [2026-05-05 01:57:09] operator / voice_transcript_partial / voice: in a
  meta: kind=partial | timestamp=1777917429.4826825 | source=windows
- [2026-05-05 01:57:09] operator / voice_transcript_partial / voice: been able
  meta: kind=partial | timestamp=1777917429.6881208 | source=windows
- [2026-05-05 01:57:10] operator / voice_transcript_partial / voice: enables
  meta: kind=partial | timestamp=1777917430.0935106 | source=windows
- [2026-05-05 01:57:10] operator / voice_transcript_partial / voice: enables arts
  meta: kind=partial | timestamp=1777917430.2972896 | source=windows
- [2026-05-05 01:57:10] operator / voice_transcript_partial / voice: enable smart sentry
  meta: kind=partial | timestamp=1777917430.5024471 | source=windows
- [2026-05-05 01:57:10] operator / voice_transcript_final / voice: enable smart sentry
  meta: kind=final | timestamp=1777917430.7078872 | source=final | confidence=0.77
- [2026-05-05 01:57:10] operator / voice_command / voice: enable smart sentry
  meta: normalized=True
- [2026-05-05 01:57:12] assistant / spoken_confirmation / voice: No confirmation received. I did not run wise chiles what s.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 01:57:12] assistant / spoken_confirmation / voice: I think I heard enable smart sentry. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 01:57:17] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777917437.4516819 | source=windows
- [2026-05-05 01:57:17] operator / voice_transcript_partial / voice: been
  meta: kind=partial | timestamp=1777917437.6525173 | source=windows
- [2026-05-05 01:57:18] operator / voice_transcript_partial / voice: in a
  meta: kind=partial | timestamp=1777917438.0609512 | source=windows
- [2026-05-05 01:57:18] operator / voice_transcript_partial / voice: been able
  meta: kind=partial | timestamp=1777917438.2644553 | source=windows
- [2026-05-05 01:57:18] operator / voice_transcript_partial / voice: in the polls
  meta: kind=partial | timestamp=1777917438.683379 | source=windows
- [2026-05-05 01:57:19] operator / voice_transcript_partial / voice: been able smart
  meta: kind=partial | timestamp=1777917439.0896623 | source=windows
- [2026-05-05 01:57:19] operator / voice_transcript_partial / voice: been able smarts
  meta: kind=partial | timestamp=1777917439.2926896 | source=windows
- [2026-05-05 01:57:19] operator / voice_transcript_partial / voice: been able smarts and
  meta: kind=partial | timestamp=1777917439.5098996 | source=windows
- [2026-05-05 01:57:19] operator / voice_transcript_partial / voice: been able smarts into
  meta: kind=partial | timestamp=1777917439.7153964 | source=windows
- [2026-05-05 01:57:20] operator / voice_transcript_final / voice: been able smarts into
  meta: kind=final | timestamp=1777917440.5464566 | source=final | confidence=0.62
- [2026-05-05 01:57:20] operator / voice_command / voice: been able smarts into
  meta: normalized=True
- [2026-05-05 01:57:22] assistant / spoken_confirmation / voice: I think I heard been able smarts into. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 01:57:23] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777917443.19353 | source=windows
- [2026-05-05 01:57:23] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917443.3961549 | source=windows
- [2026-05-05 01:57:27] operator / voice_transcript_partial / voice: queue
  meta: kind=partial | timestamp=1777917447.2624505 | source=windows
- [2026-05-05 01:57:27] operator / voice_transcript_partial / voice: hughes
  meta: kind=partial | timestamp=1777917447.4635346 | source=windows
- [2026-05-05 01:57:27] operator / voice_transcript_partial / voice: here's the
  meta: kind=partial | timestamp=1777917447.8856032 | source=windows
- [2026-05-05 01:57:28] operator / voice_transcript_partial / voice: heroes of
  meta: kind=partial | timestamp=1777917448.3095057 | source=windows
- [2026-05-05 01:57:28] operator / voice_transcript_partial / voice: hughes the huge
  meta: kind=partial | timestamp=1777917448.5098486 | source=windows
- [2026-05-05 01:57:29] operator / voice_transcript_final / voice: hughes the huge
  meta: kind=final | timestamp=1777917449.1486294 | source=final | confidence=0.73
- [2026-05-05 01:57:29] operator / voice_command / voice: hughes the huge
  meta: normalized=True
- [2026-05-05 01:57:31] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 01:57:35] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777917455.3129165 | source=windows
- [2026-05-05 01:57:35] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777917455.5180905 | source=windows
- [2026-05-05 01:57:35] operator / voice_transcript_partial / voice: as the
  meta: kind=partial | timestamp=1777917455.7206993 | source=windows
- [2026-05-05 01:57:35] operator / voice_transcript_partial / voice: as they
  meta: kind=partial | timestamp=1777917455.9240696 | source=windows
- [2026-05-05 01:57:36] operator / voice_transcript_final / voice: as they
  meta: kind=final | timestamp=1777917456.5636754 | source=final | confidence=0.07
- [2026-05-05 01:57:44] assistant / spoken_confirmation / voice: No confirmation received. I did not run been able smarts into.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 01:57:44] operator / voice_transcript_partial / voice: need
  meta: kind=partial | timestamp=1777917464.4181578 | source=windows
- [2026-05-05 01:57:44] operator / voice_transcript_partial / voice: may be
  meta: kind=partial | timestamp=1777917464.6450348 | source=windows
- [2026-05-05 01:57:45] operator / voice_transcript_partial / voice: enable
  meta: kind=partial | timestamp=1777917465.106951 | source=windows
- [2026-05-05 01:57:45] operator / voice_transcript_partial / voice: needed more than
  meta: kind=partial | timestamp=1777917465.317607 | source=windows
- [2026-05-05 01:57:45] operator / voice_transcript_final / voice: needed more than
  meta: kind=final | timestamp=1777917465.9303963 | source=final | confidence=0.16
- [2026-05-05 01:58:09] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917489.937921 | source=windows
- [2026-05-05 01:58:15] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777917495.4907434 | source=final | confidence=0.03 | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:58:18] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777917498.9307828 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:58:42] operator / voice_transcript_partial / voice: new
  meta: kind=partial | timestamp=1777917522.6536696 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:58:42] operator / voice_transcript_partial / voice: year
  meta: kind=partial | timestamp=1777917522.6536696 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:58:42] operator / voice_transcript_partial / voice: hero
  meta: kind=partial | timestamp=1777917522.8549635 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:58:43] operator / voice_transcript_final / voice: hero
  meta: kind=final | timestamp=1777917523.2601783 | source=final | confidence=0.65 | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:58:54] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777917534.553991 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:58:54] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1777917534.7566347 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:58:55] operator / voice_transcript_final / voice: is
  meta: kind=final | timestamp=1777917535.577259 | source=final | confidence=0.6 | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:04] operator / voice_transcript_partial / voice: just
  meta: kind=partial | timestamp=1777917544.8585987 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:05] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777917545.0572684 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:05] operator / voice_transcript_final / voice: as
  meta: kind=final | timestamp=1777917545.9062994 | source=final | confidence=0.57 | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:07] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777917547.9031556 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:08] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917548.1031497 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:08] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777917548.7382486 | source=final | confidence=0.51 | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:11] operator / voice_transcript_partial / voice: key to
  meta: kind=partial | timestamp=1777917551.3641603 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:12] operator / voice_transcript_final / voice: key to
  meta: kind=final | timestamp=1777917552.1932847 | source=final | confidence=0.74 | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:14] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917554.6289778 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:18] operator / voice_transcript_partial / voice: its
  meta: kind=partial | timestamp=1777917558.5177329 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:19] operator / voice_transcript_partial / voice: show
  meta: kind=partial | timestamp=1777917559.742294 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:19] operator / voice_transcript_partial / voice: have
  meta: kind=partial | timestamp=1777917559.742294 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:20] operator / voice_transcript_partial / voice: if i
  meta: kind=partial | timestamp=1777917560.569781 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:21] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777917561.3803217 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:21] operator / voice_transcript_partial / voice: see
  meta: kind=partial | timestamp=1777917561.3803217 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:21] operator / voice_transcript_final / voice: see
  meta: kind=final | timestamp=1777917561.7835724 | source=final | confidence=0.36 | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:26] operator / voice_transcript_partial / voice: if
  meta: kind=partial | timestamp=1777917566.303206 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:26] operator / voice_transcript_final / voice: if
  meta: kind=final | timestamp=1777917566.9165084 | source=final | confidence=0.53 | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:40] operator / voice_transcript_partial / voice: it's
  meta: kind=partial | timestamp=1777917580.0526853 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:41] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917581.0805511 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:42] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777917582.1010888 | source=final | confidence=0.5 | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:57] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917597.675727 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 01:59:59] operator / voice_transcript_final / voice: fifth
  meta: kind=final | timestamp=1777917599.4340115 | source=final | confidence=0.52 | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 02:00:01] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777917601.0097864 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 02:00:04] operator / typed_request / text: TELL A JOKE
  meta: source=assistant_prompt_box
- [2026-05-05 02:00:04] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] Parsed Intent: - action=none confidence=1.00 clarification=False Here is a sentry joke. I asked the turret for small talk, and it said it was still calibrating the punchline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 02:00:12] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777917612.6101754 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 02:00:13] operator / voice_transcript_final / voice: and
  meta: kind=final | timestamp=1777917613.3894558 | source=final | confidence=0.6 | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 02:00:33] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777917633.758448 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 02:00:35] assistant / spoken_reply / voice: Assistant update. Here is a sentry joke. I asked the turret for small talk, and it said it was still calibrating the punchline.
  meta: interrupt=False | assistant_output=True | spoken=True
- [2026-05-05 02:00:37] operator / voice_transcript_partial / voice: eighth
  meta: kind=partial | timestamp=1777917637.9974692 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 02:00:39] operator / voice_transcript_final / voice: eighth
  meta: kind=final | timestamp=1777917639.2176595 | source=final | confidence=0.44 | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 02:00:43] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777917643.4966216 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 02:00:43] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777917643.4966216 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 02:00:44] operator / voice_transcript_final / voice: of
  meta: kind=final | timestamp=1777917644.1747513 | source=final | confidence=0.1 | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 02:00:44] operator / voice_transcript_partial / voice: five
  meta: kind=partial | timestamp=1777917644.7350922 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 02:00:45] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777917645.9573863 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 02:00:46] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917646.1622615 | source=windows | frequency_hz=217.4 | rms=901 | updated_at=1777917493.877028
- [2026-05-05 02:00:47] operator / voice_transcript_partial / voice: an
  meta: kind=partial | timestamp=1777917647.1790123 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:00:47] operator / voice_transcript_final / voice: an
  meta: kind=final | timestamp=1777917647.8190005 | source=final | confidence=0.59 | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:00:48] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777917648.5994227 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:00:48] operator / voice_transcript_partial / voice: ad
  meta: kind=partial | timestamp=1777917648.804065 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:00:49] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777917649.1967688 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:00:49] operator / voice_transcript_final / voice: a
  meta: kind=final | timestamp=1777917649.251917 | source=final | confidence=0.26 | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:00:58] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777917658.2752285 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:00:59] operator / voice_transcript_final / voice: and
  meta: kind=final | timestamp=1777917659.157163 | source=final | confidence=0.67 | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:00] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777917660.4942029 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:00] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917660.4942029 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:01] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777917661.3490715 | source=final | confidence=0.29 | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:15] operator / voice_transcript_partial / voice: money
  meta: kind=partial | timestamp=1777917675.9586463 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:16] operator / voice_transcript_final / voice: money
  meta: kind=final | timestamp=1777917676.9793892 | source=final | confidence=0.52 | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:17] operator / voice_transcript_partial / voice: or
  meta: kind=partial | timestamp=1777917677.7915263 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:18] operator / voice_transcript_final / voice: or
  meta: kind=final | timestamp=1777917678.6435816 | source=final | confidence=0.67 | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:30] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917690.42272 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:33] operator / voice_transcript_partial / voice: in the
  meta: kind=partial | timestamp=1777917693.0869277 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:33] operator / voice_transcript_partial / voice: in a
  meta: kind=partial | timestamp=1777917693.2919447 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:33] operator / voice_transcript_final / voice: in a
  meta: kind=final | timestamp=1777917693.9468098 | source=final | confidence=0.37 | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:34] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777917694.1105075 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:39] operator / voice_transcript_partial / voice: big
  meta: kind=partial | timestamp=1777917699.0954182 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:39] operator / voice_transcript_partial / voice: big house
  meta: kind=partial | timestamp=1777917699.7222476 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:40] operator / voice_transcript_partial / voice: big house and
  meta: kind=partial | timestamp=1777917700.550828 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:40] operator / voice_transcript_partial / voice: big house
  meta: kind=partial | timestamp=1777917700.550828 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:41] operator / voice_transcript_final / voice: big house
  meta: kind=final | timestamp=1777917701.2072759 | source=final | confidence=0.32 | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:43] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777917703.2841659 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:43] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777917703.4972603 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:43] operator / voice_transcript_partial / voice: once we
  meta: kind=partial | timestamp=1777917703.9508169 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:44] operator / voice_transcript_partial / voice: -
  meta: kind=partial | timestamp=1777917704.152032 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:44] operator / voice_transcript_partial / voice: was one of the
  meta: kind=partial | timestamp=1777917704.152032 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:44] operator / voice_transcript_partial / voice: one four one five
  meta: kind=partial | timestamp=1777917704.3565087 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:44] operator / voice_transcript_partial / voice: one four one five nine
  meta: kind=partial | timestamp=1777917704.7818427 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:45] operator / voice_transcript_partial / voice: one four one five million
  meta: kind=partial | timestamp=1777917705.2127144 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:45] operator / voice_transcript_partial / voice: one four one five and was
  meta: kind=partial | timestamp=1777917705.2127144 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:45] operator / voice_transcript_partial / voice: one four one five and was able
  meta: kind=partial | timestamp=1777917705.424326 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:45] operator / voice_transcript_partial / voice: one four one five million receivers and
  meta: kind=partial | timestamp=1777917705.6211777 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:46] operator / voice_transcript_partial / voice: one four one five when was the lesson that
  meta: kind=partial | timestamp=1777917706.2359354 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:46] operator / voice_transcript_partial / voice: one four one five and was a u.s. military
  meta: kind=partial | timestamp=1777917706.4387896 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:47] operator / voice_transcript_partial / voice: one four one five when was the possibility of
  meta: kind=partial | timestamp=1777917707.2239811 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:47] operator / voice_transcript_partial / voice: one four one five when was the possibility that the
  meta: kind=partial | timestamp=1777917707.2581792 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:49] operator / voice_transcript_final / voice: 1415 when was the possibility that the
  meta: kind=final | timestamp=1777917709.1322002 | source=final | confidence=0.19 | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:49] operator / voice_transcript_partial / voice: phone
  meta: kind=partial | timestamp=1777917709.160983 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:49] operator / voice_transcript_partial / voice: fund
  meta: kind=partial | timestamp=1777917709.160983 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:49] operator / voice_transcript_partial / voice: women
  meta: kind=partial | timestamp=1777917709.3054802 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:49] operator / voice_transcript_partial / voice: women of
  meta: kind=partial | timestamp=1777917709.9210665 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:49] operator / voice_transcript_partial / voice: women of the
  meta: kind=partial | timestamp=1777917709.9210665 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:50] operator / voice_transcript_partial / voice: women of
  meta: kind=partial | timestamp=1777917710.122609 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:51] operator / voice_transcript_partial / voice: final one of the
  meta: kind=partial | timestamp=1777917711.129733 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:51] operator / voice_transcript_partial / voice: window of a
  meta: kind=partial | timestamp=1777917711.3361142 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:52] operator / voice_transcript_final / voice: window of a
  meta: kind=final | timestamp=1777917712.265031 | source=final | confidence=0.22 | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:54] operator / voice_transcript_partial / voice: few
  meta: kind=partial | timestamp=1777917714.5452979 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:54] operator / voice_transcript_partial / voice: famous
  meta: kind=partial | timestamp=1777917714.7424393 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:55] operator / voice_transcript_partial / voice: union
  meta: kind=partial | timestamp=1777917715.1441112 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:55] operator / voice_transcript_partial / voice: hearing
  meta: kind=partial | timestamp=1777917715.572615 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:01:55] operator / voice_transcript_final / voice: hearing
  meta: kind=final | timestamp=1777917715.9633822 | source=final | confidence=0.24 | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:02:06] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917726.1342413 | source=windows | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:02:07] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777917727.1542702 | source=final | confidence=0.3 | frequency_hz=152.3 | rms=191 | updated_at=1777917646.6740603
- [2026-05-05 02:02:17] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917737.3120983 | source=windows | frequency_hz=348.0 | rms=271 | updated_at=1777917737.1558275
- [2026-05-05 02:02:18] operator / voice_transcript_partial / voice: the the
  meta: kind=partial | timestamp=1777917738.5439768 | source=windows | frequency_hz=348.0 | rms=271 | updated_at=1777917737.1558275
- [2026-05-05 02:02:19] operator / voice_transcript_partial / voice: the air
  meta: kind=partial | timestamp=1777917739.0851023 | source=windows | frequency_hz=348.0 | rms=271 | updated_at=1777917737.1558275
- [2026-05-05 02:02:20] operator / voice_transcript_partial / voice: the air in its
  meta: kind=partial | timestamp=1777917740.207807 | source=windows | frequency_hz=348.0 | rms=271 | updated_at=1777917737.1558275
- [2026-05-05 02:02:21] operator / voice_transcript_final / voice: the air in its
  meta: kind=final | timestamp=1777917741.046865 | source=final | confidence=0.64 | frequency_hz=348.0 | rms=271 | updated_at=1777917737.1558275
- [2026-05-05 02:02:22] operator / voice_transcript_partial / voice: of the
  meta: kind=partial | timestamp=1777917742.6681654 | source=windows | frequency_hz=348.0 | rms=271 | updated_at=1777917737.1558275
- [2026-05-05 02:02:33] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777917753.625959 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:02:34] operator / voice_transcript_final / voice: fifth
  meta: kind=final | timestamp=1777917754.4917006 | source=final | confidence=0.4 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:02:46] operator / voice_transcript_partial / voice: day
  meta: kind=partial | timestamp=1777917766.8671606 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:01] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777917781.5867784 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:02] operator / voice_transcript_final / voice: of
  meta: kind=final | timestamp=1777917782.6250293 | source=final | confidence=0.58 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:03] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917783.899934 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:12] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777917792.406778 | source=final | confidence=0.31 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:14] operator / voice_transcript_partial / voice: be
  meta: kind=partial | timestamp=1777917794.1150908 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:38] operator / voice_transcript_partial / voice: end of the
  meta: kind=partial | timestamp=1777917818.8749325 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:39] operator / voice_transcript_partial / voice: game
  meta: kind=partial | timestamp=1777917819.0756896 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:39] operator / voice_transcript_partial / voice: end of
  meta: kind=partial | timestamp=1777917819.2804217 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:40] operator / voice_transcript_final / voice: end of
  meta: kind=final | timestamp=1777917820.2946615 | source=final | confidence=0.17 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:47] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917827.0444107 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:47] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917827.4376543 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:48] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917828.6632676 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:48] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917828.6632676 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:49] operator / voice_transcript_partial / voice: up to
  meta: kind=partial | timestamp=1777917829.2751575 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:50] operator / voice_transcript_partial / voice: the key to keep
  meta: kind=partial | timestamp=1777917830.0947719 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:50] operator / voice_transcript_partial / voice: the fifth
  meta: kind=partial | timestamp=1777917830.295602 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:51] operator / voice_transcript_final / voice: the fifth
  meta: kind=final | timestamp=1777917831.4358234 | source=final | confidence=0.46 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:53] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777917833.3775342 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:54] operator / voice_transcript_partial / voice: to eighth to
  meta: kind=partial | timestamp=1777917834.6035204 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:55] operator / voice_transcript_final / voice: to eighth to
  meta: kind=final | timestamp=1777917835.6162708 | source=final | confidence=0.5 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:56] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917836.2252808 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:57] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777917837.2448866 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:58] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917838.066987 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:58] operator / voice_transcript_final / voice: keep
  meta: kind=final | timestamp=1777917838.678797 | source=final | confidence=0.02 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:59] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917839.4030232 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:03:59] operator / voice_transcript_partial / voice: up
  meta: kind=partial | timestamp=1777917839.5017085 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:00] operator / voice_transcript_final / voice: up
  meta: kind=final | timestamp=1777917840.1184888 | source=final | confidence=0.81 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:00] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777917840.2992334 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:00] operator / voice_transcript_partial / voice: to fifty
  meta: kind=partial | timestamp=1777917840.9094172 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:01] operator / voice_transcript_final / voice: to 50
  meta: kind=final | timestamp=1777917841.9770088 | source=final | confidence=0.69 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:02] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777917842.9436579 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:03] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917843.782402 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:04] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777917844.7761397 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:05] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777917845.3867853 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:06] operator / voice_transcript_partial / voice: fifth to keep
  meta: kind=partial | timestamp=1777917846.600942 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:07] operator / voice_transcript_partial / voice: fifth to eighth to
  meta: kind=partial | timestamp=1777917847.447708 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:07] operator / voice_transcript_partial / voice: fifth to keep up to
  meta: kind=partial | timestamp=1777917847.648346 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:07] operator / voice_transcript_partial / voice: fifth to eighth to ten
  meta: kind=partial | timestamp=1777917847.8467646 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:09] operator / voice_transcript_final / voice: fifth to eighth to 10
  meta: kind=final | timestamp=1777917849.139341 | source=final | confidence=0.24 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:10] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917850.096297 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:10] operator / voice_transcript_partial / voice: to fifteen
  meta: kind=partial | timestamp=1777917850.4922025 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:11] operator / voice_transcript_final / voice: to 15
  meta: kind=final | timestamp=1777917851.4095807 | source=final | confidence=0.54 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:11] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777917851.5225904 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:11] operator / voice_transcript_partial / voice: to ten
  meta: kind=partial | timestamp=1777917851.930233 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:12] operator / voice_transcript_partial / voice: to fifteen
  meta: kind=partial | timestamp=1777917852.1545842 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:12] operator / voice_transcript_partial / voice: to fifteen to
  meta: kind=partial | timestamp=1777917852.9509082 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:13] operator / voice_transcript_partial / voice: to death to keep
  meta: kind=partial | timestamp=1777917853.560699 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:14] operator / voice_transcript_partial / voice: to death to keep up
  meta: kind=partial | timestamp=1777917854.26731 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:15] operator / voice_transcript_partial / voice: to death to keep up with
  meta: kind=partial | timestamp=1777917855.207853 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:15] operator / voice_transcript_partial / voice: to death to keep up with the
  meta: kind=partial | timestamp=1777917855.4103665 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:15] operator / voice_transcript_partial / voice: to death to keep up with death
  meta: kind=partial | timestamp=1777917855.6076663 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:16] operator / voice_transcript_partial / voice: to death to keep up with death to
  meta: kind=partial | timestamp=1777917856.4335515 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:16] operator / voice_transcript_partial / voice: to death to keep up with death to keep
  meta: kind=partial | timestamp=1777917856.900424 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:18] operator / voice_transcript_partial / voice: to death to keep up with death to keep up to
  meta: kind=partial | timestamp=1777917858.341495 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:18] operator / voice_transcript_partial / voice: to death to keep up with death to keep up to keep
  meta: kind=partial | timestamp=1777917858.9424417 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:19] operator / voice_transcript_partial / voice: to death to keep up with death to keep up to up to
  meta: kind=partial | timestamp=1777917859.8015351 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:20] operator / voice_transcript_final / voice: to death to keep up with death to keep up to up to
  meta: kind=final | timestamp=1777917860.789654 | source=final | confidence=0.56 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:21] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917861.5912304 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:21] operator / voice_transcript_partial / voice: date
  meta: kind=partial | timestamp=1777917861.790208 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:21] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777917861.9883194 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:22] operator / voice_transcript_partial / voice: fifth to
  meta: kind=partial | timestamp=1777917862.8066928 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:23] operator / voice_transcript_final / voice: fifth to
  meta: kind=final | timestamp=1777917863.484263 | source=final | confidence=0.81 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:24] operator / voice_transcript_partial / voice: ten to
  meta: kind=partial | timestamp=1777917864.3818061 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:25] operator / voice_transcript_final / voice: 10 to
  meta: kind=final | timestamp=1777917865.0440128 | source=final | confidence=0.83 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:29] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917869.3539658 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:29] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777917869.3549695 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:29] operator / voice_transcript_partial / voice: fifteen
  meta: kind=partial | timestamp=1777917869.5394797 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:30] operator / voice_transcript_final / voice: 15
  meta: kind=final | timestamp=1777917870.5573194 | source=final | confidence=0.05 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:30] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777917870.759489 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:30] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917870.9676535 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:31] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777917871.2006102 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:31] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917871.3700104 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:32] operator / voice_transcript_final / voice: to
  meta: kind=final | timestamp=1777917872.787461 | source=final | confidence=0.84 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:32] operator / voice_transcript_partial / voice: two
  meta: kind=partial | timestamp=1777917872.9929497 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:33] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917873.2060552 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:33] operator / voice_transcript_partial / voice: ten to
  meta: kind=partial | timestamp=1777917873.3962212 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:34] operator / voice_transcript_partial / voice: ten to fifteen
  meta: kind=partial | timestamp=1777917874.4131894 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:35] operator / voice_transcript_final / voice: 10 to 15
  meta: kind=final | timestamp=1777917875.6929336 | source=final | confidence=0.2 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:36] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917876.2513447 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:37] operator / voice_transcript_partial / voice: up to
  meta: kind=partial | timestamp=1777917877.269415 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:38] operator / voice_transcript_final / voice: up to
  meta: kind=final | timestamp=1777917878.0985274 | source=final | confidence=0.21 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:45] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917885.0425227 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:45] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777917885.7430935 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:45] operator / voice_transcript_partial / voice: fifty to
  meta: kind=partial | timestamp=1777917885.9450874 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:46] operator / voice_transcript_partial / voice: a fifth
  meta: kind=partial | timestamp=1777917886.149919 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:47] operator / voice_transcript_final / voice: a fifth
  meta: kind=final | timestamp=1777917887.1628103 | source=final | confidence=0.29 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:48] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777917888.1833515 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:48] operator / voice_transcript_partial / voice: and sixth
  meta: kind=partial | timestamp=1777917888.399805 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:49] operator / voice_transcript_final / voice: and sixth
  meta: kind=final | timestamp=1777917889.1902893 | source=final | confidence=0.27 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:49] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917889.3937933 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:50] operator / voice_transcript_partial / voice: up to
  meta: kind=partial | timestamp=1777917890.4077826 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:51] operator / voice_transcript_partial / voice: to keep up to
  meta: kind=partial | timestamp=1777917891.2332535 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:51] operator / voice_transcript_final / voice: to keep up to
  meta: kind=final | timestamp=1777917891.6508753 | source=final | confidence=0.8 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:55] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917895.6954124 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:56] operator / voice_transcript_partial / voice: keep up
  meta: kind=partial | timestamp=1777917896.522125 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:57] operator / voice_transcript_partial / voice: keep up its
  meta: kind=partial | timestamp=1777917897.5472517 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:57] operator / voice_transcript_partial / voice: keep up seventy
  meta: kind=partial | timestamp=1777917897.754808 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:57] operator / voice_transcript_partial / voice: keep up its fifth
  meta: kind=partial | timestamp=1777917897.9532135 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:04:58] operator / voice_transcript_final / voice: keep up its fifth
  meta: kind=final | timestamp=1777917898.5747316 | source=final | confidence=0.37 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:02] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917902.6473117 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:04] operator / voice_transcript_partial / voice: to keep up to
  meta: kind=partial | timestamp=1777917904.4964688 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:04] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917904.6921089 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:07] operator / voice_transcript_final / voice: to keep up
  meta: kind=final | timestamp=1777917907.0995488 | source=final | confidence=0.21 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:07] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777917907.540069 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:09] operator / voice_transcript_final / voice: to
  meta: kind=final | timestamp=1777917909.0008402 | source=final | confidence=0.72 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:10] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777917910.407498 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:11] operator / voice_transcript_final / voice: 50
  meta: kind=final | timestamp=1777917911.6296659 | source=final | confidence=0.67 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:15] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917915.3049734 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:16] operator / voice_transcript_final / voice: up to
  meta: kind=final | timestamp=1777917916.9494827 | source=final | confidence=0.65 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:20] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917920.0157895 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:20] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777917920.219803 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:21] operator / voice_transcript_partial / voice: fifty to
  meta: kind=partial | timestamp=1777917921.0476615 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:21] operator / voice_transcript_final / voice: 50 to
  meta: kind=final | timestamp=1777917921.5366895 | source=final | confidence=0.63 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:26] operator / voice_transcript_partial / voice: two
  meta: kind=partial | timestamp=1777917926.3796885 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:26] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917926.3796885 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:26] operator / voice_transcript_partial / voice: fifty
  meta: kind=partial | timestamp=1777917926.5822637 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:26] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917926.789379 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:28] operator / voice_transcript_final / voice: keep
  meta: kind=final | timestamp=1777917928.2291627 | source=final | confidence=0.47 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:28] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917928.2291627 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:28] operator / voice_transcript_partial / voice: up
  meta: kind=partial | timestamp=1777917928.64089 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:29] operator / voice_transcript_partial / voice: up with
  meta: kind=partial | timestamp=1777917929.438104 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:29] operator / voice_transcript_partial / voice: up
  meta: kind=partial | timestamp=1777917929.6570218 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:30] operator / voice_transcript_partial / voice: the fifth
  meta: kind=partial | timestamp=1777917930.4695578 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:30] operator / voice_transcript_partial / voice: up
  meta: kind=partial | timestamp=1777917930.6563401 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:30] operator / voice_transcript_partial / voice: up to fifty
  meta: kind=partial | timestamp=1777917930.8551664 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:31] operator / voice_transcript_final / voice: up to 50
  meta: kind=final | timestamp=1777917931.7506855 | source=final | confidence=0.2 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:34] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777917934.1209483 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:34] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777917934.5536885 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:35] operator / voice_transcript_final / voice: fifth
  meta: kind=final | timestamp=1777917935.4275517 | source=final | confidence=0.81 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:38] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777917938.2158473 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:39] operator / voice_transcript_final / voice: to
  meta: kind=final | timestamp=1777917939.0257235 | source=final | confidence=0.91 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:39] operator / voice_transcript_partial / voice: sixth
  meta: kind=partial | timestamp=1777917939.2251709 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:40] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917940.2461126 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:41] operator / voice_transcript_partial / voice: give
  meta: kind=partial | timestamp=1777917941.7611494 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:41] operator / voice_transcript_partial / voice: sixth
  meta: kind=partial | timestamp=1777917941.8790324 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:43] operator / voice_transcript_final / voice: sixth
  meta: kind=final | timestamp=1777917943.181345 | source=final | confidence=0.31 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:43] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777917943.3165717 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:43] operator / voice_transcript_partial / voice: to that
  meta: kind=partial | timestamp=1777917943.7195807 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:43] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777917943.940838 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:45] operator / voice_transcript_final / voice: fifth
  meta: kind=final | timestamp=1777917945.3696375 | source=final | confidence=0.76 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:47] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777917947.8267806 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:48] operator / voice_transcript_final / voice: to
  meta: kind=final | timestamp=1777917948.4513237 | source=final | confidence=0.25 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:49] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917949.4564316 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:49] operator / voice_transcript_partial / voice: ten to
  meta: kind=partial | timestamp=1777917949.8541873 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:50] operator / voice_transcript_final / voice: 10 to
  meta: kind=final | timestamp=1777917950.2687771 | source=final | confidence=0.69 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:51] operator / voice_transcript_partial / voice: two
  meta: kind=partial | timestamp=1777917951.291091 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:51] operator / voice_transcript_partial / voice: fifteen
  meta: kind=partial | timestamp=1777917951.4952357 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:52] operator / voice_transcript_partial / voice: fifteen to
  meta: kind=partial | timestamp=1777917952.4400542 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:53] operator / voice_transcript_partial / voice: fifth to sixth
  meta: kind=partial | timestamp=1777917953.9365354 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:54] operator / voice_transcript_partial / voice: fifth to sixth to
  meta: kind=partial | timestamp=1777917954.5448701 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:54] operator / voice_transcript_partial / voice: fifth to sixth
  meta: kind=partial | timestamp=1777917954.7668035 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:54] operator / voice_transcript_partial / voice: fifth to sixth to
  meta: kind=partial | timestamp=1777917954.9653502 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:55] operator / voice_transcript_final / voice: fifth to sixth to
  meta: kind=final | timestamp=1777917955.5811226 | source=final | confidence=0.56 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:56] operator / voice_transcript_partial / voice: ten
  meta: kind=partial | timestamp=1777917956.3922362 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:56] operator / voice_transcript_partial / voice: tenth
  meta: kind=partial | timestamp=1777917956.5870044 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:57] operator / voice_transcript_final / voice: 10th
  meta: kind=final | timestamp=1777917957.8829968 | source=final | confidence=0.56 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:58] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777917958.0093207 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:59] operator / voice_transcript_final / voice: to
  meta: kind=final | timestamp=1777917959.3414276 | source=final | confidence=0.45 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:59] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917959.3414276 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:05:59] operator / voice_transcript_partial / voice: fifteen
  meta: kind=partial | timestamp=1777917959.3414276 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:00] operator / voice_transcript_partial / voice: fifteen to
  meta: kind=partial | timestamp=1777917960.4466822 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:00] operator / voice_transcript_partial / voice: keep up
  meta: kind=partial | timestamp=1777917960.8776634 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:03] operator / voice_transcript_final / voice: keep up
  meta: kind=final | timestamp=1777917963.1450918 | source=final | confidence=0.08 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:03] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777917963.6946115 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:04] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917964.3072348 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:05] operator / voice_transcript_partial / voice: to fifth
  meta: kind=partial | timestamp=1777917965.1239252 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:05] operator / voice_transcript_partial / voice: to keep up
  meta: kind=partial | timestamp=1777917965.7250543 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:05] operator / voice_transcript_partial / voice: to fifth to
  meta: kind=partial | timestamp=1777917965.9258099 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:06] operator / voice_transcript_partial / voice: to keep up
  meta: kind=partial | timestamp=1777917966.1289124 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:06] operator / voice_transcript_partial / voice: to fifth to eighth
  meta: kind=partial | timestamp=1777917966.7420156 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:06] operator / voice_transcript_partial / voice: to keep up
  meta: kind=partial | timestamp=1777917966.9429884 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:07] operator / voice_transcript_partial / voice: to keep up the
  meta: kind=partial | timestamp=1777917967.7591565 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:07] operator / voice_transcript_partial / voice: to keep up
  meta: kind=partial | timestamp=1777917967.9697204 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:09] operator / voice_transcript_final / voice: to keep up
  meta: kind=final | timestamp=1777917969.4114954 | source=final | confidence=0.09 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:12] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777917972.2551978 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:12] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917972.6643398 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:13] operator / voice_transcript_final / voice: to 50
  meta: kind=final | timestamp=1777917973.693506 | source=final | confidence=0.54 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:14] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777917974.3036416 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:14] operator / voice_transcript_partial / voice: keep
  meta: kind=partial | timestamp=1777917974.5108743 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:15] operator / voice_transcript_partial / voice: up to
  meta: kind=partial | timestamp=1777917975.7317762 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:16] operator / voice_transcript_final / voice: up to
  meta: kind=final | timestamp=1777917976.7782907 | source=final | confidence=0.58 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:16] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917976.9719448 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:18] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777917978.1355047 | source=final | confidence=0.89 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:22] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777917982.5301678 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:28] operator / voice_transcript_partial / voice: than he
  meta: kind=partial | timestamp=1777917988.7254617 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:29] operator / voice_transcript_final / voice: than he
  meta: kind=final | timestamp=1777917989.4306533 | source=final | confidence=0.34 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:32] operator / voice_transcript_partial / voice: would
  meta: kind=partial | timestamp=1777917992.152692 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:32] operator / voice_transcript_partial / voice: can
  meta: kind=partial | timestamp=1777917992.3549788 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:33] operator / voice_transcript_final / voice: can
  meta: kind=final | timestamp=1777917993.1729398 | source=final | confidence=0.23 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:35] operator / voice_transcript_partial / voice: be
  meta: kind=partial | timestamp=1777917995.6599295 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:35] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777917995.861948 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:36] operator / voice_transcript_partial / voice: hear the
  meta: kind=partial | timestamp=1777917996.062274 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:06:36] operator / voice_transcript_final / voice: hear the
  meta: kind=final | timestamp=1777917996.890323 | source=final | confidence=0.17 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:07:25] operator / voice_transcript_partial / voice: main
  meta: kind=partial | timestamp=1777918045.3949926 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:07:26] operator / voice_transcript_final / voice: main
  meta: kind=final | timestamp=1777918046.234859 | source=final | confidence=0.52 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:07:34] operator / voice_transcript_partial / voice: and he
  meta: kind=partial | timestamp=1777918054.171805 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:07:35] operator / voice_transcript_partial / voice: and the
  meta: kind=partial | timestamp=1777918055.0022795 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:07:35] operator / voice_transcript_final / voice: and the
  meta: kind=final | timestamp=1777918055.8293955 | source=final | confidence=0.71 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:07:36] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777918056.235415 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:07:36] operator / voice_transcript_partial / voice: end
  meta: kind=partial | timestamp=1777918056.459007 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:07:37] operator / voice_transcript_final / voice: end
  meta: kind=final | timestamp=1777918057.0444806 | source=final | confidence=0.49 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:07:42] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777918062.1469285 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:07:42] operator / voice_transcript_partial / voice: of the
  meta: kind=partial | timestamp=1777918062.5333405 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:07:42] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777918062.7519724 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:07:50] operator / voice_transcript_partial / voice: of the
  meta: kind=partial | timestamp=1777918070.8973227 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:07:51] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777918071.307595 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:07:51] operator / voice_transcript_partial / voice: of the
  meta: kind=partial | timestamp=1777918071.5152516 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:07:52] operator / voice_transcript_final / voice: of the
  meta: kind=final | timestamp=1777918072.13703 | source=final | confidence=0.24 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:02] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777918082.2934425 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:03] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777918083.5957468 | source=final | confidence=0.64 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:06] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777918086.5823107 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:07] operator / voice_transcript_partial / voice: the the
  meta: kind=partial | timestamp=1777918087.4120245 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:08] operator / voice_transcript_final / voice: the the
  meta: kind=final | timestamp=1777918088.4465945 | source=final | confidence=0.28 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:19] operator / voice_transcript_partial / voice: do
  meta: kind=partial | timestamp=1777918099.0773416 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:19] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777918099.2819753 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:19] operator / voice_transcript_partial / voice: fifth and
  meta: kind=partial | timestamp=1777918099.5100305 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:20] operator / voice_transcript_final / voice: fifth and
  meta: kind=final | timestamp=1777918100.1124096 | source=final | confidence=0.46 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:29] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777918109.1130679 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:29] operator / voice_transcript_partial / voice: an
  meta: kind=partial | timestamp=1777918109.3175354 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:29] operator / voice_transcript_final / voice: an
  meta: kind=final | timestamp=1777918109.724482 | source=final | confidence=0.75 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:31] operator / voice_transcript_partial / voice: eight
  meta: kind=partial | timestamp=1777918111.3696406 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:31] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777918111.3696406 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:31] operator / voice_transcript_partial / voice: itch to
  meta: kind=partial | timestamp=1777918111.7694356 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:31] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777918111.9873748 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:32] operator / voice_transcript_final / voice: as
  meta: kind=final | timestamp=1777918112.176769 | source=final | confidence=0.14 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:32] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777918112.7916179 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:33] operator / voice_transcript_final / voice: of
  meta: kind=final | timestamp=1777918113.6220598 | source=final | confidence=0.68 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:35] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777918115.913491 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:37] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777918117.1174047 | source=final | confidence=0.85 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:47] operator / voice_transcript_partial / voice: as the
  meta: kind=partial | timestamp=1777918127.1799946 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:48] operator / voice_transcript_partial / voice: than one
  meta: kind=partial | timestamp=1777918128.1939743 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:08:49] operator / voice_transcript_final / voice: than one
  meta: kind=final | timestamp=1777918129.2322416 | source=final | confidence=0.44 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:09:32] operator / voice_transcript_partial / voice: in a
  meta: kind=partial | timestamp=1777918172.8915248 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:09:33] operator / voice_transcript_partial / voice: games
  meta: kind=partial | timestamp=1777918173.120829 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:09:35] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777918175.567626 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:09:41] operator / voice_transcript_partial / voice: half
  meta: kind=partial | timestamp=1777918181.5381904 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:09:41] operator / voice_transcript_partial / voice: of the
  meta: kind=partial | timestamp=1777918181.5431976 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:09:43] operator / voice_transcript_partial / voice: of the event he
  meta: kind=partial | timestamp=1777918183.1711771 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:09:43] operator / voice_transcript_final / voice: of the event he
  meta: kind=final | timestamp=1777918183.587816 | source=final | confidence=0.38 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:09:46] operator / voice_transcript_partial / voice: said
  meta: kind=partial | timestamp=1777918186.3975623 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:03] operator / voice_transcript_partial / voice: and the
  meta: kind=partial | timestamp=1777918203.0964968 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:03] operator / voice_transcript_partial / voice: and the two
  meta: kind=partial | timestamp=1777918203.9301383 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:04] operator / voice_transcript_partial / voice: and it's
  meta: kind=partial | timestamp=1777918204.115341 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:04] operator / voice_transcript_final / voice: and it s
  meta: kind=final | timestamp=1777918204.986521 | source=final | confidence=0.72 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:09] operator / voice_transcript_partial / voice: here to
  meta: kind=partial | timestamp=1777918209.4465058 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:09] operator / voice_transcript_partial / voice: he was
  meta: kind=partial | timestamp=1777918209.6514335 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:10] operator / voice_transcript_final / voice: he was
  meta: kind=final | timestamp=1777918210.5051196 | source=final | confidence=0.4 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:11] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777918211.083665 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:11] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777918211.9111478 | source=final | confidence=0.42 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:22] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777918222.2816918 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:22] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777918222.4671638 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:23] operator / voice_transcript_final / voice: fifth
  meta: kind=final | timestamp=1777918223.54646 | source=final | confidence=0.28 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:33] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777918233.2595382 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:33] operator / voice_transcript_final / voice: and
  meta: kind=final | timestamp=1777918233.7691405 | source=final | confidence=0.47 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:37] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777918237.3846674 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:38] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777918238.189706 | source=final | confidence=0.86 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:39] operator / voice_transcript_partial / voice: set
  meta: kind=partial | timestamp=1777918239.8458314 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:43] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777918243.0993571 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:44] operator / voice_transcript_partial / voice: the the high
  meta: kind=partial | timestamp=1777918244.9094164 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:45] operator / voice_transcript_final / voice: the the high
  meta: kind=final | timestamp=1777918245.1971445 | source=final | confidence=0.55 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:50] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777918250.6224723 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:51] operator / voice_transcript_partial / voice: that the
  meta: kind=partial | timestamp=1777918251.4452567 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:51] operator / voice_transcript_final / voice: that the
  meta: kind=final | timestamp=1777918251.912767 | source=final | confidence=0.6 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:52] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777918252.4627676 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:55] operator / voice_transcript_partial / voice: use
  meta: kind=partial | timestamp=1777918255.7674818 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:55] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777918255.7674818 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:10:59] operator / voice_transcript_partial / voice: low
  meta: kind=partial | timestamp=1777918259.8800225 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:00] operator / voice_transcript_partial / voice: whole
  meta: kind=partial | timestamp=1777918260.0734751 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:00] operator / voice_transcript_partial / voice: only a
  meta: kind=partial | timestamp=1777918260.27789 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:00] operator / voice_transcript_partial / voice: white
  meta: kind=partial | timestamp=1777918260.470467 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:00] operator / voice_transcript_partial / voice: owners of the
  meta: kind=partial | timestamp=1777918260.6596956 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:02] operator / voice_transcript_partial / voice: lighting and
  meta: kind=partial | timestamp=1777918262.1021705 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:02] operator / voice_transcript_partial / voice: lighting of
  meta: kind=partial | timestamp=1777918262.2970307 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:02] operator / voice_transcript_final / voice: lighting of
  meta: kind=final | timestamp=1777918262.7850227 | source=final | confidence=0.04 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:04] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777918264.7583911 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:07] operator / voice_transcript_partial / voice: here
  meta: kind=partial | timestamp=1777918267.9857676 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:08] operator / voice_transcript_partial / voice: here in
  meta: kind=partial | timestamp=1777918268.1950634 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:08] operator / voice_transcript_partial / voice: here and
  meta: kind=partial | timestamp=1777918268.4120617 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:09] operator / voice_transcript_final / voice: here and
  meta: kind=final | timestamp=1777918269.2817464 | source=final | confidence=0.62 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:10] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777918270.0387113 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:15] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777918275.7674315 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:16] operator / voice_transcript_partial / voice: have
  meta: kind=partial | timestamp=1777918276.177655 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:16] operator / voice_transcript_partial / voice: there are
  meta: kind=partial | timestamp=1777918276.3976583 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:16] operator / voice_transcript_partial / voice: another one
  meta: kind=partial | timestamp=1777918276.5702963 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:17] operator / voice_transcript_final / voice: another one
  meta: kind=final | timestamp=1777918277.3979897 | source=final | confidence=0.15 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:18] operator / voice_transcript_partial / voice: i
  meta: kind=partial | timestamp=1777918278.2083035 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:18] operator / voice_transcript_partial / voice: -
  meta: kind=partial | timestamp=1777918278.6275089 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:18] operator / voice_transcript_partial / voice: day in
  meta: kind=partial | timestamp=1777918278.8258784 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:19] operator / voice_transcript_partial / voice: -day when
  meta: kind=partial | timestamp=1777918279.4598536 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:19] operator / voice_transcript_partial / voice: -day when in the
  meta: kind=partial | timestamp=1777918279.8674366 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:20] operator / voice_transcript_partial / voice: -day when it has
  meta: kind=partial | timestamp=1777918280.0518875 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:20] operator / voice_transcript_partial / voice: five in the media have
  meta: kind=partial | timestamp=1777918280.4479754 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:21] operator / voice_transcript_final / voice: five in the media have
  meta: kind=final | timestamp=1777918281.393045 | source=final | confidence=0.05 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:22] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777918282.9157236 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:23] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777918283.3409407 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:24] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777918284.15671 | source=final | confidence=0.61 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:25] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777918285.7858617 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:25] operator / voice_transcript_partial / voice: oven and
  meta: kind=partial | timestamp=1777918285.9881542 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:26] operator / voice_transcript_final / voice: oven and
  meta: kind=final | timestamp=1777918286.8253007 | source=final | confidence=0.51 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:27] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777918287.2104774 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:28] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777918288.1609812 | source=final | confidence=0.84 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:29] operator / voice_transcript_partial / voice: use
  meta: kind=partial | timestamp=1777918289.2534835 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:29] operator / voice_transcript_partial / voice: use of
  meta: kind=partial | timestamp=1777918289.454872 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:29] operator / voice_transcript_partial / voice: long
  meta: kind=partial | timestamp=1777918289.660456 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:30] operator / voice_transcript_partial / voice: son of a
  meta: kind=partial | timestamp=1777918290.2898707 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:30] operator / voice_transcript_partial / voice: use of the only
  meta: kind=partial | timestamp=1777918290.48335 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:30] operator / voice_transcript_partial / voice: use of the only high
  meta: kind=partial | timestamp=1777918290.6916428 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:30] operator / voice_transcript_partial / voice: use of the only time the
  meta: kind=partial | timestamp=1777918290.8916273 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:31] operator / voice_transcript_partial / voice: use of the only time in the
  meta: kind=partial | timestamp=1777918291.915883 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:32] operator / voice_transcript_partial / voice: use of the only time in the name of the
  meta: kind=partial | timestamp=1777918292.7191007 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:32] operator / voice_transcript_partial / voice: use of the only time in the
  meta: kind=partial | timestamp=1777918292.9269717 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:33] operator / voice_transcript_final / voice: use of the only time in the
  meta: kind=final | timestamp=1777918293.3690293 | source=final | confidence=0.22 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:35] operator / voice_transcript_partial / voice: four
  meta: kind=partial | timestamp=1777918295.2009199 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:35] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777918295.3736882 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:35] operator / voice_transcript_partial / voice: fall in
  meta: kind=partial | timestamp=1777918295.9889755 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:36] operator / voice_transcript_partial / voice: fall in our
  meta: kind=partial | timestamp=1777918296.600091 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:37] operator / voice_transcript_partial / voice: fall in love
  meta: kind=partial | timestamp=1777918297.236181 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:37] operator / voice_transcript_partial / voice: fall in love or
  meta: kind=partial | timestamp=1777918297.6214445 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:38] operator / voice_transcript_partial / voice: fall in love or you
  meta: kind=partial | timestamp=1777918298.643921 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:39] operator / voice_transcript_final / voice: fall in love or you
  meta: kind=final | timestamp=1777918299.440598 | source=final | confidence=0.35 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:39] operator / voice_transcript_partial / voice: may
  meta: kind=partial | timestamp=1777918299.6416926 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:39] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777918299.863199 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:40] operator / voice_transcript_partial / voice: get out
  meta: kind=partial | timestamp=1777918300.4784098 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:40] operator / voice_transcript_partial / voice: get out of
  meta: kind=partial | timestamp=1777918300.6710207 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:41] operator / voice_transcript_final / voice: get out of
  meta: kind=final | timestamp=1777918301.3484478 | source=final | confidence=0.18 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:42] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777918302.7361686 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:44] operator / voice_transcript_partial / voice: high
  meta: kind=partial | timestamp=1777918304.2327697 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:44] operator / voice_transcript_partial / voice: his
  meta: kind=partial | timestamp=1777918304.4249642 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:44] operator / voice_transcript_partial / voice: one of the
  meta: kind=partial | timestamp=1777918304.805592 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:46] operator / voice_transcript_final / voice: one of the
  meta: kind=final | timestamp=1777918306.0660503 | source=final | confidence=0.3 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:48] operator / voice_transcript_partial / voice: high
  meta: kind=partial | timestamp=1777918308.253708 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:48] operator / voice_transcript_partial / voice: now
  meta: kind=partial | timestamp=1777918308.254706 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:57] operator / voice_transcript_partial / voice: be
  meta: kind=partial | timestamp=1777918317.4787285 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:57] operator / voice_transcript_partial / voice: main
  meta: kind=partial | timestamp=1777918317.6648192 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:11:59] operator / voice_transcript_final / voice: main
  meta: kind=final | timestamp=1777918319.0024548 | source=final | confidence=0.8 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:01] operator / voice_transcript_partial / voice: may
  meta: kind=partial | timestamp=1777918321.158352 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:01] operator / voice_transcript_partial / voice: main
  meta: kind=partial | timestamp=1777918321.3806448 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:02] operator / voice_transcript_partial / voice: main main
  meta: kind=partial | timestamp=1777918322.4058063 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:03] operator / voice_transcript_final / voice: main main
  meta: kind=final | timestamp=1777918323.2893298 | source=final | confidence=0.45 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:09] operator / voice_transcript_partial / voice: main
  meta: kind=partial | timestamp=1777918329.693326 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:10] operator / voice_transcript_partial / voice: main main
  meta: kind=partial | timestamp=1777918330.079596 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:11] operator / voice_transcript_final / voice: main main
  meta: kind=final | timestamp=1777918331.0124524 | source=final | confidence=0.33 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:13] operator / voice_transcript_partial / voice: to the
  meta: kind=partial | timestamp=1777918333.793071 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:13] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777918333.9811523 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:14] operator / voice_transcript_partial / voice: to the
  meta: kind=partial | timestamp=1777918334.207278 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:14] operator / voice_transcript_final / voice: to the
  meta: kind=final | timestamp=1777918334.8812091 | source=final | confidence=0.26 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:15] operator / voice_transcript_partial / voice: run
  meta: kind=partial | timestamp=1777918335.3983197 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:16] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777918336.2406642 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:16] operator / voice_transcript_partial / voice: u.n.
  meta: kind=partial | timestamp=1777918336.4185495 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:16] operator / voice_transcript_partial / voice: one in
  meta: kind=partial | timestamp=1777918336.642645 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:17] operator / voice_transcript_partial / voice: one you've seen
  meta: kind=partial | timestamp=1777918337.0421774 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:18] operator / voice_transcript_partial / voice: one you've seen as
  meta: kind=partial | timestamp=1777918338.4592204 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:19] operator / voice_transcript_partial / voice: one you've seen as the
  meta: kind=partial | timestamp=1777918339.0792084 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:19] operator / voice_transcript_partial / voice: one you've seen as high as
  meta: kind=partial | timestamp=1777918339.4942644 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:20] operator / voice_transcript_partial / voice: one you have to see us as
  meta: kind=partial | timestamp=1777918340.1389103 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:20] operator / voice_transcript_partial / voice: one you have to see us as the
  meta: kind=partial | timestamp=1777918340.3164384 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:20] operator / voice_transcript_partial / voice: one you have to see us as the the
  meta: kind=partial | timestamp=1777918340.9469151 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:21] operator / voice_transcript_partial / voice: one you have to see us as the of the
  meta: kind=partial | timestamp=1777918341.1619074 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:22] operator / voice_transcript_partial / voice: one you have to see us as the the name of
  meta: kind=partial | timestamp=1777918342.1697018 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:22] operator / voice_transcript_partial / voice: one you have to see us as the the the the
  meta: kind=partial | timestamp=1777918342.574815 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:22] operator / voice_transcript_final / voice: one you have to see us as the the the the
  meta: kind=final | timestamp=1777918342.8728452 | source=final | confidence=0.43 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:30] operator / voice_transcript_partial / voice: law
  meta: kind=partial | timestamp=1777918350.1490996 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:30] operator / voice_transcript_partial / voice: long
  meta: kind=partial | timestamp=1777918350.5332727 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:30] operator / voice_transcript_partial / voice: one he
  meta: kind=partial | timestamp=1777918350.7588463 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:32] operator / voice_transcript_final / voice: one he
  meta: kind=final | timestamp=1777918352.1897385 | source=final | confidence=0.45 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:32] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777918352.3548381 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:32] operator / voice_transcript_partial / voice: and the
  meta: kind=partial | timestamp=1777918352.9903219 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:33] operator / voice_transcript_final / voice: and the
  meta: kind=final | timestamp=1777918353.7079017 | source=final | confidence=0.6 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:56] operator / voice_transcript_partial / voice: hot
  meta: kind=partial | timestamp=1777918376.0177183 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:12:57] operator / voice_transcript_final / voice: hot
  meta: kind=final | timestamp=1777918377.4201252 | source=final | confidence=0.03 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:13:02] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777918382.1451604 | source=windows | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466
- [2026-05-05 02:13:02] operator / voice_transcript_final / voice: as
  meta: kind=final | timestamp=1777918382.8255606 | source=final | confidence=0.71 | frequency_hz=410.2 | rms=145 | updated_at=1777917748.5561466

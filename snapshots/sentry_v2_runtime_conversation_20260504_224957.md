# SMART SENTRY V3.5.3 Runtime Conversation Export

- Generated: 2026-05-04 22:49:57
- Entries: 612
- Roles: {'assistant': 47, 'system': 1, 'operator': 564}
- Event types: {'assistant_prompt': 5, 'assistant_analysis': 1, 'voice_status': 1, 'voice_transcript_partial': 444, 'voice_transcript_final': 74, 'voice_command': 46, 'spoken_confirmation': 41}
- Channels: {'text': 6, 'voice': 606}
- Latest operator request: what else can you do
- Latest assistant message: I think I heard what else can you do. Say yes if that is correct, say it again, or say cancel.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-04 22:41:51] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 22:41:51] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-04 22:41:53] system / voice_status / voice: listening
  meta: kind=status | timestamp=1777905713.410968 | source=windows
- [2026-05-04 22:41:58] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777905718.1501179 | source=windows
- [2026-05-04 22:41:58] operator / voice_transcript_partial / voice: his
  meta: kind=partial | timestamp=1777905718.3647919 | source=windows
- [2026-05-04 22:41:58] operator / voice_transcript_partial / voice: the zones
  meta: kind=partial | timestamp=1777905718.7974367 | source=windows
- [2026-05-04 22:41:59] operator / voice_transcript_partial / voice: his son
  meta: kind=partial | timestamp=1777905719.202915 | source=windows
- [2026-05-04 22:41:59] operator / voice_transcript_partial / voice: as soon as
  meta: kind=partial | timestamp=1777905719.6039505 | source=windows
- [2026-05-04 22:42:00] operator / voice_transcript_partial / voice: as soon as he has
  meta: kind=partial | timestamp=1777905720.425634 | source=windows
- [2026-05-04 22:42:01] operator / voice_transcript_final / voice: as soon as he has
  meta: kind=final | timestamp=1777905721.4625456 | source=final | confidence=0.15
- [2026-05-04 22:42:03] operator / voice_transcript_partial / voice: been
  meta: kind=partial | timestamp=1777905723.3081207 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:03] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777905723.5130262 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:03] operator / voice_transcript_partial / voice: a clinical
  meta: kind=partial | timestamp=1777905723.713606 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:03] operator / voice_transcript_partial / voice: a clinic was
  meta: kind=partial | timestamp=1777905723.9180286 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:04] operator / voice_transcript_final / voice: a clinic was
  meta: kind=final | timestamp=1777905724.7649257 | source=final | confidence=0.64 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:04] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777905724.965139 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:04] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777905724.965139 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:05] operator / voice_transcript_partial / voice: able
  meta: kind=partial | timestamp=1777905725.5737178 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:05] operator / voice_transcript_partial / voice: enabled us
  meta: kind=partial | timestamp=1777905725.7761629 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:05] operator / voice_transcript_partial / voice: enable smart
  meta: kind=partial | timestamp=1777905725.9795072 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:06] operator / voice_transcript_partial / voice: enabled the smarts
  meta: kind=partial | timestamp=1777905726.3860383 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:06] operator / voice_transcript_partial / voice: enable smart sentry
  meta: kind=partial | timestamp=1777905726.5873845 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:06] operator / voice_transcript_final / voice: enable smart sentry
  meta: kind=final | timestamp=1777905726.9938207 | source=final | confidence=0.82 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:31] operator / voice_command / voice: enable smart sentry
  meta: normalized=True
- [2026-05-04 22:42:12] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777905732.695164 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:15] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777905735.9952962 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:31] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 22:42:16] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777905736.399275 | source=final | confidence=0.94 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:29] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777905749.436813 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:30] operator / voice_transcript_final / voice: as
  meta: kind=final | timestamp=1777905750.454387 | source=final | confidence=0.84 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:31] assistant / spoken_confirmation / voice: Enabling Smart Sentry now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:42:33] operator / voice_transcript_partial / voice: its
  meta: kind=partial | timestamp=1777905753.7379565 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:33] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777905753.9428253 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:34] operator / voice_transcript_partial / voice: cd
  meta: kind=partial | timestamp=1777905754.1438305 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:34] operator / voice_transcript_partial / voice: you
  meta: kind=partial | timestamp=1777905754.3504512 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:34] operator / voice_transcript_partial / voice: cd has
  meta: kind=partial | timestamp=1777905754.552965 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:34] operator / voice_transcript_partial / voice: cd has been
  meta: kind=partial | timestamp=1777905754.7545087 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:35] operator / voice_transcript_partial / voice: cd has more
  meta: kind=partial | timestamp=1777905755.1613553 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:35] operator / voice_transcript_partial / voice: cd has you have
  meta: kind=partial | timestamp=1777905755.3637373 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:36] operator / voice_transcript_final / voice: cd has you have
  meta: kind=final | timestamp=1777905756.5986784 | source=final | confidence=0.42 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:36] operator / voice_command / voice: cd has you have
  meta: normalized=True
- [2026-05-04 22:42:37] assistant / spoken_confirmation / voice: I think I heard cd has you have. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:42:39] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777905759.8684905 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:40] operator / voice_transcript_partial / voice: an
  meta: kind=partial | timestamp=1777905760.6761165 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:41] operator / voice_transcript_final / voice: an
  meta: kind=final | timestamp=1777905761.100737 | source=final | confidence=0.06 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:42] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777905762.3059154 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:48] operator / voice_transcript_partial / voice: eye
  meta: kind=partial | timestamp=1777905768.056617 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:48] operator / voice_transcript_partial / voice: eyes
  meta: kind=partial | timestamp=1777905768.262012 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:48] operator / voice_transcript_partial / voice: icy
  meta: kind=partial | timestamp=1777905768.4643655 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:48] operator / voice_transcript_partial / voice: icy clinic
  meta: kind=partial | timestamp=1777905768.669548 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:48] operator / voice_transcript_partial / voice: icy clinic that
  meta: kind=partial | timestamp=1777905768.8727727 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:49] operator / voice_transcript_partial / voice: icy clinic that was
  meta: kind=partial | timestamp=1777905769.0731485 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:49] operator / voice_transcript_partial / voice: icy clinic violence
  meta: kind=partial | timestamp=1777905769.6824226 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:42:50] operator / voice_transcript_final / voice: icy clinic violence
  meta: kind=final | timestamp=1777905770.297241 | source=final | confidence=0.43 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:02] operator / voice_transcript_partial / voice: is
  meta: kind=partial | timestamp=1777905782.138793 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:02] operator / voice_transcript_partial / voice: since
  meta: kind=partial | timestamp=1777905782.5438297 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:03] operator / voice_transcript_partial / voice: since its
  meta: kind=partial | timestamp=1777905783.3724036 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:04] operator / voice_transcript_partial / voice: since its own
  meta: kind=partial | timestamp=1777905784.1834276 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:04] operator / voice_transcript_final / voice: since its own
  meta: kind=final | timestamp=1777905784.3910546 | source=final | confidence=0.5 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:07] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777905787.2817876 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:07] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777905787.4867756 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:07] operator / voice_transcript_partial / voice: alien
  meta: kind=partial | timestamp=1777905787.6896453 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:07] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 22:43:07] operator / voice_transcript_final / voice: elion
  meta: kind=final | timestamp=1777905787.8927894 | source=final | confidence=0.94 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:11] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777905791.073602 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:11] operator / voice_transcript_partial / voice: use
  meta: kind=partial | timestamp=1777905791.2778761 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:11] operator / voice_transcript_partial / voice: museum
  meta: kind=partial | timestamp=1777905791.6835291 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:11] operator / voice_transcript_partial / voice: user
  meta: kind=partial | timestamp=1777905791.8858862 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:12] operator / voice_transcript_partial / voice: museum in
  meta: kind=partial | timestamp=1777905792.4946363 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:12] operator / voice_transcript_partial / voice: user to
  meta: kind=partial | timestamp=1777905792.6951497 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:13] operator / voice_transcript_final / voice: user to
  meta: kind=final | timestamp=1777905793.506465 | source=final | confidence=0.2 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:17] operator / voice_transcript_partial / voice: see
  meta: kind=partial | timestamp=1777905797.6227784 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:17] operator / voice_transcript_partial / voice: clean
  meta: kind=partial | timestamp=1777905797.6237838 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:17] operator / voice_transcript_partial / voice: clinic
  meta: kind=partial | timestamp=1777905797.8385453 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:18] operator / voice_transcript_partial / voice: clinic that
  meta: kind=partial | timestamp=1777905798.052764 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:18] operator / voice_transcript_partial / voice: connect boards
  meta: kind=partial | timestamp=1777905798.2548172 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:18] operator / voice_transcript_final / voice: connect boards
  meta: kind=final | timestamp=1777905798.8624377 | source=final | confidence=0.81 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:18] operator / voice_command / voice: connect boards
  meta: normalized=True
- [2026-05-04 22:43:19] assistant / spoken_confirmation / voice: Connecting Smart Sentry boards now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 22:43:19] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777905799.8695076 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:19] operator / voice_transcript_partial / voice: see
  meta: kind=partial | timestamp=1777905799.8695076 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:20] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777905800.2223268 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:21] operator / voice_transcript_final / voice: as
  meta: kind=final | timestamp=1777905801.0547333 | source=final | confidence=0.77 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:21] operator / voice_command / voice: as
  meta: normalized=True
- [2026-05-04 22:43:21] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777905801.0557382 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:21] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777905801.3529193 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:21] assistant / spoken_confirmation / voice: I think I heard as. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:43:22] operator / voice_transcript_final / voice: being
  meta: kind=final | timestamp=1777905802.206492 | source=final | confidence=0.13 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:23] operator / voice_transcript_partial / voice: she
  meta: kind=partial | timestamp=1777905803.422401 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:23] operator / voice_transcript_partial / voice: shot
  meta: kind=partial | timestamp=1777905803.422401 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:23] operator / voice_transcript_partial / voice: she has
  meta: kind=partial | timestamp=1777905803.422401 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:23] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777905803.6266563 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:24] operator / voice_transcript_partial / voice: she has seen
  meta: kind=partial | timestamp=1777905804.2471664 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:25] operator / voice_transcript_final / voice: she has seen
  meta: kind=final | timestamp=1777905805.0723586 | source=final | confidence=0.49 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:25] operator / voice_command / voice: she has seen
  meta: normalized=True
- [2026-05-04 22:43:25] assistant / spoken_confirmation / voice: I think I heard she has seen. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:43:26] operator / voice_transcript_partial / voice: his
  meta: kind=partial | timestamp=1777905806.3672132 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:27] operator / voice_transcript_partial / voice: as he
  meta: kind=partial | timestamp=1777905807.4122841 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:27] operator / voice_transcript_partial / voice: as a human
  meta: kind=partial | timestamp=1777905807.632494 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:29] operator / voice_transcript_final / voice: as a human
  meta: kind=final | timestamp=1777905809.3226857 | source=final | confidence=0.57 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:29] operator / voice_command / voice: as a human
  meta: normalized=True
- [2026-05-04 22:43:29] assistant / spoken_confirmation / voice: I think I heard as a human. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:43:30] operator / voice_transcript_partial / voice: in a
  meta: kind=partial | timestamp=1777905810.965236 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:30] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777905810.9659584 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:31] operator / voice_transcript_partial / voice: in the
  meta: kind=partial | timestamp=1777905811.304668 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:31] operator / voice_transcript_partial / voice: beings
  meta: kind=partial | timestamp=1777905811.5077922 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:31] operator / voice_transcript_partial / voice: enable the smart
  meta: kind=partial | timestamp=1777905811.709345 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:31] operator / voice_transcript_partial / voice: enable the smart sentry
  meta: kind=partial | timestamp=1777905811.9120255 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:32] operator / voice_transcript_final / voice: enable smart sentry
  meta: kind=final | timestamp=1777905812.878276 | source=final | confidence=0.83 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:33] operator / voice_command / voice: enable smart sentry
  meta: normalized=True
- [2026-05-04 22:43:33] assistant / spoken_confirmation / voice: Resuming Smart Sentry now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:43:35] operator / voice_transcript_partial / voice: chain
  meta: kind=partial | timestamp=1777905815.2102222 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:37] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777905817.2382476 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:37] operator / voice_transcript_partial / voice: in a
  meta: kind=partial | timestamp=1777905817.6648617 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:37] operator / voice_transcript_partial / voice: being able
  meta: kind=partial | timestamp=1777905817.8774261 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:38] operator / voice_transcript_partial / voice: in a believes
  meta: kind=partial | timestamp=1777905818.0809512 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:38] operator / voice_transcript_partial / voice: enable the smart
  meta: kind=partial | timestamp=1777905818.4870498 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:38] operator / voice_transcript_partial / voice: enabled the smarts in
  meta: kind=partial | timestamp=1777905818.7021754 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:38] operator / voice_transcript_partial / voice: enable the smart sentry
  meta: kind=partial | timestamp=1777905818.9051876 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:39] operator / voice_transcript_final / voice: enable smart sentry
  meta: kind=final | timestamp=1777905819.1081092 | source=final | confidence=0.67 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:39] operator / voice_command / voice: enable smart sentry
  meta: normalized=True
- [2026-05-04 22:43:39] assistant / spoken_confirmation / voice: I think I heard enable smart sentry. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:43:41] operator / voice_transcript_partial / voice: being
  meta: kind=partial | timestamp=1777905821.5619562 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:45] operator / voice_transcript_partial / voice: in the
  meta: kind=partial | timestamp=1777905825.438894 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:45] operator / voice_transcript_partial / voice: in u.s.
  meta: kind=partial | timestamp=1777905825.6642222 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:47] operator / voice_transcript_final / voice: in u s
  meta: kind=final | timestamp=1777905827.1850255 | source=final | confidence=0.66 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:47] operator / voice_command / voice: in u s
  meta: normalized=True
- [2026-05-04 22:43:47] operator / voice_transcript_partial / voice: as
  meta: kind=partial | timestamp=1777905827.3267484 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:47] operator / voice_transcript_partial / voice: has yet
  meta: kind=partial | timestamp=1777905827.7321622 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:48] operator / voice_transcript_partial / voice: yes
  meta: kind=partial | timestamp=1777905828.1494727 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:48] operator / voice_transcript_final / voice: yes
  meta: kind=final | timestamp=1777905828.60831 | source=final | confidence=0.95 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:48] operator / voice_command / voice: yes
  meta: normalized=True
- [2026-05-04 22:43:49] assistant / spoken_confirmation / voice: Received. I started your assistant request about in u s in the background.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 22:43:49] assistant / spoken_confirmation / voice: I think I heard in u s. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 22:43:50] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777905830.6911647 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:50] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777905830.9044237 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:51] operator / voice_transcript_partial / voice: plane
  meta: kind=partial | timestamp=1777905831.1070523 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:51] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777905831.3082323 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:51] operator / voice_transcript_partial / voice: v. f.
  meta: kind=partial | timestamp=1777905831.513826 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:43:53] operator / voice_transcript_final / voice: vf
  meta: kind=final | timestamp=1777905833.6936646 | source=final | confidence=0.22 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:02] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777905842.5181427 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:02] operator / voice_transcript_partial / voice: in a
  meta: kind=partial | timestamp=1777905842.7379873 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:03] operator / voice_transcript_partial / voice: in able
  meta: kind=partial | timestamp=1777905843.1247096 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:03] operator / voice_transcript_partial / voice: enabled this
  meta: kind=partial | timestamp=1777905843.1247096 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:03] operator / voice_transcript_partial / voice: enable the smart
  meta: kind=partial | timestamp=1777905843.766212 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:03] operator / voice_transcript_partial / voice: enabled the smarts in
  meta: kind=partial | timestamp=1777905843.7667227 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:04] operator / voice_transcript_partial / voice: enable the smart sentry
  meta: kind=partial | timestamp=1777905844.6138132 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:04] operator / voice_transcript_final / voice: enable smart sentry
  meta: kind=final | timestamp=1777905844.6153526 | source=final | confidence=0.81 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:04] operator / voice_command / voice: enable smart sentry
  meta: normalized=True
- [2026-05-04 22:44:05] assistant / spoken_confirmation / voice: Resuming Smart Sentry now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 22:44:06] operator / voice_transcript_partial / voice: lee
  meta: kind=partial | timestamp=1777905846.9423938 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:06] operator / voice_transcript_partial / voice: she
  meta: kind=partial | timestamp=1777905846.9454033 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:08] operator / voice_transcript_final / voice: she
  meta: kind=final | timestamp=1777905848.311761 | source=final | confidence=0.45 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:08] operator / voice_command / voice: she
  meta: normalized=True
- [2026-05-04 22:44:08] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777905848.3253381 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:08] operator / voice_transcript_partial / voice: may
  meta: kind=partial | timestamp=1777905848.3253381 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:08] operator / voice_transcript_partial / voice: named
  meta: kind=partial | timestamp=1777905848.3258462 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:09] assistant / spoken_confirmation / voice: I think I heard she. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 22:44:09] operator / voice_transcript_partial / voice: named on
  meta: kind=partial | timestamp=1777905849.0733752 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:09] operator / voice_transcript_partial / voice: gained more than
  meta: kind=partial | timestamp=1777905849.88475 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:11] operator / voice_transcript_partial / voice: name and move
  meta: kind=partial | timestamp=1777905851.3397417 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:13] operator / voice_transcript_partial / voice: gained enough to say
  meta: kind=partial | timestamp=1777905853.402754 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:14] operator / voice_transcript_partial / voice: gained more than half
  meta: kind=partial | timestamp=1777905854.5417435 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:14] operator / voice_transcript_partial / voice: gained enough to say
  meta: kind=partial | timestamp=1777905854.5426314 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:14] operator / voice_transcript_final / voice: gained enough to say
  meta: kind=final | timestamp=1777905854.550555 | source=final | confidence=0.33 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:14] operator / voice_command / voice: gained enough to say
  meta: normalized=True
- [2026-05-04 22:44:14] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777905854.5516355 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:15] assistant / spoken_confirmation / voice: I think I heard gained enough to say. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:44:15] operator / voice_transcript_partial / voice: he is the
  meta: kind=partial | timestamp=1777905855.4972637 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:20] operator / voice_transcript_final / voice: he is the
  meta: kind=final | timestamp=1777905860.8422377 | source=final | confidence=0.26 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:20] operator / voice_command / voice: he is the
  meta: normalized=True
- [2026-05-04 22:44:20] operator / voice_transcript_partial / voice: end of
  meta: kind=partial | timestamp=1777905860.843238 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:20] operator / voice_transcript_partial / voice: fifth
  meta: kind=partial | timestamp=1777905860.843238 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:20] operator / voice_transcript_final / voice: fifth
  meta: kind=final | timestamp=1777905860.8442385 | source=final | confidence=0.48 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:20] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777905860.8442385 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:20] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777905860.8442385 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:21] operator / voice_transcript_partial / voice: to say
  meta: kind=partial | timestamp=1777905861.0650356 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:21] operator / voice_transcript_partial / voice: kid stays
  meta: kind=partial | timestamp=1777905861.0650356 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:21] assistant / spoken_confirmation / voice: I think I heard he is the. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:44:22] operator / voice_transcript_partial / voice: kid stays in
  meta: kind=partial | timestamp=1777905862.3166919 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:22] operator / voice_transcript_partial / voice: kid stays in the
  meta: kind=partial | timestamp=1777905862.3166919 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:22] operator / voice_transcript_partial / voice: kid stays in asia
  meta: kind=partial | timestamp=1777905862.3181963 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:22] operator / voice_transcript_partial / voice: kid stays the same
  meta: kind=partial | timestamp=1777905862.3181963 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:22] operator / voice_transcript_partial / voice: kid stays the same way
  meta: kind=partial | timestamp=1777905862.7705023 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:23] operator / voice_transcript_partial / voice: kid stays the same one
  meta: kind=partial | timestamp=1777905863.476914 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:25] operator / voice_transcript_final / voice: kid stays the same one
  meta: kind=final | timestamp=1777905865.75212 | source=final | confidence=0.29 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:25] operator / voice_command / voice: kid stays the same one
  meta: normalized=True
- [2026-05-04 22:44:26] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777905866.1841092 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:26] assistant / spoken_confirmation / voice: I think I heard kid stays the same one. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:44:26] operator / voice_transcript_partial / voice: he has
  meta: kind=partial | timestamp=1777905866.9833686 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:28] operator / voice_transcript_final / voice: he has
  meta: kind=final | timestamp=1777905868.8784738 | source=final | confidence=0.04 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:28] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777905868.8784738 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:31] operator / voice_transcript_partial / voice: seen the
  meta: kind=partial | timestamp=1777905871.0787005 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:31] operator / voice_transcript_partial / voice: seven-
  meta: kind=partial | timestamp=1777905871.0787005 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:31] operator / voice_transcript_partial / voice: seen the
  meta: kind=partial | timestamp=1777905871.0787005 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:32] operator / voice_transcript_partial / voice: to have as
  meta: kind=partial | timestamp=1777905872.6586492 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:33] operator / voice_transcript_final / voice: to have as
  meta: kind=final | timestamp=1777905873.297036 | source=final | confidence=0.11 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:33] operator / voice_command / voice: to have as
  meta: normalized=True
- [2026-05-04 22:44:34] assistant / spoken_confirmation / voice: I think I heard to have as. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:44:34] operator / voice_transcript_partial / voice: an
  meta: kind=partial | timestamp=1777905874.054144 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:34] operator / voice_transcript_partial / voice: enable
  meta: kind=partial | timestamp=1777905874.054144 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:35] operator / voice_transcript_partial / voice: enables
  meta: kind=partial | timestamp=1777905875.2066352 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:36] operator / voice_transcript_partial / voice: enable the smart
  meta: kind=partial | timestamp=1777905876.1157033 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:36] operator / voice_transcript_partial / voice: enable the smart sentry
  meta: kind=partial | timestamp=1777905876.1172106 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:37] operator / voice_transcript_final / voice: enable smart sentry
  meta: kind=final | timestamp=1777905877.4656932 | source=final | confidence=0.63 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:37] operator / voice_command / voice: enable smart sentry
  meta: normalized=True
- [2026-05-04 22:44:37] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777905877.9357312 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:37] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777905877.9357312 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:37] operator / voice_transcript_partial / voice: in a
  meta: kind=partial | timestamp=1777905877.9362347 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:38] operator / voice_transcript_partial / voice: enabled
  meta: kind=partial | timestamp=1777905878.206158 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:38] operator / voice_transcript_partial / voice: enables
  meta: kind=partial | timestamp=1777905878.2096717 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:38] operator / voice_transcript_partial / voice: enabled the smarts
  meta: kind=partial | timestamp=1777905878.2096717 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:38] operator / voice_transcript_partial / voice: enable the smart sentry
  meta: kind=partial | timestamp=1777905878.2096717 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:38] assistant / spoken_confirmation / voice: I think I heard enable smart sentry. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:44:39] operator / voice_transcript_final / voice: enable smart sentry
  meta: kind=final | timestamp=1777905879.0159035 | source=final | confidence=0.84 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:39] operator / voice_command / voice: enable smart sentry
  meta: normalized=True
- [2026-05-04 22:44:39] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777905879.016907 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:39] operator / voice_transcript_partial / voice: high as
  meta: kind=partial | timestamp=1777905879.016907 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:39] operator / voice_transcript_partial / voice: high as the
  meta: kind=partial | timestamp=1777905879.016907 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:39] operator / voice_transcript_partial / voice: fast as
  meta: kind=partial | timestamp=1777905879.016907 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:39] operator / voice_transcript_final / voice: fast as
  meta: kind=final | timestamp=1777905879.0184097 | source=final | confidence=0.17 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:39] assistant / spoken_confirmation / voice: Resuming Smart Sentry now.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:44:40] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777905880.4847424 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:41] operator / voice_transcript_partial / voice: they
  meta: kind=partial | timestamp=1777905881.075143 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:41] operator / voice_transcript_partial / voice: many as
  meta: kind=partial | timestamp=1777905881.3876982 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:42] operator / voice_transcript_partial / voice: many as the
  meta: kind=partial | timestamp=1777905882.9315464 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:42] operator / voice_transcript_partial / voice: many as a
  meta: kind=partial | timestamp=1777905882.932546 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:42] operator / voice_transcript_partial / voice: many as he
  meta: kind=partial | timestamp=1777905882.932546 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:43] operator / voice_transcript_partial / voice: many as he is
  meta: kind=partial | timestamp=1777905883.1328216 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:46] operator / voice_transcript_final / voice: many as he is
  meta: kind=final | timestamp=1777905886.0906527 | source=final | confidence=0.24 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:46] operator / voice_command / voice: many as he is
  meta: normalized=True
- [2026-05-04 22:44:46] operator / voice_transcript_partial / voice: sure
  meta: kind=partial | timestamp=1777905886.0916545 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:46] operator / voice_transcript_partial / voice: flat
  meta: kind=partial | timestamp=1777905886.0916545 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:46] operator / voice_transcript_partial / voice: fluffy
  meta: kind=partial | timestamp=1777905886.0916545 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:46] operator / voice_transcript_partial / voice: fluffy in
  meta: kind=partial | timestamp=1777905886.0916545 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:46] operator / voice_transcript_partial / voice: funny when
  meta: kind=partial | timestamp=1777905886.0916545 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:46] operator / voice_transcript_partial / voice: funny enough
  meta: kind=partial | timestamp=1777905886.0916545 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:46] operator / voice_transcript_partial / voice: sure you have
  meta: kind=partial | timestamp=1777905886.0916545 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:46] operator / voice_transcript_partial / voice: funny enough
  meta: kind=partial | timestamp=1777905886.0916545 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:46] operator / voice_transcript_partial / voice: funny enough is
  meta: kind=partial | timestamp=1777905886.0931582 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:46] assistant / spoken_confirmation / voice: I think I heard many as he is. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:44:46] operator / voice_transcript_partial / voice: funny enough san
  meta: kind=partial | timestamp=1777905886.741045 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:46] operator / voice_transcript_partial / voice: funny enough since a
  meta: kind=partial | timestamp=1777905886.741045 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:46] operator / voice_transcript_partial / voice: funny enough simpson
  meta: kind=partial | timestamp=1777905886.7420456 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:46] operator / voice_transcript_final / voice: funny enough simpson
  meta: kind=final | timestamp=1777905886.743548 | source=final | confidence=0.1 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:46] operator / voice_command / voice: funny enough simpson
  meta: normalized=True
- [2026-05-04 22:44:47] assistant / spoken_confirmation / voice: I think I heard funny enough simpson. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:44:50] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777905890.536234 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:51] operator / voice_transcript_partial / voice: change
  meta: kind=partial | timestamp=1777905891.685802 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:51] operator / voice_transcript_partial / voice: of his
  meta: kind=partial | timestamp=1777905891.8913782 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:53] operator / voice_transcript_final / voice: of his
  meta: kind=final | timestamp=1777905893.4115179 | source=final | confidence=0.18 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:53] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 22:44:54] operator / voice_transcript_partial / voice: you
  meta: kind=partial | timestamp=1777905894.4499178 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:54] operator / voice_transcript_partial / voice: yes
  meta: kind=partial | timestamp=1777905894.4499178 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:54] operator / voice_transcript_partial / voice: u.s.
  meta: kind=partial | timestamp=1777905894.4514208 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:54] operator / voice_transcript_partial / voice: yes
  meta: kind=partial | timestamp=1777905894.4529421 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:54] operator / voice_transcript_final / voice: yes
  meta: kind=final | timestamp=1777905894.83315 | source=final | confidence=0.93 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:55] operator / voice_command / voice: yes
  meta: normalized=True
- [2026-05-04 22:44:55] assistant / spoken_confirmation / voice: Received. I started your assistant request about funny enough simpson in the background.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:44:56] operator / voice_transcript_partial / voice: you
  meta: kind=partial | timestamp=1777905896.4575522 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:57] operator / voice_transcript_partial / voice: u.s.
  meta: kind=partial | timestamp=1777905897.5672965 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:58] operator / voice_transcript_partial / voice: yes
  meta: kind=partial | timestamp=1777905898.2891939 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:58] operator / voice_transcript_final / voice: yes
  meta: kind=final | timestamp=1777905898.323366 | source=final | confidence=0.94 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:58] operator / voice_command / voice: yes
  meta: normalized=True
- [2026-05-04 22:44:58] assistant / assistant_prompt / text: Assistant request queued: assistant request about yes (position 1).
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 22:44:58] operator / voice_transcript_partial / voice: key
  meta: kind=partial | timestamp=1777905898.8192039 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:58] operator / voice_transcript_partial / voice: name
  meta: kind=partial | timestamp=1777905898.8192039 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:44:59] assistant / spoken_confirmation / voice: I am still finishing assistant request about funny enough simpson. I queued your assistant request about yes. It is number 1 in line.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:44:59] operator / voice_transcript_partial / voice: main
  meta: kind=partial | timestamp=1777905899.4488397 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:00] operator / voice_transcript_final / voice: main
  meta: kind=final | timestamp=1777905900.1678545 | source=final | confidence=0.51 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:00] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777905900.9220655 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:00] operator / voice_transcript_partial / voice: main
  meta: kind=partial | timestamp=1777905900.9276388 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:01] operator / voice_transcript_partial / voice: main main
  meta: kind=partial | timestamp=1777905901.5081065 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:02] operator / voice_transcript_final / voice: main main
  meta: kind=final | timestamp=1777905902.1947184 | source=final | confidence=0.62 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:10] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777905910.8529153 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:11] operator / voice_transcript_partial / voice: it's
  meta: kind=partial | timestamp=1777905911.5962873 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:11] operator / voice_transcript_partial / voice: in seattle
  meta: kind=partial | timestamp=1777905911.5962873 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:11] operator / voice_transcript_partial / voice: it's a little
  meta: kind=partial | timestamp=1777905911.5962873 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:11] operator / voice_transcript_partial / voice: it's the love lost
  meta: kind=partial | timestamp=1777905911.8123374 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:12] operator / voice_transcript_partial / voice: it's the love of us
  meta: kind=partial | timestamp=1777905912.3933733 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:13] operator / voice_transcript_final / voice: it s the love of us
  meta: kind=final | timestamp=1777905913.0193512 | source=final | confidence=0.65 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:15] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777905915.8217554 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:16] operator / voice_transcript_partial / voice: enable
  meta: kind=partial | timestamp=1777905916.4552033 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:16] operator / voice_transcript_partial / voice: enable the
  meta: kind=partial | timestamp=1777905916.67758 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:17] operator / voice_transcript_partial / voice: enable the smart
  meta: kind=partial | timestamp=1777905917.086235 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:17] operator / voice_transcript_partial / voice: enabled the smarts and
  meta: kind=partial | timestamp=1777905917.0897582 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:17] operator / voice_transcript_partial / voice: enable the smart sentry
  meta: kind=partial | timestamp=1777905917.3365645 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:18] operator / voice_transcript_final / voice: enable smart sentry
  meta: kind=final | timestamp=1777905918.169201 | source=final | confidence=0.87 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:18] operator / voice_command / voice: enable smart sentry
  meta: normalized=True
- [2026-05-04 22:45:19] assistant / spoken_confirmation / voice: Resuming Smart Sentry now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 22:45:19] operator / voice_transcript_partial / voice: she
  meta: kind=partial | timestamp=1777905919.9321768 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:20] operator / voice_transcript_partial / voice: change
  meta: kind=partial | timestamp=1777905920.5495143 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:21] operator / voice_transcript_partial / voice: change the
  meta: kind=partial | timestamp=1777905921.3778055 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:21] operator / voice_transcript_partial / voice: in a game
  meta: kind=partial | timestamp=1777905921.5877945 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:21] operator / voice_transcript_partial / voice: in a game where
  meta: kind=partial | timestamp=1777905921.874268 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:22] operator / voice_transcript_partial / voice: in a game
  meta: kind=partial | timestamp=1777905922.2804449 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:22] operator / voice_transcript_partial / voice: in a game-high
  meta: kind=partial | timestamp=1777905922.7255669 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:23] operator / voice_transcript_partial / voice: in a game where he
  meta: kind=partial | timestamp=1777905923.0722888 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:23] operator / voice_transcript_partial / voice: in a game-high
  meta: kind=partial | timestamp=1777905923.0732896 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:24] operator / voice_transcript_partial / voice: in a game-high as
  meta: kind=partial | timestamp=1777905924.5623012 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:24] operator / voice_transcript_partial / voice: in a game has
  meta: kind=partial | timestamp=1777905924.5623012 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:24] operator / voice_transcript_partial / voice: in a game-high as the
  meta: kind=partial | timestamp=1777905924.563815 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:25] operator / voice_transcript_final / voice: in a game high as the
  meta: kind=final | timestamp=1777905925.349243 | source=final | confidence=0.16 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:25] operator / voice_command / voice: in a game high as the
  meta: normalized=True
- [2026-05-04 22:45:25] operator / voice_transcript_partial / voice: guy
  meta: kind=partial | timestamp=1777905925.6165857 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:25] operator / voice_transcript_partial / voice: beach
  meta: kind=partial | timestamp=1777905925.6165857 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:25] operator / voice_transcript_partial / voice: beach and
  meta: kind=partial | timestamp=1777905925.8448827 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:26] assistant / spoken_confirmation / voice: I think I heard in a game high as the. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:45:26] operator / voice_transcript_partial / voice: reach of
  meta: kind=partial | timestamp=1777905926.4855058 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:26] operator / voice_transcript_final / voice: reach of
  meta: kind=final | timestamp=1777905926.8115253 | source=final | confidence=0.11 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:27] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777905927.945822 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:29] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777905929.991562 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:30] operator / voice_transcript_final / voice: a
  meta: kind=final | timestamp=1777905930.1970513 | source=final | confidence=0.71 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:30] operator / voice_command / voice: a
  meta: normalized=True
- [2026-05-04 22:45:31] assistant / spoken_confirmation / voice: I think I heard a. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:45:37] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777905937.981517 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:38] operator / voice_transcript_partial / voice: no
  meta: kind=partial | timestamp=1777905938.9491143 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:39] operator / voice_transcript_partial / voice: known as
  meta: kind=partial | timestamp=1777905939.45018 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:40] operator / voice_transcript_partial / voice: known as if
  meta: kind=partial | timestamp=1777905940.0591822 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:40] operator / voice_transcript_partial / voice: u.s.
  meta: kind=partial | timestamp=1777905940.0596838 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:40] operator / voice_transcript_final / voice: known as if
  meta: kind=final | timestamp=1777905940.957537 | source=final | confidence=0.34 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:41] operator / voice_command / voice: known as if
  meta: normalized=True
- [2026-05-04 22:45:41] assistant / spoken_confirmation / voice: I think I heard known as if. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:45:42] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777905942.3298602 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:42] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777905942.3298602 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:43] operator / voice_transcript_partial / voice: it is
  meta: kind=partial | timestamp=1777905943.4174056 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:43] operator / voice_transcript_partial / voice: the case as
  meta: kind=partial | timestamp=1777905943.4174056 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:44] operator / voice_transcript_partial / voice: it is a six
  meta: kind=partial | timestamp=1777905944.0591257 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:44] operator / voice_transcript_partial / voice: it is a sixteen
  meta: kind=partial | timestamp=1777905944.060129 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:44] operator / voice_transcript_partial / voice: it is a sixteen-
  meta: kind=partial | timestamp=1777905944.060129 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:44] operator / voice_transcript_partial / voice: the case as the same as a
  meta: kind=partial | timestamp=1777905944.060129 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:44] operator / voice_transcript_partial / voice: the case as the same as a sea of
  meta: kind=partial | timestamp=1777905944.3708513 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:44] operator / voice_transcript_partial / voice: the case as the same as a female
  meta: kind=partial | timestamp=1777905944.3718545 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:45] operator / voice_transcript_partial / voice: the case as the same as a similar
  meta: kind=partial | timestamp=1777905945.2123864 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:45] operator / voice_transcript_partial / voice: it is a safe place in the city has
  meta: kind=partial | timestamp=1777905945.9103372 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:46] operator / voice_transcript_partial / voice: it is a safe place in the city have any
  meta: kind=partial | timestamp=1777905946.1269796 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:47] operator / voice_transcript_final / voice: it is a safe place in the city have any
  meta: kind=final | timestamp=1777905947.8530765 | source=final | confidence=0.18 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:48] operator / voice_command / voice: it is a safe place in the city have any
  meta: normalized=True
- [2026-05-04 22:45:48] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777905948.3034601 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:48] operator / voice_transcript_partial / voice: case
  meta: kind=partial | timestamp=1777905948.510614 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:49] assistant / spoken_confirmation / voice: I think I heard it is a safe place in the city have any. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:45:51] operator / voice_transcript_final / voice: case
  meta: kind=final | timestamp=1777905951.085232 | source=final | confidence=0.42 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:51] operator / voice_command / voice: case
  meta: normalized=True
- [2026-05-04 22:45:51] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777905951.6459923 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:51] operator / voice_transcript_partial / voice: i
  meta: kind=partial | timestamp=1777905951.6469924 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:51] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777905951.8469105 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:52] assistant / spoken_confirmation / voice: I think I heard case. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:45:52] operator / voice_transcript_partial / voice: the mta's
  meta: kind=partial | timestamp=1777905952.9707654 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:53] operator / voice_transcript_partial / voice: i as a senate
  meta: kind=partial | timestamp=1777905953.3207796 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:54] operator / voice_transcript_partial / voice: i as a senator's
  meta: kind=partial | timestamp=1777905954.9357064 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:54] operator / voice_transcript_partial / voice: i as a senate-
  meta: kind=partial | timestamp=1777905954.936088 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:54] operator / voice_transcript_partial / voice: i as a senate-and
  meta: kind=partial | timestamp=1777905954.936591 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:55] operator / voice_transcript_partial / voice: i as a seven-nt
  meta: kind=partial | timestamp=1777905955.1649265 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:55] operator / voice_transcript_partial / voice: i as a seven-nt or
  meta: kind=partial | timestamp=1777905955.1649265 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:55] operator / voice_transcript_partial / voice: i as a seven-nt on
  meta: kind=partial | timestamp=1777905955.1649265 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:55] operator / voice_transcript_partial / voice: i as a seven-nt of
  meta: kind=partial | timestamp=1777905955.8848612 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:57] operator / voice_transcript_final / voice: i as a seven nt of
  meta: kind=final | timestamp=1777905957.7189586 | source=final | confidence=0.16 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:58] operator / voice_command / voice: i as a seven nt of
  meta: normalized=True
- [2026-05-04 22:45:57] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777905957.7249746 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:58] operator / voice_transcript_partial / voice: this
  meta: kind=partial | timestamp=1777905958.341537 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:58] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777905958.544861 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:58] operator / voice_transcript_partial / voice: this
  meta: kind=partial | timestamp=1777905958.544861 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:45:59] assistant / spoken_confirmation / voice: I think I heard i as a seven nt of. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:45:59] operator / voice_transcript_partial / voice: this as
  meta: kind=partial | timestamp=1777905959.1813278 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:00] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 22:46:01] operator / voice_transcript_final / voice: this as
  meta: kind=final | timestamp=1777905961.807582 | source=final | confidence=0.69 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:02] operator / voice_command / voice: this as
  meta: normalized=True
- [2026-05-04 22:46:02] assistant / spoken_confirmation / voice: I think I heard this as. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:46:04] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777905964.8562486 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:05] operator / voice_transcript_partial / voice: our
  meta: kind=partial | timestamp=1777905965.0613377 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:05] operator / voice_transcript_partial / voice: well as
  meta: kind=partial | timestamp=1777905965.267353 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:05] operator / voice_transcript_partial / voice: a liaison
  meta: kind=partial | timestamp=1777905965.4826171 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:05] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 22:46:06] operator / voice_transcript_partial / voice: well use of the
  meta: kind=partial | timestamp=1777905966.042308 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:06] operator / voice_transcript_partial / voice: well use of the u.s.
  meta: kind=partial | timestamp=1777905966.5380917 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:06] operator / voice_transcript_partial / voice: well use of the u.s. is
  meta: kind=partial | timestamp=1777905966.7732997 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:06] operator / voice_transcript_partial / voice: well use of the u.s. is the
  meta: kind=partial | timestamp=1777905966.9997094 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:08] operator / voice_transcript_final / voice: well use of the u s is the
  meta: kind=final | timestamp=1777905968.2379713 | source=final | confidence=0.35 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:08] operator / voice_command / voice: well use of the u s is the
  meta: normalized=True
- [2026-05-04 22:46:09] assistant / spoken_confirmation / voice: I think I heard well use of the u s is the. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:46:10] operator / voice_transcript_partial / voice: year
  meta: kind=partial | timestamp=1777905970.861872 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:11] operator / voice_transcript_partial / voice: yes
  meta: kind=partial | timestamp=1777905971.0695834 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:11] operator / voice_transcript_partial / voice: u.s. is
  meta: kind=partial | timestamp=1777905971.275994 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:11] operator / voice_transcript_partial / voice: u.s. has been
  meta: kind=partial | timestamp=1777905971.720912 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:11] operator / voice_transcript_final / voice: u s is
  meta: kind=final | timestamp=1777905971.9596734 | source=final | confidence=0.33 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:12] operator / voice_command / voice: u s is
  meta: normalized=True
- [2026-05-04 22:46:13] assistant / spoken_confirmation / voice: I think I heard u s is. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:46:16] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777905976.9518425 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:17] operator / voice_transcript_partial / voice: in the
  meta: kind=partial | timestamp=1777905977.3569489 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:17] operator / voice_transcript_partial / voice: in his
  meta: kind=partial | timestamp=1777905977.560145 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:18] operator / voice_transcript_final / voice: in his
  meta: kind=final | timestamp=1777905978.5975318 | source=final | confidence=0.48 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:18] operator / voice_command / voice: in his
  meta: normalized=True
- [2026-05-04 22:46:19] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777905979.017947 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:19] assistant / spoken_confirmation / voice: I think I heard in his. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:46:20] operator / voice_transcript_partial / voice: yes
  meta: kind=partial | timestamp=1777905980.1718738 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:20] operator / voice_transcript_partial / voice: u.s. use
  meta: kind=partial | timestamp=1777905980.632253 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:21] operator / voice_transcript_final / voice: u s use
  meta: kind=final | timestamp=1777905981.7516341 | source=final | confidence=0.66 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:21] operator / voice_command / voice: u s use
  meta: normalized=True
- [2026-05-04 22:46:22] assistant / spoken_confirmation / voice: I think I heard u s use. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:46:23] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777905983.2547755 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:23] operator / voice_transcript_partial / voice: less
  meta: kind=partial | timestamp=1777905983.5586288 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:23] operator / voice_transcript_partial / voice: less even
  meta: kind=partial | timestamp=1777905983.80828 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:24] operator / voice_transcript_partial / voice: policies
  meta: kind=partial | timestamp=1777905984.046248 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:24] operator / voice_transcript_final / voice: policies
  meta: kind=final | timestamp=1777905984.530037 | source=final | confidence=0.01 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:26] operator / voice_transcript_partial / voice: on
  meta: kind=partial | timestamp=1777905986.2296488 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:26] operator / voice_transcript_partial / voice: may
  meta: kind=partial | timestamp=1777905986.4638226 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:26] operator / voice_transcript_partial / voice: main
  meta: kind=partial | timestamp=1777905986.680063 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:26] operator / voice_transcript_partial / voice: name
  meta: kind=partial | timestamp=1777905986.9217856 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:27] operator / voice_transcript_partial / voice: name of
  meta: kind=partial | timestamp=1777905987.352204 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:28] operator / voice_transcript_partial / voice: of the wall
  meta: kind=partial | timestamp=1777905988.24671 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:28] operator / voice_transcript_partial / voice: name of why
  meta: kind=partial | timestamp=1777905988.487663 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:28] operator / voice_transcript_partial / voice: e lion
  meta: kind=partial | timestamp=1777905988.7342885 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:28] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 22:46:28] operator / voice_transcript_partial / voice: name of one of these
  meta: kind=partial | timestamp=1777905988.9691098 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:29] operator / voice_transcript_partial / voice: name of one days
  meta: kind=partial | timestamp=1777905989.1823406 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:29] operator / voice_transcript_partial / voice: name of one days ago
  meta: kind=partial | timestamp=1777905989.3864732 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:29] operator / voice_transcript_partial / voice: name of one days you're in
  meta: kind=partial | timestamp=1777905989.590765 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:29] operator / voice_transcript_partial / voice: name of one days you're in a
  meta: kind=partial | timestamp=1777905989.794011 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:30] operator / voice_transcript_partial / voice: name of one days your name
  meta: kind=partial | timestamp=1777905990.406901 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:31] operator / voice_transcript_final / voice: name of one days your name
  meta: kind=final | timestamp=1777905991.056188 | source=final | confidence=0.48 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:31] operator / voice_command / voice: name of one days your name
  meta: normalized=True
- [2026-05-04 22:46:31] assistant / spoken_confirmation / voice: I think I heard name of one days your name. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:46:33] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777905993.0698843 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:33] operator / voice_transcript_partial / voice: and a
  meta: kind=partial | timestamp=1777905993.0698843 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:33] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777905993.2676992 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:33] operator / voice_transcript_partial / voice: in the
  meta: kind=partial | timestamp=1777905993.7379658 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:34] operator / voice_transcript_partial / voice: in the one
  meta: kind=partial | timestamp=1777905994.485805 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:34] operator / voice_transcript_partial / voice: in the legacy
  meta: kind=partial | timestamp=1777905994.7219234 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:34] operator / voice_transcript_partial / voice: in lights in a
  meta: kind=partial | timestamp=1777905994.9718258 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:35] operator / voice_transcript_partial / voice: in lights in
  meta: kind=partial | timestamp=1777905995.4393559 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:36] operator / voice_transcript_final / voice: in lights in
  meta: kind=final | timestamp=1777905996.1180024 | source=final | confidence=0.1 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:36] operator / voice_command / voice: in lights in
  meta: normalized=True
- [2026-05-04 22:46:37] assistant / spoken_confirmation / voice: I think I heard in lights in. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:46:42] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777906002.504872 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:43] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777906003.0069048 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:43] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777906003.3950176 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:43] operator / voice_transcript_partial / voice: game one
  meta: kind=partial | timestamp=1777906003.849264 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:44] operator / voice_transcript_partial / voice: the log
  meta: kind=partial | timestamp=1777906004.0538824 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:44] operator / voice_transcript_partial / voice: the log in
  meta: kind=partial | timestamp=1777906004.4852483 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:44] operator / voice_transcript_partial / voice: game one of these
  meta: kind=partial | timestamp=1777906004.6947086 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:44] operator / voice_transcript_partial / voice: the long as you
  meta: kind=partial | timestamp=1777906004.9149418 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:45] operator / voice_transcript_partial / voice: the long as you're
  meta: kind=partial | timestamp=1777906005.1236992 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:45] operator / voice_transcript_partial / voice: the long as your name
  meta: kind=partial | timestamp=1777906005.3758998 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:45] operator / voice_transcript_partial / voice: the long as your name or
  meta: kind=partial | timestamp=1777906005.9783285 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:46] operator / voice_transcript_partial / voice: the long as your main worry
  meta: kind=partial | timestamp=1777906006.1800587 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:46] operator / voice_transcript_partial / voice: the long as you are a lot easier
  meta: kind=partial | timestamp=1777906006.6012335 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:46] operator / voice_transcript_partial / voice: the long as your name or a survey
  meta: kind=partial | timestamp=1777906006.81464 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:47] operator / voice_transcript_partial / voice: the long as your name or eighty seven eight
  meta: kind=partial | timestamp=1777906007.0317054 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:47] operator / voice_transcript_partial / voice: the long as your name or the same age as
  meta: kind=partial | timestamp=1777906007.445052 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:48] operator / voice_transcript_final / voice: the long as your name or the same age as
  meta: kind=final | timestamp=1777906008.8856063 | source=final | confidence=0.41 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:48] operator / voice_command / voice: the long as your name or the same age as
  meta: normalized=True
- [2026-05-04 22:46:48] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777906008.8856063 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:49] operator / voice_transcript_partial / voice: these
  meta: kind=partial | timestamp=1777906009.0866747 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:49] assistant / spoken_confirmation / voice: I think I heard the long as your name or the same age as. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:46:49] operator / voice_transcript_final / voice: these
  meta: kind=final | timestamp=1777906009.703988 | source=final | confidence=0.65 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:51] operator / voice_transcript_partial / voice: may
  meta: kind=partial | timestamp=1777906011.9101076 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:51] operator / voice_transcript_partial / voice: e
  meta: kind=partial | timestamp=1777906011.9106107 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:53] operator / voice_transcript_partial / voice: she
  meta: kind=partial | timestamp=1777906013.7956192 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:54] operator / voice_transcript_partial / voice: she was
  meta: kind=partial | timestamp=1777906014.4054527 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:54] operator / voice_transcript_partial / voice: she was a
  meta: kind=partial | timestamp=1777906014.6280227 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:54] operator / voice_transcript_partial / voice: shows as the
  meta: kind=partial | timestamp=1777906014.8881166 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:55] operator / voice_transcript_partial / voice: shows as many as
  meta: kind=partial | timestamp=1777906015.819945 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:46:56] operator / voice_transcript_final / voice: shows as the
  meta: kind=final | timestamp=1777906016.0625322 | source=final | confidence=0.28 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:47:00] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777906020.112672 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:47:00] operator / voice_transcript_partial / voice: same
  meta: kind=partial | timestamp=1777906020.328345 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:47:00] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777906020.7337995 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:47:00] operator / voice_transcript_partial / voice: same rule
  meta: kind=partial | timestamp=1777906020.935698 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:47:01] operator / voice_transcript_partial / voice: same rules
  meta: kind=partial | timestamp=1777906021.1404839 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:47:01] operator / voice_transcript_partial / voice: same rules of
  meta: kind=partial | timestamp=1777906021.3774676 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:47:01] operator / voice_transcript_partial / voice: same rules are
  meta: kind=partial | timestamp=1777906021.5866826 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:47:01] operator / voice_transcript_partial / voice: same rules are you
  meta: kind=partial | timestamp=1777906021.800779 | source=windows | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:47:02] operator / voice_transcript_final / voice: same rules are you
  meta: kind=final | timestamp=1777906022.4386094 | source=final | confidence=0.37 | frequency_hz=410.2 | rms=132 | updated_at=1777905722.4909317
- [2026-05-04 22:47:03] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777906023.855226 | source=windows | frequency_hz=414.1 | rms=1580 | updated_at=1777906023.539044
- [2026-05-04 22:47:05] assistant / assistant_prompt / text: Assistant update. Assistant [Deterministic fallback / gpt-oss:20b] The local model reply was unavailable, so this response used the built-in deterministic fallback. Parsed Intent: - action=none confidence=0.35 clarification=True - question: Can you confirm the exact action you want me to prepare? I could not reach the local model, but the top deterministic finding is: Detection=YOLO Object Detection; tracking_scope=person; guard_mode=waypoint_patrol; speed=100 (aggressive); trigger=water_mosfet; burst=6@70ms; return_delay=1.50s; face=off; pir=on. Model note: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=45.0)
  meta: task_kind=prompt | speak_requested=False
- [2026-05-04 22:47:06] operator / voice_transcript_partial / voice: the truth of the
  meta: kind=partial | timestamp=1777906026.0184338 | source=windows | frequency_hz=274.7 | rms=664 | updated_at=1777906025.8486686
- [2026-05-04 22:47:06] operator / voice_transcript_partial / voice: the truth of the three
  meta: kind=partial | timestamp=1777906026.6317148 | source=windows | frequency_hz=350.1 | rms=648 | updated_at=1777906026.6136851
- [2026-05-04 22:47:06] operator / voice_transcript_partial / voice: the thought
  meta: kind=partial | timestamp=1777906026.8355372 | source=windows | frequency_hz=280.9 | rms=1262 | updated_at=1777906026.7393172
- [2026-05-04 22:47:07] operator / voice_transcript_partial / voice: the truth of the things
  meta: kind=partial | timestamp=1777906027.2394733 | source=windows | frequency_hz=278.3 | rms=821 | updated_at=1777906026.9974003
- [2026-05-04 22:47:07] operator / voice_transcript_partial / voice: the truth of the three
  meta: kind=partial | timestamp=1777906027.6456435 | source=windows | frequency_hz=270.2 | rms=1647 | updated_at=1777906027.6401312
- [2026-05-04 22:47:07] operator / voice_transcript_partial / voice: the third
  meta: kind=partial | timestamp=1777906027.8504746 | source=windows | frequency_hz=257.7 | rms=1590 | updated_at=1777906027.76778
- [2026-05-04 22:47:08] operator / voice_transcript_partial / voice: the thought
  meta: kind=partial | timestamp=1777906028.059144 | source=windows | frequency_hz=258.4 | rms=358 | updated_at=1777906028.0186274
- [2026-05-04 22:47:08] operator / voice_transcript_partial / voice: the truth of the three
  meta: kind=partial | timestamp=1777906028.4633124 | source=windows | frequency_hz=226.7 | rms=678 | updated_at=1777906028.1483808
- [2026-05-04 22:47:08] operator / voice_transcript_partial / voice: the thing
  meta: kind=partial | timestamp=1777906028.867678 | source=windows | frequency_hz=222.6 | rms=4069 | updated_at=1777906028.5284665
- [2026-05-04 22:47:09] operator / voice_transcript_partial / voice: the thief
  meta: kind=partial | timestamp=1777906029.2749426 | source=windows | frequency_hz=222.6 | rms=4069 | updated_at=1777906028.5284665
- [2026-05-04 22:47:09] operator / voice_transcript_partial / voice: the third
  meta: kind=partial | timestamp=1777906029.8830647 | source=windows | frequency_hz=323.5 | rms=253 | updated_at=1777906029.807802
- [2026-05-04 22:47:10] operator / voice_transcript_partial / voice: the truth of the things that
  meta: kind=partial | timestamp=1777906030.7276099 | source=windows | frequency_hz=325.0 | rms=1272 | updated_at=1777906030.2128193
- [2026-05-04 22:47:10] operator / voice_transcript_partial / voice: the truth of the three
  meta: kind=partial | timestamp=1777906030.9376917 | source=windows | frequency_hz=325.0 | rms=1272 | updated_at=1777906030.2128193
- [2026-05-04 22:47:11] operator / voice_transcript_partial / voice: the than through our
  meta: kind=partial | timestamp=1777906031.1397767 | source=windows | frequency_hz=325.0 | rms=1272 | updated_at=1777906030.2128193
- [2026-05-04 22:47:11] operator / voice_transcript_partial / voice: the truth of the three are you
  meta: kind=partial | timestamp=1777906031.3423133 | source=windows | frequency_hz=325.0 | rms=1272 | updated_at=1777906030.2128193
- [2026-05-04 22:47:11] operator / voice_transcript_partial / voice: the than through our youth
  meta: kind=partial | timestamp=1777906031.5451562 | source=windows | frequency_hz=325.0 | rms=1272 | updated_at=1777906030.2128193
- [2026-05-04 22:47:11] operator / voice_transcript_final / voice: the than through our youth
  meta: kind=final | timestamp=1777906031.998528 | source=final | confidence=0.08 | frequency_hz=325.0 | rms=1272 | updated_at=1777906030.2128193
- [2026-05-04 22:47:17] operator / voice_transcript_partial / voice: who
  meta: kind=partial | timestamp=1777906037.7369962 | source=windows | frequency_hz=325.0 | rms=1272 | updated_at=1777906030.2128193
- [2026-05-04 22:47:18] operator / voice_transcript_partial / voice: who are you
  meta: kind=partial | timestamp=1777906038.1422358 | source=windows | frequency_hz=325.0 | rms=1272 | updated_at=1777906030.2128193
- [2026-05-04 22:47:18] operator / voice_transcript_final / voice: who are you
  meta: kind=final | timestamp=1777906038.7661374 | source=final | confidence=0.91 | frequency_hz=325.0 | rms=1272 | updated_at=1777906030.2128193
- [2026-05-04 22:47:22] operator / voice_transcript_partial / voice: who
  meta: kind=partial | timestamp=1777906042.0556421 | source=windows | frequency_hz=265.6 | rms=209 | updated_at=1777906041.5871437
- [2026-05-04 22:47:22] operator / voice_transcript_partial / voice: was
  meta: kind=partial | timestamp=1777906042.2586656 | source=windows | frequency_hz=265.6 | rms=209 | updated_at=1777906041.5871437
- [2026-05-04 22:47:22] operator / voice_transcript_partial / voice: western
  meta: kind=partial | timestamp=1777906042.4741347 | source=windows | frequency_hz=265.6 | rms=209 | updated_at=1777906041.5871437
- [2026-05-04 22:47:22] operator / voice_transcript_partial / voice: was surname
  meta: kind=partial | timestamp=1777906042.6841464 | source=windows | frequency_hz=265.6 | rms=209 | updated_at=1777906041.5871437
- [2026-05-04 22:47:23] operator / voice_transcript_final / voice: was surname
  meta: kind=final | timestamp=1777906043.3266833 | source=final | confidence=0.49 | frequency_hz=265.6 | rms=209 | updated_at=1777906041.5871437
- [2026-05-04 22:47:28] operator / voice_transcript_partial / voice: who
  meta: kind=partial | timestamp=1777906048.9302073 | source=windows | frequency_hz=367.2 | rms=269 | updated_at=1777906048.4989293
- [2026-05-04 22:47:28] operator / voice_transcript_partial / voice: why
  meta: kind=partial | timestamp=1777906048.9302073 | source=windows | frequency_hz=367.2 | rms=269 | updated_at=1777906048.4989293
- [2026-05-04 22:47:29] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1777906049.3403497 | source=windows | frequency_hz=367.2 | rms=269 | updated_at=1777906048.4989293
- [2026-05-04 22:47:29] operator / voice_transcript_partial / voice: whack the
  meta: kind=partial | timestamp=1777906049.539967 | source=windows | frequency_hz=367.2 | rms=269 | updated_at=1777906048.4989293
- [2026-05-04 22:47:29] operator / voice_transcript_partial / voice: y. e's
  meta: kind=partial | timestamp=1777906049.740419 | source=windows | frequency_hz=367.2 | rms=269 | updated_at=1777906048.4989293
- [2026-05-04 22:47:30] operator / voice_transcript_partial / voice: y. e's your
  meta: kind=partial | timestamp=1777906050.3764029 | source=windows | frequency_hz=367.2 | rms=269 | updated_at=1777906048.4989293
- [2026-05-04 22:47:30] operator / voice_transcript_partial / voice: y. e's your name
  meta: kind=partial | timestamp=1777906050.5936642 | source=windows | frequency_hz=367.2 | rms=269 | updated_at=1777906048.4989293
- [2026-05-04 22:47:31] operator / voice_transcript_final / voice: y e s your name
  meta: kind=final | timestamp=1777906051.2346807 | source=final | confidence=0.56 | frequency_hz=367.2 | rms=269 | updated_at=1777906048.4989293
- [2026-05-04 22:47:35] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777906055.4914327 | source=windows | frequency_hz=367.2 | rms=269 | updated_at=1777906048.4989293
- [2026-05-04 22:47:35] operator / voice_transcript_partial / voice: on
  meta: kind=partial | timestamp=1777906055.7093327 | source=windows | frequency_hz=367.2 | rms=269 | updated_at=1777906048.4989293
- [2026-05-04 22:47:35] operator / voice_transcript_partial / voice: only
  meta: kind=partial | timestamp=1777906055.9153454 | source=windows | frequency_hz=367.2 | rms=269 | updated_at=1777906048.4989293
- [2026-05-04 22:47:36] operator / voice_transcript_partial / voice: on these
  meta: kind=partial | timestamp=1777906056.1746457 | source=windows | frequency_hz=406.2 | rms=254 | updated_at=1777906056.0522618
- [2026-05-04 22:47:36] operator / voice_transcript_partial / voice: on the sea
  meta: kind=partial | timestamp=1777906056.385994 | source=windows | frequency_hz=406.2 | rms=254 | updated_at=1777906056.0522618
- [2026-05-04 22:47:36] operator / voice_transcript_partial / voice: monday's steep
  meta: kind=partial | timestamp=1777906056.5880623 | source=windows | frequency_hz=376.1 | rms=169 | updated_at=1777906056.5682962
- [2026-05-04 22:47:36] operator / voice_transcript_partial / voice: monday's steep for
  meta: kind=partial | timestamp=1777906056.7946002 | source=windows | frequency_hz=376.1 | rms=169 | updated_at=1777906056.5682962
- [2026-05-04 22:47:37] operator / voice_transcript_partial / voice: monday's steep board that
  meta: kind=partial | timestamp=1777906057.2307696 | source=windows | frequency_hz=356.6 | rms=304 | updated_at=1777906056.8221495
- [2026-05-04 22:47:37] operator / voice_transcript_partial / voice: monday's steep board and the
  meta: kind=partial | timestamp=1777906057.444352 | source=windows | frequency_hz=356.6 | rms=304 | updated_at=1777906056.8221495
- [2026-05-04 22:47:37] operator / voice_transcript_final / voice: monday s steep board and the
  meta: kind=final | timestamp=1777906057.9850216 | source=final | confidence=0.39 | frequency_hz=356.6 | rms=304 | updated_at=1777906056.8221495
- [2026-05-04 22:47:39] operator / voice_transcript_partial / voice: two
  meta: kind=partial | timestamp=1777906059.0335317 | source=windows | frequency_hz=356.6 | rms=304 | updated_at=1777906056.8221495
- [2026-05-04 22:47:39] operator / voice_transcript_partial / voice: cisco
  meta: kind=partial | timestamp=1777906059.4868226 | source=windows | frequency_hz=343.8 | rms=558 | updated_at=1777906059.1269813
- [2026-05-04 22:47:39] operator / voice_transcript_partial / voice: tacoma
  meta: kind=partial | timestamp=1777906059.7022324 | source=windows | frequency_hz=343.8 | rms=558 | updated_at=1777906059.1269813
- [2026-05-04 22:47:39] operator / voice_transcript_partial / voice: diplomas and
  meta: kind=partial | timestamp=1777906059.9030395 | source=windows | frequency_hz=372.1 | rms=520 | updated_at=1777906059.8907976
- [2026-05-04 22:47:40] operator / voice_transcript_partial / voice: tooth comb the name
  meta: kind=partial | timestamp=1777906060.1063402 | source=windows | frequency_hz=372.1 | rms=520 | updated_at=1777906059.8907976
- [2026-05-04 22:47:40] operator / voice_transcript_partial / voice: tooth comb the name not be
  meta: kind=partial | timestamp=1777906060.742375 | source=windows | frequency_hz=372.1 | rms=520 | updated_at=1777906059.8907976
- [2026-05-04 22:47:40] operator / voice_transcript_partial / voice: tacoma dome were going
  meta: kind=partial | timestamp=1777906060.9274268 | source=windows | frequency_hz=372.1 | rms=520 | updated_at=1777906059.8907976
- [2026-05-04 22:47:41] operator / voice_transcript_partial / voice: tacoma and book draws nearer
  meta: kind=partial | timestamp=1777906061.1302915 | source=windows | frequency_hz=372.1 | rms=520 | updated_at=1777906059.8907976
- [2026-05-04 22:47:41] operator / voice_transcript_partial / voice: tacoma dome were grown in recent
  meta: kind=partial | timestamp=1777906061.3332534 | source=windows | frequency_hz=372.1 | rms=520 | updated_at=1777906059.8907976
- [2026-05-04 22:47:41] operator / voice_transcript_partial / voice: tacoma dome what congress and are
  meta: kind=partial | timestamp=1777906061.7399912 | source=windows | frequency_hz=372.1 | rms=520 | updated_at=1777906059.8907976
- [2026-05-04 22:47:41] operator / voice_transcript_partial / voice: tacoma dome what congress and i
  meta: kind=partial | timestamp=1777906061.9461493 | source=windows | frequency_hz=372.1 | rms=520 | updated_at=1777906059.8907976
- [2026-05-04 22:47:42] operator / voice_transcript_partial / voice: tacoma dome what congress and are
  meta: kind=partial | timestamp=1777906062.1465433 | source=windows | frequency_hz=372.1 | rms=520 | updated_at=1777906059.8907976
- [2026-05-04 22:47:42] operator / voice_transcript_partial / voice: tacoma dome what congress and are more
  meta: kind=partial | timestamp=1777906062.351934 | source=windows | frequency_hz=372.1 | rms=520 | updated_at=1777906059.8907976
- [2026-05-04 22:47:42] operator / voice_transcript_partial / voice: tacoma dome what congress and our lives
  meta: kind=partial | timestamp=1777906062.754954 | source=windows | frequency_hz=372.1 | rms=520 | updated_at=1777906059.8907976
- [2026-05-04 22:47:42] operator / voice_transcript_partial / voice: tacoma dome what congress and our allies of
  meta: kind=partial | timestamp=1777906062.9583821 | source=windows | frequency_hz=372.1 | rms=520 | updated_at=1777906059.8907976
- [2026-05-04 22:47:43] operator / voice_transcript_partial / voice: tacoma dome what congress and are mindful
  meta: kind=partial | timestamp=1777906063.1612425 | source=windows | frequency_hz=372.1 | rms=520 | updated_at=1777906059.8907976
- [2026-05-04 22:47:43] operator / voice_transcript_partial / voice: tacoma dome what congress and our blood flow
  meta: kind=partial | timestamp=1777906063.3647244 | source=windows | frequency_hz=372.1 | rms=520 | updated_at=1777906059.8907976
- [2026-05-04 22:47:43] operator / voice_transcript_partial / voice: tacoma dome what congress and are blind, phone
  meta: kind=partial | timestamp=1777906063.7674327 | source=windows | frequency_hz=372.1 | rms=520 | updated_at=1777906059.8907976
- [2026-05-04 22:47:45] operator / voice_transcript_final / voice: tacoma dome what congress and are blind phone
  meta: kind=final | timestamp=1777906065.2300847 | source=final | confidence=0.31 | frequency_hz=372.1 | rms=520 | updated_at=1777906059.8907976
- [2026-05-04 22:47:45] operator / voice_transcript_partial / voice: now
  meta: kind=partial | timestamp=1777906065.8381803 | source=windows | frequency_hz=372.1 | rms=520 | updated_at=1777906059.8907976
- [2026-05-04 22:47:46] operator / voice_transcript_partial / voice: back
  meta: kind=partial | timestamp=1777906066.2580662 | source=windows | frequency_hz=372.1 | rms=520 | updated_at=1777906059.8907976
- [2026-05-04 22:47:46] operator / voice_transcript_partial / voice: back where
  meta: kind=partial | timestamp=1777906066.460182 | source=windows | frequency_hz=341.8 | rms=306 | updated_at=1777906066.4185438
- [2026-05-04 22:47:46] operator / voice_transcript_partial / voice: background
  meta: kind=partial | timestamp=1777906066.687168 | source=windows | frequency_hz=341.8 | rms=306 | updated_at=1777906066.4185438
- [2026-05-04 22:47:47] operator / voice_transcript_partial / voice: back around more
  meta: kind=partial | timestamp=1777906067.099196 | source=windows | frequency_hz=341.8 | rms=306 | updated_at=1777906066.4185438
- [2026-05-04 22:47:47] operator / voice_transcript_partial / voice: back around no lines
  meta: kind=partial | timestamp=1777906067.5025764 | source=windows | frequency_hz=341.8 | rms=306 | updated_at=1777906066.4185438
- [2026-05-04 22:47:48] operator / voice_transcript_partial / voice: back around no lines to
  meta: kind=partial | timestamp=1777906068.7700763 | source=windows | frequency_hz=341.8 | rms=306 | updated_at=1777906066.4185438
- [2026-05-04 22:47:49] operator / voice_transcript_partial / voice: back around no lines that
  meta: kind=partial | timestamp=1777906069.0203998 | source=windows | frequency_hz=341.8 | rms=306 | updated_at=1777906066.4185438
- [2026-05-04 22:47:49] operator / voice_transcript_partial / voice: back around no lines six
  meta: kind=partial | timestamp=1777906069.2454405 | source=windows | frequency_hz=341.8 | rms=306 | updated_at=1777906066.4185438
- [2026-05-04 22:47:49] operator / voice_transcript_partial / voice: back around no lines six to
  meta: kind=partial | timestamp=1777906069.6558154 | source=windows | frequency_hz=341.8 | rms=306 | updated_at=1777906066.4185438
- [2026-05-04 22:47:49] operator / voice_transcript_partial / voice: back around no lines such as
  meta: kind=partial | timestamp=1777906069.8952618 | source=windows | frequency_hz=341.8 | rms=306 | updated_at=1777906066.4185438
- [2026-05-04 22:47:50] operator / voice_transcript_partial / voice: back around no lines six to six
  meta: kind=partial | timestamp=1777906070.2018337 | source=windows | frequency_hz=341.8 | rms=306 | updated_at=1777906066.4185438
- [2026-05-04 22:47:51] operator / voice_transcript_partial / voice: back around no lines six six six
  meta: kind=partial | timestamp=1777906071.0459478 | source=windows | frequency_hz=341.8 | rms=306 | updated_at=1777906066.4185438
- [2026-05-04 22:47:52] operator / voice_transcript_final / voice: back around no lines 666
  meta: kind=final | timestamp=1777906072.6335003 | source=final | confidence=0.41 | frequency_hz=341.8 | rms=306 | updated_at=1777906066.4185438
- [2026-05-04 22:47:55] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777906075.5436995 | source=windows | frequency_hz=335.6 | rms=640 | updated_at=1777906075.5086198
- [2026-05-04 22:47:55] operator / voice_transcript_partial / voice: am
  meta: kind=partial | timestamp=1777906075.5436995 | source=windows | frequency_hz=335.6 | rms=640 | updated_at=1777906075.5086198
- [2026-05-04 22:47:56] operator / voice_transcript_partial / voice: eileen
  meta: kind=partial | timestamp=1777906076.2275677 | source=windows | frequency_hz=330.2 | rms=393 | updated_at=1777906075.637822
- [2026-05-04 22:47:56] operator / voice_command / voice: elion
  meta: normalized=True
- [2026-05-04 22:47:56] operator / voice_transcript_partial / voice: and a
  meta: kind=partial | timestamp=1777906076.6442604 | source=windows | frequency_hz=339.0 | rms=1040 | updated_at=1777906076.535663
- [2026-05-04 22:47:56] operator / voice_transcript_partial / voice: am moved be a
  meta: kind=partial | timestamp=1777906076.8495185 | source=windows | frequency_hz=339.0 | rms=1040 | updated_at=1777906076.535663
- [2026-05-04 22:47:57] operator / voice_transcript_partial / voice: and a lee and
  meta: kind=partial | timestamp=1777906077.0508485 | source=windows | frequency_hz=339.0 | rms=1040 | updated_at=1777906076.535663
- [2026-05-04 22:47:57] operator / voice_transcript_final / voice: and a lee and
  meta: kind=final | timestamp=1777906077.4594097 | source=final | confidence=0.23 | frequency_hz=339.0 | rms=1040 | updated_at=1777906076.535663
- [2026-05-04 22:47:57] operator / voice_command / voice: and a lee and
  meta: normalized=True
- [2026-05-04 22:47:58] assistant / spoken_confirmation / voice: I think I heard and a lee and. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:48:03] operator / voice_transcript_partial / voice: he
  meta: kind=partial | timestamp=1777906083.773728 | source=windows | frequency_hz=339.0 | rms=1040 | updated_at=1777906076.535663
- [2026-05-04 22:48:05] operator / voice_transcript_final / voice: he
  meta: kind=final | timestamp=1777906085.5396187 | source=final | confidence=0.0 | frequency_hz=339.0 | rms=1040 | updated_at=1777906076.535663
- [2026-05-04 22:48:07] operator / voice_transcript_partial / voice: knew
  meta: kind=partial | timestamp=1777906087.00182 | source=windows | frequency_hz=339.0 | rms=1040 | updated_at=1777906076.535663
- [2026-05-04 22:48:07] operator / voice_transcript_partial / voice: use
  meta: kind=partial | timestamp=1777906087.4397748 | source=windows | frequency_hz=339.0 | rms=1040 | updated_at=1777906076.535663
- [2026-05-04 22:48:07] operator / voice_transcript_partial / voice: sees
  meta: kind=partial | timestamp=1777906087.6438284 | source=windows | frequency_hz=339.0 | rms=1040 | updated_at=1777906076.535663
- [2026-05-04 22:48:08] operator / voice_transcript_partial / voice: sees through
  meta: kind=partial | timestamp=1777906088.052282 | source=windows | frequency_hz=339.0 | rms=1040 | updated_at=1777906076.535663
- [2026-05-04 22:48:08] operator / voice_transcript_partial / voice: sees for three
  meta: kind=partial | timestamp=1777906088.5517614 | source=windows | frequency_hz=339.0 | rms=1040 | updated_at=1777906076.535663
- [2026-05-04 22:48:08] operator / voice_transcript_partial / voice: use troops could
  meta: kind=partial | timestamp=1777906088.8582413 | source=windows | frequency_hz=339.0 | rms=1040 | updated_at=1777906076.535663
- [2026-05-04 22:48:08] operator / voice_transcript_partial / voice: sees through played down
  meta: kind=partial | timestamp=1777906088.858759 | source=windows | frequency_hz=339.0 | rms=1040 | updated_at=1777906076.535663
- [2026-05-04 22:48:09] operator / voice_transcript_partial / voice: sees through played down the
  meta: kind=partial | timestamp=1777906089.2798817 | source=windows | frequency_hz=339.0 | rms=1040 | updated_at=1777906076.535663
- [2026-05-04 22:48:09] operator / voice_transcript_partial / voice: sees through played down the bay
  meta: kind=partial | timestamp=1777906089.4855433 | source=windows | frequency_hz=339.0 | rms=1040 | updated_at=1777906076.535663
- [2026-05-04 22:48:09] operator / voice_transcript_partial / voice: sees through played down the beach
  meta: kind=partial | timestamp=1777906089.6987746 | source=windows | frequency_hz=339.0 | rms=1040 | updated_at=1777906076.535663
- [2026-05-04 22:48:09] operator / voice_transcript_partial / voice: sees through played down the h.
  meta: kind=partial | timestamp=1777906089.917444 | source=windows | frequency_hz=339.0 | rms=1040 | updated_at=1777906076.535663
- [2026-05-04 22:48:10] operator / voice_transcript_final / voice: sees through played down the h
  meta: kind=final | timestamp=1777906090.7917337 | source=final | confidence=0.31 | frequency_hz=339.0 | rms=1040 | updated_at=1777906076.535663
- [2026-05-04 22:48:11] operator / voice_command / voice: sees through played down the h
  meta: normalized=True
- [2026-05-04 22:48:12] assistant / spoken_confirmation / voice: I think I heard sees through played down the h. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-04 22:48:14] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777906094.6652877 | source=windows | frequency_hz=318.8 | rms=382 | updated_at=1777906094.178949
- [2026-05-04 22:48:14] operator / voice_transcript_partial / voice: moore
  meta: kind=partial | timestamp=1777906094.6652877 | source=windows | frequency_hz=318.8 | rms=382 | updated_at=1777906094.178949
- [2026-05-04 22:48:14] operator / voice_transcript_partial / voice: morrow
  meta: kind=partial | timestamp=1777906094.8863933 | source=windows | frequency_hz=318.8 | rms=382 | updated_at=1777906094.178949
- [2026-05-04 22:48:15] operator / voice_transcript_partial / voice: monica
  meta: kind=partial | timestamp=1777906095.1291301 | source=windows | frequency_hz=309.8 | rms=674 | updated_at=1777906095.078986
- [2026-05-04 22:48:15] operator / voice_transcript_partial / voice: maloney crop
  meta: kind=partial | timestamp=1777906095.583985 | source=windows | frequency_hz=309.8 | rms=674 | updated_at=1777906095.078986
- [2026-05-04 22:48:16] operator / voice_transcript_partial / voice: maloney crop bowl
  meta: kind=partial | timestamp=1777906096.3416045 | source=windows | frequency_hz=347.7 | rms=252 | updated_at=1777906096.2301736
- [2026-05-04 22:48:16] operator / voice_transcript_partial / voice: moronic drop below
  meta: kind=partial | timestamp=1777906096.7676992 | source=windows | frequency_hz=351.4 | rms=247 | updated_at=1777906096.4790819
- [2026-05-04 22:48:16] operator / voice_transcript_partial / voice: maloney crop bowl and
  meta: kind=partial | timestamp=1777906096.9975479 | source=windows | frequency_hz=351.4 | rms=247 | updated_at=1777906096.4790819
- [2026-05-04 22:48:17] operator / voice_transcript_partial / voice: maloney crop boulogne
  meta: kind=partial | timestamp=1777906097.2173877 | source=windows | frequency_hz=351.4 | rms=247 | updated_at=1777906096.4790819
- [2026-05-04 22:48:17] operator / voice_transcript_partial / voice: maloney crop bowl and the
  meta: kind=partial | timestamp=1777906097.6465113 | source=windows | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:17] operator / voice_transcript_partial / voice: maloney crop bowl and ninety eight
  meta: kind=partial | timestamp=1777906097.8776898 | source=windows | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:18] operator / voice_transcript_partial / voice: maloney crop bowl and now you can i
  meta: kind=partial | timestamp=1777906098.0974925 | source=windows | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:18] operator / voice_transcript_final / voice: maloney crop bowl and 98
  meta: kind=final | timestamp=1777906098.8248105 | source=final | confidence=0.42 | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:24] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777906104.517565 | source=windows | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:24] operator / voice_transcript_partial / voice: than
  meta: kind=partial | timestamp=1777906104.517565 | source=windows | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:24] operator / voice_transcript_partial / voice: pence
  meta: kind=partial | timestamp=1777906104.9333656 | source=windows | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:25] operator / voice_transcript_partial / voice: console
  meta: kind=partial | timestamp=1777906105.1409516 | source=windows | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:26] operator / voice_transcript_final / voice: console
  meta: kind=final | timestamp=1777906106.0131931 | source=final | confidence=0.65 | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:27] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777906107.6360767 | source=windows | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:27] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777906107.8380067 | source=windows | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:28] operator / voice_transcript_partial / voice: in a
  meta: kind=partial | timestamp=1777906108.0410247 | source=windows | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:28] operator / voice_transcript_partial / voice: enabled
  meta: kind=partial | timestamp=1777906108.2442908 | source=windows | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:28] operator / voice_transcript_partial / voice: enabled us to
  meta: kind=partial | timestamp=1777906108.446346 | source=windows | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:28] operator / voice_transcript_partial / voice: enabled the smarts
  meta: kind=partial | timestamp=1777906108.8569677 | source=windows | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:29] operator / voice_transcript_partial / voice: enabled the smart sent
  meta: kind=partial | timestamp=1777906109.6663966 | source=windows | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:29] operator / voice_transcript_partial / voice: enable the smart sentry
  meta: kind=partial | timestamp=1777906109.6669195 | source=windows | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:29] operator / voice_transcript_final / voice: enable smart sentry
  meta: kind=final | timestamp=1777906109.6690543 | source=final | confidence=0.82 | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:30] operator / voice_command / voice: enable smart sentry
  meta: normalized=True
- [2026-05-04 22:48:30] assistant / spoken_confirmation / voice: Resuming Smart Sentry now.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-04 22:48:37] operator / voice_transcript_partial / voice: who
  meta: kind=partial | timestamp=1777906117.6509676 | source=windows | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:37] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1777906117.8599854 | source=windows | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:38] operator / voice_transcript_partial / voice: what else
  meta: kind=partial | timestamp=1777906118.0660396 | source=windows | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:38] operator / voice_transcript_partial / voice: what else can you do
  meta: kind=partial | timestamp=1777906118.2698116 | source=windows | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:39] operator / voice_transcript_final / voice: what else can you do
  meta: kind=final | timestamp=1777906119.1031454 | source=final | confidence=0.27 | frequency_hz=343.3 | rms=147 | updated_at=1777906097.3790164
- [2026-05-04 22:48:39] operator / voice_command / voice: what else can you do
  meta: normalized=True
- [2026-05-04 22:48:40] assistant / spoken_confirmation / voice: I think I heard what else can you do. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False

# SMART SENTRY V4.0.0 Runtime Conversation Export

- Generated: 2026-05-05 10:27:01
- Entries: 199
- Roles: {'assistant': 16, 'system': 1, 'operator': 182}
- Event types: {'assistant_prompt': 1, 'assistant_analysis': 1, 'voice_status': 1, 'spoken_confirmation': 14, 'voice_transcript_partial': 143, 'voice_transcript_final': 28, 'voice_command': 11}
- Channels: {'text': 2, 'voice': 197}
- Latest operator request: thought that the
- Latest assistant message: No confirmation received. I did not run and a book about.

## Analysis Hints

- Partial transcript fragments are much more frequent than final transcripts. Review wake-window timing, VAD gating, or microphone noise cleanup.

## Timeline

- [2026-05-05 10:22:23] assistant / assistant_prompt / text: Local AI assistant ready. It will use Ollama when available and fall back to deterministic runtime guidance if the model is offline.
  meta: task_kind=prompt | speak_requested=False
- [2026-05-05 10:22:23] assistant / assistant_analysis / text: Runtime Analyst ready. Use this tab for current-state analysis and recommendation drafts.
  meta: task_kind=analysis | speak_requested=False
- [2026-05-05 10:22:24] system / voice_status / voice: listening
  meta: kind=status | timestamp=1777947744.828161 | source=windows
- [2026-05-05 10:22:26] assistant / spoken_confirmation / voice: Smart Sentry AI is online. What do you want me to do first?
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 10:22:27] operator / voice_transcript_partial / voice: each
  meta: kind=partial | timestamp=1777947747.1036146 | source=windows
- [2026-05-05 10:22:27] operator / voice_transcript_partial / voice: each each
  meta: kind=partial | timestamp=1777947747.5111127 | source=windows
- [2026-05-05 10:22:28] operator / voice_transcript_partial / voice: each each each
  meta: kind=partial | timestamp=1777947748.139446 | source=windows
- [2026-05-05 10:22:28] operator / voice_transcript_partial / voice: each each to each
  meta: kind=partial | timestamp=1777947748.5465088 | source=windows
- [2026-05-05 10:22:29] operator / voice_transcript_final / voice: each each to each
  meta: kind=final | timestamp=1777947749.3882897 | source=final | confidence=0.63
- [2026-05-05 10:22:31] operator / voice_transcript_partial / voice: say
  meta: kind=partial | timestamp=1777947751.0073051 | source=windows
- [2026-05-05 10:22:31] operator / voice_transcript_partial / voice: small
  meta: kind=partial | timestamp=1777947751.2124548 | source=windows
- [2026-05-05 10:22:31] operator / voice_transcript_partial / voice: sub was
  meta: kind=partial | timestamp=1777947751.4159877 | source=windows
- [2026-05-05 10:22:32] operator / voice_transcript_final / voice: sub was
  meta: kind=final | timestamp=1777947752.2302883 | source=final | confidence=0.36
- [2026-05-05 10:22:48] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777947768.1762397 | source=windows
- [2026-05-05 10:23:13] operator / voice_transcript_partial / voice: of
  meta: kind=partial | timestamp=1777947793.353743 | source=windows
- [2026-05-05 10:23:13] operator / voice_transcript_partial / voice: off
  meta: kind=partial | timestamp=1777947793.353743 | source=windows
- [2026-05-05 10:23:14] operator / voice_transcript_partial / voice: off the
  meta: kind=partial | timestamp=1777947794.7737162 | source=windows | frequency_hz=345.9 | rms=1739 | updated_at=1777947794.7128935
- [2026-05-05 10:23:17] operator / voice_transcript_partial / voice: off one of the things
  meta: kind=partial | timestamp=1777947797.004703 | source=windows | frequency_hz=296.3 | rms=510 | updated_at=1777947796.8929799
- [2026-05-05 10:23:17] operator / voice_transcript_partial / voice: if the if
  meta: kind=partial | timestamp=1777947797.4099674 | source=windows | frequency_hz=296.3 | rms=510 | updated_at=1777947796.8929799
- [2026-05-05 10:23:17] operator / voice_transcript_partial / voice: if the thought
  meta: kind=partial | timestamp=1777947797.6241658 | source=windows | frequency_hz=296.3 | rms=510 | updated_at=1777947796.8929799
- [2026-05-05 10:23:18] operator / voice_transcript_partial / voice: off the th
  meta: kind=partial | timestamp=1777947798.0465806 | source=windows | frequency_hz=296.3 | rms=510 | updated_at=1777947796.8929799
- [2026-05-05 10:23:18] operator / voice_transcript_partial / voice: off the thief
  meta: kind=partial | timestamp=1777947798.251918 | source=windows | frequency_hz=296.3 | rms=510 | updated_at=1777947796.8929799
- [2026-05-05 10:23:18] operator / voice_transcript_partial / voice: off the thing
  meta: kind=partial | timestamp=1777947798.4539642 | source=windows | frequency_hz=307.4 | rms=303 | updated_at=1777947798.292955
- [2026-05-05 10:23:18] operator / voice_transcript_partial / voice: off one of the things
  meta: kind=partial | timestamp=1777947798.6714032 | source=windows | frequency_hz=307.4 | rms=303 | updated_at=1777947798.292955
- [2026-05-05 10:23:20] operator / voice_transcript_final / voice: off one of the things
  meta: kind=final | timestamp=1777947800.096247 | source=final | confidence=0.15 | frequency_hz=294.2 | rms=228 | updated_at=1777947799.5728445
- [2026-05-05 10:23:20] operator / voice_transcript_partial / voice: he can
  meta: kind=partial | timestamp=1777947800.920629 | source=windows | frequency_hz=294.2 | rms=228 | updated_at=1777947799.5728445
- [2026-05-05 10:23:21] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777947801.1240494 | source=windows | frequency_hz=294.2 | rms=228 | updated_at=1777947799.5728445
- [2026-05-05 10:23:21] operator / voice_transcript_partial / voice: connect to
  meta: kind=partial | timestamp=1777947801.328025 | source=windows | frequency_hz=294.2 | rms=228 | updated_at=1777947799.5728445
- [2026-05-05 10:23:21] operator / voice_transcript_partial / voice: the clinic that
  meta: kind=partial | timestamp=1777947801.5295703 | source=windows | frequency_hz=294.2 | rms=228 | updated_at=1777947799.5728445
- [2026-05-05 10:23:21] operator / voice_transcript_partial / voice: he connected abelson
  meta: kind=partial | timestamp=1777947801.939575 | source=windows | frequency_hz=294.2 | rms=228 | updated_at=1777947799.5728445
- [2026-05-05 10:23:22] operator / voice_transcript_partial / voice: he connected able some arts
  meta: kind=partial | timestamp=1777947802.145202 | source=windows | frequency_hz=294.2 | rms=228 | updated_at=1777947799.5728445
- [2026-05-05 10:23:22] operator / voice_transcript_partial / voice: he connected able some arts center
  meta: kind=partial | timestamp=1777947802.3595517 | source=windows | frequency_hz=195.3 | rms=338 | updated_at=1777947802.2627926
- [2026-05-05 10:23:22] operator / voice_transcript_partial / voice: the connect enables martz entry
  meta: kind=partial | timestamp=1777947802.562012 | source=windows | frequency_hz=183.7 | rms=324 | updated_at=1777947802.5224333
- [2026-05-05 10:23:22] operator / voice_transcript_final / voice: the connect enables martz entry
  meta: kind=final | timestamp=1777947802.9740515 | source=final | confidence=0.43 | frequency_hz=148.1 | rms=616 | updated_at=1777947802.9032626
- [2026-05-05 10:23:28] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777947808.2581856 | source=windows | frequency_hz=141.5 | rms=1225 | updated_at=1777947808.1527107
- [2026-05-05 10:23:28] operator / voice_transcript_partial / voice: war
  meta: kind=partial | timestamp=1777947808.8634965 | source=windows | frequency_hz=126.7 | rms=480 | updated_at=1777947808.7926114
- [2026-05-05 10:23:29] operator / voice_transcript_partial / voice: was
  meta: kind=partial | timestamp=1777947809.0669317 | source=windows | frequency_hz=126.7 | rms=480 | updated_at=1777947808.7926114
- [2026-05-05 10:23:29] operator / voice_transcript_partial / voice: warm
  meta: kind=partial | timestamp=1777947809.2699273 | source=windows | frequency_hz=126.7 | rms=480 | updated_at=1777947808.7926114
- [2026-05-05 10:23:29] operator / voice_transcript_partial / voice: was a
  meta: kind=partial | timestamp=1777947809.4710371 | source=windows | frequency_hz=223.2 | rms=633 | updated_at=1777947809.4338617
- [2026-05-05 10:23:29] operator / voice_transcript_partial / voice: warm alien
  meta: kind=partial | timestamp=1777947809.8804677 | source=windows | frequency_hz=162.3 | rms=1238 | updated_at=1777947809.8130565
- [2026-05-05 10:23:30] operator / voice_transcript_final / voice: elion warm
  meta: kind=final | timestamp=1777947810.500475 | source=final | confidence=0.7 | frequency_hz=171.0 | rms=196 | updated_at=1777947810.203376
- [2026-05-05 10:23:30] operator / voice_command / voice: elion warm
  meta: normalized=True
- [2026-05-05 10:23:32] assistant / spoken_confirmation / voice: I think I heard elion warm. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 10:23:32] operator / voice_transcript_partial / voice: who
  meta: kind=partial | timestamp=1777947812.1368883 | source=windows | frequency_hz=178.5 | rms=972 | updated_at=1777947811.8635073
- [2026-05-05 10:23:32] operator / voice_transcript_partial / voice: what
  meta: kind=partial | timestamp=1777947812.3489847 | source=windows | frequency_hz=178.5 | rms=972 | updated_at=1777947811.8635073
- [2026-05-05 10:23:32] operator / voice_transcript_final / voice: work
  meta: kind=final | timestamp=1777947812.963478 | source=final | confidence=0.13 | frequency_hz=178.5 | rms=972 | updated_at=1777947811.8635073
- [2026-05-05 10:23:34] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777947814.1876578 | source=windows | frequency_hz=245.8 | rms=453 | updated_at=1777947814.052101
- [2026-05-05 10:23:34] operator / voice_transcript_partial / voice: the air
  meta: kind=partial | timestamp=1777947814.7964623 | source=windows | frequency_hz=245.8 | rms=453 | updated_at=1777947814.052101
- [2026-05-05 10:23:34] operator / voice_transcript_partial / voice: the air and
  meta: kind=partial | timestamp=1777947814.9998631 | source=windows | frequency_hz=245.8 | rms=453 | updated_at=1777947814.052101
- [2026-05-05 10:23:35] operator / voice_transcript_partial / voice: the air and that
  meta: kind=partial | timestamp=1777947815.6053772 | source=windows | frequency_hz=304.7 | rms=1153 | updated_at=1777947815.5733428
- [2026-05-05 10:23:35] operator / voice_transcript_partial / voice: the air and the
  meta: kind=partial | timestamp=1777947815.8067777 | source=windows | frequency_hz=248.6 | rms=1810 | updated_at=1777947815.7030094
- [2026-05-05 10:23:36] operator / voice_transcript_partial / voice: the air and the own
  meta: kind=partial | timestamp=1777947816.8232746 | source=windows | frequency_hz=187.2 | rms=796 | updated_at=1777947816.342878
- [2026-05-05 10:23:37] operator / voice_transcript_final / voice: the air and the own
  meta: kind=final | timestamp=1777947817.2367551 | source=final | confidence=0.32 | frequency_hz=187.2 | rms=796 | updated_at=1777947816.342878
- [2026-05-05 10:23:37] operator / voice_command / voice: the air and the own
  meta: normalized=True
- [2026-05-05 10:23:37] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777947817.8398278 | source=windows | frequency_hz=268.0 | rms=347 | updated_at=1777947817.2428262
- [2026-05-05 10:23:38] operator / voice_transcript_partial / voice: take you
  meta: kind=partial | timestamp=1777947818.0408509 | source=windows | frequency_hz=268.0 | rms=347 | updated_at=1777947817.2428262
- [2026-05-05 10:23:38] operator / voice_transcript_partial / voice: ticket per
  meta: kind=partial | timestamp=1777947818.2443452 | source=windows | frequency_hz=268.0 | rms=347 | updated_at=1777947817.2428262
- [2026-05-05 10:23:38] operator / voice_transcript_partial / voice: take you protect
  meta: kind=partial | timestamp=1777947818.4481974 | source=windows | frequency_hz=268.0 | rms=347 | updated_at=1777947817.2428262
- [2026-05-05 10:23:38] operator / voice_transcript_partial / voice: ticket protected
  meta: kind=partial | timestamp=1777947818.8530748 | source=windows | frequency_hz=268.0 | rms=347 | updated_at=1777947817.2428262
- [2026-05-05 10:23:39] operator / voice_transcript_partial / voice: ticket protected able
  meta: kind=partial | timestamp=1777947819.0565042 | source=windows | frequency_hz=268.0 | rms=347 | updated_at=1777947817.2428262
- [2026-05-05 10:23:39] operator / voice_transcript_partial / voice: ticket protected able to supply
  meta: kind=partial | timestamp=1777947819.2596145 | source=windows | frequency_hz=268.0 | rms=347 | updated_at=1777947817.2428262
- [2026-05-05 10:23:39] operator / voice_transcript_partial / voice: ticket protected abel's arts
  meta: kind=partial | timestamp=1777947819.5935383 | source=windows | frequency_hz=268.0 | rms=347 | updated_at=1777947817.2428262
- [2026-05-05 10:23:39] operator / voice_transcript_partial / voice: ticket protected abel's arts center
  meta: kind=partial | timestamp=1777947819.8046265 | source=windows | frequency_hz=207.0 | rms=250 | updated_at=1777947819.6730516
- [2026-05-05 10:23:40] operator / voice_transcript_partial / voice: ticket protected abel's arts entry
  meta: kind=partial | timestamp=1777947820.007829 | source=windows | frequency_hz=207.0 | rms=250 | updated_at=1777947819.6730516
- [2026-05-05 10:23:40] operator / voice_transcript_partial / voice: ticket protected abel's arts entry in
  meta: kind=partial | timestamp=1777947820.6194942 | source=windows | frequency_hz=207.0 | rms=250 | updated_at=1777947819.6730516
- [2026-05-05 10:23:41] operator / voice_transcript_partial / voice: ticket protected abel's arts entry and
  meta: kind=partial | timestamp=1777947821.0243897 | source=windows | frequency_hz=207.0 | rms=250 | updated_at=1777947819.6730516
- [2026-05-05 10:23:41] operator / voice_transcript_partial / voice: ticket protected abel's arts entry and the
  meta: kind=partial | timestamp=1777947821.8389893 | source=windows | frequency_hz=207.0 | rms=250 | updated_at=1777947819.6730516
- [2026-05-05 10:23:42] operator / voice_transcript_partial / voice: ticket protected abel's arts entry and then
  meta: kind=partial | timestamp=1777947822.2435427 | source=windows | frequency_hz=238.3 | rms=522 | updated_at=1777947822.2332666
- [2026-05-05 10:23:43] operator / voice_transcript_final / voice: ticket protected abel s arts entry and then
  meta: kind=final | timestamp=1777947823.26987 | source=final | confidence=0.23 | frequency_hz=234.0 | rms=264 | updated_at=1777947822.6132014
- [2026-05-05 10:23:43] operator / voice_command / voice: ticket protected abel s arts entry and then
  meta: normalized=True
- [2026-05-05 10:23:44] assistant / spoken_confirmation / voice: I think I heard ticket protected abel s arts entry and then. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 10:23:44] assistant / spoken_confirmation / voice: I think I heard the air and the own. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 10:23:45] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777947825.1469061 | source=windows | frequency_hz=114.0 | rms=501 | updated_at=1777947825.0531147
- [2026-05-05 10:23:45] operator / voice_transcript_partial / voice: we're
  meta: kind=partial | timestamp=1777947825.1469061 | source=windows | frequency_hz=114.0 | rms=501 | updated_at=1777947825.0531147
- [2026-05-05 10:23:45] operator / voice_transcript_partial / voice: won't
  meta: kind=partial | timestamp=1777947825.353735 | source=windows | frequency_hz=114.0 | rms=501 | updated_at=1777947825.0531147
- [2026-05-05 10:23:46] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777947826.5783005 | source=windows | frequency_hz=114.0 | rms=501 | updated_at=1777947825.0531147
- [2026-05-05 10:23:46] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777947826.7817664 | source=windows | frequency_hz=114.0 | rms=501 | updated_at=1777947825.0531147
- [2026-05-05 10:23:47] operator / voice_transcript_partial / voice: an
  meta: kind=partial | timestamp=1777947827.4009843 | source=windows | frequency_hz=139.8 | rms=959 | updated_at=1777947827.3536484
- [2026-05-05 10:23:48] operator / voice_transcript_partial / voice: an end
  meta: kind=partial | timestamp=1777947828.4242148 | source=windows | frequency_hz=153.8 | rms=402 | updated_at=1777947827.4893472
- [2026-05-05 10:23:48] operator / voice_transcript_partial / voice: and the
  meta: kind=partial | timestamp=1777947828.4247181 | source=windows | frequency_hz=153.8 | rms=402 | updated_at=1777947827.4893472
- [2026-05-05 10:23:49] operator / voice_transcript_partial / voice: an invasion and
  meta: kind=partial | timestamp=1777947829.0370357 | source=windows | frequency_hz=153.8 | rms=402 | updated_at=1777947827.4893472
- [2026-05-05 10:23:49] operator / voice_transcript_partial / voice: an invasion and the
  meta: kind=partial | timestamp=1777947829.854782 | source=windows | frequency_hz=153.8 | rms=402 | updated_at=1777947827.4893472
- [2026-05-05 10:23:50] operator / voice_transcript_partial / voice: an invasion and connect
  meta: kind=partial | timestamp=1777947830.0659683 | source=windows | frequency_hz=153.8 | rms=402 | updated_at=1777947827.4893472
- [2026-05-05 10:23:50] operator / voice_transcript_partial / voice: an invasion and connected
  meta: kind=partial | timestamp=1777947830.2657175 | source=windows | frequency_hz=153.8 | rms=402 | updated_at=1777947827.4893472
- [2026-05-05 10:23:50] operator / voice_transcript_partial / voice: an invasion and connectivity
  meta: kind=partial | timestamp=1777947830.4671597 | source=windows | frequency_hz=153.8 | rms=402 | updated_at=1777947827.4893472
- [2026-05-05 10:23:50] operator / voice_transcript_partial / voice: an invasion and connected and a
  meta: kind=partial | timestamp=1777947830.6793213 | source=windows | frequency_hz=371.1 | rms=3819 | updated_at=1777947830.5559244
- [2026-05-05 10:23:51] operator / voice_transcript_partial / voice: an invasion and connected and able
  meta: kind=partial | timestamp=1777947831.0922682 | source=windows | frequency_hz=371.1 | rms=3819 | updated_at=1777947830.5559244
- [2026-05-05 10:23:51] operator / voice_transcript_partial / voice: an invasion and connected enables my
  meta: kind=partial | timestamp=1777947831.299163 | source=windows | frequency_hz=371.1 | rms=3819 | updated_at=1777947830.5559244
- [2026-05-05 10:23:51] operator / voice_transcript_partial / voice: an invasion and connected enables marks
  meta: kind=partial | timestamp=1777947831.4991488 | source=windows | frequency_hz=371.1 | rms=3819 | updated_at=1777947830.5559244
- [2026-05-05 10:23:51] operator / voice_transcript_partial / voice: an invasion and connected enables marks entry
  meta: kind=partial | timestamp=1777947831.7011383 | source=windows | frequency_hz=320.5 | rms=1537 | updated_at=1777947831.5735295
- [2026-05-05 10:23:52] operator / voice_transcript_final / voice: an invasion and connected enables marks entry
  meta: kind=final | timestamp=1777947832.5170941 | source=final | confidence=0.34 | frequency_hz=201.4 | rms=169 | updated_at=1777947832.4734259
- [2026-05-05 10:23:52] operator / voice_command / voice: an invasion and connected enables marks entry
  meta: normalized=True
- [2026-05-05 10:23:54] assistant / spoken_confirmation / voice: I think I heard an invasion and connected enables marks entry. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=True
- [2026-05-05 10:23:57] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777947837.9707403 | source=windows | frequency_hz=165.0 | rms=139 | updated_at=1777947837.2138526
- [2026-05-05 10:23:58] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777947838.175421 | source=windows | frequency_hz=165.0 | rms=139 | updated_at=1777947837.2138526
- [2026-05-05 10:23:58] operator / voice_transcript_partial / voice: that
  meta: kind=partial | timestamp=1777947838.3806076 | source=windows | frequency_hz=165.0 | rms=139 | updated_at=1777947837.2138526
- [2026-05-05 10:23:58] operator / voice_transcript_partial / voice: bad
  meta: kind=partial | timestamp=1777947838.5956285 | source=windows | frequency_hz=165.0 | rms=139 | updated_at=1777947837.2138526
- [2026-05-05 10:23:59] operator / voice_transcript_partial / voice: than
  meta: kind=partial | timestamp=1777947839.0149934 | source=windows | frequency_hz=165.0 | rms=139 | updated_at=1777947837.2138526
- [2026-05-05 10:24:00] operator / voice_transcript_final / voice: than
  meta: kind=final | timestamp=1777947840.2443957 | source=final | confidence=0.43 | frequency_hz=165.0 | rms=139 | updated_at=1777947837.2138526
- [2026-05-05 10:24:02] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777947842.0822163 | source=windows | frequency_hz=258.8 | rms=137 | updated_at=1777947841.3034618
- [2026-05-05 10:24:02] operator / voice_transcript_partial / voice: an
  meta: kind=partial | timestamp=1777947842.7095785 | source=windows | frequency_hz=258.8 | rms=137 | updated_at=1777947841.3034618
- [2026-05-05 10:24:03] operator / voice_transcript_final / voice: an
  meta: kind=final | timestamp=1777947843.1171832 | source=final | confidence=0.23 | frequency_hz=258.8 | rms=137 | updated_at=1777947841.3034618
- [2026-05-05 10:24:06] operator / voice_transcript_partial / voice: hour
  meta: kind=partial | timestamp=1777947846.587314 | source=windows | frequency_hz=230.9 | rms=147 | updated_at=1777947844.894151
- [2026-05-05 10:24:06] operator / voice_transcript_partial / voice: connect
  meta: kind=partial | timestamp=1777947846.7906523 | source=windows | frequency_hz=296.9 | rms=193 | updated_at=1777947846.685117
- [2026-05-05 10:24:07] operator / voice_transcript_partial / voice: connect the
  meta: kind=partial | timestamp=1777947847.1960351 | source=windows | frequency_hz=296.9 | rms=193 | updated_at=1777947846.685117
- [2026-05-05 10:24:07] operator / voice_transcript_partial / voice: connector and
  meta: kind=partial | timestamp=1777947847.398453 | source=windows | frequency_hz=296.9 | rms=193 | updated_at=1777947846.685117
- [2026-05-05 10:24:07] operator / voice_transcript_partial / voice: clinic that ended
  meta: kind=partial | timestamp=1777947847.601721 | source=windows | frequency_hz=296.9 | rms=193 | updated_at=1777947846.685117
- [2026-05-05 10:24:07] operator / voice_transcript_partial / voice: correct a n. n.
  meta: kind=partial | timestamp=1777947847.805655 | source=windows | frequency_hz=296.9 | rms=193 | updated_at=1777947846.685117
- [2026-05-05 10:24:08] operator / voice_transcript_partial / voice: connector and enable
  meta: kind=partial | timestamp=1777947848.2136576 | source=windows | frequency_hz=313.3 | rms=2341 | updated_at=1777947847.9633389
- [2026-05-05 10:24:08] operator / voice_transcript_partial / voice: clinic that had been able
  meta: kind=partial | timestamp=1777947848.4159997 | source=windows | frequency_hz=313.3 | rms=2341 | updated_at=1777947847.9633389
- [2026-05-05 10:24:08] operator / voice_transcript_partial / voice: connector and enabled us
  meta: kind=partial | timestamp=1777947848.6242573 | source=windows | frequency_hz=313.3 | rms=2341 | updated_at=1777947847.9633389
- [2026-05-05 10:24:08] operator / voice_transcript_partial / voice: connector and enabled smart
  meta: kind=partial | timestamp=1777947848.838489 | source=windows | frequency_hz=313.3 | rms=2341 | updated_at=1777947847.9633389
- [2026-05-05 10:24:09] operator / voice_transcript_partial / voice: connector and enabled smart said
  meta: kind=partial | timestamp=1777947849.0457902 | source=windows | frequency_hz=313.3 | rms=2341 | updated_at=1777947847.9633389
- [2026-05-05 10:24:09] operator / voice_transcript_partial / voice: connector and enabled some arts center
  meta: kind=partial | timestamp=1777947849.4529285 | source=windows | frequency_hz=277.5 | rms=172 | updated_at=1777947849.3736615
- [2026-05-05 10:24:09] operator / voice_transcript_partial / voice: connector and enabled smarts entry
  meta: kind=partial | timestamp=1777947849.6550384 | source=windows | frequency_hz=277.5 | rms=172 | updated_at=1777947849.3736615
- [2026-05-05 10:24:10] operator / voice_transcript_final / voice: enable smart sentry
  meta: kind=final | timestamp=1777947850.0664124 | source=final | confidence=0.53 | frequency_hz=277.5 | rms=172 | updated_at=1777947849.3736615
- [2026-05-05 10:24:10] operator / voice_command / voice: enable smart sentry
  meta: normalized=True
- [2026-05-05 10:24:11] assistant / spoken_confirmation / voice: No confirmation received. I did not run an invasion and connected enables marks entry.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 10:24:11] assistant / spoken_confirmation / voice: I think I heard enable smart sentry. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 10:24:13] operator / voice_transcript_partial / voice: from
  meta: kind=partial | timestamp=1777947853.5374618 | source=windows | frequency_hz=277.5 | rms=172 | updated_at=1777947849.3736615
- [2026-05-05 10:24:13] operator / voice_transcript_partial / voice: in
  meta: kind=partial | timestamp=1777947853.9432094 | source=windows | frequency_hz=277.5 | rms=172 | updated_at=1777947849.3736615
- [2026-05-05 10:24:14] operator / voice_transcript_final / voice: scene
  meta: kind=final | timestamp=1777947854.3567383 | source=final | confidence=0.69 | frequency_hz=277.5 | rms=172 | updated_at=1777947849.3736615
- [2026-05-05 10:24:14] operator / voice_command / voice: scene
  meta: normalized=True
- [2026-05-05 10:24:14] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777947854.9654589 | source=windows | frequency_hz=277.5 | rms=172 | updated_at=1777947849.3736615
- [2026-05-05 10:24:15] operator / voice_transcript_final / voice: and
  meta: kind=final | timestamp=1777947855.585492 | source=final | confidence=0.62 | frequency_hz=277.5 | rms=172 | updated_at=1777947849.3736615
- [2026-05-05 10:24:15] operator / voice_command / voice: and
  meta: normalized=True
- [2026-05-05 10:24:17] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 10:24:17] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 10:24:17] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777947857.818569 | source=windows | frequency_hz=292.3 | rms=11811 | updated_at=1777947857.6935318
- [2026-05-05 10:24:18] operator / voice_transcript_partial / voice: clinic
  meta: kind=partial | timestamp=1777947858.031619 | source=windows | frequency_hz=292.3 | rms=11811 | updated_at=1777947857.6935318
- [2026-05-05 10:24:18] operator / voice_transcript_partial / voice: connect the
  meta: kind=partial | timestamp=1777947858.2330773 | source=windows | frequency_hz=292.5 | rms=605 | updated_at=1777947858.2057552
- [2026-05-05 10:24:18] operator / voice_transcript_partial / voice: connect the board
  meta: kind=partial | timestamp=1777947858.2330773 | source=windows | frequency_hz=292.5 | rms=605 | updated_at=1777947858.2057552
- [2026-05-05 10:24:18] operator / voice_transcript_partial / voice: connect the boards
  meta: kind=partial | timestamp=1777947858.4353456 | source=windows | frequency_hz=248.9 | rms=279 | updated_at=1777947858.3363786
- [2026-05-05 10:24:18] operator / voice_transcript_final / voice: connect boards
  meta: kind=final | timestamp=1777947858.872961 | source=final | confidence=0.73 | frequency_hz=226.0 | rms=167 | updated_at=1777947858.58432
- [2026-05-05 10:24:18] operator / voice_command / voice: connect boards
  meta: normalized=True
- [2026-05-05 10:24:19] operator / voice_transcript_partial / voice: see
  meta: kind=partial | timestamp=1777947859.673322 | source=windows | frequency_hz=226.0 | rms=167 | updated_at=1777947858.58432
- [2026-05-05 10:24:19] operator / voice_transcript_partial / voice: seen
  meta: kind=partial | timestamp=1777947859.876434 | source=windows | frequency_hz=226.0 | rms=167 | updated_at=1777947858.58432
- [2026-05-05 10:24:20] operator / voice_transcript_final / voice: seen
  meta: kind=final | timestamp=1777947860.4925563 | source=final | confidence=0.71 | frequency_hz=136.7 | rms=153 | updated_at=1777947859.9939456
- [2026-05-05 10:24:20] operator / voice_command / voice: seen
  meta: normalized=True
- [2026-05-05 10:24:20] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777947860.8937104 | source=windows | frequency_hz=228.3 | rms=245 | updated_at=1777947860.5075712
- [2026-05-05 10:24:21] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777947861.9289036 | source=final | confidence=0.15 | frequency_hz=291.9 | rms=747 | updated_at=1777947861.534036
- [2026-05-05 10:24:22] operator / voice_transcript_partial / voice: go
  meta: kind=partial | timestamp=1777947862.783814 | source=windows | frequency_hz=290.8 | rms=3435 | updated_at=1777947862.684213
- [2026-05-05 10:24:22] operator / voice_transcript_partial / voice: code
  meta: kind=partial | timestamp=1777947862.783814 | source=windows | frequency_hz=290.8 | rms=3435 | updated_at=1777947862.684213
- [2026-05-05 10:24:22] operator / voice_transcript_partial / voice: clinic
  meta: kind=partial | timestamp=1777947862.785316 | source=windows | frequency_hz=290.8 | rms=3435 | updated_at=1777947862.684213
- [2026-05-05 10:24:23] operator / voice_transcript_partial / voice: clinic that
  meta: kind=partial | timestamp=1777947863.2082765 | source=windows | frequency_hz=290.8 | rms=3435 | updated_at=1777947862.684213
- [2026-05-05 10:24:23] operator / voice_transcript_partial / voice: connect the board
  meta: kind=partial | timestamp=1777947863.4085038 | source=windows | frequency_hz=290.8 | rms=3435 | updated_at=1777947862.684213
- [2026-05-05 10:24:23] operator / voice_transcript_partial / voice: connect the boards
  meta: kind=partial | timestamp=1777947863.615168 | source=windows | frequency_hz=236.2 | rms=321 | updated_at=1777947863.5745208
- [2026-05-05 10:24:24] operator / voice_transcript_final / voice: connect boards
  meta: kind=final | timestamp=1777947864.0207822 | source=final | confidence=0.88 | frequency_hz=236.2 | rms=321 | updated_at=1777947863.5745208
- [2026-05-05 10:24:24] operator / voice_command / voice: connect boards
  meta: normalized=True
- [2026-05-05 10:24:25] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 10:24:25] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 10:24:25] assistant / spoken_confirmation / voice: Please say yes, say the command again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 10:24:27] operator / voice_transcript_partial / voice: new
  meta: kind=partial | timestamp=1777947867.918394 | source=windows | frequency_hz=236.2 | rms=321 | updated_at=1777947863.5745208
- [2026-05-05 10:24:27] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777947867.918394 | source=windows | frequency_hz=236.2 | rms=321 | updated_at=1777947863.5745208
- [2026-05-05 10:24:28] operator / voice_transcript_final / voice: one
  meta: kind=final | timestamp=1777947868.5343413 | source=final | confidence=0.19 | frequency_hz=236.2 | rms=321 | updated_at=1777947863.5745208
- [2026-05-05 10:24:30] operator / voice_transcript_partial / voice: of the
  meta: kind=partial | timestamp=1777947870.3624127 | source=windows | frequency_hz=236.2 | rms=321 | updated_at=1777947863.5745208
- [2026-05-05 10:24:30] operator / voice_transcript_partial / voice: that gave
  meta: kind=partial | timestamp=1777947870.5673933 | source=windows | frequency_hz=236.2 | rms=321 | updated_at=1777947863.5745208
- [2026-05-05 10:24:30] operator / voice_transcript_partial / voice: of the book
  meta: kind=partial | timestamp=1777947870.7710369 | source=windows | frequency_hz=236.2 | rms=321 | updated_at=1777947863.5745208
- [2026-05-05 10:24:31] operator / voice_transcript_partial / voice: and a book about
  meta: kind=partial | timestamp=1777947871.1780646 | source=windows | frequency_hz=375.0 | rms=216 | updated_at=1777947871.1340055
- [2026-05-05 10:24:31] operator / voice_transcript_final / voice: and a book about
  meta: kind=final | timestamp=1777947871.8041067 | source=final | confidence=0.25 | frequency_hz=375.0 | rms=216 | updated_at=1777947871.1340055
- [2026-05-05 10:24:31] operator / voice_command / voice: and a book about
  meta: normalized=True
- [2026-05-05 10:24:33] assistant / spoken_confirmation / voice: I think I heard and a book about. Say yes if that is correct, say it again, or say cancel.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 10:24:36] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777947876.2854326 | source=windows | frequency_hz=357.2 | rms=121 | updated_at=1777947874.0744147
- [2026-05-05 10:24:36] operator / voice_transcript_partial / voice: one
  meta: kind=partial | timestamp=1777947876.2854326 | source=windows | frequency_hz=357.2 | rms=121 | updated_at=1777947874.0744147
- [2026-05-05 10:24:36] operator / voice_transcript_final / voice: one
  meta: kind=final | timestamp=1777947876.8955507 | source=final | confidence=0.29 | frequency_hz=357.2 | rms=121 | updated_at=1777947874.0744147
- [2026-05-05 10:24:44] operator / voice_transcript_partial / voice: a
  meta: kind=partial | timestamp=1777947884.2923207 | source=windows | frequency_hz=269.5 | rms=163 | updated_at=1777947884.183747
- [2026-05-05 10:24:44] operator / voice_transcript_partial / voice: are you
  meta: kind=partial | timestamp=1777947884.4966905 | source=windows | frequency_hz=269.5 | rms=163 | updated_at=1777947884.183747
- [2026-05-05 10:24:44] operator / voice_transcript_partial / voice: are you the
  meta: kind=partial | timestamp=1777947884.70091 | source=windows | frequency_hz=269.5 | rms=163 | updated_at=1777947884.183747
- [2026-05-05 10:24:44] operator / voice_transcript_partial / voice: are you use the
  meta: kind=partial | timestamp=1777947884.9037569 | source=windows | frequency_hz=269.5 | rms=163 | updated_at=1777947884.183747
- [2026-05-05 10:24:45] operator / voice_transcript_partial / voice: are you wasting your
  meta: kind=partial | timestamp=1777947885.1093335 | source=windows | frequency_hz=269.5 | rms=163 | updated_at=1777947884.183747
- [2026-05-05 10:24:45] operator / voice_transcript_partial / voice: are you wasting a lot
  meta: kind=partial | timestamp=1777947885.5149198 | source=windows | frequency_hz=299.4 | rms=5723 | updated_at=1777947885.463621
- [2026-05-05 10:24:45] operator / voice_transcript_partial / voice: are you wasting your
  meta: kind=partial | timestamp=1777947885.7182646 | source=windows | frequency_hz=291.7 | rms=3749 | updated_at=1777947885.5945477
- [2026-05-05 10:24:45] operator / voice_transcript_partial / voice: are you wasting your room
  meta: kind=partial | timestamp=1777947885.921196 | source=windows | frequency_hz=327.7 | rms=491 | updated_at=1777947885.8543487
- [2026-05-05 10:24:46] operator / voice_transcript_final / voice: are you wasting your room
  meta: kind=final | timestamp=1777947886.7466874 | source=final | confidence=0.31 | frequency_hz=318.6 | rms=179 | updated_at=1777947886.4947784
- [2026-05-05 10:24:49] assistant / spoken_confirmation / voice: No confirmation received. I did not run and a book about.
  meta: interrupt=False | assistant_output=False | spoken=False
- [2026-05-05 10:24:52] operator / voice_transcript_partial / voice: to
  meta: kind=partial | timestamp=1777947892.5262039 | source=windows | frequency_hz=314.7 | rms=183 | updated_at=1777947891.8084223
- [2026-05-05 10:24:52] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777947892.743721 | source=windows | frequency_hz=314.7 | rms=183 | updated_at=1777947891.8084223
- [2026-05-05 10:24:53] operator / voice_transcript_partial / voice: and he
  meta: kind=partial | timestamp=1777947893.7680292 | source=windows | frequency_hz=361.7 | rms=186 | updated_at=1777947893.7245939
- [2026-05-05 10:24:53] operator / voice_transcript_partial / voice: and move
  meta: kind=partial | timestamp=1777947893.7680292 | source=windows | frequency_hz=361.7 | rms=186 | updated_at=1777947893.7245939
- [2026-05-05 10:24:54] operator / voice_transcript_final / voice: and move
  meta: kind=final | timestamp=1777947894.3915246 | source=final | confidence=0.46 | frequency_hz=269.9 | rms=186 | updated_at=1777947894.3643394
- [2026-05-05 10:25:04] operator / voice_transcript_partial / voice: them
  meta: kind=partial | timestamp=1777947904.4439404 | source=windows | frequency_hz=282.2 | rms=199 | updated_at=1777947904.3462625
- [2026-05-05 10:25:08] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777947908.3415248 | source=windows | frequency_hz=177.7 | rms=192 | updated_at=1777947907.5449288
- [2026-05-05 10:25:08] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777947908.74832 | source=windows | frequency_hz=179.8 | rms=196 | updated_at=1777947908.5650935
- [2026-05-05 10:25:08] operator / voice_transcript_partial / voice: them
  meta: kind=partial | timestamp=1777947908.74832 | source=windows | frequency_hz=179.8 | rms=196 | updated_at=1777947908.5650935
- [2026-05-05 10:25:09] operator / voice_transcript_final / voice: them
  meta: kind=final | timestamp=1777947909.1535842 | source=final | confidence=0.01 | frequency_hz=179.8 | rms=196 | updated_at=1777947908.5650935
- [2026-05-05 10:25:21] operator / voice_transcript_partial / voice: and
  meta: kind=partial | timestamp=1777947921.310549 | source=windows | frequency_hz=343.1 | rms=197 | updated_at=1777947921.1849291
- [2026-05-05 10:25:22] operator / voice_transcript_final / voice: and
  meta: kind=final | timestamp=1777947922.1941915 | source=final | confidence=0.23 | frequency_hz=291.0 | rms=198 | updated_at=1777947921.9599004
- [2026-05-05 10:25:30] operator / voice_transcript_partial / voice: the
  meta: kind=partial | timestamp=1777947930.3297415 | source=windows | frequency_hz=215.5 | rms=204 | updated_at=1777947930.2749643
- [2026-05-05 10:25:31] operator / voice_transcript_final / voice: the
  meta: kind=final | timestamp=1777947931.1707053 | source=final | confidence=0.14 | frequency_hz=215.5 | rms=204 | updated_at=1777947930.2749643
- [2026-05-05 10:25:59] operator / voice_transcript_partial / voice: author of the
  meta: kind=partial | timestamp=1777947959.1322732 | source=windows | frequency_hz=218.8 | rms=201 | updated_at=1777947956.895001
- [2026-05-05 10:26:00] operator / voice_transcript_final / voice: author of the
  meta: kind=final | timestamp=1777947960.2757068 | source=final | confidence=0.04 | frequency_hz=279.9 | rms=203 | updated_at=1777947960.2265067
- [2026-05-05 10:26:08] operator / voice_transcript_partial / voice: thought of
  meta: kind=partial | timestamp=1777947968.875627 | source=windows | frequency_hz=308.8 | rms=203 | updated_at=1777947965.216008
- [2026-05-05 10:26:09] operator / voice_transcript_partial / voice: thought of the
  meta: kind=partial | timestamp=1777947969.2823024 | source=windows | frequency_hz=308.8 | rms=203 | updated_at=1777947965.216008
- [2026-05-05 10:26:09] operator / voice_transcript_partial / voice: thought of
  meta: kind=partial | timestamp=1777947969.6974967 | source=windows | frequency_hz=308.8 | rms=203 | updated_at=1777947965.216008
- [2026-05-05 10:26:09] operator / voice_transcript_partial / voice: thought of the
  meta: kind=partial | timestamp=1777947969.8925757 | source=windows | frequency_hz=308.8 | rms=203 | updated_at=1777947965.216008
- [2026-05-05 10:26:10] operator / voice_transcript_partial / voice: thought of
  meta: kind=partial | timestamp=1777947970.0952768 | source=windows | frequency_hz=308.8 | rms=203 | updated_at=1777947965.216008
- [2026-05-05 10:26:10] operator / voice_transcript_partial / voice: things that
  meta: kind=partial | timestamp=1777947970.5022435 | source=windows | frequency_hz=308.8 | rms=203 | updated_at=1777947965.216008
- [2026-05-05 10:26:11] operator / voice_transcript_partial / voice: thought that the
  meta: kind=partial | timestamp=1777947971.7635968 | source=windows | frequency_hz=308.8 | rms=203 | updated_at=1777947965.216008
- [2026-05-05 10:26:12] operator / voice_transcript_final / voice: thought that the
  meta: kind=final | timestamp=1777947972.38074 | source=final | confidence=0.05 | frequency_hz=308.8 | rms=203 | updated_at=1777947965.216008
